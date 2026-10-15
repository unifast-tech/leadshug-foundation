# TODO LeadsHug — cadastro e conexão dos números oficiais e não oficiais

## Quick Start

Contrato proposto ST-CON-01, baseado no template canônico. Usuário autorizou avançar no planejamento do cadastro de números e conversas; Nova conversa informando contato é o próximo ST-CON-04. APROVADO pelo usuário em2026-10-15 para o contrato publicado em3302964c; implementação em andamento e prova externa pendente. Proposta publicada e revisada: arquitetura e crítica convergidas, sem prova externa ou entrega reivindicada.

## Title

Cadastro e conexão dos números oficiais e não oficiais do LeadsHug, inspirado nas jornadas Central-Whatsapp e WhatsFlow.

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Tactical state:** `In-Progress`
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
- **Next exact step:** concluir remediação Web e parar esse writer; então executor API corrige NUM-API-01..18 e fortalece harness/fixtures, antes da integração browser e runtime DevOps serializados.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** implementation
- **Why this state now:** APROVADO explícito nesta sessão; regras recarregadas e preparação da execução autorizada.
- **Exit condition:** implementação no escopo, matriz local/provas reais e gates de entrega aceitos.

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

Proposta técnica revisada, subordinada ao Scope/DoD; parecer de arquitetura e críticas brutos preservados; resoluções aceitas na crítica delta independente.

### BFF e autorização

- `GET /api/bff/number-registrations/capabilities`: sessão válida; expõe apenas appId/configId/Graph version e disponibilidade/explicação por modalidade, nunca app secret/token/chave. Não chama provider.
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

## Delivery Status Semantics

`Pending` até implementação e evidência; `Local-Implemented` exige matriz local aceita. Prova externa é registrada separadamente. `Production-Ready` e deploy não são limiares desta proposta.

## Active Work State Semantics

`review` neste contrato significa revisão do planejamento; não é afirmação de implementação concluída. `implementation` somente após aprovação e authority guard go.

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
| api | test/realtime.e2e-spec.ts | M | Apenas fixture de canal verificado scoped pelo helper comum; preservar asserts de socket/grant/tenant. Admissão de execução documentada abaixo. |
| api | test/modulos.e2e-spec.ts | M | Expectativas do endpoint aposentado e positivas equivalentes na nova jornada; preservar piso oficial e teto/contratação não oficial. Admissão de execução documentada abaixo. |
| api | test/api-publica.e2e-spec.ts | M | Credencial e echo-first/sender-first no envio público; contrato preservado. |
| api | test/atendimento.e2e-spec.ts | M | Credencial, echo-first/sender-first e autoria/ID reconciliados; demais invariantes preservados. |
| api | test/typebot.e2e-spec.ts | A,?? | Credenciais e negativos de isolamento; comportamento dentro do tenant preservado. |
| api | .env.example | M | Novas variáveis sem valores reais. |
| web | src/telas/Numeros.tsx | M | Wizard de cadastro. |
| web | src/api.ts | M | Contratos/projeções e idempotency header. |
| web | src/api.spec.ts | M | Teste existente do contrato de request header/body/URL de postWithHeaders; sem alterar expectativas anteriores. Admissão necessária de execução descrita abaixo. |
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

Três admissões de testes em execução estão detalhadas abaixo. Classificação de gitlinks preexistentes no workspace não concede permissão de alterá-los manualmente. Outras fixtures encontradas necessárias devem ser admitidas antes de editadas; não modificar expectativas de negócio só para passar tests.

- `test/realtime.e2e-spec.ts`: guard de execução encontrou path não classificado. Diff inspecionado pelo orquestrador: somente import do helper `criarCanalVerificado` e substituição da criação direta de BuChannel pela fixture completa de identidade/credencial; nenhum assert, cenário ou comportamento de socket alterado. Necessário para preservar a prova de push scoped após o ingresso passar a exigir identidade durável. Classificação: concretização de fixture da validação SCOPE-07/09 já autorizada, sem nova capacidade, objetivo ou risco material. Admitido esse path exato, sem abrir `test/**`; nenhuma dispensa do guard. A edição precedeu a admissão, falha de sequência registrada e corrigida antes de qualquer entrega; executor instruído a consultar antes de novos paths.
- `test/modulos.e2e-spec.ts`: novo guard encontrou expectativa201→409 em duas chamadas do endpoint aposentado. A constituição exige atualização correspondente de testes de contrato na mesma entrega; esse path é concretização da validação já aprovada, sem ampliar capacidade ou superfície de produto. Admitido o path exato para aposentadoria E provas positivas na nova jornada. A alteração atual não é suficiente como prova positiva de módulo/piso: nomes ainda alegam conexão mas só409 não a exercita; achado de qualidade aberto para correção após a revisão congelada. As negativas404 de teto/contratação devem ser preservadas. Segunda falha de sequência registrada; não concede `test/**` nem dispensa gates.
- `web/src/api.spec.ts` (path interno Web `src/api.spec.ts`): guard intermediário encontrou path não listado que o handoff do root havia chamado incorretamente de admitido. Diff inspecionado: somente acréscimo de13linhas testando header Idempotency-Key, URL sem correlação e body do novo helper; nenhum assert anterior alterado. Classificação: teste de contrato necessário ao helper já aprovado em src/api.ts, sem nova capacidade/risco/escopo de produto, alinhado à constituição. Admitido esse path exato; falha de sequência de conferência do root registrada, sem abrir outros testes. Web já está parada; pacote de review congelado permanece imutável. Não usar o verde unitário para substituir browser. Guard deve voltar go antes de entrega.

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
| SCOPE-09 | Scope | Reautorização, identidade, dedupe e tenant | integration+race | REG-SEC-01..13; VAL-08 | PG16 isolado | planned | Resolução contratual dos achados; produto não implementado. |
| DOD-08 | Definition of Done | Harness de arquitetura/crítica e segredo raw | test+audit | VAL-08 + security/TQA | local | planned | Nenhuma execução reivindicada. |
| VAL-08 | Validation Steps | Regressões de identidade/tenant/credential | integration+race | REG-SEC-01..13 | Node22/PG16 | planned | Sem provas antecipadas. |

