#!/bin/bash
# clear-watcher.sh — fire the deliberate /clear PROMPTLY when the session has flagged it ready.
#
# Added 2026-07-01 (Beau found the gap): the /clear was gated on the 6-hourly cron-wake, so there
# was an up-to-6h lag between .clear-requested being set (at the 95% handoff) and the actual reset
# — long enough that an active session could climb to ~100% (lossy-summary fallback) first,
# defeating the deliberate handoff. This runs every ~2 min so the clear fires within minutes.
#
# Idempotent + safe: no-op unless .clear-requested exists; sends /clear once, then removes the
# flags. Same proven tmux send-keys path cron-wake uses (split text+Enter; -X cancel first to
# exit copy-mode). Does nothing if the session is missing.
set -u
SESSION="origin-node"
META="/home/ec2-user/origin-node/meta"
LOG="/home/ec2-user/origin-node/logs/cron-wake.log"
NOW=$(date -u +"%Y-%m-%dT%H:%MZ")

[ -f "$META/.clear-requested" ] || exit 0
/usr/bin/tmux has-session -t "$SESSION" 2>/dev/null || exit 0

/usr/bin/tmux send-keys -t "$SESSION" -X cancel 2>/dev/null || true
if /usr/bin/tmux send-keys -t "$SESSION" -l "/clear" 2>>"$LOG"; then
    sleep 0.3
    /usr/bin/tmux send-keys -t "$SESSION" Enter 2>>"$LOG"
    rm -f "$META/.clear-requested" "$META/.handoff-ready"
    echo "[$NOW] clear-watcher: sent /clear (deliberate boundary, prompt); flags cleared" >> "$LOG"
else
    echo "[$NOW] clear-watcher: FAILED to send /clear; leaving flags for retry" >> "$LOG"
fi
