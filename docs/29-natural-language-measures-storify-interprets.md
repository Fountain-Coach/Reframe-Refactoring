# NaturalLanguage Measures, Storify Interprets

> Chapter summary: Apple's **NaturalLanguage** framework is a measuring instrument, not a small reader. It answers
> *where is it*, *what literal form appears there*, *what resembles it*, *what changed*, and *which model claim has
> no visible textual support*. Storify answers *what is happening*, *what changes*, *who is acting*, *what is at
> stake*, *what is unresolved*. Everything NaturalLanguage produces is a **candidate or a coordinate**, never a
> fact about the story — it is offered to the reading as evidence and confirmed there, or not at all. Used this
> way it makes every model call smaller, better grounded, cheaper and more inspectable; used as a second opinion
> about meaning it becomes exactly the speculative pre-classifier [ch.12](12-the-copilot-is-one-reasoning.md)
> forbids. [ch.27](27-parse-before-you-ask.md) establishes the tiers — declared, measured, read — and this chapter
> governs the measured tier: what may be measured, what must not be concluded from a measurement, and how the
> evidence reaches the one reasoning.

## Purpose — the failure this exists to end

Two opposite failures, both observed in this app, and NaturalLanguage sits between them.

**Asking a model what a tokenizer answers.** Passages were cut at blank lines and line counts, atoms were sized by
lines rather than by the text's own units, and a model was asked to identify divisions the source states outright.
That is [ch.27](27-parse-before-you-ask.md)'s failure, and the correction was to measure first.

**Believing the measurement.** The correction over-ran. `NLTagger`'s name scheme was treated as a cast list and
handed to the map as "Who this is" — a third of the map's height spent asserting, as a doubt the reading held,
something the text simply says. Then the measurements were found to be wrong in ways that matter:

- **Named-entity recognition misses obvious people.** Measured on this prose: `.nameType` missed *Buck Mulligan*
  in a plain narrative sentence and *Mulligan* entirely, while tagging `Dei_` — from *Introibo ad altare Dei* —
  as a person, because English-language machinery was run over Latin.
- **Sentence embeddings inverted on question identity.** Two phrasings of the same doubt scored 0.999 apart while
  two plainly different questions scored 0.854 — the wrong way round, which is why threads carry stated numbers
  ([ch.28](28-a-beat-is-the-question-it-raises.md)) instead of embedding similarity.

Neither result makes the framework useless. Both make its **authority** clear: it is good at *where* and *what
form*, unreliable at *who* and *what it means*. A measurement that is wrong 5% of the time is excellent evidence
and a disastrous source of truth.

Meanwhile the copilot, composing from a reading, welded *Stephen* and *Buck Mulligan* into "Stephen Mulligan", and
described a quarrel with *Fergus* over payment at a milkman's shop that no line of the chapter contains. No
adjudication caught it, because every word was in the reading. A string search caught it in microseconds. That is
the shape of the whole opportunity: NaturalLanguage is at its best **after** the model has spoken, checking what it
said against what the text contains.

## The principle — measure and organise, never conclude

**NaturalLanguage continuously measures and organises the source; Storify interprets it.**

Everything follows from refusing to let a measurement become a conclusion:

- A tokenizer's boundaries are **coordinates**. They say where a sentence ends, not what it means.
- A tagger's tags are **candidates**. "The tagger marked *Stephen* as a possible personal name at sentences 41, 89
  and 103" is a fact about the tagger. "Stephen is a character" is a reading.
- An embedding neighbourhood is **resemblance**. "These passages are mathematically nearby" is never "these
  passages prove the interpretation."
- A fingerprint comparison is an **audit question**. "This beat names a character absent from its evidence" is
  worth asking; "this beat is wrong" is not the measurement's to say.

The output of the measured tier is therefore named for what it is — a **linguistic evidence map** — and never for
what it is not. Names like `SemanticUnderstanding`, `StoryAnalyzer`, `IntentClassifier`, `BeatDetector` or
`TruthIndex` are prohibited: a name that claims authority will eventually be believed by the code around it.

