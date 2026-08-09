# 53. A Selection Snaps to Meaning

> Chapter summary: Reframe asks the writer to point at text — to mark it, cut it, cite it, reframe it — and it has
> been asking her to do so **character by character**, with a mouse, on a manuscript. That is an operability
> failure and it belongs to the app, not to her: a reader indicates a **phrase, a line, a speech, a sentence**,
> never a character offset, and requiring the offset excludes anyone whose hands or eyes are not perfect on a
> given day. So a selection is **snapped to the smallest unit of MEANING that contains what she indicated** —
> whole words always, the sentence or speech when she has barely selected anything — and the snap is *gentle*: it
> only ever grows outward to a boundary the text itself declares, never shrinks, never moves the selection
> somewhere she did not point. The boundary is **parsed, never asked of a model** ([ch.27](27-parse-before-you-ask.md)),
> and it is **measured, never concluded** ([ch.29](29-natural-language-measures-storify-interprets.md)) — a
> tokenizer says where a sentence ends; it does not say what the sentence means. And where the text declares no
> boundary the snap **stops and says so** rather than inventing one: measured on this app's own shipped corpus,
> Ulysses' *Penelope* runs **27,287 characters with a single full stop**, so "snap to the sentence" there would
> select the whole episode. A snap that cannot find a unit falls back to words and reports that it could not find
> one; it never manufactures a grid ([ch.50](50-text-is-stored-so-it-can-be-pointed-at.md)).

## Purpose — the failure this exists to end

The writer's pencil ([ch.52](52-the-pencil-belongs-to-the-writer.md)) shipped requiring a character-precise drag
across a monospaced manuscript to mark a phrase. The writer's own report, on first using it:

> my eyesight is not too good anymore and using a tool like marking a text is somewhat difficult sometime

That is not a preference and it is not an edge case. It is the surface asking a person to perform a fine motor
task in order to express something coarse — *this bit matters* — and then storing the fine motor task as though
it were the meaning. Every failure of the hand becomes a wrong mark: three characters short of a word, a line
above the one she wanted, a partial word stored verbatim as the thing she noticed.

[ch.18](18-the-stage-presents-the-act.md) sets a floor for what a writer can **read**. This is the same floor for
what she can **do**: a control she cannot operate reliably is not a control, however correct its data model.

## The principle — the unit of a gesture is a unit of meaning

A reader pointing at text is not naming a range of characters. She is naming **a thing in the writing**: this
phrase, this speech, this stage direction, this sentence. The app's job is to hear the thing, not to transcribe
the hand.

So every selection that becomes a durable act passes through one question: *what is the smallest unit of meaning
that contains what she indicated?* The answer is what is stored, drawn, cited and reframed.

This makes the feature **contextual rather than mechanical**: the same gesture in a stage direction takes the
stage direction, in dialogue takes the speech, in prose takes the sentence. What the text is determines what a
point at it means.

## Measured — Penelope, which breaks the naive rule

The obvious implementation is "snap to the sentence". Measured against the corpus this app ships with, over the
last 400 lines of *Ulysses*:

```
27,287 characters
1 full stop
0 question marks
```

Molly's soliloquy is unpunctuated by design. "Snap to the sentence" there selects the episode. Any rule that
assumes a sentence boundary exists will produce, on the flagship work, a selection eight thousand words long
presented as though the writer had chosen it.

This is the same lesson [ch.27](27-parse-before-you-ask.md) rule 7 already records — *hard prose is the test, not
the exception* — arriving at a new surface. The rule is not "find the sentence". The rule is "grow to the nearest
declared boundary, and if the text declares none, stop and say so."

## Rules

1. **A selection that becomes a durable act is snapped before it is stored.** Marking, citing, cutting and
   reframing all take the snapped unit. What is stored is the unit, never the raw drag.
2. **The snap only grows, and only outward to a boundary the text declares.** It never shrinks a selection, never
   moves it off what she touched, and never crosses a boundary she stayed inside.
3. **Whole words, always.** A partial word is never what anyone meant.
4. **The unit is chosen by what the text IS at that point** — a speech, a stage direction, a verse line, a
   sentence, a paragraph. Structure the parse already knows takes precedence over generic punctuation.
5. **Where the text declares no boundary, the snap stops at words and SAYS it could not find a unit.** It never
   invents one, and it never silently returns something enormous.
   ([ch.50](50-text-is-stored-so-it-can-be-pointed-at.md): where no boundary exists, record the fact.)
6. **The boundary is parsed, never asked of a model** ([ch.27](27-parse-before-you-ask.md) rule 1), and measured
   with real tooling rather than hand-rolled punctuation matching (rule 3), told what language it is reading
   (rule 4), and standing down where the language is not the one the rule was written for (rule 5).
7. **A tokenizer measures; it never concludes.** Where a sentence ends is a measurement. What it means is a
   reading ([ch.29](29-natural-language-measures-storify-interprets.md) rule 1).
8. **The snap is visible before it is committed.** She sees what will be taken — highlighted as the unit, not as
   her drag — so the correction is something she watches happen, not something she discovers afterwards.
9. **She can always overrule it.** A deliberate precise selection, held, is honoured exactly; the snap is a
   kindness, never a cage.
10. **No surface reports the snap as a correction of her.** The app does not say "expanded", "fixed", or
    "adjusted your selection". It shows the unit and says what it is.

## What this forbids, stated plainly

- Requiring a character-precise drag to perform any durable act.
- Storing a partial word as a writer's mark.
- Assuming a sentence boundary exists in a manuscript.
- Snapping by scanning for `". "` where a sentence tokenizer exists.
- A snap that shrinks a selection, or moves it away from what she touched.
- Silently returning a unit thousands of words long because the text had no punctuation.
- Telling the writer her selection was wrong.

## Acceptance

1. **Penelope is the fixture.** A gesture inside the unpunctuated episode returns a word-bounded selection and a
   stated absence of a sentence unit — never the episode.
2. **A partial word never survives.** Property-tested over the corpus: for any raw range, the snapped range
   begins and ends on a word boundary.
3. **The snap only grows.** Property-tested: the snapped range contains the raw range, always.
4. **Dialogue, stage direction and verse each take their own unit** on a fixture drawn from *Circe*, which
   carries all three within a hundred lines.
5. **A held precise selection is honoured**, proven by a drive that selects exactly and marks exactly.
6. **The unit is visible before the act**, proven by a rendered image in light and dark — not by a flag
   ([ch.18](18-the-stage-presents-the-act.md) rule 6).
7. **The gesture is drivable**, which means the accessibility tooling can make a selection and press the act;
   evidence that seeds the store instead of performing the gesture does not satisfy this chapter.

## Governing sentence

Reframe shall hear what the writer pointed AT rather than transcribe how her hand moved — growing every durable
selection outward to the smallest unit of meaning the text itself declares, parsing that boundary rather than
asking for it, and stopping honestly at words wherever the writing declares no boundary at all, so that pointing
at a phrase never requires the precision of pointing at a character.
