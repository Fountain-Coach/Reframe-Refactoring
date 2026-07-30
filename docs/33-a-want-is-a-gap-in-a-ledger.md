# A Want Is a Gap in a Ledger

> Chapter summary: Uncertainty about the *world* is not a list of axes somebody enumerated. It is **a function of
> the ledgers the work keeps, and of the gaps in them** — and a ledger that is stale, broken or never built is
> itself the loudest gap of all. Each gap carries a **want**: the one thing that would close it, typed by *who can
> answer* — the manuscript, a stronger reasoning, a source outside the work, or the writer. That type is the whole
> escalation ladder ([ch.32](32-referenced-knowledge.md) rule 8) made mechanical: a want the manuscript cannot
> satisfy is the only thing that may reach for the web, and a want is never fulfilled without the writer's yes. The
> gazetteer therefore stops being mute about its own holes — it says what it lacks, and what would end the lacking.
> Uncertainty leads to a want; a want leads to a retrieval; a fulfilment closes the gap and the map redraws.

## Purpose — the failure this exists to end

**Enumerated axes cannot represent what nobody enumerated, and they fail silently when they try.**

Measured on this codebase, 2026-07-30. `ReframeUncertaintyProjection.project(…)` is a closed, fixed-arity
translator: it accepts a parameter per source of doubt and builds, by hand, exactly two lanes —
`storifyStructure` and `storifyOpenQuestions`. A third was designed. `StorifyIdentityReading` exists, its doc
comment argues the case at length — *"Deciding that 'Stephen', 'Dedalus' and 'Kinch' are one man is not
preprocessing that happens quietly before the reading — it IS a reading, made by the same model, on the same
evidence, and it fails the same way"* — and the caller genuinely computes it, scanning every line of the source
for every merged identity to find its span, then passes it in.

**`project(…)` never reads the parameter.** The work is done and dropped. Nothing failed; nothing warned. The map
reported no identity doubt whatever, which renders identically to *"identity is settled here"* — and the reading
underneath it had been treating Stephen and Kinch as two men in conflict.

That is the shape of the failure, and it is not an oversight to be patched: **a design in which absence is
unrepresentable will keep producing it.** A lane that was never built and a lane with nothing wrong are the same
picture. The parameter list is a list of the doubts we happened to think of, and the map's silence is indexed to
our imagination rather than to the work.

**And the escalation built on top inherited the same ceiling.** With no identity lane to read, ch.32's reference
lane was wired instead to a pattern detector: pairs of confirmed people whose names share a last word and differ
before it. Driven live on a virgin Telemachus store, it worked exactly as written — it raised *"Buck Mulligan and
Malachi Mulligan look like one person"* and escalated correctly. And it can never raise Kinch. Verified: `Kinch`
and `Stephen Dedalus` share no word, so no resemblance rule reaches them. **The one identity ch.32 was written to
settle is the one that door structurally cannot propose.** A pattern proposes what the pattern was written to
catch, and the writer sees a confident world with a hole in it exactly where the reading was most wrong.

## The principle — uncertainty is a function of ledgers, not a list of axes

The work keeps ledgers. The passage feed knows which stretches were read. The gazetteer knows who exists and
under which names. The unresolved-names ledger knows what the reading tried and could not settle, and how often.
The reference-search ledger knows what was asked of the world outside and what came back, including nothing. The
mention ledger knows every name the source uses and where.

Each of them knows its own holes better than any observer could infer them. So the map is not assembled *about*
the ledgers by a translator that must be taught each one; it is **collected from** them. A ledger reports its own
gaps, and the map is the union of what the ledgers report.

This inverts who must be edited when the work learns a new kind of doubt. Under enumeration, a new doubt edits a
shared function and is therefore usually not added. Under collection, a new doubt is a new ledger that already
knows how to speak, and it appears on the map by existing.

**Lanes survive, demoted.** A lane is how a gap is *drawn* — a grouping on a spine, which is what
UncertaintyScoreKit models and all it should ever model. It is not a kind of uncertainty. Lanes are emitted from
which ledger a gap came from; they are never the thing that decides what may be uncertain.

## What a ledger owes

A ledger that takes part in the map owes four things, and the fourth is the one this chapter exists for:

- **Identity** — a stable name, so its gaps can be grouped, followed across runs, and named to the writer.
- **Its gaps** — each located in the work (the span it is about), stated in the honest states ch.24 already
  fixed: `settled`, `ambiguity`, `thin`, `failure`. A gap is not a complaint; it is a located fact about what this
  ledger does not hold.
