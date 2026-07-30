# Referenced Knowledge — What the World Knows Outside the Book

> Chapter summary: Some things a manuscript needs known are not in it. *Kinch is Stephen Dedalus* is a settled fact of
> Joyce scholarship that Telemachus never states, so a world built only from what the text says cannot work it out —
> and [ch.31](31-compiled-knowledge.md) rule 4, which requires every entry to cite the passage that put it there,
> makes such knowledge structurally impossible. This chapter admits a third kind of evidence and governs it: a
> **reference** — another book, an edition, a link, a scientific source — cited well enough that a reader who doubts
> it can follow it. Its first-class rule is the one that answers the question every student asks about AI and
> citation: **references are retrieved, never recalled.** A model may say what kind of source would settle a
> question; it may not produce the source from memory. A citation is a claim about an external work's existence and
> content — verifiable, and therefore to be verified. And referenced knowledge may never pass as textual evidence:
> the manuscript remains the only authority on what the manuscript says.

## Purpose — the failure this exists to end

**Two failures, opposite in shape, and this chapter sits between them.**

**A world that can only know what the text spells out.** Measured on Telemachus, after a full reading with everything
this refactor has built: the world holds *Kinch* and *Stephen Dedalus* as **two people**. Both are correct entries —
each name occurs, each is evidenced, each was confirmed by a reading. And they are one man. The chapter never says
so; Mulligan simply calls him Kinch. No amount of closer reading of these 1,118 lines fixes it, because the fact is
not in them. It is in the scholarship — Gifford's *Ulysses Annotated* settles it in an entry — and the app had no way
to hold a fact of that kind at all.

The correction path built for this ([ch.30](30-the-living-gazetteer.md) rule 9) assumed the writer would supply what
the text withholds. The writer's own objection to that, and it is decisive:

> *"I do see the writer's willingness to edit in corrections very critical — in almost all situations people let the
> best model decide, and maybe Google it. Knowledge from people's understanding is to be referenced, too — and this
> reference is another book, a link, a clear scientific reference."*

Writers do not curate. Asked to adjudicate identities, they will delegate — to the best model available, or to a
search — and they are right to, because *Kinch is Stephen* is not a judgement anyone needs to make. It is something
known, by other people, in named places.

**And the failure that admitting references invites, which is worse.** A language model asked for a reference will
produce one: a plausible author, a plausible title, a page number of the right shape. This is the most documented
failure of the technology and the most damaging, because a footnote **reads as authority**. An invented citation does
not merely state something false; it states it in the register of things that have been checked, and it defeats the
reader who would otherwise have doubted. A world that admitted such citations would be worse than the world that
could not know Kinch is Stephen — it would be a world that could not be trusted about anything.

So the question is not whether to allow referenced knowledge. It is what a reference has to be before it counts.

## The principle — retrieved, never recalled

**A citation is a claim about an external work: that it exists, and that it says a particular thing.** Both halves
are verifiable. Anything verifiable must be verified rather than generated.

Therefore:

- The system may **retrieve** a reference — fetch the work, the record, the entry, the page — and cite what it
  fetched, with the words that bear the claim.
- The system may **not recall** a reference. A model's memory of a bibliography is not a bibliography. Where the
  work was not fetched, there is no reference, however confident the account of it.
- A model may legitimately say *what kind of source would settle this* — "an annotated edition would list this
  byname" — and that is a research plan, not a citation. The distinction is not stylistic. One can be followed; the
  other only sounds as though it could.

This is the whole of the honest answer to *how does AI handle scientific referencing*: it does not produce
references. It produces the **retrieval of** references, and shows its work.

## What a reference has to carry

A citation is admitted when a reader who doubts it can check it without asking anyone. That requires, at minimum:

- **The work**, named as a reader would name it — author, title, edition. "The literature" is not a work; "as is
  well known" is not a work.
- **A locator** — the page, entry, line, section, DOI, or identifier that addresses the claim inside the work. A
  reference to a 600-page book with no address is a gesture.
- **The quotation that bears the claim**, in the source's own words. This is the part usually omitted and the part
  that matters most: it lets a reader judge the *inference* from the source, not merely trust that one was made. A
  citation without it asks to be believed about two things at once.
