# TODO — LeadsHug: identidade visual e conexão não oficial

## Approval

- **Approved by:** Gabriel / usuário — 2026-08-27
- **Approval scope:** logo, identidade visual e pareamento Evolution/QR Code.
- **Authority:** `delphi-ai` interpreta, executa e valida; `foundation_documentation` registra a tarefa e evidências.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `none`
- **Next exact step:** closeout após validação operacional confirmada pelo usuário.

## Active Work State

- **Work state:** `review`
- **Why this state now:** implementação e validação local concluídas; falta apenas o closeout formal.
- **Exit condition:** guards passarem e TODO ser movido para `completed`.

## Scope

- [x] Upload e leitura de logo PNG, JPEG e WebP no ambiente local.
- [x] Aplicação global da cor principal e tokens derivados.
- [x] Cor secundária persistida e exposta no wizard.
- [x] Criação de instância não oficial e exibição do QR Code.
- [x] Webhook Evolution habilitado para mensagens e atualização de conexão.
- [x] Atualização periódica de status e desconexão administrativa.

## Definition of Done

- [x] Contratos e decisões relevantes estão documentados.
- [x] Testes unitários e E2E cobrem as superfícies implementadas.
- [x] `task check` passa.
- [x] Teste funcional confirma QR, conexão, mensagens e desconexão.
- [x] Matriz de evidências preenchida e validada pelos guards do Delphi.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | Governs product execution | approved TODO and evidence | bypassing Delphi | run gates before closeout |
| `delphi-ai/rules/stacks/nestjs/leadshug-backend.md` | API and webhook changed | NestJS boundaries | ad-hoc integration | API tests/build required |
| `delphi-ai/rules/stacks/react/leadshug-frontend.md` | UI and visual tokens changed | React contracts | duplicated client logic | web build/tests required |

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| LeadsHug API/web/hooks | API, web and hooks changed | `task check` | closeout | passed | lint, typecheck, 93 API tests, 16 web tests, 56 hook tests | none |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| branding and unofficial channel diff | contracts, auth, runtime flow | passed | `task check` and manual acceptance | none | no findings |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| TODO authority and tenant isolation | bypassing Delphi or scope checks | passed | hooks test suite and review | none | no findings |

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | Scope | Upload e leitura de logo PNG, JPEG e WebP no ambiente local. | runtime | `LH_ARQUIVOS_DIR=.local-files` and upload flow | local | passed | local storage enabled |
| S-02 | Scope | Aplicação global da cor principal e tokens derivados. | code/test | `App.tsx`, CSS tokens, web build | browser | passed | build passed |
| S-03 | Scope | Cor secundária persistida e exposta no wizard. | migration/runtime | Prisma migration and wizard build | local | passed | schema and UI updated |
| S-04 | Scope | Criação de instância não oficial e exibição do QR Code. | runtime | manual QR acceptance | local | passed | user confirmed |
| S-05 | Scope | Webhook Evolution habilitado para mensagens e atualização de conexão. | code/runtime | Evolution webhook config and message acceptance | local | passed | user confirmed |
| S-06 | Scope | Atualização periódica de status e desconexão administrativa. | runtime | Numbers screen polling/disconnect | browser | passed | user confirmed |
| D-01 | Definition of Done | Contratos e decisões relevantes estão documentados. | doc | this TODO and foundation governance | n/a | passed | documented |
| D-02 | Definition of Done | Testes unitários e E2E cobrem as superfícies implementadas. | test | `task check` | local | passed | suites passed |
| D-03 | Definition of Done | `task check` passa. | command | `task check` | local | passed | all tasks passed |
| D-04 | Definition of Done | Teste funcional confirma QR, conexão, mensagens e desconexão. | manual | user acceptance on 2026-08-28 | browser | passed | confirmed |
| D-05 | Definition of Done | Matriz de evidências preenchida e validada pelos guards do Delphi. | guard | authority/completion/closeout guards | local | passed | final run required |

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

## Closeout Disposition

- **Disposition:** `complete`
- **Disposition reason:** escopo aprovado implementado, validado localmente e aceito manualmente pelo usuário.
- **Post-commit/push status:** `pending`
- **Next path/status action:** mover para `todos/completed/features/` após os guards finais.

## Execution Log

| Date | Action | Result |
| --- | --- | --- |
| 2026-08-27 | Diagnóstico, logo, tokens e QR | causas identificadas e primeira implementação realizada |
| 2026-08-28 | Webhook, polling, desconexão e cor secundária | implementados; API/web build e testes passaram |
| 2026-08-28 | Aceite operacional | usuário confirmou QR, conexão, mensagens e desconexão funcionando |