- **An answer, always.** A ledger is asked and must reply. It may reply that it holds nothing open. It may not
  decline to speak, because silence and health are indistinguishable to a reader.
- **A want per gap** — the one thing that would close it, typed by who can answer. See below.

## The want, and who can answer it

A gap that does not say what would close it is a complaint. The want is the difference between a map that reports
and a map that can be acted on, and its *type* — not its wording — is what makes escalation mechanical:

- **the manuscript** — the text can still answer this; read further, or read this stretch again;
- **a stronger reasoning** — the evidence is there and this lane could not hold it; the widening offer of
  [ch.20](20-on-device-first-and-the-writers-key.md), decided by the writer's key;
- **a source outside the work** — *the manuscript cannot settle this*, and only here may the app reach for
  [ch.32](32-referenced-knowledge.md)'s reference lane;
- **the writer** — a judgement no source and no reasoning can make, which is the arbiter of last resort
  ([ch.30](30-the-living-gazetteer.md) rule 9, [ch.32](32-referenced-knowledge.md) rule 7).

This is [ch.32](32-referenced-knowledge.md) rule 8's order of resort, stated once as data instead of re-derived at
each call site. **The reference lane's trigger is a want of the third kind and nothing else.** No detector, no
resemblance rule, no enumerated pair-shape. *Kinch* reaches the web because the gazetteer's identity ledger reports
a name it cannot place and says the manuscript cannot place it — the same way any other unplaceable name will,
including the ones nobody has thought of.

**A want is a request, never an act.** It authorises nothing on its own: [ch.32](32-referenced-knowledge.md) rule
12 still requires the writer's yes at the call site, per act, and rule 11's dead-end ledger still refuses a search
already paid for on the same grounds. A want is what makes the *offer* honest, not what makes the fetch happen.

## A defunct ledger is the loudest gap

The rule that would have caught the dropped parameter, and the reason this chapter exists at all:

**A ledger that is absent, stale, failed or never built must report a gap saying so.** It may not report nothing.
Nothing means *"I looked and this is fine"*, and a thing that was never wired has looked at nothing.

This is [ch.30](30-the-living-gazetteer.md) rule 10 — *"incompleteness is stated, never filled"* — applied one
level up: not to a thin world, but to a **missing instrument for knowing whether the world is thin**. It is also
[ch.24](24-the-reasoning-is-an-uncertainty-map.md) rule 3's distinction held one tier out: a ledger that failed is
a `failure`, and a ledger holding nothing open is `settled`, and rendering them the same is the laundering that
chapter forbids.

The consequence for implementation is deliberate: ledgers are **registered**, and a registration is visible in a
way a dropped argument is not. Removing a ledger is then an act with an author, not an omission nobody can see.

## Measure before you reason, and reason before you ask

[ch.27](27-parse-before-you-ask.md) governs how a gap is *found*, and it is not repealed here. A gap that a lower
tier can establish is established there: that a stretch has no reading behind it is counted, not reasoned; that a
name occurs forty times and belongs to no confirmed identity is measured, not interpreted. Reasoning is spent on
what measurement cannot reach — whether two names are one person, in a text that never says so.

So the pattern detector this chapter retires was not wrong because it measured. It was wrong because it was the
**enumerated trigger** — the only door, admitting only the doubts it was written to shape. Measurement feeding a
ledger's gaps is right. Measurement standing in for the ledger is what fails.

## Amendment — the Gazetteer says what it does not know

[ch.30](30-the-living-gazetteer.md) rule 6 forbids the Gazetteer to set status on the uncertainty map. Rule 10 of
the same chapter requires it to state its incompleteness, and points at the uncertainty map to do it. As written,
the world must announce its holes on a surface it may not write to.

The tension is real and the resolution is not a compromise between the rules but a distinction they never drew:

- **Driving the app** — routing a turn, gating a step, answering a story question, setting a *verdict* — remains
  forbidden, absolutely. That is what rule 6 was defending, and it is what separated the Gazetteer from the index
  Phase 6 removed.
- **Reporting what it does not hold** is the opposite of authority. A ledger saying *"this name has no home and I
  cannot give it one"* makes no claim about the story, changes no route, and gates nothing. It is a confession, and
  a confession cannot be a usurpation.

