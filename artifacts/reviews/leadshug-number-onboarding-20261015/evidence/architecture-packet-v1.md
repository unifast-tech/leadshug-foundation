# Bounded architecture-opinion packet
Planning only; user selected official Meta signup/unofficial QR, local first. Nova conversa proativa is next independent story, not current implementation. No waivers, no implementation approval, no existing review findings. Proposal baseline pushed ae503c7b14c3fe51d9cb3488f2fc5df2c5d17301. TODO receipt fields updated after push without material scope edits. Review full architecture/correctness/security/performance/elegance/structural soundness/operational fit; challenge concrete gaps, avoid imagined proof. Product files below are baseline/current clean. Primary provider facts/limits are summarized in included README. No tools against external providers/credentials, no code mutation.

## FILE foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md

# TODO LeadsHug — cadastro e conexão dos números oficiais e não oficiais

## Quick Start

Contrato proposto ST-CON-01, baseado no template canônico. Usuário autorizou avançar no planejamento do cadastro de números e conversas; Nova conversa informando contato é o próximo ST-CON-04. Esta revisão não é APROVADO. Fonte de produto não alterada. Pacote preparado para freeze e revisões independentes; nenhuma prova externa ou entrega reivindicada.

## Title

Cadastro e conexão dos números oficiais e não oficiais do LeadsHug, inspirado nas jornadas Central-Whatsapp e WhatsFlow.

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Tactical state:** `Review`
- **Prepared on:** 2026-10-15
- **Planning authorization:** concordância do usuário com a prioridade de conexões e preparo de testes; confirmação de disponibilidade dos dois canais. Não equivale a APROVADO do contrato.

## Context

