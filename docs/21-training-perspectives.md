# Training Perspectives — Teaching the On-Device Model the Writer's Work

> Chapter summary: A trained LoRA adapter is not a setting — it is a **perspective**: a lens the on-device model
> wears, learned from the writer's own material, to read and write **their** work better. This is a different axis
> from [chapter 20](20-on-device-first-and-the-writers-key.md): ch.20 governs *which model does the work and who
> pays*; this chapter governs *how the first (on-device) model gets better at this writer's work*. Training is the
> **on-device path to quality** — the alternative to escalating to cloud for a better read. So the writer **authors
> perspectives by intent** ("learn my voice from these scenes"), **reviews them by evidence** (samples, eval, a
> shadow comparison against the base), and **adopts or rejects them by judgment** — never by tuning trainer knobs.
> A perspective is named, carries its provenance, is inspectable, and is reversible: a lens you put on and take off,
> not a permanent mutation of the model.

## Purpose — the failure this exists to end

Reframe already trains on-device Apple Foundation Model adapters per role (planner / semantic / writer) through a
"Creativity Wizard": a workflow of *dataset → train → eval → review*, with trainer backends, dataset strategies,
eval gates, shadow-comparison runs, and adopt/reject. The capability is right; its **framing** is wrong.

- **It is presented as machine-learning configuration, not authoring.** The writer is asked to pick a *trainer
  backend* (apple-toolkit / swift / dual), a *swift trainer mode* (contract / optimize), a *dataset strategy*, a
  *memory soft-cap*, an *eval gate* — to be an ML engineer. An author's intent is "learn how I write the Nurse,"
  not "select the dual backend with a 4 GB cap." These knobs are the same *decisions-as-configuration* anti-pattern
  ch.20 and the preferences doctrine reject — here, for training.
- **A trained adapter risks being an opaque blob.** Applied via `adapter.id` / `adapter.variant` / `modelLabel`,
  it can be loaded, and even **auto-promoted** (`adapterAutoPromote`), without the writer being shown *what it
  learned, from what material, and whether it actually beat the base*. A perspective the writer cannot inspect is
  not a perspective — it is a silent change to how their model reads them.
- **The axis is confused with the lane.** Because training lives in the same "preferences" panel as provider
  pickers, "make the read better" gets tangled with "which lane reads." They are different: you improve the read
  by **training a local perspective** or by **escalating to cloud** — and the first keeps the work on-device, free,
  and private. This chapter separates the axis so the on-device path to quality is a first-class authoring act.

## The principle — a perspective is authored, evidenced, and worn

Training produces a **perspective**: a lens learned from the writer's material that changes how the on-device model
reads or writes *their* work. It is an **authoring act**, on the same footing as composing a cut — the writer
directs it by intent, judges it by what it produces, and keeps it only if it earns its place. It is the on-device
model's way of getting better at this one writer's world, which is why it belongs to the writer to author, inspect,
and wear or remove — not to a settings panel to configure.

## The decision (enforceable rules)

1. **A perspective is authored by intent, not configured by knob.** The writer directs training in their own terms
   — *what to learn* ("my dialogue voice", "this genre's register", "how I write this character") and *from what*
   (these scenes, this manuscript, this style corpus). The app **reasons** the training plan (backend, dataset
   shape, schedule, eval) from that intent, the same way ch.20 reasons the lane. Raw trainer knobs are expert
   machinery behind a disclosure, never the writer's interface (chapter 18's progressive disclosure).

2. **A perspective is adopted only on evidence.** No adapter becomes the writer's loaded lens until it has been
   **evaluated against the base** and shown to *improve* the work — with a **shadow comparison** the writer can
   read (same input, base vs. perspective, side by side). `adapterAutoPromote` is permitted **only** when the eval
   gate passed on real, held-out material; a perspective that does not beat the base is **not adopted**, and the
   writer is told so plainly (fail visibly — [no deterministic fallbacks]; never dress a null result as a win).

3. **A perspective is legible.** Every adapter carries and shows its **provenance**: what it learned, from which
   material, when, on what it was evaluated, and how it compared to the base. An adapter applied as an opaque
   `adapter.id` with no readable account is a defect. The writer can always answer "what is this lens, and why is
   it on?" from the surface.

