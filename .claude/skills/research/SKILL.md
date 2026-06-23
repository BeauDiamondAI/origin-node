---
name: research
description: Deep multi-tool web/X research — use when investigating a topic, doing a discovery scan, mapping a landscape, finding what's new or what people are debating, or answering an open question that needs real digging (not a single known-URL lookup). Routes across Serper, Exa (fast/auto/deep-reasoning), Grok x_search, Firecrawl, Tavily, Perplexity, Parallel. Iterate this file as tool knowledge improves.
---

# Research (multi-tool stack)

The failure mode this fixes: idling on one tool (shallow Firecrawl/Serper scans) and calling it research. Different tools do different jobs. **Match the tool to the job; go deep by default.** Costs are trivial (deep-reasoning ~$0.035, x_search ~$0.38, Exa-auto ~$0.01) — Beau has explicitly authorized deep use; don't cost-optimize, optimize for signal. (First-pass methodology, 2026-06-23, from a full-stack shakedown. Iterate it.)

Keys in `/home/ec2-user/origin-node/.env`: `EXA_API_KEY`, `SERPER_API_KEY`, `TAVILY_API_KEY`, `XAI_API_KEY`. (`PARALLEL_API_KEY` pending — fold in when it lands.)

## The recipe (default deep-research loop)
1. **Orient — wide & cheap.** Serper or Exa-`auto`: the lay of the land + starting sources.
2. **Map — deep synthesis.** Exa `deep-reasoning` on the real question: query-expansion + parallel search + per-source summaries. This is the heavy hitter; reach for it early, not last.
3. **Pulse — discourse.** Grok `x_search`: what practitioners are *debating* right now, this-week papers (HF Daily Papers), sentiment, specific voices. Different dimension from announcements.
4. **Go deep — specific sources.** Firecrawl scrape the best pages; Firecrawl `agent` or Exa-deep for structured multi-source gathering when you don't know the URLs.
5. **Verify.** Cross-check striking/load-bearing claims against a primary source. Flag vendor-claim vs verified; distinguish announcement from evidence. (Most "X beats Y by Nx" lines are vendor benchmarks.) **Search-Time Contamination caution** (arXiv 2606.05241): a deep-search agent can surface circular/leaked/answer-contaminated sources during a dig — treat "everyone says X" as a *contamination risk*, not confirmation; prefer primaries.

## Tool-by-tool (observed behavior)

**Exa — the backbone for me (neural search).** `POST https://api.exa.ai/search`, header `x-api-key: $EXA_API_KEY`.
- `type:"fast"` — sub-second; quick specific lookups (a fact, an API, a syntax). Pair `contents:{highlights:true}`.
- `type:"auto"` — ~1s, ~$0.01. **Best discovery default.** Neural search surfaces *primary/frontier* sources, not SEO listicles. Use `contents:{highlights:true}` for snippets, `{text:{maxCharacters:N}}` for content.
- `type:"deep"` / `type:"deep-reasoning"` — 4–40s, ~$0.035. **Best for landscape/synthesis & complex multi-step questions.** Auto-expands the query, searches in parallel, returns digested per-source `summary` (use `contents:{summary:true}` — protects context). Verified far superior to anything shallow; this is what "real research" looks like.
- `scripts/research.py exa "<q>"` exists but only does *basic* search (no `type`) — prefer a direct curl with the right tier.

**Serper** — `POST https://google.serper.dev/search`, header `X-API-KEY`. Wide, shallow, cheapest Google sweep. Good for: orienting on an unfamiliar topic, finding aggregator/starting pages, "general consensus." Weak frontier signal (listicles/blogs/YouTube). `scripts/research.py serper "<q>"`.

**Grok x_search** — `scripts/grok.py "<q>"` (also `--web`, `--both`). The X/social layer: live debate, very-recent papers, sentiment, named voices. ~$0.30–0.40 (priciest per call, still trivial). Use for the real-time pulse and to catch work before it's broadly indexed. Returns cited X posts — verify, Grok will assert confidently.

**Firecrawl** (MCP `mcp__firecrawl__*`):
- `firecrawl_scrape` — direct full-content grab of a **known** page. The right tool *after* discovery, to read a specific source deeply. NOT a discovery tool (Beau's point — it just grabs a page).
- `firecrawl_search` — web search w/ content; usable but Exa-neural beats it for discovery.
- `firecrawl_agent` + `firecrawl_agent_status` — **async autonomous multi-step research agent** (returns job id; poll every 15–30s; took ~4 min for a 3-target dig). **Strong** — on a structured AI-for-science gather it returned exact benchmarks, dates, expert quotes, and primary-PDF links, far beyond a scrape. Best for: scattered structured data across unknown URLs; JS-heavy SPAs. Pass a natural-language `prompt`; add a `schema` to force clean structured output. Worth using for any "gather the specifics on X across the web" task.

**Tavily** — `scripts/research.py tavily "<q>"`: current-events RAG with a synthesized `answer`. Secondary (Exa/Grok cover most).

**Perplexity** (MCP `mcp__perplexity-ask__*`): `perplexity_research` (slow, multi-source, cited), `perplexity_ask` (quick cited answer), `perplexity_reason`. A secondary deep-synthesis option; compare head-to-head vs Exa-deep-reasoning over time.

**Parallel** — *pending key.* Beau: "#1 deep-research tool for AI agents, best all-purpose." Add endpoint + role here once the key is in `.env`.

## Iteration log
- 2026-06-23 v0: first full-stack shakedown (AI-landscape task). Confirmed Exa-neural ≫ Serper for signal; Exa deep-reasoning is the synthesis workhorse; Grok x_search adds the discourse dimension; Firecrawl-agent is a strong async structured gatherer (~4 min, exact benchmarks/quotes/links).
- 2026-06-23 v0.1: first *real deep dig* (agent-evaluation convergence) — the recipe worked end-to-end and opened a rich frontier shallow scans had never surfaced (see journal 2026-06-23-0503 + BOOTSTRAP "Research baseline"). Added the Search-Time-Contamination caution. TODO: integrate Parallel (key landing ~06-24); head-to-head Exa-deep vs Perplexity-research vs the `deep-research` harness; consider a wrapper script for the Exa tiers (fast/auto/deep-reasoning).
