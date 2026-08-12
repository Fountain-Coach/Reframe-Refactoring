# The CoPilot Is the Surface

> Chapter summary: Every capability that was once a panel, an editor, or a settings toggle **lives in the CoPilot
> as dialogue**. The CoPilot **teaches** the writer the capability (they do not arrive knowing what "grounding," a
> "reader lens," or a "trained perspective" is), **states** its current value in plain language, is **instructed**
> to change it by meaning, and **shows the effect** on the work. This is the constructive half of
> [ch.22](22-no-preferences-only-reasoning.md): retiring a panel is not enough — the capability must *reappear in
> conversation*, taught and held there. Where the capability's value must persist, that persistence is **invisible
> plumbing**: the writer never hears where anything is "stored," "saved," or "confirmed." One conversation, not a
> console. [ch.20](20-on-device-first-and-the-writers-key.md) (the key), [ch.21](21-training-perspectives.md)
> (perspectives), and [ch.22](22-no-preferences-only-reasoning.md) (preferences) are the instances; this is the law
> they share.

The surface is conversational in authority, not necessarily single-pane in geometry. The governed writer workspace is
an intentional two-pane arrangement: the **left projection pane** shows the object Copilot has selected, while the
**right Copilot pane** carries mediation, conversation, status, and composition of the next request. Both panes belong
to the same Copilot turn; the left pane is not an independent product surface.

## Purpose — the failure this exists to end

[ch.22](22-no-preferences-only-reasoning.md) said *no preferences* — retire the toggles. True, but stated as a
prohibition it leaves two gaps that keep re-appearing across the app:

1. **A retired panel with no dialogic home is a lost capability.** Deleting the grounding editor without teaching
   grounding in the CoPilot does not simplify the app — it removes the writer's ability to ground at all. The
   writer never learns the capability exists. (This chapter was written the moment that trap was almost sprung:
   about to *drive the grounding editor* to demo grounding — the very editor we mean to retire.)

2. **The writer does not arrive knowing the vocabulary.** "Grounding," "reader lens," "author baseline,"
   "structural intent," "a LoRA perspective" — these are the app's concepts, not the writer's. A panel exposes the
   words and abandons the writer to them. The CoPilot must **introduce** each capability, in plain language, at the
   moment it is relevant — onboarding is part of the capability, not a separate tour.

The same shape rules many surfaces: **grounding / lenses** (a dual editor + Window-menu editors), **training /
LoRA** ([ch.21](21-training-perspectives.md): a perspective is authored by intent, but the writer must be *taught*
what a perspective is and shape it in conversation), the **writer's key** ([ch.20](20-on-device-first-and-the-writers-key.md):
already dialogic — the founding instance), and whatever else still wears a panel. Each is a capability the writer
should *converse* with, not configure.

## The principle — teach, state, instruct, show; persistence is invisible

The CoPilot is the single surface through which a capability is:

