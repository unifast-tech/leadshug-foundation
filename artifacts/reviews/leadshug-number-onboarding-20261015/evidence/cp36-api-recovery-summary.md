# cp36 ST-CON-01 Evolution recovery regression

**Scope:** Idempotent recovery of the already receipt-verified current Evolution attempt after an observed disconnect/reconnect, through webhook `connection.update` and repeated administrative verification.

**RED:** `bash scripts/test-channels-local.sh api` ran before production edits. The 138 API unit tests passed. PG E2E finished with 286 passed and the new regression failed: `connecting` returned 200; `open`, duplicate `open`, and repeated `/verify` returned 409 `ATTEMPT_STALE`. The complete runner output was not tee'd during this RED run, so `cp36-api-recovery-red.log` preserves the available raw failing assertion excerpt, exact command, environment, totals and limitation. Pre-fix hashes are in `cp36-api-recovery-before.sha256`.

**Change:** A shared Channels-domain helper now promotes only the exact pending attempt for the channel's generation and pairing epoch. If promotion already occurred, it accepts only that same attempt in `CONNECTED` / `RECEIPT_VERIFIED`, with no version bump. Webhook and administrative verification keep their existing identity/channel locks, leases, receipt checks and CAS conditions. PG regressions cover normal pair → authenticated first IN → connected receipt, repeated verify, connecting/open/duplicate-open, preserved attempt version/receipt/identity/epoch/message, and rejection without channel rollback for cancelled, wrong-generation and wrong-epoch attempts. No schema or migration changed.

**GREEN:**

- `bash scripts/test-channels-local.sh api`: lint and build passed; 138 unit tests and 288 PostgreSQL E2E tests passed. Full output: `cp36-api-recovery-green-api.log`.
- `bash scripts/test-channels-local.sh all`: API lint/build, 138 unit tests, 288 PostgreSQL E2E tests, Web build, 28 Web unit tests, and all 47 Playwright browser tests passed. Full output: `cp36-api-recovery-final-all.log`.
- The browser run generated the actual pre-worker source manifest and served-bundle/database attestation, preserved as `cp36-pre-worker-freshness.json` and `cp36-browser-attestation.json`. The manifest includes the new untracked domain helper and its public-source hash. No private payload or dotenv file was inspected or included.
- `git diff --check` passed.

**Changed product paths:**

- `api-app/src/domain/channels/channels.service.ts`
- `api-app/src/domain/channels/receipt-attempt-convergence.ts`
- `api-app/src/surfaces/webhooks/evolution.controller.ts`
- `api-app/test/number-onboarding-flow.e2e-spec.ts`

Before/after public-source hashes are recorded in `cp36-api-recovery-before.sha256` and `cp36-api-recovery-after.sha256`. Validation used only the disposable `leadshug_channels_validation` namespace. This establishes local regression behavior; it does not claim a new provider proof or delivery acceptance.