## What is measured, and how it is held

**Boundaries.** `NLTokenizer` at paragraph, sentence and word level, stored as ranges against the immutable source
([ch.13](13-one-immutable-source.md)) — offsets, never copies. This gives exact citation, passage selection,
alignment of beats to text, and the ability to show *why* without fabricating a quotation.

**Observations.** Lemmas, lexical classes, personal/place/organisation candidates, language and script, quotation
and punctuation spans — each stored with the range it came from and the analyzer revision that produced it, so a
later disagreement can be attributed rather than argued.

**Entity mentions.** For each surface form: where it occurs, its variants, the pronouns and action lemmas near it,
first and last occurrence. This is a body of evidence about a NAME, not a claim about a PERSON. It exists so that
identity resolution — which is reading — has something auditable to resolve *from*.

**Resemblance.** Sentence embeddings for retrieval only: given what the reading is currently examining, hand it a
dozen candidate passages instead of a manuscript. Retrieval decides what the reader LOOKS at; it never decides what
the reader CONCLUDES.

**Fingerprints.** Per beat: dominant entities, action lemmas, dialogue ratio, pronoun distribution, lexical
density, source ranges. Cheap comparisons — is this beat a restatement of that one, which characters vanish between
adjacent beats, did a reframe remove every concrete action — asked as questions, never returned as verdicts.

## Where it earns the most: challenging what the model said

The highest-value moment for the measured tier is **after** the reading proposes something. Given a claim and the
range it cites, the deterministic layer can report what the text does and does not contain, and grade each element
of the claim:

```
Claim: "Buck humiliates Stephen in front of their guests." (ll. 88–105)
  Buck                explicit          — 3 mentions in range
  Stephen             explicit          — 5 mentions in range
  public interaction  structurally supported — 3 further person candidates present
  humiliation         interpretive      — no lexical basis; this is the reading's judgement
  guests              unsupported       — no occurrence in range or in the two preceding paragraphs
```

Five grades, and they are not opinions: **explicit**, **structurally supported**, **interpretive**, **ambiguous**,
**unsupported**. The measurement does not decide whether a humiliation occurred — that is dramaturgy. It reveals
that *guests* has no textual basis, which is the difference between an interpretation and an invention.

This is how the welded name was caught, and it generalises: names, places, quoted words, and the presence of any
action at all are all checkable without asking anyone.

## Feeding the uncertainty map without becoming a router

The map's reasons may be measured; the map's decisions may not. A concrete reason is worth more than a number:

> **Status: thin.** The proposed beat names "the mother", but the cited passage contains no explicit mother
> reference; two female pronouns occur with no resolved antecedent.
> **Resolved by:** read the preceding two paragraphs, or drop the kinship claim.

That is a better artefact than a confidence of 0.63, and it is still evidence: the *status* is the one reasoning's
([ch.12](12-the-copilot-is-one-reasoning.md), [ch.24](24-the-first-reads-product-is-uncertainty.md)), and the
measurement supplied its grounds. What the measured tier must never do is route a turn, choose a lane, pick a
target, or decide that a reading is wrong.

## Custom models and gazetteers

`NLModel` and gazetteers are permitted for **narrow, testable, form-level** questions: scene headings, dialogue
versus narration, speaker labels, chapter headings, explicit temporal or location expressions, stage directions,
quotation spans in irregular sources. Each is checkable against a fixture and fails visibly.

They are prohibited for questions of meaning — *what is the beat*, *what does the character want*, *is this
dramaturgically important*, *what does the writer intend*, *should we spend on cloud inference*. Those are reading
and routing, and a small classifier that answers them is the pre-classifier this architecture exists without.

A per-project gazetteer is built from **confirmed** facts only, producing a cycle that is allowed to improve
recognition and never allowed to overwrite the story: the framework proposes candidates → Storify confirms or
rejects → confirmed entities enter the gazetteer → later passages are analysed with better project awareness → new
evidence may split or merge identities, with provenance retained.

