# A Citation Is a Promise Someone Can Check

> Chapter summary: [ch.32](32-referenced-knowledge.md) through [ch.35](35-deep-search.md) govern knowledge coming
> IN — retrieved, never recalled. This chapter governs the claim going OUT: a sentence in the work that cites a
> source, and what the app owes a reader who tries to follow it. The failure is already on the record, and it is
> the author of [ch.39](39-a-model-cannot-be-told-what-it-cannot-do.md) committing it: a citation with authors, a
> venue and a footnote marker, formatted like scholarship, supporting a claim the cited paper does not make —
> because it came from a search engine's summary and nobody read the source. Nothing in the artifact distinguished
> that from a checked one. So: **verification is an ACT, never a state somebody asserts**, and a citation the app
> has not checked is rendered as a BREAKDOWN — loud — not as a quiet footnote. A citation is a promise that
> someone can check; until it has been checked, it is a claim about a source and not a source.

## Purpose — the failure this exists to end

**A sentence that looks checked and is not.**

On 2026-08-02 this repository published a governance chapter stating that "an explicit reject/OOS class performs
worse than the alternatives", footnoted to Cavalin et al., EMNLP 2020.[^cavalin2020] The footnote was complete:
four authors, a venue, a year, a resolvable link. The paper does not make that claim — it concerns word-graph
embeddings for class labels. The sentence had come from a search engine's summary of several papers and was
published without the source being read.

The chapter it appeared in was about not trusting fluent, confident sentences you have not checked.

Three properties of that failure decide this chapter:

1. **It was indistinguishable from good work.** Every visible attribute of a sound citation was present. There is
   no rendering fix for this, because the artifact was not malformed; it was unverified.
2. **It was caught by reading the paper, and only by that.** Not by review, not by formatting, not by the model.
3. **It propagated at the speed of copying.** The claim reached the chapter, the README narrative, a commit
   message and `PLANS.md` before anyone opened the PDF.

This is not a local embarrassment. Measured on GPT-4o across six simulated literature reviews, **19.9% of
generated citations were entirely fabricated**, and of the 141 that referred to real work, **45.4% carried
bibliographic errors** — most often an incorrect or invalid DOI (37.8% of those given one).[^linardon2025] The
same study found fabrication rising sharply with unfamiliar topics: 6% for major depressive disorder against
28–29% for less visible ones.[^linardon2025] Our incident is the ordinary case, not the exception.

## The principle — checked, or said to be unchecked

A citation makes a promise on behalf of the work: *a reader who follows this will find it says what I said it
says.* The promise is what gives a cited sentence its authority, and the authority is what makes an unverified
citation harmful rather than merely incomplete — it borrows the credibility of a check nobody performed.

So the app may hold exactly two honest positions about any citation:

- **Checked.** The source was retrieved and the quotation was found in it. The claim may stand on it.
- **Not checked.** Said so, visibly, in the same breath as the claim.

There is no third position, and in particular **"the writer says it is verified" is not one**. A verified flag
that a person sets is precisely the artifact that failed above: the ch.39 footnote was, in effect, asserted
verified by its author, and the assertion was worth nothing. Verification is an ACT — fetch the source, find the
quotation — and its absence is a fact about the app's knowledge, not a preference.

## Where this sits

[ch.32](32-referenced-knowledge.md) governs knowledge entering the work: retrieved, never recalled, with the
source's own words. This chapter is that doctrine turned outward. The two share a spine — a claim, a locator, a
quotation, a receipt — and differ in direction and therefore in obligation: an incoming reference must be
admissible before Reframe believes it; an outgoing citation must be checkable before a READER is asked to.

An outgoing citation is also an outward act, so it inherits what already governs those: what leaves is bounded and
shown ([ch.34](34-a-question-that-leaves-the-work.md) rules 4–6) — the identifier and the source's own quoted
words may travel, the writer's unpublished composition never does — and whose lane and whose money is stated
before it runs ([ch.20](20-on-device-first-and-the-writers-key.md)).

## Unverified is a breakdown, and must be rendered loud

The scoring kit already draws the distinction this needs. Its `.ambiguity` is *a result* — the material genuinely
supports more than one reading — while `.failure` is *a breakdown*: not assessed, ungrounded, or at risk of being
invented, and a renderer "is expected to make `.failure` louder, never to launder it into a calm open question".

An unverified citation is a `.failure`. It is not an open question about the source; it is an absence of
knowledge, wearing the costume of scholarship. A withdrawn one is the same. Only a checked citation is settled,
and a citation whose source was read and does NOT support the claim is a `.failure` that must be resolved by the
writer, never quietly dropped.

