# The Situated Copilot — One Copilot, Differently Placed

> Chapter summary: The Copilot is not a voice without a location. She is an object **placed in an arrangement**, and where she is placed governs what she may say, what she may offer, and what she may assume the writer can see. This chapter extends the perception contract of [chapter 10](10-copilot-implementation-extension.md) with the writer's **situation** — the active arrangement and what is wired into the conversation there — and binds the Copilot to the rule [chapter 14](14-the-beat-and-its-arrangements.md) already sets for every control on a surface. It defines required behaviour and constraints; it does not prescribe unverified types or call paths.

## Purpose

The Copilot was written as a voice from nowhere. Her opening line is a single constant, seeded into the chat transcript in the view-model's initializer — before a manuscript is open, before a surface exists, before there is anything to be situated in. It reads: *"Open the manuscript and ask in plain language."*

Chapter 14 then placed her on the Cut Script canvas as a node, wired beside the renderer node whose output she is meant to reason about. So the writer now meets her on the board, with the manuscript already open and its chapters listed in the rail beside her, and she opens by asking them to open the manuscript. She proposes an action already taken, on a surface she cannot name, about objects she has not been told are there.

This is not a copy defect. Chapter 10 gave the Copilot a perception contract of some seventeen facts — project identity, source availability, Grounding status, Storify and Cut Script and Continuity readiness, blocked operations, cost — and every one of them is a fact about **persisted workspace state**. Not one is a fact about *where the writer is standing*. The contract describes what the workspace holds; it never describes what the writer is looking at. A Copilot built exactly to that contract is necessarily blind in this way, and the blindness surfaces the moment she is given a place to stand.

Chapter 14 already forbids the consequence without naming her: *a control offered where its object is not visible is a category error, not a convenience*. The Copilot is now such a control. The doctrine exists; the perception needed to honour it does not.

## The principle — one Copilot, differently placed

The Copilot does not change identity when the writer changes surface. She is one Copilot, with one authority, one set of operations, and one relationship to the Grounding contract. What changes is her **placement** — the arrangement that hosts her, and the objects that arrangement has wired into the conversation:

| Placement | Host | Wired context | She speaks about |
| --- | --- | --- | --- |
| **Conversation pane** | the manuscript shell | the manuscript and its confirmed Grounding | the work as a whole |
| **Cut Script canvas** | a node on the board | the beats wired to her node | the cut being assembled |
| **Pre-manuscript launcher** | the library | nothing yet chosen | what could be opened |

This is the same doctrine chapter 14 states for the beat, applied to the agent: identity is invariant, arrangement is not. A Copilot who cannot tell these placements apart is not a general assistant — she is a mislocated one.

## The decision

1. **The Copilot perceives her situation.** The perception contract of chapter 10 is extended: alongside the facts of persisted workspace state, the Copilot must be able to determine the **active arrangement**, the objects that arrangement has wired into the conversation, and the current selection within it. Situation joins the contract as a first-class group; it is not an optional enrichment.
2. **Situation is perceived from application state, never inferred from the transcript.** Chapter 10's rule holds without exception here: the representation is assembled from authoritative application state and must not be reconstructed from prior assistant messages. Where she believes she is must be where she is.
3. **Her opening words are a function of her situation, not a constant.** No greeting may be seeded before a surface exists. An opening line that cannot vary with placement is a defect regardless of how well it reads, because it will eventually be read in a place it does not fit.
4. **She never proposes an action the writer has already taken.** Suggesting that an open manuscript be opened is the plainest form of the category error; the general rule is that a proposal must be checked against the state it presumes.
5. **She may not offer what her arrangement does not show.** Chapter 14's rule for controls binds the Copilot exactly as it binds a button: an operation whose object is not visible in the current arrangement may be *explained*, and it may be *reached* by naming where it lives, but it may not be offered as though it were at hand.
6. **On the canvas, the wiring is the context.** What is wired to her node is what the conversation is about — this is why arranging by instruction from a detached pane was removed rather than reimplemented. She must perceive the wired set, and she must distinguish an **unwired** board from an empty one.
7. **An empty situation is stated, not filled.** When nothing is wired, nothing selected, or no manuscript open, she says so plainly. She may not manufacture a scope to appear useful, and she may not present the absence of context as though it were context. This is chapter 11's prohibition on interpretive overreach and chapter 12's on foreshadowing content, applied to conversation.
8. **Situation is derived, never authoritative.** It is read from existing application and surface state. It does not become a stored artifact, it is never persisted as a fact about the work, and nothing downstream may treat it as evidence about the manuscript.
9. **Silence is situated too.** The Copilot opens silent and ready and wakes on demand; that decision stands. What this chapter requires is that when she does wake, her first words are the words of the place she wakes in.

## Honesty (non-goals)

- **Situated is not a persona per surface.** She does not acquire a different voice, a different name, or a different set of permissions on the board. One Copilot, one authority, one contract — only the placement differs.
- **Knowing where she is is not licence to act there.** Perception is not permission. The confirmation, cost, and blocking rules of chapter 10 are untouched by this chapter; a better-situated Copilot is not a more autonomous one.
- **The unwired board is not an invitation.** An empty wiring is a true state to report, not a gap for the Copilot to fill with a plausible selection.
- **Situation is not retrieval.** Knowing that three beats are wired is not knowing what they say. Evidence still comes from the source and the persisted structure, by the retrieval paths chapter 10 already governs.
- **This chapter adds no new surface.** It describes what the Copilot must perceive of the surfaces that already exist; it does not authorise a new one.

## Relationship to other chapters

- **[Copilot implementation extension](10-copilot-implementation-extension.md)** — this chapter extends that one's perception contract with the situation group, and inherits its rules on retrieval, mediation, confirmation, cost, and acceptance unchanged. Chapter 10 remains the authority on what the Copilot *may do*; this chapter governs what she must know about *where she is doing it*.
- **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** — supplies both the placement and the constraint: its canvas is a patch graph in which the Copilot is a node acting on wired beats, and its rule that a surface's controls belong to that surface is what this chapter makes perceivable.
- **[Animating truth](12-animating-truth.md)** — the same ethic in a different medium: state what is true now, mark what is not yet known as honestly unknown, and never sign an absence as though it were content.
- **[Grounding as a given](11-grounding-as-a-given.md)** — the Grounding she speaks from is settled and central; situation never overrides it, and a placement may not imply a different reading stance.
- **App-flow record (`reframe-app-flow-governance.md`)** — the Copilot's presence on each surface is part of that flow and must be narrated there as one agent in several placements.

## Acceptance

The doctrine is met when:

1. **The Copilot's context contains her arrangement,** named explicitly, assembled from application state rather than from the conversation.
2. **The context names what that arrangement has wired into the conversation,** including the honest empty case.
3. **No opening line is seeded before a surface exists,** and no constant greeting survives in the transcript path.
4. **Her opening differs demonstrably between placements** — the pane, the canvas, and the launcher — without becoming a different voice in each.
5. **She never proposes opening a manuscript that is open,** nor any other action whose state she can already perceive as done.
6. **She declines to offer operations whose objects are not visible in the current arrangement,** while remaining able to explain them and say where they live.
7. **An unwired canvas is reported as unwired,** and no scope is manufactured to fill it.
8. **Situation appears nowhere in persisted state** and is never cited as evidence about the manuscript.
9. **The behavioural acceptance scenarios of chapter 10 still pass unchanged,** demonstrating that situation was added to perception without altering authority.
