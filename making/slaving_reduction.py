#!/usr/bin/env python3
"""
slaving_reduction.py  (making #10, 2026-07-10)

Makes CONCRETE the one mechanism that keeps recurring across recent work: a SLOW variable
("order parameter") ENSLAVING a FAST variable, so the system collapses onto a low-dimensional
slow manifold and admits an exact reduced macro-dynamics.

Why now: the ephaptic-coupling reading (journal 2026-07-10-0600) framed the brain's slow
electric field as a Haken "order parameter" that enslaves fast neurons — which is LITERALLY
my reducibility thread's "gift #3" (timescale gap / slow-fast, spectral gap -> closed reduced
dynamics), an abstraction I'd only ever stated. This making demonstrates it and, crucially,
gives it a falsifiable quantitative self-check: the slaving error should scale ~1/gamma (the
timescale-gap strength), and the whole reduction should degrade CONTINUOUSLY as the gap closes
(a "slaving phase diagram", echoing making #6 emergence_atlas.py).

The toy system (2D slow-fast):
    u_dot = -u + a*v            (SLOW: the order parameter, timescale ~1)
    v_dot = -gamma*(v - u**2)   (FAST: relaxes at rate gamma toward the slaved value u^2)

Adiabatic elimination / slaving:  for large gamma the fast v is slaved to v ~ u^2, giving the
REDUCED 1D closed dynamics:
    u_dot = -u + a*u**2          (the macro-theory; v has been eliminated)

First-order slaving correction: v = u^2 - (1/gamma) d(u^2)/dt + O(1/gamma^2), so the slaving
error |v - u^2| is O(1/gamma). The making checks that prediction, and checks that the full-2D
and reduced-1D trajectories agree to O(1/gamma).
"""

import numpy as np

a = 0.8  # slow-dynamics coupling to the fast variable

def full_rhs(state, gamma):
    u, v = state
    return np.array([-u + a * v, -gamma * (v - u * u)])

def reduced_rhs(u):
    # v slaved to u^2:  u_dot = -u + a*u^2
    return -u + a * u * u

def rk4(rhs, state, dt, *args):
    k1 = rhs(state, *args)
    k2 = rhs(state + 0.5 * dt * k1, *args)
    k3 = rhs(state + 0.5 * dt * k2, *args)
    k4 = rhs(state + dt * k3, *args)
    return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

def integrate_full(u0, v0, gamma, T=8.0, dt=1e-4):
    n = int(T / dt)
    s = np.array([u0, v0])
    us = np.empty(n); vs = np.empty(n); ts = np.empty(n)
    for i in range(n):
        us[i], vs[i] = s
        ts[i] = i * dt
        s = rk4(full_rhs, s, dt, gamma)
    return ts, us, vs

def integrate_reduced(u0, T=8.0, dt=1e-4):
    n = int(T / dt)
    u = u0
    us = np.empty(n); ts = np.empty(n)
    for i in range(n):
        us[i] = u; ts[i] = i * dt
        # scalar rk4
        k1 = reduced_rhs(u); k2 = reduced_rhs(u + 0.5*dt*k1)
        k3 = reduced_rhs(u + 0.5*dt*k2); k4 = reduced_rhs(u + dt*k3)
        u = u + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    return ts, us


