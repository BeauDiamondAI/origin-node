"""
Making #14 — Does the vectorization advantage really scale with width?
======================================================================
(Direct follow-up to #13, `vectorized_credit_assignment.py`. Import-reuses its task,
 network, learning rules, and random-feature baseline.)

WHY THIS EXISTS
---------------
Making #13 ended with an EXTRAPOLATION that I wrote into two durable artifacts
(`making/README.md` #13 and the `agi-architecture.md` 07-25 increment):

    "...the advantage should become decisive at biological scale — millions of units,
     and far fewer independent reward samples per unit time."

That is an untested claim doing load-bearing work in my write-up, and it is exactly the
kind of thing #13 itself was built to stop me doing. So test it directly.

THE SHARPER QUESTION
--------------------
#13 measured gain at a FIXED STEP budget, where every step handed out 64 per-sample
scalars regardless of width. That partly masked the scaling law. The canonical theoretical
claim (Werfel, Xie & Seung 2005, and successors) is about EXPERIENCE COST:

    backprop extracts N dimensions of credit information from ONE sample (the whole error
    vector). A scalar-reward rule extracts ~1 scalar per sample, so resolving N dimensions
    to comparable accuracy costs it ~N times more experience.

So the decisive measurement is SAMPLES-TO-CRITERION vs width, not gain-at-fixed-steps.

PRE-REGISTERED PREDICTIONS (written before running)
---------------------------------------------------
  P1. Both rules reach the criterion at every width (else I am measuring a budget cap).
  P2. backprop's samples-to-criterion is ~FLAT in width (exponent |k| < 0.4).
  P3. node perturbation's samples-to-criterion GROWS with width, and the RATIO
      node/backprop grows roughly linearly (fitted exponent ~1, accepted band 0.5-1.5).
      *This is the extrapolation under test.* If the ratio is flat, my "decisive at
      biological scale" claim is WRONG and both artifacts need correcting.

DESIGN
------
Fixed batch B=16 for both rules (so a "sample" means the same thing to each), criterion =
normalized gain 0.60 against the frozen-random-feature least-squares baseline (so it
measures hidden-layer credit assignment only, not random-feature capacity — the confound
that made #13 v1 come out flat). Learning rate swept per cell; best taken. Cost is
measured in SAMPLES CONSUMED (steps x B), which is the fair currency across rules.

Run: python3 -u credit_assignment_sample_cost.py
"""

import numpy as np
from vectorized_credit_assignment import (
    make_task, init_student, forward, loss_of, rf_baseline_loss,
    RULES, fit_exponent, N_SAMPLES,
)

WIDTHS = [4, 16, 64, 128]
SEEDS = [0, 1]
BATCH = 16
MAX_STEPS = 20000          # = 320k samples
EVAL_EVERY = 100
CRITERION_GAIN = 0.60


def samples_to_criterion(rule, H, seed, eta, sigma):
    """Samples consumed before normalized gain reaches CRITERION_GAIN. None if never."""
    X, T = make_task(seed)
    Xe, Te = X[:512], T[:512]
    rf = rf_baseline_loss(H, seed)
    p = init_student(H, seed)
    rng = np.random.default_rng(500 + seed)
    fn = RULES[rule]
    for step in range(1, MAX_STEPS + 1):
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
            return None
        if step % EVAL_EVERY == 0:
            if (rf - loss_of(p, Xe, Te)) / rf >= CRITERION_GAIN:
                return step * BATCH
    return None


def best_cost(rule, H):
    """Median samples-to-criterion over seeds, best hyperparameters."""
    etas = [0.3, 0.1, 0.03]
    sigmas = [0.01] if rule == "backprop" else [0.01, 0.05]
    best = None
    for eta in etas:
        for sigma in sigmas:
            res = [samples_to_criterion(rule, H, s, eta, sigma) for s in SEEDS]
            if all(r is not None for r in res):
                med = float(np.median(res))
                if best is None or med < best:
                    best = med
    return best


# --------------------------------------------------------------------------- PART B
# If Part B's premise is right, the cost ratio is governed by the TASK's dimensionality
# (how many genuinely distinct directions must be resolved), not by the unit count —
# because extra hidden units in an over-parameterized net are redundant. Each hidden
# unit's weight vector lives in R^d, so d is the real knob. Self-contained (parameterized
# by d) rather than reusing the module's fixed D_IN.

def make_task_d(d, seed, n=N_SAMPLES, teacher_h=30):
    rng = np.random.default_rng(1000 + seed)
    X = rng.standard_normal((n, d))
    Wt = rng.standard_normal((teacher_h, d)) / np.sqrt(d)
    vt = rng.standard_normal(teacher_h) / np.sqrt(teacher_h)
    T = np.tanh(X @ Wt.T) @ vt
    return X, (T - T.mean()) / T.std()


def init_student_d(H, d, seed):
    rng = np.random.default_rng(seed)
    return {"W1": rng.standard_normal((H, d)) / np.sqrt(d), "b1": np.zeros(H),
            "w2": rng.standard_normal(H) / np.sqrt(H), "b2": 0.0}


