# Checkpoint 6 — Web source handoff

Status: Web source preparation complete; product writes STOPPED pending the serialized DevOps/browser phase. No API, runtime, private environment, or shared generated API artifacts were changed. No commit or push was made.

## Implementation

The guided number flow uses a centralized lifecycle owner to admit only current lifecycle/action responses, while allowing explicit server-confirmed version/generation advances and safe same-BU pairing-attempt adoption. Close invalidates pending UI writes without silently canceling a durable partial registration. Explicit cancellation retains cleanup results and safe continuation guidance. Reservations preserve an idempotency key for a repeated same-payload retry after an ambiguous response and reset it for a changed intent.

The flow resumes from the safe BU `currentAttemptId` projection, reads current attempt/options from the API, and polls boundedly with lifecycle and monotonic-version checks. SDK readiness has its own retryable lifecycle; the official login call stays synchronous with the user gesture and owns the popup operation until it settles. No unconsumed `postMessage` parser/listener remains. WABA choices survive page fetches that return only the selected WABA. Confirmation consumes the actual `{ registration: TentativaNumero }` response envelope. Ambiguous provider outcomes remain pending with manual-check/fresh-authorization guidance and do not replay external mutations. Pairing QR remains ephemeral and is shown only following fresh safe-channel correlation; completion/readback uses `receiptVerified` and verified identity dimensions rather than inferring success from registration/listing alone.

All ordinary stage/error copy is Portuguese and action-oriented. No nonce, code, PIN, QR, provider token, or other secret is persisted or logged. The Web Docker build context now excludes `.env` and `.env.*`, retaining `.env.example`.

## Browser source prepared

`e2e/number-onboarding.spec.ts` prepares real-BFF/session/database Playwright cases for official setup with two WABAs and cursor paging, denied operator role, ambiguous subscribe with no duplicate external effect, 20 submissions across five individually held/released real response waves plus stale-read barrier, and unofficial pairing with pre-identity IN rejection, close/resume, safe identity verification, receipt retry, connection event, and echo-inside-send deduplication. Only the SDK/provider boundary is faked; delayed responses use the actual `route.fetch()` response. Trace, screenshot, and video capture are disabled.

`e2e/number-onboarding-freshness.ts` chains the existing timeline DB/health/served-bundle authority check, then records pre-worker Web/API changed-source inventories including staged, unstaged, untracked, deletions, declared baselines, and hashes for relevant schemas/migrations/tests/config. Deleted files have null hashes only when Git marks deletion and the file is ENOENT; other read errors fail closed. The admitted shared `e2e/timeline-freshness.ts` has the same deletion/error distinction and scoped source inventory.

These browser scenarios and freshness runner were source-prepared, not executed. No backend/browser stack or provider calls were started in this checkpoint. Runner execution, UI review, and provider proof remain pending.

## Validation

Executed in isolated Node 22.23.3 Web container with the existing dependency volume:

`npm run build && npm test && node -e '<esbuild parse of four TypeScript browser/config sources>'`

Build passed. Unit suite passed: 5 files, 27 tests. Four TypeScript browser/config sources parsed. `git diff --check` passed. A standalone `tsc` attempt over e2e sources could not run because this Web package lacks `@types/node`; no package/dependency changes were made. Playwright was not run.

## Changed source manifest

The SHA-256 manifest is `checkpoint6-web-source-hashes.sha256`; all listed files were rechecked with `sha256sum -c`. Validation output is `checkpoint6-web-validation.log`.

Touched paths: `.dockerignore`, `e2e/timeline-freshness.ts`, `e2e/number-onboarding-freshness.ts`, `e2e/number-onboarding.spec.ts`, `playwright.config.ts`, `src/api.ts`, `src/api.spec.ts`, `src/telas/Numeros.tsx`, `src/cadastroNumero.ts`, `src/cadastroNumero.spec.ts`, `src/cadastroNumero.lifecycle.ts`, `src/cadastroNumero.lifecycle.spec.ts`, `src/componentes/CadastroNumero.tsx`.

Product writer STOPPED. Await serialized DevOps runner results before any further Web edits.
