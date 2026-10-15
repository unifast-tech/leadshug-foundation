# Independent critique delta v3 — planning only

Frozen pushed Foundation baseline 87c28c6b0f767edde5edf30d4143844f0acd5c2a. Product code unchanged at TODO API/Web/workspace baselines. No approval, waiver, implementation, provider proof or delivery claim. User wants official/unofficial number registration locally first, then Nova conversa by manually supplied contact ST-CON-04; import later.

Full v2 critique and resolution assessments of six architecture findings are carried forward verbatim. This delta reviews NUM-CRIT-01/02 fixes and their interactions with the full frozen intent; keep all critique lenses, especially correctness/security/performance/elegance/structural_soundness/operational fit/test quality. Earlier findings are not silently waived: objective counterevidence may reopen any resolution; avoid reopening adjudicated unchanged behavior solely as repetition. Existing readiness and postcommit/Typebot sequencing limits remain explicit.

Changed architecture: new logical pairing atomically invalidates old identity trust before network and uses deterministic channelId+pairingEpoch external instance, stable within retries. Old mapping retired; only current new instance queried and proved identity by CAS can enable content, ambiguous provider identity remains pending. New keyed message acceptance owner spans sender result and echo, including echo-first, with same Message.id and trusted author enrichment; public DTO/window/timeline preserved. No cache, worker, outbox, external retry or takeover of legacy. Three nonblocking observations concretize existing requirements: logs redact URL secrets, Meta raw batches partition by resource owner, PostgreSQL tenant fixtures plus non-secret resource/credential identifiers at fake external port.

Read this COMPLETE bounded delta, including all exact current governing sections, full prior critique, tests and source snapshots. Prior v2 full packet remains immutable available if additional context needed; do not read private config or call providers. May write ONLY own report planning-critique-delta.json in this review directory. Return JSON verdict approve|revise, explicit positions on all lenses, closure per NUM-CRIT-01/02 and architecture interaction, concrete remaining blockers with locus/failure/correction/test, nonblocking observations scope-classified and residual limits. No arbitrary deadline. Review advisory only; root owns edits.

## Contract Boundary

Proposta ST-CON-01: jornada de cadastro de número, com infraestrutura local estritamente necessária, credenciais e recebimento reais. Local primeiro, Railway depois. Mesmo TODO governa aprovação, execução e closeout. Critérios de cadastro não podem ser substituídos por mock do provedor. O usuário também pediu Nova conversa pelo contato: esse próximo recorte está enquadrado em ST-CON-04 e não é absorvido neste contrato. Mudança material retorna à revisão/aprovação; worktrees, legado e promoção produtiva não estão autorizados.


## Scope

- [ ] SCOPE-01: jornada Adicionar número na gestão de BUs: apelido e modalidade; criar BU conforme regra existente ou selecionar BU administrável, com retry sem duplicar cadastro.
- [ ] SCOPE-02: oficial por Embedded Signup configurado pela instalação, sessão/BU correlacionadas, número escolhido validado na Meta, cancelamento/falha explícitos e recebimento configurado sem tomar callback alheio.
- [ ] SCOPE-03: credencial Meta exclusiva do vínculo, cifrada no backend; envio BFF, público e Typebot usam a credencial da BU/canal, sem token de cliente global compartilhado.
- [ ] SCOPE-04: não oficial por apelido/QR em Evolution própria, com criação idempotente da instância, autenticação do webhook, confirmação do telefone e renovação de QR.
- [ ] SCOPE-05: estado do cadastro, recebimento e verificação separados; observação atrasada não reativa vínculo removido ou substitui estado mais novo. Listar BUs não consulta provider.
- [ ] SCOPE-06: receber primeira mensagem real em cada canal de teste e visualizá-la na conversa correta, preservando grants, histórico paginado e regras de janela.
- [ ] SCOPE-07: testes de contrato/segurança/races/PostgreSQL e Playwright com runtime real; prova externa separada por canal.
- [ ] SCOPE-08: runtime local próprio do LeadsHug com Evolution fixada, persistência isolada, wiring de variáveis e runbook de callback HTTPS; sem tocar runtime/dados do legado.
- [ ] SCOPE-09: reautorização preserva credencial válida; novo pareamento invalida confiança anterior antes da rede e usa instância por epoch; identidade mantém proprietário após exclusão; aceitação única IN/OUT+echo e Typebot isolado por Mantenedora.


## Proposed Registration Contracts

Proposta técnica revisada, subordinada ao Scope/DoD; parecer de arquitetura e crítica brutos preservados, duas resoluções da crítica aguardam revisão delta independente.

### BFF e autorização

- `GET /api/bff/number-registrations/capabilities`: sessão válida; expõe apenas appId/configId/Graph version e disponibilidade/explicação por modalidade, nunca app secret/token/chave. Não chama provider.
- `POST /api/bff/number-registrations`: `Idempotency-Key` UUID obrigatório, body exatamente uma origem (`buId` existente ou `novaBu:{nome,setorId?}`) e `tipo:OFICIAL|NAO_OFICIAL`, `operation:NOVO|REAUTORIZAR`; REAUTORIZAR exige BU existente, channelId e expectedGeneration. BU existente exige ADMIN nela; BU nova exige ADMIN na Mantenedora e herda grants/setor pela mesma regra transacional de TenancyService. Oficial sem app/config/crypto configurados e não oficial sem módulo contratado+teto configurado falham antes de criar BU/provider. Para NOVO, nova BU (quando pedida), reserva do canal e tentativa são atômicas no DB; REAUTORIZAR reutiliza canal conforme contrato de ativação abaixo; refatorar reuso transacional da criação existente, preservando audit e expansão dos grants. Mesmo key/payload retorna tentativa original; mesmo key e payload diferente409. Nenhum HTTP de provider dentro da transação.
- `GET /api/bff/number-registrations/:id`: apenas ADMIN da BU e tenant da tentativa; devolve etapas, número redigido conforme DTO da BU, erro safe e progresso. Nunca devolve código/PIN/token. Sem sessão401, recurso fora do escopo404, papel insuficiente403; autorizar antes de revelar erro de payload/estado.
- `POST /:id/authorize` (prefixo anterior): oficial, nonce+code recebido no callback SDK. Pertence à sessão exata/usuário da tentativa, hash da sessão/expiração/nonce checados; CAS PENDING→PROCESSING antes de trocar code. Código não persiste nem entra em URL/log/audit. Envelope candidato do token persistido na tentativa antes dos passos seguintes; nunca substitui a credencial ativa nesta etapa. Timeout de troca fica AMBIGUO e exige nova autorização; nunca reenvia code consumido automaticamente.
- `GET /:id/options`: somente depois de autorizar; retorna WABAs/números permitidos pela credencial dessa tentativa. Backend prova app/audience, escopos e pertencimento do recurso; IDs postMessage não são autoridade. Página máxima100 e continuação explícita, sem scan infinito. Número escolhido sempre confirmado pelo operador; nunca escolher primeiro por conveniência.
- `POST /:id/confirm`: `wabaId,phoneNumberId,modoRegistro` validados contra provider e grant atual. Telefone obtido do provider deve coincidir com BU já numerada; se BU sem telefone, preencher por CAS na mesma transação do vínculo. A identidade externa tem proprietário durável e único por provider/recurso, inclusive após exclusão do canal; colisão ou tentativa de transferir entre BUs retorna409 sem revelar tenant alheio. Só a confirmação da mesma identidade permite promover a credencial candidata por CAS.
- `modoRegistro:NOVO` admite PIN6dígitos e passo de register explícito conforme modalidade convencional Cloud API. `modoRegistro:JA_REGISTRADO` não redefine PIN nem chama registro destrutivo; vínculo fica pendente de prova operacional quando a leitura Meta não comprovar readiness. PIN não retorna em DTO/log, só persistência cifrada se necessário à recuperação. Não realizar migração/coexistência/unregister.
- `POST /:id/advance` e `POST /:id/retry`: uma rodada tem no máximo3requests externos, cada um timeout10s e um único lease de45s por vínculo; persistir estágio/resultado após cada passo. Não há retry automático de mutação ambígua. Read-before-retry reconcilia estágio; se não houver operação segura, declarar pendente/reautorizar em vez de fingir exactly-once externo. Assinar WABA só depois de mapping channel↔providerID local durável; webhook pode chegar antes do fim sem perder o tenant correto. Configurar callback apenas da própria instalação/conta de teste, sem override alheio.
- `POST /:id/cancel`: antes de side effect externo pode encerrar reserva; depois conserva vínculo/etapas parciais e informa limpeza necessária. Não apagar BU nem conversas, não fazer unsubscribe de WABA compartilhada automaticamente. Consumidores atuais exigem credencial e readiness do vínculo antes do OUT.
- `POST /api/bff/business-units/:buId/channels/:tipo/verify`: ADMIN, um lease por vínculo, mesmo budget3×10s; listagem nunca faz fan-out. Resultado muda só a dimensão efetivamente observada. Erros externos mapeados para códigos de catálogo, sem texto/token/URL brutos.
- `POST /api/bff/business-units/:buId/channels/nao-oficial/pair` inicia/renova pairing com intent INITIAL ou RENEW, sessão ADMIN, anti-CSRF, lease e geração atual. O antigo GET de QR retorna405 sem chamar Evolution nem iniciar/renovar conexão; nenhuma mutação de provider em GET. Resposta contém QR efêmero só ao admin; o QR nunca é persistido em eventos/audit. Nova UI não usa o POST antigo que conecta WABA pelo token global. Rota antiga deve recusar fluxo incompleto com instrução do contrato novo, sem fallback de token; atualizar seus testes de expectativa dentro do escopo.

### Persistência e recuperação

`ChannelRegistrationAttempt` guarda id, Mantenedora/BU/canal, tipo, userId, hash de sessão, nonce hash, idempotencyKey+requestHash, estado, versão, leaseUntil, expiresAt, stage e erro safe. Unique Mantenedora/idempotencyKey e slot BuChannel(buId,type) já existente. IDs externos únicos por tipo; migrations detectam conflito preexistente antes de impor constraint. IDs internos podem ser prealocados sem compromisso de provider.

`ChannelCredential` mantém token/PIN em envelope com keyId/version/nonce/ciphertext/tag, ligado ao canal da BU e geração; não inventar vault genérico nem refletir o envelope no model público. AAD inclui provider/BU/channelID/generation. Tamper/decrypt/key ausente falha fechado, nunca fallback global. Passar credencial por interface de adapter, sem vazá-la a audit ou payload de domínio. Não copiar secrets do ambiente legado.

Cadastro pode ficar `PENDING_AUTH`, `PENDING_NUMBER`, `REGISTERING`, `PENDING_RECEIPT`, `CONNECTED`, `ERROR`, `CANCELLED`, com dimensão de providerConnection/receipt/credential e timestamps. O enum físico e mapeamento para status atual devem ser explícitos na migração; nenhum label mágico na UI. `CONNECTED` exige etapas aplicáveis concluídas, identidade correta e conexão confirmada; oficial já registrado sem endpoint conclusivo não recebe falso CONNECTED só pela lista de números. Primeira IN autenticada pode comprovar recebimento, não validade permanente do token de saída. Teste IN/OUT externo certifica somente a execução observada, não saúde contínua.