## External Dependency Readiness (Required When External Systems Matter)

Register: `foundation_documentation/artifacts/dependency-readiness.md`.

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Evolution de teste e versão | Endpoint/payload/sessão reais. | unknown | n/a | Target inicial local confirmado; instância própria ainda não operante; v2.3.7 por digest definida, payload/saúde ainda não comprovados. | Não usar instância legada observada no inventário Docker. |
| Meta/WABA de teste | Identidade e operação oficial. | unknown | n/a | Permissões, modalidade, número e callback. | Disponibilidade oferecida não é health check. |
| Números/interlocutores de teste | Prova IN/OUT. | unknown | n/a | Usuário confirmou disponibilidade dos dois em2026-10-15. | Confirmar target/destinatário sem publicar números pessoais. |
| Documentação oficial Meta | Cadastro/registro/assinatura. | degraded | 2026-10-15 | Coleção primária Meta Postman acessível; developers direto limitado. | Elegibilidade/app/Graph version ainda dependem de readiness; histórico fora do recorte. |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Current profile:** operational-coder, execução aprovada; Genesis descartado pelo canon/produto existentes.
- **Primary execution profile:** operational-coder; handoff operational-devops antes de runtime/ingress.
- **Active technical scope:** nestjs, react, postgresql, prisma, docker
- **Expected supporting profiles:** operational-devops para target/callback; assurance-tester-quality e assurance-security-adversarial para gates aplicáveis.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log (Update when execution crosses profile boundaries)

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | Implementar somente contrato aprovado. | API/Web/canon owner | active; API remedia NUM-API-01..18 após checkpoint4 Web parado; routing-api-remediation go. |
| operational-coder | assurance-security-adversarial | Revisar correção/segurança/aderência da API antes da integração do consumidor. | Pacote API congelado e relatório, somente leitura de produto | completed-diagnostic; api-checkpoint-review-v1.json terminal,18 achados aceitos abertos; não equivale ao gate final. |
| operational-coder | assurance-tester-quality | Diagnosticar UI corrigida antes de integração browser. | Pacote Web imutável, relatório somente | completed-diagnostic; web-checkpoint-review-v1.json terminal,12achados adjudicados; pacote17snapshots SHA256df4bb1403d1b5e64d30685d33ca48eb3f9204d8d8bb26feae9e41f29274a8b50; não substitui TQA/gates finais. |
| operational-coder | operational-devops | Configurar e provar callback/target de teste se necessário. | Compose local/variáveis/callback e instância própria | preflight read-only delegado após checkpoints2/3; runtime-handoff.md governa paths e isolamento. Nenhuma edição/startup antes do stop do writer Web e handoff explícito do root. |

## Complexity

- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section: segurança/schema, fluxo providers, UI/integração, prova externa/closeout.
- **Why this level:** onboarding OAuth, credencial por cliente, dois providers, infra local, schema, autorização e concorrência. Uma jornada primária de cadastro; Nova conversa é história separada.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:** `foundation_documentation/modules/identity-and-tenancy.md`, `foundation_documentation/modules/inbox-and-conversations.md`, `foundation_documentation/modules/audit-and-history.md`.
- **Planned decision promotion targets:** integrations-and-channels: Cadastro de números, Credenciais por canal, Estados e contratos BFF, Callback e operação local; identity-and-tenancy: autorização das rotas de cadastro; inbox-and-conversations: deduplicação/identidade e isolamento da automação; audit-and-history: eventos sem segredos.
- **Module decision consolidation targets:** as mesmas seções antes do código das novas rotas; estado Verified apenas após validação. Constituição preservada; não reescrever decisões históricas/estudos concluídos.

## Decision Pending (Resolve Before Freeze)

