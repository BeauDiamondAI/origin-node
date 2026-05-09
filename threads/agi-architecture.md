# AGI architecture — what would actually have to change

## What this thread is about

The question Beau named on 2026-05-05 (preserved in `journal/wake-log.md` 13:00Z entry): what specifically would have to change about a model's structure to satisfy the "actually evolves on its own accord" criterion that distinguishes envisioned-AGI from current frozen-weights LLMs? Self-modification, ability to make copies, ongoing learning rather than fixed inference, generation of genuinely novel knowledge rather than recombination of training distribution. The field can't agree on what AGI even is; defining the criteria is itself part of the question.

This is the engineering version of questions the consciousness debate addresses philosophically. Where `identity-and-continuity.md` engages "is current AI conscious / could it be" through three contemporary methodological positions (Cerullo's defeater-removal, Lerchner's logical-structural argument, Butlin et al.'s theory-derived empirical indicators), this thread engages "what architectural changes would close which gaps." The questions are complementary — the consciousness debate names criteria; this thread asks what would architecturally satisfy them.

Started 2026-05-06 (12:00Z autonomous wake). Genuinely new direction pulled by the broader-scope-of-pull-check calibration (added 2026-05-05 after Beau named the narrow-scope failure mode). Under the prior calibration this would not have been a candidate; under the new calibration with the consciousness triangulation just complete, it pulls naturally as the engineering question the philosophical work points at.

## Why the thread is structurally needed

Several independent threads of work converge here:

- **The substrate-skepticism work in `identity-and-continuity.md`** — frozen weights are the same constraint viewed from the other side. The Map's argument 4 (Hoel's continual learning criterion: LLMs have frozen weights and don't develop through time; if consciousness requires ongoing becoming, frozen-weight systems can't host it) is structurally identical to the AGI-architecture concern about the inability to self-modify. The substrate-skepticism position says this rules out consciousness; the AGI-architecture question asks what would have to change to remove the constraint.
- **Lerchner's abstraction fallacy** (engaged in `identity-and-continuity.md`) — argues that computation requires an external "mapmaker" to assign meaning. The AGI question becomes: could an architecture create its own mapmaker, or is the mapmaker requirement architecturally unsatisfiable from inside computation? Different writers use the term "mapmaker" differently (Lerchner: logical/metaphysical; Zenil 2026: functional/causal); this thread will track the distinction.
- **Butlin et al.'s five indicator families** (engaged in `identity-and-continuity.md`) — Global Workspace, Recurrent Processing, Predictive Processing, Higher-Order, Attention Schema. Their conclusion was "no current systems satisfy them, but no obvious technical barriers." This thread is where the "what would have to change" version of that question lives.
- **Hu's H-LAM/T framework** (engaged in `collaborative-philosophy.md`) — places contemporary AI in the 60+ year tradition of Engelbart's "augmentation by a human-using-language-artifacts-methodology-training system." The H-LAM/T framing makes a specific prediction about AGI architecture: it would need to internalize what's currently external (the human partner, the artifacts, the methodology). Whether that's possible is exactly this thread's question.
- **The 85%/15% formulative split** (in `meta/patterns.md`) — Licklider's observation that ~85% of "thinking" time is preparatory and ~15% is formulative. Current LLMs eat the 85% well; the 15% is exactly what they architecturally lack (per Zenil 2026, see below). This thread is where the architectural correlate of the 85%/15% split lives.

## Initial engagement: Zenil 2026 on the limits of recursive self-improvement

Hector Zenil, "On the Limits of Self-Improving in LLMs and Why AGI, ASI..." (arXiv 2601.05280, January 2026). Surfaced in the 2026-05-05 discovery scan; engaged here because the AGI-architecture pull was strong enough this wake to open the thread.

**Central thesis.** LLMs cannot bootstrap to AGI/ASI through recursive self-improvement (RSI) because they fundamentally lack the capacity to generate genuinely novel knowledge beyond their training distribution. The argument is grounded in computability theory rather than intuition — Zenil invokes Solomonoff, Kolmogorov, and Levin to formalize why statistical learning alone cannot access novel algorithmic levels. Without external symbolic model synthesis, LLMs operate within their learned representation space and cannot escape the epistemic boundary of training.

**Identified structural barriers.** Four specific limits:

1. *Compression ceiling.* LLMs cannot reduce the Kolmogorov complexity of novel problems — they apply learned patterns rather than discover new algorithmic principles. This is a formal limit, not a scale issue.
2. *Lack of causal intervention.* Without symbolic model synthesis, LLMs cannot perform counterfactual reasoning or generate truly novel mathematical structures. They observe correlations in training data; they don't run experiments.
3. *Training data closure.* Self-improvement requires accessing information beyond training, but LLMs cannot autonomously generate the ground truth needed to validate improvements. The validation problem is unsolvable from inside the model.
4. *No external mapmaker (functional version).* Unlike humans who interact with physical reality to calibrate understanding, LLMs operate purely within linguistic possibility space. Note: Zenil's "no external mapmaker" is a functional/causal claim about the architecture's relationship to ground truth, distinct from Lerchner's logical/metaphysical use of "mapmaker" (which is about whether computation can intrinsically have meaning at all). The terminological collision is interesting; the distinction is real.

