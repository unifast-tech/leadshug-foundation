# Tactical TODO — ST-CON-05

## Title

LeadsHug — ST-CON-05: vendedor prepara e submete modelos oficiais

## Artifact Identity

- **Artifact type:** tactical_execution_contract
- **Status:** In-Progress
- **Version:** 1.1
- **Created:** 2026-10-19
- **Template provenance:** copied delphi-ai/templates/todo_template.md before refinement.

## Context
ST-CON-06 v1.3 foi entregue localmente: Channel textual abstrato, adapters Meta/Evolution por operação, resolver scoped, OutboundService comum, aceitação única e613testes no all93791, mais IN/OUT real dos dois canais. O contrato de templates consome essa base; a minuta/reviews de2026-10-19 são históricos, preservados no pacote anterior e no snapshot de origem. Esta v1.1 é planejamento novo, não aprovação de implementação.

O usuário quer preparar no LeadsHug a mensagem que usará para iniciar atendimentos e confirmou: **vendedor cria e envia diretamente para aprovação da Meta**, sem aprovação administrativa intermediária. A história entrega criar/salvar/pré-visualizar/submeter/consultar modelos textuais. Iniciar conversa e enviar o template ao contato continuam no ST-CON-04, depois deste catálogo. Rascunho, solicitação aceita e modelo aprovado são estados distintos.

## Framing Source & Story Slice

- **Feature brief:** foundation_documentation/artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md
- **Primary story ID:** ST-CON-05
- **Why this is the right current slice:** resolve a preparação do recurso oficial antes de Nova conversa ST-CON-04, mantendo um objetivo e owner primário de integrações.
- **Direct-to-TODO rationale (required when `Feature brief = direct-to-todo`):** n/a; programa já enquadrado, ampliação registrada no brief.

## Contract Boundary

- This TODO defines **WHAT** must be delivered and what counts as done.
- `Assumptions Preview` and `Execution Plan` below define **HOW** Delphi currently intends to deliver this contract.
- This TODO is **bounded but elastic**: Delphi may absorb local discoveries only while they remain inside the same primary objective and the same main approval/review/promotion conversation. Secondary modules may still be touched when they are subordinate to that same slice.
- If any assumption or plan step changes `Scope`, `Out of Scope`, `Definition of Done`, required validation semantics, public contract, or frozen decisions, update the TODO contract first and request renewed approval before execution continues.
- If the intended path explicitly authorizes a compatibility shim, fallback bridge, dual-read/dual-write period, or another non-canonical temporary construct, record that authorization in the TODO with exact scope, rationale, and removal/closeout condition. Reviewers must be able to distinguish an approved temporary exception from accidental workaround drift.

## Implementation Intent

- **Current delivery:** Modelos de mensagem no LeadsHug: vendedor rascunha e submete texto oficial com variáveis/exemplos, acompanha aprovação e consulta catálogo scoped da conta.
- **Planned next steps:** reconvergir ST-CON-04 para consumir o mesmo catálogo/projetor e iniciar conversa; histórico e Railway depois.
- **Anticipatory implementation authorized now:** none
- **Rationale:** template é ativo da Messaging account; rascunho local tem autor, submissão é durável e estado de aprovação pertence à Meta. Não implementar sender/conversa agora.

## Delivery Status Canon (Required)
- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** CP05 liberado ao mesmo executor único após terminal CP04 final5 (282unit;375/376PG; buffer assert residual). Implementar consumidor Web e provas R25/R26; validar pacote consolidado via all antes de assurance/ativação/prova assistida. CP04 não declarado GREEN.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** implementation
- **Why this state now:** APROVADO v1.1 recebido2026-10-21; binding rules recarregadas e admissão inicial confirma3HEADs/41hashes da base revisada antes de qualquer código/teste.
- **Exit condition:** SCOPE/DOD/VAL e gates derivados satisfeitos, incluindo testes reais PG/browser, assurance e prova assistida; sem antecipar entrega antes das evidências.

## Scope

- [ ] SCOPE-01 — Página autenticada Modelos de mensagem, com BU/canal oficial explícitos, listagem dos próprios rascunhos, editor textual com variáveis/exemplos e prévia.
- [ ] SCOPE-02 — Vendedor ATENDENTE+ cria/edita seus rascunhos e envia para análise da Meta, sem aprovação de ADMIN intermediária; ADMIN/OWNER da BU pode administrar rascunhos locais da mesma BU.
- [ ] SCOPE-03 — Capacidade abstrata estreita de gerenciamento de templates, separada de Channel.sendMessage; submissão oficial scoped, revisionada/idempotente, reserva de nome por conta/idioma e recuperação de resultado incerto sem repetir POST automaticamente; criptografia/segredos atuais preservados.
- [ ] SCOPE-04 — Atualização explícita de status/catálogo da Messaging account correta; aprovado/pendente/recusado/pausado/desativado/indisponível com evidência de consulta; somente APPROVED suportado pode ser indicado como apto para uso futuro.
- [ ] SCOPE-05 — Harness de dependências/capacidade e testes de domínio/contrato/concorrência PostgreSQL, Playwright contra BFF real e prova de criação/consulta em recurso oficial próprio, sem envio a destinatário; consolidação do contrato e revisões derivadas.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; sem entrega reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

Planejamento não bloqueado. O operador ainda não possui template aprovado; a própria capacidade de criar/submeter é esta história. Aprovação externa pode ser recusada/demorada e não pode ser simulada. Primeiro envio físico pertence ao ST-CON-04 e depende de recurso elegível.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `api-app:feature/number-onboarding`, `web-app:feature/number-onboarding`, `root:feature/number-onboarding`; confirmar nomes no handoff antes de editar; Foundation:main.
- **Promotion lane path:** local feature → dev → stage → main; apenas documentação Foundation main possui publicação autônoma nesta etapa.
- **Lane-promoted threshold for this TODO:** dev, fora da autorização local atual.
- **Production-ready threshold for this TODO:** main e gates operacionais próprios; nenhum deploy/push de produto autorizado agora.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

n/a nesta preparação; apenas Foundation main pode receber commits/push documentais autônomos, nenhum produto/deploy promovido.

## Out of Scope

- [ ] Primeiro envio de mensagem/conversa, campanha, disparo em lote, CRM, importação de histórico, handover/standby e modificação de roteamento.
- [ ] Modelos de mídia/botões/OTP/Flows/carrossel, editor multilíngue, recurso de IA para redigir/aprovar ou alteração/exclusão/apelação de templates já submetidos na Meta.
- [ ] Webhook novo de status, cron/polling em background, filas/outbox e plataforma genérica de operações; atualização será explícita e limitada.
- [ ] Mudança do gate de envio de mensagens ST-CON-01, nova credencial manual, token no browser/log, leitura de .env.testing ou modificação Meta durante planejamento.
- [ ] Railway/deploy/push de produto, worktrees/cópias, gitlinks/.gitmodules manuais, alteração Delphi e qualquer leitura/listagem/stat/hash/mount de api-app/.local-files.

## Diff Expectation Contract

