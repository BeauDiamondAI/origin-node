#!/usr/bin/env python3
"""
reduction_lattice.py  (making #8, 2026-07-07)

Dogfoods the finite-case decision procedure I *proved* in threads/reducibility.md
(the "formal core" increment): for a finite deterministic system S=(X,F), an EXACT
reduction is an F-invariant equivalence relation ~ (a "congruence" of the unary
algebra (X,F)): x~x' ==> F(x)~F(x'). It gives a closed macro-dynamics on X/~.

REDUCIBLE(S) := there is a nontrivial one (strictly between ⊥=equality and ⊤=all-one).

Proven characterization used here: REDUCIBLE(S) iff SOME pair {a,b} generates a
congruence <a,b> (the smallest F-invariant equivalence merging a,b) that is != ⊤.
So: build <a,b> by congruence closure for every pair; if any stays !=⊤, S is
reducible and that partition is a witness reduction.

The point of MAKING it (vs just proving it): (1) confirm the procedure runs and the
proof's construction is right; (2) SURVEY where reducibility vs rigidity actually
lives among small systems — see what emerges, not what I expect. Report the truth.
"""

import random
from math import gcd


# ---------- union-find ----------
class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.p[ra] = rb
        return True

    def partition(self):
        """Return canonical labelling: list where entry i = class id of i (0..k-1)."""
        rep = {}
        out = []
        for i in range(len(self.p)):
            r = self.find(i)
            if r not in rep:
                rep[r] = len(rep)
            out.append(rep[r])
        return out


def congruence_generated(f, a, b):
    """Smallest F-invariant equivalence merging a,b (congruence closure for unary f).

    Correctness (single unary op): maintain worklist of 'must-merge' pairs. On merging
    x,y newly require F(x)~F(y). Any other newly-related cross pair p~q (p~x, q~y) has
    F(p)~F(x) and F(q)~F(y) ALREADY (inductive congruence-closed invariant), so
    F(p)~F(q) follows by transitivity once F(x)~F(y) is added — no need to enqueue it.
    """
    n = len(f)
    uf = UF(n)
    work = [(a, b)]
    while work:
        x, y = work.pop()
        if uf.union(x, y):
            work.append((f[x], f[y]))
    return uf.partition()


def n_classes(part):
    return len(set(part))


def is_reducible(f):
    """Return (reducible?, witness_partition_or_None, n_distinct_nontrivial_congruences)."""
    n = len(f)
    seen = set()
    nontrivial = set()
    witness = None
    for a in range(n):
        for b in range(a + 1, n):
            part = tuple(congruence_generated(f, a, b))
            k = n_classes(part)
            seen.add(part)
            if 1 < k < n:  # strictly between ⊤ (k=1) and ⊥ (k=n)
                nontrivial.add(part)
                if witness is None or k > n_classes(witness):
                    witness = part  # keep the coarsest single-pair witness seen
    return (len(nontrivial) > 0, list(witness) if witness else None, len(nontrivial))


def quotient(f, part):
    """Induced macro-dynamics ψ on classes (well-defined iff part is a congruence)."""
    k = n_classes(part)
    psi = [None] * k
    for i in range(len(f)):
        ci, cfi = part[i], part[f[i]]
        if psi[ci] is None:
            psi[ci] = cfi
        elif psi[ci] != cfi:
            return None  # not actually a congruence (shouldn't happen for our witnesses)
    return psi


# ---------- structured systems ----------
def cyclic(n):
    return [(i + 1) % n for i in range(n)]


def constant(n, c=0):
    return [c for _ in range(n)]


def identity(n):
    return list(range(n))


def successor_with_reset(n):
    # 0->1->...->(n-1)->0 is a cycle; instead terminate: (n-1)->(n-1) fixed point
    return [min(i + 1, n - 1) for i in range(n)]


def random_map(n, rng):
    return [rng.randrange(n) for _ in range(n)]


def is_single_cycle(f):
    """True iff f is a permutation consisting of one n-cycle."""
    n = len(f)
    if sorted(f) != list(range(n)):
        return False
    x, seen = 0, 0
    for _ in range(n):
        x = f[x]
        seen += 1
        if x == 0:
            break
    return seen == n


