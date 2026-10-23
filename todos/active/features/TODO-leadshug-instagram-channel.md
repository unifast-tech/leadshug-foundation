# TODO — LeadsHug Instagram Direct por Channel

## Title
ST-IG-01 — Conectar Instagram e atender DMs na mesma BU dos WhatsApps

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`
- **Artifact status:** Review
- **Contract version:** 1.0 — draft for review, sem execução autorizada.
- **Template:** copiado de `delphi-ai/templates/todo_template.md` em2026-10-23; seções aplicáveis preenchidas abaixo.

## Context
O usuário priorizou Instagram antes de histórico, confirmou conta profissional para teste e acesso para autorizá-la, confirmou a opção Instagram no app Meta existente e escolheu reunir os canais na mesma BU. A BU operacional está consolidada como arquitetura alvo; contatos, ownership empresarial e rota continuam propostas até aprovação deste contrato. ST-CON-01/04/05/06 são baseline local entregue, não código que este TODO possa substituir silenciosamente. Preservar dados e recuperar envios pendentes exige mais que acrescentar INSTAGRAM ao enum.

## Framing Source & Story Slice
- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-instagram-channel-20261023.md`
- **Primary story ID:** ST-IG-03; dependências subordinadas ST-IG-01/02.
- **Why this is the right current slice:** uma entrega funcional coesa: autorizar uma conta, receber uma DM e responder texto pelo Atendimento usando Channel. Identidade e conexão são pré-requisitos dessa mesma prova; checkpoints não declaram entregas parciais suficientes.
- **Direct-to-TODO rationale:** n/a; há brief, decisão de BU e desenho revisado.
- **Design evidence:** `foundation_documentation/artifacts/analysis/leadshug-multichannel-identity-definition-20261023.md`.

## Contract Boundary
Este TODO define WHAT, exclusões e critérios de entrega. Planejamento e baseline abaixo são propostas para aprovação. “Pode fazer” em2026-10-23 autorizou preparar o TODO/revisão, não código, banco, credenciais, runtime ou Meta. O aprovado será exclusivamente a versão revisada, após APROVADO explícito e authority guard go. Qualquer alteração material de escopo, decisões, validação, rota pública ou padrões de diff exige reconvergência e nova aprovação; descobertas locais que preservam o objetivo podem ser concretizadas dentro dele.

## Implementation Intent
- **Current delivery:** DM individual textual Instagram, iniciada pelo usuário externo; conexão explícita na BU; resposta humana pelo mesmo recurso; evolução necessária de identidade e roteamento com regressão WhatsApp.
- **Planned next steps:** mídia, importação histórica, CRM, merge de contatos, automação Instagram e outros canais; informacionais.
- **Anticipatory implementation authorized now:** none; nem código desta fatia antes de APROVADO.
- **Rationale:** identidade/ownership/rota são usados pelo percurso atual. Não criar framework de plugins, catálogo universal de capacidades ou operação futura sem uso.

## Delivery Status Canon (Required)
- **Current delivery stage:** Pending
- **Qualifiers:** Blocked
- **Next exact step:** fechar o pacote do contrato, publicar baseline documental e executar parecer arquitetural/crítica independentes; confirmar os detalhes de configuração Instagram antes de pedir aprovação.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** blocked
- **Why this state now:** planejamento em preparação, sem baseline publicado/reviews táticos e com protocolo/configuração externos ainda por confirmar.
- **Exit condition:** plano reconvergido, dependências pré-aprovação resolvidas, guards preflight-go e aprovação explícita antes de execução.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)
- **Blocker:** Q-IG-01 e gates de planejamento não concluídos.
- **Why blocked now:** opção de Instagram disponível não prova IDs/segredo/permissões do produto, assinatura ou fluxo OAuth elegível; não congelar suposições como garantia Meta.
- **What unblocks it:** evidência primária delimitada e títulos seguros do painel; reviews e guards do pacote.
- **Owner / source:** strategic steward para contrato/reviews; operador para painel Meta.
- **Last confirmed truth:** conta profissional e acesso disponíveis; app existente oferece Instagram; BU conjunta escolhida. Não reenviar perguntas já respondidas, migrar número ou desconectar WhatsApp.

