# TODO — LeadsHug Instagram Direct por Channel

## Title
ST-IG-03 — Conectar Instagram e atender DMs na mesma BU dos WhatsApps

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`
- **Artifact status:** In-Progress
- **Contract version:** 1.3 — APROVADO em2026-10-23; implementação governada, sem ativação real autorizada.
- **Template:** copiado de `delphi-ai/templates/todo_template.md` em2026-10-23; seções aplicáveis preenchidas abaixo.

## Context
O usuário priorizou Instagram antes de histórico, confirmou conta profissional para teste e acesso para autorizá-la, confirmou a configuração com login do Instagram no app Meta existente e escolheu reunir os canais na mesma BU. A BU operacional, contatos qualificados, ownership empresarial e rota foram ratificados pelo APROVADO v1.3 e consolidados como arquitetura alvo. A implementação e suas provas continuam em curso. ST-CON-01/04/05/06 são baseline local entregue, não código que este TODO possa substituir silenciosamente. Preservar dados e recuperar envios pendentes exige mais que acrescentar INSTAGRAM ao enum.

## Framing Source & Story Slice
- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-instagram-channel-20261023.md`
- **Primary story ID:** ST-IG-03; dependências subordinadas ST-IG-01/02.
- **Why this is the right current slice:** uma entrega funcional coesa: autorizar uma conta, receber uma DM e responder texto pelo Atendimento usando Channel. Identidade e conexão são pré-requisitos dessa mesma prova; checkpoints não declaram entregas parciais suficientes.
- **Direct-to-TODO rationale:** n/a; há brief, decisão de BU e desenho revisado.
- **Design evidence:** `foundation_documentation/artifacts/analysis/leadshug-multichannel-identity-definition-20261023.md`.

## Contract Boundary
Este TODO define WHAT, exclusões e critérios de entrega. A baseline v1.3 abaixo foi revisada e aprovada explicitamente em2026-10-23. “Pode fazer” em2026-10-23 autorizou preparar o TODO/revisão, não código, banco, credenciais, runtime ou Meta. A execução está limitada à versão revisada e aprovada, com authority guard go registrado. Qualquer alteração material de escopo, decisões, validação, rota pública ou padrões de diff exige reconvergência e nova aprovação; descobertas locais que preservam o objetivo podem ser concretizadas dentro dele.

## Implementation Intent
- **Current delivery:** DM individual textual Instagram, iniciada pelo usuário externo; conexão explícita na BU; resposta humana pelo mesmo recurso; evolução necessária de identidade e roteamento com regressão WhatsApp.
- **Planned next steps:** mídia, importação histórica, CRM, merge de contatos, automação Instagram e outros canais; informacionais.
- **Anticipatory implementation authorized now:** none; nem código desta fatia antes de APROVADO.
- **Rationale:** identidade/ownership/rota são usados pelo percurso atual. Não criar framework de plugins, catálogo universal de capacidades ou operação futura sem uso.

## Delivery Status Canon (Required)
- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** congelar candidata29 com syntax28 reconciliado e executar UMA validação canônica completa da API. API27 parou em lint no fechamento sintático do work.push;31migrações/generate/paridade passaram, build/unit/E2E não alcançados. Nenhuma nova prova funcional desde API22.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** implementation
- **Why this state now:** a API22 passou build/406unit e alcançou569casos de integração;39falhas exigiram separar fixture/oracle, perda real do endereçoIG no aceite e medidas de tempo/batch. As correções24/25 e o lote26 estão aplicados e reconciliados estaticamente;256fontes públicas e35preservações conferidas. Os testes do scheduler têm barreiras e limpeza; nenhuma alteração24..26 foi validada por uma execução posterior ainda.
- **Exit condition:** todos os checkpoints e critérios validados, revisões/guards completos e prova runtime posterior explicitamente aprovada; nenhum fechamento parcial implícito.

## Blocker Notes
- **Blocker:** none for remaining admitted code/disposable synthetic validation. Exact OAuth-session v2 source is applied; API22 proved callback confidentiality assertions but two infrastructure cases stopped at an incorrect ordinary500 expectation (native baseline503); corrected tests24 and browser/gateway proof remain unvalidated. Privacy HTML and outbound UTF-8 proposals await explicit human validation; primary own-subscription observation remains unresolved, no gate waiver.
- **Last confirmed truth:** API22 passed31migrations/lint/build/406unit;530/569E2E passed and39 failed across11files. Root matched254sources/T/258inputs/35preservations/3index/log.33fixture cases,2ordinaryfault oracle cases,1IGpost-ACK localacceptance defect,2clock-budget misses and1batchtimeout are qualified separately; no completeGREEN. Strict<2000final-clock assertion passed within its case. Current24..26 changes require freshproof.
- **Runtime boundary:** ativação real, leitura privada, Meta e prova física dependem do plano posterior; nenhuma autorização herdada é reutilizada.

## Scope
- [x] SCOPE-01 Consolidar, após aprovação, as propostas DEC-qualified-contact-conversation, DEC-business-resource-provider-identity e DEC-explicit-channel-routing nos owners canônicos, distinguindo arquitetura e entrega.
- [ ] SCOPE-02 Estabelecer contato local e identidade externa qualificada, recursos empresariais e rotas imutáveis; no máximo um recurso empresarial WhatsApp durável por BU (oficial+Evolution no mesmo número comprovado) e múltiplas contas Instagram; preservar IDs de BU/conversa/mensagem e identidades técnicas existentes.
- [ ] SCOPE-03 Migrar consumidores de telefone/tipo para identidade/rota; BFF multicanal, API pública, Typebot e Consultar (lista/drilldown/CSV) preservados no subconjunto WhatsApp, sem Instagram acidental.
- [ ] SCOPE-04 Conexão Instagram Login no app existente com configuração própria do produto, tentativas por ator/sessão/BU, autorização server-side, armazenamento cifrado, reautorização e desconexão locais explícitas.
- [ ] SCOPE-05 Ingresso Instagram autenticado, normalização textual, deduplicação transacional e estado honesto de recebimento; nenhum sucesso inferido de OAuth/challenge sintético.
- [ ] SCOPE-06 Implementação Instagram registrada no Channel; política textual por recurso; envio pelo único OutboundService e aceitação comuns, sem fallback e sem retry externo ambíguo.
- [ ] SCOPE-07 Cadastro de conexões e Atendimento React com origem/conta/contato legíveis, compositor vinculado à rota e proteção contra resposta atrasada/troca de BU.
- [ ] SCOPE-08 Testes comuns e específicos, PostgreSQL, navegador real-backend/freshness, concorrência, isolamento, cutover, provas físicas e fechamento local com todos os gates.

## Out of Scope
- [ ] Posts/reels, comentários, comentário→DM, prospecção por username, DM não solicitada, grupos Instagram, templates Instagram, mídia, campanhas e importação histórica.
- [ ] Merge de contatos/conversas entre plataformas, contatos globais, transferência de recurso entre BUs, CRM, novas automações Instagram ou ativação implícita de Typebot.
- [ ] Facebook/Messenger, Telegram, novo provedor WhatsApp, migração/desregistro de números, alterações de outros apps/partners/roteamento Meta e desvincular WhatsApp existente.
- [ ] Railway/produção, publicação/app review Meta, Git de produto/promoção, worktrees/checkouts/cópias auxiliares, branches worker/reconcile ou alterar gitlinks/.gitmodules.
- [ ] Ler/listar/hash de arquivos privados, `.env*` reais, bancos/conversas/logs/credenciais operacionais, argumentos/env de processos ou volumes. Testes usam somente inventário público e valores sintéticos. `.env.example` é configuração pública admitida. Runtime real e eventual exceção limitada do verificador de diff exigem plano posterior explícito; nenhuma autorização herdada de ST-CON-04 é reutilizada.

## Execution Lane Tracking (Required)
- **Local implementation branches:** principal checkout API/Web no estado existente; nenhum branch, worktree, commit/push de produto criado por este planejamento. Foundation:main, único checkout.
- **Promotion lane path:** n/a para entrega local; promoção futura separada, pelo mesmo TODO se admitida.
- **Lane-promoted threshold for this TODO:** n/a; Local-Implemented somente.
- **Production-ready threshold for this TODO:** fora desta aprovação.

## Diff Expectation Contract
- **Contract status:** required
- **Policy:** strict; unclassified or forbidden paths block delivery
- **User validation:** required on deviation
- **Comparison mode:** working_tree

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| root | . | 80e3940126f22a941f90dba4f5e801b6c0eb2f58 | working_tree |
| API | api-app | db5a86758a165fac8a1ab587599c37b17890530c | working_tree |
| Web | web-app | 74b9d4b714044829796f875d00553f077c1c329d | working_tree |
| Foundation | foundation_documentation | f191266a4ae06042c875ca1efb4454a6d0ec7d52 | working_tree |

Baselines Git não representam checkout limpo: `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/public-source-baseline.json` sela218arquivos API e54Web, inclusive entregas locais anteriores ainda não commitadas. Conteúdo pré-existente fora da fatia deve ser preservado por comparação de inventário/bytes; não reverter nem incluir como implementação Instagram. Contrato de diff e herança foram reconvergidos para review v1.1; não rodar varredura integral com arquivos privados neste planejamento.

