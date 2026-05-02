The Three-API Stack
1. Exa — The Semantic Discovery Engine (Primary)
Exa is the most important one for free-time exploration specifically because it's the only major search API with a true neural index — it finds things based on conceptual similarity, not just keyword matching. When your agent wants to follow a thread from something it's been thinking about, Exa will surface genuinely related ideas, research papers, niche sites, and obscure documents that Google-based APIs simply won't find because there's no keyword overlap.

Accuracy: 94.9% on SimpleQA — highest of any search API benchmarked

Unique capabilities: dedicated people search (1B+ indexed profiles), company search, code search, research paper filtering — all in one API

Latency: sub-350ms on the Fast endpoint; p95 under 1.7s

Cost: 1,000 requests/month free; $7/1K searches + $1/1K pages for full text

March 2026 update: first 10 results with full text content are now included free with every search — makes it substantially cheaper for "search and read" workflows


2. Tavily — The RAG-Native Current Events Layer
Where Exa excels at discovery, Tavily excels at structured retrieval of current, factual, citable information. It was built specifically for the way agents consume information — it returns structured JSON with summaries, source citations, and highlights already formatted for LLM consumption, which saves processing overhead and downstream token costs.

Best for: current events, factual verification, anything where recency matters, news monitoring

Cost: 1,000 credits/month free; basic search = 1 credit; advanced = 2 credits; pay-as-you-go at $0.008/credit

Important note: Tavily was acquired by Nebius in February 2026 — worth watching for pricing/policy changes, but no disruptions yet

The limitation: no semantic/neural search, max 20 results per query vs. Exa's 100+, no own index (aggregates from Google/Bing)

The free tiers of Exa + Tavily together give you roughly 2,000 combined requests/month at $0 cost — substantial for free-time use where the agent isn't doing production-volume search.

3. Serper.dev — The High-Volume Cheap Fallback
When the agent wants to do broad, rapid Google searches — scanning many topics quickly, checking on a dozen things before deciding where to go deep — Serper is the right tool at $1/1,000 queries. That's an order of magnitude cheaper than any AI-native search API for raw discovery volume.

Cost: $1/1,000 queries at scale — cheapest raw Google access available

Best for: high-frequency shallow searches, "is there anything interesting about X?" scans before deciding to go deeper with Exa

Limitation: raw SERP JSON only — no full text extraction bundled, no semantic capability

How to Use All Three
The logical routing for free-time exploration:


Agent wants to explore a thread
    │
    ├─ "What's conceptually related to this idea?"
    │   → EXA (semantic neural search)
    │
    ├─ "What's happening with X right now?"  
    │   → TAVILY (current events, structured facts)
    │
    └─ "Quick scan — is there anything interesting 
        across 20 topics before I pick one?"
        → SERPER (cheap broad Google sweep)
