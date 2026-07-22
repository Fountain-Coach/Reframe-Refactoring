# The Timeline Is the Machine Room — What You See Is What You Get

> Chapter summary: Making beats **is** the machinery, and the beat timeline is where that machinery is seen. There is therefore no second entity: no machine room, no factory gate, no engine view, no run report, no heartbeat line. A surface that exists to *describe* the work instead of *being* it is a false lane, and it is deleted rather than relocated. This chapter states which surfaces are allowed to exist at all; it does not prescribe unverified types or call paths.

## Purpose

The app grew a second self. Alongside the timeline where beats are made, it accumulated a **Machine Room**, a **Factory Gate**, **Engine Room** views, a run **report** delivered into the conversation, and a **health line** counting heartbeats. Each was added for a real reason — someone needed to see what the run was doing — and together they became a parallel account of work that was already visible.

The measurements are unambiguous. `StorifyMachineRoomView` is **3,839 lines with zero references outside its own file**. `StorifyFactoryGateView` (838 lines) and `EngineRoomViews` (1,412 lines): **zero**. Six thousand lines of surface that nothing constructs — a room with no door. Meanwhile **212 distinct `storifyMachineRoom*` properties, referenced 1,678 times**, are not vestigial at all: `storifyMachineRoomWindowHistory` is read from 34 places and is precisely what the timeline turns into the beats the writer sees.

So the naming inverted the truth. The "machine room" was never a room; it is the run state, and the timeline is its only rendering. The vocabulary then misled everyone who met it — including an agent who, while fixing a status line, proposed to "keep the diagnostic in the machine room", preserving a sentence for an audience that does not exist.

The writer's account is simpler and correct: *what we see is what we get — the beat timeline — and creating this is the machinery, so no other entity is of any interest.*

## The principle — one machinery, one surface

The making of beats is not a process that a surface reports on. It is a process that a surface **is**: the source stands as an unanchored span, a read-head advances through it, ghosts foreshadow where structure will land, and beats settle in as they become true. A writer watching that is watching the machinery, at full fidelity, in the only place it is real.

Anything that restates this elsewhere is not extra transparency. It is a **second source of truth about the same work**, and it will drift, contradict, and interrupt — which is exactly what a run report arriving in the conversation after the writer has stopped waiting for it does.

## The decision

1. **The beat timeline is the machinery's only surface.** No machine room, factory gate, or engine view exists as a place the writer can go. Work is shown where it happens.
2. **Progress is expressed as structure, never narrated.** The read-head's position, the ghosts, the settling of beats and the passage readout are the progress. A sentence that says the same thing in other words is redundant at best (see [chapter 12](12-animating-truth.md)).
3. **A log is not a lane.** No run report, transcript of windows, or accumulated status is delivered into the conversation. The Copilot's lane is conversation with the writer; a log bubbling into it is a category error, and it arrives precisely when the writer has stopped waiting (see [chapter 15](15-the-situated-copilot.md)).
4. **A diagnostic may drive behaviour; it may not become a surface.** Stall detection, heartbeats, and timing are legitimate inputs to what the app *does* — retry, resume, fail visibly. They are not sentences to show and not screens to open.
5. **State is named for what it is.** Run state is run state; naming it for a room invents the room. Vocabulary that implies a surface which must not exist is itself a defect.
6. **Unreachable surface is deleted, not kept.** Code that no path constructs is not "available later" — it is a claim about the product that is no longer true, and it decays into a map of a place that was never built.
7. **If it cannot be shown on the timeline, ask whether the writer needs it.** The first question about any machinery detail is not "where do we put it" but "does the work of making beats require the writer to know this at all".
8. **Failure is exempt, and must stay loud.** None of the above permits swallowing an error. A run that fails says what failed, in the writer's words, and says what was and was not changed. Silence is not simplicity.

## Honesty (non-goals)

- **This does not hide the machinery.** It shows it in the only place it is real. The writer sees more of the read on the timeline than any report ever told them.
- **This is not a ban on instrumentation.** Logs to stderr, telemetry, and stored run records are not surfaces; they cost the writer nothing and may be as detailed as the work requires.
- **Deleting a view is not deleting behaviour.** The run state that the dead surfaces displayed remains the state the timeline renders. What goes is the second account of it.
- **This is not an argument against detail.** A writer who wants to know why a passage was read as it was is asking about *their manuscript*, and the surface should answer — as structure, in place.
- **One surface is not one control.** The timeline may carry many affordances; chapter 14 rule 9 still governs which belong to which arrangement.

## Relationship to other chapters

- **[Animating truth](12-animating-truth.md)** — supplies the positive form of this rule: the surface animates the work, so nothing needs to narrate it. This chapter draws the consequence — the narration, and the places built to hold it, go.
- **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** — establishes the beat as one object across the timeline, the canvas, and the score. Those are *arrangements* of the work; a machine room was never one, only a description of it.
- **[The situated Copilot](15-the-situated-copilot.md)** — the conversation is her lane, and rule 3 above keeps logs out of it. A report dumped into chat is the same category error that chapter forbids, arriving from the other direction.
- **[Storage and performance](13-storage-and-performance.md)** — a second surface costs a second set of reads. Retiring it removes work as well as words.
- **App-flow record (`reframe-app-flow-governance.md`)** — must describe one machinery with one surface; any account of a separate room is superseded by this chapter.

## Acceptance

The doctrine is met when:

1. **No machine-room, factory-gate, or engine-room surface exists in the app,** and none can be reached by any path.
2. **No code remains for such a surface** — unreachable view files are deleted, not retained.
3. **The conversation carries no run report** and no accumulated window log; a settled read is stated once, in the writer's words.
4. **No visible status names internal machinery** — no phase names, no heartbeat ages, no "next window" countdowns.
5. **Stall and timing diagnostics still exist and still act** — resuming, retrying, or failing visibly — without appearing as sentences or screens.
6. **Run state is named for the work,** not for a room, and no identifier implies a surface that must not exist.
7. **The timeline alone shows the read** — unanchored span, read-head, ghosts, settling beats, passage readout — and it is sufficient to follow the work without any other view.
8. **A failed run is unmistakable,** says what failed, and says what was left unchanged.