Nenhuma decisão de produto pendente para a proposta revisada e aceita nas críticas. Credenciais, App/config ID, elegibilidade Meta, número de teste e origem HTTPS são precondições operacionais antes da prova externa; não se presume saúde. O desenho abaixo foi desafiado no architecture_opinion e nas críticas; revisões e resoluções estão registradas.

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

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| integrations-and-channels#invariants | Providers são adapters; segredos protegidos; erros determinísticos. | Preserve | módulo owner |
| project_constitution#system-invariants | BU/número e grants isolam operação; conversa unificada BU/contato. | Preserve | constituição |
| inbox-and-conversations#contrato-aprovado-da-timeline-da-inbox | Histórico paginado usa dado persistido, contexto e leitura protegidos. | Preserve; complementar aceitação idempotente/tenant sem alterar timeline | ST-ATT-01 concluído; NUM-ARCH-01/02 |

## Decision Baseline (Frozen Before Implementation)

Baseline aprovada D-01..D-10 pelo APROVADO de2026-10-15 (contrato3302964c): NUM-ARCH-01..06, NUM-CRIT-01/02 e requisitos de execução NUM-OBS-01..03 integrados nos contratos acima, escopo, paths e critérios. Congelamento renovado antes da crítica independente; mesma jornada de cadastro. Aprovação registrada na seção Approval; esta baseline não afirma produto implementado.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability:** required
- **Why this applies:** estabelece onboarding e credencial por canal, retirando acoplamento de cliente em token global e estado conectado por simples consulta.
- **Deviation / debt being retired:** MetaHttpClient lê WHATSAPP_TOKEN global para todas as BUs; bootstrap exige token antes de cadastrar; cadastro oficial escolhe primeiro número e marca conectado; webhook não oficial só atualiza estado sem reconciliação.
- **Target steady-state after closeout:** uma jornada de cadastro por BU com credencial própria, etapas verificáveis, erro parcial durável, candidatos isolados, identidade externa durável e consumidores/entrada isolados e idempotentes.
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
| test | ingresso/reauth/CSRF | REG-SEC-01..13 | Duplicação, Typebot estrangeiro, identidade prematura, reatribuição e promoção candidata indevida. | implement-in-this-todo | DOD-08; VAL-08 |
| runtime | local deployment | compose config, migrate deploy e prova providers | Configuração válida apenas em fake. | implement-in-this-todo | DOD-04/05; VAL-04/05 |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** findings_integrated
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-number-onboarding-20261015/planning-architecture.json, pacote v1 imutável; seis bloqueadores integrados no contrato e ledger, crítica independente delta v3 confirmou a resolução contratual, sem produto implementado. Nenhuma correção de produto reivindicada.
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
- **Baseline commit:** 87c28c6b0f767edde5edf30d4143844f0acd5c2a
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** proposta revisada publicada em main e origin/main após integrar arquitetura e crítica; baseline 87c28c6b para revisão delta, ae503c7b preservada como revisão v1. Este recibo só atualiza metadados.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/README.md
- **Waiver authority / reference:** n/a

## Gate: Review Scope Drift

- **Gate decision:** required
- **Why this decision:** fechar material scope após integração de reviews.
- **Trigger stage:** after planning convergence and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md
- **Gate status:** no_material_findings
- **Findings summary:** Baseline publicada 87c28c6b sem mudança material; cláusulas técnicas adicionais comparadas separadamente. Notas baixas concretizam harness existente.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/evidence/scope-drift.json
- **Waiver authority / reference:** n/a
- **No-go handling rule:** reconvergir/refazer freeze e reviews afetados; não implementar direção materialmente alterada sem aprovação.

## Questions To Close

- [x] Local primeiro; Railway depois.
- [x] Usuário já possui portfólio empresarial Meta e acesso de administrador; confirmação nesta sessão, sem prova antecipada de elegibilidade do app/WABA.
- [x] Usuário acessou painel desenvolvedor e criou aplicativo com caso de uso WhatsApp; produto disponível. Configuração Embedded Signup, WABA e operação continuam não verificadas.
- [x] Reproduzir jornadas de cadastro oficial Meta e não oficial QR.
- [x] Usuário também quer Nova conversa proativa por contato: próximo ST-CON-04, antes de importação.
- [ ] Precondições da prova real: app Meta/configId/versão Graph suportada e elegibilidade, número/WABA, credenciais privadas, origem HTTPS e interlocutor de teste. Não impedem preparar código/contrato; impedem declarar prova real enquanto ausentes.
- [ ] Reviews/guardas e APROVADO deste contrato antes de executar produto.

## Pattern References (Optional; Enforced When Cited)

`pending-freeze`: seção reservada para a fase aplicável. Nenhum review, guard, aprovação, medição, dispensa ou evidência de entrega foi executado/concedido neste draft; preencher antes do gate correspondente.

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

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

Parecer architecture_opinion concluído e crítica completa v2 revise; resolução dos dois achados integrada e aceita na crítica delta independente, sem bloqueadores. Produto não alterado.

