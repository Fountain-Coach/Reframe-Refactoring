# Remote CodexKit — Reframe and Codex Meet as Governed MIDI2 Peer Instruments

## Status

Governance proposal.

This chapter extends the existing CodexKit, universal MIDI2 command-plane, FCIS-KIT instrument, cross-platform Reframe, iPad host, joining-machine, authentication, and asynchronous-lifecycle governance.

It does not replace those authorities.

It defines the missing remote peer relationship between them.

---

## Chapter Summary

Reframe on iPad SHALL communicate with a remote Codex execution environment through the existing governed MIDI2 instrument plane.

Reframe is a MIDI2 participant.

CodexKit exposes the Codex execution boundary as a governed MIDI2 instrument.

The two establish their peer relationship through MIDI-CI and communicate across the estate's RTP-MIDI2 transport.

The official Codex app-server remains the pinned execution backend behind CodexKit. Its native JSON-RPC protocol is an implementation-side protocol authority and does not become a second Reframe command plane.

The resulting architecture is:

```text
Human
  │
  ▼
Reframe on iPad
MIDI2 participant / governed host
  │
  │ MIDI-CI peer relationship
  │ typed MIDI2 operations + lifecycle
  │ over RTP-MIDI2
  ▼
CodexKit MIDI2 instrument
  │
  │ pinned native Codex app-server protocol
  ▼
Codex app-server
  │
  ▼
development environment
repository / git / Swift / Xcode / Linux /
EstatePublisher / MCP / other admitted capabilities
```

The network extends the existing MIDI2 capability plane.

It does not create a second remote-control architecture.

---

# 1. Governing Decision

Remote Codex operation SHALL be expressed as communication between governed MIDI2 peers.

Reframe SHALL NOT require:

```text
remote desktop
screen scraping
keyboard injection
generic SSH control
a private remote shell protocol
a second OpenAI API integration
a second capability router
```

merely because the Codex execution environment is located on another machine.

CodexKit already defines the governed boundary between Fountain Coach software and the pinned Codex app-server runtime.

This chapter extends that boundary across the existing remote MIDI2 fabric.

The canonical path is:

```text
Reframe intention
      │
      ▼
MIDI-CI-established CodexKit peer
      │
      ▼
typed MIDI2 Codex operation
      │
      ▼
CodexKit instrument lifecycle
      │
      ▼
pinned Codex app-server protocol
      │
      ▼
Codex runtime and development environment
      │
      ▼
typed MIDI2 lifecycle / result
      │
      ▼
Reframe projection + FountainStore evidence
```

---

# 2. Existing CodexKit Authority Remains Intact

Chapter 88 defines CodexKit as the governed Codex app-server boundary.

That authority remains unchanged.

CodexKit owns:

```text
runtime compatibility
process lifecycle
native app-server transport
protocol correlation
typed request decoding
typed event decoding
authentication routing
thread façade
turn façade
approval delivery
cancellation
shutdown
safe diagnostics
MIDI2 instrument boundary
```

The Codex app-server owns its provider-defined protocol and runtime behavior.

Reframe owns product meaning and human interaction.

Remote transport MUST NOT collapse those responsibilities.

Therefore:

```text
Codex app-server JSON-RPC
        ≠
Reframe remote protocol

CodexKit MIDI2 instrument
        =
governed Reframe-facing Codex boundary
```

Remote Codex is achieved by making the existing CodexKit instrument remotely addressable through the governed MIDI2 plane.

It is not achieved by exposing app-server JSON-RPC directly to arbitrary network clients.

---

# 3. Reframe on iPad Is a First-Class Reframe Host

Chapter 135 governs Reframe on iPad as a first-class creative and performance target.

That principle SHALL also apply to Codex interaction.

The iPad SHALL NOT be reduced to:

```text
a Mac remote control
a terminal emulator
a screen-sharing endpoint
a WebView around another machine's UI
```

Reframe on iPad owns its native human-facing Codex projection.

That projection MAY contain:

```text
thread navigation
conversation presentation
prompt composition
streaming response
tool activity
approval interaction
diff presentation
execution status
cancellation
resume
environment selection
```

The execution environment may be remote.

The Reframe experience remains local to the iPad.

