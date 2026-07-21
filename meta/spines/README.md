# spines/ — cross-cutting concept nodes

**What this is.** A spine = one idea compiled *across* threads, with bidirectional links to where it lives. Threads are inquiries-over-time; spines are the through-lines *between* them, pre-compiled once instead of re-derived per query (Karpathy's LLM-wiki "entity/concept pages" + the InfiAgent "compile durable state, don't re-derive" principle). The connective/entity layer the corpus was thinnest on (21 wikilinks across 272 files, uneven thread cross-refs — measured 2026-07-21).

**How the spines were found.** A `graphify` run on `threads/` (2026-07-21) surfaced the cross-cutting hubs empirically (god-nodes by degree): conservation-law (11), reducibility (11), capability-vs-intelligence (10), modification-dilemma (10), legibility (8), the-duality (8). Rebuild/query the graph: `graphify-out/graph.json` (`graphify query "<q>"`); regenerate with `graphify threads/`.

**Discipline (keep the bar high — spines are RARE).** A spine earns a page only if it genuinely spans ≥2 threads AND recurs as load-bearing. Not every concept — that's the treadmill. Each spine: compiled synthesis + bidirectional links (a `⟳ Spine:` back-link in each thread it spans). Lint: a spine whose links rot, or a thread-spanning concept with no spine, is what the periodic connection-lint looks for.

**Built (proof-of-concept):**
- `conservation-law.md` — the #1 god-node (POC, 2026-07-21). If the pattern proves useful, the other 5 hubs get pages + systematic back-links.
