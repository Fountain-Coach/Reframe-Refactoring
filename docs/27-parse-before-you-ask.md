# Parse Before You Ask

> Chapter summary: A model shall never be asked for a fact the text already declares. Structure is **parsed**;
> meaning is **read**. Between those two there is a third category this app has been ignoring — **semantic tooling**
> that is local, fixed-weight and non-generative (Apple's NaturalLanguage: named entities, part of speech, sentence
> boundaries, sentence embeddings). It measures and labels; it cannot invent. So the work divides into three tiers:
> what the text *declares* (pure functions over the characters), what tooling *measures* (deterministic, instant,
> free), and what a reader *supplies* (what this raises, what stays unresolved) — and only the third is a model
> call. Everything the parser can settle is settled before the first token is spent, shown immediately, and never
> put at risk of fabrication. Where the parse cannot type a stretch it says so: an unparseable passage is a finding
> about the text, not an apology for the tool.

## Purpose — the failure this exists to end

Reframe asked a 4,096-token on-device model to supply structure the manuscript states outright, and paid for it
exactly as you would expect. Measured, in one working period, on Telemachus:

- Asked to name a six-line fragment, the model returned **"StorifyBeatTitleG"** — the Swift type of its own guided
  schema — on 37 consecutive calls, then `The name of the story is "StoryContentAnswerG"`, then a 120-word essay
  asserting that Mulligan is Stephen's father.
- Asked which names belong to one person, it produced **"Stephen Mulligan"**, welding two characters into a man who
  does not exist, and the uncertainty map reported his invented frustrations as findings of the reading.
- Asked what a chapter leaves open, it produced 65 unrelated observations over 45 passages — one per passage,
  because nothing carried forward — and called them beats.
- The entity roster, built by taking capitalised words, offered **"God"** and **"Irish"** as characters.

Meanwhile the text said, in plain print, where its episodes divide, which lines are spoken, who is credited with
speaking them, and how long each stretch takes to read. `StorifyPass.extractCandidateAtoms` — a synchronous scan,
no model, no waiting — knew the chunk boundaries all along and they were withheld from the writer until a model
confirmed them, so a thirteen-minute read showed an empty stage for its first minute. And `ReframeCore/Fountain/`
has held an 798-line fountain parser producing `sceneHeading` / `character` / `dialogue` / `action` the whole time,
which the reading pipeline never called.

`import NaturalLanguage` appears in five files of this app. Not one API from it is used. In its place stand a
capitalisation heuristic, a hand-written list of attribution verbs, sentence splitting on `". "`, and question
identity by 60% shared words.

The failure is not that the model is small. It is that the app asked a generator to recover, unreliably and at
cost, what a parser could state exactly and for nothing — and then built machinery to catch the generator lying.

## The principle — three tiers, and only the third is a model

**1. Declared.** What the text states about itself, recoverable by a pure function over its characters: episode and
section markers, paragraph and blank-line structure, opening dashes and quotation marks, line spans, word counts
and therefore reading time, the literal questions a text asks aloud (`?`). These cannot be wrong about the text,
cost microseconds, and are available before anything is read.