- **Contract status:** required
- **Policy:** strict; unclassified or forbidden paths block delivery
- **User validation:** required on deviation
- **Comparison mode:** working_tree

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| root | . | 80e3940126f22a941f90dba4f5e801b6c0eb2f58 | working_tree |
| api | api-app | db5a86758a165fac8a1ab587599c37b17890530c | working_tree |
| web | web-app | 74b9d4b714044829796f875d00553f077c1c329d | working_tree |
| foundation | foundation_documentation | 83ed072337330465f4be3b5ced739b461e33b602 | working_tree |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/domain/message-templates/** | any | owner de rascunho/revisão/operacao/catalogo e ports estreitos de domínio, contratos/fake/harness |
| api | src/integrations/message-templates/** | any | resolver/factories/registro por operação e composição DI da capacidade, sem alterar Channel textual |
| api | src/integrations/meta/message-template*.ts | A, ?? | client HTTP de templates e raw specs dedicados, separado do contrato MetaClient existente |
| api | src/surfaces/bff/message-templates.controller.ts | A, ?? | adapter BFF sessão/CSRF/escopo |
| api | src/surfaces/bff/bff.module.ts | M | import da composição de templates e controller/serviços, mantendo ChannelTransportModule |
| api | src/domain/historico/catalogo.ts | M | companion validado pelo usuário em2026-10-21:4 ações de modelos no registro existente, frases fixas e escopo BU; sem texto/exemplos/segredos |
| api | src/domain/historico/cobertura.ts | M | companion validado pelo usuário em2026-10-21:classificar7 novas rotas;4 mutações rastreadas e3 consultas isentas com justificativa, guardião existente intocado |
| api | src/domain/channels/channel-credential-resolver.ts | M | propósito template-management explícito, mesmo owner crypto; send/verify/registration preservados |
| api | src/domain/channels/channel-credential-resolver.spec.ts | any | negativas do novo propósito e regressões dos propósitos existentes |
| api | prisma/schema.prisma | M | somente modelos/índices/FKs da jornada de templates; índice/ST06 intocados |
| api | prisma/migrations/*_message_template*/migration.sql | A, ?? | migration aditiva de templates, sem reset |
| api | test/message-template* | any | contratos HTTP/PG/capacidade/fake/tenant/recuperação |
| api | test/helpers.ts | M | fake externo da nova porta/DI, sem mudar semântica dos fakes textuais existentes |
| api | test/timeline-fixtures.cjs | M | provider de templates determinístico para browser real |
| api | test/browser-server.cjs | M | injeção/bootstrap de templates e fixtures explícitas |
| api | test/number-onboarding-pcv.e2e-spec.ts | M | herança PERF-R4-01: corrigir precisão de métricas do teste existente ao revalidar impacto de novos índices; sem alterar query/produtoST06 |
| web | src/telas/Modelos* | any | página/editor/listas/status e testes locais |
| web | src/componentes/Modelo* | any | componentes locais da mesma jornada, se necessários |
| web | src/messageTemplates* | any | DTO/state/freshness/projeção seguros da jornada |
| web | src/api.ts | M | wrappers/erro de templates sem regredir outcome de mensagens |
| web | src/api.spec.ts | M | companion para metadados seguros e erro compartilhado afetados |
| web | src/App.tsx | M | item/rota Modelos em Cadastros disponíveis ao vendedor |
| web | e2e/message-templates* | any | Playwright real BFF/PostgreSQL da jornada |
| web | e2e/number-onboarding-freshness.ts | M | companion de manifesto público/fonte-servido se necessário, sem varredura privada |
| web | e2e/timeline-freshness.ts | M | companion invocado por browser regressivo se necessário; somente inventário positivo |
| root | .github/workflows/ci.yml | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| root | scripts/test-channels-local.sh | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| root | scripts/check-channels-ci-parity.py | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/domain/inbox/conversations.service.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/domain/inbox/incoming.service.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/domain/inbox/incoming.typebot.integration.spec.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/evolution/evolution.client.spec.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/evolution/evolution.client.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/meta/meta.client.spec.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/meta/meta.client.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/surfaces/bff/conversations.controller.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/surfaces/public/conversations.controller.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/surfaces/public/public.module.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/surfaces/webhooks/webhooks.module.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | test/api-publica.e2e-spec.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | test/number-onboarding-typebot.e2e-spec.ts | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | prisma/migrations/20261020170000_message_inbound_window_index/migration.sql | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/domain/channels/transport/channel-dependencies.spec.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/domain/channels/transport/channel.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/domain/inbox/outbound.service.spec.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/domain/inbox/outbound.service.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/channels/channel-adapter-factory.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/channels/channel-adapter-registry.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/channels/channel-transport.module.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/channels/evolution-channel.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/channels/meta-channel.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | src/integrations/channels/prisma-channel-resolver.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| api | test/channel-transport.e2e-spec.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| web | src/telas/Inbox.tsx | M | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| web | e2e/channel-transport.spec.ts | A, ?? | Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json |
| foundation | todos/active/features/TODO-leadshug-official-template-authoring.md | M | contrato v1.1 e evidências |
| foundation | todos/completed/features/TODO-leadshug-official-template-authoring.md | A, ?? | closeout somente depois de gates |
| foundation | todos/active/features/TODO-leadshug-start-conversation-by-contact.md | M | handoff, sem execução antecipada |
| foundation | artifacts/reviews/leadshug-template-authoring-20261020/** | any | pacote/evidência v1.1, originais anteriores imutáveis |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | ponte factual de sequência |
| foundation | backlog/README.md | M | próximo gate do candidato |
| foundation | artifacts/dependency-readiness.md | M | readiness pontual, sem secrets |
| foundation | modules/integrations-and-channels.md | M | consolidação estável após entrega |
| foundation | modules/inbox-and-conversations.md | M | referência futura ao catálogo; sem claim04 |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .local-files/** | any | privado: nem inspecionar/percorrer/montar |
| api | .env* | any | segredos fora do diff |
| root | .env* | any | configuração privada intocada no planejamento |
| root | .gitmodules | any | pipeline-owned |
| root | api-app | any | gitlink pipeline-owned |
| root | web-app | any | gitlink pipeline-owned |
| root | delphi-ai | any | sem self-improvement |
| web | dist/** | any | gerado não é fonte |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
Planejamento v1.1 ainda não executou guard de entrega. O produto contém alterações já entregues em ST-CON-06 sobre os HEADs publicados; esse estado é a baseline herdada exata, não diff novo de05 nem justificativa para commit de produto. As linhas “Baseline herdada SOMENTE” representam esse fato para o guard Git e NÃO autorizam novas mutações. Manifesto fechado em evidence/inherited-working-tree-v1.1.json: antes da PRIMEIRA mutação ou teste, conferir HEADs e TODOS41hashes (incluindo11shared); depois da admissão,30sealed permanecem byte-exatos em cada checkpoint/entrega e shared deltas são revistos contra a origem imutável publicada. Drift inicial interrompe para atribuição/review, sem rebase silencioso. Paths compartilhados explicitamente ativos acima podem mudar apenas pela jornada05, sob regressões completas e revisão de aderência; os demais ficam byte-exatos. Não excluir achados do guard silenciosamente nem limpar/normalizar produto para fazê-lo passar.


## Bounded But Elastic Guardrails

- **May stay inside this TODO:** concretização de schema, DI, componentes e fixtures do mesmo preparar/submeter/consultar modelo; reutilizar componentes existentes quando comprovados.
- **Must update or split the TODO:** envio a contato, atualização/exclusão de ativo na Meta, novo tipo de template, novo papel/canal, background jobs ou consumo ST-CON-04 requerem contrato próprio/reconvergência.

## Definition of Done

- [ ] DOD-01 — Vendedor ATENDENTE+ abre Modelos de mensagem, cria/salva/reabre seu rascunho por BU/canal, edita com revision CAS, preenche exemplos e vê prévia coerente; atores sem grant na BU e escopos alheios falham antes de efeitos.
- [ ] DOD-02 — Submissão no LeadsHug não exige ADMIN; usa a conta/credencial verificadas do canal, valida texto/variáveis/categoria/idioma e confirma snapshot/revisão; nenhuma mensagem ou conversa é criada.
- [ ] DOD-03 — Replays/duplo clique/crash não repetem POST por operação; conta/nome/idioma concorrentes são protegidos; resultado incerto permanece explícito e reconcile não faz POST externo nem vincula definição diferente.
- [ ] DOD-04 — Consulta/status e catálogo paginados refletem Meta com frescor/categoria efetiva, sem promover PENDING/UNKNOWN/recusado/pausado a pronto; erro seguro conserva estado anterior e não finge catálogo vazio.
- [ ] DOD-05 — Troca de BU/canal/revisão, saves concorrentes e status atrasado não sobrescrevem draft/estado atual; refresh da página recupera operação sem chave do browser e sem divulgar token/segredo.
- [ ] DOD-06 — Schema/migration deploy/status, harness durável, CI-equivalent completo e Playwright mutation passam com API/PG reais e bundle servido fresco; gate send de ST-CON-01 e contratos Channel/OutboundService de ST-CON-06 permanecem inalterados.
- [ ] DOD-07 — Operador valida criar/submeter um modelo textual de teste na conta correta e consultar seu resultado real; decisão Meta pode ser PENDING/REJECTED sem falsear APPROVED. Consumo físico aprovado no ST-CON-04 continua dependência separada.
- [ ] DOD-08 — Decisões e contrato promovidos ao módulo responsável, revisões derivadas/segurança/pcv/TQA/final e guardas de entrega satisfeitos; sem P1/P2 aberto e sem claim de produção.

## Validation Steps

- [ ] VAL-01 — Executar bash scripts/test-channels-local.sh all, com boundary público positivo de ST-CON-06 preservado, incluindo deploy/status de migrations, lint/build/unit/E2E/Web/Playwright e fonte/served fingerprints.
- [ ] VAL-02 — Executar barreiras PostgreSQL + contador HTTP para save CAS, key replay, reserva do mesmo nome entre vendedores, lease vencido, timeout pós-dispatch, keys/atores diferentes na mesma revisão, mesma conta por BUs/Mantenedoras diferentes versus contas distintas, rollback real e commit real com ACK local perdido em reserva/claim/recibo/release, e alteração de conta/geração/versão de credencial em voo; sem HTTP em transação.
- [ ] VAL-03 — Executar web-app/e2e/message-templates.spec.ts via runner canônico com BFF real: editor/preview/save/reopen/submit/refresh/recusa/incerteza/roles/BU-stale e proteção de operação, sem mock BFF.
- [ ] VAL-04 — Confirmada readiness da conta própria, operador submete modelo de teste e atualiza status pelo LeadsHug; registrar resultado redigido, sem enviar mensagem a destinatário nem declarar aprovação por fixture.
- [ ] VAL-05 — Rodar architecture adherence/security/pcv/TQA/final/debt/diff público e authority/completion/closeout antes de entrega; reconvergir ST-CON-04 apenas no handoff seguinte.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | DOD-01 — Vendedor ATENDENTE+ abre Modelos de mensagem, cria/salva/reabre seu rascunho por BU/canal, edita com revision CAS, preenche exemplos e vê prévia coerente; atores sem grant na BU e escopos alheios falham antes de efeitos. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| DOD-02 | Definition of Done | DOD-02 — Submissão no LeadsHug não exige ADMIN; usa a conta/credencial verificadas do canal, valida texto/variáveis/categoria/idioma e confirma snapshot/revisão; nenhuma mensagem ou conversa é criada. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| DOD-03 | Definition of Done | DOD-03 — Replays/duplo clique/crash não repetem POST por operação; conta/nome/idioma concorrentes são protegidos; resultado incerto permanece explícito e reconcile não faz POST externo nem vincula definição diferente. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| DOD-04 | Definition of Done | DOD-04 — Consulta/status e catálogo paginados refletem Meta com frescor/categoria efetiva, sem promover PENDING/UNKNOWN/recusado/pausado a pronto; erro seguro conserva estado anterior e não finge catálogo vazio. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| DOD-05 | Definition of Done | DOD-05 — Troca de BU/canal/revisão, saves concorrentes e status atrasado não sobrescrevem draft/estado atual; refresh da página recupera operação sem chave do browser e sem divulgar token/segredo. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| DOD-06 | Definition of Done | DOD-06 — Schema/migration deploy/status, harness durável, CI-equivalent completo e Playwright mutation passam com API/PG reais e bundle servido fresco; gate send de ST-CON-01 permanece inalterado. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| DOD-07 | Definition of Done | DOD-07 — Operador valida criar/submeter um modelo textual de teste na conta correta e consultar seu resultado real; decisão Meta pode ser PENDING/REJECTED sem falsear APPROVED. Consumo físico aprovado no ST-CON-04 continua dependência separada. | test/runtime/review | Prova real assistida, response/status scoped e receipt redigido; não fixture. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| DOD-08 | Definition of Done | DOD-08 — Decisões e contrato promovidos ao módulo responsável, revisões derivadas/segurança/pcv/TQA/final e guardas de entrega satisfeitos; sem P1/P2 aberto e sem claim de produção. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| VAL-01 | Validation Steps | VAL-01 — Executar bash scripts/test-channels-local.sh all, após boundary público corrigido, incluindo deploy/status de migrations, lint/build/unit/E2E/Web/Playwright e fonte/served fingerprints. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| VAL-02 | Validation Steps | VAL-02 — Executar barreiras PostgreSQL + contador HTTP para save CAS, key replay, reserva do mesmo nome entre vendedores, lease vencido, timeout pós-dispatch, keys/atores diferentes na mesma revisão e alteração de conta/geração/versão de credencial em voo; sem HTTP em transação. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| VAL-03 | Validation Steps | VAL-03 — Executar web-app/e2e/message-templates.spec.ts via runner canônico com BFF real: editor/preview/save/reopen/submit/refresh/recusa/incerteza/roles/BU-stale e proteção de operação, sem mock BFF. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| VAL-04 | Validation Steps | VAL-04 — Confirmada readiness da conta própria, operador submete modelo de teste e atualiza status pelo LeadsHug; registrar resultado redigido, sem enviar mensagem a destinatário nem declarar aprovação por fixture. | test/runtime/review | Prova real assistida, response/status scoped e receipt redigido; não fixture. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |
| VAL-05 | Validation Steps | VAL-05 — Rodar architecture adherence/security/pcv/TQA/final/debt/diff público e authority/completion/closeout antes de entrega; reconvergir ST-CON-04 apenas no handoff seguinte. | test/runtime/review | web-app/e2e/message-templates.spec.ts; api-app/test/message-templates.e2e-spec.ts; bash scripts/test-channels-local.sh all; gates VAL-05. | local descartável; recurso próprio só quando explícito | planned | Implementação em curso. CP01–03 possuem evidência parcial; este critério aguarda suas provas CP04/Web/all, revisões e/ou validação assistida, conforme aplicável. |

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Conta Meta e grant whatsapp_business_management | criar/listar/status na conta do canal | unknown | 2026-10-19 | fonte atual e informação do operador; nenhum token lido | revalidar readiness no handoff; falta de escopo pede reautorizar pelo fluxo normal |
| Aprovação Meta do novo modelo | uso posterior fora de janela | unknown | 2026-10-19 | usuário ainda sem template aprovado | criar/submeter é a história atual; aprovação não é garantida nem requisito falso para validar recusa/pending |
| Docker/runner local | suíte determinística | historical-verified | all93791/ST-CON-06 em2026-10-20 | 613tests/guard23/Linux/selo57, sem nova execução05 | preservar inventário público positivo e recursos descartáveis Node22/PG16; revalidar antes de execução |
| HTTPS temporário | prova assistida | unknown | ST-CON-01 teve prova CP108 | nenhuma nova consulta | revalidar antes do operador, sem prometer disponibilidade contínua |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs,react,vite,postgresql,prisma,docker
- **Expected supporting profiles:** strategic-cto,operational-devops,assurance-tester-quality,assurance-security-adversarial
- **Scope-check command:** python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/README.md
- **Gate 0:** Genesis rejeitado; projeto e módulos canônicos existentes. Planejamento de ST-CON-05 atual strategic-cto, sem código.

### Handoff Log (Update when execution crosses profile boundaries)
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | APROVADO explícito v1.1 recebido2026-10-21 | API/Web e testes | accepted; principal single-writer, profile operational-coder, no worktrees |
| operational-coder | operational-devops | publicação local e readiness | runner/containers próprios | planned |
| operational-coder | assurance-tester-quality | TQA e aderência | pacote limitado | planned |
| operational-coder | assurance-security-adversarial | auth/idempotência/segredos | BFF e adapter | planned |

## Complexity

- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section
- **Why this level:** novo domínio/modelo persistente com submissão externa, status assíncrono e vendedor autorizado; um objetivo com contratos/DB/UX concorrentes.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** foundation_documentation/modules/integrations-and-channels.md
- **Secondary module docs (if any):** foundation_documentation/modules/inbox-and-conversations.md
- **Planned decision promotion targets (module sections):** integrations-and-channels: Modelos textuais ST-CON-05 e API Endpoint Definitions; inbox: referência ao catálogo que ST-CON-04 consumirá.
- **Module decision consolidation targets (required):** mesmos alvos, D-01..09 com provenance do TODO; não promover minuta como implementada. Constituição já admite templates em TODO próprio; não há novo runtime surface ou tenant boundary, apenas rotas BFF existentes.

## Decision Pending (Resolve Before Freeze)

Nenhuma pergunta funcional humana aberta: vendedor cria/submete; recorte textual/pt_BR e limites locais detalhados para aprovação. Arquitetura/capacidade/baseline e validação serão desafiadas por revisão fresh. Aprovação externa pertence à Meta.

## Decisions (Resolved Before Freeze)

- [x] D-01 — Rota Web /modelos em Cadastros acessível a ATENDENTE+ com seleção de BU/canal oficial. Tela mostra Meus rascunhos e Modelos da conta, com conteúdo/variáveis/prévia/categoria/status em português. ATENDENTE cria/edita/submete seus rascunhos; ADMIN/OWNER da BU pode administrar rascunhos da BU. Os papéis existentes são OWNER/ADMIN/ATENDENTE; ator autenticado sem grant na BU não cria/submete; outra BU/tenant/rascunho de colega sem papel administrativo retorna404/403 conforme existência autorizada. Templates submetidos são ativos compartilhados da Messaging account e seu catálogo é acessível pelos canais autorizados dessa conta; não prometer privacidade individual após submissão. Nenhuma aprovação administrativa intermediária. Fonte: decisão explícita do usuário; No Prior Decision para autoria.
- [x] D-02 — Editor desta versão cria pt_BR, categoria MARKETING (padrão de abertura comercial) ou UTILITY com descrição correta do uso, sem trocar categoria para contornar Meta. Nome interno normalizado exibido antes de submit, regex [a-z][a-z0-9_]{0,127}; BODY obrigatório1..1024 caracteres; HEADER TEXT e FOOTER estáticos opcionais até60 cada, sem variáveis neles. BODY usa até20variáveis NAMED únicas [a-z][a-z_]{0,31}, todas com exemplo textual fictício1..128caracteres e sem chaves extras/faltantes. Rejeitar braces inválidas, variável solta no início/fim e componentes não suportados; total JSON até16KiB. Prévia usa POST BFF dedicado, autenticado/CSRF, com leituras autorizadas do contexto, sem provider nem escrita DB; domínio backend valida/renderiza e retorna definição normalizada, texto plano e requestFingerprint vinculado a canal/conta/generation/activeCredentialVersion e draft/revisão quando salvos. Preview de conteúdo não salvo é marcado unpersisted e não habilita submit; create/PATCH devolvem fingerprint da revisão durável, conferida novamente em submit. React exibe texto escapado, debounce300ms e fence monotônico de contexto/resposta; nenhum import entre repositórios nem parser autoritativo duplicado, CRM/avaliação de código. Não garantir aprovação. Catálogo pode ler NAMED/POSITIONAL suportados pelo ST-CON-04; criação em NAMED/pt_BR é fronteira explícita. Fonte: Meta fundamentals/components/review; No Prior Decision local.
- [x] D-03 — Domínio message-templates é owner de draft/revisão/submissão/observação/catalog projector; TemplateManagement/Provider ports separam domínio do adapter MetaTemplateClient HTTP dedicado; a interface MetaClient e seus consumers de texto/cadastro permanecem intactos. Draft tem mantenedoraId/buId/creatorUserId/channelId/accountId imutáveis, revision monotônica e snapshot de definição; nunca token. Mesmo clientRequestId UUID por BU/ator cria um único draft (auth antes de lookup). PATCH exige expectedRevision e só draft editável; save CAS conflita409. Submit congela revisão; após ativo externo ou resultado incerto, não editar remoto nem mudar conta no mesmo draft: Criar variação faz NOVO rascunho com nome novo confirmado, sem POST Meta até nova ação. Recusa de submissão pré-dispatch/provada reabre draft para revisão/key novas por CAS; mantém recibos e replays antigos imutáveis, conforme Recovery Transition Contract. Recusa posterior da análise de ativo ACCEPTED exige Criar variação, não reabre a revisão já submetida. Fonte: invariantes de BU/backend/persistência Preserve; No Prior Decision para rascunho.
- [x] D-04 — Gerenciamento de template usa propósito explícito template-management em ChannelCredentialResolver: somente OFICIAL, identidade própria/epoch correntes, managed identity e credencial ativa da geração e activeCredentialVersion; tenant/grant ATENDENTE+ e WABA da BU/canal revalidados. Não exigir receiptVerifiedAt/CONECTADO para GERENCIAR template, porque não é mensagem; não usar verify/registration como bypass e NÃO alterar purpose send nem liberar primeiro OUT sem readiness ST-CON-01. App/audience, whatsapp_business_management e alvo da conta são comprovados no backend; nenhuma WABA/token arbitrários do cliente nem fallback global. Reauth no mesmo account exige refresh/expectedGeneration atual; operações e observações capturam e validam account/channel/generation/managedIdentity/activeCredentialVersion por CAS no dispatch claim e refresh. Resposta antiga só pode enriquecer recibo histórico, nunca certificar contexto atual; se conta mudar, bloquear draft antigo com CONTA_ALTERADA e permitir nova cópia explícita, não rebinding silencioso. Fonte: integrations scoped credential Preserve; novo propósito é extensão intencional, sem supersede do gate send.
- [x] D-05 — BFF endpoints do contrato abaixo são de sessão/CSRF. Submit recebe draftId/expectedRevision/expectedGeneration/expectedDefinitionFingerprint + Idempotency-Key UUID; o requestFingerprint confirmado cobre conta/canal/generation/activeCredentialVersion/draft/revisão/nome/idioma/categoria/componentes/exemplos imutáveis, serialização canônica de campos/mapas sem apagar conteúdo. Reserve operação PREPARED scoped e nome por namespace CANÔNICO GLOBAL de provedor/conta remota/nome/idioma em transação; revisões imutáveis e chave por BU/ator/payload garantem um dispatch. A coordenação técnica vale para todos os vínculos da mesma conta, inclusive BUs e Mantenedoras diferentes; namespace/reserva/quota não contém definição de rascunho nem concede grant. Resposta de conflito é genérica e não revela tenant/autor/operação/conteúdo/contagens alheios. Não se presume exclusividade WABA→Mantenedora; drafts, operações e observações de negócio continuam scoped pela BU/Mantenedora/autor. Referência canônica da conta vem do resolver/adaptação server-side, nunca do cliente. Reservas em contas diferentes permanecem independentes; preflight usa GET account-scoped message_templates?name=<nome persistido codificado pelo servidor>, conferindo nome/idioma exatos e ausência de recurso remoto, conflito seguro sem substituir ativo. Auth/replay antes de provider reads. Admissão/claim/recibo/release seguem também o Local Commit Certainty Contract: HTTP só depois de confirmação positiva do claim original; persistência incerta nunca libera reserva nem autoriza outro POST. Budget por submit até3GETs (grant1 + até2páginas de preflight filtradas por nome,50 por página) e1POST, timeout10s cada/budget45s/lease60s. Se lista filtrada não se esgota, filtro não é suportado ou resposta é inválida, falhar inconclusivo sem POST; não varrer todo catálogo nem tomar filtro como igualdade comprovada. Rate limit durável10tentativas/min por ator e60dispatches/h por namespace global canônico da conta (somando todos os vínculos/tenants da mesma conta), incluindo incertos; respeitar429 sem retry automático, não prometer controlar alterações de outros aplicativos. Fonte: No Prior Decision para submit; padrão HTTP fora da tx Preserve.
- [x] D-06 — PREPARED falha/lease expirada antes de dispatch termina REJECTED(dispatched=false), libera reserva sem ativo externo, sem chamada tardia por CAS vencido. PREPARED→SENDING é CAS com revisão/lease/contexto atuais; uma invocação POST por operação, sem retry de mutação. Resposta válida com id durável vira ACCEPTED, conserva conta/ID originais e snapshot mesmo se depois trocar geração; nunca rebind para conta nova. Status de aprovação é dimensão separada: ACCEPTED não significa APPROVED. Recusa Graph tipada e comprovada vira REJECTED; timeout/malformed/semID/crash após SENDING vira AMBIGUOUS, bloqueia repetir criação dessa revisão/nome, não inventa ID. POST reconcile aplica primeiro a tabela Recovery Transition Contract abaixo e faz só GETs Meta bounded por grant+até2páginas filtradas pelo nome persistido na conta original; aceita vínculo apenas se um único recurso com nome/idioma/definição semântica remota exatos. remoteSemanticFingerprint contém nome/idioma/parameter_format/categoria solicitada e componentes completos suportados (tipo/formato/texto exatos e schema de todas variáveis); exclui somente exemplos de revisão e metadata provider (id/status/timestamps). Não fazer trim/normalização de conteúdo para forçar match; exemplos permanecem no snapshot/requestFingerprint original. Campos semânticos ausentes, componente extra, categoria reclassificada ou diferença impedem correlação automática. Registrar CORRELATED_BY_DEFINITION e exibir Recurso compatível localizado, sem inferir autoria nem que o POST incerto criou o recurso ou que seus exemplos foram aceitos. Conta inacessível/diferente, múltiplos matches, nome/conteúdo divergentes, paginação inconclusiva ou ausência mantêm AMBIGUOUS; nenhum POST automático. Recursos já existentes antes de dispatch dão conflito, não adoção. Se não houver correlação segura, conservar recibo e oferecer nova variação com outro nome por ação explícita, preservando a reserva incerta; nenhuma exclusão/limpeza Meta. Qualquer falha local após ACK válido conserva criação externa ACCEPTED e receiptPersistence RECORDED só com prova positiva; caso contrário503 TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE, providerAcceptance CONFIRMED/receiptPersistence UNCONFIRMED e recuperação pela mesma operação, sem soltar nome ou repetir POST, mesmo se o rollback local estiver confirmado. Um resultado tardio conhecido melhora a MESMA operação de forma monotônica e não duplica associação, nome ou estado de outra revisão. Limite honesto: não exactly-once externo nem garantia de aprovação. Fonte: No Prior Decision para operação.
- [x] D-07 — GET local não altera status e não chama provider; Atualizar status/catálogo é POST explícito. ProviderApprovalStatus mantém enum próprio PENDING/APPROVED/REJECTED/PAUSED/DISABLED/ARCHIVED/DELETED/IN_APPEAL/PENDING_DELETION/LIMIT_EXCEEDED/UNKNOWN, categoria efetiva, definição atual e observedAt separados do pedido imutável. Mostrar Aprovado na consulta de [observedAt], nunca pronto indefinidamente. Elegibilidade observada exige APPROVED textual suportado, contexto corrente e idade da observação até300s pelo relógio do servidor; após300s ou erro/contexto diferente marcar stale/unavailable e observedEligible=false. APPROVED pode depois mudar; ST-CON-04 obrigatoriamente revalida elegibilidade de forma independente antes de enviar. Erro/malformed/permissão perdida conserva observação anterior com unavailable/stale, não aprova nem mascara como vazio. Refresh individual e refresh de catálogo compartilham UM lease persistente por conta/contexto autorizado (Mantenedora/BU/canal/conta/generation/epoch/managedIdentity/activeCredentialVersion), fence monotônico e debounce10s; os dois produtores gravam a MESMA observação por contexto/remoteTemplateId no único projector. Não existem leases independentes por endpoint. Só o dono do fence corrente e ainda vivo pode gravar observação, disponibilidade, observedAt, elegibilidade e cursor/metadata da sua página; resposta antiga/expirada perde toda autoridade de escrita mesmo com identidade ainda igual. O Shared Observation Fence Contract detalha expiração, concorrência e testes bidirecionais, preservando HTTP fora de transação e nenhum fan-out. Reclassificação/corpo alterado externamente aparecem como observação atual, nunca reescrevem snapshot pedido. Erros expõem catálogo fixo/enum traduzido, não payload bruto; exemplos/texto não vão a logs/audit bruto. Listas locais paginação20máx50, catálogo50 com after até512/continuação explícita, zero fan-out ao listar; nunca seguir URL de cursor do cliente/provedor. Catálogo validado/projetor tem um owner reutilizável por ST-CON-04, sem duplicar catálogo no futuro sender. Fonte: autoridade de Meta sobre status e integrations invariants Preserve.
- [x] D-08 — Formulário e respostas guardados por BU/canal/draftId/revision/geração/versão de credencial do contexto e revisão monotônica de UI; A→B→A não aceita resposta velha por igualdade textual. Replay/key ficam na operação, GET seguro por ID recupera submit após refresh, sem guardar token/browser key obrigatória; lista inclui operação atual + até10recentes e estado safe. Erro preserva draft e explica nome conflitado, amostras faltantes, limitação/provider unavailable, rejeição e resultado incerto. UI não declara mensagem enviada nem envia a destinatário; não há botão de uso inoperante antes de ST-CON-04. Prova real desta história verifica submissão e consulta em conta de teste própria, inclusive decisão pending/recusa autêntica; aprovação é dependency para consumir/enviar no ST-CON-04 seguinte. Fonte: ST-ATT-01 freshness Preserve; nova jornada solicitada pelo usuário.
- [x] D-09 — Channel e ChannelResolver textuais de ST-CON-06 permanecem inalterados: nenhum método createTemplate/no-op/cast instanceof/branch de provider nos consumers de mensagem. Domínio message-templates define ports abstratos TemplateManagementResolver e MessageTemplateProvider: resolver recebe referência de BU/canal já autorizada, retorna provider bound por operação + contexto seguro imutável (BU/canal/identidade/generation/epoch/activeCredentialVersion e referência opaca da conta). Provider expõe somente criar/listar/consultar modelo com DTOs/resultados tipados de templates, nunca enviar mensagem nem receber token/endereço de protocolo do caller. Integração implementa resolver scoped, factory/registro explícito da capacidade e provider Meta; somente oficial possui implementação real agora, outro canal retorna capability unavailable na resolução, sem concreto de mentira/no-op. A composição TemplateManagementModule importa ChannelTransportModule para reutilizar seu único ChannelCredentialResolver/crypto e exporta o resolver abstrato ao BFF; não redeclara clients/resolver/OutboundService da composição existente. Serviços de templates não importam MetaClient/MetaTemplateClient/HTTP, nem selecionam OFICIAL por branch; IDs de protocolo/tokens ficam privados no adapter/factory. Grant management HTTP é do MetaTemplateClient e não altera os requisitos messaging/send existentes. Fake independente da nova porta passa pelas mesmas regras de draft/operação/conta; harness com violação sintética bloqueia dispatch/client concreto nos services e alteração da porta Channel para suportar templates. Novas redes e novas capacidades futuras exigem contratos próprios; nenhuma plataforma genérica de plugins ou refatoração do registro textual nesta história.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| constitution#system-invariants | templates só em TODO próprio, domínio backend, BU scope | Preserve | este contrato próprio e D01..09 |
| integrations-and-channels#invariants | provider adapter, erro seguro, segredo privado | Preserve | MetaClient/credencial contextual |
| integrations-and-channels#bff-e-autorização | account template/billing e credenciais por canal | Preserve | D04/05, conta do servidor |
| integrations-and-channels#cadastro-de-números-st-con-01 | gate send e criptografia atuais | Preserve | propósito management separado, sem receipt para gerenciar; send intocado |
| integrations/inbox#channel-st-con-06 | Channel textual/Resolver/OutboundService comuns e aceitação única | Preserve | D09; capability estreita separada, sender/política não mudam |
| ST-CON-04/out-of-scope | criação/submissão de templates fora do primeiro envio | Preserve | ST-CON-05 novo owner; ST-CON-04 depende dele, sem ampliar aquele contrato |
| inbox-and-conversations#timeline | history/draft freshness | Preserve | não altera Message/conversa/timeline |

## Decision Baseline (Frozen Before Implementation)
- [ ] D-01 — Rota Web /modelos em Cadastros acessível a ATENDENTE+ com seleção de BU/canal oficial. Tela mostra Meus rascunhos e Modelos da conta, com conteúdo/variáveis/prévia/categoria/status em português. ATENDENTE cria/edita/submete seus rascunhos; ADMIN/OWNER da BU pode administrar rascunhos da BU. Os papéis existentes são OWNER/ADMIN/ATENDENTE; ator autenticado sem grant na BU não cria/submete; outra BU/tenant/rascunho de colega sem papel administrativo retorna404/403 conforme existência autorizada. Templates submetidos são ativos compartilhados da Messaging account e seu catálogo é acessível pelos canais autorizados dessa conta; não prometer privacidade individual após submissão. Nenhuma aprovação administrativa intermediária. Fonte: decisão explícita do usuário; No Prior Decision para autoria.
- [ ] D-02 — Editor desta versão cria pt_BR, categoria MARKETING (padrão de abertura comercial) ou UTILITY com descrição correta do uso, sem trocar categoria para contornar Meta. Nome interno normalizado exibido antes de submit, regex [a-z][a-z0-9_]{0,127}; BODY obrigatório1..1024 caracteres; HEADER TEXT e FOOTER estáticos opcionais até60 cada, sem variáveis neles. BODY usa até20variáveis NAMED únicas [a-z][a-z_]{0,31}, todas com exemplo textual fictício1..128caracteres e sem chaves extras/faltantes. Rejeitar braces inválidas, variável solta no início/fim e componentes não suportados; total JSON até16KiB. Prévia usa POST BFF dedicado, autenticado/CSRF, com leituras autorizadas do contexto, sem provider nem escrita DB; domínio backend valida/renderiza e retorna definição normalizada, texto plano e requestFingerprint vinculado a canal/conta/generation/activeCredentialVersion e draft/revisão quando salvos. Preview de conteúdo não salvo é marcado unpersisted e não habilita submit; create/PATCH devolvem fingerprint da revisão durável, conferida novamente em submit. React exibe texto escapado, debounce300ms e fence monotônico de contexto/resposta; nenhum import entre repositórios nem parser autoritativo duplicado, CRM/avaliação de código. Não garantir aprovação. Catálogo pode ler NAMED/POSITIONAL suportados pelo ST-CON-04; criação em NAMED/pt_BR é fronteira explícita. Fonte: Meta fundamentals/components/review; No Prior Decision local.
- [ ] D-03 — Domínio message-templates é owner de draft/revisão/submissão/observação/catalog projector; TemplateManagement/Provider ports separam domínio do adapter MetaTemplateClient HTTP dedicado; a interface MetaClient e seus consumers de texto/cadastro permanecem intactos. Draft tem mantenedoraId/buId/creatorUserId/channelId/accountId imutáveis, revision monotônica e snapshot de definição; nunca token. Mesmo clientRequestId UUID por BU/ator cria um único draft (auth antes de lookup). PATCH exige expectedRevision e só draft editável; save CAS conflita409. Submit congela revisão; após ativo externo ou resultado incerto, não editar remoto nem mudar conta no mesmo draft: Criar variação faz NOVO rascunho com nome novo confirmado, sem POST Meta até nova ação. Recusa de submissão pré-dispatch/provada reabre draft para revisão/key novas por CAS; mantém recibos e replays antigos imutáveis, conforme Recovery Transition Contract. Recusa posterior da análise de ativo ACCEPTED exige Criar variação, não reabre a revisão já submetida. Fonte: invariantes de BU/backend/persistência Preserve; No Prior Decision para rascunho.
- [ ] D-04 — Gerenciamento de template usa propósito explícito template-management em ChannelCredentialResolver: somente OFICIAL, identidade própria/epoch correntes, managed identity e credencial ativa da geração e activeCredentialVersion; tenant/grant ATENDENTE+ e WABA da BU/canal revalidados. Não exigir receiptVerifiedAt/CONECTADO para GERENCIAR template, porque não é mensagem; não usar verify/registration como bypass e NÃO alterar purpose send nem liberar primeiro OUT sem readiness ST-CON-01. App/audience, whatsapp_business_management e alvo da conta são comprovados no backend; nenhuma WABA/token arbitrários do cliente nem fallback global. Reauth no mesmo account exige refresh/expectedGeneration atual; operações e observações capturam e validam account/channel/generation/managedIdentity/activeCredentialVersion por CAS no dispatch claim e refresh. Resposta antiga só pode enriquecer recibo histórico, nunca certificar contexto atual; se conta mudar, bloquear draft antigo com CONTA_ALTERADA e permitir nova cópia explícita, não rebinding silencioso. Fonte: integrations scoped credential Preserve; novo propósito é extensão intencional, sem supersede do gate send.
- [ ] D-05 — BFF endpoints do contrato abaixo são de sessão/CSRF. Submit recebe draftId/expectedRevision/expectedGeneration/expectedDefinitionFingerprint + Idempotency-Key UUID; o requestFingerprint confirmado cobre conta/canal/generation/activeCredentialVersion/draft/revisão/nome/idioma/categoria/componentes/exemplos imutáveis, serialização canônica de campos/mapas sem apagar conteúdo. Reserve operação PREPARED scoped e nome por namespace CANÔNICO GLOBAL de provedor/conta remota/nome/idioma em transação; revisões imutáveis e chave por BU/ator/payload garantem um dispatch. A coordenação técnica vale para todos os vínculos da mesma conta, inclusive BUs e Mantenedoras diferentes; namespace/reserva/quota não contém definição de rascunho nem concede grant. Resposta de conflito é genérica e não revela tenant/autor/operação/conteúdo/contagens alheios. Não se presume exclusividade WABA→Mantenedora; drafts, operações e observações de negócio continuam scoped pela BU/Mantenedora/autor. Referência canônica da conta vem do resolver/adaptação server-side, nunca do cliente. Reservas em contas diferentes permanecem independentes; preflight usa GET account-scoped message_templates?name=<nome persistido codificado pelo servidor>, conferindo nome/idioma exatos e ausência de recurso remoto, conflito seguro sem substituir ativo. Auth/replay antes de provider reads. Admissão/claim/recibo/release seguem também o Local Commit Certainty Contract: HTTP só depois de confirmação positiva do claim original; persistência incerta nunca libera reserva nem autoriza outro POST. Budget por submit até3GETs (grant1 + até2páginas de preflight filtradas por nome,50 por página) e1POST, timeout10s cada/budget45s/lease60s. Se lista filtrada não se esgota, filtro não é suportado ou resposta é inválida, falhar inconclusivo sem POST; não varrer todo catálogo nem tomar filtro como igualdade comprovada. Rate limit durável10tentativas/min por ator e60dispatches/h por namespace global canônico da conta (somando todos os vínculos/tenants da mesma conta), incluindo incertos; respeitar429 sem retry automático, não prometer controlar alterações de outros aplicativos. Fonte: No Prior Decision para submit; padrão HTTP fora da tx Preserve.
- [ ] D-06 — PREPARED falha/lease expirada antes de dispatch termina REJECTED(dispatched=false), libera reserva sem ativo externo, sem chamada tardia por CAS vencido. PREPARED→SENDING é CAS com revisão/lease/contexto atuais; uma invocação POST por operação, sem retry de mutação. Resposta válida com id durável vira ACCEPTED, conserva conta/ID originais e snapshot mesmo se depois trocar geração; nunca rebind para conta nova. Status de aprovação é dimensão separada: ACCEPTED não significa APPROVED. Recusa Graph tipada e comprovada vira REJECTED; timeout/malformed/semID/crash após SENDING vira AMBIGUOUS, bloqueia repetir criação dessa revisão/nome, não inventa ID. POST reconcile aplica primeiro a tabela Recovery Transition Contract abaixo e faz só GETs Meta bounded por grant+até2páginas filtradas pelo nome persistido na conta original; aceita vínculo apenas se um único recurso com nome/idioma/definição semântica remota exatos. remoteSemanticFingerprint contém nome/idioma/parameter_format/categoria solicitada e componentes completos suportados (tipo/formato/texto exatos e schema de todas variáveis); exclui somente exemplos de revisão e metadata provider (id/status/timestamps). Não fazer trim/normalização de conteúdo para forçar match; exemplos permanecem no snapshot/requestFingerprint original. Campos semânticos ausentes, componente extra, categoria reclassificada ou diferença impedem correlação automática. Registrar CORRELATED_BY_DEFINITION e exibir Recurso compatível localizado, sem inferir autoria nem que o POST incerto criou o recurso ou que seus exemplos foram aceitos. Conta inacessível/diferente, múltiplos matches, nome/conteúdo divergentes, paginação inconclusiva ou ausência mantêm AMBIGUOUS; nenhum POST automático. Recursos já existentes antes de dispatch dão conflito, não adoção. Se não houver correlação segura, conservar recibo e oferecer nova variação com outro nome por ação explícita, preservando a reserva incerta; nenhuma exclusão/limpeza Meta. Qualquer falha local após ACK válido conserva criação externa ACCEPTED e receiptPersistence RECORDED só com prova positiva; caso contrário503 TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE, providerAcceptance CONFIRMED/receiptPersistence UNCONFIRMED e recuperação pela mesma operação, sem soltar nome ou repetir POST, mesmo se o rollback local estiver confirmado. Um resultado tardio conhecido melhora a MESMA operação de forma monotônica e não duplica associação, nome ou estado de outra revisão. Limite honesto: não exactly-once externo nem garantia de aprovação. Fonte: No Prior Decision para operação.
- [ ] D-07 — GET local não altera status e não chama provider; Atualizar status/catálogo é POST explícito. ProviderApprovalStatus mantém enum próprio PENDING/APPROVED/REJECTED/PAUSED/DISABLED/ARCHIVED/DELETED/IN_APPEAL/PENDING_DELETION/LIMIT_EXCEEDED/UNKNOWN, categoria efetiva, definição atual e observedAt separados do pedido imutável. Mostrar Aprovado na consulta de [observedAt], nunca pronto indefinidamente. Elegibilidade observada exige APPROVED textual suportado, contexto corrente e idade da observação até300s pelo relógio do servidor; após300s ou erro/contexto diferente marcar stale/unavailable e observedEligible=false. APPROVED pode depois mudar; ST-CON-04 obrigatoriamente revalida elegibilidade de forma independente antes de enviar. Erro/malformed/permissão perdida conserva observação anterior com unavailable/stale, não aprova nem mascara como vazio. Refresh individual e refresh de catálogo compartilham UM lease persistente por conta/contexto autorizado (Mantenedora/BU/canal/conta/generation/epoch/managedIdentity/activeCredentialVersion), fence monotônico e debounce10s; os dois produtores gravam a MESMA observação por contexto/remoteTemplateId no único projector. Não existem leases independentes por endpoint. Só o dono do fence corrente e ainda vivo pode gravar observação, disponibilidade, observedAt, elegibilidade e cursor/metadata da sua página; resposta antiga/expirada perde toda autoridade de escrita mesmo com identidade ainda igual. O Shared Observation Fence Contract detalha expiração, concorrência e testes bidirecionais, preservando HTTP fora de transação e nenhum fan-out. Reclassificação/corpo alterado externamente aparecem como observação atual, nunca reescrevem snapshot pedido. Erros expõem catálogo fixo/enum traduzido, não payload bruto; exemplos/texto não vão a logs/audit bruto. Listas locais paginação20máx50, catálogo50 com after até512/continuação explícita, zero fan-out ao listar; nunca seguir URL de cursor do cliente/provedor. Catálogo validado/projetor tem um owner reutilizável por ST-CON-04, sem duplicar catálogo no futuro sender. Fonte: autoridade de Meta sobre status e integrations invariants Preserve.
- [ ] D-08 — Formulário e respostas guardados por BU/canal/draftId/revision/geração/versão de credencial do contexto e revisão monotônica de UI; A→B→A não aceita resposta velha por igualdade textual. Replay/key ficam na operação, GET seguro por ID recupera submit após refresh, sem guardar token/browser key obrigatória; lista inclui operação atual + até10recentes e estado safe. Erro preserva draft e explica nome conflitado, amostras faltantes, limitação/provider unavailable, rejeição e resultado incerto. UI não declara mensagem enviada nem envia a destinatário; não há botão de uso inoperante antes de ST-CON-04. Prova real desta história verifica submissão e consulta em conta de teste própria, inclusive decisão pending/recusa autêntica; aprovação é dependency para consumir/enviar no ST-CON-04 seguinte. Fonte: ST-ATT-01 freshness Preserve; nova jornada solicitada pelo usuário.
- [ ] D-09 — Channel e ChannelResolver textuais de ST-CON-06 permanecem inalterados: nenhum método createTemplate/no-op/cast instanceof/branch de provider nos consumers de mensagem. Domínio message-templates define ports abstratos TemplateManagementResolver e MessageTemplateProvider: resolver recebe referência de BU/canal já autorizada, retorna provider bound por operação + contexto seguro imutável (BU/canal/identidade/generation/epoch/activeCredentialVersion e referência opaca da conta). Provider expõe somente criar/listar/consultar modelo com DTOs/resultados tipados de templates, nunca enviar mensagem nem receber token/endereço de protocolo do caller. Integração implementa resolver scoped, factory/registro explícito da capacidade e provider Meta; somente oficial possui implementação real agora, outro canal retorna capability unavailable na resolução, sem concreto de mentira/no-op. A composição TemplateManagementModule importa ChannelTransportModule para reutilizar seu único ChannelCredentialResolver/crypto e exporta o resolver abstrato ao BFF; não redeclara clients/resolver/OutboundService da composição existente. Serviços de templates não importam MetaClient/MetaTemplateClient/HTTP, nem selecionam OFICIAL por branch; IDs de protocolo/tokens ficam privados no adapter/factory. Grant management HTTP é do MetaTemplateClient e não altera os requisitos messaging/send existentes. Fake independente da nova porta passa pelas mesmas regras de draft/operação/conta; harness com violação sintética bloqueia dispatch/client concreto nos services e alteração da porta Channel para suportar templates. Novas redes e novas capacidades futuras exigem contratos próprios; nenhuma plataforma genérica de plugins ou refatoração do registro textual nesta história.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability (`required|not_needed`):** required
- **Why this applies:** estabelece owner compartilhado de modelos/submissão e novo propósito seguro de credencial.
- **Deviation / debt being retired:** falta capacidade de preparar modelo no produto; não introduzir fluxo por token avulso ou criação de catálogo duplicado em Inbox.
- **Target steady-state after closeout:** domínio message-templates para draft/submission/status/catalogue; MetaTemplateClient dedicado para HTTP e resolver da capacidade scoped para segredos; futura inbox apenas consumer.
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** toda criação desta jornada passa pelo owner/revisão/dispatch fence, sem rota técnica paralela ou estado de aprovação local inventado.

### Patterns To Enforce (Required when applicability = `required`)
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| um owner do modelo/revisão | D03 | API/Web/Meta | payload/preview/submissão coerentes |
| credencial por propósito, BU/conta | ST-CON-01; D04 | resolver/provider | management não libera send |
| CAS/recibo durável/HTTP fora da tx | D05/06 | submit | doubleclick/restart não duplicam POST |

### Prohibited Anti-Patterns (Required when applicability = `required`)
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| autorizar só no menu ou exigir ADMIN ao vendedor | BFF role tests/browser seller | contradiz decisão humana | none |
| cache/process memory ou botão como dedupe | PG barrier/restart | repete create na Meta | none |
| ACCEPTED/pending como APPROVED | provider fixture states | libera modelo sem análise | none |
| token global/conta cliente/HTML preview | scoped/XSS tests | quebra fronteira de confiança | none |

### Architecture Protection Harness (Required when applicability = `required`)
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | API/PG/provider | api-app/test/message-templates.e2e-spec.ts via bash scripts/test-channels-local.sh all | role, CAS, duplicate submit/name, unknown recovery/status | implement-in-this-todo | DOD02/03/04/06; VAL01/02 |
| test | Web/BFF real | web-app/e2e/message-templates.spec.ts mesmo runner | editor, preview/save/submit/status, stale BU e perda de key | implement-in-this-todo | DOD01/05/06; VAL03 |
| dependency/contract | domínio template versus integração | src/domain/message-templates/*dependencies*.spec.ts + fake provider no test/message-template* via all | client/HTTP/concrete cast no service ou método template em Channel textual; violação sintética deve falhar | implement-in-this-todo | D09/SCOPE03/05 |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** findings_integrated
- **Decision review evidence / resolution:** architecture-v1.1.raw/merge terminal21346; AR-V11-01/02/03 integrated; full fresh critique-r1 and critique-r2 independently confirm integration; current-r2 terminal/strictmerge, no material findings. See current resolution receipts; no implementation pass inferred.
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** not_run
- **Adherence review evidence / resolution:** planned after implementation
- **No-go handling:** resolver ausência/divergência antes do gate, sem auto-waiver.

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Why this decision:** Capacidade estreita e baseline herdada devem ser avaliadas sobre proposta publicada exata.
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** 961dba71015f61a1f1c1badecb9efe090a77b306
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** CR-V11-01 integrated and renewed complete contract published before fresh affected full critique. Previous bcb43f94 freeze and reviews remain historical current-cycle evidence.
- **Evidence / reference:** origin/main@961dba71015f61a1f1c1badecb9efe090a77b306; guarded push terminal0, complete evolved TODO and critique resolution included.
- **Waiver authority / reference (required if waived):** n/a

## Gate: Review Scope Drift

- **Gate decision:** required
- **Why this decision:** conferir que aprovação usará pacote revisado.
- **Trigger stage:** after the planning-side review/guard cycle converges and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Material sections compared:** Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md
- **No-go handling rule:** reconvergir pacote/review e renovar freeze, sem implementação.
- **Gate status:** no_material_findings
- **Findings summary:** Actual scope-drift GO:23material sections unchanged against published961dba71 freeze; separate extended-scope seal confirms all4normative appendices unchanged. Only factual review/guard receipts updated afterward.
- **Evidence / reference:** artifacts/reviews/leadshug-template-authoring-20261020/evidence/scope-drift-v1.1.json; freeze961dba71015f61a1f1c1badecb9efe090a77b306
- **Waiver authority / reference (required if waived):** n/a

## Questions To Close
Revisar D09 e o selo herdado como parte da proposta v1.1. Nenhuma credencial/número real ou ação no painel Meta necessária no planejamento. Produto permanece sem APROVADO específico.

## Pattern References (Optional; Enforced When Cited)

n/a; contratos/decisões locais citados diretamente, sem ID de catálogo presumido.

## Assumptions Preview (Required Before Plan Review)
| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | MetaClient atual cobre cadastro/verify/send text e não gerencia templates. | api-app/src/integrations/meta/meta.client.ts:21 | reutilizar owner comprovado sem criar protocolo duplicado | High | Keep as Assumption |
| A-02 | ChannelCredentialResolver resolve send/registration/verify, e send exige receipt/conexão; não existe template-management. | api-app/src/domain/channels/channel-credential-resolver.ts:49 | ajustar propósito sem afrouxar send | High | Keep as Assumption |
| A-03 | BFFModule importa ChannelTransportModule e sessão no prefixo; este exporta o único owner de credenciais. | api-app/src/surfaces/bff/bff.module.ts; src/integrations/channels/channel-transport.module.ts | resolver DI antes de implementar, sem segundo crypto owner | High | Keep as Assumption |
| A-04 | Não há /modelos; menu Cadastros não é globalmente limitado a ADMIN; API cliente já tem postWithHeaders. | web-app/src/App.tsx; web-app/src/api.ts | reutilizar superfície existente e preservar papéis | High | Keep as Assumption |
| A-05 | Runner/CI já admitem all completo com inventário positivo, API/PG reais e Web fresco; a falha antiga de traversal foi resolvida por06. | scripts/test-channels-local.sh; .github/workflows/ci.yml; ST-CON-06 all93791 | bloquear testes se segurança/paridade divergir; não refazer runner sem necessidade | High | Keep as Assumption |
| A-06 | Channel.sendMessage textual e seu registry não têm capacidade de templates; futura extensão requer port estreito separado. | api-app/src/domain/channels/transport/channel.ts; channel-adapter-registry.ts | reconvergir arquitetura antes de ampliar a interface | High | Keep as Assumption |
| A-07 | HEADs de produto não contêm os commits de06, mas o principal working tree entregue/final-reviewed é identificável por hash. | api-app/src/domain/channels/transport/channel.ts; scripts/test-channels-local.sh; evidence/inherited-working-tree-v1.1.json/Git public metadata | parar em drift, não assumir HEAD limpo ou autorizar commit por inferência | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces
Somente inventário positivo do Diff Expectation Contract. Nenhum código/runtime/segredo no planejamento.

### Ordered Steps
1. APROVADO do ST-CON-05 v1.1, reload binding, routing/authority go e executor novo/sticky específico05 no principal. ANTES da primeira mutação/RED/teste, recibo de admissão inicial confere os3HEADs e TODOS41hashes públicos herdados, inclusive11shared, contra a origem imutável publicada; depois30sealed e deltas shared protegidos por checkpoint. Qualquer drift para e exige atribuição/review; sem .local-files. Backlog README é documentação de sequência strategic-cto autorizada pelo objetivo; classificador genérico marca path unknown, não há mudança de produto/infra. Outras mudanças preexistentes em Delphi não pertencem a este pacote e permanecem intocadas.
2. Antes de QUALQUER teste, inclusive RED/fail-first, verificar selo público herdado e runner positivo/CI já entregue; sem traversal privado, reset ou nova correção do runner presumida. Test-first do harness de capacidade/dependência/fake, roles, parser/examples/preview, CAS e operações/status com provider HTTP controlado.
3. Schema/migration aditiva e domínio único de draft/submission/observação; ports e resolução de capacidade D09, conta/grant/proposito seguros e MetaTemplateClient dedicado. Não alterar Channel/OutboundService/MetaClient atuais.
4. Editor/listas/status em Modelos no menu do vendedor, API wrappers seguros e estado/contexto monotônico. Nunca usar secret no browser.
5. Confirmar selo herdado e boundary positivo desde o passo2; ao medir EPS/impacto dos novos índices, corrigir no teste PCV existente a nomenclatura emitted rows versus scan/filter/recheck/buffer (PERF-R4-01), preservando a query e controle reais; all completo em Node22/PG16 descartáveis e Playwright mutation com servido/fonte comprovados.
6. Após PG descartável e assurance da candidata, preflight do DB local de testes preservado, aplicar apenas migration de templates aprovada por Prisma com lock_timeout5s/statement_timeout60s e interromper em falha/estado desconhecido, sem reset/resolve/retry automático. Build/ativação API-Web locais da fonte aceita e proveniência fonte→imagem→container→HTTP; revalidar HTTPS/conta própria. Operador cria/submete um único modelo textual de teste e consulta status real; sem mensagem ao contato nem promessa de aprovação.
7. Arquitetura aderência/segurança/pcv/TQA/final/debt e guardas; consolidação ao módulo; handoff ST-CON-04 reconverge para consumir o owner estabelecido, em outro contrato aprovado.

### Test Strategy
- **Strategy:** test-first
- **Why:** novo estado persistido + side effect externo + autorização de vendedor.
- **Fail-first target(s) (when required):** API E2E/PG e Playwright da criação/submit/status, duplicate POST e conta alheia.

### Pre-APROVADO RED Evidence Capture (Optional for bugfix/regression)
- **Decision (`required|recommended|not_needed|waived`):** not_needed
- **Why now:** feature nova; diagnóstico por fonte, sem bug ambíguo a reproduzir antes da aprovação.
- **Target symptom:** n/a
- **Allowed surfaces:** none
- **Forbidden surfaces reaffirmed:** production code|runtime/config/deploy|canonical project docs outside TODO authoring
- **Planned command / target:** n/a
- **Status (`not_run|running|red_reproduced|red_not_reproduced|blocked|waived`):** not_run
- **Findings summary:** nenhum teste/produto executado nesta preparação.

### Flow Evidence Planning Matrix (Required Before `APROVADO`)
| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD01/02 editor/vendedor | create/save/readback/preview/submit | web-only | Playwright mutation | yes | yes | e2e/message-templates.spec.ts via canonical runner | n/a |
| DOD03/04 outcome/catalog/status | payload/state/provider lifecycle | web-only | Playwright mutation + PG concurrency | yes | yes | mesma spec + test/message-templates.e2e-spec.ts | n/a |
| DOD05 stale/refresh | race/draft/perda key + dois produtores de observação | web-only | Playwright mutation + PG held-response | yes | yes | A→B→A/save+submit/refresh; catálogo↔individual APPROVED antigo contra PAUSED recente, GET/reload conservam PAUSED e ineligible | n/a |
| DOD06/08 + VAL01/02/03/05 | harness/gates transversais | web-only | browser acima + audits | yes | yes | fonte/servido, DB/porta mesmos de CI-equivalent e guards por critério | n/a |
| DOD07/VAL04 físico | criação na Meta verdadeira | web-only | operador no ambiente local próprio | yes | yes | receipt redigido do submit/status, sem destinatário | fixture não substitui |

### Local CI-Equivalent Suite Matrix (Required Before `APROVADO` and Before Delivery Claim)
Colunas duplicadas de Status projetam o MESMO fato para leitores de guardas com índices distintos; Evidence conserva todas as ressalvas. Não são execuções diferentes.

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status (completion projection) | Evidence Artifact / Command | Status (authority projection) | Notes | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| api / API + PostgreSQL E2E | schema/domínio/Meta/role | bash scripts/test-channels-local.sh all | Local-Implemented | planned | Nenhuma execução atual; npm ci/lint/build/unit/E2E completos, deploy/status | planned | sem subset como aceite | CAS/replay/mesmo nome/tenant/purpose/status/parser + lease de observação compartilhado catálogo↔individual, expiração, held-response e GET/reload PAUSED/ineligible + mesma conta por2Mantenedoras, quota global e contas distintas; rollback real e commit real seguido de perda de ACK de reserva/claim/recibo/release | Node22/PG16 próprios, provider fake determinístico; dois vendedores+admin, ator sem grant e duas BUs/tenants; draft alheio e mesmo revision com keys/atores diferentes |
| web / build+unit+browser | menu/editor/fluxo | bash scripts/test-channels-local.sh all | Local-Implemented | planned | e2e/message-templates.spec.ts e regressões completas; BFF não simulado | planned | mesmo run all | draft/save/submit/status/erro/stale/refresh | DB/API mesmos de CI-equivalent;4173/3100/3101; fonte e bundle servido fresco comprovados |
| root / compose/runner | boundary operacional | bash scripts/test-channels-local.sh all | Local-Implemented | planned | só inventário público positivo/masks falsas; nenhum .env real/.local-files | planned | não tocar namespace humano | montagem/ownership/build de validação | namespace validation exclusivo, sem recurso preexistente |

### Runtime / Rollout Notes
Migration aditiva de modelos/índices/FKs de templates; deploy/status e rollback/lock/timeout primeiro em PG descartável, sem reset humano. Aplicação ao DB local de testes preservado só após preflight e gates, por Prisma, transação com lock_timeout5s/statement_timeout60s e interrupção em erro/incerteza sem repair/retry automático. Preservar dados/canais/índiceST06.  API/Web servidas a partir da principal com comparação de artefatos, não dist antigo. Coorte privada de teste mantém limites do ST-CON-01. Sem novos subscriptions Meta, background job, envio a cliente, política de aprovação local ou deploy/push de produto.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards
- **Issue ID:** PLAN-01
  - **Severity:** medium
  - **Evidence:** user explicitly permits seller submit, current credential resolver gates sending on receipt.
  - **Why it matters now:** reuse send/verify naively either blocks management needlessly or weakens message readiness.
  - **Option A (Recommended):** propósito template-management explícito, mesmo owner/grant/crypto, gate send preservado.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** usar verify/registration como atalho ou desabilitar gate send.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** só criar pelo painel Meta; **Effort:** low; **Risk:** medium; **Blast radius:** local; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** A; pedido deve ser cumprido dentro do produto com boundary explícito.
- **Issue ID:** PLAN-02
  - **Severity:** medium
  - **Evidence:** POST Meta pode resultar em recurso criado mesmo quando resposta falha.
  - **Why it matters now:** repetir mutação gera erro/duplicação e mistura autoria/status.
  - **Option A (Recommended):** operação/revisão duráveis e reconcile GET-only por conta/nome/idioma/definição exatos, sem inferir autoria.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** medium; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** retry automático por erro/timeout.
    - **Effort:** low; **Risk:** high; **Blast radius:** module; **Maintenance burden:** high; **Performance impact:** regresses; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** sem submeter no produto; **Effort:** low; **Risk:** medium; **Blast radius:** local; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** A; registrar limite externo sem exactly-once prometido.

### Failure Modes & Edge Cases
- [ ] Editor e submit de abas diferentes: expectedRevision/fingerprint; active operation imutável.
- [ ] Dois vendedores mesmo nome/idioma; conflito sem divulgação de rascunho privado e sem segundo POST concorrente.
- [ ] Reauth/troca de conta em voo, escopo management ausente ou decrypted key inválida: falha seguro, preserva recibo/account original.
- [ ] Graph recusa/limite, pendente, pausado, categoria alterada, JSON inválido ou ausência de status: não inventar aprovado/vazio.
- [ ] Timeout/crash; match remoto diferente/incerto; late result não altera revisão/contexto novos.
- [ ] Refresh conta/grant diferente ou atrasado: fence de lease/contexto e UI monotônica.

### Residual Unknowns / Risks
- [ ] Aprovação Meta e acesso efetivo da conta ainda precisam prova real; não há garantia de prazo/status aprovado.
- [ ] Outro aplicativo pode criar/alterar modelo na mesma conta; preflight não torna criação externa exatamente-uma-vez.
- [ ] Rascunho privado local e ativo compartilhado da conta são conceitos distintos, explicitados na UI.
- [ ] v1.1 ainda precisa arquitetura/crítica e guards atuais; histórico2019 não autoriza a execução. Depois disso, APROVADO e authority pós-aprovação continuam obrigatórios.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

- **Needed:** no
- **Why ambiguity remains:** n/a; a gate architecture_opinion obrigatória desafiará a direção, sem opinião duplicada.
- **Opinion count:** 0
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required na gate arquitetural
- **Required lenses:** correctness,performance,elegance,structural-soundness,operational-fit

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-template-authoring-20261020/evidence/audit-floor-final-v1.1.json; fresh current GO/8501ca58ebe4 after review convergence; no derived gate downgraded.

| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | v1.1 planned; derivar floor após novo freeze |
| blast_radius | cross-stack | v1.1 planned; derivar floor após novo freeze |
| behavioral_change_or_bugfix | yes | v1.1 planned; derivar floor após novo freeze |
| changes_public_contract | yes | v1.1 planned; derivar floor após novo freeze |
| touches_auth_or_tenant | yes | v1.1 planned; derivar floor após novo freeze |
| touches_runtime_or_infra | yes | v1.1 planned; derivar floor após novo freeze |
| touches_tests | yes | v1.1 planned; derivar floor após novo freeze |
| critical_user_journey | yes | v1.1 planned; derivar floor após novo freeze |
| release_or_promotion_critical | no | v1.1 planned; derivar floor após novo freeze |
| high_severity_plan_review_issue | no | v1.1 planned; derivar floor após novo freeze |
| explicit_three_lane_request | no | v1.1 planned; derivar floor após novo freeze |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

- **Critique decision:** required
- **Why this decision:** big, nova criação externa por vendedor, schema/UX/tenant.
- **Impact signals in scope:** public contract/schema/api|auth|runtime
- **Package mode:** bounded-file-set
- **Package minimum contents:** TODO congelado, código público limitado, parecer arquitetural/disposições, riscos/DoD/matrizes.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; reviewer não executor, aguardar terminal sem prazo arbitrário
- **Critique lenses:** correctness,performance,elegance,structural-soundness,risk
- **Critique status:** no_material_findings
- **Findings summary:** Fresh complete r2 critique terminal3864/strictmerge: no findings; AR-V11-01/02/03 and CR-V11-01 integration confirmed at planning-contract level. Product tests/runtime/provider proof remain planned and unexecuted.
- **Resolution ledger:** Architecture v1.1 and Critique v1.1 Finding Resolution tables; all4 findings Integrated, no waiver; current convergence receipt.
- **Evidence / reference:** artifacts/reviews/leadshug-template-authoring-20261020/evidence/critique-v1.1-r2.raw.json; critique-v1.1-r2.merge.json; planning-convergence-v1.1.md
- **Waiver authority / reference (required if waived):** n/a

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** pressupostos concretos de API/credencial/UI/harness.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01..07
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md
- **Gate status:** no_material_findings
- **Findings summary:** All24 bounded public source hashes still match the actually inspected corpus;7 live assumptions remain concretely anchored. All41 inherited files and3HEADs unchanged; actual code-coherence guard GO, no product tests/code/runtime/private reads.
- **Evidence / reference:** artifacts/reviews/leadshug-template-authoring-20261020/evidence/planning-source-v1.1.json; source-assumptions-v1.1.json; final-planning-source-check-v1.1.json; code-coherence-v1.1.json
- **Waiver authority / reference (required if waived):** n/a

## Approval

- **Approved by:** Usuário, autoridade humana de produto; APROVADO explícito em2026-10-21
- **Approval reference:** Mensagem “APROVADO” em2026-10-21 após pedido de aprovação ST-CON-05 v1.1; proposta publicada a238cb1191a126cd74666098802001aa5287dd67, freeze normativo961dba71015f61a1f1c1badecb9efe090a77b306.
- **Approval scope:** ST-CON-05 v1.1/SCOPE01..05/D01..09 e contratos normativos AR-V11-01/02/03/CR-V11-01, exatamente como revisados/publicados; criar/salvar/prévia/submeter/consultar modelos, testes, migration aditiva no DB local TEST só após descartável/assurance/preflight bounded, ativação API/Web local e uma prova assistida de submit/status. Sem envio ao contato ou execução antecipada ST-CON-04.
- **Execution not authorized by approval:** todo Out of Scope, consumo ST-CON-04 e ações externas durante planejamento.
- **Renewed approval required when:** decisão/critério/risco/paths ou objetivo mudam materialmente.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

Binding reload realizado em2026-10-21 após APROVADO: fontes abaixo lidas diretamente; métodos complementares de schema/query/Vite e módulos atuais carregados. Perfil operational-coder; Genesis excluído por canon/contrato existentes; escopos nestjs,react,vite,postgresql,prisma,docker. Nenhum código/teste antes de authority normal GO e admissão inicial.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | autoridade e roteamento | executor único | código no planejamento | handoff após aprovação |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | aprovação | freeze/reviews/APROVADO | concordância genérica como execução | authority pré/post |
| delphi-ai/workflows/docker/effort-selection-method.md | routing | agent_role_routing_guard.py | fingir modelo primário | guard antes da lane |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | BFF/domínio | adapters finos | regra no controller | contratos E2E |
| delphi-ai/workflows/react/change-ui-boundary-method.md | formulário/estado | freshness/draft | resposta atrasada | Playwright mutation |
| delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | schema | migration versionada | reset operacional | deploy/status descartável |
| delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | intenção/locks | unique/CAS | HTTP em tx | barriers reais |
| foundation_documentation/project_constitution.md | multi-tenant | BU/Contato | credencial global | testes scoped |
| foundation_documentation/policies/scope_subscope_governance.md | rotas existentes | BFF sessão | endpoint fora do owner | contrato explícito |
| delphi-ai/workflows/docker/performance-concurrency-validation-method.md | pcv-1 | quatro lanes | prose sem artefato | JSON/hash antes entrega |

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Subagent / delegation authorization:** main_instructions.md e todo-approval-gates-method exigem executor e reviewers independentes; produto só após APROVADO.
- **Execution topology:** primary-checkout-single-writer
- **Worktree / auxiliary-checkout authorization:** not-authorized
- **Worktree authorization evidence:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

Planned executor routing evidence: artifacts/reviews/leadshug-template-authoring-20261020/evidence/routing-planned-executor-v1.1.json; GO para rota futura, sem dispatch/execução nem aprovação.

Formal-review architecture_opinion e critique: gpt-6.1-sol/xhigh, fresh no-context CLI isolation, guard distinto. Modelo da sessão primária não reconfigurado nem declarado como outro.

## Decision Adherence Validation (Mandatory Before Delivery)

Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Pipeline/Copilot P1/P2 Preflight

Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Rule-Spirit Anti-Pattern Hunt

Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** v1.1 aprovada2026-10-21; implementação/testes em checkpoints seriais, sem entrega completa ainda.
- **Post-commit/push status:** aprovação/admissão e inícioCP01/02 publicados em Foundation main; produto permanece sem commit/push.
- **Next path/status action:** manter active/In-Progress; concluir checkpoints, all e assurance antes de ativação/prova assistida/closeout.

## Security Risk Assessment (Mandatory Before Delivery)

- **Risk level:** high
- **Why this risk level:** vendedor pode criar ativo externo de conta compartilhada; autorização/credencial/contexto são críticos.
- **Attack surface in scope:** BFF sessão/CSRF, owner local/BU/tenant/account, name/key/cursor, XSS/preview, safe error/secret, provider quota.
- **Attack simulation decision:** required
- **Review evidence:** planned após implementação, inclusive vendedor versus ator sem grant/foreign draft/channel e cursores/erro/secret.
- **Residual security risk:** conta externa compartilhada é autoridade dos ativos; drafts locais não são expostos entre autores sem direito administrativo; coorte privada atual preservada.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** escrita externa e concorrência com webhook e UI.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | pending | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | pending | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-E3 | pending | external ambiguity explicit | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E1 | pending | none | none |

### Lane Detail Packet Template
#### EPS
- **Trigger rationale:** listagem/lookup scoped de drafts/observações e reserva de nome; EXPLAIN ANALYZE com amostra cardinalidade, limite de página e budget externo. Sem N+1/catalog fan-out.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-05
- **Evidence object:** pending; JSON pcv-1 com sha256 antes da entrega, não existe execução ainda.
#### FRC
- **Trigger rationale:** save+submit e atraso em troca BU/canal/draft; Playwright real, rastrear requests e estado no backend.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-05
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### BCI
- **Trigger rationale:** barreiras PG/contador HTTP, submit e reserva de nome, crash antes/depois POST e reconcile seguro; provar também coordenação da mesma conta entre tenants e Local Commit Certainty Contract com PG real (rollback e commit concluído seguido de erro na borda de ACK); provar invariantes D-06/07 com nova instância de serviço sobre PG durável, GET observacional antes do POST recovery, dois recuperadores e executor/resposta tardios, não apenas throw na request viva.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-05
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### RLS
- **Trigger rationale:** pequeno ensaio de concorrência/load bounded do novo fluxo/listagem no PG descartável; não claim SLO ou produção.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-05
- **Evidence object:** pending; resolver recomendação com evidência ou waiver válido até o deadline, sem deixar pendente na entrega.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

- **Audit outcome:** high
- **Why this outcome:** não implementado; toda evidência de produto pendente, sem claim de entrega.
- **Inline code TODO debt:** none
- **Evidence / audit artifact:** planned após implementação
- **Accepted residual debt:** none; dependência externa não é waiver.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Audit decision:** required
- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
- **Required evidence matrix (when architectural):** unit|integration|web real-backend
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
- **Canonical method:** wf-docker-independent-test-quality-audit-method
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** planned após implementação
- **Audit status:** not_run
- **Findings summary:** none; nenhuma auditoria de entrega executada
- **Evidence / reference:** planned após implementação
- **Waiver authority / reference (required if waived):** n/a

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Final review decision:** required
- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
- **Required evidence matrix (when architectural):** unit|integration|web real-backend
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
- **Canonical method:** wf-docker-independent-final-review-method
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** planned após implementação
- **Final review status:** not_run
- **Findings summary:** none; nenhuma auditoria de entrega executada
- **Evidence / reference:** planned após implementação
- **Waiver authority / reference (required if waived):** n/a

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** not_needed
- **Why this decision:** rota aditiva sem dual-write/compatibilidade temporária ou remoção de legado; owner único preservado. Reclassificar se implementação introduzir bridge.
- **Cutover signals in scope:** none
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** n/a
- **Cutover audit status:** not_run
- **Findings summary:** none
- **Evidence / reference:** D-03/06/07 e arquitetura requerida
- **Waiver authority / reference (required if waived):** n/a

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Module Consolidation Gate (Required Before `Completed`)

Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Commands (Run Locally)

Guardas de planejamento após freeze; produto somente depois de APROVADO: bash scripts/test-channels-local.sh all. Nenhum teste/build/account call atual.

## Files Expected (Compatibility Note)

Diff Expectation Contract governa os paths, sem autorização de mudanças além dele.

## COMENTÁRIO:

Nenhuma pergunta de produto material pendente.

## Frontend / Consumer Matrix and BFF Contract

| Producer / endpoint | Consumer | Auth/owner/body | Effect / evidence |
| --- | --- | --- | --- |
| GET /api/bff/business-units/:buId/channels/:channelId/message-template-capabilities | BU/canal selector/editor | sessão/grant ATENDENTE+; somente DB/contexto público safe | disponível/explicação/gen corrente, sem provider/token |
| GET /api/bff/business-units/:buId/message-templates?view=mine&page=1 | meus rascunhos/list | scoped creator; view=bu só ADMIN+;20/50limite | local somente, ordem createdAt/id e page/temMais |
| POST /api/bff/business-units/:buId/message-templates/preview | editor/prévia | sessão/grant ATENDENTE+ e CSRF; {channelId,expectedGeneration,draftId?,expectedRevision?,definition} | leituras autorizadas permitidas; zero escritas DB/chamadas provider; definição normalizada/texto plano/fingerprint e contexto safe; unpersisted não habilita submit |
| POST /api/bff/business-units/:buId/message-templates | editor | ATENDENTE+ e CSRF; {clientRequestId,channelId,expectedGeneration,name,language,category,body,header?,footer?,examples} | draft revision1, conta derivada no server, nenhum POST Meta |
| GET/PATCH /api/bff/message-templates/:id | editor/save/reopen | own draft ou ADMIN BU; PATCH {expectedRevision,definition} | GET observacional, PATCH CAS; DTO safe |
| POST /api/bff/message-templates/:id/submit | confirmação vendedor | owner/admin, sessão/CSRF, key UUID; {expectedRevision,expectedGeneration,expectedDefinitionFingerprint} | operação persistente; até1POST Meta, nunca /messages |
| GET /api/bff/message-templates/:id/operations/:operationId | recovery/readback | mesma BU+owner/admin; ID scoped, sem key browser | resultado seguro e última observação; GET sem mutação/provider |
| POST /api/bff/message-templates/:id/operations/:operationId/reconcile | recuperar processo interrompido/resultado incerto | owner/admin, sessão/CSRF | lease vivo202; PREPARED vencido REJECTED sem dispatch; SENDING vencido AMBIGUOUS; CAS e GETs Meta bounded conforme tabela; nenhum POST Meta |
| POST /api/bff/message-templates/:id/refresh | Atualizar status | owner/admin, sessão/CSRF; identidade conta original revalidada | leitura remota bounded, MESMO lease/fence de conta/contexto e observação usados pelo catálogo |
| GET/POST /api/bff/business-units/:buId/channels/:channelId/message-template-catalog | modelos da conta | ATENDENTE+; GET cache local pagina, POST refresh com {after?} e CSRF | uma página externa por ação/sem fan-out; MESMO lease/fence e projector do refresh individual; id/nome/idioma/components/status/fingerprint/support; reutilizável por consumer futuro |

**Field Definitions:** draft local: DRAFT (editável sem submissão/ativo externo), LOCKED (revisão congelada em submit/resultado externo ou incerto). SubmissionOutcome: PREPARED (nenhum dispatch), SENDING (dispatch reservado), ACCEPTED (ID conhecido), REJECTED (recusa comprovada), AMBIGUOUS (resultado desconhecido). ProviderApprovalStatus: PENDING/APPROVED/REJECTED/PAUSED/DISABLED/ARCHIVED/DELETED/IN_APPEAL/PENDING_DELETION/LIMIT_EXCEEDED/UNKNOWN conforme observação externa; UNKNOWN não é aprovação. Category: MARKETING (abertura/oferta comercial) ou UTILITY (atualização transacional legítima); categoria efetiva Meta separada da solicitada. Purpose template-management gerencia ativo sem enviar mensagem; send mantém gate anterior.

Statuses de HTTP:401 sem sessão,403 papel insuficiente em BU conhecida,404 recurso/autor alheio sem direito,409 revisão/conta/nome/key conflitante,202 operação em andamento,201 novo draft/submissão aceita,200 leitura/replay,429 limite com retry-after safe,503 provider inconclusivo com outcome safe. Nunca retornar mensagem/bruto/URL/token do provider. Rejeição Meta de análise é providerStatus REJECTED, não erro de transporte e não falha fictícia de criar.

## Planning External References — consulted 2026-10-19

Primary Meta documentation read as public official Markdown, no account calls: [Fundamentals](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview/), [Components](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/components/), [Review](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-review/), [Template API](https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-account/message-template-api/), [Meta Postman lookup by name](https://www.postman.com/meta/whatsapp-business-platform/request/7whkjje/get-template-by-name-default-fields), [Meta SDK lookup parameters](https://github.com/facebook/facebook-python-business-sdk/blob/main/facebook_business/adobjects/whatsappbusinessaccount.py#L913). Defines account asset/creation/examples/limits/approval states. Product subset and privilege are explicit local decisions, not asserted provider restrictions.

## Module coherence — one-to-one

D01: user vendor create+submit, internal role/grant preserved. D02: Meta component subset, own TODO fulfills constitution. D03: backend owner/persistence preserved, No Prior Decision for draft. D04: scoped credential preserved, new management purpose does not alter send. D05/D06: HTTP outside tx and no secrets preserved, new mutation governed by own operation. D07: Meta authority/status and provider adapter preserved. D08: freshness patterns preserved, firstsend stays separate ST-CON-04. No constitutional invariant or runtime auth surface is changed.

## Architecture Review Resolution Ledger — 2026-10-19

| Finding | Disposition | Contract/evidence |
| --- | --- | --- |
| AR-01 | Integrated | D04/07/08: activeCredentialVersion e contexto no CAS; observação stale após300s; elegibilidade futura revalidada por ST-CON-04 |
| AR-02 | Integrated | D02 + endpoint preview: backend autoritativo, sem import cross-repo, preview unpersisted não libera submit |
| AR-03 | Integrated | D05/06 lookup por nome server-side; match exato + esgotamento bounded; Postman Meta/SDK primários |
| AR-04 | Integrated | D05/06 requestFingerprint versus remoteSemanticFingerprint; exemplos imutáveis, sem normalizar texto, CORRELATED_BY_DEFINITION sem autoria |
| AR-05 | Integrated | D01/DOD01/CI/segurança: só OWNER/ADMIN/ATENDENTE; negativos sem grant/draft alheio, nenhum papel novo |
| AR-RUNNER | Integrated | passo2 exige boundary positivo ANTES de qualquer execução de teste |

Raw MetaHttpClient contract tests são obrigatórios além de browser (que substitui META_CLIENT): verificar query/body/classificação de erro, nenhuma mutação durante reconcile. Mesmo revision/keys/atores diferentes provoca no máximo um POST; same-generation replacement, stale preview/refresh, APPROVED→PAUSED e ambiguidade pós-efeito compõem harness obrigatório. Relatório independente é evidência de planejamento, não implementação.

## Recovery Transition Contract — CR-01

GET de draft/operação permanece observacional: retorna phase/leaseExpiresAt e recoveryAction safe derivada do relógio do servidor, sem transição ou provider. UI oferece Recuperar resultado após lease expirar; nenhum polling/worker/auto-resubmit. Mesmo key de submit retorna recibo/operação original; key nova enquanto bloqueado retorna409 RECOVERY_REQUIRED com ID autorizado, sem dispatch. Recovery é somente POST /operations/:operationId/reconcile com sessão/CSRF e autorização corrente, sobre a MESMA operação persistida, transação curta com CAS de versão/lease/dispatch claim.

| Persisted outcome / condition | Authorized reconcile action | Reservation and editability |
| --- | --- | --- |
| PREPARED ou SENDING, lease vivo |202 mesma operação, zero provider; caller original conserva claim | permanece reservado/LOCKED |
| PREPARED, lease expirado | CAS para REJECTED(dispatched=false); nenhum provider, executor vencido não pode reclamar nem despachar | liberar reserva e currentOperation por CAS se ainda aponta à operação; draft DRAFT; nova edição/revisão/key explícitas |
| SENDING, lease expirado sem recibo conhecido | CAS para AMBIGUOUS(dispatched=unknown); nunca retornar PREPARED; bounded GET-only reconcile sob novo lease de recuperação | reserva e revisão LOCKED |
| AMBIGUOUS | bounded GET-only e semantic match D06, com lease/CAS, zero POST externo | match único vira ACCEPTED com proveniência; ausência/divergência/erro permanece AMBIGUOUS/LOCKED/reserva retida |
| REJECTED por recusa de submissão comprovada | devolver recibo terminal original, zero provider | liberar reserva/currentOperation por CAS, draft DRAFT; request antiga imutável; revisão/key novas para tentar novamente |
| ACCEPTED | devolver recibo/observação; atualizar análise só pela ação refresh existente | revisão LOCKED/reserva associada ao ativo; análise Meta REJECTED não desfaz aceitação; variação é novo draft/nome |

Recuperadores concorrentes não tomam a mesma versão/lease; perdedor retorna202/409 safe sem provider. PREPARED vencido perde toda autoridade de dispatch. Resultado tardio válido do dispatch original pode enriquecer apenas seu recibo histórico (provar dispatch claim/ID da operação), nunca reabrir draft novo, alterar revision nova ou certificar credencial/contexto corrente; preserva identidade remota e associação única. Tombstones/história e requestFingerprint antigos conservados. Não há limpeza Meta ou retry POST automático.

## Submission Error Classification Contract — CR-02

Adapter de templates usa resultado tipado próprio; não deduz certeza de MetaIndisponivelError genérico nem altera silenciosamente semântica dos consumers de envio/cadastro atuais. Validar shape/código/phase, não comparar texto de message/details. Nunca expor erro bruto/tokens/URLs a UI/log.

| Phase / evidence | Submission result | Required behavior |
| --- | --- | --- |
| antes do CAS SENDING/dispatch; validação/grant/preflight/timeout/429/lease falha | REJECTED(dispatched=false) | zero POST; liberar reserva por CAS e permitir nova revisão/key explícitas; histórico/replay preservados |
| após dispatch; JSON success estruturalmente válido com ID não vazio | ACCEPTED | ID/conta originais duráveis; status de análise separado, desconhecido não vira aprovado |
| após dispatch; HTTP400/401/403, envelope Graph error válido, sem ID/success concorrente, is_transient não true, error.code na allowlist10/100/190/2388040/2388047/2388072/2388073/2388293/2388299 | REJECTED(dispatched=true, provenNoCreation=true) | recusa síncrona conhecida de autorização/parâmetro/formato; liberar reserva por CAS; subcode isolado e message nunca bastam |
| após dispatch; timeout/desconexão, crash, 5xx,429, redirect, body inválido/semID, código desconhecido, code1/2, is_transient true ou qualquer evidência inconclusiva | AMBIGUOUS | reserva/LOCKED, nenhuma repetição POST; oferecer recovery GET-only; retryable não prova ausência de efeito |
| ativo ACCEPTED cuja análise posterior retorna REJECTED | ACCEPTED + ProviderApprovalStatus.REJECTED | manter ID/recibo/revisão, mostrar recusa de análise; variação explícita em novo draft |

Allowlist é decisão conservadora local apoiada no catálogo primário [Meta error codes](https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes/), lido em Markdown oficial em2026-10-19. 429 pós-dispatch permanece incerto mesmo quando há rate-limit conhecido; respeitar backoff sem retry mutante. Contratos raw HTTP exercitam todas linhas, códigos parecidos/desconhecidos, payload contraditório e efeito provider seguido de erro inconclusivo. Sem depender do fake BFF/browser para provar o wire.

## Critique Resolution Ledger — 2026-10-19

| Finding | Disposition | Contract / evidence |
| --- | --- | --- |
| CR-01 medium | Integrated | Recovery Transition Contract, D03/06 e endpoint reconcile, harness BCI inclui processo perdido/serviço novo/GET observacional/recuperadores concorrentes/late executor |
| CR-02 medium | Integrated | Submission Error Classification Contract; allowlist restrita primária, default pós-dispatch AMBIGUOUS; adapter raw tests e estado de análise separado |
| CR-03 low | Integrated | D02/endpoint preview: leituras autorizadas permitidas, zero escrita DB/provider; sem exigir auth impossível sem DB |

Delta review independente terminal contra0d4957b3: CR01..03 convergiram sem achado material remanescente. Nenhum produto executado.

## Historical Pre-approval Planning Gate Receipt — 2026-10-19 (reframing2026-10-20)

| Check | Actual outcome | Evidence |
| --- | --- | --- |
| architecture_opinion + fresh critique/delta | findings integrated; no material delta finding | architecture-opinion.md, critique.md, critique-delta.md |
| audit escalation | go;8501ca58ebe4 | evidence/audit-floor.json |
| assumption/code coherence | go;5 live assumptions | source-assumptions.json; evidence/code-coherence.json |
| reviewed scope drift | go;23 sections,0 material changes versus0d4957b3 | evidence/scope-drift.json |
| planned executor routing | go; no executor dispatched | evidence/routing-planned-executor.json |
| pre-approval authority | preflight-go; execution_authority_granted=false | evidence/authority-preapproval.json |
| TODO structure / lifecycle | PASS / exit0 | evidence/structure-final.json; evidence/planning-validation.json |

Todos os artifacts acima pertencem a artifacts/reviews/leadshug-template-authoring-20261019/. Nenhuma suite de produto, migration, publicação de runtime ou chamada de conta Meta foi executada nesta preparação. Próxima autorização é APROVADO específico do ST-CON-05; concordância funcional anterior não a substitui.

## Reframing — Channel abstraction request, 2026-10-20

ST-CON-05 conserva o objetivo funcional e permanece sem APROVADO específico de implementação. Nova direção humana exige Channel abstrato, concretos de WhatsApp e resolução/injeção scoped; preparar ST-CON-06 antes deste consumer. [Enquadramento e evidência](../../../artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md).

Decisões, pareceres e guardas de2026-10-19 descrevem o pacote então revisado; não são aprovação/readiness do contrato que será rebaseado. Este registro apenas invalida a indicação anterior de pronto para aprovação e preserva o histórico; assinaturas/paths/baseline serão reconvergidos no próximo ciclo de refinamento/reviews/guardas, sem adaptar código antecipadamente.

## Handoff recebido de ST-CON-06 v1.3

Fonte/cutover e quatro PCV convergidos; all93791/613testes, ativação local e nova troca física IN/OUT nos dois canais confirmadas. ST-CON-06 está encerrado localmente: revisão final sem findings e guards GO registrados no mesmo TODO concluído. Consumir agora os contratos canônicos de Channel/Resolver e OutboundService em modules/integrations-and-channels.md e modules/inbox-and-conversations.md. Não há aprovação de implementação desta história: reconvergir seu próprio contrato, fonte/baseline e revisões antes de novo APROVADO.

Preserve the explicit user decision: the seller creates the draft **and submits it to Meta for approval**. Do not insert an administrator approval step. The operator currently has no approved text template in the account used by LeadsHug.

Rebase the planning contract on Channel/ChannelResolver, common outbound outcomes and scoped credential ownership once06 converges. Template authoring/catalog/submission is a separate narrow capability contract: it must not add unsupported methods, no-op implementations, concrete instanceof checks or protocol fields to the universal text Channel port. No real future-network implementation is implied by this extension point.

The contract still needs to define the seller's authorized BU/channel scope, draft ownership, validation, submission/approval/rejection states, version/edit/resubmission semantics, parameter rules, safe errors, Meta status synchronization and user-facing mutation evidence. A saved draft or submitted request is not an approved template. Approval material and external requirements must be verified from current primary Meta sources during that story's planning, rather than inferred from06 text-send tests.

### Follow-up herdado ST06-DEBT-PERF-R4-01

Work item de manutenção de teste, owner API performance-test maintainer, originado em ST-CON-06 v1.3. Na próxima alteração ordinária dos testes PCV, diferenciar linhas emitidas de trabalho de scan/filtro/recheck/buffer; não interpretar ActualRows×Loops arredondado como contagem universal de visitas. Plano atual sem filtro/recheck residual: dívida baixa, sem defeito de runtime ou bloqueio da entrega06. Incorporar este item explicitamente ao refinamento/review da história05 antes de qualquer edição; a direção de planejamento não autoriza alterar produto agora. Evidência e racional: ../artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-round4-resolution.md.


## Rebase v1.1 — current review authority

Profile strategic-cto, technical scope NestJS/React/Vite/Prisma/PostgreSQL/Docker; Genesis ruled out by existing canon. verify_context PACED-Ready. Product/runtime/test changes are prohibited during this planning turn. Source and protocol inspection are read-only/public-only. Existing explicit seller-submit direction is preserved; no admin approval, recipient send, production or future networks are introduced.

### Current source inheritance and approval boundary

Current product principal working tree contains delivered06 changes not yet committed in product repositories, which this planning does not authorize committing. The exact inherited manifest defines the public baseline; ExpectedPaths rows for inheritance only are not mutation authority. Antes da primeira mutação ou teste05, conferir HEADs e TODOS41hashes, inclusive os11compartilhados admitidos, contra a baseline imutável publicada. Só depois, manter30hashes selados e rever deltas compartilhados contra a origem; drift inicial bloqueia e exige atribuição/review, sem rebase silencioso. Future05 approval covers only actively admitted paths and this mandatory seal, not arbitrary modification of06. No writable checkout/copy or new branch is used.

### Current Meta reference receipt

Public official pages were read with Accept:text/markdown (HTTP200) after the web renderer returned429. Fresh metadata/facts and source links are in primary-meta-reference-v1.1.md. No access token, provider account call or SDK-installation operation was used. Name128, variables20, examples128, pt_BR-only, local quotas60/hour and freshness300s are product restrictions; they are not represented as Meta global limits. Meta documentation states name maximum512 and category-dependent rules; only text/body/header/footer subset is admitted here. The backend wire parser remains conservative; fixtures alone never certify account readiness.


## Local Commit Certainty Contract — AR-V11-01

SubmissionOutcome de domínio e certeza de persistência local são dimensões distintas. `receiptPersistence` é RECORDED somente com confirmação positiva do commit ou readback exato; caso contrário UNCONFIRMED. `providerAcceptance` é CONFIRMED somente depois de ACK estruturalmente válido com ID não vazio; antes dele permanece UNKNOWN. Nenhum erro local é prova de recusa externa. Contexto/operationId/requestHash/dispatchClaimId são capturados e nunca substituídos por tentativa/conta/revisão novas.

| Boundary / uncertain result | Required action and response | External mutation and reservation |
| --- | --- | --- |
| PREPARED/name reservation transaction throws, before or after possible commit | Zero POST. Fazer no máximo1rotina de readback bounded no primário pela mesma key/ator/BU/payload e operationId capturados, com autorização antes de lookup. Recibo positivo retorna202/estado conhecido; ausência/erro não comprova rollback, retorna503 TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE/receiptPersistence UNCONFIRMED com instrução de consultar a mesma operação/key. | Não despachar nessa request após reserva incerta, mesmo se readback localizar PREPARED. Não soltar reserva/estado por compensação inconclusiva; recuperação/replay existentes mantêm identidade e lease. |
| CAS PREPARED→SENDING/dispatch claim throws | No máximo1readback bounded da MESMA operação/dispatchClaimId/contexto/revisão/lease. Só claim persistido exato, SENDING corrente e lease válido confirmados positivamente permitem o único POST da execução original, se nenhum POST foi iniciado. Caso contrário, parar com503/UNCONFIRMED e zero POST. | Nenhum novo claim/key/rebind por erro; SENDING incerto conserva reserva e ação de recuperar. Executor vencido não obtém autoridade por um recibo velho. |
| POST retorna ACK válido/ID, mas gravação/finalização local falha ou commit tem ACK perdido | External outcome continua ACCEPTED/providerAcceptance CONFIRMED. No máximo1readback bounded pelo owner/operação/claim/conta/ID capturados; RECORDED só se recibo/snapshot/proveniência exatos estão positivamente confirmados. Caso contrário503 TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE com outcome ACCEPTED/receiptPersistence UNCONFIRMED, operationId autorizado e texto fixo “A Meta aceitou o cadastro, mas a conclusão local não foi confirmada; consulte esta operação antes de continuar”. | Nunca REJECTED/“não criado”, nunca liberar nome, apagar recibo ou repetir POST. Rollback local confirmado não apaga a criação externa. Recuperar somente a mesma operação; merge tardio monotônico, análise APPROVED continua separada. |
| Prova de recusa ou PREPARED vencido, mas commit de recibo/liberação é incerto | Resposta conserva a evidência conhecida e receiptPersistence UNCONFIRMED, sem afirmar que a reserva foi liberada. No máximo1readback consistente bounded da operação e sua reserva/currentOperation; só confirmação positiva certifica REJECTED local/reabertura. | Liberação atômica com CAS do owner/operação/claim e transição de draft, sem compensação que possa apagar nova reserva. Não autorizar novo POST nessa request nem replay automático. |

Readback bounded é uma rotina com no máximo3queries locais indexadas (operação/claim, reserva, current revision), sem provider, espera infinita ou nova escrita; se usar transação, ela é somente de leitura e curta. GETs continuam observacionais; recuperação mutante local usa o POST reconcile autorizado e as regras PREPARED/SENDING/AMBIGUOUS existentes. Commit incerto não se resolve liberando lock ou trocando key. A falha de persistência após ACK conhecido é erro local, não “provider indisponível”. Não há worker, outbox ou segunda operação genérica.

Harness obrigatório: transações PostgreSQL reais com falha antes do commit/rollback e erro de ACK na borda depois de commit real, não DB simulado. Independente readback comprova linhas/claim/reserva/revisão e contador HTTP prova0POST sem confirmação/1POST somente após claim próprio confirmado. Incluir reserva, claim, recibo ACCEPTED e liberação REJECTED, readback indisponível, outro recuperador e resultado tardio. O defeito pós-commit é injetado na borda do retorno da transação real, sem forjar estado ou substituir a persistência; provas after-commit não serão rotuladas como queda real da rede PostgreSQL.

## Shared Account Coordination Contract — AR-V11-02

Uma conta Meta pode aparecer por telefones/vínculos verificados de mais de uma Mantenedora; esta história não cria exclusividade de ownership WABA→tenant. Persistir chave técnica canônica provider/account, derivada exclusivamente do recurso autenticado server-side. Nome/idioma e quota de dispatch usam esse namespace global na instalação, não mantenedoraId como componente da unicidade. Manter índices/unique de reserva e contador durável nesse owner técnico. Operações, definições, rascunhos e observações continuam scoped por Mantenedora/BU/autor; o namespace global não armazena esses conteúdos nem é DTO de usuário.

Autorização corrente precede lookup/claim de coordenação. Conflito de nome já reservado por outro tenant retorna409 com mensagem fixa de indisponibilidade do nome, sem ID de operação/draft/tenant/autor/conteúdo alheio. Quota global retorna429 com retry-after safe sem contagens/dados de outros tenants. Ler/gravar a coordenação técnica global não concede acesso ao recibo ou rascunho estrangeiro. Catálogo remoto continua vinculado à conta autorizada do canal e sua projeção local não mistura rascunhos privados. Liberações tardias só operam sob CAS da reserva da mesma operação/claim.

PG/provider tests obrigatórios: dois canais/números distintos da mesma conta na mesma Mantenedora e em duas Mantenedoras, grants válidos separados; nomes iguais concorrem por uma reserva e no máximo1POST. Perdedor vê conflito safe sem recibo estrangeiro. Quota agrega dispatches de todos esses vínculos. Mesmos nomes/idiomas em contas diferentes são independentes. Include foreign BU/actor negativas para assegurar que não alcançam a coordenação ou provider. Esta coordenação cobre a instalação LeadsHug, não mutações de outros apps na Meta.

## Initial Inherited Source Admission Contract — AR-V11-03

Antes da primeira edição ou teste05, conferir root/API/Web HEADs e TODOS41records do manifesto contra os bytes exatos do manifesto aprovado no freeze Foundation, incluindo11paths shared que serão editáveis depois. Public source files only: sem stat/discovery privado. Registrar recibo explícito com as41comparações e resultado; qualquer mismatch interrompe para identificar origem/impacto e reconvergir review se material. Não “atualizar a baseline” automaticamente.

Após admissão, os30inherited não ativos permanecem byte-exatos em cada checkpoint/entrega. Nos11shared, guardar a origem imutável pública no pacote/referência Git Foundation e revisar o delta estritamente05; a lista ExpectedPaths não substitui essa análise. Novos arquivos passam pelo guard estrito de paths. Nenhum produto commit, checkout/cópia auxiliar ou varredura privada é necessário para provar esse contrato.


## Architecture v1.1 Finding Resolution

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| AR-V11-01 | Integrated | useful | yes | project | n/a | D05/06 + Local Commit Certainty Contract distinguish claim/receipt/release certainty, bounded captured readback, known Meta acceptance and no premature release/POST; realPG pre/post-commit fault harness planned. |
| AR-V11-02 | Integrated | useful | yes | project | n/a | D05 and Shared Account Coordination Contract adopt global canonical account/name/language reservation/quota, preserve scoped business data and safe cross-tenant conflicts; same-account cross-tenant versus different-account PG proof planned. |
| AR-V11-03 | Integrated | useful | yes | project | n/a | Initial admission compares3HEADs and ALL41 hashes before first mutation/test;30sealed and shared-delta proof continue thereafter. Manifest records unchanged; only enforcement strengthened. |

Raw architecture21346 terminal0, strictmerged. Direction/capability accepted as simplest faithful path; material planning gaps integrated, not waived. Fresh critique must assess the complete evolved contract and these exact resolutions. No implementation or actual management/provider proof inferred.


### PCV fixture realism for v1.1

EPS: synthetic high-cardinality drafts/operations/catalog observations, scoped list pages20/50, actual SQL/EXPLAIN plans and index/storage/write effects; emitted/filter/recheck/buffer work kept distinct, no capacity claim. FRC: held preview/save/submit responses with retriggers, A→B→A and identical edited text, reload/no-browser-key recovery against real BFF/PG. BCI: 5waves×20 independent operation intents with controlled distinct account namespaces/users or admitted deterministic clock so configured quotas are not silently bypassed; prove each owned row/POST result separately. Separate same-account two-BU/two-tenant contention has intentionally one winner/safe conflicts; quota saturation has expected429 and no extra POST, not a fabricated100success sample. Fault controls execute real PG commits/rollbacks and independent readback, not a mocked repository state. RLS: bounded concurrent scoped reads/dispatch fixture mix and foreign404 cases with clear rate-limit expectations, no actual account load or production SLO. Every fixture/clock is validation-only DI, no test flag/seed bypass in production and no lower evidence floor to make the numbers fit.

## Shared Observation Fence Contract — CR-V11-01

Refresh individual do rascunho e refresh de uma página do catálogo são dois produtores da MESMA observação de status. D07 exige um único owner/projector e UM lease compartilhado por contexto autorizado de conta, não um lease por rota ou por rascunho. Chave contém Mantenedora/BU/canal/referência canônica da conta/generation/epoch/managedIdentity/activeCredentialVersion; dados de negócio continuam scoped e não são compartilhados entre tenants. A coordenação global de nome/quota de AR-V11-02 não concede acesso a observações de outro contexto.

- Após autenticação/grant/contexto e antes de qualquer leitura remota, ambos os endpoints adquirem o mesmo lease por CAS em transação curta. Cada aquisição incrementa um fence monotônico persistido; ownerId é único. Lease vivo de qualquer produtor impede outro:202 REFRESH_IN_PROGRESS com retryAfter seguro, zero provider e nenhuma alteração na observação. Debounce10s vale para os dois produtores, sem duplicar chamadas por alternância de rota.
- Uma atualização individual ou uma página de catálogo tem no máximo grant GET + um GET de template/página, timeout10s por GET e budget30s; lease60s. HTTP ocorre fora da transação. Nenhum fan-out, worker ou lock de transação mantido durante provider I/O. Expiração permite aquisição explícita posterior com fence maior; não reaproveita claim vencido nem faz retry automático.
- A conclusão grava em transação curta somente se owner/fence ainda correspondem ao lease corrente, lease está vivo e todo contexto capturado continua atual. O CAS protege conjuntamente observações, lastObservationFence, observedAt, disponibilidade/staleness, observedEligible e cursor/metadata de página. A chave da observação é contexto + remoteTemplateId; ambas as rotas atualizam a mesma linha lógica/projetor, e DTO de draft/catálogo/GET/reload deriva dela. O snapshot de criação permanece imutável. Uma página não infere exclusão por ausência.
- Resposta cujo fence/lease/contexto perdeu validade não grava nem status nem erro nem timestamp/cursor, não libera lease de outro dono e retorna409 TEMPLATE_REFRESH_SUPERSEDED seguro. O consumidor também aplica seu fence monotônico de UI. Se a consulta atual falhar, conserva status anterior com unavailable/stale e observedEligible=false somente sob o MESMO CAS; erro antigo também não sobrescreve sucesso novo. Liberação de lease compara owner/fence/contexto; falha/incerteza de commit usa no máximo um readback primário bounded pelo contexto/fence, sem afirmar gravação/liberação não comprovadas, sem compensating delete nem novo HTTP.
- Prova obrigatória PG real, provider de resposta retida e relógio DI exclusivo de validação: (a) catálogo captura APPROVED e fica retido, lease expira, refresh individual com novo fence persiste PAUSED, catálogo antigo conclui e é rejeitado; (b) mesmo caso invertendo endpoints; (c) produtor concorrente enquanto lease vivo recebe202 e zero provider; (d) sucesso/erro/lease-release antigos após novo owner não alteram observação/metadata; (e) conta/generation/credencial diferentes permanecem fenced/scoped. Em (a)/(b), verificar linha/fence persistidos, contagem de chamadas e GETs de catálogo e draft; Playwright real faz reload e mantém PAUSED/observedEligible=false. Falha de frescor300s continua independente e nunca reaprova.

## Critique v1.1 Finding Resolution

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CR-V11-01 | Integrated | useful | yes | project | n/a | D07/baseline, API/flow/CI matrices and Shared Observation Fence Contract specify common lease/fence and bidirectional PG/browser held-response proof. Fresh full r2 critique terminal3864/strictmerge confirms integration with no findings. |

## Current Pre-approval Planning Receipt — ST-CON-05 v1.1

Architecture21346 and full critiques16799/3864 terminal0 with strict merge; all4medium findings integrated, current critique no findings. Code coherence GO for7live assumptions; scope drift GO/23unchanged sections against published961dba71 plus4extended normative contracts unchanged; source24/inherited41/product3HEADs unchanged; deterministic TODO PASS, strategic-cto scope in-scope, Foundation lifecycle GO and audit-floor GO. Authority preflight returns preflight-go with execution_authority_granted=false. Full current receipts are in artifacts/reviews/leadshug-template-authoring-20261020/evidence/.

Plan is ready for explicit human APROVADO v1.1, not implemented. Pending delivery gates,613old tests and actual06INOUT are not05results. Approval proposal covers the exact listed surfaces and limits, additive migration on preserved local TEST database only after disposable/assurance preflight and bounded timeouts, source-bound local API/Web activation and one assisted test-template submit/status query. No recipient message, product commit/push/deploy or Meta account configuration is authorized by this planning receipt.

## Execution Admission — 2026-10-21

APROVADO v1.1 registrado acima, binding10fontes recarregadas; readiness PACED-Ready. Manifesto imutável da proposta a238cb11 conferido:3HEADs e41hashes exatos (11shared admitidos depois da admissão;30sealed continuam protegidos a cada checkpoint). Recibo: artifacts/reviews/leadshug-template-authoring-20261020/evidence/initial-execution-admission-v1.1.json. Routing executor gpt-6-luna/medium/principal-single-writer GO em routing-executor-approved-v1.1.json. Nenhuma mutação/teste de produto iniciada até este recibo; authority normal retornou GO/execution_authority_granted=true em authority-approved-v1.1.json antes do handoff CP01 ao executor stcon05_executor. Pipeline/gitlinks, private paths/env e produto commit/push continuam excluídos.

### CP01 — domain foundation handoff

Executor stcon05_executor (gpt-6-luna/medium), único writer de produto no principal, iniciado sob authority GO. Owned paths deste checkpoint: somente api-app/src/domain/message-templates/**. Objetivo: ports/DTO/contexto seguro, parser/prévia/fingerprints e testes/harness independentes da capacidade; sem schema/HTTP/UI/runtime humano ainda. Root mantém TODO/README/receipts Foundation; evidência cp01* do executor fica disjunta. Teste apenas após releitura do runner público/CI e selo30sealed; all completo continua gate de aceite posterior. Handoff não reduz escopo/provas aprovadas e checkpoint não equivale à entrega.

### CP01 disposition and CP02 handoff

CP01 base de domínio/parser/prévia/ports/harness recebida e5arquivos lidos pelo root; relatório estruturado em evidence/cp01-executor-report-v1.1.json. RED/GREEN api (230unit/338PG, lint/build/migrate/status) vêm do relatório do executor; stdout não foi salvo e nenhum hash de log foi inventado. Não substitui all/durabilidade/assurance/consumidor real. Root reconferiu30sealed byteexact; executor reportou41sem drift antes de avançar.

CP02 autorizado serialmente no mesmo contrato: src/domain/message-templates/**, schema.prisma, novas migrations *_message_template*/migration.sql, test/message-template*.e2e-spec.ts e helpers.ts se necessário ao novo domínio. Persistência Prisma/PG real de rascunhos/revisões, owner+BU+tenant, idempotência de criação, CAS concorrente e prévia read-only; provider fake só na porta externa, zero chamadas remotas nestes fluxos. Sem camada fake-storage que duplique CAS de produção. DTOs/ports podem ser enriquecidos dentro de D09 para próximos passos. HTTP real de integração/BFF/UI e aplicação ao banco humano continuam checkpoints posteriores. CP02 deve persistir logs reais em artifacts/tmp e recibos cp02* antes de reportar validação.

