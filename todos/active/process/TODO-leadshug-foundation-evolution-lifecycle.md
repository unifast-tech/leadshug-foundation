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
- **Next exact step:** obter validação do usuário para o escopo revisado após os findings independentes de arquitetura e planejamento.

## Active Work State

- **Work state:** `review`
- **Why this state now:** os primeiros reviews independentes encontraram ambiguidades materiais; o contrato foi reconduzido ao loop de planejamento.
- **Exit condition:** usuário valida o escopo revisado, novo baseline é publicado, reviews reconvergem e os guards pré-aprovação passam.

## Scope

- [ ] Criar `evolution_lifecycle.md` como contrato canônico do fluxo descoberta → candidato → planejamento → aprovação → entrega → encerramento.
- [ ] Criar `backlog/README.md` como autoridade de trabalho candidato ainda não aprovado e registrar ST-02, ST-03 e ST-04 como itens independentes.
- [ ] Criar `decisions/README.md` como índice de proveniência/racional de decisões duráveis e definir quando uma decisão aceita se torna efetiva nas superfícies canônicas.
- [ ] Evoluir `system_roadmap.md` para horizontes relativos, estado, dependências, resultado esperado e critério de saída, preservando as quatro fases estratégicas.
- [ ] Evoluir `modules/README.md` para declarar a autoridade dos módulos e o schema futuro, preservando integralmente os quatro documentos de módulo atuais neste recorte.
- [ ] Evoluir `contracts/README.md` como índice e regra de verificação, sem transformá-lo em uma segunda autoridade do estado dos contratos nem inventar contratos não verificados.
- [ ] Alinhar `README.md`, `project_constitution.md`, `todos/README.md` e `artifacts/README.md` ao novo lifecycle.
- [ ] Atualizar o feature brief com a disposição do ST-01 e links canônicos, preservando ST-02, ST-03 e ST-04 como stories independentes do programa.
- [ ] Definir uma matriz de autoridade por campo, papéis neutros de fornecedor e máquinas de estado/transições separadas para candidatos, capacidades, TODOs, decisões e verificação de contratos.
- [ ] Validar cenários positivo e negativo: ST-03 nasce em descoberta, entra no backlog e permanece sem autoridade de execução; mover um TODO para `active/` sem `APROVADO` não autoriza implementação.

## Delivery Status Semantics

- `Pending`: nenhum marco material de entrega foi atingido.
- `Local-Implemented`: documentos canônicos foram alterados e validados localmente.
- `Lane-Promoted`: `foundation_documentation/main` contém a entrega publicada.
- `Production-Ready`: equivalente a `Lane-Promoted` para esta entrega estritamente documental, após todos os gates.
- `Blocked` não é estágio: é um qualifier ortogonal que preserva o estágio anterior e exige razão, owner e condição de desbloqueio.

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
| Foundation evolution lifecycle | `foundation_documentation:main@pending` | `n/a — main-only authority` | `n/a` | `direct governed Foundation write; pending` | `pending` |

## Out of Scope

- [ ] Alterar código, testes, schema, runtime ou configuração do LeadsHug.
- [ ] Executar os estudos ST-02, ST-03 ou a síntese ST-04.
- [ ] Canonizar conceitos de canal, fila, equipe, setor, SLA, automação ou IA.
- [ ] Inventariar todos os endpoints ou afirmar cobertura contratual sem evidência.
- [ ] Reescrever artifacts, TODOs concluídos ou decisões históricas retroativamente.
- [ ] Limpar, normalizar ou incluir mudanças preexistentes não pertencentes a este TODO.
- [ ] Criar worktree, branch auxiliar, checkout alternativo ou cópia gravável da Foundation.
- [ ] Migrar individualmente os quatro módulos atuais para um novo schema ou declarar maturidade/capacidades não verificadas.

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `.` | `d8626df1fb0ff64751d7fae10ae93cf41ab1a458` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `evolution_lifecycle.md` | `A` | contrato canônico do lifecycle |
| Foundation | `backlog/**` | `A` | intake pré-TODO e candidatos ST-02/ST-03/ST-04 |
| Foundation | `decisions/**` | `A` | registro de decisões duráveis |
| Foundation | `README.md` | `M` | navegação e autoridade |
| Foundation | `project_constitution.md` | `M` | invariantes do lifecycle |
| Foundation | `system_roadmap.md` | `M` | previsibilidade e horizontes |
| Foundation | `modules/README.md` | `M` | autoridade por campo e schema futuro; módulos atuais permanecem intactos |
| Foundation | `contracts/README.md` | `M` | índice e estados de verificação, sem autoridade duplicada |
| Foundation | `artifacts/README.md` | `M` | distinção entre descoberta e evidência |
| Foundation | `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` | `A, M` | framing e disposição do ST-01 |
| Foundation | `todos/README.md` | `M` | corrigir lifecycle e backlog |
| Foundation | `todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md` | `A, M, D` | contrato, evidência e remoção no closeout |
| Foundation | `todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md` | `A, M` | destino esperado do closeout |
| Foundation | `.gitattributes` | `M` | mudança preexistente; aceita pelo guard, mas deve preservar o hash registrado |
| Foundation | `.gitignore` | `M` | mudança preexistente; aceita pelo guard, mas deve preservar o hash registrado |
| Foundation | `artifacts/migration/claude-legacy-reconciliation-review.prompt.txt` | `M` | mudança preexistente; aceita pelo guard, mas deve preservar o hash registrado |
| Foundation | `artifacts/publication-manifest.txt` | `M` | mudança preexistente; aceita pelo guard, mas deve preservar o hash registrado |
| Foundation | `deterministic/.gitkeep` | `M` | mudança preexistente; aceita pelo guard, mas deve preservar o hash registrado |
| Foundation | `todos/ephemeral/**` | `A, ??` | conteúdo preexistente não rastreado; deve preservar os hashes registrados |
| Foundation | `todos/promotion_lane/**` | `A, ??` | conteúdo preexistente não rastreado; deve preservar os hashes registrados |

