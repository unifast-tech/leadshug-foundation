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
- **Next exact step:** cp36j unitário isolado app_id estrangeiro + APIleaf/composição/reviews atuais, enquanto humano INOUT02 está pendente. API corrigida fe5fb7 já servida/saudável, mesma Evolution retomou automaticamente com tentativa v2/epoch1/conversa preservados. Antes oficial real/entrega resolver FINAL-CP36I-01; VAL05 aberto.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** implementation
- **Why this state now:** API-only cp49 e origem atual concluídas; reconexão automática real após SAMEEvolutionstop/start confirmada sem adminverify posterior, root verificou actualimage/compiled4/HTTPS. Falta humano INOUT02; Coder cp36j é único writer do spec e validação descartável para FINAL01, sem alterar runtime operador. TQA/final de nova cobertura continuarão obrigatórios, D05D06D07 Exception/entrega Pending.
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

Wizard: nome/BU → modalidade → janela Meta ou QR → confirmar número → mostrar cadastro/recebimento e ação de retry quando parcial. Cancelar popup, trocar BU, desmontar tela ou nova tentativa invalida callbacks/efeitos antigos no cliente; backend ainda revalida scope. A UI não consome mensagens postMessage para autorização ou seleção; somente o callback do SDK correlacionado à operação atual inicia a troca do code. IDs externos são obtidos e confirmados pelas leituras autorizadas no backend. Callback de login fica preso à geração/attempt/nonce corrente; prova server-side da credencial/ID é obrigatória.

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
| api | src/domain/channels/channels.service.spec.ts | D | Remover três testes do gerador de slug aposentado junto dos métodos legados sem callers; provas da jornada agregada nos E2E novos. |
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
| api | .dockerignore | M | Excluir .local-files/ e .git do contexto Docker antes do build operacional; nenhuma leitura/cópia dos payloads rastreados. |
| api | test/timeline-fixtures.cjs | M | Preservar fixtures de timeline e fornecer controles out-of-band do provider para browser com BFF/sessão/PG reais; nunca expor no gateway do operador. |
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
| web | e2e/telas.spec.ts | M | Caso Números: substituir botão Conectar WABA aposentado pela jornada aprovada. Caso identidade visual: somente barreira de PUT real antes do reload, admitida após falha cp14. Casos Pessoas “adicionar uma pessoa e conceder um setor a ela” e “convidar mostra o LINK quando o e-mail não sai”: somente seleção explícita do Número de QA próprio antes do convite e barreira/assert201 do POST real, admitidas cp36d após falha cp36c e classificação independente; preservar Ana/setor e Bia/link, console/auth. Preservar assertions de cores/tema, BU/ausência de canal. Nenhuma outra edição de caso. |
| web | e2e/timeline-freshness.ts | M | Concretização necessária: manifesto compartilhado deve representar deleções e cobrir fixtures/schema/config pertinentes; preservar health, banco descartável e comparação bundle servido/buildado. |
| web | playwright.config.ts | M | Projeto adicional com mesmo backend real. |
| web | .dockerignore | M | Excluir env privados do contexto de build e da carga automática Vite; manter somente exemplo público. |
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

Admissões concretas de execução estão detalhadas abaixo. Classificação de gitlinks preexistentes no workspace não concede permissão de alterá-los manualmente. Outras fixtures encontradas necessárias devem ser admitidas antes de editadas; não modificar expectativas de negócio só para passar tests.

- `test/realtime.e2e-spec.ts`: guard de execução encontrou path não classificado. Diff inspecionado pelo orquestrador: somente import do helper `criarCanalVerificado` e substituição da criação direta de BuChannel pela fixture completa de identidade/credencial; nenhum assert, cenário ou comportamento de socket alterado. Necessário para preservar a prova de push scoped após o ingresso passar a exigir identidade durável. Classificação: concretização de fixture da validação SCOPE-07/09 já autorizada, sem nova capacidade, objetivo ou risco material. Admitido esse path exato, sem abrir `test/**`; nenhuma dispensa do guard. A edição precedeu a admissão, falha de sequência registrada e corrigida antes de qualquer entrega; executor instruído a consultar antes de novos paths.
- `test/modulos.e2e-spec.ts`: novo guard encontrou expectativa201→409 em duas chamadas do endpoint aposentado. A constituição exige atualização correspondente de testes de contrato na mesma entrega; esse path é concretização da validação já aprovada, sem ampliar capacidade ou superfície de produto. Admitido o path exato para aposentadoria E provas positivas na nova jornada. A alteração atual não é suficiente como prova positiva de módulo/piso: nomes ainda alegam conexão mas só409 não a exercita; achado de qualidade aberto para correção após a revisão congelada. As negativas404 de teto/contratação devem ser preservadas. Segunda falha de sequência registrada; não concede `test/**` nem dispensa gates.
- `web/src/api.spec.ts` (path interno Web `src/api.spec.ts`): guard intermediário encontrou path não listado que o handoff do root havia chamado incorretamente de admitido. Diff inspecionado: somente acréscimo de13linhas testando header Idempotency-Key, URL sem correlação e body do novo helper; nenhum assert anterior alterado. Classificação: teste de contrato necessário ao helper já aprovado em src/api.ts, sem nova capacidade/risco/escopo de produto, alinhado à constituição. Admitido esse path exato; falha de sequência de conferência do root registrada, sem abrir outros testes. Web já está parada; pacote de review congelado permanece imutável. Não usar o verde unitário para substituir browser. Guard deve voltar go antes de entrega.
- `api/src/domain/channels/channels.service.spec.ts` (path interno API): a remoção dos métodos legados sem callers já aceita incluiu seus três testes de slug, deixando o arquivo sem cenários aplicáveis. O glob de domínio admitia escrita mas não o tipo D. Admitido exclusivamente D nesse arquivo, preservando as novas provas positivas de canais/módulos e a aposentadoria HTTP nos E2E; não há autorização genérica de apagar testes. Concretização do mesmo contrato, com conferência de tipo tardia registrada antes da entrega.
- `web/.dockerignore` (path interno Web): leitura do Dockerfile e ignore constatou `COPY . .` no builder Vite sem exclusão de `.env`/`.env.*`; a API já exclui esses arquivos. Admitido antes de qualquer edição Web para impedir ingestão de configuração privada no build, concretizando DOD-03. Nenhum arquivo privado será lido, alterado ou apagado; nenhum comportamento, dependência, endpoint ou implantação adicional. Verificar build e contexto sem registrar valores privados.

## Bounded But Elastic Guardrails

Cadastro/QR/autorização/recebimento pertencem a este objetivo. Nova conversa proativa, modelos, importação e tomada de callback externo não cabem como refinamento. Versão de provider, armazenamento de credencial, semântica de recuperação ou obrigação externa alteradas materialmente exigem nova revisão antes da execução.

## Definition of Done

- [ ] DOD-01: cadastro oficial e QR operáveis por administrador da BU, com número/identidade confirmados e cancelamento/falhas sem falso sucesso.
- [x] DOD-02: tentativas de cadastro, credenciais cifradas e número externo scoped; replay/duplo clique/troca de BU/remover-recriar não duplicam ou cruzam vínculo.
- [x] DOD-03: credencial por canal é usada por todos os consumidores Meta existentes; sem token de cliente global, logs/DTOs/artefatos sem segredo.
- [x] DOD-04: runtime local isolado e migrations aplicáveis, orçamento externo bounded, erro/retry/frescor explícitos e webhook autenticado.
- [ ] DOD-05: primeira IN real de cada canal cria/reutiliza conversa BU/contato e aparece na inbox; resposta OUT dentro do contrato existente chega ao interlocutor.
- [ ] DOD-06: CI-equivalent API/Web/workspace, fluxo Playwright com build atual, segurança/PCV e revisões independentes aceitas.
- [x] DOD-08: NUM-ARCH-01..06 e NUM-CRIT-01/02 cobertos por harness de tenant, replay, identidade, reautorização e POST de pairing; nenhum segredo de envelope webhook persiste.
- [ ] DOD-07: decisões consolidadas no módulo owner, evidence matrix completa, source commits e guardas go antes do closeout local.

## Validation Steps

- [x] VAL-01: unidade/adapter para cifra e AAD, payload Meta/Evolution, erro/timeout, seleção entre múltiplos números e contrato de registro.
- [x] VAL-02: PostgreSQL E2E para sessão/grant/tenant, tentativa expirada/cancelada/replay, disputa create/delete/recreate/verificação/evento e persistência de falha parcial.
- [x] VAL-03: Playwright do cadastro/QR, popup cancelado/erro/timeout, mudança BU e resposta velha; backend/sessão/DB reais, servidor de provider de teste apenas como porta externa.
- [x] VAL-04: migrate deploy e CI-equivalent API/Web/workspace da fonte final; fingerprints do bundle antes dos workers, banco exclusivo e execução sem sobreposição de suites destrutivas.
- [ ] VAL-05: prova externa local por canal, com autorização Meta/QR real, IN na BU certa, OUT recebida pelo interlocutor e recuperação permitida da conexão.
- [ ] VAL-06: EPS/FRC/BCI/RLS conforme plano; security, debt, architecture_adherence, TQA, audit especializado e final review antes de completar. Evidência cp27 histórica; TQA i terminal favorável e final atual condicional. FINAL-CP36I-01 obrigatório antes oficial/entrega, sem gate limpo.
- [x] VAL-08: executar REG-SEC-01..13 do plano de validação, incluindo replay por provider, renovação de canal já verificado, echo-first/sender-first com autoria, tombstone, candidata, CSRF e logs/partição raw.
- [ ] VAL-07: consolidar módulo, validar contrato/diff/coerência e closeout; nenhum claim de produção pronta.

## Completion Evidence Matrix (Required Before Delivery Claim)

Disposição local por critério: cp27 e seus reviews são históricos; API cp36i atual e Web/browser h de fonte consumidora inalterada têm composição explícita. `passed` se limita à evidência descrita; revisões do delta, requisitos externos e closeout continuam pendentes. Raw/manifestos/freshness têm hashes no recibo root-cp27; nenhuma linha dispensa VAL-05.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | Jornada Adicionar número/BU | browser+db | canais E2E; number-onboarding.spec.ts; cp27-final-all.log + root-cp27-receipt.json | local real-backend | passed | NovaBU/seleção existente, grant herdado e contagem persistida em BFF/PG/browser reais. |
| SCOPE-02 | Scope | Embedded Signup e vínculo | contract+browser+provider | number-onboarding-flow E2E; number-onboarding.spec.ts; cp27 all; VAL-05 | local + Meta teste | blocked | Contrato/local SDK-provider doubles passam; autorização/número Meta reais ausentes. |
| SCOPE-03 | Scope | Credencial cifrada scoped e consumers | unit+integration | crypto/resolver unit; caller-scoping/public/atendimento/Typebot E2E; cp27 all; cp25 cutover/security | Node22/PG16 | passed | AAD/tamper/candidata/ativa e credencial própria por caller; sem fallback global. |
| SCOPE-04 | Scope | QR/instância/webhook | browser+provider | flow/canais E2E e browser h; cp32/cp33; VAL-05 | Evolution própria | blocked | QR/identidade/primeira INOUT reais comprovados cp32/cp33; retomada automática do vínculo ainda pendente. |
| SCOPE-05 | Scope | Estado honesto e geração | race | flow/BCI/FRC PG/browser; cp24-pcv-bci/frc.json; cp27 all; NUM-RECOVERY-CP36-01 | local+real | blocked | Geração/epoch/lease/currentAttemptId e receipt separados; cp36 abriu bloqueador agora verificado em cp49 por retomada automática real/SAMEattemptv2/epoch1; humanoINOUT02 e oficial ainda obrigatórios. |
| SCOPE-06 | Scope | Primeira IN na conversa | provider+browser | webhooks/acceptance E2E; inbox browser; VAL-05 | local + dois providers | blocked | IN não oficial real comprovada em cp33: uma conversa/uma IN/uma OUT. Oficial ainda não executado. |
| SCOPE-07 | Scope | Matriz/segurança | test+review | cp36i API173/288; Web28/browser47 h por fonte idêntica; TQA i terminal; final condicional | local isolado | blocked | Matriz local validada e histórico cp27 preservado; TQA i terminal aceitou H01; final condicional mantém teste D02 obrigatório antes oficial/entrega. VAL-05 separado obrigatório. |
| SCOPE-08 | Scope | Runtime próprio | runtime | cp24-integrated-runtime-all-handoff.json; cp25-config-precedence-proof.json; cp25-https-runtime-proof.json; cp27 migrations | local | passed | Operador isolado/22migrações, HTTPS/produção/CORS/cookie exatos; nenhuma conexão real inferida. |
| DOD-01 | Definition of Done | Cadastro oficial e QR usáveis | browser+provider | VAL-03/05; cp27 browser47 | local | blocked | Jornadas locais operáveis; prova de administrador com Meta/aparelho reais obrigatória. |
| DOD-02 | Definition of Done | Replay/tenant/races | integration+race | flow/BCI PG; browser tenant/replay/FRC; cp27 all; cp24-pcv-bci/frc.json | PG16/browser | passed | Mesma tentativa/chave, slot/owner imutável e races com controles negativos. |
| DOD-03 | Definition of Done | Credencial e consumidores | test+audit | crypto/redaction unit; caller-scoping/public/Typebot/atendimento/raw E2E; cp25 cutover/security; cp21 log proof | local | passed | Todos callers scoped; logs/build/DTO secret-free dentro do harness/coorte declarados. |
| DOD-04 | Definition of Done | Runtime/migration/erro | runtime+test | cp27 migrate/lint/build/all; cp25 config/HTTPS proof; REG-SEC-12/header probe | local | passed | 22migrações, budgets/leases, erros seguros e runtime próprio; readiness contínua não inferida. |
| DOD-05 | Definition of Done | IN/OUT reais por canal | provider+browser | VAL-05 checklist do plano de validação | números teste | blocked | QR/identidade/IN/OUT não oficial comprovados em cp32/cp33 e entrega no interlocutor confirmada. Recuperação e autorização/troca oficial pendentes. |
| DOD-06 | Definition of Done | CI-equivalent e review | test+review | cp27 all + attestations; PCV4/cp25 reviews históricos; delta cp36c em validação/revisão | local/review | blocked | Aceites anteriores preservados como históricos; novo delta exige all/TQA/aderência/segurança/final atuais antes do runtime. VAL-05 obrigatório separado. |
| DOD-07 | Definition of Done | Canon/source/guardas | doc+guard | quatro módulos owner; cp27-committed-source-attestation.json; guardas finais | Foundation | pending | 74paths públicos byteexact commitados localmente; execução/diff permitidos, entrega geral ainda no-go por VAL-05; closeout geral pendente. |
| VAL-01 | Validation Steps | Unidade/adapter/cifra | unit | scripts/test-channels-local.sh api; cp36i-api.log 173unit; Web28 h | Node22 | passed | Atual API173 inclui grant revogado válido-shaped, classe/code/zero consulta de números; cifra/adapters/config e limites preservados. Webunit h fonte consumidora idêntica. |
| VAL-02 | Validation Steps | PostgreSQL/auth/races | integration | cp36i-api.log PG288/22migrações; flow/BCI/webhooks/atendimento/public/Typebot E2E | PG16 exclusivo | passed | PG16descartável, sessão/grant/tenant/lease/convergência/estado parcial e ponte Meta real no BFF com I/O externo dobrado. |
| VAL-03 | Validation Steps | Browser com backend real | browser | cp36h-api-all.log browser47; cp36h-pre-worker-freshness.json; cp36h-browser-attestation.json; root-cp36i-validation-receipt.json | bundle h/local fonte consumidora idêntica | passed | Reuso honesto h; oito paths idênticos e único spec unitário novo excluído do build. Ambas attestações originais h preservadas; não nova freshness9 i ou novo all536. |
| VAL-04 | Validation Steps | Migration/CI/freshness | runtime+suite | cp36i API leaf; manifest9 preapi/postapi; root-cp36i-validation/public-set; attestações h imutáveis | local principal | passed | API461 nova + Web28/browser47 h de bytes consumidos idênticos; 22migrações e namespaces separados, nenhum all536 ou runtime operador corrigido inferido. |
| VAL-05 | Validation Steps | Prova externa local | provider | validation-plans/leadshug-channel-readiness-20261015.md; cp22-meta-panel-setup.json | Meta/Evolution teste | blocked | cp33 comprovou cadastro/identidade/receipt e primeira IN/OUT não oficial. Recuperação cp34 autorizada, ainda pendente; conexão/troca oficial pendentes, sem waiver. |
| VAL-06 | Validation Steps | PCV/reviews | review+runtime | PCV/cp25/cp27 históricos; TQA h/i terminal, final i condicional por cobertura D02 | local/no-context | blocked | H01 test-only/API173/288 aceito; TQA completo e final distinto atuais terminal; final condicional por teste D02 obrigatório antes oficial/entrega. VAL-05 separado sem waiver. |
| VAL-07 | Validation Steps | Consolidação/diff/closeout | doc+guard | quatro módulos owner; cp27-committed-source-attestation.json; guardas finais | Foundation | pending | 74paths públicos byteexact commitados localmente; execução/diff permitidos, entrega geral ainda no-go por VAL-05; closeout geral pendente. |
| SCOPE-09 | Scope | Reautorização, identidade, dedupe e tenant | integration+race | REG-SEC-01..13; cp27 all; flow/Typebot/acceptance/atendimento e BCI | PG16 isolado | passed | REG-SEC-01..13 local aceito; BFF/public/Typebot e acceptance compartilhada preservados, suplemento TQA sem novos achados. |
| DOD-08 | Definition of Done | Harness de arquitetura/crítica e segredo raw | test+audit | REG-SEC table; cp25 security; cp27 all; TQA suplemento | local | passed | REG-SEC-01..13 aceitos local cp25; duas negativas cp26 passaram cp27 e TQA suplemento fresh aceitou ambas; VAL-05 permanece obrigatória. |
| VAL-08 | Validation Steps | Regressões de identidade/tenant/credential | integration+race | REG-SEC-01..13 table; cp27 all; cp25 security e TQA suplemento | Node22/PG16 | passed | REG-SEC-01..13 aceitos local cp25; duas negativas cp26 passaram cp27 e TQA suplemento fresh aceitou ambas; VAL-05 permanece obrigatória. |


## External Dependency Readiness (Required When External Systems Matter)

Register: `foundation_documentation/artifacts/dependency-readiness.md`.

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Evolution de teste e versão | Endpoint/payload/sessão reais. | degraded | 2026-10-16, cp21/cp22 | Runtime próprio fixado2.3.7; cp32 QR/identidade/epoch e cp33 primeira IN/OUT reais aceitos. | Preservar legado; reiniciar somente Evolution própria para recuperação autorizada e repetir IN/OUT. |
| Meta/WABA de teste | Identidade e operação oficial. | degraded | 2026-10-16, cp22 | Configuração privada reconhecida; usuário confirmou allowlists atualizadas e Meta validou/salvou callback HTTPS. OAuth/número/IN/OUT ausentes. | Messages, novo callback e wizard concluído confirmados pelo operador; cp31 onboarding completo e cadastro oficial AVAILABLE. Seguir autorização/teste de número pela UI, app sem publicar. |
| Números/interlocutores de teste | Prova IN/OUT. | unknown | n/a | Usuário confirmou disponibilidade dos dois em2026-10-15. | Confirmar target/destinatário sem publicar números pessoais. |
| Documentação oficial Meta | Cadastro/registro/assinatura. | degraded | 2026-10-15 | Coleção primária Meta Postman acessível; developers direto limitado. | Elegibilidade/app/Graph version ainda dependem de readiness; histórico fora do recorte. |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Current profile:** operational-devops em handoff para validação externa pelo operador; revisores/DevOps STOP e executor API cp36 ativo sob escopo limitado. Root consolidou aceites, commits/bridge públicos e guardas. Escopo Docker/NestJS/React/Vite/PostgreSQL/Prisma; nenhuma ação Meta/aparelho/provedor inferida. DevOps cp28..cp31 terminais STOP: HTTPS/origem/sessão recuperados, wizard concluído pelo operador e readiness/freshness cp31 aceitas. cp32/cp33 aceitaram pareamento/identidade e primeira troca IN/OUT. DevOps cp34/cp35 terminaram STOP. Operational/Coder cp36 é único writer de API/testes para regressão de retomada, seguido de assurance delta e handoff DevOps API-only.
- **Primary execution profile:** operational-coder; handoff operational-devops antes de runtime/ingress.
- **Active technical scope:** nestjs, react, postgresql, prisma, docker
- **Expected supporting profiles:** operational-devops para target/callback; assurance-tester-quality e assurance-security-adversarial para gates aplicáveis.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log (Update when execution crosses profile boundaries)

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | Implementar somente contrato aprovado. | API/Web/canon owner | active; API cp5a parada com fonte conferida e limites de runner registrados; Web recebe remediação NUM-WEB-01..12 como próximo writer único, routing-web-remediation go. |
| operational-coder | assurance-security-adversarial | Revisar correção/segurança/aderência da API antes da integração do consumidor. | Pacote API congelado e relatório, somente leitura de produto | completed-diagnostic; api-checkpoint-review-v1.json terminal,18 achados aceitos abertos; não equivale ao gate final. |
| operational-coder | assurance-tester-quality | Diagnosticar UI corrigida antes de integração browser. | Pacote Web imutável, relatório somente | completed-diagnostic; web-checkpoint-review-v1.json terminal,12achados adjudicados; pacote17snapshots SHA256df4bb1403d1b5e64d30685d33ca48eb3f9204d8d8bb26feae9e41f29274a8b50; não substitui TQA/gates finais. |
| operational-coder | operational-devops | Configurar e provar callback/target de teste se necessário. | Compose local/variáveis/callback e instância própria | stopped-cp7; runner Node22/OpenSSL3, máscara de env,21migrações,lint/build passaram após corrigir montagem dist;129/130unit revelou expectativa de versão presumida. Sem E2E/Web/browser/operador executados nessa rodada. DevOps parou, coder API recebe próximo lote de configuração/harness. |

Concretização de isolamento D-09 antes da ativação DevOps: runtime do operador em projeto novo `leadshug_channels_local`, banco `leadshug_channels_local`, separado do projeto descartável `leadshug_channels_validation`, banco `leadshug_timeline_channels_ci`. Confirmar ausência/ownership dos recursos antes de criar; não adotar homônimos existentes. Fixtures/seed e configuração fictícia ficam só na rede de validação; gateway/túnel público atende somente o runtime do operador. Banco pareado fica fora do allowlist de reset. O handoff detalha bind Windows, proteção dos env privados e prova de logs inclusive rejeição anterior à seleção de location. Recursos ainda não criados; nenhuma saúde alegada.

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
- **Adherence review status:** findings_integrated
- **Adherence review evidence / resolution:** evidence/cp25-architecture-security.result.raw.json fresh gpt-6.1-sol/max, resolução local de D-01..10/REG-SEC-01..13; dois testes cp26 únicos diferentes no cp27 foram aceitos por suplemento TQA independente. Prova externa não dispensada.
- **No-go handling:** achado material retorna ao desenho/execução; nenhum gate é dispensado.

### Architecture adherence delta finding resolutions

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| NUM-ADH-CP36-01 | Integrated | useful | yes | project | D-03/D-05/D-07 | Fonte nullable por modalidade e fluxo PG segunda página/two-verify aceitos na revisão cp36c; raw original preservado. Novo P2 de catálogo separado e runtime pendente. |
| NUM-ADH-CP36B-01 | Integrated | useful | yes | project | D-03/D-05/D-07 | Busca dedicada limitada corrige primeira página, aceita por source+PG no cp36c; catálogo inconclusivo separado em NUM-ADH-CP36C-01. |
| NUM-ADH-CP36C-01 | Integrated | useful | yes | project | D-05/D-07 | Traduzir somente MetaIndisponivelError em verify para503/catalog seguro, com negativo BFF/PG e preservação/lease; correção cp36d pendente. |

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
- [x] Usuário acessou painel desenvolvedor e criou aplicativo com caso de uso WhatsApp; produto disponível. Isso não comprova autorização SDK, elegibilidade, WABA ou operação.
- [x] Operador criou configuração de Cadastro incorporado do WhatsApp com token de60dias e permissões management/messaging, informou Configuration ID e versão Graph `v26.0`; identificadores reais não entram em exemplos versionados. SDK/credencial/recebimento ainda não exercitados.
- [x] Reproduzir jornadas de cadastro oficial Meta e não oficial QR.
- [x] Usuário também quer Nova conversa proativa por contato: próximo ST-CON-04, antes de importação.
- [ ] Precondições da prova real: app Meta/configId/versão Graph suportada e elegibilidade, número/WABA, credenciais privadas, origem HTTPS e interlocutor de teste. Não impedem preparar código/contrato; impedem declarar prova real enquanto ausentes.
- [x] Reviews/guardas de planejamento e APROVADO do contrato3302964c antes da execução do produto; não substituem reviews/gates finais.

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

Comandos abaixo registram os wrappers efetivamente usados nesta topologia, com suas folhas de teste/build. O requisito externo continua bloqueante para entrega geral; `--require-delivery-gates` deve continuar no-go enquanto VAL-05 não passar.

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API light | Domínio/adapters/boot | Build, cifra, erros e config | Node22/OpenSSL3/container, lockfile e máscaras públicos | bash scripts/test-channels-local.sh all: prisma generate/lint/build/vitest | Local-Implemented | passed | cp27-final-all.log; cp27-handoff.json | 138unit/19files, produção não foi recriada; source-owned runner. |
| API E2E | Schema/auth/consumer | Negativas/replay/receipt, público/Typebot e races | PG16 exclusivo com22migrações | bash scripts/test-channels-local.sh all: test:e2e | Local-Implemented | passed | cp27-final-all.log PG286/26files; root-cp27-receipt.json | Execução serial antes do browser; fixture real de grants/tenant. |
| Web | Wizard/helper/DTO | Cadastro/cancelar/QR/races e casos antigos | BFF/sessão/PG reais e SDK/provider doubles | bash scripts/test-channels-local.sh all: build/test/test:tela | Local-Implemented | passed | cp27-final-all.log unit28/browser47; cp27-pre-worker-freshness.json; cp27-browser-attestation.json | Build atual e JSservido=dist antes workers; API3100/fixture3101/preview4173. |
| Workspace Compose | Runtime/wiring | Config/startup/isolation, origem/port e suíte consolidada | Projetos operador/validation próprios, dotenv privado preservado | scripts/start-channels-local.sh config/up; scripts/test-channels-local.sh all | Local-Implemented | passed | cp24-integrated-runtime-all-handoff.json; cp25-config-precedence-proof.json; cp25-https-runtime-proof.json; cp27 all | Wrapper atual incluído no manifesto cp27; config-only+APIrecreate cp25 prova precedência efetiva; sem valores privados. |
| Prova externa | Cadastro real | SDK/QR+IN+OUT/recuperação em cada canal | App Meta elegível, HTTPS e números/interlocutor de teste | runbook local e checklist VAL-05 | Local-Implemented | blocked | validation-plans/leadshug-channel-readiness-20261015.md; cp22-meta-panel-setup.json | cp32/cp33 comprovam QR/identidade/receipt e primeira IN/OUT não oficial. Recuperação autorizada em curso; OAuth/troca oficial ausentes, não dispensados. |