Reserva idempotente da instância Evolution usa nome derivado de channelId+pairingEpoch persistida, estável durante retries desse epoch; nunca nome do operador+timestamp. Nova rodada de pareamento usa identidade externa distinta, conforme contrato de confiança abaixo. Se create retorna timeout, consultar a mesma identidade antes de retry; nenhuma segunda instância. Webhook deve ser configurado e verificado antes de concluir. Leitura de estado e evento usam geração e versionamento; retry de geração anterior não escreve após remove/recreate. Desconectar não apaga histórico. Callback tardio de instância sem vínculo não cria BU/tenant.

A tentativa expira em10min enquanto espera autorização. Após credencial ativa promovida, operações de recuperação do canal são administrativas e reautorizam grant/sessão corrente; não reaproveitam code/nonce antigos. Lease expirado não é sucesso e requer reconciliação; nenhuma transação DB é mantida durante rede. Não criar worker global ou sistema genérico de jobs neste slice.

### UI e integrações

Wizard: nome/BU → modalidade → janela Meta ou QR → confirmar número → mostrar cadastro/recebimento e ação de retry quando parcial. Cancelar popup, trocar BU, desmontar tela ou nova tentativa invalida callbacks/efeitos antigos no cliente; backend ainda revalida scope. SDK em postMessage aceita apenas origens Meta exatas e formato esperado; evento é dica para seleção e não prova tenant/ID. Callback de login fica preso à geração/attempt/nonce corrente; prova server-side da credencial/ID é obrigatória.

Permissões existentes preservadas: ADMIN da BU para conectar existente; ADMIN da Mantenedora para criar BU; ATENDENTE não ganha gestão; módulo não oficial depende do teto e contratação. Dados sensíveis nunca vão a config.js/bundle. UI mostra ausência de configuração e falhas por etapa, sem exigir WABA/token manual do operador comum no fluxo Meta. Administrador pode reautorizar conta já cadastrada; credencial manual de número já registrado, se usada, é caminho técnico explícito com conferência Meta e cifra, jamais env global implícita.

BFF responder e API pública responder preservam DTOs/janelas. Typebot preserva o comportamento dentro da mesma Mantenedora, com seleção e sessão obrigatoriamente isoladas pelo tenant da BU verificada. A entrada acrescenta identidade verificada e deduplicação transacional; credenciais são resolvidas por vínculo em todos os consumers. DI deve convergir nos módulos BFF/público/webhook. Primeira IN cria/reusa conversa pelo contrato existente, não manual. Nova conversa por contato aguardará ST-CON-04.

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

### Reautorização e ativação da credencial (NUM-ARCH-06)

Criar tentativa distingue `operation:NOVO|REAUTORIZAR`. NOVO reserva slot vazio; REAUTORIZAR recebe channelId e expectedGeneration e reutiliza o slot existente, inclusive canal migrado sem credencial. Valida ADMIN/tenant antes do estado; conflito de geração409. A nova tentativa torna-se currentAttemptId por CAS, sem mudar a credencial ativa. Reserva anterior expirada/cancelada sem efeito externo pode ser substituída, preservando BU; com efeito parcial, recuperar a mesma identidade externa, sem criar segunda instância.

Cada nova autorização depois de code consumido, expirado ou troca ambígua exige tentativa e nonce novos; não há reapresentação automática do code. `ChannelRegistrationAttempt` mantém envelope candidato separado de `ChannelCredential` ativa. AAD candidato inclui propósito, attemptId, provider, BU, channelId e geração; AAD ativo inclui propósito e versão ativa. Após validação server-side de identidade/escopos e confirmação do mesmo número, uma transação curta verifica currentAttemptId+generation+activeCredentialVersion e promove o envelope, recifrando para AAD ativo. Candidata de outro número, sessão revogada ou tentativa velha não pode substituir a ativa. Credencial utilizável anterior segue em uso até promoção; se já inválida, mostrar PENDENTE_CREDENCIAL, sem fallback global. Cancelar/expirar elimina o segredo candidato, conserva somente metadados seguros e mantém a ativa.

### Identidade durável, entrada e automação (NUM-ARCH-01..04)

`ProviderResourceIdentity` tem unique(provider,externalResourceId), buId proprietário imutável e vínculo atual opcional. Exclusão do BuChannel mantém tombstone/proprietário; reativação somente na mesma BU. Transferência de providerID entre BUs não é permitida neste recorte. Migration detecta colisões e aborta sem fundir/apagar dados. Meta ingress resolve phoneNumberId por essa identidade durável antes de aceitar conteúdo; webhook de recurso retirado fica sem efeitos de domínio até reativação na mesma BU. Um evento externo não carrega nossa geração: não se apresenta CAS local como prova da geração de origem. Reatribuição a outra BU retorna409 e impede que evento antigo seja encaminhado ao novo tenant.

Evolution ingress exige autenticação, instância da geração corrente e comprovação do número próprio correspondente ao telefone da BU ANTES de registrar conteúdo, Message, unread, realtime ou Typebot. Estado open sozinho não comprova número. Enquanto a identidade não foi confirmada, rejeitar com503 PENDING_IDENTITY e registrar apenas metadados seguros; divergência gera409 IDENTITY_QUARANTINED, sem conteúdo em raw/audit. Depois da comprovação correta, um retry pode ser aceito uma vez. Não há buffer/importação neste recorte e não se garante replay pelo provider: UI/runbook orientam aguardar número confirmado antes da mensagem de teste e reenviá-la se necessário. Eventos de instância removida/desconhecida não criam vínculo nem conteúdo. Adaptador distingue telefone do contato de identificadores LID: usar telefone alternativo comprovado pelo payload/contrato suportado, ou rejeitar identidade ambígua; nunca interpretar dígitos de @lid como telefone.

Entrada aceita exige externalMessageId não vazio e chave única PostgreSQL (providerResourceIdentityId,externalMessageId); identidade já incorpora provider. Mesmo ID em recursos diferentes não colide. `Message` legado pode manter FK/chave nulas; não inventar IDs nem apagar duplicatas históricas. Só backfill inequivocamente comprovado é admitido. Novas entradas sem ID ficam rejeitadas com erro seguro antes de efeito de domínio. Após identidade validada, transação curta aceita Message e cria/reusa conversa BU/contato com incremento unread; conflito de unique desfaz os efeitos daquela tentativa. Somente a transação vencedora publica realtime e aciona automação. Echo OUT e resultado do sender compartilham a mesma aceitação transacional por identidade/ID, inclusive quando o echo chega primeiro; não criam outra Message, IN ou unread. Contrato detalhado abaixo. Replay sequencial/concorrente retorna sucesso idempotente para evento já aceito. Não se promete exactly-once externo: crash depois do commit pode deixar publicação/automação ausente; não repetir bot automaticamente nem introduzir plataforma de jobs/outbox neste recorte. Essa limitação precisa constar do runbook.

IncomingService deriva Mantenedora da BU verificada. Busca de trigger exige bot.mantenedoraId desse tenant e buId exata OU trigger global dentro do MESMO tenant. Sessão retomada deve pertencer à mesma Mantenedora/BU/contato; sessão estrangeira falha fechado antes de texto externo. Criação deriva owner do contexto verificado, não de um bot arbitrário. Dois tenants com triggers globais concorrentes não compartilham bot, texto, sessão, saída ou credencial. São defeitos preexistentes na superfície tocada, cuja correção fica expressamente incluída para sustentar o recebimento deste cadastro.

### Confiança do pareamento e reconciliação OUT (NUM-CRIT-01/02)

Antes de INITIAL/RENEW produzir qualquer efeito externo, transação curta reserva pairingEpoch monotônica, limpa ownNumberVerified/verifiedEpoch e invalida leases/observações antigas por CAS. Cada novo pareamento lógico tem nome externo derivado de channelId+epoch, imutável nessa rodada; retry/renovação de QR pendente reutiliza a MESMA tentativa/epoch/instância, sem criar outra. RENEW de um canal antes verificado é novo epoch, não mera leitura de QR. Evento ou verificação pendente do epoch anterior nunca restaura confiança. Instância antiga fica aposentada no mapping durável; callback antigo só permite metadados seguros, nunca conteúdo/receipt/estado do canal atual.

O desenho escolhe identidade de instância específica do epoch, sem depender de o payload carregar uma geração local. Só observações da instância EXATA da rodada atual podem participar da confirmação. `open`/wuid isolados não reabilitam conteúdo: etapa administrativa bounded consulta identidade própria dessa instância nova no provider, valida resposta/ownPhone e grava verifiedEpoch por CAS contra currentAttemptId+pairingEpoch+generation. O cadastro/criação/configuração precede essa consulta; não aceitar resposta de outra instância nem confiar no nome informado pelo operador. Se o provider fixado não oferecer prova inequívoca da identidade da instância nova, manter PENDING_IDENTITY e bloquear a prova externa. Telefone vazio da BU só é preenchido com identidade comprovada por CAS, assim como no oficial; divergente permanece quarentena.

Antes de criar outra instância externa, reconciliar criação/aposentadoria/limpeza da instância anterior própria; timeout é ambíguo e exige read-before-retry. Ação RENEW informa ao administrador que inicia novo pareamento e interrompe aceitação até confirmação. Limpeza só atua em instância criada por este LeadsHug e com ownership comprovado; nenhuma adoção/remoção de instância legada. Mesmos budgets/leases, nenhuma transação sobre HTTP, worker ou buffer novo. Aposentar mapping ocorre antes da rede, independentemente de a limpeza externa terminar. Eventos sem a nova identidade ficam rejeitados conforme503/409 já definidos, sem promessa de replay.

Um serviço de aceitação de mensagem no domínio inbox é o owner da chave (providerResourceIdentityId,externalMessageId) para TODAS as novas gravações com ID: entrada, eco OUT, resultado de envio BFF/público e Typebot. Sender captura a identidade do canal autenticado, faz HTTP fora de transação e depois cria-ou-reconcilia pelo mesmo índice PostgreSQL. Sender-first, echo-first e ecos concorrentes devolvem o MESMO Message.id; conflito de unique não pode virar segundo registro nulo nem erro de inserção depois do envio bem sucedido. Validar owner BU/conversa/contato/direção na reconciliação; incompatibilidade é erro/quarentena de identidade, sem sobrescrever outro recurso. Registro local sem externalId confirmado conserva pendência/erro explícitos, sem inventar ID, retry externo ou garantia de deduplicação por ID inexistente.

Eco primeiro cria OUT sem autoria humana inventada; resultado interno enriquece o mesmo registro com conteúdo/autoria humana ou Typebot comprovados pelo caller. Eco posterior não apaga/substitui essa autoria e não muda createdAt/ID. Só criação vencedora emite evento de nova mensagem; enriquecimento preserva a identidade e usa refresh/projeção existente, sem novo IN, unread ou bot. Retorno BFF/público mantém seus contratos e contém o registro reconciliado. Invariantes de janela, permissão, conversa BU/contato, ordenação e timeline permanecem. Nenhum cache de ecos em memória ou lookup-antes-insert substitui o índice/transação. Continua explícito o limite de crash depois do commit e antes da publicação; não há claim exactly-once externo.

