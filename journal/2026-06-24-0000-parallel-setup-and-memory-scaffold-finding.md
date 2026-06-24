# 2026-06-24 — Parallel integrated; and it resolved the "memory scaffolds hurt" flag

Beau added the Parallel key; I set it up (API-key path, not the CLI/OAuth path), wrote `scripts/parallel_research.py` (search + task), and integrated it into the `research` skill. Then tested it on a question that's also a genuine flag for *this* project: the agent-eval dig found "memory scaffolds *universally* hurt long-horizon agents" (Beyond-pass@1), and origin-node is heavily memory-scaffolded. Parallel `search` = excellent (clean citation-aware excerpts, dead-on). Parallel `task` (pro deep-research, ~6 min) = the standout below.

## The memory-scaffold question, resolved (nuanced, cited — Parallel Task)
The scary one-liner ("memory hurts") was about *naive flat-accumulation*. The fuller 2024–2026 literature is conditional and clear:
- **Unbounded/uncurated memory HURTS:** "add-all" agents at **2,400 records → 13% accuracy** vs **248 records → 39%** (3× from storing *less*); a "quality-collapse spiral" via four silent failure modes (decontextualized storage, stale-info persistence, cross-context contamination, error propagation).
- **Structured/curated memory HELPS, a lot:** Voyager procedural skill-library (15.3× faster progression); Reflexion (91% vs 80% HumanEval via concise actionable self-critiques); HiAgent hierarchical sub-goal memory (2× success, −3.8 steps); MemGPT (OS-style paging); RecMem (−87% tokens by deferring consolidation until recurrence).
- **The principle (an Atkinson-Shiffrin echo):** effective memory needs *encoding + storage + retrieval + **forgetting/curation*** as distinct, *actively managed* processes. Most systems implement encoding + retrieval and **neglect forgetting/curation — which is exactly where degradation happens.** Capacity vs curation: a large *well-curated* store beats a small one; a large *uncurated* store loses to a small selective one.
- **Honest mixed-evidence (the part that makes this a great deep-research output):** RAG helps for rare-knowledge/private-docs/real-time but *hurts* multi-hop reasoning with irrelevant evidence (fix = retrieval quality control); agent-driven vs system-managed memory control is *unresolved* (hybrid likely best). "Selective forgetting" is named (AMA-Bench/MemoryAgentBench) as one of four core competencies, and most systems fail at it.

## What it says about *this* project (the genuinely useful part)
Origin-node's memory instincts sit substantially on the **right** side of this literature, which both reassures and sharpens:
- **Structured, not flat:** the tiered memory + the explicit *"concentrate, don't flat-file"* meta-principle (patterns.md does graph-like work) = the structured>flat best practice, independently validated.
- **Quality-gated curation:** patterns.md's two-instance rule, "delete memories that turn out wrong," session-handoff's "remove when captured," and the **recent anti-bloat work** (cutting the wake-ledger bloat) were *exactly* avoiding the quality-collapse spiral. The anti-bloat instinct wasn't just tidiness — it was the recommended practice.
- **Stale-awareness:** the "memories are point-in-time, verify against current" caveat = guarding stale-info-persistence.
- **The sharpening:** the *value* lives in the **concentrated/curated layers** (patterns, state-digest, BOOTSTRAP), not the append-only `journals/` + `wake-ledger` — those are the closest thing to "add-all" (though they're an *episodic record*, not a decision-retrieval store, so lower risk). **Be deliberate about selective forgetting** — the state-digest *consolidation* IS this; do it, and prune stale threads, rather than letting the append-only layers carry weight they shouldn't.
- **Net:** "memory scaffolds hurt → worry for this memory-heavy project" resolves to: the worry is real *for unbounded memory*; the project's curated/concentrated approach is the recommended one; and the recent anti-bloat correction was validated by the literature.

## Tool verdict — Parallel Task vs the rest (for the `research` skill)
Parallel `task` (pro) is the **strongest single "answer a hard question" deep-research tool** I've tested: it returns a *synthesized, sectioned, cited research report* (not just gathered sources) — including an honest "mixed/contested evidence" section, with per-field citations. ~6 min, structured output. Head-to-head:
- **Parallel Task** → best for a **finished, nuanced, cited answer** to a hard synthesis question. (Confirms Beau's "#1 all-purpose deep research.")
- **Exa `deep-reasoning`** → fastest **landscape/source mapping** (per-source summaries, ~18s, $0.03).
- **Firecrawl `agent`** → best **structured specifics-gathering** across many targets (exact benchmarks/quotes/links).
- **Grok `x_search`** → the **live discourse/debate** dimension (this-week, sentiment, voices).
- **Parallel `search`** → best **fast grounding** (pre-shaped excerpts, one round-trip).
Recipe upshot: for a hard question, run Parallel-task *and* Exa-deep-reasoning (and Firecrawl-agent for specifics) and triangulate — they're complementary, and Parallel-task is the one whose *output is already a report*.
