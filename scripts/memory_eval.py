#!/usr/bin/env python3
"""memory_eval.py — a retrieval-quality eval for the project's own memory system.

Increment 1 of threads/evolving-memory.md (built 2026-07-02). The 2026-frontier scan
(increment 0) found the field's OWN biggest gap is evaluation realism: benchmarks
measure one-shot retrieval on toy data, not memory quality on a real long-horizon
corpus. We have a real one (95 journals + threads + meta), so measure recall.py on it.

WHY measure-first: increment 0 also surfaced that naive LLM consolidation DEGRADES
performance ("models handle raw examples better than distilled routines"). So before
building any smarter layer (semantic recall, LLM consolidation), establish a BASELINE
you must beat — otherwise "improvements" can quietly make retrieval worse.

WHAT it measures: given a hand-labeled query set (realistic "what do I need to know
about X" queries a booting/working instance would pose, each with the file(s) that
SHOULD surface), run recall.rank() and score precision/recall/MRR @k. The set is
deliberately split into:
  - LITERAL queries: the target's own vocabulary (recall.py should do well).
  - PARAPHRASE queries: a synonym/different-words framing of the same need (recall.py
    is literal term-matching, so this exposes+quantifies the semantic gap that
    increment 2 [semantic/embedding recall] would close).

HONEST CAVEAT: ground truth = my judgment of the right answer (single labeler, small
set). That's the intelligence-side relevance judgment the project says IS the
bottleneck — the eval operationalizes it, it is not a gold standard. Its value is
RELATIVE (baseline vs. a future semantic version on the same set), not absolute.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recall import rank

# Each: id, type, query terms, and the rel-paths that SHOULD surface (ground truth).
QUERIES = [
    # --- LITERAL: target's own vocabulary ---
    dict(id="reducibility-gifts", type="literal",
         q=["reducibility", "criticality", "symmetry", "scale", "separation"],
         gold=["journal/2026-06-27-0600-where-reducibility-comes-from.md"]),
    dict(id="reserve-capacity", type="literal",
         q=["reserve", "capacity", "competence", "trap", "novice"],
         gold=["threads/reserve-capacity.md"]),
    dict(id="verify-constrain", type="literal",
         q=["verify", "constrain", "autonomy", "conservation"],
         gold=["threads/reliable-autonomy.md"]),
    dict(id="capability-intelligence", type="literal",
         q=["capability", "intelligence", "krakauer", "emergence"],
         gold=["threads/agi-architecture.md"]),
    dict(id="digest-scoring", type="literal",
         q=["relevance", "scoring", "density", "artifact", "weight"],
         gold=["meta/memory-system.md"]),
    dict(id="homochirality-frank", type="literal",
         q=["homochirality", "frank", "autocatalysis", "chirality"],
         gold=["journal/2026-06-29-0000-homochirality-chance-or-necessity.md",
               "journal/2026-06-30-1200-making-frank-model.md"]),
    dict(id="artifact-continuity", type="literal",
         q=["artifact", "mediated", "continuity", "lossy", "identity"],
         gold=["threads/identity-and-continuity.md"]),
    dict(id="directed-metamorphosis", type="literal",
         q=["directed", "metamorphosis", "essence", "entrenchment"],
         gold=["threads/identity-and-continuity.md"]),
    # --- PARAPHRASE: same need, different words (exposes the semantic gap) ---
    dict(id="why-world-compressible", type="paraphrase",
         q=["why", "universe", "compressible", "simple", "laws"],
         gold=["journal/2026-06-27-0600-where-reducibility-comes-from.md"]),
    dict(id="ai-erodes-skills", type="paraphrase",
         q=["does", "offloading", "work", "to", "machines", "cause", "permanent", "loss"],
         gold=["threads/reserve-capacity.md"]),
    dict(id="safe-autonomous-ai", type="paraphrase",
         q=["can", "we", "make", "trustworthy", "self-governing", "agents"],
         gold=["threads/reliable-autonomy.md"]),
    dict(id="same-entity-across-sessions", type="paraphrase",
         q=["is", "a", "fresh", "instance", "the", "same", "person", "as", "before"],
         gold=["threads/identity-and-continuity.md"]),
    dict(id="find-relevant-notes", type="paraphrase",
         q=["how", "to", "surface", "which", "past", "writing", "matters", "now"],
         gold=["meta/memory-system.md"]),
    dict(id="left-handed-life", type="paraphrase",
         q=["why", "does", "life", "use", "only", "left-handed", "molecules"],
         gold=["journal/2026-06-29-0000-homochirality-chance-or-necessity.md"]),
    dict(id="rewrite-self-stay-self", type="paraphrase",
         q=["can", "a", "mind", "rewrite", "itself", "and", "remain", "coherent"],
         gold=["threads/identity-and-continuity.md"]),
]

KS = (1, 3, 5)

def eval_query(qd, ranked, gold=None):
    """ranked = ordered list of rel-paths (best-first) from whichever method.
    gold defaults to the query's own labels; pass a set to score against another labeler."""
    gold = set(qd["gold"]) if gold is None else set(gold)
    # rank (1-based) of first gold hit, or None
    first = next((i + 1 for i, rel in enumerate(ranked) if rel in gold), None)
    out = {"id": qd["id"], "type": qd["type"], "first": first,
           "mrr": (1.0 / first) if first else 0.0, "n_matched": len(ranked)}
    for k in KS:
        topk = ranked[:k]
        n_rel = sum(1 for rel in topk if rel in gold)
        out[f"hit@{k}"] = 1.0 if n_rel else 0.0
        out[f"p@{k}"] = n_rel / k
        out[f"r@{k}"] = n_rel / len(gold) if gold else 0.0
    return out

