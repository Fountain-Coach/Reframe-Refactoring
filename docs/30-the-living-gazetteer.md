# The Living Gazetteer

> Chapter summary: Every work invents its own world — people, places, objects, institutions, idioms, names whose
> meaning accumulates as the work unfolds — and a reader builds that vocabulary while reading. Reframe re-derived it
> on every pass. **The Living Gazetteer** is the continuously accumulating record of *what the source has already
> established to exist*: candidates observed by the measured tier ([ch.29](29-natural-language-measures-storify-interprets.md)),
> confirmed by the reading, held with their provenance, revisable, and never authoritative about meaning. It answers
> one question — *what, in this world, has already become true?* — and refuses the others. It is **not** the
> semantic index [Phase 6](03-current-state-and-problem.md) removed: it holds no interpretive authority, routes no turn,
> answers no story question, and every entry in it is traceable to the passage that put it there and revisable by
> the writer in a sentence.

## Purpose — the failure this exists to end

**Every read starts from nothing.** A model reading passage forty has no memory that passage three established a
tower, that *Kinch* and *Stephen* are one man, or that the key has changed hands twice. It re-infers the world from
local context, every time, and pays for it in three currencies: tokens spent re-deriving what is already known,
latency, and error. Measured on Telemachus: **28 names in, 28 identities out** — the reading never worked out that
any two of them were the same person, which is precisely the state in which it went on to invent a conflict between
"Stephen" and "Dedalus", and to weld *Stephen* and *Buck Mulligan* into a person called "Stephen Mulligan" that no
line of the chapter contains.

**And the opposite failure, which this app has already suffered.** The semantic index was a parallel derived corpus
that acquired authority: it answered questions, gated steps, and drifted from the source it claimed to describe.
Phase 6 removed it, and the governing sentence of this refactor still forbids "index-derived authority" in the
production path. A persistent memory of a fictional world can become exactly that — and this chapter exists to
define, precisely, what keeps it from doing so.

The difference is not size or storage. It is **authority**:

| | The removed index | The Living Gazetteer |
|---|---|---|
| Claims | what a passage MEANS | what the source established EXISTS |
| Answers | story questions, routing decisions | none — it is consulted, never asked |
| Entry | derived automatically | observed, then CONFIRMED by the reading |
| Traceability | a vector, unattributable | every entry cites the passage that made it |
| Correction | re-index and hope | the writer edits it in a sentence; history is kept |
| On disagreement with the source | silently wins | is wrong, and says who confirmed it |

## The principle — observation becomes memory, and stops there

**The measured tier observes. The Gazetteer remembers. Storify decides.**

The Gazetteer's only question is *what has the source already established to exist?* It deliberately does not
answer *what does this mean*, *why did this happen*, *what is its dramatic function*, or *what did the author
intend* — those are reading, and reading is [ch.12](12-the-copilot-is-one-reasoning.md)'s single reasoning working
under [ch.05](05-grounding-first.md)'s declared intent.

Its authority is therefore **linguistic and historical**, never interpretive: it knows that a name occurred, where,
how often, in what company, and that a reading confirmed those occurrences to be one person — and it knows who
confirmed that and when.

## The world learns while being read

The Gazetteer begins **empty**. It is not compiled before analysis; it accumulates during it.

1. **Observation.** The measured tier reports: *possible personal name "Stephen" at sentences 41, 89 and 103.*
   Nothing else happens. An observation is not an entry.
2. **Candidate.** Repeated, located observations of a surface form become a candidate with evidence attached: its
   occurrences, the pronouns and action lemmas near them, first and last appearance.
3. **Confirmation.** The reading — and only the reading — decides that a candidate is a thing in this world, and
   which surface forms are the same thing. Confirmation is an act with an author and a moment.
4. **Revision.** Later passages split what was merged, merge what was separate, name what was anonymous. Earlier
   belief is superseded, not deleted.
5. **Retirement.** An entry the source never supported is withdrawn, with the reason kept.

From the moment a thing is confirmed, every later passage is read by a reading that already knows it exists. That
is the whole gain: the world is established once and consulted thereafter.

## Canonical identity, and the surface forms it was found under

An entity has exactly **one** canonical identity and **many** surface forms. *Stephen*, *Dedalus*, *Mr Dedalus*,
*Kinch*, *the young teacher* may all resolve to one man — and the Gazetteer records the canonical identity, every
observed form, and the passages that support each association. Identity is stated once and then known, rather than
re-inferred and re-guessed on every read.

Two rules govern that resolution, both learned the hard way:

- **Distinct people are never merged by resemblance.** Sharing a surname, sharing a scene, or being mentioned
  together is not identity. Union-find over pairwise similarity once merged Haines into Stephen.
