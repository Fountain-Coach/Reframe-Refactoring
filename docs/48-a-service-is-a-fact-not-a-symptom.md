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

## The register — what Reframe calls

Every service Reframe reaches is named here. A call to a service that is not in this register is a defect.

### External — over the network, and able to fail

| service | reached by | used for | lane |
|---|---|---|---|
| ChatGPT via **Codex CLI** | spawned process → `chatgpt.com/backend-api` (MCP) | reading, planning | paid |
| **OpenAI Responses** | `api.openai.com` | reading, planning | paid |
| **DraCor** | `dracor.org` | play import | free |
| **Wikipedia**, **arXiv**, **DOI** | `en.wikipedia.org`, `arxiv.org`, `doi.org` | reference and citation lanes | free |
| **Ovid-as-a-Service** | `api.ovidasaservice.com` | Metamorphoses fallback | free |
| **the open web** | `WebPageReader` (WebKit) | citation evidence | free |

### Internal — local, and *not* therefore infallible

| service | reached by | used for |
|---|---|---|
| **Apple Foundation Models** | on-device, ANE over XPC | the first lane, for every role |
| **the in-app Corpus API** | `127.0.0.1:<ephemeral>` — `/v1/episode/{n}`, `/v1/book/{n}`, `/v1/myths`, `/v1/book/{n}/myth/{m}` | the works Reframe opens with |
| **FountainStore** | local disk | the truth ([ch.08](08-validation-and-acceptance.md)) |
| **OS Writing Tools** | AppKit | reframing a beat |
| **Facebook OAuth callback** | loopback listener | publishing |

"Internal" means *near*, not *reliable*. The in-app corpus API binds a socket and can fail to; the on-device model
can be unavailable, busy, or too small for the passage. Each is named here for the same reason as the rest.

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

8. **A service outcome is persisted with the work it belongs to.** What reached the writer and what is in the
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
  the resemblance as the mechanism is precisely the error this chapter exists to stop.

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