---

# 4. MIDI-CI Establishes the Peer Relationship

Chapter 81 distinguishes MIDI-CI from the MIDI2 operation plane.

That distinction SHALL remain explicit.

MIDI-CI answers:

```text
Who are you?

What profiles and capabilities do you expose?

What operation vocabulary can we negotiate?

What properties describe this instrument?
```

Only after that peer relationship exists may Reframe invoke the CodexKit instrument.

The canonical sequence is:

```text
RTP-MIDI2 connectivity
      │
      ▼
MIDI-CI discovery
      │
      ▼
identity / profiles / Property Exchange
      │
      ▼
CodexKit capability established
      │
      ▼
authorization / admission
      │
      ▼
typed MIDI2 Codex operation
      │
      ▼
correlated lifecycle
      │
      ▼
terminal result
```

MIDI-CI discovery is not execution.

A successful peer handshake does not prove that a Codex turn succeeded.

A reachable host does not prove that CodexKit is admitted.

---

# 5. RTP-MIDI2 Is the Remote Transport

Where Fountain Coach's RTP-MIDI2 implementation connects the participating peers, it SHALL be the normal remote transport for this capability plane.

The architecture SHALL NOT introduce a redundant generic relay merely because the instruments are on separate machines.

The normal topology is:

```text
Reframe iPad
     │
     │
     │ RTP-MIDI2
     │
     ▼
CodexKit instrument
on admitted execution host
```

RTP-MIDI2 provides network transport.

MIDI-CI establishes the instrument relationship.

The MIDI2 IDL defines the operation and lifecycle contract.

CodexKit translates that governed contract into the pinned app-server protocol.

Each layer has one job.

---

# 6. The Codex App Server Is an Execution Backend

The Codex app-server SHALL remain behind the CodexKit instrument boundary.

Its native protocol is external and revisioned.

Its schema, methods, events, account behavior, thread semantics, approvals, and runtime compatibility MUST be pinned from the actual supported upstream implementation as required by Chapter 88.

The internal path is:

```text
MIDI2 operation
      │
      ▼
CodexKit
      │
      ▼
typed Swift façade
      │
      ▼
app-server JSON-RPC
      │
      ▼
Codex app-server
```

The native app-server protocol MUST NOT silently become a parallel Fountain Coach public protocol.

A future change in the app-server protocol SHALL require CodexKit compatibility work.

It SHALL NOT require Reframe clients to abandon the MIDI2 capability contract.

---

# 7. Remote Codex Is a Capability, Not a Machine Session

The remotely addressable object is the Codex capability exposed by CodexKit.

The user does not select a computer merely because the computer exists.

The user selects an eligible capability.

For example:

```text
CODEXKIT / UBUNTU DEVELOPMENT

codex.thread
codex.turn
codex.stream
codex.approval
codex.cancel
codex.resume

host capabilities:
swift.linux
git
estate.staging
midi2
```

or:

```text
CODEXKIT / MAC DEVELOPMENT

codex.thread
codex.turn
codex.stream
codex.approval
codex.cancel
codex.resume

host capabilities:
swift
xcode
ios.build
signing
git
```

The physical machine provides the execution environment.

CodexKit exposes the governed Codex capability.

These identities SHALL remain distinguishable.

---

# 8. Relationship to Joining-Machine Governance

Chapter 141 governs machine admission.

That chapter SHALL continue to determine whether a machine may participate in the estate.

A machine being reachable through RTP-MIDI2 is insufficient.

A machine being visible through Bonjour is insufficient.

A Codex process running is insufficient.

A CodexKit instance responds only within an execution environment whose required machine admission and capability prerequisites have been satisfied.

The conceptual hierarchy is:

```text
machine admitted
      │
      ▼
runtime prerequisites available
      │
      ▼
CodexKit instrument admitted
      │
      ▼
MIDI-CI relationship established
      │
      ▼
Codex operation authorized
      │
      ▼
execution
```

Machine admission and instrument admission are related but not interchangeable claims.

---

# 9. Relationship to FCIS-KIT

Chapter 91 establishes the FCIS-KIT instrument plane.

Chapter 93 establishes the governed instrument-creation and promotion path.

