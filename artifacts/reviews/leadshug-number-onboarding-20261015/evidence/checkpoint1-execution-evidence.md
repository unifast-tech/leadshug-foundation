# ST-CON-01 checkpoint 1 execution evidence

**Status:** checkpoint complete; TODO remains active and overall delivery remains pending.
**Branch/baseline:** `feature/number-onboarding`, API baseline `ae6a9662c29b77276351aa9de653a47276372246`.
**Runtime:** Docker Windows (`docker.exe`), Node `v22.23.3`, PostgreSQL `16-alpine`; separate network/container and database `leadshug_number_onboarding_test`, separate named Linux `node_modules` volume. Database URL used only inside the disposable container; the fixture password is disposable and no configured production credentials were read or logged.

## Implemented

- Prisma models for `ChannelRegistrationAttempt`, `ChannelCredential`, and durable `ProviderResourceIdentity`; active credentials and attempt candidates use separate encrypted envelope fields. `BuChannel` now carries generation, current attempt, pairing epoch, own-number verification, provider-connection state, and receipt timestamp. Registration workflow state is a separate explicit enum from the existing channel status.
- `Message.providerResourceIdentityId` is nullable for historical compatibility. New keyed writes use the unique `(provider_resource_identity_id, external_id)` key. Legacy message IDs were not backfilled or rewritten.
- Versioned migration preflights cross-BU collisions among already connected provider resource IDs before adding uniqueness, then seeds identities only from their unambiguous existing channel-to-BU mapping. Collision failure includes a count only and aborts; no merge/delete occurs. An additive migration makes provider/resource/BU ownership immutable in PostgreSQL; deleting a channel can detach its current pointer while retaining the BU-owned tombstone.
- `channel-credential-crypto.ts` uses AES-256-GCM, a random 12-byte nonce, a 16-byte tag, and versioned AAD bound to purpose/provider/BU/channel/generation plus candidate attempt ID or active version. Runtime config names are `CHANNEL_CREDENTIAL_KEY_ID` and `CHANNEL_CREDENTIAL_KEY`; key must be canonical base64 for exactly 32 bytes. Missing keys, wrong AAD, and tampering fail closed with a generic safe error.
- `safe-redaction.ts` recursively redacts secret-bearing fields and bearer/URL secrets.
- `MessageAcceptanceService` is ready for checkpoint 2 callers. It requires a nonempty provider message ID; shares a PostgreSQL row lock on the durable identity while checking exact current BU/channel/generation/pairing epoch/verification; transactionally creates/reuses IN conversation plus unread effects; and reconciles OUT sender/echo rows by the same key. Replays return `creationWinner`/`reconciled` metadata. Only an authenticated sender-result input can enrich an unauthored echo with trusted content and authorship; later echoes cannot replace it, and ID and `createdAt` remain stable. It does not publish realtime or call automation; callers must gate those effects on `creationWinner`.
- `persistVerifiedDiagnostic(...)` writes recursively redacted metadata only while the same identity fence is held through the final write. Checkpoint 2 retirement/renewal code must update/lock the same `ProviderResourceIdentity` row in its short transaction when resetting current attachment/trust; stale requests then cannot persist message content or diagnostics. Provider parsing remains outside this service.

## Validation

All commands used the API package's declared scripts and a new isolated PostgreSQL 16 database; no existing application database was mounted or targeted.

- `npx prisma validate` and `npm run prisma:generate`: pass, Prisma 6.19.3.
- `npm run prisma:migrate` (`prisma migrate deploy`): all 19 migrations applied successfully to the disposable DB, including the ownership-immutability migration.
- `npm run lint`: pass.
- `npm run build`: pass.
- `npm test`: pass, 18 files / 119 tests.
- `npx vitest run --config vitest.config.e2e.ts test/number-onboarding-message-acceptance.e2e-spec.ts`: pass, 1 file / 3 PostgreSQL tests, including concurrent IN replay/unread, echo-first OUT author/content reconciliation, redacted diagnostics, retired identity rejection, and immutable owner enforcement.
- Full `npm run test:e2e`: pass, 21 files / 226 tests. This broad run was immediately before the last narrow additions (`FOR SHARE` ingress locking, fenced diagnostics, owner trigger, and sender content fill); those final changes were validated by the final targeted command above.
- `git diff --check` with `core.whitespace=cr-at-eol`: pass. The canonical Prisma schema has CRLF line endings; additions retain that convention.

Raw outputs: `checkpoint1-prisma-generate.log`, `checkpoint1-migration-deploy-initial.log`, `checkpoint1-migration-deploy-final.log`, `checkpoint1-final-targeted-validation.log`, and `checkpoint1-api-e2e.log` beside this report. `checkpoint1-source-hashes.sha256` records hashes for every changed API source/schema/migration/test file.

## Handoff boundary

Checkpoint 1 does not integrate BFF/public/Typebot senders or webhooks, remove global-token use, add API routes, wire DI, or update the canonical TODO/module docs. Checkpoint 2 must route every new external-ID Message writer through `MessageAcceptanceService`, make retirement/renewal use the same identity-row fence, and publish/trigger automation only for the creation winner. Overall ST-CON-01 remains incomplete; provider proof, UI, consumer cutover, broad race/security gates, and independent reviews remain outstanding.
