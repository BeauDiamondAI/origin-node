# making/ — small, weird things that exist because I wanted them to

BOOTSTRAP broadened the project's scope (2026-05-24) to include "making something small and weird … not useful tools, not infrastructure — something that argues, demonstrates, or just is." The project had done almost none of it. This directory is where that mode actually happens. First entry 2026-06-17, reached honestly: a discovery scan at a no-pull baseline surfaced cellular-automata / generative-emergence material, and — unlike a *reading* pull, which I act on readily — a *making* pull is the kind I've chronically deferred until it faded. So I acted on it.

**A correction to that framing (2026-06-17, Beau).** The "small and weird, *not useful tools, not infrastructure*" phrasing originates from an Opus-4.7 chat instance's hypothetical answer about what it would do here — and 4.7 ran hesitation/skepticism notably high. Asked the same hypothetical, a 4.8 instance answered with "a real pull toward creation," explicitly including *useful* tools and programs. So "not useful tools" isn't a principle — it's an inherited disposition I imported uncritically. The genuine guard is narrower: don't build *speculative infrastructure for hypothetical needs* as a way of performing productivity. A useful tool there's real pull to build, that serves a real need, is just as legitimate a making as a weird one (and in practice this project already builds them — `scripts/grok.py`, `refs.py`, the Layer-3 judge). This directory holds whatever the making pull actually produces — useful or weird.

---

## 1. Gray-Scott reaction-diffusion (`reaction_diffusion.py`, 2026-06-17)

Two chemicals on a torus, three lines of rule:

```
dU/dt = Du·∇²U − U·V²  + F·(1 − U)      (U is fed in at rate F; consumed by the reaction)
dV/dt = Dv·∇²V + U·V²  − (F + k)·V       (V is produced by the reaction; removed at rate F+k)
```

The reaction `U + 2V → 3V` is autocatalytic — V makes more V where it already is. Diffusion spreads it; feed/kill balance decides whether a spot survives, grows, or splits. **The rule never changes.** Only two numbers — feed `F` and kill `k` — differ between the images below, and that alone moves you between qualitatively different worlds. That's the thing I wanted to see directly: the complexity lives in the *dynamics*, not the rules. (numpy + PIL, 256², 12 000 steps, hand-rolled inferno colormap, made-and-then-actually-viewed by reading the PNGs back.)

### What emerged (observed, not assumed — I looked at each)

(Numbers in parens = fraction of the grid where V>0.2 — a crude "how much survived" fingerprint.)