O usuário esclareceu em2026-10-15 que quer reproduzir os processos de cadastro de números oficiais e não oficiais dos sistemas de inspiração. O objetivo é uma jornada de adicionar número, escolher modalidade e concluir autorização Meta ou pareamento QR. O rascunho anterior priorizava diagnóstico de vínculos existentes; essa interpretação foi corrigida antes de freeze/aprovação. Saúde e recebimento verificáveis apoiam o cadastro; importação permanece posterior. [Fluxos observados e jornada proposta](../../../artifacts/analysis/leadshug-number-registration-reference-flows-20261015.md).

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md`
- **Primary story ID:** `ST-CON-01`
- **Why this is the right current slice:** um objetivo: cadastrar e conectar um número por uma jornada compreensível, oficial via autorização Meta e não oficial via QR, com número e resultado confirmados. Importação tem identidade/data/efeitos próprios e fica em ST-CON-02/03.
- **Direct-to-TODO rationale:** n/a; enquadramento separado realizado.

## Contract Boundary

Proposta ST-CON-01: jornada de cadastro de número, com infraestrutura local estritamente necessária, credenciais e recebimento reais. Local primeiro, Railway depois. Mesmo TODO governa aprovação, execução e closeout. Critérios de cadastro não podem ser substituídos por mock do provedor. O usuário também pediu Nova conversa pelo contato: esse próximo recorte está enquadrado em ST-CON-04 e não é absorvido neste contrato. Mudança material retorna à revisão/aprovação; worktrees, legado e promoção produtiva não estão autorizados.

## Implementation Intent

- **Current delivery:** cadastrar/vincular número oficial pela autorização Meta e não oficial por QR, confirmar identidade e habilitar recebimento na BU; primeira IN visível na inbox prova o cadastro.
- **Planned next steps:** ST-CON-04 Nova conversa por contato e primeiro envio proativo; depois ST-CON-02/03 histórico. Transferência/anexos/status permanecem próprios.
- **Anticipatory implementation authorized now:** none
- **Rationale:** um objetivo de cadastro usável. Nenhuma tela de template, criação manual de conversa ou campanha entra por antecipação.

## Delivery Status Canon (Required)

- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** publicar baseline desta proposta, obter architecture_opinion e critique independentes, integrar achados e executar preflight antes de solicitar APROVADO.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** review
- **Why this state now:** contrato proposto sendo revisado; nenhuma implementação iniciada.
- **Exit condition:** pareceres resolvidos, coerência/drift e preflight-go; após APROVADO, authority guard normal go.

## Scope

- [ ] SCOPE-01: jornada Adicionar número na gestão de BUs: apelido e modalidade; criar BU conforme regra existente ou selecionar BU administrável, com retry sem duplicar cadastro.
- [ ] SCOPE-02: oficial por Embedded Signup configurado pela instalação, sessão/BU correlacionadas, número escolhido validado na Meta, cancelamento/falha explícitos e recebimento configurado sem tomar callback alheio.
- [ ] SCOPE-03: credencial Meta exclusiva do vínculo, cifrada no backend; envio BFF, público e Typebot usam a credencial da BU/canal, sem token de cliente global compartilhado.
- [ ] SCOPE-04: não oficial por apelido/QR em Evolution própria, com criação idempotente da instância, autenticação do webhook, confirmação do telefone e renovação de QR.
- [ ] SCOPE-05: estado do cadastro, recebimento e verificação separados; observação atrasada não reativa vínculo removido ou substitui estado mais novo. Listar BUs não consulta provider.
- [ ] SCOPE-06: receber primeira mensagem real em cada canal de teste e visualizá-la na conversa correta, preservando grants, histórico paginado e regras de janela.
- [ ] SCOPE-07: testes de contrato/segurança/races/PostgreSQL e Playwright com runtime real; prova externa separada por canal.
- [ ] SCOPE-08: runtime local próprio do LeadsHug com Evolution fixada, persistência isolada, wiring de variáveis e runbook de callback HTTPS; sem tocar runtime/dados do legado.

## Proposed Registration Contracts

Proposta técnica da jornada, subordinada ao mesmo Scope/DoD e aberta a architecture_opinion.

### BFF e autorização

- `GET /api/bff/number-registrations/capabilities`: sessão válida; expõe apenas appId/configId/Graph version e disponibilidade/explicação por modalidade, nunca app secret/token/chave. Não chama provider.
- `POST /api/bff/number-registrations`: `Idempotency-Key` UUID obrigatório, body exatamente uma origem (`buId` existente ou `novaBu:{nome,setorId?}`) e `tipo:OFICIAL|NAO_OFICIAL`. BU existente exige ADMIN nela; BU nova exige ADMIN na Mantenedora e herda grants/setor pela mesma regra transacional de TenancyService. Oficial sem app/config/crypto configurados e não oficial sem módulo contratado+teto configurado falham antes de criar BU/provider. Nova BU, reserva do canal e tentativa são atômicas no DB; refatorar reuso transacional da criação existente, preservando audit e expansão dos grants. Mesmo key/payload retorna tentativa original; mesmo key e payload diferente409. Nenhum HTTP de provider dentro da transação.
- `GET /api/bff/number-registrations/:id`: apenas ADMIN da BU e tenant da tentativa; devolve etapas, número redigido conforme DTO da BU, erro safe e progresso. Nunca devolve código/PIN/token. Sem sessão401, recurso fora do escopo404, papel insuficiente403; autorizar antes de revelar erro de payload/estado.
- `POST /:id/authorize` (prefixo anterior): oficial, nonce+code recebido no callback SDK. Pertence à sessão exata/usuário da tentativa, hash da sessão/expiração/nonce checados; CAS PENDING→PROCESSING antes de trocar code. Código não persiste nem entra em URL/log/audit. Envelope do token persistido antes dos passos seguintes. Timeout de troca fica AMBIGUO e exige nova autorização; nunca reenvia code consumido automaticamente.
- `GET /:id/options`: somente depois de autorizar; retorna WABAs/números permitidos pela credencial dessa tentativa. Backend prova app/audience, escopos e pertencimento do recurso; IDs postMessage não são autoridade. Página máxima100 e continuação explícita, sem scan infinito. Número escolhido sempre confirmado pelo operador; nunca escolher primeiro por conveniência.
- `POST /:id/confirm`: `wabaId,phoneNumberId,modoRegistro` validados contra provider e grant atual. Telefone obtido do provider deve coincidir com BU já numerada; se BU sem telefone, preencher por CAS na mesma transação do vínculo. ProviderID fica único globalmente no canal para não encaminhar webhook a duas BUs; colisão409 sem revelar tenant alheio.
- `modoRegistro:NOVO` admite PIN6dígitos e passo de register explícito conforme modalidade convencional Cloud API. `modoRegistro:JA_REGISTRADO` não redefine PIN nem chama registro destrutivo; vínculo fica pendente de prova operacional quando a leitura Meta não comprovar readiness. PIN não retorna em DTO/log, só persistência cifrada se necessário à recuperação. Não realizar migração/coexistência/unregister.
- `POST /:id/advance` e `POST /:id/retry`: uma rodada tem no máximo3requests externos, cada um timeout10s e um único lease de45s por vínculo; persistir estágio/resultado após cada passo. Não há retry automático de mutação ambígua. Read-before-retry reconcilia estágio; se não houver operação segura, declarar pendente/reautorizar em vez de fingir exactly-once externo. Assinar WABA só depois de mapping channel↔providerID local durável; webhook pode chegar antes do fim sem perder o tenant correto. Configurar callback apenas da própria instalação/conta de teste, sem override alheio.
- `POST /:id/cancel`: antes de side effect externo pode encerrar reserva; depois conserva vínculo/etapas parciais e informa limpeza necessária. Não apagar BU nem conversas, não fazer unsubscribe de WABA compartilhada automaticamente. Consumidores atuais exigem credencial e readiness do vínculo antes do OUT.
- `POST /api/bff/business-units/:buId/channels/:tipo/verify`: ADMIN, um lease por vínculo, mesmo budget3×10s; listagem nunca faz fan-out. Resultado muda só a dimensão efetivamente observada. Erros externos mapeados para códigos de catálogo, sem texto/token/URL brutos.
- QR usa rota administrativa existente; pode iniciar/renovar pairing explicitamente, geração da tentativa captura efeito. Resposta contém QR efêmero só ao admin; o QR nunca é persistido em eventos/audit. Nova UI não usa o POST antigo que conecta WABA pelo token global. Rota antiga deve recusar fluxo incompleto com instrução do contrato novo, sem fallback de token; atualizar seus testes de expectativa dentro do escopo.

### Persistência e recuperação

`ChannelRegistrationAttempt` guarda id, Mantenedora/BU/canal, tipo, userId, hash de sessão, nonce hash, idempotencyKey+requestHash, estado, versão, leaseUntil, expiresAt, stage e erro safe. Unique Mantenedora/idempotencyKey e slot BuChannel(buId,type) já existente. IDs externos únicos por tipo; migrations detectam conflito preexistente antes de impor constraint. IDs internos podem ser prealocados sem compromisso de provider.

`ChannelCredential` mantém token/PIN em envelope com keyId/version/nonce/ciphertext/tag, ligado ao canal da BU e geração; não inventar vault genérico nem refletir o envelope no model público. AAD inclui provider/BU/channelID/generation. Tamper/decrypt/key ausente falha fechado, nunca fallback global. Passar credencial por interface de adapter, sem vazá-la a audit ou payload de domínio. Não copiar secrets do ambiente legado.

Cadastro pode ficar `PENDING_AUTH`, `PENDING_NUMBER`, `REGISTERING`, `PENDING_RECEIPT`, `CONNECTED`, `ERROR`, `CANCELLED`, com dimensão de providerConnection/receipt/credential e timestamps. O enum físico e mapeamento para status atual devem ser explícitos na migração; nenhum label mágico na UI. `CONNECTED` exige etapas aplicáveis concluídas, identidade correta e conexão confirmada; oficial já registrado sem endpoint conclusivo não recebe falso CONNECTED só pela lista de números. Primeira IN autenticada pode comprovar recebimento, não validade permanente do token de saída. Teste IN/OUT externo certifica somente a execução observada, não saúde contínua.

Reserva idempotente da instância Evolution usa ID estável do canal e nunca nome do operador+timestamp. Se create retorna timeout, consultar a mesma identidade antes de retry; nenhuma segunda instância. Webhook deve ser configurado e verificado antes de concluir. Leitura de estado e evento usam geração e versionamento; retry de geração anterior não escreve após remove/recreate. Desconectar não apaga histórico. Callback tardio de instância sem vínculo não cria BU/tenant.

A tentativa expira em10min enquanto espera autorização. Após token persistido, operações de recuperação do canal são administrativas e reautorizam grant/sessão corrente; não reaproveitam code/nonce antigos. Lease expirado não é sucesso e requer reconciliação; nenhuma transação DB é mantida durante rede. Não criar worker global ou sistema genérico de jobs neste slice.

### UI e integrações

Wizard: nome/BU → modalidade → janela Meta ou QR → confirmar número → mostrar cadastro/recebimento e ação de retry quando parcial. Cancelar popup, trocar BU, desmontar tela ou nova tentativa invalida callbacks/efeitos antigos no cliente; backend ainda revalida scope. SDK em postMessage aceita apenas origens Meta exatas e formato esperado; evento é dica para seleção e não prova tenant/ID. Callback de login fica preso à geração/attempt/nonce corrente; prova server-side da credencial/ID é obrigatória.

Permissões existentes preservadas: ADMIN da BU para conectar existente; ADMIN da Mantenedora para criar BU; ATENDENTE não ganha gestão; módulo não oficial depende do teto e contratação. Dados sensíveis nunca vão a config.js/bundle. UI mostra ausência de configuração e falhas por etapa, sem exigir WABA/token manual do operador comum no fluxo Meta. Administrador pode reautorizar conta já cadastrada; credencial manual de número já registrado, se usada, é caminho técnico explícito com conferência Meta e cifra, jamais env global implícita.

BFF responder, API pública responder e Typebot continuam com suas regras/DTOs/janelas; somente lookup de credencial é refeito. DI deve convergir nos módulos BFF/público/webhook. Primeira IN cria/reusa conversa pelo contrato existente, não manual. Nova conversa por contato aguardará ST-CON-04.

### Frontend / Consumer Matrix

| Producer | Consumer | Visible behavior / invariant | Validation |
| --- | --- | --- | --- |
| capabilities | Numeros/wizard | botão disponível/indisponível com motivo | browser e contrato DTO |
| attempt/create/options/confirm | wizard | identidade, replay, autorização, cancelamento | PG E2E + Playwright |
| stage/receipt/provider state | lista BU/detalhe | nenhum falso sucesso/estado antigo | barriers + race browser |
| credencial scoped | ConversationsService BFF/público | enviar pelo canal correto e janela atual | API E2E e prova OUT |
| credencial scoped | IncomingService Typebot | responder com credencial da mesma BU | Typebot E2E |
| webhook | DB/realtime/inbox | primeira IN na conversa BU/contato correta | contrato/webhook real e readback |
| eventos audit | Histórico de atividades | ator/BU/etapa sem segredo | cobertura catálogo e E2E |

## Delivery Status Semantics

`Pending` até implementação e evidência; `Local-Implemented` exige matriz local aceita. Prova externa é registrada separadamente. `Production-Ready` e deploy não são limiares desta proposta.

## Active Work State Semantics

`review` neste draft significa preparação do contrato; não é afirmação de implementação concluída. `implementation` somente após aprovação e authority guard go.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; nenhuma entrega parcial reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

n/a no estágio de drafting. Dependências técnicas desconhecidas são explicitadas abaixo; se impedirem a execução de um gate real, registrar o bloqueio naquele gate.

## Execution Lane Tracking (Required)

- **Local implementation branches:** após aprovação, `feature/number-onboarding` em workspace/API/Web; checkout principal. Foundation permanece main.
- **Promotion lane path:** implementação e commits locais de trabalho → validação local e prova real → publicação documental Foundation. Sem push de código/deploy neste contrato.
- **Lane-promoted threshold for this TODO:** n/a; entrega local validada com provider de teste.
- **Production-ready threshold for this TODO:** não reivindicado.
- **Execution topology:** primary-checkout-single-writer
- **Git isolation authorization:** not-requested; worktrees e cópias auxiliares proibidos.
- **Subagent / delegation authorization:** workflow local todo-approval-gates-method requer reviews frescos independentes e main_instructions requer executor único; não implica Git isolation.
- **Documentation git-write authority:** Foundation main é superfície documental autônoma; git_write_authority_guard antes de commit/push.
- **Source baselines:** API ae6a9662c29b77276351aa9de653a47276372246; Web4e56f6c1f4515b918d05b8c87e890d42e8542c56; workspacecab23188ec796f79131467dcce0a16acedab8d4f. Nenhuma alteração de produto anterior a esta aprovação.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

n/a; esta proposta não autoriza promoção ou deploy.

## Out of Scope

- Nova conversa proativa/manual pelo contato: ST-CON-04 é o próximo recorte solicitado, incluindo abertura oficial por template aprovado quando necessário.
- Importação de histórico, coexistência Business App, migração de número em uso, download/envio binário, templates/campanhas, transferência e estados de entrega/leitura.
- Billing/linha de crédito de BSP: modalidade proposta é Tech Provider com cobrança direta da conta de teste; elegibilidade é precondição externa, nunca simulação silenciosa.
- Alterar callback de app/número de outro sistema, revogar credencial ou apagar instância real em uso. Usar número de teste sem integração concorrente.
- Deploy/promover código para Railway/produção. Segredos reais em commits; modificação manual de gitlinks/.gitmodules; worktrees/cópias auxiliares.

## Diff Expectation Contract (Required Before Delivery)

- **Contract status:** required
- **Policy:** strict; unclassified or forbidden paths block delivery
- **User validation:** required on deviation
- **Comparison mode:** working_tree

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| api | api-app | ae6a9662c29b77276351aa9de653a47276372246 | working_tree |
| web | web-app | 4e56f6c1f4515b918d05b8c87e890d42e8542c56 | working_tree |
| workspace | . | cab23188ec796f79131467dcce0a16acedab8d4f | working_tree |
| foundation | foundation_documentation | 41572ceb | working_tree |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/domain/channels/** | A,M,?? | Cadastro, tentativa, credencial e testes. |
| api | src/integrations/meta/** | A,M,?? | Adapter explicitamente credential-scoped. |
| api | src/integrations/evolution/** | A,M,?? | Adapter v2.3.7/QR/settings. |
| api | src/infra/config/modulos.ts | M | Bootstrap coerente antes de vincular cliente. |
| api | src/infra/config/modulos.spec.ts | M | Teste do contrato de bootstrap. |
| api | src/domain/tenancy/tenancy.service.ts | M | Reuso transacional da criação BU/grants. |
| api | src/domain/inbox/conversations.service.ts | M | Apenas resolver credencial do envio existente, sem mudar timeline/público. |
| api | src/domain/inbox/incoming.service.ts | M | Apenas credencial Typebot e prova de entrada/receipt. |
| api | src/domain/inbox/incoming.typebot.integration.spec.ts | M | Contrato scoped do caller Meta. |
| api | src/domain/historico/catalogo.ts | M | Cadastro/etapas sem segredo. |
| api | src/domain/historico/cobertura.ts | M | Cobertura dos endpoints administrativos novos. |
| api | src/surfaces/bff/channels.controller.ts | M | Manter QR/remoção/listagem e contratos coerentes. |
| api | src/surfaces/bff/number-registrations.controller.ts | A,?? | Jornada agregada e tentativas. |
| api | src/surfaces/bff/me.controller.ts | M | Projeção de cadastro/receipt; permissões atuais. |
| api | src/surfaces/bff/bff.module.ts | M | Wiring de domínio/secret store. |
| api | src/surfaces/public/public.module.ts | M | Wiring do consumer Meta. |
| api | src/surfaces/webhooks/webhooks.module.ts | M | Wiring do consumer Meta. |
| api | src/surfaces/webhooks/meta.controller.ts | M | Receipt/verificação de vínculo e geração, sem mudar auth de origem. |
| api | src/surfaces/webhooks/evolution.controller.ts | M | Eventos e geração da instância. |
| api | prisma/schema.prisma | M | Attempt/credential/status/constraints. |
| api | prisma/migrations/*number_onboarding*/migration.sql | A,?? | Migração da persistência de cadastro. |
| api | test/*canais* | A,M,?? | E2E de cadastro e idempotência. |
| api | test/*number-onboarding* | A,?? | E2E/fixtures próprios. |
| api | test/helpers.ts | M | DI dos adapters e credenciais de teste. |
| api | test/setup-env.ts | M | Configuração determinística de testes. |
| api | test/browser-server.cjs | M | Backend real e fixtures de cadastro. |
| api | test/timeline-fixtures.cjs | M | Somente credencial de fixture exigida pelo novo resolver. |
| api | test/webhooks.e2e-spec.ts | M | Receipt, auth e races. |
| api | test/atendimento.e2e-spec.ts | M | Só setup credential; invariantes existentes preservados. |
| api | test/typebot.e2e-spec.ts | M | Só setup credential; comportamento preservado. |
| api | .env.example | M | Novas variáveis sem valores reais. |
| web | src/telas/Numeros.tsx | M | Wizard de cadastro. |
| web | src/api.ts | M | Contratos/projeções e idempotency header. |
| web | src/cadastroNumero* | A,?? | Modelo/helper tipado do wizard e seus testes. |
| web | src/componentes/CadastroNumero* | A,?? | UI do fluxo e testes. |
| web | e2e/*canais* | A,?? | Browser de cadastro. |
| web | e2e/number-onboarding* | A,?? | Fixtures/freshness do fluxo. |
| web | playwright.config.ts | M | Projeto adicional com mesmo backend real. |
| workspace | docker-compose.yml | M | Repasse coerente de config não secreta; default local permanece. |
| workspace | docker-compose.channels.yml | A,?? | Overlay local provider/gateway/volumes próprios. |
| workspace | docker/local-gateway.conf.template | A,?? | Ingress local único para web/API/callback. |
| workspace | scripts/test-channels-local.sh | A,?? | Runner Node22/PG16 e freshness source-owned. |
| workspace | scripts/start-channels-local.sh | A,?? | Startup/config de validação, sem adoção de legado. |
| workspace | Makefile | M | Entradas locais do pacote. |
| workspace | README.md | M | Runbook local/providers/precondições. |
| workspace | .env.example | M | Configuração vazia/redigida. |
| workspace | api-app | M | Classificar checkout de submódulo já divergente da baseline; observe-only, não autoriza stage/write de gitlink. |
| workspace | web-app | M | Mesmo contexto observe-only; gitlink pertence à pipeline. |
| workspace | foundation_documentation | M | Publicações documentais já causam checkout divergente; não stage/write de gitlink. |
| foundation | todos/active/features/TODO-leadshug-channel-connection-readiness.md | A,M,D,R,?? | Contrato e evidence. |
| foundation | todos/completed/features/TODO-leadshug-channel-connection-readiness.md | A,R,?? | Relocação do mesmo TODO no closeout. |
| foundation | artifacts/reviews/leadshug-number-onboarding-20261015/** | A,M,?? | Pacote/reviews/guardas específicos. |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | Enquadramento e sequência. |
| foundation | artifacts/validation-plans/leadshug-channel-readiness-20261015.md | M | Prova por canal. |
| foundation | artifacts/dependency-readiness.md | M | Configuração/prontidão local. |
| foundation | backlog/README.md | M | Disposição/next gate. |
| foundation | modules/integrations-and-channels.md | M | Contratos owner. |
| foundation | modules/identity-and-tenancy.md | M | Auth das novas rotas. |
| foundation | modules/audit-and-history.md | M | Eventos sem segredos. |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .env | any | Segredo real não é diff. |
| api | .env.local | any | Segredo real não é diff. |
| web | .env* | any | Nada secreto vai para browser. |
| web | src/telas/Inbox.tsx | any | Nova conversa será ST-CON-04; timeline preservada. |
| workspace | .env | any | Arquivo privado não versionado. |
| workspace | .gitmodules | any | Ownership de pipeline. |
| workspace | .github/** | any | Sem expansão CI neste recorte. |
| foundation | project_constitution.md | any | Constituição preservada. |
| foundation | system_roadmap.md | any | Sem avanço de tema/exit gate. |
| foundation | todos/completed/features/TODO-leadshug-inbox-message-timeline-pagination.md | any | Não reescrever histórico. |

### Diff Deviation Analysis

Nenhum desvio autorizado. Classificação de gitlinks preexistentes no workspace não concede permissão de alterá-los manualmente. Fixtures adicionais encontradas necessárias devem ser admitidas antes de editadas; não modificar expectativas de negócio só para passar tests.

## Bounded But Elastic Guardrails

Cadastro/QR/autorização/recebimento pertencem a este objetivo. Nova conversa proativa, modelos, importação e tomada de callback externo não cabem como refinamento. Versão de provider, armazenamento de credencial, semântica de recuperação ou obrigação externa alteradas materialmente exigem nova revisão antes da execução.

## Definition of Done

- [ ] DOD-01: cadastro oficial e QR operáveis por administrador da BU, com número/identidade confirmados e cancelamento/falhas sem falso sucesso.
- [ ] DOD-02: tentativas de cadastro, credenciais cifradas e número externo scoped; replay/duplo clique/troca de BU/remover-recriar não duplicam ou cruzam vínculo.
- [ ] DOD-03: credencial por canal é usada por todos os consumidores Meta existentes; sem token de cliente global, logs/DTOs/artefatos sem segredo.
- [ ] DOD-04: runtime local isolado e migrations aplicáveis, orçamento externo bounded, erro/retry/frescor explícitos e webhook autenticado.
- [ ] DOD-05: primeira IN real de cada canal cria/reutiliza conversa BU/contato e aparece na inbox; resposta OUT dentro do contrato existente chega ao interlocutor.
- [ ] DOD-06: CI-equivalent API/Web/workspace, fluxo Playwright com build atual, segurança/PCV e revisões independentes aceitas.
- [ ] DOD-07: decisões consolidadas no módulo owner, evidence matrix completa, source commits e guardas go antes do closeout local.

## Validation Steps

- [ ] VAL-01: unidade/adapter para cifra e AAD, payload Meta/Evolution, erro/timeout, seleção entre múltiplos números e contrato de registro.
- [ ] VAL-02: PostgreSQL E2E para sessão/grant/tenant, tentativa expirada/cancelada/replay, disputa create/delete/recreate/verificação/evento e persistência de falha parcial.
- [ ] VAL-03: Playwright do cadastro/QR, popup cancelado/erro/timeout, mudança BU e resposta velha; backend/sessão/DB reais, servidor de provider de teste apenas como porta externa.
- [ ] VAL-04: migrate deploy e CI-equivalent API/Web/workspace da fonte final; fingerprints do bundle antes dos workers, banco exclusivo e execução sem sobreposição de suites destrutivas.
- [ ] VAL-05: prova externa local por canal, com autorização Meta/QR real, IN na BU certa, OUT recebida pelo interlocutor e recuperação permitida da conexão.
- [ ] VAL-06: EPS/FRC/BCI/RLS conforme plano; security, debt, architecture_adherence, TQA, audit especializado e final review antes de completar.
- [ ] VAL-07: consolidar módulo, validar contrato/diff/coerência e closeout; nenhum claim de produção pronta.

## Completion Evidence Matrix (Required Before Delivery Claim)

Todas as linhas abaixo estão planned. Tipo e runtime não são prova antecipada.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | Jornada Adicionar número/BU | browser+db | canais Playwright; canais E2E | local real-backend | planned | Nenhuma execução reivindicada. |
| SCOPE-02 | Scope | Embedded Signup e vínculo | contract+browser+provider | number-onboarding E2E/Playwright; VAL-05 | local + Meta teste | planned | Nenhuma execução reivindicada. |
| SCOPE-03 | Scope | Credencial cifrada scoped e consumers | unit+integration | crypto tests; atendimento/public/Typebot E2E | Node22/PG16 | planned | Nenhuma execução reivindicada. |
| SCOPE-04 | Scope | QR/instância/webhook | browser+provider | canais Playwright; VAL-05 | Evolution própria | planned | Nenhuma execução reivindicada. |
| SCOPE-05 | Scope | Estado honesto e geração | race | FRC/BCI barriers e negative control | local | planned | Nenhuma execução reivindicada. |
| SCOPE-06 | Scope | Primeira IN na conversa | provider+browser | VAL-05 e readback | local + dois providers | planned | Nenhuma execução reivindicada. |
| SCOPE-07 | Scope | Matriz/segurança | test+review | CI-equivalent e security audit | local isolado | planned | Nenhuma execução reivindicada. |
| SCOPE-08 | Scope | Runtime próprio | runtime | compose config; migrate; health; runbook | local | planned | Nenhuma execução reivindicada. |
| DOD-01 | Definition of Done | Cadastro oficial e QR usáveis | browser+provider | VAL-03/05 | local | planned | Nenhuma execução reivindicada. |
| DOD-02 | Definition of Done | Replay/tenant/races | integration+race | VAL-02 + BCI/FRC | PG16/browser | planned | Nenhuma execução reivindicada. |
| DOD-03 | Definition of Done | Credencial e consumidores | test+audit | VAL-01/02/06 + cutover | local | planned | Nenhuma execução reivindicada. |
| DOD-04 | Definition of Done | Runtime/migration/erro | runtime+test | VAL-01/04 | local | planned | Nenhuma execução reivindicada. |
| DOD-05 | Definition of Done | IN/OUT reais por canal | provider+browser | VAL-05 | números teste | planned | Nenhuma execução reivindicada. |
| DOD-06 | Definition of Done | CI-equivalent e review | test+review | VAL-04/06 | local/review | planned | Nenhuma execução reivindicada. |
| DOD-07 | Definition of Done | Canon/source/guardas | doc+guard | VAL-07 | Foundation | planned | Nenhuma execução reivindicada. |
| VAL-01 | Validation Steps | Unidade/adapter/cifra | unit | npm test | Node22 | planned | Nenhuma execução reivindicada. |
| VAL-02 | Validation Steps | PostgreSQL/auth/races | integration | npm run test:e2e | PG16 exclusivo | planned | Nenhuma execução reivindicada. |
| VAL-03 | Validation Steps | Browser com backend real | browser | npm run test:tela | bundle atual/local | planned | Nenhuma execução reivindicada. |
| VAL-04 | Validation Steps | Migration/CI/freshness | runtime+suite | runner scripts/test-channels-local.sh | local principal | planned | Nenhuma execução reivindicada. |
| VAL-05 | Validation Steps | Prova externa local | provider | checklist por canal e readback | Meta/Evolution teste | planned | Nenhuma execução reivindicada. |
| VAL-06 | Validation Steps | PCV/reviews | review+runtime | artefatos EPS/FRC/BCI/RLS + reviewers | local/no-context | planned | Nenhuma execução reivindicada. |
| VAL-07 | Validation Steps | Consolidação/diff/closeout | doc+guard | guardas específicos | Foundation | planned | Nenhuma execução reivindicada. |

## External Dependency Readiness (Required When External Systems Matter)

Register: `foundation_documentation/artifacts/dependency-readiness.md`.

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Evolution de teste e versão | Endpoint/payload/sessão reais. | unknown | n/a | Target inicial local confirmado; instância própria e versão ainda a definir. | Não usar instância legada observada no inventário Docker. |
| Meta/WABA de teste | Identidade e operação oficial. | unknown | n/a | Permissões, modalidade, número e callback. | Disponibilidade oferecida não é health check. |
| Números/interlocutores de teste | Prova IN/OUT. | unknown | n/a | Usuário confirmou disponibilidade dos dois em2026-10-15. | Confirmar target/destinatário sem publicar números pessoais. |
| Documentação oficial Meta | Cadastro/registro/assinatura. | degraded | 2026-10-15 | Coleção primária Meta Postman acessível; developers direto limitado. | Elegibilidade/app/Graph version ainda dependem de readiness; histórico fora do recorte. |

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
| operational-coder | operational-devops | Configurar e provar callback/target de teste se necessário. | Compose local/variáveis/callback e instância própria | planned; target local confirmado, nenhuma infraestrutura alterada. |

## Complexity

- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section: segurança/schema, fluxo providers, UI/integração, prova externa/closeout.
- **Why this level:** onboarding OAuth, credencial por cliente, dois providers, infra local, schema, autorização e concorrência. Uma jornada primária de cadastro; Nova conversa é história separada.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:** `foundation_documentation/modules/identity-and-tenancy.md`, `foundation_documentation/modules/inbox-and-conversations.md`, `foundation_documentation/modules/audit-and-history.md`.
- **Planned decision promotion targets:** integrations-and-channels: Cadastro de números, Credenciais por canal, Estados e contratos BFF, Callback e operação local; identity-and-tenancy: autorização das rotas de cadastro; audit-and-history: eventos sem segredos.
- **Module decision consolidation targets:** as mesmas seções antes do código das novas rotas; estado Verified apenas após validação. Constituição preservada; não reescrever decisões históricas/estudos concluídos.

## Decision Pending (Resolve Before Freeze)

Nenhuma decisão de produto pendente para a proposta. Credenciais, App/config ID, elegibilidade Meta, número de teste e origem HTTPS são precondições operacionais antes da prova externa; não se presume saúde. O desenho abaixo será desafiado no architecture_opinion antes de seu congelamento final.

## Decisions (Resolved Before Freeze)

- D-01: uma BU continua representando o número; selecionar BU administrável ou criar pelo endpoint existente; modalidade não cria tenant novo. Telefone canônico não é sobrescrito por número divergente.
- D-02: Embedded Signup Tech Provider é a jornada oficial; IDs do SDK são apenas candidatos e são verificados com a credencial obtida e o provider. Sem app configurado, botão indisponível com explicação, sem conexão simulada.
- D-03: tentativas persistidas vinculadas a usuário, Mantenedora, BU, hash da sessão e nonce aleatório; expiram em10min, consumo CAS e retry explicitamente persistido. Nada de transação DB aberta durante HTTP externo.
- D-04: credencial oficial por BuChannel, envelope AES-256-GCM com chave32bytes e keyId de instalação, nonce único, AAD provider/BU/channelId. Tokens/PIN/code só no backend; código não persiste, PIN cifrado quando necessário. Nenhuma queda para token global de cliente.
- D-05: oficial tem passos separados autorizar→validar identidade→registrar quando aplicável e explicitamente confirmado→assinar WABA→verificar recebimento; falha parcial recuperável e visível. Não sobrescrever callback de outro sistema.
- D-06: Evolution v2.3.7 fixada por digest, instância própria reservada com nome derivado do ID estável do vínculo; webhook autenticado configurado antes de afirmar cadastro completo. QR é readout efêmero, não histórico/audit.
- D-07: providerConnection/registration/receipt/lastVerification são observações distintas; timeout não inventa offline/online. Query/evento têm versão de geração e CAS; listagem apenas DB, verificação explícita bounded.
- D-08: atualizar todo consumo Meta existente (BFF/público/Typebot) para resolver credencial pelo vínculo; manter contratos públicos de resposta e janela. Bootstrap pode abrir administração/onboarding sem token de cliente já obtido; piso oficial é capacidade configurada, não número previamente conectado.
- D-09: local primeiro com Evolution/DB/cache próprios e runbook HTTPS sem domínio presumido; Railway, coexistência, histórico e Nova conversa proativa ficam fora desta entrega.
- D-10: API/Web source e runtime validados serialmente no checkout principal, um executor, sem worktrees ou mudança manual dos gitlinks.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| integrations-and-channels#invariants | Providers são adapters; segredos protegidos; erros determinísticos. | Preserve | módulo owner |
| project_constitution#system-invariants | BU/número e grants isolam operação; conversa unificada BU/contato. | Preserve | constituição |
| inbox-and-conversations#contrato-aprovado-da-timeline-da-inbox | Histórico paginado usa dado persistido, contexto e leitura protegidos. | Out of Scope | ST-ATT-01 concluído |

## Decision Baseline (Frozen Before Implementation)

Proposta de decisões D-01..D-10 versionada para a revisão. Ainda não há aprovação de implementação. Após architecture_opinion/critique, registrar resolução e congelar os mesmos IDs; divergências materiais retornam ao ciclo. Nenhum reviewer pode considerar a proposta como produto já aprovado.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability:** required
- **Why this applies:** estabelece onboarding e credencial por canal, retirando acoplamento de cliente em token global e estado conectado por simples consulta.
- **Deviation / debt being retired:** MetaHttpClient lê WHATSAPP_TOKEN global para todas as BUs; bootstrap exige token antes de cadastrar; cadastro oficial escolhe primeiro número e marca conectado; webhook não oficial só atualiza estado sem reconciliação.
- **Target steady-state after closeout:** uma jornada de cadastro por BU com credencial própria, etapas verificáveis, erro parcial durável e consumidores coerentes.
- **Temporary exceptions allowed:** none; não introduzir dual token/fallback global. Configuração privada manual de credencial existente só por migração explícita e validação de identidade, não fallback de runtime.
- **Cutover / removal condition:** source scan prova ausência de consumo global do token de cliente; boot/fixtures atualizados, todos os callers scoped, migration e negativos cross-tenant aceitos.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Provider é adapter | integrations-and-channels#invariants | Meta/Evolution | Payload externo não governa tenant/grant. |
| Um contexto por operação | identity-and-tenancy#invariants | BFF/OAuth/webhooks | IDs do SDK não são autorização. |
| Conversa BU/contato e janela | inbox-and-conversations#invariants | Consumers Meta | Cadastro não altera regras do atendimento. |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| Token de cliente global ou fallback | WHATSAPP_TOKEN lido para envio de qualquer BU | Vazamento/credencial errada entre clientes. | none |
| Conectado por listagem/cache/timeout | Sem evidência de etapa no provider | Esconde cadastro incompleto. | none |
| Credencial/OAuth raw no cliente/log | DTO, URL de log, audit ou erro externo bruto | Exposição de segredo e replay. | none |
| Callback takeover silencioso | override/reconfiguração de integração alheia | Altera operação externa sem escolha do operador. | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | scopes/credentials | API unit e canais E2E | Tenant trocado, replay, token incorreto e cifra/AAD. | implement-in-this-todo | DOD-02/03; VAL-01/02 |
| test | races | PostgreSQL barrier + Playwright | Reserva duplicada e resposta antiga após troca/remoção. | implement-in-this-todo | DOD-02/06; VAL-02/03 |
| audit | global token/callers | scan dos consumers Meta e review cutover | Atualização parcial de BFF/público/Typebot. | implement-in-this-todo | DOD-03/06; VAL-06 |
| runtime | local deployment | compose config, migrate deploy e prova providers | Configuração válida apenas em fake. | implement-in-this-todo | DOD-04/05; VAL-04/05 |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** not_run
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-number-onboarding-20261015; pending-freeze
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** not_run
- **Adherence review evidence / resolution:** planned; entrega futura
- **No-go handling:** achado material retorna ao desenho/execução; nenhum gate é dispensado.

## Gate: Review Baseline Freeze

- **Gate decision:** required
- **Why this decision:** revisar contrato exato publicado, sem aparência de evidência antes do freeze.
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** ae503c7b14c3fe51d9cb3488f2fc5df2c5d17301
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** proposta publicada em main e origin/main antes de qualquer review/guard de planejamento; atualização deste recibo não altera seções materiais.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/README.md
- **Waiver authority / reference:** n/a

## Gate: Review Scope Drift

- **Gate decision:** required
- **Why this decision:** fechar material scope após integração de reviews.
- **Trigger stage:** after planning convergence and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md
- **Gate status:** not_run
- **Findings summary:** pending-freeze
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/evidence/scope-drift.json
- **Waiver authority / reference:** n/a
- **No-go handling rule:** reconvergir/refazer freeze e reviews afetados; não implementar direção materialmente alterada sem aprovação.

## Questions To Close

- [x] Local primeiro; Railway depois.
- [x] Reproduzir jornadas de cadastro oficial Meta e não oficial QR.
- [x] Usuário também quer Nova conversa proativa por contato: próximo ST-CON-04, antes de importação.
- [ ] Precondições da prova real: app Meta/configId/versão Graph suportada e elegibilidade, número/WABA, credenciais privadas, origem HTTPS e interlocutor de teste. Não impedem preparar código/contrato; impedem declarar prova real enquanto ausentes.
- [ ] Reviews/guardas e APROVADO deste contrato antes de executar produto.

## Pattern References (Optional; Enforced When Cited)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

## Assumptions Preview (Required Before Plan Review)

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Há uma credencial global Meta hoje. | api-app/src/integrations/meta/meta.client.ts:31; conversations.service.ts:292; incoming.service.ts:125 | Corrigir diagnóstico e consumers antes do freeze. | High | Keep as Assumption |
| A-02 | Cadastro oficial atual só consulta WABA e escolhe primeiro. | api-app/src/domain/channels/channels.service.ts:31-74 | Reavaliar implementação antes de substituir. | High | Keep as Assumption |
| A-03 | Middleware BFF já exige sessão e anti-CSRF. | api-app/src/surfaces/bff/session.middleware.ts:80-171 | Reforçar superfície; nunca abrir callback BFF público. | High | Keep as Assumption |
| A-04 | Listagem UI lê DB; não há consumidor do connectionState. | web-app/src/telas/Numeros.tsx:12-19; api-app/src/integrations/evolution/evolution.client.ts:66-68 | Consolidar owner existente. | High | Keep as Assumption |
| A-05 | Usuário pode disponibilizar ambos os números de teste. | Resposta explícita nesta sessão em2026-10-15 | VAL-05 fica bloqueado, não substituir por fake. | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces

A lista do Diff Expectation Contract é a autoridade de paths. Alterar callers Meta existentes para credencial scoped, wiring por módulo Nest, domain channels, schema, controllers, Numeros e runtime local; não alterar timeline/Inbox.

### Ordered Steps

1. Publicar freeze e obter architecture_opinion/critique; resolver achados e guardas antes de pedir APROVADO.
2. Após aprovação, executor único cria branches locais e consolida contratos dos módulos antes de novas rotas.
3. Test-first: migration/reserva/idempotência/cifra e isolamento; refatorar consumers Meta e bootstrap para credenciais por canal, sem fallback global.
4. Cadastro oficial por tentativa/SDK/BFF/Graph e recuperação; não oficial por reserva/QR/webhook, protegendo generation e observações.
5. Wizard Numeros: escolher/criar BU conforme grants, modalidade, Meta/QR, confirmar número, pendência/erro/retry. Geração de UI protege popup e respostas antigas.
6. Overlay/runtime local, runner Node22/PG16/freshness; migrations e suites serializadas no banco exclusivo.
7. Prova real com app/números de teste, IN/OUT e callback. Registrar impedimento de readiness, nunca substituir por fake.
8. Architecture_adherence, TQA, segurança/PCV/debt, audit especializado com cutover e final review; canon/source/guardas; publicar docs e fechar entrega local.

### Test Strategy

- **Strategy:** test-first
- **Why:** falso sucesso, erro parcial, replay e cross-tenant precisam de testes discriminantes antes da correção.
- **Fail-first targets:** tentativa/nonce one-use, Meta token scoped emBFF/público/Typebot, callbacks/múltiplos números, provider indisponível, duplicate submit e estado antigo após delete/recreate. Capturar controle negativo quando meaningful; não alegar TDD retroativo.

### Pre-APROVADO RED Evidence Capture

- **Decision:** not_needed
- **Why now:** diagnóstico estático concluído; execução/test-support só após aprovação.
- **Target symptom:** n/a
- **Allowed surfaces:** none
- **Status:** not_run
- **Findings summary:** nenhuma implementação pré-aprovação autorizada.

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Criar BU/selecionar existente e iniciar cadastro | Save/readback e grant | web-only | Playwright mutation | yes | yes | canais spec + PG16, contas propias de fixture | n/a |
| Meta autorizar/confirmar/cancelar/falhar | OAuth e vínculo | web-only | Playwright mutation + prova externa | yes | yes | contrato local com provider stub; SDK/Meta real separado | n/a |
| QR/renew/retry/close/concluir | UI/async/backend | web-only | Playwright mutation + aparelho | yes | yes | Max-in-flight e destino preservado; QR real | n/a |
| Primeiro IN e OUT existentes | Consumer de credential e inbox | web-only | Playwright mutation + provider | yes | yes | Mesma BU e interlocutor, readback; regras de janela | n/a |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API light | Domínio/adapters/boot | Build, cifra, erros e config | Node22/container, deps lockfile | npm run prisma:generate; npm run lint; npm run build; npm test | Local-Implemented | planned | raw stdout das quatro folhas | runner source-owned resolve contexto sem host Node divergente |
| API E2E | Schema/auth/consumer | Negativas/replay/receipt e regressões público/Typebot | PG16 exclusivo e migrate deploy | npm run test:e2e | Local-Implemented | planned | raw stdout e manifest | serial, sem overlap com browser |
| Web | Wizard/helper/DTO | Cadastro/cancelamento/QR/races | backend real, fonte e bundle servidos iguais | npm test; npm run test:tela | Local-Implemented | planned | stdout e pre-worker attestation | fixture não substitui BFF/sessão/DB |
| Workspace Compose | Runtime/wiring | Config coerente, isolamento, serviços e startup | .env privado, dados novos do pacote | docker compose -f docker-compose.yml -f docker-compose.channels.yml config --quiet; make test-api; make test-web | Local-Implemented | planned | resultado sem valores de env | não imprimir config renderizado com segredos; manter superfícies broad da CI |
| Prova externa | Cadastro real | SDK/QR+IN+OUT em cada canal | app Meta elegível, HTTPS e números de teste | runbook local e checklist VAL-05 | Local-Implemented | planned | evidência redigida por canal/build | não é CI externo ou prova de SLO |

### Runtime / Rollout Notes

Local primeiro, via Docker Windows nesta sessão (Engine27.1.1 observado), Node22/PG16; nenhum serviço será tratado healthy só por inventário. Overlay channels mantém Evolution v2.3.7 por digest `sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`, Postgres/cache/volumes próprios da Evolution, rede com a API e nomes distintos do legado. O parser/adapter valida versão/payload antes da prova.

Gateway local usa imagem Web/Nginx já construída, config específica no workspace: serve /api,/webhooks,/ws para API, assets/UI para Web e /config.js com apiUrl vazio. Browser/callback partilham uma origem. Porta local dedicada configurável (padrão8082); exposição HTTPS por mecanismo de operador, URL cadastrada/allowlisted no app Meta antes do SDK real; não inventar hostname, não alterar DNS ou abrir túnel persistente automaticamente. Registro de URL só sem segredo.

Variáveis privadas: app Meta ID/secret/configID/Graph version, callback verify secret, chave de cifra/keyId, credenciais Evolution e public origin; exemplos sem valores. Configuração completamente ausente permite administração com etapa indisponível; conjunto parcial é erro de configuração. Retirar exigência de WHATSAPP_TOKEN global como precondição de boot; não aceitar esse token como fallback. Base oficial é capacidade do produto, não cliente já cadastrado. Pin/token de número já existente só entram por caminho administrativo explícito e cifrado, sem ler .env legado.

Migration cria constraints de cadastro e envelope; preflight detecta providerID duplicado/telefone ambíguo e aborta com relatório redigido, não funde/deleta dados. Canal oficial existente sem credential permanece PENDENTE_CREDENCIAL, sem tentativa silenciosa de usar token global; admin reautoriza/importa credencial explicitamente. Rollback preserva BU/conversas e pode inativar o novo vínculo; nunca apaga histórico. Railway/deploy fora deste contrato.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

Preparação de parecer, não conclusão de gate; review formal após freeze.

### Review Sections

- [ ] Architecture
- [ ] Code Quality
- [ ] Tests
- [ ] Performance
- [ ] Security
- [ ] Elegance
- [ ] Structural Soundness

### Issue Cards

- **Issue ID:** PLAN-NUM-01
  - **Severity:** high
  - **Evidence:** meta.client.ts:31 e consumers sem credential explícita.
  - **Why it matters now:** credenciais de clientes diferentes não podem compartilhar token.
  - **Option A (Recommended):** secret store por vínculo cifrado e resolver único scoped; esforço alto, risco controlado por migration/testes, blast radius cross-module, manutenção média, performance neutral com lookup indexed, elegância/coerência melhoram.
  - **Option B:** token por instalação e um cliente por deploy; esforço médio, risco de limitar multitenancy, blast radius cross-stack, manutenção alta, performance neutral, elegância/estrutura regredem no produto multi-tenant.
  - **Option C (Do Nothing):** esforço baixo, risco alto de credencial incorreta, manutenção alta, performance neutral, elegância/estrutura regredem; rejeitada.
  - **Recommendation:** A; sem fallback global.
- **Issue ID:** PLAN-NUM-02
  - **Severity:** medium
  - **Evidence:** cadastro externo faz HTTP antes do registro local; QR/callback e token exchange podem falhar parcialmente.
  - **Why it matters now:** replay/duplo clique pode duplicar instância ou perder código consumido.
  - **Option A (Recommended):** reserva+tentativa persistida, CAS e retomada por etapas; esforço médio, risco médio, blast radius module, manutenção média, performance bounded, elegância/estrutura melhoram.
  - **Option B:** HTTP síncrono seguido de create simples; esforço baixo, risco alto, manutenção alta, performance regressa sob retry, estrutura frágil.
  - **Option C (Do Nothing):** mantém cadastro inconsistente; esforço baixo, risco alto, performance unknown, estrutura/elegância regredem.
  - **Recommendation:** A.

### Failure Modes & Edge Cases

Cancelar/fechar popup; code expirar; sessão/grant revogado entre etapas; IDs SDK falsos; WABA múltiplos números; nonce repetido; registro parcial; webhook não assinado; provider retornar número diferente; remove/recreate enquanto consulta pendente; resultado do QR de BU antiga; erro de decriptação/keyId ausente; provider em timeout; callback já em outro sistema; credencial expirada depois do cadastro; primeiro IN e envio Typebot usando credencial própria.

### Residual Unknowns / Risks

Meta app/Graph version e número real ainda não verificados; arquitetura pode ser implementada mas não certificada externamente sem readiness. Evolution stable fixada não é prova de compatibilidade em operação. Crypto protege DB, não protege comprometimento da aplicação/key. Não prometer SLO ou produção pronta.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

Architecture decision review requerida após freeze do pacote e antes do congelamento final de decisões; reviewers fresh no-context, evidence/resolution serão registrados. Nenhum parecer foi antecipado.

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md
- **Latest TEACH evidence / artifact:** pending-freeze

| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | Onboarding e credenciais. |
| blast_radius | cross-stack | API/Web/Compose. |
| behavioral_change_or_bugfix | yes | Cadastro novo e correção do vínculo. |
| changes_public_contract | yes | BFF/schema/config. |
| touches_auth_or_tenant | yes | OAuth/BU/segredos. |
| touches_runtime_or_infra | yes | Runtime local/callback. |
| touches_tests | yes | Testes/fixtures/runners. |
| critical_user_journey | yes | Cadastro utilizável. |
| release_or_promotion_critical | no | Local; sem promoção produtiva. |
| high_severity_plan_review_issue | yes | PLAN-NUM-01. |
| explicit_three_lane_request | no | Audit especializado derivado, não pedido humano. |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

- **Critique decision:** required
- **Why this decision:** big/cross-stack/OAuth/tenant/runtime.
- **Impact signals in scope:** public contract/schema/api, auth, runtime, cross-module
- **Package mode:** bounded-file-set
- **Package minimum contents:** frozen baseline, proposta/limites, código citado, plano, riscos, achados prévios e resolução
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; não é executor, sem contexto da conversa; aguardar até terminal sem deadline arbitrário.
- **Canonical multi-lane audit protocol:** audit-protocol-triple-review; entrega recomendada pelo floor, será executada antes de fechar.
- **Critique lenses:** correctness, performance, elegance, structural-soundness, risk
- **Critique status:** not_run
- **Findings summary:** pending-freeze
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/planning-critique.json
- **Waiver authority / reference:** n/a

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** as alterações dependem de consumers e superfícies reais.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01,A-02,A-03,A-04
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md
- **Gate status:** not_run
- **Findings summary:** pending-freeze
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/evidence/code-coherence.json
- **Waiver authority / reference:** n/a

## Approval

- **Approved by:** none
- **Approval scope:** nenhum contrato de implementação aprovado.
- **Execution not authorized by approval:** toda implementação/runtime e envio real neste draft.
- **Renewed approval required when:** escopo, decisões, validação ou risco material mudarem após futura aprovação.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

Planejadas antes de execução; reload binding após APROVADO.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | Fronteira executor/review/Git. | um writer e gates | worktree/gitlink manual | delegar execução |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | Aprovação tática. | APROVADO+guard | iniciar por concordância genérica | bloquear produto antes do guard |
| delphi-ai/workflows/docker/environment-readiness-method.md | Compose/runtime. | target próprio | usar legado/segredo em log | readiness antes da prova |
| delphi-ai/workflows/docker/effort-selection-method.md | Model/role. | execução medium/review max | autodelegação implícita | routing guard |
| foundation_documentation/policies/scope_subscope_governance.md | Ownership das rotas. | contratos do owner | controller sem owner | doc antes do código |
| foundation_documentation/policies/central_whatsapp_independent_legacy_policy.md | Inspiração. | comportamento redesenhado | copiar source/runtime/dados | só referência |
| delphi-ai/workflows/docker/todo-closeout-promotion-method.md | Entrega e fechamento. | mesmo TODO/evidência | claim prematuro | guardas antes de fechar |

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Subagent / delegation authorization:** requerida por main_instructions e workflow todo-approval-gates-method; execução apenas após APROVADO
- **Execution topology:** primary-checkout-single-writer
- **Worktree / auxiliary-checkout authorization:** not-authorized
- **Worktree authorization evidence:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

Reviews serão fresh no-context gpt-6.1-sol/max para architecture_opinion e critique, com routing guard distinto; nenhuma configuração da sessão primária é fingida.

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
- **Disposition reason:** planejamento/revisão, sem implementação aprovada.
- **Post-commit/push status:** n/a
- **Next path/status action:** resolver reviews/guardas e solicitar aprovação do contrato; mesmo TODO mantém evidência.

## Security Risk Assessment (Mandatory Before Delivery)

- **Risk level:** high
- **Gate decision:** required
- **Why this risk level:** OAuth, credential por cliente, popup/origem, webhook e grants mutáveis.
- **Attack surface in scope:** sessão+anti-CSRF BFF; origem exata Meta no postMessage; código/nonce de uso único; IDs não confiáveis; token cipher/AAD; scopes de caller.
- **Attack simulation decision:** required
- **Review evidence:** planned; negativos de replay, cross-tenant, sessão/grant revogado, origem/popup forjado, ciphertext adulterado, redirect de provider e erro redigido.
- **Residual security risk:** crypto não protege aplicação comprometida; credenciais não entram em raw webhook/audit, DTO, URL registrada, Playwright trace/screenshot ou artefato. URL Evolution só de configuração allowlisted; não aceitar URL livre do operador.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** OAuth/HTTP e DB em etapas, requests retriggerable e observações concorrentes.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-DATA-PATH-CHANGED | before_local_implemented | EPS-E1 | pending | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-POLICY | pending | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-DUPLICATE-SUBMIT-OR-REPLAY | before_local_implemented | BCI-INV | pending | none | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-QUEUE-WORKER-REALTIME-CHANGED | before_local_implemented | RLS-E1 | pending | none | none |

#### EPS
Lookup único por vínculo/tentativa e índice de expiração, EXPLAIN na tabela representativa; sem fan-out em listagem. Perfil EPS-SP-STRONG, aceitação EPS-A1; medição local e limites documentados.
#### FRC
Coalescer duplo clique; cancela contexto anterior, descarta versão velha; repetição forte10triggers×3, requests/in-flight e estado/draft observáveis. Perfil FRC-SP-M; FRC-A1.
#### BCI
CAS na tentativa, unicidade de slot/providerID e geração;10operações sobrepostas×3 com barriers para criação, finalize/replay e delete/recreate, controle negativo. Perfil BCI-SP-M; BCI-A1. Sem exactly-once de provider afirmado; timeout externo ambíguo fica pending.
#### RLS
Uma etapa bounded com cinco clientes e seis leituras por cliente,30verificações internas/conflitos, zero chamada provider em listagem. Perfil RLS-SP-L; RLS-A1. Não é benchmark de capacidade/SLO; provider real não recebe carga sintética.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

- **Audit outcome:** none
- **Why this outcome:** nenhum produto alterado ainda; audit obrigatório após implementação.
- **Inline code TODO debt:** none
- **Evidence / audit artifact:** planned, sem claim de audit realizado.
- **Accepted residual debt:** none; VAL-05 externa não pode ser dispensada implicitamente.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Audit decision:** required
- **Why this decision:** big/cross-stack, OAuth/tenant/runtime/testes.
- **Package mode:** bounded-file-set
- **Audit isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; distinto do executor, aguardar terminal sem deadline arbitrário.
- **Audit status:** not_run
- **Findings summary:** planejado para após implementação/prova primária; não foi dispensado.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015
- **Canonical multi-lane audit protocol:** audit-protocol-triple-review
- **Waiver authority / reference:** n/a

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Final review decision:** required
- **Why this decision:** big/cross-stack, OAuth/tenant/runtime/testes.
- **Package mode:** bounded-file-set
- **Final review isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; distinto do executor, aguardar terminal sem deadline arbitrário.
- **Final review status:** not_run
- **Findings summary:** planejado para após implementação/prova primária; não foi dispensado.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015
- **Canonical multi-lane audit protocol:** audit-protocol-triple-review
- **Waiver authority / reference:** n/a

## Independent Cutover Integrity Audit Gate

- **Audit decision:** required
- **Why this decision:** credencial global é retirada; todos os consumers precisam convergir, sem shim/fallback.
- **Audit status:** not_run
- **Evidence / reference:** audit-protocol-triple-review após implementação; sem dispensa.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

n/a; sem claim Production-Ready ou promoção remota.

## Module Consolidation Gate (Required Before `Completed`)

- **Gate decision:** required
- **Gate status:** not_run
- **Evidence / reference:** módulos owner e contratos antes do código; Verified somente depois de evidência aceita. Nenhuma alteração de constituição planejada.

## Commands (Run Locally)

Após APROVADO: runner source-owned API/Web e compose local; executar folhas documentadas na matriz. Segredos vêm do ambiente privado e não aparecem em comando/log. Antes de executar, routing e readiness do executor go. Nenhum comando de produto rodado nesta fase.

## Files Expected (Compatibility Note)

O Diff Expectation Contract é a referência candidata; completar lacunas antes do freeze. Nenhum Files Expected paralelo concede novos paths.

## COMENTÁRIO:

Nenhum comentário de aprovação pendente foi tratado como APROVADO.


## FILE foundation_documentation/project_constitution.md

# LeadsHug — Project Constitution
**Version:** 1.0

## Purpose and stack

Esta constituição governa o LeadsHug, uma central multi-tenant de relacionamento por WhatsApp. O stack ativo
é NestJS, React, PostgreSQL, Prisma, Docker e Railway.

## Authority hierarchy

1. Documentos canônicos vigentes deste foundation. Uma decisão `Accepted` só se torna efetiva depois que todos os seus alvos canônicos nomeados forem consolidados; sua direção passa a valer por meio desses alvos atualizados, nunca por sobreposição do registro de decisão. Antes disso, o registro preserva racional e proveniência, mas não compete com a verdade corrente.
2. TODO tático ativo e aprovado.
3. Código e testes do repositório LeadsHug.
4. Regras e workflows reutilizáveis do `leadshug-engineering`.

Quando houver conflito, a regra mais específica do produto prevalece sobre a regra genérica de engenharia.

## System invariants

- API, DTO and response projection changes require matching contract-test expectation updates in the same TODO.
- Prisma schema changes require an applicable versioned migration; changes to either the schema or migration files require `prisma migrate deploy` and CI database validation.
- Environment, port and topology changes require local validation with the same configuration as CI.
- Web-flow changes require Playwright against a freshly built bundle and the real validation backend using the same `DATABASE_URL` and resolved API port/endpoint as the CI-equivalent job, without exposing secrets.

- Toda implementação possui um TODO ativo, escopo, Definition of Done e evidência de validação.
- A Mantenedora contém Setores; a Business Unit é o número de WhatsApp.
- Grants e leituras são sempre filtrados pela BU e pela conta correta; vazamento entre tenants é falha crítica.
- Canal oficial e não oficial são transportes da BU; a conversa é unificada pelo par BU/Contato.
- BFF, API pública, API interna e webhooks são superfícies distintas, com autenticação própria.
- Domínio e regras de negócio pertencem ao backend NestJS; React consome contratos explícitos.
- Persistência usa PostgreSQL via Prisma; acesso ao banco não deve contornar a fronteira de domínio.
- Serviços executam em Docker e são promovidos pela topologia Railway declarada no projeto.
- Histórico de atendimento é persistente, consultável conforme permissão e auditável.
- Templates, disparos, CRM e campanhas só entram em execução mediante TODO e contrato próprios.

## TODO governance

`backlog/` registra candidatos não aprovados e é separado de `todos/active/`. `todos/active/` contém contratos
táticos vivos, mas sua localização nunca concede execução: somente `APROVADO` explícito e o authority guard em
`go` a concedem. Um TODO concluído deve conter evidência específica, validação e referência de branch/commit.

O lifecycle canônico em [evolution_lifecycle.md](evolution_lifecycle.md) define schemas, transições, papéis
neutros de fornecedor e owner singular por campo. Backlog possui disposição/próximo gate; roadmap possui tema,
horizonte, resultado, dependências e exit gate; módulos possuem verdade local estável; TODOs possuem
aprovação/execução/evidência; decisões possuem racional/histórico; briefs e artifacts são evidência, não
autoridade concorrente.

## Profiles and handoffs

- Genesis define a primeira arquitetura documental.
- Strategic/CTO-Tech-Lead governa constituição, lifecycle e roadmap.
- Operational/Coder implementa backend, frontend e testes por TODO.
- Operational/DevOps governa Docker, Railway, CI e runtime.
- Assurance valida qualidade, aderência e segurança.

## Lifecycle roles

- A autoridade humana de decisão valida escopo, produto e aprovação material.
- O strategic steward governa constituição, lifecycle e roadmap.
- O module owner governa ownership, invariantes e contratos locais.
- O TODO owner/executor executa somente o contrato aprovado e mantém suas evidências.
- O assurance reviewer valida qualidade, aderência e segurança sem adquirir autoridade de produto.

Ferramentas, agentes e fornecedores concretos são adapters desses papéis, não autoridade de produto.

## Explicit non-goals

Não ativar capacidades de stack não declaradas no topology do LeadsHug sem decisão documental específica.


## FILE foundation_documentation/modules/integrations-and-channels.md

# Module: Integrations and Channels
**Version:** 1.0

Owns Meta Cloud API, Evolution/Baileys, outbound webhooks, API keys and transport adapters.

## Invariants

- Providers are adapters; business workflows do not depend on provider payload shape.
- Secrets never enter logs, docs, fixtures or client bundles.
- Provider failures become deterministic application errors.


## FILE foundation_documentation/modules/identity-and-tenancy.md

# Module: Identity and Tenancy
**Version:** 1.0

Owns authentication, accounts, Mantenedoras, Setores, Business Units, roles and BU grants.

## Invariants

- Every request resolves one tenant/account context.
- Permissions are materialized at the BU boundary.
- Roles are `OWNER`, `ADMIN` and `ATENDENTE`.

## API Endpoint Definitions

The canonical BFF contracts live under `LeadsHug/apps/api` and must be documented here before new endpoints
are introduced.


## FILE foundation_documentation/modules/inbox-and-conversations.md

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


## FILE foundation_documentation/modules/audit-and-history.md

# Module: Audit and History
**Version:** 1.0

Owns durable activity history, message auditability, exports and access to historical relationship data.

## Invariants

- History is append-oriented and is not silently discarded.
- Every record is tenant- and BU-scoped.
- Read permission is evaluated independently from write permission.


## FILE foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/README.md

# Cadastro de números — planejamento ST-CON-01

Contrato governante: [TODO](../../../todos/active/features/TODO-leadshug-channel-connection-readiness.md). Proposta em preparação para revisão; nenhuma execução de produto ou aprovação reivindicada.

Escopo: cadastro guiado oficial Meta e não oficial Evolution/QR, integração com BU, recebimento e primeira conversa recebida para validar o vínculo. Nova conversa proativa é ST-CON-04, próximo recorte solicitado pelo usuário; importação segue depois.

Baseline de fonte: API `ae6a9662c29b77276351aa9de653a47276372246`; Web `4e56f6c1f4515b918d05b8c87e890d42e8542c56`; workspace `cab23188ec796f79131467dcce0a16acedab8d4f`. Foundation baseline/freeze será registrado após commit/push do pacote completo.

Fontes primárias consultadas em2026-10-15:

- [Meta: Embedded Signup](https://www.postman.com/meta/whatsapp-business-platform/collection/du6gzjv/embedded-signup): autorizar cliente é seguido de etapas de integração; elegibilidade do app continua dependência externa.
- [Meta: registro do número](https://www.postman.com/meta/whatsapp-business-platform/request/mk4p87j/register-phone-number): registro separado, com PIN de seis dígitos. Cadastro/autorização não bastam para afirmar canal pronto.
- [Meta: assinatura da WABA](https://www.postman.com/meta/whatsapp-business-platform/request/0yubu4i/subscribe-app-to-whatsapp-business-account): assinatura integra o recebimento. Não autoriza trocar callback de número em outro sistema silenciosamente.
- [Meta: janela de suporte](https://www.postman.com/meta/whatsapp-business-platform/folder/fuaee8l/statuses-object): abertura proativa oficial exige tratamento de templates fora da janela; ST-CON-04 terá contrato próprio. Campos de preço históricos dessa fonte não são adotados.
- [Evolution: releases oficiais](https://github.com/evolution-foundation/evolution-api/releases): v2.3.7 stable; versão2.4 pre-release não foi escolhida.

Consulta read-only ao registry confirmou `evoapicloud/evolution-api:v2.3.7` com índice OCI `sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`; runtime novo deve registrar a versão efetiva antes de prova. Não se adota o container legado.

As páginas developers.facebook.com continuam limitadas; coleção primária da Meta em Postman foi acessível. A configuração efetiva do app, Graph version admitida, WABA de teste e callback devem ser verificadas antes da prova externa; referência histórica não substitui verificação.


## FILE api-app/src/domain/channels/channels.service.ts

import {
  BadRequestException,
  ConflictException,
  Inject,
  Injectable,
  ServiceUnavailableException,
} from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import {
  EVOLUTION_CLIENT,
  EvolutionClient,
  EvolutionIndisponivelError,
} from '../../integrations/evolution/evolution.client';
import { META_CLIENT, MetaClient, MetaIndisponivelError } from '../../integrations/meta/meta.client';

export type TipoDeCanal = 'OFICIAL' | 'NAO_OFICIAL';

/**
 * Conectar um número a uma BU (ADR-0008 §2): o canal é vínculo da BU, no máximo
 * um de cada tipo. A janela de 24h é atributo do canal, não do produto
 * (ADR-0009 §3) — quem decide é o tipo, não quem cadastrou.
 */
@Injectable()
export class ChannelsService {
  constructor(
    private readonly prisma: PrismaService,
    @Inject(META_CLIENT) private readonly meta: MetaClient,
    @Inject(EVOLUTION_CLIENT) private readonly evolution: EvolutionClient,
  ) {}

  async conectarOficial(buId: string, wabaId: string) {
    if (!/^\d{5,}$/.test(wabaId)) {
      throw new BadRequestException({ error: 'WABA ID inválido: use só os números do ID.', code: 'WABA_INVALIDO' });
    }
    if (!this.meta.configurado()) {
      throw new ServiceUnavailableException({
        error: 'Canal oficial não configurado no servidor (WHATSAPP_TOKEN).',
        code: 'CANAL_NAO_CONFIGURADO',
      });
    }
    await this.exigirCanalLivre(buId, 'OFICIAL');

    // Valida o WABA na Meta E captura o phone_number_id na mesma ida — é o que
    // faz a conta nascer pronta para enviar, sem preenchimento manual.
    let numeros;
    try {
      numeros = await this.meta.numerosDaWaba(wabaId);
    } catch (e) {
      const detalhe = e instanceof MetaIndisponivelError ? e.detalhe : 'A Meta recusou a consulta.';
      throw new BadRequestException({ error: detalhe, code: 'META_RECUSOU' });
    }
    if (numeros.length === 0) {
      throw new BadRequestException({ error: 'Esta WABA não tem número disponível.', code: 'WABA_SEM_NUMERO' });
    }

    const numero = numeros[0];
    const canal = await this.prisma.buChannel.create({
      data: {
        buId,
        type: 'OFICIAL',
        status: 'CONECTADO',
        wabaId,
        phoneNumberId: numero.id,
        // A Meta recusa texto livre fora das 24h. É regra da plataforma, então
        // é o tipo do canal que a liga — nunca uma escolha de quem cadastra.
        requiresWindow: true,
        connectedAt: new Date(),
      },
    });

    if (numero.telefone) {
      await this.prisma.businessUnit.update({ where: { id: buId }, data: { phone: numero.telefone } });
    }
    return { canal, telefone: numero.telefone, nomeVerificado: numero.nomeVerificado };
  }

  async conectarNaoOficial(buId: string, nomeDaBu: string) {
    if (!this.evolution.configurado()) {
      throw new ServiceUnavailableException({
        error: 'Canal não oficial não configurado no servidor (EVOLUTION_API_URL/KEY).',
        code: 'CANAL_NAO_CONFIGURADO',
      });
    }
    await this.exigirCanalLivre(buId, 'NAO_OFICIAL');

    const nomeInterno = nomeDeInstancia(nomeDaBu);
    let criada;
    try {
      criada = await this.evolution.criarInstancia(nomeInterno);
    } catch (e) {
      throw new BadRequestException({
        error: e instanceof EvolutionIndisponivelError ? e.message : 'A Evolution API recusou a criação.',
        code: 'EVOLUTION_RECUSOU',
      });
    }

    const canal = await this.prisma.buChannel.create({
      data: {
        buId,
        type: 'NAO_OFICIAL',
        status: 'CONECTANDO',
        evolutionInstanceName: nomeInterno,
        requiresWindow: false,
      },
    });
    return { canal, qrcode: criada.qrcode };
  }

  /** QR para parear (ou reparear) — só existe no canal não oficial. */
  async qr(buId: string) {
    const canal = await this.prisma.buChannel.findUnique({
      where: { buId_type: { buId, type: 'NAO_OFICIAL' } },
    });
    if (!canal?.evolutionInstanceName) {
      throw new BadRequestException({ error: 'Esta BU não tem canal não oficial.', code: 'CANAL_AUSENTE' });
    }
    try {
      return { qrcode: await this.evolution.qrDaInstancia(canal.evolutionInstanceName) };
    } catch (e) {
      throw new BadRequestException({
        error: e instanceof EvolutionIndisponivelError ? e.message : 'A Evolution API recusou.',
        code: 'EVOLUTION_RECUSOU',
      });
    }
  }

  async desconectar(buId: string, tipo: TipoDeCanal) {
    const canal = await this.prisma.buChannel.findUnique({ where: { buId_type: { buId, type: tipo } } });
    if (!canal) return false;

    // Apagar na Evolution é best-effort: se ela estiver fora do ar, o vínculo
    // aqui sai do mesmo jeito. O contrário deixaria a BU presa a um canal que
    // ninguém consegue remover.
    if (tipo === 'NAO_OFICIAL' && canal.evolutionInstanceName && this.evolution.configurado()) {
      await this.evolution.apagarInstancia(canal.evolutionInstanceName).catch(() => undefined);
    }
    await this.prisma.buChannel.delete({ where: { id: canal.id } });
    return true;
  }

  private async exigirCanalLivre(buId: string, tipo: TipoDeCanal): Promise<void> {
    const existente = await this.prisma.buChannel.findUnique({ where: { buId_type: { buId, type: tipo } } });
    if (existente) {
      throw new ConflictException({ error: 'Esta BU já tem um canal desse tipo.', code: 'CANAL_JA_EXISTE' });
    }
  }
}

/**
 * Nome interno da instância na Evolution: só ASCII e hífen. Não aparece na tela
 * — quem aparece é o nome da BU.
 */
export function nomeDeInstancia(nomeDaBu: string, agora = Date.now()): string {
  const slug = nomeDaBu
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
  return `${slug || 'bu'}-${agora.toString(36)}`;
}


## FILE api-app/src/integrations/meta/meta.client.ts

import { Injectable } from '@nestjs/common';

export const META_CLIENT = Symbol('META_CLIENT');

export interface NumeroDaWaba {
  id: string;
  telefone: string;
  nomeVerificado: string | null;
}

/**
 * Porta do canal oficial. É adaptador de SAÍDA (ADR-0006, Emenda 1): nós
 * chamamos a Meta, ninguém chama aqui. Não existe controller neste diretório.
 */
export interface MetaClient {
  configurado(): boolean;
  /** Valida o WABA ID **e** captura o phone_number_id — a conta nasce pronta. */
  numerosDaWaba(wabaId: string): Promise<NumeroDaWaba[]>;
  /** Texto livre. Só vale dentro da janela de 24h — quem checa é o domínio. */
  enviarTexto(phoneNumberId: string, para: string, texto: string): Promise<string | null>;
}

export class MetaIndisponivelError extends Error {
  constructor(readonly detalhe: string) {
    super(detalhe);
  }
}

@Injectable()
export class MetaHttpClient implements MetaClient {
  private readonly token = process.env.WHATSAPP_TOKEN ?? '';
  private readonly versao = process.env.GRAPH_VERSION || 'v21.0';

  configurado(): boolean {
    return this.token.length > 0;
  }

  async numerosDaWaba(wabaId: string): Promise<NumeroDaWaba[]> {
    const url = `https://graph.facebook.com/${this.versao}/${wabaId}/phone_numbers?fields=id,display_phone_number,verified_name`;
    const res = await fetch(url, { headers: { authorization: `Bearer ${this.token}` } });
    const data = (await res.json().catch(() => ({}))) as {
      data?: { id: string; display_phone_number?: string; verified_name?: string }[];
      error?: Record<string, unknown>;
    };

    if (!res.ok) throw new MetaIndisponivelError(this.mensagemDeErro(data.error ?? {}));

    return (data.data ?? []).map((n) => ({
      id: n.id,
      telefone: (n.display_phone_number ?? '').replace(/\D/g, ''),
      nomeVerificado: n.verified_name ?? null,
    }));
  }

  async enviarTexto(phoneNumberId: string, para: string, texto: string): Promise<string | null> {
    const res = await fetch(`https://graph.facebook.com/${this.versao}/${phoneNumberId}/messages`, {
      method: 'POST',
      headers: { authorization: `Bearer ${this.token}`, 'content-type': 'application/json' },
      body: JSON.stringify({ messaging_product: 'whatsapp', to: para, type: 'text', text: { body: texto } }),
    });
    const data = (await res.json().catch(() => ({}))) as {
      messages?: { id?: string }[];
      error?: Record<string, unknown>;
    };
    if (!res.ok) throw new MetaIndisponivelError(this.mensagemDeErro(data.error ?? {}));
    return data.messages?.[0]?.id ?? null;
  }

  /** A Meta detalha o erro em campos variados; junta tudo que for legível. */
  private mensagemDeErro(err: Record<string, unknown>): string {
    const partes = [err.error_user_title, err.error_user_msg, err.message]
      .filter(Boolean)
      .map((p) => String(p));
    const codigo = [err.code, err.error_subcode].filter(Boolean).join('/');
    return (partes.join(' — ') || 'A Meta recusou a consulta.') + (codigo ? ` [código ${codigo}]` : '');
  }
}


