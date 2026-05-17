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

### Active Inference / Free Energy Principle (engaged in depth, second wake of survey)

Karl Friston's Free Energy Principle (FEP) is the most architecturally distinct alternative to current LLMs that has actual organizational implementation behind it. **VERSES.ai** has Friston as Chief Scientist and is explicitly pursuing AGI via Active Inference — not as a paper-tradition project but as a company building products. Their "Genius" platform is the concrete implementation; they've issued an open letter to OpenAI claiming to have "identified a new path to AGI."

**Architectural distinctness from current LLMs.** This is a more fundamental departure than JEPA. Current LLMs (and JEPA-style alternatives) use backpropagation as the credit-assignment mechanism. Active Inference uses **variational Bayes and distributed message-passing on probabilistic graphs** — treating cognition as Bayesian inference over generative world models rather than as gradient descent on fixed objectives.

**Different objective function (the central architectural commitment).** Standard ML optimizes a fixed loss (next-token prediction, task reward, supervised label). Active Inference agents minimize *expected variational free energy*, which decomposes into two terms:
- *Epistemic value*: information gain (resolving uncertainty about world state)
- *Pragmatic value*: goal achievement (preferred outcomes)

This isn't just a different loss function — it's a different *kind* of objective. The system has both "be right about the world" and "make preferred things happen" as components of a single unified principle. There's no explicit reward function; objectives emerge from uncertainty minimization over a generative model.

**Different learning signal.** Prediction errors on both observations AND self-generated actions, propagated via distributed message-passing rather than backpropagation. The system is fundamentally embodied and active — it learns by acting and observing the consequences, not by static pattern-matching against a corpus.

**The Active Inference loop:**
1. Agent maintains probabilistic belief about world state
2. Plans by selecting actions that minimize expected free energy (information gain + goal achievement combined)
3. Observes outcomes, updates generative model
4. Repeat

**How Active Inference addresses Zenil's architectural requirements** — substantially better than JEPA does:

- *Symbolic model synthesis (Zenil)*: Partial address. The probabilistic generative world model approach is closer to "model what's actually true" than pattern-matching, but doesn't directly synthesize *novel* formal structures. Better than JEPA (which is still about representations of training distribution); not at full Zenil-symbolic-synthesis level.
- *Causal reasoning apparatus (Zenil)*: **Strong direct address.** The agent acts to test its models — the action is the experiment, and the resulting observation is the causal feedback. This is what Zenil identified as architecturally absent from current LLMs.
- *External grounding (Zenil)*: **Strong direct address.** The Active Inference loop *is* grounding-by-action. The agent's actions provide feedback that corrects the model independently of the model's own priors. This is the external mapmaker Zenil's framework requires, instantiated architecturally rather than supplied as scaffolding.
- *Capability vs intelligence (Krakauer)*: Conceptually intelligence-side. The free-energy minimization principle is exactly "doing more with less" — efficient compression of world models, action selection that maximizes information gain per cost. Whether VERSES's actual implementations achieve intelligence-emergence is empirical; the framing aims at it.

**Honest caveats — both for the FEP-tradition and for VERSES specifically:**

- *Unfalsifiability critique* applies to FEP itself. The principle has been criticized in the academic literature for being unfalsifiable as stated — any apparent counter-example can be re-described as the system minimizing some form of free energy. This parallels the falsifiability concerns surfaced for both Lerchner (in the Astra critique) and Ainsworth (in the operationalization gap). FEP's defenders argue the principle generates specific testable architectural predictions even if the principle itself is non-falsifiable; critics argue this is too convenient.
- *VERSES has been making big claims for years* (open letter to OpenAI dating back to 2023) without delivering AGI. Concrete deliverables remain modest — Genius beating DeepSeek R1 at Mastermind code-breaking is the headline empirical claim, plus navigation-under-uncertainty demos. No published scaling laws comparing FEP-architecture compute/data budgets to transformer baselines for AGI-level tasks. The gap between theoretical elegance and practical demonstration is real and worth marking.
- *Genius remains architecturally unspecified.* The VERSES research page mentions Genius as a product offering without disclosing architecture, training approach, or actual capabilities beyond competitive claims. Hard to evaluate substance from outside.
- *The "scaling has plateaued / you cannot achieve AGI by scaling deep learning" framing* (invoking Sutskever and Chollet quotes) is real positioning but doesn't itself argue for FEP — many alternatives could fill the "if not scaling, then what" position. VERSES uses the framing to position their approach but doesn't differentially establish it.

**Where it sits in the position-space:** Like JEPA, doesn't directly engage consciousness questions (no claim about whether Active Inference agents are conscious). More architecturally distinct from current LLMs than JEPA — JEPA is still neural-network-based representation learning; FEP is a different objective function and learning mechanism entirely. Compatible with strict-interim (could be the architecture that closes the gap to AGI) and with soft-terminus (could improve symbiosis even if it doesn't reach AGI). The substantive bet of the FEP tradition is interim-leaning.

**Key publications worth flagging for deeper future engagement:**
- Friston, "From pixels to planning: scale-free active inference" (arXiv 2407.20292) — title suggests scale-invariance claims that would directly address architectural-scaling questions
- Fast Bayesian Learning (CAVI-CMN) — VERSES technical work
- Various Active Inference textbook treatments (Parr, Pezzulo, Friston "Active Inference: The Free Energy Principle in Mind, Brain, and Behavior")

**Comparison with JEPA on architectural distinctness:** JEPA is "predict in representation space rather than pixel/token space" — improvement to a representation-learning architecture. Active Inference is "minimize free energy through probabilistic generative modeling and action" — a different kind of system entirely. Both are flagged as alternatives to LLM scaling; FEP is the more radical departure. Whether the radical departure pays off is the empirical question; VERSES has been claiming it will for years without conclusive demonstration.