Remote CodexKit SHALL participate in that existing model.

Its instrument declaration SHALL identify at least:

```text
stable instrument identity
version
implementation provenance
supported MIDI2 operations
supported MIDI2 events
MIDI-CI profile/property declarations
remote execution characteristics
authorization requirements
account requirements
thread lifecycle
turn lifecycle
approval lifecycle
cancellation semantics
disconnect semantics
resume semantics
terminal predicates
timing claims
evidence authorities
Codex runtime compatibility
FCIS-KIT contract version
admission state
```

The fact that CodexKit builds SHALL NOT constitute admission.

The fact that app-server responds SHALL NOT constitute admission.

The fact that one remote turn works SHALL NOT constitute release.

The existing evidence ladder remains authoritative.

---

# 10. Codex Session Operations

The MIDI2 IDL SHALL define the bounded Codex operations required by the Reframe-facing instrument contract.

The vocabulary MAY evolve, but the semantic boundary SHOULD include equivalents of:

```text
codex.account.status

codex.thread.list
codex.thread.create
codex.thread.resume
codex.thread.inspect

codex.turn.submit
codex.turn.cancel

codex.approval.respond

codex.session.status
codex.session.resume
```

Streaming responses, tool activity, progress, approvals, cancellation and terminal completion SHALL be represented through the standard correlated lifecycle/event model rather than through a private transcript socket.

The exact operation names are an IDL decision.

This chapter establishes their required semantic roles.

---

# 11. One Correlation Identity Across the Boundary

A remote Codex operation SHALL preserve correlation from Reframe through MIDI2, CodexKit and the app-server boundary.

The implementation SHALL be able to associate, where available:

```text
instrument identity
operation identity
correlation identity
Reframe work/project identity
Codex account state
Codex thread identity
Codex turn identity
host environment identity
terminal result identity
```

The upstream app-server's own identifiers MAY participate in this correlation.

They SHALL NOT replace the Fountain Coach operation identity.

This permits the system to answer separately:

```text
Which Reframe operation was requested?

Which Codex thread handled it?

Which turn executed?

Where did it execute?

What terminal result was emitted?

What durable evidence exists?
```

---

# 12. Streaming Is MIDI2 Lifecycle, Not Authority

Codex output may arrive incrementally.

Incremental output SHALL be treated as lifecycle information.

A partial stream is not a terminal result.

A dropped stream is not deletion.

A missing client connection is not cancellation.

The operation remains governed by the asynchronous completion rules of Chapter 104.

Therefore:

```text
text delta
tool progress
command output
diff progress
approval request
heartbeat
```

are observable event states.

Completion requires a valid terminal event and the applicable durable evidence.

---

# 13. Disconnect and Resume Are Normal States

Remote execution SHALL assume that an iPad can:

```text
sleep
change network
leave WLAN
lose connectivity
terminate the client process
restart Reframe
```

without implying that the Codex turn disappeared.

A Remote CodexKit execution MUST distinguish:

```text
client disconnected
transport disconnected
Codex runtime disconnected
turn cancelled
turn failed
turn completed
```

These are different states.

Where the upstream Codex runtime supports resumable threads or turns, CodexKit SHALL bind those identities into its governed lifecycle.

Where transport replay is required, the MIDI2 operation contract SHALL define the correlation and replay behavior required to reconstruct the observable state.

Client-local persistence SHALL NOT be the only authority for a recoverable Codex session.

---

# 14. Reframe Local Storage Is a Projection Cache

Reframe MAY maintain SQLite, SwiftData, or another native local store for:

```text
cached thread metadata
rendered transcript fragments
draft prompts
navigation state
environment preferences
last-observed sequence
```

That store SHALL be treated as a client projection/cache.

Loss of the cache MUST NOT automatically mean loss of:

```text
Codex thread identity
active execution
durable operation state
governed receipts
```

Recoverable remote state SHALL be reconstructable from the authorities that actually own it.

This is a deliberate reliability boundary.

---

# 15. Approval Remains Human-Visible

Codex approval requests SHALL be projected as typed lifecycle events through the CodexKit instrument.

Reframe MAY render those requests natively on iPad.

An approval request SHOULD expose sufficient context for meaningful human consent, including where available:

```text
requested operation
execution environment
affected repository
affected resource
scope
consequence
```

The Reframe user may approve or reject.

Loss of network connectivity SHALL NOT constitute approval.

Silence SHALL NOT constitute approval.

A stale approval SHALL fail explicitly.

---

# 16. Authentication Remains a Separate Instrument Boundary

Chapter 89 governs the Codex authentication surface.

That separation SHALL continue remotely.

Reframe SHALL NOT:

```text
steal another application's cookies
inspect a private credential database
reinterpret a ChatGPT/Codex credential as an API key
require an API key merely because execution is remote
```

Codex authentication lifecycle remains exposed through the governed Codex authentication instrument.

Fountain authentication, where required for peer authorization, remains separately governed by FountainAuthKit.

The architecture therefore distinguishes:

```text
MIDI2 peer identity
machine identity
Fountain subject/client identity
Codex account identity
Codex runtime state
deployment authority
```

No one of these SHALL silently imply another.

---

# 17. FountainAuthKit Authorizes; MIDI2 Operates

Chapter 142 distinguishes authentication, authorization, operation and evidence.

Remote CodexKit SHALL preserve that separation.

FountainAuthKit MAY establish that a subject/client is authorized to invoke a CodexKit capability on a particular resource.

MIDI2 then carries the admitted operation.

CodexKit executes the capability.

FountainStore and named evidence authorities record the applicable results.

Conceptually:

```text
authenticated subject
       │
       ▼
bounded authorization
       │
       ▼
MIDI2 Codex operation
       │
       ▼
CodexKit execution
       │
       ▼
terminal result
       │
       ▼
durable evidence
```

MCP, Codex, Reframe, or a network peer SHALL NOT invent authorization merely because transport exists.

---

# 18. Host Tooling Remains Behind Codex

The development environment MAY contain:

```text
filesystem
git
Swift
Xcode
Linux toolchains
MCP servers
EstatePublisher
FountainStore tooling
MIDI2 tooling
Csound
build systems
test systems
```

Remote Reframe does not require direct generic control over those facilities.

Codex may use capabilities available in its governed execution environment according to their own authority boundaries.

Remote CodexKit projects the Codex session.

It does not turn Reframe into an unrestricted remote administrator.

---

# 19. Relationship to EstatePublisher

Chapter 140 makes EstatePublisher the governed IP-network topology mutator used by Codex for deployment outcomes.

Remote CodexKit SHALL NOT alter that authority.

For example:

```text
Human on iPad
      │
      ▼
Reframe
      │
      ▼
CodexKit MIDI2 instrument
      │
      ▼
Codex
      │
      ▼
EstatePublisher command selection
      │
      ▼
EstatePublisher
      │
      ▼
governed topology mutation
      │
      ▼
FountainStore proof
```

The fact that Codex was remotely operated from an iPad changes none of EstatePublisher's authority rules.

Remote CodexKit is not a second publisher.

It is not a second infrastructure mutator.

---

# 20. Relationship to MCP

MCP MAY be available inside the Codex execution environment.

MCP and Remote CodexKit are not equivalent.

MCP exposes tools and external capability integrations.

Remote CodexKit exposes the governed Codex execution/session capability itself.

The relationship MAY therefore be:

```text
Reframe
   │
   │ MIDI2
   ▼
CodexKit
   │
   ▼
Codex app-server
   │
   ├── repository
   ├── shell/tooling
   ├── MCP server
   ├── EstatePublisher
   └── other admitted tools
```

A reliable MCP server such as a machine-control service may be useful to Codex.

It SHALL NOT become the transport between Reframe and Codex merely because it can remotely manipulate the host.

---

# 21. Relationship to the Universal MIDI2 Command Plane

Chapter 81 establishes MIDI2 as the common command and event plane.

Remote CodexKit SHALL follow that rule rather than introduce a Codex-specific side channel.

The Reframe surface may be:

```text
Copilot
iPad conversation UI
scenario actor
another admitted peer
```

but all operational use of the CodexKit capability converges on the same typed instrument contract.

A Swift in-process optimization MAY exist when Reframe and CodexKit reside on the same machine.

It MUST preserve the same operation identity, lifecycle and terminal semantics as the remote MIDI2 path.