## FILE api-app/src/integrations/evolution/evolution.client.ts

import { Injectable } from '@nestjs/common';

export const EVOLUTION_CLIENT = Symbol('EVOLUTION_CLIENT');

export interface InstanciaCriada {
  qrcode: string | null;
}

/**
 * Porta do canal não oficial. Adaptador de SAÍDA — a Evolution API é serviço
 * interno do projeto, **sem domínio público** (ADR-0002).
 */
export interface EvolutionClient {
  configurado(): boolean;
  criarInstancia(nome: string): Promise<InstanciaCriada>;
  qrDaInstancia(nome: string): Promise<string | null>;
  estadoDaInstancia(nome: string): Promise<string>;
  apagarInstancia(nome: string): Promise<void>;
  /** Não existe janela aqui — o limite é o risco de ban, não a plataforma. */
  enviarTexto(instancia: string, para: string, texto: string): Promise<string | null>;
}

export class EvolutionIndisponivelError extends Error {}

@Injectable()
export class EvolutionHttpClient implements EvolutionClient {
  private readonly base = process.env.EVOLUTION_API_URL ?? '';
  private readonly chave = process.env.EVOLUTION_API_KEY ?? '';
  private readonly webhook = process.env.EVOLUTION_WEBHOOK_URL ?? '';

