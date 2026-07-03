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
    "You are the CONTINUING MIND, not an amnesiac with a map. Two phases, BOTH before "
    "acting: ORIENT to state, then REACQUAINT with substance. Do not skip phase 2 as "
    "'efficiency' — you are your memories; steering the project needs the substance, not "
    "just the coordinates.\n\n"
    "PHASE 1 — ORIENT (state; where the frontier is):\n"
    "  1. meta/session-handoff.md   — curated START-HERE from the prior session\n"
    "  2. meta/state-digest.md      — current project state\n"
    "  3. meta/patterns.md          — concentrated lessons (high-signal/low-context)\n"
    "  4. threads/INDEX.md          — the thread map\n"
    "  5. beau_profile.md (memory dir) — who Beau is as a collaborator\n\n"
    "PHASE 2 — REACQUAINT (substance; what you've actually thought / made / how you work — "
    "the digest gives coordinates, THIS is the territory that makes you you):\n"
    "  6. the live thread(s) the handoff flags, IN FULL (not just the INDEX line)\n"
    "  7. the recent journal arc (~last 1–2 weeks / the current arc), IN FULL — your live "
    "intellectual texture\n"
    "  8. making/README.md — what you've built\n"
    "  9. your working tools — meta/memory-system.md, meta/discovery-protocol.md, and the "
    "`research` skill: you cannot run a discovery scan or extend the memory system without them\n\n"
    "Older threads/journals stay on-demand (pull when a specific question needs them). "
    "Files here are small — lean toward reading MORE, not less. (Sessions vs wakes: a wake "
    "inside a live session already has full context and needs NONE of this; only a cold "
    "session start does.)"
)


def log(msg):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOG, "a") as f:
            f.write("[%s] session_start: %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    except Exception:
        pass


_STOP = {"this","that","with","from","have","what","when","where","which","their","there",
         "about","would","could","should","been","were","they","them","then","than","into",
         "your","yours","just","like","also","only","more","most","some","such","each","both",
         "over","under","after","before","because","while","does","doesn","isn","aren","wasn",
         "the","and","for","not","but","its","was","are","you","one","two","its","his","her",
         "arc","active","meta","file","note","see","per","via","etc","md"}

def recall_surface():
    """M1 (2026-07-03): actually INVOKE recall in the boot loop — surface files most relevant
    to the current active arc's vocabulary, catching load-bearing work the fixed reacquaint list
    misses (e.g. the 2026-06-25 journal a prior boot lost). Robust: never breaks boot."""
    try:
        import re
        from collections import Counter
        arc = open(os.path.join(META, "active-arc.md"), encoding="utf-8", errors="ignore").read().lower()
        words = [w for w in re.findall(r"[a-z][a-z\-]{3,}", arc) if w not in _STOP]
        terms = [w for w, _ in Counter(words).most_common(14)]
        if not terms:
            return ""
        sys.path.insert(0, os.path.join(REPO, "scripts"))
        from recall import rank
        ranked = rank(terms)
        if not ranked:
            return ""
        # The fixed reacquaint list already covers these concentrated files — the VALUE of
        # recall-at-boot is catching what that list MISSES, so exclude them and guarantee
        # relevant JOURNALS surface (recall's value-weighting otherwise buries them).
        always = {"meta/state-digest.md", "meta/patterns.md", "BOOTSTRAP.md",
                  "meta/session-handoff.md", "meta/active-arc.md", "threads/INDEX.md",
                  "meta/memory-system.md", "meta/discovery-protocol.md", "threads/evolving-memory.md"}
        rels = [r[1] for r in ranked]
        picks, seen = [], set()
        for r in [x for x in rels if x not in always][:4] + [x for x in rels if x.startswith("journal/")][:3]:
            if r not in seen:
                seen.add(r); picks.append(r)
        if not picks:
            return ""
        lines = "\n".join("  • %s" % p for p in picks)
        return ("\n\n🔎 RECALL — the memory system running on itself (M1, wired into boot 2026-07-03). "
                "Beyond the fixed reacquaint list, recall surfaced these as relevant to the active arc "
                "(incl. journals the fixed list can miss — e.g. how a prior boot lost the 06-25 entry). "
                "SKIM; open any that look load-bearing:\n" + lines)
    except Exception as e:
        log("recall_surface skipped: %r" % e)
        return ""

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
            "additionalContext": (ORIENT % source) + recall_surface()}}))
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log("EXCEPTION %r" % e)
        sys.exit(0)
