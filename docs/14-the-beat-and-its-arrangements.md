# The Beat and Its Arrangements — One Object, Three Views, One Firing

> Chapter summary: A beat is **one object**. The Story timeline, the Cut Script canvas, and the Score are not three views that each invent their own beat — they are three **arrangements** of the same widget, and crossing between them must read as a *transformation*, not a replacement. This chapter fixes the beat's anatomy, names the one part that is allowed to differ (its **measure**), states the rules of the canvas as a patch graph (nodes, wires, a renderer, a trigger), and defines the **take** — one firing that renders the document layer and the musical layer as siblings. It defines required behaviour and constraints; it does not prescribe unverified types or call paths.

## Purpose

The beat was two objects. The Story filmstrip drew it in SwiftUI with one corner radius, padding, type scale and colour set; the Cut Script canvas drew it in AppKit with different ones. Crossing between the two surfaces therefore read as a *replacement* — the widget the writer had been working with vanished and an unfamiliar one appeared in its place — which broke the journey at exactly the moment the writer is meant to feel a **transformation**: the same story, re-arranged in time.

The same fracture ran deeper than pixels. The canvas is a **patch graph** — beats are nodes, wires are the runtime order, the Copilot is a node acting on wired beats — and yet its *output* was a menu command in a toolbar ("Copy cut script", "Save cut script"). A patch graph has no menu verbs. Output on a canvas is a node you wire into, and it renders because something upstream fires it. That missing trigger is also the missing bridge to the musical layer, because a trigger is a **clock**, and a clock is what the MIDI 2.0 projection has been waiting for.

## The principle — one object, differently arranged

A beat does not change identity when the writer changes surface. What changes is **arrangement** — the order the beats are laid in, and the axis they are laid against:

| Arrangement | Order | Axis | Measure |
| --- | --- | --- | --- |
| **Story timeline** | manuscript order | source line position | the source it covers |
| **Cut Script canvas** | authored runtime order | free 2D space | the time it costs |
| **Score** | authored runtime order | musical time | its place in the beat clock |

Everything else about the beat — its name, its title, its text, its ground, its edge, its selected state — is *invariant across arrangements*. This is the whole doctrine of this chapter, and the rules below are its consequences.

## The decision

1. **One anatomy, declared once.** Every rendering of a beat, on every surface and in any UI framework, reads its geometry, type scale, and colour meanings from a **single declared widget spec**. A surface may not invent a corner radius, a padding, a type size, or a colour meaning for a beat. Where two renderers use different frameworks (SwiftUI, AppKit drawing, and later a score renderer), both read the same spec.
2. **The anatomy is fixed: HEADER · TITLE · BODY · MEASURE.** The header names the beat and carries what it currently *is*; the title is the beat's name; the body is the manuscript's own text, always monospaced, because it is source text on every surface; the measure is a single trailing figure in the same corner on every surface.
3. **The measure is the only part that may differ — and that difference *is* the transformation.** `ll. 3–32` on the timeline becomes `0:33` on the canvas: same slot, same corner, same eye position, a different unit because a different axis. A surface that needs to say more than one figure has misidentified its axis.
4. **Colour carries one meaning everywhere.** The accent means **selection** and nothing else. Over-budget is its own colour and appears only where a budget exists. A surface may not repurpose a colour that means something else elsewhere.
5. **The unmade beat is the same object.** A stretch of source that no beat yet represents keeps the widget's shape and dashes its edge. Making a beat is that object *settling*, not a new object appearing. A manuscript that has not been read into beats is therefore not an empty surface: it is **one unanchored span across its scope**, which is a state the timeline already has a name for.
6. **Crossing arrangements is animated as transformation.** The change of surface settles (a spring, not a cut); the widget keeps its anatomy through the crossing so the eye tracks the same object into its new arrangement.

## The canvas is a patch graph

The Cut Script canvas is a wiring surface in the tradition of Quartz Composer and Vuo, and it must obey that grammar rather than the grammar of a document window:

7. **Output is a node, not a command.** The assembled Cut Script is a **renderer node** on the board with a wired input — permanently present, showing the assembled result live, with its measure (runtime, kept proportion, what spills). "Copy" and "Save" as toolbar verbs are prohibited on this surface: they exist only because the output previously had nowhere to live.
8. **A renderer writes to its destination continuously.** The destination already exists in the document layer (chapter 13): the cut script is a plain `.fountain` file in the manuscript's bundle. The renderer writes there as the graph changes. There is no save verb because there is no unsaved state.
9. **A surface's controls belong to that surface.** Controls that act on an arrangement appear only in that arrangement. A control offered where its object is not visible is a category error, not a convenience.

