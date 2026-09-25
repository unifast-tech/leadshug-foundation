# TODO — LeadsHug: estudo conceitual de canais e atendimento do whatsflow_v2

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`

## Context

O `whatsflow_v2` contém soluções de conexão, inbox, departamentos, atendentes, distribuição, transferência e SLA que podem informar o LeadsHug. O legado, porém, usa uma arquitetura e um vocabulário diferentes: no LeadsHug, a BU é o número/unidade mínima de atendimento, o Canal é transporte e o Setor agrupa BUs. Este TODO governa um estudo conceitual independente, sem copiar código ou transformar observações do legado em arquitetura canônica por silêncio.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md`
- **Primary story ID:** `ST-03`
- **Backlog candidate:** `BLG-whatsflow-channel-attendance-study`
- **Why this is the right current slice:** ST-01 e ST-02 foram concluídos; ST-03 é a única investigação independente restante antes da síntese ST-04.
- **Direct-to-TODO rationale:** `n/a`; a decomposição já existe no feature brief.

## Contract Boundary

- Este TODO entrega um modelo conceitual e recomendações fundamentadas; não implementa nem canoniza o modelo de atendimento.
- O `whatsflow_v2` é referência somente leitura. Código, schema, configurações, credenciais, dados e infraestrutura não serão copiados ou alterados.
- Observações do legado serão distinguidas de recomendações para o LeadsHug e de decisões canônicas já existentes.
- Qualquer proposta de mudar `Setor`, `BU`, `Canal`, autorização ou unicidade da conversa exige decisão posterior e TODO próprio.

## Implementation Intent

- **Current delivery:** produzir um estudo reprodutível de conexões/canais, unidades de atendimento, equipes, filas, roteamento, atribuição, capacidade, transferência, SLA, autorização e automação/handoff.
- **Planned next steps:** `ST-04 sintetiza ST-02 e ST-03; informacional e não autorizado por este TODO`.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** separar descoberta conceitual de mudança de produto evita transportar a dívida e a colisão de vocabulário do legado.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** publicar o próximo checkpoint documental (SHA ainda inexistente), repetir evidência/quality review e executar P1/P2, rule-spirit e final review.
- **Current checkout identity:** `foundation_documentation:main@ce2af2765b1bb5a3437125537787b6c701221b98` + working-tree documental não commitado; o SHA do próximo checkpoint só existirá após commit autorizado.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `implementation`
- **Why this state now:** planejamento e gates convergiram, e o usuário autorizou explicitamente a execução documental do ST-03.
- **Exit condition:** estudo, evidências, auditorias e guards finais concluídos, seguido de closeout para `completed/features/`.

## Scope

- [x] Congelar um manifesto reprodutível do `whatsflow_v2` e registrar branch, commit, tree e superfícies admitidas.
- [x] Preencher o catálogo conceitual `C-01..C-12` e sua matriz única de cobertura, sem criar uma taxonomia canônica do produto.
- [x] Produzir diagrama conceitual, cardinalidades, glossário comparativo, invariantes, estados e transições.
- [x] Confrontar cada conceito com Mantenedora, Setor, BU, Canal, Conversa, Usuário e auditoria do LeadsHug.
- [x] Validar cenários de entrada, múltiplas BUs, fila livre, atribuição manual/automática, capacidade, transferência, SLA, automação/handoff e isolamento entre Mantenedoras.
- [x] Registrar padrões aproveitáveis, limitações, inconsistências e anti-padrões do legado.
- [x] Formular recomendações e decisões futuras sem atribuir prioridade ou autoridade de implementação.

## Out of Scope

- [ ] Alterar código, banco, runtime ou documentação canônica de produto do LeadsHug.
- [ ] Alterar, atualizar, trocar branch ou copiar artefatos do `whatsflow_v2` durante o estudo sem autorização específica.
- [ ] Buscar paridade integral ou provar saúde produtiva do legado.
- [ ] Reusar `department/setor` como `Setor` do LeadsHug sem decisão canônica posterior.
- [ ] Priorizar ou implementar recomendações; isso pertence ao ST-04 e a futuros TODOs aprovados.
- [ ] Publicar segredos, dados pessoais, payloads reais ou trechos extensos de código legado.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `foundation_documentation:main`; `whatsflow_v2:stage (read-only reference)`
- **Promotion lane path:** `Foundation main direct publication`; nenhum lane do produto ou do legado.
- **Lane-promoted threshold for this TODO:** `Foundation main published`.
- **Production-ready threshold for this TODO:** `n/a; no runtime delivery`.

## Promotion Evidence (Required Before Lane-Promoted / Production-Ready)

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| TODO e estudo ST-03 | `foundation_documentation:main@ce2af276` + corrective working tree | `n/a` | `n/a` | `direct publication pending` | implementation; exact review SHA will be frozen by the next bounded packet |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `foundation_documentation` | `main@9cf4b1d110477fff12b557481d1ebdb223a1001f` | `working_tree` |
| whatsflow_v2 | `/mnt/c/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2` | `3a36436c83ebefc6839380eb8fac1a6f13f4700a` | `working_tree` |

### Snapshot Manifest Contract

