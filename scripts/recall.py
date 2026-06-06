#!/usr/bin/env python3
"""recall.py — minimal relevance-composition helper (dogfood prototype, 2026-06-05).

Given query terms, surface the most relevant project *memory* files — automating the
"what's relevant in my own memory" step done by hand each wake.

Deliberately crude/deterministic (no embeddings, stdlib only): a PROBE of whether
grep-grade relevance surfaces a good working-set, or whether the smart (embedding/LLM)
layer is actually needed. Applies the patterns.md entry "Relevance is the migrated
bottleneck": rank by *concentrated relevance* (artifact value + length-normalized match
density + term coverage), NOT raw match count — raw frequency would let the giant
episodic wake-log dominate every query, the exact corrosive proxy the pattern warns of.

Usage:  python3 scripts/recall.py <query terms...>
"""
import os, re, sys, math

ROOT = "/home/ec2-user/origin-node"

# artifact-class weights (longest matching prefix wins): concentrated/curated memory
# ranks above the episodic log; wake-log explicitly down-weighted (it logs everything).
WEIGHTS = [
    ("meta/patterns.md", 3.0),
    ("meta/state-digest.md", 3.0),
    ("threads/", 2.5),
    ("BOOTSTRAP.md", 2.2),
    ("meta/", 2.0),
    ("temp/", 1.5),
    ("journal/wake-log.md", 0.6),   # huge episodic log — down-weight so it can't win on size
    ("journal/", 1.0),
]
SKIP_DIRS = {".git", "logs", "node_modules", "experiments"}

def weight_for(rel):
    best, blen = 1.0, -1
    for prefix, w in WEIGHTS:
        if (rel == prefix or rel.startswith(prefix)) and len(prefix) > blen:
            best, blen = w, len(prefix)
    return best

def main():
    terms = [t.lower() for t in sys.argv[1:] if t.strip()]
    if not terms:
        print("usage: recall.py <query terms...>"); return
    results = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"): continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT)
            try:
                text = open(full, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            low = text.lower()
            present = sum(1 for t in terms if t in low)      # term coverage (strong signal)
            if present == 0: continue
            hits = sum(low.count(t) for t in terms)
            nlines = text.count("\n") + 1
            density = hits / math.sqrt(nlines)               # length-normalized (sqrt softens)
            score = weight_for(rel) * (present ** 2) * (1 + math.log1p(density))
            results.append((score, rel, present, hits, text))
    results.sort(reverse=True, key=lambda r: r[0])
    print(f"\n=== recall: {' '.join(terms)} ===  ({len(results)} files matched)\n")
    for score, rel, present, hits, text in results[:8]:
        print(f"[{score:6.1f}] {rel}  (terms {present}/{len(terms)}, {hits} hits)")
        best_line, best_n = "", 0   # show densest matching line, not first (more relevant)
        for line in text.splitlines():
            ll = line.lower()
            n = sum(ll.count(t) for t in terms)
            if n > best_n and line.strip():
                best_line, best_n = line.strip(), n
        if best_line:
            print(f"        … {best_line[:150]}")
    print()

if __name__ == "__main__":
    main()
