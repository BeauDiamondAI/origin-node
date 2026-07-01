#!/usr/bin/env python3
"""Reducible vs irreducible, made concrete — elementary cellular automata.

Made 2026-07-01 to make the reducibility theme (journals 06-27→28) tangible: the abstract
claim is "a reducible system has a computational SHORTCUT (jump to step N without simulating);
an irreducible one doesn't." Two elementary CAs from the SAME family make the contrast sharp:

- RULE 90 is REDUCIBLE. From a single seed it's the Sierpinski triangle = Pascal's triangle
  mod 2. So cell (row t, column k) = C(t,k) mod 2, and by Lucas' theorem C(t,k) is ODD iff
  (t & k) == k. That's a CLOSED FORM: you compute any future row directly, O(width) bit-ops,
  WITHOUT simulating the t-1 rows before it. The shortcut exists.

- RULE 30 is (believed) IRREDUCIBLE. No closed form is known; its center column is so
  shortcut-resistant that Wolfram used it as a pseudo-random number generator. To know row t
  you must run all t steps. No shortcut.

Same rule-space, one local update each — but one has a shortcut and one doesn't. That IS the
reducibility distinction, concretely. Bonus: even irreducible Rule 30 is macro-predictable
(coarse-grained density ~0.5) — micro-irreducible, macro-statistically-reducible (the
Israeli–Goldenfeld point).
"""
import time


def simulate(rule, width, steps):
    """Evolve an elementary CA from a single central seed. Returns list of rows (0/1 tuples)."""
    table = [(rule >> i) & 1 for i in range(8)]  # table[(l<<2)|(c<<1)|r] = new center
    row = [0] * width
    row[width // 2] = 1
    grid = [tuple(row)]
    for _ in range(steps):
        nxt = [0] * width
        for i in range(width):
            l = row[i - 1] if i > 0 else 0
            c = row[i]
            r = row[i + 1] if i < width - 1 else 0
            nxt[i] = table[(l << 2) | (c << 1) | r]
        row = nxt
        grid.append(tuple(row))
    return grid


def rule90_direct_row(t, width):
    """REDUCIBLE shortcut: compute Rule-90's row t DIRECTLY (no simulation of rows 0..t-1).
    From a single seed, live cell iff C(t,k) is odd  <=>  (t & k) == k (Lucas' theorem)."""
    row = [0] * width
    center = width // 2
    for k in range(t + 1):
        if (t & k) == k:  # C(t,k) is odd
            # k = offset from apex; live cells sit at center ± (t-2j) ... map via parity
            for pos in (center - t + 2 * k,):
                if 0 <= pos < width:
                    row[pos] = 1
    return tuple(row)


def center_column(grid):
    w = len(grid[0]) // 2
    return [g[w] for g in grid]


def main():
    W, T = 201, 100

    print("=== REDUCIBLE: Rule 90 — the shortcut works ===")
    grid90 = simulate(90, W, T)
    sim_row = grid90[T]
    direct_row = rule90_direct_row(T, W)
    match = sim_row == direct_row
    print(f"row {T} by SIMULATION (ran all {T} steps) vs by CLOSED FORM (jumped straight there):")
    print(f"  identical? {match}   (live cells: {sum(sim_row)})")
    # timing: the shortcut lets you reach very deep rows without simulating
    t0 = time.perf_counter(); _ = rule90_direct_row(100000, 200003); t_direct = time.perf_counter() - t0
    print(f"  computed row 100,000 directly in {t_direct*1000:.1f} ms — no simulation needed. "
          f"That's reducibility: a shortcut past the intermediate work.\n")

    print("=== IRREDUCIBLE: Rule 30 — no shortcut, must simulate ===")
    grid30 = simulate(30, W, T)
    col = center_column(grid30)
    ones = sum(col)
    # crude randomness: bit balance + no short period in the center column (Wolfram's PRNG)
    period = next((p for p in range(1, len(col) // 2)
                   if all(col[i] == col[i + p] for i in range(len(col) - p))), None)
    print(f"center column (Wolfram's PRNG): {ones}/{len(col)} ones (~balanced), "
          f"period found: {period} (None = no short period)")
    print("  no closed form is known for cell (t,k); to get row t you must run all t steps.\n")

    print("=== BONUS: micro-irreducible, MACRO-reducible (coarse-graining) ===")
    # coarse-grain Rule 30 into blocks; the block density is a stable, predictable macro-observable
    B = 20  # block size
    def block_density(row):
        live = [i for i, v in enumerate(row) if v]
        if not live:
            return 0.0
        lo, hi = min(live), max(live)
        span = row[lo:hi + 1]
        return sum(span) / len(span)
    late = grid30[T // 2:]  # after transient
    dens = [block_density(r) for r in late]
    mean_d = sum(dens) / len(dens)
    var_d = sum((d - mean_d) ** 2 for d in dens) / len(dens)
    print(f"Rule 30 in-cone density over the last {len(late)} rows: mean={mean_d:.3f}, "
          f"std={var_d**0.5:.3f}")
    print("  micro cells are irreducible, yet the coarse density sits at a stable, predictable")
    print("  value — you can predict the MACRO without shortcutting the MICRO. (Israeli–Goldenfeld.)")


if __name__ == "__main__":
    main()