| Reference | Branch / Commit | Tree | Verified | Role |
| --- | --- | --- | --- | --- |
| primary evidence | objeto local `3a36436c83ebefc6839380eb8fac1a6f13f4700a` | `6befe605dda039a7066a7fd48403807ea93f8408` | `status`, `rev-parse HEAD`, objeto/tree locais, 2026-09-25 | baseline imutável utilizável; frescura remota não confirmada |
| comparison landmark | objeto local `cfe0aa120503687943ee81930172994a1ea9ab1a` | `d739d0a517651a4ed1621940c62e7a3107ee29ef` | `rev-list` local 0/59, 2026-09-25 | comparação local, não segunda população |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md` | `A, M, D` | governing contract and later closeout move |
| Foundation | `todos/completed/features/TODO-leadshug-whatsflow-channel-attendance-study.md` | `A, M` | closeout destination for the governing contract |
| Foundation | `artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-*.md` | `A, M, ??` | study deliverable; `??` is the pre-commit working-tree form of the approved new artifact |
| Foundation | `backlog/README.md` | `M` | factual handoff and closeout state |
| Foundation | `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` | `M` | factual ST-03 handoff only |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| whatsflow_v2 | `**` | `any` | reference is read-only |
| Foundation | `project_constitution.md,domain_entities.md,modules/**,contracts/**,decisions/**,system_roadmap.md` | `any` | canonization belongs to ST-04 or later approved TODO |
| Foundation | `.env*,**/secrets/**,**/*credential*,**/*token*` | `any` | sensitive material excluded |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)

O primeiro guard retornou `no-go` somente por defeitos estruturais do contrato: path Windows não resolvível pelo guard, comparison mode textual e change types separados por `|`, além de labels de repositório não declarados. O segundo identificou `??` para o novo artefato ainda não staged. Classificação: `necessary/justifiable contract repair`, sem path real divergente e sem mudança de escopo. O contrato foi normalizado para paths POSIX, `working_tree`, tipos separados por vírgula, somente repositórios declarados e o estado `??` previsto para o artefato aprovado; o guard deve ser repetido antes da entrega.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** ampliar buscas dentro dos mesmos conceitos, corrigir evidência e adicionar cenário subordinado ao modelo de atendimento.
- **Must update or split the TODO:** mudar conceitos canônicos, criar ADR, alterar módulos/contratos, implementar produto ou transformar ST-03 em priorização ST-04.

## Study Evidence Contract

- Cada observação material aponta para `whatsflow_v2@sha:path:symbol-or-section` e recebe força `direct|corroborated|inferred|conflicting`.
- Presença estática prova somente que um artefato existe. Uma alegação `observed_operational_path` exige call path executável e atual mais teste ou superfície corroborante; schema efetivo é obrigatório apenas para comportamento apoiado em persistência e deve ser marcado explicitamente `not_applicable` nos demais casos.
- Cada evidência recebe natureza `effective_runtime|effective_schema|test|documentation|historical|superseded|orphaned|declarative_only|conflicting`; itens sem alcance ou supersessão resolvidos não sustentam comportamento operacional.
- Cada conceito recebe estado `observed_operational_path|partial|documented_only|conflicting|unknown|not_found_after_protocol`.
- Alegação de ausência exige busca em código, schema/migrações e documentação admitidos; sem isso, permanece `not_found_after_protocol` ou `unknown`, conforme a evidência.
- O estudo separa `legacy_observation`, `leadshug_constraint`, `recommendation` e `future_decision`; recomendação nunca equivale a decisão.
- Não serão persistidos dumps, patches, payloads ou inventários brutos do legado.

## Stable Concept Catalog And Coverage Contract

Os IDs abaixo organizam o estudo, não renomeiam entidades do LeadsHug. O artefato final terá uma única linha por conceito contendo: superfícies legadas admitidas; natureza/força/estado da evidência; constraint LeadsHug; relações/cardinalidades/estados aplicáveis; cenários obrigatórios; disposição `pattern|limitation|anti_pattern|unknown`; recomendação ou decisão futura; e evidência de conclusão.

| Concept ID | Study Concept | Required Model Output |
| --- | --- | --- |
| `C-01` | conexão/provedor e seu lifecycle | adapter, identidade externa, disponibilidade, falha e troca de transporte |
| `C-02` | BU/número e vínculo com canal | cardinalidade sem criar organização paralela |
| `C-03` | entrada, identidade e continuidade da conversa | BU/contato, replay, reordenação e troca de transporte |
| `C-04` | unidade de atendimento/equipe | especialização e relação com BUs sem reutilizar Setor |
| `C-05` | associação e cobertura de agentes | papéis, grants, membership e visibilidade |
| `C-06` | fila e elegibilidade | entrada/saída, escopo, fila livre e casos sem grant/null-scope |
| `C-07` | política de roteamento/distribuição | manual, round-robin, menor carga e critérios de escolha |
| `C-08` | claim, atribuição, presença e capacidade | atomicidade, reserva/liberação e winner/loser semantics |
| `C-09` | transferência e handoff humano/automação | origem/destino, corrida, retorno à fila e trilha de auditoria |
| `C-10` | lifecycle do atendimento | aberto, pendente, em atendimento, resolvido, reaberto e ownership |
| `C-11` | SLA e escalonamento | relógios, pausas, custo de avaliação, alerta e breach |
| `C-12` | auditoria e histórico | append-only, tenant/BU scope e permissão de leitura independente |

## Canonical Invariant Coverage Matrix

| Canonical Invariant | Planned Handling | Mandatory Walkthrough / Evidence |
| --- | --- | --- |
| Conversa única por BU/contato, independente do transporte | Preserve | mesma BU/contato entra, troca provider/transporte e permanece uma conversa |
| Webhook de entrada é idempotente | Preserve | evento duplicado e fora de ordem não duplica mensagem/efeito nem regride estado |
| Saída respeita janela e capacidade do canal | Preserve | tentativa fora da janela ou sem capability falha deterministicamente |
| Provider é adapter, não dono do workflow | Preserve | troca/falha de provider não redefine fila, assignment ou identidade da conversa |
| Segredos não entram em docs/logs/fixtures/client | Preserve | revisão sanitizada do diff e referências sem valores/payloads |
| Falha de provider vira erro determinístico | Preserve | indisponibilidade explícita, sem fallback silencioso ou perda de ownership |
| Cada operação resolve uma Mantenedora/tenant | Preserve | cross-tenant negado em view/claim/assign/transfer/resolve/configure |
| Permissões são materializadas na BU | Preserve | no-grant, cross-BU e null-scope negados por padrão; exceções apenas como risco legado |
| Papéis são `OWNER`, `ADMIN`, `ATENDENTE` | Preserve | matriz por operação: view, claim, assign, transfer, resolve, configure |
| Histórico é append-oriented | Preserve | claim/transfer/handoff/resolve geram eventos e não apagam proveniência |
| Todo histórico é tenant- e BU-scoped | Preserve | consulta cross-tenant/cross-BU não vaza eventos |
| Permissão de leitura independe da escrita | Preserve | ator autorizado a operar não recebe leitura histórica implícita e vice-versa |

## Documentary Performance And Concurrency Rubric

As lanes runtime `pcv-1` continuam `not_needed`; os itens abaixo são requisitos analíticos do modelo e não autorizam load tests ou implementação.

| Concern | Required Conceptual Outcome |
| --- | --- |
| Dois agentes fazem claim simultâneo | operação atômica, um vencedor, loser determinístico, sem dupla atribuição |
| Reserva/liberação de capacidade | unidade da reserva, limites, compensação e liberação em transfer/resolve/disconnect |
| Claim versus transfer/resolve | precedência ou compare-and-set explícito; nenhum ownership perdido |
| Automação versus humano | handoff idempotente, ownership único e mensagem não duplicada |
| Presença obsoleta | TTL/heartbeat e fallback explícito; ausência não significa acesso ou disponibilidade ilimitada |
| Filas, listas e contagens | leitura bounded/paginada e agregação server-side; evitar varredura client-side ilimitada |
| SLA | custo bounded, clock/source of truth e estratégia de avaliação/escalonamento |
| Polling/realtime fan-out | deduplicação, backpressure e impacto por tenant/BU explicitados |

## Definition of Done

- [ ] `DOD-01` Manifesto, alcance/supersessão e call paths tornam cada alegação operacional reprodutível; schema efetivo é exigido quando há persistência e `not_applicable` caso contrário; histórico, órfão e declarativo não são tratados como comportamento. (rerun pending)
- [ ] `DOD-02` A matriz única `C-01..C-12` liga cada conceito a fontes, evidência, constraints, modelo, cenários, disposição e conclusão. (rerun pending)
- [ ] `DOD-03` Diagrama e glossário separam transporte, BU, unidade de atendimento, equipe, fila, política, capacidade e atribuição. (rerun pending)
- [ ] `DOD-04` Cardinalidades, invariantes e estados/transições cobrem o ciclo de atendimento e seus casos unknown/conflicting. (rerun pending)
- [ ] `DOD-05` A matriz 1:1 de invariantes canônicos passa nos walkthroughs positivos e negativos previstos. (rerun pending)
- [ ] `DOD-06` A rubrica documental de concorrência/performance cobre claim, capacidade, corridas, presença, filas, SLA e fan-out. (rerun pending)
- [ ] `DOD-07` Padrões úteis, limitações e anti-padrões possuem evidência e não viram prescrição automática. (rerun pending)
- [ ] `DOD-08` Recomendações indicam decisão futura, dependências e risco sem prioridade ou autorização. (rerun pending)
- [ ] `DOD-09` Artefato não contém segredo, PII, payload real ou código legado copiado. (rerun pending)
- [ ] `DOD-10` Validators, guards e revisões documentais aplicáveis passam antes do closeout.

## Validation Steps

- [ ] `VAL-01` Revalidar limpeza, branch, head, tree e ancestralidade do snapshot antes da execução. (rerun pending)
- [ ] `VAL-02` Classificar alcance/supersessão e resolver schema efetivo apenas nas alegações persistence-backed — registrando `not_applicable` nas demais — antes da auditoria bidirecional `C-01..C-12`. (rerun pending)
- [ ] `VAL-03` Executar todos os walkthroughs da matriz de invariantes, incluindo troca de transporte, replay/reordenação, falha/capability do provider e matriz de atores/operações. (rerun pending)
- [ ] `VAL-04` Executar a rubrica de concorrência/performance com source evidence, invariant esperado e disposição explícita `pattern|limitation|anti_pattern|unknown`. (rerun pending)
- [ ] `VAL-05` Revisar explicitamente segredos, PII, payloads e cópia indevida no diff final. (rerun pending)
- [ ] `VAL-06` Executar validador estrutural, `git diff --check` e guards de autoridade, diff, conclusão e closeout aplicáveis.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01` | Definition of Done | evidência operacional distingue call path atual e schema persistence-backed de artefato histórico/órfão | doc+review | artefato, manifesto/matriz | n/a | pending | correção de supersessão, schema e ausência requer rerun |
| `DOD-02` | Definition of Done | matriz única cobre `C-01..C-12` | doc+integrity review | artefato, `#matriz-única-de-cobertura-c-01c-12` | n/a | passed | 12/12 IDs, uma linha por conceito |
| `DOD-03` | Definition of Done | diagrama/glossário separam os conceitos | doc+review | artefato, `#modelo-conceitual-proposto-para-discussão-posterior` | n/a | passed | sem colisão Setor/Canal/BU |
| `DOD-04` | Definition of Done | cardinalidades/estados cobrem conflitos e unknowns | doc+review | artefato, modelo + C-01..C-12 | n/a | passed | sem coerência inventada |
| `DOD-05` | Definition of Done | invariantes canônicos cobertos 1:1 | scenario review | artefato, `#walkthrough-11-dos-invariantes-já-canônicos` | n/a | passed | positivos e negativos documentados |
| `DOD-06` | Definition of Done | rubrica concorrência/performance completa | scenario review | artefato, `#rubrica-de-concorrência-e-desempenho-documental` | n/a | passed | análise, sem load test |
| `DOD-07` | Definition of Done | patterns/limitations/anti-patterns fundamentados | doc+review | artefato, `#padrões-limitações-anti-padrões-e-incógnitas` | n/a | passed | legado não vira prescrição |
| `DOD-08` | Definition of Done | recomendações sem prioridade/autoridade | doc+review | artefato, `#recomendações-sem-priorização` | n/a | passed | somente handoff ST-04 |
| `DOD-09` | Definition of Done | conteúdo sensível/cópia excluídos | scan+manual review | `rg` sanitizado + revisão do diff | Foundation diff | passed | sem payload/dump ou valores sensíveis |
| `DOD-10` | Definition of Done | gates documentais passam | guard+review | validator/guards/reviews | Foundation | planned | closeout somente após tudo green |
| `VAL-01` | Validation Steps | snapshot revalidado | command | `git status/rev-parse/rev-list` local | frozen reference | pending | objetos locais confirmados; frescura remota e rerun pendentes |
| `VAL-02` | Validation Steps | alcance/supersessão e schema aplicável resolvidos antes da auditoria bidirecional | command+review | artefato, manifesto + matriz C-01..C-12 | read-only | pending | E-17/E-18 e novo alcance exigem rerun |
| `VAL-03` | Validation Steps | walkthroughs dos invariantes | scenario review | artefato, walkthrough 1:1 | n/a | passed | positivos e negativos |
| `VAL-04` | Validation Steps | rubrica operacional | scenario review | artefato, rubrica documental | n/a | passed | source + invariante + disposição |
| `VAL-05` | Validation Steps | revisão sensível/cópia | scan+manual review | `rg` sanitizado + `git diff --check` | Foundation diff | passed | nenhum payload/dump persistido |
| `VAL-06` | Validation Steps | validators/guards | command | exact command outputs | Foundation | planned | inclui completion/closeout no final |

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| local `whatsflow_v2` Git snapshot | source of evidence | usable-frozen / remote-fetch-degraded | 2026-09-25 | refs locais confirmam `HEAD=origin/stage@3a36436`, tree `6befe605`, status clean; fetch posterior não autenticou | o SHA congelado já estava local e foi lido por blob; nenhum resultado depende de mover refs |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality` for independent documentary critique/final review.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Assurance / Tester-Quality | desafiar o modelo, rastreabilidade e conclusões sem contexto prévio | TODO e estudo | checkpoint atual: correção documental pós-R4; próximo checkpoint ainda sem SHA até commit; re-review obrigatório |

## Complexity

- **Level (`small|medium|big`):** `medium`
- **Checkpoint policy:** um checkpoint consolidado para decisões, um após crítica pré-aprovação e revisão final após o estudo.
- **Why this level:** um legado amplo e quatro módulos conceituais, porém uma única entrega documental sem runtime.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/inbox-and-conversations.md`
- **Secondary module docs:**
  - `foundation_documentation/modules/integrations-and-channels.md`
  - `foundation_documentation/modules/identity-and-tenancy.md`
  - `foundation_documentation/modules/audit-and-history.md`
- **Planned decision promotion targets:** `none in ST-03; ST-04 decides whether recommendations advance`.
- **Module decision consolidation targets:** `none in ST-03; any canonization requires a later approved target`.

## Decision Pending (Resolve Before Freeze)

- Nenhuma decisão material pendente.

## Decisions (Resolved Before Freeze)

- [x] `D-01` Usar o objeto local `3a36436c83ebefc6839380eb8fac1a6f13f4700a` como fonte principal porque a comparação local registra 59 commits à frente de `cfe0aa12`; manter este último apenas como landmark. Objetos/trees locais foram verificados; frescura remota não é alegada.
- [x] `D-02` Interpretar “várias formas de atendimento” como combinação de dimensões independentes — unidade/equipe, fila, distribuição, capacidade, modalidade humana/automação e transferência — e não como subtipos pertencentes ao Canal.
- [x] `D-03` Preservar `Setor`, `BU` e `Canal` com os significados atuais durante o estudo; usar termos neutros (`unidade de atendimento`, `equipe`, `fila`, `política de roteamento`) e deixar qualquer renomeação/canonização para decisão posterior.
- **Human validation:** usuário, `VALIDO D-01..D-03`, conversa de 2026-09-25.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `domain_entities.md#Core vocabulary` | Setor agrupa números; BU é número/unidade mínima; Canal é transporte | Preserve | core vocabulary and identity rule |
| `inbox-and-conversations.md#Invariants-1` | conversa única por BU/contato, independente de transporte | Preserve | canonical invariant coverage matrix |
| `inbox-and-conversations.md#Invariants-2` | webhook de entrada idempotente | Preserve | canonical invariant coverage matrix |
| `inbox-and-conversations.md#Invariants-3` | saída respeita janela e capability do canal | Preserve | canonical invariant coverage matrix |
| `integrations-and-channels.md#Invariants-1` | providers são adapters | Preserve | canonical invariant coverage matrix |
| `integrations-and-channels.md#Invariants-2` | segredos não vazam | Preserve | canonical invariant coverage matrix |
| `integrations-and-channels.md#Invariants-3` | falha de provider é determinística | Preserve | canonical invariant coverage matrix |
| `identity-and-tenancy.md#Invariants-1` | cada operação resolve tenant/account | Preserve | canonical invariant coverage matrix |
| `identity-and-tenancy.md#Invariants-2` | grants materializados na BU | Preserve | canonical invariant coverage matrix |
| `identity-and-tenancy.md#Invariants-3` | papéis são OWNER/ADMIN/ATENDENTE | Preserve | canonical invariant coverage matrix |
| `audit-and-history.md#Invariants-1` | histórico append-oriented | Preserve | canonical invariant coverage matrix |
| `audit-and-history.md#Invariants-2` | registros tenant- e BU-scoped | Preserve | canonical invariant coverage matrix |
| `audit-and-history.md#Invariants-3` | leitura autorizada independentemente da escrita | Preserve | canonical invariant coverage matrix |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-03` validadas e prontas para o freeze de revisão, sem ampliar ST-03 para canonização.
- **Renewal trigger:** alteração material em decisões, Scope, Out of Scope, DoD, validações ou matriz de diff.

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `not_needed`
- **Why this applies:** ST-03 produz análise e recomendações; não estabelece, corrige ou substitui arquitetura canônica.
- **Deviation / debt being retired:** `n/a`
- **Target steady-state after closeout:** evidência conceitual disponível para ST-04, sem mudança silenciosa no domínio.
- **Temporary exceptions allowed:** `none`
- **Cutover / removal condition:** `n/a`

## Architecture Review Gates

- **Architecture decision review:** `not_needed`
- **Decision review lifecycle:** `n/a`
- **Decision review kind:** `n/a`
- **Decision review package:** `n/a`
- **Decision review status:** `n/a`
- **Decision review evidence / resolution:** `n/a`
- **Architecture adherence review:** `not_needed`
- **Adherence review lifecycle:** `n/a`
- **Adherence review kind:** `n/a`
- **Adherence review package:** `n/a`
- **Adherence review status:** `n/a`
- **Adherence review evidence / resolution:** `n/a`
- **No-go handling:** return to the affected decision/evidence loop; do not claim approval or completion.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** uma crítica formal deve partir de contrato publicado e reprodutível.
- **Trigger stage:** `before the first planning-side review or guard run`.
- **Baseline branch:** `main`
- **Baseline commit:** `27359d64b7cfd92d25eabeb18ce437f2e60cba4c`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** reclassificação de A-01..A-03 validada e congelada sem mudança de escopo.
- **Evidence / reference:** guards de escrita retornaram `go`; commit `27359d64` publicado como `origin/main` em 2026-09-25. `f3eed1fd` permanece como baseline histórica que detectou corretamente o drift.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impedir que integrações pós-crítica ampliem o estudo sem revalidação.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`.
- **Baseline source:** `Review Baseline Freeze -> 27359d64b7cfd92d25eabeb18ce437f2e60cba4c`.
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md`.
- **No-go handling rule:** return to review/revalidation; no automatic rollback.
- **Gate status:** `no_material_findings`
- **Findings summary:** 22 seções materiais comparadas contra `27359d64`; zero alterações materiais após o freeze renovado.
- **Evidence / reference:** `foundation_documentation/artifacts/tmp/st03-planning-review/review-scope-drift-final.json`; `Overall outcome: go`.
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] Validar conjuntamente `D-01..D-03`.
- [x] Revalidar a integração de `ST03-CRIT-001..004` sem novas decisões de produto.
- [x] Revalidar a integração de `ST03-CRIT-R2-001..002` sem novas decisões de produto.
- [x] Validar a reclassificação de `A-01..A-03` como fatos contratuais resolvidos, sem mudança de escopo ou novas decisões.
- [x] Após revisão independente e guards de planejamento, registrar `APROVADO` para executar o estudo.

## Assumptions Preview (Required Before Plan Review)

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | o snapshot local congelado está limpo e pode ser estudado sem executar runtime | status/rev-parse locais: `HEAD=3a36436`, tree `6befe605`; manifesto registra superfícies congeladas; fetch remoto indisponível | congelar outra fonte ou bloquear alegações | High | Resolved into Contract |
| `A-02` | presença estática demonstra somente existência; comportamento exige call path executável atual e teste/corroborante, mais schema efetivo somente quando persistence-backed | primeira crítica confirmou `distribution_state` sem consumidor observado e contratos concorrentes de assignment; evidence contract, DOD-01 e VAL-02 incorporam a restrição | sem alcance/supersessão resolvidos, classificar como partial, documented_only, conflicting ou unknown; nunca comportamento operacional | High | Resolved into Contract |

- **Resolved planning fact:** `central_whatsapp_independent_legacy_policy.md` não nomeia `whatsflow_v2`; a fronteira read-only específica deste estudo já é contratual no feature brief e neste TODO. Eventual política genérica permanece fora do ST-03.
- **Human reclassification validation:** usuário, `VALIDO RECLASSIFICAÇÃO A-01..A-03 COMO FATOS CONTRATUAIS SEM MUDANÇA DE ESCOPO`, conversa de 2026-09-25.

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces

- Escrita: TODO, um artefato de análise e atualizações factuais de feature brief/backlog no closeout.
- Leitura: Foundation e snapshot congelado do `whatsflow_v2`; nenhum runtime ou segredo.

### Ordered Steps

1. Revalidar/fixar o manifesto Git e declarar allowlist de superfícies.
2. Resolver alcance/supersessão e call paths das fontes; resolver schema efetivo quando persistence-backed e marcar `not_applicable` nos demais casos.
3. Preencher a matriz única `C-01..C-12`, com evidência e estado.
4. Extrair relações, cardinalidades, invariantes, estados e fluxos sem fundir contratos conflitantes.
5. Executar os walkthroughs canônicos e a rubrica de concorrência/performance.
6. Formular recomendações e decisões futuras sem canonização ou prioridade.
7. Auditar rastreabilidade, conteúdo sensível, gates e closeout documental.

### Test Strategy

- **Strategy:** `not-applicable` para testes de produto; validação documental determinística e revisão bidirecional.
- **Why:** não há implementação nem mudança de runtime.
- **Fail-first targets:** `n/a`; inconsistência de fonte, cardinalidade ou cenário reprova a seção correspondente.

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Modelo conceitual ST-03 | no behavior changes now | n/a | n/a | no | no | scenario walkthroughs in study | análise somente leitura |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation lifecycle | TODO/análise/backlog/brief | estrutura e referências válidas | Foundation checkout | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | APROVADO/delivery | passed | exit `0`, 2026-09-25 | validação documental apenas |
| Markdown/git hygiene | documentação | diff bem formado | Foundation checkout | `git -C foundation_documentation diff --check` | delivery | passed | exit `0`, 2026-09-25 | sem testes de produto |

### Runtime / Rollout Notes

- `n/a`; estudo somente leitura, sem deploy, migração, feature flag ou canal real.

## Plan Review Gate

- **Status:** `findings_integrated`; revisão renovada contra `main@f3eed1fd`, com issue-card completeness corrigida após a terceira crítica.
- **Module coherence:** `passed`; o plano preserva a identidade de Setor/BU/Canal, a conversa por BU/contato, adapters de transporte, isolamento por Mantenedora/BU e histórico auditável.
- **Architecture:** `passed` — análise não canoniza nem altera contratos.
- **Code Quality:** `n/a` — nenhum código será escrito; o contrato exige evidência sanitizada e estados explícitos.
- **Tests:** `passed for planning` — walkthroughs e auditoria bidirecional cobrem a entrega documental.
- **Performance:** `passed for planning` — sem runtime; a rubrica analisa capacidade e concorrência como atributos conceituais.
- **Security:** `passed for planning` — legado read-only e exclusão de segredos/PII/payloads.
- **Elegance:** `passed` — doze conceitos usam uma única matriz, sem taxonomia paralela canônica.
- **Structural Soundness:** `passed` — descoberta, recomendação, decisão e implementação permanecem separadas.

### Issue Cards

- **Issue ID:** `ST03-CRIT-001`
  - **Severity:** `high`
  - **Evidence:** `distribution_state` sem consumidor observado e contratos concorrentes de assignment no snapshot congelado.
  - **Why it matters now:** presença estática poderia produzir um modelo operacional falso.
  - **Option A (Recommended):** exigir call path atual + teste/corroborante; schema efetivo somente quando persistence-backed; classificar histórico/superseded/orphaned/declarative.
    - **Effort / Risk / Blast radius / Maintenance:** medium / low / local / low.
    - **Performance / Elegance / Structural soundness:** neutral / improves / improves.
  - **Option B:** aceitar schema/UI como evidência suficiente, com disclaimer geral.
    - **Effort / Risk / Blast radius / Maintenance:** low / high / cross-module / high.
    - **Performance / Elegance / Structural soundness:** unknown / regresses / regresses.
  - **Option C (Do Nothing):** manter a inferência estática sem qualificação; rejeitada por permitir canonização de código morto.
    - **Effort / Risk / Blast radius / Maintenance:** none / high / cross-module / high.
    - **Performance / Elegance / Structural soundness:** unknown / regresses / regresses.
  - **Recommendation:** `Option A`, integrada no evidence contract, A-02, DOD-01 e VAL-02.

- **Issue ID:** `ST03-CRIT-002`
  - **Severity:** `high`
  - **Evidence:** snapshot inicial comprimia os doze invariantes em quatro resumos e omitia cenários negativos.
  - **Why it matters now:** recomendações poderiam violar idempotência, BU grants, capability do canal ou leitura histórica independente.
  - **Option A (Recommended):** matriz 1:1 dos doze invariantes com walkthroughs positivos/negativos e papéis/operações.
    - **Effort / Risk / Blast radius / Maintenance:** medium / low / cross-module / low.
    - **Performance / Elegance / Structural soundness:** neutral / improves / improves.
  - **Option B:** manter cross-check narrativo genérico no closeout.
    - **Effort / Risk / Blast radius / Maintenance:** low / high / cross-module / medium.
    - **Performance / Elegance / Structural soundness:** neutral / mixed / regresses.
  - **Option C (Do Nothing):** aceitar cobertura implícita; rejeitada por não ser auditável.
    - **Effort / Risk / Blast radius / Maintenance:** none / high / cross-module / high.
    - **Performance / Elegance / Structural soundness:** neutral / regresses / regresses.
  - **Recommendation:** `Option A`, integrada nas matrizes canônica e de baseline modular.

- **Issue ID:** `ST03-CRIT-003`
  - **Severity:** `medium`
  - **Evidence:** claim, capacity, transfer e polling do legado apresentam riscos concorrentes/escala sem rubrica original.
  - **Why it matters now:** PCV runtime `not_needed` não elimina performance/concorrência como objeto conceitual.
  - **Option A (Recommended):** rubrica documental para atomic claim, capacidade, corridas, presença, paginação, SLA e fan-out.
    - **Effort / Risk / Blast radius / Maintenance:** medium / low / local / low.
    - **Performance / Elegance / Structural soundness:** improves / improves / improves.
  - **Option B:** registrar apenas observações livres no estudo.
    - **Effort / Risk / Blast radius / Maintenance:** low / medium / local / medium.
    - **Performance / Elegance / Structural soundness:** unknown / mixed / mixed.
  - **Option C (Do Nothing):** omitir os riscos; rejeitada por degradar utilidade operacional.
    - **Effort / Risk / Blast radius / Maintenance:** none / high / local / high.
    - **Performance / Elegance / Structural soundness:** regresses / regresses / regresses.
  - **Recommendation:** `Option A`, sem ativar load tests ou lanes runtime.

- **Issue ID:** `ST03-CRIT-004`
  - **Severity:** `medium`
  - **Evidence:** scope, DoD e plano usavam agrupamentos conceituais concorrentes e evidência agregada.
  - **Why it matters now:** conceitos poderiam desaparecer sem que a auditoria bidirecional detectasse.
  - **Option A (Recommended):** catálogo estável `C-01..C-12`, uma matriz crosswalk e evidência planejada por critério.
    - **Effort / Risk / Blast radius / Maintenance:** medium / low / local / low.
    - **Performance / Elegance / Structural soundness:** neutral / improves / improves.
  - **Option B:** manter listas paralelas e reconciliar manualmente no closeout.
    - **Effort / Risk / Blast radius / Maintenance:** low-now/high-later / medium / local / high.
    - **Performance / Elegance / Structural soundness:** neutral / regresses / regresses.
  - **Option C (Do Nothing):** aceitar cobertura subjetiva; rejeitada por impedir prova de completude.
    - **Effort / Risk / Blast radius / Maintenance:** none / high / local / high.
    - **Performance / Elegance / Structural soundness:** neutral / regresses / regresses.
  - **Recommendation:** `Option A`, integrada no catálogo e Completion Evidence Matrix.

### Failure Modes & Edge Cases

- [ ] Confundir canal/provedor, BU/número e unidade de atendimento.
- [ ] Tratar código/documentação conflitante do legado como verdade única.
- [ ] Tratar migration, configuração ou UI órfã/supersedida como comportamento operacional.
- [ ] Projetar vazamento entre Mantenedoras/BUs ou acesso implícito por ausência de associação.
- [ ] Omitir claim concorrente, capacidade esgotada, presença obsoleta, transferência/handoff e retorno à fila.
- [ ] Transformar recomendação do estudo em arquitetura aprovada.

### Residual Unknowns / Risks

- [ ] O comportamento real de distribuição pode divergir do schema/UI e deve ser classificado por evidência, não presumido.

## Audit Trigger Matrix

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | estudo cross-module com uma entrega documental |
| `blast_radius` | `cross-module` | quatro módulos conceituais, sem mudança canônica |
| `behavioral_change_or_bugfix` | `no` | nenhuma mudança de produto |
| `changes_public_contract` | `no` | recomendações não são contratos |
| `touches_auth_or_tenant` | `no` | analisa, mas não altera autorização/tenancy |
| `touches_runtime_or_infra` | `no` | legado e produto somente leitura |
| `touches_tests` | `no` | validação documental |
| `critical_user_journey` | `no` | nenhum fluxo entregue agora |
| `release_or_promotion_critical` | `no` | sem release de produto |
| `high_severity_plan_review_issue` | `yes` | `ST03-CRIT-001` e `ST03-CRIT-002` foram high e estão integrados; severidade histórica permanece visível |
| `explicit_three_lane_request` | `no` | não solicitado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** complexidade medium e blast radius cross-module exigem crítica expandida antes de `APROVADO`.
- **Canonical method:** `wf-docker-independent-critique-method`
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** governing TODO at pushed baseline, current domain entities and four module anchors.
- **Review routing:** `codex / formal-review / formal-reviewer / critique / gpt-5.6-sol / max / declared`
- **Critique status:** `findings_integrated`
- **Internal reviewer mandate:** `required`
- **Findings summary:** rodadas 1–2 convergiram o contrato técnico; rodada 3 confirmou todas as correções e apontou apenas campos ausentes nas opções C (`ST03-CRIT-R3-001`), agora integrados sem mudança material.
- **Evidence / reference:** dispatches `critique-dispatch.json`, `critique-round-2-dispatch.json` e `critique-round-3-dispatch.json`; três reviewers frescos; audit floor `75992daf3f8f`.

### Historical Critique Round 1 Resolution

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `ST03-CRIT-001` | Integrated | useful | yes | paced | n/a | evidence contract, A-02, DOD-01 and VAL-02 now distinguish existence, effective behavior, supersession and orphaned artifacts |
| `ST03-CRIT-002` | Integrated | useful | yes | project | n/a | canonical invariant matrix and 1:1 module snapshot cover all twelve module invariants |
| `ST03-CRIT-003` | Integrated | useful | partial | paced | n/a | documentary concurrency/performance rubric added while runtime PCV remains correctly not needed |
| `ST03-CRIT-004` | Integrated | useful | partial | project | n/a | stable `C-01..C-12` catalog and per-criterion evidence matrix replace parallel coverage lists |

- **Human integration validation:** usuário, `VALIDO INTEGRAÇÃO ST03-CRIT-001..004 SEM NOVAS DECISÕES`, conversa de 2026-09-25.

### Historical Critique Round 2 Resolution

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `ST03-CRIT-R2-001` | Integrated | useful | yes | paced | n/a | schema agora é obrigatório somente para alegações persistence-backed; call path executável + teste/corroborante sustenta comportamento não persistente |
| `ST03-CRIT-R2-002` | Integrated | useful | yes | paced | n/a | issue cards passam a carregar adjudicação completa e o trigger high reflete a severidade histórica real |

- **Human integration validation:** usuário, `VALIDO INTEGRAÇÃO ST03-CRIT-R2-001..002 SEM NOVAS DECISÕES`, conversa de 2026-09-25.

### Historical Critique Round 3 Resolution

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `ST03-CRIT-R3-001` | Integrated | useful | yes | paced | n/a | todas as Option C agora registram esforço, risco, blast radius, manutenção, performance, elegância e structural soundness; nenhuma seção material mudou |

## Gate: Assumption Code Coherence

- **Gate decision:** `not_needed`
- **Why this decision:** após as críticas e revalidações, A-01 e A-02 foram incorporadas ao manifesto/evidence contract; nenhuma premissa de código permanece viva.
- **Trigger stage:** `after critique convergence and before APROVADO`.
- **Guard scope:** `none`.
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md`.
- **Gate status:** `no_material_findings`
- **Findings summary:** nenhuma premissa viva; tentativas iniciais `no-go` levaram à classificação correta de A-01/A-02 como contrato resolvido e A-03 como fato documental.
- **Evidence / reference:** `foundation_documentation/artifacts/tmp/st03-planning-review/assumption-code-coherence.json`; rerun final após convergência da terceira crítica.
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** usuário, `APROVADO`, conversa de 2026-09-25.
- **Approval scope:** executar as sete etapas do estudo documental ST-03 no snapshot congelado, produzindo o artefato conceitual e atualizações factuais de TODO/backlog/feature brief.
- **Execution not authorized by approval:** product code, canonicalization, legacy mutation and ST-04 prioritization.
- **Renewed approval required when:** material scope, validation, decisions, risk or diff boundary changes.

## Rules Acknowledgement / Ingestion

As fontes abaixo foram recarregadas após `APROVADO` e vinculadas ao escopo documental aprovado antes da execução.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | governa autoridade, baseline, execução e evidência do TODO | escopo aprovado, single-writer e gates por fase | implementar antes de aprovação ou ampliar escopo silenciosamente | bloquear execução até approval evidence, reload e authority guard normal |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | roteia o TODO do approval ao closeout | máquina de estados e mesmo TODO governante | pular execution/delivery/closeout gates | carregar somente a fase aplicável e manter transições explícitas |
| `delphi-ai/workflows/docker/todo-execution-boundary-method.md` | governará o estudo documental após aprovação | snapshot read-only, limites elásticos e diff contract | mutar legado, produto ou cânone | revalidar manifesto e executar apenas as sete etapas aprovadas |
| `delphi-ai/workflows/docker/todo-delivery-gates-method.md` | governará evidência e revisão antes da entrega | matriz por critério, guards e auditorias derivadas | aceitar evidência agregada ou concluir com dívida oculta | preencher DOD/VAL, CI-equivalent documental e revisões finais |
| `delphi-ai/workflows/docker/todo-closeout-promotion-method.md` | governará consolidação e encerramento | handoff factual para ST-04 sem canonização | deixar TODO entregue em active ou promover recomendações como decisões | validar closeout, mover para completed e atualizar backlog/brief |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Subagent / delegation authorization:** `authorized by APROVADO for the predeclared routine-executor handoff under the mandatory execution workflow`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`

## Decision Adherence Validation

| Decision ID | Status | Evidence |
| --- | --- | --- |
| `D-01` | Adherent | manifesto usa exclusivamente o objeto local congelado `3a36436c83ebefc6839380eb8fac1a6f13f4700a`; `cfe0aa12` aparece apenas como landmark e nenhuma frescura remota é alegada |
| `D-02` | Adherent | matriz C-04/C-06/C-07/C-08/C-09 separa unidade/equipe, fila, política, capacidade, atendimento humano/automação e transferência |
| `D-03` | Adherent | diagrama, glossário e recomendações preservam Setor, BU e Canal; termos novos permanecem hipóteses/future decisions, sem canonização |

## Module Decision Consistency Validation

| Module Decision Ref | Delivery Status | Evidence |
| --- | --- | --- |
| `domain_entities.md#Core vocabulary` | Preserved | modelo e glossário mantêm Setor como agrupador, BU como número/unidade e Canal como transporte |
| `inbox-and-conversations.md#Invariants-1` | Preserved | walkthrough conversa BU/contato independente de transporte |
| `inbox-and-conversations.md#Invariants-2` | Preserved | walkthrough de replay/reordenação mantém idempotência como requisito, sem alegá-la no legado |
| `inbox-and-conversations.md#Invariants-3` | Preserved | walkthrough exige janela/capability e rejeita fallback silencioso |
| `integrations-and-channels.md#Invariants-1` | Preserved | C-01 mantém provider como adapter, separado de fila/assignment |
| `integrations-and-channels.md#Invariants-2` | Preserved | scan sanitizado e artefato sem valores sensíveis, payloads ou dumps |
| `integrations-and-channels.md#Invariants-3` | Preserved | E-12 é anti-padrão legado; recomendação exige erro determinístico |
| `identity-and-tenancy.md#Invariants-1` | Preserved | cenários mantêm tenant/account resolvido antes das operações |
| `identity-and-tenancy.md#Invariants-2` | Preserved | C-04/C-05 negam que membership ou department substituam grant da BU |
| `identity-and-tenancy.md#Invariants-3` | Preserved | walkthrough mantém `OWNER`, `ADMIN`, `ATENDENTE`; papéis legados não são mapeados |
| `audit-and-history.md#Invariants-1` | Preserved | eventos append-oriented são requisito/recomendação, não comportamento legado presumido |
| `audit-and-history.md#Invariants-2` | Preserved | C-12 exige tenant/BU scope e negativos cross-tenant/cross-BU |
| `audit-and-history.md#Invariants-3` | Preserved | C-05/C-12 separam permissão de leitura de operação/escrita |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| ST-03 documentary checkpoint | correctness/contract and CI/evidence integrity | pending | próximo checkpoint commit ainda inexistente; pacote = TODO + estudo + diff | P1/P2 abaixo | required before final review |

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `ST03-P1-evidence-supersession` | P1 | release-blocker | corrigido no mesmo TODO; exige re-review | E-03/E-17/E-18 e C-02/C-03 | integrated / pending re-review | ST-03 checkpoint pending |
| `ST03-P2-scope-and-auth-evidence` | P2 | release-blocker | corrigido no mesmo TODO; exige re-review | webhooks/router/sector matrix, ausência e actor×operação | integrated / pending re-review | ST-03 checkpoint pending |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| TODO authority and read-only legacy boundary | hidden canonization, copied legacy code/data, product or legacy mutation | pending | final diff + legacy status | pending | execute after P1/P2 sweep |
| Evidence contract | static presence presented as runtime, unresolved supersession, broad absence claims | pending | C/E matrix and TQA R4 | pending | execute after P1/P2 sweep |

## Security Risk Assessment

- **Risk level:** `low`
- **Why this risk level:** leitura de legado pode expor material sensível se a allowlist for ignorada; nenhum runtime muda.
- **Attack surface in scope:** somente risco documental de segredo/PII.
- **Attack simulation decision:** `not_needed`
- **Review evidence:** revisão de conteúdo sensível planejada em `VAL-05`.
- **Residual security risk:** evidência estática deve permanecer resumida e sanitizada.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `none`
- **Why this level:** nenhuma query, runtime, fila ou UI será alterada.
- **Current delivery stage at review time:** `Pending`

| Policy Schema Version | Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Trigger Rationale | Gate Deadline | Minimum Evidence Rule ID | State | Residual Risk | Uncertainty Reason Code | Recorded At UTC | Executor ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pcv-1` | `EPS` | endpoint-performance-scrutiny | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | estudo documental; nenhum endpoint, lookup, query shape ou data path foi alterado | `before_local_implemented` | `EPS-E1` | `not_applicable` | none | none | `2026-09-25T18:30:26Z` | `codex:/root/st03_documentary_executor` |
| `pcv-1` | `FRC` | frontend-race-condition-validation | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | estudo documental; nenhuma superfície async de UI foi alterada | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | none | none | `2026-09-25T18:30:26Z` | `codex:/root/st03_documentary_executor` |
| `pcv-1` | `BCI` | backend-concurrency-idempotency-validation | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | estudo documental; nenhuma mutação ou semântica de concorrência do produto foi alterada | `before_local_implemented` | `BCI-INV` | `not_applicable` | none | none | `2026-09-25T18:30:26Z` | `codex:/root/st03_documentary_executor` |
| `pcv-1` | `RLS` | runtime-load-stress-validation | `not_needed` | low | `n/a — pcv-1 has no negative reason code` | estudo documental; nenhum runtime, workload, SLO ou topologia foi alterado | `before_production_ready` | `RLS-E1` | `not_applicable` | none | none | `2026-09-25T18:30:26Z` | `codex:/root/st03_documentary_executor` |

- **PCV schema gap:** `pcv-1` não define reason codes negativos; `n/a` explícito evita atribuir falsamente um trigger positivo. A concorrência permanece objeto analítico do estudo, sem ativar lanes de runtime.

## Verification Debt Assessment

- **Audit outcome:** `pending required audit`
- **Why this outcome:** o audit floor exige `verification-debt-audit` antes de concluir um TODO medium.
- **Inline code TODO debt:** `none`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none yet`

## Independent Test Quality Audit Gate

- **Audit decision:** `recommended`
- **Why this decision:** validação documental não altera testes, mas a complexidade medium recomenda auditoria focada da qualidade das evidências.
- **Audit status:** `findings_integrated`
- **Audit focus:** eficácia da validação documental e rastreabilidade dos cenários.
- **Findings received:** `ST03-TQA-001`, `ST03-TQA-002`, `ST03-TQA-R2-001`, `ST03-TQA-R2-002`, `ST03-TQA-R3-001`.
- **Rerun status:** `pending`; a correção posterior invalida o clean anterior.
- **Embedded R4 result (historical, non-green now):** reviewer `/root/st03_test_quality_reaudit_r4`; pacote/checkpoint então revisado: TODO+estudo antes desta onda; resultado `clean/no_material_findings`; verificação 1:1 cobriu `ST03-TQA-001`, `002`, `R2-001`, `R2-002`, `R3-001`. Este resultado não é evidência da onda atual e não depende de dispatch externo.

| Finding ID | Evidence | Resolution integrated | Status |
| --- | --- | --- | --- |
| `ST03-TQA-001` | Cada linha C-01..C-12 precisava de referência congelada exata, e ausências precisavam registrar busca/escopo reproduzível. | O artefato recebeu o registro `E-01..E-10` com `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:path:symbol-or-lines`; cada C cita seus `E-xx`. `E-NF-01` fixa o comando, escopo e resultado limitado de `not_found_after_protocol`. | integrated; verified clean in R4 |
| `ST03-TQA-002` | C-04 não distinguia cenário positivo de negativo para unidade/equipe. | C-04 agora exige positivamente membership da unidade **e** grant da BU e nega explicitamente view/claim por membership isolado ou coincidência de `department_id`. | integrated; verified clean in R4 |
| `ST03-TQA-R2-001` | E-06 agrupava canSend, diálogo e transferências e fazia a persistência estática parecer prova runtime/atômica. | E-06 foi repartida em `E-06a..d` com as linhas verificadas do blob; `E-13` isola o upsert de assignment. C-08, C-09 e C-12 agora distinguem caminho UI, fonte estática e ausência de CAS/atomicidade runtime. | integrated; verified clean in R4 |
| `ST03-TQA-R2-002` | A ausência de presença/capacidade podia incluir indevidamente presença de provider, e a busca admitia corpus documental amplo. | `E-11` registra provider-presence efetivo; `E-12` registra o fallback/catch silencioso como limitation/anti-pattern. `E-NF-01` agora usa vocabulário de distribuição/atendente, allowlist sanitizada e exclui explicitamente corpus bruto; a ausência se limita a scheduler/claim/capacidade/presença de atendente. | integrated; verified clean in R4 |
| `ST03-TQA-R3-001` | O estudo ainda omitia superfícies que montam dashboard/configuração e que leem/polling/upsertam `agent_status`, contagens e modos de distribuição. | Foram adicionados `E-14` (MensageriaPage), `E-15` (AgentDashboard) e `E-16` (DepartmentManager), e a allowlist de `E-NF-01` foi ampliada somente com esses caminhos sanitizados. C-07/C-08 e a rubrica registram status/contagem/modo como direto ou `declarative_only`, sem inferir scheduler, CAS, reserva, grant BU ou TTL/freshness. | integrated; verified clean in R4 |

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** baseline final do audit floor para uma entrega cross-module.
- **Final review status:** `not_run`
- **Review focus:** aderência, rastreabilidade, conclusões, riscos e ausência de canonização silenciosa.

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `not_needed`
- **Why this decision:** nenhum cutover, compatibilidade ou retirada de legado.
- **Cutover audit status:** `not_run`

## Module Consolidation Gate

- [ ] Confirmar no closeout que ST-03 não alterou módulos canônicos.
- [ ] Registrar no backlog/feature brief apenas o handoff factual para ST-04.
- [ ] Mover o TODO para `completed/features/` somente após evidências e guards.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** execução documental concluída no artefato; delivery gates, auditorias e closeout continuam pendentes e fora deste handoff.
- **Post-commit/push status:** `pending`
- **Next path/status action:** executar os delivery gates/auditorias autorizados e, somente então, decidir closeout; não mover este TODO nesta etapa.

## Commands (Run Locally)

- `git.exe -C 'C:/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2' status --short --branch`
- `git.exe -C 'C:/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2' rev-parse HEAD^{tree}`
- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- `git -C foundation_documentation diff --check`
- `git diff --check --no-index /dev/null foundation_documentation/artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-20260925.md` (aceitar exit `1` somente por arquivo novo e exigir stdout vazio)
- `git -C foundation_documentation diff --no-ext-diff 9cf4b1d110477fff12b557481d1ebdb223a1001f -- todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-20260925.md`
- `git -C foundation_documentation diff --no-ext-diff --check 9cf4b1d110477fff12b557481d1ebdb223a1001f -- todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md` (tracked range; o artefato novo usa o comando `--no-index` acima)
- `rg -n -i '(api[_-]?key|authorization:|bearer |secret|token|password|@[A-Za-z0-9._%+-]+)' foundation_documentation/artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-20260925.md foundation_documentation/todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md` (revisar somente ocorrências estruturais/sanitizadas; não persistir valores)

## Files Expected

- O `Diff Expectation Contract` é o inventário autoritativo.
