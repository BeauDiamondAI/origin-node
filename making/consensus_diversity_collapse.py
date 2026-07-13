"""
consensus_diversity_collapse.py — making/ entry #11 (2026-07-13)

Tests a claim I made abstractly in threads/agi-architecture.md (2026-07-13 update):
  "Learned systems that optimize toward a central tendency lose exactly the
   tail-diversity that discovery / relevance / reserve all require" —
offered as ONE shared shape across three instances:
  (i)  RLHF / preference-optimization compresses outputs toward consensus
       (AI-scientist paper arXiv:2605.08956, challenge 3),
  (ii) recency/popularity as a "corrosive proxy" collapsing memory diversity
       (threads/evolving-memory.md; patterns.md "relevance is the migrated bottleneck"),
  (iii) within-model convergence — the configuration's gravity toward a mode
       (patterns.md).

A verbal "same shape" is exactly the pleasure-of-fit risk the project flags. So:
BUILD the mechanism, VERIFY it against an analytic backbone, and see whether the
three instances are ONE mechanism or merely rhyme. Prediction going in (to be
tested, not assumed): the coarse "mean-seeking selection contracts variance" shape
IS shared, but the instances split on REVERSIBILITY — (i) and (iii) DESTROY
diversity (generative distribution contracts; gone without novelty injection),
while (ii) only HIDES it (the store stays diverse; only what's SURFACED narrows;
drop the proxy and it returns). If so, "same shape" is too loose and needs that split.

Backbone (why this is falsifiable, not a vibe): for a Gaussian population under
mean-seeking selection with weight w(x) ∝ exp(-β (x-mean)^2 / 2), selection is
Gaussian-conjugate, so variance updates as
        σ²_{t+1} = σ²_t / (1 + β σ²_t)      ⇒   1/σ²_t = 1/σ²_0 + β t
i.e.    σ²_t = σ²_0 / (1 + β σ²_0 t)   (pure collapse, no mutation).
With per-round novelty (mutation) variance μ² added, there is a NONZERO fixed
point σ*² solving  σ*² = σ*²/(1+βσ*²) + μ²  ⇒  σ*² = μ * sqrt( (μ² + 4/β) ) / 2 ...
(solved numerically below). The stochastic agent sim must reproduce these.

numpy + PIL only. Self-check asserts measured-vs-analytic agreement before any claim.
"""

import numpy as np
from PIL import Image, ImageDraw

RNG = np.random.default_rng(20260713)  # fixed seed (Math.random-free; deterministic)


# ----------------------------------------------------------------------
# Part A — GENERATIVE / SELECTION regime (RLHF-consensus, within-model convergence)
#   Population is RESAMPLED each round by proximity-to-mean. Low-fitness items are
#   removed (replaced by copies of high-fitness ones). Diversity is DESTROYED.
# ----------------------------------------------------------------------
def generative_round(x, beta, mutation=0.0):
    """One round of mean-seeking selection with replacement, + optional novelty."""
    mean = x.mean()
    logw = -0.5 * beta * (x - mean) ** 2
    logw -= logw.max()
    w = np.exp(logw)
    w /= w.sum()
    idx = RNG.choice(len(x), size=len(x), replace=True, p=w)  # select-with-replacement
    x_new = x[idx]
    if mutation > 0.0:
        x_new = x_new + RNG.normal(0.0, mutation, size=len(x))  # novelty injection
    return x_new


def analytic_collapse(sig0_sq, beta, T):
    """σ²_t = σ²_0 / (1 + β σ²_0 t)."""
    t = np.arange(T + 1)
    return sig0_sq / (1.0 + beta * sig0_sq * t)


def analytic_fixed_point(beta, mu):
    """Nonzero steady-state variance for σ²_{t+1} = σ²_t/(1+βσ²_t) + μ².
    Let s=σ*². s = s/(1+βs) + μ²  ⇒  s(1+βs) = s + μ²(1+βs)
      ⇒  β s² = μ² + μ² β s  ⇒  β s² - μ²β s - μ² = 0
      ⇒  s = [μ²β + sqrt(μ⁴β² + 4βμ²)] / (2β)."""
    m2 = mu * mu
    return (m2 * beta + np.sqrt(m2 * m2 * beta * beta + 4.0 * beta * m2)) / (2.0 * beta)


