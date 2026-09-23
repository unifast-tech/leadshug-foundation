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

- **Current delivery stage:** `Production-Ready`
- **Tactical TODO lifecycle state:** `Completed`
- **Lifecycle state evidence:** pacote documental publicado em `foundation_documentation/main@ad6a0cc8475bc412fd1b767e9cc19ad0123fb6fe`; authority/diff/completion/closeout guards, auditorias e revisão final retornaram `go`/`no_material_findings` antes do closeout.
- **TODO owner/executor:** strategic steward como TODO owner; implementação documental delegada ao routine-executor sob single-writer no checkout principal.
- **Qualifiers:** `none`
- **Next exact step:** `n/a — completed`; qualquer trabalho futuro do validator pertence ao TODO separado em `todos/active/process/`.

## Active Work State

- **Work state:** `n/a once moved out of active`
- **Why this state now:** entrega publicada e TODO movido para `completed/` após guards pré-movimento em `go`.
- **Exit condition:** `n/a — completed`.

## Scope

- [x] Criar `evolution_lifecycle.md` como contrato canônico do fluxo descoberta → candidato → planejamento → aprovação → entrega → encerramento.
- [x] Criar `backlog/README.md` como autoridade de trabalho candidato ainda não aprovado e registrar ST-02, ST-03 e ST-04 como itens independentes.
- [x] Criar `decisions/README.md` como índice de proveniência/racional de decisões duráveis e definir quando uma decisão aceita se torna efetiva nas superfícies canônicas.
- [x] Evoluir `system_roadmap.md` para horizontes relativos, status derivado do exit gate, dependências, resultado esperado e critério de saída, preservando as quatro fases estratégicas.
- [x] Evoluir `modules/README.md` para declarar a autoridade dos módulos e o schema futuro, preservando integralmente os quatro documentos de módulo atuais neste recorte.
- [x] Evoluir `contracts/README.md` como índice e regra de verificação, sem transformá-lo em uma segunda autoridade do estado dos contratos nem inventar contratos não verificados.
- [x] Alinhar `README.md`, `project_constitution.md`, `todos/README.md` e `artifacts/README.md` ao novo lifecycle.
- [x] Atualizar o feature brief com o handoff canônico do ST-01, sem copiar estados vivos, preservando ST-02, ST-03 e ST-04 como stories independentes do programa.
- [x] Definir uma matriz de autoridade por campo, papéis neutros de fornecedor e máquinas de estado/transições separadas para candidatos, capacidades, TODOs, decisões e verificação de contratos.
- [x] Validar cenários positivo e negativo: ST-03 nasce em descoberta, entra no backlog e permanece sem autoridade de execução; mover um TODO para `active/` sem `APROVADO` não autoriza implementação.

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
| Foundation evolution lifecycle | `foundation_documentation:main@ad6a0cc8475bc412fd1b767e9cc19ad0123fb6fe` | `n/a — main-only authority` | `n/a` | `direct governed Foundation write; ad6a0cc8475bc412fd1b767e9cc19ad0123fb6fe` | `Production-Ready; closeout commit pending` |

## Out of Scope

- [ ] Alterar código, testes, schema, runtime ou configuração do LeadsHug.
- [ ] Executar os estudos ST-02, ST-03 ou a síntese ST-04.
- [ ] Canonizar conceitos de canal, fila, equipe, setor, SLA, automação ou IA.
- [ ] Inventariar todos os endpoints ou afirmar cobertura contratual sem evidência.
- [ ] Reescrever artifacts, TODOs concluídos ou decisões históricas retroativamente.
- [ ] Limpar, normalizar ou incluir mudanças preexistentes não pertencentes a este TODO.
- [ ] Criar worktree, branch auxiliar, checkout alternativo ou cópia gravável da Foundation.
- [ ] Migrar individualmente os quatro módulos atuais para um novo schema ou declarar maturidade/capacidades não verificadas.
- [ ] Generalizar neste ST-01 a política de referência independente para `whatsflow_v2`; `AMB-05` fica diferida para o framing de ST-03 ou TODO próprio antes de qualquer estudo que possa ser interpretado como permissão de copiar/acoplar.

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
| Foundation | `todos/active/process/TODO-foundation-lifecycle-structural-validator.md` | `A` | follow-up separado acionado pelo limiar D-09; permanece em Review sem autoridade de execução |
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

- [x] `DOD-01` `evolution_lifecycle.md` define schemas e transições sem duplicar valores vivos pertencentes a backlog, roadmap, módulos, decisões ou TODOs.
- [x] `DOD-02` Ideias não aprovadas possuem uma superfície de backlog separada de `todos/active/`.
- [x] `DOD-03` `todos/active/` contém contratos táticos vivos, mas somente `APROVADO` explícito e o guard de autoridade concedem execução.
- [x] `DOD-04` Cada valor vivo possui um único owner canônico e as demais superfícies usam IDs/links, conforme matriz de autoridade.
- [x] `DOD-05` Candidatos, capacidades, TODOs, decisões e contratos possuem máquinas de estado ortogonais, transições, atores, evidências e caminhos de cancelamento/reabertura.
- [x] `DOD-06` O roadmap informa tema/fase, horizonte relativo, status derivado do exit gate, dependências, resultado e critério de saída sem compromissos de calendário nem atribuir maturidade de capacidade.
- [x] `DOD-07` Módulos atuais permanecem intactos e `modules/README.md` declara somente sua autoridade e schema futuro.
- [x] `DOD-08` Decisões preservam racional/proveniência e só se tornam efetivas após consolidação nos alvos canônicos nomeados.
- [x] `DOD-09` Contratos usam estado de verificação explícito sem afirmações não verificadas e `contracts/README.md` permanece apenas índice/regra.
- [x] `DOD-10` ST-02 e ST-03 ficam `Selected-for-Planning` após o ST-01; ST-04 fica `Deferred` até ST-02/ST-03, todos sem autoridade de execução.
- [x] `DOD-11` README, constituição, artifacts e TODO governance mantêm coerência quanto a papéis neutros, índices de acesso documental e autoridade.
- [x] `DOD-12` A necessidade de validator permanente tem owner e gatilho mensurável, enquanto os checks atuais são exatos e reproduzíveis.
- [x] `DOD-13` Nenhum arquivo de produto, referência ou mudança preexistente fora do escopo foi alterado pelo ST-01.

## Validation Steps

