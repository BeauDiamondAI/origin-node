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