## Incremental recomputation

Because the measurements are coordinates against an immutable source, an edit invalidates from the smallest changed
range upward:

```
source range → linguistic observations → mentions · embeddings · fingerprints
             → evidence packet → beat claims → take / cut / continuity projections
```

A changed sentence should re-tag that sentence and its neighbours, not re-read a chapter. This is where the
framework pays for itself in time rather than quality: the reading is the expensive thing, and most of it does not
need to happen again.

## Amendment (2026-07-29) — measure once, and only what changes what the writer sees

Two failures in one day, from the same root, both worth writing down.

**The measurement was built and never given a place to live.** The tier computed its map on demand, so every
consumer computed it again for itself: the read for its prompt, the Gazetteer for its confirmation, the Spaces
band on every open, the claim grades on every render. Four full passes over one unchanged chapter, three of them
on the path the writer was waiting on. The app stalled three times — 99% CPU with the GUI frozen, then 760% with a
read going nowhere — and each time the fix I reached for was a patch to the pass rather than the missing storage.

A measurement is a pure function of the source. It is computed **once per source version**, held for the session
and persisted against that version, and every consumer READS it. A consumer that measures is a bug, however cheap
its own pass looks in isolation.

**And features were shipping because they were possible.** A band of places went onto the stage having earned
nothing: it re-measured the whole source on every open to show a handful of nouns, some of them wrong. The
discipline is not "is this measurable" but "does knowing it change what the writer does".

## Rules

1. **NaturalLanguage measures and organises; Storify interprets.** No component of the measured tier concludes
   anything about the story.
2. **Its output is candidates and coordinates.** A tag is what the tagger said, held with its range and analyzer
   revision — never promoted to a fact by being stored.
3. **A measurement never becomes canonical without confirmation by the reading**, and confirmation is recorded with
   its provenance.
4. **Retrieval is resemblance, not evidence.** Embedding neighbourhoods choose what the reader looks at and prove
   nothing.
5. **The measured tier may supply REASONS to the uncertainty map, never STATUSES**, and never routes a turn, picks
   a lane, or selects a target.
6. **Claim audits grade elements** — explicit, structurally supported, interpretive, ambiguous, unsupported — and
   stop there. An unsupported element is reported, not corrected.
7. **Custom models and gazetteers only for form-level questions** that a fixture can settle. Never for meaning,
   intent, importance or spending.
8. **Never ask a model what a measurement answers** ([ch.27](27-parse-before-you-ask.md)); **never let a
   measurement answer what only a reading can** (this chapter). Both directions are the same error.
9. **Nothing measured is shown as a doubt the reading holds.** Who is named in a passage is stated by the text; it
   is not a lane on the map.
10. **Measure once per source version, and store it.** The measurement is a pure function of the source; a
    consumer that measures rather than reads is a defect, and hot paths take an index over the source rather than
    walking it per lookup.
11. **A measured feature ships only when it changes what the writer sees or does.** Being computable is not a
    reason. What earns nothing goes back in the drawer, with its tests, until it can be shown to.
12. **Name the component for its authority.** `SourceLinguistics`, `LinguisticEvidenceMap` — never
    `SemanticUnderstanding`, `StoryAnalyzer`, `IntentClassifier`, `BeatDetector`, `TruthIndex`.

## Acceptance

- Every linguistic observation carries a source range and an analyzer revision, and no interpretation.
- A model claim can be graded against its cited range, and the grades appear where the writer can see them.
- No name reaches the writer that does not occur in the reading it claims to come from.
- Retrieval results are labelled as resemblance wherever they are shown or passed to a prompt.
- No routing decision, lane choice or turn target is taken from a measurement.
- Editing one paragraph re-measures that paragraph and its neighbours, not the chapter.
- The measured tier's types are named so that their limited authority is obvious from the call site.

## Governing sentence

Reframe shall use NaturalLanguage to know where the text is, what form it takes, what resembles it, what changed,
and which claims the text does not support — and shall never let it say what the story means.
