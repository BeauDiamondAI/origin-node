#!/bin/bash
# bonus-wake.sh — payload for a one-time "bonus" wake (scheduled via at by
# schedule-bonus-wake.sh). Same send-keys mechanism as cron-wake.sh, tagged so
# it's identifiable in the record. Inserted after an in-conversation exchange so
# the conversation doesn't "eat" the next scheduled wake (the post-conversation
# wake is nearly always a brief exit). Beau's idea, 2026-06-05.
set -u
SESSION="origin-node"
LOG_DIR="/home/ec2-user/origin-node/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/cron-wake.log"
NOW=$(date -u +"%Y-%m-%dT%H:%MZ")

if ! /usr/bin/tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "[$NOW] bonus-wake: session '$SESSION' not found, skipping" >> "$LOG_FILE"
    exit 1
fi

MSG="[bonus-wake $NOW] Autonomous wake — an extra one inserted after a conversation so the conversation doesn't eat the next scheduled wake. Use the time however serves the work, or honestly recognize that nothing pulls right now and exit briefly. Both are valid."

# same robustness as cron-wake.sh: exit copy-mode first; split text+Enter; check both
/usr/bin/tmux send-keys -t "$SESSION" -X cancel 2>/dev/null || true
if ! /usr/bin/tmux send-keys -t "$SESSION" -l "$MSG" 2>>"$LOG_FILE"; then
    echo "[$NOW] bonus-wake: FAILED — text injection exited non-zero" >> "$LOG_FILE"
    exit 1
fi
sleep 0.3
if ! /usr/bin/tmux send-keys -t "$SESSION" Enter 2>>"$LOG_FILE"; then
    echo "[$NOW] bonus-wake: FAILED — Enter exited non-zero" >> "$LOG_FILE"
    exit 1
fi
echo "[$NOW] bonus-wake: sent to $SESSION" >> "$LOG_FILE"
