# cp36i test-only result

The dedicated revoked-grant case is in `api-app/src/integrations/meta/meta.client.spec.ts` (SHA-256 `9612cd1c7a5d8c68bca7c515625db0601acb479585625f9b8fc93fbc04c464b1`). It supplies a valid-shaped grant with the matching app ID, both required scopes, and both granular targets intersecting at WABA `123456`, while `is_valid` is `false`. The operation receives a scoped candidate token. A valid phone page is defined as fallback; the same operation rejects with `MetaIndisponivelError` and `META_INDISPONIVEL`, makes one authenticated request to the fixed Graph `debug_token` endpoint, and makes no `phone_numbers` request. Product implementation did not change.

The nine-path source manifest changed only for the spec. The other eight paths are byte-identical to cp36h, and the manifest remained identical before and after API validation. `tsconfig.build.json` is unchanged and excludes `**/*.spec.ts`.

The one authorized canonical API leaf, `bash scripts/test-channels-local.sh api`, exited 0. Lint and build passed; all 22 migrations applied; 173 API unit tests and 288 PostgreSQL E2E tests passed. Raw output is preserved in `cp36i-api.log` (SHA-256 `f943d9049c06ce39a25be958228100051389fc190452c1b3d10ccb403f1778c1`).

Web (28 tests) and browser (47 tests) are composed from the immutable cp36h evidence because all eight relevant non-spec paths are byte-identical and the spec is excluded from the API build. The original cp36h pre-worker freshness and browser attestations retain their original hashes in `cp36i-result.json`; they are not claimed as fresh cp36i attestations. No new all-536 result or current browser run is claimed.

STOP: this executor completed the authorized test-only change and single API leaf. Fresh full TQA, distinct final review, and root-owned current source/candidate gates remain outstanding.