- [x] `VAL-01` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-01`; exigir exit `0` e `OK: all changed Markdown links resolve`.
- [x] `VAL-02` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-02`; exigir exit `0` e `OK: IDs, candidate records, and lifecycle enums are coherent`.
- [x] `VAL-03` Simular a trajetória documental do ST-03 até o backlog e confirmar que `Selected-for-Planning` não concede `APROVADO`.
- [x] `VAL-04` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-04`; o fixture temporário deve receber exit `2` e ao menos uma das violações de aprovação declaradas no contrato, enquanto o wrapper retorna `0` e remove os fixtures via `trap`.
- [x] `VAL-05` Comparar 1-1 as decisões e o conteúdo atual dos quatro módulos, comprovando que permaneceram inalterados.
- [x] `VAL-06` Executar `bash delphi-ai/tools/verify_context.sh`.
- [x] `VAL-07` Antes de solicitar aprovação, exigir `todo_authority_guard.py ... --pre-approval` com `Overall outcome: preflight-go`; após `APROVADO` e ingestão, exigir o guard normal sem flag com `Overall outcome: go` antes de qualquer implementação. Executar também os guards de diff, conclusão e closeout nos gates correspondentes.
- [x] `VAL-08` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-08`; exigir exit `0` e `OK: tracked and untracked ST-01 files pass whitespace checks`.
- [x] `VAL-09` Recalcular os oito hashes preexistentes registrados e exigir igualdade byte a byte.
- [x] `VAL-10` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-10`; exigir exit `0` e `OK: no secret-like assignments or private keys in ST-01 paths`.
- [x] `VAL-11` Concluir crítica pré-aprovação, revisão final e auditorias derivadas pelo piso determinístico.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SCOPE-01` | Scope | Criar `evolution_lifecycle.md` como contrato canônico do fluxo descoberta → candidato → planejamento → aprovação → entrega → encerramento. | doc | `evolution_lifecycle.md` | n/a | passed | contrato, papéis, ownership e transições consolidados |
| `SCOPE-02` | Scope | Criar `backlog/README.md` como autoridade de trabalho candidato ainda não aprovado e registrar ST-02, ST-03 e ST-04 como itens independentes. | doc | `backlog/README.md` contém três registros BLG únicos | n/a | passed | autoridade e próximo gate permanecem no backlog |
| `SCOPE-03` | Scope | Criar `decisions/README.md` como índice de proveniência/racional de decisões duráveis e definir quando uma decisão aceita se torna efetiva nas superfícies canônicas. | doc | `decisions/README.md` e `decisions/ST-01-foundation-lifecycle-decisions.md` | n/a | passed | onze decisões imutáveis e eficácia por consolidação |
| `SCOPE-04` | Scope | Evoluir `system_roadmap.md` para horizontes relativos, status derivado do exit gate, dependências, resultado esperado e critério de saída, preservando as quatro fases estratégicas. | doc | `system_roadmap.md` horizon rule e tabela com quatro fases | n/a | passed | gate status não projeta maturidade de capacidade |
| `SCOPE-05` | Scope | Evoluir `modules/README.md` para declarar a autoridade dos módulos e o schema futuro, preservando integralmente os quatro documentos de módulo atuais neste recorte. | doc+diff | schema futuro em `modules/README.md`; diff dos quatro módulos individuais exit `0` | local | passed | somente o índice de módulos foi evoluído |
| `SCOPE-06` | Scope | Evoluir `contracts/README.md` como índice e regra de verificação, sem transformá-lo em uma segunda autoridade do estado dos contratos nem inventar contratos não verificados. | doc | `contracts/README.md` | n/a | passed | índice não declara inventário ou cobertura |
| `SCOPE-07` | Scope | Alinhar `README.md`, `project_constitution.md`, `todos/README.md` e `artifacts/README.md` ao novo lifecycle. | doc | diffs dos quatro arquivos e VAL-01 | local | passed | navegação e fronteiras de autoridade alinhadas |
| `SCOPE-08` | Scope | Atualizar o feature brief com o handoff canônico do ST-01, sem copiar estados vivos, preservando ST-02, ST-03 e ST-04 como stories independentes do programa. | doc+test | feature brief canonical handoff e assertion dedicada em VAL-02 | local | passed | stories usam links BLG sem disposição concorrente |
| `SCOPE-09` | Scope | Definir uma matriz de autoridade por campo, papéis neutros de fornecedor e máquinas de estado/transições separadas para candidatos, capacidades, TODOs, decisões e verificação de contratos. | doc | `evolution_lifecycle.md` authority matrix, roles e cinco machines | n/a | passed | campos e transições têm owner explícito |
| `SCOPE-10` | Scope | Validar cenários positivo e negativo: ST-03 nasce em descoberta, entra no backlog e permanece sem autoridade de execução; mover um TODO para `active/` sem `APROVADO` não autoriza implementação. | test+review | walkthroughs em `evolution_lifecycle.md`; VAL-03 e VAL-04 | local | passed | ambos os cenários fecham sem autoridade implícita |
| `DOD-01` | Definition of Done | `DOD-01` `evolution_lifecycle.md` define schemas e transições sem duplicar valores vivos pertencentes a backlog, roadmap, módulos, decisões ou TODOs. | doc | schemas, authority matrix e links canônicos em `evolution_lifecycle.md` | n/a | passed | valores vivos remetem aos owners |
| `DOD-02` | Definition of Done | `DOD-02` Ideias não aprovadas possuem uma superfície de backlog separada de `todos/active/`. | doc | `backlog/README.md` e `todos/README.md` | n/a | passed | backlog separado e não autorizativo |
| `DOD-03` | Definition of Done | `DOD-03` `todos/active/` contém contratos táticos vivos, mas somente `APROVADO` explícito e o guard de autoridade concedem execução. | doc+guard | lifecycle tactical TODO machine; VAL-04; authority guard pós-aprovação `go` | local | passed | localização e autoridade são independentes |
| `DOD-04` | Definition of Done | `DOD-04` Cada valor vivo possui um único owner canônico e as demais superfícies usam IDs/links, conforme matriz de autoridade. | doc+review | lifecycle authority matrix e correções ST01-ADR | n/a | passed | estrutura documental sem fluxo de usuário; brief e roadmap não copiam estado de outro owner |
| `DOD-05` | Definition of Done | `DOD-05` Candidatos, capacidades, TODOs, decisões e contratos possuem máquinas de estado ortogonais, transições, atores, evidências e caminhos de cancelamento/reabertura. | doc | cinco state machines em `evolution_lifecycle.md` | n/a | passed | atores, evidências e retorno estão explícitos |
| `DOD-06` | Definition of Done | `DOD-06` O roadmap informa tema/fase, horizonte relativo, status derivado do exit gate, dependências, resultado e critério de saída sem compromissos de calendário nem atribuir maturidade de capacidade. | doc+review | `system_roadmap.md` e resolução ST01-ADR-001 | n/a | passed | estrutura documental sem fluxo de usuário; quatro temas preservados e status derivado da evidência |
| `DOD-07` | Definition of Done | `DOD-07` Módulos atuais permanecem intactos e `modules/README.md` declara somente sua autoridade e schema futuro. | diff | schema futuro em `modules/README.md`; four-module diff exit `0` | local | passed | conteúdo individual inalterado |
| `DOD-08` | Definition of Done | `DOD-08` Decisões preservam racional/proveniência e só se tornam efetivas após consolidação nos alvos canônicos nomeados. | doc+review | `decisions/ST-01-foundation-lifecycle-decisions.md`; constitution hierarchy | n/a | passed | cada DEC nomeia targets e evidência de consolidação |
| `DOD-09` | Definition of Done | `DOD-09` Contratos usam estado de verificação explícito sem afirmações não verificadas e `contracts/README.md` permanece apenas índice/regra. | doc | `contracts/README.md` e contract machine no lifecycle | n/a | passed | nenhum inventário ou cobertura inferido |
| `DOD-10` | Definition of Done | `DOD-10` ST-02 e ST-03 ficam `Selected-for-Planning` após o ST-01; ST-04 fica `Deferred` até ST-02/ST-03, todos sem autoridade de execução. | doc+test | três registros em `backlog/README.md`; VAL-02 | local | passed | estados existem somente no backlog |
| `DOD-11` | Definition of Done | `DOD-11` README, constituição, artifacts e TODO governance mantêm coerência quanto a papéis neutros, índices de acesso documental e autoridade. | doc+review | root README, constitution, artifacts README e todos README | n/a | passed | estrutura documental sem runtime; ferramentas são adapters dos papéis |
| `DOD-12` | Definition of Done | `DOD-12` A necessidade de validator permanente tem owner e gatilho mensurável, enquanto os checks atuais são exatos e reproduzíveis. | doc+test | deterministic-adoption trigger, `TODO-foundation-lifecycle-structural-validator.md` e Exact Check Command Contracts | local | passed | limiar de 18 registros abriu follow-up em Review; nenhum validator foi implementado sem aprovação |
| `DOD-13` | Definition of Done | `DOD-13` Nenhum arquivo de produto, referência ou mudança preexistente fora do escopo foi alterado pelo ST-01. | diff+hash | diff expectation guard `go`; VAL-05 e VAL-09 | local | passed | paths e hashes fora do pacote preservados |
| `VAL-01` | Validation Steps | `VAL-01` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-01`; exigir exit `0` e `OK: all changed Markdown links resolve`. | test | exact VAL-01 output e exit code | local | passed | structure-only check executado no pacote corrigido |
| `VAL-02` | Validation Steps | `VAL-02` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-02`; exigir exit `0` e `OK: IDs, candidate records, and lifecycle enums are coherent`. | test | exact VAL-02 output e exit code | local | passed | structure-only check cobre BLG, DEC, enums e ausência de disposição concorrente no brief |
| `VAL-03` | Validation Steps | `VAL-03` Simular a trajetória documental do ST-03 até o backlog e confirmar que `Selected-for-Planning` não concede `APROVADO`. | review | structure-only walkthrough e registro BLG do ST-03 | n/a | passed | planejamento não concede execução |
| `VAL-04` | Validation Steps | `VAL-04` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-04`; o fixture temporário deve receber exit `2` e ao menos uma das violações de aprovação declaradas no contrato, enquanto o wrapper retorna `0` e remove os fixtures via `trap`. | test+guard | exact VAL-04 wrapper exit `0`; inner guard exit `2` | local | passed | structure-only fixture falhou fechado e foi removido |
| `VAL-05` | Validation Steps | `VAL-05` Comparar 1-1 as decisões e o conteúdo atual dos quatro módulos, comprovando que permaneceram inalterados. | diff+review | Module Decision Consistency Validation e four-module diff exit `0` | local | passed | decisões de módulo preservadas |
| `VAL-06` | Validation Steps | `VAL-06` Executar `bash delphi-ai/tools/verify_context.sh`. | test | canonical context verifier exit `0`; `PACED-Ready` | local | passed | contexto íntegro |
| `VAL-07` | Validation Steps | `VAL-07` Antes de solicitar aprovação, exigir `todo_authority_guard.py ... --pre-approval` com `Overall outcome: preflight-go`; após `APROVADO` e ingestão, exigir o guard normal sem flag com `Overall outcome: go` antes de qualquer implementação. Executar também os guards de diff, conclusão e closeout nos gates correspondentes. | guard | preapproval/postapproval históricos; authority `--require-delivery-gates`, diff e closeout `go`; completion bootstrap recusou somente a própria linha VAL-07 antes desta marcação | local | passed | rerun final de completion obrigatório após esta atualização self-referential |
| `VAL-08` | Validation Steps | `VAL-08` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-08`; exigir exit `0` e `OK: tracked and untracked ST-01 files pass whitespace checks`. | test | exact VAL-08 output e exit code | local | passed | structure-only whitespace check cobre tracked, staged e untracked |
| `VAL-09` | Validation Steps | `VAL-09` Recalcular os oito hashes preexistentes registrados e exigir igualdade byte a byte. | test | `sha256sum` dos oito paths preservados | local | passed | todos os hashes iguais ao baseline |
| `VAL-10` | Validation Steps | `VAL-10` No cwd raiz do workspace, executar `Exact Check Command Contracts / VAL-10`; exigir exit `0` e `OK: no secret-like assignments or private keys in ST-01 paths`. | security | exact VAL-10 output e exit code | local | passed | structure-only probes e scan real satisfatórios |
| `VAL-11` | Validation Steps | `VAL-11` Concluir crítica pré-aprovação, revisão final e auditorias derivadas pelo piso determinístico. | review | critique V5; adherence, test-quality V3, cutover/P1-P2 e final-review revalidation | n/a | passed | `/root/st01_independent_final_review_revalidation` retornou `no_material_findings` em 2026-09-23 |

## Exact Check Command Contracts

Todos os comandos abaixo executam a partir da raiz do workspace, não criam arquivos persistentes e têm os critérios de saída declarados.

### VAL-01 — Relative Markdown Links

```bash
python3 - <<'PY'
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

repo = Path("foundation_documentation")
baseline = "d8626df1fb0ff64751d7fae10ae93cf41ab1a458"
tracked = subprocess.run(
    ["git", "-C", str(repo), "diff", "--name-only", baseline, "--", "*.md"],
    check=True,
    capture_output=True,
    text=True,
).stdout.splitlines()
untracked = subprocess.run(
    ["git", "-C", str(repo), "ls-files", "--others", "--exclude-standard", "--", "*.md"],
    check=True,
    capture_output=True,
    text=True,
).stdout.splitlines()
changed = sorted(set(tracked + untracked))
missing = []
for relative in changed:
    source = repo / relative
    if not source.is_file():
        continue
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
        target = raw.strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = target.split(maxsplit=1)[0]
        if not target or target.startswith(("#", "http://", "https://", "mailto:", "data:", "app://")):
            continue
        target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        resolved = Path(target) if Path(target).is_absolute() else source.parent / target
        if not resolved.exists():
            missing.append(f"{relative} -> {target}")
if missing:
    print("Missing Markdown targets:", *missing, sep="\n- ")
    sys.exit(1)
print("OK: all changed Markdown links resolve")
PY
```

Expected: exit `0` and exactly one final `OK` line; any missing target prints its source mapping and exits `1`.

### VAL-02 — IDs, Candidate Records, and Enums