### CP02 — revisão do primeiro green durável

Recibo evidence/cp02-terminal-receipt.json: api green3 terminal, migration deploy/status/lint/build,234unit e343PG. Root leu serviço/schema/migration/nova suíte e conferiu SHA256 dos cinco logs reais, sem declarar all ou D09 completo. A revisão identificou FK draft→BuChannel Restrict incompatível com ChannelsService.desconectar, que remove o canal efêmero após preservar a identidade. Correção serial no schema/migration05 e regressão PG da desconexão/preservação/recriação requisitadas ao mesmo executor; nenhum arquivo Channel herdado será alterado. Reautorização da mesma conta e reconfirmação de generation atual permanecem requisito D04 do próximo checkpoint, sem rebinding do account imutável.

### CP03 — handoff serial condicionado ao terminal CP02

Sob a aprovação v1.1 existente, mesmo executor único gpt-6-luna/medium pode iniciar CP03 após api final verde/recibo CP02 e conferência30sealed. Routing GO: evidence/routing-cp03-v1.1.json. Paths ativos limitados a domínio message-templates, integrações message-templates, NOVOS integration/meta/message-template*.ts, ChannelCredentialResolver e spec novo, test/message-template*.e2e-spec.ts/helpers só se necessário à DI. Novo purpose template-management, contexto/conta scoped, provider bound e grant remoto lazy uma vez por operação; módulo importa ChannelTransportModule/owner único, DItoken abstrato. DTOs de catálogo/semântica e outcomes tipados mais contratos HTTP raw independentes; sem mudar MetaClient/Channel/OutboundService/send gate. Reauth mesma conta reconfirma contexto/fingerprint atuais sem rebinding; conta diferente CONTA_ALTERADA. Serviços de domínio não filtram provider concreto. CP03 não inclui BFF/tela/operações duráveis, outra migration, banco humano, provider verdadeiro, runtime ou Git produto. Logs reais e recibos cp03* pertencem ao executor; TODO/README/root* ao root. Parar ao fim para revisão da fronteira antes de operações duráveis.