### Runtime / Rollout Notes

Local primeiro, via Docker Windows nesta sessão (Engine27.1.1 observado), Node22/PG16; nenhum serviço será tratado healthy só por inventário. Overlay channels mantém Evolution v2.3.7 por digest `sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`, Postgres/cache/volumes próprios da Evolution, rede com a API e nomes distintos do legado. O parser/adapter valida versão/payload antes da prova.

Gateway local usa imagem Web/Nginx já construída, config específica no workspace: serve /api,/webhooks,/ws para API, assets/UI para Web e /config.js com apiUrl vazio. Browser/callback partilham uma origem. Porta local dedicada configurável (padrão8083, pois8082 pertence a outro projeto); exposição HTTPS por mecanismo de operador, URL cadastrada/allowlisted no app Meta antes do SDK real; não inventar hostname, não alterar DNS ou abrir túnel persistente automaticamente. Registro de URL só sem segredo.

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

Conferência de implementação/prova local; não certifica OAuth, aparelho ou IN/OUT reais. Architecture/security cp21 examinou D-01..10; correções cp22/cp23 e revisão delta permanecem rastreáveis separadamente. Delivery continua Pending.

| Decision | Status | Evidence | Limit |
| --- | --- | --- | --- |
| D-01 | Adherent | number-registration.service.ts; number-onboarding-flow.e2e-spec.ts; cp32/cp33 BU/número próprios e primeira IN/OUT reais | Oficial e retomada ainda pendentes. |
| D-02 | Adherent | meta.client.ts; CadastroNumero.tsx; capabilities/options/confirm em number-onboarding.spec.ts; cp22-meta-panel-setup.json | SDK/provider doubles nos testes; OAuth real pendente. |
| D-03 | Adherent | tentativa/candidata/CAS em number-registration.service.ts; cp22-rerun3-result.json; RED/GREEN cp23 para NOVO expirado/ambíguo | Cp25 architecture/security e cp27 TQA suplemento aceitam; prova externa permanece separada. |
| D-04 | Adherent | channel-credential-crypto.ts/spec; channel-credential-resolver.ts; cp21 cutover/security; REG-SEC-06/07/12/13 | Dívida de dependências limitada ao operador privado, sem waiver externo. |
| D-05 | Exception | Mapper/503 seguro, classe+code e parser tipado cp36g aceitos nos loci pelo TQA; all530/freshness9. | TQA i terminal aceitou H01 e composição; final atual condicional por teste isolado de app_id estrangeiro ainda obrigatório antes do oficial. Prova oficial real pendente. |
| D-06 | Exception | cp32/cp33 QR/primeiraINOUT reais; cp49 SAMEEvolutionstop/start retomou automaticamente CONECTADO com novo connectedAt/identity/epoch/receipt/SAMEattemptv2, sem verify posterior | Falta humano INOUT02 e oficial real; FINAL01 cobertura app_id antes do oficial/entrega, sem dispensa externa. |
| D-07 | Exception | Páginas/grant inválidos e interseção WABA101 corrigidos/validados no all530, sem defeito de implementação observado pelo TQA cp36g. | TQA i terminal aceitou H01/composição; final condicional por cobertura D02. Recuperação e oficial reais continuam obrigatórios. |
| D-08 | Adherent | message-acceptance.service.ts; caller-scoping/Typebot/atendimento/public E2E; REG-SEC-01/02/11; cp33 primeira IN/OUT não oficial | Retomada e IN/OUT oficial continuam VAL-05. |
| D-09 | Adherent | scripts/start-channels-local.sh e test-channels-local.sh; namespaces próprios e provas HTTPS cp22; runtime cp24/cp25 e all cp27 | Railway/histórico/Nova conversa proativa não implementados neste recorte. |
| D-10 | Adherent | baselines e manifestos cp22/cp23; root-cp23-web-receipt.json; handoffs serializados e diff-cp23-pre-runtime go | Gitlinks observados, sem escrita manual; nenhum push de source. |

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Module Decision Ref | Handling | Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| integrations-and-channels#invariants | Preserve | Preserved | Mapper Meta tipado/fixo503 e negativo PG passaram cp36d; parecer fonte cp36d | Lacuna de asserção NUM-ADH-CP36D-01 separada; sem dispensa de TQA/final/recovery. |
| project_constitution#system-invariants | Preserve | Preserved | testes grants/caller-scoping/cifra/PG; máscaras/env e migrations do runner | Constituição não alterada. |
| inbox-and-conversations#contrato-aprovado-da-timeline-da-inbox | Preserve + aceitação compartilhada | Preserved | timeline.spec.ts baseline preservada; message-acceptance e atendimento E2E; cp27 browser47verde com freshness pré-worker | Inbox.tsx não alterado. |
| integrations-and-channels#cadastro-de-números-st-con-01 | Implement approved contract | Preserved | number-registration.service.ts; CadastroNumero.tsx; API cp22/Web cp23; cp27 all499 e TQA suplemento | Sem fallback global ou adoção Evolution legada. |
| identity-and-tenancy#autorização-do-cadastro-de-números-st-con-01 | Preserve | Preserved | sessão/anti-CSRF e acesso; REG-SEC-01/05/06/07; novaBU/grants E2E | Identificadores de SDK não concedem acesso. |
| audit-and-history#cadastro-e-diagnóstico-de-canais--st-con-01 | Preserve | Preserved | catálogo/cobertura; raw scoped e redigido REG-SEC-12/13; log hygiene cp21/cp22 | Histórico não apagado em cancelamento/repareamento. |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| cp36i source9/API461+Web/browserh | Test-only grant revogado válido-shaped, oito fontes idênticas e reuso histórico explícito | passed | cp36i-root-delivery-preflight.json; root-cp36i-validation/public-set-receipt.json; diff762/762go | Nenhum novo P1/P2 observado pelo root | TQA i aceito/final condicional terminal; API corrigida cp49 posteriormente servida; VAL-05 sem waiver. |
| cp36h source9/current535 | Test-only scalar/omission coverage, source8 unchanged, native transport guard | passed | cp36h-root-delivery-preflight.json; root-cp36h-validation-receipt.json; root-cp46c-receipt.json | Nenhum novo P1/P2 observado pelo root | Histórico h antes TQA i/final condicional; VAL-05 sem waiver. |
| cp36g source9/current all2 | Fences, grant shape/intersection, bounded network, typed mapper, fixture parity e honest evidence | passed | cp36g-root-delivery-preflight.json; diff expectation710/710 go | Nenhum novo P1/P2 observado pelo root | Histórico cp36g anterior ao TQA i terminal/final condicional; não equivale a runtime ou conclusão geral. |
| cp21 full + cp25 delta + cp27 TQA suplemento | Recuperação, índice, simulações e precedência de origem | passed | cp25-architecture-security.result.raw.json; round-02/performance.result.raw.json; cp27-tqa-supplement.result.raw.json; cp27 all | Todos bloqueadores locais registrados resolvidos | P1/P2 explícitos no cp25 independente; nenhum novo defeito de produção à época; delta atual tem final condicional separado. |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| cp36i contrato/fonte/evidência | Unitário sem RED falso, reuso browser por fonte idêntica e nenhum aceite externo por transporte | passed | cp36i-root-delivery-preflight.json; root-cp36i-validation/public-set-receipt.json | Nenhum novo bypass observado pelo root | TQA i aceito/final condicional terminal; nenhum all536/browser atual ou runtime corrigido alegado. |
| cp36g contrato/fonte/evidência | Falso CONNECTED, ausência por parse/truncamento, permissões/fallback e testes para passar | passed | cp36g-root-delivery-preflight.json; all2/freshness9; rawRED/firstall preservados | Nenhum novo bypass observado pelo root | Modelos externos/antigos runtime claramente separados; TQA/final ainda obrigatórios. |
| Tenant/credential/canonical cutover | Fallback global, recurso estrangeiro, bridge/adoption e falso CONNECTED | passed | cp25 security/cutover; REG-SEC-01..13; cp27 TQA suplemento | Nenhum bypass material estabelecido | Revisores independentes confirmam canonical credential/tenant/identity; VAL-05 continua obrigatória. |
| Evidência/runner/freshness | Harness rotulado como RED, mock de BFF, segredo no build e raw reconstruído como integral | passed | cp27 all/raw/manifests/attestations/root receipt; cp25 security; cp27 TQA suplemento | Mixed/test-after permanece dívida explícita; sem RED inventado | Raw integral cp24/cp27 e inventário antes all superam limite cp23; nenhuma história reescrita. |

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

Achados exatos preservados em planning-architecture.json. `fixed-in-plan` significa correção contratual, ainda sem código/prova; cada resolução será examinada na crítica independente e no harness após APROVADO.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| NUM-ARCH-01 | high | release-blocker | fix-current-contract | Typebot tocado exige isolamento tenant já canônico | verified-local | D-08; contratos de entrada; REG-SEC-01; VAL-08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ARCH-02 | high | release-blocker | fix-current-contract | Recebimento do cadastro não pode duplicar efeitos | verified-local | D-08; unique/transação; REG-SEC-02; VAL-08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ARCH-03 | high | release-blocker | fix-current-contract | Pareamento exige comprovar número antes do conteúdo | verified-local | D-06; rejeição pré-identidade; REG-SEC-03; VAL-08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ARCH-04 | high | release-blocker | fix-current-contract | Evento atrasado não pode trocar owner BU | verified-local | D-07; tombstone sem transferência; REG-SEC-04; VAL-08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ARCH-05 | medium | release-blocker | fix-current-contract | Pairing mutante exige POST/anti-CSRF | verified-local | D-06; contrato BFF; REG-SEC-05; VAL-08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ARCH-06 | medium | release-blocker | fix-current-contract | Reautorizar canal existente sem substituir ativa prematuramente | verified-local | D-03/04; candidata+CAS; REG-SEC-06/07; VAL-08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-CRIT-01 | high | release-blocker | fix-current-contract | Repareamento já prometido precisa invalidar prova anterior | verified-local | D-06; instância por epoch e trust reset; REG-SEC-10; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-CRIT-02 | medium | release-blocker | fix-current-contract | Dois writers da mesma Message precisam compartilhar aceitação | verified-local | D-08; message-acceptance e diff; REG-SEC-11; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-OBS-01 | medium | by-design/no-action | enforce-existing-requirement | Requisito secret-free já vinculante, sem defeito de gateway implementado alegado; harness concretizado | preserved-local | REG-SEC-12; runtime/logs; DOD-03; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-OBS-02 | medium | by-design/no-action | enforce-existing-requirement | Raw scoped já vinculante; batch por owner agora explícito, sem plataforma nova | preserved-local | REG-SEC-13; contrato raw; audit owner; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-OBS-03 | low | by-design/no-action | enforce-existing-requirement | Harness de tenant/credencial já requerido; observar identificador não secreto e DB real | preserved-local | REG-SEC-01/11; VAL-02/08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-DELTA-OBS-01 | low | by-design/no-action | enforce-existing-requirement | Fence até commit já exigido; barrier do webhook em voo concretiza BCI | preserved-local | Delta v3; REG-SEC-10, nota de execução; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-DELTA-OBS-02 | low | by-design/no-action | enforce-existing-requirement | Segredo em logs já proibido, inclusive hub.verify_token | preserved-local | Delta v3; REG-SEC-12, nota de execução; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-DELTA-OBS-03 | low | by-design/no-action | enforce-existing-requirement | Refresh já prometido projeta autoria/conteúdo do mesmo ID | preserved-local | Delta v3; REG-SEC-11, nota browser; Inbox excluído preservado; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-01 | high | release-blocker | fix-current-contract | Telefone canônico precisa CAS/equality atômico entre transportes | verified-local | api-checkpoint-review-v1.json; D-01/06; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-02 | high | release-blocker | fix-current-contract | Promoção deve manter attempt/generation/credential-version/lease até commit | verified-local | api-checkpoint-review-v1.json; D-03/04/06; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-03 | high | release-blocker | fix-current-contract | DELETE precisa adquirir o mesmo fence das operações externas | verified-local | api-checkpoint-review-v1.json; D-06/07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-04 | high | release-blocker | fix-current-contract | Renovação limpa antecessor mas não cria substituta reservada | verified-local | api-checkpoint-review-v1.json; D-06; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-05 | high | release-blocker | fix-current-contract | Mapping migrado não autoriza adotar/apagar instância externa | verified-local | api-checkpoint-review-v1.json; D-06/09; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-06 | medium | release-blocker | fix-current-contract | Retry QR pendente deve preservar rodada apesar de evento connecting/open | verified-local | api-checkpoint-review-v1.json; D-06/07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-07 | medium | release-blocker | fix-current-contract | Limpeza ambígua precisa sobreviver ao unlink e impedir nova criação | verified-local | api-checkpoint-review-v1.json; D-06/07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-08 | medium | release-blocker | fix-current-contract | Close observado deve remover prontidão atual de DTO/envio | verified-local | api-checkpoint-review-v1.json; D-07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-09 | medium | release-blocker | fix-current-contract | Verificação oficial sem telefone próprio não comprova identidade | verified-local | api-checkpoint-review-v1.json; D-01/07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-10 | medium | release-blocker | fix-current-contract | Expiração/supersessão/remoção devem limpar candidata e nonce | verified-local | api-checkpoint-review-v1.json; D-03/04; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-11 | medium | release-blocker | fix-current-contract | Replay concorrente same-key deve retornar a mesma tentativa | verified-local | api-checkpoint-review-v1.json; D-03; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-12 | medium | release-blocker | fix-current-contract | Audit administrativo já prometido não pode virar isenção técnica | verified-local | api-checkpoint-review-v1.json; audit-and-history#cadastro; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-13 | medium | release-blocker | fix-current-contract | Redação URL deve cobrir vocabulário de segredos e nomes codificados | verified-local | api-checkpoint-review-v1.json; REG-SEC-09/12; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-14 | medium | release-blocker | fix-current-contract | Ordem de locks identity/channel deve eliminar ciclo de deadlock | verified-local | api-checkpoint-review-v1.json; D-06/08; BCI; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-15 | medium | release-blocker | fix-current-contract | OUT sem ID confirmado conserva resultado local pendente/erro explícito | verified-local | api-checkpoint-review-v1.json; integrations-and-channels#reconciliação; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-16 | medium | release-blocker | complete-required-harness | Probes discriminantes REG-SEC e callers fazem parte do escopo aprovado | verified-local | api-checkpoint-review-v1.json; VAL-02/08; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-17 | medium | release-blocker | complete-required-harness | Positivas novas não são provadas pelos409 de rota aposentada | verified-local | api-checkpoint-review-v1.json; test/modulos e canais; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-API-18 | low | release-blocker | fix-current-contract | Metadata pré-identidade deve usar state allowlisted, sem conteúdo arbitrário | verified-local | api-checkpoint-review-v1.json; REG-SEC-03/13; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-RUNTIME-01 | high | release-blocker | enforce-existing-requirement | Provider fixado registra URL em falha de callback, expondo segredo no path apesar do gateway | verified-local | Concretizar alternativa por header já condicionada no contrato; fonte primária e prova runtime obrigatória; REG-SEC-12; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ROOT-META-01 | medium | release-blocker | enforce-existing-requirement | Capacidade oficial exige versão Graph explícita válida junto do conjunto Meta; vazio não pode anunciar AVAILABLE nem usar versão presumida | verified-local | Source read-only: meta.client.ts:42-51 aceita versão vazia se três campos Meta presentes; modulos.ts:61-65 só conta esses três; runbook/contrato exige GRAPH_VERSION informado pela instalação. Corrigir no próximo handoff API, com negativos unset/blank/malformed e positivo da versão configurada, sem nova aprovação material.; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-01 | medium | release-blocker | fix-current-contract | DTO antigo da mesma tentativa não pode regredir version/geração | verified-local | web-checkpoint-review-v1.json; D-07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-02 | medium | release-blocker | fix-current-contract | Popup precisa ownership para callback não perder code em busy no-op | verified-local | web-checkpoint-review-v1.json; D-02/03; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-03 | medium | release-blocker | fix-current-contract | Cadastro novo deve ser independente de retomada de tentativa alheia | verified-local | web-checkpoint-review-v1.json; SCOPE-01; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-04 | medium | release-blocker | fix-current-contract | Reinício de nonce usa BU já criada, sem duplicar novaBu | verified-local | web-checkpoint-review-v1.json; D-01/03; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-05 | medium | release-blocker | fix-current-contract | Cancelamento preserva explicação/resultado parcial durável | verified-local | web-checkpoint-review-v1.json; D-05; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-06 | medium | release-blocker | fix-current-contract | Verify consome receiptVerified booleano, não timestamp inexistente | verified-local | web-checkpoint-review-v1.json; SCOPE-05; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-07 | medium | release-blocker | fix-current-contract | Erros/status/finally antigos não escrevem após trocar contexto | verified-local | web-checkpoint-review-v1.json; D-02/07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-08 | medium | release-blocker | fix-current-contract | QR efêmero precisa vínculo/tentativa/geração corrente e limpeza ao concluir | verified-local | web-checkpoint-review-v1.json; D-06/07; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-09 | low | release-blocker | fix-current-contract | postMessage sem correlação não muda feedback de outra tentativa | verified-local | web-checkpoint-review-v1.json; contrato SDK; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-10 | medium | release-blocker | fix-current-contract | Loader SDK falho precisa retry controlado sem listeners obsoletos | verified-local | web-checkpoint-review-v1.json; SCOPE-02; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-11 | medium | release-blocker | enforce-existing-requirement | Recuperação parcial deve expor ação segura; leitura conclusiva condicionada a contrato real do provider, sem replay cego | verified-local | web-checkpoint-review-v1.json; fallback pending/nova autorização já explícito em D-05; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-WEB-12 | low | release-blocker | fix-current-contract | Parser de evento exige string enum primitiva, total para schema malformado | verified-local | web-checkpoint-review-v1.json; contrato SDK; aceite local cp21 full + cp25 architecture/security/cutover |
| WEB-ROOT-01 | high | release-blocker | fix-current-contract | SDK readiness perdido após reservar tentativa | verified-local | evidence/root-web-checkpoint3-findings.json; aceite local cp21 full + cp25 architecture/security/cutover |
| WEB-ROOT-02 | high | release-blocker | fix-current-contract | Consumo incorreto do wrapper registration da confirmação | verified-local | evidence/root-web-checkpoint3-findings.json; aceite local cp21 full + cp25 architecture/security/cutover |
| WEB-ROOT-03 | medium | release-blocker | fix-current-contract | Retomada persistida e cancelamento explícito necessários | verified-local | evidence/root-web-checkpoint3-findings.json; aceite local cp21 full + cp25 architecture/security/cutover |
| WEB-ROOT-04 | medium | release-blocker | fix-current-contract | Etapa no wizard precisa refletir webhook/receipt atual | verified-local | evidence/root-web-checkpoint3-findings.json; aceite local cp21 full + cp25 architecture/security/cutover |
| WEB-ROOT-05 | medium | release-blocker | fix-current-contract | Retry de reserva perdida precisa conservar chave idempotente | verified-local | evidence/root-web-checkpoint3-findings.json; aceite local cp21 full + cp25 architecture/security/cutover |
| WEB-ROOT-06 | medium | release-blocker | fix-current-contract | Troca explícita de WABA não pode perder opções autorizadas | verified-local | evidence/root-web-checkpoint3-findings.json; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-BROWSER-01 | medium | release-blocker | fix-current-contract | Submit repetido deve preservar owner ativo e coalescer reserva | verified-local | cp14 rerun3:21requests; FRC ativo; iniciar invalidava antes do guard; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-BROWSER-02 | medium | release-blocker | fix-current-contract | Cancelamento autoritativo antes de efeitos pode devolver channelId:null sem ser descartado como resposta obsoleta | verified-local | cp14 rerun5; API cancel370-373; DonoCicloCadastro.aplicar rejeita detach legítimo; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-BROWSER-03 | medium | release-blocker | complete-required-harness | Founder da fixture precisa proveniência MANTENEDORA para provar novaBU/replay conforme produto real | verified-local | cp14 rerun5:403TENANT_ADMIN_REQUIRED; seedNumberOnboarding119 vs TenancyService.criar; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ROOT-REG06 | high | release-blocker | fix-current-contract | REAUTORIZAR oficial no slot migrado sem credencial é prometido, mas guard managedLifecycle bloqueia o owner backfilled da mesma BU | verified-local | REG-SEC-06; number-registration.service.ts248,274,319; distinção da restrição de instância Evolution não gerenciada; aceite local cp21 full + cp25 architecture/security/cutover |

| NUM-ROOT-GW-01 | high | release-blocker | fix-current-contract | Nginx mantém segundo access log da imagem com URI/query e expõe verify token local; formato seguro isolado não elimina sink herdado | verified-local | cp21 scan real; REG-SEC-12; corrigir template, renovar token privado e repetir controles antes de HTTPS/pareamento; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ROOT-ENV-01 | medium | release-blocker | fix-current-contract | Overrides de origem/produção documentados não atravessam WSL para docker.exe sem bridge explícita | verified-local | cp21 HTTPS precheck detectou desenvolvimento/origem local; start script e README68; bridge WSLENV de variáveis não secretas e config-only discriminante; aceite local cp21 full + cp25 architecture/security/cutover |

| TQA-CP36C-01 | high | release-blocker | fix-current-contract | Erro público META_INDISPONIVEL não traduzido/provado no BFF | verified-local | cp36c-tqa.result.raw.json; mesmo locus NUM-ADH-CP36C-01, negativo BFF/PG e code unitário requeridos; merge recusou basename de dispatch, gate não aceito.  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |
| TQA-CP36C-02 | medium | release-blocker | fix-current-contract | Fixture browser lança Error genérico em vez da classe Meta e plataforma corrente não aceita | verified-local | cp36c-tqa.result.raw.json; alinhar classe do mesmo módulo dist nos ramos inconclusivos e preservar all falho; browser atual deve passar com freshness.  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |

| NUM-ROOT-GRANT-CP36G-01 | medium | release-blocker | fix-current-contract | Limite visual100 em wabaTargets truncava prova de pertencimento | verified-local | RED genuíno cp36g confirmou alvo101 ausente; reparo/interseção completa e options100 passaram all530, TQA cp36g não observou defeito de implementação. Casos G01h/H01i aceitos nos loci pelos TQAs completos; final/VAL05 permanecem obrigatórios. |
| CP46-LIFECYCLE-01 | medium | release-blocker | fix-current-contract | Rollback do novo túnel precisa conferir criação nativa atual/hash do supervisor/argv exato | verified-local | cp46c/rootreceipt: guardas native100ns/CIM1us/handles/exeSHA/argv/config/parent exatas, ValidateOnly passou e controle negativo rejeitou. Kill não executado; túnel preservado. |
| TQA-CP36H-01 | medium | release-blocker | fix-current-contract | Falta prova direta de grant estruturalmente válido com is_valid:false | verified-local | OpçãoA test-only cp36i/API173/288 aceita no locus pelo TQA i terminal completo/merge válido; nenhum produto novo recomendado. Não dispensa final/VAL05. |
| FINAL-CP36I-01 | medium | release-blocker | fix-current-contract | Falta negativa isolada de app_id estrangeiro com demais campos válidos | deferred-private-checkpoint-only | Guard produto correto/final sem defeito observado; owner Coder/Assurance deste TODO, UM teste recomendado obrigatório ANTES cadastro oficial real e Local-Implemented/DOD06/VAL06/closeout. Recuperação privada não oficial não executa Meta grant; sem claim de cobertura isolada/waiver/gate limpo. root-cp36i-final-adjudication.json. |
| FINAL-CP36I-R01 | high | release-blocker | fix-current-contract | D06/VAL05 reais permanecem obrigatórios | open | Integrated requisito externo vigente; fonte/candidata condicionais não certificam provider, API servida ou recuperação. |
| FINAL-CP36I-R02 | medium | by-design/no-action | enforce-existing-requirement | Reitera limite privado OWNER da dívida existente, locus inalterado | preserved-local | Integrated restrição existente e BLG-leadshug-runtime-dependency-security antes de usuários não confiáveis; nenhum upgrade novo ou dispensa. |
| FINAL-CP36I-02 | low | release-blocker | fix-current-contract | Resumos vivos ainda aguardavam TQA já aceito | verified-local | Integrated reconciliação atual das linhas de matriz/aderência/preflight/gates; raw/preflights históricos imutáveis. |
| TQA-CP36I-R01 | high | release-blocker | fix-current-contract | Prova externa D06/VAL05 permanece obrigatória | open | Integrated requisito já vigente; aceite favorável TQA e final condicional privados; API/recovery em execução, oficial real e teste D02 pendentes. Sem waiver. |
| TQA-CP36I-R02 | low | by-design/no-action | enforce-existing-requirement | Preservar composição honesta de freshness | verified-local | Integrated redação existente APIi173/288 fresca + Web28/browser47 h históricos de fonte consumidora idêntica; attestações originais intactas, nenhum all536/browser novo. |
| TQA-CP36H-R01 | high | release-blocker | fix-current-contract | VAL-05 real continua obrigatório para entrega geral | open | Integrated requisito já vigente D06/VAL05; readinesscp48 não substitui canal real. Mesma interrupção Evolution já autorizada pelo usuário, executar após gates locais, depois ação humana e prova oficial. |
| TQA-CP36G-01 | medium | release-blocker | fix-current-contract | Cobertura direta de scalars do grant e omissões legítimas | verified-local | Cinco casos h/all535/freshness9 aceitos nos loci por TQA h; H01 semântica is_valid:false separado e aceito no locus i. |
| TQA-CP36F-01 | medium | release-blocker | fix-current-contract | Formato inválido de grant Meta escapava como TypeError/500 | verified-local | Parser cp36g, RED159/8, all530 e TQA cp36g aceitam implementação tipada nos loci; cobertura G01h/H01i posteriormente aceita nos loci; final e VAL05 permanecem obrigatórios. |
| TQA-CP36E-01 | medium | release-blocker | fix-current-contract | Resposta Meta inválida pode virar ausência conclusiva | verified-local | cp36e-tqa.result.raw.json e merge válidos; reparar adapter e contrato BFF em cp36f.  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |
| TQA-CP36E-02 | medium | release-blocker | fix-current-contract | Falta assert da mensagem segura e mapeamento seletivo no BFF | verified-local | cp36e-tqa.result.raw.json; preservar erro não-Meta e invariantes em cp36f.  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |
| NUM-ADH-CP36D-01 | medium | release-blocker | fix-current-contract | Unitários do adapter precisam provar classe real e code na mesma rejeição | verified-local | cp36d-adherence.result.raw.json/merge; produção tipada correta, lacuna entre seams separados; reparo unit-only cp36e admitido antes da edição.  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |

| NUM-ADH-CP36C-01 | medium | release-blocker | fix-current-contract | Verificação oficial inconclusiva lança Error comum e vira500 genérico sem código de catálogo | verified-local | Parecer source-path adherence_cp36c: MetaIndisponivelError não HttpException, verify sem mapper, filtro Nest genérico; resposta não observada em runtime pelo reviewer. BFF503/catalog safe e invariantes requeridos antes do aceite.  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |

| NUM-ADH-CP36B-01 | medium | release-blocker | fix-current-contract | Verify oficial só consulta primeira página da WABA e rejeita número válido selecionado na segunda | verified-local | cp36b-adherence.result.raw.json/merge; cliente real e fake reproduzem caminho; all falhou287PG/1failed, sourcepathconfirma bloqueio anterior ao helper  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |

| NUM-ADH-CP36-01 | medium | release-blocker | fix-current-contract | Verify oficial repetido compara epoch legítimo null com epoch0 do canal | verified-local | cp36-adherence-security.result.raw.json/merge; helper/caller exige aplicabilidade explícita por provider e regressão PG real  Aceite do locus fonte/teste pelos pareceres cp36d/f e evidência513; novo gap grant e recuperação reais permanecem separados. |

| NUM-RECOVERY-CP36-01 | high | release-blocker | fix-current-contract | Tentativa corrente já CONNECTED pode causar ATTEMPT_STALE e rollback na reconexão/verify repetido | verified-local | Fonte/testes/PG/final loci e cp49 real SAMEEvolutionstop/start: novo automaticconnectedAt apósstart, CONECTADO/providerOPEN/currentidentity/genepoch1/receipt/SAMEattemptv2 e conversa2msgs preservados, sem postrestartadminverify. Root-cp49-runtime-recovery-receipt.json. HumanoINOUT02/oficial/VAL05 continuam separados e obrigatórios. |

| NUM-PERF-01 | high | release-blocker | fix-current-contract | Resolver de credencial carrega relação current_channel_id sem índice em cada envio; tombstones globais ampliam o scan | verified-local | Performance cp21-v2; novo índice schema/migration e EXPLAIN da consulta real; EPS foi aceito no review cp25 após correção; aceite local cp21 full + cp25 architecture/security/cutover; round-02/performance.result.raw.json, EPS aceito |
| NUM-ADH-CP21-01 | medium | release-blocker | fix-current-contract | Nova autorização após NOVO expirado/ambíguo mantém canal no backend, mas UI tenta NOVO em slot ocupado | verified-local | Architecture/security cp21; reutilizar canal exato por REAUTORIZAR e provar as duas falhas em browser real; aceite local cp21 full + cp25 architecture/security/cutover |
| NUM-ROOT-ORIGIN-CP24-01 | medium | release-blocker | fix-current-contract | Inicializador exporta origem default e sobrepõe HTTPS salvo no arquivo privado, quebrando configuração efetiva após rebuild | verified-local | scripts/start-channels-local.sh:14; corrigir precedência sem alterar arquivo privado e provar config/runtime HTTPS exatos; aceite local cp21 full + cp25 architecture/security/cutover |
| TQA-CP25-01 | medium | release-blocker | fix-current-contract | Spy realtime instalado depois do webhook antigo não observa o negativo exigido em REG-SEC-10 | verified-local | Instalar spy antes do ingresso antigo e conferir zero eventos; preservar demais negativos e aceitação atual; cp26-api-handoff.md / cp26-web-handoff.md; cp27 all499 e cp27-tqa-supplement.result.raw.json aceitam a negativa exata |
| TQA-CP25-02 | medium | release-blocker | fix-current-contract | Recuperação testa projeção coincidente, sem provar rejeição de canal/geração/currentAttemptId alterado | verified-local | Novo caso browser real com tentativa concorrente e erro seguro, sem nova reserva/BU/canal; cp26-api-handoff.md / cp26-web-handoff.md; cp27 all499 e cp27-tqa-supplement.result.raw.json aceitam a negativa exata |
| NUM-SEC-CP21-02 | medium | release-blocker | fix-current-contract | Simulações exigidas REG-SEC-01/10/11 não discriminam todos os cenários nomeados | verified-local | Trigger global estrangeiro anterior; verify antigo através de RENEW verificado; sequência epoch/quarentena/retry e ecos OUT concorrentes; aceite local cp21 full + cp25 architecture/security/cutover |

Adicional de coerência do autor: envelope raw redigido e code/PIN transitórios explicitados, sem alterar modelo de autorização; REG-SEC-08/09.

Adjudicação do checkpoint API: parecer bruto imutável api-checkpoint-review-v1.json (SHA256 e44b11aed763a452afcf1786e04e30a2a1d91ae012e3d0bd743c0281322028ee), schema nativo validado,18 achados (5high/12medium/1low), leitura completa de68 snapshots atestada. Root aceita os18 para correção no contrato atual: todos correspondem a D-01..08, limites contra legado, audit/segredos ou harness já exigidos. Não há dispensa, nova capacidade, worker, outbox ou autorização de runtime legado. Severidade baixa de NUM-API-18 não reduz o requisito explícito de metadata allowlisted. Solução deve ser simples e coerente; executor reportará qualquer necessidade de path ou decisão material ANTES da edição. Etapa pré-consumer, não gate final: correção e testes discriminantes ainda pendentes. Web termina/paralisa primeiro; API é o próximo writer único. Root permanece em orquestração documental; produto fica com Operational/Coder e runtime com DevOps.

Adjudicação do checkpoint Web: parecer terminal web-checkpoint-review-v1.json SHA25650dbe11bdffa49fd042d09c9b9a652280cb472ac6d42d3e94feb71ca1b0b5622, schema nativo validado,12 achados (10medium/2low). Root aceita correções no mesmo contrato. Para NUM-WEB-11, aceita a lacuna de ação/explicação segura, mas não presume que existam campos/endpoints conclusivos de register/subscription: leitura deve ser comprovada por fonte primária e validação; sem isso vale a alternativa já aprovada de pending/nova autorização, nunca replay cego de mutação ambígua. Nenhuma criação de endpoint remoto ou alteração de callback alheio por conveniência. Executor Web propôs um helper tipado coeso de contexto/versão/operação, aceito como HOW dentro dos globs já autorizados; deve preservar avanços legítimos de geração/attempt pelo resultado da ação atual. Implementação Web aguarda stop da API, não há writers concorrentes. Browser discriminante real-backend e FRC continuam obrigatórios.

Concretização de freshness cp6: root observou que `timeline-freshness.ts`, composto pelo novo helper, tenta ler com `readFileSync` todo path de `git diff --name-only`, incluindo a deleção já admitida de `channels.service.spec.ts`. Isso impediria o browser antes dos workers. Admitido M exato nesse helper compartilhado para registrar deleções sem leitura e completar a proveniência pertinente, preservando todas as verificações existentes; não autoriza alterar assertions dos testes históricos nem afrouxar o guard de banco. Mesmo objetivo/contrato, sem nova aprovação material.


## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** cp27 histórico aceito; cp33 primeira IN/OUT não oficial confirmada. cp36d corrige o erro de verificação inconclusiva e a precondição do harness; validação/revisões atuais e retomada ainda pendentes. VAL-05 ainda exige recuperação e oficial, sem waiver.
- **Post-commit/push status:** source commits locais API f134bd11449a553e6f57e66cdc8fc71032151060, Web d33c82c26760c671d98cab6f3e7bfe5676122c69, workspace4bccdc4aa470d1166bc14a681d0008f242db2562; sem push de código. Foundation main será publicado pelo guard documental.
- **Next path/status action:** manter este TODO active/Pending até correção/reviews/recuperação e prova oficial VAL-05; wizard/messages configurados e primeira IN/OUT não oficial já comprovados, sem inferir demais marcos.

## Security Risk Assessment (Mandatory Before Delivery)

- **Risk level:** high
- **Gate decision:** required
- **Why this risk level:** OAuth, credential por cliente, popup/origem, webhook e grants mutáveis.
- **Attack surface in scope:** sessão+anti-CSRF BFF; callback SDK preso à operação atual, sem autoridade de postMessage; código/nonce de uso único; IDs não confiáveis; token cipher/AAD; scopes de caller.
- **Attack simulation decision:** required
- **Review evidence:** evidence/cp21-architecture-security.result.raw.json e evidence/cp25-architecture-security.result.raw.json (fresh independente gpt-6.1-sol/max) aceitam a correção de NUM-ADH-CP21-01/NUM-SEC-CP21-02/NUM-ROOT-ORIGIN-CP24-01 e avaliam individualmente D-01..10/REG-SEC-01..13, segurança, dívida, P1/P2 e Rule-Spirit. Nenhum novo defeito de produção estabelecido. TQA cp25 identificou duas provas negativas ainda pendentes, prevalecendo sobre parecer genérico favorável; cp26 implementou, cp27 passou e suplemento TQA independente aceitou ambas sem novo achado. Runtime/header/log/HTTPS têm evidência cp21..25; aparelho/OAuth/IN/OUT ausentes.
- **Residual security risk:** crypto não protege aplicação comprometida; credenciais não entram em raw webhook/audit, DTO, URL registrada, Playwright trace/screenshot ou artefato. URL Evolution só de configuração allowlisted; não aceitar URL livre do operador.

### Simulações de segurança — disposição local atual

Referências relativas ao pacote `artifacts/reviews/leadshug-number-onboarding-20261015/`. Casos controlados usam portas externas dobradas; BFF, autorização, PostgreSQL e browser são reais. Fonte/execução cp24 + revisão independente cp25; cp26 alterou somente dois testes; all cp27 passou499 e suplemento TQA fresh aceitou as negativas. Nenhuma simulação equivale a OAuth/aparelho/IN/OUT reais.

| Requisito | Prova discriminante | Disposição / limite |
| --- | --- | --- |
| REG-SEC-01 | number-onboarding-typebot.e2e-spec.ts: trigger GLOBAL estrangeiro mais antigo e próprio, bot/session/credencial/saída corretos; caller-scoping E2E | Aceito local cp25 security; sem early exit por sessão estrangeira. |
| REG-SEC-02 | webhooks.e2e-spec.ts e number-onboarding-message-acceptance.e2e-spec.ts: replay sequencial e10concorrentes×3 por provider, chave por recurso, sem ID e echo OUT; acceptance unit/PG | Aceito local cp21/cp25; uma gravação vencedora, sem exactly-once externo. |
| REG-SEC-03 | number-onboarding-flow.e2e-spec.ts:503pré-identidade sem conteúdo/efeitos,409ownPhone divergente e mesmo ID aceito após prova; LID adapter | Aceito local cp25; retry depende de reenvio, sem buffer/importação. |
| REG-SEC-04 | flow E2E: tombstone após remove, rejeita rebind outraBU e evento tardio; webhooks mixed batch | Aceito local cp21/cp25; owner imutável e reativação mesma BU. |
| REG-SEC-05 | flow E2E pair sem CSRF e contador zero; canais E2E GET405/sem provider e POST ADMIN | Aceito local cp21/cp25; nenhum side effect por GET. |
| REG-SEC-06 | flow E2E reautoriza slot OFICIAL migrado exato, reserva mesmaBU/nonce novo; browser NOVO expirado/ambíguo | Aceito local cp25; nova negativa de projeção alterada passou cp27 e foi aceita pelo TQA suplemento. |
| REG-SEC-07 | flow E2E ativa preservada após número errado/cancelar/expirar, concorrência de candidatas e lease stale | Aceito local cp21/cp25; CAS até commit, sem substituir ativa ao reservar. |
| REG-SEC-08 | safe-redaction unit/PG, envelope webhook fictício, raw/audit/DTO/log secret-free e pré-identidade metadata-only | Aceito local cp21/cp25; fixture pública não contém segredos reais. |
| REG-SEC-09 | crypto unit AAD/tamper/purpose/BU/attempt/version/key; browser code/PIN sem storage/URL/trace | Aceito local cp21/cp25; memória transitória/POSTHTTPS, backend cifra. |
| REG-SEC-10 | flow E2E verifiedX→heldverify→RENEW/trust reset→oldverify409→Yquarantine→X/current same-key; BCI webhook-in-flight/remove-recreate | Produção aceita cp25; prova realtime do evento de instância antiga adicionada cp26, passou cp27 e foi aceita pelo TQA suplemento. |
| REG-SEC-11 | atendimento/public/Typebot E2E echo-inside-send/sender-first/concorrentes; mesmoMessageID/createdAt/autoria, zeroIN/unread/bot; inbox refresh baseline | Aceito local cp25; sem alterar Inbox.tsx nem contrato timeline. |
| REG-SEC-12 | cp21 gateway/header/log probes, provider2.3.7 header200/403 e cleanup semQR; Meta challenge; cp25 HTTPS/cookie/CORS | Aceito local cp21/cp25; logs fictícios testam erro/parser/upstream; webhook validado pelo usuário, sem prova de aparelho. |
| REG-SEC-13 | webhooks PG batch Meta assinado com duasBUs+unknown/retired, raw particionado e assinatura original | Aceito local cp21/cp25; partes sem identidade não persistem conteúdo. |

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** OAuth/HTTP e DB em etapas, requests retriggerable e observações concorrentes.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-DATA-PATH-CHANGED | before_local_implemented | EPS-E2 | passed | bounded local sample; no SLO | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | passed | local BFF/provider doubles | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-DUPLICATE-SUBMIT-OR-REPLAY | before_local_implemented | BCI-E3 | passed | no external exactly-once | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-QUEUE-WORKER-REALTIME-CHANGED | before_local_implemented | RLS-E1 | passed | 30 reads; no capacity claim | none |

#### EPS
Lookup único por vínculo/tentativa e índice de expiração, EXPLAIN na tabela representativa; sem fan-out em listagem. Perfil EPS-SP-STRONG, aceitação EPS-A2; medição local e limites documentados. Evidência pcv-1: evidence/cp24-pcv-eps.json, SHA canônico0ff50fc581a9794bda7578ad443b8005ad22cb03cfe538ca41ba5337523ea737; reviewer real /root/performance_delta_cp25, round-02/performance.result.raw.json. Plano25tentativas legítimo SeqScan e resolver real2.000tombstones com IndexScan; nenhuma capacidade/SLO inferida.
#### FRC
Coalescer duplo clique; cancela contexto anterior, descarta versão velha; repetição forte20triggers×5, requests/in-flight e estado/draft observáveis. Perfil FRC-SP-H; FRC-A1. Evidência: evidence/cp24-pcv-frc.json, SHA canônico7e6840f35699772e6beac6beef7a08827eec05eaec023be27e75168d3497cf0f; reviewer /root/performance_delta_cp25. 5ondas×20triggers, uma reserva/onda e maxinflight1; resposta velha concluída sem regressão.
#### BCI
CAS na tentativa, unicidade de slot/providerID e geração;20operações sobrepostas×5 com barriers para criação, finalize/replay e delete/recreate, controle negativo. Perfil BCI-SP-H; BCI-A1. Evidência: evidence/cp24-pcv-bci.json, SHA canônico00fa30af912e534ef44bfd6adf5689a3b11bf6c703c09dbd29d60f6e0f5932bf; reviewer /root/performance_delta_cp25. 5×20create/finalize e5×20pair/delete, barriers/readbacks/negative controls reais PG. Sem exactly-once de provider afirmado; timeout externo ambíguo fica pending.
#### RLS
Uma etapa bounded com cinco clientes e seis leituras por cliente,30verificações internas/conflitos, zero chamada provider em listagem. Perfil RLS-SP-L; RLS-A1. Evidência: evidence/cp24-pcv-rls.json, SHA canônico13c460ca03989bd3e66dbe8027ad9bb5cd2b9e3bca4e8bbd7635316f3a16b56b; reviewer /root/performance_delta_cp25. 5clientes×6leituras,200own/404foreign e zero provider em listagem, contador calibrado. Não é benchmark de capacidade/SLO; provider real não recebe carga sintética.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

- **Audit outcome:** high
- **Why this outcome:** auditorias históricas cp21/cp25/cp27 preservadas; TQA i terminal favorável, final i condicional e commits locais9 byteexact. FINAL-CP36I-01 permanece obrigatório no MESMO TODO antes do oficial/entrega; VAL-05 externo também impede fechamento. Checkpoint privado não oficial não é final limpo nem dispensa.
- **Inline code TODO debt:** none
- **Evidence / audit artifact:** delivery-audit-cp21-v2/round-02/resolution.md; cp25-architecture-security.result.raw.json; cp27-tqa-supplement.result.raw.json; root-cp27-receipt.json. Final review local aceito; VAL-05 e entrega geral ainda não satisfeitos.
- **Accepted residual debt:** FINAL-CP36I-01 apenas no checkpoint privado não oficial; permanece release-blocker do MESMO TODO antes de etapa oficial real/Local-Implemented/DOD06/VAL06/closeout, owner Coder/Assurance, teste direto e refresh de gates obrigatórios; não dispensa definitiva. TQA-CP21-02, proveniência mixed/test-after preservada sem RED histórico fabricado, owner executor/revisor deste TODO; BLG-leadshug-runtime-dependency-security, restrita ao operador privado e devida antes de usuários autenticados não confiáveis. VAL-05 externa continua requisito obrigatório, não dívida aceita para dispensá-la.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Audit decision:** required
- **Why this decision:** big/cross-stack, OAuth/tenant/runtime/testes.
- **Package mode:** bounded-file-set
- **Audit isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; distinto do executor, aguardar terminal sem deadline arbitrário.
- **Audit status:** findings_integrated
- **Findings summary:** TQA h terminal raw17e5a2e7.../merge válido aceitou evidência535/5casos anteriores e não observou defeito de produto; H01medium novo teste direto de grant revogado Integrated para cp36i test-only. R01 mantém VAL05 já obrigatório. TQA i terminal favorável confirmou H01 no locus e composição fonte9; root aceitou somente gate privado de fonte/testes. R01 mantém requisito externo e R02 preserva redação de reuso honesto. Candidata cp47 conferida/final terminal condicional; API-only/retomada cp49 em execução. FINAL-CP36I-01 obrigatório antes oficial/entrega; sem waiver.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015
- **Canonical multi-lane audit protocol:** audit-protocol-triple-review
- **Waiver authority / reference:** n/a

### Test quality finding resolutions

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| TQA-CP36I-R01 | Integrated | useful | partial | project | VAL-05 | Requisito externo mantido aberto/sem waiver; aceitar somente fonte/testes privados agora e continuar final/API/recovery oficial real. |
| TQA-CP36I-R02 | Integrated | useful | yes | project | evidence-freshness-composition | Preservar ambas attestações h originais e reuso explícito; não há all536/browser novo ou APIi servida. |
| TQA-CP36H-01 | Integrated | useful | yes | project | D-05/D-07 | Acrescentar caso dedicado is_valid:false com todo grant restante válido, classe+code mesma promise,1debug/authhost e zero lookup; produto correto sem RED artificial. |
| TQA-CP36H-R01 | Integrated | useful | no | none | none | VAL05 já obrigatório e não dispensado; mesma interrupção local explicitamente autorizada antes, nenhum novo pedido de permissão para repeti-la após gates. Oficial/humana ainda pendentes. |
| TQA-CP36G-01 | Integrated | useful | yes | project | D-05/D-07 | Acrescentar missing data/app_id não string/is_valid não boolean e sucessos de omissão legítima de scopes/target_ids; adapter real, classe+code mesma promise e contagemHTTP. Sem mudança de produto ou RED artificial. |
| TQA-CP36F-01 | Integrated | useful | yes | project | D-05/D-07 | Validar debug grant antes de iterar campos, rejeitar estrutura inválida com classe tipada; RED unit e representante adapter real/BFF/PG503 com invariantes em cp36g. |
| TQA-CP36E-01 | Integrated | useful | yes | project | D-07 | JSON inválido/data ausente ou não-array não provam ausência: corrigir adapter e provar classe/code mais BFF/PG503 e preservação. cp36f admitido antes da edição. |
| TQA-CP36E-02 | Integrated | useful | yes | project | D-05 | Fixar mensagem pública segura e comprovar que erro genérico não vira META_INDISPONIVEL; teste BFF com invariantes. |
| TQA-CP36C-01 | Integrated | useful | yes | project | D-05/D-07 | Mapper Meta tipado e BFF/PG negativo com invariantes; cp36d em execução, gate atual não aceito. |
| TQA-CP36C-02 | Integrated | useful | partial | project | D-05/D-07/D-09 | Classe real no double browser e nova prova browser/freshness; cp36c46/1 falho preservado, sem aceitar plataforma por inferência. |
| TQA-CP25-01 | Integrated | useful | yes | project | REG-SEC-10 | Spy antes do ingresso antigo, zero eventos; cp27 API286 e suplemento TQA fresh aceitam, sem mockClear mascarando observação. |
| TQA-CP25-02 | Integrated | useful | yes | project | NUM-WEB-11 | Sessão OWNER concorrente altera currentAttemptId; primeiro browser falha seguro semPOST/reset/BU/canal extra; cp27 browser47 e suplemento aceitam. |
| TQA-CP21-02 | Deferred | useful | partial | project | none | Dívida não bloqueante de processo mixed/test-after; owner executor/reviewer deste TODO, exigir RED autêntico em próximos defeitos; não fabricar histórico. |
| TQA-CP21-01 | Deferred | useful | no | project | VAL-05 | Fora do gate local: prova externa continua requisito obrigatório aberto para entrega geral, sem waiver ou aceite de dívida; próxima ação é teste real com operador. |

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Final review decision:** required
- **Why this decision:** big/cross-stack, OAuth/tenant/runtime/testes.
- **Package mode:** bounded-file-set
- **Final review isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; distinto do executor, aguardar terminal sem deadline arbitrário.
- **Final review status:** findings_integrated
- **Findings summary:** Final atual terminal rawSHA72612d92e48fb22d70214e6d869bc8c025f929947d31debe1a804db69831a474/schema/merge/binding válidos, completo9/candidata/rubrica. Sem defeito de produção/P1P2 observado, performance/elegância/estrutura aceitáveis. FINAL-CP36I-01 medium Deferred SOMENTE para checkpoint privado não oficial: cobertura isolada de app_id estrangeiro obrigatória neste TODO antes de cadastro oficial real/Local-Implemented/DOD06/VAL06/closeout, owner Coder/Assurance. Guard produto correto, caminho não oficial não usa Meta grant; nenhum claim de cobertura isolada ou final limpo. R01 externo Integrated/aberto; R02 limite privado existente preservado; 02docs Integrated. Root aceita condicionalmente fonte/candidata para mesma recuperação privada já autorizada, não entrega geral ou waiver. root-cp36i-final-adjudication.json.
- **Evidence / reference:** artifacts/reviews/leadshug-number-onboarding-20261015
- **Canonical multi-lane audit protocol:** audit-protocol-triple-review
- **Waiver authority / reference:** n/a

### Current final finding resolutions

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| FINAL-CP36I-01 | Deferred | useful | yes | project | D-02/app-audience-negative | SAME TODO/owner Coder+Assurance, antes cadastro oficial real e DOD06/VAL06/Local-Implemented/closeout. Guard produto correto por final independente, nenhum defeito observado; teste privado Evolution não usa Meta grant. Não alegar proteção de regressão isolada. UM caso direto e gates afetados obrigatórios antes do limite; sem waiver ou gate limpo. |
| FINAL-CP36I-R01 | Integrated | useful | partial | project | VAL-05 | Requisito real aberto/sem dispensa, mesmo teste de recuperação já autorizado e prova oficial ainda obrigatórios. |
| FINAL-CP36I-R02 | Integrated | useful | partial | project | BLG-leadshug-runtime-dependency-security | Restrição privada OWNER existente, backlog devido antes de usuários não confiáveis, locus/dependências não alterados. |
| FINAL-CP36I-02 | Integrated | useful | partial | project | current-gate-evidence-consistency | Root reconcilia resumos vivos ao TQA terminal aceito e final condicional, preserva exceções/VAL05/raw históricos. |

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** required
- **Why this decision:** credencial global é retirada; todos os consumers precisam convergir, sem shim/fallback.
- **Cutover audit status:** no_material_findings
- **Evidence / reference:** delivery-audit-cp21-v2/round-02/cutover-integrity.result.raw.json aceita delta/convergência local com zero achados, mantido na fonte cp27 com somente2testes diferentes; resolução round02 e suplemento TQA documentam. CUTOVER-EXT-01/VAL-05 mantém entrega geral Pending, sem waiver.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

n/a; sem claim Production-Ready ou promoção remota.

## Module Consolidation Gate (Required Before `Completed`)

- **Gate decision:** required
- **Gate status:** passed
- **Evidence / reference:** quatro módulos owner reconciliam implementação local exercitada e evidência cp27/reviews, com final atual condicional/FINAL-CP36I-01, closeout e VAL-05 pendentes explícitos. Contratos aprovados preservados, sem alteração constitucional ou claim de entrega completa.

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

Read-only de preparação pós-cp5a, sem executar testes: executor API identificou probes ainda necessários para o piso já contratado, sem exigir concentrar toda cobertura em um único teste. REG-SEC-02 tem duas duplicatas concorrentes no acceptance, faltam dez×três por transporte e efeitos downstream; REG-SEC-03 ainda precisa IN pré-identidade, telefone divergente e retry da mesma chave após prova; REG-SEC-04/13 precisam recurso desconhecido/retirado intercalado no batch assinado e lifecycle remove/rebind/evento tardio; REG-SEC-05 precisa ausência de CSRF com contador externo zero. Testes existentes cobrem partes desses contratos e serão preservados. BCI20×5 atual cobre create/finalize, não delete/recreate; EPS EXPLAIN/E2/A2 e RLS5×6/zero provider em listagem não possuem harness atual identificado. Integração pelo runner source-owned e handoff serializado à API ficam pendentes após preparo Web/runtime, sem fechar gates com esse diagnóstico. Novos probes cabem nos paths já admitidos `test/*number-onboarding*`; não são comportamento novo de produto.

### Checkpoint3 — preparação Web serializada

Após stop explícito do writer API com130unitários/234E2E, executor novo assume SOMENTE Web como único writer de produto. Review independente lê o pacote imutável API de68fontes, SHA256a5113ac1fd729cfc1ba902bc3b667b7b6c32818e4dbab9534028c00f5d50992a. API/fixtures/artefatos gerados/runtime não podem mudar nessa preparação; browser real-backend será integrado em etapa posterior serializada. Routing Web go e capability audit React/Vite ready, conforme manifests reais. Handoff detalhado: artifacts/reviews/leadshug-number-onboarding-20261015/web-handoff.md. Nenhuma entrega de UI ou gate geral reivindicados.

Checkpoint3 Web parado com build e23 testes/4arquivos passando; seis hashes conferidos. Revisão de fonte pelo root encontrou perda determinística de SDK readiness após reserva, ausência de retomada de tentativa persistida e falta de atualização da etapa por webhook. Achados aceitos como correções do contrato UI já aprovado, nos mesmos paths; executor Web recebe lote serializado de remediação, ainda sem editar API/runtime. Deve também conservar a chave idempotente em retry da mesma reserva quando a resposta é perdida. Provas de browser com backend real seguem pendentes, sem aceitar os testes unitários como substitutos.

Checkpoint4 Web encerrado com stop explícito, build e25 testes/4arquivos passando, seis hashes conferidos; correções de WEB-ROOT-01..06 implementadas aguardam prova de browser. Root aceita a remediação estrutural proposta para NUM-API-01..18 como execução do contrato atual, incluindo evidência de lifecycle managed separada de backfill e cleanup retido após unlink, conforme módulo owner consolidado. Handoff de volta a Operational/Coder: executor API reassume como único writer para schema/source/harness/fixtures nos paths já autorizados, routing-api-remediation.json go; Web e DevOps parados, sem escrita concorrente ou runtime externo. DoD/gates seguem abertos, nenhum achado marcado verificado por declaração do executor.