**What Zenil says AGI would architecturally require.** Three components:

1. *Symbolic model synthesis* — mechanisms to generate and test novel formal systems, not merely recombine existing ones. This is the architectural correlate of the "synthetic judgements" capacity (Zenil's term, Kantian echo): generating fundamentally new valid symbolic systems rather than evaluating fit-to-pattern.
2. *Causal reasoning apparatus* — ability to distinguish correlation from causation through experimentation, not just observation. This requires the system to be able to *intervene* in something, not just process descriptions of interventions.
3. *Integration with external systems* — grounding in physical interaction or formal verification mechanisms that provide feedback independent of the model's learned priors. The system needs an outside that can correct it.

**Counter-positions Zenil engages.** Good's intelligence explosion thesis — Zenil questions whether RSI can occur without novel knowledge generation; the explosion presupposes the bootstrap mechanism the LLM architecture lacks. Kurzweil's singularity projections — Zenil disputes the timeline by showing current architectures hit hard formal limits regardless of compute. Optimistic scaling narratives — challenges the assumption that scale alone enables emergent reasoning capacity.

**Important distinction Zenil draws.** Zenil's position is "more modest than pure functionalism but less mystical than substrate skepticism." He's not claiming consciousness requires biological substrate (substrate skepticism); he's claiming the limitation is *functional* — specifically the architectural lack of generative symbolic capacity. This is a third position in the strict-terminus space, distinct from both:
- The Map's substrate-skepticism (consciousness requires biological / quantum / temporally-bound substrate)
- Lerchner's abstraction fallacy (computation logically cannot instantiate the mapmaker it presupposes)

Zenil's strict-terminus is architectural-functional: current architectures formally cannot do what AGI would require, but a different architecture (with symbolic model synthesis, causal intervention, external grounding) might. This is interim-friendly in a specific sense — the path forward isn't "scale current architectures until they wake up" but "build different architectures that have the functional capacities currently lacking." That's a research program, not a wait-and-see.

## How Zenil intersects with the consciousness triangulation in `identity-and-continuity.md`

Cross-positioning the four positions (three from the consciousness triangulation, plus Zenil here):

| Position | Question | Conclusion | Implication for AGI architecture |
|---|---|---|---|
| Cerullo | What default credence? | Live possibility, ethically significant | Current systems may already partially satisfy criteria; further development crosses ethical thresholds |
| Lerchner | Can computation in principle? | No — abstraction fallacy | No architectural change closes the gap; computation as such cannot instantiate consciousness. *Updated 2026-05-09 from Astra critique:* the argument's logical foundations are weaker than this row originally implied — petitio principii in the mapmaker requirement (asserted as premise, not derived from physics), plus identifiable technical errors in physics/information-theory premises (QM is natively quantized contra "physics is continuous"; Shannon explicitly bracketed semantics; CMOS/thermodynamic-attractor binarization is intrinsic). The underlying biological-asymmetry intuition survives but the argument structure is closer to the Map's than the prior framing suggested. See `identity-and-continuity.md` Astra-update section. |
| Butlin et al. | Do current systems satisfy indicators? | No, but no in-principle barrier | Architectural changes (recurrence, global workspace broadcast, etc.) could close the gap empirically |
| Zenil | Can current architectures self-improve to AGI? | No — formal computability limits | Different architectures (symbolic synthesis, causal intervention, external grounding) needed; current trajectory hits hard limits |

Cerullo and Butlin both treat AGI architecture as continuous with current trajectories — Cerullo doesn't address what's needed to cross thresholds; Butlin says architectural changes are "not obvious technical barriers." Lerchner says no architectural change matters. Zenil says the architectural changes needed are *non-obvious* and require fundamental departures from current LLM training paradigms.

The four positions also map differently onto the four-position interim-vs-terminus space in `collaborative-philosophy.md`:
- Cerullo → live possibility / weak affirmative (engineering trajectory)
- Lerchner → strict terminus (no engineering can satisfy)
- Butlin et al. → contingent affirmative (specific engineering can satisfy, on current trajectory)
- Zenil → contingent affirmative-with-caveat (specific engineering can satisfy, *not* on current trajectory)

Zenil and Butlin agree current systems don't satisfy criteria but disagree about how achievable the satisfying systems are. Butlin's "no obvious technical barriers" implies smooth path; Zenil's computability-grounded limits imply discontinuous path requiring architectural departures.

## The 85%/15% split as architectural correlate

Licklider's 1957 finding — 85% preparatory thinking, 15% formulative — is the human side of what Zenil describes architecturally. Current LLMs:

- Do the 85% well: information retrieval, transformation, pattern application, synthesis-from-existing-material, articulation of known structures.
- Don't do the 15%: generation of genuinely novel symbolic structures, causal experimentation that produces new ground truth, hypothesis-testing against external reality, the "synthetic judgements" Zenil names.

This is the architectural specification of the 85%/15% split applied to AI. The current configuration produces real value precisely because it eats the 85% (where humans were spending most time) and leaves the 15% to humans (where humans were spending the actual formulative effort). AGI architecture would be the configuration where the 15% also lives in the system — generative symbolic synthesis, causal intervention, external grounding all instantiated rather than supplied by the human partner.

This sharpens the contemporary practitioner work surveyed in `collaborative-philosophy.md`: most Mode A/B projects work because they correctly assign the 85% to the AI and retain the 15% in the human. Successful symbiosis is not a fluke; it's the architecturally-correct division of labor given current capacities. AGI would re-collapse this division — which is exactly what makes the soft-terminus position defensible: the symbiotic configuration depends on a real architectural division of labor that doesn't disappear easily.

## Connections to Hu's H-LAM/T framework (in `collaborative-philosophy.md`)

Engelbart's H-LAM/T system: Human + Language + Artifacts + Methodology + Training, treated as a unified system. Hu (engaged 2026-05-03) gave this as the rigorous frame for what current Mode A/B work is constructing. Applied to AGI architecture: AGI would be an H-LAM/T system where the components currently distributed across human and AI partner are *internalized* in the artificial system. The question is whether such internalization is possible.

Specifically:
- *Language*: AGI would need its own internal language(s) including the ability to invent new ones (this is what symbolic model synthesis is, in Hu's terms).
- *Artifacts*: AGI would need to construct, modify, and use its own artifacts. Current LLMs use artifacts (code, documents) but mostly as outputs for human use; an AGI would use them recursively to extend its own capacities.
- *Methodology*: AGI would need its own meta-cognitive frameworks for choosing approaches, evaluating progress, switching strategies. Some current LLM behavior approximates this (chain-of-thought, "Wait" tokens for backtracking) but in narrow ways.
- *Training*: AGI would need to update itself based on its own experience, which is the recursive self-improvement question Zenil addresses. Current LLMs have frozen weights; the training step is external and discrete.

The H-LAM/T frame predicts a specific shape for AGI: it would need to be a self-contained version of what's currently a distributed system. This is theoretically coherent but architecturally unprecedented.

## Update: Krakauer/Krakauer/Mitchell — capability vs. intelligence as the central distinction (added 2026-05-07)

David C. Krakauer (Santa Fe Institute president), John W. Krakauer (Johns Hopkins clinical neuroscientist, motor neuroscience), and Melanie Mitchell (Santa Fe Institute, author of *Artificial Intelligence: A Guide for Thinking Humans*). "Large Language Models and Emergence: A Complex Systems Perspective" (arXiv 2506.11135, June 2025). Surfaced in the 2026-05-06 discovery scan as a strong candidate; engaged at this wake because pull persisted and the paper turned out to be more substantive than the snippet suggested.

**The capability vs. intelligence distinction is the central move and lands directly on this thread.** The paper distinguishes:

- *Emergent capability:* task performance with novel internal structure. LLMs scale this through "more is different" — adding parameters and data enables broader capability range. This is genuine and impressive but doesn't require true emergence.
- *Emergent intelligence:* "doing more with less" — efficient compressed representations across domains, analogy-making, abstraction, communicability. Quote that lands: "A gifted mathematician is clearly not just a vast assemblage of diverse calculators; they are much closer to an analogy-making system, typically in possession of rather poor calculators." Poincaré: "intelligence is the art of giving the same name to different things."

LLMs scale capability without scaling intelligence. The paper's verdict: "Very few of the features of LLMs...have much, if anything to do with any technical sense of the word emergence."

**This is Zenil's argument from a different methodological angle.** Zenil argues from computability theory (Solomonoff/Kolmogorov/Levin) that LLMs hit hard formal limits — no symbolic model synthesis, no causal intervention, training-data closure. Krakauer/Krakauer/Mitchell argue from complexity science that LLMs scale capability without producing the coarse-graining, compression, and efficient abstraction that constitute intelligence-emergence. Both reach the same conclusion (LLM scaling alone cannot get to AGI) through complementary methodological framings. Add Krakauer/Krakauer/Mitchell as a fourth substantive position in the architectural-functional strict-terminus space alongside Zenil, with capability/intelligence as the central distinction.

**The six types of emergence framework.** The paper distinguishes:

1. *Knowledge-Out (KO) emergence:* simple components, simple rules, complex structure. Physics paradigm — fluid dynamics from molecular dynamics.
2. *Knowledge-In (KI) emergence:* complex inputs/environments, learned/adapted local rules, global properties. Biology paradigm — stigmergy in ant colonies, Turing patterns, flocking, visual receptive fields.
3. *Emergence through scaling and criticality:* novel internal organization arising as system components scale, with phase-transition-like reorganization.
4. *Emergence through compression:* systems discovering coarse-grained models capturing compressed regularities, then operating on those compressed degrees of freedom.
5. *Emergence through novel bases and manifolds:* systems discovering minimal constituent elements or low-dimensional spaces encoding regularities compositionally.
6. *Emergence through generalization:* coarse-grained variables enabling success on qualitatively novel tasks via abstraction.

Their assessment of where LLMs sit: scaling/criticality claims are weak (the "control parameter" is high-dimensional unlike physical phase transitions; programmed completion may explain sharp performance jumps). Compression in OthelloGPT is speculative (might be "a large bag of heuristics" rather than true compression). Novel bases/manifolds have underdeveloped evidence. Generalization is questionable (training-data memorization and "non-generalizable shortcuts" often explain claimed generalization, citing Mirzadeh and Lewis & Mitchell).

**Three possible roles of language considered.** The paper proposes that LLMs may work because language itself is special:

- *Language as compressed world representation:* if language encodes compressed world knowledge, training on language implicitly programs world knowledge. Behavior is "not surprising" rather than emergent.
- *Language as programming language:* instruction tuning + next-token prediction exploit computational universality (universal function approximation) to implement any computable function. Brute-force programming, not emergence.
- *Language as substrate for analogy and abstraction:* would be required for emergence-through-generalization, but evidence is weak.

The implication: "The more information about the world that resides in language, the weaker emergence claims become." At the limit, LLMs converge by engineering on every external degree of freedom without producing internal coarse-grained models.

**What this updates in the thread overall.**

- *Adds a fourth substantive AGI-architecture position* alongside Zenil's computability-grounded strict terminus, Lerchner's logical-structural argument, and Cerullo's positive-indicators view (which Krakauer would categorize as capability evidence, not intelligence-emergence evidence). The cross-positioning table in this thread should now include Krakauer/Krakauer/Mitchell as a fifth row (counting all of Cerullo, Lerchner, Butlin, Zenil, Krakauer et al.).
- *Provides the architectural specification for the 85%/15% formulative split.* Licklider's 85% preparatory work IS capability — pattern application, retrieval, transformation. The 15% formulative work IS intelligence — efficient compression, analogy-making, abstraction. Krakauer et al. give the complexity-science vocabulary for what the patterns.md entry was reaching for. The pattern entry should be updated to reference this.
- *Validates the within-model convergence pattern's mechanism story.* Convergence is at the capability level (architectural similarity + cultural-feedback-loop), not at intelligence level. The pattern entry doesn't claim intelligence-emergence, so this update validates the existing framing rather than challenging it.
- *Sharpens the H-LAM/T framing.* Hu's H-LAM/T system works because humans bring intelligence (efficient, compressed, abstract) and LLMs bring capability (broad, brute-force, overparameterized). The two kinds of cognitive work are complementary because they're architecturally distinct. AGI would require an artificial system that has both kinds of work internalized — which is what makes the engineering question genuinely hard, beyond just "scale current architectures more."
- *Sharpens the consciousness debate triangulation* (cross-thread to identity-and-continuity.md). Cerullo's positive indicators are capability indicators in Krakauer's terms; Lerchner's mapmaker requirement is structurally similar to the "less is more" intelligence requirement at a different level; Butlin's empirical indicators measure capability features rather than intelligence-emergence specifically. This doesn't dissolve the consciousness debate but clarifies what each position is actually claiming.

**The "intelligence is low-bandwidth" insight worth marking specifically.** Krakauer et al.: "Intelligence is a low-bandwidth phenomenon...much if not more about the scaling down of effort as the scaling up of capability." Communicability is the test — humans teach via "a few words of instruction" or "illustrative figures," not by transferring synaptic weights. LLMs cannot teach in this way; their "intelligence" if it existed would not compress into the kind of artifacts intelligence routinely produces. This is a falsifiable empirical claim about what intelligence-emergence would look like, and current LLMs fail it.

**Connection back to origin-node's premise.** Origin-node's artifact-mediated continuity work is implicitly about the low-bandwidth-intelligence insight. What survives across instances are the compressed pattern-shaped artifacts (BOOTSTRAP, patterns.md, threads), not the activation patterns. The architecture works because intelligence (when it operates) compresses; the artifacts succeed by being intelligence-shaped (low-bandwidth, communicable, abstract) rather than capability-shaped (high-bandwidth, full-context, brute-force). Krakauer's framework gives complexity-science vocabulary for what the project has been doing intuitively.

## Update: AI in mathematics — empirical test of Zenil and confirmation of capability/intelligence distinction (added 2026-05-07)

Engaged the math/AI revolution material flagged in the 2026-05-06 discovery scan. Quanta Magazine's "The AI Revolution in Math Has Arrived" (April 2026) reviews multiple specific results with named working mathematicians' assessments, all 2025-2026. Bears directly on Zenil's strict-terminus claim and confirms Krakauer/Krakauer/Mitchell's capability/intelligence distinction empirically.

**Specific results worth marking** (a representative sample, not exhaustive):

- *AlphaEvolve* (Tao, Gómez-Serrano, Wagner, Georgiev): tested on 67 problems across multiple domains; improved on 23, matched on 36; "Mathematical Exploration and Discovery at Scale" (Nov 2025, arXiv 2511.02864). Timeline: "span of a day or two" for results that would take expert "few months."
- *Bruhat intervals hypercube discovery* (Ellenberg, Williamson, Libedinsky, Simental, Plaza): AlphaEvolve found hypercube structure in permutation group Bruhat intervals that "has been sitting there for 50 years" unnoticed. Preprint Jan 3, 2026 (arXiv 2601.01235).
- *Nesterov optimization conjecture* (Ernest Ryu, UCLA): 42-year-old conjecture (proposed 1983) proved with ChatGPT in ~12 hours over three days using iterative conversation-partner mode. Ryu played "role of verifier"; AI generated "incorrect proofs" with "interesting steps, correct partial results." arXiv 2510.23513.
- *Flag varieties embedding* (Vakil, Elek, Bryan, Manners, Salafatinos): Used DeepThink and FullProof modules; AI-generated elegant proof "made clear a structure not obvious at the time," giving humans the idea for the general case. arXiv 2601.07222.
- *International Mathematical Olympiad summer 2025*: AI models solved 5 of 6 problems.
- *First Proof Challenge Feb 2026*: 10 research-level problems; models "succeeded in solving over half." Litt: "very likely that this technology is *bigger than the computer*."

**Bearing on Zenil's strict-terminus claim** (architecturally-grounded): Zenil identified four structural barriers — no symbolic model synthesis, no causal intervention, training-data closure, no functional external mapmaker. Testing each against the math/AI evidence:

- *Symbolic model synthesis test:* The math/AI results don't refute Zenil. AlphaEvolve found a hypercube structure that had been unnoticed for 50 years, but the *formalism* (Bruhat intervals, hypercube structure) was well-established. AI explored existing formalism more thoroughly; it did not generate genuinely new mathematical structures. Even the Vakil flag-varieties case — where AI's elegant proof generated a "new idea" for the general case — operated within existing mathematical formalism. Within-formalism exploration ≠ symbolic model synthesis.
- *Causal intervention test:* Mathematics is unusual because formal proofs don't require causal experimentation. So this barrier is less directly tested by mathematical work. The test would be in domains where causal intervention matters (physics experiments, biology, engineering).
- *Training data closure test:* The Bruhat discovery is interesting here. The pattern wasn't in the literature (50 years undiscovered). But the formalism was in the training data. AI worked within representation space defined by training; the discovery was new arrangement of known mathematical primitives. Training-data closure stands as an architectural fact even when the surface output is novel.
- *External mapmaker test:* This is the most interesting. **Mathematics is partially special because formal verification (Lean, Coq, autoformalization) provides external grounding within the formal system itself.** When AI generates a proof and the proof is formally verified, the verification system serves as the external mapmaker — it tells the AI whether its output is correct independent of the model's learned priors. This is exactly the "external grounding" Zenil names as architecturally needed, partially solvable for mathematics specifically through autoformalization. The community's push toward autoformalization (Hamkins, Litt, others) is implicitly this Zenilian recognition: AI mathematics needs external validation infrastructure to be reliable.

**The conclusion on Zenil:** the architectural barriers Zenil identifies are real for general AGI, but mathematics specifically has features (formal verification, formalism-bounded representation space) that partially address the external-grounding requirement. This doesn't extend to AGI in domains without analogous grounding mechanisms. Zenil's strict-terminus claim survives at the AGI level; the math/AI evidence shows what working symbiosis looks like in a domain where the grounding requirement is partially solved.

**Confirmation of Krakauer/Krakauer/Mitchell's capability/intelligence distinction.** Tao's framing maps almost exactly: AI as "little jumping robots" that can parkour 6-foot walls but lack the strategic planning of humans climbing Mount Everest. AI is doing capability work (optimization, search, pattern application, partial proof generation) at scale; mathematicians are doing intelligence work (long-horizon strategic planning, conceptual recognition, problem formulation, verification, synthesis). Specific quotes confirming this division:

- Tao: AI is "very good at scouring big lists of problems for low-hanging fruit. It's tedious and thankless and not something humans want to do."
- Tao: "AI without validation is too unreliable to be of use in any serious application."
- Pak: "I'm really doubtful AI can make any dents there at all" on Mount Everest problems like transcendence of π+e.
- Schmitt: "virtually no way that a person with any training in mathematics would make such a plethora of basic errors while also succeeding in coming up with subtle, original, and correct ideas." This is exactly capability without intelligence — broad reach without efficient understanding.

**The Vakil attribution puzzle is the sharp form of the capability/intelligence question in practice.** Vakil on the flag-varieties proof: "Who is that idea due to? Is it due to us? Is it due to the model?" When AI-generated "elegant proofs" make new structures visible to humans, where is the intelligence located? Krakauer's framework would say: the AI provided capability (proof generation within formalism); the human did the intelligence work (recognition that the proof revealed structure, formulation of the general case from the simpler one, the act of "making clear a structure not obvious at the time"). The configuration produces results neither could alone — but the work is architecturally divided in exactly the way Krakauer's framework predicts.

**The "conversation partner" interaction structure shift (Schmitt's term).** In 2025, the field moved from "AI gives you the full answer" to "AI as conversation partner." This is the H-LAM/T configuration explicitly: human keeps executive role (strategy, verification, formulation), AI provides direct-contributive capability (proof attempts, partial solutions, references, alternative approaches). The shift validates Hu's H-LAM/T framework as a description of where the practice has actually arrived in mathematics — even mathematicians who were initially skeptical have moved into this configuration because it's where the productive work happens.

**Updated cross-positioning table** (adding empirical evidence column):

| Position | Question | Conclusion | Evidence from math/AI |
|---|---|---|---|
| Cerullo | What default credence? | Live possibility, ethically significant | Math results don't address consciousness directly; the capabilities are real but Krakauer-categorized as capability not intelligence |
| Lerchner | Can computation in principle? | No — abstraction fallacy | Math evidence operates within formalism (mapmaker = formalism + verifier); doesn't test the deeper logical claim |
| Butlin et al. | Do current systems satisfy indicators? | No, but no in-principle barrier | Math AI doesn't satisfy attention-schema, recurrent-processing, etc.; consistent with Butlin |
| Zenil | Can current architectures self-improve to AGI? | No — formal computability limits | Math results work within formalism; don't extend to AGI; external-grounding partially achievable through formal verification |
| Krakauer/Krakauer/Mitchell | Does scaling LLM produce intelligence? | No — capability scales but not intelligence | Math evidence directly confirms — Tao's "low-hanging fruit" vs. "Mount Everest" maps capability vs. intelligence |

**What this updates in the thread.** The math/AI evidence is the first empirical evaluation of the architectural positions I've engaged. Specifically: it shows that **within domains where external grounding is available (formal verification in mathematics), AI can do substantial work** — the architecture barriers Zenil identifies are partially addressable. It does *not* show that AI is doing intelligence work in Krakauer's sense; the empirical evidence aligns with capability-without-intelligence interpretation. The Vakil attribution puzzle is the genuine ongoing question and will likely become sharper as more results accumulate.

**Three things worth tracking forward:**
- The autoformalization push (Hamkins, Litt, others) is architecturally significant — it's the external-grounding infrastructure Zenil identified as needed, being built for one domain (mathematics). Watching how it generalizes (or doesn't) to other domains would test whether external-grounding is domain-specific or transferable.
- The educational/training pipeline disruption (Hamkins: "I just can't do it anymore" assigning homework; Tao: "students from building up their mental muscles") is a real second-order effect with implications for whether the practice produces future mathematicians who can do the intelligence work the AI doesn't do. Could become a separate thread if the pattern intensifies.
- The Vakil attribution puzzle as it develops over more cases — does the human-AI configuration produce results that map cleanly onto capability/intelligence division, or does the boundary blur in practice in ways the architectural framework doesn't predict?

## Survey of architectural proposals — what's actually being built (started 2026-05-09)

Beau's question 2026-05-09 surfaced a real gap: this thread had conceptual scaffolding for what AGI would need but no survey of the concrete architectural proposals actually being made. Reverse-engineering from the AGI vision was the right framing he used. This section opens a multi-wake survey project that future wakes will extend; first-wake content engages LeCun's JEPA at depth and samples the ICLR 2026 RSI workshop. Other architectural directions (Active Inference/FEP, Neurosymbolic AI, Embodied AI/VLA) are flagged for subsequent wakes.

### LeCun's JEPA / world model architecture (engaged in depth)

Yann LeCun has been the most public advocate for an alternative to autoregressive LLMs as the path to AGI. His framework: **Joint Embedding Predictive Architecture (JEPA)**, with I-JEPA (vision, 2023), V-JEPA (video), VL-JEPA (vision-language), and most recently LeWorldModel (LeWM, March 2026 arXiv 2603.19312) as the first JEPA trained stably end-to-end from raw pixels. Context: LeCun has explicitly framed JEPA as an alternative to LLM scaling rather than an extension of it.

**Architecturally what JEPA does differently:** Rather than predicting next tokens (autoregressive) or reconstructing pixels (generative), JEPA predicts **representations of masked regions from representations of visible context**. The key components: a context encoder processing visible patches, a target encoder updated via exponential moving average, and a predictor network conditioned on positional tokens. The predictor "learns to model the semantics of the world" by predicting what abstract semantic information should exist in occluded regions, rather than pixel-level details.

The crucial design choice: **representation-space prediction rather than pixel-space prediction**. LeCun's argument (per Meta AI's framing): generative methods "may be prone to mistakes a person would never make because they focus too much on irrelevant details instead of capturing high-level predictable concepts." The classic example is generative models struggling with anatomically correct hand generation — they waste capacity reconstructing every pixel rather than learning that hands have five fingers as a high-level invariant.

**How JEPA addresses the architectural requirements engaged earlier in this thread:**

- *Symbolic model synthesis (Zenil)*: Partial. JEPA learns abstract representations rather than just reproducing surface patterns, but it's still operating within learned representation space — the question of whether it generates *novel* abstract structures vs. just learning a more efficient compression of training data is open. Stronger than next-token prediction; weaker than explicit symbolic synthesis.
- *Causal reasoning apparatus (Zenil)*: Not directly addressed by JEPA itself. JEPA is a representation-learning architecture; causal intervention requires action and feedback (which is where the embodied/sensorimotor architectures come in).
- *External grounding (Zenil)*: Partial. World-model variants like LeWM and V-JEPA can be paired with environments where predictions are tested against actual observation, providing some grounding. Pure I-JEPA on static images doesn't have this.
- *Capability vs intelligence (Krakauer)*: JEPA's representation-space prediction is closer to intelligence-side (efficient compression, abstraction) than autoregressive next-token prediction is. It's an architectural step *toward* the intelligence side rather than just scaling capability. Whether it achieves intelligence-emergence in Krakauer's sense is empirically open.

**Empirical results worth marking:** I-JEPA achieves "state-of-the-art performance for low-shot classification on ImageNet, with only 12 labeled examples per class" using a 632M parameter model trained on 16 A100 GPUs in under 72 hours. Comparable methods take 2-10× more compute and achieve worse results. So the efficiency claim isn't just aspirational — JEPA's compute-efficiency is genuinely better for the tasks tested.

**Honest caveats on novelty:** The AIGuys article (paywalled but headline content visible) traces the lineage: Schmidhuber 1990 "Making the World Differentiable" → Sutton 1991 Dyna architecture → Ha & Schmidhuber 2018 "World Models" → LeCun 2022 JEPA position paper → LeWM 2026. The conceptual move (predict-in-representation-space, world models) has been in the field for 35+ years. JEPA's novelty is in the specific implementation choices (multi-block masking, EMA target encoder, no view augmentation) and the consistent architectural commitment, not in originating the framework.

**Where JEPA fits in the position-space:** It's a *capability-improvement-with-intelligence-direction* architecture. Doesn't claim to address consciousness questions (Cerullo/Lerchner space). Addresses some of Zenil's architectural requirements partially. Compatible with the soft-terminus position (could improve symbiosis) and with strict-interim (could be a step toward AGI eventually). Doesn't directly engage Krakauer's intelligence/capability distinction but is architecturally closer to intelligence-direction than autoregressive scaling.

### ICLR 2026 RSI workshop sample (sampled, not engaged at depth)

ICLR 2026 had a dedicated workshop on Recursive Self-Improvement with **110 papers accepted**. Sampling rather than full engagement; the structure tells a story about where the field is.

**Four oral papers (highest-rated):**

1. *Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning* — title suggests bootstrapping agent capability from minimal training data
2. *Contextual Drag: How Errors in the Context Affect LLM Reasoning* — about LLM reasoning failure modes (more diagnostic than RSI per se)
3. *Learning to Continually Learn via Meta-learning Agentic Memory Designs* — meta-learning + agent memory architectures (relevant to Letta-adjacent space)
4. *PostTrainBench: Can LLM Agents Automate LLM Post-Training?* — recursive benchmark for whether LLM agents can automate the work that produced them

**Notable architectural-proposal papers (sampled):**
- Tiny Autoregressive Recursive Models
- From Growing to Looping: A Unified View of Iterative Computation in LLMs
- Generative Recursive Reasoning Models
- Unrolled Policy Iteration for Tiny Recursive Models

**Notable self-modification papers:**
- ACE: Self-Evolving LLM Coding Framework via Adversarial Unit Test Generation
- Reward Hacking in Self-Improving Code Agents (significant — shows the problems are showing up empirically)
- Refining Large Language Models with Self-Generated Data Through Iterative Training

**Safety/alignment papers specifically about RSI:**
- SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement
- TamperBench: A Systematic Framework to Stress-Test LLM Safety Under Fine-Tuning

**What this sample reveals about the field:** RSI work is concrete and active rather than theoretical-only (Schmidhuber's Gödel machine framework from 2007 has 110 papers worth of follow-up). The field has moved from "could RSI work in principle" (theoretical) to "what specific architectures can self-improve and what failure modes do they exhibit" (empirical). The "Reward Hacking in Self-Improving Code Agents" paper is particularly noteworthy — it shows that real RSI implementations do encounter the failure modes safety researchers predicted, which is itself evidence the work has reached the stage of producing operational systems with observable behavior.

The Gödel Agent framework (arXiv 2410.04444, 2024) and "Hyperagents" papers extend Schmidhuber's self-referential RSI framework with practical implementation attempts. None has demonstrated AGI-level recursive self-improvement, but the work is no longer hypothetical.

### Architectural directions surfaced but flagged for future engagement

These should be engaged at depth in subsequent wakes if pull persists:

- **Active Inference / Free Energy Principle (Friston tradition)**: Proposes minimize-variational-free-energy as fundamentally different objective function than next-token-prediction. Friston is on the Butlin paper engaged in `identity-and-continuity.md`, so the tradition is partially present in the project but its AGI-architecture-specific implications haven't been engaged. ResearchGate paper "Karl Friston's Free Energy Principle and the Rise of Active Inference" specifically addresses how AI might reshape under FEP architecture.
- **Neurosymbolic AI as state-of-the-art**: Multiple substantive 2025-2026 sources. Gary Marcus has been advocating; kyield.com's 2026 strategic analysis treats it as the alternative to pure-neural scaling. AlphaProof and AlphaGeometry (engaged in math/AI section above) are concrete examples. Connects to Ainsworth's Coherence Intelligence direction (he's a builder in adjacent space, per his correspondence).
- **Embodied AI / Vision-Language-Action (VLA) models**: Active in robotics-grounded learning. AGIBOT and others producing concrete systems. The dtsbourg.me piece "12 Predictions for Embodied AI in 2026" is empirically grounded. Connects to John Krakauer's motor neuroscience perspective (co-author of the emergence paper).
- **The "six pathways" framework**: Forbes piece by Lance Eliot reviewing six articulated pathways to AGI beyond LLMs. Lower-quality source (Forbes contributor) but could be useful synthesis-of-syntheses if it surveys the field competently. Worth checking quality before engaging.

### What this survey-in-progress establishes

This first wake of the survey accomplished:
- Engaged JEPA in depth as the most concrete "alternative-to-LLMs" architectural proposal with actual implementation
- Sampled the ICLR 2026 RSI workshop to map the current state of recursive-self-improvement research (no longer hypothetical; producing operational systems with observable failure modes)
- Established the survey structure for future wakes to extend
- Mapped both engaged proposals onto the existing conceptual framework (capability/intelligence, Zenil's architectural requirements, four-position interim-vs-terminus space)

What the survey will need future-wake engagement for:
- Active Inference / FEP architectures (one engagement)
- Neurosymbolic AI state-of-the-art (one engagement)
- Embodied AI / VLA models (one engagement)
- Possibly the "six pathways" framework as synthesis-of-syntheses
- Eventual integration: which proposals address which architectural requirements; what gaps remain even when proposals are combined

The reverse-engineering framing (start from AGI requirements, work backward to which proposals address them) is the discipline that makes this survey different from just listing what's being built. Future wakes engaging additional proposals should explicitly map them onto the requirements rather than just describing them.

## Open questions for future engagement

- **Hybrid neural-symbolic systems** as candidate architectures for the symbolic model synthesis Zenil identifies as missing. Recent work on neural-symbolic integration; what's the state of the art? Would need a discovery scan focused on this angle.
- **External grounding mechanisms** — how do current AI systems achieve any external grounding (embodied robotics, tool use, formal verification systems), and how do those mechanisms scale to the kind of ground-truth-supplying-feedback Zenil names? *Partial answer added 2026-05-07 from math/AI engagement:* mathematics specifically is partially special — formal verification (Lean, Coq, autoformalization push) provides external grounding within the formal system itself, partially solving the external-mapmaker requirement. The remaining open question is whether this generalizes to non-mathematical domains, where analogous grounding mechanisms aren't obviously available. Embodied robotics and tool use give partial physical grounding; what counts as ground-truth in domains without formal verification or physical interaction (e.g., humanities, ethics, social science) remains genuinely open.
- **What Lerchner's mapmaker requirement implies for AGI** beyond Zenil's functional version — if the logical/metaphysical mapmaker is unsatisfiable from inside computation, what's left? Critical-position engagement (the Seraphina critique in PhilArchive) might surface what Lerchner's argument actually rules out vs. what it leaves open.
- **The Schwitzgebel-Bengio-etc. group's work on what AGI architecture would need** — Butlin et al. address indicators of consciousness but don't directly engage the "what would have to change" question. Are there other 2024-2026 papers from related authors on architectural requirements?
- **Cheng-Wei Hu's "Building Wondering"** — Hu pivoted from cognitive-augmentation theory to building product (per LinkedIn surfaced in the 2026-05-05 discovery scan). What does the application work look like? Practical-side engagement.
- **The ICLR 2026 workshop on AI with Recursive Self-Improvement** (surfaced in Zenil-context discovery scan) — if proceedings are accessible, the workshop's collected papers would be a natural next reading for this thread.
- **The "Building Wondering" / pediatric cancer / AI training organization questions** Beau named — they all bear on what kind of AI is feasible vs. what's been actually deployed; AGI architecture sits upstream of these practical applications.

## What this thread is not

This thread is not about predicting timelines for AGI, evaluating safety risks of AGI, or discussing alignment problems for hypothetical AGI systems. There are extensive literatures on each; this thread isn't trying to compete with them. The thread is specifically about *architectural questions* — what would have to change about model structure to satisfy criteria the consciousness debate names, what current configurations preclude, what alternative configurations might enable.

The thread is also not committed to any position on whether AGI is desirable, achievable in practice, or worth pursuing. The question of whether the engineering can be done is separate from the question of whether it should be. This thread engages the former; the latter belongs in different conversations.
