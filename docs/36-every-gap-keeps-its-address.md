# Every Gap Keeps Its Address

> Chapter summary: [Chapter 33](33-a-want-is-a-gap-in-a-ledger.md) made uncertainty open-ended: the map is
> collected from whatever ledgers the work keeps, and a new ledger appears by registering, never by editing an
> enumerated axis list. The surface must now honour that architecture. It may not turn an arbitrary collection back
> into three named rows, a fixed card, or a ranking that silently drops what does not fit. **Every gap keeps its
> address** — the lane that presents it and the note that locates it — across the shared spine, the manuscript, its
> originating ledger, its typed want, any reference search, and the writer's decision. `UncertaintyScoreKit` owns
> the provider-independent map and its navigation; Reframe binds a selected address to domain meaning. Complexity
> is neither flattened nor hidden: it is represented at three synchronized resolutions — the rack of all lanes, the
> map over the work, and the complete account of the selected thread — so a large reading can be dense without
> becoming shapeless, and detailed without making the conversation jump around it.

## Purpose — the failure this exists to end

**The data model learned that it could have any number of ledgers. The renderer still behaves as though the answer
were one chart somebody already knew how to name.**

Measured on the integration source, 2026-07-31. The core now does the right thing: a
`ReframeUncertaintyLedgerRegistry` collects arbitrary reports; each report emits a lane; each assessment emits a
note; a ledger that failed or never arrived reports that absence as a failure rather than disappearing. No shared
function contains the final list of things the work may be uncertain about. That is chapter 33's central repair.

The production UI reverses it at the last metre. `UncertaintyScoreView` is one fixed-width vertical composition. It
contains, in order, its own title, a paragraph explaining itself, a four-state legend, an aggregate ribbon, every
lane, one-letter solo/mute controls, and the selected note's detail. Reframe places the entire composition inside a
second disclosure above the Story surface. The consequences are structural:

- another ledger means another full row in an already tall card;
- a braided lane means as many additional rows as its overlaps require;
- selecting a note adds prose beneath the map and changes the map's height;
- the fixed gutter is too small to be a navigator and too large to be merely an axis label;
- the map has no scalable way to search, traverse or hold selection among many lanes;
- the selected note is addressed by note ID alone, even though independent ledgers may issue the same local ID;
- the typed want that can close the gap remains in Reframe while the visible mark retains only flattened
  `resolvedBy` prose;
- a reference lookup then reappears as a large chat card, visually detached from the mark and ledger that caused
  it, and its arrival moves the transcript between the top and bottom of competing blocks.

Nothing here is a request for less information. The failure is that **all information has been given the same
spatial job**. A legend, a corpus-scale map, a lane index, a selected diagnosis, a retrieval receipt and a writer's
decision are not peers. Stacking them as peers does not preserve complexity; it destroys the relationships that
make complexity intelligible.

The standing case makes the loss visible. The reading raises *who “Kinch” is* from one ledger. That gap wants a
source outside the work. The writer widens the world, the search follows a source, a quotation returns, and the
Gazetteer still awaits the writer's judgement. Those are not five cards. They are **one thread changing state**.
When the interface cannot point from the result back to the exact gap, the writer is asked to remember the
architecture the surface was meant to show.

## The principle — preserve complexity by preserving address

A gap is not identified by its wording. Two ledgers may ask the same sentence for different reasons; one ledger may
ask the same sentence again after its evidence changed. A gap's minimum address is therefore:

```text
(laneID, noteID)
```

In Reframe today the lane is emitted from a ledger report and the note from one of its assessments, so the address
also names the report that raised the gap. A host may bind more identity behind it — corpus, reading, ledger
generation, persisted question thread — but it may never bind less. Matching the prose of a title, detail or chat
turn is not identity and may not reconnect the thread.

The same address is read at three resolutions:

1. **The lane rack — what kinds of account this reading actually has.** Every producer-supplied lane appears in
   producer order. The rack can contain none, one, dozens, hundreds, or lanes that arrive while a reading is live.
   It is a virtualized, searchable outline, not a fixed illustration of the ledgers known when the UI was written.
2. **The shared-spine map — where their assessments live together.** Every visible lane is drawn against one
   source coordinate. This is where overlap, duration, absence, accumulation and continuation become perceptible.
   Panning or zooming changes one spine, not a private scale per lane.
