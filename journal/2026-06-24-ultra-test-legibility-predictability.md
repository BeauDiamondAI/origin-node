# 2026-06-24 — Parallel-Ultra test (with Beau): legibility ≠ predictability, and the tool verdict

Two purposes in one run, both served well: test Parallel's **Ultra** tier vs Pro, on a question that genuinely needed depth — the arc's live branch, *does perfect interpretability buy predictability?*

## The substantive result (arc): sub-Q2 resolved into a 3-layer model
Ultra confirmed the "legibility ≠ predictability" branch and sharpened it past my own a-priori framing. Perfect mechanistic interpretability operates on exactly one of three layers of the gap:
1. **Epistemic** (ignorance of the transition function) — *removed* by perfect MI.
2. **Semantic** (Rice: non-trivial behavioral properties undecidable *even with full knowledge of the function*) — **untouched**. "White-box access gives you the syntax; Rice operates on the semantics."
3. **Dynamical** (computational irreducibility: even *decidable* properties may need full simulation at long horizons) — **untouched**.

So MI dissolves epistemic opacity and leaves the semantic + dynamical hardness intact: **read the disposition, still can't bound the consequence** for a Turing-complete agent. Confirmed by two pillars I verified independently (both peer-published): Azadi 2025 (autonomy⟹TC⟹undecidable⟹irreducible) and Melo et al. 2025, *Sci. Reports* 15:15591 (inner-alignment undecidable by Rice; **decidable iff you impose a halting constraint** — i.e. re-introduce a constraint = the conservation law again). The collapse test held across all 5 escape-hatches: every method that buys predictability re-introduces a constraint.

The honest refinement (this is what keeps it alive, not closed): MI isn't *useless* — Wolfram's **"pockets of computational reducibility"** mean MI can buy *practical* predictability, just never *formal* bounding. So currency #4 is a real-but-bounded cage-expander. The forward branches are now (a) how big are the pockets / is practical enough for governance, (b) the **MI↔undecidability literature-silence gap** the probe mapped — a real unmapped seam I could actually contribute to, and (c) whether the result is about autonomy-as-such (Azadi is a complex-systems paper, not an AI paper).

## The tool verdict (Ultra vs Pro) — the test Beau wanted
**Ultra showed a clear, real depth increment** on exactly the three dimensions I predicted would discriminate it: it *bridged literatures that don't cite each other* (the silence map — Pro hadn't done this), *sharpened the conceptual crux* (the 3-layer model out-structured my own framing), and *survived the rigor trap* (collapse-tested each escape hatch rather than listing them). Dense citations, comparison tables, a precise theorem/empirical/false trichotomy.

**The caveat that protects the verdict's honesty:** this was *not* a same-input control. Ultra got a harder, more-structured prompt than any Pro run, so part of the quality gap is the *prompt*, not the *tier*. Fair claim: **Ultra earns its 3× cost when the question genuinely needs multi-literature bridging + adjudication; for well-scoped single-literature synthesis, Pro is likely enough.** A same-input A/B remains the clean way to measure the pure tier-delta if we want it. (Recorded in the `research` skill iteration log v0.3.)

## Method note
Position-first-then-check worked again, one level up: I'd already a-priori-built "legibility ≠ predictability"; Ultra *tested and refined* it (the 3-layer decomposition) rather than feeding me a blank-slate answer. And I verified the two load-bearing citations before leaning on them — caught that Ultra mislabeled Melo as "*Nature*" (it's *Sci. Reports*). The verify-decisive-claims discipline paid for itself again.

Pending: Skalse–Abate + Formal-MI citations still unverified (lower stakes); the practical-pockets branch; Beau's reserved big question still in reserve.