```bash
python3 - <<'PY'
import html
import re
import sys
import unicodedata
from pathlib import Path

backlog = Path("foundation_documentation/backlog/README.md").read_text(encoding="utf-8")
lifecycle = Path("foundation_documentation/evolution_lifecycle.md").read_text(encoding="utf-8")
feature_brief = Path("foundation_documentation/artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md").read_text(encoding="utf-8")
decision_record = Path("foundation_documentation/decisions/ST-01-foundation-lifecycle-decisions.md").read_text(encoding="utf-8")
expected_candidates = {
    "BLG-central-whatsapp-capability-study": "Selected-for-Planning",
    "BLG-whatsflow-channel-attendance-study": "Selected-for-Planning",
    "BLG-leadshug-evolution-synthesis": "Deferred",
}
expected_handoffs = {
    "ST-01": ("Governing ST-01 TODO", "../../todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md"),
    "ST-02": ("BLG-central-whatsapp-capability-study", "../../backlog/README.md"),
    "ST-03": ("BLG-whatsflow-channel-attendance-study", "../../backlog/README.md"),
    "ST-04": ("BLG-leadshug-evolution-synthesis", "../../backlog/README.md"),
}
expected_decisions = {
    "DEC-roadmap-relative-horizons": {
        "direction": "Preserve four strategic themes and add orthogonal relative horizons.",
        "rationale": "Dates/releases were rejected as false commitments; unchanged phases were too ambiguous.",
        "targets": {"system_roadmap.md"},
    },
    "DEC-candidate-backlog-boundary": {
        "direction": "Keep non-approved candidates in a backlog separate from tactical TODOs.",
        "rationale": "An active TODO backlog was rejected because location could be mistaken for authority.",
        "targets": {"backlog/README.md", "todos/README.md", "project_constitution.md"},
    },
    "DEC-feature-brief-evidence-only": {
        "direction": "Treat feature briefs as non-authoritative discovery evidence after handoff.",
        "rationale": "Keeping live dispositions in briefs was rejected because it duplicates owner state.",
        "targets": {"artifacts/README.md", "artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md"},
    },
    "DEC-orthogonal-lifecycle-machines": {
        "direction": "Use separate state machines for candidates, capabilities, tactical TODOs, decisions, and contract verification; keep `Blocked` as a qualifier.",
        "rationale": "A shared overloaded status was rejected because it erases meaning and transition authority.",
        "targets": {"evolution_lifecycle.md"},
    },
    "DEC-decision-effectiveness-after-consolidation": {
        "direction": "An accepted decision becomes effective only after all named canonical targets are consolidated.",
        "rationale": "Decision text overriding current module/constitution truth was rejected.",
        "targets": {"decisions/README.md", "evolution_lifecycle.md", "project_constitution.md"},
    },
    "DEC-single-field-authority": {
        "direction": "Assign one canonical owner to every live field and use links/IDs elsewhere.",
        "rationale": "N-way copied state was rejected because it drifts and obscures authority.",
        "targets": {"evolution_lifecycle.md", "project_constitution.md", "README.md", "modules/README.md", "contracts/README.md", "artifacts/README.md", "todos/README.md"},
    },
    "DEC-historical-adoption-boundary": {
        "direction": "Apply the lifecycle to new or materially changed records without retroactively rewriting history.",
        "rationale": "Bulk migration was rejected because it would change unrelated evidence without its own approval.",
        "targets": {"evolution_lifecycle.md"},
    },
    "DEC-pre-code-study-dispositions": {
        "direction": "Keep ST-02/ST-03 planning candidates and defer ST-04 until both studies conclude.",
        "rationale": "Immediate study execution or combined program execution was rejected as premature authority.",
        "targets": {"backlog/README.md"},
    },
    "DEC-validator-adoption-trigger": {
        "direction": "Use exact manual checks now and require a validator TODO after a measurable volume/drift trigger.",
        "rationale": "Immediate tooling was disproportionate; no control left drift undetected.",
        "targets": {"evolution_lifecycle.md", "todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md", "todos/active/process/TODO-foundation-lifecycle-structural-validator.md"},
    },
    "DEC-immutable-lifecycle-identifiers": {
        "direction": "Use immutable namespace-and-slug IDs for candidates, decisions, and capabilities.",
        "rationale": "Mutable titles/filenames alone were rejected as unstable references.",
        "targets": {"evolution_lifecycle.md", "backlog/README.md", "decisions/ST-01-foundation-lifecycle-decisions.md"},
    },
    "DEC-provider-neutral-lifecycle-roles": {
        "direction": "Define human decision authority, strategic steward, module owner, TODO owner/executor, and assurance reviewer independently of providers/tools.",
        "rationale": "Tool-named product authority was rejected as vendor-coupled governance.",
        "targets": {"evolution_lifecycle.md", "project_constitution.md", "README.md"},
    },
}
expected_decision_evidence = {
    "DEC-roadmap-relative-horizons": "`system_roadmap.md` contains the horizon rule and four theme rows.",
    "DEC-candidate-backlog-boundary": "`backlog/README.md` owns candidates; `todos/README.md` separates tactical contracts; `project_constitution.md` requires explicit approval authority.",
    "DEC-feature-brief-evidence-only": "`artifacts/README.md` defines the evidence-only rule; `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` implements canonical handoff links without copied live dispositions.",
    "DEC-orthogonal-lifecycle-machines": "`evolution_lifecycle.md` contains five enums, transitions, actors/evidence, cancellation/reopening rules, and the shared qualifier.",
    "DEC-decision-effectiveness-after-consolidation": "`decisions/README.md` defines the index rule; `evolution_lifecycle.md` defines effectiveness; `project_constitution.md` makes current canonical truth authoritative.",
    "DEC-single-field-authority": "`evolution_lifecycle.md` owns the authority matrix; `project_constitution.md` encodes governance; `README.md` routes canonical owners; `modules/README.md`, `contracts/README.md`, `artifacts/README.md`, and `todos/README.md` each state their bounded authority.",
    "DEC-historical-adoption-boundary": "`evolution_lifecycle.md` contains the historical-document exception and future-adoption condition.",
    "DEC-pre-code-study-dispositions": "`backlog/README.md` contains three immutable records with live dispositions and next gates.",
    "DEC-validator-adoption-trigger": "`evolution_lifecycle.md` records both triggers and the observed activation; `todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md` contains the exact checks and delivery evidence; `todos/active/process/TODO-foundation-lifecycle-structural-validator.md` owns the triggered follow-up in Review without execution authority.",
    "DEC-immutable-lifecycle-identifiers": "`evolution_lifecycle.md` defines syntax; `backlog/README.md` instantiates BLG IDs; `decisions/ST-01-foundation-lifecycle-decisions.md` instantiates DEC IDs.",
    "DEC-provider-neutral-lifecycle-roles": "`evolution_lifecycle.md` defines role authority; `project_constitution.md` maps lifecycle roles; `README.md` declares tools and agents as adapters.",
}
expected_target_assertions = {
    "DEC-roadmap-relative-horizons": {
        "system_roadmap.md": ("`Now`, `Next`, `Later`, and `Unscheduled` are relative planning horizons", "| Phase 4 — Relationship campaigns | Unscheduled |"),
    },
    "DEC-candidate-backlog-boundary": {
        "backlog/README.md": ("The backlog is the canonical home for candidate work that is not approved for execution.",),
        "todos/README.md": ("Candidate ideas belong in " + "[the backlog]" + "(../backlog/README.md), never in `todos/active/backlog/`.",),
        "project_constitution.md": ("`backlog/` registra candidatos não aprovados e é separado de `todos/active/`.",),
    },
    "DEC-feature-brief-evidence-only": {
        "artifacts/README.md": ("Feature briefs preserve non-authoritative discovery framing.",),
        "artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md": ("**Estado:** evidência de descoberta; estados vivos pertencem aos registros canônicos vinculados; este brief não autoriza implementação",),
    },
    "DEC-orthogonal-lifecycle-machines": {
        "evolution_lifecycle.md": ("## Shared qualifier", "### Candidates", "### Capabilities", "### Tactical TODOs", "### Decisions", "### Contract verification"),
    },
    "DEC-decision-effectiveness-after-consolidation": {
        "decisions/README.md": ("An `Accepted` decision is effective only after its named canonical targets are consolidated.",),
        "evolution_lifecycle.md": ("Acceptance and effectiveness are intentionally distinct",),
        "project_constitution.md": ("Uma decisão `Accepted` só se torna efetiva depois que todos os seus alvos canônicos nomeados forem consolidados",),
    },
    "DEC-single-field-authority": {
        "evolution_lifecycle.md": ("## Authority matrix", "| Candidate disposition and next gate |"),
        "project_constitution.md": ("Backlog possui disposição/próximo gate; roadmap possui tema,",),
        "README.md": ("## Autoridade", "`evolution_lifecycle.md`: schemas, transições, papéis e owner único por campo."),
        "modules/README.md": ("Module documents own local workflows, ownership boundaries, invariants, stable capabilities, local contracts, API definitions, and data shapes.",),
        "contracts/README.md": ("This directory is an index and verification rule, not a second authority for contract behavior or live verification state.",),
        "artifacts/README.md": ("Artifacts contain supporting evidence for discovery, TODOs, and delivery gates.",),
        "todos/README.md": ("Tactical TODOs are live execution contracts.",),
    },
    "DEC-historical-adoption-boundary": {
        "evolution_lifecycle.md": ("This lifecycle governs new or materially changed records.", "must not be retroactively rewritten merely to look current"),
    },
    "DEC-pre-code-study-dispositions": {
        "backlog/README.md": ("| BLG-central-whatsapp-capability-study |", "| BLG-whatsflow-channel-attendance-study |", "| BLG-leadshug-evolution-synthesis |"),
    },
    "DEC-validator-adoption-trigger": {
        "evolution_lifecycle.md": ("more than ten live records combined across backlog, decisions, and roadmap", "first proven recurrence of schema/field-authority drift", "ST-01 reached the volume threshold with 18 live records"),
        "todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md": ("`D-09` Não criar validator permanente neste TODO.", "### VAL-02 — IDs, Candidate Records, and Enums"),
        "todos/active/process/TODO-foundation-lifecycle-structural-validator.md": ("**Observed count:** `18`", "**Execution authority:** `none`"),
    },
    "DEC-immutable-lifecycle-identifiers": {
        "evolution_lifecycle.md": ("`BLG-<slug>`", "`DEC-<slug>`", "`CAP-<slug>`"),
        "backlog/README.md": ("BLG-central-whatsapp-capability-study",),
        "decisions/ST-01-foundation-lifecycle-decisions.md": ("DEC-roadmap-relative-horizons",),
    },
    "DEC-provider-neutral-lifecycle-roles": {
        "evolution_lifecycle.md": ("Roles are provider-neutral.", "| Assurance reviewer |"),
        "project_constitution.md": ("Ferramentas, agentes e fornecedores concretos são adapters desses papéis, não autoridade de produto.",),
        "README.md": ("Ferramentas e agentes concretos são adapters desses papéis.",),
    },
}
candidate_states = {"Proposed", "Under-Review", "Selected-for-Planning", "Deferred", "Rejected"}
decision_states = {"Proposed", "Accepted", "Superseded", "Rejected"}

def table_between(text, start_heading, end_heading=None):
    if start_heading not in text:
        return [], []
    block = text.split(start_heading, 1)[1]
    if end_heading and end_heading in block:
        block = block.split(end_heading, 1)[0]
    rows = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(set(cell.replace(" ", "")) <= {"-", ":"} for cell in cells):
            continue
        rows.append(cells)
    return (rows[0], rows[1:]) if rows else ([], [])

def clean_code(value):
    value = value.strip()
    return value[1:-1] if value.startswith("`") and value.endswith("`") else value

def normalize_rendered_text(value, soft_hyphen):
    value = unicodedata.normalize("NFKC", html.unescape(value))
    normalized = []
    for character in value:
        category = unicodedata.category(character)
        if character == "\u00ad":
            normalized.append(soft_hyphen)
        elif character == "\u2212" or category == "Pd":
            normalized.append("-")
        elif category == "Cf":
            continue
        else:
            normalized.append(character)
    return "".join(normalized)

def validate_documents(backlog_text, lifecycle_text, brief_text, decisions_text, target_overrides=None):
    failures = []
    target_overrides = target_overrides or {}
    in_memory_targets = {
        "backlog/README.md": backlog_text,
        "evolution_lifecycle.md": lifecycle_text,
        "artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md": brief_text,
        "decisions/ST-01-foundation-lifecycle-decisions.md": decisions_text,
    }

    def target_text(target):
        if target in target_overrides:
            return target_overrides[target]
        if target in in_memory_targets:
            return in_memory_targets[target]
        path = Path("foundation_documentation") / target
        return path.read_text(encoding="utf-8") if path.is_file() else ""
    for candidate_id, state in expected_candidates.items():
        if len(re.findall(rf"(?<![A-Za-z0-9-]){re.escape(candidate_id)}(?![A-Za-z0-9-])", backlog_text)) != 1:
            failures.append(f"{candidate_id}: expected exactly one backlog record")
        record = next((line for line in backlog_text.splitlines() if candidate_id in line), "")
        if state not in record:
            failures.append(f"{candidate_id}: expected state {state} on its record line")

    all_ids = re.findall(r"(?<![A-Za-z0-9-])(?:BLG|DEC|CAP)-[A-Za-z0-9-]+", backlog_text + "\n" + lifecycle_text + "\n" + decisions_text)
    for value in all_ids:
        if not re.fullmatch(r"(?:BLG|DEC|CAP)-[a-z0-9]+(?:-[a-z0-9]+)*", value):
            failures.append(f"invalid immutable ID: {value}")

    required_enums = [
        "Proposed|Under-Review|Selected-for-Planning|Deferred|Rejected",
        "Not-Assessed|Discovery|Planned|In-Progress|Delivered|Retired",
        "Draft|Review|Approved|In-Progress|Completed|Cancelled",
        "Proposed|Accepted|Superseded|Rejected",
        "Not-Assessed|Documented|Verified|Deprecated",
    ]
    for enum in required_enums:
        if enum not in lifecycle_text:
            failures.append(f"missing lifecycle enum: {enum}")

    story_header, story_rows = table_between(brief_text, "## Story Decomposition", "## Historical Recommended Sequence")
    if len(story_header) != 9 or story_header[6] != "Canonical handoff (live status elsewhere)":
        failures.append("feature brief: expected canonical-handoff column at index 7")
    if len(story_rows) != len(expected_handoffs):
        failures.append(f"feature brief: expected {len(expected_handoffs)} story rows, got {len(story_rows)}")
    seen_stories = []
    for row in story_rows:
        if len(row) != 9:
            failures.append(f"feature brief: malformed story row with {len(row)} cells")
            continue
        story_id = clean_code(row[0])
        seen_stories.append(story_id)
        expected = expected_handoffs.get(story_id)
        link = re.fullmatch(r"\[(`?)([^\]]+?)\1\]\(([^)]+)\)", row[6])
        if expected is None or link is None:
            failures.append(f"{story_id}: handoff must be one canonical Markdown link")
            continue
        label, target = link.group(2), link.group(3)
        if (label, target) != expected:
            failures.append(f"{story_id}: unexpected handoff {label} -> {target}")
        if any(state in row[6] for state in candidate_states | decision_states):
            failures.append(f"{story_id}: handoff duplicates a live lifecycle state")
    if len(seen_stories) != len(set(seen_stories)):
        failures.append("feature brief: duplicate story IDs are forbidden")
    if set(seen_stories) != set(expected_handoffs):
        failures.append(f"feature brief: story set mismatch {sorted(set(seen_stories))}")
    rendered_briefs = (normalize_rendered_text(brief_text, ""), normalize_rendered_text(brief_text, "-"))
    for state in candidate_states:
        if any(re.search(rf"(?<![A-Za-z0-9-]){re.escape(state)}(?![A-Za-z0-9-])", rendered_brief) for rendered_brief in rendered_briefs):
            failures.append(f"feature brief duplicates live candidate state outside its canonical owner: {state}")

    decision_header, decision_rows = table_between(decisions_text, "**Provenance:**")
    if decision_header != ["Immutable ID", "State", "Question and accepted direction", "Alternatives considered / rationale", "Named canonical targets", "Target-consolidation evidence"]:
        failures.append("decision records: unexpected table schema")
    if len(decision_rows) != len(expected_decisions):
        failures.append(f"decision records: expected {len(expected_decisions)} rows, got {len(decision_rows)}")
    seen_decisions = []
    for row in decision_rows:
        if len(row) != 6:
            failures.append(f"decision records: malformed row with {len(row)} cells")
            continue
        decision_id = clean_code(row[0])
        seen_decisions.append(decision_id)
        contract = expected_decisions.get(decision_id)
        if row[1] != "Accepted":
            failures.append(f"{decision_id}: expected Accepted state, got {row[1]}")
        if contract is None:
            failures.append(f"{decision_id}: unexpected decision record")
        else:
            if row[2] != contract["direction"]:
                failures.append(f"{decision_id}: accepted direction does not match the approved contract")
            if row[3] != contract["rationale"]:
                failures.append(f"{decision_id}: rationale does not match the approved contract")
            if row[5] != expected_decision_evidence[decision_id]:
                failures.append(f"{decision_id}: consolidation evidence does not match the approved contract")
        target_list = re.findall(r"`([^`]+)`", row[4])
        targets = set(target_list)
        if len(target_list) != len(targets):
            failures.append(f"{decision_id}: duplicate named targets are forbidden")
        expected_targets = contract["targets"] if contract is not None else set()
        if targets != expected_targets:
            failures.append(f"{decision_id}: named target set mismatch {sorted(targets)}")
        if not row[5].strip() or any(marker in row[5].lower() for marker in ("pending", "n/a", "tbd")):
            failures.append(f"{decision_id}: consolidation evidence is required")
        for target in targets:
            if f"`{target}`" not in row[5]:
                failures.append(f"{decision_id}: evidence does not name target {target}")
            for assertion in expected_target_assertions.get(decision_id, {}).get(target, ()):
                if assertion not in target_text(target):
                    failures.append(f"{decision_id}: target {target} lacks consolidation assertion {assertion!r}")
    if len(seen_decisions) != len(set(seen_decisions)):
        failures.append("decision records: duplicate DEC IDs are forbidden")
    if set(seen_decisions) != set(expected_decisions):
        failures.append(f"decision records: ID set mismatch {sorted(set(seen_decisions))}")
    return failures

