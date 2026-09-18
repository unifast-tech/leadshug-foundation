# TODO — LeadsHug: Foundation evolution lifecycle and predictability model

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`

## Context

A Foundation atual define autoridade, entidades, constituição, quatro fases de roadmap, módulos e execução por TODO, mas não torna suficientemente visíveis o estado das capacidades, horizontes, dependências, decisões e transições entre descoberta e entrega. O ST-01 do programa pré-código estabelece essa arquitetura da informação antes dos estudos de Central-Whatsapp e `whatsflow_v2` avançarem.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md`
- **Primary story ID:** `ST-01`
- **Why this is the right current slice:** define onde e como as descobertas dos ST-02/ST-03 serão registradas sem virarem implementação ou autoridade prematuramente.
- **Direct-to-TODO rationale:** `n/a`

## Contract Boundary

- Este TODO altera somente a autoridade documental da Foundation e sua validação estrutural.
- Nenhum código, teste, schema, runtime, CI/CD ou comportamento do produto será alterado.
- Descobertas de produto permanecem não autorizadas até terem decisão, roadmap e TODO próprios.
- Qualquer mudança de vocabulário de domínio, contrato de produto ou ownership de módulo exige outro TODO e nova aprovação.

## Implementation Intent

- **Current delivery:** estabelecer lifecycle de evolução, backlog pré-TODO, registro de decisões, roadmap orientado a resultados e estrutura previsível dos documentos de módulo/contrato.
- **Planned next steps:** `ST-02`, `ST-03` e `ST-04`, informativos e não autorizados por este TODO.
- **Anticipatory implementation authorized now:** registrar os três próximos estudos como candidatos de backlog, sem iniciar sua execução.
- **Rationale:** a estrutura deve existir antes de receber novos estudos; isso evita que artefatos de descoberta sejam confundidos com decisões ou TODOs aprovados.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** congelar e publicar o baseline deste TODO antes de iniciar os reviews de planejamento.

## Active Work State

- **Work state:** `review`
- **Why this state now:** o contrato está em preparação para o baseline freeze e para os gates independentes anteriores ao `APROVADO`.
- **Exit condition:** review baseline, crítica, coherence, scope-drift e authority preflight aprovados; então solicitar `APROVADO`.

## Scope

- [ ] Criar `evolution_lifecycle.md` como contrato canônico do fluxo descoberta → candidato → planejamento → aprovação → entrega → encerramento.
- [ ] Criar `backlog/README.md` como autoridade de trabalho candidato ainda não aprovado e registrar ST-02, ST-03 e ST-04 como itens independentes.
- [ ] Criar `decisions/README.md` como registro navegável de decisões duráveis e definir seus estados.
- [ ] Evoluir `system_roadmap.md` para horizontes relativos, estado, dependências, resultado esperado e critério de saída, preservando as quatro fases estratégicas.
- [ ] Evoluir `modules/README.md` e os quatro módulos atuais com uma estrutura mínima comum de ownership, maturidade, capacidades, lacunas, dependências, decisões e contratos.
- [ ] Evoluir `contracts/README.md` para um catálogo de contratos e seus estados, sem inventar contratos ainda não verificados.
- [ ] Alinhar `README.md`, `project_constitution.md`, `todos/README.md` e `artifacts/README.md` ao novo lifecycle.
- [ ] Atualizar o feature brief com a disposição do ST-01 e links canônicos, sem retirar ST-02/ST-04 do seu escopo original.
- [ ] Validar a navegação completa com um cenário real: ST-03 nasce em descoberta, entra no backlog e permanece sem autoridade de execução.

## Delivery Status Semantics

- `Pending`: nenhum marco material de entrega foi atingido.
- `Local-Implemented`: documentos canônicos foram alterados e validados localmente.
- `Lane-Promoted`: `foundation_documentation/main` contém a entrega publicada.
- `Production-Ready`: equivalente a `Lane-Promoted` para esta entrega estritamente documental, após todos os gates.
- `Blocked`: a execução não pode avançar; as notas de bloqueio são obrigatórias.

## Branch Recovery Evidence

