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
- **Next exact step:** publicar o baseline renovado e repetir os guards finais de scope drift e autoridade.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** o contrato foi enquadrado e permanece em revisão pré-aprovação; nenhuma execução do estudo está autorizada.
- **Exit condition:** decisões e plano congelados, gates de planejamento convergidos e aprovação explícita registrada.

## Scope

- [ ] Congelar um manifesto reprodutível do `whatsflow_v2` e registrar branch, commit, tree e superfícies admitidas.
- [ ] Preencher o catálogo conceitual `C-01..C-12` e sua matriz única de cobertura, sem criar uma taxonomia canônica do produto.
- [ ] Produzir diagrama conceitual, cardinalidades, glossário comparativo, invariantes, estados e transições.
- [ ] Confrontar cada conceito com Mantenedora, Setor, BU, Canal, Conversa, Usuário e auditoria do LeadsHug.
- [ ] Validar cenários de entrada, múltiplas BUs, fila livre, atribuição manual/automática, capacidade, transferência, SLA, automação/handoff e isolamento entre Mantenedoras.
- [ ] Registrar padrões aproveitáveis, limitações, inconsistências e anti-padrões do legado.
- [ ] Formular recomendações e decisões futuras sem atribuir prioridade ou autoridade de implementação.

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
| TODO e estudo ST-03 | `foundation_documentation:main@9cf4b1d` | `n/a` | `n/a` | `direct publication pending` | planning |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `foundation_documentation` | `main@9cf4b1d110477fff12b557481d1ebdb223a1001f` | `working_tree` |
| whatsflow_v2 | `C:/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2` | `origin/stage@3a36436c83ebefc6839380eb8fac1a6f13f4700a` | read-only frozen snapshot |

### Snapshot Manifest Contract