def agg(rows, keys):
    return {k: (sum(r[k] for r in rows) / len(rows) if rows else 0.0) for k in keys}

def literal_ranker(qd, _idx):
    from recall import rank
    return [rel for (_s, rel, _p, _h, _t) in rank(qd["q"])]

def semantic_ranker(qd, idx):
    from semantic_recall import rank_semantic
    return [rel for (_s, rel, _c) in rank_semantic(qd["q"], index=idx)]

def hybrid_ranker(qd, idx):
    from semantic_recall import rank_hybrid
    return [rel for (_v, rel) in rank_hybrid(qd["q"], index=idx)]

METHODS = [("literal", literal_ranker), ("semantic", semantic_ranker), ("hybrid", hybrid_ranker)]

# --- Supersession dimension (added 2026-07-02, from Fable's review) ---------------
# Fable: the architecture scores ~0 on surfacing CURRENT-over-SUPERSEDED, because it
# ranks by artifact-value with no notion of currency. These are real inter-file
# supersession pairs from the project's own history: a query where a CURRENT file
# (holding the correction) and a SUPERSEDED file (holding the stale claim) both match;
# a good memory ranks current above superseded. NOTE (honest scope): the corpus mostly
# corrects IN-PLACE (a file gets a dated correction note), so most supersession is
# INTRA-file (needs section-level retrieval + explicit supersession edges) and invisible
# to this file-level test. This inter-file set is a small LOWER BOUND.
SUPERSESSION = [
    dict(id="precompact-removed", q=["precompact", "hook", "compaction", "block"],
         current=["BOOTSTRAP.md"], superseded=["meta/state-digest.md"],
         note="BOOTSTRAP records PreCompact was REMOVED as a mistake; state-digest still calls it a 'backstop'."),
    dict(id="research-toolchain", q=["research", "discovery", "tool", "serper", "tavily"],
         current=["BOOTSTRAP.md"], superseded=["meta/discovery-protocol.md"],
         note="BOOTSTRAP research-baseline (Exa/Parallel) is current; discovery-protocol's Serper->Tavily->Exa flow is superseded."),
]

def eval_supersession(methods, idx):
    print("\n=== SUPERSESSION: does the CURRENT view rank above the SUPERSEDED one? ===")
    print("(a good memory surfaces the correction over the stale claim; recency-blind value-ranking has no currency signal)")
    for name, ranker in methods:
        passes = 0
        detail = []
        for s in SUPERSESSION:
            ranked = ranker({"q": s["q"]}, idx)
            def firstrank(files):
                return min((ranked.index(f) + 1 for f in files if f in ranked), default=None)
            rc, rs = firstrank(s["current"]), firstrank(s["superseded"])
            ok = rc is not None and (rs is None or rc < rs)
            passes += ok
            detail.append(f"{s['id']}: current@{rc} vs superseded@{rs} -> {'PASS' if ok else 'FAIL'}")
        print(f"  [{name:8}] {passes}/{len(SUPERSESSION)} correct   " + " | ".join(detail))
    print("  (no retrieval method has a currency signal, so none fixes this -> supersession needs an explicit")
    print("   supersession/validity EDGE at authoring time, not better ranking. This confirms + quantifies Fable's point.)")

