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
cat >> "$f"
echo "appended to temp/beau-briefings/${d}.md"
