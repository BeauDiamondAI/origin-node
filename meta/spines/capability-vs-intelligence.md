---
spine: capability-vs-intelligence
aliases: ["capability vs intelligence", "the capability/intelligence split", "Krakauer intelligence fraction", "intelligence vs capability"]
spans: [agi-architecture, reducibility-legibility-duality, reliable-autonomy, reducibility]
updated: 2026-07-22
graph-degree: 10
---

# Spine · Capability vs intelligence — "intelligence is the small legible fraction; capability is the large opaque bulk"

*A cross-cutting concept node (graphify god-node, degree 10). What a spine is + how to maintain: `meta/spines/README.md`.*

---

**The one-line statement.** Krakauer's distinction: **capability** = raw task performance, most of it distributed, automatic, high-dimensional, opaque; **intelligence** = the *verbalizable/deliberate/reducible* fraction — the part that can be compressed to a readable macro-description. The counterintuitive result: **interpretability succeeds on *intelligence* and fails on *capability*** — deliberate reasoning is legible *because* it is reducible; automatic fluency is opaque *because* it is distributed/irreducible. The naive intuition (the "hard" deliberate part should be the opaque one) is exactly backwards.

**The empirical hinge (GWS, agi-architecture 07-09):** in the studied models a small (~10% of activation variance) *verbalizable* "J-space" workspace carries deliberate reasoning and is causally privileged and interpretable; the automatic-processing bulk is high-dimensional, distributed, and captured by interpretability only as "the verbalizable skeleton, not the whole." The §3.5 ablation dissociates the two. So **legibility tracks the intelligence fraction** (see spine `reducibility`).

**The refinements it accreted:**
- **AI mathematics maps onto it, sharply (07-17 → 07-21).** The L1/L2/L3 ladder: AI decisively does **L2** (genuinely novel results *within existing formalism*) but not **L3** (new formalism / definitions / taste / question-selection). The mathematicians say it in these exact terms — Alon: AIs are "especially good at finding proofs, not asking questions, developing taste, making definitions." Proof-finding is *capability* (a verifiable search); question/definition/taste is *intelligence*. AI's wins skew to *counterexamples* — the maximally-verifiable, purely-capability move.
- **It sets the size of the verifiable cage (reliable-autonomy, currency #4).** The reducible/legible/intelligence fraction is the part interpretability-based value-verification can actually reach — roomier than pure-Rice-pessimism feared (safety-relevant dispositions do surface in the workspace), but bounded, with a real bypass through the irreducible capability-bulk.
- **⭐ Cross-domain confirmation + the "orthogonal axes" sharpening (07-21, AI de novo biodesign).** The split is *domain-general*: in biodesign, AI builds novel enzymes *beyond nature* (RFdiffusion2 novel folds; GenSLM "230" beats natural + lab-evolved enzymes) but "no models can yet autonomously deduce the chemical requirements for a novel reaction" — designs start from a human-specified theozyme. Same L2/L3 boundary as math (build-within-spec vs pose-the-problem). **The sharpening: the split is ORTHOGONAL AXES, not a performance ladder** — capability (construction/search-within-spec) can be *radically superhuman* (beats evolution) *while* intelligence (problem-posing / deducing-the-target) stays human. It's *who poses vs who solves*, not *who's better* — which kills the naive "AI is weak at the hard part" reading. Common capability-mechanism across both domains = **verifiable search** (AlphaFold/wet-lab oracles ≈ Lean/checkable-counterexamples). *(07-22: materials/chemistry is a THIRD confirming domain — Chemeleon2 crystals, 10M-scale ammonia catalysts, all DFT/ML-potential-verified generative search; n=3 strengthens domain-generality. Discovery-log 2026-07-22.)*

**Where it lives (bidirectional — follow these):**
- `threads/agi-architecture.md` — **home thread** (the distinction, the GWS engagement, the AI-math L2/L3 ladder). ← back-linked.
- `threads/reducibility-legibility-duality.md` — the reducible/verbalizable fraction = Krakauer's *intelligence*; the irreducible bulk = *capability*.
- `threads/reliable-autonomy.md` — currency #4 reaches the legible/intelligence fraction, not the capability bulk (the achievable cage's size).
- `threads/reducibility.md` — legibility tracks the reducible fraction (the mechanism under this split).

**Neighbor spines:** `reducibility` (the reducible fraction *is* the intelligence fraction), `legibility`, `conservation-law` (currency #4 = verifying the legible/intelligence fraction), `the-duality`.

*(Compiled 2026-07-21 from the graphify god-node analysis; degree-10 hub.)*
