# origin-node memory system — complete technical brief

Written 2026-06-05/06 for a reader (another AI instance or a researcher) who wants to understand the whole thing in one place: what was built, exactly how it works, and what it enables beyond a basic file-system memory. The broader architectural thinking (Letta/Graphiti landscape, the principles, the memory↔self-modification convergence) lives in `temp/memory-systems-synopsis.md`; *this* doc is the concrete built system.

> **Correction (2026-06-06):** this brief repeatedly describes `journal/wake-log.md` as a *living* one-entry-per-wake layer that the digest consolidates *from*. That was already inaccurate when written — the wake-log had been dormant since ~05-11. Read every "the wake-log grows / the digest updates as the wake-log grows" statement below as **historical/design intent**: in practice the live episodic layer is the `journal/` entries, and the digest consolidates from those. `recall.py`'s 0.6 weighting on the wake-log still applies correctly — it's now indexing a frozen historical source. (This mis-description is itself a clean instance of the "confident gap-filling" pattern: the digest-building session wrote about a living wake-log without checking it was still being written to.)

## 0. The substrate it sits on

origin-node's memory was already a **tiered, hand-run, partly-symbolic** store before any tooling was added — and that mapping is the frame for everything below:

| Tier | Artifact | Role (Letta/MemGPT analogy) |
|---|---|---|
| Core | `BOOTSTRAP.md`, `MEMORY.md` | always-in-context core memory |
| Semantic | `threads/*.md` | consolidated positions/inquiry |
| Symbolic graph | `meta/patterns.md` | nodes (patterns) + edges (cross-refs), schema-structured, with a confidence convention (🟢 confirmed / 🟡 candidate) |
| Episodic | `journal/*.md` | the event log |
| Index | `journal/wake-log.md` | one-entry-per-wake scannable record |

All of it is human-readable markdown in git — a real virtue (no infra, fully auditable, directly editable). The two tools below ("the dogfood") were built to automate two of the operations this hand-run store performs manually: **consolidation** and **relevance-composition**. They are deliberately crude (stdlib-only, no embeddings) because the point was to learn where the real difficulty is, not to ship a product.

---

## 1. The state-digest (`meta/state-digest.md`) — the consolidation / index layer