Concretização condicionada REG-SEC-12: inspeção do source primário Evolution2.3.7/cd800f2976e1e5b682fbf86a01ee4d85ae61f370 comprovou per-instance webhook.headers aplicado ao axios e URL impressa em falha de callback (webhook.controller.ts:69-122,124-136,217-243). O contrato já permite "Callback por header só se suportado e comprovado no provider fixado"; portanto concretizar POST /webhooks/evolution com segredo no header x-leadshug-webhook-secret e URL sem segredo, sem fallback de path. Mesmo segredo privado de instalação, mesma autenticação/capacidade/owner, nenhum serviço externo adicional ou privilégio novo. API implementa header no adapter e validação timing-safe do ingresso; rota antiga não aceita eventos. Todos os paths já previstos; testes/fixtures/catalogue/env correspondentes devem acompanhar. Fonte prova suporte, mas não comprova runtime: envio de header pelo provider fixado e logs reais sem marcador continuam gates obrigatórios antes de prova de aparelho. Não suprimir todos os erros do provider como substituto. LOG_LEVEL explícito sem LOG/WEBHOOKS evita impressão de QR/payload; QR permanece efêmero. Se runtime contradisser suporte/fidelidade, parar ativação e rever contrato, sem alegar prova antecipada.

Checkpoint5 API entregue parado: full unit130/19arquivos, full E2E262/25arquivos e atendimento focado25/25 após dois novos probes de lock, sem uma rodada completa na árvore final. Root verificou48hashes do manifesto final SHA2565dd04476f0f7f0bc992b329a15ccf970978d46ba7b092e4e6e226718ef12a335, mas o handoff imprime outro hash e20migrações em vez de21. Houve ainda delta de bytes em channels.service.ts após as validações, descrito pelo executor como whitespace; equivalência exata de EOF não foi reproduzida pelo root. Não há claim de alteração semântica nem aceite de frescor. Probe de auditoria por segundo ADMIN permanece aberto, e inspeção read-only Web identificou fallback indevido de code desconhecido para grant amplo no provider fake do browser. Root autoriza cp5a bounded nos mesmos paths: caso OWNER inicia/ADMIN distinto age depois, fake desconhecido fail-closed com controle negativo, metadados corrigidos em artefato novo e uma rodada build/lint/unit/E2E serial na fonte congelada antes/depois por hash. Não reescrever logs antigos, não expandir permutações infinitas de races. API reassume único writer; Web/DevOps continuam parados. DoD/REG-SEC/gates e prova externa seguem abertos.

Checkpoint5a API terminal conferido pelo root:48arquivos presentes correspondem ao inventário Git e hashes do manifesto b3d845d4f1e5597f45073fc3379a208a6dbb193309a410fdd26ca20212f610e0, mais a exclusão admitida de channels.service.spec.ts. Manifestos antes/depois são iguais; build/lint,130unitários/19arquivos e265E2E/25arquivos passaram,21migrações sem pendência. O novo teste OWNER→ADMIN distinto e o smoke de code desconhecido/grant restrito passaram. Isso autoriza continuidade do consumidor, não fecha REG-SEC/CI-equivalent nem readiness. Limitações confirmadas: runner sem CLI/libssl detectável gera aviso Prisma; montagem integral da API deixou `.env` privado visível a process.loadEnvFile/Prisma. Env fictício explícito e DB descartável não provam exclusão de outras variáveis privadas. A frase do handoff cp5a que afirma nenhum env privado usado está corrigida por esta adjudicação; original permanece imutável. Não há conteúdo privado inspecionado ou vazamento alegado. DevOps deve mascarar inputs privados, instalar OpenSSL e regenerar Prisma no runner source-owned antes da prova final. API parada; Web assume somente source/build/unit e fontes de browser nos paths admitidos, incluindo .dockerignore; runtime permanece parado até novo handoff serializado. Browser/PCV executam posteriormente pelo runner próprio, e root continua integração até concluir o trabalho independente.

Checkpoint6 Web terminal conferido pelo root:13hashes presentes correspondem ao inventário source, build e27unitários/5arquivos passaram; quatro arquivos TS browser/config apenas parseados. Handoff SHA25659f92491f597a573543a0ca70be5f9ca3525f0956490125f0af57baf6037c702, log7c60c2bda0e73844609233d20021fdbec007b6ef66931f9e0300e6f9f93b2b37. NUM-WEB01..12 implementados segundo executor, ainda sem verificação browser/review final. Cinco cenários Playwright preparados, não executados; tsc standalone e2e indisponível por falta de @types/node no Web, nenhuma dependência alterada. Writer Web parado; root transfere à Operational/DevOps, rotina gpt-6-luna/medium com routing/authority go, sem GOAL inferido. DevOps estabelece somente superfícies root admitidas e runner isolado, executa validação por suas folhas e devolve ownership ao coder diante de falha de produto/teste. Nenhum provider externo/HTTPS/QR real ou gate geral aceito.

Checkpoint7 DevOps parou: runner source-owned agora usa volumes-pai Linux com fontes/configs bind read-only da mesma principal, sem cópia/checkout auxiliar e sem mudar Nest. A primeira montagem direta de dist falhou EBUSY; retry passou lint/build. Relatórios cp7-api-first.json/cp7-api-retry.json declaram Node22.23.3,OpenSSL3.0.22,Prisma debian-openssl-3.0.x,hashes de packages/binds e máscara pública da dotenv,21migrações. Unit129/130 falhou no teste Meta que esperava v21.0 mas recebeu v-test do runner; API E2E,Web,browser e operador não executados nessa rodada. Os JSON são relatórios do executor, sem log bruto completo anexado, não prova final CI-equivalent. Root congelou8hashes de runtime em root-cp7-runtime-source.sha256. DevOps e Web parados; API cp8 recebe writer único após routing/authority go para corrigir NUM-ROOT-META-01 e completar harness já contratado, preservando testes existentes e capturando stdout bruto/manifestos na rodada final. Falha de runtime devolve ownership a DevOps; nenhum coder altera o runner para fazer testes passarem.

Conferência read-only posterior ao cp7: os volumes-pai omitem quatro inputs públicos rastreados (API docker/entrypoint.sh; Web Dockerfile,docker/40-config-js.sh,nginx/default.conf.template), a montar no próximo handoff DevOps antes do browser. `.local-files/` da API contém18payloads rastreados; a hipótese root de gitkeep era incorreta. Conteúdos não inspecionados e nenhum globalSetup browser executado. Esses dados operacionais não serão montados/lidos/hasheados/copiados/apagados/reconciliados. Freshness Web deve usar diff binário restrito por pathspec público, excluindo dados locais e env privados ANTES de ler blobs, mantendo código/test/schema/config e declarando a exclusão sem confundi-la com deleção real. Runtime/Web owners receberam essa fronteira para suas próximas ativações; API segue probes pelo runner atual, cujos inputs de compilação/teste públicos já estão montados. REG-SEC-11 cp8 também complementa público/Typebot com eco Evolution real autenticado dentro do send; uma cópia BFF literalmente idêntica em atendimento poderá ser subtraída mantendo a outra e suas assertions, sem reduzir cobertura.


### Checkpoint8 — API validada no runner isolado

API parou após `bash scripts/test-channels-local.sh api` concluir Node22.23.3/OpenSSL3.0.22, Prisma debian-openssl-3.0.x,21migrações,lint/build,137unitários/19arquivos e277E2E PostgreSQL/26arquivos. Log bruto `cp8-api-final-validation-final.log` SHA256 `7dabc94f190d2fb93cb0f0f8e4bb7936791615fa558f8312ccbdd9889f3920e9`; manifests públicos153paths antes/depois idênticos SHA256 `273442f47a1fc76ce723a20f17611349f649241c6084be0bc6aa22dfecf3a63d`, conferidos pelo root contra a fonte atual. Sem leitura dos payloads .local-files. `git diff --check` com convenção cr-at-eol passou; não normalizar CRLF por diagnóstico genérico. Relatório `evidence/cp8-api-handoff.md` e falhas intermediárias preservados. NUM-ROOT-META-01 tem testes unset/blank/malformed e request-level sem fetch; public/Typebot passam eco Evolution autenticado dentro do envio. EPS registra25tentativas,EXPLAIN e20timings; RLS5clientes concorrentes×6leituras teve calibração positiva do contador e delta zero em ambas as portas; BCI registra20pair/delete×5barreiras. São observações locais a revisar, sem SLO/provedor real ou gate final reivindicado.

Handoff após STOP: DevOps cp9 único writer root para4binds públicos, prefixos de colisão e Graph fixture válido; config-only/rawmanifest e STOP. Web permanece parado até essa entrega, depois assume freshness público/controles popup/WABA/casos faltantes e browser pelo runner. Root mantém documentação compartilhada. Sem init/start do operador nesta ativação curta. A correção de modelo Graph e esses probes concretizam o contrato existente, não ampliam a aprovação.


### Checkpoint9 — montagem pública completa antes do browser

DevOps parou após4binds públicos read-only, filtro de colisão aceitando hífen/underscore e Graph fixture v26.0. Sintaxe e config-only passaram sem criar recursos, conforme `evidence/cp9-runtime-config.json`; seis hashes declarados conferidos pelo root. Guard diff cp9 retornou GO256/256paths, zero proibidos ou não classificados (interim, não final). Sem browser/operador executado nesta etapa. Web cp10 ativado como único writer após esse STOP, mantendo API/runtime congelados; corrige diff público antes de Playwright, popup/WABA e casos de cancelamento/retry/contexto faltantes.


### Checkpoint10/11 — pré-requisito compilado do browser

Web cp10 parou após build e27unitários, com13hashes verificados pelo root. Freshness restringe o diff binário a paths públicos antes de ler blobs; popup abandon, WABA sem nome e cenários adicionais foram preparados. O browser aplicou21migrações/buildWeb e falhou antes de workers/globalSetup: timeline-fixtures.cjs exige crypto compilado em dist da API, ausente no volume limpo. Nenhum teste/attestation foi reivindicado. Raw e handoff cp10 preservados. DevOps cp11 único writer corrigiu o seletor browser para buildAPI prévio, sem duplicar no seletor all, e parou após syntax/config-only. Web cp12 foi ativado depois do STOP para alinhar os2Graph fixtures do Playwright e concluir a suíte; eventual alteração da ordem de bootstrap deve preservar buildfresh/DB/health/servedhash. Operador permanece não inicializado. Índice REG-SEC cp8 e contexto OWASP são inputs de revisão, não gates aceitos.


### Admissão de execução — teste legado da tela Números

O browser cp12 rerun1 mostrou falha real em `web-app/e2e/telas.spec.ts:391`: esperava botão Conectar WABA que o contrato aprovado manda retirar. Admitido M exclusivamente desse caso para provar BU visível, ausência de canal cadastrado e entrada no novo fluxo com modalidades explícitas; preservar todas as outras assertions e afterEach de erro/console. É concretização de teste consumidor do mesmo corte aprovado, sem novo comportamento/schema/risco ou aprovação material. Antes da edição, root comunicou o limite ao owner Web; só após terminal/freeze da rodada atual. Fixture API `browser-server.cjs:65` também força nome falso para WABA explicitamente null; correção pertence ao próximo writer API, nunca a um enfraquecimento da seleção explícita do teste.


### Checkpoint12 — execução parcial real do navegador

Após corrigir a chamada inválida test.describe.use, Playwright executou44testes:35passaram,2falharam e7do bloco serial de cadastro não executaram. Uma falha confirmou que o fake API trocava nome null por Fixture WABA; a outra era o botão aposentado no caso Números. A fonte Web atual14paths foi conferida por hash pelo root, mas inclui ajustes pós-run de FRC com espera da resposta retida/drain e JSON, SDKretry, autor/ID em refresh e teste Números admitido: não chamar esses ajustes de verificados. API cp13 recebeu writer único para corrigir só semântica null em browser-server.cjs; não mudar produto/asserts para contornar. Depois STOP e Web retoma. Pre-worker da fonte anterior preservado imutável em evidence/cp12-preworker-prior-source.json SHA2567531f261589ef8cf9236fd6d8c8d7ba60efa9f7f2bec98d1222d80f754ccc3f0; não prova fonte final. Log rerun1 SHA2565a79a960e53d715db0e1f2f1d4b786cb011fbaed28404dec6f60c088bf7f4e3c. Build/serviços reais subiram; nenhuma corrida do segundo build foi observada. Prova externa/gateway/operador permanecem pendentes.


Checkpoint13: fixture Meta passou a projetar name:null quando o nome é ausente ou explicitamente null, coerente com adapter real. Root verificou SHA2564379e94511e4d8c06e4dc6a232b85f29305c49863e17f2af639c39f4184c60e3 e os demais152paths cp8 idênticos; produto não mudou, mas a fonte total da API agora inclui esse delta de harness, a ser provado pelo browser/finalmatrix. Syntax-onlyNode22/diffcheck são relato do executor, não nova suíte. API parou; Web cp14 ativado após STOP.


### Checkpoint14 — falhas discriminantes do navegador e sincronização admitida

As rodadas preservadas `cp14-browser-validation-rerun2.log` (40/44) e `cp14-browser-validation-rerun3.log` (41/44) não fecham a suíte. O controle FRC passou a alcançar a resposta real retida e expôs 21 reservas para 20 eventos adicionais: `iniciar()` invalida o owner antes de verificar operação ativa. Corrigir o produto para coalescer a operação atual, preservando a barreira e a contagem. Recuperação de resposta perdida deve observar metadados seguros da resposta real e preservar replay válido com mesma sessão/key/payload; não substituir por cancelamento só para passar. Refresh da conversa precisa selecionar BU e aba do estado realmente persistido, mantendo o mesmo Message.id/conteúdo/autoria.

Admissão adicional estrita em `web-app/e2e/telas.spec.ts`, somente no caso “identidade visual carrega e salva os campos pós-onboarding”: a rodada rerun2 falhou no tema, e rerun3 passou sem mudança nesse caso. O teste atual clica Salvar e aguarda um heading que já estava visível antes de recarregar. A implementação envia PUT /api/bff/onboarding e atualiza /me de forma assíncrona. Admitido aguardar a resposta real desse PUT e comprovar sucesso/tema persistido antes do reload; manter todas as assertions de cores e tema e o afterEach. Sem sleep arbitrário, retry-only, mock BFF, mudança do produto de identidade visual ou edição de outros casos. Esta sincronização fortalece um gate existente da matriz aprovada, sem nova feature ou aprovação material. Web permanece único writer; runtime operador e revisões finais continuam pendentes.


### Fronteira do contexto Docker antes do operador

Inspeção read-only de `api-app/.dockerignore` mostrou exclusão de dotenv, porém sem `.local-files/` nem `.git`. O Dockerfile copia paths explícitos, mas isso sozinho não estabelece exclusão dos dados operacionais do contexto enviado ao builder. Admitido M exato nesse ignore, antes do build operacional, para excluir diretório de payloads e metadados Git que contêm seus blobs históricos. Não inspecionar dados nem alterar seu tracking. DevOps recebe essa superfície de build no próximo handoff serializado; produto API permanece congelado. Freshness final registra o novo hash público sem ler os paths excluídos. Não é ampliação funcional nem permissão para copiar payloads.


Diagnóstico cp14 rerun5: a resposta real do replay foi403/TENANT_ADMIN_REQUIRED, não nonce ausente. A fixture `seedNumberOnboarding` cria o OWNER com grant DIRETO; após nova BU, a regra canônica de herança só replica MANTENEDORA/SETOR, e esse ator perde administração derivada da Mantenedora. O fundador real de `TenancyService.criar` nasce com proveniência MANTENEDORA. Corrigir somente a proveniência do OWNER dessa fixture, preservando ADMIN/ATENDENTE diretos e seeds históricos; não relaxar autorização nem codificar reinício como substituto do replay válido. Handoff API serializado após STOP Web, nos paths já admitidos timeline-fixtures e number-onboarding-flow. Provar novaBU atômica+grant herdado, mesma tentativa/autorização no replay e contagem de BU sem duplicação. O403 continua evidência de que a autorização atual fechou corretamente para o ator parcialmente concedido.


Checkpoint14 Web STOP conferido pelo root:14hashes públicos correspondem ao manifesto `cp14-web-source-hashes.sha256` SHA2565ac633782a230fffa377be07a64aa73518a67b8dad66d299af03a67980e0d1be; build+28unitários passaram após correção de coalescing e detach de cancelamento. Handoff SHA2560fc9e5bb82af9966e5e5dc475791e075573449db161ce291482e48b20de817aa e log unit final a7dc078145418e252aabdae3486673d8cb26034d66d011d62833f62d1ab732a2. Último browser42/44 é ANTERIOR ao fix final de detach e continua falho, não gate aceito. Preworker rerun5 preservado como fonte anterior. Root transfere writer único à API cp15, somente fixture OWNER e regressão novaBU/replay nos paths já admitidos, syntax/diff/hash e STOP. A nova regressão será explicitamente não executada até o all integrado; não repetir a matriz API antiga sem mudança de produto. Depois Web recebe reteste do browser e DevOps prepara operador/all. Nenhuma prova de provider real foi inferida.


Coerência de source consumidor: o listener/parser postMessage sem correlação foi removido por subtração; a UI usa somente callback SDK ligado ao owner/attempt e seleção obtida no backend. A descrição owner foi alinhada, sem criar transportes/permissões. NUM-WEB-09/12 passam a ser examinados por ausência dessa superfície, não por alegação de parser ativo testado. Os gates finais ainda precisam avaliar a fonte e a prova atual.


Checkpoint15 API STOP: somente fixture OWNER e um caso PG novaBU/replay nos2paths admitidos; hashes ffbbb697205edbe9e076adf33f418d883339f40675f078479eccf704899ca62a e f22a48ec138978f6d09cb0eeb92ba9fc4ea5da416cfbd86d9c43ec4a5d8db12e conferidos pelo root. Comparação com o manifesto cp8 FINAL273442f... mostra somente3deltas públicos conhecidos: browser-server cp13 e esses2paths cp15;150paths iguais. Aquele manifesto inicial cp8-source-manifest-before é anterior às remediações e não baseline do gate final. Recibo root-cp15-fixture-delta.json registra a comparação sem dados operacionais. Syntax/diff passaram segundo executor; novo caso PG ainda não executado. Web cp16 é único writer para full44browser/FRC no runner próprio, com API/runtime congelados. Depois STOP e handoff DevOps; operador/all/reviews continuam obrigatórios.


Checkpoint16 Web STOP: suíte completa44/44 passou,21migrações, sem mudança de source desde cp14 final. Replay201 com mesma tentativa e autorização recuperável; FRC5×20 triggers, requests[1,1,1,1,1], max in-flight1 e resposta antiga concluída sem regredir cancelamento. Root verificou os14hashes Web e50paths alterados API da attestation pré-worker contra a principal; todos iguais. Log e36b8cd2176e9e9a4df63df28480fb772ce58c6bce0f3210f991c4dc559bd02e; preworker102ff86a05f74e8a11924cb6949e1fbdb414d9d96d19d21792cbdf31f7cbfb40; attestation de bundle servido b4be732e6aea45abb872acb8cf5ee149eb99e13c0df35727469ef8c4d4ecca63. Correção de metadata: os manifests standalone cp14/cp16 têm13paths e omitem Numeros.tsx; o preworker real contém os14incluindo esse arquivo, conferidos pelo root. A prosa anterior de14no standalone está corrigida pelo recibo root-cp16-browser-receipt.json, sem modificar provas antigas ou exigir reteste por erro documental.

Handoff Operational/DevOps cp17 ativado como único writer após ambos coders pararem: oito paths root e API.dockerignore exato; preservar produto/fixtures/UI. Deve executar build/start real do operador, bootstrap próprio pela API interna, gateway logs e prova de header Evolution sem QR, all integrado final e HTTPS temporário validado. Só então os gates independentes de entrega. Prova real Meta/aparelho/IN/OUT permanece pendência externa, sem ser certificada pelo44/44.


### Fechamento dos contratos REG-SEC-06/07/09 antes da matriz final

Diagnóstico read-only API confirmou NUM-ROOT-REG06: o contrato já aprovado permite reautorização de canal oficial migrado sem credencial, mas confirm rejeita managedLifecycle:false no mapping backfilled da mesma BU/slot, mesmo após nova autorização Meta válida. Corrigir somente o percurso OFICIAL REAUTORIZAR com owner local, canal e telefone exatos, ADMIN/sessão atuais e prova Meta fresca. Backfill sozinho continua sem confiança; só a reautorização explícita validada pode estabelecer gestão/prontidão pelo fluxo atual. Identidade de outra BU ou slot continua recusada antes de register/promoção. Não liberar adoção, verificação ou cleanup de instância Evolution legada/não gerenciada; não tocar runtime/dados do legado. Essa distinção concretiza D-03 e REG-SEC-06, sem nova permissão, schema ou feature.

Completar também as provas já prometidas: código consumido/resultado de troca ambíguo não dispara segunda troca e requer nova tentativa/nonce; candidata de outro telefone e cancelamento pós-autorização preservam o envelope ativo; AAD negativo para purpose/provider/BU/channel/generation/attempt e contexto ativo/version. Paths API de produto/teste já admitidos; usar controles positivos e negativos, sem criar plataforma de mocks. DevOps cp17 recebeu STOP no limite e conserva somente infra própria já iniciada. API só reassume após handoff terminal; depois validação pelo runner canônico e retorno DevOps para construir a fonte corrigida. Nenhuma matriz final/gate foi reivindicado pela descoberta.


Checkpoint17 parcial STOP: root conferiu todos os hashes declarados em cp17-partial-runtime-handoff.json SHA25697a7ca17e9c0c1fb66eadb47b270733a3540e18d9f46fb88fc6e3667543b93f8. API ignore exclui payloads/Git antes do build; README restaura submodules/CI e orientação de origens. Overlay prepara probe privado sem porta; script prepara bootstrap one-shot com lock/estado ambíguo. Esses novos caminhos ainda não foram executados. `.env.testing` foi criada exclusivamente com segredos/OWNER locais e DACL Windows restrita segundo executor, sem valores exibidos. Somente postgres/evolution-postgres/evolution-redis próprios e seus3volumes/rede foram iniciados, reportados healthy; conservar handles no handoff. Build API interrompido em npm ci, sem imagem concluída/migração/API/Web/gateway/bootstrap/probe/all/túnel. Não chamar runtime pronto.

Writer transferido à API cp18 após STOP, escopo produto/teste já admitido para NUM-ROOT-REG06 e REG-SEC-06/07/09. Validar pelo runner API e parar; Web e DevOps congelados. Docs são ownership exclusivo do root. Novo README/overlay/script e API ignore entram nos manifests e validação final, sem reutilizar fonte cp8 como se idêntica.


Checkpoint18 API parcial STOP:3fontes escritas (service, crypto.spec, flowE2E) e congeladas pelo root em root-cp18-partial-source.json; nenhum teste executado. O arquivo cp18-fail-first.log é falha de preflight Compose, não RED de produto: o probe de perfil inativo introduz interpolação obrigatória de EVOLUTION_WEBHOOK_SECRET, mas o env temporário fictício da validação não a fornece. A mensagem citar .env.testing não autoriza ler/adotar configuração operacional. DevOps cp19 assume somente correção desse env fictício no runner, syntax/diff/config-only e STOP, preservando infra/arquivo privado; API reassume testes depois. Não ocultar o bloqueio nem relaxar isolamento.


Checkpoint19 DevOps STOP: adicionou somente EVOLUTION_WEBHOOK_SECRET fictício ao env temporário da validação; config-only/syntax/diff passaram sem criar recursos ou tocar .env.testing. Runner4b051cb0f190c0d6e93ffda21c2635ba02b67a6fbf8ac6a2edc5636ba9918bd5 e artefato6b798e80a6e9505f826d413a0a1229fb765598b0045bd8f5b0bc5c9b22702859 conferidos pelo root. API cp20 recebeu writer único para prova de regressão reconstruída (guard antigo controlado, restauração exata) e full API final. Essa execução ainda não terminou; não interpretar arquivo de log em andamento como gate. DevOps/Web permanecem parados.


Usuário confirmou nesta retomada que preencheu os quatro campos Meta somente no arquivo privado local. Registrar apenas a confirmação de completude pelo operador; nenhum segredo foi solicitado no chat ou reproduzido em evidência. HTTPS, autorização SDK, assinatura de webhook real e conexão IN/OUT continuam sem comprovação. Preservar o arquivo e seus valores na retomada DevOps.

Checkpoint20: controle reconstruído do guard antigo alcançou o caso migrado e reproduziu a recusa; não é evidência test-first original. A primeira matriz final teve falha ECONNRESET no probe RLS. Executor identificou o listener temporário compartilhado do Supertest e fixou somente o harness PCV para app.listen uma vez em loopback/porta efêmera e app.close no encerramento, conservando cinco clientes concorrentes × seis leituras, autorização/escopo e contadores externos. Reteste completo em andamento; nenhum PASS geral até o handoff terminal.


Checkpoint20 terminal:21migrações/lint/build/138unitários19arquivos e282E2E PostgreSQL26arquivos passaram no runner canônico. Root conferiu cinco hashes finais declarados e três logs contra cp20-handoff.json SHA25682f554e866161460188e2479d316b1222fc084532c2699d7ac74202bba491e82. Recibo root-cp20-api-receipt.json distingue as provas e limites; manifesto cp20 é parcial em cinco paths, por isso o all integrado deverá capturar todos os inputs públicos pré/pós. API STOP; DevOps cp21 ativado após esse handoff como único writer nos oito paths root já autorizados. Antes do all, mascarar também os dotenv privados root com exemplo público sem tocar host; probe de transporte usa segredo fictício distinto e confirma remoção assíncrona de suas próprias instâncias. Preservar Meta privada e recursos operacionais. Nenhuma aceitação geral/produção ou conexão real reivindicada.


### Checkpoint21 em execução — runtime e bloqueio de logs

Retomada em2026-10-16 com writer serializado number_onboarding_devops_resume; agentes anteriores não estavam ativos. Executor reportou build operacional,21migrações, API healthy, Web/gateway e Evolution fixada iniciados, bootstrap único201 pelo endpoint interno. Gateway somente loopback8083. Provider probe sem QR comprovou header correto200/incorreto403 no receptor privado e remoção exata após DELETE. Esses sinais não provam pareamento nem IN/OUT. Artefatos e all final ainda pendentes.

A configuração efetiva Compose retornou booleanos false para os quatro campos Meta no arquivo privado root, apesar da confirmação anterior do operador. Pergunta assíncrona solicitou conferir o arquivo salvo exato, somente resposta de estado. Não ler/adotar outro arquivo privado por inferência e não modificar os campos Meta.