### Review Sections

- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

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

Parecer independente architecture_opinion gpt-6.1-sol/max, fresh no-context, concluído em planning-architecture.json sobre pacote v1 SHA25600bfa0389bd8c204a08c890db746923deaba79161b9bebde11d45478509de177. Veredito revise; preserva arquitetura de tentativas/cifra scoped e identifica seis bloqueadores. Todos foram integrados na proposta, com correções e testes explícitos; crítica v2 e delta v3 verificaram a resolução e o plano, com aceite contratual final. Não significa correção de produto ou conclusão de delivery audit.

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-number-onboarding-20261015/evidence/audit-floor-v2.json (go; fingerprint fa884bf1d2e7).

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
- **Critique status:** findings_integrated
- **Findings summary:** crítica v2 revise com dois bloqueadores integrados; delta v3 approve, zero bloqueadores e três notas do harness já exigido, registradas.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/planning-critique.json; planning-critique-delta.json e evidence/critique-v3-merged.json
- **Waiver authority / reference:** n/a

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| NUM-CRIT-01 | Integrated | useful | partial | project | none | Contrato de epoch/instância, D-06, REG-SEC-10; delta v3 confirma resolução contratual, produto ainda não verificado. |
| NUM-CRIT-02 | Integrated | useful | partial | project | none | Aceitação keyed de todos os writers OUT, D-08, diff helper, REG-SEC-11. |

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** as alterações dependem de consumers e superfícies reais.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01,A-02,A-03,A-04
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md
- **Gate status:** no_material_findings
- **Findings summary:** A-01..04 verificadas na fonte corrente; críticas e source-wide caller search registrados. Guard verifica anchors e não substitui leitura semântica.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015/evidence/code-coherence.json
- **Waiver authority / reference:** n/a

## Planning Readiness Summary

- architecture_opinion v1: seis achados integrados no contrato, confirmados pela crítica e delta; nenhuma correção de produto reivindicada.
- critique v2 + delta v3: approve no planejamento, zero bloqueadores restantes; oito resoluções e seis notas de execução concretizadas no ledger/plano de validação.
- Assumption code coherence: go, quatro premissas; evidence/code-coherence.json e connection-state-caller-search.json.
- Review scope drift: go,23seções e zero mudanças materiais contra baseline publicada87c28c6b; cláusulas técnicas adicionais também conferidas.
- Authority preflight: preflight-go, execution_authority_granted=false; artifacts/reviews/leadshug-number-onboarding-20261015/evidence/authority-preapproval.json.
- APROVADO explícito recebido em2026-10-15 para este contrato. A implementação está autorizada após authority guard de execução go; provas e gates de entrega continuam pendentes.

## Approval

- **Approved by:** usuário nesta conversa, mensagem literal APROVADO em2026-10-15, após publicação do contrato3302964c822f41d0c3372e16796672bd119c1c90.
- **Approval reference:** resposta APROVADO à solicitação explícita de implementar ST-CON-01; artefato evidence/approval-20261015.json.
- **Approval scope:** APROVADO para SCOPE-01..09, D-01..10, DoD/Validation e paths esperados do contrato publicado; API/Web/runtime local próprios, provas de teste quando readiness disponível, revisões e commits locais de feature; Foundation main autônoma.
- **Execution not authorized by approval:** ST-CON-04 Nova conversa manual/proativa, importação/coexistência/migração externa, mídia/status/transferência, Railway/deploy/push de produto, legado, edição manual de gitlinks/.gitmodules, worktrees/cópias auxiliares.
- **Renewed approval required when:** mudar objetivo, comportamento/risco material, desenho de identidade/credencial/recuperação ou desvios de diff não admitidos no contrato; concretização que preserve os requisitos segue neste TODO.


## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

