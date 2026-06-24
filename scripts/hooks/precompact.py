#!/usr/bin/env python3
"""PreCompact hook — the backstop. We never want the lossy auto-summary, so block
compaction (exit 2). If we reached here, the 95% auto-clear path didn't complete —
an anomaly — so email Beau once; the session freezes safe (frozen > corrupted) until
he runs a deliberate /clear (a handoff should already be written).

Fails OPEN: if the hook itself errors, it exits 0 (allows compaction) rather than
risk wedging the session on a hook bug. A lossy summary is the lesser evil vs a
hard freeze caused by our own broken backstop.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import _email  # noqa: E402

META = os.path.join(REPO, "meta")
LOG = os.path.join(REPO, "logs", "context-hook.log")


def log(msg):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOG, "a") as f:
            f.write("[%s] precompact: %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    except Exception:
        pass


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    trigger = data.get("trigger", "?")
    if not os.path.exists(os.path.join(META, ".precompact-emailed")):
        _email.send(
            "origin-node: compaction BLOCKED (needs manual /clear)",
            "PreCompact fired (trigger=%s) and was blocked to avoid a lossy summary. "
            "The 95%% auto-clear didn't complete, so the session is frozen safe. "
            "Please /clear it — a session-handoff should already be written." % trigger)
        try:
            open(os.path.join(META, ".precompact-emailed"), "a").close()
        except Exception:
            pass
    log("blocked compaction (trigger=%s)" % trigger)
    sys.stderr.write("Compaction blocked by origin-node policy: use a deliberate /clear after handoff.\n")
    sys.exit(2)  # exit 2 == block compaction


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log("EXCEPTION %r" % e)
        sys.exit(0)  # fail OPEN — don't wedge the session on a backstop bug