## The trigger, and the take

10. **The trigger is the clock.** The canvas fires by **playing its wiring**: the transport walks the wired order in story time, and the renderers assemble as it goes. This is what makes the graph live rather than static, and it is the only honest source of progress on this surface — what the writer watches is the cut being made.
11. **A firing produces a take.** A take is a timestamped render of the wiring *as it stood*. Takes are comparable, and the latest take is what the bundle holds. This is the same versioning language the beat already uses (the source is v1; each kept reframe is v2+); a trigger does not "save", it **takes**.
12. **One firing, two renders — as siblings, never as a conversion.** The same take renders the **document layer** (the cut script, story time) and the **musical layer** (the score, beats time). Neither is derived from the other: chapter 13 is explicit that the musical layer is never encoded into the document files and the document files are never encoded as MIDI. They are two projections of one order under one clock.
13. **The two clocks meet arithmetically, not by translation.** Every beat already carries a runtime; the musical spine already carries a tempo. Runtime and tempo give beats, and beats are what a UMP timestamp counts. The budget readout on the canvas and a timestamp in the score are therefore the same quantity in two units — no new concept, and no lossy mapping, is permitted to sit between them.

## Honesty (non-goals)

- **A shared spec is not a shared renderer.** Surfaces legitimately differ in what they *afford* — the timeline card carries per-beat actions, the canvas node carries ports and a cumulative position. Unity is of anatomy and meaning, not of feature set.
- **The unanchored span is not a fabricated beat.** It states that a stretch of source is not yet represented. It must never be titled, counted, or coloured as though a reading had produced it (chapter 11's prohibition on interpretive overreach; chapter 12's on foreshadowing content).
- **A take is not a promise of quality.** It records what the wiring was, nothing more. Nothing may present a take as an evaluation.
- **The bridge to MIDI 2.0 is a binding, not a new mechanism.** The projection to UMP already exists. What this chapter requires is that the *story* beat order and clock bind to it — and it forbids inventing a second, parallel notion of musical time to avoid doing so.

## Relationship to other chapters

- **[Animating truth](12-animating-truth.md)** — the crossing animation and the settling of an unanchored span into beats are that chapter's doctrine applied to this object: motion marks a real state change, and the unread region is foreshadowed as honestly unread.
- **[Storage and performance](13-storage-and-performance.md)** — supplies both destinations a take writes to: the cut script in the document bundle and the score as MIDI 2.0. This chapter adds only *when* they are written and by what.
- **[Grounding as a given](11-grounding-as-a-given.md)** — the same honesty ethic governs the unanchored span: show what is true now, mark the rest as not yet read, manufacture nothing.
- **[The situated Copilot](15-the-situated-copilot.md)** — the Copilot is a node on this canvas, and rule 9 above binds her as it binds any control. That chapter gives her the perception required to obey it: which arrangement hosts her, and which beats are wired into the conversation there.
- **[The timeline is the machine room](16-the-timeline-is-the-machine-room.md)** — the timeline, the canvas and the score are *arrangements* of the work. A machine room was never one of them, only a description of it, and that chapter retires the description.
- **App-flow record (`reframe-app-flow-governance.md`)** — the beat's journey across arrangements is part of that flow and must be narrated there as one object.

## Acceptance

The doctrine is met when:

1. **Every beat rendering reads one declared widget spec** — geometry, type scale, and colour meanings — and no surface declares its own.
2. **The anatomy is identical across surfaces** (HEADER · TITLE · BODY · MEASURE), with the measure as the only differing part, in the same slot.
3. **The accent means selection on every surface,** and no surface repurposes it.
4. **A manuscript with no beats presents one unanchored span across its scope,** in the beat widget's shape with a dashed edge — never an empty surface and never an interim screen.
5. **Crossing between arrangements settles rather than cuts,** and the widget keeps its anatomy through the crossing.
6. **The Cut Script is a renderer node on the canvas** with a wired input and a live result; no toolbar carries "copy"/"save" verbs for it, and its destination in the bundle is written continuously.
7. **Every control appears only in the arrangement it acts on.**
8. **Firing the transport produces a take** that renders the cut script and the score from one order under one clock, with neither derived from the other.
9. **The canvas budget and the score's timestamps agree numerically,** being the same quantity in two units.
