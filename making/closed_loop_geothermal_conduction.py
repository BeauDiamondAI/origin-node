"""
Making #16 — Closed-loop geothermal: is the rock's heat a STOCK problem or a FLUX problem?
===========================================================================================

THE CLAIM UNDER TEST
--------------------
Eavor-Loop, Geretsried (Bavaria) — the first commercial-scale closed-loop ("advanced")
geothermal system. Unlike EGS, it does NOT fracture the rock or produce reservoir fluid:
a sealed working fluid circulates through a multilateral "radiator" and picks up heat by
CONDUCTION alone. That is the whole selling point ("geothermal anywhere", no permeability
needed) — and it is also exactly what makes it magnitude-checkable, because conduction
through rock is slow and well-characterised.

Reported specs (NOTE: sources disagree — carried through as a range):
  * depth              ~4.2-4.5 km vertical
  * laterals           12 laterals x ~2.7 km  (EIB environmental data sheet)  => ~32 km
                       up to ~42 km implied by a drilling-trade description
  * thermal output     59 MWth (EIB) / ~64 MWth (Eavor project page)
  * electrical output  ~8-8.2 MWe
  * surface fluid      up to ~160 C

THE QUESTION
------------
Can conduction into ~32-42 km of borehole sustain ~60 MW thermal? Two DIFFERENT bounds
answer two different questions, and the distinction is the point of this making:

  (A) STOCK bound  — is there enough heat in the rock the loop can reach?
      Thermal diffusion length over time t is ~sqrt(4*alpha*t). Take the cylinder of rock
      within that radius of the borehole and ask how much sensible heat it holds.
      This is a generous UPPER bound: it assumes the whole cylinder is drawn down.

  (B) FLUX bound   — can conduction DELIVER heat fast enough?
      Classic transient line-source result for a borehole at fixed wall temperature:

          q'(t) = 4*pi*k*dT / ( ln(4*alpha*t/rb^2) - gamma )        [W per metre]

      This is the physics that actually governs, and it is only logarithmically sensitive
      to time — which is why conduction limits do not "go away" if you wait.

PRE-REGISTERED PREDICTIONS (written before computing)
------------------------------------------------------
  P1. The STOCK bound comfortably exceeds the claim — the rock holds plenty of heat.
  P2. The FLUX bound falls well SHORT of the claimed sustained output (I expect several-fold).
  P3. The shortfall is robust: it survives generous choices of conductivity, temperature
      difference, borehole radius, and lateral length, and does not disappear at early times
      (the ln(t) dependence is weak).

If P1 and P2 both hold, the honest conclusion is NOT "the project is impossible" — it is
that the binding constraint is a RATE, not a RESERVE, and that a claimed sustained output
well above the flux bound must be explained by something (initial-transient output, a
different definition of MWth, longer laterals than reported, or a mechanism beyond pure
conduction). That is a question to take to the literature, not to settle by assertion.

Run: python3 closed_loop_geothermal_conduction.py
Pure stdlib.
"""

import math

GAMMA = 0.5772156649

# --- rock properties (granite / crystalline basement)
K_ROCK = 2.8          # W/(m K), thermal conductivity
RHO_C = 2.12e6        # J/(m^3 K)  (~2650 kg/m3 * ~800 J/kg/K)
ALPHA = K_ROCK / RHO_C

# --- geometry / operating point
R_BORE = 0.11         # m, borehole radius
L_TOTAL = 32_400.0    # m of lateral (12 x 2.7 km, EIB sheet)
YEARS = 30.0
SEC_PER_YR = 3.156e7

# --- temperatures
T_ROCK = 170.0        # C at ~4.5 km (Molasse basin gradient); Eavor cites 160 C at surface
T_FLUID_MEAN = 90.0   # C, mean working-fluid temperature along the loop
DT = T_ROCK - T_FLUID_MEAN

CLAIM_MWTH = 59.0     # EIB figure; Eavor page says ~64


def flux_per_metre(dT=DT, k=K_ROCK, t_years=YEARS, rb=R_BORE, alpha=ALPHA):
    """Transient line-source heat extraction rate, W per metre of borehole."""
    t = t_years * SEC_PER_YR
    return 4.0 * math.pi * k * dT / (math.log(4.0 * alpha * t / rb**2) - GAMMA)


def stock_power(dT_used, L=L_TOTAL, t_years=YEARS, alpha=ALPHA, rho_c=RHO_C):
    """Generous upper bound: fully deplete the diffusion cylinder by dT_used, over t."""
    t = t_years * SEC_PER_YR
    r_pen = math.sqrt(4.0 * alpha * t)
    volume = math.pi * r_pen**2 * L
    return volume * rho_c * dT_used / t, r_pen


