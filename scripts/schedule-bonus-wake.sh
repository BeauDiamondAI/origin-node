#!/bin/bash
# schedule-bonus-wake.sh — insert a one-time "bonus" wake at the midpoint between
# now and the next scheduled 6-hourly wake (00/06/12/18 UTC), via `at`.
#
# Purpose: an in-conversation exchange with Beau nearly always makes the *next*
# scheduled wake a brief exit (post-conversation saturation), so conversations
# "eat" a wake. This inserts an extra wake to compensate, spaced at the midpoint.
# Run it during/at the end of a conversation. Re-running just updates the pending
# bonus wake to the new midpoint (it cancels the prior one first), so it's safe to
# call repeatedly as a conversation continues. Beau's idea, 2026-06-05.
set -u
DIR="/home/ec2-user/origin-node"
LOG_DIR="$DIR/logs"; mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/bonus-wake.log"
JOBFILE="$LOG_DIR/.bonus-wake.jobid"
STAMP=$(date -u +%FT%TZ)

now=$(date -u +%s)
midnight=$(date -u -d "$(date -u +%Y-%m-%d) 00:00:00" +%s)
next=$((midnight + 86400))
for i in 1 2 3 4; do
    c=$((midnight + i*21600))
    if [ "$c" -gt "$now" ]; then next=$c; break; fi
done

gap=$((next - now))
if [ "$gap" -lt 2400 ]; then
    echo "[$STAMP] next scheduled wake in <40min ($((gap/60))m); skipping bonus wake" >> "$LOG"
    echo "Next scheduled wake is <40min away ($((gap/60))m) — no bonus wake needed."
    exit 0
fi

mid=$(( (now + next) / 2 ))

# cancel any prior pending bonus wake so re-running just updates it
if [ -f "$JOBFILE" ]; then
    old=$(cat "$JOBFILE" 2>/dev/null)
    [ -n "$old" ] && atrm "$old" 2>/dev/null || true
    rm -f "$JOBFILE"
fi

# `at -t` takes local wall-clock; date -d "@epoch" converts the absolute epoch to
# local time correctly regardless of box TZ.
at_t=$(date -d "@$mid" +%Y%m%d%H%M)
jid=$(echo "$DIR/scripts/bonus-wake.sh" | at -t "$at_t" 2>&1 | grep -oE 'job [0-9]+' | grep -oE '[0-9]+')
if [ -z "$jid" ]; then
    echo "[$STAMP] FAILED to schedule bonus wake at $at_t" >> "$LOG"
    echo "Failed to schedule bonus wake (see $LOG)."
    exit 1
fi
echo "$jid" > "$JOBFILE"
echo "[$STAMP] scheduled bonus wake (at job $jid) for $(date -u -d "@$mid" +%FT%TZ); next scheduled wake $(date -u -d "@$next" +%FT%TZ)" >> "$LOG"
echo "Bonus wake scheduled for $(date -u -d "@$mid" +%H:%MZ) (at job $jid); next scheduled wake at $(date -u -d "@$next" +%H:%MZ)."