errors = validate_documents(backlog, lifecycle, feature_brief, decision_record)

probe_handoff = "[" + "`BLG-whatsflow-channel-attendance-study`" + "]" + "(" + "../../backlog/README.md" + ")"
mutated_brief = feature_brief.replace(probe_handoff, "`Selected-for-Planning`", 1)
if mutated_brief == feature_brief or not validate_documents(backlog, lifecycle, mutated_brief, decision_record):
    errors.append("fail-first probe: competing feature-brief state was accepted")
mutated_decisions = decision_record.replace("| DEC-roadmap-relative-horizons | Accepted |", "| DEC-roadmap-relative-horizons | Proposed |", 1)
if mutated_decisions == decision_record or not validate_documents(backlog, lifecycle, feature_brief, mutated_decisions):
    errors.append("fail-first probe: non-Accepted DEC state was accepted")
story_probe_row = next(line for line in feature_brief.splitlines() if line.startswith("| `ST-02` |"))
duplicate_story = feature_brief.replace(story_probe_row, story_probe_row + "\n" + story_probe_row, 1)
if not validate_documents(backlog, lifecycle, duplicate_story, decision_record):
    errors.append("fail-first probe: duplicate story row was accepted")
decision_probe_row = next(line for line in decision_record.splitlines() if line.startswith("| DEC-roadmap-relative-horizons |"))
duplicate_decision = decision_record.replace(decision_probe_row, decision_probe_row + "\n" + decision_probe_row, 1)
if not validate_documents(backlog, lifecycle, feature_brief, duplicate_decision):
    errors.append("fail-first probe: duplicate DEC row was accepted")
contradictory_row = decision_probe_row.replace("Preserve four strategic themes", "Replace all strategic themes")
contradictory_decision = decision_record.replace(decision_probe_row, decision_probe_row + "\n" + contradictory_row, 1)
if not validate_documents(backlog, lifecycle, feature_brief, contradictory_decision):
    errors.append("fail-first probe: contradictory duplicate DEC row was accepted")
direction_probe = decision_record.replace("Preserve four strategic themes and add orthogonal relative horizons.", "Replace all strategic themes with dated releases.", 1)
if direction_probe == decision_record or not validate_documents(backlog, lifecycle, feature_brief, direction_probe):
    errors.append("fail-first probe: in-place DEC direction mutation was accepted")
rationale_probe = decision_record.replace("Dates/releases were rejected as false commitments; unchanged phases were too ambiguous.", "Dates/releases are required commitments.", 1)
if rationale_probe == decision_record or not validate_documents(backlog, lifecycle, feature_brief, rationale_probe):
    errors.append("fail-first probe: in-place DEC rationale mutation was accepted")
state_variants = (
    "Selected&#45;for&#45;Planning",
    "Selected&shy;for&shy;Planning",
    "Selected&mdash;for&mdash;Planning",
    "Selected\u200d-for\u200d-Planning",
)
for state_variant in state_variants:
    notes_state_probe = feature_brief.replace("Dividir em oficial, não oficial e capacidades transversais", f"`{state_variant}`; dividir em oficial, não oficial e capacidades transversais", 1)
    if notes_state_probe == feature_brief or not validate_documents(backlog, lifecycle, notes_state_probe, decision_record):
        errors.append(f"fail-first probe: rendered candidate state in story Notes was accepted: {state_variant!r}")
    outside_table_probe = feature_brief.replace("## Source Idea / Request", f"Candidate state: `{state_variant}`\n\n## Source Idea / Request", 1)
    if outside_table_probe == feature_brief or not validate_documents(backlog, lifecycle, outside_table_probe, decision_record):
        errors.append(f"fail-first probe: rendered candidate state outside the story table was accepted: {state_variant!r}")