def main():
    print("=" * 78)
    print("Making #16 — closed-loop geothermal: stock vs flux")
    print(f"rock k={K_ROCK} W/mK, alpha={ALPHA:.2e} m^2/s, laterals={L_TOTAL/1000:.1f} km,"
          f" rock {T_ROCK}C, fluid {T_FLUID_MEAN}C (dT={DT}K)")
    print(f"claim under test: {CLAIM_MWTH} MWth sustained")
    print("=" * 78)

    # ---- [A] STOCK
    print("\n[A] STOCK BOUND (P1) — is there enough heat within diffusion reach?")
    for dT_used in [40, 60, 80]:
        P, r_pen = stock_power(dT_used)
        print(f"    draw down the reachable cylinder by {dT_used:3d} K -> r_pen ="
              f" {r_pen:5.1f} m, P = {P/1e6:7.1f} MW")
    P_stock, r_pen = stock_power(60)
    p1 = P_stock / 1e6 >= CLAIM_MWTH

    # ---- [B] FLUX
    print("\n[B] FLUX BOUND (P2) — can conduction deliver it fast enough?")
    q = flux_per_metre()
    print(f"    q' at {YEARS:.0f} yr, dT={DT:.0f} K : {q:6.1f} W/m")
    print(f"    total over {L_TOTAL/1000:.1f} km of lateral : {q*L_TOTAL/1e6:6.2f} MW")
    print(f"    ratio to claim : {q*L_TOTAL/1e6/CLAIM_MWTH:.2f}x")
    print(f"    (sanity check vs shallow ground-source practice: {q/DT:.2f} W/m per K of dT;")
    print(f"     shallow borehole exchangers run ~50 W/m at dT~15 K = ~3.3 W/m/K)")
    p2 = q * L_TOTAL / 1e6 < CLAIM_MWTH

    # ---- required length
    need_L = CLAIM_MWTH * 1e6 / q
    print(f"\n    lateral length required to reach {CLAIM_MWTH} MW at this q':"
          f" {need_L/1000:.0f} km  ({need_L/L_TOTAL:.1f}x reported)")

    # ---- [C] SENSITIVITY
    print("\n[C] ROBUSTNESS (P3) — generous parameter choices, MW delivered")
    print(f"    {'k':>5s} {'dT':>5s} {'rb':>6s} {'yrs':>5s} {'L km':>7s} {'MW':>8s} {'x claim':>8s}")
    ok3 = True
    rows = [
        (2.8,  80, 0.11, 30, 32.4),
        (3.5, 100, 0.11, 30, 32.4),   # higher-k rock, colder fluid
        (3.5, 120, 0.15, 30, 42.0),   # generous everything + long laterals
        (5.0, 130, 0.15, 30, 42.0),   # implausibly conductive rock
        (2.8,  80, 0.11,  1, 32.4),   # first year (transient is only log-better)
        (3.5, 120, 0.15,  1, 42.0),   # generous AND first year
    ]
    best_ratio = 0.0
    for k, dT, rb, yr, Lkm in rows:
        qq = flux_per_metre(dT=dT, k=k, t_years=yr, rb=rb)
        MW = qq * Lkm * 1000 / 1e6
        ratio = MW / CLAIM_MWTH
        best_ratio = max(best_ratio, ratio)
        print(f"    {k:5.1f} {dT:5.0f} {rb:6.2f} {yr:5.0f} {Lkm:7.1f} {MW:8.1f} {ratio:8.2f}")
        if ratio >= 1.0:
            ok3 = False
    print(f"\n    best case anywhere in this table reaches {best_ratio*100:.0f}% of the claim")

    print("\n" + "=" * 78)
    print("SELF-CHECKS")
    for name, ok in [("P1 stock bound comfortably exceeds the claim (heat IS there)", p1),
                     ("P2 flux bound falls short of the claimed sustained output", p2),
                     ("P3 shortfall survives generous parameters and early times", ok3)]:
        print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

    print(f"""
READING THE RESULT
------------------
If P1 and P2 both hold, the two bounds are answering different questions and the pair is
the finding: the rock within diffusion reach holds ENOUGH ENERGY, but conduction cannot
MOVE it fast enough. Stock is fine; flux is binding. That is why closed-loop designs need
tens of kilometres of lateral — they are buying surface area, because area is the only
lever on a conduction-limited flux (the ln(t) term means patience buys almost nothing).

What a shortfall would and would NOT license concluding:
  * NOT "the project cannot work" — I am using public spec-sheet numbers that already
    disagree with each other (59 vs 64 MWth; ~32 vs ~42 km of lateral), and a nameplate
    figure may be initial output rather than 30-year sustained output.
  * It WOULD mean the claimed figure needs an explanation beyond steady conduction:
    initial-transient output, a different MWth accounting, longer laterals than reported,
    or some non-conductive contribution.
  * The honest next step is the literature, not assertion: conduction-limited performance
    of closed-loop vs EGS is an actively argued question and I should not present a
    textbook line-source calculation as though it were news.

HONEST LIMITS
-------------
Single isolated line source: real multilaterals INTERFERE thermally, which makes the flux
bound optimistic, not conservative. Constant borehole-wall temperature (real systems have a
fluid temperature rising along the loop). No wellbore hydraulics, no pumping parasitics,
no topping cycle. Rock temperature inferred from a typical basin gradient, not measured.
""")
    print("=" * 78)
    print(POSTSCRIPT)