### CP02 final aceito; CP03 iniciado

CP02-R1 resolvido: o RED reproduziu P2003; final green migração/status/lint/build/234unit/344PG com cleanup descartável. Teste reusa o mesmo externalResourceId/ProviderResourceIdentity sob outro BuChannel ID e impede herança do draft antigo. Root leu a correção e conferiu SHA256 dos3logs; evidence/cp02-channel-detach-receipt.json e root-cp02-disposition-v1.1.json. Schema mantém channelId histórico sem FK efêmera e BU Restrict preservando snapshots. CP03 plano informativo recebido e handoff condicional ativado; same-account generation/credential refresh e fingerprint atuais seguem D04, sem novo WHAT/renovação de aprovação. Não são prova de all ou implementação/entrega completa.

### Precisão de paths CP03 — composição DI

O handoff interno inicialCP03 omitira BffModule e dizia sem BFF. Executor informou composição TemplateManagementModule/TemplateDraftService ao concluir REDdebuild (import DI type-only; nenhuma prova comportamental reivindicada). Root admitiu expressamente também src/surfaces/bff/bff.module.ts neste checkpoint, somente import do módulo e registro do service, ambos já explicitamente ativos/aprovados v1.1/D09. Executor confirmou somente esses2pontos, sem controller/rota. É concretização de DI dentro do WHAT e paths previamente aprovados pelo usuário, não nova funcionalidade nem renovação de aprovação. Delta deve ser conferido contra evidence/inherited-shared-sources-v1.1.json e preserva composição06; HTTP/controller fica checkpoint posterior.

