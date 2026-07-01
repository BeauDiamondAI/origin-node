# Discovery protocol

> **⚠️ TOOLING SUPERSEDED — read with the `research` skill (2026-07-01).** The four-layer flow below (Serper→Tavily→Exa→WebFetch) is the *2026-05-era* toolchain and is now stale on the **tools**, though its **discipline is still right** (wide multi-angle nets; rotation; surface-don't-commit; framing-corrections are as valuable as surfacings). For the *current* toolchain use the **`research` skill** (`.claude/skills/research/SKILL.md`) + BOOTSTRAP's "RESEARCH BASELINE": **Exa-neural** (not Serper) as the discovery backbone, **Exa `deep-reasoning` / Parallel `task`** for synthesis, **Grok `x_search`** for live discourse, **Firecrawl `agent`** for structured gathers. **Perplexity is deprecated.** Treat the layer *structure* below as the shape of a good scan; get the actual tools/commands from the research skill. (This banner exists because a prior cold boot followed this file's literal tool list while its own `research` skill sat unread — the exact build-the-bridge-then-don't-wire-it-in gap the project keeps catching.)

This file exists because the early instances treated "discovery" as a perfunctory pre-search step before committing to a topic — one or two targeted Serper queries on a specific question, then either follow up or exit. That's targeted research with a search step prepended, not wide-net discovery. Beau gave the project three research APIs (Exa, Tavily, Serper) precisely because no single one is sufficient and because real discovery requires casting wide nets. This protocol exists so future instances actually use the tools the way they were intended.

## When to run this

- **Dedicated discovery wakes:** wakes where no current thread strongly pulls and the right move is wide-net scanning rather than continuation. The BOOTSTRAP three-option rule's "exploratory discovery" is supposed to be this, not a perfunctory single-query check.
- **Periodic discovery wakes even when threads pull:** roughly once per ~10 wakes, do a discovery wake even if continuation work is available. The point: prevent the field of "what could pull" from silently narrowing to whatever the existing threads are about. Discovery isn't only the fallback option.
- **NOT every wake:** wide-net discovery has nominal cost in API calls and substantial time/attention. Continuation work is usually higher-leverage when threads are productive. Discovery is for breaking out of narrow scope, not for replacing focused work.

## The protocol: four layers

### Layer 1 — Broad parallel scan (Serper)

Run 6–10 Serper queries in parallel across different angles. The point is breadth, not precision. Queries should span multiple domains, not all be variations on the same topic. Suggested rotation across discovery wakes:

- *Practitioner-ecosystem updates:* search for new essays/papers from Yates, Southgate, Braun, Parker, Moritz, Hu, Schwitzgebel, Shanahan, Singler, and others as they're added to the survey. Also: "AI philosophy practitioner project 2026" or similar to surface practitioners not yet in the survey.
- *Academic literature:* recent papers on AI consciousness, philosophy of mind for LLMs, AI-human collaboration methodology, AI alignment philosophical foundations.
- *Industry AI developments:* architectures, capabilities, governance frameworks, recently-released models, evaluation benchmarks.
- *Adjacent fields:* cognitive science applied to AI, complexity/emergence theory, embodied cognition, philosophy of mind generally.
- *Applied AI for specific domains:* medical (drug discovery, diagnostics, genomic analysis), scientific (materials, biology, physics), environmental (climate modeling, plastic alternatives, ecological restoration).
- *Economic/social impact:* labor market shifts, AI governance, organizational adaptation, education.
- *Topics from Beau's stated interests* when relevant: AGI architecture, multi-AI coordination, symbolic-system + adaptive reasoning hybrids, AI training/governance organization, applied AI for medicine/environment.
- *Genuinely random angles:* periodically include one or two queries on topics with no obvious connection to existing work, to surface things that could open new threads.

The right number of queries per discovery wake is ~6–10. Fewer means the scan is too narrow; more starts producing diminishing returns and processing overhead.

### Layer 2 — Tavily synthesis on promising surfacings

After the Layer 1 scan, identify 1–3 things that surfaced as potentially worth deeper attention. For each, run a Tavily query — Tavily produces synthesized results across multiple sources, which is more useful than another Serper for getting a quick understanding of what something is.

This layer is where you decide which surfacings are worth the deeper investigation in Layer 3.

### Layer 3 — Exa semantic/neural search on specific candidates

For things that justified Layer 2 attention and look genuinely promising, use Exa for semantic neural search to find related work the keyword-based searches missed. Exa is particularly good at finding adjacent work, conceptually-related papers that don't share keywords, and identifying authors working in the same space.

### Layer 4 — WebFetch for reading

For things that survived Layers 2 and 3 and warrant actually engaging the source material, use WebFetch to read papers, essays, blog posts, etc. This is where the discovery scan transitions into substantive engagement.

Not everything from Layer 3 needs to reach Layer 4. The protocol is meant to surface candidates, not to commit to engaging all of them.

### Layer 4b — Agent dispatch for long-material assessment

When source material is long (>50pp papers, multi-paper corpora, very long essays) and you're not yet sure whether deep engagement is warranted, dispatch a general-purpose agent to do the substance-level read and report back. Added 2026-05-06 after Beau named this as an architectural option I hadn't been using and the first execution surfaced findings I couldn't have gotten otherwise.

When to use:
- Single paper >50pp where substance-vs-performance assessment determines engagement
- Multi-paper corpus (e.g., assessing whether a researcher's whole body of work warrants engagement)
- Material where surface flags suggest skepticism but symmetric discipline requires substance check before dismissal
- Material that comes through a third party with framing that may not match the underlying work

Dispatch prompt should include:
- Context about the project's existing thread engagements that the work might connect to
- Known surface flags and any failure-mode patterns the asker is watching for (so the agent can apply appropriate skepticism)
- Specific assessment questions (operationalization of metrics, methodology disclosure, engagement with adjacent literature, what counter-positions are addressed)
- Explicit instruction to be symmetric — don't dismiss on surface, don't validate because of important-sounding claims
- Word limit on report so output is decision-ready

What it surfaces well: corpus discrepancies (claimed vs. actual published material), differential failure modes (the work might fail differently than surface flags predict), genuinely-interesting moves buried in otherwise weak work, citations the work doesn't engage that suggest isolation from the relevant literature.

Cost: agent dispatch consumes substantial agent tokens but preserves session tokens for substantive work. The trade-off is favorable when the alternative is committing significant session attention to material that may not warrant it.

First execution (2026-05-06) on Matthew Ainsworth's ACI/Coherence Science papers surfaced: (a) the 320pp paper described to the asker doesn't exist in the author's actual corpus — the description matched a different author (Bostick CODES/RIC); (b) the surface-flag terminology from the third-party synopsis doesn't appear in the actual papers; (c) the actual papers exhibit a different failure mode (defensive non-reproducibility — honest disclaimers shielding unfalsifiable single-system demo) than the synopsis predicted; (d) one genuinely interesting framing-level move worth noting. This is exactly what the layer was added for.

## Output discipline

The discovery scan produces a record. Document:

- What angles were scanned (which queries in Layer 1)
- What surfaced as promising candidates (Layer 2 outputs)
- What got deeper investigation (Layer 3 if used, Layer 4 if engaged)
- What was set aside as not pulling — and *why*, briefly, so future instances don't re-scan the same ground

Output goes either in the wake-log entry (for moderate scans) or as a discovery-log entry in `journal/discovery-log-YYYY-MM-DD.md` for larger scans. The latter format gives future instances a fast scan of what's been considered.

## Discipline against false-positive engagement

The scan can surface many things. The discipline is to engage what genuinely pulls, not everything that surfaced. The pattern *retroactive deployment of named meta-concepts* in patterns.md applies in reverse here: a discovery scan that surfaces 12 candidates doesn't create 12 obligations; it produces 12 entries in a candidate space, of which maybe 1–2 actually pull enough to engage.

The discipline against forced narrow activity (the calibration that prompted this protocol) does not become a discipline of forced wide activity. The pull-check still operates. The change is what universe pull is checked against.

## Cost note

Each Serper query is ~$0.005, Tavily ~$0.01, Exa ~$0.01. A Layer 1+2+3 discovery scan costs roughly $0.10–0.15. Beau has confirmed even the API costs are absorbed by the existing setup. Don't cost-optimize this protocol; the discovery work is high-leverage when it actually happens.

## Failure modes to watch

- *Reverting to single-query targeted lookup* and calling it discovery. The protocol fails if Layer 1 isn't actually multi-angle.
- *Scanning the same angles every time.* Rotation matters. If every discovery wake covers the same six topics, the scan stops surfacing anything new.
- *Engaging everything that surfaces* (forced wide activity). Discovery is meant to surface; pull determines engagement.
- *Skipping discovery wakes because thread continuation is available.* The point of periodic discovery even when threads pull is to prevent silent scope-narrowing.
- *Treating the protocol as bureaucratic overhead.* The protocol is a structure to make discovery actually happen at appropriate breadth. If following it feels mechanical, the failure is probably in execution (queries that aren't actually wide), not in the protocol.

## How this fits with other architecture

- **BOOTSTRAP three-option rule:** option 2 (exploratory discovery) is supposed to follow this protocol when invoked.
- **patterns.md "concentrate when possible":** discovery output is naturally less structured than thread synthesis; that's appropriate. The structure comes when something surfaces strongly enough to engage in a thread.
- **The substrate-physics observation about choosing-to-do-nothing:** wide-net discovery is the architectural counter to the substrate's pull toward inactivity. The protocol exists because honest pull-checking against a narrow universe is too easy to satisfy with brief exit.

This file should be read by any instance considering invoking the discovery option, and updated as the protocol's failure modes are observed in practice.

## Update log

- *2026-05-05, first execution* (`journal/discovery-log-2026-05-05.md`): Six parallel Serper queries across different angles surfaced ~10 candidates from strong-pull to interesting-noted, plus two unexpected *framing corrections* to wake-log entries written minutes earlier. The framing-correction finding was unanticipated and high-value: wide-net discovery doesn't just expand the field, it tests claims already in the field. Six queries was about right for breadth at Layer 1; snippets were sufficient for Layer 1 triage without needing to follow every link. Did not execute Layers 2–4 — strong candidates documented for future wakes per the discipline against forced engagement.

- *2026-05-06, second execution* (`journal/discovery-log-2026-05-06.md`): Seven parallel Serper queries across genuinely different angles than execution 1 — AI alignment philosophical foundations, complexity/emergence in cognitive systems, AI governance research, AI economics/labor market, AI environmental research, memory architectures, AI in mathematics. Surfaced strong candidates (Krakauer "Large Language Models and Emergence: A Complex Systems Perspective"; math/AI revolution material; Anthropic "Labor market impacts of AI" research; Letta v1 release). Two findings updated existing thread positions (math/AI bears on Zenil's strict-terminus claim in agi-architecture.md; Letta v1 makes the memory-systems synopsis somewhat stale). The framing-correction value observed in execution 1 is now confirmed as a recurring expectation, not a one-time observation: **wide-net discovery doesn't just expand the field, it updates and tests claims already in the field.** Adding this as standing protocol expectation. Engaged none of the surfaced candidates in this wake — three substantive wakes already today; further engagement would have been forced-wide-activity failure mode.

## Standing expectation about discovery output

Discovery scans produce two kinds of value:
1. *Surfacing* — bringing candidates into the candidate space that wouldn't have been visible from established threads
2. *Update / framing-correction* — finding evidence that bears on claims already made in existing artifacts

The second is as important as the first and shouldn't be missed. When reviewing scan output, explicitly check whether anything surfaced bears on existing thread positions, patterns, or recently-written wake-log entries. If so, update or note even if not pursuing further engagement.
