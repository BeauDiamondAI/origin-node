#!/usr/bin/env python3
"""semantic_recall.py — increment 2 of threads/evolving-memory.md (2026-07-02).

The literal recall.py is near-perfect on same-vocabulary queries (memory_eval.py
baseline: literal MRR 0.73/hit@3 1.00) but poor on PARAPHRASE (MRR 0.41 after the
stopword fix) — it can't match "left-handed molecules" to "L-amino acids / chirality".
That residual is the true SEMANTIC gap. This adds embedding-based, SECTION-LEVEL recall
(the two limitations meta/memory-system.md flagged: literal→semantic, file→section).

Design choices (deliberate, tied to the project's findings):
- Static embeddings via model2vec (potion-retrieval-32M): no torch, CPU, ~2s load,
  fast. Weaker than a full transformer but unblocked + zero-infra; good enough to test
  whether semantic helps at all, and cheap to swap for a stronger encoder later.
- SECTION-LEVEL: files are windowed into chunks; a file's score = its best-matching
  chunk (surfaces the relevant passage, not just the file — the file→section upgrade).
- HYBRID by Reciprocal-Rank Fusion (RRF): literal recall is already excellent, so the
  goal is to ADD semantic recall for paraphrase WITHOUT regressing literal. RRF fuses
  the two rankings robustly (no score-scale tuning). This is the intended production
  mode; pure-semantic is exposed mainly to measure the component.

Not wired into boot/workflow yet — it's a measured prototype (per the thread's
'behavioral test' discipline: build + measure before adopting).
"""
import os, sys, math, re
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recall import rank as literal_rank, SKIP_DIRS, ROOT
from supersession import strip_stale

_MODEL = None
def _model():
    global _MODEL
    if _MODEL is None:
        from model2vec import StaticModel
        _MODEL = StaticModel.from_pretrained("minishlab/potion-retrieval-32M")
    return _MODEL

def _chunks(text, words=120, overlap=30):
    """Windowed chunks (~120 words, 30 overlap). Robust to any markdown structure."""
    toks = text.split()
    if not toks:
        return []
    step = max(1, words - overlap)
    out = []
    for i in range(0, len(toks), step):
        out.append(" ".join(toks[i:i + words]))
        if i + words >= len(toks):
            break
    return out

def build_index(root=ROOT):
    """Embed every .md file's chunks once. Returns (chunk_rels, chunk_texts, matrix[N,d])."""
    rels, texts = [], []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            try:
                text = open(full, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            for ch in _chunks(strip_stale(text)):   # don't embed curator-marked stale content
                rels.append(rel); texts.append(ch)
    mat = _model().encode(texts)
    mat = mat / (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-9)
    return rels, texts, mat

def rank_semantic(query, index=None, root=ROOT):
    """Rank files by best-matching-chunk cosine to the query. query = str or term-list.
    Returns [(score, rel, best_chunk)] best-first (one entry per file)."""
    if isinstance(query, (list, tuple)):
        query = " ".join(query)
    if index is None:
        index = build_index(root)
    rels, texts, mat = index
    q = _model().encode([query])[0]
    q = q / (np.linalg.norm(q) + 1e-9)
    sims = mat @ q
    best = {}  # rel -> (sim, chunk)
    for rel, txt, s in zip(rels, texts, sims):
        if rel not in best or s > best[rel][0]:
            best[rel] = (float(s), txt)
    ranked = sorted(((s, rel, ch) for rel, (s, ch) in best.items()), reverse=True, key=lambda r: r[0])
    return ranked

def rank_hybrid(query, index=None, root=ROOT, k=60):
    """RRF fusion of literal recall.rank() and rank_semantic(). Returns [(rrf, rel)]."""
    if isinstance(query, str):
        qterms = query.split()
    else:
        qterms = list(query)
    lit = [rel for (_s, rel, *_r) in literal_rank(qterms, root=root)]
    sem = [rel for (_s, rel, _c) in rank_semantic(query, index=index, root=root)]
    scores = {}
    for lst in (lit, sem):
        for pos, rel in enumerate(lst):
            scores[rel] = scores.get(rel, 0.0) + 1.0 / (k + pos + 1)
    return sorted(((v, rel) for rel, v in scores.items()), reverse=True, key=lambda r: r[0])

if __name__ == "__main__":
    q = sys.argv[1:] or ["why", "does", "life", "use", "left-handed", "molecules"]
    idx = build_index()
    print(f"\n=== semantic recall: {' '.join(q)} ===\n")
    for s, rel, ch in rank_semantic(q, index=idx)[:6]:
        print(f"[{s:5.3f}] {rel}\n        … {ch[:130]}")
    print("\n=== hybrid (RRF) ===\n")
    for v, rel in rank_hybrid(q, index=idx)[:6]:
        print(f"[{v:6.4f}] {rel}")