| Reference | Branch / Commit | Tree | Verified | Role |
| --- | --- | --- | --- | --- |
| primary evidence | `origin/stage@3a36436c83ebefc6839380eb8fac1a6f13f4700a` | `6befe605dda039a7066a7fd48403807ea93f8408` | fetch + clean status, 2026-09-25 | complete ST-03 inspection baseline |
| comparison landmark | `origin/main@cfe0aa120503687943ee81930172994a1ea9ab1a` | `d739d0a517651a4ed1621940c62e7a3107ee29ef` | fetch + ancestry/count, 2026-09-25 | demonstrates stage is 59 commits ahead; not a second study population |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md` | `A|M|D` | governing contract and later closeout move |
| Foundation | `artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-*.md` | `A|M` | study deliverable |
| Foundation | `backlog/README.md` | `M` | factual handoff and closeout state |
| Foundation | `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` | `M` | factual ST-03 handoff only |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| LeadsHug product repositories | `apps/**,packages/**,prisma/**,docker/**,.github/**` | `any` | study has no product implementation authority |
| whatsflow_v2 | `**` | `any` | reference is read-only |
| Foundation | `project_constitution.md,domain_entities.md,modules/**,contracts/**,decisions/**,system_roadmap.md` | `any` | canonization belongs to ST-04 or later approved TODO |
| Any repository | `.env*,**/secrets/**,**/*credential*,**/*token*` | `any` | sensitive material excluded |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)

Não aplicável enquanto nenhuma divergência existir; qualquer path não classificado exige análise e validação renovada.

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

- [ ] `DOD-01` Manifesto, alcance/supersessão e call paths tornam cada alegação operacional reprodutível; schema efetivo é exigido quando há persistência e `not_applicable` caso contrário; histórico, órfão e declarativo não são tratados como comportamento.
- [ ] `DOD-02` A matriz única `C-01..C-12` liga cada conceito a fontes, evidência, constraints, modelo, cenários, disposição e conclusão.
- [ ] `DOD-03` Diagrama e glossário separam transporte, BU, unidade de atendimento, equipe, fila, política, capacidade e atribuição.
- [ ] `DOD-04` Cardinalidades, invariantes e estados/transições cobrem o ciclo de atendimento e seus casos unknown/conflicting.
- [ ] `DOD-05` A matriz 1:1 de invariantes canônicos passa nos walkthroughs positivos e negativos previstos.
- [ ] `DOD-06` A rubrica documental de concorrência/performance cobre claim, capacidade, corridas, presença, filas, SLA e fan-out.
- [ ] `DOD-07` Padrões úteis, limitações e anti-padrões possuem evidência e não viram prescrição automática.
- [ ] `DOD-08` Recomendações indicam decisão futura, dependências e risco sem prioridade ou autorização.
- [ ] `DOD-09` Artefato não contém segredo, PII, payload real ou código legado copiado.
- [ ] `DOD-10` Validators, guards e revisões documentais aplicáveis passam antes do closeout.

## Validation Steps

- [ ] `VAL-01` Revalidar limpeza, branch, head, tree e ancestralidade do snapshot antes da execução.
- [ ] `VAL-02` Classificar alcance/supersessão e resolver schema efetivo apenas nas alegações persistence-backed — registrando `not_applicable` nas demais — antes da auditoria bidirecional `C-01..C-12`.
- [ ] `VAL-03` Executar todos os walkthroughs da matriz de invariantes, incluindo troca de transporte, replay/reordenação, falha/capability do provider e matriz de atores/operações.
- [ ] `VAL-04` Executar a rubrica de concorrência/performance com source evidence, invariant esperado e disposição explícita `pattern|limitation|anti_pattern|unknown`.
- [ ] `VAL-05` Revisar explicitamente segredos, PII, payloads e cópia indevida no diff final.
- [ ] `VAL-06` Executar validador estrutural, `git diff --check` e guards de autoridade, diff, conclusão e closeout aplicáveis.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01` | Definition of Done | evidência operacional distingue call path atual e schema persistence-backed de artefato histórico/órfão | doc+review | manifest + source classification | n/a | planned | schema obrigatório só com persistência; `not_applicable` explícito nos demais casos |
| `DOD-02` | Definition of Done | matriz única cobre `C-01..C-12` | doc+integrity review | concept coverage matrix | n/a | planned | 12/12 IDs e colunas obrigatórias |
| `DOD-03` | Definition of Done | diagrama/glossário separam os conceitos | doc+review | model sections | n/a | planned | sem colisão Setor/Canal/BU |
| `DOD-04` | Definition of Done | cardinalidades/estados cobrem conflitos e unknowns | doc+review | model sections | n/a | planned | sem coerência inventada |
| `DOD-05` | Definition of Done | invariantes canônicos cobertos 1:1 | scenario review | invariant matrix results | n/a | planned | inclui casos negativos e papéis |
| `DOD-06` | Definition of Done | rubrica concorrência/performance completa | scenario review | rubric results | n/a | planned | análise, sem load test |
| `DOD-07` | Definition of Done | patterns/limitations/anti-patterns fundamentados | doc+review | disposition column | n/a | planned | legado não vira prescrição |
| `DOD-08` | Definition of Done | recomendações sem prioridade/autoridade | doc+review | recommendation/future-decision column | n/a | planned | handoff apenas para ST-04 |
| `DOD-09` | Definition of Done | conteúdo sensível/cópia excluídos | scan+manual review | final diff review | Foundation diff | planned | sem garantia absoluta |
| `DOD-10` | Definition of Done | gates documentais passam | guard+review | validator/guards/reviews | Foundation | planned | closeout somente após tudo green |
| `VAL-01` | Validation Steps | snapshot revalidado | command | Git manifest commands | frozen reference | planned | branch pode avançar sem mover SHA |
| `VAL-02` | Validation Steps | alcance/supersessão e schema aplicável resolvidos antes da auditoria bidirecional | command+review | source classification + crosswalk | read-only | planned | itens unresolved viram partial/unknown; schema não aplicável é explícito |
| `VAL-03` | Validation Steps | walkthroughs dos invariantes | scenario review | invariant results | n/a | planned | positivos e negativos |
| `VAL-04` | Validation Steps | rubrica operacional | scenario review | concurrency/performance results | n/a | planned | source + expected invariant + disposition |
| `VAL-05` | Validation Steps | revisão sensível/cópia | scan+manual review | final diff | Foundation diff | planned | nenhum payload/dump persistido |
| `VAL-06` | Validation Steps | validators/guards | command | exact command outputs | Foundation | planned | inclui completion/closeout no final |

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| local `whatsflow_v2` Git snapshot | source of evidence | healthy | 2026-09-25 | `git.exe fetch/status/rev-parse/rev-list`; clean `stage`, local equals `origin/stage` | inspect frozen SHA; branches may advance without changing the study baseline |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality` for independent documentary critique/final review.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Assurance / Tester-Quality | desafiar o modelo, rastreabilidade e conclusões sem contexto prévio | TODO e estudo | planned |

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

- [x] `D-01` Usar `origin/stage@3a36436c83ebefc6839380eb8fac1a6f13f4700a` como fonte principal porque está 59 commits à frente de `origin/main`; manter `origin/main@cfe0aa12` apenas como marco de comparação. O fetch de 2026-09-25 confirmou os SHAs e trees congelados.
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
- **Baseline commit:** `pending renewed baseline after A-01..A-03 validation`
- **Baseline push reference:** `origin/main`
- **Gate status:** `not_run`
- **Findings summary:** reclassificação de A-01..A-03 validada; aguarda publicação da baseline renovada.
- **Evidence / reference:** validação humana registrada abaixo; `f3eed1fd` permanece como baseline histórica que detectou corretamente o drift.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impedir que integrações pós-crítica ampliem o estudo sem revalidação.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`.
- **Baseline source:** `Review Baseline Freeze -> pending renewed baseline after A-01..A-03 validation`.
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md`.
- **No-go handling rule:** return to review/revalidation; no automatic rollback.
- **Gate status:** `not_run`
- **Findings summary:** o único drift detectado contra `f3eed1fd` foi validado pelo usuário; aguarda nova baseline e rerun.
- **Evidence / reference:** checkpoint histórico em `foundation_documentation/artifacts/tmp/st03-planning-review/review-scope-drift.json`; validação humana registrada abaixo.
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] Validar conjuntamente `D-01..D-03`.
- [x] Revalidar a integração de `ST03-CRIT-001..004` sem novas decisões de produto.
- [x] Revalidar a integração de `ST03-CRIT-R2-001..002` sem novas decisões de produto.
- [x] Validar a reclassificação de `A-01..A-03` como fatos contratuais resolvidos, sem mudança de escopo ou novas decisões.
- [ ] Após revisão independente e guards de planejamento, registrar `APROVADO` para executar o estudo.

## Assumptions Preview (Required Before Plan Review)

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | o snapshot está limpo e pode ser estudado sem executar runtime | Git fetch/status: local `stage` = `origin/stage@3a36436`; manifesto registra head/tree e superfícies congeladas | congelar outra fonte ou bloquear alegações | High | Resolved into Contract |
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
| Foundation lifecycle | TODO/análise/backlog/brief | estrutura e referências válidas | Foundation checkout | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | APROVADO/delivery | planned | command | validação documental apenas |
| Markdown/git hygiene | documentação | diff bem formado | Foundation checkout | `git -C foundation_documentation diff --check` | delivery | planned | command | sem testes de produto |

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

- **Approved by:** `pending`
- **Approval scope:** `pending after D-01..D-03 and planning gates`
- **Execution not authorized by approval:** product code, canonicalization, legacy mutation and ST-04 prioritization.
- **Renewed approval required when:** material scope, validation, decisions, risk or diff boundary changes.

## Rules Acknowledgement / Ingestion

- `pending after APROVADO`; current framing used the feature-framing, lane-framing and TODO-contract-refinement methods.

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `todo-approval`
- **Selected role:** `primary-chat`
- **Selected model:** `inherited current model`
- **Selected effort:** `inherited current effort`
- **Proof mode:** `declared`
- **Subagent / delegation authorization:** `not-requested`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `pending`

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
- **Lane disposition:** `EPS`, `FRC`, `BCI` e `RLS` são `not_needed/not_applicable`; a concorrência é apenas objeto do modelo conceitual.

## Verification Debt Assessment

- **Audit outcome:** `pending required audit`
- **Why this outcome:** o audit floor exige `verification-debt-audit` antes de concluir um TODO medium.
- **Inline code TODO debt:** `none`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none yet`

## Independent Test Quality Audit Gate

- **Audit decision:** `recommended`
- **Why this decision:** validação documental não altera testes, mas a complexidade medium recomenda auditoria focada da qualidade das evidências.
- **Audit status:** `not_run`
- **Audit focus:** eficácia da validação documental e rastreabilidade dos cenários.

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
- **Disposition reason:** crítica e revalidações humanas convergiram; baseline renovada e guards finais ainda pendentes.
- **Post-commit/push status:** `pending`
- **Next path/status action:** publicar baseline renovada e repetir scope-drift/authority preflight.

## Commands (Run Locally)

- `git.exe -C 'C:/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2' status --short --branch`
- `git.exe -C 'C:/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2' rev-parse HEAD^{tree}`
- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- `git -C foundation_documentation diff --check`

## Files Expected

- O `Diff Expectation Contract` é o inventário autoritativo.

## COMENTÁRIO:

- O estudo começa somente após validação das três decisões, gates de planejamento e `APROVADO` explícito.
