"""
Making #15 — Can equilibrium solubility explain a 50% carbon release from marine snow?
======================================================================================

THE CLAIM UNDER TEST
--------------------
Stief et al., "Hydrostatic pressure induces strong leakage of dissolved organic matter
from 'marine snow' particles," *Science Advances* 2026 (doi 10.1126/sciadv.aec5677).
In rotating pressure tanks simulating 2-6 km depth (~20-60 MPa), diatom aggregates
released DOM amounting to **~50% of initial carbon and ~58-63% of initial nitrogen**.
The press framing (SDU, phys.org) calls pressure a "giant juicer" squeezing solutes out.

The measurement is an experiment and I am not disputing it. What I want to know is whether
the *intuitive* mechanism — pressure makes organics more soluble, so more dissolves out —
can produce a number that large. That is a magnitude question with a clean answer, and it
is the same shape as making #9 (where a back-of-envelope caught a ~400x gap between a
naive mechanism and a reported pressure).

THE PHYSICS
-----------
For any dissolution/transfer equilibrium, pressure shifts the equilibrium constant by the
standard molar volume change of the reaction:

    (d ln K / dP)_T  =  -DeltaV / (R T)        =>   K(P) = K(0) * exp(-DeltaV * P / (R T))

Dissolution of organics typically has DeltaV < 0 (electrostriction: the dissolved state is
more compact than solute-plus-structured-water), so pressure favours dissolution. Good.
The question is purely how *much*.

Two-phase partition model: a solute sits in particle volume Vp and surrounding water Vw
with partition coefficient K_pw = C_particle / C_water. The dissolved fraction is

    f = 1 / (1 + R),    where R = K_pw * (Vp / Vw)

Pressure divides R by the enhancement factor E = exp(-DeltaV * P / (R T)), so

    f(P) = 1 / (1 + R0 / E)

PRE-REGISTERED PREDICTIONS (written before computing)
------------------------------------------------------
  P1. The DeltaV required to lift release to ~50% exceeds the small-organic range
      (5-30 cm3/mol) even in the most generous corner of the parameter space.
      [Criterion CORRECTED after the first run: my original statistic was mislabelled —
       it reported the largest of the per-row minimums (175) as "the smallest demanded
       anywhere", when the true minimum is 53. Fixed to report both the generous corner
       and a realistic-baseline corner. The claim is weaker than I first wrote and is
       stated at its true strength.]
  P2. At physically plausible DeltaV (5-30 cm3/mol), the release shift is small — single
      digits in percentage points, nowhere near 50%.
  P3. The conclusion is robust across the plausible range of baseline release (1-20%) and
      across the full experimental pressure range (20-60 MPa).

If these hold, the honest conclusion is NOT that the paper is wrong — it is that the
mechanism cannot be equilibrium molecular solubility, and must be structural (cell lysis,
membrane failure, or a cooperative gel volume-phase transition). That distinction matters
because the two make *different further predictions*, stated at the end.

Run: python3 marine_snow_pressure_leakage.py
Pure stdlib.
"""

import math

R_GAS = 8.314          # J/(mol K)
T_DEEP = 275.0         # K (~2 C, deep ocean)
PRESSURES = [20e6, 40e6, 60e6]        # Pa; 2 km, 4 km, 6 km
CM3_PER_MOL = 1e-6                    # cm3/mol -> m3/mol

TARGET_RELEASE = 0.50                 # the reported ~50% carbon release


def enhancement(dV_cm3, P, T=T_DEEP):
    """E = exp(-dV*P/(RT)); dV given in cm3/mol, negative = dissolution favoured."""
    return math.exp(-(dV_cm3 * CM3_PER_MOL) * P / (R_GAS * T))


def released_fraction(f0, dV_cm3, P, T=T_DEEP):
    """Dissolved fraction at pressure, given baseline dissolved fraction f0 at 1 atm."""
    R0 = (1.0 - f0) / f0                      # R0 = K*(Vp/Vw) implied by f0
    return 1.0 / (1.0 + R0 / enhancement(dV_cm3, P, T))


def required_dV(f0, f_target, P, T=T_DEEP):
    """dV (cm3/mol) needed to move baseline f0 to f_target at pressure P."""
    R0 = (1.0 - f0) / f0
    Rt = (1.0 - f_target) / f_target
    E_needed = R0 / Rt
    return -(R_GAS * T * math.log(E_needed)) / P / CM3_PER_MOL


