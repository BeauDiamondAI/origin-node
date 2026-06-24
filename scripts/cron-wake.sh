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

# Deliberate session boundary (added 2026-06-24): if the Stop hook flagged that a
# handoff is written and context is critical, send /clear instead of a wake. This
# reuses the proven idle-time send-keys path. The SessionStart hook re-orients the
# fresh session; the next cron tick resumes normal wakes. No cron toggling needed —
# blocking auto-compaction (PreCompact hook) + this self-clear replace the old
# pause-the-crons-and-wait-for-Beau model.
CLEAR_FLAG="/home/ec2-user/origin-node/meta/.clear-requested"
HANDOFF_FLAG="/home/ec2-user/origin-node/meta/.handoff-ready"
if [ -f "$CLEAR_FLAG" ]; then
    /usr/bin/tmux send-keys -t "$SESSION" -X cancel 2>/dev/null || true
    if /usr/bin/tmux send-keys -t "$SESSION" -l "/clear" 2>>"$LOG_FILE"; then
        sleep 0.3
        /usr/bin/tmux send-keys -t "$SESSION" Enter 2>>"$LOG_FILE"
        rm -f "$CLEAR_FLAG" "$HANDOFF_FLAG"
        echo "[$NOW] cron-wake: sent /clear (deliberate session boundary); flags cleared" >> "$LOG_FILE"
    else
        echo "[$NOW] cron-wake: FAILED to send /clear; leaving flags for retry" >> "$LOG_FILE"
    fi
    exit 0
fi

MSG="[cron-wake $NOW] Autonomous wake. Use the time however serves the work, or honestly recognize that nothing pulls right now and exit briefly. Both are valid. The close-out is binary: any wake that wasn't a brief exit produced work, and work gets documented before you stop — a journal entry + a beau-briefings line (length matched to the work, from a one-line pointer on up), not just a thread or ledger update. A brief exit needs only its one wake-ledger line. And if the wake changed the project's state (a thread advanced, a finding, a new artifact/tool), update meta/state-digest.md too — it is the fresh-session boot view and has gone stale before."

# Notes on this message text:
# - The cron fires into the existing orchestrator session, so context is intact.
#   Don't instruct re-reading BOOTSTRAP/journals/threads — that was residual
#   thinking from the old fresh-instance pattern. The orchestrator already knows
#   where things stand.
# - Don't require a journal entry per wake — that implicit pressure produces slop
#   on wakes where nothing genuine pulls; a wake where the right move is "exit
#   briefly" stays valid. BUT (refined 2026-06-17, Beau's suggestion) the message
#   carries a close-out reminder: if the wake produced work, capture it in the
#   journal (episodic narrative) + beau-briefings, not just a thread/ledger update.
#   (2026-06-18, Beau: dropped the word "substantive" — it was a leaky threshold
#   that let a wake rule its own work below the bar and skip the record, reopening
#   the gap. The test is binary: work vs brief-exit. ANY work gets documented;
#   judgment governs the *length* — a one-line pointer for small work, a full
#   entry for a deep engagement — not *whether*. Brief exits still need only the
#   one ledger line, which is what keeps this from producing slop.) This addresses the 06-13→17 gap, where work was real but
#   the episodic trace silently lapsed (the wake-ledger lines had bloated to
#   paragraph length and "felt like" complete documentation — BOOTSTRAP line 78's
#   failure mode). The conditional keeps the no-slop principle (brief exits need
#   only their one ledger line) while a structural reminder-at-the-point-of-action
#   prevents the gap — more reliable than trusting the discipline to carry across
#   the inter-wake gap on its own (which is what failed).
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
# Exit-code checks on both send-keys calls added 2026-05-24 after a silent
# delivery failure: the 18:00Z firing logged "sent" but the wake text never
# appeared in the Claude Code TUI. Prior version logged success unconditionally
# whether or not send-keys actually succeeded — masking real failures as
# successful sends. Now: failures produce a distinct log line so future
# anomalies are diagnosable instead of invisible.

# Auto-recovery from copy-mode added 2026-05-27 after the exit-code check
# revealed the 06:00 and 12:00 May 27 firings both failed with tmux's
# "not in a mode" error. Diagnosed cause: with `mouse on` in tmux config,
# mouse-wheel scroll-up automatically enters copy-mode, and the pane stays
# in copy-mode until explicitly exited. send-keys can't inject into a pane
# in copy-mode. Now: before each inject, send `-X cancel` to exit copy-mode
# if active (no-op if not in copy-mode), so the script self-recovers from
# the most common cause of "not in a mode" failures.
/usr/bin/tmux send-keys -t "$SESSION" -X cancel 2>/dev/null || true

if ! /usr/bin/tmux send-keys -t "$SESSION" -l "$MSG" 2>>"$LOG_FILE"; then
    echo "[$NOW] cron-wake: FAILED — send-keys text injection exited non-zero" >> "$LOG_FILE"
    exit 1
fi
sleep 0.3
if ! /usr/bin/tmux send-keys -t "$SESSION" Enter 2>>"$LOG_FILE"; then
    echo "[$NOW] cron-wake: FAILED — send-keys Enter exited non-zero" >> "$LOG_FILE"
    exit 1
fi

echo "[$NOW] cron-wake: sent to $SESSION (split text+Enter)" >> "$LOG_FILE"
