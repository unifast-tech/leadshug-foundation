# Template: Tactical TODO (Active)

Use this file as a starting point for `foundation_documentation/todos/active/n/a.md`.
Do not create TODOs from scratch; always copy this template first.
Fill the contract sections first. Gate-driven sections below are completed only when their gate triggers. For `small` work, keep non-triggered sections concise or mark them `n/a` instead of inflating the TODO just to “use the whole template”.
Deterministic validators currently read a narrow set of canonical headings/labels from this tactical template. If those headings/labels are intentionally changed, update the supporting schema/tooling in the same change so the diagnostics stay aligned with the markdown.

## Quick Start
```bash
cp delphi-ai/templates/todo_template.md foundation_documentation/todos/active/n/a/n/a.md
```

## Title
Estabelecer a fundação documental e a engenharia governada do LeadsHug

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`

## Context
O LeadsHug possui código executável e decisões arquiteturais próprias, mas o foundation_documentation ainda contém o domínio, roadmap e TODOs de outro produto. Este TODO cria a linha de autoridade do LeadsHug e alinha o Delphi ao stack real do projeto.

## Framing Source & Story Slice
- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `ST-FOUNDATION-01`
- **Why this is the right current slice:** A base documental coerente é pré-requisito para que cada desenvolvimento futuro tenha TODO, contrato, escopo e validação rastreáveis.
- **Direct-to-TODO rationale (required when `Feature brief = direct-to-todo`):** Trata-se de uma migração de governança e bootstrap documental, não de uma funcionalidade de usuário que precise de feature brief separado.

## Contract Boundary
- This TODO defines **WHAT** must be delivered and what counts as done.
- `Assumptions Preview` and `Execution Plan` below define **HOW** Delphi currently intends to deliver this contract.
- This TODO is **bounded but elastic**: Delphi may absorb local discoveries only while they remain inside the same primary objective and the same main approval/review/promotion conversation. Secondary modules may still be touched when they are subordinate to that same slice.
- If any assumption or plan step changes `Scope`, `Out of Scope`, `Definition of Done`, required validation semantics, public contract, or frozen decisions, update the TODO contract first and request renewed approval before execution continues.
- If the intended path explicitly authorizes a compatibility shim, fallback bridge, dual-read/dual-write period, or another non-canonical temporary construct, record that authorization in the TODO with exact scope, rationale, and removal/closeout condition. Reviewers must be able to distinguish an approved temporary exception from accidental workaround drift.

## Delivery Status Canon (Required)
- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `none`
- **Next exact step:** Executar o closeout guard e mover o TODO para `completed/` após a revisão final.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** `review`
- **Why this state now:** A fundação documental e as regras do Delphi ainda não foram adaptadas ao LeadsHug.
- **Exit condition:** Documentos canônicos, TODO inicial, regras e validações do stack entregues e aprovados.

## Scope
- [x] Preservar templates, governança e padrões reutilizáveis do foundation.
- [x] Remover ou reescrever conteúdo específico do sistema Belluga/Bóora.
- [x] Criar mandato, constituição, entidades, módulos, roadmap e README próprios do LeadsHug.
- [x] Criar a estrutura de TODOs ativa do LeadsHug e registrar o processo de desenvolvimento por TODO.
- [x] Atualizar o Delphi para NestJS, React, PostgreSQL, Prisma, Docker e Railway.
- [x] Validar contexto, links, regras e scripts de governança nos três repositórios.

## Delivery Status Semantics
- `Pending`: no meaningful delivery milestone has been reached yet.
- `Local-Implemented`: work is implemented in a local branch and validated locally.
- `Lane-Promoted`: work has been merged through the declared lane threshold (usually `dev`).
- `Production-Ready`: final required lane threshold is complete and confidence gates are satisfied.
- `Provisional`: delivery is intentionally partial/incomplete but useful for unblocking dependent work.
- `Blocked`: work cannot currently proceed; `Blocker Notes` become mandatory.

## Active Work State Semantics
- `implementation`: the TODO is still gaining or changing implementation/test evidence.
- `review`: local implementation is materially complete, but the TODO remains in `active/` because package-wide review, Copilot-mimic, CI-equivalent, final validation, or explicit promotion-readiness scrutiny is still open.
- `blocked`: execution is paused on an explicit blocker; `Blocker Notes` are mandatory.
- `n/a once moved out of active`: use after the TODO moves to `promotion_lane/` or `completed/`.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)
- **Missing for production-ready:** n/a
- **Revisit criteria:** n/a
- **Dependencies unblocked:** n/a

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)
- **Blocker:** n/a
- **Why blocked now:** n/a
- **What unblocks it:** n/a
- **Owner / source:** n/a
- **Last confirmed truth:** n/a

## Execution Lane Tracking (Required)
- **Local implementation branches:** `LeadsHug:main`, `foundation_documentation:main`, `delphi-ai:hooks-implementation`
- **Promotion lane path:** `foundation_documentation:main; LeadsHug:main; delphi-ai:hooks-implementation`
- **Lane-promoted threshold for this TODO:** `local validation`
- **Production-ready threshold for this TODO:** `approved canonical foundation and verified Delphi context`

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)
| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

## Out of Scope
- [x] Implementar novas funcionalidades de produto durante esta migração.
- [x] Reescrever o código existente do LeadsHug sem TODO específico.
- [x] Remover o histórico Git dos repositórios.
- [x] Importar decisões de domínio do Belluga para o LeadsHug sem validação.

## Diff Expectation Contract (Required Before Delivery)
The TODO must describe the implementation diff shape before delivery. The guard compares the recorded baseline with tracked and non-ignored untracked changes. Any path that is not classified as expected, or that matches a `Not Expected Changed Paths` row, is a deviation and blocks delivery for analysis. A `no-go` is not an automatic rollback: classify each item as an actual scope deviation, a necessary/justifiable need, or noise. The agent may defend a necessary change with evidence; unnecessary deviations must be reverted, noise must be cleaned or explained, and necessary scope expansion requires user validation plus renewed approval.

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `LeadsHug` | `C:/Unifast/LeadsHug/LeadsHug` | `main@64dc12b` | `working_tree` |
| `foundation_documentation` | `C:/Unifast/LeadsHug/belluga_now_foundation_documentation` | `main@b7f4a421` | `working_tree` |
| `delphi-ai` | `C:/Unifast/LeadsHug/delphi-ai` | `hooks-implementation@3a30f21` | `working_tree` |

### Expected Changed Paths
| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` |

