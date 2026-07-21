# Reframe — How the App Must Flow

> A governance record of the whole application, in prose. This document is normative:
> it states how Reframe **must** behave, not how any particular build happens to behave.
> Where a rule already has a home in the chapter set (grounding contract, target
> architecture, grounding-as-a-given, the Copilot extension), this record restates it as
> one continuous account so the app can be reasoned about as a single thing.

## 0. What Reframe is

Reframe is a **modernization studio**: a tool a writer uses to take an existing source
work — a play, a novel, a chaptered prose text — and **reframe** it into a new destination
form, a screenplay by default. It is human-authored and AI-assisted, but authority is
always the writer's: the machine proposes structure and drafts text; the human decides.
The source is never overwritten; the reframe is a new artifact that stands beside it.

Reframe ships opinionated. It carries a reading philosophy — the "Non-Integrational"
stance — and applies it by default so the writer can begin working immediately rather than
filling in a philosophy first.

## 1. First principles (the invariants that never bend)

These hold across every surface. Nothing later in this document may contradict them.

1. **The source text is the factual authority.** What happened, who spoke, in what order —
   these are read from the canonical source, never invented. Grounding shapes *salience and
   permitted transformation*, not fact.
2. **Confirmed Grounding is the single downstream contract.** Every structural and
   generative stage reads from confirmed Grounding. There is no second, competing policy.
3. **The grounding path is deterministic and provider-free.** Composing, confirming,
   projecting, and identifying Grounding never calls a model and never re-reads the source.
   A model may later help the *writer* shape Grounding conversationally, but the artifact
   itself is produced by deterministic rules.
4. **Human interpretation is final.** AI output is structural and revisable; it is never
   promoted to authority on its own. Ordinary conversation is never silently converted into
   confirmed Grounding.
5. **Uncertainty stays visible.** Where the source is unread, thin, or genuinely ambiguous,
   the app says so rather than smoothing it over.
6. **Every durable artifact bears an identity, and identity drives staleness.** When an
   upstream artifact changes, everything derived from it is marked stale rather than
   silently trusted.

## 2. The canonical manifesto — grounding as a given

Grounding is the writer's contract with every downstream stage: an author baseline (how the
source's authorial stance is honored), a reader lens (who the reframe is for), the source
language, the destination medium, a structural intent (what the reframe should *seek*), and
optional preservation duties and transformation boundaries.

Reframe does **not** demand this as a form at the threshold. It ships **one canonical
manifesto** — the house reading stance, of the Non-Integrational family: preserve irreducible
source difference; do not manufacture continuity, causality, or thematic unity the source
does not establish; keep uncertainty visible; ground every claim in evidence; avoid
deterministic identity claims, redemptive closure, and interpretive overreach.

The manifesto is a **given**:

- It is **edited centrally, as prose**, in Preferences — one flowing document, the single
  global default every manuscript inherits. It is never dissected into fields by a model;
  when the app needs the fields, it parses the prose deterministically by its section
  headers.
- On import or open, a manuscript **inherits the manifesto as its confirmed Grounding**
  automatically — source language auto-detected, destination medium defaulted to screenplay,
  structural intent defaulted to a sensible universal. This auto-confirmation is an explicit
  product default the writer can inspect and change; it is **not** an inference from chat.
- An existing confirmed Grounding is **never** overwritten by the default. A writer who has
  authored their own stance keeps it.

Structural intent is the one field carrying genuine per-writer intent. It is **defaulted and
hidden by default**. The Copilot may raise it — as an *offer*, never a gate — when shaping it
would materially change the read.

## 3. The spine of the flow

The writer's path is short: **Library → (open / import) → Story → Cut Script → Score**, with
Continuity available as a checking stage across the reframe.

Grounding is **not a stop on this path.** Because the reading stance is a *given* — inherited
automatically and changed centrally in Preferences (§2, §6) — opening a manuscript takes the
writer straight to the structural read, **Story**. The writer never moves *through* Grounding.

