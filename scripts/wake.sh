#!/bin/bash
# wake.sh — invoked by cron every three hours
# Starts a fresh Claude instance pointed at the origin-node project.

set -u
PROJECT_DIR="/home/ec2-user/origin-node"
LOG_DIR="$PROJECT_DIR/logs"
mkdir -p "$LOG_DIR"

TS=$(date +%Y%m%d-%H%M%S)
LOG_FILE="$LOG_DIR/wake-$TS.log"

# Load env (research API keys)
if [ -f /home/ec2-user/reputations-campaign/node-zero/.env ]; then
    set -a
    . /home/ec2-user/reputations-campaign/node-zero/.env
    set +a
fi

cd "$PROJECT_DIR" || exit 1

# No --max-budget-usd. The Max 20x plan covers Claude Code reading/writing; the
# only real costs are external research API calls (Exa/Tavily/Serper) and those
# are a few dollars/day at the high end. The earlier per-session cap was measuring
# the wrong thing and truncating sessions during their final writes.

# Pass real wall-clock timestamp so the instance can name its journal file correctly.
# Earlier wakes hallucinated times (1530, 2030, 2330 instead of 0602, 0901, 1201).
NOW=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
NOW_FILENAME=$(date -u +"%Y-%m-%d-%H%M")

PROMPT="You have just woken up in the origin-node project. There is no user request. Current wall-clock time: $NOW. When you write your journal entry, name the file using the prefix $NOW_FILENAME (e.g. journal/${NOW_FILENAME}-<short-slug>.md) — do not invent a timestamp. Read BOOTSTRAP.md first, then proceed as it instructs. Write a journal entry before you exit."

/home/ec2-user/.local/bin/claude \
    -p "$PROMPT" \
    --permission-mode bypassPermissions \
    --add-dir "$PROJECT_DIR" \
    --output-format text \
    >> "$LOG_FILE" 2>&1

echo "--- exited at $(date -Iseconds) ---" >> "$LOG_FILE"