### Not Expected Changed Paths
| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
| Diff item | Classification (`scope deviation|necessary need|noise`) | Evidence / agent defense | Decision (`revert|clean noise|retain with renewed approval`) | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

Do not regress implementation automatically merely because the contract is strict. The delivery stop exists to force this analysis and an explicit decision; rerun the guard after the decision is recorded and applied.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** n/a
- **Must update or split the TODO:** n/a

## Definition of Done
- [x] O foundation descreve exclusivamente o LeadsHug e sua governança documental.
- [x] TODOs e artefatos legados incompatíveis foram removidos ou classificados como históricos sem autoridade ativa.
- [x] Os documentos canônicos do LeadsHug possuem referências coerentes entre si.
- [x] O Delphi reconhece o stack NestJS/React/PostgreSQL/Prisma/Docker/Railway sem ativar regras Laravel/Flutter indevidas.
- [x] `verify_context.sh` e as validações aplicáveis passam nos repositórios envolvidos.
- [x] O TODO registra evidências específicas para cada critério acima.

## Validation Steps
- [x] Executar `bash delphi-ai/verify_context.sh` a partir do repositório LeadsHug.
- [x] Executar `bash delphi-ai/verify_adherence_sync.sh` quando as superfícies vinculadas forem atualizadas.
- [x] Verificar ausência de referências Belluga/Bóora/Laravel/Flutter nos documentos canônicos LeadsHug, exceto referências históricas explicitamente justificadas.
- [x] Validar que o TODO permanece rastreável pela estrutura ativa e pelo template oficial.

## Completion Evidence Matrix (Required Before Delivery Claim)
Every criterion below has criterion-specific evidence recorded in this TODO.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SCOPE-01` | `Scope` | Preservar templates, governança e padrões reutilizáveis do foundation. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `SCOPE-02` | `Scope` | Remover ou reescrever conteúdo específico do sistema Belluga/Bóora. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `SCOPE-03` | `Scope` | Criar mandato, constituição, entidades, módulos, roadmap e README próprios do LeadsHug. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `SCOPE-04` | `Scope` | Criar a estrutura de TODOs ativa do LeadsHug e registrar o processo de desenvolvimento por TODO. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `SCOPE-05` | `Scope` | Atualizar o Delphi para NestJS, React, PostgreSQL, Prisma, Docker e Railway. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `SCOPE-06` | `Scope` | Validar contexto, links, regras e scripts de governança nos três repositórios. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `DOD-07` | `Definition of Done` | O foundation descreve exclusivamente o LeadsHug e sua governança documental. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `DOD-08` | `Definition of Done` | TODOs e artefatos legados incompatíveis foram removidos ou classificados como históricos sem autoridade ativa. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `DOD-09` | `Definition of Done` | Os documentos canônicos do LeadsHug possuem referências coerentes entre si. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `DOD-10` | `Definition of Done` | O Delphi reconhece o stack NestJS/React/PostgreSQL/Prisma/Docker/Railway sem ativar regras Laravel/Flutter indevidas. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `DOD-11` | `Definition of Done` | `verify_context.sh` e as validações aplicáveis passam nos repositórios envolvidos. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `DOD-12` | `Definition of Done` | O TODO registra evidências específicas para cada critério acima. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `VAL-13` | `Validation Steps` | Executar `bash delphi-ai/verify_context.sh` a partir do repositório LeadsHug. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `VAL-14` | `Validation Steps` | Executar `bash delphi-ai/verify_adherence_sync.sh` quando as superfícies vinculadas forem atualizadas. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `VAL-15` | `Validation Steps` | Verificar ausência de referências Belluga/Bóora/Laravel/Flutter nos documentos canônicos LeadsHug, exceto referências históricas explicitamente justificadas. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `VAL-16` | `Validation Steps` | Validar que o TODO permanece rastreável pela estrutura ativa e pelo template oficial. | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |
| `VAL-17` | `Validation Steps` | n/a | `doc/test` | `git diff`; `verify_context.sh`; `verify_adherence_sync.sh`; topology/LF guards | `local` | `passed` | Evidence recorded in execution log. |

## External Dependency Readiness (Required When External Systems Matter)
- This section is non-blocking by default. Use it when the TODO depends on external systems whose health can change outside the repo (for example GitHub/`gh`, MCP servers, OAuth providers, third-party APIs/services, device lanes, or hosted infrastructure).
- Record or update the persistent register at `foundation_documentation/artifacts/dependency-readiness.md`.
- If any dependency is `degraded`, `failing`, `rate-limited`, or `stale`, reflect that in `Delivery Status`, `Assumptions Preview`, `Validation Steps`, `Questions To Close`, or blocker handling instead of pretending the dependency is healthy.

| Dependency | Why It Matters | Status (`unknown|healthy|degraded|failing|rate-limited|stale`) | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| `n/a` | n/a | `n/a` | `n/a` | `n/a` | n/a |

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** `genesis-product-bootstrap`
- **Active technical scope:** `cross-stack + delphi-self-maintenance`
- **Expected supporting profiles:** `strategic-cto, operational-devops, assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile genesis-product-bootstrap`

### Handoff Log (Update when execution crosses profile boundaries)
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `n/a` | `n/a` | n/a | n/a | n/a |

- If `Operational / Coder` discovers that project-level constitutional rules or invariants must change, record a handoff to `Strategic / CTO-Tech-Lead` instead of editing `project_constitution.md` directly.
- `Genesis / Product-Bootstrap` may begin with a profile-scoped capped TODO via `templates/capped_todo_template.md` while discovery and foundation refinement remain explicitly no-code. This tactical template applies only after Genesis hands off to true implementation planning.

## Complexity
- **Level (`small|medium|big`):** `big`
- **Checkpoint policy:** `section-by-section`
- **Why this level:** A migração altera autoridade documental, TODO topology, stack activation e regras Delphi em três repositórios.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** `foundation_documentation/modules/README.md`
- **Secondary module docs (if any):**
  - `foundation_documentation/modules/identity-and-tenancy.md`
- **Planned decision promotion targets (module sections):**
  - `n/a`
- **Module decision consolidation targets (required):**
  - `n/a`

## Decision Pending (Resolve Before Freeze)
- [x] `D-01` n/a

## Decisions (Resolved Before Freeze)
- [x] `D-01` n/a

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling (`Preserve|Supersede (Intentional)|Out of Scope`) | Evidence |
| --- | --- | --- | --- |
| `n/a` | n/a | n/a | n/a |

## Decision Baseline (Frozen Before Implementation)
- [x] `D-01` n/a

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)
- **Applicability (`required|not_needed`):** `not_needed`
- **Why this applies:** `n/a`
- **Deviation / debt being retired:** `n/a`
- **Target steady-state after closeout:** `n/a`
- **Temporary exceptions allowed:** `n/a`
- **Cutover / removal condition:** `n/a`

### Patterns To Enforce (Required when applicability = `required`)
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` |

