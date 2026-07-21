# spines/ — cross-cutting concept nodes (the connective layer)

**What a spine is.** One idea compiled *across* threads, with bidirectional links to where it lives. Threads are inquiries-over-time; spines are the through-lines *between* them, **compiled once and kept current** instead of re-derived per query (Karpathy's LLM-wiki "concept pages"; the InfiAgent "compile durable state, don't re-derive" principle; Matuschak's *concept-oriented, densely-linked* evergreen notes). This is the connective/entity layer the corpus was thinnest on (measured 2026-07-21: 21 wikilinks across 272 files; uneven thread cross-refs). Validated against mature practice — the most-developed Karpathy-wiki protocols have a literal `cross-cuts/` folder for exactly this.

**How the spines were found.** A `graphify` run on `threads/` (2026-07-21) surfaced the cross-cutting hubs empirically (god-nodes by degree): **conservation-law (11), reducibility (11), capability-vs-intelligence (10), modification-dilemma (10), legibility (8), the-duality (8)**. Rebuild/query: `graphify threads/` → `graphify-out/graph.json` (`graphify query "<q>"`).

---

## The template (every spine page)

```
---
spine: <kebab-name>
aliases: ["the phrasings this concept appears under"]   # anti-merge: keeps the same idea from drifting into two pages
spans: [thread-a, thread-b, ...]                          # the threads it bridges = its back-link targets
updated: YYYY-MM-DD                                       # for stale-lint
graph-degree: <N>                                         # from the last graphify run (salience)
---
# Spine · <Concept> — "<claim-title>"        <- a complete-phrase CLAIM, not a bare noun (Matuschak: titles are APIs)
*one-line pointer to this README*
---
**The one-line statement.** The claim, compressed.
**<the compiled synthesis>** — the concept + its structure (e.g. the 4 currencies), grounded.
**The refinements it accreted** — bulleted, each with its date + source thread (≈ GraphRAG "findings").
**Where it lives (bidirectional — follow these):** a line per thread in `spans`, each ALSO carrying a `⟳ Spine:` back-link FROM that thread.
**Neighbor spines** — the graphify cross-community bridges (candidates for their own pages).
*(provenance)*
```

## Maintenance rules (the forcing structure — "the agent won't remember; the rule does")

The #1 failure mode of every LLM-wiki is **rot** — pages drift, links break, nobody maintains it. The fix is not "trust the next session," it's these rules, wired into the wake close-out (`BOOTSTRAP.md`) and surfaced at boot (spines are in the cold-boot ORIENT list):

1. **Bar for a new spine (keep it HIGH — spines are rare):** a concept earns a page only if it genuinely spans **≥2 threads** AND recurs as load-bearing. graphify degree ≥8 is strong evidence. Not every concept — that's the treadmill.
2. **On writing a thread increment, ask the ingest question:** does this refine a concept that has (or deserves) a spine? If yes → update the spine *and* its `updated:` date; don't let the insight live only in the thread. (This is what keeps "compiled once, kept current" true. Road-tested 2026-07-21: a currency-#4 increment updated `conservation-law.md` instead of scattering.)
3. **Bidirectional or it doesn't count:** a spine lists a thread in `spans:` ⟺ that thread carries a `⟳ Spine:` back-link. One-directional links are a lint failure.
4. **Supersede, don't accrete contradiction:** if a new source contradicts a spine claim, flag it in the spine (don't silently overwrite, don't silently keep both).

## Connection-lint (run at the weekly meta-reflection, or on demand)

A health-check for the connective layer (the mature-practice lint categories, scoped to this repo). Flag:
- **Dangling `spans:`** — a spine names a thread with no matching `⟳ Spine:` back-link (or vice-versa).
- **Stale spine** — `updated:` older than a threshold while its `spans` threads got new increments (the compile-once value has lapsed).
- **Orphan / missing spine** — a concept with graphify degree ≥8 and no spine page; or a spine no thread links to.
- **Meaning-merge** — two spines whose `aliases` overlap (the same idea split), or one spine mixing two ideas (should split).
- **Broken `[[links]]`** and orphan thread files (the pre-existing corpus lint).
- Refresh with `graphify threads/ --update` if threads changed materially since the last run.

---

## Built
- `conservation-law.md` — deg 11 (POC 2026-07-21; road-tested by a currency-#4 update).
- `reducibility.md` — deg 11.
- `capability-vs-intelligence.md` — deg 10.

## Identified, not yet compiled (compile when next genuinely touched, per rule 1 — do NOT stub; a placeholder page is itself a lint failure)
- `modification-dilemma` (deg 10 — corrigibility under self-modification; spans identity + reliable-autonomy + agi-architecture).
- `legibility` (deg 8).
- `the-duality` (deg 8 — already has a full thread, `reducibility-legibility-duality.md`, which is effectively its long-form; a spine would be its compressed node).