POSTSCRIPT = """
POSTSCRIPT — LITERATURE CHECK, RUN BEFORE CLAIMING ANYTHING (2026-07-28)
========================================================================
The script above says the honest next step is the literature rather than assertion. I ran
it, and it changes the framing in three ways.

1. THE CONCLUSION IS NOT NOVEL — it is a published, actively-argued critique.
   * "Technical barriers for deep closed-loop geothermal" (arXiv 2303.12689): purely
     conductive closed-loop designs yield very low power per unit length; proposals to
     overcome it by depth and lateral length do not rescue the economics.
   * "On the limitations of closed-loop geothermal systems for electricity generation
     outside high[-gradient settings]" (Nature Comms Engineering, s44172-025-00458-7):
     high lateral flow rates rapidly cool the surrounding matrix; mitigation needs many
     multilateral boreholes.
   * A GRC feasibility study: closed-loop heat-exchanger designs give "very low energy
     production per foot of drilled wellbore."
   * Plus techno-economic treatments (Renewable Energy S096014812200012X; ETH
     ethz-b-000467172).
   So this making REPRODUCES a documented result. No novelty is claimed — the value is
   tangibility plus an independent check, exactly as in makings #8 and #10.

2. IT VALIDATES WELL AGAINST EAVOR'S OWN COMMISSIONED MODEL.
   Beckers' techno-economic modelling of Eavor-Loop 2.0 (hosted on eavor.com): 7.5 km
   depth, 12 laterals, >90 km total downhole length, 30-yr average reservoir ~125 C (low
   gradient) / ~210 C (high), giving ~22 MWth and ~51 MWth respectively.
   Normalising: Beckers' high-gradient case is ~0.57 MWth per km of lateral at dT ~150 K
   => ~0.38 MWth/km per 100 K. My line-source bound gives 0.23 MWth/km at dT = 80 K
   => ~0.28 MWth/km per 100 K. Same order, mine ~35% more conservative. For a textbook
   line-source estimate against a full reservoir simulation, that is a good agreement.
   The corollary matters more: Eavor's own modelling needs >90 km of lateral to reach
   ~51 MWth AT A HIGH GRADIENT. Geretsried reports ~32 km of lateral at a moderate
   Molasse-basin gradient while carrying a 59-64 MWth nameplate. Those are hard to
   reconcile, and the tension is visible entirely within the developer's own numbers.

3. THE FIELD RESULT IS IN, AND IT IS BRUTAL — BUT NOT CLEANLY ATTRIBUTABLE TO CONDUCTION.
   Per GeoExpro, Eavor has stepped back from the operator role at Geretsried. Only 1 of 4
   planned injector-producer pairs is complete; 6 of 12 horizontal loops built; only 3-4
   loops actually contributing flow, with 2 clogged by rock fragments. Reported output:
   gross ~0.5-1 MWe against plant parasitic demand ~0.5 MWe — i.e. roughly ZERO net
   electricity, against an 8.2 MWe nameplate.
   IMPORTANT: the proximate causes reported are construction and completion problems
   (partial build-out, clogging), NOT the conduction limit. I cannot disentangle the two
   from public information, and I will not claim this calculation "predicted" the outcome.
   What is fair to say: my full-design flux bound (~7.4 MWth, i.e. ~0.7-1.0 MWe at ORC
   efficiencies typical of these temperatures) sits in the same order as the OBSERVED
   gross output, whereas the 8.2 MWe nameplate does not — and that ordering would hold
   even if every loop had been drilled and none had clogged.
"""


if __name__ == "__main__":
    main()