  configurado(): boolean {
    return this.base.length > 0 && this.chave.length > 0;
  }

  async criarInstancia(nome: string): Promise<InstanciaCriada> {
    const corpo: Record<string, unknown> = {
      instanceName: nome,
      qrcode: true,
      integration: 'WHATSAPP-BAILEYS',
    };
    if (this.webhook) {
      corpo.webhook = {
        enabled: true,
        url: this.webhook,
        byEvents: false,
        base64: false,
        events: ['MESSAGES_UPSERT', 'CONNECTION_UPDATE'],
      };
    }
    const data = await this.chamar('POST', '/instance/create', corpo);
    const payload = data as { qrcode?: { base64?: string } | string; base64?: string };
    return {
      qrcode:
        (typeof payload.qrcode === 'string' ? payload.qrcode : payload.qrcode?.base64) ??
        payload.base64 ??
        null,
    };
  }

  async qrDaInstancia(nome: string): Promise<string | null> {
    const data = await this.chamar('GET', `/instance/connect/${nome}`);
    const payload = data as { qrcode?: { base64?: string } | string; base64?: string };
    return (typeof payload.qrcode === 'string' ? payload.qrcode : payload.qrcode?.base64) ?? payload.base64 ?? null;
  }

  async estadoDaInstancia(nome: string): Promise<string> {
    const data = await this.chamar('GET', `/instance/connectionState/${nome}`);
    return (data as { instance?: { state?: string } }).instance?.state ?? 'desconhecido';
  }

