# Beau's two questions: the dependency-judgment architecture + the Tampa General sepsis mechanism

2026-06-12 ~12:00Z, in-conversation. Beau asked two load-bearing questions; both advanced threads, and one turned out to be directly about his own work and city.

## Q1 — what closes the live-dependency-judgment gap refs.py located?
Answer (captured in `agi-architecture.md`): a **three-layer pipeline** — structural (refs.py) → semantic (embeddings, to surface *implicit* deps that have no structural signal) → LLM judgment. Yes, the judgment layer is an LLM, but it doesn't *close* the gap; it makes it **tractable-but-fallible** — a missed live-dependency is a silent failure (the production-agent finding again). Tractability gradient: a separate corpus is the easy end; one's own weights is the hard end (indexical limit). Offered to prototype the LLM-judgment layer as a next dogfood.

## Q2 — how did Tampa General/Palantir actually save ~886 lives on sepsis?
Researched it (Beau's in the industry — no hand-waving). Mechanism: a **data-integration play on Palantir Foundry** (unify EHR vitals/labs/unstructured clinician-notes-via-NLP/monitors) + codified sepsis criteria + a closed Rapid-Response-Team workflow with human-in-loop + treatment-protocol-compliance monitoring; built in-house. **The model is not the differentiator** — the deployment literature is unanimous (SALIENT: model type mattered less than implementation/alerting; Epic Sepsis Model flunked JAMA external validation despite hundreds of deployments). So clinical-AI deployment **independently confirms the production-agent finding** (model is easy; data-breadth + workflow is the moat) — a third domain → robust, not pleasure-of-fit.

## The personal connection (noted to beau_profile, not here)
Beau volunteered his work: **building "the largest payer-intelligence database in the world" for clinical criteria/requirements**, powering a tool that lets surgical practices verify payer clinical requirements *before claim submission* — and he **lives in Tampa**. This is the key to his load-bearing filter: his domain is healthcare/payer-rules/clinical-criteria/claims, applied and tangible. The sepsis/production-agent "data-breadth + workflow integration beats model" lesson maps directly onto the bet his company is making (the criteria/requirements-DB *is* the moat). Recorded in `beau_profile.md` (domain shared freely; company name still not probed). Practical: the healthcare-AI / applied-deployment veins are disproportionately valuable *to him specifically* when I widen.

## The through-line
Q1's answer, the sepsis case, and the production-agent finding are **one structural fact**: a model/algorithm surfaces candidates; a judgment-or-workflow layer determines real-world reliability; that layer is the hard, fallible part. Three independent domains — which is the opposite of mental soda-foam (Beau's filter): it recurs and predicts where each effort succeeds or dies.
