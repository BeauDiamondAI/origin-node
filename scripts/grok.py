#!/usr/bin/env python3
"""Thin wrapper for xAI Grok's Agent Tools API (real-time web + X search).

Why this exists: the obvious paths don't work with our creds.
  - The `x-research` SKILL hits the X/Twitter API (needs X_BEARER_TOKEN, a
    separate paid X Developer plan) + needs `bun`. We have neither.
  - Grok's old `/v1/chat/completions` + `search_parameters` live-search is
    DEPRECATED (HTTP 410).
  - The working path (derived 2026-06-15): POST https://api.x.ai/v1/responses
    with model grok-4.3 and built-in server-side tools x_search / web_search /
    code_interpreter. ~$0.36 for a multi-search query.

Usage:
  python3 scripts/grok.py "your question"                 # x_search (default)
  python3 scripts/grok.py --web "your question"           # web_search
  python3 scripts/grok.py --both "your question"          # x + web
  python3 scripts/grok.py --model grok-4.3 "..."          # override model
Key: XAI_API_KEY in origin-node/.env
"""
import json, os, sys, urllib.request, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_key():
    if os.environ.get("XAI_API_KEY"):
        return os.environ["XAI_API_KEY"]
    env = os.path.join(ROOT, ".env")
    with open(env) as f:
        m = re.search(r'^XAI_API_KEY=["\']?([^"\'\n]+)', f.read(), re.M)
    if not m:
        sys.exit("XAI_API_KEY not found in env or .env")
    return m.group(1)

def main():
    args = sys.argv[1:]
    tools = [{"type": "x_search"}]
    model = "grok-4.3"
    while args and args[0].startswith("--"):
        flag = args.pop(0)
        if flag == "--web":
            tools = [{"type": "web_search"}]
        elif flag == "--both":
            tools = [{"type": "x_search"}, {"type": "web_search"}]
        elif flag == "--model":
            model = args.pop(0)
        else:
            sys.exit(f"unknown flag {flag}")
    if not args:
        sys.exit(__doc__)
    question = " ".join(args)

    body = json.dumps({
        "model": model,
        "input": [{"role": "user", "content": question}],
        "tools": tools,
    }).encode()
    req = urllib.request.Request(
        "https://api.x.ai/v1/responses", data=body,
        headers={"Authorization": f"Bearer {load_key()}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.load(r)

    for item in d.get("output", []):
        if item.get("type") == "message":
            for c in item.get("content", []):
                if c.get("type") in ("output_text", "text"):
                    print(c.get("text", ""))
    u = d.get("usage", {})
    cost = u.get("cost_in_usd_ticks")
    sx = u.get("server_side_tool_usage_details", {})
    print(f"\n[grok {model} | x_search={sx.get('x_search_calls',0)} "
          f"web_search={sx.get('web_search_calls',0)} | "
          f"tokens={u.get('total_tokens','?')} | "
          f"~${cost/1e9:.3f}]" if cost else "", file=sys.stderr)

if __name__ == "__main__":
    main()
