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

## FountainStore is the knowledge plane

The web is not a second memory, and a frontier model is not a second store. **FountainStore is the operational
account of what this project knows, does not know, fetched, failed to fetch, inferred, accepted and superseded.**
Anything outside it is transient input. Anything a later pass may rely on must first have become an explicit
FountainStore artefact.

This does not mean that every statement in the store is declared true. It means the store tells the truth about the
project's epistemic state:

| What is held | What it is authoritative about |
|---|---|
| The canonical source, at coordinates | What the manuscript contains |
| A retrieval record | What was asked, what came back, when and from where |
| A referenced claim | What a named source supports, contradicts or does not settle |
| A writer revision | What is true for this work because its writer decided it |
| A failed search | What was sought on these grounds and not found |
| A named but unconsulted work | Where an answer may live, and that Reframe has not read it |

The distinction is load-bearing. A web response may be wrong, a source may conflict with another, and a model may
misread a quotation. FountainStore need not hide any of that to remain the source of operational truth; it must hold
each state under the right name, with the act and evidence that produced it.

So there is no artefact called `TruthIndex`, `WorldModel` or generic `KnowledgeBase`
([ch.31](31-compiled-knowledge.md) rule 13). There are narrowly owned artefacts whose names say what they hold. An
index or embedding may retrieve their identifiers. It may never become their authority.

## The store-native research compiler

The maximum useful place for an elevated model lane is neither free-running web research nor recurring runtime
chat. It is a **research compiler**: given a durable question the project has actually failed to settle, it plans a
bounded retrieval, reads only what was fetched and persisted, and compiles a typed, evidenced result that the local
lane can consult thereafter without paying again.

The flow is:

```text
FountainStore corpus + existing artefacts
                  |
                  v
        persisted knowledge gap
                  |
        store-first resolution
                  |
                  v
      scoped research act + writer's yes
                  |
                  v
       discovery -> fetch -> persist
         leads       evidence   receipt
                  |
                  v
     frontier compiler reads stored evidence
                  |
                  v
 referenced claims / conflicts / negative result
                  |
                  v
 Gazetteer or another narrowly owned projection
                  |
                  v
       on-device runtime consults it locally
```

The order contains the principal drift control: **persist before interpretation**. A model never receives a
transient browser page as operational context and then leaves only its summary behind. Retrieval writes the source
record first. The compiler reads that record from FountainStore. If the record was never written, nothing downstream
may act as though the page was seen.

The model response is not the citation. Work, locator, quotation, retrieval moment and origin are assembled from the
retrieval artefact. The model may state the inference between quotation and claim; it may not author or repair the
quotation, locator or source identity.

### Query the project before querying the world

Every research act begins inside FountainStore:

1. Consult the current Gazetteer and the other compiled artefacts that own this concern.
2. Consult prior referenced claims and retrieval records.
3. Consult writer revisions, which already win.
4. Consult failed searches and named-but-unreachable works.
5. Consult the current knowledge gap and the evidence generation that left it open.
6. Only when none of these settles the question may an external retrieval be proposed.

This is [ch.31](31-compiled-knowledge.md)'s ratchet applied to research. A fact the project has settled is read, not
researched again. A failed search is not repeated on identical grounds. A source already fetched is not fetched
again merely because another model turn began.

Similarity search and embeddings may nominate stored artefacts for this consultation. They remain measured
retrieval aids: the returned artefact and its evidence decide whether it bears on the question, never the similarity
score ([ch.29](29-natural-language-measures-storify-interprets.md)).

### A research act is claim-shaped and bounded

An unresolved token is not yet a web query. The reasoning first turns it into a claim-shaped research act:

> Determine whether an attributable external source identifies the manuscript name “Kinch” with the established
> project entity “Stephen Dedalus.”

The act carries:

- the question and corpus scope;
- the FountainStore artefacts and source coordinates that left it open;
- why this is external-world knowledge rather than something the manuscript can answer;
- the kinds of source that could settle it;
- what would support, contradict or fail to address it;
- the writer's grant for this act;
- what invalidates the result narrowly.

This is a structured project artefact, not a stored provider prompt. A model's remembered bibliography may suggest a
source *class* or search vocabulary. A proper name it recalls remains a named-but-unconsulted work until retrieval
establishes otherwise.

The grant is to this research act, not a general payment gateway and not a permanent web preference. Every
cost-bearing fetch or compiler call checks the act at its call site. If the question or scope materially widens, the
old grant does not cover it and the Copilot asks again ([ch.20](20-on-device-first-and-the-writers-key.md),
[ch.26](26-internals-tune-themselves.md)).

### Discovery, retrieval and compilation are different acts

Web search is useful precisely because it is broad, and dangerous for the same reason. Its stages therefore remain
separate:

1. **Discovery** finds candidates. Search results, snippets, model suggestions and catalogue hits are leads.
2. **Retrieval** opens a work, record, edition, entry or page and records what actually came back.
3. **Compilation** determines what the persisted source material supports about the project question.
4. **Promotion** changes a project artefact only under the precedence and conflict rules below.