### Pre-existing Paths To Preserve Byte-for-Byte Unless Separately Authorized

| Path | SHA-256 at ST-01 baseline | Treatment |
| --- | --- | --- |
| `.gitattributes` | `c189c1da423aa9a0f39bce54eddfeddd8a48d18f2ad242ff3587333b75ace1e5` | do not edit |
| `.gitignore` | `1c286328c8951177f22f7784da0458c509aa4b41257a5089189b73da039a58ad` | do not edit |
| `artifacts/migration/claude-legacy-reconciliation-review.prompt.txt` | `2e1bae65ad5e2edd16c0e24c1a01b780af9bdec608bc32326089f97cafd79167` | do not edit |
| `artifacts/publication-manifest.txt` | `5579dd6ac5099f8ef87836464e6dde0d7f1a153e6cee9a5128f7a73516dbe348` | do not edit |
| `deterministic/.gitkeep` | `7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6` | do not edit |
| `todos/ephemeral/.gitignore` | `eef48e8788e8d8c98b1132c9ef3294ae77f759af05b662bccd0f5b27966040dd` | do not edit |
| `todos/ephemeral/.gitkeep` | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | do not edit |
| `todos/promotion_lane/.gitkeep` | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | do not edit |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `project_mandate.md` | `any` | mandato não muda neste recorte |
| Foundation | `domain_entities.md` | `any` | vocabulário de produto não muda |
| Foundation | `technology_baseline.md` | `any` | stack/runtime não muda |
| Foundation | `modules/identity-and-tenancy.md` | `any` | migração detalhada dos módulos foi retirada do recorte |
| Foundation | `modules/inbox-and-conversations.md` | `any` | migração detalhada dos módulos foi retirada do recorte |
| Foundation | `modules/audit-and-history.md` | `any` | migração detalhada dos módulos foi retirada do recorte |
| Foundation | `modules/integrations-and-channels.md` | `any` | migração detalhada dos módulos foi retirada do recorte |
| Foundation | `policies/**` | `any` | políticas de produto não mudam |
| Foundation | `artifacts/analysis/**` | `any` | análises históricas permanecem intactas |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** refinements de títulos, links, campos e exemplos necessários para tornar o mesmo lifecycle coerente e navegável.
- **Must update or split the TODO:** novo comportamento de produto, mudança de domínio, validator executável novo, inventário completo de APIs, estudo comparativo ou decisão de canal/atendimento.

## Definition of Done

- [ ] `DOD-01` `evolution_lifecycle.md` define schemas e transições sem duplicar valores vivos pertencentes a backlog, roadmap, módulos, decisões ou TODOs.
- [ ] `DOD-02` Ideias não aprovadas possuem uma superfície de backlog separada de `todos/active/`.
- [ ] `DOD-03` `todos/active/` contém contratos táticos vivos, mas somente `APROVADO` explícito e o guard de autoridade concedem execução.
- [ ] `DOD-04` Cada campo vivo possui um único owner canônico e as demais superfícies usam IDs/links, conforme matriz de autoridade.
- [ ] `DOD-05` Candidatos, capacidades, TODOs, decisões e contratos possuem máquinas de estado ortogonais, transições, atores, evidências e caminhos de cancelamento/reabertura.
- [ ] `DOD-06` O roadmap informa tema/fase, horizonte `Now|Next|Later|Unscheduled`, estado, dependências, resultado e critério de saída sem prometer datas.
- [ ] `DOD-07` Módulos atuais permanecem intactos e `modules/README.md` declara somente sua autoridade e schema futuro.
- [ ] `DOD-08` Decisões preservam racional/proveniência e só se tornam efetivas após consolidação nos alvos canônicos nomeados.
- [ ] `DOD-09` Contratos usam estado de verificação explícito sem afirmações não verificadas e `contracts/README.md` permanece apenas índice/regra.
- [ ] `DOD-10` ST-02 e ST-03 ficam `Selected-for-Planning` após o ST-01; ST-04 fica `Deferred` até ST-02/ST-03, todos sem autoridade de execução.
- [ ] `DOD-11` README, constituição, artifacts e TODO governance concordam sobre papéis neutros, navegação e autoridade.
- [ ] `DOD-12` A necessidade de validator permanente tem owner e gatilho mensurável, enquanto os checks atuais são exatos e reproduzíveis.
- [ ] `DOD-13` Nenhum arquivo de produto, referência ou mudança preexistente fora do escopo foi alterado pelo ST-01.