### CP03 terminal aceito; CP04 backend autorizado serialmente

Root conferiu os6logs preservados/17sources/30sealed/3HEADs e os deltas de credential resolver/BffModule contra a origem shared imutável. Canonical api terminal0:281unit/351PG; não é all nem entrega. evidence/cp03-terminal-receipt.json e root-cp03-disposition-v1.1.json distinguem falhas intermediárias, incluindo build sem log preservado, e limitações.

Mesmo executor único/routing-cp04-v1.1.json GO, mesma aprovação v1.1, perfil operational-coder/nestjs+prisma+postgresql+docker. CP04 pode concluir backend nos paths já aprovados: domínio/message-templates, integrações/message-templates e novos Meta/message-template*, schema e novas migrations *_message_template*, message-templates.controller.ts/BffModule, tests/message-template* e helpers; number-onboarding-pcv somente precisão PERF-R4-01/impacto dos índices. Sem Web, runner/CI, canais herdados, segredos, banco humano/runtime ou Git produto. Root conserva TODO/README/root*; executor cp04* e produto. Node audit genérico não pode percorrer API: readiness positivo publicado substitui inventário invasivo; nenhuma leitura/listagem/stat/hash/mount de .local-files.

GOAL CP04: operação/revisão/recibos duráveis e Local Commit Certainty, reserva/quota global por conta canônica, recuperação GET-only, lease/fence único catálogo↔individual, BFF sessão/CSRF e contratos negativos/concorrência PG reais. Incluir o guard privado depois do grant imediatamente antes do POST (rotação retida →0POST), runtime invalid view fail-closed, atuais permissões/conta/contexto e deduplicação. Sem quarto método público no provider, sem HTTP em transação, sem outbox/genérico, sem alterar Channel/send gate. Provas dos quatro limites de commit usam transação real e erro antes/depois do commit, readback independente bounded e contador HTTP; recibo externo ACCEPTED nunca vira recusa por erro local. Cada run usa log único persistido; não reescrever logs. Fazer RED comportamental significativo, implementação e api canônico verde; parar com recibo terminal honesto para revisão. PCV EPS/BCI/RLS backend conforme contrato; FRC/browser e all ficam após Web. D09 e entrega só com consumidores/gates completos.

