# A Beat Is the Question It Raises

> **Vocabulary amendment (2026-08-17):** The historical term “beat” in this chapter names the open-question span.
> The current Reframe projection presents that record as **Questions**. **Movements** are a separate lane for
> grounded dramatic changes. Existing `beat` identifiers remain compatibility aliases only; writer-facing surfaces
> must use Questions, Movements, and Read coverage.

> Chapter summary: A **beat** is a story unit defined by the open question it raises — it begins where the question
> is raised and ends where the story stops holding it. An **atom** is something else entirely: the reader's local
> choice about where one close-read stretch ends, measured in **a minute of performance** and cut at the text's own
> seam. Atoms are not beats and must never be labelled as such. They carry no NAMES — every attempt to name one
> produced a description of its contents on every lane tried — but they may carry a **claim** about their own
> lines, which unlike a name can be graded against them (amended 2026-07-29). The question names the beat: grounded by construction, impossible to fabricate, free. Because
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
   name is missing.
3a. **An atom may carry a CLAIM, never a name** (amended 2026-07-29 — see below). A claim is a sentence about what
   these lines contain, and it must be gradeable against them; a name is unfalsifiable and remains prohibited. An
   atom with no claim is normal and needs no apology.
3b. **A claim's grade travels with it.** An element nothing in the span supports is shown as unsupported — never
   deleted quietly, and never carried onward as though it were established.
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
- No model call exists whose purpose is to name a beat, or to name an atom.
- Every atom claim shown to the writer can be graded against its own lines, and the grade is reachable from where
  the claim is shown.
- A claim naming someone the span does not contain is marked unsupported rather than displayed as a heading.
- Every thread the map shows carries a first line, a last line, how many passages held it, and whether it was still
  open where the reading stopped.
- A run over a whole chapter produces at least one thread that closes before the end, and the app states closure as
  silence rather than resolution.
- Beats form during the read, visible as they accumulate, without a second pass.

## Amendment (2026-07-29) — a claim is not a name

The original rule read as a ban on writing anything about an atom. That was too wide, and the reason is in what it
was measured from: every failure came from asking for a **name**. A name is unfalsifiable — nothing can be checked
against "The Keeper's Dilemma" — which is why the lane returned its own schema type on 37 consecutive calls, then a
120-word essay claiming Mulligan was Stephen's father, and why roughly three hundred lines of repair machinery
never made a name good.

Measured again on 2026-07-29, reading Telemachus on-device with the entity-mention ledger in the prompt
([ch.30](30-the-living-gazetteer.md)), the atoms carried this instead:

```
ATOM 3  ll. 63–82   Stephen and Buck Mulligan's relationship is strained as Stephen questions
                    Buck's judgment and Buck's disdain for the English
ATOM 4  ll. 83–105  Stephen and Buck Mulligan are in a tense moment, with Stephen expressing
                    fear and Buck trying to reassure him
ATOM 5  ll. 106–129 Stephen and Buck Mulligan face a major conflict as Stephen is accused of
                    murdering his mother
```

Those are not names. They are **claims**: two people correctly distinguished — no welded "Stephen Mulligan", no
imported Fergus — and every element of them checkable against the lines they cover. They are also useful in a way a
name never was: a writer scanning the strip learns what is in each stretch without opening it.

And the third one is wrong. The text has the aunt's *"you killed your mother"* and Mulligan's *"you could have
knelt down… when your dying mother"*; **murder** is an overreach, and it was displayed in bold at the head of a
card, where a claim reads as established and travels onward into the digest and into answers with nothing attached
saying how well it is supported. That is the whole hazard, and it is an argument for GRADING rather than for
silence: a claim can be audited ([ch.29](29-natural-language-measures-storify-interprets.md) §claim audits), a name
cannot.

So the rule changes shape rather than lifting:

- an atom may carry a claim about its own lines, and never a name;
- the claim is gradeable against those lines, and its grade travels with it;
- a beat is still named by its question alone, and an atom's claim never becomes a beat's name;
- **repeated claims across neighbouring atoms remain beat evidence** — the reader saying *these belong together* —
  and are not de-duplicated away, which is what this chapter said about repeated titles from the beginning.

## Governing sentence

Reframe shall treat a beat as the question the story holds open — found in one forward pass, named by that
question, shown as it forms, and never confused with the atoms it spans, which are minutes of performance: they
carry no names, and what they may carry instead is a claim about their own lines that can be checked against
them.
