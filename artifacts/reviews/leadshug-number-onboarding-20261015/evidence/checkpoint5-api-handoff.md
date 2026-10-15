# API checkpoint 5 handoff

Date: 2026-10-15. API source is frozen after this handoff; no commit or push was made. This completes the bounded API implementation/remediation work, not the overall TODO or final security/operational gates.

## Validation

- Node `22.23.3` Docker runner; PostgreSQL `16.15` Docker, disposable DB `leadshug_timeline_onboarding_cp5_final2`. No operational database or live provider was used.
- `npm run build` and `npm run lint` passed in `checkpoint5-lock-order-probes-final.log`.
- Full unit run: 19 files, 130 tests passed (`checkpoint5-full-unit.log`). It predates only the final lock-probe test-only change in `test/atendimento.e2e-spec.ts`; no product source changed after it.
- Full serial PostgreSQL E2E: 25 files, 262 tests passed (`checkpoint5-full-e2e-final.log`). It predates the final two lock-probe tests. The later current-source focused `test/atendimento.e2e-spec.ts` run passed 25/25 (`checkpoint5-lock-order-probes-final.log`), so both added probes pass. The union covers 264 distinct tests; this is not one whole-suite run against the exact final test tree.
- Existing focused suites: 60/60 flow/webhook/atendimento regressions (`checkpoint5-browser-api-regressions.log`) and caller scoping 1/1 (`checkpoint5-caller-scoping-regression.log`). The focused atendimento rerun supersedes its earlier failed expectation-only attempt; the earlier raw logs remain unchanged.
- BCI duplicate create/finalize proof: 20 concurrent operations × 5 repetitions, 5 mismatch negative controls, winner persisted each repetition (`checkpoint5-bci-rerun3.log`). This is specifically duplicate-submit/replay evidence, not a general BCI/REG-SEC pass.
- Browser fixture scripts pass Node 22 syntax checks and provider fixture smoke (`checkpoint5-browser-fixture-syntax.log`, `checkpoint5-browser-fixture-smoke.log`): unauthenticated provider-state control returned 403; authenticated state returned 200 with safe resource projection. This is fixture-server smoke only; no Playwright/browser run was performed.
- Current source manifest: `checkpoint5-source-manifest-final.json`, 48 changed/untracked API source files, branch `feature/number-onboarding`, baseline `ae6a9662c29b77276351aa9de653a47276372246`; manifest SHA-256 `26d8a3f1e811e7acce446606d320958860b78704900d2ba5ada85cb7d4da4e8e`.
- Four additive migrations are in `prisma/migrations/*number_onboarding*/`; final isolated DB had all 20 project migrations deployed. Earlier `checkpoint5-schema-generate-migrate.log` records fresh deployment and Prisma generation.

## NUM-API finding map

| Finding | Implemented behavior and discriminating evidence | Coverage status |
|---|---|---|
| 01 BU phone CAS | Evolution identity proof reserves the canonical BU phone before Meta registration; concurrent different-phone official/Evolution case is in `number-onboarding-flow.e2e-spec.ts` (“atomically prevents official enrollment…”). Losing official attempt makes zero register calls. | Tested. |
| 02 Attempt/credential/operation fencing | Confirmation and lifecycle CAS use attempt/version/generation/epoch/operation lease; stale confirmation after lease replacement and same-key reservation race are in `number-onboarding-flow.e2e-spec.ts`. | Tested for listed barriers; exhaustive expiry permutations remain part of security review. |
| 03 Removal vs lease | `number-onboarding-flow.e2e-spec.ts` (“serializes unlink against an in-flight managed create lease”) verifies removal cannot bypass active pair operation; `atendimento.e2e-spec.ts` also pauses send response across retirement. | Tested. |
| 04 Renewal cleanup/replacement | Managed RENEW cleanup produces a reserved never-created replacement; flow test (“renews a managed Evolution identity…”) verifies cleanup then one replacement. Real RENEW is also exercised in the lock-order probe. | Tested. |
| 05 No legacy adoption | Migrated unmanaged identity test proves it is neither adopted, verified, nor deleted. | Tested. |
| 06 Same QR round across observations | Flow test (“keeps an unverified QR attempt and epoch across connecting/open observations”) verifies the pending epoch remains stable. | Tested. |
| 07 Retained ambiguous cleanup | Flow test (“retains ambiguous managed cleanup…”) proves cleanup is reconciled before the next create after unlink. | Tested. |
| 08 Honest readiness after disconnect | Webhook E2E “close removes readiness and sender resolver blocks channel” checks disconnect invalidates readiness and sending. First-in receipt and subscription convergence cases are in flow tests. | Tested. |
| 09 Own-number proof required | Flow identity/phone tests reject wrong resource/phone and Evolution verifies from provider-owned identity; connection only follows own-identity proof plus keyed first IN. | Tested; no external Meta identity proof. |
| 10 Candidate secret expiry/supersession | Flow test verifies candidate ciphertext/nonce wipe on expiry and supersession while active credential remains. | Tested. |
| 11 Same-key idempotency winner | Flow tests cover duplicate request after reservation commit and different-BU resource ownership race; BCI log provides 20×5 duplicate-submit/replay with mismatched-payload controls. | Tested for create/finalize replay. The BCI sample is limited to this probe. |
| 12 Administrative audit | Audit path records actual actor for mutation. | Code path present, but no discriminating second-ADMIN audit E2E was added; keep this probe open. |
| 13 URL/secret redaction | Safe-redaction unit and webhook diagnostic tests cover URL/path/query secrets and redacted provider payloads. | Tested; keep broader adversarial encoded-secret review open. |
| 14 Lock order ingress vs retirement/renewal | Actual PostgreSQL `FOR UPDATE` barrier tests in `atendimento.e2e-spec.ts` hold the identity row, start inbound acceptance, and then unlink or RENEW. The RENEW case proves old identity cleanup/epoch replacement wins and no stale message is stored. | Tested for unlink and RENEW lock ordering; not a universal proof of every possible lock graph. |
| 15 OUT without provider ID | Atendimento and Typebot tests preserve explicit failed/ambiguous durable outcome without synthetic external ID or automatic resend. | Tested. |
| 16 Tenant/caller/session isolation | New real-Nest/PG caller test verifies distinct channel credentials for BFF, public API and Typebot and rejects cross-resource token reuse; mixed-owner Meta raw batch partitions by verified resource; Typebot tenant/session isolation, actor revalidation, cross-tenant and role/module tests also run. | Key scenarios tested. Not all revoked-session/grant race permutations or all caller failure points have separate barriers. |
| 17 Legacy route and module positives | Legacy connect/QR routes reject without provider calls; `modulos.e2e-spec.ts` retains 404 ceilings and adds new-path official-floor and nonofficial positive module proof. | Tested. |
| 18 Pre-identity diagnostics | Webhook diagnostic test rejects arbitrary pre-identity state content; verified diagnostics are persisted through the identity fence and redacted. | Tested. |

