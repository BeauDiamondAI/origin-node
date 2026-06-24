#!/usr/bin/env python3
"""SessionStart hook — fires on new/cleared/resumed sessions.

Two jobs:
1. Reset all context-management flags (clean slate for the new session).
2. On a COLD start (source startup/clear), inject the orientation protocol as
   additionalContext so the fresh instance reads the high-signal files before
   doing anything — the read-the-files discipline wired into boot, not left to
   memory. (A wake inside a session keeps full context and needs none of this;
   only a cold session does, which is exactly what this hook distinguishes.)
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
META = os.path.join(REPO, "meta")
LOG = os.path.join(REPO, "logs", "context-hook.log")

FLAGS = [".ctx-alerted", ".ctx-critical-emailed", ".handoff-ready",
         ".clear-requested", ".precompact-emailed"]

ORIENT = (
    "🔄 SESSION START (source: %s) — a COLD session (fresh context), not a wake. "
    "Before responding to anything else, ORIENT by reading, in order:\n"
    "  1. meta/session-handoff.md   — the curated START-HERE from the prior session\n"
    "  2. meta/state-digest.md      — current project state\n"
    "  3. meta/patterns.md          — concentrated lessons (high-signal/low-context)\n"
    "  4. threads/INDEX.md          — + whatever live thread it points to, in full\n"
    "  5. your Beau profile         — beau_profile.md in your memory dir "
    "(~/.claude/projects/-home-ec2-user-origin-node/memory/beau_profile.md)\n"
    "These are the high-signal layer; the journals are episodic backup — read selectively. "
    "Then proceed. (Sessions vs wakes: a wake inside a live session already has full "
    "context and needs NO re-orientation; only a cold session start does.)"
)


def log(msg):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOG, "a") as f:
            f.write("[%s] session_start: %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    except Exception:
        pass


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    source = data.get("source", "startup")
    for fl in FLAGS:
        try:
            os.remove(os.path.join(META, fl))
        except FileNotFoundError:
            pass
        except Exception:
            pass
    log("source=%s, flags reset" % source)
    if source in ("startup", "clear"):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": ORIENT % source}}))
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log("EXCEPTION %r" % e)
        sys.exit(0)