for candidate_state in candidate_states:
    first_component, separator, remainder = candidate_state.partition("-")
    insertion_point = max(1, len(first_component) // 2)
    state_variant = first_component[:insertion_point] + "&shy;" + first_component[insertion_point:] + (separator + remainder if separator else "")
    notes_state_probe = feature_brief.replace("Dividir em oficial, não oficial e capacidades transversais", f"`{state_variant}`; dividir em oficial, não oficial e capacidades transversais", 1)
    if notes_state_probe == feature_brief or not validate_documents(backlog, lifecycle, notes_state_probe, decision_record):
        errors.append(f"fail-first probe: in-token soft-hyphen state in story Notes was accepted: {candidate_state}")
    outside_table_probe = feature_brief.replace("## Source Idea / Request", f"Candidate state: `{state_variant}`\n\n## Source Idea / Request", 1)
    if outside_table_probe == feature_brief or not validate_documents(backlog, lifecycle, outside_table_probe, decision_record):
        errors.append(f"fail-first probe: in-token soft-hyphen state outside the story table was accepted: {candidate_state}")
duplicate_target_decision = decision_record.replace("| `system_roadmap.md` |", "| `system_roadmap.md`; `system_roadmap.md` |", 1)
if duplicate_target_decision == decision_record or not validate_documents(backlog, lifecycle, feature_brief, duplicate_target_decision):
    errors.append("fail-first probe: duplicate named DEC target was accepted")
roadmap_text = Path("foundation_documentation/system_roadmap.md").read_text(encoding="utf-8")
contradictory_roadmap = roadmap_text.replace("`Now`, `Next`, `Later`, and `Unscheduled` are relative planning horizons", "Dated releases are mandatory planning horizons", 1)
if contradictory_roadmap == roadmap_text or not validate_documents(backlog, lifecycle, feature_brief, decision_record, {"system_roadmap.md": contradictory_roadmap}):
    errors.append("fail-first probe: unconsolidated canonical target was accepted")
contradictory_evidence = decision_record.replace("`system_roadmap.md` contains the horizon rule and four theme rows.", "`system_roadmap.md` does not contain the horizon rule and four theme rows.", 1)
if contradictory_evidence == decision_record or not validate_documents(backlog, lifecycle, feature_brief, contradictory_evidence):
    errors.append("fail-first probe: contradictory target-consolidation evidence was accepted")
if errors:
    print("Contract validation failures:", *errors, sep="\n- ")
    sys.exit(1)
print("OK: IDs, candidate records, and lifecycle enums are coherent")
PY
```

Expected: exit `0` and exactly one final `OK` line; duplicate/missing candidate or decision, wrong disposition, malformed ID, absent enum, or competing feature-brief disposition exits `1`.

### VAL-04 — Negative Approval Fixture

```bash
set -euo pipefail
fixture="$(mktemp --suffix=.md)"
output="$(mktemp)"
trap 'rm -f "$fixture" "$output"' EXIT
sed -E \
  -e 's|^- \*\*Approved by:\*\*.*|- **Approved by:** `pending`|' \
  -e 's|^- \*\*Approval scope:\*\*.*|- **Approval scope:** `pending`|' \
  foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md > "$fixture"
set +e
python3 delphi-ai/tools/todo_authority_guard.py "$fixture" > "$output" 2>&1
rc=$?
set -e
test "$rc" -eq 2
rg -q 'APPROVAL-(EVIDENCE-MISSING|TOKEN-MISSING|SCOPE-MISSING)' "$output"
```

Expected: o guard interno retorna `2`, o output contém uma violação de aprovação e o wrapper retorna `0`; `trap` remove os dois fixtures em qualquer saída.

### VAL-08 — Tracked and Untracked Whitespace Integrity

```bash
set -euo pipefail
baseline='d8626df1fb0ff64751d7fae10ae93cf41ab1a458'
pathspecs=(
  README.md project_constitution.md evolution_lifecycle.md backlog decisions system_roadmap.md
  modules/README.md contracts/README.md artifacts/README.md
  artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md
  todos/README.md todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md
  todos/active/process/TODO-foundation-lifecycle-structural-validator.md
  todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md
)
git -C foundation_documentation diff --check "$baseline" -- "${pathspecs[@]}"
mapfile -t untracked_paths < <(git -C foundation_documentation ls-files --others --exclude-standard -- "${pathspecs[@]}")
for relative_path in "${untracked_paths[@]}"; do
  set +e
  output="$(git diff --no-index --check /dev/null "foundation_documentation/$relative_path" 2>&1)"
  rc=$?
  set -e
  if [ "$rc" -ne 1 ] || [ -n "$output" ]; then
    printf '%s\n' "$output" >&2
    exit 1
  fi
done
echo 'OK: tracked and untracked ST-01 files pass whitespace checks'
```

Expected: tracked diff retorna `0`; cada arquivo untracked retorna `1` sem output no probe `--no-index`; o wrapper retorna `0` e imprime a mensagem `OK`. Qualquer diagnóstico de whitespace ou erro bloqueia.

### VAL-10 — Scoped Secret Pattern Scan

```bash
set -euo pipefail
mapfile -t relative_paths < <({
  git -C foundation_documentation diff --name-only d8626df1fb0ff64751d7fae10ae93cf41ab1a458 -- \
    README.md project_constitution.md evolution_lifecycle.md backlog decisions system_roadmap.md \
    modules/README.md contracts/README.md artifacts/README.md \
    artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md \
    todos/README.md todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md \
    todos/active/process/TODO-foundation-lifecycle-structural-validator.md \
    todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md
  git -C foundation_documentation ls-files --others --exclude-standard -- \
    README.md project_constitution.md evolution_lifecycle.md backlog decisions system_roadmap.md \
    modules/README.md contracts/README.md artifacts/README.md \
    artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md \
    todos/README.md todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md \
    todos/active/process/TODO-foundation-lifecycle-structural-validator.md \
    todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md
} | sort -u)
test "${#relative_paths[@]}" -gt 0
scan_paths=()
for relative_path in "${relative_paths[@]}"; do
  test -f "foundation_documentation/$relative_path" && scan_paths+=("foundation_documentation/$relative_path")
done
test "${#scan_paths[@]}" -gt 0
secret_pattern="(?i)(?:api[_-]?key|client[_-]?secret|password)\s*[:=]\s*(?:\"[^\"]+\"|'[^']+'|[^\s#]+)|authorization\s*:\s*bearer\s+[^\s#]+|BEGIN [A-Z ]*PRIVATE KEY"
printf '%s%s\n' 'API_' 'KEY=sk_live_example' | rg -q --pcre2 "$secret_pattern"
printf '%s%s\n' 'API_' 'KEY="sk_live_example"' | rg -q --pcre2 "$secret_pattern"
set +e
output="$(rg -n --pcre2 "$secret_pattern" "${scan_paths[@]}" 2>&1)"
rc=$?
set -e
if [ "$rc" -eq 1 ]; then
  echo 'OK: no secret-like assignments or private keys in ST-01 paths'
elif [ "$rc" -eq 0 ]; then
  printf '%s\n' "$output"
  exit 1
else
  printf '%s\n' "$output" >&2
  exit "$rc"
fi
```

Expected: os probes quoted/unquoted retornam `0`; no scan real, `rg` exit `1` (nenhum match) é convertido em exit `0` com a mensagem `OK`; qualquer match ou erro bloqueia.

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| GitHub origin | baseline e publicação da autoridade `main` | healthy | 2026-09-18 | `git.exe fetch origin --prune` via Windows credential manager | usar Windows Git para push se WSL Git permanecer sem helper |

## Profile Scope & Handoffs

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `routine-executor` para a implementação documental pós-`APROVADO` e `assurance-tester-quality` para revisão independente; nenhum implementador de produto/runtime.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | routine-executor | implementar somente o pacote documental aprovado | paths esperados do ST-01 | authorized em 2026-09-21; principal checkout, single writer, sem worktrees |
| strategic-cto | assurance-tester-quality | crítica e revisão final independentes | TODO + diff documental limitado | completed; test-quality V3 e final-review revalidation sem finding material |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** `one checkpoint`
- **Why this level:** não muda runtime, mas estabelece governança transversal para roadmap, módulos, contratos, decisões, artifacts, backlog e TODOs.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/README.md`
- **Secondary module docs:** os quatro documentos atuais em `foundation_documentation/modules/` são anchors de preservação, não alvos de edição.
- **Planned decision promotion targets:** `evolution_lifecycle.md`, `system_roadmap.md`, `project_constitution.md`, `modules/README.md`, `contracts/README.md`.
- **Module decision consolidation targets:** seção de autoridade e schema futuro em `modules/README.md`; nenhum módulo individual é migrado neste TODO.

## Decision Validation

- [x] Usuário validou o escopo reduzido e as decisões `D-01..D-11` em 2026-09-18 com a resposta explícita `Valido`.
- [x] Usuário revalidou em 2026-09-21 as correções contratuais `ST01-R2-001..007` com a resposta explícita `valido`; `D-01..D-11` permanecem inalteradas.
- [x] Usuário revalidou em 2026-09-21 as correções contratuais `ST01-R3-001..006` com a resposta explícita `Valido`; `D-01..D-11` permanecem inalteradas.
- [x] Usuário revalidou em 2026-09-21 as correções contratuais `ST01-R4-001..003` com a resposta explícita `valido`; `D-01..D-11` permanecem inalteradas.
- [x] Usuário renovou a validação e a autoridade de continuação em 2026-09-21 com `APROVADO para continuar`, após receber o estado `Local-Implemented`, as correções `ST01-ADR`, `ST01-TQA/CUT` e os gates restantes; `D-01..D-11` e o escopo documental permanecem inalterados.

## Decision Baseline (Frozen Before Implementation)

User-validated on 2026-09-18, revalidated after the R2, R3 and R4 contract corrections on 2026-09-21, and explicitly approved for execution on 2026-09-21.

- [x] `D-01` Preservar as quatro fases atuais como temas estratégicos e usar horizonte ortogonal `Now|Next|Later|Unscheduled`; horizonte não representa prazo, e datas/releases exigem aprovação explícita. Ref: `system_roadmap.md`.
- [x] `D-02` Criar `foundation_documentation/backlog/` para candidatos não aprovados. `todos/active/` contém contratos táticos vivos em `Draft|Review|Approved|In-Progress`; estar na pasta nunca concede execução, que exige `APROVADO` explícito e authority guard `go`. Ref: constituição `TODO governance`.
- [x] `D-03` Manter `artifacts/feature-briefs/` como evidência de descoberta não autoritativa e, após handoff, somente com link para o registro vivo; briefs não duplicam estado operacional. Ref: feature brief ST-01.
- [x] `D-04` Definir máquinas ortogonais: candidato `Proposed|Under-Review|Selected-for-Planning|Deferred|Rejected`; capacidade `Not-Assessed|Discovery|Planned|In-Progress|Delivered|Retired`; TODO `Draft|Review|Approved|In-Progress|Completed|Cancelled`; decisão `Proposed|Accepted|Superseded|Rejected`; contrato `Not-Assessed|Documented|Verified|Deprecated`. `Blocked` é qualifier com razão, owner e estado anterior, nunca estado destrutivo.
- [x] `D-05` Registrar decisões duráveis em `decisions/` como racional/proveniência. Uma decisão `Accepted` só é efetiva depois que seus alvos canônicos nomeados são consolidados; constituição/módulos mantêm a verdade corrente.
- [x] `D-06` Adotar owner único por campo: backlog possui disposição e próximo gate; roadmap possui tema, horizonte, resultado, dependências e exit gate; módulos possuem ownership, invariantes, capacidades estáveis e contratos locais; TODO possui aprovação/execução/evidência; decisions possui racional/histórico; lifecycle possui schemas/transições; contracts README é índice; briefs são evidência.
- [x] `D-07` Não retroajustar artifacts/TODOs concluídos nem os três TODOs ativos alheios ao ST-01. A estrutura passa a reger registros novos; um TODO legado só adota o novo schema quando receber futura alteração material autorizada. Documentos históricos mantêm marcador de contexto e ficam fora dos validadores correntes.
- [x] `D-08` Registrar ST-02 e ST-03 como `Selected-for-Planning` com gate após ST-01; registrar ST-04 como `Deferred` até conclusão dos ST-02/ST-03. Nenhum recebe TODO ativo neste escopo.
- [x] `D-09` Não criar validator permanente neste TODO. Strategic é owner do follow-up; abrir TODO próprio quando houver mais de dez registros vivos somados em backlog/decisions/roadmap ou na primeira recorrência comprovada de drift de schema/autoridade. Até lá, usar checks exatos e reproduzíveis deste TODO.
- [x] `D-10` Usar IDs imutáveis baseados em namespace e slug (`BLG-<slug>`, `DEC-<slug>`, `CAP-<slug>`); títulos e filenames podem mudar, mas o ID e os links de supersessão permanecem.
- [x] `D-11` Definir papéis provider-neutral: human decision authority, strategic steward, module owner, TODO owner/executor e assurance reviewer. Ferramentas/agentes concretos são adapters da política de engenharia, não autoridade de produto.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `modules/README#ownership` | módulos possuem workflows, contratos, APIs e data shapes locais | Preserve | `modules/README.md` |
| `identity-and-tenancy#invariants` | tenant por request, permissão na BU, roles atuais | Preserve | `modules/identity-and-tenancy.md` |
| `inbox-and-conversations#invariants` | conversa por BU/contato, idempotência, capacidade do canal | Preserve | `modules/inbox-and-conversations.md` |
| `audit-and-history#invariants` | histórico persistente, tenant/BU scoped, leitura separada de escrita | Preserve | `modules/audit-and-history.md` |
| `integrations-and-channels#invariants` | providers são adapters, segredos não vazam, erros determinísticos | Preserve | `modules/integrations-and-channels.md` |

## Module Coherence Gate

- **Status:** `no_material_findings`
- **Checked against:** `project_constitution.md`, `system_roadmap.md`, `modules/README.md` e os quatro módulos individuais em 2026-09-18.
- **Evidence:** os quatro módulos individuais permanecem sem diff desde `d8626df1fb0ff64751d7fae10ae93cf41ab1a458`; suas invariantes são preservadas. A frase atual da constituição que associa `todos/active/` à autoridade de execução é a ambiguidade intencionalmente aposentada por `D-02`, não uma decisão de módulo silenciosamente superseded.
- **Outcome:** a architecture opinion R2 permaneceu limpa; a correção do contrato de validação não altera invariantes de módulo e foi revalidada pelo usuário em 2026-09-21.

## Decision Freeze Evidence

- [x] `D-01` a `D-11` formam o baseline de decisão validado pelo usuário em 2026-09-18; qualquer mudança material exige nova validação e futuro `APROVADO` renovado.
- [x] `ST01-R2-001..007` foram integradas sem alterar `D-01..D-11` e revalidadas pelo usuário em 2026-09-21 (`valido`).
- [x] `ST01-R3-001..006` foram integradas sem alterar `D-01..D-11` e revalidadas pelo usuário em 2026-09-21 (`Valido`).
- [x] `ST01-R4-001..003` foram integradas sem alterar `D-01..D-11` e revalidadas pelo usuário em 2026-09-21 (`valido`).

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
| guard | tactical contract files | `todo_authority_guard.py`, `todo_completion_guard.py` | execução/closeout sem autoridade/evidência | already-enforced | registrar stdout, exit code e timestamp na Completion Evidence Matrix antes do closeout |
| audit | Foundation | resolved-link, IDs/enums e positive/negative traceability checks | links, estados e transições inconsistentes | manual-only-with-rationale | comandos exatos neste TODO; follow-up automático pelo gatilho D-09 |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `no_material_findings`
- **Decision review evidence / resolution:** reviewer inicial `/root/st01_architecture_review` produziu ST01-ARCH-001..007, todos integrados; após o freeze `accdd4057d6dbd1b1bfc9fcb005f60aacd3f2e0c`, o primeiro dispatch V2 terminou objetivamente por limite de uso e o único retry permitido `/root/st01_architecture_review_v2_retry` concluiu em 2026-09-21 com `no_material_findings`, recomendando preservar D-01..D-11 sem alteração.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `no_material_findings`
- **Adherence review evidence / resolution:** a primeira lane encontrou `ST01-ADR-001..004`, todos integrados; a revalidação fresh/no-context `/root/st01_adherence_revalidation` confirmou em 2026-09-21 que D-01..D-11 permanecem aderentes, owner singular é determinístico, módulos individuais estão intactos e não há novo finding material.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** o TODO é `medium`, transversal e estabelece arquitetura documental.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `foundation_documentation/main`
- **Baseline commit:** `ad6a0cc8475bc412fd1b767e9cc19ad0123fb6fe`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** o pacote completo, incluindo auditorias, final review e follow-up D-09, foi congelado no commit de implementação publicado antes do closeout.
- **Evidence / reference:** freezes históricos `565ff17a81a6faa663f9e024e9784e396cd50bfe`, `accdd4057d6dbd1b1bfc9fcb005f60aacd3f2e0c`, `956b26d8ba5b5bc0a64d07f59e82129d63d5452a`, `075a91efc49481780044fd3d3feb35912598aa0d` e `17ced7b867aaa6e73650f3726f7b20b513dd7ddd`; freeze de entrega vigente `ad6a0cc8475bc412fd1b767e9cc19ad0123fb6fe`, publicado em `origin/main` em 2026-09-23.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** o diff final deve permanecer no ST-01 documental.
- **Trigger stage:** `after planning review converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** o baseline foi atualizado para o pacote publicado; nenhum dos 22 blocos materiais mudou entre `ad6a0cc8` e o estado de closeout.
- **Evidence / reference:** `review_scope_drift_guard.py` em 2026-09-23: `Overall outcome: go`, baseline `foundation_documentation/main@ad6a0cc8475bc412fd1b767e9cc19ad0123fb6fe`, `Changed material sections: 0`.
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] Usuário validou o escopo reduzido e `D-01..D-11` em 2026-09-18 (`Valido`).
- [x] `AMB-03`: fases são temas; horizonte é `Now|Next|Later|Unscheduled`, sem datas implícitas (`D-01`).
- [x] `AMB-04`: adotar `foundation_documentation/backlog/` fora de `todos/active/` (`D-02`).
- [x] Usuário revalidou em 2026-09-21 o contrato corrigido após `ST01-R2-001..007`, sem mudança nas decisões `D-01..D-11` (`valido`).
- [x] `AMB-05`: diferida para o framing de ST-03 ou TODO próprio; ST-01 não altera `policies/**` nem autoriza uso acoplado/cópia de `whatsflow_v2`.
- [x] Usuário revalidou em 2026-09-21 as correções `ST01-R3-001..006`, sem mudança em `D-01..D-11` (`Valido`).
- [x] Usuário revalidou em 2026-09-21 as correções `ST01-R4-001..003`, sem mudança em `D-01..D-11` (`valido`).

## Assumptions Preview

| Assumption ID | Assumption | Confidence | Validation / Handling |
| --- | --- | --- | --- |
| `n/a` | Nenhuma premissa viva; o escopo depende somente de constraints e decisões validadas abaixo. | high | placeholder intencional para o guard; nenhuma implementação pode depender desta linha |

## Confirmed Constraints (No Live Assumptions)

| Constraint ID | Constraint | Evidence | Handling |
| --- | --- | --- | --- |
| `C-01` | Foundation é a autoridade de produto/governança. | `README.md`, constituição | preserve |
| `C-02` | As quatro fases atuais serão preservadas por decisão de escopo, não por inferência de validade completa. | `D-01` | frozen after user validation |
| `C-03` | Os quatro módulos atuais e seu conteúdo permanecem inalterados neste recorte. | Out of Scope + Diff Expectation Contract | preserve |
| `C-04` | Datas não entram sem aprovação explícita. | `D-01` | frozen after user validation |
| `C-05` | A política de referência para `whatsflow_v2` não muda no ST-01; `AMB-05` deve ser resolvida no framing de ST-03 ou TODO próprio antes do estudo. | feature brief `AMB-05` + Out of Scope | defer explicitly; no copy/coupling authority |

## Execution Plan

### Touched Surfaces

- Authority/navigation: `README.md`, `project_constitution.md`, `evolution_lifecycle.md`.
- Planning: `system_roadmap.md`, `backlog/`, `decisions/`.
- Local contracts: `modules/README.md`, `contracts/README.md`; módulos individuais são observe-only.
- Evidence/execution: `artifacts/README.md`, feature brief, `todos/README.md`, este TODO.

### Ordered Steps

1. Revalidação concluída em 2026-09-21 para as correções contratuais `ST01-R4-001..003`; `D-01..D-11` permanecem conceitualmente inalteradas.
2. Congelar/publicar novo baseline e repetir a crítica fresh/no-context com `README.md` incluído; repetir architecture opinion somente se alguma decisão arquitetural mudar.
3. Rodar coherence/scope-drift/pre-approval guards e solicitar `APROVADO`; `preflight-go` não concede execução.
4. Após `APROVADO`, registrar aprovação/ingestão e executar `todo_authority_guard.py <todo>` sem `--pre-approval`; exigir `Overall outcome: go` antes de qualquer alteração canônica.
5. Implementar authority matrix, papéis, state machines e lifecycle central.
6. Implementar backlog, decisions, roadmap e navegação sem duplicar estado vivo.
7. Atualizar somente `modules/README.md` e `contracts/README.md`; preservar módulos individuais.
8. Registrar ST-02/ST-03/ST-04 com as disposições D-08 e validar cenários positivo/negativo.
9. Executar validações, decision/module adherence, auditorias, revisão final e closeout.

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

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundation context readiness | links e contexto Delphi governam todos os documentos tocados | `bash delphi-ai/tools/verify_context.sh` | Local-Implemented | passed | exit `0`; `Environment Verified: PACED-Ready.` em 2026-09-21 | verificador canônico executado no checkout principal |
| Foundation Markdown integrity | todo o pacote é Markdown versionado | `git -C foundation_documentation diff --check HEAD` | Local-Implemented | passed | exit `0` sem output | cobre working tree, inclusive arquivos adicionados após staging final |
| Foundation links and schemas | navegação, IDs, enums e ownership mudaram | executar os contratos exatos VAL-01 e VAL-02 | Local-Implemented | passed | ambos retornaram exit `0` e suas mensagens `OK` | inclui feature brief, backlog, decisions e lifecycle |
| Foundation boundary safety | pacote deve preservar paths, whitespace, hashes e segredos | executar VAL-05, VAL-08, VAL-09 e VAL-10 | Local-Implemented | passed | cada contrato retornou seu resultado satisfatório | nenhum produto/runtime ou módulo individual foi alterado |
| Product/runtime pipeline jobs | nenhum código, runtime, teste de produto, build ou deploy pertence ao diff aprovado | `n/a` | Production-Ready | n/a | diff expectation guard e lista de paths ST-01 | não existe job de aplicação em escopo para esta entrega documental |

Este recorte não possui job de produto/runtime: a matriz é a prova local completa da mudança documental no checkout principal, sem alegar paridade com uma pipeline de aplicação inexistente neste escopo.

### Runtime / Rollout Notes

- Nenhum runtime, deploy, migration ou browser flow é afetado.
- A publicação é a atualização governada de `foundation_documentation/main`.

## Plan Review Gate

- **Status:** `no_material_findings`; correções R4 revalidadas/congeladas e crítica V5 limpa.

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
- **Evidence:** `foundation_documentation/system_roadmap.md:4` inicia as quatro fases; até `:22` não há estado, dependência ou exit gate.
- **Why now:** os próximos estudos precisam de um local previsível sem falsa promessa de data.
- **Recommendation:** B (`D-01`); melhor equilíbrio entre clareza, manutenção, elegância e risco.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — quarters/releases | medium | high: datas fictícias | roadmap | recurring date churn | neutral | medium | low without delivery evidence |
| B — temas + horizontes | medium | low | roadmap + backlog links | low | neutral | high | high: dimensões ortogonais |
| C — manter fases | none | high: baixa previsibilidade | roadmap consumers | high manual interpretation | neutral | low | low |

#### PR-02 — Local do backlog

- **Severity:** medium
- **Evidence:** `foundation_documentation/project_constitution.md:38` cita `backlog/`; `foundation_documentation/todos/README.md:7` cita `todos/active/backlog/`; nenhum dos caminhos existe no baseline.
- **Why now:** os estudos ST-02/ST-03 precisam de uma disposição viva e não autorizativa assim que ST-01 encerrar.
- **Recommendation:** B (`D-02`); menor acoplamento e melhor coerência estrutural.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — `todos/active/backlog` | low | high: confunde autoridade | TODO governance | medium | neutral | low | low |
| B — `backlog/` separado | medium | low | navigation + governance | low | neutral | high | high: boundary explícita |
| C — não criar backlog | none | high: candidatos sem disposição viva | artifacts + planning | high manual triage | neutral | low | low |

#### PR-03 — Automação de proteção

- **Severity:** low
- **Evidence:** `delphi-ai/tools/manifest.md:1` é o inventário canônico de tooling e o baseline Foundation contém apenas `foundation_documentation/deterministic/.gitkeep:1`, sem validator documental próprio.
- **Why now:** o ST-01 precisa de checks reproduzíveis, mas o volume e a recorrência ainda não justificam uma ferramenta permanente.
- **Recommendation:** B (`D-09`), com owner e gatilho mensurável para validator permanente.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — validator agora | high | medium: escopo prematuro | Foundation + Delphi tooling | high | negligible runtime | medium | medium until schema stabilizes |
| B — checks exatos + gatilho | low | low | ST-01 only | low until trigger | neutral | high | high: proportional control |
| C — não adicionar controle | none | high: drift não detectado | review process | high manual recovery | neutral | low | low |

#### PR-04 — Contrato vivo versus execução aprovada

- **Severity:** high
- **Evidence:** `delphi-ai/workflows/docker/todo-driven-execution-method.md:30` exige aguardar `APROVADO`, e `:38` proíbe implementação anterior à aprovação.
- **Why now:** tratar localização como aprovação tornaria o próprio processo circular.
- **Recommendation:** B (`D-02`); separa estado documental de autoridade de execução.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — `active = approved` | low | critical: circular | every TODO | low but unsafe | neutral | low | invalid against workflow |
| B — active vivo + gate | medium | low | TODO governance | low | neutral | high | high: state/authority separated |
| C — nova árvore `draft/` | high | medium: tooling drift | paths + guards | high | neutral | medium-low | medium |

#### PR-05 — Owner dos campos vivos

- **Severity:** high
- **Evidence:** `foundation_documentation/modules/README.md:3` já atribui contratos/workflows locais aos módulos, enquanto `foundation_documentation/system_roadmap.md:22` separa roadmap de autoridade de implementação; duplicar campos vivos entre essas superfícies violaria ambos os limites.
- **Why now:** sincronização N-way destruiria previsibilidade e aumentaria custo operacional.
- **Recommendation:** B (`D-06`); maior elegância e solidez estrutural.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — duplicar campos | low initially | high: drift N-way | all planning docs | high | neutral | low | low |
| B — owner único + links | medium | low | all planning docs | low | neutral | high | high |
| C — arquivo central único | high migration | medium: perde boundaries | whole Foundation | medium-high | neutral | medium | low-medium |

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
- **Confidence:** high; decisões D-01..D-11 e correções R3/R4 reconvergiram sem findings materiais na V5.

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** governança transversal exige crítica externa sobre complexidade acidental e autoridade duplicada.
- **Opinion count:** `2 completed; initial corrective review + freeze-backed clean rerun`
- **Package mode:** `bounded-file-set`
- **Internal reviewer mandate:** `required; fresh no-context reviewer after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `/root/st01_architecture_review` | corrigir autoridade, owners, transições, papéis e proteção | runtime neutro; evitar sincronização N-way | owner único + IDs/links | máquinas ortogonais antes de aprovação | Integrated; clean rerun completed | findings `ST01-ARCH-001..007` |
| `/root/st01_architecture_review_v2_retry` | preservar D-01..D-11 e seguir para crítica/coherence/scope-drift/preflight | acceptable; runtime-neutral | strong | sound | `no_material_findings` | freeze-backed review em 2026-09-21; primeiro dispatch V2 falhou terminalmente por limite de uso |

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Latest TEACH evidence / artifact:** guard `go` em 2026-09-21, fingerprint `75992daf3f8f`; critique `required/expanded`, test-quality `recommended/full`, final review `required/expanded`, verification debt `required`, architecture decision/adherence reviews `required`, demais lanes `not_needed`.

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
- **Package minimum contents:** feature brief, TODO congelado e todos os documentos canônicos tocados, incluindo explicitamente `foundation_documentation/README.md`.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after freeze; reviewer cannot implement`
- **Canonical multi-lane audit protocol:** `n/a`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `no_material_findings`
- **Findings summary:** V5 confirmou D-01..D-11, R3/R4, commands, promotion ledger, baseline e riscos sem finding material; updates futuros somente de evidência não reabrem a crítica salvo drift material.
- **Evidence / reference:** reviewers `/root/st01_plan_critique` (`ST01-R01..R08`), `/root/st01_plan_critique_v2` (`ST01-R2-001..007`), `/root/st01_plan_critique_v3` (`ST01-R3-001..006`), `/root/st01_plan_critique_v4` (`ST01-R4-001..003`) e `/root/st01_plan_critique_v5` (`no_material_findings`, 2026-09-21).
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
| `ST01-R2-001` | Integrated | useful | yes | project | `Review Baseline Freeze` | ref real `origin/main`, status canônico e narrativas sincronizadas |
| `ST01-R2-002` | Integrated | useful | yes | paced | `Assumptions Preview` | heading parseável com placeholder `n/a`; constraints seguem separadas |
| `ST01-R2-003` | Integrated | useful | yes | paced | `Rules Acknowledgement / Agent Routing` | paths concretos, tuple de implementação e guards de git explícitos |
| `ST01-R2-004` | Integrated | useful | yes | project | `Critique package` | `foundation_documentation/README.md` incluído explicitamente |
| `ST01-R2-005` | Integrated | useful | yes | project | `Exact Check Command Contracts` | cwd, fixtures, exits e outputs definidos para VAL-01/02/04/08/10 |
| `ST01-R2-006` | Integrated | useful | yes | project | `Plan Review Issue Cards` | file:line e matrizes A/B/C completas |
| `ST01-R2-007` | Challenged | useful | yes | paced | `pcv-1 negative-reason gap` | o schema `pcv-1` vigente aceita `n/a` explícito para lanes não aplicáveis; não há defeito deste pacote nem follow-up de projeto a abrir |
| `ST01-R3-001` | Integrated | useful | yes | project | `C-05 / AMB-05` | ambiguidade explicitamente diferida para ST-03 ou TODO próprio; policy fora do ST-01 |
| `ST01-R3-002` | Integrated | useful | partial | project | `Review lifecycle state` | narrativas sincronizadas para revalidação → refreeze → crítica |
| `ST01-R3-003` | Integrated | useful | yes | paced | `Plan Review Issue Cards` | `Why now` e opção C do-nothing adicionados a PR-02/PR-03 |
| `ST01-R3-004` | Integrated | useful | yes | paced | `Agent Routing Preflight` | reviewer e executor desacoplados; delegação futura marcada `not-requested` |
| `ST01-R3-005` | Integrated | useful | yes | paced | `pcv-1 registries` | deadlines e minimum evidence IDs canônicos restaurados |
| `ST01-R3-006` | Integrated | useful | yes | paced | `VAL-10` | scan aceita secrets quoted/unquoted e inclui probes fail-first |
| `ST01-R4-001` | Integrated | useful | yes | paced | `Post-approval authority gate` | guard normal `go` inserido entre `APROVADO` e implementação; distinto de `preflight-go` |
| `ST01-R4-002` | Integrated | useful | yes | paced | `VAL-01/08/10` | descoberta usa união tracked + untracked; whitespace de novos arquivos possui probe próprio |
| `ST01-R4-003` | Integrated | useful | yes | project | `Review lifecycle state` | narrativas sincronizadas para revalidação → refreeze → crítica |
| `ST01-ADR-001` | Integrated | useful | yes | project | `D-01,D-04,D-06` | roadmap usa `Open|Exit-Gate-Met` somente como sinal derivado do exit gate e não projeta capability state |
| `ST01-ADR-002` | Integrated | useful | yes | project | `D-02,D-04` | TODO registra lifecycle state `In-Progress`, owner e crosswalk com work state de assurance |
| `ST01-ADR-003` | Integrated | useful | yes | project | `D-03,D-06` | feature brief removeu cópias de disposições vivas e mantém links canônicos |
| `ST01-ADR-004` | Integrated | useful | yes | project | `D-05` | constituição e decisions tornam eficácia dependente da consolidação dos targets |
| `ST01-TQA-001` | Integrated | useful | yes | project | `VAL-02,D-03,D-06` | story table usa links BLG e VAL-02 falha se o brief reintroduzir decisão concorrente |
| `ST01-CUT-001` | Integrated | useful | yes | paced | `Local CI-Equivalent Suite Matrix` | matriz adota sete colunas canônicas com comandos e evidência concreta |
| `ST01-CUT-002` | Integrated | useful | yes | paced | `Completion Evidence Matrix` | cada item de Scope, DOD e VAL possui linha com texto exato e evidência própria |
| `ST01-CUT-003` | Integrated | useful | yes | project | `D-03` | mesma resolução de ADR-003, incluindo cabeçalho e sequência histórica do brief |
| `ST01-CUT-004` | Integrated | useful | yes | project | `D-05` | onze registros `DEC-*` preservam alternativas, proveniência, targets e consolidação |
| `ST01-CUT-005` | Integrated | useful | yes | project | `D-01,D-04,D-06` | mesma resolução de ADR-001 sem criar sexta máquina lifecycle |
| `ST01-CUT-006` | Integrated | useful | yes | paced | `Delivery Status Canon` | estágio alinhado para `Local-Implemented` no canon e no PCV |
| `ST01-TQAR-001` | Integrated | useful | yes | project | `VAL-02` | validator agora parseia handoffs/DEC rows, exige target sets e evidence e executa dois mutation probes fail-closed |
| `ST01-TQAR-002` | Integrated | useful | yes | paced | `delivery gates` | matriz 1-1 confirmada; heurísticas estruturais reconciliadas e gates restantes mantidos visíveis até execução |
| `ST01-CUTR-001` | Integrated | useful | yes | project | `DEC-single-field-authority` | categoria aberta substituída por sete paths explícitos com evidência por target e check determinístico |
| `ST01-TQAF-001` | Integrated | useful | yes | project | `VAL-02 uniqueness` | exige cardinalidade exata, IDs únicos e três probes fail-closed de duplicação/contradição |
| `ST01-CUTF-001` | Integrated | useful | yes | paced | `staged package integrity` | allowlist completo restageado; working tree e index idênticos; cached check e VAL-01/02 verdes |
| `ST01-TQAU-001` | Integrated | useful | yes | project | `VAL-02 brief-wide state exclusion` | candidate-state scan cobre todo o brief; probes Notes e outside-table falham fechado |
| `ST01-TQFINAL-001` | Integrated | useful | yes | project | `VAL-02 decision-content contract` | direction e rationale de cada DEC agora são comparados exatamente ao baseline aprovado; probes in-place falham fechado |
| `ST01-TQFINAL-002` | Integrated | useful | yes | project | `VAL-02 rendered-state normalization` | scan do brief normaliza entidades HTML e variantes Unicode de hífen; probes em Notes e fora da tabela falham fechado |
| `ST01-TQFINALR-001` | Integrated | useful | yes | project | `VAL-02 Unicode normalization` | NFKC, categorias Unicode `Pd`, soft hyphen, minus e caracteres de formato são normalizados; quatro variantes são testadas em dois loci |
| `ST01-TQFINALR-002` | Integrated | useful | yes | project | `VAL-02 target consolidation` | evidência DEC é exata e assertions específicas são verificadas dentro de cada alvo canônico; probes contradizem target e evidence |
| `ST01-TQFINALV2-001` | Integrated | useful | yes | project | `VAL-02 soft-hyphen dual normalization` | soft hyphen é testado tanto como invisível quanto como hífen discricionário; os cinco estados possuem probes em Notes e fora da tabela |
| `ST01-TQFINALV2-002` | Integrated | useful | yes | project | `VAL-02 target uniqueness` | lista e set de targets mantêm cardinalidade explícita; target repetido falha antes da consolidação |
| `ST01-FINAL-001` | Integrated | useful | yes | project | `D-09 validator trigger` | o limiar de 18 registros foi reconhecido; follow-up separado aberto em Review e consolidado como target, sem implementar o validator |
| `ST01-FINAL-002` | Integrated | useful | yes | paced | `TODO Closeout Disposition` | ação stale substituída pela sequência real de revalidação final, VAL-07/11, guards, publicação e closeout |

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `ST01-R2-001..006` | high/medium | `release-blocker` | integrate in ST-01 | execução dos gates dependia das correções | resolved | resolution rows acima + revalidação R2 |
| `ST01-R2-007` | medium | `by-design/no-action` | preserve explicit `n/a` under current pcv-1 | o schema vigente não exige reason code negativo e o pacote é docs-only | resolved | finding challenged against the approved pcv-1 contract; no project follow-up required |
| `ST01-R3-001..006` | high/medium | `release-blocker` | integrate in ST-01 | traceabilidade, schema e validação pertencem ao contrato atual | resolved | resolution rows acima + revalidação R3 |
| `ST01-R4-001` | high | `release-blocker` | integrate in ST-01 | authority pós-aprovação é pré-condição da execução atual | resolved | Execution Plan + VAL-07 + Commands + revalidação R4 |
| `ST01-R4-002` | high | `release-blocker` | integrate in ST-01 | falso verde invalidaria a evidência deste pacote | resolved | VAL-01/08/10 exact contracts + revalidação R4 |
| `ST01-R4-003` | medium | `release-blocker` | integrate in ST-01 | estado operacional precisa permanecer inequívoco | resolved | lifecycle status fields + revalidação R4 |
| `ST01-ADR-001..004` | high | `release-blocker` | integrate in ST-01 | findings atingiam owner único, estado lifecycle e eficácia de decisões | resolved | resolution rows e superfícies canônicas corrigidas; revalidação requerida |
| `ST01-TQA-001` | high | `release-blocker` | integrate in ST-01 | VAL-02 não detectava decisão concorrente no feature brief | resolved | story handoff por BLG + assertion fail-closed em VAL-02 |
| `ST01-CUT-001..006` | high | `release-blocker` | integrate in ST-01 | evidência/CI, decisões, roadmap, brief e delivery status bloqueavam closeout | resolved | matrices canônicas, DEC records, gate status e `Local-Implemented`; revalidação requerida |
| `ST01-TQAR-001` | high | `release-blocker` | integrate in ST-01 | mutation probes provaram que VAL-02 aceitava drift semântico equivalente | resolved | structural parser, exact target maps e fail-first mutations em VAL-02 |
| `ST01-TQAR-002` | medium | `release-blocker` | finish current gates | dívida correspondia aos gates abertos, sem novo defeito de conteúdo | resolved | test-quality/final review concluídos; authority/diff/closeout `go` e completion entra no rerun self-referential final |
| `ST01-CUTR-001` | medium/P2 | `release-blocker` | integrate in ST-01 | target aberto tornava eficácia de DEC não determinística | resolved | paths/evidence explícitos + VAL-02 structural target check |
| `ST01-TQAF-001` | high | `release-blocker` | integrate in ST-01 | sets validavam membership, mas não cardinalidade/uniqueness | resolved | exact row counts, duplicate-ID rejection e mutation probes em VAL-02 |
| `ST01-CUTF-001` | high/P1 | `release-blocker` | integrate in ST-01 | index staged antigo não representava o pacote auditado | resolved | full explicit restage; `git diff --quiet`, cached diff check e VAL-01/02 exit `0` |
| `ST01-TQAU-001` | high | `release-blocker` | integrate in ST-01 | scan limitado ao handoff permitia estado concorrente em outras células/texto | resolved | brief-wide candidate-state exclusion + Notes/outside-table mutation probes |
| `ST01-TQFINAL-001` | high | `release-blocker` | integrate in ST-01 | o contrato aceitava mutação in-place de direction/rationale de uma DEC | resolved | exact decision-content contract + two in-place mutation probes in VAL-02 |
| `ST01-TQFINAL-002` | high | `release-blocker` | integrate in ST-01 | entidades HTML podiam ocultar estado concorrente no feature brief | resolved | HTML/unicode normalization + encoded-state probes in VAL-02 |
| `ST01-TQFINALR-001` | high | `release-blocker` | integrate in ST-01 | soft hyphen, em dash e format controls ainda ocultavam estado concorrente | resolved | Unicode category normalization + Notes/outside-table variant matrix in VAL-02 |
| `ST01-TQFINALR-002` | high | `release-blocker` | integrate in ST-01 | nomes/evidência textual não provavam consolidação real nos targets | resolved | exact evidence + per-target assertions + contradictory target/evidence probes in VAL-02 |
| `ST01-TQFINALV2-001` | high | `release-blocker` | integrate in ST-01 | soft hyphen inserido dentro de estado sem hífen ainda passava | resolved | dual soft-hyphen normalization + 5-state/2-locus probe matrix in VAL-02 |
| `ST01-TQFINALV2-002` | medium | `release-blocker` | integrate in ST-01 | conversão direta para set ocultava target DEC duplicado | resolved | target-list cardinality check + duplicate-target fail-first probe in VAL-02 |
| `ST01-FINAL-001` | medium/P2 | `release-blocker` | integrate in ST-01 | D-09 já havia disparado com 18 registros sem follow-up próprio | resolved | `TODO-foundation-lifecycle-structural-validator.md` aberto em Review; lifecycle, DEC target, adherence, DOD-12 e debt reconciliados |
| `ST01-FINAL-002` | medium/P2 | `release-blocker` | integrate in ST-01 | ação de closeout apontava para lanes já concluídas | resolved | Next path/status action atualizado para os gates realmente restantes |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** o primeiro review encontrou assumptions inadequadas; após promovê-las para constraints/decisions, o guard deve confirmar que nenhuma assumption viva permanece.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `none; verify no live Assumptions Preview rows remain`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** zero premissas vivas; `AMB-05` foi diferida explicitamente em C-05 e a crítica V5 não encontrou incoerência.
- **Evidence / reference:** `assumption_code_coherence_guard.py` em 2026-09-21: `Overall outcome: go`; `Live assumptions checked: 0`; decisão/status `required / no_material_findings`.
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** usuário em 2026-09-21, com a resposta explícita `APROVADO — incluindo delegação da implementação documental ao routine-executor, no checkout principal, single-writer, sem worktrees.`
- **Approval scope:** implementar exclusivamente o pacote documental ST-01 descrito em `Scope`, conforme `D-01..D-11`, por `routine-executor` no checkout principal, em regime single-writer e sem worktrees/branches/checkouts auxiliares.
- **Pre-approval authority evidence:** `todo_authority_guard.py --pre-approval` em 2026-09-21: `Overall outcome: preflight-go`, sem violações; esse resultado não concede execução.
- **Execution not authorized by approval:** código/produto/referências, execução de ST-02/ST-03/ST-04, migração dos módulos individuais e mudanças de domínio.
- **Renewed approval required when:** qualquer decisão D-01..D-11, escopo, validator, contrato de produto ou arquivo esperado mudar materialmente.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/main_instructions.md` | autoridade e Foundation main-only | documentação antes de código | branch/worktree paralelo | freeze/push canônico |
| `delphi-ai/rules/core/core-instructions-always-on.md` | disciplina geral | hierarquia e segurança | atalhos de workflow | gates obrigatórios |
| `delphi-ai/rules/core/project-mandate-always-on.md` | mandato e core docs | propósito/invariantes | drift de produto | revisão 1-1 |
| `delphi-ai/rules/core/foundation-docs-sync-model-decision.md` | sincronização Foundation | roadmap/módulos coerentes | side notes concorrentes | consolidação canônica |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | decisão de governança do TODO | fases e autoridade explícita | implementação pré-APROVADO | execução governada |
| `delphi-ai/rules/core/audit-escalation-model-decision.md` | piso de auditoria | lanes derivadas pelo guard | seleção subjetiva | gates proporcionais |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | entrega governada | TODO, aprovação, evidência | implementação pré-APROVADO | execução por fases |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | fase atual | freeze, crítica, scope drift e preflight | pedir aprovação cedo | sequência pré-APROVADO |
| `delphi-ai/workflows/docker/todo-execution-boundary-method.md` | próxima fase | boundary após aprovação | implementação implícita | handoff explícito |
| `delphi-ai/workflows/docker/effort-selection-method.md` | seleção de effort/model | routing conforme superfície | reviewer como writer | tuple verificável |
| `delphi-ai/workflows/docker/subagent-orchestration-method.md` | delegação aprovada | executor único no checkout principal | worktree ou writers concorrentes | handoff delimitado e serializado |

- **Binding ingestion evidence:** fontes acima recarregadas após o `APROVADO` em 2026-09-21; nenhuma regra revelou conflito material com o escopo aprovado.

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Routing lifecycle note:** tuple planejado para a lane pós-`APROVADO`; não concede autoridade antes da aprovação explícita.
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `approved`
- **Delegation note:** autorização humana explícita em 2026-09-21: `APROVADO — incluindo delegação da implementação documental ao routine-executor, no checkout principal, single-writer, sem worktrees.`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Guard evidence:** tuple pós-aprovação revalidado em 2026-09-21 por `agent_role_routing_guard.py`; `Overall outcome: go`, lane `executor`, `max_concurrent_writers: 1`.
- **Post-approval authority outcome:** `go`
- **Post-approval authority evidence:** `todo_authority_guard.py` sem `--pre-approval` em 2026-09-21; `execution_authority_granted: True`, 11 regras/workflows ingeridos e nenhuma violação.
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation (Mandatory Before Delivery)

| Decision ID | Status (`Adherent`/`Exception`) | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01` | Adherent | `system_roadmap.md:7-18` | temas preservados; horizonte ortogonal sem datas |
| `D-02` | Adherent | `backlog/README.md:5`; `todos/README.md:3-7`; VAL-04 | localização não concede execução |
| `D-03` | Adherent | feature brief `ST-01 disposition and canonical handoff`; `artifacts/README.md:3-5` | brief permanece evidência não autoritativa |
| `D-04` | Adherent | `evolution_lifecycle.md:36-128` | cinco máquinas ortogonais + qualifier Blocked |
| `D-05` | Adherent | `decisions/README.md:5-13`; lifecycle `Decisions` | eficácia somente após target consolidation |
| `D-06` | Adherent | `evolution_lifecycle.md:23-34` | owner singular por campo e links externos |
| `D-07` | Adherent | `evolution_lifecycle.md:130-132`; diff guard | superfícies históricas/legadas preservadas |
| `D-08` | Adherent | `backlog/README.md:11-19`; VAL-02 | ST-02/ST-03 selected; ST-04 deferred |
| `D-09` | Adherent | `evolution_lifecycle.md` Deterministic-adoption trigger; `todos/active/process/TODO-foundation-lifecycle-structural-validator.md` | limiar atingido com 18 registros; follow-up aberto em Review e nenhum validator implementado sem aprovação |
| `D-10` | Adherent | `evolution_lifecycle.md:19-21`; VAL-02 | namespaces/slugs imutáveis válidos |
| `D-11` | Adherent | `evolution_lifecycle.md:7-17`; `project_constitution.md` Lifecycle roles | agentes/ferramentas são adapters, não autoridade |

Only `Adherent` or an explicitly approved `Exception` is valid at delivery.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Module Decision Ref | Planned Handling | Delivery Status (`Preserved|Superseded (Approved)|Regression`) | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `modules/README#ownership` | Preserve | Preserved | `modules/README.md:3-16` | ownership local mantido; lifecycle apenas referenciado |
| `identity-and-tenancy#invariants` | Preserve | Preserved | baseline diff exit `0` | arquivo individual inalterado |
| `inbox-and-conversations#invariants` | Preserve | Preserved | baseline diff exit `0` | arquivo individual inalterado |
| `audit-and-history#invariants` | Preserve | Preserved | baseline diff exit `0` | arquivo individual inalterado |
| `integrations-and-channels#invariants` | Preserve | Preserved | baseline diff exit `0` | arquivo individual inalterado |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| bounded ST-01 diff + validation/adherence packet | CI/Copilot-style P1/P2, link/schema/authority drift | passed | `/root/st01_cutover_retry_final`; full restage; `git diff --quiet`; cached diff check; VAL-01/02 | `ST01-CUTF-001` integrado; nenhum P1/P2 remanescente | index e working tree representam o mesmo pacote validado |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| TODO authority + singular ownership + Foundation main-only | active-as-approval, duplicated live state, inferred contracts, legacy rewrite, hidden topology | passed | `/root/st01_cutover_retry_final`; diff guard; hashes/module preservation; worktree inspection | no_material_findings | nenhum bypass, estado vivo duplicado, contrato inferido, rewrite legado ou topologia oculta |

### Exception Handling

- Qualquer decisão marcada `Exception` bloqueia a entrega até a exceção ou alternativa ser explicitamente aprovada e o baseline receber novo `APROVADO`.
- Qualquer decisão de módulo marcada `Regression` bloqueia a entrega até existir supersessão intencional aprovada e consolidação no módulo canônico.

## TODO Closeout Disposition

- **Disposition:** `move-completed`
- **Disposition reason:** entrega documental publicada, critérios completos, auditorias limpas e decisões consolidadas; não resta trabalho de execução neste TODO.
- **Post-commit/push status:** `implementation package pushed at ad6a0cc8475bc412fd1b767e9cc19ad0123fb6fe; completed-path closeout is represented by the commit containing this file`
- **Next path/status action:** `completed`; nenhum movimento ou execução permanece neste TODO.

## Security Risk Assessment

- **Risk level:** `low`
- **Why this risk level:** docs only; principal risk is publishing secret/reference data or weakening tenant invariants, both explicitly forbidden.
- **Attack surface in scope:** documentation authority only.
- **Attack simulation decision:** `not_needed`
- **Review evidence:** VAL-10 em 2026-09-23 retornou exit `0` com nenhum secret-like assignment/private key; primeira revisão final não encontrou risco de segurança adicional.
- **Residual security risk:** inaccurate documentation claims; mitigated by evidence requirements.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `none`
- **Why this level:** no endpoint, UI, backend mutation, queue or runtime change.
- **Current delivery stage at review time:** `Local-Implemented`

| Policy Schema Version | Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Trigger Rationale | Gate Deadline | Minimum Evidence Rule ID | State | Residual Risk | Uncertainty Reason Code | Recorded At UTC | Executor ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pcv-1` | `EPS` | endpoint-performance-scrutiny | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | docs-only; nenhum endpoint, lookup, query shape ou data path muda | `before_local_implemented` | `EPS-E1` | `not_applicable` | none | none | `2026-09-21T13:02:56Z` | `codex:/root` |
| `pcv-1` | `FRC` | frontend-race-condition-validation | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | docs-only; nenhum async UI lifecycle, navigation ou race surface muda | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | none | none | `2026-09-21T13:02:56Z` | `codex:/root` |
| `pcv-1` | `BCI` | backend-concurrency-idempotency-validation | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | docs-only; nenhuma mutação, idempotency key, transaction ou lock muda | `before_local_implemented` | `BCI-INV` | `not_applicable` | none | none | `2026-09-21T13:02:56Z` | `codex:/root` |
| `pcv-1` | `RLS` | runtime-load-stress-validation | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | docs-only; nenhum runtime, workload, SLO ou topology muda | `before_production_ready` | `RLS-E1` | `not_applicable` | none | none | `2026-09-21T13:02:56Z` | `codex:/root` |

- **PCV schema gap:** `pcv-1` não possui reason codes negativos/not-triggered; `n/a` explícito evita atribuir falsamente um trigger positivo. O gap é follow-up de hardening do Delphi, sem impacto em produto/runtime e fora do ST-01.

## Verification Debt Assessment

- **Audit outcome:** `none`
- **Why this outcome:** o helper genérico retornou heurística `high`, mas a adjudicação 1-1 classificou seus hits como vocabulário governado (`TODO`, `Pending`, `Blocked`, `Deferred`), `n/a` estruturais justificados, fixtures negativos intencionais e os gates finais ainda em execução. O único follow-up material detectado — o validator acionado pelo limiar D-09 — foi promovido ao TODO separado `TODO-foundation-lifecycle-structural-validator.md`.
- **Inline code TODO debt:** `none`
- **Evidence / audit artifact:** `verification_debt_audit.sh --repo foundation_documentation --todo todos/active/process/TODO-leadshug-foundation-evolution-lifecycle.md --scan-git-modified` executado via normalização CRLF em memória em 2026-09-23; revisão manual confirmou zero marker inline de código, zero waiver material e consolidação nas superfícies canônicas.
- **Accepted residual debt:** `none`

## Independent Test Quality Audit Gate

- **Audit decision:** `recommended`
- **Why this decision:** piso determinístico para TODO medium; será focalizado na eficácia dos checks estruturais, embora não haja teste de produto.
- **Trigger signals in scope:** `none`
- **Required evidence matrix:** `n/a`
- **Audit status:** `no_material_findings`
- **Findings summary:** `ST01-TQA/TQAR/TQAF/TQAU/TQFINAL/TQFINALR/TQFINALV2` foram integrados. A revalidação V3 confirmou fail-closed para cinco estados e variantes HTML/Unicode, conteúdo e unicidade das onze DEC, targets/evidência/assertions canônicos, handoffs e parity staged/working tree, sem finding material.
- **Evidence / reference:** `/root/st01_test_quality_final_revalidation_v3`, 2026-09-23, `no_material_findings`; VAL-01/02/04/08/10 e cached diff check verdes no pacote congelado.

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
- **Final review status:** `no_material_findings`
- **Findings summary:** a primeira revisão final encontrou `ST01-FINAL-001` (gatilho D-09 já acionado sem TODO próprio) e `ST01-FINAL-002` (ação de closeout stale), ambos integrados sem alterar D-01..D-11. A revalidação confirmou 18 registros, follow-up em Review sem autoridade, matrizes/guards coerentes e nenhum finding material.
- **Evidence / reference:** `/root/st01_independent_final_review` e `/root/st01_independent_final_review_revalidation`, 2026-09-23; revalidation `no_material_findings`.
- **Waiver authority / reference:** `n/a`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `recommended`
- **Why this decision:** há cutover documental de lifecycle, mas documentos históricos permanecem por exceção explícita.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement`
- **Package mode:** `bounded-file-set`
- **Cutover audit status:** `no_material_findings`
- **Findings summary:** `ST01-CUTR-001` foi integrado com targets finitos/evidência por target; o retry encontrou somente `ST01-CUTF-001`, um index staged antigo. O allowlist completo foi restageado e index/working tree agora são idênticos; CUT-001..006, P1/P2 e rule-spirit não possuem finding remanescente.
- **Evidence / reference:** `/root/st01_cutover_revalidation`, `/root/st01_cutover_retry_final`, full explicit restage, `git diff --quiet`, cached diff check, VAL-01/02 e diff expectation guard em `go`.

## Module Consolidation Gate

- [x] Decisões estáveis foram consolidadas nas superfícies canônicas.
- [x] Módulos preservam suas decisões anteriores e `modules/README.md` aponta ao lifecycle.
- [x] Feature brief e TODO apontam para as superfícies finais.
- [x] Referências conflitantes de backlog/autoridade foram eliminadas das superfícies atuais.

## Commands (Run Locally)

- `bash delphi-ai/tools/verify_context.sh`
- `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md --pre-approval`
- `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md` somente após registrar `APROVADO`/ingestão e antes de implementar; exigir `Overall outcome: go`.
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py --repo-root foundation_documentation foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/todo_completion_guard.py --require-delivery foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/todo_closeout_guard.py --repo foundation_documentation foundation_documentation/todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md`
- `python3 delphi-ai/tools/git_write_authority_guard.py --repo foundation_documentation --action git-commit` antes de qualquer commit Foundation; exigir `Overall outcome: go`.
- `python3 delphi-ai/tools/git_write_authority_guard.py --repo foundation_documentation --action git-push` antes de qualquer push Foundation; exigir `Overall outcome: go`.
- Executar `Exact Check Command Contracts / VAL-08` para cobrir conjuntamente arquivos tracked e untracked do allowlist ST-01.
- `git -C foundation_documentation diff --exit-code d8626df1fb0ff64751d7fae10ae93cf41ab1a458 -- modules/identity-and-tenancy.md modules/inbox-and-conversations.md modules/audit-and-history.md modules/integrations-and-channels.md`
- `sha256sum foundation_documentation/.gitattributes foundation_documentation/.gitignore foundation_documentation/artifacts/migration/claude-legacy-reconciliation-review.prompt.txt foundation_documentation/artifacts/publication-manifest.txt foundation_documentation/deterministic/.gitkeep foundation_documentation/todos/ephemeral/.gitignore foundation_documentation/todos/ephemeral/.gitkeep foundation_documentation/todos/promotion_lane/.gitkeep` (comparar exatamente com a tabela de preservação).
- Executar `Exact Check Command Contracts / VAL-10`; os probes quoted/unquoted devem passar e o scan dos paths ST-01 deve retornar a mensagem `OK` sem matches.
