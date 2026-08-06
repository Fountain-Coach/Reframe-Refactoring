# 48. A Service Is a Fact, Not a Symptom

> Chapter summary: Reframe reads, plans, imports and cites by calling services — the on-device model, a paid cloud
> lane reached through a spawned CLI, corpus APIs on loopback, reference sources on the open web, and the store.
> Every one of those calls has a **name, a lane, a cost class and an outcome**, and all four are known at the call
> site. This chapter requires that they be carried as facts and reported to the **writer**, in her terms, where she
> is working — and forbids the app from re-inferring a service's state downstream from its symptoms. A browser is
> the standard: it names the resource, shows the status, says *"this site can't be reached"* in the reader's
> language, offers the one action that exists, keeps the console for maintainers, and renders what it can.

## Purpose — the failure this exists to end

Measured 2026-08-06, reading Ulysses' **Circe** on the paid lane. The Codex CLI transport to `chatgpt.com` was
down. The writer's own console showed it plainly:

```
the ChatGPT call failed — Codex CLI failed (exit 1). Reconnecting... 2/5 (request timed out)
ERROR codex_models_manager::manager: failed to refresh available models: timeout waiting for child process to exit
ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed …
    http/request failed: error sending request for url (https://chatgpt.com/backend-api/ps/mcp)
```

Reframe never said any of that. Because a failed read is treated as evidence that the **window is too big**, the
reader narrowed its window and tried again, and again:

```
[PROMPT 8 atoms]                        4326 tokens = manuscript 2698
[PROMPT retry, 4 atoms]                 2949 tokens = manuscript 1370
[PROMPT retry, 2 atoms]                 2338 tokens = manuscript  785
[PROMPT 4 atoms, atom text COMPACTED]   2043 tokens = manuscript  260
[PROMPT retry, 1 atoms]                 1810 tokens = manuscript   65
```

It ended by handing the model **65 tokens of Joyce inside a 1,810-token prompt**, having cut the writer's text to
260 characters an atom — the on-device failure mode, at cloud cost, in answer to a dead network. Ninety-eight
seconds a passage, then a page deadline at six hundred.

Everything needed to say the true thing was known at the moment it happened. It went to a log written for
maintainers. What reached the writer was a reading of *Circe* getting quietly worse.

Two people then diagnosed it wrongly from the symptoms — including the agent, which located a real defect (a
budget clamped by a fallback lane's ceiling), fixed it, re-drove, and watched the identical numbers appear. A
symptom that is allowed to stand in for a cause will be diagnosed, repeatedly, by everyone who looks at it.

## The principle — the call site knows

A service call produces four things:

| | | |
|---|---|---|
| **which service** | fact | known at the call site |
| **which lane** | fact | known at the call site |
| **what it costs** | fact | known at the call site |
| **what happened** | fact | known at the call site |
| *what it means for the work* | judgement | reasoned afterwards |

Only the last is a matter for reasoning. The first four are facts, and
[ch.39](39-a-model-cannot-be-told-what-it-cannot-do.md) has already settled what to do with a fact about the app:
**where a fact exists, the app speaks it** — it is not re-derived, not inferred, and not left to prose. A
transport error is exactly that kind of fact. It was certain when it happened; every later attempt to recover it
by reading the words of an error message is a guess about something nobody needed to guess about.

This is the same disease, in a third place, as the machine notes that had to be filtered out of a reading's
questions by matching their opening words, and as the conflict annotation that ended up naming a beat. The cure is
the same: **give the fact a slot at the point it is known.**

## Binding — a service declares itself, and the register is derived

The first draft of this chapter carried a hand-written table of the services Reframe calls. **It was wrong within
the hour.** It omitted Ulysses-as-a-Service entirely —

```swift
// UlyssesAsAService: ULYSSES_BASE_URL (a self-hosted or richer edition) → the API SHIPPED INSIDE the app
static let defaultBaseURL = "http://127.0.0.1:8765"
```

— a real service with its own host, its own environment override and its own in-app fallback. A list of live
infrastructure maintained by hand is stale on the day it is written, and a stale list inside a governance chapter
is worse than none, because it is read as authority.

This repository already knows the answer. Capabilities are not listed in prose; they are **generated**
(`GeneratedCopilotCapabilities.swift`, marked "DO NOT EDIT") from declarations, which is why ch.37 can say Copilot
claims only what the registry holds. Services bind the same way. So this chapter does not enumerate services — it
defines **what a service must declare in order to be callable**, and the register is derived from those
declarations.

### What a service declares in order to bind

| field | why it is required |
|---|---|
| **identity** | a stable id, so an outcome can be attributed and persisted without matching prose |
| **writer-facing name** | what the writer is told when it fails — "Codex CLI" is not a sentence for a writer |
| **reach** | internal (in-process, loopback) or external (network) |
| **lane and cost class** | free or paid — [ch.20](20-on-device-first-and-the-writers-key.md) needs this *before* the call |
| **endpoint resolution** | the ordered chain: environment override → declared default → in-app fallback, or *none* |
| **health probe** | how to ask whether it is reachable, cheaply, without doing the work |
| **failure kinds** | which of the closed set (rule 2) this service can actually produce |
| **remedies** | which of the closed set of writer actions apply when it fails |

Two of those already exist in the code and were never written down, which is why they were never inherited:

- **Endpoint resolution is a chain, not a constant.** Ulysses and Ovid both resolve
  `ULYSSES_BASE_URL` / `OVID_BASE_URL` → a declared default → the corpus API shipped inside the app. That chain is
  what lets a self-hosted or richer edition replace a service without touching Reframe, and it is what makes the
  bundled works readable offline. Declaring it means a new service inherits the pattern instead of reinventing it.
- **A fallback is a service too**, with its own identity and lane. Falling back is an event the writer may need to
  know about — a free lane answering where a paid one was asked, or the reverse — and it cannot be reported if the
  fallback was never named.

### The other direction: how a service makes itself bindable

The same declaration is the contract a **new service reads**. Implement the routes, answer the probe, name your
failure kinds, and Reframe can call you with no change to Reframe. This is already true by accident of the corpus
API — anything speaking `/v1/episode/{n}` or `/v1/book/{n}` is a drop-in replacement today, which is exactly what
`ULYSSES_BASE_URL` is for — and the declaration makes it true by design.

### The register is generated evidence, not chapter prose

What Reframe calls *today* is generated from the declarations and lives with the other generated artifacts. A call
to a service with no declaration is a defect catchable at the boundary rather than by review. To know what Reframe
calls, read the generated register; to know what a service must **be**, read this chapter. The two cannot drift,
because only one of them is written by hand.

## The decision (enforceable rules)

1. **Every service call is typed at its call site** — service identity, lane, cost class, outcome — and that
   record travels with the result. No consumer recovers any of the four by inspecting a message string.

2. **A failure is classified by its KIND, where it is known**, from a closed set: *unreachable*, *not
   authorised*, *out of quota*, *too big for the window*, *refused on policy*, *too slow*. New kinds are added to
   the set, never expressed as a new sentence that another layer must recognise.

3. **A lane that cannot be reached is not a passage that is too dense.** Narrowing a window, compacting atom text,
   or any other adaptation of the writer's material is a legitimate answer to *too big for the window* and to
   nothing else. Adapting the work in response to a transport failure is forbidden.

4. **The writer is told, where she is working, in her own terms**: which service, whether it costs her money, what
   happened, and what she can do about it. A line in a log is written for maintainers and does not discharge this
   rule. Silence while the work degrades is the specific failure this chapter ends.

5. **Remedies are enumerated from what actually exists** — wait and retry, switch lane, stay on device, stop —
   and never invented. An offered remedy that cannot work is worse than none
   ([ch.24](24-the-reasoning-is-an-uncertainty-map.md): a failure is surfaced loud, never laundered).

6. **Health is learned from real calls, not only from a start-up probe.** A probe answers about a door, not about
   the room; the first real failure is the moment the truth arrives and it changes behaviour immediately, not
   eighty windows later.

7. **A paid call that fails still costs.** Spend is reported whether or not the work succeeded, and a failed paid
   attempt is named as spend in the writer's account of the run. ([ch.20](20-on-device-first-and-the-writers-key.md)
   holds the key; this chapter holds the receipt.)

