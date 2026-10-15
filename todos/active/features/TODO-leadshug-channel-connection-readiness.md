# TODO LeadsHug — conexão verificável dos canais

## Quick Start

Rascunho do contrato ST-CON-01, criado de `delphi-ai/templates/todo_template.md` em 2026-10-15. Prioridade confirmada pelo usuário; implementação **não aprovada**. Preparação `prepared-pre-freeze`: ainda não houve freeze, review formal ou guard de aprovação deste contrato. Não executar produto a partir deste draft.

## Title

Conexão verificável dos canais oficial e não oficial do LeadsHug.

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Tactical state:** `Draft`
- **Prepared on:** 2026-10-15
- **Planning authorization:** concordância do usuário com a prioridade de conexões e preparo de testes; confirmação de disponibilidade dos dois canais. Não equivale a APROVADO do contrato.

## Context

A tela de números mostra estado salvo, mas o oficial é marcado CONECTADO após listar números da WABA e o não oficial depende do webhook. O método Evolution de consulta de estado existe sem consumidor. Os testes internos substituem os provedores externos. Precisamos tornar essa conexão verificável para que testes de atendimento representem operação real. Histórico do aparelho ainda não é importado e terá contratos seguintes.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md`
- **Primary story ID:** `ST-CON-01`
- **Why this is the right current slice:** um objetivo: conectar o número certo e conhecer seu estado real o suficiente para testar envio/recebimento. Importação tem identidade/data/efeitos próprios e fica em ST-CON-02/03.
- **Direct-to-TODO rationale:** n/a; enquadramento separado realizado.

## Contract Boundary

Este draft define a proposta da primeira entrega. Nenhum checkpoint do histórico anterior autoriza esta execução. O contrato deve ser refinado após confirmar ambiente, versão Evolution e modalidade da WABA, congelado, revisado e aprovado antes de tocar produto. Mudança material exige reconvergência; refinamento local só cabe no mesmo objetivo e aprovação.

## Implementation Intent

- **Current delivery:** diagnóstico e representação confiáveis da conexão dos canais existentes, com prova operacional separada.
- **Planned next steps:** ST-CON-02 importa histórico Evolution; ST-CON-03 resolve histórico oficial conforme capacidade comprovada. Transferência vem depois desta frente.
- **Anticipatory implementation authorized now:** none
- **Rationale:** conexão pode ser validada sem introduzir importador, sincronização de mensagens ou onboarding oficial novo.

## Delivery Status Canon (Required)

- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** confirmar ambiente/versão Evolution/modalidade oficial; fechar semântica e superfícies do contrato antes do freeze e das revisões.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** review
- **Why this state now:** elaboração do contrato e fechamento de dependências; nenhuma implementação iniciada.
- **Exit condition:** contrato concreto, dependências delimitadas, revisões/guardas exigidos aceitos e APROVADO do usuário.

## Scope

- [ ] SCOPE-01: definir identidade do número oficial explicitamente quando houver múltiplos números na WABA; confirmar BU correta, grants e vínculo de um canal por tipo.
- [ ] SCOPE-02: distinguir estado informado pelo provedor, momento da última verificação, indisponibilidade da verificação e prova operacional de mensagens. Consulta de WABA ou status no banco não equivale a teste ponta a ponta.
- [ ] SCOPE-03: permitir verificação administrativa explícita com timeout e orçamento bounded, sem alterar estado para conectado por erro ou ausência de resposta; não fazer I/O externo em listagem periódica.
- [ ] SCOPE-04: reconciliar consulta/evento com geração do vínculo e ordem de observações; resposta velha não pode reativar canal removido/substituído ou sobrescrever evento mais novo.
- [ ] SCOPE-05: validar QR inicial/renovação/repareamento, persistência da instância e recuperação após interrupção na versão Evolution admitida, com erros compreensíveis.
- [ ] SCOPE-06: acrescentar testes internos e fluxo browser de número/canal, preservando inbox e isolamento multi-tenant.
- [ ] SCOPE-07: fornecer procedimento reproduzível de teste real IN/OUT para cada canal, registrando resultado por canal e build; manter pendência explícita se o provedor não puder ser testado.

## Delivery Status Semantics

`Pending` até implementação e evidência; `Local-Implemented` exige matriz local aceita. Prova externa é registrada separadamente. `Production-Ready` e deploy não são limiares desta proposta.

## Active Work State Semantics

`review` neste draft significa preparação do contrato; não é afirmação de implementação concluída. `implementation` somente após aprovação e authority guard go.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; nenhuma entrega parcial reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

n/a no estágio de drafting. Dependências técnicas desconhecidas são explicitadas abaixo; se impedirem a execução de um gate real, registrar o bloqueio naquele gate.

## Execution Lane Tracking (Required)

- **Local implementation branches:** propostas futuras `feature/channel-connection-readiness` em API/Web; ainda não criadas. Foundation em main.
- **Promotion lane path:** implementação local após aprovação, validação local e prova externa no ambiente de testes confirmado; promoção remota de produto exige autorização separada.
- **Lane-promoted threshold for this TODO:** n/a
- **Production-ready threshold for this TODO:** não reivindicado.
- **Execution topology:** primary-checkout-single-writer
- **Git isolation authorization:** not-requested; worktrees/cópias auxiliares proibidos.
- **Subagent / delegation authorization:** workflow local requer executor serializado e reviewers independentes nas fases aplicáveis; nenhum agente de implementação despachado neste draft.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

n/a; esta proposta não autoriza promoção ou deploy.

## Out of Scope

- Importação/backfill do aparelho, MESSAGES_SET e dados históricos oficiais; ST-CON-02/03 terão contratos próprios.
- Embedded Signup/coexistência novos, migração de número, templates, campanhas, transferência, mídia binária e máquina de estados de entrega/leitura.
- Remover sessões/instâncias existentes do usuário para testar; testes destrutivos só em vínculo descartável explicitamente identificado.
- Integração com o legado, mudanças de gitlinks/.gitmodules, segredos versionados e alteração de ambiente de produção.
- Disparar automaticamente uma mensagem de teste ao clicar em verificar conexão. Troca real usa interlocutor definido e procedimento explícito.

## Diff Expectation Contract (Required Before Delivery)

- **Contract status:** required
- **Policy:** strict; unclassified or forbidden paths block delivery
- **Comparison mode:** working_tree
- **Draft qualification:** paths abaixo são candidatos; completar a lista exata e a baseline Foundation antes do freeze. Nenhuma permissão de edição de produto é concedida.

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| api | api-app | ae6a9662c29b77276351aa9de653a47276372246 | working_tree |
| web | web-app | 4e56f6c1f4515b918d05b8c87e890d42e8542c56 | working_tree |
| foundation | foundation_documentation | 6665aad58f9b04841df85d981bf89434b1164cdb | working_tree |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/domain/channels/** | A,M,?? | Estado, verificação e concorrência dos vínculos. |
| api | src/integrations/evolution/** | A,M,?? | Adapter da versão confirmada. |
| api | src/integrations/meta/** | A,M,?? | Identidade/capacidade do oficial e diagnóstico. |
| api | src/surfaces/bff/channels.controller.ts | M | Contratos administrativos. |
| api | src/surfaces/webhooks/evolution.controller.ts | M | Reconciliação de estado com evento. |
| api | test/*canais* | A,M,?? | Contratos/races e fixtures específicas. |
| api | test/webhooks.e2e-spec.ts | M | Contrato de evento. |
| web | src/telas/Numeros.tsx | M | Número, QR, estados e ação de verificação. |
| web | src/api.ts | M | Projeções tipadas. |
| web | e2e/*canais* | A,M,?? | Fluxo browser. |
| foundation | todos/active/features/TODO-leadshug-channel-connection-readiness.md | A,M,?? | Contrato e evidência. |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | A,M,?? | Enquadramento. |
| foundation | artifacts/validation-plans/leadshug-channel-readiness-20261015.md | A,M,?? | Cenários de validação. |
| foundation | artifacts/dependency-readiness.md | A,M,?? | Dependências verificáveis. |
| foundation | backlog/README.md | M | Prioridade confirmada. |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .env* | any | Segredos/configuração não pertencem ao diff de produto. |
| api | src/surfaces/public/** | any | API pública não é este contrato. |
| web | src/telas/Inbox.tsx | any | Histórico paginado já entregue. |
| foundation | todos/completed/** | any | Não reescrever história. |

Schema/migração, projeção em tenancy, wiring e bootstrap de testes podem ser necessários; seus paths exatos devem ser admitidos antes do freeze, após decidir persistência da observação. Esta lacuna explícita impede tratar o draft como aprovação-ready.

## Bounded But Elastic Guardrails

Somente concretizações de conexão/verificação no mesmo objetivo. Importação ou onboarding novo exigem contrato próprio; não absorver por conveniência técnica.

## Definition of Done

- [ ] DOD-01: seleção/identidade do número e permissões verificadas por contrato e fluxo browser.
- [ ] DOD-02: nenhum falso CONECTADO por mera listagem, timeout, resposta inválida ou resultado velho; conexão e saúde de verificação claramente distintas.
- [ ] DOD-03: polling/listagem sem fan-out externo, verificações bounded e races determinísticas protegidas.
- [ ] DOD-04: QR, estados/erros/retry e repareamento validados com browser/backend reais.
- [ ] DOD-05: matriz local CI-equivalent, segurança, concorrência, auditorias independentes e consolidação do módulo aceitas.
- [ ] DOD-06: prova real de IN/OUT e reconexão registrada por canal no target de teste confirmado. Se indisponível, nenhum claim de canal operacional ou closeout integral deste contrato.

## Validation Steps

- [ ] VAL-01: validar adapters com respostas da versão confirmada, múltiplos números, credencial recusada, timeout e payload inválido.
- [ ] VAL-02: E2E PostgreSQL com grant autorizado, papel insuficiente, outro tenant/BU; verificação e evento concorrentes, remoção/recriação enquanto consulta está pendente.
- [ ] VAL-03: Playwright contra build atual/backend real: selecionar número, parear, consultar estado, falhar/repetir sem falso sucesso e preservar contexto.
- [ ] VAL-04: executar matriz local API/Web em execução canônica serializada, com fonte/build servido identificados e banco isolado.
- [ ] VAL-05: executar checklist real de conexão, IN/OUT e interrupção/retomada por canal; registrar o que está ou não comprovado.
- [ ] VAL-06: concluir reviews/guardas de aderência, qualidade de testes, segurança, performance/dívida e consolidação antes de encerrar.

## Completion Evidence Matrix (Required Before Delivery Claim)

Nenhuma linha passed. Matriz por critério será completada na revisão do contrato; [plano de validação](../../../artifacts/validation-plans/leadshug-channel-readiness-20261015.md) define os sinais planejados e sua separação da prova real.

## External Dependency Readiness (Required When External Systems Matter)

Register: `foundation_documentation/artifacts/dependency-readiness.md`.

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Evolution de teste e versão | Endpoint/payload/sessão reais. | unknown | n/a | Versão, acesso e teste no target a confirmar. | Não adivinhar versão. |
| Meta/WABA de teste | Identidade e operação oficial. | unknown | n/a | Permissões, modalidade, número e callback. | Disponibilidade oferecida não é health check. |
| Números/interlocutores de teste | Prova IN/OUT. | unknown | n/a | Usuário confirmou disponibilidade dos dois em2026-10-15. | Confirmar target/destinatário sem publicar números pessoais. |
| Documentação oficial Meta | Semântica atual/eligibilidade. | rate-limited | 2026-10-15 | HTTP429 nas páginas de onboarding. | Reconsultar antes de congelar decisões dependentes. |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Current profile:** strategic-cto, elaboração e sequência; Genesis descartado por existência de canon/produto.
- **Primary execution profile:** operational-coder após aprovação.
- **Active technical scope:** nestjs, react, postgresql, prisma, docker
- **Expected supporting profiles:** operational-devops para target/callback; assurance-tester-quality e assurance-security-adversarial para gates aplicáveis.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log (Update when execution crosses profile boundaries)

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | Implementar somente contrato aprovado. | API/Web/canon owner | planned; nenhuma execução. |
| operational-coder | operational-devops | Configurar e provar callback/target de teste se necessário. | Runtime de teste explicitamente confirmado | planned; nenhuma infraestrutura alterada. |

## Complexity

- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section
- **Why this level:** dois providers, identidade de número, estado assíncrono, grants, browser e prova externa. Scope permanece uma história de conexão confiável.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:** identity-and-tenancy, inbox-and-conversations, audit-and-history.
- **Planned decision promotion targets:** integrations-and-channels: identidade, verificação de conexão, frescor/erros e limites operacionais.
- **Module decision consolidation targets:** mesmas seções, com evidência scoped por canal; não promover interpretação provisória de provider.

## Decision Pending (Resolve Before Freeze)

- [ ] D-01: fixar versão Evolution e contrato de payloads/consulta/configuração de webhook suportados.
- [ ] D-02: confirmar modalidade/WABA e política de seleção explícita do número; separar vínculo configurado, estado observado e prova IN/OUT.
- [ ] D-03: fechar persistência, frescor, prioridade de evento/consulta, geração de vínculo e resposta de erro sem mentir conexão.
- [ ] D-04: fixar budgets/timeouts/concurrency e contrato BFF administrativo; completar todos os paths previstos e testes.
- [ ] D-05: confirmar ambiente não produtivo, callbacks e interlocutores; decidir procedimento de interrupção sem remover canal real em uso.

## Decisions (Resolved Before Freeze)

Prioridade de planejamento confirmada. Decisões de implementação D-01..05 ainda abertas, nenhuma freeze claim.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| integrations-and-channels#invariants | Providers são adapters; segredos protegidos; erros determinísticos. | Preserve | módulo owner |
| project_constitution#system-invariants | BU/número e grants isolam operação; conversa unificada BU/contato. | Preserve | constituição |
| inbox-and-conversations#contrato-aprovado-da-timeline-da-inbox | Histórico paginado usa dado persistido, contexto e leitura protegidos. | Out of Scope | ST-ATT-01 concluído |

## Decision Baseline (Frozen Before Implementation)

`pending-freeze`: nenhuma decisão de implementação congelada neste draft.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Gate: Review Baseline Freeze

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Gate: Review Scope Drift

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Questions To Close

- [ ] Ambiente local ou Railway de testes, versão Evolution e acesso às suas rotas sem depender do legado.
- [ ] Número oficial já pertence à WABA? Modalidade de onboarding e número selecionado.
- [ ] Callback público de teste e interlocutor permitido para troca real.
- [ ] Resolver D-01..05 e completar review baseline + revisão/guardas antes de pedir APROVADO.

## Pattern References (Optional; Enforced When Cited)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Assumptions Preview (Required Before Plan Review)

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | O usuário pode disponibilizar ambos os canais. | Resposta nesta sessão em2026-10-15. | Ajustar gates externos; não mascarar com mocks. | High | Keep as Assumption |
| A-02 | O oficial atual usa WABA manual e primeiro número. | channels.service.ts:31-74 | Atualizar diagnóstico antes do freeze. | High | Keep as Assumption |
| A-03 | Não há reconciliação por connectionState no domínio. | Busca estadoDaInstancia em src retorna apenas adapter/interface. | Reavaliar owner existente antes de introduzir fluxo. | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

`prepared-pre-freeze`: plano candidato, subordinado às decisões ainda abertas.

### Touched Surfaces

ChannelsService, clients Meta/Evolution, controller BFF, estado do webhook e projeção usada por Numeros; testes locais/browser e módulo owner. Paths definitivos pendentes.

### Ordered Steps

1. Resolver D-01..05; completar diff/contratos/matriz; congelar e publicar baseline antes dos reviews/guards.
2. Obter decisões/critique independentes, auditar floor, coerência e drift; pedir APROVADO só com preflight-go.
3. Após aprovação, carregar regras e delegar implementação a executor único no checkout principal.
4. Provar falhas/races antes da correção; implementar adapter/domínio, estados UI e proteção de observações antigas.
5. Validar CI-equivalent e browser no target fresco; executar testes reais por canal.
6. Resolver aderência/TQA/final e guardas; consolidar módulo/artefatos e encerrar conforme limiar aprovado.

### Test Strategy

- **Strategy:** test-first após aprovação, com regressões de falso conectado/estado velho e readback de banco.
- **Why:** a lacuna é observável e não basta o endpoint retornar200.

### Pre-APROVADO RED Evidence Capture (Optional for bugfix/regression)

- **Decision:** not_needed
- **Why now:** diagnóstico por código basta para drafting; nenhum teste ou produto pode ser alterado neste estágio.
- **Status:** not_run

### Flow Evidence Planning Matrix (Required Before `APROVADO`)

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Número/QR/verificação/retry | Identidade e estado vistos pelo administrador. | web-only | Playwright mutation | yes | yes | Spec de canais e PostgreSQL isolado; build/servido conferidos. | n/a |
| IN/OUT e reconexão do provider | Canal precisa operar fora do harness. | web-only | Playwright mutation + prova externa | yes | yes | Checklist e readback do mesmo canal/número de teste. | n/a |

### Local CI-Equivalent Suite Matrix (Required Before `APROVADO` and Before Delivery Claim)

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API CI light | Domínio/adapters. | Tipos/build e regressões de status/erros. | Node22, dependências exatas. | npm run prisma:generate; npm run lint; npm run build; npm test | Local-Implemented | planned | nenhuma execução | Resolver runner canônico antes do run. |
| API E2E | Auth, persistência e races. | Negativas tenant/papel e resposta/evento concorrentes. | PG16 isolado, migrations, execução serial. | npm run test:e2e | Local-Implemented | planned | nenhuma execução | Provider substituído prova só contrato interno. |
| Web | Tela de conexão. | QR/estado/retry/contexto. | Bundle atual e backend/DB isolados. | npm test; npm run test:tela | Local-Implemented | planned | nenhuma execução | Reusar prova de freshness atual; não exigir Flutter. |
| Providers reais | Validade operacional. | Conexão, IN/OUT e recuperação. | Versão, conta/callback/destinatário confirmados. | Procedimento no plano de validação; comandos específicos após readiness. | Local-Implemented | planned | nenhuma execução | Não substituível por fake; não é CI externo. |

### Runtime / Rollout Notes

Não alterar ambiente real agora. Mudança de schema, se necessária, deve entrar no contrato com migração antes da aprovação. Sem gitlinks, mudança de configuração secreta ou deploy de produção.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Gate: Assumption Code Coherence

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Approval

- **Approved by:** none
- **Approval scope:** nenhum contrato de implementação aprovado.
- **Execution not authorized by approval:** toda implementação/runtime e envio real neste draft.
- **Renewed approval required when:** escopo, decisões, validação ou risco material mudarem após futura aprovação.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Decision Adherence Validation (Mandatory Before Delivery)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Pipeline/Copilot P1/P2 Preflight

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Rule-Spirit Anti-Pattern Hunt

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** draft do contrato; decisões materiais e revisão ainda pendentes.
- **Post-commit/push status:** n/a
- **Next path/status action:** refinar o mesmo TODO após confirmar dependências; não mover ou encerrar antes dos gates.

## Security Risk Assessment (Mandatory Before Delivery)

- **Risk level:** high
- **Why this risk level:** operação administrativa de canal, credenciais externas, callback e fronteira multi-tenant.
- **Attack surface in scope:** BFF, identificação do vínculo e webhook existente; não remover autenticação para diagnosticar.
- **Attack simulation decision:** required
- **Review evidence:** planned, nenhuma prova nova.
- **Residual security risk:** resposta de provider e URL de webhook podem conter segredo; projetar erro safe sem devolvê-los em texto bruto.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

Draft: risco material em verificação concorrente, evento vs consulta, reconnect e remoção/recriação. Classificar EPS/FRC/BCI/RLS e samples pelo schema pcv-1 antes do freeze; não autorizar fan-out externo em polling. Nenhuma medição executada.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Independent Cutover Integrity Audit Gate

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Module Consolidation Gate (Required Before `Completed`)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Commands (Run Locally)

Nenhum comando de produto autorizado. Runners e targets exatos devem ser fechados antes da execução. Leitura de código e checagem documental somente nesta fase.

## Files Expected (Compatibility Note)

O Diff Expectation Contract é a referência candidata; completar lacunas antes do freeze. Nenhum Files Expected paralelo concede novos paths.

## COMENTÁRIO:

Nenhum comentário de aprovação pendente foi tratado como APROVADO.
