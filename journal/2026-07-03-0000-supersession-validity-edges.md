# 2026-07-03 00:00Z — increment 3: supersession/validity edges (the value-ranking stance done right)

The teed-up build from increment 1.5 (recall scores ~0 on surfacing current-over-stale; no ranker fixes it). This is the novelty-gate's defensible core implemented correctly: **demote *superseded*, not *old*** — a curator-asserted validity edge, not the recency proxy.

**Built:** `scripts/supersession.py` + a convention — `[[SUPERSEDED]]` (block: marks a passage until blank/header/next-list-item) and `[[SUPERSEDED-BEGIN/END]]` (range: a multi-section stale region). Curator-asserted at authoring time (judgment, per the project's thesis — not auto-inferred recency). Integrated: `recall.rank()` discounts hits on stale lines ×0.1 and counts coverage only from live lines; `semantic_recall` excludes stale lines from embedding. Old text demoted, not deleted.

**It works, measured on the (already-built) supersession test:** marked two real stale passages from our own history — the PreCompact bullet in state-digest (fully stale — PreCompact removed 06-30) and discovery-protocol's Serper→Tavily→Exa flow (range). **PreCompact flipped FAIL→PASS across literal/semantic/hybrid** — the stale bullet dropped from rank 1 → 6, so BOOTSTRAP's correction now surfaces first. **No regression** on the 15-query eval (goldA hybrid 0.61 unchanged).

**Honest boundary the test surfaced (not swept):** the research-toolchain pair stays "FAIL" — but *correctly*. discovery-protocol isn't wholly stale; its current banner legitimately mentions the tools and points to the research skill, so live lines keep it relevant. That's the real line between **clean supersession** (fully-stale passage → demotes) and **partial-file staleness** (living file + stale region + current pointer → should stay relevant; wants *section-level surfacing* to show the reader the live part). Didn't over-claim a universal fix.

**Why it matters:** first increment that builds directly ON the validated-novel part of the design (the corrosive-proxy-resistance stance), not just retrieval mechanics. Cheap (grep-able marker, no infra), judgment-based (fits the thesis), demonstrably flips the clean case. And it's dogfooded on the project's own real corrections — the memory system now handles its own staleness, which is the point.

**Next candidates (pick by pull):** write-side capture schema (Fable's "largest lever, currently zero" — the `[[SUPERSEDED]]` edge is the first piece of it); section-level surfacing for the partial-staleness boundary; the always-resident-core/integrative program (Fable's deepest reframe). Lower priority: LLM-consolidation probe (degradation-checked), decay, reader-side behavioral eval.

Six built/validated increments across two days, each measured and honestly self-corrected. The effort Beau named as the surprising absence is now the most active, best-instrumented thread in the project.