### Admissão dos companions de histórico — 2026-10-21

O usuário respondeu **“Validar os dois arquivos de apoio”** à proposta `artifacts/reviews/leadshug-template-authoring-20261020/history-companion-path-admission-v1.1-proposal.md`, publicada em Foundation `da41a3fc`. São admitidos somente `src/domain/historico/catalogo.ts` e `src/domain/historico/cobertura.ts` além dos caminhos anteriores. As4 ações usam o RegistroDeAtividade existente na transação da mutação efetiva;3 consultas têm justificativa de isenção. Não isentar mutações para passar o teste, não alterar o guardião, não criar novo owner/schema/entidade, não copiar conteúdo ou segredos ao histórico. Escopo funcional, D01–09, matriz de prova, selos e limites externos permanecem os aprovados. Baseline pública dos2 arquivos e disposição em `evidence/history-companion-path-admission-v1.1.json`. O executor aplica após o terminal da execução API corrente, sem mutação com a fonte congelada.

### CP04 governança preliminar de diff público

Classificador canônico inalterado com adapter efêmero Git Windows/case do volume e pathspecs positivos antes de diff/untracked discovery:121/121paths esperados,0forbidden/0unclassified nesta fotografia anterior às mudançasCP04. evidence/root-cp04-public-diff-preflight-v1.1.json registra código/hash/commands/limite; nenhuma inspeção da árvore privada e nenhuma equivalência com auditoria global. Primeiro no-go de parsing corrigido removendo apenas o sufixo explicativo do heading Diff Expectation Contract, que o helper exige exato; contrato normativo não mudou. Reexecutar após estado final. Backlog atualizado factualmente de aguardando aprovação para implementação autorizada; não promove entrega.

