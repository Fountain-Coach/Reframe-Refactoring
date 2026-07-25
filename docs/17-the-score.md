# The Score — Reframe's Performance Space, and the One Surface That Folds the Others

> Chapter summary: The Score is not a better timeline nor an alternative piano roll. It is the **performance space of the work itself** — a stage on which *participants* (a voice, a text, a light, an image, an instrument, an algorithm, an entire remote Reframe) enter into relation under a shared structure. This chapter makes the Score the **one consolidated working surface**: the Story timeline and the Cut arrangement become **lenses** of it, not separate destinations, and the free-2D patch-graph canvas of chapter 14 is **retired**. It fixes the Score's ontology (a lane is a participant, not a track; the beat/arc is the structural spine; Grounding is the condition of entry; MIDI 2.0 protocol state is part of the composition), and it defines the **minimum honest Score** we build first — the grounded beat-spine plus a single Text participant rendered from the source — with the distributed multi-participant stage named explicitly as horizon, not as this increment. It states required behaviour and constraints; it does not prescribe unverified types, files, or call paths.

## Purpose

The work had three destinations: Storify (the timeline), Cut (a canvas), and the Score (a projection somewhere downstream). A writer moved *through* them in sequence, and each pretended to be its own place. Chapter 14 already named the deeper truth — a beat is **one object, three arrangements** — but it left the three arrangements living in three surfaces the writer crosses between. This chapter draws the consequence chapter 14 stopped short of: if they are arrangements of one object, they belong in **one surface**, and that surface is the Score. The timeline and the Cut are how the Score is *read* (by source position; by runtime order); they are lenses on the stage, not rooms the writer walks between.

Two things make this reachable now rather than someday. First, the local lane segments a manuscript into grounded beats without a paid model and without a cloud round-trip — so a text can **populate** the Score the moment it is imported. Second, every beat now carries its **provenance** (chapter 4 identity: origin, source hash, Grounding identity) — so a beat can become a participant's action *without drifting free of the source it came from*, which is the Score's one non-negotiable.

## The principle — a stage of participants, not a timeline of tracks

A Digital Audio Workstation asks *what happens next*. Its objects derive their identity from transport: tracks carry signals, regions contain recordings, clips contain events. The Score asks a different question — *who or what is presently capable of acting, under which conditions, in relation to whom* — and its objects derive their identity from **presence**. A lane is therefore a **participant**, an actor with identity, state, capabilities, and the ability to negotiate, refuse, and respond. The Score is populated not by signals but by actors, and its work is less to schedule events than to **sustain relationships**: it remembers not only that something happened, but under which understanding it became possible.

This is why the Score cannot be understood as an editor. Editors manipulate representations; the Score **convenes presences**. And it is Grounding that lets those presences cohere: musical, textual, and visual action meet not because they were hand-aligned on a timeline but because they **derive from a common semantic structure**. The Score is where interpretation acquires duration — the visible form of the work's understanding, not merely the execution surface of its media.

## The decision