### Expected Changed Paths
| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| root | scripts/test-channels-local.sh | M | safe runner/admissão de fontes e cenários Instagram |
| root | scripts/check-channels-ci-parity.py | A,M,?? | paridade explícita dos specs novos |
| root | .github/workflows/ci.yml | M | paridade de config/testes; sem promoção |
| root | docker-compose.channels.yml | M | somente validação/variáveis públicas sintéticas da capacidade nova |
| root | docker/local-gateway.conf.template | M | callback seguro, sem query/logs privados |
| root | .env.example | M | contrato público de configuração Instagram |
| root | api-app | M | projeção de submódulo, índice não pode ser alterado |
| root | web-app | M | projeção de submódulo, índice não pode ser alterado |
| root | foundation_documentation | M | projeção documental, índice preservado |
| API | prisma/schema.prisma | M | identidade, contato, rota e OAuth |
| API | prisma/migrations/*_instagram_*/migration.sql | A,?? | migração versionada delimitada, sem reset |
| API | src/domain/channels/** | A,M,?? | conexões, identidade empresarial, credenciais e contratos Channel |
| API | src/domain/inbox/** | A,M,?? | contato/rota, política, aceitação e recuperação |
| API | src/infra/http/body-parsers* | A,M,?? | raw bytes e limite específico do webhook, incluindo testes |
| API | src/infra/config/modulos* | A,M,?? | capacidade Instagram isolada e testes de configuração pública |
| API | src/domain/tenancy/tenancy.service.ts | M | BU operacional sem exigir telefone |
| API | src/domain/historico/catalogo.ts | M | eventos seguros, sem token/conteúdo DM |
| API | src/domain/historico/cobertura.ts | M | leituras justificadas |
| API | src/integrations/channels/** | A,M,?? | composição e resolver por vínculo/rota |
| API | src/integrations/instagram/** | A,?? | cliente/protocolo Instagram isolados |
| API | src/surfaces/bff/session.middleware.ts | M | Exact reviewed OAuth callback confidentiality v2 only; user admitted2026-10-24, original/candidate hashes in oauth-callback-session-user-admission-v2.json |
| API | src/surfaces/bff/me.controller.ts | M | Bound legacy BU connections projection to compatible WhatsApp max2; preserve grants and other controller behavior |
| API | src/surfaces/bff/bff.module.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/conversations.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/channels.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/number-registrations.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/instagram-authorizations.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/webhooks/** | A,M,?? | callback/OAuth/ingresso Instagram sem mudar semântica WhatsApp |
| API | src/surfaces/public/conversations.controller.ts | M | conservar API v1 WhatsApp pelo namespace correto |
| API | test/*instagram*.e2e-spec.ts | A,?? | OAuth/ingresso/isolation/routing/cutover reais |
| API | test/*multichannel*.e2e-spec.ts | A,?? | identidades, colisões e preservação |
| API | test/*onboarding*.e2e-spec.ts | M | fixtures/asserts com a nova identidade, sem perder cenários |
| API | test/initial-message.e2e-spec.ts | M | snapshots e recuperação de aceitos |
| API | test/channel-transport.e2e-spec.ts | M | substituição por Channel e rota |
| API | test/api-publica.e2e-spec.ts | M | API antiga não trata ID Instagram como telefone |
| API | test/atendimento.e2e-spec.ts | M | inbox/claim/readback |
| API | test/webhooks.e2e-spec.ts | M | autenticação, echo e dedup |
| API | test/historico.e2e-spec.ts | M | Canonical fixtures and qualified WhatsApp Consultar boundary assertions; preserve all existing scenarios/assertions |
| API | test/painel.e2e-spec.ts | M | Canonical fixture-only adaptation for mandatory contact identity; preserve all existing scenarios/assertions/counters |
| API | test/historico-atividades.e2e-spec.ts | M | Canonical fixture-only adaptation for mandatory contact identity; preserve all existing scenarios/assertions/counters |
| API | test/setores.e2e-spec.ts | M | Canonical fixture-only adaptation for mandatory contact identity; preserve all existing scenarios/assertions/counters |
| API | test/helpers.ts | M | seed determinístico por identidade |
| API | test/browser-server.cjs | M | backend real e fake de fronteira HTTP |
| API | test/timeline-fixtures.cjs | M | persistência/identidade sintéticas |
| API | .env.example | M | nomes de configuração sem segredos |
| Web | src/telas/Inbox.tsx | M | rota e identidade legíveis |
| Web | src/telas/Numeros.tsx | M | BU/conexões multicanal, preservando WhatsApp |
| Web | src/componentes/CadastroNumero.tsx | M | link de cadastro WhatsApp por conexão |
| Web | src/componentes/NovaConversa.tsx | M | texto/template WhatsApp e capacidades corretas |
| Web | src/componentes/*Instagram* | A,?? | conexão/callback/estado Instagram |
| Web | src/*instagram* | A,?? | estado puro e testes do fluxo |
| Web | src/api.ts | M | DTOs seguros e rota esperada |
| Web | src/api.spec.ts | M | contratos/erros seguros |
| Web | src/cadastroNumero* | M | lifecycle WhatsApp preservado |
| Web | src/componentes/NovaConversa.spec.ts | M | rascunho/fences/política |
| Web | e2e/instagram*.spec.ts | A,?? | jornada browser completa |
| Web | e2e/number-onboarding.spec.ts | M | não regredir cadastro |
| Web | e2e/channel-transport.spec.ts | M | substituição e rota |
| Web | e2e/start-conversation.spec.ts | M | primeiro envio existente |
| Web | e2e/message-templates.spec.ts | M | modelo WhatsApp não elegível Instagram |
| Web | e2e/*freshness.ts | M | inventário positivo e backend real |
| Foundation | todos/active/features/TODO-leadshug-instagram-channel.md | A,M,?? | contrato/evidências |
| Foundation | todos/completed/features/TODO-leadshug-instagram-channel.md | A,?? | apenas após conclusão |
| Foundation | artifacts/tmp/instagram-channel-planning/** | A,M,?? | preparação/reviews/guards públicos |
| Foundation | artifacts/reviews/leadshug-instagram-channel-20261023/** | A,M,?? | evidências delimitadas |
| Foundation | artifacts/feature-briefs/leadshug-instagram-channel-20261023.md | A,M,?? | enquadramento autorizado |
| Foundation | artifacts/analysis/leadshug-multichannel-identity-definition-20261023.md | A,M,?? | desenho autorizado |
| Foundation | decisions/leadshug-multichannel-identity-decisions.md | A,M,?? | proveniência/aceitação após aprovação |
| Foundation | decisions/README.md | M | índice singular |
| Foundation | domain_entities.md | M | identidade do contato aprovada |
| Foundation | project_constitution.md | M | consolidação estratégica já iniciada, sem claim de execução |
| Foundation | policies/scope_subscope_governance.md | M | BU operação/rotas governadas |
| Foundation | modules/identity-and-tenancy.md | M | contrato canônico do owner tocado |
| Foundation | modules/inbox-and-conversations.md | M | contrato canônico do owner tocado |
| Foundation | modules/integrations-and-channels.md | M | contrato canônico do owner tocado |
| Foundation | modules/audit-and-history.md | M | contrato canônico do owner tocado |
| Foundation | backlog/README.md | M | candidato/next gate |
| Foundation | system_roadmap.md | M | prioridade antes de histórico |
| Foundation | artifacts/dependency-readiness.md | M | readiness honesta |
| API | prisma/migrations/20261020170000_message_inbound_window_index/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261021130000_message_template_drafts/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261021150000_message_template_operations/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261022140000_initial_message_orchestration/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261022150000_initial_message_admissions/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-definition.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-definition.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-draft.service.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-management.dependencies.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-management.ports.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-management.ports.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-observation.service.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-submission.service.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-transaction-boundary.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/message-templates/template-management.module.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/message-templates/template-management.resolver.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/initial-message.client.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/initial-message.client.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/message-template.client.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/message-template.client.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/surfaces/bff/message-templates.controller.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | test/conversation-start.e2e-spec.ts | A,M,?? | Canonical fixture/qualified lookup/context adaptations only; preserve all scenarios/assertions/counters and deliberate v1 cutover cases; baseline hash retained, final freeze lifted per IG-CRIT-R1-01 |
| API | test/dispatch-admission.e2e-spec.ts | A,M,?? | Canonical fixture/qualified lookup/context adaptations only; preserve all scenarios/assertions/counters and deliberate v1 cutover cases; baseline hash retained, final freeze lifted per IG-CRIT-R1-01 |
| API | test/message-template-bff.e2e-spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | test/message-template-drafts.e2e-spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | test/message-template-management.e2e-spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/evolution/evolution.client.spec.ts | M | Limited user-validated Evolution observation guard/unit tests; exact scope and original hashes in evidence/evolution-observation-companion-user-validation.json; no unrelated mutation |
| API | src/integrations/evolution/evolution.client.ts | M | Limited user-validated Evolution observation guard/unit tests; exact scope and original hashes in evidence/evolution-observation-companion-user-validation.json; no unrelated mutation |
| API | src/integrations/meta/meta.client.spec.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/meta.client.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/surfaces/public/public.module.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Web | src/telas/Modelos.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Web | src/telas/Modelos.tsx | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Web | src/App.tsx | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Foundation | artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/v13-public-product.diff | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| Foundation | artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-output-e53-v1.1.txt | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| Foundation | artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-output-e54-v1.1.txt | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| Foundation | artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-output-e64-v1.1.txt | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| root | [ ]foundation_documentation/artifacts/tmp/st-con-05-r27-browser-capture-20261021T2325Z/chunks/012.json | ?? | Prior ST-CON-04 retained109byte artifact only, exact SHA b9e84a70e27049eb661ac7c9496c0db2a8721f8c46909aa90f872e6c40ec7c80; no input/proof or new mutation; later authorized companion check required |

### Not Expected Changed Paths
| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| root | .gitmodules | any | pipeline-owned, sem alteração |
| root | .env | any | segredo privado |
| root | .env.testing | any | segredo privado |
| API | .env | any | segredo privado |
| API | .env.testing | any | segredo privado |
| API | .local-files/** | any | dados privados |
| Web | .env | any | segredo privado |
| Web | .env.testing | any | segredo privado |
| API | package-lock.json | any | nenhum pacote novo é necessário para HTTP/crypto |
| Web | package-lock.json | any | nenhum SDK novo no browser |
| Foundation | todos/completed/features/TODO-leadshug-start-conversation-by-contact.md | any | preservar prova anterior |

### Diff Deviation Analysis
Superfícies root/safe runner/CI/compose/gateway e diferenças públicas herdadas estão admitidas por caminhos exatos e inventário de preservação em evidence/inherited-public-preservation-v1.2.json. Só a zona de mutação desta fatia pode ganhar alterações; herança fora dela deve manter hashes/deleções e índice root. O resíduo root109bytes conserva a admissão exata anterior e exige companion autorizado posterior. Não executar guards integrais que enumerem/leiam/hash privados até o plano específico posterior; code approval não concede essa exceção. Nada será restaurado automaticamente para satisfazer guard.

Active v1.2 preserves35inherited rows plus two user-admitted Evolution paths. Complete original v1.1 policy and hashes remain unchanged historical evidence.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** nomes privados de classes, índices e testes dentro das responsabilidades congeladas; correções exigidas pelo mesmo percurso.
- **Must update or split the TODO:** mídia, merge, nova plataforma, publicação Meta, outro ambiente, permissões mais amplas, política externa diferente ou novos caminhos fora da admissão estrita.

## Definition of Done
- [ ] DOD-01 Contato local, identidades qualificadas e rota imutável têm unicidade/FKs que comprovam mesma BU, mesmo contato e recurso da conexão; nenhum recurso empresarial em duas BUs através de adapters. Uma BU admite um recurso WhatsApp durável, com seus dois adapters, e várias contas Instagram; outro número WhatsApp falha409sem alterar owner.
- [ ] DOD-02 Migração preserva IDs de conversa/mensagem/BU/ProviderResourceIdentity, autoria, timestamps, unread e conteúdo; proveniência desconhecida conserva sua incerteza. Snapshots/intenções antigos e conclusão local de aceitos têm cutover explícito, sem HTTP repetido.
- [ ] DOD-03 Conexão OAuth Instagram é ADMIN+, idempotente, ligada à sessão e ao recurso verificado; tokens cifrados, expirados/revogados não habilitam envio; reautorizar não muda recurso/owner silenciosamente.
- [ ] DOD-04 Webhook autentica raw body e app correto antes de conteúdo; nova entrada e replay concorrem sem duplicar contato/conversa/mensagem/unread; echo não vira entrada nem autoria humana inventada.
- [ ] DOD-05 DM textual aparece na lista/thread da BU; resposta usa rota exata pelo Channel/OutboundService, respeita política e conserva distinção entre aceitação e entrega.
- [ ] DOD-06 Cadastro/Atendimento apresentam BU, conta/origem e remetente sem tratar ID Instagram como telefone; ações/rascunhos e respostas assíncronas estão vinculados à BU/rota/geração.
- [ ] DOD-07 API v1, Typebot e Consultar/lista/drilldown/CSV WhatsApp mantêm contratos e isolamento; projeções legadas de conexões carregam no máximo os dois bindings WhatsApp compatíveis e não hidratam Instagram; Instagram não entra por telefone ou ativa bot por acidente; autoria/modelos/janela atuais preservados.
- [ ] DOD-08 Harness de dependência abstrata, batch/queries limitadas e invariantes PostgreSQL/concorrência passam; nenhum framework genérico ou fallback escondido.
- [ ] DOD-09 ALL canônico com fontes seladas, migrações descartáveis e Playwright mutation contra backend real passa, com admissão CI de todos os novos cenários e sem segredos operacionais.
- [ ] DOD-10 Em plano runtime posterior aprovado: DM real Instagram→LeadsHug→resposta no aparelho e retomada; nova troca nos dois WhatsApps. Teste Meta sintético não substitui essas provas.
- [ ] DOD-11 Revisões independentes, segurança, pcv-1, cutover, TQA, guards de escopo/completion/authority e owners canônicos concluídos, riscos herdados mantidos sob suas restrições.

## Validation Steps
- [ ] VAL-01 RED/GREEN causal para identidade/ownership/rota/nonce/replay/assinatura; falhar contra baseline real antes da implementação e não adaptar asserts para mascarar erro.
- [ ] VAL-02 PostgreSQL descartável: todas as migrations, seed legado com duas modalidades, grupos e proveniência incompleta; snapshots PREPARED/SENDING/aceitos; deploy/checksum e preservação antes/depois, com abortos seguros.
- [ ] VAL-03 OAuth falso no boundary HTTP, multi-BU/tenant/ator, CAS concorrente, code único e troca tardia; assinatura raw/segredo errado, contas com IDs iguais, credencial vencida/rotacionada, eco e replay.
- [ ] VAL-04 Playwright real-backend: conectar/salvar/recarregar, pending/erro/reautorizar, DM e resposta por conta, duas contas Instagram na mesma BU com mesmo peer textual, mudança de BU A→B→A e janela fechada; nenhuma chamada a destinatários reais no browser automatizado.
- [ ] VAL-05 `bash scripts/test-channels-local.sh all` com paridade CI e bundle/backend comprovadamente frescos; testes específicos são diagnóstico, nunca substituto do ALL.
- [ ] VAL-06 Segurança + EPS/FRC/BCI/RLS + audit-protocol-triple-review (Performance, TQA e Cutover), adherence e final review independentes sobre a fonte consolidada.
- [ ] VAL-07 Plano local separado aprovado, sem reset: estado/migrations, imagens/freshness, HTTPS e callback próprios Instagram, prova física Instagram+WhatsApps e retomada preservando outros serviços/volumes.
- [ ] VAL-08 Guards finais e evidência específica por Scope/DoD/Validation; sem nova varredura privada não autorizada, promoção ou produção.

## Completion Evidence Matrix (Required Before Delivery Claim)
Linhas por critério exato; evidência futura permanece planned, sem alegação de implementação. Em critérios de schema/migration, anexar deploy/status e preservação em PostgreSQL descartável. Em fluxos visíveis, anexar Playwright mutation com backend real e freshness; testes unitários não substituem navegação ou prova física. Atualizar caminhos/comandos exatos com receipts reais antes de aceitar cada linha.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | SCOPE-01 Consolidar, após aprovação, as propostas DEC-qualified-contact-conversation, DEC-business-resource-provider-identity e DEC-explicit-channel-routing nos owners canônicos, distinguindo arquitetura e entrega. | doc | artifacts/reviews/leadshug-instagram-channel-20261023/evidence/canonical-consolidation-cp1.json | n/a | passed | Canonical target consolidation only; no product/runtime proof |
| SCOPE-02 | Scope | SCOPE-02 Estabelecer contato local e identidade externa qualificada, recursos empresariais e rotas imutáveis; no máximo um recurso empresarial WhatsApp durável por BU (oficial+Evolution no mesmo número comprovado) e múltiplas contas Instagram; preservar IDs de BU/conversa/mensagem e identidades técnicas existentes. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-03 | Scope | SCOPE-03 Migrar consumidores de telefone/tipo para identidade/rota; BFF multicanal, API pública, Typebot e Consultar (lista/drilldown/CSV) preservados no subconjunto WhatsApp, sem Instagram acidental. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-04 | Scope | SCOPE-04 Conexão Instagram Login no app existente com configuração própria do produto, tentativas por ator/sessão/BU, autorização server-side, armazenamento cifrado, reautorização e desconexão locais explícitas. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-05 | Scope | SCOPE-05 Ingresso Instagram autenticado, normalização textual, deduplicação transacional e estado honesto de recebimento; nenhum sucesso inferido de OAuth/challenge sintético. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-06 | Scope | SCOPE-06 Implementação Instagram registrada no Channel; política textual por recurso; envio pelo único OutboundService e aceitação comuns, sem fallback e sem retry externo ambíguo. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-07 | Scope | SCOPE-07 Cadastro de conexões e Atendimento React com origem/conta/contato legíveis, compositor vinculado à rota e proteção contra resposta atrasada/troca de BU. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-08 | Scope | SCOPE-08 Testes comuns e específicos, PostgreSQL, navegador real-backend/freshness, concorrência, isolamento, cutover, provas físicas e fechamento local com todos os gates. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-01 | Definition of Done | DOD-01 Contato local, identidades qualificadas e rota imutável têm unicidade/FKs que comprovam mesma BU, mesmo contato e recurso da conexão; nenhum recurso empresarial em duas BUs através de adapters. Uma BU admite um recurso WhatsApp durável, com seus dois adapters, e várias contas Instagram; outro número WhatsApp falha409sem alterar owner. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-02 | Definition of Done | DOD-02 Migração preserva IDs de conversa/mensagem/BU/ProviderResourceIdentity, autoria, timestamps, unread e conteúdo; proveniência desconhecida conserva sua incerteza. Snapshots/intenções antigos e conclusão local de aceitos têm cutover explícito, sem HTTP repetido. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-03 | Definition of Done | DOD-03 Conexão OAuth Instagram é ADMIN+, idempotente, ligada à sessão e ao recurso verificado; tokens cifrados, expirados/revogados não habilitam envio; reautorizar não muda recurso/owner silenciosamente. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-04 | Definition of Done | DOD-04 Webhook autentica raw body e app correto antes de conteúdo; nova entrada e replay concorrem sem duplicar contato/conversa/mensagem/unread; echo não vira entrada nem autoria humana inventada. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-05 | Definition of Done | DOD-05 DM textual aparece na lista/thread da BU; resposta usa rota exata pelo Channel/OutboundService, respeita política e conserva distinção entre aceitação e entrega. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-06 | Definition of Done | DOD-06 Cadastro/Atendimento apresentam BU, conta/origem e remetente sem tratar ID Instagram como telefone; ações/rascunhos e respostas assíncronas estão vinculados à BU/rota/geração. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-07 | Definition of Done | DOD-07 API v1, Typebot e Consultar/lista/drilldown/CSV WhatsApp mantêm contratos e isolamento; projeções legadas de conexões carregam no máximo os dois bindings WhatsApp compatíveis e não hidratam Instagram; Instagram não entra por telefone ou ativa bot por acidente; autoria/modelos/janela atuais preservados. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-08 | Definition of Done | DOD-08 Harness de dependência abstrata, batch/queries limitadas e invariantes PostgreSQL/concorrência passam; nenhum framework genérico ou fallback escondido. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-09 | Definition of Done | DOD-09 ALL canônico com fontes seladas, migrações descartáveis e Playwright mutation contra backend real passa, com admissão CI de todos os novos cenários e sem segredos operacionais. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-10 | Definition of Done | DOD-10 Em plano runtime posterior aprovado: DM real Instagram→LeadsHug→resposta no aparelho e retomada; nova troca nos dois WhatsApps. Teste Meta sintético não substitui essas provas. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-11 | Definition of Done | DOD-11 Revisões independentes, segurança, pcv-1, cutover, TQA, guards de escopo/completion/authority e owners canônicos concluídos, riscos herdados mantidos sob suas restrições. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-01 | Validation Steps | VAL-01 RED/GREEN causal para identidade/ownership/rota/nonce/replay/assinatura; falhar contra baseline real antes da implementação e não adaptar asserts para mascarar erro. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-02 | Validation Steps | VAL-02 PostgreSQL descartável: todas as migrations, seed legado com duas modalidades, grupos e proveniência incompleta; snapshots PREPARED/SENDING/aceitos; deploy/checksum e preservação antes/depois, com abortos seguros. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-03 | Validation Steps | VAL-03 OAuth falso no boundary HTTP, multi-BU/tenant/ator, CAS concorrente, code único e troca tardia; assinatura raw/segredo errado, contas com IDs iguais, credencial vencida/rotacionada, eco e replay. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-04 | Validation Steps | VAL-04 Playwright real-backend: conectar/salvar/recarregar, pending/erro/reautorizar, DM e resposta por conta, duas contas Instagram na mesma BU com mesmo peer textual, mudança de BU A→B→A e janela fechada; nenhuma chamada a destinatários reais no browser automatizado. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-05 | Validation Steps | VAL-05 `bash scripts/test-channels-local.sh all` com paridade CI e bundle/backend comprovadamente frescos; testes específicos são diagnóstico, nunca substituto do ALL. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-06 | Validation Steps | VAL-06 Segurança + EPS/FRC/BCI/RLS + audit-protocol-triple-review (Performance, TQA e Cutover), adherence e final review independentes sobre a fonte consolidada. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-07 | Validation Steps | VAL-07 Plano local separado aprovado, sem reset: estado/migrations, imagens/freshness, HTTPS e callback próprios Instagram, prova física Instagram+WhatsApps e retomada preservando outros serviços/volumes. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-08 | Validation Steps | VAL-08 Guards finais e evidência específica por Scope/DoD/Validation; sem nova varredura privada não autorizada, promoção ou produção. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |

## External Dependency Readiness (Required When External Systems Matter)
| Dependency | Why It Matters | Status (`unknown|healthy|degraded|failing|rate-limited|stale`) | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Conta profissional e acesso humano | autorização/prova real | healthy | 2026-10-24, declaração humana | conta adicionada, sem token de teste gerado | não é teste de API/token; geração aguarda plano apropriado |
| Opção Instagram no app existente | reutilização da instalação | healthy | 2026-10-23, declaração humana | usuário consultou o painel | não comprova configuração/Advanced Access |
| Documentação Meta detalhada | OAuth/assinatura/expiração/eligibilidade | healthy | 2026-10-23 | leitura direta pública200 de Business Login, get-started, Messaging e Webhooks; hashes no receipt primário | 429da ferramenta web foi observação anterior, não limite corrente; conta real continua unknown |
| Conta/app/API Instagram efetivos | campos, permissões e entrega | unknown | n/a | nenhuma API/segredo consultados | gates próprios, sem copiar WABA/SDK WhatsApp |
| Runtime/HTTPS local | prova assistida | stale | última prova ST-CON-04 | nenhum probe nesta tarefa | plano separado, não reutilizar túnel antigo por suposição |

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs, react, postgresql, prisma, docker
- **Expected supporting profiles:** strategic-cto, operational-devops, assurance-tester-quality, assurance-security-adversarial
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | contrato e código após aprovação | API/Web | CP1 accepted; CP2 sole writer next, authority/routing receipts recorded below |
| operational-coder | strategic-cto | consolidação de domínio/constituição | Foundation | SCOPE-01 consolidated; implementation evidence remains pending |
| operational-coder | operational-devops | rollout local com migrações/HTTPS | runtime aprovado depois | planned |
| operational-coder | assurance-tester-quality | testes e revisões | provas consolidadas | planned |

## Complexity
- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section: CP1identidade/cutover; CP2OAuth/ingresso; CP3Channel/política; CP4UI/CI; CP5reviews; CP6runtime real/fechamento. Somente CP6 fecha a entrega funcional.
- **Why this level:** alteração cross-module de schema, grants, entrada autenticada, envio irreversível e UI concorrente, mantendo dados e consumidores existentes.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:** identity-and-tenancy.md, inbox-and-conversations.md, audit-and-history.md no mesmo diretório.
- **Planned decision promotion targets (module sections):** identidade empresarial/credencial/Instagram em Canais; contato/conversa/rota em Inbox; BU/grants em Tenancy; eventos seguros em Audit.
- **Module decision consolidation targets:** os mesmos owners; não promover essas propostas como entregues antes dos gates e provas.

## Decision Pending (Resolve Before Freeze)
- Q-IG-01 resolved-for-review: Instagram Login confirmado pelo operador; protocolo e relações de IDs verificados em fontes primárias200, com contrato explícito abaixo. Valores/concessões/entrega reais permanecem gates de runtime, não suposições de readiness atual.
- Q-IG-02 resolved-for-review: caminhos públicos exatos e ledger de herança/fingerprints preservados; nenhuma inspeção privada ou alteração de produto feita. Revisão/guards de preapproval ainda precisam aceitar a estrutura; conferência integral posterior requer plano próprio.

## Decisions (Resolved Before Freeze)
- D-01 BU operacional conforme escolha humana; Channel abstrato com conexões persistidas, sem telefone sintético.
- D-02 Contato local por BU e identidades qualificadas: WhatsApp pessoa E.164 compartilhado por oficial/não oficial comprovados; grupo namespace separado; Instagram por contexto de app/API+conta empresarial+peer opaco. Sem merge entre plataformas.
- D-03 Identidade empresarial única no LeadsHug atravessa adapters e mantém owner durável; ProviderResourceIdentity preserva IDs técnicos/chaves de mensagens. Conflito não transfere nem vaza.
- D-04 Rota imutável com contato/recurso/BU coerentes e operação v2 capturada com vínculo exato; múltiplas contas Instagram na BU, mas um único recurso empresarial WhatsApp durável com oficial+Evolution comprovados. Sem seleção pelo primeiro tipo, fallback automático ou redirecionamento por nova entrada concorrente.
- D-05 Instagram Login confirmado no app existente; clientId/secret do produto e segredo de webhook por finalidade, sem fallback. OAuth, user_id/IG_ID, assinatura, inscrição e token longo seguem o contrato primário abaixo; configuração real e entrega são verificadas só no plano runtime posterior.
- D-06 DM individual textual recebida primeiro; política própria, sem HUMAN_AGENT, prospecção, mídia/grupos ou templates. Bots Instagram desabilitados explicitamente.
- D-07 Único sender/aceitação e resultados ACCEPTED/BLOCKED/REJECTED/UNKNOWN; preservar idempotência/admissões, autoria, dedup e fences; erro/timeout não autoriza novo POST.
- D-08 Migração versionada preserva IDs/histórico e bytes lógicos de request/fingerprint/snapshots/deadlines v1; a matriz de estados abaixo governa recuperação local sem provider HTTP. Contexto v2 e novas identidades somente para novos writes; não rehash/rewrite v1 nem derivar rota histórica de BU.phone/canal disponível.
- D-09 Consultar/lista/drilldown/CSV conservam o contrato por telefone apenas para identidades WhatsApp qualificadas, com número empresarial do recurso único comprovado; Instagram fica no Atendimento e não nessa consulta. Projeções legadas de conexões de BU retornam no máximo os dois bindings WhatsApp compatíveis; Instagram usa catálogo paginado. API pública v1 conserva semântica WhatsApp: accounts/conversations/messages/claim/release não aceitam nem projetam Instagram como telefone; rotas BFF evoluem com React. Typebot/session/webhooks OUT existentes devem qualificar identidade e manter automação Instagram bloqueada.
- D-10 Test-first e ALL real-backend com fontes frescas; isolamento e capacidade também provados com duas contas Instagram sintéticas na mesma BU. Prova real exige plano posterior e não habilita produção/App Review.

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling (`Preserve|Supersede (Intentional)|Out of Scope`) | Evidence |
| --- | --- | --- | --- |
| identity-and-tenancy#bu-operacional-multicanal | BU operação/grants confirmados; produto ainda WhatsApp | Preserve | decisão DEC-bu-operational-multichannel |
| integrations-and-channels#cadastro-de-números-st-con-01 | recurso/credencial por vínculo e geração, ownership durável de provider | Preserve | contrato ST-CON-01 |
| integrations-and-channels#channel | Channel/Resolver e sender comum | Preserve | channel.ts e registro |
| inbox-and-conversations#iniciar-conversa-e-primeiro-envio--st-con-04 | abertura WhatsApp por telefone, preview/intenção/admissão e snapshots duráveis | Supersede (Intentional) | evoluir endereço/rota e manter o percurso funcional WhatsApp e recuperação |
| inbox-and-conversations#invariants | conversa por BU/contato | Preserve | contato passa a ter ID local/identidade qualificada |
| integrations-and-channels#templates | gestão e envio de templates WhatsApp | Preserve | nenhuma elegibilidade fictícia Instagram |

## Decision Baseline (Frozen Before Implementation)
D-01..D-10 e as cláusulas normativas v1.3 estão FROZEN e APROVADAS para implementação pela resposta humana de2026-10-23. Receipt approval-execution-cp1.json preserva hash do TODO apresentado e baseline f4891ba1. Atualizações de status/ingestão registram a aprovação, sem mudar WHAT; novos achados materiais exigem reconvergência/renovação antes de executar o desvio.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)
- **Applicability (`required|not_needed`):** required
- **Why this applies:** aposenta BU=número no comportamento e seleção por enum único; muda identidade/rotas canônicas.
- **Deviation / debt being retired:** telefone/username como identidade de domínio e primeiro canal do tipo como endereço de dispatch.
- **Target steady-state after closeout:** BU operacional, contato/peer/empresa/provider separados, conexão e rota explícitas e um Channel/Outbound/Acceptance.
- **Temporary exceptions allowed:** reader v1 somente para leitura/replay/conclusão local de fatos preexistentes, e colunas legadas read-only para preservar evidência; limites definidos na matriz por estado IG-ARCH-R1-02. Nenhuma escrita canônica v1 ou dispatch nesse reader.
- **Cutover / removal condition:** migrações descartáveis e auditoria provam novos writes exclusivamente v2/identidades/rotas; consumidores deixam de resolver destinatário por contact string ou BU.phone. Reader de fatos v1 fica restrito ao acervo imutável, sem reinserir o caminho antigo de envio.

### Patterns To Enforce
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| DIP/DI e capacidades explícitas, substituição pelo contrato Channel | D-01, D-06, D-07 | consumers/Channel/composição | nenhum cast concreto ou sender paralelo |
| Constraints, ownership durável e rota/contexto imutáveis | D-02, D-03, D-04, IG-ARCH-R1-01 | PostgreSQL/Inbox/Canais | mesma BU, contato e recurso comprovados antes de dispatch |
| Transações curtas, HTTP fora da transação e aceitação comum | D-07, D-08 | OAuth/ingresso/envio | concorrência e recuperação não repetem efeito externo |
| Segredo por finalidade e dados privados somente no adapter/crypto | D-05 | configuração/OAuth/webhook | nenhuma credencial ou destinatário controlado pelo browser |

### Prohibited Anti-Patterns
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| Contato sem namespace, primeiro canal pronto, rota inferida ou lista truncada | testes de colisão/rota/cardinalidade e revisão | destinatário e recurso errados | none |
| Cast concreto, sender/inbox duplicado ou fallback de segredo | dependency harness e testes negativos | viola contrato comum e isolamento | none |
| Getter que muta provider, bot Instagram implícito ou HTTP de recuperação v1 | contadores HTTP/Typebot e cutover | efeitos não autorizados/duplicação | none |
| Asserts removidos, fonte stale ou dual-write canônico indefinido | ALL/freshness/TQA/cutover | prova fraca ou autoridade concorrente | somente reader v1 limitado, sem novos writes |

### Architecture Protection Harness
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing (`already-enforced|implement-in-this-todo|follow-up-approved|manual-only-with-rationale`) | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | domínio→integração | channel-dependencies.spec.ts e template-management.dependencies.spec.ts | import concreto/cast ou sender duplicado | implement-in-this-todo | DOD-08 / VAL-01,05 |
| test | PostgreSQL | instagram/multichannel e2e e migrations | colisão, ownership interadapter, replay, snapshots | implement-in-this-todo | DOD-01,02 / VAL-02,03 |
| test | UI/rotas | e2e/instagram*.spec.ts com backend real | troca de BU/conta, rascunho e publicação desatualizada | implement-in-this-todo | DOD-06 / VAL-04,05 |
| audit | fonte consolidada | adherence, TQA, Performance e Cutover independentes | atalhos, bridge oculto e prova fraca | implement-in-this-todo | DOD-11 / VAL-06 |

## Architecture Review Gates
- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** no_material_findings
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/architecture-r2-result.json; terminal go sobre r1 integrado e duas clarificações r2 revisadas/fechadas, sem autoridade de implementação.
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** not_run
- **Adherence review evidence / resolution:** planned para entrega.
- **No-go handling:** findings materiais reconvergem contrato e baseline antes de aprovação/entrega.

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** f4891ba1bddec62737f5624cac8d4a32224006d7
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** baseline v1.3 publicada após integração dos três achados de crítica r1; re-review permitido, sem execução de produto.
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/review-baseline-freeze-r4.json
- **Pre-freeze packet-prep rule:** prepared-pre-freeze não equivale a passed; guards formais só depois do commit/push.

## Gate: Review Scope Drift
- **Gate decision:** required
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md`
- **Gate status:** no_material_findings
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/review-scope-guard-r4.json; actual go,23seções materiais comparadas e0alteradas contra baseline publicada f4891ba1.

## Questions To Close
- Q-IG-01/02 reconvergidos para review: verificar suficiência na nova rodada. Detalhe físico de classes sem efeito no contrato não vira pergunta de produto.
- O operador já confirmou profissional/acesso/BU conjunta/produto Instagram: manter fatos, sem pedir número/IDs/tokens no chat.

## Assumptions Preview
| Assumption ID | Assumption | Evidence | If False | Confidence (`High|Medium|Low`) | Handling (`Keep as Assumption|Promote to Decision|Block`) |
| --- | --- | --- | --- | --- | --- |
| A-01 | Channel/OutboundService e MessageAcceptanceService são os owners reutilizáveis de envio/aceitação; preservam contexto/admissões | api-app/src/domain/channels/transport/channel.ts; api-app/src/domain/inbox/outbound.service.ts; api-app/src/domain/inbox/message-acceptance.service.ts | reabrir diagnóstico/escopo, não criar outro sender | High | Keep as Assumption |
| A-02 | consumer atual seleciona tipo e contact string; mudança demanda mais que adapter | api-app/src/integrations/channels/prisma-channel-resolver.ts; api-app/prisma/schema.prisma; web-app/src/telas/Numeros.tsx | revisar plano, não declarar banco pronto para Instagram | High | Promote to Decision |
| A-03 | API v1 e Typebot usam endereço WhatsApp e devem ficar fora da ativação Instagram | api-app/src/surfaces/public/conversations.controller.ts; api-app/src/domain/inbox/incoming.service.ts | revisar consumers antes de code | High | Promote to Decision |
| A-04 | Protocolo Instagram deve usar namespace/cliente próprios; valores e concessões reais só serão verificados no plano runtime | api-app/src/surfaces/webhooks/meta.controller.ts é somente WhatsApp; primary-instagram-contract-r1.json e confirmação do título Instagram Login | impedir ativação/prova se recurso/testador não for elegível | High | Promote to Decision |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces
Contrato de API proposto e modelo físico a seguir; lista estrita e herança pública explícitas acima. Runners públicos e fixtures são owners da validação descartável. API/Web e Foundation no checkout principal, sem ambiente runtime tocado agora.

### Ordered Steps
1. CP0confirmar a reconvergência Q-IG-01/02; diagnóstico+arquitetura e crítica no-context táticas; Plan Review completo; coherence/scope/authority pre-approval; pedir APROVADO.
2. CP1executor único, baseline público pós-aprovação, REDcausal de identidade/cutover e migrações descartáveis; garantir ownership/dedupe/recuperação sem provider HTTP.
3. CP2OAuth/registro Instagram e ingresso contra HTTP fake nos limites reais; assinatura/nonce/contexto e estados.
4. CP3Channel Instagram e resolução de política/rota; aceitação/admissões comuns, APIv1/Typebot WhatsApp isolados.
5. CP4UI e paridade CI/browser; fontes/bundle/backend selados antes do ALL e das reviews.
6. CP5adherence, segurança, pcv, TQA/cutover e final review; consolidar owners, rever diffs e preparar plano runtime concreto.
7. CP6somente depois de aprovar plano runtime: migração local preservativa, imagens e HTTPS comprovados, configuração Meta pelo operador, DM/reply/retomada e regressão WhatsApp; guards/fechamento local.

### Test Strategy
- **Strategy:** test-first
- **Why:** isolamento e envio irreversível não podem depender de testes espelhando a implementação.
- **Fail-first target(s):** colisões de peer por plataforma/conta; owner do mesmo telefone em adapters/BUs distintos; replay concorrente; nonce de outra sessão; assinatura errada; composer A→B→A; aceito remoto com persistência local interrompida.
- **Pre-APROVADO RED Evidence Capture:** not_needed; feature nova, nenhuma edição de teste antes de aprovação.

### Flow Evidence Planning Matrix
| Criterion / Flow | Why Flow-Impacting | Platform Parity (`android-only|web-only|shared-android-web|divergent-android-web|n/a`) | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Conectar/reautorizar/cancelar e persistir conta | OAuth/config/estado/admin | web-only | Playwright mutation | yes | yes | instagram*.spec.ts com fake no HTTP, PostgreSQL real e reload | n/a |
| DM/Inbox/resposta/rotas e troca de BU | identidade, DTO, unread, dispatch | web-only | Playwright mutation | yes | yes | duas contas e dois tenants sintéticos; backend real | n/a |
| Preservação WhatsApp/modelos/primeiro envio | refatoração de consumers/dados | web-only | Playwright mutation | yes | yes | onboarding/channel/start/template specs existentes preservados | n/a |
| DM real e retomada | provedor externo e aparelho | web-only | prova assistida e runtime aprovado | yes | yes | operador + receipts seguros/freshness, sem conteúdo privado | browser fake não substitui provider |

### Frontend / Consumer Matrix
| Producer / Contract | Consumers | Handling and regression boundary |
| --- | --- | --- |
| BU/conexão/identidades/rotas | BFF/React/cadastro/tenancy | DTOs explícitos e navegação por IDs locais; sem número obrigatório |
| Contact/Conversation/Message | Inbox/paginação/realtime/histórico/initial/admissions | mesmos IDs e owner de aceitação, contexto versionado e rota segura |
| Novos tipos/plataformas | API v1, Typebot/session, webhook OUT, templates | revisar todas as projeções; conservar subconjunto WhatsApp, bloquear Instagram não contratado |
| Credencial/geração/política | resolver/adapter/estado/compositor | não enviar segredo, nem tratar readiness local como concessão permanente |
| OAuth/webhook | gateway/session/CSRF/audit/HTTPclients | callback dedicado com segredo correto, sem query sensível nos logs |

### Local CI-Equivalent Suite Matrix
| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API + PostgreSQL | schema/auth/rotas/consumers | identidade/ownership, OAuth, dedup/echo, snapshots e WhatsApp legado | DB descartável; seed legado+novo; fake na fronteira HTTP; config sintética | `bash scripts/test-channels-local.sh all` | Local-Implemented | planned | ALLstdout/JSONduráveis | unitários não substituem constraints/transações |
| Web + Playwright | UI/projeções/rotas | conexão→reload→DM→resposta, multiaccount/tenant e races | build atual, backend real, mesmo DB/porta de CI, bundle provado | `bash scripts/test-channels-local.sh all` | Local-Implemented | planned | traces+report+fontes+fingerprints | sem stub de regra de domínio |
| Root CI/paridade | runners/compose/admissão | novos specs efetivamente executados com corpo/asserts | inventário público; nenhum .env real; admissões explícitas | `python3 scripts/check-channels-ci-parity.py --self-test` e ALL | Local-Implemented | planned | relatório de admissão/freshness | caminhos e ledger públicos explícitos |

### Runtime / Rollout Notes
Local primeiro, projeto runtime existente `leadshug_channels_local`; validação descartável `leadshug_channels_validation`, conforme runner. NÃO executar runtime nesta tarefa. Ativação, acesso opaco ao .env.testing, migração em DB real e callbacks/túneis dependem de plano próprio posterior. Plano deverá provar preservação de peers/volumes, snapshots/admissões pendentes, versões/checksums e abort-before-write em conflito. Lock timeout5s/statement60s nos comandos de migração; nenhum reset. Aprovação de código não publica app Meta nem autoriza produção.

## Plan Review Gate
**Status:** arquitetura r2go, findings r1/r2 integrados; crítica r2 terminal go após as três correções r1; sete lentes revisadas, sem achado material pendente. Evidência critique-r2-result.json; isso não prova implementação.

### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards
| Issue ID / evidence / why now | Option A — recommended | Option B | Option C — do nothing | Recommendation |
| --- | --- | --- | --- | --- |
| IG-P01 high — schema.prisma:93/127/175/389; mesma BU terá peers não telefônicos | identidade local/qualificada, recurso empresarial+provider e rota. Effort high; risk medium; blast cross-module; manutenção medium; performance indexed; elegância/solidez improve | só adicionar enum/guardar IGSID em contact. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | manter WhatsApp-only. Effort none; risk low; blast local; manutenção neutral; performance/elegância/solidez neutral; não entrega objetivo | A, com cutover preservativo |
| IG-P02 high — prisma-channel-resolver.ts:selectCandidate; tipo não identifica conta | rota/vínculo capturados e revalidados. Effort medium; risk medium; blast cross-module; manutenção low; performance bounded; elegância/solidez improve | primeiro canal pronto/fallback. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | não habilitar Instagram. Effort none; risk low; blast local; manutenção/performance/elegância/solidez neutral | A, sem roteamento silencioso |
| IG-P03 high — meta.controller.ts só WhatsApp; Q-IG-01 agora documentado em fonte primária | protocolo/segredo/config Instagram próprios verificados; nonce/session/CAS. Effort medium; risk medium; blast module; manutenção medium; performance bounded; elegância/solidez improve | reutilizar token/WABA/segredo sem prova. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | esperar evidência antes de code. Effort low; risk low; blast local; manutenção neutral; performance/elegância/solidez neutral | A após evidência, C enquanto pendente |
| IG-P04 high — intents/admissions e receipts de ST-CON-04 persistidos | cutover versionado para dados+snapshots, reconstrução só comprovada, accepted local-only. Effort high; risk medium; blast cross-module; manutenção medium; performance bounded; elegância/solidez improve | recriar DB/IDs. Effort low; risk high; blast cross-module; manutenção low; performance neutral; elegância/solidez regress | não migrar. Effort none; risk low; blast local; manutenção/performance/elegância/solidez neutral; não entrega objetivo | A, sem reset/route guess |

### Failure Modes & Edge Cases
Mesmo ID em plataformas/contas; username mutável; propriedade conflitante entre adapters; OAuth popup cancelado/code consumido/sem sessão; token vencido/revogado; bad signature e payload oversized; eventos fora de ordem, duplicados e echo-first; timeout remoto; DB após ACK; rascunho antigo/A→B→A; janela fechada; múltiplas rotas; legacy sem proveniência; bot e APIv1 tratando IGSID como telefone; callbacks WhatsApp alterados indevidamente.

### Residual Unknowns / Risks
Q-IG-01/02 estão reconvergidos para review; arquitetura/crítica e guards ainda impedem pedir APROVADO. Não há medidas de desempenho ou prova de permissão real nesta etapa. SEC-R6-04, OPS-R4-01 e TQA-ST05-03 do baseline permanecem sob a coorte privada e restrições já registradas; este TODO não as resolve nem amplia público/ambiente.

## Additional Architectural Opinions
- **Needed:** yes
- **Why ambiguity remains:** modelo físico, cutover e protocolo operacional precisam de challenge no pacote completo; opinião estratégica prévia não revisou este TODO.
- **Opinion count:** 2 para este TODO; r1changes_required integrado e r2go terminal
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required; fresh internal no-context reviewer, sem implementação; esperar estado terminal sem interromper/reempacotar por demora.
- **Required lenses:** correctness, performance, elegance, structural-soundness, operational-fit.

## Audit Trigger Matrix
- **Canonical method:** wf-docker-audit-escalation-method
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/audit-floor-r2.json, actual go; todas as lanes abaixo preservam o piso required.

| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | jornada cross-module |
| blast_radius | cross-stack | Nest/React/DB |
| behavioral_change_or_bugfix | yes | canal novo |
| changes_public_contract | yes | BFF/schema/consumers |
| touches_auth_or_tenant | yes | ownership/OAuth/grants |
| touches_runtime_or_infra | yes | novo callback/freshness |
| touches_tests | yes | causal/integração/browser |
| critical_user_journey | yes | atendimento/envio |
| release_or_promotion_critical | no | local/coorte privada |
| high_severity_plan_review_issue | yes | riscos acima |
| explicit_three_lane_request | yes | Performance+TQA+Cutover após implementação |

## Independent No-Context Critique Gate
- **Critique decision:** required
- **Why this decision:** big/cross-stack/schema/auth; confirmar piso após freeze.
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline publicada, escopo candidato completo, decisões, assumptions, plano/issue cards, fontes públicas exatas, dívida/limitações herdadas.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; não implementing agent; wait status-based, external provider não satisfaz gate.
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review, posterior à implementação e adicional à crítica.
- **Critique status:** no_material_findings
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/critique-r2-result.json; terminal go, três achados r1 fechados no contrato v1.3 publicado.

## Rules Acknowledgement / Ingestion
Ingestão vinculante recarregada após APROVADO em2026-10-23: fontes abaixo e workflow de execução/orquestração; executor recarrega o subconjunto do checkpoint antes de editar. Não há waiver.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | autoridade | escopo/execução separadas | code antes de aprovação | executor único |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | gates | freeze/reviews/preflight | aprovação implícita | GO antes de code |
| delphi-ai/workflows/docker/effort-selection-method.md | routing | lanes e provas | modelo inventado | guard por lane |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | backend | contrato/domain/adapter | regra no controller | integração real |
| delphi-ai/workflows/react/change-ui-boundary-method.md | interface | estado/contexto/freshness | resposta atrasada | Playwright |
| delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | schema | migrations versionadas | reset | deploy descartável |
| delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | dados/concurrency | constraints/locks | HTTP em tx | barriers reais |
| foundation_documentation/project_constitution.md | multitenancy | BU/grants | scope por browser | isolamento |
| foundation_documentation/policies/scope_subscope_governance.md | superfícies | owner/route | superfície informal | contrato scoped |
| delphi-ai/workflows/docker/performance-concurrency-validation-method.md | pcv-1 | provas/thresholds | boolean pass | lanes antes da entrega |

## Agent Routing Preflight
- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Routing evidence:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/routing-execution-cp1.json; actual go pós-aprovação, gpt-6-luna medium, um writer no checkout principal.
- **Execution topology:** primary-checkout-single-writer
- **Subagent / delegation authorization:** workflows de executor/review; um writer de produto serializado.
- **Git isolation authorization:** not-authorized
- **Worktree authorization:** not-authorized
- **Worktree authorization reference:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

## Decision Adherence Validation
D-01..D-10 terão evidência específica após execução; todas planned, nenhuma alegação Adherent de código ainda.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)
Uma linha por decisão da baseline dos módulos antes da entrega; Preserved/Superseded(Approved) com prova. Regression ou Exception não resolvidas bloqueiam fechamento.

## Pipeline/Copilot P1/P2 Preflight
Planned sobre fonte/evidências finais; unresolved P1/P2 bloqueia entrega.

## Rule-Spirit Anti-Pattern Hunt
Planned: telefone sintético, segredo global, provider branch nos consumers, fallback de rota, mocks de regra de negócio, asserts enfraquecidos e replay HTTP disfarçado.

## Promotion Finding Routing Ledger
Historical planning observation retained: IG-REV-01..04, strategic source, high/medium/low, release-blocker; ownership/dedup/cutover/limits were integrated into the approved plan, with product verification still open. These observations are not a waiver or proof of product repair. The concrete CP1 findings below all remain in this approved delivery.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP1-R1-01 | high | release-blocker | fix in this TODO | immutable qualified peer is SCOPE-02/DOD-01 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-02 | high | release-blocker | fix in this TODO | current provider attachment equality is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; final persisted association defect repaired; actual official confirmation proved |
| IG-CP1-R1-03 | high | release-blocker | fix in this TODO | durable cross-adapter resource ownership is SCOPE-02/DOD-01 | closed by r5 | adherence-cp1-r5-result.json; exact current quarantine recovery after actual prior receipt |
| IG-CP1-R1-04 | high | release-blocker | fix in this TODO | qualified contact reuse is SCOPE-02,03 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-05 | medium | release-blocker | fix in this TODO | retained ownership/cardinality is SCOPE-02/DOD-01 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-06 | medium | release-blocker | fix in this TODO | safe canonical migration is DOD-02/VAL-02 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-07 | medium | release-blocker | fix in this TODO | preserved regression tests are SCOPE-08/DOD-09 | closed by r5 | cp1-frozen-full-api-green-r5.json; complete379unit/483e2e GREEN on matching37sources |
| IG-CP1-R1-08 | medium | release-blocker | fix in this TODO | required historical cohort is DOD-02/VAL-02 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R2-01 | high | release-blocker | fix in this TODO | one coherent WA business scope is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; WA business scope BU agrees with CHECK/FK and actual positive route |
| IG-CP1-R2-02 | high | release-blocker | fix in this TODO | honest unverified renewal staging is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; original reservation/proof defect repaired; distinct pending lifecycle findings remain below |
| IG-CP1-R3-01 | high | release-blocker | fix in this TODO | single-create/read-before-retry after pending renewal is SCOPE-02/08 | closed by r5 | adherence-cp1-r5-result.json; single create and read-before-retry retained |
| IG-CP1-R3-02 | high | release-blocker | fix in this TODO | managed cleanup ownership survives staged unlink under SCOPE-02/08 | closed by r5 | adherence-cp1-r5-result.json; current staged unlink and stale snapshot fence repaired |
| IG-CP1-R3-03 | medium | release-blocker | fix in this TODO | durable quarantine and later correct-proof recovery preserve existing channel contract | closed by r5 | adherence-cp1-r5-result.json; wrong-number quarantine and correct-proof recovery retained |
| IG-CP1-R3-04 | low | release-blocker | fix in this TODO | required ownership concurrency proof cannot assume winner scheduling; fix assertions in this TODO | closed by r5 | adherence-cp1-r5-result.json; actual-winner concurrency assertion retained |
| IG-CP1-ROOT-01 | high | release-blocker | fix in this TODO | pending current ingress remains retryable without content/trust before proof | closed by r5 | adherence-cp1-r5-result.json; metadata-only staged retry and accepted-key proof retained |
| IG-CP1-R4-01 | high | release-blocker | repeat affected proof in this TODO | four mutations violated the explicit r4 freeze; preserve evidence and validate current bytes anew | closed by r5 | adherence-cp1-r5-result.json; cp1-frozen-full-api-green-r5.json; new stable proof replaces invalidated acceptance |
| IG-CP1-R5-01 | medium | release-blocker | bounded companion in this TODO; protected path validation required | current staged cleanup guarantee depends on a truthful absence observation; inherited adapter weakness is not a new Instagram regression | closed by r8 complete review/current full API | cp1-r8-acceptance.json; adherence-cp1-r8-result.json; cp1-observation-r8-full-api-green.json |
| IG-EVOCOMP-01 | medium | release-blocker | fix admitted caller lifecycle in this TODO | conclusive cleanup must recover same reserved operation and permit one create, without widening protected paths | closed by r3/current full API; protected parser remains R5-01 | evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json |
| IG-EVOCOMP-02 | medium | release-blocker | strengthen proposed tests before source admission | independent malformed name/state and null projection branches need concrete proof plan | proposal resolved r2; implementation not admitted | evolution-observation-companion-critique-r2-result.json |
| IG-EVOCOMP-03 | low | release-blocker | correct proposal wording before validation | exact subject and absence contract must be clear to approving user; small same-artifact correction | proposal resolved r2; implementation not admitted | evolution-observation-companion-critique-r2-result.json |
| IG-EVOCOMP-R2-01 | medium | release-blocker | fence late failure mutation in same admitted caller/test paths | same-attempt recovery must retain later holder facts after lease takeover; inherited catch is not a new adapter regression | closed by r3/current full API | evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json |
| IG-CP1-ROOT-R7-01 | medium | release-blocker | revalidate authorization before provider-error fact mutation in same admitted paths | live DB lease does not replace post-call session/grant revalidation; same existing lifecycle contract, no new middleware scope | closed by r3/current full API | evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json |

| IG-CP2-ROOT-01 | medium | release-blocker | fix in this TODO | accurate persisted budget backoff under SCOPE-04/VAL-03 | closed original defect by CP2 r1; persisted actor/BU backoff assertions; no pre-fix causal RED inferred | adherence-cp2-r1-result.json; prior evidence retained |
| IG-CP2-ROOT-02 | high | release-blocker | fix in this TODO | current post-HTTP lease fence under SCOPE-04/VAL-03 | open; source16 clocks proved; residual finalmapping and mapped preHTTP attemptTTL | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-CP2-ROOT-03 | medium | release-blocker | fix in this TODO | actual credential acquisition/expiry under DOD-03/VAL-03 | closed original defect by CP2 r1; acquisition before delayed profile; no pre-fix causal RED inferred | adherence-cp2-r1-result.json; prior evidence retained |
| IG-CP2-ROOT-04 | high | release-blocker | fix in this TODO | Existing UUID key and durable replay/conflict contract also governs OAuth confirmation | closed original key/recovery defect; strict20 and actualnewversion/currentexpiry historical replay passed | adherence-cp2-r4-result.json; cp2-r3-source-validation-16-result.json; cp2-api-full-r4-result.json |
| IG-CP2-ROOT-05 | medium | release-blocker | verify and fix in this TODO | Successful connected-channel reauthorization must preserve resource/receipt and known subscription | closed original defect by CP2 r1; connected reauthorization preserves receipt/messages without another POST | adherence-cp2-r1-result.json; prior evidence retained |
| IG-CP2-ROOT-06 | high | release-blocker | fix in this TODO | Eligible authenticated current-resource ingress must provide independent receipt after ambiguous dispatch | closed original defect by CP2 r1; signed ingress during held POST and after uncertainty | adherence-cp2-r1-result.json; prior evidence retained |
| IG-SUBPROTO-01 | high | release-blocker | resolve primary protocol in this TODO | Own-subscription GET envelope, ID subject and completeness remain unproved; do not infer unsupported from omission | open; primary prerequisite | subscription-protocol-opinion-result.json |
| IG-SUBPROTO-02 | medium | release-blocker | preserve UNKNOWN fence in admitted code | An unexplained empty or mismatched-ID observation cannot permit a second POST after uncertainty | closed original defect by CP2 r1; UNKNOWN preserves mutation fence; concurrent lifecycle stays SUBREC-02 | adherence-cp2-r1-result.json; prior evidence retained |
| IG-SUBPROTO-03 | medium | release-blocker | retain typed identity purposes in this TODO | No speculative parent-app configuration or guessed ID comparison; same approved OAuth path | closed original defect by CP2 r1; distinct identity purposes; no speculative parent-app configuration | adherence-cp2-r1-result.json; prior evidence retained |
| IG-SUBREC-02 | high | release-blocker | fix in this TODO; related to IG-SUBPROTO-02 | Resource-lifecycle dispatch fence survives new attempt, reauthorization, lease expiry and crash | open; source16 settledcleanup/GETtuple proved; acquisition postCOMMIT cleanup residual | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-SUBREC-03 | medium | release-blocker | retain with IG-SUBPROTO-01 in this TODO | UNKNOWN is valid, but own-account observation remains mandatory and unaccepted | open; primary protocol | subscription-recovery-concretization-result.json |
| IG-SUBREC-04 | medium | by-design/no-action | proposed investigation remains unexecuted | Bounded empirical observations cannot establish universal completeness or authorize repeated mutation | documented; no execution authority inferred | subscription-recovery-concretization-result.json |

| IG-CP2-R1-01 | high | release-blocker | fix in this TODO | Confirmation can promote an expired candidate or overwrite cancellation | closed original TTL/cancel/CAS defect; final clocks remain ROOT02 | adherence-cp2-r3-result.json; qualified stable11..13 |
| IG-CP2-R1-02 | medium | release-blocker | fix in this TODO | Instagram authorization admission diverges from current BU scope and error ordering | closed original authorization order/activeBU/array defect | adherence-cp2-r3-result.json; qualified stable11..13 |
| IG-CP2-R1-03 | high | release-blocker | fix in this TODO | The Instagram HTTP boundary follows redirects beyond its validated endpoints | closed original redirect defect; native fetch boundary proof | adherence-cp2-r3-result.json; qualified stable11..13 |
| IG-CP2-R1-04 | medium | release-blocker | fix in this TODO | Failed OAuth callbacks retain sensitive query URLs without the required response protections | open; exact user-admitted v2 source applied12; infrastructure/fullAPI/gateway/browser proof NOTRUN | adherence-cp2-r3-result.json; oauth-callback-session-companion-ready-v2.json |
| IG-CP2-R1-05 | medium | release-blocker | fix in this TODO | Whole-batch preflight does not validate the supported message structure | closed original preflight defect and exactaccount fixture; currentfullAPI passed | adherence-cp2-r4-result.json; cp2-api-full-r4-result.json |
| IG-CP2-R1-06 | medium | release-blocker | fix in this TODO | The reported sixteen-obligation map exceeds the behavioral proof actually present | open; exact finalmapping/preHTTP TTL/postCOMMIT proof plus primary/precontroller; replay/config/secondNest now supported | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json; cp2-api-full-r4-result.json |
| IG-CP2-ROOT-07 | medium | release-blocker | fix in this TODO | Five Instagram write routes need safe catalog/audit classification | closed original audit/catalog defect; complete canonical coverage passed | adherence-cp2-r3-result.json; cp2-api-full-r3-result.json |

| IG-OAUTH-SESSCOMP-01 | medium | release-blocker | revise companion in same TODO | Unexpected precontroller callback failure also needs clean generic failure redirect | proposal resolved by terminal r2; source unadmitted, implementation proof pending | oauth-callback-session-companion-critique-result.json |

| IG-CP2-ROOT-08 | medium | release-blocker | reprove stable candidate in this TODO | Executor edited authorization source during GREEN05, invalidating current-source proof | closed original source-drift proof defect by stable16/fullAPI/currentcompleteR4; GREEN05 remains invalid | cp2-r4-root-adjudication.json; cp2-api-full-r4-result.json; adherence-cp2-r4-collection.json |

| IG-CP2-ROOT-09 | medium | release-blocker | validate actual current candidate in this TODO | Executor consulted non-authoritative backup instructions and misread empty exact-path Git diff; root corrected authority and positive hash evidence | closed original backup-input/emptydiff inference by currentprincipal/publicproof; filename-only metadata note retained | cp2-r4-root-adjudication.json; adherence-cp2-r4-collection.json; cp2-api-full-r4-result.json |

| IG-CP2-ROOT-15 | medium | release-blocker | fix test fixture in this TODO | Exact account selection is required under multiaccount CP2 proof | closed exactaccount fixture; selected16 andfull549 passed | cp2-api-full-r4-result.json; adherence-cp2-r4-result.json |

## TODO Closeout Disposition
- **Disposition:** blocked
- **Disposition reason:** implementação aprovada em curso; CP1 aceito, findings CP2 e demais checkpoints/gates abertos, sem entrega parcial aceita.
- **Post-commit/push status:** pending
- **Next path/status action:** manter ativo em implementation; corrigir CP2 e continuar CP3..CP6 sob a aprovação e os limites existentes.

## Security Risk Assessment
- **Risk level:** high
- **Why this risk level:** OAuth/segredos/ownership multi-tenant, webhook público e envio irreversível.
- **Attack surface in scope:** session/state/CSRF, assinatura raw, SSRF/URLsdecontinuação, token storage, callbacks/logs e alcance cross-BU.
- **Attack simulation decision:** required
- **Review evidence:** planned, nenhum ataque executado em runtime.
- **Residual security risk:** dívidas herdadas mantidas na coorte OWNER privada; nenhum acesso público novo sem tratamento.

## Performance & Concurrency Risk Assessment
- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** chaves de lookup/rota/listagem, OAuth e mensagens concorrentes, estado React.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | high | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | pending | none | U-QUERY-PATH-UNKNOWN |
| FRC | frontend-race-condition-validation | required | high | FRC-STALE-RESPONSE | before_local_implemented | FRC-E3 | pending | none | U-ASYNC-SURFACE-UNKNOWN |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-JOB-WEBHOOK-API-OVERLAP | before_local_implemented | BCI-E3 | pending | none | U-WRITE-OVERLAP-UNKNOWN |
| RLS | runtime-load-stress-validation | required | high | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E2 | pending | none | U-RUNTIME-PRESSURE-UNKNOWN |

Thresholds/amostragem por lane estão congelados na integração IG-ARCH-R1-04 abaixo; nenhum budget de fornecedor é benchmark do produto.

## Verification Debt Assessment
- **Audit outcome:** high
- **Why this outcome:** feature não implementada, ainda faltam provas de todos os critérios.
- **Inline code TODO debt:** none introduced
- **Evidence / audit artifact:** planned antes de Completed.
- **Accepted residual debt:** somente restrições herdadas declaradas; nenhuma waiver nova.

## Independent Test Quality Audit Gate
- **Audit decision:** required
- **Why this decision:** schema/auth/sharedcontract/criticaljourney e testes novos.
- **Trigger signals in scope:** changed test logic, behavior-defining change, architectural change, shared contract/api/schema, compatibility, critical-user-journey.
- **Required evidence matrix (when architectural):** unit, integration PostgreSQL, web real-backend.
- **Package mode:** bounded-file-set
- **Canonical method:** wf-docker-independent-test-quality-audit-method
- **Audit isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; não implementing agent, sem deadline artificial/review externo.
- **Audit status:** not_run
- **Evidence / reference:** after implementation, full applicable audit, não questionário abreviado.

## Independent No-Context Final Review Gate
- **Final review decision:** required
- **Why this decision:** big/cross-module/schema/auth/runtime.
- **Impact signals in scope:** cross-module blast radius, public contract/schema/api, auth/payment, runtime/queue/realtime/ingress, intentional module supersede, high-severity issue card.
- **Package mode:** bounded-file-set
- **Review isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; esperar estado terminal.
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Final review status:** not_run
- **Evidence / reference:** after all applicable implementation/proof/adherence/test-audit gates.

## Independent Cutover Integrity Audit Gate
- **Cutover audit decision:** required
- **Why this decision:** migração de contato/rotas e contextos persistidos.
- **Cutover signals in scope:** canonical cutover, compatibility exception.
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** audit-protocol-triple-review
- **Cutover audit status:** not_run
- **Evidence / reference:** planned, receita legada versionada deve ser contrato explícito e não shadow canonical path.

## Delivery Confidence Gate
Production-Ready fora de escopo. Local exige todos os critérios, pcv-1 e provas reais do contrato; não declarar concluído com adapter/fake apenas.

## Module Consolidation Gate
Após aprovação, promover decisões aceitas nos owners; após evidência, atualizar estado entregue e cruzar links. Não reescrever entregas históricas ST-CON para parecer novas.

## Commands (Run Locally)
Somente análise pública e guards documentais antes da aprovação. Depois: runner canônico e deploy descartável; runtime local só após plano específico. Nenhum comando com token ou env real aparece neste TODO.

## Gate: Assumption Code Coherence
- **Gate decision:** required
- **Gate status:** no_material_findings
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md`
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/assumption-code-manual-r4.json; leitura delimitada confirmou A-01..04, sem achado material. Guard determinístico artifacts/reviews/leadshug-instagram-channel-20261023/evidence/assumption-code-guard-r4.json retornou actual go; elegibilidade real segue runtime.

## Approval
- **Approval status:** APROVADO
- **Approved by:** usuário desta conversa, em2026-10-23, resposta explícita `APROVADO` ao contrato Instagram v1.3.
- **Approval reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/approval-execution-cp1.json; hash do pacote apresentado e baseline revisada preservados nesse receipt.
- **Approval scope:** SCOPE-01..08, D-01..10, DOD/VAL e cláusulas normativas v1.3; implementação API/Web, documentação e validação descartável sintética exclusivamente nos caminhos admitidos. Não autoriza arquivos privados/dados reais, ativação local, Meta/envios externos, Git de produto, gitlinks, worktrees/cópias, produção ou App Review; plano runtime próprio continua obrigatório.
- **Renewed approval trigger:** mudança material de WHAT/decisões/validação/escopo ou qualquer caminho não admitido.


## Proposed Data and API Contract — candidate v1.0

Esta seção e as cláusulas normativas seguintes tornam o candidato v1.1 revisável; Q-IG-01 tem evidência primária e confirmação humana do caminho de login, sem prova de concessão real. Os limites abaixo são políticas propostas do LeadsHug, não quotas ou garantias da Meta.

### Modelo físico candidato

| Owner | Modelo / chave | Preservação e transição |
| --- | --- | --- |
| Inbox | Contact: UUID local e buId; ContactIdentity: buId,platform,namespace,scopeReference,externalPeerId únicos | criar um contato por identidade inédita; WhatsApp pessoa/grupo separados; Instagram scope inclui contexto app/API e identidade estável da conta. FKscoped impede ligação cross-BU; não usar username como unique. |
| Canais | BusinessChannelIdentity: plataforma+namespace+externalResourceId único no LeadsHug, owner buId imutável | WhatsApp usa número próprio comprovado comum aos adapters; Instagram recurso devolvido pela autorização verificada no namespace correto. Conflicts abort antes de promover credencial; ownership não liberado por desconexão. |
| Canais | ProviderResourceIdentity existente com associação opcional/comprovada a BusinessChannelIdentity | preservar ID/provider/externalResourceId/owner/tombstone e unique de Message; não reinterpretar instância Evolution como phoneNumberId ou colapsar dedup. Identidade desconhecida não ganha mapeamento por conveniência. |
| Canais | BuChannel existente, ID mantido, tipo/adapter e vínculo ao recurso empresarial; remover unique(buId,type) como seletor de conta | restrição da conexão ativa por recurso/adapter; OAuth/credencial por vínculo/geração. APIs antigas por tipo só podem operar quando houver exatamente um vínculo compatível; ambiguidade409, nunca primeiro. Número próprio fica no recurso, BU.phone deixa de governar validação/dispatch. |
| Inbox | Conversation.contactId local obrigatório após backfill; unique(buId,contactId), mesmos IDs de conversa | Conversation.contact antigo fica somente como evidência legada/read-only, nullable para Instagram; não é fonte canônica nem endereço de dispatch após cutover. Uma identidade WhatsApp legada válida mapeia exatamente à conversa existente; incerteza/conflito bloqueia adoção e recebe disposição explícita. |
| Inbox/Canais | ConversationRoute: conversationId,businessIdentityId,contactIdentityId com unicidade/FKs da mesma BU | uma rota pode ter adapters WhatsApp diferentes comprovados; resposta captura também channelId concreto e generation. Peers Instagram de duas contas não são unidos. Não há operação de merge nesta entrega. |
| Inbox | Message e admissões/intents conservam IDs/proveniência e recebem referência opcional/versionada de rota | reader v1 apenas para recuperar/exibir receipts antigos com associação comprovada; novos writes somente contrato v2. Nenhum HTTP para reconstruir rota, nenhum side effect de backfill. |
| Canais | InstagramAuthorizationAttempt: UUID, BU, ator/sessionHash, nonceHash, expiry, state, generation e token candidato cifrado | nova tentativa atômica/idempotente, state10min, CAS antes de code exchange; code nunca persiste. Token candidato não sobrescreve ativo até identidade/ownership verificados. |

Compatibilidade admitida é delimitada: receipt reader v1 conserva fatos antigos e pode concluir localmente aceitos já conhecidos; não dispara novo envio e não sustenta dual-write. Colunas legadas só para preservação de evidência e compatibilidade explicitamente testada; consultas/novas gravações usam o modelo canônico. Adoção local ocorre com API quiescente sob plano posterior; inventário seguro deve incluir intenções ativas, conflitos de owners e referências sem prova. Conflito ou versão desconhecida aborta antes de escrita destrutiva. Nada é resetado, transferido ou unido automaticamente.

### Auth, projeções e endpoints candidatos

Todos os endpoints BFF resolvem tenant pela sessão e BU pelos grants atuais; ADMIN+ administra conexões; ATENDENTE+ lê/atende. POST exige anti-CSRF. Idempotency-Key UUID e replay/conflito duráveis são exigidos nas criações/confirmações OAuth e nos primeiros envios já contratados; resposta ordinária preserva as admissões existentes, sem prometer idempotência durável por request key após término. Respostas:401sem sessão,403papel insuficiente em BU conhecida,404fora do escopo,400payload inválido após autorização,409contexto/geração/conflito,429budget com Retry-After,503resultado externo inconclusivo. Erros nunca carregam payload bruto/URL/token. Nenhuma operação recebe URL externa arbitrária, WABA, credencial ou peer Instagram declarado pelo browser.

| Endpoint | Entrada e autorização | Resultado/efeitos |
| --- | --- | --- |
| GET /api/bff/channel-capabilities | sessão e grants; sem I/O externo | plataformas, login disponível e motivos seguros; configuração Instagram ausente desabilita essa capacidade, sem fallback WhatsApp. Parcial/malformada não anuncia disponibilidade. |
| POST /api/bff/business-units/:buId/instagram-authorizations | ADMIN+, CSRF, key; operation CONNECT ou REAUTHORIZE, channelId+expectedGeneration quando reautorizar | reserva tentativa durável e URL de autorização somente para hosts/redirect da instalação; TTL10min, consentimento explícito. Mesmo key/body replay; key com outro body409. |
| GET /api/bff/instagram-authorizations/:id | ADMIN+, mesma BU/ator quando tentativa em andamento | etapa, conta redigida, erro seguro; não consulta provider, não expõe state/code/token. |
| GET /api/bff/instagram-authorizations/callback | callback OAuth no contexto de sessão, state/nonce/session/expiry exatos; validar antes de usar code | CAS único; troca/valida recurso por client configurado; persistir candidato e ownership antes de inscrições; code/erro em query nunca logado; redirect303 sem parâmetros sensíveis e headers no-store/no-referrer. Expirado/ambíguo exige tentativa nova. Não é webhook de mensagens. |
| POST /api/bff/instagram-authorizations/:id/confirm | ADMIN+, CSRF, key, expectedGeneration; apenas recurso candidato devolvido pelo servidor | operador confirma conta legível; claim empresarial e provider identity atômicos, promover token por CAS; inscrição só depois de mapping durável. Conexão fica aguardando receipt real. |
| POST /api/bff/instagram-authorizations/:id/advance | ADMIN+, CSRF; recuperação explícita | até3requests de10s, budget40s sob lease60s; read-before-retry; inscrição ambígua não vira repetição automática de mutação. |
| POST /api/bff/instagram-authorizations/:id/cancel | ADMIN+, CSRF | encerra tentativa; preserva recurso/sideeffects parciais e token ativo anterior; não deleta histórico/BU nem revoga outro sistema. |
| GET /api/bff/business-units/:buId/channel-connections | ATENDENTE+, cursor local opaco, limit1..50(default20) | conexões identificadas por UUID+conta legível; página com continuação explícita, nenhum fan-out externo. Alias WhatsApp existente só preserva seu contrato, não escolhe entre múltiplos. |
| POST /api/bff/business-units/:buId/channel-connections/:channelId/verify | ADMIN+, CSRF e generation | observação explícita limitada/lease; autenticação e identity não comprovam recebimento. Receipt real depende de ingresso aceito. |
| POST /api/bff/business-units/:buId/channel-connections/:channelId/disconnect | ADMIN+, CSRF, expectedGeneration | desliga uso local, cerca geração/credencial e mantém tombstone/histórico; limpeza remota só quando sua propriedade/alcance for comprovada, senão reporta pendência. Não transferir recurso. |
| GET /webhooks/instagram | challenge e verify-token da instalação; sem sessão | handshake isolado, sem leitura de negócio ou promover canal pronto. |
| POST /webhooks/instagram | assinatura do app/produto correto sobre raw bytes, antes de conteúdo/DB de domínio | resolve recurso/server owner; normaliza mensagens textuais, echo/proveniência; commit e dedup transacionais. Eventos válidos fora da capacidade não inventam texto/destinatário. |
| GET /api/bff/conversations/:id/reply-options | ATENDENTE+; sem provider HTTP | rotas/vínculos da conversa, capacidades e política locais com versão/fingerprint. Conteúdo é autorizado antes da consulta. |
| POST /api/bff/conversations/:id/messages (existente, ampliado) | ATENDENTE+, CSRF; text e routeId/channelId/expectedGeneration/contextFingerprint | captura rota e destinatário server-side, passa pelo único OutboundService/admissões; contexto obsoleto409, sem enviar. Ack remoto e persistência local seguem resultados existentes. |

O único endpoint BFF de resposta continua POST /api/bff/conversations/:id/messages, com texto e contexto de rota obrigatório no cliente atualizado. Instagram aceita1..1000caracteres, WhatsApp mantém4096e seu parser/envelope atual; não reduzir o limite do WhatsApp por causa da nova plataforma. A resposta ordinária preserva concorrência entre replies existentes e claims single-use, com exclusão entre primeiro envio e reply, sem novo subsistema de request-key. O cliente impede duplo clique da mesma ação e não repete automaticamente envio incerto. Não criar POST /reply concorrente nem duplicar sender. A projeção de leitura devolve IDs locais/display, separando telefone WhatsApp e username Instagram; atualizar React/fixtures/expectativas no mesmo contrato. API v1/account_id e telefone continuam WhatsApp-only: filtrar accounts/canais/conversations e resolver messages/claim/release/post por identidade WhatsApp. Conta sem WhatsApp não aparece como número nulo usável no contrato legado. Typebot e webhook OUT não recebem Instagram por acidente.

### Limites de produto e confiança

- Instagram textual inicialmente entre1e1000caracteres; WhatsApp mantém4096e o envelope/parser atual. Novas rotas OAuth de payload pequeno limitam16KiB; não aplicar esse limite ao reply WhatsApp. Webhook Instagram até8MiB com no máximo1000updates por POST, conforme limite de batch documentado. Parser/gateway aplicam8MiB somente nessa rota; demais limites permanecem. Excedentes413antes de efeitos, sem slice/drop silencioso. Batch com falha parcial usa o mesmo replay/dedup das entradas já confirmadas; não retornar200para trabalho perdido.
- OAuth/troca de code, inscrição e send: um dispatch por claim, timeout10s/request e no máximo3requests externos por etapa administrativa; HTTP fora da transação. Máximo10tentativas de autorização/ator/hora e30/BU/hora persistentes. verify/advance usam lease por vínculo e cooldown10s; listagens não chamam provider.
- Token nunca no bundle, URL de retorno, docs, logs, histórico, eventos ou erros. Variáveis públicas exemplificam INSTAGRAM_CLIENT_ID, INSTAGRAM_CLIENT_SECRET, INSTAGRAM_WEBHOOK_APP_SECRET, INSTAGRAM_WEBHOOK_VERIFY_TOKEN, INSTAGRAM_API_VERSION e redirect/origin permitidos; os propósitos e a origem dos segredos seguem o contrato primário abaixo, sem fallback automático a META_APP_SECRET.
- Credential expiry vem do expires_in verificado na troca obrigatória curta→longa, armazenado com instante de aquisição e margem de60spara bloquear uso perto da expiração. Reautorização explícita renova a concessão; nada é chamado permanente. Nenhum cron/refresh automático ou token manual global nesta entrega.
- Política candidata de resposta: somente após INtextual assinada daquela conta/peer, até24hdo timestamp qualificado, com fence/lease atuais; read/echo/out/localcreatedAt não abrem janela. Esse teto é política conservadora do LeadsHug: a documentação primária admite a janela padrão24he uma exceção de até7dias para certos anúncios, que esta fatia não oferece. Usar o timestamp da ação original; não o entry.time de entrega. Timestamp ausente/inválido/futuro além de5minnão abre janela; timestamp antigo não a reabre por atraso. Não há HUMAN_AGENT ou extensão de janela.
- Frontend apresenta nome/username se conhecido, plataforma e conta atendida, nunca ID opaco como telefone. Nova conversa por telefone e templates permanece WhatsApp-only; DM Instagram nasce pelo ingresso autorizado. Compositor captura rota antes de digitar; mudança de contexto não apaga nem envia rascunho em outro destino.
- Medição pcv congelada abaixo: seed10milconversas, doze contas Instagram e um recurso WhatsApp por BU. Opções e lista não inspecionam todos os vínculos nem fazem HTTP por conversa. Nenhum benchmark foi realizado nesta etapa.

### Fontes primárias e limites da leitura

Coleção oficial Meta consultada em2026-10-23: [Instagram Login](https://www.postman.com/meta/instagram/folder/6raa77c/instagram-api-with-instagram-login), [pré-requisitos de mensagens](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api?entity=request-23987686-3fe78620-2258-44b6-893f-42d76c7200d7) e [envio de texto](https://www.postman.com/meta/instagram/request/scob1z4/text-message). Confirmam conta profissional, escopos de perfil/mensagens, início pelo usuário e referência opaca do destinatário; o exemplo inclui message_id no aceite. Não provam que o app do operador tem concessão ativa, nem entregam todo o contrato de OAuth/assinatura/renovação. O erro429foi a primeira observação da ferramenta web; a leitura direta posterior200 e o receipt primário abaixo encerram esse limite documental, sem usar terceiros como autoridade técnica.


## Normative architecture r1 integration — candidate v1.1

O parecer tático r1 em `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/architecture-r1-result.json` retornou changes_required. As resoluções abaixo são parte do contrato candidato que entrará em nova baseline/review; não mudaram código e não transformam o r1 em aprovação.

### IG-ARCH-R1-01 — rota, destinatário e contexto v2

A rota é imutável: não trocar seu contato, peer, recurso ou escopo. A rota deve provar simultaneamente Conversation.buId=Contact.buId=ContactIdentity.buId=BusinessChannelIdentity.buId=BuChannel.buId=ProviderResourceIdentity.buId; ContactIdentity.contactId=Conversation.contactId; ProviderResourceIdentity.businessIdentityId=ConversationRoute.businessIdentityId e a mesma igualdade para BuChannel; ProviderResourceIdentity.currentChannelId=BuChannel.id e provider=adapter. O namespace/escopo Instagram da identidade destinatária deve corresponder à conta/app da rota. Implementar essas relações por FKs compostas/unicidade e validação transacional centralizada das associações, com imutabilidade defendida no banco, sem depender somente de checks no controller.

Contexto de novos envios tem schemaVersion=2 e a tupla obrigatória: buId,conversationId,contactId,contactIdentityId,routeId,channelId,businessIdentityId,providerResourceIdentityId,adapterOrigin,generation,pairingEpoch,activeCredentialVersion,providerAccountReference. References imutáveis determinam o peer no servidor; nenhuma cópia de token/URL ou peer do browser entra no contexto. O fingerprint inclui a versão, a rota/tupla e os mesmos dados semânticos do pedido; cada claim conserva sua tupla. Antes do POST validar tupla e grant atuais sob as cercas já existentes; depois de ACK, reconciliação local aceita somente a identidade comprovada da tupla original, sem pedir token atual para apagar um fato passado nem aceitar outra conta.

Introduzir porta pequena ChannelEligibilityPolicy, resolvida junto à operação, para `reply`, `initial` e `automation`: supportedKinds continua no Channel; política/credencial/cadastro não viram métodos fictícios. OutboundService deixa de depender diretamente de OfficialChannelWindowPolicy; a implementação WhatsApp reutiliza a política existente e Instagram aplica24h/recebimento textual qualificado. Initial Instagram=false e automation Instagram=false, antes de reserva ou chamada Typebot. Não criar catálogo universal de plugins. Opções e dispatch usam o mesmo owner de política e mesmo contexto confiável.

Testes negativos obrigatórios: rota de outro contato na MESMA BU; peer de outra conta Instagram na mesma BU; canal/provider de outro recurso; versão desconhecida; mudança de geração; entrada concorrente por outra rota enquanto rascunho/envio usa a anterior. Todos recusam sem HTTP ao destinatário errado.

### IG-ARCH-R1-02 — cutover e leitura v1 por estado

Preservar request/canonicalRequest/requestFingerprint/selectedContext/ownerNonce/originalConversation (inclusive updatedAt)/deadlines/actor/receipt e IDs; não rehash, converter v1 em v2 ou tocar updatedAt de conversas durante backfill. O reader de contexto v1 só reconhece o shape exato existente (inclusive ausência do novo version tag); desconhecido não é v1 por fallback. Mapeamento v1→identidade local é associação comprovada externa ao receipt, sem escrever rota fictícia nele. Replay de mesma key com payload original é resolvido antes de elegibilidade atual; mudança de payload permanece409.

| Versão/estado existente | Ação permitida no cutover e recuperação | Proibição |
| --- | --- | --- |
| v1 PREPARED inicial/ordinário | quiescer API e cercar CAS; preservar exclusão até expiração original; depois encerrar/liberar somente pelo mecanismo local existente que prova ausência de dispatch. Nova intenção exige novo preview/key/contexto v2 | não enviar pelo reader v1, antecipar deadline, reescrever snapshot ou transformar em aceite |
| v1 SENDING sem receipt | manter exclusão/deadline original; após prazo, usar reconciliação local existente para AMBIGUOUS(initial) ou UNCERTAIN(ordinário) | não reenviar HTTP nem liberar por migração/restart |
| v1 AMBIGUOUS/UNCERTAIN | manter registro e exclusão; liberar somente com ação humana explícita de risco e deadline original, conforme contrato ST-CON-04 | migração não faz acknowledge automático nem zera lease/deadline |
| v1 EXTERNAL_ACCEPTED / EXTERNAL_ACCEPTED_LOCAL_BLOCKED | completar Message/slot localmente pelo mesmo owner, receipt/ator/snapshot e associação comprovada; se associação/grant/CAS não passar, conservar bloqueio e fatos | não repetir provider POST, apagar ACK ou recalcular originalConversation.updatedAt para forçar CAS |
| v1 terminal ou ordinário SETTLED | conservar fatos e replay/leitura; owner comprovado protege leitura; novo envio é v2 com nova key quando o owner já a exige; reply ordinário recebe nova admissão/nonce | não editar desfecho nem reabrir exclusão como se nunca enviado |
| versão desconhecida ou associação sem prova | registrar diagnóstico seguro e bloquear adoção/fluxo afetado antes de qualquer dispatch; intervenção explícita sob plano runtime | não inferir rota de BU.phone, do primeiro canal ou de coincidência de externalId |

Fixtures PostgreSQL devem cobrir todos os estados, snapshots/keys/deadlines antes/depois e zero chamadas de provider em recuperação v1. Opções de versão e migração mantêm v1 só para leitura/conclusão local; não há novo writer canônico v1 nem dual-write. IDs de mensagens/recurso e autoria/timestamps permanecem. Conflitos de owner ou duas conversas legadas para a mesma identidade não podem ser resolvidos por merge automático.

### IG-ARCH-R1-03 — cardinalidade nesta entrega

Uma BU admite no máximo UMA BusinessChannelIdentity WhatsApp durável, mesmo desconectada, e pode ter oficial+Evolution sobre esse mesmo número comprovado. Constraint parcial por buId para platform=WHATSAPP na identidade empresarial retida; segundo número retorna409antes de promover credencial, preservando owners/grants/histórico. Não filtrar só conexões prontas para decidir unicidade/ambiguidade. Múltiplas contas Instagram são admitidas e identificadas pelo vínculo exato.

Múltiplos números empresariais WhatsApp na mesma BU são fora desta entrega e exigem contrato próprio de API v1/Typebot/rotas; não criar primary/default ou multi-number UI antecipadamente. account_id continua BU e numero/telefone vêm do único recurso/identidade WhatsApp qualificados, nunca de um IGSID ou de BU.phone como autoridade. Typebot consulta/cria sessão e chama seu cliente apenas após provar plataforma WhatsApp, antes de trigger/session; keys legadas são preservadas, não generalizadas para Instagram.

### IG-ARCH-R1-04 — consultas e pcv congelados

- Inbox consulta em batch somente IDs de rotas/conexões relevantes à página de até50conversas; nenhuma leitura de toda a lista de conexões da BU e nenhum HTTP por conversa.
- reply-options faz lookup exato da rota/identidade da conversa: uma conta Instagram oferece um vínculo compatível; WhatsApp oferece no máximo oficial+Evolution do recurso único. Mais vínculos do que a cardinalidade ou referência incompatível é conflito, não truncamento. Quando houver mais de uma rota conhecida na conversa, usar a interação selecionada; se ausente, seleção explícita e catálogo paginado20até50, cursor opaco de até512caracteres, sem coletar todas as páginas no backend.
- start-options de abertura manual/primeira mensagem continua apenas WhatsApp, no máximo seus dois adapters; Instagram pronto não torna abertura por telefone elegível. Não manter take10silencioso sobre todos os tipos; catalogar conexões por página e resolver apenas as selecionadas. Verificar ambiguidade antes de readiness.
- EPS: seed10milconversas/BU em duas BUs/tenants, doze contas Instagram por BU+um recurso WA com dois adapters; leituras por ID e listagem50, cinco rodadas de20clientes após warmup. p95<=1000ms lookup/options e<=2000ms lista50; no máximo8queries de domínio por página e zero HTTP externo; plano de índice para peer/owner/rota, sem N+1. Registrar CPU/memória/DB, versões/imagens, amostra, percentis e query counts.
- FRC: navegação/mutações A→B→A e respostas em ordem inversa, duplo clique, popup cancelado, recarga/storage indisponível, chegada por outra conta com rascunho aberto; destino/rascunho/estado nunca atravessam contexto, zero POST no destino errado.
- BCI: nos owners com key durável (OAuth e primeiro envio), cinco ondas20requisições com mesmo key/payload: um claim/um POST/uma aceitação e mismatches409. Mais20replays de ingresso sobre a mesma mensagem: uma persistência, sem duplicar unread. Resposta ordinária preserva concorrência ordinary→ordinary e exclusão initial↔ordinary existentes: cada claim só é usado uma vez; o cliente é single-flight por ação, sem retry automático após incerteza. Não se promete um único ordinary admission global nem replay por key após estado terminal; retries locais conhecidos não repetem HTTP. Também20claims de recurso concorrentes de BUs/adapters distintos, um owner apenas. Barriers reais, não mocks de transação.
- RLS: sobre a mesma amostra, burst20readers+20mensagens sintéticas concorrentes por5rodadas; erro inesperado zero, nenhum bloqueio/deadlock pendente, preservação dos invariantes e dos budgets de leitura. Batch de1000updates textuais documentado: aceitar todos com dedup em até15sno teste isolado; replay sem novos efeitos. Execução é descartável com fake HTTP; não é SLA de provedor nem teste de carga no número real.

## Primary Instagram protocol reconvergence — r1

Fonte primária direta retornou200 em2026-10-23 após o acesso via ferramenta web ter retornado429. O receipt `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/primary-instagram-contract-r1.json` guarda URLs e hashes públicos, sem payloads operacionais. Não usar blogs/SDKs de terceiros como autoridade. Usuário confirmou o título Instagram Login no app existente; dados secretos serão configurados só na fase própria.

- Instagram Login usa client_id e client_secret do produto Instagram. Autorizar em www.instagram.com/oauth/authorize com redirect configurado e state; trocar code uma vez via POST api.instagram.com/oauth/access_token. Verificar lista de permissions retornada, exigindo apenas instagram_business_basic e instagram_business_manage_messages. Exigir envelope único válido; resposta ambígua/inválida falha sem escolher primeiro.
- Troca inicial também captura o user_id de autorização no seu namespace; não presumir que seja o mesmo valor de outros campos. Trocar token curto por longo via graph.instagram.com/access_token e ler expires_in. Ler /me?fields=user_id,username com o token ativo candidato: user_id identifica IG_ID da conta profissional e o entry.id de webhook; id app-scoped é diferente e não o substitui. Persistir a associação de forma tipada/comprovada, sem converter IDs para Number.
- API Graph desta entrega configurada explicitamente em v26.0, conforme exemplos primários atuais; ausente/malformada desabilita Instagram, sem fallback à versão WhatsApp. Token longo não é permanente; reautorização explícita usa mesma regra e só promove recurso igual. Refresh automático não está incluído; expirado/revogado pede reautorização e bloqueia envio.
- Inscrever o campo messages na configuração do app e ativar /IG_ID/subscribed_apps em graph.instagram.com para essa conta depois do mapping local. Inscrição no app e na conta são verificações distintas. Ler somente estado de inscrição da conta própria; mutação ambígua exige read-before-retry, sem tocar subscriptions de outros apps.
- GETchallenge usa token de verificação próprio. POST exige X-Hub-Signature-256 e HMAC SHA256 nos bytes brutos com o segredo explicitamente configurado para o app que entrega o webhook. O guia de setup aponta o App Secret do app; não presumir que seja o client_secret OAuth do produto nem fazer try-all/fallback a segredos WhatsApp. Teste negativo cruza os dois propósitos e recusa segredo errado. Corpo/parser/gateway seguem limites/assinatura antes de trust de dados.
- Para IN, entry.id e recipient.id precisam identificar a mesma conta empresarial verificada; sender.id é o peer IGSID. Para OUTecho, orientação é inversa: sender.id é a conta, recipient.id é o peer; message.mid qualifica o ID de mensagem. is_echo/is_self/is_deleted/unsupported/read/reaction não abrem janela ou simulam entrada textual. Timestamp da mensagem é em ms, não entry.time nem receivedAt local; clamp/falha fechada conforme política.
- Responder texto por POST graph.instagram.com/v26.0/IG_ID/messages com recipient.id resolvido da rota. Exigir message_id válido e compatibilidade da referência destinatária na resposta; ACKsemID ou timeout permanecem incertos. Só uma IN elegível cria contexto de resposta. Teto conservador24h; nenhum caso de CTD7dias ou HUMAN_AGENT é habilitado.
- Setup/testes controlados devem respeitar o nível de acesso e os papéis exigidos pela Meta para os recursos do operador. Disponibilidade de produto/conta não é aprovação de Advanced Access. Usuários externos, publicação e App Review não são autorizados por este TODO; a prova real só é aceita após recurso/testador elegível, app/conta inscritos, callback200, assinatura real e receipt persistido.


## Planning Finding Resolution Ledger — architecture r1

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-ARCH-R1-01 | Integrated | useful | partial | project | n/a | tupla v2, invariantes de contato/conta/recurso e porta de política congelados no candidato; testes negativos exigidos, sem código ainda |
| IG-ARCH-R1-02 | Integrated | useful | partial | project | n/a | matriz por estado v1, snapshots/fingerprint/CAS e recuperação zeroHTTP; nada reescrito no produto |
| IG-ARCH-R1-03 | Integrated | useful | yes | project | n/a | limite de um recurso WA por BU e múltiplas contas Instagram, partial unique e preservação APIv1/Typebot; sujeito à aprovação do contrato |
| IG-ARCH-R1-04 | Integrated | useful | partial | project | n/a | batch/cardinalidade/paginação exatos e thresholds EPS/FRC/BCI/RLS; ainda sem medição |

Essa disposição resolve a proposta documental para a nova rodada; não muda o outcome histórico changes_required do r1 e não prova a implementação. Nenhum finding foi dispensado ou tratado como waiver.

## Planning Finding Resolution Ledger — architecture r2

| Finding ID | Resolution | Status | Evidence |
| --- | --- | --- | --- |
| IG-ARCH-R2-01 | Integrated | closed | chaves duráveis OAuth/initial, concorrência ordinary preservada e BCI delimitado; correção inspecionada pelo reviewer |
| IG-ARCH-R2-02 | Integrated | closed | limites Instagram separados de WhatsApp4096/parser; correção inspecionada pelo reviewer |

Parecer terminal r2go, estático e sem execução; receipt architecture-r2-result.json. Crítica r2go e guards de coerência/escopo concluídos posteriormente, com receipts próprios; nenhuma autorização de implementação.

## Normative critique r1 integration — candidate v1.3

As três correções abaixo integram o parecer changes_required de critique-r1-result.json; nenhum teste/código foi editado. Baseline v1.3 publicada em f4891ba1 e crítica r2go concluída posteriormente; ver receipt próprio.

- IG-CRIT-R1-01: seis arquivos exatos de regressão admitidos acima. conversation-start e dispatch-admission deixam de ter freeze final byte-exact, mas hashes originais continuam fatos de baseline. Só fixtures canônicas, lookup qualificado e contextos versionados podem ser adaptados; preservar todos os cenários, asserts, contadores e evidência causal. Casos v1 deliberados continuam como cutover, não writers novos. Os outros quatro arquivos recebem apenas fixtures, exceto historico que também testa a fronteira explícita abaixo. Não interceptar Prisma nem criar writer/trigger legado para satisfazer fixtures obsoletas. A política v1.1 de preservação governa essas exceções; as observações anteriores não são apagadas.
- IG-CRIT-R1-02: GET /api/bff/business-units e seu detalhe preservam a projeção legacy channels/canais apenas WhatsApp, no máximo os dois bindings compatíveis do recurso empresarial durável único. Resolver bindings atuais/proveniência antes de readiness; desconectado não é apagado para esconder ambiguidade. Histórico de bindings aposentados não vira catálogo implícito. Incompatibilidade/cardinalidade excedida é conflito explícito, sem take/slice silencioso. me.controller.ts é admitido somente para essa projeção limitada; grants/criação e outras responsabilidades ficam preservadas. A UI Instagram usa channel-connections paginado, sem hidratar toda a conta via business-units. Testes provam zero contas Instagram nessa projeção, inclusive com12contas, consultas limitadas e ausência de HTTP externo.
- IG-CRIT-R1-03: Consultar legado (lista, drilldown e CSV) é WhatsApp-only. historico.service.ts filtra por identidade WhatsApp qualificada, usa telefone do peer e número empresarial do recurso comprovado único, nunca Conversation.contact/BU.phone como autoridade. BU só Instagram não produz linha telefônica; BU mista exclui Instagram; IGSID numérico igual a E.164 não colide nem revela conversa. Preservar filtros, paginação, grants e histórico WhatsApp; os testes de historico cobrem esses três casos sem enfraquecer os anteriores. Instagram continua na caixa de Atendimento; Consultar multicanal exige contrato próprio futuro, sem Web/controller novos nesta fatia.
- Webhook de saída para parceiro: owner atualmente sem import/call nos fontes públicos verificados. Não implementar nem registrar novo caller Instagram; nenhum caminho novo para esse serviço dormente, nenhuma expansão de contrato parceiro. Typebot continua bloqueado antes de trigger/session/client para Instagram.

| Finding ID | Resolution | Status | Evidence |
| --- | --- | --- | --- |
| IG-CRIT-R1-01 | Integrated | closed by critique r2 | seis caminhos exatos e política de preservação v1.1 |
| IG-CRIT-R1-02 | Integrated | closed by critique r2 | produtor BU legacy limitado e Instagram paginado |
| IG-CRIT-R1-03 | Integrated | closed by critique r2 | Consultar WhatsApp qualificado, testes de isolamento/collision |

## Approval Readiness Evidence — v1.3

Arquitetura r2 e crítica r2 retornaram go. Crítica revisou as sete lentes e fechou os três findings r1. Coherence e scope-drift retornaram go; nenhuma das23seções materiais mudou após a baseline revisada. Authority preflight é estrutural, não execução. Full diff guard/runtime/API/Meta/provas físicas ainda não foram executados nesta preparação e permanecem para suas fases próprias. APROVADO do contrato não autoriza leitura privada, banco real, callbacks, envio externo, Git de produto, produção ou App Review.

Authority preflight final: `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/authority-preflight-final-r4.json`, outcome preflight-go, execution_authority_granted=false. Naquele preflight, aprovação humana permanecia pendente; ela foi recebida posteriormente e registrada em approval-execution-cp1.json.

## Execution Checkpoints — approved v1.3

| Checkpoint | State | Owner / next proof |
| --- | --- | --- |
| CP1 Identity/route/state cutover | accepted r8 | cp1-r8-acceptance.json; source companion validated and proved, no Instagram runtime claim |
| CP2 OAuth/ingress | in progress; not accepted | source18 full398unit/555E2E GREEN +affectedR5 reconciled; ROOT02/SUBREC02 resolvedqualified; primary/precontroller remainopen |
| CP3 Channel/policy/consumers | test-first lane ready | two new admitted specs and externalHTTP fake only; shared sender/acceptance next |
| CP4 UI/CI/browser | pending | profile handoff for CI/runtime tooling |
| CP5 independent audits | pending | consolidated source and ALL evidence |
| CP6 local real rollout/proof | pending separate plan | approval later; no real runtime/private inputs now |

## CP1 execution notes

- Aprovação original conferida contra o seal v1.3 antes de alterar status; authority normal go em authority-execution-cp1.json e roteamento de código/validação go.
- Root atua em Strategic/CTO para documentação; `/root/instagram_cp1_executor` é o único writer de produto, gpt-6-luna medium, Operational/Coder. Nenhum worktree, cópia ou Git de produto.
- SCOPE-01 documental concluído: três decisões Accepted e todos os alvos canônicos consolidados, com receipt `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/canonical-consolidation-cp1.json`. Lifecycle exit0 após corrigir a forma das referências de evidência. Isso não comprova migração/schema ou Instagram operando.
- Profile classifier não catalogava decisions/** como regra explícita: resultado review-required adjudicado pelo SCOPE-01 e caminho exato já aprovado, sem ampliar escopo ou alterar o classificador; receipt próprio.
- Initial CP1 handoff: code implementation started with RED/GREEN and PostgreSQL proof pending. Subsequent attempts and their remaining limits are recorded below; other checkpoints remain open.

CP1 RED report: executor ran `bash scripts/test-channels-local.sh api` on disposable synthetic DB;28baseline migrations/lint/build passed,34/35unit files passed, three new context cases failed on missing v2/exact-v1 parser exports. Report in `evidence/cp1-red-reported.json`; GREEN/schema/ownership/route/state proof remain pending.

CP1 intermediate report:30migrations, lint/build and36unit files/373tests passed according to the executor. The subsequent integration attempt remained RED (389passed/69failed;14files) on an earlier source snapshot. Synthetic cleanup, obsolete peer fixtures and residual compound lookups are being corrected. Receipt `evidence/cp1-progress-reported.json` is progress evidence only; final stable-source validation, seeded migration preservation and independent checkpoint review remain pending. No API/ALL, cutover or delivery acceptance is claimed.

CP1 validation dependency: after the current full API attempt ends and the sole coder stops, serialize an Operational/DevOps handoff for a bounded Instagram diagnostic target in the existing safe runner and its parity self-test. These exact paths are already admitted. Preserve the complete api/all/CI gates, positive public mounts, synthetic configuration, mandatory parity guard and cleanup; accept no arbitrary host paths or commands. The diagnostic is intermediate evidence only and never replaces VAL-05. This advances validation support needed by CP1 within the approved objective; it does not advance runtime/Meta authority or functional scope. Resume the sole coder only after DevOps releases the product-code writer slot.

CP1 diagnostic handoff completed: `api-instagram` retains the complete API/ALL gates and runs only fixed Instagram specs after the shared setup/lint/build/unit stages. DevOps is terminal. The complete synthetic log proves30migrations,373unit cases and8Instagram e2e cases passed; root independently checked its summary/hash and all33API source hashes remained frozen. Receipt `evidence/cp1-diagnostic-green.json`. This is partial proof for SCOPE-02/DOD-01,02/VAL-01,02, not complete acceptance: the broader migration cohort, resource-claim paths and the full API regression result remain open.

## CP1 Finding Resolution Ledger — adherence r1

Independent no-context review returned `changes_required`; schema-valid result and deterministic merge are recorded in `evidence/adherence-cp1-r1-{result,merge}.json`. All33API source hashes and the governing TODO hash matched before/after review. These are corrections to approved identity, association, preservation and regression obligations; no new functional scope or runtime authority is introduced. The unchanged source is undergoing a complete captured API rerun; repairs start only after that validator releases the writer slot.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP1-R1-01 | Integrated | useful | yes | project | n/a | closed by r2: freeze qualified peer/contact ownership behind immutable routes; negative PostgreSQL mutations required |
| IG-CP1-R1-02 | Integrated | useful | yes | project | n/a | open: enforce provider attachment equality with channel BU/resource/adapter; preserve explicitly unmapped legacy rows |
| IG-CP1-R1-03 | Integrated | useful | yes | project | n/a | open: central transactional provider-proved WhatsApp resource claim before verification/credential promotion; concurrent cross-adapter/BUs and retained-owner proof |
| IG-CP1-R1-04 | Integrated | useful | yes | project | n/a | closed by r2: manual start must reuse canonical WhatsApp PERSON conversation before readiness and under creation fence; real service regressions |
| IG-CP1-R1-05 | Integrated | useful | yes | project | n/a | closed by r2: append-only business ownership/tombstone; deletion/reclaim and disconnected cardinality proof |
| IG-CP1-R1-06 | Integrated | useful | yes | project | n/a | closed by r2: one explicit person-address grammar; invalid legacy address/collision abort preserves all original facts |
| IG-CP1-R1-07 | Integrated | useful | partial | project | n/a | open: two bulk fixtures need canonical contact IDs; preserve15k/60row datasets and all EXPLAIN/query/HTTP assertions; locate remaining API failure |
| IG-CP1-R1-08 | Integrated | useful | partial | project | n/a | closed by r2: actual pre-upgrade cohort must include both adapters/groups/incomplete provenance/all persisted states; compare all original rows and safe aborts |

At the r1 handoff, all eight findings remained open for implementation and fresh re-review; current per-ID dispositions are updated by r2 below. Performance is unmeasured; no full API/ALL or CP1 acceptance is claimed. CP3 still owns v2 dispatch wiring, state-specific v1 local-only recovery and the remaining consumers; CP2..CP6 stay required as already approved. No finding has been waived or routed away from this delivery.

Complete captured API attempt20261023-01: exit1;36unit files/373cases passed;34of35e2e files and462of464cases passed. Both remaining failures are the canonical contactId bulk-fixture defects in IG-CP1-R1-07; the corrected isolated migration and cross-account route tests passed. Receipt `evidence/cp1-full-api-before-repair.json` records the full synthetic log hash and the root-observed summaries. Both validator and reviewer became terminal before the coder resumed as sole writer for findings01..08; no concurrent source changes were used as proof.

## CP1 Finding Resolution Ledger — adherence r2

Fresh no-context review returned `changes_required`; result/merge in `evidence/adherence-cp1-r2-{result,merge}.json`. Frozen35source hashes and TODO matched before/after. R1-01/04/05/06/08 are closed for this checkpoint's source/preservation proof; R1-02/03 remain open. R1-07 fixture preparations are repaired but full API acceptance remains open. No waiver or expanded functional scope.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP1-R1-02 | Integrated | useful | yes | project | n/a | open: deferred checks must validate final persisted rows, not obsolete queued NEW; actual official confirmation regression |
| IG-CP1-R1-03 | Integrated | useful | yes | project | n/a | open: administrative verification must claim freshly provider-proved resource before trust for either adapter; no BU.phone authority |
| IG-CP1-R2-01 | Integrated | useful | yes | project | n/a | open: align WA business scope across real claim and route CHECK/FK; positive route using actual owner required |
| IG-CP1-R2-02 | Integrated | useful | yes | project | n/a | open: renewed provider remains explicitly unverified/noneligible until its own proof; never prefill its business identity from retained channel |

The complete captured API rerun is RED:36unit files/379cases passed;27of35e2e files and453of470cases passed,17cases failed. Root observed the full summary and all35source hashes remained unchanged; `evidence/cp1-r1-repair-full-api-red.json` preserves exact failure headings/log hash. Repair transition defects and restore compatibility rather than weakening regression assertions. Business-resource tombstone retention is distinct from retaining a channel row; existing detach/history behavior and canonical phone response projections must remain coherent without rewriting stored legacy data. The next sole-writer handoff follows terminal review and validator states. CP1 and the entire Instagram delivery remain incomplete.

Serialized r2 repair handoff: `evidence/cp1-r2-repair-handoff.json`; prior executor, reviewer and validator terminal before resuming the sole coder. New production-path regressions must run as causal RED before their fixes. Full API GREEN and fresh CP1 review remain required.

CP2 preparation only: `evidence/cp2-test-first-handoff-plan.json` derives sixteen OAuth/ingress test obligations from the approved v1.3 clauses. It grants no additional scope and records no executed case; CP2 execution still depends on accepted CP1.

CP1 r2 causal RED established before production repairs: `evidence/cp1-r2-causal-red.json`. The corrected actual lifecycle suite reached all seven intended defects, with379unit cases passing and7of19Instagram e2e cases failing. Original35source hashes were preserved through the pre-fix seal; the new lifecycle spec hash was independently matched. Earlier lint/fixture-only failures are explicitly excluded as product RED evidence. Product repair follows this seal; GREEN and fresh review remain pending.

CP1 r2 targeted GREEN: `evidence/cp1-r2-repair-diagnostic-green.json` records root-observed30migrations,379unit cases and19Instagram integration cases passing. `cp1-r2-repair-source-manifest.json` freezes36exact public paths; the37immutable inherited public paths still match their original hashes. Complete API validation and fresh r3 adherence run against this same source freeze. No code edits until both are terminal; no CP1 or delivery acceptance yet.

## CP1 Finding Resolution Ledger — adherence r3

Fresh no-context r3 returned changes_required, strict schema merge passed. All36source hashes and frozen TODO matched before/after. R1-02/R2-01/R2-02 original defects are closed; R1-03 remains open for contradictory proof about an already trusted current Evolution instance. R1-07 remains open for complete API GREEN. The previous five r2 closures remain supported.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP1-R1-03 | Integrated | useful | yes | project | n/a | current-instance contradictory proof must durably invalidate trust; official wrong candidate still preserves old credential |
| IG-CP1-R1-07 | Integrated | useful | partial | project | n/a | canonical scope/proved phone fixtures, preserved assertions and held-request finally cleanup; API remains RED |
| IG-CP1-R3-01 | Integrated | useful | yes | project | n/a | claim create durably before external effect; connecting/ambiguous retry observes rather than repeats create |
| IG-CP1-R3-02 | Integrated | useful | yes | project | n/a | staged unlink retains exact managed resource cleanup fence through deletion/recreate |
| IG-CP1-R3-03 | Integrated | useful | yes | project | n/a | preserve channel/attempt quarantine and later correct-proof recovery using durable owner |
| IG-CP1-R3-04 | Integrated | useful | yes | project | n/a | assert actual successful contender, one winner/rejection and unchanged losing tuple |
| IG-CP1-ROOT-01 | Integrated | useful | yes | project | n/a | root exact-source cross-check: detached current staging bypasses existing503/safe metadata branch; causal product test required |

Root-observed full API is RED:379unit cases pass;34of36integration files and474of477cases pass,3case failures plus1suite-hook timeout. Receipt cp1-r2-repair-full-api-red.json retains exact log hash/headings and36source/TODO freeze checks. No source edit occurred until both reviewer and validator became terminal. Corrections stay within approved identity/lifecycle/ingress and regression obligations. No waiver or new functional scope.

The explicit unverified/noneligible state is approved WHAT; currentChannelId=NULL was an implementation choice. A simpler explicitly unproved attachment may be evaluated if DB guards still enforce BU/provider/instance/current-operation consistency, block every trusted/ingress/send path before fresh proof and never populate the candidate business owner from the retained channel. Preserve legitimate metadata/retry and cleanup contracts. Prove any chosen representation through actual lifecycle/ingress regressions and fresh review.

Serialized r3 repair resumed only after both frozen lanes were terminal; `evidence/cp1-r3-repair-handoff.json`. Root remains documentation owner and the existing coder is sole product writer. No new human approval is required for these corrections inside approved WHAT; real runtime/private/Meta authority still requires its later concrete plan.

CP1 r3 causal RED established before production edits: `evidence/cp1-r3-causal-red.json`. All production paths remained unchanged; only the admitted lifecycle spec changed.379unit cases pass,4of23Instagram cases fail on quarantine outcome, repeated create, lost cleanup fence and pending message200instead of503. The receipt distinguishes the first failed quarantine assertion from dynamic exploit proof; all subsequent no-content/unread/realtime/bot and recovery assertions must execute in GREEN.

CP1 r3 targeted GREEN: `evidence/cp1-r3-repair-diagnostic-green.json` records root-observed379unit/24Instagram e2e passes on37frozen public paths. All37immutable inherited public paths still match. The implementation retains explicit detached staging and adds tightly fenced current-stage metadata/retry handling; source acceptance is pending independent r4 and the complete API result. No source edits until both lanes become terminal.

## CP1 r4 invalidation and serialized recovery

The fresh r4 reviewer returned terminal `changes_required`; its package was invalidated after four source mutations while review remained active. `evidence/cp1-r4-freeze-breach.json` preserves the original and observed hashes. The executor acknowledged the error and became terminal. No edits were reverted to hide the drift. Its later targeted GREEN (379 unit/24 Instagram cases) is on different bytes from the complete API RED (477/482 e2e cases,34/36 files), and neither constitutes acceptance of current source. `cp1-r4-terminal-source-baseline.json` seals the actual retained37paths for the next repair.

Qualified r4 observations on its originally inspected bytes support the original-defect repairs for R3-01/03/04 and ROOT-01, but confer no acceptance on changed files. R1-03 remains open for a previously received/CONNECTED channel that cannot recover its quarantined current attempt after correct proof; R3-02 remains open for stale unlink deleting a newer generation without cleanup; R1-07 still requires complete stable-source API GREEN. R4-01 is Integrated, useful, project-level and a release-blocker: preserve invalidated evidence, establish a new freeze, validate it and obtain fresh review. No shared Delphi policy change or new scope is authorized.

A fresh bounded routine executor replaces the terminal sticky executor under the same single-writer contract and approved WHAT. Root owns Foundation documentation. The next lane first adds actual residual transition RED cases, then repairs only admitted current lifecycle/fixture code, captures targeted results and becomes terminal. Root alone authorizes the subsequent frozen complete API run and fresh review; that validation lane cannot edit sources. CP2–CP6 remain mandatory and pending. Real runtime, private inputs, Meta and full private diff guard remain excluded until later concrete plan approval.

CP1 residual recovery RED/GREEN: `evidence/cp1-r4-residual-causal-red.json` records a clean targeted RED after real prior receipt/CONNECTED and after the actual stale unlink/renewal interleaving. Earlier harness iterations remain qualified in separate receipts and are not suite acceptance. `cp1-r4-residual-diagnostic-green.json` records379unit/25Instagram e2e passes after the repair. The scheduling wrapper returns the unchanged actual helper/DB snapshot and fabricates no transaction/constraint results.

The residual executor is terminal. `cp1-r4-residual-frozen-source-manifest.json` seals all37public sources. Root will start a separate validation-only complete API lane and fresh no-context r5 reviewer. Neither lane may edit source or TODO; repairs require a later explicit root handoff after both lanes terminal. R4-01 remains open until that new stable proof is collected. All remaining checkpoint, physical and independent delivery gates stay mandatory.

## CP1 Finding Resolution Ledger — adherence r5

Both frozen lanes are terminal. Fresh r5 source review preserves prior source closures and closes current quarantine-recovery, stale-unlink, single-create, valid quarantine, concurrency-winner and metadata/retry defects. Root matched all37source hashes and frozen TODO after the complete API runner. `evidence/cp1-frozen-full-api-green-r5.json` records30migrations, lint/build,379unit and483integration passes, with disposable cleanup; it resolves R1-07 and the remaining R4-01 evidence requirement. The invalidated r4 history remains intact. CP1 is not accepted because the distinct R5-01 observation limitation remains.

R5-01 is Integrated, useful and project-level. Its malformed-success-to-absence behavior predates this work and the protected client/spec remain byte-exact. Root classifies it as a release-blocker for the current staged cleanup guarantee: an inconclusive provider observation cannot release the retained cleanup fence merely because the domain received null. This is a subordinate concretization of the same cleanup/identity objective, not permission for general Evolution hardening. No follow-up waiver is inferred.

## Proposed bounded source admission — Evolution observation companion

Status: proposed, unapplied, awaiting independent proposal review and human path validation. Existing approved WHAT and private/runtime exclusions remain unchanged.

The candidate in `evidence/evolution-observation-companion-proposal.json` and its exact `evolution-observation-companion-proposed.diff` admits only `api-app/src/integrations/evolution/evolution.client.ts` and `api-app/src/integrations/evolution/evolution.client.spec.ts` for strict inventory-shape/ambiguity interpretation and unit regressions. Existing response projection and confirmed absence stay compatible. No new request, fallback, send/auth/signature behavior, dependency or real-runtime action is included. The already-admitted lifecycle spec must prove malformed actual-adapter observation retains CLEANUP_PENDING with zero new creates and that valid absence/deletion enables recovery.

The current immutable-path rows and preservation policy are NOT lifted by this proposal. If validated, root will record the limited exception while retaining original hashes as baseline facts; the remaining inherited files stay byte-exact. Test-first causal RED/GREEN, frozen complete API and fresh review remain required after implementation. No code change can start on these paths before validation.

## Observation companion critique — bounded reconvergence

The independent proposal critique found the guard itself statically correct, but requires proposal refresh before asking human validation. IG-EVOCOMP-01 is a concrete existing caller transition: ERROR/CLEANUP_AMBIGUOUS can retain pendingCleanup fields after the prior provider was reconciled, while INITIAL cannot resume and RENEW refuses. Root classifies this as a release-blocker for the same staged cleanup guarantee and will first repair the already-admitted service/lifecycle paths, without asking permission for work already authorized. This discovery does not lift the protected adapter files.

IG-EVOCOMP-02 and03 are release-blockers to proposal readiness, not claims of executed patch failure: strengthen independent name/connectionStatus and omitted/null projection tests; identify WhatsApp/Evolution pairing precisely and preserve valid nonmatching inventory absence. Actual-adapter tests must use synthetic config and intercept only the exact HTTP boundary with real Response parsing, retain real authenticated service/BFF and PostgreSQL behavior, restore hooks/env/globals in finally, and prove both safety and eventual explicit recovery/single create. Both retained-renewal cleanup and post-unlink recovery are required.

Next source phase owns only channels.service.ts and instagram-lifecycle.e2e-spec.ts for the caller transition. Protected client/spec remain unchanged until later explicit validation. Preserve r5 full-GREEN as its exact historical source receipt; after caller edits, current-source proof must be recaptured before further acceptance.

## CP1 r6 caller recovery — frozen validation

The clean causal RED in `evidence/cp1-caller-r6-causal-red.json` reproduced exactly one lifecycle failure through the actual EvolutionHttpClient/Response boundary; the earlier run1 remains qualified because of fixture teardown noise. `cp1-caller-r6-targeted-green.json` records379unit and26Instagram cases passing after the admitted caller repair. It retains the same reservation, generation, pairing epoch and attempt, resolves the exact managed cleanup tuple and advances to RESERVED_NEVER_CREATED before one create; new staging remains unproved and ingress blocked. All37immutable inherited public paths still match.

Caller, lifecycle test, all other37sources, TODO and proposal revision3 are now frozen for separate complete API validation and a fresh independent companion/caller critique. Revision3 only updates the caller dependency/proof status after the actual repair; revision2 strengthened the proposed unit cases and clarified absence semantics. The adapter diff remains unapplied. No CP1 acceptance, path exception, private/runtime permission or delivery claim follows from targeted GREEN.

## CP1 companion r2 result and serialized stale-failure repair

Both r6 frozen lanes are terminal and source hashes matched. `cp1-caller-r6-full-api-green.json` records379unit/484integration passes on those exact bytes; no source repair occurred during either lane. The independent critique supports normal same-attempt recovery and proposed tests/wording02/03, but finds an inherited unfenced catch that can regress a later holder after lease expiry (IG-EVOCOMP-R2-01). Ordinary10s HTTP timeouts do not bound asynchronous authorization/database waits or suspension beyond45s. This is static evidence until a real PostgreSQL interleaving proves it.

Root routes that finding as a release-blocker for the same recovery guarantee, on the two already-admitted caller/spec paths. Next writer must capture causal RED, then persist ambiguity only under exact current tuple/ownership/live lease fencing; lost/stale ownership must not rewrite later RESERVED_NEVER_CREATED, terminal or cancelled state or reopen cleaned resources. No protected path admission or parallel provider probe is authorized. The old r6 proof is preserved, and new full/API review is required after repair.

R7 root source cross-check identified IG-CP1-ROOT-R7-01 before terminal acceptance: the new fenced provider-error mutation still needs post-call authorization revalidation. The sole writer agrees the controller contract applies. Finish the active targeted run without editing; then add actual authenticated BFF/PostgreSQL revoked-grant/provider-error causal coverage before the narrow service correction. A live lease alone does not authorize actor writes, and revalidation failure must propagate without mutating newer facts. The scope remains the two already-admitted paths.

## CP1 r7 final caller freeze

`cp1-caller-r7-causal-red.json` proves the actual stale holder overwrote a later recovered attempt; `cp1-caller-r7-auth-causal-red.json` proves failure-fact mutation after actual passwordChangedAt session invalidation. Earlier response-only, setup and build attempts remain separately qualified. `cp1-caller-r7-targeted-green.json` records30migrations, lint/build,379unit and28Instagram integration passes after the admitted repairs. The ambiguity transaction locks prior provider→BU→channel, verifies exact pending tuple/live lease/compatible attempt, and post-provider-error revalidation propagates actor denial before mutation. Stale revalidation lies outside provider catches. Same reservation, exactly-one create and unproved ingress guarantees pass.

All37immutable inherited public hashes match. Only the two admitted caller/test paths changed since r6. All37current sources, protected client/spec, governing TODO and proposal revision4/diff are frozen for separate full API and fresh complete affected critique r3. Protected diff remains byte-identical to revision2 and unapplied; actual-adapter malformed observation proof on both paths still requires later human admission. No code, TODO or proposal edits until both lanes terminal; validation-only lane cannot repair. No CP1 or delivery acceptance.

## CP1 r7 validation complete; bounded source admission ready

Both frozen lanes are terminal. `evidence/cp1-caller-r7-full-api-green.json` records379unit/486APIintegration passes on the exact frozen r7 source; all37sources, protected2, controller, TODO/proposal/diff and37immutable inherited rows matched. Fresh `evolution-observation-companion-critique-r3-result.json` found no material issue and supports closure of the stale-failure and revoked-session caller findings. Earlier qualified attempts and invalidated r4 history remain intact. This closes the currently authorized caller work, not CP1 or the Instagram delivery.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate rule level | Candidate rule ID | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| IG-EVOCOMP-R2-01 | Integrated | useful | yes | project | n/a | Exact live operation fence and compatible attempt guards prevent late failure from regressing newer facts; real takeover RED/GREEN, current full API and independent r3 support closure |
| IG-CP1-ROOT-R7-01 | Integrated | useful | yes | project | n/a | Post-provider-error revalidation propagates denial before ambiguity transaction; actual BFF passwordChangedAt revocation RED/GREEN, full API and r3 support closure |

`evidence/evolution-observation-companion-admission-ready.json` binds the exact protected two-path diff to its review and current caller proof. The read-only apply check passed again. No exception has been granted or applied: original immutable rows and hashes remain authoritative. IG-CP1-R5-01 remains open pending explicit human path validation, then actual adapter RED/GREEN and both real-boundary cleanup regressions, frozen full API and fresh affected review. CP2..CP6, UI/browser, ALL/pcv/security/TQA/cutover/final review and separately approved real runtime/Meta proof remain mandatory.

## Limited Evolution source admission — user validated

User answered **“Validar os dois arquivos”** to admission-ready question `call_4056c67b34054c88bcbe41f341ffb3b8`. `evidence/evolution-observation-companion-user-validation.json` binds reviewed proposal/diff, original source hashes and expected candidate hashes. Only the two client/spec mutation restrictions are lifted for the reviewed observation guard/tests. Original v1.3 business decisions, other35immutable rows, six regression-companion restrictions and private/runtime/Meta/Git exclusions remain unchanged. Original v1.1 evidence and all prior review/RED/GREEN history remain intact.

Execution is test-first: real-adapter retained-renewal and post-unlink malformed observation RED with client/unit unchanged; then unit RED; then exact reviewed guard and GREEN. Stable tuple checks apply to an existing replacement reservation; post-unlink recovery must never resurrect a cancelled/deleted channel or attempt. No DB result fabrication, weakened prior scenario, new HTTP/fallback or general Evolution refactor is authorized.

After targeted terminal proof, freeze39sources and require full API plus fresh complete CP1 adherence. CP1 acceptance enables CP2 and is not a stopping point; all CP2..CP6 and delivery criteria remain required.

## CP1 r8 actual observation guard — frozen complete validation

User-admitted client/spec equal the exact reviewed candidate hashes. The clean product RED reached four actual authenticated BFF/PostgreSQL CLEANUP_PENDING→CLEANED violations with the original client; the separate unit RED reached11malformed/ambiguous response failures. `evidence/cp1-observation-r8-targeted-green.json` records395unit and32Instagram passes after the guard. All qualified fixture/query/projection/count attempts remain separately retained; none is presented as product failure or acceptance. Tests fake external HTTP only, reflect inventory truth, verify no deletion/create after malformed observation, and prove explicit eventual recovery and blocked ingress before identity.

The writer is terminal. `evidence/cp1-observation-r8-frozen-source-manifest.json` seals39exact public product paths;35remaining immutable inherited rows match. Source/TODO and review artifacts are frozen until both the validation-only full API executor and fresh complete CP1 adherence reviewer are terminal. No repair during either lane. R5-01 remains open for adjudication after matching current-source evidence. Prior supported closures and r4 invalidation history remain intact. This checkpoint is not delivery: CP2..CP6, complete consumer/UI/browser/freshness/ALL/pcv/security/TQA/cutover/final reviews and separately approved real runtime/Meta proof remain mandatory.

## CP1 r8 accepted — CP2 execution handoff

Both frozen lanes are terminal with no source/TODO drift. `evidence/cp1-observation-r8-full-api-green.json` records30migrations, lint/build,395unit and490integration passes; `evidence/adherence-cp1-r8-result.json` is the fresh COMPLETE bounded39source review, no findings and all four positions acceptable. Strict merge passed. `evidence/cp1-r8-acceptance.json` closes R5-01 with the combined current-source proof; prior closures and invalidated history remain. No capacity/browser/realprovider claim follows.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP1-R5-01 | Integrated | useful | yes | project | n/a | Exact user-admitted guard, real-adapter product/unit causal RED, both cleanup recovery proofs and395unit/490fullintegration GREEN, fresh complete review on matching39sources |

CP2 continues under APROVADOv1.3, not a renewed approval boundary. A fresh serialized operational coder implements OAuth/authorization and raw signed ingress using `evidence/cp2-execution-handoff.json`, all16obligations in the prepared test-first plan and verified primary protocol. No other code writer or runner is active. Root retains documentation ownership. Existing WhatsApp contracts,35immutable rows and six regression restrictions remain. Actual env/private/runtime/Meta/tunnel/device work is still excluded until its later concrete plan. CP2 must end in complete checkpoint proof, not merely a partial OAuth endpoint; CP3..CP6 remain mandatory.

## CP2 implementation — initial route RED and concrete observations

`evidence/cp2-initial-route-red.json` retains the clean395unit/33integration-pass/2route404fail diagnostic before any production edits, as explicitly reported by the executor. It proves route absence only; no downstream OAuth/signature behavior is inferred. Three later pre-test lint/build failures remain qualified in separate receipts, with31migrations applied to the disposable database. All16CP2 obligations remain required before acceptance.

`evidence/cp2-root-static-observations.json` records three concrete static risks in currently mutable admitted source: budget backoff collapses to1second, captured acquisition time is reused as a stale callback-lease clock, and credential acquisition is recorded after /me delay. They remain open until meaningful behavioral proof and narrow correction; no dynamic exploit is claimed. The same artifact records Q01 as an unresolved subscription-envelope question, not an established defect: verify app/account identity semantics from primary evidence before accepting read-before-write. No guessed identity equivalence, new config, fallback or scope grant follows. User-approved WHAT,35immutable paths and runtime/private exclusions remain unchanged.

## CP2 protocol opinion and reached diagnostic proof

The strongest fresh bounded architecture opinion is terminal with changes_required; strict merge passed. This was a frozen-summary protocol opinion, not source adherence. Public primary sources establish the initial Instagram Login subscription POST and success:true, but did not establish the GET envelope, returned ID namespace, own-app visibility or conclusive-empty semantics. Their omission does not establish unsupported. No replacement identity or configuration is inferred.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-SUBPROTO-01 | Integrated | useful | partial | project | n/a | Primary-contract prerequisite remains open; subscription-protocol-opinion-result.json |
| IG-SUBPROTO-02 | Integrated | useful | yes | project | closed original defect by CP2 r1; UNKNOWN preserves mutation fence; concurrent lifecycle stays SUBREC-02 | adherence-cp2-r1-result.json; prior evidence retained |
| IG-SUBPROTO-03 | Integrated | useful | partial | project | closed original defect by CP2 r1; distinct identity purposes; no speculative parent-app configuration | adherence-cp2-r1-result.json; prior evidence retained |

Initial mutation and retry have distinct proof requirements: the documented first POST can be dispatched once only under a durable claim proving no earlier dispatch. A prior uncertain dispatch requires observation before any retry, and UNKNOWN never permits another mutation. This is subordinate HOW within the approved read-before-retry contract, not a waiver of the unresolved recovery criterion. Actual provider/private investigation remains excluded until a concrete later plan is approved.

Root-observed receipts cp2-postimplementation-diagnostic-red-04..08.json retain actual failed rounds, reached assertions and executor diagnoses. Round8 passed395unit and43/47integration; the remaining ingress scope defect was corrected only after that run terminated. Source remains mutable and CP2 unaccepted; no current acceptance follows from aggregate counts. ROOT01..03 have reported corrections and later behavioral assertions, but no separate pre-fix causal RED was captured for those static findings.

The path-only broad Git status deviation is retained in cp2-inventory-boundary-deviation.json: one unauthorized inventory command, no content/credential exposure or writes reported. Root did not inspect, reproduce or copy its raw output. No private-file authority or evidence claim follows. Existing runtime and35immutable public-path boundaries remain unchanged.

The current mutable confirmation controller/service/spec do not consume or persist a confirmation request key despite the approved endpoint contract. IG-CP2-ROOT-04 records this static gap and requests real BFF/PostgreSQL causal RED followed by one-promotion/one-dispatch replay proof. The executor was notified without changing source during its active runner. No new scope or acceptance is inferred. Callback return-route alignment remains within the admitted controller/UI responsibility; the protected App.tsx is not to be edited.

## CP2 recovery concretization — independent sequencing

Fresh strongest opinion subscription-recovery-concretization-result.json is terminal and strict merge passed. It confirms that the existing approved contract does not guarantee automatic successful recovery independent of provider evidence: truthful durable UNKNOWN is valid. It also confirms that a permanent no-op cannot satisfy the required own-account read. IG-SUBPROTO-01 and IG-SUBREC-03 stay open until the supported primary protocol, implementation and proof are established. No safety or consumer criterion is waived.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-SUBPROTO-01 | Integrated | useful | partial | project | n/a | Remains primary prerequisite before recovery acceptance and delivery |
| IG-SUBREC-02 | Integrated | useful | yes | project | open; source16 settledcleanup/GETtuple proved; acquisition postCOMMIT cleanup residual | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-SUBREC-03 | Integrated | useful | yes | project | n/a | Honest pending does not erase the explicit own-account observation requirement |
| IG-SUBREC-04 | Integrated | useful | partial | none | n/a | Two-GET operator proposal only; no provider activity authorized or executed, no universal inference |

Sequencing HOW is concretized as follows: finish current CP2 safety/idempotency proof and fresh source review with exact limits; independent CP3 implementation may then proceed without waiting for the provider-protocol clarification, while CP2 remains unaccepted. Overlapping source writes remain serialized, and no source changes occur during frozen validation/review. This is no new functional scope or gate waiver: all sixteen CP2 obligations, the missing own-account read, CP3–CP6, complete UI/browser and assurance gates remain mandatory before delivery.

User readiness confirmation on2026-10-24: the professional Instagram test account is added, with no test token generated. instagram-test-account-readiness-20261024.json records only this state. No credential acquisition or provider operation follows; synthetic implementation continues. The proposed operator investigation remains unexecuted and currently lacks its existing-token prerequisite.

Qualified causal receipts cp2-subscription-unknown-causal-red-01.json and cp2-confirmation-idempotency-causal-red-01.json preserve the actually reached failures. ROOT04 missing key returned200 instead of400; subsequent invalid-key assertions were not reached. Subscription assertions observed speculative GETs; these rounds do not prove every downstream UNKNOWN/crash/cross-attempt case. No aggregate RED/GREEN count substitutes for the exact remaining obligations.

Current candidate observations ROOT05/06 are retained in cp2-reauthorization-receipt-observations.json, with exact static/reached qualifications. A fixture failure did not prove positive connected reauthorization. A pending external subscription result cannot itself fabricate a receipt or become a circular prerequisite for accepting the actual eligible signed message that supplies receipt proof. Preserve the current identity/credential/generation/owner fences and all partial-batch replay obligations.

Primary send-limit mismatch is a proposed normative reconvergence only: instagram-text-byte-limit-ready.json binds the exact reviewed change from1000characters to1000UTF8bytes for outbound Instagram. Fresh critique found no proposal defects and strict merge passed; explicit user validation is pending. The governing numeric rules and product have not been changed under this proposal. All unrelated authorized work continues.

## CP2 candidate17 frozen — full API and complete source adherence

Sole executor is terminal. cp2-targeted-green-candidate-17.json records31disposable migrations, lint/build,395unit and47integration passes. Root matched all15reported changed paths, exact terminal log hash, all35immutable public rows and three preserved root index references. The exact16-obligation map is executor-reported and remains subject to assertion/source review; aggregate GREEN alone closes none of the current findings. Qualified failed and causal rounds remain retained.

Current source and this TODO are frozen for a separate validation-only complete API runner and fresh complete CP2 source-adherence review. Neither lane may edit sources or TODO; root collects evidence only. Both lanes must become terminal and source/context hashes must match before any repair or next code writer. New human approval, if received during this freeze, is recorded separately and applied to the governing TODO only after these lanes terminate.

The source review covers all approved OAuth/ingress/security/idempotency/receipt/uncertainty obligations and shared-owner regressions, not only residual fixes. It must carry the unresolved own-account primary protocol/read as open and all declared CP4consumers as still required under approved checkpoint sequencing. No backend-only delivery or UI waiver is inferred. ROOT01..06 and other code findings remain open for adjudication; no complete CP2 or functional delivery acceptance. Independent CP3 may follow truthful evidence reconciliation under the recorded opinion while missing primary observation remains explicitly unaccepted.

## CP2 r1 reconciled — admitted repair, no checkpoint acceptance

Both frozen lanes are terminal. cp2-r1-post-terminal-freeze-reconciliation.json matched234public sources, frozen TODO,26inputs,35preservation rows and3index references before thaw. Complete API:31migrations, lint/build,395unit and504/505integration; five Instagram write routes lack catalog classification. Fresh complete adherence strict collection passed with changes_required and ten findings. Original closures above are supported; ROOT02/04 and SUBREC02 retain residual defects. SUBPROTO01/SUBREC03 remain unaccepted primary-protocol obligations.

| Finding ID | Resolution | Usefulness | Formalizable | Rule Level | Follow-up | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-SUBPROTO-01 | Integrated | useful | partial | project | n/a | The own-account observation criterion remains unimplemented as an accepted protocol; adherence-cp2-r1-result.json |
| IG-CP2-R1-01 | Integrated | useful | yes | project | n/a | Confirmation can promote an expired candidate or overwrite cancellation; adherence-cp2-r1-result.json |
| IG-SUBREC-02 | Integrated | useful | yes | project | open; source16 settledcleanup/GETtuple proved; acquisition postCOMMIT cleanup residual | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-CP2-ROOT-04 | Integrated | useful | yes | project | closed original key/recovery defect; strict20 and actualnewversion/currentexpiry historical replay passed | adherence-cp2-r4-result.json; cp2-r3-source-validation-16-result.json; cp2-api-full-r4-result.json |
| IG-CP2-ROOT-02 | Integrated | useful | yes | project | open; source16 clocks proved; residual finalmapping and mapped preHTTP attemptTTL | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-CP2-R1-02 | Integrated | useful | yes | project | n/a | Instagram authorization admission diverges from current BU scope and error ordering; adherence-cp2-r1-result.json |
| IG-CP2-R1-03 | Integrated | useful | yes | project | n/a | The Instagram HTTP boundary follows redirects beyond its validated endpoints; adherence-cp2-r1-result.json |
| IG-CP2-R1-04 | Integrated | useful | yes | project | n/a | Failed OAuth callbacks retain sensitive query URLs without the required response protections; adherence-cp2-r1-result.json |
| IG-CP2-R1-05 | Integrated | useful | yes | project | closed original preflight defect and exactaccount fixture; currentfullAPI passed | adherence-cp2-r4-result.json; cp2-api-full-r4-result.json |
| IG-CP2-R1-06 | Integrated | useful | partial | project | open; exact finalmapping/preHTTP TTL/postCOMMIT proof plus primary/precontroller; replay/config/secondNest now supported | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json; cp2-api-full-r4-result.json |

All unresolved findings are release-blockers of this approved delivery. cp2-r1-repair-handoff.json assigns one fresh routine executor admitted OAuth/ingress/catalog fixes and real BFF/PostgreSQL causal tests. Root retains Foundation ownership. Access helpers may be reused/read, not edited merely because a review lists them. Preserve existing scenarios, inherited bytes, WhatsApp semantics and independent receipt. No blanket route exemptions or domain/transaction mocks.

Source freeze is lifted for this serialized repair. After targeted terminal proof, refreeze exact source/inputs for complete API and fresh affected source review. Independent CP3 may proceed under the recorded sequencing, without accepting CP2 or waiving the own-account observation, consumers or later gates. CP4..CP6, ALL/pcv/security/TQA/cutover/final and separately approved real runtime remain mandatory. The proposed1000UTF-8-byte correction still awaits human validation; no change to its normative clauses here.

## Public privacy companion — reviewed proposal, admission pending

The existing public privacy page still describes WhatsApp only. privacy-instagram-companion-ready.json binds the exact one-file staticHTML proposal, unchanged sourcehash, full original/diff and terminal independent critique with zero findings/allpositionsacceptable; strict merge passed. The proposal adds only factual Instagram Login/profile/identifier/textDM/humanreply descriptions and BU scoping, preserving institutional contact, legal/retention/deletion text, existing hosting claims and staticpage protections. User path validation is requested because web-app/public/privacidade.html is outside this strict contract. No expected-path admission, product change, publication, legal-compliance certification or runtime authority follows until explicit approval. Before applying, the sole writer must recheck sourcehash, effective date and actual final data-flow parity; material mismatch returns the proposal to review. All React/operator/browser consumers and CP2..CP6 remain required.

## OAuth callback session companion — exact proposal review

R1-04 has a concrete protected-path dependency: session.middleware.ts can reject before the admitted controller. The first exact companion critique is terminal with one medium security finding IG-OAUTH-SESSCOMP-01; early headers plus known-denial redirects still leave unexpected database/session errors on a sensitive query URL. That finding is Integrated/useful/formalizable yes/project and retained as release-blocker. Revised exact proposal v2 wraps unchanged session enforcement only for the effective GETcallback; all failures before output use fixed safe303 and known/generic classifications, without making the callback public. Ordinary routes retain their original exception/status/order. Sourcehash/CRLF preserved, no sourcewrite/pathadmission. Fresh complete companion critique is required before humanvalidation of this unadmitted path. Controller, Numerosconsumer, actualNest/PG and latergateway/browser remain mandatory; no R1-04 closure or delivery is inferred.

## CP2 repair diagnostics — source edit during validation, split lanes

cp2-r1-repair-result-01..05 receipts retain exact qualified diagnostic outcomes; build-only rounds prove no functional behavior. GREEN05 is invalid as stable/current-source proof: the executor edited callback/activeBU authorization during e2e. Its395unit/54of58integration counts are diagnostic only. IG-CP2-ROOT-08 records the concrete deviation, no invented credential or data exposure. The executor stopped and became terminal; root matched10reported currentfiles,35immutable rows and3rootindex entries in cp2-r1-intermediate-source-handoff.json. No source acceptance follows.

Next writer is fresh test-only, with no runner/sourceproduction authority: repair the four harness/assertion defects and add remaining actual-boundary CP2proof. Then it becomes terminal. Root alone freezes exactcurrent sources/TODO/reviewinputs and dispatches a separate validation-only executor. No active productwriter during validation; after every terminal result root explicitly thaws any repair. No edits during a running test or review. Primary observer obligation, fullAPI/currentreview and allCP3..CP6 remain mandatory.

Sessioncompanion v2 is now proposal-converged: complete terminal r2critique has zero findings/allpositionsacceptable and strictmergeexit0. Initial native turn had capacity failure after saving outputs; samecomplete frozenpackage continuation verified them and completed successfully, without fallback/reduction/waiver. oauth-callback-session-companion-ready-v2.json binds exact sourcehash/CRLF/candidate/diff. Explicit onepath humanvalidation is requested and pending; session.middleware.ts remains unchanged/unadmitted. IG-OAUTH-SESSCOMP-01 closes atproposal level only; R1-04 remains open until actualsource/consumer/gateway/browserproof. Privacyfile and outboundbyte proposals also await human replies.

## CP2 residual proof — frozen validation and code-only repair

The test-only writer became terminal; root matched reported sources and sealed236publicfiles plus this TODO. Separate validation01 stopped at one unused test binding after31migrations/Prisma; no functional assertions ran. After a one-binding test-only correction and refreeze, validation02 passed31migrations, lint/build and395unit;64of67selected integration passed. Root rechecked236sources/TODO,35immutable rows and3rootindex refs after both lanes terminated. Receipts retain exact log hashes and unexecuted downstream assertions.

Validation02 reached a causal expiry race: confirmation returned200instead of409after the durable claim expired before the mapping transaction. R1-01/ROOT02 remain open. The callback failure was an overly strict relative-URL test assumption; the fourth observation conflicts with the approved three-request budget and must be corrected without raising/resetting that budget or weakening confidentiality. cp2-residual-code-only-repair-handoff.json assigns one serialized code/test writer with NO runner authority, addressing all remaining admitted current-clock/credential/deadline/CAS/history fences and meaningful independent tests. Root will refreeze and dispatch a separate validator after the writer is terminal. No source edits during validation/review.

No CP2 acceptance follows. The primary observer, precontroller session confidentiality companion, public privacy companion and outbound-byte proposal remain open with their exact authority limits. CP3..CP6 and all complete regression/browser/assurance/physical gates remain required.

## CP2 code-only candidate — terminal and refreeze

The residual code-only executor is terminal without running validation. Root matched8reported changed paths, allother228frozen public paths,35preservation rows and3rootindex references. cp2-residual-code-only-terminal-reconciliation.json records the exact candidate. Repairs and new cases remain NOTRUN; source hash agreement is not correctness evidence.

IG-CP2-ROOT-09 retains an instruction/evidence alignment lapse: reported backup instruction reads and an inaccurate committed/baseline inference from empty exact-path Git diff. Edits paused; principal instructions/profile/TODO were reloaded, scope corrected and same admitted path ownership preserved. Root did not inspect/copy backup files, and no exposure, Git write or sourcecopy is inferred. Independent actualsource review and clean stable validation are mandatory; backup context/emptydiff cannot substantiate acceptance.

An executor static concern about the expiry-test barrier is qualified: the test releases the first blocker before waiting for the claim, and prior frozen validation02 reached the response assertion only after claimSeen/CANDIDATE_READY assertions passed. That observation does not prove the newly repaired version; the separate rerun determines its actual reached result. No assertion is weakened on speculation.

Current236publicfiles and this TODO are frozen for one separate api-instagram validation. No source/TODO writer during the run; only distinct evidence outputs. After terminal matching, fullAPI/freshcompleteCP2adherence and then independentCP3 remain required, without waiving primaryobserver, pendinghuman companions or CP4..CP6.

## CP2 validation03 — builder failure and narrow causal proof lane

The separate frozen validation03 is terminal, with236source/TODO/35preservation/3index matched. Prisma generation stopped atP1012because the two new resource-history indexes have colliding generated truncated names; migrations/lint/build/unit/integration were NOTREACHED. cp2-residual-validation-03-result.json preserves this as builder-only evidence, not a functional result.

Freeze03 ended only for a fresh narrow code/test-only lane: explicit unique short indexmaps matching SQL names, with identical columns/order, plus one actualBFF/PG natural signed-session expiry case. Existing ROOT02/R1-06 require current authorization after waits; requireActorTx currently verifies the session before awaiting the user row. This is a static concern, not a proven exploit. cp2-session-clock-static-observation.json and cp2-index-clock-proof-handoff.json bind the three admitted paths and causal proof plan. The service stays unchanged so a later separate runner can establish RED. Actual SessionService signing/verification, realPG waits and current BFF are used; no auth/clock/transaction mocks, private data or runtime authority. No runner in writer lane.

## CP2 complete r2 — adjudication and causal proof repair

Both frozen lanes are terminal. Root matched236sources, this TODO,42boundinputs,35preservedfiles and3rootindex refs in cp2-r2-both-terminal-reconciliation.json. Complete fresh review is changes_required with10findings; cp2-r2-root-adjudication.json integrates every finding and preserves supported repairs without claiming checkpoint acceptance. Stable fullAPI passed31migrations/lint/build/395unit and522of528integration; six failures are classified in cp2-api-full-r2-result.json. Catalog coverage has one obsolete callbackGET entry; the indexed SQL case failed fixture setup before plan assertions. Four Instagram failures reflect concrete counter/cooldown/mapped-snapshot fixture defects. The15second natural-session PASS is confounded by5second transaction timeout; it does not prove live postwait authorization.

The frozen r2 source/input package remains immutable historical evidence. Thaw is now limited to one fresh test-only writer for the two admitted Instagram specs, as cp2-r2-causal-test-only-handoff.json. No production edit or runner in that lane. It establishes short causal PG/session RED with a matched live control, structural entry preflight/route-alias probes, and corrects fixtures without lowering guarantees. Root will refreeze before a separate disposable validator, then assign the admitted source repair. Primary observer, pendinghuman protected companions, actual writer recovery, all16obligations and CP3..CP6 remain required; ROOT08/09 still need clean validation acceptance.

## CP2 r2 causal proof — source repair authorized

Validation07 stopped at one unused test initialization; no functional proof. After exact two-literal fixture correction and refreeze08, the separate runner passed31migrations/lint/build/395unit and68of71selectedintegration. cp2-r2-causal-validation-08-result.json records the actual finalsession snapshot: one externalrequest and EXCHANGING after naturalexpiry, despite zero candidate/mapping/credential facts. The reached finalassertion follows a matched livecontrol and realPG waiter/expiry/<4.5s assertions in the byte-bound source; fields were not separately printed. This is qualified causalRED, distinct from the15s timeoutconfound. Missingentryaccount returned200; laterzeroeffect/numericcases were not reached. OAuthalias returned429 instead413, reaching domainbudget rather than the declared16KiBparser. LaterIGalias proof remains open. Previousfourfixture failures are absent in this selectedrun.

Alllanes terminal and root236/TODO/7inputs/35preserved/3index matched. Explicitthaw is now one fresh source/test-only writer under cp2-r2-source-repair-handoff.json, owning thirteen exactadmittedpaths including twooptionalInstagramrecovery/binding specs and the optional HTTPclient unit companion inside the approved integrations/instagram pattern. No runner whilewriter active. It covers final liveauthorization, durable bindingholder/cooldown acrossreceipt/cancel, actualwriterfault recovery, ingresspreflight/effectivealiases, obsoleteGETcoverage and bounded15000row fixture. Protectedhumancompanions and ownprimaryobserver remain open. Newcode is NOTRUN until terminal/refreeze/separatevalidation; no checkpoint/delivery acceptance. CP3..CP6 and all mandatory gates remain.

## CP2 source09 — qualified proof and bounded follow-up

The13path codewriter and separate source09validator are terminal. Root matched239sources/currentTODO/8boundinputs/35preservations/3index.31migrations/lint/build/398unit passed;69of73selectedintegration passed. The short naturalexpiry test isGREEN across two distinct under5s transactions (5025ms wholecase); nativefetchloopback3cases passed. This doesnot close finalawaitROOT02 or thefullHTTPremainingbudget obligation. Fourfailures remain: boundsfixture hits inheritedactorquota beforeprobes; bindingfake throwsbeforeits heldhook; recoveryfaulttriggerstillactive onreplay; stalefixture refers to removed resource-lifetimecounter. cp2-r2-source-validation-09-result.json records reached/notreached boundaries; actualinterruptedwriter+committedsnapshot were reached, successfulrecovery wasnot.

cp2-r2-source-static-followup-09.json retains ROOT10..12 concrete fixture/deadline/finalawait observations withoutclaiming dynamicexploitation. After terminalmatching, cp2-r2-code-only-followup-09.json explicitlythaws onlyseven previouslyadmittedpaths for thesecorrections and remaining freshconfirmation/clockproof. No runner withwriter active. Bindinglease/cooldown isglobal; three-requestbudget remainsperadministrativestage/currentattempt, no inventedresource-lifetimecap. Ownobserver and protectedhumancompanions remainunaccepted; CP3..CP6/fullAPI/freshreview/allmandatorygates remain.

## CP2 follow-up11 — qualified stable validation, two residual failures

After the source writer became terminal, root sealed239public sources/currentTODO/9boundinputs. Validation10 was lint-onlyRED (three unusedinitializations); exact preimage reconstruction qualifies the one-file correction before freeze11. Separate validation11 passed31migrations/lint/build/398unit and75of77selectedintegration. Root independently matched239/TODO/9inputs/35preserved/3index and exactlogSHA after validator terminal in cp2-r2-lint-validation-11-result.json. Natural signed-session expiry after an actual attempt-row wait passed with its equal-duration livecontrol; actual committed-writer recovery originalkey/body replay passed. Effectivealias/bodybounds and late success/lostACK successor-binding protection passed. No complete CP2/fullAPI acceptance follows.

Two residual failures are explicit. The20freshconfirmation case failed its loser status/code predicate, without capturing the actual distribution; later winner/replay/audit assertions were not reached. The receipt/cancellation case retained the original bindingholder after a settled provider error; cancellation and acceptedmessage/receipt assertions passed before that failure. Source inspection identifies tuple rejection before the holderrelease in the error path. Do not infer duplicate provider dispatch or lostreceipt from either result.

cp2-r2-qualified11-narrow-repair.json thaws only the previouslyadmitted authorizationservice and binding/residual specs for one serialized code-only writer. Preserve strict19conflict losers, one actualPOST and immutable replay; capture safe actualstatus/code diagnostics rather than relax the predicate. Ensure exact-token cleanup after the HTTP operation settles and stale result handling rejects, retaining successorholders, independentreceipt/cancel, cooldown and firstPOST history. No runner whilewriter active. Other236sources stayimmutable; root will refreeze before separatevalidation. Primaryobserver, pendinghumancompanions, complete regression/freshreview and CP3..CP6 remain required.

## CP2 cleanup12 — receipt cancellation passes, exact concurrency conflict remains

The cleanup writer was terminal before root sealed239sources/TODO/12inputs. Separate validation12 passed31migrations/lint/build/398unit and76of77integration. Root independently matched allfrozeninputs/35preservations/3index and exactlogSHA after validator terminal. The signedreceipt/cancellation case now passed including originalholder cleanup and independentlycommitted facts; both late successorholder success/error cases, recovery and shortsession matchedcontrol remainGREEN.

The actual20fresh case reached19losers, all409:18CONFIRMATION_IN_PROGRESS and1OPERATION_IN_PROGRESS. Laterwinner/replay/audit assertions were not reached. This proves a classification/claimgap, not a duplicatePOST. The currentclaim predicate misses mapped/NOT_STARTED between mappingcommit and resourceholderclaim. cp2-r2-confirmation-gap-repair-13.json explicitlythaws onlytheauthorizationservice for the existing original liveclaim interval underits40s deadline; no newlease/schema or renewalonloser. KnownSUBSCRIBED localrecovery and UNCERTAIN/no-repeatPOST history remain unchanged. Allother238sources staysealed; no runner duringwriter. Currentcomplete regression/freshreview and everypendinghuman/primary/CP3..CP6 obligation remain.

## CP2 complete r3 — adjudicated, causal test-only lane

Both stable lanes are terminal; cp2-r3-both-terminal-reconciliation.json independently matches239sources/TODO/15phaseinputs/51reviewinputs/35preservations/3index and allfourreviewoutputSHAs. Selected13passed31migrations/lint/build/398unit/77integration, including strict19confirmationconflicts and subsequentwinner/audit/onePOST/version/replay. A validator narrative accidentallycopied18+1fromrun12; it was corrected against the unchangedstrict13assertion andcaselevelPASS, notinvented individualprintedvalues. CompleteAPIr3passed398unit and534of535integration across40files; onlyunqualifiedfindFirst account selection inmain1016failed. Laterassertions inthatcase wereunreached. ROOT15 is fixture determinism, notproven ingressregression. OriginalobsoleteGETcoverage and15kfixture failures areabsent.

Freshcomplete r3 read60actualsources/fullTODO/51inputs/all16obligations andstrictmergepassed, changes_required withfivefindings. cp2-r3-root-adjudication.json integrates allfive. SupportedoriginalTTL/cancel/CAS/authorder/redirect/preflight/keyrecovery/catalogrepairs are retained above. ROOT02 now distinguishes repairedsignedsession fromresidualfinaloperation/deadline/credential clocks. SUBREC02 retainsglobalfirstPOST/holder/CAS repairs butcoverspostsettlementcontinuationcleanup andsuccessfulGETnull tuple revalidation. OwnprimaryGETandprotectedprecontroller remainunaccepted; R1-06 retains exactremainingproof. Originalseverity/routing isnotweakened; allunresolved arecurrentdeliveryrelease-blockers. ROOT08/09 completecleanacceptance stillpending, nohash-onlyclosure.

| Finding ID | Resolution | Usefulness | Formalizable | Rule Level | Follow-up | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-SUBPROTO-01 | Integrated | useful | partial | project | n/a | Primary own-observer contract remains unestablished; SUBREC03 retained |
| IG-CP2-ROOT-02 | Integrated | useful | yes | project | open; source16 clocks proved; residual finalmapping and mapped preHTTP attemptTTL | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-SUBREC-02 | Integrated | useful | yes | project | open; source16 settledcleanup/GETtuple proved; acquisition postCOMMIT cleanup residual | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-CP2-R1-04 | Integrated | useful | yes | project | n/a | Exact session companion pending human admission, no source waiver |
| IG-CP2-R1-06 | Integrated | useful | partial | project | open; exact finalmapping/preHTTP TTL/postCOMMIT proof plus primary/precontroller; replay/config/secondNest now supported | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json; cp2-api-full-r4-result.json |

Explicitthaw is one test-only writer under cp2-r3-final-clock-test-only-handoff.json: existingmain/residual specs and optionalnew instagram-cp2-final-clock.e2e-spec.ts / instagram-cp2-finalization.e2e-spec.ts insideapprovedtestglob/canonicalselector. Allproduction/other237sources remainimmutable. Prove realPostgreSQL finalwrite waits and equal-duration controls undernormal5s budget; labeldeliberatelyshortenedlease robustness accurately, nevernatural60sexpiry. UseactualPGfault/queuedtakeover, notdomain/transactionmocks. Correctonlyexactfixtureselection, preserveeveryassertion/counter. Addcurrentusabilitychanged completedreplay andconfig/service-recreation proof. No runner whilewriter; terminal/refreeze/separatevalidation beforeproductionrepair. Primaryobserver/bytes/privacy/sessionhumanproposals andCP3..CP6/allconsumers/ALL/stress/browser/assurance/runtime remain mandatory; no newWHAT, protectedpathadmission, checkpointacceptance orwaiver.

## CP2 r3 causal candidate14 — test writer terminal, production unchanged

cp2-r3-test-only-terminal-14.json matchesall4reportedtestpaths, allother237source13paths,35immutablefiles and3index refs. Two new specs are insideapprovedglob/canonicalselector. Production source13isunchanged so subsequentfailures canbequalifiedcausalRED. Existingmain selects exactprofessional/channel; versionrotation replayretains samegeneration, currentexpiredcredential nevercausesHTTP; quotausesreal secondaryNest/samePG withprimaryappalive. Missingwebhook/crypto config variants restoreonlysyntheticfixtureenv.

Rootstaticpreexecutionchecks corrected TEXT-vsUUIDtriggercomparison, rawPGvoiddeserialization, invalidlongblockertimeouts, expiredresponseexpectation, pooledPID-vsTX identity, ownerC transaction-boundtakeover andidempotentunblock/cleanup. Mainfixedinventedgenerationincrease andfixtureappcleanupowner. These corrections consumednorunner and grantnofunctionalproof. cp2-r3-test-preexecution-alignment.json andmainalignment retainqualifications. Everyapp/holder remainsunderordinary5sTX; deliberatepersistedleaseshortening isrobustness, actualproviderexpiry/margin isidentifiedseparately.

All241explicitpublicsources/currentTODO/boundinputs arefrozen for one separate canonicalapi-instagram validation14; no source/T/inputwriter. Newphaseclock/postsettlement/GETtakeovercases areNOTRUN; actor/sessionproof andprior13GREENstayhistorical. Onlyactualwait/clock/matchedcontrol/reachedassertions can supportRED. Rootreconciles terminalhashes beforeanyproductionthaw. FullAPI/freshcompleteadherence/all16/currenthuman/primary andCP3..CP6 obligations remain; no current checkpoint/delivery acceptance.


## CP2 r3 validation15 — qualified causal RED and bounded repair16

Separate validation15 passed31migrations/lint/build/398unit and84of91selectedintegration. Root independently matched241sources/currentTODO/72inputs/35preservation rows/3index references and exactlogSHA after validator terminal. cp2-r3-causal-validation-15-result.json records six reached causal failures: callback final clock/margin persistence, subscription final fact despite409, provider-error settlement, originalholder cleanup after postPOST SQLfault, and successfulGET/null continuation after queued bindingtakeover. Equal-duration live/no-fault controls passed. Deliberatelyshortened persistedlease/deadline cases are robustness proofs, not natural60s lease expiry; combined subscriptionclock failure doesnot isolate eachclock. Only reached assertions support each conclusion; later assertions remain unproved. Independent signedreceipt/originalkeyrecovery/tombstone assertions were reached before the final cleanupflag failure.

The seventh failure is a stale ordinaryGET fixture: firstPOST1 plus laterGET1 gives2within the currentattempt budget3. Correct only the final counter to afterPost.subscriptionRequests+1 and2, retaining the earlier1, UNKNOWN, exactoneGET/zeroPOST and allother assertions. Do not change the product requestbudget. ROOT15 exactaccount fixture passed selected15; completeAPI rerun remains pending.

All lanes are terminal. Explicitthaw under cp2-r3-final-clock-source-repair-16.json assigns the sole codewriter only api-app/src/domain/channels/instagram-authorization.service.ts and the one counter correction in api-app/test/instagram-cp2-finalization.e2e-spec.ts. Allother239frozen sources remain immutable. Final database-time predicates and synchronous guards after last awaitedfactwrite must reject expired current operation/credential facts; centralized exact-original-token settlement cleanup must preserve successors and independentreceipt/cancellation. GET/null finalization rechecks the current tuple inside its own lockedtransaction. Historical authorizedCOMPLETED/knownACK recovery stays immutable zeroHTTP despite current credential changes. No runner/Git/private/runtime/docs authority in this writer lane. Root refreezes after terminal and dispatches separate validation16, then currentcompleteAPI/freshcompleteCP2review. No CP2 acceptance, primaryobserver waiver, humancompanion admission or CP3..CP6 reduction follows.


## CP2 source16 — terminal reconciliation and frozen validation

The sole writer is terminal; root matched bothreported pathhashes, allother239sources,35preservedfiles and3rootindex refs in cp2-r3-source16-terminal-reconciliation.json. Reconstructing the exact prior test bytes proves its only change is the agreed ordinaryGET counter correction. Preexecution static alignment required a second pass within the same service/pathscope: finalclock facts now come from the current lockedtransaction, with DB-time mutation predicates and a fresh synchronous max(DBclock,Date.now) check afterlastmutation/auditawait. One captured-original-token finally covers settledcontinuations, and GET/null revalidates inside its finaltransaction. Source changes remain NOTRUN.

All241explicitpublicsources/currentTODO/boundinputs are frozen for one separate canonical api-instagram validation16. No source/TODO/inputwriter during the run; only unique evidence outputs. Root will reconcile exactterminalhashes and reached assertions before currentcompleteAPI/freshcompleteCP2review. No acceptance follows from static inspection; allsix causalRED qualifications, originalseverity/openfindings, ownprimaryobserver, threependinghumanproposals, all16obligations, CP3..CP6 and mandatoryconsumers/ALL/assurance/runtime remain.


## CP2 complete r4 — current full API reconciled, bounded final-boundary proof

Both lanes are terminal. Source16 selected91 and full549integration plus398unit/lint/build/31migrations passed on independentlymatched241sources/currentTODO/77inputs/35preservations/3index. CompleteR4 read all62actualsourcebodies/fullTODO/61evidence/all16obligations/fiveaxes, strictmergepassed withfivefindings. Two honest capacitycontinuations kept the same completepackage untilallreads/postchecks completed; no reducedreview or partialacceptance. The fullAPIreceipt was excludedfromreviewinputs and reconciledseparatelybyroot in cp2-r4-both-terminal-reconciliation.json.

cp2-r4-root-adjudication.json integrates allfive and preserves their governing release-blocker routing/severity. ROOT02 retains two distinct static intervals: finalcandidate->active promotion after its SQLclockpredicate and mappedpreHTTP attemptTTL. SUBREC02 retains the acquisitionawait beforecleanup, where signed-session rejection afterCOMMIT can retain an originalholder despite zeroHTTP. Sixsource16causalGREENrepairs remain supported; no newdynamicfailure isclaimed. Existing strict20/recovery/current-usabilityreplay/config9/realNestquota proofs are supported. ROOT15 exactfixture passedfullcurrentAPI. Original ROOT08/09 invalidproof/authorityinference defects now have stablecurrentAPI pluscompleteactualpublicsource review; GREEN05 staysinvalid, and reviewerfilename-only bootstrap metadata note isretained withoutcopying/usingbackupcontent or inventingexposure. Alllaterassurance remains mandatory.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-SUBPROTO-01 | Integrated | useful | partial | project | n/a | Ownprimaryobservation and SUBREC03 remain unaccepted |
| IG-CP2-ROOT-02 | Integrated | useful | yes | project | n/a | Complete current finalmapping/dispatchTTL proof and guard; preserve source16 repairs |
| IG-SUBREC-02 | Integrated | useful | yes | project | n/a | One exact-original-token lifecycle must also cover committedclaim rejection |
| IG-CP2-R1-04 | Integrated | useful | yes | project | n/a | Humanprotectedcompanion admission and actualconsumer/browser proof remain pending |
| IG-CP2-R1-06 | Integrated | useful | partial | project | n/a | Precise threeboundarytests stillneeded; currentfullAPI nowreconciled, no universalcoverageclaim |

Explicitthaw is one fresh test-only writer for api-app/test/instagram-cp2-commit-fences.e2e-spec.ts inside the approved test/*instagram*.e2e-spec.ts glob/canonicalselector. All241source16existingpaths remainimmutable, especially production. cp2-r4-commit-fences-test-handoff.json defines three actualPostgreSQL boundaries with matchedlivecontrols: finalpromotioncrossingactualcandidate60smargin; deliberatelyshortenedpersistedattemptTTL beforeHTTP; naturallyexpiringsignedsession acrossactualclaimCOMMIT using a deferredtrigger. Keepnormal5sTX, observedfinitebarriers/clock/assertionordering and safeawaitedcleanup; no mocks of session/clock/Prisma/domain/transaction, no timeoutincreases or oldassertionedits. No runner/Git/private/runtime/Meta/provider/docs authority in writerlane. Rootrefreezes afterterminal and usesseparatecausalvalidation17 beforeanyproductionrepair. Source16fullGREEN remainshistoricalstableproof, not acceptance oftheseuntestedintervals. Primaryobserver, threehumanproposals andCP3..CP6/allconsumers/ALL/stress/security/TQA/cutover/final/runtime remainmandatory; no newWHAT or waiver.

## CP2 final-boundary test17 — preexecution reconciliation

The sole test writer is terminal. Only api-app/test/instagram-cp2-commit-fences.e2e-spec.ts was added; all241source16 paths,77historical boundinputs,35preserved public rows and3rootindex entries match. Root read the complete new spec and reconciled eager realHTTP, actual observed UPDATE/COMMIT barriers, native session expiry, before-release clock eligibility, matched live waits, mapping rollback/candidate preservation, exact original-holder cleanup and counter/tombstone assertions. The short native session fixture now has about3seconds remaining, with positive validity observed at queued COMMIT; normal5second transaction budgets are unchanged. Shortened persisted TTL remains a robustness case, not natural10minute expiry. The phase window is additionally bounded by actual request/holder durations below4.5seconds against the existing40second invocation deadline. No test result is inferred from this static preflight.

All242explicit public sources/currentTODO/boundinputs freeze for one separate canonical api-instagram17 invocation. No source/TODO/input writer during validation. Expected negative boundaries remain hypotheses until their actual barriers, clock crossings and decisive snapshots are reached; matched controls must pass. Root will reconcile terminal evidence before any production thaw. Source16 selected/fullAPI GREEN stays historical; primary own-account observation, pending bytes/privacy/middleware human proposals and complete CP3..CP6/consumers/ALL/assurance/runtime remain mandatory.

## CP2 validation17 — unit timing measurement, new boundaries unreached

The single api-instagram17 invocation terminated exit1 after31migrations/lint/build PASS and397/398unit tests. All E2E, including the six new boundary cases, are UNREACHED; no causal RED/GREEN follows. The native body-read test reached bodyStarted/guardCompleted and rejected correctly, but Date.now elapsed1499ms failed the unchanged875ms threshold while Vitest reported721ms case duration. This time-source discrepancy is a measurement confound, not proof of a provider deadline regression; no host-clock change or environment explanation is asserted. Root matched242sources/currentT/93inputs/35preserved/3index and actuallog SHA after the validator became terminal.

Explicitthaw is limited to api-app/src/integrations/instagram/instagram-http.client.spec.ts under the admitted Instagram integration glob. Use performance.now solely for the two elapsed-duration assertions, retain Date.now for absolute deadlines, retain the strict875ms/1500ms bounds, actual nativeHTTP/AbortSignal/body/guard/request assertions and every scenario. No production/new-boundary spec edits, no test runner or runtime/private/Git authority in the writer lane. Then root refreezes and dispatches one separate complete canonical validation17b. All prior safety hypotheses, primary observer, three pending human proposals and CP3..CP6 remain required.

The unit17b writer is terminal. Root reconstructed the exact previous unit-spec bytes by removing only the performance import/two elapsed measurement starts and restoring two elapsed expressions; SHA matches the historical unit file exactly. All other241sources/35preserved rows/3index match. No product change, relaxed latency threshold, new scenario or clock mock. Current242sources/currentTODO/inputs freeze for one complete api-instagram17b invocation; no writers during validation.

## CP2 validation17b — three causal boundary failures, matched controls passed

The separate canonical api-instagram17b invocation applied31migrations and passed lint/build/398unit tests. SelectedE2E executed97cases:94passed, including all91previous cases and all3newlivecontrols; exactly3newnegativecases failed. Root matched242source/currentTODO/100inputs/35preserved/3index and actualterminal logSHA. cp2-r4-causal-validation-17b-result.json records complete reached-assertion qualifications.

ROOT02 finalmapping is causally reproduced: the actual finalUPDATE wait crossed the actual62second candidate60second margin, yet promotion/owner/channel/credential/provider effects committed and candidate secrets were cleared; later409/zeroPOST did not undo them. ROOT02 preHTTP TTL is causally reproduced: a deliberately shortened future persistedTTL expired at an observed subscription-claimUPDATE wait while other authorization/phase facts stayed live; one NEWPOST/counter1/OBSERVING occurred before409. This is robustness against shortened metadata, not natural10minute expiry. SUBREC02 is causally reproduced across an actualdeferredCOMMIT: native signed session was valid at queue and expired before release;401/zeroPOST retained the exact original binding holder although claim history was correctly durable. Equal-duration65second/liveTTL/liveSession controls all passed under normal5second transaction budgets. Governinghigh/release-blocker severities stay unchanged.

Explicitthaw is one sole sourcewriter for api-app/src/domain/channels/instagram-authorization.service.ts under cp2-r4-source-repair-18.json. Tests and allother241sources remain sealed. Implement finalmappingfresh-clock rollback, active subscription attemptTTL eligibility before newHTTP, and one exact-original-token binding lifecycle covering acquisition await/postCOMMIT failure as well as settled provider continuations. Classify all17actorTransaction callsites as new activephase or authorized historical/localfact; preserve completedreplay/knownACK/independentreceipt/cancel/successor history without blanket expiry rejection. No providerHTTP inside transaction, no retry/schema/config/newframework/Channelmethods, no timeoutincrease, no testweakening or pendinghuman path edits. No runner withwriteractive. After terminal, root uses one complete canonicalAPI run to cover targeted cases plus allprevious API regressions and a fresh affected-source adherence review carrying completeR4 unchanged-source/all16obligations. This avoids a redundant selected-only rerun; it waives no validation. Then independentCP3 proceeds under recorded sequencing while CP2 remains unaccepted until its primary/human obligations are met.

## CP2 source18 — final temporal owner reconciliation and current proof

The sole sourcewriter is terminal. Only instagram-authorization.service.ts changed; root matched allother241sources,100historical boundinputs,35preservations and3rootindex entries. cp2-r4-source18-terminal-reconciliation.json records exact sourceSHA, read guard/lifecycle changes and all17actorTransaction caller classifications. Active mapping/claim/finalprovider phases use the current database clock and original locked temporal facts. Acquisition is inside the exact-original-token lifecyclefinally. The final preHTTP active fence and subscription recheck also guard captured clocks after the awaited transaction and perform a synchronous signed-session check after the last awaited clock read. Receipt/replay/cancellation/localfacts keep their existing selective semantics. Tests remain byte-identical to qualified17b, including monotonic unit measurements and allthree failing safety assertions. No new limit, framework, schema or protected-path admission.

All242publicsources/currentTODO/currentinputs freeze for one canonical API-complete18 invocation and a fresh bounded affected-source architecture-adherence r5 review. R5 supplements the terminal complete62source/all16 R4 review: it rereads full changed service/unit/newcausal spec and immediate current temporal/session/transaction/client/fence test bodies, plus exact governing contract sections and completeR4 findings/collection; it is not a repeated full62body review or CP2 acceptance. Allunchanged completeR4 source bodies are independently checked by exact currenthash. This is a new prospective affected package after terminalR4, never shrinkage of a live review. CurrentfullAPI18 log is excluded while active; root reconciles it independently after bothterminal. CompleteAPI contains the targeted cases and allprevious API regressions, replacing a redundant selected-only run without waiving coverage. No writer during either lane. Primaryobserver, threependinghuman proposals, all16obligations, CP3..CP6/consumers/ALL/stress/assurance/physical gates remain mandatory.

## CP2 source18 + affectedR5 reconciled — independent CP3 test-first

Both lanes are terminal. Root independently matched242source/currentTODO/108boundinputs+24reviewinputs/35preservedrows/3index and allfourreportedreviewoutputs. FullcanonicalAPI18 actually passed31migrations/lint/build/398unit/555E2E, including allthree17bnegative-boundaryoracles, their3matchedlivecontrols and all91priorInstagramcases. R5 completed12actualfullbodies/11governingranges/15evidence/all16obligations/17callers; strictmergeexit0. It supplements completeR4, carrying60unchangedbodyreviews; no freshfull62/fullTODOclaim. CurrentAPI18wasexcluded/unreadbyR5 and independently reconciledbyroot.

| Finding | Resolution | Current authoritative disposition |
| --- | --- | --- |
| IG-SUBPROTO-01 / IG-SUBREC-03 | Integrated | Open primaryownobserver; UNKNOWN/no-repeat does notsatisfy it; no waiver. |
| IG-CP2-ROOT-02 | Integrated | Resolvedqualified on current18: actualexpiredcandidatepromotion rollback and expiredattemptTTL zeroNEWPOST/counter0, matchedlivecontrols andpreviousclockcases allpassed. Originalhighseverity retainedhistorically, notdowngraded. |
| IG-SUBREC-02 | Integrated | Resolvedqualified on current18: actualpostCOMMITnativeexpiry exactoriginalholderrelease/historyretained, heldHTTP/successor/receipt/fault regressions allpassed. Originalhighseverity retainedhistorically. |
| IG-CP2-R1-04 | Integrated | Open exactsessionmiddlewarehumanadmission and actualNest/consumer/gateway/browserproof. |
| IG-CP2-R1-06 | Integrated | Currenttemporalproof reconciled; remainingprimary/precontroller/consumers/CP3..CP6/ALL/stress/assurance/runtime obligations open. |

No additionalmaterialsource defect was identified byR5; affectedperformance/elegance/structure acceptable, operationalfit/adherence mixed due remainingmandatoryscope. No CP2acceptance orfunctionaldelivery. Rootadjudication in cp2-r5-root-adjudication.json preservesexactproofqualifications, historical17/17b/16/R4 and priorclosedROOT08/09/15 dispositions.

IndependentCP3 now proceeds under alreadyrecordedsequencing withoutwaitingforownprotocolclarification andwithoutacceptingCP2. Explicitthaw is one test-onlywriter for api-app/test/instagram-cp3-routing.e2e-spec.ts, api-app/test/instagram-cp3-v1-cutover.e2e-spec.ts and a narrowlyisolated /messages externalfakeextension in api-app/test/helpers.ts. Allproduction and existingtests remainimmutable; no runner withwriteractive. ActualNest/BFF/PG/nativeSession, fakeexternalHTTP only. TwoIGaccounts/sameopaquepeer must staydistinct; newwriter strictlyV2; originalV1 recovery/read iszeroHTTP withoutpoisoning legitimate NEWV2 sends afterpermittedrelease. Actualschemafield/state/endpoint oracles govern, not fabricated ordinaryreceipt/request columns. SmallASCIIbodies fit bothpendinglimits; no numericcontractchoice. Rootfreezesafterterminal beforeseparatecanonicalproof and sourcewriter. Threependinghumanproposals/primaryobserver, allconsumers and CP4..CP6/allmandatorygates remain unwaived.


## CP3 test-first02 — fixtures reconciled, preimplementation proof frozen

The sole testwriter is terminal. Root matched the two new specs and admitted helper currentSHAs, allother241existing sources,35preservedrows and3rootindex refs. Two642line sequentialcases establish candidate assertions for samepeer/twoaccount separation, explicitreplyV2metadata/sendfences, initialexclusion, originaltimestamp24hpolicy and all4ordinary/7initialV1states pluslive/deadline/unknownassociation controls. NativeNest/PG/session/OAuth/signedingress are used; only externalHTTP isfake. Staticpreexecution corrections and exactDTOdecisions are in cp3-test-first-static-alignment-02.json and cp3-test-first-terminal-reconciliation02.json. They are not testresults. Because assertions aresequential, a firstmissingendpoint404 leaves laterchecksunreached; reporteach reachedboundary honestly. TQA effectivenessaudit remains mandatory.

Helper evidencequalification: removalofobviousnewfields/messagesbranch/resetexpressions didnotreconstructtheexactprevioushelperbytes (4byte difference). No savedprivatebackup wasread and no restorationinferred. Thus no byte-identical residualhelperclaim; currenthelperbody wasread byroot and mustreceive currentregression/fullAPI andindependentreview coverage. Allother241sourcepaths and35protectedrows match exactly; no out-of-scope mutation hasbeenestablished. The threepaths areadmitted currenttestwrites; no productsource changed.

All244publicsources/currentTODO/boundinputs nowfreeze for one separatecanonical api-instagram preimplementationvalidation02. No source/T/inputwriter or concurrentrunner. Recordunit/lint/build/actualreachedintegration failures separatelyfromfixture/measurementfailures; no automaticretry/fix duringrun. Root willreconcileterminalhashes/log and onlythen explicitlythaw CP3source. Publicsubscriptiondocs recheck confirmedPOST contract but establishednoGETownappidentity/completeness/absence semantics; primaryobserver remainsopen. Userconfirmedprofessionalaccountaddedbutnotesttoken; no manualtoken/private/runtime/provider actionrequested. AllCP2repairqualifications/3humanproposals/CP3consumerproof/CP4..CP6 and mandatoryALL/stress/security/TQA/cutover/final/physicalproof remainunwaived.


## CP3 test-first02 — qualified feature RED, sole source writer03

The separatecanonical api-instagram invocation terminatedexit1. Rootmatched244sources/currentT/126inputs/35protectedrows/3indexandactualfullsyntheticlogSHA3074c5e47501601f48781b0ce54cc80bde07b98a7fc79c16245a749cf84970e4.31migrations/lint/build/398unitpassed; selected99integration executed:97oldcasespassed andbothnewcasesfailedexactreply-options404. Routingcase reachedactualOAuth/signedingress/twoaccount/samepeer isolationbeforethemissingendpoint. V1case reachedalllocalstate/replay/knownACK/unknownassociation/immutablefact/zeroHTTP checksbeforeline404. Replymetadata/newV2sends/IGpolicy/negativefences afterthefirst404 areUNREACHED, notproved. cp3-test-first02-result.json records thisqualification; no fixture/compiler barrier, no retry orproductrepairyet.

Explicitthaw is one solecodewriter under cp3-source-handoff03.json: exact21sourcepaths andlistedunitcompanions/newpurpose-specificunitglobs inapproveddomains. Implement ChannelInstagram/composition, operation-specificeligibility, strictV2operationalresolver/newwriters andseparateexactV1localfactrecovery; explicitBFFreplyoptions/existingPOSTcontext andqualifiedWAonlypublic/Typebot/Consultar/legacyprojections. Channel stayssendMessage+supportedKinds only; no new sender/framework/retry/fallback. DTOconcretizationisboundtoactualnewtestsandapprovedroutecontract. Keepcurrent1000characterWHAT untilhumanbyteproposalvalidated; do notsilentlychangeit. No newE2E/helper/schema/CP2OAuth/http/webhook/protectedclient/middleware/privacy edits inthislane; preserveall35immutablefilesandlimitedcompanions. Anyunavoidablepathneedmustbeconcretelyreportedbeforemutation.

The newtwoE2Es remainbytefrozen causaloracles. Operationalunitmockfixtures mayconcretizetheactualV2contract withoutweakeningassertions orconvertingdeliberatehistoricalV1. No runnerwhilewriteractive; returnterminalallpathhashes beforeseparatecurrentcompleteAPIandfreshadherence. Helperspriorbyte-reconstructionqualificationandallmandatoryconsumer/primary/human/CP4..CP6/ALL/stress/assurance/physicalobligationsremain. No checkpoint/featureaccepted bythisthaw.


## CP3 source03 — partial, static gaps and serialized core continuation04

Source03 is terminal and explicitly incomplete. Root matched14 changed existing files and3new files (including channel-eligibility-policy.ts),230unchanged existing sources,35preserved rows and3rootindex entries. Both new CP3E2Es/current helper and restored OAuth/window sources remain exact. No lint/build/unit/E2E ran on this candidate. The current qualified404RED receipt remains historical; source03 is not validated or accepted.

| Finding ID | Severity | Classification | Routing Decision | Same TODO rationale | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP3-ROOT-01 | high | release-blocker | fix in this TODO | D-04/D-06 abstract operation policy and bounded batch are approved scope | open | cp3-source03-terminal-preflight.json; static policy/origin switches and IG N queries |
| IG-CP3-ROOT-02 | high | release-blocker | fix in this TODO | new strictV2 and historical local recovery/tuple proof are approved scope | open | metadata expiry not selected; V2 knownACK reader absent; explicit newWA route absent; accepted-account comparison/legacy credential coupling |
| IG-CP3-ROOT-03 | high | release-blocker | fix in this TODO | SCOPE-03 requires all public/Typebot/Consultar/legacy consumers | open | author acknowledged remaining consumers; no subset acceptance |
| IG-CP3-ROOT-04 | medium | release-blocker | retain corrected provenance in this TODO | writer-path discipline and originalCP2 preservation | corrected qualified | cp3-source03-boundary-correction04.json; own additions removed exactly before any runner |
| IG-CP3-ROOT-05 | high | release-blocker | fix in this TODO | SCOPE02/06 actual verified WA ingress must establish reply route | open; shared acceptance repair14 | cp3-message-acceptance-wa-ingress14-handoff.json |
| IG-CP3-ROOT-06 | high | release-blocker | fix in this TODO | canonical peer identity must govern acceptance while preserving legacy presentation | open; shared acceptance repair14 | cp3-message-acceptance-wa-ingress14-handoff.json |
| IG-CP3-ROOT-07 | high | release-blocker | fix in this TODO | identity/contact-advisory/conversation lock order shared acceptance | open; source16 companion repairs newly introduced ordering before callback; no dynamic deadlock claimed | cp3-fixture16-lock-order-companion.json |
| IG-CP3-ROOT-08 | high | release-blocker | fix in this TODO | D-02/D-04/D-07 require qualified captured IG address for accepted and uncertain local facts | open; sender25 prepared, not applied | API22 first ordinary IG503; outbound acceptanceInput drops qualified address |

Root authorized only removal of the writer's accidental send method from the sealed OAuth client and four IG widenings plus the remaining own SQL cast from the sealed official window policy. Exact original hashes were reconstructed in memory and independently verified after correction; no Git restore, private backup or user-work discard occurred. The outgoing implementation moved into the already admitted new messaging client. These corrections add no human scope/WHAT deviation. The read-only CP4 advisor incidentally observed the changed OAuth hash while checking config; that read is not frozen or final-source evidence.

Explicit thaw04 is one fresh sole code writer for the exact core paths/unit companions in cp3-core-source-handoff04.json. Required structural work includes actual abstract operation-policy DI, bounded IG batch, one metadata/context owner, exact credential/route provenance, new explicitWA route proof and separate V1/V2 local recovery. Complete consumers follow in their own serialized lane; no approved goal is removed. The two E2Es/helper/CP2 sources/schema/protected clients remain sealed, no runner with a writer active. Root preflight and all later fullAPI/fresh adherence/consumer/ALL/stress/security/TQA/cutover/final/physical gates remain mandatory. Primary observer and the three pending human proposals stay open.


## CP3 core04 terminal source reconciliation — consumer test-first preparation

Executor único terminal. `cp3-core04-terminal-preflight.json` e `cp3-core04-public-baseline.json` registram248caminhos públicos:15existentes alterados e1spec novo em relação à fonte03;35preservados e3ponteiros do índice coincidem; nenhuma alteração fora da lane. Não houve teste/build/lint/runner pelo writer. O root leu as fronteiras corrigidas de política, metadados, rota inicial, claim final e readback; a conferência estática não aceita o núcleo nem encerra findings de corretude.

O ACK sem ID conserva UNKNOWN/ACK_WITHOUT_ID. A recuperação v2 usa a rota/identidade canônicas; v1 mantém a comparação histórica. A verificação final após claim volta a conferir contexto/janela e aplica as bordas originais de prazo antes de HTTP. Essas implementações ainda exigem provas reais descartáveis e revisão independente, inclusive falha temporal pós-claim; não transformar declaração do executor em GREEN.

A lane seguinte está preparada em `cp3-consumer-source-handoff05.json`: primeiro somente `test/instagram-consumer-isolation.e2e-spec.ts`, depois adjudicação do resultado PostgreSQL e followup explícito antes de mudar os quatro consumidores. A projeção pública que ainda admite200registros deve ser alinhada ao limite50aprovado, preservando paginação/continuação. `cp3-fixture-qualified-preparation06.json` qualifica os ajustes posteriores de testes: opções reais do servidor, rota WA comprovada e preservação dos cenários/counters/v1. As fontes fora da lane e os helpers/E2Es existentes continuam preservados.

IG-CP3-ROOT-01/02 permanecem pendentes de validação/revisão; IG-CP3-ROOT-03 permanece aberto nos consumidores. Não há aceite CP3, disponibilidade Instagram, mudança de arquivos humanos pendentes ou ativação privada/runtime.


## Human admission — exact OAuth session callback v2

Em2026-10-24 o usuário respondeu `Validar o ajuste do retorno OAuth` à call_99741f4364ad445eac91376a11faa152. O receipt `oauth-callback-session-user-admission-v2.json` vincula fonte original80d8be.../CRLF, candidata3106e6... e diff/review/merge exatos já apresentados. O caminho singular `api-app/src/surfaces/bff/session.middleware.ts` está admitido somente para essa mudança. Continua sem alteração nesta anotação; autenticação, ordem e exceções das outras rotas devem permanecer idênticas. Não tornar callback público nem ampliar a admissão para outras mudanças nesse middleware.

A execução será serializada: primeiro testes de negação confidencial pela sessão/Nest/PostgreSQL reais, controle de outras rotas e qualificação dos faults de infraestrutura; depois aplicação dos bytes revisados por writer único e validação. A prova de Numeros/gateway/browser e fullAPI/freshadherence continua obrigatória. R1-04 não está encerrado. A admissão não cobre `.env`, runtime, Meta, credenciais, worktrees ou Git de produto. Privacy HTML e limite1000UTF8bytes continuam pendentes; as menções históricas a3propostas pendentes acima descrevem seus momentos anteriores.


## CP3 consumer05/OAuth companion — test-first frozen candidate

Test-onlywriter terminal. Root leu ambos os novos specs e reconvergiu os oracles: snapshots Typebot anteriores ao ingresso, número empresarial canônico diferente de BU.phone, list/detail legados, códigos de sessão exatos. `cp3-consumer05-test-first-preflight.json` registra2specs novos e248fontes anteriores preservadas, incluindo middleware ainda original. Não foram executados testes pelo writer. Cobertura de falha inesperada de infraestrutura e guard defensivo Incoming não é alegada por esses testes.

Congelar250fontes públicas, este TODO e entradas positivas para uma execução canônica separada `bash scripts/test-channels-local.sh api-instagram`, conforme `cp3-consumer05-validation-handoff.json`. A rodada deve distinguir RED causal de consumidor/callback, eventual defeito novo no núcleo e falhas de fixture/compilação; não chamar um bloqueio anterior de prova dos asserts não alcançados. Nenhuma mudança de fonte/TODO/inputs durante a execução, apenas evidências distintas. Depois, adjudicação root e lanes serializadas de reparo/consumidores/companion; fullAPI/freshadherence, UI/ALL/assurance e runtime próprio permanecem obrigatórios.


## CP3 consumer05 canonical attempt — lint blocked before tests

Uma execução canônica terminou exit1:31migrations e setup passaram, lint encontrou8erros em4caminhos; build/unit/E2E não foram alcançados. `cp3-consumer05-validation-result.json` e `cp3-consumer05-root-reconciliation.json` registram a leitura root do log real e correspondência250fontes/150inputs/T/35preservações/3índices. Isso não é RED causal de consumidor/OAuth nem GREEN do núcleo.

Thaw limitado a `cp3-lint-repair06.json`, writer único para quatro caminhos de lint. Nenhuma semântica nova ou redução de regra; novos testes/helpers/CP2/middleware/schema ficam preservados. Depois do retorno terminal, congelar nova candidata e repetir uma execução canônica separada. O ajuste middleware já admitido só será aplicado após prova causal/qualificação; fullAPI e demais gates não foram dispensados.


## CP3 lint06 terminal — prospective canonical rerun

Writer de lint terminal. `cp3-lint06-terminal-preflight.json` confirma somente4caminhos alterados,246demais fontes preservadas. Root reconstruiu apenas em memória os8ajustes de lint e reproduziu o hash anterior exato dos4arquivos; nada foi restaurado na fonte. Não há alegação de equivalência funcional além dessa edição restrita nem de teste aprovado.

Nova candidata250fontes/T/inputs positivos será congelada conforme `cp3-consumer06-frozen-manifest.json` para uma nova execução de `bash scripts/test-channels-local.sh api-instagram`, prevista em `cp3-consumer06-validation-handoff.json`. Mesmos asserts causais preservados. Nenhum writer durante a rodada; resultado anterior é lint-bloqueado, não RED causal nem prova dos testes não alcançados.


## CP3 consumer06 canonical attempt — build blocked before tests

Uma nova execução terminou exit1 depois de setup/31migrations/generate/lint aprovados. Build Nest reportou28erros TypeScript em5caminhos; unit/E2E não foram alcançados. `cp3-consumer06-root-reconciliation.json` confirmou fonte250/inputs159/T/preservação35/índices3 e hash do log real. Não há RED causal dos consumidores ou callback nem GREEN do núcleo.

Thaw limitado a `cp3-compiler-repair07.json`: cinco fontes já admitidas, incluindo correção do nome real da relação Prisma em public/conversations.controller.ts. Honrar nullability real de staging sem enfraquecer contexto operacional v2; restaurar o shape de receipt realmente consumido pela recuperação; corrigir ordem dos parâmetros e narrowing. Nenhuma mudança em assert/regra/schema/middleware/consumidor funcional. Depois, nova candidata selada e validação canônica separada.


## CP3 compiler07 terminal — prospective canonical rerun

Writer07 terminal. `cp3-compiler07-terminal-preflight.json` confirma5fontes alteradas/245demais preservadas. O controller público mudou somente a grafia da relação Prisma: root reconstituiu bytes anteriores em memória e preservou315CRLF, zero LF isolado. O receipt de recuperação voltou a um tipo com os campos realmente consumidos; contexto v1/v2 é discriminado antes do uso. Nullability de staging foi mantida sem dispensar prova empresarial de operação nova. Nada disso é prova de build/teste.

Nova candidata250fontes/T/inputs positivos fica selada em `cp3-consumer07-frozen-manifest.json` para uma execução canônica `bash scripts/test-channels-local.sh api-instagram`, conforme `cp3-consumer07-validation-handoff.json`. Novos testes/helpers/middleware continuam inalterados; resultado06 não provou nenhum assert unit/E2E. Adjudicação posterior distingue erros de compilação/fixture de RED causal e corretude.

### Readiness humana complementar —2026-10-24
O usuário confirmou outra conta Instagram disponível para enviar DM à conta profissional e verificar a resposta quando o plano real for autorizado. Nenhuma configuração ou mensagem real solicitada agora; não autoriza runtime, token manual ou provedor.


## CP3 candidate13 reconciliation and actual WA ingress repair14

Fonte13 terminal: quatro consumidores e um spec novo; root conferiu253fontes públicas, somente os quatro caminhos admitidos mudaram em relação à baseline12. O histórico mantém fatos WA canônicos sem canal ativo/rota e sem inferir número de BU.phone; API pública/legacy BUs ficam WA-only; Incoming qualifica a identidade antes de consultar Typebot e preserva grupos WA. O controle de sessão WA do novo spec usa gatilho por palavra-chave porque a conversa já existe. Tudo permanece NOTRUN; não equivale a prova de isolamento ou regressão. Artefatos: `cp3-consumers13-terminal-reconciliation.json` e baseline positiva homônima.

A candidata exata OAuth v2 está aplicada12 (SHA3106e6...), com fault spec novo e restauração protegida, ainda sem execução. A readiness11 foi centralizada para aceitar o subestado IG SUBSCRIBED_PENDING_RECEIPT somente com CONECTADO/receipt reais; o V1 deliberado preserva todos os fatos anteriores e fornece WABA sintética só antes do novoV2. Essas fontes não foram validadas pela rodada10 anterior. R1-04 e os findings CP3 continuam abertos.

Root encontrou duas lacunas adicionais no owner comum: ingresso WA autenticado ainda não cria ConversationRoute, e aceitação/eco compara o campo legado contact em vez da identidade canônica. A premissa da preparação06 de que o webhook WA já fornecia rota está invalidada; não preencher rota após o webhook em fixture para esconder defeito real. `cp3-message-acceptance-wa-ingress14-handoff.json` delimita um único writer no serviço de aceitação e spec novo: derivar rota apenas do ingresso atual comprovado, preservar fatos/IDs/display legados e provar o percurso webhook→opçõesV2→resposta com Nest/PostgreSQL. Nenhum runtime privado, migração ou alteração Meta está autorizado.


### Core14 terminal e fixtures15/16 preparadas
Root conferiu254fontes públicas, somente MessageAcceptance alterado e um spec novo;35preservações e3índices mantidos. A correção usa identidade canônica para entradas/eco/resultados/diagnóstico, mantém display legado e deriva rota apenas de ingresso atual comprovado. Foram corrigidos estaticamente o enum do guard, a comparação de telefone formatado e o eco com conversa explícita; nenhuma execução ocorreu. Findings ROOT05/06 continuam abertos até validação/revisão.

Fixtures seguem serializadas em `cp3-fixture-lane15-handoff.json` (helpers/atendimento/transporte/boundaries) e `cp3-fixture-lane16-handoff.json` (initial/admission/public/history). WABA é opção explícita para recurso operacional atual, defaultnull preservado. Rotas sintéticas são opt-in apenas para conversas manualmente semeadas; ingresso real deve criá-las no produto. Abertura/preview inicial continua com o owner real de rota, sem efeito global na fixture; seeds históricos V1 e templates preservados. Correções estáticas de fixture não provam o produto e não dispensam a suíte atual completa.


### Fixtures15 terminal — conferência estática e próxima lane16
Root conferiu254fontes e somente5caminhos admitidos alterados, com35preservados. Os25/17cenários e89/59linhas de asserts de domínio originais foram mantidos; transporte acrescenta2asserts. O helper thenable foi corrigido antes de rodar, preservando o início não bloqueante dos testes com envio retido. Seeder permanece sem prova por default, e o empate conserva as linhas originais. No serviço, root reconstruiu o hash14 exato ao inverter somente as duas assinaturas de helpers. Isso é conferência estática, não GREEN/TQA/aceite. cp3-fixture15-terminal-reconciliation.json contém qualificações completas.

Correção da preparação: a comparação RAM do arquivo original confirma que o caso public claimoverlap já tinha uma IN; fonte15 a qualifica no lugar, sem acrescentar mensagem. A leitura anterior que afirmou ausência de IN fica invalidada. Somente pinned-bot recebe a IN anterior adicional autorizada. Lane16 inclui quatro E2E e dois companions unitários já dentro de inbox/**; depois os consumidores onboarding remanescentes exigem fixtures canônicas próprias, sem reduzir EPS/RLS/counters. Nenhuma execução ocorreu nas fontes11..15.


### Source16 lock-order discovery and remaining onboarding fixtures
A revisão estática encontrou o novo lock canônico adquirido após o callback inicial que pode bloquear a conversa. O companion16 corrige a ordem real no serviço comum, preservando o oracle do teste em vez de adaptá-lo à inversão; ainda sem execução ou prova de deadlock. A fixture de quota também separa a conta dos60novosV2 da conta dos60seedsV1 para impedir um falso positivo, e os dois POSTs de settlement restantes devem capturar contexto nativo.

A preparação17 ficou em três specs onboarding já admitidos. Root verificou que o caso PCV500 é somente SQL EXPLAIN/latestRows, não endpoint; essa amostra inteira deve permanecer sem rota e sem nova prova WABA. Só30/25pais dos endpoints e o caso único de janela necessitam rotas sintéticas antes da medição; helper atual é suficiente. A inferência anterior do advisor de que500rotas e um helper bulk novo seriam necessários foi rejeitada antes de qualquer edição. O caso caller-scoping recebe pré-condição IN oficial qualificada para responder, sem se apresentar como teste de primeiro envio.

Preparações CP4 em cp4-readonly-preparation18-root-qualified.json e cp4-live-ingress-preparation19.json não implementam/validam UI. O ingresso IG atual grava pelo owner comum, mas não publica evento de realtime; o Atendimento usa WS e fallback60s. A integração posterior deve completar esse consumidor, preservando dedup/zeroTypebot/escopo e revalidando a candidata inteira.


### Fixtures16 terminal — candidata ainda não executada
Root conferiu254fontes, exatamente7caminhos alterados e35preservações. Comparação das quatro E2E retém declarações e linhas de assertions originais, acrescentando0/60na quota; units estendem a ordem canônica sem perder callback-beforetimestamp/insert nem no-rewrite de eco. A tentativa de criar segundo Official na mesma BU foi rejeitada estaticamente pelo índice parcial e removida antes de rodar. SeedsV1 guardam conta histórica987654321; novas60reservas usam123456789, e o outro tenant prova a conta compartilhada atual por contextoV2 real. Lock canônico é adquirido uma vez antes do callback e reutilizado. cp3-fixture16-terminal-reconciliation.json registra as qualificações; não há GREEN ou aceite. Próxima lane17 limitada aos três specs onboarding preparados, seguida de validação completa da API.


### Fixtures17 terminal — candidata completa API preparada
Root conferiu254fontes públicas, somente os três onboarding specs admitidos alterados,35preservações e3índices mantidos. Diffs completos em relação aos originais RAM confirmam qualificações de fixture sem remover/assert/frouxar métricas, preservando500rawSQL e outras amostras. Caller recebe uma IN pública assinada antes do trigger, mantendo o propósito de credencial por recurso; isso não prova primeiro envio. Typebot conserva o ingresso real e somente declara WABA atual. PCV acrescenta rotas selecionadas antes das medições30/25, sem novo helper/per-row durante o request. Prova estática em cp3-fixture17-terminal-reconciliation.json, ainda NOTRUN.

Todos os writers ficam terminais e a candidata254/T/inputs positivos será selada para UMA execução canônica completa da API conforme cp3-api18-validation-handoff.json. Não haverá autofix, retry interno ou mutação durante a rodada. A adjudicação posterior separa compilação/fixture/reachability/produto e medidas; não inferir GREEN ou aceite dos testes não alcançados. CP2primary, pendências humanas, consumidorUI/realtime/browser e demais gates permanecem abertos.


### API18 terminal — lint bloqueou antes de testes
Root conferiu254fontes/T/228inputs/35preservações/3índices e SHA do log completo. Parity/setup/generate/31migrações passaram; lint parou em duas variáveis descartadas na projeção WA de me.controller.ts. Build/unit/E2E/OAuthfault/clock não foram alcançados; nenhum GREEN ou aceite. cp3-api18-root-reconciliation.json registra a prova atual. O freeze18 está encerrado. Thaw19 permite somente tornar explícito o descarte dos dois campos omitidos, no caminho já admitido, sem alterar seleção/projeção/grants/auth/testes; conferência root precede nova execução completa. CP4..CP6 e todas as pendências permanecem obrigatórias.


### Lint19 terminal — candidata completa20 preparada
Root inverteu apenas as duas expansões void/return e reproduziu o SHA original exato de me.controller.ts, preservando CRLF; as outras253fontes permanecem iguais. A nova candidata254/T/inputs positivos será selada para UMA execução canônica completa conforme cp3-api20-validation-handoff.json. Nenhuma edição de fonte/T/inputs/autofix/retry ocorrerá durante a rodada. Testes ainda NOTRUN nesta candidata.


### API20 terminal — compilação do histórico
Root reconferiu254fontes/T/242inputs/35preservações/3índices e hash do log. Lint passou; build parou em7erros TypeScript no histórico: enum de provider ampliado para string[], tuple readonly e inferência de select consequente. Unit/E2E/OAuth/clock ainda não alcançados. Freeze20 encerrado; cp3-compiler21-handoff.json limita o próximo writer a tipagem Prisma do filtro/localwhere e import type, preservando todos os filtros/fatos/queries/testes. Nenhum aceite ou GREEN de produto.


### Compiler21 terminal — nova candidata API22
Root reproduziu o SHA anterior exato do histórico ao inverter somente import/type/const e confirmou253demais fontes iguais. As annotations contextuais usam o contrato gerado Prisma sem cast permissivo. Candidata254/T/inputs será selada para UMA execução completa API22, sem writer/retry concorrente. Prova anterior20 é somente lint/compilação interrompida. Preparação CP4 também identificou endpoints de catálogo/verify/disconnect ainda ausentes e a reativação da mesma conta após tombstone como percurso obrigatório; não há UI/backend de conexões aceito por antecipação.


### API22 terminal — prova completa alcançada, sem GREEN global
Root confirmou254fontes/T/258inputs/35preservações/3índices e hash do log.31migrações/lint/build/406unit passaram; integração530/569passou e39casos falharam em11arquivos.22admissioncases param na mesma preparação antes do corpo;33falhas são classificadas estaticamente como fixture,2como oracle503do filtro existente,1como omissão real de endereço Instagram no aceite apósACK,2como limites medidos de relógio e1como timeout do batch1000. A classificação não equivale a correção provada. O primeiro caso final-clock passou e contém o assert estrito<2000; outras medidas4500/750falharam, sem relaxamento. cp3-api22-root-reconciliation.json qualifica reachability e evidência.

Freeze22 encerrado. cp3-fixture24-handoff.json admite somente7specs já autorizados e ajustes causais de dados/contexto/oracle, preservando cada cenário/limite/contador; não alterar produto, helpersglobais ou testes CP2tempo/batch. Depois será corrigido o endereço canônico que o sender Instagram descarta, com prova nativa deACK/UNKNOWN e sem retry. CP4continua preparada, não implementada; nenhuma pendência ou gate foi dispensado.


### Sender25 preparada e desempenho sem inferência
O endereço Instagram é resolvido na rota, mas reduzido a peer string antes do aceite e do diagnóstico UNKNOWN. cp3-sender-address25-handoff.json delimita correção no owner existente e prova nativa deACK/semID; só despachar após fixture24 terminal. O batch1000não tem marcador por request, portanto o timeout não identifica se ocorreu no primeiroPOST ou replay. Nenhuma perda/duplicação foi demonstrada, mas o critério15scontinua sem prova e não será relaxado. O caminho de paralelismo limitado por peer, mantendo cada transação/fence atuais e aguardando trabalho em voo antes de erro, está em avaliação somente como HOW. Nenhuma nova superfície funcional ou aceite parcial.


### Fixture24 terminal e sender25 serializado
Root reconstruiu em RAM os7SHAs anteriores exatos revertendo somente as alterações admitidas;254fontes,35preservações conferidas. Nenhum teste/runner ocorreu. Templatekind na fixture de admissão captura apenas a tupla operacional sem inventar janela/texto/histórico; legado é nulo desdeCREATE, não apagado depois. cp3-fixture24-terminal.json registra a conferência. Agora um único writer25 trata o endereçoIG no sender e seus trêscompanions já admitidos. Teste conhecidoACK tem REDnativo22; o casoUNKNOWNnovo será escrito antes da correção, sem alegar REDdinâmico ainda não executado. Campos/snapshotsV1, todas as cercas e ausência de retry preservados.


### Sender25 terminal e batch26 delimitado
Root conferiu254fontes, somente os3caminhos autorizados mudaram; leu os corpos afetados e os cenários nativosACK/UNKNOWN. O endereço qualificado é capturado da rota antes do envio e mantido no aceite/diagnóstico; snapshotsV1, inicialInstagraminapto e cercas permanecem. Não houve execução; ROOT08segue aberto.

cp3-batch26-handoff.json define HOW limitado para o timeout1000:4workers locais por peer com ordem preservada, colisão de mesma chave entrepeers volta à ordem FLAToriginal, falha interrompe agendamento e aguarda tudo em voo antes de responder. Cada mensagem mantém a transação/fence do owner comum. A proposta de atalho em receipt foi descartada: receiptVerifiedAt e connectedAt continuam atualizados como antes; nenhuma alteração MessageAcceptance/autorização/cache. Teste existente ganha medição inicial<=15s e marcadores primeiro/replay, mantendo30s/asserts/restante byte exatos. Fonte só poderá mudar por writerúnico após despacho; desempenho não é presumido.