**2. Measured.** Local, fixed-weight, non-generative tooling — in this app, Apple's NaturalLanguage: named-entity
recognition, lexical class, sentence and token boundaries, sentence embeddings. Same input, same output; no
sampling, no temperature, no prompt. It can *label* ("this span is a personal name") and *measure* ("these two
sentences are near in meaning"); it cannot produce a character who is not there, or a claim the text does not
support. Every failure mode this app has fought — welded names, invented endings, schema words as titles — is
structurally impossible in this tier.

**It cannot invent, but it can miss.** Measured while building the prose projection: NER tags "Stephen" inside a
full sentence, but not "Stephen Dedalus" standing alone, and never "Mulligan" — with or without the language set.
Precision without recall. So a positive from this tier is *evidence*, and its silence is *nothing at all*: a design
that reads "not recognised" as "not a person" throws away half the speakers in Telemachus. Measured tooling
promotes a candidate; it never rejects one.

**3. Read.** What only a reader can supply: what this stretch raises that nobody says aloud, what remains
unresolved, what a beat costs a character, whether an ambiguity is the work's or the reader's. This tier is
interpretation, it can be wrong, and it is the only tier a model call belongs to.

The rule that follows is simple: **a question that a lower tier can answer must never be put to a higher one.**

## Rules

1. **No model call for a declared fact.** If the answer is recoverable from the characters of the text, parse it.
   A model asked where the chapters divide is a model given the chance to be wrong about it.
2. **Show the parse immediately.** Deterministic structure is on screen before the reading begins — the whole
   chapter's skeleton, not the part a model has confirmed. What fills in during a read is the *reading*.
3. **Prefer measured tooling to hand-rolled linguistics.** A capitalisation test where NER exists, a verb list
   where part-of-speech exists, `". "` where a sentence tokenizer exists, word overlap where sentence embeddings
   exist — each is a defect to be replaced, not a style choice.
4. **Take the tooling's positives, never its silence.** Recognition is evidence; non-recognition is not evidence of
   absence. Combine a positive with the structural signal beside it — an attributive verb, a typographic mark —
   rather than gating on the tool alone. And ask the tooling what it needs: a sentence tokenizer left to guess its
   language cuts "Mr. " off as a sentence of its own, which is the exact failure it was brought in to fix.
5. **A linguistic rule applies only to the language it was written for.** Detect, and stand down otherwise. English
   attributive grammar run over Joyce's Latin — "—_Introibo ad altare Dei_." — reads "altare" as a verb and reports
   a character named "Dei_" celebrating mass. The recogniser reads that line as Italian and every English line
   around it as English; a rule applied to a language it was not written for is not a parse, it is a coincidence.
6. **What will not parse is marked, never smoothed.** A stretch the rules cannot type is returned as
   *unclassified* and shown as such. Filing hard prose under "action" and calling it read is the same lie as a
   fabricated beat name.
7. **Hard prose is the test, not the exception.** Ulysses stops obeying by *Proteus* and abandons the rules in
   *Penelope*. A projection that types every stretch confidently is lying; the episodes that break it are how it
   is hardened. No apology, no special-casing to make a demo look clean.
8. **Fixed weights are versioned.** Tooling assets (embedding revisions, tagger models) can change between OS
   releases and shift a comparison. Where their output feeds a persisted judgement, the revision belongs in the
   reading contract ([ch.24](24-the-reasoning-is-an-uncertainty-map.md)), exactly as the reading's own contract is
   stamped — two readings compared across a change of tooling measure the tooling.
9. **The model's share shrinks as the parse grows,** and that is the goal. Every fact moved down a tier makes the
   reading faster, cheaper, more honest, and less able to invent.

## What this changes

- **Atoms become fountain elements.** The reading's unit stops being a blank-line block and becomes what the
  fountain parser already produces: a scene heading is a boundary, an exchange is a unit, an action paragraph is a
  unit. Prose is *projected* onto that spine deterministically (dash-initiated speech → `dialogue`; attributive
  clause → `character`; the rest → `action`; what resists → `unclassified`).
- **Presence becomes running state.** Who is on stage follows from attributed speech, not from a model's guess —
  and only from attribution: being mentioned is not being present, and inferring it is a claim the parse is not
  entitled to make.
- **Identity resolution starts from NER**, not from capitalised tokens, so "God" and "Irish" never enter a cast
  list and the model is asked only the genuinely interpretive part: whether two *names* are one *person*.
- **Question identity uses sentence embeddings.** "Stephen's motivation for leaving is unclear" and "It is unclear
  what motivates Stephen to leave" are one doubt; a bag-of-words comparison agrees by luck, an embedding by
  measurement.
- **Reading time, stopping places and the dog-ear become computable.** Where a reader would pause — an exchange
  closing, a division, an accumulated span of minutes — is arithmetic. Only the *note* about why one stopped is a
  reader's.

## Acceptance

- No path in the reading pipeline calls a model for chapter divisions, speech/narration typing, speaker
  attribution where the text attributes, sentence boundaries, entity candidacy, or reading time.
- Opening a manuscript draws its full structural skeleton with no model available at all (verifiable with the
  lanes disabled).
- `import NaturalLanguage` is either used or removed; no hand-rolled substitute for an API in that framework
  remains in linguistic code.
- Every projection has tests over **unmodified source text** of the work it claims to handle, including at least
  one stretch that legitimately returns `unclassified`, one the tooling fails to recognise (proving its silence is
  not treated as a negative), and one in another language (proving the rules stand down).
- Where tooling output feeds a persisted judgement, its revision appears in the reading contract.

## Governing sentence

Reframe shall parse what the text declares, measure what local non-generative tooling can measure, and ask a model
only what a reader alone can answer — showing the parse before the reading begins, and marking what will not parse
rather than smoothing it away.