### Segredos transitórios e webhook raw

Code SDK e PIN podem existir transitoriamente no formulário/memória do browser e seguir via BFF HTTPS; nunca em URL, storage, trace, screenshot, log ou DTO de retorno. Token, chave e envelope ficam somente no backend. Antes de persistir evento raw de provider autenticado, redigir recursivamente apikey, token, authorization, code, PIN, QR e componentes secretos de URLs; erros/audit usam catálogo e metadados allowlisted. Evento sem identidade verificada não persiste conteúdo. Harness envia envelope Evolution com apikey fictícia e comprova sua ausência em raw/audit/DTO/erro. QR só é devolvido efemeramente ao administrador no POST autorizado. Gateway Nginx, proxy e logs de aplicação não registram URI/token do callback Evolution: política explícita remove caminho secreto e query de access/error logs, inclusive erros; harness passa segredo fictício pelo gateway real e inspeciona logs/artefatos. Callback por header só se suportado e comprovado no provider fixado, sem presumir capacidade.

Meta raw é particionado por recurso verificado/BU, não por corpo de request inteiro. Batch assinado com entry/change/value de BUs diferentes produz registros scoped separados; fragmento desconhecido/retirado/sem identidade contribui apenas metadados allowlisted, sem conteúdo. Assinatura é verificada sobre o corpo original antes de parse/partição. REG-SEC-12/13 concretizam requisitos já existentes de segredo/owner, sem novo armazenamento genérico.


## Out of Scope

- Nova conversa proativa/manual pelo contato: ST-CON-04 é o próximo recorte solicitado, incluindo abertura oficial por template aprovado quando necessário.
- Importação de histórico, coexistência Business App, migração de número em uso, download/envio binário, templates/campanhas, transferência e estados de entrega/leitura.
- Billing/linha de crédito de BSP: modalidade proposta é Tech Provider com cobrança direta da conta de teste; elegibilidade é precondição externa, nunca simulação silenciosa.
- Alterar callback de app/número de outro sistema, revogar credencial ou apagar instância real em uso. Usar número de teste sem integração concorrente.
- Deploy/promover código para Railway/produção. Segredos reais em commits; modificação manual de gitlinks/.gitmodules; worktrees/cópias auxiliares.


