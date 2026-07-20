# Extended Grounding Contract

> Chapter summary: This chapter specifies the writer-confirmed Grounding Profile that replaces index-mediated intent, including its fields, identity, lifecycle, direct Storify use, and failure behavior.

Grounding is not preliminary configuration. In the target Reframe architecture it is the durable agreement between the writer and every downstream reasoning stage. Removing indexing makes that agreement more direct and therefore more important: Storify must not infer an adaptation policy from generic defaults, old semantic memory, or the source alone.

## The Grounding Profile

The application should persist one current Grounding Profile per manuscript session, with versioned history where existing baseline conventions require it. The exact FountainStore identifier should follow the repository's session-scoped naming conventions; the recommended current-profile identity is `grounding:session:<sessionId>:profile`, accompanied by immutable historical versions or an existing store-native version ledger.

The profile contains the following semantic fields.

**Author baseline** describes the authorial engine: the commitments, tensions, formal principles, and modernization posture the writer wants preserved. It is not a biography and not a source synopsis.

**Reader lens** describes the intended act of attention: whose experience matters, what forms of dramatic change should remain visible, and which interpretive habits the system should resist.

**Source language** identifies the language or languages that govern source interpretation. It must not be inferred from a few tokens when the writer has confirmed it explicitly.

**Destination medium** names the intended output form and its relevant constraints. It may affect structural recommendations, but it does not authorize rewriting during Storify.

**Structural intent** directly tells Storify what kind of structure the writer is seeking. This is the field that index-mediated architecture lacked. It may emphasize causal turns, reversals, distributed attention, episodic rhythm, or another writer-stated principle.

**Preservation duties** state what must remain legible or intact through structural transformation. These duties are interpreted as policy, never as claims that the source already satisfies them.

**Transformation boundaries** state what the system may transform and what it must not normalize, resolve, redeem, simplify, or integrate.

**Current source relationship** records the source document identity for which the profile was confirmed. A profile may be reusable across a source revision only when the writer's declared policy remains current and the application can prove that no policy-bearing source relationship changed.

**Confirmation and provenance** record who confirmed the profile, when it was confirmed, how it was produced or edited, and the operation/schema version that defines its meaning.

## Grounding identity

The Grounding identity is a content identity over the canonical semantic representation of all confirmed fields that influence downstream work. Display labels, timestamps, UI expansion state, and telemetry do not change it. Author baseline, reader lens, source language, destination medium, structural intent, preservation duties, transformation boundaries, and relevant schema version do.

No numeric fit decision may determine the identity. Two profiles are equivalent because their canonical policy content is equivalent, not because their byte or token counts fit the same envelope.

Each Storify window stores the Grounding identity it used. A change creates a new interpretation lineage. Existing atom extraction may be reused when the source is unchanged because atomization is source-derived; kept/noise decisions, beat ordering, summaries, synopsis, and arcs become stale because their policy changed.

## Direct Storify context

Storify receives a phase-specific Grounding context, not the old semantic index. The safest implementation is to make the new structural fields explicit and writer-inspectable so Storify can consume their meaning without hidden summarization. If a provider cannot safely receive every relevant field, a reasoning mediation step may form a persisted, inspectable Storify projection. That projection must preserve semantic obligations, cite its parent Grounding identity, and fail visibly when it cannot decide what is relevant. It may not truncate by position, clamp by token count, or use phrase matching as the authority for meaning.

A Storify semantic request therefore contains the selected source atoms, the confirmed Grounding policy relevant to structural reading, the active Storify preset, and any current steering instruction. The prompt explicitly states that Grounding governs salience while source atoms govern fact.

## Confirmation lifecycle

A fresh manuscript begins with Grounding incomplete. The writer may import and inspect the source, but Source Auto does not run until required fields are confirmed. Confirmation is explicit and persisted. Opening a panel, saving a draft field, or accepting a default visually is not confirmation unless the corresponding store artifact says so.

Editing a confirmed field creates a draft Grounding state and makes downstream Storify interpretation stale. The application may continue to display older results with clear lineage, but it must not label them current. Reconfirmation produces a new Grounding identity and enables a new or selectively reusable Storify run.

If the writer chooses a shipped preset, the profile stores the resolved semantic content or a stable preset identity plus the exact version required to reconstruct it. A mutable preset name alone is insufficient provenance.

## Failure behavior

Missing Grounding produces one clear next action: complete and confirm Grounding. It does not launch indexing, fabricate a default Guide, or queue Source Auto invisibly.

Invalid or internally contradictory Grounding is mediated as a clarification, not settled with a deterministic phrase rule. Provider inability to use the Grounding context is reported as a transport or availability failure. Grounding never silently disappears from the request merely so a model call can proceed.

## Human-readable projection

Reframe may present the Grounding Profile as a concise “Working Contract” or retain a “Manuscript Guide” label for a combined report. Such a view is a projection, not a separately generated authority. After Storify completes, the projection may add source-grounded structural findings, clearly distinguishing writer-declared policy from model-derived story structure. Regenerating the view must be deterministic from stored artifacts and must not reread the source.

## Authoring model

The persistence, identity, and invalidation semantics above are authoritative. The *authoring model* — how the writer arrives at a confirmed profile — is refined in [Grounding as a given](11-grounding-as-a-given.md): a canonical manifesto ships as the default given, is auto-applied and auto-confirmed on import, and is edited centrally as prose (never dissected into fields by a model, which would violate the deterministic, no-model, no-overreach rule of this contract). That chapter changes only how the profile is authored; every invariant here — confirmed Grounding governs Storify, artifacts carry identity, edits mark downstream stale — is preserved.