Local execution is an optimization.

It is not a second architecture.

---

# 22. Relationship to Semantic Execution Governance

Chapter 102 already places local model execution and Codex app-server execution behind a common MIDI2 semantic-execution boundary.

This chapter extends that principle across remote peers.

Remote placement SHALL NOT change:

```text
source-window isolation
session identity
turn identity
terminal truth
provenance
cancellation
evidence requirements
```

The transport may differ.

The semantic contract does not.

---

# 23. Relationship to Event-Time Governance

Chapter 104 governs event ordering, jitter observation, heartbeat, cancellation and asynchronous completion.

Remote CodexKit SHALL inherit that contract.

RTP-MIDI2 latency or temporary connectivity changes MAY be observed.

They SHALL NOT permit wall-clock guessing to replace typed completion.

A remote run remains active until:

```text
typed terminal completion
explicit cancellation
typed terminal failure
or applicable durable evidence failure
```

An arbitrary UI timeout SHALL NOT classify a healthy Codex operation as failed.

---

# 24. Relationship to the MIDI2 Monitor

The MIDI2 Monitor MAY project Remote CodexKit lifecycle facts.

It MAY show:

```text
peer discovery
CodexKit readiness
thread operation
turn start
stream activity
tool activity
approval waiting
resume
completion
failure
latency
jitter
```

The Monitor is a projection.

It does not become runtime authority.

The same typed facts MAY be projected through Teatro under the existing runtime-projection governance.

---

# 25. Cross-Platform Consequence

Chapter 108 defines Reframe as a Swift-native cross-platform runtime connected through the MIDI2 capability plane.

Remote CodexKit follows that constitution.

The CodexKit instrument MAY execute on:

```text
macOS
Linux
another supported Swift host
```

provided its implementation, runtime dependency, app-server compatibility and admission claims are actually established.

Reframe on iPad does not care about the physical location merely because the semantic instrument contract is stable.

Platform-specific host capabilities remain explicit properties of the execution environment.

---

# 26. No Client/Server Collapse

For network implementation purposes, one endpoint may listen while another connects.

That implementation fact SHALL NOT redefine the semantic architecture as:

```text
dumb client → authoritative server
```

The governed relationship remains peer-to-peer at the MIDI2 instrument plane.

Each participant has its own identity and declared capabilities.

Reframe is authoritative for the human/product interaction it owns.

CodexKit is authoritative for its declared instrument lifecycle.

The app-server owns its native runtime semantics.

The host owns its local resources.

Named Fountain authorities own their respective state and receipts.

---

# 27. Required Failure Vocabulary

Remote CodexKit SHALL distinguish at least:

```text
peer unavailable
MIDI-CI negotiation failed
instrument not admitted
operation unauthorized
CodexKit unavailable
Codex runtime unavailable
Codex authentication required
thread unavailable
turn refused
turn interrupted
approval required
approval rejected
client disconnected
RTP-MIDI2 disconnected
resume unavailable
protocol incompatible
terminal execution failure
durable-evidence failure
```

These states MUST NOT collapse into:

```text
chat lost
```

A presentation surface may simplify wording for the human.

The underlying state remains typed.

---

# 28. Compatibility and Versioning

Three versions may matter simultaneously:

```text
Remote CodexKit instrument contract
CodexKit implementation version
pinned Codex app-server protocol/runtime version
```

The implementation SHALL preserve those distinctions.

CodexKit SHALL reject upstream protocol versions it cannot safely interpret.

MIDI-CI capability exchange SHALL make the remotely usable CodexKit profile/version discoverable.

A Reframe client SHALL reject an incompatible instrument rather than guessing protocol behavior.

---

# 29. Security Boundary

Remote operation MUST NOT increase the execution authority of Codex merely because the human is using another device.

If the host Codex environment can:

```text
read repository A
build target B
request EstatePublisher operation C
```

Remote CodexKit may expose those Codex outcomes according to their existing policies.

It does not automatically acquire authority to:

```text
read every filesystem path
use every credential
publish every estate
mutate every host
```

Instrument admission, authorization, host policy, tool policy and human approval continue to apply.

---

# 30. Scenario-First Acceptance

