# 136 — Reframe Web, Native, Headless, and Audio Runtime Boundary

> Chapter summary: Reframe has one governed runtime model and multiple clients. A Linux headless service owns
> Store, MIDI2, scenarios, and receipts; web and native iPad/macOS clients project and control that model. Interactive
> audio renders at the user's device, while the server owns typed intent, state, timing, and evidence.

## The decision

Reframe is a multi-client product. The web client is the natural SaaS surface and the native iPad client remains a
first-class creative host. Neither client becomes a second semantic authority. ReframeCore, MIDI2, and FountainStore
remain the shared spine; platform adapters own presentation, device access, and local rendering.

```text
web / native iPad / native macOS → typed MIDI2 gateway → headless ReframeCore on Linux
                                                               ↓
                                             FountainStore, scenarios, receipts
```

## Audio boundary

Interactive instruments render locally. The web client uses Web Audio with AudioWorklet and WebAssembly where needed;
the iPad client uses AVAudioEngine and Audio Units; macOS may use its native audio graph. The server sends typed MIDI2
intent, parameter state, timing, and instrument assets. It does not stream every audio sample for local interaction.

Remote rendered audio may use WebRTC as a monitoring or ensemble lane, but it is not the authority for instrument
state, timing, or completion. Audio callbacks remain real-time safe: no Store access, network requests, model calls,
or allocation-heavy semantic work occurs inside them.

## Rules

1. ReframeCore is one semantic runtime shared by web, iPad, macOS, and Linux headless hosts.
2. The web client is a first-class SaaS client, not a replacement authority or a parallel OpenAPI command system.
3. Native iPad is a first-class creative and performance client, not merely a web wrapper or Mac remote control.
4. Linux headless Reframe owns Store, MIDI2, scenario execution, leases, receipts, and service operations.
5. Web, iPad, and macOS clients consume generated MIDI2 contracts and typed terminal state.
6. Interactive audio renders on the user's device; the server transports intent, state, assets, and synchronization.
7. Web Audio/AudioWorklet/WASM and AVAudioEngine/AudioUnit implementations may differ while preserving instrument
   identity, parameters, event semantics, timing policy, and failure states.
8. WebRTC is an optional rendered-audio transport and never replaces MIDI2 or FountainStore authority.
9. Audio callbacks cannot call ReframeCore, FountainStore, network services, or conversational reasoning.
10. Client, runtime, audio, and SaaS claims each require their own typed acceptance evidence.

## Governing sentence

One Reframe runtime may have many faces: let Linux hold the governed state, let web and native clients meet the
writer where they are, and let each user's device render interactive sound without moving authority into the audio
stream.
