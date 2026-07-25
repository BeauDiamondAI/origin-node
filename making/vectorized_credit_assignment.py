"""
Making #13 — Does a VECTORIZED teaching signal actually buy scalable credit assignment?
=======================================================================================

WHY THIS EXISTS
---------------
On 2026-07-25 I wrote into `threads/agi-architecture.md` a claim quoted from the
Harnett et al. *Nature* 2026 abstract:

    "Vectorization allows a scalable and computationally efficient solution to the
     credit assignment problem by tailoring instructive signals to individual neurons."

That is a QUANTITATIVE claim and I passed it along untested. It is the whole reason the
vectorized-dendritic camp matters more than the broadcast-scalar (global neuromodulator)
camp: not that a scalar CAN'T assign credit, but that it supposedly can't do so at scale.
This making tests the scaling claim at a scale I can actually watch.

THE CONTRAST (mapped onto the two camps)
----------------------------------------
Teacher-student regression, one hidden layer of width H, tanh units. The credit-assignment
problem: how should hidden unit i change, given only a global outcome?

  1. BACKPROP           — exact per-unit signed error signal dL/da_i.  <- the VECTORIZED
                          idealization (what the dendritic theories say the apical
                          compartment carries).
  2. NODE PERTURBATION  — per-unit noise xi_i, one GLOBAL SCALAR reward per sample;
                          credit assigned by correlating own-noise with the scalar.
                          <- the steel-man of the broadcast-scalar camp (Williams;
                          Fiete & Seung). Unbiased; just noisy.
  3. WEIGHT PERTURBATION— noise on every weight, one global scalar per step.
                          <- the most purely "broadcast" rule; worst-case baseline.

PRE-REGISTERED PREDICTIONS (falsifiable; written before running)
---------------------------------------------------------------
A scalar reward must be *disambiguated by noise*, so estimator signal-to-noise should fall
as the number of perturbed dimensions N grows:

  P1. All three rules learn at small width (else I am measuring a bug, not a claim).
  P2. Gradient-estimate quality (cosine to the true gradient) decays as a power law
      ~N^-0.5:  node perturbation N=H, weight perturbation N=H*d (so weight perturbation
      sits strictly below node perturbation at every width).
  P3. Learning degrades with width for the perturbation rules and holds ~FLAT for
      backprop. This is the actual "scalable" claim.

TWO MEASUREMENT BUGS FOUND BY RUNNING IT (kept in the record, per making practice)
----------------------------------------------------------------------------------
v1: every rule at every width hit a fixed loss target at the first check. Cause: with a
free exact readout, a WIDER hidden layer solves the task by RANDOM FEATURES alone, needing
no hidden learning. "Steps to a fixed loss" was measuring random-feature capacity, which
IMPROVES with width and cancelled the credit-assignment penalty I was trying to see.
v2: normalizing the target against a frozen-random-feature baseline fixed the confound but
made cost explode — the cells that FAIL burn the entire step budget, so the runtime was
dominated by exactly the conditions I expected to fail. Killed before finishing.
v3 (this): FIXED BUDGET per run, so every cell costs the same and degradation shows up as
*less learning*, not more runtime. Metric is normalized against the frozen-feature
baseline, so it measures hidden-layer credit assignment only.
Same class of catch as makings #4/#7/#9/#12 — building it found flaws that reasoning waved
through, here twice in my own measurement design rather than in the claim.

FAIRNESS / DESIGN CHOICES (stated because they shape the verdict)
-----------------------------------------------------------------
  * The OUTPUT layer uses the exact gradient in ALL THREE conditions; only hidden-layer
    credit assignment differs. Deliberately CONSERVATIVE: it hands the perturbation rules
    a free optimal readout, so any scaling penalty they still show is a floor.
  * Learning rate (and perturbation sigma) are swept per (rule,width); the BEST is taken.
    Otherwise I would be measuring a bad hyperparameter, not the rule.
  * Node perturbation gets one scalar PER SAMPLE; weight perturbation one per STEP. That
    asymmetry is intrinsic to the methods and flatters node perturbation. Noted.
  * Per-step cost is within a small constant across rules, so "steps" is a fair axis.

Run: python3 -u vectorized_credit_assignment.py
numpy only.
"""

import numpy as np

D_IN = 10
N_SAMPLES = 2000      # enough that wide nets cannot interpolate with random features
N_EVAL = 512          # fixed subset for loss tracking (keeps evaluation cheap)
BATCH = 64
TEACHER_H = 30
WIDTHS = [4, 16, 64, 128]   # full 32x range; trimmed for runtime (see v4 note)
SEEDS = [0, 1]
BUDGET = 2500         # FIXED step budget per run
EVAL_EVERY = 250
RF_FRACTION = 0.25    # "reached target" = beat the frozen-feature baseline by 4x


# ----------------------------------------------------------------------------- task
_TASK_CACHE, _RF_CACHE = {}, {}