The implementation SHALL be accepted through a governed scenario rather than through an informal demonstration.

The scenario SHOULD prove:

```text
Reframe iPad
      │
      │ MIDI-CI over RTP-MIDI2
      ▼
remote CodexKit instrument
      │
      ▼
Codex app-server
      │
      ▼
real development repository
```

with one uninterrupted correlation identity.

The scenario SHALL include disconnect and resume.

---

# 31. Definition of Done

The capability is implemented when the following complete scenario succeeds.

### Preconditions

- Reframe is running on an iPad.
- Reframe participates through the governed MIDI2 plane.
- A Mac or Linux development machine has been admitted under the machine governance contract.
- A compatible Codex runtime is installed and authenticated.
- CodexKit is built, admitted and available as a MIDI2 instrument.
- Reframe and CodexKit can establish their peer relationship through MIDI-CI over RTP-MIDI2.

### Execution

The writer:

1. opens Reframe on iPad;
2. discovers the remote CodexKit instrument;
3. sees its declared availability and execution environment;
4. selects or resumes a Codex thread;
5. submits a natural-language turn;
6. observes an admitted MIDI2 operation;
7. receives incremental Codex lifecycle/output;
8. observes tool activity when applicable;
9. receives an approval request when applicable;
10. approves or rejects it from Reframe;
11. receives a typed terminal result;
12. verifies the applicable durable state/evidence;
13. disconnects the iPad;
14. reconnects through RTP-MIDI2;
15. re-establishes the MIDI-CI peer relationship if required;
16. resumes the same governed Codex session/thread;
17. reconstructs the relevant visible state;
18. continues the work.

### The scenario MUST NOT depend on

```text
remote desktop
public SSH
screen coordinates
keyboard injection
private ChatGPT application state
ChatGPT's local SQLite history
a pasted OpenAI API key
a direct OpenAI API replacement for app-server
a private parallel WebSocket command API
a generic remote shell as the Codex client contract
```

---

# 32. Evidence Required

Acceptance SHALL bind the applicable evidence authorities.

At minimum:

```text
source revision
CodexKit build identity
Codex runtime/app-server version
FCIS-KIT contract version
MIDI-CI discovery evidence
RTP-MIDI2 transport evidence
typed MIDI2 operation trace
correlation identity
thread/turn binding
approval evidence where exercised
terminal MIDI2 lifecycle result
FountainStore receipt where applicable
Reframe-visible projection witness
disconnect/resume evidence
```

A successful screenshot alone does not prove the contract.

A Codex response alone does not prove the contract.

An RTP packet trace alone does not prove semantic completion.

Each witness establishes only its own claim.

---

# 33. Explicit Non-Goals

This chapter does not create:

```text
a new model provider
a new OpenAI API client
a generic remote-desktop product
a generic remote-shell product
a second EstatePublisher
a second FountainStore
a second authorization authority
a second MIDI2 command plane
a replacement for Codex's native app-server protocol
```

It connects existing governed systems.

---

# 34. Interlinks

This chapter SHALL be read with the following existing governance.

### Chapter 81 — The Universal MIDI2 Command Plane

Defines MIDI2 as the common command and lifecycle plane and distinguishes MIDI-CI peer establishment from operation execution.

This chapter applies that distinction to remote Codex interaction.

### Chapter 88 — CodexKit Is a Governed Codex App-Server Boundary

Defines the pinned app-server process/protocol boundary and CodexKit MIDI2 instrument.

This chapter extends that instrument across the remote MIDI2 fabric.

### Chapter 89 — The Codex Auth Instrument Is the Copilot Login Surface

Defines Codex authentication as its own governed lifecycle.

Remote Codex does not bypass or replace that authentication boundary.

### Chapter 91 — The FCIS-KIT Instrument Store Is the Capability Plane

Defines local and remote governed capabilities as reusable MIDI2 instruments.

CodexKit participates in that capability plane.

### Chapter 93 — Instrument Creation Is a Governed Promotion Path

Defines implementation, admission, testing, evidence and release requirements for a MIDI2 instrument.

Remote CodexKit obtains no special exemption.

### Chapter 102 — Semantic Inference Execution, Session, and Latency Governance

