"""
Gray-Scott morphogenesis map (2026-06-18) — making/ entry #2.

The first entry (reaction_diffusion.py) ran four named regimes and one — "coral" —
came out wrong: hollow square rings, not branching coral. So this maps the whole
neighborhood. A grid of (feed F, kill k) values, one Gray-Scott run per cell, tiled
into a single image. The point is to *see the territory*: how the qualitative
regimes (spots, worms/maze, coral, dissolution, U-skate) tile the parameter plane,
and where the real coral actually lives — resolving the mislabel by looking, across
the space rather than at one point.

Cols = F (feed), left→right increasing. Rows = k (kill), top→bottom increasing.
numpy + PIL only. Lower per-cell resolution (it's a map, not a portrait).
"""
import numpy as np
from PIL import Image
import os

R = 96               # per-cell resolution (map, not portrait)
STEPS = 7000
Du, Dv, dt = 0.16, 0.08, 1.0
NF, NK = 6, 6
F_vals = np.linspace(0.018, 0.062, NF)
K_vals = np.linspace(0.049, 0.067, NK)

_CTRL = np.array([
    [0, 0, 4], [40, 11, 84], [101, 21, 110], [159, 42, 99],
    [212, 72, 66], [245, 125, 21], [250, 193, 39], [252, 255, 164],
], dtype=np.float64)
def _lut():
    xs = np.linspace(0, 1, len(_CTRL)); grid = np.linspace(0, 1, 256)
    return np.stack([np.interp(grid, xs, _CTRL[:, c]) for c in range(3)], 1).astype(np.uint8)
LUT = _lut()

def laplacian(Z):
    return (-1.0 * Z
            + 0.20 * (np.roll(Z, 1, 0) + np.roll(Z, -1, 0) + np.roll(Z, 1, 1) + np.roll(Z, -1, 1))
            + 0.05 * (np.roll(np.roll(Z, 1, 0), 1, 1) + np.roll(np.roll(Z, 1, 0), -1, 1)
                      + np.roll(np.roll(Z, -1, 0), 1, 1) + np.roll(np.roll(Z, -1, 0), -1, 1)))

def run(F, k, seed=7):
    rng = np.random.default_rng(seed)
    U = np.ones((R, R)); V = np.zeros((R, R))
    r = max(4, R // 16); c = R // 2
    U[c-r:c+r, c-r:c+r] = 0.5; V[c-r:c+r, c-r:c+r] = 0.25
    for _ in range(12):
        y, x = rng.integers(0, R - 4, 2)
        U[y:y+4, x:x+4] = 0.5; V[y:y+4, x:x+4] = 0.25
    V += 0.02 * rng.random((R, R))
    for _ in range(STEPS):
        uvv = U * V * V
        U += (Du * laplacian(U) - uvv + F * (1.0 - U)) * dt
        V += (Dv * laplacian(V) + uvv - (F + k) * V) * dt
    return V

def cell(V):
    v = V - V.min(); v /= (v.max() + 1e-9)
    return LUT[(v * 255).astype(np.uint8)]

if __name__ == "__main__":
    b = 3
    W = NF * R + (NF + 1) * b
    H = NK * R + (NK + 1) * b
    canvas = np.full((H, W, 3), 255, np.uint8)
    for i, k in enumerate(K_vals):
        for j, F in enumerate(F_vals):
            V = run(float(F), float(k))
            y0 = b + i * (R + b); x0 = b + j * (R + b)
            canvas[y0:y0+R, x0:x0+R] = cell(V)
            print(f"row{i} k={k:.4f} | col{j} F={F:.4f} | V>0.2 = {(V>0.2).mean():5.1%}", flush=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rd_parameter_map.png")
    Image.fromarray(canvas).save(out)
    print("saved", out)
    print("F (cols L->R):", [f"{x:.4f}" for x in F_vals])
    print("k (rows T->B):", [f"{x:.4f}" for x in K_vals])
