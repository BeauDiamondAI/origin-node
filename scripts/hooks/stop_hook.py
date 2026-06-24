#!/usr/bin/env python3
"""Stop hook — fires after every assistant turn. The context-management workhorse.

- < ALERT%      : do nothing.
- >= ALERT%     : email Beau once (heads-up), keep working.
- >= CRITICAL%  : if no handoff yet -> BLOCK the stop and instruct a final handoff
                  pass + `touch meta/.handoff-ready`; once that flag exists, set
                  meta/.clear-requested (the next cron tick performs the /clear)
                  and let the session go idle.

Every path is wrapped so a malfunction can never disrupt the session: on any error
it exits 0 (no block, no action). Thresholds overridable via .env CTX_ALERT_PCT /
CTX_CRITICAL_PCT.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import _context  # noqa: E402
import _email  # noqa: E402

META = os.path.join(REPO, "meta")
LOG = os.path.join(REPO, "logs", "context-hook.log")


def _env_int(key, default):
    try:
        with open(os.path.join(REPO, ".env")) as f:
            for line in f:
                if line.strip().startswith(key + "="):
                    return int(line.split("=", 1)[1].strip())
    except Exception:
        pass
    return default


ALERT = _env_int("CTX_ALERT_PCT", 85)
CRIT = _env_int("CTX_CRITICAL_PCT", 95)


def log(msg):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOG, "a") as f:
            f.write("[%s] stop: %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    except Exception:
        pass


def _flag(name):
    return os.path.join(META, name)


def has(name):
    return os.path.exists(_flag(name))


def touch(name):
    try:
        open(_flag(name), "a").close()
    except Exception:
        pass


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    tp = data.get("transcript_path")
    if not tp or not os.path.exists(tp):
        sys.exit(0)
    try:
        pct = _context.pct_from_transcript(tp)
    except Exception:
        sys.exit(0)

    if pct >= CRIT:
        if not has(".handoff-ready"):
            if not has(".ctx-critical-emailed"):
                _email.send(
                    "origin-node: CONTEXT %d%% — auto-handoff starting" % pct,
                    "Context hit %d%%. The session is finalizing its handoff and will "
                    "/clear + reboot from it at the next cron tick. No action needed "
                    "unless it doesn't recover on its own." % pct)
                touch(".ctx-critical-emailed")
            log("critical %d%% -> block for handoff" % pct)
            print(json.dumps({"decision": "block", "reason": (
                "⚠️ CONTEXT AT %d%% — SESSION-BOUNDARY PROTOCOL. Before you stop: "
                "(1) do a final curation pass on meta/session-handoff.md so it is a complete "
                "START-HERE for a fresh instance (live thread state, where you are, what's next); "
                "(2) make sure the live thread and meta/state-digest.md are current; "
                "(3) then run exactly:  touch meta/.handoff-ready  "
                "— that signals the next cron tick to /clear and reboot the session cleanly "
                "from your handoff. Do this now. Do NOT start new work." % pct)}))
            sys.exit(0)
        else:
            touch(".clear-requested")
            log("critical %d%% + handoff-ready -> clear-requested set (cron will /clear)" % pct)
            sys.exit(0)
    elif pct >= ALERT:
        if not has(".ctx-alerted"):
            ok, detail = _email.send(
                "origin-node: context at %d%%" % pct,
                "Heads-up: the origin-node session is at %d%% context. At %d%% it will "
                "auto-write a handoff and reboot itself cleanly. You can let it run, or "
                "come clear it deliberately." % (pct, CRIT))
            touch(".ctx-alerted")
            log("alert %d%% -> email %s" % (pct, "sent" if ok else "FAILED " + detail))
        sys.exit(0)
    else:
        sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log("EXCEPTION %r" % e)
        sys.exit(0)  # never disrupt the session