**ch.30 rule 6 is amended by this chapter**, by pointer and not by footnote: the Gazetteer sets no *status* and
still routes, gates and answers nothing — and it **does** report its own gaps and their wants, because rule 10
already required it to and gave it nowhere to speak. Everything else in rule 6 stands unchanged.

## The seam — which side owns what

**UncertaintyScoreKit stays exactly as it is, and must not learn about ledgers.** It is a public library beyond
this app; its subject is scoring and drawing a spine of lanes and notes, and it already models that openly. "A
source outside the work" is Reframe's ladder, not a general fact about uncertainty, and pushing our domain into a
shared library would be this chapter's own failure committed in the other direction.

**The collection, the ledgers, the gaps and the wants are Reframe's.** The want is typed here; what crosses into
the kit is a note with its state and its `resolvedBy` — the want's *rendering*, keyed back to the note, so the kit
carries display and Reframe carries meaning.

## Rules

1. **Uncertainty about the work is collected from ledgers, never enumerated.** No function may hold a fixed list
   of the kinds of doubt that exist. Adding a kind of doubt is adding a ledger, not editing a translator.
2. **Every ledger reports its own gaps**, each located in the work and stated in ch.24's states.
3. **A ledger always answers.** Holding nothing open is an answer; declining to speak is not.
4. **A ledger that is absent, stale, failed or never built reports a `failure` gap saying so.** Silence from a
   defunct instrument is prohibited, because it is indistinguishable from health.
5. **Every gap carries a want, typed by who can answer it** — the manuscript, a stronger reasoning, a source
   outside the work, or the writer. An untyped want is a complaint and is not admitted.
6. **The reference lane is triggered by a want of kind "a source outside the work", and by nothing else.**
   Resemblance detectors, pair shapes and keyword rules may not trigger retrieval
   ([ch.30](30-the-living-gazetteer.md) rule 7: resemblance never establishes identity).
7. **A want authorises nothing.** The writer's yes is still required at the call site, per act
   ([ch.32](32-referenced-knowledge.md) rule 12), and a want may not re-open a search the dead-end ledger has
   closed on the same grounds (rule 11).
8. **A fulfilment closes the gap it was wanted for, and the map redraws.** What was retrieved is recorded as a
   reference, marked as referenced forever ([ch.32](32-referenced-knowledge.md) rule 3); the ledger stops reporting
   that gap because it no longer has it, never because the question was tired of.
9. **A gap is found at the lowest tier that can find it** ([ch.27](27-parse-before-you-ask.md)); reasoning is
   spent only where measurement cannot reach.
10. **Lanes are emitted, not enumerated.** A lane names where a gap came from. It is a drawing, and it never
    decides what may be uncertain.
11. **Ledgers are registered, and removing one is an act with an author.** A ledger may not leave the map by being
    quietly unwired.
12. **The map remains removable.** Deleting every ledger's accumulated knowledge leaves the manuscript whole and
    readable ([ch.31](31-compiled-knowledge.md) rule 4, [ch.32](32-referenced-knowledge.md) rule 10); nothing
    downstream may require a gap, a want, or a fulfilment to exist.

## Acceptance

The doctrine is met when:

1. No function anywhere holds an enumerated list of uncertainty axes; the projection takes a collection of ledgers
   and emits a lane per ledger that reported.
2. A ledger removed, broken or never wired appears on the map as a loud `failure` — demonstrated by disabling one
   and seeing the map say so, rather than seeing it grow quieter.
3. Every gap on the map states a want, and every want names who can answer it.
4. An unplaceable identity the manuscript cannot settle — *Kinch* is the standing case — reaches the reference
   lane through its want, with no rule naming it, no pair-shape, and no resemblance.
5. `WorldDuplicates` (and any successor pattern detector) no longer triggers retrieval; deleting it changes which
   doubts are *measured*, never which may be escalated.
6. A retrieval the writer authorises and accepts closes the gap that wanted it, and the map redraws without it —
   verified by reading the store, not the screen.
7. Refusing a want leaves the world exactly as it was, and the gap is still reported.
8. Deleting every ledger leaves the manuscript readable and every reading performable.

## Governing sentence

Reframe shall know what it does not know by asking the ledgers that keep the work, never by consulting a list of
the doubts it once thought of — and every gap they report shall name the one thing that would close it, so that
reaching outside the manuscript is something a want justifies rather than something a pattern happens to notice.