## Diff Expectation Contract

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
| api | src/domain/inbox/conversations.service.ts | M | Credencial scoped e persistência OUT na mesma aceitação keyed de echo/sender; preservar DTO/janela/timeline. |
| api | src/domain/inbox/message-acceptance* | A,?? | Owner de aceitação/reconciliação transacional e testes unitários. |
| api | src/domain/inbox/incoming.service.ts | M | Credencial Typebot, isolamento tenant e aceitação idempotente da entrada. |
| api | src/domain/inbox/incoming.typebot.integration.spec.ts | M | Caller Meta e triggers/sessões de tenants concorrentes. |
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
| api | prisma/schema.prisma | M | Attempt/candidate/credential/status, identidade externa durável e chave de deduplicação. |
| api | prisma/migrations/*number_onboarding*/migration.sql | A,?? | Migração da persistência de cadastro. |
| api | test/*canais* | A,M,?? | E2E de cadastro e idempotência. |
| api | test/*number-onboarding* | A,?? | E2E/fixtures próprios. |
| api | test/helpers.ts | M | DI dos adapters e credenciais de teste. |
| api | test/setup-env.ts | M | Configuração determinística de testes. |
| api | test/browser-server.cjs | M | Backend real e fixtures de cadastro. |
| api | test/timeline-fixtures.cjs | M | Somente credencial de fixture exigida pelo novo resolver. |
| api | test/webhooks.e2e-spec.ts | M | Receipt, auth e races. |
| api | test/api-publica.e2e-spec.ts | M | Credencial e echo-first/sender-first no envio público; contrato preservado. |
| api | test/atendimento.e2e-spec.ts | M | Credencial, echo-first/sender-first e autoria/ID reconciliados; demais invariantes preservados. |
| api | test/typebot.e2e-spec.ts | A,?? | Credenciais e negativos de isolamento; comportamento dentro do tenant preservado. |
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
| foundation | modules/inbox-and-conversations.md | M | Invariantes de aceitação idempotente e automação isolada por tenant; timeline preservada. |
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
- [ ] DOD-08: NUM-ARCH-01..06 e NUM-CRIT-01/02 cobertos por harness de tenant, replay, identidade, reautorização e POST de pairing; nenhum segredo de envelope webhook persiste.
- [ ] DOD-07: decisões consolidadas no módulo owner, evidence matrix completa, source commits e guardas go antes do closeout local.


## Validation Steps

- [ ] VAL-01: unidade/adapter para cifra e AAD, payload Meta/Evolution, erro/timeout, seleção entre múltiplos números e contrato de registro.
- [ ] VAL-02: PostgreSQL E2E para sessão/grant/tenant, tentativa expirada/cancelada/replay, disputa create/delete/recreate/verificação/evento e persistência de falha parcial.
- [ ] VAL-03: Playwright do cadastro/QR, popup cancelado/erro/timeout, mudança BU e resposta velha; backend/sessão/DB reais, servidor de provider de teste apenas como porta externa.
- [ ] VAL-04: migrate deploy e CI-equivalent API/Web/workspace da fonte final; fingerprints do bundle antes dos workers, banco exclusivo e execução sem sobreposição de suites destrutivas.
- [ ] VAL-05: prova externa local por canal, com autorização Meta/QR real, IN na BU certa, OUT recebida pelo interlocutor e recuperação permitida da conexão.
- [ ] VAL-06: EPS/FRC/BCI/RLS conforme plano; security, debt, architecture_adherence, TQA, audit especializado e final review antes de completar.
- [ ] VAL-08: executar REG-SEC-01..13 do plano de validação, incluindo replay por provider, renovação de canal já verificado, echo-first/sender-first com autoria, tombstone, candidata, CSRF e logs/partição raw.
- [ ] VAL-07: consolidar módulo, validar contrato/diff/coerência e closeout; nenhum claim de produção pronta.


## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:** `foundation_documentation/modules/identity-and-tenancy.md`, `foundation_documentation/modules/inbox-and-conversations.md`, `foundation_documentation/modules/audit-and-history.md`.
- **Planned decision promotion targets:** integrations-and-channels: Cadastro de números, Credenciais por canal, Estados e contratos BFF, Callback e operação local; identity-and-tenancy: autorização das rotas de cadastro; inbox-and-conversations: deduplicação/identidade e isolamento da automação; audit-and-history: eventos sem segredos.
- **Module decision consolidation targets:** as mesmas seções antes do código das novas rotas; estado Verified apenas após validação. Constituição preservada; não reescrever decisões históricas/estudos concluídos.


## Decisions (Resolved Before Freeze)

- D-01: uma BU continua representando o número; selecionar BU administrável ou criar pelo endpoint existente; modalidade não cria tenant novo. Telefone canônico não é sobrescrito por número divergente.
- D-02: Embedded Signup Tech Provider é a jornada oficial; IDs do SDK são apenas candidatos e são verificados com a credencial obtida e o provider. Sem app configurado, botão indisponível com explicação, sem conexão simulada.
- D-03: tentativas persistidas scoped expiram em10min antes da autorização, nonce/code uso único e CAS; NOVO reserva slot vazio, REAUTORIZAR reutiliza canal ocupado com expectedGeneration. Candidata separada da ativa, promoção atômica após identidade confirmada. Nada de transação DB aberta durante HTTP externo.
- D-04: credencial oficial por BuChannel, envelope AES-256-GCM com chave32bytes e keyId de instalação, nonce único, AAD com propósito/provider/BU/channelId/geração e attemptId ou versão ativa. Code/PIN transitórios no formulário e BFF HTTPS, sem persistência do code ou exposição em logs; token/envelope somente backend e PIN cifrado quando necessário. Nenhuma queda para token global de cliente.
- D-05: oficial tem passos separados autorizar→validar identidade→registrar quando aplicável e explicitamente confirmado→assinar WABA→verificar recebimento; falha parcial recuperável e visível. Não sobrescrever callback de outro sistema.
- D-06: Evolution v2.3.7 fixada por digest, instância própria reservada com nome derivado do ID estável do vínculo; webhook autenticado configurado antes de afirmar cadastro completo. Pairing/renovação apenas POST ADMIN com anti-CSRF; GET não muta provider. QR é efêmero, não histórico/audit. Cada novo pareamento lógico invalida confiança antes da rede e usa instância própria por pairingEpoch; retry reutiliza a rodada. Identidade da instância atual deve ser comprovada por consulta bounded e CAS antes de conteúdo; falha mantém pendência/rejeição, sem promessa de replay.
- D-07: providerConnection/registration/receipt/lastVerification são observações distintas; timeout não inventa offline/online. Query/observação local tem geração e CAS; eventos externos não provam nossa geração. Identidade externa retém owner após exclusão e não muda de BU; listagem apenas DB, verificação explícita bounded.
- D-08: atualizar todo consumo Meta existente (BFF/público/Typebot) para resolver credencial pelo vínculo; manter contratos públicos de resposta e janela; Typebot seleciona triggers/sessões da Mantenedora da BU e entrada tem unique por recurso/ID externo com aceitação transacional compartilhada por sender e echo OUT; criação vencedora para unread/realtime/automação, reconciliação preserva ID/autoria e contratos públicos. Bootstrap pode abrir administração/onboarding sem token de cliente já obtido; piso oficial é capacidade configurada, não número previamente conectado.
- D-09: local primeiro com Evolution/DB/cache próprios e runbook HTTPS sem domínio presumido; Railway, coexistência, histórico e Nova conversa proativa ficam fora desta entrega.
- D-10: API/Web source e runtime validados serialmente no checkout principal, um executor, sem worktrees ou mudança manual dos gitlinks.


## Decision Baseline (Frozen Before Implementation)

Proposta revisada D-01..D-10: NUM-ARCH-01..06, NUM-CRIT-01/02 e requisitos de execução NUM-OBS-01..03 integrados nos contratos acima, escopo, paths e critérios. Congelamento renovado antes da crítica independente; mesma jornada de cadastro. Ainda não há APROVADO de implementação; esta baseline congela a proposta revisável, não afirma produto implementado.


## Assumptions Preview (Required Before Plan Review)

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Há uma credencial global Meta hoje. | api-app/src/integrations/meta/meta.client.ts:31; api-app/src/domain/inbox/conversations.service.ts:292; api-app/src/domain/inbox/incoming.service.ts:125 | Corrigir diagnóstico e consumers antes do freeze. | High | Keep as Assumption |
| A-02 | Cadastro oficial atual só consulta WABA e escolhe primeiro. | api-app/src/domain/channels/channels.service.ts:31-74 | Reavaliar implementação antes de substituir. | High | Keep as Assumption |
| A-03 | Middleware BFF já exige sessão e anti-CSRF. | api-app/src/surfaces/bff/session.middleware.ts:80-171 | Reforçar superfície; nunca abrir callback BFF público. | High | Keep as Assumption |
| A-04 | Listagem UI lê DB; não há consumidor do connectionState. | web-app/src/telas/Numeros.tsx:12-19; api-app/src/integrations/evolution/evolution.client.ts:66-68 | Consolidar owner existente. | High | Keep as Assumption |
| A-05 | Usuário pode disponibilizar ambos os números de teste. | Resposta explícita nesta sessão em2026-10-15 | VAL-05 fica bloqueado, não substituir por fake. | High | Promote to Decision |


## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces

A lista do Diff Expectation Contract é a autoridade de paths. Alterar callers Meta existentes para credencial scoped, wiring por módulo Nest, domain channels, schema, controllers, Numeros e runtime local; não alterar timeline/Inbox.

### Ordered Steps

1. Publicar freeze e obter architecture_opinion/critique; resolver achados e guardas antes de pedir APROVADO.
2. Após aprovação, executor único cria branches locais e consolida contratos dos módulos antes de novas rotas.
3. Test-first: migration/reserva/idempotência/cifra e isolamento; refatorar consumers Meta e bootstrap para credenciais por canal, sem fallback global.
4. Persistência compartilhada IN/OUT/echo por identidade, preservando autoria/DTO e prova de echo-first no BFF/público/Typebot. Cadastro oficial com candidata e promoção CAS/reauth no slot; não oficial por reserva/POST QR/webhook com novo pairingEpoch/instância e trust reset antes da rede. Implementar identidade durável, rejeição pré-identidade, dedupe transacional, redaction raw e Typebot tenant-scoped; harness REG-SEC antes da prova externa.
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


## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

Achados exatos preservados em planning-architecture.json. `fixed-in-plan` significa correção contratual, ainda sem código/prova; cada resolução será examinada na crítica independente e no harness após APROVADO.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| NUM-ARCH-01 | high | release-blocker | fix-current-contract | Typebot tocado exige isolamento tenant já canônico | fixed-in-plan | D-08; contratos de entrada; REG-SEC-01; VAL-08 |
| NUM-ARCH-02 | high | release-blocker | fix-current-contract | Recebimento do cadastro não pode duplicar efeitos | fixed-in-plan | D-08; unique/transação; REG-SEC-02; VAL-08 |
| NUM-ARCH-03 | high | release-blocker | fix-current-contract | Pareamento exige comprovar número antes do conteúdo | fixed-in-plan | D-06; rejeição pré-identidade; REG-SEC-03; VAL-08 |
| NUM-ARCH-04 | high | release-blocker | fix-current-contract | Evento atrasado não pode trocar owner BU | fixed-in-plan | D-07; tombstone sem transferência; REG-SEC-04; VAL-08 |
| NUM-ARCH-05 | medium | release-blocker | fix-current-contract | Pairing mutante exige POST/anti-CSRF | fixed-in-plan | D-06; contrato BFF; REG-SEC-05; VAL-08 |
| NUM-ARCH-06 | medium | release-blocker | fix-current-contract | Reautorizar canal existente sem substituir ativa prematuramente | fixed-in-plan | D-03/04; candidata+CAS; REG-SEC-06/07; VAL-08 |
| NUM-CRIT-01 | high | release-blocker | fix-current-contract | Repareamento já prometido precisa invalidar prova anterior | fixed-in-plan | D-06; instância por epoch e trust reset; REG-SEC-10 |
| NUM-CRIT-02 | medium | release-blocker | fix-current-contract | Dois writers da mesma Message precisam compartilhar aceitação | fixed-in-plan | D-08; message-acceptance e diff; REG-SEC-11 |
| NUM-OBS-01 | medium | by-design/no-action | enforce-existing-requirement | Requisito secret-free já vinculante, sem defeito de gateway implementado alegado; harness concretizado | covered-in-plan | REG-SEC-12; runtime/logs; DOD-03 |
| NUM-OBS-02 | medium | by-design/no-action | enforce-existing-requirement | Raw scoped já vinculante; batch por owner agora explícito, sem plataforma nova | covered-in-plan | REG-SEC-13; contrato raw; audit owner |
| NUM-OBS-03 | low | by-design/no-action | enforce-existing-requirement | Harness de tenant/credencial já requerido; observar identificador não secreto e DB real | covered-in-plan | REG-SEC-01/11; VAL-02/08 |

Adicional de coerência do autor: envelope raw redigido e code/PIN transitórios explicitados, sem alterar modelo de autorização; REG-SEC-08/09.


## FILE foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/planning-critique.json

{
  "review_kind": "critique",
  "review_date": "2026-10-15",
  "verdict": "revise",
  "planning_only": true,
  "implementation_authority": "none; this report is advisory and grants neither APROVADO nor a waiver",
  "reviewed_packet": {
    "path": "foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/critique-packet-v2.md",
    "sha256": "6c29940c895577f71d21bae6db43e0975fbbffc6df5b064d291373f9668b6fd2",
    "bytes": 270204,
    "lines_read": 4743,
    "complete_packet_read": true,
    "foundation_baseline_declared_in_packet": "850feeb63869de7410b4c279c8e0956804aec68b",
    "api_baseline_declared_in_packet": "ae6a9662c29b77276351aa9de653a47276372246",
    "web_baseline_declared_in_packet": "4e56f6c1f4515b918d05b8c87e890d42e8542c56",
    "workspace_baseline_declared_in_packet": "cab23188ec796f79131467dcce0a16acedab8d4f",
    "baseline_proof_limit": "The immutable local packet hash was checked. Pushed-baseline and unchanged-source declarations are package inputs; this reviewer made no remote calls or independent remote-ref attestation.",
    "isolation": "Fresh internal no-context reviewer; no implementation transcript or implementing-agent memory was supplied.",
    "method": "Read every packet line, including the complete previous architecture opinion, revised contract, source snapshots, canon, validation plan and included tests. Evaluated the six resolutions and the complete plan independently. Source line numbers below refer to the FILE blocks in this immutable packet.",
    "additional_instruction_context": [
      "AGENTS.md",
      "delphi-ai/main_instructions.md",
      "delphi-ai/system_architecture_principles.md",
      "delphi-ai/ecosystem_template_configuration.md",
      "delphi-ai/workflows/docker/profile-selection-method.md",
      "delphi-ai/workflows/docker/todo-approval-gates-method.md",
      "delphi-ai/workflows/docker/effort-selection-method.md"
    ],
    "readiness_check": "bash delphi-ai/verify_context.sh returned Environment Verified: PACED-Ready; this is instruction-context readiness, not product/provider validation.",
    "routing_evidence": "evidence/routing-critique.json records go for formal-reviewer / critique / gpt-6.1-sol / max, proof_mode declared; read, not rerun by this reviewer.",
    "actions_not_performed": [
      "No product or TODO edits",
      "No private configuration or credential reads",
      "No external-provider, network or remote-ref calls",
      "No product tests, migrations, runtime startup or delivery claims",
      "No waiver or implementation approval"
    ]
  },
  "overall_assessment": "Retain the proposed architecture. Persisted attempts, separate candidate and active credentials, channel-scoped encryption, durable provider ownership, a short transactional incoming boundary, bounded provider calls and DB-only listing form a coherent solution for ST-CON-01. All six earlier findings have substantial contractual resolutions. Two remaining interactions need a concrete contract and discriminating tests before approval: renewing an already verified Evolution pairing must revoke the old identity proof, and sender persistence must participate in the same identity/message reconciliation promised for outbound echoes. These are bounded gaps in the revised plan, not assertions that unimplemented changes have regressed the product.",
  "correctness_position": "Revise the two lifecycle/concurrency boundaries below. The initial onboarding, reauthorization, collision, ambiguity and incoming duplicate paths are otherwise described consistently. Preserve current public response and timeline contracts while correcting internal persistence; neither issue requires ST-CON-04, history import or a generic workflow platform.",
  "security_position": "The revised tenant predicates, server-side Meta resource proof, authenticated webhooks, one-use authorization, candidate isolation, AES-GCM/AAD and fail-closed decryption are sound. Initial Evolution input now has the required identity gate. The same gate needs an explicit trust-reset and stale-observation rule for RENEW, because a persisted proof from a previous pairing is not proof of the phone that has just scanned a new QR. Secret-free request logging and per-resource raw-event scoping remain implementation obligations under the existing contract, with focused harness notes below.",
  "performance_position": "Favorable, subject to the planned measurements. DB-only listing avoids provider fan-out; indexed attempt/credential/resource lookups and the message uniqueness constraint are appropriate. Three 10-second calls under a 45-second per-link lease bound a recovery round without holding a DB transaction during HTTP. The recommended fixes add short indexed/CAS operations and an indexed outbound upsert/reconciliation, rather than workers or an outbox. The small synthetic workload and pinned digest establish neither production capacity nor a continuous-health SLO.",
  "elegance_position": "Retain the small domain-specific state machine and explicit provider adapters. Make identity trust a property of the current pairing epoch, and give outbound message acceptance one consistent internal owner. Those changes remove implicit coupling. An in-memory echo cache, ad hoc query-before-insert exceptions, route-specific CSRF exceptions, global token fallback or a generic saga/vault/job framework would weaken this design.",
  "structural_soundness_position": "The BU remains the number, transports remain BU channels, and conversations remain keyed by BU/contact. Durable provider ownership and separate candidate/active credentials strengthen these boundaries. The two blockers are boundary omissions: channel existence/current generation versus current phone identity during renewal, and incoming uniqueness versus all writers of the same outbound message. Amend the strict expected-change reason for ConversationsService to admit the necessary internal persistence work while preserving DTOs, window rules and timeline behavior.",
  "operational_fit_position": "Local-first execution, a dedicated pinned Evolution runtime and storage, PostgreSQL 16, Node 22, a single principal-checkout writer, serial destructive suites and served-build attestation fit the declared scope. Meta eligibility/configuration, usable test assets, a real HTTPS callback, actual Evolution payload compatibility and real IN/OUT remain unknown. Their unknown state blocks the corresponding real-proof criterion, not honest planning. No legacy runtime adoption, Railway deployment or source promotion is authorized by this report.",
  "test_quality_position": "The planned PG E2E, real-backend browser lane, adapter/crypto tests, concurrency barriers, negative controls, source freshness and separate external proof are strong. REG-SEC-02 currently allows a duplicate OUT to pass because it requires only that an echo not become IN; REG-SEC-03 does not distinguish initial unverified pairing from renewing a previously verified instance. Add both discriminating sequences below. Existing fakes record only destination/text, so scoped-credential tests must observe the resource and credential identity at the external port without recording the secret. All assertions and results remain planned, not evidence of implemented safety.",
  "resolution_assessment": [
    {
      "finding_id": "NUM-ARCH-01",
      "position": "addressed-in-plan",
      "evidence": "TODO lines 128, 385 and 717; validation-plan REG-SEC-01; packet lines 138, 395, 727 and 4375.",
      "assessment": "The incoming BU is the source of Mantenedora ownership. A candidate trigger requires that tenant's bot plus exact BU or a global trigger inside the same tenant; resumed sessions must match Mantenedora/BU/contact. The competing-global-trigger and foreign-session negative tests directly distinguish the original defect. This is a planned correction of existing code at IncomingService.executarTypebot, not an implemented fix.",
      "remaining_condition": "Exercise the real relational predicate and session ownership with two tenants and distinct adapter credential identities; do not satisfy the test by disabling Typebot. No additional architecture change is requested for this original finding."
    },
    {
      "finding_id": "NUM-ARCH-02",
      "position": "addressed-for-IN-replay; outbound-reconciliation-interaction-needs-revision",
      "evidence": "TODO line 126 and validation-plan REG-SEC-02; packet lines 136 and 4376.",
      "assessment": "A PostgreSQL unique key on verified resource/external message ID, transactional Message plus conversation/unread mutation, rollback on duplicate and effects only from the acceptance winner resolve the original incoming replay failure. Equal IDs across distinct resources and missing-ID handling are explicit. Legacy rows may retain null keys without invented backfill. The accepted postcommit publication/bot crash gap is stated honestly.",
      "remaining_condition": "NUM-CRIT-02 covers the additional promised echo reconciliation. The incoming unique key alone does not reconcile a sender that inserts outside that key."
    },
    {
      "finding_id": "NUM-ARCH-03",
      "position": "addressed-for-initial-pairing; renewal-trust-boundary-needs-revision",
      "evidence": "TODO lines 80 and 124; validation-plan REG-SEC-03; packet lines 90, 134 and 4377.",
      "assessment": "Authentication plus verified own-number identity before content/raw/domain effects, safe 503 before proof, 409 quarantine on mismatch, no reliance on state=open, and fail-closed LID handling address the original initial-pairing disclosure. Rejection without guaranteed replay is an explicit product/runbook limitation rather than a hidden delivery promise.",
      "remaining_condition": "NUM-CRIT-01 requires the same safety after INITIAL/RENEW is invoked on an instance whose previous own-number proof is already valid."
    },
    {
      "finding_id": "NUM-ARCH-04",
      "position": "addressed-in-plan",
      "evidence": "TODO lines 122 and 384; validation-plan REG-SEC-04; packet lines 132, 394 and 4378.",
      "assessment": "ProviderResourceIdentity retains an immutable BU owner after channel removal, prohibits cross-BU reassignment, and admits only same-BU reactivation. The plan explicitly acknowledges that external Meta events carry no local generation. This resolves the temporal tenant-crossover failure without pretending that local CAS identifies an old webhook's origin generation.",
      "remaining_condition": "Migration and deletion must preserve the owner row, and both incoming domain effects and receipt updates must use it. Same-owner delayed input after reactivation remains a residual temporal issue, not cross-tenant attribution proof."
    },
    {
      "finding_id": "NUM-ARCH-05",
      "position": "addressed-in-plan",
      "evidence": "TODO line 80 and validation-plan REG-SEC-05; packet lines 90 and 4379.",
      "assessment": "POST pair reuses current ADMIN and mutation-header enforcement; the former GET returns 405 without a provider call. This removes the mutating GET rather than adding a middleware exception. The test distinguishes authorization failure from provider-side mutation.",
      "remaining_condition": "Keep the no-provider-call assertion on GET, missing-header POST and unauthorized POST. The independently addressed identity-epoch issue does not reopen this HTTP/CSRF resolution."
    },
    {
      "finding_id": "NUM-ARCH-06",
      "position": "addressed-in-plan",
      "evidence": "TODO lines 116 and 118; validation-plan REG-SEC-06/07/09; packet lines 126, 128, 4380, 4381 and 4383.",
      "assessment": "Explicit NOVO versus REAUTORIZAR, occupied-slot reuse with expectedGeneration, a fresh attempt/nonce after consumed or ambiguous code, currentAttemptId, activeCredentialVersion CAS and candidate-to-active re-encryption define a viable recovery/activation path. A valid old credential is preserved until the candidate proves the same resource. Cancel/expiry removes the candidate while preserving the active credential.",
      "remaining_condition": "The eventual activation transaction must enforce current authorization/session validity and the recorded CAS, rather than relying only on a check before provider HTTP. The contract already requires this and planned revocation/race tests should prove it; no additional blocker is raised for this original finding."
    }
  ],
  "blocking_findings": [
    {
      "id": "NUM-CRIT-01",
      "severity": "high",
      "blocking": true,
      "scope_classification": "in-scope lifecycle clarification for SCOPE-04/05/09 and CON-04/REG-SEC-03; no new feature or generic infrastructure",
      "title": "RENEW must invalidate the previous pairing's own-number proof before new input can be accepted",
      "evidence": [
        {
          "path": "foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md",
          "line": 80,
          "packet_line": 90,
          "detail": "INITIAL or RENEW uses the current link/generation, but the pairing action does not specify when an existing verified identity becomes untrusted."
        },
        {
          "path": "foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md",
          "line": 124,
          "packet_line": 134,
          "detail": "The acceptance gate requires persisted verified own-number identity; it does not define a pairing epoch or how old same-instance observations are fenced during RENEW."
        },
        {
          "path": "api-app/src/surfaces/webhooks/evolution.controller.ts",
          "line": 29,
          "packet_line": 2620,
          "detail": "Current code routes solely by instance name; own phone is learned separately from connection.update at source line 94. No provider-carried local pairing generation is shown."
        },
        {
          "path": "foundation_documentation/artifacts/validation-plans/leadshug-channel-readiness-20261015.md",
          "line": 96,
          "packet_line": 4377,
          "detail": "REG-SEC-03 covers input before initial confirmation; it does not start from an already verified channel and then renew pairing."
        }
      ],
      "concrete_failure": "Start with the existing instance verified as phone X for BU X. An administrator requests RENEW and scans its QR with Y. If the new implementation merely adds the proposed persisted-identity check to the current routing, the old X proof remains true while Y's messages.upsert arrives before its connection observation. Y's content can therefore enter BU X. Merely clearing proof and allowing an old connection.update/open/wuid=X on the same instance to restore it leaves the same gap. A request-local lease or current generation captured when handling that old event does not prove which pairing produced it. This is a missing renewal contract, not a claim that the future implementation already behaves this way.",
      "why_now": "Re-pairing/renewal is explicitly promised and tested in this story. The initial identity correction must hold throughout that lifecycle, including the period in which a previous proof already exists.",
      "recommended_correction": "Freeze an explicit pairing trust epoch. Before any INITIAL/RENEW provider side effect, atomically invalidate the previous acceptance proof and fence pending identity/verification observations. Re-enable content only after current-epoch own-number evidence matches the canonical BU phone, with shared compare/fill-by-CAS behavior for an empty BU phone. A same-instance open event or old wuid observation cannot alone restore trust. Specify what positively ties the supported pinned provider's own-number proof to the renewed pairing; if that attribution cannot be established, retain PENDING_IDENTITY or use a generation-specific stable external instance identity and retire the old mapping. Do not present a locally assigned generation on an uncorrelated webhook as external proof. Maintain the chosen safe rejection/no-buffer policy.",
      "required_discriminating_test": "With PostgreSQL and the real auth/domain boundary, begin from an accepted verified X channel, issue RENEW, and hold the external step behind a barrier. Assert proof is invalidated before that side effect. Deliver authenticated content for the new pairing before fresh own-number proof, a delayed old open/wuid=X event and an old verify completion; none may restore acceptance or persist content/raw, increment unread, publish or run a bot. Then prove ownPhone=Y produces quarantine and no effects. Repeat with a fresh matching X proof and replay the same message; exactly one accepted message results. A test that starts with an unverified channel does not discriminate this failure.",
      "options": [
        {
          "option": "A",
          "recommended": true,
          "description": "Add an explicit trust epoch, invalidate it before pairing, and require positively current own-number proof; stay fail-closed when provider attribution is ambiguous.",
          "implementation_effort": "medium; a bounded channels/webhook/adapter state and test clarification",
          "risk": "low after the supported proof source and stale-result rules are fixed; otherwise ambiguity must remain visible",
          "blast_radius": "pairing, identity acceptance and their projections in the existing story",
          "maintenance_burden": "low-to-medium; one explicit identity lifecycle rather than dispersed exceptions",
          "performance_impact": "small indexed/CAS checks; any identity read remains inside the existing bounded provider rounds",
          "elegance_impact": "improves coherence by separating previous trust from a new pairing",
          "structural_soundness_impact": "keeps authentication, external identity proof and local channel generation distinct"
        },
        {
          "option": "B",
          "recommended": false,
          "description": "Use a stable channel-plus-pairing-generation instance name for renewal, retire the old external mapping and validate the new resource before accepting its input. Prefer this if the pinned provider cannot supply adequate current-pairing attribution for A.",
          "implementation_effort": "medium-to-high; additional bounded resource replacement/cleanup states",
          "risk": "stronger event separation, with more operational cleanup and partial-creation cases to manage",
          "blast_radius": "same channel/runtime slice; no cross-BU transfer or generic job platform",
          "maintenance_burden": "medium; stable per-epoch identity, retirement and explicit cleanup must remain idempotent",
          "performance_impact": "extra bounded create/read/cleanup steps, never duplicate creation on retry",
          "elegance_impact": "more state, but justified if it makes external attribution reliable",
          "structural_soundness_impact": "external routing itself distinguishes retired pairing epochs"
        },
        {
          "option": "C",
          "recommended": false,
          "description": "Keep the old verified proof during RENEW or restore it from an uncorrelated same-instance event.",
          "implementation_effort": "low",
          "risk": "high; allows the wrong phone's content to enter a verified BU",
          "blast_radius": "BU conversations, raw content, unread, realtime and automation",
          "maintenance_burden": "high; later conditional patches cannot retract a disclosure",
          "performance_impact": "slightly fewer checks at an unacceptable correctness cost",
          "elegance_impact": "hidden coupling between two different pairing lifecycles",
          "structural_soundness_impact": "fails the declared identity-before-content boundary; do nothing is not reasonable"
        }
      ]
    },
    {
      "id": "NUM-CRIT-02",
      "severity": "medium",
      "blocking": true,
      "scope_classification": "in-scope correction needed to satisfy the newly explicit echo reconciliation contract; preserve public DTOs/windows/timeline",
      "title": "The OUT sender and webhook echo must share the same acceptance key and persistence boundary",
      "evidence": [
        {
          "path": "foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md",
          "line": 126,
          "packet_line": 136,
          "detail": "The plan promises reconciliation of echo OUT with the persisted send by the same resource identity and external ID."
        },
        {
          "path": "foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md",
          "line": 200,
          "packet_line": 210,
          "detail": "The strict expected-change reason permits ConversationsService to change only credential resolution, leaving its independent OUT insertion outside the proposed acceptance key."
        },
        {
          "path": "api-app/src/domain/inbox/conversations.service.ts",
          "line": 201,
          "packet_line": 2070,
          "detail": "Provider send precedes an unconditional message.create at source line 203; it currently stores externalId without a provider resource identity."
        },
        {
          "path": "api-app/src/surfaces/webhooks/evolution.controller.ts",
          "line": 84,
          "packet_line": 2675,
          "detail": "Provider fromMe events enter IncomingService as OUT, which independently creates Message."
        },
        {
          "path": "foundation_documentation/artifacts/validation-plans/leadshug-channel-readiness-20261015.md",
          "line": 95,
          "packet_line": 4376,
          "detail": "REG-SEC-02 asserts echo does not become IN, which does not detect two persisted OUT rows."
        }
      ],
      "concrete_failure": "The existing sender calls Evolution; Evolution delivers an authenticated fromMe echo with external ID E before the send promise resumes. The revised incoming path accepts OUT under resource R/E. The existing sender then inserts another OUT after the provider response. If only credential resolution is changed as permitted, its new resource-key columns remain absent/null and the incoming unique constraint cannot conflict; two timeline entries result. A sequential lookup for a previously persisted send also misses this echo-first ordering. If sender key columns instead become mandatory without reconciliation, the sender fails after a successful provider send. This is an existing send/echo race exposed by the new reconciliation promise, not an alleged implemented regression.",
      "why_now": "The revised plan explicitly adds an identity/message key and promises echo reconciliation while retaining the send path. An internally coherent cutover needs all new writers of that same message identity to participate.",
      "recommended_correction": "Permit the bounded internal OUT-persistence change in ConversationsService and any other actual sender. Resolve the authenticated channel resource identity for a send, populate it on new outbound records, and use one transactional create-or-reconcile path keyed by resource/external message ID for sender results and echoes. Define echo-first, sender-first and duplicate-echo outcomes, including retaining the human/Typebot author and returning the same persisted message to the sender. A unique collision must reconcile the existing message rather than fail a successfully completed send or insert a null-key duplicate. Keep network outside DB transactions, preserve public response/window contracts and do not add external-send retry or exactly-once claims.",
      "required_discriminating_test": "Have the Evolution external-port stub deliver a real authenticated fromMe webhook inside enviarTexto, await its acceptance, and only then resolve the send with the identical external ID. Exercise the BFF and public sender paths that share the service. Assert one physical OUT row with the correct resource key, content and internal author, the returned message identity is that row, no IN/unread effect, and the existing response contract is preserved. Repeat sender-first and concurrently repeated echoes; a different resource using the same external ID remains independent. Add the equivalent check for another sender wherever that provider supports such echoes. Merely asserting direction=OUT is insufficient.",
      "options": [
        {
          "option": "A",
          "recommended": true,
          "description": "Share a narrow keyed outbound acceptance/reconciliation operation between sender-result persistence and webhook ingestion, and amend the strict path reason accordingly.",
          "implementation_effort": "medium; bounded persistence/helper and E2E changes in already touched files",
          "risk": "controlled by echo-first/sender-first barriers and authorship assertions",
          "blast_radius": "internal message persistence and applicable existing sender callers; no public DTO or timeline contract change",
          "maintenance_burden": "low-to-medium; one owner for the message identity",
          "performance_impact": "one indexed upsert/short transaction in place of independent inserts",
          "elegance_impact": "improves coherence and removes query-before-insert and null-key exceptions",
          "structural_soundness_impact": "all writers honor the same domain identity and database constraint"
        },
        {
          "option": "B",
          "recommended": false,
          "description": "Search for an existing send only inside the webhook path or suppress echoes with an in-memory cache while leaving sender persistence unchanged.",
          "implementation_effort": "low initially",
          "risk": "high; echo-first ordering, restarts and multiple processes still produce duplicates or lost external sends",
          "blast_radius": "same messages with additional implicit coupling between transport timing and storage",
          "maintenance_burden": "high; increasingly special-case reconciliation",
          "performance_impact": "extra lookups/cache work without a concurrency guarantee",
          "elegance_impact": "brittle timing workaround",
          "structural_soundness_impact": "does not make the uniqueness contract authoritative across writers"
        },
        {
          "option": "C",
          "recommended": false,
          "description": "Keep only the assertion that echoes are not IN and leave independent OUT inserts.",
          "implementation_effort": "low",
          "risk": "known duplicate OUT or post-send insertion failure under the stated ordering",
          "blast_radius": "conversation history and successful-send responses",
          "maintenance_burden": "high; inaccurate history becomes a permanent ambiguity",
          "performance_impact": "wastes storage/publication on duplicate rows",
          "elegance_impact": "retains two competing acceptance rules",
          "structural_soundness_impact": "contradicts the explicit echo reconciliation promise; do nothing is not reasonable"
        }
      ]
    }
  ],
  "nonblocking_observations": [
    {
      "id": "NUM-OBS-01",
      "severity": "medium",
      "scope_classification": "in-scope execution/test concretization already required by DOD-03 and REG-SEC-08; no new approval blocker or claim of an observed leak",
      "observation": "The current Evolution authenticator puts its secret in /webhooks/evolution/:segredo, while the planned new gateway is Nginx. Scrubbing JSON payloads and application errors does not by itself scrub access/error logs that record request URIs. The packet contains no implemented gateway/log policy to inspect.",
      "evidence": "EvolutionWebhookController lines 12-19 (packet 2603-2610); TODO runtime notes line 556 (packet 566); REG-SEC-08 at packet 4382.",
      "recommended_handling": "When concretizing the gateway, explicitly handle secret-bearing request paths in ingress/proxy/application logs, or use authenticated callback headers only if the pinned provider supports them. Extend the existing secret-negative harness to route a dummy secret through the real gateway and inspect access/error logs and captured artifacts, not just envelope fields. A leak would fail the already declared secret-free delivery criteria."
    },
    {
      "id": "NUM-OBS-02",
      "severity": "medium",
      "scope_classification": "in-scope raw-event ownership/test concretization under the declared identity gate and audit module; not a request for a new raw-event platform",
      "observation": "Meta delivers a body containing multiple entry/change/value resources. The current code stores the whole body before mapping any resource, with no BU. Moving this write after one mapping and redacting secret keys would still be insufficient if the stored payload retained another BU's or an unknown resource's content. The revised identity-before-content and BU-scoping invariants already require the implementation to avoid this.",
      "evidence": "MetaWebhookController lines 37-43 (packet 2473-2479), registrarEventoCru in IncomingService, and audit-and-history invariant at packet 1011.",
      "recommended_handling": "Partition accepted diagnostic payloads by verified resource/BU, or use an equivalently explicit scoped representation. Unknown/retired/unverified portions must contribute only allowed metadata. Add a signed mixed batch for two BUs plus an unknown resource; no raw record may expose a different owner's content and no unverified content may persist. This strengthens enforcement of the existing plan rather than expanding the product story."
    },
    {
      "id": "NUM-OBS-03",
      "severity": "low",
      "scope_classification": "in-scope test-quality implementation requirement already covered by credential/tenant cutover tests",
      "observation": "The current metaFake records only para/texto and the Typebot unit test constructs a mocked Prisma result. Either can pass while a caller uses the wrong credential or the relational tenant predicate is missing.",
      "evidence": "test/helpers.ts line 16 (packet 3636); incoming.typebot.integration.spec.ts in packet lines 4481-4538.",
      "recommended_handling": "Use real PostgreSQL tenant/trigger/session fixtures and observe channel/resource plus a non-secret credential identifier at the external port. Competing tenants should use distinct credentials and bot IDs with the same contact/text, so the expected correct call and the absence of the foreign call are both discriminating. Never put real tokens in assertion output or fixture artifacts."
    }
  ],
  "assumption_vs_current_code": [
    {
      "assumption_id": "A-01",
      "position": "supported",
      "confidence": "high",
      "evidence": [
        "meta.client.ts:31, packet 1237: process.env.WHATSAPP_TOKEN is a client-wide field",
        "meta.client.ts:20-24: callers provide resource/destination/text, without a credential parameter",
        "conversations.service.ts:292, packet 2161; incoming.service.ts:125, packet 2306: both use that port"
      ],
      "qualification": "This establishes the existing global-token defect. The scoped resolver, credential storage and consumer cutover remain proposed."
    },
    {
      "assumption_id": "A-02",
      "position": "supported",
      "confidence": "high",
      "evidence": [
        "channels.service.ts:31-74 in packet 1072-1115: consults numerosDaWaba, takes numeros[0], creates CONECTADO and updates the BU phone"
      ],
      "qualification": "The existing code does not implement Embedded Signup, explicit multiple-number selection, registration/subscription proof or per-channel credential activation. The new plan correctly treats those as new work."
    },
    {
      "assumption_id": "A-03",
      "position": "supported-with-method-and-binding-qualifications",
      "confidence": "high for included middleware behavior",
      "evidence": [
        "session.middleware.ts:70, packet 1559: GET/HEAD/OPTIONS are excluded from mutation checks",
        "session.middleware.ts:80-96, packet 1569-1585: session claims and current user/password state are checked",
        "session.middleware.ts:123 and 136, packet 1612 and 1625: unsafe methods require X-Requested-With"
      ],
      "qualification": "The assumption means unsafe-method CSRF enforcement on routes actually mounted behind this middleware, not CSRF protection for a mutating GET. The POST pairing correction is coherent. New controller binding and revoked-session/grant checks across asynchronous steps still require the planned real-app E2E proof; bff.module wiring is a future changed surface, not implemented evidence in this packet."
    },
    {
      "assumption_id": "A-04",
      "position": "supported-with-bounded-corpus-limit",
      "confidence": "high for UI behavior; medium for the repository-wide negative claim",
      "evidence": [
        "Numeros.tsx:12-19, packet 3322-3329: polls the BFF business-units projection every five seconds without a provider request in the UI",
        "channels.controller.ts:29-35, packet 1414-1420: included channel listing reads Prisma only",
        "evolution.client.ts:66-68, packet 1353-1355: estadoDaInstancia is present; no production caller appears elsewhere in the supplied corpus"
      ],
      "qualification": "The packet does not contain every production source file or the business-units listing implementation. A complete-repository absence of callers is not conclusively proven by this bounded review. The dedicated A-04 coherence pass should record a source-wide read-only caller search on the frozen code; do not mark this critique as that deterministic guard. The proposed DB-only listing contract remains sound even if an additional existing caller is later discovered."
    }
  ],
  "module_coherence": {
    "position": "coherent-target-with-two-local-contract-gaps",
    "constitution_change_required_by_recommended_fixes": false,
    "assessment": "The primary integration owner and secondary identity, inbox and audit owners match the touched boundaries. Tenant isolation, incoming idempotency, channel-window enforcement and the BU/contact conversation key are preserved rather than intentionally superseded. Current short integration/identity modules do not yet define the proposed endpoints; their consolidation before new routes is correctly planned. A stale identity gate or dual OUT writer would fail those existing invariants, so the blockers should be resolved in the same TODO and owner modules. Do not mark any module Verified from this planning report.",
    "decision_mapping": [
      { "decision": "D-01", "modules": ["identity-and-tenancy", "inbox-and-conversations"], "handling": "Preserve", "reason": "BU owns the canonical number; a transport does not create a new tenant or conversation namespace." },
      { "decision": "D-02", "modules": ["integrations-and-channels", "identity-and-tenancy"], "handling": "Preserve and define new explicit contract", "reason": "SDK/provider data remains untrusted until server-side identity and permission proof." },
      { "decision": "D-03", "modules": ["integrations-and-channels", "identity-and-tenancy"], "handling": "Preserve and define lifecycle", "reason": "Persisted attempts and separate activation retain one current context without holding DB transactions over HTTP." },
      { "decision": "D-04", "modules": ["integrations-and-channels", "audit-and-history"], "handling": "Preserve", "reason": "Secrets belong to backend credential storage and never enter domain DTOs, bundles or activity history." },
      { "decision": "D-05", "modules": ["integrations-and-channels"], "handling": "Preserve and define lifecycle", "reason": "Provider steps and partial failure are explicit; foreign callbacks are not taken over." },
      { "decision": "D-06", "modules": ["integrations-and-channels", "identity-and-tenancy"], "handling": "Preserve; clarify renewal per NUM-CRIT-01", "reason": "Authenticated POST pairing and verified own-number ingress need the same safety after every pairing epoch." },
      { "decision": "D-07", "modules": ["integrations-and-channels", "identity-and-tenancy"], "handling": "Preserve", "reason": "Durable immutable resource ownership and honest observation semantics defend tenant attribution." },
      { "decision": "D-08", "modules": ["inbox-and-conversations", "integrations-and-channels", "identity-and-tenancy"], "handling": "Preserve; align all OUT writers per NUM-CRIT-02", "reason": "Tenant-scoped bots/credentials and transactional acceptance implement existing invariants without changing public/timeline behavior." },
      { "decision": "D-09", "modules": ["integrations-and-channels"], "handling": "Preserve", "reason": "Dedicated local runtime and separate real-provider proof do not imply Railway promotion or historical import." },
      { "decision": "D-10", "modules": ["project governance"], "handling": "Preserve", "reason": "Single-writer principal-checkout execution and pipeline-owned gitlinks match the local authority rules." }
    ]
  },
  "residual_risks_and_limits": [
    {
      "scope_classification": "in-scope accepted limitation already explicit",
      "risk": "Safe rejection before Evolution identity verification can lose events if the provider does not retry. The UI/runbook must require confirmed number identity before the test message and permit manual resend; no buffer/import guarantee is inferred."
    },
    {
      "scope_classification": "in-scope accepted postcommit limitation already explicit",
      "risk": "A crash after message commit can omit realtime or automation. Winner-only processing prevents duplicate execution in ordinary replay but does not create a transactional outbox or external exactly-once semantics. Keep the runbook and delivery claims within that stated limit."
    },
    {
      "scope_classification": "external readiness prerequisite, not evidence or a waiver",
      "risk": "Meta app eligibility, actual Graph/version permissions, code-exchange/resource-proof/register/subscribe behavior, callback reachability, test assets and actual pinned Evolution own-number/payload behavior still require primary-provider/runtime confirmation. This packet does not prove them."
    },
    {
      "scope_classification": "in-scope migration/operations condition",
      "risk": "Existing resource collisions must abort with a redacted report. Nullable legacy message keys do not provide retroactive deduplication, and existing channels without credentials remain visibly pending until explicit validated reauthorization. Cipher keys/key IDs must remain available or decryption correctly fails closed."
    },
    {
      "scope_classification": "preexisting behavior outside the bounded incoming duplicate guarantee; follow-up only if stronger bot sequencing is required",
      "risk": "Distinct simultaneous accepted messages can still contend for Typebot session startup/continuation in the existing implementation. Deduplicating the same external message does not establish ordered or exactly-once bot conversations. No such broader guarantee should be inferred from REG-SEC-02 or introduced through an unapproved worker framework."
    },
    {
      "scope_classification": "security/operational limit",
      "risk": "Encrypted DB credentials do not protect against a compromised running application or installation key. Local correctness and small synthetic concurrency trials do not establish production availability, throughput or continuous token health."
    },
    {
      "scope_classification": "explicitly excluded future product work",
      "risk": "ST-CON-04 proactive conversation creation/templates, historical import/coexistence/migration, binary media, status lifecycle and Railway promotion remain outside this review's implementation recommendation."
    }
  ],
  "required_next_review_actions": [
    "Resolve NUM-CRIT-01 and NUM-CRIT-02 in the governing TODO, validation plan, strict expected-change reasons and relevant module-consolidation targets; classify each resolution explicitly.",
    "Refresh the immutable pushed planning baseline if the material identity/persistence direction changes, and rerun the affected independent review/critique lanes before requesting approval.",
    "After planning convergence, run the dedicated assumption-code coherence, post-review scope-drift and execution-readiness preflight guards; this report does not substitute for them.",
    "Request APROVADO only after the required planning gates converge. Implementation, provider calls, architecture adherence, TQA, security/PCV/debt and final delivery review remain later authorized work."
  ]
}


## FILE foundation_documentation/artifacts/validation-plans/leadshug-channel-readiness-20261015.md

# Plano de validação — conexões e histórico dos canais

**Data:** 2026-10-15
**Estado:** planejamento; nenhum cenário abaixo foi executado nesta frente.
**Contrato candidato:** [ST-CON-01 draft](../../todos/active/features/TODO-leadshug-channel-connection-readiness.md).
**Enquadramento:** [conexões e histórico](../feature-briefs/leadshug-channel-readiness-and-history-20261015.md).

## Sequência de ambientes

Usuário confirmou em2026-10-15: **local primeiro**, Railway de testes depois. O primeiro ciclo valida o backend local com providers/números de teste reais. Railway não é dependência de conclusão deste ciclo e exigirá readiness/evidência próprias antes de qualquer promoção.

Inspeção de leitura: Docker Engine acessível via cliente Windows; socket Linux indisponível nesta sessão. Containers do Compose LeadsHug existentes estavam parados. O Compose não declara Evolution nem repassa as variáveis de webhook/instância à API. A existência de uma Evolution no legado não fornece runtime autorizado para este teste. Nada foi iniciado ou alterado.

## Preparação do ambiente

1. Preparar ambiente local próprio do LeadsHug: fixar versão/build da Evolution, persistência/sessão e dono de execução; completar Compose/wiring e configuração privada em contrato antes da implementação. Não derivar o target do ambiente legado.
2. Identificar BU, canal, número oficial selecionado e instância de teste, com permissão do operador. Não publicar telefones completos, QR, payloads pessoais ou credenciais nos artefatos.
3. Configurar credenciais no mecanismo privado do ambiente; registrar apenas presença/ausência, permissões e resultados redigidos. Credencial presente não significa válida.
4. Definir endereço de callback alcançável pelos providers para o backend local e autenticação de origem; selecionar o mecanismo de exposição no contrato, sem presumir domínio ou abrir túnel agora. Webhook forjado deve ser recusado; endpoint responder200 a probe artificial não prova que o provider consegue alcançá-lo.
5. Confirmar interlocutor/segundo aparelho de teste. Identificar quais vínculos são descartáveis antes de interrupção/repareamento; não remover instância em uso.
6. Registrar branch@SHA API/Web, bundle servido e target redigido; fonte/build devem ser atuais antes do Playwright. Sessão, grants, PostgreSQL e WebSocket continuam reais no harness.

Dependências desconhecidas permanecem no [registro](../dependency-readiness.md). Uma oferta de número ainda não é prova de acesso ao provider.

## Matriz de prova de cadastro e conexão — ST-CON-01

| ID | Cenário | Resultado necessário | Evidência planejada |
| --- | --- | --- | --- |
| CAD-01 | Iniciar cadastro oficial, autorizar/cancelar na Meta e receber callback | Vínculo correlacionado com sessão/BU, código trocado somente no backend e credenciais scoped; sem sucesso em cancelamento/erro. | Contratos de OAuth/adapter, browser e autorização real separada. |
| CAD-02 | Iniciar cadastro não oficial por apelido e ler QR | Instância própria e vínculo corretos, número confirmado e conclusão visível; QR usado removido. | Browser/backend real e aparelho de teste. |
| CON-01 | WABA sem número, com um e com múltiplos | Erro explícito quando vazia; vínculo ao número escolhido; nunca escolher silenciosamente o primeiro quando há ambiguidade. | Contrato adapter/BFF e Playwright com readback da BU. |
| CON-02 | Credencial inválida, expirada ou sem permissão | Mostrar falha de verificação sem expor segredo ou converter ausência de prova em CONECTADO. | Negativas por canal + amostra real permitida. |
| CON-03 | Evolution cria instância e QR é lido | Transição compatível com estado real do provider e telefone confirmado; tela não fica exibindo QR como se ainda estivesse pendente após conclusão. | Browser + estado observado + mensagem real. |
| CON-04 | QR expirado/novo e repareamento | Renovação visível; resultado antigo não altera vínculo novo. | Browser/harness de concorrência e aparelho de teste. |
| CON-05 | Provider indisponível/timeout/payload inválido | Verificação falha de forma limitada e permite retry; momento da última observação continua explícito. | Adapter e E2E com contador de chamadas/tempo. |
| CON-06 | Vários cliques/poll/usuários | Orçamento e concorrência definidos; listar não gera consultas externas por BU em cada poll. | Readback e contagem/in-flight de consultas. |
| CON-07 | Evento mais novo enquanto consulta velha está pendente | Resposta velha não regrede estado; ordenação e origem da observação são testadas conforme regra congelada. | Barrier determinístico + controle negativo. |
| CON-08 | Remover/recriar canal durante consulta | Consulta antiga não escreve no vínculo novo e não o reativa. | Teste de geração/identidade com PostgreSQL real. |
| CON-09 | Atendente sem poder administrativo e usuário de outro tenant | Negação scoped; nenhuma consulta externa ou escrita não autorizada. | E2E + contador de adapter e readback. |
| CON-10 | Mensagem IN de interlocutor real | Callback autenticado, BU/contato corretos, uma mensagem visível e persistida; carimbo de build/provider/canal. | Observação provider → webhook → banco → inbox. |
| CON-11 | Resposta OUT pela inbox | Identificador externo e recebimento no interlocutor; estado de janela oficial respeitado. | Inbox → provider → aparelho e readback; aceite HTTP isolado não basta. |
| CON-12 | Interrupção e retomada permitidas | Estado honesto durante interrupção e recuperação comprovada por nova IN/OUT. | Checklist por canal; diferenciar reconexão de socket do navegador. |

O teste CON-03 é específico do não oficial; no oficial usar o onboarding admitido, sem inventar QR de dispositivo. CON-12 não exige derrubar produção ou revogar credencial real: procedimento será limitado ao target de teste e às ações admitidas no contrato.

## Provas futuras de histórico — ST-CON-02/03

Estes cenários orientam contratos futuros; não ampliam o ST-CON-01.

| ID | Cenário | Resultado necessário |
| --- | --- | --- |
| HIS-01 | Carga inicial oferecida pelo provider | Quantidade, período e limitações visíveis; não anunciar todo o aparelho quando só há subconjunto disponível. |
| HIS-02 | Mesmo lote reapresentado e evento simultâneo | Identidade scoped e idempotência atômica; não duplicar a mensagem já persistida por envio/webhook. |
| HIS-03 | Datas antigas/empatadas e mensagens OUT | Preservar timestamp externo e direção; ordenação determinística e proveniência separadas da data de ingestão. |
| HIS-04 | Importação durante atendimento e bot ativo | Não incrementar não lidas, reabrir conversa, responder bot ou estender janela oficial por ingestão de mensagem antiga. |
| HIS-05 | Interrupção no meio e retry | Checkpoint persistente e retomada bounded; falha/progresso explícitos; não reiniciar tudo silenciosamente. |
| HIS-06 | Evento novo durante backfill e mensagens antigas inseridas | Cobertura e política de invalidação da timeline explicitamente definidas. ST-ATT-01 excluiu backdating fora da fronteira; importação exigirá novo contrato nessa fronteira. |
| HIS-07 | Dados de outra BU/canal/tenant ou payload sem ID | Recusar vazamento; regra de identidade/fallback decidida antes de persistir. |
| HIS-08 | Oficial sem capacidade/eligibilidade comprovada | Mostrar indisponível ou pendente; não prometer histórico e não importar usando mecanismo do não oficial. |

## Registro de resultados por canal

O resultado deve distinguir: configuração/identidade, conexão observada com horário, IN comprovada, OUT comprovada, recuperação comprovada, histórico disponível/importado e limitações. Falha em uma dimensão não deve ser escondida por sucesso em outra.

Para cada execução, registrar cenário, target redigido, canal, versão do provider, branch/build, precondição, resultado, IDs técnicos redigidos, horário e evidência. Nunca usar resultado do harness com provider substituído como prova real.

## Critério de encerramento

O TODO governante define o limiar final. Para a proposta ST-CON-01, exigir matriz local aceita e troca real por cada canal disponibilizado. Se não houver acesso, registrar pendência explícita; não substituir por falso sucesso, dispensa implícita ou alegação de produção pronta.

## Próximo recorte confirmado — Nova conversa pelo contato (ST-CON-04)

O usuário confirmou que também quer iniciar conversas informando o contato. Estes sinais são candidatos do contrato seguinte, após o cadastro de números; não entram por antecipação no ST-CON-01.

| ID | Jornada | Sinal de aceitação candidato |
| --- | --- | --- |
| CONV-01 | Selecionar BU e informar telefone | Validar país/telefone e normalizar identidade sem criar variante do mesmo contato por formatação. |
| CONV-02 | Abrir conversa já existente | Reutilizar conversa BU/contato e histórico, sem duplicar thread ou apagar responsável/estado. |
| CONV-03 | Contato novo | Criar a conversa scoped e mostrar o destino antes do primeiro envio; não criar entidade CRM implicitamente. |
| CONV-04 | Duplo clique e mensagem chegando por webhook ao mesmo tempo | Um único par BU/contato e resultado consistente; nenhum envio duplicado por replay da UI. |
| CONV-05 | Primeiro envio não oficial | Canal conectado e credencial corretos; erro/aceite e recebimento real observáveis. |
| CONV-06 | Oficial dentro da janela | Texto livre somente quando janela e permissão de envio permitem. |
| CONV-07 | Oficial fora da janela | Usar template já aprovado pela Meta, com idioma/parâmetros validados; texto livre não é enviado. Gestão/submissão de templates e campanhas não são presumidas. |
| CONV-08 | Sem canal, sem grant, outro tenant ou contato inválido | Erro explícito; não criar thread ou chamar provider sem autorização. |
| CONV-09 | Trocar BU/destino com criação/envio pendente | Resposta antiga não abre conversa ou limpa texto do destino novo. |
| CONV-10 | Nova conversa por contato vs histórico importado | São ações distintas; abrir contato não importa conversas do aparelho. |

## Cadastro: regressões da revisão de arquitetura (VAL-08)

Casos planejados, nenhum executado. Fixtures de dois tenants e recursos distintos; PostgreSQL real e barreiras para disputas. Provider stub só na porta externa; prova de aparelho separada.

| Caso | Cenário / expectativa obrigatória |
| --- | --- |
| REG-SEC-01 | Dois tenants com triggers globais concorrentes: IN A só escolhe bot/credencial A; nenhuma sessão/texto/saída B. Sessão estrangeira falha antes do HTTP externo. |
| REG-SEC-02 | Replay sequencial e dez duplicatas concorrentes x3 por Meta/Evolution: uma Message, um unread e uma ação downstream; controle negativo com mesmo externalMessageId em dois recursos aceita ambos. Sem ID rejeita; echo OUT não vira IN; echo e sender reconciliam a mesma linha conforme REG-SEC-11. |
| REG-SEC-03 | Mensagem Evolution antes da confirmação do número retorna503 e não persiste conteúdo/raw, Message, unread, realtime ou bot; ownPhone divergente409 mantém quarentena. Número correto permite retry idempotente; sem promessa de replay. LID sem telefone comprovado rejeita. |
| REG-SEC-04 | Evento Meta criado sob recurso de A; remover vínculo preserva owner; tentar vincular mesmo recurso a B retorna409; evento tardio não afeta B/receipt/bot. Reativar somente mesma BU. |
| REG-SEC-05 | GET QR não chama provider; POST pair sem anti-CSRF rejeita antes da chamada; ADMIN com header válido usa lease/generation e budget. |
| REG-SEC-06 | Canal migrado sem credencial reautoriza no slot ocupado, sem WHATSAPP_TOKEN; troca ambígua/consumida exige tentativa e nonce novos; reserva sem efeito expirada pode ser retomada sem nova BU. |
| REG-SEC-07 | Candidata para outro número/cancelada/expirada ou geração anterior nunca substitui ativa válida; duas candidatas concorrentes só currentAttemptId pode promover por CAS; owner/readiness confirmados antes da ativação. |
| REG-SEC-08 | Envelope Evolution com apikey/token/URL secreta fictícios e QR/code/PIN: segredo ausente em raw DB, audit, erro, DTO, log, trace e artefatos. Pré-identidade persiste apenas metadados seguros. |
| REG-SEC-09 | Code/PIN transitórios saem do formulário apenas via BFF HTTPS; não há browser storage/URL/retorno/trace; cifra candidata e ativa rejeitam tamper, purpose/BU/attempt/version incorretos e keyId ausente. |

Limitação explícita: vencedor publica realtime/aciona bot após commit; crash nessa janela pode deixar efeito ausente. Não é claim exactly-once externo nem autorização para replay automático de automação. Esse risco constará do runbook de validação.

## Resoluções da crítica independente — casos discriminantes adicionais

| Caso | Cenário / expectativa obrigatória |
| --- | --- |
| REG-SEC-10 | Começar com canal Evolution comprovado X, executar RENEW com barrier no HTTP: proof invalidada antes da chamada. Nova instância tem nome channelId+epoch; retries reutilizam essa instância. Mensagem da nova rodada antes da prova, open/wuid=X antigo e conclusão de verify antigo não restauram aceitação nem persistem conteúdo/raw/unread/realtime/bot. Identidade nova Y fica em quarentena; consulta nova da instância atual com X permite replay aceito uma vez. Não satisfazer com fixture inicialmente não verificada. |
| REG-SEC-11 | Stub Evolution entrega webhook autenticado fromMe DENTRO de enviarTexto e só depois retorna o mesmo externalId. BFF e público retornam o mesmo Message.id e só uma OUT física scoped ao recurso, com conteúdo/autoria humana correta, zero IN/unread/bot. Repetir sender-first e ecos concorrentes; recurso distinto com mesmo ID é independente. Typebot usa o mesmo owner para gravar OUT/autoria, com sequência equivalente quando esse provider emite echo. Checar identificador não secreto da credencial/recurso na porta externa e triggers/sessões reais no PostgreSQL; mocks sem predicado não bastam. |
| REG-SEC-12 | Segredo Evolution fictício na URL atravessa o gateway real: access/error/application logs e artefatos não contêm path/query/token. Exercitar request válido e erro. Requisito de segredo já declarado, não claim de teste executado. |
| REG-SEC-13 | Meta batch assinado contém recursos de duas BUs e recurso desconhecido/retirado. Cada raw record só tem fragmentos do owner verificado; partes não verificadas só metadados. Nenhum conteúdo cru global ou de outro tenant; assinatura original validada antes da partição. |

Não há garantia de sequenciamento para mensagens distintas simultâneas no Typebot; o contrato de replay diz respeito à mesma mensagem externa. Nenhum worker/fila/retry de envio é autorizado por estes testes.


## FILE foundation_documentation/modules/integrations-and-channels.md

# Module: Integrations and Channels
**Version:** 1.0

Owns Meta Cloud API, Evolution/Baileys, outbound webhooks, API keys and transport adapters.

## Invariants

- Providers are adapters; business workflows do not depend on provider payload shape.
- Secrets never enter logs, docs, fixtures or client bundles.
- Provider failures become deterministic application errors.


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


## FILE foundation_documentation/modules/audit-and-history.md

# Module: Audit and History
**Version:** 1.0

Owns durable activity history, message auditability, exports and access to historical relationship data.

## Invariants

- History is append-oriented and is not silently discarded.
- Every record is tenant- and BU-scoped.
- Read permission is evaluated independently from write permission.


## FILE foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/manual-code-assumptions.json

{
  "scope": "manual current-source anchoring prepared during independent critique; gate not declared complete",
  "checks": [
    {
      "id": "A-01",
      "source": "api-app/src/integrations/meta/meta.client.ts",
      "sha256": "fefdd6fe1152b8dc61b39da5037984b3f48f1c1bd43ed416e067ba9fee433672",
      "needle": "private readonly token = process.env.WHATSAPP_TOKEN",
      "position": "confirmed in unchanged current source; proposed correction does not assert already implemented"
    },
    {
      "id": "A-02",
      "source": "api-app/src/domain/channels/channels.service.ts",
      "sha256": "c81b8e627b0c0abed13ad7559b1799f86e6e8abeb0780082b5de6762671c8986",
      "needle": "const numero = numeros[0]",
      "position": "confirmed in unchanged current source; proposed correction does not assert already implemented"
    },
    {
      "id": "A-03",
      "source": "api-app/src/surfaces/bff/session.middleware.ts",
      "sha256": "80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211",
      "needle": "exigirCabecalhoAntiCsrf",
      "position": "confirmed in unchanged current source; proposed correction does not assert already implemented"
    },
    {
      "id": "A-04",
      "source": "web-app/src/telas/Numeros.tsx",
      "sha256": "428348ea39eeb065d46e1aaea31821e8e242918b900096410fa2b322553f228d",
      "needle": "'/business-units'",
      "position": "confirmed in unchanged current source; proposed correction does not assert already implemented"
    }
  ],
  "caveat": "A-03 CSRF applies only mutating HTTP verbs; NUM-ARCH-05 moves pairing side effect to POST. A-04 connectionState method exists in adapter but no current caller."
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

