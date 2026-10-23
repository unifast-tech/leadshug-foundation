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
- **Next exact step:** CP1: corrigir recuperação da quarentena após recebimento e unlink concorrente apontados em r4; refazer freeze, API completo e revisão independente após invalidar a rodada r4 por edição concorrente.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** implementation
- **Why this state now:** usuário respondeu APROVADO ao contrato v1.3 em2026-10-23; execução por checkpoints, um writer, authority normal exigido antes do primeiro código.
- **Exit condition:** todos os checkpoints e critérios validados, revisões/guards completos e prova runtime posterior explicitamente aprovada; nenhum fechamento parcial implícito.

## Blocker Notes
- **Blocker:** none for approved code/disposable synthetic validation. Human approval was received; no unresolved planning blocker.
- **Runtime boundary:** ativação local real, leitura privada, Meta e prova física dependem do plano próprio posterior já exigido no contrato; não bloqueiam CP1..CP5.

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
| API | src/integrations/evolution/evolution.client.spec.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/evolution/evolution.client.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
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
Superfícies root/safe runner/CI/compose/gateway e diferenças públicas herdadas estão admitidas por caminhos exatos e inventário de preservação em evidence/inherited-public-preservation-v1.1.json. Só a zona de mutação desta fatia pode ganhar alterações; herança fora dela deve manter hashes/deleções e índice root. O resíduo root109bytes conserva a admissão exata anterior e exige companion autorizado posterior. Não executar guards integrais que enumerem/leiam/hash privados até o plano específico posterior; code approval não concede essa exceção. Nada será restaurado automaticamente para satisfazer guard.

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
| Conta profissional e acesso humano | autorização/prova real | healthy | 2026-10-23, declaração humana | usuário confirmou disponibilidade | não é teste de API/token |
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
| strategic-cto | operational-coder | contrato e código após aprovação | API/Web | active CP1; sole writer and authority/routing receipts recorded below |
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
| IG-CP1-R1-03 | high | release-blocker | fix in this TODO | durable cross-adapter resource ownership is SCOPE-02/DOD-01 | open | adherence-cp1-r3-result.json; residual current-instance trust contradiction |
| IG-CP1-R1-04 | high | release-blocker | fix in this TODO | qualified contact reuse is SCOPE-02,03 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-05 | medium | release-blocker | fix in this TODO | retained ownership/cardinality is SCOPE-02/DOD-01 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-06 | medium | release-blocker | fix in this TODO | safe canonical migration is DOD-02/VAL-02 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-07 | medium | release-blocker | fix in this TODO | preserved regression tests are SCOPE-08/DOD-09 | open | cp1-r2-repair-full-api-red.json; preserved fixture/context obligations |
| IG-CP1-R1-08 | medium | release-blocker | fix in this TODO | required historical cohort is DOD-02/VAL-02 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R2-01 | high | release-blocker | fix in this TODO | one coherent WA business scope is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; WA business scope BU agrees with CHECK/FK and actual positive route |
| IG-CP1-R2-02 | high | release-blocker | fix in this TODO | honest unverified renewal staging is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; original reservation/proof defect repaired; distinct pending lifecycle findings remain below |
| IG-CP1-R3-01 | high | release-blocker | fix in this TODO | single-create/read-before-retry after pending renewal is SCOPE-02/08 | open | adherence-cp1-r3-result.json |
| IG-CP1-R3-02 | high | release-blocker | fix in this TODO | managed cleanup ownership survives staged unlink under SCOPE-02/08 | open | adherence-cp1-r3-result.json |
| IG-CP1-R3-03 | medium | release-blocker | fix in this TODO | durable quarantine and later correct-proof recovery preserve existing channel contract | open | adherence-cp1-r3-result.json |
| IG-CP1-R3-04 | low | release-blocker | fix in this TODO | required ownership concurrency proof cannot assume winner scheduling; fix assertions in this TODO | open | adherence-cp1-r3-result.json |
| IG-CP1-ROOT-01 | high | release-blocker | fix in this TODO | pending current ingress remains retryable without content/trust before proof | open | cp1-r3-root-staged-ingress-finding.json |
| IG-CP1-R4-01 | high | release-blocker | repeat affected proof in this TODO | four mutations violated the explicit r4 freeze; preserve evidence and validate current bytes anew | open | cp1-r4-freeze-breach.json; adherence-cp1-r4-result.json |

## TODO Closeout Disposition
- **Disposition:** blocked
- **Disposition reason:** implementação aprovada em curso; findings CP1 remanescentes e demais checkpoints/gates abertos, sem entrega parcial aceita.
- **Post-commit/push status:** pending
- **Next path/status action:** manter ativo em implementation; corrigir CP1 e continuar CP2..CP6 sob a aprovação e os limites existentes.

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
| CP1 Identity/route/state cutover | running; r4 invalidated, changes required | fresh serial executor; repair prior-receipt recovery/stale unlink, then stable API and fresh review |
| CP2 OAuth/ingress | pending | follows CP1 accepted checkpoint |
| CP3 Channel/policy/consumers | pending | shared sender/acceptance only |
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