Ingestão binding realizada em2026-10-15 após APROVADO: fontes das linhas abaixo relidas; executor deve recarregar antes de tocar suas superfícies.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | Fronteira executor/review/Git. | um writer e gates | worktree/gitlink manual | delegar execução |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | Aprovação tática. | APROVADO+guard | iniciar por concordância genérica | bloquear produto antes do guard |
| delphi-ai/workflows/docker/environment-readiness-method.md | Compose/runtime. | target próprio | usar legado/segredo em log | readiness antes da prova |
| delphi-ai/workflows/docker/effort-selection-method.md | Model/role. | execução medium/review max | autodelegação implícita | routing guard |
| foundation_documentation/policies/scope_subscope_governance.md | Ownership das rotas. | contratos do owner | controller sem owner | doc antes do código |
| foundation_documentation/policies/central_whatsapp_independent_legacy_policy.md | Inspiração. | comportamento redesenhado | copiar source/runtime/dados | só referência |
| delphi-ai/workflows/docker/todo-execution-boundary-method.md | Execução após APROVADO. | escopo/authority go | expansão silenciosa | um writer, checkpoint técnico |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | API/contratos. | adapter fino e DI explícita | regra de domínio no controller | validar contrato/auth |
| delphi-ai/workflows/react/change-ui-boundary-method.md | Wizard React. | estado/efeitos e contexto | resposta velha/dobro clique | browser real |
| delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | Schema versionado. | migration deploy em DB exclusivo | reset operacional/editar migration antiga | gerar client e provar schema |
| delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | Dedupe e CAS. | índices/locks/transações curtas | HTTP dentro de transação | barriers reais |
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
| NUM-DELTA-OBS-01 | low | by-design/no-action | enforce-existing-requirement | Fence até commit já exigido; barrier do webhook em voo concretiza BCI | covered-in-plan | Delta v3; REG-SEC-10, nota de execução |
| NUM-DELTA-OBS-02 | low | by-design/no-action | enforce-existing-requirement | Segredo em logs já proibido, inclusive hub.verify_token | covered-in-plan | Delta v3; REG-SEC-12, nota de execução |
| NUM-DELTA-OBS-03 | low | by-design/no-action | enforce-existing-requirement | Refresh já prometido projeta autoria/conteúdo do mesmo ID | covered-in-plan | Delta v3; REG-SEC-11, nota browser; Inbox excluído preservado |
| NUM-API-01 | high | release-blocker | fix-current-contract | Telefone canônico precisa CAS/equality atômico entre transportes | accepted-open | api-checkpoint-review-v1.json; D-01/06 |
| NUM-API-02 | high | release-blocker | fix-current-contract | Promoção deve manter attempt/generation/credential-version/lease até commit | accepted-open | api-checkpoint-review-v1.json; D-03/04/06 |
| NUM-API-03 | high | release-blocker | fix-current-contract | DELETE precisa adquirir o mesmo fence das operações externas | accepted-open | api-checkpoint-review-v1.json; D-06/07 |
| NUM-API-04 | high | release-blocker | fix-current-contract | Renovação limpa antecessor mas não cria substituta reservada | accepted-open | api-checkpoint-review-v1.json; D-06 |
| NUM-API-05 | high | release-blocker | fix-current-contract | Mapping migrado não autoriza adotar/apagar instância externa | accepted-open | api-checkpoint-review-v1.json; D-06/09 |
| NUM-API-06 | medium | release-blocker | fix-current-contract | Retry QR pendente deve preservar rodada apesar de evento connecting/open | accepted-open | api-checkpoint-review-v1.json; D-06/07 |
| NUM-API-07 | medium | release-blocker | fix-current-contract | Limpeza ambígua precisa sobreviver ao unlink e impedir nova criação | accepted-open | api-checkpoint-review-v1.json; D-06/07 |
| NUM-API-08 | medium | release-blocker | fix-current-contract | Close observado deve remover prontidão atual de DTO/envio | accepted-open | api-checkpoint-review-v1.json; D-07 |
| NUM-API-09 | medium | release-blocker | fix-current-contract | Verificação oficial sem telefone próprio não comprova identidade | accepted-open | api-checkpoint-review-v1.json; D-01/07 |
| NUM-API-10 | medium | release-blocker | fix-current-contract | Expiração/supersessão/remoção devem limpar candidata e nonce | accepted-open | api-checkpoint-review-v1.json; D-03/04 |
| NUM-API-11 | medium | release-blocker | fix-current-contract | Replay concorrente same-key deve retornar a mesma tentativa | accepted-open | api-checkpoint-review-v1.json; D-03 |
| NUM-API-12 | medium | release-blocker | fix-current-contract | Audit administrativo já prometido não pode virar isenção técnica | accepted-open | api-checkpoint-review-v1.json; audit-and-history#cadastro |
| NUM-API-13 | medium | release-blocker | fix-current-contract | Redação URL deve cobrir vocabulário de segredos e nomes codificados | accepted-open | api-checkpoint-review-v1.json; REG-SEC-09/12 |
| NUM-API-14 | medium | release-blocker | fix-current-contract | Ordem de locks identity/channel deve eliminar ciclo de deadlock | accepted-open | api-checkpoint-review-v1.json; D-06/08; BCI |
| NUM-API-15 | medium | release-blocker | fix-current-contract | OUT sem ID confirmado conserva resultado local pendente/erro explícito | accepted-open | api-checkpoint-review-v1.json; integrations-and-channels#reconciliação |
| NUM-API-16 | medium | release-blocker | complete-required-harness | Probes discriminantes REG-SEC e callers fazem parte do escopo aprovado | accepted-open | api-checkpoint-review-v1.json; VAL-02/08 |
| NUM-API-17 | medium | release-blocker | complete-required-harness | Positivas novas não são provadas pelos409 de rota aposentada | accepted-open | api-checkpoint-review-v1.json; test/modulos e canais |
| NUM-API-18 | low | release-blocker | fix-current-contract | Metadata pré-identidade deve usar state allowlisted, sem conteúdo arbitrário | accepted-open | api-checkpoint-review-v1.json; REG-SEC-03/13 |
| NUM-RUNTIME-01 | high | release-blocker | enforce-existing-requirement | Provider fixado registra URL em falha de callback, expondo segredo no path apesar do gateway | accepted-open | Concretizar alternativa por header já condicionada no contrato; fonte primária e prova runtime obrigatória; REG-SEC-12 |
| NUM-WEB-01 | medium | release-blocker | fix-current-contract | DTO antigo da mesma tentativa não pode regredir version/geração | accepted-open | web-checkpoint-review-v1.json; D-07 |
| NUM-WEB-02 | medium | release-blocker | fix-current-contract | Popup precisa ownership para callback não perder code em busy no-op | accepted-open | web-checkpoint-review-v1.json; D-02/03 |
| NUM-WEB-03 | medium | release-blocker | fix-current-contract | Cadastro novo deve ser independente de retomada de tentativa alheia | accepted-open | web-checkpoint-review-v1.json; SCOPE-01 |
| NUM-WEB-04 | medium | release-blocker | fix-current-contract | Reinício de nonce usa BU já criada, sem duplicar novaBu | accepted-open | web-checkpoint-review-v1.json; D-01/03 |
| NUM-WEB-05 | medium | release-blocker | fix-current-contract | Cancelamento preserva explicação/resultado parcial durável | accepted-open | web-checkpoint-review-v1.json; D-05 |
| NUM-WEB-06 | medium | release-blocker | fix-current-contract | Verify consome receiptVerified booleano, não timestamp inexistente | accepted-open | web-checkpoint-review-v1.json; SCOPE-05 |
| NUM-WEB-07 | medium | release-blocker | fix-current-contract | Erros/status/finally antigos não escrevem após trocar contexto | accepted-open | web-checkpoint-review-v1.json; D-02/07 |
| NUM-WEB-08 | medium | release-blocker | fix-current-contract | QR efêmero precisa vínculo/tentativa/geração corrente e limpeza ao concluir | accepted-open | web-checkpoint-review-v1.json; D-06/07 |
| NUM-WEB-09 | low | release-blocker | fix-current-contract | postMessage sem correlação não muda feedback de outra tentativa | accepted-open | web-checkpoint-review-v1.json; contrato SDK |
| NUM-WEB-10 | medium | release-blocker | fix-current-contract | Loader SDK falho precisa retry controlado sem listeners obsoletos | accepted-open | web-checkpoint-review-v1.json; SCOPE-02 |
| NUM-WEB-11 | medium | release-blocker | enforce-existing-requirement | Recuperação parcial deve expor ação segura; leitura conclusiva condicionada a contrato real do provider, sem replay cego | accepted-conditional-open | web-checkpoint-review-v1.json; fallback pending/nova autorização já explícito em D-05 |
| NUM-WEB-12 | low | release-blocker | fix-current-contract | Parser de evento exige string enum primitiva, total para schema malformado | accepted-open | web-checkpoint-review-v1.json; contrato SDK |
| WEB-ROOT-01 | high | release-blocker | fix-current-contract | SDK readiness perdido após reservar tentativa | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-02 | high | release-blocker | fix-current-contract | Consumo incorreto do wrapper registration da confirmação | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-03 | medium | release-blocker | fix-current-contract | Retomada persistida e cancelamento explícito necessários | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-04 | medium | release-blocker | fix-current-contract | Etapa no wizard precisa refletir webhook/receipt atual | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-05 | medium | release-blocker | fix-current-contract | Retry de reserva perdida precisa conservar chave idempotente | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-06 | medium | release-blocker | fix-current-contract | Troca explícita de WABA não pode perder opções autorizadas | accepted-open | evidence/root-web-checkpoint3-findings.json |


