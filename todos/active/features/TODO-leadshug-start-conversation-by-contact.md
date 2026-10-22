# Tactical TODO — ST-CON-04

## Title

LeadsHug — ST-CON-04: abrir conversa por contato e conduzir o primeiro envio com segurança

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** InProgress
- **Version:** 1.1
- **Created:** 2026-10-19; materially rebased 2026-10-22
- **Template provenance:** copied from `delphi-ai/templates/todo_template.md` before refinement.
- **Authority:** APROVADO explicitly received from the user on2026-10-22 for reviewed ST-CON-04 v1.1 at Foundation fbbdfa6f; execution requires current normal authority GO, binding rules and strict approved boundaries.

## Context

ST-CON-06 entregou o transporte abstrato textual, adapters Meta/Evolution, resolução scoped e um `OutboundService` compartilhado; ST-CON-05 entregou autoria/submissão e o catálogo/projetor compartilhado de templates. Ambos permanecem contratos entregues e evidência de dependência, não aprovação desta história. A inbox ainda não permite iniciar atendimento manual por contato e conduzir o primeiro envio oficial de modo recuperável.

Este v1.1 substitui a autoridade ativa da minuta revisada em 2026-10-19. O original e suas decisões/reviews são preservados pelo owner do pacote como `historical-planning-20261019-20261020.md`; nada daquele ciclo é evidência de revisão, guard, aprovação ou execução deste texto. Os handoffs de ST-CON-06 e ST-CON-05 continuam como contexto factual.