Scan real revelou NUM-ROOT-GW-01: um segundo access log herdado da imagem Nginx registrou request-target/query com o token local de verificação Meta. Nenhuma linha ou valor foi exposto no chat/artefato. Corrigir ambos os sinks no template já admitido, recriar gateway próprio, renovar somente WEBHOOK_VERIFY_TOKEN privado preservando ACL/demais campos e repetir controles positivos/negativos, parser e falha upstream com inspeção dos logs reais. Sem claim de ausência de segredo só pelo formato da configuração. Teto não oficial ativado prematuramente pelo executor foi revertido; nenhuma instância real/aparelho foi pareado. Habilitar novamente somente após a prova; all e HTTPS continuam seguintes, antes dos reviews independentes.


Atualização cp21: all canônico terminou exit0 com138unitários API,282E2E PostgreSQL,28unitários Web e44Playwright. Fonte/bundle, manifests e handoff terminal ainda serão conferidos antes dos reviews finais. Usuário localizou o arquivo, preencheu e salvou os quatro campos Meta; Compose efetivo confirmou quatro booleanos true, sem exibir valores. Após save atômico do editor, executor restaurou DACL restrita e renovou novamente o token local não cadastrado, preservando Meta e demais chaves; API healthy, novo challenge200 e anterior403. Provider-origin header200/403 e ingresso pelo gateway real→API200/403 são provas distintas, ambas realizadas com cenário descartável/sem pareamento.

Diagnóstico independente de dependências antes de HTTPS: evidence/cp21-dependency-exposure-diagnostic.json SHA25661afd41adb2cf1335be5fd2345449961db19029da9e98c96d2488c38045f7763, reviewer /root/dependency_exposure_diagnostic, routing gpt-6.1-sol/max go. Audit da imagem contém8pacotes afetados incluindo efeitos transitivos (1critical/6high/1moderate). O parecer não estabeleceu cadeia anônima dos advisories nesta configuração e não bloqueou o teste HTTPS temporário restrito ao OWNER privado/dados sintéticos. Multer2.2 mantém DoS autenticado concreto; registrar manutenção prioritária antes de usuários autenticados não confiáveis, sem upgrades neste TODO. Backlog BLG-leadshug-runtime-dependency-security captura owner/próximo gate. Numeric trust proxy=1 não executa a compilação de sub-redes afetada pelo alerta crítico; outros pré-requisitos e limites estão no diagnóstico. Não é aceite final de segurança/TQA/aderência nem claim de produção.


Concretização cp21 pós-all no mesmo script operacional admitido: o precheck HTTPS detectou que os overrides do processo WSL não alcançavam docker.exe. O operador foi configurado com valores privados e provou cookie Secure/origem exata, porém o comando público documentado também deve cumprir esse contrato. Admitido corrigir a passagem das quatro variáveis não secretas de runtime por WSLENV, preservando as entradas existentes e sem exportar segredos. Provar precedência por config-only com valores diferentes do arquivo privado e manter runtime real intacto. O all anterior continua prova da API/Web/runner inalterados; esse delta isolado de start script exige sua prova dirigida e manifesto final, sem alegar que precedeu a matriz. Nenhuma capacidade/risco/arquivo novo ou aprovação adicional introduzidos.

### Revisões independentes cp21-v2 e handoff cp22

Todos os leitores cp21 terminaram antes de nova escrita de produto. Performance gpt-6.1-sol/max, TQA e cutover gpt-5.6-terra/max nativos e architecture/security gpt-6.1-sol/max usaram pacote sem contexto herdado. Root conferiu32hashes do handoff runtime; resultados schema-valid preservados. Performance encontrou NUM-PERF-01; security confirmou NUM-ADH-CP21-01 e NUM-SEC-CP21-02. São correção de HOW/cobertura já aprovada, sem alteração D-01..10 ou nova funcionalidade. TQA aceitou cobertura local mas sua conclusão genérica REG-SEC fica limitada pela evidência específica de simulações ausentes do review security; completar os casos explícitos, sem alegar exploit reproduzido.

TQA-CP21-02 é accepted-debt de processo: cobertura final substantiva com proveniência mixed/test-after; não fabricar RED histórico. Owner executor/revisor deste TODO; revisitar em cada correção futura, começando pelo RED real da recuperação NOVO. TQA-CP21-01 e CUTOVER-EXT-01 reiteram VAL-05 conhecido: fora do gate estrito de correção local, mas continuam bloqueadores obrigatórios do fechamento geral; nenhuma dispensa ou aceite de risco substitui provider/aparelho real. Sessão delivery-audit-cp21-v2 está em resolução; próxima rodada será delta após correções, nunca repetição para redescobrir o gap externo.

FRC/BCI/RLS têm envelopes pcv-1 cp21-pcv-frc/bci/rls.json com reviewer independente real e hashes canônicos, baseados na amostra cp21 explicitamente aceita pelo performance; EPS não foi marcado passed. Tabelas/gates finais ainda serão reconciliados após nova fonte/validação;492testes não incluem as correções futuras. Meta4 presentes na API confirmados por booleanos; usuário confirmou domínio e URLs OAuth/SDK salvos. Webhook/cadastro real pendentes, sem publicação do app.

API cp22: schema acrescenta índice currentChannelId em migration nova e evidência de acesso real com população material; completar apenas simulações exigidas nos testes admitidos. Preservar21migrations já aplicadas, dados operacionais, credenciais, tombstones e contratos. Web tratará recuperação com REAUTORIZAR no slot retido e NOVO só se realmente liberado; DevOps atualizará runtime próprio/validação depois dos coders pararem. Nenhum commit/push de source ou deploy autorizado por esses reviews.

### cp22: validação parcial e recuperação do endereço temporário

API cp22 adicionou índice currentChannelId e migration20261016160000 em schema versionado;22migrações,lint/build e138unit passaram. PG284/286: novo teste OUT usa buId indefinido, e novo RENEW espera409 antes da rodada explícita de criação. completePairing termina primeiro a limpeza com200/CLEANUP_COMPLETED_RETRY_PAIR, preservando budget; teste deve conferir essa fase e continuar até quarentenaY/verifyX, sem reduzir exigência. Raw cp22-api-validation.log SHA2567bb87d0ab076bc70912907c2f83ad6b444fb067ede9fecca85f49695bbb12542; fonte/manifests215pré/pós e handoff preservados. Nenhum gate verde geral. API parou sem editar após a falha.

O usuário confirmou webhook vazio. Probe read-only encontrou PID12615 ausente e DNS do host QuickTunnel anterior indisponível em WSL/Windows; cp21 era prova histórica, não liveness atual. DevOps recebeu writer único para um processo Windows destacado com handles e filtro de saída antes de persistir, mantendo imagens cp21 atuais e configuração privada. Não reconstruir fonte cp22 não validada. Meta4/OWNER/chaves/token/ACL preservados; app sem publicar, nenhum dispositivo/número real conectado. Após HTTPS atual validado, usuário atualizará os3campos de allowlist junto do callback/token local, sem segredo em chat.

### HTTPS cp22 recuperado e API retomada

DevOps STOP e root verificou health200 após o encerramento do agente, PIDs WSL28234/28236 vivos e sete hashes do handoff. Processo Windows wsl.exe24396 mantém QuickTunnel com filtro que drena/descarte de saída e persiste somente hostname allowlisted; parent launcher já encerrou. Um primeiro attempt encerrou antes da prova e está registrado, sem host pronto alegado. Configuração privada de origem foi alterada em-place preservando Meta4/OWNER/chaves/token/ACL; API recriada --no-build/--no-deps na imagem cp21. SessãoHTTPS/cookie/CORS reais passaram. Operador segue21migrações;22somente no runner de validação. BFFcapabilities409ONBOARDING_PENDENTE não foi contornado nem houve alteração de módulo/cobrança. Usuário recebeu atualização agrupada do novo host e callback; resultado ainda pendente.

Normalização da execução: API aplicou indevidamente skill opcional orchestrated-single-todo-implementation sem invocação nominal e abriu trackerGOAL contra a instrução explícita. A skill foi considerada inaplicável; nenhum falso --goal-completed/waiver ou alteração de método. O tracker acidental disparou turnos repetidos aguardando o mesmo handoff externo e foi marcado blocked somente após ultrapassar três turnos, para cessar esse monitoramento. Isso não é estado do TODO. API retomada pela tarefa normal aprovada/routing/diff, sem criar novo tracker.

Usuário confirmou atualização dasURLs e validação do webhook pela Meta no novo host; cp22-meta-panel-setup.json registra confirmação humana do painel, sem OAuth, vínculo de número ou entrega de mensagem inferidos. Assinatura messages é próxima checagem manual. Reteste API encontrou uma expectativa incorreta de providerConnectionState: evento open pode observar conexão sem restaurar ownNumberVerified/verifiedEpoch/receipt ou status pronto; manter negativos de confiança/efeitos na dimensão correta. Nenhuma mudança de produto adicional estabelecida.

### API cp22 terminal verde; Web cp23 assume

Final cp22-rerun3 passou22migrações,lint/build,138unitários/19arquivos e286PG/26arquivos. Raw9aa7683bd56eccbe1407dd3ea2a1953ec78412cc6061d9c4ae543a298f562e39. Manifestos primários215 +15referências públicas suplementares pré/pós têm zero hash alterado; root conferiu230entradas atuais, incluindo apenas ausência aprovada do spec antigo. Índice currentChannelId escolhido em Index Scan real com2.000tombstones, uma linha retornada, sem planner forçado; resultado não é SLO/capacidade. REG-SEC-01/10/11 adicionais passaram com trigger global estrangeiro anterior, old-verify através da renovação/quarentenaY/provaX e ecosOUT concorrentes. Relatórios cp22-rerun3-result/handoff e root-cp22-api-receipt preservam fontes/limites. Falhas anteriores são de harness e ficam nos quatro rawlogs distintos; não representam novos bypasses de produto.

Web cp23 recebeu writer único para os dois cenários de recuperação do botão anunciado, com RED antes da edição do componente. Controle de expiração é test-only, scope attemptId+BU exatos, em fixture privada de DB descartável; troca Meta ambígua usa failures.meta.exchange, não ambiguousAfter. Nenhum envio real ou OAuth remoto inferido. Runtime próprio permanece imagemcp21/21migrações até ambos coders terminarem e novo build/prova.

Dois runs browser cp23 preservados comprovaram a falha real de recuperação após troca ambígua: reserva retorna409 em vez de201/REAUTORIZAR. Expiração ainda não chegou à asserção de produto: a fixture exigia UUID36 para attemptId, mas cryptoRandomId() de number-registration.service.ts gera32hex e substitui o default Prisma. Web, ainda writer único, recebeu ajuste test-only estritamente nesse guard de api-app/test/timeline-fixtures.cjs, já admitido no contrato; manter BU UUID, autenticação, DB descartável e todos os predicados de escopo/estado. Não alterar IDs do produto nem aceitar os dois runs como RED de expiração. Após corrigir o harness, capturar essa falha antes de editar o componente.

RED cp23 confirmado em cp23-web-red-confirmed.log, antes de editar o componente:44/46 passaram, somente os dois casos novos falharam com409/CHANNEL_SLOT_OCCUPIED e requestNOVO sem channelId na mesma BU. Expiração chegou a ERROR/EXPIRED com canal retido; controles sem header403 e BU estrangeira404 passaram. Quatro logs anteriores preservam problemas de harness/sincronização e uma falha intermitente no cenário existente Ana/grant, não reproduzida na quinta rodada; nenhum desses controles antigos foi relaxado. Web agora aplica recuperação por projeção fresca e canal exato; GREEN ainda não reivindicado.

### Web cp23 terminal verde; DevOps cp24 assume

Web parou após46/46browser no runner canônico, inclusive as duas recuperações201/REAUTORIZAR na mesma BU/canal/geração, e28/28unitários/build Web. Dois manifestos pré/pós independentes de230referências permaneceram iguais; root os conferiu contra a fonte atual e verificou os SHA dos logs RED e Web. Handoff cp23-web-handoff.md e root-cp23-web-receipt.json preservam a prova. O browser final foi observado na sessão48343, sem raw completo capturado; isso não será apresentado como log integral. O all integrado já requerido capturará raw completo e substituirá esse limite. A primeira rodada pós-fix falhou somente nos seletores dos dois novos testes, pois o botão correto se chama Reservar reautorização; a busca foi ajustada sem relaxar contrato/DB/nonce nem mudar o texto do produto.

DevOps cp24 recebe writer único para build/migration/runtime próprio e all integrado da fonte consolidada, com inventário público completo capturado ANTES do comando, comparação posterior e prova de bundle servido/attestation antes dos workers. Preservar túnel atual, Meta/OWNER/chaves/token/ACL, DB e volumes; não repetir bootstrap nem iniciar OAuth/QR por inferência. API/Web parados. Usuário também recebeu pergunta de estado sobre o wizard normal; nenhum onboarding ou módulo será contornado.

### Precedência da origem no inicializador cp24

Operator up terminou verde com22migrações e novas imagens. Probe HTTPS login/me passou com cookie seguro, mas WEB_ORIGIN efetivo ficou http://localhost:8083 e preflight da origem HTTPS não retornou allow-origin exato. Diagnóstico source: export default de CHANNELS_LOCAL_ORIGIN no inicializador prevalece sobre a origem salva no --env-file. Não alegar CORS exato nem tratar sucesso same-origin como prova dessa dimensão. NUM-ROOT-ORIGIN-CP24-01 é correção HOW do D-09 existente no path já admitido, sem mudar contrato, provider, dependência ou domínio.

Preservar all cp24 em voo e manifestos sem edição/interrupção. Depois, DevOps mantém writer único para corrigir somente precedência dos valores públicos do inicializador: override explícito continua prioritário; quando ausente, respeitar configuração privada salva e defaults do Compose, sem source/eval de dotenv nem segredo em stdout. Validar config-only de origem salva/override/default e porta salva/override, com WSLENV existente preservado; restaurar runtime HTTPS próprio e repetir sessão/CORS/health/log hygiene. Guardar delta posterior do script separadamente: all anterior continua prova dos229inputs inalterados e não será falsamente atribuído ao script final. Test runner/API/Web/migrations não mudam nessa correção; fullall só se novas falhas ou impacto justificarem.

All cp24 terminou exit0:138APIunitários,286PG,28Webunitários,46browser =498;22migrações; raw c7f2a6c70384bea881ba5106787b4a1911e8fdc763760e80a8a8eb34faa73277. Inventário230entradas/228paths únicos pré/pós iguais, capturado antes de build/all. Root conferiu11hashes do handoff e230referências atuais. O handoff não exportou attestation e declarou lacuna; root encontrou os arquivos genuínos gerados pelo globalSetup às15:16:12/15:16:15Z, dentro desse all e antes dos workers. Retidos byte a byte em cp24-browser-attestation.json/cp24-pre-worker-freshness.json, fonte/API/DB22migrações/portas e bundle conferidos. SHA JS d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd coincide com runtime HTTPS/imagem. root-cp24-receipt.json complementa a prova sem reescrever handoff ou produzir probe pré-worker retroativo. DevOps parou e foi reativado somente para cp25.

Cp25 terminal STOP: somente scripts/start-channels-local.sh mudou, SHA a8b7790f68da1154a85eb3108ac7b1365e9b1d881af21fe089620db881377de5;229referências públicas iguais ao all, heads iguais. Matriz real Compose provou saved origin/porta, override explícito, arquivo público salvo com porta18084 distinta de8083, defaults, WSLENV/modifiers e portas inválidas; sem mutação de recursos na config-only. Só API recriada sem build/deps, mesma imagem; todos os demais containers/volumes preservados. HTTPS health/root/login/me200, cookie seguro/host-only e CORS exato204 com credentials; configuração privada intacta por booleanos e nenhuma ocorrência de segredo nos logs inspecionados em memória. Capabilities409ONBOARDING_PENDENTE permanece. Root conferiu8hashes do handoff e230entradas atuais; fonte congelada para delta, sem declarar gates finais passados ou VAL-05 dispensada.

### Revisão cp25 terminal e duas provas negativas cp26

Performance6.1/max zero achados aceitou NUM-PERF-01 e quatro amostras PCV; root derivou cp24-pcv-eps/frc/bci/rls.json com hashes canônicos e identidade real do revisor. Cutover nativo5.6-terra/max zero achados; architecture/security6.1/max zero achados, com posições explícitas P1/P2 e Rule-Spirit. TQA nativo5.6-terra/max concluiu duas lacunas específicas de prova, aceitas como TQA-CP25-01/02: spy realtime precisa observar o webhook antigo e recuperação precisa provar projeção divergente. São testes de comportamento já correto, não exploits reproduzidos nem nova funcionalidade. Conclusão genérica favorável de outro lane não substitui esses negativos explícitos.

Todos leitores terminaram antes de retomar escrita. Remediação limitada aos dois paths de teste já admitidos: number-onboarding-flow.e2e-spec.ts e e2e/number-onboarding.spec.ts. API move/adiciona observação e para; Web acrescenta um caso com alteração legítima pela sessão concorrente no BFF real e para. Preservar produção, endpoints/fixtures, dois positivos e44baselines. Uma execução canônica all499 após ambas edições valida API/Web/novo negativo e inclui o inicializador atual, com raw completo, manifesto completo pré/pós e attestation. Não repetir suites parciais antes desse all sem falha concreta. Depois TQA fresh específico sobre os dois achados, preservando pareceres Performance/cutover/architecture sobre produção inalterada; sem novo round amplo só para zerar achados.


### Handoff cp27 — validação integrada após cp26

API e Web cp26 parados. Root conferiu hashes atuais dos dois testes e handoff Web; somente duas alterações de testes desde cp25. Perfil Operational/DevOps, Gate0 Genesis rejeitado pois contrato e runtime já existem, routing-cp27.json go. DevOps assume rodada única canônica all; expected499 é previsão, não resultado. Reter manifestos completos antes/depois e arquivos genuínos gerados antes dos workers, sem recriar operador ou modificar credenciais. Revisão TQA específica e final review ficam pendentes dos resultados.

### cp27 — prova primária integrada aceita

Uma rodada canônica `bash scripts/test-channels-local.sh all` saiu0:138unitAPI+286PG+28unitWeb+47browser=499,22migrações. Raw completo cp27-final-all.log SHA256da8b5f823300db161ecfffa8204a6fb6f98792f551f8528c5398f353950c60d5. Root-cp27-receipt.json confere230refs/228unique, delta exato de2testes desde cp25, manifestos pré/pós idênticos,7hashes de artefato,66entries do freshness incluindo deleção admitida e JS servido=build d1434360… antes dos workers. Preworker genuíno16:06:54/57Z, não probe retroativo; produção/operador intactos. API/Web/DevOps STOP. TQA suplemento fresh específico e final review continuam obrigatórios.

### cp27 — TQA suplemento aceito e consolidação local

Native fresh gpt-5.6-terra/max terminou exit0/turn.completed, schema válido; raw SHA2568bf9f15e70410cfb48a9504914f4f69c15d160b7c7cf1fab4885f7b921e43ccc. Aceita TQA-CP25-01/02, sem novo achado. Merge e round02 resolution=resolved preservam relatórios originais. Matriz25critérios,64findingrows,13REGSEC,PCV4/segurança/dívida/P1P2/RuleSpirit e módulos owner reconciliados com evidência local e limites. Final_review fresh distinto e commits/guardas locais continuam pendentes. Não abrir novo audit amplo para zerar histórico. VAL-05 obrigatória; TODO Pending.

### cp27 — final review local, fonte commitada e handoff externo

Final_review fresh /root/final_review_cp27 gpt-6.1-sol/max terminou sem achados adicionais e aceitou o checkpoint local, sem exigir nova suite ou auditoria. Raw ecb944f247b1226bd1a5b88557980e34c26a331d43b7af0e0b54e7b6c1c01343, schema/merge válidos; root integra o aceite. Após STOP de todos leitores atuais, commits locais de trabalho API f134bd11449a553e6f57e66cdc8fc71032151060, Web d33c82c26760c671d98cab6f3e7bfe5676122c69 e workspace4bccdc4aa470d1166bc14a681d0008f242db2562. Cada commit teve guard go, index explícito52/14/8paths públicos, whitespace check e bytes staged/committed iguais ao manifesto cp27. Bridge preserva heads antigos da execução; não afirma que499 rodaram nos novos commits. Sem payload operacional/.local-files, gitlinks, push de source, deploy ou mudança runtime.

Checagem read-only do executor às16:30:49UTC confirmou gateway8083 e HTTPS configurado / e /health200, sem ler corpos/headers/private config ou mudar runtime. Isso prova alcance naquele instante, não pareamento. Messages e wizard continuam sem resposta; API não foi contornada. TODO active/Pending, requisito VAL-05 sem waiver e guard de entrega deve continuar no-go pelo único requisito externo.

### cp28 — confirmação humana de prerequisites e readiness autenticada

Em2026-10-16 o operador confirmou campo messages inscrito no app Meta e configuração inicial realizada no LeadsHug. É confirmação humana, não prova de subscribed_apps da WABA, OAuth, pareamento ou IN/OUT. Perfil Operational/DevOps, escopo Docker/NestJS/React/PostgreSQL; Gate0 Genesis rejeitado pois contrato/runtime existem, routing-cp28-readiness go. Executor sticky DevOps faz somente health/login normal/me/onboarding/capabilities/business-unit summaries em memória, sem expor credenciais/telefones/QR/cookies e sem mutar fonte/runtime/configuração/provedor. Root mantém canon; resultados cp28 ainda pendentes. All499 e reviews finais já aceitos permanecem, sem rerun por confirmação de setup.

Resultado cp28: loopback8083 responde200; hostname HTTPS salvo falhou DNS antes de qualquer login, sem cookie/sessão ou credencial transmitida. Onboarding/capabilities autenticados ainda não observados. DevOps cp29 recebe recuperação bounded do mesmo HTTPS temporário: diagnosticar DNS WSL/Windows e processo próprio com proteção de PID reuse; somente se irrecuperável iniciar uma QuickTunnel efêmera para o gateway próprio, sem infra persistente nem mudanças de origem/config privada até handoff ao root. Fonte/runtime de aplicação preservados; prova externa segue pendente.

Cp29 terminal conferido pelo root: hostname novo operating-brussels-internship-interviews.trycloudflare.com resolve WSL/Windows e /,/health200 em ambos; alvo único127.0.0.1:8083, binário fixado2026.10.0/SHA d33ff2d1… e processo Windows29132/supervisor77581/cloudflared77593 vivos. Túnel antigo estava vivo sem transporte, hostname público NXDOMAIN; causa desconhecida. Encerrado por guard de identidade após provar o novo; somente um cloudflared próprio ativo. Root conferiu4hashes de artefatos; cp29 não mudou app/API/env. Cp30 autorizado somente CHANNELS_LOCAL_ORIGIN e APIrecreate sembuild da mesma imagem, preservando segredo/ACL/volumes e outros serviços, seguido de sessão/onboarding/capabilities redigidos. MetaURLsnovas solicitadas ao operador, resposta pendente.

### cp30 — origem/sessão recuperadas e esclarecimento do operador

Root verificou SHA256 dos2artefatos cp30. Origem nova efetiva/prod válida, apenas CHANNELS_LOCAL_ORIGIN alterada; outros bytes privados/Meta4/OWNER/chaves/tokens/PUBLIC_ORIGIN/ACL preservados. API apenas recriada sem build e com a mesma imagem c2e8d62b…; outros6containers/5volumes intactos. HTTPS root/health WSL/Windows200, um login OWNER200, me200, cookieSecure/HttpOnly/Lax/host-only e CORS204/origemexata. GETonboarding200 mostra complete=false, módulo WhatsApp não oficial oferecido mas desligado; capabilities e BU409ONBOARDING_PENDENTE. Nenhum onboarding/contratação/provedor/QR executado pelo agente.

Operador confirmou depois novo domínio/OAuth/SDK/callback Meta salvos e webhook validado; esclareceu que não havia feito o wizard em nenhuma conta, havia esquecido. Isso resolve a divergência como etapa humana pendente, sem defeito de produto demonstrado. Root leu Wizard.tsx/OnboardingService: Continuar muda o formulário local; só Revisão→Concluir faz o POST normal e persiste onboardingConcluido. Próximo passo humano enviado com seleção normal de WhatsApp não oficial; sem bypass/reset/seed. Fonte permanece nos mesmos3commits locais, sem nova suite/auditoria por mudanças apenas operacionais/documentais.

Correção de destino de artefato: cp30 foi emitido em root/artifacts/reviews/...; root identificou antes de qualquer delivery/Git claim, conferiu hashes e moveu somente os2arquivos próprios byteexact para Foundation/artifacts/reviews/.../evidence. Diretórios vazios removidos, demais arquivos preservados. Ruído operacional corrigido, nenhuma expansão de escopo ou mutação de código; handoffs seguintes usarão destino absoluto Foundation. Relatórios originais e confirmação humana cp28 preservados como histórico, esclarecidos por cp30-operator-setup-clarification.json.

### cp31 — conclusão humana do wizard e readiness pré-dispositivo

Operador confirmou clique em Concluir e abertura da tela principal. Perfil Operational/DevOps, Gate0 Genesis não se aplica; mesmo contrato NestJS/React/Vite/PostgreSQL/Prisma/Docker. Routing-cp31-readiness go, único executor em checagem autenticada somente leitura e fingerprint do JS servido comparado ao build validado antes de qualquer nova evidência de dispositivo. Não criar reserva/QR/onboarding/módulo por agente; próximo passo da UI dependerá dos estados efetivamente observados. Root mantém canon. Nenhuma nova suite ou fonte necessária por essa conclusão humana de setup.

Root conferiu hashes dos artefatos cp31 e o resultado autenticado: root/health/login/me/onboarding/capabilities/BU200, onboarding complete=true, módulo não oficial habilitado, ambos cadastros AVAILABLE, uma BU/zero canais. Cookie efêmero Secure/HttpOnly/Lax/host-only. JS público d1434360… igual ao asset do container e cp27 validado, capturado antes da próxima prova humana; fontes/imagens permanecem aceitas. Sem mutação de fonte/runtime/configuração, provedor, OAuth ou QR pelo executor. Handoff UI enviado ao operador para reservar tentativa não oficial, parear aparelho e verificar identidade/recebimento; não enviar primeira IN antes da identidade confirmada. Nenhuma conexão real ou VAL-05 certificada por esta leitura. Evidências: cp31-operator-readiness.json/.md e root-cp31-receipt.json.

### cp32 — pareamento humano não oficial e precondição da primeira IN

Operador relatou identidade própria confirmada, provedor conectado e recebimento pendente após fluxo QR/Verificar identidade e recebimento. Nome/telefone informados não são retidos nos artefatos. Confirmação humana sanitizada em cp32-operator-pairing-confirmation.json; leitura autenticada/estado do epoch e bundle pré-IN em curso. Operational/DevOps, escopo NestJS/React/Vite/PostgreSQL/Prisma/Docker, mesmo contrato; routing-cp32-readiness go, executor sticky limitado a leitura sem chamadas externas/provedor/QR ou mudanças de fonte/runtime/configuração. Root mantém canon. Não inferir IN/OUT, recuperação, histórico ou conclusão geral do rótulo conectado.