- **User authorization:** `2026-09-18 — Autorizo`.
- **Recovered branch state:** `foundation_documentation/main` está anexada a `origin/main@11842b251a84681346936f93488c7cc738d98992`.
- **Preserved divergent ref:** bundle completo em `/mnt/c/Unifast/LeadsHug/.migration-staging/20260918/foundation-local-main-dc860a05705558b5a2ae3cf5b0d513384932fe48.bundle`, SHA-256 `5b3b090b4cdeda1bd495472d931750988ba73a9abb7316dc4c449edc27918602`.
- **Working-tree backup:** `/mnt/c/Unifast/LeadsHug/.migration-staging/20260918/foundation-working-tree-before-reanchor-11842b25.tar.gz`, SHA-256 `d962040d97325e455b5c42fcea7d23e0ebae3fbd0008bfe70969dfcb73244748`.
- **Preservation proof:** aggregate content hash before and after reanchor `3df15ea7391cbd18cc743af4c7a6063c3e10db73954a8d0f888fabca0886ef48`.
- **Remote freshness:** `git.exe fetch origin --prune` succeeded using the configured Windows credential manager; `origin/main` remained `11842b25`.
- **Guard note:** the shared installer could not run because its checked-out shell files have CRLF line endings; manual branch/worktree checks passed and this issue is not repaired inside ST-01.

## Execution Lane Tracking

- **Local implementation branches:** `foundation_documentation:main` após o desbloqueio; nenhuma branch auxiliar autorizada.
- **Promotion lane path:** `foundation_documentation/main` como autoridade documental única.
- **Lane-promoted threshold for this TODO:** commit enviado a `origin/main`.
- **Production-ready threshold for this TODO:** mesmo commit confirmado em `origin/main`, com guards e revisão final aprovados.

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Foundation evolution lifecycle | `foundation_documentation:main@pending` | `n/a — main-only authority` | `n/a` | `direct governed Foundation write; pending` | `blocked` |

## Out of Scope

