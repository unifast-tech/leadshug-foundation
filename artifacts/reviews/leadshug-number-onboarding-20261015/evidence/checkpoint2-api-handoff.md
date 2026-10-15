# Checkpoint 2 — API onboarding and caller cutover

Status: implementation handoff for independent API review. The bounded API checkpoint is implemented and validated; the larger TODO remains open. No commit or push has been made. Product edits are stopped pending root review.

## Source and validation

- Checkout: `api-app`, branch `feature/number-onboarding`, baseline `ae6a9662c29b77276351aa9de653a47276372246`.
- Source manifest and SHA-256: `checkpoint2-api-source-hashes.sha256` (42 product files, including three additive migrations).
- Validation source tree: the same checkout/source hashes above. Node runner: `node:22.23.3-slim`; PostgreSQL 16 container: `leadshug-number-onboarding-pg16-final`; isolated database `leadshug_timeline_onboarding`; reusable dependency volume `leadshug-number-onboarding-node-modules`.
- Fresh disposable database migration deployment: 20 migrations found; third new migration `20261015140000_number_onboarding_channel_operation_fence` applied successfully. Raw output: `checkpoint2-api-migrate-deploy-final.log`.
- Final source command: `npm run build && npm run lint && npm test && npm run test:e2e` in the Node 22 container, with `DATABASE_URL` explicitly pointed at that isolated PG16 database. Raw output: `checkpoint2-api-final-source-validation.log`.
- Final results: build PASS; lint PASS; unit 20 files / 130 tests PASS; serial PostgreSQL E2E 22 files / 234 tests PASS. Targeted lifecycle evidence is also retained in `checkpoint2-api-lifecycle-targeted-rerun.log` (two selected lifecycle tests PASS). The earlier deliberately failing recovery probe is retained as `checkpoint2-api-lifecycle-targeted-failed.log`; it identified the stale-session check after subscription and was corrected before the final full validation.
- `checkpoint2-evolution-first-in-pg.log` preserves the initial targeted Evolution run. `checkpoint2-api-full-e2e-rerun1.log` is an earlier full-suite run (232 tests, before the last two lifecycle cases); it is superseded by the final source run.

## API contract for Web

`GET /api/bff/number-registrations/capabilities` returns installation/module availability for `oficial` and `naoOficial` with safe reason codes. `POST /api/bff/number-registrations` accepts `tipo`, `operation` (`NOVO` or `REAUTORIZAR`), and exactly one of `buId` or `novaBu`; reauthorization also requires `channelId` and `expectedGeneration`. It requires `Idempotency-Key` UUID and returns `{ attempt, nonce, replay }`. The nonce is a one-use correlation value; replay returns it only for the same user/session while pending and valid.

`GET /:id` returns only the allowlisted registration DTO: `{ id, buId, channelId, tipo, operation, state, stage, errorCode, expiresAt, version, generation }`. It excludes attempts' nonce/session hashes, lease data, candidate envelopes, and provider credentials. `POST /:id/authorize` takes `{ nonce, code }`; `GET /:id/options?wabaId=…&after=…` returns the bounded resource page and cursor; `POST /:id/confirm` takes `{ wabaId, phoneNumberId, modoRegistro: "NOVO"|"JA_REGISTRADO", pin?, after? }`; `POST /:id/advance`, `/retry`, and `/cancel` take empty objects.

Safe channel projections in `/api/bff/business-units`, `/api/bff/business-units/:buId`, and `GET /api/bff/business-units/:buId/channels` carry `id`, `type`, `status`, `generation`, `currentAttemptId`, `ownNumberVerified`, `providerConnectionState`, `receiptVerifiedAt`, `requiresWindow`, and `connectedAt`; the business-unit list also carries the user's direct `papel` for that BU. They do not expose provider resource IDs or private credentials.

Evolution pairing is `POST /api/bff/business-units/:buId/channels/nao-oficial/pair` with `{ intent: "INITIAL"|"RENEW", expectedGeneration? }`. `POST /:tipo/verify` verifies the current provider identity. Legacy channel create responds with deterministic `409 USE_NUMBER_REGISTRATIONS`; legacy QR GET responds `405 QR_GET_REMOVED`. Delete is `DELETE /api/bff/business-units/:buId/channels/:tipo`.

## Configuration names

Official Meta install capability: `META_APP_ID`, private `META_APP_SECRET`, `META_SIGNUP_CONFIG_ID`, `GRAPH_VERSION`, `PUBLIC_ORIGIN`, `WEBHOOK_VERIFY_TOKEN`, and `META_APP_SECRET` for signed webhook verification. Credential encryption uses `CHANNEL_CREDENTIAL_KEY_ID` plus `CHANNEL_CREDENTIAL_KEY` (canonical base64 encoding of exactly 32 random bytes). Evolution install capability uses `EVOLUTION_API_URL`, private `EVOLUTION_API_KEY`, `EVOLUTION_WEBHOOK_URL`, and `EVOLUTION_WEBHOOK_SECRET`. Names and placeholder values are documented in `api-app/.env.example`; no real `.env` was written. Global `WHATSAPP_TOKEN` is no longer required or used for channel sending.

## Behavior delivered

The API now has durable registration attempts, separate encrypted candidate/active credentials, unique immutable provider-resource ownership, a persisted per-channel 45-second operation fence, BU/session/grant checks, nonce/idempotency/expiry handling, post-promotion recovery under a fresh valid session, bounded Meta resource paging and selected-page revalidation, scoped credential resolution, signed Meta ingress, fenced Evolution ingress/diagnostics, keyed IN/OUT message acceptance, sender/echo reconciliation, and safe DTO/redaction paths. Existing BFF, public API, Typebot, webhook and inbox writers now route through current mapped identities and the acceptance service; channel readiness requires the applicable own-identity, subscription and receipt evidence. No provider network is inside a database transaction.

## Remaining evidence and dependencies

- Real Meta setup and external proof are still blocked on the user's Meta app/configuration and public HTTPS webhook origin. Fixtures never assert a real `CONNECTED` Meta account, and no external provider call or phone-number change was made. The Meta source contract has been checked against the pinned/provider references recorded in the preceding evidence, but runtime behavior for a real app remains unverified.
- Root's separate final PCV gate calls for 20 operations × 5 repetitions for the high FRC/BCI probes. The existing timeline E2E in this final run executes its established three batches; this API handoff does not claim that strengthened PCV gate.
- Additional stress evidence remains for same-idempotency-key concurrent replay barriers, cancellation/renewal while external requests are paused, stale Evolution cleanup/ambiguous-create recovery under lease expiry, candidate-resource mismatch preserving an already active credential, all per-tenant grant/session revocation interleavings, and real Meta app/scopes/audience. The full suite passing does not substitute for those unrun REG-SEC/PCV probes.
- No final TODO acceptance claim is made. Web integration, root review, final adversarial probe expansion, and real provider setup/proof remain outstanding.
