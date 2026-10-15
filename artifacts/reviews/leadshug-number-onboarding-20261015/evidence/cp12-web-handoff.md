# CP12 Web handoff

Status: Web product writes STOPPED pending the serialized API fixture correction and one final browser run. No API, runner, runtime, private environment, operational payload, Inbox, package/lockfile source or source history was edited. No commit or push was made.

## Changes prepared

- Playwright child-server fixture Graph versions are both `v26.0`, matching API cp8.
- Shared timeline freshness uses a `HEAD` diff with explicit public pathspecs for source, tests, schemas/migrations, build/test config, Docker and public assets. `.local-files` and private dotenv files are excluded. The manifest explicitly says omitted operational payloads are not source deletions. DB family, health and served-versus-built hash checks remain.
- Popup abandonment remains enabled while its popup operation owns pending state and invalidates late callbacks. Unnamed WABAs render `Conta <public WABA ID>` without auto-selection.
- Added popup cancel/error/abandon, SDK retry, late callback after close/BU switch, lost-response same-intent new-BU retry, and two-null-name WABA tests. Updated the single admitted legacy Números case to verify the BU/no-channel state, guided registration entry, explicit modality choices, and the real noncontracted-module reason/disabled action.
- Strengthened FRC evidence to wait for the held real GET's `requestfinished` event plus a UI drain, and to print one `[FRC-EVIDENCE]` JSON record with 5 waves, 20 triggers/wave, actual request and in-flight counts, and final stale-control state. Added an SDK test double to the FRC reservation case.
- The echo-inside-send UI test now verifies the trusted `owner` attribution and, after reopening the Inbox, asserts the same rendered message ID and attribution.

## Browser run evidence

The first cp12 attempt built the API and started the real fixture/API/preview servers, ran freshness global setup, then failed at test discovery because this Playwright version does not support `test.describe.use`. That raw output is preserved in `cp12-browser-validation.log`.

After switching to supported file-level `test.use({ trace: 'off', screenshot: 'off', video: 'off' })`, the serialized browser run completed 44 tests: 35 passed, 2 failed, and 7 onboarding tests were skipped by the serial suite after the first onboarding failure. The 35 passing tests include the existing timeline suite. The first failure confirms the API fake transforms configured `wabaName: null` into `Fixture WABA`, so Web cannot yet prove the actual null-name fallback. This was independently verified by root from the frozen fixture source; I made no API edit. The second failure was the legacy Números test expecting the retired `Conectar WABA` action; its narrowly admitted replacement is prepared above but was edited after this run and has not been executed.

Raw completed run: `cp12-browser-validation-rerun1.log`, SHA-256 `5a79a960e53d715db0e1f2f1d4b786cb011fbaed28404dec6f60c088bf7f4e3c`. Earlier attempt log: `cp12-browser-validation.log`, SHA-256 `263aa9e2b0e9cff31e9c282f5408e5cd19b50a788463235f7fa2d030b1a5c954`.

The runner's pre-worker freshness record was emitted at `artifacts/tmp/number-onboarding-execution/pre-worker-freshness.json` (SHA-256 `7531f261589ef8cf9236fd6d8c8d7ba60efa9f7f2bec98d1222d80f754ccc3f0`). It records the public API/Web source manifests, declared baselines, disposable DB and served bundle check for the run's source snapshot. It predates the post-run E2E-only corrections listed above, so it is not attestation for the final current hashes. The current post-run Web source hash inventory is `cp12-web-source-hashes.sha256`; all 14 files verify. API cp8 pre/post manifests remain the root-verified unchanged 153-file pair.

The build embedded in the browser runner passed for Web. The earlier cp10 source-owned Web runner also passed production build and 27 unit tests; cp12 changes after that point are Playwright test/config only. The supported whitespace check `git -c core.whitespace=cr-at-eol diff --check` passed, preserving the existing CRLF format of the one touched legacy test file.

## Limits and next owner

No onboarding browser case passed through its meaningful flow after the first null-name fixture assertion, so FRC evidence, popup lifecycle cases, null-name display behavior, QR identity/receipt and echo-inside-send attribution remain pending. Do not claim local browser acceptance or external provider proof. API must first preserve the fixture's explicitly configured null WABA name (source adapter contract returns `name: null`); then return Web ownership for the final serialized browser run. The possible second API build in Playwright did not produce a race: fixture, API and preview all started and the 44-test suite ran.