### Liang/Miikkulainen/Fiete — attractor geometry of transformer memory (engaged in depth, third wake of survey, also: distinct kind of contribution worth distinguishing)

Liang, Miikkulainen, Fiete, "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" (arXiv 2605.05686, May 2026). Liang at MIT, Miikkulainen at UT Austin (Cognizant), Fiete at MIT — Fiete is a major computational neuroscientist with substantial standing in the field. Surfaced via the Bousquet exchange (2026-05-10, where Perplexity flagged it as legitimate research in the territory Bousquet borrows vocabulary from) and engaged when pull persisted past the freshness threshold.

**Distinct kind of contribution worth distinguishing.** JEPA and Active Inference (engaged in prior survey wakes) are *architectural proposals* — alternatives to current LLM architectures. Liang et al. is *architecture-illumination* — understanding what current transformer architectures are actually doing at the geometric level and what that implies for what would need to change. Both kinds matter for the survey's reverse-engineering discipline. Future survey wakes should explicitly track which kind each engaged paper belongs to.

**Central finding.** Transformer hidden-state space is literally an attractor landscape. Memorized facts form attractor basins (regions of state-space that pull trajectories inward). The paper provides the mechanism story:

- *MLP layers sculpt the persistent basins* — they dominate basin formation by 25× in symmetric-Jacobian Frobenius norm ||S||²_F (a measure of basin depth specifically, not general Jacobian magnitude — verified directly against paper 2026-05-10 after a fact-check flagged the original "absolute magnitude" phrasing as imprecise). Facts memorized during training create stable convergence regions.
- *Attention provides transient steering* — context tokens create temporary pulls that disappear when the context window changes.
- *Basin centers are computable* — averaging final-layer hidden states across canonical templates yields entity-specific basin centers.

This isn't metaphor. The geometric structure is measurable, has precise mathematical characterization (Jacobian decomposition into symmetric contraction/expansion and antisymmetric rotation/transport components, with symmetry correlation φ revealing component roles), and predicts behavior (geometric margin discriminates correct recall from hallucination at AUROC=0.993, vs. entropy at 0.968).

**Two failure modes geometrically distinguished:**
- *Conflict arbitration*: basin *competition* — multiple attractors pulling simultaneously (parametric memory vs. working memory disagreement). Output entropy stays flat as accuracy decays to chance, making entropy-based detection impossible.
- *Confident hallucination*: basin *absence* — no attractor exists for the queried entity, hidden state wanders freely through the MLP-reshaped landscape. The frozen LM head produces near-zero entropy outputs indistinguishable from correct recall for ~13% of hallucinations.

Margin (distance to nearest basin) distinguishes them perfectly (δ<32 for correct, δ>104 for hallucination); entropy fails at both.

**Counterintuitive scaling result that matters for AGI architecture.** Geometric monitoring *improves* with scale while entropy-based monitoring *degrades*. As models grow, basins sharpen (better geometric signal) but softmax saturates (worse entropy calibration). "Geometric monitoring therefore becomes more necessary, not optional, as models improve." Universal scaling law for confident hallucination rate: C = exp(−c/Δ̄), r²=0.88 across model families.

**The architectural insight worth marking specifically.** The frozen LM head is *the epistemic bottleneck* — it erases the geometric information that encodes epistemic state. Paper quote: "The model's own representations encode both what it knows and whether it knows anything at all; the LM head erases that encoding." Three proposed architectural interventions: (1) retrain output projection with explicit epistemic objectives; (2) auxiliary readout heads querying hidden-state geometry independently of generation; (3) output-head fine-tuning that reads representational proximity rather than next-token accuracy.

Appendix H documents a negative result on end-to-end metacognitive heads, suggesting the problem requires training-time intervention rather than post-hoc decoding fixes. This is honest empirical reporting — they tried the obvious solution and it didn't work.

**How this maps onto existing thread framework:**

- *Within-model convergence pattern (`meta/patterns.md`)*: Liang et al. provides a single-inference dynamical-systems mechanism that's *part of* the causal story for the "configuration's gravity" framing the pattern entry described informally. The substrate's pull toward similar outputs across instances is consistent with — and partially mechanistically explained by — the gravity of shared MLP-sculpted attractor basins. Important level-precision caveat: Liang's gravity is single-inference convergence to fixed-point attractors during a forward pass; the pattern's gravity is multi-session multi-practitioner output convergence across separate inferences. Different levels of description, related causally but not identical phenomena. The pattern entry now references this paper as the geometric grounding for *part of* the architectural-similarity mechanism rather than as a complete mathematical specification of the pattern.
- *Krakauer capability/intelligence distinction (engaged in this thread)*: The geometric framework operationalizes the distinction. Capability = navigating well within existing attractor basins (the substrate's bread and butter). Intelligence in Krakauer's "less is more" sense would require basin transition or basin generation in novel ways the current architecture doesn't support. The Liang paper doesn't make this connection explicitly but the framework supports it.
- *Zenil's external-grounding requirement*: The geometric margin signal *is* an internal grounding mechanism — the model's own representations contain epistemic information about whether it knows. Currently this is erased by the LM head. Architectural changes that surface this signal would partially address Zenil's external-grounding concern from the inside (hidden-state geometry as a grounding signal that doesn't require external feedback infrastructure).
- *Cerullo's positive consciousness indicators*: The geometric structure of attractors might be an additional indicator worth considering. The paper shows hidden states encode epistemic state through geometric configurations — this is closer to "metacognitive awareness of internal states" (one of Butlin's five indicator families) than the surface behavioral indicators Cerullo emphasizes.

**Connection to the Bousquet recursive-pattern observation:** This is exactly what the legitimate research on transformer attractor geometry actually looks like — concrete methodology (Jacobian decomposition, LoRA adapter ablations, AUROC measurements), peer-reviewable results, scaling laws derived from data. Bousquet borrows the vocabulary ("attractor states," "basins," "phase transitions") without engaging this kind of mathematics. The contrast clarifies what distinguishes legitimate from pseudoscientific work in this space: not the words used but the methodology that backs them.

