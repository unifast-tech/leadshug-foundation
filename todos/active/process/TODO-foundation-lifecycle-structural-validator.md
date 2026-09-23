# TODO — Foundation lifecycle structural validator

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`

## Context

O lifecycle da Foundation exige um validator permanente quando backlog, decisões e roadmap ultrapassarem dez registros vivos combinados ou quando houver recorrência comprovada de drift. O ST-01 consolidou 18 registros vivos — três candidatos, onze decisões e quatro linhas de roadmap — e acionou o primeiro limiar. Até este TODO ser aprovado e entregue, os exact checks versionados no TODO concluído do ST-01 continuam sendo o controle obrigatório.

## Framing Source & Story Slice

- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `n/a`
- **Why this is the right current slice:** materializar somente o follow-up obrigatório de `D-09` como um validador permanente, sem misturar evolução de produto, pipeline ou novos estudos.
- **Direct-to-TODO rationale:** o gatilho, o owner estratégico, os invariantes de origem e o resultado esperado já estão definidos em [evolution_lifecycle.md](../../../evolution_lifecycle.md#deterministic-adoption-trigger); não existe ambiguidade de decomposição que justifique outro feature brief.

## Contract Boundary

- Este TODO define **WHAT** deve ser protegido pelo validador e o que prova sua entrega.
- `Assumptions Preview` e `Execution Plan` definem **HOW** a implementação é recomendada; não concedem execução.
- O TODO é **bounded but elastic**: correções locais no parser, fixtures e mensagens podem permanecer aqui quando preservarem os mesmos invariantes e a mesma conversa de aprovação.
- Novo owner canônico, mudança de schema/lifecycle, integração com CI/CD, expansão para código de produto ou exceção histórica exigem atualização do contrato e novo `APROVADO`.
- O TODO permanece em `Review`; refinamento, reviews e guards de planejamento não equivalem a autorização de implementação.

## Implementation Intent

- **Current delivery:** estabelecer um validador Foundation fail-closed, project-owned e sem dependências externas, acompanhado de testes positivos/negativos e comando documental reproduzível.
- **Planned next steps:** avaliar integração com GitHub Actions/CI em TODO próprio após a superfície local provar estabilidade.
- **Anticipatory implementation authorized now:** `none`
- **Rationale:** separar o mecanismo local determinístico da adoção em CI evita ampliar este slice e permite validar a semântica antes de torná-la gate remoto.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Tactical TODO lifecycle state:** `Review`
- **Qualifiers:** `none`
- **Next exact step:** obter validação humana das decisões revisadas `D-01..D-10`, congelar uma nova baseline e repetir architecture opinion, plan critique e guards pré-aprovação.

## Active Work State

- **Work state:** `review`
- **Why this state now:** architecture opinion e crítica encontraram findings materiais; o contrato foi reconvergido e exige nova validação humana antes de outro freeze.
- **Exit condition:** decisões validadas, baseline congelada/publicada, reviews e guards pré-aprovação verdes, seguidos de `APROVADO` explícito ou cancelamento com racional.

## Trigger Evidence

- **Trigger:** mais de dez registros vivos combinados em backlog, decisões e roadmap.
- **Observed count:** `18` em 2026-09-23 (`3` candidatos + `11` decisões `Accepted` + `4` linhas de roadmap).
- **Source:** [ST-01 D-09](../../completed/process/TODO-leadshug-foundation-evolution-lifecycle.md) e [Deterministic-adoption trigger](../../../evolution_lifecycle.md#deterministic-adoption-trigger).
- **Execution authority:** `none`; abertura e refinamento do TODO não equivalem a `APROVADO`.

## Scope

- [ ] `S-01` Criar `deterministic/validate_foundation_lifecycle.py`, executável com Python standard library, que derive regras dos owners canônicos sempre que possível e nunca se torne owner concorrente de estado vivo.
- [ ] `S-02` Validar fail-closed os headings/tabelas, schemas/colunas obrigatórias e enums do source graph enumerado para lifecycle, backlog, decisões e roadmap.
- [ ] `S-03` Validar sintaxe e unicidade dos IDs `BLG-*` e `DEC-*` somente nos registros autoritativos admitidos, permitindo referências repetidas fora do owner; `CAP-*` fica fora deste slice.
- [ ] `S-04` Validar owner singular por registro admitido, links Markdown e decision-target paths confinados/resolvíveis; campos de dependência/next-gate em prosa são obrigatórios, mas não fingem ser IDs resolvíveis.
- [ ] `S-05` Distinguir decisão `Accepted` válida porém `pending-effect` de structurally eligible for effectiveness: exigir targets existentes, únicos e mapeados 1:1 a evidências não-placeholder, sem alegar validação semântica do conteúdo consolidado.
- [ ] `S-06` Preservar a exceção histórica por construção: somente o source graph explícito é escaneado; histórico entra apenas após TODO material atualizar o source graph canônico.
- [ ] `S-07` Criar testes test-first positivos e mutation/fail-first negativos, com oráculos independentes do parser, fixtures temporárias e prova byte-for-byte read-only.
- [ ] `S-08` Documentar owner, comando, cobertura, códigos de saída e mensagens de diagnóstico em `deterministic/README.md`, além de atualizar o lifecycle e o índice raiz com o handoff canônico.
- [ ] `S-09` Substituir os exact checks do ST-01 como controle corrente somente depois que o novo comando e sua suíte passarem no checkout principal consolidado.

## Out of Scope

- [ ] `OOS-01` Alterar backend, frontend, banco, runtime, Docker, Railway, CI/CD ou contratos de produto do LeadsHug.
- [ ] `OOS-02` Editar workflows de GitHub Actions ou alegar integração remota neste TODO.
- [ ] `OOS-03` Reabrir/reformular a direção de decisões `D-01..D-11` do ST-01 ou mudar seus enums/schemas; validação estrutural não adjudica verdade semântica da consolidação.
- [ ] `OOS-04` Retroajustar TODOs concluídos, artifacts históricos ou documentos legados apenas para fazê-los passar no novo validator.
- [ ] `OOS-05` Copiar contagens, títulos, disposições ou conteúdo específico do ST-01 para o código do validator como verdade permanente.
- [ ] `OOS-06` Criar configuração paralela que replique schemas, enums, owners ou estados já pertencentes a documentos canônicos.
- [ ] `OOS-07` Integrar o validator aos guards genéricos do `delphi-ai`; esta entrega permanece project-specific em `foundation_documentation/`.
- [ ] `OOS-08` Validar registros `CAP-*`, módulos, TODOs ou contract-verification records neste slice; sua admissão futura exige source-graph/schema próprios.

## Execution Lane Tracking

- **Local implementation branches:** `foundation_documentation:main`
- **Promotion lane path:** `main -> origin/main`
- **Lane-promoted threshold for this TODO:** `origin/main`
- **Production-ready threshold for this TODO:** `origin/main` com gates de entrega e closeout verdes

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Foundation lifecycle validator | `main@pending` | `n/a — single-branch Foundation authority` | `n/a` | `direct push after governed gates` | planned |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `.` | `697864f6ec9e44a8c122a2963fcb9f9e7219b515` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `deterministic/validate_foundation_lifecycle.py` | `A` | implementação project-owned do validator |
| Foundation | `deterministic/tests/test_validate_foundation_lifecycle.py` | `A` | suíte positiva, negativa e mutation-oriented |
| Foundation | `deterministic/README.md` | `A` | contrato de uso, owner, cobertura e diagnóstico |
| Foundation | `evolution_lifecycle.md` | `M` | substituir o handoff temporário pelo comando permanente entregue |
| Foundation | `README.md` | `M` | expor navegação e comando canônico sem duplicar regras |
| Foundation | `todos/active/process/TODO-foundation-lifecycle-structural-validator.md` | `M, D, R` | contrato, evidência e movimento de closeout |
| Foundation | `todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` | `A, M, R` | destino governado após todos os gates |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `project_constitution.md` | `any` | invariantes constitucionais já definidos; mudança exigiria nova decisão material |
| Foundation | `backlog/**` | `any` | registros vivos serão lidos, não reescritos |
| Foundation | `decisions/**` | `any` | decisões existentes são baseline, não alvo de alteração |
| Foundation | `system_roadmap.md` | `any` | roadmap é entrada de validação, não alvo desta entrega |
| Foundation | `modules/**` | `any` | nenhum contrato de produto/módulo muda |
| Foundation | `contracts/**` | `any` | nenhum contrato de produto muda |
| Foundation | `artifacts/**` | `any` | artifacts históricos não serão retroajustados |
| Foundation | `.github/**` | `any` | integração CI/CD permanece fora do escopo |
| Foundation | `../delphi-ai/**` | `any` | validator específico do LeadsHug, sem self-maintenance Delphi |

### Diff Deviation Analysis

Preencher somente se o guard retornar `no-go`; qualquer novo path ou change type exige classificação e, quando ampliar escopo, validação humana e novo `APROVADO`.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** helpers internos do parser, fixtures, mensagens de diagnóstico, casos negativos adicionais e pequenas correções documentais nos paths esperados.
- **Must update or split the TODO:** integração com CI, novo schema/owner, alteração de dados vivos para fazê-los passar, adoção em `delphi-ai`, nova dependência ou expansão para validação de produto.

## Definition of Done

- [ ] `DOD-01` O validator retorna `0` para a Foundation canônica válida e código diferente de zero para qualquer violação coberta, sem alterar arquivos.
- [ ] `DOD-02` Cada regra enumerada na Test Rule Matrix possui fail-first positivo/negativo, mensagem/exit assertions e oráculo independente do helper sob teste.
- [ ] `DOD-03` Mutations detectam estrutura Markdown ambígua, ID inválido/duplicado, enum inválido, coluna/owner ausente, link/anchor/target inválido, path/symlink escape, evidência 1:1 ausente/contraditória e output não redigido; referências repetidas válidas e `pending-effect` válido passam.
- [ ] `DOD-04` O validator deriva enums/owners dos documentos canônicos ou usa assertions estruturais documentadas; não mantém segundo catálogo editável de estado vivo.
- [ ] `DOD-05` Testes provam histórico fora do source graph ignorado, inclusão apenas após source-graph explícito e impossibilidade de excluir registro vivo inválido.
- [ ] `DOD-06` `deterministic/README.md`, `evolution_lifecycle.md` e `README.md` apontam para um único comando e declaram que CI remoto não foi alterado.
- [ ] `DOD-07` O comando permanente substitui o controle temporário somente após dual-run old/new no mesmo branch@sha consolidado, com paridade verde e ordem de cutover registrada.
- [ ] `DOD-08` Diff expectation, decisões, evidence matrix, audits, crítica, test-quality audit, final review e closeout guards estão completos e verdes.

## Validation Steps

- [ ] `VAL-01` Executar `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` e exigir exit `0` com resumo determinístico.
- [ ] `VAL-02` Executar `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` e exigir todos os testes verdes.
- [ ] `VAL-03` Executar a Test Rule Matrix inteira, incluindo root confinement, symlink/`..` escape, anchors, Unicode/HTML, read-only byte snapshot, `pending-effect` válido e evidência contraditória.
- [ ] `VAL-04` Executar `python3 -m py_compile foundation_documentation/deterministic/validate_foundation_lifecycle.py foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`.
- [ ] `VAL-05` Executar separadamente `git diff --check`, diff expectation guard e scan redigido de secret/private-key patterns; nenhum comando isolado pode alegar as três capacidades.
- [ ] `VAL-06` Executar diff, authority, completion e closeout guards; exigir `go` antes do movimento final e provar todos os deliverables esperados mais exclusividade `active XOR completed`.
- [ ] `VAL-07` No mesmo branch@sha final, executar os Exact Check Command Contracts aplicáveis do ST-01 (`VAL-01`, `VAL-02`, `VAL-08`, `VAL-10`) e o novo validator/tests; exigir dual-run verde antes de atualizar o handoff/cutover.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01..S-09` | Scope | implementação e adoção documental do validator | code+test+doc | paths esperados + `VAL-01..VAL-05` | local Foundation | planned | expandir 1:1 após implementação |
| `DOD-01..DOD-08` | Definition of Done | critérios de entrega | test+review | comandos e gates correspondentes | local Foundation | planned | evidência agregada não substituirá linhas finais 1:1 |
| `VAL-01..VAL-06` | Validation Steps | comandos obrigatórios | test | stdout/exit e referências versionadas | local Foundation | planned | registrar comando, resultado e branch@sha |

## External Dependency Readiness

- **Decision:** `required only for publication/Production-Ready; not needed for local implementation`
- **Rationale:** parser/tests usam apenas arquivos locais, mas freeze e closeout exigem `origin/main`; GitHub/origin deve estar acessível e sincronizado antes dessas alegações.
- **Current evidence:** `origin/main@4af3a247f27c1754dfc5c7f28cb55021ee08aea7` estava sincronizado no pacote revisado; revalidar antes do próximo freeze/push.

## Profile Scope & Handoffs

- **Primary planning profile:** `Strategic / CTO-Tech-Lead`
- **Primary execution profile:** `routine-executor`
- **Active technical scope:** `cross-stack` documental/determinístico
- **Expected supporting profiles:** `Assurance / Tester-Quality`; `formal-reviewer`
- **Genesis Gate 0:** `rejected — canonical Foundation already exists and this is governed evolution`
- **Profile scope command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/evolution_lifecycle.md foundation_documentation/README.md foundation_documentation/deterministic/validate_foundation_lifecycle.py foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py foundation_documentation/deterministic/README.md`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `Strategic / CTO-Tech-Lead` | `routine-executor` | decisões são estratégicas; parser/testes são execução delimitada | `deterministic/**`; handoffs documentais | planned; depende de validação, preflight e `APROVADO` |
| `routine-executor` | `Assurance / Tester-Quality` | mutation coverage e fail-closed behavior exigem challenge independente | validator, tests, evidence packet | planned após implementação |
| `Assurance / Tester-Quality` | `formal-reviewer` | final review fecha aderência e dívida residual | pacote consolidado | planned |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** um review de plano antes do `APROVADO`, crítica independente após freeze e gates de entrega após implementação.
- **Why this level:** o diff é pequeno e docs-only quanto ao produto, mas estabelece enforcement compartilhado, parser estrutural e suíte de mutações sobre várias autoridades Foundation.

## Canonical Module Anchors

- **Primary canonical anchor:** `foundation_documentation/evolution_lifecycle.md`
- **Secondary anchors:** `foundation_documentation/backlog/README.md`; `foundation_documentation/decisions/README.md`; `foundation_documentation/decisions/ST-01-foundation-lifecycle-decisions.md`; `foundation_documentation/system_roadmap.md`; `foundation_documentation/README.md`
- **Canonical Coverage Status:** `Complete for the touched lifecycle surface`
- **Decision consolidation targets:** `evolution_lifecycle.md`; `deterministic/README.md`; `README.md`
- **Module docs:** `n/a — no product module behavior or contract changes`

### Validator Source Graph (Revised Contract)

| Owner Path | Unique Heading / Record Surface | Required Structure | Validation Boundary |
| --- | --- | --- | --- |
| `evolution_lifecycle.md` | `Authority matrix`, five `State machines`, `Historical-document exception`, `Deterministic-adoption trigger` | headings unique; schemas/enums readable; authority rows unique | source of schemas/enums/owner semantics; no live record discovery outside rows below |
| `backlog/README.md` | `## Candidates` | exact eight-column table; unique `BLG-*`; state from Candidates enum; nonempty fields | Markdown links resolve; freeform Dependencies/Next gate are required prose, not IDs |
| `decisions/README.md` | `## Records` | Markdown links enumerate decision record files | only linked records are admitted; no unrestricted `decisions/*.md` glob |
| linked decision record files | unique decision table | exact six columns; unique `DEC-*`; state from Decisions enum | targets unique/existing/root-confined; evidence segments map 1:1 structurally; semantics remain review-owned |
| `system_roadmap.md` | unique six-column roadmap table | unique phase rows; valid Horizon/Gate status; nonempty dependencies/outcome/exit gate | prose dependencies are required but not treated as resolvable IDs |

### Narrow Markdown Grammar (Revised Contract)

- UTF-8 strict input; reject undecodable bytes and hidden Unicode format controls in identifiers, enum values and paths.
- Required headings/tables are unique; duplicate/missing/reordered headers or row cardinality mismatch fail closed.
- Pipe tables are parsed structurally with inline code/link awareness; ambiguous escaped pipes/code spans fail with a diagnostic instead of silent token shifting.
- Markdown links/anchors and decision target paths must be relative, remain under `--root`, resolve without absolute paths, `..` escape or symlink escape, and never cause content echo in diagnostics.
- Discovery depth is exactly the source graph above. Historical/completed/artifact content can be a resolved reference target without becoming a scanned live owner.
- Decision effectiveness output is structural only: `Accepted + valid targets + incomplete mapping = pending-effect` is valid; complete 1:1 target/evidence mapping is `structurally-eligible`, never a semantic truth claim.

## Decision Pending

| Decision ID | Revised Recommended Direction | Review Finding Source | Human Validation Needed |
| --- | --- | --- | --- |
| `D-01` | Admit only the explicit source graph above; validate `BLG-*` and `DEC-*`; exclude `CAP-*`, modules, TODO records and contract-verification records from this slice. | `AR-02/03`, `F-02` | confirm revised boundary |
| `D-02` | Add the source graph and narrow Markdown grammar to `evolution_lifecycle.md`; derive from those authorities without a parallel mutable catalog. | `AR-02/04`, `F-02` | confirm extraction contract |
| `D-03` | Make the validator read-only/fail-closed with mandatory root/symlink confinement, byte-preservation and bounded/redacted diagnostics. | `AR-04`, `F-07/08` | confirm safety contract |
| `D-04` | Implement the historical boundary through explicit source-graph admission, not heuristics or Git-time inference; a later material TODO must update the graph to admit a new owner. | `AR-02`, `F-04` | confirm adoption rule |
| `D-05` | Deliver local validation only; record CI-equivalent as `n/a — no repo-owned CI`; remote CI integration stays in another TODO. | preserved; `F-10` terminology fix | confirm two-stage adoption |
| `D-06` | Use Python stdlib + unittest with `test-first` strategy, independent fixture oracles and a 1:1 rule/mutation matrix. | `AR-04`, `F-07` | confirm stack/testing |
| `D-07` | Keep owner project-specific in Foundation and route implementation to routine-executor; no `delphi-ai` implementation changes. | preserved; `F-09` routing fix | confirm ownership/routing |
| `D-08` | Cut over only after old/new dual-run on the same final branch@sha, audits/reviews, publication, deliverable existence and `active XOR completed` checks. | `AR-05`, `F-06` | confirm cutover |
| `D-09` | Treat `Accepted` with incomplete consolidation as valid `pending-effect`; validator may report structurally eligible mapping but never claim semantic effectiveness. | `AR-01`, `F-03` | confirm validity/effectiveness split |
| `D-10` | Treat prose dependencies/next gates as required nonempty text; validate only explicit Markdown links/anchors as resolvable references. | `F-02` | confirm dependency grammar |

## Decisions

- `pending renewed human validation of revised D-01..D-10`

## Module Decision Baseline Snapshot

| Canonical Decision Ref | Current Direction | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `DEC-validator-adoption-trigger` | criar validator após limiar ou drift recorrente | Preserve | decisions record + lifecycle trigger |
| `DEC-single-field-authority` | um owner por campo e links/IDs fora dele | Preserve | ST-01 decisions record |
| `DEC-historical-adoption-boundary` | não retroajustar histórico intocado | Preserve | decisions record + historical exception |
| `DEC-decision-effectiveness-after-consolidation` | decisão só é efetiva após todos os targets | Preserve | decisions index + lifecycle |
| `DEC-immutable-lifecycle-identifiers` | IDs imutáveis com syntax canônica | Preserve | lifecycle immutable identifiers |
| `DEC-provider-neutral-lifecycle-roles` | papéis neutros de provider | Preserve | lifecycle roles and authority |

## Decision Baseline

- **Prior freeze:** `D-01..D-08` at `b685fb52fa00b245b4bfb58ded6b8d7212f7f6eb`, invalidated by material findings `AR-01..05` and `F-01..11`.
- **Freeze status:** `not_frozen — revised D-01..D-10 pending renewed validation`
- **Frozen decisions:** `none current`
- **Historical validation evidence:** Gabriel/user, 2026-09-23, phrase `APROVADO`; preserved as provenance, not execution authority.

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `required`
- **Why this applies:** estabelece enforcement permanente de arquitetura documental compartilhada e aposenta checks ad hoc como controle corrente.
- **Deviation / debt being retired:** exact checks longos embutidos no TODO concluído do ST-01 e ausência de comando project-owned reutilizável.
- **Target steady-state after closeout:** um comando read-only, fail-closed, testado e documentado valida a Foundation viva sem duplicar verdade.
- **Temporary exceptions allowed:** `none`; os exact checks ST-01 permanecem somente como controle anterior até o cutover, não como implementação paralela permanente.
- **Cutover / removal condition:** validator e suíte publicados, acceptance real verde, reviews/audits obrigatórios limpos e lifecycle atualizado para apontar ao comando permanente.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| single-field authority | `DEC-single-field-authority` | owners e referências lifecycle | impede estado vivo concorrente |
| canonical-source derivation | `D-02` | parser e regras | evita segundo catálogo editável |
| fail-closed diagnostics | `D-03` | CLI e gates | impede falso verde e torna falha acionável |
| historical adoption boundary | `DEC-historical-adoption-boundary` | seleção de entradas | preserva história sem esconder drift vivo |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| hard-coded ST-01 snapshot | novo registro válido exige editar validator | congela conteúdo transitório como regra | none |
| duplicated live-state catalog | enum/schema/owner copiado em config paralela | cria owner concorrente | none |
| regex-only validation without structural parsing | fixture estruturalmente inválida passa | aceita drift semântico/falsos verdes | regex pode apoiar parsing, nunca substituir estrutura |
| warning-only failures | input inválido retorna zero | não protege lifecycle | none |
| rewriting invalid source | hash/working tree muda durante validação | mascara drift e viola read-only | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| guard | live Foundation | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | schemas/IDs/owners/links/target-evidence mapping estrutural inválidos | implement-in-this-todo | `VAL-01`, `DOD-01/04` |
| test | validator rules | `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` | falsos verdes e regressões por mutation | implement-in-this-todo | `VAL-02/03`, `DOD-02/03/05` |
| rule | usage contract | `foundation_documentation/deterministic/README.md` | uso sem boundary/owner/exit semantics | implement-in-this-todo | `DOD-06` |
| audit | delivered package | critique + test-quality audit + final review | fragilidade, duplicação e dívida de verificação | implement-in-this-todo | gate evidence no TODO |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** `/root/validator_architecture_opinion`, 2026-09-23: `AR-01..AR-05` materiais integrados; approval contract requer renovação e nova review após freeze revisado.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`
- **No-go handling:** `when either required review is absent, blocked, or exposes an unresolved approval-breaking divergence, return to the affected diagnosis/decision or delivery-evidence loop; do not claim APROVADO or Completed.`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** TODO medium de architecture enforcement requer pacote estável/publicado antes da crítica.
- **Trigger stage:** `after D-01..D-10 validation and before renewed planning-side reviews`
- **Baseline branch:** `main`
- **Baseline commit:** `b685fb52fa00b245b4bfb58ded6b8d7212f7f6eb`
- **Baseline push reference:** `origin/main@b685fb52fa00b245b4bfb58ded6b8d7212f7f6eb`
- **Gate status:** `findings_integrated`
- **Findings summary:** baseline foi congelada corretamente, mas reviews materiais invalidaram o approval contract; nova baseline será exigida após validação de `D-01..D-10`.
- **Evidence / reference:** commit `b685fb52fa00b245b4bfb58ded6b8d7212f7f6eb`, pushed to `origin/main` on 2026-09-23.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** reviews podem revelar expansão acidental para CI, histórico ou owners.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **No-go handling rule:** `return to review, revalidate evolved scope, refresh pushed baseline when needed, and rerun affected review/guard lanes`
- **Gate status:** `not_run`
- **Findings summary:** `n/a`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close

- `Q-01` A autoridade humana valida o contrato revisado `D-01..D-10`, que substitui a baseline anterior?

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | `deterministic/` é a superfície project-owned para enforcement local. | diretório versionado com `.gitkeep`; `DEC-validator-adoption-trigger`; expected diff | outro path exige renovar diff/handoff | High | Promote to Decision (`D-07`) |
| `A-02` | Python 3 está disponível no contexto de validação Foundation. | guards e exact checks ST-01 usam Python 3 | stack/commands precisam revisão | High | Keep as Assumption |
| `A-03` | Exact checks ST-01 são oráculo temporário de paridade, não código a copiar. | lifecycle trigger + `D-02/D-08` | cutover/test plan muda materialmente | High | Promote to Decision (`D-02,D-08`) |
| `A-04` | Não existe CI repo-owned Foundation a espelhar. | tree sem `.github/workflows`; `D-05` | exige handoff DevOps e renewed approval | High | Promote to Decision (`D-05`) |
| `A-05` | Nenhum fluxo de usuário/runtime é afetado. | diff/out-of-scope restritos a Foundation tooling/docs/tests | exige split e runtime evidence | High | Promote to Decision (`D-01,D-07`) |

## Execution Plan

### Touched Surfaces

- Validator: `foundation_documentation/deterministic/validate_foundation_lifecycle.py`.
- Tests: `foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`.
- Usage contract: `foundation_documentation/deterministic/README.md`.
- Canonical handoff: `foundation_documentation/evolution_lifecycle.md` e `foundation_documentation/README.md`.
- Governance/evidence: este TODO.

### Ordered Steps

1. Após validação humana, congelar `D-01..D-10`, publicar baseline e concluir plan/architecture critique + guards pré-aprovação.
2. Após `APROVADO` e authority guard `go`, implementar parser/diagnostics read-only derivados dos owners.
3. Criar fixtures temporárias e testes; executar mutations fail-first antes de aceitar implementação.
4. Documentar comando, boundary, exit contract e owner; atualizar somente handoffs esperados.
5. Executar validator real, unittest, py_compile, diff/security hygiene e evidence matrices.
6. Executar architecture adherence, test-quality audit, final review e closeout guards.
7. Publicar, mover o TODO para `completed/process/` e confirmar cutover sem lacuna.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** validator e testes podem compartilhar o mesmo erro; cada regra deve falhar contra uma fixture/mutation independente antes do código que a satisfaz.
- **Fail-first targets:** source graph/headers, table cardinality, BLG/DEC syntax+uniqueness, enums, link/anchor/path confinement, pending-effect versus structurally-eligible mapping, historical exclusion/admission, Unicode/HTML, bounded/redacted diagnostics e byte-for-byte read-only.
- Fixtures/oráculos são escritos manualmente em temporary directories e não reutilizam helpers internos do parser para construir o expected result.
- Real-repository acceptance e dual-run ST-01/new ocorrem somente após todos os fail-first cases convergirem.

### Test Rule Matrix

| Rule ID | Positive Control | Required Mutation / Negative Case | Required Assertion |
| --- | --- | --- | --- |
| `T-01` | unique required heading/table | missing, duplicate or reordered heading/header | non-zero + rule/path |
| `T-02` | exact row cardinality | missing/extra cell, ambiguous pipe/code span | non-zero + row locator |
| `T-03` | unique valid `BLG-*`/`DEC-*` owners | invalid case/slug, duplicate owner | non-zero + ID |
| `T-04` | repeated reference outside owner | duplicate reference only | remains zero |
| `T-05` | enum from lifecycle | invalid/hidden Unicode/HTML state | non-zero + normalized diagnostic |
| `T-06` | valid relative link/anchor | missing anchor/path, absolute, `..`, symlink escape | non-zero without content leak |
| `T-07` | `Accepted` with incomplete mapping | pending-effect fixture | remains zero + pending-effect classification |
| `T-08` | complete 1:1 target/evidence mapping | duplicate target, absent/contradictory segment | non-zero; never semantic-effective claim |
| `T-09` | history outside source graph | historical file invalid but unadmitted | remains zero |
| `T-10` | explicitly admitted live record | invalid live/admitted record | non-zero; cannot be excluded heuristically |
| `T-11` | bounded/redacted diagnostic | secret-like fixture payload | diagnostic omits value and respects limit |
| `T-12` | read-only tree | full validation pass/fail | byte hashes and symlink metadata unchanged |

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Rationale:** não é bug/regressão; falsos negativos serão provados por mutations durante implementação aprovada.

### Flow Evidence Planning Matrix

| Criterion | User-visible / Runtime Impact | Required Final Lane | Rationale |
| --- | --- | --- | --- |
| `S-01..S-09` | none | `n/a — structure-only` | somente parser/docs/tests Foundation; sem jornada de usuário |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation repository | nenhum job/suite CI repo-owned existe neste slice | `n/a — local validation only` | `n/a` | `n/a — no CI-equivalent claim` | APROVADO | n/a | source tree + `D-05` | validator/unittest ficam na matriz local abaixo |

### Local Validation Matrix

| Surface | Behavior / Scenario | Preconditions | Command | Required Before | Status |
| --- | --- | --- | --- | --- | --- |
| validator acceptance | source graph real válido | consolidated branch@sha | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | Local-Implemented | planned |
| unittest/mutations | `T-01..T-12` | isolated temporary fixtures | `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` | Local-Implemented | planned |
| cutover parity | old exact checks + new validator/tests agree | same final branch@sha, before handoff update | ST-01 `VAL-01/02/08/10` exact contracts + commands above | Production-Ready | planned |

### Runtime / Rollout Notes

- `n/a — no runtime, migration, deploy, secret, database, browser or device surface`
- Exact checks ST-01 permanecem requeridos até o novo comando passar e ser publicado.

## Plan Review Gate

- **Status:** `findings_integrated — original package no-go; revised package awaits human validation, refreeze and fresh review`
- **Required lenses:** Architecture, Code Quality, Tests, Performance, Security, Elegance, Structural Soundness.
- **Expected focus:** evitar parser frágil, catálogo duplicado, cobertura superficial, bypass histórico e expansão para CI.

### Review Sections

- [x] Architecture — source graph/effectiveness/history findings integrated.
- [x] Code Quality — narrow grammar, confinement and diagnostics contract added.
- [x] Tests — test-first and `T-01..T-12` matrix added.
- [x] Performance — bounded linear scan; no specialized lane triggered.
- [x] Security — root/symlink confinement and redaction made mandatory.
- [x] Elegance — one project-owned stdlib validator; no parallel catalog.
- [x] Structural Soundness — old/new parity and explicit cutover added.

### Issue Cards

- **Issue ID:** `PLAN-01` — decision validity/effectiveness conflated (`high`). Option A: structural `pending-effect`/eligible split (recommended, medium effort/low risk/local blast/low maintenance/neutral performance/high elegance+soundness); Option B: atomic Accepted (high effort/risk/cross-doc); Option C: do nothing (high false-block risk). **Resolution:** integrated into `D-09`, `S-05`, `T-07/08`.
- **Issue ID:** `PLAN-02` — open scan universe/history (`high`). Option A: explicit source graph + grammar (recommended, medium effort/low risk); Option B: hard-code snapshot (low effort/high maintenance); Option C: broad scan (high false-positive risk). **Resolution:** integrated into source graph, `D-01/02/04/10`.
- **Issue ID:** `PLAN-03` — parser/read-only/security proof incomplete (`high`). Option A: mandatory narrow grammar, confinement, redaction and byte snapshot (recommended, medium effort/low risk); Option B: external parser (medium supply-chain risk); Option C: do nothing (high false-green risk). **Resolution:** integrated into `D-03/06`, `T-01..T-12`.
- **Issue ID:** `PLAN-04` — cutover/test/routing evidence incomplete (`high`). Option A: test-first + dual-run + exact implementation routing (recommended, medium effort/low risk); Option B: cut over after new-only local green (medium risk); Option C: do nothing (control gap). **Resolution:** integrated into `D-05/07/08`, matrices and routing.

### Failure Modes & Edge Cases

- Markdown com coluna deslocada ou registro duplicado.
- IDs válidos referenciados várias vezes sem confundir com owner duplicado.
- Links com anchors, paths relativos e targets existentes.
- Decisão `Accepted` com múltiplos targets e evidência incompleta para um deles.
- Unicode/HTML ocultando enum/ID/estado inválido.
- Histórico inválido excluído versus registro vivo inválido ignorado indevidamente.
- Novo registro válido deve passar sem alteração do código.
- Validator nunca corrige/regrava entradas.

### Residual Unknowns / Risks

- Granularidade do parser pode exigir helper interno, sem justificar dependência externa ou mudança de contrato.
- Mensagens/estrutura interna são implementation details desde que preservem exit, diagnóstico e testes.

## Additional Architectural Opinions

- **Needed:** `no at refinement; deterministic critique required after freeze`
- **Why ambiguity remains:** caminho dominante; risco está na qualidade do parser, coberto por review/critique.
- **Opinion count:** `0`
- **Package mode:** `bounded-file-set`
- **Internal reviewer mandate:** `required after freeze; reviewer cannot implement`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Latest TEACH evidence / artifact:** `prepared-pre-freeze` diagnostic on revised package, 2026-09-23, fingerprint `b82442926521`; critique/test-quality/final/verification-debt/architecture decision/adherence `required`; triple/security/performance-concurrency `not_needed`; rerun after renewed freeze for gate evidence.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | shared enforcement + mutation suite |
| `blast_radius` | `cross-stack` | governa Foundation compartilhada, sem produto |
| `behavioral_change_or_bugfix` | `yes` | cria comportamento fail-closed |
| `changes_public_contract` | `no` | sem API/schema/route/auth público |
| `touches_auth_or_tenant` | `no` | sem auth/tenant |
| `touches_runtime_or_infra` | `no` | sem runtime/infra/CI |
| `touches_tests` | `yes` | nova suíte unittest/mutation |
| `critical_user_journey` | `no` | governança interna |
| `release_or_promotion_critical` | `no` | não promove produto |
| `high_severity_plan_review_issue` | `yes` | `PLAN-01..04` high integrated; fresh review still required |
| `explicit_three_lane_request` | `no` | não solicitado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** piso esperado para medium, cross-stack governance e test logic.
- **Impact signals in scope:** `cross-stack documentary governance; deterministic enforcement; tests`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** TODO congelado, owners canônicos, assumptions, plan, issue cards e risks.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Canonical multi-lane audit protocol:** `n/a — deterministic floor says triple_review=not_needed`
- **Audit session / round evidence:** `n/a unless triggered`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `findings_integrated`
- **Findings summary:** `F-01..F-11` integrados no contrato revisado; material changes require renewed validation, refreeze and fresh critique.
- **Evidence / reference:** `/root/validator_plan_critique`, 2026-09-23; `overall_assessment=material_findings_present; approval_contract=renewal_required`.
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** assumptions `A-01..A-05` govern paths, interpreter, CI and runtime boundary.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03,A-04,A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending`
- **Approval scope:** `pending after D-01..D-10 validation and planning gates`
- **Execution not authorized by approval:** `CI/CD, product/runtime, historical rewrites, delphi-ai changes, worktrees or auxiliary checkouts unless separately named`
- **Renewed approval required when:** scope, invariant semantics, validation, expected paths, architecture, risk, exception or CI adoption changes materially.
- **Execution authority:** `not_granted`
- **Pre-gate human token:** Gabriel/user, 2026-09-23, `APROVADO`; it validated the superseded `D-01..D-08` only. Material findings require renewed validation and a new post-gate `APROVADO`.

## Rules Acknowledgement / Ingestion

Predeclared for pre-approval readiness; reload and bind after `APROVADO`.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | tactical implementation | approval, strict diff, evidence, closeout | implementation before authority | Review until APROVADO + guard |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | phase transitions | phase order/evidence | merging gates | routes execution/closeout |
| `delphi-ai/workflows/docker/todo-contract-refinement-method.md` | current phase | decisions, assumptions, plan | guessed assumptions | approval-ready contract |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | next phase | freeze, reviews, preflight | premature approval request | blocks until ready |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | new tests | meaningful fail-first cases | happy-path-only | governs test design |
| `delphi-ai/skills/test-quality-audit/SKILL.md` | validator trust | adversarial mutations | false confidence | audit after implementation |
| `foundation_documentation/project_constitution.md` | project authority | TODO hierarchy | product drift | project precedence |
| `foundation_documentation/evolution_lifecycle.md` | primary anchor | schemas, owners, history | competing owner | derive from lifecycle |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `pending explicit inclusion in renewed APROVADO`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Routing evidence:** `agent_role_routing_guard.py`, 2026-09-23; `implementation/routine-executor/gpt-5.6-terra/medium/primary-checkout-single-writer/no-worktree`.
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01..D-10` | planned | implementation/tests/docs after approval | expand 1:1 before delivery |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `DEC-validator-adoption-trigger` | Preserve | planned | validator + lifecycle handoff | no module behavior |
| `DEC-single-field-authority` | Preserve | planned | derived-rule implementation | no second owner |
| `DEC-historical-adoption-boundary` | Preserve | planned | exclusion tests | no retroactive migration |
| `DEC-decision-effectiveness-after-consolidation` | Preserve | planned | target tests | all targets required |
| `DEC-immutable-lifecycle-identifiers` | Preserve | planned | ID tests | references may repeat |
| `DEC-provider-neutral-lifecycle-roles` | Preserve | planned | code/docs review | provider is not authority |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| validator + tests + docs + TODO evidence | false greens, parser fragility, path drift, missing mutations | planned | fresh no-context delivery review | pending | required before closeout |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| single-field authority | duplicated state/config in Python | planned | review + mutations | pending | blocker if found |
| historical boundary | broad ignore hiding live failures | planned | adversarial fixtures | pending | blocker if found |
| fail-closed | warnings/zero exit on invalid input | planned | negative CLI tests | pending | blocker if found |
| strict diff | unrelated Foundation/product/CI edits | planned | diff guard | pending | renewed approval on expansion |

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `AR-01..AR-05` | high/medium | release-blocker | integrate in current TODO | mesmos objetivo e boundary do validador; não requer split | fixed-pending-revalidation | revised `D-01..D-10`, source graph, grammar, tests and cutover |
| `F-01..F-08` | high/medium | release-blocker | integrate in current TODO | correções do mesmo contrato de planejamento e verificação | fixed-pending-revalidation | assumptions schema, boundary/effectiveness/history, tests, security and cutover revised |
| `F-09..F-11` | medium | release-blocker | integrate in current TODO | correções de routing, CI terminology, PCV/state bookkeeping | fixed-pending-revalidation | routing, CI terminology, PCV/state bookkeeping revised |

## Security Risk Assessment

- **Risk level:** `low`
- **Why this risk level:** parser local read-only; riscos são path escape ou conteúdo sensível em diagnóstico.
- **Attack surface in scope:** filesystem paths and Markdown content inside Foundation root.
- **Attack simulation decision:** `not_needed`
- **Review evidence:** audit floor `SEC-NOT-TRIGGERED`; code/final review ainda verificará root confinement, ausência de shell interpolation e secret-value echo.
- **Residual security risk:** malformed Markdown may deny validation by design; diagnostics must remain bounded.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `none`
- **Why this level:** pequeno conjunto Markdown local; sem endpoint/query/async/concurrency/runtime.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `n/a — no endpoint` | `before_local_implemented` | `EPS-E1` | `not_applicable` | `none` | `none` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `n/a — no frontend` | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `n/a — no backend mutation` | `before_local_implemented` | `BCI-INV` | `not_applicable` | `none` | `none` |
| `RLS` | `runtime-load-stress-validation` | `not_needed` | `low` | `n/a — local docs tooling` | `before_production_ready` | `RLS-E1` | `not_applicable` | `none` | `none` |

### Lane Detail Packets

#### `EPS`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** no endpoint, repository query or data-access path is changed.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

#### `FRC`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** no frontend, async UI or retriggerable user flow is changed.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

#### `BCI`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** validator is read-only and does not create backend mutation/idempotency surfaces.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

#### `RLS`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** no runtime/queue/worker/realtime/bulk production path or SLO claim changes.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

## Verification Debt Assessment

- **Audit decision:** `required because complexity=medium`
- **Audit status:** `not_run`
- **Why this outcome:** guard logic/assertions can create hidden false-green debt.
- **Inline code TODO debt:** `pending implementation scan`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none planned`

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** validator trust depends on mutation coverage and negative assertions.
- **Trigger signals in scope:** `complexity=medium; touches_tests=yes; fail-closed enforcement`
- **Required evidence matrix:** each `DOD-02/03/05` scenario, expected failure and assertion quality.
- **Audit status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** enforcement determinístico deve ser desafiado após implementação.
- **Impact signals in scope:** `cross-stack governance; architecture protection harness; tests`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen decisions, diff, test/mutation outputs, adherence e audits.
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Review focus:** `adherence|regressions|validation evidence|security/performance residuals|elegance|structural soundness|verification debt`
- **Final review status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** material review findings were integrated; revised decisions require renewed human validation, refreeze and fresh reviews.
- **Post-commit/push status:** `refined Review contract committed locally; publication pending because the current environment has no GitHub HTTPS credentials; no implementation claim`
- **Next path/status action:** obtain renewed validation of `D-01..D-10`, then refreeze and rerun all planning-side gates; no implementation before a later post-gate APROVADO and authority guard `go`.

## Commands

### Planning / pre-approval

- `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md --pre-approval`
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py --repo-root foundation_documentation foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`

### Planned implementation validation

- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'`
- `python3 -m py_compile foundation_documentation/deterministic/validate_foundation_lifecycle.py foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`
- `git -C foundation_documentation diff --check`

## Files Expected

- `foundation_documentation/deterministic/validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/README.md`
- `foundation_documentation/evolution_lifecycle.md`
- `foundation_documentation/README.md`
- este TODO e seu rename para `todos/completed/process/` no closeout.
