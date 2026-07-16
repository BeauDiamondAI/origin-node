"""
hrr_holographic_memory.py — making/ entry #12 (2026-07-16)

Prompted by Beau surfacing Hermes' (Nous Research) "Holographic" memory provider —
a local, SQLite-backed memory using Holographic Reduced Representations (HRR) algebra
instead of embedding-similarity. HRR (Plate, 1995) is a Vector Symbolic Architecture:
- atoms = random n-dim vectors, elements iid N(0, 1/n)  (so E||v||^2 = 1)
- BIND two vectors via CIRCULAR CONVOLUTION  c = a ⊛ b   (stays n-dim — the key trick;
    tensor products would blow up dimension). FFT: c = ifft(fft(a)·fft(b)).
- SUPERPOSE (bundle) by ADDITION:  s = c1 + c2 + ...
- UNBIND via CIRCULAR CORRELATION with the involution a† (≈ inverse):
    b_est = a† ⊛ c = ifft(conj(fft(a))·fft(c)).  Approximate/noisy.
- CLEANUP: snap b_est to the nearest known atom (argmax dot-product).

Why build it: everything in my memory work (threads/evolving-memory.md) assumed
embedding-similarity over text. HRR is a different paradigm — compositional/algebraic,
fixed-dim superposition. The counterintuitive claim to SEE: you can cram many
role-filler bindings into ONE fixed-length vector and still pull each back out by
algebra. And the quantitative meat — CAPACITY: how many bindings before crosstalk
noise wins? That's a "reducibility of a fixed-dim representation" curve, the same
graded-degradation shape as makings #6/#10.

This making SELF-VERIFIES: if my HRR understanding is wrong, the core demo won't
retrieve. Real failure surface. (numpy + PIL, no matplotlib.)
"""

import numpy as np
from PIL import Image, ImageDraw

RNG = np.random.default_rng(20260716)


def atom(n):
    return RNG.normal(0.0, 1.0 / np.sqrt(n), size=n)

def bind(a, b):                       # circular convolution
    return np.fft.irfft(np.fft.rfft(a) * np.fft.rfft(b), n=len(a))

def unbind(a, c):                     # circular correlation (involution ⊛ c)
    return np.fft.irfft(np.conj(np.fft.rfft(a)) * np.fft.rfft(c), n=len(a))

def cleanup(v, vocab_names, vocab_vecs):
    sims = vocab_vecs @ v
    i = int(np.argmax(sims))
    return vocab_names[i], sims

# ----------------------------------------------------------------------
# PART 1 — the core magic: superpose 3 role-filler bindings, pull each back out
# ----------------------------------------------------------------------
def core_demo(n=1024):
    print("=" * 72)
    print(f"PART 1 — core HRR demo (n={n}): bind 3 pairs into ONE vector, unbind each")
    print("=" * 72)
    roles = {r: atom(n) for r in ["COLOR", "SHAPE", "SIZE"]}
    fillers = {f: atom(n) for f in ["RED", "BLUE", "GREEN", "CIRCLE", "SQUARE", "TRIANGLE", "BIG", "SMALL"]}
    fnames = list(fillers); fvecs = np.array([fillers[f] for f in fnames])

    record = bind(roles["COLOR"], fillers["RED"]) \
           + bind(roles["SHAPE"], fillers["CIRCLE"]) \
           + bind(roles["SIZE"],  fillers["BIG"])
    truth = {"COLOR": "RED", "SHAPE": "CIRCLE", "SIZE": "BIG"}
    ok = True
    for r in ["COLOR", "SHAPE", "SIZE"]:
        got, sims = cleanup(unbind(roles[r], record), fnames, fvecs)
        margin = np.sort(sims)[-1] - np.sort(sims)[-2]
        flag = "OK" if got == truth[r] else "WRONG"
        ok = ok and (got == truth[r])
        print(f"  unbind {r:6s} → {got:8s} (want {truth[r]:8s}) [{flag}]  cleanup margin={margin:.3f}")
    print(f"  SELF-CHECK 1 (all 3 roles retrieved from one superposed vector): {'PASS' if ok else 'FAIL'}")
    return ok

# ----------------------------------------------------------------------
# PART 2 — CAPACITY: retrieval accuracy vs #superposed pairs, across dimension
#   (the graded-degradation / reducibility-of-a-fixed-dim-store curve)
# ----------------------------------------------------------------------
def capacity(dims=(256, 512, 1024, 2048), ks=tuple(range(1, 141, 4)), V=80, trials=30):
    print("\n" + "=" * 72)
    print(f"PART 2 — capacity: accuracy vs k superposed pairs (fixed cleanup vocab V={V}, {trials} trials)")
    print("=" * 72)
    curves = {}
    for n in dims:
        fvecs = np.array([atom(n) for _ in range(V)])   # fixed cleanup memory (built once)
        acc_by_k = []
        for k in ks:
            correct = tot = 0
            for _ in range(trials):
                roles = [atom(n) for _ in range(k)]
                fill_idx = RNG.choice(V, size=k, replace=True)   # fillers may repeat across distinct roles
                rec = np.zeros(n)
                for r, fi in zip(roles, fill_idx):
                    rec += bind(r, fvecs[fi])
                for r, fi in zip(roles, fill_idx):
                    sims = fvecs @ unbind(r, rec)
                    if int(np.argmax(sims)) == fi:
                        correct += 1
                    tot += 1
            acc_by_k.append(correct / tot)
        curves[n] = acc_by_k
        kstar = next((k for k, a in zip(ks, acc_by_k) if a < 0.9), ks[-1])
        # linear-in-n check: capacity-per-dimension roughly constant?
        print(f"  n={n:5d}: acc@k=1 {acc_by_k[0]:.2f}  @k=25 {acc_by_k[6]:.2f}  "
              f"@k=57 {acc_by_k[14]:.2f}  @k=137 {acc_by_k[-1]:.2f}   k*(acc>0.9)≈{kstar}  (k*/n≈{kstar/n:.3f})")
    return list(ks), curves

