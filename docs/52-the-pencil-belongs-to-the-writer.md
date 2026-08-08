# 52. The Pencil Belongs to the Writer

> Chapter summary: A reader underlining with a pencil marks **forward, in ignorance** — something registered
> before she could say why, and the mark is a bet on the future of her own reading: it flags salience rather than
> asserting a conclusion, it is mute (no caption, and often unreconstructable later, which is normal), it is cheap
> to be wrong about, and it layers across readings. The mark Reframe now has is the **exact inverse in every
> respect**: made backward from a window the model has already finished, asserting a proposition ("these words
> raised this question"), captioned by the question it belongs to, and expensive to be wrong about because a
> machine's mark is read as a finding. So it is **not an underline — it is a citation**, a footnote drawn in
> reverse from a claim back to its evidence, and calling it an underline is the app quietly claiming to have done
> the thing the reader does. The two marks therefore have different owners and must not share a visual language:
> the **machine's citation** is captioned, answerable and tied to its question's lane; the **pencil is the
> writer's**, and when she marks a line she is not citing anything — she is saying *this matters to me, I do not
> yet know why*, which is an instruction with an address (ch.46) and the app's job is to notice it and ask, never
> to interpret it as evidence. A machine mark drawn in the visual language of a reader's pencil is a category
> error with a cost: it launders retrospection as attention. Absence stays absent — a question the reading could
> not place gets no mark at all, and the writer's unexplained mark is never given a reason it did not carry.

## Purpose — the failure this exists to end

An underline was already three different things in this app, and the CoPilot's own help text had to spend a
paragraph warning the writer not to confuse them:

```
In the Semantic Index passage cards and expanded reader, an underline marks a source line included in
`IndexedPassage.citedLines`, meaning at least one recorded claim cites that line as evidence.
…
The live read-in animation uses underlines differently: it shows read-through progress while a run is
happening. Do not confuse that progress animation with the Semantic Index evidence marks.
```

Three meanings, one mark:

| meaning | the statement it makes | status, measured 2026-08-08 |
|---|---|---|
| evidence — a recorded claim cites this line | "something I concluded rests here" | producer removed with the semantic-index runtime; `BaselineViews.evidenceTint` survives but nothing mounts the view |
| progress — the read-through animation | "I have been here" | transient |
| anchor — a question was raised here | "these words are why I am asking this" | emitted as of 2026-08-08; 13 of 15 windows anchored on the Circe run |

Two of those are not marks about the text at all. *Progress* says the reader passed through, which is a fact about
the reader; it must leave nothing behind, because a mark that persists is read as a claim. *Evidence-of-claim* was
coherent and its producer is gone. Only the third says something about the writing that a person could check.

But the third one arrived wearing the wrong name, and the name was about to decide the drawing. That is the
failure this chapter exists to end: **the app was one design review away from rendering a citation as a pencil
stroke**, which would have made a retrospective machine inference look like a reader's live attention.

## What a reader does with a pencil

She underlines **forward, in ignorance.** She does not know what the book will make of this sentence. Something
registered — a phrase caught, a name recurred, a tone shifted — and the pencil moved before she could say why. The
mark is a bet placed on the future of her own reading.

Three consequences, all load-bearing:

1. **It flags salience, not conclusion.** It says *come back here*, not *this is what that means*. It is addressed
   to her later self.
2. **It is mute.** No caption, no reason attached. She re-reads and often cannot reconstruct why she marked it —
   and that is not a failure of the mark. A reason invented later is not the reason she had.
3. **It is cheap and it layers.** Being wrong costs nothing. Second reading, different pencil; the accumulation
   becomes a record of her changing relationship to the text.

Its unit is the eye's unit — a clause, a sentence, what she holds in one glance.

## What the machine's mark is instead

Point for point, the inverse.

It is made **backward**: the model has read the whole window and then reports where the question was raised. It
**asserts a proposition** — *these words raised this question* — which is exactly why it must be falsifiable. It is
**captioned**: it belongs to a named question, and pointing at it must answer with that question. And it is
**expensive to be wrong about**, because a machine's mark is read as a finding, not as a mood.

The honest name is **citation**: a footnote drawn in reverse, from the claim back to the evidence, and therefore
governed by [ch.40](40-a-citation-is-a-promise-someone-can-check.md) — a promise someone can check.

## It is the beat's head, never the beat

Measured on the Circe run of 2026-08-08 (on-device, 16 passages):

```
thread   20608 → 20815     anchor  20776 → 20790   (15 lines)
thread   20925 → 21228     anchor  20925 → 20945   (21 lines)
thread   21230 → 21713     anchor  21230 → 21315   (86 lines)
window   20194 → 20317     anchor  20289 → 20317   — the thread opens 95 lines into its own passage
```

A beat is the stretch over which one question stays open ([ch.28](28-a-beat-is-the-question-it-raises.md) rule 1)
— hundreds of lines, overlapping other beats. An anchor is the twenty-odd lines that raised it. Marking the body
would stripe the chapter three deep and say nothing; marking the head is checkable by eye, which is the only
property that matters.

So one beat is drawn twice, in two registers, each carrying half of one statement: the **ribbon** says how long
the story held the question open and what it overlapped; the **citation in the text** says which words opened it.
Neither is the beat alone. This is why the anchor sets a thread's opening and never its end — closing a thread at
its anchor would turn every question into a few lines long and delete the beat itself.

## The writer's mark is an instruction with an address

If the machine's mark is a citation, the pencil is unclaimed — and it belongs to the writer.

When she marks a line she is not citing anything. She is saying *this matters to me, I do not yet know why*, in
the text, with an address attached. That is grounding taught in the work rather than configured in a panel
([ch.46](46-dynamic-grounding.md)), and it is the most honest form of it: no lens named, no category chosen, no
claim made — a location and an emphasis, which is all she has at that moment.

What the app owes such a mark is **notice, not interpretation**. It may ask about it, later and in dialogue, and
what she answers becomes the reason. It may not supply the reason itself, rank the mark, classify it, or feed it
into a reading as though it were evidence — an unexplained mark is exactly as informative as it looks, and
inventing its reason is the same failure as naming a beat the reading left unnamed
([ch.28](28-a-beat-is-the-question-it-raises.md) rule 3).

## Rules

1. **A mark made backward is a citation and is drawn as one.** It carries the question it belongs to, and pointing
   at it answers with that question. A machine mark that cannot say what it is a citation *of* is not drawn.
2. **A mark made forward is the writer's, and only the writer makes one.** Reframe never draws a mark that means
   "this seems important" — it has not read forward, and it cannot mean it.
3. **The two marks never share a visual language.** Not the same stroke, weight, colour role or gesture. A reader
   must be able to tell, without clicking, which marks are hers.
4. **The citation is bound to its question's identity** — the same lane, the same colour, the same object as the
   mark on the map above ([ch.36](36-every-gap-keeps-its-address.md)); pointing at either is one act.
5. **The citation marks the head, never the body.** The stretch a question stays open is the ribbon's to draw.
6. **Progress leaves nothing behind.** A read-through animation is motion, and it may not deposit a persistent
   mark; "I have been here" is a fact about the reader that no one can check against the text.
7. **Absence is absence.** A question the reading could not place gets no mark — never the passage's span borrowed
   to look located ([ch.50](50-text-is-stored-so-it-can-be-pointed-at.md)).
8. **The writer's mark is never given a reason it did not carry.** It is noticed, and asked about in dialogue; it
   is not classified, ranked, scored, or read as evidence.
9. **Marks stack without flattening.** Threads overlap ([ch.28](28-a-beat-is-the-question-it-raises.md) rule 5),
   so a line may sit under several citations and the drawing must express multiplicity rather than merge it into
   one rule.

## What this forbids, stated plainly

- Drawing a machine inference as a pencil stroke.
- One mark carrying two meanings, with prose somewhere explaining which is which.
- A persistent mark deposited by a progress animation.
- An anchor defaulted to its passage span so that every question looks located.
- Underlining a beat's whole span.
- Interpreting, scoring or ranking the writer's own marks.
- A citation that cannot name its question, or a question whose citation opens something else.

## Acceptance

1. **Every drawn citation resolves to a question**, and the question resolves back to the same span — asserted on
   a real reading, not a fixture.
2. **Unanchored questions draw nothing**, and the surface says the reading could not place them rather than
   showing a passage-wide mark. The Circe run is the fixture: 2 of its 15 windows are unanchored.
3. **The writer's marks and the app's marks are distinguishable in a rendered image** by someone who is not told
   which is which — pixel evidence in both themes ([ch.19](19-apple-human-interface-guidelines.md)), not a flag.
4. **A citation and its ribbon lane are one object**: selecting either selects the other, and both are reachable
   by identity in the accessibility tree (FCIS-AX-01).
5. **Overlapping citations remain individually addressable** where three or more threads cover one line.
6. **No writer mark reaches a prompt as evidence.** Proven with a reading run over a manuscript carrying marks,
   asserting the marks appear in no prompt composition.

## Governing sentence

Reframe shall draw its own marks as citations — backward-looking, captioned, answerable, bound to the question
they belong to — and shall leave the pencil to the writer, whose forward, unexplained mark it may notice and ask
about but never interpret, so that the app can never wear the appearance of having attended to a page it has only
finished reading.