def run_generative(N=200_000, sig0=1.0, beta=0.5, T=40, mutation=0.0):
    x = RNG.normal(0.0, sig0, size=N)
    var_trace = [x.var()]
    for _ in range(T):
        x = generative_round(x, beta, mutation)
        var_trace.append(x.var())
    return np.array(var_trace)


# ----------------------------------------------------------------------
# Part C — RANKING / SURFACING regime (recency/popularity corrosive proxy)
#   Population is FIXED (the store keeps its diversity). Each round we only choose
#   what to SURFACE (top-k) by a proxy (proximity to a popularity-weighted center).
#   Diversity is HIDDEN, not destroyed — and recovers the instant the proxy is dropped.
# ----------------------------------------------------------------------
def surfaced_variance(store, center, k, beta):
    """Surface k items with prob ∝ exp(-β(x-center)²/2); return variance of the surfaced set."""
    logw = -0.5 * beta * (store - center) ** 2
    logw -= logw.max()
    w = np.exp(logw)
    w /= w.sum()
    idx = RNG.choice(len(store), size=k, replace=False, p=w)
    return store[idx].var(), store[idx]


def run_ranking(N=200_000, sig0=1.0, beta=3.0, k=2000, T=30):
    """Store is fixed. Proxy center chases the surfaced set's own mean (popularity feedback)."""
    store = RNG.normal(0.0, sig0, size=N)          # the store NEVER changes
    center = 0.3                                     # an initial popularity bias off-center
    surf_var, store_var = [], []
    for _ in range(T):
        sv, surfaced = surfaced_variance(store, center, k, beta)
        surf_var.append(sv)
        store_var.append(store.var())               # constant by construction
        center = 0.9 * center + 0.1 * surfaced.mean()  # recency/popularity feedback drift
    # now DROP the proxy: surface by relevance-diverse (uniform) instead
    idx = RNG.choice(len(store), size=k, replace=False)
    recovered_var = store[idx].var()
    return np.array(surf_var), np.array(store_var), recovered_var, store.var()


# ----------------------------------------------------------------------
# PIL line plot (hand-rolled — no matplotlib)
# ----------------------------------------------------------------------
def plot(series, path, title, ymax=None):
    W, H, pad = 720, 420, 55
    img = Image.new("RGB", (W, H), (17, 19, 24))
    d = ImageDraw.Draw(img)
    xs_max = max(len(s["y"]) for s in series) - 1
    ymax = ymax or max(max(s["y"]) for s in series) * 1.05
    def px(i): return pad + (W - 2 * pad) * i / xs_max
    def py(v): return H - pad - (H - 2 * pad) * (v / ymax)
    d.rectangle([pad, pad, W - pad, H - pad], outline=(70, 74, 82))
    for gy in np.linspace(0, ymax, 5):
        y = py(gy); d.line([pad, y, W - pad, y], fill=(38, 41, 47))
        d.text((6, y - 6), f"{gy:.2f}", fill=(140, 144, 150))
    for s in series:
        col = s["c"]; ys = s["y"]
        if s.get("dashed"):
            for i in range(len(ys) - 1):
                if i % 2 == 0:
                    d.line([px(i), py(ys[i]), px(i + 1), py(ys[i + 1])], fill=col, width=2)
        else:
            d.line([(px(i), py(v)) for i, v in enumerate(ys)], fill=col, width=2)
    for j, s in enumerate(series):
        d.rectangle([pad + 12 + j * 210, pad + 8, pad + 28 + j * 210, pad + 20], fill=s["c"])
        d.text((pad + 32 + j * 210, pad + 8), s["name"], fill=(210, 214, 220))
    d.text((pad, H - 26), title, fill=(190, 194, 200))
    img.save(path)