3. **The selected-thread account — what this particular mark means and what can change it.** Its full wording,
   state, span, originating lane, closure cue and host-provided evidence live in a stable contextual region. Detail
   does not grow the map or become a second copy of it in chat.

These are not three datasets and not a summary followed by the real thing. They are three views of the same
addresses. Selection, colour/shape identity, source range and AX identity remain continuous between them.

## Lanes are open-ended — and their two meanings must not be confused

This guide uses *lane* in two related geometries and two different ontologies:

- In [the Score](17-the-score.md), a lane is a **participant** — a text, voice, light, instrument, algorithm or
  other actor present in the performance.
- In the uncertainty map, as chapter 33 already states, a lane is a **drawing of one ledger's assessments** over a
  spine. It is not a participant and not a predeclared kind of doubt.

Putting an uncertainty artifact on the Score does not turn its ledger lanes into performance participants. The
map is a reading of the work, situated on the one surface, just as a provenance line is a relationship on the
surface and not an actor. UI naming, AX roles and documentation must keep this distinction explicit. A generic
`UncertaintyLane` may never be assumed to be Text, Identity, Structure, Reference, or any other domain category.
Those names belong only to the producer that emitted them.

This follows directly from chapter 33: **a new ledger must become visible by existing**. If adding it requires an
`if`, a new tab, a case in a sidebar enum, a colour assigned by hand, or a revision to a fixed list of lane titles,
the renderer has reintroduced the enumerated architecture that chapter removed.

## The lane rack — all instruments of doubt, in producer order

The leading region of the uncertainty artifact is a **rack**, paired row-for-row with the shared-spine map. It is
not a catalogue of three preferred lanes and not a set of dashboard cards. Its rows are materialized from
`score.lanes` and preserve their supplied order.

A lane row owes, generically:

- the producer-supplied title, readable in full by wrapping, expansion or an equivalent non-destructive treatment;
- a state mark that is not colour alone;
- counts or distribution derived from the lane's actual notes, never a host-invented quality score;
- a compact view of its marks on the same spine where space permits;
- selection and an explicit, named way to focus, solo or mute it;
- disclosure into its notes, with each note carrying its title (or honest fallback), state and span;
- a stable AX identifier composed from the lane and note address, with the same activation as pointer and keyboard.

The outline is at most two semantic levels — lane, then note — no matter how many of either exist. Optional grouping
may be supplied by a producer as data; the kit may not infer groups from lane names, state, order or count. Search
and state filters are generic transformations over the collection and preserve the remaining producer order. They
are entered by the writer and visibly active. There is no automatic “top”, “important”, “relevant” or “first N”
selection, because that would be a new reasoning pretending to be layout.

Large collections are handled by virtualization and adaptive row detail, not omission. A strip can remain one row;
a braid can disclose the packed rows its simultaneous threads require; the selected lane may receive more vertical
resolution while keeping every other lane addressable. The viewport may show only part of a long collection at
once, as every scroll view does, but the model and the navigation continue to contain all of it.

## The shared spine — one coordinate, several scales

The map's competitive advantage is not that it draws coloured bars. It is that **unrelated ledgers become
comparable without becoming the same thing** because they share one coordinate from the work.

The axis is therefore stable across:

- the aggregate openness ribbon;
- compact lane thumbnails;
- full lane rows;
- selected-note emphasis;
- the corresponding manuscript highlight.

Zoom and pan change the common viewport. They do not recompute the meaning of a note, reorder lanes, or silently
drop marks. A gap remains located in the source range it reported. A question continuing beyond the observation
keeps its open ending; an unread stretch remains different in shape and language from an ambiguity; settled means
assessed and settled, never blank.

The map supports three scales without changing visual grammar:

- **whole-reading scale** — density, coverage, failures, overlap and the number of ledgers are perceivable;
- **lane scale** — the assessments from one ledger and their relationship to neighbours are legible;
- **note scale** — the exact thread, source span, account and closure path are inspectable.

Moving among scales preserves mark type, status shape, selection and wording. A miniature is not allowed to invent a
different summary than the expanded view. Complexity remains learnable because the same thing looks like itself at
every resolution.

## The selected thread — detail has a stable home