def main():
    print("=" * 78)
    print("Making #15 — can equilibrium solubility explain ~50% DOM release?")
    print(f"T = {T_DEEP} K; pressures = 2/4/6 km (20/40/60 MPa)")
    print("=" * 78)

    # ---- [1] What DeltaV would be REQUIRED?
    print("\n[1] REQUIRED DeltaV to reach 50% release (P1)")
    print("    (typical |DeltaV| for dissolution/transfer of small organics: 5-30 cm3/mol;")
    print("     pressure-unfolding of a whole protein: ~50-100 cm3/mol)")
    print(f"    {'baseline release':>17s} {'20 MPa':>12s} {'40 MPa':>12s} {'60 MPa':>12s}")
    all_required = []
    for f0 in [0.01, 0.05, 0.10, 0.20]:
        row = [required_dV(f0, TARGET_RELEASE, P) for P in PRESSURES]
        all_required += [abs(v) for v in row]
        print(f"    {f0*100:16.0f}% " + " ".join(f"{v:11.0f}" for v in row))
    easiest = min(all_required)   # most generous corner: high baseline AND deepest pressure
    typical = min(abs(required_dV(0.05, TARGET_RELEASE, P)) for P in PRESSURES)
    print(f"\n    smallest |DeltaV| demanded ANYWHERE (most generous corner: 20% baseline,"
          f" 60 MPa): {easiest:.0f} cm3/mol")
    print(f"    at a more realistic 5% baseline, the easiest corner still demands:"
          f" {typical:.0f} cm3/mol")
    # criterion: even the most generous corner must exceed the small-organic range (5-30)
    p1 = easiest > 30

    # ---- [2] What do PLAUSIBLE DeltaV actually give?
    print("\n[2] ACTUAL release at physically plausible DeltaV (P2), baseline 5%")
    print(f"    {'DeltaV (cm3/mol)':>17s} {'E(40MPa)':>10s} {'20 MPa':>10s} {'40 MPa':>10s} {'60 MPa':>10s}")
    f0 = 0.05
    plausible_max = 0.0          # scoped to the STATED plausible range, |dV| <= 30
    for dV in [-5, -10, -20, -30, -50, -100]:
        rel = [released_fraction(f0, dV, P) for P in PRESSURES]
        if abs(dV) <= 30:
            plausible_max = max(plausible_max, max(rel))
        tag = "" if abs(dV) <= 30 else "   <- beyond molecular range (protein-unfolding scale)"
        print(f"    {dV:17d} {enhancement(dV, 40e6):10.2f} "
              + " ".join(f"{r*100:9.1f}%" for r in rel) + tag)
    print(f"\n    baseline {f0*100:.0f}%; within the plausible range (|DeltaV|<=30) the best"
          f" case reaches {plausible_max*100:.1f}% (target {TARGET_RELEASE*100:.0f}%)")
    print("    NOTE: the -100 row does approach the target at 60 MPa — but a volume change")
    print("    of 100 cm3/mol per solute is whole-protein-unfolding scale, not small-molecule")
    print("    dissolution. Needing it IS the structural conclusion, stated in other units.")
    p2 = plausible_max < 0.25

    # ---- [3] Robustness across baselines and pressures
    print("\n[3] ROBUSTNESS (P3) — max achievable release at |DeltaV| <= 30 cm3/mol")
    print(f"    {'baseline':>10s} {'max release (any P<=60MPa)':>28s}")
    ok3 = True
    for f0 in [0.01, 0.05, 0.10, 0.20]:
        best = max(released_fraction(f0, dV, P) for dV in (-5, -10, -20, -30) for P in PRESSURES)
        print(f"    {f0*100:9.0f}% {best*100:27.1f}%")
        if best >= TARGET_RELEASE:
            ok3 = False

    # ---- [4] Verdict
    print("\n" + "=" * 78)
    print("SELF-CHECKS")
    for name, ok in [("P1 required DeltaV exceeds the small-organic range (>30 cm3/mol) even in the most generous corner", p1),
                     ("P2 plausible DeltaV gives only a small shift (<25%)", p2),
                     ("P3 conclusion robust across baselines 1-20% and P up to 60 MPa", ok3)]:
        print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

    print("""
CONCLUSION (what this does and does not show)
---------------------------------------------
It does NOT dispute the measurement — that is an experiment, and ~50% release is what they
observed. What it shows is that the *intuitive* reading of it is wrong: equilibrium
molecular solubility cannot deliver a release of that size at 20-60 MPa. You would need a
volume change per solute of ~53 cm3/mol even in the most generous corner (a high 20%
baseline release AND the deepest 60 MPa), and ~112-337 cm3/mol at a realistic 5% baseline
— against 5-30 cm3/mol for small-organic dissolution. Pressure at deep-sea magnitudes is
simply not a strong lever on molecular solubility.

So the mechanism has to be STRUCTURAL, and the "giant juicer" metaphor is closer to right
than the solubility intuition: cell lysis / membrane failure, or a cooperative volume-phase
transition of the TEP-polysaccharide gel matrix. Note the consistency — a *cooperative*
transition can carry a large effective DeltaV precisely because many monomers move
together, which is another way of saying the effect is structural rather than molecular.
Two supporting observations point the same way: nitrogen is released in *higher* proportion
than carbon (58-63% vs ~50%), which fits protein-rich cytoplasmic contents escaping rather
than bulk matrix dissolving; and the released material is described as labile proteins and
carbohydrates — cell contents, not a solubility-limited equilibrium pool.

⭐ A DISCRIMINATING PREDICTION (what would settle it)
-----------------------------------------------------
The two mechanisms differ in ways an experiment can separate:
  * Equilibrium partitioning  -> release is REVERSIBLE on decompression, and scales
                                 smoothly (log-linearly) with pressure, with no threshold.
  * Structural failure        -> release is largely IRREVERSIBLE, plausibly THRESHOLD-like
                                 (little below some depth-equivalent, then a sharp onset),
                                 and should track cell integrity / viability, not solute
                                 chemistry.
So: decompress and see whether the DOM goes back in. This analysis predicts it does not.

HONEST LIMITS
-------------
Idealised two-phase partition model with a single lumped DeltaV; real marine snow is a
heterogeneous porous gel with a distribution of solutes and binding environments. I have
read the abstract and press coverage, NOT the full paper — it is entirely possible the
authors already state the mechanism is structural, in which case this confirms rather than
corrects, and the value is the quantitative bound plus the reversibility test. The
argument is a bound on the equilibrium channel, not a complete mechanism.
""")
    print("=" * 78)


if __name__ == "__main__":
    main()
