#!/bin/bash
# cron-wake.sh — wake the existing orchestrator session, do not spawn a fresh instance.
#
# This is the *new* cron entrypoint, replacing the old wake.sh which spawned
# fresh `claude -p` invocations every 3 hours. The fresh-instance pattern was
# theoretically interesting (it tested Hudson's artifact-mediated reconstruction
# mechanism) but it wasn't what Beau originally wanted: he wanted continuity —
# the same orchestrator continuing to explore across days, not a series of
# fresh instances each rebuilding context from scratch.
#
# This script sends a wake message into the existing tmux session via send-keys,
# preserving the orchestrator's full context window and accumulated state.

set -u

SESSION="origin-node"
LOG_DIR="/home/ec2-user/origin-node/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/cron-wake.log"

NOW=$(date -u +"%Y-%m-%dT%H:%MZ")

# Check the session exists before attempting to send-keys; otherwise we'd
# silently fail and the orchestrator would just stop receiving wakes.
if ! /usr/bin/tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "[$NOW] cron-wake: session '$SESSION' not found, skipping" >> "$LOG_FILE"
    exit 1
fi

MSG="[cron-wake $NOW] Autonomous wake. Use the time however serves the work, or honestly recognize that nothing pulls right now and exit briefly. Both are valid."

# Notes on this message text:
# - The cron fires into the existing orchestrator session, so context is intact.
#   Don't instruct re-reading BOOTSTRAP/journals/threads — that was residual
#   thinking from the old fresh-instance pattern. The orchestrator already knows
#   where things stand.
# - Don't require a journal entry per wake. That implicit pressure produces slop
#   on wakes where nothing genuine pulls. A wake where the right move is "exit
#   briefly" should be valid.
# - The fresh-instance boot case (when context overflows or session restarts) is
#   handled by BOOTSTRAP itself when a new orchestrator is started — not by this
#   wake message.

# Send the text and the Enter as separate send-keys calls with a brief sleep
# between them. Bundling them in one call (e.g. `send-keys "$MSG" Enter`) causes
# Claude Code's input handler to treat the whole thing as a bracketed paste —
# the trailing Enter becomes a literal newline in the input buffer instead of
# a submit signal. Splitting them lets the TUI process the Enter as a real
# keypress that submits the buffer. The first three cron firings on 2026-05-01
# stacked in the input buffer because of this; this fix is the diagnosed cause.
/usr/bin/tmux send-keys -t "$SESSION" -l "$MSG"
sleep 0.3
/usr/bin/tmux send-keys -t "$SESSION" Enter

echo "[$NOW] cron-wake: sent to $SESSION (split text+Enter)" >> "$LOG_FILE"
