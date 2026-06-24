#!/usr/bin/env python3
"""Compute context-window occupancy % from a Claude Code transcript.

CLI:        _context.py <transcript_path>   -> prints integer percent (0-100+)
Importable: pct_from_transcript(path) -> int

Occupancy = input_tokens + cache_creation_input_tokens + cache_read_input_tokens
of the most recent assistant message carrying a usage block. That SUM is the real
size of the prompt sent for the turn = how full the context window is. input_tokens
ALONE is misleading under prompt caching: it's tiny (the bulk shows up as
cache_read_input_tokens). Verified against a real transcript 2026-06-24:
input_tokens=2 while cache_read=232694 — a naive parse under-reads ~100x.

Window size: CONTEXT_WINDOW_SIZE in .env, default 1_000_000 (claude-opus-4-8 [1m]).
If the model/window ever changes, set CONTEXT_WINDOW_SIZE in .env — no code edit.

FAIL-SAFE: any parse/IO error returns 0%, so a malfunction can NEVER trigger the
destructive (auto-clear) path. The system fails toward "do nothing", not "wipe".
"""
import json
import os
import sys

_ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".env")


def _load_window():
    val = 1_000_000
    try:
        with open(_ENV) as f:
            for line in f:
                line = line.strip()
                if line.startswith("CONTEXT_WINDOW_SIZE="):
                    val = int(line.split("=", 1)[1].strip())
    except (FileNotFoundError, ValueError):
        pass
    return val


def occupancy_tokens(transcript_path):
    # Read only the tail for speed — the last assistant-usage line is always near
    # the end (followed by at most a few tool-result lines). Over a long 1M-context
    # session the transcript can be 100MB+, and this runs every turn via the Stop
    # hook, so don't scan the whole file.
    tail_bytes = 2_000_000
    size = os.path.getsize(transcript_path)
    with open(transcript_path, "rb") as f:
        if size > tail_bytes:
            f.seek(size - tail_bytes)
            f.readline()  # discard the partial first line
        data = f.read()
    last = None
    for raw in data.splitlines():
        if b'"usage"' not in raw:
            continue
        try:
            obj = json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            continue
        u = (obj.get("message") or {}).get("usage")
        if isinstance(u, dict) and "input_tokens" in u:
            last = u
    if not last:
        return 0
    return (last.get("input_tokens", 0)
            + last.get("cache_creation_input_tokens", 0)
            + last.get("cache_read_input_tokens", 0))


def pct_from_transcript(transcript_path, window=None):
    if window is None:
        window = _load_window()
    if window <= 0:
        return 0
    return int(occupancy_tokens(transcript_path) * 100 / window)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("0")
        sys.exit(0)
    try:
        print(pct_from_transcript(sys.argv[1]))
    except Exception:
        print("0")  # fail-safe