This is the property that would have caught ch.39 before publication: the claim would have carried a loud lane
saying *no one has opened this*, rather than reading as finished work.

## Withdrawal is recorded, not erased

When a citation fails verification, the claim it supported does not silently lose a footnote. The withdrawal is
part of the record: what was claimed, what was cited, what the source actually says, and when it was withdrawn.
ch.39 keeps its own withdrawal in the chapter text for exactly this reason — a corrected artifact that hides the
correction teaches nothing and cannot be audited.

Every citation therefore keeps its address ([ch.36](36-every-gap-keeps-its-address.md)): the claim can be reached
from the score, the source from the claim, and the withdrawal from both.

## What this does not license

- **Not a bibliography feature.** Formatting a reference list is not verification, and a well-formatted
  unverifiable citation is the exact object this chapter exists to prevent.
- **Not the model producing citations.** [ch.32](32-referenced-knowledge.md) rule 1 stands: a source is retrieved,
  never recalled. A model may say what kind of work would support a claim; it may not supply the reference.
- **Not automatic assent.** A checked citation means the quotation is really there. Whether it SUPPORTS the claim
  is the writer's judgement, presented to them, never inferred by the app
  ([ch.32](32-referenced-knowledge.md) rule 7).
- **Not a blocker on writing.** A writer may make a claim with no citation at all. That is an honest, unscored
  sentence; the failure state is reserved for a citation that claims a check that did not happen.

## Rules

1. **A citation carries a resolvable identifier** — DOI, arXiv id, ISBN, or a URL — and enough bibliographic
   detail for a reader to find the work without it.
2. **Verification is an act performed by the app**: the source is retrieved and the quotation is found in it.
   Nothing else may set a citation to checked.
3. **An unchecked citation renders as a breakdown**, at the same prominence as the claim it supports — never as a
   quiet footnote, and never laundered into an open question.
4. **A citation whose source contradicts the claim is a breakdown the writer resolves.** The app states the
   disagreement and does not choose ([ch.32](32-referenced-knowledge.md) rule 7).
5. **A model never supplies a citation** ([ch.32](32-referenced-knowledge.md) rule 1). It may name the kind of
   source that would settle a claim.
6. **The quotation is the source's own words**, selected mechanically, exactly as an incoming reference requires.
7. **A withdrawal is recorded with its reason** and remains reachable from the claim it once supported.
8. **Every citation keeps its address** ([ch.36](36-every-gap-keeps-its-address.md)): claim ↔ score ↔ source, both
   ways.
9. **Verification obeys the outward rules**: bounded content leaves ([ch.34](34-a-question-that-leaves-the-work.md)),
   the writer's unpublished composition never leaves, and the lane and its cost are stated
   ([ch.20](20-on-device-first-and-the-writers-key.md)).
10. **An uncitable claim is allowed and unscored.** This governs citations, not assertions.

## Showing evidence — the check the writer can make herself

**Status: not implemented.** This section governs a Copilot feature that does not exist yet. It is written before
the code, and the capability identity it names is declared **unavailable** in the registry
([ch.37](37-copilot-capability-governance.md)) until it satisfies what is below. Nothing here describes current
behaviour.

The writer must be able to inspect the bounded evidence that supports a citation or research result without being
sent into an open web. The evidence surface is a structured, read-only record: provider, work or record identity,
locator, retrieval time, content digest, the source's own quotation or extracted passage, provenance, and checked or
unchecked state. It is not a page browser and it is not a second reading surface.

The textual evidence and the rendered evidence are one bundle. When the provider returns a source that can be
rendered, WebKit may produce a read-only snapshot of that exact retrieved page state. The snapshot is evidence of the
retrieval, not a new source. It must remain addressable beside the quotation and receipt, so the writer can see the
words that were cited in the source presentation that produced them.

### What this must not become

- **Not a browser.** The view exists to display a *bounded evidence record*, not to navigate. Following a link is not
  available from Reframe. A new retrieval requires a new explicit, mediated research or citation request, governed
  by [ch.34](34-a-question-that-leaves-the-work.md) rules 4–6 and [ch.20](20-on-device-first-and-the-writers-key.md).
- **Not a way to set `checked`.** Looking is not verifying. Rule 2 is unchanged: the act is retrieve-and-find, and
  a writer who reads the page has still not performed it.
- **Not a service reporter.** [ch.48](48-a-service-is-a-fact-not-a-symptom.md) governs what happens when a call
  fails; a rendered page and a dead transport share an idiom and nothing else. A spawned CLI failing over MCP has
  no page to render, and treating that resemblance as a mechanism is the error ch.48 exists to stop.

### Rules for the reading surface

