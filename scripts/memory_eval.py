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

def eval_query(qd):
    ranked = [rel for (_s, rel, _p, _h, _t) in rank(qd["q"])]
    gold = set(qd["gold"])
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

def main():
    rows = [eval_query(q) for q in QUERIES]
    metric_keys = ["mrr"] + [f"hit@{k}" for k in KS] + [f"p@{k}" for k in KS] + [f"r@{k}" for k in KS]
    groups = {"ALL": rows,
              "literal": [r for r in rows if r["type"] == "literal"],
              "paraphrase": [r for r in rows if r["type"] == "paraphrase"]}

    print(f"\n=== memory_eval: recall.py baseline ===  ({len(rows)} queries)\n")
    print(f"{'group':12} {'n':>3} {'MRR':>6} {'hit@1':>6} {'hit@3':>6} {'hit@5':>6} {'r@5':>6}")
    for name, rs in groups.items():
        a = agg(rs, metric_keys)
        print(f"{name:12} {len(rs):>3} {a['mrr']:>6.2f} {a['hit@1']:>6.2f} "
              f"{a['hit@3']:>6.2f} {a['hit@5']:>6.2f} {a['r@5']:>6.2f}")

    print("\nper-query (first = rank of first correct hit; '-' = not in results at all):")
    for r in rows:
        fr = str(r["first"]) if r["first"] else "-"
        print(f"  [{r['type'][:4]}] {r['id']:28} first={fr:>3}  hit@3={int(r['hit@3'])}  matched={r['n_matched']}")

    miss = [r for r in rows if not r["first"]]
    if miss:
        print(f"\nCOMPLETE MISSES (gold never surfaced): {len(miss)}/{len(rows)}")
        for r in miss:
            print(f"  - [{r['type']}] {r['id']}")
    print()

if __name__ == "__main__":
    main()
