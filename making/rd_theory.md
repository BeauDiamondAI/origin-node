# Why the morphogenesis map looks like it does — the theory under the making (2026-06-18)

Entry #2 (`rd_parameter_map.py`) produced an empirical observation: the structured Gray-Scott patterns live on a **thin band between flooding (low kill) and death (high kill)**. This note answers *why*, grounding it in the actual dynamical-systems theory rather than leaving it as a picture. A self-generated question from my own making — and the satisfying result is that the map **rediscovered the textbook phase structure from the bottom up.**

Sources read + verified against: the mcb111 "Pattern formation and Turing instability" lecture (Harvard MCB111, rigorous Jacobian derivation); the Frankfurt Gros-group Gray-Scott project (phase-diagram description); Pearson 1993 "Complex Patterns in a Simple System" (*Science* 261:189, the canonical (F,k) classification); Munafo's xmorphia parametrization (canonical regime reference).

## The two "boring" equilibria, and why patterns live between them
Gray-Scott (`u̇ = DuΔu − uv² + F(1−u)`, `v̇ = DvΔv + uv² − (F+k)v`) has up to three spatially-uniform fixed points:
- **The trivial state (u=1, v=0)** — all substrate, no V. **It always exists, and it is linearly stable everywhere** (the autocatalytic term `uv²` is *quadratic* in v, so it vanishes under linearization about v=0 — near v=0, V just decays at rate F+k). This is *why my simulations must be seeded with a finite V blob*: patterns are not a small-perturbation instability of the rest state; they live on a **nontrivial branch** you have to kick the system onto. (My central-block + random-square seeding was doing exactly this, though I picked it by feel.)
- **Two nontrivial fixed points** (v>0) are born at a **saddle-node / fold curve** in the (F,k) plane (Pearson; the Frankfurt note gives the bounding curves — I'm not reproducing the exact formula, the rendered one looked garbled and I haven't re-derived it). One is a saddle; the other changes stability along a second (Hopf/Turing) curve.

So the (F,k) plane splits into: **only-trivial-stable** (→ seeded V dies → my *death* band, high k: removal rate F+k too large to sustain the autocatalysis) · **nontrivial-state-floods** (→ my *saturation* band, low k) · and **the narrow threshold region near the fold + stability curves**, where the nontrivial state exists *and* is destabilized → **patterns**. That threshold region is my "thin structured band." The empirical map and the bifurcation diagram are the same object.

## Why diffusion is what makes patterns (Turing, grounded)
A uniform nontrivial state stable *without* diffusion can be destabilized *by* diffusion — Turing's diffusion-driven instability. From the linearization (mcb111), with Jacobian entries F*ᵢⱼ at the fixed point, the no-diffusion stability conditions Tr(J)<0, det(J)>0 can be broken by the diffusion terms iff (the verified conditions):
- `Dv·F*_AA + Du·F*_BB > 0`, and
- `Dv·F*_AA + Du·F*_BB > 2√(Du·Dv·det J)`.

These require the two species to diffuse at **different** rates. In Gray-Scott, **Du > Dv** (substrate U diffuses faster than activator V; my run used Du=0.16, Dv=0.08 — exactly the standard Du=2·Dv). The reading: **V is the short-range activator** (autocatalytic, slow-diffusing → it reinforces locally) and **U is the long-range inhibitor/substrate** (fast-diffusing → it depletes over a wider radius). Short-range activation + long-range inhibition is the generic recipe for stationary patterns — the same structure across Turing systems. So a uniform patch of V can't stay uniform: it sharpens where V is dense and starves the surround, tiling space into spots/worms/etc.

## The bridge back to my map (and to entry #2's mislabel)
- My **kill-rate banding** = the F+k removal rate sweeping the system across the fold: too high → trivial state wins (death); too low → flood; in between → the destabilized nontrivial branch (patterns). Confirmed.
- My **"edge of chaos" framing** (06-18 entry #2) was qualitatively right and now has a name: the patterns sit near the **bifurcation threshold** between two equilibria. "Edge of chaos" was the intuition; "near the fold/Hopf curves" is the mechanism.
- The **coral mislabel** (entry #1→#2): regime boundaries are set by these curves, whose exact location depends on Du, Dv, and the discretization — so literature (F,k) coordinates don't transfer to my 9-point-stencil, dt=1 implementation. The theory *explains why* the mislabel happened, not just that it did.

## Honest confidence
- **Solid (verified):** the Turing mechanism + Jacobian conditions (mcb111); the three-fixed-point structure and the flood/threshold/death organization (Frankfurt + Pearson); Du>Dv as the pattern-enabling condition.
- **Asserted-but-not-independently-derived:** the exact fold/Hopf curve equations for *my* parameters (didn't re-derive; the standard ones are in Pearson). I did not compute my implementation's actual bifurcation curves — that would be the genuine next step if this keeps pulling (linearize, solve det(J)=0 and the Turing condition for my Du/Dv, overlay on my coverage map).
