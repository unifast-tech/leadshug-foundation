# Checkpoint 3 — Web preparation handoff

Status: bounded Web implementation and unit/build validation complete. Product writes stopped after validation. The API snapshot remains untouched during independent review; browser/API integration, PCV and real provider proof remain later serialized gates.

## Source

- Checkout: `web-app`, branch `feature/number-onboarding`, baseline `4e56f6c1f4515b918d05b8c87e890d42e8542c56`.
- Owned paths changed: `src/telas/Numeros.tsx`, `src/api.ts`, `src/api.spec.ts`, `src/cadastroNumero.ts`, `src/cadastroNumero.spec.ts`, `src/componentes/CadastroNumero.tsx`.
- Source hashes: `checkpoint3-web-source-hashes.sha256` (all six changed source files).
- Validation log: `checkpoint3-web-validation.log`.

The new guided flow reserves attempts with an idempotency key, uses existing BU roles or tenant admin for atomic BU creation, loads safe capability reasons, opens the official Meta SDK popup synchronously from the user click, correlates the one-use nonce to the current attempt, and presents explicit WABA/phone/page selection. PIN and authorization code stay transient in component state/closures. Existing channel state now distinguishes identity, provider connection and receipt. Evolution pairing uses the POST action with expected generation on renewal, displays its QR only ephemerally, follows replacement attempt IDs, and calls out identity/receipt and ambiguous-operation states. No old WABA prompt, retired channel-create POST, QR GET, or unscoped/global token path remains in the screen.

## Validation

Ran in `node:22.23.3-slim`, using separate Web dependency volume `leadshug-number-onboarding-web-node-modules`:

```text
npm ci
npm run build
npm test
```

Final result: production build passed; 4 Web test files and all 23 unit tests passed. New unit coverage checks exact Meta origin/schema filtering and the idempotency-header request boundary. `npm ci` reported 9 dependency audit findings (5 moderate, 2 high, 2 critical); dependency manifests and lockfile were not changed.

## Gaps held for later gates

- No Playwright/browser test, real-backend integration or API fixture change in this checkpoint.
- No Meta or Evolution provider call, real credential, phone, QR capture or deployment.
- The later browser lane must disable tracing/screenshots for tests that exercise transient code, PIN or QR. Existing `playwright.config.ts` tracing remains unchanged; do not use its retain-on-failure trace for those flows.
- Final PCV, independent API review adjudication and complete TODO acceptance remain pending.