The accepted API review findings were addressed in source, but the rows above do not constitute an all-green REG-SEC-01..13 security gate. Root should preserve the explicit open items noted above and any remaining final-review findings.

## Browser fixture contract and API DTOs

The browser lane can use `test/browser-server.cjs` plus `test/timeline-fixtures.cjs`. The browser talks to real Nest BFF, session/CSRF, policy, and PostgreSQL. Only SDK/provider adapters are replaced. The fixture exposes provider-only authenticated configuration/state/call/effect/barrier controls, Meta code/resource grants and cursor pages, Evolution per-instance inventory/QR/owner/status/cleanup outcomes, and an authenticated Evolution webhook callback. Controls track provider calls/effects and can fail before an effect, hold before/after an effect, or drop an ambiguous response. No fake BFF DTO path was added. Full Playwright exercise of these controls remains pending.

Registration routes:

- `GET /api/bff/number-registrations/capabilities`
- `POST /api/bff/number-registrations` with `tipo`, `operation`, optional `buId` / `novaBu` / `channelId` / `expectedGeneration`, and `Idempotency-Key`.
- `GET /api/bff/number-registrations/:id`; `POST .../:id/authorize` with one-use `nonce` and transient `code`; `GET .../:id/options` with optional `wabaId` and `after` cursor.
- `POST .../:id/confirm` with `wabaId`, `phoneNumberId`, `modoRegistro`, optional transient `pin` and `after`; `POST .../:id/advance`, `/retry`, and `/cancel` take empty objects.
- Unofficial pairing is `POST /api/bff/business-units/:buId/channels/nao-oficial/pair` with `intent` and `expectedGeneration`; legacy channel POST and QR GET are retired. Incoming Evolution callbacks use `POST /webhooks/evolution` and header `x-leadshug-webhook-secret`, never a secret path/query.
- Install variables: public `META_APP_ID`, `META_SIGNUP_CONFIG_ID`, `GRAPH_VERSION`, `PUBLIC_ORIGIN`; private `META_APP_SECRET`, `WEBHOOK_VERIFY_TOKEN`, `CHANNEL_CREDENTIAL_KEY_ID`, `CHANNEL_CREDENTIAL_KEY`, Evolution API key and `EVOLUTION_WEBHOOK_SECRET`. Canonical credential key is base64 for 32 bytes. Do not populate actual values in tracked config. `GRAPH_VERSION=v26.0` is the current setup input supplied by operator; account-level external verification is still pending.

DTOs expose attempt ID, BU, safe state/stage/error code, expiry/version/generation and selected channel readiness dimensions; they do not expose attempt rows, encrypted envelopes, nonce hash, provider tokens, PINs, or codes.

## Remaining boundary

There was no Meta authorization, number registration, subscription, Evolution QR pairing, real inbound/outbound message, HTTPS callback, or browser Playwright run. No actual provider readiness is claimed. Source and evidence are uncommitted; root owns subsequent review and handoff.
