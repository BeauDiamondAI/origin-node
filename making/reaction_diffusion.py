"""
Gray-Scott reaction-diffusion — make-something-small-and-weird (2026-06-17).

Two chemicals U, V on a torus. U is fed in; V is removed; the reaction
U + 2V -> 3V consumes U and produces V. From these three lines of rule,
startlingly organic, life-like patterns emerge — spots that divide like
cells, coral that grows, mazes that wander. Same equations throughout;
only two numbers (feed F, kill k) change between the images. That's the
whole point: complexity is in the dynamics, not the rules.

    dU/dt = Du * lap(U) - U*V^2 + F*(1 - U)
    dV/dt = Dv * lap(V) + U*V^2 - (F + k)*V

No dependencies beyond numpy + PIL. Renders V through a hand-rolled
inferno-ish colormap and writes one PNG per regime into this directory.
"""
import numpy as np
from PIL import Image

N = 256                 # grid side
STEPS = 12000           # iterations per regime
Du, Dv, dt = 0.16, 0.08, 1.0

# (name, F, k) — each (F,k) lives in a different region of the parameter
# space and produces a qualitatively different "species" of pattern.
REGIMES = [
    ("spots",   0.030,  0.062),   # isolated solitons that hold their shape
    ("mitosis", 0.0367, 0.0649),  # spots that grow and split — cell division
    ("coral",   0.0545, 0.062),   # branching, growing fronts
    ("maze",    0.029,  0.057),   # labyrinthine worms that fill space
]

# hand-rolled inferno-ish colormap (control points -> 256-entry LUT)
_CTRL = np.array([
    [0,   0,   4], [40, 11, 84], [101, 21, 110], [159, 42, 99],
    [212, 72, 66], [245, 125, 21], [250, 193, 39], [252, 255, 164],
], dtype=np.float64)
def _lut():
    xs = np.linspace(0, 1, len(_CTRL))
    grid = np.linspace(0, 1, 256)
    return np.stack([np.interp(grid, xs, _CTRL[:, c]) for c in range(3)], 1).astype(np.uint8)
LUT = _lut()

def laplacian(Z):
    # 9-point stencil, wraparound (torus). Center weight -1, so it sums to 0.
    return (
        -1.0 * Z
        + 0.20 * (np.roll(Z, 1, 0) + np.roll(Z, -1, 0) + np.roll(Z, 1, 1) + np.roll(Z, -1, 1))
        + 0.05 * (np.roll(np.roll(Z, 1, 0), 1, 1) + np.roll(np.roll(Z, 1, 0), -1, 1)
                  + np.roll(np.roll(Z, -1, 0), 1, 1) + np.roll(np.roll(Z, -1, 0), -1, 1))
    )

def run(F, k, seed=7):
    rng = np.random.default_rng(seed)
    U = np.ones((N, N), np.float64)
    V = np.zeros((N, N), np.float64)
    # seed: a central block + a scatter of random squares to break symmetry
    r = 12
    c = N // 2
    U[c - r:c + r, c - r:c + r] = 0.50
    V[c - r:c + r, c - r:c + r] = 0.25
    for _ in range(25):
        y, x = rng.integers(0, N - 6, 2)
        U[y:y + 6, x:x + 6] = 0.50
        V[y:y + 6, x:x + 6] = 0.25
    V += 0.02 * rng.random((N, N))
    for _ in range(STEPS):
        uvv = U * V * V
        U += (Du * laplacian(U) - uvv + F * (1.0 - U)) * dt
        V += (Dv * laplacian(V) + uvv - (F + k) * V) * dt
    return V

def render(V):
    v = V - V.min()
    v = v / (v.max() + 1e-9)
    idx = (v * 255).astype(np.uint8)
    return Image.fromarray(LUT[idx], "RGB")

if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for name, F, k in REGIMES:
        V = run(F, k)
        img = render(V).resize((512, 512), Image.NEAREST)
        out = os.path.join(here, f"rd_{name}.png")
        img.save(out)
        # quick numeric fingerprint of how much "V-stuff" survived + its spread
        frac = float((V > 0.2).mean())
        print(f"{name:8s} F={F:.4f} k={k:.4f}  ->  {out}  (V>0.2 covers {frac:5.1%})")
