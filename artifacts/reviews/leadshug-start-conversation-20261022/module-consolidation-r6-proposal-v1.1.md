# ST-CON-04 module consolidation proposal — current candidate

This is a concrete documentation proposal for review. It does not modify canonical modules or claim implementation delivery. The original proposal, completed ST05/ST06 decisions and their evidence remain historical. The E71 candidate is in validation; only the selected later terminal full-GREEN source seal and independent review can establish readiness to apply this proposal.

Edits are limited to `modules/inbox-and-conversations.md` and `modules/integrations-and-channels.md`. Preserve historical decision text and add explicit current ST04 supersede references for the two approved changes: the single transport payload becomes `text | approved-template`, and the official text window uses qualified current-resource Meta IN timestamps. ST05 management remains a narrow authoring/catalog capability with no recipient-send method. Future providers remain extension points, with no new implementation here.

## Inbox contract to consolidate

Document manual BU/contact opening or reuse independently from sending. Phone normalization retains 8–15 explicit digits and never invents a country. New conversations are QUEUED, unreadCount=0, lastMessageAt=null; opening does not send, mark read, take ownership, reopen/close or trigger automation. Preserve the unique BU/contact identity, timeline timestamps and existing first-IN automation semantics. The dialog belongs to its selected BU; late responses from an old BU cannot select a conversation or leave controls busy in the new BU.

The first send requires explicit channel, message and confirmation. Preview is read-only and local. A new template preview/reservation requires both page availability and an individually available APPROVED observation; renderer support for available POSITIONAL models is independent of inherited authoring flags. Same-key canonical replay precedes new eligibility work. Preserve Unicode code-point limits, bounded JSON envelopes and safe escaped previews.

Document durable immutable request/key/context, one unresolved conversation slot, 90-second immutable deadline and the distinction between a known provider ID and a committed local Message. The common MessageAcceptanceService remains the sole Message owner. Preserve owner/status CAS against concurrent claim or close, conservative uncertainty, and commit-winner-only best-effort publication. An unknown provider result never authorizes automatic resend. Browser reload recovers the persisted original snapshot without issuing a POST automatically.

PREPARED reconciliation is explicit and local: a live lease keeps the slot, while proven pre-dispatch expiry permits rejection/release. Known acceptance can be completed locally without provider network calls. AMBIGUOUS or EXTERNAL_ACCEPTED_LOCAL_BLOCKED risk release needs the immutable database deadline and explicit duplication-risk confirmation. Late outcomes do not reacquire a released slot or change a successor's owner/status. Ordinary BFF/public/BOT callers honor the interlock and preserve inherited null-ID diagnostics; they gain no global idempotency.

## Stable BFF endpoint definitions to consolidate

All new routes require the existing signed BFF session, current tenant/BU authorization at ATENDENTE or above, and CSRF protection on mutation. Define full bodies, safe projections and error/status semantics from the approved TODO and actual controller under the Inbox API Endpoint Definitions section:

- `POST /api/bff/business-units/:buId/conversations/open`
- `GET /api/bff/conversations/:id/start-options`
- `POST /api/bff/conversations/:id/initial-message-preview`
- `POST /api/bff/conversations/:id/initial-messages`
- `GET /api/bff/conversations/:id/initial-messages/:attemptId`
- `POST /api/bff/conversations/:id/initial-messages/:attemptId/reconcile`
- `POST /api/bff/conversations/:id/initial-messages/:attemptId/acknowledge`
- `POST /api/bff/conversations/:id/dispatch-admissions/:admissionId/reconcile`
- `POST /api/bff/conversations/:id/dispatch-admissions/:admissionId/acknowledge`

Keep the delivered ST05 catalog routes as the sole catalog API. Acknowledgment requires `X-Confirm-Duplication-Risk: true`; initial submission requires its captured `Idempotency-Key`. GET remains observational. Define 201/200/202/409 and known-local-incomplete responses truthfully; provider acceptance is never described as delivery or reading at the recipient.

## Channel and persistence invariants to consolidate

Consumers depend on the single abstract Channel send method and readonly supportedKinds. Meta owns the text/template protocol and international wire recipient format; Evolution refuses templates with typed zero-HTTP results. Keep concrete factories and protocol inside integrations, without provider branches in inbox or reverse module ownership.

Preserve channel readiness and `requiresWindow`. For official text when `requiresWindow` is enabled, only signed, verified positive nonfuture Meta IN timestamps for the selected managed resource open the strict 24-hour window; the inherited disabled-window configuration remains exempt. There is no createdAt, imported history or unofficial fallback. Reuse the single window-policy query for reads and dispatch. At the durable SENDING transition, the same SQL update checks the trusted expiry and lease against the current database clock. Pin mutable active BU readiness, channel binding and official credential version through that claim. Refuse conflicting row locks without waiting at those pins and the actor/grant fence, preserving the approved identity→contact→conversation→intent relative order and the unchanged ST05 observation owner. Local completion preserves a previously recorded external acceptance if grant/readiness or contention prevents its commit.

The initial Meta template path verifies the fresh same-account APPROVED asset using the existing filtered bounded list, never a browser cursor/URL as authority. Preserve at most six GETs and one POST, ten seconds per operation and 75 seconds overall inside the immutable 90-second deadline. All remote preflight ends before the database claim transaction; recovery is local-only. There is no fallback, provider retry or external exactly-once claim.

Record the additive current-resource and inbox-order indexes plus the two recovery-query access paths. The active-admission ordered index is intentionally SQL-only and partial on `released_at IS NULL`; native metadata and actual captured-query EXPLAIN proof, rather than an unfiltered schema declaration, establish that contract. The whole-conversation conflict query stays unchanged. Preserve all quota, uniqueness and existing SQL-only indexes; apply migrations only under the separately approved preserved-local runtime plan with five-second lock and sixty-second statement bounds.

## Application and closure conditions

Apply only after fresh independent findings are resolved against the selected full-GREEN candidate. Record exact module baseline/current hashes and stable anchors; populate the one-to-one frozen decision/module consistency tables without rewriting historical ST05 D09 as recipient sending. Preserve SEC-R6-04, OPS-R4-01 and TQA-ST05-03 as inherited scoped debt.

Canonical module consolidation, preserved-runtime activation and assisted real first-send/reply, the one separately approved full-diff inspection, final review and closure guards are distinct required gates. None is inferred from this proposal, a synthetic provider, a previous story's proof or the user's attestation that the template is approved.
