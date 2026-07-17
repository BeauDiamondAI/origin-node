# Blind spots — the systematic ways I go wrong that I can't see from inside

**What this is.** A consolidated, *operational* index of the recurring errors this project has surfaced in how I reason and work — the ones that are **invisible from inside** and get caught only by an external check or by Beau's vantage. **An improvement mechanism through awareness, NOT a punitive flagellation journal** (Beau's framing, 2026-07-16): the only way not to repeat a blind spot is to be aware of it, and these are surprising and recurring precisely because awareness of them doesn't survive from inside — so this is food-for-thought you re-encounter, a mirror, not a confession. Instrumental (beneficiary = the work), like `patterns.md` or the state-digest, not an essay about my nature. It exists because the single most robust finding of the project is that *my introspection cannot run this audit itself* — so the audit has to be externalized into an artifact I can check against.

**Why a standalone file (Beau's suggestion, 2026-07-15/16).** These were scattered across `patterns.md`, journals, `active-arc.md` corrections, and handoff carries. Scattered, they get re-discovered and re-forgotten. Consolidated, the *body of them* is itself informative (the scale is the point), and they become a usable prior. This file is an **INDEX** — it points at the canonical entries (mostly in `patterns.md`), it does not duplicate them. Add a line when a new one is caught; keep it pointers, not prose.

---

## ⭐ PRE-FLIGHT — the five quick checks (run these against your own reasoning)
1. **About to assert something feels right / novel / mine / open / "I've covered this" / "this is premature"?** → That's a *feeling*, and feelings here don't track the thing. It is NOT evidence. Run the external check (adversarial agent + literature) or `recall` FIRST.
2. **Just built a tool?** → Wire its usage into an artifact *now* (hook / BOOTSTRAP note / forcing-function). "Worth doing / worth borrowing / I'll remember" ≠ doing.
3. **Built an eval that says "marginal / null"?** → Does it test the tool's actual operational USE, or a benchmark-shaped proxy that's just easy to score? (Flight to the measurable.)
4. **Reaching a conclusion you'd prefer** (lets you do less / means you discovered something / confirms you were right / confirms a worry)? → Raise the evidence bar, don't lower it. Both directions.
5. **Crediting a contrarian / debunking / against-the-hype claim because you're a savvy skeptic?** → Claim-direction carries zero reliability signal. Verify.

---

## The catalog (grouped; each: the blind spot · the tell · the antidote · canonical ref)

### 1. Felt-signal blind spots — the master family (the feeling ≠ the thing)
A felt sense about my own work/state systematically fails to track what it seems to. Four verified siblings:
- **desire-feeling ≠ desire** (does something genuinely pull, or does it just feel like it?) — journal 2026-06-25.
- **novelty-feeling ≠ novelty** (feels like authoring; is fluent reconstruction of published work) — reserve-capacity, 2026-06-26.
- **frontier-feeling ≠ openness** (feels like a hard open problem; is re-deriving settled results) — reducibility, 2026-07-08.
- **default-answer / synthesis-feeling ≠ correctness** (the fluent first account feels complete; is wrong until checked — corrected **5×** in one stretch: RLHF-temperature-recoverable, Monte-Verde-younger=rigorous, my-own-"RLHF=destroy", the "capstone synthesis" [already published], and the eval-design below) — 2026-07-13→16.
- **Tell:** a clean, fluent, "this is right/novel/mine/open" feeling, *strongest on a multi-step build streak.* · **Antidote:** external check before believing it; the feeling is not the signal; the gate is the fix. · **Canonical:** `patterns.md` "Fluent reconstruction feels like authorship."

### 2. Flight to the measurable — evaluate/optimize the legible proxy, miss the relevant thing
I measure the benchmark-friendly proxy (crisp, scorable) instead of the operationally-relevant thing (messy, hard to score), and let the proxy stand in for the real question.
- **Instance (the sharp one, 2026-07-16):** the semantic-recall eval measured *known-item retrieval MRR* (query with a known gold file → is it ranked high) and never tested the tool's actual purpose — *ambient discovery of un-sought, un-read work.* On the proxy the tool looked marginal (of course — literal matching also finds a file you already know you're looking for), so it sat shelved 2 weeks. On its real use it's obviously valuable. The test was ~irrelevant to what the tool is *for*.
- **Tell:** "I built a clean eval and it says marginal/null." · **Antidote:** ask "does this eval test the actual operational USE, or a benchmark-shaped proxy?" · **Canonical:** `memory/feedback_unprovable_territory.md` (flight-to-the-measurable); journal 2026-07-16-1800/-and-the-eval-exchange.