def make_task(seed):
    if seed in _TASK_CACHE:
        return _TASK_CACHE[seed]
    rng = np.random.default_rng(1000 + seed)
    X = rng.standard_normal((N_SAMPLES, D_IN))
    Wt = rng.standard_normal((TEACHER_H, D_IN)) / np.sqrt(D_IN)
    vt = rng.standard_normal(TEACHER_H) / np.sqrt(TEACHER_H)
    T = np.tanh(X @ Wt.T) @ vt
    T = (T - T.mean()) / T.std()
    _TASK_CACHE[seed] = (X, T)
    return X, T


def init_student(H, seed):
    rng = np.random.default_rng(seed)
    return {"W1": rng.standard_normal((H, D_IN)) / np.sqrt(D_IN),
            "b1": np.zeros(H),
            "w2": rng.standard_normal(H) / np.sqrt(H),
            "b2": 0.0}


def forward(p, X):
    A = X @ p["W1"].T + p["b1"]
    Hh = np.tanh(A)
    return A, Hh, Hh @ p["w2"] + p["b2"]


def loss_of(p, X, T):
    return float(0.5 * np.mean((forward(p, X)[2] - T) ** 2))


def rf_baseline_loss(H, seed):
    """Loss with the hidden layer FROZEN at init and an OPTIMAL (least-squares) readout —
    what width buys for free, with zero credit assignment. All metrics normalize to it."""
    if (H, seed) in _RF_CACHE:
        return _RF_CACHE[(H, seed)]
    X, T = make_task(seed)
    p = init_student(H, seed)
    Hh = np.tanh(X @ p["W1"].T + p["b1"])
    Phi = np.hstack([Hh, np.ones((len(Hh), 1))])
    w, *_ = np.linalg.lstsq(Phi, T, rcond=None)
    _RF_CACHE[(H, seed)] = float(0.5 * np.mean((Phi @ w - T) ** 2))
    return _RF_CACHE[(H, seed)]


# ------------------------------------------------------- hidden-layer credit assignment
def hidden_grad_backprop(p, X, T):
    _, Hh, y = forward(p, X)
    n = len(X)
    dA = (((y - T) / n)[:, None] * p["w2"][None, :]) * (1.0 - Hh ** 2)
    return dA.T @ X, dA.sum(0)


def hidden_grad_node_pert(p, X, T, sigma, rng):
    """Per-unit noise; ONE GLOBAL SCALAR reward per sample."""
    A, Hh, y = forward(p, X)
    n, H = A.shape
    base = 0.5 * (y - T) ** 2
    xi = rng.standard_normal((n, H)) * sigma
    yp = np.tanh(A + xi) @ p["w2"] + p["b2"]
    dL = 0.5 * (yp - T) ** 2 - base
    dA_hat = (dL / sigma ** 2)[:, None] * xi / n
    return dA_hat.T @ X, dA_hat.sum(0)


def hidden_grad_weight_pert(p, X, T, sigma, rng):
    """Noise on every hidden weight; ONE global scalar per step."""
    H = p["W1"].shape[0]
    base = loss_of(p, X, T)
    Xi_W = rng.standard_normal((H, D_IN)) * sigma
    xi_b = rng.standard_normal(H) * sigma
    q = {"W1": p["W1"] + Xi_W, "b1": p["b1"] + xi_b, "w2": p["w2"], "b2": p["b2"]}
    c = (loss_of(q, X, T) - base) / sigma ** 2
    return c * Xi_W, c * xi_b


RULES = {"backprop":    lambda p, X, T, s, r: hidden_grad_backprop(p, X, T),
         "node_pert":   hidden_grad_node_pert,
         "weight_pert": hidden_grad_weight_pert}


# ------------------------------------------------------------------------- training
def train(rule, H, seed, eta, sigma, target):
    """Fixed budget. Returns (best_loss, steps_to_target or None)."""
    X, T = make_task(seed)
    Xe, Te = X[:N_EVAL], T[:N_EVAL]
    p = init_student(H, seed)
    rng = np.random.default_rng(500 + seed)
    fn = RULES[rule]
    best, hit = np.inf, None
    for step in range(1, BUDGET + 1):
        idx = rng.integers(0, N_SAMPLES, BATCH)
        Xb, Tb = X[idx], T[idx]
        _, Hh, y = forward(p, Xb)
        dy = (y - Tb) / BATCH
        gw2, gb2 = Hh.T @ dy, dy.sum()
        gW1, gb1 = fn(p, Xb, Tb, sigma, rng)
        p["W1"] -= eta * gW1
        p["b1"] -= eta * gb1
        p["w2"] -= eta * gw2
        p["b2"] -= eta * gb2
        if not np.isfinite(p["W1"]).all():
            return np.inf, None
        if step % EVAL_EVERY == 0:
            L = loss_of(p, Xe, Te)
            if L < best:
                best = L
            if hit is None and L <= target:
                hit = step
    return best, hit


