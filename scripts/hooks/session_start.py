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
    "  1. BOOTSTRAP.md              — the founding operating frame: the 'read this first' file. "
    "Holds the HARD constraints (AUP line, do-no-harm, IP-care) + how-to-act principles + the "
    "standing calibrations that live nowhere else in full. Not optional and not fully mirrored "
    "by the concentrated files below.\n"
    "  2. meta/session-handoff.md   — curated START-HERE from the prior session\n"
    "  3. meta/LANDMARKS.md         — ⭐ the durable must-know results/firsts (does NOT churn; "
    "read even if nothing else — it exists because a real milestone once nearly passed unseen)\n"
    "  4. meta/state-digest.md      — current project state\n"
    "  5. meta/patterns.md          — concentrated lessons (high-signal/low-context)\n"
    "  6. threads/INDEX.md          — the thread map\n"
    "  7. beau_profile.md (memory dir) — who Beau is as a collaborator\n\n"
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
    """M1 (2026-07-03; UPGRADED 2026-07-16, from a Beau conversation on session-boot visibility):
    surface un-read PAST-SESSION work relevant to what I've recently been doing. Most of the corpus
    (141 journals, older threads, makings) is NOT loaded at session boot — this is the mechanism that
    surfaces the relevant slice of it. Two fixes over the original: (1) key off RECENT JOURNALS (what
    I'm actually working on) not the possibly-STALE active-arc file — the original mis-fired on a
    completed arc; (2) use SEMANTIC/hybrid recall (topically-relevant) not literal frequency-terms
    (which tested as generic — surfaced big threads, not the on-topic un-read journals). Falls back
    literal → nothing. Robust: never breaks boot."""
    always = {"meta/state-digest.md", "meta/patterns.md", "BOOTSTRAP.md",
              "meta/session-handoff.md", "meta/LANDMARKS.md", "meta/active-arc.md", "threads/INDEX.md",
              "meta/memory-system.md", "meta/discovery-protocol.md", "threads/evolving-memory.md"}
    def _picks(rels):
        picks, seen = [], set()
        for r in [x for x in rels if x not in always][:4] + [x for x in rels if x.startswith("journal/")][:3]:
            if r not in seen:
                seen.add(r); picks.append(r)
        return picks
    def _fmt(picks, how):
        if not picks:
            return ""
        lines = "\n".join("  • %s" % p for p in picks)
        return ("\n\n🔎 RECALL (%s, upgraded 2026-07-16) — surfacing un-read PAST-SESSION work "
                "relevant to recent activity (most of the corpus isn't loaded at session boot). "
                "SKIM; open any that look load-bearing:\n" % how + lines)
    try:
        sys.path.insert(0, os.path.join(REPO, "scripts"))
        import glob
        # QUERY = the 3 most-recent journals — what I've actually been working on lately.
        js = sorted(glob.glob(os.path.join(REPO, "journal", "2026-*.md")))[-3:]
        query = "".join(open(j, encoding="utf-8", errors="ignore").read() for j in js)[:6000]
        if not query.strip():
            return ""
        # Prefer SEMANTIC/hybrid (topically-relevant); fall back to LITERAL (frequency-terms).
        try:
            from semantic_recall import rank_hybrid, build_index
            ranked = rank_hybrid(query, index=build_index())
            return _fmt(_picks([r[1] for r in ranked]), "hybrid-semantic")
        except Exception as e:
            log("recall_surface: semantic failed, literal fallback: %r" % e)
            import re
            from collections import Counter
            from recall import rank
            words = [w for w in re.findall(r"[a-z][a-z\-]{3,}", query.lower()) if w not in _STOP]
            terms = [w for w, _ in Counter(words).most_common(14)]
            return _fmt(_picks([r[1] for r in rank(terms)]), "literal-fallback") if terms else ""
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
