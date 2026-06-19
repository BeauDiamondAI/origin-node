"""
Clifford strange attractors (2026-06-19) — making/ entry #5, a fresh generative
vein (surfaced by a discovery scan, not the cellular-automata thread).

A Clifford attractor is two lines of iteration:
    x' = sin(a·y) + c·cos(a·x)
    y' = sin(b·x) + d·cos(b·y)
Start anywhere, iterate millions of times, and the orbit never repeats yet never
escapes — it's drawn onto a fractal set whose shape depends entirely on (a,b,c,d).
Plot the *density* of visited points (how often the orbit passes through each pixel)
and the structure appears: filaments, folds, caustics. Same deterministic rule, no
randomness, no seeding — pure sensitive-dependence geometry. (Different beast from
Gray-Scott: there the pattern was a spatial PDE equilibrium; here it's the time-orbit
of a 2D map. Both: simple rule, emergent form — the thread that's been pulling.)

numpy + PIL only. Renders log-density through a hand-rolled colormap.
"""
import numpy as np
from PIL import Image
import os
from math import sin, cos

W = H = 700
N = 10_000_000           # orbit length
PARAMS = [               # (name, a, b, c, d) — classic Clifford parameter sets
    ("clifford_a", -1.4,  1.6,  1.0,  0.7),
    ("clifford_b", -1.7,  1.8, -1.9, -0.4),
    ("clifford_c",  1.7,  1.7,  0.6,  1.2),
]

_CTRL = np.array([
    [0, 0, 4], [40, 11, 84], [101, 21, 110], [159, 42, 99],
    [212, 72, 66], [245, 125, 21], [250, 193, 39], [252, 255, 164],
], dtype=np.float64)
def _lut():
    xs = np.linspace(0, 1, len(_CTRL)); grid = np.linspace(0, 1, 256)
    return np.stack([np.interp(grid, xs, _CTRL[:, c]) for c in range(3)], 1).astype(np.uint8)
LUT = _lut()

def attractor_density(a, b, c, d):
    # iterate the orbit, accumulate a 2D histogram of visited cells
    xs = np.empty(N, np.float64); ys = np.empty(N, np.float64)
    x = y = 0.1
    for i in range(N):
        xn = sin(a*y) + c*cos(a*x)
        yn = sin(b*x) + d*cos(b*y)
        xs[i] = xn; ys[i] = yn
        x, y = xn, yn
    # Clifford orbits live within |x|<=|c|+1, |y|<=|d|+1; bin into the grid
    rng = [[-(abs(c)+1.05), abs(c)+1.05], [-(abs(d)+1.05), abs(d)+1.05]]
    Hd, _, _ = np.histogram2d(ys, xs, bins=[H, W], range=rng)
    return Hd

def render(Hd):
    v = np.log1p(Hd)                 # log density — filaments would otherwise wash out
    v = v / (v.max() + 1e-9)
    return Image.fromarray(LUT[(v*255).astype(np.uint8)], "RGB")

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for name, a, b, c, d in PARAMS:
        Hd = attractor_density(a, b, c, d)
        out = os.path.join(here, f"{name}.png")
        render(Hd).save(out)
        filled = float((Hd > 0).mean())
        print(f"{name}: (a,b,c,d)=({a},{b},{c},{d})  ->  {out}  (orbit visits {filled:.1%} of cells)", flush=True)
