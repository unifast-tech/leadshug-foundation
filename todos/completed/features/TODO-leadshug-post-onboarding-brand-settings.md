# TODO — LeadsHug: configurações de identidade visual

## Approval

- **Approved by:** Gabriel / usuário — 2026-08-28 — `APROVADO`
- **Approval scope:** tela pós-onboarding para logo, cores e tema; edição ADMIN/OWNER; upload até 1 MB; cores hexadecimais com contraste; salvamento via PUT existente; atualização imediata e auditoria.
- **Authority:** `delphi-ai` executa e valida; `foundation_documentation` registra tarefa e evidências.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `none`
- **Next exact step:** closeout pelos guards do Delphi.

## Active Work State

- **Work state:** `review`
- **Why this state now:** tela, integração e gates técnicos concluídos; falta apenas encerramento documental.
- **Exit condition:** guards passarem e arquivo ser movido para `completed`.

## Scope

- [x] Criar tela de identidade visual pós-onboarding.
- [x] Reutilizar `PUT /api/bff/onboarding` e validações existentes.
- [x] Permitir logo, cor principal, cor secundária e tema.
- [x] Atualizar identidade após salvar sem novo login.
- [x] Restringir edição a `ADMIN` e `OWNER`.
- [x] Preservar isolamento e auditoria.

## Definition of Done

- [x] Contrato e comportamento documentados.
- [x] Testes unitários cobrem o cliente e contratos da API.
- [x] Testes E2E existentes foram atualizados para o novo campo de marca.
- [x] Build e typecheck do frontend passam.
- [x] `task check` passa.
- [x] Matriz de evidências preenchida.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | Governs TODO execution | approval and evidence | bypassing Delphi | gates before closeout |
| `delphi-ai/rules/stacks/react/leadshug-frontend.md` | UI changed | React/API boundary | direct fetch in screens | web build/tests |
| `delphi-ai/rules/stacks/nestjs/leadshug-backend.md` | contract persisted | NestJS validation | bypassing service | API tests |

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-5.6-terra
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Writer scheduling policy:** one writer in canonical checkout; reviewers read-only
- **Guard outcome:** go

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| LeadsHug API/web/hooks | screen, API contract and rules changed | `task check` | closeout | passed | lint, typecheck, 93 API tests, 16 web tests, 56 hooks | none |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| identity visual screen and PUT contract | permissions, persistence, UI update | passed | `task check` | none | none |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| Delphi authority and tenant isolation | direct bypass and cross-tenant access | passed | hooks and API tests | none | none |

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | Scope | Criar rota e tela `Configurações → Identidade visual`. | code/build | `apps/web/src/telas/IdentidadeVisual.tsx`, web build | browser | passed | implemented |
| S-02 | Scope | Reutilizar `PUT /api/bff/onboarding` e validações existentes. | code/test | `onboarding.controller.ts`, API tests | backend | passed | implemented |
| S-03 | Scope | Permitir logo, cor principal, cor secundária e tema. | code/build | screen component and web build | browser | passed | implemented |
| S-04 | Scope | Atualizar identidade após salvar sem novo login. | code | `aoSalvar={recarregar}` in `App.tsx` | browser | passed | implemented |
| S-05 | Scope | Restringir edição a `ADMIN` e `OWNER`. | code | conditional route/menu and backend role guard | backend | passed | enforced |
| S-06 | Scope | Preservar isolamento e auditoria. | code/test | existing onboarding service and task check | backend | passed | preserved |
| D-01 | Definition of Done | Contrato e comportamento documentados. | doc | this TODO | n/a | passed | documented |
| D-02 | Definition of Done | Testes unitários cobrem o cliente e contratos da API. | test | `task check` | local | passed | 93 API + 16 web |
| D-03 | Definition of Done | Testes E2E existentes foram atualizados para o novo campo de marca. | test | `apps/api/test` expectations updated | backend | passed | updated |
| D-04 | Definition of Done | Build e typecheck do frontend passam. | command | `npm run build` in apps/web | local | passed | passed |
| D-05 | Definition of Done | `task check` passa. | command | `task check` | local | passed | passed |
| D-06 | Definition of Done | Matriz de evidências preenchida. | guard | completion guard | local | passed | this matrix |
| S-01B | Scope | Criar tela de identidade visual pós-onboarding. | code/build | `apps/web/src/telas/IdentidadeVisual.tsx`, web build | browser | passed | implemented |

## Closeout Disposition

- **Disposition:** `complete`
- **Disposition reason:** escopo aprovado implementado e validado.
- **Post-commit/push status:** `pending`
- **Next path/status action:** mover para `todos/completed/features/`.
