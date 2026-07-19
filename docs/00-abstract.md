# Abstract

> Chapter summary: This abstract states the architectural decision, its motivation, the resulting pipeline, and the conditions under which the refactor may be considered complete.

Reframe accumulated two source-reading systems. Semantic indexing read passages into durable semantic memory and eventually became the hidden engine behind the Manuscript Guide. Storify Source Auto then read source atoms again to decide what mattered and how the story should be ordered. Later development reduced that duplication by allowing Storify to derive beats from indexed turns, but the optimization depended on an index whose on-device results were not consistently strong enough to deserve structural authority. At the same time, Storify acquired a complete independent source-reading path, chapter-aware paging, provider recovery, durable window artifacts, synopsis synthesis, and an immutable-source operating model.

The refactor resolves this history by removing semantic indexing completely from Reframe's final production architecture. It does not replace indexing with an ungrounded generic pass. Instead, it extends Grounding into a persisted, writer-confirmed downstream contract and sends that contract directly into Storify. The author baseline states what must be preserved or transformed; the reader lens states what deserves attention; source language and destination medium establish interpretive conditions; explicit structural intent tells Storify how the writer wants the material organized. Source atoms remain factual authority. Grounding influences salience and transformation policy but never licenses invention.

The target pipeline is therefore:

```text
canonical source
      ↓
confirmed Grounding Profile
      ↓
Storify Source Auto
      ↓
Storify windows, beats, uncertainty, synopsis, and arcs
      ↓
Cut Script
      ↓
Continuity
      ↓
compose, publish, and optional training
```

The Manuscript Guide ceases to be an independently generated prerequisite. If a guide-like human document remains desirable, it becomes a read-only projection of confirmed Grounding and completed Storify synthesis; producing it must never cause another model to reread the source. Indexed passages, reading states, index repair debt, learned index split memory, index-specific performance controls, and `semantic_index_fresh` readiness gates are removed after their replacements have passed end-to-end validation.

This is a replacement-first refactor. Grounding must reach every Storify semantic window before index inputs are disabled. Readiness and downstream consumers must use source, Grounding, Storify, Cut Script, and Continuity identities before index documents become archival. Only after those replacements are proven may implementation code and UI dedicated to indexing be deleted.

Completion is not defined by a smaller source tree. Completion means that a clean store containing no semantic-index documents can import a source, confirm Grounding, finish Storify Source Auto, produce a Cut Script, run Continuity, relaunch without readiness drift, and explain its state from FountainStore truth. No runtime, capability, prompt, status message, test, or generated reasoning artifact may still require semantic indexing or a published semantic object.