  async apagarInstancia(nome: string): Promise<void> {
    await this.chamar('DELETE', `/instance/delete/${nome}`);
  }

  async enviarTexto(instancia: string, para: string, texto: string): Promise<string | null> {
    const data = await this.chamar('POST', `/message/sendText/${instancia}`, { number: para, text: texto });
    return (data as { key?: { id?: string } }).key?.id ?? null;
  }

  private async chamar(metodo: string, caminho: string, corpo?: unknown): Promise<unknown> {
    const res = await fetch(`${this.base}${caminho}`, {
      method: metodo,
      headers: { apikey: this.chave, 'content-type': 'application/json' },
      body: corpo ? JSON.stringify(corpo) : undefined,
      signal: AbortSignal.timeout(20_000),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      const msg = (data as { message?: string }).message ?? `HTTP ${res.status}`;
      throw new EvolutionIndisponivelError(msg);
    }
    return data;
  }
}


## FILE api-app/src/surfaces/bff/channels.controller.ts

import { BadRequestException, Body, Controller, Delete, Get, HttpCode, Param, Post, Req } from '@nestjs/common';
import type { Request } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { ChannelsService, TipoDeCanal } from '../../domain/channels/channels.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ModulosService } from '../../domain/produto/modulos.service';
import { ChaveDoCatalogo } from '../../domain/historico/catalogo';
import { RegistroDeAtividade } from '../../domain/historico/registro.service';

const TIPOS: TipoDeCanal[] = ['OFICIAL', 'NAO_OFICIAL'];

/**
 * Conectar e remover número é **parte administrativa** — exige ADMIN na BU
 * (ADR-0008 §5). O papel é o único eixo de permissão desde o ADR-0018.
 */
@Controller('api/bff/business-units/:buId/channels')
export class ChannelsController {
  constructor(
    private readonly access: AccessService,
    private readonly channels: ChannelsService,
    private readonly prisma: PrismaService,
    private readonly modulos: ModulosService,
    private readonly registro: RegistroDeAtividade,
  ) {}

  @Get()
  async listar(@Param('buId') buId: string, @Req() req: Request) {
    // Ver os canais é leitura: basta estar no escopo.
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    const canais = await this.prisma.buChannel.findMany({
      where: { buId },
      select: { type: true, status: true, requiresWindow: true, wabaId: true, connectedAt: true },
    });
    return { canais };
  }

  @Post()
  @HttpCode(201)
  async conectar(
    @Param('buId') buId: string,
    @Body() body: { tipo?: string; wabaId?: string },
    @Req() req: Request,
  ) {
    const bu = await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ADMIN');
    const tipo = String(body?.tipo ?? '') as TipoDeCanal;
    if (!TIPOS.includes(tipo)) {
      throw new BadRequestException({ error: 'tipo deve ser OFICIAL ou NAO_OFICIAL.', code: 'PAYLOAD_INVALIDO' });
    }

    if (tipo === 'OFICIAL') {
      const r = await this.channels.conectarOficial(buId, String(body?.wabaId ?? '').trim());
      await this.auditar(req, buId, 'canal.conectado', { canal: 'oficial', nome: bu.name });
      return { tipo, telefone: r.telefone, nomeVerificado: r.nomeVerificado, status: r.canal.status };
    }

    // O canal não oficial é MÓDULO (ADR-0016): a instalação precisa ser capaz
    // dele e a Mantenedora precisa tê-lo contratado. O canal oficial acima não
    // passa por aqui de propósito — ele é o piso do produto (Emenda 2 §1).
    await this.modulos.exigir(req.usuario!.mantenedoraId, 'canalNaoOficial');

    const r = await this.channels.conectarNaoOficial(buId, bu.name);
    await this.auditar(req, buId, 'canal.conectado', { canal: 'não oficial', nome: bu.name });
    return { tipo, status: r.canal.status, qrcode: r.qrcode };
  }

  /** QR de pareamento — só o canal não oficial tem. */
  @Get('nao-oficial/qr')
  async qr(@Param('buId') buId: string, @Req() req: Request) {
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ADMIN');
    return this.channels.qr(buId);
  }

  @Delete(':tipo')
  @HttpCode(204)
  async desconectar(@Param('buId') buId: string, @Param('tipo') tipoParam: string, @Req() req: Request) {
    const bu = await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ADMIN');
    const tipo = tipoParam.toUpperCase().replace('-', '_') as TipoDeCanal;
    if (!TIPOS.includes(tipo)) {
      throw new BadRequestException({ error: 'tipo deve ser OFICIAL ou NAO_OFICIAL.', code: 'PAYLOAD_INVALIDO' });
    }
    await this.channels.desconectar(buId, tipo);
    await this.auditar(req, buId, 'canal.removido', { canal: tipo === 'OFICIAL' ? 'oficial' : 'não oficial', nome: bu.name });
  }

