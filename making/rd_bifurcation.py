"""
Gray-Scott bifurcation analysis (2026-06-18/19) — making/ entry #4: does the
empirical morphogenesis map (entry #2) match the analytical theory (entry #3)?

This is the loop-closer. Entry #2 *observed* three bands (flood / structured / death);
entry #3 *read* the theory (patterns near a bifurcation threshold). Here I *derive*
the threshold for my own parameters and overlay it on my actual coverage data.

Reaction-only steady states (no diffusion) of
    u̇ = -u v² + F(1-u)
    v̇ =  u v² - (F+k) v
From v̇=0: v=0 (trivial u=1,v=0) OR u v = F+k.  Substituting into u̇=0 gives
    (F+k) v² - F v + F(F+k) = 0
so nontrivial fixed points are real iff the discriminant ≥ 0:
    F² - 4 F (F+k)² ≥ 0   ⟺   F ≥ 4 (F+k)²      ← the SADDLE-NODE / FOLD curve.
(This is exactly the Frankfurt source's "F=4(F+k)²" — which I'd wrongly suspected
was garbled. It isn't; it's the fold. Self-correction logged.)

Turing (diffusion-driven) instability of a reaction-stable fixed point, with the
Jacobian J = [[-v²-F, -2uv], [v², 2uv-(F+k)]] and Du>Dv (mcb111 conditions):
    reaction-stable:  Tr(J) < 0  and  det(J) > 0
    diffusion destabilises:  Dv·Juu + Du·Jvv > 0
                         and (Dv·Juu + Du·Jvv)² > 4·Du·Dv·det(J)
"""
import numpy as np

Du, Dv = 0.16, 0.08   # same as the simulations

def nontrivial_fps(F, k):
    s = F + k
    disc = F*F - 4*F*s*s
    if disc < 0:
        return []                      # only the trivial FP exists -> "death"
    r = np.sqrt(disc)
    out = []
    for v in ((F + r) / (2*s), (F - r) / (2*s)):
        if v > 1e-9:
            out.append((s / v, v))     # u = (F+k)/v
    return out

def jacobian(u, v, F, k):
    return np.array([[-v*v - F, -2*u*v],
                     [ v*v,      2*u*v - (F + k)]])

def classify(F, k):
    fps = nontrivial_fps(F, k)
    if not fps:
        return "death"                 # trivial state only
    turing = False
    react_stable_any = False
    for (u, v) in fps:
        J = jacobian(u, v, F, k)
        tr, det = J[0,0] + J[1,1], J[0,0]*J[1,1] - J[0,1]*J[1,0]
        if tr < 0 and det > 0:         # stable without diffusion
            react_stable_any = True
            h = Dv*J[0,0] + Du*J[1,1]
            if h > 0 and h*h > 4*Du*Dv*det:
                turing = True
    if turing:
        return "PATTERN"               # Turing-unstable -> stationary patterns
    if react_stable_any:
        return "homog"                 # nontrivial stable, no Turing -> uniform fill
    return "osc/other"                 # reaction-unstable (Hopf etc.)

if __name__ == "__main__":
    # the exact (F,k) grid of the empirical map (rd_parameter_map.py), with the
    # observed V>0.2 coverage pasted from that run for side-by-side comparison.
    F_vals = np.linspace(0.018, 0.062, 6)
    K_vals = np.linspace(0.049, 0.067, 6)
    coverage = {  # (row k-index, col F-index) -> empirical V>0.2 fraction
        (0,0):.276,(0,1):1.0,(0,2):1.0,(0,3):1.0,(0,4):1.0,(0,5):1.0,
        (1,0):.219,(1,1):.679,(1,2):1.0,(1,3):1.0,(1,4):1.0,(1,5):1.0,
        (2,0):.199,(2,1):.419,(2,2):1.0,(2,3):1.0,(2,4):1.0,(2,5):1.0,
        (3,0):.069,(3,1):.253,(3,2):.442,(3,3):.642,(3,4):.994,(3,5):.533,
        (4,0):.000,(4,1):.020,(4,2):.028,(4,3):.030,(4,4):.030,(4,5):.031,
        (5,0):.000,(5,1):.000,(5,2):.023,(5,3):.023,(5,4):.020,(5,5):.003,
    }
    print(f"{'':6}" + "".join(f"F={F:.3f} " for F in F_vals))
    for i, k in enumerate(K_vals):
        cells = []
        for j, F in enumerate(F_vals):
            c = classify(float(F), float(k))
            cov = coverage[(i,j)]
            tag = {"death":"·death ", "PATTERN":"#PATT  ", "homog":"=flood ", "osc/other":"~osc   "}[c]
            cells.append(f"{tag}")
        print(f"k={k:.3f} " + "".join(cells))
    print()
    print("empirical coverage (V>0.2), same grid:")
    print(f"{'':6}" + "".join(f"F={F:.3f} " for F in F_vals))
    for i, k in enumerate(K_vals):
        print(f"k={k:.3f} " + "".join(f"{coverage[(i,j)]*100:5.0f}%  " for j in range(6)))
    # fold curve check at a few points
    print("\nfold check  F >= 4(F+k)^2 :")
    for (F,k) in [(0.030,0.060),(0.018,0.067),(0.062,0.049),(0.044,0.067)]:
        print(f"  F={F:.3f} k={k:.3f}: 4(F+k)^2={4*(F+k)**2:.4f}  -> nontrivial FP exists: {F >= 4*(F+k)**2}")
