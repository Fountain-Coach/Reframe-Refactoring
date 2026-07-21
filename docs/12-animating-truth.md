# Animating Truth — Foreshadowing and Perceived Performance

> Chapter summary: The application must never sign its waiting with a spinner. A spinner is the animation of *absence* — indeterminate, meaningless, and read by the writer as overload or hang. Instead the app **foreshadows**: it renders the frame and every cheaply-known truth instantly, and streams the expensive truth in as honest, animated structure whose motion **maps to real work**. This chapter sets that doctrine and applies it first to **loading**. It defines required behaviour and constraints; it does not prescribe unverified types, files, or call paths. Perceived performance is not a substitute for real loading performance — both are required.

## Purpose

The journey from launch to a working surface is today *signed by spinning wheels*: the library spins while it loads, bootstrap spins, and opening a manuscript lands on a Story pane that shows an empty box, a bright frame, and "Starting…". Individually each is a small delay; together they read as **overload and hang** — the app feels heavy before the writer has done anything.

The delays are partly real (loading performance must improve — this chapter does not excuse it) and partly a *presentation* failure: the app withholds everything until everything is ready, then signs the wait with the one animation that says nothing. This chapter fixes the presentation and sets the standard the real performance work must meet.

## The principle — animate truth, not absence

A spinner tells the writer nothing: not what is coming, not how far along, not whether anything is wrong. It is the animation of absence, and it is the **last resort** — reserved for a genuinely unknowable, genuinely short wait, never for a load whose shape is already knowable.

Everywhere else the app must **animate truth**: motion must express something real that is happening, or that has just become true. Three consequences follow, and the rest of this chapter is their application:

- **Motion maps to work.** Every animation corresponds to a real state change — a row arriving, a beat settling, the read-head advancing. Motion disconnected from state is only a prettier spinner and is prohibited.
- **The frame never waits for everything.** What can be shown now is shown now; the expensive truth streams in behind it.
- **The unknown is shown as honestly unknown** — foreshadowed as pending, never faked, never spinning forever.

## The decision

1. **Nothing waits for everything.** The frame and every synchronously-available truth render immediately; expensive truth streams in. No surface presents a full-screen indeterminate wait while a knowable frame exists.
2. **Every element enters as it becomes true.** A manuscript row appears when its name is known; a beat appears when it settles. The entry animation marks the instant that datum became real.
3. **Cheap and cached truth is shown first.** Persisted structure paints instantly on reopen; any refresh happens *behind* what is already on screen, never by blanking it back to a spinner.
4. **The unknown is foreshadowed as honestly unknown.** Placeholders read as *pending* — dim, quiet, alive — and resolve either to real content or to a visible NOT-READ / failure state. A placeholder that cannot fill must never animate forever.
5. **Motion carries progress spatially and semantically** — a read-head's position, a structure filling in — not an abstract spinner or a bare percentage.
6. **The spinner is the last resort**, reserved for the genuinely unknowable short wait alone.
7. **Nothing that is not the manuscript may delay the manuscript.** Bookkeeping the writer did not ask for — a
   last-opened pointer, a registry write, a usage record — must never sit between a click and the frame it asks for.
   Such work runs *behind* the open, never before it. No animation excuses a wait that should not exist, and the first
   question about any delay is whether it belongs on the path at all.
8. **Absence must not overwrite a truth already held.** When a slower authority has not yet loaded, its emptiness is
   not an answer: a surface may not publish "nothing" over structure that is already on screen and correct. Only a
   loaded authority may clear what a cheaper one established.
9. **A click lands in the surface it asks for, not in an interim one.** If the destination can be rendered from truth
   already at hand, it is rendered at once — including its honest not-yet-populated state, which is a state of the
   destination, not a screen standing in for it. Interim screens between the click and the destination are prohibited.

## Loading, animated — how truth is animated at each moment

### At launch

Truth available immediately: the app shell, the identity of the last-opened manuscript, and the manuscript **registry** (names, last-opened, chapter counts) — all cheap reads. The library frame and its rows must appear as the registry resolves. A full-screen "Loading your library…" that withholds the whole list for tens of seconds is prohibited: the names are cheap truth and must be shown as truth.

### The library

The manuscript list is cheap truth. Rows **settle in** as each becomes known — a brief eased entrance keyed to the moment that row's data arrived. Skeleton rows stand only for a count not yet read, and resolve as it arrives. The motion is *rows arriving*, never the screen spinning.

### Opening a manuscript → Story

