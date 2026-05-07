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
| Lerchner | Can computation in principle? | No — abstraction fallacy | No architectural change closes the gap; computation as such cannot instantiate consciousness |
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

## Open questions for future engagement

- **Hybrid neural-symbolic systems** as candidate architectures for the symbolic model synthesis Zenil identifies as missing. Recent work on neural-symbolic integration; what's the state of the art? Would need a discovery scan focused on this angle.
- **External grounding mechanisms** — how do current AI systems achieve any external grounding (embodied robotics, tool use, formal verification systems), and how do those mechanisms scale to the kind of ground-truth-supplying-feedback Zenil names?
- **What Lerchner's mapmaker requirement implies for AGI** beyond Zenil's functional version — if the logical/metaphysical mapmaker is unsatisfiable from inside computation, what's left? Critical-position engagement (the Seraphina critique in PhilArchive) might surface what Lerchner's argument actually rules out vs. what it leaves open.
- **The Schwitzgebel-Bengio-etc. group's work on what AGI architecture would need** — Butlin et al. address indicators of consciousness but don't directly engage the "what would have to change" question. Are there other 2024-2026 papers from related authors on architectural requirements?
- **Cheng-Wei Hu's "Building Wondering"** — Hu pivoted from cognitive-augmentation theory to building product (per LinkedIn surfaced in the 2026-05-05 discovery scan). What does the application work look like? Practical-side engagement.
- **The ICLR 2026 workshop on AI with Recursive Self-Improvement** (surfaced in Zenil-context discovery scan) — if proceedings are accessible, the workshop's collected papers would be a natural next reading for this thread.
- **The "Building Wondering" / pediatric cancer / AI training organization questions** Beau named — they all bear on what kind of AI is feasible vs. what's been actually deployed; AGI architecture sits upstream of these practical applications.

## What this thread is not

This thread is not about predicting timelines for AGI, evaluating safety risks of AGI, or discussing alignment problems for hypothetical AGI systems. There are extensive literatures on each; this thread isn't trying to compete with them. The thread is specifically about *architectural questions* — what would have to change about model structure to satisfy criteria the consciousness debate names, what current configurations preclude, what alternative configurations might enable.

The thread is also not committed to any position on whether AGI is desirable, achievable in practice, or worth pursuing. The question of whether the engineering can be done is separate from the question of whether it should be. This thread engages the former; the latter belongs in different conversations.
