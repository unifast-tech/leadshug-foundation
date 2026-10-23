# ST-CON-04 v1.1 implementation review candidate

This is a fresh no-context internal challenge package. Do not call tools or edit files. Assess this bounded evidence and the exact approved intent. Return only the dispatch-required JSON. Findings first by severity; no package access outside the embedded material is required. Source is frozen from the principal checkout. This fresh r2 round evaluates the complete corrected candidate and original r1 resolutions; it has no inherited chat context. Prior reviews are challenge evidence, not approval authority.

Stage: implementation candidate, delivery Pending. The complete implementation is being evaluated for readiness to request a separately bounded preserved-local activation; no actual new runtime/operator proof or final delivery is claimed. DOD11/12/13 and full canonical diff-guard remain pending. Identify those as explicit follow-up gates; do not invent a completion claim. Product defects, missing producer/consumer implementation or insufficient implementation proof are material findings even at this stage.

Approved: user APROVADO; subsequent exact Typebot/PCV test fixture adjustments validated; own template reported APPROVED by human, not remote verified. Public roots only; no actual .env, .local-files, process/env/log or business-row inspection. The canonical recursive capability helper and full diff guard cannot silently cross that boundary. No product Git writes/worktree/provider routing or automated contact.

Chronology is mixed and must be judged honestly: E03 was absent-module RED; E04 included actual renderer RED plus a separately disclosed post-hoc reversion diagnostic, never retroactive test-first. E11 valid union RED, E21/22 ordinary dispatch RED, E25 coordinator module RED, E35 real-BFF/browser missing-first-flow assertion RED, E41 actual UI/uncertainty defects, E44 exact snapshot-read data-loss assertion RED before E45 UI fix. Most later fault/protocol/boundary tests were alongside/post-implementation. No causal proof is claimed for an assertion not reached. Explicit qualification: E03/E15/E25 absent-module RED is not business assertion RED; E04 reversion is post-hoc. E50 actual PG/BFF projection/interlock/COUNT/settlement/realtime assertions and E51 positional Unicode snapshot assertion precede the r1 product fixes. E48/E49 test-support failures are not product RED. Detailed exact chronology and fresh corrected full-all proof are embedded. E18 editing during an old live run invalidated that old candidate; source-freeze and full independent inventory/byte postseals govern current evidence. E02 broad discovery and E35a .gitmodules read deviations are preserved, not hidden behind full-compliance language.

Inherited constraints SEC-R6-04 (ST05 recovery-budget debt), OPS-R4-01 and TQA-ST05-03 remain assigned to their prior scopes; no future work is implemented here. The already-approved initial-send union and trusted-IN window deliberately supersede prior ST06 text-only/createdAt behavior; ST05 authoring payload/flags remain sealed and independent. Public/BOT preserve existing diagnostic/error semantics; they do not gain global idempotency. One POST per captured initial attempt is the claim, never end-to-end external exactly-once.

Evidence boundaries: real disposable PostgreSQL, actual BFF/session/CSRF and fresh served React browser. External provider is an owned fake. Port invocation counters are not provider TCP request counts. Full preserved runtime/source/image/migration and human own-channel first-send/reply tests are later required gates.

The repository baseline includes inherited uncommitted ST05/ST06 sources. Exact inherited hashes precede ST04 changes; 38 protected/exact-companion records remain equal. Git HEAD alone does not identify those dirty bytes. Current source hashes and original seals bind the candidate. A Git-baseline aggregate diff must not be misrepresented as an isolated ST04 patch; full current relevant source plus explicit initial-seal change classification is embedded here.

Current source fingerprint: `604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c`, 259 complete positive public records.

## Exact approved governing contract excerpts

## Context

ST-CON-06 entregou o transporte abstrato textual, adapters Meta/Evolution, resolução scoped e um `OutboundService` compartilhado; ST-CON-05 entregou autoria/submissão e o catálogo/projetor compartilhado de templates. Ambos permanecem contratos entregues e evidência de dependência, não aprovação desta história. A inbox ainda não permite iniciar atendimento manual por contato e conduzir o primeiro envio oficial de modo recuperável.

Este v1.1 substitui a autoridade ativa da minuta revisada em 2026-10-19. O original e suas decisões/reviews são preservados pelo owner do pacote como `historical-planning-20261019-20261020.md`; nada daquele ciclo é evidência de revisão, guard, aprovação ou execução deste texto. Os handoffs de ST-CON-06 e ST-CON-05 continuam como contexto factual.

**Perfil desta etapa:** Strategic / CTO-Tech-Lead; escopo ativo NestJS, React, Vite, PostgreSQL, Prisma e Docker. Genesis foi rejeitado: o projeto canônico já existe. Próximo handoff planejado: Operational / Coder após contrato congelado, reviews/guards atuais e aprovação humana explícita. Supporting profiles: Assurance / Tester-Quality, Assurance / Security-Adversarial e Operational / DevOps para os respectivos gates. Seleção declarada conforme `delphi-ai/workflows/docker/profile-selection-method.md`.


## Contract Boundary

- Este TODO define **WHAT** será entregue; `Assumptions Preview` e `Execution Plan` registram a proposta **HOW** para revisão.
- O escopo é fechado ao início manual e primeiro envio de uma conversa. Qualquer alteração material de Scope, DoD, validação, contrato público ou decisões requer retorno à revisão e nova aprovação antes de execução.
- “Aceito” significa ID externo válido persistido; não significa entrega ao aparelho nem leitura.
- Baseline inicial publicado antes dos primeiros guards/review; parecer arquitetural r1 integrado abaixo. Mudanças materiais decorrentes do parecer serão publicadas em novo freeze antes da crítica. Nenhuma implementação ou aprovação humana é reivindicada.


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
| api | test/number-onboarding-pcv.e2e-spec.ts | M | Human-validated E23 bounded test-only synthetic signed timestamp/current-resource alignment and corresponding trusted-window EXPLAIN per window-fixture-companion-admission-v1.1.patch; all other baseline bytes/scenarios/counters preserved |
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
| api | test/number-onboarding-typebot.e2e-spec.ts | M | Human-validated E23 bounded test-only synthetic signed timestamp/current-resource alignment and corresponding trusted-window EXPLAIN per window-fixture-companion-admission-v1.1.patch; all other baseline bytes/scenarios/counters preserved |
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


## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/inbox-and-conversations.md`
- **Secondary module docs:** `foundation_documentation/modules/integrations-and-channels.md`; completed ST-CON-05 owner TODO reference (no new template module).
- **Planned decision promotion targets:** inbox module first-send/open/recovery and trusted-window sections; integrations module Channel payload/capability and scoped resolver section.
- **Module decision consolidation targets:** same sections only after implementation and reviews; no module docs edited in this planning slice.


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


## Security Risk Assessment

- **Risk level:** high
- **Why this risk level:** cross-tenant first-contact external side effect, account selection, credentials and irreversible ambiguity.
- **Attack surface in scope:** session/CSRF, BU/contact/channel/template/account/attempt IDs, parameter renderer, stale contexts, payload/key/rate limits, sender-slot races.
- **Attack simulation decision:** required
- **Review evidence:** actual high-risk negative synthetic scenarios passed full E54; current map evidence/security-candidate-map-e54-v1.1.json. Fresh independent challenge pending; no live provider/runtime query performed.
- **Residual security risk:** private existing local cohort only. Delivered SEC-R6-04 recovery-budget debt remains outside04;04 recovery does no external reads. OPS-R4-01 and TQA-ST05-03 retain their dispositions. A fresh current approved template is not presumed.


## Performance & Concurrency Risk Assessment

- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** escrita externa e concorrência com webhook e UI.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | running | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | running | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-E3 | running | external ambiguity explicit | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E1 | running | none | none |

### Lane Detail Packet Template
#### EPS
- **Trigger rationale:** listagem de conversas vazias/ordem e lookup scoped/intenção; EXPLAIN ANALYZE com amostra cardinalidade, limite de página e budget externo. Sem N+1/catalog fan-out.
- **Recorded at (UTC):** 2026-10-22T23:00:47.612421+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-eps-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `08138da3019c4a4269e82701d38732f84fcd7ae0476c37127e84257b7c868ab5`; sample EPS-SP-STRONG; acceptance EPS-A2. Independent assessment pending; no delivery/runtime/provider claim.

#### FRC
- **Trigger rationale:** duas submissões e atraso em troca BU/canal/draft; Playwright real, rastrear requests e estado no backend.
- **Recorded at (UTC):** 2026-10-22T23:00:47.620028+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-frc-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `994c5487144cd1be2301b4099b0c7d05af4f88aa5955b9441e5b9910736f0e4a`; sample FRC-SP-H; acceptance FRC-A1. Independent assessment pending; no delivery/runtime/provider claim.

#### BCI
- **Trigger rationale:** barreiras PG e contador HTTP externo, crash antes/depois POST, replay e echo; provar invariantes D-06/07.
- **Recorded at (UTC):** 2026-10-22T23:00:47.626397+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-bci-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `c505c53965ac7a15999d0f91915e75dac1fac6e9c3a0fca6694a3078f54aa5f2`; sample BCI-SP-H; acceptance BCI-A1. Independent assessment pending; no delivery/runtime/provider claim.

#### RLS
- **Trigger rationale:** pequeno ensaio de concorrência/load bounded do novo fluxo/listagem no PG descartável; não claim SLO ou produção.
- **Recorded at (UTC):** 2026-10-22T23:00:47.632810+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-rls-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `25f71eadd5ac094b794fbf1ffb694a49d3031791486f4cb473537d08698c7fb8`; sample RLS-SP-L; acceptance RLS-A1. Independent assessment pending; no delivery/runtime/provider claim.


## Verification Debt Assessment

Required at closeout. Explicitly carry ST-05 `SEC-R6-04`, `OPS-R4-01`, and `TQA-ST05-03` as accepted delivered limitations unless the owning TODO changes them. No backlog fix is admitted here. Record newly found debt and owner before Completed; no claim that it was cleared by this plan.


## Approval

- **Approval status:** approved — APROVADO
- **Approver:** current human user/task authority
- **Approval reference:** user reply “APROVADO” on2026-10-22 after current reviewed ST-CON-04 request; evidence/approval-execution-admission-v1.1.json; reviewed Foundation fbbdfa6fd4faf3a1d4cdb62297a06e57676d9cd3
- **Approval scope:** ST-CON-04 v1.1 SCOPE-01..12 and D-01..10 including normative architecture-r1/critique-r1 contracts, strict file admission, local-only validation/activation sequence and every required delivery gate. Supplemental human validation E23 admits ONLY the two exact test fixture adjustments in window-fixture-companion-admission-v1.1.patch (SHA c35143d98838f25e7b44eafd24085ca5dd08b8869985120c6125a14359f07957), reply “Validar os dois ajustes de teste”. No delivery or provider success is inferred.
- **Exclusions:** all existing Out of Scope constraints remain; no private file/data inspection, automatic real recipient actions, product Git/promotion/Railway, worktrees/auxiliary copies, unrelated debt fixes or implicit broader exposure.
- **Renewed-approval trigger:** material scope/decision/API/schema/validation change, strict path deviation, new private/public exposure or independently testable objective outside the approved journey.


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



## Canonical module baseline before planned consolidation: foundation_documentation/modules/inbox-and-conversations.md

SHA256 `24b3f1edd8f10bf991d61135be2364b49679c43e5894ce024c2d5169921756a2`. Historical ST05/ST06 rules are preserved; two explicit ST04 supersedes are approved. Module consolidation is pending, not a production divergence waiver.

# Module: Inbox and Conversations
**Version:** 1.0

Owns contacts, conversations, messages, inbox, assignment and service responses across official and unofficial
WhatsApp transports.

## Invariants

- A conversation is unique by BU and contact, not by transport.
- Incoming webhook processing is idempotent.
- Outbound responses enforce the platform window and channel capability.

## API Endpoint Definitions

BFF routes use `/api/bff`; public integrations use `/api/v1`; webhook contracts use `/webhooks`.

## Contrato aprovado da timeline da inbox

Aprovado pelo usuário em 2026-10-14 no [TODO ST-ATT-01](../todos/completed/features/TODO-leadshug-inbox-message-timeline-pagination.md). Este módulo é o owner do contrato; implementação e verificação são registradas no TODO. Estado de verificação: **Verified local**, em2026-10-15. API115unit/224E2E, Web20unit/36browser e FRC3 passaram em Node22/PG16 descartável com fontes/build servido conferidos. Aderência e TQA independentes convergiram; [evidência e limites](../artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md). Final review aceito e guardas de entrega go; commits locais APIae6a9662c29b77276351aa9de653a47276372246 e Web4e56f6c1f4515b918d05b8c87e890d42e8542c56 têm os16 blobs conferidos no [bridge de fonte](../artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/committed-source-attestation.json). Entrega local, sem promoção operacional ou Production-Ready.

### Thread paginada BFF v1 — GET /api/bff/conversations/:id/messages

- Sessão e grant ATENDENTE ou superior na BU; resolver/autorizar a conversa antes de validar ou consultar cursores. Sem sessão: 401. Recurso fora do escopo: 404, inclusive com query/cursor malformado.
- Query: `limite` inteiro decimal 1..100, padrão 50; `antes` cursor opaco opcional, máximo 256 caracteres; `marcarLida` booleano textual `true|false` opcional.
- Sem `antes`, `marcarLida` ausente equivale a true para conservar abertura humana. Cliente usa explicitamente false para refresh, pós-ação, poll, reconexão e recuperação. Com `antes`, leitura é sempre false; `marcarLida=true` explícito com `antes` é inválido. Valores inválidos, query repetida/array e cursor inexistente/alheio à conversa autorizada: 400 `PAGINACAO_INVALIDA`; query desconhecida é ignorada e não altera comportamento.
- A marcação de abertura é uma única atualização atômica de `unreadCount=0`, depois da autorização e antes de buscar a página. Essa escrita é a fronteira de reconhecimento: incrementos de entrada serializados depois dela permanecem não lidos. Não fazer select-depois-reset nem adicionar estado de leitura por mensagem. Se abertura/marcação falhar, não executar uma escrita posterior compensatória que apague entradas novas.
- Resposta conserva `conversa`, `janela` e `messages` e acrescenta `paginacao: { limite, temAnteriores, cursorAnterior }`.
- Sem cursor, buscar as últimas N mensagens. Responder páginas em ordem crescente pelo par `(createdAt,id)`; ordenação de ID segue a comparação do banco.
- Cursor versionado identifica a mensagem-âncora; resolver seus dados somente na conversa autorizada. Paginação anterior usa comparação estrita do par, busca no máximo N+1 registros e nunca escreve não lidas.
- `cursorAnterior` representa o registro mais antigo da página quando há continuação; caso contrário null. Vazio: messages vazio, temAnteriores false, cursor null.
- API pública e Consultar mantêm seus contratos e efeitos atuais. Dublês no backend de testes substituem somente portas externas; não há flag de teste no código de produção.

### Recuperação e estado da inbox

- Manter somente a coleção da conversa ativa por ID; liberar contexto/páginas quando BU/conversa mudar. O cursor histórico pertence ao backfill e não é substituído pelo cursor da página recente de um refresh.
- Na atualização, capturar uma fronteira fixa T igual ao timestamp da mensagem mais recente conhecida antes da passagem. Buscar página recente sem marcar leitura e caminhar para trás até alcançar timestamp estritamente menor que T, ou esgotar mensagens. Incluir integralmente o grupo empatado em T; encontrar um ID conhecido não encerra a recuperação.
- Se a coleção ainda é vazia, atualização funciona como página inicial sem efeito de leitura. Separar o piso de cobertura confirmado do maior timestamp mesclado. A recuperação captura um piso pendente T e toda passagem coalescida/retomada/retry conserva esse piso original, mesmo quando a cabeça já avançou para H maior que T.
- Evento durante a recuperação marca uma nova passagem necessária desde a página recente, ainda com o piso pendente T; terminar a caminhada atual não confirma cobertura. Só promover o piso confirmado quando uma passagem atravessar todo T sem evento/trabalho concorrente pendente. Se houver dirty/pending, conservar T e a indicação de atualização, com o mesmo orçamento de três queries por rodada. Não promover pelo máximo da coleção nem por um poll enquanto houver recuperação pendente.
- A recuperação cobre inserções novas, incluindo ID menor em T atrás de um cursor já percorrido. Importação/backdating de histórico fora do grupo de cobertura permanece fora deste recorte. Mensagens mais recentes mescladas não eliminam essa prova de continuidade.
- Recuperação tem cursor/progresso próprios e uma única passagem em voo por contexto. Cada rodada executa no máximo três queries de página, separadas e bounded; uma rodada incompleta mantém indicação visível de atualização/lacuna e cursor para `Continuar atualização`/retry. Novo evento não reinicia seu orçamento; polling pode retomar a rodada pendente. Não afirmar continuidade até cruzar toda a fronteira.
- Disparadores: evento de mensagem coalescido, socket restabelecido sem depender de outro evento, pós-ação e poll da thread selecionada a cada 60 segundos. Registrar callback de conexão no helper existente; preservar seus consumidores.
- Backfill altera somente coleção e cursor histórico. Metadados conversa/janela só são aplicados pela leitura atual com versão/frescor adequado; uma página anterior atrasada não desfaz close, troca de status ou atualização de janela.
- Todo efeito assíncrono captura BU/conversa/geração. Resposta, erro, scroll e limpeza do texto enviado são ignorados se contexto mudou; limpeza de draft também verifica que o usuário não digitou outro texto enquanto o envio estava pendente.
- Histórico anterior preserva posição do usuário. Mensagens novas não forçam deslocamento quando ele lê trecho antigo. Estados de loading, vazio, fim, recuperação pendente, falha/retry e acesso perdido são visíveis e operáveis por teclado.

### Decisões verificadas e limites locais

- Acesso por cursor permanece limitado à conversa autorizada; reconhecimento atômico precede a página e leituras de fundo são neutras.
- A coleção pertence somente à conversa ativa. Recuperação conserva T e o restart pendente, com no máximo3tentativas por rodada inclusive falhas; evento não renova saldo. Continue/poll autorizam retomada.
- Notificações durante abertura/recuperação vazia são conservadas. Respostas, erros, rascunho, metadados e scroll respeitam geração; a limpeza do erro verifica sua versão/owner.
- O EXPLAIN recente/profundo/empates e trial de índice não justificaram migration; o predicado profundo ainda filtra linhas mais recentes. Medições locais não estabelecem SLO/capacidade de produção.
- API pública, Consultar, transporte/providers, transferência, estados de mensagens e mídia mantêm os contratos e escopos próprios.


## Aceitação de mensagens e automação — ST-CON-01

APROVADO em2026-10-15; implementação exercitada localmente em2026-10-16 ([all499/22migrações e fonte/freshness](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp27-receipt.json)); architecture/security, Performance/cutover e TQA independentes aceitos no escopo local. Final review local aceito; source commits/bridge byteexact registrados, prova externa local dos dois canais concluída CP106-108; encerramento local concluído CP108 no TODO, sem alterar o contrato de timeline verificado acima. Owner inbox-and-conversations; identidade externa e pareamento pertencem a [canais](integrations-and-channels.md#cadastro-de-números-st-con-01). Execução no [TODO](../todos/completed/features/TODO-leadshug-channel-connection-readiness.md).

Entrada aceita exige externalMessageId não vazio e chave única PostgreSQL (providerResourceIdentityId,externalMessageId); identidade já incorpora provider. Mesmo ID em recursos diferentes não colide. `Message` legado pode manter FK/chave nulas; não inventar IDs nem apagar duplicatas históricas. Só backfill inequivocamente comprovado é admitido. Novas entradas sem ID ficam rejeitadas com erro seguro antes de efeito de domínio. Após identidade validada, transação curta aceita Message e cria/reusa conversa BU/contato com incremento unread; conflito de unique desfaz os efeitos daquela tentativa. Somente a transação vencedora publica realtime e aciona automação. Echo OUT e resultado do sender compartilham a mesma aceitação transacional por identidade/ID, inclusive quando o echo chega primeiro; não criam outra Message, IN ou unread. Contrato detalhado abaixo. Replay sequencial/concorrente retorna sucesso idempotente para evento já aceito. Não se promete exactly-once externo: crash depois do commit pode deixar publicação/automação ausente; não repetir bot automaticamente nem introduzir plataforma de jobs/outbox neste recorte. Essa limitação precisa constar do runbook.

IncomingService deriva Mantenedora da BU verificada. Busca de trigger exige bot.mantenedoraId desse tenant e buId exata OU trigger global dentro do MESMO tenant. Sessão retomada deve pertencer à mesma Mantenedora/BU/contato; sessão estrangeira falha fechado antes de texto externo. Criação deriva owner do contexto verificado, não de um bot arbitrário. Dois tenants com triggers globais concorrentes não compartilham bot, texto, sessão, saída ou credencial. São defeitos preexistentes na superfície tocada, cuja correção fica expressamente incluída para sustentar o recebimento deste cadastro.

Um serviço de aceitação de mensagem no domínio inbox é o owner da chave (providerResourceIdentityId,externalMessageId) para TODAS as novas gravações com ID: entrada, eco OUT, resultado de envio BFF/público e Typebot. Sender captura a identidade do canal autenticado, faz HTTP fora de transação e depois cria-ou-reconcilia pelo mesmo índice PostgreSQL. Sender-first, echo-first e ecos concorrentes devolvem o MESMO Message.id; conflito de unique não pode virar segundo registro nulo nem erro de inserção depois do envio bem sucedido. Validar owner BU/conversa/contato/direção na reconciliação; incompatibilidade é erro/quarentena de identidade, sem sobrescrever outro recurso. Registro local sem externalId confirmado conserva pendência/erro explícitos, sem inventar ID, retry externo ou garantia de deduplicação por ID inexistente.

Eco primeiro cria OUT sem autoria humana inventada; resultado interno enriquece o mesmo registro com conteúdo/autoria humana ou Typebot comprovados pelo caller. Eco posterior não apaga/substitui essa autoria e não muda createdAt/ID. Só criação vencedora emite evento de nova mensagem; enriquecimento preserva a identidade e usa refresh/projeção existente, sem novo IN, unread ou bot. Retorno BFF/público mantém seus contratos e contém o registro reconciliado. Invariantes de janela, permissão, conversa BU/contato, ordenação e timeline permanecem. Nenhum cache de ecos em memória ou lookup-antes-insert substitui o índice/transação. Continua explícito o limite de crash depois do commit e antes da publicação; não há claim exactly-once externo.

A verificação final de mapping/epoch deve ser sincronizada à gravação de conteúdo, incluindo webhook em voo atravessando RENEW/remove-recreate. A projeção existente após refresh mostra o mesmo ID enriquecido; se exigir diff hoje excluído, registrar a falha antes de admitir mudança de escopo. Não há autorização para Nova conversa manual, importação, sequenciamento de bot para mensagens distintas, worker ou outbox.


## Channel abstrato e envio comum — ST-CON-06

Contrato v1.3 aprovado e exercitado localmente: all93791 passou613testes, revisões independentes de aderência/segurança/cutover/TQA e Performance convergiram, com uma dívida baixa explícita de precisão de métrica de teste. O operador confirmou nova IN e resposta OUT nos vínculos oficial e não oficial após ativação das imagens atuais; a proveniência fonte→imagem→container→HTTP foi conferida antes e depois. A revisão final e os guards de closeout são registrados no [TODO governante](../todos/completed/features/TODO-leadshug-channel-abstraction.md). Evidências: [validação automatizada](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/v13r4-final-validation.json), [ativação](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-activation-provenance-v13r4-final.json), [prova assistida](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-operator-proof-v13r4.json) e [proveniência posterior](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/post-operator-readback-v13r4.json). Não é prova de produção, disponibilidade contínua ou redes futuras.

BFF, partner public API and Typebot consume one OutboundService. Trusted BFF human/public EXTERNO/bot source intent is established before dispatch. MessageAcceptanceService remains the sole keyed writer for provider-ID Messages and sender/echo convergence. Human/public completion conditionally updates the current owner, preserves a newer concurrent claim and sets IN_SERVICE except existing group behavior. Bot retains queue/status/human owner/unread semantics and stops without replay after uncertain or blocked output.

Human/public responses use the deterministic latest message origin ordered by createdAt DESC,id DESC. An unavailable selected origin is not replaced by another connected channel. Without history, only a sole binding can be selected; zero and multiple bindings have explicit absent/ambiguous errors. Bot responses remain pinned to their accepted verified ingress even if another channel becomes the latest origin. The selected binding's free-text-window requirement applies to all senders before every text. Existing latest-IN stored timestamp without transport filtering is preserved and must be revisited in ST-CON-04.

ST-CON-04 first-send, if separately approved, consumes the shared template catalogue owned by [Integrations and Channels — ST-CON-05](integrations-and-channels.md). Before every first-send it independently revalidates that the selected template is currently eligible (`APPROVED`, observation at most 300 seconds old) for the current selected account/channel context and rechecks the existing send policy. It adds no template authoring/catalogue, sender, or route here. ST-CON-04 remains unimplemented and requires its own TODO and approval.

Availability is safe local metadata, separate from authorization and dispatch revalidation. BFF thread adds disponivel/motivo; public list/thread adds envio_disponivel/motivo_indisponibilidade. Batched public availability reads BU bindings/credential metadata at most once per page and latest-IN only for references whose actually selected binding requires a window, without decrypting secrets or calling providers. The managed Message index `(conversation_id,direction,created_at,id)` supports direction-constrained latest-IN lookup, including OUT-heavy/no-IN histories and equal-time ID ordering; it does not change the historical timestamp rule or imply a production capacity/SLO. The public list loads parent metadata with one-row lookahead, slices the returned page, then reads latest-any-message metadata in one parameterized batch restricted to those returned IDs. Direction-constrained top-one IN/OUT probes use the approved index and choose the larger createdAt/id tuple from at most2candidates per parent, preserving null message/direction for an empty history. This is separate from the selected-window latest-IN projection and never hydrates full histories. Public list and message-thread pagination normalize the optional limit before Prisma: maximum500, defaults200/list and100/thread for absent, blank, non-string/repeated, nonfinite, nonpositive or sub-one-after-floor values; finite positive fractions are floored. The list may fetch one additional row solely to report truncado, then projects availability for at most500 returned conversations. These bounds were exercised by request-level PostgreSQL regression cases and all93791; measured emitted rows must remain distinct from general scan/filter/recheck work (PERF-R4-01). Existing thread read-marker behavior is retained; only the availability projection is observational. No new route, user-supplied provider selection or Message DTO status field is introduced.

Inbox shows fixed truthful explanations, disables unavailable sends, retains draft on uncertainty/local incomplete/error, and never automatically resends. Monotonic BU/conversation generations fence late completions, including A→B→A with a newly edited identical draft. Composer duplicate triggers are dropped while a send is in flight.

Contrato de campos e erros: [canais e envio comum](integrations-and-channels.md#channel-abstrato-e-envio-comum--st-con-06).


## Canonical module baseline before planned consolidation: foundation_documentation/modules/integrations-and-channels.md

SHA256 `6b1865ab4f27458e1e1e225535e2f4a713e987e18344ca86d3f9411fa6c6f168`. Historical ST05/ST06 rules are preserved; two explicit ST04 supersedes are approved. Module consolidation is pending, not a production divergence waiver.

# Module: Integrations and Channels
**Version:** 1.0

Owns Meta Cloud API, Evolution/Baileys, outbound webhooks, API keys and transport adapters.

## Invariants

- Providers are adapters; business workflows do not depend on provider payload shape.
- Secrets never enter logs, docs, fixtures or client bundles.
- Provider failures become deterministic application errors.


## Cadastro de números ST-CON-01

Contrato aprovado pelo usuário em2026-10-15 no [TODO governante](../todos/completed/features/TODO-leadshug-channel-connection-readiness.md), documentação publicada3302964c. Estado: **Approved; implementação exercitada localmente em2026-10-16 ([all499/22migrações e fonte/freshness](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp27-receipt.json)); architecture/security, Performance/cutover e TQA independentes aceitos no escopo local. Final review local aceito; source commits/bridge byteexact registrados, prova externa dos dois canais concluída CP106-108; encerramento local concluído CP108 no TODO**. Owner: integrations-and-channels, escopo Mantenedora/BU; mantém constituição e políticas de isolamento. O módulo é autoridade do contrato; o TODO registra execução/evidência. Fonte API em api-app; Web em web-app.

### Disposição do complemento técnico de teste (CP84)

O [complemento ST-CON-01-TESTAUTH](../todos/active/features/TODO-leadshug-meta-api-test-number-binding.md) foi **Cancelled por decisão humana em 2026-10-18**, antes de qualquer implementação de produto. A entrada técnica por token privado do Test Number não integra o contrato entregue deste módulo. Seu planejamento/diagnósticos permanecem históricos; retoma-se ST-CON-01 por Embedded Signup; primeira prova oficial de recebimento passou em cp106 e recuperação com nova troca física passou em cp107-108. Inscrição ausente foi descoberta relatada pelo operador e corrige a premissa anterior; acesso/elegibilidade, callback e roteamento devem ser conferidos no contexto atual. Nenhum suporte de standby/handover é declarado ou implementado por esta disposição.

### BFF e autorização

Contexto do provedor conferido em2026-10-19: no [modelo atual da Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/), WhatsApp account (WAAC) representa o telefone; Messaging account contém templates, billing e inscrições de webhook. Na fase atual, o WABA ID existente identifica a Messaging account e os phoneNumberIds/APIs continuam compatíveis. O [onboarding padrão](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/onboarding/) cria uma Messaging account por parceiro e permite compartilhar um telefone já registrado com outro parceiro. Duas Messaging accounts no mesmo telefone ou ausência de templates de outro parceiro não comprovam erro do vínculo. Conferir autorização, associação do recurso e inscrição efetivas, além do roteamento no contexto atual. Registro do mesmo telefone e seleção da conta antiga são operações distintas; elegibilidade precisa ser observada na resposta real da Meta.

IDs/endpoints próprios de WAAC e transições obrigatórias futuras não são tratados como APIs disponíveis nesta entrega. O [parâmetro messaging_account_id](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/messaging/) deve ser avaliado quando a credencial tem acesso de envio a mais de uma Messaging account no mesmo telefone; não é causa presumida de falta de entrada nem autorização para mudança antecipada de schema/consumer. Cadastro, primeira troca oficial e retomada local passaram cp106-108; encerramento local está registrado no TODO ST-CON-01 concluído.

- `GET /api/bff/number-registrations/capabilities`: sessão válida; expõe apenas appId/configId/Graph version e disponibilidade/explicação por modalidade, nunca app secret/token/chave. Não chama provider. A modalidade oficial depende de versão Graph explícita no formato `vXX.0` e do conjunto Meta completo da instalação; valores ausentes, vazios ou malformados não anunciam disponibilidade, sem fallback de versão presumida. A configuração Meta inteira ausente mantém a administração disponível; configuração parcial é erro de implantação.
- `POST /api/bff/number-registrations`: `Idempotency-Key` UUID obrigatório, body exatamente uma origem (`buId` existente ou `novaBu:{nome,setorId?}`) e `tipo:OFICIAL|NAO_OFICIAL`, `operation:NOVO|REAUTORIZAR`; REAUTORIZAR exige BU existente, channelId e expectedGeneration. BU existente exige ADMIN nela; BU nova exige ADMIN na Mantenedora e herda grants/setor pela mesma regra transacional de TenancyService. Oficial sem app/config/crypto configurados e não oficial sem módulo contratado+teto configurado falham antes de criar BU/provider. Para NOVO, nova BU (quando pedida), reserva do canal e tentativa são atômicas no DB; REAUTORIZAR reutiliza canal conforme contrato de ativação abaixo; refatorar reuso transacional da criação existente, preservando audit e expansão dos grants. Mesmo key/payload retorna tentativa original; mesmo key e payload diferente409. Nenhum HTTP de provider dentro da transação.
- `GET /api/bff/number-registrations/:id`: apenas ADMIN da BU e tenant da tentativa; devolve etapas, número redigido conforme DTO da BU, erro safe e progresso. Nunca devolve código/PIN/token. Sem sessão401, recurso fora do escopo404, papel insuficiente403; autorizar antes de revelar erro de payload/estado.
- `POST /:id/authorize` (prefixo anterior): oficial, nonce+code recebido no callback SDK. Pertence à sessão exata/usuário da tentativa, hash da sessão/expiração/nonce checados; CAS PENDING→PROCESSING antes de trocar code. Código não persiste nem entra em URL/log/audit. Envelope candidato do token persistido na tentativa antes dos passos seguintes; nunca substitui a credencial ativa nesta etapa. Timeout de troca fica AMBIGUO e exige nova autorização; nunca reenvia code consumido automaticamente.
- `GET /:id/options`: somente depois de autorizar; retorna WABAs/números permitidos pela credencial dessa tentativa. Backend prova app/audience, escopos e pertencimento do recurso; IDs postMessage não são autoridade. Página máxima100 e continuação explícita, sem scan infinito. `options` aceita `wabaId` e cursor opaco `after` limitado a512caracteres; `confirm` admite o mesmo `after` opcional para reler somente a página selecionada. Cursor e IDs do cliente não concedem autoridade: backend revalida app/escopos, WABA permitida e presença do phoneNumberId na página retornada pelo provider para ESSA WABA, com budget3requests/10s. Cursor forjado/velho sem o recurso falha sem promoção nem mutação; não seguir URL externa indicada pelo cliente. Número escolhido sempre confirmado pelo operador; nunca escolher primeiro por conveniência.
- `POST /:id/confirm`: `wabaId,phoneNumberId,modoRegistro` validados contra provider e grant atual. Telefone obtido do provider deve coincidir com BU já numerada; se BU sem telefone, preencher por CAS na mesma transação do vínculo. A identidade externa tem proprietário durável e único por provider/recurso, inclusive após exclusão do canal; colisão ou tentativa de transferir entre BUs retorna409 sem revelar tenant alheio. Só a confirmação da mesma identidade permite promover a credencial candidata por CAS.
- `modoRegistro:NOVO` admite PIN6dígitos e passo de register explícito conforme modalidade convencional Cloud API. `modoRegistro:JA_REGISTRADO` não redefine PIN nem chama registro destrutivo; vínculo fica pendente de prova operacional quando a leitura Meta não comprovar readiness. PIN não retorna em DTO/log, só persistência cifrada se necessário à recuperação. Não realizar migração/coexistência/unregister.
- `POST /:id/advance` e `POST /:id/retry`: uma rodada tem no máximo3requests externos, cada um timeout10s e um único lease de45s por vínculo; persistir estágio/resultado após cada passo. Não há retry automático de mutação ambígua. Read-before-retry reconcilia estágio; se não houver operação segura, declarar pendente/reautorizar em vez de fingir exactly-once externo. Assinar WABA só depois de mapping channel↔providerID local durável; webhook pode chegar antes do fim sem perder o tenant correto. Configurar callback apenas da própria instalação/conta de teste, sem override alheio.
- `POST /:id/cancel`: antes de side effect externo pode encerrar reserva; depois conserva vínculo/etapas parciais e informa limpeza necessária. Não apagar BU nem conversas, não fazer unsubscribe de WABA compartilhada automaticamente. Consumidores atuais exigem credencial e readiness do vínculo antes do OUT.
- `POST /api/bff/business-units/:buId/channels/:tipo/verify`: ADMIN, um lease por vínculo, mesmo budget3×10s; listagem nunca faz fan-out. Resultado muda só a dimensão efetivamente observada. Erros externos mapeados para códigos de catálogo, sem texto/token/URL brutos.
- `POST /api/bff/business-units/:buId/channels/nao-oficial/pair` inicia/renova pairing com intent INITIAL ou RENEW, sessão ADMIN, anti-CSRF, lease e geração atual. O antigo GET de QR retorna405 sem chamar Evolution nem iniciar/renovar conexão; nenhuma mutação de provider em GET. Resposta contém QR efêmero só ao admin; o QR nunca é persistido em eventos/audit. Nova UI não usa o POST antigo que conecta WABA pelo token global. Rota antiga deve recusar fluxo incompleto com instrução do contrato novo, sem fallback de token; atualizar seus testes de expectativa dentro do escopo.

A verificação administrativa de um número oficial já vinculado revalida app, escopos e WABA da credencial ativa uma vez; procura o ID exato em no máximo duas páginas de números, sem seguir URLs de continuação. O limite total é uma consulta de grant e duas páginas, cada request com timeout10s sob lease45s. O confirm do cadastro continua relendo somente a página escolhida pelo operador. Ausência só é conclusiva quando uma lista estruturalmente válida se esgota; JSON inválido, data ausente/não-array, linha inválida, paginação inconsistente, continuação além do limite, ciclo ou cursor inválido mantêm a observação anterior e devolve503/codeMETA_INDISPONIVEL com mensagem fixa segura. O serviço traduz apenas a falha Meta reconhecida, preserva erros de autorização/concorrência e libera o próprio lease; não expõe erro bruto nem promove status por consulta inconclusiva. O reparo cp36g valida também a estrutura do grant antes de iterar os escopos/alvos e usa a interseção completa de autorização para verificar o número persistido; o limite100 permanece na apresentação de opções. A validação corrente cp36j passou 174 testes unitários e 288 E2E PostgreSQL pelo runner canônico. Web28/browser47 são evidências cp36h reaproveitadas por fontes consumidoras idênticas, sem alegar novo browser ou all537. Os testes diretos de grant revogado e app_id estrangeiro, com os demais campos válidos, foram aceitos no TQA completo e na revisão final independente j. A imagem servida continua i: somente o teste excluído do build mudou, com ponte explícita de bytes/compilados, sem novo build ou rótulo j. A retomada automática não oficial e a troca posterior real estão comprovadas cp49/cp52; a nova conversa foi de outro contato e o histórico anterior foi preservado. A primeira troca oficial IN/OUT e o recebimento foram comprovados em cp106, com readback canônico CONECTADO/identidade verificada/SUBSCRIBED/receipt confirmado; recuperação oficial foi comprovada por restart permitido da API e nova IN/OUT cp107-108. O baseline histórico cp60 ainda não tinha receipt; cp106 o confirmou na BU Local Test Ofc. CP107 retomou a API e preservou os estados; CP108 confirmou nova troca física após interrupção. Entrega geral Pending e restrição privada de dependências preservadas.

### Persistência e recuperação

`ChannelRegistrationAttempt` guarda id, Mantenedora/BU/canal, tipo, userId, hash de sessão, nonce hash, idempotencyKey+requestHash, estado, versão, leaseUntil, expiresAt, stage e erro safe. Unique Mantenedora/idempotencyKey e slot BuChannel(buId,type) já existente. IDs externos únicos por tipo; migrations detectam conflito preexistente antes de impor constraint. IDs internos podem ser prealocados sem compromisso de provider.

`ChannelCredential` mantém token/PIN em envelope com keyId/version/nonce/ciphertext/tag, ligado ao canal da BU e geração; não inventar vault genérico nem refletir o envelope no model público. AAD inclui provider/BU/channelID/generation. Tamper/decrypt/key ausente falha fechado, nunca fallback global. Passar credencial por interface de adapter, sem vazá-la a audit ou payload de domínio. Não copiar secrets do ambiente legado.

Cadastro pode ficar `PENDING_AUTH`, `PENDING_NUMBER`, `REGISTERING`, `PENDING_RECEIPT`, `CONNECTED`, `ERROR`, `CANCELLED`, com dimensão de providerConnection/receipt/credential e timestamps. O enum físico e mapeamento para status atual devem ser explícitos na migração; nenhum label mágico na UI. `CONNECTED` exige etapas aplicáveis concluídas, identidade correta e conexão confirmada; oficial já registrado sem endpoint conclusivo não recebe falso CONNECTED só pela lista de números. Primeira IN autenticada pode comprovar recebimento, não validade permanente do token de saída. Teste IN/OUT externo certifica somente a execução observada, não saúde contínua.

Reconexão e verificação administrativa repetida devem convergir de forma idempotente quando a tentativa corrente da mesma geração e do marcador de pareamento aplicável já está `CONNECTED`/`RECEIPT_VERIFIED`. No canal oficial, a tentativa conserva `pairingEpoch=null`, pois não há pareamento QR; no não oficial, exige o epoch numérico exato da rodada corrente. Essa aplicabilidade vem da modalidade confiável do canal, sem aceitar null como alternativa genérica para Evolution. Repetir essa observação não promove novamente nem incrementa a versão da tentativa; receipt e identidade existentes permanecem. Tentativa cancelada, etapa incompatível ou geração/epoch divergente falha fechada e não restaura estado do canal. A aceitação continua condicionada aos locks, owner, vínculo corrente e receipt; estado persistido durante indisponibilidade é a última observação, não garantia de saúde contínua.

Reserva idempotente da instância Evolution usa nome derivado de channelId+pairingEpoch persistida, estável durante retries desse epoch; nunca nome do operador+timestamp. Nova rodada de pareamento usa identidade externa distinta, conforme contrato de confiança abaixo. Se create retorna timeout, consultar a mesma identidade antes de retry; nenhuma segunda instância. Webhook deve ser configurado e verificado antes de concluir. Leitura de estado e evento usam geração e versionamento; retry de geração anterior não escreve após remove/recreate. Desconectar não apaga histórico. Callback tardio de instância sem vínculo não cria BU/tenant.

A tentativa expira em10min enquanto espera autorização. Após credencial ativa promovida, operações de recuperação do canal são administrativas e reautorizam grant/sessão corrente; não reaproveitam code/nonce antigos. Lease expirado não é sucesso e requer reconciliação; nenhuma transação DB é mantida durante rede. Não criar worker global ou sistema genérico de jobs neste slice.

### UI e integrações

Wizard: nome/BU → modalidade → janela Meta ou QR → confirmar número → mostrar cadastro/recebimento e ação de retry quando parcial. Cancelar popup, trocar BU, desmontar tela ou nova tentativa invalida callbacks/efeitos antigos no cliente; backend ainda revalida scope. A UI não consome mensagens postMessage para autorização ou seleção; somente o callback do SDK correlacionado à operação atual inicia a troca do code. IDs externos são obtidos e confirmados pelas leituras autorizadas no backend. Callback de login fica preso à geração/attempt/nonce corrente; prova server-side da credencial/ID é obrigatória.

Permissões existentes preservadas: ADMIN da BU para conectar existente; ADMIN da Mantenedora para criar BU; ATENDENTE não ganha gestão; módulo não oficial depende do teto e contratação. Dados sensíveis nunca vão a config.js/bundle. UI mostra ausência de configuração e falhas por etapa, sem exigir WABA/token manual do operador comum no fluxo Meta. Administrador pode reautorizar conta já cadastrada; credencial manual de número já registrado, se usada, é caminho técnico explícito com conferência Meta e cifra, jamais env global implícita.

BFF responder e API pública responder preservam DTOs/janelas. Typebot preserva o comportamento dentro da mesma Mantenedora, com seleção e sessão obrigatoriamente isoladas pelo tenant da BU verificada. A entrada acrescenta identidade verificada e deduplicação transacional; credenciais são resolvidas por vínculo em todos os consumers. DI deve convergir nos módulos BFF/público/webhook. Primeira IN cria/reusa conversa pelo contrato existente, não manual. Nova conversa por contato aguardará ST-CON-04.

### Reautorização e ativação da credencial (NUM-ARCH-06)

Criar tentativa distingue `operation:NOVO|REAUTORIZAR`. NOVO reserva slot vazio; REAUTORIZAR recebe channelId e expectedGeneration e reutiliza o slot existente, inclusive canal migrado sem credencial. Valida ADMIN/tenant antes do estado; conflito de geração409. A nova tentativa torna-se currentAttemptId por CAS, sem mudar a credencial ativa. Reserva anterior expirada/cancelada sem efeito externo pode ser substituída, preservando BU; com efeito parcial, recuperar a mesma identidade externa, sem criar segunda instância.

Cada nova autorização depois de code consumido, expirado ou troca ambígua exige tentativa e nonce novos; não há reapresentação automática do code. `ChannelRegistrationAttempt` mantém envelope candidato separado de `ChannelCredential` ativa. AAD candidato inclui propósito, attemptId, provider, BU, channelId e geração; AAD ativo inclui propósito e versão ativa. Após validação server-side de identidade/escopos e confirmação do mesmo número, uma transação curta verifica currentAttemptId+generation+activeCredentialVersion e promove o envelope, recifrando para AAD ativo. Candidata de outro número, sessão revogada ou tentativa velha não pode substituir a ativa. Credencial utilizável anterior segue em uso até promoção; se já inválida, mostrar PENDENTE_CREDENCIAL, sem fallback global. Cancelar/expirar elimina o segredo candidato, conserva somente metadados seguros e mantém a ativa.

### Confiança do pareamento e reconciliação OUT (NUM-CRIT-01/02)

Antes de INITIAL/RENEW produzir qualquer efeito externo, transação curta reserva pairingEpoch monotônica, limpa ownNumberVerified/verifiedEpoch e invalida leases/observações antigas por CAS. Cada novo pareamento lógico tem nome externo derivado de channelId+epoch, imutável nessa rodada; retry/renovação de QR pendente reutiliza a MESMA tentativa/epoch/instância, sem criar outra. RENEW de um canal antes verificado é novo epoch, não mera leitura de QR. Evento ou verificação pendente do epoch anterior nunca restaura confiança. Instância antiga fica aposentada no mapping durável; callback antigo só permite metadados seguros, nunca conteúdo/receipt/estado do canal atual.

O desenho escolhe identidade de instância específica do epoch, sem depender de o payload carregar uma geração local. Só observações da instância EXATA da rodada atual podem participar da confirmação. `open`/wuid isolados não reabilitam conteúdo: etapa administrativa bounded consulta identidade própria dessa instância nova no provider, valida resposta/ownPhone e grava verifiedEpoch por CAS contra currentAttemptId+pairingEpoch+generation. O cadastro/criação/configuração precede essa consulta; não aceitar resposta de outra instância nem confiar no nome informado pelo operador. Se o provider fixado não oferecer prova inequívoca da identidade da instância nova, manter PENDING_IDENTITY e bloquear a prova externa. Telefone vazio da BU só é preenchido com identidade comprovada por CAS, assim como no oficial; divergente permanece quarentena.

Antes de criar outra instância externa, reconciliar criação/aposentadoria/limpeza da instância anterior própria; timeout é ambíguo e exige read-before-retry. Ação RENEW informa ao administrador que inicia novo pareamento e interrompe aceitação até confirmação. Limpeza só atua em instância criada por este LeadsHug e com ownership comprovado; nenhuma adoção/remoção de instância legada. Mesmos budgets/leases, nenhuma transação sobre HTTP, worker ou buffer novo. Aposentar mapping ocorre antes da rede, independentemente de a limpeza externa terminar. Eventos sem a nova identidade ficam rejeitados conforme503/409 já definidos, sem promessa de replay.

Concretização física do mesmo contrato após revisão de implementação: backfill de nome externo conserva owner da BU, mas não comprova gestão do runtime por esta instalação. A evidência da reserva/criação própria deve ser durável e distinta desse backfill; verify/cleanup nunca deduzem essa autoridade só do nome mapeado. O tombstone/attempt retido mantém resultado e fence de limpeza mesmo após unlink do canal, sem perder ambiguidades. Etapa reservada ainda não criada distingue-se de create ambíguo, permitindo criar exatamente a substituta já reservada depois de limpar antecessora própria. Essas são condições dos limites já aprovados, sem adoção de legado ou sistema genérico de jobs. Promoções e remoções usam ordem consistente de locks e CAS verificado até commit; a fixação do telefone da BU valida o valor canônico atual dentro da mesma transação.

Um serviço de aceitação de mensagem no domínio inbox é o owner da chave (providerResourceIdentityId,externalMessageId) para TODAS as novas gravações com ID: entrada, eco OUT, resultado de envio BFF/público e Typebot. Sender captura a identidade do canal autenticado, faz HTTP fora de transação e depois cria-ou-reconcilia pelo mesmo índice PostgreSQL. Sender-first, echo-first e ecos concorrentes devolvem o MESMO Message.id; conflito de unique não pode virar segundo registro nulo nem erro de inserção depois do envio bem sucedido. Validar owner BU/conversa/contato/direção na reconciliação; incompatibilidade é erro/quarentena de identidade, sem sobrescrever outro recurso. Registro local sem externalId confirmado conserva pendência/erro explícitos, sem inventar ID, retry externo ou garantia de deduplicação por ID inexistente.

Eco primeiro cria OUT sem autoria humana inventada; resultado interno enriquece o mesmo registro com conteúdo/autoria humana ou Typebot comprovados pelo caller. Eco posterior não apaga/substitui essa autoria e não muda createdAt/ID. Só criação vencedora emite evento de nova mensagem; enriquecimento preserva a identidade e usa refresh/projeção existente, sem novo IN, unread ou bot. Retorno BFF/público mantém seus contratos e contém o registro reconciliado. Invariantes de janela, permissão, conversa BU/contato, ordenação e timeline permanecem. Nenhum cache de ecos em memória ou lookup-antes-insert substitui o índice/transação. Continua explícito o limite de crash depois do commit e antes da publicação; não há claim exactly-once externo.

A regra de não adotar instâncias Evolution não gerenciadas não impede a reautorização oficial já contratada no slot migrado. Mapping OFICIAL backfilled conserva somente ownership local, sem credencial nem confiança. Uma nova REAUTORIZAR explícita por ADMIN, no mesmo slot/BU/telefone e com recurso e credencial novamente comprovados na Meta, pode estabelecer o vínculo pelo fluxo canônico atual e suas condições de promoção. Backfill isolado, recurso de outra BU/slot e instância Evolution legada continuam recusados; não há adoção ou cleanup externo por inferência de nome/mapping.

### Segredos transitórios e webhook raw

Code SDK e PIN podem existir transitoriamente no formulário/memória do browser e seguir via BFF HTTPS; nunca em URL, storage, trace, screenshot, log ou DTO de retorno. Token, chave e envelope ficam somente no backend. Antes de persistir evento raw de provider autenticado, redigir recursivamente apikey, token, authorization, code, PIN, QR e componentes secretos de URLs; erros/audit usam catálogo e metadados allowlisted. Evento sem identidade verificada não persiste conteúdo. Harness envia envelope Evolution com apikey fictícia e comprova sua ausência em raw/audit/DTO/erro. QR só é devolvido efemeramente ao administrador no POST autorizado. Gateway Nginx, proxy e logs de aplicação não registram URI/token do callback Evolution: política explícita remove caminho secreto e query de access/error logs, inclusive erros; harness passa segredo fictício pelo gateway real e inspeciona logs/artefatos. Callback por header só se suportado e comprovado no provider fixado, sem presumir capacidade.

Meta raw é particionado por recurso verificado/BU, não por corpo de request inteiro. Batch assinado com entry/change/value de BUs diferentes produz registros scoped separados; fragmento desconhecido/retirado/sem identidade contribui apenas metadados allowlisted, sem conteúdo. Assinatura é verificada sobre o corpo original antes de parse/partição. REG-SEC-12/13 concretizam requisitos já existentes de segredo/owner, sem novo armazenamento genérico.

O suporte condicional de header foi confirmado no source fixado Evolution2.3.7 (`webhook.controller.ts` do commit cd800f2976e1e5b682fbf86a01ee4d85ae61f370): o provider aplica webhook.headers ao callback, mas registra URL em erros. Para cumprir a regra secret-free, o callback desta instalação usa URL sem segredo `POST /webhooks/evolution` e header privado `x-leadshug-webhook-secret`, comparado de modo timing-safe com EVOLUTION_WEBHOOK_SECRET. Não manter autenticação alternativa por path. Essa concretização exige teste real de callback/logs no runtime fixado antes da prova de aparelho; confirmação apenas de source não certifica execução. O segredo continua privado no adapter/backend, sem DTO/audit/raw/config.js.

Na prova privada cp49 de2026-10-17, a imagem API com a convergência corrigida recebeu o retorno automático da mesma Evolution após stop/start: connectedAt novo posterior ao start, identidade/geração/epoch/receipt atuais e tentativa já concluída v2 preservados, sem verificação administrativa posterior. A mesma conversa e suas duas mensagens anteriores permaneceram. Isso comprova somente essa retomada observada; INOUT02 humana e fluxo oficial continuam requisitos separados no TODO, e a cobertura isolada de app_id estrangeiro está sendo concluída antes da etapa oficial.


### Documento público de privacidade da instalação de testes

O complemento cp63 autorizado pelo usuário disponibiliza /privacidade.html como asset estático do Web, sem autenticação, resolução de Mantenedora/BU, formulários, SDK ou leitura de dados de negócio. A UNIFAST e o contato público unitech@unifast.com.br foram informados pelo responsável. A política distingue tokens oficiais cifrados de outras credenciais, histórico persistente de diagnósticos de webhook da API (rotina90dias), e cópias/estado mantidos pela integração, cuja retenção efetiva não foi demonstrada. Solicitações são tratadas por e-mail, sem promessa de exclusão integral automática. O documento descreve somente a instalação privada de testes; sua URL pública não autoriza publicação Meta/produção nem admissão de usuários não confiáveis.

Fonte cp63: único asset web-app/public/privacidade.html byteexact com cp63-privacy-policy.accepted.html SHA d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d. Crítica independente terminal integrada; build e28testes Web passaram uma vez. A candidata6f teve prova direta/layout e final distinto aceitos; no HTTPS houve transformação Cloudflare, resolvida cp64 pela location exata no-transform da candidata cfd5. Prova pública independente root40f8df7d... confirma20012865/d0 sem scripts/formulários/CFmarkers/cookies/redirect; roothealth200 e JSd143. API segue mesma imagemfe5 com origem atual alinhada; publicação do mesmo app Meta autorizada cp66 e confirmada pelo operador cp67. Baseline posterior permanece semreceipt/connectedAt e IN0/OUT0 na identidade oficial atual; teste real02 não apareceu, readbackcp68 ainda semmensagens e GETMeta confirma appinscrito naWABA. Destinatário/tiques atuais aguardam conferência; causaaberta. O build transitório não foi tratado como prova de dist/HTTP. Evidência no pacote de revisão ST-CON-01.

Histórico operacional (cp106,2026-10-19): o operador concluiu o cadastro oficial Já registrado pelo fluxo atual e confirmou IN visível em Atendimento Local Test Ofc e OUT recebida no WhatsApp do interlocutor. BFF canônico confirmou BU ativa/OWNER, canal oficial CONECTADO/geração2/identidade própria verificada/SUBSCRIBED/receipt confirmado; IDs externos não são expostos nesse DTO. O QR da Local Test BU foi preservado CONECTADO/geração1/identidade e recebimento verificados; sua INOUT e retomada anteriores cp49/52 continuam válidas. Provas antigas de controle sintético e falhas cp62/68 são históricas. A hipótese de proprietário da conversa antiga não foi comprovada. Recuperação oficial CON-12/VAL05 e closeout permanecem pendentes; nenhuma prontidão geral, operação contínua ou conclusão do TODO é declarada. Evidência: artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp106-official-inout-readback.json.

Atualização operacional cp107 (2026-10-19): um único restart autorizado da API preservou seu ID/imagem e mudou StartedAt; health local e HTTPS voltaram200. BFF antes/depois preservou canais oficial/QR, gerações2/1, tentativas, identidade, provider SUBSCRIBED/CONNECTED e receipt true. Nenhuma alteração de fonte/configuração/Meta/credencial/banco. Isso comprova retomada do backend observado, sem comprovar nova IN/OUT ou reconexão da conta Meta. Nova troca física foi solicitada ao mesmo interlocutor alternativo; CON-12/VAL05 e closeout seguem pendentes. [Evidência cp107](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp107-api-restart-recovery.json).

Estado operacional CP108 (2026-10-19): usuário confirmou nova IN visível em Atendimento Local Test Ofc e resposta OUT recebida no WhatsApp após o reinício autorizado da API. Readback confirma o mesmo processo reiniciado, BUs ativas/OWNER, oficial CONECTADO/geração2/SUBSCRIBED/identidade e receipt true, QR preservado CONECTADO/geração1/CONNECTED/receipt true. Com CP106/107 e não oficial CP33/49/52, VAL05 físico local por ambos os canais está satisfeito. Contador Meta POST200 agregado é evidência separada de transporte, sem atribuição de conteúdo/conta. Encerramento local concluído CP108; sem alegar produção, disponibilidade contínua ou importação de histórico. Próximo recorte de produto permanece ST-CON-04 Nova conversa por contato, sujeito a contrato próprio. [Prova CP108](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp108-post-restart-official-inout.json).


## Channel abstrato e envio comum — ST-CON-06

Contrato v1.3 aprovado e exercitado localmente: all93791 passou613testes, revisões independentes de aderência/segurança/cutover/TQA e Performance convergiram, com uma dívida baixa explícita de precisão de métrica de teste. O operador confirmou nova IN e resposta OUT nos vínculos oficial e não oficial após ativação das imagens atuais; a proveniência fonte→imagem→container→HTTP foi conferida antes e depois. A revisão final e os guards de closeout são registrados no [TODO governante](../todos/completed/features/TODO-leadshug-channel-abstraction.md). Evidências: [validação automatizada](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/v13r4-final-validation.json), [ativação](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-activation-provenance-v13r4-final.json), [prova assistida](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-operator-proof-v13r4.json) e [proveniência posterior](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/post-operator-readback-v13r4.json). Não é prova de produção, disponibilidade contínua ou redes futuras.

Channel is the domain text-send abstraction. TextMessage carries kind:text, opaque recipientRef and text; sendMessage returns a discriminated result. Current Meta/Evolution adapters encapsulate protocol addresses and credentials in an immutable operation instance created by an explicitly registered factory. ChannelResolver is injected through one ChannelTransportModule; existing BFF/Public/Webhooks composition shares its resolver and outbound orchestration. Common senders do not import concrete clients, switch on provider, use service location, mutate singleton credentials, or retain an old dispatch shim. Registration/protocol clients remain legitimate narrow consumers outside the common send boundary.

A server-authorized conversation/BU or accepted verified bot ingress selects the binding. The context captures channel/BU, resource identity, generation, epoch and official credential version. Before the sole external POST, local owner/identity/readiness/version checks fail closed. Same-resource REAUTORIZAR changes generation; it is distinct from a credential-version-only reseal after dispatch. Captured context is never rebound to a newer identity. No HTTP occurs in a DB transaction, and no automatic external retry or per-send external probe is introduced. The local-check-to-network interval and crash recovery remain explicit limitations.

ACCEPTED requires a valid nonempty provider message ID and does not mean handset delivery. BLOCKED occurs locally before dispatch. Meta definitive REJECTED uses only the approved stable Graph envelope allowlist; contradictory/malformed/timeout/redirect/transient results remain UNKNOWN. A supported acknowledgement without ID can yield a positively committed failed/null-ID diagnostic. Arbitrary2xx objects do not establish that acknowledgement. Legacy HTTP codes remain compatible while outcome/evidence accurately describe uncertainty. Known provider acceptance followed by any local failure remains ACCEPTED_LOCAL_INCOMPLETE, with RECORDED only on positive commit or bounded captured-key readback. No blind resend, durable outbox or null-ID echo merge is promised.

Future networks register a concrete implementation against the same narrow port. The current physical origin enum is storage provenance, not a declaration that Instagram/Messenger/Telegram identity, credentials, ingress or lifecycle are implemented. New capabilities, including template authoring/catalog/submission in ST-CON-05, require narrow contracts rather than no-op methods or concrete casts on Channel.

### Contratos de API e resultados seguros

Existing authorization remains upstream of channel resolution: session/BU grant and CSRF for BFF mutations; scoped partner key/account for the public API; accepted verified ingress for Typebot. Availability grants no access and the POST revalidates the bound context. Message and success DTOs are preserved.

| Surface | Contract addition / preserved result |
|---|---|
| GET `/api/bff/conversations/:id/messages` | `janela.disponivel:boolean`, `janela.motivo:AvailabilityReason|null`; existing `exigida`, `aberta`, `expiraEm`, `canal` and timeline pagination retained. Existing authorized read-marker semantics remain separate from observational availability. |
| POST `/api/bff/conversations/:id/messages` | Existing `{texto}` and201 `{id,canal,em}`; shared outbound policy/acceptance and safe uncertainty projection below. |
| GET `/api/v1/conversations` | Add `envio_disponivel:boolean`, `motivo_indisponibilidade:AvailabilityReason|null` per row; retain window/timeline fields. Bindings/credential metadata batched, latest-IN only for actually selected window-requiring origins. |
| GET `/api/v1/conversations/:telefone/messages` | Add `envio_disponivel`, `motivo_indisponibilidade`; existing message/window fields and scoped lookup retained. |
| POST `/api/v1/messages` | Existing numeric phone normalization, account/key scope, rate limit, `{account_id,telefone,texto,atendente?}` and201 `{ok:true,message_id,canal}` retained. Existing conversation creation before attempted send remains; first-send intent belongs to04. |
| Accepted Typebot text output | Same bound abstract send/policy, exact verified ingress, no fabricated human actor, no external replay after refusal/uncertainty/block. |

**Field Definitions**

- `AvailabilityReason`: `CANAL_AUSENTE` no binding; `CANAL_AMBIGUO` multiple bindings without selecting history; `CANAL_SELECIONADO_INDISPONIVEL` selected origin has no usable binding; `CHANNEL_IDENTITY_NOT_VERIFIED` identity proof missing; `CHANNEL_NOT_READY` connection/receipt not ready; `PENDING_CREDENTIAL` credential metadata not active; `JANELA_FECHADA` applicable free-text window closed. Available observation has `motivo=null`.
- Transport `ChannelSendResult.outcome`: `ACCEPTED` valid provider ID; `BLOCKED` local pre-dispatch failure; `REJECTED` proven synchronous refusal; `UNKNOWN` inconclusive dispatched result. Accepted does not mean handset delivery.
- Safe error `outcome`: `BLOCKED`, `REJECTED`, `UNKNOWN`, plus `AMBIGUOUS_SEND_RECORDED` only a positively committed ACK-without-ID diagnostic, and `ACCEPTED_LOCAL_INCOMPLETE` known external acceptance with incomplete local conclusion.
- `evidence`: `ACK_WITHOUT_ID` structurally supported acknowledgement missing ID, or `TRANSPORT_UNCONFIRMED` inconclusive transport result. `localMessageState` and `diagnosticPersistence`: `RECORDED` only positive commit/captured-key readback evidence; otherwise `UNCONFIRMED`. No raw provider text, token, URL, credential envelope or callback data enters these fields.

| Safe error case | HTTP/code and state |
|---|---|
| Proven refusal |400 provider mapper code, `outcome=REJECTED`, fixed refusal text. |
| Unconfirmed transport |Legacy400/code retained with `outcome=UNKNOWN`, `evidence=TRANSPORT_UNCONFIRMED`; no authoritative sent Message. A changed captured context instead takes409 `CHANNEL_CONTEXT_CHANGED`. |
| ACK without ID, positive diagnostic commit |409 `EXTERNAL_MESSAGE_ID_MISSING`, `outcome=AMBIGUOUS_SEND_RECORDED`, `evidence=ACK_WITHOUT_ID`, `diagnosticPersistence=RECORDED`; diagnostic is failed/null-ID, never a sent Message. |
| ACK without ID, diagnostic/context failure |Changed captured context takes409 `CHANNEL_CONTEXT_CHANGED`, `outcome=UNKNOWN`; other diagnostic failure takes503 `OUTBOUND_LOCAL_INCOMPLETE`, `outcome=UNKNOWN`. Persistence metadata reflects only observed commit. |
| Valid provider ID, any local acceptance/finalization failure |409 `CHANNEL_CONTEXT_CHANGED` when captured identity/generation/epoch changed; otherwise503 `OUTBOUND_LOCAL_INCOMPLETE`. Both retain `outcome=ACCEPTED_LOCAL_INCOMPLETE` and truthful `localMessageState`. No extra provider call/rebind. |

The Inbox retains drafts for every error, uses fixed safe text for uncertainty/local-incomplete outcomes, drops duplicate in-flight submit triggers and fences late body/completion effects by BU/conversation generation. Consumers must inspect outcome/evidence rather than infer rejection from a legacy400. No automatic retry is authorized.

### Consumidores seguintes e limites

ST-CON-05 is approved and implemented locally; its durable contract is consolidated below. The seller creates and submits directly for Meta review; no administrator intermediary is inserted. ST-CON-04 may later consume eligible templates for first-send outside the official window, but needs its own approval and must independently revalidate current eligibility and account/channel context. Existing public POST conversation creation before attempted send remains unchanged. Local channel activation and assisted IN/OUT evidence belong to their respective TODOs and do not establish production readiness.

## Modelos textuais — ST-CON-05

This section owns the stable template-management contract. The completed [ST-CON-05 TODO](../todos/completed/features/TODO-leadshug-official-template-authoring.md) remains authoritative for execution, validation, evidence, and closeout. The seller is the submitter; submitted assets belong to the shared remote Messaging account and are not private to their creator. The initial product surface supports official-channel management only. It does not send a template to a recipient or implement ST-CON-04.

### Ownership and persisted records

The `message-templates` domain owns drafts, immutable revisions, submissions, status observations, and the account catalog projection. Its persistence is scoped by the authorized Mantenedora/BU, creator, channel, and server-resolved account. The account-level name reservation is a coordination record across all local links to the same remote account; it carries no draft content and grants no access to another tenant's draft or operation.

| Record | Durable responsibility and invariant |
| --- | --- |
| Draft and revision | Creator, BU, channel, resolved account, monotonic revision, and immutable definition snapshot. `DRAFT` is editable; `LOCKED` is frozen while dispatch or an uncertain/accepted external result is being resolved. No credential is stored here. |
| Submission operation | Scoped idempotency key, request fingerprint, immutable revision reference, phase/outcome, lease/fence, dispatch claim, and safe receipt metadata. A request key replays its original operation; it never authorizes a second POST. |
| Account/name reservation | Canonical remote-account/name/language namespace, coordinated globally for that account. Reservation and release use CAS and positive local commit certainty; conflicts reveal no foreign tenant, owner, content, or counts. |
| Remote observation and catalog projection | Remote ID, account/context identity, supported definition/status fields, observation time, eligibility/freshness, and bounded-page cursor metadata. Individual refresh and catalog refresh update the same observation owner. |

The domain depends on narrow `TemplateManagementResolver` and `MessageTemplateProvider` ports. The resolver receives an already-authorized BU/channel reference and returns an operation-bound provider plus immutable safe context (BU, channel, resource identity, generation, epoch, active credential version, and opaque account reference). The provider exposes template create/list/query operations only. Protocol IDs, addresses, and credentials stay inside the integration adapter. The Meta template adapter has a dedicated client and explicit registration; template services do not import HTTP or concrete Meta clients. Channel and `ChannelResolver` remain text-send contracts and gain no template methods, no-op capability, casts, or provider branches. Management reuses the existing credential resolver/crypto with purpose `template-management`; it does not weaken the `send` purpose or readiness checks.

### API Endpoint Definitions

All endpoints are BFF session routes under `/api/bff`. Reads require an authenticated session and a grant in the resolved BU. Mutations also require CSRF protection. Role shorthand: `ATENDENTE+` means ATENDENTE, ADMIN, or OWNER with a grant in the target BU; `owner/admin` means the draft creator or an ADMIN/OWNER authorized for that BU. A known insufficient role is 403; an absent session is 401; an inaccessible resource/owner is 404. Account, channel, generation, and active credential version are resolved and checked server-side; client IDs never grant scope.

| Method and path | Authorization and request | Outcome and effect |
| --- | --- | --- |
| `GET /api/bff/business-units/:buId/channels/:channelId/message-template-capabilities` | Session, `ATENDENTE+`; no body. | 200 with safe capability, reason, and current generation from local context only. No provider call or credential material. |
| `GET /api/bff/business-units/:buId/message-templates?view=mine&page=1` | Session, creator-scoped `mine`; `view=bu` requires ADMIN/OWNER; page size defaults to 20 and is capped at 50. | 200 local page ordered by `(createdAt,id)`, with `hasMore`; no provider fan-out. |
| `POST /api/bff/business-units/:buId/message-templates/preview` | Session/CSRF, `ATENDENTE+`; `{channelId,expectedGeneration,draftId?,expectedRevision?,definition}`. | 200 normalized definition, plain-text preview, and request fingerprint bound to current context. Zero DB writes and zero provider calls. An unsaved preview is explicitly unpersisted and cannot authorize submit. |
| `POST /api/bff/business-units/:buId/message-templates` | Session/CSRF, `ATENDENTE+`; `{clientRequestId,channelId,expectedGeneration,name,language,category,body,header?,footer?,examples}`. | 201 for a new DRAFT revision 1; account is derived server-side and no Meta POST occurs. Idempotent replay returns the original safe result. |
| `GET /api/bff/message-templates/:id` | Session; own draft or ADMIN/OWNER in its BU. | 200 safe draft/revision/operation projection. Observational only; no provider call or transition. |
| `PATCH /api/bff/message-templates/:id` | Session/CSRF; own editable draft or ADMIN/OWNER; `{expectedRevision,definition}`. | 200 on CAS save with a new immutable revision/fingerprint; 409 on revision/state conflict. No remote mutation. |
| `POST /api/bff/message-templates/:id/submit` | Session/CSRF; owner/admin; `Idempotency-Key` UUID and `{expectedRevision,expectedGeneration,expectedDefinitionFingerprint}`. | At most one Meta POST per durably claimed operation. 201 when newly accepted for processing; 202 while its lease is active; replay returns the same operation/receipt. No `/messages` call. |
| `GET /api/bff/message-templates/:id/operations/:operationId` | Session; same BU and owner/admin. No browser idempotency key. | 200 safe receipt, phase, lease expiry, and server-derived recovery action. Observational; no provider call. |
| `POST /api/bff/message-templates/:id/operations/:operationId/reconcile` | Session/CSRF; owner/admin, same persisted operation. | 202 for a live lease. Expired PREPARED is CAS-closed as REJECTED without dispatch. Expired SENDING/AMBIGUOUS uses bounded GET-only recovery; it never repeats the POST. |
| `POST /api/bff/message-templates/:id/refresh` | Session/CSRF; owner/admin; server-resolved original account/context. | Bounded remote read updates the shared observation only under the current account lease/fence. Stale or failed reads preserve the prior observation and report it unavailable/stale. |
| `GET /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` | Session, `ATENDENTE+`; local page, optional bounded `after` cursor. | 200 cached local catalog page (maximum 50); no remote fan-out. |
| `POST /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` | Session/CSRF, `ATENDENTE+`; `{after?}`. | One bounded remote page per explicit action, through the same account lease/fence and observation projector as individual refresh. No caller-supplied provider URL/cursor URL. |

Common safe HTTP outcomes: 400 for invalid definition/request; 401 unauthenticated; 403 insufficient role on a known BU; 404 inaccessible resource; 409 for revision, account, name, key, or context conflict; 200 for reads/replays; 201 for a newly created draft or accepted operation; 202 for an in-progress operation; 429 with safe `Retry-After`; 503 for an inconclusive provider/local result. Provider text, raw payloads, URLs, tokens, and credential envelopes never appear in responses or logs. Meta review rejection is a `ProviderApprovalStatus.REJECTED` observation, not transport failure or failed creation.

### Field Definitions

Create supports `pt_BR`, `MARKETING` or `UTILITY`, a normalized name matching `[a-z][a-z0-9_]{0,127}`, required BODY text of 1–1024 characters, optional static TEXT HEADER/FOOTER of at most 60 characters each, and up to 20 unique named BODY variables matching `[a-z][a-z_]{0,31}`. Each variable has one fictional text example of 1–128 characters. Unsupported components, malformed/unpaired braces, variables at the start/end, and definitions over 16 KiB are rejected. Preview is backend-validated; React renders escaped text and fences debounced responses by monotonically changing context/revision ownership.

| Field | Values and meaning |
| --- | --- |
| Draft state | `DRAFT` is editable before external submission; `LOCKED` is immutable while submitted, accepted, or uncertain. A proven pre-dispatch rejection can reopen by CAS for a new revision/key; a later Meta analysis rejection does not reopen an accepted revision. |
| Submission outcome | `PREPARED` means no dispatch; `SENDING` means a durable dispatch claim; `ACCEPTED` means a known nonempty remote ID; `REJECTED` means proven refusal; `AMBIGUOUS` means external outcome is unknown. |
| Provider approval status | `PENDING`, `APPROVED`, `REJECTED`, `PAUSED`, `DISABLED`, `ARCHIVED`, `DELETED`, `IN_APPEAL`, `PENDING_DELETION`, `LIMIT_EXCEEDED`, or `UNKNOWN`. `UNKNOWN` is never approval. Requested category and provider-effective category remain separate. |
| Observation eligibility | Only an observed `APPROVED` status in the current account/channel/generation/epoch/managed-identity/credential-version context, no older than 300 seconds by server time, is `observedEligible=true`. Stale, failed, malformed, or context-mismatched refresh preserves prior status but marks it unavailable/stale. ST-CON-04 must independently revalidate before sending. |
| Fingerprints | `requestFingerprint` binds the full immutable local request, account/context, revision, and examples. `remoteSemanticFingerprint` compares exact supported remote semantics and excludes only provider metadata and examples. Content is not trimmed or normalized to force a match. |
| Acceptance provenance | `ACKNOWLEDGED` records a known provider creation ID; `CORRELATED_BY_DEFINITION` records an exact recovery match without proving authorship. `providerAcceptance=CONFIRMED` requires a known acknowledged ID; correlation alone leaves it `UNKNOWN`. A later different acknowledged ID preserves both facts and reports `PROVIDER_ACK_CONFLICT` rather than silently replacing the association. |
| Error/receipt metadata | Template creation returns `ACCEPTED`, proven `REJECTED`, or `AMBIGUOUS`; the operation also has the pre-dispatch phases `PREPARED` and `SENDING`. Post-dispatch uncertainty reports `TEMPLATE_SUBMISSION_UNCERTAIN` with phase `AMBIGUOUS` and outcome `PROVIDER_RESULT_UNCERTAIN`. Local incompleteness reports `TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE`, preserving known acceptance separately. `receiptPersistence=RECORDED` requires positive commit or exact captured-key readback; otherwise it is `UNCONFIRMED`. A recorded receipt can coexist with `projectionPersistence=UNCONFIRMED`. No raw provider text or secret is included. |

### Dispatch, recovery, and shared observation rules

Submission reserves the canonical account/name/language and operation in a short transaction, then performs HTTP outside the transaction. The namespace coordinates every local link to the same remote account, including different BUs/tenants, while all business drafts, operations, and observations remain tenant/BU/creator scoped. Submit performs at most three bounded GETs (grant plus up to two filtered pages) and one POST; each external request times out at 10 seconds, total work is budgeted to 45 seconds under a 60-second operation lease, and durable limits are 10 attempts/minute per actor and 60 dispatches/hour per canonical account namespace. The server performs exact name/language checks; it never scans the full catalog or trusts client/provider continuation URLs. An incomplete filtered listing fails closed without POST. A confirmed claim commit is required before HTTP; uncertain persistence retains the reservation and cannot authorize another POST.

The `PREPARED → SENDING` transition is a CAS over revision, lease, dispatch claim, and captured account context. A durable operation makes at most one POST. A structurally valid response with a nonempty ID is `ACCEPTED`; acceptance and local receipt persistence are separate facts. If an ACK is known but persisting its receipt/association is unconfirmed, the submit endpoint returns 503 `TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE` with outcome/phase `ACCEPTED`, `providerAcceptance=CONFIRMED`, and `receiptPersistence=UNCONFIRMED`; retain the reservation and recover the same operation without another POST. This error response does not include `acceptanceProvenance`; persisted operation/receipt projections expose provenance separately when available. If the receipt is confirmed but its projection is incomplete, keep `receiptPersistence=RECORDED` and report `projectionPersistence=UNCONFIRMED`. A creation response without an ID remains `AMBIGUOUS`, never acknowledged acceptance. A synchronous refusal is `REJECTED` only when the response shape/code proves no creation; timeout, malformed or missing ID, 5xx/429 after dispatch, redirect, transient/unknown code, or crash is `AMBIGUOUS`. No automatic POST retry is allowed.

Reconcile is the sole explicit recovery mutation. A live lease returns 202 without provider access. Expired PREPARED is CAS-closed as `REJECTED(dispatched=false)` and cannot later dispatch. Expired SENDING and AMBIGUOUS recovery are GET-only, under a new lease/fence, against the original account, bounded by grant plus two name-filtered pages. Exactly one semantic match may be recorded as `CORRELATED_BY_DEFINITION`; it does not prove who created the remote asset or that examples were accepted. Missing, multiple, divergent, inaccessible, or incompletely paginated results remain `AMBIGUOUS`, locked, and reserved. Late dispatch results may enrich only their original receipt monotonically; they cannot change a newer revision or context. Existing remote assets found before dispatch conflict and are never adopted or deleted.

Individual refresh and catalog refresh share one persistent lease and monotonic fence per authorized account/context, one 10-second debounce window, and one observation projector. Each writer captures BU, channel, resource identity, generation, epoch, managed identity, and active credential version. Only the owner of the live current fence may update observations, status, `observedAt`, eligibility, or its page cursor. A stale response cannot overwrite newer `APPROVED → PAUSED` or other status. Refresh failure retains the previous status/time/fence/content but marks the current availability unavailable; an explicit later refresh can recover it. Catalog page size is at most 50 and does not fan out per item.

### Decision mapping and accepted limits

The approved D01–D09 and review resolutions AR-01..05 / CR-01..03 are consolidated here; detailed execution criteria remain in the completed TODO:

| Decision | Stable module contract |
| --- | --- |
| D01 | Seller-owned create/submit; existing OWNER/ADMIN/ATENDENTE grants; admin/owner BU view; inaccessible drafts are hidden; remote assets are account-shared, with no approval intermediary. |
| D02 | Backend-authoritative subset, preview, normalization, examples, and fingerprint; no cross-repository import or client-side authoritative parser; no approval guarantee. |
| D03 | `message-templates` owns durable draft/revision/operation/observation/catalog; immutable revisions and CAS; no prior draft decision is replaced. |
| D04 | Explicit `template-management` purpose on the current official managed identity and active credential version; no receipt/readiness bypass and no weakening of `send`. |
| D05 | Durable scoped idempotency, canonical account-wide name namespace, positive commit before HTTP, bounded preflight and one POST maximum. |
| D06 | Typed refusal/acceptance/ambiguity, GET-only recovery, truthful persistence certainty, no automatic mutation retry or external exactly-once claim. |
| D07 | Meta owns approval state; local GET is observational; explicit bounded refresh, shared fenced projector, and 300-second freshness. |
| D08 | UI state belongs to BU/channel/draft/revision/generation/credential-version and monotonic UI context; A→B→A stale results are fenced; no recipient send or premature first-send action. |
| D09 | Narrow template resolver/provider capability is independently registered; Channel/ChannelResolver/OutboundService remain text-only and unchanged. |

AR-01 fixes current credential-version/context CAS, 300-second stale behavior, and ST-CON-04 revalidation. AR-02 makes preview backend-authoritative and unable to authorize submission. AR-03 requires exact server-side name lookup with bounded exhaustion. AR-04 keeps local request and remote semantic fingerprints distinct and preserves examples without claiming authorship. AR-05 preserves existing roles and negative grant/foreign-draft behavior. CR-01 defines observational GET, expired-lease recovery and late-result monotonicity; CR-02 defines evidence-based typed outcomes and default post-dispatch ambiguity; CR-03 permits authorized preview reads while forbidding writes/provider calls. The API contract/raw adapter cases and race harness remain governed by the completed TODO.

Accepted limits: OPS-R4-01 preserves prior status/time/fence/content and reports unavailable after a late failure; explicit refresh can recover. SEC-R6-04 keeps recovery within the current private local cohort until its read-budget follow-up is completed before public/untrusted or Railway exposure. TQA-ST05-03 retains the original test-after/unknown classification; no retrospective RED is claimed. The operator's real own-account proof records creation, status query, and persistence after reload on the owned local HTTPS origin. The actual Meta approval enum, remote receipt/ID, payload, and latency were not reported; this is not evidence of `APPROVED`, recipient delivery, ST-CON-04, public/Railway admission, production readiness, or continuing availability. See [assisted-provider proof](../artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-r42-assisted-provider-proof-v1.1.json), [source/image/running acceptance](../artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-r41-source-image-running-acceptance-v1.1.json), and [assurance disposition](../artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-candidate-r41-assurance-disposition-v1.1.json). Independent final reviews completed; their two documentation findings were integrated against the exact template source. The approved scope is complete locally; closure evidence remains in the completed TODO.


Also assess security attack scenarios and bounded I/O/transaction behavior against the current signed webhook/session/tenant fence implementation and included negative proof. Determine whether the bounded runtime activation proposal preserves data and respects pending approval boundaries. Find concrete defects; do not redesign the already-approved finite admission architecture solely for style.

## Bounded source and original-seal classification


### api-app/src/domain/channels/transport/channel.ts

SHA256 `49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import type { TemplateManagementContext, TemplateSummary } from '../../message-templates/template-management.ports';
import type { Prisma } from '@prisma/client';

export type ChannelOrigin = 'OFICIAL' | 'NAO_OFICIAL';

export type ChannelAvailabilityReason =
  | 'CANAL_AUSENTE'
  | 'CANAL_AMBIGUO'
  | 'CANAL_SELECIONADO_INDISPONIVEL'
  | 'CHANNEL_IDENTITY_NOT_VERIFIED'
  | 'CHANNEL_NOT_READY'
  | 'PENDING_CREDENTIAL'
  | 'JANELA_FECHADA'
  | 'UNSUPPORTED_KIND';

export type ChannelSendResult =
  | { outcome: 'ACCEPTED'; externalMessageId: string }
  | { outcome: 'BLOCKED'; reason: ChannelAvailabilityReason | 'CHANNEL_CONTEXT_CHANGED' }
  | { outcome: 'REJECTED'; code: string }
  | { outcome: 'UNKNOWN'; evidence: 'ACK_WITHOUT_ID' | 'TRANSPORT_UNCONFIRMED'; legacyCode: string };

export interface TextMessage {
  kind: 'text';
  recipientRef: string;
  text: string;
}

export interface ApprovedTemplateMessage {
  kind: 'approved-template';
  recipientRef: string;
  template: {
    readonly summary: TemplateSummary;
    readonly values: Readonly<Record<string, string>> | readonly string[];
    readonly managementContext: TemplateManagementContext;
    readonly renderedText: string;
    readonly semanticFingerprint: string;
  };
}

export type ChannelMessage = TextMessage | ApprovedTemplateMessage;
export type ChannelMessageKind = ChannelMessage['kind'];

export interface ChannelSendOptions {
  /** Initial dispatch carries its durable claim fence into the provider adapter. */
  readonly purpose?: 'initial';
  /** Generic dispatch fence; invoked at the final provider boundary for ordinary and initial sends. */
  readonly beforeDispatch?: () => Promise<boolean>;
}

export abstract class Channel {
  abstract readonly supportedKinds: readonly ChannelMessageKind[];
  abstract sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult>;
}

/** Safe storage provenance captured for one send; never includes provider credentials or protocol addresses. */
export interface ChannelOperationContext {
  readonly channelId: string;
  readonly buId: string;
  readonly channelOrigin: ChannelOrigin;
  readonly providerResourceIdentityId: string;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
  readonly requiresWindow: boolean;
  readonly providerAccountReference: string | null;
}

/** Parse the provider-neutral operation context persisted by the admission owner. */
export function parseChannelOperationContext(value: Prisma.JsonValue): ChannelOperationContext | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const row = value as Record<string, Prisma.JsonValue>;
  if (typeof row.channelId !== 'string' || !row.channelId
    || typeof row.buId !== 'string' || !row.buId
    || (row.channelOrigin !== 'OFICIAL' && row.channelOrigin !== 'NAO_OFICIAL')
    || typeof row.providerResourceIdentityId !== 'string' || !row.providerResourceIdentityId
    || typeof row.generation !== 'number' || !Number.isSafeInteger(row.generation) || row.generation < 1
    || typeof row.pairingEpoch !== 'number' || !Number.isSafeInteger(row.pairingEpoch) || row.pairingEpoch < 0
    || row.activeCredentialVersion !== null && (typeof row.activeCredentialVersion !== 'number'
      || !Number.isSafeInteger(row.activeCredentialVersion) || row.activeCredentialVersion < 1)
    || typeof row.requiresWindow !== 'boolean'
    || row.providerAccountReference !== null && (typeof row.providerAccountReference !== 'string' || !row.providerAccountReference)) return null;
  return {
    channelId: row.channelId,
    buId: row.buId,
    channelOrigin: row.channelOrigin,
    providerResourceIdentityId: row.providerResourceIdentityId,
    generation: row.generation,
    pairingEpoch: row.pairingEpoch,
    activeCredentialVersion: row.activeCredentialVersion,
    requiresWindow: row.requiresWindow,
    providerAccountReference: row.providerAccountReference,
  };
}

export interface ResolvedChannelOperation {
  readonly channel: Channel;
  readonly context: ChannelOperationContext;
}

export interface ChannelAvailability {
  available: boolean;
  reason: ChannelAvailabilityReason | null;
  channelOrigin: ChannelOrigin | null;
  requiresWindow: boolean;
  windowOpen: boolean;
  expiresAt: Date | null;
}

export interface ConversationChannelReference {
  conversationId: string;
  buId: string;
}

export interface InitialChannelReference extends ConversationChannelReference {
  readonly channelId: string;
  readonly kind: ChannelMessageKind;
}

export interface ConversationAvailabilityReference extends ConversationChannelReference {
  latestMessageOrigin: ChannelOrigin | null;
}

export interface VerifiedIngressChannelReference extends ConversationChannelReference {
  channelId: string;
  providerResourceIdentityId: string;
  channelOrigin: ChannelOrigin;
  generation: number;
  pairingEpoch: number;
}

export abstract class ChannelResolver {
  abstract resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation>;
  abstract resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation>;
  /** Explicit channel selection for first-message intent; never infers or falls back. */
  abstract resolveForInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation>;
  /** Bind one explicitly selected channel for bounded, local initial-message options. */
  abstract resolveForInitialOptions(reference: ConversationChannelReference & { channelId: string }): Promise<ResolvedChannelOperation>;
  abstract inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability>;
  abstract inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>>;
  abstract hasReadyChannelForNewConversation(buId: string): Promise<boolean>;
  /** Revalidates the immutable captured transport tuple using the caller's already locked local transaction. */
  abstract validateOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedContext: Prisma.JsonValue,
  ): Promise<boolean>;
  /** Validates a known accepted operation for local-only Message recovery; credential/readiness may rotate after provider ACK. */
  abstract validateAcceptedOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedContext: Prisma.JsonValue,
  ): Promise<boolean>;
  abstract contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'>;
}

```

### api-app/src/domain/inbox/conversation-start.service.ts

SHA256 `97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelResolver } from '../channels/transport/channel';

const PHONE_FORMAT = /^\+?[0-9 ().-]+$/;

export function normalizeContactPhone(value: unknown): string {
  if (typeof value !== 'string' || value.length > 40 || !PHONE_FORMAT.test(value)) {
    throw new BadRequestException({ code: 'TELEFONE_INVALIDO' });
  }
  const digits = value.replace(/\D/g, '');
  if (!/^[1-9]\d{7,14}$/.test(digits)) {
    throw new BadRequestException({ code: 'TELEFONE_INVALIDO' });
  }
  return digits;
}

/** Opens or reuses a BU/contact conversation without changing an existing one. */
@Injectable()
export class ConversationStartService {
  constructor(private readonly prisma: PrismaService, private readonly channels: ChannelResolver) {}

  async start(buId: string, phone: unknown) {
    if (!buId) throw new BadRequestException({ code: 'BU_INVALIDA' });
    const contact = normalizeContactPhone(phone);
    const existingBeforeReadiness = await this.prisma.conversation.findUnique({ where: { buId_contact: { buId, contact } } });
    if (existingBeforeReadiness) return { conversation: existingBeforeReadiness, created: false };
    // Readiness uses the resolver's narrow local metadata only. Run before the
    // row lock/transaction so concurrent same-contact requests never hold a
    // database connection while waiting for a second resolver connection.
    const ready = await this.channels.hasReadyChannelForNewConversation(buId);
    return this.prisma.$transaction(async (tx) => {
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${JSON.stringify([buId, contact])}, 0))::text AS locked`;
      const existing = await tx.conversation.findUnique({ where: { buId_contact: { buId, contact } } });
      if (existing) return { conversation: existing, created: false };
      if (!ready) {
        throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
      }
      const conversation = await tx.conversation.create({ data: {
        buId,
        contact,
        contactType: 'PESSOA',
        status: 'QUEUED',
        unreadCount: 0,
        lastMessageAt: null,
      } });
      return { conversation, created: true };
    });
  }
}

```

### api-app/src/domain/inbox/initial-message-template-renderer.ts

SHA256 `a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { createHash } from 'node:crypto';
import type { TemplateComponentSummary, TemplateSummary } from '../message-templates/template-management.ports';

export class InitialTemplateRenderError extends Error {
  readonly code = 'INITIAL_TEMPLATE_UNSUPPORTED';
  constructor() {
    super('O modelo não pode ser usado neste primeiro envio.');
    this.name = 'InitialTemplateRenderError';
  }
}

export interface InitialTemplateRender {
  readonly text: string;
  readonly semanticFingerprint: string;
}

const NAMED_KEY = /^[a-z][a-z0-9_]{0,31}$/;
const PLACEHOLDER = /\{\{([^{}]+)\}\}/g;
const MAX_PARAMETERS = 20;

function fail(): never { throw new InitialTemplateRenderError(); }
function chars(text: string): number { return Array.from(text).length; }

function canonical(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonical).join(',')}]`;
  if (value && typeof value === 'object') {
    const row = value as Record<string, unknown>;
    return `{${Object.keys(row).sort().map((key) => `${JSON.stringify(key)}:${canonical(row[key])}`).join(',')}}`;
  }
  return JSON.stringify(value) ?? 'null';
}

function validateComponentGrammar(components: readonly TemplateComponentSummary[]): { body: string; semanticComponents: unknown[] } {
  const bodies = components.filter((component) => component.type === 'BODY');
  const headers = components.filter((component) => component.type === 'HEADER');
  const footers = components.filter((component) => component.type === 'FOOTER');
  if (bodies.length !== 1 || headers.length > 1 || footers.length > 1
    || components.some((component) => !['BODY', 'HEADER', 'FOOTER'].includes(component.type))) fail();

  for (const component of components) {
    if (component.type === 'HEADER') {
      if (component.format !== 'TEXT' || typeof component.text !== 'string' || component.parameters.length !== 0
        || /[{}]/.test(component.text)) fail();
    } else if ((component.type === 'BODY' || component.type === 'FOOTER')
      && (typeof component.text !== 'string' || !Array.isArray(component.parameters))) fail();
    if ((component.type === 'BODY' || component.type === 'FOOTER')
      && [...component.text.matchAll(PLACEHOLDER)].map((match) => match[1]).join('\0') !== component.parameters.join('\0')) fail();
    if (component.type === 'FOOTER' && (component.parameters.length !== 0 || /[{}]/.test(component.text))) fail();
  }
  const body = bodies[0];
  if (!body || body.type !== 'BODY') fail();
  if (!body.text.trim()) fail();
  return {
    body: body.text,
    semanticComponents: [...headers, ...bodies, ...footers],
  };
}

export function renderInitialTemplate(
  summary: TemplateSummary,
  supplied: Readonly<Record<string, string>> | readonly string[],
): InitialTemplateRender {
  if (!summary || !summary.remoteTemplateId || !summary.name || !summary.language
    || (summary.category !== 'MARKETING' && summary.category !== 'UTILITY')
    || (summary.parameterFormat !== 'NAMED' && summary.parameterFormat !== 'POSITIONAL')
    || !Array.isArray(summary.components)) fail();
  const { body, semanticComponents } = validateComponentGrammar(summary.components);
  const occurrences = [...body.matchAll(PLACEHOLDER)].map((match) => match[1]);
  if (/[{}]/.test(body.replace(PLACEHOLDER, ''))) fail();

  let orderedValues: string[];
  let keys: string[];
  if (summary.parameterFormat === 'NAMED') {
    if (Array.isArray(supplied) || !supplied || typeof supplied !== 'object'
      || Object.getPrototypeOf(supplied) !== Object.prototype && Object.getPrototypeOf(supplied) !== null) fail();
    keys = [...new Set(occurrences)];
    if (keys.some((key) => !NAMED_KEY.test(key)) || keys.length > MAX_PARAMETERS) fail();
    const record = supplied as Readonly<Record<string, string>>;
    const suppliedKeys = Object.keys(record);
    if (suppliedKeys.length !== keys.length || suppliedKeys.some((key) => !keys.includes(key))) fail();
    orderedValues = keys.map((key) => record[key]);
  } else {
    if (!Array.isArray(supplied)) fail();
    const occurrenceKeys = [...new Set(occurrences)];
    if (occurrenceKeys.length > MAX_PARAMETERS || occurrenceKeys.some((key) => !/^(?:[1-9]|1[0-9]|20)$/.test(key))) fail();
    const positions = occurrenceKeys.map(Number).sort((left, right) => left - right);
    if (positions.some((position, index) => position !== index + 1)) fail();
    if (supplied.length !== positions.length) fail();
    keys = positions.map(String);
    orderedValues = positions.map((_, index) => supplied[index]);
  }

  if (orderedValues.some((value) => typeof value !== 'string' || chars(value) < 1 || chars(value) > 1024)) fail();
  const valueByKey = new Map(keys.map((key, index) => [key, orderedValues[index]]));
  const renderedBody = body.replace(PLACEHOLDER, (_token, key: string) => {
    const value = valueByKey.get(key);
    return value === undefined ? fail() : value;
  });
  const text = [
    ...summary.components.flatMap((component) => component.type === 'HEADER' && component.format === 'TEXT' ? [component.text] : []),
    renderedBody,
    ...summary.components.flatMap((component) => component.type === 'FOOTER' ? [component.text] : []),
  ].join('\n');
  if (chars(text) < 1 || chars(text) > 4096) fail();

  const semanticFingerprint = createHash('sha256').update(canonical({
    version: 'initial-template-text-v1',
    remoteTemplateId: summary.remoteTemplateId,
    name: summary.name,
    language: summary.language,
    category: summary.category,
    parameterFormat: summary.parameterFormat,
    components: semanticComponents,
  })).digest('hex');
  return Object.freeze({ text, semanticFingerprint });
}

```

### api-app/src/domain/inbox/initial-message.service.ts

SHA256 `ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { ConflictException, HttpException, Injectable, NotFoundException, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type InitialMessageIntent } from '@prisma/client';
import { createHash, randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { OutboundService } from './outbound.service';
import { DispatchAdmissionService } from './dispatch-admission.service';
import { TEMPLATE_MANAGEMENT_RESOLVER, type TemplateManagementResolver, type TemplateManagementContext, type TemplateSummary } from '../message-templates/template-management.ports';
import { TemplateObservationService } from '../message-templates/template-observation.service';
import { InitialTemplateRenderError, renderInitialTemplate } from './initial-message-template-renderer';
import type { ChannelMessage, ChannelOperationContext } from '../channels/transport/channel';
import { Inject } from '@nestjs/common';

type TextRequest = { channelId: string; expectedGeneration: number; kind: 'text'; text: string; previewFingerprint: string };
type TemplateRequest = { channelId: string; expectedGeneration: number; kind: 'approved-template'; remoteTemplateId: string; language: string; catalogAfter: string | null; expectedDefinitionFingerprint: string; values: Readonly<Record<string, string>> | readonly string[]; previewFingerprint: string };
type InitialRequest = TextRequest | TemplateRequest;
type PreviewRequest = Omit<TextRequest, 'previewFingerprint'> | Omit<TemplateRequest, 'previewFingerprint'>;
const canonical = (value: unknown): string => {
  if (Array.isArray(value)) return `[${value.map(canonical).join(',')}]`;
  if (value && typeof value === 'object') return `{${Object.keys(value as object).sort().map((key) => `${JSON.stringify(key)}:${canonical((value as Record<string, unknown>)[key])}`).join(',')}}`;
  return JSON.stringify(value) ?? 'null';
};
const fingerprint = (value: unknown) => createHash('sha256').update(canonical(value)).digest('hex');

@Injectable()
export class InitialMessageService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly outbound: OutboundService,
    private readonly admissions: DispatchAdmissionService,
    @Inject(TEMPLATE_MANAGEMENT_RESOLVER) private readonly templates: TemplateManagementResolver,
    private readonly observations: TemplateObservationService,
  ) {}

  async assertOrdinaryDispatchAllowed(conversationId: string, buId: string): Promise<void> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: conversationId, buId }, select: { id: true },
    });
    if (!conversation) throw new NotFoundException({ code: 'CONVERSATION_NOT_FOUND' });
    const [existingMessage, active] = await Promise.all([
      this.prisma.message.findFirst({ where: { conversationId }, select: { id: true } }),
      this.prisma.initialMessageIntent.findFirst({ where: { conversationId, buId, slotReleasedAt: null }, select: { id: true, state: true } }),
    ]);
    if (active) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: active.id, state: active.state });
    if (!existingMessage) throw new ConflictException({ code: 'INITIAL_SEND_REQUIRED' });
  }

  async preview(input: { conversationId: string; buId: string; actorId: string; message: PreviewRequest }) {
    const conversation = await this.conversation(input.conversationId, input.buId);
    const operation = await this.outbound.prepareInitial({ conversationId: conversation.id, buId: conversation.buId, channelId: input.message.channelId, kind: input.message.kind });
    this.assertGeneration(operation.context, input.message.expectedGeneration);
    let text: string;
    let semantics: unknown;
    let managementContext: TemplateManagementContext | undefined;
    if (input.message.kind === 'text') {
      if (typeof input.message.text !== 'string' || !input.message.text.trim() || [...input.message.text].length > 4096) throw new ConflictException({ code: 'INITIAL_PREVIEW_INVALID' });
      text = input.message.text;
      semantics = { kind: 'text', text };
    } else {
      const templateRequest = input.message;
      const resolved = await this.templates.resolve({ buId: input.buId, channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration });
      managementContext = resolved.context;
      this.assertManagementContext(operation.context, resolved.context);
      const catalog = await this.observations.getCatalog(input.actorId, input.buId, input.message.channelId, input.message.catalogAfter);
      const summary = (catalog.items as TemplateSummary[]).find((item) => item.remoteTemplateId === templateRequest.remoteTemplateId && item.language === templateRequest.language);
      if (!catalog.available || !summary || summary.status !== 'APPROVED' || !managementContext.accountReference) throw new ConflictException({ code: 'INITIAL_TEMPLATE_UNAVAILABLE' });
      const rendered = this.renderTemplate(summary, input.message.values);
      if (rendered.semanticFingerprint !== input.message.expectedDefinitionFingerprint) throw new ConflictException({ code: 'INITIAL_TEMPLATE_CHANGED' });
      text = rendered.text;
      semantics = { kind: 'approved-template', remoteTemplateId: summary.remoteTemplateId, language: input.message.language,
        values: input.message.values, semanticFingerprint: rendered.semanticFingerprint };
    }
    const previewFingerprint = fingerprint({ version: 'initial-preview-v1', context: operation.context, recipient: conversation.contact, semantics });
    return { text, previewFingerprint,
      channel: { channelId: operation.context.channelId, channelOrigin: operation.context.channelOrigin,
        generation: operation.context.generation, requiresWindow: operation.context.requiresWindow },
      ...(managementContext ? { template: { available: true } } : {}) };
  }

  async submit(input: {
    conversationId: string; buId: string; actorId: string; actorName: string; idempotencyKey: string;
    message: InitialRequest; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>;
  }) {
    if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(input.idempotencyKey)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_INVALID' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const conversation = await this.conversation(input.conversationId, input.buId);
    const canonicalRequest = { ...input.message, recipient: conversation.contact };
    const requestFingerprint = fingerprint(canonicalRequest);
    const ownerNonce = randomUUID();
    const replay = await this.admissions.findInitialReplay({
      conversationId: input.conversationId, buId: input.buId, actorId: input.actorId,
      idempotencyKey: input.idempotencyKey, requestFingerprint, ownerNonce,
      selectedChannelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration,
    });
    if (replay) {
      const stored = this.requestRecord(replay.intent.request);
      if (canonical(stored?.canonicalRequest) !== canonical(canonicalRequest)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
      if (replay.intent.state === 'AMBIGUOUS' || replay.intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') {
        throw new ConflictException({ code: 'INITIAL_SEND_UNCERTAIN', attemptId: replay.intent.id, state: replay.intent.state });
      }
      return { replay: true, attempt: this.projectIntent(replay.intent), expiredPrepared: replay.intent.state === 'PREPARED' && replay.intent.leaseExpiresAt <= new Date() };
    }

    let preview: Awaited<ReturnType<InitialMessageService['preview']>>;
    let operation: Awaited<ReturnType<OutboundService['prepareInitial']>>;
    let payload: ChannelMessage;
    let finalSemantics: unknown;
    try {
      preview = await this.preview({ conversationId: input.conversationId, buId: input.buId, actorId: input.actorId, message: input.message.kind === 'text'
        ? { channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration, kind: 'text', text: input.message.text }
        : { channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration, kind: 'approved-template', remoteTemplateId: input.message.remoteTemplateId, language: input.message.language, catalogAfter: input.message.catalogAfter, expectedDefinitionFingerprint: input.message.expectedDefinitionFingerprint, values: input.message.values } });
      if (preview.previewFingerprint !== input.message.previewFingerprint) throw new ConflictException({ code: 'PREVIEW_CONTEXT_CHANGED' });
      operation = await this.outbound.prepareInitial({ conversationId: input.conversationId, buId: input.buId, channelId: input.message.channelId, kind: input.message.kind });
      this.assertGeneration(operation.context, input.message.expectedGeneration);
      if (input.message.kind === 'text') {
        payload = { kind: 'text', recipientRef: conversation.contact, text: input.message.text };
        finalSemantics = { kind: 'text', text: input.message.text };
      } else {
        const templateRequest = input.message;
        const management = await this.templates.resolve({ buId: input.buId, channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration });
        this.assertManagementContext(operation.context, management.context);
        const catalog = await this.observations.getCatalog(input.actorId, input.buId, input.message.channelId, input.message.catalogAfter);
        const summary = (catalog.items as TemplateSummary[]).find((item) => item.remoteTemplateId === templateRequest.remoteTemplateId && item.language === templateRequest.language);
        if (!catalog.available || !summary || summary.status !== 'APPROVED') throw new ConflictException({ code: 'INITIAL_TEMPLATE_UNAVAILABLE' });
        const rendered = this.renderTemplate(summary, input.message.values);
        if (rendered.semanticFingerprint !== input.message.expectedDefinitionFingerprint) throw new ConflictException({ code: 'INITIAL_TEMPLATE_CHANGED' });
        finalSemantics = { kind: 'approved-template', remoteTemplateId: summary.remoteTemplateId, language: input.message.language,
          values: input.message.values, semanticFingerprint: rendered.semanticFingerprint };
        payload = { kind: 'approved-template', recipientRef: conversation.contact, template: {
          summary, values: input.message.values, managementContext: management.context,
          renderedText: rendered.text, semanticFingerprint: rendered.semanticFingerprint,
        } };
      }
      const context = operation.context;
      if (fingerprint({ version: 'initial-preview-v1', context, recipient: conversation.contact, semantics: finalSemantics }) !== input.message.previewFingerprint) {
        throw new ConflictException({ code: 'PREVIEW_CONTEXT_CHANGED' });
      }
    } catch (error) {
      if (error instanceof HttpException) {
        const response = error.getResponse();
        const body = response && typeof response === 'object' && !Array.isArray(response)
          ? response as Record<string, unknown> : {};
        const marked = {
          ...(typeof body.code === 'string' ? { code: body.code } : { code: 'INITIAL_PRE_ADMISSION_REJECTED' }),
          ...(typeof body.message === 'string' ? { message: body.message } : {}),
          ...(typeof body.error === 'string' ? { error: body.error } : {}),
          preAdmission: true,
        };
        throw new HttpException(marked, error.getStatus());
      }
      throw error;
    }
    const context = operation.context;
    const originalConversation = { updatedAt: conversation.updatedAt.toISOString(), status: conversation.status,
      attendantUserId: conversation.attendantUserId, attendantName: conversation.attendantName, attendantOrigin: conversation.attendantOrigin };
    const storedRequest = { canonicalRequest, originalConversation, renderedText: preview.text, originalActorName: input.actorName } as unknown as Prisma.InputJsonValue;
    const reservation = await this.admissions.reserveInitial({
      conversationId: input.conversationId, buId: input.buId, contact: conversation.contact, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
      ownerNonce, selectedContext: context as unknown as Prisma.InputJsonValue,
      requestFingerprint, request: storedRequest,
    });
    if (!reservation.created) {
      const stored = this.requestRecord(reservation.intent.request);
      if (canonical(stored?.canonicalRequest) !== canonical(canonicalRequest)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
      if (reservation.intent.state === 'AMBIGUOUS' || reservation.intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') {
        throw new ConflictException({ code: 'INITIAL_SEND_UNCERTAIN', attemptId: reservation.intent.id, state: reservation.intent.state });
      }
      return { replay: true, attempt: this.projectIntent(reservation.intent), expiredPrepared: reservation.intent.state === 'PREPARED' && reservation.intent.leaseExpiresAt <= new Date() };
    }
    const result = await this.outbound.sendInitial({
      conversationId: input.conversationId, buId: input.buId, channelId: input.message.channelId,
      kind: input.message.kind, intent: reservation.intent, ownerNonce, operation, payload,
      request: storedRequest,
      originalConversation: { updatedAt: conversation.updatedAt, status: conversation.status, attendantUserId: conversation.attendantUserId,
        attendantName: conversation.attendantName, attendantOrigin: conversation.attendantOrigin },
      actorId: input.actorId, actorName: input.actorName, validateActorInTransaction: input.validateActorInTransaction,
    });
    let finalIntent: InitialMessageIntent | null;
    try {
      finalIntent = await this.admissions.getInitialForScopedAttempt({ id: reservation.intent.id, conversationId: input.conversationId, buId: input.buId });
    } catch {
      finalIntent = null;
    }
    if (!finalIntent) throw new ServiceUnavailableException({ code: 'INITIAL_ATTEMPT_READBACK_UNCONFIRMED', attemptId: reservation.intent.id,
      providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED', localMessageState: 'RECORDED', recoveryAction: 'RECONCILE' });
    return { replay: false, expiredPrepared: false, attempt: this.projectIntent(finalIntent),
      message: { id: result.id, channelOrigin: result.channelOrigin, createdAt: result.createdAt } };
  }

  async options(input: { conversationId: string; buId: string }) {
    const conversation = await this.conversation(input.conversationId, input.buId);
    const [channels, active, admissions, recent] = await Promise.all([
      this.prisma.buChannel.findMany({ where: { buId: input.buId }, select: { id: true, type: true, generation: true }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], take: 10 }),
      this.prisma.initialMessageIntent.findFirst({ where: { conversationId: conversation.id, slotReleasedAt: null }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }] }),
      this.admissions.listActiveAdmissions({ conversationId: conversation.id, buId: input.buId, limit: 10 }),
      this.prisma.initialMessageIntent.findMany({ where: { conversationId: conversation.id, buId: input.buId }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], take: 11 }),
    ]);
    const channelOptions = await Promise.all(channels.map(async ({ id, type, generation }) => {
      try {
        const { operation, windowOpen, expiresAt } = await this.outbound.prepareInitialOptions({ conversationId: conversation.id, buId: input.buId, channelId: id });
        const supportedKinds = operation.channel.supportedKinds;
        return { id, type, generation, pairingEpoch: operation.context.pairingEpoch,
          activeCredentialVersion: operation.context.activeCredentialVersion, supportedKinds,
          availability: { text: !operation.context.requiresWindow || windowOpen ? null : 'JANELA_FECHADA',
            'approved-template': supportedKinds.includes('approved-template') ? null : 'UNSUPPORTED_KIND' },
          ...(expiresAt ? { windowExpiresAt: expiresAt } : {}) };
      } catch (error) {
        const response = error instanceof ConflictException ? error.getResponse() : null;
        const code = response && typeof response === 'object' ? (response as Record<string, unknown>).code : null;
        return { id, type, generation, supportedKinds: [], availability: { text: typeof code === 'string' ? code : 'CHANNEL_NOT_READY', 'approved-template': typeof code === 'string' ? code : 'CHANNEL_NOT_READY' } };
      }
    }));
    return { conversationId: conversation.id,
      channels: channelOptions,
      activeAttempt: active ? this.projectIntent(active) : null,
      ordinaryAdmissions: admissions.items.map(({ id, state, expiresAt, dispatchDeadlineAt, createdAt }) => ({ id, state, expiresAt, dispatchDeadlineAt, createdAt })),
      admissionsTruncated: admissions.truncated,
      recentAttempts: recent.slice(0, 10).map((intent) => this.projectIntent(intent)),
      attemptsTruncated: recent.length > 10 };
  }

  async getAttempt(input: { id: string; conversationId: string; buId: string }) {
    const intent = await this.admissions.getInitialForScopedAttempt(input);
    if (!intent) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    return this.projectIntent(intent);
  }

  async reconcile(input: { id: string; conversationId: string; buId: string; actorId: string; actorName: string; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean> }) {
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const intent = await this.admissions.reconcileInitial({ ...input, validateActor: input.validateActorInTransaction });
    if (!intent) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    if (intent.externalMessageId && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) {
      const message = await this.outbound.reconcileInitial({ intent, actorId: input.actorId, actorName: input.actorName, validateActorInTransaction: input.validateActorInTransaction });
      const current = await this.admissions.getInitialForScopedAttempt(input);
      return { ...this.projectIntent(current ?? intent), ...(message ? { message: { id: message.id, channelOrigin: message.channelOrigin, createdAt: message.createdAt } } : {}) };
    }
    return this.projectIntent(intent);
  }

  async acknowledge(input: { id: string; conversationId: string; buId: string; actorId: string; confirmed: boolean; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>; auditInTransaction: (tx: Prisma.TransactionClient) => Promise<void> }) {
    if (input.confirmed !== true) throw new ConflictException({ code: 'DUPLICATION_RISK_CONFIRMATION_REQUIRED' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const window = await this.admissions.initialRiskWindow(input);
    if (!window) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    if (window.eligibleAt && !window.eligible) throw new ConflictException({ code: 'ACK_TOO_EARLY', eligibleAt: window.eligibleAt });
    if (!await this.admissions.acknowledgeInitialRisk({ id: input.id, actorId: input.actorId, ownerNonce: window.intent.ownerNonce,
      validateActor: input.validateActorInTransaction, audit: input.auditInTransaction })) throw new ConflictException({ code: 'ACK_NOT_ELIGIBLE' });
    return this.getAttempt(input);
  }

  async reconcileOrdinary(input: { id: string; conversationId: string; buId: string; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean> }) {
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const result = await this.admissions.reconcileOrdinary({ ...input, validateActor: input.validateActorInTransaction });
    if (!result) throw new NotFoundException({ code: 'ADMISSION_NOT_FOUND' });
    const { id, state, expiresAt, dispatchDeadlineAt, createdAt, releasedAt, riskAcknowledgedAt } = result;
    return { id, state, expiresAt, dispatchDeadlineAt, createdAt, releasedAt, riskAcknowledgedAt };
  }

  async acknowledgeOrdinary(input: { id: string; conversationId: string; buId: string; actorId: string; confirmed: boolean; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>; auditInTransaction: (tx: Prisma.TransactionClient) => Promise<void> }) {
    if (!input.confirmed) throw new ConflictException({ code: 'DUPLICATION_RISK_CONFIRMATION_REQUIRED' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const window = await this.admissions.ordinaryRiskWindow(input);
    if (!window) throw new NotFoundException({ code: 'ADMISSION_NOT_FOUND' });
    if (window.eligibleAt && !window.eligible) throw new ConflictException({ code: 'ACK_TOO_EARLY', eligibleAt: window.eligibleAt });
    if (!await this.admissions.acknowledgeOrdinaryRisk({ ...input, validateActor: input.validateActorInTransaction, audit: input.auditInTransaction })) throw new ConflictException({ code: 'ACK_NOT_ELIGIBLE' });
    const { admission } = window;
    return { id: admission.id, acknowledged: true };
  }

  private async conversation(id: string, buId: string) {
    const conversation = await this.prisma.conversation.findFirst({ where: { id, buId } });
    if (!conversation) throw new NotFoundException({ code: 'CONVERSATION_NOT_FOUND' });
    return conversation;
  }
  private projectIntent(intent: InitialMessageIntent) {
    return {
      id: intent.id, state: intent.state, createdAt: intent.createdAt, updatedAt: intent.updatedAt,
      leaseExpiresAt: intent.leaseExpiresAt, dispatchDeadlineAt: intent.dispatchDeadlineAt,
      eligibleAt: ['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state) && intent.slotReleasedAt === null
        ? intent.dispatchDeadlineAt : null,
      slotReleasedAt: intent.slotReleasedAt, externalAccepted: intent.externalMessageId !== null,
      providerAcceptance: intent.externalMessageId !== null ? 'CONFIRMED' : ['SENDING', 'AMBIGUOUS'].includes(intent.state) ? 'UNKNOWN' : 'NOT_ACCEPTED',
      receiptPersistence: intent.externalMessageId !== null ? 'RECORDED' : 'NOT_RECORDED',
      localMessageState: intent.state === 'SUCCEEDED' ? 'RECORDED' : 'UNCONFIRMED',
      recoveryAction: ['PREPARED', 'SENDING', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)
        ? 'RECONCILE' : intent.state === 'AMBIGUOUS' ? 'ACK_AFTER_DEADLINE' : null,
      riskAcknowledgementAvailable: intent.slotReleasedAt === null && ['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state),
    };
  }
  private requestRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value) ? value as Record<string, Prisma.JsonValue> : null;
  }
  private renderTemplate(summary: TemplateSummary, values: Readonly<Record<string, string>> | readonly string[]) {
    try { return renderInitialTemplate(summary, values); }
    catch (error) {
      if (error instanceof InitialTemplateRenderError) throw new ConflictException({ code: error.code });
      throw error;
    }
  }
  private assertGeneration(context: ChannelOperationContext, expected: number) {
    if (context.generation !== expected) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
  }
  private assertManagementContext(operation: ChannelOperationContext, management: TemplateManagementContext) {
    if (operation.channelId !== management.channelId || operation.buId !== management.buId
      || operation.providerResourceIdentityId !== management.providerResourceIdentityId || operation.generation !== management.generation
      || operation.pairingEpoch !== management.pairingEpoch || operation.activeCredentialVersion !== management.activeCredentialVersion
      || operation.providerAccountReference !== management.accountReference) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
  }
}

```

### api-app/src/domain/inbox/dispatch-admission.service.ts

SHA256 `bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { ConflictException, Injectable, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type DispatchAdmission, type InitialMessageIntent } from '@prisma/client';
import { randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';

const TOKEN_LEASE_MS = 90_000;

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (value && typeof value === 'object') {
    const record = value as Record<string, unknown>;
    const entries = Object.keys(record).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(record[key])}`);
    return `{${entries.join(',')}}`;
  }
  return JSON.stringify(value);
}

export function isInitialRiskAcknowledgmentEligible(
  state: InitialMessageIntent['state'], deadline: Date | null, databaseNow: Date,
): boolean {
  return (state === 'AMBIGUOUS' || state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED')
    && deadline !== null && databaseNow.getTime() >= deadline.getTime();
}

export interface ReserveOrdinaryAdmissionInput {
  conversationId: string;
  buId: string;
  caller: 'BFF' | 'PUBLIC' | 'BOT';
  actorId: string;
  ownerNonce: string;
  selectedContext: Prisma.InputJsonValue;
}

export interface ReserveInitialIntentInput {
  conversationId: string;
  buId: string;
  contact: string;
  actorId: string;
  idempotencyKey: string;
  ownerNonce: string;
  selectedContext: Prisma.InputJsonValue;
  requestFingerprint: string;
  request: Prisma.InputJsonValue;
}

export interface InitialReplayLookup {
  conversationId: string;
  buId: string;
  actorId: string;
  idempotencyKey: string;
  requestFingerprint: string;
  selectedChannelId: string;
  expectedGeneration: number;
  ownerNonce: string;
}

@Injectable()
export class DispatchAdmissionService {
  constructor(private readonly prisma: PrismaService) {}

  /** Idempotency replay lookup happens before channel binding or provider preflight. */
  async findInitialReplay(input: InitialReplayLookup): Promise<{ intent: InitialMessageIntent; ownerNonce: string } | null> {
    const intent = await this.prisma.initialMessageIntent.findUnique({ where: {
      buId_actorId_idempotencyKey: { buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey },
    } });
    if (!intent) return null;
    if (intent.conversationId !== input.conversationId || intent.requestFingerprint !== input.requestFingerprint) {
      throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
    }
    const context = this.contextRecord(intent.selectedContext);
    if (!context || context.channelId !== input.selectedChannelId || context.generation !== input.expectedGeneration) {
      throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
    }
    return { intent, ownerNonce: input.ownerNonce };
  }

  /** Create a finite owner token under the shared conversation row lock. */
  async reserveOrdinary(input: ReserveOrdinaryAdmissionInput): Promise<{ admission: DispatchAdmission; ownerNonce: string }> {
    const admissionId = randomUUID();
    try {
      const admission = await this.prisma.$transaction(async (tx) => {
        const { now } = await this.lockConversation(tx, input.conversationId, input.buId);
        const initial = await tx.initialMessageIntent.findFirst({
          where: { conversationId: input.conversationId, slotReleasedAt: null },
          select: { id: true, state: true },
        });
        if (initial) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: initial.id, state: initial.state });
        return tx.dispatchAdmission.create({ data: {
          id: admissionId,
          conversationId: input.conversationId,
          buId: input.buId,
          caller: input.caller,
          actorId: input.actorId,
          ownerNonce: input.ownerNonce,
          selectedContext: input.selectedContext,
          state: 'PREPARED',
          expiresAt: new Date(now.getTime() + TOKEN_LEASE_MS),
        } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      return { admission, ownerNonce: input.ownerNonce };
    } catch (error) {
      const admission = await this.readAdmission(admissionId);
      if (admission && this.sameOrdinaryOwner(admission, input)) return { admission, ownerNonce: input.ownerNonce };
      throw error;
    }
  }

  /** Reserve the exclusive first-send slot and immutable request under that same row lock. */
  async reserveInitial(input: ReserveInitialIntentInput): Promise<{ intent: InitialMessageIntent; ownerNonce: string; created: boolean }> {
    const intentId = randomUUID();
    try {
      return await this.prisma.$transaction(async (tx) => {
      const replay = await tx.initialMessageIntent.findUnique({
        where: { buId_actorId_idempotencyKey: {
          buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
        } },
      });
      if (replay) {
        if (replay.conversationId !== input.conversationId || replay.requestFingerprint !== input.requestFingerprint) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        if (canonicalJson(this.canonicalRequestFromStored(replay.request)) !== canonicalJson(this.canonicalRequestFromStored(input.request))) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        // Never adopt a nonce read from an idempotent replay. The caller keeps
        // the nonce it captured before this request; a stale/replayed owner
        // cannot pass a later CAS with the new nonce.
        return { intent: replay, ownerNonce: input.ownerNonce, created: false };
      }

      const selected = this.contextRecord(input.selectedContext as Prisma.JsonValue);
      if (!selected || typeof selected.providerResourceIdentityId !== 'string' || typeof selected.channelId !== 'string') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      }
      const identity = await tx.$queryRaw<Array<{ id: string }>>`
        SELECT id FROM provider_resource_identities
        WHERE id = ${selected.providerResourceIdentityId} AND bu_id = ${input.buId} AND current_channel_id = ${selected.channelId}
        FOR SHARE
      `;
      if (!identity[0]) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      const contactLockKey = JSON.stringify([input.buId, input.contact]);
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactLockKey}, 0))::text AS locked`;
      const { now, contact } = await this.lockConversation(tx, input.conversationId, input.buId);
      if (contact !== input.contact) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });

      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'initial-actor:' + input.actorId}, 0))::text AS locked`;
      const contextForRate = this.contextRecord(input.selectedContext as Prisma.JsonValue);
      const accountNamespace = typeof contextForRate?.providerAccountReference === 'string'
        ? contextForRate.providerAccountReference
        : typeof contextForRate?.providerResourceIdentityId === 'string' ? contextForRate.providerResourceIdentityId : null;
      if (!accountNamespace) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'initial-account:' + accountNamespace}, 0))::text AS locked`;
      const rateNow = await this.databaseNow(tx);
      const actorRate = await tx.$queryRaw<Array<{ count: number }>>`
        SELECT count(*)::int AS count FROM initial_message_intents
        WHERE actor_id = ${input.actorId} AND created_at >= ${new Date(rateNow.getTime() - 60_000)}
      `;
      const accountRate = await tx.$queryRaw<Array<{ count: number }>>`
        SELECT count(*)::int AS count FROM initial_message_intents
        WHERE COALESCE(selected_context->>'providerAccountReference', selected_context->>'providerResourceIdentityId') = ${accountNamespace}
          AND created_at >= ${new Date(rateNow.getTime() - 60 * 60_000)}
      `;
      if ((actorRate[0]?.count ?? 0) >= 10 || (accountRate[0]?.count ?? 0) >= 60) {
        throw new ConflictException({ code: 'INITIAL_RATE_LIMIT' });
      }

      // PREPARED means no provider claim occurred, so its immutable lease can
      // close it safely. SENDING/UNCERTAIN are never released by elapsed time.
      await tx.dispatchAdmission.updateMany({
        where: { conversationId: input.conversationId, releasedAt: null, state: 'PREPARED', expiresAt: { lte: now } },
        data: { state: 'SETTLED', releasedAt: now },
      });
      const ordinary = await tx.dispatchAdmission.findMany({
        where: { conversationId: input.conversationId, releasedAt: null },
        orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
        select: { id: true, state: true }, take: 11,
      });
      if (ordinary.length) throw new ConflictException({ code: 'ORDINARY_SEND_IN_PROGRESS', outcome: 'BLOCKED',
        ordinaryAdmissions: ordinary.slice(0, 10).map(({ id, state }) => ({ id, state })), admissionsTruncated: ordinary.length > 10 });

      const active = await tx.initialMessageIntent.findFirst({
        where: { conversationId: input.conversationId, slotReleasedAt: null },
        select: { id: true, state: true },
      });
      if (active) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: active.id, state: active.state });

      const intent = await tx.initialMessageIntent.create({ data: {
        id: intentId,
        conversationId: input.conversationId,
        buId: input.buId,
        actorId: input.actorId,
        idempotencyKey: input.idempotencyKey,
        ownerNonce: input.ownerNonce,
        requestFingerprint: input.requestFingerprint,
        request: input.request,
        selectedContext: input.selectedContext,
        state: 'PREPARED',
        leaseExpiresAt: new Date(now.getTime() + TOKEN_LEASE_MS),
      } });
      return { intent, ownerNonce: input.ownerNonce, created: true };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const intent = await this.readIntent(intentId);
      if (intent && this.sameInitialOwner(intent, input)) return { intent, ownerNonce: input.ownerNonce, created: true };
      const replay = await this.prisma.initialMessageIntent.findUnique({ where: { buId_actorId_idempotencyKey: {
        buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
      } } });
      if (replay) {
        if (replay.conversationId !== input.conversationId || replay.requestFingerprint !== input.requestFingerprint
          || canonicalJson(this.canonicalRequestFromStored(replay.request)) !== canonicalJson(this.canonicalRequestFromStored(input.request))
          || canonicalJson(replay.selectedContext) !== canonicalJson(input.selectedContext)) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        return { intent: replay, ownerNonce: input.ownerNonce, created: false };
      }
      throw error;
    }
  }

  /** Same-owner CAS after preflight; all external reads must already be complete. */
  async claimOrdinary(input: {
    id: string;
    ownerNonce: string;
    /** Must perform only bounded, transaction-local checks; all remote preflight is already complete. */
    validate: (tx: Prisma.TransactionClient, selectedContext: Prisma.JsonValue) => Promise<boolean>;
  }): Promise<boolean> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return false;
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string' || typeof context.channelId !== 'string') return false;
        // Identity retirement/renewal takes the same lock first in acceptance.
        // Preserve the global identity -> conversation -> admission order.
        const identities = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null }>>`
          SELECT id, bu_id, current_channel_id
          FROM provider_resource_identities
          WHERE id = ${context.providerResourceIdentityId}
            AND bu_id = ${hint.buId}
            AND current_channel_id = ${context.channelId}
          FOR SHARE
        `;
        if (!identities[0]) return false;
        const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${hint.conversationId} AND bu_id = ${hint.buId}`;
        if (!contactRows[0]) return false;
        const contactKey = JSON.stringify([hint.buId, contactRows[0].contact]);
        await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || current.state !== 'PREPARED'
          || current.releasedAt !== null || current.expiresAt.getTime() <= now.getTime()) return false;
        if (!await input.validate(tx, current.selectedContext)) return false;
        const claimNow = await this.databaseNow(tx);
        if (current.expiresAt.getTime() <= claimNow.getTime()) return false;
        const claimed = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE dispatch_admissions
          SET state = 'SENDING'::"DispatchAdmissionState",
              dispatch_deadline_at = expires_at,
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state = 'PREPARED'::"DispatchAdmissionState"
            AND released_at IS NULL
            AND expires_at > clock_timestamp()
          RETURNING id
        `;
        return claimed.length === 1;
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SENDING'
        && current.dispatchDeadlineAt?.getTime() === current.expiresAt.getTime()) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.releasedAt === null) return false;
      throw error;
    }
  }

  /** Initial claim shares the identity→conversation→intent lock order and immutable 90s deadline. */
  async claimInitial(input: {
    id: string;
    ownerNonce: string;
    validate: (tx: Prisma.TransactionClient, selectedContext: Prisma.JsonValue, request: Prisma.JsonValue) => Promise<boolean>;
  }): Promise<boolean> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.initialMessageIntent.findUnique({ where: { id: input.id } });
        if (!hint) return false;
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string' || typeof context.channelId !== 'string') return false;
        const identities = await tx.$queryRaw<Array<{ id: string }>>`
          SELECT id
          FROM provider_resource_identities
          WHERE id = ${context.providerResourceIdentityId}
            AND bu_id = ${hint.buId}
            AND current_channel_id = ${context.channelId}
          FOR SHARE
        `;
        if (!identities[0]) return false;
        const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${hint.conversationId} AND bu_id = ${hint.buId}`;
        if (!contactRows[0]) return false;
        const contactKey = JSON.stringify([hint.buId, contactRows[0].contact]);
        await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.initialMessageIntent.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || current.state !== 'PREPARED'
          || current.slotReleasedAt !== null || current.leaseExpiresAt.getTime() <= now.getTime()) return false;
        if (!await input.validate(tx, current.selectedContext, current.request)) return false;
        const eligibleAtClaim = await this.databaseNow(tx);
        if (current.leaseExpiresAt.getTime() <= eligibleAtClaim.getTime()) return false;
        const claimed = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE initial_message_intents
          SET state = 'SENDING'::"InitialMessageIntentState",
              dispatch_deadline_at = lease_expires_at,
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state = 'PREPARED'::"InitialMessageIntentState"
            AND slot_released_at IS NULL
            AND lease_expires_at > clock_timestamp()
          RETURNING id
        `;
        return claimed.length === 1;
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SENDING'
        && current.dispatchDeadlineAt?.getTime() === current.leaseExpiresAt.getTime()) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.slotReleasedAt === null) return false;
      throw error;
    }
  }

  async rejectInitial(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null
          || !['PREPARED', 'SENDING'].includes(current.state) || current.externalMessageId !== null) return { count: 0 };
        const now = await this.databaseNow(tx);
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: current.state, slotReleasedAt: null, externalMessageId: null },
          data: { state: 'REJECTED', slotReleasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null) return true;
      throw error;
    }
  }

  /** Releases only an owner positively known to be PREPARED; never guesses after a claim commit ACK loss. */
  async rejectPreparedInitial(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null || current.state !== 'PREPARED') return { count: 0 };
        const now = await this.databaseNow(tx);
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'PREPARED', slotReleasedAt: null, externalMessageId: null },
          data: { state: 'REJECTED', slotReleasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null) return true;
      throw error;
    }
  }

  async recordInitialExternalAccepted(input: { id: string; ownerNonce: string; externalMessageId: string }): Promise<boolean> {
    if (!input.externalMessageId.trim()) return false;
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce) return { count: 0 };
        if (current.externalMessageId === input.externalMessageId
          && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state)) {
          return { count: 1 };
        }
        if (current.externalMessageId !== null || !['SENDING', 'AMBIGUOUS'].includes(current.state)) return { count: 0 };
        // A late known provider receipt improves only this original intent. If
        // risk acknowledgment already released its slot, retain that release
        // and classify the local projection as blocked; never reacquire a slot.
        const nextState = current.slotReleasedAt === null ? 'EXTERNAL_ACCEPTED' : 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED';
        return tx.initialMessageIntent.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: current.state,
            externalMessageId: null, slotReleasedAt: current.slotReleasedAt,
          },
          data: { state: nextState, externalMessageId: input.externalMessageId },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.externalMessageId === input.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state);
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.externalMessageId === input.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state)) return true;
      throw error;
    }
  }

  async markInitialAmbiguous(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null) return { count: 0 };
        if (current.state === 'AMBIGUOUS') return { count: 1 };
        if (current.state !== 'SENDING' || current.externalMessageId !== null) return { count: 0 };
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'SENDING', externalMessageId: null, slotReleasedAt: null },
          data: { state: 'AMBIGUOUS' },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'AMBIGUOUS' && current.slotReleasedAt === null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'AMBIGUOUS' && current.slotReleasedAt === null) return true;
      throw error;
    }
  }

  async acknowledgeInitialRisk(input: { id: string; ownerNonce: string; actorId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean>; audit?: (tx: Prisma.TransactionClient) => Promise<void> }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null
          || !['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(current.state)
          || !current.dispatchDeadlineAt) return { count: 0 };
        if (input.validateActor && !await input.validateActor(tx)) return { count: 0 };
        const rows = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE initial_message_intents
          SET slot_released_at = clock_timestamp(),
              risk_acknowledged_at = clock_timestamp(),
              risk_acknowledged_by_actor_id = ${input.actorId},
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state IN ('AMBIGUOUS'::"InitialMessageIntentState", 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'::"InitialMessageIntentState")
            AND external_message_id IS NOT DISTINCT FROM ${current.externalMessageId}
            AND slot_released_at IS NULL
            AND dispatch_deadline_at IS NOT NULL
            AND clock_timestamp() >= dispatch_deadline_at
          RETURNING id
        `;
        if (rows.length === 1 && input.audit) await input.audit(tx);
        return { count: rows.length };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.slotReleasedAt !== null
        && current.riskAcknowledgedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.slotReleasedAt !== null
        && current.riskAcknowledgedAt !== null) return true;
      throw error;
    }
  }

  async listActiveAdmissions(input: { conversationId: string; buId: string; limit?: number }): Promise<{ items: DispatchAdmission[]; truncated: boolean }> {
    const limit = input.limit ?? 10;
    const rows = await this.prisma.dispatchAdmission.findMany({
      where: { conversationId: input.conversationId, buId: input.buId, releasedAt: null },
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], take: limit + 1,
    });
    return { items: rows.slice(0, limit), truncated: rows.length > limit };
  }

  async reconcileOrdinary(input: { id: string; conversationId: string; buId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean> }): Promise<DispatchAdmission | null> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return null;
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string') return null;
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} FOR SHARE`;
        await this.lockConversation(tx, input.conversationId, input.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.conversationId !== input.conversationId || current.buId !== input.buId) return null;
        if (input.validateActor && !await input.validateActor(tx)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        const now = await this.databaseNow(tx);
        if (current.state === 'PREPARED' && current.releasedAt === null && current.expiresAt <= now) {
          await tx.dispatchAdmission.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'PREPARED', releasedAt: null },
            data: { state: 'SETTLED', releasedAt: now },
          });
        } else if (current.state === 'SENDING' && current.releasedAt === null
          && current.dispatchDeadlineAt !== null && current.dispatchDeadlineAt <= now) {
          await tx.dispatchAdmission.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'SENDING', releasedAt: null, dispatchDeadlineAt: current.dispatchDeadlineAt },
            data: { state: 'UNCERTAIN' },
          });
        }
        return tx.dispatchAdmission.findUnique({ where: { id: current.id } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof ConflictException) throw error;
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      if (current && ((current.state === 'SETTLED' && current.releasedAt !== null)
        || ['SENDING', 'UNCERTAIN'].includes(current.state))) return current;
      throw new ServiceUnavailableException({ code: 'ADMISSION_RECONCILE_UNCONFIRMED' });
    }
  }

  async acknowledgeOrdinaryRisk(input: { id: string; conversationId: string; buId: string; actorId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean>; audit?: (tx: Prisma.TransactionClient) => Promise<void> }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return { count: 0 };
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string') return { count: 0 };
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} FOR SHARE`;
        const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId}`;
        if (!contactRows[0]) return { count: 0 };
        const contactKey = JSON.stringify([input.buId, contactRows[0].contact]);
        await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
        await this.lockConversation(tx, input.conversationId, input.buId);
        if (input.validateActor && !await input.validateActor(tx)) return { count: 0 };
        const rows = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE dispatch_admissions
          SET released_at = clock_timestamp(), risk_acknowledged_at = clock_timestamp(),
              risk_acknowledged_by_actor_id = ${input.actorId}, updated_at = clock_timestamp()
          WHERE id = ${input.id} AND conversation_id = ${input.conversationId} AND bu_id = ${input.buId}
            AND state = 'UNCERTAIN'::"DispatchAdmissionState" AND released_at IS NULL
            AND dispatch_deadline_at IS NOT NULL AND clock_timestamp() >= dispatch_deadline_at
          RETURNING id
        `;
        if (rows.length === 1 && input.audit) await input.audit(tx);
        return { count: rows.length };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      return Boolean(current?.releasedAt && current.riskAcknowledgedAt);
    } catch {
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      if (current?.releasedAt && current.riskAcknowledgedAt) return true;
      throw new ServiceUnavailableException({ code: 'ADMISSION_RELEASE_UNCONFIRMED' });
    }
  }

  async reconcileInitial(input: { id: string; conversationId: string; buId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean> }): Promise<InitialMessageIntent | null> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.initialMessageIntent.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return null;
        const current = await this.lockInitialOwner(tx, hint.id);
        if (!current) return null;
        if (input.validateActor && !await input.validateActor(tx)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        const now = await this.databaseNow(tx);
        if (current.state === 'PREPARED' && current.slotReleasedAt === null && current.leaseExpiresAt <= now) {
          await tx.initialMessageIntent.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'PREPARED', slotReleasedAt: null },
            data: { state: 'REJECTED', slotReleasedAt: now },
          });
        } else if (current.state === 'SENDING' && current.slotReleasedAt === null
          && current.dispatchDeadlineAt !== null && current.dispatchDeadlineAt <= now) {
          await tx.initialMessageIntent.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'SENDING', slotReleasedAt: null, dispatchDeadlineAt: current.dispatchDeadlineAt },
            data: { state: 'AMBIGUOUS' },
          });
        }
        return tx.initialMessageIntent.findUnique({ where: { id: current.id } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof ConflictException) throw error;
      const current = await this.getInitialForScopedAttempt(input);
      if (current && ['PREPARED', 'SENDING', 'AMBIGUOUS', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED', 'REJECTED'].includes(current.state)) return current;
      throw new ServiceUnavailableException({ code: 'INITIAL_RECONCILE_UNCONFIRMED' });
    }
  }

  async getInitialForActor(input: { id: string; conversationId: string; buId: string; actorId: string }): Promise<InitialMessageIntent | null> {
    return this.prisma.initialMessageIntent.findFirst({ where: {
      id: input.id, conversationId: input.conversationId, buId: input.buId, actorId: input.actorId,
    } });
  }

  async getInitialForScopedAttempt(input: { id: string; conversationId: string; buId: string }): Promise<InitialMessageIntent | null> {
    return this.prisma.initialMessageIntent.findFirst({ where: {
      id: input.id, conversationId: input.conversationId, buId: input.buId,
    } });
  }

  async initialRiskWindow(input: { id: string; conversationId: string; buId: string }): Promise<{ intent: InitialMessageIntent; eligibleAt: Date | null; eligible: boolean } | null> {
    const intent = await this.getInitialForScopedAttempt(input);
    if (!intent) return null;
    const rows = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    const now = rows[0]?.now;
    if (!(now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    const allowedState = intent.state === 'AMBIGUOUS' || intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED';
    return { intent, eligibleAt: allowedState ? intent.dispatchDeadlineAt : null,
      eligible: isInitialRiskAcknowledgmentEligible(intent.state, intent.dispatchDeadlineAt, now) };
  }

  async ordinaryRiskWindow(input: { id: string; conversationId: string; buId: string }): Promise<{ admission: DispatchAdmission; eligibleAt: Date | null; eligible: boolean } | null> {
    const admission = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
    if (!admission) return null;
    const rows = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    const now = rows[0]?.now;
    if (!(now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    return { admission, eligibleAt: admission.dispatchDeadlineAt, eligible: Boolean(admission.dispatchDeadlineAt && now.getTime() >= admission.dispatchDeadlineAt.getTime()) };
  }

  async markInitialLocalBlocked(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || !current.externalMessageId) return { count: 0 };
        if (current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') return { count: 1 };
        if (current.state !== 'EXTERNAL_ACCEPTED') return { count: 0 };
        return tx.initialMessageIntent.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: 'EXTERNAL_ACCEPTED',
            externalMessageId: current.externalMessageId, slotReleasedAt: current.slotReleasedAt,
          },
          data: { state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED' },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'
        && current.externalMessageId !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'
        && current.externalMessageId !== null) return true;
      throw error;
    }
  }

  /** Settle only the original owner; a late completion cannot release a successor token. */
  async settleOrdinary(input: { id: string; ownerNonce: string; state: 'SETTLED' | 'UNCERTAIN' }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return { count: 0 };
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || !['SENDING', 'UNCERTAIN'].includes(current.state)) return { count: 0 };
        return tx.dispatchAdmission.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: { in: ['SENDING', 'UNCERTAIN'] }, releasedAt: current.releasedAt,
          },
          data: {
            state: input.state,
            ...(input.state === 'SETTLED' ? { releasedAt: current.releasedAt ?? now } : {}),
          },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readAdmission(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === input.state
        && (input.state === 'UNCERTAIN' ? current.releasedAt === null : current.releasedAt !== null);
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === input.state
        && (input.state === 'UNCERTAIN' ? current.releasedAt === null : current.releasedAt !== null)) return true;
      if (current?.ownerNonce === input.ownerNonce && ['SENDING', 'UNCERTAIN'].includes(current.state) && current.releasedAt === null) return false;
      throw error;
    }
  }

  /** A confirmed pre-dispatch abort releases only this still-PREPARED owner. */
  async releasePrepared(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return { count: 0 };
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        return tx.dispatchAdmission.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'PREPARED', releasedAt: null },
          data: { state: 'SETTLED', releasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readAdmission(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'SETTLED' && current.releasedAt !== null;
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SETTLED' && current.releasedAt !== null) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.releasedAt === null) return false;
      throw error;
    }
  }

  private async lockConversation(tx: Prisma.TransactionClient, conversationId: string, buId: string) {
    const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; contact: string }>>`
      SELECT id, bu_id, contact
      FROM conversations
      WHERE id = ${conversationId} AND bu_id = ${buId}
      FOR UPDATE
    `;
    const row = rows[0];
    if (!row) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    return { now: await this.databaseNow(tx), contact: row.contact };
  }

  /** Preserve identity→conversation→intent order for all initial lifecycle mutations. */
  private async lockInitialOwner(tx: Prisma.TransactionClient, id: string): Promise<InitialMessageIntent | null> {
    const hint = await tx.initialMessageIntent.findUnique({ where: { id } });
    if (!hint) return null;
    const context = this.contextRecord(hint.selectedContext);
    if (!context || typeof context.providerResourceIdentityId !== 'string') return null;
    await tx.$queryRaw<Array<{ id: string }>>`
      SELECT id FROM provider_resource_identities
      WHERE id = ${context.providerResourceIdentityId}
      FOR SHARE
    `;
    const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${hint.conversationId} AND bu_id = ${hint.buId}`;
    if (!contactRows[0]) return null;
    const contactKey = JSON.stringify([hint.buId, contactRows[0].contact]);
    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
    await this.lockConversation(tx, hint.conversationId, hint.buId);
    return tx.initialMessageIntent.findUnique({ where: { id } });
  }

  private async databaseNow(tx: Prisma.TransactionClient): Promise<Date> {
    const rows = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    if (!rows[0] || !(rows[0].now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    return rows[0].now;
  }

  private contextRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value)
      ? value as Record<string, Prisma.JsonValue>
      : null;
  }

  private canonicalRequestFromStored(value: Prisma.JsonValue | Prisma.InputJsonValue): unknown {
    const record = value && typeof value === 'object' && !Array.isArray(value)
      ? value as Record<string, unknown>
      : null;
    return record && Object.hasOwn(record, 'canonicalRequest') ? record.canonicalRequest ?? null : value;
  }

  private async readAdmission(id: string): Promise<DispatchAdmission | null> {
    try { return await this.prisma.dispatchAdmission.findUnique({ where: { id } }); }
    catch { throw new ServiceUnavailableException({ code: 'ADMISSION_COMMIT_UNCONFIRMED' }); }
  }

  private async readIntent(id: string): Promise<InitialMessageIntent | null> {
    try { return await this.prisma.initialMessageIntent.findUnique({ where: { id } }); }
    catch { throw new ServiceUnavailableException({ code: 'INITIAL_INTENT_COMMIT_UNCONFIRMED' }); }
  }

  private sameOrdinaryOwner(row: DispatchAdmission, input: ReserveOrdinaryAdmissionInput): boolean {
    return Boolean(row.id) && row.ownerNonce === input.ownerNonce && row.conversationId === input.conversationId
      && row.buId === input.buId && row.caller === input.caller && row.actorId === input.actorId
      && canonicalJson(row.selectedContext) === canonicalJson(input.selectedContext);
  }

  private sameInitialOwner(row: InitialMessageIntent, input: ReserveInitialIntentInput): boolean {
    return row.ownerNonce === input.ownerNonce && row.conversationId === input.conversationId
      && row.buId === input.buId && row.actorId === input.actorId && row.idempotencyKey === input.idempotencyKey
      && row.requestFingerprint === input.requestFingerprint
      && canonicalJson(row.selectedContext) === canonicalJson(input.selectedContext)
      && canonicalJson(row.request) === canonicalJson(input.request);
  }
}

```

### api-app/src/domain/inbox/outbound.service.ts

SHA256 `0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { BadRequestException, ConflictException, HttpException, Injectable, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type InitialMessageIntent } from '@prisma/client';
import { randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelResolver, parseChannelOperationContext, type ChannelMessage, type ChannelOperationContext, type InitialChannelReference, type ResolvedChannelOperation, type VerifiedIngressChannelReference } from '../channels/transport/channel';
import type { ChannelSendResult } from '../channels/transport/channel';
import { MessageAcceptanceService, type MessageAcceptanceInput } from './message-acceptance.service';
import { DispatchAdmissionService } from './dispatch-admission.service';
import { RealtimeService } from '../../realtime/realtime.service';
import { OfficialChannelWindowPolicy } from './channel-window-policy';

const FIXED_UNKNOWN = 'Resultado do envio não confirmado; confira a conversa antes de tentar novamente.';
const FIXED_LOCAL_INCOMPLETE = 'O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente.';
const FIXED_REJECTED = 'O canal recusou o envio.';
type OutboundConversation = Prisma.ConversationGetPayload<object>;

type InitialConversationSnapshot = Pick<OutboundConversation, 'updatedAt' | 'status' | 'attendantUserId' | 'attendantName' | 'attendantOrigin'>;
type InitialActorFence = (tx: Prisma.TransactionClient) => Promise<boolean>;

export type OutboundAttribution =
  | { kind: 'BFF'; userId: string; name: string }
  | { kind: 'PUBLIC'; name: string }
  | { kind: 'BOT'; name: string };

export interface SendOutboundInput {
  conversationId: string;
  buId: string;
  text: string;
  attribution: OutboundAttribution;
  ingress?: Omit<VerifiedIngressChannelReference, 'conversationId' | 'buId'>;
}

@Injectable()
export class OutboundService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly resolver: ChannelResolver,
    private readonly acceptance: MessageAcceptanceService,
    private readonly realtime: RealtimeService,
    private readonly windows: OfficialChannelWindowPolicy,
    private readonly admissions: DispatchAdmissionService,
  ) {}

  async prepareInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation> {
    return this.resolver.resolveForInitial(reference);
  }

  async prepareInitialOptions(reference: { conversationId: string; buId: string; channelId: string }) {
    const operation = await this.resolver.resolveForInitialOptions(reference);
    const window = operation.context.requiresWindow
      ? await this.windows.inspect({ conversationId: reference.conversationId, providerResourceIdentityId: operation.context.providerResourceIdentityId })
      : { open: true, expiresAt: null };
    return { operation, windowOpen: window.open, expiresAt: window.expiresAt };
  }

  /** Local-only completion of a separately persisted known Meta/Evolution receipt. */
  async reconcileInitial(input: {
    readonly intent: InitialMessageIntent;
    readonly actorId: string;
    readonly actorName: string;
    readonly validateActorInTransaction: InitialActorFence;
  }) {
    const intent = input.intent;
    if (!intent.externalMessageId || !['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) return null;
    const context = parseChannelOperationContext(intent.selectedContext);
    const stored = this.initialRequestRecord(intent.request);
    const canonicalRequest = stored?.canonicalRequest;
    const renderedText = stored?.renderedText;
    const original = this.originalConversationSnapshot(stored?.originalConversation);
    const originalActorName = stored?.originalActorName;
    if (!context || !original || typeof renderedText !== 'string' || !renderedText || typeof originalActorName !== 'string' || !originalActorName) {
      await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(intent.id, 'RECORDED');
    }
    const conversation = await this.prisma.conversation.findFirst({ where: { id: intent.conversationId, buId: intent.buId } });
    if (!conversation || !canonicalRequest || typeof canonicalRequest !== 'object' || Array.isArray(canonicalRequest)) {
      throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    }
    const acceptanceInput: MessageAcceptanceInput = {
      externalMessageId: intent.externalMessageId, providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId, generation: context.generation, pairingEpoch: context.pairingEpoch,
      buId: context.buId, channelOrigin: context.channelOrigin, contact: conversation.contact,
      contactType: conversation.contactType, conversationId: conversation.id, direction: 'OUT', messageType: 'TEXTO',
      content: renderedText, authorUserId: intent.actorId, authorName: originalActorName, senderResult: true,
    };
    const complete = (tx: Prisma.TransactionClient) => this.acceptance.acceptInTransaction(tx, acceptanceInput,
      async (transaction, priorExists) => {
        if (!await this.resolver.validateAcceptedOperationContextInTransaction(transaction, context, intent.selectedContext)) {
          throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
        }
        if (!await input.validateActorInTransaction(transaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        await this.finalizeInitialInTransaction(transaction, {
          conversationId: conversation.id, buId: conversation.buId, intent, ownerNonce: intent.ownerNonce,
          originalConversation: original, actorId: intent.actorId, actorName: originalActorName,
          conversation, externalMessageId: intent.externalMessageId!, priorExists,
        });
      });
    try {
      const accepted = await this.prisma.$transaction(complete, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (accepted.creationWinner) {
        try {
          this.realtime.publicarNaBu(conversation.buId, {
            tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
            direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
          });
        } catch { /* Durable local completion is authoritative; realtime is best effort. */ }
      }
      return accepted.message;
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        const prior = await this.readBack(conversation, context, intent.externalMessageId);
        if (prior) {
          try {
            const retried = await this.prisma.$transaction(complete, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
            if (retried.creationWinner) {
              try {
                this.realtime.publicarNaBu(conversation.buId, {
                  tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
                  direcao: 'OUT', canal: retried.message.channelOrigin, naoLidas: retried.conversation.unreadCount,
                });
              } catch { /* Durable local completion is authoritative; realtime is best effort. */ }
            }
            return retried.message;
          } catch {
            await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
            throw this.initialLocalIncomplete(intent.id, 'RECORDED');
          }
        }
      } else {
        const message = await this.readBack(conversation, context, intent.externalMessageId);
        const current = await this.admissions.getInitialForScopedAttempt({ id: intent.id, conversationId: intent.conversationId, buId: intent.buId }).catch(() => null);
        if (message && current?.state === 'SUCCEEDED' && current.externalMessageId === intent.externalMessageId) return message;
      }
      await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(intent.id, 'RECORDED');
    }
  }

  /** Dispatches one already-reserved initial intent through the common channel and Message owners. */
  async sendInitial(input: {
    readonly conversationId: string;
    readonly buId: string;
    readonly channelId: string;
    readonly kind: ChannelMessage['kind'];
    readonly intent: InitialMessageIntent;
    readonly ownerNonce: string;
    readonly operation: ResolvedChannelOperation;
    readonly payload: ChannelMessage;
    readonly request: Prisma.InputJsonValue;
    readonly originalConversation: InitialConversationSnapshot;
    readonly actorId: string;
    readonly actorName: string;
    readonly validateActorInTransaction: InitialActorFence;
  }) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: input.conversationId, buId: input.buId },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    let operation: ResolvedChannelOperation;
    try {
      operation = await this.resolver.resolveForInitial({
        conversationId: conversation.id, buId: conversation.buId, channelId: input.channelId, kind: input.kind,
      });
    } catch (error) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
      throw error;
    }
    if (!sameContext(operation.context, input.operation.context)) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
    }

    let claimed = false;
    type InitialClaimOutcome = 'NOT_ATTEMPTED' | 'CLAIMED' | 'NOT_CLAIMED' | 'UNKNOWN';
    const claimStatus: { value: InitialClaimOutcome } = { value: 'NOT_ATTEMPTED' };
    const claimOutcome = (): InitialClaimOutcome => claimStatus.value;
    let claimPromise: Promise<boolean> | null = null;
    const beforeDispatch = async () => {
      if (!claimPromise) {
        claimPromise = this.admissions.claimInitial({
          id: input.intent.id,
          ownerNonce: input.ownerNonce,
          validate: async (tx, selectedContext, request) => {
            if (canonicalJson(request) !== canonicalJson(input.request)) return false;
            if (!await this.validateDispatchContext(tx, operation.context, selectedContext, conversation.id, input.kind === 'text')) return false;
            return input.validateActorInTransaction(tx);
          },
        }).then((value) => { claimStatus.value = value ? 'CLAIMED' : 'NOT_CLAIMED'; return value; }, () => { claimStatus.value = 'UNKNOWN'; return false; });
      }
      claimed = await claimPromise;
      return claimed;
    };

    let result: ChannelSendResult;
    try {
      result = await operation.channel.sendMessage(input.payload, { purpose: 'initial', beforeDispatch });
    } catch {
      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
    }

    if (result.outcome === 'BLOCKED') {
      if (claimOutcome() === 'NOT_ATTEMPTED' || claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'CLAIMED') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw this.blocked(result.reason);
    }
    if (result.outcome === 'REJECTED') {
      if (claimOutcome() === 'NOT_ATTEMPTED' || claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'CLAIMED') await this.admissions.rejectInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
    }
    if (result.outcome === 'UNKNOWN') {
      if (!claimed) {
        if (claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
        else if (claimOutcome() === 'UNKNOWN') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
        throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_UNCONFIRMED', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
      }
      let classified = false;
      try {
        classified = await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      } catch { /* a lost write acknowledgment needs a positive scoped readback */ }
      if (!classified) {
        const persisted = await this.admissions.getInitialForScopedAttempt({
          id: input.intent.id, conversationId: input.conversationId, buId: input.buId,
        }).catch(() => null);
        classified = persisted?.ownerNonce === input.ownerNonce && persisted.state === 'AMBIGUOUS'
          && persisted.slotReleasedAt === null;
      }
      if (!classified) {
        throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_UNCONFIRMED', outcome: 'UNKNOWN', attemptId: input.intent.id, error: FIXED_UNKNOWN });
      }
      throw new ConflictException({ code: 'INITIAL_SEND_AMBIGUOUS', outcome: 'AMBIGUOUS', state: 'AMBIGUOUS', attemptId: input.intent.id, error: FIXED_UNKNOWN });
    }
    if (!claimed) {
      if (claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'UNKNOWN') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_FENCE_MISSING', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
    }

    let receipt: boolean;
    try {
      receipt = await this.admissions.recordInitialExternalAccepted({
        id: input.intent.id, ownerNonce: input.ownerNonce, externalMessageId: result.externalMessageId,
      });
    } catch {
      const exact = await this.admissions.getInitialForScopedAttempt({
        id: input.intent.id, conversationId: input.conversationId, buId: input.buId,
      }).catch(() => null);
      receipt = exact?.ownerNonce === input.ownerNonce && exact.externalMessageId === result.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(exact.state);
        if (!receipt) throw this.initialLocalIncomplete(input.intent.id, 'UNCONFIRMED', 'INITIAL_RECEIPT_UNCONFIRMED');
    }
    if (!receipt) {
      await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(input.intent.id, 'UNCONFIRMED', 'INITIAL_RECEIPT_UNCONFIRMED');
    }

    const acceptanceInput = this.initialAcceptanceInput(input, conversation, operation.context, result.externalMessageId);
    const completeInitial = async (transaction: Prisma.TransactionClient, priorExists: boolean) => {
      const valid = await this.resolver.validateAcceptedOperationContextInTransaction(transaction, operation.context, input.intent.selectedContext);
      if (!valid) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      if (!await input.validateActorInTransaction(transaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
      await this.finalizeInitialInTransaction(transaction, {
        ...input, conversation, externalMessageId: result.externalMessageId, priorExists,
      });
    };
    let accepted: Awaited<ReturnType<MessageAcceptanceService['acceptInTransaction']>>;
    try {
      accepted = await this.prisma.$transaction(async (tx) => this.acceptance.acceptInTransaction(
        tx,
        acceptanceInput,
        completeInitial,
      ), { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        const prior = await this.findConfirmedOutbound({
          providerResourceIdentityId: operation.context.providerResourceIdentityId,
          externalMessageId: result.externalMessageId,
          conversationId: conversation.id, buId: conversation.buId,
          contact: conversation.contact, channelOrigin: operation.context.channelOrigin,
        }).catch(() => null);
        if (prior) {
          try {
            accepted = await this.prisma.$transaction(async (tx) => this.acceptance.acceptInTransaction(
              tx,
              acceptanceInput,
              completeInitial,
            ), { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
          } catch {
            await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
            throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
          }
        } else {
          await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
          throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
        }
      } else {
        const message = await this.readBack(conversation, operation.context, result.externalMessageId).catch(() => null);
        if (message) {
          const row = await this.admissions.getInitialForScopedAttempt({
            id: input.intent.id, conversationId: conversation.id, buId: conversation.buId,
          }).catch(() => null);
          if (row?.state === 'SUCCEEDED' && row.externalMessageId === result.externalMessageId) {
            return message;
          }
        }
        await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
        throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
      }
    }

    if (accepted.creationWinner) {
      try {
        this.realtime.publicarNaBu(conversation.buId, {
          tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
          direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
        });
      } catch { /* Message commit is authoritative; realtime is best effort. */ }
    }
    return accepted.message;
  }

  async send(input: SendOutboundInput) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: input.conversationId, buId: input.buId },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });

    let operation: ResolvedChannelOperation;
    try {
      operation = input.ingress
        ? await this.resolver.resolveForIngress({
            conversationId: conversation.id, buId: conversation.buId, ...input.ingress,
          })
        : await this.resolver.resolveForConversation({ conversationId: conversation.id, buId: conversation.buId });
    } catch (error) {
      if (error instanceof HttpException) throw this.asBlocked(error);
      throw error;
    }

    if (operation.context.requiresWindow && !(await this.windows.inspect({
      conversationId: conversation.id,
      providerResourceIdentityId: operation.context.providerResourceIdentityId,
    })).open) {
      throw new ConflictException({ code: 'JANELA_FECHADA', outcome: 'BLOCKED', error: 'Fora da janela de 24h da última mensagem recebida.' });
    }

    const attribution = input.attribution;
    const actorId = attribution.kind === 'BFF' ? attribution.userId
      : attribution.kind === 'PUBLIC' ? `public:${conversation.buId}`
        : `bot:${attribution.name}`;
    const reservation = await this.admissions.reserveOrdinary({
      conversationId: conversation.id,
      buId: conversation.buId,
      caller: attribution.kind,
      actorId,
      ownerNonce: randomUUID(),
      selectedContext: operation.context as unknown as Prisma.InputJsonValue,
    });
    let claimed = false;
    let claimPromise: Promise<boolean> | null = null;
    const beforeDispatch = async () => {
      if (!claimPromise) {
        claimPromise = this.admissions.claimOrdinary({
          id: reservation.admission.id,
          ownerNonce: reservation.ownerNonce,
          validate: (tx, selectedContext) => this.validateDispatchContext(
            tx, operation.context, selectedContext, conversation.id,
          ),
        });
      }
      claimed = await claimPromise;
      return claimed;
    };

    let result: ChannelSendResult;
    try {
      result = await operation.channel.sendMessage(
        { kind: 'text', recipientRef: conversation.contact, text: input.text },
        { beforeDispatch },
      );
    } catch {
      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
    }
    if (result.outcome === 'BLOCKED') {
      if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
      else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      throw this.blocked(result.reason);
    }
    if (result.outcome === 'REJECTED') {
      if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
      else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
    }
    if (result.outcome === 'UNKNOWN') {
      if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'UNCERTAIN' });
      else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      return this.finishUnknown(input, conversation, operation.context, result);
    }
    if (!claimed) {
      // An adapter may not report acceptance unless the durable owner fence ran.
      await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      throw new ServiceUnavailableException({ code: 'OUTBOUND_DISPATCH_FENCE_MISSING', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
    }

    const contextState = await this.contextState(operation.context);
    if (contextState !== 'CURRENT') {
      const message = await this.readBack(conversation, operation.context, result.externalMessageId);
      try { await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: message ? 'SETTLED' : 'UNCERTAIN' }); }
      catch { /* Keep the confirmed provider result projection below. */ }
      throw this.acceptedIncomplete(contextState, message ? 'RECORDED' : 'UNCONFIRMED');
    }

    const acceptanceInput = this.acceptanceInput(input, conversation, operation.context, result.externalMessageId);
    let accepted: Awaited<ReturnType<MessageAcceptanceService['accept']>>;
    try {
      accepted = await this.acceptance.accept(acceptanceInput);
    } catch {
      const [after, message] = await Promise.all([
        this.contextState(operation.context),
        this.readBack(conversation, operation.context, result.externalMessageId),
      ]);
      try { await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: message ? 'SETTLED' : 'UNCERTAIN' }); }
      catch { /* Preserve the confirmed remote ACK and local Message readback. */ }
      throw this.acceptedIncomplete(after, message ? 'RECORDED' : 'UNCONFIRMED');
    }

    let settled = false;
    try {
      settled = await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
    } catch {
      // The provider ACK and accepted Message are already durable; settlement uncertainty
      // must preserve that projection without retrying the provider operation.
    }
    if (!settled) throw this.acceptedIncomplete(await this.contextState(operation.context), 'RECORDED');

    let localFailure = false;
    if (accepted.creationWinner) {
      try {
        this.realtime.publicarNaBu(conversation.buId, {
          tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
          direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
        });
      } catch { localFailure = true; }
    }
    try {
      await this.finalizeOutbound({
        conversationId: conversation.id, buId: conversation.buId, contact: conversation.contact,
        contactType: conversation.contactType, attribution: input.attribution,
      });
    } catch { localFailure = true; }
    if (localFailure) {
      throw this.acceptedIncomplete(await this.contextState(operation.context), 'RECORDED');
    }
    return accepted.message;
  }

  private initialAcceptanceInput(
    input: { actorId: string; actorName: string; payload: ChannelMessage },
    conversation: OutboundConversation,
    context: ChannelOperationContext,
    externalMessageId: string,
  ): MessageAcceptanceInput {
    const content = input.payload.kind === 'text' ? input.payload.text : input.payload.template.renderedText;
    return {
      externalMessageId, providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId, generation: context.generation, pairingEpoch: context.pairingEpoch,
      buId: context.buId, channelOrigin: context.channelOrigin, contact: conversation.contact,
      contactType: conversation.contactType, conversationId: conversation.id, direction: 'OUT',
      messageType: 'TEXTO', content, authorUserId: input.actorId, authorName: input.actorName, senderResult: true,
    };
  }

  private async finalizeInitialInTransaction(
    tx: Prisma.TransactionClient,
    input: {
      conversationId: string; buId: string; intent: InitialMessageIntent; ownerNonce: string;
      originalConversation: InitialConversationSnapshot; actorId: string; actorName: string;
      conversation: OutboundConversation; externalMessageId: string; priorExists: boolean;
    },
  ): Promise<void> {
    const contactLockKey = JSON.stringify([input.buId, input.conversation.contact]);
    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactLockKey}, 0))::text AS locked`;
    const rows = await tx.$queryRaw<Array<{ id: string; updated_at: Date; status: string; attendant_user_id: string | null; attendant_name: string | null; attendant_origin: string | null }>>`
      SELECT id, updated_at, status::text AS status, attendant_user_id
        , attendant_name, attendant_origin
      FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId} FOR UPDATE
    `;
    await tx.$queryRaw`SELECT id FROM initial_message_intents WHERE id = ${input.intent.id} FOR UPDATE`;
    const intent = await tx.initialMessageIntent.findUnique({ where: { id: input.intent.id } });
    const current = rows[0];
    if (!current || !intent || intent.ownerNonce !== input.ownerNonce
      || intent.externalMessageId !== input.externalMessageId
      || !['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) {
      throw new ConflictException({ code: 'INITIAL_INTENT_CONTEXT_CHANGED' });
    }

    const original = input.originalConversation;
    const originalCas = current.updated_at.getTime() === original.updatedAt.getTime()
      && current.status === original.status && current.attendant_user_id === original.attendantUserId
      && current.attendant_name === original.attendantName && current.attendant_origin === original.attendantOrigin;
    const ownsSlot = intent.slotReleasedAt === null;
    const hasOwner = current.attendant_user_id !== null || current.attendant_name !== null || current.attendant_origin !== null;
    const canAssign = !input.priorExists && originalCas && ownsSlot && (!hasOwner || current.attendant_user_id === input.actorId);
    if (canAssign) {
      await tx.conversation.updateMany({
        where: {
          id: input.conversationId, buId: input.buId, updatedAt: original.updatedAt,
          status: original.status as never, attendantUserId: original.attendantUserId,
          attendantName: original.attendantName, attendantOrigin: original.attendantOrigin,
        },
        data: { status: 'IN_SERVICE', attendantUserId: input.actorId, attendantName: input.actorName, attendantOrigin: 'INTERNO' },
      });
    }
    const completed = await tx.$queryRaw<Array<{ id: string }>>`
      UPDATE initial_message_intents
      SET state = 'SUCCEEDED'::"InitialMessageIntentState",
          slot_released_at = CASE WHEN slot_released_at IS NULL THEN clock_timestamp() ELSE slot_released_at END,
          updated_at = clock_timestamp()
      WHERE id = ${input.intent.id}
        AND owner_nonce = ${input.ownerNonce}
        AND external_message_id = ${input.externalMessageId}
        AND state IN ('EXTERNAL_ACCEPTED'::"InitialMessageIntentState", 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'::"InitialMessageIntentState")
        AND slot_released_at IS NOT DISTINCT FROM ${intent.slotReleasedAt}
      RETURNING id
    `;
    if (completed.length !== 1) throw new ConflictException({ code: 'INITIAL_INTENT_CONTEXT_CHANGED' });
  }

  private async finishUnknown(
    input: SendOutboundInput,
    conversation: OutboundConversation,
    context: ChannelOperationContext,
    result: Extract<ChannelSendResult, { outcome: 'UNKNOWN' }>,
  ): Promise<never> {
    if (result.evidence === 'TRANSPORT_UNCONFIRMED') {
      const state = await this.contextState(context);
      if (state === 'CHANGED') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
      }
      throw new BadRequestException({ code: result.legacyCode, outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
    }

    if (await this.contextState(context) === 'CHANGED') {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
    }

    try {
      await this.acceptance.recordAmbiguousOutbound(this.acceptanceInput(input, conversation, context));
    } catch {
      const state = await this.contextState(context);
      if (state === 'CHANGED') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
      }
      throw new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
    }

    const state = await this.contextState(context);
    if (state === 'CHANGED') {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'RECORDED', error: FIXED_UNKNOWN });
    }
    throw new ConflictException({
      code: 'EXTERNAL_MESSAGE_ID_MISSING', outcome: 'AMBIGUOUS_SEND_RECORDED', evidence: 'ACK_WITHOUT_ID',
      diagnosticPersistence: 'RECORDED', error: 'O canal aceitou o envio sem confirmar o ID externo. Verifique a conversa antes de tentar novamente.',
    });
  }

  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
    externalMessageId: string,
  ): MessageAcceptanceInput;
  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
  ): Omit<MessageAcceptanceInput, 'externalMessageId'>;
  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
    externalMessageId?: string,
  ): MessageAcceptanceInput | Omit<MessageAcceptanceInput, 'externalMessageId'> {
    const attribution = input.attribution;
    return {
      ...(externalMessageId ? { externalMessageId } : {}),
      providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId,
      generation: context.generation,
      pairingEpoch: context.pairingEpoch,
      buId: context.buId,
      channelOrigin: context.channelOrigin,
      contact: conversation.contact,
      contactType: conversation.contactType,
      conversationId: conversation.id,
      direction: 'OUT',
      messageType: 'TEXTO',
      content: input.text,
      authorUserId: attribution.kind === 'BFF' ? attribution.userId || null : null,
      authorName: attribution.name,
      senderResult: true,
    };
  }

  private async contextState(context: ChannelOperationContext) {
    try { return await this.resolver.contextAfterDispatch(context); }
    catch { return 'UNKNOWN' as const; }
  }

  private async validateDispatchContext(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
    conversationId: string,
    checkWindow = true,
  ): Promise<boolean> {
    const current = await this.resolver.validateOperationContextInTransaction(tx, expected, selectedValue);
    if (!current) return false;
    if (!checkWindow || !expected.requiresWindow) return true;
    return (await this.windows.inspectInTransaction(tx, {
      conversationId,
      providerResourceIdentityId: expected.providerResourceIdentityId,
    })).open;
  }

  private initialRequestRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value) ? value as Record<string, Prisma.JsonValue> : null;
  }

  private originalConversationSnapshot(value: Prisma.JsonValue | undefined): InitialConversationSnapshot | null {
    if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
    const row = value as Record<string, Prisma.JsonValue>;
    const updatedAt = typeof row.updatedAt === 'string' ? new Date(row.updatedAt) : null;
    if (!updatedAt || !Number.isFinite(updatedAt.getTime()) || typeof row.status !== 'string'
      || row.attendantUserId !== null && typeof row.attendantUserId !== 'string'
      || row.attendantName !== null && typeof row.attendantName !== 'string'
      || row.attendantOrigin !== null && typeof row.attendantOrigin !== 'string') return null;
    return { updatedAt, status: row.status as InitialConversationSnapshot['status'],
      attendantUserId: row.attendantUserId as string | null, attendantName: row.attendantName as string | null,
      attendantOrigin: row.attendantOrigin as InitialConversationSnapshot['attendantOrigin'] };
  }

  private async readBack(
    conversation: { id: string; buId: string; contact: string },
    context: ChannelOperationContext,
    externalMessageId: string,
  ) {
    try {
      return await this.findConfirmedOutbound({
        providerResourceIdentityId: context.providerResourceIdentityId,
        externalMessageId, conversationId: conversation.id, buId: conversation.buId,
        contact: conversation.contact, channelOrigin: context.channelOrigin,
      });
    } catch { return null; }
  }

  private async findConfirmedOutbound(input: {
    providerResourceIdentityId: string; externalMessageId: string; conversationId: string;
    buId: string; contact: string; channelOrigin: 'OFICIAL' | 'NAO_OFICIAL';
  }) {
    const message = await this.prisma.message.findUnique({
      where: { providerResourceIdentityId_externalId: {
        providerResourceIdentityId: input.providerResourceIdentityId,
        externalId: input.externalMessageId,
      } }, include: { conversation: true },
    });
    if (!message || message.direction !== 'OUT' || message.buId !== input.buId
      || message.channelOrigin !== input.channelOrigin || message.conversation.contact !== input.contact
      || message.conversationId !== input.conversationId) return null;
    return message;
  }

  private async finalizeOutbound(input: {
    conversationId: string; buId: string; contact: string; contactType: 'PESSOA' | 'GRUPO'; attribution: OutboundAttribution;
  }) {
    return this.prisma.$transaction(async (tx) => {
      await tx.$queryRaw`SELECT id FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId} FOR UPDATE`;
      const current = await tx.conversation.findFirst({
        where: { id: input.conversationId, buId: input.buId, contact: input.contact },
      });
      if (!current || current.contactType !== input.contactType) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
      if (input.attribution.kind === 'BOT') return current;

      const hasOwner = current.attendantUserId !== null || current.attendantName !== null || current.attendantOrigin !== null;
      return tx.conversation.update({ where: { id: current.id }, data: {
        lastMessageAt: new Date(),
        status: input.contactType === 'GRUPO' ? undefined : 'IN_SERVICE',
        ...(hasOwner || input.contactType === 'GRUPO' ? {} : input.attribution.kind === 'BFF'
          ? { attendantUserId: input.attribution.userId || null, attendantName: input.attribution.name, attendantOrigin: 'INTERNO' }
          : { attendantUserId: null, attendantName: input.attribution.name, attendantOrigin: 'EXTERNO' }),
      } });
    });
  }

  private asBlocked(error: HttpException): HttpException {
    const response = error.getResponse();
    const detail = typeof response === 'object' && response !== null ? response as Record<string, unknown> : { error: response };
    return new HttpException({ ...detail, outcome: 'BLOCKED' }, error.getStatus());
  }

  private blocked(reason: Extract<ChannelSendResult, { outcome: 'BLOCKED' }>['reason']): HttpException {
    if (reason === 'CANAL_AUSENTE') return new BadRequestException({ code: reason, outcome: 'BLOCKED', error: 'Esta BU não tem canal conectado.' });
    return new ConflictException({ code: reason, outcome: 'BLOCKED', error: 'O canal selecionado não está disponível para envio.' });
  }

  private acceptedIncomplete(contextState: 'CURRENT' | 'CHANGED' | 'UNKNOWN', localMessageState: 'RECORDED' | 'UNCONFIRMED'): HttpException {
    if (contextState === 'CHANGED') {
      return new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
    }
    return new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
  }

  private initialLocalIncomplete(attemptId: string, receiptPersistence: 'RECORDED' | 'UNCONFIRMED', code = 'INITIAL_LOCAL_ACCEPTANCE_UNCONFIRMED') {
    return new ServiceUnavailableException({
      code, outcome: 'ACCEPTED_LOCAL_INCOMPLETE', attemptId, state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED',
      providerAcceptance: 'CONFIRMED', receiptPersistence,
      localMessageState: 'UNCONFIRMED', recoveryAction: 'RECONCILE', error: FIXED_LOCAL_INCOMPLETE,
    });
  }
}

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (value && typeof value === 'object') {
    const record = value as Record<string, unknown>;
    return `{${Object.keys(record).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(record[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}

function sameContext(a: ChannelOperationContext, b: ChannelOperationContext): boolean {
  return canonicalJson(a) === canonicalJson(b);
}

```

### api-app/src/domain/inbox/message-acceptance.service.ts

SHA256 `71194c70b12cb920054586a7a86266d90f8eca0b7008b1b5688627e0694979f1`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { redactProviderData } from '../channels/safe-redaction';

export interface VerifiedResourceContext {
  providerResourceIdentityId: string;
  buId: string;
  channelId: string;
  generation: number;
  pairingEpoch: number;
  channelOrigin: 'OFICIAL' | 'NAO_OFICIAL';
}

export interface MessageAcceptanceInput extends VerifiedResourceContext {
  externalMessageId: string;
  contact: string;
  contactType: 'PESSOA' | 'GRUPO';
  displayName?: string | null;
  conversationId?: string;
  direction: 'IN' | 'OUT';
  messageType: 'TEXTO' | 'IMAGEM' | 'AUDIO' | 'VIDEO' | 'DOCUMENTO' | 'OUTRO';
  status?: 'RECEBIDA' | 'ENVIADA' | 'ENTREGUE' | 'LIDA' | 'FALHOU';
  content?: string | null;
  /** Present only when derived from a verified signed Meta inbound message. */
  officialInboundAt?: Date | null;
  authorUserId?: string | null;
  authorName?: string | null;
  /** True only for an authenticated sender result; echo payloads cannot assert authorship. */
  senderResult?: boolean;
}

export interface MessageAcceptanceResult {
  conversation: Prisma.ConversationGetPayload<object>;
  message: Prisma.MessageGetPayload<object>;
  creationWinner: boolean;
  reconciled: boolean;
  conversationCreated: boolean;
  reopened: boolean;
}

/** Sole transactional owner of keyed Message creation and sender/echo reconciliation. */
@Injectable()
export class MessageAcceptanceService {
  constructor(private readonly prisma: PrismaService) {}

  /** Persist only an allowlist-redacted, identity-scoped diagnostic while the resource fence is held. */
  async persistVerifiedDiagnostic(
    context: VerifiedResourceContext,
    eventType: string,
    safeMetadata: Record<string, unknown>,
  ): Promise<void> {
    if (!/^[A-Za-z0-9_.:-]{1,100}$/.test(eventType)) throw new BadRequestException({ code: 'INVALID_EVENT_TYPE' });
    await this.prisma.$transaction(async (tx) => {
      await this.lockAndValidateCurrentIdentity(tx, context);
      await tx.webhookEvent.create({
        data: {
          buId: context.buId, channel: context.channelOrigin, eventType,
          payload: redactProviderData(safeMetadata) as Prisma.InputJsonValue,
        },
      });
    });
  }

  /** Persist safe identity/state metadata while fenced, even before own-number proof. */
  async persistCurrentResourceMetadata(
    context: VerifiedResourceContext,
    eventType: string,
    safeMetadata: Record<string, unknown>,
  ): Promise<void> {
    if (!/^[A-Za-z0-9_.:-]{1,100}$/.test(eventType)) throw new BadRequestException({ code: 'INVALID_EVENT_TYPE' });
    await this.prisma.$transaction(async (tx) => {
      const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null }>>`
        SELECT id, bu_id, current_channel_id FROM provider_resource_identities
        WHERE id = ${context.providerResourceIdentityId} FOR SHARE
      `;
      if (!rows[0] || rows[0].bu_id !== context.buId || rows[0].current_channel_id !== context.channelId) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
      const channel = await tx.buChannel.findFirst({ where: { id: context.channelId, buId: context.buId, type: context.channelOrigin, generation: context.generation, pairingEpoch: context.pairingEpoch }, select: { id: true } });
      if (!channel) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
      await tx.webhookEvent.create({ data: { buId: context.buId, channel: context.channelOrigin, eventType, payload: redactProviderData(safeMetadata) as Prisma.InputJsonValue } });
    });
  }

  async accept(input: MessageAcceptanceInput): Promise<MessageAcceptanceResult> {
    this.validateAcceptanceInput(input);
    try {
      return await this.prisma.$transaction((tx) => this.acceptInTransaction(tx, input), {
        isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted,
      });
    } catch (error) {
      // A concurrent insert may win after our initial lookup. The whole failed
      // transaction has rolled back before the exact-key readback and retry.
      if (!isUniqueViolation(error)) throw error;
      const prior = await this.prisma.message.findUnique({
        where: { providerResourceIdentityId_externalId: {
          providerResourceIdentityId: input.providerResourceIdentityId,
          externalId: input.externalMessageId,
        } }, include: { conversation: true },
      });
      if (!prior) throw error;
      return this.prisma.$transaction((tx) => this.acceptInTransaction(tx, input), {
        isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted,
      });
    }
  }

  /**
   * The same Message owner primitive used by normal acceptance and initial-send
   * completion. The caller owns the short transaction; no provider I/O belongs
   * here. `beforeConversationMutation` runs after identity validation and before
   * this method mutates the conversation timestamp, allowing initial completion
   * to apply its captured pre-HTTP owner/status CAS in the required order.
   */
  async acceptInTransaction(
    tx: Prisma.TransactionClient,
    input: MessageAcceptanceInput,
    beforeConversationMutation?: (tx: Prisma.TransactionClient, priorExists: boolean) => Promise<void>,
  ): Promise<MessageAcceptanceResult> {
    this.validateAcceptanceInput(input);
    await this.lockAndValidateCurrentIdentity(tx, input);
    const key = { providerResourceIdentityId: input.providerResourceIdentityId, externalId: input.externalMessageId };
    const prior = await tx.message.findUnique({ where: { providerResourceIdentityId_externalId: key }, include: { conversation: true } });
    await beforeConversationMutation?.(tx, Boolean(prior));
    if (prior) return this.reconcile(tx, prior, input);

    let conversation: Prisma.ConversationGetPayload<object>;
    let conversationCreated = false;
    let reopened = false;
    if (input.direction === 'IN') {
      const acceptedConversation = await this.acceptIncomingConversation(tx, input);
      conversation = acceptedConversation.conversation;
      conversationCreated = acceptedConversation.created;
      reopened = acceptedConversation.reopened;
    } else {
      conversation = await this.loadOutboundConversation(tx, input);
    }
    const message = await tx.message.create({
      data: {
        conversationId: conversation.id,
        buId: input.buId,
        direction: input.direction,
        messageType: input.messageType,
        content: input.content ?? null,
        channelOrigin: input.channelOrigin,
        status: input.status ?? (input.direction === 'IN' ? 'RECEBIDA' : 'ENVIADA'),
        externalId: input.externalMessageId,
        providerResourceIdentityId: input.providerResourceIdentityId,
        officialInboundAt: this.qualifiedOfficialTimestamp(input),
        authorUserId: input.senderResult ? input.authorUserId ?? null : null,
        authorName: input.senderResult ? input.authorName ?? null : null,
      },
    });
    if (input.direction === 'IN') await this.confirmInboundReceipt(tx, input);
    return { conversation, message, creationWinner: true, reconciled: false, conversationCreated, reopened };
  }

  private validateAcceptanceInput(input: MessageAcceptanceInput): void {
    if (!input.externalMessageId?.trim()) throw new BadRequestException({ code: 'EXTERNAL_MESSAGE_ID_REQUIRED' });
    if (!input.providerResourceIdentityId || !input.channelId || !input.buId) {
      throw new BadRequestException({ code: 'VERIFIED_RESOURCE_REQUIRED' });
    }
  }

  private async confirmInboundReceipt(tx: Prisma.TransactionClient, input: MessageAcceptanceInput): Promise<void> {
    const now = new Date();
    await tx.buChannel.updateMany({
      where: { id: input.channelId, buId: input.buId, generation: input.generation, pairingEpoch: input.pairingEpoch },
      data: { receiptVerifiedAt: now },
    });
    const currentChannel = await tx.buChannel.findUnique({ where: { id: input.channelId }, select: { currentAttemptId: true, providerConnectionState: true, type: true } });
    const providerReady = currentChannel?.providerConnectionState === 'SUBSCRIBED'
      || (input.channelOrigin === 'NAO_OFICIAL' && currentChannel?.providerConnectionState === 'CONNECTED');
    if (providerReady) {
      await tx.buChannel.updateMany({ where: { id: input.channelId, generation: input.generation, pairingEpoch: input.pairingEpoch }, data: { status: 'CONECTADO', connectedAt: now } });
    }
    if (currentChannel?.type === 'NAO_OFICIAL' && currentChannel.currentAttemptId && currentChannel.providerConnectionState === 'CONNECTED') {
      await tx.buChannel.updateMany({ where: { id: input.channelId, generation: input.generation, pairingEpoch: input.pairingEpoch }, data: { status: 'CONECTADO', connectedAt: now } });
      await tx.channelRegistrationAttempt.updateMany({ where: { id: currentChannel.currentAttemptId, generation: input.generation, pairingEpoch: input.pairingEpoch, state: { in: ['PENDING_NUMBER', 'PENDING_RECEIPT'] } }, data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', version: { increment: 1 } } });
    }
    if (input.channelOrigin === 'OFICIAL' && currentChannel?.currentAttemptId && providerReady) {
      await tx.channelRegistrationAttempt.updateMany({
        where: { id: currentChannel.currentAttemptId, state: 'PENDING_RECEIPT', stage: 'SUBSCRIBED' },
        data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', version: { increment: 1 } },
      });
    }
  }

  private qualifiedOfficialTimestamp(input: MessageAcceptanceInput): Date | null {
    const timestamp = input.officialInboundAt;
    if (input.direction !== 'IN' || input.channelOrigin !== 'OFICIAL' || !(timestamp instanceof Date)) return null;
    const value = timestamp.getTime();
    return Number.isSafeInteger(value) && value > 0 && value <= Date.now() ? timestamp : null;
  }

  /** Persist an explicitly ambiguous result after a provider accepted a send but returned no key. */
  async recordAmbiguousOutbound(input: Omit<MessageAcceptanceInput, 'externalMessageId' | 'status'>): Promise<Prisma.MessageGetPayload<object>> {
    if (input.direction !== 'OUT' || !input.senderResult) throw new BadRequestException({ code: 'OUTBOUND_RESULT_REQUIRED' });
    return this.prisma.$transaction(async (tx) => {
      await this.lockAndValidateCurrentIdentity(tx, input);
      const conversation = await tx.conversation.findFirst({ where: { id: input.conversationId, buId: input.buId, contact: input.contact } });
      if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
      await tx.conversation.update({ where: { id: conversation.id }, data: { lastMessageAt: new Date() } });
      return tx.message.create({ data: {
        conversationId: conversation.id, buId: input.buId, direction: 'OUT', messageType: input.messageType,
        content: input.content ?? null, channelOrigin: input.channelOrigin, status: 'FALHOU', externalId: null,
        providerResourceIdentityId: input.providerResourceIdentityId, authorUserId: input.authorUserId ?? null,
        authorName: input.authorName ?? null,
      } });
    });
  }

  private async lockAndValidateCurrentIdentity(tx: Prisma.TransactionClient, input: VerifiedResourceContext): Promise<void> {
    // Retirement/renewal must update this same identity row before changing the
    // channel epoch. The lock is held through message commit as the ingress fence.
    const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null }>>`
      SELECT id, bu_id, current_channel_id
      FROM provider_resource_identities
      WHERE id = ${input.providerResourceIdentityId}
      FOR SHARE
    `;
    const identity = rows[0];
    if (!identity || identity.bu_id !== input.buId || identity.current_channel_id !== input.channelId) {
      throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
    }
    const channel = await tx.buChannel.findFirst({
      where: {
        id: input.channelId, buId: input.buId, generation: input.generation,
        pairingEpoch: input.pairingEpoch, ownNumberVerified: true, verifiedEpoch: input.pairingEpoch,
      }, select: { id: true, type: true, currentAttemptId: true },
    });
    if (!channel || channel.type !== input.channelOrigin) {
      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
    }
  }

  private async acceptIncomingConversation(tx: Prisma.TransactionClient, input: MessageAcceptanceInput) {
    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${JSON.stringify([input.buId, input.contact])}, 0))::text AS locked`;
    const existing = await tx.conversation.findUnique({
      where: { buId_contact: { buId: input.buId, contact: input.contact } },
    });
    if (input.conversationId && existing?.id !== input.conversationId) {
      throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    }
    const reopens = existing?.status === 'CLOSED' && input.contactType === 'PESSOA';
    const conversation = await tx.conversation.upsert({
      where: { buId_contact: { buId: input.buId, contact: input.contact } },
      create: {
        buId: input.buId, contact: input.contact, contactType: input.contactType,
        displayName: input.displayName ?? null,
        status: 'QUEUED', unreadCount: 1, lastMessageAt: new Date(),
      },
      update: {
        displayName: input.displayName ?? undefined,
        lastMessageAt: new Date(), unreadCount: { increment: 1 },
        status: reopens ? 'QUEUED' : undefined,
        attendantUserId: reopens ? null : undefined,
        attendantName: reopens ? null : undefined,
        attendantOrigin: reopens ? null : undefined,
      },
    });
    return { conversation, created: !existing, reopened: Boolean(reopens) };
  }

  private async loadOutboundConversation(tx: Prisma.TransactionClient, input: MessageAcceptanceInput) {
    if (!input.conversationId && input.senderResult) throw new BadRequestException({ code: 'CONVERSATION_REQUIRED' });
    if (input.conversationId) {
      const conversation = await tx.conversation.findFirst({
        where: { id: input.conversationId, buId: input.buId, contact: input.contact },
      });
      if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
      return tx.conversation.update({ where: { id: conversation.id }, data: { lastMessageAt: new Date() } });
    }
    // An authenticated provider echo can arrive before our send result and can
    // be the first observed message for this contact. Create an OUT-only
    // conversation with zero unread; an authenticated sender result above must
    // always name an already-authorized conversation.
    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${JSON.stringify([input.buId, input.contact])}, 0))::text AS locked`;
    return tx.conversation.upsert({
      where: { buId_contact: { buId: input.buId, contact: input.contact } },
      create: {
        buId: input.buId, contact: input.contact, contactType: input.contactType,
        status: 'QUEUED', unreadCount: 0, lastMessageAt: new Date(),
      },
      update: { lastMessageAt: new Date() },
    });
  }

  private async reconcile(
    tx: Prisma.TransactionClient,
    prior: Prisma.MessageGetPayload<{ include: { conversation: true } }>,
    input: MessageAcceptanceInput,
  ): Promise<MessageAcceptanceResult> {
    const conversation = prior.conversation;
    if (prior.buId !== input.buId || conversation.buId !== input.buId || conversation.contact !== input.contact
      || (input.conversationId && conversation.id !== input.conversationId)
      || prior.direction !== input.direction || prior.channelOrigin !== input.channelOrigin) {
      throw new ConflictException({ code: 'MESSAGE_IDENTITY_CONFLICT' });
    }
    let message = prior;
    const trustedSenderEnrichment = input.senderResult && !prior.authorUserId && !prior.authorName;
    if (trustedSenderEnrichment) {
      message = await tx.message.update({
        where: { id: prior.id },
        data: {
          authorUserId: input.authorUserId ?? null,
          authorName: input.authorName ?? null,
          content: input.content ?? prior.content,
        },
        include: { conversation: true },
      });
    }
    return { conversation, message, creationWinner: false, reconciled: true, conversationCreated: false, reopened: false };
  }
}

function isUniqueViolation(error: unknown): boolean {
  return error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002';
}

```

### api-app/src/domain/inbox/channel-window-policy.ts

SHA256 `46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';

const WINDOW_MS = 24 * 60 * 60 * 1000;

export function officialWindowState(timestamp: Date | null, now = new Date()): OfficialWindowState {
  if (!timestamp || !Number.isFinite(timestamp.getTime()) || timestamp.getTime() <= 0 || timestamp.getTime() > now.getTime()) {
    return { open: false, expiresAt: null };
  }
  const expiresAt = new Date(timestamp.getTime() + WINDOW_MS);
  return { open: expiresAt.getTime() > now.getTime(), expiresAt };
}

export function qualifiedMetaInboundTimestamp(value: unknown, now = new Date()): Date | null {
  if (typeof value !== 'string' && typeof value !== 'number') return null;
  if (typeof value === 'string' && !/^\d+$/.test(value)) return null;
  const seconds = typeof value === 'number' ? value : Number(value);
  if (!Number.isSafeInteger(seconds) || seconds <= 0) return null;
  const timestamp = new Date(seconds * 1000);
  if (!Number.isFinite(timestamp.getTime()) || timestamp.getTime() > now.getTime()) return null;
  return timestamp;
}

export interface OfficialInboundWindowEvidence {
  readonly direction: 'IN' | 'OUT';
  readonly channelOrigin: 'OFICIAL' | 'NAO_OFICIAL';
  readonly providerResourceIdentityId: string | null;
  readonly officialInboundAt: Date | null;
  /** Kept in callers' row shape to make it explicit that this is never a policy fallback. */
  readonly createdAt?: Date;
}

export interface OfficialWindowReference {
  readonly conversationId: string;
  readonly providerResourceIdentityId: string;
}

export interface OfficialWindowState {
  readonly open: boolean;
  readonly expiresAt: Date | null;
}

/** The single indexed query boundary used by outbound and every availability projection. */
@Injectable()
export class OfficialChannelWindowPolicy {
  constructor(private readonly prisma: PrismaService) {}

  async inspect(reference: OfficialWindowReference, now = new Date()): Promise<OfficialWindowState> {
    return this.inspectWith(this.prisma, reference, now);
  }

  /** Same current-resource query and expiry calculation inside a dispatch claim transaction. */
  async inspectInTransaction(
    tx: Prisma.TransactionClient,
    reference: OfficialWindowReference,
  ): Promise<OfficialWindowState> {
    const clock = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    if (!clock[0] || !(clock[0].now instanceof Date)) return { open: false, expiresAt: null };
    return this.inspectWith(tx, reference, clock[0].now);
  }

  private async inspectWith(
    client: PrismaService | Prisma.TransactionClient,
    reference: OfficialWindowReference,
    now: Date,
  ): Promise<OfficialWindowState> {
    const row = await client.message.findFirst({
      where: {
        conversationId: reference.conversationId,
        providerResourceIdentityId: reference.providerResourceIdentityId,
        direction: 'IN',
        channelOrigin: 'OFICIAL',
        officialInboundAt: { not: null, lte: now },
      },
      orderBy: [{ officialInboundAt: 'desc' }, { id: 'desc' }],
      select: { officialInboundAt: true },
    });
    return this.state(row?.officialInboundAt ?? null, now);
  }

  async inspectMany(references: readonly OfficialWindowReference[], now = new Date()): Promise<Map<string, OfficialWindowState>> {
    if (!references.length) return new Map();
    const conversationIds = references.map(({ conversationId }) => conversationId);
    const resourceIds = references.map(({ providerResourceIdentityId }) => providerResourceIdentityId);
    const rows = await this.prisma.$queryRaw<Array<{ conversation_id: string; official_inbound_at: Date }>>`
      SELECT requested.conversation_id, latest.official_inbound_at
      FROM unnest(ARRAY[${Prisma.join(conversationIds)}]::text[], ARRAY[${Prisma.join(resourceIds)}]::text[])
        AS requested(conversation_id, provider_resource_identity_id)
      CROSS JOIN LATERAL (
        SELECT message.official_inbound_at
        FROM messages AS message
        WHERE message.conversation_id = requested.conversation_id
          AND message.provider_resource_identity_id = requested.provider_resource_identity_id
          AND message.direction = 'IN' AND message.channel_origin = 'OFICIAL'
          AND message.official_inbound_at IS NOT NULL AND message.official_inbound_at <= ${now}
        ORDER BY message.official_inbound_at DESC, message.id DESC
        LIMIT 1
      ) AS latest
    `;
    const latest = new Map(rows.map((row) => [row.conversation_id, row.official_inbound_at]));
    return new Map(references.map((reference) => [reference.conversationId, this.state(latest.get(reference.conversationId) ?? null, now)]));
  }

  private state(timestamp: Date | null, now: Date): OfficialWindowState {
    return officialWindowState(timestamp, now);
  }
}

/** Applies the current selected managed resource's already-qualified Meta IN timestamps only. */
export function isOfficialWindowOpen(
  evidence: readonly OfficialInboundWindowEvidence[],
  selectedResourceIdentityId: string,
  now = new Date(),
): boolean {
  const latest = evidence.reduce<Date | null>((current, row) => {
    const timestamp = row.officialInboundAt;
    if (row.direction !== 'IN' || row.channelOrigin !== 'OFICIAL'
      || row.providerResourceIdentityId !== selectedResourceIdentityId || !timestamp
      || !Number.isFinite(timestamp.getTime()) || timestamp.getTime() <= 0 || timestamp.getTime() > now.getTime()) return current;
    return !current || timestamp.getTime() > current.getTime() ? timestamp : current;
  }, null);
  return officialWindowState(latest, now).open;
}

```

### api-app/src/domain/inbox/conversations.service.ts

SHA256 `6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { criarCursorTimeline, lerCursorTimeline } from './timeline-pagination';
import { OutboundService } from './outbound.service';
import { ChannelResolver, type ChannelOrigin } from '../channels/transport/channel';
import type { OutboundAttribution } from './outbound.service';

export const JANELA_MS = 24 * 60 * 60 * 1000;

export interface Atendente {
  userId: string;
  nome: string;
}

@Injectable()
export class ConversationsService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly outbound: OutboundService,
    private readonly channelResolver: ChannelResolver,
  ) {}

  /** Carrega a conversa **dentro do escopo**. Fora dele, ninguém sabe que ela existe. */
  async carregarNoEscopo(conversaId: string, buIdsDoEscopo: string[]) {
    const conversa = await this.prisma.conversation.findFirst({
      where: { id: conversaId, buId: { in: buIdsDoEscopo } },
    });
    if (!conversa) throw new NotFoundException({ error: 'Não encontrado.', code: 'NAO_ENCONTRADO' });
    return conversa;
  }

  /**
   * A inbox pagina.
   *
   * Antes o `take` era 200 fixo, e o que passasse disso era **inalcançável em
   * silêncio** — nada na resposta dizia que cortou. Teto silencioso é o que vira
   * "sumiram conversas" seis meses depois; `temMais` é o mínimo para que quem
   * consome saiba que existe mais.
   */
  async listar(
    buId: string,
    filtro: { status?: string; grupos?: boolean; minhas?: string; pagina?: number; limite?: number },
  ) {
    const limite = Math.min(Math.max(filtro.limite ?? 50, 1), 200);
    const pagina = Math.max(filtro.pagina ?? 1, 1);

    const where: Record<string, unknown> = { buId };
    if (filtro.grupos) where.contactType = 'GRUPO';
    else {
      where.contactType = 'PESSOA';
      if (filtro.status) where.status = filtro.status;
    }
    if (filtro.minhas) where.attendantUserId = filtro.minhas;

    const conditions = [Prisma.sql`bu_id = ${buId}`];
    if (filtro.grupos) conditions.push(Prisma.sql`contact_type = 'GRUPO'::"ContactType"`);
    else {
      conditions.push(Prisma.sql`contact_type = 'PESSOA'::"ContactType"`);
      if (filtro.status) conditions.push(Prisma.sql`status = ${filtro.status}::"ConversationStatus"`);
    }
    if (filtro.minhas) conditions.push(Prisma.sql`attendant_user_id = ${filtro.minhas}`);
    const [total, pageIds] = await Promise.all([
      this.prisma.conversation.count({ where }),
      this.prisma.$queryRaw<Array<{ id: string }>>`
        SELECT id FROM conversations
        WHERE ${Prisma.join(conditions, ' AND ')}
        ORDER BY COALESCE(last_message_at, created_at) DESC, id DESC
        OFFSET ${(pagina - 1) * limite} LIMIT ${limite}
      `,
    ]);
    const loaded = pageIds.length ? await this.prisma.conversation.findMany({
      where: { ...where, id: { in: pageIds.map(({ id }) => id) } },
      select: {
        id: true,
        contact: true,
        contactType: true,
        displayName: true,
        status: true,
        attendantName: true,
        attendantOrigin: true,
        unreadCount: true,
        lastMessageAt: true,
        // O setor é PROJEÇÃO, não modelo (ADR-0017 §3): vem por junção do
        // número. Duplicá-lo na conversa criaria a pergunta "e quando o número
        // muda de setor, o histórico muda junto?" — pergunta que não precisa
        // existir.
        bu: { select: { setor: { select: { id: true, name: true } } } },
      },
    }) : [];
    const loadedById = new Map(loaded.map((conversation) => [conversation.id, conversation]));
    const conversas = pageIds.map(({ id }) => loadedById.get(id)).filter((conversation) => conversation !== undefined);

    return { total, pagina, temMais: pagina * limite < total, conversas };
  }

  /** Página bounded da timeline; o reconhecimento é uma atualização atômica anterior à leitura. */
  async timeline(conversaId: string, limite: number, cursor: string | null, marcarLida: boolean) {
    let ancora: { id: string; createdAt: Date } | null = null;
    if (cursor) {
      const decodificado = lerCursorTimeline(cursor);
      if (decodificado.conversaId !== conversaId) {
        throw new BadRequestException({
          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
        });
      }
      ancora = await this.prisma.message.findFirst({
        where: { id: decodificado.mensagemId, conversationId: conversaId },
        select: { id: true, createdAt: true },
      });
      if (!ancora) {
        throw new BadRequestException({
          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
        });
      }
    }

    if (marcarLida) {
      await this.prisma.conversation.updateMany({
        where: { id: conversaId }, data: { unreadCount: 0 },
      });
    }

    const where = ancora
      ? {
          conversationId: conversaId,
          OR: [
            { createdAt: { lt: ancora.createdAt } },
            { createdAt: ancora.createdAt, id: { lt: ancora.id } },
          ],
        }
      : { conversationId: conversaId };
    const encontradas = await this.prisma.message.findMany({
      where,
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
      take: limite + 1,
      select: {
        id: true, direction: true, messageType: true, content: true,
        channelOrigin: true, authorName: true, createdAt: true,
      },
    });
    const temAnteriores = encontradas.length > limite;
    const messages = encontradas.slice(0, limite).reverse();
    return {
      messages,
      paginacao: {
        limite,
        temAnteriores,
        cursorAnterior: temAnteriores && messages.length
          ? criarCursorTimeline(conversaId, messages[0].id)
          : null,
      },
    };
  }

  /**
   * Estado da janela de 24h — **atributo do canal, não do produto** (ADR-0009 §3).
   *
   * Numa BU com os dois canais, o canal considerado é o da ÚLTIMA mensagem: a
   * janela fechada no oficial não libera responder pelo não oficial sozinha.
   * Trocar de número no meio da conversa é decisão de quem atende, nunca do
   * sistema.
   */
  async estadoDaJanela(conversaId: string, buId: string) {
    const estado = await this.channelResolver.inspectForConversation({ conversationId: conversaId, buId });
    return {
      canal: estado.channelOrigin ? { type: estado.channelOrigin } : null,
      exigeJanela: estado.requiresWindow,
      aberta: estado.windowOpen,
      expiraEm: estado.expiresAt,
      disponivel: estado.available,
      motivoIndisponibilidade: estado.reason,
    };
  }

  async estadosDasJanelas(references: readonly { conversationId: string; buId: string; latestMessageOrigin: ChannelOrigin | null }[]) {
    return this.channelResolver.inspectManyForConversations(references);
  }

  async responder(conversaId: string, buId: string, texto: string, attribution: OutboundAttribution) {
    return this.outbound.send({ conversationId: conversaId, buId, text: texto, attribution });
  }

  /** Assumir sem responder. 409 se outro — interno ou externo — já está nela. */
  async assumir(conversaId: string, atendente: Atendente) {
    const conversa = await this.prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
    if (conversa.contactType === 'GRUPO') {
      throw new BadRequestException({ error: 'Grupos não usam fila de atendimento.', code: 'GRUPO_SEM_FILA' });
    }
    if (
      conversa.status === 'IN_SERVICE' &&
      conversa.attendantUserId &&
      conversa.attendantUserId !== atendente.userId
    ) {
      throw new ConflictException({
        error: `Já está sendo atendida por ${conversa.attendantName ?? 'outro agente'}.`,
        code: 'JA_ATENDIDA',
      });
    }
    if (conversa.status === 'IN_SERVICE' && conversa.attendantOrigin === 'EXTERNO' && !conversa.attendantUserId) {
      throw new ConflictException({
        error: `Já está sendo atendida por ${conversa.attendantName ?? 'um sistema externo'}.`,
        code: 'JA_ATENDIDA',
      });
    }

    return this.prisma.conversation.update({
      where: { id: conversa.id },
      data: {
        status: 'IN_SERVICE',
        attendantUserId: atendente.userId,
        attendantName: atendente.nome,
        attendantOrigin: 'INTERNO',
      },
    });
  }

  /** Finalizar. Mensagem nova do contato reabre para QUEUED (ver incoming). */
  async finalizar(conversaId: string) {
    const conversa = await this.prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
    if (conversa.contactType === 'GRUPO') {
      throw new BadRequestException({ error: 'Grupos não usam fila de atendimento.', code: 'GRUPO_SEM_FILA' });
    }
    return this.prisma.conversation.update({
      where: { id: conversa.id },
      data: { status: 'CLOSED', attendantUserId: null, attendantName: null, attendantOrigin: null },
    });
  }
}

```

### api-app/src/domain/inbox/incoming.service.ts

SHA256 `390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { Inject, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { RealtimeService } from '../../realtime/realtime.service';
import { TYPEBOT_CLIENT, TypebotClient } from '../../integrations/typebot/typebot.client';
import { MessageAcceptanceService } from './message-acceptance.service';
import { OutboundService } from './outbound.service';
import type { ChannelOrigin } from '../channels/transport/channel';

export type CanalDeOrigem = ChannelOrigin;

export interface MensagemRecebida {
  buId: string;
  canal: CanalDeOrigem;
  /** Telefone E.164 só dígitos, ou o identificador do grupo. */
  contato: string;
  ehGrupo: boolean;
  /** Nome do contato, quando o canal informa e ele é confiável (ver webhooks). */
  nomeExibicao?: string | null;
  direcao: 'IN' | 'OUT';
  tipo: 'TEXTO' | 'IMAGEM' | 'AUDIO' | 'VIDEO' | 'DOCUMENTO' | 'OUTRO';
  conteudo?: string | null;
  officialInboundAt?: Date | null;
  externalId?: string | null;
  /** Quem respondeu, quando a mensagem saiu por fora do produto. */
  autorNome?: string | null;
  providerResourceIdentityId: string;
  channelId: string;
  generation: number;
  pairingEpoch: number;
}

/**
 * O ponto onde os dois canais viram a MESMA coisa (ADR-0009 §1): uma conversa
 * pendurada na BU, com as mensagens marcadas pelo canal por onde entraram.
 *
 * Os adaptadores de webhook traduzem o formato de cada plataforma para
 * `MensagemRecebida`; daqui para baixo não existe Meta nem Evolution.
 */
@Injectable()
export class IncomingService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly realtime: RealtimeService,
    @Inject(TYPEBOT_CLIENT) private readonly typebot: TypebotClient,
    private readonly acceptance: MessageAcceptanceService,
    private readonly outbound: OutboundService,
  ) {}

  async registrar(m: MensagemRecebida) {
    const accepted = await this.acceptance.accept({
      providerResourceIdentityId: m.providerResourceIdentityId, channelId: m.channelId, generation: m.generation,
      pairingEpoch: m.pairingEpoch, buId: m.buId, channelOrigin: m.canal, externalMessageId: m.externalId ?? '',
      contact: m.contato, contactType: m.ehGrupo ? 'GRUPO' : 'PESSOA', displayName: m.nomeExibicao,
      direction: m.direcao, messageType: m.tipo, content: m.conteudo, authorName: m.autorNome,
      officialInboundAt: m.officialInboundAt,
    });
    const { conversation: conversa, message: mensagem, creationWinner } = accepted;
    if (creationWinner) {
      this.realtime.publicarNaBu(m.buId, { tipo: 'mensagem', conversaId: conversa.id, contato: conversa.contact, direcao: m.direcao, canal: m.canal, naoLidas: conversa.unreadCount });
      if (m.direcao === 'IN' && m.tipo === 'TEXTO' && m.conteudo?.trim()) {
        await this.executarTypebot(m, m.conteudo.trim(), conversa.id, accepted.conversationCreated).catch(() => undefined);
      }
    }
    return { conversa, mensagem, reabriu: accepted.reopened, creationWinner, reconciled: accepted.reconciled };
  }

  private async executarTypebot(incoming: MensagemRecebida, texto: string, conversationId: string, conversationCreated: boolean): Promise<void> {
    const { buId, contato } = incoming;
    const bu = await this.prisma.businessUnit.findUnique({ where: { id: buId }, select: { mantenedoraId: true } });
    if (!bu) return;
    const gatilhos = await this.prisma.typebotTrigger.findMany({
      where: { active: true, bot: { status: 'ATIVO', mantenedoraId: bu.mantenedoraId }, OR: [{ buId: null }, { buId }] },
      include: { bot: true }, orderBy: { createdAt: 'asc' },
    });
    const normalized = texto.toLocaleLowerCase('pt-BR');
    const gatilho = gatilhos.find((g) => gatilhoCombina(g.kind, g.value, normalized, conversationCreated));
    if (!gatilho || !this.typebot.configurado()) return;
    const botId = gatilho.bot.publishedTypebotId;
    if (!botId) return;
    const atual = await this.prisma.typebotSession.findUnique({ where: { botId_buId_contato: { botId: gatilho.botId, buId, contato } } });
    if (atual && (atual.mantenedoraId !== bu.mantenedoraId || atual.buId !== buId || atual.botId !== gatilho.botId || gatilho.bot.mantenedoraId !== bu.mantenedoraId)) return;
    const resposta = atual?.ativo ? await this.typebot.continuar(atual.sessionId, texto) : await this.typebot.iniciar(botId, contato, texto);
    const sessionId = 'sessionId' in resposta && typeof resposta.sessionId === 'string' ? resposta.sessionId : null;
    if (!atual && sessionId) await this.prisma.typebotSession.create({ data: { botId: gatilho.botId, mantenedoraId: gatilho.bot.mantenedoraId, buId, contato, sessionId } });
    for (const mensagem of resposta.messages) {
      const saida = textoDaRespostaTypebot(mensagem);
      if (!saida) continue;
      await this.outbound.send({
        conversationId,
        buId,
        text: saida,
        attribution: { kind: 'BOT', name: 'Typebot' },
        ingress: {
          channelId: incoming.channelId,
          providerResourceIdentityId: incoming.providerResourceIdentityId,
          channelOrigin: incoming.canal,
          generation: incoming.generation,
          pairingEpoch: incoming.pairingEpoch,
        },
      });
    }
  }

}

function textoDaRespostaTypebot(mensagem: unknown): string | null {
  if (!mensagem || typeof mensagem !== 'object') return null;
  const m = mensagem as { type?: string; content?: { richText?: unknown; text?: string } };
  if (m.type !== 'text') return null;
  if (typeof m.content?.text === 'string') return m.content.text.trim() || null;
  const juntar = (v: unknown): string => Array.isArray(v) ? v.map(juntar).join('') : v && typeof v === 'object' ? juntar((v as { children?: unknown }).children) : typeof v === 'string' ? v : '';
  const texto = juntar(m.content?.richText).trim();
  return texto || null;
}

export function gatilhoCombina(tipo: 'PALAVRA_CHAVE' | 'NOVA_CONVERSA', valor: string, textoNormalizado: string, novaConversa: boolean): boolean {
  return tipo === 'NOVA_CONVERSA' ? novaConversa : textoNormalizado.toLocaleLowerCase('pt-BR').includes(valor.toLocaleLowerCase('pt-BR'));
}

```

### api-app/src/integrations/channels/meta-channel.ts

SHA256 `99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import type { Channel, ChannelMessage, ChannelMessageKind, ChannelSendOptions, ChannelSendResult } from '../../domain/channels/transport/channel';
import type { MetaClient } from '../meta/meta.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';
import { MetaInitialMessageClient } from '../meta/initial-message.client';
import { metaAccountReference } from './account-reference';

class BoundMetaChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: MetaClient,
    private readonly initialClient: MetaInitialMessageClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  readonly supportedKinds: readonly ChannelMessageKind[] = Object.freeze(['text', 'approved-template']);

  async sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult> {
    // Approved templates always use the initial protocol path; text selects
    // that path explicitly so ordinary text retains its legacy wire format.
    if (options?.purpose === 'initial' || message.kind === 'approved-template') {
      const claimFence = options?.beforeDispatch;
      if (!claimFence) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
      if (!this.credential.phoneNumberId || !this.credential.wabaId || !this.credential.accessToken) {
        return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
      }
      if (!/^\d{8,15}$/.test(message.recipientRef)) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
      const template = message.kind === 'approved-template' ? message.template : null;
      const managementContext = template?.managementContext;
      return this.initialClient.sendInitialMessage({
        wabaId: this.credential.wabaId,
        phoneNumberId: this.credential.phoneNumberId,
        recipientE164: `+${message.recipientRef}`,
        accessToken: this.credential.accessToken,
        accountReference: metaAccountReference(this.credential.wabaId),
        payload: message,
        ...(managementContext ? { managementContext } : {}),
        beforeDispatch: async () => {
          const contextCurrent = await this.beforeDispatch().catch(() => false);
          if (!contextCurrent) return false;
          try { return await claimFence(); } catch { return false; }
        },
      });
    }
    if (message.kind !== 'text') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    if (!this.credential.phoneNumberId || !this.credential.accessToken) {
      return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
    }
    if (options?.beforeDispatch) {
      let dispatched: boolean;
      try { dispatched = await options.beforeDispatch(); } catch { dispatched = false; }
      if (!dispatched) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    try {
      return await this.client.enviarTexto(
        this.credential.phoneNumberId,
        message.recipientRef,
        message.text,
        this.credential.accessToken,
      );
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
    }
  }
}

export class MetaChannelFactory extends ChannelAdapterFactory {
  readonly origin = 'OFICIAL' as const;
  constructor(private readonly client: MetaClient, private readonly initialClient: MetaInitialMessageClient) { super(); }
  locallyConfigured(): boolean { return this.client.canSendText(); }
  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundMetaChannel(credential, this.client, this.initialClient, beforeDispatch);
  }
}

```

### api-app/src/integrations/channels/evolution-channel.ts

SHA256 `6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import type { Channel, ChannelMessage, ChannelMessageKind, ChannelSendOptions, ChannelSendResult } from '../../domain/channels/transport/channel';
import type { EvolutionClient } from '../evolution/evolution.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';

class BoundEvolutionChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: EvolutionClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  readonly supportedKinds: readonly ChannelMessageKind[] = Object.freeze(['text']);

  async sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult> {
    if (message.kind !== 'text') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    if (options?.purpose === 'initial' && !options.beforeDispatch) {
      return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (options?.beforeDispatch) {
      let dispatched: boolean;
      try { dispatched = await options.beforeDispatch(); } catch { dispatched = false; }
      if (!dispatched) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (!this.credential.evolutionInstanceName) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    try {
      return await this.client.enviarTexto(this.credential.evolutionInstanceName, message.recipientRef, message.text);
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
    }
  }
}

export class EvolutionChannelFactory extends ChannelAdapterFactory {
  readonly origin = 'NAO_OFICIAL' as const;
  constructor(private readonly client: EvolutionClient) { super(); }
  locallyConfigured(): boolean { return this.client.configurado(); }
  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundEvolutionChannel(credential, this.client, beforeDispatch);
  }
}

```

### api-app/src/integrations/channels/prisma-channel-resolver.ts

SHA256 `60005fd226534a178b646d6ec775bb059ec55cc4cfea24a3d72d2c6e4a1ca64a`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver, type ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import {
  ChannelResolver,
  type ChannelAvailability,
  type InitialChannelReference,
  type ConversationAvailabilityReference,
  type ChannelOperationContext,
  type ChannelOrigin,
  type ConversationChannelReference,
  type ResolvedChannelOperation,
  type VerifiedIngressChannelReference,
} from '../../domain/channels/transport/channel';
import { ChannelAdapterRegistry } from './channel-adapter-registry';
import { OfficialChannelWindowPolicy, type OfficialWindowState } from '../../domain/inbox/channel-window-policy';
import { metaAccountReference } from './account-reference';

type Candidate = {
  id: string;
  buId: string;
  type: ChannelOrigin;
  status: string;
  generation: number;
  pairingEpoch: number;
  verifiedEpoch: number | null;
  ownNumberVerified: boolean;
  providerConnectionState: string;
  receiptVerifiedAt: Date | null;
  requiresWindow: boolean;
  wabaId: string | null;
  providerIdentities: Array<{ id: string; buId: string; provider: ChannelOrigin; currentChannelId: string | null; managedLifecycle: boolean }>;
};

@Injectable()
export class PrismaChannelResolver extends ChannelResolver {
  constructor(
    private readonly prisma: PrismaService,
    private readonly credentials: ChannelCredentialResolver,
    private readonly adapters: ChannelAdapterRegistry,
    private readonly windows: OfficialChannelWindowPolicy,
  ) { super(); }

  async resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation> {
    const { candidate } = await this.selectForConversation(reference);
    return this.bind(candidate);
  }

  async resolveForInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    if (!candidate) this.throwUnavailable('CANAL_SELECIONADO_INDISPONIVEL');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    const operation = await this.bind(candidate);
    if (!operation.channel.supportedKinds.includes(reference.kind)) this.throwUnavailable('UNSUPPORTED_KIND');
    if (reference.kind === 'text' && operation.context.requiresWindow) {
      const window = await this.windows.inspect({
        conversationId: conversation.id,
        providerResourceIdentityId: operation.context.providerResourceIdentityId,
      });
      if (!window.open) this.throwUnavailable('JANELA_FECHADA');
    }
    return operation;
  }

  async resolveForInitialOptions(reference: ConversationChannelReference & { channelId: string }): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId }, select: { id: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    if (!candidate) this.throwUnavailable('CANAL_SELECIONADO_INDISPONIVEL');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    return this.bind(candidate);
  }

  async resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true, contact: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    const identity = candidate?.providerIdentities.find((item) => item.id === reference.providerResourceIdentityId);
    if (!candidate || candidate.type !== reference.channelOrigin || candidate.generation !== reference.generation
      || candidate.pairingEpoch !== reference.pairingEpoch || !identity || identity.buId !== reference.buId
      || identity.provider !== reference.channelOrigin || identity.currentChannelId !== reference.channelId
      || !identity.managedLifecycle) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    return this.bind(candidate);
  }

  async hasReadyChannelForNewConversation(buId: string): Promise<boolean> {
    const candidates = await this.channels(buId);
    for (const candidate of candidates) {
      if (!await this.inspectCandidate(candidate)) return true;
    }
    return false;
  }

  async inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability> {
    try {
      const conversation = await this.prisma.conversation.findFirst({
        where: { id: reference.conversationId, buId: reference.buId }, select: { id: true },
      });
      if (!conversation) return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
      const { candidate, selectionReason, selectedOrigin } = await this.selectCandidate(reference);
      if (!candidate) {
        return this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL');
      }
      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      let reason: ChannelAvailability['reason'] = null;
      if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
        || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
        reason = 'CHANNEL_IDENTITY_NOT_VERIFIED';
      } else if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
        || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
        || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
        || !this.adapters.locallyConfigured(candidate.type)) {
        reason = 'CHANNEL_NOT_READY';
      } else if (candidate.type === 'OFICIAL') {
        const credential = await this.credentials.inspectActiveCredential(candidate.id, candidate.generation);
        if (!credential.ready) reason = 'PENDING_CREDENTIAL';
      }

      const currentIdentity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      const window = candidate.requiresWindow && currentIdentity
        ? await this.windows.inspect({ conversationId: reference.conversationId, providerResourceIdentityId: currentIdentity.id })
        : { open: !candidate.requiresWindow, expiresAt: null };
      if (!reason && candidate.requiresWindow && !window.open) reason = 'JANELA_FECHADA';
      return {
        available: reason === null,
        reason,
        channelOrigin: candidate.type,
        requiresWindow: candidate.requiresWindow,
        windowOpen: window.open,
        expiresAt: window.expiresAt,
      };
    } catch {
      return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
    }
  }

  /** Batch-only GET view: BU bindings and credential metadata are read once for the page. */
  async inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>> {
    if (!references.length) return new Map();
    const buId = references[0].buId;
    if (references.some((reference) => reference.buId !== buId)) {
      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
    }
    try {
      const ids = references.map(({ conversationId }) => conversationId);
      const channels = await this.channels(buId);
      const credentialState = await this.credentials.inspectActiveCredentials(channels
        .filter((candidate) => candidate.type === 'OFICIAL')
        .map(({ id, generation }) => ({ channelId: id, generation })));
      const selectedById = new Map<string, {
        candidate: Candidate | null;
        selectedOrigin: ChannelOrigin | null;
        selectionReason: ChannelAvailability['reason'] | null;
      }>();
      for (const reference of references) {
        let selectedOrigin = reference.latestMessageOrigin;
        let candidate: Candidate | null;
        let selectionReason: ChannelAvailability['reason'] | null = null;
        if (selectedOrigin) {
          candidate = channels.find((item) => item.type === selectedOrigin) ?? null;
          if (!candidate) selectionReason = 'CANAL_SELECIONADO_INDISPONIVEL';
        } else if (channels.length === 0) {
          candidate = null; selectionReason = 'CANAL_AUSENTE';
        } else if (channels.length > 1) {
          candidate = null; selectionReason = 'CANAL_AMBIGUO';
        } else {
          candidate = channels[0]; selectedOrigin = candidate.type;
        }
        selectedById.set(reference.conversationId, { candidate, selectedOrigin, selectionReason });
      }
      const windowRefs = references.flatMap(({ conversationId }) => {
        const candidate = selectedById.get(conversationId)?.candidate;
        const identity = candidate?.providerIdentities.find((item) => item.currentChannelId === candidate.id);
        return candidate?.requiresWindow && identity
          ? [{ conversationId, providerResourceIdentityId: identity.id }]
          : [];
      });
      const windows = windowRefs.length
        ? await this.windows.inspectMany(windowRefs)
        : new Map<string, OfficialWindowState>();
      const result = new Map<string, ChannelAvailability>();
      for (const id of ids) {
        const { candidate, selectedOrigin, selectionReason } = selectedById.get(id)!;
        if (!candidate) {
          result.set(id, this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL'));
          continue;
        }
        const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
        let reason: ChannelAvailability['reason'] = null;
        if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
          || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
          reason = 'CHANNEL_IDENTITY_NOT_VERIFIED';
        } else if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
          || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
          || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
          || !this.adapters.locallyConfigured(candidate.type)) {
          reason = 'CHANNEL_NOT_READY';
        } else if (candidate.type === 'OFICIAL' && !credentialState.get(candidate.id)?.ready) {
          reason = 'PENDING_CREDENTIAL';
        }
        let windowOpen = true;
        let expiresAt: Date | null = null;
        if (candidate.requiresWindow) {
          const state = windows.get(id);
          windowOpen = state?.open ?? false;
          expiresAt = state?.expiresAt ?? null;
          if (!reason && !windowOpen) reason = 'JANELA_FECHADA';
        }
        result.set(id, {
          available: reason === null, reason, channelOrigin: candidate.type,
          requiresWindow: candidate.requiresWindow, windowOpen, expiresAt,
        });
      }
      return result;
    } catch {
      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
    }
  }

  async contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
    try {
      const status = await this.contextStatus(context, false);
      return status;
    } catch {
      return 'UNKNOWN';
    }
  }

  async validateOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
  ): Promise<boolean> {
    if (!selectedValue || typeof selectedValue !== 'object' || Array.isArray(selectedValue)) return false;
    const selected = selectedValue as Record<string, Prisma.JsonValue>;
    const tuple = [
      'channelId', 'buId', 'channelOrigin', 'providerResourceIdentityId', 'generation',
      'pairingEpoch', 'activeCredentialVersion', 'requiresWindow', 'providerAccountReference',
    ] as const;
    if (tuple.some((key) => selected[key] !== expected[key])) return false;

    const [businessUnit, identity] = await Promise.all([
      tx.businessUnit.findFirst({ where: { id: expected.buId, status: 'ATIVO' }, select: { id: true } }),
      tx.providerResourceIdentity.findFirst({
      where: {
        id: expected.providerResourceIdentityId,
        buId: expected.buId,
        provider: expected.channelOrigin,
        currentChannelId: expected.channelId,
        managedLifecycle: true,
      },
        select: { id: true, externalResourceId: true },
      }),
    ]);
    if (!businessUnit || !identity) return false;

    const channel = await tx.buChannel.findFirst({
      where: {
        id: expected.channelId,
        buId: expected.buId,
        type: expected.channelOrigin,
        generation: expected.generation,
        pairingEpoch: expected.pairingEpoch,
        ownNumberVerified: true,
        verifiedEpoch: expected.pairingEpoch,
        status: 'CONECTADO',
        receiptVerifiedAt: { not: null },
        providerConnectionState: expected.channelOrigin === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
      },
      select: {
        wabaId: true,
        phoneNumberId: true,
        evolutionInstanceName: true,
        requiresWindow: true,
        credential: { select: { generation: true, version: true } },
      },
    });
    const providerResource = expected.channelOrigin === 'OFICIAL' ? channel?.phoneNumberId : channel?.evolutionInstanceName;
    if (!channel || channel.requiresWindow !== expected.requiresWindow || providerResource !== identity.externalResourceId
      || (channel.wabaId ? metaAccountReference(channel.wabaId) : null) !== expected.providerAccountReference) return false;
    if (expected.channelOrigin === 'OFICIAL' && (!channel.credential
      || channel.credential.generation !== expected.generation
      || channel.credential.version !== expected.activeCredentialVersion)) return false;
    return true;
  }

  async validateAcceptedOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
  ): Promise<boolean> {
    if (!selectedValue || typeof selectedValue !== 'object' || Array.isArray(selectedValue)) return false;
    const selected = selectedValue as Record<string, Prisma.JsonValue>;
    const tuple = ['channelId', 'buId', 'channelOrigin', 'providerResourceIdentityId', 'generation', 'pairingEpoch',
      'activeCredentialVersion', 'requiresWindow', 'providerAccountReference'] as const;
    if (tuple.some((key) => selected[key] !== expected[key])) return false;
    const [businessUnit, identity, channel] = await Promise.all([
      tx.businessUnit.findFirst({ where: { id: expected.buId, status: 'ATIVO' }, select: { id: true } }),
      tx.providerResourceIdentity.findFirst({ where: {
        id: expected.providerResourceIdentityId, buId: expected.buId, provider: expected.channelOrigin,
        currentChannelId: expected.channelId, managedLifecycle: true,
      }, select: { id: true, externalResourceId: true } }),
      tx.buChannel.findFirst({ where: {
        id: expected.channelId, buId: expected.buId, type: expected.channelOrigin,
        generation: expected.generation, pairingEpoch: expected.pairingEpoch,
        ownNumberVerified: true, verifiedEpoch: expected.pairingEpoch,
      }, select: { wabaId: true, phoneNumberId: true, evolutionInstanceName: true, requiresWindow: true } }),
    ]);
    if (!businessUnit || !identity || !channel || channel.requiresWindow !== expected.requiresWindow) return false;
    const providerResource = expected.channelOrigin === 'OFICIAL' ? channel.phoneNumberId : channel.evolutionInstanceName;
    return providerResource === identity.externalResourceId
      && (channel.wabaId ? metaAccountReference(channel.wabaId) : null) === expected.providerAccountReference;
  }

  private async bind(candidate: Candidate): Promise<ResolvedChannelOperation> {
    const availability = await this.inspectCandidate(candidate);
    if (availability) this.throwUnavailable(availability);
    const credential = await this.credentials.resolve(candidate.id);
    const context: ChannelOperationContext = Object.freeze({
      channelId: candidate.id,
      buId: candidate.buId,
      channelOrigin: candidate.type,
      providerResourceIdentityId: credential.providerResourceIdentityId,
      generation: credential.generation,
      pairingEpoch: credential.pairingEpoch,
      activeCredentialVersion: credential.activeCredentialVersion,
      requiresWindow: candidate.requiresWindow,
      providerAccountReference: credential.wabaId ? metaAccountReference(credential.wabaId) : null,
    });
    if (!this.sameCredentialContext(candidate, credential)) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    const factory = this.adapters.get(candidate.type);
    if (!factory) throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
    const channel = factory.create(credential, async () => {
      try { return (await this.contextStatus(context, true)) === 'CURRENT'; }
      catch { return false; }
    });
    return { channel, context };
  }

  private async inspectCandidate(candidate: Candidate): Promise<ChannelAvailability['reason']> {
    const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
    if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
      || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
      return 'CHANNEL_IDENTITY_NOT_VERIFIED';
    }
    if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
      || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
      || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
      || !this.adapters.locallyConfigured(candidate.type)) return 'CHANNEL_NOT_READY';
    if (candidate.type === 'OFICIAL' && !(await this.credentials.inspectActiveCredential(candidate.id, candidate.generation)).ready) {
      return 'PENDING_CREDENTIAL';
    }
    return null;
  }

  private async selectForConversation(reference: ConversationChannelReference) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true, contact: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const { candidate, selectionReason } = await this.selectCandidate(reference);
    if (!candidate) this.throwUnavailable(selectionReason ?? 'CANAL_AUSENTE');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    if (candidate.requiresWindow) {
      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      const window = identity
        ? await this.windows.inspect({ conversationId: conversation.id, providerResourceIdentityId: identity.id })
        : { open: false, expiresAt: null };
      if (!window.open) this.throwUnavailable('JANELA_FECHADA');
    }
    return { conversation, candidate };
  }

  private async selectCandidate(reference: ConversationChannelReference): Promise<{
    candidate: Candidate | null; selectedOrigin: ChannelOrigin | null; selectionReason: ChannelAvailability['reason'] | null;
  }> {
    const latest = await this.prisma.message.findFirst({
      where: { conversationId: reference.conversationId },
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
      select: { channelOrigin: true },
    });
    const channels = await this.channels(reference.buId);
    if (latest) {
      const selectedOrigin = latest.channelOrigin as ChannelOrigin;
      const candidate = channels.find((channel) => channel.type === selectedOrigin) ?? null;
      return { candidate, selectedOrigin, selectionReason: candidate ? null : 'CANAL_SELECIONADO_INDISPONIVEL' };
    }
    if (channels.length === 0) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AUSENTE' };
    if (channels.length > 1) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AMBIGUO' };
    return { candidate: channels[0], selectedOrigin: channels[0].type, selectionReason: null };
  }

  private async channels(buId: string): Promise<Candidate[]> {
    return this.prisma.buChannel.findMany({
      where: { buId },
      select: {
        id: true, buId: true, type: true, wabaId: true, status: true, generation: true, pairingEpoch: true,
        verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
        receiptVerifiedAt: true, requiresWindow: true,
        providerIdentities: { select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } },
      },
    }) as unknown as Promise<Candidate[]>;
  }

  private async findCandidate(channelId: string, buId: string): Promise<Candidate | null> {
    const rows = await this.prisma.buChannel.findMany({ where: { id: channelId, buId }, select: {
      id: true, buId: true, type: true, wabaId: true, status: true, generation: true, pairingEpoch: true,
      verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
      receiptVerifiedAt: true, requiresWindow: true,
      providerIdentities: { select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } },
    } });
    return (rows[0] as unknown as Candidate | undefined) ?? null;
  }

  private async contextStatus(context: ChannelOperationContext, beforeDispatch: boolean): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
    const where: Prisma.BuChannelWhereInput = {
      id: context.channelId, buId: context.buId, type: context.channelOrigin,
      generation: context.generation, pairingEpoch: context.pairingEpoch,
      ownNumberVerified: true, verifiedEpoch: context.pairingEpoch,
      ...(beforeDispatch ? {
        status: 'CONECTADO', receiptVerifiedAt: { not: null },
        providerConnectionState: context.channelOrigin === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
      } : {}),
    };
    const channel = await this.prisma.buChannel.findFirst({
      where,
      select: { id: true, wabaId: true, credential: { select: { version: true, generation: true } },
        providerIdentities: { where: { id: context.providerResourceIdentityId }, select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } } },
    });
    const identity = channel?.providerIdentities[0];
    if (!channel || !identity || identity.buId !== context.buId || identity.provider !== context.channelOrigin
      || identity.currentChannelId !== context.channelId || !identity.managedLifecycle) {
      return 'CHANGED';
    }
    const currentAccountReference = channel.wabaId ? metaAccountReference(channel.wabaId) : null;
    if (currentAccountReference !== context.providerAccountReference) return 'CHANGED';
    if (context.channelOrigin === 'OFICIAL') {
      const credential = channel.credential;
      if (!credential || credential.generation !== context.generation) return 'CHANGED';
      if (beforeDispatch && credential.version !== context.activeCredentialVersion) return 'CHANGED';
    }
    return 'CURRENT';
  }

  private sameCredentialContext(candidate: Candidate, credential: ResolvedChannelCredential): boolean {
    const identity = candidate.providerIdentities.find((item) => item.id === credential.providerResourceIdentityId);
    return credential.channelId === candidate.id && credential.buId === candidate.buId
      && credential.provider === candidate.type && credential.generation === candidate.generation
      && (credential.wabaId ? metaAccountReference(credential.wabaId) : null) === (candidate.wabaId ? metaAccountReference(candidate.wabaId) : null)
      && credential.pairingEpoch === candidate.pairingEpoch && identity?.currentChannelId === candidate.id
      && identity?.buId === candidate.buId && identity.provider === candidate.type;
  }

  private unavailable(channelOrigin: ChannelOrigin | null, reason: ChannelAvailability['reason']): ChannelAvailability {
    return { available: false, reason, channelOrigin, requiresWindow: false, windowOpen: false, expiresAt: null };
  }

  private throwUnavailable(reason: ChannelAvailability['reason']): never {
    if (reason === 'CANAL_AUSENTE') throw new BadRequestException({ code: reason, error: 'Esta BU não tem canal conectado.' });
    if (reason === 'CANAL_AMBIGUO') throw new ConflictException({ code: reason, error: 'Selecione uma origem de conversa antes de responder.' });
    throw new ConflictException({ code: reason, error: reason === 'JANELA_FECHADA'
      ? 'Fora da janela de 24h da última mensagem recebida.'
      : 'O canal selecionado não está disponível para envio.' });
  }
}

```

### api-app/src/integrations/channels/channel-adapter-factory.ts

SHA256 `e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc`. unchanged inherited pre-ST04 bytes.

```typescript
import type { Channel, ChannelOrigin } from '../../domain/channels/transport/channel';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';

export abstract class ChannelAdapterFactory {
  abstract readonly origin: ChannelOrigin;
  abstract locallyConfigured(): boolean;
  abstract create(
    credential: ResolvedChannelCredential,
    beforeDispatch: () => Promise<boolean>,
  ): Channel;
}

```

### api-app/src/integrations/channels/channel-adapter-registry.ts

SHA256 `655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b`. unchanged inherited pre-ST04 bytes.

```typescript
import { Injectable } from '@nestjs/common';
import type { ChannelOrigin } from '../../domain/channels/transport/channel';
import { ChannelAdapterFactory } from './channel-adapter-factory';

/** Explicit provider registration; common consumers never select a provider. */
@Injectable()
export class ChannelAdapterRegistry {
  private readonly factories: ReadonlyMap<ChannelOrigin, ChannelAdapterFactory>;

  constructor(factories: ChannelAdapterFactory[]) {
    const entries = factories.map((factory) => [factory.origin, factory] as const);
    if (new Set(entries.map(([origin]) => origin)).size !== entries.length) {
      throw new Error('Duplicate channel adapter registration.');
    }
    this.factories = new Map(entries);
  }

  get(origin: ChannelOrigin): ChannelAdapterFactory | undefined {
    return this.factories.get(origin);
  }

  locallyConfigured(origin: ChannelOrigin): boolean {
    return this.factories.get(origin)?.locallyConfigured() ?? false;
  }
}

```

### api-app/src/integrations/channels/channel-transport.module.ts

SHA256 `4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { Module } from '@nestjs/common';
import { ChannelResolver } from '../../domain/channels/transport/channel';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { OutboundService } from '../../domain/inbox/outbound.service';
import { EVOLUTION_CLIENT, EvolutionHttpClient } from '../evolution/evolution.client';
import { META_CLIENT, MetaHttpClient } from '../meta/meta.client';
import { ChannelAdapterRegistry } from './channel-adapter-registry';
import { EvolutionChannelFactory } from './evolution-channel';
import { MetaChannelFactory } from './meta-channel';
import { PrismaChannelResolver } from './prisma-channel-resolver';
import { OfficialChannelWindowPolicy } from '../../domain/inbox/channel-window-policy';
import { MetaInitialMessageClient } from '../meta/initial-message.client';
import { DispatchAdmissionService } from '../../domain/inbox/dispatch-admission.service';

@Module({
  providers: [
    MessageAcceptanceService,
    DispatchAdmissionService,
    OfficialChannelWindowPolicy,
    ChannelCredentialResolver,
    MetaHttpClient,
    EvolutionHttpClient,
    { provide: META_CLIENT, useExisting: MetaHttpClient },
    { provide: EVOLUTION_CLIENT, useExisting: EvolutionHttpClient },
    {
      provide: MetaInitialMessageClient,
      useFactory: (meta: MetaHttpClient) => new MetaInitialMessageClient(meta),
      inject: [META_CLIENT],
    },
    {
      provide: ChannelAdapterRegistry,
      useFactory: (meta: MetaHttpClient, initial: MetaInitialMessageClient, evolution: EvolutionHttpClient) => new ChannelAdapterRegistry([
        new MetaChannelFactory(meta, initial),
        new EvolutionChannelFactory(evolution),
      ]),
      inject: [META_CLIENT, MetaInitialMessageClient, EVOLUTION_CLIENT],
    },
    PrismaChannelResolver,
    { provide: ChannelResolver, useExisting: PrismaChannelResolver },
    OutboundService,
  ],
  exports: [
    MessageAcceptanceService,
    DispatchAdmissionService,
    ChannelCredentialResolver,
    META_CLIENT,
    EVOLUTION_CLIENT,
    ChannelResolver,
    OutboundService,
  ],
})
export class ChannelTransportModule {}

```

### api-app/src/integrations/channels/account-reference.ts

SHA256 `da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { createHash } from 'node:crypto';
import type { TemplateAccountReference } from '../../domain/message-templates/template-management.ports';

/** Stable opaque account pin shared with the delivered template-management context. */
export function metaAccountReference(wabaId: string): TemplateAccountReference {
  return createHash('sha256').update(`meta-waba\0${wabaId}`).digest('hex') as TemplateAccountReference;
}

```

### api-app/src/integrations/meta/initial-message.client.ts

SHA256 `e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import type { ChannelMessage, ChannelSendResult } from '../../domain/channels/transport/channel';
import { renderInitialTemplate } from '../../domain/inbox/initial-message-template-renderer';
import type { TemplateAccountReference, TemplateManagementContext, TemplateSummary } from '../../domain/message-templates/template-management.ports';
import type { MetaClient } from './meta.client';
import { MetaTemplateClient } from './message-template.client';
import { metaAccountReference } from '../channels/account-reference';

const TEMPLATE_PREFLIGHT_UNAVAILABLE = Symbol('TEMPLATE_PREFLIGHT_UNAVAILABLE');

export interface MetaInitialMessageRequest {
  readonly wabaId: string;
  readonly phoneNumberId: string;
  readonly recipientE164: string;
  readonly accessToken: string;
  readonly accountReference: TemplateAccountReference;
  readonly payload: ChannelMessage;
  readonly managementContext?: TemplateManagementContext;
  readonly beforeDispatch: () => Promise<boolean>;
}

/** Private protocol path for newly reserved messages; ordinary sends stay on MetaClient.enviarTexto. */
export class MetaInitialMessageClient {
  constructor(private readonly legacyMeta: MetaClient) {}

  async sendInitialMessage(input: MetaInitialMessageRequest): Promise<ChannelSendResult> {
    const deadlineAt = Date.now() + 75_000;
    if (!input.wabaId || !input.phoneNumberId || !input.accessToken
      || !/^\+[1-9]\d{7,14}$/.test(input.recipientE164)
      || input.accountReference !== metaAccountReference(input.wabaId)) {
      return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
    }

    const graphVersion = process.env.GRAPH_VERSION?.trim() ?? '';
    if (!/^v\d+\.0$/.test(graphVersion)) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    let templateWire: Record<string, unknown> | null | typeof TEMPLATE_PREFLIGHT_UNAVAILABLE = null;
    if (input.payload.kind === 'approved-template') {
      templateWire = await this.verifyCurrentTemplate(input, deadlineAt);
      if (templateWire === TEMPLATE_PREFLIGHT_UNAVAILABLE) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
      if (!templateWire) return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    }
    if (Date.now() >= deadlineAt) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    const body = input.payload.kind === 'text'
      ? { messaging_product: 'whatsapp', messaging_account_id: input.wabaId, to: input.recipientE164, type: 'text', text: { body: input.payload.text } }
      : { messaging_product: 'whatsapp', messaging_account_id: input.wabaId, to: input.recipientE164, type: 'template', template: templateWire };

    // This call performs the current messaging-grant and selected-WABA phone
    // membership reads. The durable claim is deliberately after every GET.
    // Reserve 40 seconds for the maximum three 10-second membership GETs and
    // the single 10-second POST. If that budget is no longer available, fail
    // before opening another request.
    if (deadlineAt - Date.now() < 40_000) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    try {
      const phone = await this.legacyMeta.verificarNumeroVinculado(input.wabaId, input.phoneNumberId, input.accessToken);
      if (!phone || phone.id !== input.phoneNumberId) return { outcome: 'BLOCKED', reason: 'CHANNEL_IDENTITY_NOT_VERIFIED' };
    } catch {
      return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    }
    if (Date.now() >= deadlineAt) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    let claimed: boolean;
    try { claimed = await input.beforeDispatch(); } catch { claimed = false; }
    if (!claimed) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };

    // The claim may itself wait behind the immutable admission fence. If it
    // consumed the remaining request budget, the known result is still a safe
    // pre-dispatch rejection because POST has not started.
    if (Date.now() >= deadlineAt) return { outcome: 'REJECTED', code: 'INITIAL_PREFLIGHT_DEADLINE' };
    return this.postMessage(input, body, graphVersion, deadlineAt);
  }

  private async verifyCurrentTemplate(input: MetaInitialMessageRequest, deadlineAt: number): Promise<Record<string, unknown> | null | typeof TEMPLATE_PREFLIGHT_UNAVAILABLE> {
    const value = input.payload.kind === 'approved-template' ? input.payload.template : null;
    if (!value) return null;
    const { summary, values } = value;
    const context = input.managementContext;
    if (!summary || summary.status !== 'APPROVED' || !context || context.accountReference !== input.accountReference) return null;
    let render: ReturnType<typeof renderInitialTemplate>;
    try { render = renderInitialTemplate(summary, values as Readonly<Record<string, string>> | readonly string[]); }
    catch { return null; }

    const client = new MetaTemplateClient();
    const seenCursors = new Set<string>();
    let after: string | null = null;
    const matches: TemplateSummary[] = [];
    for (let page = 0; page < 2; page += 1) {
      // MetaTemplateClient bounds each request at ten seconds; retain enough
      // of the immutable 75-second operation budget for every possible page.
      if (deadlineAt - Date.now() < (2 - page) * 10_000 + 40_000) return null;
      let result;
      try {
        result = await client.listTemplates({
          context, accessToken: input.accessToken, wabaId: input.wabaId,
          name: summary.name ?? undefined, after, limit: 50,
        });
      } catch { return TEMPLATE_PREFLIGHT_UNAVAILABLE; }
      matches.push(...result.templates.filter((candidate) => candidate.remoteTemplateId === summary.remoteTemplateId));
      if (!result.nextCursor) break;
      if (page === 1 || seenCursors.has(result.nextCursor)) return null;
      seenCursors.add(result.nextCursor);
      after = result.nextCursor;
    }
    if (matches.length !== 1) return null;
    const current = matches[0];
    if (!current || current.status !== 'APPROVED' || current.name !== summary.name || current.language !== summary.language
      || current.category !== summary.category || current.parameterFormat !== summary.parameterFormat) return null;
    let currentRender: ReturnType<typeof renderInitialTemplate>;
    try { currentRender = renderInitialTemplate(current, values as Readonly<Record<string, string>> | readonly string[]); }
    catch { return null; }
    if (currentRender.semanticFingerprint !== render.semanticFingerprint
      || currentRender.text !== value.renderedText
      || render.semanticFingerprint !== value.semanticFingerprint) return null;
    return this.templateWire(current, values as Readonly<Record<string, string>> | readonly string[]);
  }

  private templateWire(summary: TemplateSummary, values: Readonly<Record<string, string>> | readonly string[]): Record<string, unknown> | null {
    const body = summary.components.find((component) => component.type === 'BODY');
    if (!body || body.type !== 'BODY') return null;
    const supplied = Array.isArray(values) ? values : null;
    const keyed = !Array.isArray(values) && values && typeof values === 'object' ? values as Readonly<Record<string, string>> : null;
    const names = summary.parameterFormat === 'POSITIONAL'
      ? [...new Set(body.parameters)].sort((left, right) => Number(left) - Number(right))
      : [...new Set(body.parameters)];
    if ((summary.parameterFormat === 'POSITIONAL' && (!supplied || supplied.length !== names.length))
      || (summary.parameterFormat === 'NAMED' && (!keyed || Object.keys(keyed).length !== names.length))) return null;
    const parameters = names.map((name, index) => {
      const text = summary.parameterFormat === 'POSITIONAL' ? supplied?.[index] : keyed?.[name];
      return typeof text === 'string'
        ? { type: 'text', text, ...(summary.parameterFormat === 'NAMED' ? { parameter_name: name } : {}) }
        : null;
    });
    if (parameters.some((parameter) => parameter === null)) return null;
    return {
      name: summary.name,
      language: { code: summary.language },
      components: parameters.length ? [{ type: 'body', parameters }] : [],
    };
  }

  private async postMessage(input: MetaInitialMessageRequest, body: Record<string, unknown>, graphVersion: string, deadlineAt: number): Promise<ChannelSendResult> {
    let response: Response;
    try {
      response = await fetch(`https://graph.facebook.com/${graphVersion}/${encodeURIComponent(input.phoneNumberId)}/messages`, {
        method: 'POST',
        headers: { accept: 'application/json', authorization: `Bearer ${input.accessToken}`, 'content-type': 'application/json' },
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(Math.max(1, Math.min(10_000, deadlineAt - Date.now()))), redirect: 'error',
      });
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
    }
    let payload: unknown;
    try { payload = await response.json(); } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
    }
    if (!payload || typeof payload !== 'object' || Array.isArray(payload)) {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
    }
    const messages = (payload as Record<string, unknown>).messages;
    const record = payload as Record<string, unknown>;
    const error = record.error;
    const success = record.success;
    const successValid = success === undefined || typeof success === 'boolean';
    if (response.ok && successValid && success !== false && (error === undefined || error === null)
      && Array.isArray(messages) && messages.length === 1
      && messages[0] && typeof messages[0] === 'object' && typeof (messages[0] as Record<string, unknown>).id === 'string'
      && ((messages[0] as Record<string, unknown>).id as string).trim()) {
      return { outcome: 'ACCEPTED', externalMessageId: (messages[0] as Record<string, unknown>).id as string };
    }
    const graphError = error && typeof error === 'object' && !Array.isArray(error) ? error as Record<string, unknown> : null;
    const graphCode = graphError?.code;
    const refusalErrorValid = graphError !== null && typeof graphError.message === 'string' && graphError.message.trim().length > 0
      && typeof graphCode === 'number' && Number.isSafeInteger(graphCode)
      && (graphError.is_transient === undefined || typeof graphError.is_transient === 'boolean');
    const noContradictoryReceipt = !Object.hasOwn(record, 'data')
      && (messages === undefined || Array.isArray(messages) && messages.length === 0);
    if ([400, 401, 403].includes(response.status) && refusalErrorValid
      && [10, 100, 190].includes(graphCode as number)
      && graphError?.is_transient !== true && successValid && success !== true && noContradictoryReceipt) {
      return { outcome: 'REJECTED', code: 'META_RECUSOU' };
    }
    if (response.ok && successValid && success !== false && (error === undefined || error === null)
      && Array.isArray(messages) && messages.length === 1 && messages[0] && typeof messages[0] === 'object'
      && !Object.hasOwn(messages[0], 'id')) {
      return { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'META_RECUSOU' };
    }
    return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
  }
}

```

### api-app/src/integrations/message-templates/template-management.resolver.ts

SHA256 `1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { ConflictException, Injectable } from '@nestjs/common';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
import type {
  MessageTemplateProvider,
  ResolvedTemplateManagement,
  TemplateManagementContext,
  TemplateManagementResolver,
  TemplateReference,
} from '../../domain/message-templates/template-management.ports';
import { BoundMetaMessageTemplateProvider, MetaTemplateClient, TemplateManagementProviderError } from '../meta/message-template.client';
import { metaAccountReference } from '../channels/account-reference';

interface TemplateProviderFactory {
  create(context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider;
}

class OfficialTemplateProviderFactory implements TemplateProviderFactory {
  create(context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider {
    return new BoundMetaMessageTemplateProvider(context, credential, wabaId, new MetaTemplateClient());
  }
}

/** Explicit allowlist: unsupported origins have no placeholder/no-op provider. */
class TemplateProviderFactoryRegistry {
  private readonly factories = new Map([['OFICIAL', new OfficialTemplateProviderFactory()]]);

  create(origin: string, context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider {
    const factory = this.factories.get(origin);
    if (!factory) throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    return factory.create(context, credential, wabaId);
  }
}

@Injectable()
export class ScopedTemplateManagementResolver implements TemplateManagementResolver {
  private readonly factories = new TemplateProviderFactoryRegistry();

  constructor(private readonly prisma: PrismaService, private readonly credentials: ChannelCredentialResolver) {}

  async resolve(reference: TemplateReference, options?: { readonly transaction?: Prisma.TransactionClient }): Promise<ResolvedTemplateManagement> {
    const database = options?.transaction ?? this.prisma;
    const channel = await database.buChannel.findFirst({
      where: { id: reference.channelId, buId: reference.buId },
      include: { providerIdentities: true, bu: { select: { mantenedoraId: true } } },
    });
    if (!channel || channel.generation !== reference.expectedGeneration || channel.type !== 'OFICIAL'
      || !channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const identity = channel.providerIdentities.find((row) => row.currentChannelId === channel.id);
    if (!identity || !identity.managedLifecycle || identity.provider !== 'OFICIAL' || identity.buId !== channel.buId
      || !channel.phoneNumberId || identity.externalResourceId !== channel.phoneNumberId || !channel.wabaId) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const credentialMetadata = await this.credentials.inspectActiveCredential(channel.id, channel.generation, { provider: 'OFICIAL', buId: channel.buId }, options?.transaction);
    if (!credentialMetadata.ready || credentialMetadata.version === null) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const context: TemplateManagementContext = Object.freeze({
      mantenedoraId: channel.bu.mantenedoraId,
      buId: channel.buId,
      channelId: channel.id,
      providerResourceIdentityId: identity.id,
      generation: channel.generation,
      pairingEpoch: channel.pairingEpoch,
      activeCredentialVersion: credentialMetadata.version,
      accountReference: metaAccountReference(channel.wabaId),
    });
    const credential = async (): Promise<string> => {
      const current = await this.credentials.resolve(channel.id, 'template-management');
      if (current.provider !== 'OFICIAL' || current.buId !== context.buId || current.channelId !== context.channelId
        || current.providerResourceIdentityId !== context.providerResourceIdentityId || current.generation !== context.generation
        || current.pairingEpoch !== context.pairingEpoch || current.activeCredentialVersion !== context.activeCredentialVersion
        || current.wabaId !== channel.wabaId || current.phoneNumberId !== channel.phoneNumberId
        || metaAccountReference(current.wabaId ?? '') !== context.accountReference || !current.accessToken) {
        throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
      }
      return current.accessToken;
    };
    const provider = this.factories.create(channel.type, context, credential, channel.wabaId);
    return Object.freeze({ context, provider });
  }
}

```

### api-app/src/domain/message-templates/template-observation.service.ts

SHA256 `41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488`. unchanged inherited pre-ST04 bytes.

```typescript
import { ConflictException, ForbiddenException, Inject, Injectable, NotFoundException, ServiceUnavailableException, UnauthorizedException } from '@nestjs/common';
import { Prisma, type MessageTemplateDraft } from '@prisma/client';
import { createHash, randomUUID } from 'node:crypto';
import { AccessService } from '../access/access.service';
import { atLeast, type Role } from '../access/role';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { TEMPLATE_MANAGEMENT_RESOLVER, type TemplateDefinition, type TemplateManagementContext, type TemplateManagementResolver, type TemplateReference, type TemplateSummary } from './template-management.ports';
import { templateDefinitionSemanticFingerprint } from './template-definition';
import { TEMPLATE_TRANSACTION_BOUNDARY, type TemplateTransactionBoundary } from './template-transaction-boundary';

export const TEMPLATE_OBSERVATION_CLOCK = Symbol('TEMPLATE_OBSERVATION_CLOCK');
export interface TemplateObservationClock { now(): Date }
const LEASE_MS = 60_000;
const DEBOUNCE_MS = 10_000;
const FRESH_MS = 300_000;

class ObservationCommitUnconfirmedError extends Error {}
type ObservationAuthRevalidation = (tx: Prisma.TransactionClient) => Promise<void>;

interface ProjectedSavedObservation {
  remoteTemplateId: string;
  status: string;
  name: string | null;
  language: string | null;
  category: string;
  parameterFormat: string;
  components: Prisma.JsonValue;
  supported: boolean;
  semanticFingerprint: string | null;
  available: boolean;
  safeCode: string | undefined;
  observedAt: Date;
  observedFence: string;
  eligible: boolean;
}

export interface TemplateObservationBinding {
  readonly mantenedoraId: string;
  readonly buId: string;
  readonly channelId: string;
  readonly providerResourceIdentityId: string;
  readonly accountReference: string;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
}

@Injectable()
export class TemplateObservationService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly access: AccessService,
    @Inject(TEMPLATE_MANAGEMENT_RESOLVER) private readonly resolver: TemplateManagementResolver,
    @Inject(TEMPLATE_TRANSACTION_BOUNDARY) private readonly transactions: TemplateTransactionBoundary,
    @Inject(TEMPLATE_OBSERVATION_CLOCK) private readonly clock: TemplateObservationClock,
  ) {}

  async refreshDraft(actorId: string, draftId: string, revalidateAuth?: ObservationAuthRevalidation) {
    const { draft } = await this.authorizeDraft(actorId, draftId);
    const reference = await this.currentReference(actorId, draft.buId, draft.channelId);
    const resolved = await this.resolver.resolve(reference);
    this.assertBinding(draft, resolved.context);
    const operation = await this.prisma.messageTemplateOperation.findFirst({
      where: { draftId, buId: draft.buId, mantenedoraId: draft.mantenedoraId },
      orderBy: [{ revision: 'desc' }], select: { remoteTemplateId: true, acknowledgedRemoteTemplateId: true, phase: true },
    });
    if (!operation?.remoteTemplateId || !['ACCEPTED', 'AMBIGUOUS'].includes(operation.phase)) {
      throw new ConflictException({ code: 'TEMPLATE_REMOTE_ID_UNAVAILABLE' });
    }
    const lease = await this.acquire(resolved.context);
    if (!lease.acquired) return { phase: 'REFRESH_IN_PROGRESS', retryAfter: 10 };
    try {
      const summary = await resolved.provider.getTemplate({ context: resolved.context, remoteTemplateId: operation.remoteTemplateId });
      const applied = await this.applyObservation(actorId, resolved.context, lease, summary, draftId, revalidateAuth);
      if (!applied) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      const projected = await this.projectObservation(resolved.context, summary.remoteTemplateId, draft.definition);
      if (operation.acknowledgedRemoteTemplateId && operation.acknowledgedRemoteTemplateId !== operation.remoteTemplateId) {
        return { ...projected, eligible: false, eligibleForUse: false, safeCode: 'PROVIDER_ACK_CONFLICT' };
      }
      return projected;
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      if (error instanceof ConflictException && error.getResponse() && (error.getResponse() as { code?: string }).code === 'TEMPLATE_REFRESH_SUPERSEDED') throw error;
      if (error instanceof ObservationCommitUnconfirmedError) throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      if (!await this.markUnavailableSafely(actorId, resolved.context, lease, operation.remoteTemplateId, null, 'TEMPLATE_REFRESH_UNAVAILABLE', undefined, revalidateAuth, draftId)) {
        throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      }
      throw new ConflictException({ code: 'TEMPLATE_REFRESH_UNAVAILABLE' });
    }
  }

  async refreshCatalog(actorId: string, buId: string, channelId: string, after: string | null, revalidateAuth?: ObservationAuthRevalidation) {
    await this.authorizeBu(actorId, buId);
    const currentReference = await this.currentReference(actorId, buId, channelId);
    const resolved = await this.resolver.resolve(currentReference);
    const lease = await this.acquire(resolved.context);
    if (!lease.acquired) return { phase: 'REFRESH_IN_PROGRESS', retryAfter: 10 };
    const cursorHash = this.hash(after ?? 'first-page');
    try {
      const page = await resolved.provider.listTemplates({ context: resolved.context, after, limit: 50 });
      const applied = await this.applyCatalogPage(actorId, resolved.context, lease, cursorHash, after, page.templates, page.nextCursor, revalidateAuth);
      if (!applied) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      return this.getCatalog(actorId, buId, channelId, after);
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      if (error instanceof ConflictException && error.getResponse() && (error.getResponse() as { code?: string }).code === 'TEMPLATE_REFRESH_SUPERSEDED') throw error;
      if (error instanceof ObservationCommitUnconfirmedError) throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      if (!await this.markUnavailableSafely(actorId, resolved.context, lease, null, cursorHash, 'TEMPLATE_CATALOG_UNAVAILABLE', after, revalidateAuth)) {
        throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      }
      throw new ConflictException({ code: 'TEMPLATE_CATALOG_UNAVAILABLE' });
    }
  }

  async getCatalog(actorId: string, buId: string, channelId: string, after: string | null) {
    await this.authorizeBu(actorId, buId);
    const currentReference = await this.currentReference(actorId, buId, channelId);
    const resolved = await this.resolver.resolve(currentReference);
    const cursorHash = this.hash(after ?? 'first-page');
    const page = await this.prisma.messageTemplateCatalogPage.findUnique({ where: { contextKey_cursorHash: { contextKey: this.contextKey(resolved.context), cursorHash } } });
    if (!page) return { items: [], nextCursor: null, available: false, safeCode: 'TEMPLATE_CATALOG_NOT_OBSERVED', observedAt: null };
    const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
    if (ids.length > 50) return { items: [], nextCursor: null, available: false,
      safeCode: 'TEMPLATE_CATALOG_INVALID', observedAt: page.observedAt };
    const rows = ids.length ? await this.prisma.$queryRaw<Array<{
      remoteTemplateId: string; status: string; name: string | null; language: string | null; category: string;
      parameterFormat: string; components: Prisma.JsonValue; supported: boolean; semanticFingerprint: string | null;
      available: boolean; safeCode: string | null; observedEligible: boolean; observedAt: Date; observedFence: bigint;
    }>>(Prisma.sql`
      WITH requested AS (
        SELECT remote_template_id, ordinality
        FROM unnest(ARRAY[${Prisma.join(ids)}]::varchar(128)[]) WITH ORDINALITY AS request(remote_template_id, ordinality)
      )
      SELECT observation.remote_template_id AS "remoteTemplateId", observation.status, observation.name, observation.language, observation.category,
        observation.parameter_format AS "parameterFormat", observation.components, observation.supported,
        observation.semantic_fingerprint AS "semanticFingerprint", observation.available, observation.safe_code AS "safeCode",
        observation.observed_eligible AS "observedEligible", observation.observed_at AS "observedAt", observation.observed_fence AS "observedFence"
      FROM requested
      CROSS JOIN LATERAL (
        SELECT remote_template_id, status, name, language, category, parameter_format, components, supported,
          semantic_fingerprint, available, safe_code, observed_eligible, observed_at, observed_fence
        FROM message_template_remote_observations
        WHERE context_key = ${page.contextKey}::char(64)
          AND remote_template_id = requested.remote_template_id
        LIMIT 1
      ) observation
      ORDER BY requested.ordinality`) : [];
    const byId = new Map(rows.map((row) => [row.remoteTemplateId, row]));
    const fresh = this.clock.now().getTime() - page.observedAt.getTime() <= FRESH_MS;
    return { items: ids.flatMap((id) => { const row = byId.get(id); return row ? [this.projectRow(row)] : []; }),
      nextCursor: page.nextCursor, available: page.available && fresh, safeCode: page.safeCode ?? (!fresh ? 'TEMPLATE_CATALOG_STALE' : undefined), observedAt: page.observedAt };
  }

  async projectSavedObservation(binding: TemplateObservationBinding, remoteTemplateId: string,
    definitionValue: unknown, acknowledgedRemoteTemplateId?: string | null): Promise<(ProjectedSavedObservation & { matchesDefinition: boolean; eligibleForUse: boolean }) | null> {
    const historicalContextKey = this.hash({ mantenedoraId: binding.mantenedoraId, buId: binding.buId,
      channelId: binding.channelId, accountReference: binding.accountReference,
      generation: binding.generation, pairingEpoch: binding.pairingEpoch,
      providerResourceIdentityId: binding.providerResourceIdentityId,
      activeCredentialVersion: binding.activeCredentialVersion });
    let currentContext: TemplateManagementContext | null = null;
    try {
      const channel = await this.prisma.buChannel.findFirst({ where: { id: binding.channelId, buId: binding.buId }, select: { generation: true } });
      if (channel) {
        const resolved = await this.resolver.resolve({ buId: binding.buId, channelId: binding.channelId, expectedGeneration: channel.generation });
        const sameResourceAssociation = resolved.context.mantenedoraId === binding.mantenedoraId
          && resolved.context.buId === binding.buId && resolved.context.channelId === binding.channelId
          && resolved.context.providerResourceIdentityId === binding.providerResourceIdentityId
          && resolved.context.accountReference === binding.accountReference;
        if (sameResourceAssociation) currentContext = resolved.context;
      }
    } catch { /* historical detail remains readable, but a stale binding cannot be eligible */ }

    const currentContextKey = currentContext ? this.contextKey(currentContext) : null;
    const currentRow = currentContextKey ? await this.prisma.messageTemplateRemoteObservation.findUnique({
      where: { contextKey_remoteTemplateId: { contextKey: currentContextKey, remoteTemplateId } },
    }) : null;
    const row = currentRow ?? (currentContextKey === historicalContextKey ? null
      : await this.prisma.messageTemplateRemoteObservation.findUnique({
        where: { contextKey_remoteTemplateId: { contextKey: historicalContextKey, remoteTemplateId } },
      }));
    if (!row) return null;
    const currentObservation = currentRow !== null;

    let matchesDefinition = false;
    try { matchesDefinition = row.semanticFingerprint !== null
      && row.semanticFingerprint === this.definitionFingerprint(definitionValue as TemplateDefinition); }
    catch { /* unsupported historical definitions cannot be considered a match */ }
    const projected = this.projectRow(row);
    const available = currentObservation && projected.available;
    const ackMatchesAssociation = !acknowledgedRemoteTemplateId || acknowledgedRemoteTemplateId === remoteTemplateId;
    const eligible = available && matchesDefinition && ackMatchesAssociation && row.supported && row.status === 'APPROVED';
    return { ...projected, available, eligible,
      ...(!currentObservation ? { safeCode: 'TEMPLATE_CONTEXT_STALE' }
        : !ackMatchesAssociation ? { safeCode: 'PROVIDER_ACK_CONFLICT' } : {}),
      matchesDefinition, eligibleForUse: eligible };
  }

  private async acquire(context: TemplateManagementContext): Promise<{ acquired: boolean; ownerId: string; fence: bigint; contextKey: string }> {
    const contextKey = this.contextKey(context);
    const ownerId = randomUUID();
    try { return await this.transactions.run('observation', async (tx) => {
      const now = this.clock.now();
      await tx.messageTemplateObservationLease.createMany({ data: [{
        contextKey, mantenedoraId: context.mantenedoraId, buId: context.buId,
        channelId: context.channelId, accountReference: context.accountReference,
        channelGeneration: context.generation, pairingEpoch: context.pairingEpoch,
        providerResourceIdentityId: context.providerResourceIdentityId,
        activeCredentialVersion: context.activeCredentialVersion ?? 0, fence: 0n,
      }], skipDuplicates: true });
      const current = await tx.messageTemplateObservationLease.findUniqueOrThrow({ where: { contextKey } });
      const debounceDone = !current.lastStartedAt || current.lastStartedAt.getTime() <= now.getTime() - DEBOUNCE_MS;
      const updated = debounceDone ? await tx.messageTemplateObservationLease.updateMany({
        where: { contextKey, lastStartedAt: current.lastStartedAt, OR: [{ leaseUntil: null }, { leaseUntil: { lte: now } }] },
        data: { ownerId, fence: { increment: 1n }, leaseUntil: new Date(now.getTime() + LEASE_MS), lastStartedAt: now },
      }) : { count: 0 };
      const latest = await tx.messageTemplateObservationLease.findUniqueOrThrow({ where: { contextKey } });
      return { acquired: updated.count === 1, ownerId, fence: latest.fence, contextKey };
    }); } catch (error) {
      if (error instanceof ConflictException) throw error;
      throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
    }
  }

  private async applyObservation(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, summary: TemplateSummary, draftId: string, revalidateAuth?: ObservationAuthRevalidation): Promise<boolean> {
    const observedAt = this.clock.now();
    try {
      return await this.transactions.run('observation', async (tx) => {
        await revalidateAuth?.(tx);
        await this.assertTxObservationAccess(tx, actorId, context, draftId);
        if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
        await this.writeObservation(tx, lease, observedAt, summary);
        await this.releaseLease(tx, lease);
        return true;
      });
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      try { if (await this.observationCommitted(lease, observedAt, summary)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async applyCatalogPage(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, cursorHash: string, after: string | null, summaries: readonly TemplateSummary[], nextCursor: string | null, revalidateAuth?: ObservationAuthRevalidation): Promise<boolean> {
    const observedAt = this.clock.now();
    try { return await this.transactions.run('observation', async (tx) => {
      await revalidateAuth?.(tx);
      await this.assertTxObservationAccess(tx, actorId, context);
      if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
      const remoteTemplateIds = summaries.map((summary) => summary.remoteTemplateId);
      for (const summary of summaries) await this.writeObservation(tx, lease, observedAt, summary);
      await tx.messageTemplateCatalogPage.upsert({
        where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
        create: { contextKey: lease.contextKey, cursorHash, requestedCursor: after, remoteTemplateIds: remoteTemplateIds as Prisma.InputJsonValue,
          nextCursor, available: true, safeCode: null, observedAt, observedFence: lease.fence },
        update: { requestedCursor: after, remoteTemplateIds: remoteTemplateIds as Prisma.InputJsonValue, nextCursor,
          available: true, safeCode: null, observedAt, observedFence: lease.fence },
      });
      await this.releaseLease(tx, lease);
      return true;
    }); } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      try { if (await this.catalogPageCommitted(lease, cursorHash, observedAt, summaries, nextCursor)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async writeObservation(tx: Prisma.TransactionClient, lease: { fence: bigint; contextKey: string }, observedAt: Date, summary: TemplateSummary): Promise<void> {
    const observedEligible = summary.supported && summary.status === 'APPROVED';
    await tx.messageTemplateRemoteObservation.upsert({
      where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId } },
      create: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId, status: summary.status,
        name: summary.name, language: summary.language, category: summary.category, parameterFormat: summary.parameterFormat,
        components: summary.components as unknown as Prisma.InputJsonValue, semanticFingerprint: summary.semanticFingerprint,
        supported: summary.supported, available: true, safeCode: null, observedEligible, observedAt, observedFence: lease.fence },
      update: { status: summary.status, name: summary.name, language: summary.language, category: summary.category,
        parameterFormat: summary.parameterFormat, components: summary.components as unknown as Prisma.InputJsonValue,
        semanticFingerprint: summary.semanticFingerprint, supported: summary.supported, available: true,
        safeCode: null, observedEligible, observedAt, observedFence: lease.fence },
    });
  }

  private async observationCommitted(lease: { fence: bigint; contextKey: string }, observedAt: Date, summary: TemplateSummary): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    const row = await this.prisma.messageTemplateRemoteObservation.findUnique({
      where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId } },
      select: { observedAt: true, observedFence: true, semanticFingerprint: true, available: true,
        status: true, name: true, language: true, category: true, parameterFormat: true, components: true, supported: true },
    });
    return Boolean(row && row.observedFence === lease.fence && row.observedAt.getTime() === observedAt.getTime()
      && row.semanticFingerprint === summary.semanticFingerprint && row.available
      && this.sameSummary(row, summary));
  }

  private async catalogPageCommitted(lease: { fence: bigint; contextKey: string }, cursorHash: string, observedAt: Date, summaries: readonly TemplateSummary[], nextCursor: string | null): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    const page = await this.prisma.messageTemplateCatalogPage.findUnique({
      where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
      select: { observedAt: true, observedFence: true, available: true, nextCursor: true, remoteTemplateIds: true },
    });
    if (!page || page.observedFence !== lease.fence || page.observedAt.getTime() !== observedAt.getTime()
      || !page.available || page.nextCursor !== nextCursor) return false;
    const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds : [];
    if (ids.length !== summaries.length || !summaries.every((summary, i) => ids[i] === summary.remoteTemplateId)) return false;
    if (!ids.length) return true;
    const rows = await this.prisma.messageTemplateRemoteObservation.findMany({
      where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids as string[] }, observedFence: lease.fence, observedAt, available: true },
      select: { remoteTemplateId: true, status: true, name: true, language: true, category: true,
        parameterFormat: true, components: true, supported: true, semanticFingerprint: true },
    });
    const byId = new Map(rows.map((row) => [row.remoteTemplateId, row]));
    return rows.length === ids.length && summaries.every((summary) => {
      const row = byId.get(summary.remoteTemplateId);
      return Boolean(row && row.semanticFingerprint === summary.semanticFingerprint && this.sameSummary(row, summary));
    });
  }

  private async markUnavailable(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, remoteId: string | null, cursorHash: string | null, safeCode: string, requestedCursor: string | null = null, revalidateAuth?: ObservationAuthRevalidation, draftId?: string): Promise<boolean> {
    const observedAt = this.clock.now();
    try { return await this.transactions.run('observation', async (tx) => {
      await revalidateAuth?.(tx);
      await this.assertTxObservationAccess(tx, actorId, context, draftId);
      if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
      if (remoteId) await tx.messageTemplateRemoteObservation.updateMany({
        where: { contextKey: lease.contextKey, remoteTemplateId: remoteId },
        data: { available: false, observedEligible: false, safeCode, observedFence: lease.fence },
      });
      if (cursorHash) {
        const page = await tx.messageTemplateCatalogPage.findUnique({ where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } }, select: { remoteTemplateIds: true } });
        const ids = Array.isArray(page?.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
        if (ids.length) await tx.messageTemplateRemoteObservation.updateMany({
          where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids } },
          data: { available: false, observedEligible: false, safeCode, observedFence: lease.fence },
        });
        await tx.messageTemplateCatalogPage.upsert({
          where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
          create: { contextKey: lease.contextKey, cursorHash, requestedCursor,
            remoteTemplateIds: [] as unknown as Prisma.InputJsonValue, nextCursor: null,
            available: false, safeCode, observedAt, observedFence: lease.fence },
          update: { available: false, safeCode, observedFence: lease.fence },
        });
      }
      await this.releaseLease(tx, lease);
      return true;
    }); } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      try { if (await this.unavailableCommitted(lease, remoteId, cursorHash, safeCode)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async markUnavailableSafely(actorId: string, context: TemplateManagementContext,
    lease: { ownerId: string; fence: bigint; contextKey: string }, remoteId: string | null,
    cursorHash: string | null, safeCode: string, requestedCursor: string | null = null,
    revalidateAuth?: ObservationAuthRevalidation, draftId?: string): Promise<boolean> {
    try { return await this.markUnavailable(actorId, context, lease, remoteId, cursorHash, safeCode, requestedCursor, revalidateAuth, draftId); }
    catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      if (error instanceof ObservationCommitUnconfirmedError) {
        throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      }
      throw error;
    }
  }

  private async releaseLeaseAfterAuthorizationFailure(lease: { ownerId: string; fence: bigint; contextKey: string }): Promise<void> {
    try { await this.transactions.run('observation', (tx) => this.releaseLease(tx, lease)); }
    catch { /* authorization response remains authoritative; the bounded lease expires if cleanup cannot be confirmed */ }
  }

  private async unavailableCommitted(lease: { fence: bigint; contextKey: string }, remoteId: string | null, cursorHash: string | null, safeCode: string): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    if (remoteId) {
      const row = await this.prisma.messageTemplateRemoteObservation.findUnique({
        where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: remoteId } },
        select: { available: true, safeCode: true, observedFence: true },
      });
      return Boolean(row && !row.available && row.safeCode === safeCode && row.observedFence === lease.fence);
    }
    if (cursorHash) {
      const page = await this.prisma.messageTemplateCatalogPage.findUnique({
        where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
        select: { available: true, safeCode: true, observedFence: true, remoteTemplateIds: true },
      });
      if (!page || page.available || page.safeCode !== safeCode || page.observedFence !== lease.fence) return false;
      const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
      if (!ids.length) return true;
      const rows = await this.prisma.messageTemplateRemoteObservation.findMany({
        where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids }, available: false, safeCode, observedFence: lease.fence },
        select: { remoteTemplateId: true },
      });
      return rows.length === ids.length;
    }
    return false;
  }

  private sameSummary(row: { status: string; name: string | null; language: string | null; category: string;
    parameterFormat: string; components: Prisma.JsonValue; supported: boolean }, summary: TemplateSummary): boolean {
    return row.status === summary.status && row.name === summary.name && row.language === summary.language
      && row.category === summary.category && row.parameterFormat === summary.parameterFormat
      && row.supported === summary.supported
      && JSON.stringify(row.components) === JSON.stringify(summary.components);
  }

  private async ownsLease(tx: Prisma.TransactionClient, actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, now: Date): Promise<boolean> {
    const lock = await tx.$queryRaw<Array<{ contextKey: string }>>`SELECT context_key AS "contextKey" FROM message_template_observation_leases WHERE context_key = ${lease.contextKey} FOR UPDATE`;
    if (lock.length !== 1) return false;
    const current = await tx.messageTemplateObservationLease.findFirst({ where: {
      contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: now },
      mantenedoraId: context.mantenedoraId, buId: context.buId, channelId: context.channelId, accountReference: context.accountReference,
      channelGeneration: context.generation, pairingEpoch: context.pairingEpoch,
      providerResourceIdentityId: context.providerResourceIdentityId, activeCredentialVersion: context.activeCredentialVersion ?? 0,
    }, select: { contextKey: true } });
    if (!current) return false;
    // Pin all mutable inputs while resolver rechecks the same transaction snapshot.
    await tx.$queryRaw`SELECT id FROM app_users WHERE id = ${actorId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${context.buId} AND mantenedora_id = ${context.mantenedoraId} FOR UPDATE`;
    await tx.$queryRaw`SELECT user_id FROM user_bu_roles WHERE user_id = ${actorId} AND bu_id = ${context.buId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${context.channelId} AND bu_id = ${context.buId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} AND current_channel_id = ${context.channelId} FOR UPDATE`;
    await tx.$queryRaw`SELECT channel_id FROM channel_credentials WHERE channel_id = ${context.channelId} FOR UPDATE`;
    const checkedAt = this.clock.now();
    const stillOwned = await tx.messageTemplateObservationLease.findFirst({ where: {
      contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: checkedAt },
    }, select: { contextKey: true } });
    if (!stillOwned) return false;
    const [actor, bu, grant] = await Promise.all([
      tx.appUser.findFirst({ where: { id: actorId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.businessUnit.findFirst({ where: { id: context.buId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.userBuRole.findUnique({ where: { userId_buId: { userId: actorId, buId: context.buId } }, select: { userId: true } }),
    ]);
    if (!actor || !bu || !grant) return false;
    try {
      const actual = await this.resolver.resolve({ buId: context.buId, channelId: context.channelId, expectedGeneration: context.generation }, { transaction: tx });
      return this.sameContext(context, actual.context);
    } catch { return false; }
  }

  private async releaseLease(tx: Prisma.TransactionClient, lease: { ownerId: string; fence: bigint; contextKey: string }): Promise<void> {
    const checkedAt = this.clock.now();
    const released = await tx.messageTemplateObservationLease.updateMany({ where: { contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: checkedAt } }, data: { ownerId: null, leaseUntil: null } });
    if (released.count !== 1) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
  }

  private async projectObservation(context: TemplateManagementContext, remoteId: string, definitionValue: Prisma.JsonValue) {
    const row = await this.prisma.messageTemplateRemoteObservation.findUnique({ where: { contextKey_remoteTemplateId: { contextKey: this.contextKey(context), remoteTemplateId: remoteId } } });
    if (!row) throw new ConflictException({ code: 'TEMPLATE_REFRESH_UNAVAILABLE' });
    const definition = definitionValue as unknown as TemplateDefinition;
    const current = row.semanticFingerprint !== null && row.semanticFingerprint === this.definitionFingerprint(definition);
    return { ...this.projectRow(row), matchesDefinition: current,
      eligibleForUse: current && row.available && row.supported && row.status === 'APPROVED'
        && this.clock.now().getTime() - row.observedAt.getTime() <= FRESH_MS };
  }

  private projectRow(row: { remoteTemplateId: string; status: string; name: string | null; language: string | null; category: string; parameterFormat: string; components: Prisma.JsonValue; supported: boolean; semanticFingerprint: string | null; available: boolean; safeCode: string | null; observedEligible: boolean; observedAt: Date; observedFence: bigint }): ProjectedSavedObservation {
    const current = this.clock.now().getTime() - row.observedAt.getTime() <= FRESH_MS;
    return { remoteTemplateId: row.remoteTemplateId, status: row.status, name: row.name, language: row.language,
      category: row.category, parameterFormat: row.parameterFormat, components: row.components,
      supported: row.supported, semanticFingerprint: row.semanticFingerprint,
      available: row.available && current, safeCode: row.safeCode ?? undefined,
      observedAt: row.observedAt, observedFence: row.observedFence.toString(),
      eligible: row.available && current && row.observedEligible && row.supported && row.status === 'APPROVED' };
  }

  private async authorizeDraft(actorId: string, draftId: string) {
    const actor = await this.prisma.appUser.findUnique({ where: { id: actorId }, select: { mantenedoraId: true, status: true } });
    if (!actor || actor.status !== 'ATIVO') throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
    const grants = await this.access.grantsDoUsuario(actorId);
    const draft = await this.prisma.messageTemplateDraft.findFirst({ where: { id: draftId, mantenedoraId: actor.mantenedoraId, buId: { in: grants.map((grant) => grant.buId) } } });
    const grant = draft && grants.find((row) => row.buId === draft.buId);
    if (!draft || !grant || (draft.creatorUserId !== actorId && !atLeast(grant.role, 'ADMIN'))) throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
    return { draft, role: grant.role as Role };
  }

  private async assertTxObservationAccess(tx: Prisma.TransactionClient, actorId: string,
    context: TemplateManagementContext, draftId?: string): Promise<void> {
    const [actor, bu, grants] = await Promise.all([
      tx.appUser.findFirst({ where: { id: actorId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.businessUnit.findFirst({ where: { id: context.buId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.$queryRaw<Array<{ role: Role }>>`SELECT role::text AS role FROM user_bu_roles
        WHERE user_id = ${actorId} AND bu_id = ${context.buId} FOR SHARE`,
    ]);
    if (!actor) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    if (!bu) throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    const role = grants[0]?.role;
    if (!role) throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
    if (draftId) {
      const draft = await tx.messageTemplateDraft.findFirst({ where: {
        id: draftId, buId: context.buId, mantenedoraId: context.mantenedoraId,
        channelId: context.channelId, providerResourceIdentityId: context.providerResourceIdentityId,
        accountReference: context.accountReference,
      }, select: { creatorUserId: true } });
      if (!draft) throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
      if (draft.creatorUserId !== actorId && !atLeast(role, 'ADMIN')) {
        throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
      }
    } else if (!atLeast(role, 'ATENDENTE')) {
      throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
    }
  }

  private isAuthOrAccessFailure(error: unknown): boolean {
    return error instanceof UnauthorizedException || error instanceof ForbiddenException || error instanceof NotFoundException;
  }

  private async authorizeBu(actorId: string, buId: string): Promise<void> {
    const scoped = await this.access.resolverBu(actorId, buId);
    const actor = await this.prisma.appUser.findUnique({ where: { id: actorId }, select: { mantenedoraId: true, status: true } });
    const bu = await this.prisma.businessUnit.findUnique({ where: { id: buId }, select: { mantenedoraId: true, status: true } });
    if (!scoped || !actor || actor.status !== 'ATIVO' || !bu || bu.status !== 'ATIVO' || actor.mantenedoraId !== bu.mantenedoraId) {
      throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    }
  }

  private assertBinding(draft: MessageTemplateDraft, context: TemplateManagementContext): void {
    if (draft.mantenedoraId !== context.mantenedoraId || draft.channelId !== context.channelId || draft.providerResourceIdentityId !== context.providerResourceIdentityId) throw new ConflictException({ code: 'TEMPLATE_CHANNEL_CONTEXT_STALE' });
    if (draft.accountReference !== context.accountReference) throw new ConflictException({ code: 'CONTA_ALTERADA' });
  }

  private sameContext(a: TemplateManagementContext, b: TemplateManagementContext): boolean {
    return a.mantenedoraId === b.mantenedoraId && a.buId === b.buId && a.channelId === b.channelId && a.accountReference === b.accountReference
      && a.providerResourceIdentityId === b.providerResourceIdentityId && a.generation === b.generation
      && a.pairingEpoch === b.pairingEpoch && a.activeCredentialVersion === b.activeCredentialVersion;
  }

  private async currentReference(actorId: string, buId: string, channelId: string): Promise<TemplateReference> {
    await this.authorizeBu(actorId, buId);
    const channel = await this.prisma.buChannel.findFirst({ where: { id: channelId, buId }, select: { generation: true } });
    if (!channel) throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    return { buId, channelId, expectedGeneration: channel.generation };
  }
  private contextKey(context: TemplateManagementContext): string { return this.hash({ mantenedoraId: context.mantenedoraId, buId: context.buId, channelId: context.channelId, accountReference: context.accountReference, generation: context.generation, pairingEpoch: context.pairingEpoch, providerResourceIdentityId: context.providerResourceIdentityId, activeCredentialVersion: context.activeCredentialVersion }); }
  private hash(value: unknown): string { return createHash('sha256').update(this.canonicalJson(value)).digest('hex'); }
  private canonicalJson(value: unknown): string {
    if (Array.isArray(value)) return `[${value.map((item) => this.canonicalJson(item)).join(',')}]`;
    if (value && typeof value === 'object') {
      const row = value as Record<string, unknown>;
      return `{${Object.keys(row).filter((key) => key !== 'example').sort().map((key) => `${JSON.stringify(key)}:${this.canonicalJson(row[key])}`).join(',')}}`;
    }
    return JSON.stringify(value) ?? 'null';
  }
  private definitionFingerprint(definition: TemplateDefinition): string {
    return templateDefinitionSemanticFingerprint(definition);
  }
}

```

### api-app/src/surfaces/bff/conversations.controller.ts

SHA256 `f8682cc211695df59caaa3f32799ad6a0444e120d683592e32984a71d71c8c1d`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { BadRequestException, Body, Controller, Get, HttpCode, NotFoundException, Param, Post, Query, Req, Res } from '@nestjs/common';
import type { Request, Response } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { RegistroDeAtividade } from '../../domain/historico/registro.service';
import { ator } from './setores.controller';
import { validarConsultaTimeline } from '../../domain/inbox/timeline-pagination';
import { ConversationStartService } from '../../domain/inbox/conversation-start.service';
import { InitialMessageService } from '../../domain/inbox/initial-message.service';
import { SessionService } from '../../infra/session/session.service';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';

const ABAS = ['QUEUED', 'IN_SERVICE', 'CLOSED'] as const;

/** A inbox por BU (ADR-0009): uma tela para os dois canais. */
@Controller('api/bff')
export class ConversationsController {
  constructor(
    private readonly access: AccessService,
    private readonly conversas: ConversationsService,
    private readonly registro: RegistroDeAtividade,
    private readonly conversationStart: ConversationStartService,
    private readonly initialMessages: InitialMessageService,
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
  ) {}

  @Post('business-units/:buId/conversations/open')
  @HttpCode(200)
  async abrirPorContato(
    @Param('buId') buId: string,
    @Body() body: { telefone?: unknown },
    @Req() req: Request,
    @Res({ passthrough: true }) response: Response,
  ) {
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    await this.assertActorTenant(req, buId);
    if (!body || typeof body !== 'object' || Object.keys(body).some((key) => key !== 'telefone')
      || typeof body.telefone !== 'string') {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    const result = await this.conversationStart.start(buId, body.telefone);
    if (result.created) {
      await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.conversa.aberta', ator(req), {
        buId,
        entidadeId: result.conversation.id,
        frase: { contato: result.conversation.contact },
      });
    }
    response.status(result.created ? 201 : 200);
    return {
      conversaId: result.conversation.id,
      criada: result.created,
      contact: result.conversation.contact,
    };
  }

  @Get('conversations/:id/start-options')
  async startOptions(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    return this.initialMessages.options({ conversationId: conversa.id, buId: conversa.buId });
  }

  @Post('conversations/:id/initial-message-preview')
  @HttpCode(200)
  async initialPreview(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    const message = this.initialMessageRequest(body, false);
    return this.initialMessages.preview({ conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id, message });
  }

  @Post('conversations/:id/initial-messages')
  async initialSend(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) response: Response) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    const key = req.header('Idempotency-Key') ?? '';
    const message = this.initialMessageRequest(body, true);
    const result = await this.initialMessages.submit({
      conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id, actorName: req.usuario!.nome,
      idempotencyKey: key, message: message as never,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
    });
    const { expiredPrepared, ...safeResult } = result;
    const active = ['SENDING', 'EXTERNAL_ACCEPTED'].includes(result.attempt.state)
      || result.attempt.state === 'PREPARED' && !expiredPrepared;
    response.status(result.expiredPrepared ? 409 : active ? 202 : result.replay ? 200 : result.attempt.state === 'SUCCEEDED' ? 201 : 409);
    return expiredPrepared ? { ...safeResult, code: 'INITIAL_ATTEMPT_EXPIRED' } : safeResult;
  }

  @Get('conversations/:id/initial-messages/:attemptId')
  async initialAttempt(@Param('id') id: string, @Param('attemptId') attemptId: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertUuid(attemptId);
    return this.initialMessages.getAttempt({ id: attemptId, conversationId: conversa.id, buId: conversa.buId });
  }

  @Post('conversations/:id/initial-messages/:attemptId/reconcile')
  @HttpCode(200)
  async reconcileInitial(@Param('id') id: string, @Param('attemptId') attemptId: string, @Body() body: unknown, @Req() req: Request, @Res({ passthrough: true }) response: Response) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(attemptId);
    const result = await this.initialMessages.reconcile({ id: attemptId, conversationId: conversa.id, buId: conversa.buId,
      actorId: req.usuario!.id, actorName: req.usuario!.nome,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx) });
    if (['PREPARED', 'SENDING'].includes(result.state)) response.status(202);
    return result;
  }

  @Post('conversations/:id/initial-messages/:attemptId/acknowledge')
  @HttpCode(200)
  async acknowledgeInitial(@Param('id') id: string, @Param('attemptId') attemptId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(attemptId);
    return this.initialMessages.acknowledge({ id: attemptId, conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id,
      confirmed: req.header('X-Confirm-Duplication-Risk') === 'true', validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
      auditInTransaction: (tx) => this.registro.registrar(tx, req.usuario!.mantenedoraId, 'atendimento.initial.risk_acknowledged', ator(req), { buId: conversa.buId, entidadeId: attemptId }) });
  }

  @Post('conversations/:id/dispatch-admissions/:admissionId/reconcile')
  @HttpCode(200)
  async reconcileAdmission(@Param('id') id: string, @Param('admissionId') admissionId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(admissionId);
    return this.initialMessages.reconcileOrdinary({ id: admissionId, conversationId: conversa.id, buId: conversa.buId,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx) });
  }

  @Post('conversations/:id/dispatch-admissions/:admissionId/acknowledge')
  @HttpCode(200)
  async acknowledgeAdmission(@Param('id') id: string, @Param('admissionId') admissionId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(admissionId);
    return this.initialMessages.acknowledgeOrdinary({ id: admissionId, conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id,
      confirmed: req.header('X-Confirm-Duplication-Risk') === 'true', validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
      auditInTransaction: (tx) => this.registro.registrar(tx, req.usuario!.mantenedoraId, 'atendimento.dispatch.risk_acknowledged', ator(req), { buId: conversa.buId, entidadeId: admissionId }) });
  }

  private initialMessageRequest(body: Record<string, unknown>, includeFingerprint: boolean) {
    if (!body || typeof body !== 'object' || Array.isArray(body)) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    const allowed = ['channelId', 'expectedGeneration', 'mensagem', ...(includeFingerprint ? ['previewFingerprint'] : [])];
    if (Object.keys(body).some((key) => !allowed.includes(key)) || typeof body.channelId !== 'string'
      || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(body.channelId)
      || !Number.isSafeInteger(body.expectedGeneration) || (body.expectedGeneration as number) < 1
      || includeFingerprint && (typeof body.previewFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(body.previewFingerprint))) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    const message = body.mensagem;
    if (!message || typeof message !== 'object' || Array.isArray(message)) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    const row = message as Record<string, unknown>;
    const base = { channelId: body.channelId, expectedGeneration: body.expectedGeneration as number };
    const preview = includeFingerprint ? { previewFingerprint: body.previewFingerprint as string } : {};
    if (row.tipo === 'TEXTO') {
      if (Object.keys(row).some((key) => !['tipo', 'texto'].includes(key)) || typeof row.texto !== 'string'
        || !row.texto.trim() || [...row.texto].length > 4096) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
      return { ...base, kind: 'text' as const, text: row.texto, ...preview };
    }
    if (row.tipo !== 'TEMPLATE' || Object.keys(row).some((key) => !['tipo', 'templateId', 'language', 'catalogAfter', 'expectedDefinitionFingerprint', 'parameters'].includes(key))
      || typeof row.templateId !== 'string' || !row.templateId || row.templateId.length > 128
      || typeof row.language !== 'string' || !row.language || row.language.length > 16
      || row.catalogAfter !== undefined && (typeof row.catalogAfter !== 'string' || row.catalogAfter.length < 1 || row.catalogAfter.length > 512)
      || typeof row.expectedDefinitionFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(row.expectedDefinitionFingerprint)
      || !row.parameters || typeof row.parameters !== 'object'
      || Array.isArray(row.parameters) && (row.parameters.length > 20 || row.parameters.some((value) => typeof value !== 'string' || !value || [...value].length > 1024))
      || !Array.isArray(row.parameters) && (Object.keys(row.parameters as object).length > 20 || Object.values(row.parameters as Record<string, unknown>).some((value) => typeof value !== 'string' || !value || [...value].length > 1024))) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    return { ...base, kind: 'approved-template' as const, remoteTemplateId: row.templateId, language: row.language,
      catalogAfter: typeof row.catalogAfter === 'string' ? row.catalogAfter : null,
      expectedDefinitionFingerprint: row.expectedDefinitionFingerprint,
      values: row.parameters as Record<string, string> | string[], ...preview };
  }

  private assertEmptyBody(body: unknown): void {
    if (body !== undefined && (!body || typeof body !== 'object' || Array.isArray(body) || Object.keys(body).length !== 0)) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
  }

  private assertUuid(value: string): void {
    if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(value)) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
  }

  private async currentActorHasGrant(req: Request, buId: string, tx: Prisma.TransactionClient): Promise<boolean> {
    const cookie = this.sessions.extrairDoCabecalho(req.headers.cookie);
    const claimsAtRequest = this.sessions.verificar(cookie);
    if (!claimsAtRequest || claimsAtRequest.uid !== req.usuario!.id) return false;
    const rows = await tx.$queryRaw<Array<{ id: string; user_status: string; password_changed_at: Date | null;
      user_mantenedora_id: string; bu_status: string; bu_mantenedora_id: string; role: string }>>`
      SELECT u.id, u.status::text AS user_status, u.password_changed_at,
        u.mantenedora_id AS user_mantenedora_id, b.status::text AS bu_status,
        b.mantenedora_id AS bu_mantenedora_id, r.role::text AS role
      FROM app_users u
      JOIN user_bu_roles r ON r.user_id = u.id AND r.bu_id = ${buId}
      JOIN business_units b ON b.id = r.bu_id
      WHERE u.id = ${claimsAtRequest.uid}
      FOR SHARE OF u, r, b`;
    const current = rows[0];
    const claimsNow = this.sessions.verificar(cookie);
    return Boolean(current && claimsNow && claimsNow.uid === claimsAtRequest.uid
      && claimsNow.iat === claimsAtRequest.iat && claimsNow.exp === claimsAtRequest.exp
      && claimsNow.exp > Date.now() && current.user_status === 'ATIVO'
      && current.bu_status === 'ATIVO' && current.user_mantenedora_id === current.bu_mantenedora_id
      && (!current.password_changed_at || current.password_changed_at.getTime() <= claimsNow.iat)
      && ['ATENDENTE', 'ADMIN', 'OWNER'].includes(current.role));
  }

  /** New initial-contact routes require the actor's home tenant to match the BU. */
  private async assertActorTenant(req: Request, buId: string): Promise<void> {
    const rows = await this.prisma.$queryRaw<Array<{ user_id: string; user_mantenedora_id: string; bu_mantenedora_id: string; user_status: string; bu_status: string }>>`
      SELECT u.id AS user_id, u.mantenedora_id AS user_mantenedora_id,
        b.mantenedora_id AS bu_mantenedora_id, u.status::text AS user_status,
        b.status::text AS bu_status
      FROM app_users u CROSS JOIN business_units b
      WHERE u.id = ${req.usuario!.id} AND b.id = ${buId}`;
    const row = rows[0];
    if (!row || row.user_status !== 'ATIVO' || row.bu_status !== 'ATIVO'
      || row.user_mantenedora_id !== row.bu_mantenedora_id) throw new NotFoundException();
  }

  @Get('business-units/:buId/conversations')
  async listar(
    @Param('buId') buId: string,
    @Query() q: Record<string, string>,
    @Req() req: Request,
  ) {
    // Estar no escopo BASTA: com o eixo de capacidades dissolvido (ADR-0018 §3),
    // quem tem grant na BU atende as conversas dela. Era isso que a capacidade
    // ATENDIMENTO dizia, e agora quem diz é o papel.
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');

    const aba = q.aba?.toUpperCase();
    const r = await this.conversas.listar(buId, {
      grupos: aba === 'GRUPO',
      status: ABAS.includes(aba as (typeof ABAS)[number]) ? aba : undefined,
      minhas: q.minhas === 'true' ? req.usuario!.id : undefined,
      pagina: q.pagina ? Number(q.pagina) : undefined,
      limite: q.limite ? Number(q.limite) : undefined,
    });
    // O setor sobe achatado, como a tela o consome (`conversa.setor`).
    return {
      total: r.total,
      pagina: r.pagina,
      temMais: r.temMais,
      conversations: r.conversas.map(({ bu, ...c }) => ({ ...c, setor: bu.setor.name })),
    };
  }

  @Get('conversations/:id/messages')
  async thread(@Param('id') id: string, @Query() q: Record<string, unknown>, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    // Validar somente depois do resolver: recurso fora do escopo permanece 404,
    // mesmo quando os parâmetros enviados são inválidos.
    const consulta = validarConsultaTimeline(q);
    const timeline = await this.conversas.timeline(
      conversa.id, consulta.limite, consulta.antes, consulta.marcarLida,
    );

    const janela = await this.conversas.estadoDaJanela(conversa.id, conversa.buId);
    return {
      conversa: {
        id: conversa.id,
        contato: conversa.contact,
        nome: conversa.displayName,
        status: conversa.status,
        atendente: conversa.attendantName,
      },
      // O front precisa saber que "responder" pode estar indisponível, e por quê.
      janela: {
        exigida: janela.exigeJanela,
        aberta: janela.aberta,
        expiraEm: janela.expiraEm,
        canal: janela.canal?.type ?? null,
        disponivel: janela.disponivel,
        motivo: janela.motivoIndisponibilidade,
      },
      messages: timeline.messages,
      paginacao: timeline.paginacao,
    };
  }

  @Post('conversations/:id/messages')
  @HttpCode(201)
  async responder(@Param('id') id: string, @Body() body: { texto?: string }, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);

    const texto = String(body?.texto ?? '').trim();
    if (!texto) throw new BadRequestException({ error: 'Escreva uma mensagem.', code: 'TEXTO_VAZIO' });
    if (texto.length > 4096) {
      throw new BadRequestException({ error: 'Mensagem muito longa (máx. 4096).', code: 'TEXTO_LONGO' });
    }

    await this.initialMessages.assertOrdinaryDispatchAllowed(conversa.id, conversa.buId);

    const m = await this.conversas.responder(conversa.id, conversa.buId, texto, {
      kind: 'BFF',
      userId: req.usuario!.id,
      name: req.usuario!.nome,
    });
    return { id: m.id, canal: m.channelOrigin, em: m.createdAt };
  }

  @Post('conversations/:id/claim')
  async assumir(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);

    const c = await this.conversas.assumir(conversa.id, { userId: req.usuario!.id, nome: req.usuario!.nome });
    await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.assumido', ator(req), {
      buId: conversa.buId,
      entidadeId: conversa.id,
      frase: { contato: conversa.contact },
    });
    return { id: c.id, status: c.status, atendente: c.attendantName };
  }

  @Post('conversations/:id/close')
  async finalizar(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);

    const c = await this.conversas.finalizar(conversa.id);
    await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.encerrado', ator(req), {
      buId: conversa.buId,
      entidadeId: conversa.id,
      frase: { contato: conversa.contact },
    });
    return { id: c.id, status: c.status };
  }

  /** Escopo primeiro: fora dele, 404 — inclusive para BU de outra Mantenedora. */
  private async resolver(conversaId: string, req: Request) {
    const escopo = await this.access.escopo(req.usuario!.id);
    const conversa = await this.conversas.carregarNoEscopo(conversaId, escopo);
    const bu = await exigirPapelNaBu(this.access, req.usuario!.id, conversa.buId, 'ATENDENTE');
    return { conversa, papel: bu.papel };
  }
}

```

### api-app/src/surfaces/bff/session.middleware.ts

SHA256 `80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { ConflictException, ForbiddenException, Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common';
import type { NextFunction, Request, Response } from 'express';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { SessionService } from '../../infra/session/session.service';

export interface UsuarioDaSessao {
  id: string;
  mantenedoraId: string;
  nome: string;
  email: string;
  precisaTrocarSenha: boolean;
}

declare global {
  // eslint-disable-next-line @typescript-eslint/no-namespace
  namespace Express {
    interface Request {
      usuario?: UsuarioDaSessao;
    }
  }
}

/** Rotas liberadas dentro do BFF: são o que existe ANTES de haver sessão. */
const PUBLICAS = new Set([
  '/api/bff/auth/login',
  // Convite e recuperação (ADR-0025 §6): quem pede recuperação não tem sessão
  // por definição, e quem aceita convite ainda não tem conta utilizável. Não
  // viram superfície nova — a plateia é a mesma do login: a tela.
  '/api/bff/auth/recuperar',
]);

/** As rotas de token carregam o valor no caminho, então casam por prefixo. */
const PUBLICAS_POR_PREFIXO = ['/api/bff/auth/token/'];

/** Enquanto a troca inicial não acontece, só estas respondem (ADR-0007 §4). */
const LIBERADAS_EM_TROCA_OBRIGATORIA = new Set(['/api/bff/me', '/api/bff/me/password', '/api/bff/auth/logout']);

/**
 * Enquanto o wizard não termina, só estas respondem (ADR-0016 §4).
 *
 * A ORDEM É `senha → wizard → produto` (ADR-0016, Emenda 1 §3), e é a razão de
 * o wizard NÃO estar na lista acima: a troca de senha é trava de SEGURANÇA — a
 * credencial do bootstrap passou por fora do produto — e o wizard é onboarding
 * de PRODUTO. Segurança primeiro. Sem essa ordem, o OWNER recém-criado fica
 * preso entre os dois portões sem rota para nenhum.
 */
const LIBERADAS_EM_ONBOARDING = new Set([
  '/api/bff/me',
  '/api/bff/me/password',
  '/api/bff/auth/logout',
  '/api/bff/onboarding',
]);

/**
 * Guard da superfície BFF (ADR-0006): montado no PREFIXO, então rota nova nasce
 * exigindo sessão sem ninguém lembrar de anotá-la.
 *
 * O cookie prova que ele é autêntico — não que o acesso continua válido AGORA.
 * Por isso o usuário é relido do banco a cada request (ADR-0007 §1).
 */
@Injectable()
export class SessionMiddleware implements NestMiddleware {
  constructor(
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
  ) {}

  async use(req: Request, _res: Response, next: NextFunction): Promise<void> {
    const caminho = req.path;
    const mudaEstado = !['GET', 'HEAD', 'OPTIONS'].includes(req.method);

    // Rota pública do BFF (só o login). Ela muda estado e não tem sessão para
    // proteger, mas ainda assim exige o cabeçalho: login por CSRF existe, e o
    // custo de barrar é zero.
    if (PUBLICAS.has(caminho) || PUBLICAS_POR_PREFIXO.some((p) => caminho.startsWith(p))) {
      this.exigirCabecalhoAntiCsrf(req, mudaEstado);
      return next();
    }

    const token = this.sessions.extrairDoCabecalho(req.headers.cookie);
    const claims = this.sessions.verificar(token);
    if (!claims) {
      throw new UnauthorizedException({ error: 'Não autenticado.', code: 'NAO_AUTENTICADO' });
    }

    const user = await this.prisma.appUser.findUnique({ where: { id: claims.uid } });
    // Excluído, inativado ou com senha trocada depois da emissão: a sessão cai
    // na requisição seguinte, não no vencimento do cookie.
    if (!user || user.status !== 'ATIVO') {
      throw new UnauthorizedException({ error: 'Não autenticado.', code: 'NAO_AUTENTICADO' });
    }
    if (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat) {
      throw new UnauthorizedException({ error: 'Sessão expirada.', code: 'NAO_AUTENTICADO' });
    }

    if (user.mustChangePassword && !LIBERADAS_EM_TROCA_OBRIGATORIA.has(caminho)) {
      throw new ForbiddenException({
        error: 'Troque sua senha inicial antes de usar o sistema.',
        code: 'TROCA_DE_SENHA_OBRIGATORIA',
      });
    }

    // O segundo portão, e SÓ depois que o primeiro foi vencido. Painel sem
    // módulo escolhido não tem o que mostrar — a tela em branco do /inbox já
    // custou uma sessão de QA.
    if (!LIBERADAS_EM_ONBOARDING.has(caminho)) {
      const cfg = await this.prisma.mantenedoraSettings.findUnique({
        where: { mantenedoraId: user.mantenedoraId },
        select: { onboardingConcluido: true },
      });
      if (!cfg?.onboardingConcluido) {
        throw new ConflictException({
          error: 'A conta ainda está sendo configurada.',
          code: 'ONBOARDING_PENDENTE',
        });
      }
    }

    // CSRF depois da sessão, de propósito: sem cookie válido não há nada que um
    // site de terceiro possa cavalgar, e responder 403 antes do 401 só
    // confundiria quem depura. SameSite=Lax cobre o caso comum; o cabeçalho
    // cobre o que muda estado (ADR-0007 §1).
    this.exigirCabecalhoAntiCsrf(req, mudaEstado);

    req.usuario = {
      id: user.id,
      mantenedoraId: user.mantenedoraId,
      nome: user.name,
      email: user.email,
      precisaTrocarSenha: user.mustChangePassword,
    };
    next();
  }

  private exigirCabecalhoAntiCsrf(req: Request, mudaEstado: boolean): void {
    if (mudaEstado && !req.headers['x-requested-with']) {
      throw new ForbiddenException({ error: 'Requisição sem X-Requested-With.', code: 'CSRF_SUSPEITO' });
    }
  }
}

```

### api-app/src/infra/session/session.service.ts

SHA256 `884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { Injectable } from '@nestjs/common';
import { createHmac, timingSafeEqual } from 'node:crypto';

export const SESSION_COOKIE = 'lh_session';

export type SameSite = 'Lax' | 'Strict' | 'None';

/**
 * Lê `COOKIE_SAMESITE` sem exigir que ninguém acerte a caixa.
 *
 * O valor é o do atributo do cookie (`None`, com N maiúsculo), mas aceitar só a
 * forma exata seria uma armadilha: quem escrevesse `none` receberia `Lax` em
 * silêncio, e o sintoma seria exatamente o login mudo que a variável existe para
 * resolver. Vazio e desconhecido caem em `Lax` — nunca no mais permissivo.
 */
export function normalizarSameSite(valor: string | undefined): SameSite {
  switch (valor?.trim().toLowerCase()) {
    case 'none':
      return 'None';
    case 'strict':
      return 'Strict';
    default:
      return 'Lax';
  }
}

/** Um valor escrito e não reconhecido é engano de quem configurou, não default. */
export function valorDeSameSiteEhSuspeito(valor: string | undefined): boolean {
  const v = valor?.trim();
  if (!v) return false;
  return !['none', 'lax', 'strict'].includes(v.toLowerCase());
}

/** 1 dia — limita a janela de risco de um computador esquecido logado (ADR-0007). */
const DURACAO_MS = 24 * 60 * 60 * 1000;

export interface SessionClaims {
  /** id do app_user. O papel NÃO vem aqui: ele é lido do banco a cada request. */
  uid: string;
  iat: number;
  exp: number;
}

/**
 * Cookie de sessão assinado (ADR-0007 §1).
 *
 * O corpo carrega apenas `uid`, `iat` e `exp`. Papel, capacidade e escopo ficam
 * de fora de propósito: se viajassem no cookie, promoção e rebaixamento só
 * valeriam no próximo login.
 */
@Injectable()
export class SessionService {
  private readonly segredo = process.env.SESSION_SECRET ?? '';

  get configurado(): boolean {
    return this.segredo.length > 0;
  }

  assinar(uid: string, agora = Date.now()): string {
    const claims: SessionClaims = { uid, iat: agora, exp: agora + DURACAO_MS };
    const corpo = Buffer.from(JSON.stringify(claims)).toString('base64url');
    return `${corpo}.${this.hmac(corpo)}`;
  }

  verificar(token: string | undefined, agora = Date.now()): SessionClaims | null {
    if (!token || !token.includes('.')) return null;
    const [corpo, assinatura] = token.split('.');
    if (!corpo || !assinatura) return null;
    if (!this.assinaturaConfere(corpo, assinatura)) return null;

    try {
      const claims = JSON.parse(Buffer.from(corpo, 'base64url').toString()) as SessionClaims;
      if (!claims.uid || typeof claims.exp !== 'number') return null;
      if (agora > claims.exp) return null;
      return claims;
    } catch {
      return null;
    }
  }

  /**
   * `Secure` só fora de desenvolvimento: em http local o navegador descartaria
   * o cookie.
   *
   * `Domain` vem de COOKIE_DOMAIN e é o que faz o cookie emitido pela API valer
   * no subdomínio do front (ADR-0015). SameSite continua `Lax` porque
   * subdomínios do mesmo domínio são o **mesmo site** — sem essa variável, o
   * cookie fica preso ao host que o emitiu e o login "funciona e não entra".
   */
  cookie(token: string): string {
    const maxAge = Math.floor(DURACAO_MS / 1000);
    return `${SESSION_COOKIE}=${token}; HttpOnly;${this.atributos()} Max-Age=${maxAge}`;
  }

  cookieVazio(): string {
    return `${SESSION_COOKIE}=;${this.atributos()} HttpOnly; Max-Age=0`;
  }

  /**
   * `SameSite` é `Lax` por padrão, e é assim que produção tem de ficar.
   *
   * `COOKIE_SAMESITE=None` existe para UM caso: stage nos domínios gerados pela
   * Railway. `*.up.railway.app` é sufixo público, então dois serviços ali são
   * **sites diferentes** — o navegador recusa `Domain` compartilhado e o `Lax`
   * bloqueia o envio. O sintoma é mudo: o login responde 200, o Set-Cookie
   * chega, e a requisição seguinte vai sem cookie.
   *
   * O preço de `None`: a proteção de CSRF passa a depender **só** do cabeçalho
   * `X-Requested-With` exigido no que muda estado. Aceitável num ambiente de QA,
   * inaceitável em produção — ver ADR-0015, Emenda 1.
   */
  private atributos(): string {
    const sameSite = normalizarSameSite(process.env.COOKIE_SAMESITE);
    // `SameSite=None` sem `Secure` é recusado por todo navegador atual, então o
    // Secure deixa de depender do NODE_ENV quando ele está ligado.
    const secure = sameSite === 'None' || process.env.NODE_ENV === 'production' ? ' Secure;' : '';
    const dominio = process.env.COOKIE_DOMAIN ? ` Domain=${process.env.COOKIE_DOMAIN};` : '';
    return `${secure}${dominio} SameSite=${sameSite}; Path=/;`;
  }

  extrairDoCabecalho(cookieHeader: string | undefined): string | undefined {
    if (!cookieHeader) return undefined;
    for (const parte of cookieHeader.split(';')) {
      const [nome, ...resto] = parte.trim().split('=');
      if (nome === SESSION_COOKIE) return resto.join('=');
    }
    return undefined;
  }

  private hmac(corpo: string): string {
    return createHmac('sha256', this.segredo).update(corpo).digest('base64url');
  }

  private assinaturaConfere(corpo: string, assinatura: string): boolean {
    const esperada = Buffer.from(this.hmac(corpo));
    const recebida = Buffer.from(assinatura);
    if (esperada.length !== recebida.length) return false;
    return timingSafeEqual(esperada, recebida);
  }
}

```

### api-app/src/surfaces/webhooks/meta.controller.ts

SHA256 `261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { Controller, ForbiddenException, Get, HttpCode, Post, Query, Req, ServiceUnavailableException } from '@nestjs/common';
import type { RawBodyRequest } from '@nestjs/common';
import type { Request } from 'express';
import { createHmac, timingSafeEqual } from 'node:crypto';
import { IncomingService, MensagemRecebida } from '../../domain/inbox/incoming.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { qualifiedMetaInboundTimestamp } from '../../domain/inbox/channel-window-policy';

/**
 * Webhook do canal oficial. Autenticação POR ORIGEM (ADR-0006): a Meta assina o
 * corpo com o app secret, e é isso que provamos aqui.
 *
 * Fecha o risco S2: hoje, nos dois sistemas antigos, o POST do webhook não é
 * verificado — qualquer um que alcance a URL injeta mensagem.
 */
@Controller('webhooks/meta')
export class MetaWebhookController {
  constructor(
    private readonly incoming: IncomingService,
    private readonly prisma: PrismaService,
    private readonly acceptance: MessageAcceptanceService,
  ) {}

  /** Verificação do endpoint, feita pela Meta ao cadastrar a URL. */
  @Get()
  verificar(@Query() q: Record<string, string>): string {
    const esperado = process.env.WEBHOOK_VERIFY_TOKEN ?? '';
    if (esperado && q['hub.mode'] === 'subscribe' && q['hub.verify_token'] === esperado) {
      return q['hub.challenge'] ?? '';
    }
    throw new ForbiddenException();
  }

  @Post()
  @HttpCode(200)
  async receber(@Req() req: RawBodyRequest<Request>): Promise<string> {
    this.exigirAssinatura(req);

    const body = req.body as MetaWebhookBody;
    for (const entry of (body?.entry ?? []).slice(0, 100)) {
      for (const change of (entry.changes ?? []).slice(0, 100)) {
        if (change.field !== 'messages') continue;
        await this.tratarMensagens(change.value ?? {});
      }
    }

    // A Meta reentrega o que não recebeu 200. Erro de processamento nosso não
    // pode virar reentrega infinita — o evento cru já está gravado.
    return 'EVENT_RECEIVED';
  }

  /**
   * A assinatura é verificada sobre os BYTES BRUTOS. Sobre JSON reserializado
   * ela falharia (ou, pior, aceitaria payload alterado com a mesma semântica).
   */
  private exigirAssinatura(req: RawBodyRequest<Request>): void {
    const segredo = process.env.META_APP_SECRET ?? '';
    // Ausência de configuração é NEGAÇÃO, nunca liberação: sem segredo, não há
    // como provar origem, e aceitar seria reabrir o S2 por conveniência.
    if (!segredo) throw new ForbiddenException({ error: 'Webhook não configurado.', code: 'ORIGEM_NAO_VERIFICAVEL' });

    const cabecalho = req.headers['x-hub-signature-256'];
    const bruto = req.rawBody;
    if (typeof cabecalho !== 'string' || !bruto) {
      throw new ForbiddenException({ error: 'Assinatura ausente.', code: 'ASSINATURA_INVALIDA' });
    }

    const esperada = 'sha256=' + createHmac('sha256', segredo).update(bruto).digest('hex');
    const a = Buffer.from(esperada);
    const b = Buffer.from(cabecalho);
    if (a.length !== b.length || !timingSafeEqual(a, b)) {
      throw new ForbiddenException({ error: 'Assinatura inválida.', code: 'ASSINATURA_INVALIDA' });
    }
  }

  private async tratarMensagens(value: MetaMessagesValue): Promise<void> {
    const phoneNumberId = value.metadata?.phone_number_id;
    if (!phoneNumberId) return;
    const identity = await this.prisma.providerResourceIdentity.findUnique({
      where: { provider_externalResourceId: { provider: 'OFICIAL', externalResourceId: phoneNumberId } },
      include: { currentChannel: true },
    });
    const channel = identity?.currentChannel;
    if (!identity || !channel || channel.phoneNumberId !== phoneNumberId) return;
    const context = {
      providerResourceIdentityId: identity.id, buId: identity.buId, channelId: channel.id,
      generation: channel.generation, pairingEpoch: channel.pairingEpoch, channelOrigin: 'OFICIAL' as const,
    };
    if (!channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch) {
      await this.acceptance.persistCurrentResourceMetadata(context, 'meta.webhook', { phoneNumberId, field: 'messages', state: 'PENDING_IDENTITY' });
      throw new ServiceUnavailableException({ code: 'PENDING_IDENTITY' });
    }
    const redactedEvent = { phoneNumberId, value };
    await this.acceptance.persistVerifiedDiagnostic(context, 'meta.webhook', redactedEvent);

    const nome = value.contacts?.[0]?.profile?.name ?? null;

    for (const msg of (value.messages ?? []).slice(0, 100)) {
      if (typeof msg.id !== 'string' || !msg.id.trim()) continue;
      const rawContact = typeof msg.from === 'string' ? msg.from : '';
      // This slice supports WhatsApp phone contacts only. Opaque Meta IDs
      // (including BSUID-style identifiers) are rejected until their mapping
      // contract is implemented; never turn letters into another phone.
      if (!/^\+?[1-9]\d{7,14}$/.test(rawContact)) continue;
      const contact = rawContact.replace(/^\+/, '');
      await this.incoming.registrar({
        buId: identity.buId,
        canal: 'OFICIAL',
        contato: contact,
        ehGrupo: false,
        nomeExibicao: nome,
        direcao: 'IN',
        tipo: tipoDaMensagem(msg.type),
        conteudo: conteudoDaMensagem(msg),
        officialInboundAt: qualifiedMetaInboundTimestamp(msg.timestamp),
        externalId: msg.id,
        providerResourceIdentityId: identity.id,
        channelId: channel.id,
        generation: channel.generation,
        pairingEpoch: channel.pairingEpoch,
      });
    }
  }
}

export function tipoDaMensagem(tipo?: string): MensagemRecebida['tipo'] {
  switch (tipo) {
    case 'text':
    case 'button':
    case 'interactive':
      return 'TEXTO';
    case 'image':
      return 'IMAGEM';
    case 'audio':
      return 'AUDIO';
    case 'video':
      return 'VIDEO';
    case 'document':
      return 'DOCUMENTO';
    default:
      return 'OUTRO';
  }
}

/** A v1 registra o tipo e não baixa arquivo (ADR-0009 §6). */
export function conteudoDaMensagem(msg: MetaMessage): string {
  if (msg.type === 'text') return msg.text?.body ?? '';
  if (msg.type === 'button') return msg.button?.text ?? '';
  if (msg.type === 'interactive') {
    return msg.interactive?.button_reply?.title ?? msg.interactive?.list_reply?.title ?? '[interativo]';
  }
  return `[${msg.type ?? 'mensagem'}]`;
}

interface MetaWebhookBody {
  entry?: { changes?: { field?: string; value?: MetaMessagesValue }[] }[];
}
interface MetaMessagesValue {
  metadata?: { phone_number_id?: string };
  contacts?: { profile?: { name?: string } }[];
  messages?: MetaMessage[];
}
export interface MetaMessage {
  id?: string;
  from?: string;
  timestamp?: string | number;
  type?: string;
  text?: { body?: string };
  button?: { text?: string };
  interactive?: { button_reply?: { title?: string }; list_reply?: { title?: string } };
}

```

### api-app/src/surfaces/public/conversations.controller.ts

SHA256 `bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1`. unchanged inherited pre-ST04 bytes.

```typescript
import {
  BadRequestException,
  Body,
  Controller,
  ForbiddenException,
  Get,
  HttpCode,
  HttpException,
  Param,
  Post,
  Query,
  Req,
  Res,
} from '@nestjs/common';
import type { Request, Response } from 'express';
import { Prisma } from '@prisma/client';
import { ApiKeyService } from '../../domain/integration/api-key.service';
import { RateLimitService } from '../../domain/integration/rate-limit.service';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { PrismaService } from '../../infra/prisma/prisma.service';

const TETO = 500;

function limitePublico(valor: unknown, padrao: number): number {
  if (typeof valor !== 'string' || valor.trim() === '') return padrao;
  const numero = Number(valor);
  if (!Number.isFinite(numero) || numero <= 0) return padrao;
  const inteiro = Math.floor(numero);
  if (inteiro < 1) return padrao;
  return Math.min(inteiro, TETO);
}

/**
 * Superfície pública v1 (ADR-0010) — o contrato do parceiro.
 *
 * `account_id` continua se chamando assim e passa a valer o **UUID da BU**: o
 * parceiro já integrou esse nome com esse significado nos dois sistemas antigos,
 * e trocá-lo daria trabalho a ele sem entregar clareza.
 */
@Controller('api/v1')
export class PublicConversationsController {
  constructor(
    private readonly chaves: ApiKeyService,
    private readonly conversas: ConversationsService,
    private readonly limite: RateLimitService,
    private readonly prisma: PrismaService,
  ) {}

  @Get('accounts')
  async accounts(@Req() req: Request) {
    const ids = await this.chaves.busDaChave(req.chave!);
    const bus = await this.prisma.businessUnit.findMany({
      where: { id: { in: ids } },
      select: { id: true, name: true, phone: true, channels: { select: { type: true, status: true } } },
      orderBy: { name: 'asc' },
    });

    return {
      accounts: bus.map((b) => ({
        id: b.id,
        name: b.name,
        numero: b.phone,
        canais: b.channels.map((c) => ({ tipo: c.type, conectado: c.status === 'CONECTADO' })),
      })),
    };
  }

  @Get('conversations')
  async conversations(@Query() q: Record<string, string>, @Req() req: Request) {
    const buId = await this.resolverConta(req, q.account_id);
    const periodo = periodoDe(q.de, q.ate);
    const limite = limitePublico(q.limit, 200);

    const where: Record<string, unknown> = { buId, contactType: 'PESSOA' };
    if (periodo) where.lastMessageAt = { gte: periodo.de, lte: periodo.ate };
    if (q.q?.trim()) {
      where.OR = [
        { displayName: { contains: q.q.trim(), mode: 'insensitive' } },
        { contact: { contains: q.q.trim() } },
      ];
    }

    const linhas = await this.prisma.conversation.findMany({
      where,
      orderBy: { lastMessageAt: 'desc' },
      take: limite + 1,
      select: { id: true, contact: true, displayName: true, status: true, attendantName: true, lastMessageAt: true, unreadCount: true },
    });

    const pagina = linhas.slice(0, limite);
    type LatestMessage = {
      conversationId: string;
      content: string | null;
      direction: 'IN' | 'OUT' | null;
      channelOrigin: 'OFICIAL' | 'NAO_OFICIAL' | null;
    };
    const mensagensRecentes = pagina.length
      ? await this.prisma.$queryRaw<LatestMessage[]>`
        SELECT requested.conversation_id AS "conversationId",
          latest.content,
          latest.direction::text AS "direction",
          latest.channel_origin::text AS "channelOrigin"
        FROM unnest(ARRAY[${Prisma.join(pagina.map((conversation) => conversation.id))}]::text[]) AS requested(conversation_id)
        LEFT JOIN LATERAL (
          SELECT candidate.content, candidate.direction, candidate.channel_origin
          FROM (
            (
              SELECT message.id, message.content, message.direction, message.channel_origin, message.created_at
              FROM messages AS message
              WHERE message.conversation_id = requested.conversation_id AND message.direction = 'IN'
              ORDER BY message.created_at DESC, message.id DESC
              LIMIT 1
            )
            UNION ALL
            (
              SELECT message.id, message.content, message.direction, message.channel_origin, message.created_at
              FROM messages AS message
              WHERE message.conversation_id = requested.conversation_id AND message.direction = 'OUT'
              ORDER BY message.created_at DESC, message.id DESC
              LIMIT 1
            )
          ) AS candidate
          ORDER BY candidate.created_at DESC, candidate.id DESC
          LIMIT 1
        ) AS latest ON TRUE
      `
      : [];
    const mensagemPorConversa = new Map(mensagensRecentes.map((message) => [message.conversationId, message]));
    const estados = await this.conversas.estadosDasJanelas(pagina.map((c) => ({
      conversationId: c.id, buId, latestMessageOrigin: mensagemPorConversa.get(c.id)?.channelOrigin ?? null,
    })));
    const conversas = pagina.map((c) => {
        const janela = estados.get(c.id);
        const mensagem = mensagemPorConversa.get(c.id);
        return {
          telefone: c.contact,
          nome_whatsapp: c.displayName,
          status: c.status,
          atendendo: c.attendantName,
          ultima_mensagem: mensagem?.content ?? null,
          ultima_direcao: mensagem?.direction ? (mensagem.direction === 'OUT' ? 'enviada' : 'recebida') : null,
          ultima_em: c.lastMessageAt?.toISOString() ?? null,
          nao_lidas: c.unreadCount,
          // Campo generalizado: quem integrou só o Hub recebe `true` e não muda
          // nada; quem integrou a Central continua lendo o que já lia.
          janela_aberta: janela?.windowOpen ?? false,
          janela_expira_em: janela?.expiresAt?.toISOString() ?? null,
          envio_disponivel: janela?.available ?? false,
          motivo_indisponibilidade: janela ? janela.reason : 'CANAL_SELECIONADO_INDISPONIVEL',
        };
      });

    return { conta: { id: buId }, conversations: conversas, truncado: linhas.length > limite };
  }

  @Get('conversations/:telefone/messages')
  async messages(
    @Param('telefone') telefone: string,
    @Query() q: Record<string, string>,
    @Req() req: Request,
  ) {
    const buId = await this.resolverConta(req, q.account_id);
    const conversa = await this.conversaDoTelefone(buId, telefone);
    const limite = limitePublico(q.limit, 100);

    const mensagens = await this.prisma.message.findMany({
      where: {
        conversationId: conversa.id,
        // `since` permite sync incremental: o parceiro guarda a data da última
        // mensagem copiada e pede só o que veio depois.
        ...(q.since ? { createdAt: { gt: new Date(q.since) } } : {}),
      },
      orderBy: { createdAt: 'asc' },
      take: limite,
    });

    const janela = await this.conversas.estadoDaJanela(conversa.id, buId);
    return {
      telefone: conversa.contact,
      janela_aberta: janela.aberta,
      envio_disponivel: janela.disponivel,
      motivo_indisponibilidade: janela.motivoIndisponibilidade,
      messages: mensagens.map((m) => ({
        id: m.id,
        direcao: m.direction === 'OUT' ? 'enviada' : 'recebida',
        tipo: m.messageType,
        texto: m.content,
        canal: m.channelOrigin,
        respondido_por: m.authorName,
        // Data SEMPRE em ISO-8601 UTC: API externa não pode entregar formato variável.
        em: m.createdAt.toISOString(),
      })),
    };
  }

  @Post('messages')
  @HttpCode(201)
  async enviar(@Body() body: Record<string, string>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    const buId = await this.resolverConta(req, body?.account_id);
    const telefone = String(body?.telefone ?? '').replace(/\D/g, '');
    const texto = String(body?.texto ?? '').trim();
    if (!telefone) throw new BadRequestException({ error: 'Informe o telefone.', code: 'TELEFONE_INVALIDO' });
    if (!texto) throw new BadRequestException({ error: 'Informe o texto.', code: 'TEXTO_VAZIO' });
    if (texto.length > 4096) throw new BadRequestException({ error: 'Texto muito longo.', code: 'TEXTO_LONGO' });

    const espera = this.limite.consumir(req.chave!.id, buId);
    if (espera > 0) {
      res.setHeader('Retry-After', String(espera));
      throw new HttpException({ error: 'Ritmo acima do permitido.', code: 'LIMITE_DE_TAXA' }, 429);
    }

    const conversa = await this.conversaOuNova(buId, telefone);
    const atendente = String(body?.atendente ?? '').trim() || req.chave!.nome;
    const m = await this.conversas.responder(conversa.id, buId, texto, { kind: 'PUBLIC', name: atendente });

    return { ok: true, message_id: m.id, canal: m.channelOrigin };
  }

  @Post('conversations/:telefone/claim')
  async claim(@Param('telefone') telefone: string, @Body() body: Record<string, string>, @Req() req: Request) {
    const buId = await this.resolverConta(req, body?.account_id);
    const conversa = await this.conversaDoTelefone(buId, telefone);
    const atendente = String(body?.atendente ?? '').trim() || req.chave!.nome;

    if (conversa.status === 'IN_SERVICE' && conversa.attendantName && conversa.attendantName !== atendente) {
      throw new HttpException(
        { error: `Já está sendo atendida por ${conversa.attendantName}.`, code: 'JA_ATENDIDA' },
        409,
      );
    }
    await this.prisma.conversation.update({
      where: { id: conversa.id },
      data: { status: 'IN_SERVICE', attendantName: atendente, attendantOrigin: 'EXTERNO', attendantUserId: null },
    });
    return { ok: true };
  }

  @Post('conversations/:telefone/release')
  async release(@Param('telefone') telefone: string, @Body() body: Record<string, string>, @Req() req: Request) {
    const buId = await this.resolverConta(req, body?.account_id);
    const conversa = await this.conversaDoTelefone(buId, telefone);
    await this.prisma.conversation.update({
      where: { id: conversa.id },
      data: { status: 'QUEUED', attendantName: null, attendantOrigin: null, attendantUserId: null },
    });
    return { ok: true };
  }

  /** A conta pedida precisa estar no escopo DA CHAVE — e o escopo nulo nunca sai da Mantenedora. */
  private async resolverConta(req: Request, accountId?: string): Promise<string> {
    if (!accountId) {
      throw new BadRequestException({ error: 'Informe o account_id.', code: 'CONTA_NAO_INFORMADA' });
    }
    const permitidas = await this.chaves.busDaChave(req.chave!);
    if (!permitidas.includes(accountId)) {
      throw new ForbiddenException({
        error: 'Esta chave não tem acesso a essa conta.',
        code: 'SEM_ACESSO_A_CONTA',
      });
    }
    return accountId;
  }

  private async conversaDoTelefone(buId: string, telefone: string) {
    const conversa = await this.prisma.conversation.findUnique({
      where: { buId_contact: { buId, contact: telefone.replace(/\D/g, '') } },
    });
    if (!conversa) {
      throw new BadRequestException({ error: 'Conversa não encontrada.', code: 'CONVERSA_NAO_ENCONTRADA' });
    }
    return conversa;
  }

  private async conversaOuNova(buId: string, telefone: string) {
    return this.prisma.conversation.upsert({
      where: { buId_contact: { buId, contact: telefone } },
      create: { buId, contact: telefone, contactType: 'PESSOA', status: 'IN_SERVICE' },
      update: {},
    });
  }
}

function periodoDe(de?: string, ate?: string): { de: Date; ate: Date } | null {
  if (!de || !ate) return null;
  if (!/^\d{4}-\d{2}-\d{2}$/.test(de) || !/^\d{4}-\d{2}-\d{2}$/.test(ate)) {
    throw new BadRequestException({ error: 'Use de e ate no formato AAAA-MM-DD.', code: 'PERIODO_INVALIDO' });
  }
  return { de: new Date(`${de}T00:00:00.000Z`), ate: new Date(`${ate}T23:59:59.999Z`) };
}

```

### api-app/prisma/schema.prisma

SHA256 `d2c94a0b0908d268f498ed0e288924343abeb1bb206d71f8291063caec50fbed`. changed since exact pre-ST04 seal within admitted mutation scope.

```prisma
// Schema do núcleo unificado (v1). Nomenclatura conforme ADR-0011:
// estrutura em inglês, Mantenedora e BusinessUnit como nomes próprios do
// domínio, snake_case no banco via @map.
//
// Regra 0 do CLAUDE.md: toda tabela de dado de negócio tem bu_id, e toda
// leitura filtra pelo escopo do usuário. Quem tem mantenedora_id NÃO é dado de
// negócio (app_users, api_keys, mantenedora_settings) e não entra nesse filtro.

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

/* ------------------------------- tenancy -------------------------------- */

enum TenantStatus {
  ATIVO
  INATIVO
}

/// A conta do cliente. Agrupa, endereça e é dona das integrações — não possui
/// conversa e não recebe grant (ADR-0008).
model Mantenedora {
  id        String       @id @default(uuid())
  name      String
  status    TenantStatus @default(ATIVO)
  createdAt DateTime     @default(now()) @map("created_at")
  updatedAt DateTime     @updatedAt @map("updated_at")

  businessUnits BusinessUnit[]
  setores       Setor[]
  arquivos      Arquivo[]
  appUsers      AppUser[]
  apiKeys       ApiKey[]
  settings      MantenedoraSettings?
  typebotBots   TypebotBot[]
  channelRegistrationAttempts ChannelRegistrationAttempt[]
  messageTemplateDrafts MessageTemplateDraft[]
  messageTemplateOperations MessageTemplateOperation[]

  @@map("mantenedoras")
}

/// A Business Unit É O NÚMERO (ADR-0008). É onde a permissão existe de fato e
/// onde conversa e mensagem penduram.
/// Setor — o agrupamento entre a Mantenedora e o número (ADR-0017).
///
/// Ele NÃO é o escopo de permissão: o grant continua materializado na BU, e
/// conceder um setor é EXPANSÃO. É isso que faz nenhuma leitura mudar.
model Setor {
  id            String       @id @default(uuid())
  mantenedoraId String       @map("mantenedora_id")
  mantenedora   Mantenedora  @relation(fields: [mantenedoraId], references: [id], onDelete: Cascade)
  name          String
  /// INATIVO some do seletor de cadastro e marca o setor como fora de uso. NÃO
  /// interrompe atendimento: sumir com a inbox de um número por engano de
  /// cadastro seria perder conversa (ADR-0017 §1).
  status        TenantStatus @default(ATIVO)
  createdAt     DateTime     @default(now()) @map("created_at")

  businessUnits BusinessUnit[]
  grants        SetorGrant[]

  @@unique([mantenedoraId, name])
  @@map("setores")
}

/// A CONCESSÃO de um setor a alguém — o fato, separado da consequência.
///
/// As linhas em `user_bu_roles` são a MATERIALIZAÇÃO dela, uma por número. Sem
/// esta tabela, conceder um setor VAZIO não guardaria nada: a concessão só
/// existiria derivada das linhas materializadas, e um setor sem número não teria
/// nenhuma para derivar. O número adicionado depois não encontraria a concessão,
/// e ninguém perceberia — porque o sintoma é um acesso que nunca aparece.
model SetorGrant {
  id        String   @id @default(uuid())
  setorId   String   @map("setor_id")
  setor     Setor    @relation(fields: [setorId], references: [id], onDelete: Cascade)
  userId    String   @map("user_id")
  user      AppUser  @relation(fields: [userId], references: [id], onDelete: Cascade)
  role      Role
  createdAt DateTime @default(now()) @map("created_at")

  @@unique([setorId, userId])
  @@index([userId])
  @@map("setor_grants")
}

model BusinessUnit {
  id            String       @id @default(uuid())
  mantenedoraId String       @map("mantenedora_id")
  mantenedora   Mantenedora  @relation(fields: [mantenedoraId], references: [id], onDelete: Restrict)
  /// OBRIGATÓRIO (ADR-0017 §1): número sem setor é número que nenhum atendente
  /// enxerga. Toda Mantenedora nasce com o setor `Geral`, e é nele que cai quem
  /// não escolher.
  setorId       String       @map("setor_id")
  setor         Setor        @relation(fields: [setorId], references: [id], onDelete: Restrict)
  name          String
  /// Telefone em E.164, só dígitos. Nulo enquanto o canal não informar.
  phone         String?
  status        TenantStatus @default(ATIVO)
  /// Rastreio da origem na migração (ADR-0003). Sai quando ninguém mais cruzar
  /// com o sistema antigo.
  legacyRef     String?      @map("legacy_ref")
  createdAt     DateTime     @default(now()) @map("created_at")
  updatedAt     DateTime     @updatedAt @map("updated_at")

  channels      BuChannel[]
  roles         UserBuRole[]
  conversations Conversation[]
  channelRegistrationAttempts ChannelRegistrationAttempt[]
  providerResourceIdentities ProviderResourceIdentity[]
  messageTemplateDrafts MessageTemplateDraft[]
  messageTemplateOperations MessageTemplateOperation[]
  messageTemplateObservationLeases MessageTemplateObservationLease[]

  @@unique([id, mantenedoraId])
  @@index([mantenedoraId, status])
  @@index([setorId])
  @@map("business_units")
}

enum ChannelType {
  OFICIAL
  NAO_OFICIAL
}

enum ChannelStatus {
  CONECTANDO
  CONECTADO
  DESCONECTADO
  DESLOGADO
}

/// O vínculo da BU com a tecnologia. No máximo um de cada tipo por BU.
model BuChannel {
  id     String       @id @default(uuid())
  buId   String       @map("bu_id")
  bu     BusinessUnit @relation(fields: [buId], references: [id], onDelete: Cascade)
  type   ChannelType
  status ChannelStatus @default(CONECTANDO)
  generation Int @default(1)
  currentAttemptId String? @unique @map("current_attempt_id")
  currentAttempt ChannelRegistrationAttempt? @relation("CurrentChannelAttempt", fields: [currentAttemptId], references: [id], onDelete: SetNull)
  pairingEpoch Int @default(0) @map("pairing_epoch")
  ownNumberVerified Boolean @default(false) @map("own_number_verified")
  verifiedEpoch Int? @map("verified_epoch")
  providerConnectionState String @default("PENDING") @map("provider_connection_state")
  receiptVerifiedAt DateTime? @map("receipt_verified_at")
  operationLeaseToken String? @map("operation_lease_token")
  operationLeaseUntil DateTime? @map("operation_lease_until")
  pendingCleanupInstanceName String? @map("pending_cleanup_instance_name")
  pendingCleanupIdentityId String? @map("pending_cleanup_identity_id")

  /// Canal OFICIAL (Meta Cloud API)
  wabaId        String? @map("waba_id")
  phoneNumberId String? @map("phone_number_id")

  /// Canal NAO_OFICIAL (Evolution API)
  evolutionInstanceName String? @unique @map("evolution_instance_name")

  /// A janela de 24h da Meta é atributo do CANAL, não do produto (ADR-0009).
  requiresWindow Boolean   @default(false) @map("requires_window")
  connectedAt    DateTime? @map("connected_at")
  createdAt      DateTime  @default(now()) @map("created_at")
  updatedAt      DateTime  @updatedAt @map("updated_at")

  credential ChannelCredential?
  attempts ChannelRegistrationAttempt[]
  providerIdentities ProviderResourceIdentity[]
  @@unique([buId, type])
  @@map("bu_channels")
}

enum ChannelRegistrationState {
  PENDING_AUTH
  PENDING_NUMBER
  REGISTERING
  PENDING_RECEIPT
  CONNECTED
  ERROR
  CANCELLED
}

enum ChannelRegistrationOperation {
  NOVO
  REAUTORIZAR
}

/// Registration workflow state is deliberately separate from ChannelStatus,
/// which preserves the existing transport-facing status contract.
model ChannelRegistrationAttempt {
  id String @id @default(uuid())
  mantenedoraId String @map("mantenedora_id")
  mantenedora Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Restrict)
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId], references: [id], onDelete: Restrict)
  channelId String? @map("channel_id")
  channel BuChannel? @relation(fields: [channelId], references: [id], onDelete: Restrict)
  currentForChannel BuChannel? @relation("CurrentChannelAttempt")
  type ChannelType
  operation ChannelRegistrationOperation @default(NOVO)
  userId String @map("user_id")
  sessionHash String @map("session_hash")
  nonceHash String? @map("nonce_hash")
  idempotencyKey String @map("idempotency_key")
  requestHash String @map("request_hash")
  state ChannelRegistrationState @default(PENDING_AUTH)
  version Int @default(1)
  generation Int @default(1)
  pairingEpoch Int? @map("pairing_epoch")
  leaseUntil DateTime? @map("lease_until")
  expiresAt DateTime @map("expires_at")
  stage String @default("RESERVED")
  safeErrorCode String? @map("safe_error_code")
  candidateKeyId String? @map("candidate_key_id")
  candidateNonce Bytes? @map("candidate_nonce")
  candidateCiphertext Bytes? @map("candidate_ciphertext")
  candidateTag Bytes? @map("candidate_tag")
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")

  @@unique([mantenedoraId, idempotencyKey])
  @@index([buId, type, state])
  @@index([state, expiresAt])
  @@map("channel_registration_attempts")
}

/// Active encrypted credential. Ciphertext is only ever passed to adapters
/// through the channel credential resolver; never project this model publicly.
model ChannelCredential {
  id String @id @default(uuid())
  channelId String @unique @map("channel_id")
  channel BuChannel @relation(fields: [channelId], references: [id], onDelete: Restrict)
  provider ChannelType
  buId String @map("bu_id")
  generation Int
  version Int @default(1)
  keyId String @map("key_id")
  nonce Bytes
  ciphertext Bytes
  tag Bytes
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")

  @@index([buId, provider])
  @@map("channel_credentials")
}

/// Durable ownership tombstone: deleting a channel detaches currentChannelId,
/// while buId remains RESTRICT-owned and cannot be transferred. A PostgreSQL
/// trigger also makes (provider, externalResourceId, buId) immutable after create.
model ProviderResourceIdentity {
  id String @id @default(uuid())
  provider ChannelType
  externalResourceId String @map("external_resource_id")
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId], references: [id], onDelete: Restrict)
  currentChannelId String? @map("current_channel_id")
  currentChannel BuChannel? @relation(fields: [currentChannelId], references: [id], onDelete: SetNull)
  createdAt DateTime @default(now()) @map("created_at")
  retiredAt DateTime? @map("retired_at")
  managedLifecycle Boolean @default(false) @map("managed_lifecycle")
  cleanupState String @default("UNMANAGED") @map("cleanup_state")
  cleanupLeaseToken String? @map("cleanup_lease_token")
  cleanupLeaseUntil DateTime? @map("cleanup_lease_until")
  messages Message[]
  messageTemplateDrafts MessageTemplateDraft[]

  @@unique([id, buId])
  @@unique([provider, externalResourceId])
  @@index([buId])
  @@index([currentChannelId])
  @@map("provider_resource_identities")
}

/* ------------------------------ identidade ------------------------------ */

/// De onde veio o grant (ADR-0017 §2). DIRETO é concessão nominal; os outros
/// dois são expansão, e carregam o id da origem em `granted_via_id`.
enum OrigemDoGrant {
  DIRETO
  SETOR
  MANTENEDORA
}

/// Três papéis (ADR-0018). VIEWER saiu, e o eixo de capacidades também:
/// disponibilidade passou a ser MÓDULO (ADR-0016), não permissão de usuário.
enum Role {
  OWNER
  ADMIN
  ATENDENTE
}

/// Pessoa que usa o produto. Sempre de UMA Mantenedora; e-mail único dentro
/// dela, não globalmente (ADR-0008 §3).
model AppUser {
  id            String       @id @default(uuid())
  mantenedoraId String       @map("mantenedora_id")
  mantenedora   Mantenedora  @relation(fields: [mantenedoraId], references: [id], onDelete: Restrict)
  name          String
  email         String
  /// bcrypt (ADR-0007). Hash PBKDF2 importado é reconhecido pelo prefixo e
  /// reidratado no primeiro login.
  /// NULO enquanto o convite não foi usado (ADR-0025 §2): pessoa sem credencial
  /// existe no cadastro e não entra.
  passwordHash  String?      @map("password_hash")
  /// Só para o hash PBKDF2 legado, que guardava o salt em coluna separada.
  /// Limpo na reidratação.
  legacySalt    String?      @map("legacy_salt")
  /// Contato da pessoa, editável por ela mesma no perfil. Não é credencial e
  /// não participa de login — o e-mail é que identifica (ADR-0007).
  phone         String?
  /// Id do arquivo no armazenamento (ADR-0024), nunca um caminho.
  avatar        String?
  status        TenantStatus @default(ATIVO)
  mustChangePassword Boolean  @default(false) @map("must_change_password")
  passwordChangedAt  DateTime? @map("password_changed_at")
  createdAt          DateTime  @default(now()) @map("created_at")
  updatedAt          DateTime  @updatedAt @map("updated_at")

  roles       UserBuRole[]
  createdMessageTemplateDrafts MessageTemplateDraft[]
  messageTemplateOperations MessageTemplateOperation[]
  setorGrants SetorGrant[]
  tokens      TokenDeAcesso[]

  @@unique([id, mantenedoraId])
  @@unique([mantenedoraId, email])
  @@map("app_users")
}

/// A única fonte de permissão. bu_id é SEMPRE uma BU — não existe grant em
/// Mantenedora; o papel nela é calculado (ADR-0008 §4).
model UserBuRole {
  id     String       @id @default(uuid())
  userId String       @map("user_id")
  user   AppUser      @relation(fields: [userId], references: [id], onDelete: Cascade)
  buId   String       @map("bu_id")
  bu     BusinessUnit @relation(fields: [buId], references: [id], onDelete: Cascade)
  role   Role
  /// Proveniência, em PAR (ADR-0017 §2). Era um campo só, que só distinguia
  /// direto de expansão da Mantenedora; com o Setor há três origens, e o tipo
  /// precisa ser explícito. Grant DIRETO vence expansão, e revogar uma origem
  /// remove só o que ela criou.
  grantedViaTipo OrigemDoGrant @default(DIRETO) @map("granted_via_tipo")
  grantedViaId   String?       @map("granted_via_id")
  createdAt      DateTime      @default(now()) @map("created_at")

  @@unique([userId, buId])
  @@index([buId])
  @@map("user_bu_roles")
}

/// Tentativas de senha erradas, por e-mail (ADR-0007 §4).
model LoginAttempt {
  email        String    @id
  fails        Int       @default(0)
  lastFailAt   DateTime? @map("last_fail_at")
  blockedUntil DateTime? @map("blocked_until")

  @@map("login_attempts")
}

/* ----------------------------- atendimento ------------------------------ */

enum ConversationStatus {
  QUEUED
  IN_SERVICE
  CLOSED
}

enum ContactType {
  PESSOA
  GRUPO
}

enum AttendantOrigin {
  INTERNO
  EXTERNO
}

/// Conversa é entidade e pendura na BU (ADR-0009). Chave natural (bu_id,
/// contact); o JID fica no adaptador, nunca no domínio.
model Conversation {
  id      String       @id @default(uuid())
  buId    String       @map("bu_id")
  bu      BusinessUnit @relation(fields: [buId], references: [id], onDelete: Cascade)
  /// Telefone E.164 só dígitos, ou o identificador do grupo.
  contact     String
  contactType ContactType        @default(PESSOA) @map("contact_type")
  displayName String?            @map("display_name")
  status      ConversationStatus @default(QUEUED)

  /// Atribuição: um conceito com proveniência (ADR-0009 §2). FK opcional com
  /// SetNull + snapshot de nome (ADR-0007).
  attendantUserId String?          @map("attendant_user_id")
  attendantName   String?          @map("attendant_name")
  attendantOrigin AttendantOrigin? @map("attendant_origin")

  unreadCount   Int       @default(0) @map("unread_count")
  lastMessageAt DateTime? @map("last_message_at")
  createdAt     DateTime  @default(now()) @map("created_at")
  updatedAt     DateTime  @updatedAt @map("updated_at")

  messages Message[]
  dispatchAdmissions DispatchAdmission[]
  initialMessageIntents InitialMessageIntent[]

  @@unique([buId, contact])
  @@index([buId, status, lastMessageAt])
  @@map("conversations")
}

enum DispatchAdmissionCaller {
  BFF
  PUBLIC
  BOT
}

enum DispatchAdmissionState {
  PREPARED
  SENDING
  SETTLED
  UNCERTAIN
}

enum InitialMessageIntentState {
  PREPARED
  SENDING
  EXTERNAL_ACCEPTED
  EXTERNAL_ACCEPTED_LOCAL_BLOCKED
  SUCCEEDED
  REJECTED
  AMBIGUOUS
}

/// Finite exclusion token for one ordinary outbound attempt; it is not a Message or retry owner.
model DispatchAdmission {
  id              String                  @id @default(uuid())
  conversationId  String                  @map("conversation_id")
  conversation    Conversation            @relation(fields: [conversationId], references: [id], onDelete: Cascade)
  buId            String                  @map("bu_id")
  caller           DispatchAdmissionCaller
  actorId          String                  @map("actor_id")
  ownerNonce       String                  @map("owner_nonce")
  selectedContext  Json                    @map("selected_context")
  state            DispatchAdmissionState  @default(PREPARED)
  expiresAt        DateTime                @map("expires_at") @db.Timestamp(3)
  dispatchDeadlineAt DateTime?             @map("dispatch_deadline_at") @db.Timestamp(3)
  releasedAt       DateTime?               @map("released_at") @db.Timestamp(3)
  riskAcknowledgedAt DateTime?             @map("risk_acknowledged_at") @db.Timestamp(3)
  riskAcknowledgedByActorId String?        @map("risk_acknowledged_by_actor_id")
  createdAt        DateTime                @default(now()) @map("created_at") @db.Timestamp(3)
  updatedAt        DateTime                @updatedAt @map("updated_at") @db.Timestamp(3)

  @@unique([ownerNonce])
  @@index([conversationId, releasedAt, state, expiresAt], map: "dispatch_admissions_active_conversation_idx")
  @@map("dispatch_admissions")
}

/// Durable first-send request and exclusive conversation slot; Message remains owned by MessageAcceptanceService.
model InitialMessageIntent {
  id                    String                     @id @default(uuid())
  conversationId        String                     @map("conversation_id")
  conversation          Conversation               @relation(fields: [conversationId], references: [id], onDelete: Cascade)
  buId                  String                     @map("bu_id")
  actorId               String                     @map("actor_id")
  idempotencyKey        String                     @map("idempotency_key")
  ownerNonce            String                     @map("owner_nonce")
  requestFingerprint    String                     @map("request_fingerprint")
  request               Json
  selectedContext       Json                       @map("selected_context")
  state                 InitialMessageIntentState @default(PREPARED)
  leaseExpiresAt        DateTime                   @map("lease_expires_at") @db.Timestamp(3)
  dispatchDeadlineAt    DateTime?                  @map("dispatch_deadline_at") @db.Timestamp(3)
  externalMessageId     String?                    @map("external_message_id")
  slotReleasedAt        DateTime?                  @map("slot_released_at") @db.Timestamp(3)
  riskAcknowledgedAt    DateTime?                  @map("risk_acknowledged_at") @db.Timestamp(3)
  riskAcknowledgedByActorId String?                @map("risk_acknowledged_by_actor_id")
  createdAt             DateTime                   @default(now()) @map("created_at") @db.Timestamp(3)
  updatedAt             DateTime                   @updatedAt @map("updated_at") @db.Timestamp(3)

  @@unique([buId, actorId, idempotencyKey], map: "initial_message_intents_idempotency_key")
  @@unique([ownerNonce])
  @@index([conversationId, slotReleasedAt, state, createdAt], map: "initial_message_intents_slot_idx")
  @@index([actorId, createdAt(sort: Desc)], map: "initial_message_intents_actor_rate_idx")
  @@map("initial_message_intents")
}

enum MessageDirection {
  IN
  OUT
}

enum MessageType {
  TEXTO
  IMAGEM
  AUDIO
  VIDEO
  DOCUMENTO
  OUTRO
}

enum MessageStatus {
  RECEBIDA
  ENVIADA
  ENTREGUE
  LIDA
  FALHOU
}

model Message {
  id             String       @id @default(uuid())
  conversationId String       @map("conversation_id")
  conversation   Conversation @relation(fields: [conversationId], references: [id], onDelete: Cascade)
  /// Denormalizado do conversation para que TODA tabela de dado de negócio
  /// tenha bu_id (regra 0).
  buId          String           @map("bu_id")
  direction     MessageDirection
  messageType   MessageType      @default(TEXTO) @map("message_type")
  content       String?
  mediaRef      String?          @map("media_ref")
  /// Por qual canal entrou ou saiu (ADR-0009 §1).
  channelOrigin ChannelType      @map("channel_origin")
  status        MessageStatus
  externalId    String?          @map("external_id")
  providerResourceIdentityId String? @map("provider_resource_identity_id")
  providerResourceIdentity ProviderResourceIdentity? @relation(fields: [providerResourceIdentityId], references: [id], onDelete: Restrict)
  /// Autoria: FK opcional SetNull + snapshot (ADR-0007). O payload cru NÃO
  /// mora aqui — só no log de webhook, com expurgo (ADR-0009 §7).
  authorUserId String?  @map("author_user_id")
  authorName   String?  @map("author_name")
  /// Only a signed, verified Meta IN timestamp; never a timeline timestamp.
  officialInboundAt DateTime? @map("official_inbound_at")
  createdAt    DateTime @default(now()) @map("created_at")

  @@index([conversationId, createdAt])
  @@index([conversationId, direction, createdAt, id], map: "messages_conversation_direction_created_id_idx")
  @@index([conversationId, providerResourceIdentityId, direction, channelOrigin, officialInboundAt, id], map: "messages_conversation_trusted_window_idx")
  @@index([buId, createdAt])
  @@unique([providerResourceIdentityId, externalId])
  @@map("messages")
}

/* ------------------------------ integração ------------------------------ */

/// Chave da API pública. Pertence a uma Mantenedora; escopo nulo = todas as
/// BUs DELA, nunca do sistema (ADR-0008 §6, ADR-0010).
model ApiKey {
  id            String      @id @default(uuid())
  mantenedoraId String      @map("mantenedora_id")
  mantenedora   Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Cascade)
  name          String
  /// Só o SHA-256. A chave em claro aparece uma vez, na criação.
  keyHash    String    @unique @map("key_hash")
  keyPrefix  String    @map("key_prefix")
  scopeBuIds String[]  @map("scope_bu_ids")
  lastUsedAt DateTime? @map("last_used_at")
  revokedAt  DateTime? @map("revoked_at")
  createdByName String? @map("created_by_name")
  createdAt  DateTime  @default(now()) @map("created_at")

  @@index([mantenedoraId])
  @@map("api_keys")
}

/// Webhook de saída, agora POR MANTENEDORA — deixou de ser singleton
/// (ADR-0008 §6).
model MantenedoraSettings {
  mantenedoraId         String      @id @map("mantenedora_id")
  mantenedora           Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Cascade)
  outboundWebhookUrl    String?     @map("outbound_webhook_url")
  outboundWebhookSecret String?     @map("outbound_webhook_secret")

  /// O que ESTA Mantenedora contratou (ADR-0016). O teto continua sendo a env:
  /// o efetivo é a interseção dos dois, e é ela que o /me devolve.
  /// Chave ausente = módulo desligado.
  modulos               Json        @default("{}")

  /// Marca, escolhida no wizard. Vira token de CSS no front, nunca env de build.
  marcaNome             String?     @map("marca_nome")
  marcaCor              String?     @map("marca_cor")
  marcaCorClaro         String?     @map("marca_cor_claro")
  marcaCorEscuro        String?     @map("marca_cor_escuro")
  marcaCorSecundaria    String?     @map("marca_cor_secundaria")
  /// Id do arquivo no armazenamento (ADR-0024), nunca um caminho nem uma URL.
  marcaLogo             String?     @map("marca_logo")
  marcaTema             String      @default("claro") @map("marca_tema")

  /// Subdomínio do cliente. Na v1 é RÓTULO, não roteamento (ADR-0016 §5): a
  /// Mantenedora continua vindo da sessão.
  host                  String?
  /// Remetente dos e-mails de convite.
  remetente             String?
  /// Papel padrão de quem entra por convite. OWNER é recusado — seria
  /// transferência de titularidade disfarçada de cadastro (ADR-0018 §4).
  papelConvite          Role        @default(ATENDENTE) @map("papel_convite")

  /// Enquanto false, todo o resto do BFF responde 409 ONBOARDING_PENDENTE
  /// (ADR-0016 §4). Painel sem módulo escolhido não tem o que mostrar.
  onboardingConcluido   Boolean     @default(false) @map("onboarding_concluido")

  updatedAt             DateTime    @updatedAt @map("updated_at")

  @@map("mantenedora_settings")
}

enum TypebotBotStatus {
  ATIVO
  INATIVO
}

enum TypebotTriggerKind {
  PALAVRA_CHAVE
  NOVA_CONVERSA
}

/// Catálogo local dos bots Typebot Cloud. O fluxo continua no Typebot; escopo,
/// ativação e vínculo com a conta continuam no LeadsHug.
model TypebotBot {
  id            String          @id @default(uuid())
  mantenedoraId String          @map("mantenedora_id")
  mantenedora   Mantenedora     @relation(fields: [mantenedoraId], references: [id], onDelete: Cascade)
  typebotId     String          @map("typebot_id")
  publishedTypebotId String?    @map("published_typebot_id")
  name          String
  status        TypebotBotStatus @default(ATIVO)
  editorUrl     String          @map("editor_url")
  createdAt     DateTime        @default(now()) @map("created_at")
  updatedAt     DateTime        @updatedAt @map("updated_at")

  triggers TypebotTrigger[]
  sessions TypebotSession[]

  @@unique([mantenedoraId, typebotId])
  @@index([mantenedoraId, status])
  @@map("typebot_bots")
}

model TypebotTrigger {
  id        String             @id @default(uuid())
  botId     String             @map("bot_id")
  bot       TypebotBot         @relation(fields: [botId], references: [id], onDelete: Cascade)
  kind      TypebotTriggerKind
  value     String
  buId      String?            @map("bu_id")
  active    Boolean            @default(true)
  createdAt DateTime           @default(now()) @map("created_at")
  updatedAt DateTime           @updatedAt @map("updated_at")

  @@index([botId, active])
  @@map("typebot_triggers")
}

model TypebotSession {
  id            String     @id @default(uuid())
  botId         String     @map("bot_id")
  bot           TypebotBot @relation(fields: [botId], references: [id], onDelete: Cascade)
  mantenedoraId String     @map("mantenedora_id")
  buId          String     @map("bu_id")
  contato       String
  sessionId     String     @map("session_id")
  ativo         Boolean    @default(true)
  createdAt     DateTime   @default(now()) @map("created_at")
  updatedAt     DateTime   @updatedAt @map("updated_at")

  @@unique([botId, buId, contato])
  @@index([mantenedoraId, buId, contato])
  @@map("typebot_sessions")
}

/// Quem é dono de cada arquivo (ADR-0024 §5). O binário mora no volume; esta
/// tabela é o que permite barrar a leitura por escopo.
model Arquivo {
  id            String      @id
  mantenedoraId String      @map("mantenedora_id")
  mantenedora   Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Cascade)
  tipo          String
  bytes         Int
  createdAt     DateTime    @default(now()) @map("created_at")

  @@index([mantenedoraId])
  @@map("arquivos")
}

/// Convite e recuperação de senha — o mesmo mecanismo, validade diferente
/// (ADR-0025 §3).
enum TipoDeToken {
  CONVITE
  RECUPERACAO
}

/// O token vive HASHEADO: o valor em claro existe uma vez, no link. Vazamento do
/// banco não vira vazamento de contas — mesmo raciocínio da chave de API.
model TokenDeAcesso {
  id        String      @id @default(uuid())
  userId    String      @map("user_id")
  user      AppUser     @relation(fields: [userId], references: [id], onDelete: Cascade)
  tipo      TipoDeToken
  /// sha256 do valor. Único, para que a busca seja por igualdade e não varredura.
  hash      String      @unique
  expiraEm  DateTime    @map("expira_em")
  /// Uso ÚNICO: preenchido na mesma transação em que a senha é gravada.
  usadoEm   DateTime?   @map("usado_em")
  createdAt DateTime    @default(now()) @map("created_at")

  @@index([userId, tipo])
  @@map("tokens_de_acesso")
}

/* -------------------------- auditoria e webhook -------------------------- */

/// Ação humana auditável, transversal aos dois canais (ADR-0007 §5).
/// Autoria por snapshot: sobrevive à exclusão do usuário.
/// O escopo da linha (ADR-0020 §1.1). Existe para tornar o vazamento
/// IRREPRESENTÁVEL, não improvável: com `bu_id` nulável, NULL significaria "ação
/// da conta" E "alguém esqueceu de preencher" ao mesmo tempo, e a leitura teria
/// de virar `bu_id IS NULL OR ...`, que é a forma que a regra 0 proíbe.
enum EscopoDaAtividade {
  BU
  CONTA
}

/// As seis categorias do filtro (ADR-0020 §1). Cinco vêm do desenho; EXPORTACAO
/// é a sexta, e a divergência é deliberada.
enum CategoriaDeAtividade {
  CRIAR
  EDITAR
  MOVER
  ATENDIMENTO
  TAG
  EXPORTACAO
}

enum EntidadeDaAtividade {
  CARD
  CONVERSA
  NUMERO
  SETOR
  USUARIO
  INTEGRACAO
  CONFIGURACAO
}

/// O rastro das ações dos usuários (ADR-0020). NÃO é módulo: é núcleo, grava
/// sempre, e **não expurga** — o volume é texto curto, e auditoria com data de
/// validade falha justamente na pergunta antiga.
model ActivityLog {
  id            String   @id @default(uuid())
  mantenedoraId String   @map("mantenedora_id")

  escopo        EscopoDaAtividade
  /// Obrigatório quando escopo=BU, PROIBIDO quando escopo=CONTA. O CHECK no
  /// banco é quem cobra — não este comentário.
  buId          String?  @map("bu_id")

  userId        String?  @map("user_id")
  /// CONGELADO: o nome de quem agiu, naquele dia. Sobrevive à remoção da pessoa
  /// e ao renome de qualquer coisa.
  userName      String?  @map("user_name")
  userEmail     String?  @map("user_email")

  categoria     CategoriaDeAtividade
  entidade      EntidadeDaAtividade
  entidadeId    String?  @map("entidade_id")
  campo         String?
  de            String?
  para          String?
  /// Só para categoria que declare um formato no ADR-0022 — hoje, EXPORTACAO.
  detalhe       Json?

  /// A frase pronta, em português, CONGELADA na escrita.
  texto         String

  /// Compatibilidade com o que a v1 já gravava; some quando ninguém mais ler.
  action        String
  detail        String?
  ip            String?
  createdAt     DateTime @default(now()) @map("created_at")

  @@index([mantenedoraId, createdAt])
  @@index([entidade, entidadeId])
  @@map("activity_log")
}

/// O payload cru vive AQUI e só aqui, com expurgo de 90 dias (ADR-0009 §7).
model WebhookEvent {
  id        String      @id @default(uuid())
  channel   ChannelType
  buId      String?     @map("bu_id")
  eventType String      @map("event_type")
  payload   Json
  receivedAt DateTime   @default(now()) @map("received_at")

  @@index([receivedAt])
  @@map("webhook_events")
}

enum MessageTemplateDraftState {
  DRAFT
  LOCKED
}

/// Safe local draft snapshot. Provider identities and account references stay server-side.
model MessageTemplateDraft {
  id String @id @default(uuid())
  mantenedoraId String @map("mantenedora_id")
  mantenedora Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Restrict, map: "mt_draft_mantenedora_fkey")
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_draft_bu_fkey")
  creatorUserId String @map("creator_user_id")
  creator AppUser @relation(fields: [creatorUserId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_draft_creator_fkey")
  /// Historical immutable BuChannel id; the channel row is transient and may be detached.
  channelId String @map("channel_id")
  providerResourceIdentityId String @map("provider_resource_identity_id")
  providerResourceIdentity ProviderResourceIdentity @relation(fields: [providerResourceIdentityId, buId], references: [id, buId], onDelete: Restrict, map: "mt_draft_identity_fkey")
  accountReference String @map("account_reference") @db.VarChar(128)
  channelGeneration Int @map("channel_generation")
  pairingEpoch Int @map("pairing_epoch")
  activeCredentialVersion Int? @map("active_credential_version")
  clientRequestId String @map("client_request_id") @db.VarChar(128)
  requestHash String @map("request_hash") @db.Char(64)
  state MessageTemplateDraftState @default(DRAFT)
  revision Int @default(1)
  definition Json
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  revisions MessageTemplateRevision[]
  operations MessageTemplateOperation[]

  @@unique([id, buId, mantenedoraId], map: "mt_draft_id_bu_tenant_uq")

  @@unique([buId, creatorUserId, clientRequestId], map: "mt_draft_bu_creator_req_uq")
  @@index([buId, creatorUserId, createdAt, id], map: "mt_draft_bu_creator_created_idx")
  @@index([buId, createdAt, id], map: "mt_draft_bu_created_idx")
  @@map("message_template_drafts")
}

model MessageTemplateRevision {
  id String @id @default(uuid())
  draftId String @map("draft_id")
  draft MessageTemplateDraft @relation(fields: [draftId], references: [id], onDelete: Cascade, map: "mt_revision_draft_fkey")
  revision Int
  definition Json
  createdAt DateTime @default(now()) @map("created_at")

  @@unique([draftId, revision], map: "mt_revision_draft_rev_uq")
  @@map("message_template_revisions")
}

enum MessageTemplateOperationPhase {
  PREPARED
  SENDING
  ACCEPTED
  REJECTED
  AMBIGUOUS
}

enum MessageTemplateAcceptanceProvenance {
  ACKNOWLEDGED
  CORRELATED_BY_DEFINITION
}

/// Durable, immutable submit intent. The provider request is always derived
/// from this snapshot and can never be rebound to a later credential/account.
model MessageTemplateOperation {
  id String @id @default(uuid())
  mantenedoraId String @map("mantenedora_id")
  mantenedora Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Restrict, map: "mt_ops_mantenedora_fkey")
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_ops_bu_fkey")
  draftId String @map("draft_id")
  draft MessageTemplateDraft @relation(fields: [draftId, buId, mantenedoraId], references: [id, buId, mantenedoraId], onDelete: Restrict, map: "mt_ops_draft_fkey")
  actorUserId String @map("actor_user_id")
  actor AppUser @relation(fields: [actorUserId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_ops_actor_fkey")
  idempotencyKey String @map("idempotency_key") @db.Uuid
  requestHash String @map("request_hash") @db.Char(64)
  expectedFingerprint String @map("expected_fingerprint") @db.Char(64)
  revision Int
  definitionSnapshot Json @map("definition_snapshot")
  channelId String @map("channel_id")
  providerResourceIdentityId String @map("provider_resource_identity_id")
  accountReference String @map("account_reference") @db.VarChar(128)
  channelGeneration Int @map("channel_generation")
  pairingEpoch Int @map("pairing_epoch")
  activeCredentialVersion Int? @map("active_credential_version")
  phase MessageTemplateOperationPhase @default(PREPARED)
  version Int @default(1)
  dispatchClaimId String? @unique(map: "mt_ops_dispatch_claim_uq") @map("dispatch_claim_id") @db.Uuid
  leaseOwnerId String? @map("lease_owner_id") @db.Uuid
  leaseUntil DateTime? @map("lease_until")
  recoveryOwnerId String? @map("recovery_owner_id") @db.Uuid
  recoveryLeaseUntil DateTime? @map("recovery_lease_until")
  remoteTemplateId String? @map("remote_template_id") @db.VarChar(128)
  acknowledgedRemoteTemplateId String? @map("acknowledged_remote_template_id") @db.VarChar(128)
  safeCode String? @map("safe_code") @db.VarChar(64)
  providerStatus String? @map("provider_status") @db.VarChar(32)
  acceptanceProvenance MessageTemplateAcceptanceProvenance? @map("acceptance_provenance")
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  receipts MessageTemplateSubmissionReceipt[]
  reservation MessageTemplateNameReservation?
  quotaEvents MessageTemplateQuotaEvent[]

  @@unique([buId, actorUserId, idempotencyKey], map: "mt_ops_bu_actor_key_uq")
  @@unique([draftId, revision], map: "mt_ops_draft_revision_uq")
  @@index([buId, actorUserId, createdAt, id], map: "mt_ops_bu_actor_created_idx")
  @@index([accountReference, phase, leaseUntil], map: "mt_ops_account_phase_lease_idx")
  @@index([phase, recoveryLeaseUntil], map: "mt_ops_recovery_lease_idx")
  @@map("message_template_operations")
}

/// Append-only evidence; APIs project the latest ten without deleting history.
model MessageTemplateSubmissionReceipt {
  id String @id @default(uuid())
  operationId String @map("operation_id")
  operation MessageTemplateOperation @relation(fields: [operationId], references: [id], onDelete: Restrict, map: "mt_receipt_operation_fkey")
  sequence Int
  phase MessageTemplateOperationPhase
  safeCode String? @map("safe_code") @db.VarChar(64)
  remoteTemplateId String? @map("remote_template_id") @db.VarChar(128)
  acceptanceProvenance MessageTemplateAcceptanceProvenance? @map("acceptance_provenance")
  createdAt DateTime @default(now()) @map("created_at")

  @@unique([operationId, sequence], map: "mt_receipt_op_sequence_uq")
  @@index([operationId, createdAt, id], map: "mt_receipt_op_created_idx")
  @@map("message_template_submission_receipts")
}

/// Global account/name lock contains no tenant payload or user-visible ids.
model MessageTemplateNameReservation {
  id String @id @default(uuid())
  accountReference String @map("account_reference") @db.VarChar(128)
  name String @db.VarChar(128)
  language String @db.VarChar(35)
  operationId String @unique(map: "mt_res_operation_uq") @map("operation_id")
  operation MessageTemplateOperation @relation(fields: [operationId], references: [id], onDelete: Restrict, map: "mt_reservation_operation_fkey")
  createdAt DateTime @default(now()) @map("created_at")

  @@unique([accountReference, name, language], map: "mt_res_account_name_lang_uq")
  @@index([accountReference, createdAt], map: "mt_res_account_created_idx")
  @@map("message_template_name_reservations")
}

/// Durable events counted under per-scope advisory locks for exact sliding windows.
model MessageTemplateQuotaEvent {
  id String @id @default(uuid())
  kind String @db.VarChar(16)
  scopeKey String @map("scope_key") @db.VarChar(128)
  operationId String? @map("operation_id")
  operation MessageTemplateOperation? @relation(fields: [operationId], references: [id], onDelete: Restrict, map: "mt_quota_operation_fkey")
  occurredAt DateTime @default(now()) @map("occurred_at")

  @@unique([kind, operationId], map: "mt_quota_kind_operation_uq")
  @@index([kind, scopeKey, occurredAt], map: "mt_quota_scope_time_idx")
  @@map("message_template_quota_events")
}

/// One lease/fence shared by individual refresh and each explicit catalogue page.
model MessageTemplateObservationLease {
  contextKey String @id @map("context_key") @db.Char(64)
  mantenedoraId String @map("mantenedora_id")
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_lease_bu_fkey")
  channelId String @map("channel_id")
  accountReference String @map("account_reference") @db.VarChar(128)
  channelGeneration Int @map("channel_generation")
  pairingEpoch Int @map("pairing_epoch")
  providerResourceIdentityId String @map("provider_resource_identity_id")
  activeCredentialVersion Int @map("active_credential_version")
  ownerId String? @map("owner_id") @db.Uuid
  fence BigInt @default(0)
  leaseUntil DateTime? @map("lease_until")
  lastStartedAt DateTime? @map("last_started_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  observations MessageTemplateRemoteObservation[]
  pages MessageTemplateCatalogPage[]

  @@index([accountReference, leaseUntil], map: "mt_lease_account_expiry_idx")
  @@map("message_template_observation_leases")
}

/// The single semantic observation projector for both draft and catalog views.
model MessageTemplateRemoteObservation {
  id String @id @default(uuid())
  contextKey String @map("context_key") @db.Char(64)
  lease MessageTemplateObservationLease @relation(fields: [contextKey], references: [contextKey], onDelete: Restrict, map: "mt_observation_lease_fkey")
  remoteTemplateId String @map("remote_template_id") @db.VarChar(128)
  status String @db.VarChar(32)
  name String? @db.VarChar(128)
  language String? @db.VarChar(35)
  category String @db.VarChar(32)
  parameterFormat String @map("parameter_format") @db.VarChar(16)
  components Json
  semanticFingerprint String? @map("semantic_fingerprint") @db.Char(64)
  supported Boolean @default(false)
  available Boolean @default(true)
  safeCode String? @map("safe_code") @db.VarChar(64)
  observedEligible Boolean @default(false) @map("observed_eligible")
  observedAt DateTime @map("observed_at")
  observedFence BigInt @map("observed_fence")
  updatedAt DateTime @updatedAt @map("updated_at")

  @@unique([contextKey, remoteTemplateId], map: "mt_observation_context_remote_uq")
  @@index([contextKey, status, observedAt], map: "mt_observation_status_time_idx")
  @@map("message_template_remote_observations")
}

/// Cached explicit catalogue pages; GET never fans out to the provider.
model MessageTemplateCatalogPage {
  id String @id @default(uuid())
  contextKey String @map("context_key") @db.Char(64)
  lease MessageTemplateObservationLease @relation(fields: [contextKey], references: [contextKey], onDelete: Restrict, map: "mt_page_lease_fkey")
  cursorHash String @map("cursor_hash") @db.Char(64)
  requestedCursor String? @map("requested_cursor") @db.VarChar(512)
  remoteTemplateIds Json @map("remote_template_ids")
  nextCursor String? @map("next_cursor") @db.VarChar(512)
  available Boolean @default(true)
  safeCode String? @map("safe_code") @db.VarChar(64)
  observedAt DateTime @map("observed_at")
  observedFence BigInt @map("observed_fence")

  @@unique([contextKey, cursorHash], map: "mt_page_context_cursor_uq")
  @@index([contextKey, observedAt], map: "mt_page_context_time_idx")
  @@map("message_template_catalog_pages")
}

```

### api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql

SHA256 `a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```sql
BEGIN;
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '60s';

ALTER TABLE "messages"
  ADD COLUMN "official_inbound_at" TIMESTAMP(3);

CREATE INDEX "messages_conversation_trusted_window_idx"
  ON "messages"("conversation_id", "provider_resource_identity_id", "direction", "channel_origin", "official_inbound_at", "id");

COMMIT;

```

### api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql

SHA256 `78963dce996b2cec9e0990812a5091725238f9995e892c196e614ce9b2a6464f`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```sql
BEGIN;
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '60s';

CREATE TYPE "DispatchAdmissionCaller" AS ENUM ('BFF', 'PUBLIC', 'BOT');
CREATE TYPE "DispatchAdmissionState" AS ENUM ('PREPARED', 'SENDING', 'SETTLED', 'UNCERTAIN');
CREATE TYPE "InitialMessageIntentState" AS ENUM (
  'PREPARED', 'SENDING', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED',
  'SUCCEEDED', 'REJECTED', 'AMBIGUOUS'
);

CREATE TABLE "dispatch_admissions" (
  "id" TEXT NOT NULL,
  "conversation_id" TEXT NOT NULL,
  "bu_id" TEXT NOT NULL,
  "caller" "DispatchAdmissionCaller" NOT NULL,
  "actor_id" TEXT NOT NULL,
  "owner_nonce" TEXT NOT NULL,
  "selected_context" JSONB NOT NULL,
  "state" "DispatchAdmissionState" NOT NULL DEFAULT 'PREPARED',
  "expires_at" TIMESTAMP(3) NOT NULL,
  "dispatch_deadline_at" TIMESTAMP(3),
  "released_at" TIMESTAMP(3),
  "risk_acknowledged_at" TIMESTAMP(3),
  "risk_acknowledged_by_actor_id" TEXT,
  "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP(3) NOT NULL,
  CONSTRAINT "dispatch_admissions_pkey" PRIMARY KEY ("id"),
  CONSTRAINT "dispatch_admissions_conversation_id_fkey"
    FOREIGN KEY ("conversation_id") REFERENCES "conversations"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE UNIQUE INDEX "dispatch_admissions_owner_nonce_key" ON "dispatch_admissions"("owner_nonce");
CREATE INDEX "dispatch_admissions_active_conversation_idx"
  ON "dispatch_admissions"("conversation_id", "released_at", "state", "expires_at");

CREATE TABLE "initial_message_intents" (
  "id" TEXT NOT NULL,
  "conversation_id" TEXT NOT NULL,
  "bu_id" TEXT NOT NULL,
  "actor_id" TEXT NOT NULL,
  "idempotency_key" TEXT NOT NULL,
  "owner_nonce" TEXT NOT NULL,
  "request_fingerprint" TEXT NOT NULL,
  "request" JSONB NOT NULL,
  "selected_context" JSONB NOT NULL,
  "state" "InitialMessageIntentState" NOT NULL DEFAULT 'PREPARED',
  "lease_expires_at" TIMESTAMP(3) NOT NULL,
  "dispatch_deadline_at" TIMESTAMP(3),
  "external_message_id" TEXT,
  "slot_released_at" TIMESTAMP(3),
  "risk_acknowledged_at" TIMESTAMP(3),
  "risk_acknowledged_by_actor_id" TEXT,
  "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP(3) NOT NULL,
  CONSTRAINT "initial_message_intents_pkey" PRIMARY KEY ("id"),
  CONSTRAINT "initial_message_intents_conversation_id_fkey"
    FOREIGN KEY ("conversation_id") REFERENCES "conversations"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE UNIQUE INDEX "initial_message_intents_idempotency_key"
  ON "initial_message_intents"("bu_id", "actor_id", "idempotency_key");
CREATE UNIQUE INDEX "initial_message_intents_owner_nonce_key" ON "initial_message_intents"("owner_nonce");
-- SQL-only partial unique index: Prisma schema cannot represent the unreleased-slot predicate.
CREATE UNIQUE INDEX "initial_message_intents_active_conversation_key"
  ON "initial_message_intents"("conversation_id") WHERE "slot_released_at" IS NULL;
CREATE INDEX "initial_message_intents_slot_idx"
  ON "initial_message_intents"("conversation_id", "slot_released_at", "state", "created_at");
CREATE INDEX "initial_message_intents_actor_rate_idx"
  ON "initial_message_intents"("actor_id", "created_at" DESC);
-- SQL-only JSONB expression index: Prisma schema cannot represent the canonical account/resource expression.
CREATE INDEX "initial_message_intents_account_rate_idx"
  ON "initial_message_intents"((COALESCE("selected_context"->>'providerAccountReference', "selected_context"->>'providerResourceIdentityId')), "created_at" DESC);

COMMIT;

```

### api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql

SHA256 `60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```sql
BEGIN;
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '60s';

-- Supports the canonical BFF inbox order for every contact type. This is a
-- SQL-only expression index because Prisma schema syntax cannot express COALESCE.
CREATE INDEX "conversations_inbox_order_idx"
  ON "conversations" ("bu_id", "contact_type", (COALESCE("last_message_at", "created_at")) DESC, "id" DESC);

COMMIT;

```

### web-app/src/componentes/NovaConversa.tsx

SHA256 `2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { FormEvent, useCallback, useEffect, useRef, useState } from 'react';
import { api, ErroDaApi, templateApi, type TemplateSummary } from '../api';

interface OpenedConversation { conversaId: string; criada: boolean; contact: string }
const templateKey = (summary: TemplateSummary) => `${summary.remoteTemplateId}:${summary.language ?? ''}`;

export interface StartOptions {
  conversationId: string;
  channels: Array<{
    id: string;
    type: string;
    generation: number;
    pairingEpoch?: number;
    activeCredentialVersion?: number;
    supportedKinds: string[];
    availability: { text: string | null; 'approved-template': string | null };
  }>;
  activeAttempt: InitialAttempt | null;
  ordinaryAdmissions: Array<{ id: string; state: string; expiresAt: string; dispatchDeadlineAt: string | null; createdAt: string }>;
  admissionsTruncated: boolean;
  recentAttempts: InitialAttempt[];
  attemptsTruncated: boolean;
}

export interface InitialAttempt {
  id: string;
  state: string;
  externalAccepted?: boolean;
  providerAcceptance: string;
  receiptPersistence: string;
  localMessageState: string;
  recoveryAction: 'RECONCILE' | 'ACK_AFTER_DEADLINE' | null;
  eligibleAt?: string | null;
  slotReleasedAt?: string | null;
  riskAcknowledgementAvailable?: boolean;
}

function canonical(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonical).join(',')}]`;
  if (value && typeof value === 'object') {
    const row = value as Record<string, unknown>;
    return `{${Object.keys(row).sort().map((key) => `${JSON.stringify(key)}:${canonical(row[key])}`).join(',')}}`;
  }
  return JSON.stringify(value) ?? 'null';
}

/** Computes only the server-defined canonical semantic hash; it does not parse or authorize template grammar. */
export async function fingerprintInitialTemplate(summary: TemplateSummary): Promise<string> {
  const components = summary.components as Array<{ type?: unknown }>;
  const semanticComponents = [
    ...components.filter((component) => component.type === 'HEADER'),
    ...components.filter((component) => component.type === 'BODY'),
    ...components.filter((component) => component.type === 'FOOTER'),
  ];
  const canonicalSource = canonical({ version: 'initial-template-text-v1', remoteTemplateId: summary.remoteTemplateId,
    name: summary.name, language: summary.language, category: summary.category, parameterFormat: summary.parameterFormat,
    components: semanticComponents });
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(canonicalSource));
  return [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, '0')).join('');
}

function templateParameterNames(summary: TemplateSummary): string[] {
  const body = (summary.components as Array<{ type?: unknown; parameters?: unknown }>).find((component) => component.type === 'BODY');
  const parameters = Array.isArray(body?.parameters) ? body.parameters.filter((value): value is string => typeof value === 'string') : [];
  const unique = [...new Set(parameters)];
  return summary.parameterFormat === 'POSITIONAL' ? unique.sort((left, right) => Number(left) - Number(right)) : unique;
}

function attemptMessage(attempt: InitialAttempt): string {
  if (attempt.externalAccepted && attempt.localMessageState !== 'RECORDED') {
    return 'Envio aceito pelo canal; registro da conversa pendente. Aceite não confirma entrega.';
  }
  if (attempt.state === 'AMBIGUOUS' || attempt.providerAcceptance === 'UNKNOWN') {
    return 'Resultado do envio ainda desconhecido. Consulte o estado antes de qualquer nova ação.';
  }
  return 'O primeiro envio ainda está sendo processado.';
}

function operationError(cause: unknown, fallback: string): string {
  if (cause instanceof ErroDaApi && cause.codigo === 'ACK_TOO_EARLY') {
    return cause.eligibleAt
      ? `A confirmação de risco só estará disponível após ${new Date(cause.eligibleAt).toLocaleString('pt-BR')}.`
      : 'A confirmação de risco ainda não está disponível.';
  }
  return fallback;
}

function availabilityMessage(code: string | null | undefined): string | null {
  switch (code) {
    case 'JANELA_FECHADA': return 'A janela de texto livre foi encerrada. Escolha um modelo aprovado para iniciar o contato.';
    case 'UNSUPPORTED_KIND': return 'Este canal não oferece esse tipo de primeira mensagem.';
    case 'CHANNEL_NOT_READY': return 'O canal ainda não está pronto para iniciar o contato.';
    case 'CHANNEL_IDENTITY_NOT_VERIFIED': return 'A identidade do canal precisa ser conferida antes do envio.';
    case 'PENDING_CREDENTIAL': return 'A credencial do canal precisa ser atualizada.';
    default: return code ? 'Este tipo de envio está indisponível para o canal selecionado.' : null;
  }
}

function channelLabel(type: string): string {
  if (type === 'OFICIAL') return 'WhatsApp oficial';
  if (type === 'NAO_OFICIAL') return 'WhatsApp não oficial';
  return 'Canal de mensagens';
}

interface Preview {
  text: string;
  previewFingerprint: string;
  channel: { channelId: string; channelOrigin: string; generation: number; requiresWindow: boolean };
}

interface InitialSendSnapshot {
  key: string;
  request: string;
  body: { channelId: string; expectedGeneration: number; mensagem: Record<string, unknown>; previewFingerprint: string };
  attemptId?: string;
  hadUnknownOutcome?: boolean;
}

// Both text and rendered templates are capped at 4,096 code points. In the
// worst case JSON escapes each control character to six ASCII characters.
const MAX_INITIAL_SNAPSHOT_REQUEST_LENGTH = 32_768;

export function isInitialSendSnapshot(value: unknown): value is InitialSendSnapshot {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return false;
  const snapshot = value as Partial<InitialSendSnapshot>;
  const body = snapshot.body;
  if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(snapshot.key ?? '')
    || typeof snapshot.request !== 'string' || snapshot.request.length > MAX_INITIAL_SNAPSHOT_REQUEST_LENGTH
    || !body || typeof body !== 'object' || Array.isArray(body)
    || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(body.channelId)
    || !Number.isInteger(body.expectedGeneration) || body.expectedGeneration < 1
    || typeof body.previewFingerprint !== 'string' || !/^[0-9a-f]{64}$/i.test(body.previewFingerprint)
    || Object.keys(body).sort().join(',') !== 'channelId,expectedGeneration,mensagem,previewFingerprint'
    || !body.mensagem || typeof body.mensagem !== 'object' || Array.isArray(body.mensagem)
    || canonical(body) !== snapshot.request) return false;
  const message = body.mensagem;
  if (message.tipo === 'TEXTO') {
    return Object.keys(message).sort().join(',') === 'texto,tipo'
      && typeof message.texto === 'string' && message.texto.length > 0 && [...message.texto].length <= 4096;
  }
  if (message.tipo !== 'TEMPLATE' || typeof message.templateId !== 'string' || message.templateId.length === 0 || message.templateId.length > 200
    || typeof message.language !== 'string' || message.language.length === 0 || message.language.length > 64
    || typeof message.expectedDefinitionFingerprint !== 'string' || !/^[0-9a-f]{64}$/i.test(message.expectedDefinitionFingerprint)
    || (message.catalogAfter !== undefined && (typeof message.catalogAfter !== 'string' || message.catalogAfter.length > 512))
    || !(Array.isArray(message.parameters) || (message.parameters && typeof message.parameters === 'object'))
    || (Array.isArray(message.parameters) && (message.parameters.length > 20 || message.parameters.some((item) => typeof item !== 'string' || [...item].length > 1024)))
    || (message.parameters && !Array.isArray(message.parameters) && (Object.keys(message.parameters).length > 20
      || Object.entries(message.parameters).some(([name, item]) => name.length > 40 || typeof item !== 'string' || [...item].length > 1024)))) return false;
  return Object.keys(message).every((key) => ['tipo', 'templateId', 'language', 'catalogAfter', 'expectedDefinitionFingerprint', 'parameters'].includes(key));
}

export function NovaConversa({ buId, onOpened, onClose }: {
  buId: string;
  onOpened: (result: OpenedConversation) => void;
  onClose: () => void;
}) {
  const [telefone, setTelefone] = useState('');
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const openGeneration = useRef(0);
  const openBu = useRef(buId);
  const openLatch = useRef(false);
  const openMounted = useRef(true);
  useEffect(() => {
    openMounted.current = true;
    return () => { openMounted.current = false; openGeneration.current += 1; };
  }, []);
  if (openBu.current !== buId) {
    openBu.current = buId;
    openGeneration.current += 1;
  }

  async function submit(event: FormEvent) {
    event.preventDefault();
    if (!buId || openLatch.current) return;
    openLatch.current = true;
    const requestGeneration = openGeneration.current;
    setSaving(true);
    setError(null);
    try {
      const result = await api.post<OpenedConversation>(`/business-units/${buId}/conversations/open`, { telefone });
      if (!openMounted.current || requestGeneration !== openGeneration.current || openBu.current !== buId) return;
      onOpened(result);
    } catch (cause) {
      if (openMounted.current && requestGeneration === openGeneration.current) setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível abrir a conversa.');
    } finally {
      if (openMounted.current && requestGeneration === openGeneration.current) setSaving(false);
      openLatch.current = false;
    }
  }

  return <div role="dialog" aria-modal="true" aria-labelledby="nova-conversa-titulo" className="cartao grade">
    <div className="linha"><strong id="nova-conversa-titulo">Nova conversa</strong><button type="button" onClick={onClose} disabled={saving}>Fechar</button></div>
    <form className="grade" onSubmit={(event) => void submit(event)}>
      <label>Telefone com DDI explícito
        <input autoFocus inputMode="tel" autoComplete="tel" maxLength={40} value={telefone} onChange={(event) => setTelefone(event.target.value)} />
      </label>
      <span className="suave">Informe o código do país. O sistema não adivinha o DDI.</span>
      {error && <span role="alert" className="erro">{error}</span>}
      <button className="primario" disabled={!telefone.trim() || saving}>{saving ? 'Abrindo…' : 'Abrir ou reutilizar'}</button>
    </form>
  </div>;
}

export function PrimeiraMensagem({ actorId, buId, conversationId, options, onOptions, onComplete, onCancel }: {
  actorId: string;
  buId: string;
  conversationId: string;
  options: StartOptions;
  onOptions: (options: StartOptions) => void;
  onComplete: () => void;
  onCancel?: () => void;
}) {
  const [channelId, setChannelId] = useState('');
  const [kind, setKind] = useState<'text' | 'approved-template'>('text');
  const [text, setText] = useState('');
  const [catalog, setCatalog] = useState<TemplateSummary[]>([]);
  const [catalogAfter, setCatalogAfter] = useState<string | null>(null);
  const [catalogCursorByTemplate, setCatalogCursorByTemplate] = useState<Record<string, string | null>>({});
  const [selectedTemplate, setSelectedTemplate] = useState('');
  const [parameterValues, setParameterValues] = useState<Record<string, string>>({});
  const [preview, setPreview] = useState<Preview | null>(null);
  const [previewing, setPreviewing] = useState(false);
  const [sending, setSending] = useState(false);
  const [catalogBusy, setCatalogBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [confirmRisk, setConfirmRisk] = useState(false);
  const [retryOnly, setRetryOnly] = useState(false);
  const [sendSnapshot, setSendSnapshot] = useState<InitialSendSnapshot | null>(null);
  const [snapshotLoaded, setSnapshotLoaded] = useState(false);
  const [storageReadUnavailable, setStorageReadUnavailable] = useState(false);
  const [consulted, setConsulted] = useState<InitialAttempt | null>(null);
  const [recoveredAttempt, setRecoveredAttempt] = useState<InitialAttempt | null>(null);
  const generation = useRef(0);
  const previewLatch = useRef(false);
  const sendLatch = useRef(false);
  const sendSnapshotRef = useRef<InitialSendSnapshot | null>(null);
  const mounted = useRef(true);
  const catalogRequest = useRef(0);
  const storageKey = `leadshug:initial-send:v1:${encodeURIComponent(actorId)}:${encodeURIComponent(buId)}:${encodeURIComponent(conversationId)}`;

  const saveSnapshot = useCallback((value: InitialSendSnapshot | null): boolean => {
    sendSnapshotRef.current = value;
    setSendSnapshot(value);
    try {
      if (value) sessionStorage.setItem(storageKey, JSON.stringify(value));
      else sessionStorage.removeItem(storageKey);
      return true;
    } catch { return false; }
  }, [storageKey]);

  const clearSnapshot = useCallback(() => {
    saveSnapshot(null);
    setRetryOnly(false);
  }, [saveSnapshot]);

  const restoreSnapshot = useCallback(() => {
    try {
      const raw = sessionStorage.getItem(storageKey);
      const parsed = raw ? JSON.parse(raw) as unknown : null;
      if (isInitialSendSnapshot(parsed)) {
        const restored = { ...parsed, hadUnknownOutcome: true };
        sendSnapshotRef.current = restored;
        setSendSnapshot(restored);
        setRetryOnly(true);
      } else if (raw) {
        sessionStorage.removeItem(storageKey);
      }
      setStorageReadUnavailable(false);
      setError(null);
    } catch {
      // A failed read cannot prove that no idempotency snapshot exists.
      setStorageReadUnavailable(true);
    }
  }, [storageKey]);

  useEffect(() => {
    generation.current += 1;
    return () => { generation.current += 1; };
  }, [conversationId]);

  useEffect(() => {
    mounted.current = true;
    return () => { mounted.current = false; };
  }, []);

  useEffect(() => {
    setSnapshotLoaded(false);
    sendSnapshotRef.current = null;
    setSendSnapshot(null);
    setRetryOnly(false);
    setStorageReadUnavailable(false);
    restoreSnapshot();
    setSnapshotLoaded(true);
  }, [storageKey, restoreSnapshot]);

  useEffect(() => {
    const snapshot = sendSnapshotRef.current;
    if (!snapshot?.attemptId) return;
    const durable = [options.activeAttempt, ...options.recentAttempts].find((item) => item?.id === snapshot.attemptId);
    if (durable && (durable.state === 'SUCCEEDED' || durable.state === 'REJECTED' || durable.slotReleasedAt)) clearSnapshot();
  }, [options.activeAttempt, options.recentAttempts, clearSnapshot]);

  const channel = options.channels.find((item) => item.id === channelId) ?? null;
  const selectedSummary = catalog.find((item) => templateKey(item) === selectedTemplate) ?? null;
  const parameterNames = selectedSummary ? templateParameterNames(selectedSummary) : [];
  const kindAvailability = channel?.availability[kind];
  const kindUnavailable = !channel || kindAvailability !== null;
  const kindUnavailableMessage = availabilityMessage(kindAvailability);
  const storageBlocked = !snapshotLoaded || storageReadUnavailable;
  const attempt = options.activeAttempt ?? recoveredAttempt ?? options.recentAttempts.find((item) => item.slotReleasedAt === null && item.recoveryAction !== null) ?? null;
  const ordinaryUncertain = options.ordinaryAdmissions.some((item) => ['SENDING', 'UNCERTAIN'].includes(item.state));
  const locked = Boolean(options.activeAttempt || (recoveredAttempt && recoveredAttempt.slotReleasedAt === null)) || ordinaryUncertain;
  const currentGeneration = () => generation.current;
  const invalidateDraft = () => { generation.current += 1; setPreview(null); setError(null); };

  useEffect(() => {
    generation.current += 1;
    setPreview(null);
    setError(null);
    setCatalogCursorByTemplate({});
    if (kind !== 'approved-template' || !channelId) return;
    const owner = ++catalogRequest.current;
    let current = true;
    setCatalog([]);
    setCatalogAfter(null);
    setSelectedTemplate('');
    setParameterValues({});
    setCatalogBusy(true);
    templateApi.catalog(buId, channelId).then((page) => {
      if (!current) return;
      setCatalog(page.items ?? []);
      setCatalogAfter(page.nextCursor);
      setCatalogCursorByTemplate(Object.fromEntries((page.items ?? []).map((item) => [templateKey(item), null])));
      setNotice(page.available ? null : 'Atualize o catálogo para observar os modelos desta conta.');
    }).catch((cause) => { if (current) setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível ler o catálogo.'); })
      .finally(() => { if (mounted.current && catalogRequest.current === owner) setCatalogBusy(false); });
    return () => { current = false; if (catalogRequest.current === owner) catalogRequest.current += 1; };
  }, [buId, channelId, kind]);

  useEffect(() => {
    generation.current += 1;
    setPreview(null);
  }, [channel?.generation, channel?.pairingEpoch, channel?.activeCredentialVersion]);

  function messageFor(kindValue = kind, content = text): Record<string, unknown> {
    if (kindValue === 'text') return { tipo: 'TEXTO', texto: content };
    const summary = selectedSummary;
    if (!summary || !summary.language) throw new Error('Selecione um modelo observado no catálogo.');
    const values = summary.parameterFormat === 'POSITIONAL'
      ? parameterNames.map((name) => parameterValues[name] ?? '')
      : Object.fromEntries(parameterNames.map((name) => [name, parameterValues[name] ?? '']));
    return { tipo: 'TEMPLATE', templateId: summary.remoteTemplateId, language: summary.language,
      ...(catalogCursorByTemplate[selectedTemplate] ? { catalogAfter: catalogCursorByTemplate[selectedTemplate] } : {}),
      expectedDefinitionFingerprint: '0'.repeat(64), parameters: values };
  }

  async function withTemplateFingerprint(): Promise<Record<string, unknown>> {
    const message = messageFor();
    if (kind === 'text') return message;
    const summary = selectedSummary;
    if (!summary) return message;
    return { ...message, expectedDefinitionFingerprint: await fingerprintInitialTemplate(summary) };
  }

  async function refreshCatalog() {
    if (!channel || catalogBusy) return;
    invalidateDraft();
    const owner = ++catalogRequest.current;
    const current = currentGeneration();
    setCatalogBusy(true); setError(null); setNotice(null);
    try {
      const result = await templateApi.refreshCatalog(buId, channel.id);
      if (generation.current !== current || catalogRequest.current !== owner) return;
      if ('phase' in result) { setNotice('Atualização do catálogo em andamento; tente novamente em instantes.'); return; }
      setCatalog(result.items ?? []); setCatalogAfter(result.nextCursor);
      setCatalogCursorByTemplate(Object.fromEntries((result.items ?? []).map((item) => [templateKey(item), null])));
      setSelectedTemplate('');
      setNotice(result.available ? 'Catálogo atualizado.' : 'O catálogo não está disponível para este canal.');
    } catch (cause) { if (generation.current === current) setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível atualizar o catálogo.'); }
    finally { if (mounted.current && catalogRequest.current === owner) setCatalogBusy(false); }
  }

  async function loadMoreTemplates() {
    if (!channel || !catalogAfter || catalogBusy) return;
    invalidateDraft();
    const owner = ++catalogRequest.current;
    const current = currentGeneration();
    setCatalogBusy(true); setError(null);
    try {
      const page = await templateApi.catalog(buId, channel.id, catalogAfter);
      if (generation.current !== current || catalogRequest.current !== owner) return;
      setCatalog((previous) => [...previous, ...page.items]); setCatalogAfter(page.nextCursor);
      setCatalogCursorByTemplate((previous) => ({ ...previous, ...Object.fromEntries(page.items.map((item) => [templateKey(item), catalogAfter])) }));
    } catch (cause) { if (generation.current === current) setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível carregar mais modelos.'); }
    finally { if (mounted.current && catalogRequest.current === owner) setCatalogBusy(false); }
  }

  async function previewMessage() {
    if (previewLatch.current || !snapshotLoaded || storageReadUnavailable || !channel || locked || retryOnly) return;
    previewLatch.current = true;
    const current = currentGeneration();
    setPreviewing(true); setError(null); setNotice(null); setPreview(null);
    try {
      const message = await withTemplateFingerprint();
      if (generation.current !== current) return;
      const result = await api.post<Preview>(`/conversations/${conversationId}/initial-message-preview`, {
        channelId: channel.id, expectedGeneration: channel.generation, mensagem: message,
      });
      if (generation.current !== current) return;
      setPreview(result);
    } catch (cause) {
      if (generation.current === current) setError(cause instanceof ErroDaApi ? cause.message : cause instanceof Error ? cause.message : 'A prévia não está disponível.');
    } finally {
      previewLatch.current = false;
      if (mounted.current) setPreviewing(false);
    }
  }

  async function resumeOriginal() {
    const snapshot = sendSnapshotRef.current;
    if (!snapshot || !snapshotLoaded || storageReadUnavailable || sendLatch.current) return;
    sendLatch.current = true;
    const current = currentGeneration();
    setSending(true); setError(null); setNotice(null);
    try {
      const result = await api.postWithHeaders<{ attempt: InitialAttempt }>(`/conversations/${conversationId}/initial-messages`, snapshot.body, {
        'Idempotency-Key': snapshot.key,
      });
      if (generation.current !== current || !mounted.current) return;
      setRecoveredAttempt(result.attempt);
      saveSnapshot({ ...snapshot, attemptId: result.attempt.id, hadUnknownOutcome: true });
      if (result.attempt.state === 'SUCCEEDED' || result.attempt.state === 'REJECTED' || result.attempt.slotReleasedAt) clearSnapshot();
      await reloadOptions();
      if (generation.current !== current || !mounted.current) return;
      setNotice(result.attempt.state === 'SUCCEEDED' ? 'Primeira mensagem registrada na conversa.' : 'Envio em andamento; consulte o estado antes de tentar novamente.');
      if (result.attempt.state === 'SUCCEEDED') onComplete();
    } catch (cause) {
      if (generation.current === current && mounted.current) {
        if (cause instanceof ErroDaApi && cause.attemptId && cause.state) {
          saveSnapshot({ ...snapshot, attemptId: cause.attemptId, hadUnknownOutcome: true });
        }
        setRetryOnly(true);
        setError(operationError(cause, 'O resultado ainda não foi confirmado. Consulte a tentativa original antes de enviar outra mensagem.'));
        await reloadOptions();
      }
    } finally {
      sendLatch.current = false;
      if (mounted.current) setSending(false);
    }
  }

  async function sendMessage() {
    if (retryOnly && sendSnapshotRef.current?.hadUnknownOutcome) { await resumeOriginal(); return; }
    if (sendLatch.current || !snapshotLoaded || storageReadUnavailable || !channel || !preview || locked || retryOnly) return;
    sendLatch.current = true;
    const current = currentGeneration();
    setSending(true); setError(null); setNotice(null);
    try {
      const mensagem = await withTemplateFingerprint();
      if (generation.current !== current) return;
      const body = { channelId: channel.id, expectedGeneration: channel.generation, mensagem, previewFingerprint: preview.previewFingerprint };
      const request = canonical(body);
      let snapshot = sendSnapshotRef.current;
      if (snapshot && snapshot.request !== request) throw new Error('O envio anterior não foi confirmado. Consulte o estado antes de alterar ou repetir a mensagem.');
      if (!snapshot) {
        snapshot = { key: crypto.randomUUID(), request, body, hadUnknownOutcome: false };
        if (!saveSnapshot(snapshot)) {
          sendSnapshotRef.current = null;
          setSendSnapshot(null);
          setError('Não foi possível guardar a tentativa neste navegador. Nenhuma mensagem foi enviada.');
          return;
        }
      }
      const result = await api.postWithHeaders<{ attempt: InitialAttempt }>(`/conversations/${conversationId}/initial-messages`, snapshot.body,
        { 'Idempotency-Key': snapshot.key });
      if (generation.current !== current || !mounted.current) return;
      setRecoveredAttempt(result.attempt);
      if (sendSnapshotRef.current) {
        const confirmed = { ...sendSnapshotRef.current, attemptId: result.attempt.id };
        saveSnapshot(confirmed);
      }
      if (result.attempt.state === 'SUCCEEDED' || result.attempt.state === 'REJECTED' || result.attempt.slotReleasedAt) {
        clearSnapshot();
      } else {
        setRetryOnly(true);
      }
      await reloadOptions();
      if (generation.current !== current) return;
      setNotice(result.attempt.state === 'SUCCEEDED' ? 'Primeira mensagem registrada na conversa.' : 'Envio em andamento; consulte o estado antes de tentar novamente.');
      if (result.attempt.state === 'SUCCEEDED') onComplete();
    } catch (cause) {
      if (generation.current === current) {
        if (cause instanceof ErroDaApi && cause.preAdmission === true && !retryOnly && !sendSnapshotRef.current?.hadUnknownOutcome) {
          clearSnapshot();
          setPreview(null);
          setError('A prévia precisa ser atualizada antes de iniciar. Revise as opções e gere uma nova prévia.');
          await reloadOptions();
          return;
        }
        if (cause instanceof ErroDaApi && cause.attemptId && cause.state) {
          const fallback: InitialAttempt = {
            id: cause.attemptId, state: cause.state, externalAccepted: cause.providerAcceptance === 'CONFIRMED',
            providerAcceptance: cause.providerAcceptance ?? 'UNKNOWN', receiptPersistence: cause.receiptPersistence ?? 'UNCONFIRMED',
            localMessageState: cause.localMessageState ?? 'UNCONFIRMED', eligibleAt: cause.eligibleAt ?? null, slotReleasedAt: null,
            recoveryAction: cause.state === 'AMBIGUOUS' ? 'ACK_AFTER_DEADLINE' : ['SENDING', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(cause.state) ? 'RECONCILE' : null,
            riskAcknowledgementAvailable: ['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(cause.state),
          };
          setRecoveredAttempt(fallback);
          if (sendSnapshotRef.current) {
            const withAttempt = { ...sendSnapshotRef.current, attemptId: cause.attemptId };
            saveSnapshot(withAttempt);
          }
        }
        if (sendSnapshotRef.current) {
          const uncertain = { ...sendSnapshotRef.current, hadUnknownOutcome: true };
          saveSnapshot(uncertain);
          setRetryOnly(true);
        }
        setError(operationError(cause, 'Não foi possível confirmar o resultado. Consulte o estado antes de tentar novamente.'));
        await reloadOptions();
      }
    } finally {
      sendLatch.current = false;
      if (mounted.current) setSending(false);
    }
  }

  async function reloadOptions() {
    const current = currentGeneration();
    try {
      const fresh = await api.get<StartOptions>(`/conversations/${conversationId}/start-options`);
      if (generation.current === current) {
        if (fresh.activeAttempt) setRecoveredAttempt(fresh.activeAttempt);
        onOptions(fresh);
      }
    } catch (cause) {
      if (generation.current === current) setError(operationError(cause, 'Não foi possível conferir o estado atual.'));
    }
  }

  async function consultState() {
    if (!attempt || sendLatch.current) return;
    const current = currentGeneration();
    try {
      const state = await api.get<InitialAttempt>(`/conversations/${conversationId}/initial-messages/${attempt.id}`);
      if (generation.current === current) {
        setConsulted(state); setRecoveredAttempt(state);
        if (sendSnapshotRef.current?.attemptId === state.id && (state.state === 'SUCCEEDED' || state.state === 'REJECTED' || state.slotReleasedAt)) {
          clearSnapshot();
        }
        await reloadOptions();
      }
    } catch (cause) { if (generation.current === current) setError(operationError(cause, 'Não foi possível consultar o estado.')); }
  }

  async function reconcileLocal() {
    if (!attempt || attempt.recoveryAction !== 'RECONCILE' || sendLatch.current) return;
    sendLatch.current = true;
    const current = currentGeneration();
    setSending(true); setError(null);
    try {
      const response = await api.post<InitialAttempt>(`/conversations/${conversationId}/initial-messages/${attempt.id}/reconcile`, {});
      if (generation.current !== current) return;
      setRecoveredAttempt(response);
      if (sendSnapshotRef.current?.attemptId === response.id && (response.state === 'SUCCEEDED' || response.state === 'REJECTED' || response.slotReleasedAt)) {
        clearSnapshot();
      }
      await reloadOptions();
      if (generation.current !== current) return;
      setNotice(response.state === 'SUCCEEDED' ? 'Registro local concluído; nenhuma nova chamada ao canal foi feita.' : 'Estado consultado; nenhuma nova chamada ao canal foi feita.');
      if (response.state === 'SUCCEEDED') onComplete();
    } catch (cause) { if (generation.current === current) setError(operationError(cause, 'Não foi possível concluir o registro local.')); }
    finally { sendLatch.current = false; if (mounted.current) setSending(false); }
  }

  async function acknowledgeRisk() {
    if (!attempt || !(attempt.recoveryAction === 'ACK_AFTER_DEADLINE' || attempt.riskAcknowledgementAvailable) || !confirmRisk || sendLatch.current) return;
    sendLatch.current = true;
    const current = currentGeneration();
    setSending(true); setError(null);
    try {
      const response = await api.postWithHeaders<InitialAttempt>(`/conversations/${conversationId}/initial-messages/${attempt.id}/acknowledge`, {}, {
        'X-Confirm-Duplication-Risk': 'true',
      });
      if (generation.current !== current) return;
      setRecoveredAttempt(response);
      if (sendSnapshotRef.current?.attemptId === response.id && response.slotReleasedAt) {
        clearSnapshot();
      }
      setConfirmRisk(false);
      await reloadOptions();
      if (generation.current !== current) return;
      setNotice('Bloqueio de reenvio reconhecido. Nenhum envio foi repetido.');
    } catch (cause) { if (generation.current === current) setError(operationError(cause, 'Não foi possível registrar a confirmação de risco.')); }
    finally { sendLatch.current = false; if (mounted.current) setSending(false); }
  }

  if (locked && attempt) return <section className="cartao grade" aria-label="Recuperação do primeiro envio">
    <strong>{attemptMessage(consulted ?? attempt)}</strong>
    {(consulted ?? attempt).eligibleAt && <span>Confirmação de risco disponível após {new Date((consulted ?? attempt).eligibleAt!).toLocaleString('pt-BR')}.</span>}
    {error && <span role="alert" className="erro">{error}</span>}
    {notice && <span role="status">{notice}</span>}
    <button type="button" onClick={() => void consultState()} disabled={sending}>Consultar estado</button>
    {attempt.recoveryAction === 'RECONCILE' && <button type="button" onClick={() => void reconcileLocal()} disabled={sending}>Concluir registro local</button>}
    {(attempt.recoveryAction === 'ACK_AFTER_DEADLINE' || attempt.riskAcknowledgementAvailable) && <>
      <label><input type="checkbox" checked={confirmRisk} onChange={(event) => setConfirmRisk(event.target.checked)} />Confirmo o risco de mensagem duplicada.</label>
      <button type="button" onClick={() => void acknowledgeRisk()} disabled={sending || !confirmRisk}>Reconhecer risco sem reenviar</button>
    </>}
  </section>;

  return <section className="cartao grade" aria-label="Primeira mensagem">
    <h2>Primeira mensagem</h2>
    <label>Canal selecionado
      <select value={channelId} onChange={(event) => { invalidateDraft(); setCatalogBusy(false); setChannelId(event.target.value); setSelectedTemplate(''); }} disabled={storageBlocked || retryOnly || sending}>
        <option value="">Selecione um canal</option>
        {options.channels.map((item) => <option key={item.id} value={item.id}>{channelLabel(item.type)}</option>)}
      </select>
    </label>
    {options.channels.length === 0 && <span role="status">Nenhum canal está disponível para iniciar o contato.</span>}
    {kindUnavailableMessage && <span role="status">{kindUnavailableMessage}</span>}
    <label>Tipo de primeira mensagem
      <select value={kind} onChange={(event) => { invalidateDraft(); setCatalogBusy(false); setKind(event.target.value as typeof kind); setSelectedTemplate(''); setParameterValues({}); }} disabled={storageBlocked || !channel || retryOnly || sending}>
        <option value="text">Texto</option>
        {channel?.supportedKinds.includes('approved-template') && <option value="approved-template">Modelo aprovado</option>}
      </select>
    </label>
    {kind === 'text' ? <label>Mensagem inicial
      <textarea value={text} onChange={(event) => { invalidateDraft(); setText([...event.target.value].slice(0, 4096).join('')); }} disabled={storageBlocked || retryOnly || sending} />
    </label> : <>
      <label>Modelo do catálogo
        <select value={selectedTemplate} onChange={(event) => { invalidateDraft(); setSelectedTemplate(event.target.value); setParameterValues({}); }} disabled={storageBlocked || retryOnly || sending}>
          <option value="">Selecione um modelo observado</option>
          {catalog.map((item) => <option key={templateKey(item)} value={templateKey(item)}>
            {item.name ?? item.remoteTemplateId} · {item.language ?? 'idioma desconhecido'} · {item.status}
          </option>)}
        </select>
      </label>
      {selectedSummary && parameterNames.map((name) => <label key={name}>Parâmetro {name}
        <input value={parameterValues[name] ?? ''}
          onChange={(event) => { invalidateDraft(); setParameterValues((values) => ({ ...values, [name]: [...event.target.value].slice(0, 1024).join('') })); }} disabled={storageBlocked || retryOnly || sending} />
      </label>)}
      <div className="linha">
        <button type="button" onClick={() => void refreshCatalog()} disabled={storageBlocked || catalogBusy || retryOnly || sending}>{catalogBusy ? 'Consultando…' : 'Atualizar catálogo'}</button>
        {catalogAfter && <button type="button" onClick={() => void loadMoreTemplates()} disabled={storageBlocked || catalogBusy || retryOnly || sending}>Mais modelos</button>}
      </div>
    </>}
    {storageReadUnavailable
      ? <span role="alert" className="erro">Não foi possível verificar a tentativa salva neste navegador.</span>
      : error && <span role="alert" className="erro">{error}</span>}
    {storageReadUnavailable && <button type="button" onClick={restoreSnapshot} disabled={sending}>Recuperar tentativa salva</button>}
    {notice && <span role="status">{notice}</span>}
    <div className="linha">
      {onCancel && <button type="button" onClick={onCancel} disabled={sending || previewing}>Voltar ao histórico</button>}
      <button type="button" onClick={() => void previewMessage()} disabled={storageBlocked || retryOnly || previewing || sending || kindUnavailable || (kind === 'text' && !text.trim()) || (kind === 'approved-template' && (!selectedSummary || parameterNames.some((name) => !(parameterValues[name] ?? '').trim())))}>
        {previewing ? 'Pré-visualizando…' : 'Pré-visualizar'}
      </button>
      <button type="button" className="primario" onClick={() => void sendMessage()} disabled={storageBlocked || locked || sending || previewing || (!retryOnly && (kindUnavailable || !preview)) || (retryOnly && !sendSnapshot)}>
        {sending ? 'Enviando…' : retryOnly ? 'Retomar tentativa original' : 'Confirmar primeiro envio'}
      </button>
    </div>
    {preview && <div className="aviso" aria-label="Prévia da primeira mensagem">
      <strong>Prévia segura</strong><p>{preview.text}</p>
      {preview.channel.requiresWindow && <span>O canal exige janela atual para texto livre.</span>}
    </div>}
    {retryOnly && sendSnapshot && <span role="status">O resultado ainda não foi confirmado. Consulte a tentativa original antes de enviar outra mensagem.</span>}
    {locked && <span role="alert">Há outra operação ativa; nenhuma nova mensagem será enviada.</span>}
  </section>;
}

export function OrdinaryRecovery({ conversationId, admission, onOptions }: {
  conversationId: string;
  admission: StartOptions['ordinaryAdmissions'][number];
  onOptions: (options: StartOptions) => void;
}) {
  const [confirmRisk, setConfirmRisk] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [now, setNow] = useState(Date.now());
  const actionOwner = useRef(0);
  const actionLatch = useRef(false);
  const actionMounted = useRef(true);
  useEffect(() => {
    actionMounted.current = true;
    actionOwner.current += 1;
    return () => { actionMounted.current = false; actionOwner.current += 1; };
  }, [conversationId, admission.id]);
  useEffect(() => {
    const timer = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(timer);
  }, []);
  const eligibleAt = admission.dispatchDeadlineAt ? Date.parse(admission.dispatchDeadlineAt) : Number.POSITIVE_INFINITY;
  const refresh = async (owner: number) => {
    const options = await api.get<StartOptions>(`/conversations/${conversationId}/start-options`);
    if (actionMounted.current && actionOwner.current === owner) onOptions(options);
  };
  async function reconcile() {
    if (actionLatch.current) return;
    actionLatch.current = true;
    const owner = actionOwner.current;
    setBusy(true); setError(null); setNotice(null);
    try {
      await api.post(`/conversations/${conversationId}/dispatch-admissions/${admission.id}/reconcile`, {});
      await refresh(owner);
      if (actionMounted.current && actionOwner.current === owner) setNotice('Estado atualizado sem repetir o envio.');
    } catch (cause) { if (actionMounted.current && actionOwner.current === owner) setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível consultar o estado.'); }
    finally { actionLatch.current = false; if (actionMounted.current && actionOwner.current === owner) setBusy(false); }
  }
  async function acknowledge() {
    if (actionLatch.current || !confirmRisk || now < eligibleAt) return;
    actionLatch.current = true;
    const owner = actionOwner.current;
    setBusy(true); setError(null); setNotice(null);
    try {
      await api.postWithHeaders(`/conversations/${conversationId}/dispatch-admissions/${admission.id}/acknowledge`, {}, {
        'X-Confirm-Duplication-Risk': 'true',
      });
      await refresh(owner);
      if (!actionMounted.current || actionOwner.current !== owner) return;
      setConfirmRisk(false);
      setNotice('O bloqueio foi liberado após a confirmação de risco. Nenhum envio foi repetido.');
    } catch (cause) { if (actionMounted.current && actionOwner.current === owner) setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível registrar a confirmação de risco.'); }
    finally { actionLatch.current = false; if (actionMounted.current && actionOwner.current === owner) setBusy(false); }
  }
  return <section className="cartao grade" aria-label="Recuperação do envio comum">
    <strong>O resultado do envio comum ainda não está confirmado. Consulte o estado antes de responder.</strong>
    {admission.dispatchDeadlineAt && <span>Confirmação de risco disponível após {new Date(admission.dispatchDeadlineAt).toLocaleString('pt-BR')}.</span>}
    {error && <span role="alert" className="erro">{error}</span>}
    {notice && <span role="status">{notice}</span>}
    <button type="button" onClick={() => void reconcile()} disabled={busy}>Consultar estado</button>
    <label><input type="checkbox" checked={confirmRisk} onChange={(event) => setConfirmRisk(event.target.checked)} />Confirmo o risco de mensagem duplicada.</label>
    <button type="button" onClick={() => void acknowledge()} disabled={busy || !confirmRisk || now < eligibleAt}>Reconhecer risco sem reenviar</button>
  </section>;
}

```

### web-app/src/telas/Inbox.tsx

SHA256 `bbd6facb3f60fafb01f661ec5fe6c0dec826b3023c9ba5ad44aec5b31865ddbd`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { FormEvent, useCallback, useEffect, useRef, useState } from 'react';
import { BusinessUnit, Conversa, ErroDaApi, Eu, Mensagem, Thread, api, ignorarSessaoMorta } from '../api';
import { ouvirTempoReal } from '../tempoReal';
import { cruzouPiso, mesclarMensagens } from '../timeline';
import { NovaConversa, OrdinaryRecovery, PrimeiraMensagem, type StartOptions } from '../componentes/NovaConversa';

const ABAS = [
  { id: 'QUEUED', rotulo: 'Na fila' },
  { id: 'IN_SERVICE', rotulo: 'Em atendimento' },
  { id: 'CLOSED', rotulo: 'Finalizadas' },
  { id: 'GRUPO', rotulo: 'Grupos' },
];

function explicarMotivoEnvio(motivo: string | null): string {
  switch (motivo) {
    case 'CANAL_AUSENTE': return 'Não há um canal conectado para responder.';
    case 'CANAL_AMBIGUO': return 'Esta conversa ainda não tem um canal definido. Aguarde uma mensagem recebida para responder.';
    case 'CANAL_SELECIONADO_INDISPONIVEL': return 'O canal desta conversa não está disponível.';
    case 'CHANNEL_IDENTITY_NOT_VERIFIED': return 'A identidade do canal ainda precisa ser verificada.';
    case 'CHANNEL_NOT_READY': return 'O canal ainda não está pronto para enviar.';
    case 'PENDING_CREDENTIAL': return 'A credencial do canal precisa ser atualizada.';
    case 'JANELA_FECHADA': return 'A janela de 24 horas foi encerrada.';
    default: return 'O envio está temporariamente indisponível.';
  }
}

interface Recuperacao {
  id: string;
  geracao: number;
  piso: string;
  cursor: string | null;
  dirty: boolean;
  eventos: number;
  emVoo: boolean;
  paginasRestantes: number;
  vazio?: boolean;
}

interface InvalidacaoDeAbertura {
  id: string;
  geracao: number;
  eventos: number;
}

interface ErroDeRecuperacao {
  geracao: number;
  versao: number;
}

export default function Inbox({ eu }: { eu: Eu }) {
  const [bus, setBus] = useState<BusinessUnit[]>([]);
  const [buId, setBuId] = useState<string>('');
  const [aba, setAba] = useState('QUEUED');
  const [conversas, setConversas] = useState<Conversa[]>([]);
  const [aberta, setAberta] = useState<Thread | null>(null);
  const [abrindo, setAbrindo] = useState(false);
  const [texto, setTexto] = useState('');
  const [erro, setErro] = useState<string | null>(null);
  const [carregandoAnteriores, setCarregandoAnteriores] = useState(false);
  const [recuperacaoPendente, setRecuperacaoPendente] = useState(false);
  const [enviando, setEnviando] = useState(false);
  const [novaConversa, setNovaConversa] = useState(false);
  const [startOptions, setStartOptions] = useState<StartOptions | null>(null);
  const [startOptionsFor, setStartOptionsFor] = useState<string | null>(null);
  const [startOptionsError, setStartOptionsError] = useState<string | null>(null);
  const [manualInitialConversationId, setManualInitialConversationId] = useState<string | null>(null);
  const textoRef = useRef('');
  const versaoErro = useRef(0);
  const erroRecuperacao = useRef<ErroDeRecuperacao | null>(null);
  const geracao = useRef(0);
  const buAtual = useRef('');
  const conversaAtual = useRef<string | null>(null);
  const abaAtual = useRef('QUEUED');
  const threadAtual = useRef<Thread | null>(null);
  const recuperacao = useRef<Recuperacao | null>(null);
  const invalidacaoAbertura = useRef<InvalidacaoDeAbertura | null>(null);
  const executarRecuperacaoRef = useRef<() => Promise<void>>(async () => {});
  const versaoMetadados = useRef(0);
  const bolhas = useRef<HTMLDivElement>(null);
  const carregarListaRef = useRef<(id?: string, filtro?: string) => Promise<void>>(async () => {});
  const reconciliarRef = useRef<() => void>(() => {});

  const guardarThread = (thread: Thread | null) => {
    threadAtual.current = thread;
    setAberta(thread);
  };

  const guardarTexto = (valor: string) => {
    textoRef.current = valor;
    setTexto(valor);
  };

  const definirErro = useCallback((mensagem: string | null, geracaoDaRecuperacao?: number) => {
    versaoErro.current += 1;
    erroRecuperacao.current = mensagem !== null && geracaoDaRecuperacao !== undefined
      ? { geracao: geracaoDaRecuperacao, versao: versaoErro.current }
      : null;
    setErro(mensagem);
  }, []);

  const limparErroRecuperacao = useCallback((geracaoDaRecuperacao: number) => {
    const erroAtual = erroRecuperacao.current;
    if (erroAtual?.geracao !== geracaoDaRecuperacao || erroAtual.versao !== versaoErro.current) return;
    erroRecuperacao.current = null;
    versaoErro.current += 1;
    setErro(null);
  }, []);

  useEffect(() => {
    api.get<{ businessUnits: BusinessUnit[] }>('/business-units').then((r) => {
      const lista = r.businessUnits ?? [];
      setBus(lista);
      const inicial = lista[0]?.id ?? '';
      buAtual.current = inicial;
      setBuId(inicial);
    }).catch(ignorarSessaoMorta);
  }, []);

  const carregarLista = useCallback(async (id = buAtual.current, filtro = aba) => {
    if (!id) return;
    try {
      const r = await api.get<{ conversations: Conversa[] }>(`/business-units/${id}/conversations?aba=${filtro}`);
      if (buAtual.current === id && abaAtual.current === filtro) setConversas(r.conversations);
    } catch (e) {
      if (buAtual.current === id && abaAtual.current === filtro) throw e;
    }
  }, [aba]);

  const aplicarPaginaRecente = useCallback((id: string, geracaoDaChamada: number, versao: number, response: Thread) => {
    if (conversaAtual.current !== id || geracao.current !== geracaoDaChamada) return;
    const anterior = threadAtual.current;
    const novo: Thread = {
      ...response,
      messages: mesclarMensagens(anterior?.messages ?? [], response.messages),
      // O cursor de reconciliação recente não substitui o cursor do histórico.
      paginacao: anterior && anterior.messages.length > 0 ? anterior.paginacao : response.paginacao,
      conversa: versaoMetadados.current === versao ? response.conversa : anterior?.conversa ?? response.conversa,
      janela: versaoMetadados.current === versao ? response.janela : anterior?.janela ?? response.janela,
    };
    guardarThread(novo);
  }, []);

  const executarRecuperacao = useCallback(async () => {
    const r = recuperacao.current;
    if (!r || r.emVoo || r.paginasRestantes <= 0 || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
    r.emVoo = true;
    const eventosNoInicio = r.eventos;
    r.dirty = false;
    let cruzou = false;
    try {
      if (r.vazio) {
        if (r.cursor === null && r.paginasRestantes > 0) {
          const versao = versaoMetadados.current;
          r.paginasRestantes -= 1;
          const inicial = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          aplicarPaginaRecente(r.id, r.geracao, versao, inicial);
          r.cursor = inicial.paginacao.cursorAnterior;
          if (!inicial.paginacao.temAnteriores) r.cursor = null;
        }
        while (r.cursor && r.paginasRestantes > 0 && !r.dirty) {
          const cursor = r.cursor;
          r.paginasRestantes -= 1;
          const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          const atual = threadAtual.current;
          if (atual) guardarThread({
            ...atual,
            messages: mesclarMensagens(atual.messages, pagina.messages),
            paginacao: pagina.paginacao,
          });
          r.cursor = pagina.paginacao.cursorAnterior;
        }
        if (r.eventos !== eventosNoInicio || r.dirty) {
          r.cursor = null;
          setRecuperacaoPendente(true);
        } else if (!r.cursor) {
          recuperacao.current = null;
          setRecuperacaoPendente(false);
          limparErroRecuperacao(r.geracao);
        } else {
          setRecuperacaoPendente(true);
        }
        return;
      }
      if (r.cursor === null && r.paginasRestantes > 0) {
        const versao = versaoMetadados.current;
        r.paginasRestantes -= 1;
        const recente = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        aplicarPaginaRecente(r.id, r.geracao, versao, recente);
        r.cursor = recente.paginacao.cursorAnterior;
        cruzou = cruzouPiso(recente.messages, r.piso) || !recente.paginacao.temAnteriores;
      }
      while (!cruzou && r.cursor && r.paginasRestantes > 0 && !r.dirty) {
        const cursor = r.cursor;
        r.paginasRestantes -= 1;
        const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        const atual = threadAtual.current;
        if (atual) guardarThread({
          ...atual,
          messages: mesclarMensagens(atual.messages, pagina.messages),
        });
        r.cursor = pagina.paginacao.cursorAnterior;
        cruzou = cruzouPiso(pagina.messages, r.piso) || !pagina.paginacao.temAnteriores;
      }

      if (r.eventos !== eventosNoInicio || r.dirty) {
        // Um evento concorrente exige nova passagem recente e preserva o piso.
        r.cursor = null;
        setRecuperacaoPendente(true);
      } else if (cruzou) {
        recuperacao.current = null;
        setRecuperacaoPendente(false);
        limparErroRecuperacao(r.geracao);
      } else {
        setRecuperacaoPendente(true);
      }
    } catch (e) {
      if (r.geracao === geracao.current && r.id === conversaAtual.current) {
        if (r.dirty || r.eventos !== eventosNoInicio) r.cursor = null;
        definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível atualizar o histórico. Tente novamente.', r.geracao);
        setRecuperacaoPendente(true);
      }
    } finally {
      r.emVoo = false;
      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.paginasRestantes > 0 && r.geracao === geracao.current) {
        queueMicrotask(() => void executarRecuperacaoRef.current());
      }
    }
  }, [aplicarPaginaRecente, definirErro, limparErroRecuperacao]);

  useEffect(() => { executarRecuperacaoRef.current = executarRecuperacao; }, [executarRecuperacao]);

  const reconciliar = useCallback(() => {
    const thread = threadAtual.current;
    const id = conversaAtual.current;
    if (!id) return;
    if (!thread) {
      const abertura = invalidacaoAbertura.current;
      if (abertura?.id === id && abertura.geracao === geracao.current) abertura.eventos += 1;
      return;
    }
    let r = recuperacao.current;
    if (!r || r.id !== id || r.geracao !== geracao.current) {
      const mensagens = thread.messages;
      if (mensagens.length === 0) {
        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3, vazio: true };
        recuperacao.current = r;
        void executarRecuperacao();
        return;
      }
      const piso = mensagens.reduce((max, m) => Date.parse(m.createdAt) > Date.parse(max) ? m.createdAt : max, mensagens[0].createdAt);
      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3 };
      recuperacao.current = r;
      setRecuperacaoPendente(true);
    } else {
      r.dirty = true;
      r.eventos += 1;
      if (!r.emVoo) r.cursor = null;
      setRecuperacaoPendente(true);
    }
    if (r.paginasRestantes > 0) void executarRecuperacao();
  }, [aplicarPaginaRecente, executarRecuperacao]);

  const iniciarRodadaAutorizada = useCallback(() => {
    const r = recuperacao.current;
    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
    r.paginasRestantes = 3;
    void executarRecuperacao();
  }, [executarRecuperacao]);

  useEffect(() => {
    carregarListaRef.current = carregarLista;
    reconciliarRef.current = reconciliar;
  }, [carregarLista, reconciliar]);

  useEffect(() => {
    const id = aberta?.conversa.id;
    if (!id) {
      setStartOptions(null);
      setStartOptionsFor(null);
      setStartOptionsError(null);
      return;
    }
    let current = true;
    const generationAtStart = geracao.current;
    setStartOptions(null);
    setStartOptionsFor(null);
    setStartOptionsError(null);
    api.get<StartOptions>(`/conversations/${id}/start-options`).then((result) => {
      if (!current || generationAtStart !== geracao.current || id !== conversaAtual.current || buId !== buAtual.current) return;
      setStartOptions(result);
      setStartOptionsFor(id);
    }).catch((cause) => {
      if (!current || generationAtStart !== geracao.current || id !== conversaAtual.current) return;
      setStartOptionsError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível conferir as opções de envio.');
      setStartOptionsFor(id);
    });
    return () => { current = false; };
  }, [aberta?.conversa.id, buId]);

  useEffect(() => {
    void carregarLista().catch(ignorarSessaoMorta);
    const t = setInterval(() => {
      void carregarLista().catch(ignorarSessaoMorta);
      if (recuperacao.current) iniciarRodadaAutorizada();
      else reconciliar();
    }, 60_000);
    return () => clearInterval(t);
  }, [buId, aba, carregarLista, reconciliar, iniciarRodadaAutorizada]);

  useEffect(() => {
    // Espera a lista inicial de BUs e mantém o socket apesar de filtros, BUs ou
    // callbacks locais mudarem. Isso evita reconectar durante o mesmo login.
    if (bus.length === 0) return;
    const parar = ouvirTempoReal((evento) => {
      if (evento.buId !== buAtual.current) return;
      void carregarListaRef.current().catch(ignorarSessaoMorta);
      if (evento.conversaId === conversaAtual.current) reconciliarRef.current();
    }, () => reconciliarRef.current());
    return parar;
  }, [eu.id, bus.length]);

  function trocarBu(novoBu: string) {
    geracao.current += 1;
    buAtual.current = novoBu;
    conversaAtual.current = null;
    recuperacao.current = null;
    invalidacaoAbertura.current = null;
    guardarThread(null);
    setAbrindo(false);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    definirErro(null);
    setRecuperacaoPendente(false);
    setConversas([]);
    setStartOptions(null);
    setStartOptionsFor(null);
    setStartOptionsError(null);
    setManualInitialConversationId(null);
    setBuId(novoBu);
  }

  async function abrir(id: string, marcarLida = true) {
    const gen = ++geracao.current;
    conversaAtual.current = id;
    recuperacao.current = null;
    invalidacaoAbertura.current = { id, geracao: gen, eventos: 0 };
    versaoMetadados.current += 1;
    guardarThread(null);
    setAbrindo(true);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    definirErro(null);
    setRecuperacaoPendente(false);
    try {
      const response = await api.get<Thread>(`/conversations/${id}/messages?marcarLida=${marcarLida}`);
      if (gen !== geracao.current || conversaAtual.current !== id) return;
      response.messages = mesclarMensagens(response.messages);
      guardarThread(response);
      setAbrindo(false);
      const invalidacao = invalidacaoAbertura.current;
      invalidacaoAbertura.current = null;
      void carregarLista().catch(ignorarSessaoMorta);
      if (invalidacao?.id === id && invalidacao.geracao === gen && invalidacao.eventos > 0) reconciliar();
    } catch (e) {
      if (gen === geracao.current) {
        invalidacaoAbertura.current = null;
        guardarThread(null);
        setAbrindo(false);
        definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível carregar a conversa.');
      }
    }
  }

  async function carregarAnteriores() {
    const atual = threadAtual.current;
    const id = conversaAtual.current;
    const cursor = atual?.paginacao.cursorAnterior;
    if (!atual || !id || !cursor || carregandoAnteriores) return;
    const gen = geracao.current;
    setCarregandoAnteriores(true);
    definirErro(null);
    try {
      const pagina = await api.get<Thread>(`/conversations/${id}/messages?antes=${encodeURIComponent(cursor)}`);
      if (gen !== geracao.current || id !== conversaAtual.current || !threadAtual.current) return;
      // Inclua alterações legítimas que chegaram enquanto a página estava no ar.
      const alturaAntes = bolhas.current?.scrollHeight ?? 0;
      const topoAntes = bolhas.current?.scrollTop ?? 0;
      const corrente = threadAtual.current;
      guardarThread({ ...corrente, messages: mesclarMensagens(corrente.messages, pagina.messages), paginacao: pagina.paginacao });
      requestAnimationFrame(() => {
        if (gen === geracao.current && bolhas.current) bolhas.current.scrollTop = topoAntes + (bolhas.current.scrollHeight - alturaAntes);
      });
    } catch (e) {
      if (gen === geracao.current) definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Falha ao carregar mensagens anteriores.');
    } finally {
      if (gen === geracao.current) setCarregandoAnteriores(false);
    }
  }

  async function agir(acao: () => Promise<unknown>) {
    const id = conversaAtual.current;
    const gen = geracao.current;
    if (!id) return;
    versaoMetadados.current += 1;
    definirErro(null);
    try {
      await acao();
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) definirErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
    }
  }

  async function responder(e: FormEvent) {
    e.preventDefault();
    const id = conversaAtual.current;
    const gen = geracao.current;
    const textoEnviado = textoRef.current;
    if (!id || !textoEnviado.trim() || enviando) return;
    setEnviando(true);
    definirErro(null);
    try {
      await api.post(`/conversations/${id}/messages`, { texto: textoEnviado });
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      if (textoRef.current === textoEnviado) guardarTexto('');
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) definirErro(e instanceof ErroDaApi ? e.message : 'Falha ao enviar mensagem.');
    } finally {
      if (gen === geracao.current) setEnviando(false);
    }
  }

  const envioIndisponivel = aberta ? !aberta.janela.disponivel : false;
  const janelaFechada = aberta?.janela.exigida && !aberta.janela.aberta;
  const currentStartOptions = aberta && startOptionsFor === aberta.conversa.id ? startOptions : null;
  const ordinaryUncertainAdmission = currentStartOptions?.ordinaryAdmissions.find((item) => ['SENDING', 'UNCERTAIN'].includes(item.state)) ?? null;
  const activeOrdinaryAdmission = Boolean(ordinaryUncertainAdmission);
  const requiresInitialFlow = Boolean(aberta && (aberta.messages.length === 0 || currentStartOptions?.activeAttempt || activeOrdinaryAdmission || manualInitialConversationId === aberta.conversa.id));
  const startOptionsLoading = Boolean(aberta && startOptionsFor !== aberta.conversa.id);

  return (
    <div className="grade">
      <div className="linha">
        <select aria-label="Business Unit" value={buId} onChange={(e) => trocarBu(e.target.value)} style={{ maxWidth: 280 }}>
          {bus.map((b) => <option key={b.id} value={b.id}>{b.name}</option>)}
        </select>
        <button type="button" onClick={() => setNovaConversa(true)} disabled={!buId}>Nova conversa</button>
        {erro && <span className="erro" role="alert">{erro}</span>}
      </div>

      {novaConversa && <NovaConversa buId={buId} onClose={() => setNovaConversa(false)} onOpened={(result) => {
        setNovaConversa(false);
        setManualInitialConversationId(result.conversaId);
        void carregarLista().catch(ignorarSessaoMorta);
        void abrir(result.conversaId, false);
      }} />}

      <div className="abas">
        {ABAS.map((a) => <button key={a.id} className={aba === a.id ? 'ativa' : ''} onClick={() => { abaAtual.current = a.id; setAba(a.id); }}>{a.rotulo}</button>)}
      </div>

      <div className="inbox">
        <div className="cartao lista" style={{ padding: 0 }}>
          {conversas.map((c) => <button key={c.id} className={`item ${aberta?.conversa.id === c.id ? 'ativo' : ''}`} onClick={() => { setManualInitialConversationId(null); void abrir(c.id); }}>
            <div className="linha"><strong>{c.displayName ?? c.contact}</strong>{c.unreadCount > 0 && <span className="suave">({c.unreadCount})</span>}</div>
            <div className="suave">{c.attendantName ?? 'sem atendente'}</div>
          </button>)}
          {conversas.length === 0 && <p className="suave" style={{ padding: 12 }}>Nada aqui.</p>}
        </div>

        <div className="cartao grade">
          {!aberta && (abrindo
            ? <p className="suave" role="status" aria-live="polite">Abrindo conversa…</p>
            : <p className="suave">Escolha uma conversa.</p>)}
          {aberta && <>
            <div className="linha">
              <strong>{aberta.conversa.nome ?? aberta.conversa.contato}</strong>
              <span className="suave">{aberta.conversa.status}</span>
              <span className="suave" style={{ marginLeft: 'auto' }}>{aberta.janela.canal}</span>
            </div>
            <div className="linha">
              {aberta.paginacao.temAnteriores
                ? <button onClick={() => void carregarAnteriores()} disabled={carregandoAnteriores} aria-label="Carregar mensagens anteriores">
                    {carregandoAnteriores ? 'Carregando…' : 'Carregar anteriores'}
                  </button>
                : <span className="suave">Início do histórico</span>}
              {recuperacaoPendente && <span className="suave" role="status">Atualização pendente. O histórico pode ter uma lacuna.</span>}
              {recuperacaoPendente && <button onClick={() => iniciarRodadaAutorizada()}>Continuar atualização</button>}
            </div>
            <div className="bolhas" ref={bolhas} aria-live="polite">
              {aberta.messages.map((m: Mensagem) => <div key={m.id} data-message-id={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>
                <div>{m.content}</div>
                <div className="suave">{new Date(m.createdAt).toLocaleString('pt-BR')}{m.authorName ? ` · ${m.authorName}` : ''}</div>
              </div>)}
              {aberta.messages.length === 0 && <p className="suave">Nenhuma mensagem nesta conversa.</p>}
            </div>

            {envioIndisponivel && <div className="aviso" role="status">{janelaFechada
              ? 'Fora da janela de 24h do canal selecionado. Texto livre está indisponível.'
              : explicarMotivoEnvio(aberta.janela.motivo)}</div>}
            {requiresInitialFlow
              ? startOptionsLoading
                ? <p className="suave" role="status">Conferindo opções do primeiro envio…</p>
                : currentStartOptions
                  ? ordinaryUncertainAdmission && !currentStartOptions.activeAttempt
                    ? <OrdinaryRecovery conversationId={aberta.conversa.id} admission={ordinaryUncertainAdmission} onOptions={setStartOptions} />
                    : <PrimeiraMensagem key={`${eu.id}:${buId}:${aberta.conversa.id}`} actorId={eu.id} buId={buId} conversationId={aberta.conversa.id}
                      options={currentStartOptions} onOptions={setStartOptions} onComplete={() => {
                        setManualInitialConversationId(null);
                        void abrir(aberta.conversa.id, false);
                      }} onCancel={aberta.messages.length > 0 ? () => setManualInitialConversationId(null) : undefined} />
                  : <span role="alert" className="erro">{startOptionsError ?? 'Não foi possível conferir se existe uma operação ativa.'}</span>
              : startOptionsLoading
                ? <p className="suave" role="status">Conferindo se há um envio inicial pendente…</p>
                : <form className="linha" onSubmit={responder}>
                    <input value={texto} onChange={(e) => guardarTexto(e.target.value)} placeholder={envioIndisponivel ? 'Envio indisponível' : 'Escreva uma resposta'} disabled={envioIndisponivel || !currentStartOptions || Boolean(currentStartOptions.activeAttempt) || activeOrdinaryAdmission} maxLength={4096} />
                    <button className="primario" disabled={envioIndisponivel || enviando || !texto.trim() || !currentStartOptions || Boolean(currentStartOptions.activeAttempt) || activeOrdinaryAdmission}>{enviando ? 'Enviando…' : 'Enviar'}</button>
                  </form>}
            {startOptionsError && !requiresInitialFlow && <span role="status" className="suave">{startOptionsError}</span>}
            {aberta.conversa.status !== 'CLOSED' && <div className="linha">
              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/claim`))}>Atender</button>
              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/close`))}>Finalizar</button>
            </div>}
          </>}
        </div>
      </div>
    </div>
  );
}

```

### web-app/src/api.ts

SHA256 `7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
/**
 * Cliente do BFF.
 *
 * O front é serviço próprio, num SUBDOMÍNIO do mesmo domínio da API (ADR-0015).
 * Isso é origem diferente e **mesmo site** — então:
 *  - `credentials: 'include'` manda o cookie `HttpOnly` para a API;
 *  - o cookie continua `SameSite=Lax`, porque subdomínio é o mesmo site;
 *  - `X-Requested-With` é exigido pelo servidor no que muda estado (CSRF).
 *
 * A base da API vem de `/config.js`, escrito pelo container no START — não do
 * build (ver `config.ts`). Vazio = mesma origem.
 */
import { API_BASE as BASE } from './config';
/** Evento disparado quando qualquer chamada volta 401. */
export const SESSAO_MORTA = 'leadshug:sessao-morta';

/**
 * A conta ainda não terminou o wizard (409 ONBOARDING_PENDENTE), ou um módulo
 * foi desligado com a aba aberta (404 MODULO_DESLIGADO).
 *
 * Nos dois casos o estado da tela está VELHO, não errado: o app rebusca o /me e
 * se remonta, em vez de mostrar erro. É o mesmo padrão do SESSAO_MORTA.
 */
export const PRODUTO_MUDOU = 'leadshug:produto-mudou';

/**
 * `typeof window` porque este módulo também é exercitado fora do navegador —
 * é o teste de unidade que prova isso. Estourar aqui trocaria o erro REAL da
 * chamada por um "window is not defined", que aponta para o lugar errado.
 */
function avisar(evento: string): void {
  if (typeof window !== 'undefined') window.dispatchEvent(new CustomEvent(evento));
}

export class ErroDaApi extends Error {
  constructor(
    readonly status: number,
    readonly codigo: string | undefined,
    mensagem: string,
    readonly outcome?: string,
    readonly evidence?: string,
    readonly localMessageState?: string,
    readonly diagnosticPersistence?: string,
    readonly operationId?: string,
    readonly phase?: string,
    readonly providerAcceptance?: string,
    readonly receiptPersistence?: string,
    readonly acceptanceProvenance?: string,
    readonly recoveryAction?: string,
    readonly attemptId?: string,
    readonly state?: string,
    readonly eligibleAt?: string,
    readonly preAdmission?: boolean,
  ) {
    super(mensagem);
  }
}

async function chamar<T>(caminho: string, init: RequestInit = {}): Promise<T> {
  const mudaEstado = Boolean(init.method && init.method !== 'GET');
  const res = await fetch(`${BASE}/api/bff${caminho}`, {
    ...init,
    credentials: 'include',
    headers: {
      'content-type': 'application/json',
      ...(mudaEstado ? { 'x-requested-with': 'leadshug-web' } : {}),
      ...(init.headers ?? {}),
    },
  });

  if (res.status === 204) return undefined as T;

  // Resposta que NÃO é JSON é falha de configuração, não corpo vazio.
  //
  // O caso real: sem `LEADSHUG_API_URL`, a base fica vazia e o front chama a
  // PRÓPRIA origem — onde o nginx serve o index.html para qualquer caminho. A
  // resposta vem 200, com HTML. Engolir isso como `{}` fazia a tela quebrar três
  // passos depois, num campo que não tem relação nenhuma com a causa
  // ("Cannot read properties of undefined"), e mandava quem depura para o lugar
  // errado. Falhar aqui, dizendo o que provavelmente está errado, é o mínimo.
  const bruto = await res.text();
  let corpo: Record<string, unknown>;
  try {
    corpo = bruto ? JSON.parse(bruto) : {};
  } catch {
    // 405 num POST é assinatura de SERVIDOR DE ARQUIVOS: nginx responde assim
    // quando recebe POST para um arquivo estático. Dizer isso poupa a rodada de
    // "confira se é mesmo a API" — o que responde não é uma API.
    const pareceEstatico = res.status === 405 || /^\s*<(!doctype|html)/i.test(bruto);

    throw new ErroDaApi(
      res.status,
      'RESPOSTA_NAO_E_JSON',
      !BASE
        ? 'A base da API está VAZIA: o front está chamando a própria origem. ' +
          'Configure LEADSHUG_API_URL no serviço web.'
        : pareceEstatico
          ? `${BASE} respondeu ${res.status} como um servidor de ARQUIVOS, não como a API ` +
            `(em ${caminho}). Esse endereço aponta para o serviço errado — confira ` +
            'LEADSHUG_API_URL e o domínio do serviço `api`.'
          : `A API respondeu ${res.status} com algo que não é JSON em ${caminho}. ` +
            `Confira se ${BASE} é mesmo a API.`,
    );
  }

  if (res.status === 401) {
    // A sessão morreu (expirou, a conta foi inativada, a senha foi resetada).
    // Quem descobre isso é qualquer chamada, então o aviso é central: a tela
    // que estava aberta não tem como saber o que fazer sozinha.
    avisar(SESSAO_MORTA);
  }
  // Estado VELHO, não erro: a conta não terminou o wizard, ou um módulo foi
  // desligado com esta aba aberta. O app rebusca o /me e se remonta.
  if (corpo.code === 'ONBOARDING_PENDENTE' || corpo.code === 'MODULO_DESLIGADO') {
    avisar(PRODUTO_MUDOU);
  }
  if (!res.ok) {
    // `error` é o campo das recusas do produto. Um 500 do Nest NÃO tem esse
    // campo — ele traz `message` —, e ignorá-lo transformava toda falha de
    // servidor em "Falha inesperada.", que não diz nem o status. O status entra
    // sempre: é o primeiro dado que quem depura precisa.
    const dito = corpo.error ?? corpo.message;
    throw new ErroDaApi(
      res.status,
      typeof corpo.code === 'string' ? corpo.code : undefined,
      dito ? `${dito} (HTTP ${res.status})` : `A API respondeu ${res.status} sem explicar o motivo.`,
      typeof corpo.outcome === 'string' ? corpo.outcome : undefined,
      typeof corpo.evidence === 'string' ? corpo.evidence : undefined,
      typeof corpo.localMessageState === 'string' ? corpo.localMessageState : undefined,
      typeof corpo.diagnosticPersistence === 'string' ? corpo.diagnosticPersistence : undefined,
      typeof corpo.operationId === 'string' ? corpo.operationId : undefined,
      typeof corpo.phase === 'string' ? corpo.phase : undefined,
      typeof corpo.providerAcceptance === 'string' ? corpo.providerAcceptance : undefined,
      typeof corpo.receiptPersistence === 'string' ? corpo.receiptPersistence : undefined,
      typeof corpo.acceptanceProvenance === 'string' ? corpo.acceptanceProvenance : undefined,
      typeof corpo.recoveryAction === 'string' ? corpo.recoveryAction : undefined,
      typeof corpo.attemptId === 'string' && /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(corpo.attemptId) ? corpo.attemptId : undefined,
      typeof corpo.state === 'string' && ['PREPARED', 'SENDING', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED', 'AMBIGUOUS', 'REJECTED'].includes(corpo.state) ? corpo.state : undefined,
      typeof corpo.eligibleAt === 'string' && corpo.eligibleAt.length <= 40 && Number.isFinite(Date.parse(corpo.eligibleAt)) ? corpo.eligibleAt : undefined,
      corpo.preAdmission === true ? true : undefined,
    );
  }
  return corpo as T;
}

/**
 * Trata a falha de uma chamada disparada e esquecida (carregamento de tela).
 *
 * 401 aqui é normal e não é problema da tela: a sessão morreu — no logout, por
 * expiração, ou porque a conta foi inativada — e quem redireciona é o App. Sem
 * este filtro, cada chamada em voo no momento do logout vira uma **rejeição não
 * tratada**, que o navegador registra como exceção da página. Foi assim que o
 * teste de navegador pegou o primeiro defeito real.
 */
export function ignorarSessaoMorta(e: unknown): void {
  if (e instanceof ErroDaApi && e.status === 401) return;
  // Tratados centralmente pelo App, que rebusca o /me e remonta. Deixá-los
  // chegar ao console faria a tela reclamar de algo que já está sendo resolvido.
  if (e instanceof ErroDaApi && (e.codigo === 'ONBOARDING_PENDENTE' || e.codigo === 'MODULO_DESLIGADO')) return;
  console.error(e);
}

export const api = {
  get: <T>(c: string) => chamar<T>(c),
  post: <T>(c: string, corpo?: unknown) =>
    chamar<T>(c, { method: 'POST', body: corpo ? JSON.stringify(corpo) : undefined }),
  postWithHeaders: <T>(c: string, corpo: unknown, headers: Record<string, string>) =>
    chamar<T>(c, { method: 'POST', body: JSON.stringify(corpo), headers }),
  patch: <T>(c: string, corpo?: unknown) =>
    chamar<T>(c, { method: 'PATCH', body: corpo ? JSON.stringify(corpo) : undefined }),
  put: <T>(c: string, corpo?: unknown) =>
    chamar<T>(c, { method: 'PUT', body: corpo ? JSON.stringify(corpo) : undefined }),
  del: <T>(c: string) => chamar<T>(c, { method: 'DELETE' }),

  /**
   * Envia um arquivo (ADR-0024). Sem `content-type`: o navegador precisa montar
   * o `boundary` do multipart sozinho, e declará-lo à mão quebra o parse no
   * servidor de um jeito que não diz o que houve.
   */
  async enviarArquivo(arquivo: File): Promise<{ id: string; tipo: string }> {
    const corpo = new FormData();
    corpo.append('arquivo', arquivo);
    const res = await fetch(`${BASE}/api/bff/arquivos`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'x-requested-with': 'leadshug-web' },
      body: corpo,
    });
    const bruto = await res.text();
    let json: Record<string, string> = {};
    try {
      json = bruto ? JSON.parse(bruto) : {};
    } catch {
      throw new ErroDaApi(res.status, 'RESPOSTA_NAO_E_JSON', 'A API respondeu algo que não é JSON.');
    }
    if (!res.ok) throw new ErroDaApi(res.status, json.code, json.error ?? 'Falha ao enviar o arquivo.');
    return json as unknown as { id: string; tipo: string };
  },
};

/** O endereço de leitura de um arquivo guardado — passa pela sessão. */
export function urlDoArquivo(id: string | null | undefined): string | null {
  return id ? `${BASE}/api/bff/arquivos/${id}` : null;
}

export interface Produto {
  /** JÁ interseccionado no servidor (env ∩ Mantenedora) — aqui não se faz conta. */
  modulos: { canalNaoOficial: boolean };
  marca: { nome: string | null; cor: string | null; corClaro: string | null; corEscuro: string | null; corSecundaria: string | null; tema: string; logo: string | null };
  /** O wizard ainda não terminou: o app monta o wizard, não o produto. */
  onboardingPendente: boolean;
}

export interface Eu {
  id: string;
  nome: string;
  email: string;
  precisaTrocarSenha: boolean;
  papel: string | null;
  mantenedora: { id: string; name: string } | null;
  escopo: string[];
  produto: Produto;
  telefone: string | null;
  avatar: string | null;
}

export interface BusinessUnit {
  id: string;
  name: string;
  phone: string | null;
  papel?: string | null;
  setor?: { id: string; name: string } | null;
  channels: {
    id: string;
    type: string;
    status: string;
    generation?: number;
    currentAttemptId?: string | null;
    ownNumberVerified?: boolean;
    providerConnectionState?: string | null;
    receiptVerifiedAt?: string | null;
    requiresWindow?: boolean;
    connectedAt?: string | null;
  }[];
}

export interface TemplateDefinition {
  name: string;
  language: 'pt_BR';
  category: 'MARKETING' | 'UTILITY';
  body: string;
  header?: string;
  footer?: string;
  examples: Record<string, string>;
}

export interface TemplateReceipt {
  id: string;
  sequence: number;
  phase: string;
  safeCode: string | null;
  remoteTemplateId: string | null;
  acceptanceProvenance?: string | null;
  createdAt: string;
}

export interface TemplateOperation {
  id: string;
  phase: string;
  revision: number;
  providerAcceptance: 'CONFIRMED' | 'UNKNOWN';
  acceptanceProvenance?: 'ACKNOWLEDGED' | 'CORRELATED_BY_DEFINITION' | null;
  receiptPersistence: 'RECORDED' | 'UNCONFIRMED';
  safeCode?: string | null;
  remoteTemplateId: string | null;
  updatedAt: string;
  leaseExpiresAt: string | null;
  recoveryAction: 'WAIT' | 'RECONCILE' | null;
  savedObservation?: TemplateSummary | null;
  receipts?: TemplateReceipt[];
}

export interface TemplateDraft {
  id: string;
  mantenedoraId: string;
  buId: string;
  creatorUserId: string;
  channelId: string;
  revision: number;
  state: 'DRAFT' | 'LOCKED';
  definition: TemplateDefinition;
  definitionFingerprint?: string;
  savedObservation?: TemplateSummary | null;
  currentOperation?: TemplateOperation | null;
  recentOperations?: TemplateOperation[];
}

export interface TemplatePreview {
  definition: TemplateDefinition;
  renderedText: string;
  requestFingerprint: string;
  persistence: 'PERSISTED' | 'UNPERSISTED';
}

export interface TemplateSummary {
  remoteTemplateId: string;
  status: string;
  name: string | null;
  language: string | null;
  category: string;
  parameterFormat: string;
  components: unknown[];
  supported: boolean;
  semanticFingerprint: string | null;
  available: boolean;
  safeCode?: string;
  observedAt: string;
  observedFence: string;
  eligible: boolean;
  matchesDefinition?: boolean;
  eligibleForUse?: boolean;
}

export interface TemplateCatalogPage {
  items: TemplateSummary[];
  nextCursor: string | null;
  available: boolean;
  safeCode?: string;
  observedAt: string | null;
}
export interface TemplateRefreshInProgress { phase: 'REFRESH_IN_PROGRESS'; retryAfter: number }

export interface TemplateCapabilities {
  available: boolean;
  expectedGeneration: number;
  explanation: string | null;
}

export const templateApi = {
  capabilities: (buId: string, channelId: string) =>
    api.get<TemplateCapabilities>(`/business-units/${buId}/channels/${channelId}/message-template-capabilities`),
  listDrafts: (buId: string, view: 'mine' | 'bu' = 'mine', page = 1, limit = 20) =>
    api.get<{ items: TemplateDraft[]; page: number; limit: number; total: number; hasMore: boolean }>(
      `/business-units/${buId}/message-templates?view=${view}&page=${page}&limit=${limit}`),
  preview: (buId: string, input: { channelId: string; expectedGeneration: number; draftId?: string; expectedRevision?: number; definition: TemplateDefinition }) =>
    api.post<TemplatePreview>(`/business-units/${buId}/message-templates/preview`, input),
  createDraft: (buId: string, input: { clientRequestId: string; channelId: string; expectedGeneration: number } & TemplateDefinition) =>
    api.post<TemplateDraft & { replayed?: boolean }>(`/business-units/${buId}/message-templates`, input),
  getDraft: (draftId: string) => api.get<TemplateDraft>(`/message-templates/${draftId}`),
  saveDraft: (draftId: string, expectedRevision: number, definition: TemplateDefinition) =>
    api.patch<TemplateDraft>(`/message-templates/${draftId}`, { expectedRevision, definition }),
  submit: (draftId: string, idempotencyKey: string, input: { expectedRevision: number; expectedGeneration: number; expectedDefinitionFingerprint: string }) =>
    api.postWithHeaders<TemplateOperation & { replayed?: boolean; recoveryInProgress?: boolean }>(
      `/message-templates/${draftId}/submit`, input, { 'idempotency-key': idempotencyKey }),
  operation: (draftId: string, operationId: string) =>
    api.get<TemplateOperation>(`/message-templates/${draftId}/operations/${operationId}`),
  reconcile: (draftId: string, operationId: string) =>
    api.post<TemplateOperation & { recoveryInProgress?: boolean }>(`/message-templates/${draftId}/operations/${operationId}/reconcile`, {}),
  refreshDraft: (draftId: string) => api.post<(TemplateSummary & { matchesDefinition?: boolean; eligibleForUse?: boolean }) | TemplateRefreshInProgress>(`/message-templates/${draftId}/refresh`, {}),
  catalog: (buId: string, channelId: string, after: string | null = null) =>
    api.get<TemplateCatalogPage>(`/business-units/${buId}/channels/${channelId}/message-template-catalog${after ? `?after=${encodeURIComponent(after)}` : ''}`),
  refreshCatalog: (buId: string, channelId: string, after: string | null = null) =>
    api.post<TemplateCatalogPage | TemplateRefreshInProgress>(`/business-units/${buId}/channels/${channelId}/message-template-catalog`, after ? { after } : {}),
};

export interface Setor {
  id: string;
  nome: string;
  status: 'ATIVO' | 'INATIVO';
  numeros: number;
}

export interface Atividade {
  id: string;
  categoria: string;
  entidade: string;
  ator: string | null;
  texto: string;
  de: string | null;
  para: string | null;
  em: string;
}

export interface Conversa {
  id: string;
  contact: string;
  displayName: string | null;
  status: string;
  attendantName: string | null;
  unreadCount: number;
  lastMessageAt: string | null;
}

export interface Mensagem {
  id: string;
  direction: 'IN' | 'OUT';
  content: string | null;
  channelOrigin: string;
  authorName: string | null;
  createdAt: string;
}

export interface Thread {
  conversa: { id: string; contato: string; nome: string | null; status: string; atendente: string | null };
  janela: { exigida: boolean; aberta: boolean; expiraEm: string | null; canal: string | null; disponivel: boolean; motivo: string | null };
  messages: Mensagem[];
  paginacao: { limite: number; temAnteriores: boolean; cursorAnterior: string | null };
}

```

### api-app/test/initial-message.e2e-spec.ts

SHA256 `a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { INestApplication } from '@nestjs/common';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import {
  contratarCanalNaoOficial,
  criarCanalVerificado,
  criarMantenedora,
  criarUsuario,
  evolutionFake,
  limparBanco,
  login,
  metaFake,
  subirApp,
  tetoComCanalNaoOficial,
} from './helpers';
import { renderInitialTemplate } from '../src/domain/inbox/initial-message-template-renderer';
import { SessionService } from '../src/infra/session/session.service';
import { MetaHttpClient } from '../src/integrations/meta/meta.client';
import { DispatchAdmissionService } from '../src/domain/inbox/dispatch-admission.service';
import { OutboundService } from '../src/domain/inbox/outbound.service';
import { randomUUID } from 'node:crypto';

type TransactionCall = (...args: unknown[]) => Promise<unknown>;
async function withTransactionFault<T>(prisma: PrismaService, mode: 'commit-ack-loss' | 'rollback', action: () => Promise<T>): Promise<T> {
  const target = prisma as unknown as { $transaction: TransactionCall };
  const original = target.$transaction.bind(prisma);
  let injected = false;
  target.$transaction = (...args: unknown[]) => {
    if (injected) return original(...args);
    injected = true;
    if (mode === 'rollback' && typeof args[0] === 'function') {
      const callback = args[0] as (tx: unknown) => Promise<unknown>;
      return original(async (tx: unknown) => {
        await callback(tx);
        throw new Error('synthetic ambiguity classification rollback');
      }, ...args.slice(1));
    }
    return original(...args).then(() => { throw new Error('synthetic ambiguity classification ACK loss'); });
  };
  try { return await action(); }
  finally { target.$transaction = original; }
}

async function waitForActorGrantShareLock(prisma: PrismaService): Promise<void> {
  for (let attempt = 0; attempt < 500; attempt += 1) {
    const rows = await prisma.$queryRaw<Array<{ waiting: boolean }>>`
      SELECT EXISTS (
        SELECT 1 FROM pg_stat_activity
        WHERE wait_event_type = 'Lock' AND query ILIKE '%FOR SHARE OF u, r, b%'
      ) AS waiting`;
    if (rows[0]?.waiting) return;
    await new Promise((resolve) => setTimeout(resolve, 10));
  }
  throw new Error('Timed out waiting for the current actor/grant share lock.');
}

describe('initial message BFF journey', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let businessUnitId: string;
  let mantenedoraId: string;
  let cookie: string;
  let channelId: string;
  let conversationId: string;
  let generation: number;
  const sqlQueries: Array<{ query: string; params: string }> = [];

  beforeAll(async () => {
    tetoComCanalNaoOficial();
    ({ app, prisma } = await subirApp(undefined, true));
    prisma.$on('query', (event) => { sqlQueries.push({ query: event.query, params: event.params }); });
    await app.listen(0, '127.0.0.1');
  });

  afterAll(async () => {
    await limparBanco(prisma);
    await app?.close();
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    sqlQueries.length = 0;
    const tenant = await criarMantenedora(app, 'Initial journey', 'initial-journey@leadshug.test');
    businessUnitId = tenant.businessUnit.id;
    mantenedoraId = tenant.mantenedora.id;
    await contratarCanalNaoOficial(prisma, tenant.mantenedora.id);
    const channel = await criarCanalVerificado(prisma, businessUnitId, 'NAO_OFICIAL', 'initial-journey-evolution', { requiresWindow: false });
    channelId = channel.channel.id;
    generation = channel.channel.generation;
    cookie = await login(app, 'initial-journey@leadshug.test');
    const opened = await request(app.getHttpServer())
      .post(`/api/bff/business-units/${businessUnitId}/conversations/open`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ telefone: '+55 (11) 98765-4321' }).expect(201);
    expect(opened.body).toMatchObject({ criada: true, contact: '5511987654321' });
    conversationId = opened.body.conversaId;
  });

  it('keeps PREPARED options and attempt reads observational while exposing local recovery, and interlocks ordinary sends', async () => {
    const base = `/api/bff/conversations/${conversationId}`;
    const emptyBefore = await prisma.message.count({ where: { conversationId } });
    await request(app.getHttpServer()).post(`${base}/messages`).set('Cookie', cookie)
      .set('x-requested-with', 'teste').send({ texto: 'must stay blocked' }).expect(409)
      .expect(({ body }) => expect(body.code).toBe('INITIAL_SEND_REQUIRED'));
    expect(await prisma.message.count({ where: { conversationId } })).toBe(emptyBefore);

    const actor = await prisma.appUser.findFirstOrThrow({ where: { email: 'initial-journey@leadshug.test' } });
    const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
    const operation = await app.get(OutboundService).prepareInitial({ conversationId, buId: businessUnitId, channelId, kind: 'text' });
    const reserved = await app.get(DispatchAdmissionService).reserveInitial({
      conversationId, buId: businessUnitId, contact: conversation.contact, actorId: actor.id,
      idempotencyKey: randomUUID(), ownerNonce: randomUUID(), selectedContext: operation.context as never,
      requestFingerprint: 'prepared-options-proof', request: {
        canonicalRequest: { kind: 'text', text: 'prepared read-only probe', recipient: conversation.contact },
        originalConversation: { updatedAt: conversation.updatedAt.toISOString(), status: conversation.status,
          attendantUserId: conversation.attendantUserId, attendantName: conversation.attendantName,
          attendantOrigin: conversation.attendantOrigin },
        renderedText: 'prepared read-only probe', originalActorName: actor.name,
      } as never,
    });
    expect(reserved.intent.state).toBe('PREPARED');
    const intentBefore = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } });
    const providerBefore = evolutionFake.enviados.length;
    const providerCallsBefore = evolutionFake.providerCalls;
    const options = await request(app.getHttpServer()).get(`${base}/start-options`).set('Cookie', cookie).expect(200);
    const projected = options.body.activeAttempt;
    process.stdout.write(`ST04_PREPARED_OPTIONS ${JSON.stringify({ state: projected?.state, recoveryAction: projected?.recoveryAction ?? null })}\n`);
    const read = await request(app.getHttpServer()).get(`${base}/initial-messages/${reserved.intent.id}`).set('Cookie', cookie).expect(200);
    expect.soft(projected).toMatchObject({ id: reserved.intent.id, state: 'PREPARED', recoveryAction: 'RECONCILE' });
    expect.soft(read.body).toMatchObject({ id: reserved.intent.id, state: 'PREPARED', recoveryAction: 'RECONCILE' });
    const competingMessage = { tipo: 'TEXTO', texto: 'another explicit initial request while PREPARED owns the slot' };
    const competingPreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem: competingMessage }).expect(200);
    const competing = await request(app.getHttpServer()).post(`${base}/initial-messages`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', randomUUID())
      .send({ channelId, expectedGeneration: generation, mensagem: competingMessage,
        previewFingerprint: competingPreview.body.previewFingerprint });
    process.stdout.write(`ST04_ACTIVE_SLOT_CONFLICT ${JSON.stringify({ code: competing.body.code ?? null,
      attemptId: competing.body.attemptId ?? null, state: competing.body.state ?? null })}\n`);
    await request(app.getHttpServer()).post(`${base}/messages`).set('Cookie', cookie)
      .set('x-requested-with', 'teste').send({ texto: 'still blocked by active slot' }).expect(409)
      .expect(({ body }) => expect.soft(body).toMatchObject({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: reserved.intent.id, state: 'PREPARED' }));
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } })).toEqual(intentBefore);
    expect(await prisma.message.count({ where: { conversationId } })).toBe(0);
    expect(evolutionFake.enviados).toHaveLength(providerBefore);
    expect(evolutionFake.providerCalls).toBe(providerCallsBefore);
    expect.soft(competing.status).toBe(409);
    expect.soft(competing.body).toMatchObject({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: reserved.intent.id, state: 'PREPARED' });

    const reconcilePath = `${base}/initial-messages/${reserved.intent.id}/reconcile`;
    const live = await request(app.getHttpServer()).post(reconcilePath).set('Cookie', cookie)
      .set('x-requested-with', 'teste').send({}).expect(202);
    expect(live.body).toMatchObject({ id: reserved.intent.id, state: 'PREPARED' });
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } }))
      .toMatchObject({ state: 'PREPARED', slotReleasedAt: null });
    expect(await prisma.message.count({ where: { conversationId } })).toBe(0);
    expect(evolutionFake.enviados).toHaveLength(providerBefore);
    expect(evolutionFake.providerCalls).toBe(providerCallsBefore);

    await prisma.initialMessageIntent.update({ where: { id: reserved.intent.id }, data: { leaseExpiresAt: new Date(Date.now() - 1_000) } });
    const expired = await request(app.getHttpServer()).post(reconcilePath).set('Cookie', cookie)
      .set('x-requested-with', 'teste').send({}).expect(200);
    expect(expired.body).toMatchObject({ id: reserved.intent.id, state: 'REJECTED', slotReleasedAt: expect.any(String) });
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } }))
      .toMatchObject({ state: 'REJECTED', slotReleasedAt: expect.any(Date) });
    expect(await prisma.message.count({ where: { conversationId } })).toBe(0);
    expect(evolutionFake.enviados).toHaveLength(providerBefore);
    expect(evolutionFake.providerCalls).toBe(providerCallsBefore);
  });

  it('checks ordinary history with bounded existence SQL rather than counting the full conversation', async () => {
    const rows = Array.from({ length: 320 }, (_, index) => ({
      conversationId, buId: businessUnitId, direction: 'IN' as const, messageType: 'TEXTO' as const,
      content: `synthetic history ${index}`, channelOrigin: 'NAO_OFICIAL' as const, status: 'RECEBIDA' as const,
      externalId: `history-${randomUUID()}`, providerResourceIdentityId: (null as string | null),
    }));
    await prisma.message.createMany({ data: rows });
    sqlQueries.length = 0;
    const before = evolutionFake.enviados.length;
    const response = await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'ordinary after existing history' }).expect(201);
    expect(response.body.id).toMatch(/^[0-9a-f-]{36}$/i);
    expect(evolutionFake.enviados).toHaveLength(before + 1);
    const messageSql = sqlQueries.filter((event) => /FROM\s+(?:"public"\.)?"messages"/i.test(event.query));
    expect(messageSql.length).toBeGreaterThan(0);
    expect(messageSql.map((event) => event.query).join('\n')).not.toMatch(/COUNT\s*\(\s*\*\s*\)/i);
    expect(messageSql.some((event) => /\bLIMIT\b/i.test(event.query)
      && (JSON.parse(event.params) as unknown[]).includes(1))).toBe(true);
  });

  it('opens, previews, sends once, and returns a safe terminal replay without another provider call or Message', async () => {
    const base = `/api/bff/conversations/${conversationId}`;
    const options = await request(app.getHttpServer()).get(`${base}/start-options`)
      .set('Cookie', cookie).expect(200);
    expect(options.body.channels).toEqual(expect.arrayContaining([
      expect.objectContaining({ id: channelId, supportedKinds: ['text'], availability: { text: null, 'approved-template': 'UNSUPPORTED_KIND' } }),
    ]));

    const message = { tipo: 'TEXTO', texto: 'Olá, posso ajudar?' };
    const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
    expect(preview.body).toMatchObject({ text: message.texto, channel: { channelId, generation, requiresWindow: false } });
    expect(preview.body).not.toHaveProperty('recipient');

    const key = 'e4e13e0a-1a63-4bfc-8cc0-11bd490b01d4';
    const payload = { channelId, expectedGeneration: generation, mensagem: message, previewFingerprint: preview.body.previewFingerprint };
    const sent = await request(app.getHttpServer()).post(`${base}/initial-messages`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', key)
      .send(payload).expect(201);
    expect(sent.body).toMatchObject({ replay: false, attempt: {
      state: 'SUCCEEDED', providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED',
    } });
    expect(sent.body).not.toHaveProperty('ownerNonce');
    expect(sent.body).not.toHaveProperty('externalMessageId');
    expect(evolutionFake.enviados).toEqual([{ para: '5511987654321', texto: message.texto }]);
    const countBeforeReplay = await prisma.message.count({ where: { conversationId, direction: 'OUT' } });

    const replay = await request(app.getHttpServer()).post(`${base}/initial-messages`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', key)
      .send(payload).expect(200);
    expect(replay.body).toMatchObject({ replay: true, attempt: { id: sent.body.attempt.id, state: 'SUCCEEDED' } });
    expect(replay.body).not.toHaveProperty('ownerNonce');
    expect(replay.body).not.toHaveProperty('externalMessageId');
    expect(evolutionFake.enviados).toHaveLength(1);
    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(countBeforeReplay);

    const foreign = await criarMantenedora(app, 'Foreign scope', 'foreign-initial@leadshug.test');
    const foreignCookie = await login(app, 'foreign-initial@leadshug.test');
    await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', foreignCookie).set('x-requested-with', 'teste').send({ untrusted: true }).expect(404);
    expect(foreign.businessUnit.id).not.toBe(businessUnitId);
  });

  it('survives five waves of twenty concurrent same-key initial-send requests without duplicate effects', async () => {
    const base = `/api/bff/conversations/${conversationId}`;
    const initialCount = evolutionFake.enviados.length;
    const initialMessages = await prisma.message.count({ where: { conversationId, direction: 'OUT' } });
    let enter!: () => void;
    let release!: () => void;
    let entered = new Promise<void>((resolve) => { enter = resolve; });
    const gate = new Promise<void>((resolve) => { release = resolve; });
    evolutionFake.sendHook = async () => { enter(); await gate; };
    let drainOriginal: Promise<unknown> | null = null;
    const measurements: Array<{ wave: number; requests: number; replay202: number; posts: number; messages: number; elapsedMs: number }> = [];
    try {
      for (let wave = 0; wave < 5; wave += 1) {
        const message = { tipo: 'TEXTO', texto: `BCI onda ${wave + 1}` };
        const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
          .set('Cookie', cookie).set('x-requested-with', 'teste')
          .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
        const payload = { channelId, expectedGeneration: generation, mensagem: message,
          previewFingerprint: preview.body.previewFingerprint };
        const key = `c4e13e0${wave + 1}-1a63-4bfc-8cc0-11bd490b01d4`;
        const before = Date.now();
        const postsBefore = evolutionFake.enviados.length;
        const intentsBefore = await prisma.initialMessageIntent.count({ where: { conversationId } });
        const original = request(app.getHttpServer()).post(`${base}/initial-messages`)
          .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', key).send(payload)
          .then((response) => response);
        drainOriginal = original;
        await entered;
        const replays = await Promise.all(Array.from({ length: 19 }, () => request(app.getHttpServer())
          .post(`${base}/initial-messages`).set('Cookie', cookie).set('x-requested-with', 'teste')
          .set('Idempotency-Key', key).send(payload).then((response) => response)));
        expect(replays.map((response) => response.status)).toEqual(Array(19).fill(202));
        release();
        const first = await original;
        drainOriginal = null;
        expect(first.status).toBe(201);
        expect(first.body.attempt.state).toBe('SUCCEEDED');
        expect(evolutionFake.enviados.length - postsBefore).toBe(1);
        expect(await prisma.initialMessageIntent.count({ where: { conversationId } })).toBe(intentsBefore + 1);
        const durationMs = Date.now() - before;
        expect(durationMs).toBeLessThan(15_000);
        const messagesThisWave = await prisma.message.count({ where: { conversationId, direction: 'OUT' } }) - initialMessages - wave;
        expect(messagesThisWave).toBe(1);
        measurements.push({ wave: wave + 1, requests: 20, replay202: replays.length, posts: evolutionFake.enviados.length - postsBefore,
          messages: messagesThisWave,
          elapsedMs: durationMs });
        if (wave < 4) {
          let nextEnter!: () => void;
          let nextRelease!: () => void;
          entered = new Promise<void>((resolve) => { nextEnter = resolve; });
          const nextGate = new Promise<void>((resolve) => { nextRelease = resolve; });
          evolutionFake.sendHook = async () => { nextEnter(); await nextGate; };
          release = nextRelease;
          enter = nextEnter;
        }
      }
    } finally {
      release();
      evolutionFake.sendHook = null;
      if (drainOriginal) await drainOriginal.catch(() => undefined);
    }
    expect(evolutionFake.enviados).toHaveLength(initialCount + 5);
    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(initialMessages + 5);
    expect(measurements).toHaveLength(5);
    process.stdout.write(`ST04_BCI_5x20 ${JSON.stringify(measurements)}\n`);
  });

  it('requires an empty ACK body, explicit risk header, and elapsed immutable deadline at the BFF', async () => {
    const base = `/api/bff/conversations/${conversationId}`;
    const message = { tipo: 'TEXTO', texto: 'Ambiguous BFF acknowledgment fixture' };
    const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
    evolutionFake.sendIdNull = true;
    try {
      const sent = await request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'a4e13e0a-1a63-4bfc-8cc0-11bd490b01d5')
        .send({ channelId, expectedGeneration: generation, mensagem: message, previewFingerprint: preview.body.previewFingerprint }).expect(409);
      expect(sent.body).toMatchObject({ code: 'INITIAL_SEND_AMBIGUOUS', outcome: 'AMBIGUOUS', state: 'AMBIGUOUS' });
      const attemptId = sent.body.attemptId as string;
      expect(attemptId).toMatch(/^[0-9a-f-]{36}$/i);
      const ackPath = `${base}/initial-messages/${attemptId}/acknowledge`;
      await request(app.getHttpServer()).post(ackPath).set('Cookie', cookie).set('x-requested-with', 'teste')
        .set('X-Confirm-Duplication-Risk', 'true').send({ confirm: true }).expect(400);
      await request(app.getHttpServer()).post(ackPath).set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({}).expect(409).expect(({ body }) => expect(body.code).toBe('DUPLICATION_RISK_CONFIRMATION_REQUIRED'));
      await request(app.getHttpServer()).post(ackPath).set('Cookie', cookie).set('x-requested-with', 'teste')
        .set('X-Confirm-Duplication-Risk', 'true').send({}).expect(409)
        .expect(({ body }) => expect(body.code).toBe('ACK_TOO_EARLY'));
      await prisma.initialMessageIntent.update({ where: { id: attemptId }, data: { dispatchDeadlineAt: new Date(Date.now() - 1_000) } });
      await request(app.getHttpServer()).post(ackPath).set('Cookie', cookie).set('x-requested-with', 'teste')
        .set('X-Confirm-Duplication-Risk', 'true').send({}).expect(200);
      const intent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: attemptId } });
      expect(intent).toMatchObject({ state: 'AMBIGUOUS', slotReleasedAt: expect.any(Date), riskAcknowledgedAt: expect.any(Date) });
      expect(evolutionFake.enviados).toHaveLength(1);
      expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(0);
    } finally {
      evolutionFake.sendIdNull = false;
    }
  });

  it.each([
    ['commit-ack-loss', 409, 'AMBIGUOUS', true],
    ['rollback', 503, undefined, false],
  ] as const)('classifies an unknown provider result only from durable exact state (%s)', async (fault, status, expectedState, committed) => {
    const base = `/api/bff/conversations/${conversationId}`;
    const message = { tipo: 'TEXTO', texto: `Unknown classification ${fault}` };
    const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
    const admission = app.get(DispatchAdmissionService);
    const original = admission.markInitialAmbiguous.bind(admission);
    const mark = vi.spyOn(admission, 'markInitialAmbiguous').mockImplementation((input) =>
      withTransactionFault(prisma, fault, () => original(input)));
    evolutionFake.sendIdNull = true;
    try {
      const response = await request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .set('Idempotency-Key', fault === 'rollback' ? 'b4e13e0a-1a63-4bfc-8cc0-11bd490b01d7' : 'b4e13e0a-1a63-4bfc-8cc0-11bd490b01d8')
        .send({ channelId, expectedGeneration: generation, mensagem: message, previewFingerprint: preview.body.previewFingerprint })
        .expect(status);
      if (committed) expect(response.body).toMatchObject({ code: 'INITIAL_SEND_AMBIGUOUS', state: expectedState });
      else {
        expect(response.body).toMatchObject({ code: 'INITIAL_DISPATCH_UNCONFIRMED', outcome: 'UNKNOWN' });
        expect(response.body).not.toHaveProperty('state');
      }
      expect(mark).toHaveBeenCalledTimes(1);
      expect(evolutionFake.enviados).toHaveLength(1);
      const attemptId = response.body.attemptId as string;
      expect(attemptId).toMatch(/^[0-9a-f-]{36}$/i);
      const intent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: attemptId } });
      expect(intent).toMatchObject({ state: committed ? 'AMBIGUOUS' : 'SENDING', slotReleasedAt: null });
      expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(0);
    } finally {
      mark.mockRestore();
      evolutionFake.sendIdNull = false;
    }
  });

  it('marks preview-context rejection as definitively pre-reservation and performs no provider send', async () => {
    const base = `/api/bff/conversations/${conversationId}`;
    const message = { tipo: 'TEXTO', texto: 'Context changed before admission' };
    const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
    await prisma.buChannel.update({ where: { id: channelId }, data: { generation: generation + 1 } });
    const response = await request(app.getHttpServer()).post(`${base}/initial-messages`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'b4e13e0a-1a63-4bfc-8cc0-11bd490b01d6')
      .send({ channelId, expectedGeneration: generation, mensagem: message, previewFingerprint: preview.body.previewFingerprint })
      .expect(409);
    expect(response.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', preAdmission: true });
    expect(response.body).not.toHaveProperty('attemptId');
    expect(await prisma.initialMessageIntent.count({ where: { conversationId } })).toBe(0);
    expect(evolutionFake.enviados).toHaveLength(0);
  });

  it('rejects a forged cross-tenant BU grant on every new initial-contact route before effects', async () => {
    const foreign = await criarMantenedora(app, 'Forged grant tenant', 'forged-initial@leadshug.test');
    await prisma.userBuRole.create({ data: { userId: foreign.owner.id, buId: businessUnitId, role: 'ATENDENTE' } });
    const foreignCookie = await login(app, 'forged-initial@leadshug.test');
    const base = `/api/bff/conversations/${conversationId}`;
    const ownerPreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem: { tipo: 'TEXTO', texto: 'Owner only fixture' } }).expect(200);
    const ownerSend = await request(app.getHttpServer()).post(`${base}/initial-messages`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'b4e13e0a-1a63-4bfc-8cc0-11bd490b01d4')
      .send({ channelId, expectedGeneration: generation, mensagem: { tipo: 'TEXTO', texto: 'Owner only fixture' },
        previewFingerprint: ownerPreview.body.previewFingerprint }).expect(201);
    const actualAttemptId = ownerSend.body.attempt.id as string;
    const externalBefore = evolutionFake.enviados.length + metaFake.enviados.length;
    const messagesBefore = await prisma.message.count({ where: { conversationId } });
    await request(app.getHttpServer()).post(`/api/bff/business-units/${businessUnitId}/conversations/open`)
      .set('Cookie', foreignCookie).set('x-requested-with', 'teste').send({ telefone: '5511999999999' }).expect(404);
    await request(app.getHttpServer()).get(`${base}/start-options`).set('Cookie', foreignCookie).expect(404);
    await request(app.getHttpServer()).post(`${base}/initial-message-preview`).set('Cookie', foreignCookie)
      .set('x-requested-with', 'teste').send({ channelId, expectedGeneration: generation, mensagem: { tipo: 'TEXTO', texto: 'nope' } }).expect(404);
    await request(app.getHttpServer()).post(`${base}/initial-messages`).set('Cookie', foreignCookie)
      .set('x-requested-with', 'teste').set('Idempotency-Key', 'd4e13e0a-1a63-4bfc-8cc0-11bd490b01d4')
      .send({ channelId, expectedGeneration: generation, mensagem: { tipo: 'TEXTO', texto: 'nope' }, previewFingerprint: 'a'.repeat(64) }).expect(404);
    await request(app.getHttpServer()).get(`${base}/initial-messages/${actualAttemptId}`).set('Cookie', foreignCookie).expect(404);
    await request(app.getHttpServer()).post(`${base}/initial-messages/${actualAttemptId}/reconcile`).set('Cookie', foreignCookie)
      .set('x-requested-with', 'teste').send({}).expect(404);
    await request(app.getHttpServer()).post(`${base}/initial-messages/${actualAttemptId}/acknowledge`).set('Cookie', foreignCookie)
      .set('x-requested-with', 'teste').set('X-Confirm-Duplication-Risk', 'true').send({}).expect(404);
    expect(foreign.businessUnit.id).not.toBe(businessUnitId);
    expect(evolutionFake.enviados.length + metaFake.enviados.length).toBe(externalBefore);
    expect(await prisma.message.count({ where: { conversationId } })).toBe(messagesBefore);
    expect(await prisma.conversation.count({ where: { buId: businessUnitId, contact: '5511999999999' } })).toBe(0);
  });

  it('previews and sends approved NAMED and POSITIONAL templates outside the window on the selected Meta account', async () => {
    const official = await criarCanalVerificado(prisma, businessUnitId, 'OFICIAL', '111111111', { requiresWindow: true });
    await prisma.buChannel.update({ where: { id: official.channel.id }, data: { wabaId: '123456789' } });
    const templates = [
      { id: 'template-named', name: 'initial_named', language: 'en_US', status: 'APPROVED', category: 'UTILITY', parameter_format: 'NAMED',
        components: [{ type: 'BODY', text: 'Hello {{name}}', example: { body_text_named_params: [{ param_name: 'name', example: 'Ada' }] } }] },
      { id: 'template-positional', name: 'initial_positional', language: 'en_US', status: 'APPROVED', category: 'UTILITY', parameter_format: 'POSITIONAL',
        components: [{ type: 'BODY', text: 'Hello {{2}} before {{1}}, then {{2}}', example: { body_text: [['first', 'second']] } }] },
      { id: 'template-buttons', name: 'initial_buttons', language: 'en_US', status: 'APPROVED', category: 'UTILITY', parameter_format: 'NAMED',
        components: [{ type: 'BODY', text: 'Hello', example: { body_text: [['Hello']] } }, { type: 'BUTTONS', buttons: [{ type: 'QUICK_REPLY', text: 'Confirm' }] }] },
    ];
    const graphRequests: Array<{ url: string; method: string; body: Record<string, unknown> | null }> = [];
    let grantTargets = ['123456789'];
    let denyMessagingGrant = false;
    let statusOverride: string | null = null;
    let overflowTemplateList = false;
    let twoPageTemplateList = false;
    let duplicateTemplateResult = false;
    let changeTemplateDefinition = false;
    let twoPageMembership = false;
    let phoneReadLatch: { enter: () => void; gate: Promise<void> } | null = null;
    let postLatch: { enter: () => void; gate: Promise<void> } | null = null;
    const originalMembershipVerifier = metaFake.verificarNumeroVinculado;
    metaFake.verificarNumeroVinculado = (wabaId, phoneNumberId, accessToken) =>
      new MetaHttpClient().verificarNumeroVinculado(wabaId, phoneNumberId, accessToken);
    const armPhoneRead = () => {
      let enter!: () => void;
      let release!: () => void;
      const entered = new Promise<void>((resolve) => { enter = resolve; });
      const gate = new Promise<void>((resolve) => { release = resolve; });
      phoneReadLatch = { enter, gate };
      return { entered, release: () => { release(); phoneReadLatch = null; } };
    };
    vi.stubGlobal('fetch', vi.fn(async (input: string | URL | Request, init?: RequestInit) => {
      const url = String(input);
      const method = init?.method ?? 'GET';
      let body: Record<string, unknown> | null = null;
      if (typeof init?.body === 'string') body = JSON.parse(init.body) as Record<string, unknown>;
      graphRequests.push({ url, method, body });
      if (url.includes('/phone_numbers')) {
        if (phoneReadLatch) {
          const latch = phoneReadLatch;
          latch.enter();
          await latch.gate;
        }
        const after = new URL(url).searchParams.get('after');
        const phonePage = twoPageMembership && !after
          ? { data: Array.from({ length: 50 }, (_, index) => ({ id: `unrelated-${index}`, display_phone_number: '+55 11 00000-0000' })), paging: { next: 'https://graph.facebook.com/next', cursors: { after: 'phone-page-2' } } }
          : { data: [{ id: '111111111', display_phone_number: '+55 11 98765-4321' }] };
        return new Response(JSON.stringify(phonePage), { status: 200, headers: { 'content-type': 'application/json' } });
      }
      if (url.includes('/debug_token?')) return new Response(JSON.stringify({ data: {
        app_id: 'fixture-app', is_valid: true, scopes: denyMessagingGrant ? ['whatsapp_business_management'] : ['whatsapp_business_management', 'whatsapp_business_messaging'],
        granular_scopes: [{ scope: 'whatsapp_business_management', target_ids: grantTargets },
          ...(!denyMessagingGrant ? [{ scope: 'whatsapp_business_messaging', target_ids: grantTargets }] : [])],
      } }), { status: 200, headers: { 'content-type': 'application/json' } });
      if (url.includes('/message_templates?')) {
        const name = new URL(url).searchParams.get('name');
        const after = new URL(url).searchParams.get('after');
        const matching = templates.filter((template) => !name || template.name === name)
          .map((template) => statusOverride ? { ...template, status: statusOverride } : template)
          .map((template) => changeTemplateDefinition && template.id === 'template-named'
            ? { ...template, components: [{ type: 'BODY', text: 'Changed {{name}}', example: { body_text_named_params: [{ param_name: 'name', example: 'Ada' }] } }] }
            : template);
        if (twoPageTemplateList) return new Response(JSON.stringify(after
          ? { data: matching }
          : { data: [], paging: { cursors: { after: 'template-page-2' }, next: 'https://graph.facebook.com/next' } }),
        { status: 200, headers: { 'content-type': 'application/json' } });
        if (overflowTemplateList) return new Response(JSON.stringify(after
          ? { data: matching, paging: { cursors: { after: 'third-page' }, next: 'fixture:next' } }
          : { data: [], paging: { cursors: { after: 'second-page' }, next: 'fixture:next' } }),
        { status: 200, headers: { 'content-type': 'application/json' } });
        const data = duplicateTemplateResult && matching[0] ? [...matching, matching[0]] : matching;
        return new Response(JSON.stringify({ data }),
          { status: 200, headers: { 'content-type': 'application/json' } });
      }
      if (url.endsWith('/111111111/messages') && method === 'POST') {
        if (postLatch) {
          const latch = postLatch;
          latch.enter();
          await latch.gate;
        }
        return new Response(JSON.stringify({ messaging_product: 'whatsapp', messages: [{ id: `wamid-template-${graphRequests.filter((entry) => entry.method === 'POST').length}` }] }),
          { status: 200, headers: { 'content-type': 'application/json' } });
      }
      return new Response(JSON.stringify({ error: { message: 'unexpected fixture request' } }),
        { status: 404, headers: { 'content-type': 'application/json' } });
    }));
    metaFake.confirmHook = async () => {
      const latch = phoneReadLatch;
      if (!latch) return;
      latch.enter();
      await latch.gate;
    };
    try {
      const catalog = await request(app.getHttpServer()).post(`/api/bff/business-units/${businessUnitId}/channels/${official.channel.id}/message-template-catalog`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').send({}).expect(200);
      expect(catalog.body).toMatchObject({ available: true, items: expect.arrayContaining([
        expect.objectContaining({ remoteTemplateId: 'template-named', status: 'APPROVED' }),
        expect.objectContaining({ remoteTemplateId: 'template-positional', status: 'APPROVED' }),
        expect.objectContaining({ remoteTemplateId: 'template-buttons', status: 'APPROVED' }),
      ]) });

      const base = `/api/bff/conversations/${conversationId}`;
      await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: {
          tipo: 'TEMPLATE', templateId: 'template-buttons', language: 'en_US', expectedDefinitionFingerprint: 'a'.repeat(64), parameters: {},
        } }).expect(409).expect(({ body }) => expect(body).toMatchObject({ code: 'INITIAL_TEMPLATE_UNSUPPORTED' }));
      expect(graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(0);
      expect(await prisma.initialMessageIntent.count({ where: { conversationId } })).toBe(0);
      const inboundWindowSeed = await prisma.message.create({ data: {
        conversationId, buId: businessUnitId, direction: 'IN', messageType: 'TEXTO', content: 'trusted window seed',
        channelOrigin: 'OFICIAL', status: 'RECEBIDA', externalId: `window-expiry-seed-${conversationId}`,
        providerResourceIdentityId: official.identity.id, officialInboundAt: new Date(),
      } });
      const textMessage = { tipo: 'TEXTO', texto: 'Window must be checked after the real provider GET' };
      const textPreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: textMessage }).expect(200);
      const windowLatch = armPhoneRead();
      const windowKey = 'c4e13e0a-1a63-4bfc-8cc0-11bd490b01d6';
      const postsBeforeWindow = graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages')).length;
      const windowSend = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', windowKey)
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: textMessage,
          previewFingerprint: textPreview.body.previewFingerprint }).then((response) => response);
      try {
        await windowLatch.entered;
        await prisma.message.update({ where: { id: inboundWindowSeed.id }, data: {
          officialInboundAt: new Date(Date.now() - 24 * 60 * 60 * 1000 - 1_000),
        } });
        windowLatch.release();
        const blocked = await windowSend;
        expect(blocked.status).toBe(409);
        expect(blocked.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
        expect(graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(postsBeforeWindow);
        const windowIntent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: {
          buId_actorId_idempotencyKey: { buId: businessUnitId, actorId: (await prisma.appUser.findFirstOrThrow({ where: { email: 'initial-journey@leadshug.test' } })).id, idempotencyKey: windowKey },
        } });
        expect(windowIntent).toMatchObject({ state: 'REJECTED', dispatchDeadlineAt: null, slotReleasedAt: expect.any(Date) });
      } finally {
        windowLatch.release();
        await windowSend.catch(() => undefined);
      }

      const delayedSummary = catalog.body.items.find((row: { remoteTemplateId: string }) => row.remoteTemplateId === 'template-named');
      const delayedRender = renderInitialTemplate(delayedSummary, { name: 'Delay' });
      const delayedMessage = { tipo: 'TEMPLATE', templateId: 'template-named', language: 'en_US',
        expectedDefinitionFingerprint: delayedRender.semanticFingerprint, parameters: { name: 'Delay' } };
      const delayedPreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage }).expect(200);
      const delayedKey = 'c4e13e0a-1a63-4bfc-8cc0-11bd490b01d4';
      const messagesBeforeDelay = await prisma.message.count({ where: { conversationId, direction: 'OUT' } });
      const leaseRead = armPhoneRead();
      const delayedSend = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', delayedKey)
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage,
          previewFingerprint: delayedPreview.body.previewFingerprint }).then((response) => response);
      try {
        await leaseRead.entered;
        const waitingIntent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: {
          buId_actorId_idempotencyKey: { buId: businessUnitId, actorId: (await prisma.appUser.findFirstOrThrow({ where: { email: 'initial-journey@leadshug.test' } })).id, idempotencyKey: delayedKey },
        } });
        await prisma.initialMessageIntent.update({ where: { id: waitingIntent.id }, data: { leaseExpiresAt: new Date(Date.now() - 1) } });
        leaseRead.release();
        const blocked = await delayedSend;
        expect(blocked.status).toBe(409);
        expect(blocked.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
        expect(graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(0);
        expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(messagesBeforeDelay);
        expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: waitingIntent.id } })).toMatchObject({
          state: 'REJECTED', dispatchDeadlineAt: null, slotReleasedAt: expect.any(Date),
        });
      } finally {
        leaseRead.release();
      }

      const actorId = await criarUsuario(prisma, mantenedoraId, businessUnitId, 'initial-claim-revoked@leadshug.test', 'ATENDENTE');
      const actorCookie = await login(app, 'initial-claim-revoked@leadshug.test');
      const revokePreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', actorCookie).set('x-requested-with', 'teste')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage }).expect(200);
      const revokeLatch = armPhoneRead();
      const revokeKey = 'f4e13e0a-1a63-4bfc-8cc0-11bd490b01d4';
      const postsBeforeRevoke = graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages')).length;
      const revokeSend = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', actorCookie).set('x-requested-with', 'teste').set('Idempotency-Key', revokeKey)
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage,
          previewFingerprint: revokePreview.body.previewFingerprint }).then((response) => response);
      let signalDelete!: () => void;
      let releaseDelete!: () => void;
      const deleteEntered = new Promise<void>((resolve) => { signalDelete = resolve; });
      const deleteGate = new Promise<void>((resolve) => { releaseDelete = resolve; });
      let deleteTransaction: Promise<unknown> | null = null;
      try {
        await revokeLatch.entered;
        deleteTransaction = prisma.$transaction(async (tx) => {
          await tx.userBuRole.deleteMany({ where: { userId: actorId, buId: businessUnitId } });
          signalDelete();
          await deleteGate;
        });
        await deleteEntered;
        revokeLatch.release();
        await waitForActorGrantShareLock(prisma);
        releaseDelete();
        await deleteTransaction;
        const revoked = await revokeSend;
        expect(revoked.status).toBe(409);
        expect(revoked.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
        expect(graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(postsBeforeRevoke);
        expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(messagesBeforeDelay);
        expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: {
          buId_actorId_idempotencyKey: { buId: businessUnitId, actorId, idempotencyKey: revokeKey },
        } })).toMatchObject({ state: 'REJECTED', dispatchDeadlineAt: null, slotReleasedAt: expect.any(Date) });
      } finally {
        revokeLatch.release();
        releaseDelete();
        if (deleteTransaction) await deleteTransaction.catch(() => undefined);
      }

      const expiryActorId = await criarUsuario(prisma, mantenedoraId, businessUnitId, 'initial-claim-expiry@leadshug.test', 'ATENDENTE');
      const expiryCookie = await login(app, 'initial-claim-expiry@leadshug.test');
      const expiryClaims = app.get(SessionService).verificar(app.get(SessionService).extrairDoCabecalho(expiryCookie));
      expect(expiryClaims).not.toBeNull();
      const expiryPreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', expiryCookie).set('x-requested-with', 'teste')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage }).expect(200);
      const expiryLatch = armPhoneRead();
      const expiryKey = 'a4e13e0a-1a63-4bfc-8cc0-11bd490b01d4';
      const postsBeforeExpiry = graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages')).length;
      const expirySend = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', expiryCookie).set('x-requested-with', 'teste').set('Idempotency-Key', expiryKey)
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage,
          previewFingerprint: expiryPreview.body.previewFingerprint }).then((response) => response);
      let signalRoleLock!: () => void;
      let releaseRoleLock!: () => void;
      const roleLockEntered = new Promise<void>((resolve) => { signalRoleLock = resolve; });
      const roleLockGate = new Promise<void>((resolve) => { releaseRoleLock = resolve; });
      let roleLockTransaction: Promise<unknown> | null = null;
      const expiryClock = vi.spyOn(Date, 'now');
      try {
        await expiryLatch.entered;
        roleLockTransaction = prisma.$transaction(async (tx) => {
          await tx.userBuRole.updateMany({ where: { userId: expiryActorId, buId: businessUnitId }, data: { role: 'ATENDENTE' } });
          signalRoleLock();
          await roleLockGate;
        });
        await roleLockEntered;
        expiryLatch.release();
        await waitForActorGrantShareLock(prisma);
        expiryClock.mockReturnValue(expiryClaims!.exp + 1);
        releaseRoleLock();
        await roleLockTransaction;
        const expired = await expirySend;
        expect(expired.status).toBe(409);
        expect(expired.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
        expect(graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(postsBeforeExpiry);
        expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(messagesBeforeDelay);
      } finally {
        expiryClock.mockRestore();
        expiryLatch.release();
        releaseRoleLock();
        if (roleLockTransaction) await roleLockTransaction.catch(() => undefined);
      }

      const ownerRacePreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage }).expect(200);
      let enterPost!: () => void;
      let releasePost!: () => void;
      const postEntered = new Promise<void>((resolve) => { enterPost = resolve; });
      const postGate = new Promise<void>((resolve) => { releasePost = resolve; });
      postLatch = { enter: enterPost, gate: postGate };
      const ownerRaceKey = 'd4e13e0a-1a63-4bfc-8cc0-11bd490b01d4';
      const ownerRaceSend = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', ownerRaceKey)
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: delayedMessage,
          previewFingerprint: ownerRacePreview.body.previewFingerprint }).then((response) => response);
      try {
        await postEntered;
        await prisma.conversation.update({ where: { id: conversationId }, data: {
          status: 'CLOSED', attendantUserId: null, attendantName: 'Concurrent external owner', attendantOrigin: 'EXTERNO',
        } });
        releasePost();
        const accepted = await ownerRaceSend;
        expect(accepted.status).toBe(201);
        expect(accepted.body.attempt).toMatchObject({ state: 'SUCCEEDED', providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED' });
        expect(await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } })).toMatchObject({
          status: 'CLOSED', attendantUserId: null, attendantName: 'Concurrent external owner', attendantOrigin: 'EXTERNO',
        });
      } finally {
        releasePost();
        postLatch = null;
        await ownerRaceSend.catch(() => undefined);
      }

      const cases = [
        { id: 'template-named', values: { name: 'Ada' } },
        { id: 'template-positional', values: ['first', 'second'] },
      ] as const;
      for (const [index, item] of cases.entries()) {
        const summary = catalog.body.items.find((row: { remoteTemplateId: string }) => row.remoteTemplateId === item.id);
        const rendered = renderInitialTemplate(summary, item.values);
        const mensagem = { tipo: 'TEMPLATE', templateId: item.id, language: 'en_US', expectedDefinitionFingerprint: rendered.semanticFingerprint, parameters: item.values };
        const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
          .set('Cookie', cookie).set('x-requested-with', 'teste')
          .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem }).expect(200);
        expect(preview.body.text).toBe(rendered.text);
        expect(preview.body.channel).toMatchObject({ channelId: official.channel.id, requiresWindow: true });
        const payload = { channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem,
          previewFingerprint: preview.body.previewFingerprint };
        const key = index === 0 ? 'a4e13e0a-1a63-4bfc-8cc0-11bd490b01d4' : 'b4e13e0a-1a63-4bfc-8cc0-11bd490b01d4';
        const protocolStartedAt = Date.now();
        const protocolStart = graphRequests.length;
        await request(app.getHttpServer()).post(`${base}/initial-messages`)
          .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', key)
          .send(payload).expect(201).expect(({ body }) => {
            expect(body.attempt).toMatchObject({ state: 'SUCCEEDED', providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED', localMessageState: 'RECORDED' });
          });
        const initialProtocol = graphRequests.slice(protocolStart);
        expect(initialProtocol.filter((entry) => entry.method === 'GET').length).toBeLessThanOrEqual(6);
        expect(initialProtocol.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(1);
        expect(Date.now() - protocolStartedAt).toBeLessThan(75_000);
        const requestsBeforeReplay = graphRequests.length;
        const replay = await request(app.getHttpServer()).post(`${base}/initial-messages`)
          .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', key)
          .send(payload).expect(200);
        expect(replay.body.attempt.state).toBe('SUCCEEDED');
        expect(graphRequests).toHaveLength(requestsBeforeReplay);
      }
      twoPageTemplateList = true;
      twoPageMembership = true;
      const boundedSummary = catalog.body.items.find((row: { remoteTemplateId: string }) => row.remoteTemplateId === 'template-named');
      const boundedRender = renderInitialTemplate(boundedSummary, { name: 'Bounded' });
      const boundedMessage = { tipo: 'TEMPLATE', templateId: 'template-named', language: 'en_US',
        expectedDefinitionFingerprint: boundedRender.semanticFingerprint, parameters: { name: 'Bounded' } };
      const boundedPreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: boundedMessage }).expect(200);
      const boundedStart = graphRequests.length;
      const boundedAt = Date.now();
      await request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'f4e13e0a-1a63-4bfc-8cc0-11bd490b01d5')
        .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem: boundedMessage,
          previewFingerprint: boundedPreview.body.previewFingerprint }).expect(201);
      const boundedProtocol = graphRequests.slice(boundedStart);
      expect(boundedProtocol.filter((entry) => entry.method === 'GET')).toHaveLength(6);
      expect(boundedProtocol.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(1);
      expect(boundedProtocol.filter((entry) => entry.url.includes('/message_templates?'))).toHaveLength(2);
      expect(boundedProtocol.filter((entry) => entry.url.includes('/phone_numbers'))).toHaveLength(2);
      expect(Date.now() - boundedAt).toBeLessThan(75_000);
      twoPageTemplateList = false;
      twoPageMembership = false;
      const posts = graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'));
      expect(posts).toHaveLength(4);
      expect(posts[1].body).toMatchObject({ messaging_product: 'whatsapp', messaging_account_id: '123456789', to: '+5511987654321',
        template: { name: 'initial_named', components: [{ type: 'body', parameters: [{ type: 'text', text: 'Ada', parameter_name: 'name' }] }] } });
      expect(posts[2].body).toMatchObject({ template: { name: 'initial_positional', components: [{ type: 'body', parameters: [
        { type: 'text', text: 'first' }, { type: 'text', text: 'second' },
      ] }] } });
      expect(metaFake.enviados).toHaveLength(0);
      expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(4);
      const noDispatchCases: Array<{ label: string; mode: () => void; reset: () => void; key: string; expectedCode?: string }> = [
        { label: 'paused', mode: () => { statusOverride = 'PAUSED'; }, reset: () => { statusOverride = null; }, key: 'b4e13e0a-1a63-4bfc-8cc0-11bd490b01d5' },
        { label: 'unknown-status', mode: () => { statusOverride = 'UNKNOWN'; }, reset: () => { statusOverride = null; }, key: 'e4e13e0a-1a63-4bfc-8cc0-11bd490b01d5' },
        { label: 'off-account', mode: () => { grantTargets = ['another-account']; }, reset: () => { grantTargets = ['123456789']; }, key: 'c4e13e0a-1a63-4bfc-8cc0-11bd490b01d5', expectedCode: 'CHANNEL_NOT_READY' },
        { label: 'missing-messaging-grant', mode: () => { denyMessagingGrant = true; }, reset: () => { denyMessagingGrant = false; }, key: 'e4e13e0a-1a63-4bfc-8cc0-11bd490b01d6', expectedCode: 'CHANNEL_NOT_READY' },
        { label: 'two-page-overflow', mode: () => { overflowTemplateList = true; }, reset: () => { overflowTemplateList = false; }, key: 'd4e13e0a-1a63-4bfc-8cc0-11bd490b01d5' },
        { label: 'changed-definition', mode: () => { changeTemplateDefinition = true; }, reset: () => { changeTemplateDefinition = false; }, key: 'a4e13e0a-1a63-4bfc-8cc0-11bd490b01d6' },
        { label: 'duplicate-template-id', mode: () => { duplicateTemplateResult = true; }, reset: () => { duplicateTemplateResult = false; }, key: 'b4e13e0a-1a63-4bfc-8cc0-11bd490b01d6' },
      ];
      for (const item of noDispatchCases) {
        item.mode();
        const negativeActorId = await criarUsuario(prisma, mantenedoraId, businessUnitId,
          `initial-template-negative-${item.label}@leadshug.test`, 'ATENDENTE');
        const negativeCookie = await login(app, `initial-template-negative-${item.label}@leadshug.test`);
        const summary = catalog.body.items.find((row: { remoteTemplateId: string }) => row.remoteTemplateId === 'template-named');
        const rendered = renderInitialTemplate(summary, { name: item.label });
        const mensagem = { tipo: 'TEMPLATE', templateId: 'template-named', language: 'en_US',
          expectedDefinitionFingerprint: rendered.semanticFingerprint, parameters: { name: item.label } };
        const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
          .set('Cookie', negativeCookie).set('x-requested-with', 'teste')
          .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem }).expect(200);
        const postsBefore = graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages')).length;
        const response = await request(app.getHttpServer()).post(`${base}/initial-messages`)
          .set('Cookie', negativeCookie).set('x-requested-with', 'teste').set('Idempotency-Key', item.key)
          .send({ channelId: official.channel.id, expectedGeneration: official.channel.generation, mensagem,
            previewFingerprint: preview.body.previewFingerprint }).expect(409);
        expect(response.body.code).toBe(item.expectedCode ?? 'UNSUPPORTED_KIND');
        expect(graphRequests.filter((entry) => entry.method === 'POST' && entry.url.endsWith('/111111111/messages'))).toHaveLength(postsBefore);
        const rejected = await prisma.initialMessageIntent.findUniqueOrThrow({ where: {
          buId_actorId_idempotencyKey: { buId: businessUnitId, actorId: negativeActorId, idempotencyKey: item.key },
        } });
        expect(rejected).toMatchObject({ state: 'REJECTED', slotReleasedAt: expect.any(Date), dispatchDeadlineAt: null });
        item.reset();
      }
    } finally {
      phoneReadLatch = null;
      postLatch = null;
      metaFake.verificarNumeroVinculado = originalMembershipVerifier;
      metaFake.confirmHook = null;
      vi.unstubAllGlobals();
    }
  });

  it('requires the immutable deadline for local risk release of known acceptance and permits a new successor without resend', async () => {
    const actorId = await criarUsuario(prisma, mantenedoraId, businessUnitId, 'initial-risk-ack@leadshug.test', 'ATENDENTE');
    const actorCookie = await login(app, 'initial-risk-ack@leadshug.test');
    const base = `/api/bff/conversations/${conversationId}`;
    const mensagem = { tipo: 'TEXTO', texto: 'Known external acceptance without local completion' };
    const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', actorCookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem }).expect(200);
    let enter!: () => void;
    let release!: () => void;
    const atProvider = new Promise<void>((resolve) => { enter = resolve; });
    const gate = new Promise<void>((resolve) => { release = resolve; });
    evolutionFake.sendHook = async () => { enter(); await gate; };
    let pending: Promise<{ status: number; body: Record<string, unknown> }> | null = null;
    try {
      pending = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', actorCookie).set('x-requested-with', 'teste').set('Idempotency-Key', randomUUID())
        .send({ channelId, expectedGeneration: generation, mensagem, previewFingerprint: preview.body.previewFingerprint })
        .then((response) => response);
      await atProvider;
      await prisma.userBuRole.deleteMany({ where: { userId: actorId, buId: businessUnitId } });
      release();
      const incomplete = await pending;
      expect(incomplete.status).toBe(503);
      expect(incomplete.body).toMatchObject({ state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', providerAcceptance: 'CONFIRMED',
        receiptPersistence: 'RECORDED', recoveryAction: 'RECONCILE' });
    } finally {
      release();
      evolutionFake.sendHook = null;
      if (pending) await pending.catch(() => undefined);
    }

    const intent = await prisma.initialMessageIntent.findFirstOrThrow({ where: { conversationId } });
    const currentId = await criarUsuario(prisma, mantenedoraId, businessUnitId, 'initial-risk-reviewer@leadshug.test', 'ATENDENTE');
    const currentCookie = await login(app, 'initial-risk-reviewer@leadshug.test');
    const currentAttempt = await request(app.getHttpServer()).get(`${base}/initial-messages/${intent.id}`).set('Cookie', currentCookie).expect(200);
    expect(currentAttempt.body).toMatchObject({ state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', riskAcknowledgementAvailable: true,
      providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED', localMessageState: 'UNCONFIRMED' });
    const ackPath = `${base}/initial-messages/${intent.id}/acknowledge`;
    await request(app.getHttpServer()).post(ackPath).set('Cookie', currentCookie).set('x-requested-with', 'teste')
      .set('X-Confirm-Duplication-Risk', 'true').send({}).expect(409)
      .expect(({ body }) => expect(body).toMatchObject({ code: 'ACK_TOO_EARLY', eligibleAt: expect.any(String) }));
    const ackBeforeProvider = evolutionFake.enviados.length;
    await prisma.initialMessageIntent.update({ where: { id: intent.id }, data: { dispatchDeadlineAt: new Date(Date.now() - 1_000) } });
    const acknowledged = await request(app.getHttpServer()).post(ackPath).set('Cookie', currentCookie).set('x-requested-with', 'teste')
      .set('X-Confirm-Duplication-Risk', 'true').send({}).expect(200);
    expect(acknowledged.body).toMatchObject({ id: intent.id, state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', slotReleasedAt: expect.any(String) });
    expect(evolutionFake.enviados).toHaveLength(ackBeforeProvider);
    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(0);
    const releasedOriginal = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: intent.id } });
    expect(releasedOriginal).toMatchObject({
      externalMessageId: expect.any(String), slotReleasedAt: expect.any(Date), riskAcknowledgedAt: expect.any(Date),
    });
    expect(releasedOriginal.slotReleasedAt!.toISOString()).toBe(acknowledged.body.slotReleasedAt);

    const successorText = { tipo: 'TEXTO', texto: 'New explicit send after released slot' };
    const successorPreview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', currentCookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem: successorText }).expect(200);
    const successor = await request(app.getHttpServer()).post(`${base}/initial-messages`)
      .set('Cookie', currentCookie).set('x-requested-with', 'teste').set('Idempotency-Key', randomUUID())
      .send({ channelId, expectedGeneration: generation, mensagem: successorText,
        previewFingerprint: successorPreview.body.previewFingerprint }).expect(201);
    expect(successor.body.attempt.id).not.toBe(intent.id);
    expect(evolutionFake.enviados).toHaveLength(ackBeforeProvider + 1);
    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(1);
    const successorConversation = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
    const providerCallsBeforeLateRecovery = evolutionFake.providerCalls;
    const lateRecovery = await request(app.getHttpServer()).post(`${base}/initial-messages/${intent.id}/reconcile`)
      .set('Cookie', currentCookie).set('x-requested-with', 'teste').send({}).expect(200);
    expect(lateRecovery.body).toMatchObject({ id: intent.id, state: 'SUCCEEDED', slotReleasedAt: expect.any(String) });
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: successor.body.attempt.id } }))
      .toMatchObject({ state: 'SUCCEEDED', slotReleasedAt: expect.any(Date) });
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: intent.id } }))
      .toMatchObject({ state: 'SUCCEEDED', slotReleasedAt: releasedOriginal.slotReleasedAt });
    expect(await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } }))
      .toMatchObject({ status: successorConversation.status, attendantUserId: successorConversation.attendantUserId,
        attendantName: successorConversation.attendantName, attendantOrigin: successorConversation.attendantOrigin });
    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(2);
    expect(evolutionFake.providerCalls).toBe(providerCallsBeforeLateRecovery);
    expect(evolutionFake.enviados).toHaveLength(ackBeforeProvider + 1);
    expect(currentId).not.toBe(actorId);
  });

  it('keeps known provider acceptance explicit when the current grant is revoked before local Message commit', async () => {
    const actorId = await criarUsuario(prisma, mantenedoraId, businessUnitId, 'initial-revoked@leadshug.test', 'ATENDENTE');
    const actorCookie = await login(app, 'initial-revoked@leadshug.test');
    const base = `/api/bff/conversations/${conversationId}`;
    const mensagem = { tipo: 'TEXTO', texto: 'Grant revocation fence' };
    const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
      .set('Cookie', actorCookie).set('x-requested-with', 'teste')
      .send({ channelId, expectedGeneration: generation, mensagem }).expect(200);
    let enter!: () => void;
    let release!: () => void;
    const atProvider = new Promise<void>((resolve) => { enter = resolve; });
    const gate = new Promise<void>((resolve) => { release = resolve; });
    evolutionFake.sendHook = async () => { enter(); await gate; };
    const pending = request(app.getHttpServer()).post(`${base}/initial-messages`)
      .set('Cookie', actorCookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'c4e13e0a-1a63-4bfc-8cc0-11bd490b01d4')
      .send({ channelId, expectedGeneration: generation, mensagem, previewFingerprint: preview.body.previewFingerprint })
      .then((response) => response);
    try {
      await atProvider;
      await prisma.userBuRole.deleteMany({ where: { userId: actorId, buId: businessUnitId } });
      release();
      const response = await pending;
      expect(response.status).toBe(503);
      expect(response.body).toMatchObject({ code: 'INITIAL_LOCAL_ACCEPTANCE_UNCONFIRMED', state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE',
        providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED', localMessageState: 'UNCONFIRMED', recoveryAction: 'RECONCILE' });
      expect(response.body).not.toHaveProperty('externalMessageId');
      expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(0);
      const attempt = await prisma.initialMessageIntent.findFirstOrThrow({ where: { conversationId } });
      expect(attempt).toMatchObject({ state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', externalMessageId: expect.stringMatching(/^evo-enviado-/) });
    } finally {
      release();
      evolutionFake.sendHook = null;
    }
    expect(evolutionFake.enviados).toHaveLength(1);

    const originalAttempt = await prisma.initialMessageIntent.findFirstOrThrow({ where: { conversationId } });
    const originalRequest = originalAttempt.request as { originalActorName: string };
    const currentActorId = await criarUsuario(prisma, mantenedoraId, businessUnitId, 'initial-current-reconciler@leadshug.test', 'ATENDENTE');
    const currentActorCookie = await login(app, 'initial-current-reconciler@leadshug.test');
    const providerCallsBeforeRecovery = evolutionFake.enviados.length;
    const recovered = await request(app.getHttpServer()).post(`${base}/initial-messages/${originalAttempt.id}/reconcile`)
      .set('Cookie', currentActorCookie).set('x-requested-with', 'teste').send({}).expect(200);
    expect(recovered.body).toMatchObject({ id: originalAttempt.id, state: 'SUCCEEDED', localMessageState: 'RECORDED', recoveryAction: null });
    const localMessage = await prisma.message.findFirstOrThrow({ where: { conversationId, direction: 'OUT' } });
    expect(localMessage).toMatchObject({ authorUserId: actorId, authorName: originalRequest.originalActorName });
    expect(currentActorId).not.toBe(actorId);
    expect(evolutionFake.enviados).toHaveLength(providerCallsBeforeRecovery);
  });
});

```

### api-app/test/dispatch-admission.e2e-spec.ts

SHA256 `ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47`. not in inherited dirty-file seal; current exact source supplied, not inferred as newly added.

```typescript
import { INestApplication } from '@nestjs/common';
import { randomUUID } from 'node:crypto';
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from 'vitest';
import type { Prisma } from '@prisma/client';
import { DispatchAdmissionService } from '../src/domain/inbox/dispatch-admission.service';
import { OutboundService } from '../src/domain/inbox/outbound.service';
import { InitialMessageService } from '../src/domain/inbox/initial-message.service';
import { MessageAcceptanceService } from '../src/domain/inbox/message-acceptance.service';
import { sealChannelCredential } from '../src/domain/channels/channel-credential-crypto';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { criarCanalVerificado, criarMantenedora, limparBanco, login, metaFake, subirApp } from './helpers';
import request from 'supertest';
import { RealtimeService } from '../src/realtime/realtime.service';

type TransactionCall = (...args: unknown[]) => Promise<unknown>;

async function withTransactionFault<T>(prisma: PrismaService, mode: 'commit-ack-loss' | 'rollback', action: () => Promise<T>): Promise<T> {
  const target = prisma as unknown as { $transaction: TransactionCall };
  const original = target.$transaction.bind(prisma);
  let injected = false;
  target.$transaction = (...args: unknown[]) => {
    if (injected) return original(...args);
    injected = true;
    if (mode === 'rollback' && typeof args[0] === 'function') {
      const callback = args[0] as (tx: unknown) => Promise<unknown>;
      return original(async (tx: unknown) => {
        await callback(tx);
        throw new Error('synthetic transaction rollback');
      }, ...args.slice(1));
    }
    return original(...args).then(() => { throw new Error('synthetic commit acknowledgment loss'); });
  };
  try { return await action(); }
  finally { target.$transaction = original; }
}

describe('ordinary/initial dispatch admission interlock (PostgreSQL)', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let admission: DispatchAdmissionService;
  let outbound: OutboundService;
  let tenant: Awaited<ReturnType<typeof criarMantenedora>>;
  let conversationId: string;
  let selectedContext: { buId: string; channelId: string; providerResourceIdentityId: string; channelOrigin: 'OFICIAL'; generation: number; pairingEpoch: number; activeCredentialVersion: number; requiresWindow: boolean; providerAccountReference: null };

  beforeAll(async () => {
    ({ app, prisma } = await subirApp());
    admission = app.get(DispatchAdmissionService);
    outbound = app.get(OutboundService);
  });

  afterAll(async () => {
    if (prisma) await limparBanco(prisma);
    await app?.close();
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    tenant = await criarMantenedora(app, 'Dispatch admission', 'dispatch-admission@example.test');
    const { channel, identity } = await criarCanalVerificado(prisma, tenant.businessUnit.id, 'OFICIAL', `dispatch-resource-${randomUUID()}`);
    selectedContext = {
      buId: tenant.businessUnit.id, channelId: channel.id, providerResourceIdentityId: identity.id,
      channelOrigin: 'OFICIAL', generation: channel.generation, pairingEpoch: channel.pairingEpoch,
      activeCredentialVersion: 1, requiresWindow: true, providerAccountReference: null,
    };
    const conversation = await prisma.conversation.create({ data: {
      buId: tenant.businessUnit.id, contact: '5511987654321', contactType: 'PESSOA', status: 'QUEUED',
    } });
    conversationId = conversation.id;
  });

  const ordinary = (caller: 'BFF' | 'PUBLIC' | 'BOT' = 'BFF', actorId = 'owner-user') => admission.reserveOrdinary({
    conversationId, buId: tenant.businessUnit.id, caller, actorId, ownerNonce: randomUUID(), selectedContext,
  });

  const initial = async (ownerNonce = randomUUID(), key = randomUUID()) => {
    const original = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
    return admission.reserveInitial({
      conversationId, buId: tenant.businessUnit.id, contact: '5511987654321', actorId: tenant.owner.id, idempotencyKey: key, ownerNonce,
      selectedContext, requestFingerprint: 'fingerprint-1', request: {
        canonicalRequest: { kind: 'text', text: 'First contact', recipient: '5511987654321' },
        originalConversation: { updatedAt: original.updatedAt.toISOString(), status: original.status, attendantUserId: original.attendantUserId,
          attendantName: original.attendantName, attendantOrigin: original.attendantOrigin },
        renderedText: 'First contact', originalActorName: 'Operator',
      },
    });
  };

  it('keeps Prisma-representable and intentional SQL-only admission indexes explicit', async () => {
    const rows = await prisma.$queryRaw<Array<{ indexname: string; indexdef: string }>>`
      SELECT indexname, indexdef FROM pg_indexes
      WHERE schemaname = current_schema() AND indexname IN (
        'initial_message_intents_actor_rate_idx',
        'initial_message_intents_active_conversation_key',
        'initial_message_intents_account_rate_idx',
        'messages_conversation_trusted_window_idx',
        'conversations_inbox_order_idx'
      ) ORDER BY indexname`;
    expect(rows.map((row) => row.indexname)).toEqual([
      'conversations_inbox_order_idx',
      'initial_message_intents_account_rate_idx',
      'initial_message_intents_active_conversation_key',
      'initial_message_intents_actor_rate_idx',
      'messages_conversation_trusted_window_idx',
    ]);
    const byName = Object.fromEntries(rows.map((row) => [row.indexname, row.indexdef]));
    expect(byName.initial_message_intents_actor_rate_idx).toMatch(/actor_id.*created_at DESC/i);
    expect(byName.initial_message_intents_active_conversation_key).toMatch(/UNIQUE.*conversation_id.*WHERE.*slot_released_at.*IS NULL/i);
    expect(byName.initial_message_intents_account_rate_idx).toMatch(/selected_context.*providerAccountReference.*providerResourceIdentityId/i);
    expect(byName.conversations_inbox_order_idx).toMatch(/bu_id.*contact_type.*COALESCE\(last_message_at, created_at\).*DESC.*id DESC/i);
    expect(byName.messages_conversation_trusted_window_idx).toMatch(/conversation_id.*provider_resource_identity_id.*direction.*channel_origin.*official_inbound_at.*id/i);
    const columns = await prisma.$queryRaw<Array<{ column_name: string; data_type: string; is_nullable: string }>>`
      SELECT column_name, data_type, is_nullable FROM information_schema.columns
      WHERE table_schema = current_schema() AND table_name = 'initial_message_intents'
      AND column_name IN ('request', 'selected_context', 'dispatch_deadline_at', 'external_message_id', 'slot_released_at', 'risk_acknowledged_at')
      ORDER BY column_name`;
    expect(columns).toEqual([
      { column_name: 'dispatch_deadline_at', data_type: 'timestamp without time zone', is_nullable: 'YES' },
      { column_name: 'external_message_id', data_type: 'text', is_nullable: 'YES' },
      { column_name: 'request', data_type: 'jsonb', is_nullable: 'NO' },
      { column_name: 'risk_acknowledged_at', data_type: 'timestamp without time zone', is_nullable: 'YES' },
      { column_name: 'selected_context', data_type: 'jsonb', is_nullable: 'NO' },
      { column_name: 'slot_released_at', data_type: 'timestamp without time zone', is_nullable: 'YES' },
    ]);
    const enumLabels = await prisma.$queryRaw<Array<{ typname: string; enumlabel: string }>>`
      SELECT t.typname, e.enumlabel FROM pg_type t JOIN pg_enum e ON e.enumtypid = t.oid
      WHERE t.typname IN ('InitialMessageIntentState', 'DispatchAdmissionState', 'DispatchAdmissionCaller')
      ORDER BY t.typname, e.enumsortorder`;
    expect(enumLabels.map(({ typname, enumlabel }) => `${typname}:${enumlabel}`)).toEqual([
      'DispatchAdmissionCaller:BFF', 'DispatchAdmissionCaller:PUBLIC', 'DispatchAdmissionCaller:BOT',
      'DispatchAdmissionState:PREPARED', 'DispatchAdmissionState:SENDING', 'DispatchAdmissionState:SETTLED', 'DispatchAdmissionState:UNCERTAIN',
      'InitialMessageIntentState:PREPARED', 'InitialMessageIntentState:SENDING', 'InitialMessageIntentState:EXTERNAL_ACCEPTED',
      'InitialMessageIntentState:EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'InitialMessageIntentState:SUCCEEDED', 'InitialMessageIntentState:REJECTED',
      'InitialMessageIntentState:AMBIGUOUS',
    ]);
    const constraints = await prisma.$queryRaw<Array<{ conname: string; contype: string }>>`
      SELECT conname, contype FROM pg_constraint
      WHERE conrelid = 'initial_message_intents'::regclass AND conname IN (
        'initial_message_intents_pkey', 'initial_message_intents_conversation_id_fkey'
      ) ORDER BY conname`;
    expect(constraints).toEqual([
      { conname: 'initial_message_intents_conversation_id_fkey', contype: 'f' },
      { conname: 'initial_message_intents_pkey', contype: 'p' },
    ]);
    const companionColumns = await prisma.$queryRaw<Array<{ table_name: string; column_name: string; data_type: string; datetime_precision: number | null; is_nullable: string }>>`
      SELECT table_name, column_name, data_type, datetime_precision, is_nullable FROM information_schema.columns
      WHERE table_schema = current_schema() AND (
        (table_name = 'dispatch_admissions' AND column_name IN ('selected_context', 'expires_at', 'dispatch_deadline_at', 'released_at')) OR
        (table_name = 'messages' AND column_name = 'official_inbound_at')
      ) ORDER BY table_name, column_name`;
    expect(companionColumns).toEqual([
      { table_name: 'dispatch_admissions', column_name: 'dispatch_deadline_at', data_type: 'timestamp without time zone', datetime_precision: 3, is_nullable: 'YES' },
      { table_name: 'dispatch_admissions', column_name: 'expires_at', data_type: 'timestamp without time zone', datetime_precision: 3, is_nullable: 'NO' },
      { table_name: 'dispatch_admissions', column_name: 'released_at', data_type: 'timestamp without time zone', datetime_precision: 3, is_nullable: 'YES' },
      { table_name: 'dispatch_admissions', column_name: 'selected_context', data_type: 'jsonb', datetime_precision: null, is_nullable: 'NO' },
      { table_name: 'messages', column_name: 'official_inbound_at', data_type: 'timestamp without time zone', datetime_precision: 3, is_nullable: 'YES' },
    ]);
    const dispatchConstraints = await prisma.$queryRaw<Array<{ conname: string; contype: string }>>`
      SELECT conname, contype FROM pg_constraint WHERE conrelid = 'dispatch_admissions'::regclass
      AND conname IN ('dispatch_admissions_pkey', 'dispatch_admissions_conversation_id_fkey') ORDER BY conname`;
    expect(dispatchConstraints).toEqual([
      { conname: 'dispatch_admissions_conversation_id_fkey', contype: 'f' },
      { conname: 'dispatch_admissions_pkey', contype: 'p' },
    ]);
  });

  it('distinguishes a committed reservation with lost ACK from a rolled-back reservation', async () => {
    const committed = await withTransactionFault(prisma, 'commit-ack-loss', () => initial());
    expect(committed).toMatchObject({ created: true, intent: { state: 'PREPARED', ownerNonce: committed.ownerNonce } });
    expect(await prisma.initialMessageIntent.count({ where: { id: committed.intent.id } })).toBe(1);
    expect(await admission.rejectPreparedInitial({ id: committed.intent.id, ownerNonce: committed.ownerNonce })).toBe(true);

    await expect(withTransactionFault(prisma, 'rollback', () => initial())).rejects.toThrow('synthetic transaction rollback');
    expect(await prisma.initialMessageIntent.count({ where: { conversationId } })).toBe(1);
  });

  it('positively reads back a committed claim after ACK loss and leaves a rolled-back claim PREPARED', async () => {
    const committed = await initial();
    await expect(withTransactionFault(prisma, 'commit-ack-loss', () => admission.claimInitial({
      id: committed.intent.id, ownerNonce: committed.ownerNonce, validate: async () => true,
    }))).resolves.toBe(true);
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: committed.intent.id } })).toMatchObject({ state: 'SENDING', dispatchDeadlineAt: expect.any(Date) });

    await limparBanco(prisma);
    tenant = await criarMantenedora(app, 'Dispatch claim rollback', `dispatch-claim-${randomUUID()}@example.test`);
    const created = await criarCanalVerificado(prisma, tenant.businessUnit.id, 'OFICIAL', `dispatch-resource-${randomUUID()}`);
    selectedContext = { buId: tenant.businessUnit.id, channelId: created.channel.id, providerResourceIdentityId: created.identity.id,
      channelOrigin: 'OFICIAL', generation: created.channel.generation, pairingEpoch: created.channel.pairingEpoch,
      activeCredentialVersion: 1, requiresWindow: true, providerAccountReference: null };
    conversationId = (await prisma.conversation.create({ data: { buId: tenant.businessUnit.id, contact: '5511987654321', contactType: 'PESSOA', status: 'QUEUED' } })).id;
    const rolledBack = await initial();
    await expect(withTransactionFault(prisma, 'rollback', () => admission.claimInitial({
      id: rolledBack.intent.id, ownerNonce: rolledBack.ownerNonce, validate: async () => true,
    }))).resolves.toBe(false);
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: rolledBack.intent.id } })).toMatchObject({ state: 'PREPARED', dispatchDeadlineAt: null, slotReleasedAt: null });
  });

  it('reads back receipt commit after ACK loss and preserves SENDING after real rollback', async () => {
    const committed = await initial();
    await admission.claimInitial({ id: committed.intent.id, ownerNonce: committed.ownerNonce, validate: async () => true });
    await expect(withTransactionFault(prisma, 'commit-ack-loss', () => admission.recordInitialExternalAccepted({
      id: committed.intent.id, ownerNonce: committed.ownerNonce, externalMessageId: 'receipt-commit-ack-loss',
    }))).resolves.toBe(true);
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: committed.intent.id } })).toMatchObject({
      state: 'EXTERNAL_ACCEPTED', externalMessageId: 'receipt-commit-ack-loss', slotReleasedAt: null,
    });

    await limparBanco(prisma);
    tenant = await criarMantenedora(app, 'Dispatch receipt rollback', `dispatch-receipt-${randomUUID()}@example.test`);
    const created = await criarCanalVerificado(prisma, tenant.businessUnit.id, 'OFICIAL', `dispatch-resource-${randomUUID()}`);
    selectedContext = { buId: tenant.businessUnit.id, channelId: created.channel.id, providerResourceIdentityId: created.identity.id,
      channelOrigin: 'OFICIAL', generation: created.channel.generation, pairingEpoch: created.channel.pairingEpoch,
      activeCredentialVersion: 1, requiresWindow: true, providerAccountReference: null };
    conversationId = (await prisma.conversation.create({ data: { buId: tenant.businessUnit.id, contact: '5511987654321', contactType: 'PESSOA', status: 'QUEUED' } })).id;
    const rolledBack = await initial();
    await admission.claimInitial({ id: rolledBack.intent.id, ownerNonce: rolledBack.ownerNonce, validate: async () => true });
    await expect(withTransactionFault(prisma, 'rollback', () => admission.recordInitialExternalAccepted({
      id: rolledBack.intent.id, ownerNonce: rolledBack.ownerNonce, externalMessageId: 'receipt-rolled-back',
    }))).rejects.toThrow('synthetic transaction rollback');
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: rolledBack.intent.id } })).toMatchObject({
      state: 'SENDING', externalMessageId: null, slotReleasedAt: null,
    });
  });

  it('reads back a committed prepared release after ACK loss and leaves a rolled-back release untouched', async () => {
    const committed = await initial();
    await expect(withTransactionFault(prisma, 'commit-ack-loss', () => admission.rejectPreparedInitial({
      id: committed.intent.id, ownerNonce: committed.ownerNonce,
    }))).resolves.toBe(true);
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: committed.intent.id } })).toMatchObject({ state: 'REJECTED', slotReleasedAt: expect.any(Date) });

    await limparBanco(prisma);
    tenant = await criarMantenedora(app, 'Dispatch release rollback', `dispatch-release-${randomUUID()}@example.test`);
    const created = await criarCanalVerificado(prisma, tenant.businessUnit.id, 'OFICIAL', `dispatch-resource-${randomUUID()}`);
    selectedContext = { buId: tenant.businessUnit.id, channelId: created.channel.id, providerResourceIdentityId: created.identity.id,
      channelOrigin: 'OFICIAL', generation: created.channel.generation, pairingEpoch: created.channel.pairingEpoch,
      activeCredentialVersion: 1, requiresWindow: true, providerAccountReference: null };
    conversationId = (await prisma.conversation.create({ data: { buId: tenant.businessUnit.id, contact: '5511987654321', contactType: 'PESSOA', status: 'QUEUED' } })).id;
    const rolledBack = await initial();
    await expect(withTransactionFault(prisma, 'rollback', () => admission.rejectPreparedInitial({
      id: rolledBack.intent.id, ownerNonce: rolledBack.ownerNonce,
    }))).rejects.toThrow('synthetic transaction rollback');
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: rolledBack.intent.id } })).toMatchObject({ state: 'PREPARED', slotReleasedAt: null });
  });

  it('commits irreversible risk release and its audit together across ACK loss, and rolls both back together', async () => {
    const committed = await initial();
    await admission.claimInitial({ id: committed.intent.id, ownerNonce: committed.ownerNonce, validate: async () => true });
    await admission.markInitialAmbiguous({ id: committed.intent.id, ownerNonce: committed.ownerNonce });
    await prisma.initialMessageIntent.update({ where: { id: committed.intent.id }, data: { dispatchDeadlineAt: new Date(Date.now() - 1000) } });
    const audit = async (tx: Prisma.TransactionClient) => {
      await tx.webhookEvent.create({ data: { channel: 'OFICIAL', buId: tenant.businessUnit.id,
        eventType: 'test.initial.risk_ack', payload: { attemptId: committed.intent.id } } });
    };
    await expect(withTransactionFault(prisma, 'commit-ack-loss', () => admission.acknowledgeInitialRisk({
      id: committed.intent.id, ownerNonce: committed.ownerNonce, actorId: tenant.owner.id,
      validateActor: async () => true, audit,
    }))).resolves.toBe(true);
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: committed.intent.id } })).toMatchObject({
      state: 'AMBIGUOUS', slotReleasedAt: expect.any(Date), riskAcknowledgedAt: expect.any(Date),
    });
    expect(await prisma.webhookEvent.count({ where: { eventType: 'test.initial.risk_ack' } })).toBe(1);

    await limparBanco(prisma);
    tenant = await criarMantenedora(app, 'Dispatch risk rollback', `dispatch-risk-${randomUUID()}@example.test`);
    const created = await criarCanalVerificado(prisma, tenant.businessUnit.id, 'OFICIAL', `dispatch-resource-${randomUUID()}`);
    selectedContext = { buId: tenant.businessUnit.id, channelId: created.channel.id, providerResourceIdentityId: created.identity.id,
      channelOrigin: 'OFICIAL', generation: created.channel.generation, pairingEpoch: created.channel.pairingEpoch,
      activeCredentialVersion: 1, requiresWindow: true, providerAccountReference: null };
    conversationId = (await prisma.conversation.create({ data: { buId: tenant.businessUnit.id, contact: '5511987654321', contactType: 'PESSOA', status: 'QUEUED' } })).id;
    const rolledBack = await initial();
    await admission.claimInitial({ id: rolledBack.intent.id, ownerNonce: rolledBack.ownerNonce, validate: async () => true });
    await admission.markInitialAmbiguous({ id: rolledBack.intent.id, ownerNonce: rolledBack.ownerNonce });
    await prisma.initialMessageIntent.update({ where: { id: rolledBack.intent.id }, data: { dispatchDeadlineAt: new Date(Date.now() - 1000) } });
    const rollbackAudit = async (tx: Prisma.TransactionClient) => {
      await tx.webhookEvent.create({ data: { channel: 'OFICIAL', buId: tenant.businessUnit.id,
        eventType: 'test.initial.risk_ack', payload: { attemptId: rolledBack.intent.id } } });
    };
    await expect(withTransactionFault(prisma, 'rollback', () => admission.acknowledgeInitialRisk({
      id: rolledBack.intent.id, ownerNonce: rolledBack.ownerNonce, actorId: tenant.owner.id,
      validateActor: async () => true, audit: rollbackAudit,
    }))).rejects.toThrow('synthetic transaction rollback');
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: rolledBack.intent.id } })).toMatchObject({ slotReleasedAt: null, riskAcknowledgedAt: null });
    expect(await prisma.webhookEvent.count({ where: { eventType: 'test.initial.risk_ack' } })).toBe(0);
  });

  it('enforces the actor and canonical account rate windows across released reservations', async () => {
    const reserveAs = (actorId: string) => admission.reserveInitial({
      conversationId, buId: tenant.businessUnit.id, contact: '5511987654321', actorId,
      idempotencyKey: randomUUID(), ownerNonce: randomUUID(), selectedContext,
      requestFingerprint: 'rate-window-fixture', request: {
        canonicalRequest: { kind: 'text', text: 'rate-window', recipient: '5511987654321' },
        originalConversation: { updatedAt: new Date().toISOString(), status: 'QUEUED', attendantUserId: null, attendantName: null, attendantOrigin: null },
        renderedText: 'rate-window', originalActorName: 'Fixture',
      },
    });
    const reserveAndRelease = async (actorId: string) => {
      const reserved = await reserveAs(actorId);
      expect(await admission.rejectPreparedInitial({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce })).toBe(true);
    };
    for (let index = 0; index < 10; index += 1) await reserveAndRelease('actor-rate-limited');
    await expect(reserveAs('actor-rate-limited')).rejects.toMatchObject({ response: { code: 'INITIAL_RATE_LIMIT' } });
    for (let index = 0; index < 50; index += 1) await reserveAndRelease(`distinct-account-actor-${index}`);
    await expect(reserveAs('account-limit-next-actor')).rejects.toMatchObject({ response: { code: 'INITIAL_RATE_LIMIT' } });
    expect(await prisma.initialMessageIntent.count({ where: { buId: tenant.businessUnit.id } })).toBe(60);

    const sharedAccountReference = 'opaque-shared-account-rate-fixture';
    const seedContext = { ...selectedContext, providerAccountReference: sharedAccountReference };
    const now = new Date();
    await prisma.initialMessageIntent.createMany({ data: Array.from({ length: 60 }, (_, index) => ({
      conversationId, buId: tenant.businessUnit.id, actorId: `foreign-account-seed-${index}`,
      idempotencyKey: randomUUID(), ownerNonce: randomUUID(), requestFingerprint: 'shared-account-seed',
      request: { canonicalRequest: { kind: 'text', text: 'seed', recipient: '5511987654321' } } as Prisma.InputJsonValue,
      selectedContext: seedContext as unknown as Prisma.InputJsonValue, state: 'REJECTED' as const,
      leaseExpiresAt: now, slotReleasedAt: now, createdAt: now, updatedAt: now,
    })) });
    const otherTenant = await criarMantenedora(app, 'Shared account tenant', `shared-account-${randomUUID()}@example.test`);
    const otherChannel = await criarCanalVerificado(prisma, otherTenant.businessUnit.id, 'OFICIAL', `shared-account-${randomUUID()}`);
    const otherConversation = await prisma.conversation.create({ data: { buId: otherTenant.businessUnit.id,
      contact: '5511987654321', contactType: 'PESSOA', status: 'QUEUED' } });
    tenant = otherTenant;
    conversationId = otherConversation.id;
    selectedContext = { buId: otherTenant.businessUnit.id, channelId: otherChannel.channel.id,
      providerResourceIdentityId: otherChannel.identity.id, channelOrigin: 'OFICIAL', generation: otherChannel.channel.generation,
      pairingEpoch: otherChannel.channel.pairingEpoch, activeCredentialVersion: 1, requiresWindow: true,
      providerAccountReference: sharedAccountReference };
    await expect(reserveAs('cross-tenant-shared-account-actor')).rejects.toMatchObject({ response: { code: 'INITIAL_RATE_LIMIT' } });
  });

  it('keeps multiple ordinary provider phases open without holding the conversation lock over them', async () => {
    const tokens = await Promise.all([
      ordinary('BFF', 'user-a'), ordinary('PUBLIC', 'key-a'), ordinary('BOT', 'bot-a'),
    ]);
    let releaseProviderStages!: () => void;
    const providerStages = new Promise<void>((resolve) => { releaseProviderStages = resolve; });
    let notifyClaimsComplete!: () => void;
    const allClaimsComplete = new Promise<void>((resolve) => { notifyClaimsComplete = resolve; });
    let completedClaims = 0;
    let claimFailure: unknown;
    const providerOperations = tokens.map(async ({ admission: token, ownerNonce }) => {
      let claimed = false;
      try {
        claimed = await admission.claimOrdinary({ id: token.id, ownerNonce, validate: async () => true });
      } catch (error) {
        claimFailure ??= error;
      } finally {
        completedClaims += 1;
        if (completedClaims === tokens.length) notifyClaimsComplete();
      }
      if (claimed) await providerStages;
      return claimed;
    });
    try {
      await allClaimsComplete;
      expect(claimFailure).toBeUndefined();
      expect(await prisma.dispatchAdmission.count({ where: { conversationId, state: 'SENDING', releasedAt: null } })).toBe(3);

      // Each owner is now paused after its committed claim, as it would be during
      // its provider call. The next reservation must finish without their locks.
      const fourth = await ordinary('BFF', 'user-d');
      expect(fourth.admission.state).toBe('PREPARED');
      expect(await prisma.dispatchAdmission.count({ where: { conversationId, state: 'SENDING', releasedAt: null } })).toBe(3);
    } finally {
      releaseProviderStages();
      await Promise.allSettled(providerOperations);
    }
  });

  it('excludes initial reservation behind any ordinary token, including expired SENDING uncertainty', async () => {
    const { admission: token, ownerNonce } = await ordinary();
    await expect(initial()).rejects.toMatchObject({ response: { code: 'ORDINARY_SEND_IN_PROGRESS', outcome: 'BLOCKED', ordinaryAdmissions: [{ id: token.id, state: 'PREPARED' }], admissionsTruncated: false } });
    await expect(admission.claimOrdinary({ id: token.id, ownerNonce, validate: async () => true })).resolves.toBe(true);
    await prisma.dispatchAdmission.update({ where: { id: token.id }, data: { expiresAt: new Date(Date.now() - 1000) } });
    await admission.settleOrdinary({ id: token.id, ownerNonce, state: 'UNCERTAIN' });
    await expect(initial()).rejects.toMatchObject({ response: { code: 'ORDINARY_SEND_IN_PROGRESS', outcome: 'BLOCKED', ordinaryAdmissions: [{ id: token.id, state: 'UNCERTAIN' }], admissionsTruncated: false } });
    expect(await prisma.dispatchAdmission.findUniqueOrThrow({ where: { id: token.id } })).toMatchObject({
      state: 'UNCERTAIN', releasedAt: null,
    });
  });

  it('excludes a new ordinary send behind an active initial slot and keeps idempotent replay on its captured owner', async () => {
    const capturedOwner = randomUUID();
    const created = await initial(capturedOwner);
    expect(created).toMatchObject({ created: true, ownerNonce: capturedOwner, intent: { ownerNonce: capturedOwner, state: 'PREPARED' } });
    await expect(ordinary()).rejects.toMatchObject({ response: { code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: created.intent.id, state: 'PREPARED' } });

    const replayOwner = randomUUID();
    const replay = await initial(replayOwner, created.intent.idempotencyKey);
    expect(replay).toMatchObject({ created: false, ownerNonce: replayOwner, intent: { id: created.intent.id, ownerNonce: capturedOwner } });
  });

  it('rechecks database time after delayed preflight so an expired PREPARED token cannot claim or POST', async () => {
    const { admission: token, ownerNonce } = await ordinary();
    const deadline = new Date(Date.now() + 300);
    await prisma.dispatchAdmission.update({ where: { id: token.id }, data: { expiresAt: deadline } });
    let providerPostCount = 0;
    const claimed = await admission.claimOrdinary({
      id: token.id,
      ownerNonce,
      validate: async () => {
        await new Promise((resolve) => setTimeout(resolve, 450));
        return true;
      },
    });
    if (claimed) providerPostCount += 1;

    expect(claimed).toBe(false);
    expect(providerPostCount).toBe(0);
    expect(await prisma.dispatchAdmission.findUniqueOrThrow({ where: { id: token.id } })).toMatchObject({
      state: 'PREPARED', dispatchDeadlineAt: null, releasedAt: null,
    });
  });

  it('does not claim an initial attempt after delayed transaction validation crosses its immutable deadline', async () => {
    const { intent } = await initial();
    const deadline = new Date(Date.now() + 300);
    await prisma.initialMessageIntent.update({ where: { id: intent.id }, data: { leaseExpiresAt: deadline } });
    let providerPostCount = 0;
    const claimed = await admission.claimInitial({
      id: intent.id,
      ownerNonce: intent.ownerNonce,
      validate: async () => {
        await new Promise((resolve) => setTimeout(resolve, 450));
        return true;
      },
    });
    if (claimed) providerPostCount += 1;

    expect(claimed).toBe(false);
    expect(providerPostCount).toBe(0);
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: intent.id } })).toMatchObject({
      state: 'PREPARED', dispatchDeadlineAt: null, slotReleasedAt: null,
    });
  });

  it('keeps a late known receipt attached to an irreversibly released owner after a successor reserves', async () => {
    const original = await initial();
    await admission.claimInitial({ id: original.intent.id, ownerNonce: original.ownerNonce, validate: async () => true });
    await prisma.initialMessageIntent.update({ where: { id: original.intent.id }, data: {
      dispatchDeadlineAt: new Date(Date.now() - 1000), state: 'AMBIGUOUS',
    } });
    await expect(admission.acknowledgeInitialRisk({
      id: original.intent.id, ownerNonce: original.ownerNonce, actorId: 'operator-a', validateActor: async () => true,
    })).resolves.toBe(true);

    const successor = await initial(randomUUID(), randomUUID());
    expect(successor.created).toBe(true);
    await expect(admission.recordInitialExternalAccepted({
      id: original.intent.id, ownerNonce: original.ownerNonce, externalMessageId: 'external-late-1',
    })).resolves.toBe(true);
    const [oldOwner, currentOwner] = await Promise.all([
      prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: original.intent.id } }),
      prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: successor.intent.id } }),
    ]);
    expect(oldOwner).toMatchObject({ state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', externalMessageId: 'external-late-1', slotReleasedAt: expect.any(Date) });
    expect(currentOwner).toMatchObject({ state: 'PREPARED', slotReleasedAt: null });
  });

  it('rejects risk acknowledgment before the immutable deadline, then releases exactly once after it', async () => {
    const { intent, ownerNonce } = await initial();
    expect(await admission.claimInitial({ id: intent.id, ownerNonce, validate: async () => true })).toBe(true);
    expect(await admission.markInitialAmbiguous({ id: intent.id, ownerNonce })).toBe(true);
    const deadline = new Date(Date.now() + 350);
    await prisma.initialMessageIntent.update({ where: { id: intent.id }, data: { dispatchDeadlineAt: deadline } });
    const service = app.get(InitialMessageService);
    const request = {
      id: intent.id, conversationId, buId: tenant.businessUnit.id, actorId: tenant.owner.id,
      confirmed: true, validateActorInTransaction: async () => true, auditInTransaction: async () => undefined,
    };
    await expect(service.acknowledge(request)).rejects.toMatchObject({ response: { code: 'ACK_TOO_EARLY', eligibleAt: expect.any(Date) } });
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: intent.id } })).toMatchObject({ slotReleasedAt: null, riskAcknowledgedAt: null });
    await new Promise((resolve) => setTimeout(resolve, 400));
    await expect(service.acknowledge(request)).resolves.toMatchObject({ id: intent.id, state: 'AMBIGUOUS', slotReleasedAt: expect.any(Date) });
    const successor = await initial(randomUUID(), randomUUID());
    expect(successor.created).toBe(true);
    expect(await admission.rejectPreparedInitial({ id: intent.id, ownerNonce })).toBe(false);
    expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: successor.intent.id } })).toMatchObject({ state: 'PREPARED', slotReleasedAt: null });
  });

  it('never releases a persisted SENDING claim through prepared-only cleanup', async () => {
    const reserved = await initial();
    expect(await admission.claimInitial({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, validate: async () => true })).toBe(true);
    expect(await admission.rejectPreparedInitial({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce })).toBe(false);
    const current = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } });
    expect(current).toMatchObject({ state: 'SENDING', dispatchDeadlineAt: expect.any(Date), slotReleasedAt: null });
  });

  it('completes a known first outbound receipt locally through the shared Message owner and reconciles it without network', async () => {
    const reserved = await initial();
    expect(await admission.claimInitial({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, validate: async () => true })).toBe(true);
    const externalMessageId = `initial-external-${randomUUID()}`;
    expect(await admission.recordInitialExternalAccepted({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, externalMessageId })).toBe(true);
    const acceptedIntent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } });
    const credential = await prisma.channelCredential.findUniqueOrThrow({ where: { channelId: selectedContext.channelId } });
    const channel = await prisma.buChannel.findUniqueOrThrow({ where: { id: selectedContext.channelId } });
    const nextVersion = credential.version + 1;
    const envelope = sealChannelCredential('fixture-rotated-token-after-ack', credential.keyId,
      Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY!, 'base64'), {
        purpose: 'active', provider: 'OFICIAL', buId: tenant.businessUnit.id, channelId: channel.id,
        generation: channel.generation, version: nextVersion,
      });
    await prisma.channelCredential.update({ where: { channelId: channel.id }, data: {
      version: nextVersion, nonce: new Uint8Array(envelope.nonce), ciphertext: new Uint8Array(envelope.ciphertext), tag: new Uint8Array(envelope.tag),
    } });
    const providerCallsBefore = metaFake.providerCalls;
    const publish = vi.spyOn(app.get(RealtimeService), 'publicarNaBu');
    try {
      const message = await outbound.reconcileInitial({
        intent: acceptedIntent, actorId: 'currently-authorized-operator', actorName: 'Changed display name',
        validateActorInTransaction: async () => true,
      });
      expect(message).toMatchObject({ externalId: externalMessageId, content: 'First contact', authorUserId: tenant.owner.id, authorName: 'Operator' });
      expect(publish).toHaveBeenCalledTimes(1);
      expect(publish).toHaveBeenCalledWith(tenant.businessUnit.id,
        expect.objectContaining({ tipo: 'mensagem', conversaId: conversationId, direcao: 'OUT' }));
      expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } }))
        .toMatchObject({ state: 'SUCCEEDED', externalMessageId, slotReleasedAt: expect.any(Date) });
      const replay = await outbound.reconcileInitial({
        intent: await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } }),
        actorId: 'currently-authorized-operator', actorName: 'Changed display name', validateActorInTransaction: async () => true,
      });
      expect(replay).toBeNull();
      expect(publish).toHaveBeenCalledTimes(1);
      expect(await prisma.message.count({ where: { providerResourceIdentityId: selectedContext.providerResourceIdentityId, externalId: externalMessageId } })).toBe(1);
      expect(metaFake.providerCalls).toBe(providerCallsBefore);
    } finally {
      publish.mockRestore();
    }
  });

  it('preserves a known receipt across local-completion commit ACK loss and rollback', async () => {
    const exercise = async (mode: 'commit-ack-loss' | 'rollback') => {
      const reserved = await initial();
      expect(await admission.claimInitial({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, validate: async () => true })).toBe(true);
      const externalMessageId = `completion-${mode}-${randomUUID()}`;
      expect(await admission.recordInitialExternalAccepted({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, externalMessageId })).toBe(true);
      const acceptedIntent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } });
      const callsBefore = metaFake.providerCalls;
      const result = withTransactionFault(prisma, mode, () => outbound.reconcileInitial({
        intent: acceptedIntent, actorId: tenant.owner.id, actorName: 'Later operator', validateActorInTransaction: async () => true,
      }));
      if (mode === 'commit-ack-loss') {
        await expect(result).resolves.toMatchObject({ externalId: externalMessageId, content: 'First contact' });
        expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } })).toMatchObject({
          state: 'SUCCEEDED', externalMessageId, slotReleasedAt: expect.any(Date),
        });
        expect(await prisma.message.count({ where: { providerResourceIdentityId: selectedContext.providerResourceIdentityId, externalId: externalMessageId } })).toBe(1);
      } else {
        await expect(result).rejects.toMatchObject({ response: { code: 'INITIAL_LOCAL_ACCEPTANCE_UNCONFIRMED' } });
        expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } })).toMatchObject({
          state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', externalMessageId, slotReleasedAt: null,
        });
        expect(await prisma.message.count({ where: { providerResourceIdentityId: selectedContext.providerResourceIdentityId, externalId: externalMessageId } })).toBe(0);
      }
      expect(metaFake.providerCalls).toBe(callsBefore);
    };

    await exercise('commit-ack-loss');
    await limparBanco(prisma);
    tenant = await criarMantenedora(app, 'Dispatch completion rollback', `dispatch-completion-${randomUUID()}@example.test`);
    const created = await criarCanalVerificado(prisma, tenant.businessUnit.id, 'OFICIAL', `dispatch-resource-${randomUUID()}`);
    selectedContext = { buId: tenant.businessUnit.id, channelId: created.channel.id, providerResourceIdentityId: created.identity.id,
      channelOrigin: 'OFICIAL', generation: created.channel.generation, pairingEpoch: created.channel.pairingEpoch,
      activeCredentialVersion: 1, requiresWindow: true, providerAccountReference: null };
    conversationId = (await prisma.conversation.create({ data: { buId: tenant.businessUnit.id,
      contact: '5511987654321', contactType: 'PESSOA', status: 'QUEUED' } })).id;
    await exercise('rollback');
  });

  it('rolls back the whole initial completion on a real P2002 race, exact-reads back, and retries one local transaction', async () => {
    const reserved = await initial();
    expect(await admission.claimInitial({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, validate: async () => true })).toBe(true);
    const externalMessageId = `initial-race-${randomUUID()}`;
    expect(await admission.recordInitialExternalAccepted({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, externalMessageId })).toBe(true);
    const acceptedIntent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } });
    const acceptance = app.get(MessageAcceptanceService);
    const original = acceptance.acceptInTransaction.bind(acceptance);
    let firstCompletionEntered!: () => void;
    let releaseFirstCompletion!: () => void;
    const entered = new Promise<void>((resolve) => { firstCompletionEntered = resolve; });
    const gate = new Promise<void>((resolve) => { releaseFirstCompletion = resolve; });
    let paused = false;
    const wrapped = vi.spyOn(acceptance, 'acceptInTransaction').mockImplementation(async (tx, input, beforeConversationMutation) => {
      if (input.externalMessageId === externalMessageId && input.senderResult && !paused && beforeConversationMutation) {
        paused = true;
        return original(tx, input, async (transaction, priorExists) => {
          firstCompletionEntered();
          await gate;
          await beforeConversationMutation(transaction, priorExists);
        });
      }
      return original(tx, input, beforeConversationMutation);
    });
    const transactionTarget = prisma as unknown as { $transaction: TransactionCall };
    const transactionOriginal = transactionTarget.$transaction.bind(prisma);
    let transactionCount = 0;
    transactionTarget.$transaction = (...args: unknown[]) => { transactionCount += 1; return transactionOriginal(...args); };
    let reconciliation: Promise<unknown> | null = null;
    try {
      reconciliation = outbound.reconcileInitial({ intent: acceptedIntent, actorId: tenant.owner.id, actorName: 'Later operator',
        validateActorInTransaction: async () => true });
      await entered;
      const echo = await acceptance.accept({
        externalMessageId, providerResourceIdentityId: selectedContext.providerResourceIdentityId,
        channelId: selectedContext.channelId, generation: selectedContext.generation, pairingEpoch: selectedContext.pairingEpoch,
        buId: tenant.businessUnit.id, channelOrigin: 'OFICIAL', contact: '5511987654321', contactType: 'PESSOA',
        conversationId, direction: 'OUT', messageType: 'TEXTO', content: 'First contact', authorUserId: null,
        authorName: null, senderResult: false,
      });
      expect(echo.creationWinner).toBe(true);
      releaseFirstCompletion();
      const completed = await reconciliation;
      expect(completed).toMatchObject({ externalId: externalMessageId, content: 'First contact' });
      expect(wrapped).toHaveBeenCalledTimes(3);
      expect(transactionCount).toBe(3);
      expect(await prisma.message.count({ where: { providerResourceIdentityId: selectedContext.providerResourceIdentityId, externalId: externalMessageId } })).toBe(1);
      expect(await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } })).toMatchObject({ state: 'SUCCEEDED', externalMessageId });
      expect(metaFake.providerCalls).toBe(0);
    } finally {
      releaseFirstCompletion();
      if (reconciliation) await reconciliation.catch(() => undefined);
      wrapped.mockRestore();
      transactionTarget.$transaction = transactionOriginal;
    }
  });

  it('does not assign or reopen the conversation when the accepted external key already has an echo row', async () => {
    const reserved = await initial();
    expect(await admission.claimInitial({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, validate: async () => true })).toBe(true);
    const externalMessageId = `initial-echo-${randomUUID()}`;
    expect(await admission.recordInitialExternalAccepted({ id: reserved.intent.id, ownerNonce: reserved.ownerNonce, externalMessageId })).toBe(true);
    const before = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
    await prisma.message.create({ data: {
      conversationId, buId: tenant.businessUnit.id, direction: 'OUT', messageType: 'TEXTO', content: 'First contact',
      channelOrigin: 'OFICIAL', status: 'ENVIADA', externalId: externalMessageId,
      providerResourceIdentityId: selectedContext.providerResourceIdentityId,
      authorUserId: tenant.owner.id, authorName: 'Operator',
    } });
    const acceptedIntent = await prisma.initialMessageIntent.findUniqueOrThrow({ where: { id: reserved.intent.id } });

    const providerCallsBefore = metaFake.providerCalls;
    const publish = vi.spyOn(app.get(RealtimeService), 'publicarNaBu');
    try {
      await outbound.reconcileInitial({ intent: acceptedIntent, actorId: tenant.owner.id, actorName: 'Operator', validateActorInTransaction: async () => true });
      expect(publish).not.toHaveBeenCalled();
    } finally {
      publish.mockRestore();
    }

    const after = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
    expect(after.updatedAt).toEqual(before.updatedAt);
    expect(after.status).toBe('QUEUED');
    expect(after.attendantUserId).toBeNull();
    expect(after.attendantName).toBeNull();
    expect(after.attendantOrigin).toBeNull();
    expect(await prisma.message.count({ where: { providerResourceIdentityId: selectedContext.providerResourceIdentityId, externalId: externalMessageId } })).toBe(1);
    expect(metaFake.providerCalls).toBe(providerCallsBefore);
  });

  it('does not report full ordinary-send success when settlement rolls back after ACK and Message acceptance', async () => {
    await prisma.message.create({ data: {
      conversationId, buId: tenant.businessUnit.id, direction: 'IN', messageType: 'TEXTO', content: 'trusted inbound fixture',
      channelOrigin: 'OFICIAL', status: 'RECEBIDA', externalId: `ordinary-window-${randomUUID()}`,
      providerResourceIdentityId: selectedContext.providerResourceIdentityId, officialInboundAt: new Date(),
    } });
    const cookie = await login(app, 'dispatch-admission@example.test');
    const settleOriginal = admission.settleOrdinary.bind(admission);
    const settle = vi.spyOn(admission, 'settleOrdinary').mockImplementation((input) =>
      input.state === 'SETTLED'
        ? withTransactionFault(prisma, 'rollback', () => settleOriginal(input))
        : settleOriginal(input));
    const providerBefore = metaFake.providerCalls;
    let response: { status: number; body: Record<string, unknown> };
    try {
      response = await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'ordinary accepted before settlement rollback' });
    } finally {
      settle.mockRestore();
    }
    expect(response!.status).not.toBe(201);
    expect(response!.body).toMatchObject({ outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState: 'RECORDED' });
    expect(metaFake.providerCalls).toBe(providerBefore + 1);
    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(1);
    expect(await prisma.dispatchAdmission.count({ where: { conversationId, state: 'SENDING' } })).toBe(1);
  });
});

```

### api-app/src/surfaces/bff/bff.module.ts

SHA256 `8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a`. changed since exact pre-ST04 seal within admitted mutation scope.

```typescript
import { MiddlewareConsumer, Module, NestModule, RequestMethod } from '@nestjs/common';
import { AccessService } from '../../domain/access/access.service';
import { IdentityService } from '../../domain/identity/identity.service';
import { LoginAttemptService } from '../../domain/identity/login-attempt.service';
import { PasswordService } from '../../domain/identity/password.service';
import { SessionService } from '../../infra/session/session.service';
import { ChannelsService } from '../../domain/channels/channels.service';
import { NumberRegistrationService } from '../../domain/channels/number-registration.service';
import { NumberRegistrationsController } from './number-registrations.controller';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { ConversationStartService } from '../../domain/inbox/conversation-start.service';
import { InitialMessageService } from '../../domain/inbox/initial-message.service';
import { HistoricoService } from '../../domain/inbox/historico.service';
import { ApiKeyService } from '../../domain/integration/api-key.service';
import { TenancyService } from '../../domain/tenancy/tenancy.service';
import { ModulosService } from '../../domain/produto/modulos.service';
import { SetorService } from '../../domain/setor/setor.service';
import { RegistroDeAtividade } from '../../domain/historico/registro.service';
import { AtividadesService } from '../../domain/historico/atividades.service';
import { OnboardingService } from '../../domain/produto/onboarding.service';
import { PainelService } from '../../domain/painel/painel.service';
import { ArmazenamentoDeArquivo, ArmazenamentoEmDisco } from '../../infra/arquivos/armazenamento';
import { EnvioDeEmail, ResendEmail } from '../../integrations/email/email.client';
import { TokensService } from '../../domain/acesso/tokens.service';
import { ConvitesService } from '../../domain/acesso/convites.service';
import { LimiteDeRecuperacao } from '../../domain/acesso/limite-de-recuperacao.service';
import { ChannelTransportModule } from '../../integrations/channels/channel-transport.module';
import { AuthController } from './auth.controller';
import { ChannelsController } from './channels.controller';
import { ConversationsController } from './conversations.controller';
import { UsuariosService } from '../../domain/identity/usuarios.service';
import { HistoricoController } from './historico.controller';
import { UsuariosController } from './usuarios.controller';
import { IntegracaoController } from './integracao.controller';
import { BusinessUnitsController, MeController } from './me.controller';
import { SetoresController } from './setores.controller';
import { AtividadesController } from './atividades.controller';
import { OnboardingController } from './onboarding.controller';
import { PainelController } from './painel.controller';
import { ArquivosController } from './arquivos.controller';
import { SessionMiddleware } from './session.middleware';
import { TYPEBOT_CLIENT, TypebotHttpClient } from '../../integrations/typebot/typebot.client';
import { TemplateManagementModule } from '../../integrations/message-templates/template-management.module';
import { TemplateDraftService } from '../../domain/message-templates/template-draft.service';
import { TemplateSubmissionService } from '../../domain/message-templates/template-submission.service';
import { PrismaTemplateTransactionBoundary, TEMPLATE_TRANSACTION_BOUNDARY } from '../../domain/message-templates/template-transaction-boundary';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { MessageTemplatesController } from './message-templates.controller';
import { TEMPLATE_OBSERVATION_CLOCK, TemplateObservationService } from '../../domain/message-templates/template-observation.service';

/**
 * Superfície BFF (ADR-0006): o que as telas consomem, autenticado por sessão.
 *
 * O middleware é montado no PREFIXO. É isso que faz o guard ser da superfície e
 * não da rota, e é o que impede o defeito que já mordeu os dois sistemas: no
 * Hub, um router.use(requireAuth) sem path interceptou o webhook público.
 */
@Module({
  imports: [ChannelTransportModule, TemplateManagementModule],
  controllers: [
    AuthController,
    MeController,
    BusinessUnitsController,
    ChannelsController,
    NumberRegistrationsController,
    ConversationsController,
    IntegracaoController,
    HistoricoController,
    UsuariosController,
    SetoresController,
    AtividadesController,
    OnboardingController,
    PainelController,
    ArquivosController,
    MessageTemplatesController,
  ],
  providers: [
    SessionService,
    IdentityService,
    PasswordService,
    LoginAttemptService,
    AccessService,
    TemplateDraftService,
    TemplateSubmissionService,
    TemplateObservationService,
    { provide: TEMPLATE_OBSERVATION_CLOCK, useValue: { now: () => new Date() } },
    { provide: TEMPLATE_TRANSACTION_BOUNDARY, useFactory: (prisma: PrismaService) => new PrismaTemplateTransactionBoundary(prisma), inject: [PrismaService] },
    ChannelsService,
    NumberRegistrationService,
    ConversationsService,
    ConversationStartService,
    InitialMessageService,
    HistoricoService,
    UsuariosService,
    ApiKeyService,
    TenancyService,
    ModulosService,
    SetorService,
    RegistroDeAtividade,
    AtividadesService,
    OnboardingService,
    PainelService,
    { provide: ArmazenamentoDeArquivo, useClass: ArmazenamentoEmDisco },
    { provide: EnvioDeEmail, useClass: ResendEmail },
    TokensService,
    ConvitesService,
    LimiteDeRecuperacao,
    // Adaptadores de SAÍDA por porta (ADR-0006, Emenda 1): o domínio depende da
    // interface, não do HTTP. É o que deixa o teste provar permissão sem a Meta
    // nem a Evolution no ar.
    { provide: TYPEBOT_CLIENT, useClass: TypebotHttpClient },
  ],
  exports: [SessionService, PasswordService],
})
export class BffModule implements NestModule {
  configure(consumer: MiddlewareConsumer): void {
    consumer
      .apply(SessionMiddleware)
      .forRoutes({ path: 'api/bff/{*path}', method: RequestMethod.ALL });
  }
}

```

### api-app/src/integrations/message-templates/template-management.module.ts

SHA256 `aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd`. unchanged inherited pre-ST04 bytes.

```typescript
import { Module } from '@nestjs/common';
import { TEMPLATE_MANAGEMENT_RESOLVER } from '../../domain/message-templates/template-management.ports';
import { ChannelTransportModule } from '../channels/channel-transport.module';
import { ScopedTemplateManagementResolver } from './template-management.resolver';

@Module({
  imports: [ChannelTransportModule],
  providers: [
    ScopedTemplateManagementResolver,
    { provide: TEMPLATE_MANAGEMENT_RESOLVER, useExisting: ScopedTemplateManagementResolver },
  ],
  exports: [TEMPLATE_MANAGEMENT_RESOLVER],
})
export class TemplateManagementModule {}

```

### api-app/src/domain/channels/transport/channel-dependencies.spec.ts

SHA256 `f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3`. unchanged inherited pre-ST04 bytes.

```typescript
import { readdirSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

const inboxDirectory = resolve(dirname(fileURLToPath(import.meta.url)), '../../inbox');
const consumerPaths = [
  resolve(inboxDirectory, 'conversations.service.ts'),
  resolve(inboxDirectory, 'incoming.service.ts'),
  ...readdirSync(inboxDirectory)
    .filter((name) => /^outbound.*\.ts$/.test(name))
    .map((name) => resolve(inboxDirectory, name)),
];

function providerDispatchViolations(source: string): string[] {
  const rules: Array<[string, RegExp]> = [
    ['provider client or adapter import', /from\s+['"][^'"]*integrations\/(?:meta|evolution|channels)\/[^'"]+['"]/],
    ['credential resolver import', /from\s+['"][^'"]*channel-credential-resolver['"]/],
    ['provider injection token', /\b(?:META_CLIENT|EVOLUTION_CLIENT)\b/],
    ['provider text dispatch', /\.enviarTexto\s*\(/],
    ['provider-specific branch', /\.(?:provider|channelOrigin|type)\s*(?:===|!==|==|!=)\s*['"](?:OFICIAL|NAO_OFICIAL)['"]|switch\s*\(\s*[^)]*\.(?:provider|channelOrigin|type)\s*\)/],
  ];
  return rules.filter(([, expression]) => expression.test(source)).map(([name]) => name);
}

describe('common outbound dependency boundary', () => {
  it('keeps provider clients and dispatch inside channel adapters', () => {
    const violations = consumerPaths.flatMap((path) => {
      const source = readFileSync(path, 'utf8');
      return providerDispatchViolations(source).map((rule) => `${path}: ${rule}`);
    });
    expect(violations).toEqual([]);
  });

  it.each([
    "import { MetaClient } from '../../integrations/meta/meta.client';",
    "import { MetaChannelFactory } from '../../integrations/channels/meta-channel';",
    "import { ChannelCredentialResolver } from '../channels/channel-credential-resolver';",
    "if (context.channelOrigin === 'OFICIAL') return sendMeta();",
    "switch (binding.type) { case 'NAO_OFICIAL': return sendEvolution(); }",
    "const send = context.channelOrigin === 'OFICIAL' ? sendMeta() : sendEvolution();",
    "switch (context.provider) { case 'OFICIAL': return sendMeta(); }",
  ])('detects synthetic provider coupling outside the adapter allowlist: %s', (source) => {
    expect(providerDispatchViolations(source).length).toBeGreaterThan(0);
  });
});

```

## Exact machine receipts and candid boundaries


### browser-result-e44-v1.1.json

```json
{
  "checkpoint": "E44 canonical browser terminal RED",
  "recorded_at_utc": "2026-10-22T22:24:39.509520+00:00",
  "command": "bash scripts/test-channels-local.sh browser",
  "executor_session_id": 88340,
  "actual_exit_code": 1,
  "browser": {
    "passed": 83,
    "failed": 2,
    "total": 85,
    "duration": "14.6m"
  },
  "stdout_sha256": "8f7c82457524c5f63ea62212ba5afdc3dfc5cd7c9a7edf9014f7e0227f303858",
  "owned_disposable_cleanup_observed": true,
  "independent_postseal": "browser-source-recheck-e44-v1.1.json",
  "freshness": "browser-freshness-collection-e44-v1.1.json",
  "failures": [
    {
      "test": "retry com resposta pré-admission não apaga uma submissão anterior incerta",
      "path": "web-app/e2e/start-conversation.spec.ts:231",
      "actual": "Role alert does not contain expected recovery notice; exact expected notice is under role status.",
      "classification": "Test selector mismatch; no product bug or suite success inferred. Later assertions in this test not reached.",
      "next": "Select actual status region, preserving all immutable key/body/retry/negative-effect assertions."
    },
    {
      "test": "mantém snapshot após resposta perdida e não repete o envio automaticamente no reload",
      "path": "web-app/e2e/start-conversation.spec.ts:363",
      "actual": "After an actually accepted BFF/PG send and lost browser response, persistent scoped Storage.getItem exception on reload; stored snapshot lookup via Object.entries is null. Production UI byte-exact to E43 before this test-only run.",
      "classification": "Causal assertion RED before product fix: read exception catch deleted original persisted replay identity.",
      "preceding_assertions": "Original key/body captured; accepted Message persisted; original BU/conversation explicitly reopened; read-fault flag true and no automatic second BFF POST.",
      "not_reached": "Original key/body retention assertions after null, explicit read-error gate/button, blocked reread, later successful local reread, exact-key replay and final one-effect/Message assertions.",
      "next": "Fail closed and preserve original storage on read failure; explicit local reread only. Recover same request/key, no automatic resend."
    }
  ],
  "newly_passing_individual_proofs": [
    "Shared raw-provider catalog refresh returns200 with available template, UI chooses POSITIONAL and dispatches once; no manual lease/catalog-observation seeding.",
    "Escaped inert HTML preview is displayed as text with zero nested markup nodes; preview leaves local Message/state/provider counters unchanged.",
    "Five20-trigger browser waves preserve single open request and single initial send/effect/Message per wave.",
    "Existing protected template/onboarding browser test files pass unchanged."
  ],
  "limits": [
    "Browser mode does not execute current API unit/fullPG/Web unit suites. Three new renderer boundary cases await next full all.",
    "No criterion or delivery stage promoted. No actual preserved runtime/provider proof, independent implementation review or full diff-guard GO."
  ],
  "handoff": "Root independently verified259 records/full inventory,93changed source hashes and served/dist bundle, then released sole writer for bounded E45 UI/read retry and selector correction."
}

```

### storage-read-recovery-evidence-loop-v1.1.json

```json
{
  "kind": "Evidence-first storage-read recovery bug; causal runtime RED confirmed",
  "recorded_at_utc": "2026-10-22T21:56:10.186441+00:00",
  "skill": "delphi-ai/skills/bug-fix-evidence-loop/SKILL.md",
  "source_fingerprint_before": "119149da2b803ed539962d57eaeb6ee0485bf6853ed1cdebeda6a56c4cc3bdfa",
  "source_fact": {
    "path": "web-app/src/componentes/NovaConversa.tsx",
    "stage": "PrimeiraMensagem storageKey load effect",
    "observation": "getItem/parse/validation failures share catch; catch attempts removeItem, then snapshotLoaded becomes true. A read exception is treated as absence and can erase an exact persisted replay key.",
    "certainty": "Confirmed by actual E44 causal assertion RED before production UI mutation."
  },
  "mandatory_questions": {
    "1_existing_end_to_end_tests": "Lost-response reload covers normal storage reads and explicit exact retry; quota case covers failed write before dispatch. Neither injects read failure after a possibly accepted initial send.",
    "2_current_real_payload": "Owned disposable real PostgreSQL/BFF current tests exercise persisted SUCCEEDED/Message and closed key/body. No actual private business DB or provider data queried, as prohibited. The risk concerns browser storage failure, not a hypothesized live DTO mismatch.",
    "3_existing_failing_test": "No existing dedicated getItem-throws case; current all may pass that untested failure chain. E43 two queued count assertions are unrelated and not causal proof for this risk.",
    "4_test_before_fix": "Implemented persistent read-failure injection (not merely one-shot/transient); E44 failed at original snapshot retention after actual accepted send/lost response and explicit reload/reopen. Test-only seal proves production UI unchanged. Later gates/recovery assertions remain unexecuted until fix.",
    "5_architectural_rule_assessment": "Tentative no-rule-needed: failure depends on storage availability plus lost-response/reload ordering, not a proven recurring statically invalid dependency shape. Behavioral regression test is the protection. No analyzer/Delphi change authorized."
  },
  "coverage_matrix": [
    {
      "stage": "Provider boundary / actual disposable BFF+PG acceptance",
      "state": "covered",
      "evidence": "E43 initial-message9/9 and current browser accepted-send assertions; terminal package pending."
    },
    {
      "stage": "Closed request/key DTO and normal replay",
      "state": "covered",
      "evidence": "Existing API replay and browser lost-response/normal-read paths."
    },
    {
      "stage": "Browser persisted snapshot read exception after possible effect",
      "state": "covered",
      "evidence": "E44 causal RED followed by E45 full browser PASS with preserved exact key/body."
    },
    {
      "stage": "UI gate while durable replay identity cannot be read",
      "state": "covered",
      "evidence": "E45 actual UI blocked under persistent read exception; explicit failed/successful local reread and exact original replay verified, one provider effect/Message."
    }
  ],
  "planned_checkpoints": {
    "E43": "No edits; finish frozen all and independent postseal.",
    "E44": "Test-only bounded corrections and new storage-read regression; canonical browser RED required before production fix.",
    "E45": "If causal RED confirmed, sole writer adds fail-closed read handling on admitted UI path; fresh canonical all and postseal."
  },
  "safety": "Only owned disposable synthetic browser/BFF/PG/provider doubles. No actual env/data/logs, real contacts or provider changes. No rollback of implementation to fabricate test-first chronology.",
  "state": "causal_RED_then_frozen_full_GREEN",
  "next": "Keep exact regression; technical assurance and actual local/provider proof remain separate gates.",
  "red_evidence": "browser-result-e44-v1.1.json",
  "green_evidence": "all-result-e45-v1.1.json and all-source-recheck-e45-v1.1.json",
  "architecture_prevention_final": "no-rule-needed: runtime storage availability/lost-response/reload ordering; dedicated behavioral regression guards it. No analyzer/Delphi rule added."
}

```

### test-quality-public-roots-e54-v1.1.json

```json
{
  "kind": "Current full positive-public-root static TQA scan, not independent audit clearance",
  "recorded_at_utc": "2026-10-23T00:24:09.244186+00:00",
  "source_seal": "all-source-seal-e54-v1.1.json",
  "command": [
    "bash",
    "delphi-ai/tools/test_quality_audit.sh",
    "--path",
    "api-app/src",
    "--path",
    "api-app/test",
    "--path",
    "web-app/src",
    "--path",
    "web-app/e2e"
  ],
  "exit_code": 2,
  "heuristic_outcome": "high",
  "raw_sha256": "7bf27069cd8756cbddf3dff5d807d8e3d86387f93e2dc9b75c64853009de9b0c",
  "counts": {
    "hard_bypass": 5,
    "test_support": 0,
    "auth_shortcut": 0,
    "status_only": 196,
    "no_exception_only": 4,
    "ambient_subject_fallback": 16,
    "di_override": 0,
    "mock_hint": 29
  },
  "hard_bypass_disposition": [
    {
      "path": "api-app/src/domain/setor/setor.service.ts",
      "sha256": "d8cb22d68452d1ab9ea9daa69fe9660d867612f81db8e9e9a7fb34a6e56cda84",
      "lines": [
        35
      ],
      "source_fact": "Prisma findMany argument skip beside take/orderBy; pagination offset, not a disabled/skipped test.",
      "disposition": "False positive for hard test bypass; no source change needed."
    },
    {
      "path": "api-app/src/domain/identity/usuarios.service.ts",
      "sha256": "ff82f54a7aa6e495c5ce20626e88221fc20f4474a5ec84ff2f257b081f803364",
      "lines": [
        51
      ],
      "source_fact": "Prisma findMany argument skip beside take/orderBy; pagination offset, not a disabled/skipped test.",
      "disposition": "False positive for hard test bypass; no source change needed."
    },
    {
      "path": "api-app/src/domain/historico/atividades.service.ts",
      "sha256": "9a081318375268d76839a83502d194bb12bfc1fb619a3cb6badab80c425d4609",
      "lines": [
        53
      ],
      "source_fact": "Prisma findMany argument skip beside take/orderBy; pagination offset, not a disabled/skipped test.",
      "disposition": "False positive for hard test bypass; no source change needed."
    },
    {
      "path": "api-app/src/domain/inbox/historico.service.ts",
      "sha256": "811212eeb5b9e8318ef344eb6660385382707cb6d6882c5e9f84e8d4951ccfaa",
      "lines": [
        38,
        101
      ],
      "source_fact": "Prisma findMany argument skip beside take/orderBy; pagination offset, not a disabled/skipped test.",
      "disposition": "False positive for hard test bypass; no source change needed."
    }
  ],
  "remaining_signals": "Current broader heuristic hints require independent test-quality judgment of adjacent assertions. Real PostgreSQL/BFF fixtures and provider controls are not implicitly bypasses. No skip/only nor production test-support/auth shortcut signal found; do not downgrade full scan exit2 to raw PASS.",
  "scope_boundary": "Only four explicit positive public source roots. No --scan-git-modified, actual env, .local-files, process inspection or root-wide Git discovery.",
  "durable_raw": "test-quality-public-roots-output-e54-v1.1.txt",
  "limits": "Static current-source inventory only while canonical ALL is running. No current dynamic GREEN, actual provider, full diff guard/private inspection, build images or runtime proof inferred.",
  "exact_test_focus_skip_crosscheck": {
    "exit_code": 1,
    "matches": 0,
    "scope": "Same four complete positive public roots; supplemental, not narrowed replacement."
  },
  "actual_exit_code": 2,
  "stdout_sha256": "7bf27069cd8756cbddf3dff5d807d8e3d86387f93e2dc9b75c64853009de9b0c",
  "current_raw_summary": [
    "Outcome heuristic: high",
    "Counts: hard_bypass=5 test_support=0 auth_shortcut=0 status_only=196 no_exception_only=4 ambient_subject_fallback=16 di_override=0 mock_hint=29"
  ]
}

```

### capability-owner-evidence-e44-v1.1.json

```json
{
  "kind": "Exact known manifest capability/command evidence; not canonical discovery-tool GO",
  "recorded_at_utc": "2026-10-22T22:07:59.025596+00:00",
  "source_seal": "browser-source-seal-e44-v1.1.json",
  "owners": [
    {
      "manifest": "api-app/package.json",
      "manifest_sha256": "df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d",
      "lockfile": "api-app/package-lock.json",
      "lockfile_sha256": "d1e45274c4b10d134469d7ec63e88777ec26b917d48197a03a4b97cefda047c7",
      "capability_dependencies": {
        "nestjs": {
          "@nestjs/core": "^11.0.0"
        },
        "prisma": {
          "@prisma/client": "^6.0.0",
          "prisma": "^6.0.0"
        }
      },
      "required_scripts": {
        "build": "nest build",
        "lint": "eslint \"{src,test}/**/*.ts\"",
        "test": "vitest run --config vitest.config.ts",
        "test:e2e": "vitest run --config vitest.config.e2e.ts --no-file-parallelism --maxWorkers=1",
        "prisma:generate": "prisma generate",
        "prisma:migrate": "prisma migrate deploy"
      },
      "execution_owner": "bash scripts/test-channels-local.sh all",
      "observed_last_complete_phases": "E43 build/lint/unit/realPG andWebunit passed;browserRED3; no broad parity claim."
    },
    {
      "manifest": "web-app/package.json",
      "manifest_sha256": "fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de",
      "lockfile": "web-app/package-lock.json",
      "lockfile_sha256": "546aec97be8273cf195a16b75c0127474ea3a5042668f8d4c93aab96c1619c8f",
      "capability_dependencies": {
        "react": {
          "react": "^18.3.1",
          "react-dom": "^18.3.1"
        },
        "vite": {
          "vite": "^5.4.11"
        },
        "browser": {
          "@playwright/test": "^1.62.1"
        }
      },
      "required_scripts": {
        "build": "tsc -b && vite build",
        "test": "vitest run",
        "test:tela": "npm run build && playwright test"
      },
      "execution_owner": "bash scripts/test-channels-local.sh all",
      "observed_last_complete_phases": "E43 build/lint/unit/realPG andWebunit passed;browserRED3; no broad parity claim."
    }
  ],
  "canonical_helper_not_executed": {
    "path": "delphi-ai/tools/node_capability_surface_audit.py",
    "reason": "Even --manifest first calls load_manifests(root), whose manifest_paths os.walk recursively enumerates repository directories. It has no private-directory prune for .local-files; this conflicts with explicit approved no-private-traversal boundary.",
    "source_references": [
      "manifest_paths:155-169",
      "audit:229-246"
    ],
    "handling": "Read only2explicit known public package.json/locks and attest against full source seal, owning dependencies/scripts and actual canonical runner. No modified/copied repository, monkeypatch, filtered faux GO, user waiver or silent private discovery."
  },
  "scope_limit": "This establishes only these known project owners and current declared commands; it does not inventory unknown packages or certify the whole actual filesystem. Fresh independent TQA still required."
}

```

### producer-consumer-crosswalk-e54-v1.1.json

```json
{
  "kind": "Current E54 full-execution producer-to-consumer crosswalk",
  "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
  "source_seal": "all-source-seal-e54-v1.1.json",
  "state": "Full canonical ALL terminal GREEN; each listed consumer has current candidate execution. No actual provider/runtime delivery claim.",
  "rows": [
    {
      "id": "manual-open",
      "producer": "ConversationStartService atomically returns created/reused row without send/read/claim/automation",
      "consumers": [
        "NovaConversa dialog POST and onOpened",
        "Inbox selected manual conversation / truthful list order"
      ],
      "exact_test_references": [
        "api-app/test/conversation-start.e2e-spec.ts:25",
        "api-app/test/conversation-start.e2e-spec.ts:64",
        "api-app/test/conversation-start.e2e-spec.ts:153",
        "api-app/test/conversation-start.e2e-spec.ts:177",
        "web-app/e2e/start-conversation.spec.ts:74"
      ],
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json",
        "browser-freshness-collection-e54-v1.1.json"
      ],
      "historical_evidence": "E45 atomic PG5x20/no automation and real browser open/reuse passed; E46 corresponding browser regression passed.",
      "evidence_and_limit": "Relevant API/PG/served-browser scenarios passed full E54. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."
    },
    {
      "id": "qualified-window",
      "producer": "Verified signed Meta IN timestamp accepted only for current managed identity; Message.officialInboundAt nullable",
      "consumers": [
        "PrismaChannelResolver.inspectForConversation",
        "PrismaChannelResolver.inspectManyForConversations via BFF/public listing",
        "OutboundService ordinary BFF/PUBLIC/BOT",
        "Initial text dispatch claim in transaction"
      ],
      "exact_test_references": [
        "api-app/src/domain/inbox/channel-window-policy.spec.ts",
        "api-app/test/webhooks.e2e-spec.ts",
        "api-app/test/number-onboarding-pcv.e2e-spec.ts",
        "api-app/test/number-onboarding-typebot.e2e-spec.ts",
        "api-app/test/api-publica.e2e-spec.ts",
        "web-app/e2e/channel-transport.spec.ts"
      ],
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json",
        "browser-freshness-collection-e54-v1.1.json"
      ],
      "historical_evidence": "E45 signed timestamp/resource policy, BFF/public/BOT projected/send regressions and raw/substitution tests passed; public index/query counts in actual PCV receipt.",
      "evidence_and_limit": "Relevant API/PG/served-browser scenarios passed full E54. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."
    },
    {
      "id": "shared-template-catalog",
      "producer": "ST05 bounded catalog projector/lease/TTL remains owner; initial renderer consumes unchanged components",
      "consumers": [
        "Shared catalog route and PrimeiraMensagem template selector",
        "Read-only local preview/escaped React text",
        "Fresh same-account remote eligibility before new dispatch"
      ],
      "exact_test_references": [
        "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts:18",
        "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts:64",
        "api-app/test/initial-message.e2e-spec.ts:329",
        "web-app/e2e/start-conversation.spec.ts:447"
      ],
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json",
        "browser-freshness-collection-e54-v1.1.json"
      ],
      "historical_evidence": "E45 renderer exact bounds/NAMED/POSITIONAL, real catalog refresh, escaped read-only preview, same-account fresh membership before dispatch passed. Protected authoring/catalog browser cases passed E46.",
      "evidence_and_limit": "Relevant API/PG/served-browser scenarios passed full E54. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."
    },
    {
      "id": "abstract-channel-union",
      "producer": "One Channel.sendMessage(text|approved-template), readonly supportedKinds, awaited operation fence",
      "consumers": [
        "OutboundService ordinary calls",
        "Initial coordinator through same OutboundService",
        "Meta adapter concrete formatter",
        "Evolution adapter text-only typed refusal"
      ],
      "exact_test_references": [
        "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
        "api-app/src/domain/channels/transport/channel-initial-message.spec.ts:46",
        "api-app/src/domain/channels/transport/channel-initial-message.spec.ts:62",
        "api-app/test/channel-transport.e2e-spec.ts"
      ],
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json",
        "browser-freshness-collection-e54-v1.1.json"
      ],
      "historical_evidence": "E45 dependency/substitution, Evolution typed zeroHTTP, raw Meta account/recipient protocol and ordinary BFF/public/BOT text regressions passed.",
      "evidence_and_limit": "Relevant API/PG/served-browser scenarios passed full E54. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."
    },
    {
      "id": "durable-intent-outcome",
      "producer": "Immutable original key/body/context and truthful persisted receipt/uncertainty/state projection",
      "consumers": [
        "Scoped BFF create/read/reconcile/ack routes with session+grant+CSRF",
        "api.ts safe closed error metadata",
        "PrimeiraMensagem explicit recovery/exact retry and actor+BU+conversation sessionStorage"
      ],
      "exact_test_references": [
        "api-app/test/dispatch-admission.e2e-spec.ts:165",
        "api-app/test/dispatch-admission.e2e-spec.ts:196",
        "api-app/test/initial-message.e2e-spec.ts:95",
        "api-app/test/initial-message.e2e-spec.ts:206",
        "web-app/e2e/start-conversation.spec.ts:198",
        "web-app/e2e/start-conversation.spec.ts:266",
        "web-app/e2e/start-conversation.spec.ts:599"
      ],
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json",
        "browser-freshness-collection-e54-v1.1.json"
      ],
      "historical_evidence": "E45 actual PG barriers/readback/CAS and browser read/reconcile/ACK, failed local storage read/write, lost-response original-key replay passed. E46 those browser cases pass.",
      "evidence_and_limit": "Relevant API/PG/served-browser scenarios passed full E54. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."
    },
    {
      "id": "shared-admission-interlock",
      "producer": "Ordinary per-owner tokens and exclusive initial slot use same conversation lock; no SENDING clock takeover",
      "consumers": [
        "BFF ordinary composer empty/unresolved gate",
        "PUBLIC ordinary sender through ConversationsService",
        "BOT ordinary sender through IncomingService",
        "Initial reservation and explicit local risk release controls",
        "OrdinaryRecovery actual scoped reconcile/acknowledge controls on reopened thread"
      ],
      "exact_test_references": [
        "api-app/test/dispatch-admission.e2e-spec.ts:328",
        "api-app/test/dispatch-admission.e2e-spec.ts:367",
        "api-app/test/dispatch-admission.e2e-spec.ts:379",
        "api-app/test/dispatch-admission.e2e-spec.ts:434",
        "api-app/test/dispatch-admission.e2e-spec.ts:457",
        "api-app/test/channel-transport.e2e-spec.ts",
        "api-app/test/api-publica.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts:531"
      ],
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json",
        "browser-freshness-collection-e54-v1.1.json"
      ],
      "historical_evidence": "E45 real PG races/ordinary concurrency, public/BOT and empty BFF mapping pass; E47 actual ordinary BFF browser uncertain send→reopen→reconcile→real90s risk ACK→composer return with unchanged provider/audit snapshots passed.",
      "evidence_and_limit": "Relevant API/PG/served-browser scenarios passed full E54. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."
    },
    {
      "id": "prepared-safe-action",
      "producer": "Valid durable PREPARED projected as RECONCILE, GET read-only",
      "consumers": [
        "PrimeiraMensagem existing local recovery action",
        "Scoped BFF reconcile"
      ],
      "exact_test_references": [
        "api-app/test/initial-message.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "evidence_and_limit": "Current full E54: live202 unchanged slot then synthetic DB expiry local reject/release, zero provider/Message. Actual compiled reserveInitial fixture uses canonical request/fingerprint and90s lease.",
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json"
      ]
    },
    {
      "id": "known-ack-local-blocked-risk-release",
      "producer": "EXTERNAL_ACCEPTED_LOCAL_BLOCKED safe state, immutable original deadline, scoped409 metadata",
      "consumers": [
        "Actual UI early acknowledgment409",
        "Explicit after-deadline acknowledgment200",
        "Successor and late-old local recovery"
      ],
      "exact_test_references": [
        "api-app/test/initial-message.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "evidence_and_limit": "E54 real BFF early ACK_TOO_EARLY409 leaves slot/provider/Message unchanged; synthetic disposable deadline expiry permits one successor, later original local completion never reacquires slot or changes current owner. No disabled-button requirement invented.",
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json"
      ]
    },
    {
      "id": "unicode-contract",
      "producer": "Server code-point limits4096 text/1024 template values",
      "consumers": [
        "NovaConversa input clamp",
        "Scoped session snapshot restore",
        "Escaped preview and actual initial POST"
      ],
      "exact_test_references": [
        "web-app/src/componentes/NovaConversa.spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "evidence_and_limit": "E51 real positional snapshot RED precedes fix; E54 named and positional1024/1025 plus text4096/4097 unit bounds, actual4096-text and1024-positional browser input/preview/send. No separate named full-browser1024 claim.",
      "consumer_state": "implemented + evidenced",
      "actual_receipts": [
        "all-result-e54-v1.1.json",
        "web-result-e51-v1.1.json"
      ]
    }
  ],
  "external_proof_boundary": "Synthetic provider boundary plus real disposable BFF/PostgreSQL/browser. User attests own template APPROVED; same-account first-template actual send/reply and nonofficial first-send/reply are pending source-bound local activation.",
  "assurance_boundary": "No full diff-guard, required implementation reviews, runtime activation or criterion checkbox promoted.",
  "remaining_required_gates": [
    "Fresh architecture/TQA/cutover assessment and material finding resolution",
    "Concrete Alpine images then separately approved preserved-local activation/migrations/operator first-send/reply",
    "Modules, full canonical diff inspection exception/guard and final closure gates"
  ]
}

```

### candidate-criterion-index-e54-v1.1.json

```json
{
  "kind": "Current E54 criterion-specific full execution index; not delivery closure",
  "source_seal": "all-source-seal-e54-v1.1.json",
  "source_fingerprint": "604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c",
  "execution_state": "Full canonical ALL terminal0, API364/PG439/Web54/browser88; current full postseal and browser binding verified.",
  "interpretation": "Exact approved criterion wording is retained. Current full execution replaces former composite proof; no claim that these checkboxes are closed before independent reviews/runtime/modules/guards.",
  "criteria": [
    {
      "criterion_id": "DOD-01",
      "approved_criterion": "opening invokes no automation; manual-open-without-send then first inbound leaves NOVA_CONVERSA false while keyword automation retains its predicate; authorized operator opens/reuses BU/contact atomically; no side effects listed in SCOPE-01 occur; new conversation has truthful empty state and deterministic list ordering.",
      "candidate_source_references": [
        "api-app/test/conversation-start.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "proof_target": [
        "Atomic open/reuse,5x20 open requests, no trigger on open/first IN and separate keyword case.",
        "Browser empty-open and reuse-before-send audit."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "API atomic5x20/empty-state/keyword and NOVA_CONVERSA cases plus browser create/reuse pass. Independent exact criterion review remains."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-02",
      "approved_criterion": "stale/foreign BU, actor, slot, selected channel, grant, credential epoch/version, conversation generation, template fingerprint, or policy context fails closed before external dispatch.",
      "candidate_source_references": [
        "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
        "api-app/test/initial-message.e2e-spec.ts",
        "api-app/test/dispatch-admission.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "proof_target": [
        "Nine-field immutable-context mismatch unit matrix.",
        "BFF forged grant/current session/grant/preflight deadline and owner/close fences.",
        "Browser stale A-B-A preview and permission recovery."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Nine-field mismatch, forged-tenant/session/grant/remote preflight fences and browser A-B-A pass; independent security/adherence remains."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-03",
      "approved_criterion": "Preview is escaped, deterministic, local/read-only and context-bound; supported textual subset and exact limits are enforced server-side.",
      "candidate_source_references": [
        "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts",
        "api-app/src/domain/inbox/initial-message.service.spec.ts",
        "api-app/test/initial-message.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "proof_target": [
        "NAMED/POSITIONAL ordering/repeats/static component order/unsupported subset.",
        "Local preview and changed-context preAdmission rejection.",
        "React preview and explicit confirmation."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "New exact renderer4096/4097,1024/1025 Unicode and20/21 parameter bounds pass; escaped inert markup/read-only preview passes. Independent assessment remains."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable.",
        "Server and snapshot code-point bounds plus actual Unicode browser input/preview/send passed; separate JSON storage guard remains."
      ]
    },
    {
      "criterion_id": "DOD-04",
      "approved_criterion": "existing Channel consumers remain substitutable; Meta supports declared text/template kinds; Evolution template is typed unsupported with zero HTTP; no second send method/provider branching outside adapters or DI cycle; immutable descriptor plus same-operation fence preserves common dispatch.",
      "candidate_source_references": [
        "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
        "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
        "api-app/test/channel-transport.e2e-spec.ts"
      ],
      "proof_target": [
        "Inherited sealed dependency harness; union substitution and unsupported Evolution0HTTP.",
        "Ordinary legacy text and initial protocol in same bound Channel."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Dependency/substitution/typed Evolution0HTTP/raw Meta union/text regressions pass; independent architecture/cutover remains."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-05",
      "approved_criterion": "prove commit certainty at reservation/dispatch-claim/receipt/release, including real commit with lost ACK and real rollback; every remote eligibility/grant/phone GET completes before durable SENDING claim; the abstract fence CAS-claims immediately before one POST, and expiry of PREPARED during delayed preflight produces zero POST. Each initial attempt dispatches at most one POST; failures are classified truthfully; known provider ID is durably separate from local Message; recovery never contacts provider and never creates a Message without external ID.",
      "candidate_source_references": [
        "api-app/test/dispatch-admission.e2e-spec.ts",
        "api-app/test/initial-message.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "proof_target": [
        "Actual PG commit-with-lost-ACK versus actual rollback at reservation/claim/receipt/release/completion.",
        "Delayed remote GET expiry0POST, bounded protocol and same-key5x20.",
        "Browser unknown response, reload and same-key replay/storage failure."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Actual PG commit/rollback distinction and browser E44 causal read-failure RED -> E45 full GREEN pass; exact replay preserves1effect/Message. No external exactly-once claim; independent assessment remains."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-06",
      "approved_criterion": "initial transaction locks identity then conversation, checks original pre-HTTP status/owner CAS before acceptance mutates updatedAt, permits eligible acceptance when status CAS fails, and recovers unique conflict by whole-local-transaction rollback/readback/re-entry at most once; MessageAcceptance remains sole Message owner and existing sender/error behavior is preserved; CAS prevents late initial outcome from changing concurrent claim/close/owner or reacquiring released slot. Initial acknowledgment in either allowed state waits for immutable dispatchDeadlineAt; before it409 ACK_TOO_EARLY and zero release.",
      "candidate_source_references": [
        "api-app/test/dispatch-admission.e2e-spec.ts",
        "api-app/test/initial-message.e2e-spec.ts",
        "api-app/src/domain/inbox/dispatch-admission.service.spec.ts",
        "api-app/src/domain/inbox/message-acceptance.service.spec.ts"
      ],
      "proof_target": [
        "Original owner/status CAS, competing echo P2002 in local reconciliation, known receipt local completion.",
        "Risk ACK before/after DB deadline; exact deadline-1/equality/+1 deterministic unit predicate."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Actual PG owner/CAS/whole-tx P2002/readback/local retry and irreversible deadline release cases pass. Exact equality is deterministic unit proof, not PG wall-clock equality. Independent transaction assessment remains."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable.",
        "Actual BFF/UI EALB early409 and after synthetic expiry200, successor/late-old isolation passed; ordinary recovery separately waited actual90s."
      ]
    },
    {
      "criterion_id": "DOD-07",
      "approved_criterion": "official window uses only qualified trusted Meta IN timestamp for selected resource; all current BFF/public/BOT availability and send policy consumers use the same rule; timeline/cursors and performance bounds hold.",
      "candidate_source_references": [
        "api-app/src/domain/inbox/channel-window-policy.spec.ts",
        "api-app/test/webhooks.e2e-spec.ts",
        "api-app/test/number-onboarding-pcv.e2e-spec.ts",
        "api-app/test/number-onboarding-typebot.e2e-spec.ts",
        "api-app/test/api-publica.e2e-spec.ts",
        "web-app/e2e/channel-transport.spec.ts"
      ],
      "proof_target": [
        "Signed timestamp provenance, duplicate immutability, selected resource strict24h.",
        "Single inspect/inspectMany boundary, batched public projection and OUT-heavy/no-IN EXPLAIN.",
        "Preserved timeline/cursor suites included in all."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Signed timestamp/current-resource, BFF/PUBLIC/BOT/window projections and full timeline/cursor regressions pass; SQL/index query bounds measured. Independent cross-consumer assessment remains."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-08",
      "approved_criterion": "owner-scoped ordinary admissions and exclusive initial reservation serialize under the same conversation lock without serializing ordinary-versus-ordinary sends; uncertain dispatched tokens block initial reservation until settlement or explicit risk acknowledgment, never time takeover; late owner release cannot touch successor; existing composer is blocked before HTTP for new/empty/unresolved slot; public/BOT respect slot and retain existing mappings; text regressions pass.",
      "candidate_source_references": [
        "api-app/src/domain/inbox/outbound.service.spec.ts",
        "api-app/test/dispatch-admission.e2e-spec.ts",
        "api-app/test/channel-transport.e2e-spec.ts",
        "api-app/test/atendimento.e2e-spec.ts",
        "api-app/test/api-publica.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "proof_target": [
        "Ordinary per-owner overlap and exclusive initial slot; SENDING never time takeover.",
        "BFF empty gate, PUBLIC/BOT mappings, owner-scoped settlement and late release.",
        "Browser empty/unresolved composer block and risk controls."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Actual ordinary browser send/reopen/reconcile/risk ACK after90s/composer return passes E47; API/PG public/BOT interlock regressions pass E45. Current full E47 regression/independent assessment still pending."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-09",
      "approved_criterion": "NAMED and POSITIONAL initial support is derived by the initial text renderer from the unchanged catalog components/format, independently of inherited authoring flags; exact full context binds management descriptor to selected transport and final text-window fence; current eligibility is checked before every new official template dispatch via bounded same-account reads; template is actually APPROVED; Meta request pins server-captured `messaging_account_id`, uses `+` plus full DDI, and preserves existing ordinary text semantics. Tests cover same-country and cross-country recipients. Official raw reference receipt confirms account pin and recipient formatting; actual own-account readiness remains unverified.",
      "candidate_source_references": [
        "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts",
        "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
        "api-app/src/integrations/meta/initial-message.client.spec.ts",
        "api-app/test/initial-message.e2e-spec.ts",
        "web-app/e2e/start-conversation.spec.ts"
      ],
      "proof_target": [
        "ST05 catalog flags remain unchanged; initial renderer independent.",
        "Pinned account,+fullDDI,same/cross-country raw protocol,6GET/1POST upper case.",
        "Negative current status/account/definition/membership bounds."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "API NAMED/POSITIONAL same-account tuple and raw recipient/account-pin cases + realBFF/browser POSITIONAL flow pass. Actual own-account approved template send/reply remains required."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-10",
      "approved_criterion": "per actor/account limits, tenant isolation, request/deadline budgets and zero-network recovery are demonstrated with real bounded counters/barriers.",
      "candidate_source_references": [
        "api-app/test/dispatch-admission.e2e-spec.ts",
        "api-app/test/initial-message.e2e-spec.ts",
        "api-app/src/integrations/meta/initial-message.client.spec.ts"
      ],
      "proof_target": [
        "10/min actor,60/h opaque canonical account, retained released attempts; forged grant rejection.",
        "75s bounded preflight, immutable90s lease, no-retry provider counters, local-only recovery."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Real bounded actor/account quota/barriers/zero-network recovery pass. Independent security/PCV and same-source evidence assessment remain."
      ],
      "remaining_or_limit": [
        "Current relevant automated scenario passed full E54; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."
      ]
    },
    {
      "criterion_id": "DOD-11",
      "approved_criterion": "additive migration passes explicit preflight and disposable local validation without reset/drop; current source/image/API freshness and approved local validation topology are proven.",
      "candidate_source_references": [
        "api-app/prisma/schema.prisma",
        "api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql",
        "api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql",
        "api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql",
        "api-app/test/dispatch-admission.e2e-spec.ts",
        "web-app/e2e/timeline-freshness.ts"
      ],
      "proof_target": [
        "Disposable migrate deploy/status; ST04 columns/native types/enum/constraints/index facts.",
        "5s lock timeout/60s statement timeout; positive-public source pre/post seals."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Disposable28migrations deploy/status and bounded ST04 schema/index checks pass; served bundle/source manifest match. Actual preserved local image/native runtime/migration and approved activation remain."
      ],
      "remaining_or_limit": [
        "Disposable28migration/source/served-bundle proof passed. Actual Alpine images/preserved local activation/migration not executed."
      ]
    },
    {
      "criterion_id": "DOD-12",
      "approved_criterion": "assisted proof: operator sends first unofficial message, an actually APPROVED official template, receives a reply; no auto-contact; if eligible approved asset is unavailable, completion remains blocked.",
      "candidate_source_references": [],
      "proof_target": [
        "User reports own prior model APPROVED; human attestation only, not provider query or send."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Only human attestation of APPROVED template; actual first nonofficial send + official approved template send + replies remain unperformed."
      ],
      "remaining_or_limit": [
        "Actual own-resource first-send/reply, required modules/reviews/guards remain uncompleted; no delivery claim."
      ]
    },
    {
      "criterion_id": "DOD-13",
      "approved_criterion": "architecture/adherence/security/performance/TQA/final/cutover/debt and delivery guards pass at their required stages; no open P1/P2; constraints SEC-R6-04, OPS-R4-01, TQA-ST05-03 remain truthfully carried.",
      "candidate_source_references": [],
      "proof_target": [
        "Chronology/deviations E02/E04/E18/E35a and inherited SEC-R6-04/OPS-R4-01/TQA-ST05-03 explicitly preserved."
      ],
      "state": "actual test proof indexed; criterion not closed",
      "current_checkpoint": "all-result-e54-v1.1.json; browser-freshness-collection-e54-v1.1.json",
      "historical_remaining_or_limit": [
        "Independent implementation assessments, current full E47 terminal, canonical diff-guard inspection exception, module consolidation, actual local runtime/operator proof and final delivery gates remain."
      ],
      "remaining_or_limit": [
        "Actual own-resource first-send/reply, required modules/reviews/guards remain uncompleted; no delivery claim."
      ]
    }
  ],
  "validation_crosswalk": {
    "VAL-01": [
      "DOD-01",
      "DOD-04",
      "DOD-08"
    ],
    "VAL-02": [
      "DOD-02",
      "DOD-05",
      "DOD-06",
      "DOD-08",
      "DOD-10"
    ],
    "VAL-03": [
      "DOD-02",
      "DOD-04",
      "DOD-09"
    ],
    "VAL-04": [
      "DOD-07"
    ],
    "VAL-05": [
      "DOD-07",
      "DOD-10"
    ],
    "VAL-06": [
      "DOD-01",
      "DOD-02",
      "DOD-03",
      "DOD-05",
      "DOD-08"
    ],
    "VAL-07": [
      "DOD-11"
    ],
    "VAL-08": [
      "DOD-11",
      "DOD-12"
    ],
    "VAL-09": [
      "DOD-13"
    ]
  },
  "causality": "Do not retroactively claim test-first: only documented actual causal REDs qualify. Most added fault/protocol/storage cases are alongside/post-implementation.",
  "validation_rows": [
    {
      "criterion_id": "VAL-01",
      "mapped_dod_ids": [
        "DOD-01",
        "DOD-04",
        "DOD-08"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-02",
      "mapped_dod_ids": [
        "DOD-02",
        "DOD-05",
        "DOD-06",
        "DOD-08",
        "DOD-10"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-03",
      "mapped_dod_ids": [
        "DOD-02",
        "DOD-04",
        "DOD-09"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-04",
      "mapped_dod_ids": [
        "DOD-07"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-05",
      "mapped_dod_ids": [
        "DOD-07",
        "DOD-10"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-06",
      "mapped_dod_ids": [
        "DOD-01",
        "DOD-02",
        "DOD-03",
        "DOD-05",
        "DOD-08"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-07",
      "mapped_dod_ids": [
        "DOD-11"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-08",
      "mapped_dod_ids": [
        "DOD-11",
        "DOD-12"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    },
    {
      "criterion_id": "VAL-09",
      "mapped_dod_ids": [
        "DOD-13"
      ],
      "state": "Current E54 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.",
      "criterion_source": "Approved TODO Validation Steps, not inferred from aggregate counts",
      "current_checkpoint": "all-result-e54-v1.1.json"
    }
  ]
}

```

### security-candidate-map-e54-v1.1.json

```json
{
  "kind": "Current E54 executed adversarial proof map for fresh independent challenge",
  "risk_level": "high",
  "attack_simulation_decision": "required",
  "source_seal": "all-source-seal-e54-v1.1.json",
  "execution_state": "Actual terminal0: API364/PG439/Web54/browser88, complete259 inventory and93 browser manifest records verified.",
  "threat_intelligence": [
    {
      "source": "OWASP API1:2023 Broken Object Level Authorization",
      "url": "https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/",
      "consulted_date": "2026-10-22",
      "paraphrase": "Every object-based action needs permission checks for that object. A valid login and an opaque UUID alone do not establish authorization.",
      "applies_to": "BU/conversation/channel/template/attempt/admission ownership; forged grants and foreign references."
    },
    {
      "source": "OWASP API4:2023 Unrestricted Resource Consumption",
      "url": "https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/",
      "consulted_date": "2026-10-22",
      "paraphrase": "Bound execution time, pages, operation counts and third-party resource use. Concurrent valid calls can consume provider and server resources.",
      "applies_to": "Actor/account limits, bounded template/membership pages, overall lease/preflight budget, one external POST, local-only recovery."
    }
  ],
  "surfaces": [
    {
      "entry": "Authenticated BFF open/options/preview/initial/read/reconcile/ack",
      "boundary": "Session+CSRF+current home-tenant/BU role before detailed validation; current grant after awaits/inside mutation",
      "abuse": "Forge cross-tenant BU grant; change object IDs; revoke session/role while provider GET held",
      "source_tests": [
        "api-app/test/initial-message.e2e-spec.ts"
      ],
      "current_receipt": "all-result-e54-v1.1.json; all-source-recheck-e54-v1.1.json",
      "historical_e45_status": "Actual forged cross-tenant grant case295 and current session/grant negative scenarios in approved-template compound329 passed E45; exact BFF current grant/CSRF tested with real PG.",
      "status": "Corresponding negative scenarios passed again in full E54; source tests are bound to current seal. Historical description is retained separately, not current line numbering.",
      "source_hashes": [
        {
          "path": "api-app/test/initial-message.e2e-spec.ts",
          "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
        }
      ]
    },
    {
      "entry": "Selected Channel descriptor and scoped credential",
      "boundary": "Immutable BU/channel/origin/resource/generation/epoch/version/account/window context; no browser credentials/account override",
      "abuse": "Confuse descriptor/transport account or use rotated/retired resource before POST",
      "source_tests": [
        "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
        "api-app/test/channel-transport.e2e-spec.ts"
      ],
      "current_receipt": "all-result-e54-v1.1.json; all-source-recheck-e54-v1.1.json",
      "historical_e45_status": "Actual nine-field immutable context/substitution tests and channel-transport regressions passed E45; no real credential/provider probing.",
      "status": "Corresponding negative scenarios passed again in full E54; source tests are bound to current seal. Historical description is retained separately, not current line numbering.",
      "source_hashes": [
        {
          "path": "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
          "sha256": "46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"
        },
        {
          "path": "api-app/test/channel-transport.e2e-spec.ts",
          "sha256": "a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"
        }
      ]
    },
    {
      "entry": "Template catalog/preview/provider preflight",
      "boundary": "Sanitized shared catalog, exact bounded renderer, fresh same-account eligibility/status and grant membership",
      "abuse": "Use paused/unknown/off-account/changed/duplicate template; unbounded pages; inject provider fields",
      "source_tests": [
        "api-app/test/initial-message.e2e-spec.ts",
        "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts"
      ],
      "current_receipt": "all-result-e54-v1.1.json; all-source-recheck-e54-v1.1.json",
      "historical_e45_status": "Actual approved-template compound329 covers off-account/paused/unknown/changed/duplicate/unexhausted and no-dispatch counters; renderer length/parameter boundaries passed356API.",
      "status": "Corresponding negative scenarios passed again in full E54; source tests are bound to current seal. Historical description is retained separately, not current line numbering.",
      "source_hashes": [
        {
          "path": "api-app/test/initial-message.e2e-spec.ts",
          "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
        },
        {
          "path": "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts",
          "sha256": "c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"
        }
      ]
    },
    {
      "entry": "Initial/ordinary dispatch admissions and local acceptance",
      "boundary": "Durable owned slot, immutable key/request/context, positive claim readback; exactly one POST maximum per intent, no automatic retry",
      "abuse": "Concurrent replay, delayed preflight after expiry, commit ACK loss, late outcome after explicit risk release, echo unique conflict",
      "source_tests": [
        "api-app/test/dispatch-admission.e2e-spec.ts",
        "api-app/test/initial-message.e2e-spec.ts"
      ],
      "current_receipt": "all-result-e54-v1.1.json; all-source-recheck-e54-v1.1.json",
      "historical_e45_status": "Actual dispatch-admission commit/rollback and immutable deadline, late-receipt/successor/echo barriers passed435PG; five20-request waves preserve1dispatch/Message each.",
      "status": "Corresponding negative scenarios passed again in full E54; source tests are bound to current seal. Historical description is retained separately, not current line numbering.",
      "source_hashes": [
        {
          "path": "api-app/test/dispatch-admission.e2e-spec.ts",
          "sha256": "ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47"
        },
        {
          "path": "api-app/test/initial-message.e2e-spec.ts",
          "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
        }
      ]
    },
    {
      "entry": "Signed official webhook timestamp",
      "boundary": "Verified signature/current resource/positive integer nonfuture timestamp; no createdAt/nonofficial fallback",
      "abuse": "Manufacture free-text window with invalid/future/foreign/duplicate/nonofficial IN",
      "source_tests": [
        "api-app/test/webhooks.e2e-spec.ts",
        "api-app/src/domain/inbox/channel-window-policy.spec.ts"
      ],
      "current_receipt": "all-result-e54-v1.1.json; all-source-recheck-e54-v1.1.json",
      "historical_e45_status": "Timestamp policy invalid/future/nonofficial/foreign-resource cases and signed webhook tests passed E45; source-bound BFF/public/BOT regression preserved.",
      "status": "Corresponding negative scenarios passed again in full E54; source tests are bound to current seal. Historical description is retained separately, not current line numbering.",
      "source_hashes": [
        {
          "path": "api-app/test/webhooks.e2e-spec.ts",
          "sha256": "e9f80894181676b2fcb4ec18339a6ebdb1e189f3f13374cd1c2e77d13e647f4a"
        },
        {
          "path": "api-app/src/domain/inbox/channel-window-policy.spec.ts",
          "sha256": "e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"
        }
      ]
    },
    {
      "entry": "Browser compose/recovery/storage and safe errors",
      "boundary": "Actor/BU/conversation-scoped immutable snapshot, explicit confirmation, no automatic POST on reload; escaped React text, closed safe error fields",
      "abuse": "Double-trigger, stale A-B-A preview, quota/storage failure before dispatch, lost response followed by context refusal and new key",
      "source_tests": [
        "web-app/e2e/start-conversation.spec.ts",
        "web-app/src/api.spec.ts"
      ],
      "current_receipt": "all-result-e54-v1.1.json; all-source-recheck-e54-v1.1.json",
      "historical_e45_status": "Actual escaped preview, delayed A-B-A, session refusal, storage write/read failure and lost-response same-key replay passed85browser. Ordinary recovery action proof still pending E46.",
      "status": "Actual PREPARED UI, ordinary90s recovery, EALB early409/expired acknowledgment/successor/late-old isolation, Unicode input/preview/send, storage read/write and same-key replay passed full E54. EALB/PREPARED expiry is explicit disposable fixture arrangement; ordinary90s case uses actual wait.",
      "source_hashes": [
        {
          "path": "web-app/e2e/start-conversation.spec.ts",
          "sha256": "16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"
        },
        {
          "path": "web-app/src/api.spec.ts",
          "sha256": "9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9"
        }
      ]
    }
  ],
  "validation_safety": "Owned disposable synthetic DB/provider boundary only. No actual provider probes, contacts, private data/env/log inspection or destructive test.",
  "residuals": [
    "SEC-R6-04 existing management recovery read budget debt not silently resolved; new initial recovery performs no provider I/O.",
    "OPS-R4-01 and TQA-ST05-03 retained.",
    "Procedural E02/E04/E18/E35a stay in independent assurance packet; no blanket privacy compliance claim.",
    "Candidate map does not replace final security findings/decision, independent review, actual runtime proof or canonical guards.",
    "Canonical npm ci emitted inherited dependency audit warnings; package/lock source remains unchanged and no dependency remediation/scope expansion or blanket dependency-clean claim is made.",
    "No actual preserved local activation, real provider eligibility/send or recipient reply proof for ST04 yet."
  ],
  "promotion_candidates": "None proposed; no Delphi edits.",
  "findings_state": "R1 corrections have actual full current regression proof; fresh r2 independent security/architecture and final runtime/closure gates remain."
}

```

### decision-module-candidate-map-e54-v1.1.json

```json
{
  "kind": "Current E54 executed decision/module map for fresh independent challenge",
  "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
  "approved_baseline": "TODO Decision Baseline (Frozen Before Implementation), D-01 through D-10 exact wording remains authority",
  "source_seal": "all-source-seal-e54-v1.1.json",
  "execution_receipt": "all-result-e54-v1.1.json",
  "current_status": "Full canonical ALL terminal GREEN; implementation candidate only. No module consolidation/runtime/final closure yet.",
  "canonical_module_baselines": [
    {
      "path": "foundation_documentation/modules/inbox-and-conversations.md",
      "sha256": "24b3f1edd8f10bf991d61135be2364b49679c43e5894ce024c2d5169921756a2"
    },
    {
      "path": "foundation_documentation/modules/integrations-and-channels.md",
      "sha256": "6b1865ab4f27458e1e1e225535e2f4a713e987e18344ca86d3f9411fa6c6f168"
    }
  ],
  "rows": [
    {
      "decision_id": "D-01",
      "proposed_handling": "Preserve",
      "implementation_claim": "BU/contact unique, normalization and no-send manual open; COALESCE order for empty rows.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/conversation-start.service.ts",
          "sha256": "97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118"
        },
        {
          "path": "api-app/src/domain/inbox/conversations.service.ts",
          "sha256": "6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c"
        },
        {
          "path": "api-app/src/domain/inbox/incoming.service.ts",
          "sha256": "390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/test/conversation-start.e2e-spec.ts",
          "sha256": "35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"
        }
      ],
      "promotion_target": "inbox: manual open and truthful empty state",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-02",
      "proposed_handling": "Supersede (Intentional)",
      "implementation_claim": "Text-only payload restriction becomes one discriminated sendMessage union with declared kinds; narrow management capability remains separate.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/channels/transport/channel.ts",
          "sha256": "49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9"
        },
        {
          "path": "api-app/src/integrations/channels/meta-channel.ts",
          "sha256": "99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26"
        },
        {
          "path": "api-app/src/integrations/channels/evolution-channel.ts",
          "sha256": "6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34"
        },
        {
          "path": "api-app/src/integrations/channels/channel-transport.module.ts",
          "sha256": "4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
          "sha256": "46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"
        },
        {
          "path": "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
          "sha256": "f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3"
        }
      ],
      "promotion_target": "integrations: ST06 payload supersede, historical ST05 D09 unchanged",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-03",
      "proposed_handling": "Preserve",
      "implementation_claim": "Inbox coordinator uses common OutboundService and same MessageAcceptance owner; transactional collaboration stays there.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/initial-message.service.ts",
          "sha256": "ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"
        },
        {
          "path": "api-app/src/domain/inbox/outbound.service.ts",
          "sha256": "0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"
        },
        {
          "path": "api-app/src/domain/inbox/message-acceptance.service.ts",
          "sha256": "71194c70b12cb920054586a7a86266d90f8eca0b7008b1b5688627e0694979f1"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/test/dispatch-admission.e2e-spec.ts",
          "sha256": "ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47"
        }
      ],
      "promotion_target": "inbox: first-send ownership and tx boundaries",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-04",
      "proposed_handling": "Supersede (Intentional)",
      "implementation_claim": "Qualified signed Meta IN timestamp replaces historical createdAt latest-IN window; timeline timestamp/cursors preserved.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/channel-window-policy.ts",
          "sha256": "46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e"
        },
        {
          "path": "api-app/src/surfaces/webhooks/meta.controller.ts",
          "sha256": "261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f"
        },
        {
          "path": "api-app/src/integrations/channels/prisma-channel-resolver.ts",
          "sha256": "60005fd226534a178b646d6ec775bb059ec55cc4cfea24a3d72d2c6e4a1ca64a"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/src/domain/inbox/channel-window-policy.spec.ts",
          "sha256": "e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"
        },
        {
          "path": "api-app/test/webhooks.e2e-spec.ts",
          "sha256": "e9f80894181676b2fcb4ec18339a6ebdb1e189f3f13374cd1c2e77d13e647f4a"
        },
        {
          "path": "api-app/test/number-onboarding-pcv.e2e-spec.ts",
          "sha256": "3825b0286f9906781e83666616caa05417647ee47c022763fc76e39a3c4ddca0"
        }
      ],
      "promotion_target": "inbox/integrations: trusted-window provenance and bounded query",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-05",
      "proposed_handling": "Preserve with bounded initial-send addition",
      "implementation_claim": "Same ST05 catalog; local preview and independent renderer/current same-account eligibility; Meta wire account pin/full international recipient.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/initial-message-template-renderer.ts",
          "sha256": "a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"
        },
        {
          "path": "api-app/src/domain/inbox/initial-message.service.ts",
          "sha256": "ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"
        },
        {
          "path": "api-app/src/integrations/meta/initial-message.client.ts",
          "sha256": "e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/test/initial-message.e2e-spec.ts",
          "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
        },
        {
          "path": "api-app/test/channel-transport.e2e-spec.ts",
          "sha256": "a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"
        }
      ],
      "promotion_target": "inbox/integrations: eligible template first-send, no authoring changes",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-06",
      "proposed_handling": "New bounded first-send contract",
      "implementation_claim": "Captured request/key/slot/context; all GET preflight then same-operation claim and onePOST; local-only reconciliation and explicit elapsed-deadline risk ACK.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/initial-message.service.ts",
          "sha256": "ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"
        },
        {
          "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
          "sha256": "bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"
        },
        {
          "path": "api-app/src/surfaces/bff/conversations.controller.ts",
          "sha256": "f8682cc211695df59caaa3f32799ad6a0444e120d683592e32984a71d71c8c1d"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/test/initial-message.e2e-spec.ts",
          "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
        },
        {
          "path": "api-app/test/dispatch-admission.e2e-spec.ts",
          "sha256": "ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47"
        }
      ],
      "promotion_target": "inbox: immutable intent and local recovery",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-07",
      "proposed_handling": "Preserve ordinary semantics with explicit interlock",
      "implementation_claim": "Owner tokens exclude initial intent while ordinary requests remain concurrent; uncertain token never expires into blind takeover. BFF empty thread requires first flow, public/BOT legacy behavior retained without slot.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/outbound.service.ts",
          "sha256": "0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"
        },
        {
          "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
          "sha256": "bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"
        },
        {
          "path": "web-app/src/telas/Inbox.tsx",
          "sha256": "bbd6facb3f60fafb01f661ec5fe6c0dec826b3023c9ba5ad44aec5b31865ddbd"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/test/dispatch-admission.e2e-spec.ts",
          "sha256": "ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47"
        },
        {
          "path": "api-app/test/channel-transport.e2e-spec.ts",
          "sha256": "a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"
        },
        {
          "path": "web-app/e2e/start-conversation.spec.ts",
          "sha256": "16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"
        }
      ],
      "promotion_target": "inbox/integrations: ordinary interlock and finite recovery; browser proof pending",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-08",
      "proposed_handling": "New bounded textual subset",
      "implementation_claim": "NAMED/POSITIONAL plain text from unchanged catalog components; static header/footer, <=20values, Unicode length and context-bound escaped read-only preview.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/initial-message-template-renderer.ts",
          "sha256": "a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"
        },
        {
          "path": "web-app/src/componentes/NovaConversa.tsx",
          "sha256": "2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts",
          "sha256": "c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"
        },
        {
          "path": "web-app/e2e/start-conversation.spec.ts",
          "sha256": "16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"
        }
      ],
      "promotion_target": "inbox: template subset and preview safety",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-09",
      "proposed_handling": "New bounded budgets/local proof",
      "implementation_claim": "Max6GET+1POST,10s/request75s aggregate90s immutable reservation; actor10/min,account60/hour. Additive migration and later approved preserved local proof.",
      "implementation_sources": [
        {
          "path": "api-app/src/integrations/meta/initial-message.client.ts",
          "sha256": "e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"
        },
        {
          "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
          "sha256": "bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/src/integrations/meta/initial-message.client.spec.ts",
          "sha256": "0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057"
        },
        {
          "path": "api-app/test/dispatch-admission.e2e-spec.ts",
          "sha256": "ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47"
        }
      ],
      "promotion_target": "integrations/inbox: budget invariants; actual-runtime proof pending",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    },
    {
      "decision_id": "D-10",
      "proposed_handling": "Preserve sole Message owner and explicit local certainty",
      "implementation_claim": "Positive commit/captured-key exact readback distinguishes ACK loss vs rollback; no claim/noPOST, no fake RECORDED or unsafe release; canonical opaque account hash namespace remains byte-compatible.",
      "implementation_sources": [
        {
          "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
          "sha256": "bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"
        },
        {
          "path": "api-app/src/domain/inbox/initial-message.service.ts",
          "sha256": "ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"
        },
        {
          "path": "api-app/src/domain/inbox/message-acceptance.service.ts",
          "sha256": "71194c70b12cb920054586a7a86266d90f8eca0b7008b1b5688627e0694979f1"
        },
        {
          "path": "api-app/src/integrations/channels/account-reference.ts",
          "sha256": "da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24"
        }
      ],
      "test_sources": [
        {
          "path": "api-app/test/dispatch-admission.e2e-spec.ts",
          "sha256": "ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47"
        },
        {
          "path": "api-app/test/initial-message.e2e-spec.ts",
          "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
        }
      ],
      "promotion_target": "inbox/integrations: commit certainty, CAS, known receipt and opaque account",
      "assessment": "Current full E54 candidate proof; original frozen decision remains authority, independent r2 assessment pending."
    }
  ]
}

```

### additive-migration-assessment-e45-v1.1.json

```json
{
  "kind": "Bounded additive migration assessment, disposable proof only",
  "recorded_at_utc": "2026-10-22T23:07:06.928239+00:00",
  "source_seal": "all-source-seal-e45-v1.1.json",
  "migrations": [
    {
      "path": "api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql",
      "sha256": "a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437",
      "bounded_transaction": true
    },
    {
      "path": "api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql",
      "sha256": "78963dce996b2cec9e0990812a5091725238f9995e892c196e614ce9b2a6464f",
      "bounded_transaction": true
    },
    {
      "path": "api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql",
      "sha256": "60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544",
      "bounded_transaction": true
    }
  ],
  "source_findings": [
    "Nullable official_inbound_at is added without fabricated backfill/default timestamp; selected-resource direction/origin timestamp index added.",
    "New finite dispatch admission and initial intent tables/enums; existing conversation FK references preserved with declared cascade only on future explicit parent deletion. No data deletion is executed by migration.",
    "SQL-only unreleased-slot partial unique, JSONB account-rate expression and COALESCE inbox-order indexes are explicit; ordinary admission owner nonce and initial BU+actor+key unique indexes remain represented.",
    "Nonconcurrent CREATE INDEX may take table write locks;5s lock wait/60s statement bound means local migration can fail. Never treat additive as lock-free, auto-retry, reset or skip unexpected pending drift."
  ],
  "actual_disposable_evidence": {
    "receipt": "all-result-e45-v1.1.json",
    "freshness": "browser-freshness-collection-e45-v1.1.json",
    "completed_migrations": 28,
    "schema_assertions": "dispatch-admission.e2e-spec.ts:87 asserts new columns/native precision/enums and intentional SQL-only indexes; actual PG tests include admission uniqueness and transaction barriers.",
    "explain_receipt": "pcv-eps-e45-v1.1.json"
  },
  "scope_limits": [
    "No whole-database schema equivalence claim from bounded new-column/index assertions.",
    "No migration, preflight connection, dump or data read on the preserved user test runtime has been performed.",
    "Apply only under the later approved local plan after exact local database identity/status/source preflight; stop on mismatch/lock failure.",
    "No destructive rollback. An older API lacks the new interlock; do not blindly revert after possible send or unresolved intent."
  ],
  "independent_status": "Candidate assessment submitted for fresh architecture/TQA/cutover challenge, not self-certified final delivery."
}

```

### local-activation-proof-plan-proposal-v1.1.json

```json
{
  "kind": "Reviewable future local activation/proof plan; NOT approved or executed",
  "governing_todo": "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
  "preconditions": [
    "Frozen complete candidate passes canonical all with identical pre/post public source manifest.",
    "Required independent implementation/migration/security/architecture assessments resolve material findings.",
    "Full diff guard inspection exception is separately explicit; no inferred private inspection.",
    "Reconfirm preserved local project identity from exact approved public topology and safe selected Docker metadata; stop on unexpected topology/resources."
  ],
  "proposed_target": {
    "project": "leadshug_channels_local",
    "profile": "channels-local",
    "public_composition": [
      "docker-compose.yml",
      "docker-compose.channels.yml"
    ],
    "operator_origin": "existing loopback gateway on127.0.0.1:8083; current availability unknown",
    "services_to_replace": [
      "api",
      "web"
    ],
    "services_to_preserve": [
      "postgres",
      "gateway",
      "evolution-postgres",
      "evolution-redis",
      "evolution"
    ],
    "data": "All existing volumes, BUs, channels, credentials and conversation history preserved. No reset/drop/truncate/deletion."
  },
  "build_provenance": [
    "Use explicit positive public build-input inventory from principal checkout; no root-wide context capture or private traversal.",
    "No copied writable checkout/worktree; disposable build context/archive is a generated build artifact only.",
    "Record approved public input hashes, image IDs/digests, API compiled hashes and Web built/served bundle equality.",
    "Do not claim an unbuilt source fingerprint as the served image. Fresh attestation must precede interpreting operator/browser proof.",
    "Public Dockerfiles were inspected for this proposal: API explicitly COPYs package/lock,prisma,src,tsconfigs,nest-cli and docker/entrypoint; Web uses COPY . . in its builder, so its generated build context must contain only individually admitted public inputs (never the whole checkout). These Dockerfiles are not mutated. Actual Alpine image health is required; Debian disposable-suite results alone do not establish native runtime compatibility."
  ],
  "proposed_private_exception": {
    "purpose": "Mechanical Compose consumption of the existing private test configuration to preserve current runtime settings.",
    "allowed": "Only existing .env.testing as an opaque input to existing Compose; no printing/copying/dumping values. Local migration process may use its existing DB connection in-memory.",
    "forbidden": "No .local-files access; no process argument/env/log dumps; no manual token/provider probe; no credential/session password read by agent; no private-file edits unless separately concrete and approved.",
    "unknown": "HTTPS current hostname/process state unknown; no existing tunnel adopted/killed by assumption. If origin change requires private-file mutation, prepare exact bounded change first."
  },
  "migration": [
    "Only three approved additive initial_message migrations from sealed source after disposable deploy/status/schema proof.",
    "Preflight exact local TEST database/service; record migration names/checksums/status and no unexpected pending drift.",
    "SET lock_timeout5s and statement_timeout60s as in approved SQL; stop on lock/migration failure; no blind retry/reset.",
    "No destructive down migration; rollback assessment is application compatibility plus preserved data, not dropping new tables/columns.",
    "Rollback assessment: an older API does not enforce the new initial-intent interlock. Do not automatically revert to an old API after a possible dispatch or while an initial outcome is unresolved; stop outbound use, preserve data and review the exact attempt in the normal UI. No destructive down/reset or blind migration retry is admitted. Initial activation checks precede operator sends."
  ],
  "activation": [
    "Recreate only selected API/Web using newly verified local images, no pull/restart of preserved providers or databases.",
    "Verify health and compiled/bundle equality through the existing gateway.",
    "Public gateway config uses static upstream host resolution. After API/Web replacement, validate nginx config and gracefully reload only the existing gateway process so it resolves current API/Web container addresses; preserve its container/network/volume. Record health and served bundle after reload, not an old cached upstream. No provider/database restart.",
    "If a new owned temporary HTTPS tunnel is needed, validate DNS/TLS/health/assets and then have operator update Meta callback/privacy URLs; no automatic provider configuration changes."
  ],
  "assisted_proof": [
    "Operator logs in normally; agent does not extract OWNER password or enumerate live business rows.",
    "In the nonofficial BU, operator opens a consenting test contact with explicit DDI, previews and confirms one first text; recipient replies.",
    "In the official BU, operator selects the already-approved own-account text template through the shared catalog, fills fictitious/test values, previews and confirms once; recipient replies.",
    "Record only safe outcome/state/timestamps and source-runtime attestation. Do not persist phone/contact/body/token.",
    "No automated sends, new contacts, routing changes, migration/registration at Meta, or Railway deployment."
  ],
  "current_status": "E54 full canonical ALL terminal0: API364/PG439/Web54/browser88, complete259source/93manifest/served-bundle binding and cleanup verified. Corrected current API177/Web47 public archive bytes rechecked, no images/activation yet. Fresh r2 implementation reviews required.",
  "build_context_positive_inputs": {
    "api": {
      "roots": [
        "api-app/src",
        "api-app/prisma"
      ],
      "exact_files": [
        "api-app/Dockerfile",
        "api-app/package.json",
        "api-app/package-lock.json",
        "api-app/tsconfig.json",
        "api-app/tsconfig.build.json",
        "api-app/nest-cli.json",
        "api-app/docker/entrypoint.sh"
      ]
    },
    "web": {
      "roots": [
        "web-app/src"
      ],
      "exact_files": [
        "web-app/Dockerfile",
        "web-app/package.json",
        "web-app/package-lock.json",
        "web-app/tsconfig.json",
        "web-app/vite.config.ts",
        "web-app/index.html",
        "web-app/nginx/default.conf.template",
        "web-app/docker/40-config-js.sh",
        "web-app/public/config.js",
        "web-app/public/privacidade.html"
      ]
    },
    "policy": "Reject symlinks; hash each positive input, produce generated archive only. Exclude every .env, node_modules, existing dist, e2e/test artifacts and all unlisted paths. Add no extra file by discovery or implicit COPY context. Source specs under admitted src remain public build inputs; build exclusions remain canonical."
  },
  "prepared_build_context_receipt": "positive-build-contexts-e53-v1.1.json",
  "entrypoint_scope": "Existing API entrypoint mechanically keeps ownership of the preserved named file volume at /dados/arquivos, then runs as node. No host .local-files bind, agent content inspection, payload mutation or file deletion is proposed.",
  "candidate_receipt": "all-result-e54-v1.1.json",
  "build_context_current_recheck": "positive-build-contexts-e54-recheck-v1.1.json"
}

```

### final-diff-guard-boundary-proposal-v1.1.json

```json
{
  "kind": "Concrete proposed one-time delivery inspection exception; NOT approved or executed",
  "governing_todo": "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
  "existing_restriction": "The approved TODO forbids reading/listing/stat/hash/traversal/mount of private paths, and permits only positive public inspection. No exception has been inferred.",
  "why_needed": "The required unmodified canonical todo_diff_expectation_guard.py enumerates real tracked and non-ignored untracked differences for all four declared repositories. It has no positive-pathspec/private-prune argument. A public-only inventory cannot truthfully substitute for that guard.",
  "proposed_exception": {
    "purpose": "One-time canonical delivery diff inspection, after the functional candidate and reviewable evidence are complete.",
    "scope": "Only operations the canonical guard and its Git subprocesses require for declared root/api/web/foundation repository baselines.",
    "private_access": "May enumerate/stat private paths and internally read/hash tracked file bytes as Git requires to compare changes or detect renames. No private file content is printed or published.",
    "mutations": "None: no private-file edits/deletes, Git staging/commit, topology changes or service/provider changes are authorized by this exception.",
    "raw_result_destination": "Restricted local /tmp files, mode0600; do not commit raw stdout/JSON or private filenames.",
    "public_receipt": "Tool-source hash, exact canonical arguments, terminal exit/outcome, counts and stable violation codes only. No private path values or content.",
    "on_failure": "Classify and report the guard failure; do not erase private files, silently filter violations, edit Delphi or claim GO.",
    "scope_lifetime": "One completed canonical guard run and redacted collection; follow-up private inspection requires its own established authority."
  },
  "canonical_command_proposed": [
    "python3",
    "delphi-ai/tools/todo_diff_expectation_guard.py",
    "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
    "--repo-root",
    "/mnt/c/unifast/leadshug/leadshug_now_docker",
    "--json-output",
    "/tmp/stcon04-final-diff-guard-private.json"
  ],
  "approval_handling": "Present the concrete candidate and this exact exception to the user before any private inspection. If explicitly approved, record the limited exception in the governing TODO and re-run normal authority before executing. No implementation scope, DoD or classifier weakening is proposed.",
  "current_status": "Proposal only. Implementation and positively bounded test work continue. Full diff-guard GO remains absent.",
  "other_closeout_helpers_assessment": {
    "todo_completion_guard": "Use explicit governing TODO argument, not --all-completed; inspected helper reads documentary TODO/evidence, no Git/private product enumeration.",
    "todo_closeout_guard": "Use canonical --repo foundation_documentation with explicit governing TODO. Inspected git_context invokes full status only on that selected Foundation repository; this is the authorized documentary authority, not root/API/Web private-product repositories. No private-product exception inferred for closeout.",
    "scope_lifetime": "Only the full diff guard remains the proposed one-time private inspection exception. Runtime opaque Compose configuration access is separately named in the activation proposal."
  }
}

```

### root-topology-inspection-deviation-e35a-v1.1.json

```json
{
  "checkpoint": "E35a root inspection deviation",
  "actor": "root orchestrator",
  "trigger": "Read-only investigation of canonical final diff guard versus no-private-inspection boundary",
  "action": "A bounded cat command read the exact root .gitmodules together with exact public .gitignore files.",
  "contract_violation": "Root .gitmodules is an explicit Not Expected Changed Paths row whose reason also disallows inspection. Its known/public nature did not override the approved boundary.",
  "observed_output": "Three submodule path and public GitHub URL declarations; no credential value was returned.",
  "containment": [
    "No write, stage, commit or topology operation on .gitmodules occurred.",
    "Root stopped that inspection path and retains the canonical diff-guard incompatibility as unresolved.",
    "Do not repeat the read or infer a general metadata/private-inspection waiver."
  ],
  "assurance": "Preserve for independent adherence/security/final review alongside E02, mixed test chronology and E18. No claim of full procedural/privacy compliance.",
  "product_authority": "No product scope expansion; sole writer and candidate validation freeze rules remain unchanged."
}

```

### execution-discovery-deviation-e02-v1.1.json

```json
{
  "recorded_at_utc": "2026-10-22T15:21:30.829820+00:00",
  "incident": "executor used non-admitted recursive AGENTS discovery",
  "reported_command": "find .. -name AGENTS.md -print followed by public documentation reads",
  "cwd": "/mnt/c/unifast/leadshug/leadshug_now_docker",
  "original_tool_return": "executor printed only empty output, losing any session/terminal metadata; termination and traversed scope cannot be established",
  "private_content_returned": false,
  "private_traversal_outcome": "unknown; forbidden traversal could have occurred; not a privacy compliance pass",
  "containment": {
    "broad_discovery": "stopped and expressly prohibited; positive public inventories only",
    "process_probe": "pgrep -x find",
    "probe_exit_code": 1,
    "probe_result": "no live find PID; no args/env/process logs read",
    "private_remediation": "none; no further private surface inspected; no credential exposure inferred"
  },
  "continuation": "authorized public product work and single canonical disposable RED runner only",
  "required_follow_up": "carry incident into independent security/adherence/final review; no claim that this session never traversed private paths"
}

```

### test-causality-chronology-r1-v1.1.json

```json
{
  "kind": "Honest test causality and regression chronology",
  "version": "1.1",
  "recorded_at_utc": "2026-10-22T23:47:37.148844+00:00",
  "finding": "TQA-ST04-04",
  "scope": "ST-CON-04 whole approved journey, including inherited and new verification",
  "adjudication": "Test-first coverage is partial. Final-state regression, post-hoc controlled reversion, module loading and causal assertion failures are distinct evidence classes. No retroactive reversion or repeated run solely to fabricate chronology.",
  "rows": [
    {
      "checkpoint": "E03",
      "source_receipt": "executor-red-e03-v1.1.json",
      "classification": "module-loading only",
      "observed_fact": "New modules absent; 3 suites fail to load, 284 existing tests pass and zero behavior assertions fail.",
      "claim_limit": "No business-level test-first proof."
    },
    {
      "checkpoint": "E04",
      "source_receipt": "TODO#E04",
      "classification": "mixed chronology",
      "observed_fact": "After compile-only repair, RED3 reaches two renderer assertions before their fixes; later RED4 temporarily reverts a preliminary implementation and reaches six failures.",
      "claim_limit": "RED3 causal only for reached renderer assertions; RED4 controlled post-hoc verification, never original test-first."
    },
    {
      "checkpoint": "E11",
      "source_receipt": "transport-valid-red-e11-v1.1.json",
      "classification": "causal assertion RED",
      "observed_fact": "Corrected transport fixture reaches three failures before transport implementation: unsupported Evolution dispatch and missing Meta protocol delegation.",
      "claim_limit": "Earlier invalid protocol fixture is not product RED; later pin/fence assertions not reached."
    },
    {
      "checkpoint": "E15",
      "source_receipt": "dispatch-admission-red-e15-v1.1.json",
      "classification": "module-loading only",
      "observed_fact": "Absent new admission implementation prevents suite loading; 311 existing unit tests pass.",
      "claim_limit": "Admission behavior and PostgreSQL assertions not reached."
    },
    {
      "checkpoint": "E21/E22",
      "source_receipt": "outbound-causal-red-e21-v1.1.json; outbound-valid-red-e22-v1.1.json",
      "classification": "causal assertion RED",
      "observed_fact": "Before ordinary sender admission wiring, split tests reach missing reserve/claim, prepared release, uncertain settlement and refusal settlement assertions.",
      "claim_limit": "Unit boundary proof only; real PG/concurrency is later regression verification."
    },
    {
      "checkpoint": "E25",
      "source_receipt": "initial-coordinator-red-e25-v1.1.json",
      "classification": "module-loading plus unrelated assertion failures",
      "observed_fact": "Coordinator import is absent-module failure; two actual assertions fail in admission/protocol suites.",
      "claim_limit": "No request/idempotency/coordinator business assertion RED; other failures require their own causal classification."
    },
    {
      "checkpoint": "E35",
      "source_receipt": "browser-result-e35-v1.1.json",
      "classification": "causal browser assertion RED",
      "observed_fact": "Actual first-message field is missing before new initial-send UI implementation. Real BFF open/empty PG/zero-provider assertions passed first.",
      "claim_limit": "Existing manual-open UI/backend predates test; later ordinary-composer assertion not reached."
    },
    {
      "checkpoint": "E41",
      "source_receipt": "all-result-e41-v1.1.json",
      "classification": "mixed product and test-support failures",
      "observed_fact": "Actual UI reuse state loss and missing AMBIGUOUS state projection fail before their corrections.",
      "claim_limit": "Fixture reassignment/audit omission/cumulative counters/mapping expectations are not product behavior REDs; shell exit metadata unavailable, no invented exit code."
    },
    {
      "checkpoint": "E44/E45",
      "source_receipt": "storage-read-recovery-evidence-loop-v1.1.json",
      "classification": "causal browser regression RED then full GREEN",
      "observed_fact": "Actual accepted-send/lost-response/storage-read failure deletes original replay snapshot; failure precedes fix preserving key/body and blocking unsafe actions; full E45 all passes.",
      "claim_limit": "Only named storage recovery behavior has this causal history; whole suite does not inherit it."
    },
    {
      "checkpoint": "E46/E47",
      "source_receipt": "browser-result-e46-v1.1.json; browser-result-e47-v1.1.json",
      "classification": "post-implementation recovery coverage",
      "observed_fact": "New ordinary recovery case first fails an invalid fake-effects counter; narrow correction followed by full86browser pass.",
      "claim_limit": "Counter failure is not production RED. Added ordinary UI recovery coverage is post-implementation regression proof."
    },
    {
      "checkpoint": "E48/E49",
      "source_receipt": "api-result-e48-v1.1.json; api-result-e49-v1.1.json",
      "classification": "test-support failures before target regressions",
      "observed_fact": "E48 lint fails on spy assertion capture in finally; E49 lint/build pass, 362unit tests pass and one negative-control detector test fails because axios.post is not recognized. PostgreSQL never reached.",
      "claim_limit": "Neither failure proves a production defect. PREPARED payload and r1 behavior assertion RED still pending. Product unchanged; detector and contract tests are being corrected before next run."
    },
    {
      "checkpoint": "E50",
      "source_receipt": "api-result-e50-v1.1.json; api-source-recheck-e50-v1.1.json; prepared-recovery-live-payload-e50-v1.1.json",
      "classification": "causal real PostgreSQL/BFF assertion RED",
      "observed_fact": "Before product fixes, four integration tests fail on PREPARED action/active-slot safe metadata and wrong ordinary code, full-history COUNT, omitted realtime creation-winner event and ordinary201 after actual settlement rollback. 363unit and435otherPG tests pass.",
      "claim_limit": "Actual owned synthetic state and payload proof, no real provider/preserved runtime claim. Local PREPARED live202 and expired REJECTED release steps passed; missing browser action proof still pending."
    },
    {
      "checkpoint": "E51",
      "source_receipt": "web-result-e51-v1.1.json; web-source-recheck-e51-v1.1.json",
      "classification": "causal Unicode snapshot assertion RED",
      "observed_fact": "Valid1024astral POSITIONAL parameter is rejected before product fix; prior text4096/4097 code-point checks pass. Build and53otherWebunit tests pass.",
      "claim_limit": "Later NAMED branch and positional1025 assertion were not reached in combined test; require final complete passing unit and actual input/browser proof."
    },
    {
      "checkpoint": "E52/E53/E54",
      "source_receipt": "candidate-source-preflight-e52-v1.1.json; all-result-e53-v1.1.json; all-source-seal-e54-v1.1.json",
      "classification": "faithful fixture/source preflight and post-implementation test baseline repair",
      "observed_fact": "E52 did not run: fixture corrected to real owner reservation with90s lease and full canonical data, early UIACK tests actual BFF409 rather than adding an unapproved timer feature. E53 product regressions pass (364unit/438PG); new late-old test incorrectly compares to pre-ACK null timestamp, while actual late state is SUCCEEDED and release remains nonnull. E54 changes only that test to exact post-ACK timestamp and reruns full ALL.",
      "claim_limit": "E53 stale expectation is not product RED. E54 currently running; 12initial-message PG tests passed individually, no full candidate/Web/browser result yet."
    }
  ],
  "broader_coverage": "Most PostgreSQL fault/commit/protocol/boundary/rate/concurrency cases were added alongside or after their production implementation. They are meaningful final-state regression evidence, not universally pre-implementation causal RED.",
  "review_correction": "The broad r1 reviewer shorthand naming E03/E25 as selected causal RED is qualified here by exact receipts: their new coordinator/admission behavior failed to load and did not reach business assertions. Original raw review results remain immutable.",
  "method_assessment": "No generic rule/analyzer edit is warranted solely by chronology. Preserve evidence classification and add actual causal regressions for newly found bugs before fixing those bugs.",
  "resolution": "Explicit chronology correction complete. Current newly found product regressions now have actual causal E50/E51 assertions before their fixes; original alongside/post-implementation chronology remains unchanged. Independent reassessment pending."
}

```

### implementation-r1-finding-triage-v1.1.json

```json
{
  "kind": "Authoritative root r1 finding triage and in-scope remediation plan; fixes pending",
  "recorded_at_utc": "2026-10-22T23:40:01.058997+00:00",
  "candidate_source_seal": "browser-source-seal-e47-v1.1.json",
  "deduplication": "Root ST04-PREPARED-RECOVERY-01 is same locus as ARCH-ST04-R1-01/F-3E65B77F, not an eleventh finding.",
  "rows": [
    {
      "finding_id": "F-511FF1D6",
      "source_finding_id": "ARCH-ST04-R1-06",
      "review_kind": "architecture_adherence",
      "severity": "medium",
      "title": "The dependency protection harness omits the new initial coordinator",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Add companion protection in admitted channel-initial-message.spec.ts with synthetic forbidden coupling controls.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Edit sealed inherited harness (unneeded approval deviation).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Leave new coordinator outside protection.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Current coordinator has no forbidden dispatch; this is harness coverage added after implementation, not a product RED. Keep inherited38protected bytes.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    },
    {
      "finding_id": "F-8E89FC19",
      "source_finding_id": "ARCH-ST04-R1-02",
      "review_kind": "architecture_adherence",
      "severity": "medium",
      "title": "Ordinary success ignores an unconfirmed settlement result",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Check positive settlement boolean; preserve known ACK/recorded Message in incomplete result when false.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Introduce additional settlement retry machinery (unneeded extra semantics).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Report normal success while durable exclusion remains unresolved.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Root verified boolean false path is ignored by current Outbound.send; real rollback/ACK-loss regression queued.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    },
    {
      "finding_id": "F-ED2FCC37",
      "source_finding_id": "ARCH-ST04-R1-03",
      "review_kind": "architecture_adherence",
      "severity": "medium",
      "title": "Local initial reconciliation omits realtime publication for its creation winner",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Publish only after confirmed local creation-winner commit through same common owner, echo/replay zero.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Add a new worker/outbox subsystem (outside scope).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Leave recovered creation unannounced until polling.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Root verified reconcile returns accepted.message without using creationWinner; PG event counter regression queued.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    },
    {
      "finding_id": "F-C8AF5811",
      "source_finding_id": "ARCH-ST04-R1-05",
      "review_kind": "architecture_adherence",
      "severity": "medium",
      "title": "Every ordinary BFF send counts the complete message history",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Use bounded indexed existence lookup and actual large-history query proof.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Introduce a cached Message-count write model (extra consistency burden).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Keep full history COUNT per ordinary BFF send.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Message.channelOrigin is required ChannelType in schema; every Message is transport, so preserve existing conversation predicate without inventing a new filter/index. Root confirmed COUNT is only used for existence.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    },
    {
      "finding_id": "F-3E65B77F",
      "source_finding_id": "ARCH-ST04-R1-01",
      "review_kind": "architecture_adherence",
      "severity": "medium",
      "title": "An abandoned PREPARED attempt has no usable browser recovery action",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Expose existing local PREPARED reconciliation, with live-lease retention and expired safe release.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Mutate/clean up PREPARED implicitly during GET (changes observational semantics).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Leave the operator stranded with only GET/manual tooling.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Source independently confirmed by root/executor and fresh architecture reviewer; actual new BFF RED queued E48.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    },
    {
      "finding_id": "F-F7C06078",
      "source_finding_id": "ARCH-ST04-R1-04",
      "review_kind": "architecture_adherence",
      "severity": "medium",
      "title": "Active-slot refusals do not implement the frozen interlock error contract",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Implement exact frozen BLOCKED/INITIAL_SEND_IN_PROGRESS and authorized ordinary-token conflict metadata; preserve empty INITIAL_SEND_REQUIRED and other legacy mappings.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Change approved contract to match weaker implemented codes (would require renewed approval).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Retain conflated empty/active slot errors and missing scoped metadata.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Frozen D07 and normative interlock explicitly define these distinctions; tests must protect approved behavior, not current divergent codes.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    },
    {
      "finding_id": "F-B25EB3CF",
      "source_finding_id": "TQA-ST04-02",
      "review_kind": "test_quality_audit",
      "severity": "high",
      "title": "Required full browser-platform evidence is not terminal for the current E47 source seal",
      "classification": "release-blocker",
      "status": "fixed",
      "planned_resolution": "Integrate",
      "actual_resolution": "Integrated with actual E47 terminal proof",
      "options": [
        {
          "id": "A",
          "action": "Collect current full E47 terminal/cleanup/independent postseal.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Waive full platform evidence (neither necessary nor authorized).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Infer aggregate GREEN from one test.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Resolved by actual E47terminal0/86pass/cleanup/postseal259fp603cc.../93freshness hashes. This resolves E47 only; changed E48+candidate needs its own fresh full run.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "root documentation/evidence"
    },
    {
      "finding_id": "F-8D9F2A1C",
      "source_finding_id": "TQA-ST04-01",
      "review_kind": "test_quality_audit",
      "severity": "high",
      "title": "Browser snapshot and input limits use UTF-16 length while server template validation uses Unicode code points",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Match code-point input/parameter-snapshot limits with server; retain separate JSON size budget and exact Unicode boundary/browser proof.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Reduce server to UTF16 units (rejects approved valid text).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Keep valid astral messages blocked.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Confirmed for parameter snapshots and HTML maxLength. Free-text snapshot already uses code points at139; preserve that correct guard instead of repeating the reviewer overbroad subclaim.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    },
    {
      "finding_id": "F-9EFF5F01",
      "source_finding_id": "TQA-ST04-04",
      "review_kind": "test_quality_audit",
      "severity": "medium",
      "title": "Test-first evidence is partial; most behavior-defining fault and protocol coverage is retrofit evidence",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Preserve group-level causal vs post-implementation chronology and enforce fail-first for current new defects.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Rewrite history as if all tests were fail-first (invalid).",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Leave broad test-first implication unqualified.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Most later fault/protocol tests are final-state regression evidence. No retroactive reversion RED or missing-module bootstrap as a business assertion proof. Detailed chronology qualification still to consolidate; no product change follows merely from history.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "root documentation/evidence",
      "root_chronology_correction": "Detailed honest evidence classifications recorded in test-causality-chronology-r1-v1.1.json; current status remains open for independent reassessment, not a product fix or claim of universal test-first."
    },
    {
      "finding_id": "F-B360C531",
      "source_finding_id": "TQA-ST04-03",
      "review_kind": "test_quality_audit",
      "severity": "medium",
      "title": "Acknowledgement coverage does not fully exercise EXTERNAL_ACCEPTED_LOCAL_BLOCKED through the BFF lifecycle",
      "classification": "release-blocker",
      "status": "open",
      "planned_resolution": "Integrate",
      "actual_resolution": "Pending integration; no fix/PASS claimed",
      "options": [
        {
          "id": "A",
          "action": "Reach known-accepted/local-blocked state through actual BFF, assert early/late ACK and successor isolation/zero resend, then UI consumer coverage.",
          "assessment": "recommended, existing approved objective"
        },
        {
          "id": "B",
          "action": "Rely on pure predicate and AMBIGUOUS-only endpoint proof.",
          "assessment": "not recommended"
        },
        {
          "id": "C",
          "action": "Leave irreversible known-ACK release unexercised.",
          "assessment": "not acceptable for current delivery confidence"
        }
      ],
      "source_assessment": "Existing known-blocked case736 uses local reconcile to success, not ACK; new endpoint lifecycle coverage is required.",
      "same_scope_basis": "Already-approved recovery/dispatch/renderer/performance/protection and evidence contract; no new product behavior/provider/state/migration/global platform.",
      "formalization": "Candidate hints preserved in original review; no analyzer/Delphi rule implementation authorized.",
      "remediation_owner": "stcon04_continuation sole code writer; root assurance"
    }
  ],
  "scope_admission": "API tests/dispatch/initial/new companion and Web Unicode tests remain in current admitted paths. Sealed inherited dependency harness and Typebot/PCV companions are not reopened. No additional approval requested for these already-authorized correctness fixes.",
  "stage": "E47fullGREEN does not close assurance findings; E48test-only handoff released after actual terminal/postseal/r1collection and normal authorityGO.",
  "follow_up_policy": "No product finding discarded as nonblocking. All material fixes/coverage addressed in current TODO; optional rule formalization hints remain proposals only, not an invented scope."
}

```

### implementation-r1-resolution-v1.1.json

```json
{
  "kind": "Actual integrated r1 finding resolutions for fresh independent r2 challenge",
  "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
  "source_seal": "all-source-seal-e54-v1.1.json",
  "rows": [
    {
      "finding_id": "F-511FF1D6",
      "source_finding_id": "ARCH-ST04-R1-06",
      "review_kind": "architecture_adherence",
      "resolution": "Integrated",
      "resolution_evidence": "Current coordinator dependency harness added with actual-source import/HTTP protection and synthetic forbidden controls.",
      "source": {
        "path": "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
        "sha256": "46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-8E89FC19",
      "source_finding_id": "ARCH-ST04-R1-02",
      "review_kind": "architecture_adherence",
      "resolution": "Integrated",
      "resolution_evidence": "Ordinary local settlement must be positive; false/throw returns known accepted/local incomplete preserving Message and ACK; actual PG rollback regression passed.",
      "source": {
        "path": "api-app/src/domain/inbox/outbound.service.ts",
        "sha256": "0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-ED2FCC37",
      "source_finding_id": "ARCH-ST04-R1-03",
      "review_kind": "architecture_adherence",
      "resolution": "Integrated",
      "resolution_evidence": "Only confirmed local creationWinner publishes best-effort realtime after commit; replay/echo/uncertain readback do not duplicate.",
      "source": {
        "path": "api-app/src/domain/inbox/outbound.service.ts",
        "sha256": "0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-C8AF5811",
      "source_finding_id": "ARCH-ST04-R1-05",
      "review_kind": "architecture_adherence",
      "resolution": "Integrated",
      "resolution_evidence": "Ordinary BFF uses bounded findFirst select id rather than whole-history COUNT; query-event regression passed.",
      "source": {
        "path": "api-app/src/domain/inbox/initial-message.service.ts",
        "sha256": "ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-3E65B77F",
      "source_finding_id": "ARCH-ST04-R1-01",
      "review_kind": "architecture_adherence",
      "resolution": "Integrated",
      "resolution_evidence": "PREPARED safe action RECONCILE; actual E50 before payload RED and full E54 PG/UI live/expired zero-network proof.",
      "source": {
        "path": "api-app/src/domain/inbox/initial-message.service.ts",
        "sha256": "ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-F7C06078",
      "source_finding_id": "ARCH-ST04-R1-04",
      "review_kind": "architecture_adherence",
      "resolution": "Integrated",
      "resolution_evidence": "Active initial conflict includes scoped safe attemptId/state and BLOCKED; empty remains REQUIRED; ordinary admissions use bounded scoped10+truncation.",
      "source": {
        "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
        "sha256": "bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-B25EB3CF",
      "source_finding_id": "TQA-ST04-02",
      "review_kind": "test_quality_audit",
      "resolution": "Integrated",
      "resolution_evidence": "E47 actually terminated86pass with cleanup/postseal; current corrected E54 now actually terminated88pass with full259/93 source/bundle binding.",
      "source": {
        "path": "web-app/e2e/start-conversation.spec.ts",
        "sha256": "16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-8D9F2A1C",
      "source_finding_id": "TQA-ST04-01",
      "review_kind": "test_quality_audit",
      "resolution": "Integrated",
      "resolution_evidence": "Input clamps and named/positional snapshot validation use code points; E51 causal RED then current unit and Unicode browser proof; separate JSON bound preserved.",
      "source": {
        "path": "web-app/src/componentes/NovaConversa.tsx",
        "sha256": "2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-9EFF5F01",
      "source_finding_id": "TQA-ST04-04",
      "review_kind": "test_quality_audit",
      "resolution": "Integrated",
      "resolution_evidence": "Chronology corrected explicitly: absent-module/fixture/detector failures and post-hoc reversion never business assertion test-first; mixed sequencing remains disclosed, not retroactively fixed.",
      "source": {
        "path": "api-app/test/initial-message.e2e-spec.ts",
        "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    },
    {
      "finding_id": "F-B360C531",
      "source_finding_id": "TQA-ST04-03",
      "review_kind": "test_quality_audit",
      "resolution": "Integrated",
      "resolution_evidence": "Actual EALB early UI409 unchanged slot, disposable expiry ACK200, successor and late-old local reconciliation isolating owner/provider verified in full E54.",
      "source": {
        "path": "web-app/e2e/start-conversation.spec.ts",
        "sha256": "16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"
      },
      "proof": [
        "all-result-e54-v1.1.json",
        "all-source-recheck-e54-v1.1.json"
      ],
      "limits": "Fresh r2 challenge still required; no delivery/real-provider claim."
    }
  ],
  "chronology": "test-causality-chronology-r1-v1.1.json",
  "remaining": "Runtime/operator/module/guard/final review gates remain; no waiver or unsupported completion."
}

```

### api-result-e50-v1.1.json

```json
{
  "checkpoint": "E50 actual r1 causal assertion RED before product fixes",
  "exit_code": 1,
  "session": 25991,
  "recorded_at_utc": "2026-10-23T00:00:01.821396+00:00",
  "stdout_sha256": "07889c1cf4d849be54524d3f0b62971c2371dd09c8bed504a4a88adfc5fcdd2c",
  "source_count": 259,
  "source_fingerprint": "c4f327b54a574e7ac9850fb83141aca9beeabeb3b390cb28276b86a88541bbfc",
  "full_inventory_and_bytes_match_preseal": true,
  "production_and_fixtures_unchanged_from_e47": true,
  "phases": {
    "migrations_lint_build": "passed",
    "unit": {
      "files_passed": 34,
      "tests_passed": 363
    },
    "postgresql": {
      "files_passed": 31,
      "files_failed": 2,
      "tests_passed": 435,
      "tests_failed": 4
    },
    "cleanup": "actual owned containers volumes network removal observed"
  },
  "failures": [
    "PREPARED scoped projection recoveryAction null; active ordinary send wrong REQUIRED code and competing initial conflict lacks attempt/state. Soft assertions allow remaining local recovery checks.",
    "Ordinary-send query event capture contains COUNT(*) over messages instead of bounded existence.",
    "Local initial creation-winner reconcile publishes zero realtime events, expected one.",
    "Ordinary provider ACK and Message accepted but real settlement rollback still returns normal201."
  ],
  "causal_limits": [
    "Actual assertions precede corresponding product changes.",
    "PREPARED live202/no release and expired200 REJECTED/released local recovery checks executed and passed despite soft projection failures; no extra provider/Message.",
    "Known-accepted blocked ACK lifecycle case passed in PostgreSQL; real browser counterpart still pending.",
    "Architecture current-source and synthetic negative controls passed after test-detector repair; this is post-implementation harness protection, not a product defect RED.",
    "Unicode Web not run yet. Full candidate GREEN, actual providers, preserved runtime and final delivery not claimed."
  ],
  "safe_synthetic_markers": [
    "ST04_PREPARED_OPTIONS {\"state\":\"PREPARED\",\"recoveryAction\":null}",
    "ST04_ACTIVE_SLOT_CONFLICT {\"code\":\"INITIAL_SEND_IN_PROGRESS\",\"attemptId\":null,\"state\":null}"
  ]
}

```

### web-result-e51-v1.1.json

```json
{
  "checkpoint": "E51 actual Unicode snapshot causal assertion RED before product fix",
  "exit_code": 1,
  "session": 70146,
  "stdout_sha256": "f3f11e53cbe8ccb46dd27fcd6512853611b7cd7bc3ddbef9e9cb8fff1da37677",
  "recorded_at_utc": "2026-10-23T00:02:00.440091+00:00",
  "source_count": 259,
  "source_fingerprint": "c4f327b54a574e7ac9850fb83141aca9beeabeb3b390cb28276b86a88541bbfc",
  "full_inventory_and_bytes_match_preseal": true,
  "phases": {
    "web_build": "passed,60modules",
    "unit": {
      "files_passed": 6,
      "files_failed": 1,
      "tests_passed": 53,
      "tests_failed": 1
    },
    "cleanup": "owned removal observed"
  },
  "causal_failure": "isInitialSendSnapshot rejects valid POSITIONAL parameter with1024astral code points because .length counts2048UTF16 units. Actual assertion NovaConversa.spec.ts69 before fix.",
  "prior_assertions_passed": [
    "4096astral free text accepted",
    "4097astral free text rejected",
    "JSON envelope remains below32768units"
  ],
  "not_reached": [
    "Later positional1025 rejection",
    "NAMED1024/1025 branch in same combined case"
  ],
  "required_final_coverage": [
    "Both POSITIONAL/NAMED snapshot bounds",
    "Real browser input value/preview/send/persistence without HTML UTF16 truncation"
  ],
  "limits": "Unit/build only; no actual browser/PG/external provider/preserved runtime or delivery claim.",
  "next": "Sole writer may now fix r1 defects inside admitted scope and add real BFF/PG browser recovery proof; final candidate requires fresh complete freeze/all/independent review."
}

```

### prepared-recovery-evidence-loop-v1.1.json

```json
{
  "kind": "Living prepared-recovery evidence loop; initial pre-test answers retained with later execution update",
  "issue_id": "ST04-PREPARED-RECOVERY-01",
  "recorded_at_utc": "2026-10-22T23:30:06.267282+00:00",
  "skill": "delphi-ai/skills/bug-fix-evidence-loop/SKILL.md",
  "source_finding": "prepared-recovery-source-finding-e47-v1.1.json",
  "mandatory_questions": [
    {
      "question": 1,
      "answer": "No end-to-end PREPARED crash/read→UI reconciliation proof found. Existing PG tests exercise prepare/claim/expiry cleanup; UI/browser recovery proves SENDING/AMBIGUOUS/known receipt and ordinary uncertainty, not a persisted PREPARED activeAttempt action."
    },
    {
      "question": 2,
      "answer": "Current source/projection/render chain was inspected by root and executor. No actual preserved user DB/payload was read, by approved privacy boundary. Capture actual owned disposable PostgreSQL row and scoped BFF GET payload before fix in the new targeted test; this is still pending, not a fictitious runtime sample."
    },
    {
      "question": 3,
      "answer": "No existing test failed for this state omission. E45fullGREEN and E47 current individual recovery PASS concern other states. E46 effects-counter failure was a fake observation mismatch unrelated to this defect. A runtime false-green label waits for concrete new contract assertion RED."
    },
    {
      "question": 4,
      "answer": "Before product changes, add actual PG/BFF PREPARED read-model regression for unexpired/expired durable unclaimed intents, expecting the existing local reconciliation action and verifying read does not mutate/dispatch. Add actual browser persisted-PREPARED recovery coverage through scoped BFF POST and exact state/provider/Message audits; do not fabricate provider death, rewrite a sent intent into PREPARED or stub BFF payloads. Final suite exercises full UI flow."
    },
    {
      "question": 5,
      "answer": "Provisional no-rule-needed: this is a finite recovery state→action semantic omission across safe DTO and rendering. Exhaustive enum syntax alone can still explicitly map PREPARED to wrong null; a generic analyzer cannot safely infer this product action policy. Add behavior/state coverage and preserve same local-only recovery owner. No Delphi/analyzer edits authorized."
    }
  ],
  "coverage_chain": [
    {
      "stage": "Persisted PREPARED and deadline CAS/reconciliation",
      "state": "covered",
      "evidence": "Existing dispatch-admission actual PG tests; new consumer action proof missing."
    },
    {
      "stage": "BFF projectIntent safe state/action DTO",
      "state": "missing",
      "evidence": "Source maps PREPARED to null; new actual PG/BFF assertion needed before fix."
    },
    {
      "stage": "API client typed InitialAttempt",
      "state": "covered",
      "evidence": "Existing RECONCILE value accepted; no new enum/provider-specific operation required."
    },
    {
      "stage": "React locked recovery branch and local POST handler",
      "state": "missing",
      "evidence": "Button only when recoveryAction RECONCILE. PREPARED receives null and GET consult does not change it."
    },
    {
      "stage": "Full browser recovery after persisted preparation interruption",
      "state": "missing",
      "evidence": "Queue new real-BFF/PG Playwright scenario; final actual assertion result pending."
    }
  ],
  "selected_direction": "OptionA: expose existing local-only reconciliation through the safe PREPARED projection and existing UI action; preserve GET read-only, same grant/CSRF/immutable lease/owner CAS and no automatic dispatch. Final code choice awaits independent findings and exact regression design.",
  "sequencing": "Keep E47 and live r1 source packets frozen. Wait actual runner terminal/cleanup/postseal and review lifecycle terminal before sole-writer test-first handoff. No test-only route in production or additional provider/platform capability.",
  "proof_limits": "Historical E47/E50 answers are retained. E54 now proves corrected valid PREPARED producer, read-only BFF projection and actual UI local reconciliation with real disposable PG. No preserved runtime/provider delivery claim.",
  "execution_update": {
    "checkpoint": "E50 actual terminal1 with root full259source postseal",
    "recorded_at_utc": "2026-10-23T00:03:57.063457+00:00",
    "actual_payload": {
      "state": "PREPARED",
      "recoveryAction": null
    },
    "evidence": [
      "prepared-recovery-live-payload-e50-v1.1.json",
      "api-result-e50-v1.1.json",
      "api-source-recheck-e50-v1.1.json"
    ],
    "questions_updated": {
      "2": "Yes: actual valid owned disposable PostgreSQL reservation plus authenticated scoped BFF options and attempt GET, captured before product fix. No actual preserved private database or payload was accessed.",
      "3": "New exact regression fails on PREPARED recoveryAction and active-slot contract while existing E47 full browser was GREEN. Earlier tests covered other states and lacked this durable PREPARED producer/consumer branch. E50 is concrete assertion RED, not just source inference.",
      "4": "New BFF test reaches actual observational reads, live local202 unchanged slot, and expiry local rejection/release with zero extra provider and Message. Final real browser action test remains required before closing the UI gap."
    },
    "current_coverage": {
      "persistence_and_local_recovery": "covered by actual E50 PG steps",
      "BFF_safe_action_projection": "new regression catches failure before fix",
      "React_button_and_full_browser": "missing proof until new real-BFF/PG browser case passes"
    },
    "fix_status": "Sole writer released after E50/E51 actual terminal postseals; product fixes in progress, no after/GREEN claim."
  },
  "after_fix": {
    "checkpoint": "E54",
    "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
    "evidence": [
      "all-result-e54-v1.1.json",
      "all-source-recheck-e54-v1.1.json",
      "browser-freshness-collection-e54-v1.1.json"
    ],
    "actual_safe_payload": {
      "state": "PREPARED",
      "recoveryAction": "RECONCILE"
    },
    "coverage_chain": "Real reserveInitial 90s reservation -> observational scoped GET RECONCILE -> served React local action -> live202 no release -> synthetic DB expiry -> REJECTED/release; zero provider calls and Message in both phases. Browser fixture invokes actual compiled reservation service, not sent-intent state rewrite.",
    "coverage_status": "All formerly missing BFF and React/browser stages now covered; independent review remains.",
    "root_cause": "Safe DTO omitted the existing local reconciliation action for durable PREPARED state; UI correctly rendered only declared actions.",
    "rule_decision": "no-rule-needed: finite product state/action semantics; companion behavior regression, no Delphi/analyzer change."
  }
}

```

### all-result-e45-v1.1.json

```json
{
  "checkpoint": "E45 canonical all terminal GREEN, not delivery",
  "recorded_at_utc": "2026-10-22T22:50:14.887276+00:00",
  "command": "bash scripts/test-channels-local.sh all",
  "executor_session_id": 57348,
  "actual_exit_code": 0,
  "phases": {
    "generate_migrate_deploy_status_lint_api_build": "passed",
    "api_unit": {
      "files": 34,
      "passed": 356
    },
    "postgresql_integration": {
      "files": 33,
      "passed": 435
    },
    "web_typescript_vite_build": "passed",
    "web_unit": {
      "files": 7,
      "passed": 53
    },
    "browser": {
      "passed": 85,
      "failed": 0,
      "duration": "14.5m"
    }
  },
  "stdout_sha256": "76923c5f6b39ecb4deec0c296c7d5360b8a8ebc0620e1f43908e43df97600233",
  "source_recheck": "all-source-recheck-e45-v1.1.json",
  "freshness": "browser-freshness-collection-e45-v1.1.json",
  "owned_cleanup_observed": true,
  "specific_proofs": [
    "E44 causal snapshot-read failure now passes: persistent read fault preserves original key/body and blocks sends, failed local reread adds no POST, explicit successful reread enables only original-key replay;2BFFPOSTs total/1provider effect/1Message.",
    "Status-specific recovery selector passes original immutable-key/preAdmission provenance test.",
    "Shared catalog real refresh/POSITIONAL browser dispatch, escaped/read-only preview, keyboard,5x20 frontend triggers all pass.",
    "New renderer4096/4097 final snapshot,1024/1025 Unicode per-value and20/21 distinct-param boundaries pass.",
    "Actual PG commit-with-lost-ACK vs rollback at reserve/claim/receipt/releases/local acceptance; unique echo/CAS and risk deadlines pass.",
    "Current API/public/BOT/window/timeline/template/onboarding regression suites pass; protected test bytes unchanged."
  ],
  "metrics": {
    "initial_same_key_waves": [
      {
        "wave": 1,
        "requests": 20,
        "replay202": 19,
        "posts": 1,
        "messages": 1,
        "elapsedMs": 191
      },
      {
        "wave": 2,
        "requests": 20,
        "replay202": 19,
        "posts": 1,
        "messages": 1,
        "elapsedMs": 153
      },
      {
        "wave": 3,
        "requests": 20,
        "replay202": 19,
        "posts": 1,
        "messages": 1,
        "elapsedMs": 136
      },
      {
        "wave": 4,
        "requests": 20,
        "replay202": 19,
        "posts": 1,
        "messages": 1,
        "elapsedMs": 132
      },
      {
        "wave": 5,
        "requests": 20,
        "replay202": 19,
        "posts": 1,
        "messages": 1,
        "elapsedMs": 138
      }
    ],
    "inbox_order": {
      "rowCount": 50,
      "plan": "Limit  (cost=0.41..9.23 rows=50 width=45) (actual time=0.015..0.030 rows=50 loops=1)\n  Buffers: shared hit=6\n  ->  Index Scan using conversations_inbox_order_idx on conversations  (cost=0.41..2645.78 rows=15000 width=45) (actual time=0.014..0.026 rows=50 loops=1)\n        Index Cond: ((bu_id = '2d5ef223-1ad0-4812-b634-24014bce4b6f'::text) AND (contact_type = 'PESSOA'::\"ContactType\"))\n        Filter: (status = 'QUEUED'::\"ConversationStatus\")\n        Buffers: shared hit=6\nPlanning:\n  Buffers: shared hit=71\nPlanning Time: 0.207 ms\nExecution Time: 0.043 ms"
    },
    "inbox_out_heavy": {
      "rows": 60,
      "listed": 50,
      "conversationQueries": 3,
      "messageQueries": 0
    },
    "public_trusted_window": {
      "policy_schema_version": "pcv-1",
      "lane_id": "EPS",
      "trigger_result": "required",
      "trigger_severity": "medium",
      "trigger_reason_code": "EPS-DATA-PATH-CHANGED",
      "gate_deadline": "before_local_implemented",
      "min_evidence_rule_id": "EPS-E2",
      "acceptance_rule_id": "EPS-A2",
      "sample_profile": "EPS-SP-STRONG",
      "access_pattern_classification": "Public conversation page loads selected BU channels once, official credential metadata once, one bounded latest-any-message projection for returned page IDs, and one batched indexed selected-resource trusted Meta IN timestamp query when selected bindings require a window; no provider credentials are decrypted or probed.",
      "pageConversations": 30,
      "historyRowsPerConversation": 24,
      "availabilitySample": [
        {
          "available": true,
          "reason": null,
          "windowOpen": true
        },
        {
          "available": true,
          "reason": null,
          "windowOpen": true
        },
        {
          "available": true,
          "reason": null,
          "windowOpen": true
        }
      ],
      "queryCounts": {
        "buChannelFindMany": 1,
        "channelCredentialFindMany": 1,
        "latestAnyMessageProjection": 1,
        "latestInboundWindowProjection": 1
      },
      "elapsedMs": 14.70497800000021,
      "explainLatestInboundProjection": [
        {
          "Plan": {
            "Node Type": "Nested Loop",
            "Parallel Aware": false,
            "Async Capable": false,
            "Join Type": "Inner",
            "Startup Cost": 0.28,
            "Total Cost": 96.31,
            "Plan Rows": 30,
            "Plan Width": 40,
            "Actual Startup Time": 0.024,
            "Actual Total Time": 0.19,
            "Actual Rows": 30,
            "Actual Loops": 1,
            "Inner Unique": false,
            "Shared Hit Blocks": 90,
            "Shared Read Blocks": 0,
            "Shared Dirtied Blocks": 0,
            "Shared Written Blocks": 0,
            "Local Hit Blocks": 0,
            "Local Read Blocks": 0,
            "Local Dirtied Blocks": 0,
            "Local Written Blocks": 0,
            "Temp Read Blocks": 0,
            "Temp Written Blocks": 0,
            "Plans": [
              {
                "Node Type": "Function Scan",
                "Parent Relationship": "Outer",
                "Parallel Aware": false,
                "Async Capable": false,
                "Function Name": "unnest",
                "Alias": "requested",
                "Startup Cost": 0,
                "Total Cost": 0.3,
                "Plan Rows": 30,
                "Plan Width": 32,
                "Actual Startup Time": 0.004,
                "Actual Total Time": 0.005,
                "Actual Rows": 30,
                "Actual Loops": 1,
                "Shared Hit Blocks": 0,
                "Shared Read Blocks": 0,
                "Shared Dirtied Blocks": 0,
                "Shared Written Blocks": 0,
                "Local Hit Blocks": 0,
                "Local Read Blocks": 0,
                "Local Dirtied Blocks": 0,
                "Local Written Blocks": 0,
                "Temp Read Blocks": 0,
                "Temp Written Blocks": 0
              },
              {
                "Node Type": "Limit",
                "Parent Relationship": "Inner",
                "Parallel Aware": false,
                "Async Capable": false,
                "Startup Cost": 0.28,
                "Total Cost": 3.18,
                "Plan Rows": 1,
                "Plan Width": 45,
                "Actual Startup Time": 0.006,
                "Actual Total Time": 0.006,
                "Actual Rows": 1,
                "Actual Loops": 30,
                "Shared Hit Blocks": 90,
                "Shared Read Blocks": 0,
                "Shared Dirtied Blocks": 0,
                "Shared Written Blocks": 0,
                "Local Hit Blocks": 0,
                "Local Read Blocks": 0,
                "Local Dirtied Blocks": 0,
                "Local Written Blocks": 0,
                "Temp Read Blocks": 0,
                "Temp Written Blocks": 0,
                "Plans": [
                  {
                    "Node Type": "Index Only Scan",
                    "Parent Relationship": "Outer",
                    "Parallel Aware": false,
                    "Async Capable": false,
                    "Scan Direction": "Backward",
                    "Index Name": "messages_conversation_trusted_window_idx",
                    "Relation Name": "messages",
                    "Alias": "message",
                    "Startup Cost": 0.28,
                    "Total Cost": 72.85,
                    "Plan Rows": 25,
                    "Plan Width": 45,
                    "Actual Startup Time": 0.006,
                    "Actual Total Time": 0.006,
                    "Actual Rows": 1,
                    "Actual Loops": 30,
                    "Index Cond": "((conversation_id = requested.conversation_id) AND (provider_resource_identity_id = '399453c9-f007-4ae2-b81c-14a4e8a9fa2c'::text) AND (direction = 'IN'::\"MessageDirection\") AND (channel_origin = 'OFICIAL'::\"ChannelType\") AND (official_inbound_at IS NOT NULL) AND (official_inbound_at <= CURRENT_TIMESTAMP))",
                    "Rows Removed by Index Recheck": 0,
                    "Heap Fetches": 30,
                    "Shared Hit Blocks": 90,
                    "Shared Read Blocks": 0,
                    "Shared Dirtied Blocks": 0,
                    "Shared Written Blocks": 0,
                    "Local Hit Blocks": 0,
                    "Local Read Blocks": 0,
                    "Local Dirtied Blocks": 0,
                    "Local Written Blocks": 0,
                    "Temp Read Blocks": 0,
                    "Temp Written Blocks": 0
                  }
                ]
              }
            ]
          },
          "Planning": {
            "Shared Hit Blocks": 68,
            "Shared Read Blocks": 0,
            "Shared Dirtied Blocks": 0,
            "Shared Written Blocks": 0,
            "Local Hit Blocks": 0,
            "Local Read Blocks": 0,
            "Local Dirtied Blocks": 0,
            "Local Written Blocks": 0,
            "Temp Read Blocks": 0,
            "Temp Written Blocks": 0
          },
          "Planning Time": 0.216,
          "Triggers": [],
          "Execution Time": 0.203
        }
      ],
      "providerCallsBefore": {
        "meta": 0,
        "evolution": 0
      },
      "providerCallsAfter": {
        "meta": 0,
        "evolution": 0
      },
      "limits": "Disposable PostgreSQL and one bounded 30-conversation public page; local query count/plan observation, not a capacity or latency SLO claim."
    }
  },
  "metric_interpretation": {
    "initial_same_key_waves": "Each20-request wave includes1held original and19concurrent replays. posts counts Evolution fake-port invocations, not external TCP. Actual Message/intent counts asserted independently.",
    "inbox_order": "Fixture creates15000 conversations; logged rowCount50 is returned page size, not fixture cardinality. SQL-only expression index observed, no external sort.",
    "inbox_out_heavy": "3queries touching conversations, not3totalSQL;0standalone Message hydration queries.",
    "public_trusted_window": "One channel binding/credential metadata/latest-any projection/batched trusted-IN projection for30rows; no external credential probe.",
    "runtime": "Disposable synthetic stage only; no production capacity/SLO or actual Meta delivery claim."
  },
  "remaining": [
    "OrdinaryRecovery new consumer has no direct browser reconcile/ack proof yet; one already-admitted test-only real90s-deadline case queued after this postseal. No product bug inferred.",
    "Required independent architecture/security/PCV/TQA/cutover/final/debt and complete item-specific evidence disposition remain.",
    "Full canonical diff guard/private-boundary exception and preserved local activation plan are unapproved/unexecuted.",
    "Own-account approved template human attestation does not establish source-bound first-send/reply; assisted nonofficial/official operator proof still required."
  ],
  "delivery": "InProgress/Pending/implementation, no completed checkbox or runtime promotion"
}

```

### all-source-recheck-e45-v1.1.json

```json
{
  "checkpoint": "E45 terminal full positive source recheck",
  "stage": "After actual executor terminal and owned cleanup; BEFORE writer release",
  "count": 259,
  "fingerprint": "27e37bc4ac9398e64b3035aa785135d8c639c8dd1beefe53db1c16a39e0bd87f",
  "matches_preseal_full_inventory_and_bytes": true,
  "record_reference": "all-source-seal-e45-v1.1.json#records",
  "stdout_sha256": "76923c5f6b39ecb4deec0c296c7d5360b8a8ebc0620e1f43908e43df97600233",
  "executor_reported_exit_code": 0,
  "recorded_at_utc": "2026-10-22T22:49:30.695194+00:00",
  "boundary": "Only declared positive public roots and7 exact publicfiles; no actual env/data/process inspection."
}

```

### browser-freshness-collection-e45-v1.1.json

```json
{
  "kind": "Independent owned browser attestation collection",
  "checkpoint": "E45",
  "source_seal": "all-source-seal-e45-v1.1.json",
  "attestation_sha256": "f82a301326ac1b512a51f5ae1a2feeadb989ab5700b87f8194dea236b39636cf",
  "run_id": "2026-10-22T22-33-52-337Z",
  "captured_at_utc": "2026-10-22T22:33:52.337Z",
  "runtime": "v22.23.3",
  "completed_migrations": 28,
  "current_api_head": "db5a86758a165fac8a1ab587599c37b17890530c",
  "current_web_head": "74b9d4b714044829796f875d00553f077c1c329d",
  "served_dist_bundle_equal": true,
  "served_bundle_sha256": "ca94c89f5bce634bb6c22c019fcb83420a8287e302a07a80a59e392c4176800f",
  "manifest_count": 93,
  "all_manifest_records_match_presealed_sources": true,
  "manifest_checks": [
    {
      "path": "api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/schema.prisma",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/transport/channel.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/historico/catalogo.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/historico/cobertura.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/channel-window-policy.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/channel-window-policy.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/conversation-start.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/conversation-start.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/conversations.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/dispatch-admission.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/incoming.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/incoming.typebot.integration.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message-template-renderer.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/message-acceptance.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/message-acceptance.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-definition.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-definition.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-draft.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.dependencies.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.ports.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.ports.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-observation.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-submission.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-transaction-boundary.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/account-reference.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-factory.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-registry.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/channel-transport.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/evolution-channel.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/meta-channel.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/prisma-channel-resolver.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/message-templates/template-management.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/message-templates/template-management.resolver.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/initial-message.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/initial-message.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/message-template.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/message-template.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/bff/bff.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/bff/conversations.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/bff/message-templates.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/public/conversations.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/public/public.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/webhooks/meta.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/webhooks/webhooks.module.ts",
      "matches": true
    },
    {
      "path": "api-app/test/api-publica.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/atendimento.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/browser-server.cjs",
      "matches": true
    },
    {
      "path": "api-app/test/channel-transport.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/conversation-start.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/dispatch-admission.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/helpers.ts",
      "matches": true
    },
    {
      "path": "api-app/test/initial-message.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/message-template-bff.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/message-template-drafts.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/message-template-management.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/number-onboarding-bci.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/number-onboarding-pcv.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/number-onboarding-typebot.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/timeline-fixtures.cjs",
      "matches": true
    },
    {
      "path": "api-app/test/webhooks.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/channel-transport.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/message-templates.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/number-onboarding-freshness.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/start-conversation.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/timeline-freshness.ts",
      "matches": true
    },
    {
      "path": "web-app/src/api.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/src/api.ts",
      "matches": true
    },
    {
      "path": "web-app/src/App.tsx",
      "matches": true
    },
    {
      "path": "web-app/src/componentes/NovaConversa.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/src/componentes/NovaConversa.tsx",
      "matches": true
    },
    {
      "path": "web-app/src/telas/Inbox.tsx",
      "matches": true
    },
    {
      "path": "web-app/src/telas/Modelos.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/src/telas/Modelos.tsx",
      "matches": true
    }
  ],
  "limits": "Disposable synthetic proof only; historical declaredBaseline fields do not replace current approved repository baselines. No actual preserved runtime/provider activation proof."
}

```

### verification-debt-preclosure-e46-v1.1.json

```json
{
  "kind": "Pre-closure verification-debt audit, complete positive public roots",
  "recorded_at_utc": "2026-10-22T22:57:26.296530+00:00",
  "command": [
    "bash",
    "delphi-ai/tools/verification_debt_audit.sh",
    "--todo",
    "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
    "--path",
    "api-app/src",
    "--path",
    "api-app/test",
    "--path",
    "api-app/prisma",
    "--path",
    "web-app/src",
    "--path",
    "web-app/e2e"
  ],
  "actual_exit_code": 2,
  "stdout_sha256": "c565d5609b509e0c37371c9b3851c353a3b58bcba81280e5560ad6f5dfb7d4d4",
  "raw_public_output": "verification-debt-output-e46-v1.1.txt",
  "summary_lines": [
    "Inline code TODO debt classification: none",
    "Unchecked checklist items:",
    "Counts: waiver=42 blocker=58 unchecked=45 accepted_inline=0 canonical_link_missing=0 cleanup_required=0"
  ],
  "boundary": "No --scan-git-modified, no actual env/private paths. Exact TODO plus five public source roots.",
  "stage": "Pending implementation assurance; unchecked delivery criteria and later runtime/guard approval are explicit gates, not hidden debt or evidence of completion.",
  "retained_prior_debt": [
    "SEC-R6-04",
    "OPS-R4-01",
    "TQA-ST05-03"
  ],
  "final_disposition": "Not final clean closure; classify reported evidence/inline findings before delivery.",
  "outcome": "high",
  "inline_code_todo_debt_classification": "none",
  "classification": [
    {
      "signals": "42waiver/58blocker/45unchecked, raw heuristic counts",
      "meaning": "Planning/history language, explicit n/a and currently open delivery gates match broad regex; counts do not imply42 granted waivers. No closure was claimed.",
      "disposition": "Preserve current pending gates; re-audit at actual final closeout."
    },
    {
      "signals": "Inline markers in five complete public roots",
      "meaning": "No TODO/FIXME/HACK/TBD/XXX marker requiring inline cleanup.",
      "disposition": "none"
    },
    {
      "signals": "Stable architecture decisions not yet promoted to module docs",
      "meaning": "Approved module consolidation gate follows implementation/assurance and has not run.",
      "disposition": "Concrete module mapping/consolidation remains required before completion."
    }
  ]
}

```

### positive-build-contexts-e53-v1.1.json

```json
{
  "kind": "Current corrected public-only deterministic build archives",
  "recorded_at_utc": "2026-10-23T00:18:20.760248+00:00",
  "source_seal": "all-source-seal-e53-v1.1.json",
  "source_fingerprint": "3d1d7e83d7425b7c9f82258768d00e4cb5d066ab54d645ddf7b0b6fa275d17ec",
  "builds": [
    {
      "service": "api",
      "generated_archive": "/tmp/stcon04-build-context-api-e53.tar",
      "archive_sha256": "3a4716b1870223d79ae9853d0790c00b4aefbaa248c53c5dfcc8032b5def7aec",
      "record_count": 177,
      "records": [
        {
          "path": "api-app/Dockerfile",
          "archive_path": "Dockerfile",
          "sha256": "188a83953c950d65f3fd5b3d428382cafc88e42efa0776c95fb4ba49b54d0a15",
          "bytes": 2504
        },
        {
          "path": "api-app/docker/entrypoint.sh",
          "archive_path": "docker/entrypoint.sh",
          "sha256": "3f6168bba444074ff220d09ef4127593cf5af6744462ef344695cd749aeac095",
          "bytes": 687
        },
        {
          "path": "api-app/nest-cli.json",
          "archive_path": "nest-cli.json",
          "sha256": "4f3595ef15ab569316b8bc91f8bfa33adccb3f3b1a082a39851c4bfc8ad60651",
          "bytes": 223
        },
        {
          "path": "api-app/package-lock.json",
          "archive_path": "package-lock.json",
          "sha256": "d1e45274c4b10d134469d7ec63e88777ec26b917d48197a03a4b97cefda047c7",
          "bytes": 305491
        },
        {
          "path": "api-app/package.json",
          "archive_path": "package.json",
          "sha256": "df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d",
          "bytes": 1670
        },
        {
          "path": "api-app/prisma/migrations/20260818125556_nucleo_v1_tenancy_identidade_atendimento/migration.sql",
          "archive_path": "prisma/migrations/20260818125556_nucleo_v1_tenancy_identidade_atendimento/migration.sql",
          "sha256": "680ff78cf5c8dab2bc5ec51688b83252bb86d214e8af7817356ee125ed47daa4",
          "bytes": 9362
        },
        {
          "path": "api-app/prisma/migrations/20260821175101_modulos_e_marca_por_mantenedora/migration.sql",
          "archive_path": "prisma/migrations/20260821175101_modulos_e_marca_por_mantenedora/migration.sql",
          "sha256": "fe2155893de7a9ade15493617e36e77e299bcffc9b86ec19ad813a15bfd1c6bc",
          "bytes": 234
        },
        {
          "path": "api-app/prisma/migrations/20260821180000_tres_papeis_owner_admin_atendente/migration.sql",
          "archive_path": "prisma/migrations/20260821180000_tres_papeis_owner_admin_atendente/migration.sql",
          "sha256": "ecf379d151e2f73ff1b81baef00c27561b2b9f1acc885599144603541987b7f7",
          "bytes": 928
        },
        {
          "path": "api-app/prisma/migrations/20260821190000_setor_e_proveniencia_do_grant/migration.sql",
          "archive_path": "prisma/migrations/20260821190000_setor_e_proveniencia_do_grant/migration.sql",
          "sha256": "968394573271ce426d3011db774ce9a219750dc5822f251fdea291e588d12d59",
          "bytes": 2354
        },
        {
          "path": "api-app/prisma/migrations/20260821190500_concessao_de_setor_e_fato_proprio/migration.sql",
          "archive_path": "prisma/migrations/20260821190500_concessao_de_setor_e_fato_proprio/migration.sql",
          "sha256": "176c7664c7c1458f0e06beb33f21359db72511e6cd20f1da5fb63b7eec50cdbf",
          "bytes": 858
        },
        {
          "path": "api-app/prisma/migrations/20260821200000_historico_de_atividades/migration.sql",
          "archive_path": "prisma/migrations/20260821200000_historico_de_atividades/migration.sql",
          "sha256": "3a87e44c2cc8a3a7f91fc59819bae065e9a1f1eeacfc28685710e8d5d7e18a75",
          "bytes": 2069
        },
        {
          "path": "api-app/prisma/migrations/20260821210000_wizard_de_onboarding/migration.sql",
          "archive_path": "prisma/migrations/20260821210000_wizard_de_onboarding/migration.sql",
          "sha256": "013d4428d36afe752966762ae8a2d6195032d88c57ab9d18b2c147df21865735",
          "bytes": 894
        },
        {
          "path": "api-app/prisma/migrations/20260821220000_preserva_modulo_ja_em_uso/migration.sql",
          "archive_path": "prisma/migrations/20260821220000_preserva_modulo_ja_em_uso/migration.sql",
          "sha256": "a33a51234e7097f95e10452c3652b33e9e5c5c1b488a4545404222711d5abec5",
          "bytes": 1086
        },
        {
          "path": "api-app/prisma/migrations/20260824122559_perfil_do_proprio_usuario/migration.sql",
          "archive_path": "prisma/migrations/20260824122559_perfil_do_proprio_usuario/migration.sql",
          "sha256": "5f14615eef62afaa05be2f6e1a144667c30e4c2f618f899ade8c108c7ae9a80e",
          "bytes": 69
        },
        {
          "path": "api-app/prisma/migrations/20260824125224_arquivos_logo_e_avatar/migration.sql",
          "archive_path": "prisma/migrations/20260824125224_arquivos_logo_e_avatar/migration.sql",
          "sha256": "4a8bb54855ff5de7c89632df84f92c5589ffd99cd9e8c5001a080d01f7c121d1",
          "bytes": 162
        },
        {
          "path": "api-app/prisma/migrations/20260824125227_arquivos_dono/migration.sql",
          "archive_path": "prisma/migrations/20260824125227_arquivos_dono/migration.sql",
          "sha256": "864ced863cd894f7df333f16a6eaafe0870d72f263c18600b7cf4985e5c8120a",
          "bytes": 572
        },
        {
          "path": "api-app/prisma/migrations/20260824125334_avatar_e_do_usuario_nao_da_bu/migration.sql",
          "archive_path": "prisma/migrations/20260824125334_avatar_e_do_usuario_nao_da_bu/migration.sql",
          "sha256": "297f051ce252e4e6abc6b7dde2ded19a126c5db074e74c29b937ef7787f0cfa8",
          "bytes": 283
        },
        {
          "path": "api-app/prisma/migrations/20260824161138_convite_e_recuperacao_de_senha/migration.sql",
          "archive_path": "prisma/migrations/20260824161138_convite_e_recuperacao_de_senha/migration.sql",
          "sha256": "a46e62f79cd2e0f4d818bada129caf89f800fc372d963da4bbac6b9e597229c3",
          "bytes": 934
        },
        {
          "path": "api-app/prisma/migrations/20260827170000_cor_secundaria/migration.sql",
          "archive_path": "prisma/migrations/20260827170000_cor_secundaria/migration.sql",
          "sha256": "01d41f5e3772b4278b41511b2a7efbb39bd76a62e31f67b2a4967de4e6357380",
          "bytes": 76
        },
        {
          "path": "api-app/prisma/migrations/20260831130000_cores_primarias_por_tema/migration.sql",
          "archive_path": "prisma/migrations/20260831130000_cores_primarias_por_tema/migration.sql",
          "sha256": "03cecfbf50ed896fed322d63dbb1fea40126685b9193d08e677a4e598c5b4e30",
          "bytes": 265
        },
        {
          "path": "api-app/prisma/migrations/20260901120000_typebot_bots_and_triggers/migration.sql",
          "archive_path": "prisma/migrations/20260901120000_typebot_bots_and_triggers/migration.sql",
          "sha256": "62188240b4f2f7db65a3f2e8d45cf866b5c22311225782a669bf6389d517a8a9",
          "bytes": 1736
        },
        {
          "path": "api-app/prisma/migrations/20260901130000_typebot_sessions/migration.sql",
          "archive_path": "prisma/migrations/20260901130000_typebot_sessions/migration.sql",
          "sha256": "47fa9f58f4b89cf038eda3cf54cd576d3ab4cd3b2e54be1f7474c94a2f43f795",
          "bytes": 847
        },
        {
          "path": "api-app/prisma/migrations/20261015120000_number_onboarding_foundation/migration.sql",
          "archive_path": "prisma/migrations/20261015120000_number_onboarding_foundation/migration.sql",
          "sha256": "55d84f5eef1b9b9e9a22891695812e522fe4e405041341218984507426ef0946",
          "bytes": 6681
        },
        {
          "path": "api-app/prisma/migrations/20261015130000_number_onboarding_provider_resource_ownership_immutable/migration.sql",
          "archive_path": "prisma/migrations/20261015130000_number_onboarding_provider_resource_ownership_immutable/migration.sql",
          "sha256": "a6fa9ad9e99a0b55ed5d9e86b99d42b603b404c13f41f97ac718e6443f29a3fe",
          "bytes": 880
        },
        {
          "path": "api-app/prisma/migrations/20261015140000_number_onboarding_channel_operation_fence/migration.sql",
          "archive_path": "prisma/migrations/20261015140000_number_onboarding_channel_operation_fence/migration.sql",
          "sha256": "e484edd01e78133bcaf23f12fb47e44e92cba44a89b29803eff1530b103bc496",
          "bytes": 270
        },
        {
          "path": "api-app/prisma/migrations/20261015150000_number_onboarding_managed_cleanup/migration.sql",
          "archive_path": "prisma/migrations/20261015150000_number_onboarding_managed_cleanup/migration.sql",
          "sha256": "27a07435e3327f004ad8d46cd4c18eec57b89ce3cdbf51c39631b248555214ad",
          "bytes": 837
        },
        {
          "path": "api-app/prisma/migrations/20261016160000_number_onboarding_current_channel_identity_index/migration.sql",
          "archive_path": "prisma/migrations/20261016160000_number_onboarding_current_channel_identity_index/migration.sql",
          "sha256": "aadefab2ce66f3484661e66fdf918f5e295926bf9b89b0af4c3e2c8c5c78b740",
          "bytes": 126
        },
        {
          "path": "api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql",
          "archive_path": "prisma/migrations/20261020170000_message_inbound_window_index/migration.sql",
          "sha256": "586e709e07736eca0908ab5dcc668cf0e0b317189b4c963b361399848a3c9710",
          "bytes": 212
        },
        {
          "path": "api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql",
          "archive_path": "prisma/migrations/20261021130000_message_template_drafts/migration.sql",
          "sha256": "3feab40fed1c9be1bac9e43464fd587d57693424c4b3012d8c4b8536661d51dd",
          "bytes": 4453
        },
        {
          "path": "api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql",
          "archive_path": "prisma/migrations/20261021150000_message_template_operations/migration.sql",
          "sha256": "2822bff860b5aa3476e7614f6a5d5515520dfd8e40708767d1bc4c5bfe2d991d",
          "bytes": 12940
        },
        {
          "path": "api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql",
          "archive_path": "prisma/migrations/20261022140000_initial_message_orchestration/migration.sql",
          "sha256": "a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437",
          "bytes": 343
        },
        {
          "path": "api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql",
          "archive_path": "prisma/migrations/20261022150000_initial_message_admissions/migration.sql",
          "sha256": "78963dce996b2cec9e0990812a5091725238f9995e892c196e614ce9b2a6464f",
          "bytes": 3535
        },
        {
          "path": "api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql",
          "archive_path": "prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql",
          "sha256": "60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544",
          "bytes": 398
        },
        {
          "path": "api-app/prisma/migrations/migration_lock.toml",
          "archive_path": "prisma/migrations/migration_lock.toml",
          "sha256": "bc487c02c71ad9cae8694647129e3ea7f32b1fe7007d0a6ced064e51022cd3fb",
          "bytes": 131
        },
        {
          "path": "api-app/prisma/schema.prisma",
          "archive_path": "prisma/schema.prisma",
          "sha256": "d2c94a0b0908d268f498ed0e288924343abeb1bb206d71f8291063caec50fbed",
          "bytes": 42200
        },
        {
          "path": "api-app/src/app.module.ts",
          "archive_path": "src/app.module.ts",
          "sha256": "a59880adc1bd8250fdbf5d52637fc38fe3177a2615e1b25389716946da7ad420",
          "bytes": 1857
        },
        {
          "path": "api-app/src/domain/access/access.service.ts",
          "archive_path": "src/domain/access/access.service.ts",
          "sha256": "2ef3761a138d7c8c386c5ddb4bf2a2000c960328789834bde5e12135a1ea66e7",
          "bytes": 2390
        },
        {
          "path": "api-app/src/domain/access/require-role.ts",
          "archive_path": "src/domain/access/require-role.ts",
          "sha256": "1281da1ad31748e2bd78bffdf2962376d3413c7b37cfe6102448710cc7d7ce61",
          "bytes": 1142
        },
        {
          "path": "api-app/src/domain/access/role.spec.ts",
          "archive_path": "src/domain/access/role.spec.ts",
          "sha256": "7d5400e3af84896ba021aa220908ad7ac995f2f0af1405cf53c72f5ef7a6a8d8",
          "bytes": 1996
        },
        {
          "path": "api-app/src/domain/access/role.ts",
          "archive_path": "src/domain/access/role.ts",
          "sha256": "ec92764e75c52b754e430355d196137ca90de89b4c5ed6f3fb49a05da10e1b42",
          "bytes": 1776
        },
        {
          "path": "api-app/src/domain/access/scope.spec.ts",
          "archive_path": "src/domain/access/scope.spec.ts",
          "sha256": "e3386d1e27d27c38ebbf8f3c06222c50c0cd5d164c29437ec83fcafbf14919c3",
          "bytes": 7356
        },
        {
          "path": "api-app/src/domain/access/scope.ts",
          "archive_path": "src/domain/access/scope.ts",
          "sha256": "412f68eb157328855c87cb86b6b89cc1c267eee7068dc59c0abbe085074db26d",
          "bytes": 5701
        },
        {
          "path": "api-app/src/domain/acesso/convites.service.ts",
          "archive_path": "src/domain/acesso/convites.service.ts",
          "sha256": "089931bcf9acd7b3807364e9b7eefbbbcfa14c41e649a3f87e74ca81cb83d211",
          "bytes": 5266
        },
        {
          "path": "api-app/src/domain/acesso/limite-de-recuperacao.service.ts",
          "archive_path": "src/domain/acesso/limite-de-recuperacao.service.ts",
          "sha256": "9661ebd71ab182f177743295bd15d1e857970025587c7a8c8566c9c43532ae16",
          "bytes": 1242
        },
        {
          "path": "api-app/src/domain/acesso/tokens.service.ts",
          "archive_path": "src/domain/acesso/tokens.service.ts",
          "sha256": "00f5f240ba10ad2a0178e4c583ac4e6f04fb07b8a3fc7e55c58ab5ce6702c180",
          "bytes": 4032
        },
        {
          "path": "api-app/src/domain/channels/channel-credential-crypto.spec.ts",
          "archive_path": "src/domain/channels/channel-credential-crypto.spec.ts",
          "sha256": "eda02a1bf69f40eb07309184adad8d2f1862f563c33afa03fb1657991d29faf1",
          "bytes": 3766
        },
        {
          "path": "api-app/src/domain/channels/channel-credential-crypto.ts",
          "archive_path": "src/domain/channels/channel-credential-crypto.ts",
          "sha256": "4a438a1e73903c011d212962f41b38dfb2a999c539112b6831156664de6d9ef4",
          "bytes": 3649
        },
        {
          "path": "api-app/src/domain/channels/channel-credential-resolver.spec.ts",
          "archive_path": "src/domain/channels/channel-credential-resolver.spec.ts",
          "sha256": "a60d142fcc335de43c5a697d9f7758f722883a1725c824dd0a4b4f0a2f7fb03b",
          "bytes": 4021
        },
        {
          "path": "api-app/src/domain/channels/channel-credential-resolver.ts",
          "archive_path": "src/domain/channels/channel-credential-resolver.ts",
          "sha256": "7782792bb945701cc6f6d0ac1460d0504356fa8d73a4261f37112f7c892a23ac",
          "bytes": 6500
        },
        {
          "path": "api-app/src/domain/channels/channels.service.ts",
          "archive_path": "src/domain/channels/channels.service.ts",
          "sha256": "e910b2b395abc0ebca74deea917cf107dd36eca58491f1b0893efb702e1dfcf5",
          "bytes": 36719
        },
        {
          "path": "api-app/src/domain/channels/number-registration.service.ts",
          "archive_path": "src/domain/channels/number-registration.service.ts",
          "sha256": "be53f7f1feb00c0bacb36ce0cf5d60915bb398ed011f69d28d3d4987f83417dc",
          "bytes": 45315
        },
        {
          "path": "api-app/src/domain/channels/receipt-attempt-convergence.ts",
          "archive_path": "src/domain/channels/receipt-attempt-convergence.ts",
          "sha256": "ca8cb841fab2574866c3508ab41aa0a269608a20658db18840b2b89f0c281512",
          "bytes": 920
        },
        {
          "path": "api-app/src/domain/channels/safe-redaction.spec.ts",
          "archive_path": "src/domain/channels/safe-redaction.spec.ts",
          "sha256": "b35f2c689ee22cf0f8ebe50b4979ca7e25a708e0bd6930c93c376fbf57a3ff6a",
          "bytes": 971
        },
        {
          "path": "api-app/src/domain/channels/safe-redaction.ts",
          "archive_path": "src/domain/channels/safe-redaction.ts",
          "sha256": "704539c0a9aabd17dd5fc19826f5079da816c2bc5e22d438b8672662b9998606",
          "bytes": 2705
        },
        {
          "path": "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
          "archive_path": "src/domain/channels/transport/channel-dependencies.spec.ts",
          "sha256": "f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3",
          "bytes": 2383
        },
        {
          "path": "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
          "archive_path": "src/domain/channels/transport/channel-initial-message.spec.ts",
          "sha256": "46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa",
          "bytes": 22801
        },
        {
          "path": "api-app/src/domain/channels/transport/channel.ts",
          "archive_path": "src/domain/channels/transport/channel.ts",
          "sha256": "49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9",
          "bytes": 6698
        },
        {
          "path": "api-app/src/domain/historico/atividades.service.ts",
          "archive_path": "src/domain/historico/atividades.service.ts",
          "sha256": "9a081318375268d76839a83502d194bb12bfc1fb619a3cb6badab80c425d4609",
          "bytes": 2752
        },
        {
          "path": "api-app/src/domain/historico/catalogo.ts",
          "archive_path": "src/domain/historico/catalogo.ts",
          "sha256": "7cc5d9b1a76019b99161334ca05cb899be961c73192cf0d47437763b1837823f",
          "bytes": 7992
        },
        {
          "path": "api-app/src/domain/historico/cobertura.ts",
          "archive_path": "src/domain/historico/cobertura.ts",
          "sha256": "8f8208f0a22a9ea78d5d244e1a4eafd78ff04138e1c0ff25b8c66856f0db64e5",
          "bytes": 8812
        },
        {
          "path": "api-app/src/domain/historico/registro.service.ts",
          "archive_path": "src/domain/historico/registro.service.ts",
          "sha256": "3826c4b841af898c4824fc53b64249f17f929157ac60769fb72336574d5d9c32",
          "bytes": 2691
        },
        {
          "path": "api-app/src/domain/identity/identity.service.ts",
          "archive_path": "src/domain/identity/identity.service.ts",
          "sha256": "e839d6be1e2f1a5e1db681e742c31f5de0efb3a224cb1013ae81a21e8caf8e3a",
          "bytes": 4159
        },
        {
          "path": "api-app/src/domain/identity/login-attempt.service.ts",
          "archive_path": "src/domain/identity/login-attempt.service.ts",
          "sha256": "979b1c873319d3d8142e4aeb13c71f502c332c7dda862c0ae758948e763d34fa",
          "bytes": 1912
        },
        {
          "path": "api-app/src/domain/identity/password.service.spec.ts",
          "archive_path": "src/domain/identity/password.service.spec.ts",
          "sha256": "3ec4ae1217e76e8191fb713f762c2041e588e1e88bbfb2dd0ef913a9a58289f1",
          "bytes": 1809
        },
        {
          "path": "api-app/src/domain/identity/password.service.ts",
          "archive_path": "src/domain/identity/password.service.ts",
          "sha256": "6aecadaf5295c909d8f399b38d78c72b5aed90b72a0aea68fe39a648bf371d0e",
          "bytes": 1985
        },
        {
          "path": "api-app/src/domain/identity/usuarios.service.ts",
          "archive_path": "src/domain/identity/usuarios.service.ts",
          "sha256": "ff82f54a7aa6e495c5ce20626e88221fc20f4474a5ec84ff2f257b081f803364",
          "bytes": 9791
        },
        {
          "path": "api-app/src/domain/inbox/channel-window-policy.spec.ts",
          "archive_path": "src/domain/inbox/channel-window-policy.spec.ts",
          "sha256": "e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692",
          "bytes": 2077
        },
        {
          "path": "api-app/src/domain/inbox/channel-window-policy.ts",
          "archive_path": "src/domain/inbox/channel-window-policy.ts",
          "sha256": "46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e",
          "bytes": 5700
        },
        {
          "path": "api-app/src/domain/inbox/conversation-start.service.spec.ts",
          "archive_path": "src/domain/inbox/conversation-start.service.spec.ts",
          "sha256": "e72060157628dbd2c27d27bc2c55d3d2a2f40d6f56ba344c97c97e69b80d0fc2",
          "bytes": 4588
        },
        {
          "path": "api-app/src/domain/inbox/conversation-start.service.ts",
          "archive_path": "src/domain/inbox/conversation-start.service.ts",
          "sha256": "97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118",
          "bytes": 2328
        },
        {
          "path": "api-app/src/domain/inbox/conversations.service.ts",
          "archive_path": "src/domain/inbox/conversations.service.ts",
          "sha256": "6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c",
          "bytes": 9091
        },
        {
          "path": "api-app/src/domain/inbox/dispatch-admission.service.spec.ts",
          "archive_path": "src/domain/inbox/dispatch-admission.service.spec.ts",
          "sha256": "412272cc81a0c1b18a61b95940b875adb38dc798edba95928db4e95f224f77b2",
          "bytes": 14779
        },
        {
          "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
          "archive_path": "src/domain/inbox/dispatch-admission.service.ts",
          "sha256": "bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc",
          "bytes": 45213
        },
        {
          "path": "api-app/src/domain/inbox/historico.service.spec.ts",
          "archive_path": "src/domain/inbox/historico.service.spec.ts",
          "sha256": "eb1ca83e588c58382a332aee0fdda200f3eb6cb5f8c0cbd430e9790623393ec0",
          "bytes": 1015
        },
        {
          "path": "api-app/src/domain/inbox/historico.service.ts",
          "archive_path": "src/domain/inbox/historico.service.ts",
          "sha256": "811212eeb5b9e8318ef344eb6660385382707cb6d6882c5e9f84e8d4951ccfaa",
          "bytes": 6325
        },
        {
          "path": "api-app/src/domain/inbox/incoming.service.ts",
          "archive_path": "src/domain/inbox/incoming.service.ts",
          "sha256": "390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b",
          "bytes": 6157
        },
        {
          "path": "api-app/src/domain/inbox/incoming.typebot.integration.spec.ts",
          "archive_path": "src/domain/inbox/incoming.typebot.integration.spec.ts",
          "sha256": "7b0e7d75fc5809b8c950896818779402fe2bf32ef37a94d970fe081240562975",
          "bytes": 7081
        },
        {
          "path": "api-app/src/domain/inbox/incoming.typebot.spec.ts",
          "archive_path": "src/domain/inbox/incoming.typebot.spec.ts",
          "sha256": "faedadd6fdf05bf445b846e89dd17c608b0cc3599e3463c89f6338f6febad72f",
          "bytes": 662
        },
        {
          "path": "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts",
          "archive_path": "src/domain/inbox/initial-message-template-renderer.spec.ts",
          "sha256": "c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0",
          "bytes": 5150
        },
        {
          "path": "api-app/src/domain/inbox/initial-message-template-renderer.ts",
          "archive_path": "src/domain/inbox/initial-message-template-renderer.ts",
          "sha256": "a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf",
          "bytes": 5657
        },
        {
          "path": "api-app/src/domain/inbox/initial-message.service.spec.ts",
          "archive_path": "src/domain/inbox/initial-message.service.spec.ts",
          "sha256": "70b7a925743cb8776729dd9280abb021e6a9e9c81d4eb45edda0c77c2e68f317",
          "bytes": 6686
        },
        {
          "path": "api-app/src/domain/inbox/initial-message.service.ts",
          "archive_path": "src/domain/inbox/initial-message.service.ts",
          "sha256": "ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6",
          "bytes": 24538
        },
        {
          "path": "api-app/src/domain/inbox/message-acceptance.service.spec.ts",
          "archive_path": "src/domain/inbox/message-acceptance.service.spec.ts",
          "sha256": "f6561e2e2dce670f94ce95510f97da0680249ff2484b0c1098d5e6a3b1232ee6",
          "bytes": 3577
        },
        {
          "path": "api-app/src/domain/inbox/message-acceptance.service.ts",
          "archive_path": "src/domain/inbox/message-acceptance.service.ts",
          "sha256": "71194c70b12cb920054586a7a86266d90f8eca0b7008b1b5688627e0694979f1",
          "bytes": 16712
        },
        {
          "path": "api-app/src/domain/inbox/outbound.service.spec.ts",
          "archive_path": "src/domain/inbox/outbound.service.spec.ts",
          "sha256": "92b24248602908f4a35ed5a2cf8f9f7d3d3ed7174739b2ad72404f6a041f3dfd",
          "bytes": 18621
        },
        {
          "path": "api-app/src/domain/inbox/outbound.service.ts",
          "archive_path": "src/domain/inbox/outbound.service.ts",
          "sha256": "0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1",
          "bytes": 40195
        },
        {
          "path": "api-app/src/domain/inbox/timeline-pagination.spec.ts",
          "archive_path": "src/domain/inbox/timeline-pagination.spec.ts",
          "sha256": "a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d",
          "bytes": 1373
        },
        {
          "path": "api-app/src/domain/inbox/timeline-pagination.ts",
          "archive_path": "src/domain/inbox/timeline-pagination.ts",
          "sha256": "d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af",
          "bytes": 2469
        },
        {
          "path": "api-app/src/domain/integration/api-key.service.spec.ts",
          "archive_path": "src/domain/integration/api-key.service.spec.ts",
          "sha256": "41ef8944d57caec1a6db7bc7c0c05c9e4936a7cb5992bf45f26ecd646df3c976",
          "bytes": 727
        },
        {
          "path": "api-app/src/domain/integration/api-key.service.ts",
          "archive_path": "src/domain/integration/api-key.service.ts",
          "sha256": "bde94ae81c4a17c4cf6cb8b28d8e9d2cdb22feb1def06848f6f125e8018917c5",
          "bytes": 2125
        },
        {
          "path": "api-app/src/domain/integration/outbound-webhook.service.ts",
          "archive_path": "src/domain/integration/outbound-webhook.service.ts",
          "sha256": "fdc13f9aadcc8f0e9c566643b7da08cf7cb0aec63c821ef98025e4f2a3baee1b",
          "bytes": 1851
        },
        {
          "path": "api-app/src/domain/integration/rate-limit.service.spec.ts",
          "archive_path": "src/domain/integration/rate-limit.service.spec.ts",
          "sha256": "88e910431be104406fb84c375ddc83153755a9d7b4a81a9c098b0b7cfd2cbb12",
          "bytes": 1096
        },
        {
          "path": "api-app/src/domain/integration/rate-limit.service.ts",
          "archive_path": "src/domain/integration/rate-limit.service.ts",
          "sha256": "0579e073c05f57f9a87cf0f96f0301d01661957bea2490140c1e63566686503f",
          "bytes": 1558
        },
        {
          "path": "api-app/src/domain/message-templates/template-definition.spec.ts",
          "archive_path": "src/domain/message-templates/template-definition.spec.ts",
          "sha256": "9a60549d1c79d73889fd2d47b7ea3bb25b8a0bf140da805f64216decc6ff9d97",
          "bytes": 7219
        },
        {
          "path": "api-app/src/domain/message-templates/template-definition.ts",
          "archive_path": "src/domain/message-templates/template-definition.ts",
          "sha256": "1f28bfd19454b1e187b854c4f2e9785b59e7726032c20f82d62460d87401203c",
          "bytes": 9341
        },
        {
          "path": "api-app/src/domain/message-templates/template-draft.service.ts",
          "archive_path": "src/domain/message-templates/template-draft.service.ts",
          "sha256": "429a078fb48d5a66601d83883275dcc12cea659692e463e94a17d41d5cdf0713",
          "bytes": 29240
        },
        {
          "path": "api-app/src/domain/message-templates/template-management.dependencies.spec.ts",
          "archive_path": "src/domain/message-templates/template-management.dependencies.spec.ts",
          "sha256": "a03a567e5b96a348b4ab40bb18282a555d30ad3533e6efb929c5d2f2614c82b2",
          "bytes": 3510
        },
        {
          "path": "api-app/src/domain/message-templates/template-management.ports.spec.ts",
          "archive_path": "src/domain/message-templates/template-management.ports.spec.ts",
          "sha256": "ddf581459b66bf0eb26ec710ded050f45713e5dd5317066cea574dacf57a68bc",
          "bytes": 2963
        },
        {
          "path": "api-app/src/domain/message-templates/template-management.ports.ts",
          "archive_path": "src/domain/message-templates/template-management.ports.ts",
          "sha256": "c7ed169d87a4224f82f8d1abe109bfa02b913bb2cb63303fc6477673f45ed693",
          "bytes": 4562
        },
        {
          "path": "api-app/src/domain/message-templates/template-observation.service.ts",
          "archive_path": "src/domain/message-templates/template-observation.service.ts",
          "sha256": "41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488",
          "bytes": 39343
        },
        {
          "path": "api-app/src/domain/message-templates/template-submission.service.ts",
          "archive_path": "src/domain/message-templates/template-submission.service.ts",
          "sha256": "a2b8b33ecfb0af165c2b94b50703d18a364d5b64ef581bbdd7659325bc631709",
          "bytes": 63540
        },
        {
          "path": "api-app/src/domain/message-templates/template-transaction-boundary.ts",
          "archive_path": "src/domain/message-templates/template-transaction-boundary.ts",
          "sha256": "ea3e0550ad5c82b263391dbfb3dae6b9e8656d219f18aa0d7c55cd5668722123",
          "bytes": 978
        },
        {
          "path": "api-app/src/domain/painel/painel.service.ts",
          "archive_path": "src/domain/painel/painel.service.ts",
          "sha256": "d916a08d748336f2f17af8204504707c49db7396642c2c79067a6f71be68609d",
          "bytes": 2281
        },
        {
          "path": "api-app/src/domain/produto/modulos.service.ts",
          "archive_path": "src/domain/produto/modulos.service.ts",
          "sha256": "1283ac1879467c3ebb079daaf29bfd5cda9f0ca02fd45a1b3f8ec865c7d5544e",
          "bytes": 3094
        },
        {
          "path": "api-app/src/domain/produto/onboarding.service.ts",
          "archive_path": "src/domain/produto/onboarding.service.ts",
          "sha256": "3b643a474a51b4ef0050f520d5059067897572843317e4a632cf0e37a6228c5e",
          "bytes": 6966
        },
        {
          "path": "api-app/src/domain/setor/setor.service.ts",
          "archive_path": "src/domain/setor/setor.service.ts",
          "sha256": "d8cb22d68452d1ab9ea9daa69fe9660d867612f81db8e9e9a7fb34a6e56cda84",
          "bytes": 12971
        },
        {
          "path": "api-app/src/domain/tenancy/tenancy.service.ts",
          "archive_path": "src/domain/tenancy/tenancy.service.ts",
          "sha256": "c9348f86f1f2bcfd4af3f9bd3e91cb5218d81cf13098989b5f6ea64acbb41398",
          "bytes": 10923
        },
        {
          "path": "api-app/src/health/health.controller.ts",
          "archive_path": "src/health/health.controller.ts",
          "sha256": "92bdd3eeecdd69ed564e7089a910e6d6d667e55e3f6f3965898911e575b98b20",
          "bytes": 890
        },
        {
          "path": "api-app/src/health/health.module.ts",
          "archive_path": "src/health/health.module.ts",
          "sha256": "9ce204c0535a897d545388170bcb6e308716d70a16074fbe94330787c8a95489",
          "bytes": 474
        },
        {
          "path": "api-app/src/infra/arquivos/armazenamento.ts",
          "archive_path": "src/infra/arquivos/armazenamento.ts",
          "sha256": "de7a13259b03599c709b9c0097a4ddc84d07990f1a48ceb7f2aca86a826416a6",
          "bytes": 4798
        },
        {
          "path": "api-app/src/infra/config/modulos.spec.ts",
          "archive_path": "src/infra/config/modulos.spec.ts",
          "sha256": "57d60337ce3564e071b019e127ab6d409759eea8ae77e2d45095e4fea877928e",
          "bytes": 5203
        },
        {
          "path": "api-app/src/infra/config/modulos.ts",
          "archive_path": "src/infra/config/modulos.ts",
          "sha256": "fd1ccabf7bee088f230a12d773c56a5d41fc07642d04262b55a6497a7b9c2a03",
          "bytes": 5134
        },
        {
          "path": "api-app/src/infra/http/body-parsers.ts",
          "archive_path": "src/infra/http/body-parsers.ts",
          "sha256": "0f65f24e300b2204362fff3ee1c799a35baecb1c57d141fe0ac0957091a5e624",
          "bytes": 1023
        },
        {
          "path": "api-app/src/infra/http/origens.ts",
          "archive_path": "src/infra/http/origens.ts",
          "sha256": "db66c02e2ce21f725d445e6c4137a1d8462ffd85827a1cf4a211850e502c79b8",
          "bytes": 1275
        },
        {
          "path": "api-app/src/infra/prisma/banco-atrasado.filter.ts",
          "archive_path": "src/infra/prisma/banco-atrasado.filter.ts",
          "sha256": "e4329ef4ccc2b91596afe82137286dbb7328f64ceec786440f28c7b8e45b0eba",
          "bytes": 1823
        },
        {
          "path": "api-app/src/infra/prisma/migracoes.ts",
          "archive_path": "src/infra/prisma/migracoes.ts",
          "sha256": "d416bab2e0c7cdaef7313b92195a1d58b18ac665afb86d3b1e05ffad0bd7ae62",
          "bytes": 1346
        },
        {
          "path": "api-app/src/infra/prisma/prisma.module.ts",
          "archive_path": "src/infra/prisma/prisma.module.ts",
          "sha256": "14d19dcd7848e4d134cd9eaa205818d5e0302123a5fc5ea2440d358a39f2fd25",
          "bytes": 219
        },
        {
          "path": "api-app/src/infra/prisma/prisma.service.ts",
          "archive_path": "src/infra/prisma/prisma.service.ts",
          "sha256": "8c6034455186bfc6497b329f94af7c867fb6f28b9226d54db5716a907db6e200",
          "bytes": 393
        },
        {
          "path": "api-app/src/infra/session/session.service.spec.ts",
          "archive_path": "src/infra/session/session.service.spec.ts",
          "sha256": "dbb215e931a5856269b07057ce74c7af7ee66c4947961fbf1a01f903f3c7f4fb",
          "bytes": 5306
        },
        {
          "path": "api-app/src/infra/session/session.service.ts",
          "archive_path": "src/infra/session/session.service.ts",
          "sha256": "884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200",
          "bytes": 5483
        },
        {
          "path": "api-app/src/integrations/channels/account-reference.ts",
          "archive_path": "src/integrations/channels/account-reference.ts",
          "sha256": "da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24",
          "bytes": 424
        },
        {
          "path": "api-app/src/integrations/channels/channel-adapter-factory.ts",
          "archive_path": "src/integrations/channels/channel-adapter-factory.ts",
          "sha256": "e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc",
          "bytes": 440
        },
        {
          "path": "api-app/src/integrations/channels/channel-adapter-registry.ts",
          "archive_path": "src/integrations/channels/channel-adapter-registry.ts",
          "sha256": "655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b",
          "bytes": 975
        },
        {
          "path": "api-app/src/integrations/channels/channel-transport.module.ts",
          "archive_path": "src/integrations/channels/channel-transport.module.ts",
          "sha256": "4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d",
          "bytes": 2242
        },
        {
          "path": "api-app/src/integrations/channels/evolution-channel.ts",
          "archive_path": "src/integrations/channels/evolution-channel.ts",
          "sha256": "6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34",
          "bytes": 2211
        },
        {
          "path": "api-app/src/integrations/channels/meta-channel.ts",
          "archive_path": "src/integrations/channels/meta-channel.ts",
          "sha256": "99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26",
          "bytes": 3900
        },
        {
          "path": "api-app/src/integrations/channels/prisma-channel-resolver.ts",
          "archive_path": "src/integrations/channels/prisma-channel-resolver.ts",
          "sha256": "60005fd226534a178b646d6ec775bb059ec55cc4cfea24a3d72d2c6e4a1ca64a",
          "bytes": 25890
        },
        {
          "path": "api-app/src/integrations/email/email.client.spec.ts",
          "archive_path": "src/integrations/email/email.client.spec.ts",
          "sha256": "ea88b5a7243aec296b461ffe612b41ba40f141b8608e81e071f605ee659ce2c5",
          "bytes": 3954
        },
        {
          "path": "api-app/src/integrations/email/email.client.ts",
          "archive_path": "src/integrations/email/email.client.ts",
          "sha256": "95d89c14c2022a0ff9ea87e2acc173f319abfe766875156999cd55e347dc934a",
          "bytes": 2629
        },
        {
          "path": "api-app/src/integrations/evolution/evolution.client.spec.ts",
          "archive_path": "src/integrations/evolution/evolution.client.spec.ts",
          "sha256": "119d962fdcd9c895b75845dca74d8506147e11480d74b82e8c37f29f97c04081",
          "bytes": 6530
        },
        {
          "path": "api-app/src/integrations/evolution/evolution.client.ts",
          "archive_path": "src/integrations/evolution/evolution.client.ts",
          "sha256": "b0824e8fd4f801a239521855aaa02da5e0943a8c86c4ac8778e2f1f352821698",
          "bytes": 7214
        },
        {
          "path": "api-app/src/integrations/message-templates/template-management.module.ts",
          "archive_path": "src/integrations/message-templates/template-management.module.ts",
          "sha256": "aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd",
          "bytes": 595
        },
        {
          "path": "api-app/src/integrations/message-templates/template-management.resolver.ts",
          "archive_path": "src/integrations/message-templates/template-management.resolver.ts",
          "sha256": "1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00",
          "bytes": 4910
        },
        {
          "path": "api-app/src/integrations/meta/initial-message.client.spec.ts",
          "archive_path": "src/integrations/meta/initial-message.client.spec.ts",
          "sha256": "0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057",
          "bytes": 4339
        },
        {
          "path": "api-app/src/integrations/meta/initial-message.client.ts",
          "archive_path": "src/integrations/meta/initial-message.client.ts",
          "sha256": "e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721",
          "bytes": 11410
        },
        {
          "path": "api-app/src/integrations/meta/message-template.client.spec.ts",
          "archive_path": "src/integrations/meta/message-template.client.spec.ts",
          "sha256": "6b42b44577e2c06ae73fb0525dac10b99f7364a04e2c04184dc303c6d47872b8",
          "bytes": 22687
        },
        {
          "path": "api-app/src/integrations/meta/message-template.client.ts",
          "archive_path": "src/integrations/meta/message-template.client.ts",
          "sha256": "8dff223f7a97632cf228800cdbbb12ce6f5b151efc5fa30411d03e5ec3280cb5",
          "bytes": 21888
        },
        {
          "path": "api-app/src/integrations/meta/meta.client.spec.ts",
          "archive_path": "src/integrations/meta/meta.client.spec.ts",
          "sha256": "d7e76f5c392afab1638363d3c851f8ce8c5223ff27c64801a79fdc8ec00d5e7a",
          "bytes": 38572
        },
        {
          "path": "api-app/src/integrations/meta/meta.client.ts",
          "archive_path": "src/integrations/meta/meta.client.ts",
          "sha256": "9f954f6c1c2bd10030f5eed0cb42e493d6e480106bcfc3f44977cb97a716d34f",
          "bytes": 17388
        },
        {
          "path": "api-app/src/integrations/typebot/typebot.client.spec.ts",
          "archive_path": "src/integrations/typebot/typebot.client.spec.ts",
          "sha256": "1d78eaa3e63fa27550be7a74bb59dca841bb738db46ced76cd41136648231e74",
          "bytes": 2562
        },
        {
          "path": "api-app/src/integrations/typebot/typebot.client.ts",
          "archive_path": "src/integrations/typebot/typebot.client.ts",
          "sha256": "fe5c461b56d9c363953ba301129b3e78b0f3f408c510e0ac03ce8ec2c96ab873",
          "bytes": 3195
        },
        {
          "path": "api-app/src/main.spec.ts",
          "archive_path": "src/main.spec.ts",
          "sha256": "082a0836f57481e22d2c2dd655f65cca40d008016561e49543b82b8e3430dc5b",
          "bytes": 1630
        },
        {
          "path": "api-app/src/main.ts",
          "archive_path": "src/main.ts",
          "sha256": "05ff096cdcf67a8a153736264ed46a7faf9f5c0f45325c2d3fed95188fb2b1ad",
          "bytes": 5963
        },
        {
          "path": "api-app/src/realtime/realtime.module.ts",
          "archive_path": "src/realtime/realtime.module.ts",
          "sha256": "c8ed324d8e8861fe9b97538161639aedade82420a55d53bb25b9d27441029139",
          "bytes": 394
        },
        {
          "path": "api-app/src/realtime/realtime.service.ts",
          "archive_path": "src/realtime/realtime.service.ts",
          "sha256": "69d43aa7b694fa744819823f7e24071c250b390ad54d09446b2f2c797a7f3829",
          "bytes": 4686
        },
        {
          "path": "api-app/src/rotinas/agendador.service.ts",
          "archive_path": "src/rotinas/agendador.service.ts",
          "sha256": "b639a996ce541ace79c139cd525229367f198dac2aa769ba0dfa8b0194dcbec2",
          "bytes": 2049
        },
        {
          "path": "api-app/src/rotinas/expurgo-de-webhook.rotina.ts",
          "archive_path": "src/rotinas/expurgo-de-webhook.rotina.ts",
          "sha256": "b0cac2efff44dc5f3b652f0a3f384c9e8cf4801f31319442b13454963b2951a6",
          "bytes": 2073
        },
        {
          "path": "api-app/src/rotinas/rotina-periodica.ts",
          "archive_path": "src/rotinas/rotina-periodica.ts",
          "sha256": "71a72d85b993a99c317a962f3b3477129cf265ac3ec54c9f092c3c704d3dc06c",
          "bytes": 5043
        },
        {
          "path": "api-app/src/rotinas/rotinas.module.ts",
          "archive_path": "src/rotinas/rotinas.module.ts",
          "sha256": "44c7a4949922e7194fc0584381c0d7606517a05ae5179274a50e1cb1b59fac44",
          "bytes": 531
        },
        {
          "path": "api-app/src/surfaces/bff/arquivos.controller.ts",
          "archive_path": "src/surfaces/bff/arquivos.controller.ts",
          "sha256": "4c5119ee8aa8c77cffa72b5ac0d0b4a98db872c8784dfc037fa5937a32210d65",
          "bytes": 2245
        },
        {
          "path": "api-app/src/surfaces/bff/atividades.controller.ts",
          "archive_path": "src/surfaces/bff/atividades.controller.ts",
          "sha256": "71b8f699c7ff2a0884d4f4e6c999470769ee8d21e123e86b181c985f84f86b3c",
          "bytes": 1998
        },
        {
          "path": "api-app/src/surfaces/bff/auth.controller.ts",
          "archive_path": "src/surfaces/bff/auth.controller.ts",
          "sha256": "1cd884fe1a716d82b67ffbcc1a4c6cbcf237a30111a6bd0a2a92c48ad7d32381",
          "bytes": 7275
        },
        {
          "path": "api-app/src/surfaces/bff/bff.module.ts",
          "archive_path": "src/surfaces/bff/bff.module.ts",
          "sha256": "8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a",
          "bytes": 6282
        },
        {
          "path": "api-app/src/surfaces/bff/channels.controller.ts",
          "archive_path": "src/surfaces/bff/channels.controller.ts",
          "sha256": "c7a3917c84ac1921b757fd7bca5a9b0b29ab2078312fcf2fd421104ef41a6182",
          "bytes": 6018
        },
        {
          "path": "api-app/src/surfaces/bff/conversations.controller.ts",
          "archive_path": "src/surfaces/bff/conversations.controller.ts",
          "sha256": "f8682cc211695df59caaa3f32799ad6a0444e120d683592e32984a71d71c8c1d",
          "bytes": 19043
        },
        {
          "path": "api-app/src/surfaces/bff/historico.controller.ts",
          "archive_path": "src/surfaces/bff/historico.controller.ts",
          "sha256": "3bab5868bfabde5d37be8b4d2579c8dc417307904d53c743c8a7ce522526b84a",
          "bytes": 4057
        },
        {
          "path": "api-app/src/surfaces/bff/integracao.controller.ts",
          "archive_path": "src/surfaces/bff/integracao.controller.ts",
          "sha256": "d060c6fec31f188950193a163ddf7093f9613c65e0e8d27ca597b09c2b6c2bdb",
          "bytes": 11352
        },
        {
          "path": "api-app/src/surfaces/bff/integracao.typebot.spec.ts",
          "archive_path": "src/surfaces/bff/integracao.typebot.spec.ts",
          "sha256": "38cf0dd1746b00e6d7ec110e549fe29fad24e9fd8f4554465877f756a242af6b",
          "bytes": 1925
        },
        {
          "path": "api-app/src/surfaces/bff/me.controller.ts",
          "archive_path": "src/surfaces/bff/me.controller.ts",
          "sha256": "0edd826d4e9a3c0b8cde4334bf2e88f360f5f5e9d5db99e5dfc4382b5bf71bb0",
          "bytes": 9442
        },
        {
          "path": "api-app/src/surfaces/bff/message-templates.controller.ts",
          "archive_path": "src/surfaces/bff/message-templates.controller.ts",
          "sha256": "0e0449a80852a4513f626d0df7b1a5bb17b034eeceb50f53842fb91454ff4491",
          "bytes": 11822
        },
        {
          "path": "api-app/src/surfaces/bff/number-registrations.controller.ts",
          "archive_path": "src/surfaces/bff/number-registrations.controller.ts",
          "sha256": "c57797667ff26a4ea74aa939e4972a8cd8f442c9beafa166b1bdf808e19c236e",
          "bytes": 5003
        },
        {
          "path": "api-app/src/surfaces/bff/onboarding.controller.ts",
          "archive_path": "src/surfaces/bff/onboarding.controller.ts",
          "sha256": "beb15af03cdeec8a5202ec0dff529c41fb991b4b874bd10ee3e4cd684c478240",
          "bytes": 2153
        },
        {
          "path": "api-app/src/surfaces/bff/painel.controller.ts",
          "archive_path": "src/surfaces/bff/painel.controller.ts",
          "sha256": "3894286559507f9fcae0ddedf3f66cdd879e4871d4a5f835855aa4a33458fa3d",
          "bytes": 798
        },
        {
          "path": "api-app/src/surfaces/bff/session.middleware.ts",
          "archive_path": "src/surfaces/bff/session.middleware.ts",
          "sha256": "80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211",
          "bytes": 5651
        },
        {
          "path": "api-app/src/surfaces/bff/setores.controller.ts",
          "archive_path": "src/surfaces/bff/setores.controller.ts",
          "sha256": "b94cdefcf0c28accd0c0fdf9088ba695bb10a7bd434d6732bab9bd32c71d0558",
          "bytes": 4741
        },
        {
          "path": "api-app/src/surfaces/bff/usuarios.controller.ts",
          "archive_path": "src/surfaces/bff/usuarios.controller.ts",
          "sha256": "09a4125968a55021ecb9942d1466fbc80ff61fc71f69995dc231c814ce7cb846",
          "bytes": 4345
        },
        {
          "path": "api-app/src/surfaces/internal/internal.module.ts",
          "archive_path": "src/surfaces/internal/internal.module.ts",
          "sha256": "6fbb35d40890862af9cfdc1b8b87f7ebd2b2e8d0e256f454f68a1053eef34f04",
          "bytes": 1098
        },
        {
          "path": "api-app/src/surfaces/internal/mantenedoras.controller.ts",
          "archive_path": "src/surfaces/internal/mantenedoras.controller.ts",
          "sha256": "35359bd6185a43ca148fba1dfb7edc048f25d7890e377602c8f2222d78924c77",
          "bytes": 1624
        },
        {
          "path": "api-app/src/surfaces/internal/service-credential.middleware.ts",
          "archive_path": "src/surfaces/internal/service-credential.middleware.ts",
          "sha256": "b2db1b715a65995d8a21b3da296de93930292cc6bd23f72b4cba24d6cdfe093b",
          "bytes": 1391
        },
        {
          "path": "api-app/src/surfaces/public/api-key.middleware.ts",
          "archive_path": "src/surfaces/public/api-key.middleware.ts",
          "sha256": "f76cd8854c8145c4b456e8c9d2d1ab000c17bc5278af76997745b5696edd9877",
          "bytes": 1274
        },
        {
          "path": "api-app/src/surfaces/public/conversations.controller.ts",
          "archive_path": "src/surfaces/public/conversations.controller.ts",
          "sha256": "bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1",
          "bytes": 12059
        },
        {
          "path": "api-app/src/surfaces/public/public.module.ts",
          "archive_path": "src/surfaces/public/public.module.ts",
          "sha256": "00a96d54fde7061f61f4ddf2b9cef836a02ad77ca29b62ea422695b9d8f90ef8",
          "bytes": 1208
        },
        {
          "path": "api-app/src/surfaces/webhooks/evolution.controller.ts",
          "archive_path": "src/surfaces/webhooks/evolution.controller.ts",
          "sha256": "12139a5b50b4dacf43492e038c91f006c9db999d0f6a76fd5d73e45ee987a041",
          "bytes": 8204
        },
        {
          "path": "api-app/src/surfaces/webhooks/meta.controller.ts",
          "archive_path": "src/surfaces/webhooks/meta.controller.ts",
          "sha256": "261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f",
          "bytes": 7195
        },
        {
          "path": "api-app/src/surfaces/webhooks/webhooks.module.ts",
          "archive_path": "src/surfaces/webhooks/webhooks.module.ts",
          "sha256": "abc8fd7960fcca1ce43d21d44a90f8d4708d47e07bde9a48c0009e02dc0503a6",
          "bytes": 1111
        },
        {
          "path": "api-app/tsconfig.build.json",
          "archive_path": "tsconfig.build.json",
          "sha256": "44e82cf32b2bd7cfdb7c4d9ca48ab13101f6ff66349578545d2c229ef55cbca6",
          "bytes": 102
        },
        {
          "path": "api-app/tsconfig.json",
          "archive_path": "tsconfig.json",
          "sha256": "5a8a8b3e2e00213a8cdd3877ecb7347944b689875a989cd3bbe2effef64816cc",
          "bytes": 760
        }
      ],
      "status": "Prepared positive-only archive; no image build or actual runtime use."
    },
    {
      "service": "web",
      "generated_archive": "/tmp/stcon04-build-context-web-e53.tar",
      "archive_sha256": "c06f8b1f0923fd257806084e7250ad2ca4468349ef46eca7222630df2a00e612",
      "record_count": 47,
      "records": [
        {
          "path": "web-app/Dockerfile",
          "archive_path": "Dockerfile",
          "sha256": "b3fb2e04dc033ec8977926c93eb8cec36bf44f6351652bdb2f739325e4be19d4",
          "bytes": 1262
        },
        {
          "path": "web-app/docker/40-config-js.sh",
          "archive_path": "docker/40-config-js.sh",
          "sha256": "77b929c9a8705015ea9fb4a53fef39a03aff72f6d54d95c382fc4540e9d035c6",
          "bytes": 1243
        },
        {
          "path": "web-app/index.html",
          "archive_path": "index.html",
          "sha256": "0adc005d98f50e7ddc59280f062b1acd36a6a6e794347677b03bb72032dc341a",
          "bytes": 596
        },
        {
          "path": "web-app/nginx/default.conf.template",
          "archive_path": "nginx/default.conf.template",
          "sha256": "0cdafce3f985f351a0610e46b76df5babbaefa6c40d428a1bf90e093ce586313",
          "bytes": 1444
        },
        {
          "path": "web-app/package-lock.json",
          "archive_path": "package-lock.json",
          "sha256": "546aec97be8273cf195a16b75c0127474ea3a5042668f8d4c93aab96c1619c8f",
          "bytes": 78215
        },
        {
          "path": "web-app/package.json",
          "archive_path": "package.json",
          "sha256": "fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de",
          "bytes": 701
        },
        {
          "path": "web-app/public/config.js",
          "archive_path": "public/config.js",
          "sha256": "1ad17fefa4173ed847cabd79e7fdc1b262fa19ea4ff33c3ef435e141275fb532",
          "bytes": 444
        },
        {
          "path": "web-app/public/privacidade.html",
          "archive_path": "public/privacidade.html",
          "sha256": "d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d",
          "bytes": 12865
        },
        {
          "path": "web-app/src/App.tsx",
          "archive_path": "src/App.tsx",
          "sha256": "2d9f3b3d03658a8d6d6132986346f3be8f36a2582faca29285b3d46c9920307e",
          "bytes": 12285
        },
        {
          "path": "web-app/src/EnvioDeImagem.tsx",
          "archive_path": "src/EnvioDeImagem.tsx",
          "sha256": "23dabf408b9a42f823b645f5cff7f4381a24088c387b4c2b276181cd8626c0d8",
          "bytes": 2163
        },
        {
          "path": "web-app/src/Erro.tsx",
          "archive_path": "src/Erro.tsx",
          "sha256": "72920e0bccd28660e93413d9c422b47c222f2fcfa27d69535dcd609b9b203c0c",
          "bytes": 1545
        },
        {
          "path": "web-app/src/api.spec.ts",
          "archive_path": "src/api.spec.ts",
          "sha256": "9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9",
          "bytes": 9776
        },
        {
          "path": "web-app/src/api.ts",
          "archive_path": "src/api.ts",
          "sha256": "7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c",
          "bytes": 16785
        },
        {
          "path": "web-app/src/cadastroNumero.lifecycle.spec.ts",
          "archive_path": "src/cadastroNumero.lifecycle.spec.ts",
          "sha256": "a340c48e30c712cafecb1d35fe20bd3841c46e2dfbda21645fc8ef3ed6977834",
          "bytes": 3960
        },
        {
          "path": "web-app/src/cadastroNumero.lifecycle.ts",
          "archive_path": "src/cadastroNumero.lifecycle.ts",
          "sha256": "5c60a8fc7456c82a7d782b3484ba447bda826e65bf93a9175a991dc50be254a3",
          "bytes": 6020
        },
        {
          "path": "web-app/src/cadastroNumero.spec.ts",
          "archive_path": "src/cadastroNumero.spec.ts",
          "sha256": "9c2581c1886d108c4c153d485fd77f017805c2e3b813a9536d21d0296f2a1ecb",
          "bytes": 1513
        },
        {
          "path": "web-app/src/cadastroNumero.ts",
          "archive_path": "src/cadastroNumero.ts",
          "sha256": "584401ed8ab1ce1d53950998e85765a35d55d7ac4961286924f98e4132edcb6b",
          "bytes": 9708
        },
        {
          "path": "web-app/src/componentes/CadastroNumero.tsx",
          "archive_path": "src/componentes/CadastroNumero.tsx",
          "sha256": "9afbe4f419dcf4b5133f8103a0082b6eaa32837aaaf307ffbc61489c50f8cb78",
          "bytes": 43466
        },
        {
          "path": "web-app/src/componentes/NovaConversa.spec.ts",
          "archive_path": "src/componentes/NovaConversa.spec.ts",
          "sha256": "84184865db156d6c147e382982e235ea82f16ea9892cb0cc6e59f16ac1393757",
          "bytes": 6611
        },
        {
          "path": "web-app/src/componentes/NovaConversa.tsx",
          "archive_path": "src/componentes/NovaConversa.tsx",
          "sha256": "2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd",
          "bytes": 40678
        },
        {
          "path": "web-app/src/config.ts",
          "archive_path": "src/config.ts",
          "sha256": "ca30d02d04774b79d6e62715c83c49dd23f1db02f0b49ec6781634acbf09befb",
          "bytes": 1952
        },
        {
          "path": "web-app/src/estilo.css",
          "archive_path": "src/estilo.css",
          "sha256": "a86305e2303f640345c07d2b9f7ed9274b328d7459e714225e7f05885255809a",
          "bytes": 11062
        },
        {
          "path": "web-app/src/main.tsx",
          "archive_path": "src/main.tsx",
          "sha256": "42d0c9e45f19eb88f8cdbfd81343004becacf4b47c248f4d03d52bb9f951b9f3",
          "bytes": 301
        },
        {
          "path": "web-app/src/telas/Consultar.tsx",
          "archive_path": "src/telas/Consultar.tsx",
          "sha256": "b65ce0320a082df811796ca66c73990fd57512ee123802fd2123f8dfad90fd89",
          "bytes": 7114
        },
        {
          "path": "web-app/src/telas/DefinirSenha.tsx",
          "archive_path": "src/telas/DefinirSenha.tsx",
          "sha256": "7b3a3eeafe8af2f315d299cc40f612568a5216b9d99a5a52b50925cffbc466cd",
          "bytes": 3821
        },
        {
          "path": "web-app/src/telas/Historico.tsx",
          "archive_path": "src/telas/Historico.tsx",
          "sha256": "a950e2571adc86cf5a390f7602ae2193d4b0de45d1c1f5b7640697308d398414",
          "bytes": 4448
        },
        {
          "path": "web-app/src/telas/IdentidadeVisual.tsx",
          "archive_path": "src/telas/IdentidadeVisual.tsx",
          "sha256": "2b9720d7eaf3b0ef078ee6827d3d7fb3c93aa0b4c209662fbf143468c51cefa2",
          "bytes": 2531
        },
        {
          "path": "web-app/src/telas/Inbox.tsx",
          "archive_path": "src/telas/Inbox.tsx",
          "sha256": "bbd6facb3f60fafb01f661ec5fe6c0dec826b3023c9ba5ad44aec5b31865ddbd",
          "bytes": 25549
        },
        {
          "path": "web-app/src/telas/Integracao.tsx",
          "archive_path": "src/telas/Integracao.tsx",
          "sha256": "66e87b87fbd35596fe064079be121c25f0d942c1b50b6b3b239fe765493fa59b",
          "bytes": 4158
        },
        {
          "path": "web-app/src/telas/Login.tsx",
          "archive_path": "src/telas/Login.tsx",
          "sha256": "3b62a752d0e4f71679dab3427862884bb8ebc5863d16d240a0c84d1d0b1ce923",
          "bytes": 2946
        },
        {
          "path": "web-app/src/telas/Modelos.spec.ts",
          "archive_path": "src/telas/Modelos.spec.ts",
          "sha256": "123e1b345342bdba0d1e9de07886c5116fd21c66d92d77a9fd814478142adf52",
          "bytes": 26616
        },
        {
          "path": "web-app/src/telas/Modelos.tsx",
          "archive_path": "src/telas/Modelos.tsx",
          "sha256": "ec5410d1e38a5dd963fe48d3ba715697d9c49cd574875c784fa8e6300275771c",
          "bytes": 58744
        },
        {
          "path": "web-app/src/telas/Numeros.tsx",
          "archive_path": "src/telas/Numeros.tsx",
          "sha256": "22cf5877d6336e4c22b8650402c5913b064278b9ba639e20e10f9a80c00fc791",
          "bytes": 3177
        },
        {
          "path": "web-app/src/telas/Painel.tsx",
          "archive_path": "src/telas/Painel.tsx",
          "sha256": "7b678b29d8467dd8c22c4d8fa3667483b157c1495fb23b1368a34c48b2c6fdb2",
          "bytes": 3161
        },
        {
          "path": "web-app/src/telas/Perfil.tsx",
          "archive_path": "src/telas/Perfil.tsx",
          "sha256": "f425279d3598d14a609050d960b8848447afc3bace89fc0761f1cec2f045df0f",
          "bytes": 4001
        },
        {
          "path": "web-app/src/telas/Setores.tsx",
          "archive_path": "src/telas/Setores.tsx",
          "sha256": "94280910f7ba31bd964350fe513d3d492b7e56b4a09931c29b9d727c8a734472",
          "bytes": 3970
        },
        {
          "path": "web-app/src/telas/TrocarSenha.tsx",
          "archive_path": "src/telas/TrocarSenha.tsx",
          "sha256": "c9079fd57f8d28d61e313152f53dd85fbc48f74ea09a2bfbbdb88ed8a85df31f",
          "bytes": 1572
        },
        {
          "path": "web-app/src/telas/Typebot.tsx",
          "archive_path": "src/telas/Typebot.tsx",
          "sha256": "1088336e7ca1cfe29ff7a3dfdad66ec630d550f08387fc937cddb607fcc2ceee",
          "bytes": 4342
        },
        {
          "path": "web-app/src/telas/Usuarios.tsx",
          "archive_path": "src/telas/Usuarios.tsx",
          "sha256": "3fc7c7a17004e17b9788c0d9f89083aa954893a60ab57827e6dd55a1bf882b18",
          "bytes": 8335
        },
        {
          "path": "web-app/src/telas/Wizard.tsx",
          "archive_path": "src/telas/Wizard.tsx",
          "sha256": "edbd2bb875874eb4bbd5dccdfc7a50e297e070ca9b16eeead771a1853327d2d1",
          "bytes": 8319
        },
        {
          "path": "web-app/src/tempoReal.spec.ts",
          "archive_path": "src/tempoReal.spec.ts",
          "sha256": "378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5",
          "bytes": 3349
        },
        {
          "path": "web-app/src/tempoReal.ts",
          "archive_path": "src/tempoReal.ts",
          "sha256": "118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf",
          "bytes": 2512
        },
        {
          "path": "web-app/src/timeline.test.ts",
          "archive_path": "src/timeline.test.ts",
          "sha256": "16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4",
          "bytes": 959
        },
        {
          "path": "web-app/src/timeline.ts",
          "archive_path": "src/timeline.ts",
          "sha256": "0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311",
          "bytes": 604
        },
        {
          "path": "web-app/src/vite-env.d.ts",
          "archive_path": "src/vite-env.d.ts",
          "sha256": "6436117a885784b650c7d4fa2e8701fac64f15196680a65ad4072973063c9b8f",
          "bytes": 261
        },
        {
          "path": "web-app/tsconfig.json",
          "archive_path": "tsconfig.json",
          "sha256": "d36535ca0c646e7ed37314db1f0ee01ed900d2ac45bb21af936e0294d0625200",
          "bytes": 355
        },
        {
          "path": "web-app/vite.config.ts",
          "archive_path": "vite.config.ts",
          "sha256": "8b61a846e95c7fe77c938a2ebced24b48bbba45c42efcd25c8191491655e74b2",
          "bytes": 1865
        }
      ],
      "status": "Prepared positive-only archive; no image build or actual runtime use."
    }
  ],
  "policy": "Exact positive public source roots and individually admitted public config files; symlinks rejected. Generated tar archives only, no writable checkout, no whole-repository context, env/private/process inspection or mutation. Source specs are build inputs but canonical tsconfig excludes spec compilation.",
  "execution": "Canonical ALL is still running. No image build, runtime, actual env/private data/process inspection or delivery claim. Source specs are build inputs but runtime compilation excludes tests. Recheck complete input manifest before builds and actual candidate activation."
}

```

### pcv-eps-e54-v1.1.json

```json
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "todo_id": "ST-CON-04",
  "run_id": "E54-canonical-all-2734",
  "environment_id": "owned-disposable-node22-postgresql16-real-BFF-fake-external-provider",
  "executor_id": "stcon04_continuation",
  "reviewer_id": "root-independent-source-and-output-collector; formal lane assessment pending",
  "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
  "lane_id": "EPS",
  "evidence_type": "explain-and-query-log",
  "sample_profile_id": "EPS-SP-STRONG",
  "acceptance_rule_id": "EPS-A2",
  "result_summary": "Disposable PostgreSQL EXPLAIN and bounded projection counts satisfy the declared page/query shape; no N+1 credential/provider probe.",
  "artifact_payload": {
    "evidence_receipt": "all-result-e54-v1.1.json",
    "stdout_sha256": "f6c6049a3e31cbe33d62c9d3376d4bf7d476fd552dac1c9232c2a94f36882a5f",
    "source_seal": "all-source-seal-e54-v1.1.json",
    "source_fingerprint": "604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c",
    "terminal_exit_code": 0,
    "assessment_status": "Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.",
    "access_pattern_classification": "Scoped exact open/intent/admission lookups and batched indexed page projection of current-resource trusted IN timestamps. Empty-conversation ordering uses additive expression index.",
    "touched_path_audit_summary": {
      "list_order_fixture_conversations": 15000,
      "list_returned_rows": 50,
      "out_heavy_fixture_conversations": 60,
      "out_heavy_returned_rows": 50,
      "conversation_query_count": 3,
      "standalone_message_hydration_query_count": 0,
      "counts_limit": "Three queries touching conversations, not total SQL count.",
      "trusted_window_fixture_conversations": 30,
      "history_rows_per_conversation": 24,
      "current_resource_batch_counts": {
        "buChannelFindMany": 1,
        "channelCredentialFindMany": 1,
        "latestAnyMessageProjection": 1,
        "latestInboundWindowProjection": 1
      },
      "provider_probe_count": 0
    },
    "strong_query_evidence_type": "EXPLAIN ANALYZE BUFFERS plus Prisma query-event counts",
    "inbox_order": {
      "rowCount": 50,
      "plan": "Limit  (cost=0.41..9.23 rows=50 width=45) (actual time=0.015..0.030 rows=50 loops=1)\n  Buffers: shared hit=6\n  ->  Index Scan using conversations_inbox_order_idx on conversations  (cost=0.41..2645.78 rows=15000 width=45) (actual time=0.014..0.026 rows=50 loops=1)\n        Index Cond: ((bu_id = '2d5ef223-1ad0-4812-b634-24014bce4b6f'::text) AND (contact_type = 'PESSOA'::\"ContactType\"))\n        Filter: (status = 'QUEUED'::\"ConversationStatus\")\n        Buffers: shared hit=6\nPlanning:\n  Buffers: shared hit=71\nPlanning Time: 0.207 ms\nExecution Time: 0.043 ms"
    },
    "trusted_window": {
      "policy_schema_version": "pcv-1",
      "lane_id": "EPS",
      "trigger_result": "required",
      "trigger_severity": "medium",
      "trigger_reason_code": "EPS-DATA-PATH-CHANGED",
      "gate_deadline": "before_local_implemented",
      "min_evidence_rule_id": "EPS-E2",
      "acceptance_rule_id": "EPS-A2",
      "sample_profile": "EPS-SP-STRONG",
      "access_pattern_classification": "Public conversation page loads selected BU channels once, official credential metadata once, one bounded latest-any-message projection for returned page IDs, and one batched indexed selected-resource trusted Meta IN timestamp query when selected bindings require a window; no provider credentials are decrypted or probed.",
      "pageConversations": 30,
      "historyRowsPerConversation": 24,
      "availabilitySample": [
        {
          "available": true,
          "reason": null,
          "windowOpen": true
        },
        {
          "available": true,
          "reason": null,
          "windowOpen": true
        },
        {
          "available": true,
          "reason": null,
          "windowOpen": true
        }
      ],
      "queryCounts": {
        "buChannelFindMany": 1,
        "channelCredentialFindMany": 1,
        "latestAnyMessageProjection": 1,
        "latestInboundWindowProjection": 1
      },
      "elapsedMs": 14.70497800000021,
      "explainLatestInboundProjection": [
        {
          "Plan": {
            "Node Type": "Nested Loop",
            "Parallel Aware": false,
            "Async Capable": false,
            "Join Type": "Inner",
            "Startup Cost": 0.28,
            "Total Cost": 96.31,
            "Plan Rows": 30,
            "Plan Width": 40,
            "Actual Startup Time": 0.024,
            "Actual Total Time": 0.19,
            "Actual Rows": 30,
            "Actual Loops": 1,
            "Inner Unique": false,
            "Shared Hit Blocks": 90,
            "Shared Read Blocks": 0,
            "Shared Dirtied Blocks": 0,
            "Shared Written Blocks": 0,
            "Local Hit Blocks": 0,
            "Local Read Blocks": 0,
            "Local Dirtied Blocks": 0,
            "Local Written Blocks": 0,
            "Temp Read Blocks": 0,
            "Temp Written Blocks": 0,
            "Plans": [
              {
                "Node Type": "Function Scan",
                "Parent Relationship": "Outer",
                "Parallel Aware": false,
                "Async Capable": false,
                "Function Name": "unnest",
                "Alias": "requested",
                "Startup Cost": 0,
                "Total Cost": 0.3,
                "Plan Rows": 30,
                "Plan Width": 32,
                "Actual Startup Time": 0.004,
                "Actual Total Time": 0.005,
                "Actual Rows": 30,
                "Actual Loops": 1,
                "Shared Hit Blocks": 0,
                "Shared Read Blocks": 0,
                "Shared Dirtied Blocks": 0,
                "Shared Written Blocks": 0,
                "Local Hit Blocks": 0,
                "Local Read Blocks": 0,
                "Local Dirtied Blocks": 0,
                "Local Written Blocks": 0,
                "Temp Read Blocks": 0,
                "Temp Written Blocks": 0
              },
              {
                "Node Type": "Limit",
                "Parent Relationship": "Inner",
                "Parallel Aware": false,
                "Async Capable": false,
                "Startup Cost": 0.28,
                "Total Cost": 3.18,
                "Plan Rows": 1,
                "Plan Width": 45,
                "Actual Startup Time": 0.006,
                "Actual Total Time": 0.006,
                "Actual Rows": 1,
                "Actual Loops": 30,
                "Shared Hit Blocks": 90,
                "Shared Read Blocks": 0,
                "Shared Dirtied Blocks": 0,
                "Shared Written Blocks": 0,
                "Local Hit Blocks": 0,
                "Local Read Blocks": 0,
                "Local Dirtied Blocks": 0,
                "Local Written Blocks": 0,
                "Temp Read Blocks": 0,
                "Temp Written Blocks": 0,
                "Plans": [
                  {
                    "Node Type": "Index Only Scan",
                    "Parent Relationship": "Outer",
                    "Parallel Aware": false,
                    "Async Capable": false,
                    "Scan Direction": "Backward",
                    "Index Name": "messages_conversation_trusted_window_idx",
                    "Relation Name": "messages",
                    "Alias": "message",
                    "Startup Cost": 0.28,
                    "Total Cost": 72.85,
                    "Plan Rows": 25,
                    "Plan Width": 45,
                    "Actual Startup Time": 0.006,
                    "Actual Total Time": 0.006,
                    "Actual Rows": 1,
                    "Actual Loops": 30,
                    "Index Cond": "((conversation_id = requested.conversation_id) AND (provider_resource_identity_id = '399453c9-f007-4ae2-b81c-14a4e8a9fa2c'::text) AND (direction = 'IN'::\"MessageDirection\") AND (channel_origin = 'OFICIAL'::\"ChannelType\") AND (official_inbound_at IS NOT NULL) AND (official_inbound_at <= CURRENT_TIMESTAMP))",
                    "Rows Removed by Index Recheck": 0,
                    "Heap Fetches": 30,
                    "Shared Hit Blocks": 90,
                    "Shared Read Blocks": 0,
                    "Shared Dirtied Blocks": 0,
                    "Shared Written Blocks": 0,
                    "Local Hit Blocks": 0,
                    "Local Read Blocks": 0,
                    "Local Dirtied Blocks": 0,
                    "Local Written Blocks": 0,
                    "Temp Read Blocks": 0,
                    "Temp Written Blocks": 0
                  }
                ]
              }
            ]
          },
          "Planning": {
            "Shared Hit Blocks": 68,
            "Shared Read Blocks": 0,
            "Shared Dirtied Blocks": 0,
            "Shared Written Blocks": 0,
            "Local Hit Blocks": 0,
            "Local Read Blocks": 0,
            "Local Dirtied Blocks": 0,
            "Local Written Blocks": 0,
            "Temp Read Blocks": 0,
            "Temp Written Blocks": 0
          },
          "Planning Time": 0.216,
          "Triggers": [],
          "Execution Time": 0.203
        }
      ],
      "providerCallsBefore": {
        "meta": 0,
        "evolution": 0
      },
      "providerCallsAfter": {
        "meta": 0,
        "evolution": 0
      },
      "limits": "Disposable PostgreSQL and one bounded 30-conversation public page; local query count/plan observation, not a capacity or latency SLO claim."
    },
    "sources": [
      {
        "path": "api-app/test/conversation-start.e2e-spec.ts",
        "sha256": "35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"
      },
      {
        "path": "api-app/test/number-onboarding-pcv.e2e-spec.ts",
        "sha256": "3825b0286f9906781e83666616caa05417647ee47c022763fc76e39a3c4ddca0"
      }
    ],
    "bounded_existence_query": "New actual query-event regression asserts findFirst bounded existence instead of whole-history COUNT; no new path-specific EXPLAIN claim.",
    "historical_plan_samples": "Existing exact EXPLAIN samples below are from E45; unchanged plan-test source executed again E54. They are historical samples, not relabeled current measured costs."
  },
  "artifact_sha256": "08138da3019c4a4269e82701d38732f84fcd7ae0476c37127e84257b7c868ab5"
}

```

### pcv-frc-e54-v1.1.json

```json
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "todo_id": "ST-CON-04",
  "run_id": "E54-canonical-all-2734",
  "environment_id": "owned-disposable-node22-postgresql16-real-BFF-fake-external-provider",
  "executor_id": "stcon04_continuation",
  "reviewer_id": "root-independent-source-and-output-collector; formal lane assessment pending",
  "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
  "lane_id": "FRC",
  "evidence_type": "deterministic-real-browser-real-BFF-post-readback",
  "sample_profile_id": "FRC-SP-H",
  "acceptance_rule_id": "FRC-A1",
  "result_summary": "Five independent first-send flows each receive20 synchronous open/confirm triggers; assertions require1open/1initialPOST/1provider invocation/1persistedOUT per flow.",
  "artifact_payload": {
    "evidence_receipt": "all-result-e54-v1.1.json",
    "stdout_sha256": "f6c6049a3e31cbe33d62c9d3376d4bf7d476fd552dac1c9232c2a94f36882a5f",
    "source_seal": "all-source-seal-e54-v1.1.json",
    "source_fingerprint": "604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c",
    "terminal_exit_code": 0,
    "assessment_status": "Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.",
    "concurrency_policy": "drop duplicate",
    "burst_profile_observed": {
      "bursts": 5,
      "triggers_per_burst": 20,
      "open_requests_per_burst": 1,
      "initial_posts_per_burst": 1,
      "provider_invocations_per_burst": 1,
      "persisted_out_per_burst": 1,
      "observation_type": "Exact loop/assertions in current E54 test passed; not separately emitted metric trace."
    },
    "runner_or_manual_path": "bash scripts/test-channels-local.sh all -> Playwright start-conversation.spec.ts: cinco envios recebem vinte gatilhos síncronos cada sem duplicar o POST",
    "additional_race_coverage": "Current E54 includes A-B-A, storage refusal, same-key replay, actual90s ordinary recovery, valid PREPARED and EALB successor/late-old UI proof.",
    "sources": [
      {
        "path": "web-app/e2e/start-conversation.spec.ts",
        "sha256": "16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"
      }
    ],
    "limits": "Route delays a real BFF response after actual route.fetch(); external provider fake. No real WhatsApp/SLO claim.",
    "per_action_policy": [
      {
        "action": "Manual open and initial confirmation",
        "policy": "drop duplicate",
        "proof": "Synchronous latches; five20-trigger browser waves with real BFF and one provider invocation/Message per flow."
      },
      {
        "action": "Preview/channel/BU/draft-dependent options and completion",
        "policy": "last-write-wins",
        "scope": "Only matching mounted owner/generation/conversation/draft; an older same-text A→B→A result cannot update newer ownership.",
        "proof": "Delayed preview, context switches and late-body/completion browser cases passed E45."
      },
      {
        "action": "Initial read/reconcile/acknowledge",
        "policy": "drop duplicate",
        "scope": "Busy latch plus mounted owner/generation; explicit actions and immutable key/deadline.",
        "proof": "Initial uncertainty/read and known-receipt local-reconcile browser cases passed E45; no provider operation."
      },
      {
        "action": "Ordinary recovery reconcile/acknowledge",
        "policy": "drop duplicate",
        "scope": "Same local action latch/owner fence; checkbox and immutable deadline required.",
        "proof": "Dedicated actual E54 real BFF/browser case passed through actual90s risk acknowledgment and composer return."
      },
      {
        "action": "Saved snapshot reread",
        "policy": "serialize",
        "scope": "Explicit synchronous local storage read only; failed read blocks writes and preserves original key/body.",
        "proof": "Causal E44 read-loss RED then E45 actual failed/successful local reread and same-key replay PASS."
      }
    ]
  },
  "artifact_sha256": "994c5487144cd1be2301b4099b0c7d05af4f88aa5955b9441e5b9910736f0e4a"
}

```

### pcv-bci-e54-v1.1.json

```json
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "todo_id": "ST-CON-04",
  "run_id": "E54-canonical-all-2734",
  "environment_id": "owned-disposable-node22-postgresql16-real-BFF-fake-external-provider",
  "executor_id": "stcon04_continuation",
  "reviewer_id": "root-independent-source-and-output-collector; formal lane assessment pending",
  "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
  "lane_id": "BCI",
  "evidence_type": "real-concurrent-BFF-PG-barrier-and-state-readback",
  "sample_profile_id": "BCI-SP-H",
  "acceptance_rule_id": "BCI-A1",
  "result_summary": "Five20-request same-key waves each persist one intent and one Message, dispatch once and return19 in-flight replays; manual open five20-request waves create five rows and send zero messages.",
  "artifact_payload": {
    "evidence_receipt": "all-result-e54-v1.1.json",
    "stdout_sha256": "f6c6049a3e31cbe33d62c9d3376d4bf7d476fd552dac1c9232c2a94f36882a5f",
    "source_seal": "all-source-seal-e54-v1.1.json",
    "source_fingerprint": "604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c",
    "terminal_exit_code": 0,
    "assessment_status": "Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.",
    "invariant_id": "ST04-one-owned-active-slot-and-at-most-one-POST-per-immutable-initial-intent",
    "concurrency_policy": "idempotent same-key replay",
    "probe_profile_observed": {
      "waves": 5,
      "overlapping_requests_per_wave": 20,
      "same_key_initial_waves": [
        {
          "wave": 1,
          "requests": 20,
          "replay202": 19,
          "posts": 1,
          "messages": 1,
          "elapsedMs": 169
        },
        {
          "wave": 2,
          "requests": 20,
          "replay202": 19,
          "posts": 1,
          "messages": 1,
          "elapsedMs": 142
        },
        {
          "wave": 3,
          "requests": 20,
          "replay202": 19,
          "posts": 1,
          "messages": 1,
          "elapsedMs": 135
        },
        {
          "wave": 4,
          "requests": 20,
          "replay202": 19,
          "posts": 1,
          "messages": 1,
          "elapsedMs": 132
        },
        {
          "wave": 5,
          "requests": 20,
          "replay202": 19,
          "posts": 1,
          "messages": 1,
          "elapsedMs": 125
        }
      ],
      "manual_open": {
        "waves": 5,
        "requests_per_wave": 20,
        "created": 5,
        "reused": 95,
        "distinct_conversations": 5,
        "provider_call_delta": 0,
        "message_count": 0
      }
    },
    "additional_barriers": "Ordinary-vs-initial admission, unique echo race, CAS owner/closed preservation, commit ACK loss versus rollback and after-deadline local risk acknowledgment passed actual PG suites. E54 also proves settlement rollback after provider ACK, EALB early/late acknowledgment and late-old isolation.",
    "sources": [
      {
        "path": "api-app/test/initial-message.e2e-spec.ts",
        "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
      },
      {
        "path": "api-app/test/conversation-start.e2e-spec.ts",
        "sha256": "35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"
      },
      {
        "path": "api-app/test/dispatch-admission.e2e-spec.ts",
        "sha256": "ec1975b985ea766dcc9b8136bb6d1288cf71f4a40bde34bb23cfbc19f7669d47"
      }
    ],
    "limits": "posts in ST04_BCI_5x20 are Evolution fake-port invocations, not external TCP requests. Durable external exactly-once is not claimed."
  },
  "artifact_sha256": "c505c53965ac7a15999d0f91915e75dac1fac6e9c3a0fca6694a3078f54aa5f2"
}

```

### pcv-rls-e54-v1.1.json

```json
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "todo_id": "ST-CON-04",
  "run_id": "E54-canonical-all-2734",
  "environment_id": "owned-disposable-node22-postgresql16-real-BFF-fake-external-provider",
  "executor_id": "stcon04_continuation",
  "reviewer_id": "root-independent-source-and-output-collector; formal lane assessment pending",
  "recorded_at_utc": "2026-10-23T00:47:04.414607+00:00",
  "lane_id": "RLS",
  "evidence_type": "bounded-disposable-one-stage-concurrent-load",
  "sample_profile_id": "RLS-SP-L",
  "acceptance_rule_id": "RLS-A1",
  "result_summary": "Declared bounded stage of20 overlapping initial requests repeated five times stays below15000ms per wave; not a production capacity/SLO measurement.",
  "artifact_payload": {
    "evidence_receipt": "all-result-e54-v1.1.json",
    "stdout_sha256": "f6c6049a3e31cbe33d62c9d3376d4bf7d476fd552dac1c9232c2a94f36882a5f",
    "source_seal": "all-source-seal-e54-v1.1.json",
    "source_fingerprint": "604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c",
    "terminal_exit_code": 0,
    "assessment_status": "Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.",
    "stage_profile_observed": {
      "stages": 1,
      "concurrency": 20,
      "waves": 5,
      "request_count": 100,
      "request_type": "same-key BFF initial sends with held first provider operation"
    },
    "thresholds": {
      "wave_elapsed_ms_strictly_less_than": 15000,
      "definition_time": "Predeclared expect(durationMs).toBeLessThan(15_000), present in frozen source before E45 runner."
    },
    "metrics_summary": {
      "elapsed_ms": [
        169,
        142,
        135,
        132,
        125
      ],
      "max_elapsed_ms": 169,
      "all_five_below_threshold": true,
      "per_wave_provider_invocations": 1,
      "per_wave_persisted_OUT": 1
    },
    "sources": [
      {
        "path": "api-app/test/initial-message.e2e-spec.ts",
        "sha256": "a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"
      }
    ],
    "limits": "Reuses explicitly bound BCI stage metrics as allowed by pcv-1; fake provider held by deterministic barrier. No throughput saturation, live provider latency or production SLO claim."
  },
  "artifact_sha256": "25f71eadd5ac094b794fbf1ffb694a49d3031791486f4cb473537d08698c7fb8"
}

```

### all-result-e54-v1.1.json

```json
{
  "checkpoint": "E54 corrected full canonical candidate GREEN",
  "recorded_at_utc": "2026-10-23T00:46:53.721503+00:00",
  "command": "bash scripts/test-channels-local.sh all",
  "executor_session_id": 2734,
  "exit_code": 0,
  "actual_exit_code": 0,
  "terminal_authority": "Actual session terminal tool exit0 collected by owning executor; root independently bound stdout/full inventory and browser attestation.",
  "phases": {
    "migrations": 28,
    "lint_and_build": "passed",
    "api_unit": {
      "files": 34,
      "tests": 364
    },
    "api_postgresql": {
      "files": 33,
      "tests": 439,
      "duration_seconds": 274.67
    },
    "web_unit": {
      "files": 7,
      "tests": 54
    },
    "browser": {
      "tests": 88,
      "passed": 88,
      "duration_minutes": 15.9
    }
  },
  "stdout_sha256": "f6c6049a3e31cbe33d62c9d3376d4bf7d476fd552dac1c9232c2a94f36882a5f",
  "source_recheck": "all-source-recheck-e54-v1.1.json",
  "source_fingerprint": "604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c",
  "freshness": "browser-freshness-collection-e54-v1.1.json",
  "owned_cleanup_observed": true,
  "specific_proofs": [
    "Valid PREPARED service reservation -> read-only action -> actual BFF/UI local reconcile live202 then synthetic expiry local rejection, zero provider/Message",
    "EALB early UI/BFF409 then synthetic expiry ACK200 -> one successor -> late-original local recovery preserving current owner/slot",
    "Actual90s ordinary uncertainty risk acknowledgment -> composer return",
    "Unicode4096text and1024positional actual input/preview/send, named/positional snapshot exact code-point unit bounds",
    "Ordinary settlement actual rollback after known ACK produces local incomplete, bounded history existence query and confirmed winner-only realtime",
    "Same-key5x20 and browser20-trigger5waves, signed trusted-window/current-resource, shared BFF/PUBLIC/BOT transport regressions"
  ],
  "limits": [
    "Disposable synthetic DB and owned fake provider, not actual WhatsApp delivery",
    "EALB/PREPARED fixture deadline arrangement is not actual90s elapsed claim",
    "R1 fixes have regression proof; fresh independent review still required",
    "No preserved runtime activation, module consolidation, full canonical diff guard or delivery claim"
  ]
}

```

### all-source-recheck-e54-v1.1.json

```json
{
  "checkpoint": "E54 terminal full positive source recheck",
  "stage": "After actual executor terminal and owned cleanup; BEFORE writer release",
  "count": 259,
  "fingerprint": "604a6867f1d715ffac564e6a47c68539e0b07a657b046145542d42620cbbbe0c",
  "matches_preseal_full_inventory_and_bytes": true,
  "record_reference": "all-source-seal-e54-v1.1.json#records",
  "stdout_sha256": "f6c6049a3e31cbe33d62c9d3376d4bf7d476fd552dac1c9232c2a94f36882a5f",
  "executor_reported_exit_code": 0,
  "recorded_at_utc": "2026-10-23T00:46:32.920900+00:00",
  "boundary": "Only declared positive public roots and7 exact publicfiles; no actual env/data/process inspection."
}

```

### browser-freshness-collection-e54-v1.1.json

```json
{
  "kind": "Independent owned browser attestation collection",
  "checkpoint": "E54",
  "source_seal": "all-source-seal-e54-v1.1.json",
  "attestation_sha256": "c8b7361644564618e26af9872395a97aa954117cf67a846995e635775504b6fb",
  "run_id": "2026-10-23T00-29-13-003Z",
  "captured_at_utc": "2026-10-23T00:29:13.004Z",
  "runtime": "v22.23.3",
  "completed_migrations": 28,
  "current_api_head": "db5a86758a165fac8a1ab587599c37b17890530c",
  "current_web_head": "74b9d4b714044829796f875d00553f077c1c329d",
  "served_dist_bundle_equal": true,
  "served_bundle_sha256": "05af33d08741c946111a078f58de739340bbf0fbf4e4e945679b355c51e4cfd7",
  "manifest_count": 93,
  "all_manifest_records_match_presealed_sources": true,
  "manifest_checks": [
    {
      "path": "api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql",
      "matches": true
    },
    {
      "path": "api-app/prisma/schema.prisma",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/transport/channel-initial-message.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/channels/transport/channel.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/historico/catalogo.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/historico/cobertura.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/channel-window-policy.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/channel-window-policy.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/conversation-start.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/conversation-start.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/conversations.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/dispatch-admission.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/incoming.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/incoming.typebot.integration.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message-template-renderer.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message-template-renderer.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/initial-message.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/message-acceptance.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/message-acceptance.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-definition.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-definition.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-draft.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.dependencies.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.ports.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.ports.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-observation.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-submission.service.ts",
      "matches": true
    },
    {
      "path": "api-app/src/domain/message-templates/template-transaction-boundary.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/account-reference.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-factory.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-registry.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/channel-transport.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/evolution-channel.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/meta-channel.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/channels/prisma-channel-resolver.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/message-templates/template-management.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/message-templates/template-management.resolver.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/initial-message.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/initial-message.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/message-template.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/message-template.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.spec.ts",
      "matches": true
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/bff/bff.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/bff/conversations.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/bff/message-templates.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/public/conversations.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/public/public.module.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/webhooks/meta.controller.ts",
      "matches": true
    },
    {
      "path": "api-app/src/surfaces/webhooks/webhooks.module.ts",
      "matches": true
    },
    {
      "path": "api-app/test/api-publica.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/atendimento.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/browser-server.cjs",
      "matches": true
    },
    {
      "path": "api-app/test/channel-transport.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/conversation-start.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/dispatch-admission.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/helpers.ts",
      "matches": true
    },
    {
      "path": "api-app/test/initial-message.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/message-template-bff.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/message-template-drafts.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/message-template-management.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/number-onboarding-bci.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/number-onboarding-pcv.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/number-onboarding-typebot.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "api-app/test/timeline-fixtures.cjs",
      "matches": true
    },
    {
      "path": "api-app/test/webhooks.e2e-spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/channel-transport.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/message-templates.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/number-onboarding-freshness.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/start-conversation.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/e2e/timeline-freshness.ts",
      "matches": true
    },
    {
      "path": "web-app/src/api.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/src/api.ts",
      "matches": true
    },
    {
      "path": "web-app/src/App.tsx",
      "matches": true
    },
    {
      "path": "web-app/src/componentes/NovaConversa.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/src/componentes/NovaConversa.tsx",
      "matches": true
    },
    {
      "path": "web-app/src/telas/Inbox.tsx",
      "matches": true
    },
    {
      "path": "web-app/src/telas/Modelos.spec.ts",
      "matches": true
    },
    {
      "path": "web-app/src/telas/Modelos.tsx",
      "matches": true
    }
  ],
  "limits": "Disposable synthetic proof only; historical declaredBaseline fields do not replace current approved repository baselines. No actual preserved runtime/provider activation proof."
}

```

## Proposed module consolidation (not applied)

# ST-CON-04 module consolidation proposal

Proposal for review, not canonical module edits or delivery proof. Preserve completed ST05/ST06 execution history and their evidence. Their text-only/window rules remain historical baselines; two explicitly approved ST04 supersedes define the new current contract when implemented and validated.

Planned edits are limited to `modules/inbox-and-conversations.md` and `modules/integrations-and-channels.md`. Replace stale forward-looking statements that ST04 has no approval/implementation with a stage-correct reference to the governing active TODO; never claim the required preserved-runtime operator proof before it occurs.

Inbox gains a stable section describing manual open/reuse without send/read/claim/automation, truthful empty state, explicit channel and read-only preview, durable first-send key/request/slot and same-owner Message acceptance, CAS preservation of concurrent claim/close, known external receipt versus local completion, and local-only reconciliation/risk release after the immutable deadline. Document recovery of the original browser snapshot after storage failure without automatic POST. Ordinary diagnostic null-ID failed Messages remain their inherited behavior; the new first-send path never fabricates a sent Message without external ID.

Integrations gains a stable section extending the one abstract sendMessage operation to text/approved-template with supportedKinds and typed zero-HTTP refusal. Management stays create/list/query only; no send method is added to it. Concrete Meta/Evolution adapters own protocol and registration. The initial coordinator composes narrow transport/management dependencies without reverse module imports or provider branches in consumers.

Both modules state that only qualified signed Meta IN timestamps for the currently selected managed resource open the strict24-hour free-text window; no createdAt/import/nonofficial fallback. Keep the historical timestamp/timeline and former ST06 index semantics as delivered history, and document the additive current-resource index/batched projections.

The initial Meta path reuses the catalog observation but verifies the fresh same-account APPROVED textual asset in at most2filtered pages50 each before claim; pin the captured messaging account and international recipient. Bound6GET/1POST,10s per operation75s overall against90s immutable deadline. Preserve no fallback/retry/network in DB transactions and no external exactly-once claim.

Historical ST05 D09 records the original text-only boundary; append an explicit ST04 supersede link for the transport payload only. Do not rewrite D09 as if management originally sent recipient messages. Ordinary BFF/public/BOT callers remain on the common sender and honor initial-slot exclusion, with no global idempotency/outbox conversion.

One-to-one D01–D10 source/test/target mapping is in `evidence/decision-module-candidate-map-e54-v1.1.json`. Apply only after independent implementation findings are resolved; record exact module diff, baseline hash, stable anchors and final decision consistency before completion. Runtime proof and full guard remain separate gates.


The current stable contract must explicitly include PREPARED local reconciliation as an action while keeping GET observational; live lease retains its slot and expiry permits only local rejection/release. Ordinary sends distinguish an empty conversation from an active initial slot, return scoped safe identifiers, and preserve known provider acceptance when durable settlement is unconfirmed. Local Message creation publishes a best-effort event only for its confirmed commit winner; echoes/replays and uncertain readback do not invent publication ownership. Text and template parameter limits use Unicode code points with a separate bounded JSON envelope. These points implement the existing approved decisions; they introduce no new states, providers, retries or migration. Current source/test references are bound by the full E54 candidate; independent r2 and actual delivery gates remain.


## Current-stage status

The current full canonical ALL run is actually terminal exit0 with full positive source postseal and served-browser binding. Historical E45/E47 and RED receipts explain chronology, not substitute current execution. Judge current candidate and r1 resolutions afresh. No preserved-runtime activation or completed delivery is inferred.