Adicional de coerência do autor: envelope raw redigido e code/PIN transitórios explicitados, sem alterar modelo de autorização; REG-SEC-08/09.

Adjudicação do checkpoint API: parecer bruto imutável api-checkpoint-review-v1.json (SHA256 e44b11aed763a452afcf1786e04e30a2a1d91ae012e3d0bd743c0281322028ee), schema nativo validado,18 achados (5high/12medium/1low), leitura completa de68 snapshots atestada. Root aceita os18 para correção no contrato atual: todos correspondem a D-01..08, limites contra legado, audit/segredos ou harness já exigidos. Não há dispensa, nova capacidade, worker, outbox ou autorização de runtime legado. Severidade baixa de NUM-API-18 não reduz o requisito explícito de metadata allowlisted. Solução deve ser simples e coerente; executor reportará qualquer necessidade de path ou decisão material ANTES da edição. Etapa pré-consumer, não gate final: correção e testes discriminantes ainda pendentes. Web termina/paralisa primeiro; API é o próximo writer único. Root permanece em orquestração documental; produto fica com Operational/Coder e runtime com DevOps.

Adjudicação do checkpoint Web: parecer terminal web-checkpoint-review-v1.json SHA25650dbe11bdffa49fd042d09c9b9a652280cb472ac6d42d3e94feb71ca1b0b5622, schema nativo validado,12 achados (10medium/2low). Root aceita correções no mesmo contrato. Para NUM-WEB-11, aceita a lacuna de ação/explicação segura, mas não presume que existam campos/endpoints conclusivos de register/subscription: leitura deve ser comprovada por fonte primária e validação; sem isso vale a alternativa já aprovada de pending/nova autorização, nunca replay cego de mutação ambígua. Nenhuma criação de endpoint remoto ou alteração de callback alheio por conveniência. Executor Web propôs um helper tipado coeso de contexto/versão/operação, aceito como HOW dentro dos globs já autorizados; deve preservar avanços legítimos de geração/attempt pelo resultado da ação atual. Implementação Web aguarda stop da API, não há writers concorrentes. Browser discriminante real-backend e FRC continuam obrigatórios.

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** execução aprovada iniciando; critérios de entrega/provas ainda pendentes.
- **Post-commit/push status:** n/a
- **Next path/status action:** executar checkpoints e evidências neste mesmo TODO, sem claim antecipado de entrega.

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
| EPS | endpoint-performance-scrutiny | required | medium | EPS-DATA-PATH-CHANGED | before_local_implemented | EPS-E2 | pending | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | pending | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-DUPLICATE-SUBMIT-OR-REPLAY | before_local_implemented | BCI-E3 | pending | none | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-QUEUE-WORKER-REALTIME-CHANGED | before_local_implemented | RLS-E1 | pending | none | none |

