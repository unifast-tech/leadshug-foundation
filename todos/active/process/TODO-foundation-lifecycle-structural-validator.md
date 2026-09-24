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
- **Next exact step:** publicar a replacement baseline congelada e repetir architecture opinion, plan critique e guards sobre TODO mais owners canônicos explícitos.

## Active Work State

- **Work state:** `review`
- **Why this state now:** `D-01..D-11` foram validadas; a replacement baseline precisa ser congelada/publicada antes dos reviews e guards pré-aprovação.
- **Exit condition:** decisões validadas, baseline congelada/publicada, reviews e guards pré-aprovação verdes, seguidos de `APROVADO` explícito ou cancelamento com racional.

## Trigger Evidence

- **Trigger:** mais de dez registros vivos combinados em backlog, decisões e roadmap.
- **Observed count:** `18` em 2026-09-23 (`3` candidatos + `11` decisões `Accepted` + `4` linhas de roadmap).
- **Source:** [ST-01 D-09](../../completed/process/TODO-leadshug-foundation-evolution-lifecycle.md) e [Deterministic-adoption trigger](../../../evolution_lifecycle.md#deterministic-adoption-trigger).
- **Execution authority:** `none`; abertura e refinamento do TODO não equivalem a `APROVADO`.

## Scope

- [ ] `S-01` Criar `deterministic/validate_foundation_lifecycle.py`, executável com Python standard library, que derive estado vivo dos owners canônicos e mantenha somente um bootstrap trust kernel versionado para provar que owners/surfaces/schemas obrigatórios não foram removidos.
- [ ] `S-02` Validar fail-closed o bootstrap kernel, headings/tabelas, schemas/colunas obrigatórias e enums do source graph enumerado para lifecycle, backlog, decisões e roadmap.
- [ ] `S-03` Validar sintaxe e unicidade dos IDs `BLG-*` e `DEC-*` somente nos registros autoritativos admitidos, permitindo referências repetidas fora do owner; `CAP-*` fica fora deste slice.
- [ ] `S-04` Validar owner singular por registro admitido, links Markdown e decision-target paths confinados/resolvíveis; campos de dependência/next-gate em prosa são obrigatórios, mas não fingem ser IDs resolvíveis.
- [ ] `S-05` Distinguir decisão `Accepted` válida porém `pending-effect` de structurally eligible for effectiveness por uma gramática posicional explícita: cada target possui exatamente um segmento de evidência; o sentinel literal `PENDING` é válido e mantém pending-effect; ausência, duplicidade, placeholder diferente do sentinel ou contradição falham.
- [ ] `S-06` Preservar a exceção histórica por construção e provar completude: o conjunto de links em `decisions/README.md` deve ser exatamente igual aos arquivos `decisions/*.md` no nível raiz, exceto `README.md`; subdiretórios permanecem históricos/não admitidos até TODO material alterar o boundary.
- [ ] `S-07` Criar testes test-first positivos e mutation/fail-first negativos, com oráculos independentes do parser, fixtures temporárias e prova byte-for-byte read-only.
- [ ] `S-08` Documentar owner, comando, cobertura, códigos de saída e mensagens de diagnóstico em `deterministic/README.md`, além de atualizar o lifecycle e o índice raiz com o handoff canônico.
- [ ] `S-09` Substituir os exact checks do ST-01 somente após validar um candidate SHA que já contenha código, testes e handoffs, mas ainda não alegue cutover; após review/publicação/movimento do TODO, rerodar validator/tests/guards no closeout SHA antes da declaração final.

## Out of Scope

- [ ] `OOS-01` Alterar backend, frontend, banco, runtime, Docker, Railway, CI/CD ou contratos de produto do LeadsHug.
- [ ] `OOS-02` Editar workflows de GitHub Actions ou alegar integração remota neste TODO.
- [ ] `OOS-03` Reabrir/reformular a direção de decisões `D-01..D-11` do ST-01 ou mudar seus enums/schemas; validação estrutural não adjudica verdade semântica da consolidação.
- [ ] `OOS-04` Retroajustar TODOs concluídos, artifacts históricos ou documentos legados apenas para fazê-los passar no novo validator.
- [ ] `OOS-05` Copiar contagens, títulos, disposições ou conteúdo específico do ST-01 para o código do validator como verdade permanente.
- [ ] `OOS-06` Criar configuração paralela editável ou copiar registros vivos; o bootstrap kernel v1 é uma assertion de compatibilidade versionada e só muda junto com uma alteração material do contrato canônico.
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
- [ ] `DOD-03` Mutations detectam estrutura Markdown ambígua, ID inválido/duplicado, enum inválido, coluna/owner ausente, link/anchor/target inválido, path/symlink escape, sentinel/evidência 1:1 ausente/duplicada/contraditória e output não redigido; referências repetidas válidas e `PENDING` explícito passam.
- [ ] `DOD-04` O validator deriva estado vivo dos documentos canônicos e mantém apenas o bootstrap kernel v1 documentado — paths de owners, surfaces/headings, schemas/colunas e enums obrigatórios — sem copiar registros vivos, contagens, títulos ou disposições.
- [ ] `DOD-05` Testes provam igualdade bidirecional entre o index de decisões e `decisions/*.md`, com mutations de unlink, orphan e duplicate-link; histórico em subdiretórios fica ignorado até mudança material do boundary.
- [ ] `DOD-06` `deterministic/README.md`, `evolution_lifecycle.md` e `README.md` apontam para um único comando e declaram que CI remoto não foi alterado.
- [ ] `DOD-07` O candidate SHA contendo implementação, testes e handoffs passa dual-run old/new sem ainda declarar substituição; após audits, publicação e `active XOR completed`, o closeout SHA reroda validator/tests/guards e somente então declara o cutover.
- [ ] `DOD-08` Diff expectation, decisões, evidence matrix, audits, crítica, test-quality audit, final review e closeout guards estão completos e verdes.

## Validation Steps

- [ ] `VAL-01` Executar `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` e exigir exit `0` com resumo determinístico.
- [ ] `VAL-02` Executar `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` e exigir todos os testes verdes.
- [ ] `VAL-03` Executar a Test Rule Matrix inteira, incluindo bootstrap deletion, unlink/orphan decision records, root confinement, symlink/`..` escape, anchor dialect, Unicode/HTML, read-only byte snapshot, `PENDING` válido e evidência contraditória.
- [ ] `VAL-04` Executar `python3 -m py_compile foundation_documentation/deterministic/validate_foundation_lifecycle.py foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`.
- [ ] `VAL-05` Executar separadamente `git diff --check`, diff expectation guard e scan redigido de secret/private-key patterns; nenhum comando isolado pode alegar as três capacidades.
- [ ] `VAL-06` Executar diff, authority, completion e closeout guards; exigir `go` antes do movimento final e provar todos os deliverables esperados mais exclusividade `active XOR completed`.
- [ ] `VAL-07` No candidate SHA que já contém código/testes/handoffs, executar os Exact Check Command Contracts aplicáveis do ST-01 (`VAL-01`, `VAL-02`, `VAL-08`, `VAL-10`) e o novo validator/tests; exigir dual-run verde antes de declarar substituição.
- [ ] `VAL-08` Após publicação e movimento `active -> completed`, rerodar validator, unittest, diff/authority/completion/closeout guards no closeout SHA e só então registrar a declaração final de cutover.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01..S-09` | Scope | implementação e adoção documental do validator | code+test+doc | paths esperados + `VAL-01..VAL-05` | local Foundation | planned | expandir 1:1 após implementação |
| `DOD-01..DOD-08` | Definition of Done | critérios de entrega | test+review | comandos e gates correspondentes | local Foundation | planned | evidência agregada não substituirá linhas finais 1:1 |
| `VAL-01..VAL-08` | Validation Steps | comandos obrigatórios | test | stdout/exit e referências versionadas | local Foundation | planned | registrar candidate SHA, closeout SHA, comando e resultado |

## External Dependency Readiness

- **Decision:** `required only for publication/Production-Ready; not needed for local implementation`
- **Rationale:** parser/tests usam apenas arquivos locais, mas freeze e closeout exigem `origin/main`; GitHub/origin deve estar acessível e sincronizado antes dessas alegações.
- **Current evidence:** `origin/main@e43658ef59b87dc6eec8b4b446781a02ac48abeb` contains the reviewed `D-01..D-10` package; the reconverged `D-01..D-11` working state still requires publication after validation.

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
| bootstrap trust kernel v1 in validator | fixed identities for the four owner files; lifecycle authority/state-machine headings; exact table columns; required current enums | removal, duplication or rename fails until a material contract update changes kernel and lifecycle together | immutable parser trust root only; never stores live record IDs/counts/titles/dispositions |
| `evolution_lifecycle.md` | `Authority matrix`, five `State machines`, `Historical-document exception`, `Deterministic-adoption trigger` | kernel-required headings/schemas/enums present and unique; authority rows unique | canonical semantic owner; validator kernel proves the v1 contract was not silently weakened |
| `backlog/README.md` | `## Candidates` | exact eight-column table; unique `BLG-*`; state from Candidates enum; nonempty fields | Markdown links resolve; freeform Dependencies/Next gate are required prose, not IDs |
| `decisions/README.md` | `## Records` | normalized record links are unique and exactly equal root-level `decisions/*.md` except `README.md` | immediate-child discovery exists only to prove index completeness; decision subdirectories are historical/unadmitted |
| indexed root-level decision record files | unique decision table | exact six columns; unique `DEC-*`; state from Decisions enum | targets and semicolon-delimited evidence segments map positionally 1:1; semantics remain review-owned |
| `system_roadmap.md` | unique six-column roadmap table | unique phase rows; valid Horizon/Gate status; nonempty dependencies/outcome/exit gate | prose dependencies are required but not treated as resolvable IDs |

### Narrow Markdown Grammar (Revised Contract)

- UTF-8 strict input; reject undecodable bytes and hidden Unicode format controls in identifiers, enum values and paths.
- Required headings/tables are unique; duplicate/missing/reordered headers or row cardinality mismatch fail closed.
- Pipe tables are parsed structurally with inline code/link awareness; ambiguous escaped pipes/code spans fail with a diagnostic instead of silent token shifting.
- Markdown paths and decision targets must be relative, remain under `--root`, resolve without absolute paths, `..` escape or symlink escape, and never cause content echo in diagnostics.
- Fragment links use a constrained v1 dialect: ASCII heading text only; lowercase; spaces and ASCII punctuation become a single `-`; leading/trailing `-` removed; duplicate normalized headings fail; percent-encoded fragments, Unicode-derived fragments and HTML anchors are rejected rather than guessed.
- Discovery depth is exactly the source graph above. Historical/completed/artifact content can be a resolved reference target without becoming a scanned live owner.
- Decision targets and target-consolidation evidence are split on semicolons outside inline code/links and mapped positionally. Exactly one evidence segment is required per target: literal `PENDING` yields valid `pending-effect`; a concrete non-placeholder segment yields structural coverage; missing/extra/duplicate/contradictory segments fail. Complete structural coverage is `structurally-eligible`, never a semantic truth claim.

## Decision Pending

- `none — reconverged D-01..D-11 validated by Gabriel/user on 2026-09-23 through the exact phrase VALIDO D-01..D-11; this validates the planning contract but does not grant implementation authority.`

## Decisions

- [x] `D-01` Admit only the explicit source graph; validate `BLG-*` and `DEC-*`; exclude `CAP-*`, modules, TODO records and contract-verification records.
- [x] `D-02` Keep lifecycle as semantic owner while a versioned bootstrap trust kernel hard-codes only mandatory owner identities, headings, schemas/columns and current required enums; never live records or dispositions.
- [x] `D-03` Keep the validator read-only/fail-closed with root/symlink confinement, byte preservation and bounded/redacted diagnostics.
- [x] `D-04` Define current decisions bidirectionally: index links must equal root-level `decisions/*.md` except README; subdirectories remain historical until a material boundary change.
- [x] `D-05` Deliver local validation only; CI-equivalent remains `n/a`; remote CI integration stays in another TODO.
- [x] `D-06` Use Python stdlib + unittest, test-first, independent fixture oracles and a 1:1 rule/mutation matrix.
- [x] `D-07` Keep ownership project-specific in Foundation and route implementation to routine-executor; no `delphi-ai` implementation changes.
- [x] `D-08` Validate old/new on a candidate SHA already containing handoffs but no cutover claim; after reviews/publication/TODO move, rerun closeout checks and declare cutover only on the closeout SHA.
- [x] `D-09` Require exactly one positional evidence segment per target: literal `PENDING` is valid pending-effect; concrete non-placeholder evidence is structural coverage; missing/extra/duplicate/contradictory mapping fails.
- [x] `D-10` Treat prose dependencies/next gates as required nonempty text; validate only explicit Markdown paths/fragments as resolvable references.
- [x] `D-11` Use the constrained ASCII heading-fragment dialect defined above; reject percent-encoded, Unicode-derived and HTML anchors instead of emulating an unspecified renderer.

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

- **Prior freezes:** `D-01..D-08@b685fb52` invalidated by `AR-01..05/F-01..11`; `D-01..D-10@504a9785` published and invalidated by `AR-R01..AR-R05/F-12..F-17`.
- **Freeze status:** `frozen-locally — publication required before planning-side reviews`
- **Frozen decisions:** `D-01..D-11`
- **Validation evidence:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-11`; planning-contract validation only, not implementation approval.
- **Prior validation evidence:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-10`; preserved as provenance but superseded by the material review findings.
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
| canonical-source derivation + trust root | `D-02` | parser e regras | deriva estado vivo e impede que o próprio contrato obrigatório seja silenciosamente removido |
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
- **Decision review evidence / resolution:** `/root/validator_architecture_revalidation`, 2026-09-23: `AR-R01..AR-R05` classificados como release-blocker e integrados; nova validação, freeze e architecture opinion ainda são obrigatórios.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `AR-R01` | Integrated | useful | yes | project | n/a | bootstrap trust kernel v1 added without live-record duplication |
| `AR-R02` | Integrated | useful | yes | project | n/a | decisions index and root-level record set must be exactly equal |
| `AR-R03` | Integrated | useful | yes | project | n/a | explicit `PENDING` sentinel and positional mapping truth table added |
| `AR-R04` | Integrated | useful | yes | project | n/a | constrained ASCII heading-fragment dialect defined |
| `AR-R05` | Integrated | useful | yes | none | n/a | lifecycle/status fields returned to renewed-validation state |

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
- **Trigger stage:** `after D-01..D-11 validation and before renewed planning-side reviews`
- **Baseline branch:** `main`
- **Baseline commit:** `2562f62e86cbc15bcaa7865b652e240cb49fcb0e`
- **Baseline push reference:** `pending publication to origin/main`
- **Gate status:** `frozen-locally-pending-publication`
- **Findings summary:** validated `D-01..D-11` were frozen locally; reviews remain blocked until publication.
- **Evidence / reference:** local commit `2562f62e86cbc15bcaa7865b652e240cb49fcb0e`, 2026-09-23.
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

- `none — Q-02 closed by Gabriel/user on 2026-09-23 with VALIDO D-01..D-11.`

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

1. Após validação humana, congelar `D-01..D-11`, publicar replacement baseline e repetir plan/architecture reviews com TODO + todos os owners do source graph no pacote.
2. Após `APROVADO` e authority guard `go`, escrever primeiro fixtures/oráculos fail-first e então implementar bootstrap kernel, parser e diagnostics read-only.
3. Implementar as regras até `T-01..T-14` convergirem, mantendo estado vivo somente nos owners canônicos.
4. Documentar comando/boundary/exit contract e atualizar handoffs no candidate SHA, sem ainda declarar cutover.
5. Executar validator, unittest, py_compile, hygiene e old/new dual-run no candidate SHA; depois executar adherence/audits/final review.
6. Publicar o pacote aprovado e mover o TODO para `completed/process/` somente com deliverables existentes e `active XOR completed`.
7. Rerodar validator/tests/guards no closeout SHA e então registrar o cutover permanente.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** validator e testes podem compartilhar o mesmo erro; cada regra deve falhar contra uma fixture/mutation independente antes do código que a satisfaz.
- **Fail-first targets:** bootstrap weakening, source graph/headers, index↔record completeness, table cardinality, BLG/DEC syntax+uniqueness, enums, link/anchor/path confinement, `PENDING` versus structurally-eligible mapping, historical exclusion/admission, Unicode/HTML, bounded/redacted diagnostics e byte-for-byte read-only.
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
| `T-06` | valid relative path under root | missing path, absolute, `..`, symlink escape | non-zero without content leak |
| `T-07` | one literal `PENDING` segment per pending target | explicit pending mapping | remains zero + pending-effect classification |
| `T-08` | complete 1:1 concrete mapping | missing/extra/duplicate/placeholder/contradictory segment | non-zero; never semantic-effective claim |
| `T-09` | invalid historical file in decision subdirectory | historical file remains unindexed | remains zero |
| `T-10` | index links equal root-level record files | unlink, orphan file or duplicate link | non-zero + membership diagnostic |
| `T-11` | bounded/redacted diagnostic | secret-like fixture payload | diagnostic omits value and respects limit |
| `T-12` | read-only tree | full validation pass/fail | byte hashes and symlink metadata unchanged |
| `T-13` | complete bootstrap kernel surfaces | remove mandatory owner, heading, schema column or enum member | non-zero + kernel/version diagnostic |
| `T-14` | valid constrained ASCII fragment | duplicate slug, Unicode/encoded/HTML fragment, punctuation/case mismatch | deterministic pass/fail per v1 dialect |

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
| unittest/mutations | `T-01..T-14` | isolated temporary fixtures | `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` | Local-Implemented | planned |
| candidate parity | old exact checks + new validator/tests agree | candidate SHA already contains code/tests/handoffs but no cutover claim | ST-01 `VAL-01/02/08/10` exact contracts + commands above | before delivery reviews | planned |
| closeout confirmation | permanent checks stay green after TODO move/publication bookkeeping | closeout SHA with `active XOR completed` | validator + unittest + diff/authority/completion/closeout guards | Production-Ready | planned |

### Runtime / Rollout Notes

- `n/a — no runtime, migration, deploy, secret, database, browser or device surface`
- Exact checks ST-01 permanecem requeridos até o novo comando passar e ser publicado.

## Plan Review Gate

- **Status:** `findings_integrated — AR-R01..AR-R05/F-12..F-17 reconverged; D-01..D-11 await human validation, replacement freeze and fresh review`
- **Required lenses:** Architecture, Code Quality, Tests, Performance, Security, Elegance, Structural Soundness.
- **Expected focus:** evitar parser frágil, catálogo duplicado, cobertura superficial, bypass histórico e expansão para CI.

### Review Sections

- [x] Architecture — trust kernel, bidirectional membership, evidence truth table and anchor dialect integrated.
- [x] Code Quality — narrow grammar, confinement and diagnostics contract added.
- [x] Tests — test-first and `T-01..T-14` matrix added.
- [x] Performance — bounded linear scan; no specialized lane triggered.
- [x] Security — root/symlink confinement and redaction made mandatory.
- [x] Elegance — one project-owned stdlib validator; no parallel catalog.
- [x] Structural Soundness — two-SHA cutover, membership completeness and trust-root protection added.

### Issue Cards

- **Issue ID:** `PLAN-01` — decision validity/effectiveness conflated (`high`). Option A: structural `pending-effect`/eligible split (recommended, medium effort/low risk/local blast/low maintenance/neutral performance/high elegance+soundness); Option B: atomic Accepted (high effort/risk/cross-doc); Option C: do nothing (high false-block risk). **Resolution:** integrated into `D-09`, `S-05`, `T-07/08`.
- **Issue ID:** `PLAN-02` — open scan universe/history (`high`). Option A: explicit source graph + grammar (recommended, medium effort/low risk); Option B: hard-code snapshot (low effort/high maintenance); Option C: broad scan (high false-positive risk). **Resolution:** integrated into source graph, `D-01/02/04/10`.
- **Issue ID:** `PLAN-03` — parser/read-only/security proof incomplete (`high`). Option A: mandatory narrow grammar, confinement, redaction and byte snapshot (recommended, medium effort/low risk); Option B: external parser (medium supply-chain risk); Option C: do nothing (high false-green risk). **Resolution:** integrated into `D-03/06`, `T-01..T-12`.
- **Issue ID:** `PLAN-04` — cutover/test/routing evidence incomplete (`high`). Option A: test-first + dual-run + exact implementation routing (recommended, medium effort/low risk); Option B: cut over after new-only local green (medium risk); Option C: do nothing (control gap). **Resolution:** integrated into `D-05/07/08`, matrices and routing.
- **Issue ID:** `PLAN-05` — mutable source graph could self-weaken (`high`). Option A: minimal versioned bootstrap trust kernel (recommended, medium effort/low runtime risk); Option B: duplicate all live truth (high drift); Option C: self-derived only (high false-green risk). **Resolution:** integrated into `D-02`, source graph, `DOD-04`, `T-13`.
- **Issue ID:** `PLAN-06` — index-only decision admission permits silent unlink (`high`). Option A: exact equality with root-level decision files (recommended, low effort/low risk); Option B: dedicated directory migration (higher scope); Option C: keep index-only (false-green). **Resolution:** integrated into `D-04`, `S-06`, `DOD-05`, `T-10`.
- **Issue ID:** `PLAN-07` — pending mapping pass/fail contradiction (`high`). Option A: explicit positional `PENDING` sentinel (recommended, low effort/clear oracle); Option B: new schema columns (higher migration scope); Option C: infer from prose (ambiguous). **Resolution:** integrated into `D-09`, grammar, `T-07/08`.
- **Issue ID:** `PLAN-08` — renderer anchor dialect unspecified (`medium`). Option A: constrained ASCII v1 grammar (recommended, low complexity); Option B: emulate GitHub fully (higher maintenance); Option C: skip anchors (coverage gap). **Resolution:** integrated into `D-11`, grammar, `T-14`.
- **Issue ID:** `PLAN-09` — same-SHA cutover chronology impossible after TODO move (`medium`). Option A: candidate SHA parity plus closeout SHA rerun (recommended); Option B: single mutable claim (contradictory); Option C: no parity. **Resolution:** integrated into `D-08`, `DOD-07`, `VAL-07/08`.

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

- **Needed:** `yes — rerun after D-01..D-11 replacement freeze`
- **Why ambiguity remains:** os findings materiais foram integrados, mas a arquitetura reconvergida precisa de nova confirmação independente sobre o pacote completo de owners.
- **Opinion count:** `1 completed with material findings; 1 fresh rerun pending`
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
| `high_severity_plan_review_issue` | `yes` | `PLAN-01..09` include integrated high findings; fresh review still required |
| `explicit_three_lane_request` | `no` | não solicitado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** piso esperado para medium, cross-stack governance e test logic.
- **Impact signals in scope:** `cross-stack documentary governance; deterministic enforcement; tests`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen TODO plus exact baseline-bound contents of `evolution_lifecycle.md`, `backlog/README.md`, `decisions/README.md`, every linked root-level decision record, `system_roadmap.md`, assumptions, plan, issue cards and risks.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Canonical multi-lane audit protocol:** `n/a — deterministic floor says triple_review=not_needed`
- **Audit session / round evidence:** `n/a unless triggered`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `findings_integrated`
- **Findings summary:** prior `F-01..F-11` plus renewed `F-12..F-17` integrated; the latest review found the package approval-not-ready and requires renewed validation, replacement freeze and a full-owner fresh critique.
- **Resolution ledger:** prior findings are recorded individually below for deterministic carry-forward.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `F-01` | Integrated | useful | yes | project | n/a | canonical six-column assumptions schema now covers `A-01..A-05` |
| `F-02` | Integrated | useful | yes | project | n/a | explicit source graph and opaque-prose dependency boundary added in `D-01/D-02/D-10` |
| `F-03` | Integrated | useful | partial | project | n/a | `D-09` separates valid `pending-effect` from structural eligibility and semantic truth |
| `F-04` | Integrated | useful | yes | project | n/a | historical admission is now decided only through the explicit source graph |
| `F-05` | Integrated | useful | yes | none | n/a | earlier review-order defect caused renewed validation, refreeze and fresh-review requirement |
| `F-06` | Integrated | useful | yes | project | n/a | cutover now requires same-SHA dual-run, deliverable existence and `active XOR completed` |
| `F-07` | Integrated | useful | yes | project | n/a | test-first strategy and `T-01..T-12` positive/mutation matrix added |
| `F-08` | Integrated | useful | yes | project | n/a | whitespace, diff-scope and secret hygiene validations are separated in `VAL-05` |
| `F-09` | Integrated | useful | yes | none | n/a | planned implementation routing now names `routine-executor` with single-writer/no-worktree topology |
| `F-10` | Integrated | useful | yes | project | n/a | CI-equivalent is explicitly `n/a`; local validator/unittest evidence has its own matrix |
| `F-11` | Integrated | useful | yes | none | n/a | lifecycle, freeze, approval and closeout state were reconciled before renewed validation |
| `F-12` | Integrated | useful | yes | paced | n/a | future dispatch package must contain the exact canonical owner files, not the TODO alone |
| `F-13` | Integrated | useful | yes | paced | n/a | all lifecycle fields now return to renewed-validation and replacement-freeze state |
| `F-14` | Integrated | useful | yes | project | n/a | explicit positional `PENDING` truth table removes pass/fail contradiction |
| `F-15` | Integrated | useful | yes | project | n/a | bidirectional decisions index/root-file equality proves live membership completeness |
| `F-16` | Integrated | useful | yes | project | n/a | candidate SHA parity and closeout SHA rerun establish coherent cutover ordering |
| `F-17` | Integrated | useful | yes | project | n/a | constrained ASCII fragment dialect supplies independent test oracle |

- **Evidence / reference:** `/root/validator_plan_revalidation`, 2026-09-23; `overall_assessment=material_findings_present; approval_not_ready`.
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
- **Approval scope:** `pending after D-01..D-11 validation and planning gates`
- **Execution not authorized by approval:** `CI/CD, product/runtime, historical rewrites, delphi-ai changes, worktrees or auxiliary checkouts unless separately named`
- **Renewed approval required when:** scope, invariant semantics, validation, expected paths, architecture, risk, exception or CI adoption changes materially.
- **Execution authority:** `not_granted`
- **Pre-gate human token:** Gabriel/user, 2026-09-23, `APROVADO`; it validated the superseded `D-01..D-08` only. Material findings require renewed validation and a new post-gate `APROVADO`.
- **Renewed validation token:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-10`; validates the revised decisions, but does not grant implementation authority.
- **Renewal status:** `satisfied for replacement freeze by the D-01..D-11 validation token; post-gate APROVADO remains required.`
- **Latest validation token:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-11`; validates the reconverged decisions, but does not grant implementation authority.

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
| `D-01..D-11` | pending-validation | reconverged TODO contract | expand 1:1 only after replacement freeze and approval |

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
| `AR-R01..AR-R05` | high/medium | release-blocker | integrate in current TODO | mesma arquitetura do validator; trust root, membership, mapping, anchors e state bookkeeping | fixed-pending-revalidation | reconverged `D-02/D-04/D-08/D-09/D-11`; fresh review required |
| `F-12..F-17` | high/medium | release-blocker | integrate in current TODO | mesmos approval/readiness boundaries; nenhum split necessário | fixed-pending-revalidation | full-owner package, lifecycle state, mapping, membership, cutover and anchor grammar revised |

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
- **Post-commit/push status:** `reconverged D-01..D-11 frozen locally; replacement publication pending; no implementation claim`
- **Next path/status action:** publish the replacement freeze and rerun all planning-side gates with the full owner package; no implementation before a later post-gate APROVADO and authority guard `go`.

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