The writer's navigation surfaces are exactly **Library · Story · Score** (with Cut Script and
Continuity as the maturing work between Story and Score, not separate tabs). Grounding is not
among them — it is a **Preferences** concern, the canonical manifesto edited as prose. There is
likewise no Index surface; semantic indexing has been removed (§16).

## 4. Launch and the Library

On launch, Reframe opens to the **Library** — the writer's manuscripts, browsable and
switchable in place. On first run against an empty store it installs its bundled works
(Ulysses, Ovid's Metamorphoses) **as sources only** — the whole text, its chapters named, and
nothing else. No pre-built reading and no index ship; the writer brings their own model
account and does the structural read on their own terms. Installation is non-destructive: a
work the writer has already opened, read into, renamed, or cut is left untouched.

The Library must load without blocking the writer from importing, and must never present an
empty void where a real failure occurred — if the corpus service cannot start, it says so.

## 5. Opening or importing a manuscript

Opening an existing manuscript or importing a new source (from a file or a web corpus) must
converge on the same landed state:

1. The source is loaded and its structure (chapters) made addressable.
2. **Grounding is auto-confirmed from the canonical manifesto** if the manuscript has none —
   deterministically, provider-free, per §2.
3. The writer **lands on Story**, the structural read.

There is **no Grounding surface to land on and no gate to clear.** The given is settled behind
the writer; the work — the structural read — is what they are shown. If for any reason the
given is not yet in place at the instant of landing, the app still opens on the writer's work
surfaces and the given settles behind them; it must never park the writer on a grounding form.

## 6. Grounding — the given, and where it changes

Grounding is held as the confirmed contract behind every stage, but it is **not a surface the
writer visits.** There is no per-manuscript Grounding form or tab in the writer's flow. The
given is inherited automatically on open (§2, §5) and simply *is* in effect.

When the writer wants a different stance, there are two doors — neither of them a
per-manuscript form:

- **Preferences.** The canonical manifesto is edited there as one prose document: the single
  global default every manuscript inherits. Editing it re-identifies Grounding and marks
  dependent downstream artifacts stale (§13). This is the home of the reading stance.
- **The Copilot.** A writer can shape the stance conversationally ("ground it with me"); the
  Copilot proposes and the writer confirms (§11).

Confirming — whether the auto-confirmed default, a Preferences edit, or a Copilot-assisted
change — assembles the policy fields into **one Grounding identity** (a content hash over the
policy fields), computed deterministically with no model call. Grounding is **never created
implicitly** from conversation; the auto-confirmed default is an explicit product default the
writer can inspect and change, and every other change is the writer's explicit act.

## 7. Story (Storify) — the sole structural reader

**Storify is the only thing that reads the source into structure.** Under confirmed Grounding
it performs the structural read ("Source Auto"): it segments the reading into **beats** and
records **windows** over the source (line spans, with their uncertainties and any unreadable
spans marked). Grounding governs what the read foregrounds and what transformation it permits;
the source atoms govern fact. The read is stated to be what it is — a derived reading, not a
new source of truth.

Storify's structural read may spend on the writer's own model account, so starting it is a
**guarded** action the writer explicitly authorizes. Its outputs — beats, their synopsis,
windows, and the run's identity — are persisted and stamped with the Grounding identity they
were produced under, so any consumer can prove the exact Grounding-plus-Storify lineage it
read.

Story is also where the writer's questions about the work are answered. "What is this story
about?" is answered from **Storify's beats** — a compressed, derived digest that carries the
open questions and unreadable spans honestly — never from a separate index. When the reading
is thin, the answer says so.

## 8. Cut Script — the reframed work toward the medium

The **Cut Script** is the reframe itself: the beats carried toward the destination medium
(screenplay by default), arranged and edited by the writer. It offers order (a timeline of
beats), a freeform board for spatial arrangement, and a runtime budget in minutes that frames
the target length. It generates screenplay (.fountain) text when the writer wants it.

The Cut Script is downstream of Storify and Grounding: it records the Storify-plus-Grounding
identity it consumed, and it is marked stale when either changes.

## 9. Continuity

**Continuity** is the checking stage across the reframe: it examines the assembled work for
the continuity the *reframe* commits to, while honoring the manifesto's refusal to manufacture
continuity the source never established. It is a stage in the journey, reachable as work
matures, and it reports rather than silently repairs.

## 10. Score — the MIDI 2.0 surface

**Score** is Reframe's native musical surface: a MIDI 2.0-native score composed per cut. It is
one of the four navigation surfaces and reads from the settled structure like any other
downstream consumer — never from a removed index.

## 11. The Copilot — conversational authority, offer-not-gate

The Copilot is the conversational front door and the working partner, present beside the
manuscript. Its governing rules:

- **Silent on open, ready on demand.** It does not auto-fire a greeting turn when a manuscript
  opens (which would both surprise the writer and spend on their account). It wakes when
  addressed.
- **Its perception is grounding-first.** It reasons from live authority — the confirmed
  Grounding, the Storify structure, and the journey's readiness — not from any stale memory or
  removed index. It can answer "where are we" and "why can't I continue" from that truth.
- **It proposes; the writer disposes.** Editorial actions are represented as typed operations
  and gated: anything that spends on the writer's account or replaces the source is
  **guarded** and requires the writer's go-ahead. Slash commands and the planner reach the
  same operations.
- **It never fabricates Grounding from chat.** It can *help the writer author* Grounding
  conversationally ("ground it with me"), and it can confirm the current draft when the writer
  asks — but only when the draft is complete, reporting the verified persisted result, never
  inventing a stance from the conversation.
- **Structural intent is an offer, never a gate.** The Copilot may propose shaping structural
  intent when it would materially change the read; it never blocks the read on it.

## 12. Readiness and the journey (monotonic staging)

The app carries a single **journey** projection — the writer's position along the spine —
derived from readiness that is **monotonic**: grounding-ready, then storify-ready, then
cut-script-ready, then continuity-ready. A later stage can never report ready before its
predecessor. The journey is the one source of truth for "what stage are we in / what's next,"
consumed by the operator guidance and by the Copilot's perception alike, and it speaks in
grounding-first vocabulary only.

## 13. Identity, staleness, and invalidation

Every durable artifact carries a content identity:

- **Grounding** — a hash over its policy fields.
- **Storify** — a hash over the settled structure together with the Grounding identity it read.
- **Cut Script and beyond** — the Storify-plus-Grounding lineage they consumed.

When an upstream artifact's identity changes, everything derived from it is **marked stale**,
visibly, rather than silently trusted. Re-confirming Grounding or re-running Storify refreshes
the chain. Staleness is surfaced, never hidden, so the writer always knows when a downstream
view no longer reflects the contract above it.

## 14. Determinism and the no-model rule in the grounding path

The grounding path — composing the default manifesto, confirming it, projecting the working
contract, computing identity, parsing the prose manifesto into fields — is entirely
deterministic. No step calls a model, and none re-reads the source. This is not an
optimization; it is what makes the one artifact everything else depends on trustworthy and
reproducible. A model's help is confined to *conversation with the writer about* Grounding,
whose output the writer must still confirm.

## 15. Persistence and relaunch

Reframe persists to a durable store. Across relaunch it must restore the source, the confirmed
Grounding, the Storify windows and structure, the Cut Script, Continuity results, and the
conversation history. In-memory-only state (transient view state, the Copilot's ephemeral
perception) is recomputed. A freshly opened manuscript must leave a landed, current record so
that other surfaces and any cross-app handoff read truth, not a half-flushed write.

## 16. What Reframe deliberately does not do

Reframe **removed the semantic index** and everything that gated on it. There is no Index
surface, no background reindex, no "read-in-chapter" step that builds an index, and no path
that requires a pre-built index before the writer can work. Structure comes from Storify;
story knowledge comes from Storify's beats. Any lingering inert status-plumbing is exactly
that — inert — and must never re-become a gate.

## 17. Navigation, in one sentence

The writer moves through **Library · Story · Score** — the Copilot alongside, Cut Script and
Continuity as the maturing work between Story and Score — and **never through Grounding**, which
is the settled given: changed in Preferences (or with the Copilot), not a stop on the path.
