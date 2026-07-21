# Storage and Performance — What Persists Where, and Why Reads Are Fast

> Chapter summary: Two persistence layers, chosen by fit. The **document layer** — source text, the grounding manifesto, beats, cut script — persists as a **plain-text bundle plus a single library manifest**: human-readable, diffable, portable, and fast to read. The **musical layer** — the Score — persists in **MIDI 2.0** (UMP / Clip File), the native lossless format the project owns. Read performance is an **architectural** property (remove indirection, read one manifest, serve cached truth first), **not** a property of the encoding: the serialization format barely moves the numbers. This chapter locks those decisions and the performance doctrine behind them. It defines required behaviour and constraints; it does not prescribe unverified types or call paths.

## Purpose

A cold library open was measured at ~107s on a full library. The cause was not the storage engine and not the encoding — it was **indirection and N-ness**: every manuscript's metadata was fetched, one at a time, through an HTTP corpus service and a serializing actor. Parallelizing the reads cut it to ~26s; the rest of the win is architectural. This chapter states where data must live and how reads must be shaped so the library feels instant and stays fast as it grows.

## The storage decision

1. **The document layer is a plain-text bundle.** A manuscript's durable content — source (`.fountain`), the grounding manifesto (prose, per chapter 11), beats/windows (human-readable JSON), the cut script (`.fountain`) — persists as plain, human-readable, **diffable, portable** files the writer owns. Prose stays prose; structure stays legible.
2. **The library is a single manifest.** The list the library surface needs — per manuscript: name, last activity, has-source — persists as **one manifest**, read in a single operation. Listing the library must never require one read per manuscript.
3. **The musical layer is MIDI 2.0.** The Score persists in **UMP / a MIDI 2.0 Clip File** — the native, lossless, round-trippable format for time-based musical events, which the project owns end to end. Property Exchange (JSON) and Flex Data carry structured sidecar metadata where wanted. The document layer is never encoded as MIDI, and the musical layer is never flattened out of it.
4. **Format is not the performance lever.** Choosing binary over text (or MIDI over JSON) for the document layer buys effectively nothing for load time — parsing a few dozen names is negligible in any encoding. Persist each layer in the format that fits its *meaning*, and win performance architecturally (below), not by re-encoding documents.

## The performance doctrine (how reads must be shaped)

Read performance is governed by three rules, in order of leverage:

1. **Serve cached truth first (cache-first).** After a successful library load, the resolved list is cached locally, keyed to the store. The next open reads that cache and shows the library **immediately**, then refreshes in the background — the writer never waits on the network/store for a list they already had. (This is chapter 12 applied to the catalog: cheap/cached truth renders first.)
2. **Read one manifest, not N items.** The library load reads the single manifest (rule 2 above), an O(1) operation, rather than iterating manuscripts. Per-item reads happen at **write** time (create/rename), maintaining the manifest — never on the hot read path.
3. **Remove indirection; when reads must fan out, bound their concurrency.** Prefer reading local files/manifest directly over routing every read through a service hop and a serializing actor. Where a fan-out is unavoidable, issue it with bounded concurrency so round-trips overlap and the store is not swamped — never a serial loop.

A corollary: **the store/service is a working/index layer, not the read hot path.** It may remain as the write-through and indexing mechanism during the transition, but the surfaces read from the manifest and the cache.

## Honesty (non-goals)

- **Never fabricate the cache.** The cache is the *last truthful result*; a refresh reconciles it. A stale entry is corrected on refresh, and a genuinely-removed manuscript disappears — the cache is a head-start, not a source of invented truth.
- **Portability is a feature, not an accident.** The plain-text bundle exists so the writer owns readable, diffable files. A future encoding change must not sacrifice that without cause.
- **This is a real re-architecture, done incrementally.** Today reads and writes both route through the store/service; moving the document layer to a bundle + manifest and the read path to cache-first is staged, keeping the store as the working layer until the bundle is the truth.
- **Perceived speed is not actual speed.** Cache-first makes the library *feel* instant; the background refresh must still get fast (one manifest, no serial fan-out). Both are required (chapter 12).

## Relationship to other chapters

- **[Animating truth](12-animating-truth.md)** — perceived performance: cache-first is its "cheap/cached truth first" rule applied to the catalog; the background refresh is foreshadowed, not spun.
- **[Grounding as a given](11-grounding-as-a-given.md)** — the grounding manifesto is prose precisely so it belongs in the plain-text bundle and diffs cleanly.
- **App-flow record (`reframe-app-flow-governance.md`)** — persistence and relaunch there are governed by this chapter's layering.

## Acceptance

1. The library surface reads a **single manifest** for its list; no path iterates per-manuscript reads on load.
2. Opening the app shows the library from a **local cache immediately**, then refreshes in the background — a populated library never blocks on the store/network.
3. The **document layer persists as human-readable, diffable files** (source, grounding prose, beats, cut script); the grounding manifesto remains prose.
4. The **Score persists as MIDI 2.0** (UMP / Clip File); the document layer is never encoded as MIDI.
5. Any unavoidable read fan-out is **bounded-concurrent**, never a serial loop.
6. The cache is reconciled by refresh — stale entries correct and removed manuscripts disappear; nothing in the cache is fabricated.
