# TODO - LeadsHug: CI contract, migration and E2E test gates

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`

## Approval

- **Approved by:** Gabriel / user - 2026-08-31
- **Approval scope:** strengthen TODO governance so every implementation that changes API responses, database schema, migrations, environment topology or user flows updates the corresponding contract tests and validates the same commands/configuration used by GitHub Actions.
- **Renewed approval:** Gabriel / user - 2026-09-23 — `APROVADO` para editar exclusivamente `foundation_documentation/project_constitution.md` e `delphi-ai/templates/todo_template.md`, resolver `CI-CRIT-003`/`CI-CRIT-004`, revalidar e fechar este TODO.
- **Authority:** `leadshug-foundation` governa o contrato; `leadshug-engineering` fornece método e guardas; Codex executa e Claude Code revisa.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `none`
- **Next exact step:** publicar o pacote Foundation e validar a crítica independente e a revisão final sobre os commits congelados antes do closeout.

## Active Work State

- **Work state:** `review`
- **Why this state now:** as duas correções autorizadas foram implementadas; resta publicar/congelar Foundation e concluir as revisões independentes.
- **Exit condition:** correções implementadas, publicadas nos dois repositórios, crítica/final review limpas e guards em `go`.

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
| Foundation | `.` | `763e759f7682259d61cb28102e76e377aaa8db08` | `working_tree` |
| Engineering | `../delphi-ai` | `2662e3aedd70d89d74a924be5834ed3cdea59a39` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `todos/active/process/TODO-ci-contract-and-migration-test-gates.md` | `M, D, R` | revalidar o registro legado e removê-lo de `active/` no closeout |
| Foundation | `todos/completed/process/TODO-ci-contract-and-migration-test-gates.md` | `A, M, R` | destino governado do mesmo TODO após gates verdes |
| Foundation | `project_constitution.md` | `M` | explicitar trigger migration-only e paridade Playwright/CI específica do LeadsHug |
| Engineering | `templates/todo_template.md` | `M` | tornar os dois gates genéricos e reutilizáveis no template Engineering |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `modules/**` | `any` | nenhum módulo pertence ao closeout deste TODO |
| Foundation | `contracts/**` | `any` | nenhum contrato adicional será criado nesta revalidação |
| Foundation | `artifacts/**` | `any` | o pacote usa comandos e referências versionadas, sem novo artefato persistente |
| Engineering | `rules/**` | `any` | a correção aprovada pertence somente ao template |
| Engineering | `workflows/**` | `any` | nenhum workflow será alterado |
| Engineering | `tools/**` | `any` | nenhum guard/tool será alterado |
| Engineering | `skills/**` | `any` | nenhuma skill será alterada |
| Engineering | `foundation_documentation/**` | `any` | documentação interna do Engineering fora do escopo |

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
| `S03` | Scope | Require migration validation whenever Prisma schema or migration files change. | doc | Prisma schema/migration contract em `foundation_documentation/project_constitution.md:21`; migration evidence em `delphi-ai/templates/todo_template.md:140` at `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` | local documentation | passed | Schema ou migration file agora acionam comando aplicável de validation/deploy/migration-state e database evidence. |
| `S04` | Scope | Require response-shape expectation updates whenever API projections or DTOs change. | doc | `foundation_documentation/project_constitution.md:20`; API projection/DTO evidence em `delphi-ai/templates/todo_template.md:142,322` | local documentation | passed | O contrato exige atualização de contract-test expectation no mesmo TODO. |
| `S05` | Scope | Require Playwright to use the same `DATABASE_URL`, API port and refreshed web build as CI. | doc | Playwright web/build contract em `foundation_documentation/project_constitution.md:22-23`; Playwright web provenance/parity em `delphi-ai/templates/todo_template.md:146` at `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` | documentary CI/runtime contract | passed | LeadsHug exige `DATABASE_URL` e API port/endpoint iguais ao job CI-equivalent; template exige comparação redigida e agnóstica dessas identidades/configurações. |
| `S06` | Scope | Require evidence of the exact CI commands before TODO closeout. | doc | `delphi-ai/templates/todo_template.md:328-335` — exact Local CI-Equivalent command and evidence columns | local documentation | passed | Evidência agregada não substitui comando e cenário específicos. |
| `D01` | Definition of Done | Future TODOs explicitly identify affected contracts and their tests. | doc | `delphi-ai/templates/todo_template.md:137-153,321-335` — contract/test and flow/CI matrices | local documentation | passed | O template exige critério e evidência específicos. |
| `D02` | Definition of Done | Future TODOs explicitly identify migration and environment validation when applicable. | doc | `foundation_documentation/project_constitution.md:21-23`; `delphi-ai/templates/todo_template.md:140,146,338` at `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` | local documentation | passed | Contrato explícito para migration e environment parity; structure-only, sem navigation/browser própria para esta edição documental. |
| `D03` | Definition of Done | Future TODOs cannot claim completion with aggregate test evidence only. | doc | `delphi-ai/templates/todo_template.md:137-153` — aggregate summaries are supporting notes only | local documentation | passed | A matriz exige prova 1:1 por critério e validation step. |
| `D04` | Definition of Done | Process changes are documented in canonical Foundation/Engineering sources. | review | `foundation_documentation/project_constitution.md:20-23` + `delphi-ai/templates/todo_template.md:137-153,321-335` at `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` | local documentation | passed | Regra específica está na Foundation; método reutilizável e sem hard-code de projeto está no Engineering. |
| `VAL-01` | Validation Steps | Inspect updated constitution and TODO template. | review | `nl -ba foundation_documentation/project_constitution.md`; `nl -ba delphi-ai/templates/todo_template.md` executados em 2026-09-23 | local documentation | passed | Inspeção confirmou invariantes nas linhas 20-23 e matrizes nas linhas 137-153/321-335. |
| `VAL-02` | Validation Steps | Run authority and completion guards on this TODO. | test | `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/active/process/TODO-ci-contract-and-migration-test-gates.md --require-delivery-gates`; `python3 delphi-ai/tools/todo_completion_guard.py foundation_documentation/todos/active/process/TODO-ci-contract-and-migration-test-gates.md --require-delivery` | `foundation_documentation:main` local checkout | passed | Executados em 2026-09-23: authority/completion deram `go` antes da crítica; após integrar blockers, completion deve retornar `no-go` até S03/S05/D02/D04 serem satisfeitos. |

## Complexity

- **Level:** `small`
- **Checkpoint policy:** `consolidated`
- **Why this level:** revalidação e closeout de governança documental existente, sem alteração de produto, testes, runtime ou pipeline.

## Profile Scope & Handoffs

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack; delphi-self-maintenance`
- **Expected supporting profiles:** `routine-executor; assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/project_constitution.md delphi-ai/templates/todo_template.md`

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `Strategic / CTO-Tech-Lead` | `routine-executor / delphi-self-maintenance` | a constituição é autoridade estratégica; o template Engineering é uma superfície agnóstica de execução | `foundation_documentation/project_constitution.md`; `delphi-ai/templates/todo_template.md` | completed; Engineering `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` |
| `routine-executor / delphi-self-maintenance` | `Assurance / Tester-Quality` | crítica e revisão final precisam validar as duas correções após publicação | TODO + duas fontes canônicas | active após publicação Foundation |

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
- **Critique status:** `running`
- **Findings summary:** cinco findings: `CI-CRIT-001/002/005` integrados; `CI-CRIT-003/004` autorizados para implementação e aguardando revalidação independente.
- **Evidence / reference:** `/root/ci_gate_closeout_critique`, 2026-09-23; `overall_assessment=material_findings_present; not ready for closeout`.
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** a crítica precisa avaliar um pacote versionado e imutável.
- **Trigger stage:** `before the retrospective independent critique`
- **Baseline branch:** `main`
- **Baseline commit:** `7dcdecf37b98613af4f235fb1c207cde680366e2`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** pacote de revalidação congelado e publicado sem mudanças fora do TODO.
- **Evidence / reference:** conteúdo congelado em `foundation_documentation:main@7dcdecf37b98613af4f235fb1c207cde680366e2`; registro do freeze em `f4bf50e6fc23b779ee0c480dc779fc7cacb7d840`, ambos publicados em `origin/main` em 2026-09-23.
- **Waiver authority / reference:** `n/a`

## Independent Test Quality Audit Gate

- **Audit decision:** `not_needed`
- **Why this decision:** nenhum teste, assertion, fixture, runner ou comportamento de produto mudou.
- **Trigger signals in scope:** `none`
- **Required evidence matrix:** `n/a`
- **Audit status:** `not_run`
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
- **Findings summary:** será executada sobre o pacote corrigido e publicado.
- **Evidence / reference:** `pending corrected package`
- **Waiver authority / reference:** `n/a`

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | governa a execução pelo TODO | autoridade e gates | fechar com evidência implícita | manter o TODO ativo até guards verdes |
| `delphi-ai/workflows/docker/todo-delivery-gates-method.md` | governa evidência de entrega | prova 1:1 e auditorias derivadas | aggregate-only claims | substituir as antigas alegações genéricas |
| `delphi-ai/workflows/docker/todo-closeout-promotion-method.md` | governa o movimento final | disposition e publicação | mover antes do commit/push | executar closeout em duas etapas |
| `delphi-ai/skills/ci-equivalent-governance/SKILL.md` | o TODO usa o termo CI-Equivalent | comandos exatos e branch autoritativa | chamar smoke genérico de CI-equivalent | registrar `n/a` para esta revalidação docs-only |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | a autorização renovada abre implementação documental | recorte aprovado e single-writer | ampliar objetivo ou criar worktree | authority guard deve permanecer `go` |
| `delphi-ai/skills/rule-docker-shared-foundation-docs-sync-model-decision/SKILL.md` | Foundation e Engineering precisam permanecer coerentes | autoridade específica do projeto sobre regra genérica | hard-code de projeto no template agnóstico | regra específica na constituição; gatilho reutilizável no template |

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
| Foundation documentary closeout | somente Markdown no repositório Foundation; nenhum job/suite de produto foi tocado | `n/a — no product CI surface in this documentary-only diff` | closeout | n/a | `git diff --check` + guards determinísticos listados em Validation Steps | A antiga alegação genérica `task check`/Playwright foi retirada porque não possuía artefato nem branch@sha; não é reutilizada como CI-Equivalent. |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| Foundation documentary package | consistência documental e qualidade da evidência | n/a | bounded package encaminhado à revisão independente | none | O diff não altera workflow de CI e não há finding P1/P2 aberto; findings documentais da revisão final serão classificados antes do closeout. |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| CI-Equivalent evidence hygiene | claim genérico sem comando, branch@sha ou artefato | passed | remoção das linhas históricas `task check`/Playwright e substituição por `n/a` docs-only | alegação histórica fraca encontrada | Integrada nesta revalidação; nenhum produto foi declarado validado. |
| Contract/migration parity | regra ausente nas fontes canônicas | passed | `project_constitution.md:20-23`; `delphi-ai/templates/todo_template.md:140,146` at `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` | none after remediation | `CI-CRIT-003/004` integrados sem hard-code de projeto no template Engineering. |

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `CI-GATE-REVAL-001` | medium | release-blocker | integrar evidência específica e remover falsa alegação CI-equivalent | mesmo TODO; afeta diretamente a validade do closeout | resolved | revalidação de 2026-09-23; matrizes deste arquivo |
| `CI-CRIT-001` | high | release-blocker | corrigir SHA e separar baseline de conteúdo do commit de freeze | mesmo TODO; erro de rastreabilidade | resolved | baseline `7dcdecf37b98613af4f235fb1c207cde680366e2`; freeze `f4bf50e6fc23b779ee0c480dc779fc7cacb7d840` |
| `CI-CRIT-002` | medium | release-blocker | registrar comandos exatos e outcomes | mesmo TODO; evidência do VAL-02 | resolved | Completion Evidence Matrix `VAL-02` |
| `CI-CRIT-003` | medium | release-blocker | ampliar regra canônica para mudanças em migration files | mesmo TODO; obrigação aprovada não satisfeita | resolved | `project_constitution.md:21`; Engineering `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` |
| `CI-CRIT-004` | medium | release-blocker | explicitar paridade de `DATABASE_URL` e API port no Playwright | mesmo TODO; obrigação aprovada não satisfeita | resolved | `project_constitution.md:23`; Engineering `55ead9bd457db5d5e10ffbfb363d138ae88bfacb` |
| `CI-CRIT-005` | low | release-blocker | usar qualifier canônico | mesmo TODO; schema de status | resolved | `Qualifiers: Provisional+Blocked` |

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
- **Why this outcome:** `CI-CRIT-003/004` foram resolvidos nas fontes canônicas; o helper anterior marcou vocabulário estrutural do próprio TODO, sem dívida inline de código.
- **Inline code TODO debt:** `none`
- **Evidence / audit artifact:** `tr -d '\r' < delphi-ai/tools/verification_debt_audit.sh | bash -s -- --repo foundation_documentation --todo todos/active/process/TODO-ci-contract-and-migration-test-gates.md --scan-git-modified`, 2026-09-23; heurística `high`, adjudicada 1:1.
- **Accepted residual debt:** `none`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** implementação documental concluída; publicação Foundation e revisões independentes ainda estão em andamento.
- **Post-commit/push status:** `Engineering published at 55ead9bd457db5d5e10ffbfb363d138ae88bfacb; Foundation implementation package pending publication`
- **Next path/status action:** publicar Foundation, validar a crítica e a final review independentes e mover para `todos/completed/process/` se os guards estiverem verdes.
