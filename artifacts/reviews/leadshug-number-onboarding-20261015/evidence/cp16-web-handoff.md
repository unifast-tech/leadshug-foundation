# Web checkpoint 16 handoff

Status: Web source writer stopped; browser validation is green and ownership can pass to the serialized DevOps phase.

`bash scripts/test-channels-local.sh browser` completed successfully on Node 22.23.3. The runner built the Web bundle, started the real API and fixture services, migrated the isolated PostgreSQL database through all 21 migrations, and executed all 44 Playwright cases with one worker. Trace, screenshot and video capture were disabled. The run exercised real BFF/session/PostgreSQL flows with provider-only fixture controls and an SDK test double; it does not certify live Meta or Evolution behavior.

The response-loss case recorded safe metadata only: the same request key and payload replayed HTTP 201 for the same attempt, with a nonce present, `PENDING_AUTH`, stage `RESERVED`, version 1. No nonce value or popup code was logged. The `FRC-EVIDENCE` line records five waves of 20 submit triggers: one reservation request and one in-flight request per wave, maximum in-flight 1. The held real stale-read response finished after cancellation; the UI remained cancelled.

The green suite includes explicit choice between null-name WABAs, page cursor use, popup cancel/error/abandon, SDK retry, BU switching and stale callbacks, same-session same-key recovery after response loss, role refusal, no automatic mutation replay after ambiguous Meta subscription, QR/current-pair scope, early-IN refusal, authenticated Evolution echo with stable message ID/author after inbox refresh, the BU/modality screen and existing timeline cases. The identity visual check waits for the real successful PUT and persisted theme before reload.

Evidence:

- Browser log: `cp16-browser-validation.log` — SHA-256 `e36b8cd2176e9e9a4df63df28480fb772ce58c6bce0f3210f991c4dc559bd02e`.
- Pre-worker freshness manifest: `cp16-preworker-freshness.json` — SHA-256 `102ff86a05f74e8a11924cb6949e1fbdb414d9d96d19d21792cbdf31f7cbfb40`.
- Timeline served-bundle/source attestation: `cp16-timeline-attestation.json` — SHA-256 `b4be732e6aea45abb872acb8cf5ee149eb99e13c0df35727469ef8c4d4ecca63`.
- Post-run Web source SHA-256 manifest: `cp16-web-source-hashes.sha256` — SHA-256 `5ac633782a230fffa377be07a64aa73518a67b8dad66d299af03a67980e0d1be`.
- Web build and unit log from the final source set: `cp14-web-unit-build-rerun1.log` — 28/28 tests passed; SHA-256 `a7dc078145418e252aabdae3486673d8cb26034d66d011d62833f62d1ab732a2`.

The API writer's additional regression tests from cp15 were not run by this Web browser command and are not claimed as passed. No Web source changes were made after the green run.