**Perfil desta etapa:** Strategic / CTO-Tech-Lead; escopo ativo NestJS, React, Vite, PostgreSQL, Prisma e Docker. Genesis foi rejeitado: o projeto canônico já existe. Próximo handoff planejado: Operational / Coder após contrato congelado, reviews/guards atuais e aprovação humana explícita. Supporting profiles: Assurance / Tester-Quality, Assurance / Security-Adversarial e Operational / DevOps para os respectivos gates. Seleção declarada conforme `delphi-ai/workflows/docker/profile-selection-method.md`.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md`
- **Primary story ID:** ST-CON-04
- **Why this is the right current slice:** sequência humana confirmada: cadastro → preparar/submeter template em ST-CON-05 → abrir/reusar conversa e conduzir primeiro contato → importação/histórico em fatia futura. Um fluxo inicial assistido, sem CRM, campanha ou operação em lote.
- **Direct-to-TODO rationale:** n/a; brief existente.

## Contract Boundary

- Este TODO define **WHAT** será entregue; `Assumptions Preview` e `Execution Plan` registram a proposta **HOW** para revisão.
- O escopo é fechado ao início manual e primeiro envio de uma conversa. Qualquer alteração material de Scope, DoD, validação, contrato público ou decisões requer retorno à revisão e nova aprovação antes de execução.
- “Aceito” significa ID externo válido persistido; não significa entrega ao aparelho nem leitura.
- Baseline inicial publicado antes dos primeiros guards/review; parecer arquitetural r1 integrado abaixo. Mudanças materiais decorrentes do parecer serão publicadas em novo freeze antes da crítica. Nenhuma implementação ou aprovação humana é reivindicada.

## Implementation Intent

- **Current delivery:** propor abertura/reuso BU+contato e um primeiro envio de texto livre quando a política permite ou de template textual Meta aprovado quando necessária a janela oficial, com intenção durável e recuperação sem reenvio cego.
- **Planned next steps:** congelar esta revisão; executar fresh architecture opinion, crítica independente e guards de planejamento; resolver findings; somente então submeter o contrato para APROVADO humano.
- **Anticipatory implementation authorized now:** none.
- **Rationale:** reaproveitar os owners existentes de conversa, transporte, aceitação de Message e catálogo. O fluxo novo coordenará uma intenção durável; não duplicará sender, aceitação ou catálogo.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** concluir a admissão/transição de tentativa do backend com candidato congelado e prova PostgreSQL, pelo único writer, preservando as duas fixtures protegidas até validação humana.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `implementation`
- **Why this state now:** APROVADO humano recebido para v1.1; regras binding recarregadas e69 fontes/3HEADs conferidos. Reviews e guards de planejamento preservados; normal authority GO é gate anterior à primeira edição de produto.
- **Exit condition:** implementação e todas as evidências/reviews/gates de entrega aprovados; estágio continua Pending até os critérios locais reais, sem claim de entrega por aprovação.

## Scope

- [ ] **SCOPE-01 — Abrir/reusar conversa:** sessão BFF com CSRF e papel ATENDENTE+; criar/reusar atomicamente a conversa única por BU+contato, com telefone obrigatório normalizado a 8–15 dígitos sem inferir país/DDI. Sem CRM. Abrir não envia, não reivindica atendimento, não reabre/fecha, não marca leitura e não altera timeline existente. Conversa nova começa `QUEUED`, `unreadCount=0`, `lastMessageAt=null`; listagem ordena por `COALESCE(lastMessageAt, createdAt)` sem data fictícia. Abrir nunca dispara automação. Preservar NOVA_CONVERSA baseado em criação persistida: primeiro IN posterior a uma abertura manual vazia não o dispara; PALAVRA_CHAVE mantém sua regra atual.
- [ ] **SCOPE-02 — Primeiro envio durável:** endpoints autenticados BFF para opções, preview, criação de intenção, leitura/reconciliação/acknowledgment; UUID idempotency por BU+ator; slot ativo por conversa; request/context/fingerprint imutáveis. Fallback automático entre canais é proibido.
- [ ] **SCOPE-03 — Política de texto e janela:** manter readiness e `requiresWindow`; introduzir `Message.officialInboundAt` nullable somente de IN Meta assinada e verificada com timestamp inteiro positivo, não futuro e identidade/resource gerenciados. Janela por maior valor confiável na conversa e recurso atualmente selecionado, com limite estrito `<24h`; não inferir de `createdAt`, payload bruto, importação ou fonte não oficial. Dados ausentes/malformados/futuros permanecem null sem descartar a mensagem. Timeline/cursor seguem `createdAt`.
- [ ] **SCOPE-04 — Primeiro envio por canal abstrato:** proposta sob revisão: estender a única abstração `Channel.sendMessage` a um union discriminado `text | approved-template`, acompanhado de `readonly supportedKinds`; Meta declara ambos; Evolution declara text e responde `BLOCKED/UNSUPPORTED_KIND` antes de qualquer HTTP para template. Adapter Meta formata destinatário como `+` seguido do DDI completo; identidade/storage do domínio continua dígitos canônicos. Cobrir destinatários do mesmo país e de outro país e preservar a semântica de envio de texto existente, verificando explicitamente sua formatação wire compartilhada. Resolver seleciona canal explicitamente com contexto immutable e versão atual da credencial. Não criar `sendTemplate`, branches por provider em domínio/consumers, casts/`instanceof`, plataforma genérica de plugins ou integrações futuras.
- [ ] **SCOPE-05 — Catálogo e composição:** reutilizar exatamente `GET/POST /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` e seu domínio, projector, lease/fence, TTL de 300s e parser de enum entregues por ST-CON-05. Remover da proposta anterior o duplicado `GET /conversations/:id/channels/:channelId/templates`. TemplateManagement permanece capability estreita sem método de envio a destinatário. Preview POST é local/read-only, sessão+CSRF, sem DB write/provider call; retorna texto escapado e fingerprint determinístico ligado a conversa/contato/contexto atual.
- [ ] **SCOPE-06 — Subconjunto de template:** BODY textual NAMED/POSITIONAL, header/footer somente estáticos; sem botão, mídia, auth, flows, arbitrary Graph payload ou ampliação de categorias suportadas. Texto final 1–4096 chars; até 20 parâmetros de 1–1024 chars; snapshot total até 4096. Catálogo é observação, nunca autorização de envio: antes de cada novo envio validar remotamente asset/status atual da mesma conta; detectar mudança/pausa/unknown e falhar fechado. `getTemplate(id)` isolado não prova vínculo de conta; usar listagem existente por nome salvo na observação confiável, filtrada em até 2 páginas de 50, com correspondência exata ID/nome/idioma/semântica e resultado esgotado. Cursor/URL do browser nunca autoriza fetch.
- [ ] **SCOPE-07 — Saga local e owner:** coordenador de intenção vive no domínio inbox e chama o `OutboundService` comum; reutilizar seu dispatch abstrato e `MessageAcceptanceService` como único owner de Message. Se necessário, permitir que esse mesmo owner aceite via transação scoped, preservando wrapper existente; hoje `OutboundService.finalize` separado e `MessageAcceptanceService.accept` transacional não devem ser descritos como já integrados. Efeitos de status/owner do novo fluxo só por CAS contra `updatedAt/state` capturados antes do HTTP e owner ativo; preservar claim/close concorrentes, sem roubo.
- [ ] **SCOPE-08 — Estados e recuperação:** UUID keyed por BU+actor; replay do request canônico acontece antes de leituras de provider, respeitando grant atual. Slot único ativo separado do outcome. `PREPARED` lease 90s; `SENDING` só após todos os reads remotos de elegibilidade/grant/phone preflight e claim CAS persistido pelo abstract dispatch-fence hook imediatamente antes do POST; no máximo um POST externo por tentativa e nenhuma repetição automática. Falha/expiração comprovadamente pré-dispatch → `REJECTED`, slot liberado por CAS. SENDING abandonado/timeout/resultado desconhecido/ID faltante → `AMBIGUOUS`, slot bloqueado. ID conhecido → `EXTERNAL_ACCEPTED` persistido separado da Message local; recuperação apenas local. Não fazer provider GET/POST, fuzzy echo matching ou criar Message sem externalID. `EXTERNAL_ACCEPTED_LOCAL_BLOCKED` conserva o fato e ID, sem falsificar sucesso. Acknowledgment apenas após classificação de incerteza/bloqueio e DBnow >= dispatchDeadlineAt imutável (mesmo deadline da lease90s original, nunca renovado), inclusive para EXTERNAL_ACCEPTED_LOCAL_BLOCKED, com risco explícito de duplicata e liberação irreversível; resultado tardio não readquire slot nem altera owner/status corrente.
- [ ] **SCOPE-09 — Compatibilidade de callers:** composer BFF existente deve bloquear, antes de qualquer HTTP, conversa nova/vazia ou qualquer slot inicial não resolvido. BFF público e BOT também consultam/respeitam slot ativo antes de dispatch para evitar duplicação; manter suas atuais formas de aceitação/erro e não lhes atribuir idempotência global. Interlock finito definido no aditivo normativo r1 abaixo: tokens ordinários por owner, compatíveis entre si, excluem reserva inicial até settlement ou acknowledgment explícito de incerteza. Expiração de SENDING nunca libera por relógio. Preservar semântica diagnóstica de ACK nulo de ST-CON-06 para callers antigos; regra de Message sem externalID aplica-se ao novo coordenador.
- [ ] **SCOPE-10 — Bounded I/O, prova e limites:** readiness permanece RECEIPT/identidade própria/epoch/estado CONECTADO/`activeCredentialVersion`; management purpose não desvia a prova de envio. Reutilizar reads estreitos ST-05 e client de protocolo de template-send dentro do adapter Meta; nenhum HTTP Meta no inbox. Até 6 GETs no novo template dispatch: 1 grant management + 2 páginas filtered templates + 1 messaging grant + 2 membership pages; no máximo 1 POST. Timeout por request 10s, orçamento total 75s dentro de lease 90s. Reutilizar grant por request-bound adapter sem probe oculto/double count. Limites de nova intenção: 10/min por ator e 60/h por namespace canônico de conta/recurso, inclusive links locais entre BUs/tenants da mesma conta, sem expor dados estrangeiros. Leituras de catálogo preservam limites/dívidas privadas de ST-05; recovery tem zero rede.
- [ ] **SCOPE-11 — Prova assistida futura:** depois de candidate GREEN, assurance de imagens e migration descartável/local, validar primeiro envio assistido não oficial, template oficial realmente `APPROVED` próprio e reply do destinatário. A ausência de asset elegível bloqueia conclusão; fixture não prova aprovação. Nenhum contato automático.
- [ ] **SCOPE-12 — Harness e consumidores:** dependency/fake substitutability, testes negativos Evolution zero HTTP, regressões de texto BFF/public/BOT, janela/projeções batched, timeline/cursor e performance. Preservar SEC-R6-04, OPS-R4-01 e TQA-ST05-03 como limitações entregues; não implementar backlog dessas histórias aqui.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; não há entrega reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

n/a; planning draft em revisão, não marcado blocked.

## Execution Lane Tracking (Required)

- **Local implementation branches:** root/api/web all feature/number-onboarding, observed immediately after approval; principal checkout only. Foundation main. No product Git writes or topology changes authorized.
- **Promotion lane path:** local → lanes definidas pelos TODOs/repos após approval; não assumidas neste planejamento.
- **Lane-promoted threshold:** pending contract/review.
- **Production-ready threshold:** fora da autorização atual.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

n/a nesta etapa; nenhum código, promoção ou implantação autorizado.

## Out of Scope

- CRM, lead/funnel, campanhas, broadcast, importação de histórico, sender automático ou criação automática de contato/conversa.
- Gestão/autoria/submissão/status de templates, novo projector/cache/catalog DTO, refresh oculto/polling, nova rota de catálogo ou nova capability provider genérica.
- Novos providers, envio outbound em lote, retry automático, exactly-once externo, outbox/event platform, fuzzy matching ou qualquer envio no browser.
- Modificar credenciais/routing Meta, nova modalidade de cadastro, consultar conta real nesta fase, Railway/promoção/deploy. Código/runtime/testes só após APROVADO deste contrato; ativação local futura limitada à evidência abaixo.
- Corrigir SEC-R6-04, OPS-R4-01, TQA-ST05-03 ou demais backlog ST-05/ST-06 sem decisão própria.
- Ler/listar/stat/hash/traversar/montar `api-app/.local-files/`, `.env` ou `.env.testing`; ler argumentos/process env/logs/linhas de negócio.
- Código fora da lista aprovada, worktrees/cópias auxiliares, gitlinks/.gitmodules, alterações Delphi, commit/push de produto. Foundation main pode publicar apenas TODO e pacote de planejamento/revisão pelos guardas documentais próprios.

## Diff Expectation Contract (Required Before Delivery)

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
| foundation | foundation_documentation | 197e7a0713c132c6213e218748655bcda5a19c72 | working_tree |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | prisma/migrations/20261021130000_message_template_drafts/migration.sql | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | prisma/migrations/20261021150000_message_template_operations/migration.sql | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | prisma/schema.prisma | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/channels/channel-credential-resolver.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/channels/channel-credential-resolver.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/historico/catalogo.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/historico/cobertura.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/message-templates/template-definition.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-definition.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-draft.service.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-management.dependencies.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-management.ports.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-management.ports.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-observation.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/message-templates/template-submission.service.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-transaction-boundary.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/message-templates/template-management.module.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/message-templates/template-management.resolver.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/meta/message-template.client.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/meta/message-template.client.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/bff/bff.module.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/surfaces/bff/message-templates.controller.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/browser-server.cjs | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | test/helpers.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | test/message-template-bff.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/message-template-drafts.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/message-template-management.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/number-onboarding-bci.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/number-onboarding-pcv.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/timeline-fixtures.cjs | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | e2e/message-templates.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| web | e2e/number-onboarding-freshness.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | e2e/timeline-freshness.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/App.tsx | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| web | src/api.spec.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/api.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/telas/Modelos.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| web | src/telas/Modelos.tsx | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| root | .github/workflows/ci.yml | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| root | scripts/test-channels-local.sh | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| root | scripts/check-channels-ci-parity.py | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/inbox/conversations.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/incoming.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/incoming.typebot.integration.spec.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: qualified window, shared admission and manual-open first-inbound automation regression only; initial hash mandatory before FIRST change |
| api | src/integrations/evolution/evolution.client.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/evolution/evolution.client.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/meta/meta.client.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/meta/meta.client.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/bff/conversations.controller.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: BFF manual open/options/preview/intent/admission-recovery endpoints and scoped ACL; initial hash mandatory before FIRST change |
| api | src/surfaces/public/conversations.controller.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/public/public.module.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/webhooks/webhooks.module.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/api-publica.e2e-spec.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: ordinary public text/window/admission mappings; initial hash mandatory before FIRST change |
| api | test/number-onboarding-typebot.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | prisma/migrations/20261020170000_message_inbound_window_index/migration.sql | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/channels/transport/channel-dependencies.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/channels/transport/channel.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/outbound.service.spec.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/outbound.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/channel-adapter-factory.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/channel-adapter-registry.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/channel-transport.module.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/evolution-channel.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/meta-channel.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/prisma-channel-resolver.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | test/channel-transport.e2e-spec.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/telas/Inbox.tsx | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | e2e/channel-transport.spec.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: inherited ordinary text/window browser regressions; initial hash mandatory before FIRST change |
| api | src/domain/inbox/initial-message* | any | intent/selection/renderer/state, exact scoped services and specs; no second Message or catalog owner |
| api | src/domain/inbox/conversation-start* | any | open/reuse and tests |
| api | src/domain/inbox/channel-window-policy* | any | one trusted-window query and its tests |
| api | src/domain/inbox/message-acceptance.service.spec.ts | any | same owner transaction and sender/echo contract |
| api | src/domain/inbox/conversations.service.spec.ts | any | list/open/empty/read effects |
| api | src/domain/channels/transport/channel*.spec.ts | any | union/fence/substitution architecture harness |
| api | src/integrations/channels/account-reference.ts | A, ?? | extract exact existing opaque hash helper |
| api | src/integrations/meta/initial-message.client*.ts | any | provider-private protocol preflight/text/template for new attempts inside same Meta Channel; old client interface preserved |
| api | src/surfaces/webhooks/meta.controller.ts | M | signed timestamp extraction only |
| api | prisma/migrations/*_initial_message*/migration.sql | A, ?? | additive intent/timestamp/index migration; no unrelated migration edit |
| api | test/initial-message* | any | real PG/BFF/PCV/scoped account and durability fault contracts |
| api | test/conversation-start* | any | open races and list SQL |
| api | test/atendimento.e2e-spec.ts | M | common BFF sender/window compatibility |
| api | test/webhooks.e2e-spec.ts | M | timestamp signature and origin/resource proof |
| web | src/componentes/NovaConversa* | any | local form/confirmation and tests |
| web | src/telas/Inbox.spec.ts* | any | composer/freshness/recovery regression |
| web | e2e/start-conversation.spec.ts | A, ?? | new real-BFF browser mutation flow |
| foundation | todos/active/features/TODO-leadshug-start-conversation-by-contact.md | M, D, R | contract and approved lifecycle closeout |
| foundation | todos/completed/features/TODO-leadshug-start-conversation-by-contact.md | A, ??, R | only after delivery gates |
| foundation | artifacts/reviews/leadshug-start-conversation-20261022/** | any | planning/review/implementation evidence |
| foundation | modules/inbox-and-conversations.md | M | stable contracts after approval/delivery |
| foundation | modules/integrations-and-channels.md | M | approved payload/window supersede after delivery |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | factual story sequence |
| foundation | backlog/README.md | M | current gate only |
| foundation | artifacts/dependency-readiness.md | M | redacted runtime readiness only |
| api | src/domain/inbox/message-acceptance.service.ts | M | Same acceptance owner tx-capable primitive and original-CAS ordering; existing bytes sealed in supplemental-source-seal-v1.1.json before first mutation |
| api | src/domain/inbox/dispatch-admission*.ts | A, ?? | Finite ordinary admission/exclusive-initial interlock and unit cases, no global operation platform |
| api | test/dispatch-admission*.e2e-spec.ts | A, ?? | Real PG interlock/expiry/owner-CAS/commit certainty barriers |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .local-files/** | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| api | .env* | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | .env* | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | .gitmodules | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | api-app | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | web-app | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | delphi-ai | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| web | dist/** | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |

### Initial inheritance admission
Closed68-file inventory: evidence/inherited-source-seal-v1.1.json. Before first implementation/test compare ALL68 hashes and3 product HEADs. Thereafter only specifically admitted paths may change for04; every remaining inherited record stays byte-exact. No broad discovery of private files. Root and source repositories remain principal single-checkout. Planned companion extraction shares the exact opaque account-reference algorithm without changing existing ST05 keys. Historical source files/receipts are never reclassified as new04 work.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** local details of open/reuse, bounded preview, initial attempt lifecycle, current account eligibility, and tests needed to prove this same first-contact flow.
- **Must update or split the TODO:** CRM/import, authoring/catalog changes, new transport/provider, automated sending, campaign or any global sender/idempotency redesign.

## Definition of Done

- [ ] **DOD-01:** opening invokes no automation; manual-open-without-send then first inbound leaves NOVA_CONVERSA false while keyword automation retains its predicate; authorized operator opens/reuses BU/contact atomically; no side effects listed in SCOPE-01 occur; new conversation has truthful empty state and deterministic list ordering.
- [ ] **DOD-02:** stale/foreign BU, actor, slot, selected channel, grant, credential epoch/version, conversation generation, template fingerprint, or policy context fails closed before external dispatch.
- [ ] **DOD-03:** Preview is escaped, deterministic, local/read-only and context-bound; supported textual subset and exact limits are enforced server-side.
- [ ] **DOD-04:** existing Channel consumers remain substitutable; Meta supports declared text/template kinds; Evolution template is typed unsupported with zero HTTP; no second send method/provider branching outside adapters or DI cycle; immutable descriptor plus same-operation fence preserves common dispatch.
- [ ] **DOD-05:** prove commit certainty at reservation/dispatch-claim/receipt/release, including real commit with lost ACK and real rollback; every remote eligibility/grant/phone GET completes before durable SENDING claim; the abstract fence CAS-claims immediately before one POST, and expiry of PREPARED during delayed preflight produces zero POST. Each initial attempt dispatches at most one POST; failures are classified truthfully; known provider ID is durably separate from local Message; recovery never contacts provider and never creates a Message without external ID.
- [ ] **DOD-06:** initial transaction locks identity then conversation, checks original pre-HTTP status/owner CAS before acceptance mutates updatedAt, permits eligible acceptance when status CAS fails, and recovers unique conflict by whole-local-transaction rollback/readback/re-entry at most once; MessageAcceptance remains sole Message owner and existing sender/error behavior is preserved; CAS prevents late initial outcome from changing concurrent claim/close/owner or reacquiring released slot. Initial acknowledgment in either allowed state waits for immutable dispatchDeadlineAt; before it409 ACK_TOO_EARLY and zero release.
- [ ] **DOD-07:** official window uses only qualified trusted Meta IN timestamp for selected resource; all current BFF/public/BOT availability and send policy consumers use the same rule; timeline/cursors and performance bounds hold.
- [ ] **DOD-08:** owner-scoped ordinary admissions and exclusive initial reservation serialize under the same conversation lock without serializing ordinary-versus-ordinary sends; uncertain dispatched tokens block initial reservation until settlement or explicit risk acknowledgment, never time takeover; late owner release cannot touch successor; existing composer is blocked before HTTP for new/empty/unresolved slot; public/BOT respect slot and retain existing mappings; text regressions pass.
- [ ] **DOD-09:** NAMED and POSITIONAL initial support is derived by the initial text renderer from the unchanged catalog components/format, independently of inherited authoring flags; exact full context binds management descriptor to selected transport and final text-window fence; current eligibility is checked before every new official template dispatch via bounded same-account reads; template is actually APPROVED; Meta request pins server-captured `messaging_account_id`, uses `+` plus full DDI, and preserves existing ordinary text semantics. Tests cover same-country and cross-country recipients. Official raw reference receipt confirms account pin and recipient formatting; actual own-account readiness remains unverified.
- [ ] **DOD-10:** per actor/account limits, tenant isolation, request/deadline budgets and zero-network recovery are demonstrated with real bounded counters/barriers.
- [ ] **DOD-11:** additive migration passes explicit preflight and disposable local validation without reset/drop; current source/image/API freshness and approved local validation topology are proven.
- [ ] **DOD-12:** assisted proof: operator sends first unofficial message, an actually APPROVED official template, receives a reply; no auto-contact; if eligible approved asset is unavailable, completion remains blocked.
- [ ] **DOD-13:** architecture/adherence/security/performance/TQA/final/cutover/debt and delivery guards pass at their required stages; no open P1/P2; constraints SEC-R6-04, OPS-R4-01, TQA-ST05-03 remain truthfully carried.

## Scope Planning Matrix

| Scope ID | Contract outcome | Owner/boundary | Planned evidence after approval | Planning status |
| --- | --- | --- | --- | --- |
| SCOPE-01 | sessão BFF com CSRF e papel ATENDENTE+; criar/reusar atomicamente a conversa única por BU+contato, com telefone obrigatório normalizado a 8–15 dígitos sem inferir país/DDI | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-02 | endpoints autenticados BFF para opções, preview, criação de intenção, leitura/reconciliação/acknowledgment; UUID idempotency por BU+ator; slot ativo por conversa; request/context/fingerprint imutáveis | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-03 | manter readiness e `requiresWindow`; introduzir `Message.officialInboundAt` nullable somente de IN Meta assinada e verificada com timestamp inteiro positivo, não futuro e identidade/resource gerenciados | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-04 | proposta sob revisão: estender a única abstração `Channel.sendMessage` a um union discriminado `text | approved-template`, acompanhado de `readonly supportedKinds`; Meta declara ambos; Evolution declara text e responde `BLOCKED/UNSUPPORTED_KIND` antes de qualquer HTTP para template | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-05 | reutilizar exatamente `GET/POST /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` e seu domínio, projector, lease/fence, TTL de 300s e parser de enum entregues por ST-CON-05 | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-06 | BODY textual NAMED/POSITIONAL, header/footer somente estáticos; sem botão, mídia, auth, flows, arbitrary Graph payload ou ampliação de categorias suportadas | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-07 | coordenador de intenção vive no domínio inbox e chama o `OutboundService` comum; reutilizar seu dispatch abstrato e `MessageAcceptanceService` como único owner de Message | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-08 | UUID keyed por BU+actor; replay do request canônico acontece antes de leituras de provider, respeitando grant atual | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-09 | composer BFF existente deve bloquear, antes de qualquer HTTP, conversa nova/vazia ou qualquer slot inicial não resolvido | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-10 | readiness permanece RECEIPT/identidade própria/epoch/estado CONECTADO/`activeCredentialVersion`; management purpose não desvia a prova de envio | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-11 | depois de candidate GREEN, assurance de imagens e migration descartável/local, validar primeiro envio assistido não oficial, template oficial realmente `APPROVED` próprio e reply do destinatário | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-12 | dependency/fake substitutability, testes negativos Evolution zero HTTP, regressões de texto BFF/public/BOT, janela/projeções batched, timeline/cursor e performance | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |

## Validation Steps

- [ ] **VAL-01:** include real PG integration open-without-send→first inbound with isolated NOVA_CONVERSA trigger (no bot start), separate PALAVRA_CHAVE fixture (retained), and no automation on open; after approval only, run contract/unit/dependency harness and exact existing BFF/public/BOT textual regressions; no test execution is part of this planning draft.
- [ ] **VAL-02:** initial acknowledgment before deadline rejects without release; at/after deadline permits only classified states, successor admission and late original result stay fenced; PostgreSQL race/barrier and fault injection for unique BU/contact creation, idempotent replay, delayed remote preflight vs PREPARED expiry with zero POST, claim immediately before POST, claim/close during HTTP, timeout/late provider result, ack/release then successor; assert provider counters and no lock-held HTTP; both ordinary/initial admission orderings, ordinary concurrency preserved, suspension before/after claim, uncertain token never expires into takeover, owner-CAS late release; real rollback/commit-ACK-loss at all four local boundaries; pre-acceptance CAS and echo-first conflicts.
- [ ] **VAL-03:** adapter substitution and raw protocol tests; Evolution template unsupported produces zero requests; Meta pages/status/account membership limits and same-account exact tuple are bounded; NAMED and POSITIONAL end-to-end order; closed-window template allowed, text-window expiry during preflight blocked, every descriptor/context dimension mismatch blocked before POST.
- [ ] **VAL-04:** signed webhook cases for valid, absent, malformed, future, nonofficial, duplicate and old timestamps; assert nullable provenance and unchanged timeline/cursors.
- [ ] **VAL-05:** same trusted-window policy across BFF/public/BOT availability and dispatch; EXPLAIN/query count for large OUT-heavy and no-IN histories; enforce batched consumer bounds.
- [ ] **VAL-06:** Playwright on freshly served React/Vite bundle + real BFF/PostgreSQL: open/reuse, preview, stale context, create/replay/read/reconcile/ack, safe errors, refresh, composer block, preserve draft, keyboard flow.
- [ ] **VAL-07:** migrations: explicit additive preflight, lock timeout 5s, statement timeout 60s, disposable TEST target, migration deploy/status and rollback assessment; never reset/drop or run before separate authorized implementation stage.
- [ ] **VAL-08:** local source-bound API/Web activation and owned stable/temporary HTTPS only under later approved runtime plan; assisted own-channel proofs as DOD-12.
- [ ] **VAL-09:** run appropriate architecture, critique, assumption/code, review drift, decision adherence, module consistency, security, performance/concurrency, TQA, final, cutover and completion guards after their proper lifecycle stages. Architecture planning r1 exists; other planning/delivery gates require their actual current artifacts. No implementation validation is claimed.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | opening invokes no automation; manual-open-without-send then first inbound leaves NOVA_CONVERSA false while keyword automation retains its predicate; authorized operator opens/reuses BU/contact atomically; no side effects listed in SCOPE-01 occur; new conversation has truthful empty state and deterministic list ordering. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-02 | Definition of Done | stale/foreign BU, actor, slot, selected channel, grant, credential epoch/version, conversation generation, template fingerprint, or policy context fails closed before external dispatch. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-03 | Definition of Done | Preview is escaped, deterministic, local/read-only and context-bound; supported textual subset and exact limits are enforced server-side. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-04 | Definition of Done | existing Channel consumers remain substitutable; Meta supports declared text/template kinds; Evolution template is typed unsupported with zero HTTP; no second send method/provider branching outside adapters or DI cycle; immutable descriptor plus same-operation fence preserves common dispatch. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-05 | Definition of Done | prove commit certainty at reservation/dispatch-claim/receipt/release, including real commit with lost ACK and real rollback; every remote eligibility/grant/phone GET completes before durable SENDING claim; the abstract fence CAS-claims immediately before one POST, and expiry of PREPARED during delayed preflight produces zero POST. Each initial attempt dispatches at most one POST; failures are classified truthfully; known provider ID is durably separate from local Message; recovery never contacts provider and never creates a Message without external ID. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-06 | Definition of Done | initial transaction locks identity then conversation, checks original pre-HTTP status/owner CAS before acceptance mutates updatedAt, permits eligible acceptance when status CAS fails, and recovers unique conflict by whole-local-transaction rollback/readback/re-entry at most once; MessageAcceptance remains sole Message owner and existing sender/error behavior is preserved; CAS prevents late initial outcome from changing concurrent claim/close/owner or reacquiring released slot. Initial acknowledgment in either allowed state waits for immutable dispatchDeadlineAt; before it409 ACK_TOO_EARLY and zero release. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-07 | Definition of Done | official window uses only qualified trusted Meta IN timestamp for selected resource; all current BFF/public/BOT availability and send policy consumers use the same rule; timeline/cursors and performance bounds hold. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-08 | Definition of Done | owner-scoped ordinary admissions and exclusive initial reservation serialize under the same conversation lock without serializing ordinary-versus-ordinary sends; uncertain dispatched tokens block initial reservation until settlement or explicit risk acknowledgment, never time takeover; late owner release cannot touch successor; existing composer is blocked before HTTP for new/empty/unresolved slot; public/BOT respect slot and retain existing mappings; text regressions pass. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-09 | Definition of Done | NAMED and POSITIONAL initial support is derived by the initial text renderer from the unchanged catalog components/format, independently of inherited authoring flags; exact full context binds management descriptor to selected transport and final text-window fence; current eligibility is checked before every new official template dispatch via bounded same-account reads; template is actually APPROVED; Meta request pins server-captured `messaging_account_id`, uses `+` plus full DDI, and preserves existing ordinary text semantics. Tests cover same-country and cross-country recipients. Official raw reference receipt confirms account pin and recipient formatting; actual own-account readiness remains unverified. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-10 | Definition of Done | per actor/account limits, tenant isolation, request/deadline budgets and zero-network recovery are demonstrated with real bounded counters/barriers. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-11 | Definition of Done | additive migration passes explicit preflight and disposable local validation without reset/drop; current source/image/API freshness and approved local validation topology are proven. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-12 | Definition of Done | assisted proof: operator sends first unofficial message, an actually APPROVED official template, receives a reply; no auto-contact; if eligible approved asset is unavailable, completion remains blocked. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-13 | Definition of Done | architecture/adherence/security/performance/TQA/final/cutover/debt and delivery guards pass at their required stages; no open P1/P2; constraints SEC-R6-04, OPS-R4-01, TQA-ST05-03 remain truthfully carried. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| VAL-01 | Validation Steps | include real PG integration open-without-send→first inbound with isolated NOVA_CONVERSA trigger (no bot start), separate PALAVRA_CHAVE fixture (retained), and no automation on open; after approval only, run contract/unit/dependency harness and exact existing BFF/public/BOT textual regressions; no test execution is part of this planning draft. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-02 | Validation Steps | initial acknowledgment before deadline rejects without release; at/after deadline permits only classified states, successor admission and late original result stay fenced; PostgreSQL race/barrier and fault injection for unique BU/contact creation, idempotent replay, delayed remote preflight vs PREPARED expiry with zero POST, claim immediately before POST, claim/close during HTTP, timeout/late provider result, ack/release then successor; assert provider counters and no lock-held HTTP; both ordinary/initial admission orderings, ordinary concurrency preserved, suspension before/after claim, uncertain token never expires into takeover, owner-CAS late release; real rollback/commit-ACK-loss at all four local boundaries; pre-acceptance CAS and echo-first conflicts. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-03 | Validation Steps | adapter substitution and raw protocol tests; Evolution template unsupported produces zero requests; Meta pages/status/account membership limits and same-account exact tuple are bounded; NAMED and POSITIONAL end-to-end order; closed-window template allowed, text-window expiry during preflight blocked, every descriptor/context dimension mismatch blocked before POST. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-04 | Validation Steps | signed webhook cases for valid, absent, malformed, future, nonofficial, duplicate and old timestamps; assert nullable provenance and unchanged timeline/cursors. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-05 | Validation Steps | same trusted-window policy across BFF/public/BOT availability and dispatch; EXPLAIN/query count for large OUT-heavy and no-IN histories; enforce batched consumer bounds. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-06 | Validation Steps | Playwright on freshly served React/Vite bundle + real BFF/PostgreSQL: open/reuse, preview, stale context, create/replay/read/reconcile/ack, safe errors, refresh, composer block, preserve draft, keyboard flow. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-07 | Validation Steps | migrations: explicit additive preflight, lock timeout 5s, statement timeout 60s, disposable TEST target, migration deploy/status and rollback assessment; never reset/drop or run before separate authorized implementation stage. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-08 | Validation Steps | local source-bound API/Web activation and owned stable/temporary HTTPS only under later approved runtime plan; assisted own-channel proofs as DOD-12. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-09 | Validation Steps | run appropriate architecture, critique, assumption/code, review drift, decision adherence, module consistency, security, performance/concurrency, TQA, final, cutover and completion guards after their proper lifecycle stages. Architecture planning r1 exists; other planning/delivery gates require their actual current artifacts. No implementation validation is claimed. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |

## External Reference Evidence

Official primary references consulted 2026-10-22: [WhatsApp Send Messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages/), [Messaging account model](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/messaging/), and [Template fundamentals](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview/). Raw response provenance, hashes, lengths and paraphrased facts are in root-owned `artifacts/reviews/leadshug-start-conversation-20261022/evidence/meta-primary-reference-receipt-v1.1.json`. These docs establish protocol facts, not own-account readiness or actual asset approval.

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status (`unknown|healthy|degraded|failing|rate-limited|stale`) | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Meta official raw contract/docs | confirm exact send wire fields and recipient formatting | `healthy` | 2026-10-22 | anonymous official HTTP `Accept: text/markdown`; provenance receipt above | pin server-captured `messaging_account_id`; use `+` plus full DDI; no fallback/retry on rejection |
| Meta own account approved asset | real proof requires actually APPROVED eligible template | `unknown` | not probed in this planning turn | future operator-assisted proof only | no fixture substitutes; unavailable asset prevents completed claim |
| Existing local runtime/readiness | delivery needs current clean candidate and disposable validation | `stale` | not reprobed for this task | future DevOps handoff | source-bound assurances and topology re-resolution required |
| ST-CON-05 catalog | shared template observation/lease/fence/TTL and remote port | inherited delivered contract | 2026-10-22 handoff | completed TODO, not re-run here | reuse unchanged; any required mutation returns to review |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `operational-coder` after approved strategic handoff; supporting assurance and DevOps profiles at their scoped gates.
- **Active technical scope:** `nestjs`, `react`, `vite`, `postgresql`, `prisma`, `docker`.
- **Expected supporting profiles:** `assurance-tester-quality`, `assurance-security-adversarial`, `operational-devops` at their gates.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/README.md` returned in scope, exit0; documentation only.

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Operational / Coder | after v1.1 contract freeze, fresh reviews/guards, and explicit APROVADO | scoped product paths in diff contract | planned; no implementation authority |
| Operational / Coder | Assurance / Tester-Quality + Security | independent delivery evidence after implementation | harness/evidence package | planned |
| Operational / Coder | Operational / DevOps | disposable migration, source-bound local activation and assisted proof | approved local runtime only | planned |

