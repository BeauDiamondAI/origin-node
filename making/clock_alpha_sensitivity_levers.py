"""
Making #17 — Are constants constant? Which lever actually buys the answer.
==========================================================================

THE SETTING
-----------
Optical clocks now reach extraordinary precision — NIST reports clock frequency RATIOS with
fractional uncertainty <= 3.2e-18 (2026), and an Al+ clock with 1.6e-18 systematic
uncertainty. One headline use is testing whether the fine-structure constant alpha is
actually constant: if alpha drifts, different atomic transitions shift by DIFFERENT
amounts, so the RATIO of two clocks drifts even though each clock is "correct".

THE RELATION
------------
Each clock transition has a dimensionless alpha-sensitivity K (the fractional sensitivity;
distinct from the dimensional q coefficients — see arXiv:1807.08337 on the two conventions).
For a ratio R = nu_A / nu_B,

    d(ln R)/dt = (K_A - K_B) * d(ln alpha)/dt        =>      alpha_dot/alpha = (dlnR/dt) / dK

so a campaign of duration T that pins the ratio to fractional uncertainty sigma_R bounds

    |alpha_dot/alpha|  ~  sigma_R / (dK * T)              [per year, with T in years]

THE QUESTION THIS MAKING ASKS
------------------------------
Three levers sit in that formula and they are NOT interchangeable:
  * sigma_R — clock precision. ENGINEERING. Improves steadily with effort and money.
  * T       — campaign baseline. PATIENCE. Linear, and you cannot rush it.
  * dK      — the sensitivity DIFFERENCE between the two transitions. ATOMIC STRUCTURE.
              Fixed the moment you choose which two species to compare. No amount of
              laboratory skill changes the K of a given transition.
Which one is actually binding? The intuition worth testing is that precision is the thing
everyone quotes, but dK may dominate — and unlike the other two, you cannot buy it.

SOURCING DISCIPLINE (important — these are exactly the numbers I must not recite)
---------------------------------------------------------------------------------
VERIFIED and used: a proposed neutral-Yb clock transition (4f14 6s6p 3P0 -> 4f13 6s2 5d,
J=2) has K = -15, described as the highest sensitivity among current atomic clocks,
exceeding Yb+ E3 (Phys. Rev. Lett. 120, 173001). Highly charged ions such as Ho14+ are
proposed explicitly to push sensitivity higher (arXiv:1411.0775). Some clock species are
nearly alpha-INSENSITIVE (K near zero). Published bound for scale: alpha_dot/alpha =
-0.20(20) x 10^-16 /yr (Phys. Rev. Lett. 113, 210802).
NOT ASSERTED: individual K values for Yb+ E3/E2, Sr, Hg+, Al+ etc. I have not verified
them, so this making does NOT hardcode them. It works with the SPREAD of dK, which is what
the argument actually turns on, and treats specific pairings as clearly-labelled
illustrations rather than as sourced facts.

PRE-REGISTERED PREDICTIONS
--------------------------
  P1. Realistic dK values span at least two orders of magnitude (near-zero-sensitivity
      pairs up to |dK| ~ 15 for the best proposed pairing).
  P2. Therefore, at FIXED precision and baseline, the choice of clock pair moves the
      alpha-drift bound by >= 100x — comparable to or larger than a decade of precision
      progress.
  P3. Buying that same factor through precision alone takes ~a decade or more at
      historical rates of optical-clock improvement, and the conclusion is robust across
      any plausible assumed rate.

Run: python3 clock_alpha_sensitivity_levers.py
Pure stdlib.
"""

# --- anchors (see sourcing note above)
SIGMA_MODERN = 3.2e-18      # NIST 2026 clock frequency ratio uncertainty
SIGMA_2014 = 3e-16          # era of the Yb+ E3/E2 ratio measurement
PUBLISHED_BOUND = 2.0e-17   # |alpha_dot/alpha| /yr, PRL 113 210802 (value 0.20(20)e-16)
K_BEST = 15.0               # |K| of the best proposed transition (neutral Yb, PRL 120 173001)


def bound(sigma_R, dK, T_years):
    """Implied |alpha_dot/alpha| per year."""
    return sigma_R / (dK * T_years)


