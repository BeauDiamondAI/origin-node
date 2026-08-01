#!/bin/bash
# ledger.sh — append one terse line to journal/wake-ledger.md, with a length guard.
# Wired 2026-08-01 on direct evidence, not intent: after the meta-reflection cut ledger
# work-lines from 478w back to ~63w, they re-drifted 63→66→98→131 in FOUR wakes, unnoticed
# until inspected — while the GUARDED briefing was caught at 169w the same day. Guarded
# artifact caught; unguarded artifact drifted. BOOTSTRAP:285 — rhythm record, not mini-journal.
# Usage:  scripts/ledger.sh <<'EOF' ... EOF
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"; f="$root/journal/wake-ledger.md"
tmp=$(mktemp); cat > "$tmp"; cat "$tmp" >> "$f"
w=$(wc -w < "$tmp"); rm -f "$tmp"
echo "appended to journal/wake-ledger.md (${w} words)"
if [ "$w" -gt 90 ]; then
  echo "⚠️  LEDGER LINE OVER SPEC (${w}w). It is a rhythm record, not a mini-journal —"
  echo "    episodic detail belongs in journal/. Cut to one line + a pointer."
fi