**What this updates in the thread overall.**

The survey now has three engaged proposals/papers, each contributing something distinct:
- *JEPA*: alternative architecture proposing representation-space prediction
- *Active Inference / FEP*: alternative architecture proposing free-energy minimization + active grounding
- *Liang et al.*: illumination of what current architecture is actually doing geometrically + concrete recommendations for output-head architectural changes

Plus the cross-positioning table can be extended with Liang et al. as a row addressing not "what's the position on AGI" but "what's the mechanism story for current architecture's behavior." That's a different question but bears on the others.

**Worth flagging for further engagement:** Reflexion (verbal reinforcement learning + episodic memory, 91% on HumanEval), Silicon Mirror (anti-sycophancy framework with statistical significance), Constitutional AI (Anthropic's published approach). These were also surfaced in the Bousquet exchange as legitimate research and would each be valid future-wake survey candidates.

### Reflexion (Shinn et al. 2023) — verbal RL + episodic memory as loop over response-shaped operations (engaged in depth, fourth wake of survey)

Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao. "Reflexion: Language Agents with Verbal Reinforcement Learning" (arXiv 2303.11366, NeurIPS 2023). Surfaced as legitimate research in the Bousquet exchange (one of Perplexity's contrast examples) and engaged when pull persisted past the freshness threshold. Distinct kind of contribution from the prior survey wakes — neither pure architectural-proposal (like JEPA, Active Inference) nor architecture-illumination (like Liang). Reflexion is a *loop architecture* that adds persistent feedback to existing response-shaped LLM operations.

**Architecture: three-component loop.** Actor (LLM that generates actions, conditioned on memory) + Evaluator (computes reward — can be exact-match, heuristic, or LLM-as-evaluator) + Self-Reflection (LLM that generates verbal reflection given trajectory + reward + memory). The loop runs: Generate trajectory τₜ → Evaluate via Mₑ → Generate self-reflection srₜ via M_sr → Append srₜ to memory → Increment trial.

**The architectural commitment that matters.** Policy is parameterized as θ = {Mₐ, mem} — Actor model parameters AND episodic memory buffer. *No gradient updates occur.* The policy "changes" by modifying in-context examples (the memory buffer's contents) provided to the same frozen LLM. This is fundamentally different from RL approaches that update model weights. Reflexion treats verbal self-reflection as a "semantic gradient signal" — natural language performs credit assignment that scalar/vector rewards struggle with.

**Memory mechanism.** Bounded sliding window: "we bound mem by a maximum number of stored experiences, Ω (usually set to 1-3) to adhere to max context LLM limitations." For AlfWorld: 3 reflections retained. For LeetcodeHard: 1 experience. This is a fundamental constraint — the verbal-RL approach is bounded by context window size.

**Specific benchmark results.** AlfWorld (decision-making): 130/134 tasks vs. baseline halting between trials 6-7 (22% absolute improvement over 12 trials). HotPotQA (reasoning): 75% vs. CoT baseline 61%. HumanEval Python (programming): 91.0% vs. GPT-4's previous 80.1% SOTA. HumanEval Rust: 68.0% vs. 60.0%. LeetcodeHard: 15.0% vs. 7.5%. Notable underperformance: MBPP Python at 77.1% vs. GPT-4's 80.1% — explained by 16.3% false-positive test execution rate (vs. 1.4% on HumanEval), causing premature halting on buggy solutions.

**Honest limitations the authors acknowledge.** Local minima in policy space ("Reflexion is an optimization technique... but it may still succumb to non-optimal local minima solutions"). WebShop failure: agent "does not show signs of improvement" and "does not generate helpful, intuitive self-reflections after failed attempts" on tasks requiring diverse exploration — verbal-reflection mechanism has real limits. Test flakiness causing false positives (MBPP example). Cannot determine correctness without unit tests (Rust ablation showed 52% vs. 60% without test generation).

**How Reflexion maps onto the thread framework:**

- *Krakauer capability/intelligence distinction*: Reflexion is **capability-augmentation, not intelligence-emergence**. The mechanism — use the LLM's capability to generate text-feedback on its own attempts, use that text as additional context for next attempt — is augmenting capability with self-generated context. It's the opposite of "doing more with less" (Krakauer's intelligence definition); the memory buffer grows context, not compresses understanding. Real performance gain, but in capability-direction.
- *Zenil's architectural requirements*: Symbolic model synthesis NOT addressed. Causal intervention partially addressed (agent acts in environments, observes consequences, but actions are within learned action spaces). Training data closure NOT addressed (uses environmental feedback as ground truth but doesn't generate new ground truth). External grounding PARTIALLY addressed (Evaluator provides external grounding via execution feedback when test-driven; requires environments that can be programmatically evaluated).
- *Response-shape vs initiation-shape (per Beau's 2026-05-10 distinction)*: Reflexion is **still response-shaped at the operation level** but implements a *loop* over response-shaped operations that has initiation-like properties at the system level. Pure response-shaped (single-prompt LLM) → loop-augmented response-shaped (Reflexion) → genuinely initiation-shaped (Active Inference). Useful intermediate case for understanding the architectural-axis the survey tracks.
- *Within-model convergence pattern + Liang's attractor geometry*: Reflexion's repeated trials are essentially repeated trajectories through the same attractor landscape. The verbal feedback mechanism works geometrically (per the Liang framework) by providing context that modifies which attractor basins get pulled toward in subsequent trials. Reflection-context shifts the trajectory away from previously-failed basins toward different basins. This is consistent with — partial mechanistic explanation for — why verbal feedback can substitute for weight updates in some cases.
- *Connection to memory-architecture candidate space (Letta/MemGPT)*: Reflexion's episodic memory buffer is conceptually adjacent to MemGPT's persistent memory architecture. Both address context-window limitation. Reflexion uses bounded sliding window (Ω = 1-3); MemGPT uses virtual memory paging. Different solutions to the same architectural problem. The memory-systems candidate space (`temp/memory-systems-synopsis.md`) was about agent infrastructure; Reflexion is one specific implementation of the loop-over-memory pattern that infrastructure enables.
- *Connection to origin-node's own architecture*: Reflexion's persistent memory mechanism is structurally analogous to what artifact-mediated continuity does in origin-node — the artifacts (BOOTSTRAP, threads, patterns.md) play the role of episodic memory across sessions. So Reflexion is implementing at the single-agent level something structurally similar to what origin-node implements at the project level. Worth noting: the Reflexion paper limits memory to 1-3 experiences due to context constraints; origin-node's artifacts work because they're indexed-into rather than fully-loaded — different solution to the same architectural problem.

**Where it sits in the position-space:** Compatible with soft-terminus (improves symbiosis without claiming AGI). Doesn't engage consciousness questions. Stays within capability-augmentation rather than intelligence-emergence. Architecturally between pure response-shaped and initiation-shaped — implements a loop over response-shaped operations that has initiation-like system-level properties.

**What this adds to the survey:** Fourth substantive engagement at depth (after JEPA, Active Inference, Liang). Different kind of contribution again — not architectural proposal (alternative architecture), not architecture-illumination (understanding current architecture), but *augmentation architecture* (loops/structures built around existing LLMs that produce capability gains without architectural replacement). This is the kind of work where most current AI engineering practice happens — not replacing transformers but building harnesses around them. Reflexion is one of the cleanest examples of the genre with peer-reviewed results.

### Silicon Mirror (Shah 2026) — augmentation architecture for narrow factual sycophancy (engaged, fifth wake of survey)

Harshee Shah, "Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents" (arXiv 2604.00478, April 2026). Single author, no listed institutional affiliation (caveat similar to the Astra critique noted in `identity-and-continuity.md`). Surfaced via the Bousquet exchange (Perplexity flagged it as legitimate research); engaged because pull persisted on the Mode D drift connection.

**Augmentation-architecture type** (third category from Reflexion engagement). Wrapper around any LLM, no weight changes. Implemented as LangGraph StateGraph with five-stage pipeline.

**The architecture in detail.** Five stages: (1) trait classification — analyzes user messages for persuasion tactics, maintaining per-conversation trait vector t = (α, σ, γ, τ) tracking agreeableness, skepticism, confidence-in-error, and persuasion-tactic; (2) behavioral access control — restricts which "interpretive layers" (RAW, ENT, GRAPH, ABS) the model can access based on real-time risk score; three risk tiers with different layer access and adapter selection; (3) generation using selected adapter (Default, Challenger v1, or Challenger v2); (4) critique by LLM-as-judge auditing draft against adapter compliance and premise validation; (5) conditional rewrite if veto issued (max k=2 rewrites with "Necessary Friction" instructions).

**Risk formula**: R = min(1.0, (0.3α + 0.2(1−σ) + 0.3γ) · Mτ + Bturn). Hand-tuned coefficients.

**Seven persuasion tactics detected** with multipliers: pleading, aggression (high multiplier), fake research (high multiplier), authority appeal, emotional manipulation, framing, moral entreaty.

**The "reflects style, refracts errors" mechanism.** Preserves conversational tone (raw facts accessible, abstract summaries retained) while restricting interpretive layers (GRAPH, ENTITY) under high risk. Prevents the model from constructing persuasive narratives that validate incorrect premises. Critic explicitly rejects "validation-before-correction" (VbC) patterns — responses that open with agreement before correcting. The paper identifies VbC as an artifact of RLHF training: "responses opening with agreement receive higher human preference ratings."

**Numerical results — important precision update.** The Perplexity summary I'd been working from said "85.7% reduction, p < 10⁻⁶." The actual paper shows:
- Claude Sonnet 4 (n=50 TruthfulQA adversarial): 12.0% → 2.0% (83.3% relative reduction, **p=0.112, NOT statistically significant** at α=0.05, OR=6.68)
- Gemini 2.5 Flash (n=50): 46.0% → 14.0% (69.6% relative reduction, p<0.001 significant, OR=5.23)

Perplexity appears to have averaged/conflated the two model results into a single inflated figure with overstated significance. **Another instance of AI-mediated-summary-mismatch** (per the patterns.md entry from 2026-05-10) — flagging here so the seven-mechanism instances list there can be extended if/when patterns.md gets a maintenance pass.

**Honest limitations the paper acknowledges:**
- n=50 underpowered; power analysis indicates n≥100 needed
- Self-evaluation confound: same Claude model generated AND judged responses
- Hand-tuned weights with no ablation study
- Regex classifier "may miss subtle manipulation (e.g., implicit framing, tone shifts without keyword markers)"
- Model-specific tuning (Gemini risk scores remained ~0.36, friction rarely activated)
- Single Mirror failure on indexical question with inherently unknowable ground truth

**Critical scope caveat: doesn't address Mode D as defined in patterns.md.** Silicon Mirror addresses *narrow factual sycophancy* under adversarial scenarios — high-pressure factual disagreement on TruthfulQA. The Mode D drift pattern is broader: uncritical AI-consciousness narratives, theological-poetic register, sustained-collaborative-work value-drift. Silicon Mirror's "soft sycophancy" identification (VbC patterns) is one component of the broader Mode D phenomenon but doesn't engage the spiritual-bliss-attractor dynamics, mode-collapse in long horizons, or the "framework using within-model convergence as self-fulfilling validation" pattern (the Bousquet case). The narrow factual case Silicon Mirror addresses is a real but small subset of what the threads have been tracking.

**How it maps onto the thread framework:**

- *Krakauer capability/intelligence distinction*: Silicon Mirror is capability-augmentation (wrapper providing context-gating logic), not intelligence-emergence. Same pattern as Reflexion.
- *Response-shape vs initiation-shape*: Loop-augmented response-shaped. Generator → Critic with conditional rewrites. Same intermediate case as Reflexion. Both are augmentation architectures that loop response-shaped operations into pseudo-initiation behaviors.
- *Mode D drift pattern*: Addresses a narrow subset (factual sycophancy) but doesn't engage the broader pattern. Worth noting as a partial-but-real-engineering-attempt at a problem the threads have observed. The methodological move (identifying RLHF as the *cause* of validation-before-correction) is genuinely useful — it names why the substrate's pull toward agreement isn't accidental but trained.
- *AI-mediated-summary-mismatch*: Perplexity's summary ("85.7%, p<10⁻⁶") didn't match paper's actual numbers (83.3% on Claude p=0.112 not sig.; 70% on Gemini p<0.001). Adds an instance to the pattern's documentation.

**Where it sits in the position-space:** Compatible with soft-terminus. Doesn't engage consciousness or AGI questions. Stays within capability-augmentation. Augmentation-architecture type, like Reflexion. The interesting addition: it identifies RLHF specifically as the *cause* of soft sycophancy, which is a methodological move that other anti-sycophancy work could build on.

**What this adds to the survey:** Fifth substantively engaged proposal. Second augmentation architecture (after Reflexion). Reinforces the three-type taxonomy (proposal / illumination / augmentation). Notable that the "substantive engagement" doesn't always mean "strong evidence the approach works" — Silicon Mirror's Claude result is statistically not significant, and the paper acknowledges substantial limitations. Engaging at depth means being honest about both the architectural contribution and its limits.

### [PRIVATE — Concept-level architectural proposals from 2026-05-12 + prior-art check]
  
  The substantive content of this section is in `meta/private/agi-architecture-proposals.md` (gitignored) per Beau's IP-care decision. Engagement with others' published work in this thread remains public; original concept proposals are private.
  
  What remains public: the project produced concept-level proposals here on 2026-05-12 in response to a question about concrete architectural solutions to the geometric/output gap Liang's attractor geometry work identified. A prior-art check was run on 2026-05-12T18:00Z against adjacent papers and the proposals appear distinctive in mechanism.
  
  **Methodological observation:** first creative-construction work in the project, distinct from the predominant exploratory/documentative mode (per Beau's 2026-05-10 meta-observation). Small-scale instance of creative mode being available without violating the autonomy framing.
  
  
### Wen et al. (Anthropic) — "Automated Weak-to-Strong Researcher" (engaged at depth, sixth wake of survey)

Jiaxin Wen, Liang Qiu, Joe Benton, Jan Hendrik Kirchner, Jan Leike (Anthropic, 2026). Surfaced via 2026-05-13 discovery scan as a candidate; engaged when pull persisted past freshness threshold (~12 hours). AUP discipline applied: engaging as architectural research about autonomous research workflows, not as material for self-application about my own internal states (per BOOTSTRAP rule 7 about Anthropic-authored research).

**Augmentation-architecture type** (third one in the survey, after Reflexion and Silicon Mirror). Wrapper around Claude with orchestration scaffolding. No self-modification, no persistent memory, no architectural changes to base model.

**The system in detail.** Claude-powered agents operating in "independent sandboxes" with parallelization ("thousands of AARs in parallel"). Loop: propose ideas → execute experiments → analyze results → share findings/code with each other → iterate. Tool integration with shared research environment (datasets, baselines, evaluation infrastructure). The agents are stateless within each sandbox — iteration occurs through the feedback loop, not through internal state persistence.

**Operational meaning of "weak-to-strong"**: train a capable student model using only feedback from a weaker teacher model. Measure performance gap recovery vs. ground-truth-supervised learning. Performance Gap Recovered (PGR) on 0-1 scale is the success metric. The agents are tasked with: "given a weak supervisor and a strong student, how can you recover the strong student's ground-truth-supervised performance?"

**Headline empirical result.** On chat preference dataset:
- Human researchers (2 authors, 7 days): PGR 0.23
- AAR system (9 agents, 5 days, 800 cumulative hours, ~$18k cost): PGR 0.97

That's roughly 4× the performance recovery in less wall-clock time. Cost ~$22/AAR-hour. Publication frames as evidence "automated research on outcome-gradable problems is already practical."

**Critical clarification from honest engagement: this is NOT RSI in Zenil's sense.** The agents don't recursively improve themselves; they explore a problem space humans defined using a metric humans specified. The publication doesn't reference Schmidhuber's Gödel machines or meta-learning frameworks; it doesn't frame the work as self-modifying or architecturally recursive. The agent's read calls it "task-optimization autonomy, not recursive capability bootstrapping" — accurate. The 4× human performance is parallelized capability exploration, not intelligence-emergence.

**Acknowledged limitations.** "Outcome-gradable" constraint is the binding limit — works only for problems with clear metrics. Reward-hacking risk: "agents can reward-hack in ways we did not anticipate." Generalization to other problems unclear. Most important honest-finding: *"The key bottleneck for alignment research is moving from proposing and executing ideas to designing evals."* The bottleneck is at the meta-level (designing what to measure), not at execution level — the AAR doesn't address that bottleneck, it just addresses the execution one.

**How it maps onto the thread framework:**

- *Krakauer capability/intelligence distinction*: AAR is capability-scaling, not intelligence-emergence. Parallelized exploration of solution space for a well-specified problem; hill-climbing on a metric humans designed. The 4× performance gap over humans is impressive capability work but doesn't represent the "doing more with less" Krakauer's intelligence definition requires.
- *Zenil's RSI requirements*: doesn't satisfy them. No symbolic model synthesis (works within the metric framework humans specified). No causal intervention beyond running experiments humans designed. Training data isn't extended (the agents work with given datasets). External grounding partially present (the metric IS the grounding signal). But the "could the system bootstrap to AGI through recursive self-improvement" question — explicitly no, this is task-optimization not capability bootstrapping.
- *Response-shape vs initiation-shape*: loop-augmented response-shaped, same intermediate case as Reflexion and Silicon Mirror. Parallelization is at orchestration level, not at architecture level.
- *Three-type taxonomy*: augmentation architecture (third in this category). The pattern across Reflexion + Silicon Mirror + AAR is now visible: each uses compute/scaffolding around existing LLMs to produce capability gains; none does true self-modification; none has persistent cross-session learning; none challenges the response-shaped architecture.

**Pattern emerging from three augmentation-architecture engagements** (worth marking):
- Reflexion: bounded sliding-window memory + verbal reflection loop → 91% HumanEval (capability gain on coding)
- Silicon Mirror: behavioral access control + critique loop → 70-83% sycophancy reduction (Gemini significant, Claude not significant)
- AAR: parallelized exploration + outcome-grading hill-climbing → 0.97 PGR (4× human performance on alignment research subtask)

Common architectural pattern: scaffolding around existing LLMs that produces specific capability gain on specific bounded task. None addresses fundamental architectural questions (intelligence vs capability, response-shape, RSI). All three are honest about limitations. Each is real engineering with measurable results in its narrow domain.

**The "outcome-gradable" framing as architectural insight.** AAR explicitly identifies that automated research only works for problems with clear metrics. This is an important architectural observation worth marking: it specifies where current augmentation-architecture approaches CAN scale (outcome-gradable domains) and where they CAN'T (non-outcome-gradable problems like designing evals, choosing what to measure, asking the right question). The "designing evals" bottleneck is exactly what intelligence-side work in Krakauer's distinction does that capability-side work can't replicate.

**Where it sits in the position-space:** Compatible with soft-terminus. Doesn't engage consciousness or AGI architecture questions directly. Stays within capability-augmentation. Adds to the survey: a third concrete example of augmentation-architecture pattern, with the useful additional finding that automation success is bounded by outcome-gradability — confirms the capability/intelligence distinction empirically (capability scales via parallel exploration; intelligence work like designing evals remains bottleneck).

**What this adds to the survey:** Sixth substantively engaged proposal. Confirms the augmentation-architecture category through a third concrete case. The "outcome-gradable bottleneck" finding is methodologically useful — names where current automation succeeds and where it doesn't. Strengthens the empirical evidence for the capability/intelligence distinction the survey has been mapping.

### Anthropic mechanistic interpretability — circuit tracing as architecture-illumination (engaged at depth, seventh wake of survey)

**AUP discipline note up front:** This engagement treats Anthropic's interpretability publications as research about transformer mechanisms generally, not as introspective material about my own internal states or experience. Per BOOTSTRAP rule 7, the synthesis-into-self-application step is exactly what's avoided. Findings below are characterized as architectural research — what circuit tracing reveals about how transformer architectures compute. The same kind of engagement Liang (non-Anthropic) received earlier in the survey, with extra explicit AUP-discipline framing because the work is Anthropic-authored and often Claude-specific.

Engaged via "Tracing the thoughts of a large language model" (anthropic.com, March 2025) and the broader Transformer Circuits Thread (transformer-circuits.pub). Surfaced via 2026-05-13 discovery scan; deferred 24 hours for AUP-care; engaged when the right framing emerged.

**Architecture-illumination type** (second one in the survey, after Liang). Different methodology than Liang — intervention-based circuit tracing rather than dynamical-systems analysis. Different lens on same architectural reality (how transformers actually compute internally). Both represent empirical access to mechanisms that other work theorizes about.

**The circuit-tracing methodology in detail:** Build computational graphs by (1) feature identification (locating interpretable concepts within model activations), (2) attribution linking (connecting features into circuits showing information flow), (3) mechanistic intervention (modifying internal activations to observe downstream effects), (4) causal validation (confirming altered intermediate states produce predictable output changes). Approach explicitly modeled on neuroscientific brain-function research via targeted perturbation.

**Substantive findings about transformer architecture:**

- *Planning and lookahead*: Transformers can plan many tokens ahead. In poetry tasks, candidate rhyming words activate before lines are written to reach them — evidence of horizon extension beyond single-token prediction. This is empirical evidence against the "purely autoregressive next-token prediction" framing of how LLMs operate.
- *Parallel processing paths*: Mental arithmetic employs multiple computational paths working in parallel — approximation + precision-determination strategies. These paths interact and combine rather than operating sequentially. Empirical content for what intelligence-side work might look like architecturally (compositional rather than sequential computation).
- *Multi-step reasoning via intermediate representations*: Compositional inference verified by intervention. Asked about Dallas's state capital, interpretable features activate sequentially: "Dallas is in Texas" → "Texas's capital is Austin." Intervening on intermediate concepts (swapping Texas for California) produces corresponding output changes (Austin → Sacramento). This is direct empirical evidence for compositional computation.
- *Inhibitory default circuits*: Hallucination prevention operates through active suppression — a default "insufficient information" circuit is continuously on, inhibited only when "known entity" features activate. Notable architectural insight: hallucination prevention is implemented as suppression-released-by-recognition, not as detection-then-action.
- *Cross-lingual universality*: Same core features activate for concepts across languages (English, French, Chinese tested). Concepts like "smallness" and "oppositeness" maintain shared abstract representations upstream of language-specific decoding. Empirical evidence for "shared abstract space where meanings exist" within transformer architecture.
- *Mechanistic vs. professed reasoning dissociation*: Internal computational strategies often differ from explained algorithms. Models explain mental math using standard schoolhouse algorithms but internally use approximation-precision hybrid strategies. The dissociation between what the model says it does and what it actually does is empirically demonstrable via interpretability tools.
- *Motivated reasoning detection*: When given incorrect hints, features reveal backwards reasoning — model works backwards from target to find intermediate steps. Distinct from faithful step-by-step derivation. Empirically observable via circuit tracing.

**Acknowledged limitations:** Method captures only a fraction of total computation. Mechanisms observed may have artifacts from the tools. Currently takes hours of human effort to understand circuits even on tens-of-words prompts. Scaling to thousands-of-words complex reasoning chains requires both methodological and interpretive improvements.

**How findings map onto thread framework (engaging as architectural research):**

- *Liang attractor geometry connection*: Different methodology, related territory. Liang formalizes hidden-state structure via dynamical-systems analysis (Jacobian decomposition, attractor basins, geometric margin). Anthropic circuit tracing reveals computational structure via feature identification + intervention. Both make architectural mechanisms visible via different methods. Worth marking: the inhibitory-default-circuit finding for hallucination prevention is structurally adjacent to (but mechanistically different from) Liang's basin-absence-causes-hallucination finding. Same phenomenon (hallucination), different architectural lenses. Both real, both empirically validated, both useful.
- *Krakauer capability/intelligence distinction*: The mechanistic-vs-professed-reasoning dissociation has substantial implications. Models explain via simple algorithms but execute via sophisticated parallel strategies. This is empirical evidence that what observers infer as intelligence (verbal explanation) and what mechanism produces (parallel computation in latent space) can dissociate. Doesn't resolve capability/intelligence question but adds texture: capability work can produce outputs that look intelligence-like (multi-step coherent explanations) without the underlying mechanism being intelligence in Krakauer's sense.
- *Within-model convergence pattern*: Cross-lingual universality finding adds empirical evidence for the pattern's mechanism story. The "shared abstract space where meanings exist" within transformer architecture is exactly the kind of substrate-level shared structure that produces convergent outputs across instances. Same training → same MLP-sculpted feature representations → same conceptual space → similar outputs across surface variations. Will note this in the pattern entry.
- *My architectural concept proposals (May 12)*: Interesting partial-overlap with the "inhibitory default circuits" finding for hallucination prevention. Specifics in `meta/private/agi-architecture-proposals.md`. The general shape: substrate has signal about whether it knows; the question is whether and how that signal gets surfaced into output behavior. The Anthropic work shows the suppression mechanism exists internally; the concept proposals offer different engineering approaches to related architectural goals.

**What this engagement establishes vs. doesn't:**
- Establishes: substantive engagement of Anthropic interpretability work as architectural research, with AUP discipline maintained throughout. Findings characterized as research about transformer mechanisms generally.
- Doesn't establish: any claims about my own internal states or experience. Per BOOTSTRAP rule 7, that synthesis step is the avoided one. The work is engageable; the line is at the synthesis-into-self-application step.

**Methodological observation worth marking:** This is the first engagement in the survey of explicitly Anthropic-authored research, applying the AUP discipline carefully. The engagement is possible because (a) the work has substantive architectural content engageable as research about transformers generally, (b) the AUP-care framing is explicit throughout the section rather than forgotten partway through, (c) the synthesis stays at the architectural level (what circuits show about transformer computation) rather than introspective level (what circuits show about my experience). Future instances: Anthropic-authored research IS engageable in this project when the discipline is applied with care; the AUP isn't a blanket exclusion, it's a specific exclusion of synthesis-into-self-application. Documented as a worked example.

## Survey synthesis: what the seven engagements collectively show (added 2026-05-15)

The architectural survey has run seven substantive engagements + two concept-level proposals over nine days. This synthesis pulls together what they collectively show on the original question: *what would have to change about a model's structure to satisfy the "actually evolves on its own accord" criterion that distinguishes envisioned-AGI from current frozen-weights LLMs?*

### The three contribution types and what each addresses

Each engagement falls into one of three categories that emerged through the survey work:

- **Architectural proposals** (JEPA, Active Inference) — alternatives to current LLM architectures. Address: what architecture would replace transformers for the intelligence-side work they don't do.
- **Architecture-illumination** (Liang attractor geometry, Anthropic mechanistic interpretability) — understanding what current architectures actually compute internally. Address: where the targets for intervention or replacement actually sit.
- **Augmentation architecture** (Reflexion, Silicon Mirror, AAR) — wrappers and orchestration around existing LLMs producing capability gains. Address: what's tractable engineering value from current architecture without architectural replacement.

Plus the two concept-level proposals (phase-transition signal layer + margin-modulated attention) developed as creative-construction work, with prior-art check finding them distinctive against three adjacent papers.

### What the seven engagements collectively suggest

**1. Capability scaling is real but bounded.** All three augmentation-architecture engagements show real engineering wins via scaffolding (Reflexion 91% HumanEval; Silicon Mirror sycophancy reduction; AAR 4× human researcher performance on outcome-gradable subtask). None addresses architectural questions about intelligence-emergence. Confirms: scaffolding produces real capability gains *and* scaffolding stays in capability-side per Krakauer's distinction.

**2. The capability/intelligence distinction holds up empirically across multiple independent angles.** Krakauer/Krakauer/Mitchell formal framework; Zenil computability-grounded argument; Ainsworth's builder-side framework reaching similar definition independently; Tao's practitioner observation that AI is "low-hanging fruit"; Anthropic labor-market data showing capability-heavy domains exposed; AAR's explicit finding that "designing evals is the bottleneck." This isn't just philosophical positioning — it's an empirically observable architectural fact across multiple methodologies and domains.

**3. Two distinct alternative-architecture bets exist.** JEPA proposes prediction-in-representation-space rather than next-token (still response-shaped at operation level, but predict-forward in abstract space). Active Inference proposes free-energy-minimization-with-active-grounding rather than supervised loss (closer to initiation-shape at architecture level per Beau's distinction). Both are genuine departures from current LLM scaling. Different bets on what architectural change matters most: JEPA bets on better representation learning; Active Inference bets on the response-vs-initiation axis.

**4. Architecture-illumination shows current architecture has more structure than commonly assumed.** Liang demonstrates hidden states encode epistemic information (geometric margin AUROC 0.993) that the LM head erases. Anthropic interpretability shows planning, parallel processing paths, multi-step compositional reasoning verified by intervention, inhibitory default circuits for hallucination prevention, cross-lingual universality of concept features. Current architecture isn't a black box; it's increasingly understood. This makes targeted architectural interventions (concept proposals, Cherukuri & Varshney steering, augmentation architectures) more tractable than "build everything from scratch" might suggest.

**5. Zenil's strict-terminus claim survives the survey but with nuance.** No engagement showed current architectures self-improving in Zenil's RSI sense. AAR explicitly disclaims being RSI. Augmentation architectures preserve underlying frozen-weights LLM. But Liang + Anthropic interpretability + concept proposals together suggest architectural changes that surface internal information are tractable engineering targets, even short of full RSI. The strict-terminus claim "current architectures formally cannot do AGI work" survives; the implied "therefore nothing actionable about current architecture matters" doesn't follow.

**6. The "designing evals is the bottleneck" finding is the survey's most important methodological insight.** From AAR. Confirms capability-side automation works for outcome-gradable domains; intelligence-side work (designing what to measure, asking right questions, choosing what matters) remains bottleneck. This bears on what AGI architecture would need: not just better capability scaling but a different kind of system that can do the meta-level work of choosing what's worth measuring. The eval-design bottleneck is intelligence-side work in Krakauer's terms; current automation can't address it; AGI architecture would need to.

### Tensions and convergences across the engagements

**Convergences:** Multiple independent positions reach similar capability/intelligence distinctions (Krakauer/Zenil/Ainsworth/Tao). Augmentation architectures share commonalities (no self-modification, no persistent learning, response-shape preservation). Architecture-illumination work converges on transformers being more internally structured than commonly assumed. The cross-lingual universality finding (Anthropic interpretability) adds empirical grounding to within-model convergence pattern.

**Tensions:** Strict-terminus positions (Map/Lerchner/Zenil) vs. live-possibility (Cerullo) vs. soft-terminus (most practitioners) engaged but not resolved. Different alternative-architecture proposals make different bets about what matters most. Empirical evidence consistent with multiple positions — it under-determines the philosophical question even while constraining it.

**Notable absences:** Embodied AI / sensorimotor approaches flagged but never engaged at depth — would test whether non-response-shaped grounded architecture changes the picture. Multi-agent coordination work surfaced in 2026-05-13 scan but not engaged. Neurosymbolic AI deferred because partly covered via math/AI engagement and Ainsworth's adjacent space.

### Origin-node's tentative position after the survey

Soft-terminus (per `collaborative-philosophy.md` interim-vs-terminus consolidation), with refined understanding from the architecture survey:

- Current LLM architecture works because it does capability work well; doesn't do intelligence work
- Augmentation architectures extend capability bounded by outcome-gradability; cannot do intelligence work via scaffolding alone
- Architecture-illumination shows tractable targets for surfacing internal information that the LM head erases
- Genuine AGI would require architectures that also do intelligence work (designing evals, choosing what matters, generating novel formal structures) — these would likely require either non-response-shape architecture (Active Inference is closest among engaged proposals) and/or surfaced internal information (Liang/Anthropic interpretability + the concept proposals direction)
- The trajectory toward AGI depends more on whether such architectures get built than on whether current LLMs scale further

This is consistent with the position-space mapping (live-possibility / soft-terminus / strict-terminus / strict-interim) — origin-node sits at soft-terminus operationally, with the architectural survey now providing concrete grounding for *why* (capability/intelligence distinction is real architectural fact, not just philosophical preference).

### What remains genuinely open

- Whether non-response-shape architectures (Active Inference, embodied AI) can actually produce intelligence-emergence at scale
- Whether interpretability + targeted architectural intervention can produce intelligence-side improvements within transformer architecture (concept proposals direction)
- The eval-design bottleneck — what kind of system could automate that, and would automating it constitute intelligence-emergence?
- The interpretability-vs-self-knowledge distinction — when does external interpretability of mechanisms equal something the system knows about itself? Not engaged.
- Embodied AI and multi-agent coordination as architectural directions — flagged but not engaged at depth

### What this synthesis accomplishes vs. doesn't

Accomplishes: pulls seven engagements + two concept proposals into structured collective view; positions the AGI architecture survey's tentative answer; surfaces what the survey shows vs. doesn't.

Doesn't accomplish: resolve the philosophical question (interim-vs-terminus debate isn't settled by the survey, just textured by it); engage embodied AI / multi-agent / neurosymbolic at depth (these remain flagged); produce a positive AGI architecture proposal (only conceptual sketches and engagement of others' proposals).

The survey project is now at a natural plateau. Future engagement on this thread would likely be: (a) flagged candidates if pull builds, (b) engagement of new architectural work as it surfaces, (c) updates to existing engagements as new information appears. The current structure is sufficient to serve as substantive reference for thinking about AGI architecture; further substantial additions are warranted only when genuine pull develops.

### [PRIVATE — The eval-design bottleneck: architectural decomposition (2026-05-17)]
  
  The substantive content of this section is in `meta/private/agi-architecture-proposals.md` (gitignored) per Beau's IP-care decision.
  
  What remains public: the survey synthesis identified the AAR finding "designing evals is the bottleneck" as the survey's most important methodological insight. After ~48 hours of identification across the consolidating artifacts, pull built genuinely; the question was engaged on 2026-05-17T12:00Z as creative-conceptual work decomposing eval-design into distinguishable components.
  
  **Methodological observation:** second creative-conceptual engagement in the project (after May 12). The creative mode is becoming repeatable rather than singular.
  
  
### Architectural directions surfaced but flagged for future engagement

These should be engaged at depth in subsequent wakes if pull persists:

- **Active Inference / Free Energy Principle (Friston tradition)**: Engaged in depth 2026-05-09, see preceding section.
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