Defines local and Codex execution behind one MIDI2 semantic-execution seam.

This chapter extends that seam across RTP-MIDI2 peers.

### Chapter 104 — MIDI2 Event Time, Jitter, and Asynchronous Completion Governance

Defines event ordering, asynchronous completion, cancellation, heartbeat and timing truth.

Remote Codex streams obey that lifecycle.

### Chapter 108 — Reframe Is a Swift-Native Cross-Platform Runtime

Defines the MIDI2 capability plane as the cross-host boundary.

Remote CodexKit is one concrete application of that cross-host architecture.

### Chapter 135 — Reframe iPad as a Scenario-Driven Creative Host

Defines iPad as a first-class Reframe host rather than a Mac remote control.

This chapter gives that host a first-class remote Codex capability.

### Chapter 140 — EstatePublisher Is Codex's Governed IP-Network Topology Mutator

Defines Codex's relationship to infrastructure mutation.

Remote Codex does not acquire parallel deployment authority.

### Chapter 141 — Each Joining Machine Is a Governed MIDI2 Instrument

Defines machine admission before an execution host may participate in estate operations.

A remote CodexKit instrument runs within that admitted machine environment.

### Chapter 142 — FountainAuthKit

Separates identity, authorization, operation and evidence.

Remote CodexKit consumes that authority; it does not replace it.

---

# 35. Architectural Consequence

With this chapter, the Fountain Coach development topology becomes:

```text
                         HUMAN
                           │
                           ▼
                  REFRAME ON IPAD
                  first-class host
                           │
                           │
                    MIDI-CI / MIDI2
                     over RTP-MIDI2
                           │
                           ▼
                  CODEXKIT INSTRUMENT
                           │
                    typed Swift façade
                           │
                           ▼
                   CODEX APP-SERVER
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
             git         Swift        MCP/tools
              │                         │
              │                         ▼
              │                  EstatePublisher
              │                         │
              └────────────┬────────────┘
                           ▼
                 governed host state
```

The iPad does not remotely operate a desktop.

It participates in the same capability plane.

Codex is not remotely screen-controlled.

Its governed instrument boundary is invoked.

RTP-MIDI2 is not a decorative transport detail.

It is the remote continuation of the existing MIDI2 execution plane.

---

# 36. Governing Rules

1. **Remote Codex SHALL remain a MIDI2 capability, not a separate remote-control subsystem.**

2. **MIDI-CI SHALL establish the Reframe ↔ CodexKit peer relationship before remote operations are invoked.**

3. **RTP-MIDI2 SHALL carry the remote MIDI2 relationship where it is the admitted Fountain transport.**

4. **CodexKit SHALL remain the governed MIDI2 boundary around the pinned Codex app-server protocol.**

5. **The Codex app-server native protocol SHALL remain behind CodexKit and SHALL NOT become a second public Reframe operation plane.**

6. **Reframe on iPad SHALL remain a first-class Reframe host and SHALL NOT be reduced to remote desktop control.**

7. **Remote and local CodexKit execution SHALL expose the same governed operation semantics.**

8. **Streaming SHALL be lifecycle, not persistence authority.**

9. **Disconnect SHALL NOT imply cancellation, failure or deletion.**

10. **Resume SHALL preserve correlation with the actual Codex thread/turn where supported.**

11. **Client-local SQLite or SwiftData SHALL remain projection/cache state rather than the sole durable authority.**

12. **Machine admission, instrument admission, Codex authentication, Fountain authorization, execution and durable evidence SHALL remain separate claims.**

13. **Remote CodexKit SHALL NOT become an infrastructure, publication, credential or FountainStore authority.**

14. **MCP MAY serve Codex tools but SHALL NOT replace the Reframe ↔ CodexKit instrument contract.**

15. **Acceptance SHALL require a complete remote peer scenario including disconnect and resume.**

---

# Governing Sentence

> Reframe and CodexKit meet as governed MIDI2 peers: MIDI-CI establishes the relationship, RTP-MIDI2 carries the remote capability plane, CodexKit translates the typed MIDI2 lifecycle into the pinned Codex app-server protocol, the execution host supplies the development environment, and durable evidence—not a client stream or local chat database—establishes what actually happened.
