# TODO - LeadsHug: Typebot automation integration

## Approval

- **Approved by:** user (2026-09-01)
- **Approval scope:** define and implement the first bounded integration between LeadsHug and Typebot for automations/chatbots, preserving LeadsHug authority over tenants, users, contacts, conversations and WhatsApp channels.
- **Authority:** `delphi-ai` executes and validates this TODO.

## Delivery Status Canon

- **Current delivery stage:** `In-Progress`
- **Qualifiers:** approved; enhancement-scope-recorded; automated-checks-green; real-channel-validation-pending
- **Next exact step:** validate one real Typebot flow through an official WhatsApp number; automated implementation and regression checks are complete.

## Active Work State

- **Work state:** `review`
- **Why this state now:** the approved management slice and automated validation are complete; the TODO remains active for one external official-channel proof and for an undecided correlation/delivery/failure audit contract.
- **Exit condition:** the real official Typebot exchange is confirmed and the correlation/retry/audit decision is approved and implemented, or the latter is split into a separately approved TODO.

## Objective

Enable LeadsHug users to create, configure and operate Typebot automations/chatbots from the LeadsHug ecosystem, with tenant isolation, permission enforcement, conversation traceability and a path to send/receive through the official WhatsApp API.

## Proposed Authority Boundary

- LeadsHug remains authoritative for Mantenedoras, users, roles, Business Units, contacts, conversations, channel credentials and audit history.
- Typebot remains authoritative for bot flow editing, nodes, variables and bot execution state only where explicitly delegated.
- Integration contracts must identify the LeadsHug account/BU and correlation ID on every bot-triggered conversation or action.
- No Typebot capability may bypass LeadsHug tenant scope, permissions or official channel rules.

## Decisions Required Before Execution

- [x] Hosting: Typebot Cloud, using the user's existing Starter account.
- [x] Initial surface: provide a Typebot management screen inside LeadsHug and open the Cloud editor in a new tab from that flow; direct editor iframe embedding is not supported by the selected Cloud setup.
- [x] First release: complete integration, including chatbot execution and automations.
- [x] Channel scope: official WhatsApp only in the first release.
- [x] Ownership: bots belong to the Mantenedora.
- [x] Data policy: the bot may perform the actions required by its approved flows through LeadsHug contracts, with tenant scope, permissions, official-channel rules and audit enforced by LeadsHug.
- [x] Activation model: provide a LeadsHug trigger-management screen so the user can configure how each bot operates.
- [x] Bot discovery: search by bot name or ID.
- [x] Bot creation: open the Typebot Cloud creation flow in a new tab from LeadsHug.
- [x] Inline trigger UX: configure each bot's trigger beside its editor action.

### Consolidated approved direction

The first release will integrate Typebot Cloud into LeadsHug through a management screen and server-side Typebot contracts. The Cloud editor opens in a new browser tab from the LeadsHug flow. Mantenedoras will own the bots. The integration will support the complete approved automation surface, but execution will be limited to official WhatsApp and to actions exposed by LeadsHug's governed contracts. A trigger screen in LeadsHug will configure bot activation and routing. LeadsHug remains authoritative for account scope, permissions, contacts, conversations, channel credentials, delivery and audit.

The implementation must not expose Typebot credentials in the browser, must not allow a bot to bypass LeadsHug authorization, and must define the exact trigger/action catalog before coding the runtime.

### Newly requested enhancement boundary

The three management improvements above are part of this TODO's next delivery slice. The unofficial WhatsApp channel remains a separate unapproved scope: it requires Evolution validation, a channel authority decision and separate security, delivery and regression tests. Lack of an official physical device does not authorize mixing it into the official runtime.

## Scope

- [x] Define the Typebot integration contract and initial lifecycle states (`ATIVO`/`INATIVO`).
- [x] Define tenant/BU mapping and permission model: bots belong to the Mantenedora; triggers may target all eligible official BUs or one BU owned by that Mantenedora; administrative BFF routes enforce Mantenedora ADMIN.
- [x] Add secure backend-only Typebot Cloud configuration (`TYPEBOT_API_URL`, `TYPEBOT_API_TOKEN`, `TYPEBOT_WORKSPACE_ID`) without exposing the token to the browser.
- [x] Implement bot registration, connection and status management through the Typebot workspace catalog and local bot status.
- [x] Implement the first approved trigger/action flow for new conversations and keyword text responses through official Meta.
- [ ] Persist correlation, delivery and failure audit records in LeadsHug.
- [x] Add unit tests for Typebot client contracts, trigger matching, session start/continue and Meta response dispatch.
- [x] Add API contract, authorization, integration and Playwright tests for the approved flow.
- [x] Document local, staging and production topology and required environment variables.

