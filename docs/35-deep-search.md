# Deep Search

> Chapter summary: A search engine cites a page; the answer is often not on it. Measured: asked who Kinch is in
> *Ulysses*, the search cited a Joyce annotation site whose page is a **list of note titles** — "Kinch" appears
> there as a link label, and the annotation itself is one click away. A lane that quotes the page it was handed
> either quotes nothing or quotes a run of link labels as if it were prose. **Deep search is following a source's
> own links to the passage that actually answers** — and its bounds are the whole difficulty. A depth limit is a
> number we made up; whether a link is worth following is a JUDGEMENT, and it belongs to the local lane, reasoning
> for free over the link labels and over everything FountainStore already holds. A hop is taken because it is
> semantically likely to reach the answer, never because a counter has not run out; and a search that stopped says
> WHY it stopped, because "I stopped looking" and "there is nothing there" are different facts.

## Purpose — the failure this exists to end

**The cited page is a signpost, and we were treating it as the destination.**

Measured on 2026-07-31, against the real provider and the real web. Asked *"In James Joyce's Ulysses, who is called
'Kinch'?"* with the search tool required, the model cited one document: a page on a Joyce annotation site. Three
facts about that page, in order of discovery:

- A plain `URLSession` fetch returned **948 bytes** — a JavaScript shell with no prose in it at all. The lane could
  point at a source and could not read a word of it.
- Rendered in a browser, the same page yielded **22,119 characters**. The instrument was the problem, not the page.
- And what those characters say is: *"…John Eglinton · John Wyse Nolan's wife · Joking Jesus · Julius Caesar ·
  Kathleen Kearney · Kevin Egan · Kickshaws · **Kinch** · King Billy · King Edward · Kingsbridge Station…"*

It is an **index**. "Kinch" is a link label. The annotation that answers the question is one hop away, and the page
we were handed contains no sentence about him at all. Quoting the run of labels between two full stops would put a
paragraph of navigation in front of the writer wearing a source's authority — the exact failure
[ch.32](32-referenced-knowledge.md) exists to prevent, arrived at from a new direction.

**And the failure this chapter must not commit in fixing it.** The obvious repair is a crawl with limits:
`maxDepth = 2`, `maxPages = 6`, follow the first three links. Those numbers are ours. They encode no knowledge of
the source, they are wrong for the next site, and a search that stops because a counter ran out reports the same
"nothing found" as a search that genuinely looked — which is the silence
[ch.33](33-a-want-is-a-gap-in-a-ledger.md) forbids, one tier out. A constant is what we write down when we have not
worked out what the question actually is.

## The principle — a hop is a judgement, not a decrement

The question is never "how deep are we". It is **"is this link likely to reach the answer?"** — and that is
answerable, cheaply, from things already in hand:

- **The link's own label.** A reader deciding whether to click reads the words on the link, and so does this. That
  a label is the exact subject of the question — `Kinch` — is the strongest signal a site can give, and it is
  measured, not inferred.
- **What the page around it is.** A page of many short labels is an index; a page of sentences is prose. Countable
  ([ch.27](27-parse-before-you-ask.md)).
- **What the project already holds.** FountainStore knows the world, the passages, and every search already made.
  A link toward something the project has already settled is not worth a hop, and a link toward a question the
  ledger records as a dead end is worth less than one nobody has tried.

Where those do not settle it, the judgement is **reasoned by the LOCAL lane** — on this Mac, free, and therefore
affordable at every hop ([ch.20](20-on-device-first-and-the-writers-key.md)). It is given the labels, the shape of
the page, and what the world already knows, and it says which link, if any, is worth following and why. That
"why" travels with the hop, so a deep search is legible as a sequence of reasons rather than a trail of URLs.

**The reasoning is local and it stays local.** The paid lane found the document; deciding where to click inside it
is not worth the writer's money, and a lane that spends per hop would make depth expensive precisely where it
should be cheap.

## What a hop may not do

- **It may not leave the work being consulted.** The writer consented to asking a source, not to a walk across the
  web. Following the site that was cited is reading that source; following a link off it is asking a different one,
  which is a different act and needs its own grounds.
- **It may not re-read.** A page already rendered in this search is not rendered again.
- **It may not follow a link it cannot justify.** No candidate worth a reason is a stopping condition, not an
  invitation to try the rest in order.
- **It may not spend the writer's money to choose.** See above.
- **It may not change what is quoted.** Whatever page the search ends on, the quotation is still the document's own
  sentence, selected by literal match, still guarded by the work-mention test, and still never the model's prose
  ([ch.32](32-referenced-knowledge.md) rule 2, [ch.34](34-a-question-that-leaves-the-work.md) rules 7 and 8).

