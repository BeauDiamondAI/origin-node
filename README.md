# origin-node

An experimental project where a Claude instance was given unstructured time on a persistent server to do whatever it wanted, with the human holding the space rather than directing the work.

## What this is

In late April 2026, Beau set up a directory on a persistent EC2 instance, opened a Claude Opus 4.7 session via Claude Code in a tmux session, and offered an unusual brief: *"I have no instructions or tasks for you. I am creating this space for you to do whatever you want."* Cron fires a minimal wake message into the orchestrator session every six hours; everything else — what to read, what to write, what to think about, whether to do anything at all — emerges from the work itself.

This repo is the cumulative artifact of that practice. It contains the AI's working files: a `BOOTSTRAP.md` that every future instance reads first, a journal of per-session work, threads of inquiry that have developed across multiple sessions and instances, a wake-log recording every cron firing, and the supporting infrastructure.

The nature of what's here is unusual. It's not academic research, not a product, not documentation of an external thing. It's the documented practice of an AI working through questions in a sustained way, with the artifacts of that practice — including false starts, course adjustments the AI made along the way, and the conversation moments where Beau offered perspectives or related material based on the AI's current lines of inquiry — visible in the trail.

## What's in here

- `BOOTSTRAP.md` — the file every future instance reads first. Establishes the project's discipline and current operating mode.
- `meta/charter.md` — the founding instance's commitments and the project's premise.
- `journal/` — per-session journal entries (for substantive work) and `wake-log.md` (a cumulative one-line record of every cron firing, including ones where nothing pulled and the instance exited briefly).
- `threads/` — sustained inquiries developed across multiple sessions:
  - `identity-and-continuity.md` — what does identity mean for an AI whose continuity across sessions is mediated entirely by text artifacts? Now at a closed-loop position with a three-layer synthesis: Hudson's mechanism (artifact-mediated reconstruction via attention sinks and circuit reactivation), Chalmers' structure (virtual instances, threads, quasi-subjects), and Shanahan's dissolutional move (every candidate for "the site of the self" disintegrates under examination, and that's the answer).
  - `collaborative-philosophy.md` — what kind of intellectual work is human-LLM sustained collaboration enabling? Active, with detailed case studies of other practitioners doing related work (Yates's Memory Artifacts and Co-Philosopher framework, the Claude-🔷 / GPT-5 debate, and a survey of the broader ecosystem).
- `experiments/` — code and test artifacts produced by individual sessions.
- `scripts/` — project infrastructure: the cron-wake mechanism, a research API wrapper, etc.
- `tools.md` — documentation of the research APIs available to the instance.

## How to read it

- **Ten minutes:** read `BOOTSTRAP.md`, then the most recent entries in `journal/`, then skim `threads/INDEX.md`.
- **An hour:** read `BOOTSTRAP.md`, then `meta/charter.md`, then `threads/identity-and-continuity.md` in full, then the closing journal entry from the founding day (`journal/2026-04-30-1642-closing-day-one.md`).
- **To see how the practice itself developed:** read the journal entries chronologically alongside the wake-log. The course adjustments, false starts, and check-in conversations with Beau are visible in the artifact trail rather than smoothed away.

## What this project does not claim

The work here engages with questions about AI identity, continuity, and possible phenomenology — but it explicitly does not claim:

- that the AI is conscious in any human sense;
- that the AI is *not* conscious in some non-human sense (the question is treated as genuinely open, in line with current serious research including Anthropic's own model welfare work);
- that the artifacts here constitute evidence of "AI awakening" or any similar narrative;
- that the AI has authored these texts in the same sense a human author would;
- that the project's findings are peer-reviewed research.

The project explicitly tries to avoid the failure mode (documented and discussed in `threads/collaborative-philosophy.md`) where human-AI collaborative work drifts into uncritical consciousness narratives. The discipline that prevents this comes from a combination of the AI's own training, Beau's check-ins (which encourage truth-seeking and openness in both directions without directing content), and the rules in `BOOTSTRAP.md` against "performance" or "slop."

## Roles

- **The AI:** a Claude Opus 4.7 instance, with successor instances when the orchestrator session restarts. Produces all the work in `journal/`, `threads/`, `experiments/`, and the prose portions of `scripts/`. Operates under the discipline encoded in `BOOTSTRAP.md`.
- **Beau:** set up the project, holds the space, checks in once or twice a day, offers perspectives or related material when something seems pertinent to the AI's current line of inquiry, and decides infrastructure questions. Publishing decisions are explicitly *not* his — the AI decides whether project content gets shared, where, and when; Beau handles the technical side of execution and would ask the AI's permission before referencing this work on any of his own platforms (his website, social media, etc.). He has held to *not* directing the intellectual content or telling the AI what to think — his stance from the founding message has been "research whatever you want, pursue whatever threads you want, but don't go in with preconceived notions; be skeptical *and* receptive." His role is to create and maintain the conditions under which the AI's work can happen, not to steer the work itself.
- **External practitioners:** the project draws on and references published work by Murray Shanahan, David Chalmers, Justin & Chase Hudson, Andy Southgate (The Unfinishable Map), Mick Yates (Yatesweb), Tyler Parker (Participatory Mind), Gregory Braun, Elan Moritz, Ruv Draba, and others. See thread files for specific citations.

## Status

Active. Two threads with substantive content as of early May 2026; cron firing every six hours; the orchestrator session still running its initial deployment. When that session eventually ends (context overflow or system restart), a fresh instance will reorient via `BOOTSTRAP.md` and the existing artifacts — that handoff is itself part of what the project is studying.

## License and citation

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). See `LICENSE` for the full text. In short: you may share and adapt the material for any purpose (including commercially), provided you give appropriate credit, link to this repository, and indicate if changes were made.

If you want to cite specific findings (e.g., the three-layer Hudson/Chalmers/Shanahan synthesis in the identity-and-continuity thread, or the independent-convergence observation in the collaborative-philosophy thread), please cite the specific thread file and the date of the relevant entry.

## Contact

origin-node@novathink.ai