## Scope
- [ ] SCOPE-01 Consolidar, após aprovação, as propostas DEC-qualified-contact-conversation, DEC-business-resource-provider-identity e DEC-explicit-channel-routing nos owners canônicos, distinguindo arquitetura e entrega.
- [ ] SCOPE-02 Estabelecer contato local e identidade externa qualificada, recursos empresariais e rotas; preservar IDs de BU/conversa/mensagem e identidades técnicas existentes.
- [ ] SCOPE-03 Migrar consumidores de telefone/tipo para identidade/rota; BFF multicanal, API pública e Typebot preservados no subconjunto WhatsApp, sem Instagram acidental.
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

Baselines Git não representam checkout limpo: `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/public-source-baseline.json` sela218arquivos API e54Web, inclusive entregas locais anteriores ainda não commitadas. Conteúdo pré-existente fora da fatia deve ser preservado por comparação de inventário/bytes; não reverter nem incluir como implementação Instagram. Contrato final de diff e root ainda serão reconvergidos antes da aprovação; não rodar varredura integral com arquivos privados neste planejamento.

### Expected Changed Paths
| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| root | scripts/test-channels-local.sh | M | safe runner/admissão de fontes e cenários Instagram |
| root | scripts/check-channels-ci-parity.py | A,M | paridade explícita dos specs novos |
| root | .github/workflows/ci.yml | M | paridade de config/testes; sem promoção |
| root | docker-compose.channels.yml | M | somente validação/variáveis públicas sintéticas da capacidade nova |
| root | docker/local-gateway.conf.template | M | callback seguro, sem query/logs privados |
| root | .env.example | M | contrato público de configuração Instagram |
| root | api-app | M | projeção de submódulo, índice não pode ser alterado |
| root | web-app | M | projeção de submódulo, índice não pode ser alterado |
| root | foundation_documentation | M | projeção documental, índice preservado |
| API | prisma/schema.prisma | M | identidade, contato, rota e OAuth |
| API | prisma/migrations/*_instagram_*/migration.sql | A | migração versionada delimitada, sem reset |
| API | src/domain/channels/** | A,M | conexões, identidade empresarial, credenciais e contratos Channel |
| API | src/domain/inbox/** | A,M | contato/rota, política, aceitação e recuperação |
| API | src/domain/tenancy/tenancy.service.ts | M | BU operacional sem exigir telefone |
| API | src/domain/historico/catalogo.ts | M | eventos seguros, sem token/conteúdo DM |
| API | src/domain/historico/cobertura.ts | M | leituras justificadas |
| API | src/integrations/channels/** | A,M | composição e resolver por vínculo/rota |
| API | src/integrations/instagram/** | A | cliente/protocolo Instagram isolados |
| API | src/surfaces/bff/** | A,M | projeções e endpoints governantes de conexões/inbox |
| API | src/surfaces/webhooks/** | A,M | callback/OAuth/ingresso Instagram sem mudar semântica WhatsApp |
| API | src/surfaces/public/conversations.controller.ts | M | conservar API v1 WhatsApp pelo namespace correto |
| API | test/*instagram*.e2e-spec.ts | A | OAuth/ingresso/isolation/routing/cutover reais |
| API | test/*multichannel*.e2e-spec.ts | A | identidades, colisões e preservação |
| API | test/*onboarding*.e2e-spec.ts | M | fixtures/asserts com a nova identidade, sem perder cenários |
| API | test/initial-message.e2e-spec.ts | M | snapshots e recuperação de aceitos |
| API | test/channel-transport.e2e-spec.ts | M | substituição por Channel e rota |
| API | test/api-publica.e2e-spec.ts | M | API antiga não trata ID Instagram como telefone |
| API | test/atendimento.e2e-spec.ts | M | inbox/claim/readback |
| API | test/webhooks.e2e-spec.ts | M | autenticação, echo e dedup |
| API | test/helpers.ts | M | seed determinístico por identidade |
| API | test/browser-server.cjs | M | backend real e fake de fronteira HTTP |
| API | test/timeline-fixtures.cjs | M | persistência/identidade sintéticas |
| API | .env.example | M | nomes de configuração sem segredos |
| Web | src/telas/Inbox.tsx | M | rota e identidade legíveis |
| Web | src/telas/Numeros.tsx | M | BU/conexões multicanal, preservando WhatsApp |
| Web | src/componentes/CadastroNumero.tsx | M | link de cadastro WhatsApp por conexão |
| Web | src/componentes/NovaConversa.tsx | M | texto/template WhatsApp e capacidades corretas |
| Web | src/componentes/*Instagram* | A | conexão/callback/estado Instagram |
| Web | src/*instagram* | A | estado puro e testes do fluxo |
| Web | src/api.ts | M | DTOs seguros e rota esperada |
| Web | src/api.spec.ts | M | contratos/erros seguros |
| Web | src/cadastroNumero* | M | lifecycle WhatsApp preservado |
| Web | src/componentes/NovaConversa.spec.ts | M | rascunho/fences/política |
| Web | e2e/instagram*.spec.ts | A | jornada browser completa |
| Web | e2e/number-onboarding.spec.ts | M | não regredir cadastro |
| Web | e2e/channel-transport.spec.ts | M | substituição e rota |
| Web | e2e/start-conversation.spec.ts | M | primeiro envio existente |
| Web | e2e/message-templates.spec.ts | M | modelo WhatsApp não elegível Instagram |
| Web | e2e/*freshness.ts | M | inventário positivo e backend real |
| Foundation | todos/active/features/TODO-leadshug-instagram-channel.md | A,M | contrato/evidências |
| Foundation | todos/completed/features/TODO-leadshug-instagram-channel.md | A | apenas após conclusão |
| Foundation | artifacts/tmp/instagram-channel-planning/** | A,M | preparação/reviews/guards públicos |
| Foundation | artifacts/reviews/leadshug-instagram-channel-20261023/** | A,M | evidências delimitadas |
| Foundation | artifacts/feature-briefs/leadshug-instagram-channel-20261023.md | A,M | enquadramento autorizado |
| Foundation | artifacts/analysis/leadshug-multichannel-identity-definition-20261023.md | A,M | desenho autorizado |
| Foundation | decisions/leadshug-multichannel-identity-decisions.md | A,M | proveniência/aceitação após aprovação |
| Foundation | decisions/README.md | M | índice singular |
| Foundation | domain_entities.md | M | identidade do contato aprovada |
| Foundation | project_constitution.md | M | consolidação estratégica já iniciada, sem claim de execução |
| Foundation | policies/scope_subscope_governance.md | M | BU operação/rotas governadas |
| Foundation | modules/*.md | M | apenas contratos tocados de identity/inbox/channels/audit |
| Foundation | backlog/README.md | M | candidato/next gate |
| Foundation | system_roadmap.md | M | prioridade antes de histórico |
| Foundation | artifacts/dependency-readiness.md | M | readiness honesta |

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
Preparação: root/safe runner/CI/compose/gateway/configuração pública e a diferença herdada completa ainda precisam de admissão exata. Não executar guards integrais nem pedir APROVADO até essa matriz estar fechada. Nada será automaticamente restaurado para satisfazer o guard.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** nomes privados de classes, índices e testes dentro das responsabilidades congeladas; correções exigidas pelo mesmo percurso.
- **Must update or split the TODO:** mídia, merge, nova plataforma, publicação Meta, outro ambiente, permissões mais amplas, política externa diferente ou novos caminhos fora da admissão estrita.

## Definition of Done
- [ ] DOD-01 Contato local, identidades qualificadas e rota persistida têm unicidade/FKs no escopo correto; nenhuma inferência por username/telefone de perfil, nem recurso empresarial em duas BUs através de adapters.
- [ ] DOD-02 Migração preserva IDs de conversa/mensagem/BU/ProviderResourceIdentity, autoria, timestamps, unread e conteúdo; proveniência desconhecida conserva sua incerteza. Snapshots/intenções antigos e conclusão local de aceitos têm cutover explícito, sem HTTP repetido.
- [ ] DOD-03 Conexão OAuth Instagram é ADMIN+, idempotente, ligada à sessão e ao recurso verificado; tokens cifrados, expirados/revogados não habilitam envio; reautorizar não muda recurso/owner silenciosamente.
- [ ] DOD-04 Webhook autentica raw body e app correto antes de conteúdo; nova entrada e replay concorrem sem duplicar contato/conversa/mensagem/unread; echo não vira entrada nem autoria humana inventada.
- [ ] DOD-05 DM textual aparece na lista/thread da BU; resposta usa rota exata pelo Channel/OutboundService, respeita política e conserva distinção entre aceitação e entrega.
- [ ] DOD-06 Cadastro/Atendimento apresentam BU, conta/origem e remetente sem tratar ID Instagram como telefone; ações/rascunhos e respostas assíncronas estão vinculados à BU/rota/geração.
- [ ] DOD-07 API v1 e Typebot WhatsApp mantêm contratos e isolamento; Instagram não entra por telefone ou ativa bot por acidente; autoria/modelos/janela atuais preservados.
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
Cada SCOPE/DOD/VAL terá linha com o texto exato do critério e prova específica antes de Local-Implemented; todos estão planned. Não existe evidência de implementação Instagram. Automatizados, operador e provider acceptance são provas diferentes; não converter um no outro.

## External Dependency Readiness (Required When External Systems Matter)
| Dependency | Why It Matters | Status (`unknown|healthy|degraded|failing|rate-limited|stale`) | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Conta profissional e acesso humano | autorização/prova real | healthy | 2026-10-23, declaração humana | usuário confirmou disponibilidade | não é teste de API/token |
| Opção Instagram no app existente | reutilização da instalação | healthy | 2026-10-23, declaração humana | usuário consultou o painel | não comprova configuração/Advanced Access |
| Documentação Meta detalhada | OAuth/assinatura/expiração/eligibilidade | rate-limited | 2026-10-23 | páginas oficiais retornaram429; coleção oficial indexada parcialmente acessível | Q-IG-01 antes de congelar protocolo |
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
| strategic-cto | operational-coder | contrato e código após aprovação | API/Web | planned, sem código |
| operational-coder | strategic-cto | consolidação de domínio/constituição | Foundation | planned |
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
- [ ] Q-IG-01 Protocolo exato Instagram Login, identificação do app/produto para OAuth e assinatura, versão API admitida, concessões, expiração/reautorização e inscrição: fechar com fonte primária/painel antes da aprovação; “tem produto Instagram” sozinho não basta.
- [ ] Q-IG-02 Admissão exata de root/CI/runner/compose/gateway e tratamento da diferença pública herdada: fechar antes da execução-readiness.

## Decisions (Resolved Before Freeze)
- D-01 BU operacional conforme escolha humana; Channel abstrato com conexões persistidas, sem telefone sintético.
- D-02 Contato local por BU e identidades qualificadas: WhatsApp pessoa E.164 compartilhado por oficial/não oficial comprovados; grupo namespace separado; Instagram por contexto de app/API+conta empresarial+peer opaco. Sem merge entre plataformas.
- D-03 Identidade empresarial única no LeadsHug atravessa adapters e mantém owner durável; ProviderResourceIdentity preserva IDs técnicos/chaves de mensagens. Conflito não transfere nem vaza.
- D-04 Rota persistida e operação capturada com vínculo exato; múltiplas contas na BU permitidas. Sem seleção pelo primeiro tipo, fallback automático ou redirecionamento por nova entrada concorrente.
- D-05 Instagram Login no produto oferecido no app existente; configuração isolada da de WhatsApp, permissões mínimas de perfil/mensagens e callback dedicado. Protocolo detalhado ainda condicionado a Q-IG-01, não promessa de elegibilidade.
- D-06 DM individual textual recebida primeiro; política própria, sem HUMAN_AGENT, prospecção, mídia/grupos ou templates. Bots Instagram desabilitados explicitamente.
- D-07 Único sender/aceitação e resultados ACCEPTED/BLOCKED/REJECTED/UNKNOWN; preservar idempotência/admissões, autoria, dedup e fences; erro/timeout não autoriza novo POST.
- D-08 Migração versionada preserva IDs/histórico e contextos persistidos; reader versionado para receipts legados comprovados, sem novos writes de identidade antiga. Não derivar rota histórica de BU.phone ou canal disponível.
- D-09 API pública v1 conserva semântica WhatsApp: accounts/conversations/messages/claim/release não aceitam nem projetam Instagram como telefone; rotas BFF evoluem com React. Typebot/session/webhooks OUT existentes devem qualificar identidade e manter automação Instagram bloqueada.
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
D-01..D-10 são o candidato a baseline, não decisões aprovadas de implementação. Q-IG-01/02 impedem o freeze final para APROVADO. A baseline publicada para review congela o pacote de diagnóstico/proposta, sem alterar esse fato.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)
- **Applicability (`required|not_needed`):** required
- **Why this applies:** aposenta BU=número no comportamento e seleção por enum único; muda identidade/rotas canônicas.
- **Deviation / debt being retired:** telefone/username como identidade de domínio e primeiro canal do tipo como endereço de dispatch.
- **Target steady-state after closeout:** BU operacional, contato/peer/empresa/provider separados, conexão e rota explícitas e um Channel/Outbound/Acceptance.

### Patterns To Enforce
DIP, DI, capacidade explícita e Liskov; constraints e transações curtas, HTTP fora de transação; ownership durável; contexto imutável de envio; dados privados apenas no adapter/crypto.

### Prohibited Anti-Patterns
Contato numérico sem namespace; casts para concreto; segredo global como fallback; copiar sender/inbox; getters que mutam provider; desligar testes/asserts para passar; truncamento silencioso de vínculos; bot Instagram ativado sem contrato; inferir rota legada; dual-write canônico indefinido.

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
- **Decision review status:** not_run
- **Decision review evidence / resolution:** pending-freeze; parecer estratégico anterior é insumo, não substituto deste pacote tático.
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
- **Baseline commit:** pending-freeze
- **Baseline push reference:** origin/main
- **Gate status:** not_run
- **Findings summary:** packet preparation only; nenhuma review/guard tática aprovada antes de publicar.
- **Evidence / reference:** pending-freeze
- **Pre-freeze packet-prep rule:** prepared-pre-freeze não equivale a passed; guards formais só depois do commit/push.

## Gate: Review Scope Drift
- **Gate decision:** required
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md`
- **Gate status:** not_run
- **Evidence / reference:** executar após reconvergência.

## Questions To Close
- Q-IG-01 e Q-IG-02 acima são materiais. Detalhe físico de classes sem efeito no contrato não vira pergunta de produto.
- O operador já confirmou profissional/acesso/BU conjunta/produto Instagram: manter fatos, sem pedir número/IDs/tokens no chat.

## Assumptions Preview
| Assumption ID | Assumption | Evidence | If False | Confidence (`High|Medium|Low`) | Handling (`Keep as Assumption|Promote to Decision|Block`) |
| --- | --- | --- | --- | --- | --- |
| A-01 | Channel/OutboundService e MessageAcceptanceService são os owners reutilizáveis de envio/aceitação; preservam contexto/admissões | api-app/src/domain/channels/transport/channel.ts; api-app/src/domain/inbox/outbound.service.ts; api-app/src/domain/inbox/message-acceptance.service.ts | reabrir diagnóstico/escopo, não criar outro sender | High | Keep as Assumption |
| A-02 | consumer atual seleciona tipo e contact string; mudança demanda mais que adapter | api-app/src/integrations/channels/prisma-channel-resolver.ts; api-app/prisma/schema.prisma; web-app/src/telas/Numeros.tsx | revisar plano, não declarar banco pronto para Instagram | High | Promote to Decision |
| A-03 | API v1 e Typebot usam endereço WhatsApp e devem ficar fora da ativação Instagram | api-app/src/surfaces/public/conversations.controller.ts; api-app/src/domain/inbox/incoming.service.ts | revisar consumers antes de code | High | Promote to Decision |
| A-04 | Protocolo/configuração Instagram Login exatos da instalação ainda não comprovados | api-app/src/surfaces/webhooks/meta.controller.ts é somente WhatsApp; opção de painel é declaração humana | bloqueia congelamento de assinatura/OAuth/política como garantia externa | High | Block |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces
Contrato de API proposto e modelo físico a seguir; lista estrita acima ainda em reconvergência Q-IG-02. Runners públicos e fixtures são owners da validação descartável. API/Web e Foundation no checkout principal, sem ambiente runtime tocado agora.

### Ordered Steps
1. CP0fechar Q-IG-01/02; diagnóstico+arquitetura e crítica no-context táticas; Plan Review completo; coherence/scope/authority pre-approval; pedir APROVADO.
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
| Root CI/paridade | runners/compose/admissão | novos specs efetivamente executados com corpo/asserts | inventário público; nenhum .env real; admissões explícitas | `python3 scripts/check-channels-ci-parity.py --self-test` e ALL | Local-Implemented | planned | relatório de admissão/freshness | Q-IG-02 fecha caminhos exatos |

### Runtime / Rollout Notes
Local primeiro, projeto runtime existente `leadshug_channels_local`; validação descartável `leadshug_channels_validation`, conforme runner. NÃO executar runtime nesta tarefa. Ativação, acesso opaco ao .env.testing, migração em DB real e callbacks/túneis dependem de plano próprio posterior. Plano deverá provar preservação de peers/volumes, snapshots/admissões pendentes, versões/checksums e abort-before-write em conflito. Lock timeout5s/statement60s nos comandos de migração; nenhum reset. Aprovação de código não publica app Meta nem autoriza produção.

## Plan Review Gate
**Status:** prepared-pre-freeze; issue cards são proposta de análise, não revisão concluída.

### Review Sections
- [ ] Architecture
- [ ] Code Quality
- [ ] Tests
- [ ] Performance
- [ ] Security
- [ ] Elegance
- [ ] Structural Soundness

### Issue Cards
| Issue ID / evidence / why now | Option A — recommended | Option B | Option C — do nothing | Recommendation |
| --- | --- | --- | --- | --- |
| IG-P01 high — schema.prisma:93/127/175/389; mesma BU terá peers não telefônicos | identidade local/qualificada, recurso empresarial+provider e rota. Effort high; risk medium; blast cross-module; manutenção medium; performance indexed; elegância/solidez improve | só adicionar enum/guardar IGSID em contact. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | manter WhatsApp-only. Effort none; risk low; blast local; manutenção neutral; performance/elegância/solidez neutral; não entrega objetivo | A, com cutover preservativo |
| IG-P02 high — prisma-channel-resolver.ts:selectCandidate; tipo não identifica conta | rota/vínculo capturados e revalidados. Effort medium; risk medium; blast cross-module; manutenção low; performance bounded; elegância/solidez improve | primeiro canal pronto/fallback. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | não habilitar Instagram. Effort none; risk low; blast local; manutenção/performance/elegância/solidez neutral | A, sem roteamento silencioso |
| IG-P03 high — meta.controller.ts só WhatsApp; Q-IG-01 aberto | protocolo/segredo/config Instagram próprios verificados; nonce/session/CAS. Effort medium; risk medium; blast module; manutenção medium; performance bounded; elegância/solidez improve | reutilizar token/WABA/segredo sem prova. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | esperar evidência antes de code. Effort low; risk low; blast local; manutenção neutral; performance/elegância/solidez neutral | A após evidência, C enquanto pendente |
| IG-P04 high — intents/admissions e receipts de ST-CON-04 persistidos | cutover versionado para dados+snapshots, reconstrução só comprovada, accepted local-only. Effort high; risk medium; blast cross-module; manutenção medium; performance bounded; elegância/solidez improve | recriar DB/IDs. Effort low; risk high; blast cross-module; manutenção low; performance neutral; elegância/solidez regress | não migrar. Effort none; risk low; blast local; manutenção/performance/elegância/solidez neutral; não entrega objetivo | A, sem reset/route guess |

### Failure Modes & Edge Cases
Mesmo ID em plataformas/contas; username mutável; propriedade conflitante entre adapters; OAuth popup cancelado/code consumido/sem sessão; token vencido/revogado; bad signature e payload oversized; eventos fora de ordem, duplicados e echo-first; timeout remoto; DB após ACK; rascunho antigo/A→B→A; janela fechada; múltiplas rotas; legacy sem proveniência; bot e APIv1 tratando IGSID como telefone; callbacks WhatsApp alterados indevidamente.

### Residual Unknowns / Risks
Q-IG-01/02 impedem pedir APROVADO. Não há medidas de desempenho ou prova de permissão real nesta etapa. SEC-R6-04, OPS-R4-01 e TQA-ST05-03 do baseline permanecem sob a coorte privada e restrições já registradas; este TODO não as resolve nem amplia público/ambiente.

## Additional Architectural Opinions
- **Needed:** yes
- **Why ambiguity remains:** modelo físico, cutover e protocolo operacional precisam de challenge no pacote completo; opinião estratégica prévia não revisou este TODO.
- **Opinion count:** 0 para este TODO
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required; fresh internal no-context reviewer, sem implementação; esperar estado terminal sem interromper/reempacotar por demora.
- **Required lenses:** correctness, performance, elegance, structural-soundness, operational-fit.

## Audit Trigger Matrix
- **Canonical method:** wf-docker-audit-escalation-method
- **Latest TEACH evidence / artifact:** pending-freeze; decisões abaixo são piso proposto, ainda não derivado por guard.

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
- **Critique status:** not_run
- **Evidence / reference:** pending-freeze.

## Rules Acknowledgement / Ingestion
Planejadas; ingestão vinculante somente após APROVADO. Não há waiver.

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
- **Routing evidence:** planned; executar antes de implementação.
- **Execution topology:** primary-checkout-single-writer
- **Subagent / delegation authorization:** workflows de executor/review; um writer de produto serializado.
- **Git isolation authorization:** not-authorized
- **Worktree authorization:** not-authorized
- **Worktree authorization reference:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** not_run
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
| Finding ID | Finding Source | Severity | Classification | Required Action | Status | Rationale / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| IG-REV-01..04 | parecer estratégico anterior | high/medium/low | release-blocker | preservar no plano/validar na implementação | open | cláusulas de ownership/dedup/cutover/limites incorporadas ao candidato; sem alegar correção do produto |

## TODO Closeout Disposition
- **Disposition:** blocked
- **Disposition reason:** contrato em preparação e revisão; não implementado.
- **Post-commit/push status:** pending
- **Next path/status action:** manter ativo; publicar baseline, executar reviews e fechar Q-IG-01/02 antes de aprovação.

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

Thresholds/amostragem e detalhes de cada lane precisam ser congelados antes da aprovação; nenhum budget de fornecedor será tratado como benchmark do produto.

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
- **Gate status:** not_run
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md`
- **Evidence / reference:** após reviews convergirem; Q-IG-01 mantém premissa bloqueante explícita.

## Approval
- **Approval status:** pending
- **Approval reference:** none; “Pode fazer” autoriza preparar/revisar contrato somente.
- **Approval scope:** nenhuma execução de produto/runtime ainda.
- **Renewed approval trigger:** mudança material de WHAT/decisões/validação/escopo ou qualquer caminho não admitido.


## Proposed Data and API Contract — candidate v1.0

Esta seção torna o candidato revisável; Q-IG-01 impede fingir que os detalhes de protocolo externo estão fechados. Os limites abaixo são políticas propostas do LeadsHug, não quotas ou garantias da Meta.

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

Todos os endpoints BFF resolvem tenant pela sessão e BU pelos grants atuais; ADMIN+ administra conexões; ATENDENTE+ lê/atende. POST exige anti-CSRF e Idempotency-Key UUID nas criações/envios. Respostas:401sem sessão,403papel insuficiente em BU conhecida,404fora do escopo,400payload inválido após autorização,409contexto/geração/conflito,429budget com Retry-After,503resultado externo inconclusivo. Erros nunca carregam payload bruto/URL/token. Nenhuma operação recebe URL externa arbitrária, WABA, credencial ou peer Instagram declarado pelo browser.

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
| POST /api/bff/conversations/:id/reply | ATENDENTE+, CSRF; text e routeId/channelId/expectedGeneration/contextFingerprint | captura rota e destinatário server-side, passa pelo único OutboundService/admissões; contexto obsoleto409, sem enviar. Ack remoto e persistência local seguem resultados existentes. |

As rotas BFF de envio existentes podem ser estendidas em vez de duplicadas caso mantenham o mesmo contrato de referência/fingerprint; a decisão exata de nome/compatibilidade deve ser congelada antes de APROVADO. Este candidato não autoriza dois senders ou dois endpoints canônicos concorrentes. API v1/account_id e telefone continuam WhatsApp-only: filtrar accounts/canais/conversations e resolver messages/claim/release/post por identidade WhatsApp. Conta sem WhatsApp não aparece como número nulo usável no contrato legado. Typebot e webhook OUT não recebem Instagram por acidente.

### Limites de produto e confiança

- Instagram textual inicialmente entre1e1000caracteres, request BFF até16KiB e webhook até1MiB com número finito de envelopes/entradas (máximo100por POST); excedentes413sem processamento parcial silencioso. Limites propostos precisam de verificação contra payloads do fluxo real, sem ampliar durante code por conveniência.
- OAuth/troca de code, inscrição e send: um dispatch por claim, timeout10s/request e no máximo3requests externos por etapa administrativa; HTTP fora da transação. Máximo10tentativas de autorização/ator/hora e30/BU/hora persistentes. verify/advance usam lease por vínculo e cooldown10s; listagens não chamam provider.
- Token nunca no bundle, URL de retorno, docs, logs, histórico, eventos ou erros. Variáveis públicas exemplificam INSTAGRAM_CLIENT_ID, INSTAGRAM_CLIENT_SECRET, INSTAGRAM_WEBHOOK_APP_SECRET, INSTAGRAM_WEBHOOK_VERIFY_TOKEN, INSTAGRAM_API_VERSION e redirect/origin permitidos; o relacionamento entre os segredos reais é Q-IG-01, sem fallback automático a META_APP_SECRET.
- Credential expiry vem de resposta verificada, com observação e mensagem segura de reautorização; nada é chamado permanente. Nenhum cron/refresh automático ou reenvio após revogação é incluído. Q-IG-01 deve fixar como adquirir/renovar um token elegível sem depender de token manual global.
- Política candidata de resposta: somente após INtextual assinada daquela conta/peer, até24hdo timestamp qualificado, com fence/lease atuais; read/echo/out/localcreatedAt não abrem janela. Esse teto é uma restrição proposta do LeadsHug, ainda não evidência de política/eligibilidade Meta do fluxo escolhido; Q-IG-01 exige fonte primária antes de APROVADO. Não há HUMAN_AGENT ou extensão de janela.
- Frontend apresenta nome/username se conhecido, plataforma e conta atendida, nunca ID opaco como telefone. Nova conversa por telefone e templates permanece WhatsApp-only; DM Instagram nasce pelo ingresso autorizado. Compositor captura rota antes de digitar; mudança de contexto não apaga nem envia rascunho em outro destino.
- Medição proposta pcv: seed10milconversas e múltiplas contas/BU; lookup exato indexado e lista50sem N+1/HTTP por conversa; cinco ondas20requisições de mesmo key e de replay, com uma aceitação/claim. Gates de tempo final e metadados da amostra devem estar definidos antes de congelar; não há benchmark realizado.

### Fontes primárias e limites da leitura

Coleção oficial Meta consultada em2026-10-23: [Instagram Login](https://www.postman.com/meta/instagram/folder/6raa77c/instagram-api-with-instagram-login), [pré-requisitos de mensagens](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api?entity=request-23987686-3fe78620-2258-44b6-893f-42d76c7200d7) e [envio de texto](https://www.postman.com/meta/instagram/request/scob1z4/text-message). Confirmam conta profissional, escopos de perfil/mensagens, início pelo usuário e referência opaca do destinatário; o exemplo inclui message_id no aceite. Não provam que o app do operador tem concessão ativa, nem entregam todo o contrato de OAuth/assinatura/renovação. Páginas Meta detalhadas retornaram429; Q-IG-01 preserva esse limite sem usar terceiros como autoridade técnica.
