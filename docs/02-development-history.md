# Development History and Retained Lessons

> Chapter summary: This chapter reconstructs how Reframe arrived at its current overlapping reading systems and records which lessons survive even though indexing itself is being retired.

Reframe's index was not an accidental subsystem. It arose from a legitimate need: imported source text needed line-addressable interpretation that could survive model calls, relaunches, and downstream use. Early semantic-memory work established chunk tracking, resumable progress, grounded claims, drift and pattern artifacts, provider recovery, and FountainStore persistence. Those decisions corrected real failures—unbounded reads, invented relationships, silently missing coverage, and transient UI state masquerading as knowledge.

By early July 2026, Grounding had become a visible product stage and the index had become the source-reading engine behind the Manuscript Guide. Commits such as `e88238fe` and `bd973c35` moved Grounding to the front door and repaired its confirmation flow. `cf22bf96` stopped an imported manuscript from silently launching expensive indexing, establishing an important autonomy rule: source availability does not imply permission to infer. Chapter and episode work (`f245e9c5`, `4fa88ee9`, `d5e97f40`, and `13339d07`) then made the open chapter the practical unit of reading for long works.

The Reading Laboratory phase deepened the index rather than merely enlarging it. Work on source fidelity, evidence-linked observations, uncertainty, repair queues, quality accounting, checkpoints, and honest provider attribution made the index more auditable. The July 17–18 Apple performance program measured where time was actually spent, rejected several superficially attractive schema and fan-out experiments, and eventually learned exact-source context and safety failures. That work demonstrated disciplined empirical optimization, but it also exposed the remaining floor: on-device indexing still required a serial sequence of successful generations, while the measured output could remain shallow relative to the structural decision Storify needed to make.

Storify evolved in parallel. It began as a second semantic pass over source or draft atoms, with window history and resume tokens. It gained source-aware atom extraction, chapter seams, persistent machine-room state, second-pass synopsis and arc synthesis, crash recovery, provider fallback, and an increasingly explicit source-authoritative prompt. The pivotal change is recorded in `cc87a37f`: beats began to come from the reading rather than from a separately privileged Guide. That move demoted the Manuscript Guide and exposed the duplicate economy directly. When a strong indexed turn existed, Storify could avoid another model call; when it did not, Storify already possessed a complete independent reading path.

The next historical turn matters just as much. Current Source Auto orchestration explicitly says that it always proceeds and treats readiness as status rather than a hidden queue. The active auto loop also states that the source is immutable and persists analysis into Storify-owned documents rather than splicing analysis into screenplay text. These behaviors are newer than several app and repository documents that still describe an index-first blocking conveyor or source boneyard materialization. The contradiction is historical residue, not a choice to preserve both truths.

On 2026-07-19 the architectural decision changed. A comparatively weak index is not a sound authority for structural segmentation. If it contains no usable turn, Storify rereads the source and the application pays twice. If it contains a plausible but under-supported turn, the optimization can suppress the stronger independent reading. The proper simplification is not to make the index cheaper indefinitely. It is to let the writer's confirmed Grounding govern Storify directly and to make Storify the only structural source reader.

## Lessons that survive indexing

The index may leave, but its hard-won principles remain binding.

Source evidence must remain line-addressable. Generated structure must cite real atoms and line spans, and returned atom identifiers must be validated against the request. Ambiguity is a result; transport failure is a breakdown. The application must not fabricate beats to hide a failed read. Provider outcomes, retries, persistence, budgets, chunk or window progress, and resume state remain observable telemetry rather than invisible control flow.

FountainStore remains truth. A successful provider response is not a product until its validated artifact and identity land in the store. Relaunch must reconstruct readiness from persisted state rather than flags, transcript prose, or the fact that a view once rendered.

Reasoning remains responsible for semantic relevance. The refactor must not replace index chunking with numeric prompt-content selection, silent grounding compression, phrase heuristics, or positional truncation. Physical provider limits are transport constraints. If a Grounding Profile cannot be represented safely for a phase, the application must retrieve a more targeted, semantically explicit field or ask the writer; it may not silently decide that the tail of the profile matters less.

Finally, user authority remains explicit. Importing a source does not authorize a model run. Confirming Grounding authorizes its use as policy, not a rewrite. Storify may propose structure, Cut Script may contain chosen authored output, and Continuity may identify risk; none of them silently overwrite the canonical source.

## Superseded assumptions

The following statements belong to older architecture and must not guide new implementation:

- A full semantic index is a prerequisite for meaningful Storify segmentation.
- The Manuscript Guide is an independently generated canonical object that all downstream stages must await.
- Indexed coverage is equivalent to structural reading quality.
- Source Auto should materialize generated analysis into the canonical source document.
- `semantic_index_fresh` is a valid readiness gate for Storify, Cut Script, Continuity, compose, or publish.
- A low-quality index is harmless because Storify can always fall back; an accepted but weak index-derived turn can itself prevent that fallback.

Historical files may continue to explain why these ideas once existed. They must be cited as history, never used as operational authority after the corresponding migration phase lands.