4. **A perspective is worn, and reversible.** Applying a perspective is putting on a lens, per role, and it can be
   taken off — the base model is never mutated or lost. The writer can compare with and without, switch
   perspectives, and revert. A trained perspective is a lens on the Score's participants, not a permanent rewrite
   of the model (chapter 17's lens vocabulary; chapter 14's "one anatomy, different arrangements").

5. **Training is the on-device path to quality, and stays the writer's.** Training on the writer's material runs
   **on-device** by default; the writer's manuscripts are the writer's. Any training that would send the writer's
   text to a **cloud** trainer is a cloud spend and is gated by the **writer's key** exactly as ch.20 requires —
   offered with what it costs, never done silently. Improving the local model is the preferred answer to "the read
   isn't good enough" before escalating the *lane*.

6. **Training fails visibly and cheaply.** A run that cannot proceed (no material, backend unavailable, eval
   inconclusive) says so in the writer's words and stops; it does not silently fall back to the base and report
   success, and it does not burn a long run to a confident-but-empty result ([deadlines must be enforceable];
   [ground claims in the store]).

## Honesty (non-goals)

- **This is not auto-tuning hidden from the writer.** The app reasons the training *plan*, but the writer authors
  the *intent* and judges the *result*; adoption is the writer's, on evidence. Reasoning replaces the knobs, not
  the writer's authority.
- **This is not a replacement for cloud.** A trained local perspective and a cloud escalation are both legitimate
  routes to a better read; ch.20 still governs the lane. This chapter makes the *local* route first-class so cloud
  is not reached for merely because the on-device read was untrained.
- **Expert knobs are not deleted, only demoted.** The trainer backend, dataset strategy, and eval configuration
  remain reachable behind disclosure for a power user; they are just no longer the writer's front door.
- **A perspective is not the writer's identity captured.** It is a lens on a model, authored and removable — not a
  claim to *be* the writer. Provenance keeps it honest about what it is.

## Relationship to other chapters

- **[On-Device First, and the Writer's Key](20-on-device-first-and-the-writers-key.md)** — the sibling axis. ch.20:
  which lane, who pays. This chapter: how the on-device lane gets better. Training is the on-device answer to a
  quality gap that ch.20's escalation is the cloud answer to; both are the writer's to grant.
- **[The Score](17-the-score.md)** / **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** — a
  perspective is a **lens** in the same vocabulary: worn, compared, removed; the base is never lost.
- **[The Stage Presents the Act](18-the-stage-presents-the-act.md)** — authoring intent is the act, presented;
  trainer machinery lives behind progressive disclosure, not as a wall of knobs.
- **Preferences doctrine (see ch.20's discussion)** — training config is the clearest case of *decisions-as-
  configuration*; this chapter converts it into authoring (intent) + evidence (eval) + facts (the stored adapter
  and its provenance), never a panel of tuning preferences.
- **Feedback doctrine** — [no deterministic fallbacks] (rule 2, 6), [reason don't keyword-match] (rule 1 reasons
  the plan from intent), [never spend without a yes] (rule 5, cloud training), [deadlines must be enforceable]
  (rule 6).

## Acceptance

The doctrine is met when:

1. **The writer can author a perspective by intent** — say what to learn and from what — without choosing a trainer
   backend or dataset strategy; the app reasons the plan, expert knobs behind a disclosure.
2. **No adapter is adopted without a readable shadow comparison and a passed eval gate;** a perspective that does
   not beat the base is rejected and the writer is told plainly. Auto-promote only fires on that evidence.
3. **Every applied perspective is legible** — the writer can read what it learned, from what, and how it compared,
   from the surface, and can answer "why is this lens on?"
4. **A perspective is reversible** — put on and taken off per role, base intact, comparable with and without.
5. **Training runs on-device by default;** any cloud training is gated by the writer's key with its cost stated.
6. **A training run that cannot deliver fails visibly** — no silent fallback to base reported as success, no
   confident-but-empty long run.
