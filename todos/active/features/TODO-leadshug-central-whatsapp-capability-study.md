# TODO — Estudo comparativo de capacidades do Central-Whatsapp

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Program:** `leadshug-pre-code-evolution-program`
- **Backlog item:** `BLG-central-whatsapp-capability-study`

## Context

O LeadsHug foi reconstruído a partir de referências históricas do Central-Whatsapp, mas os repositórios seguiram evoluções independentes. Antes de implementar novas funcionalidades, o projeto precisa saber quais capacidades surgiram ou amadureceram no Central, quais já existem no LeadsHug e quais ideias merecem avaliação posterior dentro da arquitetura atual.

Este trabalho é um estudo de capacidades e comportamentos. O Central-Whatsapp permanece uma referência legada independente e somente leitura; não é upstream do LeadsHug e não autoriza cópia de código, sincronização de árvores ou adoção automática de decisões antigas.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md`
- **Primary story ID:** `ST-02`
- **Why this is the right current slice:** ST-01 está concluído e o catálogo comparativo é a próxima etapa pré-código. Ele produz evidência para decisões futuras sem misturar priorização (`ST-04`) nem o estudo específico do Whatsflow (`ST-03`).
- **Direct-to-TODO rationale:** `n/a`

## Contract Boundary

- Este TODO define o catálogo comparativo e a evidência necessária para considerá-lo confiável.
- A entrega descreve capacidades em linguagem própria do LeadsHug; ela não importa código, esquema, infraestrutura ou terminologia interna sem reinterpretação.
- Descobertas permanecem neste TODO enquanto forem linhas do mesmo catálogo. Uma segunda entrega independente ou mudança de arquitetura exige novo TODO e nova aprovação.

## Implementation Intent

- **Current delivery:** produzir um único catálogo de gaps de capacidade entre snapshots congelados do Central-Whatsapp e do LeadsHug, com trilhas oficial, não oficial e transversal.
- **Planned next steps:** `ST-03` estuda separadamente canais no Whatsflow; `ST-04` prioriza oportunidades depois dos dois estudos.
- **Anticipatory implementation authorized now:** `none`
- **Rationale:** primeiro separar fatos, lacunas e lições; decisões de produto e implementação continuam fora deste trabalho.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** validar em uma única rodada `D-01..D-06`, congelar o contrato e executar os gates pré-aprovação.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** o contrato foi refinado, mas decisões e autorização de execução ainda não foram congeladas.
- **Exit condition:** decisões validadas, gates pré-aprovação concluídos e `APROVADO` explícito registrado.

## Scope

- [ ] `S-01` Congelar e registrar os snapshots de comparação e sua proveniência histórica.
- [ ] `S-02` Inventariar capacidades relevantes do Central oficial surgidas ou alteradas após a baseline de importação.
- [ ] `S-03` Inventariar capacidades relevantes do hub não oficial surgidas ou alteradas após a baseline de importação.
- [ ] `S-04` Examinar separadamente o overlay local do hub incorporado ao antigo LeadsHug, sem atribuí-lo ao Central independente.
- [ ] `S-05` Comparar cada capacidade candidata com o LeadsHug API/Web atual e seus contratos canônicos.
- [ ] `S-06` Classificar cada item por estado, valor potencial, riscos, dependências e disposição recomendada.
- [ ] `S-07` Registrar lições negativas e exclusões explícitas para evitar que antipadrões legados sejam tratados como oportunidades.
- [ ] `S-08` Validar cobertura por amostragem bidirecional e publicar um único artefato de análise.

## Out of Scope

- `OOS-01` Alterar código, testes, schema, migrations, configuração, runtime, deploy ou dados do LeadsHug.
- `OOS-02` Copiar ou portar código, dependências, variáveis, segredos, infraestrutura ou dados do Central-Whatsapp.
- `OOS-03` Criar sincronização, subtree, submodule ou dependência de runtime entre os projetos.
- `OOS-04` Inspecionar, listar ou reproduzir conteúdo de `hub-whatsapp/secrets/**` ou qualquer credencial.
- `OOS-05` Definir prioridade final, roadmap de implementação ou aprovar automaticamente capacidades (`ST-04`).
- `OOS-06` Modelar em profundidade canais com múltiplas formas de atendimento (`ST-03`).
- `OOS-07` Alterar módulos, contratos ou decisões canônicas antes de um TODO futuro específico.
- `OOS-08` Avaliar produção ou executar chamadas reais a provedores externos.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `foundation_documentation:main`
- **Promotion lane path:** `main (documentação somente)`
- **Lane-promoted threshold for this TODO:** `commit/push em foundation_documentation:main`
- **Production-ready threshold for this TODO:** `artefato publicado e TODO fechado em completed/features/`
- **Topology:** checkout principal, single-writer, sem worktrees.

## Promotion Evidence (Required Before Lane-Promoted / Production-Ready)

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Catálogo ST-02 e closeout | `main@pending` | `n/a` | `n/a` | `direct documentation publication` | pending |

## Diff Expectation Contract (Required Before Delivery)

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `foundation_documentation` | `main@6344bf64d8bb7330d8c992aaff93833fc65ca6ed` | `working_tree` |
| LeadsHug API | `api-app` | `5db3fbe2043428749895fc3ff6441e9457467dd0` | `read_only_snapshot` |
| LeadsHug Web | `web-app` | `6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9` | `read_only_snapshot` |
| Central oficial | `.../Central-Whatsapp/api-oficial` | `337f3e4839cef8ca400de87b3de088a79d512944` | `read_only_snapshot` |
| Central hub | `.../Central-Whatsapp/hub-whatsapp` | `51bc16e544c7625a71c3012d8adef656c6392c37` | `read_only_snapshot` |
| LeadsHug legado | `.../Backup LeadsHug/LeadsHug` | `994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2` | `read_only_historical_snapshot` |

### Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| Foundation | `todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md` | `A/M/D` | contrato, evidência e movimento atômico no closeout |
| Foundation | `todos/completed/features/TODO-leadshug-central-whatsapp-capability-study.md` | `A` | destino do closeout |
| Foundation | `artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md` | `A/M` | entrega documental única do ST-02 |
| Foundation | `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` | `M` | atualização factual do estado/evidência de ST-02 no closeout |
| Foundation | `backlog/README.md` | `M` | transição factual do item no closeout |

### Not Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| LeadsHug API | `api-app/**` | `any` | estudo sem código |
| LeadsHug Web | `web-app/**` | `any` | estudo sem código |
| Central oficial | `.../Central-Whatsapp/api-oficial/**` | `any` | referência somente leitura |
| Central hub | `.../Central-Whatsapp/hub-whatsapp/**` | `any` | referência somente leitura |
| LeadsHug legado | `.../Backup LeadsHug/LeadsHug/**` | `any` | referência histórica somente leitura |
| Foundation | `modules/**` | `any` | nenhuma decisão de produto será promovida neste estudo |
| Foundation | `contracts/**` | `any` | contratos de runtime permanecem inalterados |
| Foundation | `project_constitution.md` | `any` | arquitetura permanece inalterada |
| Foundation | `system_roadmap.md` | `any` | priorização pertence ao ST-04 |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)

Qualquer caminho não classificado deve ser analisado antes da entrega. Expansão material requer validação humana e novo `APROVADO`.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** novas linhas de capacidade, evidência adicional, correção de classificação e melhorias locais no catálogo único.
- **Must update or split the TODO:** nova entrega independente, alteração canônica, priorização, implementação ou catálogo acima de 40 capacidades substantivas que deixe de ser revisável como uma unidade.

## Definition of Done

- [ ] `DOD-01` Baselines de importação, overlays e snapshots finais estão registrados com hashes verificáveis.
- [ ] `DOD-02` Cada capacidade tem evidência do Central e evidência/estado correspondente no LeadsHug, ou incerteza explícita.
- [ ] `DOD-03` Cada capacidade informa trilha, época, estado atual, valor potencial, riscos, dependências e disposição recomendada.
- [ ] `DOD-04` Itens posteriores à baseline estão separados dos itens que já existiam na baseline mas não foram reimplementados.
- [ ] `DOD-05` Lições negativas, exclusões e capacidades não desejadas estão explícitas.
- [ ] `DOD-06` Amostragem bidirecional não encontra superfícies relevantes sem catálogo ou exclusão justificada.
- [ ] `DOD-07` O catálogo não contém segredos, dados pessoais, payloads sensíveis nem trechos de código copiados.
- [ ] `DOD-08` Nenhuma recomendação é apresentada como prioridade aprovada ou autorização de implementação.
- [ ] `DOD-09` Gates documentais e revisão final passam; feature brief/backlog refletem apenas o estado factual concluído.

## Validation Steps

- [ ] `VAL-01` Revalidar snapshots e commits exatos de importação com `git rev-parse`/`git show`.
- [ ] `VAL-02` Comparar históricos `6517f197..9368421` e `94ce80aa..51bc16e` por commits, arquivos e comportamentos.
- [ ] `VAL-03` Comparar o overlay do hub entre a importação `beb655cd` e o snapshot legado `994e1e8` em trilha separada.
- [ ] `VAL-04` Fazer amostragem Central → catálogo e catálogo → Central/LeadsHug em cada trilha.
- [ ] `VAL-05` Verificar ausência de `secrets/**`, credenciais, dados pessoais e blocos de código copiados.
- [ ] `VAL-06` Executar validador estrutural, `git diff --check` e guards de diff, autoridade, conclusão e closeout aplicáveis.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01..S-08` | Scope | Entrega integral do estudo | doc+review | catálogo + rastreabilidade | n/a | planned | detalhar por critério antes do closeout |
| `DOD-01..DOD-09` | Definition of Done | Critérios do catálogo | doc+review+guard | catálogo, amostras, guards e revisões | n/a | planned | detalhar por critério antes do closeout |
| `VAL-01..VAL-06` | Validation Steps | Validações reproduzíveis | command+manual review | comandos e relatório | local/read-only | planned | registrar resultados exatos |

## External Dependency Readiness (Required When External Systems Matter)

- Nenhum sistema externo de runtime é necessário.
- Repositórios de referência são somente leitura; hashes congelados mantêm a reprodutibilidade se os branches avançarem.
- As duas `main` foram revalidadas em 2026-09-25: o oficial avançou 56 commits desde o snapshot anterior `9368421`; o hub permaneceu em `51bc16e`.

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality` para crítica/revisão documental obrigatória
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Assurance / Tester-Quality | desafiar cobertura, rastreabilidade e conclusões | TODO e catálogo | planned |

## Complexity

- **Level (`small|medium|big`):** `medium`
- **Checkpoint policy:** um checkpoint consolidado antes de `APROVADO` e revisão final após o catálogo.
- **Why this level:** vários repositórios e três trilhas de evidência, porém uma entrega documental, sem runtime nem implementação.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:**
  - `foundation_documentation/modules/inbox-and-conversations.md`
  - `foundation_documentation/modules/audit-and-history.md`
- **Planned decision promotion targets:** `none in ST-02; findings remain analysis inputs for ST-04`
- **Module decision consolidation targets:** `none; future implementation TODOs must promote accepted decisions`

## Decision Pending (Resolve Before Freeze)

- Nenhuma decisão material pendente após a validação conjunta de `D-01..D-06` em 2026-09-25.

## Decisions (Resolved Before Freeze)

- [x] `D-01` Usar baselines por repositório: oficial `6517f197c97d0b5bcad886d26eb0d28a813b47ca`; hub `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2`; não uma data única. O catálogo cobre diferenças entre os estados atuais e usa essas baselines para separar capacidade preexistente não reimplementada de evolução posterior.
- [x] `D-02` Tratar o overlay local do hub no LeadsHug legado até `994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2` como trilha separada, não evolução do Central.
- [x] `D-03` Comparar capacidades/comportamentos, não arquivos: cada item será reescrito como problema ou oportunidade do LeadsHug.
- [x] `D-04` Usar os estados `Entregue`, `Parcial`, `Ausente`, `Não desejado` e `Incerto`, com evidência obrigatória para estados afirmados.
- [x] `D-05` Manter oficial, não oficial e transversal no mesmo catálogo, com limite de 40 capacidades; ultrapassar pausa a execução para propor divisão.
- [x] `D-06` Tratar disposições (`descartar`, `estudar`, `candidata ao ST-04`) como recomendação fundamentada, nunca prioridade ou autorização de implementação.
- **Human validation:** usuário, `VALIDO D-01..D-06`, conversa de 2026-09-25.

### Decision Validation Review (Prepared Pre-Freeze)

| Decision | Technical validation | Evidence | Outcome |
| --- | --- | --- | --- |
| `D-01` | Os commits-base são exatos e permanecem alcançáveis nos repositórios atuais. | O tree `76e80538...` de `api-oficial@6517f197` é idêntico ao subtree importado por `LeadsHug legado@4ac8ddee`; o tree `f926eca3...` de `hub-whatsapp@94ce80aa` é idêntico ao subtree importado por `beb655cd`. | technically-valid; pending-human-validation |
| `D-02` | O overlay incorporado é uma linha histórica distinta. | Entre `beb655cd` e `994e1e8`, apenas `994e1e8` toca `hub-whatsapp/`; ele não é commit do Central independente. | technically-valid; pending-human-validation |
| `D-03` | Comparação por arquivo produziria ruído e falsas equivalências. | Desde as baselines há 455 commits no oficial e 240 no hub, distribuídos entre backend, frontend, migrations, docs e correções; vários commits representam a mesma capacidade. | technically-valid; pending-human-validation |
| `D-04` | A taxonomia cobre presença integral, parcial, ausência, rejeição intencional e falta de evidência. | Os cinco estados distinguem fato observado, decisão negativa e incerteza sem converter inferência em verdade. | technically-valid; pending-human-validation |
| `D-05` | Um catálogo único preserva leitura transversal; o limite evita uma entrega irrevisável. | O feature brief admite divisão apenas se o inventário exceder um TODO manejável; 40 capacidades é o stop condition explícito, não meta de preenchimento. | technically-valid; pending-human-validation |
| `D-06` | Recomendações não podem adquirir autoridade de roadmap neste estudo. | O backlog é dono da disposição e `ST-04` é a story de síntese/priorização; o policy boundary proíbe adoção automática. | technically-valid; pending-human-validation |

**Material-decision sweep:** nenhuma decisão adicional é necessária para congelar o contrato. Novas escolhas de produto descobertas durante o estudo serão evidência para `ST-04`, não expansão silenciosa deste TODO.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `integrations-and-channels#provider-boundary` | provedores ficam atrás de adapters e payloads não vazam ao core | Preserve | `modules/integrations-and-channels.md` |
| `inbox-and-conversations#conversation-identity` | conversa é única por BU/contato e independente do transporte | Preserve | `modules/inbox-and-conversations.md` |
| `audit-and-history#append-oriented-history` | histórico auditável e tenant/BU-scoped | Preserve | `modules/audit-and-history.md` |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-06` congeladas exatamente como registradas em `Decisions`.
- **Freeze scope:** decisões, snapshots, Scope/Out of Scope, Definition of Done, Validation Steps e Diff Expectation Contract deste TODO.
- **Renewal trigger:** qualquer mudança material nesses campos requer nova validação do usuário e novo `APROVADO`.

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `not_needed`
- **Why this applies:** o estudo registra evidência e recomendações; não muda arquitetura nem contratos.
- **Deviation / debt being retired:** `n/a`
- **Target steady-state after closeout:** Central permanece referência independente; LeadsHug permanece dono de suas decisões.
- **Temporary exceptions allowed:** `none`
- **Cutover / removal condition:** `n/a`

## Gate: Review Baseline Freeze

- **Status:** `passed`; baseline decisória congelada, commitada e publicada antes dos reviews/guards formais.
- **Freeze target:** `D-01..D-06`, snapshots, escopo e diff contract.
- **Baseline branch/commit/push:** `foundation_documentation:main@cff19546`, publicado em `origin/main` em 2026-09-25.
- **Evidence:** `git_write_authority_guard.py` retornou `Overall outcome: go` para commit e push; `git.exe push origin main` publicou `6344bf64..cff19546`.

## Gate: Review Scope Drift

- **Status:** `pending execution`
- **Rule:** implementação, promoção canônica ou entrega independente exige novo contrato/aprovação.

## Questions To Close

- [x] Validar conjuntamente `D-01..D-06`.
- [ ] Após os gates de planejamento, registrar `APROVADO` para executar o catálogo.

## Assumptions Preview (Required Before Plan Review)

- Hashes congelados são a unidade de reprodutibilidade; branches podem avançar sem mudar o escopo.
- Histórico, docs e código demonstram presença de capacidade, não automaticamente sua qualidade ou adequação.
- Ausência só será afirmada após busca no API, Web e documentação atual; caso contrário, será `Incerto`.
- `secrets/**`, valores de ambiente, dados reais e payloads sensíveis são excluídos mesmo quando aparecem no histórico.
- A terminologia Mantenedora → Setor → BU e conversa independente de transporte prevalece sobre nomes legados.

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces

- Escrita: TODO, catálogo, atualização factual do feature brief e backlog no closeout.
- Leitura: Foundation; LeadsHug API/Web; Central oficial/hub; snapshot legado incorporado.

### Ordered Steps

1. Revalidar hashes, proveniência e limpeza das árvores de referência.
2. Gerar inventários por histórico e superfícies funcionais nas três trilhas.
3. Normalizar capacidades, deduplicar e separar evolução pós-baseline de lacunas preexistentes.
4. Verificar cada candidato no LeadsHug e confrontar módulos/contratos canônicos.
5. Preencher valor, risco, dependências, disposição e exclusões sem definir prioridade.
6. Executar amostragem bidirecional, revisão de privacidade/segredos e crítica de conclusões.
7. Corrigir achados, preencher evidência, atualizar estados factuais e fechar o TODO.

### Test Strategy

- Validação documental e histórica somente leitura.
- Amostragem por trilha: cinco superfícies ou todas, quando houver menos de cinco.
- Amostra catálogo → fontes: ao menos 25% das linhas, mínimo de cinco, incluindo todas `Não desejado` ou `Incerto`.
- Amostra fontes → catálogo: cada item selecionado resulta em capacidade catalogada ou exclusão explícita.

### Flow Evidence Planning Matrix

| Flow / Criterion | User-visible or runtime impact now? | Planned Evidence | Runtime Lane | Waiver Rationale |
| --- | --- | --- | --- | --- |
| Catálogo ST-02 | no | rastreabilidade entre snapshots, catálogo e estado LeadsHug | n/a | análise sem mudança de runtime/UI |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundation lifecycle | TODO, análise, backlog e feature brief | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | approval/delivery | planned | exact command | testes de produto não se aplicam |
| Markdown/git hygiene | documentação | `git -C foundation_documentation diff --check` | delivery | planned | exact command | inclui caminhos esperados |

### Runtime / Rollout Notes

- `n/a`: nenhuma mudança executável ou rollout.

## Plan Review Gate

- **Status:** `pending after decision validation`
- **Required review:** cobertura, falsos positivos/negativos, separação histórica e suficiência da amostragem.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`
- **Latest TEACH evidence / artifact:** `pending audit-escalation run after review baseline cff19546`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | múltiplos repositórios, uma entrega documental |
| `blast_radius` | `cross-module` | integrações/canais, inbox/conversas e auditoria |
| `behavioral_change_or_bugfix` | `no` | análise sem alteração de comportamento |
| `changes_public_contract` | `no` | nenhum contrato será alterado |
| `touches_auth_or_tenant` | `no` | restrições são lidas, não modificadas |
| `touches_runtime_or_infra` | `no` | nenhum runtime ou infraestrutura será tocado |
| `touches_tests` | `no` | nenhuma suíte de produto será alterada |
| `critical_user_journey` | `no` | estudo pré-código |
| `release_or_promotion_critical` | `no` | não participa de release do produto |
| `high_severity_plan_review_issue` | `no` | nenhum issue card alto aberto antes da revisão |
| `explicit_three_lane_request` | `no` | nenhuma solicitação de auditoria em três lanes |

## Independent No-Context Critique Gate

- **Critique decision:** `pending audit-escalation guard`
- **Why this decision:** complexidade média e blast radius cross-module.
- **Impact signals in scope:** `cross-module blast radius`.
- **Package mode:** `bounded-file-set`.
- **Package minimum contents:** TODO congelado, feature brief, policy de legado e três módulos âncora.
- **Critique isolation mode:** `fresh internal no-context reviewer`.
- **Internal reviewer mandate:** `pending audit-escalation guard`.
- **Canonical multi-lane audit protocol:** `n/a`.
- **Audit session / round evidence:** `n/a`.
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`.
- **Critique status:** `not_run`.
- **Findings summary:** `none yet`.
- **Evidence / reference:** `pending review baseline freeze`.
- **Waiver authority / reference:** `n/a`.

## Gate: Assumption Code Coherence

- **Status:** `pending after D-01..D-06`
- **Required check:** confirmar que termos e estados correspondem às superfícies reais, sem transformar nomes de arquivo em capacidades.

## Approval

- **Decision validation:** `pending`
- **Execution approval:** `pending`
- **Required phrase after plan gates:** `APROVADO`

## Rules Acknowledgement / Ingestion

- Pendente até `APROVADO`. Na execução, preservar política de legado independente, modelo tenant/BU/conversa e limite estrito de escrita documental.

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** contract-refinement
- **Selected role:** strategic-cto
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Writer scheduling policy:** one writer in canonical checkout; reviewers read-only
- **Guard outcome:** pending decisions and approval gates

## Decision Adherence Validation (Mandatory Before Delivery)

- Pendente; verificar `D-01..D-06` linha a linha no catálogo e no diff final.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

- Pendente; preservar os três módulos âncora sem promover recomendações como decisões.

## Security Risk Assessment (Mandatory Before Delivery)

- **Risk:** baixo se exclusão de segredos/PII e leitura somente forem mantidas.
- **Required evidence:** diff sem valores sensíveis, trechos copiados ou acesso a `hub-whatsapp/secrets/**`.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Risk:** `n/a` para runtime; análise local deve permanecer somente leitura e bounded.

## Verification Debt Assessment (Required Before `Completed`)

- Pendente. Lacunas de amostragem e classificações `Incerto` serão dívida explícita, nunca ocultada.

## Independent Test Quality Audit Gate

- **Applicability:** `not_needed`; não há testes de produto. A amostragem será avaliada na crítica e revisão final.

## Independent No-Context Final Review Gate

- **Status:** `pending delivery`
- **Required focus:** rastreabilidade, linguagem não prescritiva, cobertura, privacidade e ausência de implementação.

## Independent Cutover Integrity Audit Gate

- **Applicability:** `not_needed`; não há cutover.

## Delivery Confidence Gate

- **Status:** `pending`
- **Required outcome:** critérios/evidências passam sem recomendação apresentada como decisão aprovada.

## Module Consolidation Gate

- **Status:** `not applicable for product decisions`; somente feature brief/backlog recebem atualização factual de conclusão.

## Commands (Run Locally)

- `git rev-parse` e `git show` nos snapshots congelados.
- `git log --name-status`/`git diff --stat` nos intervalos históricos.
- `rg` somente em superfícies não sensíveis.
- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`.
- `git -C foundation_documentation diff --check`.

## Files Expected

- `foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`
- `foundation_documentation/artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md` após aprovação.
- Feature brief/backlog e movimento para `completed/features/` apenas no closeout.

## COMENTÁRIO:

- Contrato deliberadamente reduzido a uma entrega documental e seis decisões materiais reunidas em uma única rodada.