Leitura cp32 confirmou um canal não oficial, ownNumberVerified=true, pairingEpoch=verifiedEpoch=1, geração da tentativa/epoch atuais e único mapping ativo da mesma BU/canal/instância. Provedor CONNECTED, status CONECTANDO e receipt ausente. Baseline scoped à BU obtido antes da orientação humana: zero conversas, zero IN, zero OUT. Root orientou envio sintético a partir de OUTRO WhatsApp de teste para o número conectado, leitura em Atendimento e resposta pela mesma conversa, com confirmação no aparelho interlocutor. Não há prova IN/OUT até retorno humano e readback. Fingerprint cp31 já precede QR e testes; quaisquer novas checagens de bundle após a orientação devem conservar timestamp real, sem rotulagem retroativa como pré-IN.

Root conferiu hashes cp32 e aceitou prova limitada do pareamento atual. Baseline foi comunicado antes da instrução humana; o início da sequência de leitura está registrado, mas não há timestamp da instrução SQL. Bundle/fonte/imagens cp32 foram conferidos depois da solicitação humana e assim rotulados; JS igual ao cp27 e prova anterior cp31 preservada. Recibo root-cp32-receipt.json registra limites e resultado humano ainda pendente. Sem nova suíte/review por esta leitura e ação humana, fontes/runtime inalterados; VAL-05 segue obrigatória.

### cp33/cp34 — primeira troca não oficial e recuperação controlada autorizada

Operador confirmou entrada visível em Atendimento e resposta recebida no outro aparelho. Root verificou hashes cp33: leitura SQL com CURRENT_TIMESTAMP confirmou uma conversa, uma IN e uma OUT do recurso atual na mesma conversa, IDs externos presentes e autoria OUT presente, sem reter conteúdos/identificadores. Receipt verificado, status CONECTADO/connected=true, identidade/epoch/mapping consistentes. Fonte/imagens/bundle permanecem aceitos. Este é aceite da primeira troca observada, não de recuperação, histórico ou oficial.

Usuário confirmou explicitamente que o vínculo é de teste e pode ser interrompido por cerca de um minuto, para reiniciar apenas a Evolution local e repetir IN/OUT. Evidência cp34-operator-recovery-authorization.json. Operational/DevOps, Gate0 Genesis rejeitado por contrato/runtime existentes; mesmo escopo NestJS/React/Vite/PostgreSQL/Prisma/Docker. Routing-cp34-recovery go. Executor único pode parar/iniciar SOMENTE o container Evolution próprio após conferir ID/labels/imagem, com start em finally, observação limitada antes/durante/depois e preservação de todos volumes/dados/configurações/outros containers. Sem reset/recreate/QR/RENEW/remoção de instância/OAuth/SQL de escrita/env/código/envio. Não inferir novo recebimento do recibo anterior; repetir prova humana após retomada.

### cp34 parcial / cp35 — sessão ainda em retomada

Executor interrompeu SOMENTE container Evolution próprio e iniciou mesmo ID em finally; parada 5,59s, demais seis containers/cinco volumes preservados. Durante parada API/root200 e DTO mantiveram último estado conhecido, sem prova de saúde ao vivo. Após startup identidade/epoch/mapping preservados, conversa/IN/OUT continuam 1/1/1 e recibo anterior intacto, mas três leituras normais retornaram CONECTANDO/CONNECTING, connected=false. Tentativa CONNECTED/RECEIPT_VERIFIED e receipt antigo não provam retomada. Não orientar nova troca enquanto estado não for esclarecido. Routing-cp35-recovery-diagnosis go para diagnóstico de leitura SOMENTE da instância corrente: endpoints GET conhecidos do adapter com segredo em memória, estados/HTTP/códigos/owner-match booleanos apenas; sem listar recursos alheios, QR/renew/create/delete/connect/restart ou escrita de fonte/runtime/DB/configuração. Logs brutos e conteúdo pessoal não devem ser expostos/retidos. Root mantém canon; caso precise repareamento ou alteração material, retornar evidência antes da ação.

### cp36 — regressão de retomada de tentativa já concluída

cp35 consultou apenas instância própria por GET e confirmou OPEN e ownerPhone compatível com BU, enquanto BFF permaneceu CONNECTING. Inspeção em src/surfaces/webhooks/evolution.controller.ts::tratarConexao e src/domain/channels/channels.service.ts::verificar identifica hipótese reproduzível: promoção de tentativa só admite PENDING_NUMBER/PENDING_RECEIPT; tentativa corrente já CONNECTED produz update count0/ATTEMPT_STALE e rollback do estado do canal. Mesma verificação administrativa pode rejeitar repetição após conclusão. Tratar como bloqueador de SCOPE-05/06, DOD-01/05 e CON-12 do contrato aprovado, sem novo objetivo/arquitetura/risco: convergência idempotente do MESMO attempt/generation/epoch/owner, nunca relaxar tentativa obsoleta/cancelada/expirada ou identidade. Proibido reparar DB manualmente, simular webhook de provedor no operador ou renovar QR para mascarar a regressão.

Handoff Operational/Coder (nestjs/postgresql/prisma/docker), apenas domínio channels, webhook Evolution e testes E2E de onboarding/webhook já admitidos; Web/schema/dependências/env/runtime permanecem congelados durante a edição. Executor fresco deve reproduzir RED com PG real em namespace descartável antes da correção, cobrir reconexão e verify repetido após tentativa CONNECTED com receipt, duplicata open e negativos de scope/estado, depois validar build/lint/PG/suite apropriada no runner próprio. Recarregar regras aplicáveis, authority/routing go e único writer; nenhuma leitura/hash/cópia/mount de api-app/.local-files ou env privados. Após aceite técnico, review delta de segurança/aderência e TQA independente; então DevOps build/recreate API SOMENTE, preservando operador, e prova humana nova IN/OUT para retomada. Sem source push/deploy, source commit só feature autorizado e guardado. O blueprint aprovado permanece, sem antecipar novos recursos.

RED preliminar cp36 comunicado pelo executor em PostgreSQL real: verify administrativo repetido409 ATTEMPT_STALE; connecting200, open e open duplicado409 ATTEMPT_STALE. Nenhum código de produção havia sido editado antes desses resultados. Log terminal/hash e correção ainda serão adjudicados; D-06 marcado Exception temporária e SCOPE-05 bloqueado até resolução e novos aceites, sem reaprovar um requisito que permanece inalterado.

cp36 código congelado em quatro paths públicos (helper receipt-attempt-convergence.ts, ChannelsService, webhook Evolution e flow E2E), hashes em cp36-review-source-freeze.json. RED comprovou ambos loci409; stdout completo RED não foi teeado e não existe para recuperar: preservar o excerpt/totais e hashes reais, sem reconstruir log nem fingir cobertura raw integral. GREEN API completo em cp36-api-recovery-green-api.log: lint/build,138unit e288PG passaram. Final all em curso nas mesmas fontes. Routing-cp36-tqa go (role formal-reviewer; tentativa inicial com role reviewer foi recusada antes de ativação e corrigida); fresh native Codex gpt-5.6-terra/max executa somente revisão de testes pelo pacote cp36-tqa-package.md/dispatch e evidência API terminal, sem ler o all ainda vivo. ALL não declarado verde antecipadamente. Auditoria estática não achou hard bypasses e sinalizou hints médios em asserts/spy preexistentes para adjudicação contextual.

cp36 final all terminou exit0:138APIunit+288PG+28Webunit+47browser=501 testes,22migrações. Root conferiu quatro hashes atuais contra freeze e hashes dos logs/manifests/summary; root-cp36-validation-receipt.json registra aceite primário. GlobalSetup genuíno antes dos workers em cp36-browser-attestation.json incluiu helper novo/untracked com mesmo hash, DB descartável e JS servido=dist d1434360…; Web sem mudanças de fonte. Executor API terminou STOP, sem stage/commit/runtime. TQA continua vivo e não é interrompido por timeout de polling; depois review delta final/security/aderência e atualização API-only antes da repetição externa.

### cp36b — integração do achado oficial da revisão

Fresh arquitetura/segurança terminou STOP, raw SHA6647e509bd021facbb6a2ae39c2f9b047eb5c0813168f49ef9ef39adb6cca870/schema válido. Um P2 NUM-ADH-CP36-01 aceito Integrated para correção no mesmo contrato: tentativa oficial criada com pairingEpoch=null versus canal com0. Não é regressão introduzida pelo helper, mas a correção compartilhada permanece incompleta para verify oficial. Nenhum novo bypass de autenticação/tenant estabelecido; posições de performance/elegância aceitáveis e estrutura mixed somente por aplicabilidade.

Autorizado executor API serial cp36b, routing go, mesmos quatro paths públicos. Acrescentar ao fluxo oficial real já existente prova do epoch null e duas verificações após CONNECTED, com invariantes receipt/credencial/owner/currentAttempt/version e RED autêntico capturado integralmente antes da correção. Depois tornar expected epoch explicitamente nullable SOMENTE para OFICIAL no caller confiável; NAO_OFICIAL continua exigindo epoch numérico exato (negativo null também). Não normalizar dados/schema/migration nem usar fallback ORnull genérico. RED pode usar runner API seguro; após fix executar um único all final, sem repetir API-green separado pois all inclui as folhas. Preservar cp36/501 e seus reviews como históricos, patch público congelado em cp36-reviewed-delta.patch; novos bytes/evidência/reviews cp36b. TQA e aderência delta independentes frescos devem julgar a correção antes de final review e runtime. Nenhum leitor vivo permanece; código único writer API, DevOps STOP. Sem nova aprovação para concretização do mesmo requisito.

cp37 preflight somente leitura autorizado para executor DevOps em paralelo ao writer API: checar HTTPS atual/health e identidade/labels/imagens dos sete containers/cinco volumes próprios, presença de configuração sem valores, sem auth/provedor/DB/código/build/restart/recreate/rotação do túnel. Routing-cp37-preflight go. Não é runtimewriter; API cp36b permanece único escritor. Preparar condições do futuro handoff API-only após fontes/reviews aceitos, sem consumir bytes ainda em edição.

cp36b RED oficial foi capturado completo antes de editar produção: duas verificações409 contra200 esperado. Uma expectativa errada no novo negativo de fixture (entrada manual null versus assert final anterior de epoch+1) foi identificada como falha de harness, não produto; corrigir somente para o valor realmente atribuído e preservar409/rollback. Segundo RED já havia sido iniciado antes da orientação root de dispensá-lo; permitir término e preservar ambos logs/manifests distintos, sem fabricar histórico ou sobrescrever a primeira captura. Nova fonte/aceite cp36b permanece separado do all501 cp36.

cp36b segundo RED completo terminou com apenas a falha oficial esperada ([409,409] versus[200,200]),287PG passaram e negativo Evolution com null passou;138unit também verdes. Correção de produção limitada ao parâmetro nullable e seleção explícita por modalidade confiável. Final all único em curso; quatro hashes atuais congelados em cp36b-review-source-freeze.json. Fresh adherence_cp36b gpt-6.1-sol/max revisa somente a correção/finding e controles do locus enquanto all valida, sem declarar GREEN antecipado; routing-cp36b-adherence go. Módulo owner explicita null apenas oficial e epoch estrito Evolution, preservando restante do contrato.

### cp36c — verificação limitada do número oficial vinculado

Fresh review cp36b terminou STOP, raw SHA85448d60b6072799281ff9547ead06844c030d6732ebc9c7572be94a46b52625/schema válido. NUM-ADH-CP36-01 corrigido em fonte quanto à aplicabilidade nullable, mas não encerrado por comportamento: all falhou no verify oficial com409. NUM-ADH-CP36B-01/P2 aceito Integrated para correção. Trace de fonte prova que verificar usa confirmarNumero sem after, cliente real e fake leem apenas primeira página enquanto o teste seleciona legitimamente a segunda. Logs anteriores guardaram somente status409: NÃO afirmar código de erro observado nem RED discriminante do epoch; a atribuição inicial exclusivamente ao epoch foi hipótese, agora corrigida. Preservar capturas originais; all falho é RED funcional da verificação de número selecionado, antes do fix de paginação.

Mesmo objetivo e aprovação: verificar qualquer vínculo selecionado com segurança e orçamento3requests×10s/lease45, sem fan-out na listagem, sem mudar regra do confirm que relê somente página escolhida. Executor API cp36c, routing go, amplia ownership ANTES de editar: quatro paths anteriores MAIS src/integrations/meta/meta.client.ts e meta.client.spec.ts, test/helpers.ts e test/browser-server.cjs (já permitidos no diff contract). Nenhum outro path. Nova operação interna dedicada no adapter para verificar número já vinculado: revalidar grant/app/scopes/WABA uma vez e consultar no máximo duas páginas phone_numbers=3requests externos; sempre host Graph fixo e after opaco limitado, nunca seguir URL next externa. Cursor cíclico/maior512 ou páginas restantes após budget => erro seguro explícito de verificação inconclusiva; null somente quando exaustão comprovar ausência. Onboarding confirmarNumero/after mantém semântica de página selecionada. Mesmo contrato de método deve existir nos doubles API/browser, com testes reais do adapter e DI/escopo/budget, sem mock sempre-sucesso.

Preservar alvo/paginação do teste oficial e assertar200/invariantes; melhorar falha para mostrar somente status/catalog code, sem body bruto. Unidade do adapter deve provar segundo-page alvo, grant estrangeiro, token explícito, ausência exaurida, limite/ciclo/cursor inválido, sem URL externa/retry de mutação. Não afirmar novo RED integral se só add-unit depois: RED funcional atual já existe em all cp36b antes desta alteração. Sem rerun RED completo apenas para obter código que não foi capturado. Após fix executar um único all com raw completo e freshness; source frozen antes de revisões técnicas/aderência/final frescas do delta atual. Não ordenar/reduzir lista nem trocar para primeiro número só para passar; nenhuma nova seleção de WABA real, alteração de schema/env/deps/runtime ou reparo SQL. Leitores prévios terminais STOP antes deste writer serial.

cp36c congelou oito paths antes de um único all canônico. API lint/build e141 testes unitários/288 PostgreSQL passaram; Web build/28 unitários passaram, navegador em curso neste checkpoint. Fresh adherence_cp36c (gpt-6.1-sol/max) e TQA nativo efêmero (gpt-5.6-terra/max) ativados com routing GO, pacotes/dispatch cp36c e schema canônico; nenhum editor de fonte durante revisão. TQA cobre workload completo aplicável, incluindo eficiência/eficácia das asserções, DI/PG real, HTTP real do adapter sob stub, fakes, budget, bypass/fail-first/plataforma/decisões e incerteza. Não declarar all/browser ou reviews aceitos antes de término. Contador do fake conta páginas; limite real3requests é demonstrado nos testes HTTP do adapter, sem confundir as duas evidências.

cp36c all TERMINAL exit1: API lint/build141unit+288PG e Web build28unit passaram; navegador46pass/1failed, caso Pessoas “adicionar uma pessoa e conceder um setor a ela” em telas.spec.ts348 (Ana ausente após Convidar; consoleHTTP400). Sem body/catalog capturado; error-context desapareceu com cleanup e não será reconstruído. Não declarar all verde nem aceitar rerun-only. cp36c-final-result.md e root-cp36c-validation-receipt.json retêm limite. Oito hashes antes/depois idênticos e freshness/globalSetup genuínos antes dos workers, DB descartável22migrações, JS servido=dist. Fontes continuam congeladas; runtime operador ainda anterior. Revisões dedicadas em curso; classificar falha de readiness do caso Pessoas antes de qualquer concretização de harness, sem ampliar objetivo de produto ou enfraquecer asserções.

Classificação independente de adherence_cp36c: Usuarios.tsx inicia novo.buId vazio e só o preenche após três GETs; teste de convite não espera/seleciona Número, botão já permite submit; UsuariosService rejeita BU desconhecida antes de criar. Essa corrida existente é hipótese concreta compatível com400, não causa observada comprovada (body ausente). Loci alterados cp36c não integram a chamada de convite. all segue FAILED; não aceitar repetição sem corrigir precondição. Proposta de concretização do harness após término dos leitores: usar controle real Número para selecionar explicitamente o Número de QA pertencente à conta antes de Convidar, aguardar/assertar POST real201 e preservar Ana/setor/console. Nenhuma mudança de produto Pessoas, timeout/sleep/retry/mock/filtro400 ou remoção de assertion. Registrar admissão do caso no diff contract ANTES de eventual edição, validar folha browser canônica e revisão TQA fresca somente desse delta, preservando aceites API/Web nos mesmos hashes. Revisão final separada continua obrigatória antes do runtime.

Achado source-path independente NUM-ADH-CP36C-01 aceito Integrated-for-fix: limite/ciclo/cursor no novo caminho oficial lança MetaIndisponivelError plain Error; ChannelsService/controller não traduzem, filtro Nest responde500 genérico, sem código prometido. Inferência de fonte concreta, não captura HTTP. Preservar raw terminal que vier; nenhuma fonte alterada enquanto reviewers vivos. Concretização aprovada do mesmo contrato: catch restrito à classe MetaIndisponivelError no serviço verify, converter para HttpException503/codeMETA_INDISPONIVEL/mensagem fixa segura; conservar exceções auth/CAS/grant, não retornar mensagem/providerraw, e finally liberar somente o lease próprio. Teste PG BFF deve reproduzir500 antes da correção e exigir503/catalog+preservação credential/attempt/version/identidade/receipt/estado/BU+lease livre depois, cobrindo caminho inconclusivo real do fake bounded e separando HTTP real do adapter nos unitários. Scope API continua os mesmos oito paths, nenhum globalfilter/novoendpoint/schema/dado/env. Registrar próxima execução cp36d após todos leitores terminais; depois all atual e revisões frescas afetadas antes do runtime.

cp36c aderência/segurança TERMINAL STOP, schema+merge válidos, raw SHA4e7f2d614610d0f1fad0ef2c2f22d05add34fc7e5acc6a5d4b872c79ef2b3829. Dois P2 anteriores resolvidos no locus fonte e comportamento positivo PG, sem atribuir código ao RED histórico. Um P2 de catálogo NUM-ADH-CP36C-01 integrado para correção restrita; performance/elegância aceitáveis, estrutura/fit mixed por esse limite e gate browser falho. Recomendação independente também aceita concretização futura estrita do teste Pessoas como precondição legítima, sem resolver/ocultar a corrida de produto. Diff contract do caso Pessoas ampliado ANTES de editar. Próximo executor cp36d só após TQA atual terminal; ownership oito API paths atuais + um caso de web-app/e2e/telas.spec.ts, sem qualquer arquivo de produto Web. RED novo deve capturar BFF500/catalog ausente antes do mapper; final all único após correção e seleção/barreira de harness, revisões afetadas novas e final separado. TQA cp36c vivo não é interrompido por polling.

Antes da edição cp36d, a mesma precondição de convite é admitida também no caso Bia/link imediatamente adjacente (telas.spec357), que usa a mesma sequência de campos/click sem aguardar Número. A falha observada continua somente Ana; Bia passou no cp36c. Tratar ambos pela mesma seleção explícita+resposta201 evita manter o mesmo risco de harness no outro caso; não alterar expectativa de fallback email/link, produto, qualquer outro caso, tempo ou filtros. Total continua um path Web/two-existing-case test-only, oito API.

TQA cp36c nativo TERMINAL exit0. Raw original preservado; dois achados úteis aceitos Integrated-for-fix: TQA-CP36C-01/high repete gap de mapper/cobertura BFF e pede assert code no adapter; TQA-CP36C-02/medium identifica que double browser usa Error genérico nos novos ramos inconclusivos, comprometendo paridade do catch tipado. Também mantém plataforma browser não aceita; root preserva46/1 FAILED, não infere sucesso. Merge recusou dispatch_path basename porque prompt foi impreciso; raw não normalizado/regravado, nenhuma aceitação desse gate. root-cp36c-tqa-protocol-receipt.json registra falha de binding e limite; revisão técnica nova nos bytes cp36d deve receber dispatch absoluto correto. Não repetir a auditoria de fontes que agora serão corrigidas só para consertar metadata: revisão posterior fresca é obrigatória por mudança real.

cp36d pode agora executar serialmente: todos leitores terminais. Além do catch restrito/negativo PG e dois casos Pessoas admitidos, alinhar SOMENTE os novos ramos de erro inconclusivo do browser double à mesma MetaIndisponivelError exportada do módulo dist real, e fortalecer os testes unitários de budget/cursor com codeMETA_INDISPONIVEL sem duplicar rede. Oito paths API+um Web já admitidos; nenhum novo arquivo de produto/rota/testsupport/config. Handoff cp36d-execution-handoff.md, routing-cp36d-apiGO; executor deve revalidar authority/rules antes de escrever. Preservar callbackdispositivo/dadosoperador e proibição.local-files. All/revisões atuais antes de runtime; nenhuma dispensa de VAL05.

cp36d fonte congelada em nove paths e único all em curso. RED API completo capturou141unit/287PGpass+1falha: BFF500/catalognull contra503/META_INDISPONIVEL, por injeção do erro tipado no port; o reforço posterior de loop com spy de duas páginas não teve nova execução RED e não é apresentado como tal. Correção restrita e negativo final agora percorreram o loop fake real e passaram no API leaf: lint/build141unit+288PG, incluindo503/code e preservação de estado/lease. Webbuild28unit também passaram; navegador ainda em execução. Não antecipar aceite all.

