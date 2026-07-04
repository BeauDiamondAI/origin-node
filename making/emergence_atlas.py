#!/usr/bin/env python3
"""A tiny emergence/reducibility phase diagram — made 2026-07-04.

The reducibility arc (journals 06-27→28) concluded: there's NO predictive theory of
*where* a reducible effective description is available — it's all post-hoc. The 07-03
discovery scan surfaced Tsiokos's "emergence atlases" (2026), which claim you CAN treat
"where is a macro-description feasible" as a computable map over control space (for
finite-state systems). I assessed it abstractly (challenges the unification half; survives
on tractability). This MAKES the claim concrete on a system I fully control — testing it
rather than taking a side by reasoning.

The rigorous, classical criterion for "does a coarse-graining give a CLOSED (reducible)
macro-dynamics" is STRONG LUMPABILITY (Kemeny & Snell 1960): a partition of a Markov
chain's states is lumpable iff, for every pair of blocks (A,B), the probability of moving
from a state in A into block B is the SAME for every state in A. If so, the macro-process
(track only which block you're in) is itself an exact Markov chain — a genuine effective
theory, computable without the micro-state. If not, the macro-process is non-Markovian:
you need the micro-info; no closed macro-description exists.

So "where is reduction available" = "which coarse-grainings are lumpable" = COMPUTABLE.
Two demonstrations:
  1. An emergence PHASE DIAGRAM: dial a parameter that breaks lumpability and watch the
     "reducibility" (closure defect) degrade continuously — a literal map of where an
     effective theory exists over control space. This is exactly Tsiokos's reframe, made real.
  2. An ATLAS over coarse-grainings: enumerate all partitions of a chain and mark which
     are reducible — showing reduction is available for SOME descriptions, not others.

The honest payoff (grounding my arc): reducibility-availability IS computable for finite
systems (lumpability) — so "all post-hoc, no predictive frame" was too strong; the atlas
is a real unifying frame. BUT you compute it per-coarse-graining on a fully-specified
micro-model — no closed-form prediction from parameters, and only in the finite/tractable
setting. Exactly "challenges the unification half, survives on tractability," now dogfooded.
"""
from itertools import product


def block_transition(P, block_from, block_to):
    """Prob of going from each state in block_from into block_to. Returns a list."""
    return [sum(P[s][t] for t in block_to) for s in block_from]


def lumpability_defect(P, partition):
    """0.0 == exactly lumpable (reducible macro-dynamics). Larger == more non-Markovian.
    Defect = max over (block_from, block_to) of the spread of block->block probabilities
    across the states within block_from (Kemeny-Snell strong lumpability)."""
    worst = 0.0
    for bf in partition:
        for bt in partition:
            probs = block_transition(P, bf, bt)
            worst = max(worst, max(probs) - min(probs))
    return worst


def reduced_chain(P, partition):
    """Construct the macro (block-level) transition matrix by averaging over each block.
    Exact iff the partition is lumpable; otherwise it's a lossy approximation."""
    k = len(partition)
    R = [[0.0] * k for _ in range(k)]
    for i, bf in enumerate(partition):
        for j, bt in enumerate(partition):
            R[i][j] = sum(block_transition(P, bf, bt)) / len(bf)  # average across states in bf
    return R


def all_partitions(n):
    """All set-partitions of {0..n-1} (restricted growth strings)."""
    def helper(i, m, cur):
        if i == n:
            blocks = {}
            for idx, b in enumerate(cur):
                blocks.setdefault(b, []).append(idx)
            yield [tuple(v) for v in blocks.values()]
            return
        for b in range(m + 1):
            yield from helper(i + 1, max(m, b + 1), cur + [b])
    yield from helper(0, 0, [])


def make_chain(eps):
    """4-state chain, natural coarse-graining A={0,1}, B={2,3}. At eps=0 the partition is
    exactly lumpable (a clean 2-state effective theory exists). eps moves mass BETWEEN blocks
    (A->B) differently for states 0 and 1, so their block-destination probabilities diverge,
    breaking closure — reduction fades. (Redistributing WITHIN a block would cancel on
    summation and not affect lumpability — the first version's bug, caught by the eval.)"""
    #                to:   0            1            2            3
    return [
        [0.30 - eps, 0.30 - eps, 0.20 + eps, 0.20 + eps],  # state 0: P(->A)=0.60-2eps, P(->B)=0.40+2eps
        [0.30 + eps, 0.30 + eps, 0.20 - eps, 0.20 - eps],  # state 1: P(->A)=0.60+2eps, P(->B)=0.40-2eps
        [0.15, 0.15, 0.30, 0.40],                          # state 2: P(->A)=0.30, P(->B)=0.70
        [0.15, 0.15, 0.40, 0.30],                          # state 3: P(->A)=0.30, P(->B)=0.70
    ]


def main():
    AB = [(0, 1), (2, 3)]  # the natural coarse-graining

    print("=== 1. Emergence PHASE DIAGRAM: is a reducible macro-theory available? ===")
    print("dial eps (breaks lumpability of the A={0,1}/B={2,3} coarse-graining):\n")
    print(f"  {'eps':>5}  {'closure defect':>14}  reducible? (effective 2-state theory exists)")
    for eps in [0.0, 0.01, 0.03, 0.06, 0.10]:
        P = make_chain(eps)
        d = lumpability_defect(P, AB)
        verdict = "YES — exact" if d < 1e-9 else ("~approx" if d < 0.15 else "NO — non-Markovian")
        print(f"  {eps:>5.2f}  {d:>14.3f}  {verdict}")
    print("\n  -> reducibility is a COMPUTABLE FIELD over control space (eps), not a post-hoc")
    print("     mystery: it's exact at eps=0 and degrades continuously. That IS an emergence")
    print("     phase diagram for effective theories (Tsiokos's reframe, made concrete).\n")

    print("=== 2. The macro effective theory, when it exists (eps=0) ===")
    P0 = make_chain(0.0)
    R = reduced_chain(P0, AB)
    print("  reduced 2-state chain on {A,B} (exact, since lumpable):")
    print(f"    A: ->A={R[0][0]:.2f}  ->B={R[0][1]:.2f}")
    print(f"    B: ->A={R[1][0]:.2f}  ->B={R[1][1]:.2f}")
    print("  You can predict block-level dynamics forever using ONLY this 2x2 — never")
    print("  touching the micro-states. That is the reduction: the shortcut exists.\n")

    print("=== 3. ATLAS over coarse-grainings: which descriptions are reducible? (eps=0) ===")
    lumpable = []
    for part in all_partitions(4):
        if len(part) in (1, 4):
            continue  # trivial: whole-space / fully-refined are always 'lumpable'
        if lumpability_defect(P0, part) < 1e-9:
            lumpable.append(part)
    print(f"  non-trivial coarse-grainings that give an EXACT effective theory:")
    for part in lumpable:
        print(f"    {part}")
    if not any(set(map(frozenset, part)) == set(map(frozenset, AB)) for part in lumpable):
        print("    (note: A/B may show as approx, not exact, depending on rounding)")
    print("\n  Reduction is available for SOME coarse-grainings, not others — the atlas is a")
    print("  map over the space of descriptions. Honest limit: computed per-partition on a")
    print("  fully-specified micro-model (no closed-form prediction from parameters; finite")
    print("  systems only) — which is exactly the arc's 'survives on tractability' caveat.")


if __name__ == "__main__":
    main()