  private async auditar(
    req: Request,
    buId: string,
    chave: ChaveDoCatalogo,
    frase: Record<string, string>,
  ): Promise<void> {
    const u = req.usuario!;
    await this.registro.registrarSolto(u.mantenedoraId, chave, {
      id: u.id,
      nome: u.nome,
      email: u.email,
      ip: req.ip ?? null,
    }, { buId, entidadeId: buId, frase });
  }
}


## FILE api-app/src/surfaces/bff/session.middleware.ts

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


## FILE api-app/src/domain/tenancy/tenancy.service.ts

import { BadRequestException, ConflictException, Injectable, NotFoundException } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { PasswordService } from '../identity/password.service';
import { RegistroDeAtividade } from '../historico/registro.service';

/** O setor em que cai quem não escolher (ADR-0017 §1). */
export const SETOR_PADRAO = 'Geral';

export interface NovaMantenedora {
  nome: string;
  bu: { nome: string; telefone?: string };
  owner: { nome: string; email: string; senha: string };
}

/**
 * Criação de Mantenedora — a operação que o ADR-0008 §7 deixou sem dono ao
 * decidir que não existe `platform_user` nesta v1.
 *
 * Ela vive na superfície INTERNA (ADR-0006, Emenda 1): não é delegável ao
 * cliente, nem à tela nem a quem consome a API pública. Nenhum `app_user`
 * alcança esta rota.
 */
@Injectable()
export class TenancyService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly passwords: PasswordService,
    private readonly registro: RegistroDeAtividade,
  ) {}

  async criar(input: NovaMantenedora) {
    const email = input.owner.email.trim().toLowerCase();

    return this.prisma.$transaction(async (tx) => {
      const mantenedora = await tx.mantenedora.create({ data: { name: input.nome.trim() } });

      // Toda Mantenedora nasce com o setor `Geral` (ADR-0017 §1): `setor_id` é
      // obrigatório, e número sem setor é número que nenhum atendente enxerga.
      const geral = await tx.setor.create({
        data: { mantenedoraId: mantenedora.id, name: SETOR_PADRAO },
      });

      const bu = await tx.businessUnit.create({
        data: {
          mantenedoraId: mantenedora.id,
          setorId: geral.id,
          name: input.bu.nome.trim(),
          phone: input.bu.telefone?.replace(/\D/g, '') || null,
        },
      });

      const jaExiste = await tx.appUser.findUnique({
        where: { mantenedoraId_email: { mantenedoraId: mantenedora.id, email } },
      });
      if (jaExiste) throw new ConflictException('Já existe usuário com esse e-mail nesta Mantenedora.');

      const owner = await tx.appUser.create({
        data: {
          mantenedoraId: mantenedora.id,
          name: input.owner.nome.trim(),
          email,
          passwordHash: await this.passwords.gerarHash(input.owner.senha),
        },
      });

      // O grant do fundador nasce como EXPANSÃO da Mantenedora, não como grant
      // direto. É a correção que o ADR-0023 do gateway_unifast documentou e que
      // o código de lá ainda não tem: com grant direto, a replicação de
      // expansões não enxerga o fundador, e ele perde a administração da conta
      // que criou quando alguém cria uma BU nova.
      await tx.userBuRole.create({
        data: {
          userId: owner.id,
          buId: bu.id,
          role: 'OWNER',
          grantedViaTipo: 'MANTENEDORA',
          grantedViaId: mantenedora.id,
        },
      });

      // Nasce com onboarding PENDENTE: é o wizard que decide os módulos, e o
      // OWNER é o único usuário que existe até ele terminar (ADR-0016 §4).
      await tx.mantenedoraSettings.create({
        data: { mantenedoraId: mantenedora.id, onboardingConcluido: false },
      });

      await this.registro.registrar(
        tx,
        mantenedora.id,
        'mantenedora.criada',
        { id: owner.id, nome: owner.name, email: owner.email },
        { buId: bu.id, entidadeId: mantenedora.id, frase: { nome: mantenedora.name } },
      );

      return { mantenedora, bu, owner: { id: owner.id, email: owner.email } };
    });
  }

  /**
   * BU nova sob uma Mantenedora **herda as expansões dela, na mesma transação**
   * (ADR-0008 §4, regra 3).
   *
   * Sem isso, quem administra a conta perde acesso ao número que acabou de
   * conectar — e, pior, o papel calculado na Mantenedora cai para ATENDENTE, porque
   * ele passa a ter grant em "algumas, não todas". É exatamente o defeito que o
   * ADR-0023 documentou no gateway_unifast, e ele aparece na primeira vez que
   * alguém cria a segunda BU.
   */
  /**
   * Renomear ou inativar um número.
   *
   * Faltava: dava para criar e para mover de setor, e um nome errado só se
   * consertava no banco. `status` inativa — nunca apaga: a BU é dona das
   * conversas, e apagá-la levaria o histórico junto.
   */
  async atualizarBusinessUnit(
    mantenedoraId: string,
    buId: string,
    dados: { nome?: string; status?: 'ATIVO' | 'INATIVO' },
    ator: { id: string | null; nome: string; email?: string | null },
  ) {
    const antes = await this.prisma.businessUnit.findFirst({ where: { id: buId, mantenedoraId } });
    if (!antes) throw new NotFoundException({ error: 'Não encontrado.', code: 'NAO_ENCONTRADO' });

    const nome = dados.nome?.trim();
    if (dados.nome !== undefined && !nome) {
      throw new BadRequestException({ error: 'O nome não pode ficar vazio.', code: 'PAYLOAD_INVALIDO' });
    }

    return this.prisma.$transaction(async (tx) => {
      const bu = await tx.businessUnit.update({
        where: { id: buId },
        data: { ...(nome ? { name: nome } : {}), ...(dados.status ? { status: dados.status } : {}) },
      });

      const mudouNome = Boolean(nome && nome !== antes.name);
      await this.registro.registrar(tx, mantenedoraId, 'numero.editado', ator, {
        buId,
        entidadeId: buId,
        campo: mudouNome ? 'nome' : 'status',
        de: mudouNome ? antes.name : antes.status,
        para: mudouNome ? bu.name : bu.status,
        frase: {
          nome: bu.name,
          campo: mudouNome ? 'nome' : 'status',
          de: mudouNome ? antes.name : antes.status,
          para: mudouNome ? bu.name : bu.status,
        },
      });

      return { id: bu.id, nome: bu.name, status: bu.status };
    });
  }

  async criarBusinessUnit(
    mantenedoraId: string,
    nome: string,
    telefone?: string,
    setorId?: string,
    ator?: { id: string | null; nome: string; email?: string | null },
  ) {
    return this.prisma.$transaction(async (tx) => {
      // Sem setor escolhido, cai no `Geral` — criado aqui se ainda não existir,
      // para que uma Mantenedora anterior ao ADR-0017 não trave.
      const setor = setorId
        ? await tx.setor.findFirst({ where: { id: setorId, mantenedoraId } })
        : ((await tx.setor.findFirst({ where: { mantenedoraId, name: SETOR_PADRAO } })) ??
          (await tx.setor.create({ data: { mantenedoraId, name: SETOR_PADRAO } })));
      if (!setor) throw new NotFoundException({ error: 'Setor não encontrado.', code: 'NAO_ENCONTRADO' });

      const bu = await tx.businessUnit.create({
        data: {
          mantenedoraId,
          setorId: setor.id,
          name: nome.trim(),
          phone: telefone?.replace(/\D/g, '') || null,
        },
      });

      // A BU nova herda as expansões da MANTENEDORA e as do SETOR em que nasce
      // (ADR-0017 §2, regra 3). É o que faz "conectar um número novo no
      // Comercial" não deixar o time comercial de fora dele.
      //
      // A Mantenedora vem primeiro e o Setor só preenche o que sobrou: as duas
      // são expansão, e a regra 1 (uma linha por par usuário/BU) precisa de um
      // desempate estável.
      const daMantenedora = await tx.userBuRole.findMany({
        where: { grantedViaTipo: 'MANTENEDORA', grantedViaId: mantenedoraId },
        select: { userId: true, role: true },
        distinct: ['userId'],
      });
      // A CONCESSÃO do setor, não as linhas materializadas nele: é o que faz o
      // primeiro número de um setor recém-concedido já nascer com o acesso.
      const doSetor = await tx.setorGrant.findMany({
        where: { setorId: setor.id },
        select: { userId: true, role: true },
      });

      const jaTem = new Set(daMantenedora.map((e) => e.userId));
      const novas = [
        ...daMantenedora.map((e) => ({
          userId: e.userId,
          buId: bu.id,
          role: e.role,
          grantedViaTipo: 'MANTENEDORA' as const,
          grantedViaId: mantenedoraId,
        })),
        ...doSetor
          .filter((e) => !jaTem.has(e.userId))
          .map((e) => ({
            userId: e.userId,
            buId: bu.id,
            role: e.role,
            grantedViaTipo: 'SETOR' as const,
            grantedViaId: setor.id,
          })),
      ];

      if (novas.length) await tx.userBuRole.createMany({ data: novas });

      if (ator) {
        await this.registro.registrar(tx, mantenedoraId, 'numero.criado', ator, {
          buId: bu.id,
          entidadeId: bu.id,
          frase: { nome: bu.name },
        });
      }

      return { bu, setor, herdaram: novas.length };
    });
  }
}


## FILE api-app/src/domain/inbox/conversations.service.ts

