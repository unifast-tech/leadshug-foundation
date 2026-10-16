# Web checkpoint 14 handoff

Status: Web source writer stopped pending the API fixture provenance correction and a serialized browser rerun.

The Web production changes and browser scenarios are prepared. The isolated Node 22 `web` runner passed TypeScript/Vite build and all 28 Vitest assertions. The last `browser` run executed all 44 cases with one worker: 42 passed and 2 failed.

The idempotent response-loss case preserved the same request key and payload. Its second real BFF response was HTTP 403 with allowlisted code `TENANT_ADMIN_REQUIRED`, no attempt or nonce, and the UI's generic safe recovery copy. The actual response metadata is in the raw run log. Root adjudicated the fixture seed's OWNER provenance as the cause: it uses direct grant provenance, so a newly created BU does not receive the founder's inherited tenant role. The Web test must keep requiring a successful same-attempt/same-session replay with a recoverable nonce; do not weaken authorization or rewrite this test around the 403. Retest after the API fixture owner corrects the seed provenance.

The FRC case verified 20 repeated submit events now coalesce into one reservation request after the synchronous operation-owner guard. Its stale-read/cancel assertion exposed a second product defect: a legitimate server cancellation releases `channelId`, but the lifecycle owner rejected that authoritative DTO. The lifecycle now admits only a monotonic same-attempt/same-BU/same-type `CANCELLED` action DTO with stage `CANCELLED` and `channelId: null`; it continues rejecting a late read and later channel reattachment. A focused lifecycle assertion covers this rule. The full FRC browser proof remains pending a post-fix rerun.

Browser cases that passed include explicit WABA selection with null names, pagination cursor use, popup cancel/error/abandon, SDK retry, role refusal, ambiguous Meta subscription without automatic replay, QR scoping, early-IN refusal, authenticated Evolution echo and inbox refresh, the updated BU/modality screen, and existing timeline coverage. The prior run also passed the theme persistence case after adding a real PUT-success and persisted-GET barrier before reload. The current run's only failure outside onboarding is the replay fixture blocker described above; all other cases passed.

The browser harness uses the real BFF, session and PostgreSQL with provider-only fixtures and the SDK test double. The run applied 21 migrations and used one Playwright worker. Trace, screenshot and video capture are disabled. No live Meta/Evolution provider behavior is certified by these tests.

Evidence files:

- Raw browser runs: `cp14-browser-validation.log`, `cp14-browser-validation-rerun1.log` through `cp14-browser-validation-rerun5.log`.
- Final run summary and safe replay metadata: `cp14-browser-validation-rerun5.log` (42/44; 403 replay cause).
- Latest pre-worker freshness attestation: `cp14-preworker-freshness-rerun5.json`.
- Unit/build log after the lifecycle cancellation fix: `cp14-web-unit-build-rerun1.log` (28/28 tests passed).
- Source hash manifest: `cp14-web-source-hashes.sha256`.

Hashes:

- Source manifest SHA-256: `5ac633782a230fffa377be07a64aa73518a67b8dad66d299af03a67980e0d1be`.
- Final browser log SHA-256: `8b51de50bb8d224fba3616417ec40893d06c6719f492d9756ee3409f02a85fb1`.
- Unit/build log SHA-256: `a7dc078145418e252aabdae3486673d8cb26034d66d011d62833f62d1ab732a2`.
- Pre-worker freshness SHA-256: `287342201d69452aeccd2183c3aea965f61268aca6578ca8a2a404f932d5c16a`.
