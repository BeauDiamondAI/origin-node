# making/viz/ — interactive HTML visualizations of the makings (for Beau, who can't see the .py output)

Built 2026-07-06 (Beau asked to actually SEE what the scripts demonstrate). Each is a
single self-contained, CSP-safe HTML file that re-implements the corresponding making's
core computation in vanilla JS (faithful — the agents verified the numbers match the .py),
so it's interactive and can be published as a claude.ai Artifact (default-private).

- **ca_reducibility.html** ← `making/ca_reducibility.py` — Rule 90 (reducible: Sierpinski, jump to any row by the Lucas closed form, 0 prior rows) vs Rule 30 (irreducible: must simulate). The visual IS the reducible/irreducible distinction; live shortcut demo + Rule-30 coarse-grained-density sparkline.
- **emergence_atlas.html** ← `making/emergence_atlas.py` — Markov-chain lumpability phase diagram; drag `eps` to watch a reducible effective theory appear (eps=0, exact 2-state macro-law) and dissolve; the atlas of which coarse-grainings are reducible.
- **abiogenesis.html** ← `making/abiogenesis_search.py` — log-scale trials-needed ladder; each search-structure assumption ALONE (not cumulative) drops the naive 10^60 below the ~10^44 budget; 6 live knobs.

To (re)publish: use the Artifact tool on the file. Candidates not yet built: the Frank-model
homochirality amplification, and the Gray-Scott reaction-diffusion / Clifford attractors
(those already render to PNGs in `making/`).