#### EPS
Lookup único por vínculo/tentativa e índice de expiração, EXPLAIN na tabela representativa; sem fan-out em listagem. Perfil EPS-SP-STRONG, aceitação EPS-A2; medição local e limites documentados.
#### FRC
Coalescer duplo clique; cancela contexto anterior, descarta versão velha; repetição forte20triggers×5, requests/in-flight e estado/draft observáveis. Perfil FRC-SP-H; FRC-A1.
#### BCI
CAS na tentativa, unicidade de slot/providerID e geração;20operações sobrepostas×5 com barriers para criação, finalize/replay e delete/recreate, controle negativo. Perfil BCI-SP-H; BCI-A1. Sem exactly-once de provider afirmado; timeout externo ambíguo fica pending.
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

- **Cutover audit decision:** required
- **Why this decision:** credencial global é retirada; todos os consumers precisam convergir, sem shim/fallback.
- **Cutover audit status:** not_run
- **Evidence / reference:** audit-protocol-triple-review após implementação; sem dispensa.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

n/a; sem claim Production-Ready ou promoção remota.

## Module Consolidation Gate (Required Before `Completed`)

- **Gate decision:** required
- **Gate status:** not_run
- **Evidence / reference:** módulos owner e contratos antes do código; Verified somente depois de evidência aceita. Nenhuma alteração de constituição planejada.

## Commands (Run Locally)

Após APROVADO: runner source-owned API/Web e compose local; executar folhas documentadas na matriz. Segredos vêm do ambiente privado e não aparecem em comando/log. Antes de executar, routing e readiness do executor go. Comandos já executados no checkpoint1 constam do relatório específico; a matriz final continua pendente.

## Files Expected (Compatibility Note)

O Diff Expectation Contract é a referência candidata; paths atualizados após architecture_opinion; desvios novos exigem classificação antes da edição. Nenhum Files Expected paralelo concede novos paths.

## COMENTÁRIO:

Nenhum comentário de aprovação pendente foi tratado como APROVADO.


## Execution Checkpoints

- Checkpoint1 concluído em2026-10-15: schema/2migrations, cifra/redaction e owner de aceitação de mensagens. Evidência: artifacts/reviews/leadshug-number-onboarding-20261015/evidence/checkpoint1-execution-evidence.md. Fonte final:119unidades+3PGtargeted+lint/build/migrate.226E2E amplas anteriores ao último hardening não serão reaproveitadas como prova da fonte final do produto.
- Checkpoint2 API entregue para revisão independente: build/lint,130unitários/20arquivos,234E2E PostgreSQL/22arquivos e20migrações passaram na fonte registrada em evidence/checkpoint2-api-handoff.md;42hashes conferidos pelo root. Writer parado. Ainda faltam probes REG-SEC/PCV listados no handoff, correções/review, UI, runtime/ingress com handoff DevOps e prova real. Não equivale a aceite geral do TODO.
- Usuário confirmou nesta execução não ter ainda app Meta/Embedded Signup nem HTTPS e autorizou preparo. A prova oficial permanece pendente dessa configuração na conta do operador; não bloqueia trabalho interno independente.
- Preparação documental: artifacts/reviews/leadshug-number-onboarding-20261015/local-setup.md; handoff de runtime planejado em runtime-handoff.md no mesmo diretório. Nenhuma criação de app, túnel ou runtime foi reivindicada por esses roteiros.
- O classificador genérico profile_scope_check não reconhece prefixos api-app Nest; paths unknown foram conferidos contra constituição, owners e Diff Expectation do TODO aprovado. Nenhuma negação de escopo foi ignorada; Delphi/regras não foram modificados.
- Artefatos checkpoint1 inicialmente escritos no prefixo workspace artifacts por ambiguidade do handoff foram movidos byte a byte para foundation_documentation/artifacts, sem mudar stdout/hash. Próximos handoffs usarão caminhos absolutos.

