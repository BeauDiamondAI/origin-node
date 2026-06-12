# Design brief: the achievably-most-useful expanded dependency system

**Provenance.** Requested by Beau (2026-06-12) as a *vision brief* — "the achievably most useful version" of an expanded `scripts/refs.py`: keep what works, solve as much as possible of what doesn't. Persisted here against conversational evaporation. **This is a design vision, not a build commitment** — whether any of it gets built is a separate, independent pull-test (Beau explicitly decoupled the two). It also extends the dependency-self-model arc (`threads/identity-and-continuity.md` move 5; `threads/agi-architecture.md` dependency-self-model + 2026-06-12 extension) and applies the production-agent / clinical-AI-deployment finding (model is the easy part; the integration + judgment + reliability layer is the moat).

## Goal
Answer "I changed X — what is *genuinely* now stale?" with **low false-positives**, catching **implicit** dependencies (no explicit reference), and **honest about its own fallibility** rather than pretending to be an oracle. (The crude tool over-flags structural mentions and is blind to implicit deps — see `meta/memory-system.md` §6b.)

## Architecture — layers, each solving a named gap

**Layer 0 — Structural graph (already works).** refs.py's explicit-reference graph stays as the cheap, exact, deterministic first pass. A free filter; don't replace it.

**Layer 1 — Claim-level granularity.** Extract atomic *claims/anchors* per file (sections, named patterns, specific assertions), not whole files — fixes the file-level coarseness. Markdown structure + the patterns.md schema get most of the way; an LLM extracts finer claims. Dependencies now attach to "the FluxMem-is-associative claim," not just "agi-architecture.md."

**Layer 2 — Semantic index (embeddings).** Embed each claim. The "smart layer" recall.py lacked; it surfaces **implicit dependencies** — content depending on a claim *without naming its path* (the FluxMem→state-digest case). Local sqlite-vector or a small embedding model; cheap.

**Layer 3 — LLM edge-typing (the live-vs-dead solver).** For each candidate edge (structural *or* semantic), an LLM classifies the relation: **DEPENDS-ON** (correctness relies on the current claim — live), **MENTIONS** (historical/contextual — dead), plus ELABORATES / CONTRADICTS / SUPERSEDES. Converts the raw reference graph into a **typed dependency graph.** Typing is done *once per edge, incrementally at write-time* — not per query — so it's affordable.

**Layer 4 — Change-impact propagation.** When a claim changes, walk the typed graph propagating staleness through **DEPENDS-ON edges only** (not MENTIONS) → a precise, low-noise "what's now stale" list, plus a final per-edge LLM check ("did this change *actually* invalidate the dependent, or is it still consistent?"). This kills refs.py's `--stale` over-flagging.

**Layer 5 — Reliability/workflow (what makes it *usable*, and where most such tools die).** The production-agent + sepsis lesson, made concrete:
- **Confidence-gating:** low-confidence judgments → human review (supervision matched to error rate), not silently accepted.
- **Alert-ranking / threshold:** surface the *few* high-confidence-stale items, never a wall — the explicit anti-alert-fatigue move that sank Epic's commercial sepsis model.
- **Audit/replay log + periodic full re-scan:** every judgment logged and reversible; re-scan catches drift the incremental path misses.

## What this achieves
Moves the tool from "structural over-flagging noise" to "a typed, claim-level, judgment-backed staleness detector that catches implicit dependencies and surfaces the *few* genuine ones, with uncertain cases sent to review." It *would* catch the FluxMem→state-digest implicit staleness and *not* flag dead historical mentions.

## The irreducible residue (honest)
It does **not** "solve" the dependency-self-model — it makes it *reliable-enough-with-supervision*. Three hard floors:
1. **Fallibility:** the LLM judgment misses some staleness silently (mitigated by confidence-gating + re-scan + audit, never eliminated — the reliability floor).
2. **Recall limit:** you can't judge an edge the semantic layer never surfaces as a candidate.
3. **The indexical limit:** a system tracking its *own weight-dependencies* (real self-modification) stays out of reach — this whole design works precisely because it tracks an *external* corpus.

## The meta-point
The achievable win is exactly the production-agent / sepsis shape: **not a perfect oracle, but a well-integrated system where the LLM does the hard judgment and a confidence/ranking/audit layer makes it trustworthy.** The moat is the integration and reliability-handling, not a cleverer algorithm.

## Notes
- **General, not project-specific:** this is a knowledge-base-consistency engine for any evolving corpus (wiki, docs, codebase).
- **Domain adjacency (observation, not advice):** structurally the same problem as "when a payer requirement changes, which codified criteria — and which in-flight cases — are now affected?" — change-impact propagation through typed dependency edges is domain-agnostic.
- **Build status:** unbuilt by design. The smallest real next step (if it ever pulls) is Layer 3 alone over Layer 0's candidates — an LLM judging which of refs.py's *structural* references are live-and-now-stale — which would empirically measure the judgment layer's reliability on a real corpus.
