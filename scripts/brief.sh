#!/bin/bash
# brief.sh — append a Beau-briefing entry to TODAY's dated file, always.
# Operationalizes the per-date-file convention so it can't drift again: the path is
# COMPUTED from the date, never hardcoded (the 2026-07-18 drift was a hardcoded path
# reused from command-momentum, dumping 6 days into one misnamed file). Content on stdin.
#   Usage:  scripts/brief.sh <<'EOF'
#           ## HH:MMZ (headline)
#           ...body...
#           EOF
set -u
d=$(date -u +%Y-%m-%d)
dir="$(cd "$(dirname "$0")/.." && pwd)/temp/beau-briefings"
mkdir -p "$dir"
f="$dir/${d}.md"
[ -f "$f" ] || printf '# Beau briefing — %s\n' "$d" > "$f"
printf '\n' >> "$f"
tmp=$(mktemp); cat > "$tmp"; cat "$tmp" >> "$f"
w=$(wc -w < "$tmp"); rm -f "$tmp"
echo "appended to temp/beau-briefings/${d}.md (${w} words)"
# Point-of-use guard, added 2026-08-01 after a week-long silent violation:
# temp/beau-briefings/README.md specifies 2-4 sentences per wake and "skip the
# discipline reflection". That spec was violated 4-20x for a week because reading
# the README is not part of the loop -- running this script IS.
if [ "$w" -gt 140 ]; then
  echo "⚠️  BRIEFING OVER SPEC (${w}w). README says 2-4 sentences, and to SKIP the"
  echo "    discipline reflection. If this is method-talk rather than substance, cut it."
fi