## Complexity

- **Level (`small|medium|big`):** `big`
- **Checkpoint policy:** one writer, principal checkout, explicit review checkpoints; no worktrees/copies.
- **Why this level:** cross-module public contract, persistence, transport, authentication, external side effect and recovery semantics.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/inbox-and-conversations.md`
- **Secondary module docs:** `foundation_documentation/modules/integrations-and-channels.md`; completed ST-CON-05 owner TODO reference (no new template module).
- **Planned decision promotion targets:** inbox module first-send/open/recovery and trusted-window sections; integrations module Channel payload/capability and scoped resolver section.
- **Module decision consolidation targets:** same sections only after implementation and reviews; no module docs edited in this planning slice.

## Decision Pending (Resolve Before Freeze)

Nenhuma escolha de produto delegada ao operador nesta etapa: recomendações D-01..D-10 abaixo definem a proposta concreta. Revisores devem desafiar defeitos materiais antes de APROVADO. Readiness/asset APPROVED e prova física são dependências futuras explícitas, não fatos presumidos.

## Decisions (Resolved Before Freeze)

Decisões selecionadas para revisão, ainda sem aprovação de execução. A alternativa C de D-02 é a recomendação concreta. Mudança material após reviews exige reconvergência e freeze atualizado antes de pedir aprovação.

- [x] D-01 — preserve BU+contact uniqueness and current grant; required 8–15 digit normalized DDI without country guess. No CRM/provider side effects on open. New conversation `QUEUED`, unread zero, lastMessageAt null; order empty rows by COALESCE(lastMessageAt,createdAt).
- [x] D-02 — alternatives: **A)** a second `sendTemplate` Channel method (splits the abstract operation and adds obligations to every adapter); **B)** parallel concrete sender (bypasses scoped resolver/common acceptance); **C)** one `sendMessage` with discriminated text/template union and readonly `supportedKinds` (selected proposal). C intentionally supersedes ST-CON-06's delivered text-only payload while retaining one method. Avoid DI cycle: `TemplateManagementModule` already imports `ChannelTransportModule`, therefore `ChannelTransportModule`/`OutboundService` must not import or inject management. Initial orchestration composes both, reuses `listTemplates/getTemplate`, and passes a validated immutable provider-agnostic descriptor plus optional generic per-attempt dispatch fence through the same `sendMessage`; management port gets no send method. Meta send client completes its remaining grant/phone GETs, then calls the fence to CAS-claim immediately before POST, chained with current-context guard. No network/retry in fence/transaction, provider branching in domain/consumers, casts/`instanceof`, or generic plugin platform. Reviewer assesses substitutability, dependency/harness, blast, maintenance and performance.
- [x] D-03 — initial-intent coordinator belongs to inbox; calls common `OutboundService` dispatch and sole `MessageAcceptanceService`. If needed, add scoped transaction collaboration to that owner while preserving current wrapper. Do not copy sender, acceptance or finalization into coordinator; no claim existing transaction integration already exists. Normative r1 explicit initial selection/context equality and payload/window-specific fence below are part of this decision.
- [x] D-04 — new nullable officialInboundAt is written only from verified signed Meta IN timestamp passing positive integer/nonfuture/resource identity checks. No backfill. Window is max trusted IN on selected current resource and conversation `<24h`; same policy for sender and availability/batched BFF/public/BOT projections. Preserve createdAt timeline/cursors; use bounded index and retain ST06 index.
- [x] D-05 — shared ST-05 catalog route/projector only. Preview route `POST /api/bff/conversations/:id/initial-message-preview` is local/read-only. Before each new template send, recheck same-account current asset by trusted observed name using existing `listTemplates`, at most two filtered pages, and require exhausted exact ID/name/language/semantic match; `getTemplate(id)` alone does not prove account membership. Official raw reference receipt confirms optional supported `messaging_account_id`; pin the server-captured account. Meta recipient wire format is `+` plus full DDI while domain identity remains canonical digits; no fallback/retry on rejection. Normative r1 initial renderer validates POSITIONAL independently of inherited authoring flags and fingerprints unchanged catalog components.
- [x] D-06 — endpoints: `POST /conversations/:id/initial-messages`; `GET start-options`; `GET attempt`; authenticated `POST reconcile` and `POST acknowledge`. UUID per BU+actor; replay canonical request before provider reads after current grant check. PREPARED lease 90s. All remote asset/grant/phone preflight GETs complete before the SENDING claim; a generic dispatch-fence hook on the same `sendMessage` CAS-claims immediately before the sole POST. Expiry during preflight proves zero POST. Pre-dispatch failure rejects/releases; uncertain SENDING locks slot as AMBIGUOUS. Persist known external ID separately before local acceptance; recovery is local-only, with no fuzzy echo or missing-ID Message. Acknowledgment follows explicit classification and irreversibly releases; a late result cannot reacquire slot or mutate newer owner/status. Normative r1 transaction ordering and exact readback/one local re-entry applies. Initial risk acknowledgment for either allowed state waits until original persisted dispatchDeadlineAt=reservationDBtime+90s, never renewed; early409 ACK_TOO_EARLY.
- [x] D-07 — composer BFF blocks new/empty/unresolved slot before any HTTP; public/BOT must honor same active slot before dispatch without global durable-intent conversion; preserve existing mappings outside this bounded change. O resultado novo é BLOCKED, code INITIAL_SEND_IN_PROGRESS, HTTP409, somente attemptId local autorizado e safe state; nenhuma rede. Sem slot, callers antigos seguem fluxo anterior. BFF /messages em conversa sem mensagem de transporte retorna INITIAL_SEND_REQUIRED409; API pública/BOT sem slot preservam seu fluxo próprio existente. Ver Dispatch Interlock abaixo. Normative r1 owner-token admission, no time takeover of uncertain dispatch and separate local-only token recovery applies.
- [x] D-08 — template renderer supports text BODY NAMED/POSITIONAL, static header/footer only, <=20 params and stated length bounds. Preview binds exact conversation/contact/context/fingerprint, escaped and read-only. Catalog observation at most 300s is not send authorization.
- [x] D-09 — maximum six GETs / one POST per new official template attempt, 10s each, 75s budget <90s lease; limits 10/min actor, 60/hour canonical account/resource. Official raw-contract receipt confirms account pinning and recipient formatting; actual account/asset readiness remains unknown. Disposable local TEST migration only after approval, explicit preflight, lock5s/statement60s, no reset/drop. Local proof sequence as DOD-12.

- [x] D-10 — Certeza local: reserva, claim, persistência de ID externo/recibo e release de slot exigem confirmação positiva ou readback exato da chave capturada após erro de commit. Erro Prisma não prova rollback. Sem confirmação de claim original não há POST; persistência incerta não libera slot nem admite nova tentativa. ACK externo conhecido permanece CONFIRMED e nunca vira recusa por falha local. Persistência do fato/Message e projeção/realtime são dimensões separadas, sem falso RECORDED. Provar rollback real e commit real com perda do ACK em cada fronteira com PG, sem protocolo genérico de operações. Hash opaco canônico de conta usa o namespace existente meta-waba+NUL+accountId; extrair helper de integração preservando bytes/ST05observations, e expor só referência opaca no contexto do canal, nunca aceitar accountId do browser.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling (`Preserve|Supersede (Intentional)|Out of Scope`) | Evidence |
| --- | --- | --- | --- |
| inbox-and-conversations: BU/contact uniqueness | Conversation unique by BU+contact | Preserve | current Prisma source, exact anchor to be captured in fresh package |
| inbox-and-conversations: ST-CON-01 message acceptance | one MessageAcceptance owner; no exactly-once external/outbox | Preserve; narrow scoped transaction collaboration proposed | module handoff and current source |
| integrations-and-channels: ST-CON-06 Channel | one text sendMessage / adapter resolver | Supersede (Intentional) only text-only payload limit if C accepted | module ST-CON-06 contract and sealed source |
| integrations-and-channels: current window rule | latest IN stored createdAt, unfiltered by transport | Supersede (Intentional) with trusted official timestamp/resource selection | module ST-CON-06 handoff; exact code anchor pending freeze |
| integrations-and-channels: ST-CON-05 management/catalog | narrow separate management resolver + shared catalog projector | Preserve; remove duplicate route proposal | completed ST-CON-05 TODO and current files |
| ST-ATT-01 timeline | createdAt/cursor behavior and read acknowledgement | Preserve | inbox module contract |
| SEC-R6-04 / OPS-R4-01 / TQA-ST05-03 | delivered constraints/debts | Preserve | ST-CON-05 completed handoff; no cleanup in this slice |

## Decision Baseline (Frozen Before Implementation)

Proposta selecionada abaixo deve coincidir com o freeze publicado e os reviews atuais. APROVADO e authority pós-ingestão ainda necessários.

- [ ] D-01 — preserve BU+contact uniqueness and current grant; required 8–15 digit normalized DDI without country guess. No CRM/provider side effects on open. New conversation `QUEUED`, unread zero, lastMessageAt null; order empty rows by COALESCE(lastMessageAt,createdAt).
- [ ] D-02 — alternatives: **A)** a second `sendTemplate` Channel method (splits the abstract operation and adds obligations to every adapter); **B)** parallel concrete sender (bypasses scoped resolver/common acceptance); **C)** one `sendMessage` with discriminated text/template union and readonly `supportedKinds` (selected proposal). C intentionally supersedes ST-CON-06's delivered text-only payload while retaining one method. Avoid DI cycle: `TemplateManagementModule` already imports `ChannelTransportModule`, therefore `ChannelTransportModule`/`OutboundService` must not import or inject management. Initial orchestration composes both, reuses `listTemplates/getTemplate`, and passes a validated immutable provider-agnostic descriptor plus optional generic per-attempt dispatch fence through the same `sendMessage`; management port gets no send method. Meta send client completes its remaining grant/phone GETs, then calls the fence to CAS-claim immediately before POST, chained with current-context guard. No network/retry in fence/transaction, provider branching in domain/consumers, casts/`instanceof`, or generic plugin platform. Reviewer assesses substitutability, dependency/harness, blast, maintenance and performance.
- [ ] D-03 — initial-intent coordinator belongs to inbox; calls common `OutboundService` dispatch and sole `MessageAcceptanceService`. If needed, add scoped transaction collaboration to that owner while preserving current wrapper. Do not copy sender, acceptance or finalization into coordinator; no claim existing transaction integration already exists. Normative r1 explicit initial selection/context equality and payload/window-specific fence below are part of this decision.
- [ ] D-04 — new nullable officialInboundAt is written only from verified signed Meta IN timestamp passing positive integer/nonfuture/resource identity checks. No backfill. Window is max trusted IN on selected current resource and conversation `<24h`; same policy for sender and availability/batched BFF/public/BOT projections. Preserve createdAt timeline/cursors; use bounded index and retain ST06 index.
- [ ] D-05 — shared ST-05 catalog route/projector only. Preview route `POST /api/bff/conversations/:id/initial-message-preview` is local/read-only. Before each new template send, recheck same-account current asset by trusted observed name using existing `listTemplates`, at most two filtered pages, and require exhausted exact ID/name/language/semantic match; `getTemplate(id)` alone does not prove account membership. Official raw reference receipt confirms optional supported `messaging_account_id`; pin the server-captured account. Meta recipient wire format is `+` plus full DDI while domain identity remains canonical digits; no fallback/retry on rejection. Normative r1 initial renderer validates POSITIONAL independently of inherited authoring flags and fingerprints unchanged catalog components.
- [ ] D-06 — endpoints: `POST /conversations/:id/initial-messages`; `GET start-options`; `GET attempt`; authenticated `POST reconcile` and `POST acknowledge`. UUID per BU+actor; replay canonical request before provider reads after current grant check. PREPARED lease 90s. All remote asset/grant/phone preflight GETs complete before the SENDING claim; a generic dispatch-fence hook on the same `sendMessage` CAS-claims immediately before the sole POST. Expiry during preflight proves zero POST. Pre-dispatch failure rejects/releases; uncertain SENDING locks slot as AMBIGUOUS. Persist known external ID separately before local acceptance; recovery is local-only, with no fuzzy echo or missing-ID Message. Acknowledgment follows explicit classification and irreversibly releases; a late result cannot reacquire slot or mutate newer owner/status. Normative r1 transaction ordering and exact readback/one local re-entry applies. Initial risk acknowledgment for either allowed state waits until original persisted dispatchDeadlineAt=reservationDBtime+90s, never renewed; early409 ACK_TOO_EARLY.
- [ ] D-07 — composer BFF blocks new/empty/unresolved slot before any HTTP; public/BOT must honor same active slot before dispatch without global durable-intent conversion; preserve existing mappings outside this bounded change. O resultado novo é BLOCKED, code INITIAL_SEND_IN_PROGRESS, HTTP409, somente attemptId local autorizado e safe state; nenhuma rede. Sem slot, callers antigos seguem fluxo anterior. BFF /messages em conversa sem mensagem de transporte retorna INITIAL_SEND_REQUIRED409; API pública/BOT sem slot preservam seu fluxo próprio existente. Ver Dispatch Interlock abaixo. Normative r1 owner-token admission, no time takeover of uncertain dispatch and separate local-only token recovery applies.
- [ ] D-08 — template renderer supports text BODY NAMED/POSITIONAL, static header/footer only, <=20 params and stated length bounds. Preview binds exact conversation/contact/context/fingerprint, escaped and read-only. Catalog observation at most 300s is not send authorization.
- [ ] D-09 — maximum six GETs / one POST per new official template attempt, 10s each, 75s budget <90s lease; limits 10/min actor, 60/hour canonical account/resource. Official raw-contract receipt confirms account pinning and recipient formatting; actual account/asset readiness remains unknown. Disposable local TEST migration only after approval, explicit preflight, lock5s/statement60s, no reset/drop. Local proof sequence as DOD-12.
- [ ] D-10 — Certeza local: reserva, claim, persistência de ID externo/recibo e release de slot exigem confirmação positiva ou readback exato da chave capturada após erro de commit. Erro Prisma não prova rollback. Sem confirmação de claim original não há POST; persistência incerta não libera slot nem admite nova tentativa. ACK externo conhecido permanece CONFIRMED e nunca vira recusa por falha local. Persistência do fato/Message e projeção/realtime são dimensões separadas, sem falso RECORDED. Provar rollback real e commit real com perda do ACK em cada fronteira com PG, sem protocolo genérico de operações. Hash opaco canônico de conta usa o namespace existente meta-waba+NUL+accountId; extrair helper de integração preservando bytes/ST05observations, e expor só referência opaca no contexto do canal, nunca aceitar accountId do browser.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability:** `required`
- **Why this applies:** contract introduces durable first-send ownership and intentionally proposes two narrow supersedes to Channel payload and official-window timestamp truth.
- **Deviation / debt being retired:** split/missing first-send lifecycle; current timestamp selection can use unrelated stored IN; Channel's delivered payload is text-only.
- **Target steady-state after closeout:** one Channel send abstraction; one common Outbound dispatch; sole MessageAcceptance owner; one template-management/catalog owner; one initial-intent coordinator; current selected resource's trusted official window; monotonic attempt and slot recovery.
- **Temporary exceptions allowed:** none proposed.
- **Cutover / removal condition:** no duplicate channel/template routes or send owners; only after all current callers and projections share the approved policy and regression matrix passes.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Channel operation selected through abstract resolver | ST-CON-06 module contract | adapters/domain | provider choice remains scoped and substituted by contract |
| one MessageAcceptance owner keyed by external ID | ST-CON-01 module contract | all new Message writes | sender/echo converge without duplicate owner |
| shared ST-05 projector and management capability | ST-CON-05 completed TODO | catalog reads | one observation/freshness authority |
| transaction-free provider I/O | ST-CON-05/06 contracts | all HTTP | DB locks never span network calls |
| idempotent local intent, no external exactly-once claim | this proposed contract | initial attempts | uncertainty cannot become blind resend |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why Forbidden | Exception Policy |
| --- | --- | --- | --- |
| second Channel send method or parallel sender | API/adherence search and dependency contract | splits abstract transport/common acceptance | none unless renewed approval |
| provider if/instanceof in domain/consumers or casts | architecture guard/grep/code review | leaks concrete provider details | none |
| duplicate catalog projector/route/cache/DTO owner | route/DI/dependency tests | splits ST-05 ownership | none |
| fallback to alternate connected channel | resolver/request test | may dispatch under unconfirmed account | none |
| timestamp fallback to createdAt/raw/import/nonofficial | window tests/code inspection | manufactures 24h eligibility | none |
| automatic retry/fuzzy match/missing-ID Message | fault-injection tests | may duplicate external contact | none |
| HTTP inside DB transaction or hidden extra probe | request counter/transaction barriers | violates bounded latency/locks | none |
| generic future provider/plugin framework | architecture review | adds unrequested platform | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| dependency/substitutability tests | Channel/factories | existing harness plus new typed-kind cases | concrete branching, new required methods, wrong support declaration | implement-in-this-TODO | contract and fake tests |
| adapter protocol tests | Meta/Evolution | request recorder, no live provider | extra/unbounded HTTP; Evolution template HTTP | implement-in-this-TODO | exact counters and payload fixtures |
| architecture/adherence check | inbox/integrations | canonical project guard after freeze | duplicate owners, provider leak, wrong route owner | implement-in-this-todo | post-implementation review |
| DB race/fault harness | attempt/slot/Message | PG barriers and CAS checks | duplicate POST, slot reacquisition, status/owner steal | implement-in-this-TODO | real disposable PG |
| schema/migration gate | Prisma | migrate deploy/status with bounded preflight | destructive or blocking migration | implement-in-this-TODO | authorized local DB only |
| consumer regressions | BFF/public/BOT/Web | existing API/E2E/Playwright suites | broken text send/window/timeline/UI recovery | implement-in-this-TODO | exact commands after approval |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/architecture-r1.merge.json + architecture-r1-resolution.md; four material findings integrated into the contract, subject to fresh critique before approval
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **No-go handling:** unresolved material divergence returns to contract/review; no approval or completion claim.

## Gate: Review Baseline Freeze

- **Gate decision:** required
- **Why this decision:** current proposed04 package must be published before reviews.
- **Trigger stage:** before first planning review/guard
- **Baseline branch:** main
- **Baseline commit:** a107a6ab73172c70ef18dc3a34c8681d5e1b5f31
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** architecture r1 and critique r1 completed; both finite critique clarifications published in refreshed freeze a107a6ab before affected fresh critique r2; only gate metadata added afterward.
- **Evidence / reference:** Foundation main a107a6ab73172c70ef18dc3a34c8681d5e1b5f31 pushed origin/main, exit0; evidence/freeze-after-critique-r1-v1.1.json records actual publication.
- **Waiver authority / reference (required if waived):** n/a

## Gate: Review Scope Drift

- **Gate decision:** required
- **Why this decision:** conferir que aprovação usará pacote revisado.
- **Trigger stage:** after the planning-side review/guard cycle converges and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Material sections compared:** Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **No-go handling rule:** reconvergir pacote/review e renovar freeze, sem implementação.
- **Gate status:** no_material_findings
- **Findings summary:** canonical guard GO:23 material sections compared, zero changed against pushed a107a6ab. Initial run v1.1 exposed only Windows path casing in Git adapter; corrected orchestration adapter v1.2 confirmed no scope drift; no Delphi/product change.
- **Evidence / reference:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/review-scope-drift-v1.2.json GO against pushed a107a6ab; v1.1 is preserved failed adapter evidence, not a waiver
- **Waiver authority / reference (required if waived):** n/a

## Questions To Close

- [x] Architecture option C, explicit initial resolver and descriptor-to-context equality: selected by r1 and frozen in normative r1 contract; fresh critique still required.
- [x] MessageAcceptance transaction collaboration and CAS-before-own-mutation: fixed ordering and bounded whole-local-tx recovery defined in normative r1 contract.
- [x] Ordinary-versus-initial race: per-owner admissions with no uncertain time takeover; same lock admission, independent token release and explicit local risk acknowledgment, detailed below.
- [x] POSITIONAL consumption: initial renderer validates existing components without changing ST-05 flags/parser/projector.
- [x] Exact source admission: same acceptance owner explicitly included with supplemental pre-edit seal; other allowed paths remain in strict inventory.
- [ ] Future execution dependency only: actual own-account APPROVED asset and healthy disposable/runtime source binding; no current enum/runtime claim. Required proof cannot be waived by mocks or this planning approval.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Conversation unique BU/contact; list current order lastMessageAt and no manual-open BFF route | api-app/prisma/schema.prisma:389; api-app/src/domain/inbox/conversations.service.ts:61; api-app/src/surfaces/bff/conversations.controller.ts:20 | reconverge upsert/list and API before approval | High; source inspection only | Keep as Assumption |
| A-02 | Channel only text today; bound factories/current-context guard exist | api-app/src/domain/channels/transport/channel.ts:28; api-app/src/integrations/channels/meta-channel.ts:13; api-app/src/integrations/channels/evolution-channel.ts:13 | reconverge explicit supersede and dependency harness | High; source inspection only | Keep as Assumption |
| A-03 | Acceptance owns its own transaction; common sender finalization is separate | api-app/src/domain/inbox/message-acceptance.service.ts:82; api-app/src/domain/inbox/outbound.service.ts:83 | do not pretend tx collaboration exists; adapt same owner explicitly | High; source inspection only | Keep as Assumption |
| A-04 | Catalog and template provider owner already delivered; read-ID alone lacks fresh parent membership proof | api-app/src/domain/message-templates/template-observation.service.ts:115; api-app/src/integrations/meta/message-template.client.ts:118 | do not duplicate catalog or assume ID grants account scope | High; source inspection only | Keep as Assumption |
| A-05 | Window currently uses stored createdAt/latest any IN; signed Meta adapter discards provider timestamp | api-app/src/domain/inbox/outbound.service.ts:244; api-app/src/integrations/channels/prisma-channel-resolver.ts:68; api-app/src/surfaces/webhooks/meta.controller.ts:103 | reconverge all projections/consumers before approval | High; source inspection only | Keep as Assumption |
| A-06 | Template management depends on transport for its single credential resolver, so reverse import would cycle | api-app/src/integrations/message-templates/template-management.module.ts:1; api-app/src/integrations/channels/channel-transport.module.ts:1 | composition of initial flow imports both; no reverse dependency | High; source inspection only | Keep as Assumption |
| A-07 | Browser has context generations and shared catalog API wrapper | web-app/src/telas/Inbox.tsx:50; web-app/src/api.ts:352 | reuse actual guards and freeze new flow-specific freshness | High; source inspection only | Keep as Assumption |
| A-08 | Current canonical opaque management account reference uses a private hash helper | api-app/src/integrations/message-templates/template-management.resolver.ts:83 | extract exact byte-compatible integration helper; no protocol IDs in domain input | High; source inspection only | Keep as Assumption |

External facts and actual readiness are dependency records, not fictitious code-backed assumptions: official primary docs verified200 anonymously via Accept:text/markdown on2026-10-22; approved asset enum/current runtime not queried.

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces

Candidate only: inbox domain/services/schema, BFF and inbound webhook boundary, Channel abstract contract and concrete adapters/resolver, Meta template protocol adapter, React Inbox, focused contract/E2E/Playwright harness. Exact proposed admission is in the strict inventory, including r1 supplemental acceptance-owner seal; any further deviation returns to review. No template authoring/catalog owner, no credentials/config, no runtime routing changes.

### Ordered Steps

1. Freeze this v1.1 TODO and sealed baseline through root-owned Foundation workflow; preserve the v1.0 archive untouched.
2. Fresh architecture opinion challenges D-01..10 and compares A/B/C with cost, risk, blast radius, maintenance, performance, elegance and structural quality.
3. Fresh independent critique; integrate findings in TODO and regenerate only affected package; run assumption/code and scope-drift guards. All statuses are not_run until actually produced.
4. Use the verified official raw contract: pin the server-captured `messaging_account_id`, format Meta recipients as `+` + full DDI, keep storage/domain identity provider-neutral digits, and test same-country/cross-country plus existing ordinary text semantics. Never fallback/retry if pinned request is rejected.
5. Human explicitly approves the converged v1.1, then authority guard must return go before implementation begins.
6. Operational/Coder implements admitted exact paths; keep all sealed non-admitted bytes exact, no worktrees or second writer.
7. Additive migration only after explicit candidate/environment preflight on approved disposable TEST DB, lock timeout 5s, statement timeout 60s; no reset/drop.
8. Run targeted domain/contract/PG tests and full existing BFF/public/BOT regressions; Playwright fresh bundle against real backend; bounded counters and performance evidence.
9. After candidate GREEN and runtime provenance assurance, run own local channel checks and assisted unofficial/official APPROVED/reply proof. If no eligible asset exists, do not claim complete.
10. Fresh delivery assurance/reviews/guards, reconcile stable module decisions and closeout only after all criteria have exact evidence.

### Test Strategy

- **Strategy:** test-first
- **Why:** irreversible external side effects, shared dispatch contract and concurrency require causal fail-first proof.
- **Fail-first targets:** open/reuse authorization and races; typed unsupported zero HTTP; trusted resource window; intent/dispatch/readback fault barriers; real-BFF initiation/recovery browser flow. Capture RED after approval and before the corresponding production change.

No implementation tests have been run for this planning draft. Future tests are those in VAL-01..09, including substitutability, zero-HTTP negative case, PG barriers, one-POST counters, signature/timestamp provenance, current account list membership, endpoint ACL/CSRF, consumer regressions, freshness and real browser mutation. Never substitute mocks for the required real BFF/PG flow or an actual approved-asset proof.

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 open/reuse + empty list | creates persisted conversation; changes list projection and NOVA_CONVERSA behavior on later first inbound | web-only | Playwright mutation | yes | yes | start-conversation.spec.ts with real BFF/PG, parallel open/readback, truthful empty list and open-without-send→first inbound NOVA_CONVERSA/keyword fixtures | n/a |
| DOD-03/09 catalog and preview | safe DTO, rendered text, freshness, current supported template | web-only | Playwright mutation | yes | yes | existing shared catalog + preview request counter, persisted observation fixture and escaped DOM | n/a |
| DOD-02/04/05/06 initial send | external effect, persisted outcome and conversation ownership | web-only | Playwright mutation | yes | yes | real BFF/PG and protocol-bound fake, exact POST counter, ID/Message/owner readback | n/a |
| DOD-05 recovery/reconcile/ack | safe state/actions persist after reload; irreversible slot release | web-only | Playwright mutation | yes | yes | timeout/ACK-loss fixtures, reload, local reconcile/ack before/after immutable deadline, late-result barrier | n/a |
| DOD-07 qualified window | affects options/composer and public/BOT send eligibility | web-only | Playwright mutation | yes | yes | signed-provider fixture and selected resource, boundary timestamp, unchanged timeline/cursor | n/a |
| DOD-08 ordinary composer interlock | send must block on initial activity, preserve normal text callers | web-only | Playwright mutation | yes | yes | backend races/counters and real browser error/recovery; API/BOT contract tests | n/a |
| DOD-10/11 rate/schema/runtime | safe errors and persisted state; served bundle must match source | web-only | Playwright mutation | yes | yes | migration/provenance + tenant/rate test fixture and refreshed served bundle | n/a |
| DOD-12 own unofficial and approved official | actual channel capability, provider acceptance and recipient reply | web-only | Playwright readonly | no | yes | later explicitly authorized operator first-send + reply, own preserved local source-bound runtime | operator performs actual sends; no browser automation contacts real recipients |

### Frontend / Consumer Matrix

| Producer / contract | Existing consumer / owner | Required preservation or deliberate change | Planned proof |
| --- | --- | --- | --- |
| conversation open/list | React Inbox + BFF conversations controller | no implicit send/read/claim; empty ordering based on COALESCE, stable createdAt/id | PG contract + real browser create/reuse/list |
| shared template catalog | Inbox selector + delivered Modelos | same ST-05 DTO, projector, lease/fence/TTL; authoring behavior stays sealed | catalog dependency and inherited authoring regressions |
| preview/new attempt state | new NovaConversa + Inbox | explicit channel; context generations and draft ownership; escaped rendering | real-BFF Playwright A-B-A/role revoke/late response |
| attempt read/reconcile/ack | recovery controls | local state only; no credentials; irreversible release and duplicate risk stated | real PG/readback + browser reload/recovery |
| Channel.sendMessage | common OutboundService + bound Meta/Evolution/fakes | one operation; text regression; declared kinds and unsupported zero HTTP | substitutability/dependency/raw protocol |
| common outbound dispatch interlock | BFF /messages, public API, incoming BOT | same shared dispatch boundary; typed safe block while unresolved; existing outside-slot mappings | parallel PG barriers + endpoint/BOT regressions |
| signed officialInboundAt | sender policy + availability projections | one trusted current-resource rule, batch/index bounds; no createdAt fallback | signed timestamp cases, API DTO and browser options |
| keyed MessageAcceptance | sender and verified provider echo | sole owner, exact identity/externalID dedup; no missing-ID Message for new flow | PG dual-order barriers and realtime winner count |
| manual-open row creation then first inbound | IncomingService / Typebot trigger | opening invokes no automation; NOVA_CONVERSA remains tied to actual row creation, so manual-open empty row means false on subsequent inbound; keyword rule preserved | PG integration and real-BFF open/readback; isolated new-conversation/keyword trigger fixtures |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status (completion projection) | Evidence Artifact / Command | Status (authority projection) | Notes | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| api / lint/build/unit/PG | schema/domain/adapters/BFF/webhook | bash scripts/test-channels-local.sh all | Local-Implemented | planned | api-app/test/initial-message*.e2e-spec.ts; new source-owned unit/adapter suites | planned | no test run during planning | open/contact/slot/claim/ACK loss/echo/CAS/account/qualified window and existing public/BOT/BFF regressions | own disposable Node22/PG16; bound fake external provider; real BFF/PG; concurrent actor/BU/tenant/account cases |
| web / build/unit/Playwright | new manual initiation and recovery | bash scripts/test-channels-local.sh all | Local-Implemented | planned | web-app/e2e/start-conversation.spec.ts (new) and inherited suites | planned | source-owned mutation and readonly journeys | open/reuse/preview/explicit channel/text/template/refresh/reconcile/ack; stale A-B-A and role revocation | same disposable BFF/PG; new rebuilt served bundle attested before browser; fake external boundary only |
| root / canonical parity and public boundary | existing runner remains execution owner | bash scripts/test-channels-local.sh all | Local-Implemented | planned | scripts/test-channels-local.sh; scripts/check-channels-ci-parity.py | planned | inherited scripts stay byte-exact; already use public inventory | full suite ownership/bootstrap/build/cleanup/provenance, no .local-files traversal | existing owned validation namespace only; no actual env/private read |

### Runtime / Rollout Notes

No config/credential/routing mutation during planning. Future local proof only after candidate GREEN, disposable migration assurance, source/image/runtime binding and approval. Owned local HTTPS origin only. No public/Railway promotion authorized.

## Plan Review Gate

- **Complexity:** big
- **Checkpoint policy:** section-by-section architecture/contract, schema/concurrency, adapter/security, browser/performance and final adherence. Planning reviews precede APROVADO; delivery checkpoints require their own actual evidence.

- **Decision:** required, fresh after freeze
- **Status:** `findings_integrated`
- **Baseline history:** architecture r1 and critique r1 integrations published through a107a6ab before fresh critique r2; r2 no material findings; full seven-axis issue/option cards and checkpoint policy retained
- **Review sections:** architecture, quality, tests, performance, security, elegance and structural design.

### Scoped Review Questions

| ID | Section | Finding / question to challenge | Options / tradeoff | Required disposition |
| --- | --- | --- | --- | --- |
| ARCH-01 | Architecture | Is one union send method plus supportedKinds a sound abstraction? | A second method expands the abstract contract; B parallel sender forks policy/acceptance; C one discriminated operation keeps one abstract method but widens payload and all adapter contracts | Compare substitution, consumers, dependencies/harness, blast and future extension; no future plugin framework |
| ARCH-02 | Architecture | Can initial coordinator reuse shared sender while durable acceptance spans external I/O, without a TemplateManagementModule ↔ ChannelTransportModule cycle? | composition imports ChannelTransportModule and TemplateManagementModule only at initial-flow boundary; pass provider-agnostic descriptor to sender. Common OutboundService does not inject management resolver. Reuse listTemplates/getTemplate; no send method on management port. | Preserve one MessageAcceptance owner and existing wrapper semantics; no HTTP in transaction |
| ARCH-03 | Architecture | How capture immutable selected channel/resource/credential context and enforce current version immediately before POST, after every remote preflight GET? | all bounded grant/phone/template GETs first, then abstract attempt fence/CAS immediately before POST, chained with current-context fence; test expired PREPARED zero POST | Selected same identity only; current-version/CAS checks; stale context fails closed |
| ARCH-04 | Architecture | Does one trusted timestamp policy cover sender and every availability projection? | nullable qualified Meta timestamp + bounded index vs old createdAt rule | no fallback/backfill; preserve timeline; prove all BFF/public/BOT consumers |
| ARCH-05 | Architecture | Does same-account list-by-trusted-name prove current exact remote asset with finite reads? | bounded two filtered pages + exact semantics vs ID-only GET | reject partial/exhaustion/ambiguous/status unknown; no browser cursor authority |
| QUALITY-01 | Quality | Are durable outcomes and acknowledgment truthful and monotonic after timeout, process death, late result and slot release? | single POST, AMBIGUOUS lock, explicit irreversible ack vs retry convenience | prove state transition table and no status/owner steal |
| QUALITY-02 | Quality | Are open/reuse and empty-conversation UI truthful with no implicit send/read/claim? | atomic idempotent create/reuse; explicit user confirmation | role/tenant, race and refresh UX |
| TEST-01 | Tests | Are tests proving absence of provider call, no duplicate POST, current-resource membership and no missing-ID Message? | real counters/barriers and typed fakes vs happy-path mocks | adversarial integration cases and substitutability harness |
| TEST-02 | Tests | Are existing BFF/public/BOT text paths and composer errors preserved? | focused regression matrix vs broad rewritten tests | exact mapping and endpoint response assertions |
| PERF-01 | Performance | Are read budgets, list/index query, lease and API limits mutually consistent under concurrency? | max6 GET/1POST, 10s each, 75s total, lease90s; bounded rate keys | measure counts/queries/latency; no network while locked |
| PERF-02 | Performance | Does trusted-window projection remain batched and index-backed at scale? | direction/resource-filtered indexed query vs per-row hydration | query count, examined rows and EXPLAIN under OUT-heavy/no-IN fixtures |
| SEC-01 | Security | Can actor, BU, contact, selected resource, remote asset, or attempt ID be confused across tenants/accounts? | scoped authorization and canonical account namespace | no foreign existence leaks; stale/foreign before effects; safe DTO only |
| SEC-02 | Security | Are preview/template params bounded and safe, and recovery authenticated/CSRF protected? | text-only grammar and explicit ack risk vs arbitrary provider payload | parser bounds, escaping, no secrets/provider body, replay ordering after grant |
| ELEGANCE-01 | Elegance | Does proposal use existing owners with minimal new concepts? | one coordinator + one common sender + one acceptance + shared catalog vs duplicates | explain each boundary; no parallel template authoring or platform abstraction |
| STRUCT-01 | Structural | Are modules and dependency direction coherent across inbox, channels, templates and BFF? | inbox orchestrates ports; adapters own provider protocol; catalog stays ST-05 | no domain Meta HTTP/provider branches; no new owner for Message/template observation |
| STRUCT-02 | Structural | Are schema, transaction and external side-effect boundaries explicit and recoverable? | durable states/slot/unique constraints/CAS vs locks or memory state | migration and crash matrix; no pretending at-most-once means exactly-once |

### Plan Review Issue Cards — full option comparison

The recommended options below include the r1 fixes. These are plan-review choices, not implemented evidence. Cost means relative implementation/test work for this bounded slice. All impacts are predicted; runtime performance is unmeasured. No material finding is hidden by a low-cost option.

| Issue ID / axis | Severity | Concrete evidence | Why now | Recommendation |
| --- | --- | --- | --- | --- |
| PR-ARCH / Architecture | high | api-app/src/domain/channels/transport/channel.ts:24; integrations/channel composition; ARCH-R1-03 | template outside window needs explicit scoped selection, one abstract method and no dependency cycle | C |
| PR-QUAL / Code Quality | high | api-app/src/domain/inbox/message-acceptance.service.ts:82,231; ARCH-R1-02 | self-mutated updatedAt and aborted transaction must not fake a current CAS | A |
| PR-TEST / Tests | high | api-app/src/domain/inbox/outbound.service.spec.ts:1; test/channel-transport.e2e-spec.ts; ARCH-R1-01 | mocks cannot prove exclusion or real commit/rollback ACK certainty | A |
| PR-PERF / Performance | medium | api-app/src/domain/inbox/outbound.service.ts:244; integrations/channels/prisma-channel-resolver.ts:68 | new window/account validation must be index-backed, batched and finitely bounded | A |
| PR-SEC / Security | high | api-app/src/surfaces/bff/conversations.controller.ts:20; integrations/message-templates/template-management.resolver.ts:83 | external first contact binds tenant/actor/context and exact current account/template | A |
| PR-ELEG / Elegance | medium | api-app/src/integrations/message-templates/template-management.module.ts:1; channel-transport.module.ts | avoid a second sender/projector or provider plugin platform | A |
| PR-STRUCT / Structural Soundness | high | api-app/src/domain/inbox/outbound.service.ts:37; ARCH-R1-01/02 | exclusive initial intent must coexist with ordinary callers without HTTP locks or unsafe lease takeover | A |

| Issue | Option / outcome | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-ARCH | A: second Channel.sendTemplate operation | medium | medium | cross-module | medium | neutral vs C | regresses: operation-specific expansion | mixed: ownership possible but broader contract |
| PR-ARCH | B: parallel concrete template sender | medium | high | cross-module | high | unknown, duplicate preflight likely | regresses | regresses: bypasses common scoped dispatch/acceptance |
| PR-ARCH | C recommended: discriminated same sendMessage + supportedKinds + explicit initial resolver/fence | high | medium | cross-module | medium | bounded extra validation; measured later | improves coherence | improves: one operation and owner graph |
| PR-QUAL | A recommended: same acceptance owner, pre-acceptance CAS, bounded whole-local-tx re-entry | medium | medium | module | low | extra short row lock; no network lock | improves | improves: truthful atomic local completion |
| PR-QUAL | B: duplicate Message/finalizer in initial service | medium | high | cross-module | high | unknown duplication | regresses | regresses: two mutation owners |
| PR-QUAL | C: do nothing; finalize after acceptance with stale updatedAt | low | high | module | high | fewer checks, invalid behavior | regresses | regresses: self-invalidating CAS |
| PR-TEST | A recommended: causal RED + real PG barriers/ACK faults + protocol recorder + real BFF browser | high | medium | cross-stack | medium | test time increases within owned runner | improves confidence without product workaround | improves |
| PR-TEST | B: happy-path mocks only | low | high | module | medium | faster tests, no concurrency proof | mixed | regresses: required failure states unproved |
| PR-TEST | C: weaken assertions to existing behavior | low | high | module | high | no valid improvement claim | regresses | regresses: test-only shortcut |
| PR-PERF | A recommended: filtered two-page account reads, shared request grant, bounded index/batched window | medium | medium | cross-module | medium | bounded extra latency/query work; measure | improves predictable limits | improves |
| PR-PERF | B: full account scan / per-row IN queries | medium | high | cross-module | high | regresses unbounded work/N+1 | regresses | regresses |
| PR-PERF | C: trust stale local catalog and createdAt window | low | high | cross-module | high | fewer reads with false authorization | regresses | regresses |
| PR-SEC | A recommended: current auth/CSRF, immutable full context, fresh exact account eligibility, local-only recovery | high | medium | cross-module | medium | bounded extra checks | improves explicit authority | improves |
| PR-SEC | B: accept arbitrary browser Graph payload/account/URL | low | high | cross-stack | high | unknown/unbounded | regresses | regresses: crosses credential/tenant boundary |
| PR-SEC | C: do nothing; no manual first contact capability | low | low | local | low | neutral | neutral | preserves baseline but does not deliver agreed story |
| PR-ELEG | A recommended: inbox coordinator composes delivered transport and management; one acceptance/projector | medium | medium | cross-module | low | avoids duplicated HTTP/cache | improves | improves |
| PR-ELEG | B: new generic provider/plugin/workflow platform | high | high | cross-stack | high | unknown overhead | regresses incidental complexity | mixed, unauthorized future platform |
| PR-ELEG | C: scattered provider branches in Inbox/domain | low | high | cross-stack | high | unknown drift | regresses | regresses DIP |
| PR-STRUCT | A recommended: per-owner ordinary tokens coexist, exclude initial slot; uncertain dispatch never expires into takeover | high | medium | cross-module | medium | short admission writes, ordinary concurrency preserved | acceptable bounded safety state | improves truthful exclusion |
| PR-STRUCT | B: one exclusive send lease for every caller | high | high | cross-module | high | regresses ordinary concurrency; unsafe expiry unless expanded recovery | regresses unnecessary platform | mixed, changes ordinary compatibility |
| PR-STRUCT | C: early SELECT or auto-expire SENDING | low | high | cross-module | high | superficially cheap but permits concurrent dispatch | regresses | regresses external-effect safety |

## Failure Modes & Edge Cases

- actor loses grant after creating PREPARED; replay must verify grant before exposing or dispatching but must not reread provider before canonical replay resolution.
- lease expires while remote validation is slow; claim CAS prevents any later dispatch.
- provider accepts but response is lost or ID malformed; AMBIGUOUS remains locked and never retries.
- known ID cannot be locally accepted due changed resource/generation; preserve ID as `EXTERNAL_ACCEPTED_LOCAL_BLOCKED`; quarantine/no Message without ID.
- operator acknowledges uncertainty, starts successor, then old ID arrives; old intent may improve its own local record only if still eligible but cannot take slot or change successor status/owner.
- simultaneous human claim/close while HTTP is in flight; final CAS respects the current owner/state.
- selected template changes status or semantic definition after catalog observation; fresh same-account check rejects before POST.
- selected phone shares a Messaging account; send must pin the captured account and correctly format full international recipient.
- signature invalid, timestamp missing/zero/fractional/future, imported or nonofficial IN; never open window from those records.
- official selected identity changes during send; no substitution/fallback to a newer connected channel.
- public/BOT/outbound composer races the active slot; all dispatch boundaries enforce slot policy with their existing response mapping.
- same phone contact with optional DDI input normalizes consistently without guessing country; validation and unique index handle concurrent creation.
- no eligible approved asset/account is available; honest blocker, never fixture-based completion.

## Residual Unknowns / Risks

- The current official own account and eligible APPROVED asset are not verified; documentation evidence does not establish account readiness.
- No current own-account APPROVED template availability is asserted.
- Runtime state/current validation owner is intentionally not reprobed during this planning-only slice.
- Exact current source anchors and consumer matrix are attached; final implementations must still prove inherited public/BOT mappings and ordinary concurrency.
- This contract proposes a material Channel supersede; architecture reviewer can reject C and require a revised draft/reapproval.

## Additional Architectural Opinions

Fresh internal no-context r1 completed: option C recommended, four material findings integrated as normative contract below. Raw/strict merge and resolution in current review package. Performance mixed/unmeasured; elegance acceptable; structural and operational fit mixed until r1 fixes are validated. Fresh critique must assess those fixes, not reuse old19/20 opinions. Root owns serialized documentation orchestration.

## Planning Finding Resolution Ledger

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-R1-01 / F-E3C20901 | Integrated | useful | partial | project | n/a | Normative r1 owner-token interlock, explicit ordinary compatibility, no uncertain expiry takeover, local-only risk recovery and complete barriers; Scope09/DoD08/Val02 updated. |
| ARCH-R1-02 / F-2D3CB947 | Integrated | useful | yes | project | n/a | Same acceptance owner explicitly admitted/sealed; original CAS before self-mutation; identity/conversation lock order; whole-local-tx rollback/readback/one re-entry; Scope07/DoD06/Val02. |
| ARCH-R1-03 / F-0715A55A | Integrated | useful | yes | project | n/a | Explicit initial resolver, exact management/transport full context equality, parameter/semantic descriptor, applicable text-window check at final fence; DoD09/Val03. |
| ARCH-R1-04 / F-E2F76277 | Integrated | useful | yes | project | n/a | Initial renderer over unchanged existing catalog components; separate initial semantic fingerprint and POSITIONAL ordering; no authoring/parser/projector flag change; DoD09/Val03. |

These dispositions amend proposed contract only. Fresh no-context critique must assess them after refreshed freeze. They do not assert production fixes or grant execution authority.

## Audit Trigger Matrix

- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/audit-floor-after-architecture-v1.1.json; actual guard GO with high review issue signal; finite deadline/automation clarifications do not change trigger matrix; no implementation audit claimed.

| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | escopo ST-CON-04; derivar após freeze |
| blast_radius | cross-stack | escopo ST-CON-04; derivar após freeze |
| behavioral_change_or_bugfix | yes | escopo ST-CON-04; derivar após freeze |
| changes_public_contract | yes | escopo ST-CON-04; derivar após freeze |
| touches_auth_or_tenant | yes | escopo ST-CON-04; derivar após freeze |
| touches_runtime_or_infra | yes | escopo ST-CON-04; derivar após freeze |
| touches_tests | yes | escopo ST-CON-04; derivar após freeze |
| critical_user_journey | yes | escopo ST-CON-04; derivar após freeze |
| release_or_promotion_critical | no | escopo ST-CON-04; derivar após freeze |
| high_severity_plan_review_issue | yes | escopo ST-CON-04; derivar após freeze |
| explicit_three_lane_request | no | escopo ST-CON-04; derivar após freeze |

## Independent No-Context Critique Gate

- **Critique decision:** required
- **Why this decision:** big/cross-stack/escrita externa scoped.
- **Impact signals in scope:** public contract/schema/api; auth; realtime; intentional module supersede
- **Package mode:** bounded-file-set
- **Package minimum contents:** TODO congelado, fontes públicas limitadas, decisões/matriz/issue cards/riscos, parecer arquitetural e resolução.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; novo agente, não executor, aguardar terminal sem prazo artificial
- **Critique lenses:** correctness,performance,elegance,structural-soundness,risk
- **Critique status:** findings_integrated
- **Findings summary:** critique r1 two finite findings integrated; fresh critique r2 reports no material planning findings and confirms all architecture/r1 dispositions at contract level. Performance mixed/unmeasured; elegance, structural soundness and operational fit acceptable for planning.
- **Resolution ledger:** machine-checkable critique dispositions below; architecture ledger retained separately
- **Evidence / reference:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/critique-r2.merge.json plus critique-r1-resolution.md and machine-checkable rows; both current raw/strict merges immutable, old reviews historical
- **Waiver authority / reference (required if waived):** n/a

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CR-R1-01 | Integrated | useful | yes | project | n/a | Uniform immutable90s dispatchDeadlineAt predicate for AMBIGUOUS and EXTERNAL_ACCEPTED_LOCAL_BLOCKED; endpoint, Scope08/DoD06/Val02 and normative r2 appendix aligned; merged F-49CD0618. |
| CR-R1-02 | Integrated | useful | partial | project | n/a | Preserve actual NOVA_CONVERSA row-creation predicate and keyword behavior; no automation on manual open; Scope01/DoD01/Val01, consumer/flow and existing admitted Typebot test scope aligned; merged F-4ACC72C3. |

## Rules Acknowledgement / Ingestion

Binding ingestion completed after current APROVADO on2026-10-22 for all10 paths below, plus execution/profile/schema/relational workflows. Implementer must reload its touched-surface sources. No rule waiver or product Git authority is inferred.

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

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Routing evidence:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/routing-implementation-v1.1.json; actual post-APROVADO implementation route GO, one routine executor serialized
- **Execution topology:** primary-checkout-single-writer
- **Subagent / delegation authorization:** repository workflow authorizes executors/reviewers; no product execution yet
- **Git isolation authorization:** not-authorized
- **Worktree authorization:** not-authorized
- **Worktree authorization reference:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

## Decision Adherence Validation

Pending implementation; not run.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

Pending implementation; not run. Every frozen decision must map one-to-one to module decision handling before delivery.

## Pipeline/Copilot P1/P2 Preflight

Pending required delivery stage; not run for planning.

## Rule-Spirit Anti-Pattern Hunt

Pending required delivery stage; not run for planning.

## Promotion Finding Routing Ledger

No promotion review exists for v1.1. Root-owned review artifacts are authoritative after freeze.

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** current planning reviews/guards converged; keep active NotStarted/Pending/review while awaiting explicit APROVADO, with no execution authority.
- **Post-commit/push status:** planning evidence publication only on Foundation main; final commit/push and clean status recorded in session, no product Git write
- **Next path/status action:** remain active/NotStarted/review; no implementation until authorized.

## Security Risk Assessment

- **Risk level:** high
- **Why this risk level:** cross-tenant first-contact external side effect, account selection, credentials and irreversible ambiguity.
- **Attack surface in scope:** session/CSRF, BU/contact/channel/template/account/attempt IDs, parameter renderer, stale contexts, payload/key/rate limits, sender-slot races.
- **Attack simulation decision:** required
- **Review evidence:** planned after implementation; no live provider/runtime query performed.
- **Residual security risk:** private existing local cohort only. Delivered SEC-R6-04 recovery-budget debt remains outside04;04 recovery does no external reads. OPS-R4-01 and TQA-ST05-03 retain their dispositions. A fresh current approved template is not presumed.

## Performance & Concurrency Risk Assessment

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
- **Trigger rationale:** listagem de conversas vazias/ordem e lookup scoped/intenção; EXPLAIN ANALYZE com amostra cardinalidade, limite de página e budget externo. Sem N+1/catalog fan-out.
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256 antes da entrega, não existe execução ainda.
#### FRC
- **Trigger rationale:** duas submissões e atraso em troca BU/canal/draft; Playwright real, rastrear requests e estado no backend.
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### BCI
- **Trigger rationale:** barreiras PG e contador HTTP externo, crash antes/depois POST, replay e echo; provar invariantes D-06/07.
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### RLS
- **Trigger rationale:** pequeno ensaio de concorrência/load bounded do novo fluxo/listagem no PG descartável; não claim SLO ou produção.
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; resolver recomendação com evidência ou waiver válido até o deadline, sem deixar pendente na entrega.

## Verification Debt Assessment

Required at closeout. Explicitly carry ST-05 `SEC-R6-04`, `OPS-R4-01`, and `TQA-ST05-03` as accepted delivered limitations unless the owning TODO changes them. No backlog fix is admitted here. Record newly found debt and owner before Completed; no claim that it was cleared by this plan.

## Independent Test Quality Audit Gate

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
- **Findings summary:** no current delivery review performed
- **Evidence / reference:** planned current implementation evidence only; prior planning artifacts historical
- **Waiver authority / reference (required if waived):** n/a

## Independent No-Context Final Review Gate

- **Final review decision:** required
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
- **Final review status:** not_run
- **Findings summary:** no current delivery review performed
- **Evidence / reference:** planned current implementation evidence only; prior planning artifacts historical
- **Waiver authority / reference (required if waived):** n/a

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** required
- **Why this decision:** intentionally replace the Channel text-only payload restriction and stored-createdAt window rule without duplicate dispatch/catalog/Message owners.
- **Cutover signals in scope:** canonical cutover; legacy-path retirement
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** planned after implementation; no current delivery review
- **Audit focus:** one abstract send operation, qualified window in every caller/projection, sole acceptance owner, zero hidden fallback
- **Cutover audit status:** not_run
- **Findings summary:** implementation has not begun
- **Resolution ledger:** delivery-stage findings will be recorded with disposition and evidence
- **Evidence / reference:** current delivered source and future implemented diff; no cutover evidence yet
- **Waiver authority / reference (required if waived):** n/a

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Not applicable to planning; future production confidence is outside current authorized scope.

## Module Consolidation Gate (Required Before `Completed`)

Pending after delivery evidence. Update inbox/channels module docs only after accepted reviews and implementation truth; no module mutation in this task.

## Commands (Run Locally)

Planning-only review/guard and Foundation main publication commands are recorded in current evidence. No product/test/runtime command was run or authorized by this planning slice. Future product commands use the declared canonical suite and approved disposable/local topology after APROVADO.

## Files Expected (Compatibility Note)

Root owns this active TODO, archive and review/evidence artifacts; the terminal draft author previously owned only the TODO. The 68-file source seal is planning evidence; no source edits are made now.

## COMENTÁRIO

Planning contract reviewed and ready for explicit human APROVADO. This status grants no execution authority; product tests/runtime/provider work remain future approved execution.

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** premissas de implementação dependem de fontes atuais.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01..08
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **Gate status:** no_material_findings
- **Findings summary:** dedicated post-review source assessment found A-01..08 coherent with exact current code; implementation, template enum and runtime health not inferred.
- **Evidence / reference:** artifacts/reviews/leadshug-start-conversation-20261022/assumption-code-observations-v1.1.md + evidence/assumption-code-source-manifest-v1.1.json; evidence/assumption-code-coherence-v1.1.json actual GO,8 live source-backed assumptions
- **Waiver authority / reference (required if waived):** n/a

## Approval

- **Approval status:** approved — APROVADO
- **Approver:** current human user/task authority
- **Approval reference:** user reply “APROVADO” on2026-10-22 after current reviewed ST-CON-04 request; evidence/approval-execution-admission-v1.1.json; reviewed Foundation fbbdfa6fd4faf3a1d4cdb62297a06e57676d9cd3
- **Approval scope:** ST-CON-04 v1.1 SCOPE-01..12 and D-01..10 including normative architecture-r1/critique-r1 contracts, strict file admission, local-only validation/activation sequence and every required delivery gate. No delivery or provider success is inferred.
- **Exclusions:** all existing Out of Scope constraints remain; no private file/data inspection, automatic real recipient actions, product Git/promotion/Railway, worktrees/auxiliary copies, unrelated debt fixes or implicit broader exposure.
- **Renewed-approval trigger:** material scope/decision/API/schema/validation change, strict path deviation, new private/public exposure or independently testable objective outside the approved journey.

## Prior-cycle provenance and sequencing handoffs

- The original 2026-10-19 planning/review record is archived by root at `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/historical-planning-20261019-20261020.md`; retain its content unmodified.
- ST-CON-06 v1.3 and ST-CON-05 v1.1 are completed locally with their own evidence and limits. Their reviews do not transfer approval to ST-CON-04.
- The old separate `GET /conversations/:id/channels/:channelId/templates` is superseded in this proposal by the one ST-05 catalog route/projector.
- The 2026-10-19 assumption-code, review, critique, and preflight outcomes remain historical only. Current v1.1 evidence is recorded gate by gate; original pending-freeze statements are authoring history, not current success evidence.

## API Endpoint Definitions — proposed ST-CON-04 v1.1

All new routes are BFF session routes, BU/conversation resolved server-side. ATENDENTE+ means current BU grant; missing session401, insufficient known BU403, inaccessible conversation/channel/attempt404. Every POST requires CSRF; strict unknown-field rejection/UUID parsing. Never accept protocol URL/token/account ID, foreign BU context or arbitrary Graph payload.

| Method / path under /api/bff | Request / effect | Safe response |
| --- | --- | --- |
| POST /business-units/:buId/conversations/open | required telefone string max40, DDI explicit; normalize only spaces/parens/hyphen/dot and optional initial +; digits8..15 firstnonzero; current local ready-channel metadata required only for new row |201 created or200 reused: {conversaId,criada,contact}; no external I/O, no read/claim/status side effect |
| GET /conversations/:id/start-options | observational local channel capabilities/readiness/window and one active attempt+up to10recent ordered by createdAt/id; separate truncated flag |200 safe channel generation/epoch/credential-version metadata and attempt IDs; no credentials, keys or external I/O |
| POST /conversations/:id/initial-message-preview | channelId UUID, expectedGeneration positive integer, mensagem typed text or template with templateId/language/catalogAfter?/expectedDefinitionFingerprint/parameters |200 rendered text and context-bound request fingerprint; local reads only, no persistence/network; stale or unsupported409 |
| POST /conversations/:id/initial-messages | same immutable message payload plus preview fingerprint; Idempotency-Key UUID; explicit selected channel, expected generation |201 new locally accepted result;200 replay terminal;202 active lease;409 blocked/conflict/ambiguous with safe attemptId/state;503 local or remote inconclusive; no recipient-delivery claim |
| GET /conversations/:id/initial-messages/:attemptId | observational scoped lookup, no browser key needed |200 safe state/provenance/local persistence/action metadata; no effects or external I/O |
| POST /conversations/:id/initial-messages/:attemptId/reconcile | empty body; same persisted attempt; current authorization, CAS |202 live lease;200 local classified/recovered state; expired PREPARED closes undispatched, expired SENDING becomes uncertain; zero external calls |
| POST /conversations/:id/initial-messages/:attemptId/acknowledge | empty body; explicit operator confirmation of duplication risk |200 irreversible slot release only for AMBIGUOUS/EXTERNAL_ACCEPTED_LOCAL_BLOCKED and DBnow >= original persisted dispatchDeadlineAt; before deadline409 ACK_TOO_EARLY + eligibleAt, no release; repeat already released idempotent; no resend/outcome rewrite |

Shared catalog continues existing GET/POST /business-units/:buId/channels/:channelId/message-template-catalog with its existing exact DTO/owner/lease/fence. No second templates route. Renderer preview never authorizes dispatch: fresh same-account eligibility and current grant/context/window are checked again for a new attempt.

**Field Definitions**
- Initial state: PREPARED (no dispatch claim), SENDING (durable claim, external result may be unknown), EXTERNAL_ACCEPTED (known external ID; local work may remain), EXTERNAL_ACCEPTED_LOCAL_BLOCKED (known acceptance, current identity/fence prevents local finalization), SUCCEEDED (Message persisted; delivery not implied), REJECTED (proven pre-dispatch or proven external refusal), AMBIGUOUS (dispatch outcome unknown).
- Slot: active while no slotReleasedAt; release is irreversible independently of outcome. One active row per conversation by partial unique index/transactionally equivalent constraint.
- Provider acceptance: CONFIRMED only with captured valid ID; otherwise UNKNOWN. receiptPersistence/localMessageState: RECORDED only after positive commit or exact readback; otherwise UNCONFIRMED. No failed DB ACK becomes REJECTED by inference.
- Content: TEXTO text1..4096; TEMPLATE reference to currently observed supported MARKETING/UTILITY, language max16 and remoteID max128, exactly matching NAMED keys or POSITIONAL1..N; maximum20 values1..1024 and rendered snapshot4096. No components outside text BODY and static TEXT header/footer.
- Channel contract: one sendMessage with text/approved-template discriminant and supportedKinds; optional generic dispatch fence is awaited once after remote preflight, directly before POST. Unsupported kind is BLOCKED/UNSUPPORTED_KIND with zero external requests. Domain receives no token/phone protocol address/raw account ID.

## Dispatch Interlock and Transaction Boundary — proposed

The new initial coordinator reserves an intent and immutable request/scope, not a Message. Common OutboundService alone resolves/binds the abstract channel and performs dispatch; common MessageAcceptanceService alone creates/reconciles keyed Message. Extend that SAME acceptance owner with an explicit tx-capable primitive, keeping its existing accept wrapper. A shared Outbound finalization collaboration consumes it for initial local acceptance/intent state/CAS effects in one short transaction, preserving the existing sender wrappers. Initial orchestration composes transport and management modules; transport never imports management, preventing a DI cycle. The Meta initial protocol client is an integration detail of the SAME bound Meta Channel, never a parallel application sender.

Before every ordinary dispatch and exclusive initial reservation, use the owner-token admission defined in the normative r1 integration below. The earlier lock-or-lease alternative is closed; no time takeover of uncertain dispatched tokens and no ordinary-versus-ordinary serialization.

For a new initial attempt, all provider preflight reads precede its SENDING claim. The same-method fence rechecks live user/grant/channel/resource/generation/epoch/active credential and payload fingerprint in the short claim transaction. A failed/expired PREPARED claim does zero POST. Positive original-claim commit/readback is the only dispatch authority. Exactly one POST per attempt; no transport mutation retry. A fresh independent credential/account/template preflight remains outside the transaction. This fence constrains local authority and cannot retract an HTTP call already accepted externally.

Only an active initial slot holder may finalize status/owner via CAS against pre-HTTP updatedAt/state/owner; explicit concurrent claim/close wins. Late accepted outcomes may add the exact original receipt/Message via same acceptance owner when current fence permits, but never reclaim a released slot, steal owner or reopen a later close. Unknown outcomes stay in the intent, not a Message without ID. Sender/echo reconciliation uses exact providerResourceIdentityId+externalID, not text/time/contact heuristics. Readback and reconcile are observational/local respectively; neither repeats provider I/O.

## Planned operational admission and proof

After explicit APROVADO and current authority GO: test-first admitted public paths only; full canonical all suite; current security/PCV/TQA/adherence assurance; disposable migration deploy/status, then one bounded local preserved TEST preflight/apply with5s lock/60s command limits, no reset/drop/resolve retry; source-bound API/Web images/runtime/static proof, preserve peers/volumes. Temporary owned HTTPS only after those gates; never adopt/kill unknown processes or require raw env/log reads. Assisted operator tests use only already designated private test channels/contacts; no automatic real send. Both unofficial first text+reply and official genuinely APPROVED template+reply are completion requirements; operator authorizes actual recipient tests at that stage. Publication/promotion of product/Railway remains excluded. Actual approval enum is currently unknown, and current runtime health has not been reprobed. Existing SEC-R6-04/OPS-R4-01/TQA-ST05-03 remain bounded, not fixed or generalized here.

## Normative architecture r1 integration — exact bounded contracts

This section is part of SCOPE-02/04/06/07/08/09/10 and D-03/05/06/07/10; it resolves ARCH-R1-01..04 and overrides earlier open-ended interlock alternatives, never the private boundary. These are proposed contract changes awaiting human APROVADO.

### Ordinary admission and exclusive initial reservation

Use a small durable per-send `DispatchAdmission` record for ordinary sends, separate from initial-message intent. Fields: id/token, conversation/BU, caller kind and current attributable actor, immutable selected context, owner nonce, `PREPARED|SENDING|SETTLED|UNCERTAIN`, deadline and irreversible releasedAt. This record authorizes exclusion only; it is not ordinary-send idempotency, retry, Message acceptance, provider lookup or a second operation owner. Every BFF/public/BOT dispatch obtains its own token under the SAME conversation row lock used by initial-slot reservation. Existing ordinary tokens can coexist; ordinary-versus-ordinary concurrency and response mappings remain unchanged. Any unreleased ordinary token blocks initial reservation; active initial slot blocks admission of a new ordinary send. Initial and ordinary admissions never pass each other through a SELECT race.

Ordinary PREPARED admission has 90s deadline; bounded provider preflight completes before a same-operation fence validates current owner/context/applicable trusted window and positively commits SENDING. If expiry wins while still PREPARED, classify/release as undispatched and fence produces zero POST. No automatically released dispatched token: SENDING expiry, process death, timeout or missing provider ID becomes UNCERTAIN and still blocks INITIAL reservation. Known accepted/refused/blocked result settles only that owner's token; unknown result keeps the token while existing caller outcome/diagnostic behavior remains unchanged. No automatic retry or provider recovery is added. All normal finally/catch release uses token+owner CAS; a late release never releases an initial slot or another owner's token.

A small local-only recovery surface exists solely to unblock initial admission: `GET start-options` adds up to10 active ordinary admissions plus truncated flag; `POST /conversations/:id/dispatch-admissions/:admissionId/reconcile` locally closes expired PREPARED or classifies expired SENDING, and `POST .../acknowledge` irreversibly releases only UNCERTAIN after its 90s dispatch deadline, current ATENDENTE+ and CSRF, with explicit duplicate-risk confirmation/audit. Never expose service principals/foreign state. Acknowledgment cannot cancel an already-claimed HTTP request; suspension after the fence or late response can still cause an external effect, which is the stated risk, not a guarantee. It never retries or changes ordinary response/Message. Known result can subsequently settle only its original token; release remains irreversible. Initial reservation seeing active token returns BLOCKED/ORDINARY_SEND_IN_PROGRESS409 with authorized local token IDs; missing/unconfirmed admission or SENDING commit means zero POST. Exact captured-key readback, no inference of rollback from an exception, applies to reserve/claim/settle/release. Local readback inconclusive keeps exclusion conservative.

Admission rows live in the same short conversation transaction as exclusive-slot checks, but never hold DB locks over HTTP. Rate limits and active-token read bounds apply; bounded row/index queries only. Preserve caller compatibility outside this narrowly reviewed admission change. Tests prove both orderings, multiple ordinary sends remain concurrent, suspension before/after fence, PREPARED expiry vs late fence, uncertain dispatch without time takeover, manual risk release, successor and late owner-CAS release. This finite recovery is included here, not delegated to an unspecified future interlock.

### Initial resolution and dispatch descriptor

Add narrow abstract `resolveForInitial` reference to ChannelResolver: current conversation/BU, explicit selected channel, expected immutable channel/resource/generation/epoch/credential-version/account-reference context and message kind. Resolve explicit channel, never infer latest origin or fallback. Approved-template resolution does not apply the free-text window; text resolution and final claim do. Existing ordinary resolver methods preserve current semantics except the explicitly superseded qualified window rule.

Initial coordinator composes transport and management and gives common dispatch an immutable descriptor containing normalized recipient from the stored conversation, complete scoped channel context, payload kind, exact template ID/name/language/category/format/canonical text components and ordered/keyed parameter values, rendered snapshot and request fingerprint. Validated management context MUST equal selected transport context in BU, channel, resource identity, opaque account reference, generation, pairing epoch and active credential version. Browser provides neither account/protocol address nor a credential. Keep transport independent of management DI. Fresh exact same-account definition/status verification completes first; generic same-send fence then verifies current user/grant, full context equality, immutable payload fingerprint, slot/owner/deadline and applicable trusted text-window at claim time, immediately before one POST. Window expiry during preflight rejects text before dispatch; closed-window approved template remains allowed. External status can change after check; provider refusal is not converted to success/fallback/retry.

### Transaction ordering and local recovery

Keep the known external receipt committed separately before local Message work. Reuse `MessageAcceptanceService.acceptInTransaction` (proposed name) as SAME owner primitive; current `accept` remains wrapper with its existing observable behavior. Initial short local completion obtains current verified-identity lock first, BU/contact advisory lock where required, then conversation row lock, then intent/admission rows in that order; no reverse acquisition in new collaborators. Under that row lock evaluate ORIGINAL pre-HTTP updatedAt/status/owner + active initial-slot CAS BEFORE acceptance's own lastMessageAt/updatedAt mutation. Capture the boolean; do not refresh expected values from a newer/echo-first conversation. A false status/owner CAS skips those effects but does not reject an otherwise eligible keyed Message. Same owner accepts/reconciles exact resource+external ID, and same transaction records initial completion and slot release. Echo-first may conservatively suppress assignment/reopen; never steal/reopen on a newly captured baseline.

Unique conflict aborts the entire local transaction. Do not query/reconcile inside an aborted transaction. After rollback, exact positive readback of receipt/Message/intent then at most ONE fresh whole-local transaction may reconcile through the same primitive and original CAS context; no external call. Commit-ACK loss first uses exact readback; if still unconfirmed, keep truthful CONFIRMED external acceptance, UNCONFIRMED local projection and unreleased slot. Local-only later reconcile can resume after current identity/grant checks. Old wrapper's acceptance/error/unknown mapping stays covered. Realtime emits only for the Message creation winner after confirmed local commit; crash-gap remains best-effort (no outbox claim).

### Initial template subset over unchanged ST-05 catalogue

The delivered `supported`, `eligible` and `semanticFingerprint` fields describe ST-05 authoring support and mark POSITIONAL unsupported. They are preserved byte/semantics-compatible and are NOT authorization or complete initial-send support flags. New initial text renderer consumes existing sanitized `TemplateSummary.components`, `parameterFormat`, account-bound observation freshness/availability/status and exact ID/name/language/category. It validates its own strictly narrower text-send grammar: one BODY, max one static TEXT HEADER and FOOTER, no other/unknown component, no placeholder in header/footer; NAMED unique keys or POSITIONAL contiguous keys1..N with repeated occurrences mapped consistently. Every supplied value must exactly match the required names/positions and existing bounds. Unknown/unsupported syntax fails closed. This renderer is not a second catalogue/projector and writes no remote observation.

Derive an initial-only semantic fingerprint from a fixed canonical versioned representation of the existing sanitized ID/name/language/category/parameterFormat/text components, then combine context, recipient and ordered/keyed values into preview/request fingerprint. Do not reuse null ST-05 positional fingerprint or silently treat eligible=false as send permission. Initial UI labels subset support based on this same renderer/preview, not inherited authoring flags. Fresh bounded same-account reads pass through the SAME renderer and must exactly match selected initial semantics and APPROVED status before POST. No shared parser/DTO/authoring change admitted. If actual raw semantics cannot be represented unambiguously by sanitized components, reject that template rather than broaden parser scope. End-to-end POSITIONAL and NAMED catalog→preview→fresh-check→wire-order tests are required.

## Normative critique r1 integration — acknowledgment and automation

**Initial deadline:** reserve PREPARED with leaseExpiresAt = reservation DB timestamp +90s. The successful original SENDING claim persists dispatchDeadlineAt equal to that same leaseExpiresAt; never extend or reset either timestamp during replay/read/reconcile/failure classification. All preflight and claim must fit before expiry. This original deadline governs initial risk acknowledgment; it does not promise remote cancellation.

For a never-released initial attempt, acknowledgment requires current authorization/CSRF, classified AMBIGUOUS or EXTERNAL_ACCEPTED_LOCAL_BLOCKED, captured non-null dispatchDeadlineAt and database time at/after it. This uniform timing applies even to a confirmed external acceptance blocked locally: no earlier exception. Before it, return409 ACK_TOO_EARLY with safe eligibleAt and leave slot/outcome unchanged. Unknown transaction/readback never supplies release authority. After it, explicit duplication-risk confirmation may irreversibly release; a request paused after claim may still produce a late external effect, so this is knowingly accepted risk, never a cancellation guarantee. Repeat acknowledgment on a previously released attempt is idempotent; late improvement of that attempt cannot reclaim its slot or alter successor state. Reconcile before deadline does not expire a live SENDING claim; an explicit transport timeout may already classify AMBIGUOUS but still cannot be acknowledged early. Cases at deadline-1ms, equality, +1ms, PREPARED with no claim, active SENDING, both classified states, lost release ACK, successor and late original response must be tested.

**Automation preservation:** current IncomingService calls NOVA_CONVERSA with acceptance.conversationCreated, not 'first inbound ever'. Manual open creates the row without any bot/provider side effect. A later first inbound into that manually opened empty row therefore does not fire NOVA_CONVERSA, even if the seller abandoned the draft. Keep that delivered predicate; no new first-inbound semantic, automation execution on open or trigger migration is admitted. Keyword automation retains its current matching predicate. Add focused real-PG/domain integration fixtures: open-without-send then first inbound with only NOVA_CONVERSA configured produces no bot start; the corresponding keyword trigger still matches. Browser validates open/readback without automation. No production automation behavior change beyond the explicit consequence of manually creating the conversation.

## Planning execution-readiness preflight — 2026-10-22

- **Authority pre-approval:** actual `preflight-go`, evidence/authority-preapproval-v1.1.json, execution_authority_granted=false. Normal authority GO requires actual human APROVADO and binding ingestion; it has not run for04.
- **Current planning review chain:** architecture-r1 four integrated; critique-r1 two integrated; fresh affected critique-r2 no material findings; immutable raw/strict merges and current resolution rows retained.
- **Source/assumption coherence:** dedicated post-review semantic assessment A-01..08 and exact source manifest; deterministic guard GO. Real account template approval/runtime remain unknown future dependencies.
- **Review scope:** canonical23-section comparison to a107a6ab pushed freeze gives zero material changes, GO. Temporary Git adapter only translates canonical git.exe path/case output for Python guard; no methodology/guard semantics or product change.
- **Preservation:**68 inherited public source records + supplemental acceptance owner match their seals;3 product HEADs unchanged. No env/private/runtime/business/provider query, test run, product Git or deployment in this planning turn.
- **Future execution:** test-first + full canonical runner, actual PG/real BFF/browser, candidate assurance and only then bounded preserved local migration/source-bound runtime/operator-assisted own-contact proof. Actual APPROVED official asset remains a completion dependency; baseline802 are prior05 evidence only.
- **Required binding sources:** the10 concrete rules/workflows named in Rules Acknowledgement / Ingestion, including TODO Approval Gates, NestJS application boundary, React UI boundary, Prisma migration, PostgreSQL integrity and performance/concurrency methods. Reload after approval; no inferred authority from advisory reviewers.

## Execution admission checkpoint E01 — 2026-10-22

Operational/Coder active for NestJS/React/Vite/PostgreSQL/Prisma/Docker, Genesis rejected (existing reviewed canonical package). verify_context: PACED-Ready exit0. All10 binding rule sources and execution/profile/schema/relational methods reloaded. Current post-approval route: routine-executor/gpt-6-luna/medium, GO; principal-checkout-single-writer, no worktree authority. Initial69 public-source seals and3 productHEADs match; current root/api/web branch feature/number-onboarding. Raw secrets, private storage, process args/env/logs and business data excluded. No persistent tool GOAL is created absent explicit human request; bounded executor objective is documented here.

Next implementation checkpoint: causal RED for manual contact/open, initial renderer and qualified window; then same-owner transport/admission/intent lifecycle, real-PG/barrier/commit certainty and UI proof. Root owns this TODO and review/evidence; delegated executor alone owns admitted product changes. Any runtime/test namespace operation uses the canonical public-only disposable runner; preserved local/provider proof follows candidate gates only. No product code was changed before normal authority GO.

## Execution checkpoint E02 — discovery deviation and containment

The delegated executor reported an initial broad `find .. -name AGENTS.md -print`, despite the approved positive-public-path restriction. The wrapper printed an empty output while losing terminal/session metadata; exact traversal and termination outcome are unknown. No private path/content was returned or used. Root prohibited further broad discovery and checked process name only (`pgrep -x find`, exit1/no PID); no live find remained, no process arguments/env/logs or private surface were inspected for remediation. This is a procedural deviation, not proof of privacy compliance; it must be included in independent security/adherence/final packages. Evidence: evidence/execution-discovery-deviation-e02-v1.1.json. Subsequent public implementation/testing remains authorized under the unchanged strict boundary. No inferred credential exposure, runtime/credential change or user data query is performed.

Exact Node/Prisma/React/Vite dependency/script evidence was collected from the four explicit public package/lockfile paths. Recursive node_capability_surface_audit CLI was intentionally not invoked because it traverses before applying --manifest and does not exclude .local-files. Evidence/positive-node-capability-v1.1.json records declared and locked versions, scripts, method and this limitation; it is not a claimed recursive-helper PASS.

## Execution checkpoint E03 — initial causal RED

Delegated canonical API runner returned exit1 after reaching Vitest: the three newly admitted service spec suites could not import their absent implementation modules;26 existing suites/284 tests passed. This is module-loading RED for a new feature, not assertion-level behavior RED. Disposable cleanup was observed by the executor. Receipt: evidence/executor-red-e03-v1.1.json; full synthetic validation stdout remains at the designated temporary path with its hash, not copied into source/evidence as actual-runtime logs. A later compile error in the first implementation attempt (TS2339 union narrowing in initial renderer) was recorded before further correction; no GREEN claim is made. Boundary/order assertion cases were then added before behavioral fixes, with a second canonical RED run in progress. All04 DoD/VAL remain unchecked.

## Execution checkpoint E04 — test causality and pending phase1 GREEN

Actual sequence remains explicit: initial module-loading RED (no service files); first implementation build failed TS2339 before tests; narrow compile-only corrections preceded a true assertion RED3 (2 renderer failures,298 tests passed). Some additional edge cases were completed after preliminary behavior corrections. The executor then temporarily restored pre-fix methods and ran RED4:6 assertion failures/297 tests passed in2 suites,27 passed suites. RED4 is controlled post-hoc causal/reversion evidence, NEVER retrospective test-first proof. It isolated raw phone41-char valid-digit+allowed-space overflow, control-whitespace trimming, reverse/repeated positional binding, blank BODY with static header and raw component-order display. Correct behavior was reapplied before a new canonical API GREEN run. Current unit open/reuse test mocks upsert and is not real-PG/create-vs-reuse/race evidence. No Scope/DoD/VAL is marked complete by this checkpoint; exact PG, authorization/readiness and real-browser evidence remain required. TQA must assess the actual mixed causality, not a rewritten timeline.

## Execution checkpoint E05 — bounded phase1 canonical API GREEN

Canonical API runner59939 exited0 after lint/build, disposable migration deploy/status,29 unit files/303 tests and30 PostgreSQL E2E files/398 tests; namespace cleanup completed. The synthetic stdout hash was independently rechecked against the delegated receipt. Evidence: evidence/executor-phase1-green-e05-v1.1.json. This proves the six new helper/service/spec files coexist with the inherited API baseline; it does not prove the full new journey. Open/reuse is still mock-based, and the trusted-window helpers are not wired to persistence or consumers. E04 mixed causality and E02 discovery deviation remain unchanged. All Scope/DoD/VAL delivery items remain pending. The same sole product executor is continuing the already approved backend integration: additive schema, trusted timestamp consumers, atomic open, abstract dispatch, admission/intent durability, BFF and real-PG fault/race proof. No second writer, product Git, preserved-runtime, provider or tunnel operation is authorized by this checkpoint.

## Execution checkpoint E06 — trusted timestamp persistence substep

Executor reported canonical API runner34233 terminal exit0: lint/build,29 unit files/303 tests,30 PostgreSQL E2E files/399 tests, disposable deploy/status and owned cleanup. New signed-webhook case verifies valid Meta time persisted and missing/malformed/future values accepted with null provenance. This is post-wiring verification, not historical test-first RED; stdout was not saved and no stdout hash or independent transcript inspection is claimed. Evidence: evidence/executor-timestamp-e06-v1.1.json. Root public-source review identified missing bounded transaction/timeouts and Prisma-vs-SQL timestamp native-type mismatch in the new candidate migration; executor will correct before the next candidate run. Deploy/status alone is not schema parity proof. Current-resource strict window queries/consumers remain pending. No full04/migration-parity/browser/provider/preserved-runtime delivery claim; E02/E04 disclosures remain applicable.

## Execution checkpoint E07 — exact inherited read-only source recheck

Root hashed only the positively named inherited public files under current exact “NO new mutation” rows: all matched. Evidence: evidence/readonly-source-recheck-e07-v1.2.json. The first v1.1 recheck incorrectly used historical planning active_mutation_admitted=false as current admission authority and therefore selected all68 records; four differences are explicitly approved ST04 mutable paths, not deviations. v1.2 fixes classification against the authoritative TODO without erasing raw observations or changing scope. This is a narrow source-preservation check, not a full diff guard/delivery proof. No private discovery or runtime operation was used.

## Execution checkpoint E08 — strict window exposes synthetic fixture drift

Canonical runner83187 exited1:29 unit files/303 tests passed;25 PostgreSQL E2E files passed,5 failed;384 E2E tests passed/16 failed. Root independently verified the synthetic stdout hash and bounded failure summary. New current-resource/missing-date policy case passed. Existing positive-send fixtures omit qualified Meta time/current identity and now fail closed; no createdAt fallback, global test middleware or Prisma backfill/interception will be introduced. Two affected fixtures are exact inherited read-only paths (number-onboarding-pcv and number-onboarding-typebot); a minimal exact proposal must receive the TODO-required user deviation validation before mutation. Existing admitted tests can align synthetic signed/current-resource inputs. Source review confirms new migration now has bounded transaction/timeouts and TIMESTAMP(3); executor reports policy consolidation after terminal runner, not yet GREEN. Evidence: evidence/window-regression-e08-v1.1.json. No full delivery or retrospective test-first claim.

## Execution checkpoint E09 — manual open real-PG target passes, full API RED

Runner31732 exited1 with lint/build and29 unit files/304 tests passed;25 E2E files passed/6 failed,385 tests passed/17 failed. New BFF/PostgreSQL manual-open cases passed: empty QUEUED creation, immutable reuse after readiness loss, and10 same-contact concurrent requests yielding one201/nine200 with one row and no Message/send. Current-resource window test passed. Root verified synthetic stdout hash. Evidence: evidence/manual-open-e09-v1.1.json. Full RED remains16 inherited date-fixture failures plus new-route history catalog coverage. The exact catalogo.ts/cobertura.ts paths are already admitted; bounded route/audit coverage needs no further user permission. Two sealed fixture edits still await actual user validation. Small-pool/floor concurrency, full ACL/automation/sort/browser and initial-send durability proof remain outstanding; root flagged outside-tx metadata queries under advisory lock for correction/proof. Actual open/window tests followed implementation, not historical assertion RED. Remaining interlock/intent/transport production work must capture new target fail-first before implementation; unrelated regression RED does not substitute.

## Execution checkpoint E10 — transport RED review corrected invalid expectations

Runner86380 exited1 in unit phase:28 files passed/2 failed; actual synthetic stdout304 tests passed/4 failed (delegated306 corrected); no E2E. Root verified hash. Capability assertions observed missing supportedKinds, but later Evolution zero-send assertion was not reached. Two Meta expectations were contract-invalid: routing a template object through sealed legacy MetaClient.enviarTexto and changing ordinary text recipient formatting. Root rejected these before transport production changes; initial-only same-bound-Meta protocol tests must replace them, then capture actual valid RED. An unrelated open unit had brittle query-count expectation. The executor-owned new test was temporarily created at unadmitted integrations/channels/channel-initial-message.spec.ts; root classified location as noise to relocate after terminal runner to admitted domain/channels/transport/channel-initial-message.spec.ts, not new scope/user permission. Evidence: evidence/transport-red-e10-v1.1.json. No claim that all failing tests prove approved behavior; chronology retained for TQA/adherence.

## Execution checkpoint E11 — corrected admitted transport causal RED

After E10 terminal, executor relocated its new spec to admitted domain/channels/transport/channel-initial-message.spec.ts and corrected the initial protocol fixture with captured account and a staged preflight→fence→POST fake. Runner97310 intermediate RED retained; runner85250 corrected RED exited1 with29 files passed/1 failed,305 tests passed/3 failed. Actual failures: Evolution unsupported template invokes legacy send; Meta template/initial text fail to use the new injected initial client. This is causal assertion RED before transport production edits. Later WABA/fence/capability/result assertions were not reached and are not claimed proven. Both stdout transcripts actually show successful generate/migrate/lint/build before unit; delegated “no lint/build” prose corrected. Root rechecked hashes. Evidence: evidence/transport-valid-red-e11-v1.1.json. Bounded positive-public API untracked inventory now classifies all41 names under approved paths (separate narrow precheck artifact; not full diff/readonly/delivery guard). No full journey, admission or provider eligibility proof yet.

## Execution checkpoint E12 — transport candidate requires raw-protocol corrections

After valid causal RED, transport union/capabilities and additive Meta initial protocol candidate were written. Runner78537 failed one unit fixture missing required durable callback (307 pass/1 fail reported); fixture corrected and runner66596 active at review. Root source review identified TR-01..06: both initial wire payloads must pin captured messaging account; composed current-context+late claim fence/full tuple equality; typed descriptor; contradictory/refusal response certainty; generic ordinary hook; preclaim config and finite I/O proof. These are approved-contract corrections, no new scope. Evidence: evidence/transport-candidate-observations-e12-v1.1.json. Fake-client factory tests cannot prove raw protocol details; direct protocol specs are required before any transport GREEN claim. Existing per-attempt MetaTemplateClient grantPromise reuse is correct. No full04 or independent assurance claim.

## Execution checkpoint E13 — union unit passes; new BCI HTTP failure remains separate

Runner66596 exited1: generate/deploy/status/lint/build passed;30 unit files/308 tests passed;25 E2E files passed/6 failed,388 E2E tests passed/17 failed. Root verified hash/failure summary. Five known inherited suites still need timestamp/current-resource fixture alignment. Sixth is NEW manual-open20×5 stress with ECONNRESET, not inherited fixture drift; no BCI pass is claimed. Proposed diagnosis is Supertest implicit listener lifecycle; explicit owned loopback listener on the new admitted test fixture must be verified without reducing load/assertions. New manual-open automation cases passed (no NOVA_CONVERSA after manual row, keyword retained). Root TR01..06 raw-protocol corrections/direct tests remain required despite factory unit pass. Two exact protected fixture edits await actual user validation; other admitted fixtures and own harness can be corrected now. Evidence: evidence/transport-unit-and-bci-e13-v1.1.json.

## Execution checkpoint E14 — direct protocol unit and manual-open concurrency pass

Runner81812 exited1: lint/build/generate/deploy/status passed;30 unit files/311 tests passed;29 PG files passed/2 failed,399 tests passed/6 failed. Root independently verified synthetic stdout hash and terminal owned cleanup. Remaining failures are exactly the two protected fixture companions (PCV1, Typebot5), still awaiting actual human validation. The new20×5 open test now passes with5 created/95 reused/one row per contact and zero provider calls; owned explicit HTTP listener correction preserved stress/assertions. Three direct raw-protocol tests now pass, but were added alongside corrections and have no historical causal pre-fix RED; intermediate lint failure35934 and invalid synthetic grant fixture62998 are retained. After terminal, missing-field webhook coverage and template capability routing were corrected; this run does not validate those later edits. Evidence: evidence/transport-and-open-e14-v1.1.json. Overall API RED remains; full tuple equality,75s I/O budget, durable admission/intent, SQL plans, UI/browser and final assurance remain pending. A new dispatch-admission module-loading RED is being captured separately; no admission behavior implementation precedes it.

## Execution checkpoint E15 — durable admission module-loading RED

Runner65756 exited1 after generate/deploy/status/lint/build passed:30 unit files/311 tests passed; one new dispatch-admission suite could not load its absent service. No admission assertions or PG ran; root verified stdout hash and owned cleanup. This is causal module-loading RED before production admission changes, not behavioral/concurrency proof. Prior62370 failed TS18048 in optional Meta callback narrowing before tests and does not count as admission RED. Sequential owner-token fake will be labeled accurately; real PG overlap/ordering/CAS/commit uncertainty and scoped recovery remain mandatory. Evidence: evidence/dispatch-admission-red-e15-v1.1.json. Sole executor continues approved durable admission/schema/integration under unchanged scope; no protected companion edit is inferred authorized.

## Execution checkpoint E16 — admission candidate review and owned path correction

The first admission candidate adds finite ordinary tokens and initial intents with a shared conversation-row lock, partial unique initial slot, original nonce and lease. This is incomplete scaffolding, not delivery. Executor initially placed its owned migration outside api-app; it relocated it into the already admitted20261022150000_initial_message_admissions path and removed only its exact staging noise. Root verified the current public SQL; no user scope expansion or private discovery is inferred. Review required pre-captured IDs/exact commit readback, DB time after lock, schema/index naming parity, order-independent JSONB comparison, consistent return typing and late known owner settlement preserving an earlier risk release/successor. Corrections and real-PG/fault evidence remain pending. Evidence: evidence/admission-candidate-review-e16-v1.1.json. This procedural path noise joins E10 for independent adherence; E02 remains separately disclosed.

## Execution checkpoint E17 — partial admission candidate and remaining proof

Runner68010 exited1 after generate/deploy/status/lint/build:30 unit files passed/one failed,318 tests passed/two failed. Seven new admission assertions passed; two owned fake setups retained a hardcoded ID or omitted the root intent-readback delegate. Root verified stdout hash and owned cleanup. This is partial unit evidence only; no PG admission or schema drift/parity claim. Executor corrected the fakes, added a DB-time recheck after awaited validator plus SQL-clock expiry CAS, and added post-implementation real-PG interlock/deadline cases before runner51922. Current service remains unintegrated with ordinary sender and full initial coordinator/recovery/UI. Evidence: evidence/admission-candidate-e17-v1.1.json. Final diff-guard compatibility assessment (evidence/final-diff-guard-private-boundary-assessment-v1.1.json) records an unresolved required-method conflict: default helper performs root-wide untracked discovery without positive pathspec/private-prune support; it has NOT run and no GO/waiver is inferred. Independent authorized implementation continues while final-method resolution remains pending.

## Execution checkpoint E18 — active validation freeze deviation

Executor confirmed product/spec edits occurred while runner51922 was active, contrary to the explicit frozen-candidate rule. Snapshot exercised is unknown; this run is diagnostic only and cannot establish candidate GREEN. Root earlier observation of320 unit passes applies to the earlier mutable snapshot, not the later lock-order/claimInitial changes. Executor stopped writes; only owner polling/terminal receipt/cleanup continues, with no duplicate runner. After terminal, fix the owned PG missing import and notifier-after-held-gate deadlock, capture exact public source hashes, then rerun canonically and recheck source after terminal. Evidence: evidence/validation-freeze-deviation-e18-v1.1.json. This evidence-quality deviation must remain in independent TQA/adherence/final review; it does not rewrite E02 or authorize private inspection. User was informed of the invalidated-round/retest correction.

## Execution checkpoint E19 — exact protected source preservation

Root rehashed only the38 positively named inherited read-only public paths from corrected E07v1.2: all match the original seals, including both pending fixture companions. Evidence: evidence/readonly-source-recheck-e19-v1.1.json. This is neither a full inventory/diff guard nor candidate freshness proof; runner51922 remains non-authoritative under E18. No private traversal/metadata/read was used.

## Execution checkpoint E20 — terminal diagnostic and corrected outbound RED contract

Invalidated51922 exited1:320 unit pass;399 PG pass/11 fail, exactly5 admission fixture-setup failures,1 PCV and5 Typebot (root verified transcript hash/cleanup). Candidate remains non-authoritative under E18. After terminal, import and held-gate notifier fixed. New outbound tests then ran in61864: delegated320 pass/two fail, no saved stdout/hash and root does not claim transcript verification; earlier “redirected capture” launch prose was wrong. Root250positivepublic-file capture taken during bootstrap (after launch, not prelaunch) matches all exact bytes/inventory after terminal before edits. The second RED case had an invalid expectation (successful claim followed by releasePrepared); root rejected it before production wiring. Corrected safe unclaimed/uncertain/refusal cases run under captured50255 before ordinary sender integration. Evidence: evidence/validation-chronology-e20-v1.1.json and runner61864-public-source-capture/recheck-v1.1.json. No full admission/PG/initial journey pass.

## Execution checkpoint E21 — valid ordinary-send integration causal RED

Runner50255 exited1:30 unit files passed/one failed,320 tests passed/two failed; no PG. Root verified synthetic stdout hash and cleanup. Corrected preflight-block test reaches expected409 then releasePrepared assertion fails with0calls: valid causal missing-integration RED before production wiring. Ordering fake detects absent generic callback and old sender maps UNKNOWN, so later full trace is not reached; this is bounded missing-hook evidence, not proof of all later assertions. Combined uncertain/refusal assertions were not reached. Executor split cases/recorded unfenced acceptance for clearer trace in subsequent42918; no further RED solely for presentation is required once current valid target failure is observed. Evidence: evidence/outbound-causal-red-e21-v1.1.json. Full admission/initial journey remains pending.

## Execution checkpoint E22 — four-case ordinary sender causal RED

Runner42918 exited1:30 unit files passed/one failed,320 tests passed/four failed; no PG. Root verified stdout hash/cleanup. All four split target tests reach their own assertions: missing reserve/final claim gives preflight/unfenced-post, preflight block has no reserved-owner release, UNKNOWN lacks UNCERTAIN settlement, confirmed refusal lacks SETTLED settlement. This is valid assertion-level RED before ordinary sender production integration. Evidence: evidence/outbound-valid-red-e22-v1.1.json. Sole executor now continues the approved full backend; no additional RED merely to change presentation is needed. Admission PG/barriers, original claim/commit certainty, full coordinator/receipt/atomic local completion, recovery, BFF, UI/browser and final assurance remain required.