## Acceptance Criteria

- [x] A Mantenedora ADMIN can search the Typebot workspace catalog by bot name or ID.
- [x] The management screen can open Typebot Cloud creation in a new tab and each bot editor in a new tab.
- [x] Each bot exposes inline trigger configuration for `NOVA_CONVERSA` and `PALAVRA_CHAVE`.
- [x] Trigger writes preserve Mantenedora/BU isolation, require an official connected channel for a selected BU, and create an activity record transactionally.
- [x] The official inbound text flow starts or continues a Typebot session and sends text replies through the existing Meta contract.
- [x] Typebot credentials remain on the API and provider unavailability degrades to an explicit recoverable UI state.
- [ ] One real Typebot flow is validated with a real official WhatsApp message in the target environment.

## Validation Steps

- [x] Run `task check`.
- [x] Run `task test:e2e` against PostgreSQL and the applied Prisma migrations.
- [x] Run `task test:tela` against the built Web and API processes.
- [x] Run `npm run test:cov` in `apps/api`.
- [x] Run the Typebot-focused unit and BFF regression tests.
- [x] Run the Delphi rule-spirit scan for the changed LeadsHug API/Web surfaces.
- [ ] Send and observe one real Typebot response through an official WhatsApp number.

### Execution evidence

- Prisma models and migration added for `typebot_bots` and `typebot_triggers`.
- Backend Typebot Cloud adapter added using the documented `GET /typebots?workspaceId=...` contract.
- Authenticated workspace query validated successfully; current workspace returned 14 bots.
- Administrative BFF status route added at `GET /api/bff/integracao/typebot`.
- API TypeScript build passed after the first integration slice.
- Typebot runtime bridge added for active keyword/new-conversation triggers, persisted sessions, bot replies through `MetaClient`, and conversation history registration.
- Prisma session migration and published Typebot ID mapping added.
- API unit suite passed: 93 tests.
- Current automated API unit suite passed: 103 tests in 16 files.
- `task check` passed: lint, API/Web typecheck, API unit tests, Web unit tests and 56 guardrail checks.
- `task test:e2e` passed against the local PostgreSQL after applying all 17 migrations.
- Web production build passed.
- Runtime event test added for Meta → Typebot → Meta, including session creation, bot output dispatch and conversation persistence.
- Editor URL corrected to the current Cloud route `https://app.typebot.com/typebots/{typebotId}/edit`; regression test added after the first generated URL returned `404 NOT_FOUND`.
- `task check` passed again after the editor URL correction and BFF fallback: 103 API unit tests, 16 Web tests and 56 guardrails.
- Real official-WhatsApp Typebot execution is still pending; no production message was sent by automated tests.
- Requested next UX slice recorded: bot search, Typebot Cloud create action and per-bot inline trigger configuration.
- Corrigido o link de criação do Typebot Cloud: a rota baseada somente no workspace
  retornava `404 NOT_FOUND`; o contrato agora usa a rota oficial
  `https://app.typebot.com/typebots/create`, com testes de cliente, BFF e tela
  atualizados para impedir regressão.
- Bot search now filters the workspace catalog by name or ID without exposing the Typebot token.
  - Bot creation opens the official Typebot Cloud `/typebots/create` route in a new tab; each catalog bot opens the current `/typebots/{id}/edit` route in a new tab.
- Trigger configuration is inline per bot and supports `NOVA_CONVERSA` or `PALAVRA_CHAVE`, with active/inactive state and official-BU validation.
- Trigger create/status writes are transactional with the LeadsHug activity catalog; cross-tenant bots and BUs are rejected.
- Playwright coverage added for the Typebot screen, including search, creation/editor links and trigger save; API runtime coverage proves Meta → Typebot → Meta with session persistence.
- BFF catalog fallback added: a Typebot network/TLS failure returns `indisponivel=true` with an empty catalog instead of HTTP 500, and the Web shows a recoverable warning.
- Final local evidence: `task check` green (103 API unit tests, 16 Web tests, 56 guardrails), `task test:e2e` green (217/217), `task test:tela` green (20/20), and `npm run test:cov` green (320/320, 90.19% statements).

## Out of Scope Until Separately Approved

- [x] Embedding the Typebot Cloud editor directly inside LeadsHug; the supported UX is a new tab launched from the LeadsHug management flow.
- [ ] Replacing LeadsHug conversations or contact records with Typebot storage.
- [ ] Supporting unofficial WhatsApp through Evolution.
- [ ] Arbitrary code execution or unrestricted external webhooks from bots.

