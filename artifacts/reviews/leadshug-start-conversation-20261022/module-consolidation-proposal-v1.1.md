# ST-CON-04 module consolidation proposal

Proposal for review, not canonical module edits or delivery proof. Preserve completed ST05/ST06 execution history and their evidence. Their text-only/window rules remain historical baselines; two explicitly approved ST04 supersedes define the new current contract when implemented and validated.

Planned edits are limited to `modules/inbox-and-conversations.md` and `modules/integrations-and-channels.md`. Replace stale forward-looking statements that ST04 has no approval/implementation with a stage-correct reference to the governing active TODO; never claim the required preserved-runtime operator proof before it occurs.

Inbox gains a stable section describing manual open/reuse without send/read/claim/automation, truthful empty state, explicit channel and read-only preview, durable first-send key/request/slot and same-owner Message acceptance, CAS preservation of concurrent claim/close, known external receipt versus local completion, and local-only reconciliation/risk release after the immutable deadline. Document recovery of the original browser snapshot after storage failure without automatic POST. Ordinary diagnostic null-ID failed Messages remain their inherited behavior; the new first-send path never fabricates a sent Message without external ID.

Integrations gains a stable section extending the one abstract sendMessage operation to text/approved-template with supportedKinds and typed zero-HTTP refusal. Management stays create/list/query only; no send method is added to it. Concrete Meta/Evolution adapters own protocol and registration. The initial coordinator composes narrow transport/management dependencies without reverse module imports or provider branches in consumers.

Both modules state that only qualified signed Meta IN timestamps for the currently selected managed resource open the strict24-hour free-text window; no createdAt/import/nonofficial fallback. Keep the historical timestamp/timeline and former ST06 index semantics as delivered history, and document the additive current-resource index/batched projections.

The initial Meta path reuses the catalog observation but verifies the fresh same-account APPROVED textual asset in at most2filtered pages50 each before claim; pin the captured messaging account and international recipient. Bound6GET/1POST,10s per operation75s overall against90s immutable deadline. Preserve no fallback/retry/network in DB transactions and no external exactly-once claim.

Historical ST05 D09 records the original text-only boundary; append an explicit ST04 supersede link for the transport payload only. Do not rewrite D09 as if management originally sent recipient messages. Ordinary BFF/public/BOT callers remain on the common sender and honor initial-slot exclusion, with no global idempotency/outbox conversion.

One-to-one D01–D10 source/test/target mapping is in `evidence/decision-module-candidate-map-e45-v1.1.json`. Apply only after independent implementation findings are resolved; record exact module diff, baseline hash, stable anchors and final decision consistency before completion. Runtime proof and full guard remain separate gates.