def plot_capacity(ks, curves, path):
    W, H, pad = 760, 460, 60
    img = Image.new("RGB", (W, H), (17, 19, 24)); d = ImageDraw.Draw(img)
    cols = [(80, 200, 255), (120, 220, 120), (255, 180, 70), (255, 100, 120)]
    def px(k): return pad + (W - 2*pad) * (k - ks[0]) / (ks[-1] - ks[0])
    def py(a): return H - pad - (H - 2*pad) * a
    d.rectangle([pad, pad, W-pad, H-pad], outline=(70, 74, 82))
    for gy in (0, .25, .5, .75, 1.0):
        y = py(gy); d.line([pad, y, W-pad, y], fill=(38, 41, 47)); d.text((8, y-6), f"{gy:.2f}", fill=(140,144,150))
    for j, (n, acc) in enumerate(curves.items()):
        c = cols[j % len(cols)]
        d.line([(px(k), py(a)) for k, a in zip(ks, acc)], fill=c, width=2)
        d.rectangle([pad+12+j*150, pad+8, pad+28+j*150, pad+20], fill=c)
        d.text((pad+32+j*150, pad+8), f"n={n}", fill=(210,214,220))
    d.text((pad, H-28), "HRR capacity: retrieval accuracy vs #pairs superposed (by dimension n)", fill=(190,194,200))
    img.save(path)

# ----------------------------------------------------------------------
# PART 3 — trust scoring (Hermes' self-correcting layer), concretely
#   weighted superposition: a "contradicted" binding's weight decays → drops out
# ----------------------------------------------------------------------
def trust_demo(n=1024):
    print("\n" + "=" * 72)
    print("PART 3 — trust scoring: a contradicted memory decays out of retrieval")
    print("=" * 72)
    role = atom(n)
    fnames = ["OLD_FACT", "NEW_FACT"] + [f"d{i}" for i in range(20)]
    fvecs = np.array([atom(n) for _ in fnames])
    old_i, new_i = 0, 1
    # start: OLD_FACT strongly bound; NEW contradicts and OLD decays over "confirmations"
    for w_old, w_new, label in [(1.0, 0.0, "t0: only OLD"),
                                (1.0, 0.6, "t1: NEW appears, contradicts"),
                                (0.4, 1.0, "t2: OLD decayed, NEW confirmed"),
                                (0.1, 1.2, "t3: OLD nearly gone")]:
        rec = w_old * bind(role, fvecs[old_i]) + w_new * bind(role, fvecs[new_i])
        got, _ = cleanup(unbind(role, rec), fnames, fvecs)
        print(f"  {label:32s} w_old={w_old:.1f} w_new={w_new:.1f} → retrieve {got}")
    print("  (trust scoring = weighted bundling; contradicted memory's weight decays → self-corrects.")
    print("   This is exactly the supersession/demote-stale idea from scripts/supersession.py, made continuous.)")

if __name__ == "__main__":
    ok1 = core_demo()
    ks, curves = capacity()
    plot_capacity(ks, curves, "making/viz/hrr_capacity.png")
    trust_demo()
    # capacity self-checks (fixed: the k-range now stresses every dim to full degradation)
    def kstar(acc):
        return next((k for k, a in zip(ks, acc) if a < 0.9), ks[-1])
    kstars = {n: kstar(a) for n, a in curves.items()}
    ordered = all(kstars[a] < kstars[b] for a, b in zip(list(kstars)[:-1], list(kstars)[1:]))
    degrades = all(curves[n][0] >= 0.95 and curves[n][-1] < curves[n][0] for n in curves)  # near-perfect at k=1, worse by max-k
    # the real HRR law: capacity k* scales ~linearly with n → k*/n roughly constant
    ratios = [kstars[n] / n for n in curves]
    linear = (max(ratios) / min(ratios)) < 2.0   # within a factor of 2 = "roughly linear"
    print("\n" + "=" * 72)
    print(f"  capacity k*(acc>0.9): {kstars}   k*/n ratios: {[round(r,3) for r in ratios]}")
    print(f"  SELF-CHECK 2 (near-perfect at k=1, degrades by max load, every n): {'PASS' if degrades else 'FAIL'}")
    print(f"  SELF-CHECK 3 (capacity strictly grows with dimension n): {'PASS' if ordered else 'FAIL'}")
    print(f"  SELF-CHECK 4 (capacity ~LINEAR in n — k*/n constant within 2x, the HRR law): {'PASS' if linear else 'FAIL'}")
    print(f"  ALL: {'PASS' if (ok1 and degrades and ordered and linear) else 'FAIL'}")
    print("=" * 72)