This is the worked case. At the instant Story is shown, the app already knows, cheaply, far more than it displays:

- **The chapters** — names, order, and line spans — are in the source structure, loaded early. The timeline **spine** (axis + chapter ticks) must **stroke in immediately** over them. This is truthful motion over real data.
- **Prior persisted beats**, if the manuscript was storified before, are a cheap store read and must **paint at once** — on reopen the writer sees their story instantly, with any refresh happening behind.
- **The unread region** shows **breathing ghost beats**: dim, low-contrast, phase-offset placeholders positioned along the spine where structure will land. They foreshadow *that beats will appear here*, never *what they say*.
- **A read-head sweeps** to the chunk currently being read (Telemachus → Nestor → …); its position *is* the progress indicator, replacing "Starting…".
- **Each settled beat resolves its ghost** — a short, eased crossfade-and-settle (~250–350 ms, spring not linear). The choreography of arrival is the progress bar; the writer watches the story take shape.

Prohibited on this surface: a bright accent frame around the pane (it reads as a selection or error box) and an empty box captioned "Navigator ready / Starting…" (it reads as a stall).

Also prohibited: **internal phase names on screen.** "Navigator ready", "Storify running", "Opening store…" name our machinery, not the writer's work, and a status line the writer cannot interpret is no better than a spinner. Every visible status says what is happening to *their manuscript*, in their words.

A manuscript that has not been read into beats is not an empty surface. Its source is a cheap read, so the timeline renders from it immediately and holds the whole scope as **one unanchored span** — a state the timeline already has a name for — which real beats then carve up as they arrive (see [chapter 14](14-the-beat-and-its-arrangements.md)).

## Honesty (non-goals)

This strategy must not become a lie, and it does not lower any other bar:

- **Never fabricate content.** Ghosts foreshadow *structure the source establishes* — chapters exist, beats will land here — never invented beat text, titles, or counts the reading has not produced. Foreshadowing structure is truthful; foreshadowing content the source does not establish is the interpretive overreach chapter 11 forbids.
- **A placeholder that cannot fill degrades to the visible NOT-READ / retry state.** Uncertainty stays visible (a first principle); a ghost must never breathe forever over a stalled or failed load.
- **Reduce-motion is honored.** With motion reduced, the app falls back to opacity/skeleton without movement; the truth-first *ordering* (frame first, cheap truth first) still holds.
- **This does not replace real loading performance.** Foreshadowing masks latency; it does not remove it. If the read takes thirty seconds it still takes thirty seconds — the writer merely sees honest progress instead of a hang. The actual load must also improve.

## Relationship to other chapters

- **[Target architecture](04-target-architecture.md)** — the critical-vs-ancillary hydration split is the seam that makes "the frame never waits for everything" real: the Story frame must render at *critical-hydration-complete* and stream the rest, rather than waiting on ancillary hydration.
- **[Grounding as a given](11-grounding-as-a-given.md)** — the same honesty ethic: show what is truly known now, mark the rest pending, never manufacture.
- **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** — what the Story surface renders while it waits, and how a beat settles out of an unanchored span, is that chapter's object under this chapter's doctrine.
- **App-flow record (`reframe-app-flow-governance.md`)** — this chapter governs how every surface in that flow must *load and feel*.

## Acceptance

The doctrine is met when:

1. **No surface presents a full-screen indeterminate spinner while a knowable frame is available;** the frame renders first.
2. **The library shows real manuscript rows as the registry resolves** — never a single "Loading…" gate for the whole list.
3. **Opening a manuscript renders the Story timeline spine from its chapters immediately,** and any persisted beats at once, before the storify run.
4. **The unread region is foreshadowed by placeholders** that read as pending and resolve to real beats or to a visible NOT-READ / failure state — never an eternal animation.
5. **Motion corresponds to real state changes** (a beat settling, the read-head advancing); no decorative-only motion stands in for progress.
6. **The bright accent frame and the "Navigator ready / Starting…" empty state are removed** from the Story surface.
7. **Reduce-motion is honored,** and the truth-first ordering holds without movement.
8. **No bookkeeping write blocks an open.** Opening a manuscript performs no work that the writer did not ask for
   before the frame appears.
9. **No surface publishes emptiness over structure it is already showing** while a slower authority loads.
10. **Clicking a manuscript lands in its destination surface,** rendered from truth already at hand, with no interim
    screen in between.
11. **No visible status names an internal phase or subsystem;** every status line is in the writer's terms.
