# TODO — Delphi: validação multiplataforma e autoridade de engenharia

## Status

- **Estado:** `complete`
- **Current delivery stage:** `Local-Implemented`
- **Work state:** `review`
- **Approved by:** Gabriel / usuário — 2026-08-27
- **Authority boundary:** `delphi-ai` é a autoridade de inteligência, engenharia, agentes, regras, execução e validação. `foundation_documentation` registra TODOs, contratos, decisões, evidências e closeout.

## Approval

- **Approved by:** Gabriel / usuário — 2026-08-27
- **Approval scope:** adaptação do fluxo Delphi ao LeadsHug, normalização LF, regras, topologia e validação.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `none`
- **Next exact step:** closeout documental e movimentação para completed.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | Governs every implementation | TODO approval and evidence | Bypassing TODO governance | Delphi executes from approved TODO |
| `delphi-ai/tools/validate_leadshug_topology.py` and `delphi-ai/rules/stacks/` | Governs LeadsHug stack | Real topology and stack rules | Legacy topology assumptions | Validate before closeout |

## Scope

- [x] `.gitattributes` define LF para scripts e arquivos de engenharia.
- [x] Scripts shell rastreados do Delphi foram normalizados para LF.
- [x] `tools/check_shell_line_endings.py` foi criado e validado.
- [x] Capacidades NestJS, React, PostgreSQL/Prisma e Railway foram adicionadas.
- [x] Regras específicas de NestJS e React foram adicionadas.
- [x] Validador de topologia LeadsHug foi criado.
- [x] Sincronização e verificação foram adaptadas para `apps/api`, `apps/web` e referências congeladas.
- [x] O Delphi é a autoridade principal para ações de engenharia.

## Definition of Done

- [x] `.gitattributes` define LF para scripts e arquivos de engenharia.
- [x] Scripts shell rastreados do Delphi foram normalizados para LF.
- [x] Guard determinístico de line endings passa.
- [x] Regras e topologia LeadsHug foram adaptadas.
- [x] Validações de sincronização e ativação passam.

## Validation Steps

- [x] `python delphi-ai/tools/check_shell_line_endings.py delphi-ai`
- [x] `python delphi-ai/tools/validate_leadshug_topology.py .`
- [x] `bash delphi-ai/tools/verify_adherence_sync.sh`
- [x] `bash delphi-ai/verify_context.sh`

## Execution Evidence

| Criterion | Evidence | Status |
| --- | --- | --- |
| LF policy | `delphi-ai/.gitattributes` | passed |
| LF validation | `python delphi-ai/tools/check_shell_line_endings.py delphi-ai` | passed |
| LeadsHug topology | `python delphi-ai/tools/validate_leadshug_topology.py .` | passed |
| Rule synchronization | `bash delphi-ai/tools/verify_adherence_sync.sh` | passed |
| Context activation | `bash delphi-ai/verify_context.sh` | passed |

## Closeout Disposition

- **Disposition:** `complete`
- **Reason:** implementação e validações do fluxo de engenharia concluídas; commit/push permanecem pendentes.
- **Next action:** mover para `todos/completed/features/` e iniciar somente o próximo TODO aprovado.

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
| Delphi engineering | Shell and adherence are touched | line-ending guard + adherence sync | closeout | passed | recorded above | none |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| Bounded Delphi engineering diff | topology, line endings, context | passed | topology, line-ending and context guards | none | no findings |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| Delphi authority and TODO-driven execution | bypassing Delphi or TODO | passed | authority boundary and adherence sync | none | no findings |

## Completion Evidence Matrix

| Criterion ID | Criterion | Evidence | Status |
| --- | --- | --- | --- |
| SCOPE-01 | LF policy and normalization | `.gitattributes` and LF guard | passed |
| SCOPE-02 | LeadsHug stack/topology adaptation | topology validator and stack rules | passed |
| DOD-01 | Deterministic validation | `check_shell_line_endings.py` | passed |
| DOD-02 | Rule synchronization | `verify_adherence_sync.sh` | passed |
| DOD-03 | Context activation | `verify_context.sh` | passed |
| SCOPE-03 | Stack capabilities | `config/stack_capabilities.yaml` | passed |
| SCOPE-04 | NestJS and React rules | `rules/stacks/nestjs/` and `rules/stacks/react/` | passed |
| SCOPE-05 | Delphi authority boundary | Approval and rules ingestion sections | passed |
| DOD-04 | Context activation | `verify_context.sh` | passed |
| DOD-05 | Delphi authority | `Agent Routing Preflight` | passed |
| VAL-01 | Shell line endings | `check_shell_line_endings.py` | passed |
| VAL-02 | Product topology | `validate_leadshug_topology.py` | passed |
| VAL-03 | Adherence sync | `verify_adherence_sync.sh` | passed |
| VAL-04 | PACED readiness | `verify_context.sh` | passed |
| EXACT-01 | Scope | `.gitattributes` define LF para scripts e arquivos de engenharia. | file | `.gitattributes` | local | passed | verified |
| EXACT-02 | Scope | Scripts shell rastreados do Delphi foram normalizados para LF. | guard | LF guard | local | passed | verified |
| EXACT-03 | Scope | `tools/check_shell_line_endings.py` foi criado e validado. | script | guard script | local | passed | verified |
| EXACT-04 | Scope | Capacidades NestJS, React, PostgreSQL/Prisma e Railway foram adicionadas. | config | stack capabilities | local | passed | verified |
| EXACT-05 | Scope | Regras específicas de NestJS e React foram adicionadas. | rules | stack rules | local | passed | verified |
| EXACT-06 | Scope | Validador de topologia LeadsHug foi criado. | script | topology validator | local | passed | verified |
| EXACT-07 | Scope | Sincronização e verificação foram adaptadas para `apps/api`, `apps/web` e referências congeladas. | script | `apps/api`, `apps/web`, adherence sync | local | passed | verified |
| EXACT-08 | Scope | O Delphi é a autoridade principal para ações de engenharia. | governance | authority boundary | local | passed | verified |
| EXACT-09 | Definition of Done | Guard determinístico de line endings passa. | command | LF guard | local | passed | verified |
| EXACT-10 | Definition of Done | Regras e topologia LeadsHug foram adaptadas. | command | topology and rules | local | passed | verified |
| EXACT-11 | Definition of Done | Validações de sincronização e ativação passam. | command | adherence and context guards | local | passed | verified |
| EXACT-12 | Validation Steps | `python delphi-ai/tools/check_shell_line_endings.py delphi-ai` | command | command output | local | passed | verified |
| EXACT-13 | Validation Steps | `python delphi-ai/tools/validate_leadshug_topology.py .` | command | command output | local | passed | verified |
| EXACT-14 | Validation Steps | `bash delphi-ai/tools/verify_adherence_sync.sh` | command | command output | local | passed | verified |
| EXACT-15 | Validation Steps | `bash delphi-ai/verify_context.sh` | command | command output | local | passed | verified |