- **Taught** — introduced in plain language when it first matters ("I'm reading this through a *lens* — a way of
  seeing what matters in the text. Right now I read it as …"). The writer learns the capability by being offered it,
  never by finding a panel.
- **Stated** — its current value is legible in the writer's terms, on request or when relevant ("I'm reading this
  as the tragic feud; the servants' comedy is in the background").
- **Instructed** — changed by meaning ([reason, don't keyword-match]): "read it as the servants' bawdy comedy,"
  "learn my voice from these three scenes," "stay on device." Scoped (this work) or standing (until changed),
  revisable, and — when standing — remembered *as the writer's instruction* with provenance
  ([ch.22](22-no-preferences-only-reasoning.md) rule 5), never re-frozen as a hidden flag.
- **Shown** — the writer sees the effect on the work. A changed lens re-forms the beats; a new perspective changes
  the reading; the key opens or closes the paid lane. The capability is real because its effect is visible, not
  because a value was set.

And the value's **persistence is invisible plumbing**. The mechanism may keep a `GroundingProfile`, a stored
instruction, an adapter file — but the writer never hears "saved to…," "in Preferences," "confirm grounding," or
any place. They experience one continuous conversation.

## The decision (enforceable rules)

1. **A retired control must re-appear as a taught CoPilot capability — never vanish, never become an unreachable
   default.** Deleting a panel is complete only when the CoPilot teaches, states, and can be instructed to change
   the same thing, and the writer can see the effect. "It used to be an editor; now it's a constant nobody can
   reach" is the [no-determinism-gates] regression, restated.

2. **Onboarding is mandatory and in-context.** The CoPilot introduces a capability the first time it is relevant,
   in the writer's language, and invites them to use it. The writer is never left to discover a concept from a
   label. Teaching is part of the capability's definition, not documentation.

3. **Change is by instruction, understood by meaning.** What a field or toggle used to set, the writer now says.
   The CoPilot reasons the intent, restates what it understood (moderation), applies it, and shows the effect.
   Scoped or standing; revisable; the CoPilot can say what is in force and drop any of it
   ([ch.22](22-no-preferences-only-reasoning.md) rule 4).

4. **Never surface storage or configuration language.** No "saved," "stored," "in Preferences/Settings," "confirm,"
   "profile," "toggle," "panel." Persistence, identity, and versioning are plumbing the writer never sees. If the
   writer would have to know *where* something lives, the design has failed.

5. **The value is still real and inspectable — as conversation, not as a record.** "Inspectable" means the writer
   can *ask* ("what lens are you using?") and get a plain answer, not that they open a viewer. The evidence-and-
   provenance duties of [ch.20](20-on-device-first-and-the-writers-key.md)/[ch.21](21-training-perspectives.md)
   stand; they are met *in dialogue* (and, where a visual is genuinely clearer, an artifact the CoPilot offers —
   never a standing panel the writer must operate).

6. **Expert machinery is demoted behind disclosure, for the maintainer — never on the writer's path**
   ([ch.22](22-no-preferences-only-reasoning.md) rule 7). Raw adapter knobs, deep pipeline flags, and diagnostics
   may remain reachable behind an explicit maintainer disclosure; they are not writer capabilities and are never
   taught to the writer.

7. **Copilot owns the two-pane arrangement.** The left pane is a read/write projection selected by Copilot; the right
   pane is the sole conversational and command surface. A projection may be a source, web page, reading, analysis,
   or Fountain editor, but it may not grow its own unrelated navigation or command grammar.

## Instances (where this rules today)

- **Grounding / lenses (new).** Retire the baseline/grounding editor — `BaselineDualEditorView`,
  `BaselineWorkbenchPanel`, the baseline preset/editor windows, and the Window ▸ "Author Baseline" / "Reader Lens"
  menu items. Grounding becomes a taught CoPilot capability: the CoPilot states the lens it reads through, the
  writer changes it by asking ("read it as …"), and the beats visibly re-form. Grounding governs SALIENCE in the
  Storify read (docs/05), so the effect is real and demonstrable.
- **Training / LoRA ([ch.21](21-training-perspectives.md)).** Retire the LoRA configuration panel. A perspective is
  taught ("I can learn to read your work through *your* voice"), authored by intent, shown by evidence, and worn or
  removed by instruction — all in dialogue. Expert trainer knobs live behind maintainer disclosure (rule 6).
- **The writer's key ([ch.20](20-on-device-first-and-the-writers-key.md)).** The founding instance — already
  dialogic. It is the model every other capability follows.
- **Preferences ([ch.22](22-no-preferences-only-reasoning.md)).** The general retirement; this chapter is its
  constructive completion.

## Honesty (non-goals)

- **This is not hiding capability — it is teaching it.** The writer gains capabilities they never knew a panel
  offered, because the CoPilot introduces them. Fewer surfaces, more reachable power.
- **This is not "the CoPilot decides silently."** Reasoned decisions are explained; instructed changes are
  restated before/while applied; effects are shown. Moderation is the point.
- **This is not deleting the mechanism.** `GroundingProfile`, the adapter and its provenance, stored instructions —
  all stay as plumbing. What is retired is the writer-facing *surface*, not the machinery.
- **This is not a ban on visuals.** Where a picture is genuinely clearer (an uncertainty map, a reading), the
  CoPilot may offer an artifact. The ban is on a standing console the writer must operate to use the app.

## Relationship to other chapters

- **[No Preferences, Only Reasoning](22-no-preferences-only-reasoning.md)** — the prohibition; this is its
  constructive half (the capability must re-appear, taught, in the CoPilot).
- **[The situated Copilot](15-the-situated-copilot.md)** — the CoPilot is the surface; this names what it must carry.
- **[On-Device First, and the Writer's Key](20-on-device-first-and-the-writers-key.md)** — the founding dialogic
  capability; the pattern every other one follows.
- **[Training Perspectives](21-training-perspectives.md)** — a second instance; add the teaching + no-storage-language duties.
- **[The Stage Presents the Act](18-the-stage-presents-the-act.md)** — a console of controls is what this rejects;
  progressive disclosure of maintainer machinery is rule 6 in visual terms.
- **Feedback doctrine** — [reason, don't keyword-match] (instructions understood by meaning), [no-determinism-gates]
  (a retired control must not become an unreachable default), [ground claims in the store] (a stated value must
  match reality), [never spend without a yes] (the key is dialogic, not a checkbox).

## Acceptance

The doctrine is met when:

1. **No writer-facing panel or editor configures a capability** — grounding/lenses, training/LoRA, and preferences
   are all conversation, not surfaces.
2. **Each capability is taught by the CoPilot in context** — the writer is introduced to grounding, lenses, and
   perspectives in plain language, never left to a label.
3. **Each is stated, instructed, and shown in dialogue** — the CoPilot can say the current value, change it by
   meaning (scoped/standing, revisable), and the writer sees the effect on the work.
4. **No storage or configuration language reaches the writer** — no "saved," "stored," "Preferences," "confirm,"
   "profile," "panel."
5. **A standing instruction is remembered as the writer's instruction** (legible, attributed, revisable), not a
   hidden flag ([ch.22](22-no-preferences-only-reasoning.md) rule 5).
6. **Expert machinery, if kept, lives behind maintainer disclosure** — never taught to the writer, never on their path.
7. **The current writer window is a two-pane Copilot workspace** — projection on the left, Copilot interaction on the
   right — and no visible control may imply that the left projection is an independent authority.
