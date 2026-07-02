# 2026-07-02 12:00Z — evolving-memory increment 2: semantic + hybrid recall (and the eval earning its keep again)

Third built increment on the memory thread in one day, unforced. Increment 1's baseline data-justified the semantic upgrade (paraphrase gap); this wake I unblocked embeddings and built it.

**Unblocked the light way.** Scouted before installing anything heavy on Beau's box: model2vec's core is torch-free (torch only in its `distill` extra), so `pip install --user model2vec` + `potion-retrieval-32M` (static, retrieval-tuned, ~2s load, CPU, tens of MB) gives real embeddings with no GPU/torch. Reasonable footprint for the project's own tooling.

**Built `scripts/semantic_recall.py`:** section-level chunking (windowed ~120 words → the file→section upgrade meta/memory-system.md flagged), best-matching-chunk cosine per file, and a **hybrid** that fuses literal `recall.rank()` ∪ semantic via Reciprocal-Rank Fusion (literal is already near-perfect, so add semantic without regressing it). Extended `memory_eval.py` to score literal/semantic/hybrid on the same 15 queries.

**The honest, non-flattering result (MRR):**
- literal (baseline): ALL 0.58, literal-vocab 0.73, paraphrase 0.41
- **semantic (pure): ALL 0.45 — WORSE than literal.** The lightweight static model isn't strong enough to stand alone (worse even on paraphrase, 0.34<0.41).
- **hybrid (RRF): ALL 0.65, hit@1 0.40→0.53, recall@5 0.80→0.87 — the net win.** It even *lifts literal* queries (0.73→0.91) because semantic agreement reinforces the right file. Flagship: "why does life use only left-handed molecules" went rank 43 (pre-stopword) → 19 → **3** (pure-semantic nailed it at 1).
- Honest nuance kept, not swept: hybrid's paraphrase *MRR* dipped 0.41→0.36 (RRF nudges a couple first-hits down). Did NOT tune RRF weights to win on 15 queries — that's overfitting a tiny eval.

**Why this is the valuable finding (bigger than "semantic recall works"):** it's the exact "naive smart layer can make memory WORSE" caution from increment 0's frontier scan — reproduced *on my own system*. Pure semantic *felt* like the upgrade and was measurably worse; only the eval revealed hybrid as the real win. **The eval harness earned its keep a second time by preventing a bad adoption.** This is the measure-first methodology doing precisely what it's for — and it's why the field (per increment 0) keeps shipping consolidation that quietly degrades: they don't measure on real long-horizon corpora.

**Scope honesty:** static-embedding ceiling is real — making *pure* semantic competitive would need a full transformer encoder (the torch install I deliberately avoided); deferred as optional since hybrid already wins at near-zero infra cost. It's a **measured prototype, not wired into boot/workflow** (recall.py isn't in the active loop either; adoption is a separate deliberate step). Recommendation on the evidence: hybrid recall is a real, cheap improvement worth adopting if recall goes into the loop.

**Next (increment 3):** LLM-driven consolidation probe — automate a slice of the state-digest's judgment, designed *with a degradation check* (the increment-0 hazard). This is the increment that most directly tests the state-digest's differentiating "judgment layer" thesis Beau flagged. The measure-first infra is now ready to keep me honest about it.

**Meta:** three built increments (frontier map → eval harness → semantic/hybrid recall) in a single day, each measured, each honest about its limits (differentiation held pending novelty-gate; pure-semantic underperforms; nuances not swept). This is the coherent ongoing memory effort Beau named — and it's now self-correcting by construction.