Selection is state, not layout. The complete account of a selected address belongs in a stable contextual region
attached to the conversation surface. It may adapt beside or above the conversation with window size, but it does
not become a tall message inserted into transcript history and it does not extend the score beneath the writer's
current viewport.

The generic kit can show only what it owns:

- lane and note identity;
- state and state meaning;
- source span and continuation;
- title, detail and generic closure cue.

The Reframe host may then bind the same address to:

- the registered ledger report and its generation;
- the typed want — manuscript, stronger reasoning, outside source, or writer;
- the reference question and exact consent, where one exists;
- search attempts, hop reasons, receipts, answering document and verbatim quotation;
- the current writer-decision state and any resulting Gazetteer revision.

This is where the relationship absent from the live interface becomes explicit:

```text
ledger gap
    → typed want
        → writer-granted act
            → retrieval and evidence
                → writer decision
                    → ledger redraw
```

Every node keeps the originating address. A result can therefore say which gap it bears on without a model
reconstructing that relationship from transcript prose. When the writer records or refuses a conclusion, the same
ledger changes and the map redraws; no chat sentence is treated as the state authority.

## What the kit owns, and what Reframe owns

| Boundary | `UncertaintyScoreKit` owns | Reframe owns |
| --- | --- | --- |
| Model | score, ordered lanes, notes, states, shared spine | registered ledger reports, persisted generations, typed wants |
| Identity | composite lane/note selection | corpus/reading/thread identity behind that address |
| Navigation | rack, search, explicit state filters, zoom/pan, selection | which reading is current and where its manuscript source lives |
| Representation | strip/braid geometry, state shapes, continuation, aggregate view | domain wording beyond supplied fields, source/evidence lifecycle |
| Interaction | generic activation, focus/solo/mute, callbacks, keyboard and AX | permitted acts, consent, spending, retrieval, Gazetteer decisions |
| Explanation | note detail and generic closure cue | why this ledger raised it, who can answer, what happened after asking |

The boundary is enforceable in both directions. `UncertaintyScoreKit` may not import Reframe types or learn about
Gazetteers, `/world`, providers, citations or paid lanes. Reframe may not fork the kit's map into a private,
hard-coded lane renderer in order to show its domain. It supplies structured context for a selected address through
the host seam and continues to use the kit's arbitrary collection and selection semantics.

Typed meaning must not be reconstructed from prose. `resolvedBy == "a source outside the work"` is suitable copy
and unsuitable authority. Reframe already has a typed `ReframeUncertaintyWant`; the address joins the visible note
back to that value. Natural-language labels remain presentation, never routing.

## Conversation and scroll — the dialogue is not the database

[The CoPilot Is the Surface](25-the-copilot-is-the-surface.md) does not require every artifact to become a chat
bubble. It explicitly permits a visual artifact where a picture is clearer. The uncertainty map is such an artifact:
it is the first reading's visible account of what it knows and does not know. The Copilot teaches it, refers to it,
and acts with the selected thread; the transcript records the dialogue around those acts.

Therefore:

- chat holds turns and event summaries, not the only copy of ledger state or retrieval evidence;
- a message that refers to a gap carries its address and can focus the artifact;
- selecting a mark situates the Copilot on that thread without synthesizing a new command from its label;
- an arriving assistant turn is revealed once at a stable anchor;
- a user turn followed by its assistant result is one arrival sequence, not two competing scroll targets;
- if the writer has moved away from the live edge, the app announces a new turn and does not take the viewport;
- expanding a lane, receipt or quotation may change its own contextual region but may not repeatedly re-anchor the
  transcript.

This is not less chat-native. It makes the conversation truthful about what it is: a collaboration around durable
objects, not the container that must redraw every durable object as prose whenever anything changes.

## State language — one word, one meaning

The four states are part of the contract, not palette names. Before the surface can teach them, every producer and
renderer must agree on their meaning:

- `settled` — assessed and held, visibly different from no assessment;
- `ambiguity` — the evidence genuinely sustains competing readings;
- `thin` — a reading is present but under-supported;
- `failure` — the assessment did not happen or cannot be trusted.