- [ ] Alterar código, testes, schema, runtime ou configuração do LeadsHug.
- [ ] Executar os estudos ST-02, ST-03 ou a síntese ST-04.
- [ ] Canonizar conceitos de canal, fila, equipe, setor, SLA, automação ou IA.
- [ ] Inventariar todos os endpoints ou afirmar cobertura contratual sem evidência.
- [ ] Reescrever artifacts, TODOs concluídos ou decisões históricas retroativamente.
- [ ] Limpar, normalizar ou incluir mudanças preexistentes não pertencentes a este TODO.
- [ ] Criar worktree, branch auxiliar, checkout alternativo ou cópia gravável da Foundation.

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`, complementado por hashes dos arquivos preexistentes não pertencentes ao TODO.

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `foundation_documentation` | `origin/main@11842b251a84681346936f93488c7cc738d98992` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `evolution_lifecycle.md` | `A` | contrato canônico do lifecycle |
| Foundation | `backlog/**` | `A` | intake pré-TODO e candidatos ST-02/ST-03/ST-04 |
| Foundation | `decisions/**` | `A` | registro de decisões duráveis |
| Foundation | `README.md` | `M` | navegação e autoridade |
| Foundation | `project_constitution.md` | `M` | invariantes do lifecycle |
| Foundation | `system_roadmap.md` | `M` | previsibilidade e horizontes |
| Foundation | `modules/**` | `M` | estrutura mínima e rastreabilidade |
| Foundation | `contracts/README.md` | `M` | catálogo e estados de contrato |
| Foundation | `artifacts/README.md` | `M` | distinção entre descoberta e evidência |
| Foundation | `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` | `A|M` | framing e disposição do ST-01 |
| Foundation | `todos/README.md` | `M` | corrigir lifecycle e backlog |
| Foundation | `todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md` | `A|M|D` | contrato, evidência e closeout deste trabalho |

### Pre-existing Paths To Preserve Byte-for-Byte Unless Separately Authorized

| Path | Initial state | Treatment |
| --- | --- | --- |
| `.gitattributes`, `.gitignore`, `artifacts/migration/claude-legacy-reconciliation-review.prompt.txt`, `artifacts/publication-manifest.txt`, `deterministic/.gitkeep` | modified before ST-01 | do not edit; verify hashes at delivery |
| `todos/ephemeral/`, `todos/promotion_lane/` | untracked before ST-01 | do not edit; preserve |
| `todos/active/process/TODO-leadshug-engineering-and-foundation-publication-baseline.md` | deleted by prior explicit cancellation request | preserve deletion; do not absorb into ST-01 |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| API | `api-app/**` | `any` | product code is out of scope |
| Web | `web-app/**` | `any` | product code is out of scope |
| Engineering | `delphi-ai/**` | `any` | agnostic method is out of scope |
| References | `C:/Unifast/LeadsHug/Inspirações LeadsHug/**` | `any` | references are read-only |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** refinements de títulos, links, campos e exemplos necessários para tornar o mesmo lifecycle coerente e navegável.
- **Must update or split the TODO:** novo comportamento de produto, mudança de domínio, validator executável novo, inventário completo de APIs, estudo comparativo ou decisão de canal/atendimento.

## Definition of Done

- [ ] `DOD-01` Existe uma fonte canônica única para lifecycle, estados, transições, autoridades e critérios de promoção.
- [ ] `DOD-02` Ideias não aprovadas possuem uma superfície de backlog separada de `todos/active/`.
- [ ] `DOD-03` Decisões duráveis possuem registro e status navegáveis, sem substituir módulos, constituição ou TODOs.
- [ ] `DOD-04` O roadmap informa horizonte relativo, estado, dependências, resultado e critério de saída sem prometer datas não aprovadas.
- [ ] `DOD-05` Cada módulo atual expõe a estrutura mínima definida e preserva suas invariantes existentes.
- [ ] `DOD-06` Contratos possuem catálogo e estado explícito sem afirmações não verificadas.
- [ ] `DOD-07` ST-02, ST-03 e ST-04 ficam rastreáveis como candidatos, mas sem autoridade de execução.
- [ ] `DOD-08` README, constituição, artifacts e TODO governance concordam sobre a mesma navegação e autoridade.
- [ ] `DOD-09` Nenhum arquivo de produto, referência ou mudança preexistente fora do escopo foi alterado pelo ST-01.

## Validation Steps

- [ ] `VAL-01` Resolver todos os links relativos adicionados ou alterados.
- [ ] `VAL-02` Verificar ausência de placeholders, estados inválidos e referências conflitantes a backlog/TODO.
- [ ] `VAL-03` Simular a jornada ST-03 da descoberta ao backlog e confirmar que ela não aparece como execução aprovada.
- [ ] `VAL-04` Comparar 1-1 as invariantes atuais de cada módulo com a versão entregue.
- [ ] `VAL-05` Executar `bash delphi-ai/tools/verify_context.sh`.
- [ ] `VAL-06` Executar guards de autoridade, expectativa de diff, conclusão e closeout aplicáveis.
- [ ] `VAL-07` Executar `git diff --check` no patch pertencente ao ST-01 e comprovar preservação dos hashes preexistentes.
- [ ] `VAL-08` Concluir revisão independente no-context de planejamento e revisão final, conforme o piso determinístico.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01` | Definition of Done | lifecycle canônico | doc | `evolution_lifecycle.md` | n/a | planned | inspeção estrutural |
| `DOD-02` | Definition of Done | backlog separado | doc | `backlog/README.md` | n/a | planned | intake e autoridade |
| `DOD-03` | Definition of Done | decisões navegáveis | doc | `decisions/README.md` | n/a | planned | estados e índice |
| `DOD-04` | Definition of Done | roadmap previsível | doc | `system_roadmap.md` | n/a | planned | campos obrigatórios |
| `DOD-05` | Definition of Done | módulos alinhados | doc | `modules/*.md` | n/a | planned | comparação 1-1 |
| `DOD-06` | Definition of Done | catálogo de contratos | doc | `contracts/README.md` | n/a | planned | sem claims não verificadas |
| `DOD-07` | Definition of Done | próximos estudos sem execução | doc | `backlog/*.md` | n/a | planned | cenário ST-03 |
| `DOD-08` | Definition of Done | autoridades coerentes | review | navegação cruzada | n/a | planned | sem conflito |
| `DOD-09` | Definition of Done | escopo preservado | diff | path diff + hashes | local | planned | arquivos alheios intactos |
| `VAL-01` | Validation Steps | links relativos | test | resolved-link scan | local | planned | docs only |
| `VAL-02` | Validation Steps | estados e placeholders | test | `rg` checks | local | planned | docs only |
| `VAL-03` | Validation Steps | jornada ST-03 | manual | traceability walkthrough | n/a | planned | sem active TODO |
| `VAL-04` | Validation Steps | invariantes preservadas | review | module consistency table | n/a | planned | 1-1 |
| `VAL-05` | Validation Steps | contexto Delphi | test | `bash delphi-ai/tools/verify_context.sh` | local | planned | readiness |
| `VAL-06` | Validation Steps | guards | test | guard outputs | local | planned | deterministic |
| `VAL-07` | Validation Steps | patch e preexistentes | test | `git diff --check` + SHA-256 | local | planned | scoped |
| `VAL-08` | Validation Steps | revisões independentes | review | reviewer evidence | n/a | planned | fresh no-context |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| GitHub origin | baseline e publicação da autoridade `main` | healthy | 2026-09-18 | `git.exe fetch origin --prune` via Windows credential manager | usar Windows Git para push se WSL Git permanecer sem helper |

## Profile Scope & Handoffs

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality` para revisão independente; nenhum implementador de produto.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | assurance-tester-quality | crítica e revisão final independentes | TODO + diff documental limitado | planned |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** `one checkpoint`
- **Why this level:** não muda runtime, mas estabelece governança transversal para roadmap, módulos, contratos, decisões, artifacts, backlog e TODOs.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/README.md`
- **Secondary module docs:** os quatro documentos atuais em `foundation_documentation/modules/`.
- **Planned decision promotion targets:** `evolution_lifecycle.md`, `system_roadmap.md`, `project_constitution.md`, `modules/README.md`, `contracts/README.md`.
- **Module decision consolidation targets:** seção de lifecycle e rastreabilidade em `modules/README.md`; seções de maturidade/dependências em cada módulo.

## Decision Pending

- [x] Nenhuma decisão material permanece aberta para formar o baseline proposto; as escolhas abaixo aguardam aprovação do usuário pelo gate `APROVADO`.

## Decisions

- [x] `D-01` Usar horizontes relativos `Current`, `Next`, `Later` e `Explore`; datas/releases só entram mediante aprovação explícita. Ref: `No Prior Decision`.
- [x] `D-02` Criar `foundation_documentation/backlog/` como autoridade de candidatos não aprovados; `todos/active/` continua exclusivo para execução aprovada. Ref: constituição `TODO governance`.
- [x] `D-03` Manter `artifacts/feature-briefs/` como descoberta não autoritativa; um brief nunca substitui backlog, decisão, roadmap ou TODO. Ref: feature brief ST-01.
- [x] `D-04` Usar estados de candidato `Proposed|Under-Review|Accepted|Deferred|Rejected` e estados de capacidade `Discovery|Planned|In-Progress|Blocked|Delivered|Retired`.
- [x] `D-05` Registrar decisões duráveis em `decisions/` com estado `Proposed|Accepted|Superseded|Rejected`, mantendo constituição e módulos como verdade consolidada.
- [x] `D-06` Exigir que roadmap e módulos exponham ownership, estado, dependências, resultado e próximo gate, sem transformar planejamento em autorização.
- [x] `D-07` Não retroajustar artifacts/TODOs concluídos; a nova estrutura governa superfícies atuais e futuras.
- [x] `D-08` Registrar ST-02, ST-03 e ST-04 como candidatos independentes; não criar seus TODOs ativos neste escopo.
- [x] `D-09` Não criar validator permanente neste TODO; usar os guards existentes e validações determinísticas ad hoc, deixando automação adicional para necessidade comprovada.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `modules/README#ownership` | módulos possuem workflows, contratos, APIs e data shapes locais | Preserve | `modules/README.md` |
| `identity-and-tenancy#invariants` | tenant por request, permissão na BU, roles atuais | Preserve | `modules/identity-and-tenancy.md` |
| `inbox-and-conversations#invariants` | conversa por BU/contato, idempotência, capacidade do canal | Preserve | `modules/inbox-and-conversations.md` |
| `audit-and-history#invariants` | histórico persistente, tenant/BU scoped, leitura separada de escrita | Preserve | `modules/audit-and-history.md` |
| `integrations-and-channels#invariants` | providers são adapters, segredos não vazam, erros determinísticos | Preserve | `modules/integrations-and-channels.md` |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01` a `D-09` formam o baseline proposto; qualquer alteração material exige reconvergência e `APROVADO` renovado.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** o TODO estabelece a arquitetura de informação e o lifecycle que governarão todas as evoluções futuras.
- **Deviation / debt being retired:** roadmap sem estado/dependências, backlog citado mas ausente, módulos mínimos sem maturidade/rastreabilidade e ausência de registro de decisões.
- **Target steady-state after closeout:** uma ideia pode ser rastreada desde descoberta até entrega, com autoridade e promoção inequívocas em cada transição.
- **Temporary exceptions allowed:** documentos históricos não serão retroajustados.
- **Cutover / removal condition:** superfícies operacionais atuais apontam para o novo lifecycle; referências conflitantes foram removidas ou classificadas como históricas.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| autoridade por estágio | `D-02`, `D-03`, `D-05` | Foundation | evita ideia virar execução silenciosamente |
| roadmap orientado a resultado | `D-01`, `D-06` | roadmap/modules | torna dependências e saída verificáveis |
| TODO como única autoridade de execução | constituição + `D-02` | todos | preserva aprovação e evidência |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| ideia não aprovada em `todos/active/` | TODO sem aprovação/origem | mistura descoberta com execução | none |
| roadmap como lista de desejos sem estado/saída | item sem campos mínimos | reduz previsibilidade | documentos históricos apenas |
| decisão durável somente em chat/TODO | módulo/constituição sem consolidação | perde continuidade | none |
| inventário de contrato baseado em inferência | contrato sem evidência | cria autoridade falsa | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| rule | execução | `project_constitution.md` + `todos/README.md` | candidato tratado como TODO aprovado | implement-in-this-todo | revisão 1-1 |
| guard | TODO | `todo_authority_guard.py`, `todo_completion_guard.py` | execução/closeout sem autoridade/evidência | already-enforced | outputs no TODO |
| audit | Foundation | resolved-link, status-vocabulary e traceability walkthrough | links, estados e transições inconsistentes | manual-only-with-rationale | comandos reproduzíveis; árvore pequena e sem parser canônico atual |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** aguarda o Review Baseline Freeze.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** o TODO é `medium`, transversal e estabelece arquitetura documental.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `foundation_documentation/main`
- **Baseline commit:** `565ff17a81a6faa663f9e024e9784e396cd50bfe`
- **Baseline push reference:** `origin/main@565ff17a81a6faa663f9e024e9784e396cd50bfe`
- **Gate status:** `no_material_findings`
- **Findings summary:** feature brief e TODO foram commitados e publicados na autoridade `foundation_documentation/main`; nenhum arquivo preexistente não pertencente ao pacote foi incluído.
- **Evidence / reference:** commit `565ff17a81a6faa663f9e024e9784e396cd50bfe`; push `d8626df1..565ff17a main -> main`.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** o diff final deve permanecer no ST-01 documental.
- **Trigger stage:** `after planning review converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Gate status:** `not_run`
- **Findings summary:** aguardando baseline.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] `AMB-03`: adotar horizontes relativos, sem datas implícitas (`D-01`).
- [x] `AMB-04`: adotar `foundation_documentation/backlog/` fora de `todos/active/` (`D-02`).

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | A Foundation, não o código, é a autoridade de produto/governança. | `README.md`, constituição | o escopo teria owner errado | High | Keep as Assumption |
| `A-02` | As quatro fases atuais continuam válidas como intenção estratégica. | `system_roadmap.md`, feature brief não pede substituição | exigiria nova decisão de produto | High | Keep as Assumption |
| `A-03` | Os quatro módulos atuais permanecem os owners canônicos nesta story. | `modules/README.md`, ST-01 não muda domínio | exigiria decomposição de módulo separada | High | Keep as Assumption |
| `A-04` | Não há necessidade de datas para obter previsibilidade nesta etapa. | pedido enfatiza evolução ao longo do tempo, sem compromisso de release | roadmap teria de adotar calendário aprovado | Medium | Promote to Decision (`D-01`) |

## Execution Plan

### Touched Surfaces

- Authority/navigation: `README.md`, `project_constitution.md`, `evolution_lifecycle.md`.
- Planning: `system_roadmap.md`, `backlog/`, `decisions/`.
- Local contracts: `modules/`, `contracts/README.md`.
- Evidence/execution: `artifacts/README.md`, feature brief, `todos/README.md`, este TODO.

### Ordered Steps

1. Corrigir com autorização a âncora Git da Foundation, preservando ref e working tree.
2. Congelar e publicar o baseline deste TODO.
3. Executar review de arquitetura e crítica independente; integrar findings.
4. Rodar coherence/scope-drift/pre-approval guards e solicitar `APROVADO`.
5. Implementar lifecycle, backlog, decisions e navegação central.
6. Evoluir roadmap, módulos e catálogo de contratos sem inventar estado de produto.
7. Registrar ST-02/ST-04 como backlog e validar a jornada ST-03.
8. Executar validações, decisão/adherence, revisão final e closeout.

### Test Strategy

- **Strategy:** `test-after`
- **Why:** mudança exclusivamente documental; os testes são navegação, vocabulário, autoridade, diff e guards.
- **Fail-first targets:** `n/a`; o diagnóstico está documentado no feature brief e neste TODO.

### Flow Evidence Planning Matrix

| Flow | Entry | Expected Transition | Evidence |
| --- | --- | --- | --- |
| ST-03 | feature brief/discovery | backlog candidate, sem active TODO | links e estados canônicos |
| candidato aprovado futuramente | backlog | roadmap/TODO somente mediante aprovação | lifecycle walkthrough |
| entrega concluída | active TODO | completed + evidência + consolidação | lifecycle walkthrough |

### Local CI-Equivalent Suite Matrix

| Surface | Command / Check | Status | Evidence |
| --- | --- | --- | --- |
| Context | `bash delphi-ai/tools/verify_context.sh` | planned | terminal output |
| Markdown patch | scoped `git diff --check` | planned | terminal output |
| Relative links | filesystem-resolved link scan | planned | terminal output |
| TODO authority | authority/completion/diff/closeout guards | planned | guard outputs |
| Foundation integrity | state vocabulary + traceability walkthrough | planned | command/manual record |

### Runtime / Rollout Notes

- Nenhum runtime, deploy, migration ou browser flow é afetado.
- A publicação é a atualização governada de `foundation_documentation/main`.

## Plan Review Gate

- **Status:** `prepared-pre-freeze`; nenhuma linha abaixo conta como revisão aprovada antes do baseline commit/push.

### Review Sections

| Lens | Preliminary Position |
| --- | --- |
| Architecture | separação entre discovery, backlog, roadmap, decision e TODO reduz ambiguidade de autoridade |
| Code Quality | n/a; nenhum código de produto ou validator novo |
| Tests | comandos reproduzíveis e walkthrough de traceabilidade são proporcionais ao escopo documental |
| Performance | sem impacto de runtime |
| Security | reduz risco de claims/segredos legados virarem autoridade; não toca trust boundaries |
| Elegance | uma fonte de lifecycle e índices leves evitam taxonomia duplicada |
| Structural Soundness | módulos/constituição consolidam decisões; artifacts continuam evidência, não autoridade |

### Issue Cards

#### PR-01 — Horizonte do roadmap

- **Severity:** medium
- **Evidence:** `system_roadmap.md` possui fases sem estado, dependência ou saída.
- **Why now:** os próximos estudos precisam de um local previsível sem falsa promessa de data.
- **A:** quarters/releases; maior previsibilidade temporal, maior risco de compromisso fictício.
- **B:** `Current/Next/Later/Explore`; menor precisão calendárica, maior durabilidade.
- **C:** manter fases atuais; esforço zero, problema permanece.
- **Recommendation:** B (`D-01`); melhor equilíbrio entre clareza, manutenção, elegância e risco.

#### PR-02 — Local do backlog

- **Severity:** medium
- **Evidence:** constituição cita `backlog/`, `todos/README.md` cita `todos/active/backlog/`, e nenhum existe.
- **A:** `todos/active/backlog`; simples, mas mistura não aprovado com execução ativa.
- **B:** `foundation_documentation/backlog/`; autoridade separada e transição explícita.
- **C:** somente feature briefs; falta disposição canônica e priorização.
- **Recommendation:** B (`D-02`); menor acoplamento e melhor coerência estrutural.

#### PR-03 — Automação de proteção

- **Severity:** low
- **Evidence:** não existe validator canônico de IA documental na Foundation.
- **A:** criar validator permanente agora; maior cobertura, amplia escopo e manutenção.
- **B:** usar guards existentes + checks reproduzíveis e observar recorrência.
- **C:** apenas revisão manual; menor esforço, menor previsibilidade.
- **Recommendation:** B (`D-09`); evita automação prematura sem deixar validação implícita.

### Failure Modes & Edge Cases

- Duplicar estado divergente entre roadmap, backlog e TODO.
- Transformar `Accepted` no backlog em autorização de execução.
- Inventar maturidade de módulo ou contrato sem evidência.
- Reclassificar documentos históricos retroativamente.
- Usar horizonte relativo como substituto de prioridade ou dependência.
- Absorver alterações preexistentes no diff do ST-01.

### Residual Unknowns / Risks

- **Assumptions:** fases e módulos atuais permanecem válidos; datas não são requeridas.
- **Unknowns:** baseline histórico exato da transposição pertence ao ST-02, não a este TODO.
- **Confidence:** high para lifecycle; medium para a granularidade final dos campos até crítica independente.

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** governança transversal exige crítica externa sobre complexidade acidental e autoridade duplicada.
- **Opinion count:** `1`
- **Package mode:** `bounded-file-set`
- **Internal reviewer mandate:** `required; fresh no-context reviewer after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Latest TEACH evidence / artifact:** `pending Review Baseline Freeze`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | transversal, docs only |
| `blast_radius` | `cross-module` | todos os módulos usam o lifecycle |
| `behavioral_change_or_bugfix` | `no` | sem comportamento de produto |
| `changes_public_contract` | `no` | estrutura de catálogo, sem contrato de API novo |
| `touches_auth_or_tenant` | `no` | invariantes apenas preservadas |
| `touches_runtime_or_infra` | `no` | docs only |
| `touches_tests` | `no` | sem test logic |
| `critical_user_journey` | `no` | governança interna |
| `release_or_promotion_critical` | `no` | sem release de produto |
| `high_severity_plan_review_issue` | `no` | maior severidade medium |
| `explicit_three_lane_request` | `no` | não solicitado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** complexidade medium com blast radius cross-module.
- **Impact signals in scope:** `cross-module blast radius`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** feature brief, TODO congelado e documentos canônicos tocados.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after freeze; reviewer cannot implement`
- **Canonical multi-lane audit protocol:** `n/a`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** aguardando baseline.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** as premissas referem-se a documentos canônicos existentes; o guard deve confirmar os anchors citados.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03,A-04`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Gate status:** `not_run`
- **Findings summary:** aguardando baseline e crítica.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending explicit APROVADO after preflight-go`
- **Approval scope:** `pending`
- **Execution not authorized by approval:** código/produto/referências, ST-02/ST-04 e mudanças de domínio.
- **Renewed approval required when:** qualquer decisão D-01..D-09, escopo, validator, contrato de produto ou arquivo esperado mudar materialmente.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/main_instructions.md` | autoridade e Foundation main-only | documentação antes de código | branch/worktree paralelo | freeze/push canônico |
| `rule-docker-shared-core-instructions-always-on` | disciplina geral | hierarquia e segurança | atalhos de workflow | gates obrigatórios |
| `rule-docker-shared-project-mandate-always-on` | mandato e core docs | propósito/invariantes | drift de produto | revisão 1-1 |
| `rule-docker-shared-foundation-docs-sync-model-decision` | sincronização Foundation | roadmap/módulos coerentes | side notes concorrentes | consolidação canônica |
| `wf-docker-todo-driven-execution-method` | entrega governada | TODO, aprovação, evidência | implementação pré-APROVADO | execução por fases |
| `wf-docker-todo-*` phase methods | lifecycle do TODO | freeze, review, guards, closeout | pular gates | sequência registrada |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `todo-approval`
- **Selected role:** `primary-chat`
- **Selected model:** `current session model`
- **Selected effort:** `max-or-closest-equivalent`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `required by independent no-context critique skill after freeze`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `review-required`
- **Waiver / exception reference:** `routing guard pending after planning reviews`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** contrato em review pré-aprovação; nenhuma implementação canônica iniciada.
- **Post-commit/push status:** `pending`
- **Next path/status action:** commit/push do baseline, reviews de planejamento e preflight de autoridade.

## Security Risk Assessment

- **Risk level:** `low`
- **Why this risk level:** docs only; principal risk is publishing secret/reference data or weakening tenant invariants, both explicitly forbidden.
- **Attack surface in scope:** documentation authority only.
- **Attack simulation decision:** `not_needed`
- **Review evidence:** scoped secret-pattern scan and independent final review planned.
- **Residual security risk:** inaccurate documentation claims; mitigated by evidence requirements.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `none`
- **Why this level:** no endpoint, UI, backend mutation, queue or runtime change.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | endpoint-performance-scrutiny | `not_needed` | low | `EPS-DATA-PATH-CHANGED` | before_local_implemented | `EPS-E1` | `not_applicable` | none | none |
| `FRC` | frontend-race-condition-validation | `not_needed` | low | `FRC-LIFECYCLE-ASYNC-EFFECT` | before_local_implemented | `FRC-POLICY` | `not_applicable` | none | none |
| `BCI` | backend-concurrency-idempotency-validation | `not_needed` | low | `BCI-NON-IDEMPOTENT-WRITE` | before_local_implemented | `BCI-INV` | `not_applicable` | none | none |
| `RLS` | runtime-load-stress-validation | `not_needed` | low | `RLS-SLO-CLAIM` | before_production_ready | `RLS-E1` | `not_applicable` | none | none |

## Verification Debt Assessment

- **Audit outcome:** `pending`
- **Why this outcome:** obrigatório para medium antes de Completed.
- **Inline code TODO debt:** `none`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none`

## Independent Test Quality Audit Gate

- **Audit decision:** `not_needed`
- **Why this decision:** nenhum teste, comportamento, contrato público ou código muda.
- **Trigger signals in scope:** `none`
- **Required evidence matrix:** `n/a`
- **Audit status:** `not_run`
- **Findings summary:** `n/a`
- **Evidence / reference:** audit trigger matrix após freeze.

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** medium com blast radius documental cross-module e arquitetura de governança.
- **Impact signals in scope:** `cross-module blast radius`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** baseline, escopo, diff documental, adherence, validações e riscos residuais.
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Canonical multi-lane audit protocol:** `n/a`
- **Review focus:** `adherence|regressions|validation evidence|elegance|structural soundness|verification debt`
- **Final review status:** `not_run`
- **Findings summary:** `pending implementation`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `recommended`
- **Why this decision:** há cutover documental de lifecycle, mas documentos históricos permanecem por exceção explícita.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement`
- **Package mode:** `bounded-file-set`
- **Cutover audit status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`

## Module Consolidation Gate

- [ ] Decisões estáveis foram consolidadas nas superfícies canônicas.
- [ ] Módulos preservam suas decisões anteriores e apontam ao lifecycle.
- [ ] Feature brief e TODO apontam para as superfícies finais.
- [ ] Referências conflitantes de backlog/autoridade foram eliminadas das superfícies atuais.

## Commands (Run Locally)

- `bash delphi-ai/tools/verify_context.sh`
- `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md --pre-approval`