Revisão cp36d em andamento confirma em fonte mapper e double browser usando a mesma classe real, mas identificou lacuna de harness: trocar a asserção anterior de classe por code-only permite que um Error comum com code correto passe nos unitários do adapter, enquanto o BFF usa instanceof. Isso não demonstra tipo errado na produção atual; é proteção incompleta entre seams separados. Nenhuma fonte será editada durante all/reviewer. Depois dos terminais, o reparo planejado é SOMENTE meta.client.spec.ts: preservar asserção de classe E code sobre a MESMA promise, sem repetir requests. Validar a folha API canônica nos novos bytes; Web/browser podem ser reaproveitados somente com vínculo explícito de produção/fixtures/testes Web imutáveis. tsconfig.build.json exclui **/*.spec.ts do build da API. Não relabelar manifest pré-worker anterior como se contivesse teste unitário novo; receipt futuro deve explicitar composição das folhas e hashes. TQA fresco completo e final separado ainda obrigatórios.

Admissão pré-edição cp36e (aguardando todos os terminais cp36d): mesmo path unitário meta.client.spec.ts já autorizado, somente reter classe e code em duas expectativas padrão sobre uma única promise rejeitada. Nenhuma invocação HTTP adicional nem mudança de código runtime. Routing-cp36e-api-test GO. Validar a folha API source-owned depois dessa alteração de teste; não há justificativa para repetir Web/browser sem alteração em seus bytes/produção. O receipt composto deve provar oito dos nove paths sem mudança e o único spec alterado excluído pelo build, guardar manifest/attestação cp36d genuínos imutáveis e manifest atualizado, sem alegar um novo all cp36e. TQA fresco deve auditar todas as fronteiras aplicáveis e fechar a lacuna; final review gpt-6.1-sol/max separado julgará produção e teste atuais. Nenhuma dispensa/aceitação automática por teste-only.

cp36d ALL TERMINAL exit0,504 testes=141APIunit+288PG+28Webunit+47browser/22migrações. Root verificou nove hashes antes/depois/atuais e ambas attestations genuínas pré-worker contra os nove paths (inclui spec novo e dois casos Web), JS servido=dist e DB descartável. root-cp36d-validation-receipt.json guarda hashes reais; raw all b94bf3c7a54e0030e798dc7a0058625814d3cb5fa0e1f238e6461171b9e31262. Nenhum byte do runtime operador atualizado.

cp36d aderência TERMINAL, raw b661b76cd95aa4718155573a2abf974186a09f46bc907fd279c364d7d61ce40b/schema+merge válidos. Fonte de produção/mapper/paridade browser e precondições Web conformes; performance/elegância/estrutura aceitáveis, fit mixed pela validação/externo pendentes ao dispatch. Um achado medium NUM-ADH-CP36D-01 integrado para reparo test-only classe+code, sem novo defeito runtime. D-05/D-07 e invariant de catálogo voltam Adherent/Preserved em fonte+PG; D-06 Exception de retomada real permanece. Todos leitores/executor anteriores STOP. Autorizar serialmente cp36e apenas meta.client.spec.ts, expectativas padrão classe+code na mesma promise por caso/mesmos fetch counts, sem novo RED artificial nem código de produto. Depois API leaf completo pelo runner próprio, novo manifest9 e prova8imutáveis+spec excluído do build; reaproveitar Web/browser cp36d pelos seus bytes exatos, nunca reescrever attestation antiga. Fresh TQA completo e final separado devem aceitar a composição atual antes de source commit/runtime.

cp36e API TERMINAL exit0: lint/build141unit+288PG/22migrações. Root verificou nove hashes atuais, before=cp36d e somente spec alterado para1cbcd9a9bade8c90c0c468042c1396285b1e2f3eae4b5beb1718551d8ef65078; oito paths de produção/fixtures/Webtest idênticos. root-cp36e-validation-receipt.json compõe API atual com Web28/browser47 cp36d, mantendo attestation genuína e hash unitário anterior sem relabel. Fresh TQA nativo gpt-5.6-terra/max iniciado com routingGO, pacote/dispatch cp36e e caminho absoluto de binding obrigatório, full workload aplicável. Fonte congelada; executor STOP; nenhum commit/runtime realizado.

cp38 preflight read-only admitido em paralelo ao reviewer: DevOps pode checar somente HTTPS/health/asset público conhecido, IDs/labels/imagens/running dos sete containers e presença/ownership dos cinco volumes, presença de configuração privada em booleans sem valores/hashes/cópias. Não login/DB/provider, código/build/restart/recreate/túnel/Git. Objetivo é confirmar readiness que pode derivar desde cp37, não aceitar runtime novo/retomada. Preservar todas as superfícies, parar e aguardar gates antes da atualização API-only. Rotear executor de rotina/medium antes da ativação; root conserva canon.

cp38 preflight TERMINAL STOP, root verificou JSON/md e hashes3bee98efc328cca8e76d68c21007493be5f94f48f9731b9f8955535f623d233a/341757b8331111cca53d9ea4fa361539b814db2125b6ac6191fc11073b94552a. Em20:19:56UTC, HTTPSroot/health200, JSd143…igual aceito, sete containers/cinco volumes próprios preservados, API ainda imagem anterior. Configuração apenas booleans, sem login/DB/provider/mutação. root-cp38-receipt.json aceita readiness/preservação, não novo runtime/recuperação. DevOps STOP até gates atuais.

cp39 concretização de validação em paralelo ao TQA: preparar SOMENTE imagem candidata isolada da API com o Dockerfile/contexto reais atuais, sob tag nova de teste vinculada ao manifest cp36e. É build/checagem de artefato para tornar o checkpoint concreto antes do final review, sem atualizar a aplicação servida. Namespace de imagem proposto leadshug-channels-api-candidate:cp36e-ea3080d36a43, owner/checkpoint/source-manifest em labels; confirmar ausência antes de criar e não sobrescrever recurso alheio. Usar Docker Windows canônico, mesmo Dockerfile, sem build args/vars privadas. .dockerignore exclui .local-files/.env e Dockerfile copia explicitamente src/prisma/manifests, sem ler payload privado. Sem alterar tag/imagem do operador, arquivos/configuração ou os sete containers/cinco volumes existentes. Único executor DevOps; demais agentes somente leem fontes congeladas. Uma sonda efêmera do candidato pode importar apenas módulos compilados/checar Node22/Alpine/OpenSSL/classe/helper, com --network none/--read-only/sem env/ports/volumes e entrypoint substituído para NÃO iniciar API/migrations. Nunca conectar DB/provider. Registrar IDs/hash/source9 antes/depois e artifact proof, preservar todos recursos do operador e parar. Ativação do candidato/recreate/restart continuam SOMENTE após TQA/final/source checkpoint aceitos. Não alegar runtime novo servido ou device recovery pela imagem construída. Esta antecipação de build local não muda contrato ou plataforma, e não requer source push/publicação.


### cp36e TQA terminal e admissão cp36f

TQA nativo terminou exit0, raw imutável e merge válido com dispatch absoluto. Achados medium TQA-CP36E-01/02 Integrated, release-blocker/fix-current-contract: não flexibilizam o contrato; reforçam D-05/D-07 já aprovados. Gate não aceito. cp39 build/probe terminou com fonte cp36e, sete containers/cinco volumes preservados e imagem NÃO servida; artefato agora anterior ao reparo, jamais ativar como fonte corrigida.

Admissão cp36f antes da edição: único executor Coder/NestJS/Prisma/PostgreSQL no checkout principal. Pode editar somente api-app/src/integrations/meta/meta.client.ts, seu spec e test/number-onboarding-flow.e2e-spec.ts. Primeiro testes reais do adapter para JSON malformado, data ausente/não-array (e formato estrutural necessário para não concluir ausência); captar RED canônico antes da correção. Adapter deve lançar MetaIndisponivelError sem payload cru, preservar limite/grant/host/cursor/semântica de página vazia válida; não expandir API pública. BFF prova envelope público fixo, ausência de dados do provider, erro genérico não remapeado e invariantes de canal/BU/tentativa/credencial/identidade/receipt/audit/lease. O teste deve exercitar adapter real para inválidos e a fronteira BFF com DI declarada, sem simular prova externa. API leaf RED pode terminar antes de PG ao falhar unit; preservar raw completo, não inventar RED posterior. Depois alteração de produto, rodar canônico all para nova fonte/build/browser, guardar freshness genuína e novo manifest9. Sem novo teste/mudança de Web ou mapper se o comportamento correto já existe. Demais caminhos somente leitura, inclusive outros seis paths cp36e. Proibido ler/hash/copiar/montar/stage api-app/.local-files ou dotenv privado; não mudar Git/runtime/provider/túnel/DB operador. Root é dono exclusivo de canon/Git. Routing cp36f API GO; TQA/final frescos exigidos após validação. Nenhuma nova autorização humana necessária para reparar os achados do contrato já aprovado.


cp36f TERMINAL canônico all exit0: lint/build150unit+288PG+28Webunit+47browser=513,22migrações. REDapi exit1 genuíno142pass/8fail, produto Meta preservado antes da correção, sem PG RED. Root comparou manifest9 atual a AMBAS attestações genuínas pré-worker21:00UTC e conferiu built=served JSd143 e DB descartável22migrações. O executor inicialmente não localizou esses artefatos emitidos pelo globalSetup existente; resultado/freeze corrigidos após descoberta, sem rerun ou attestation fabricada. root-cp36f-validation-receipt.json e REDreceipt distinguem claramente as execuções. Três paths cp36f modificados e seis adjacentes byte-idênticos; todo produto congelado. TQA fresco com workload completo, binding absoluto/routingGO e pacote cp36f inicia; final separado posterior obrigatório. D07 continua Exception até adjudicação do reparo, D06/VAL05 externos sem waiver. Foundation histórico cp33..e/39+canon checkpoint106arquivos foi commitado e pushmain68c9a794; nenhum source push/Gitlink/runtime foi alterado.


cp40 admissão de artefato antes da execução: somente novo build/probe ISOLADO da API com fonte cp36f validada/freeze9 (manifestSHA88d419218e080050e2d95724b1ecee19a095c4541e74b6b0f658536336f6859e). Mesmo contrato cp39, única tag nova leadshug-channels-api-candidate:cp36f-88d419218e08, confirmar ausente; labels owner=number-onboarding/checkpoint=cp40/source-manifest. Não reutilizar/ativar cp39. DevOps executor único, sem alteração source/canon/Git/configuração privada/runtime operador. Dockerfile/contexto públicos reais, sem private buildargs/env/payloads; probe rede none/read-only/sem env/volumes/ports, entrypoint substituído (sem API/migração). Guardar sete containers/cinco volumes preservados contra cp38/cp39, hashes9 antes/depois e resultados públicos. Sem retag de operador, Compose/recreate/start/stop/DB/provider/auth/túnel. TQA atual pode ler fontes congeladas paralelamente; qualquer mudança de fonte bloqueia build. Ativação atualizada permanece condicionada a TQA terminal/final separado/sourcecheckpoint. Routing cp40 GO.


cp40 TERMINAL build/probe aceito estritamente como artefato isolado: imagem8f78e4813da53f29e48dd61e20077f616b4c915d30fe8d7676c102df8b9bd805 vinculada ao manifest cp36f88d419..., Node22.23.3/Alpine3.24.2/OpenSSL3.5.8/Prisma/exports; probe removido; sete containers/cinco volumes e candidato cp39 histórico preservados. Root verificou hashes dos três artefatos cp40. Nenhuma nova API servida. A checagem opcional de transporte constatou hostname atual não resolvido nos dois ambientes (WSL EAI_NONAME/Windows curl6); cp38 saudável é histórico, disponibilidade HTTPS atual não aceita.

Admissão cp42/read-only antes da execução: DevOps deve diagnosticar somente o túnel próprio cp29/cp30 para origin operating-brussels-internship-interviews.trycloudflare.com e target127.0.0.1:8083, com guardas exatos do lifecycle; verificar processos próprios por identidade/executable/cmdline/target/starttime, não por PID sozinho, estado de DNS/transporte e gateway local. Pode ler somente metadata pública/trechos pertinentes redigidos do seu log de túnel; nunca dotenv/segredos/payloads .local-files/Config.Env/provider. Nenhuma rotação/start/stop/kill/recreate/mudança de config nesta fase; retornar diagnóstico e plano concreto restrito à restauração do transporte. Fonte continua congelada e TQA ativo; sem API/provider/DB/auth/Meta alterações. Evidência cp42-tunnel-diagnosis.json/md em E, root canon exclusivo. Routing GO e autorização vigente de testes locais cobrem este diagnóstico reversível/read-only; nenhum novo APROVADO necessário.


cp42 TERMINAL read-only/root hashes verificados: gateway root/health200; nome público confirmado DNS name-error em Windows/WSL/resolver público. Motivo do desaparecimento desconhecido. Processo Windows corresponde à linha cp29; continuidade dos PIDs WSL não comprovada por starttime discrepante. Não encerrar nenhum processo antigo por PID. Sem mutação realizada.

Admissão cp43 antes da execução: restauração estrita do transporte de teste já autorizado pelo usuário neste TODO, sem nova API/credencial/configuração de app servida. DevOps único pode iniciar UM novo Quick Tunnel via processo Windows wsl.exe detached próprio, Ubuntu, binário cloudflared2026.10.0 de hash fixado cp29, target exato127.0.0.1:8083, novo diretório/handle/log metadata cp43. Confirmar path/handle ausente, criar ownership claro por parent/child/executable/cmdline/starttime/target e processo Windows/WSL; saída filtrada sem segredos e sem callback query. Provar DNS/HTTPSroot/health200 nos dois ambientes, mesmoJSd143 e runtime Docker7/cinco volumes preservados. NÃO encerrar/alterar processos antigos de continuidade incerta; preservar também os comprovados nesta etapa. Sem API/Evolutionrestart/recreate/tag/config/DB/provider/auth/Meta/privateenv/source/Git. Novo hostname será só evidência transporte, não configurar automaticamente Meta nem declarar origem API migrada. Só após TQA/final/sourcecheckpoint a atualização API poderá ajustar o valor público de origem conforme runbook; nada nesta admissão antecipa essa ativação. A evidência deve incluir lifecycle reversível com guardas de identidade e rollback do único processo novo se falhar; nenhum processo alheio. Evidência pública cp43-tunnel-restoration.json/md em E e STOP. Root valida e só então pede ao usuário a configuração Meta com o endereço concreto. A restauração reversível está no escopo de infraestrutura local/autorização já persistente; não é publicação/app Meta. Routing cp43 GO.


cp43 TERMINAL/root hashes+proof verificados: novo transporte https://minority-influenced-veterans-ready.trycloudflare.com ativo, DNS/HTTPSroot/health200 e JSd143 iguais em WSL/Windows. Novo owner Windows16108 e WSL125292/125296 com boot_id/start_ticks/command/exe/parent/target e rollback guardado; processo anterior preservado. Sete containers/cinco volumes intactos; origem da API/Meta ainda NÃO ajustadas e API antiga continua servida. O relógio WSL mudou21:18→21:55 durante o diagnóstico; guardas Linux usam identidade monotônica, não UTC derivado. Não inferir que a continuidade cp29 foi comprovada pelo relógio. Root-cp43-receipt.json aceita somente transporte. Solicitar ao operador atualizar domínio/OAuth/SDK/callback Meta no app de testes com o novo hostname e mesmo verifytoken local, sem publicar; esta ação humana está pendente. Ajuste público da origem da API e nova imagem ainda aguardam gates de fonte.


Operador respondeu à solicitação cp43: Meta não validou URL/token do novo callback (erro genérico #N/A; nenhum token enviado). Não registrar como callback salvo/validado, não presumir causa. Admissão cp44 antes da execução: DevOps único diagnostica GET de verificação no caminho público /webhooks/meta e gateway local8083 com challenge sintético. Exceção necessária e estritamente delimitada à leitura do campo WEBHOOK_VERIFY_TOKEN do .env.testing em memória e sua comparação booleana com o campo correspondente do runtime API existente, sem mostrar valores/hash/cópias/Config.Env bruto nem tocar outros segredos. Pode consumir process.env.WEBHOOK_VERIFY_TOKEN dentro do container via script stdin e retornar apenas presença/igualdade, nunca valor em argv/stdout/log. Não ler/copiar/montar payload .local-files. Confirmar exato ownedAPIID/labels antes de exec read-only; script não grava/DB/provider/auth. GETs reais de callback com token atual são permitidos somente no gateway127.0.0.1:8083 e novo hostname cp43 já guardado, request em memória/stdio seguro (sem segredo em argumentos, erros/URL/query/logs), saída apenas status e bodyMatchesChallenge boolean. Token inválido sintético/ausente deve falhar; não expor body cru. Usar TLS normal. Checar DNS público atual e comportamento WSL/Windows se útil; provider Meta/OAuth/admin não chamado. Não editar arquivo/env/imagem/container/Meta/Git/source/túnel nem promover nova API; nenhum rotate/tokenchange. Registrar cp44-webhook-diagnosis.json/md com booleans/status/causa confirmada vs hipótese e STOP. O usuário autorizou diagnóstico do problema real; sem nova pergunta de token/credencial. Routing cp44 GO; TQA65990 ainda ativo/sourcefrozen, ativação só após gates.


cp36f TQA TERMINAL exit0: raw44480e3c16207699354ed21b1df28beb6f5a93d41f5849325c2f00bd6abc0065/schema+merge válidos. O mesmo reviewer aceitou eficácia/eficiência das páginas inválidas, classe+code/BFFseguro503, mapperseletivo, preservação/lease, freshness9 e platform atual. Um novo medium TQA-CP36F-01 Integrated/release-blocker: debugToken/data e campos scopes/granular_scopes/entries/target_ids usam casts e iteração sem validar formato, podendo escapar TypeError500. Formato JSON raiz não-record também precisa cobertura direta (guard já existe). Fonte atual permanece não aceita no conjunto; D05/D07 Exception de grant, D06 externo inalterado. Aceite específico dos loci já corrigidos fecha somente seus achados antigos, não este novo nem retomada real. Instabilidade de stream do native foi recuperada automaticamente e terminou com parecer genuíno; não houve duplicação/retry de auditoria por tempo nem reescrita de raw.

Admissão cp36g antes de edição: executor Coder único, mesmos três paths (MetaHttpClient.ts/spec e number-onboarding-flow.e2e-spec.ts), outros seis somente leitura; sem editar mapper/fixtures/Web/runtime/Git. Implementar uma fronteira coerente de validação tipada do grant antes de spreads/map/target iterations, mantendo semântica válida de app/scopes/target intersection e opcionalidade legítima prévia, sem coerção silenciosa do formato inválido para ausência nem captura genérica de erros. Payload raíz e data/arrays/entries/target IDs malformados devem resultar em MetaIndisponivelError sem detalhe cru, sem novas requisições ou mudanças de permissão/target/lease. Primeiro table tests de estruturas ruins e nonrecordroots, provar class+code na mesma promise/requestbounds com RED API canônico antes de produto; casos já protegidos podem passar no RED, relatar os números exatos. Representante BFF/PG usa o adapter real por port seam para grant ruim,503/envelope fixo/no provider leak e preservação dos mesmos invariantes/lease/audit. Runner API para RED pode parar antesPG; não alegar PG RED. Depois reparar produto e rodar all UMA vez com fonte congelada, copiar attestações genuínas pelos paths existentes em artifacts/tmp, manifest9 before/after/freeze e recibo honesto. Sem fabricar/renomear evidência antiga. Novo TQA completo e final independente obrigatórios. Candidatos cp39/cp40 históricos jamais ativar como reparo cp36g; próximo build só após TQA limpo, antes final, para evitar candidato destinado à fonte já recusada. DevOps cp44 é estritamente diagnóstico read-only da API servida antiga, não conflita com fonte; nenhuma outra mutação código/runtime simultânea. Source/payloads .local-files/segredos continuam proibidos de leitura/hash/cópia/mount/stage. Root canon/Git exclusivos. Routing cp36g GO e autoridade vigente.


Concretização cp36g pré-edição adicional no mesmo helper/contrato: root identificou source-path wabaTargets retornando interseção.slice(0,100), embora recursos já aplique slice100 para a apresentação. Se o alvo persistido está depois100 na autorização válida, includes pode dizer falso e verify retornar ausência sem consultar página. NUM-ROOT-GRANT-CP36G-01/medium/release-blocker é hipótese causal por fonte, ainda sem observação executada. Admitir um teste de grant válido com101alvos/interseção e WABA persistida na posição101, mantendo listagem options<=100, grant/lookup sem requisições extras. Se RED confirmar, separar o limite de apresentação da prova completa de pertencimento no helper interno (custo já linear antes do slice), mesmos três paths cp36g. Não aumentar página/UI/rondas/budget, nem aceitar recurso não autorizado; app/scopes/interseção completos continuam obrigatórios. Isso remove falsa ausência no verify existente, não cria nova capacidade nem afirma limite real da Meta. Se não reproduzir, registrar red_not_reproduced e não mudar fonte por hipótese. Integrar no RED/gates atuais se ainda não iniciado; se RED já estiver vivo, esperar terminal e capturar caso novo genuíno antes da respectiva correção, sem interromper/rótulo retroativo. Routing cp36g válido; rootfonte pública não leu payload/privados, executor continua único writer.


cp44 TERMINAL/root verificou hashes JSONb4f79c.../MDcaa770...: tokenlocalpresente=runtimepresente=igualtrue, sem segredo registrado; gatewaychallengeválido200/match e inválido/ausente403. Novo hostname cp43 voltou a falhar DNS nos dois ambientes, logo requests públicos não chegaram ao callback. Erro Meta não prova rejeição de token; transporte atual falho, cp43saudável é histórico. Nenhuma nova URL será solicitada até transporte+challenge público terem prova atual.

Admissão cp45 READ-ONLY préflight: DevOps pode verificar disponibilidade de cloudflared.exe NATIVO Windows, versão/path/hash se existir, processo(s) próprio(s) e targetgateway8083, comandos/help pertinentes apenas se binário confiável. Não tocar instalações/processos/config existentes, não baixar/instalar ainda, não parar túneis (continuidadedaidentidadecp43provada por monotonicmetadata, mas semautorização de cleanup nestaetapa). Read-only DNS/socket/lifecycle do cp43 pode constatar perda atual sem dumps de logs/query/privados. Root consultou release oficial https://github.com/cloudflare/cloudflared/releases/tag/2026.10.0: artefato cloudflared-windows-amd64.exe SHA25686aee4017b26625cee8484c113558f48effa4cd47f7aa05fcf425604e5d2b23c; Linuxd33ff2... continua igual. Plano proposto para restauração posterior: cliente portableWindows na mesma versão/hash, execução nativa detached com stdout/stderr drenados em memória e persistência só de hostname/eventclasses+metadata, targetloopback8083, sem ler config/credenciais homedir; verificar suporte a --protocol http2 por help e considerar transporteTCP como experimento. Não afirmar que WSL/QUIC causou a queda: só hipótese. Topologia de API/DB/provedores inalterada, mesmoCloudflareQuickTunnel público efêmero; nenhuma conta paga/domínio/serviçoWindows/registro/login externo autorizado. Este preflight não autoriza iniciar cliente/baixarconfig/editar runtime. Executor de produto cp36g ainda único writer; futura restauração mutável só depois do STOP/freeze source, em paralelo com reviews read-only. E/cp45-native-tunnel-preflight.json/md e STOP, routingGO.


cp45 TERMINAL/root hashes verificados: nenhumcloudflared.exe noPATHWindows, gateway8083 saudável; processosWindows/WSLcp43 ausentes e DNSfalho. Causa da saída não comprovada. Não encerrar/rotacionarprocessos com base em hipótese. root-cp45-receipt.json aceita sómetadata/plano e registra releaseoficial/SHApinned; nenhuma instalação executada. cp36g RED API159pass/8fail genuínos inclui WABA101resolvendonull (hipótese fonte confirmada), grant shapes e casos pré-protegidos que passaram. Primeiro allfalhou166/1 por índice novo de assertHTTP de duasoperações: a requisição de página era calls[2], não calls[1] (segunda era debug token do verify). É defeito do teste, não nova falha de produto; rawcp36g-api-all.log/exit1 permanecem imutáveis. Executor corrigiu somente índice e iniciou all2 completo nos bytes atuais, raw separado cp36g-api-all-2.log/preall2; PG/browser nunca rodaram na primeira tentativa, sem GREEN/pre-fixPG fabricado. Não promover source até resultado/reviews atuais.


cp36g TERMINAL sourceSTOP/freeze: all2 exit0 lint/build167unit+288PG+28Web+47browser=530/22migrações, genuine pre-worker/browser9 rootverificados/hashmanifestb8cb7ac56f304ca0383d58a1a00f1d9211f6e1f1108b0322481b2e52dbe55d61. Rootreceipt distingueRED159/8/prodantesinalterado, firstall166/1unitindexsemPG, segundoallatual530; somente spec mudou entre primeiroallfalho eall2. Nenhum raw regravado. SourceMetaad6d9.../specfd97.../PG650b... e seisadjacentes idênticos; app/device/externo não testadosporesteall. PacoteTQAcp36g completo aplicável/routingGO/bindingabsoluto pronto; iniciar reviewerfreshnativo e aguardarterminalsemdeadline. Novo candidato só depoisTQA limpo; final separadoapósartifactconcreto obrigatório. Nenhum sourcecommit/runtimeAPIativação.


Retomada solicitada pelo usuário: nove hashes cp36g e all2exit0 reconferidos, readiness PACED-Ready. Auditoria nativa anterior não deixou raw/parecer terminal; processo já não existe no ambiente retomado, exitcode anterior indisponível. Log original incompleto preservado. cp36g-tqa-resume-protocol.json registra falha objetiva de continuidade sem inventar resultado e admite UMA repetição fresh do MESMO pacote completo/dispatch/modelo/binding, sem reduzir rubrica nem aceitar self-review. Não substituir reviewer vivo por tempo; nenhuma instância anterior viva foi localizada. Fontes continuam congeladas e TQA/final/API/recovery pendentes.


Admissão cp46 antes da execução, após STOP/freeze produto cp36g confirmado: único writer DevOps pode baixar cliente PORTABLE nativo Windows cloudflared2026.10.0, assetoficial https://github.com/cloudflare/cloudflared/releases/download/2026.10.0/cloudflared-windows-amd64.exe, confirmar SHA86aee4017b26625cee8484c113558f48effa4cd47f7aa05fcf425604e5d2b23c antes de qualquer execução e versão correta. Apenas diretório novo privado de artefatos de teste artifacts/tmp/number-onboarding-execution/cloudflared-cp46, sem instalação/registro/serviço/tarefa agendada/admin/login/conta paga. Não substituir cliente existente; não tocar outros processos/projetos. Verificar ownproject gateway8083 e baseline setecontainers/cincovolumes antes do início; divergência não autoriza reset/recreate.

Novo processo/supervisor Windows nativo detached sob handle claro, target SOMENTE http://127.0.0.1:8083. Configuração vazia explícita e ambiente mínimo para não ler config/credenciais homedir; não repor HOME/home/CODEX_HOME. Checar flags na ajuda do binário confiável, usar HTTP2/TCP se suportado como experimento controlado, sem afirmar causa anterior. Drenar stdout/stderr continuamente em memória; persistir somente hostname gerado, categorias permitidas de conexão/erro sem texto cru e metadata de ownership (exe, binary/script hashes, native PID/creation/parent/argv/target) mais rollback guardado só do novo processo. Sem raw log, query/header/body/token ou segredo em argumentos/erros. Nenhuma alteração da origem API, privateenv, imagens/tags, containers, DB/provider/auth/Meta ou source/Git. Runtime API permanece antigo até TQA/final/sourcecheckpoint.

Provar DNS/HTTPSroot/health e JSd143 em WSL/Windows, observar múltiplas amostras monotônicas durante cerca de2min e sobrevivência a retornos de tool. Incluir GETcallback com challenge sintético: leitura em memória SOMENTE WEBHOOK_VERIFY_TOKEN de .env.testing e igualdade booleana com campo runtime permitidas pelo mesmo método seguro cp44 (stdin sem argvsecreto, TLS normal, sem logging de URL/query/response cru); tokenválido200/bodyMatchesChallenge e inválido/ausente403. Se token/origem/runtime divergirem, apenas registrar; não alterar segredos. Alvo público permitido só novo hostname guardado que retorna nosso bundle/gateway. Não provar Meta/WhatsApp/recovery por esses GETs; não alegar saúde contínua/permanência de DNS. Se falhar, restaurar apenas o novo processo por guardas de identidade; processos anteriores não serão encerrados. Registrar E/cp46-native-tunnel-restoration.json/md e lifecycle público seguro; root canon/Git exclusivo. Source9 congelado, TQA74259 read-only pode seguir paralelamente; nenhum outro code/runtime writer. Só após root aceitar transporte+challenge e TQA terminal será solicitado novo ajuste Meta, evitando interromper reviewer com configuração humana pendente. Routing cp46 GO, mesma infraestrutura local já autorizada no TODO.


cp46 concretização de flags antes da retomada: executor informou checksum/versão/gateway/baseline próprios verificados e ausência de --protocol na consulta `help tunnel run`. Uma consulta de ajuda malformada iniciou acidentalmente um Quick Tunnel; somente o processo recém-criado PID19108 foi encerrado por identidade nativa guardada, sem uso para evidência e sem afetar terceiros. Registrar esse incidente honestamente no artefato cp46. Não repetir consultas com --url; consultar somente `--help`, `tunnel --help` ou `tunnel run --help`, sem alvo, rede ou credenciais. Root verificou documentação oficial https://developers.cloudflare.com/tunnel/reference/run-parameters/: protocolo aceita auto/quic/http2, opção --protocol e variável TUNNEL_TRANSPORT_PROTOCOL. Admitir explicitamente o override público TUNNEL_TRANSPORT_PROTOCOL=http2 no ambiente mínimo do ÚNICO novo filho nativo se a flag não estiver disponível; não herdar variáveis TUNNEL_* ou credenciais. É a mesma seleção de transporte TCP já admitida, não nova capacidade ou causa comprovada da queda. Manter configuração vazia explícita/sem autoupdate e toda a rubrica cp46; não parar por ausência da flag se a alternativa oficial funcionar. Se nem flag nem variável forem aceitas, registrar falha concreta e STOP, sem criar túneis adicionais por tentativa. Routing existente está em foundation_documentation/artifacts/tmp/number-onboarding-execution/routing-cp46-native-tunnel.json (outcome go); sem alteração de modelo/escopo.


cp36g TQA TERMINAL exit0, rawb713bfb8520799597a37595e7e0fbfbb6415296b70cf2949fa03ea5f358a52fc e merge absoluto válidos. Workload completo/5perguntas/matrizes/camadas/DI/fences/bypass/performance/elegância/estrutura examinados. Nenhum novo defeito de implementação observado; parsing/interseção/fonte530 fortes. Um medium TQA-CP36G-01 Integrated/release-blocker de cobertura: faltam direct cases de data ausente, app_id não string/is_valid não boolean e omissões legítimas de scopes e target_ids irrelevante. Findings fonte anteriores TQA-CP36F-01/NUM-ROOT-GRANT-CP36G-01 verified-local nos loci, não aceitam entrega geral; D05/D07 aguardam cobertura atual, D06/VAL05 externos seguem abertos. Não reescrever o raw nem tratar exit0 como gate verde.

Admissão cp36h TEST-ONLY, execução SOMENTE após cp46 STOP (único writer runtime atual). Novo executor Coder pode editar apenas api-app/src/integrations/meta/meta.client.spec.ts; outros oito paths atuais totalmente read-only/byte-idênticos, inclusive Meta produto. Acrescentar três casos negativos estruturais acima (classe MetaIndisponivelError+code na MESMA promise, exatamente1fetch e fixedhost/auth) e dois positivos de omissão (grant granular válido com scopes omitido; entrada granular irrelevante válida sem target_ids; número exato+telefone e2fetchbounded), usando fetch double definido e válido, sem stub undefined acidental ou redefinir erro. Estes protegem comportamento existente correto/test-after; não há novo bug/RED honesto exigível, não editar produto ou fabricar falha. Depois run canônico all completo UMA rodada nos bytes congelados para renovar evidência e freshness9; guardar manifest9before/after/preall e genuinepreworker/browser pelos mesmos paths existentes, raw/command/exit sem relabel. Se surgir falha real, registrar antes de corrigir e manter raw. Root canon/Git; executor sem dotenv/.local-files/Git/runtime operador/provider/túnel/worktrees. Routing cp36h GO. TQA fresco completo aplicável e final separado continuam obrigatórios, novo candidato só após TQA limpo; nenhuma nova aprovação humana para esta cobertura dentro do contrato atual.


cp46 TERMINAL STOP, root conferiu JSONadbcccb4.../MDf2bcca71... e hashes do cliente/EXE ativo. Treze amostras142009ms de DNS/HTTPSroothealthJS200 em WSL/Windows e JSd143, challenge público válido200/match e inválido/ausente403, tokenpresence/equality booleans true. Setecontainers/cincovolumes próprios preservados; API/origem continuam antigos. Novo host comments-heart-gale-muscles.trycloudflare.com aceita apenas transporte bounded, não Meta salvo/WhatsApp/saúde contínua. Owner22836/child21180, cliente86aee... e EXEbdf680...; snapshot exato de C# compilado foi sobrescrito durante hardening, reprodutibilidade fonte-binário limitada e registrada, nunca alegar patch atual executando. Incidente help/duas tentativas supervisor falhas e cleanup próprio preservados; causa anterior desconhecida. Root public GETreadback adicional e recibo root-cp46-receipt.json. Nenhuma URL Meta solicitada enquanto cp36h/reviews continuam. cp36h executor ativado somente após este STOP.

Observação root CP46-LIFECYCLE-01/medium: rollback script cp46 sintaticamente válido guarda identidade/estado/exe/parent/target mas não confronta CreationDate REAL atual dos dois processos com as datas registradas, nem SHA do supervisor/argv exato. NÃO EXECUTAR este rollback até complemento. Não invalida GETs públicos observados ou atual ownership do processo, mas mantém ação destrutiva bloqueada. Reparo script-only será serializado após cp36h STOP, sem alterar binário/supervisor/túnel atual ou outros processos; nova evidência suplementar e syntaxcheck sem kill. Não enfraquecer guarda por ausência de metadata.


Admissão cp46b READ-ONLY durante cp36h writer: mesmo DevOps pode preparar metadata exata para futura ativação API-only. Guardar setecontainers/cincovolumes próprios; obter somente Config.Image/API label com.docker.compose.project.config_files/working_dir e projeto/service/owner, sem Config.Env bruto. Em API exata/ownlabels, node stdin pode ler apenas campos públicos NODE_ENV/WEB_ORIGIN/EVOLUTION_WEBHOOK_URL/PUBLIC_ORIGIN, emitir modo e booleans de origem antiga conhecida/nova cp46/interna esperada, nunca URL arbitrária/query ou segredo. Não ler privateenv/.local-files/provider/DB/auth ou executar mutação nesta etapa. Root leu compose: WEB_ORIGIN efetivo vem de CHANNELS_LOCAL_ORIGIN, não de WEB_ORIGIN do dotenv; PUBLIC_ORIGIN não tem consumidor em api/src ou web/src. Confirmar callback Evolution interno vs público em booleans para não confundir perda de túnel com bug de reconexão. Gatewayconf atual tem proxy_pass api estático, risco de IP cached após recreate; apenas registrar plano condicional de graceful reload do mesmo ownedgateway se IP realmente mudar/502 apósAPI, sem executar agora. Sem script/canon/Git/build/restart/túnel/arquivo; salvar E/cp46b-activation-readiness.json/md e STOP. Hardening rollback CP46-LIFECYCLE-01 permanece postergado até cp36h STOP.


Admissão condicional cp46c, SOMENTE após cp36h writer STOP: DevOps pode fortalecer apenas stop-cp46.ps1 no diretório próprio ignored cp46 e salvar complemento E/cp46c-lifecycle-guard.json/md. Pinar identidade do owner22836/child21180 por executável/parent/argv COMPLETOS/SHA cliente86aee.../SHA supervisorbdf680... e tempo REAL de criação native (Get-Process.StartTime ticks ou CreationDate atual normalizado com precisão declarada) contra cp46 imutável e rootreceipt, não apenas contra runtime-state JSON. Prender handles dos mesmos processos quando possível antes de decidir ação, falhar fechado para ausente/divergente, sem tolerância de tempo ampla ou fallback PID-only. Estado/log não é autoridade para aceitar outro processo. Manter target exato8083 e configuração vazia. Script não encerra recursos antigos/alheios. Permitir -ValidateOnly explícito para testar guardas em read-only (inclusive controle negativo com tempo/expectativa deliberadamente errados); NUNCA executar kill/Stop-Process nessa tarefa. Syntaxcheck e prova somente validação atual, preservar source9/candidato/runtime7/5/túnel. Não recompile/substitua/edite binário/collector ativo nem alegue snapshot de build recuperado. Registrar hashes scriptantes/depois, atualmetadata ownerchild segura e resultados das guardas, sem rawlogs/query/segredo. Sem privateenv/DB/provider/Meta/auth/API/configGIT/canon. Mesmo routing DevOps cp46 GO, única mutação script-only após STOP, em paralelo apenas com reviewer read-only.


cp36h TERMINAL STOP/freeze, canônico all exit0:172unit+288PG+28Web+47browser=535/22migrações, raw588d37e0... e manifest94130344d...; root-cp36h-validation-receipt.json confere before=cp36g, somente spec2d6a7be4... mudou, oitoadjacentes idênticos. AMBAS attestações genuínas dos nove paths, sourceHEADs originais e JSbuilt=servedd143 conferidos. Sem novo RED ou mudança de produto; h protege comportamento correto existente conforme achado. Iniciar TQA completo fresco/routinghGO com bindingabsoluto, sem deadline ou limitar detecção ao últimoachado. Final distinto após TQA+candidato atual. DevOps cp46c pode agora atuar SOMENTE no script rollback admitido, fonteproduto congelada e TQA read-only em paralelo; nenhuma API/origem/candidato alterada.


cp36h TQA ativo nativo session51854, pacote cp36h-tqa-package.md/dispatch absolutos/routingGO, fonte94130344d congelada. Nenhum outro reviewer vivo substituído, nenhum resultado presumido. cp36g TQA terminal permanece parecer histórico independente; h pass completo poderá aceitar/rejeitar com detecção plena, não apenas reapreciar cinco casos. cp46c é somente script ownrollback em paralelo, API/produto/privados intocados.


cp46c TERMINAL STOP, root verificou hashes JSONd25188a4.../MDc8f90ae2... e script8c084a66...; leu guardas de criação nativa100ns independente de stateJSON, CIM1us com truncamento inteiro/handles/argv completos/parent/hashes/config. ValidateOnly real passou e ticks errados rejeitados sem kill; binários/túnel preservados. CP46-LIFECYCLE-01 verified-local; rollback real não exercitado. Fonte C# compilada ausente continua limitação explícita. cp36h TQA permanece único reviewer de produto atual, scriptwriter STOP; candidato/API/sourcecommit ainda aguardam gates.


Retomada2026-10-17: fonte9 cp36h/all535 preservada e readiness PACED-Ready. TQA51854 anterior não deixou raw/parecer terminal; PID11955 ausente e unifiedexec desconhecido. Log incompleto e metadata originais preservados em cp36h-tqa-resume-protocol.json, exitcode indisponível, sem parecer fabricado. Admitir UMA repetição fresh do MESMO pacote completo cp36h/dispatch/modelo/effort/binding absoluto, sem reduzir rubrica nem substituir reviewer vivo. Routing-resume GO. Nenhuma imagem/sourcecommit/ativação/retomada real realizada.

Admissão cp48 READ-ONLY antes da execução: DevOps fresco pode verificar transporte cp46 por hostname conhecido/roothealthJS em WSL/Windows, identidade nativa dos processos22836/21180 por datas/exe/hash/parent/argv (sem executar rollback), gateway8083, setecontainers/cincovolumes próprios usando cp46b/rootreceipt como baseline64chars. Nenhum kill/start/reload/build/recreate/tag/config/source/Git/privateenv/Config.Env dump/DB/provider/auth/Meta. Não baixar/abrir novo túnel. DNS/PIDs podem ter mudado; registrar causa conhecida vs hipótese e plano concreto, sem interferir em terceiros. E/cp48-resume-readiness.json/md e STOP; root canon exclusivo. Fonteproduto9 congelada, TQA pode ler em paralelo. Routing cp48GO, mesmo runtime de testes já autorizado.


cp36h repetição completa ativa session89539/PID nativo no live-session.json, mesma hash de pacote2f8b0315.../dispatch/binding/modelo/effort. WSL boot_id mudou em relação à tentativa anterior; motivo da reinicialização não inferido. Child em nova sessão POSIX para isolar lifecycle de sinais do shell, sem promessa de sobreviver a reboot. Fonte9/535 preservados; cp48 verifica readiness hoje, cp46 saudável é histórico até nova conferência.


cp48 TERMINAL STOP2026-10-17, root verificou JSON543e5a36.../MD6a5cd641...: DNS/roothealthJS200 em Windows/WSL, JSd143 igual, nativeowner22836/child21180 com mesmoStartTime/exeSHA/parent/argv/target confirmados mesmo após bootWSLnovo; setecontainers/cincovolumes próprios preservados, API antiga c2e8... continua. Root conferiu também HEADs API/Web e changed-public-set8+1 exatamente iguais à attestation535, além dos novehashes. root-cp48-receipt.json aceita somente readiness/preservação, sem nova API ou recuperação de WhatsApp/Meta. Não criar outro túnel ou solicitar troca adicional de URL por esta retomada. TQA89539 completo continua read-only; DevOps STOP até gate/candidato.


Admissão CONDICIONAL cp47, não ativar antes de TQA cp36h atual terminal/aceito pelo root: único DevOps poderá construir UMA candidata API isolada da fonte9 atual4130344d3093891069681e0c78f6c364df68b0d92f10cdae6625269fa44507be, tag nova leadshug-channels-api-candidate:cp36h-4130344d3093 (recusar se já existir sem ownership inequívoco). Mesma principal/Dockerfile real/contextoapi-app/.dockerignore excluindo dotenv/.local-files/.git, sem buildargs/env privados. WindowsDocker contexto próprio atual; confirmar source9 antes/depois e setecontainers/cincovolumes contra cp48/cp46b. Labels owner=number-onboarding/checkpoint=cp47/source-manifest=4130344d...; preservar candidatos cp39/cp40 e tag/imagem de operador. Probe único efêmero com --network none/--read-only/sem portas/volumes/envargs/entrypoint substituído, sem iniciarAPI/migração/DB/provider. Provar Node22/Alpine/OpenSSL3/Prisma/Metaexports/helper e hashes dos quatro módulos compilados alterados (channels.service, convergencehelper, evolutioncontroller, metaclient) para ligar futura imagem servida ao artefato; só ler código público do container isolado. Remover somente probe próprio com guardas; não alterar source/config/privados/Git/runtime7/5/túnel ou autenticar. E/cp47-candidate-build.log/json/md com rawsha/ID/manifest/probe/preservação e STOP. Só após final independente e sourcecheckpoint local a candidata poderá ser retag/servida por API-only, fora desta admissão. Routing cp47GO; nenhum novo contrato/dependência/stack.


cp36h TQA TERMINAL exit0/raw17e5a2e70fa43ecc87eb636b95730dfe19b8bc4d2b914759dfbd9992cd6a38d2/merge/schema/binding absoluto válidos. Full workload/matrizes/5perguntas e todos9paths examinados, evidência535/freshness9 forte; performance/elegância/estrutura aceitáveis, fitmixed por externo. H01 medium Integrated/release-blocker: falta unitário direto de grant válido-shaped revogado(is_valid:false), distinto do tipo não-boolean. Nenhuma mudança de produto indicada. R01high Integrated mantém requisito VAL05 já aberto, não invalida plano de teste privado autorizado nem exige renovação de permissão para a mesma interrupção. TQA não aceito como limpo; gcinco casos anteriores verified-local, D05/D07 pendentes de H01.

Admissão cp36i TEST-ONLY antes de editar: único Coder pode alterar SOMENTE api-app/src/integrations/meta/meta.client.spec.ts, outros8hpublicpaths/read-only/byte-idênticos. Um caso DEDICADO de grant estruturalmente válido, app_id correto/scopes+granularinterseção corretos, is_valid:false, credentialscoped e fallbackphonepage válido. Assert SAME rejection classe real+code, exatamente1debugfetch fixedGraphhost/auth e zero consulta phone_numbers; sem enfraquecer/renomear testes existentes/refatorar fixture/produto. Protege comportamento existente correto, test-after, sem RED fabricado. Capturar manifest9before=h/after/preapi e somente spec mudou. Executar runner canônico API leaf bash scripts/test-channels-local.sh api UMA rodada (lint/build/unidade+PG/22migrações; esperado173+288, registrar real), rawcommand/exit/log cp36i-* preservados. Web28/browser47 h podem ser REAPROVEITADOS honestamente pelos8paths byte-idênticos e unit.spec excluído por tsconfig.build.json(**/*spec.ts), nenhum consumidor/build/Web/runner/PGtest mudou. Não rodar/relabel all536 nem copiar/alterar attestationh como se tivesse hashunitnovo; recibo composiçãoAPIatual+Web/browserh original com limites explícitos, sha de ambas h e prova oitoimutáveis/exclusão do build. Novo TQA fresh FULL aplicável julgará composição atual+todos9, sem reduzir workload/detecção ao caso novo; final distinto e candidato atual depoisTQAaceito. Fonte/operador/privateenv/.local-files/Git/túnel/provider/DBoperador/worktrees proibidos ao Coder; runner só namespace descartável canônico. RoutingiGO, cp48STOP, rootcanon/Git exclusivos. Nenhuma aprovação humana nova para testar este contrato.