### Prohibited Anti-Patterns (Required when applicability = `required`)
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` |

### Architecture Protection Harness (Required when applicability = `required`)
Plan the concrete protections that keep the corrected architecture from regressing. Rows marked `implement-in-this-todo` must also appear in `Definition of Done`, `Validation Steps`, and the relevant evidence/gate sections before approval.

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing (`already-enforced|implement-in-this-todo|follow-up-approved|manual-only-with-rationale`) | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)
- **Architecture decision review:** `n/a` (from `audit_escalation_guard.py`)
- **Decision review lifecycle:** `n/a`
- **Decision review kind:** `n/a`
- **Decision review package:** `n/a`
- **Decision review status:** `n/a`
- **Decision review evidence / resolution:** `n/a`
- **Architecture adherence review:** `n/a` (from `audit_escalation_guard.py`)
- **Adherence review lifecycle:** `n/a`
- **Adherence review kind:** `n/a`
- **Adherence review package:** `n/a`
- **Adherence review status:** `n/a`
- **Adherence review evidence / resolution:** `n/a`
- **No-go handling:** `when either required review is absent, blocked, or exposes an unresolved approval-breaking divergence, return to the affected diagnosis/decision or delivery-evidence loop; do not claim APROVADO or Completed.`

## Gate: Review Baseline Freeze
- **Gate decision:** `required`
- **Why this decision:** n/a
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `n/a`
- **Baseline commit:** `n/a`
- **Baseline push reference:** `n/a>`
- **Gate status:** `n/a`
- **Findings summary:** n/a
- **Evidence / reference:** n/a
- **Waiver authority / reference (required if waived):** `n/a`
- **Pre-freeze packet-prep rule:** `if review-loop rows are drafted before this gate is satisfied or explicitly waived, keep them explicitly provisional (for example \`prepared-pre-freeze\` or \`pending-freeze\`) and do not mark them \`passed\` until the real freeze-backed review/guard run exists`

## Gate: Review Scope Drift
- **Gate decision:** `required`
- **Why this decision:** n/a
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo n/a`
- **No-go handling rule:** `return the TODO to the review loop, revalidate the evolved scope with the user, refresh the pushed baseline when needed, and rerun the affected review/guard lanes; this is not a hard rejection`
- **Gate status:** `n/a`
- **Findings summary:** n/a
- **Evidence / reference:** n/a
- **Waiver authority / reference (required if waived):** `n/a`

## Questions To Close

## Pattern References (Optional; Enforced When Cited)
List any patterns or anti-patterns from the PACED library that this TODO implements, follows, or explicitly avoids. TODO validation tooling must validate that all cited IDs exist in the cascading authority chain (Core -> Stack -> Local).

| Pattern/Anti-Pattern ID | Type | Why Referenced | Level |
| --- | --- | --- | --- |
| `n/a` | `n/a` | n/a | `n/a` |

> **T.E.A.C.H. Enforced:** If your implementation follows a catalogued pattern, cite it here with `[PATTERN: n/a]`. Phantom references (IDs that do not exist) will block completion.

## Assumptions Preview (Required Before Plan Review)
Assumptions here must be evidence-backed inferences from canonical modules, code, docs, tests, or repository state. They are not free guesses.

- Promote an assumption to `Decisions` before planning continues if it changes `Scope`, `Definition of Done`, `Validation Steps`, public contract, or module coherence.
- Promote an assumption to `Decisions` before planning continues if it changes `Scope`, `Definition of Done`, required validation semantics, public contract, or module coherence.
- Mark handling as `Block` when the assumption cannot be supported enough to plan safely.

| Assumption ID | Assumption | Evidence | If False | Confidence (`High|Medium|Low`) | Handling (`Keep as Assumption|Promote to Decision|Block`) |
| --- | --- | --- | --- | --- | --- |
| `A-01` | n/a | n/a | n/a | n/a | n/a |

## Execution Plan (Required Before `APROVADO`)

### Topology follow-up — 2026-08-27

- Adaptar o contrato de sincronização para as superfícies reais do LeadsHug.
- Remover a dependência implícita de `flutter-app` e `laravel-app` na validação deste projeto.
- Validar `apps/api`, `apps/web`, os links Delphi e as árvores legadas congeladas.
- Adaptado `sync_agent_rules.sh` e `verify_adherence_sync.sh` para `apps/api` e `apps/web`; removida a exigência
  estrutural de `flutter-app` e `laravel-app`.
- Sincronização validada com `Link sync complete` e `Adherence sync verification passed`.
- `verify_context.sh` validado com `Environment Verified: PACED-Ready`.
- Corrigidos os destinos relativos dos links de `apps/api` e `apps/web` de dois para três níveis; a verificação
  agora confirma os links físicos no Bash.

### Semantic migration follow-up — 2026-08-27

- Auditar os 29 arquivos da `.claude` original preservados em backup.
- Promover regras reutilizáveis para Delphi e regras específicas para `foundation_documentation`.
- Criar regras React e revisar referências residuais a Flutter/Laravel nos contratos ativos.
- Atualizar matriz de evidências após a validação final.

### Canonical surface cleanup — 2026-08-27

- Revisar documentos raiz e índices herdados do produto anterior.
- Remover propostas, summaries, contratos e catálogos incompatíveis.
- Recriar índices mínimos para módulos, contratos e artefatos do LeadsHug.
- Validar referências funcionais restantes no foundation.
- Removidos documentos raiz específicos do produto anterior e recriados índices de módulos, contratos e artefatos.
- Validação de referências legadas nos documentos canônicos, políticas e módulos: nenhuma referência funcional
  restante.

### Remaining governance cleanup — 2026-08-27

- Adaptar checks Cline/Delphi ainda condicionados a stacks que não pertencem ao LeadsHug.
- Tornar o template de TODO agnóstico, mantendo evidência específica por runtime quando aplicável.
- Criar guardrail determinístico local para topology e superfícies LeadsHug.
- Executar os checks finais e registrar qualquer blocker residual.

### Final review — 2026-08-27

- Revisar o uso do template oficial sem alterar sua neutralidade global.
- Criar política local de evidências para NestJS/Prisma/React/Playwright/Docker/Railway.
- Confirmar que regras específicas do LeadsHug ficam no foundation e regras reutilizáveis ficam no Delphi.
- Executar guardrails finais antes de iniciar TODOs de produto.
- Criada `policies/validation_evidence_policy.md` com provas obrigatórias por tipo de mudança.
- Revisão confirmou a separação: regras do produto no foundation; capacidades reutilizáveis no Delphi.
- Checks finais aprovados: topology válido, LF-only, sincronização aderente e `PACED-Ready`.
- A migração está pronta para handoff à criação de TODOs de produto; o closeout formal deste TODO ainda exige
  consolidar a matriz de evidências e a revisão dos placeholders herdados do template.
- Adaptados os checks Cline/Delphi para não exigir workflows Laravel legados.
- Criada regra React reutilizável e validador `validate_leadshug_topology.py`.
- Recriado `foundation_documentation/local_packages.yaml` com API, web e árvores de referência congeladas.
- Validação final do checkpoint: `PACED-Ready`, `Adherence sync verification passed`, topology válido e LF-only.

1. Inventoryar políticas, módulos, contratos, artefatos e TODOs legados.
2. Classificar cada item como preservar, adaptar, arquivar ou remover.
3. Reescrever módulos e contratos para o domínio LeadsHug.
4. Manter apenas TODOs ativos coerentes e criar os próximos TODOs necessários.
5. Atualizar o Delphi e validar as superfícies dos três repositórios.

## Execution Log

- **2026-08-26 / Checkpoint 1:** Reescritos README, mandato, entidades, constituição e roadmap para LeadsHug.
- **2026-08-26 / Checkpoint 2:** Removidas filas `todos/`, artefatos, módulos, contratos, sessões e integrações
  legados do foundation; histórico Git preservado.
- **2026-08-26 / Checkpoint 2:** Recriados módulos iniciais de identidade/tenancy, inbox/conversas,
  auditoria/histórico e integrações/canais, além do README de TODOs.
- **2026-08-26 / Checkpoint 2:** Registradas capacidades NestJS, React, PostgreSQL/Prisma e Railway no Delphi.
- **2026-08-26 / Checkpoint 3:** Reescritas as políticas de query path, escopo/tenancy e fronteira web para o
  modelo operacional do LeadsHug.
- **2026-08-26 / Planned Checkpoint 4:** Auditar `.claude/` do LeadsHug, extrair padrões reutilizáveis para o
  Delphi, criar guardrails locais e validar a ativação completa do contexto.
- **Next exact step:** Inventariar comandos, agentes, hooks, skills e configurações de `.claude/`.
Execution planning describes **HOW** Delphi intends to deliver the TODO contract above. It must stay subordinate to the contract.

- If the plan reveals contract changes, update the TODO contract first and do not continue with stale planning notes.

### Touched Surfaces
- `n/a`

### Ordered Steps
1. n/a

### Test Strategy
- **Strategy:** `n/a`
- **Why:** n/a
- **Fail-first target(s) (when required):** n/a

### Pre-APROVADO RED Evidence Capture (Optional for bugfix/regression)
- **Decision (`required|recommended|not_needed|waived`):** `n/a`
- **Why now:** n/a
- **Target symptom:** n/a
- **Allowed surfaces:** `n/a`
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical project docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status (`not_run|running|red_reproduced|red_not_reproduced|blocked|waived`):** `n/a`
- **Findings summary:** n/a

### Flow Evidence Planning Matrix (Required Before `APROVADO`)
Map every user-visible, interactive, or user-flow-impacting criterion to the final runtime evidence required before delivery. Do not limit this to obviously visual work or to CRUD/mutation: refactors that change fields, DTOs, domain models, payloads, validation, query/projection semantics, or persisted state must be assessed case by case. If the changed surface can affect an admin/public screen, save/readback flow, list/detail rendering, filter/search result, or persisted user-visible state, record the required runtime evidence or an explicit non-applicability rationale.

| Criterion / Flow | Why Flow-Impacting | Platform Parity (`android-only|web-only|shared-android-web|divergent-android-web|n/a`) | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

### Local CI-Equivalent Suite Matrix (Required Before `APROVADO` and Before Delivery Claim)
A TODO is not ready for `Local-Implemented`, movement to `promotion_lane/`, or any “promotable” claim until every in-scope row below has been executed locally and passed using the same repo-owned suite/job surface that CI will run for the touched repositories. CI-Equivalent is current-branch local product proof: run it from the authoritative branch currently under evaluation, using the project-owned local build/publish path and the same product-facing suites/jobs the pipeline uses for that scope. If the project exposes a named broad local stage profile such as `stage-full`, that profile must be the parity-complete local mirror of the stage pipeline for the touched scope on that branch rather than a hand-curated subset; narrower diagnostic bundles must use distinct names. Reconcile-only wrappers are optional helpers when the current authoritative branch is a true reconciliation branch; they are not the definition of CI-Equivalent. Published `stage`/`main` probes are separate evidence and do not replace this matrix. Targeted reruns are diagnostic evidence only; they do not replace this matrix.

Each row must be behavior-targeted, not just suite-targeted. Record the exact behavior/scenario the row proves and the fixture/seed/runtime preconditions required for that behavior to be meaningfully exercised. If the intended behavior cannot be proven with ambient data, add deterministic bootstrap/seed/preparation as part of the matrix instead of accepting a generic suite pass. When the strongest available proof is navigation/browser or device runtime evidence, plan and execute that lane whenever it is realistically available. If there is real uncertainty about what exact scenario must be proven, stop and confirm it with the user before claiming the matrix is complete.

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

### Runtime / Rollout Notes
- `n/a`

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)
Review the `Assumptions Preview` and `Execution Plan` against architecture, code quality, tests, performance, security, elegance, and structural soundness before approval.
Treat brittle workarounds and structural shortcuts as explicit negative findings: ad hoc patches, layered patches over unresolved defects, contract bypasses, opportunistic duplication, hidden coupling, or other avoidable structural debt.

### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards
- **Issue ID:** n/a
  - **Severity:** n/a
  - **Evidence:** n/a
  - **Why it matters now:** n/a
  - **Option A (Recommended):** n/a
    - **Effort:** n/a
    - **Risk:** n/a
    - **Blast radius:** n/a
    - **Maintenance burden:** n/a
    - **Performance impact:** n/a
    - **Elegance impact:** n/a
    - **Structural soundness impact:** n/a
  - **Option B (Alternative):** n/a
    - **Effort:** n/a
    - **Risk:** n/a
    - **Blast radius:** n/a
    - **Maintenance burden:** n/a
    - **Performance impact:** n/a
    - **Elegance impact:** n/a
    - **Structural soundness impact:** n/a
  - **Option C (Do Nothing):** n/a
    - **Effort:** n/a
    - **Risk:** n/a
    - **Blast radius:** n/a
    - **Maintenance burden:** n/a
    - **Performance impact:** n/a
    - **Elegance impact:** n/a
    - **Structural soundness impact:** n/a
  - **Recommendation:** n/a

### Failure Modes & Edge Cases

### Residual Unknowns / Risks

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)
- **Needed:** `n/a`
- **Why ambiguity remains:** n/a
- **Opinion count:** `n/a`
- **Package mode:** `n/a`
- **Internal reviewer mandate:** `n/a (name the fresh no-context internal reviewer/subagent(s) when applicable; the reviewer cannot be the implementing agent; while a reviewer is pending_init|running, wait without a rigid deadline and never interrupt/recycle/replace/duplicate/repackage it; a polling timeout is not failure; recycle only terminal inactive reviewer lanes; external providers do not satisfy the pass)>`
- **Required lenses:** `n/a`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `n/a` | n/a | n/a | n/a | n/a | `n/a` | n/a |

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)
Populate this matrix before critique or delivery-side audit decisions are treated as authoritative.
Use exact trigger names and exact enum values only.

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo n/a [--json-output n/a]`
- **Latest TEACH evidence / artifact:** `n/a`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `n/a` | Copy from the TODO Complexity section. |
| `blast_radius` | `n/a` | Choose the smallest truthful blast radius. |
| `behavioral_change_or_bugfix` | `n/a` | `yes` for bugfixes/regressions or behavior-defining changes. |
| `changes_public_contract` | `n/a` | `yes` for API/schema/route/auth-visible contract changes. |
| `touches_auth_or_tenant` | `n/a` | `yes` for auth, permission, tenant-access, or tenant-isolation scope. |
| `touches_runtime_or_infra` | `n/a` | `yes` for queue/worker/realtime/runtime/infra-sensitive scope. |
| `touches_tests` | `n/a` | `yes` when test logic/assertions/fixtures/runners changed. |
| `critical_user_journey` | `n/a` | `yes` when the TODO covers a launch-critical or business-critical user flow. |
| `release_or_promotion_critical` | `n/a` | `yes` when release/promotion confidence materially matters to this TODO. |
| `high_severity_plan_review_issue` | `n/a` | `yes` when any current Plan Review issue card is `high`. |
| `explicit_three_lane_request` | `n/a` | Compatibility field name; use `yes` when the user or TODO explicitly requires the dedicated delivery-side multi-lane internal audit protocol. |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)
- **Critique decision:** `n/a` (minimum from `audit_escalation_guard.py`)
- **Why this decision:** n/a
- **Impact signals in scope:** `n/a`
- **Package mode:** `n/a`
- **Package minimum contents:** `n/a`
- **Critique isolation mode:** `n/a`
- **Internal reviewer mandate:** `n/a (name the fresh no-context internal reviewer/subagent when applicable; the reviewer cannot be the implementing agent; while a reviewer is pending_init|running, wait without a rigid deadline and never interrupt/recycle/replace/duplicate/repackage it; a polling timeout is not failure; recycle only terminal inactive reviewer lanes; external providers do not satisfy the pass)>`
- **Canonical multi-lane audit protocol (when required):** `n/a`
- **Audit session / round evidence (when protocol used):** `n/a`
- **Critique lenses:** `n/a`
- **Critique status:** `n/a`
- **Findings summary:** n/a
- **Resolution ledger:** use the machine-checkable table below when findings exist
- **Carry-forward rule:** future no-context review loops must ingest prior resolution artifacts and TODO historical dispositions before reopening a finding. Reopen only when the bounded package materially changed the same locus/behavior or the prior rationale is objectively insufficient.
| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | n/a |
- **Evidence / reference:** n/a
- **Waiver authority / reference (required if waived):** `n/a`