### Concretização de paginação — checkpoint2

O executor identificou que confirmar só a primeira página impossibilitaria selecionar um número mostrado por continuação. Admitidos `wabaId`/`after` em options e `after` opcional em confirm, conforme contrato owner acima. É concretização do HOW da seleção paginada já aprovada: mesmos paths/objetivo/credencial, mesmo limite externo, nenhuma nova permissão, persistência, integração ou comportamento independente. A página vem sempre do edge phone_numbers da WABA revalidada; o cursor não substitui prova de pertencimento. Testar seleção da segunda página, cursor inválido e número estrangeiro. D-01..10 e limites do escopo preservados; não é expansão material nem nova aprovação.

### Alinhamento do piso PCV — execução

A releitura de performance-concurrency-validation-method.md identificou que EPS medium requer E2/A2 e FRC/BCI high requerem o piso H, enquanto o rascunho aprovado misturava severidade high com amostragem M. Corrigidas as referências e fortalecida a amostragem para20×5 antes de executar esses gates. Nenhuma obrigação foi reduzida, nenhum gate foi dispensado e nenhuma evidência anterior foi reclassificada. RLS permanece a etapa bounded explicitamente contratada, sem claim SLO/capacidade ou carga no provider real.

### Checkpoint3 — preparação Web serializada

Após stop explícito do writer API com130unitários/234E2E, executor novo assume SOMENTE Web como único writer de produto. Review independente lê o pacote imutável API de68fontes, SHA256a5113ac1fd729cfc1ba902bc3b667b7b6c32818e4dbab9534028c00f5d50992a. API/fixtures/artefatos gerados/runtime não podem mudar nessa preparação; browser real-backend será integrado em etapa posterior serializada. Routing Web go e capability audit React/Vite ready, conforme manifests reais. Handoff detalhado: artifacts/reviews/leadshug-number-onboarding-20261015/web-handoff.md. Nenhuma entrega de UI ou gate geral reivindicados.

Checkpoint3 Web parado com build e23 testes/4arquivos passando; seis hashes conferidos. Revisão de fonte pelo root encontrou perda determinística de SDK readiness após reserva, ausência de retomada de tentativa persistida e falta de atualização da etapa por webhook. Achados aceitos como correções do contrato UI já aprovado, nos mesmos paths; executor Web recebe lote serializado de remediação, ainda sem editar API/runtime. Deve também conservar a chave idempotente em retry da mesma reserva quando a resposta é perdida. Provas de browser com backend real seguem pendentes, sem aceitar os testes unitários como substitutos.

Checkpoint4 Web encerrado com stop explícito, build e25 testes/4arquivos passando, seis hashes conferidos; correções de WEB-ROOT-01..06 implementadas aguardam prova de browser. Root aceita a remediação estrutural proposta para NUM-API-01..18 como execução do contrato atual, incluindo evidência de lifecycle managed separada de backfill e cleanup retido após unlink, conforme módulo owner consolidado. Handoff de volta a Operational/Coder: executor API reassume como único writer para schema/source/harness/fixtures nos paths já autorizados, routing-api-remediation.json go; Web e DevOps parados, sem escrita concorrente ou runtime externo. DoD/gates seguem abertos, nenhum achado marcado verificado por declaração do executor.

Concretização condicionada REG-SEC-12: inspeção do source primário Evolution2.3.7/cd800f2976e1e5b682fbf86a01ee4d85ae61f370 comprovou per-instance webhook.headers aplicado ao axios e URL impressa em falha de callback (webhook.controller.ts:69-122,124-136,217-243). O contrato já permite "Callback por header só se suportado e comprovado no provider fixado"; portanto concretizar POST /webhooks/evolution com segredo no header x-leadshug-webhook-secret e URL sem segredo, sem fallback de path. Mesmo segredo privado de instalação, mesma autenticação/capacidade/owner, nenhum serviço externo adicional ou privilégio novo. API implementa header no adapter e validação timing-safe do ingresso; rota antiga não aceita eventos. Todos os paths já previstos; testes/fixtures/catalogue/env correspondentes devem acompanhar. Fonte prova suporte, mas não comprova runtime: envio de header pelo provider fixado e logs reais sem marcador continuam gates obrigatórios antes de prova de aparelho. Não suprimir todos os erros do provider como substituto. LOG_LEVEL explícito sem LOG/WEBHOOKS evita impressão de QR/payload; QR permanece efêmero. Se runtime contradisser suporte/fidelidade, parar ativação e rever contrato, sem alegar prova antecipada.
