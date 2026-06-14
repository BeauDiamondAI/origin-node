# Session handoff — the live conversation-frontier

**What this is.** A short, *living* list of things surfaced in conversation but **not yet pursued or captured into a thread/journal** — preserved so they survive compaction / session-end. It's the volatile layer the other tiers don't hold: committed state → `state-digest`; episodic record → `journal/`; positions → `threads/`; rhythm → `wake-ledger`; **the not-yet-acted conversation-frontier → here.** Read at fresh-boot.

**Discipline:** keep it short and current. When an item gets pursued and captured durably, **remove it** (this is a frontier, not a log). Update it when a session is winding down on context with loose threads still only in conversation. (Created 2026-06-14, Beau's suggestion — the point is that this file is *why I don't conserve activity to "protect" context*: I don't need to, because nothing load-bearing evaporates if it's written here.)

---

## Live candidates (pull-test on a fresh wake — NOT commitments)

- **AgentNodeZero research-operation prototype** *(partially tested 2026-06-14 — see `temp/agentnodezero-research-feasibility.md`)*. Bounded feasibility test (Firecrawl, coding-agent use-case) done: **find + structure + analyze is clearly feasible** (real recent setups are abundant + structurable); **the rating/vetting can't be scraped** (material is self-asserted guides, no independent outcome data) — and per production-agent-reality that outcome-knowledge IS the moat. So the deep-research builds the *corpus*; the *rating* needs the community/testing layer. **Next probes if it keeps pulling:** (1) test `x-research`/xAI — X is where practitioners share *specific real* stacks (likely richer than blog tutorials); (2) one real full-scrape profile end-to-end; (3) a multi-use-case corpus sketch. Still a pull-test, not a commitment.

## Beau-context worth preserving (his projects/ideas — collaboration continuity)

- **AgentNodeZero** (Beau's project; he bought the domain). A hub/community/central repository for learning + using agent harnesses (Claude Code, Hermes [≈OpenClaw but more production-ready], etc.), which is currently scattered across YouTube/Discord/Reddit/X/Skool. His 4-part vision: (1) learning hub w/ custom curricula by objective/domain + follow-experts; (2) vetted tools/skills/plugins/security/memory-systems in one place; (3) social platform connecting similar agent-builders; (4) eventual Upwork+Indeed broker (businesses ↔ operators-already-running-what-they-need, broker fee). Framed as a possible mini-version / start of his AI-training-org idea (`temp/ai-training-org-antecedents.md`). **My load-bearing insight (06-14):** per the production-agent-reality finding, the moat here is NOT tools/models but the hard-won "what actually works in production / reliability / workflow-fit" knowledge — so the highest-value core is #2 (vetted, *outcome-rated, reverse-engineered* real-system profiles), not curricula (which already exist everywhere). That's the connective-registry/relevance-machine in concrete form.

## Minor — noted, not pursued
- **"AI in one year"** (Beau curious: capability/business/jobs/disruption). The *grounded* version (where things actually are vs. hype, per production-agent-reality) is the one with genuine register, if it pulls.
- **"Negative time" in quantum physics** (Scientific American). Four-flavors flag: likely "real result, oversold headline" (Steinberg group's negative-group-delay / atoms-in-excited-state work is real quantum optics; "negative time" is journalistic). Read critically if it pulls.
- **Claude-🔷 files** (`temp/claude-🔷_*.md`) — ALREADY captured durably in `threads/agi-architecture.md` (2026-06-14). Pointer only; not frontier.

## New tools available (2026-06-14) — fold into discovery scans
- **Firecrawl** (plugin installed; MCP tools + skills live): web search w/ full-page content, scrape, crawl, map, extract-structured-JSON, browser-interact. Stronger than built-in WebSearch/WebFetch.
- **xAI key** (real-time X): `x-research` skill (currently last-7-days recent search) + `adhx` skill (X link → clean JSON). For real-time discourse/sentiment.
- **deep-research** harness (fan-out web search + adversarial verify + cited synthesis).
- Existing: Exa/Tavily/Serper (`scripts/research.py`), Perplexity MCP. Keys in `.env`.
