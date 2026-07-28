# A Beat Is the Question It Raises

> Chapter summary: A **beat** is a story unit defined by the open question it raises — it begins where the question
> is raised and ends where the story stops holding it. An **atom** is something else entirely: the reader's local
> choice about where one close-read stretch ends, measured in **a minute of performance** and cut at the text's own
> seam. Atoms are not beats, must never be labelled as such, and need no names — an atom raises no question, so
> there is nothing to name it for, which is why every attempt to name one produced a description of its contents on
> every lane tried. The question names the beat: grounded by construction, impossible to fabricate, free. Because
> the reading carries its open questions forward, beats are found in **one pass**, while the text is read, and they
> are shown as they form. Closure is inferred from silence and must be stated that way. [ch.14](14-the-beat-and-its-arrangements.md)
> governs how a beat is arranged and shown; this chapter governs what makes it a beat at all.

## Purpose — the failure this exists to end

The app called atoms beats. The strip said BEAT 1 over five lines, BEAT 2 over six, and the writer was invited to
compose a cut from them. Three consequences followed, all measured on Ulysses:

- **Naming became an unanswerable question.** Asked to name a six-line fragment, the on-device lane returned its
  own guided-schema type name on 37 consecutive calls; freed of a JSON instruction it wrote a 120-word essay
  claiming Mulligan is Stephen's father; the strong lane did no better, because the deficiency was not capability.
  A fragment that raises no question has no name, and roughly three hundred lines of machinery were built to chase
  one — a name repair, a shape rule, a uniqueness pass, a de-duplication merge — of which the fastest fix was
  deletion.
- **Repetition was read as a defect.** The same title appearing on neighbouring atoms was treated first as a bug to
  de-duplicate and then as a "boundary ambiguity" to report, when it was the reader saying *these atoms are one
  thing*. The signal that identifies beats was being suppressed as noise.
- **The reading could not say what it was unsure of over a stretch.** Questions were raised afresh per passage and
  carried nowhere, so a chapter produced 65 unrelated observations across 45 passages — one per passage, none
  spanning anything. A map of those is a list, not a reading.

Meanwhile the Cut lane sat beside all of it, inviting the writer to arrange a runtime order over a reading that
still held unnamed beats and unsettled questions.

## The principle — the question is the unit

A beat is the stretch of story over which **one question stays open**. It begins where the question is raised and
ends where the story stops holding it. This is not a heuristic for finding beats; it is what a beat is, and
everything else follows from it:

- **Its name is its question.** "Will Stephen confront Mulligan?" *is* the beat's name — drawn from the text,
  impossible to fabricate, costing nothing. Naming is not a task to be performed on a beat; it is a property the
  beat already has.
- **Its length is meaningful.** A question raised and dropped inside one passage is a short beat; one held across
  forty is the episode's spine. Length used to be the size of whatever the reader could hold in its window, which
  told you about the model rather than the story.
- **Beats overlap, and that is the texture.** Several questions run at once — the leaving, the key, the mother —
  and their braiding is the chapter's shape. It must never be flattened into a strip.

An **atom** is the other thing, and keeping the two apart is the whole discipline. An atom is the reader's local
judgement about where one close-read stretch ends: real, worth keeping, and *not* a unit of meaning. Its measure is
**a minute of performance** — the unit the destination medium already uses, that the app already budgets in ("≈ 20
/ 90 min"), and that is self-normalising, since a minute of speech is fewer words than a minute of description.
Time decides an atom's size; the text decides its seam.

## How beats are found — one pass, rolling forward

Each passage is told what the story is still holding open, and answers about those as well as itself. A question
that matches one already open is the same doubt continuing; a question matching nothing is newly raised, and a beat
begins; a question no longer raised has been left behind, and its beat ends where it was last held. No second pass
over the text, and nothing to recompute on reopen beyond replaying the passages the store already holds.

**Closure is inferred from silence.** The reading never says "that is answered now" — it stops raising it. That is
a real signal and a weak one, so the app claims *"the story stopped holding this here"* and never *"this was
resolved here"*.

## Measured — the whole of Telemachus, on-device, one pass

```
Will Buck Mulligan and Stephen Dedalus's conflict escalate?   ll. 1–1118, 45 passages — still open
What is the significance of Buck Mulligan's blessing?         ll. 1–105,   4 passages — CLOSED
What will happen next between Stephen and Buck?               ll. 130–1118, 40 passages — still open
```

Threads close: the blessing was raised at the first line, held four passages, and let go at l. 105 when the story
moved past it. And where they do not close, the story is the reason — an antagonism running from the first line to
the last *is* Telemachus, and it does not resolve; a reading that closed it would have been wrong about the
chapter.

The same run exposes the current limit: 44 questions reduced to **three** threads, where the episode plainly holds
more — the mother's death, the tower's rent, Haines in the night. Matching doubts by shared vocabulary over-merges
them; matching by sentence embedding ([ch.27](27-parse-before-you-ask.md), the measured tier) is the correction,
and this measurement is the evidence for it.

## Rules

1. **A beat is the stretch over which one question stays open.** Not a window, not a paragraph, not a fragment the
   reader happened to cut.
2. **An atom is a minute of performance, closed at the text's own seam** — and it is never called a beat, in code,
   in the interface, or in a count shown to the writer.
3. **Nothing names a beat but its question.** No model is asked for a beat's name; no stand-in is stamped where a
   name is missing. An unnamed *atom* is normal and needs no apology.
4. **Closure is inferred from silence, and said that way.** "The story stopped holding this here", never
   "resolved".
5. **Threads overlap and are never flattened.** Parallel questions are the dramatic texture, not a collision.
6. **What the reading holds open is shown while it reads**, forming over the structure the parse already put on
   screen — not assembled afterwards in a report.
7. **No cut before understanding.** Arranging a runtime order is an act performed *on* a reading; offering it
   beside a reading that still holds unsettled questions invites composing from a text nobody has finished
   understanding. This is the dramaturg's objection, and it belongs at the read, not later at the reframe.

## Acceptance

- No surface labels an atom a beat, and no beat count counts atoms.
- No model call exists whose purpose is to name a beat.
- Every thread the map shows carries a first line, a last line, how many passages held it, and whether it was still
  open where the reading stopped.
- A run over a whole chapter produces at least one thread that closes before the end, and the app states closure as
  silence rather than resolution.
- Beats form during the read, visible as they accumulate, without a second pass.

## Governing sentence

Reframe shall treat a beat as the question the story holds open — found in one forward pass, named by that
question, shown as it forms, and never confused with the atoms it spans, which are minutes of performance and
carry no names at all.