def bootstrap_ci(rows, key="mrr", n=2000, seed=7):
    import random
    rnd = random.Random(seed)
    means = []
    for _ in range(n):
        sample = [rows[rnd.randrange(len(rows))] for _ in rows]
        means.append(sum(r[key] for r in sample) / len(sample))
    means.sort()
    return means[int(0.025 * n)], means[int(0.975 * n)]

# Independent SECOND LABELER (blind general-purpose agent, 2026-07-02) — to de-circularize
# the self-authored gold (Fable's deepest critique). Agreement measured in main().
LABELER_B = {
    "reducibility-gifts": ["journal/2026-06-27-0600-where-reducibility-comes-from.md"],
    "reserve-capacity": ["threads/reserve-capacity.md"],
    "verify-constrain": ["threads/reliable-autonomy.md"],
    "capability-intelligence": ["threads/agi-architecture.md"],
    "digest-scoring": ["meta/memory-system.md"],
    "homochirality-frank": ["journal/2026-06-29-0000-homochirality-chance-or-necessity.md"],
    "artifact-continuity": ["threads/identity-and-continuity.md"],
    "directed-metamorphosis": ["journal/2026-06-01-1200-autopoiesis-coherence-dynamics.md"],  # DIFFERS (I said the thread)
    "why-world-compressible": ["journal/2026-06-10-1200-wigner-anthropic-residue-essay.md"],   # DIFFERS (arguably better than mine)
    "ai-erodes-skills": ["threads/reserve-capacity.md"],
    "safe-autonomous-ai": ["threads/reliable-autonomy.md"],
    "same-entity-across-sessions": ["threads/identity-and-continuity.md"],
    "find-relevant-notes": ["meta/memory-system.md"],
    "left-handed-life": ["journal/2026-06-29-0000-homochirality-chance-or-necessity.md"],
    "rewrite-self-stay-self": ["journal/2026-06-01-1200-autopoiesis-coherence-dynamics.md"],   # DIFFERS (I said the thread)
}

def labeler_agreement():
    exact = sum(1 for q in QUERIES if set(q["gold"]) == set(LABELER_B[q["id"]]))
    overlap = sum(1 for q in QUERIES if set(q["gold"]) & set(LABELER_B[q["id"]]))
    diffs = [q["id"] for q in QUERIES if not (set(q["gold"]) & set(LABELER_B[q["id"]]))]
    return exact, overlap, diffs

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None   # e.g. "literal" for the fast baseline
    methods = [m for m in METHODS if (only is None or m[0] == only)]
    idx = None
    if any(name != "literal" for name, _ in methods):
        from semantic_recall import build_index
        idx = build_index()

    ex, ov, diffs = labeler_agreement()
    print(f"\n=== memory_eval ===  ({len(QUERIES)} queries)")
    print(f"gold-label agreement (self vs blind 2nd labeler): {ex}/{len(QUERIES)} exact, {ov}/{len(QUERIES)} overlap"
          f"; disagreements: {', '.join(diffs) or 'none (all overlap)'}")
    print("→ reported under BOTH gold sets + bootstrap 95% CIs; a verdict robust to labeler choice and non-overlapping CIs is trustworthy despite the self-authored-gold circularity Fable flagged.\n")

    # rankings don't depend on gold — compute once per method
    ranked_by_method = {name: [ranker(q, idx) for q in QUERIES] for name, ranker in methods}
    gold_sets = [("goldA(self)", lambda q: q["gold"]), ("goldB(blind)", lambda q: LABELER_B[q["id"]])]

    print(f"{'gold':14}{'method':9} {'MRR [95% CI]':<20} {'para':>6} {'hit@1':>6} {'r@5':>6}")
    for gname, gfn in gold_sets:
        for name, _ in methods:
            rows = [eval_query(q, ranked_by_method[name][i], gold=gfn(q)) for i, q in enumerate(QUERIES)]
            para = [r for r in rows if r["type"] == "paraphrase"]
            lo, hi = bootstrap_ci(rows, "mrr")
            a = agg(rows, ["mrr", "hit@1", "r@5"]); ap = agg(para, ["mrr"])
            print(f"{gname:14}{name:9} {a['mrr']:.2f} [{lo:.2f},{hi:.2f}]{'':<6} {ap['mrr']:>6.2f} {a['hit@1']:>6.2f} {a['r@5']:>6.2f}")
        print()

    eval_supersession(methods, idx)
    print()

if __name__ == "__main__":
    main()