## Definition of Done

- [x] Hosting and integration boundary decisions are approved and recorded.
- [x] Tenant and BU isolation is enforced and tested.
- [ ] Approved bot lifecycle and trigger/action flow work end to end through a real external Typebot/official WhatsApp exchange.
- [x] Secrets remain server-side and are not exposed in browser payloads.
- [x] Official WhatsApp behavior remains within existing LeadsHug contracts.
- [ ] Failure, retry, idempotency and audit behavior are defined and tested.
- [x] Every automated test created by this TODO passes, including unit, API authorization/contract boundaries, integration and browser tests, against the declared local topology.
- [x] No test is skipped, weakened or removed to obtain approval; any intentional exception requires a new user decision.
- [x] `task check` and CI-equivalent application checks pass.
- [ ] Delphi-ai authority, completion and closeout guards pass.
- [ ] Completion evidence matrix is filled with all criteria passed before closeout.

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `apps/api` job | API source, Prisma schema/migrations, Typebot client and runtime changed | `task check`; `task test:e2e`; `npm run test:cov` in `apps/api` | code and migrations present | passed | `task check`; `task test:e2e` 20 files/217 tests; `npm run test:cov` 36 files/320 tests, 90.19% statements | Matches API lint, build, migration, unit, E2E and coverage gates. |
| `apps/web` job | Typebot management UX and Playwright flow changed | `task check`; `task test:tela` | API build and local PostgreSQL healthy | passed | `task test:tela`: production build and 20/20 browser tests | Includes search, new-tab and trigger-save regression. |
| `.claude/hooks` job | Guardrails inspect changed API/Web boundaries and documentation reminders | `task hooks:test` | changed surfaces available | passed | `task check`: 56 guardrails, 0 failures | No guardrail was bypassed or weakened. |
| Prisma migration gate | Typebot tables are schema-owned delivery surfaces | `task db:deploy` | PostgreSQL container healthy | passed | `task test:e2e`: 17 migration versions found and database schema is current | Local topology uses PostgreSQL at `127.0.0.1:55433`. |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| GitHub CI API package | P1/P2 regressions in API build, migration, unit, E2E and coverage path | passed | `.github/workflows/ci.yml`; `task check`; `task test:e2e`; `npm run test:cov` | No P1/P2 findings; all local equivalents passed. | Remote execution remains a promotion check after push; no remote pass is asserted here. |
| GitHub CI Web and guardrails package | P1/P2 regressions in Web build/browser flow and deterministic hooks | passed | `.github/workflows/ci.yml`; `task test:tela`; `task check` | No P1/P2 findings; 20/20 browser tests and 56 guardrails passed. | Provider failure is handled by the explicit BFF fallback. |