def main():
    print("=" * 78)
    print("Making #17 — three levers on 'is alpha constant?', and only two are purchasable")
    print("=" * 78)

    # ---- [1] the spread of dK
    print("\n[1] THE SPREAD OF dK (P1) — illustrative pairings, |dK|")
    pairs = [
        ("two low-sensitivity clocks (both K near zero)",        0.05),
        ("a low-sensitivity pair, modest difference",            0.5),
        ("a conventional sensitive/insensitive pairing",         3.0),
        ("a strongly sensitive transition vs an insensitive one", 6.0),
        ("best proposed pairing (neutral-Yb K=-15 vs K~0)",     K_BEST),
    ]
    for name, dK in pairs:
        print(f"    {name:52s} |dK| = {dK:6.2f}")
    spread = pairs[-1][1] / pairs[0][1]
    print(f"\n    spread across this range: {spread:.0f}x")
    p1 = spread >= 100

    # ---- [2] what that does to the bound, at fixed precision and baseline
    T = 1.0
    print(f"\n[2] BOUND AT FIXED PRECISION (sigma_R = {SIGMA_MODERN:.1e}) AND T = {T:.0f} yr (P2)")
    print(f"    {'pairing':52s} {'|alpha_dot/alpha| /yr':>22s}")
    vals = []
    for name, dK in pairs:
        b = bound(SIGMA_MODERN, dK, T)
        vals.append(b)
        print(f"    {name:52s} {b:22.2e}")
    ratio = vals[0] / vals[-1]
    print(f"\n    worst pairing is {ratio:.0f}x weaker than the best — from ATOMIC STRUCTURE alone,")
    print("    with identical clocks, identical baseline, identical laboratory skill.")
    p2 = ratio >= 100

    # ---- [3] can precision buy it back?
    print("\n[3] CAN PRECISION BUY THAT BACK? (P3)")
    gain_precision = SIGMA_2014 / SIGMA_MODERN
    print(f"    precision progress from ~{SIGMA_2014:.0e} to {SIGMA_MODERN:.1e} = {gain_precision:.0f}x")
    print(f"    the dK spread above                                   = {spread:.0f}x")
    print("\n    years of precision progress needed to match the dK spread,")
    print("    under different assumed historical rates:")
    ok3 = True
    import math
    for per_decade in [10.0, 30.0, 100.0]:
        years = 10.0 * math.log10(spread) / math.log10(per_decade)
        flag = "" if years >= 8 else "   <- would undercut P3"
        if years < 8:
            ok3 = False
        print(f"      at {per_decade:5.0f}x per decade -> {years:5.1f} years{flag}")

    # ---- [4] sanity check against a published bound
    print("\n[4] SANITY CHECK — does the relation reproduce a published bound's scale?")
    print(f"    published: |alpha_dot/alpha| ~ {PUBLISHED_BOUND:.0e} /yr (PRL 113, 210802)")
    for dK, T_yr in [(6.0, 1.0), (6.0, 3.0), (3.0, 1.0)]:
        b = bound(SIGMA_2014, dK, T_yr)
        print(f"      sigma_R={SIGMA_2014:.0e}, |dK|={dK:4.1f}, T={T_yr:.0f} yr -> {b:.1e} /yr"
              f"   ({b/PUBLISHED_BOUND:5.1f}x the published value)")
    print("    Order-of-magnitude agreement is the check being made here — not a")
    print("    reproduction. The published analyses combine several clock pairs and")
    print("    handle mu-variation jointly, which this one-line relation does not.")

    print("\n" + "=" * 78)
    print("SELF-CHECKS")
    for name, ok in [("P1 dK spans >= 2 orders of magnitude", p1),
                     ("P2 pair choice moves the bound >= 100x at fixed precision", p2),
                     ("P3 matching that by precision alone costs ~a decade+", ok3)]:
        print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

    print("""
WHAT THIS SAYS
--------------
The number everyone quotes about a clock is sigma_R, and it is the lever that responds to
effort. But in the alpha-drift bound, dK enters on exactly equal footing — and dK is not
purchasable. It is fixed by the atomic structure of whichever two transitions you chose to
compare. Two laboratories with identical world-record clocks, running identical campaigns,
can differ by more than 100x in what they can say about alpha, purely from that choice.

So "build a better clock" and "test fundamental physics better" are related but distinctly
NOT the same project, and conflating them misallocates effort: past a point, the binding
constraint is atomic structure, not engineering.

A PREDICTION, AND THE FIELD ALREADY MAKES IT
--------------------------------------------
If this framing is right, the field should be visibly chasing dK rather than only sigma_R —
investing in exotic, hard-to-operate systems whose only advantage is a large K. It is:
highly charged ions such as Ho14+ are proposed specifically for alpha sensitivity
(arXiv:1411.0775), and the neutral-Yb 4f13 5d transition (K = -15) is advertised precisely
as the highest-sensitivity option (PRL 120, 173001) despite being far harder to realise
than the well-established Sr and Yb lattice clocks. Chasing a harder system for a better
coefficient only makes sense if the coefficient is a first-class lever. Same corroboration
shape as making #16, where the developer's own remedy (deeper + more laterals) was exactly
the two levers a conduction-limited flux leaves.

HONEST LIMITS
-------------
A one-line scaling relation, not an analysis. Real bounds fit drifts across MANY clock
pairs simultaneously, treat alpha and the electron-proton mass ratio mu jointly (microwave
references bring in mu), and must model systematic drift, not just statistical uncertainty.
The illustrative |dK| values in [1] are labelled illustrations, NOT sourced measurements —
only K = -15 and 'some clocks are near-zero' are sourced. T enters linearly here, which
ignores that long campaigns also accumulate systematic risk.
""")
    print("=" * 78)


if __name__ == "__main__":
    main()
