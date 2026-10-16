# cp22 API handoff

Status: implementation edits preserved; canonical `bash scripts/test-channels-local.sh api` finished. Do not interpret this run as accepted or green. The runtime handoff paused product work after the runner.

## Validation

- New migration `20261016160000_number_onboarding_current_channel_identity_index` applied successfully; Prisma reported 22 migrations and schema up to date.
- Lint and Nest build passed.
- Unit: 19 files, 138 tests passed.
- PostgreSQL e2e: 24 files passed, 2 failed; 284/286 tests passed.
- Failure 1: `test/atendimento.e2e-spec.ts:139`, new concurrent authenticated same-key OUT echo test throws `ReferenceError: buId is not defined`.
- Failure 2: `test/number-onboarding-flow.e2e-spec.ts:668`, held-old-verification RENEW test expected HTTP 409 / `IDENTITY_QUARANTINED` but got HTTP 200. The assertion is preserved pending bounded diagnosis of RENEW operation/stage semantics; it must not be weakened without confirming the contract.
- Raw runner log SHA-256: `7bb87d0ab076bc70912907c2f83ad6b444fb067ede9fecca85f49695bbb12542`.
- Post-run manifest: `cp22-api-source-manifest-after.json` (215 public entries; zero private/operational paths read or hashed).

## Changed admitted source paths and SHA-256

- `api-app/prisma/schema.prisma` — `3dd87c61af51167ae8aaa07a1b35e8616f108d9e5a05b2c0911ea84a8bfa5636`
- `api-app/prisma/migrations/20261016160000_number_onboarding_current_channel_identity_index/migration.sql` — `aadefab2ce66f3484661e66fdf918f5e295926bf9b89b0af4c3e2c8c5c78b740`
- `api-app/test/number-onboarding-pcv.e2e-spec.ts` — `5a608fa9ed3df38b91b2f90b18f34a0d3a88bf0cce75cdf629aa612c04747956`
- `api-app/test/helpers.ts` — `6f58ee65d1d514a1549de8f8ade0adae5718cf624fbe809eb0b56a7af6534dda`
- `api-app/test/number-onboarding-typebot.e2e-spec.ts` — `d814bfb2193a9aa8a69c841042b1429d8bd2c8670b49499ef994b0171fec382f`
- `api-app/test/atendimento.e2e-spec.ts` — `ff2e08991b3b814c1abd24d7c99bfc2718e68f5d686413ad21e3ab2b4a9d5261`
- `api-app/test/number-onboarding-flow.e2e-spec.ts` — `39c35578d1a2be4761c7ea5981b3bd48f55a65fd707a2c1c867b7f271ee493ef`
- `api-app/test/timeline-fixtures.cjs` — `0764582d7b97d231a0e614ccbe83079ba15582f5e0c868d5da3e75aef9391fd5`

## Disposable browser fixture control for Web

The loopback fixture exposes `POST http://127.0.0.1:${LEADSHUG_FIXTURE_PORT ?? 3101}/provider/attempt/expire` behind header `x-fixture-provider-token: timeline-provider-port-only`. JSON body must be `{ "attemptId": "<UUID>", "buId": "<UUID>" }`. It updates only the matching attempt scoped by both IDs and only if `operation=NOVO`, `state=PENDING_AUTH`, and `channelId IS NOT NULL`; otherwise it returns 404. It sets `expiresAt` into the past. The route is on the existing provider fixture listener, not a Nest/public endpoint; it does not synthesize BFF responses. A browser test can read the real BFF create-NOVO response's attempt and BU IDs, then call this fixture control before reloading/polling the real BFF. For ambiguous exchange, configure the effective provider-call failure as `failures: { "meta.exchange": { "remaining": 1 } }`; `exchangeCode` calls `/provider/call`, which consumes this control and throws. This simulates an ambiguous exchange error at the API boundary; it does not prove that the remote provider consumed the OAuth code. The `ambiguousAfter` map is checked by `/provider/effect` and is not reached by `exchangeCode`.