## Validation Steps

- [ ] `VAL-01` Resolver todos os links relativos Markdown adicionados ou alterados e exigir zero destinos ausentes.
- [ ] `VAL-02` Verificar IDs, campos obrigatórios e valores de enum em todos os registros criados neste TODO.
- [ ] `VAL-03` Simular ST-03 da descoberta ao backlog e confirmar que `Selected-for-Planning` não concede `APROVADO`.
- [ ] `VAL-04` Criar temporariamente um cenário negativo de TODO em `active/` sem aprovação e confirmar que o contrato o mantém sem autoridade de execução.
- [ ] `VAL-05` Comparar 1-1 as decisões e o conteúdo atual dos quatro módulos, comprovando que permaneceram inalterados.
- [ ] `VAL-06` Executar `bash delphi-ai/tools/verify_context.sh`.
- [ ] `VAL-07` Executar os comandos exatos de autoridade, expectativa de diff, conclusão e closeout listados neste TODO e exigir `Overall outcome: go` no gate correspondente.
- [ ] `VAL-08` Executar `git diff --check d8626df1fb0ff64751d7fae10ae93cf41ab1a458 --` e exigir saída vazia para o patch pertencente ao ST-01.
- [ ] `VAL-09` Recalcular os oito hashes preexistentes registrados e exigir igualdade byte a byte.
- [ ] `VAL-10` Executar scan de padrões de segredo somente nos arquivos adicionados/modificados pelo ST-01 e exigir zero ocorrências não explicadas.
- [ ] `VAL-11` Concluir crítica pré-aprovação, revisão final e auditorias derivadas pelo piso determinístico.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01` | Definition of Done | lifecycle sem valores duplicados | doc | `evolution_lifecycle.md#authority-matrix` | n/a | planned | schema/transições somente |
| `DOD-02` | Definition of Done | backlog separado | doc | `backlog/README.md` | n/a | planned | nunca autoriza execução |
| `DOD-03` | Definition of Done | active não implica aprovado | doc+guard | `evolution_lifecycle.md#tactical-todos`; authority guard | local | planned | aprovação explícita |
| `DOD-04` | Definition of Done | owner único por campo | doc | authority matrix | n/a | planned | referências fora do owner |
| `DOD-05` | Definition of Done | máquinas de estado completas | doc | transition tables in `evolution_lifecycle.md` | n/a | planned | inclui reopen/cancel/supersede |
| `DOD-06` | Definition of Done | roadmap previsível | doc | `system_roadmap.md` | n/a | planned | fase e horizonte ortogonais |
| `DOD-07` | Definition of Done | módulos preservados | diff | `git diff d8626df1 -- modules/` | local | planned | somente README muda |
| `DOD-08` | Definition of Done | decisões como proveniência | doc | `decisions/README.md` | n/a | planned | eficácia após consolidação |
| `DOD-09` | Definition of Done | verificação de contratos | doc | `contracts/README.md` | n/a | planned | índice, não autoridade duplicada |
| `DOD-10` | Definition of Done | disposições ST-02/ST-03/ST-04 | doc | `backlog/*.md` + feature brief | n/a | planned | IDs/estados coerentes |
| `DOD-11` | Definition of Done | navegação e papéis coerentes | review | README/constitution/TODO/artifacts cross-check | n/a | planned | provider-neutral roles |
| `DOD-12` | Definition of Done | gatilho de validator | doc | `evolution_lifecycle.md#deterministic-adoption-trigger` | n/a | planned | owner + limiar mensurável |
| `DOD-13` | Definition of Done | escopo preservado | diff | diff guard + SHA-256 comparison | local | planned | arquivos alheios intactos |
| `VAL-01` | Validation Steps | links relativos | test | Markdown target resolver over changed `.md` files; expected missing count `0` | local | planned | comando registrado no execution log |
| `VAL-02` | Validation Steps | IDs/campos/enums | test | exact `rg`/field matrix checks; expected invalid count `0` | local | planned | sem parser permanente nesta story |
| `VAL-03` | Validation Steps | cenário positivo ST-03 | review | lifecycle trace table | n/a | planned | sem execução implícita |
| `VAL-04` | Validation Steps | cenário negativo active sem approval | review+guard | temporary fixture under `artifacts/tmp/`; expected authority `no-go` | local | planned | fixture descartável |
| `VAL-05` | Validation Steps | módulos preservados | review | Module Decision Consistency Validation | n/a | planned | conteúdo 1-1 |
| `VAL-06` | Validation Steps | contexto Delphi | test | `bash delphi-ai/tools/verify_context.sh` | local | planned | expected PACED-Ready |
| `VAL-07` | Validation Steps | guards | test | commands in `Commands`; expected gate-specific `go` | local | planned | deterministic |
| `VAL-08` | Validation Steps | whitespace patch | test | `git diff --check d8626df1fb0ff64751d7fae10ae93cf41ab1a458 --` | local | planned | expected empty |
| `VAL-09` | Validation Steps | hashes preexistentes | test | `sha256sum` against recorded values | local | planned | eight exact matches |
| `VAL-10` | Validation Steps | secret patterns | security | scoped `rg` over ST-01 paths | local | planned | zero unexplained matches |
| `VAL-11` | Validation Steps | independent gates | review | critique/final-review/audit evidence | n/a | planned | fresh no-context |

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
- **Secondary module docs:** os quatro documentos atuais em `foundation_documentation/modules/` são anchors de preservação, não alvos de edição.
- **Planned decision promotion targets:** `evolution_lifecycle.md`, `system_roadmap.md`, `project_constitution.md`, `modules/README.md`, `contracts/README.md`.
- **Module decision consolidation targets:** seção de autoridade e schema futuro em `modules/README.md`; nenhum módulo individual é migrado neste TODO.