cp36i TERMINAL STOP: somente spec mudou para9612cd1c..., oito paths idênticos a h; manifest9 af21e98e41ec1ba86f4dac877ba2bd69b3ff0857fba930ca1c3973428723b581. API leaf canônico UMA rodada exit0/lintbuild/173unit+288PG/22migrações, rawf943d9049c06ce39a25be958228100051389fc190452c1b3d10ccb403f1778c1. root-cp36i-validation-receipt.json e public-set receipt conferem hashes atuais, HEADs, changed-public-set8+1, duas attestações h imutáveis e tsconfigbuild exclui spec. Composição é APIi461 + Web28/browser47 HISTÓRICOS h de fonte consumidora inalterada, não novo all536 ou freshness9 browser atual. Test-after de comportamento correto, nenhum RED fabricado.

Perfil Assurance/Tester-Quality, escopos NestJS/Prisma/PostgreSQL/React/Vite/Docker; Genesis não aplicável ao contrato aprovado existente. Novo TQA cp36i FULL fresh sem contexto ativado session47512/PID9741/modelgpt-5.6-terra/max/routingGO, pacoteSHA1f8d79897ecd6d16768238f48960bf0797610b6055a6d7875840d5072e1feaf2 e dispatch absolutos. Rubrica completa/all9/5perguntas/matrizes/detecção irrestrita no escopo; nenhum reviewer vivo substituído ou prazo rígido. Fonte9 congelada, nenhum writer produto/runtime ativo; root é único dono canon/Git. H01 permanece aberto até adjudicação; final distinto/candidato/API-only/retomada/VAL05 pendentes. Admissão cp47 anterior h NÃO ativada e será substituída pela atual i SOMENTE após TQA aceito.


cp36i TQA TERMINAL47512 exit0, rawSHA26779259e39792e8848556b6927ca545e5e09d397e2541b694e67bf50c07b872/schema/merge/binding absoluto válidos. Full aplicável/all9/5perguntas/matrizes/DI/bypass/fences/freshness/eficácia e eficiência examinados, sem novo defeito de fonte/testes e nenhuma mudança de produto recomendada. Performance/elegância/estrutura acceptable; fitmixed por externo. H01 verified-local no locus. R01high Integrated é VAL05 já obrigatório aberto; R02low Integrated exige preservar composição honesta já existente, sem novo all536/browser/servedclaim. Root aceita APENAS pré-requisito privado de fonte/testes; D05/D06/D07 Exception até final e provas externas. root-cp36i-tqa-adjudication.json.

Admissão cp47 atual SUBSTITUI a condicional h anterior sem ativá-la: único DevOps pode construir UMA candidata tag leadshug-channels-api-candidate:cp36i-af21e98e41ec de manifest9 atual af21e98e41ec1ba86f4dac877ba2bd69b3ff0857fba930ca1c3973428723b581. Aplicam-se integralmente guardas cp47 anteriores de contexto/Dockerfile/dockerignore excluindo privados, source9 beforeafter, labels owner/checkpoint/source, setecontainers/cincovolumes cp48 preservados e probe networknone/readonly/sem envargsportvolumes/entrypoint substituído, com hashes4compilados. Routing cp47GO. Fonte/API/origem/config/segredos/DB/provider/túnel/Git/canon intocados; não servir/retag operador. Buildlog/resultados próprios E/cp47-candidate-build.* e STOP. Só depois final independente/sourcecheckpoint haverá admissão separada API-only. Nenhum writer produto/runtime paralelo; root canon/Git exclusivo.


cp47 TERMINAL STOP: candidata tagcp36i-af21e98e41ec/imagefe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821, buildexit0/rawSHAe353c4b8... e fonte9 beforeafteraf21e98e... iguais. Probe efetivo offline/readonly/entrypointnode confirmou Node22.23.3/Alpine/OpenSSL3.5.8/Prisma6.19.3/artifactmusl/exports e hashes4compilados. Primeira tentativa stdin foi no-op/sem script/output, nenhum check inferido; segunda node-e efetiva, ambas removidas. Prisma proxy instanceoffalse explícito, nenhum DBquery/compatibility inferido. Root-cp47-candidate-receipt.json confirma hashes/actualcandidateIDlabels/source9 e setecontainers/cincovolumes reais preservados; API antiga permanece. Ownership de runtime é com.leadshug.channels.owner conforme Compose. DevOps STOP, nenhuma ativação/private/source/Git/config/túnel alteração. Diffguard771/771GO antes de evidência posterior.

Admissão final-review atual: fresh no-context gpt-6.1-sol/max, distinto dos executores e TQA, routing cp36i-finalGO, pacote completo cp36i-final-package.md/dispatch absoluto. Julgar todos9/candidata/evidência/aderência/P1P2/rulespirit/security/performance/elegância/estrutura/debt, sem resposta esperada nem reabrir arquitetura sem defeito material. Pode escrever SOMENTE rawresult do parecer como exceção de artefato, nenhuma mutação produto/runtime/canon; rootmerge/adjudicação depois terminal. Fonte9 congelada e nenhum writer produto/runtime ativo. Gate não pode dispensar D06/VAL05 nem fechar TODO geral.


Final fresh /root/final_cp36i_current_candidate ativado com fork_turns:none/gpt-6.1-sol/max, pacoteSHA2a824e9cde7ae79ac21e037fbf130cdefd8c49702622fe29a798bc5129b7cd71/dispatch absoluto. Único reviewer final atual, no-context distinto do TQA/execução, rubrica completa/source9/candidata; fonte congelada, DevOps e Coder STOP. Raw esperado cp36i-final.result.raw.json, root fará merge/adjudicação após terminal; nenhum deadline ou resultado presumido. API antiga/origem inalterada/VAL05 aberto.


Final atual TERMINAL /root/final_cp36i_current_candidate, raw/merge/schema/binding válidos, sem defeito de produção/P1P2 ou regressão estrutural observados. Root escolheu opçãoC explicitamente oferecida por FINAL-CP36I-01 SOMENTE para checkpoint privado não oficial: guard app_id presente/correto, proteção de regressão isolada NÃO alegada, caminho Evolution não consulta Meta grant. Achado permanece release-blocker do mesmo TODO com owner Coder/Assurance e prazo ANTES etapa oficial real e entrega local/VAL06/DOD06/closeout. Não declarar final limpo/Local-Implemented/entrega. Fonte9/candidata exatas permanecem congeladas e podem ser checkpointadas localmente para teste privado já autorizado; nenhuma reclassificação por tempo ou redução de detecção/auditoria. R01 externo mantido; R02 restrição OWNER existente; 02docs integrado nos resumos vivos.


Sourcecheckpoint local PRIVADO CONDICIONAL concluído, sem sourcepush/gitlinks: API7e948c3045da736f7db1f8e97825cf6384777e4f/Web34408c47b4f2f935291d5fc9934f5118b5516bd4. Guardas GitGO e staged/committed9 blobs byteexact manifestaf21e98e...; cp49-committed-source-attestation.json faz ponte honesta aos HEADs originais de execução, não afirma testes nos commits novos. Final permanece condicional/FINAL01 release-blocker antes oficial/entrega; não há claim Local-Implemented.

Admissão cp49 ANTES execução, único DevOps/projeto WindowsDocker leadshug_channels_local, candidata fe5fb7... exata. Permitir SOMENTE API-only activation e origem pública verificada comments-heart-gale-muscles.trycloudflare.com, depois MESMA interrupção Evolution própria já autorizada. Privado exception explícita: ler .env.testing bytes SOMENTE em memória para mudar APENAS CHANNELS_LOCAL_ORIGIN, preservar todos outros bytes/lineterminators/permissões, comparar bytes em memória antes de escrever/recusar concorrência, nenhum backup/hash/output do arquivo ou segredos; original só memória para rollback. Compose normal pode consumir arquivo privado existente como config, sem dump/extraedição. Login OWNER normal pode ler SOMENTE CHANNELS_BOOTSTRAP_OWNER_EMAIL/PASSWORD em memória para HTTPS próprio verificado, cookies/CSRF/password só memória/sem argv/log/body/query; sem novo bootstrap/tenant/wizard/reset. Provider GET próprio bounded pode usar adapter/credenciais runtime apenas em memória para OPEN/igualdade de identidade, nenhum Config.Env dump ou telefone nos resultados. .local-files continua absolutamente proibido.

Guardas cp49: antes API confirmar hostTLS/JSd143/owner nativo atuais e setecontainers/cincovolumes baseline cp47/48. Retag somente candidata aceita para ownedtag leadshug_channels_local-api; mesma Compose/privateenv/overlay/profile, up -d --no-build --no-deps --force-recreate api, nunca start script up/buildstack. API novaID/imagem e hashes4compilados exatos;6outros e5volumes preservados, NODE_ENVproduction/origemcurrent; nenhum schema novo/DBreset. Gracefulreload SOMENTE gateway próprio seIPAPI mudou E502staleupstream constatado, sem recreategateway. Rollback sóprópriaAPI/env/tag sefalhar. Login/readiness/normalverify ANTES do restart pode estabelecer baselineCONECTADO/identity/gen/epoch/receipt/currentattempt/version/conversas. Depois SAMEEvolutionIDstop/start com finallyrestore, ZERO adminverify/pair/retry/advance após restart antes prova automática. Exigir connectedAt/update novo >restart ou transição nova, providerOPEN/identity/epoch/receipt atuais, SAMEattempt/version/histórico, nãocachedCONNECTED. SemSQLrepair/QRrenew/fakewebhook/agentoutbound. E/cp49-api-activation.json/md +cp49-unofficial-recovery.json/md e STOP. HumanoINOUT02 separado depois; oficial NÃO iniciar até FINAL01 resolvido; TODO Pending/VAL05/D05D06D07 Exception. Routingcp49GO; rootcanon/Git exclusivo, nenhum outro writer ativo.


cp49 preflight TERMINAL STOP antes de mutação: transporte/TLS/JSd143/identidadecp46/candidata/sourcecommits/7containers5volumes conferidos, mas campo público único CHANNELS_LOCAL_ORIGIN no privatefile não era igual ao antigo WEB_ORIGINruntime inferido ou currenthost. Nenhum valor/hash do campo ou conteúdo privado registrado; sem edição/credenciais/Compose/API/provider/DB/Evolution. cp49-origin-preflight-stop.json. Suposição root invalidada: origem no arquivo não foi previamente verificada e não precisa igualar a runtime antiga. SUPLEMENTO antes retomada: manter campo único/bytesconcorrênciaguardados/currenthostTLSJSown verificado; autorizar substituir APENAS origem pública mesmo que oldvalue desconhecido/diferente, valor anterior somente memória para rollback, sem imprimir/hash/seguir. Todos outros bytes/terminadores/permissões existentes0777 preservados, nenhum chmod/backup/segredo extra. Não abrir nova URL/túnel/repetir aprovação. Mesma admissão cp49/routingGO, único DevOps pode retomar o processo integral com essa única correção de precondição; fonte/candidata/gates/D02/VAL05 inalterados.


cp49 TERMINAL STOP: APIc138a845... saudável/imagefe5fb7..., origem pública comments... atualizada APENAS no campo público, owner login/readiness e quatrocompilados exatos. Normal ADMINverify ANTES restart reconciliou baselineCONECTADO/currentattemptv2/genepoch1/receipt/owner semlease, apesar DTOoperação PENDING_RECEIPT (não tomado comoestado). SAMEEvolutionID stop/start UMA vez04:13:00.392→04:13:01.849UTC; automaticconnectedAt04:13:15.384 capturado04:13:16.521, SAMEattemptv2/epochgen1/receipt/currentidentity/conversa2msgs preservados, sem postrestartadminverify/pairing. Sódepois providerGETbounded confirmouOPEN/identity. root-cp49-runtime-recovery-receipt.json verificou hashes/provas/actual7containers/compiled4/publicTLSroothealthJS. Não saúde contínua/entrega humana02/oficial. Consulta inicial mais ampla de metadata da BU ocorreu, sem contato/conteúdo/telefone/PII/mutação ou IDs alheios persistidos; registrada e restrita depois ao UUID cp33. Campo executor privateFileOtherFieldsReadOrChanged=false é esclarecido no recibo root: OWNERemail/password foram lidos em memória conforme admissão; nunca alegar que não houve leitura dessas duas chaves autorizadas.

Pergunta humana INOUT02 emitida via async: abrir host atual, outro aparelho envia teste02 ao mesmo vínculo e responder pela mesma conversa; resultado obrigatório ainda pendente. Nenhuma resposta inferida pelo tempo. Prova de entrada/resposta humana anterior cp33 permanece separada.

Admissão cp36j ANTES editar, SOMENTE após DevOps cp49 STOP confirmado: único Coder pode editar APENAS api-app/src/integrations/meta/meta.client.spec.ts para UMA negativa dedicada de app_id estrangeiro com todos demais campos válidos (is_validtrue/ambosscopes/interseçãoWABA correta/token scoped/fallbackphonepage válido). Provar SAME rejection classe real+code, exato1debugGraphhost/auth e zero phonequeries; preservar todoscasos existentes/nenhum refactor/skip/retry/fallbacksemdefinição. Corrige FINAL-CP36I-01 de cobertura existente correta, TEST-AFTER/semREDinventado/produtointocado. Beforemanifest9=i af21e98e..., outros8 byteidênticos; sourceHEADs agora API7e948c3/Web34408c4 committedbyteexact (não HEADs de execução histórica h/i). Run APIleafcanônico bash scripts/test-channels-local.sh api UMA rodada/namespaceleadshug_channels_validation PGdescartável, lintbuild/unidade+PG/22migrações, esperado174+288 registrarreal/raw/command/exit/manifests9. Compôr HONESTAMENTE novoAPIj +Web28/browser47 h originais de consumerbytesidênticos e spec excluído unchangedtsconfig44e82cf..., sem all537/browserfreshnessnovo/rewrite deattestation. RuntimeAPI/Evolution/QR/túnel/.envtesting/.local-files/DBoperador/auth/provider/canon/Git proibidos ao Coder. Rootcanon/Git, ainda poderá receber resultadohumano e fazerreadbackscoped somente após STOPunitwriter se necessário; nenhuma interferência no produto servido por imagemfe5fb7 de productionbytesidênticos. RoutingjGO. Depois obrigatório freshTQA FULL aplicável/9/currentcomposition e finaldistinto, semdetecçãoreduzida ao últimoachado. Não reimplantarAPI por mudança somenteunitária/excluídadobuild: imagem atual i temsource-manifestlabel i preservada e será reusada SOMENTE com ponte explícita de oito bytes/build-neutralidade/compiled4, sem fingir buildj. DeadlineFINAL01 antesoficial/entrega permanece atéaceite.