- **A way to follow it, where one exists** — a URL, an archive identifier, a library record. A link is not required;
  being followable is. Links rot, so the locator must survive the URL's death.

A reference missing the work or the locator is not a weak reference. It is not a reference.

## Precedence — who wins, about what

Three authorities now speak, and conflating them is how scholarship comes to overrule the page it is about:

| The question | Who is authoritative | Why |
|---|---|---|
| What does the manuscript *contain*? | **The text**, at coordinates | It is the only immutable source ([ch.13](13-storage-and-performance.md)) |
| What does this *world* hold — a byname, a date, a usage, a place | **A reference**, cited | It is where such things are known |
| What is *true for this work* when these disagree | **The writer**, having been shown both | It is their manuscript ([ch.30](30-the-living-gazetteer.md) rule 9) |

Two consequences follow, and both are rules below. A reference may never assert what a passage contains — if a
source says a scene contains a milkman's shop and the lines do not, the lines are right and the source is about
something else. And the writer's authority is exercised **on a presented disagreement**, not on a blank prompt: the
difference between "who is Kinch?" and "Gifford's annotations say Kinch is Stephen Dedalus — shall I record that?"
is the difference between delegating work to the writer and asking them to decide.

That reorders the human's role, deliberately. The writer is not the **curator** of the world's knowledge — asked to
type in what the app lacks. They are its **arbiter of last resort**: best reasoning first, then reference, and their
judgement invoked when those disagree or fail, on a question already made small enough to answer in a word.

## Scholarship disagrees with itself

A reference is not a fact. It is a record of what a source says, and sources conflict, revise and go out of date.
So a referenced entry holds the **reference**, not the truth — and a second source that disagrees is recorded
**beside** the first, not instead of it ([ch.30](30-the-living-gazetteer.md) rule 5 applies unchanged).

This is why the quotation is required rather than encouraged. Two annotators disagreeing about a byname is a fact
about the scholarship, useful to a writer, and invisible unless both were quoted rather than summarised.

An editorial consensus may be stated as one — "every annotated edition glosses this the same way" — only when the
editions were fetched and can be listed. Otherwise it is recall wearing a plural.

## No laundering

The failure that will actually happen, if nothing forbids it: a fact enters through a reference, is compiled into
project memory, is read by a later pass as part of the world, and three passes later the app **knows** it with no
account of where it came from. Provenance decays into confidence.

So: **the kind of evidence an entry rests on travels with it forever, and is never flattened.** Nothing in the app
says "confirmed" where it could say which of the three confirmed it. A surface that shows the world shows, for each
thing in it, whether the manuscript said so, a source said so, or the writer said so — because those are three
different reasons to believe something and a writer's response to each is different.

Negative results are knowledge too: *"I looked for a source for this and found none"* belongs beside what was found,
for the same reason an unresolved name is a result rather than an absence
([ch.24](24-the-reasoning-is-an-uncertainty-map.md), [ch.31](31-compiled-knowledge.md) rule 2).

## What may be referenced, and what may not

Referenced knowledge is admitted for **facts about the world the work belongs to** that a source can settle:

- an established byname, alias, patronymic or title (*Kinch* for Stephen; *Buck* for Malachi Mulligan);
- a place, institution, currency, custom, or dating a reader of the period would know;
- a language, a quotation's origin, a liturgical or scientific term;
- an editorial or textual fact about the work — variants, editions, published emendations.

It is refused, absolutely, for:

- **what a passage contains** — that is measurement and reading ([ch.29](29-natural-language-measures-storify-interprets.md));
- **what the work means** — a source may inform an interpretation; it may never become one
  ([ch.12](12-animating-truth.md));
- **what the writer intends** — no reference outranks the author of the draft;
- **dramaturgical judgement** — whether a beat works is nobody's citation.

## Amendment — what is not reachable but is knowable

The rule above — retrieved, never recalled — collapses two very different things into nothing, and the writer caught
it while granting the allowance to fetch:

> *"You are allowed to fetch what's useful, reachable, trustful in a measurable way — and honestly, what is not
> reachable, but knowable (from books or the world outside) as is and as it happens. And this is an allowance that is
> given for Reframe, too."*

**Gifford's *Ulysses Annotated* settles Kinch, and it is a book.** No endpoint returns it. Treating that as
*unknown* is its own dishonesty: the answer exists, its location is known, and the app can say so. What it must not
do is act as though it had read it.