## Decision Pending

- [ ] O usuário deve validar o escopo reduzido e as decisões D-01..D-11 integradas após os findings independentes antes do novo baseline/review.

## Proposed Decisions (Pending User Validation)

- [ ] `D-01` Preservar as quatro fases atuais como temas estratégicos e usar horizonte ortogonal `Now|Next|Later|Unscheduled`; horizonte não representa prazo, e datas/releases exigem aprovação explícita. Ref: `system_roadmap.md`.
- [ ] `D-02` Criar `foundation_documentation/backlog/` para candidatos não aprovados. `todos/active/` contém contratos táticos vivos em `Draft|Review|Approved|In-Progress`; estar na pasta nunca concede execução, que exige `APROVADO` explícito e authority guard `go`. Ref: constituição `TODO governance`.
- [ ] `D-03` Manter `artifacts/feature-briefs/` como evidência de descoberta não autoritativa e, após handoff, somente com link para o registro vivo; briefs não duplicam estado operacional. Ref: feature brief ST-01.
- [ ] `D-04` Definir máquinas ortogonais: candidato `Proposed|Under-Review|Selected-for-Planning|Deferred|Rejected`; capacidade `Not-Assessed|Discovery|Planned|In-Progress|Delivered|Retired`; TODO `Draft|Review|Approved|In-Progress|Completed|Cancelled`; decisão `Proposed|Accepted|Superseded|Rejected`; contrato `Not-Assessed|Documented|Verified|Deprecated`. `Blocked` é qualifier com razão, owner e estado anterior, nunca estado destrutivo.
- [ ] `D-05` Registrar decisões duráveis em `decisions/` como racional/proveniência. Uma decisão `Accepted` só é efetiva depois que seus alvos canônicos nomeados são consolidados; constituição/módulos mantêm a verdade corrente.
- [ ] `D-06` Adotar owner único por campo: backlog possui disposição e próximo gate; roadmap possui tema, horizonte, resultado, dependências e exit gate; módulos possuem ownership, invariantes, capacidades estáveis e contratos locais; TODO possui aprovação/execução/evidência; decisions possui racional/histórico; lifecycle possui schemas/transições; contracts README é índice; briefs são evidência.
- [ ] `D-07` Não retroajustar artifacts/TODOs concluídos nem os três TODOs ativos alheios ao ST-01. A estrutura passa a reger registros novos; um TODO legado só adota o novo schema quando receber futura alteração material autorizada. Documentos históricos mantêm marcador de contexto e ficam fora dos validadores correntes.
- [ ] `D-08` Registrar ST-02 e ST-03 como `Selected-for-Planning` com gate após ST-01; registrar ST-04 como `Deferred` até conclusão dos ST-02/ST-03. Nenhum recebe TODO ativo neste escopo.
- [ ] `D-09` Não criar validator permanente neste TODO. Strategic é owner do follow-up; abrir TODO próprio quando houver mais de dez registros vivos somados em backlog/decisions/roadmap ou na primeira recorrência comprovada de drift de schema/autoridade. Até lá, usar checks exatos e reproduzíveis deste TODO.
- [ ] `D-10` Usar IDs imutáveis baseados em namespace e slug (`BLG-<slug>`, `DEC-<slug>`, `CAP-<slug>`); títulos e filenames podem mudar, mas o ID e os links de supersessão permanecem.
- [ ] `D-11` Definir papéis provider-neutral: human decision authority, strategic steward, module owner, TODO owner/executor e assurance reviewer. Ferramentas/agentes concretos são adapters da política de engenharia, não autoridade de produto.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `modules/README#ownership` | módulos possuem workflows, contratos, APIs e data shapes locais | Preserve | `modules/README.md` |
| `identity-and-tenancy#invariants` | tenant por request, permissão na BU, roles atuais | Preserve | `modules/identity-and-tenancy.md` |
| `inbox-and-conversations#invariants` | conversa por BU/contato, idempotência, capacidade do canal | Preserve | `modules/inbox-and-conversations.md` |
| `audit-and-history#invariants` | histórico persistente, tenant/BU scoped, leitura separada de escrita | Preserve | `modules/audit-and-history.md` |
| `integrations-and-channels#invariants` | providers são adapters, segredos não vazam, erros determinísticos | Preserve | `modules/integrations-and-channels.md` |

