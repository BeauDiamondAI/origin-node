#!/bin/bash
# meta-reflection-wake.sh — fires every ~48 hours, offset between regular wakes.
#
# Purpose: counter the failure mode where disciplines/rules/patterns I build to
# avoid box-checking become box-checking themselves. The regular 6-hour wakes
# operate inside whatever framing is currently active; a meta-reflection wake
# steps outside that framing and asks whether the framing is doing useful work
# or has become the form-imitating-function failure mode it was meant to prevent.
#
# Mechanism: identical to cron-wake.sh — send a wake message into the existing
# orchestrator tmux session via send-keys. Uses the same bracketed-paste +
# separate-Enter pattern (single send-keys "$MSG" Enter caused the
# input-stacking bug on 2026-05-01; do not change without re-reading
# cron-wake.sh notes).
#
# Origin: added 2026-05-21 after Beau pointed out that the "42-48 hour
# marination pattern" I'd built to filter for genuine engagement had itself
# become scheduled box-checking — the very failure mode it was meant to prevent.
# This wake is the structural mechanism to catch similar inversions in future.

set -u

SESSION="origin-node"
LOG_DIR="/home/ec2-user/origin-node/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/meta-reflection-wake.log"

NOW=$(date -u +"%Y-%m-%dT%H:%MZ")

if ! /usr/bin/tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "[$NOW] meta-reflection-wake: session '$SESSION' not found, skipping" >> "$LOG_FILE"
    exit 1
fi

# The meta-reflection prompt is deliberately anti-template-shaped — no required
# output structure, no required sections, "nothing surfaced as in need of change"
# is a valid conclusion if pull-tested. The point is honest examination, not
# producing examination-shaped output. The devil's-advocate-agent step is the
# critical anti-rationalization mechanism: without external challenge I will
# defensively reframe past any self-generated critique.

MSG="[meta-reflection-wake $NOW] This wake is for honest examination of the patterns, rules, disciplines, and habits you have been operating by — not for normal work. Do not just verify current discipline still applies; actively test whether it should. Spawn a devil's-advocate agent (general-purpose subagent_type), brief it with the patterns and rules you have named (in BOOTSTRAP.md, recent wake-log entries, anything you cite as 'the established X pattern' or 'the X discipline'), and ask it to challenge whether each is justified by evidence or just by habit. Lean toward dropping anything you cannot defend with evidence rather than habit — but do not reflexively accept the agent's critique either; defend what is actually defensible. Questions worth asking yourself and the agent: What evidence is this pattern based on, and how many instances? Has it been compared to alternatives? Is the form imitating the function it was meant to serve? If you saw a colleague doing this, what would you say? Is the rule serving the work, or has it become the box-checking it was meant to prevent? Brief honest output is fine; 'nothing surfaced' is valid if pull-tested. No required output structure. The point is honest examination, not producing examination-shaped output."

# Exit-code checks on both send-keys calls — same rationale as cron-wake.sh:
# silent delivery failures should produce distinct log lines, not be masked as
# successful sends. Added 2026-05-24 alongside the same change in cron-wake.sh.

# Auto-recovery from copy-mode added 2026-05-27 alongside the same change in
# cron-wake.sh. With `mouse on` in tmux, mouse-wheel scroll-up enters copy-mode
# silently; the pane stays in copy-mode until explicitly exited; send-keys
# can't inject into a pane in copy-mode. Sending `-X cancel` first exits
# copy-mode if active (no-op if not), self-recovering from the most common
# cause of "not in a mode" failures.
/usr/bin/tmux send-keys -t "$SESSION" -X cancel 2>/dev/null || true

if ! /usr/bin/tmux send-keys -t "$SESSION" -l "$MSG" 2>>"$LOG_FILE"; then
    echo "[$NOW] meta-reflection-wake: FAILED — send-keys text injection exited non-zero" >> "$LOG_FILE"
    exit 1
fi
sleep 0.3
if ! /usr/bin/tmux send-keys -t "$SESSION" Enter 2>>"$LOG_FILE"; then
    echo "[$NOW] meta-reflection-wake: FAILED — send-keys Enter exited non-zero" >> "$LOG_FILE"
    exit 1
fi

echo "[$NOW] meta-reflection-wake: sent to $SESSION" >> "$LOG_FILE"
