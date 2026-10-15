# Checkpoint 4 — Web lifecycle remediation

Status: bounded Web remediation implemented and validated; product writes are stopped for root adjudication. No API, API fixtures, generated output, browser/E2E, package, runtime/config, or shared dependency paths were edited. No commit or push was made.

## Source

- Checkout: `web-app`, branch `feature/number-onboarding`, baseline `4e56f6c1f4515b918d05b8c87e890d42e8542c56`.
- Owned paths: `src/telas/Numeros.tsx`, `src/api.ts`, `src/api.spec.ts`, `src/cadastroNumero.ts`, `src/cadastroNumero.spec.ts`, `src/componentes/CadastroNumero.tsx`.
- SHA-256 manifest: `checkpoint4-web-source-hashes.sha256`.
- Validation log: `checkpoint4-web-validation.log`.

## Remediation

The Meta SDK readiness flag is now independent of attempt invalidation, so reserving an attempt does not strand the authorization control in its loading state. Durable attempts remain active when the panel closes; an authorized administrator can resume from the safe BU projection, which reloads the attempt DTO and current options. The wizard polls the active attempt at five-second intervals, bounded to 60 reads, and rejects stale updates after lifecycle or attempt changes. A nonce is retained only in component memory for the current mounted session; when it cannot be recovered after reload, the UI offers explicit cancellation and a fresh reservation instead of inventing or persisting it. Popup callbacks are correlated to the attempt and lifecycle, and `FB.login` remains synchronous in the click handler.

Same-payload reservation retries reuse the same in-memory Idempotency-Key; changed intent rotates it. Confirmation consumes the API's `{ registration: attempt }` envelope. Meta message parsing accepts a bounded JSON string or object only after exact origin validation, rejects malformed/array/unknown-schema events, and treats IDs as hints. When a selected-WABA page returns one WABA, the previously loaded authorized WABA choices remain available while only number results and cursor are replaced.

## Validation

Ran in `node:22.23.3-slim` with the existing isolated Web dependency volume `leadshug-number-onboarding-web-node-modules`:

```text
npm run build
npm test
```

Production build passed. Vitest passed 4 files and 25 tests. Focused helper coverage includes exact-origin/schema and bounded JSON event parsing, idempotency-key reuse/rotation, confirmation envelope unwrapping, and the request-header boundary. The first validation attempt caught two unmatched parentheses in the new parser tests; those were fixed before the passing run recorded in the final log.

## Remaining gates

- No Playwright/browser or real-backend integration was run. Later browser proof should cover reload/resume with a safe attempt projection, close-without-cancel, current-attempt polling, multi-WABA selection and WABA switching across number pagination, and popup gesture/correlation behavior.
- No real Meta or Evolution provider call, credential, phone-number change, QR capture, or deployment occurred. Meta Embedded Signup event serialization/origin behavior has not been certified against a live configured app; Meta developer documentation was rate limited during source review.
- Independent API review/adjudication, browser integration, PCV, provider proof, and final TODO acceptance remain pending.
