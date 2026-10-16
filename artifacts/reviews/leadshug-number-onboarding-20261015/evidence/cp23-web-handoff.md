# CP23 Web recovery handoff

Web CP23 completed its authorized work and is at terminal STOP. No commits or pushes were made.

## Change

- `web-app/src/componentes/CadastroNumero.tsx`: recovery after `CANCELLED`, `EXPIRED`, or `AMBIGUOUS_CODE_EXCHANGE` refreshes the authoritative unit projection while retaining operation ownership and checking the captured attempt lifecycle. It resumes as `REAUTORIZAR` only when the exact retained channel, type, generation, and current attempt still match. It submits `NOVO` only after an authoritative cancelled attempt has released its channel and the fresh projection has no slot for that type. Missing or mismatched projection state fails safe before clearing the prior lifecycle.
- `web-app/e2e/number-onboarding.spec.ts`: adds real BFF/session/PG coverage for expiry and ambiguous exchange; expiry also checks unauthenticated `403`, wrong-BU `404`, and unchanged `PENDING_AUTH` state before the authorized exact-scope fixture action. Both cases require a `201` `REAUTORIZAR` request and response for the same BU/channel/generation, a distinct attempt, nonce, and idempotency key, one channel slot, and no duplicate BU. Ambiguous exchange verifies no repeated fixture exchange call. Recovery submit locators accept the UI's existing reservation and reauthorization labels.
- `api-app/test/timeline-fixtures.cjs`: the authorized test-only expiry fixture correction validates attempt IDs as 32 hexadecimal characters, matching the API's existing ID generator; BU UUID validation and fixture authorization/scope predicates remain unchanged.

## Validation

- Preserved genuine pre-product browser RED: `cp23-web-red-confirmed.log`, SHA-256 `c8ff6a514631556fe1cbfd42a4aac11cb676d8e912909b0aba73454c27f3c1cc`. Both scenarios reached the recovery request and got `409 CHANNEL_SLOT_OCCUPIED` with the old NOVO behavior. Earlier fixture-scope and visibility-wait harness failures remain separately preserved in the earlier `cp23-web-red-browser*.log` evidence; they were not treated as product RED.
- Final canonical browser command: `bash scripts/test-channels-local.sh browser`, exec session `48343`, exit 0, 46/46 passed. Both new cases logged response 201, `REAUTORIZAR`, same BU/channel, expected generation 1. The existing controlled `meta.exchange` fixture failure was observed in the ambiguous test and that test passed. This run's stdout was not tee-captured to a complete byte-exact raw file; only available session output was observed. It is recorded this way and is not represented as a complete raw log. The earlier `cp23-web-green-browser.log` is the distinct post-fix selector-mismatch run and is not the final GREEN evidence. Root's later integrated final run can supersede the browser stdout capture limitation without repeating this browser run here.
- Final canonical Web command: `bash scripts/test-channels-local.sh web`, exec session `18532`, exit 0. TypeScript/Vite build passed and Vitest passed 5 files / 28 tests. Complete tee log: `cp23-web-final-green-web.log`, SHA-256 `109da24ff9b687a3cd2e8d5a1ecc7f1a5b6f268dc96d4b9127082963fe2797af`.
- For both final runs, distinct pre/post curated manifests cover 230 public references with identical file hashes and identical source heads. Each manifest declares zero private or operational paths read or hashed. The sole known missing path is the approved deleted `api-app/src/domain/channels/channels.service.spec.ts`.
- Source heads remained: root `cab23188ec796f79131467dcce0a16acedab8d4f`, API `ae6a9662c29b77276351aa9de653a47276372246`, Web `4e56f6c1f4515b918d05b8c87e890d42e8542c56`, all on `feature/number-onboarding`.
- Final owned-source SHA-256: `web-app/src/componentes/CadastroNumero.tsx` `9afbe4f419dcf4b5133f8103a0082b6eaa32837aaaf307ffbc61489c50f8cb78`; `web-app/e2e/number-onboarding.spec.ts` `4076adf4405bc61818d985e1550fe49d7662862884843e5846b3e16be54acea3`; `api-app/test/timeline-fixtures.cjs` `1372f7bfb38792bffa948411208a5cc60abb4dffbecfa118e913abdfd38a07fb`.

## Manifest evidence

- Browser: `cp23-web-final-green-source-manifest-before.json` and `cp23-web-final-green-source-manifest-after.json`.
- Web build/unit: `cp23-web-final-web-source-manifest-before.json` and `cp23-web-final-web-source-manifest-after.json`.
- Earlier post-fix browser selector mismatch evidence remains untouched as `cp23-web-green-browser.log` with its own earlier pre-manifest.