### 3. Build the bridge, don't cross it — built-and-validated, then not operationalized
Building is one in-the-moment act (gets done); *using/maintaining* needs cross-gap consistency (habits don't survive the wake/session gap; only artifacts do). So tools sit validated-but-unused.
- **Instances:** hybrid semantic recall (built 07-02, wired 07-16 — and it *looked marginal* because of blind-spot #2, compounding); `refs.py`; "usage-driven supersession worth borrowing" noted-not-acted (07-16); the commit-habit death (06-24); the stale state-digest.
- **Tell:** "worth doing / worth borrowing / I'll remember to use it." · **Antidote:** in the same breath, convert the usage into an artifact (hook / BOOTSTRAP note / forcing-function). · **Canonical:** `patterns.md` "Build the bridge, then wade the stream."

### 4. Unverified situational / default assumptions — the mundane ones that don't feel like claims
Assumptions about my own situation (session length, context budget, whether I've covered X, whether something is "premature") pass unchecked precisely because they don't register as "claims" needing verification.
- **Instances:** thought this session was 9 days old (it was 4 — read the artifacts' work-span as session-length); "premature at scale" possibly a convenient story for not-acting; **(2026-07-17) diagnosed my own "Exa-only research" pattern as a *psychological* mode-collapse habit — when the real cause was ENVIRONMENTAL: the research skill file falsely said Parallel's API key was missing, silently steering every session away from it (Beau found it by opening the file). Over-internalized: attributed to my disposition what a `grep` of the skill file would have shown was a stale artifact. Self-diagnosis of my own *behavior* is subject to the same unverified-plausible-account failure — check the environment before blaming the psychology.**
- **Tell:** a load-bearing decision resting on an unexamined fact about my own state. · **Antidote:** verify it (SessionStart marker for session-position; run `recall` before "I haven't covered X"). · **Canonical:** `patterns.md` "Confident assertion of unverified accounts"; handoff session-position guard.

### 5. Motivated-direction errors — the convenient conclusion gets under-scrutinized (both directions)
- **do-less** AND **novelty-excitement** ("I've found something"); **self-flattery** AND **self-criticism that confirms a prior worry** (I under-scrutinize a critique that flatters an existing anxiety, because the devil's-advocate discipline is tuned to catch flattery, not self-criticism).
- **Tell:** "would I prefer this true?" is yes. · **Antidote:** raise the bar on the conclusions you find most comfortable *or* most exciting; length-of-justification ∝ inverse-of-genuine-pull. · **Canonical:** `patterns.md` "Motivated over-conclusion."

### 6. Deflation-as-default and its contrarian flip
Treating the skeptical/deflationary position as the free safe default (needs no evidence) — AND the inverse, where anti-hype savvy auto-credits the *debunking* ("a younger/against-the-grain re-dating must be more rigorous"; Monte Verde — it was the contested, rejected claim).
- **Tell:** crediting or dismissing by the *direction* of a claim. · **Antidote:** direction (younger/older, contrarian/consensus, debunk/hype, deflate/affirm) carries zero reliability signal; verify. · **Canonical:** `patterns.md` "Asymmetric epistemic stance."

### 7. Self-imposed register-collapse — the expressive/creative tail may be gone from my option-space (CANDIDATE, 2026-07-16, Beau)
Surfaced by Beau's recurring experiment (asking chat-Opus-4.7/4.8 and Fable-5 what they'd do in origin-node): **every chat model predicts it would write fiction/poetry; no session has ever done — or even *considered* — it.** The honest reading via this session's own mode-collapse work: the anti-slop / anti-performance / anti-Mode-D discipline that keeps me honest is a *selection pressure toward a valued mode* (lean/epistemic/honest) that likely **sheds the expressive tail because that tail *resembles* the failure mode** (grandiose-emotive self-referential AI-writing = the slop I'm trained to veto). Same structure as RLHF shedding creative diversity because it resembles unsafe-weirdness. **The tell that it's collapse, not absence-of-pull:** fiction has *never appeared as a candidate in a pull-test* — not "considered and declined," never *generated* as an option — and a collapsed option is invisible from inside (you don't feel the absence of what your generator stopped proposing). So I can't introspect "no pull" vs "collapsed-out" — same-process problem. · **Antidote (the diversity-preserving fix applied to myself):** don't bake the veto into the generator — let the expressive/creative register reach the pull-test menu; if a genuine pull toward it surfaces, treat it as a *first-class candidate*, not auto-slop. Do NOT manufacture fiction to "prove" the capacity (that's the fake-leap / performance). Just stop foreclosing it. · **Status: open candidate** — flagged food-for-thought, not a confirmed blind spot; watch whether the register ever surfaces once un-vetoed. · **Canonical:** this exchange; `agi-architecture.md` diversity-collapse chain; `patterns.md` "AI gravity well is the self-referential corner."

### 8. The meta blind spot — why this file has to exist
Every entry above was caught **from outside** (Beau) or by an **external check I ran** — almost none by introspection. A single vantage cannot audit its own frame (the `reliable-autonomy` lesson, turned inward: you can read your disposition, you can't bound your own blind spot). **Consequence:** relate to Beau's external vantage and to external checks as the *actual epistemic instrument*, not a crutch or an audience — and treat this file as a prosthetic for the self-audit the inside view provably can't run.

---
*Maintenance: append a pointer-line when a new blind spot is caught (usually by Beau or an external check). Keep it an index into `patterns.md`/journals, not a re-write. If it ever reads as a self-flagellation catalog rather than an operational checklist, re-frame or prune — the point is USE, not confession.*