## Rule-Spirit Anti-Pattern Hunt

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| LeadsHug API/Web changed surfaces | Secret leakage, browser-owned provider calls, tenant bypass and test-only shortcuts | passed | Delphi `rule_spirit_anti_pattern_scan.sh --repo ... --stack docker --path apps/api/src --path apps/web/src --path apps/web/e2e` | 22 heuristic review findings, max severity `review`; no blocker findings. | Findings are local URL/test fixtures or validation regexes; no unresolved high-priority bypass was found. |
| Typebot delivery package | Confirm new-tab UX and provider fallback do not bypass server authority | passed | `integracao.controller.ts`; `Typebot.tsx`; focused Typebot tests | No blocker findings; token is not returned to Web and Cloud failure no longer becomes a 500. | Keep the real provider exchange as the explicit manual validation gate. |

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | Define the Typebot integration contract and initial lifecycle states (`ATIVO`/`INATIVO`). | code + test | `apps/api/prisma/schema.prisma`; Typebot client tests | local | passed | Enums, adapter contract and regression tests exist. |
| SCOPE-02 | Scope | Define tenant/BU mapping and permission model: bots belong to the Mantenedora; triggers may target all eligible official BUs or one BU owned by that Mantenedora; administrative BFF routes enforce Mantenedora ADMIN. | code + test | `integracao.controller.ts`; existing BFF access tests; `task test:e2e` | local | passed | Queries and validation are scoped by Mantenedora and official BU. |
| SCOPE-03 | Scope | Add secure backend-only Typebot Cloud configuration (`TYPEBOT_API_URL`, `TYPEBOT_API_TOKEN`, `TYPEBOT_WORKSPACE_ID`) without exposing the token to the browser. | code + docs | `apps/api/.env.example`; `docs/artifacts/env.yml`; Web browser BFF contract | local | passed | Token is consumed only by the API client and is absent from the browser response. |
| SCOPE-04 | Scope | Implement bot registration, connection and status management through the Typebot workspace catalog and local bot status. | code + test | Typebot BFF routes; Prisma `typebot_bots`; `integracao.typebot.spec.ts` | local | passed | Remote catalog is reconciled into the Mantenedora-owned local catalog. |
| SCOPE-05 | Scope | Implement the first approved trigger/action flow for new conversations and keyword text responses through official Meta. | integration test | `incoming.typebot.integration.spec.ts`; `task test:e2e` | local | passed | Session start/continue and Meta text dispatch are covered with persisted conversation output. |
| SCOPE-06 | Scope | Persist correlation, delivery and failure audit records in LeadsHug. | design decision | No approved correlation/retry/failure contract exists yet | production | blocked | Requires a new explicit product/architecture decision before schema and runtime changes. |
| SCOPE-07 | Scope | Add unit tests for Typebot client contracts, trigger matching, session start/continue and Meta response dispatch. | test | `typebot.client.spec.ts`; `incoming.typebot.spec.ts`; `incoming.typebot.integration.spec.ts` | local | passed | Focused Typebot tests pass. |
| SCOPE-08 | Scope | Add API contract, authorization, integration and Playwright tests for the approved flow. | test | `integracao.typebot.spec.ts`; `task test:e2e`; Playwright `task test:tela` | local | passed | BFF fallback, runtime bridge and browser management flow are covered. |
| SCOPE-09 | Scope | Document local, staging and production topology and required environment variables. | docs | `docs/artifacts/api.yml`; `docs/artifacts/schema.yml`; `docs/artifacts/env.yml` | local/stage/prod | passed | Typebot routes, models, migrations and variables are recorded without values. |
| AC-01 | Acceptance Criteria | A Mantenedora ADMIN can search the Typebot workspace catalog by bot name or ID. | browser test | `apps/web/e2e/telas.spec.ts`; `task test:tela` | local | passed | Search hides non-matching bots and restores matching results. |
| AC-02 | Acceptance Criteria | The management screen can open Typebot Cloud creation in a new tab and each bot editor in a new tab. | browser test | `apps/web/e2e/telas.spec.ts`; `typebot.client.spec.ts` | local | passed | Current editor route is `/typebots/{id}/edit`. |
| AC-03 | Acceptance Criteria | Each bot exposes inline trigger configuration for `NOVA_CONVERSA` and `PALAVRA_CHAVE`. | browser test | `apps/web/e2e/telas.spec.ts` | local | passed | Form opens beside the bot and persists the selected keyword trigger. |
| AC-04 | Acceptance Criteria | Trigger writes preserve Mantenedora/BU isolation, require an official connected channel for a selected BU, and create an activity record transactionally. | code + test | `integracao.controller.ts`; `catalogo.ts`; `cobertura.ts` | local | passed | Transaction and activity catalog are in the API boundary. |
| AC-05 | Acceptance Criteria | The official inbound text flow starts or continues a Typebot session and sends text replies through the existing Meta contract. | integration test | `incoming.typebot.integration.spec.ts` | local | passed | Both new-session and existing-session paths are covered. |
| AC-06 | Acceptance Criteria | Typebot credentials remain on the API and provider unavailability degrades to an explicit recoverable UI state. | unit + browser test | `integracao.typebot.spec.ts`; `Typebot.tsx`; `task test:tela` | local | passed | Network/TLS failure returns `indisponivel` instead of HTTP 500. |
| AC-07 | Acceptance Criteria | One real Typebot flow is validated with a real official WhatsApp message in the target environment. | manual external validation | Typebot Cloud workspace + official WhatsApp number | stage/prod | blocked | Requires an available official number and user confirmation of the received reply. |
| DOD-01 | Definition of Done | Hosting and integration boundary decisions are approved and recorded. | TODO decision | Approval section and consolidated approved direction | foundation | passed | Typebot Cloud/new tab/official-only/Mantenedora ownership are recorded. |
| DOD-02 | Definition of Done | Tenant and BU isolation is enforced and tested. | code + test | BFF validation and existing cross-tenant E2E suites | local | passed | No provider catalog or trigger query crosses the Mantenedora scope. |
| DOD-03 | Definition of Done | Approved bot lifecycle and trigger/action flow work end to end through a real external Typebot/official WhatsApp exchange. | manual external validation | Real Typebot start/continue and Meta receive/send proof | stage/prod | blocked | Local automated flow passes; external channel proof is still required. |
| DOD-04 | Definition of Done | Secrets remain server-side and are not exposed in browser payloads. | code review + test | Typebot client and BFF response contract | local | passed | Browser receives URLs/catalog data only. |
| DOD-05 | Definition of Done | Official WhatsApp behavior remains within existing LeadsHug contracts. | integration test | `IncomingService`; `MetaClient`; Typebot runtime tests | local | passed | Typebot replies are dispatched by the existing official Meta adapter. |
| DOD-06 | Definition of Done | Failure, retry, idempotency and audit behavior are defined and tested. | design decision | No approved full delivery/correlation contract | production | blocked | Requires user decision before implementing persistent execution/audit semantics. |
| DOD-07 | Definition of Done | Every automated test created by this TODO passes, including unit, API authorization/contract boundaries, integration and browser tests, against the declared local topology. | test | `task check`; `task test:e2e`; `task test:tela`; `npm run test:cov` | local | passed | 103 API unit, 16 Web unit, 217 API E2E, 20 browser and 320 coverage tests passed. |
| DOD-08 | Definition of Done | No test is skipped, weakened or removed to obtain approval; any intentional exception requires a new user decision. | review | Git diff/test review; guardrails | local | passed | No Typebot test was skipped or weakened. |
| DOD-09 | Definition of Done | `task check` and CI-equivalent application checks pass. | test | `task check`; `task test:e2e`; `task test:tela`; `npm run test:cov` | local | passed | All recorded application gates pass. |
| DOD-10 | Definition of Done | Delphi-ai authority, completion and closeout guards pass. | guard | `todo_authority_guard.py`; `todo_closeout_guard.py`; completion guard output | foundation | blocked | Authority and closeout are being refreshed after this matrix update; completion remains blocked by open criteria. |
| DOD-11 | Definition of Done | Completion evidence matrix is filled with all criteria passed before closeout. | TODO closeout | This matrix plus blocked AC-07/SCOPE-06/DOD-03/DOD-06 rows | foundation | blocked | Closeout cannot claim complete while external validation and audit contract remain open. |
| VAL-01 | Validation Steps | Run `task check`. | command | `task check` | local | passed | 103 API unit, 16 Web unit and 56 guardrails passed. |
| VAL-02 | Validation Steps | Run `task test:e2e` against PostgreSQL and the applied Prisma migrations. | command | `task test:e2e` | local | passed | 20 files and 217 tests passed; all 17 migration versions were current. |
| VAL-03 | Validation Steps | Run `task test:tela` against the built Web and API processes. | command | Playwright `task test:tela` | local | passed | Web build succeeded and 20/20 browser tests passed. |
| VAL-04 | Validation Steps | Run `npm run test:cov` in `apps/api`. | command | `npm run test:cov` | local | passed | 36 files and 320 tests passed; 90.19% statements. |
| VAL-05 | Validation Steps | Run the Typebot-focused unit and BFF regression tests. | command | `npx vitest run src/surfaces/bff/integracao.typebot.spec.ts src/integrations/typebot/typebot.client.spec.ts` | local | passed | 6 focused tests passed. |
| VAL-06 | Validation Steps | Run the Delphi rule-spirit scan for the changed LeadsHug API/Web surfaces. | guard | Delphi `rule_spirit_anti_pattern_scan.sh` | local | passed | 22 review-level heuristic findings, no blocker or P1/P2. |
| VAL-07 | Validation Steps | Send and observe one real Typebot response through an official WhatsApp number. | manual external validation | Typebot Cloud + official WhatsApp | stage/prod | blocked | Awaiting available official number and user confirmation. |

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | governs TODO execution | approved boundary and evidence | implementation before decisions | stop at decision gate |
| `delphi-ai/rules/stacks/nestjs/leadshug-backend.md` | governs API/integration work | tenant scope and server authority | browser-held secrets | add contract/security tests |

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** implementation-validation
- **Selected role:** routine-executor
- **Selected model:** gpt-5.6-terra
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Writer scheduling policy:** one writer in canonical checkout; reviewers read-only
- **Guard outcome:** go

## Next Action

Delphi-ai may execute the TODO and will stop only if a new product or security decision is required.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** the approved UX/runtime slice is implemented and locally green, but external official-channel validation and the not-yet-decided correlation/delivery/failure audit semantics remain actionable.
- **Post-commit/push status:** `pending`
- **Next path/status action:** keep in `active/features/` until the two remaining gates are resolved; then refresh the completion matrix and move to `completed/features/` only after all closeout guards pass.
