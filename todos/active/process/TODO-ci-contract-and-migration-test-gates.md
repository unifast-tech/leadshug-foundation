# TODO - LeadsHug: CI contract, migration and E2E test gates

## Approval

- **Approved by:** Gabriel / user - 2026-08-31
- **Approval scope:** strengthen TODO governance so every implementation that changes API responses, database schema, migrations, environment topology or user flows updates the corresponding contract tests and validates the same commands/configuration used by GitHub Actions.
- **Authority:** `leadshug-foundation` governa o contrato; `leadshug-engineering` fornece método e guardas; Codex executa e Claude Code revisa.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `validated-local`
- **Next exact step:** validar as evidências registradas, executar os guards de delivery e closeout e decidir se este TODO deve ser movido para `todos/completed/process/`.

## Active Work State

- **Work state:** `review`
- **Why this state now:** the process changes and local evidence are recorded, but this TODO remains in `active/` until its historical evidence is revalidated against the current guards and a governed closeout disposition is confirmed.
- **Exit condition:** authority, completion and closeout guards return `go`, then the TODO is either moved to `todos/completed/process/` or kept active with a concrete unresolved review action.

## Scope

- [x] Update LeadsHug constitution with contract/migration/CI/E2E parity requirements.
- [x] Update the Engineering TODO template with mandatory CI-equivalent and contract-test checks.
- [x] Require migration validation whenever Prisma schema or migration files change.
- [x] Require response-shape expectation updates whenever API projections or DTOs change.
- [x] Require Playwright to use the same `DATABASE_URL`, API port and refreshed web build as CI.
- [x] Require evidence of the exact CI commands before TODO closeout.

## Definition of Done

- [x] Future TODOs explicitly identify affected contracts and their tests.
- [x] Future TODOs explicitly identify migration and environment validation when applicable.
- [x] Future TODOs cannot claim completion with aggregate test evidence only.
- [x] Process changes are documented in canonical Foundation/Engineering sources.

## Validation Steps

- [x] Inspect updated constitution and TODO template.
- [x] Run authority and completion guards on this TODO.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Scope | Update LeadsHug constitution with contract/migration/CI/E2E parity requirements. | doc | project_constitution.md | local | passed | |
| S02 | Scope | Update the Engineering TODO template with mandatory CI-equivalent and contract-test checks. | doc | todo_template.md | local | passed | |
| S03 | Scope | Require migration validation whenever Prisma schema or migration files change. | doc | template persistence gate | local | passed | |
| S04 | Scope | Require response-shape expectation updates whenever API projections or DTOs change. | doc | template contract-test gate | local | passed | |
| S05 | Scope | Require Playwright to use the same `DATABASE_URL`, API port and refreshed web build as CI. | doc | template browser parity gate | local | passed | |
| S06 | Scope | Require evidence of the exact CI commands before TODO closeout. | doc | template CI-equivalent matrix | local | passed | |
| D01 | Definition of Done | Future TODOs explicitly identify affected contracts and their tests. | doc | updated template | local | passed | |
| D02 | Definition of Done | Future TODOs explicitly identify migration and environment validation when applicable. | doc | updated template | local | passed | |
| D03 | Definition of Done | Future TODOs cannot claim completion with aggregate test evidence only. | doc | completion evidence rules | local | passed | |
| D04 | Definition of Done | Process changes are documented in canonical Foundation/Engineering sources. | review | constitution and template changes | local | passed | |

## Rules Acknowledgement / Ingestion
| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `leadshug-engineering/workflows/docker/todo-delivery-gates-method.md` | governs delivery evidence | exact commands and artifacts | aggregate-only claims | require matrices |
| `leadshug-engineering/rules/stacks/nestjs/leadshug-backend.md` | governs Prisma/API changes | schema and contract alignment | drift between code and tests | require migration tests |

## Agent Routing Preflight
- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-5.6-terra
- **Selected effort:** medium
- **Proof mode:** declared
- **Guard outcome:** go

## Local CI-Equivalent Suite Matrix
| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| LeadsHug API | contract and migration checks | task check | closeout | passed | API suite and Prisma build | |
| LeadsHug Web | browser contract | task check and Playwright | closeout | passed | web suite and Playwright | |

## Pipeline/Copilot P1/P2 Preflight
| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| CI contract gates | missing test/migration parity | n/a | process rule update | no findings | no separate pipeline surface |

## Rule-Spirit Anti-Pattern Hunt
| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| Contract parity | changed response without expectation update | passed | PR failure analysis | found and formalized | template gate added |
| Migration parity | schema changed without deploy validation | passed | PR failure analysis | found and formalized | constitution gate added |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** the implementation is recorded as local and validated, but the evidence and current deterministic closeout requirements still need revalidation before movement.
- **Post-commit/push status:** `pending closeout revalidation`
- **Next path/status action:** validate the existing evidence with the current authority, completion and closeout guards; if all return `go`, move this TODO to `todos/completed/process/`.
