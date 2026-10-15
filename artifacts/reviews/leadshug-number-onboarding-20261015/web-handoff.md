# ST-CON-01 — Web checkpoint handoff

Planned handoff prepared on 2026-10-15, within the approved TODO. Start only after the API writer has delivered a stable validated checkpoint and relinquished product write ownership. Read its final DTO/env/endpoint handoff; this note is not an independent API contract or implementation claim.

Execution admission: API checkpoint2 has stopped with130unit/234E2E passing and42verified source hashes. An independent read-only review now examines its immutable snapshot. Web preparation may proceed as the only product writer, confined to Web source/build/unit checks. Do not mutate API source, browser fixtures, API generated artifacts or runtime during that review. Backend fixture wiring, real-backend Playwright and final PCV remain a later serialized step after review/adjudication; this preparation is not a completed UI delivery claim.

## Authority

Use `operational-coder`, the active TODO, owner modules and actual React/Nest boundary rules. Principal checkout, one product writer across all repositories. API branch is `feature/number-onboarding`; create the same local feature branch from the existing Web baseline before Web edits. Foundation remains `main` and root-owned. No source push, deployment, worktree, auxiliary checkout, or gitlink edits.

Allowed Web paths are the exact TODO entries: `src/telas/Numeros.tsx`, `src/api.ts`, `src/cadastroNumero*`, `src/componentes/CadastroNumero*`, `e2e/*canais*`, `e2e/number-onboarding*`, and `playwright.config.ts`. API browser fixtures may be adjusted only in their already admitted paths and with the sole writer role transferred. Other paths require evidence and admission before editing. `Inbox.tsx`, manual new conversation, templates and history import remain excluded.

## User flow

- Replace manual WABA prompts and the old channel-create/QR GET calls with the new number-registration journey. Create a BU atomically through the registration endpoint, or select an administrable existing BU. Use its per-BU role for existing-number actions; use the Mantenedora role for new BU creation.
- Show unavailable modality reasons from capabilities. Do not request app secret, access token or encryption key from the ordinary operator. Do not silently choose the first WABA/phone. Support explicit WABA selection and number-page continuation, preserving the selected page cursor for confirmation.
- Load the Meta SDK only as needed. Keep the actual popup-opening `FB.login` tied to a direct user gesture; avoid awaiting a registration request inside that click before opening a popup. The earlier step can reserve the attempt/nonce. Use the public app/config/version from capabilities.
- Correlate callbacks with the exact current attempt/nonce and client lifecycle. Accept only the approved exact Meta origins and supported message shape. postMessage IDs are hints; confirmation uses the server-validated options. Popup cancel/error, BU switch, unmount and a newer attempt invalidate old callbacks and replies.
- Keep code and PIN transient. No URL, storage, trace, screenshot or console containing them. Clear sensitive fields when their lifecycle ends. Automated browser fixtures use fictitious values and must not capture real authorization or QR material.
- Pairing is administrative POST with the existing CSRF header. Display QR only to the authorized operator. Explain RENEW interrupts acceptance until the new own-number identity is confirmed. Pending QR refresh/retry must preserve the server's current attempt/epoch rather than create a second instance.
- Display registration, provider connection and receipt separately. A QR, list response, `open` event or WABA subscription alone cannot produce a success claim. Expose safe retry/verify/reauthorize/cancel actions according to the actual state and error catalog.
- Preserve existing classes/layout, grants and timeline refresh behavior. Do not introduce another UI library, route family or manual contact creation.

## Browser proof

Use the built Web bundle and real API, session and disposable PostgreSQL database. Only the external provider/SDK port may be replaced. Never intercept BFF responses to simulate a successful flow. Keep all existing timeline tests meaningful.

The existing browser server, fixture server and timeline freshness helper guard the disposable `leadshug_timeline_*` database family. A separate name within that family can preserve those safeguards for this checkpoint; do not weaken the guard or repoint fixtures to an operational database. The global timeline freshness helper is outside the allowed edit list: compose it with an allowed `number-onboarding*` helper if additional attestation is needed. Disable registration-flow tracing that would persist code/PIN request bodies; keep real authorization and pairing out of automated trace/screenshot capture.

Capture freshness before workers: exact branches/SHAs plus dirty source hashes, built assets, served target, and served-versus-built hash comparison. The source already has a timeline freshness helper; add a number-onboarding helper in the allowed glob and compose/reuse existing behavior without editing unrelated historical tests.

Cover both modalities, disabled capabilities, explicit multi-number selection and continuation, session/role denial, popup cancel/error, stage failure/retry, double click, stale responses after BU switch/unmount, and receipt arriving between mapping and subscription. For the high-severity FRC lane use20 repeated triggers×5 repetitions with observable requests/in-flight and final state; include a negative control that detects a deliberately stale client observation. Do not replace behavior proof with unit-only checks.

REG-SEC-11 also requires echo-first rendering: the provider send stub awaits an actual webhook before returning its result, then the existing inbox refresh must show the trusted author/content on the same Message.id. If the current Inbox fails that observation, capture the failure and return to root for scope admission; do not silently edit the excluded file.

## Exit

Deliver final DTO usage, owned-file list, build/unit/Playwright results with raw evidence/source hashes, unresolved gaps, and exact runtime handles. Runtime/ingress edits belong to a later serialized DevOps handoff. Real Meta/app/HTTPS/phone proof remains separate; do not mark the governing TODO complete.
