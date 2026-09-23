# TODO - LeadsHug: CI contract, migration and E2E test gates

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`

## Approval

- **Approved by:** Gabriel / user - 2026-08-31
- **Approval scope:** strengthen TODO governance so every implementation that changes API responses, database schema, migrations, environment topology or user flows updates the corresponding contract tests and validates the same commands/configuration used by GitHub Actions.
- **Authority:** `leadshug-foundation` governa o contrato; `leadshug-engineering` fornece método e guardas; Codex executa e Claude Code revisa.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `validated-local; documentary-governance-only`
- **Next exact step:** concluir a crítica retrospectiva e a revisão final independentes, integrar eventuais findings, rerodar os guards e mover este arquivo para `todos/completed/process/` se todos retornarem `go`.

## Active Work State

- **Work state:** `review`
- **Why this state now:** as regras canônicas estão publicadas, mas o registro legado precisa satisfazer a revalidação e os gates atuais antes do closeout.
- **Exit condition:** crítica e revisão final independentes concluídas, evidências revalidadas e guards de authority, completion, diff e closeout em `go`.

## Scope

- [x] Update LeadsHug constitution with contract/migration/CI/E2E parity requirements.
- [x] Update the Engineering TODO template with mandatory CI-equivalent and contract-test checks.
- [x] Require migration validation whenever Prisma schema or migration files change.
- [x] Require response-shape expectation updates whenever API projections or DTOs change.
- [x] Require Playwright to use the same `DATABASE_URL`, API port and refreshed web build as CI.
- [x] Require evidence of the exact CI commands before TODO closeout.

## Out of Scope

- [x] Alterar código de produto, schema Prisma, migrations, pipeline, runtime ou testes do LeadsHug.
- [x] Alegar execução retroativa de suites API, Web ou Playwright sem artefato rastreável.
- [x] Alterar o template de Engineering durante esta revalidação; a tarefa é comprovar o contrato publicado e fechar o registro histórico.

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `.` | `30c398252a58b1571d1de55fb3a406fd98ccf185` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `todos/active/process/TODO-ci-contract-and-migration-test-gates.md` | `M, D, R` | revalidar o registro legado e removê-lo de `active/` no closeout |
| Foundation | `todos/completed/process/TODO-ci-contract-and-migration-test-gates.md` | `A, M, R` | destino governado do mesmo TODO após gates verdes |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `project_constitution.md` | `any` | contrato canônico já publicado; esta revalidação não o altera |
| Foundation | `modules/**` | `any` | nenhum módulo pertence ao closeout deste TODO |
| Foundation | `contracts/**` | `any` | nenhum contrato adicional será criado nesta revalidação |
| Foundation | `artifacts/**` | `any` | o pacote usa comandos e referências versionadas, sem novo artefato persistente |

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
| `S01` | Scope | Update LeadsHug constitution with contract/migration/CI/E2E parity requirements. | doc | `foundation_documentation/project_constitution.md:20-23` — contract, migration, CI and E2E/Playwright invariants | local documentation | passed | Linhas versionadas desde `dbd7dded455182de6beb5803b47d8c336d440782`. |
| `S02` | Scope | Update the Engineering TODO template with mandatory CI-equivalent and contract-test checks. | doc | `delphi-ai/templates/todo_template.md:137-153,328-335` — contract-test criterion evidence and Local CI-Equivalent matrix | local documentation | passed | O conteúdo também existe em `delphi-ai` `origin/main@2f2fa7722243fc0cd5b2b0d192d2f8371b03db6f`. |
| `S03` | Scope | Require migration validation whenever Prisma schema or migration files change. | doc | `foundation_documentation/project_constitution.md:21`; schema/migration evidence também é obrigatória em `delphi-ai/templates/todo_template.md:140` | local documentation | passed | A constituição exige migration versionada, `prisma migrate deploy` e CI database validation. |
| `S04` | Scope | Require response-shape expectation updates whenever API projections or DTOs change. | doc | `foundation_documentation/project_constitution.md:20`; API projection/DTO evidence em `delphi-ai/templates/todo_template.md:142,322` | local documentation | passed | O contrato exige atualização de contract-test expectation no mesmo TODO. |
| `S05` | Scope | Require Playwright to use the same `DATABASE_URL`, API port and refreshed web build as CI. | doc | `foundation_documentation/project_constitution.md:22-23`; Playwright/refreshed web build provenance em `delphi-ai/templates/todo_template.md:146,328-335` | documentary CI/runtime contract | passed | `DATABASE_URL` e API port são parâmetros da mesma configuração de CI exigida pela linha 22; nenhum browser run é alegado por este TODO documental. |
| `S06` | Scope | Require evidence of the exact CI commands before TODO closeout. | doc | `delphi-ai/templates/todo_template.md:328-335` — exact Local CI-Equivalent command and evidence columns | local documentation | passed | Evidência agregada não substitui comando e cenário específicos. |
| `D01` | Definition of Done | Future TODOs explicitly identify affected contracts and their tests. | doc | `delphi-ai/templates/todo_template.md:137-153,321-335` — contract/test and flow/CI matrices | local documentation | passed | O template exige critério e evidência específicos. |
| `D02` | Definition of Done | Future TODOs explicitly identify migration and environment validation when applicable. | doc | `foundation_documentation/project_constitution.md:21-23`; migration/environment validation markers em `delphi-ai/templates/todo_template.md:140,338` | local documentation | passed | Desvio structure-only aprovado pelo escopo de 2026-08-31: esta regra documental não muda fluxo observável e não exige navigation/browser execution própria. |
| `D03` | Definition of Done | Future TODOs cannot claim completion with aggregate test evidence only. | doc | `delphi-ai/templates/todo_template.md:137-153` — aggregate summaries are supporting notes only | local documentation | passed | A matriz exige prova 1:1 por critério e validation step. |
| `D04` | Definition of Done | Process changes are documented in canonical Foundation/Engineering sources. | review | `foundation_documentation/project_constitution.md:20-23` + `delphi-ai/templates/todo_template.md:137-153,321-335` | local documentation | passed | Foundation e Engineering contêm as duas metades do contrato. |
| `VAL-01` | Validation Steps | Inspect updated constitution and TODO template. | review | `nl -ba foundation_documentation/project_constitution.md`; `nl -ba delphi-ai/templates/todo_template.md` executados em 2026-09-23 | local documentation | passed | Inspeção confirmou invariantes nas linhas 20-23 e matrizes nas linhas 137-153/321-335. |
| `VAL-02` | Validation Steps | Run authority and completion guards on this TODO. | test | `python3 delphi-ai/tools/todo_authority_guard.py ... --require-delivery-gates`; `python3 delphi-ai/tools/todo_completion_guard.py ... --require-delivery` | local checkout | passed | Reexecutados após a regularização final; resultados registrados no closeout deste arquivo. |

## Complexity

- **Level:** `small`
- **Checkpoint policy:** `consolidated`
- **Why this level:** revalidação e closeout de governança documental existente, sem alteração de produto, testes, runtime ou pipeline.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-ci-contract-and-migration-test-gates.md`
- **Latest TEACH evidence / artifact:** `go` em 2026-09-23, fingerprint `0355b4c97735`; critique/final review `required`, test-quality/security/performance/verification-debt/architecture/triple-review `not_needed`.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `small` | closeout documental delimitado |
| `blast_radius` | `cross-stack` | as regras orientam API, banco e Web, sem modificar esses stacks nesta entrega |
| `behavioral_change_or_bugfix` | `no` | nenhum comportamento de produto muda |
| `changes_public_contract` | `no` | governa evidência; não muda API/schema público |
| `touches_auth_or_tenant` | `no` | sem alteração de auth ou isolamento |
| `touches_runtime_or_infra` | `no` | sem runtime/infra |
| `touches_tests` | `no` | nenhum teste, fixture ou runner alterado |
| `critical_user_journey` | `no` | governança interna |
| `release_or_promotion_critical` | `no` | fechamento não promove produto |
| `high_severity_plan_review_issue` | `no` | nenhum issue card high registrado |
| `explicit_three_lane_request` | `no` | não solicitado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** piso determinístico atual; execução retrospectiva para desafiar a suficiência do contrato antes do closeout.
- **Impact signals in scope:** `cross-stack documentary governance`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** este TODO, `project_constitution.md` e `delphi-ai/templates/todo_template.md`.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** `none recorded yet`
- **Evidence / reference:** `to be recorded after the pushed review baseline`
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** a crítica precisa avaliar um pacote versionado e imutável.
- **Trigger stage:** `before the retrospective independent critique`
- **Baseline branch:** `main`
- **Baseline commit:** `7dcdecf371598ba628188a335b6b7cf298754fb0`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** pacote de revalidação congelado e publicado sem mudanças fora do TODO.
- **Evidence / reference:** `foundation_documentation:main@7dcdecf371598ba628188a335b6b7cf298754fb0`, sincronizado com `origin/main` em 2026-09-23.
- **Waiver authority / reference:** `n/a`

## Independent Test Quality Audit Gate

- **Audit decision:** `not_needed`
- **Why this decision:** nenhum teste, assertion, fixture, runner ou comportamento de produto mudou.
- **Trigger signals in scope:** `none`
- **Required evidence matrix:** `n/a`
- **Audit status:** `n/a`
- **Findings summary:** `nenhuma lógica de teste pertence ao diff documental`
- **Evidence / reference:** Audit Trigger Matrix (`touches_tests=no`, `behavioral_change_or_bugfix=no`, `changes_public_contract=no`).
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** piso determinístico atual antes de `Completed`.
- **Impact signals in scope:** `cross-stack documentary governance`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** baseline, escopo aprovado, diff documental, matriz de evidência, guards e riscos residuais.
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Review focus:** `adherence|regressions|validation evidence|security/performance residuals|elegance|structural soundness|verification debt`
- **Final review status:** `not_run`
- **Findings summary:** `none recorded yet`
- **Evidence / reference:** `to be recorded after critique convergence and deterministic guards`
- **Waiver authority / reference:** `n/a`

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | governa a execução pelo TODO | autoridade e gates | fechar com evidência implícita | manter o TODO ativo até guards verdes |
| `delphi-ai/workflows/docker/todo-delivery-gates-method.md` | governa evidência de entrega | prova 1:1 e auditorias derivadas | aggregate-only claims | substituir as antigas alegações genéricas |
| `delphi-ai/workflows/docker/todo-closeout-promotion-method.md` | governa o movimento final | disposition e publicação | mover antes do commit/push | executar closeout em duas etapas |
| `delphi-ai/skills/ci-equivalent-governance/SKILL.md` | o TODO usa o termo CI-Equivalent | comandos exatos e branch autoritativa | chamar smoke genérico de CI-equivalent | registrar `n/a` para esta revalidação docs-only |

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** formal-review
- **Selected role:** formal-reviewer
- **Selected model:** gpt-5.6-sol
- **Selected effort:** xhigh
- **Proof mode:** declared
- **Guard outcome:** go

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundation documentary closeout | somente Markdown no repositório Foundation; nenhum job/suite de produto foi tocado | `n/a — no product CI surface in this documentary-only diff` | closeout | n/a | `git diff --check` + guards determinísticos listados em Validation Steps | A antiga alegação genérica `task check`/Playwright foi retirada porque não possuía artefato nem branch@sha; não é reutilizada como CI-Equivalent. |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| Foundation documentary package | consistência documental e qualidade da evidência | n/a | bounded package encaminhado à revisão independente | none | O diff não altera workflow de CI e não há finding P1/P2 aberto; findings documentais da revisão final serão classificados antes do closeout. |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| CI-Equivalent evidence hygiene | claim genérico sem comando, branch@sha ou artefato | passed | remoção das linhas históricas `task check`/Playwright e substituição por `n/a` docs-only | alegação histórica fraca encontrada | Integrada nesta revalidação; nenhum produto foi declarado validado. |
| Contract/migration parity | regra ausente nas fontes canônicas | passed | `project_constitution.md:20-23`; `delphi-ai/templates/todo_template.md:137-153,321-335` | nenhuma ausência material | Contrato Foundation e método Engineering permanecem complementares. |

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `CI-GATE-REVAL-001` | medium | release-blocker | integrar evidência específica e remover falsa alegação CI-equivalent | mesmo TODO; afeta diretamente a validade do closeout | resolved | revalidação de 2026-09-23; matrizes deste arquivo |

## Security Risk Assessment

- **Risk level:** `none`
- **Why this risk level:** diff documental fechado ao próprio TODO; sem secrets, auth, tenant, endpoint ou runtime.
- **Attack surface in scope:** `none`
- **Attack simulation decision:** `not_needed`
- **Review evidence:** Audit Trigger Matrix e diff contract.
- **Residual security risk:** `none`

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `none`
- **Why this level:** nenhum endpoint, query, async UI, mutação, worker ou runtime muda.
- **Current delivery stage at review time:** `Local-Implemented`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `n/a — docs-only` | `before_local_implemented` | `EPS-E1` | `not_applicable` | `none` | `none` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `n/a — docs-only` | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `n/a — docs-only` | `before_local_implemented` | `BCI-INV` | `not_applicable` | `none` | `none` |
| `RLS` | `runtime-load-stress-validation` | `not_needed` | `low` | `n/a — docs-only` | `before_production_ready` | `RLS-E1` | `not_applicable` | `none` | `none` |

## Verification Debt Assessment

- **Audit outcome:** `none`
- **Why this outcome:** a única dívida material encontrada foi a evidência agregada histórica, resolvida neste mesmo registro; não há código ou testes no diff.
- **Inline code TODO debt:** `none`
- **Evidence / audit artifact:** `verification_debt_audit.sh` será reexecutado após o pacote final.
- **Accepted residual debt:** `none`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** baseline de revalidação ainda precisa ser congelada e as revisões independentes obrigatórias ainda não foram executadas.
- **Post-commit/push status:** `pending review baseline publication`
- **Next path/status action:** publicar o baseline, executar crítica e revisão final independentes, integrar findings, rerodar guards e então mover para `todos/completed/process/` se todos estiverem verdes.
