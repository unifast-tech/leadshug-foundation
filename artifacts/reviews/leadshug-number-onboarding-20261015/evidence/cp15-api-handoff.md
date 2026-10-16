# CP15 bounded API fixture handoff

Only the two authorized API test paths changed in this handoff.

In `api-app/test/timeline-fixtures.cjs`, `seedNumberOnboarding` now creates its OWNER fixture grant with `grantedViaTipo: MANTENEDORA` and `grantedViaId` set to that fixture tenant. ADMIN and ATENDENTE retain direct grants; historical timeline seed behavior is unchanged.

In `api-app/test/number-onboarding-flow.e2e-spec.ts`, one PostgreSQL regression exercises the production founder's `novaBu` path: create a BU and registration attempt; replay the same idempotency key and body; assert one BU, one attempt, the same attempt ID and nonce, and the inherited OWNER grant; then assert a changed body returns `IDEMPOTENCY_CONFLICT` without creating another BU.

`git diff --check` passed. `timeline-fixtures.cjs` passed a syntax-only check using Node v22.23.3 in a disposable container. No browser, application, database, or E2E tests were run in this bounded handoff. The new PostgreSQL regression is authored and awaits the integrated final test run.

File hashes are recorded in `cp15-source-hashes.sha256` (manifest SHA-256 `cb15ac4e643fa5eaccccff784eac1d2b5e092074b65c5f5af6b7291e29639e16`): `timeline-fixtures.cjs` `ffbbb697205edbe9e076adf33f418d883339f40675f078479eccf704899ca62a`; `number-onboarding-flow.e2e-spec.ts` `f22a48ec138978f6d09cb0eeb92ba9fc4ea5da416cfbd86d9c43ec4a5d8db12e`.

API writes are stopped for the Web browser lane and integrated final validation.