## Decision Baseline (Frozen Before Implementation)

- [ ] `D-01` a `D-11` formam o baseline revisado pendente de validação do usuário, novo freeze e reconvergência dos reviewers.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** o TODO estabelece a arquitetura de informação e o lifecycle que governarão todas as evoluções futuras.
- **Deviation / debt being retired:** roadmap sem estado/dependências, backlog citado mas ausente, ausência de registro de decisões e ambiguidade entre TODO vivo e execução aprovada.
- **Target steady-state after closeout:** uma ideia pode ser rastreada desde descoberta até entrega, com autoridade e promoção inequívocas em cada transição.
- **Temporary exceptions allowed:** documentos históricos não serão retroajustados.
- **Cutover / removal condition:** superfícies operacionais atuais apontam para o novo lifecycle; referências conflitantes foram removidas ou classificadas como históricas.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| autoridade por campo | `D-02`, `D-03`, `D-05`, `D-06` | Foundation | evita cópias concorrentes de estado |
| roadmap orientado a resultado | `D-01`, `D-06` | roadmap | torna dependências e saída verificáveis |
| aprovação explícita | constituição + `D-02` | TODOs | separa contrato vivo de autoridade de execução |
| papéis provider-neutral | `D-11` | Foundation | evita acoplamento da autoridade a uma ferramenta |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| presença em `todos/active/` tratada como aprovação | TODO sem `APROVADO` executado | contorna o gate de autoridade | none |
| roadmap como lista de desejos sem estado/saída | item sem campos mínimos | reduz previsibilidade | documentos históricos apenas |
| decisão durável somente em chat/TODO | módulo/constituição sem consolidação | perde continuidade | none |
| inventário de contrato baseado em inferência | contrato sem evidência | cria autoridade falsa | none |
| mesmo estado vivo gravado em múltiplas superfícies | divergência entre IDs/links | cria múltiplas fontes de verdade | none |
| migração automática de TODO legado | alteração sem recorte/aprovação próprios | mistura governança nova com trabalho preexistente | somente ao tocar materialmente o TODO em trabalho futuro autorizado |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| rule | execução | `project_constitution.md` + `todos/README.md` | candidato tratado como TODO aprovado | implement-in-this-todo | revisão 1-1 |
| guard | TODO | `todo_authority_guard.py`, `todo_completion_guard.py` | execução/closeout sem autoridade/evidência | already-enforced | outputs no TODO |
| audit | Foundation | resolved-link, IDs/enums e positive/negative traceability checks | links, estados e transições inconsistentes | manual-only-with-rationale | comandos exatos neste TODO; follow-up automático pelo gatilho D-09 |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** reviewer `/root/st01_architecture_review`; findings ST01-ARCH-001..007 integrados no contrato revisado; nova rodada será exigida após validação do usuário e refreeze.
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
- **Baseline commit:** `pending user scope validation and refreeze`
- **Baseline push reference:** `origin/main@pending`
- **Gate status:** `pending_user_validation`
- **Findings summary:** o baseline original `565ff17a81a6faa663f9e024e9784e396cd50bfe` sustentou as primeiras revisões; findings materiais exigiram escopo reduzido, decisões revisadas e novo freeze.
- **Evidence / reference:** baseline original `565ff17a81a6faa663f9e024e9784e396cd50bfe`; evidence-only commit `0c2c050861af97f76ffd44724ddcd26be7af6174`; novo baseline pendente.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** o diff final deve permanecer no ST-01 documental.
- **Trigger stage:** `after planning review converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Gate status:** `not_run`
- **Findings summary:** drift material reconhecido pelas revisões; guard será executado somente após validação do usuário, refreeze e reconvergência.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [ ] Usuário valida o escopo reduzido e D-01..D-11 após integração dos findings?
- [x] `AMB-03`: fases são temas; horizonte é `Now|Next|Later|Unscheduled`, sem datas implícitas (`D-01`).
- [x] `AMB-04`: adotar `foundation_documentation/backlog/` fora de `todos/active/` (`D-02`).

## Confirmed Constraints (No Live Assumptions)

| Constraint ID | Constraint | Evidence | Handling |
| --- | --- | --- | --- |
| `C-01` | Foundation é a autoridade de produto/governança. | `README.md`, constituição | preserve |
| `C-02` | As quatro fases atuais serão preservadas por decisão de escopo, não por inferência de validade completa. | `D-01` | frozen after user validation |
| `C-03` | Os quatro módulos atuais e seu conteúdo permanecem inalterados neste recorte. | Out of Scope + Diff Expectation Contract | preserve |
| `C-04` | Datas não entram sem aprovação explícita. | `D-01` | frozen after user validation |

## Execution Plan

### Touched Surfaces

- Authority/navigation: `README.md`, `project_constitution.md`, `evolution_lifecycle.md`.
- Planning: `system_roadmap.md`, `backlog/`, `decisions/`.
- Local contracts: `modules/README.md`, `contracts/README.md`; módulos individuais são observe-only.
- Evidence/execution: `artifacts/README.md`, feature brief, `todos/README.md`, este TODO.

### Ordered Steps

1. Validar com o usuário o escopo reduzido e D-01..D-11 após os primeiros reviews.
2. Atualizar o feature brief, congelar/publicar novo baseline e rerodar reviews afetados.
3. Rodar coherence/scope-drift/pre-approval guards e solicitar `APROVADO`.
4. Implementar authority matrix, papéis, state machines e lifecycle central.
5. Implementar backlog, decisions, roadmap e navegação sem duplicar estado vivo.
6. Atualizar somente `modules/README.md` e `contracts/README.md`; preservar módulos individuais.
7. Registrar ST-02/ST-03/ST-04 com as disposições D-08 e validar cenários positivo/negativo.
8. Executar validações, decision/module adherence, auditorias, revisão final e closeout.

### Test Strategy

- **Strategy:** `test-after`
- **Why:** mudança exclusivamente documental; os testes são navegação, vocabulário, autoridade, diff e guards.
- **Fail-first targets:** `n/a`; o diagnóstico está documentado no feature brief e neste TODO.

### Flow Evidence Planning Matrix

| Flow | Entry | Expected Transition | Evidence |
| --- | --- | --- | --- |
| ST-03 | feature brief/discovery | `BLG-whatsflow-channel-attendance-study`, `Selected-for-Planning`, sem execução | links e owner canônico |
| candidato selecionado | backlog | TODO `Draft|Review`; ainda sem execução | negative authorization check |
| TODO aprovado | explicit `APROVADO` + guard `go` | `Approved|In-Progress` | authority evidence |
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

- **Status:** `findings_integrated`; escopo materialmente revisado e pendente de validação do usuário, refreeze e nova rodada.

### Review Sections

| Lens | Preliminary Position |
| --- | --- |
| Architecture | field-level ownership e máquinas ortogonais evitam autoridade duplicada |
| Code Quality | n/a; nenhum código de produto ou validator novo |
| Tests | checks exatos + cenários positivo/negativo; validator permanente condicionado ao gatilho D-09 |
| Performance | sem impacto de runtime |
| Security | reduz risco de claims/segredos legados virarem autoridade; não toca trust boundaries |
| Elegance | lifecycle possui schemas/transições; cada valor vivo existe em um único owner |
| Structural Soundness | IDs imutáveis e links substituem sincronização N-way de estado |

### Issue Cards

#### PR-01 — Horizonte do roadmap

- **Severity:** medium
- **Evidence:** `system_roadmap.md` possui fases sem estado, dependência ou saída.
- **Why now:** os próximos estudos precisam de um local previsível sem falsa promessa de data.
- **A:** quarters/releases; maior previsibilidade temporal, maior risco de compromisso fictício.
- **B:** fases como temas + `Now/Next/Later/Unscheduled`; separa estratégia de agendamento sem datas falsas.
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
- **Recommendation:** B (`D-09`), com owner e gatilho mensurável para validator permanente.

#### PR-04 — Contrato vivo versus execução aprovada

- **Severity:** high
- **Evidence:** o fluxo de refinamento exige TODO em `active/` antes do `APROVADO`.
- **Why now:** tratar localização como aprovação tornaria o próprio processo circular.
- **A:** manter `active = approved`; incompatível com o workflow.
- **B:** `active = live tactical contract`; execução exige `APROVADO` + authority guard `go`.
- **C:** criar uma nova árvore `draft/`; aumenta movimentações e tooling sem necessidade.
- **Recommendation:** B (`D-02`); separa estado documental de autoridade de execução.

#### PR-05 — Owner dos campos vivos

- **Severity:** high
- **Evidence:** o plano inicial repetia estado/dependências entre backlog, roadmap, modules, decisions e TODO.
- **Why now:** sincronização N-way destruiria previsibilidade e aumentaria custo operacional.
- **A:** duplicar campos e exigir revisão manual; frágil.
- **B:** matriz de owner único com IDs/links; simples e auditável.
- **C:** centralizar tudo em um único arquivo; reduz ownership modular.
- **Recommendation:** B (`D-06`); maior elegância e solidez estrutural.

### Failure Modes & Edge Cases

- Duplicar estado divergente entre roadmap, backlog e TODO.
- Transformar `Selected-for-Planning` no backlog ou presença em `active/` em autorização de execução.
- Inventar maturidade de módulo ou contrato sem evidência.
- Reclassificar documentos históricos retroativamente.
- Usar horizonte relativo como substituto de prioridade ou dependência.
- Absorver alterações preexistentes no diff do ST-01.

### Residual Unknowns / Risks

- **Assumptions:** nenhuma premissa viva; C-01..C-04 são constraints/decisões verificáveis.
- **Unknowns:** baseline histórico exato da transposição pertence ao ST-02, não a este TODO.
- **Confidence:** high no escopo revisado; nova rodada independente obrigatória após validação/refreeze.

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** governança transversal exige crítica externa sobre complexidade acidental e autoridade duplicada.
- **Opinion count:** `1`
- **Package mode:** `bounded-file-set`
- **Internal reviewer mandate:** `required; fresh no-context reviewer after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `/root/st01_architecture_review` | corrigir autoridade, owners, transições, papéis e proteção | runtime neutro; evitar sincronização N-way | owner único + IDs/links | máquinas ortogonais antes de aprovação | Integrated; rerun required | findings `ST01-ARCH-001..007` |

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Latest TEACH evidence / artifact:** guard `go`, fingerprint `ef66891d75b2`; deve rerodar após `high_severity_plan_review_issue=yes`.

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
| `high_severity_plan_review_issue` | `yes` | PR-04 e PR-05 high, integrados no plano revisado |
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
- **Critique status:** `findings_integrated`
- **Findings summary:** autoridade, diff schema, assumptions, owners, DoD/evidence, audit floor e taxonomia foram revisados; nova rodada exigida após validação/refreeze.
- **Evidence / reference:** reviewer `/root/st01_plan_critique`, findings `ST01-R01..R08`.
- **Waiver authority / reference:** `n/a`

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `ST01-R01` | Integrated | useful | yes | project | `D-02` | active não implica approval |
| `ST01-R02` | Integrated | useful | yes | project | `Diff Expectation Contract` | schema, baseline, labels e closeout corrigidos |
| `ST01-R03` | Integrated | useful | yes | project | `C-01..C-04` | assumptions removidas/promovidas |
| `ST01-R04` | Integrated | useful | yes | project | `D-03,D-05,D-06` | owner único e scope reduzido |
| `ST01-R05` | Integrated | useful | yes | project | `DOD/VAL + adherence tables` | evidência 1-1 planejada |
| `ST01-R06` | Integrated | useful | yes | paced | `Audit Trigger Matrix` | high trigger e test audit ajustados |
| `ST01-R07` | Integrated | useful | yes | project | `D-01,D-04,D-10` | taxonomia e IDs revisados |
| `ST01-R08` | Integrated | useful | yes | project | `Delivery/Execution state` | status e próximos passos atualizados |
| `ST01-ARCH-001` | Integrated | useful | yes | project | `D-02` | execução exige aprovação explícita |
| `ST01-ARCH-002` | Integrated | useful | yes | project | `D-06` | field-level authority matrix |
| `ST01-ARCH-003` | Integrated | useful | yes | project | `D-01,D-04` | state machines e phase/horizon semantics |
| `ST01-ARCH-004` | Integrated | useful | partial | project | `Review state consistency` | freeze-dependent fields sincronizados |
| `ST01-ARCH-005` | Integrated | useful | yes | project | `D-11` | papéis provider-neutral |
| `ST01-ARCH-006` | Integrated | useful | yes | project | `D-09` | validator trigger mensurável |
| `ST01-ARCH-007` | Integrated | useful | yes | project | `D-08` | disposições por story reconciliadas |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** o primeiro review encontrou assumptions inadequadas; após promovê-las para constraints/decisions, o guard deve confirmar que nenhuma assumption viva permanece.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `none; verify no live Assumptions Preview rows remain`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Gate status:** `not_run`
- **Findings summary:** aguardando validação do usuário, refreeze e nova crítica.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending explicit APROVADO after preflight-go`
- **Approval scope:** `pending`
- **Execution not authorized by approval:** código/produto/referências, execução de ST-02/ST-03/ST-04, migração dos módulos individuais e mudanças de domínio.
- **Renewed approval required when:** qualquer decisão D-01..D-11, escopo, validator, contrato de produto ou arquivo esperado mudar materialmente.

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

## Decision Adherence Validation (Mandatory Before Delivery)

| Decision ID | Status (`Adherent`/`Exception`) | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01` | pending | planned canonical diff + lifecycle walkthrough | pending validation and implementation |
| `D-02` | pending | planned backlog/TODO authority walkthrough | pending validation and implementation |
| `D-03` | pending | planned feature-brief handoff review | pending validation and implementation |
| `D-04` | pending | planned transition-table positive/negative scenarios | pending validation and implementation |
| `D-05` | pending | planned decision-to-canonical-target trace | pending validation and implementation |
| `D-06` | pending | planned field-owner matrix audit | pending validation and implementation |
| `D-07` | pending | planned historical-surface diff check | pending validation and implementation |
| `D-08` | pending | planned ST-02/ST-03/ST-04 disposition trace | pending validation and implementation |
| `D-09` | pending | planned threshold/owner check | pending validation and implementation |
| `D-10` | pending | planned ID/schema check | pending validation and implementation |
| `D-11` | pending | planned provider-neutral role review | pending validation and implementation |