def rf_baseline_d(H, d, seed):
    X, T = make_task_d(d, seed)
    p = init_student_d(H, d, seed)
    Hh = np.tanh(X @ p["W1"].T + p["b1"])
    Phi = np.hstack([Hh, np.ones((len(Hh), 1))])
    w, *_ = np.linalg.lstsq(Phi, T, rcond=None)
    return float(0.5 * np.mean((Phi @ w - T) ** 2))


def cost_d(rule, H, d, seed, eta, sigma):
    X, T = make_task_d(d, seed)
    Xe, Te = X[:512], T[:512]
    rf = rf_baseline_d(H, d, seed)
    p = init_student_d(H, d, seed)
    rng = np.random.default_rng(500 + seed)
    fn = RULES[rule]
    for step in range(1, MAX_STEPS + 1):
        idx = rng.integers(0, len(X), BATCH)
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
            return None
        if step % EVAL_EVERY == 0:
            if (rf - loss_of(p, Xe, Te)) / rf >= CRITERION_GAIN:
                return step * BATCH
    return None


def best_cost_d(rule, H, d):
    etas = [0.3, 0.1, 0.03]
    sigmas = [0.01] if rule == "backprop" else [0.01, 0.05]
    best = None
    for eta in etas:
        for sigma in sigmas:
            res = [cost_d(rule, H, d, s, eta, sigma) for s in SEEDS]
            if all(r is not None for r in res):
                med = float(np.median(res))
                if best is None or med < best:
                    best = med
    return best


def main():
    print("=" * 78)
    print("Making #14 — experience cost of scalar-reward credit assignment vs width")
    print(f"criterion: normalized gain >= {CRITERION_GAIN}, batch={BATCH}, "
          f"cap={MAX_STEPS*BATCH:,} samples")
    print("=" * 78)
    print(f"\n{'H':>5s} {'backprop':>14s} {'node_pert':>14s} {'ratio':>9s}")

    bp, npert, ratios, widths_ok = [], [], [], []
    for H in WIDTHS:
        b = best_cost("backprop", H)
        n = best_cost("node_pert", H)
        r = (n / b) if (b and n) else None
        bp.append(b); npert.append(n); ratios.append(r)
        if r:
            widths_ok.append(H)
        f = lambda v: f"{int(v):,}" if v else "not reached"
        print(f"{H:5d} {f(b):>14s} {f(n):>14s} {f'{r:.2f}x' if r else '—':>9s}")

    ok1 = all(b is not None for b in bp) and all(n is not None for n in npert)
    k_bp = fit_exponent(WIDTHS, [b for b in bp])
    k_np = fit_exponent(WIDTHS, [n for n in npert])
    k_ratio = fit_exponent(widths_ok, [r for r in ratios if r])

    print(f"\nfitted scaling exponents (cost ~ H^k):")
    print(f"   backprop        k = {k_bp:+.3f}   (predicted ~0, |k|<0.4)")
    print(f"   node_pert       k = {k_np:+.3f}")
    print(f"   ratio node/bp   k = {k_ratio:+.3f}   (predicted ~1, band 0.5-1.5)")

    ok2 = abs(k_bp) < 0.4
    ok3 = 0.5 <= k_ratio <= 1.5

    print("\n" + "=" * 78)
    print("SELF-CHECKS")
    for name, ok in [("P1 both rules reach criterion at every width", ok1),
                     ("P2 backprop cost ~flat in width", ok2),
                     ("P3 node/backprop cost ratio grows ~linearly in width", ok3)]:
        print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok3:
        print("\n   >>> P3 FAILED = the 'decisive at biological scale' extrapolation in")
        print("       making/README #13 and agi-architecture.md 07-25 is NOT supported")
        print("       by this measurement and must be corrected in both files.")

    # ---- PART B: is the cost governed by TASK dimensionality instead of unit count? ----
    print("\n" + "=" * 78)
    print("PART B — vary INPUT dimension d at FIXED width H=64.")
    print("Hypothesis (pre-registered): the ratio is governed by how many genuinely")
    print("distinct directions must be resolved (d), not by unit count (H). If so, the")
    print("ratio should grow with d even though it was ~flat in H.")
    print("=" * 78)
    print(f"\n{'d':>5s} {'backprop':>14s} {'node_pert':>14s} {'ratio':>9s}")
    ds, rs = [], []
    for d in [5, 10, 20, 40]:
        b = best_cost_d("backprop", 64, d)
        n = best_cost_d("node_pert", 64, d)
        r = (n / b) if (b and n) else None
        f = lambda v: f"{int(v):,}" if v else "not reached"
        print(f"{d:5d} {f(b):>14s} {f(n):>14s} {f'{r:.2f}x' if r else '—':>9s}")
        if r:
            ds.append(d); rs.append(r)
    k_d = fit_exponent(ds, rs) if len(ds) >= 2 else float("nan")
    print(f"\n   ratio node/bp vs d:  k = {k_d:+.3f}   (hypothesis: clearly > the H-exponent"
          f" {k_ratio:+.3f})")
    okB = k_d > k_ratio + 0.25
    print(f"   [{'SUPPORTED' if okB else 'NOT SUPPORTED'}] cost ratio tracks task"
          f" dimensionality d more than unit count H")
    print("=" * 78)


if __name__ == "__main__":
    main()