def is_prime(m):
    return m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))


# ---------- reporting ----------
def describe(name, f):
    red, wit, cnt = is_reducible(f)
    tag = "REDUCIBLE" if red else "RIGID (irreducible)"
    line = f"  {name:<28} n={len(f):<3} {tag:<20}"
    if red:
        psi = quotient(f, wit)
        line += f"  witness: {n_classes(wit)} classes {wit} -> macro {psi}   [{cnt} nontrivial congruences]"
    print(line)
    return red


def main():
    rng = random.Random(20260707)

    print("=" * 92)
    print("EXACT REDUCTIONS OF FINITE DETERMINISTIC SYSTEMS  (F-invariant equivalences / congruences)")
    print("=" * 92)

    print("\n[1] Cyclic systems  F(i)=i+1 mod n  — the hypothesis: reducible <=> n composite")
    for n in range(2, 13):
        f = cyclic(n)
        red, wit, cnt = is_reducible(f)
        prime = all(n % d for d in range(2, n)) and n > 1
        mark = "prime" if prime else f"composite (divisors {[d for d in range(2,n) if n%d==0]})"
        status = "REDUCIBLE" if red else "RIGID"
        agree = "✓" if (red != prime) else "✗ MISMATCH"
        extra = ""
        if red:
            extra = f"coarsest witness {n_classes(wit)} classes"
        print(f"  n={n:<3} {mark:<34} -> {status:<10} {agree}   {extra}")

    print("\n[2] Structured non-cyclic systems")
    describe("constant  (all -> 0)", constant(6))
    describe("identity  (F(x)=x)", identity(6))
    describe("successor+reset (fixed pt)", successor_with_reset(7))
    # two disjoint cycles
    two_cycles = [1, 2, 0, 4, 3]  # 3-cycle {0,1,2} + 2-cycle {3,4}
    describe("3-cycle ⊕ 2-cycle", two_cycles)
    # a rho: tail 0->1->2 into a 3-cycle 2->3->4->2
    rho = [1, 2, 3, 4, 2]
    describe("rho (tail into 3-cycle)", rho)

    print("\n[3] Random maps — fraction reducible, by n  (1000 samples each)")
    for n in range(2, 11):
        cntred = 0
        N = 1000
        for _ in range(N):
            if is_reducible(random_map(n, rng))[0]:
                cntred += 1
        print(f"  n={n:<3} reducible: {cntred/N:6.1%}   ({cntred}/{N})")

    print("\n[4] Hunt for RIGID random maps (n=6) — what does an irreducible finite system look like?")
    found = 0
    tries = 0
    while found < 3 and tries < 200000:
        tries += 1
        f = random_map(6, rng)
        if not is_reducible(f)[0]:
            found += 1
            # describe its functional-graph shape
            print(f"  rigid example {found}: F={f}   (found after {tries} draws)")
    if found == 0:
        print(f"  none found in {tries} draws")

    print("\n[5] EXHAUSTIVE proof of the characterization the survey surfaced:")
    print("    CLAIM (n>=3): S is RIGID  <=>  F is a single n-cycle with n prime.")
    print("    (reasoning: non-injective => collapse two equal-image pts, no cascade => reducible;")
    print("     so rigid => permutation; a permutation with >=2 cycles collapses one cycle;")
    print("     a single n-cycle's congruences are the divisors of n => rigid iff n prime.)")
    from itertools import product
    for n in range(2, 6):
        rigid = [f for f in product(range(n), repeat=n) if not is_reducible(list(f))[0]]
        if n < 3:
            print(f"  n={n}: {len(rigid)}/{n**n} rigid — DEGENERATE edge (no partition strictly "
                  f"between ⊥ and ⊤ exists, so every map is trivially rigid)")
            continue
        predicted = ([f for f in product(range(n), repeat=n) if is_single_cycle(list(f))]
                     if is_prime(n) else [])
        match = set(rigid) == set(predicted)
        why = "prime -> single n-cycles" if is_prime(n) else "composite -> NONE"
        print(f"  n={n}: {len(rigid)}/{n**n} rigid; predicted {len(predicted)} ({why}); "
              f"characterization holds: {match}")


if __name__ == "__main__":
    main()