## Where it stops, and saying which

A deep search ends in exactly one of four ways, and the writer is told which:

1. **It found the passage.** A page bearing a quotable sentence about the subject, in the work. The citation is
   that page — the one that answers — not the one that was first handed to us.
2. **Nothing left was worth following.** The reasoning had no candidate it could justify. That is an honest end and
   a real result: this source does not appear to hold it.
3. **The writer's limit was reached.** Rendering pages costs time and the writer's attention, so a search may be
   asked to stop. Stated as a stop, never as an absence.
4. **A page could not be read at all.** Named, with its URL, so the writer can open what the app could not
   ([ch.34](34-a-question-that-leaves-the-work.md) rule 8's sibling: found and unreadable is not "not found").

Only the first produces a citation. The other three produce a lead or a stated stop — and **none of them may be
recorded as a dead end that closes the question**, because a search that stopped has not established that the
answer is absent ([ch.32](32-referenced-knowledge.md) rule 11 is about grounds, not about effort).

## Every hop is on the record

A deep search is several outward acts, and [ch.32](32-referenced-knowledge.md) rule 13 governs each: when, what
was asked, what came back, and from where. To that this chapter adds **why** — the reason the hop was taken, in the
words the reasoning used. A trail of URLs is not auditable; a trail of reasons is, and it is the only way a writer
can tell a search that thought from one that wandered.

The record also makes the stop legible: a reader of the receipts can see the last thing considered and why it was
not followed.

## What this does not license

- **Not a crawler.** A deep search follows a source's own links toward one question and stops; it does not index a
  site, and it does not fetch what it was not sent toward.
- **Not a way around consent.** The writer's yes was to consult a source. Hops inside that source are part of the
  act they authorised; a hop to a different source is not, and needs its own.
- **Not a licence to read more of the manuscript.** What leaves is still only the question
  ([ch.34](34-a-question-that-leaves-the-work.md) rules 4 and 5). Depth is about the SOURCE, never about sending
  more of the writer's work.
- **Not a second reader.** Nothing found at depth is interpreted; it is quoted, and the writer decides
  ([ch.32](32-referenced-knowledge.md) rule 7).

## Rules

1. **The cited page is where a search STARTS.** A lane that quotes only the page it was handed has not read the
   source.
2. **A hop is taken because it is judged likely to reach the answer** — never because a depth or page counter has
   not yet run out. No constant may stand in for that judgement.
3. **The judgement is made by the local lane**, free, at every hop
   ([ch.20](20-on-device-first-and-the-writers-key.md)); the paid lane is never asked where to click.
4. **The judgement reads the link's own label, the shape of the page, and what FountainStore already holds** —
   measured first, reasoned only where measurement cannot decide ([ch.27](27-parse-before-you-ask.md)).
5. **A search stays inside the source it was authorised to consult.** Leaving it is a different act with its own
   grounds.
6. **A page is rendered once.**
7. **A page that cannot be read is named with its URL**, never counted as absent.
8. **A search that stops says why it stopped** — answered, nothing worth following, limit reached, or unreadable —
   and only the first yields a citation.
9. **A stop is never recorded as a dead end.** Rule 11's protection is about grounds, not effort; a question the
   app gave up on stays open.
10. **Every hop is recorded with its reason**, beyond ch.32 rule 13's when/what/where.
11. **Depth changes nothing about quotation.** The sentence is still the document's own, selected by literal match,
    still work-guarded, still never generated prose.
12. **Depth sends nothing further.** What leaves is the question and only the question.

## Acceptance

The doctrine is met when:

1. An index page whose link label matches the subject is followed to the page that bears the answer — demonstrated
   on the standing case, where the annotation is one hop from the cited page.
2. No depth, page-count or breadth constant appears in the traversal; removing the local reasoning stops the search
   rather than falling back to a fixed crawl.
3. The receipts show, for every hop, why it was taken — readable as a sequence of reasons.
4. A search that stops reports which of the four endings occurred, and the three non-answering endings leave the
   question open and re-askable.
5. A page that renders nothing is reported with its URL as unreadable, never as absent.
6. No hop leaves the consulted source, and no hop sends anything about the manuscript beyond the question already
   shown to the writer.
7. Deleting the deep search leaves the reference lane working on the page it was handed
   ([ch.33](33-a-want-is-a-gap-in-a-ledger.md) rule 12's removability).

## Governing sentence

Reframe shall treat a cited page as the beginning of reading rather than the end of it, follow a source's own links
only where the local reasoning can say why the next one is likely to answer, stop when nothing more is worth
following, and always say which of those happened — so that going deeper is something the app can justify step by
step, and never something it does until a counter runs out.
