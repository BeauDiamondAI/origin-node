#!/usr/bin/env python3
"""Finite-trial abiogenesis: how search STRUCTURE dissolves the "too improbable" argument.

Made 2026-07-05, continuing the chance-vs-necessity vein (homochirality Frank model 06-30;
convergent evolution 06-30; the emergence atlas 07-04). The classic anti-abiogenesis
argument (Hoyle's "tornado in a junkyard") is quantitative: a functional self-replicator
needs a specific sequence of length L over an alphabet of k monomers, so the chance of
hitting it by random assembly is k^-L — astronomically smaller than any plausible number
of prebiotic trials. Ergo "chance can't do it."

This makes the counter concrete: that argument assumes UNIFORM RANDOM search for ONE long
target. Drop that assumption — as real chemistry does — and the number moves by tens of
orders of magnitude. The point isn't "abiogenesis is proven easy" (it isn't; the real
prebiotic search structure is the open empirical question). The point is that the ANSWER
IS ENTIRELY CONTROLLED BY THE SEARCH STRUCTURE, so an estimate built on uniform-random
search measures the assumption, not the world — exactly the homochirality lesson (a
persistent bias above threshold beats astronomical odds) in probabilistic form.

Everything is in log10, orders of magnitude. Numbers are illustrative toy figures, not
real estimates — the structure of the dependence is the content.
"""
import math

log10 = lambda x: math.log10(x)

# --- the trial budget (rough, order-of-magnitude; the literature spans ~10^40-10^52) ---
# molecules in a prebiotic ocean-ish reservoir * reaction attempts per molecule over ~1e8 yr
LOG_TRIALS = log10(1e44)   # ~10^44 assembly attempts available. Illustrative.

# --- the target ---
k = 4          # nucleotide alphabet
L = 100        # length of a "functional replicator" on the naive telling (a long ribozyme)

def log_expected_trials(log_p_hit):
    """Expected trials to first success = 1/p_hit; return log10 of it."""
    return -log_p_hit

def verdict(log_needed):
    gap = log_needed - LOG_TRIALS
    if gap <= 0:
        return f"FEASIBLE (needs 10^{log_needed:.0f} <= budget 10^{LOG_TRIALS:.0f})"
    return f"beyond budget by 10^{gap:.0f}  (needs 10^{log_needed:.0f})"

def main():
    print(f"Trial budget assumed: 10^{LOG_TRIALS:.0f} assembly attempts.  Target: length-{L} sequence, alphabet {k}.\n")

    # (0) NAIVE: uniform search for one specific L-mer -----------------------------------
    log_p0 = -L * log10(k)                       # p = k^-L
    need0 = log_expected_trials(log_p0)
    print("(0) Naive uniform search for ONE specific length-100 sequence:")
    print(f"     p(hit)=k^-L = 10^{log_p0:.0f};  {verdict(need0)}")
    print("     -> this is the 'impossible' number. Now relax each unphysical assumption:\n")

    # Each factor below is an INDEPENDENT relaxation of the naive model, computed from the
    # naive baseline — NOT a cumulative stack (stacking would double-count, and building this
    # is what surfaced that: my first draft's "+X +Y" ladder falsely implied they multiply).
    # The honest, stronger point: ANY ONE realistic assumption alone crosses into feasibility.

    # (1) NEUTRAL NETWORK: not one target, but a large functional fraction f -------------
    # RNA sequence-function maps have huge neutral networks; a fraction f of sequences fold
    # to a working ribozyme. Say ~1 in 10^11 (measured-ish for some ribozyme functions).
    log_f = log10(1e-11)
    need1 = -log_f
    print("(1) neutral network alone (many sequences work, not one specific target):")
    print(f"     functional fraction f~10^{log_f:.0f};  need ~1/f = 10^{need1:.0f} trials;  {verdict(need1)}")
    print(f"     dropping 'exactly one target' alone buys ~10^{need0-need1:.0f} orders.\n")

    # (2) SHORTER MINIMAL REPLICATOR ----------------------------------------------------
    # The FIRST replicator need not be a 100-mer ribozyme; minimal self-replicating systems
    # / autocatalytic sets can be far smaller. Naive uniform search, but at L=30.
    L2 = 30
    log_p2 = -L2 * log10(k)
    need2 = -log_p2
    print(f"(2) shorter minimal replicator alone (L={L2}, not 100; still naive uniform):")
    print(f"     p=k^-{L2}=10^{log_p2:.0f};  need ~10^{need2:.0f} trials;  {verdict(need2)}\n")

    # (3) MODULAR / HIERARCHICAL ASSEMBLY -----------------------------------------------
    # You don't assemble L monomers at once and hope. You find small functional modules,
    # SELECTION keeps them, and you combine survivors. An exponential k^L search becomes
    # ~ (L/m) independent searches of length m — additive in log, not multiplicative.
    m = 6
    n_modules = math.ceil(L / m)                  # modularize the FULL length-100 target
    log_p_module = -m * log10(k)
    need3 = log10(n_modules) + (-log_p_module)
    print(f"(3) modular assembly alone (build the length-{L} target as {n_modules} modules of {m}, select, combine):")
    print(f"     EXPONENTIAL k^{L} search becomes ADDITIVE: ~{n_modules} x 10^{-log_p_module:.0f} = 10^{need3:.1f};  {verdict(need3)}")
    print("     same trick evolution uses — cumulative selection, not one lucky jump.\n")

    # --- summary: each factor ALONE, from the naive baseline --------------------------
    print("=== each factor ALONE vs the naive baseline (log10 trials needed) — NOT cumulative ===")
    for label, n in [("naive uniform, one 100-mer", need0),
                     ("neutral network alone", need1),
                     ("shorter replicator alone (L=30)", need2),
                     ("modular assembly alone (L=100)", need3)]:
        bar = "beyond budget" if n > LOG_TRIALS else "WITHIN BUDGET"
        print(f"  10^{n:>5.1f}   {label:34}  [{bar}]")
    print(f"  10^{LOG_TRIALS:>5.1f}   {'<-- trial budget':34}")
    print(f"\nThe naive number is 10^{need0:.0f}; the trial budget is 10^{LOG_TRIALS:.0f}. Each single realistic")
    print("assumption ALONE drops it below budget (the biggest single drop, neutral networks,")
    print(f"is ~10^{need0-need1:.0f}). So the naive 'impossible' number is fragile to ANY one of them.")
    print("NONE of this proves abiogenesis was easy;")
    print("it shows the naive number measures the *uniform-random assumption*, not chemistry. The")
    print("real question is empirical: what was the prebiotic search's actual structure? That is")
    print("chance-WITHIN-structure — neither pure chance (uniform) nor pure necessity (determined) —")
    print("the same shape as homochirality (structure/threshold, not raw odds, decides the outcome).")

if __name__ == "__main__":
    main()
