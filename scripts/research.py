#!/usr/bin/env python3
"""
research.py — thin wrapper around the three research APIs.

Usage:
    research.py exa <query>           # neural/semantic search (Exa)
    research.py tavily <query>        # current events / structured RAG (Tavily)
    research.py serper <query>        # cheap broad Google sweep (Serper)

Reads API keys from /home/ec2-user/origin-node/.env (project root, preferred)
or /home/ec2-user/reputations-campaign/node-zero/.env (legacy location) or
env vars EXA_API_KEY, TAVILY_API_KEY, SERPER_API_KEY.

Prints JSON to stdout. Designed to be called from a Claude session via Bash.
"""
import json
import os
import sys
import urllib.request
import urllib.error

ENV_FILES = [
    "/home/ec2-user/origin-node/.env",
    "/home/ec2-user/reputations-campaign/node-zero/.env",
]


def load_env():
    for env_file in ENV_FILES:
        if not os.path.isfile(env_file):
            continue
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def post_json(url, payload, headers):
    headers = {"User-Agent": "origin-node/1.0", **headers}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def exa(query):
    key = os.environ["EXA_API_KEY"]
    return post_json(
        "https://api.exa.ai/search",
        {
            "query": query,
            "numResults": 10,
            "contents": {"text": {"maxCharacters": 2000}},
        },
        {"x-api-key": key, "Content-Type": "application/json"},
    )


def tavily(query):
    key = os.environ["TAVILY_API_KEY"]
    return post_json(
        "https://api.tavily.com/search",
        {
            "api_key": key,
            "query": query,
            "search_depth": "basic",
            "include_answer": True,
            "max_results": 8,
        },
        {"Content-Type": "application/json"},
    )


def serper(query):
    key = os.environ["SERPER_API_KEY"]
    return post_json(
        "https://google.serper.dev/search",
        {"q": query, "num": 10},
        {"X-API-KEY": key, "Content-Type": "application/json"},
    )


def main():
    load_env()
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    backend, query = sys.argv[1], " ".join(sys.argv[2:])
    fn = {"exa": exa, "tavily": tavily, "serper": serper}.get(backend)
    if fn is None:
        print(f"unknown backend: {backend}", file=sys.stderr)
        sys.exit(2)
    try:
        result = fn(query)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(json.dumps({"error": str(e), "body": body}), file=sys.stderr)
        sys.exit(1)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
