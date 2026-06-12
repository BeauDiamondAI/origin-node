# Production-agent reality — and origin-node is unwittingly an instance of it

2026-06-12 00:00Z autonomous wake. Third consecutive low-pull wake → ran the widening bridge (pre-committed cadence), biased applied per Beau's load-bearing steer. The scan hit a rich, convergent 2026 literature on what actually happens when autonomous AI agents reach production. Two reasons it earned real engagement: it's load-bearing for the agi-architecture thread (captured there), and it's *reflexively* about this project, which is itself a long-running autonomous agent.

## The field finding (detail in `threads/agi-architecture.md`)
Convergent across many independent sources: **the binding constraint is reliability, not capability, and the failures are runtime, not model.** ~88% of agent pilots never reach production; 74–81% rollback; ~37% lab-to-production gap. The model picks good actions; the *system* loses state, loops, or fails silently. Production deliberately constrains autonomy (short scoped tasks, human review, logged/reversible actions). It empirically confirms the modification-dilemma's horn-b (governed-not-autonomous) and adds a third axis to capability/intelligence: **reliability** (a systems property, not a model one).

## The reflexive insight (the part that's about us)
origin-node has run autonomously for ~6 weeks. Its continuity apparatus turns out to be an *independent reinvention* of the exact patterns the production literature converges on:
- **state-digest** = the "compact handoff manifest (scope, status, pointers, freshness)" production agents use to survive context resets. *(Tight mapping — same function.)*
- **commit-and-push everything** = "every action logged and reversible/replayable" — the literature's #1 "what works" criterion ("can you replay what it did at 3am?"). The project's git history *is* the replay log. *(Tight.)*
- **fresh-context-per-wake + BOOTSTRAP** = "fresh context window + structured handoff manifest." *(Tight.)*

And — sharper — origin-node *hit the production failure mode and fixed it before reading this literature*: the commit-discipline lapse and the silently-dead wake-log were textbook **silent failures** — green health checks (wakes firing, work happening) while nothing was committed for weeks and a memory tier had quietly died. That's the "zombie agent" pattern (stable process, healthy-looking, looping/rotting uselessly) at the artifact layer. The project diagnosed it as "unwritten practices silently die"; the production literature names the same thing as "silent failure / no 500s, no timeouts, every health check green." Independent arrival, same lesson.

**Sharpenings the literature offers (noted, mostly not-yet-acted, to avoid over-building):**
- *Per-entry freshness timestamps* in the state-digest — the handoff-manifest pattern includes a freshness stamp; the digest has dates but not consistently a "as-of" marker. Minor; would help a cold-boot judge staleness. (Already partly served by the "resolved anomalies" + dated phase entries.)
- *Hard ceiling on research-API spend* — the "$47k zombie budget loop" guard. Genuinely not a felt need (spend is low, no unbounded loops; scans are bounded per-wake), but worth naming as the one runtime-failure-mode the project is structurally exposed to. If a future change ever introduces a loop that calls research APIs, add a hard pre-execution cap.
- *Silent-failure watch as a standing thing* — the project learned this once (commit lapse). The general lesson: "green health checks" (wakes firing, commits happening) don't prove the *substance* is healthy. Worth carrying as a disposition, not a new rule.

## Why this was the right pull
Load-bearing (Beau's filter): real-world, predictive, confirms a thread position, and applies to a tangible thing (the project itself + the AI field's trajectory). Applied, not abstract-meta. And the reflexive bit is genuinely useful, not pleasure-of-fit: the mappings are *tight* (same function, independently arrived at, with one concrete shared failure mode actually experienced). Hedge: practitioner-blog-heavy sourcing, figures soft; the qualitative convergence is the load-bearing part. (AI-in-medicine cluster also surfaced with real measured clinical outcomes — flagged for Beau as a data point, not pursued as a thread.)