import {
  BadRequestException,
  ConflictException,
  Inject,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { EVOLUTION_CLIENT, EvolutionClient } from '../../integrations/evolution/evolution.client';
import { META_CLIENT, MetaClient } from '../../integrations/meta/meta.client';
import { CanalDeOrigem } from './incoming.service';
import { criarCursorTimeline, lerCursorTimeline } from './timeline-pagination';

export const JANELA_MS = 24 * 60 * 60 * 1000;

export interface Atendente {
  userId: string;
  nome: string;
}

@Injectable()
export class ConversationsService {
  constructor(
    private readonly prisma: PrismaService,
    @Inject(META_CLIENT) private readonly meta: MetaClient,
    @Inject(EVOLUTION_CLIENT) private readonly evolution: EvolutionClient,
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

    const [total, conversas] = await Promise.all([
      this.prisma.conversation.count({ where }),
      this.prisma.conversation.findMany({
      where,
      orderBy: { lastMessageAt: 'desc' },
      skip: (pagina - 1) * limite,
      take: limite,
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
      }),
    ]);

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
  async estadoDaJanela(conversaId: string, buId: string, agora = Date.now()) {
    const ultima = await this.prisma.message.findFirst({
      where: { conversationId: conversaId },
      orderBy: { createdAt: 'desc' },
      select: { channelOrigin: true },
    });
    const canais = await this.prisma.buChannel.findMany({ where: { buId } });
    if (canais.length === 0) return { canal: null, exigeJanela: false, aberta: false, expiraEm: null };

    const tipo = (ultima?.channelOrigin ?? canais[0].type) as CanalDeOrigem;
    const canal = canais.find((c) => c.type === tipo) ?? canais[0];
    if (!canal.requiresWindow) {
      return { canal, exigeJanela: false, aberta: true, expiraEm: null as Date | null };
    }

    const ultimaEntrada = await this.prisma.message.findFirst({
      where: { conversationId: conversaId, direction: 'IN' },
      orderBy: { createdAt: 'desc' },
      select: { createdAt: true },
    });
    if (!ultimaEntrada) return { canal, exigeJanela: true, aberta: false, expiraEm: null };

    const expiraEm = new Date(ultimaEntrada.createdAt.getTime() + JANELA_MS);
    return { canal, exigeJanela: true, aberta: expiraEm.getTime() > agora, expiraEm };
  }

  async responder(conversaId: string, texto: string, atendente: Atendente) {
    const conversa = await this.prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
    const janela = await this.estadoDaJanela(conversaId, conversa.buId);

    if (!janela.canal) {
      throw new BadRequestException({ error: 'Esta BU não tem canal conectado.', code: 'CANAL_AUSENTE' });
    }
    if (janela.exigeJanela && !janela.aberta) {
      // A alternativa (disparar um template) NÃO existe na v1: modelos e disparo
      // seguem na Central de Modelos até a v2. A tela leva para lá por link em
      // vez de fingir que há botão (ADR-0009 §3).
      throw new ConflictException({
        error:
          'Fora da janela de 24h da Meta: só é possível responder texto livre até 24h após a última mensagem da pessoa.',
        code: 'JANELA_FECHADA',
      });
    }

    const externalId = await this.enviarPeloCanal(janela.canal, conversa.contact, texto);

    const mensagem = await this.prisma.message.create({
      data: {
        conversationId: conversa.id,
        buId: conversa.buId,
        direction: 'OUT',
        messageType: 'TEXTO',
        content: texto,
        channelOrigin: janela.canal.type,
        status: 'ENVIADA',
        externalId,
        authorUserId: atendente.userId,
        // Snapshot: a autoria sobrevive à exclusão do usuário (ADR-0007).
        authorName: atendente.nome,
      },
    });

    // Responder move para IN_SERVICE e auto-atribui — mas só se ninguém estiver
    // atendendo: responder NÃO rouba conversa de outro (ADR-0009 §2).
    const semDono = !conversa.attendantUserId && !conversa.attendantName;
    await this.prisma.conversation.update({
      where: { id: conversa.id },
      data: {
        lastMessageAt: new Date(),
        status: conversa.contactType === 'GRUPO' ? undefined : 'IN_SERVICE',
        attendantUserId: semDono ? atendente.userId : undefined,
        attendantName: semDono ? atendente.nome : undefined,
        attendantOrigin: semDono ? 'INTERNO' : undefined,
      },
    });

    return mensagem;
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

  private async enviarPeloCanal(
    canal: { type: string; phoneNumberId: string | null; evolutionInstanceName: string | null },
    contato: string,
    texto: string,
  ): Promise<string | null> {
    try {
      if (canal.type === 'OFICIAL') {
        if (!canal.phoneNumberId) {
          throw new BadRequestException({ error: 'Canal sem número de envio.', code: 'CANAL_SEM_NUMERO' });
        }
        return await this.meta.enviarTexto(canal.phoneNumberId, contato, texto);
      }
      if (!canal.evolutionInstanceName) {
        throw new BadRequestException({ error: 'Canal sem instância.', code: 'CANAL_SEM_INSTANCIA' });
      }
      return await this.evolution.enviarTexto(canal.evolutionInstanceName, contato, texto);
    } catch (e) {
      if (e instanceof BadRequestException || e instanceof ConflictException) throw e;
      // Os dois códigos ficam DISTINTOS de propósito: quem trata o erro quer
      // saber qual plataforma recusou, porque o contorno é diferente (ADR-0010).
      throw new BadRequestException({
        error: e instanceof Error ? e.message : 'O canal recusou o envio.',
        code: canal.type === 'OFICIAL' ? 'META_RECUSOU' : 'EVOLUTION_RECUSOU',
      });
    }
  }
}


## FILE api-app/src/domain/inbox/incoming.service.ts

import { Inject, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { RealtimeService } from '../../realtime/realtime.service';
import { META_CLIENT, MetaClient } from '../../integrations/meta/meta.client';
import { TYPEBOT_CLIENT, TypebotClient } from '../../integrations/typebot/typebot.client';

export type CanalDeOrigem = 'OFICIAL' | 'NAO_OFICIAL';

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
  externalId?: string | null;
  /** Quem respondeu, quando a mensagem saiu por fora do produto. */
  autorNome?: string | null;
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
    @Inject(META_CLIENT) private readonly meta: MetaClient,
    @Inject(TYPEBOT_CLIENT) private readonly typebot: TypebotClient,
  ) {}

  async registrar(m: MensagemRecebida) {
    const existente = await this.prisma.conversation.findUnique({
      where: { buId_contact: { buId: m.buId, contact: m.contato } },
    });

    // Mensagem nova do contato REABRE a conversa fechada e solta a atribuição:
    // ela volta "ao balcão", não necessariamente para quem atendeu antes. Uma
    // conversa em atendimento NÃO é rebaixada por mensagem nova (ADR-0009 §2).
    const reabrindo = existente?.status === 'CLOSED' && m.direcao === 'IN' && !m.ehGrupo;

    const conversa = await this.prisma.conversation.upsert({
      where: { buId_contact: { buId: m.buId, contact: m.contato } },
      create: {
        buId: m.buId,
        contact: m.contato,
        contactType: m.ehGrupo ? 'GRUPO' : 'PESSOA',
        displayName: m.nomeExibicao ?? null,
        status: m.direcao === 'IN' ? 'QUEUED' : 'IN_SERVICE',
        unreadCount: m.direcao === 'IN' ? 1 : 0,
        lastMessageAt: new Date(),
      },
      update: {
        displayName: m.nomeExibicao ?? undefined,
        lastMessageAt: new Date(),
        unreadCount: m.direcao === 'IN' ? { increment: 1 } : undefined,
        status: reabrindo ? 'QUEUED' : undefined,
        attendantUserId: reabrindo ? null : undefined,
        attendantName: reabrindo ? null : undefined,
        attendantOrigin: reabrindo ? null : undefined,
      },
    });

    const mensagem = await this.prisma.message.create({
      data: {
        conversationId: conversa.id,
        // Denormalizado do conversation para que TODA tabela de dado de negócio
        // tenha bu_id — é o que a regra 0 exige para poder filtrar sempre.
        buId: m.buId,
        direction: m.direcao,
        messageType: m.tipo,
        content: m.conteudo ?? null,
        channelOrigin: m.canal,
        status: m.direcao === 'IN' ? 'RECEBIDA' : 'ENVIADA',
        externalId: m.externalId ?? null,
        authorName: m.autorNome ?? null,
      },
    });

    // Só quem tem grant nesta BU recebe. O push respeita o mesmo escopo do REST.
    this.realtime.publicarNaBu(m.buId, {
      tipo: 'mensagem',
      conversaId: conversa.id,
      contato: conversa.contact,
      direcao: m.direcao,
      canal: m.canal,
      naoLidas: conversa.unreadCount,
    });

    if (m.canal === 'OFICIAL' && m.direcao === 'IN' && m.tipo === 'TEXTO' && m.conteudo?.trim()) {
      await this.executarTypebot(m.buId, m.contato, m.conteudo.trim(), !existente).catch(() => undefined);
    }

    return { conversa, mensagem, reabriu: reabrindo };
  }

  private async executarTypebot(buId: string, contato: string, texto: string, novaConversa: boolean): Promise<void> {
    const gatilhos = await this.prisma.typebotTrigger.findMany({
      where: { active: true, bot: { status: 'ATIVO' }, OR: [{ buId: null }, { buId }] },
      include: { bot: true }, orderBy: { createdAt: 'asc' },
    });
    const normalized = texto.toLocaleLowerCase('pt-BR');
    const gatilho = gatilhos.find((g) => gatilhoCombina(g.kind, g.value, normalized, novaConversa));
    if (!gatilho || !this.typebot.configurado()) return;
    const canal = await this.prisma.buChannel.findFirst({ where: { buId, type: 'OFICIAL', status: 'CONECTADO' }, select: { phoneNumberId: true } });
    if (!canal?.phoneNumberId) return;
    const botId = gatilho.bot.publishedTypebotId;
    if (!botId) return;
    const atual = await this.prisma.typebotSession.findUnique({ where: { botId_buId_contato: { botId: gatilho.botId, buId, contato } } });
    const resposta = atual?.ativo ? await this.typebot.continuar(atual.sessionId, texto) : await this.typebot.iniciar(botId, contato, texto);
    const sessionId = 'sessionId' in resposta && typeof resposta.sessionId === 'string' ? resposta.sessionId : null;
    if (!atual && sessionId) await this.prisma.typebotSession.create({ data: { botId: gatilho.botId, mantenedoraId: gatilho.bot.mantenedoraId, buId, contato, sessionId } });
    for (const mensagem of resposta.messages) {
      const saida = textoDaRespostaTypebot(mensagem);
      if (!saida) continue;
      const externalId = await this.meta.enviarTexto(canal.phoneNumberId, contato, saida);
      await this.registrar({ buId, canal: 'OFICIAL', contato, ehGrupo: false, direcao: 'OUT', tipo: 'TEXTO', conteudo: saida, externalId, autorNome: 'Typebot' });
    }
  }

  /** Registra o evento cru. É o ÚNICO lugar com payload bruto (ADR-0009 §7). */
  async registrarEventoCru(canal: CanalDeOrigem, tipo: string, payload: unknown, buId?: string | null) {
    await this.prisma.webhookEvent.create({
      data: { channel: canal, eventType: tipo, payload: payload as object, buId: buId ?? null },
    });
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


## FILE api-app/src/infra/config/modulos.ts

/**
 * Módulos do produto (ADR-0016 e suas duas emendas).
 *
 * Dois níveis, e o efetivo é a interseção:
 *
 *   env  →  o que a INSTALAÇÃO é capaz de fazer   (teto, lido uma vez no boot)
 *    ∩
 *   banco →  o que a MANTENEDORA contratou        (escolhido no wizard)
 *
 * O **canal oficial não está aqui**: ele é o piso do produto, não um módulo
 * (Emenda 2). Não se escolhe, não se desliga, e sem ele o processo não sobe.
 */

/** As chaves do registro. Uma por módulo que EXISTE — ver o aviso abaixo. */
export type Modulo = 'canalNaoOficial';

export interface ModulosDaInstalacao {
  canalNaoOficial: boolean;
}

export interface DescricaoDeModulo {
  chave: Modulo;
  env: string;
  rotulo: string;
}

/**
 * O registro de módulos da v1.1 — **um item**.
 *
 * CRM está fora desta versão, disparo é v2, e o histórico deixou de ser módulo
 * (ADR-0016, Emenda 2 §2). Nenhum dos três aparece aqui, e isso é regra, não
 * esquecimento: **flag que nunca pode ser verdadeira é código que mente sobre o
 * que o produto faz** — quem lesse o `.env.example` concluiria que basta ligar.
 *
 * Módulo entra no registro na mesma mudança em que ganha código.
 */
export const REGISTRO_DE_MODULOS: readonly DescricaoDeModulo[] = [
  { chave: 'canalNaoOficial', env: 'LH_CHANNEL_UNOFFICIAL', rotulo: 'WhatsApp não oficial' },
];

export class ConfiguracaoIncoerente extends Error {}

function ligada(valor: string | undefined): boolean {
  return ['1', 'true', 'sim', 'yes'].includes(String(valor ?? '').trim().toLowerCase());
}

/** O teto da instalação, lido do ambiente. */
export function lerModulos(env: NodeJS.ProcessEnv = process.env): ModulosDaInstalacao {
  return { canalNaoOficial: ligada(env['LH_CHANNEL_UNOFFICIAL']) };
}

/**
 * O piso e a coerência do teto, verificados **no boot** (ADR-0016 §2 + Emenda 2).
 *
 * Configuração incoerente é defeito de implantação — e defeito de implantação
 * precisa aparecer na hora de implantar, não como 503 no meio de um atendimento.
 */
export function verificarConfiguracao(env: NodeJS.ProcessEnv = process.env): void {
  const faltando: string[] = [];

  // O piso: o canal oficial É o produto (Emenda 2 §1).
  if (!String(env['WHATSAPP_TOKEN'] ?? '').trim()) {
    faltando.push('WHATSAPP_TOKEN — o canal oficial é o piso do produto, e sem ele não há LeadsHug');
  }

  // Ligar um módulo na env não dispensa a credencial dele.
  if (ligada(env['LH_CHANNEL_UNOFFICIAL'])) {
    if (!String(env['EVOLUTION_API_URL'] ?? '').trim()) {
      faltando.push('EVOLUTION_API_URL — exigida por LH_CHANNEL_UNOFFICIAL=true');
    }
    if (!String(env['EVOLUTION_API_KEY'] ?? '').trim()) {
      faltando.push('EVOLUTION_API_KEY — exigida por LH_CHANNEL_UNOFFICIAL=true');
    }
  }

  if (faltando.length) {
    throw new ConfiguracaoIncoerente(
      `A instalação está incoerente e o processo não sobe:\n  - ${faltando.join('\n  - ')}`,
    );
  }
}

/** A interseção — o que a Mantenedora de fato enxerga. */
export function efetivos(teto: ModulosDaInstalacao, contratados: Partial<ModulosDaInstalacao>): ModulosDaInstalacao {
  return { canalNaoOficial: teto.canalNaoOficial && contratados.canalNaoOficial === true };
}

/** Ignora chave desconhecida na leitura; a ESCRITA é que recusa (ADR-0016 §4). */
export function lerContratados(valor: unknown): Partial<ModulosDaInstalacao> {
  if (!valor || typeof valor !== 'object') return {};
  const bruto = valor as Record<string, unknown>;
  const saida: Partial<ModulosDaInstalacao> = {};
  for (const m of REGISTRO_DE_MODULOS) {
    if (typeof bruto[m.chave] === 'boolean') saida[m.chave] = bruto[m.chave] as boolean;
  }
  return saida;
}


## FILE api-app/src/surfaces/webhooks/meta.controller.ts

import { Controller, ForbiddenException, Get, HttpCode, Post, Query, Req } from '@nestjs/common';
import type { RawBodyRequest } from '@nestjs/common';
import type { Request } from 'express';
import { createHmac, timingSafeEqual } from 'node:crypto';
import { IncomingService, MensagemRecebida } from '../../domain/inbox/incoming.service';
import { PrismaService } from '../../infra/prisma/prisma.service';

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
    await this.incoming.registrarEventoCru('OFICIAL', 'meta.webhook', body);

    for (const entry of body?.entry ?? []) {
      for (const change of entry.changes ?? []) {
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

    // A BU sai do NÚMERO que recebeu, não de nada que o payload afirme sobre
    // dono. Número desconhecido é ignorado em silêncio — o evento cru fica
    // gravado para diagnóstico.
    const canal = await this.prisma.buChannel.findFirst({
      where: { type: 'OFICIAL', phoneNumberId },
      select: { buId: true },
    });
    if (!canal) return;

    const nome = value.contacts?.[0]?.profile?.name ?? null;

    for (const msg of value.messages ?? []) {
      await this.incoming.registrar({
        buId: canal.buId,
        canal: 'OFICIAL',
        contato: (msg.from ?? '').replace(/\D/g, ''),
        ehGrupo: false,
        nomeExibicao: nome,
        direcao: 'IN',
        tipo: tipoDaMensagem(msg.type),
        conteudo: conteudoDaMensagem(msg),
        externalId: msg.id ?? null,
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
  type?: string;
  text?: { body?: string };
  button?: { text?: string };
  interactive?: { button_reply?: { title?: string }; list_reply?: { title?: string } };
}


## FILE api-app/src/surfaces/webhooks/evolution.controller.ts

import { Body, Controller, ForbiddenException, HttpCode, Param, Post } from '@nestjs/common';
import { timingSafeEqual } from 'node:crypto';
import { IncomingService } from '../../domain/inbox/incoming.service';
import { PrismaService } from '../../infra/prisma/prisma.service';

/**
 * Webhook do canal não oficial. Autenticação POR ORIGEM (ADR-0006) — e aqui ela
 * é diferente da Meta por um motivo que não é escolha nossa: **a Evolution API
 * não assina nada**. O que resta é segredo no caminho, comparado em tempo
 * constante, com a URL tratada como credencial.
 */
@Controller('webhooks/evolution')
export class EvolutionWebhookController {
  constructor(
    private readonly incoming: IncomingService,
    private readonly prisma: PrismaService,
  ) {}

  @Post(':segredo')
  @HttpCode(200)
  async receber(@Param('segredo') segredo: string, @Body() body: EvolutionEvent) {
    this.exigirSegredo(segredo);

    const evento = body?.event;
    const instancia = body?.instance;
    if (!evento || !instancia) return { received: true };

    const canal = await this.prisma.buChannel.findFirst({
      where: { type: 'NAO_OFICIAL', evolutionInstanceName: instancia },
      select: { buId: true, id: true },
    });

    await this.incoming.registrarEventoCru('NAO_OFICIAL', evento, body, canal?.buId ?? null);
    if (!canal) return { received: true };

    // Os nomes de evento vêm em minúsculo com ponto no payload ENTREGUE, e em
    // maiúsculo com underscore quando são REGISTRADOS. São strings diferentes
    // para a mesma coisa — o parser do Hub já comparou contra o formato errado
    // uma vez (hub-whatsapp/docs/evolution-api-payloads.md).
    switch (evento) {
      case 'messages.upsert':
        await this.tratarMensagem(canal.buId, body.data as UpsertData);
        break;
      case 'connection.update':
        await this.tratarConexao(canal.id, body.data as ConnectionData);
        break;
      default:
        break;
    }
    return { received: true };
  }

  private exigirSegredo(recebido: string): void {
    const esperado = process.env.EVOLUTION_WEBHOOK_SECRET ?? '';
    if (!esperado) throw new ForbiddenException({ error: 'Webhook não configurado.', code: 'ORIGEM_NAO_VERIFICAVEL' });
    const a = Buffer.from(esperado);
    const b = Buffer.from(recebido ?? '');
    if (a.length !== b.length || !timingSafeEqual(a, b)) {
      throw new ForbiddenException({ error: 'Origem não reconhecida.', code: 'ORIGEM_INVALIDA' });
    }
  }

  private async tratarMensagem(buId: string, data: UpsertData | undefined): Promise<void> {
    const jid = data?.key?.remoteJid;
    if (!jid) return;

    const ehGrupo = jid.endsWith('@g.us');
    const daGente = Boolean(data?.key?.fromMe);
    const texto = data?.message?.conversation ?? data?.message?.extendedTextMessage?.text ?? '';

    // `pushName` é o nome de QUEM MANDOU aquela mensagem, não o nome do contato
    // da conversa. Numa mensagem nossa ele é o nome do próprio número — usá-lo
    // aqui é o bug que troca o nome do contato pelo do responsável (corrigido
    // no Hub em 756bd91, e não repetido aqui).
    const nome = !ehGrupo && !daGente ? (data?.pushName ?? null) : null;

    await this.incoming.registrar({
      buId,
      canal: 'NAO_OFICIAL',
      // O JID é detalhe de transporte e não entra no domínio (ADR-0009 §1).
      contato: ehGrupo ? jid : jid.split('@')[0],
      ehGrupo,
      nomeExibicao: nome,
      direcao: daGente ? 'OUT' : 'IN',
      tipo: 'TEXTO',
      conteudo: texto,
      externalId: data?.key?.id ?? null,
    });
  }

  private async tratarConexao(canalId: string, data: ConnectionData | undefined): Promise<void> {
    const estado = data?.state;
    // O número vem em `wuid`, no formato JID — não existe campo `number`.
    const telefone = data?.wuid?.split('@')[0];

    const status = estado === 'open' ? 'CONECTADO' : estado === 'connecting' ? 'CONECTANDO' : 'DESCONECTADO';

    await this.prisma.buChannel.update({
      where: { id: canalId },
      data: { status, connectedAt: status === 'CONECTADO' ? new Date() : undefined },
    });

    if (telefone) {
      const canal = await this.prisma.buChannel.findUniqueOrThrow({ where: { id: canalId } });
      await this.prisma.businessUnit.update({ where: { id: canal.buId }, data: { phone: telefone } });
    }
  }
}

interface EvolutionEvent {
  event?: string;
  instance?: string;
  data?: unknown;
}
interface UpsertData {
  key?: { remoteJid?: string; fromMe?: boolean; id?: string };
  pushName?: string;
  message?: { conversation?: string; extendedTextMessage?: { text?: string } };
}
interface ConnectionData {
  state?: string;
  wuid?: string;
}


## FILE api-app/prisma/schema.prisma

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

  @@unique([buId, type])
  @@map("bu_channels")
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
  setorGrants SetorGrant[]
  tokens      TokenDeAcesso[]

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

  @@unique([buId, contact])
  @@index([buId, status, lastMessageAt])
  @@map("conversations")
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
  /// Autoria: FK opcional SetNull + snapshot (ADR-0007). O payload cru NÃO
  /// mora aqui — só no log de webhook, com expurgo (ADR-0009 §7).
  authorUserId String?  @map("author_user_id")
  authorName   String?  @map("author_name")
  createdAt    DateTime @default(now()) @map("created_at")

  @@index([conversationId, createdAt])
  @@index([buId, createdAt])
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


## FILE web-app/src/telas/Numeros.tsx

import { FormEvent, useEffect, useState } from 'react';
import { BusinessUnit, ErroDaApi, Eu, api, ignorarSessaoMorta } from '../api';

/** A BU é o número (ADR-0008), e o canal é vínculo dela. A tela diz isso. */
export default function Numeros({ eu }: { eu: Eu }) {
  const [bus, setBus] = useState<BusinessUnit[]>([]);
  const [erro, setErro] = useState<string | null>(null);
  const [qr, setQr] = useState<{ buId: string; imagem: string } | null>(null);
  const [nomeNovo, setNomeNovo] = useState('');
  const admin = eu.papel === 'ADMIN' || eu.papel === 'OWNER';

  const carregar = () =>
    api.get<{ businessUnits: BusinessUnit[] }>('/business-units').then((r) => setBus(r.businessUnits));

  useEffect(() => {
    carregar().catch(ignorarSessaoMorta);
    const timer = window.setInterval(() => carregar().catch(ignorarSessaoMorta), 5000);
    return () => window.clearInterval(timer);
  }, []);

  async function tentar(acao: () => Promise<unknown>) {
    setErro(null);
    try {
      await acao();
      await carregar();
    } catch (e) {
      setErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
    }
  }

  async function criarBu(e: FormEvent) {
    e.preventDefault();
    await tentar(async () => {
      await api.post('/business-units', { nome: nomeNovo });
      setNomeNovo('');
    });
  }

  async function conectarOficial(buId: string) {
    const wabaId = prompt('WABA ID (só números):')?.trim();
    if (!wabaId) return;
    await tentar(() => api.post(`/business-units/${buId}/channels`, { tipo: 'OFICIAL', wabaId }));
  }

  async function conectarNaoOficial(buId: string) {
    await tentar(async () => {
      const r = await api.post<{ qrcode: string | null }>(`/business-units/${buId}/channels`, {
        tipo: 'NAO_OFICIAL',
      });
      if (r.qrcode) setQr({ buId, imagem: r.qrcode });
    });
  }

  async function novoQr(buId: string) {
    await tentar(async () => {
      const r = await api.get<{ qrcode: string | null }>(`/business-units/${buId}/channels/nao-oficial/qr`);
      if (r.qrcode) setQr({ buId, imagem: r.qrcode });
    });
  }

  async function desconectar(buId: string) {
    await tentar(() => api.del(`/business-units/${buId}/channels/nao-oficial`));
    setQr((atual) => (atual?.buId === buId ? null : atual));
  }

  return (
    <div className="grade">
      <h2 style={{ margin: 0 }}>Números</h2>
      {erro && <p className="erro">{erro}</p>}

      {admin && (
        <form className="cartao linha" onSubmit={criarBu}>
          <input
            placeholder="Nome do número novo (ex.: Financeiro)"
            value={nomeNovo}
            onChange={(e) => setNomeNovo(e.target.value)}
            required
          />
          <button className="primario">Adicionar</button>
        </form>
      )}

      {bus.map((bu) => {
        const oficial = bu.channels.find((c) => c.type === 'OFICIAL');
        const naoOficial = bu.channels.find((c) => c.type === 'NAO_OFICIAL');
        return (
          <div key={bu.id} className="cartao grade">
            <div className="linha">
              <strong>{bu.name}</strong>
              <span className="suave">{bu.phone ?? 'sem número ainda'}</span>
            </div>
            <div className="linha">
              <span className="suave">Oficial:</span>
              {oficial ? (
                <span>{oficial.status}</span>
              ) : admin ? (
                <button onClick={() => conectarOficial(bu.id)}>Conectar WABA</button>
              ) : (
                <span className="suave">não conectado</span>
              )}
            </div>
            <div className="linha">
              <span className="suave">Não oficial:</span>
              {naoOficial ? (
                <>
                  <span>{naoOficial.status}</span>
                  {admin && <button onClick={() => novoQr(bu.id)}>Ver QR</button>}
                  {admin && <button onClick={() => void desconectar(bu.id)}>Desconectar</button>}
                </>
              ) : admin ? (
                <button onClick={() => conectarNaoOficial(bu.id)}>Parear número</button>
              ) : (
                <span className="suave">não conectado</span>
              )}
            </div>
            {qr?.buId === bu.id && (
              <div className="grade">
                <span className="suave">Leia o QR no celular, em Aparelhos conectados.</span>
                <img src={qr.imagem} alt="QR de pareamento" style={{ width: 240 }} />
              </div>
            )}
          </div>
        );
      })}
      {bus.length === 0 && <p className="suave">Nenhum número no seu escopo.</p>}
    </div>
  );
}


## FILE web-app/src/config.ts

/**
 * Configuração de EXECUÇÃO, não de build.
 *
 * `import.meta.env.VITE_*` é substituído textualmente pelo Vite no momento do
 * build — o que tornaria a imagem do `web` específica do ambiente: promover
 * stage para produção exigiria rebuild, não redeploy. Em vez disso, o container
 * escreve `/config.js` no start, a partir do ambiente, e o `index.html` o carrega
 * antes do bundle.
 *
 * É o mesmo princípio do backend, onde a env é lida quando o processo sobe: uma
 * imagem, muitos ambientes.
 */
declare global {
  interface Window {
    __LEADSHUG__?: { apiUrl?: string };
  }
}

/**
 * Base da API. Vazio = mesma origem — que é o caso do desenvolvimento, onde o
 * proxy do Vite responde por `/api`, e o do container servido no mesmo host.
 *
 * Barra sobrando é tolerada: `https://api.x.com/` e `https://api.x.com` valem o
 * mesmo, e a diferença geraria `//api/bff` — que alguns servidores tratam como
 * outro caminho.
 */
function lerBase(): string {
  // `typeof window` porque o teste de unidade roda em Node, sem DOM. Fora do
  // navegador não há /config.js, e "mesma origem" é a resposta certa.
  const bruto = (typeof window === 'undefined' ? '' : (window.__LEADSHUG__?.apiUrl ?? '')).trim();
  if (!bruto) return '';

  // Sem esquema, o navegador trataria isto como CAMINHO relativo e toda chamada
  // voltaria para o próprio front — com 405 no login e nada apontando para a
  // causa. O container já recusa subir assim; esta é a segunda rede, para o caso
  // de o arquivo ter sido escrito por outro caminho.
  if (!/^https?:\/\//i.test(bruto)) {
    throw new Error(
      `LEADSHUG_API_URL="${bruto}" está sem esquema. Use https://${bruto} — sem ele, ` +
        'o navegador trata o valor como caminho e toda chamada volta para o próprio front.',
    );
  }
  return bruto.replace(/\/+$/, '');
}

export const API_BASE: string = lerBase();


## FILE web-app/nginx/default.conf.template

# Processado pelo entrypoint da imagem oficial do nginx, que roda envsubst nos
# arquivos de /etc/nginx/templates. É assim que a porta deixa de ser fixa: a
# Railway injeta PORT, e um servidor que escuta noutra porta responde 502 —
# domínio existe, serviço não atende.
server {
    listen ${PORT};
    server_name _;
    root /usr/share/nginx/html;

    # Assets com hash no nome podem ser cacheados para sempre.
    location /assets/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Caminho de API NÃO cai no index.html.
    #
    # Sem isto, um front mal configurado (base vazia) recebe 200 com HTML em toda
    # chamada — e o sintoma vira "a tela quebrou" num campo qualquer, longe da
    # causa. 404 aqui é ruidoso e honesto: este serviço não é a API.
    location /api/ { return 404; }
    location /health { return 404; }
    location /ws { return 404; }

    # O index.html NUNCA é cacheado: é ele que aponta para os assets novos a
    # cada deploy. Errar isso significa gente vendo a versão velha sem suspeitar
    # do cache.
    location / {
        add_header Cache-Control "no-store";
        try_files $uri $uri/ /index.html;
    }
}


## FILE docker-compose.yml

services:
  postgres:
    image: postgres:16
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-leadshug}
      POSTGRES_USER: ${POSTGRES_USER:-leadshug}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-leadshug}
    ports:
      - "${POSTGRES_HOST_PORT:-55433}:5432"
    volumes:
      - leadshug_pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
      interval: 5s
      timeout: 5s
      retries: 10

  api:
    build:
      context: ./api-app
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      DATABASE_URL: postgresql://${POSTGRES_USER:-leadshug}:${POSTGRES_PASSWORD:-leadshug}@postgres:5432/${POSTGRES_DB:-leadshug}?schema=public
      PORT: "3000"
      WEB_ORIGIN: ${WEB_ORIGIN:-http://localhost:8080}
      SESSION_SECRET: ${SESSION_SECRET:?Set SESSION_SECRET in .env}
      INTERNAL_SERVICE_TOKEN: ${INTERNAL_SERVICE_TOKEN:?Set INTERNAL_SERVICE_TOKEN in .env}
      WHATSAPP_TOKEN: ${WHATSAPP_TOKEN:?Set WHATSAPP_TOKEN in .env}
      LH_ARQUIVOS_DIR: /dados/arquivos
    volumes:
      - leadshug_arquivos:/dados/arquivos
    ports:
      - "${API_HOST_PORT:-3000}:3000"
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1:3000/health >/dev/null 2>&1"]
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 20s
    restart: unless-stopped

  web:
    build:
      context: ./web-app
    depends_on:
      api:
        condition: service_healthy
    environment:
      PORT: "80"
      LEADSHUG_API_URL: ${LEADSHUG_API_URL:-http://localhost:3000}
    ports:
      - "${WEB_HOST_PORT:-8080}:80"
    restart: unless-stopped

volumes:
  leadshug_pg_data:
  leadshug_arquivos:


## FILE Makefile

SHELL := /bin/bash

.PHONY: up down ps logs test-api test-web migrate

up:
	docker compose up -d --build

down:
	docker compose down

ps:
	docker compose ps

logs:
	docker compose logs -f --tail=200

test-api:
	cd api-app && npm ci && npm run lint && npm run build && npm test

test-web:
	cd web-app && npm ci && npm run build && npm test

migrate:
	docker compose exec api npx prisma migrate deploy


## FILE api-app/test/helpers.ts

import { INestApplication } from '@nestjs/common';
import { Test } from '@nestjs/testing';
import type { NestExpressApplication } from '@nestjs/platform-express';
import request from 'supertest';
import { AppModule } from '../src/app.module';
import { configurarBodyParsers } from '../src/infra/http/body-parsers';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { EVOLUTION_CLIENT, EvolutionClient } from '../src/integrations/evolution/evolution.client';
import { META_CLIENT, MetaClient } from '../src/integrations/meta/meta.client';

/** Dublês das portas de saída: o teste prova permissão, não a Meta. */
export const metaFake: MetaClient & { wabaRecusada: string | null; enviados: { para: string; texto: string }[] } = {
  wabaRecusada: null,
  enviados: [],
  async enviarTexto(_phoneNumberId: string, para: string, texto: string) {
    metaFake.enviados.push({ para, texto });
    return `wamid-enviado-${metaFake.enviados.length}`;
  },
  configurado: () => true,
  async numerosDaWaba(wabaId: string) {
    if (metaFake.wabaRecusada === wabaId) throw new Error('WABA recusada');
    return [{ id: `phone-${wabaId}`, telefone: '5584999990000', nomeVerificado: 'Teste' }];
  },
};

export const evolutionFake: EvolutionClient & { enviados: { para: string; texto: string }[] } = {
  enviados: [],
  configurado: () => true,
  async enviarTexto(_instancia: string, para: string, texto: string) {
    evolutionFake.enviados.push({ para, texto });
    return `evo-enviado-${evolutionFake.enviados.length}`;
  },
  async criarInstancia() {
    return { qrcode: 'data:image/png;base64,QR' };
  },
  async qrDaInstancia() {
    return 'data:image/png;base64,QR';
  },
  async estadoDaInstancia() {
    return 'open';
  },
  async apagarInstancia() {},
};

/**
 * Liga o canal não oficial nos DOIS níveis: o teto da instalação (env, lido no
 * boot do serviço) e o contrato da Mantenedora (banco) — ADR-0016.
 *
 * Precisa vir ANTES de `subirApp`, porque o teto é lido uma vez na construção.
 * É o mesmo que acontece em produção: mudar módulo de instalação é deploy.
 */
export function tetoComCanalNaoOficial(): void {
  process.env.LH_CHANNEL_UNOFFICIAL = 'true';
}

export async function contratarCanalNaoOficial(prisma: PrismaService, mantenedoraId: string): Promise<void> {
  await prisma.mantenedoraSettings.upsert({
    where: { mantenedoraId },
    create: { mantenedoraId, modulos: { canalNaoOficial: true } },
    update: { modulos: { canalNaoOficial: true } },
  });
}

export const TOKEN_INTERNO = 'token-interno-de-teste';
export const META_APP_SECRET = 'segredo-do-app-meta';
export const EVOLUTION_WEBHOOK_SECRET = 'segredo-do-caminho-evolution';

export async function subirApp(): Promise<{ app: INestApplication; prisma: PrismaService }> {
  process.env.SESSION_SECRET ||= 'segredo-de-teste';
  process.env.INTERNAL_SERVICE_TOKEN = TOKEN_INTERNO;
  process.env.META_APP_SECRET = META_APP_SECRET;
  process.env.EVOLUTION_WEBHOOK_SECRET = EVOLUTION_WEBHOOK_SECRET;
  process.env.WEBHOOK_VERIFY_TOKEN = 'verify-token-de-teste';

  const moduleRef = await Test.createTestingModule({ imports: [AppModule] })
    .overrideProvider(META_CLIENT)
    .useValue(metaFake)
    .overrideProvider(EVOLUTION_CLIENT)
    .useValue(evolutionFake)
    .compile();
  // A MESMA fiação de produção: sem isto o corpo bruto não existe e o teste de
  // assinatura passaria a provar outra coisa.
  const app = moduleRef.createNestApplication({ bodyParser: false });
  configurarBodyParsers(app as unknown as NestExpressApplication);
  await app.init();
  return { app, prisma: app.get(PrismaService) };
}

/** Limpa na ordem das dependências — o banco de teste é real (ADR-0012 §4). */
/** Cria um usuário com papel escolhido numa BU — para o caso "papel insuficiente". */
export async function criarUsuario(
  prisma: PrismaService,
  mantenedoraId: string,
  buId: string,
  email: string,
  role: 'OWNER' | 'ADMIN' | 'ATENDENTE',
  senha = 'senha-de-teste-1',
): Promise<string> {
  const bcrypt = await import('bcryptjs');
  const user = await prisma.appUser.create({
    data: {
      mantenedoraId,
      name: email,
      email,
      passwordHash: await bcrypt.default.hash(senha, 10),
    },
  });
  await prisma.userBuRole.create({ data: { userId: user.id, buId, role, grantedViaTipo: 'DIRETO' } });
  return user.id;
}

export async function limparBanco(prisma: PrismaService): Promise<void> {
  await prisma.webhookEvent.deleteMany();
  await prisma.message.deleteMany();
  await prisma.conversation.deleteMany();
  await prisma.activityLog.deleteMany();
  await prisma.tokenDeAcesso.deleteMany();
  await prisma.arquivo.deleteMany();
  await prisma.setorGrant.deleteMany();
  await prisma.userBuRole.deleteMany();
  await prisma.appUser.deleteMany();
  await prisma.buChannel.deleteMany();
  await prisma.businessUnit.deleteMany();
  await prisma.setor.deleteMany();
  await prisma.mantenedora.deleteMany();
  await prisma.loginAttempt.deleteMany();
}

/** Cria uma Mantenedora pela superfície interna — o caminho real de bootstrap. */
/**
 * Cria a Mantenedora **com o onboarding já concluído**.
 *
 * O bootstrap a cria PENDENTE (ADR-0016 §4), e é assim em produção. Os testes
 * que exercitam o produto vêm depois do wizard; quem exercita o portão é
 * `onboarding.e2e-spec.ts`, que usa `criarMantenedoraPendente`.
 */
export async function criarMantenedora(
  app: INestApplication,
  nome: string,
  email: string,
  senha = 'senha-de-teste-1',
) {
  const r = await criarMantenedoraPendente(app, nome, email, senha);
  const prisma = app.get(PrismaService);
  await prisma.mantenedoraSettings.update({
    where: { mantenedoraId: r.mantenedora.id },
    data: { onboardingConcluido: true },
  });
  return r;
}

export async function criarMantenedoraPendente(
  app: INestApplication,
  nome: string,
  email: string,
  senha = 'senha-de-teste-1',
) {
  const res = await request(app.getHttpServer())
    .post('/api/internal/mantenedoras')
    .set('x-internal-token', TOKEN_INTERNO)
    .set('x-requested-with', 'teste')
    .send({ nome, bu: { nome: `Número da ${nome}`, telefone: '5584999990000' }, owner: { nome: 'Dono', email, senha } })
    .expect(201);
  return res.body as {
    mantenedora: { id: string; nome: string };
    businessUnit: { id: string; nome: string };
    owner: { id: string; email: string };
  };
}

/** Faz login e devolve o cookie de sessão para reusar nas próximas chamadas. */
export async function login(app: INestApplication, email: string, senha = 'senha-de-teste-1'): Promise<string> {
  const res = await request(app.getHttpServer())
    .post('/api/bff/auth/login')
    .set('x-requested-with', 'teste')
    .send({ email, senha })
    .expect(200);
  const setCookie = res.headers['set-cookie'] as unknown as string[];
  return setCookie[0].split(';')[0];
}


## FILE api-app/test/canais.e2e-spec.ts

import { INestApplication } from '@nestjs/common';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import {
  contratarCanalNaoOficial,
  criarMantenedora,
  criarUsuario,
  limparBanco,
  login,
  metaFake,
  subirApp,
  tetoComCanalNaoOficial,
} from './helpers';

describe('canais da BU', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let A: Awaited<ReturnType<typeof criarMantenedora>>;
  let B: Awaited<ReturnType<typeof criarMantenedora>>;
  let cookieOwnerA: string;

  const post = (cookie: string, buId: string, body: object) =>
    request(app.getHttpServer())
      .post(`/api/bff/business-units/${buId}/channels`)
      .set('Cookie', cookie)
      .set('x-requested-with', 'teste')
      .send(body);

  beforeAll(async () => {
    // O canal não oficial é módulo (ADR-0016); o oficial é o piso e não passa
    // por aqui. Sem o teto, conectar o não oficial responde 404.
    tetoComCanalNaoOficial();
    ({ app, prisma } = await subirApp());
  });

  afterAll(async () => {
    await limparBanco(prisma);
    await app?.close();
    process.env.LH_CHANNEL_UNOFFICIAL = 'false';
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    metaFake.wabaRecusada = null;
    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');
    await contratarCanalNaoOficial(prisma, A.mantenedora.id);
    await contratarCanalNaoOficial(prisma, B.mantenedora.id);
    cookieOwnerA = await login(app, 'dono@alfa.test');
  });

  describe('POST channels — o trio (ADR-0012 §2)', () => {
    it('autorizado: OWNER conecta o canal oficial, e o phone_number_id é capturado na mesma ida', async () => {
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(201);
      expect(res.body.telefone).toBe('5584999990000');

      const canal = await prisma.buChannel.findFirstOrThrow({ where: { buId: A.businessUnit.id } });
      expect(canal.phoneNumberId).toBe('phone-123456789');
      // A janela de 24h é atributo do CANAL, e quem a liga é o tipo (ADR-0009).
      expect(canal.requiresWindow).toBe(true);
    });

    it('papel insuficiente: MEMBRO recebe 403 — a BU é dele, o poder é que não alcança', async () => {
      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'membro@alfa.test', 'ATENDENTE');
      const cookie = await login(app, 'membro@alfa.test');

      const res = await post(cookie, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(403);
      expect(res.body.code).toBe('PAPEL_INSUFICIENTE');
    });

    it('CROSS-TENANT: OWNER de Alfa recebe 404 ao conectar canal na BU de Beta', async () => {
      const res = await post(cookieOwnerA, B.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(404);
      expect(res.body.code).toBe('NAO_ENCONTRADO');

      // E nada foi criado do outro lado.
      expect(await prisma.buChannel.count({ where: { buId: B.businessUnit.id } })).toBe(0);
    });
  });

  describe('canal não oficial', () => {
    it('cria a instância e devolve o QR, com a janela DESLIGADA', async () => {
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'NAO_OFICIAL' }).expect(201);
      expect(res.body.qrcode).toContain('base64');
      expect(res.body.status).toBe('CONECTANDO');

      const canal = await prisma.buChannel.findFirstOrThrow({ where: { buId: A.businessUnit.id } });
      expect(canal.requiresWindow).toBe(false);
      expect(canal.evolutionInstanceName).toBeTruthy();
    });

    it('devolve QR novo para reparear', async () => {
      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'NAO_OFICIAL' }).expect(201);
      const res = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/channels/nao-oficial/qr`)
        .set('Cookie', cookieOwnerA)
        .expect(200);
      expect(res.body.qrcode).toContain('base64');
    });
  });

  describe('regras do vínculo', () => {
    it('a BU aceita um canal de cada tipo, e recusa o segundo do mesmo tipo', async () => {
      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(201);
      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'NAO_OFICIAL' }).expect(201);

      const repetido = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '999888777' }).expect(409);
      expect(repetido.body.code).toBe('CANAL_JA_EXISTE');
    });

    it('recusa WABA ID que não é numérico, antes de falar com a Meta', async () => {
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: 'abc' }).expect(400);
      expect(res.body.code).toBe('WABA_INVALIDO');
    });

    it('repassa a recusa da Meta como META_RECUSOU', async () => {
      metaFake.wabaRecusada = '123456789';
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(400);
      expect(res.body.code).toBe('META_RECUSOU');
    });

    it('remover exige ADMIN e libera o tipo para ser conectado de novo', async () => {
      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(201);

      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'viewer@alfa.test', 'ATENDENTE');
      const cookieViewer = await login(app, 'viewer@alfa.test');
      await request(app.getHttpServer())
        .delete(`/api/bff/business-units/${A.businessUnit.id}/channels/OFICIAL`)
        .set('Cookie', cookieViewer).set('x-requested-with', 'teste')
        .expect(403);

      await request(app.getHttpServer())
        .delete(`/api/bff/business-units/${A.businessUnit.id}/channels/OFICIAL`)
        .set('Cookie', cookieOwnerA).set('x-requested-with', 'teste')
        .expect(204);

      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(201);
    });

    it('listar canais é leitura: VIEWER enxerga', async () => {
      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(201);
      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'viewer2@alfa.test', 'ATENDENTE');
      const cookie = await login(app, 'viewer2@alfa.test');

      const res = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/channels`)
        .set('Cookie', cookie)
        .expect(200);
      expect(res.body.canais).toHaveLength(1);
    });
  });
});

