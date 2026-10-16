# cp22 API validation handoff

The authorized API index and reviewer controls are implemented in the principal checkout. The final source-owned `bash scripts/test-channels-local.sh api` run passed after the two earlier reruns exposed test-harness assumptions. This is bounded API validation evidence; it is not acceptance of the overall local gate or TODO.

The new versioned migration `20261016160000_number_onboarding_current_channel_identity_index` applied successfully. Prisma reported all 22 migrations applied and the validation database up to date. Lint and Nest build passed. Unit tests passed: 19 files, 138 tests. PostgreSQL e2e passed: 26 files, 286 tests.

The final RENEW regression holds the old verify request and cleanup consult, observes trust reset before cleanup completes, verifies the expected cleanup-complete/retry stage without a premature new provider instance, then proves the old verification returns stale. A same-epoch retry creates the new Y-owned instance and quarantines it. Old-WUID `open` events may update the provider connection observation, so readiness is checked through the top-level `CONECTANDO` status, `ownNumberVerified=false`, `verifiedEpoch=null`, and no receipt. The test then verifies message rejection without content/identity leakage, Message/conversation/unread/realtime/bot effects, and same-key acceptance only after current X verification. The foreign-first global trigger test and concurrent authenticated same-key OUT echo test also passed.

NUM-PERF-01 evidence is in the final raw log at line 345. The PostgreSQL probe seeded 2,000 unrelated retired identities (2,001 total), invoked `ChannelCredentialResolver.resolve(channel.id, 'registration')`, then explained the same `provider_resource_identities.current_channel_id = channel.id` relation filter. PostgreSQL chose `Index Scan` on `provider_resource_identities_current_channel_id_idx`, with one actual row and 0.012 ms reported execution time. The test runs `ANALYZE` and does not force planner settings. This is a test-after, disposable-database observation of the resolver-shaped relation lookup, not a capacity or SLO claim.

The browser fixture handoff remains available at `POST http://127.0.0.1:${LEADSHUG_FIXTURE_PORT ?? 3101}/provider/attempt/expire`, guarded by `x-fixture-provider-token: timeline-provider-port-only`, with exact `{attemptId, buId}` UUID scope and NOVO/PENDING_AUTH/channel eligibility. The effective simulated ambiguous exchange setup is `/provider/config` with `failures: { "meta.exchange": { "remaining": 1 } }`; `exchangeCode` calls `/provider/call`, which consumes that failure. It represents an ambiguous API result and does not prove remote OAuth code consumption. `ambiguousAfter` does not affect this exchange path.

The final pre/post manifests cover 215 public source inputs plus 15 supplementary public build/config references. The only primary manifest entry recorded missing is the already-deleted `api-app/src/domain/channels/channels.service.spec.ts`; all other primary and supplementary hashes match across the run. No private or operational paths were read or hashed.

Final raw log SHA-256: `9aa7683bd56eccbe1407dd3ea2a1953ec78412cc6061d9c4ae543a298f562e39`.

Final pre/post manifests: `cp22-rerun3-source-manifest-before.json` and `cp22-rerun3-source-manifest-after.json`.

The first two run logs are retained without alteration: `cp22-api-validation.log` (initial failures), `cp22-api-validation-rerun.log` (harness fixes with one overly strong provider-state assertion), and `cp22-api-validation-rerun2.log` (old-WUID observation contract correction). The final run is `cp22-api-validation-rerun3.log`.

## Final admitted source hashes

- `api-app/prisma/schema.prisma` — `3dd87c61af51167ae8aaa07a1b35e8616f108d9e5a05b2c0911ea84a8bfa5636`
- `api-app/prisma/migrations/20261016160000_number_onboarding_current_channel_identity_index/migration.sql` — `aadefab2ce66f3484661e66fdf918f5e295926bf9b89b0af4c3e2c8c5c78b740`
- `api-app/test/number-onboarding-pcv.e2e-spec.ts` — `5a608fa9ed3df38b91b2f90b18f34a0d3a88bf0cce75cdf629aa612c04747956`
- `api-app/test/helpers.ts` — `6f58ee65d1d514a1549de8f8ade0adae5718cf624fbe809eb0b56a7af6534dda`
- `api-app/test/number-onboarding-typebot.e2e-spec.ts` — `d814bfb2193a9aa8a69c841042b1429d8bd2c8670b49499ef994b0171fec382f`
- `api-app/test/atendimento.e2e-spec.ts` — `d7047c83ba6338dc3452d8d182a9586df79bcb5a90032a2282d8f1422b1b43dd`
- `api-app/test/number-onboarding-flow.e2e-spec.ts` — `40128cbe31499fa490430632367967d3b4a8851a7f53321ebf160dc69c533ff5`
- `api-app/test/timeline-fixtures.cjs` — `0764582d7b97d231a0e614ccbe83079ba15582f5e0c868d5da3e75aef9391fd5`