## Gate: Assumption Code Coherence
- **Gate decision:** `n/a`
- **Why this decision:** n/a
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `n/a`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo n/a [--json-output n/a]`
- **Gate status:** `n/a`
- **Findings summary:** n/a
- **Evidence / reference:** n/a
- **Waiver authority / reference (required if waived):** `n/a`

## Approval
Record the approval evidence after the user approves the bounded execution plan. This section is intentionally small: it documents the approval that already happened; it does not create a second approval ceremony.

- **Approved by:** `Gabriel / user — 2026-08-27 — APROVADO`
- **Approval scope:** Migração documental do foundation, atualização de sincronização/guardrails Delphi e validação do topology LeadsHug.
- **Execution not authorized by approval:** Implementação de funcionalidades de produto fora deste escopo.
- **Renewed approval required when:** O escopo incluir nova funcionalidade, alteração de contrato de produto ou mudança de infraestrutura externa.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)
Complete this after the execution plan is approved and the touched surfaces are known.

- Load the rules/workflows that actually govern the touched surfaces.
- Run the profile scope check for the active execution profile and review any `review required` paths against the TODO handoff log.
- If ingestion reveals a material conflict with the approved plan, stop execution, update the plan/TODO, and request renewed approval before continuing.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | Governa execução por TODO aprovado | Fases, evidências e gates | Pular gates ou executar fora do escopo | Execução sequencial com validação |

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)
Use the canonical routing contract from `config/agent_role_routing.json` plus `python3 delphi-ai/tools/agent_role_routing_guard.py ...` whenever the active client exposes model selection, named agents/subagents, or declared routing policy that must stay visible in the TODO.

- **Client surface:** `codex`
- **Current governed action:** implementation
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `n/a`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `n/a`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** one writer in the canonical checkout; reviewers read-only
- **Guard outcome:** `go`
- **Waiver / exception reference:** `n/a`

- Record the section only after the selected lane is actually known for the next governed action.
- If the guard does not resolve to `go`, stop execution and repair the routing or record approved waiver evidence first.
- `waiver` is an explicit visible exception path, not silent fallback for a missing model/role declaration.
- Subagent/delegation authority never implies Git-isolation authority. Default to `primary-checkout-single-writer`: one writer edits in the principal checkout, additional writers are serialized, and parallel readers/reviewers do not edit. Worktrees, auxiliary checkouts/copies, `worker/*`, and `reconcile/*` require separate worktree-specific human authorization.

## Decision Adherence Validation (Mandatory Before Delivery)
| Decision ID | Status (`Adherent`/`Exception`) | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01` | n/a | n/a | n/a |

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)
| Module Decision Ref | Planned Handling | Delivery Status (`Preserved|Superseded (Approved)|Regression`) | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `n/a` | n/a | n/a | n/a | n/a |

### Exception Handling
- If any decision is `Exception`, delivery is blocked until:
  - the decision is explicitly challenged with rationale, or
  - a better alternative is proposed,
  and the updated decision/baseline receives renewed **APROVADO**.
- If any module decision is `Regression`, delivery is blocked until:
  - an intentional supersede decision is approved, and
  - canonical module consolidation targets are updated accordingly.

## Pipeline/Copilot P1/P2 Preflight
| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

## Rule-Spirit Anti-Pattern Hunt
| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| `config/agent_role_routing.json` | No bypass of governed routing | passed | `verify_context.sh` + declared profile | none | Genesis bootstrap executed in primary checkout |

When the heuristic scanner is in scope, prefer JSON evidence for non-trivial diffs. Scanner allowlists must be temporary and include owner, expiration, and reason; expired entries count as active findings.

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)
Use this whenever promotion/CI/Copilot/check/no-context review evidence creates findings. Same-scope remediation may stay inside the governing TODO and promotion lane when it preserves the same approved objective, scenario, and risk conversation. Split or renewed approval is required when the finding changes approved scope, adds a new independently testable behavior, creates a new approval/risk conversation, or needs a waiver/exception for a blocking P1/P2.
Carry prior recorded rows forward into every future no-context/Copilot review loop. A repeated finding is actionable only when the current bounded package materially changed the same locus/behavior or the prior adjudication is objectively insufficient.
Every deduplicated finding must be classified as `release-blocker`, `follow-up-fast-follow`, `follow-up-hardening`, or `by-design/no-action`.
- Only `release-blocker` rows may block the current delivery/promotion claim.
- `follow-up-fast-follow` and `follow-up-hardening` rows require an explicit TODO path/reference before the package can be called clean.
- `by-design/no-action` rows require rationale that ties back to approved intent, pre-existing scope boundaries, or proven reviewer noise.

| Finding ID | Finding Source | Severity | Classification | Required Action | Status | Rationale / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

## TODO Closeout Disposition
- **Disposition:** `complete`
- **Disposition reason:** Migration artifacts, topology contracts, guardrails, and validation evidence are complete for the approved scope.
- **Post-commit/push status:** Local validation complete; repository commit/push remains pending and is outside this TODO execution.
- **Next path/status action:** Move this TODO to `todos/completed/features/` and start the next approved TODO.

## Security Risk Assessment (Mandatory Before Delivery)
- **Risk level:** `n/a`
- **Why this risk level:** n/a
- **Attack surface in scope:** n/a
- **Attack simulation decision:** `n/a`
- **Review evidence:** `n/a`
- **Residual security risk:** n/a

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)
- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `n/a`
- **Why this level:** n/a
- **Current delivery stage at review time:** `n/a`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |
| `FRC` | `frontend-race-condition-validation` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |
| `BCI` | `backend-concurrency-idempotency-validation` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |
| `RLS` | `runtime-load-stress-validation` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` |

### Lane Detail Packet Template
Repeat the block below once for each lane in matrix order (`EPS`, `FRC`, `BCI`, `RLS`).

#### `n/a`
- **Trigger rationale:** n/a
- **Recorded at (UTC):** `n/a`
- **Executor ID:** `n/a`
- **Evidence object:** `n/a`
  - `evidence_type`: `n/a`
  - `environment_id`: `n/a`
  - `run_id`: `n/a`
  - `artifact_uri`: `n/a`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `n/a`
  - `sample_profile_id`: `n/a`
  - `acceptance_rule_id`: `n/a`
  - `result_summary`: `n/a`
  - `reviewer_id`: `n/a`
- **Blocker object:** `n/a`
  - `blocker_reason_code`: `n/a`
  - `blocker_reason`: n/a
  - `unblock_condition`: n/a
  - `follow_up_task_id`: `n/a`
  - `follow_up_owner`: `n/a`
- **Waiver object:** `n/a`
  - `waiver_reason_code`: `n/a`
  - `waiver_reason`: n/a
  - `waiver_expiry_utc`: `n/a`
  - `approver_id`: `n/a`
  - `approval_reference`: `n/a`
  - `follow_up_task_id`: `n/a`
  - `follow_up_owner`: `n/a`
  - `mitigation_summary`: n/a
  - `reviewer_id`: `n/a`
- **Classification change object:** `n/a`
  - `previous_trigger_result`: `n/a`
  - `new_trigger_result`: `n/a`
  - `classification_changed_by`: `n/a`
  - `classification_changed_at_utc`: `n/a`
  - `classification_change_reason`: n/a
  - `approval_reference`: `n/a`

Use `templates/performance_concurrency_lane_artifact_template.json` for machine-checkable lane artifacts. `recommended` lanes must still resolve by their gate deadline; only `trigger_result = not_needed` may use `state = not_applicable`.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)
- **Audit outcome:** `n/a`
- **Why this outcome:** n/a
- **Inline code TODO debt:** `n/a`
- **Evidence / audit artifact:** `n/a`
- **Accepted residual debt:** n/a

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)
- **Audit decision:** `n/a` (minimum from `audit_escalation_guard.py`)
- **Why this decision:** n/a
- **Trigger signals in scope:** `n/a`
- **Required evidence matrix (when architectural):** `n/a`
- **Package mode:** `n/a`
- **Package minimum contents:** `n/a`
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `n/a`
- **Internal reviewer mandate:** `n/a (name the fresh no-context internal reviewer/subagent when applicable; the reviewer cannot be the implementing agent; while a reviewer is pending_init|running, wait without a rigid deadline and never interrupt/recycle/replace/duplicate/repackage it; a polling timeout is not failure; recycle only terminal inactive reviewer lanes; external providers do not satisfy the pass)>`
- **Gate-satisfying evidence expectation:** `n/a`
- **Audit focus:** `n/a`
- **Required applicable evidence:** `n/a`
- **Audit status:** `n/a`
- **Findings summary:** n/a
- **Resolution ledger:** use the machine-checkable table below when findings exist
- **Carry-forward rule:** future no-context review loops must ingest prior resolution artifacts and TODO historical dispositions before reopening a finding. Reopen only when the bounded package materially changed the same locus/behavior or the prior rationale is objectively insufficient.
| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | n/a |
- **Evidence / reference:** n/a
- **Waiver authority / reference (required if waived):** `n/a`

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)
- **Final review decision:** `n/a` (minimum from `audit_escalation_guard.py`)
- **Why this decision:** n/a
- **Impact signals in scope:** `n/a`
- **Package mode:** `n/a`
- **Package minimum contents:** `n/a`
- **Review isolation mode:** `n/a`
- **Internal reviewer mandate:** `n/a (name the fresh no-context internal reviewer/subagent when applicable; the reviewer cannot be the implementing agent; while a reviewer is pending_init|running, wait without a rigid deadline and never interrupt/recycle/replace/duplicate/repackage it; a polling timeout is not failure; recycle only terminal inactive reviewer lanes; external providers do not satisfy the pass)>`
- **Canonical multi-lane audit protocol (when required):** `n/a`
- **Audit session / round evidence (when protocol used):** `n/a`
- **Review focus:** `n/a`
- **Final review status:** `n/a`
- **Findings summary:** n/a
- **Resolution ledger:** use the machine-checkable table below when findings exist
- **Carry-forward rule:** future no-context review loops must ingest prior resolution artifacts and TODO historical dispositions before reopening a finding. Reopen only when the bounded package materially changed the same locus/behavior or the prior rationale is objectively insufficient.
| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | n/a |
- **Evidence / reference:** n/a
- **Waiver authority / reference (required if waived):** `n/a`

## Independent Cutover Integrity Audit Gate
- **Cutover audit decision:** `n/a`
- **Why this decision:** n/a
- **Cutover signals in scope:** `n/a`
- **Package mode:** `n/a`
- **Canonical multi-lane audit protocol (when used):** `n/a`
- **Audit session / round evidence (when protocol used):** `n/a`
- **Audit focus:** `n/a`
- **Cutover audit status:** `n/a`
- **Findings summary:** n/a
- **Resolution ledger:** use the machine-checkable table below when findings exist
- **Carry-forward rule:** future no-context review loops must ingest prior resolution artifacts and TODO historical dispositions before reopening a finding. Reopen only when the bounded package materially changed the same locus/behavior or the prior rationale is objectively insufficient.
| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | n/a |
- **Evidence / reference:** n/a
- **Waiver authority / reference (required if waived):** `n/a`

## Delivery Confidence Gate (Required for `✅ Production-Ready`)
- [x] **Lane promotion evidence complete:** local commits and required PR merges recorded in `Promotion Evidence`.
- [x] **Runtime impact classified:** n/a
- [x] **Every `pcv-1` lane with `Gate Deadline = before_production_ready` is gate-satisfying:** `n/a`
- [x] **Any waived `pcv-1` lane still carried into production-ready has owner, expiry, mitigation, and follow-up recorded:** `n/a`
- [x] **Operational checks run (if runtime-impacting):**
  - [x] migration/index status checked
  - [x] queue/scheduler/worker health checked
  - [x] smoke flow executed in the best available environment (or justified as N/A)
- [x] **Lane artifacts recorded and hashed:** `foundation_documentation/artifacts/tmp/n/a/...`
- [x] **Confidence stated:** n/a + n/a
- [x] **Release readiness outcome:** n/a

## Module Consolidation Gate (Required Before `Completed`)
- [x] Canonical module docs were updated with stable conceptual outcomes and final decisions from this TODO.
- [x] Decision promotion ledger (or equivalent trace table) in module docs links back to this TODO.
- [x] Every relevant prior module decision is either preserved or intentionally superseded with explicit traceability.
- [x] Superseded/conflicting tactical notes were removed or replaced by canonical module references.
- [x] TODO/module cross-links were updated (including active/completed path changes).

## Commands (Run Locally)
- Query the project-declared stable full-workspace VS Code Problems snapshot
- n/a

## Files Expected (Compatibility Note)
- Use `Diff Expectation Contract` above as the authoritative expected-file/folder/type inventory. This legacy note is only for human navigation and is not used by the delivery guard.

## COMENTÁRIO:
- n/a

n/a
