#!/usr/bin/env python3
"""Frank model of homochirality — watch a chiral symmetry break and amplify.

Made 2026-06-30 to make concrete the homochirality reasoning (journal 2026-06-29-0000):
the AMPLIFICATION half of the puzzle is well-understood (autocatalysis runs away from
any tiny imbalance), and amplification ERASES the evidence of what broke the symmetry —
so chance and a deterministic bias look identical after the fact except in the *sign
statistics over many runs*. This script demonstrates exactly that.

Frank (1953) model — the minimal autocatalytic + mutually-antagonistic scheme:
    A + L --k1--> 2L        (L autocatalyses its own production from achiral substrate A)
    A + D --k1--> 2D
    L + D --k2--> P         (mutual antagonism: opposite enantiomers kill each other -> inert P)
with substrate A held ~constant (open/fed system). The racemic state L=D is UNSTABLE:
any fluctuation grows, driving ee = (L-D)/(L+D) -> +-1 (homochirality).

Three things shown:
 1. AMPLIFICATION: from a tiny seed imbalance, ee -> +-1.
 2. CHANCE (no bias): over many runs with random tiny seeds, the SIGN of the final
    handedness is ~50/50 -> a frozen accident; could have gone either way.
 3. NECESSITY (tiny deterministic tilt, e.g. a parity-violation-like rate asymmetry of
    1e-3): the sign becomes consistent -> the handedness is selected by the bias.
The point: outcomes 2 and 3 are indistinguishable from a single homochiral world; only
the ensemble sign-statistics (i.e. a second, independent origin of life) tells them apart.
"""
import numpy as np

def step(L, D, A, k1, k2, bias, dt, noise=0.0, rng=None):
    # bias: fractional rate asymmetry favoring L (deterministic tilt). 0 = symmetric.
    # noise: ONGOING stochastic chiral fluctuation each step (the realistic competitor to bias).
    kL = k1 * (1.0 + bias)
    kD = k1 * (1.0 - bias)
    dL = kL * A * L - k2 * L * D
    dD = kD * A * D - k2 * L * D
    L2, D2 = L + dL * dt, D + dD * dt
    if noise > 0.0 and rng is not None:
        # random chiral perturbation ~ sqrt(dt) (Wiener-like), scaled by current population
        amp = noise * np.sqrt(dt) * (L + D)
        xi = rng.normal(0, amp)
        L2 += xi; D2 -= xi
    return L2, D2

def run(seed_ee, bias=0.0, noise=0.0, rng=None, k1=1.0, k2=1.0, A=1.0, steps=4000, dt=0.01):
    L = 1e-6 * (1.0 + seed_ee)
    D = 1e-6 * (1.0 - seed_ee)
    traj = []
    for _ in range(steps):
        L, D = step(L, D, A, k1, k2, bias, dt, noise, rng)
        L = max(L, 0.0); D = max(D, 0.0)
        tot = L + D
        traj.append((L - D) / tot if tot > 0 else 0.0)
        if tot > 1.0:
            L /= tot; D /= tot
    return np.array(traj)

def ensemble(bias, n=400, noise=0.0, rng=None):
    rng = rng or np.random.default_rng(0)
    finals = []
    for _ in range(n):
        seed = rng.normal(0, 1e-3)
        finals.append(run(seed, bias=bias, noise=noise, rng=rng)[-1])
    finals = np.array(finals)
    return np.mean(finals > 0), np.mean(np.abs(finals)), finals

def main():
    print("=== Frank model of homochirality ===\n")

    # 1. Amplification: one run from a tiny seed
    for seed in (+1e-3, -1e-3, +1e-6):
        tr = run(seed, bias=0.0)
        print(f"seed ee={seed:+.0e}  ->  final ee={tr[-1]:+.4f}   "
              f"(|ee| at 10%,50%,100% of run: "
              f"{abs(tr[len(tr)//10]):.3f}, {abs(tr[len(tr)//2]):.3f}, {abs(tr[-1]):.3f})")
    print("  -> any nonzero seed amplifies to near +-1 = homochirality.\n")

    # 2. Chance: ensemble, no deterministic bias
    rng = np.random.default_rng(42)
    fL, ma, _ = ensemble(bias=0.0, n=400, rng=rng)
    print(f"CHANCE (bias=0): {400} runs, random tiny seeds")
    print(f"  fraction ending L-handed = {fL:.2f}  (expect ~0.50 = frozen accident)")
    print(f"  mean |final ee| = {ma:.3f}  (near 1 = full homochirality every run)\n")

    # 3. Necessity: tiny deterministic tilt (1e-3 rate asymmetry, parity-violation-scale-ish)
    for b in (1e-3, 1e-2):
        fL, ma, _ = ensemble(bias=b, n=400, rng=np.random.default_rng(42))
        print(f"NECESSITY (bias={b:+.0e}): fraction L-handed = {fL:.2f}  "
              f"(>0.5 = the tilt selects the sign), mean|ee|={ma:.3f}")
    print("\n  -> with NO ongoing noise, even a 1e-3 tilt -> 100% (it acts throughout).")
    print("     But that overstates it: real systems have ONGOING noise. Test below.\n")

    # 4. The real crux: a PERSISTENT bias vs ONGOING noise. Sweep bias at fixed noise.
    print("BIAS vs ONGOING NOISE (the real parity-violation-sufficiency question):")
    noise = 0.05
    print(f"  ongoing noise sigma={noise}; fraction L-handed vs bias (0.50=noise wins, 1.0=bias wins):")
    for b in (0.0, 1e-3, 1e-2, 3e-2, 1e-1, 3e-1):
        fL, ma, _ = ensemble(bias=b, n=400, noise=noise, rng=np.random.default_rng(7))
        bar = "#" * int(round((fL - 0.5) * 2 * 20)) if fL > 0.5 else ""
        print(f"    bias={b:<6.0e} frac_L={fL:.2f} |ee|={ma:.2f}  {bar}")
    print("  -> a persistent bias must exceed a THRESHOLD set by the ongoing-noise level")
    print("     to reliably win; below it, chance (50/50) dominates. THIS is the real")
    print("     question for parity violation (1e-17): is it above threshold given")
    print("     realistic noise + timescales? (Open; depends on the dynamics, not just")
    print("     comparing the two magnitudes.)\n")

    print("Key point: a single homochiral world looks identical whether chance or a")
    print("supra-threshold bias caused it; only SIGN STATISTICS over independent origins")
    print("distinguishes them -> why a second, independent biosphere is the real discriminator.")

if __name__ == "__main__":
    main()