Only `Adherent` or an explicitly approved `Exception` is valid at delivery.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Module Decision Ref | Planned Handling | Delivery Status (`Preserved|Superseded (Approved)|Regression`) | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `modules/README#ownership` | Preserve | pending | planned 1-1 diff/review | README may gain lifecycle pointers without changing ownership |
| `identity-and-tenancy#invariants` | Preserve | pending | planned SHA/diff + semantic review | file must remain unchanged |
| `inbox-and-conversations#invariants` | Preserve | pending | planned SHA/diff + semantic review | file must remain unchanged |
| `audit-and-history#invariants` | Preserve | pending | planned SHA/diff + semantic review | file must remain unchanged |
| `integrations-and-channels#invariants` | Preserve | pending | planned SHA/diff + semantic review | file must remain unchanged |

### Exception Handling

- Qualquer decisão marcada `Exception` bloqueia a entrega até a exceção ou alternativa ser explicitamente aprovada e o baseline receber novo `APROVADO`.
- Qualquer decisão de módulo marcada `Regression` bloqueia a entrega até existir supersessão intencional aprovada e consolidação no módulo canônico.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** contrato em revalidação após findings materiais; nenhuma implementação canônica iniciada.
- **Post-commit/push status:** `pending`
- **Next path/status action:** usuário valida o escopo revisado; então novo baseline, reviews e preflight.

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

