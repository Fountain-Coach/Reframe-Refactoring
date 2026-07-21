# Grounding as a Given — the Canonical Manifesto and Conversational Authoring

> Chapter summary: This chapter refines the Grounding-first authoring model. Grounding stops being a per-manuscript form the writer must fill before working. A canonical, app-level manifesto ships as the default given, is auto-applied and auto-confirmed on import, and is edited centrally as prose. The underlying contract — confirmed Grounding governs Storify, deterministically, with no model call and no interpretive overreach — is preserved. This chapter defines the required behaviour and constraints; it does not prescribe unverified types, files, or call paths.

## Purpose

The Grounding-first refactor (chapters 04–08) made confirmed Grounding the direct downstream policy contract. It did not settle *how the writer authors it*. In practice, the authoring surface became a long, field-by-field form — author baseline, reader lens, reading quality, structural intent, preservation duties, transformation boundaries — presented up front, in the app's own vocabulary, gated by an explicit confirmation step.

That is the wrong instrument for the task. Grounding asks the writer to legislate, in the abstract and before touching the work, how their source should be read — a manifesto, a reader model, and a preservation ethic. Demanded as a form, at the threshold, alone, it is a high cognitive burden that reads like an assessment questionnaire and stands as a wall before the actual writing.

This chapter changes the *authoring model* to remove that wall, while preserving every authority invariant of the Grounding contract.

## The decision

1. **A canonical manifesto is the default given.** Reframe ships one authoritative reading stance — the interpretive and ethical position the application already embodies (the "Non-Integrational" family: preserve irreducible source difference; do not manufacture continuity, causality, or thematic unity the source does not establish; keep uncertainty visible; ground every claim in evidence; avoid deterministic identity claims, redemptive closure, and interpretive overreach). This stance is not per-manuscript. It is Reframe's philosophy, shipped as a default.

2. **Grounding is auto-applied and auto-confirmed on import.** A newly imported or opened manuscript inherits the manifesto as its confirmed Grounding, with source language auto-detected and destination medium defaulting to screenplay. The writer is not stopped at a form.

3. **Import goes straight to Story (Storify).** With Grounding pre-supplied, the next surface is the structural read, not a gate.

4. **Grounding is not a per-manuscript surface.** The writer does not move *through* Grounding at all: the reading stance is the settled given, held behind every stage, with no per-manuscript form or tab to visit. The writer’s navigation is Story-first (Story · Score); the stance is read and changed centrally in Preferences, or conversationally with the Copilot. (This supersedes an earlier formulation that kept a read-only Grounding tab as "a quiet statement of the given.")

5. **The manifesto is edited centrally, as prose.** The whole stance surfaces as one editable flow-text in the application's Preferences (the natural home, where grounding defaults already resurface). It is the single global default every manuscript inherits.

6. **Conversational authoring is the front door for those who want to shape it.** A writer who wants a different stance — or wants to shape what the read should *seek* for a particular piece — is helped by the Copilot, not by re-filling a form. This is the conversational grounding of the Copilot Implementation Extension (chapter 10): the Copilot proposes and helps refine; the writer reacts and confirms.

## The prose principle — no model dissection

The manifesto is authored and edited as prose, and it is **never dissected into discrete fields by a model.**

The reasoning is a direct consequence of the Grounding-first contract. Grounding is deterministic, writer-confirmed, and provider-free ("a deterministic projection — no model call, never rereads the source"). Using a language model to parse a free-text manifesto into structured fields would make the model *interpret the writer's stance* — the precise interpretive overreach the manifesto itself forbids — and would add cost and non-determinism to the one artifact that must be rock-solid.

The discrete fields were a **form artifact, not a downstream requirement.** The structural reader can receive the manifesto as a single stance block; artifact identity and staleness can be computed over the prose; completeness reduces to "the manifesto is non-empty." Therefore:

- Prefer feeding the manifesto **as prose** into the structural read, dropping the field split, keeping only the genuinely separate, per-manuscript facts (source language, destination medium) as distinct values.
- If preserving the current structural-read prompt roles is required, present the manifesto as **one lightly-sectioned document** whose sections map deterministically to the existing fields — still no model, still one flowing manifesto to the writer.

Either way, no model call is introduced into the grounding path.

## What remains per-manuscript

Three things are genuinely not part of the shared manifesto:

- **Source language** — auto-detected from the imported source.
- **Destination medium** — defaults to screenplay (Reframe's purpose); changeable.
- **Structural intent** — "what this reframe should seek" (causal turns, reversals, distributed attention, episodic rhythm). This is the single field that carries genuine *per-writer* intent. It is **defaulted to a sensible universal consistent with the manifesto and hidden by default.** The Copilot may raise it — as an *offer*, never a gate — when shaping it would materially change the read.

## Preserved invariants (non-goals)

This refinement does not weaken any Grounding-first authority rule:

- Confirmed Grounding still directly governs Storify; Storify Source Auto remains the sole structural reader.
- Grounding remains a persisted, identity-bearing artifact; changing the manifesto re-identifies it and marks dependent downstream artifacts stale, per the existing invalidation semantics (chapter 05).
- No model call is introduced into the grounding path.
- Canonical source text remains the factual authority; the manifesto shapes salience and permitted transformation only.
- Ordinary conversation is never silently promoted into confirmed Grounding (chapter 10, writer steering). Auto-confirming the *default manifesto* is an explicit product default the writer can inspect and change — not an inference from chat.

## Relationship to the other chapters

- **[Grounding contract](05-grounding-contract.md)** — this chapter refines its *authoring model* (default manifesto, auto-confirm, central prose editing) while preserving its persistence, identity, and invalidation semantics.
- **[Target architecture](04-target-architecture.md)** — the writer flow becomes import → Story, with Grounding as a pre-supplied given rather than a gate.
- **[Copilot implementation extension](10-copilot-implementation-extension.md)** — the conversational "ground it with me" front door and the offer-not-gate handling of structural intent are Copilot behaviours governed there.

## Acceptance

The refinement is accepted when:

1. Importing or opening a manuscript yields **confirmed Grounding from the canonical manifesto**, with source language auto-detected and medium defaulted, and the writer lands on **Story**, not a grounding form.
2. The **whole manifesto is editable as prose** in Preferences, as a single default that every manuscript inherits.
3. Editing the manifesto **re-identifies Grounding and marks dependent downstream artifacts stale**, per chapter 05.
4. **No model call** occurs anywhere in the grounding path — the manifesto is never dissected by a model.
5. **There is no per-manuscript Grounding tab.** Opening a manuscript lands the writer on Story; the reading stance is read and changed centrally in Preferences (the canonical manifesto, as prose) or conversationally with the Copilot — never as a per-manuscript form.
6. Structural intent is defaulted and hidden; when the Copilot surfaces it, it does so as an **offer**, and confirmed Grounding is never created implicitly from ordinary conversation.
