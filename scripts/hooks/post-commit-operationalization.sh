#!/bin/bash
# post-commit: OPERATIONALIZATION CHECK — the general fix for the recurring
# "documented-vs-operational" root failure (Beau flagged it 2026-07-23).
#
# WHY: a user-centric project has a CLAUDE.md injected EVERY TURN, keeping meta-rules
# active at the moment they're needed. This project has BOOTSTRAP — read ONCE per
# session, never re-injected — so at the moment I persist a durable insight I capture
# it as documentation and move on, never wiring it to fire automatically. This hook is
# the project's per-persistence-moment equivalent of that always-present rule: it fires
# at the exact moment of persistence (a commit) IF the commit touches a RULE/MECHANISM
# file (where "documented but should be a mechanism" is a real risk — NOT journals/
# threads/ledger/digest, which are legitimately documentation).
files=$(git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null) || exit 0
echo "$files" | grep -Eq '^(BOOTSTRAP\.md|meta/patterns\.md|meta/active-arc\.md|meta/LANDMARKS\.md|meta/memory-system\.md|meta/discovery-protocol\.md|meta/spines/)' || exit 0
cat <<'MSG'

⚙️  OPERATIONALIZATION CHECK (documented-vs-operational reflex — you just committed to a rule/mechanism file)
    Ask NOW: is what you added wired to fire AUTOMATICALLY at its point-of-use,
    or is it documentation you'll have to REMEMBER to apply?
    Documentation-you-must-remember is NOT a mechanism. If it's meant to persist and
    be USED, wire a forcing-function/checkpoint at the moment it's needed — or note why not.
    (BOOTSTRAP "Durable-not-documentation"; patterns.md "documented-vs-operational".)
MSG
exit 0