- **Audit decision:** `recommended`
- **Why this decision:** piso determinístico para TODO medium; será focalizado na eficácia dos checks estruturais, embora não haja teste de produto.
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
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py --repo-root foundation_documentation foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/todo_completion_guard.py --require-delivery foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/todo_closeout_guard.py --repo foundation_documentation foundation_documentation/todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `git -C foundation_documentation diff --check d8626df1fb0ff64751d7fae10ae93cf41ab1a458 -- README.md project_constitution.md evolution_lifecycle.md backlog decisions system_roadmap.md modules/README.md contracts/README.md artifacts/README.md artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md todos/README.md todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `git -C foundation_documentation diff --exit-code d8626df1fb0ff64751d7fae10ae93cf41ab1a458 -- modules/identity-and-tenancy.md modules/inbox-and-conversations.md modules/audit-and-history.md modules/integrations-and-channels.md`
- `sha256sum foundation_documentation/.gitattributes foundation_documentation/.gitignore foundation_documentation/artifacts/migration/claude-legacy-reconciliation-review.prompt.txt foundation_documentation/artifacts/publication-manifest.txt foundation_documentation/deterministic/.gitkeep foundation_documentation/todos/ephemeral/.gitignore foundation_documentation/todos/ephemeral/.gitkeep foundation_documentation/todos/promotion_lane/.gitkeep` (comparar exatamente com a tabela de preservação).
- `rg -n '(api[_-]?key|client[_-]?secret|password|authorization:[[:space:]]*bearer|BEGIN [A-Z ]*PRIVATE KEY)'` limitado aos paths pertencentes ao ST-01; qualquer ocorrência exige classificação explícita antes da entrega.