- **A merge is a claim, and is shown as one.** The writer can split it in a sentence — which is worth more than the
  app being quietly right most of the time.

## Provenance is part of the entity

Every entry records when it first appeared, where, which passages support it, who confirmed it, what was revised,
what competing hypotheses existed, and how confidence moved. Nothing exists in the Gazetteer without evidence, so
any later conclusion can be walked back through an unbroken chain to the lines that produced it.

This is what makes the Gazetteer inspectable rather than authoritative: an entry is never *the truth*, it is *what
was confirmed, from this, by this, then*.

## The world remembers change

The Gazetteer stores **history, not snapshots**. Characters evolve; relationships become explicit; objects acquire
weight; an anonymous figure receives a name at line 900. A reading that has to be re-run because the writer edited
the manuscript may split an identity that was merged — and the earlier belief remains visible as a superseded
revision rather than vanishing, because a world that silently rewrites its own past cannot be audited.

Relationships are held on the same terms — *parent of*, *married to*, *works at*, *located in*, *travels with*,
*alias of* — each backed by the passage that grounded it, never by plausibility.

## Retrieval begins after identity, not before it

When the reading reaches a passage naming *Bloom*, it does not begin from an empty window. It receives the
canonical identity, the known aliases, the previous appearances, the grounded relationships, and the passages
establishing each — and only then does resemblance-based retrieval ([ch.29](29-natural-language-measures-storify-interprets.md)
rule 4) offer further passages that may bear on it.

This ordering is the point. Retrieval over an ungrounded world returns passages that merely *sound* related;
retrieval after identity returns passages about the same person.

## Where it lives

In FountainStore, with everything else this project remembers — not as an index, but because a work must have **one**
memory rather than many competing caches. Beats, cuts, continuity audits, the story view, copilot turns and every
future reading consult the same vocabulary. It is written against the immutable source by coordinate
([ch.13](13-one-immutable-source.md)): the Gazetteer never materialises text into the manuscript, and the manuscript
never depends on the Gazetteer to be readable.

## Incomplete on purpose

Completion is not a goal and would be a lie. A later reading finds what an earlier one missed; a writer revises the
world's ontology; a minor figure turns out to matter. The Gazetteer's value is in being **continuously correct**,
never in claiming to be finished — and an empty or thin Gazetteer is an honest state that must never be disguised
by invention.

## Human authority

The writer is the final authority on their world. Every confirmed entity is inspectable, every alias editable,
every relationship challengeable, every revision preserved. Where the writer and the Gazetteer disagree, the writer
is right and the correction is recorded as theirs.

## Rules

1. **The Gazetteer answers only "what has the source established to exist?"** It never answers what something
   means, why it happened, what it is for, or what the writer intends.
2. **Nothing enters without confirmation by the reading.** The measured tier may only produce candidates; a
   candidate stored is still a candidate.
3. **Every entry carries its provenance** — passages, confirmer, moment — and an entry that cannot cite the source
   that produced it is invalid.
4. **One canonical identity, many surface forms**, with the association evidenced per form. Distinct people are
   never merged by resemblance, and a merge is shown as the claim it is.
5. **History is kept.** Merges, splits, namings and retirements supersede; they do not erase.
6. **The Gazetteer is consulted, never asked.** It routes no turn, sets no status on the uncertainty map, gates no
   step, and answers no story question — the prohibition that separates it from the index Phase 6 removed.
7. **Retrieval follows identity**; resemblance never establishes it.
8. **It never writes into the source** ([ch.13](13-one-immutable-source.md)) and the source never depends on it.
9. **The writer overrides it**, and the override is recorded with its reason.
10. **Incompleteness is stated, never filled.** A thin world is reported as thin; nothing is invented to round it
    out ([ch.24](24-the-first-reads-product-is-uncertainty.md)).

## Acceptance

- Every entry names the passages that established it, and clicking through reaches those lines in the source.
- No entity exists that a reading did not confirm; candidates are visibly distinct from confirmed entities.
- A merge or split can be performed by the writer in a sentence, and the previous state remains visible afterwards.
- A second reading of the same manuscript consults the existing world instead of re-deriving it, and says so.
- No routing decision, uncertainty status or story answer is taken from the Gazetteer.
- Deleting the Gazetteer leaves the manuscript whole and readable; only accumulated knowledge is lost.
- The count of confirmed identities is honest — 28 names resolving to 28 identities is reported as a world nobody
  has worked out yet, not as a cast.

## Governing sentence

Reframe shall accumulate, from what the reading confirms and the source can evidence, the vocabulary of the work's
own world — holding it with its provenance, its history and its corrections, consulting it before every later
reading, and never letting it say what any of it means.