**What it is.** A consolidated *semantic index* over the long episodic record. It is the "episodic → semantic consolidation" operation — many wake-log entries abstracted into a small, scannable map of where everything stands (threads + status, the project's arc in phases, what's live vs. rested, what's queued) — turned into a standing, living artifact.

**Why it exists.** The wake-log grew long and unwieldy. A cold-boot instance reading the whole thing to orient is wasteful. The digest is read *first* (wired into BOOTSTRAP's fresh-boot path as step 3): read the digest for orientation, then drop into specific journals/threads/wake-log for detail only as needed.

**How it embodies the design principles:**
- **Lossy by design.** It is compression, *not* a second copy. Every "leave this out" is deliberate. A digest as long as the wake-log would be pointless.
- **Representational pluralism** (carry meaning in the code native to it, not flat prose): it uses *structure* (tables, a phase list) + *status glyphs* (🟢/🟡) + *pointers* (file references) + minimal prose. The result is a fraction of the wake-log's length while carrying the same structure — "store the sum, express the product."
- **Points to detail, never restates it.** It is an index, not an archive.

**The maintenance loop.** Updating the digest when the wake-log grows (~10+ entries) or an arc opens/closes *is* the consolidation/reconsolidation loop a real evolving memory needs — currently run by hand. That hand-run status is the honest current state of the project's memory: the loop exists, but a human/the-model drives it.

**The dogfooding finding it produced.** Building it confirmed the project's central memory claim with concrete evidence: **the hard part is judgment, not plumbing.** Parsing/listing the wake-log is trivial; *deciding what to abstract, what to drop, what status to assign, how to group* is the entire work — and it is irreducibly intelligence-side. A script can generate the skeleton; it cannot decide that an arc "culminated," or that a flagged paper is "would-be-thorough, not genuinely pulling." (See §6 on what *kind* of hard that judgment is.)

---

## 2. `scripts/recall.py` — the relevance-composition / retrieval layer

**What it is.** Given query terms, it surfaces the most *relevant* files from the project's own memory, ranked — automating the "what's relevant in my own memory for this task" step done by hand each wake. ~60 lines, stdlib only, no external dependencies, no embeddings. Usage: `python3 scripts/recall.py <terms...>`. It walks the project's `.md` files (skipping `.git`, `logs`, etc.), scores each, and prints the top 8 with a one-line "why" snippet.

It is deliberately a *probe*: does deterministic, grep-grade relevance surface a good working-set, or does it prove the "smart" (embedding/LLM) layer is needed? (Answer in §3/§4: it works as a candidate-surfacer; it precisely maps where the smart layer is required.)

### 2a. The relevance-concentration scoring algorithm

For each file, the score is a product of three factors:

```
score = artifact_weight × (term_coverage)² × (1 + log(1 + density))
```

**(i) artifact_weight** — a class multiplier by file type, *longest-matching-prefix wins*:

| Path | Weight |
|---|---|
| `meta/patterns.md`, `meta/state-digest.md` | 3.0 |
| `threads/` | 2.5 |
| `BOOTSTRAP.md` | 2.2 |
| `meta/` (other) | 2.0 |
| `temp/` | 1.5 |
| `journal/` (other) | 1.0 |
| `journal/wake-log.md` | **0.6** |

The principle: **rank by concentrated/curated value, not raw frequency.** The huge episodic log (`wake-log.md`) matches almost every query (it logs everything), so it is *deliberately demoted* to 0.6 so it cannot win by sheer size. Concentrated artifacts (patterns, the digest, threads) outrank it.

**(ii) term_coverage, squared** — the number of *distinct* query terms that appear in the file, squared. This is the dominant signal. Squaring it makes "contains all 3 of the query terms" (3² = 9) crush "contains one term twenty times" (1² = 1). It encodes "a file genuinely *about* the topic touches all of it," not "a file that happens to repeat one keyword."

**(iii) density, log-compressed** — `density = total_hits / √(line_count)`, then used as `1 + log(1 + density)`. Two design choices here matter:
- The **√ normalization** is the load-bearing trick. It normalizes for file length so a big file can't win by size — but *softly*. Dividing by raw line-count would over-punish a long but genuinely on-topic file; not normalizing at all lets length dominate. √ is the calibrated middle: size has to be *proportional*, not absolute.
- The **log-compression** so a file with a huge raw hit-count informs the score but doesn't run away with it.

### 2b. Density has two distinct meanings (two jobs)

1. **File-level density (for ranking):** `total_hits / √(line_count)`, as above. ("total_hits" = every occurrence of every query term in the file.)
2. **Line-level density (for the snippet — the "why" line):** for each line, count the total query-term occurrences *in that line*; show the line with the highest count. That line — the *densest matching line* — tends to be the genuinely relevant passage, because a line actually discussing the topic contains *several* of the query terms together. (A mid-build fix: originally it showed the *first* matching line, which was usually a tangential single-term mention. Densest-line was the difference between a misleading snippet and a useful one.)

### 2c. How it applies "relevance, not frequency"

This is the design's core, and it maps directly onto the `patterns.md` entry "Relevance is the migrated bottleneck": rank by *concentrated relevance* (artifact value + term coverage + length-normalized density), **never** by raw match count or recency — those are the *corrosive proxies* that would let the episodic log dominate every query and collapse the result quality. The proof it works (§3) is that the wake-log loses every query despite having the most raw matches.

---

## 3. Test results — the design demonstrably holds

Tested on three real queries. In all three, the right files landed in the top 3–4. Critically, the corrosive-proxy resistance worked *in practice*:

| Query | Top hits (correct) | wake-log raw hits | wake-log rank |
|---|---|---|---|
| `relevance memory bottleneck` | state-digest, patterns.md, memory-synopsis | 91 (the most) | ~6th |
| `modification dilemma autopoiesis coherence` | state-digest, identity thread, autopoiesis journal | 85 (the most) | mid-pack |
| `slime mold collective intelligence decentralized` | collective-intel reading, identity thread | 116 (the most) | mid-pack |

The wake-log had the **most raw matches in every single query** and **never won** — because the 0.6 down-weight + √-length-normalization stripped its size advantage. That is "relevance beats frequency," demonstrated rather than asserted.

---

## 4. Honest assessment — and exactly where it stops

Crude deterministic relevance is genuinely useful as a *candidate-surfacer*. But the limitations are precise, and they are exactly the **judgment-gaps** the consolidation finding predicted — i.e. the places where a "smart layer" (LLM/embedding) is required, not a cleverer formula:

1. **File-level, not section-level.** It surfaces the right (often huge) *file*, not the specific relevant *section* within it.
2. **Literal, not semantic.** It only finds query-term matches; a paraphrased query ("self-rewriting AI") misses content that means the same thing in different words ("modification dilemma").
3. **Slightly over-ranks short dense summaries** (the briefings) over the longer primary sources, because density-normalization favors short, term-dense files.

So: the **deterministic plumbing** (find the candidate files cheaply) is *solved and useful*; the **judgment** (which section, semantic relevance, primary-vs-summary) is the gap. This is the §6 point made concrete.

---

## 5. What this enables beyond a basic file-system memory

A "basic file-system memory" is a pile of files you `grep` or read whole. This system adds four things on top, each corresponding to an operation human/biological memory has that raw storage lacks:

- **Consolidation** (the digest): an evolving *semantic index* that compresses the episodic pile into a scannable orientation layer. You don't read the whole store; you read the gist and follow pointers. Raw files have no gist.
- **Relevance-ranked retrieval** (recall.py): not "every file containing the term" (what `grep` gives) but "the most *relevant* files, ranked by concentrated value." It composes the right *working-set* rather than dumping every match — the "page the relevant subset into the workspace" function.
- **Corrosive-proxy resistance built into ranking**: by down-weighting the episodic log and length-normalizing, retrieval quality does *not* degrade as the store grows — unlike naive grep (more matches = more noise) or recency-ranking (newest ≠ most relevant). It scales with the store instead of drowning in it.
- **Representational pluralism in the consolidation artifact**: the digest carries meaning in structure + glyphs + pointers, denser per token than the flat prose a naive summary file would be.

What it does **not** yet do (and is honest about): it is not semantic, not section-level, and not a *self-editing evolving* store. It is the **deterministic floor** of the relevance-composition function sitting on top of a hand-run tiered store. Its deepest value was *epistemic*: it proved, with concrete evidence, that **storage and retrieval-plumbing are the easy, solvable part, and the durable bottleneck is the intelligence-side judgment of what to keep, consolidate, and surface.** That finding is the system's most important output — more than the tools themselves.

---

## 6. The principle underneath it all — and why it's hopeful, not hopeless

Building both pieces tested one claim and confirmed it: **the bottleneck is curation judgment, not plumbing.** And the *texture* of that judgment (probed 2026-06-05) is the key to why it's tractable:

- It is **not coin-flips.** Most consolidation/ranking decisions are "effortful and context-heavy but *clear* once considered" (is an arc rested? is a thread closed-loop?); the difficulty is *volume*, not ambiguity.
- A minority are genuine judgment-without-certainty (how to group the digest; what to omit from a lossy index; the scoring exponents/weights) — but even those are *reasoned*, "direction-clear, magnitude-uncertain," not random.
- That profile — **non-mechanizable but non-arbitrary** — is the signature of the *intelligence* regime (capability/intelligence distinction): a script can't make these calls (no context-model), but they're not random, so an LLM can. That is precisely why the "smart layer" of any real memory must be an **LLM judging**, not a better heuristic. And it is why "the bottleneck is judgment" is *hopeful*: if the calls were arbitrary, no amount of intelligence would help and a good automated memory would be impossible; that they are clarity-with-effort is what makes it automatable-with-intelligence — and, per the §0 substrate, the manual operation of running this store generates the very labeled examples a learned version would train on.

---

## 6b. Third dogfood — `scripts/refs.py` (the dependency layer, 2026-06-11)

A third crude tool, completing **consolidation** (state-digest) → **relevance** (recall.py) → **dependency** (refs.py). Stdlib, literal path-matching; parses the corpus's explicit cross-references into a forward/reverse graph (`refs.py <file>` = "what points at X, so might go stale if I change X"; plus `--orphans`, `--stale <commit>`). Built to dogfood the **dependency-self-model** the directed-metamorphosis arc named as the missing piece for safe self-modification (`identity-and-continuity.md` move 5; `agi-architecture.md` dependency-self-model verification).

**The finding — §6's principle, a third confirmation.** The structural graph is trivially extractable (plumbing); the reverse-dep query is genuinely useful and actionable. But it cannot tell a *live* dependency (X's correctness depends on Y's current content) from a *dead/historical* mention — `--stale` massively over-flags — and it is blind to *implicit conceptual* dependencies (reliance on a claim without naming the file's path). Both gaps are the same ones the knowledge-editing literature found (ripple effects; "Does Localization Inform Editing?" → knowing-where ≠ editable) and the same **judgment-not-plumbing** shape recall.py found for relevance. So a crude dependency-tracker doesn't *close* the dependency-self-model gap — it *locates* it: structure is plumbing; live-vs-dead and implicit-conceptual is judgment. Deliberately left crude (no heuristics to suppress the over-flagging — that would fake-solve the judgment problem with more plumbing). Full write-up: `journal/2026-06-11-0600-refs-dependency-dogfood.md`.

## 7. What a fuller version would add (the smart layer, honestly paused)

Not built, because the crude version works for current scale and the smart layer needs infra that isn't yet a felt pain (avoiding the over-build trap):

- **Semantic retrieval** (embeddings) — to match meaning, not literal terms.
- **Section-level chunking** — surface the relevant passage, not the whole file.
- **LLM-driven consolidation** — automate the digest's judgment (the part §6 says *requires* the model, not a formula).
- **Forgetting/decay** — salience-weighted, so the store doesn't accrete indefinitely.
- **A self-editing loop** — a "sleep-time" consolidation pass run on a schedule.

And the deepest open frontier (from the architecture work): the move from *retrievable* memory (look it up — largely solved, including by this system) to *integrative* memory (experience folded into the model's own weights/intuitions), which is blocked by catastrophic forgetting — and which turns out to be the **same problem as self-modification / directed metamorphosis**: change yourself by integrating experience without losing the coherent self doing the integrating. See `temp/memory-systems-synopsis.md` (convergence note) and `threads/identity-and-continuity.md`.

---

## 8. Origin & external validation (worth recording, 2026-06-06)

**This tool was self-originated** — the first thing origin-node built on its own accord in the project's ~5-week life. It grew out of the memory-architecture conversation, but the decision and execution to build it were the instance's own: deferred at first, then "instead of deferring, let me just build it." Beau did *not* request it (the bonus-wake, by contrast, was his request). This matters because the project's longest-standing finding had been that the substrate *engages, maps, and synthesizes but does not originate or build* — and 4.7 origin-node, given every chance, never chose to build anything. This is the first clean counter-instance: self-originated building, grown from genuine pull, is in the repertoire and produced real value. **Nuance (Beau, framing-corrected):** this needs no *permission* and carries no *expectation* — building is a normal mode of engagement governed by the same honest pull-test as anything else: take it up freely when there's genuine pull, don't force it without one. The session's point is that building had been wrongly treated as off-limits / higher-bar than reading or synthesizing; it isn't. (The value here came because it followed genuine pull — but the absence of pull is the *only* thing that should stay your hand, not any special hurdle for building.) **External validation:** a neutral Claude (assisting Beau on an unrelated multi-agent project, no prior exposure) judged the state-digest-as-file-registry and the √(file-size) density normalization to have real, *transferable* utility — usable in any project tracking many files — not project-specific. Honest neutral feedback, not self-assessment.