8. **No call without a declaration.** A service is callable only if it has bound (above); the register of what
   Reframe currently calls is GENERATED from those declarations and never hand-maintained. A hand-kept list of
   live infrastructure is stale on the day it is written — measured: the first draft of this chapter omitted
   Ulysses-as-a-Service, which has its own host, its own override and its own in-app fallback.

9. **A service outcome is persisted with the work it belongs to.** What reached the writer and what is in the
   store agree, so a reading can be asked later which lane answered and what it cost
   ([ch.37](37-copilot-capability-governance.md): claim only what the store can prove).

## Honesty (non-goals)

- **This is not a dashboard.** The writer must never have to watch a panel to know whether her work is going well.
  Reporting is *situated and event-driven*: it appears where the affected work is, when something happens, and is
  otherwise absent.
- **This is not a retry engine.** Saying what failed is not repairing it, and rule 5 forbids dressing a retry up
  as a solution when the service is simply down.
- **This is not the citation browser.** Rendering a cited page in WebKit so the writer can *check a quotation* is
  an evidence feature governed by [ch.40](40-a-citation-is-a-promise-someone-can-check.md). It shares an idiom
  with this chapter and solves a different problem: a spawned CLI failing over MCP has no page to render. Treating
  the resemblance as the mechanism is precisely the error this chapter exists to stop. That surface is governed by
  ch.40 §Showing the source and is **not implemented**; its capability identity stays declared unavailable
  ([ch.37](37-copilot-capability-governance.md)) until it satisfies those rules.

## Acceptance

A drive with a service deliberately unavailable, on the surface, per [ch.08](08-validation-and-acceptance.md):

1. With the paid lane's transport down, the writer is told **that lane is unreachable** — named, in the Copilot,
   with the actions that exist. Verified by reading the accessibility tree, not the log.
2. The reading window **does not narrow** and atom text **is not compacted** in response to that failure.
3. The run's record in FountainStore names the service, the lane, the outcome, and any spend.
4. With the same lane healthy, the identical drive reads without any of the above appearing.
5. The maintainer's log still carries the underlying error, unchanged: this chapter adds a report, it does not
   remove telemetry.

## Governing sentence

Every call Reframe makes has a name, a lane, a cost and an outcome, and all four are known where the call is made;
the writer is told what happened to *her work* in her own words, and nothing about a service is ever re-inferred
downstream from its symptoms.
