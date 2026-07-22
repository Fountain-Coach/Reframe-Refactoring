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

## What is retired

- **The Cut Script patch-graph canvas** (chapter 14 rules 7–9): the free 2D space, nodes, wires, ports, and the renderer-as-node output. Deprecated and removed as a surface. Its *purpose* — arranging beats in authored runtime order and rendering a cut script continuously to the bundle — survives as the **Cut lens** of the Score and the transport's take.
- **"Move between Storify / Cut / Score" as a navigation model.** There is one surface with lenses; there is no longer a place the writer is sent to.

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

1. **There is one working surface.** The application presents the Score; the timeline and the Cut are lenses selected in place, and no flow sends the writer to a separate Storify, Cut, or Score destination.
2. **The beat-spine is the structure**, built from the source and carrying each beat's provenance; an un-read manuscript shows one unanchored span, never an empty stage.
3. **The Text participant renders the source** beneath the spine, grounded, with the beat anatomy of chapter 14 and the measure changing with the lens.
4. **Lens-crossing is a transformation** (source-position ⟷ runtime-order), animated as a settling, with the beat keeping its anatomy across the crossing.
5. **The transport produces a take** that renders the cut script to the bundle; no patch-graph canvas, node, wire, or "copy/save" verb exists for it.
6. **Every participant states what it is grounded to;** none appears without a real actor behind it, and no protocol state is shown for a participant that does not declare it.
7. **The Score opens simple** — text and spine — and media lanes, inspectors, subscriptions, and the protocol monitor appear only when a real participant or trigger calls them.
8. **The distributed stage is reachable, not present:** nothing in the minimum Score fabricates a participant, a remote instance, or UMP traffic to appear more complete than the work is.
