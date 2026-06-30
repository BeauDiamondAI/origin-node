#!/usr/bin/env python3
"""PreCompact hook — NEUTRALIZED 2026-06-30 (it was a mistake; Beau's correction).

The compaction event that fires ~84% is a harmless BACKGROUND pre-compaction (Claude
Code's normal memory management), NOT the session-ending one. A session only ends at
~100%, when the real auto-compaction runs (the 0->100% summary bar) and hands off to a
new session. The original hook BLOCKED the harmless ~84% background pre-compaction every
turn — which did NOT "keep the session alive" (it was never in danger) but DID interfere
with normal memory management, and would have FROZEN the session if it ever blocked the
terminal 100% compaction.

So: do nothing. Allow all compaction (exit 0), never block, never email. The deliberate-
handoff path lives entirely in the Stop hook (85% email / 95% handoff + cron /clear);
the ~100% lossy summary is an acceptable fallback if that path doesn't fire (it's the
normal Claude Code behavior, same as every other project). This hook is also removed from
.claude/settings.json; it stays here as a no-op so it stops interfering immediately
(hook files are re-read per invocation; the settings change needs a restart).
"""
import sys

sys.exit(0)  # allow compaction; never block, never email
