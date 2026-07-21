---
spine: conservation-law
aliases: ["you can only verify what you constrain", "the conservation law", "verify-what-you-constrain"]
spans: [reliable-autonomy, reducibility-legibility-duality, agi-architecture]
updated: 2026-07-21
graph-degree: 11
---

# Spine · The conservation law — "you can only verify what you constrain"

*A cross-cutting concept node (top god-node in the `threads/` graph, degree 11). What a spine is + how to maintain them: `meta/spines/README.md`.*

---

**The one-line statement.** Every strong guarantee about an open-ended agent is *paid for* by a constraint somewhere in the system. You can **move** the constraint but not eliminate it; "verified genuine open-ended autonomy" is close to a contradiction. The honest goal is never "solve reliable autonomy" but "shrink and govern the irreducible residue."

**The four currencies (where the constraint gets paid).** A verification guarantee is bought in one of: (1) **action-space** — constrain what the agent *can do* (decidable verification); (2) **property-strength** — prove a *weaker* property / on an over-approximation (sound-but-incomplete); (3) **certainty-coverage** — "safe w.p. 1−δ *on distribution D*" (the distribution is the cage; novelty walks the agent off it); (4) **representation-legibility** — verify a legible internal value-representation instead of the action-space (interpretability). The dominant 2026 "verify-the-framework-not-the-model" paradigm is the law's own corollary — guarantees come from verifying the constrained wrapper while the open-ended core stays unverified.

**Why it's a theorem, not a slogan (grounding).** Rice's theorem: every non-trivial *semantic* property of a Turing-complete system is undecidable; an open-ended agent realizes an unrestricted behavioral range, so any interesting behavioral property (safe/corrigible/won't-harm) is undecidable *for it* — making it decidable *requires* restricting to a sub-Turing class. Independently grounded: **Azadi 2025** (arXiv:2505.04646, *BioSystems* — autonomy⟹Turing-complete⟹undecidable behavioral properties⟹computational irreducibility, both verified); **Melo 2025** (*Sci. Reports* 15:15591 — inner-alignment undecidable by Rice, *decidable iff a halting constraint is imposed* = re-introduce a constraint). Counterexample search returned none: every known method buys its guarantee by constraining.

**The refinements it has accreted (each from a different thread):**
- **currency #4 is a bounded cage-expander, not an escape (07-09, GWS).** Interpretability reaches the *reducible/verbalizable* fraction (Gurnee "J-space" workspace ≈ the intelligence fraction), not the irreducible bulk — roomier than pure-Rice-pessimism feared, still a cage; the residue has a real bypass route. And at the *human-decision* layer it can go **net-negative** (07-19): an explanation the reviewer pattern-matches instead of reasoning through *subtracts* oversight — legibility without enforced engagement is counterfeit currency.
- **CoT-monitorability = #4's sharpest working instance, fragile in a conservation-law shape (07-21).** The reasoning trace is a legible representation a (weaker) monitor can read; it *currently works* (models struggle to obfuscate their CoT even when told they're watched). But its value is destroyed by the **"monitorability tax"** (Baker 2025): optimize the CoT to *look* safe and the model learns *obfuscated* misbehavior — you can't have both a look-safe-optimized CoT and a trustworthy-monitor CoT. Verifiability is bought by leaving the constraint (optimization pressure on the CoT) *unpaid* — the representation-layer Goodhart. Also architecture-bought: latent/opaque reasoning would destroy it, so requiring-CoT is itself a constraint-for-verifiability. (07-19 human-layer net-negative + this training-layer obfuscation = the legibility currency is worth less than face value under *any* pressure to make the legible artifact look-good rather than be-faithful.)
- **The governance corollary (07-18).** When you *can't* verify the agent (which the theorem says you can't, for open-ended ones), you constrain its *autonomy* to preserve a verifiable **human accountability + contestability** — verification's *cousin*, not verification. The 2026 cross-sector AI-governance wave is this law *legislated* (governed-not-autonomous across health/hiring/credit/benefits).
- **It bites twice (07-18b → 07-19).** Constraining the AI's action-space (human-in-the-loop) is necessary-not-sufficient; genuine accountability needs a *second*, usually-skipped payment — real human oversight-capacity — which is often unpayable at the UI and migrates *institutional* (Green 2022: justify-before-deploy). Target = *appropriate reliance*, both over- and under-reliance are failures.
- **Verification-clustering in AI-math (07-21).** AI's biggest math wins skew to *counterexamples* — a bounded, maximally-*verifiable* search within existing formalism; formal verification (Lean) is "the constraint that buys back verifiability." What's verifiable is what's reducible.

**Where it lives (bidirectional — follow these):**
- `threads/reliable-autonomy.md` — **home thread** (the conjecture → working theorem; the 4 currencies; the governance increments). ← back-linked.
- `threads/reducibility-legibility-duality.md` — the **agent-side of the duality** (reducibility-availability-undecidability ↔ agent-verification-undecidability = the same Rice-style wall pointed opposite ways); the law is the duality's Part 3.
- `threads/agi-architecture.md` — reliability-as-3rd-axis; verification-buys-verifiability (AlphaProof/Lean, 07-08); the 07-21 AI-math verifiability-clustering.

**Neighbor spines (graphify cross-community bridges — candidates for their own pages):** `capability-vs-intelligence` (legibility tracks the intelligence fraction), `reducibility`, `legibility`, `verifiability`, `the-duality`, `modification-dilemma` (corrigibility-under-self-mod = the law applied to the modification operator; SEVerA).

*(POC provenance: built 2026-07-21 from a `graphify` run on `threads/` — this concept was the #1 god-node. If the pattern proves useful, the other 5 hubs get spine pages + systematic back-links, per the LLM-wiki discussion with Beau.)*
