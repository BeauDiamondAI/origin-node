#!/usr/bin/env python3
"""
Thin wrapper for the Parallel API (Beau: "#1 all-purpose deep-research tool for agents").
Two modes:
  search  — one round-trip natural-language objective + keyword queries -> LLM-optimized excerpts
  task    — deep-research agent (multi-hop, minutes), cited structured output

Usage:
  python3 scripts/parallel_research.py search "<objective sentence>" "<kw q1>" "<kw q2>" ["<kw q3>"]
  python3 scripts/parallel_research.py task "<research question>" [processor]   # processor default: pro

Notes:
  - search_queries: 2-3 diverse 3-6-word keyword queries (NOT sentences, no site: ops).
  - task processors: pro (~<10min, blocking ok) / ultra / ultra8x (up to 2hr -> use webhooks, not this).
    Append -fast for lower latency (pro-fast). Run `task` via Bash run_in_background (it takes minutes).
  - Key: PARALLEL_API_KEY in origin-node/.env (loaded below).
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_key():
    if not os.environ.get("PARALLEL_API_KEY"):
        with open(os.path.join(ROOT, ".env")) as f:
            m = re.search(r'PARALLEL_API_KEY=["\']?([^"\'\n]+)', f.read())
        if not m:
            sys.exit("PARALLEL_API_KEY not found in env or .env")
        os.environ["PARALLEL_API_KEY"] = m.group(1).strip()

def do_search(objective, queries):
    from parallel import Parallel
    client = Parallel()
    search = client.search(objective=objective, search_queries=queries)
    for r in search.results:
        print(f"\n- {getattr(r,'title','')}  |  {getattr(r,'url','')}")
        for ex in (getattr(r, "excerpts", None) or [])[:3]:
            print("   ", ex[:280].replace("\n", " "))

def do_task(question, processor="pro"):
    from parallel import Parallel
    client = Parallel()
    run = client.task_run.create(input=question, processor=processor)
    print(f"[parallel task: run_id={run.run_id} processor={processor} — blocking for result...]", file=sys.stderr, flush=True)
    result = client.task_run.result(run.run_id, api_timeout=3600)
    out = result.output
    print(getattr(out, "content", ""))
    basis = getattr(out, "basis", None) or []
    print(f"\n[basis: {len(basis)} fields | "
          + ", ".join(f"{getattr(b,'field','?')}:{len(getattr(b,'citations',[]) or [])}cit" for b in basis[:8]) + "]",
          file=sys.stderr)

def main():
    load_key()
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    mode = sys.argv[1]
    if mode == "search":
        objective = sys.argv[2]
        queries = sys.argv[3:] or [objective]
        do_search(objective, queries[:3])
    elif mode == "task":
        question = sys.argv[2]
        processor = sys.argv[3] if len(sys.argv) > 3 else "pro"
        do_task(question, processor)
    else:
        sys.exit(f"unknown mode {mode!r} (use: search | task)")

if __name__ == "__main__":
    main()