11. **What is shown is what was retrieved.** The evidence record is the retrieval that produced the receipt. If it
    must be fetched again, the app says so and re-performs the check.
12. **The quotation is located in the returned evidence.** The record names the locator and preserves the source's
    own words; the writer is not asked to search an unbounded page.
13. **Retrieval is an explicit outward act and is bounded as one.** The provider, purpose, scope, lane, and cost are
    stated before it runs. The writer's unpublished composition never leaves.
14. **The evidence surface is read-only.** Nothing may be edited, submitted, navigated, or authenticated into from
    it. It is evidence, not a web client.
15. **Evidence that cannot be returned says so, in place** — offline, refused, unavailable, or without a checkable
    quotation — with the same prominence as an unchecked citation. "Could not retrieve" is a state, never a blank pane.
16. **Text and snapshot share one evidence identity.** A citation bundle binds the claim, provider, locator, retrieval
    receipt, timestamp, response/content digest, exact quotation, and WebKit snapshot to one retrieval identity. A
    screenshot from another request, a quotation copied from another response, or a page rendered after navigation
    cannot satisfy the bundle.
17. **WebKit is an evidence renderer, never a browser.** The snapshot is read-only and non-navigable: no links,
    forms, authentication, redirects into a new source, or arbitrary URL entry. A new source requires a new mediated
    retrieval and a new evidence bundle.
18. **The bundle is atomic in presentation.** Reframe must not present the quotation as checked while omitting its
    matching receipt or snapshot when one was available. If any required member is missing or mismatched, the bundle
    is visibly unchecked or failed, never silently repaired from a different fetch.

## Acceptance

The doctrine is met when:

1. No citation can reach the checked state without a retrieval receipt and a quotation located in the fetched
   source.
2. An unverified or withdrawn citation is visible at the claim, and is rendered in the breakdown register rather
   than the settled one.
3. Following a citation from the uncertainty display reaches the claim, and following it from the claim reaches
   the source — demonstrated on the standing case, ch.39's withdrawn footnote.
4. A withdrawal remains in the record with its reason after the claim has been corrected.
5. No model-supplied reference can enter the work.
6. Verifying a citation sends the identifier and the source's own words, and nothing of the writer's composition.
7. A citation evidence bundle can be opened and shows its exact quotation, locator, retrieval receipt, content
   digest, and matching WebKit snapshot, all resolving to the same retrieval identity.

**For the reading surface, when it is built** (it does not exist today, and until it does the capability stays
declared unavailable per [ch.37](37-copilot-capability-governance.md)):

- A checked citation can be opened and the writer sees the bounded retrieved evidence with its quotation and locator.
- When renderable evidence exists, the writer sees the matching WebKit snapshot in the same evidence bundle; its
  receipt and digest agree with the quotation, and the snapshot cannot navigate.
- A new retrieval states its purpose, provider, lane, and any cost before it runs, and never carries the writer's
  composition.
- Evidence that cannot be returned renders its reason at claim prominence, never an empty pane.
- Inspecting evidence does not change any citation's checked state, and no web page can be navigated from Reframe.

## Governing sentence

Reframe shall let the work cite outward only in a form a reader could check, shall perform that check itself
rather than accept anyone's word that it was performed, and shall show an unchecked citation as the breakdown it
is — so that a sentence never borrows the authority of a verification that never happened.

## Sources

[^cavalin2020]: Paulo Cavalin, Victor Henrique Alves Ribeiro, Ana Appel and Claudio Pinhanez. *Improving
    Out-of-Scope Detection in Intent Classification by Using Embeddings of the Word Graph Space of the Classes.*
    EMNLP 2020. <https://aclanthology.org/2020.emnlp-main.324/>. Cited here only as the subject of the withdrawn
    claim recorded in [ch.39](39-a-model-cannot-be-told-what-it-cannot-do.md); the paper does not support that
    claim, which is the point.

[^linardon2025]: Jake Linardon, Hannah K. Jarman, Zoe McClure, Cleo Anderson, Claudia Liu and Mariel Messer.
    *Influence of Topic Familiarity and Prompt Specificity on Citation Fabrication in Mental Health Research Using
    Large Language Models: Experimental Study.* JMIR Mental Health, 2025;12:e80371.
    doi:[10.2196/80371](https://doi.org/10.2196/80371). Of 176 citations generated by GPT-4o across six literature
    reviews, 35 (19.9%) were entirely fabricated; of the 141 non-fabricated, 64 (45.4%) carried bibliographic
    errors, most often an incorrect or invalid DOI (51 of 135 given one, 37.8%). Verified against the article
    text, per [ch.39](39-a-model-cannot-be-told-what-it-cannot-do.md) rule 9.