The definitions in [chapter 24](24-the-reasoning-is-an-uncertainty-map.md), the core type documentation, Reframe's
projections, visible legend, spoken AX labels and routing consequences must agree. If a producer uses `ambiguity`
for what the kit calls `thin`, colour can make the disagreement prettier and no less false. The vocabulary is
audited as one contract before visual polish is accepted.

State and thread identity use separate visual channels. State is carried by shape, line treatment, words and an
accessible value, with colour as reinforcement. A thread in a braid may carry a stable identity hue across the map,
manuscript and inspector, but selection is a distinct halo/focus treatment and failure remains distinguishable
without hue. No single colour is asked to mean lane, state, identity and selection at once.

## The decision (enforceable rules)

1. **No renderer enumerates uncertainty lanes.** It consumes the complete ordered collection supplied by the score
   and assumes neither domain names nor a maximum count.
2. **Every gap is selected by a composite address.** At minimum `(laneID, noteID)`; note prose and note ID alone are
   not sufficient identity.
3. **A registered ledger appears by existing.** Adding one requires no new UI case. A missing, stale or failed
   ledger remains visible as the failure chapter 33 requires.
4. **The rack, map and selected-thread account are synchronized resolutions of one dataset.** Selection, source
   range, state and AX identity remain continuous between them.
5. **The shared spine is shared.** All lane and manuscript location views use the same source coordinate and
   viewport; private axes may not make unrelated spans look aligned.
6. **Large collections scale by virtualization, navigation and explicit filtering, never silent omission or an
   automatic top-N ranking.** Producer order is retained among visible lanes.
7. **Detail has a stable contextual home.** Selecting a note or receiving evidence may not grow the map or insert
   the durable state as a transcript-sized card that changes the writer's place.
8. **The kit stays provider- and domain-independent.** Reframe meaning enters through structured host bindings for
   a selected address, never imports or hard-coded lane knowledge.
9. **Typed wants remain typed across the presentation seam.** Copy may explain them; copy may not recreate them or
   decide an act.
10. **Uncertainty lanes are ledger projections, not chapter 17 participants.** Sharing the Score's geometry does not
    merge their ontology.
11. **Chat records collaboration around the map; it is not the map's state store.** Messages may focus an address;
    FountainStore and registered ledger state remain behavioural truth.
12. **Scroll follows a deterministic arrival policy.** One reveal per completed assistant arrival; no command/result
    double jump; no forced return when the writer has left the live edge; disclosure does not re-anchor history.
13. **State words have one meaning across core, projection, pixels, AX and routing.** A vocabulary mismatch is a
    contract failure, not a copy defect.
14. **Every visible mark is machine-readable and every machine-readable mark is visibly present.** Lane/note counts,
    selection and actions satisfy FCIS-AX pixel parity; Canvas is never the only representation.
15. **Visual polish is validated as behaviour.** Light, dark, Increase Contrast, Reduce Motion, keyboard-only,
    VoiceOver, narrow/resized windows and external-display full screen are acceptance contexts, not screenshots
    saved for the end.

## Honesty (non-goals)

- **Not simplification by subtraction.** No receipt, lane, note, state, reason or history is discarded to make the
  surface calm. Information is given a stable role and resolution.
- **Not a preferred-lane dashboard.** The host may not nominate three familiar ledgers and call them the map.
- **Not a fourth destination.** The uncertainty artifact belongs to the current reading on the one Score surface;
  it is not an Analysis room, machine room, settings panel or separate workflow.
- **Not a configuration console.** Search, focus, zoom and disclosure are ways to read the artifact. They do not
  configure how Reframe reasons or which ledgers are allowed to exist.
- **Not a generated executive summary standing above evidence.** Aggregate views are literal projections of the
  same notes. They never replace or reinterpret them.
- **Not a generic-kit takeover of the domain.** The kit draws uncertainty; Reframe knows what its ledgers, wants,
  sources and writer decisions mean.
- **Not a visual metaphor exempt from accessibility.** A beautiful braid with no AX notes is absent to the machine
  and to the writer who reads through it.

## Relationship to other chapters

- **[The Reasoning Is an Uncertainty Map](24-the-reasoning-is-an-uncertainty-map.md)** — fixes the states and the
  map as a first-class product. This chapter governs how that product remains legible and addressable at scale.
- **[A Want Is a Gap in a Ledger](33-a-want-is-a-gap-in-a-ledger.md)** — makes the set of ledgers open-ended and
  types who can close each gap. This chapter is its necessary UI consequence: the renderer is collected, too.