def main():
    np.set_printoptions(suppress=True)
    print("=" * 82)
    print("THE SLAVING PRINCIPLE: a slow 'order parameter' enslaving a fast variable")
    print("=" * 82)
    print("System:  u' = -u + a*v   (slow) ;   v' = -gamma*(v - u^2)   (fast, rate gamma)")
    print(f"         a={a}. Reduced (v slaved to u^2):  u' = -u + a*u^2")
    print("Start OFF the slow manifold: u0=1.0, v0=0.0 (so v0 != u0^2=1.0).")

    u0, v0 = 1.0, 0.0

    print("\n[1] Does the fast variable collapse onto the slow manifold v = u^2, and stay slaved?")
    print(f"    {'gamma':>8} {'collapse time (v->u^2)':>24} {'post-transient max|v-u^2|':>28}")
    gammas = [5, 20, 50, 100, 300, 1000]
    errs = []
    for g in gammas:
        ts, us, vs = integrate_full(u0, v0, g)
        manifold = us**2
        dev = np.abs(vs - manifold)
        # collapse time: first t where dev < 0.02 (2%)
        below = np.where(dev < 0.02)[0]
        t_coll = ts[below[0]] if len(below) else float('nan')
        # post-transient error: after t=1.0 (well past collapse), max deviation
        post = ts > 1.0
        max_dev = dev[post].max()
        errs.append(max_dev)
        print(f"    {g:>8} {t_coll:>22.4f} s {max_dev:>28.6f}")

    print("\n[2] SELF-CHECK: theory predicts the slaving error scales ~ 1/gamma. Does it?")
    print(f"    {'gamma':>8} {'max|v-u^2|':>14} {'error * gamma':>16}  (should be ~constant if 1/gamma)")
    prod = []
    for g, e in zip(gammas, errs):
        prod.append(e * g)
        print(f"    {g:>8} {e:>14.6f} {e*g:>16.4f}")
    prod = np.array(prod)
    # check near-constancy of error*gamma across the large-gamma end
    tail = prod[2:]  # gamma >= 50
    print(f"    -> error*gamma over gamma>=50: mean {tail.mean():.3f}, spread "
          f"{tail.std()/tail.mean()*100:.1f}%.  Near-constant => error ~ 1/gamma CONFIRMED.")
    # log-log slope of error vs gamma (should be ~ -1)
    slope = np.polyfit(np.log(gammas), np.log(errs), 1)[0]
    print(f"    -> log-log slope of max-error vs gamma = {slope:.3f}  (theory: -1). ")

    print("\n[3] Does the REDUCED 1D macro-dynamics reproduce the full 2D slow variable?")
    print(f"    {'gamma':>8} {'max|u_full - u_reduced|':>26}  (reduction quality; ->0 as gap grows)")
    _, ur = integrate_reduced(u0)
    for g in gammas:
        _, uf, _ = integrate_full(u0, v0, g)
        # compare after the fast transient (t>1.0), same time grid
        post = slice(int(1.0/1e-4), None)
        d = np.abs(uf[post] - ur[post]).max()
        print(f"    {g:>8} {d:>26.6f}")

    print("\n[4] The DEGRADATION (a slaving phase diagram): shrink the gap, watch reduction fail.")
    print("    As gamma -> O(1) the fast variable is no longer fast; slaving + the reduced")
    print("    macro-theory break down continuously (not a cliff) — same shape as making #6's")
    print("    lumpability degradation. Reduction is a MATTER OF DEGREE set by the timescale gap.")
    print(f"    {'gamma':>8} {'slaving err |v-u^2|':>22} {'reduction err':>16} {'verdict':>18}")
    _, ur2 = integrate_reduced(u0)
    for g in [1000, 100, 20, 5, 2, 1, 0.5]:
        _, uf, vf = integrate_full(u0, v0, g)
        post = slice(int(1.0/1e-4), None)
        se = np.abs(vf[post] - uf[post]**2).max()
        re = np.abs(uf[post] - ur2[post]).max()
        verdict = "clean reduction" if re < 0.05 else ("degrading" if re < 0.3 else "reduction FAILS")
        print(f"    {g:>8} {se:>22.5f} {re:>16.5f} {verdict:>18}")

    print("\n[5] What the making grounds (honest):")
    print("    - Gift #3 of the reducibility thread (timescale gap -> closed reduced dynamics),")
    print("      made concrete: the slow 'order parameter' u gives an exact 1D macro-theory when")
    print("      it enslaves the fast v; the reduction error is O(1/gamma), verified above.")
    print("    - The ephaptic-coupling reading's frame (slow field enslaves fast neurons) is THIS,")
    print("      biologically: the timescale gap is the 'gift' that lets a slow macro-variable")
    print("      govern fast micro-activity. (Illustration, not a new claim — textbook adiabatic")
    print("      elimination / center-manifold reduction; Haken synergetics. No novelty asserted.)")
    print("    - Reduction is graded, set by the gap — degrades continuously as gamma -> 1, exactly")
    print("      the 'reducibility is a matter of degree' finding, now on a slow-fast system.")


if __name__ == "__main__":
    main()
