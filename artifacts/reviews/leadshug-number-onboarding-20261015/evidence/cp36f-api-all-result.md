# cp36f API payload contract validation

The Meta adapter now fails closed when a successful response cannot be parsed as a JSON object, when a phone-number page lacks an array of valid rows, or when pagination fields are structurally inconsistent. A valid exhausted page still returns `null`; grant validation, fixed Graph host, bounded cursor and request budget remain in place. The BFF test exercises the real `MetaHttpClient` behind the declared `META_CLIENT` port with deterministic `fetch` stubs, then asserts the fixed public 503 envelope, no provider detail, and unchanged channel, BU, attempt/version, credential, identity, receipt, audit count, and released lease. A separate generic port error remains a generic 500 and is not mapped to `META_INDISPONIVEL`.

The test-first RED is genuine: `bash scripts/test-channels-local.sh api` exited 1 after 22 disposable migrations and stopped at the API unit leaf with 142 passing and 8 failing tests. The new invalid-page cases exposed resolved `null` for malformed JSON/missing data/row-without-id/paging type defects, plus raw `TypeError` for non-array data and null rows. The existing missing-cursor case already failed closed, so it passed in RED. No PostgreSQL RED is claimed because the canonical API leaf stopped at the unit failure.

After the adapter correction, one canonical `bash scripts/test-channels-local.sh all` run exited 0: 150 API unit tests, 288 PostgreSQL tests, 28 Web unit tests, 47 browser tests, and 22 migrations passed. The runner reported Node v22.23.3, OpenSSL 3.0.22 and Prisma `debian-openssl-3.0.x` in its isolated validation namespace.

Genuine freshness evidence is retained byte-for-byte in `cp36f-pre-worker-freshness.json` and `cp36f-browser-attestation.json`. Both include nine source hashes exactly matching `cp36f-source-after.sha256`; both API/Web HEADs match current submodule HEADs. The pre-worker capture ran before Playwright workers and recorded API, fixture, and preview health. The browser attestation records the disposable PostgreSQL database and 22 migrations, and confirms that the served JavaScript hash matches the built `dist` bundle. The runner raw ends with 47 passing browser tests. External Meta/provider behavior and the operator runtime were not exercised or changed.

Evidence files:

- `cp36f-api-red-command.txt`, `cp36f-api-red.exit-code`, `cp36f-api-red.log`, `cp36f-red-source.sha256`
- `cp36f-api-all-command.txt`, `cp36f-api-all.exit-code`, `cp36f-api-all.log`
- `cp36f-source-before.sha256` is the pre-fix source snapshot captured for RED; `cp36f-source-after.sha256` is the post-validation snapshot; `cp36f-source-freeze.json` binds source hashes, raw log hashes, and freshness attestations.
