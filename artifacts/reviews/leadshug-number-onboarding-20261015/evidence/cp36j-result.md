# cp36j test-only result

A dedicated wrong-app test was added to `api-app/src/integrations/meta/meta.client.spec.ts` (SHA-256 `9faf845a3395b646013b82ced46eeb42b79888b16b0f82b542697fd2223c2247`). Its grant has `app_id: different-app`, `is_valid: true`, both required scopes, and granular targets intersecting at the requested WABA `123456`. The real client receives the scoped candidate token, and a valid matching phone page is defined as fallback. The same operation rejects with `MetaIndisponivelError` and `META_INDISPONIVEL`, makes exactly one authenticated request to the fixed Graph `debug_token` endpoint, and makes no `phone_numbers` request. Product implementation did not change.

Only the spec differs from cp36i among the nine manifested public source paths. The manifest was unchanged before and after the API run. `tsconfig.build.json` remains unchanged and excludes `**/*.spec.ts`.

The single canonical API leaf, `bash scripts/test-channels-local.sh api`, exited 0. Lint and build passed; all 22 migrations applied; 174 API unit tests and 288 PostgreSQL E2E tests passed. Raw output is preserved in `cp36j-api.log` (SHA-256 `88d69b62ae8c4b272fa8fb1ee15583340575fa60ed5bb1ceabfd79f06503da61`).

Web (28 tests) and browser (47 tests) are reused from the immutable cp36h evidence because the eight relevant non-spec paths remain byte-identical and the spec is excluded from the API build. The original cp36h freshness and browser attestations retain their original hashes and tested unit-spec hash; they are not relabeled as current cp36j attestations. No new all-537 result or current browser run is claimed.

STOP: the authorized test-only change and single API leaf are complete. Fresh full TQA, distinct final review, and root-owned gates remain outstanding.