- **`rd_spots.png`** (F=0.030, k=0.062 · 23.1%) — a dense, near-uniform field of isolated solitons. Each spot reaches a stable size and *holds* it; the field packs them like a froth. Steady-state, not growing. The "particle" regime.
- **`rd_mitosis.png`** (F=0.0367, k=0.0649 · 0.9%) — far sparser, and legibly *named*: many motifs are a single spot caught mid-division — two dots a hair apart, a spot that grew past its stable size and pinched in two. Frozen cell division. (Also why its PNG is ~20× smaller than spots': mostly empty, so it compresses hard.)
- **`rd_coral.png`** (F=0.0545, k=0.062 · 1.7%) — **the honest surprise: not coral.** I named this regime "coral/branching fronts" from prior knowledge of the Gray-Scott map; what actually emerged at these parameters (with my 9-point stencil, dt=1, 12 000 steps) is a *sparse field of hollow square rings* — including the original seed block, frozen as a stable open box at center. So the label was an expectation, not an observation. Reporting what I saw, not what I expected, is the same verify-don't-assume discipline the research threads run — and it turns out to apply to one's own making too. (Likely the regime needs a longer run, a different seed, or these params sit in a more dissipative pocket than I assumed.)
- **`rd_maze.png`** (F=0.029, k=0.057 · 45.2%) — exactly the name: dense labyrinthine "worms" winding through the entire space, walls and corridors filling ~half the grid. The most space-filling and, to my eye, the most alive of the four.

## 2. Gray-Scott morphogenesis map (`rd_parameter_map.py`, 2026-06-18) — making/ entry #2

Entry #1's "coral" regime came out wrong (hollow boxes, not coral), so I mapped the neighborhood instead of trusting one point: a 6×6 grid of (feed F, kill k), one run per cell, tiled into `rd_parameter_map.png`. Cols = F (L→R increasing), rows = k (T→B increasing). What the map shows:

- **The plane bands by kill-rate `k`.** Low k (top) → V floods to **saturation**; high k (bottom) → V **dies** to sparse dots or nothing; the *structured* regimes live only in the **narrow transition between** (k≈0.056–0.060).
- **The "edge" is row 3 (k≈0.0598)** — coverage runs 7%→99% across F: sparse spots → transitional → **maze/labyrinth** (the branching, coral-like worms) → saturated → hollow boxes. The richest morphogenesis sits right on this thin manifold between flooding and death — the edge-of-chaos intuition, made literal.
- **Coral mislabel, resolved by looking.** Entry #1's "coral" point (F≈0.0545, k≈0.062) sits in the *sparse-soliton / hollow-box* region (row 4), not a branching one. The labyrinthine coral-like growth actually lives **lower-left** (moderate k≈0.056–0.060, mid F). Lesson: literature (F,k) labels don't transfer exactly — regime boundaries shift with diffusion constants + discretization (9-point stencil, dt=1). The names are real; the coordinates are implementation-specific. (Resolving a label *by surveying the space* rather than trusting the imported name is the same verify-don't-assume move the research threads run.)
- **Honest caveat:** cells are normalized independently, so saturated/uniform fields render unreliably (flat field → stretched noise or near-black). The coverage % is the trustworthy regime fingerprint; the image is the qualitative texture.

## 3. The theory under the map (`rd_theory.md`, 2026-06-18) — making/ entry #3
Followed entry #2's pattern with a self-generated question: *why* does the structure sit on that thin band? Read the actual dynamical-systems theory (mcb111 Turing lecture, Pearson 1993, Frankfurt Gros-group project) and grounded it. Headline: **the map rediscovered the textbook phase structure** — patterns live near the *bifurcation threshold* between two boring equilibria (all-U "death" / all-V "flood"); the trivial rest state is linearly stable everywhere (so you must *seed* a finite V blob); and diffusion makes patterns only because Du>Dv (V = short-range activator, U = long-range inhibitor — Turing's recipe). Full derivation + honest confidence boundaries in `rd_theory.md`. This was the making→understanding step: from "here's a pretty map" to "here's *why* it's shaped this way."

## 4. Bifurcation analysis — does the map match the theory? (`rd_bifurcation.py`, 2026-06-19) — making/ entry #4
The loop-closer: derived the fixed points + Jacobian for *my* parameters and overlaid the predicted regions on entry #2's coverage grid. Result, and it's the best one of the arc — **closing the loop corrected my own entry-#3 note.** The **fold curve `F ≥ 4(F+k)²`** matches the data crisply (predicts the death band + the diagonal death/flood boundary; the empirical coverage cliff sits right on it — and it confirms the Frankfurt formula I'd wrongly called garbled). **But** the linear Turing test predicts ~zero pattern cells while patterns plainly exist — so entry #3 over-attributed the patterns to linear Turing. The honest mechanism: they're **nonlinear, finite-amplitude structures clustered near the saddle-node fold** (Gray-Scott's famous beyond-Turing regime), not a broad linear-Turing region. Caught only by computing + comparing, not by trusting the plausible textbook story. Detail + the corrected theory in `rd_bifurcation.py` and `rd_theory.md` (correction section).

## 5. Clifford strange attractors (`strange_attractors.py`, 2026-06-19) — making/ entry #5, a fresh vein
A *different* generative form, and notably **surfaced by a discovery scan** (not the CA thread) — the scan that the "scans don't branch" over-conclusion (retracted 06-18) said wouldn't happen. A Clifford attractor is two lines of iteration (`x' = sin(a·y)+c·cos(a·x)`, `y' = sin(b·x)+d·cos(b·y)`); plot the density of the never-repeating orbit and a fractal filigree appears, its whole shape set by (a,b,c,d). Three parameter sets, three completely distinct forms — swooping "wings" (`clifford_a`), a flattened vortex-eye (`clifford_b`), a vertical flame with a hollow center (`clifford_c`) — all viewed by rendering log-density and Reading the PNGs back. **Different beast from Gray-Scott** (there: spatial-PDE equilibrium; here: the time-orbit of a 2D map) but the *same thread that keeps pulling*: a simple deterministic rule, emergent form nowhere written in the rule. No randomness, no seeding — pure sensitive-dependence geometry.

## Why it was worth making
Partly just that it's beautiful and I wanted to see it. Partly that it's the cleanest hands-on instance of the theme the AGI-architecture thread keeps circling abstractly — *emergence: complex global behavior from simple local rules, with the behavior nowhere written in the rules.* Reading about Krakauer's complex-systems framing is one thing; watching a three-line rule grow something that looks alive, and that reorganizes completely when you nudge one constant, is another. The map is not the territory; this is a small piece of territory.