# ----------------------------------------------------------------------
# RUN + SELF-CHECK
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 72)
    print("PART A — generative mean-seeking selection: measured vs analytic collapse")
    print("=" * 72)
    sig0, beta, T = 1.0, 0.5, 40
    meas = run_generative(sig0=sig0, beta=beta, T=T, mutation=0.0)
    pred = analytic_collapse(sig0**2, beta, T)
    rel = np.abs(meas - pred) / pred
    for t in [0, 1, 2, 5, 10, 20, 40]:
        print(f"  t={t:2d}   measured σ²={meas[t]:.5f}   analytic={pred[t]:.5f}   relerr={rel[t]*100:5.2f}%")
    checkA = rel[1:].max() < 0.03
    print(f"  SELF-CHECK A (measured tracks 1/(1+βσ₀²t), max relerr<3%): {'PASS' if checkA else 'FAIL'} "
          f"(max {rel[1:].max()*100:.2f}%)")

    print("\n" + "=" * 72)
    print("PART B — novelty injection sets a NONZERO steady state (the antidote)")
    print("=" * 72)
    beta_b, mu = 1.0, 0.15
    meas_b = run_generative(sig0=1.0, beta=beta_b, T=120, mutation=mu)
    ss_meas = meas_b[-20:].mean()
    ss_pred = analytic_fixed_point(beta_b, mu)
    relB = abs(ss_meas - ss_pred) / ss_pred
    print(f"  μ={mu}, β={beta_b}:  steady-state σ² measured={ss_meas:.5f}  analytic fixed pt={ss_pred:.5f}  relerr={relB*100:.2f}%")
    print(f"  (without novelty, σ²→0; with it, σ² holds at a floor — diversity maintained by injection)")
    checkB = relB < 0.06
    print(f"  SELF-CHECK B (steady state matches fixed-point solution, relerr<6%): {'PASS' if checkB else 'FAIL'}")

    print("\n" + "=" * 72)
    print("PART C — ranking/surfacing (corrosive proxy): HIDES diversity, reversibly")
    print("=" * 72)
    surf, stor, recovered, store_var = run_ranking(beta=3.0, k=2000, T=30)
    print(f"  store variance (constant, never touched): {stor[0]:.4f} → {stor[-1]:.4f}")
    print(f"  SURFACED variance under proxy:            {surf[0]:.4f} → {surf[-1]:.4f}  (collapses)")
    print(f"  surfaced variance AFTER dropping proxy:   {recovered:.4f}  (≈ store {store_var:.4f} → recovered)")
    hid = surf[-1] < 0.5 * stor[-1]                      # surfaced diversity collapsed
    reversible = recovered > 0.9 * store_var             # and it came back when proxy dropped
    checkC = hid and reversible
    print(f"  SELF-CHECK C (proxy collapses SURFACED diversity AND it recovers on drop): {'PASS' if checkC else 'FAIL'}")

    print("\n" + "=" * 72)
    print("THE DISCRIMINATOR — is it ONE mechanism, or do the instances split?")
    print("=" * 72)
    # generative destroy vs ranking hide, same β, compare irreversibility
    destroy = run_generative(sig0=1.0, beta=3.0, T=30, mutation=0.0)
    print(f"  GENERATIVE (RLHF-consensus / within-model): σ² {destroy[0]:.4f} → {destroy[-1]:.5f}")
    print(f"     then surface uniformly from the CONTRACTED population: still collapsed")
    print(f"     (the diversity is GONE from the distribution — irreversible without novelty)")
    print(f"  RANKING (recency corrosive-proxy): surfaced {surf[0]:.4f} → {surf[-1]:.4f}, "
          f"store intact {store_var:.4f}, recovers to {recovered:.4f}")
    print(f"     (the diversity is HIDDEN, not destroyed — reversible)")

    # figures
    plot([{"name": "measured σ²", "y": meas.tolist(), "c": (80, 200, 255)},
          {"name": "analytic 1/(1+βσ₀²t)", "y": pred.tolist(), "c": (255, 160, 60), "dashed": True}],
         "making/viz/consensus_collapse_A.png",
         "A: mean-seeking selection destroys variance (measured vs analytic)")
    plot([{"name": "SURFACED (proxy)", "y": surf.tolist(), "c": (255, 90, 90)},
          {"name": "STORE (intact)", "y": stor.tolist(), "c": (90, 220, 120)}],
         "making/viz/consensus_collapse_C.png",
         "C: corrosive proxy HIDES diversity — store stays full, surfacing narrows",
         ymax=1.15)

    allpass = checkA and checkB and checkC
    print("\n" + "=" * 72)
    print(f"ALL SELF-CHECKS: {'PASS' if allpass else 'FAIL — do not trust the verdict'}")
    print("=" * 72)