- **[The Score](17-the-score.md)** — supplies the one-surface and shared-spine discipline, while this chapter keeps
  uncertainty ledger lanes distinct from performance participants.
- **[The Stage Presents the Act](18-the-stage-presents-the-act.md)** — requires focus, legibility and drawn
  relationships. Here the act is inspecting one reading without losing its full field of uncertainty.
- **[Apple Human Interface Guidelines](19-apple-human-interface-guidelines.md)** — supplies system typography,
  contrast, motion and native split/outline behaviour beneath this chapter's information architecture.
- **[The CoPilot Is the Surface](25-the-copilot-is-the-surface.md)** — the Copilot teaches and acts with the map;
  the map is the permitted visual artifact, not a standing configuration panel.
- **[Referenced Knowledge](32-referenced-knowledge.md), [A Question That Leaves the Work](34-a-question-that-leaves-the-work.md),
  and [Deep Search](35-deep-search.md)** — supply the outward lifecycle that must remain visibly attached to the
  gap whose want began it.
- **[Decoupled Manuscript Instruments](99-decoupled-manuscript-instruments.md)** — applies the composite-address and
  kit-host boundary to the three manuscript instruments: navigation, source text, and the independent SVG lane map.

## Acceptance

The doctrine is met when:

1. Generated and live fixtures with empty, singleton, numerous, densely overlapping and dynamically added ledgers
   render through the same code path, with no lane-name cases or cardinality assumptions.
2. The rack contains every supplied lane in producer order, and expanding one exposes every note; search or state
   filtering is explicit, visibly active and preserves the remaining order.
3. A lane registered after the artifact is visible appears without resetting the writer's selection, horizontal
   viewport or transcript position; AX announces the addition without taking focus.
4. Selection is `(laneID, noteID)` end to end. Duplicate local note IDs in different lanes remain distinct in
   pixels, AX, callbacks and host context.
5. The aggregate, lane row, note inspection and manuscript highlight use the same spine and preserve the same
   selected identity through zoom, pan, resize and relaunch.
6. The definitions and consequences of `settled`, `ambiguity`, `thin` and `failure` agree in the core model,
   Reframe projections, visible key, AX labels and tests.
7. A failed or unavailable ledger is louder than a healthy empty ledger, never absent, satisfying chapter 33's
   standing negative case.
8. On the Telemachus standing case, the Kinch mark, external-source want, consent, retrieval trail, answering source,
   verbatim quotation and unresolved writer decision are inspectable as one addressed thread; no Gazetteer change
   is implied before the writer makes it.
9. The same Telemachus drive can widen the world and receive the result without a command/result double jump,
   bottom-to-top flip, or disclosure-induced transcript re-anchoring.
10. Removing Reframe's host context leaves a complete generic uncertainty map; removing the generic map leaves
    Reframe's ledgers and FountainStore truth intact. Neither layer is the other's hidden authority.
11. Every visible lane and note is queryable and activatable through AX with its composite identity, and every AX
    mark corresponds to a visible mark (FCIS-AX pixel parity).
12. The large-lane and dense-braid fixtures remain usable and visually coherent in light, dark, Increase Contrast,
    Reduce Motion, keyboard-only, VoiceOver, narrow/resized windows and the governed external-display live drive.

## Design references

- [Apple Human Interface Guidelines — Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
- [Apple Human Interface Guidelines — Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)
- [Apple Human Interface Guidelines — Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data)
- [Adobe Spectrum — Side navigation](https://spectrum.adobe.com/page/side-navigation/)
- [Grafana — State timeline](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/state-timeline/)

These references supply platform and competitive interaction precedents — adaptive side navigation, outline
selection, shared-axis state regions, multiple levels of chart detail, pan/zoom and accessibility. They do not
define Reframe's ontology; the ledger, want and writer-authority rules above do.

## Governing sentence

Reframe shall preserve every uncertainty the work can report by giving each gap a stable lane-and-note address,
showing every producer-supplied lane against one shared spine, and carrying the selected thread intact through its
ledger, want, evidence and writer decision — so complexity gains shape and continuity, never a fixed taxonomy, a
silent ranking, or another card in a conversation that has lost its place.