### CP05 consumer handoff — conditional on CP04 terminal

Mesmo executor único gpt-6-luna/medium, principal single-writer, routing `evidence/routing-cp05-v1.1.json` GO. Perfil operational-coder com react/vite/nestjs/prisma/postgresql/docker; Genesis descartado por contrato existente. Root recarregou os métodos React UI boundary e Vite build/runtime; readiness positiva de manifests permanece em `evidence/positive-node-manifest-readiness-v1.1.json`, sem inventário recursivo privado. Handoff entra em vigor somente após terminal da execução API corrente e recibo honesto do checkpoint; eventuais lacunas remanescentes ficam explicitamente abertas para o all, sem declarar aceite completo.

Paths CP05: somente Web Modelos*/Modelo*/messageTemplates*, api.ts/api.spec.ts/App.tsx/e2e/message-templates* e companions de freshness admitidos; API browser-server/timeline-fixtures para fake exclusivamente externo e testes message-template* já aprovados. Correções residuais do owner de modelos continuam nos paths CP04, serialmente pelo mesmo executor. Sem editar runner/CI/config/Channel/send gate/30sealed, sem dependência nova, private/env, banco preservado, runtime ou Git produto nesta etapa.

GOAL: jornada real BFF/PG Cadastros→Modelos para ATENDENTE+, rascunho versionado/prévia autoritativa/salvar/reabrir/submeter uma vez/catálogo/status/reconciliar; fences monotônicos contexto+edição+request inclusive A→B→A/texto idêntico e criação enquanto edição prossegue. Preview300ms; status aceito separado de aprovado, correlação não afirma autoria; erros preservam operação/certeza segura, sem expor segredo nem habilitar envio ao destinatário. Testes Playwright usam BFF real e PostgreSQL, fake somente Meta, nenhuma rota de produto para teste. Incluir RLS concorrente scoped+foreign404 e erro/liberação de observação antigos após novo owner caso não exista prova explícita. Uma execução canônica `bash scripts/test-channels-local.sh all` valida o pacote consolidado, fonte congelada durante a execução e logs únicos retidos. Revisões independentes completas e ativação/prova assistida continuam gates posteriores, não são dispensadas por este handoff.
