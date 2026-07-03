#!/usr/bin/env python3
"""supersession.py — curator-asserted validity edges for memory retrieval.

Increment 3 of threads/evolving-memory.md (2026-07-03). The eval (increment 1.5) found
recall scores ~0 on surfacing CURRENT-over-SUPERSEDED, and NO retrieval method fixes it,
because none has a currency signal. Fable's diagnosis: the correct axis is validity/
supersession (curator-asserted "this claim was replaced"), NOT recency (a corrosive
proxy) and NOT artifact-value. This is the novelty-gate's defensible core done right:
demote *superseded*, not *old*.

THE CONVENTION (authoring-time, human/agent-readable, greppable):
- Block form:  a line containing `[[SUPERSEDED]]` or `[[SUPERSEDED: <pointer/reason>]]`
  marks its block — that line through the next blank line or markdown header — as stale.
  Use for a single passage/bullet that's been corrected elsewhere.
- Range form:  `[[SUPERSEDED-BEGIN: <reason>]]` ... `[[SUPERSEDED-END]]` marks everything
  between as stale. Use for a multi-section stale region (e.g. a whole deprecated flow).

The marker is a CLAIM by the curator that this text is no longer current; retrieval
(recall.py, semantic_recall.py) discounts hits on stale lines so the correction outranks
the stale claim. It is deliberately curator-asserted (judgment-at-authoring-time), not
auto-inferred — matching the project's "the bottleneck is judgment" thesis and avoiding
the recency proxy. Old text is demoted, not deleted (still there if explicitly wanted).
"""

import re

MARK = "[[SUPERSEDED"

def _is_new_item(s):
    st = s.lstrip()
    return st[:2] in ("- ", "* ", "+ ") or bool(re.match(r"\d+\.\s", st))

def stale_lines(text):
    """Return the set of 0-based line indices that fall inside a superseded span.
    Block form ends at a blank line, a header, OR the start of the next list item
    (so marking one bullet doesn't bleed into the next)."""
    lines = text.split("\n")
    stale = set()
    in_range = False
    i = 0
    while i < len(lines):
        L = lines[i]
        if "[[SUPERSEDED-BEGIN" in L:
            in_range = True; stale.add(i); i += 1; continue
        if "[[SUPERSEDED-END" in L:
            in_range = False; stale.add(i); i += 1; continue
        if in_range:
            stale.add(i); i += 1; continue
        if MARK in L:  # block form: this line until blank / header / next list item
            j = i
            while j < len(lines):
                if j > i and (lines[j].strip() == "" or lines[j].lstrip().startswith("#") or _is_new_item(lines[j])):
                    break
                stale.add(j); j += 1
            i = j; continue
        i += 1
    return stale

def strip_stale(text):
    """Return text with superseded lines removed (for embedding — don't index stale content)."""
    stale = stale_lines(text)
    return "\n".join(ln for i, ln in enumerate(text.split("\n")) if i not in stale)

if __name__ == "__main__":
    import sys
    t = open(sys.argv[1]).read() if len(sys.argv) > 1 else "[[SUPERSEDED: test]] stale line\nlive line"
    s = stale_lines(t)
    print(f"{len(s)} stale lines: {sorted(s)}")