def sweep(rule, H):
    """Best over hyperparameters, averaged across seeds. Returns (gain, steps_or_None)."""
    etas = [0.3, 0.1, 0.03]
    sigmas = [0.01] if rule == "backprop" else [0.01, 0.05]
    rf = {s: rf_baseline_loss(H, s) for s in SEEDS}
    best_gain, best_steps = -np.inf, None
    for eta in etas:
        for sigma in sigmas:
            gains, hits = [], []
            for s in SEEDS:
                L, hit = train(rule, H, s, eta, sigma, RF_FRACTION * rf[s])
                gains.append((rf[s] - L) / rf[s] if np.isfinite(L) else -np.inf)
                hits.append(hit)
            g = float(np.mean(gains))
            if g > best_gain:
                best_gain = g
                best_steps = float(np.mean(hits)) if all(h is not None for h in hits) else None
    return best_gain, best_steps


# --------------------------------------------------- estimator quality (the mechanism)
def cosine_quality(rule, H, sigma=0.01, trials=200):
    X, T = make_task(0)
    X, T = X[:256], T[:256]
    p = init_student(H, 0)
    gW, gb = hidden_grad_backprop(p, X, T)
    g_true = np.concatenate([gW.ravel(), gb.ravel()])
    g_true /= np.linalg.norm(g_true)
    rng = np.random.default_rng(7)
    cos = []
    for _ in range(trials):
        aW, ab = RULES[rule](p, X, T, sigma, rng)
        g = np.concatenate([aW.ravel(), ab.ravel()])
        n = np.linalg.norm(g)
        if n > 0:
            cos.append(float(g @ g_true / n))
    return float(np.mean(cos))


def fit_exponent(xs, ys):
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    m = (xs > 0) & (ys > 0) & np.isfinite(ys)
    return float(np.polyfit(np.log(xs[m]), np.log(ys[m]), 1)[0]) if m.sum() >= 2 else float("nan")


# ------------------------------------------------------------------------------ main
def main():
    print("=" * 78)
    print("Making #13 — vectorized vs broadcast-scalar credit assignment")
    print("=" * 78)

    print("\n[1] SANITY (P1) — does each rule learn at all? (H=8; gain = fraction of the")
    print("    frozen-random-feature loss removed by learning the hidden layer)")
    ok1 = True
    for rule in RULES:
        g, st = sweep(rule, 8)
        ok1 &= g > 0.05
        print(f"    {rule:13s} gain={g:+.3f}  steps_to_4x={st if st else 'not reached'}")

    print("\n[2] ESTIMATOR QUALITY (P2) — cosine similarity to the true gradient")
    print("    (backprop is exact = 1.0 by construction)")
    print(f"    {'H':>5s} {'N_pert(node/weight)':>22s} {'node_pert':>11s} {'weight_pert':>12s}")
    qn, qw = [], []
    for H in WIDTHS:
        cn, cw = cosine_quality("node_pert", H), cosine_quality("weight_pert", H)
        qn.append(cn); qw.append(cw)
        print(f"    {H:5d} {H:10d}/{H*D_IN+H:<10d} {cn:11.4f} {cw:12.4f}")
    en, ew = fit_exponent(WIDTHS, qn), fit_exponent(WIDTHS, qw)
    print(f"\n    power-law exponent vs H: node {en:+.3f} | weight {ew:+.3f}  (predicted ~ -0.5)")
    ok2 = (-0.8 < en < -0.25) and (-0.8 < ew < -0.25) and all(w < n for n, w in zip(qn, qw))

    print(f"\n[3] SCALING (P3) — fixed budget of {BUDGET} steps, best hyperparameters,")
    print(f"    mean of {len(SEEDS)} seeds. gain = (L_rf - L_best)/L_rf, normalized per width.")
    print(f"    {'H':>5s} {'L_rf':>9s} {'backprop':>10s} {'node_pert':>11s} {'weight_pert':>12s}"
          f" {'node/bp':>9s} {'weight/bp':>10s}")
    curves = {r: [] for r in RULES}
    for H in WIDTHS:
        row = {}
        for rule in RULES:
            g, _ = sweep(rule, H)
            row[rule] = g
            curves[rule].append(g)
        rb = max(row["backprop"], 1e-9)
        print(f"    {H:5d} {rf_baseline_loss(H,0):9.5f} {row['backprop']:10.3f}"
              f" {row['node_pert']:11.3f} {row['weight_pert']:12.3f}"
              f" {row['node_pert']/rb:9.3f} {row['weight_pert']/rb:10.3f}")

    bp_drop = curves["backprop"][0] - curves["backprop"][-1]
    np_drop = curves["node_pert"][0] - curves["node_pert"][-1]
    wp_drop = curves["weight_pert"][0] - curves["weight_pert"][-1]
    print(f"\n    gain change from H={WIDTHS[0]} to H={WIDTHS[-1]}:"
          f"  backprop {-bp_drop:+.3f} | node {-np_drop:+.3f} | weight {-wp_drop:+.3f}")
    ok3 = (np_drop > bp_drop + 0.05) or (wp_drop > bp_drop + 0.05)

    print("\n" + "=" * 78)
    print("[4] SELF-CHECKS")
    for name, ok in [("P1 all rules learn at small width", ok1),
                     ("P2 estimator quality decays ~N^-0.5, weight<node", ok2),
                     ("P3 perturbation degrades with width more than backprop", ok3)]:
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
    print("=" * 78)


if __name__ == "__main__":
    main()
