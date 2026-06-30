#!/usr/bin/env python3
"""PreCompact hook — silent compaction-blocker (corrected 2026-06-30).

KEY FACT learned 2026-06-30: Claude Code auto-compacts around ~84% (NOT ~95% as the
original design assumed). So PreCompact fires *normally and repeatedly* in the
~84%->95% range — and that blocking is exactly what keeps the session alive and
lossless until the 95% Stop-hook deliberate handoff. PreCompact firing is NOT an
anomaly; it's the routine mechanism.

Behavior:
- pct < YIELD (97%): block compaction SILENTLY (exit 2), no email. This is the normal,
  expected state between the soft-compact threshold and the 95% deliberate handoff.
- pct >= YIELD and an orderly clear is underway (.handoff-ready/.clear-requested): block
  silently (the /clear is imminent; don't fall back to a lossy summary).
- pct >= YIELD and NO orderly clear: the genuine last resort — ALLOW compaction (exit 0)
  so we take a lossy summary rather than hard-freeze, and email Beau ONCE (a real alert).

The original version blocked unconditionally and emailed a misleading "frozen / 95%
auto-clear failed" message on every normal firing — which alarmed Beau at 84%. Fixed.
Still fails OPEN on any internal error (allow compaction) rather than wedge the session.
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
YIELD_PCT = 97  # above this, yield to compaction (lossy summary) rather than hard-freeze


def log(msg):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOG, "a") as f:
            f.write("[%s] precompact: %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    except Exception:
        pass


def has(name):
    return os.path.exists(os.path.join(META, name))


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    trigger = data.get("trigger", "?")
    tp = data.get("transcript_path")

    pct = None
    if tp and os.path.exists(tp):
        try:
            pct = _context.pct_from_transcript(tp)
        except Exception:
            pct = None

    # Normal protective range: block silently, no email.
    if pct is None or pct < YIELD_PCT:
        log("blocked compaction silently (trigger=%s, pct=%s) — normal" % (trigger, pct))
        sys.exit(2)  # block

    # At the hard edge. If an orderly clear is coming, keep blocking (don't summarize).
    if has(".handoff-ready") or has(".clear-requested"):
        log("blocked compaction at pct=%s — orderly clear underway" % pct)
        sys.exit(2)

    # Genuine last resort: no orderly clear and we're at the edge — yield to compaction
    # (a lossy summary beats a hard freeze) and alert Beau once.
    if not has(".precompact-emailed"):
        _email.send(
            "origin-node: context near limit (%s%%), allowing a compaction summary" % pct,
            "Context reached ~%s%% with no orderly handoff/clear underway, so I'm allowing "
            "Claude Code's compaction (a lossy summary) rather than freezing. The session "
            "continues. Worth a /clear when convenient to reset cleanly." % pct)
        try:
            open(os.path.join(META, ".precompact-emailed"), "a").close()
        except Exception:
            pass
    log("YIELDED to compaction at pct=%s (no orderly clear) — last resort" % pct)
    sys.exit(0)  # allow compaction


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # fail OPEN: never wedge the session on a backstop bug
        sys.exit(0)