1. **The Score is the one working surface; the timeline and the Cut are its lenses.** The application no longer presents Storify, Cut, and Score as three destinations to move between. There is one Score. *Reading by source position* (the manuscript-order timeline, chapter 14's Story arrangement) and *reading by runtime order* (the Cut arrangement) are **views onto the Score**, selected in place, never surfaces the writer is sent away to. Crossing between lenses is the chapter-14 transformation — the same beat, differently arranged — animated as a settling, never a replacement.

2. **A lane is a participant, not a track.** Each lane represents an actor in the performance — a text, a voice, a light, an image, an instrument, an architectural element, an algorithm, or an entire remote Reframe instance. A lane exposes a **role** (what it is here), not a channel. Its identity precedes any output it produces.

3. **The beat and its arc are the structural spine; participants perform beneath it.** The story structure the reading produces — scenes, sequences, beats — is the Score's horizontal **spine** (the Scene and Structure bands running across the top of the field). Participants are laid out vertically and perform *within* that structure. The beat is therefore not one more lane; it is the **shared time-structure every participant is grounded to**. This is what makes textual and any later medium meet without manual alignment.

4. **Grounding is the condition of entry.** No participant, and no region a participant performs, may drift free of the source from which it emerged. Every element enters the Score already carrying a grounded relationship to the work — its **provenance** (chapter 4: source document identity, operational source hash, confirmed Grounding identity, operation version, provider provenance). A participant that cannot state what it belongs to has not been admitted to the stage. (This is the same lineage the beat-provenance stamp already carries; the Score surfaces it, it does not invent it.)

5. **The free-2D patch-graph canvas is retired** — this supersedes chapter 14's rules 7–9. The Cut Script was to be a wiring surface in the Quartz Composer / Vuo tradition: beats as nodes, wires as runtime order, a renderer node, output-as-a-node. That grammar does not serve the writer — an infinite canvas of node-wiring is a machinist's surface, not a place to arrange a story — and it is safely deprecated. The **Cut survives as a lens**: the beats arranged in *authored runtime order* along the Score's spine, with their measure reading time-cost rather than source span (chapter 14 rule 3). What dies is the free 2D space and the node/wire/port grammar; what lives is arrangement-by-runtime-order as a reading of the one Score.

6. **The take and its clock survive as the Score's transport** — relocated from the retired canvas. Chapter 14's *trigger* was "playing the wiring"; here it is **playing the spine**: the transport walks the structure in time and the participants render as it goes. A firing still produces a **take** (a timestamped render of the arrangement as it stood; the source is v1, each kept reframe v2+; a trigger does not "save", it takes). One firing still renders the **document layer** (the cut script `.fountain` in the bundle) and, at the horizon, the **musical layer** (MIDI 2.0) as **siblings**, neither derived from the other (chapter 13). The clock is the Score's transport, not a canvas node.

7. **Protocol state is part of the composition, surfaced honestly — at the horizon.** For non-text participants the Score exposes, per participant, its MIDI 2.0 identity: **Profile**, **Properties**, **State**, **Capabilities**, and live **Subscriptions** (who it responds to, what it is listening to), with a UMP monitor available as a lens. This is composition, not technical metadata: the Score records *under which understanding* an action became possible. This richness is **horizon** (see below), not the first increment, and it must never be fabricated for a participant that does not yet exist.

8. **The Score opens simple.** A writer meets a text and its beat-spine, not a mixing desk. Media lanes, inspectors, subscriptions, and the protocol monitor **accrue only as the work calls them into being** (chapter 12's progressive-disclosure ethic; chapter 16's one-surface discipline). The DAW-like geometry is deliberate familiarity, but the writer modernising a manuscript must never be handed an eight-lane console they did not ask for.

## The minimum honest Score (what we build first)

The full stage — many media participants across machines, remote Reframe instances, live Property Exchange — is the endgame, not this increment. The **minimum honest Score** is the smallest surface that is genuinely the Score and not a mock of it:

- **The grounded beat-spine.** The reading's scenes/sequences/beats laid across the top as the structural bands, built from the source (the local lane suffices), each beat carrying its provenance (chapter 4). An un-read manuscript is **one unanchored span across its scope** (chapter 14 rule 5), never an empty stage.
- **One participant: the Text lane**, rendered directly from the source beneath the spine — the manuscript performing itself as text over its own structure. Its regions are the beats' source text; its measure is source span (timeline lens) or runtime cost (Cut lens).
- **The two lenses in place, not two rooms:** read the spine by source position or by authored runtime order, switched in place, animated as transformation.
- **The transport and a take:** playing the spine renders the cut script into the bundle (chapter 13). The musical-layer sibling is stubbed at the binding only — no invented second notion of musical time (chapter 14 rule 12/13).

Everything absent from this list — additional media participants, remote instances, Property Exchange, the protocol monitor, subscriptions between actors — is **honestly absent**, foreshadowed as capacity the stage will gain, never faked. A Text lane that reads the source truthfully, grounded, under one structure, is the whole Score in miniature; the rest is the same idea admitting more kinds of actor.

## The horizon (named, so we build toward it and not past it)

The distributed stage is real and intended: participants of any medium, each possibly a separate Reframe instance, discovering one another through negotiated presence rather than hard-coded assumption; rehearsal, testing, and performance converging on one field; a simulated instrument later replaced by a physical one without altering the composition that addresses it. **Triggers to expand past the minimum:** a second medium is genuinely rendered (a voice, a light) and needs its own lane and role; two Reframe instances must sustain one work while keeping their individuality; a participant must publish or subscribe to another's state; the musical-layer sibling must actually render rather than bind. Until a trigger is met, the lane, the monitor, or the subscription is not built — because an empty console is a lie about the work's present.

## Where the stage actually is (decided 2026-07-24)

**The Score is not ahead of us. We are standing on it.** The surface a writer already works in — the manuscript surface carrying the beat-spine (Scene/Structure bands), the beats rendered from the source beneath it, the lens selection, the transport's read-head, and the Copilot beside it — **is** the Score. It is not a preview of the stage, nor a step toward it: it is the stage, and **every other view and state must evolve from it**.

This resolves an inversion that had crept in. The "minimum honest Score" was built as **its own view**, reached from a third icon, sitting beside the timeline and the Cut — so the Score appeared as a *destination peer to its own two lenses*. That is exactly the navigation model this chapter retires (decision 1, acceptance 1). A surface that is the whole stage cannot also be one tab of three.

Consequences, binding:

- **The surface picker is retired entirely — all of it.** First the "Score" icon went, because it made the stage a destination peer to its own lenses. Then the remaining pair (timeline · cut) went too: **a picker of any size still teaches the writer that the work lives in several places.** A writer never chooses a surface, because there is only one, and they are standing on it. This *revises decision 1*, which had kept the two lenses as an in-place selection: the lenses remain real as *readings*, but they are no longer a control above the stage.
  - **Honestly stated loss:** removing the picker removes the only route to the **runtime-order (Cut) reading**. The lens is not deleted — the Cut arrangement and its runtime measure remain in the surface — but nothing reaches it today. This is a **deliberate, recorded absence**, not consolidation quietly costing a capability (see the non-goal below): the way to read by runtime order must **evolve from the stage** rather than sit above it as a toggle, and until it does, the absence is stated rather than papered over.
- **The separate Score view is superseded as a destination.** Its Text participant is what the stage already renders — the beats' own source beneath the spine — so nothing is lost by folding it in. Its Music participant does not become a tab: per decision 8 and the honesty rules, a media lane **accrues when a real actor backs it**, and until then is honestly absent.
- **This surface is the baseline all evolution starts from.** New participants arrive as **lanes beneath the spine**; new ways of reading arrive as **lenses in place**. Neither may arrive as a new destination — a "fourth view" is, by this chapter, already wrong.

The rest of the chapter is unchanged: what the horizon adds is *more kinds of actor under one spine*, never more places to go.

## The Cut lens, composed (decided 2026-07-25)

The Cut lens is not only a *reading* of the spine — it is where the writer **composes a take**: chooses which beats belong, arranges them in runtime order, and in doing so authors the transformed relationship every other projection then hangs off. This makes concrete what decisions 5–6 named. Four parts:

1. **Selection from the spine.** The writer selects beats. The cut is *what remains* (decision 5) — not every beat need enter it — and the accent means selection and nothing else (ch.14 rule 4). An unselected beat is not deleted; it is simply not in this take.

2. **Placement — movement to a runtime position.** A selected beat is moved to where it plays, which need not be where it sits in the source. This is the "authored runtime order" the Cut lens already reads by; composing it is the writer setting that order. The beat keeps its whole anatomy through the move (ch.14 rule 6) — a settling, not a new object.
   - **Where placement happens — the Cut strip, a second lane (decided 2026-07-25).** This answers the open question left by retiring the surface picker (how reading-by-runtime-order returns without a destination). The source-position strip stays the *reading* and does not move; **beneath it a second lane — the Cut strip — holds the kept beats in runtime order**, and dragging a chip there is placement by hand. Reading above, composing below: one surface, two lanes, no picker and no mode to switch. The Take fires from this lane, with the cut it records. A beat moved here draws its provenance noodle. (This is the runtime reading *evolving from the stage* that decision 5 required; it is not a return of the retired canvas — it is a lane, not a free 2D space.)

3. **The provenance noodle — a grounding thread, NOT a patch wire.** When a beat is placed away from its source position, a **clickable provenance thread** links the placement back to where it came from. This is deliberately *not* the node/wire/port "noodling" ch.14 retired (that was free runtime-wiring on an infinite canvas, a machinist's surface). This noodle carries no runtime order — the placement on the spine already does. What it carries is **grounding made visible**: the beat's `StorifyBeatProvenance` (ch.4 — origin, source hash, confirmed Grounding, operation version) and its source-position origin, so a move can never drift free of the source it came from (decision 4, the Score's one non-negotiable). Clicking it **situates the Copilot on that one cut decision** (ch.15), handing her the cut-script reasoning the writer needs:
   - **cues** — what this juxtaposition now creates that neither beat did alone;
   - **questions** — what setup, continuity, or knowledge the move breaks or presumes;
   - **consequences** — what later beats now assume because this one moved.
   The noodle is thus the writer's *and* the Copilot's shared handle on a single decision, grounded by construction. (It is honest per ch.11/12: it states a real relationship, never a fabricated one, and shows nothing for a placement that has no provenance to carry.)

4. **The take is the transformed root; projections have one cut.** The selected, arranged beat list, fired, becomes a **take** (ch.14 rule 11 / decision 6): a timestamped render of the arrangement as it stood. The new architectural commitment: **once a take exists, it is the root the other projections read from.** Before a cut, projections hang off the raw spine in source order; after one, each projection binds to the take and reads its *runtime* order and measure. Every downstream projection therefore carries a **"has one cut"** relation — the Text participant renders the take's order, the Music participant scores it, any later medium projects it — each bound to exactly one take as its root, none inventing its own order. A projection with no take falls back to the spine (source order), honestly; it never fabricates a cut it does not have.

This keeps the whole doctrine: one surface (the Cut is a lens, not a place), grounding as the condition of entry (the noodle *is* the visible grounding), the take as the transport's product, and no revival of the retired canvas — the provenance thread is a grounding relationship on the spine, never free wiring in 2D space.

## What is retired

- **The Cut Script patch-graph canvas** (chapter 14 rules 7–9): the free 2D space, nodes, wires, ports, and the renderer-as-node output. Deprecated and removed as a surface. Its *purpose* — arranging beats in authored runtime order and rendering a cut script continuously to the bundle — survives as the **Cut lens** of the Score and the transport's take.
- **"Move between Storify / Cut / Score" as a navigation model.** There is one surface with lenses; there is no longer a place the writer is sent to.
- **The three-icon surface picker, and the Score-as-its-own-view** (see "Where the stage actually is"). The Score is the surface the writer is already in; only its lenses are selectable.

## Honesty (non-goals)

- **A lane is not a fabricated participant.** A participant appears only when a real actor backs it (the Text lane is backed by the source). The Score never shows a Piano or a Light lane as decoration for a work that has none — that is chapter 11's interpretive overreach and chapter 12's foreshadowing-of-content, on a larger canvas.
- **Protocol state is not invented.** Properties, capabilities, and subscriptions are shown only for participants that actually declare them. An empty or stubbed protocol area states its absence; it never displays plausible-looking UMP traffic.
- **Familiarity is not the goal; presence is.** The DAW geometry orients the writer, but the Score is measured by whether participants meet under a common grounded structure, not by resembling a workstation.
- **The take is not a promise of quality** (chapter 14 non-goal, retained): it records what the arrangement was, nothing more.
- **Consolidation is not feature-loss disguised as simplicity.** Folding the timeline and Cut into lenses must preserve what each did (read by source position; arrange by runtime and render the cut script); it removes a *navigation model and a canvas grammar*, not capability.

## Relationship to other chapters

- **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** — the parent. This chapter keeps its beat anatomy (HEADER · TITLE · BODY · MEASURE), its measure-is-the-transformation rule, its unanchored span, and its take; it **supersedes** that chapter's patch-graph canvas (rules 7–9) and relocates the trigger/clock from the canvas to the Score's transport.
- **[Target architecture](04-target-architecture.md)** / **[Grounding contract](05-grounding-contract.md)** — supply the identity every participant carries on entry (decision 4). The Score surfaces lineage; it does not weaken it.
- **[Animating truth](12-animating-truth.md)** — the Score opens on cheap/known truth (the spine from the source) and foreshadows the rest; lens-crossing settles rather than cuts; absent participants are honestly absent, never faked.
- **[Storage and performance](13-storage-and-performance.md)** — the document layer (cut script `.fountain`) and the musical layer (MIDI 2.0) are the two destinations a take writes; the Score adds *when* and *by what*, and forbids a second notion of musical time.
- **[The situated Copilot](15-the-situated-copilot.md)** — the Copilot is a participant situated in the Score; she perceives which lens hosts her and which participants are in the conversation, and offers nothing whose object the surface does not show.
- **[The timeline is the machine room](16-the-timeline-is-the-machine-room.md)** — one machinery, one surface. The Score is that surface; the timeline and Cut are its lenses, and no fourth "view" is a place.
- **App-flow record (`reframe-app-flow-governance.md`)** — the writer's journey now flows *into* the Score and stays there; that record must narrate one surface with lenses, not three destinations.

## Acceptance

The doctrine is met when:

1. **There is one working surface.** The application presents the Score; the timeline and the Cut are lenses of it, and no flow sends the writer to a separate Storify, Cut, or Score destination. **Concretely: there is no surface picker at all** — not for the Score, and not for its lenses. The writer is standing on the stage; nothing above it offers a choice of where the work lives (see "Where the stage actually is", which revises decision 1 on this point).
2. **The beat-spine is the structure**, built from the source and carrying each beat's provenance; an un-read manuscript shows one unanchored span, never an empty stage.
3. **The Text participant renders the source** beneath the spine, grounded, with the beat anatomy of chapter 14 and the measure changing with the lens.
4. **Lens-crossing is a transformation** (source-position ⟷ runtime-order), animated as a settling, with the beat keeping its anatomy across the crossing.
5. **The transport produces a take** that renders the cut script to the bundle; no patch-graph canvas, node, wire, or "copy/save" verb exists for it.
6. **Every participant states what it is grounded to;** none appears without a real actor behind it, and no protocol state is shown for a participant that does not declare it.
7. **The Score opens simple** — text and spine — and media lanes, inspectors, subscriptions, and the protocol monitor appear only when a real participant or trigger calls them.
8. **The distributed stage is reachable, not present:** nothing in the minimum Score fabricates a participant, a remote instance, or UMP traffic to appear more complete than the work is.
9. **The Cut lens composes a take** (see "The Cut lens, composed"): the writer selects beats and places them in runtime order; a placement away from source carries a clickable **provenance thread** (grounding, not a patch wire) that situates the Copilot on that one cut decision. Firing produces a take, and **once a take exists the projections read from it** — each carrying a "has one cut" relation to exactly one take, falling back to the source-order spine when there is none, never fabricating a cut.