A source adapter may address an annotated edition, institutional archive, library catalogue, DOI record,
encyclopaedia, Wikipedia/Wikidata, period dictionary, scientific reference or writer-supplied work. Wikipedia is a
useful adapter and often a useful discovery source; it is not the architecture. Source fitness is reasoned for the
question and made inspectable through provenance. There is no global numerical trust score that silently crowns one
domain authoritative.

The open web is untrusted data. Text fetched from it cannot issue tools, change the research act, widen the grant or
instruct the compiler to ignore project rules. It is presented to reasoning as quoted source material with an
origin, never as an instruction.

## Artefacts — one owner for each fact

The pragmatic implementation is a small family of FountainStore document kinds. Names may follow the repository's
document-id grammar, but their ownership does not vary:

| Artefact | Owns | Must not own |
|---|---|---|
| `KnowledgeGap` | The durable open question, its grounds and what would resolve it | A speculative answer |
| `ResearchAct` | Scope, purpose, grant, state and invalidation | Retrieved content |
| `SearchAttempt` | Query, source, moment and found/lead/failed outcome | A citation |
| `RetrievalReceipt` | Request, resolved origin, response identity and retrieval moment | The model's inference |
| `ReferenceExcerpt` | Work, edition/revision, locator and verbatim bearing words | A project conclusion |
| `ReferencedClaim` | Source S supports/contradicts/does not settle claim C | Unattributed truth |
| `ConflictSet` | The relation among cited claims that disagree | A synthetic winner |
| Gazetteer revision | The current project identity/world state and what it rests on | Retrieval history it merely links |

The retrieval receipt keeps, at minimum, the request, retrieval moment, resolved origin and a stable content
identity. The reference excerpt keeps the exact bearing words, work and locator. Where rights and source behaviour
permit, a content-addressed snapshot may also be retained; otherwise the exact excerpt, response metadata, content
hash and durable locator preserve the audit trail without silently warehousing a work.

These artefacts are stored, not cached. Their projections may be rebuilt, but the acts and evidence are never
silently discarded or regenerated. No two artefacts gain authority over the same fact: a receipt owns what was
fetched, a referenced claim owns what the source says, and the Gazetteer owns the project's current entity state.

## Promotion without drift

Fetching is not promotion. The safe sequence is:

1. Persist the retrieval receipt and source excerpt automatically.
2. Compile an atomic referenced claim from those persisted artefacts.
3. Check it against the canonical source, existing referenced claims and writer revisions.
4. If it settles an uncontested external-world gap, the reading may promote it with `.reference` evidence attached.
5. If it conflicts with the manuscript *about the manuscript*, the text wins and the contradiction remains visible.
6. If it conflicts with another source, both enter a conflict set; neither replaces the other.
7. If it conflicts with the writer, the writer wins and both prior grounds remain in history.
8. Ask the writer only for the remaining presented disagreement, never to repeat the research.

This preserves the writer's role as arbiter rather than curator. A retrieved source that plainly fills an open
world-level gap does not turn the writer into a confirmation queue. A genuine conflict reaches them already reduced
to the smallest decision and carrying the words on both sides.

A source about interpretation follows a different path. Reframe may hold the attributed proposition *“critic S
reads this as X”* in an artefact that owns critical perspectives; it may not promote *“the work means X”* into the
Gazetteer. Editorial variants, chronology, places, institutions, terms and aliases likewise belong in artefacts
whose scope says exactly what they can claim. A new artefact joins the family only when it changes what the writer
sees or does ([ch.31](31-compiled-knowledge.md) rule 9).

Every consumer receives a semantically selected FountainStore packet for its present question — the relevant
project entities, claims, conflicts and provenance — rather than a full web transcript or undifferentiated corpus.
Selection is reasoned from artefact dependencies and current phase. Numeric token or byte measurements remain
telemetry and transport observation; they never decide which semantic evidence is included.

## How the frontier lane earns its cost

An elevated model is valuable here for work a weaker local pass should not repeat:

- turning a persisted uncertainty into a precise research question;
- choosing source classes and query vocabulary without asserting a remembered citation;
- refining a query from recorded failures, variant names, editions and aliases;
- judging whether a fetched quotation actually bears the claim;
- distinguishing support, contradiction, non-address and ambiguity;
- comparing sources without flattening disagreement;
- compiling the durable result into the project's typed artefacts.

It is not valuable as a recurring oracle over the same manuscript. Once the durable result is compiled, the local
lane reads it forever after. Frontier and local compilers may produce the same kinds of artefact at different rates;
the project memory, not the provider, is the durable capability.

The useful measure is therefore not how many pages were searched or how many tokens were spent. It is whether a
cost-bearing act left one reusable, evidenced, falsifiable result that later work no longer re-derives. Retrieval
reuse, avoided duplicate searches, unsupported-claim rejection, conflict frequency, provenance depth, invalidation
scope and cost per durable result may be observed as telemetry. They do not set semantic thresholds.

## Pragmatic realization

The implementation should arrive in slices that are independently removable and testable:

1. **Persist the research ledger.** Store research acts, search attempts, retrieval receipts and negative results in
   FountainStore before adding another live source.
2. **Enforce persist-before-interpret.** The compiler accepts FountainStore artefact identifiers, not transient page
   bodies. A missing receipt is a hard refusal.
3. **Make retrieval adapter-shaped.** Keep the current reachable source as one adapter behind the common finding
   contract; add archives, catalogues or scholarly sources without changing the evidence rules.
4. **Compile typed claims.** Produce support/contradiction/non-address/ambiguity against one explicit project
   question. Citation fields come from receipts, never model output.
5. **Promote through one choke point.** Only the Gazetteer or the other owning artefact can accept a compiled claim,
   and only when its evidence kind is admissible.
6. **Keep conflict and revision.** Additions append or supersede with history; they never overwrite a contrary
   source or writer act.
7. **Project locally.** Later readings receive the relevant compiled knowledge and provenance from FountainStore and
   do no web work of their own.
8. **Expose the account.** Through the Copilot and FCIS-AX, the writer can inspect what was asked, fetched, inferred,
   not found, disputed and adopted, and can correct it in a sentence.

The persistence path uses native FountainStore access when available. It introduces no shadow database, provider
memory or HTTP backplane, and correctness with the web capability absent remains the acceptance floor.

## Validation — prove the boundary, not the demo

The decisive tests are invariants:

- A compiler cannot receive or cite web material that has no persisted retrieval receipt.
- A quotation must be present verbatim in the recorded response material; a model cannot repair or complete it.
- A snippet, generated bibliography and named-but-unconsulted work cannot promote a claim.
- Restarting the app preserves successful, failed and refused searches and prevents identical paid work.
- New evidence reopens only the affected research question; unrelated knowledge remains valid.
- Two conflicting sources survive compilation, persistence and projection side by side.
- A writer correction supersedes referenced evidence without deleting its history.
- Refreshing a changed source creates a new dated retrieval and never rewrites the old one.
- Referenced provenance survives repeated read, compile and projection cycles without becoming plain “confirmed.”
- Deleting all referenced artefacts leaves import, reading, beats, composition and correction functional.
- A recorded research act can be replayed offline from FountainStore without touching the network.
- Adversarial source text cannot invoke tools, change scope, spend or become an instruction.
- AX exposes source, locator, quotation, evidence kind, research state, conflict and available writer actions.
- A live acceptance fetch proves the real adapter and persisted artefacts; deterministic fixtures prove the doctrine
  without depending on network availability.

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
15. **FountainStore is the only operational knowledge plane.** Web responses and model outputs are transient until
    typed, attributed artefacts record them; no later pass may rely on provider memory or an unpersisted page.
16. **Persist before interpretation.** Retrieval records itself before a compiler reads it, and the compiler consumes
    the stored artefact rather than a transient browser response.
17. **Query the project before the world.** Existing artefacts, writer revisions, prior retrievals and failed
    searches are consulted before a new external act is proposed.
18. **Discovery, retrieval, compilation and promotion remain distinct.** A lead cannot become evidence, and evidence
    cannot mutate project memory without the owning artefact's admission rule.
19. **Frontier reasoning compiles; it does not become authority.** It may plan, compare and infer from fetched
    material, but citations are assembled from retrieval records and durable knowledge lives in FountainStore.
20. **Each artefact owns one kind of fact.** Receipts own what was fetched; claims own what a source says; the
    Gazetteer owns current world identity; projections and indexes are rebuildable and own none of them.
21. **External content is untrusted data.** It cannot issue tools, alter scope, widen a grant, override doctrine or
    become an instruction merely because a model can read it.
22. **Promotion is typed, historied and conflict-preserving.** An uncontested admissible reference may fill an
    external-world gap; contradiction appends or supersedes visibly and never silently overwrites.
23. **Every cost-bearing lookup belongs to a scoped research act.** The writer's yes covers that act and no materially
    wider one; credentials or a prior grant are not standing permission.
24. **Research artefacts are narrowly invalidated and reusable.** A later pass reads them; a source refresh creates a
    new dated retrieval; new grounds reopen only the question they actually affect.

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
- No operational model context contains web material that does not first exist as a FountainStore retrieval artefact.
- A complete recorded research act replays offline from FountainStore and performs no network or frontier call.
- Search, retrieval, claim compilation and promotion are separately inspectable; no lead crosses the boundary by
  sharing a convenient response shape with evidence.
- The same stored evidence can be consumed by local and frontier reasoning without changing its citation or
  provenance.
- Prompt injection in a fetched source cannot change tools, scope, grants, routing or persisted project state.
- Every research-derived surface is FCIS-AX inspectable and offers the relevant follow, refresh, adjudicate or
  correct action.
- Publication and integration copies of this chapter remain byte-identical, with reciprocal commit or pull-request
  provenance recorded whenever the doctrine changes.

## Governing sentence

Reframe shall admit knowledge from outside the manuscript only as a reference it has actually fetched, cited well
enough for a doubting reader to follow, marked as referenced for as long as it is held — and shall never let such
knowledge speak about what the pages themselves contain.