So there is a third state, and it is neither evidence nor silence:

- **Fetched** — retrieved, quoted, followable. May confirm (rules 1–2).
- **Named but unreachable** — a work that exists and would settle the question, identified as precisely as it can be,
  explicitly not consulted. **May be stated; may never confirm.** It is a signpost: it tells a writer where the answer
  lives so they can go and get it, or decide from their own knowledge of it.
- **Recalled** — a citation produced from a model's memory. Prohibited, because it is indistinguishable in form from
  the first and carries none of its warrant.

The line between the second and the third is not what the model knows; it is what the app **claims**. "Gifford's
annotations gloss the bynames — I have not consulted them" is honest and useful. "Gifford, *Ulysses Annotated*, p.
14: Kinch is Stephen's byname" is a fabrication unless page 14 was actually read.

And the allowance's other half — **trustful in a measurable way** — is a requirement on what a fetch must record.
Trust in a source is not asserted; it is made checkable by keeping the retrieval itself: when it happened, what was
asked, what came back verbatim, and from where. A reference whose retrieval was not recorded is a reference nobody
can audit, which by this chapter's own standard is not a reference.

## Rules

1. **References are retrieved, never recalled.** Producing a citation from a model's memory is prohibited outright.
   A work that was not fetched may still be NAMED as where an answer lives — honestly, as unconsulted — and in that
   state it may inform a question and never confirm an entry.
2. **A citation carries its work, its locator, and the quotation that bears the claim** — and a way to follow it
   where one exists. Missing the work or the locator, it is not admitted at all.
3. **Referenced knowledge is marked as referenced, forever.** The three kinds of evidence — the text, a reference,
   the writer — are never flattened into "confirmed", on any surface or in any store.
4. **A reference may never assert what a passage contains.** Where a source and the lines disagree about the text,
   the lines are right.
5. **A referenced entry holds the reference, not the truth.** A conflicting source is recorded beside it; neither
   silently replaces the other.
6. **A consensus may be claimed only from sources that were fetched and can be listed.**
7. **The writer decides on a presented disagreement**, never on a blank prompt. Asking them to supply what could
   have been retrieved is delegating work, not seeking judgement.
8. **The order of resort is reasoning, then reference, then the writer** — and the writer's word, once given, wins
   over both and is recorded as theirs ([ch.30](30-the-living-gazetteer.md) rule 9).
9. **A search result is not a reference** unless it names a work and can be followed. A snippet is a lead.
10. **Nothing referenced may gate a reading.** The manuscript is readable with no reference at all; references
    improve a world and are never required by one ([ch.31](31-compiled-knowledge.md) rule 4's removability).
11. **A failed search is recorded.** That a source was sought and not found is knowledge, and it stops the same
    search being paid for again.
12. **No spend on retrieval without the writer's yes**, at the call site, per act
    ([ch.26](26-internals-tune-themselves.md)) — a reference is worth paying for, and it is still their money.
13. **A retrieval records itself** — when, what was asked, what came back verbatim, and from where — because trust in
    a source is made measurable, never asserted. An unrecorded retrieval yields no admissible reference.
14. **Reachability is stated, not implied.** Where the app knows a work would settle a question and cannot reach it,
    it says both: what the work is, and that it has not read it.

## Acceptance

- No citation exists in the store that was not fetched; each carries work, locator and quotation.
- Every surface that shows a fact from the world shows which of the three kinds of evidence it rests on.
- A source contradicting the text about the text loses, visibly, with both recorded.
- A writer is never asked to identify something a fetched reference would have settled.
- Two sources disagreeing are both present, quoted, and attributed.
- Deleting every reference leaves the manuscript readable and every reading performable.
- A search that found nothing is recorded, and is not repeated without new grounds.
- Every fetched reference has its retrieval on record: the moment, the request, the response, the origin.
- A work named but unconsulted is labelled as such wherever it appears, and has confirmed nothing.

## Governing sentence

Reframe shall admit knowledge from outside the manuscript only as a reference it has actually fetched, cited well
enough for a doubting reader to follow, marked as referenced for as long as it is held — and shall never let such
knowledge speak about what the pages themselves contain.
