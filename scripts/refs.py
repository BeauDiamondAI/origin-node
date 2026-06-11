#!/usr/bin/env python3
"""refs.py — crude dependency/cross-reference tracker for the project's own corpus.

A dogfood of the "dependency-self-model" the directed-metamorphosis arc named as the
missing piece for safe self-modification (see threads/identity-and-continuity.md move
5 and threads/agi-architecture.md "dependency-self-model" verification). Crude on
purpose — stdlib only, literal path-matching — exactly like scripts/recall.py was for
relevance. The point is to learn WHERE the hard part is, not to ship a product.

What it does: parses every .md file for references to other project files (the
*explicit/structural* dependency graph) and answers "if I change X, what points at X
and might go stale?" (reverse deps).

What it can't do — and this is the finding, not a bug: it catches only *explicit*
references (a file naming another file's path). It cannot see *implicit/conceptual*
dependencies — file Z relying on a claim in file Y without naming Y. That gap mirrors
the arc's result exactly: models "do not explicitly represent the dependencies between
pieces of knowledge, so the consequences of an edit are unknown in advance." Structural
deps = plumbing (this script). Conceptual deps = judgment (needs the model). Same
"bottleneck is judgment, not plumbing" shape recall.py found for relevance.

Usage:
  python3 scripts/refs.py <file>     reverse + forward deps for one file
  python3 scripts/refs.py --orphans  .md files nothing references
  python3 scripts/refs.py --stale <commit>  files referencing anything changed since <commit>
"""
import os, re, sys, collections, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {".git", "logs", "node_modules", "__pycache__", "temp"}  # temp/ is gitignored
PATH_RE = re.compile(r"(?:[\w.-]+/)*[\w.-]+\.(?:md|py|sh)")

def project_files():
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            if fn.endswith((".md", ".py", ".sh")):
                out.append(os.path.relpath(os.path.join(dp, fn), ROOT))
    return out

def resolve(ref, known, by_base):
    if ref in known:
        return ref
    cands = by_base.get(os.path.basename(ref), [])
    return cands[0] if len(cands) == 1 else None  # ambiguous basename -> skip (honest)

def build():
    files = project_files()
    known = set(files)
    by_base = collections.defaultdict(list)
    for f in files:
        by_base[os.path.basename(f)].append(f)
    fwd = collections.defaultdict(set)
    for f in files:
        if not f.endswith(".md"):
            continue
        try:
            text = open(os.path.join(ROOT, f), encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for m in PATH_RE.findall(text):
            tgt = resolve(m, known, by_base)
            if tgt and tgt != f:
                fwd[f].add(tgt)
    rev = collections.defaultdict(set)
    for src, tgts in fwd.items():
        for t in tgts:
            rev[t].add(src)
    return files, fwd, rev, known, by_base

def main():
    files, fwd, rev, known, by_base = build()
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == "--orphans":
        for f in sorted(x for x in files if x.endswith(".md")):
            if not rev.get(f):
                print(f"(unreferenced) {f}")
        return
    if args[0] == "--stale" and len(args) > 1:
        try:
            changed = subprocess.check_output(
                ["git", "-C", ROOT, "diff", "--name-only", args[1], "HEAD"],
                text=True).split()
        except subprocess.CalledProcessError:
            print("git diff failed"); return
        flagged = set()
        for c in changed:
            for src in rev.get(c, ()):
                flagged.add((src, c))
        for src, c in sorted(flagged):
            print(f"{src}  references changed file  {c}")
        return
    q = resolve(args[0], known, by_base) or args[0]
    r, f = sorted(rev.get(q, [])), sorted(fwd.get(q, []))
    print(f"# {q}")
    print(f"\n## referenced BY ({len(r)}) — may go stale if you change {os.path.basename(q)}:")
    for x in r:
        print(f"  <- {x}")
    print(f"\n## references ({len(f)}):")
    for x in f:
        print(f"  -> {x}")

if __name__ == "__main__":
    main()
