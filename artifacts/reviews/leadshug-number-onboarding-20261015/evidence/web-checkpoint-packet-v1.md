# Frozen Web checkpoint review v1 — ST-CON-01

Derived non-authoritative diagnostic checkpoint after bounded Web remediation, BEFORE real-backend browser/runtime integration. No final delivery/security/TQA/PCV or provider readiness claim. Read COMPLETE packet and independently assess concrete Web correctness, stale effect/callback/lifecycle behavior, permissions, transient secret handling, SDK user gesture, duplicate/replay handling, persisted resume, current-stage display, number/WABA/cursor selection and maintainability relative to approved scope. Do not run tests/network, edit product, read private env/auth files, create goals/worktrees/children, or inspect changing API source. Only write designated native JSON report.

Web writer STOPPED; branch feature/number-onboarding at baseline4e56f6c1f4515b918d05b8c87e890d42e8542c56 + frozen six source files. Build passed and25unit tests passed in Node22; six hashes verified. Earlier root source findings are included with exact evidence; declared fixes are not verification. Re-raise any defect still present with concrete behavior and discriminating browser test. Browser/realSDK proof is explicitly absent and still required later; do not label that acknowledged phase boundary itself as a new API defect.

API checkpoint2 historical response boundary: POST registration returns {attempt,nonce,replay}; GET/authorize/advance/retry/cancel returns safe direct attempt DTO; POST confirm returns {registration:attempt}. Capabilities and safe BU/channel shape are in included types and frozen TODO; server independently proves all IDs. Existing pending-auth nonce can only be replayed with same original idempotency key/session and must not be invented/persisted in browser. Server options for selected WABA may return only that WABA plus selected number page. Pair returns {channelId,attemptId,generation,pairingEpoch,state,qrcode}; provider QR/string does not certify identity/receipt. Explicit verify returns {status,ownNumberVerified,receiptVerified}, not receiptVerifiedAt. API independent review found18implementation defects; all accepted for in-contract remediation now underway, API will refreeze before integration. Do not inspect the live changing API or assume those defects fixed. New manually initiated conversations are ST-CON-04 and excluded; Inbox.tsx edits not authorized.

Return subagent-review-result-v1 review_kind architecture_adherence. Include precise path/line or function evidence and a concrete interleaving for each finding; avoid speculative scaling/style blockers. Overall assessment must attest packet SHA and complete input read and say diagnostic Web checkpoint, not final TODO approval. Source hashes refer to original bytes; text blocks normalize LF.

## Snapshot: foundation_documentation/project_constitution.md

Original SHA256: f9b8d3397a4f78c74f4c29739eb509d12bfc9ccda84a50fed718bfe7a668566a

````text
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
````

## Snapshot: foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md

Original SHA256: 444772a8eeca903e4fd9e6ceffd4435d99c8531633ca6cb4fa51ec7d0d48db1e

````text
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

Duas admissões de testes em execução estão detalhadas abaixo. Classificação de gitlinks preexistentes no workspace não concede permissão de alterá-los manualmente. Outras fixtures encontradas necessárias devem ser admitidas antes de editadas; não modificar expectativas de negócio só para passar tests.

- `test/realtime.e2e-spec.ts`: guard de execução encontrou path não classificado. Diff inspecionado pelo orquestrador: somente import do helper `criarCanalVerificado` e substituição da criação direta de BuChannel pela fixture completa de identidade/credencial; nenhum assert, cenário ou comportamento de socket alterado. Necessário para preservar a prova de push scoped após o ingresso passar a exigir identidade durável. Classificação: concretização de fixture da validação SCOPE-07/09 já autorizada, sem nova capacidade, objetivo ou risco material. Admitido esse path exato, sem abrir `test/**`; nenhuma dispensa do guard. A edição precedeu a admissão, falha de sequência registrada e corrigida antes de qualquer entrega; executor instruído a consultar antes de novos paths.
- `test/modulos.e2e-spec.ts`: novo guard encontrou expectativa201→409 em duas chamadas do endpoint aposentado. A constituição exige atualização correspondente de testes de contrato na mesma entrega; esse path é concretização da validação já aprovada, sem ampliar capacidade ou superfície de produto. Admitido o path exato para aposentadoria E provas positivas na nova jornada. A alteração atual não é suficiente como prova positiva de módulo/piso: nomes ainda alegam conexão mas só409 não a exercita; achado de qualidade aberto para correção após a revisão congelada. As negativas404 de teto/contratação devem ser preservadas. Segunda falha de sequência registrada; não concede `test/**` nem dispensa gates.

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
| strategic-cto | operational-coder | Implementar somente contrato aprovado. | API/Web/canon owner | active; aprovação/authority go registrados, checkpoint1 concluído e checkpoint2 API em execução. |
| operational-coder | assurance-security-adversarial | Revisar correção/segurança/aderência da API antes da integração do consumidor. | Pacote API congelado e relatório, somente leitura de produto | active; routing-api-checkpoint-review-v1 go; writer API parado, revisão não equivale ao gate final. |
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
| WEB-ROOT-01 | high | release-blocker | fix-current-contract | SDK readiness perdido após reservar tentativa | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-02 | high | release-blocker | fix-current-contract | Consumo incorreto do wrapper registration da confirmação | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-03 | medium | release-blocker | fix-current-contract | Retomada persistida e cancelamento explícito necessários | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-04 | medium | release-blocker | fix-current-contract | Etapa no wizard precisa refletir webhook/receipt atual | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-05 | medium | release-blocker | fix-current-contract | Retry de reserva perdida precisa conservar chave idempotente | accepted-open | evidence/root-web-checkpoint3-findings.json |
| WEB-ROOT-06 | medium | release-blocker | fix-current-contract | Troca explícita de WABA não pode perder opções autorizadas | accepted-open | evidence/root-web-checkpoint3-findings.json |


Adicional de coerência do autor: envelope raw redigido e code/PIN transitórios explicitados, sem alterar modelo de autorização; REG-SEC-08/09.

Adjudicação do checkpoint API: parecer bruto imutável api-checkpoint-review-v1.json (SHA256 e44b11aed763a452afcf1786e04e30a2a1d91ae012e3d0bd743c0281322028ee), schema nativo validado,18 achados (5high/12medium/1low), leitura completa de68 snapshots atestada. Root aceita os18 para correção no contrato atual: todos correspondem a D-01..08, limites contra legado, audit/segredos ou harness já exigidos. Não há dispensa, nova capacidade, worker, outbox ou autorização de runtime legado. Severidade baixa de NUM-API-18 não reduz o requisito explícito de metadata allowlisted. Solução deve ser simples e coerente; executor reportará qualquer necessidade de path ou decisão material ANTES da edição. Etapa pré-consumer, não gate final: correção e testes discriminantes ainda pendentes. Web termina/paralisa primeiro; API é o próximo writer único. Root permanece em orquestração documental; produto fica com Operational/Coder e runtime com DevOps.

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
````

## Snapshot: foundation_documentation/modules/integrations-and-channels.md

Original SHA256: 66d6a57429ae78e6dcc1ed8af70de2723e256c9deff70e1a073e83b9db2018bc

````text
# Module: Integrations and Channels
**Version:** 1.0

Owns Meta Cloud API, Evolution/Baileys, outbound webhooks, API keys and transport adapters.

## Invariants

- Providers are adapters; business workflows do not depend on provider payload shape.
- Secrets never enter logs, docs, fixtures or client bundles.
- Provider failures become deterministic application errors.


## Cadastro de números ST-CON-01

Contrato aprovado pelo usuário em2026-10-15 no [TODO governante](../todos/active/features/TODO-leadshug-channel-connection-readiness.md), documentação publicada3302964c. Estado: **Approved, implementação e verificação pendentes**. Owner: integrations-and-channels, escopo Mantenedora/BU; mantém constituição e políticas de isolamento. O módulo é autoridade do contrato; o TODO registra execução/evidência. Fonte API em api-app; Web em web-app.

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

### Segredos transitórios e webhook raw

Code SDK e PIN podem existir transitoriamente no formulário/memória do browser e seguir via BFF HTTPS; nunca em URL, storage, trace, screenshot, log ou DTO de retorno. Token, chave e envelope ficam somente no backend. Antes de persistir evento raw de provider autenticado, redigir recursivamente apikey, token, authorization, code, PIN, QR e componentes secretos de URLs; erros/audit usam catálogo e metadados allowlisted. Evento sem identidade verificada não persiste conteúdo. Harness envia envelope Evolution com apikey fictícia e comprova sua ausência em raw/audit/DTO/erro. QR só é devolvido efemeramente ao administrador no POST autorizado. Gateway Nginx, proxy e logs de aplicação não registram URI/token do callback Evolution: política explícita remove caminho secreto e query de access/error logs, inclusive erros; harness passa segredo fictício pelo gateway real e inspeciona logs/artefatos. Callback por header só se suportado e comprovado no provider fixado, sem presumir capacidade.

Meta raw é particionado por recurso verificado/BU, não por corpo de request inteiro. Batch assinado com entry/change/value de BUs diferentes produz registros scoped separados; fragmento desconhecido/retirado/sem identidade contribui apenas metadados allowlisted, sem conteúdo. Assinatura é verificada sobre o corpo original antes de parse/partição. REG-SEC-12/13 concretizam requisitos já existentes de segredo/owner, sem novo armazenamento genérico.
````

## Snapshot: foundation_documentation/modules/identity-and-tenancy.md

Original SHA256: 604371cc509981d4561ce3cf404857990e5d30126ea04bda2a766aa0eeee1c91

````text
# Module: Identity and Tenancy
**Version:** 1.0

Owns authentication, accounts, Mantenedoras, Setores, Business Units, roles and BU grants.

## Invariants

- Every request resolves one tenant/account context.
- Permissions are materialized at the BU boundary.
- Roles are `OWNER`, `ADMIN` and `ATENDENTE`.

## API Endpoint Definitions

The canonical BFF contracts live under `api-app` and must be documented here before new endpoints
are introduced.


## Autorização do cadastro de números ST-CON-01

APROVADO em2026-10-15; implementação/verificação pendentes no [TODO](../todos/active/features/TODO-leadshug-channel-connection-readiness.md). Jornada e endpoints pertencem ao [owner de canais](integrations-and-channels.md#cadastro-de-números-st-con-01).

- Endpoints /api/bff/number-registrations e pairing/verificação de canal passam pelo middleware de sessão e anti-CSRF existente; pairing é POST, GET antigo não tem efeito externo.
- Conectar/reautorizar BU existente exige ADMIN na BU da Mantenedora verificada; criar BU exige ADMIN na Mantenedora e reutiliza transação/expansão de grants de TenancyService. ATENDENTE não ganha gestão por UI.
- Validar permissão antes de revelar estado ou erro de payload: sem sessão401, recurso fora do contexto404, papel insuficiente403. Revalidar grant/sessão após HTTP antes de ativar candidata ou promover observação.
- Tentativa oficial liga usuário/Mantenedora/BU/hash de sessão/nonce com expiração10min e consumo CAS; code/nonce consumidos ou ambíguos exigem tentativa nova. SDK IDs são candidatos, nunca autoridade.
- Nova BU, reserva/tentativa e grants/audit são atômicos. Mesmo Idempotency-Key e payload devolvem a mesma tentativa; payload diferente409; reautorização usa slot existente e expectedGeneration.
- ProviderResourceIdentity conserva owner de BU após remoção de canal e não é transferível entre BUs neste recorte. Webhooks têm autenticação própria e só passam conteúdo após identidade corrente comprovada.
````

## Snapshot: foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-web-checkpoint3-findings.json

Original SHA256: 56a3850b19034074529cea3acd95abf8f2dbc4e0392005bbe7abc3c8606d6684

````text
{
  "kind": "root-diagnostic-findings",
  "date": "2026-10-15",
  "scope": "checkpoint3 Web; source inspection only, not formal delivery review or browser evidence",
  "source_manifest": "checkpoint3-web-source-hashes.sha256",
  "disposition": "Integrated into serialized Web remediation; verification pending",
  "findings": [
    {
      "id": "WEB-ROOT-01",
      "severity": "high",
      "classification": "release-blocker",
      "evidence": "src/componentes/CadastroNumero.tsx invalidate(), iniciar(), SDK effect dependencies",
      "problem": "Reservation clears sdkReady after SDK loaded; unchanged effect dependencies leave the Meta authorization button disabled.",
      "required_proof": "Real-backend browser reserves official attempt, then enabled button synchronously invokes provider SDK port from click."
    },
    {
      "id": "WEB-ROOT-02",
      "severity": "high",
      "classification": "release-blocker",
      "evidence": "CadastroNumero confirmar() expects direct TentativaNumero; NumberRegistrationService.confirm() returns {registration: DTO}, controller forwards it",
      "problem": "Successful confirmation replaces attempt with a wrapper lacking id/state, breaking stage rendering and subsequent actions.",
      "required_proof": "Real BFF confirmation renders pending receipt and advances correct persisted attempt."
    },
    {
      "id": "WEB-ROOT-03",
      "severity": "medium",
      "classification": "release-blocker",
      "evidence": "CadastroNumero showWizard()/close; safe channel.currentAttemptId unused",
      "problem": "Close automatically cancels durable partial registration; reload has no resume path.",
      "required_proof": "Close/reload resumes authorized partial attempt with server options; no secret persisted. Pending authorization without nonce exposes deliberate safe restart."
    },
    {
      "id": "WEB-ROOT-04",
      "severity": "medium",
      "classification": "release-blocker",
      "evidence": "Numeros polls only BU list; CadastroNumero only GETs attempt immediately after pair/actions",
      "problem": "Webhook progression updates channel projection while wizard attempt remains stale.",
      "required_proof": "Normal provider webhook advances displayed current attempt; old response cannot update after close/BU switch/unmount."
    },
    {
      "id": "WEB-ROOT-05",
      "severity": "medium",
      "classification": "release-blocker",
      "evidence": "CadastroNumero iniciar() creates crypto.randomUUID() for every submit",
      "problem": "Response-loss retry of same atomic new-BU registration gets a new idempotency key and can duplicate the reservation intent.",
      "required_proof": "Drop first real BFF response after commit; same intent retries same key and returns one BU/channel/attempt. Changed intent gets fresh key."
    },
    {
      "id": "WEB-ROOT-06",
      "severity": "medium",
      "classification": "release-blocker",
      "evidence": "MetaHttpClient.recursos(token,wabaId,after) returns selected WABA only; carregarOpcoes replaces entire options",
      "problem": "Loading numbers removes the other authorized WABA choices.",
      "required_proof": "Multi-WABA browser selection can load and switch WABA without accepting stale numbers/cursor."
    }
  ],
  "additional_probe": "SDK callback must be generation/attempt correlated and duplicate popup blocked; bounded JSON-string/object messages must reject malformed/untrusted origin without logging payload. Meta primary SDK page retrieval returned429; no real-SDK certification claimed.",
  "remaining_gates": "Real-backend Playwright, FRC/BCI, independent delivery/security/adherence/test quality reviews, runtime and external provider evidence."
}
````

## Snapshot: foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/checkpoint4-web-handoff.md

Original SHA256: c46db97317b9a937e1ae93de93d5259ed91b9d0c0a721470e6b2ca4f7cd4b81f

````text
# Checkpoint 4 — Web lifecycle remediation

Status: bounded Web remediation implemented and validated; product writes are stopped for root adjudication. No API, API fixtures, generated output, browser/E2E, package, runtime/config, or shared dependency paths were edited. No commit or push was made.

## Source

- Checkout: `web-app`, branch `feature/number-onboarding`, baseline `4e56f6c1f4515b918d05b8c87e890d42e8542c56`.
- Owned paths: `src/telas/Numeros.tsx`, `src/api.ts`, `src/api.spec.ts`, `src/cadastroNumero.ts`, `src/cadastroNumero.spec.ts`, `src/componentes/CadastroNumero.tsx`.
- SHA-256 manifest: `checkpoint4-web-source-hashes.sha256`.
- Validation log: `checkpoint4-web-validation.log`.

## Remediation

The Meta SDK readiness flag is now independent of attempt invalidation, so reserving an attempt does not strand the authorization control in its loading state. Durable attempts remain active when the panel closes; an authorized administrator can resume from the safe BU projection, which reloads the attempt DTO and current options. The wizard polls the active attempt at five-second intervals, bounded to 60 reads, and rejects stale updates after lifecycle or attempt changes. A nonce is retained only in component memory for the current mounted session; when it cannot be recovered after reload, the UI offers explicit cancellation and a fresh reservation instead of inventing or persisting it. Popup callbacks are correlated to the attempt and lifecycle, and `FB.login` remains synchronous in the click handler.

Same-payload reservation retries reuse the same in-memory Idempotency-Key; changed intent rotates it. Confirmation consumes the API's `{ registration: attempt }` envelope. Meta message parsing accepts a bounded JSON string or object only after exact origin validation, rejects malformed/array/unknown-schema events, and treats IDs as hints. When a selected-WABA page returns one WABA, the previously loaded authorized WABA choices remain available while only number results and cursor are replaced.

## Validation

Ran in `node:22.23.3-slim` with the existing isolated Web dependency volume `leadshug-number-onboarding-web-node-modules`:

```text
npm run build
npm test
```

Production build passed. Vitest passed 4 files and 25 tests. Focused helper coverage includes exact-origin/schema and bounded JSON event parsing, idempotency-key reuse/rotation, confirmation envelope unwrapping, and the request-header boundary. The first validation attempt caught two unmatched parentheses in the new parser tests; those were fixed before the passing run recorded in the final log.

## Remaining gates

- No Playwright/browser or real-backend integration was run. Later browser proof should cover reload/resume with a safe attempt projection, close-without-cancel, current-attempt polling, multi-WABA selection and WABA switching across number pagination, and popup gesture/correlation behavior.
- No real Meta or Evolution provider call, credential, phone-number change, QR capture, or deployment occurred. Meta Embedded Signup event serialization/origin behavior has not been certified against a live configured app; Meta developer documentation was rate limited during source review.
- Independent API review/adjudication, browser integration, PCV, provider proof, and final TODO acceptance remain pending.
````

## Snapshot: foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/checkpoint4-web-source-hashes.sha256

Original SHA256: 1365c2ccbd9196e168215fe2d192e5bf9ecfab107346cbafb4e194d2ab36752d

````text
1ed2b572f1d30f2e9e169111a4254cf9691fd36b89ff5861dbf7c43c66c59bd7  src/telas/Numeros.tsx
99259de1c09b61d5ded00f7bbd8f2254db10ac3e58ff1b693fb4659d60b3a1f8  src/api.ts
578f78142ff110322ddb4b5f0e86a4f7b66c5bbdf70311a28f91f57cb2f41a4a  src/api.spec.ts
cb54451f13ab38b862dfded64d402dedd6dec073b91befc6c1a875c2f82e1c4c  src/cadastroNumero.ts
d1d9a67cfc176861f57c1277fe0e38029f75bde3ec4d7a1190ddd793228de57a  src/cadastroNumero.spec.ts
b10b0c138b3c9e736e6eb191c05428956f4c3c619f2ae4001839c17edba97417  src/componentes/CadastroNumero.tsx
````

## Snapshot: web-app/src/telas/Numeros.tsx

Original SHA256: 1ed2b572f1d30f2e9e169111a4254cf9691fd36b89ff5861dbf7c43c66c59bd7

````text
import { useCallback, useEffect, useRef, useState } from 'react';
import { BusinessUnit, Eu, api, ignorarSessaoMorta } from '../api';
import CadastroNumero from '../componentes/CadastroNumero';

/** A BU é o número (ADR-0008), e o canal é vínculo dela. A tela diz isso. */
export default function Numeros({ eu }: { eu: Eu }) {
  const [bus, setBus] = useState<BusinessUnit[]>([]);
  const [erro, setErro] = useState<string | null>(null);
  const generation = useRef(0);
  const request = useRef<Promise<void> | null>(null);

  const carregar = useCallback((): Promise<void> => {
    if (request.current) return request.current;
    const startedAt = generation.current;
    const pending = api.get<{ businessUnits: BusinessUnit[] }>('/business-units')
      .then((result) => {
        if (generation.current === startedAt) { setBus(result.businessUnits); setErro(null); }
      })
      .catch((error: unknown) => { ignorarSessaoMorta(error); if (generation.current === startedAt) setErro('Não foi possível atualizar a lista de números.'); })
      .finally(() => { request.current = null; });
    request.current = pending;
    return pending;
  }, []);

  useEffect(() => {
    void carregar();
    const timer = window.setInterval(() => { void carregar(); }, 5000);
    return () => { generation.current += 1; window.clearInterval(timer); };
  }, [carregar]);

  return <div className="grade">
    <h2 style={{ margin: 0 }}>Números</h2>
    {erro && <p className="erro" role="status">{erro}</p>}
    <CadastroNumero eu={eu} bus={bus} aoAtualizar={carregar} />
    {bus.map((bu) => (
      <div key={bu.id} className="cartao grade">
        <div className="linha">
          <strong>{bu.name}</strong>
          <span className="suave">{bu.phone ?? 'sem número ainda'}</span>
          <span className="suave">Seu papel nesta BU: {bu.papel ?? 'sem acesso administrativo'}</span>
        </div>
        {bu.channels.length === 0 && <p className="suave">Nenhum canal cadastrado.</p>}
        {bu.channels.map((channel) => (
          <div key={channel.id} className="grade">
            <div className="linha">
              <strong>{channel.type === 'OFICIAL' ? 'Canal oficial' : 'Canal não oficial'}</strong>
              <span>{channel.status}</span>
              <span className="suave">Geração {channel.generation ?? '—'}</span>
            </div>
            <div className="linha suave" role="status">
              Identidade própria: {channel.ownNumberVerified ? 'confirmada' : 'pendente'} ·
              conexão do provedor: {channel.providerConnectionState ?? 'pendente'} ·
              recebimento: {channel.receiptVerifiedAt ? 'confirmado' : 'pendente'}
            </div>
          </div>
        ))}
      </div>
    ))}
    {bus.length === 0 && !erro && <p className="suave">Nenhum número no seu escopo.</p>}
  </div>;
}
````

## Snapshot: web-app/src/componentes/CadastroNumero.tsx

Original SHA256: b10b0c138b3c9e736e6eb191c05428956f4c3c619f2ae4001839c17edba97417

````text
import { FormEvent, useCallback, useEffect, useRef, useState } from 'react';
import { api, BusinessUnit, Eu, ErroDaApi } from '../api';
import { CapacidadesNumero, ChaveIdempotenciaReserva, ConfirmacaoNumeroResponse, chaveIdempotenciaReserva, MensagemMetaSignup, mensagemMetaSignup, motivoCapacidade, nomeEstadoTentativa, OpcoesMeta, TentativaNumero, tentativaConfirmada, TipoNumero } from '../cadastroNumero';

declare global {
  interface Window { FB?: { init(options: { appId: string; version: string; xfbml?: boolean }): void; login(callback: (response: FbLoginResponse) => void, options: Record<string, unknown>): void } }
}
interface FbLoginResponse { authResponse?: { code?: string }; status?: string }

function erroSeguro(error: unknown): string {
  if (error instanceof ErroDaApi) return error.codigo === 'ATTEMPT_STALE'
    ? 'Esta tentativa ficou desatualizada. Atualize a lista e inicie novamente.'
    : error.message;
  return 'Não foi possível concluir esta etapa. Tente novamente.';
}

/** Wizard de cadastro. Segredos vivem somente nas closures e no estado transitório desta tela. */
export default function CadastroNumero({ eu, bus, aoAtualizar }: { eu: Eu; bus: BusinessUnit[]; aoAtualizar: () => Promise<void> }) {
  const [open, setOpen] = useState(false);
  const [capacidades, setCapacidades] = useState<CapacidadesNumero | null>(null);
  const [buId, setBuId] = useState('');
  const [novoBu, setNovoBu] = useState(false);
  const [nomeBu, setNomeBu] = useState('');
  const [tipo, setTipo] = useState<TipoNumero>('OFICIAL');
  const [canal, setCanal] = useState<BusinessUnit['channels'][number] | null>(null);
  const [tentativa, setTentativa] = useState<TentativaNumero | null>(null);
  const [opcoes, setOpcoes] = useState<OpcoesMeta | null>(null);
  const [wabaId, setWabaId] = useState('');
  const [numeroId, setNumeroId] = useState('');
  const [cursorUsado, setCursorUsado] = useState<string | undefined>();
  const [pin, setPin] = useState('');
  const [modo, setModo] = useState<'NOVO' | 'JA_REGISTRADO'>('JA_REGISTRADO');
  const [sdkReady, setSdkReady] = useState(false);
  const [qr, setQr] = useState<string | null>(null);
  const [pending, setPending] = useState(false);
  const [popupOpen, setPopupOpen] = useState(false);
  const [nonceMissing, setNonceMissing] = useState(false);
  const [erro, setErro] = useState<string | null>(null);
  const [mensagem, setMensagem] = useState<string | null>(null);
  const lifecycle = useRef(0);
  const attemptRef = useRef<TentativaNumero | null>(null);
  const nonceByAttemptRef = useRef(new Map<string, string>());
  const popupAttemptRef = useRef<{ attemptId: string; life: number; token: number } | null>(null);
  const popupSequence = useRef(0);
  const optionsAttemptRef = useRef<string | null>(null);
  const reservationKeyRef = useRef<ChaveIdempotenciaReserva | null>(null);
  const busy = useRef(false);
  const fbInit = useRef<string | null>(null);
  const wabaSelectionRef = useRef('');
  const opener = useRef<HTMLButtonElement>(null);
  const heading = useRef<HTMLHeadingElement>(null);
  const wasOpen = useRef(false);

  const invalidate = useCallback(() => {
    lifecycle.current += 1;
    attemptRef.current = null;
    nonceByAttemptRef.current.clear(); popupAttemptRef.current = null;
    optionsAttemptRef.current = null;
    wabaSelectionRef.current = '';
    setPopupOpen(false); setNonceMissing(false);
    setTentativa(null); setOpcoes(null); setWabaId(''); setNumeroId(''); setPin(''); setQr(null);
  }, []);

  useEffect(() => () => { lifecycle.current += 1; attemptRef.current = null; nonceByAttemptRef.current.clear(); popupAttemptRef.current = null; optionsAttemptRef.current = null; }, []);

  useEffect(() => {
    if (open) heading.current?.focus();
    else if (wasOpen.current) opener.current?.focus();
    wasOpen.current = open;
  }, [open]);

  useEffect(() => {
    let active = true;
    api.get<CapacidadesNumero>('/number-registrations/capabilities')
      .then((result) => { if (active) setCapacidades(result); })
      .catch((error: unknown) => { if (active) setErro(erroSeguro(error)); });
    return () => { active = false; };
  }, []);

  useEffect(() => {
    if (!open || tipo !== 'OFICIAL' || !capacidades?.oficial.available || !capacidades.oficial.appId) return;
    let active = true;
    const scriptId = 'facebook-jssdk';
    const existing = document.getElementById(scriptId) as HTMLScriptElement | null;
    const init = () => {
      if (!active || !window.FB) return;
      const key = `${capacidades.oficial.appId}:${capacidades.oficial.graphVersion}`;
      if (fbInit.current !== key) {
        window.FB.init({ appId: capacidades.oficial.appId!, version: capacidades.oficial.graphVersion, xfbml: false });
        fbInit.current = key;
      }
      setSdkReady(true);
    };
    if (window.FB) init();
    else if (existing) existing.addEventListener('load', init, { once: true });
    else {
      const script = document.createElement('script');
      script.id = scriptId; script.async = true; script.defer = true;
      script.src = 'https://connect.facebook.net/en_US/sdk.js';
      script.addEventListener('load', init, { once: true });
      script.addEventListener('error', () => { if (active) setErro('Não foi possível carregar a autorização da Meta. Verifique a conexão e tente novamente.'); }, { once: true });
      document.head.appendChild(script);
    }
    return () => { active = false; };
  }, [open, tipo, capacidades]);

  const carregarCapacidades = async () => {
    try { setCapacidades(await api.get<CapacidadesNumero>('/number-registrations/capabilities')); }
    catch (error) { setErro(erroSeguro(error)); }
  };

  const atualizarTentativa = useCallback(async (id: string, life: number) => {
    const atual = await api.get<TentativaNumero>(`/number-registrations/${id}`);
    if (life !== lifecycle.current || attemptRef.current?.id !== id) return null;
    attemptRef.current = atual; setTentativa(atual); return atual;
  }, []);

  useEffect(() => {
    const id = tentativa?.id;
    if (!open || !id || ['CONNECTED', 'ERROR', 'CANCELLED'].includes(tentativa.state)) return;
    const life = lifecycle.current;
    let active = true;
    let reads = 0;
    let timer = 0;
    const poll = async () => {
      if (!active || reads >= 60 || life !== lifecycle.current || attemptRef.current?.id !== id) return;
      reads += 1;
      try {
        const current = await api.get<TentativaNumero>(`/number-registrations/${id}`);
        if (!active || life !== lifecycle.current || attemptRef.current?.id !== id) return;
        attemptRef.current = current; setTentativa(current);
        if (current.tipo === 'OFICIAL' && current.state === 'PENDING_NUMBER' && optionsAttemptRef.current !== id) {
          const options = await api.get<OpcoesMeta>(`/number-registrations/${id}/options`);
          if (!active || life !== lifecycle.current || attemptRef.current?.id !== id) return;
          setOpcoes(options); optionsAttemptRef.current = id;
        }
        if (['CONNECTED', 'ERROR', 'CANCELLED'].includes(current.state)) {
          nonceByAttemptRef.current.delete(id);
          reservationKeyRef.current = null;
          return;
        }
      } catch (error) {
        if (!active || life !== lifecycle.current || attemptRef.current?.id !== id) return;
        setErro(erroSeguro(error));
      }
      if (active && reads < 60) timer = window.setTimeout(() => void poll(), 5000);
    };
    timer = window.setTimeout(() => void poll(), 5000);
    return () => { active = false; window.clearTimeout(timer); };
  }, [open, tentativa?.id]);

  const retomar = async (bu: BusinessUnit, channel: BusinessUnit['channels'][number]) => {
    if (busy.current) return;
    const id = channel.currentAttemptId;
    if (!id) return;
    const cachedNonce = nonceByAttemptRef.current.get(id);
    invalidate();
    const life = lifecycle.current;
    if (cachedNonce) nonceByAttemptRef.current.set(id, cachedNonce);
    setOpen(true); setBuId(bu.id); setNovoBu(false); setNomeBu(''); setTipo(channel.type as TipoNumero); setCanal(channel);
    await executar(async () => {
      const current = await api.get<TentativaNumero>(`/number-registrations/${id}`);
      if (life !== lifecycle.current) return;
      attemptRef.current = current; setTentativa(current);
      const hasNonce = current.state === 'PENDING_AUTH' && nonceByAttemptRef.current.has(id);
      setNonceMissing(current.state === 'PENDING_AUTH' && !hasNonce);
      if (current.state === 'PENDING_AUTH' && !hasNonce) {
        setMensagem('A Meta não devolve o nonce de uso único. Para continuar após recarregar a tela, cancele esta tentativa e reserve uma nova autorização.');
      }
      if (current.tipo === 'OFICIAL' && current.state === 'PENDING_NUMBER') {
        const options = await api.get<OpcoesMeta>(`/number-registrations/${id}/options`);
        if (life === lifecycle.current && attemptRef.current?.id === id) { setOpcoes(options); optionsAttemptRef.current = id; }
      }
    });
  };

  const executar = async (job: () => Promise<void>) => {
    if (busy.current) return;
    busy.current = true; setPending(true); setErro(null); setMensagem(null);
    try { await job(); }
    catch (error) { setErro(erroSeguro(error)); }
    finally { busy.current = false; setPending(false); }
  };

  const iniciar = async (event: FormEvent) => {
    event.preventDefault();
    await executar(async () => {
      invalidate();
      const life = lifecycle.current;
      const corpo = { tipo, operation: canal ? 'REAUTORIZAR' as const : 'NOVO' as const,
        ...(canal ? { buId, channelId: canal.id, expectedGeneration: canal.generation }
          : novoBu ? { novaBu: { nome: nomeBu.trim() } } : { buId }) };
      const fingerprint = JSON.stringify(corpo);
      const reservationKey = chaveIdempotenciaReserva(reservationKeyRef.current, fingerprint, () => crypto.randomUUID());
      reservationKeyRef.current = reservationKey;
      const result = await api.postWithHeaders<{ attempt: TentativaNumero; nonce: string | null; replay: boolean }>(
        '/number-registrations', corpo, { 'idempotency-key': reservationKey.key },
      );
      if (lifecycle.current !== life || (buId && !novoBu && buId !== result.attempt.buId)) return;
      attemptRef.current = result.attempt; setTentativa(result.attempt);
      if (result.nonce) nonceByAttemptRef.current.set(result.attempt.id, result.nonce);
      setNonceMissing(result.attempt.state === 'PENDING_AUTH' && !result.nonce);
      await aoAtualizar();
      if (life !== lifecycle.current || attemptRef.current?.id !== result.attempt.id) return;
      if (result.attempt.tipo === 'OFICIAL' && result.attempt.state === 'PENDING_NUMBER') {
        const options = await api.get<OpcoesMeta>(`/number-registrations/${result.attempt.id}/options`);
        if (lifecycle.current === life && attemptRef.current?.id === result.attempt.id) { setOpcoes(options); optionsAttemptRef.current = result.attempt.id; }
      }
      if (result.attempt.tipo === 'NAO_OFICIAL') setMensagem('O cadastro foi reservado. Agora inicie o pareamento do provedor.');
    });
  };

  const autorizar = () => {
    const current = attemptRef.current;
    const currentNonce = current ? nonceByAttemptRef.current.get(current.id) : undefined;
    if (!current || !currentNonce || !window.FB || !capacidades?.oficial.configId || busy.current || popupAttemptRef.current) return;
    const life = lifecycle.current;
    const popupToken = ++popupSequence.current;
    popupAttemptRef.current = { attemptId: current.id, life, token: popupToken }; setPopupOpen(true);
    try {
      // FB.login must run synchronously from this click to preserve browser popup permission.
      window.FB.login((response) => {
        const popup = popupAttemptRef.current;
        if (!popup || popup.token !== popupToken || popup.attemptId !== current.id || popup.life !== life) return;
        popupAttemptRef.current = null; setPopupOpen(false);
        if (life !== lifecycle.current || attemptRef.current?.id !== current.id) return;
        const code = response.authResponse?.code;
        if (!code) {
          setMensagem('A autorização foi cancelada ou não concluiu. A tentativa continua disponível; você pode tentar novamente ou cancelá-la.');
          return;
        }
        nonceByAttemptRef.current.delete(current.id);
        void executar(async () => {
          const result = await api.post<TentativaNumero>(`/number-registrations/${current.id}/authorize`, { nonce: currentNonce, code });
          if (life !== lifecycle.current || attemptRef.current?.id !== current.id) return;
          setNonceMissing(false); setTentativa(result); attemptRef.current = result;
          const options = await api.get<OpcoesMeta>(`/number-registrations/${current.id}/options`);
          if (life === lifecycle.current && attemptRef.current?.id === current.id) { setOpcoes(options); optionsAttemptRef.current = current.id; }
        });
      }, { config_id: capacidades.oficial.configId, response_type: 'code', override_default_response_type: true, extras: { setup: {} } });
    } catch {
      if (popupAttemptRef.current?.token === popupToken) {
        popupAttemptRef.current = null; setPopupOpen(false);
        setErro('Não foi possível abrir a janela de autorização da Meta. Tente novamente.');
      }
    }
  };

  const carregarOpcoes = async (after?: string) => {
    const current = attemptRef.current; if (!current || !wabaId) return;
    await executar(async () => {
      const life = lifecycle.current; const id = current.id; const selectedWaba = wabaId;
      const q = new URLSearchParams({ wabaId: selectedWaba, ...(after ? { after } : {}) });
      const page = await api.get<OpcoesMeta>(`/number-registrations/${id}/options?${q}`);
      if (life === lifecycle.current && attemptRef.current?.id === id && wabaSelectionRef.current === selectedWaba) {
        setOpcoes((existing) => ({ wabas: existing?.wabas ?? page.wabas, numbers: page.numbers, next: page.next }));
        optionsAttemptRef.current = id;
        setCursorUsado(after); setNumeroId('');
      }
    });
  };

  const confirmar = async (event: FormEvent) => {
    event.preventDefault();
    const current = attemptRef.current; if (!current || !numeroId) return;
    const life = lifecycle.current;
    await executar(async () => {
      const response = await api.post<ConfirmacaoNumeroResponse>(`/number-registrations/${current.id}/confirm`, {
        wabaId, phoneNumberId: numeroId, modoRegistro: modo,
        ...(modo === 'NOVO' ? { pin } : {}), ...(cursorUsado ? { after: cursorUsado } : {}),
      });
      if (life !== lifecycle.current || attemptRef.current?.id !== current.id) return;
      const updated = tentativaConfirmada(response);
      setPin(''); attemptRef.current = updated; setTentativa(updated);
      setMensagem('Seleção confirmada. A conexão e o recebimento serão verificados em etapas separadas.');
      if (updated.state === 'PENDING_RECEIPT') {
        try { await api.post(`/number-registrations/${current.id}/advance`, {}); }
        catch (error) { if (life === lifecycle.current) await atualizarTentativa(current.id, life); throw error; }
      }
      if (life !== lifecycle.current) return;
      await atualizarTentativa(current.id, life); await aoAtualizar();
    });
  };

  const acaoTentativa = async (acao: 'advance' | 'retry' | 'cancel') => {
    const current = attemptRef.current; if (!current) return;
    const life = lifecycle.current;
    await executar(async () => {
      let updated: TentativaNumero;
      try { updated = await api.post<TentativaNumero>(`/number-registrations/${current.id}/${acao}`, {}); }
      catch (error) { if (life === lifecycle.current) await atualizarTentativa(current.id, life).catch(() => null); throw error; }
      if (life !== lifecycle.current || attemptRef.current?.id !== current.id) return;
      attemptRef.current = updated; setTentativa(updated);
      if (updated.state === 'PENDING_NUMBER' && updated.tipo === 'OFICIAL') {
        const options = await api.get<OpcoesMeta>(`/number-registrations/${current.id}/options`);
        if (life === lifecycle.current && attemptRef.current?.id === current.id) { setOpcoes(options); optionsAttemptRef.current = current.id; }
      }
      if (acao === 'cancel') {
        if (current.operation === 'NOVO') setCanal(null);
        reservationKeyRef.current = null;
        invalidate(); setMensagem('Cadastro cancelado. Você pode reservar uma nova tentativa com um nonce novo.');
        await aoAtualizar();
        return;
      }
      if (life !== lifecycle.current) return;
      await aoAtualizar();
    });
  };

  const pair = async (bu: BusinessUnit, intent: 'INITIAL' | 'RENEW') => {
    await executar(async () => {
      const life = lifecycle.current;
      const priorAttempt = attemptRef.current;
      setQr(null); const generation = bu.channels.find((c) => c.type === 'NAO_OFICIAL')?.generation;
      const result = await api.post<{ qrcode: string | null; state: string; attemptId?: string | null }>(
        `/business-units/${bu.id}/channels/nao-oficial/pair`,
        { intent, ...(intent === 'RENEW' && generation ? { expectedGeneration: generation } : {}) },
      );
      if (life !== lifecycle.current) return;
      setQr(result.qrcode);
      if (result.attemptId && priorAttempt?.buId === bu.id && attemptRef.current?.id === priorAttempt.id) {
        const latest = await api.get<TentativaNumero>(`/number-registrations/${result.attemptId}`);
        if (life === lifecycle.current && attemptRef.current?.id === priorAttempt.id) {
          attemptRef.current = latest; setTentativa(latest);
        }
      }
      const estadoPair = result.state.toUpperCase();
      const etapa = estadoPair === 'CLEANUP_AMBIGUOUS' || estadoPair === 'CREATE_AMBIGUOUS'
        ? 'A operação externa ficou ambígua e exige reconciliação administrativa antes de qualquer nova tentativa.'
        : estadoPair === 'PENDING_IDENTITY'
          ? 'O pareamento está pendente de confirmação da identidade própria deste número.'
          : estadoPair === 'PENDING_RECEIPT'
            ? 'A identidade foi confirmada; o recebimento ainda precisa ser observado.'
            : result.qrcode
              ? 'Leia o QR no WhatsApp. O QR não confirma identidade nem recebimento.'
              : `Estado atual: ${estadoPair}. A lista será atualizada para mostrar as etapas confirmadas.`;
      setMensagem(`${intent === 'RENEW' ? 'O pareamento foi renovado. O recebimento fica interrompido até a confirmação da identidade deste número. ' : ''}${etapa}`);
      await aoAtualizar();
    });
  };

  const verificarCanal = async (bu: BusinessUnit, tipoCanal: TipoNumero) => {
    await executar(async () => {
      const life = lifecycle.current;
      const result = await api.post<{ status?: string; providerConnectionState?: string; receiptVerifiedAt?: string | null }>(
        `/business-units/${bu.id}/channels/${tipoCanal.toLowerCase().replace('_', '-')}/verify`, {},
      );
      if (life !== lifecycle.current) return;
      await aoAtualizar();
      setMensagem(result.receiptVerifiedAt ? 'Recebimento confirmado pelo canal.' : 'Verificação solicitada. O estado permanece pendente até haver confirmação de recebimento.');
    });
  };

  useEffect(() => {
    if (!open) return;
    const current = attemptRef.current;
    const life = lifecycle.current;
    const onMessage = (event: MessageEvent) => {
      if (!current || current.state !== 'PENDING_AUTH' || life !== lifecycle.current || attemptRef.current?.id !== current.id) return;
      const message: MensagemMetaSignup | null = mensagemMetaSignup(event);
      if (!message) return;
      if (message.event === 'CANCEL' || message.event === 'ERROR') setMensagem(message.event === 'CANCEL' ? 'Autorização Meta cancelada.' : 'A Meta informou uma falha na autorização.');
    };
    window.addEventListener('message', onMessage);
    return () => window.removeEventListener('message', onMessage);
  }, [open, tentativa?.id, tentativa?.state]);

  const showWizard = async () => {
    const active = bus.flatMap((unit) => unit.channels.filter((channel) => channel.currentAttemptId).map((channel) => ({ unit, channel })));
    if (active.length === 1) { await retomar(active[0].unit, active[0].channel); return; }
    setOpen(true); setErro(null); setMensagem(null);
    await carregarCapacidades();
  };

  const fecharWizard = () => {
    lifecycle.current += 1;
    attemptRef.current = null;
    popupAttemptRef.current = null;
    setPopupOpen(false); setOpen(false); setTentativa(null); setOpcoes(null);
    setWabaId(''); wabaSelectionRef.current = ''; setNumeroId(''); setPin(''); setQr(null);
    setErro(null); setMensagem(null);
  };

  const selectedBu = bus.find((bu) => bu.id === buId);
  const canManageSelected = selectedBu?.papel === 'ADMIN' || selectedBu?.papel === 'OWNER';
  const canCreateBu = eu.papel === 'ADMIN' || eu.papel === 'OWNER';
  const capability = tipo === 'OFICIAL' ? capacidades?.oficial : capacidades?.naoOficial;
  const activeAttemptChannel = selectedBu?.channels.find((item) => item.type === tipo && item.currentAttemptId);

  return <section className="grade" aria-labelledby="cadastro-numero-title">
    <div className="linha"><h3 id="cadastro-numero-title" style={{ margin: 0 }}>Adicionar ou reautorizar número</h3>
      <button ref={opener} type="button" onClick={() => void showWizard()}>Iniciar cadastro</button></div>
    {open && <div className="cartao grade" role="region" aria-label="Cadastro guiado de número">
      <div className="linha"><h4 ref={heading} tabIndex={-1} style={{ margin: 0 }}>Cadastro guiado</h4><button type="button" onClick={fecharWizard}>Fechar</button></div>
      {erro && <p className="erro" role="alert">{erro}</p>}{mensagem && <p role="status" aria-live="polite">{mensagem}</p>}
      {!tentativa && <form className="grade" onSubmit={iniciar}>
        <label>Business Unit
          <select value={novoBu ? '__nova__' : buId} onChange={(e) => {
            reservationKeyRef.current = null; invalidate(); setCanal(null); setBuId(e.target.value === '__nova__' ? '' : e.target.value); setNovoBu(e.target.value === '__nova__'); setNomeBu(''); setQr(null);
          }} required>
            <option value="" disabled>Escolha uma Business Unit</option>
            {bus.filter((bu) => bu.papel === 'ADMIN' || bu.papel === 'OWNER').map((bu) => <option key={bu.id} value={bu.id}>{bu.name}</option>)}
            {canCreateBu && <option value="__nova__">Criar nova Business Unit</option>}
          </select>
        </label>
        {novoBu && <label>Nome da nova Business Unit<input value={nomeBu} onChange={(e) => { reservationKeyRef.current = null; setNomeBu(e.target.value); }} maxLength={120} required /></label>}
        {selectedBu && <label>Canal existente (opcional)
          <select value={canal?.type ?? ''} onChange={(e) => {
            const chosen = selectedBu.channels.find((c) => c.type === e.target.value) ?? null;
            reservationKeyRef.current = null;
            setCanal(chosen); if (chosen) setTipo(chosen.type as TipoNumero);
          }}><option value="">Novo número para esta BU</option>{selectedBu.channels.map((c) => <option key={c.id} value={c.type}>{c.type === 'OFICIAL' ? 'Oficial' : 'Não oficial'} — {c.status}</option>)}</select>
        </label>}
        {activeAttemptChannel && <p className="suave" role="status">Já existe uma tentativa atual para esta modalidade nesta Business Unit. <button type="button" disabled={pending} onClick={() => { if (selectedBu) void retomar(selectedBu, activeAttemptChannel); }}>Ver ou retomar etapa</button></p>}
        {!canal && <fieldset><legend>Modalidade</legend>
          <label><input type="radio" name="modalidade" value="OFICIAL" checked={tipo === 'OFICIAL'} onChange={() => { reservationKeyRef.current = null; setTipo('OFICIAL'); }} /> Oficial</label>
          <label><input type="radio" name="modalidade" value="NAO_OFICIAL" checked={tipo === 'NAO_OFICIAL'} onChange={() => { reservationKeyRef.current = null; setTipo('NAO_OFICIAL'); }} /> Não oficial</label>
        </fieldset>}
        {capacidades && capability && !capability.available && <p className="suave" role="status">{motivoCapacidade(capability.reason)}</p>}
        <button className="primario" disabled={pending || !capacidades || !capability?.available || (!novoBu && !buId) || (novoBu && !nomeBu.trim()) || (novoBu && !canCreateBu) || (!novoBu && !canManageSelected)}>
          {pending ? 'Preparando…' : canal ? 'Reservar reautorização' : 'Reservar tentativa'}
        </button>
      </form>}
      {tentativa && <div className="grade">
        <p role="status" aria-live="polite"><strong>{nomeEstadoTentativa[tentativa.state]}</strong> · Etapa: {tentativa.stage}</p>
        {tentativa.errorCode && <p className="erro">A etapa retornou o código seguro: {tentativa.errorCode}.</p>}
        {!['CONNECTED', 'ERROR', 'CANCELLED'].includes(tentativa.state) && <button type="button" disabled={pending} onClick={() => void acaoTentativa('cancel')}>{nonceMissing ? 'Cancelar e preparar nova autorização' : 'Cancelar tentativa'}</button>}
        {tentativa.tipo === 'OFICIAL' && tentativa.state === 'PENDING_AUTH' && <div className="grade">
          <p>A autorização abre a janela oficial da Meta. O app e a configuração são definidos pela instalação.</p>
          {!nonceMissing && <button type="button" className="primario" disabled={!sdkReady || pending || popupOpen || !nonceByAttemptRef.current.has(tentativa.id)} onClick={autorizar}>{popupOpen ? 'Autorização aberta…' : sdkReady ? 'Continuar com a Meta' : 'Carregando autorização…'}</button>}
          {nonceMissing && <p className="suave">O nonce de uso único não pode ser recuperado após recarregar a página. Cancele a tentativa e reserve outra para receber um nonce novo.</p>}
        </div>}
        {tentativa.tipo === 'OFICIAL' && opcoes && tentativa.state === 'PENDING_NUMBER' && <form className="grade" onSubmit={confirmar}>
          <label>Conta do WhatsApp Business
            <select value={wabaId} onChange={(e) => { wabaSelectionRef.current = e.target.value; setWabaId(e.target.value); setNumeroId(''); setCursorUsado(undefined); setOpcoes({ wabas: opcoes.wabas, numbers: [], next: null }); }} required>
              <option value="" disabled>Escolha a conta</option>{opcoes.wabas.map((w) => <option value={w.id} key={w.id}>{w.name || `Conta ${w.id}`}</option>)}
            </select>
          </label>
          {wabaId && <><button type="button" disabled={pending} onClick={() => void carregarOpcoes()}>Carregar números desta conta</button>
            {opcoes.numbers.length > 0 && <label>Número
              <select value={numeroId} onChange={(e) => setNumeroId(e.target.value)} required><option value="" disabled>Escolha o número</option>
                {opcoes.numbers.map((n) => <option value={n.id} key={n.id}>{n.telefone || n.id}{n.nomeVerificado ? ` — ${n.nomeVerificado}` : ''}</option>)}
              </select>
            </label>}
            {opcoes.next && <button type="button" disabled={pending} onClick={() => void carregarOpcoes(opcoes.next!)}>Carregar próxima página</button>}
          </>}
          {numeroId && <><fieldset><legend>Estado de registro na Meta</legend>
            <label><input type="radio" name="modo-registro" checked={modo === 'JA_REGISTRADO'} onChange={() => { setModo('JA_REGISTRADO'); setPin(''); }} /> Já registrado</label>
            <label><input type="radio" name="modo-registro" checked={modo === 'NOVO'} onChange={() => setModo('NOVO')} /> Registrar número novo</label>
          </fieldset>
            {modo === 'NOVO' && <label>PIN de 6 dígitos<input type="password" inputMode="numeric" autoComplete="off" value={pin} onChange={(e) => setPin(e.target.value.replace(/\D/g, '').slice(0, 6))} minLength={6} maxLength={6} required /></label>}
            <button className="primario" disabled={pending || (modo === 'NOVO' && pin.length !== 6)}>Confirmar número</button>
          </>}
        </form>}
        {tentativa.tipo === 'OFICIAL' && tentativa.state === 'PENDING_RECEIPT' && <div className="linha">
          {!tentativa.stage.endsWith('_AMBIGUOUS') && tentativa.stage !== 'SUBSCRIBING'
            ? <><button type="button" disabled={pending} onClick={() => void acaoTentativa(tentativa.stage === 'SUBSCRIBED' ? 'advance' : 'retry')}>{tentativa.stage === 'SUBSCRIBED' ? 'Confirmar recebimento' : 'Tentar etapa novamente'}</button>
              {tentativa.stage !== 'SUBSCRIBED' && <button type="button" disabled={pending} onClick={() => void acaoTentativa('advance')}>Verificar conexão e recebimento</button>}</>
            : <span className="suave">A etapa exige reconciliação antes de uma nova chamada ao provedor.</span>}
        </div>}
        {tentativa.tipo === 'NAO_OFICIAL' && tentativa.state === 'PENDING_NUMBER' && <div className="grade">
          <p>A reserva está pronta. Inicie o pareamento administrativo desta Business Unit para continuar.</p>
          <button type="button" className="primario" disabled={pending || !capacidades?.naoOficial.available} onClick={() => {
            const bu = bus.find((item) => item.id === tentativa.buId);
            if (bu) void pair(bu, 'INITIAL');
          }}>Iniciar pareamento</button>
        </div>}
        {['ERROR', 'CANCELLED'].includes(tentativa.state) && <div className="linha">
          {tentativa.state === 'ERROR' && <button type="button" disabled={pending} onClick={() => void acaoTentativa('cancel')}>Encerrar tentativa</button>}
          <button type="button" onClick={() => { reservationKeyRef.current = null; invalidate(); }}>Limpar tentativa</button>
        </div>}
        {tentativa.state === 'CONNECTED' && <p role="status">A conexão do provedor e o recebimento estão confirmados para a tentativa atual.</p>}
      </div>}
    </div>}
    {qr && <div className="cartao grade" role="status"><p>Leia este QR com o WhatsApp. Parear sozinho não confirma identidade nem recebimento.</p><img src={qr} alt="QR transitório de pareamento" style={{ width: 240 }} /></div>}
    {bus.map((bu) => {
      const noOficial = bu.channels.find((channel) => channel.type === 'NAO_OFICIAL');
      return (noOficial && (bu.papel === 'ADMIN' || bu.papel === 'OWNER')) || bu.channels.some((channel) => channel.currentAttemptId && (bu.papel === 'ADMIN' || bu.papel === 'OWNER')) ? <div key={bu.id} className="linha">
        {bu.channels.filter((channel) => channel.currentAttemptId && (bu.papel === 'ADMIN' || bu.papel === 'OWNER')).map((channel) => <button key={channel.id} type="button" disabled={pending} onClick={() => void retomar(bu, channel)}>Retomar {channel.type === 'OFICIAL' ? 'canal oficial' : 'canal não oficial'} · {bu.name}</button>)}
        {noOficial && (bu.papel === 'ADMIN' || bu.papel === 'OWNER') && <>
        <span className="suave">{bu.name}: pareamento não oficial · {noOficial.status}; identidade {noOficial.ownNumberVerified ? 'confirmada' : 'pendente'}; provedor {noOficial.providerConnectionState ?? 'pendente'}; recebimento {noOficial.receiptVerifiedAt ? 'confirmado' : 'pendente'}.</span>
        <button type="button" disabled={pending || !capacidades?.naoOficial.available} onClick={() => void pair(bu, 'RENEW')}>Renovar QR</button>
        <button type="button" disabled={pending} onClick={() => void verificarCanal(bu, 'NAO_OFICIAL')}>Verificar canal</button>
        </>}
      </div> : null;
    })}
  </section>;
}
````

## Snapshot: web-app/src/cadastroNumero.ts

Original SHA256: cb54451f13ab38b862dfded64d402dedd6dec073b91befc6c1a875c2f82e1c4c

````text
export type TipoNumero = 'OFICIAL' | 'NAO_OFICIAL';
export type EstadoTentativa = 'PENDING_AUTH' | 'PENDING_NUMBER' | 'REGISTERING' | 'PENDING_RECEIPT' | 'CONNECTED' | 'ERROR' | 'CANCELLED';

export interface TentativaNumero {
  id: string;
  buId: string;
  channelId: string | null;
  tipo: TipoNumero;
  operation: 'NOVO' | 'REAUTORIZAR';
  state: EstadoTentativa;
  stage: string;
  errorCode: string | null;
  expiresAt: string;
  version: number;
  generation: number;
}

export interface CapacidadesNumero {
  oficial: { appId: string | null; configId: string | null; graphVersion: string; available: boolean; reason: string };
  naoOficial: { available: boolean; reason: string };
}

export interface OpcoesMeta {
  wabas: Array<{ id: string; name: string | null }>;
  numbers: Array<{ id: string; telefone: string | null; nomeVerificado: string | null }>;
  next: string | null;
}

export interface ConfirmacaoNumeroResponse {
  registration: TentativaNumero;
}

export interface ChaveIdempotenciaReserva {
  fingerprint: string;
  key: string;
}

/** Keep a request key across same-payload retries after an ambiguous response. */
export function chaveIdempotenciaReserva(
  anterior: ChaveIdempotenciaReserva | null,
  fingerprint: string,
  criar: () => string,
): ChaveIdempotenciaReserva {
  if (anterior?.fingerprint === fingerprint) return anterior;
  return { fingerprint, key: criar() };
}

/** The BFF confirmation DTO wraps the attempt under `registration`. */
export function tentativaConfirmada(response: ConfirmacaoNumeroResponse): TentativaNumero {
  return response.registration;
}

export interface MensagemMetaSignup {
  event: 'FINISH' | 'CANCEL' | 'ERROR';
  data?: { waba_id?: string; phone_number_id?: string; business_id?: string };
}

/** SDK messages are hints only. Identity and options are revalidated by the API. */
export function mensagemMetaSignup(event: MessageEvent): MensagemMetaSignup | null {
  if (event.origin !== 'https://www.facebook.com') return null;
  let value: unknown = event.data;
  if (typeof value === 'string') {
    if (value.length > 8192) return null;
    try { value = JSON.parse(value) as unknown; } catch { return null; }
  }
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const message = value as Record<string, unknown>;
  if (message.type !== 'WA_EMBEDDED_SIGNUP' || !['FINISH', 'CANCEL', 'ERROR'].includes(String(message.event))) return null;
  const raw = message.data;
  if (raw !== undefined && (!raw || typeof raw !== 'object' || Array.isArray(raw))) return null;
  const data = raw as Record<string, unknown> | undefined;
  return {
    event: message.event as MensagemMetaSignup['event'],
    ...(data ? { data: {
      ...(typeof data.waba_id === 'string' ? { waba_id: data.waba_id } : {}),
      ...(typeof data.phone_number_id === 'string' ? { phone_number_id: data.phone_number_id } : {}),
      ...(typeof data.business_id === 'string' ? { business_id: data.business_id } : {}),
    } } : {}),
  };
}

export const nomeEstadoTentativa: Record<EstadoTentativa, string> = {
  PENDING_AUTH: 'Aguardando autorização da Meta',
  PENDING_NUMBER: 'Autorização recebida; escolha a conta e o número',
  REGISTERING: 'Registro do número em andamento',
  PENDING_RECEIPT: 'Aguardando confirmação de recebimento',
  CONNECTED: 'Conectado e com recebimento confirmado',
  ERROR: 'Cadastro com falha',
  CANCELLED: 'Cadastro cancelado',
};

export function motivoCapacidade(reason: string): string {
  const motivos: Record<string, string> = {
    NOT_CONFIGURED: 'Esta modalidade ainda não está configurada nesta instalação.',
    PARTIAL_CONFIGURATION: 'A configuração Meta está incompleta. Peça ao administrador da instalação para concluí-la.',
    CREDENTIAL_ENCRYPTION_UNAVAILABLE: 'O armazenamento seguro de credenciais não está configurado. Peça ao administrador da instalação para habilitá-lo.',
    MODULE_NOT_CONTRACTED: 'O módulo não oficial não está contratado para esta Mantenedora.',
    AVAILABLE: 'Disponível',
  };
  return motivos[reason] ?? 'Esta modalidade está indisponível. Peça ao administrador da instalação para verificar a configuração.';
}
````

## Snapshot: web-app/src/cadastroNumero.spec.ts

Original SHA256: d1d9a67cfc176861f57c1277fe0e38029f75bde3ec4d7a1190ddd793228de57a

````text
import { describe, expect, it } from 'vitest';
import { chaveIdempotenciaReserva, mensagemMetaSignup, motivoCapacidade, nomeEstadoTentativa, tentativaConfirmada, TentativaNumero } from './cadastroNumero';

function metaMessage(origin: string, data: unknown): MessageEvent {
  return { origin, data } as MessageEvent;
}

describe('contrato efêmero do cadastro de número', () => {
  it('aceita somente o evento Embedded Signup na origem Meta aprovada e no schema esperado', () => {
    expect(mensagemMetaSignup(metaMessage('https://www.facebook.com', {
      type: 'WA_EMBEDDED_SIGNUP', event: 'FINISH', data: { waba_id: '12345', phone_number_id: '67890' },
    }))).toEqual({ event: 'FINISH', data: { waba_id: '12345', phone_number_id: '67890' } });
    expect(mensagemMetaSignup(metaMessage('https://www.facebook.com', JSON.stringify({
      type: 'WA_EMBEDDED_SIGNUP', event: 'CANCEL', data: {},
    })))).toEqual({ event: 'CANCEL', data: {} });
    expect(mensagemMetaSignup(metaMessage('https://evil.example', {
      type: 'WA_EMBEDDED_SIGNUP', event: 'FINISH', data: { waba_id: '12345' },
    }))).toBeNull();
    expect(mensagemMetaSignup(metaMessage('https://www.facebook.com', { type: 'OTHER', event: 'FINISH' }))).toBeNull();
    expect(mensagemMetaSignup(metaMessage('https://www.facebook.com', '{malformed'))).toBeNull();
    expect(mensagemMetaSignup(metaMessage('https://www.facebook.com', 'x'.repeat(8193)))).toBeNull();
    expect(mensagemMetaSignup(metaMessage('https://www.facebook.com', '[]'))).toBeNull();
  });

  it('não trata IDs da mensagem como prova e mantém status e causa de indisponibilidade claros', () => {
    expect(mensagemMetaSignup(metaMessage('https://www.facebook.com', { type: 'WA_EMBEDDED_SIGNUP', event: 'FINISH', data: { waba_id: 123 } })))
      .toEqual({ event: 'FINISH', data: {} });
    expect(nomeEstadoTentativa.PENDING_RECEIPT).toMatch(/Aguardando confirmação/);
    expect(motivoCapacidade('CREDENTIAL_ENCRYPTION_UNAVAILABLE')).toMatch(/administrador da instalação/);
  });
});

describe('contrato de reserva e confirmação do BFF', () => {
  it('reuses the same idempotency key after a same-payload retry and rotates it when intent changes', () => {
    const first = chaveIdempotenciaReserva(null, '{"tipo":"OFICIAL"}', () => 'key-1');
    expect(chaveIdempotenciaReserva(first, '{"tipo":"OFICIAL"}', () => 'unexpected')).toBe(first);
    expect(chaveIdempotenciaReserva(first, '{"tipo":"NAO_OFICIAL"}', () => 'key-2')).toEqual({
      fingerprint: '{"tipo":"NAO_OFICIAL"}', key: 'key-2',
    });
  });

  it('reads the registration attempt from the API confirmation envelope', () => {
    const attempt: TentativaNumero = {
      id: 'attempt-1', buId: 'bu-1', channelId: 'channel-1', tipo: 'OFICIAL', operation: 'NOVO',
      state: 'PENDING_RECEIPT', stage: 'REGISTERED_PENDING_RECEIPT', errorCode: null,
      expiresAt: '2026-10-15T00:00:00.000Z', version: 4, generation: 1,
    };
    expect(tentativaConfirmada({ registration: attempt })).toBe(attempt);
  });
});
````

## Snapshot: web-app/src/api.ts

Original SHA256: 99259de1c09b61d5ded00f7bbd8f2254db10ac3e58ff1b693fb4659d60b3a1f8

````text
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
  let corpo: Record<string, string | undefined>;
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
      corpo.code,
      dito ? `${dito} (HTTP ${res.status})` : `A API respondeu ${res.status} sem explicar o motivo.`,
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
  janela: { exigida: boolean; aberta: boolean; expiraEm: string | null; canal: string | null };
  messages: Mensagem[];
  paginacao: { limite: number; temAnteriores: boolean; cursorAnterior: string | null };
}
````

## Snapshot: web-app/src/api.spec.ts

Original SHA256: 578f78142ff110322ddb4b5f0e86a4f7b66c5bbdf70311a28f91f57cb2f41a4a

````text
import { afterEach, describe, expect, it, vi } from 'vitest';
import { ErroDaApi, api } from './api';

function responde(corpo: string, init: { status?: number; ok?: boolean } = {}) {
  const status = init.status ?? 200;
  vi.stubGlobal(
    'fetch',
    vi.fn(async () => ({
      status,
      ok: init.ok ?? status < 400,
      text: async () => corpo,
    })),
  );
}

afterEach(() => vi.unstubAllGlobals());

describe('resposta que não é JSON (api.ts)', () => {
  it('falha DIZENDO a causa provável, em vez de devolver objeto vazio', async () => {
    // O que o nginx do próprio front devolve quando a base da API está vazia.
    responde('<!doctype html><html><body><div id="root"></div></body></html>');

    await expect(api.get('/painel')).rejects.toThrow(/base da API está VAZIA/);
    await expect(api.get('/painel')).rejects.toMatchObject({ codigo: 'RESPOSTA_NAO_E_JSON' });
  });

  it('a mensagem aponta para LEADSHUG_API_URL quando a base está vazia', async () => {
    responde('<html></html>');
    await expect(api.get('/painel')).rejects.toThrow(/LEADSHUG_API_URL/);
  });

  it('corpo vazio com 200 continua sendo objeto vazio — isso é legítimo', async () => {
    responde('');
    await expect(api.get('/x')).resolves.toEqual({});
  });

  /**
   * Com a base CONFIGURADA — o cenário do stage.
   *
   * `API_BASE` é lida na importação do módulo, então o `window` precisa existir
   * ANTES dela. Importar de novo com `resetModules` é o que faz este teste
   * exercitar o caminho de verdade, e não o de base vazia.
   */
  async function comBase(url: string) {
    vi.resetModules();
    vi.stubGlobal('window', { __LEADSHUG__: { apiUrl: url } });
    return (await import('./api')) as typeof import('./api');
  }

  it('405 é reconhecido como servidor de ARQUIVOS, não como "API confusa"', async () => {
    // nginx responde 405 a um POST para arquivo estático. É assinatura, não
    // ambiguidade — e dizer isso poupa uma rodada de investigação.
    const mod = await comBase('https://api.exemplo.com.br');
    responde('<html>405</html>', { status: 405 });

    await expect(mod.api.post('/auth/login', {})).rejects.toThrow(/servidor de ARQUIVOS/);
    await expect(mod.api.post('/auth/login', {})).rejects.toThrow(/LEADSHUG_API_URL/);
  });

  it('HTML com 200 também é reconhecido como servidor de arquivos', async () => {
    const mod = await comBase('https://api.exemplo.com.br');
    responde('<!doctype html><html></html>');
    await expect(mod.api.get('/painel')).rejects.toThrow(/servidor de ARQUIVOS/);
  });

  it('resposta não-JSON que NÃO parece estática cai na mensagem genérica', async () => {
    const mod = await comBase('https://api.exemplo.com.br');
    responde('isto não é json nem html', { status: 502 });
    await expect(mod.api.get('/painel')).rejects.toThrow(/não é JSON/);
  });

  it('JSON válido passa como sempre', async () => {
    responde(JSON.stringify({ atendimento: { emEspera: 3 } }));
    await expect(api.get('/painel')).resolves.toEqual({ atendimento: { emEspera: 3 } });
  });
});

describe('base sem esquema (o erro de stage)', () => {
  it('recusa host solto: sem esquema, o navegador trata como CAMINHO', async () => {
    vi.resetModules();
    vi.stubGlobal('window', { __LEADSHUG__: { apiUrl: 'leadshug-api-stage.up.railway.app' } });
    // A chamada viraria https://<o-proprio-front>/leadshug-api-stage.../api/bff/...
    // e bateria no nginx do front — 405 no login, sem nada citando a variável.
    await expect(import('./api')).rejects.toThrow(/sem esquema/);
  });

  it('aceita https e http', async () => {
    vi.resetModules();
    vi.stubGlobal('window', { __LEADSHUG__: { apiUrl: 'https://api.exemplo.com.br' } });
    await expect(import('./api')).resolves.toBeDefined();
  });
});

describe('falha do servidor (o 500 do Nest)', () => {
  it('usa `message` quando não há `error`, e SEMPRE mostra o status', async () => {
    // Formato do 500 do Nest. Antes, isto virava "Falha inesperada." — que não
    // dizia nem que era 500.
    responde(JSON.stringify({ statusCode: 500, message: 'Internal server error' }), { status: 500 });
    await expect(api.post('/auth/login', {})).rejects.toThrow('Internal server error (HTTP 500)');
  });

  it('sem `error` e sem `message`, diz o status mesmo assim', async () => {
    responde(JSON.stringify({ statusCode: 502 }), { status: 502 });
    await expect(api.get('/x')).rejects.toThrow(/respondeu 502 sem explicar/);
  });

  it('recusa do produto continua mostrando a mensagem do produto', async () => {
    responde(JSON.stringify({ error: 'E-mail ou senha inválidos.', code: 'CREDENCIAL_INVALIDA' }), { status: 401 });
    await expect(api.post('/auth/login', {})).rejects.toThrow(/E-mail ou senha inválidos/);
  });
});

describe('requisição com cabeçalho de correlação', () => {
  it('envia Idempotency-Key sem colocar dados transitórios na URL', async () => {
    const fetchMock = vi.fn(async (_input: RequestInfo | URL, _init?: RequestInit) => ({ status: 201, ok: true, text: async () => '{"attempt":{"id":"a"}}' }));
    vi.stubGlobal('fetch', fetchMock);
    await api.postWithHeaders('/number-registrations', { tipo: 'OFICIAL' }, { 'idempotency-key': 'test-key' });
    const [url, init] = fetchMock.mock.calls[0] as unknown as [string, RequestInit];
    expect(url).toContain('/api/bff/number-registrations');
    expect(url).not.toContain('test-key');
    expect(new Headers(init.headers).get('idempotency-key')).toBe('test-key');
    expect(init.body).toBe('{"tipo":"OFICIAL"}');
  });
});
````

## Snapshot: web-app/src/config.ts

Original SHA256: ca30d02d04774b79d6e62715c83c49dd23f1db02f0b49ec6781634acbf09befb

````text
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
````

## Snapshot: web-app/src/App.tsx

Original SHA256: 2562715676e2c06d1eab190b1739becae8bc5a9f24eacc47036566c11945236a

````text
import { useEffect, useState } from 'react';
import {
  BrowserRouter,
  NavLink,
  Navigate,
  Route,
  Routes,
  useLocation,
  useNavigate,
} from 'react-router-dom';
import { Eu, PRODUTO_MUDOU, SESSAO_MORTA, api, urlDoArquivo } from './api';
import Login from './telas/Login';
import Numeros from './telas/Numeros';
import Inbox from './telas/Inbox';
import Consultar from './telas/Consultar';
import Integracao from './telas/Integracao';
import Usuarios from './telas/Usuarios';
import Setores from './telas/Setores';
import Painel from './telas/Painel';
import Perfil from './telas/Perfil';
import DefinirSenha from './telas/DefinirSenha';
import Historico from './telas/Historico';
import Wizard from './telas/Wizard';
import TrocarSenha from './telas/TrocarSenha';
import IdentidadeVisual from './telas/IdentidadeVisual';
import Typebot from './telas/Typebot';

export default function App() {
  const [eu, setEu] = useState<Eu | null>(null);
  const [carregando, setCarregando] = useState(true);
  const [pendente, setPendente] = useState(false);

  const recarregar = () =>
    api
      .get<Eu>('/me')
      .then((r) => {
        setEu(r);
        setPendente(false);
      })
      .catch(() => setEu(null))
      .finally(() => setCarregando(false));

  useEffect(() => {
    void recarregar();
    // Sessão morta em QUALQUER chamada derruba o estado aqui, e o roteador
    // manda para /login sozinho — em vez de cada tela mostrar "não autenticado".
    const aoMorrer = () => setEu(null);
    // Estado VELHO, não erro: a conta não terminou o wizard, ou um módulo foi
    // desligado com esta aba aberta. Rebusca e remonta, sem tela de erro.
    const aoMudar = () => setPendente(true);
    window.addEventListener(SESSAO_MORTA, aoMorrer);
    window.addEventListener(PRODUTO_MUDOU, aoMudar);
    return () => {
      window.removeEventListener(SESSAO_MORTA, aoMorrer);
      window.removeEventListener(PRODUTO_MUDOU, aoMudar);
    };
  }, []);

  // O TEMA é preferência DE QUEM OLHA, não da conta: o wizard define o padrão,
  // e a pessoa troca para si. Guardar no navegador basta — é escolha de conforto
  // visual, não configuração que precise atravessar dispositivos.
  const [tema, setTema] = useState<'claro' | 'escuro'>(
    () => (localStorage.getItem('leadshug:tema') as 'claro' | 'escuro' | null) ?? 'claro',
  );
  const [temaEscolhido, setTemaEscolhido] = useState(() => localStorage.getItem('leadshug:tema') !== null);

  // O padrão da conta só vale enquanto a pessoa não escolheu o dela.
  useEffect(() => {
    const daConta = eu?.produto?.marca?.tema;
    if (!temaEscolhido && (daConta === 'claro' || daConta === 'escuro')) setTema(daConta);
  }, [eu, temaEscolhido]);

  // A marca vem do servidor, nunca do build (ADR-0016 §3). A cor escolhida é a
  // origem dos tokens derivados também; deixar os derivados estáticos fazia a
  // identidade aparecer apenas em alguns botões.
  useEffect(() => {
    const raiz = document.documentElement;

    if (tema === 'escuro') raiz.setAttribute('data-theme', 'dark');
    else raiz.removeAttribute('data-theme');

    const cor = tema === 'escuro' ? (eu?.produto?.marca?.corEscuro ?? eu?.produto?.marca?.cor) : (eu?.produto?.marca?.corClaro ?? eu?.produto?.marca?.cor);
    const corSecundaria = eu?.produto?.marca?.corSecundaria;
    if (cor || corSecundaria) {
      if (cor) {
      raiz.style.setProperty('--brand', cor);
      raiz.style.setProperty('--brand-deep', 'color-mix(in srgb, var(--brand) 82%, black)');
      raiz.style.setProperty('--brand-soft', 'color-mix(in srgb, var(--brand) 16%, transparent)');
      raiz.style.setProperty('--brand-ink', 'color-mix(in srgb, var(--brand) 72%, black)');
      raiz.style.setProperty('--brand-secondary', corSecundaria || '#27272A');
      }
    } else {
      for (const token of ['--brand', '--brand-deep', '--brand-soft', '--brand-ink', '--brand-secondary']) raiz.style.removeProperty(token);
    }
  }, [eu, tema]);

  function trocarTema() {
    const novo = tema === 'escuro' ? 'claro' : 'escuro';
    localStorage.setItem('leadshug:tema', novo);
    setTemaEscolhido(true);
    setTema(novo);
  }

  if (carregando) return <div className="centro">carregando…</div>;

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<TelaDeLogin eu={eu} aoEntrar={recarregar} />} />
        {/* Convite e recuperação chegam por link, e valem MESMO com sessão
            aberta: quem clica pode estar em outro navegador, ou ser outra
            pessoa. Por isso a rota vem antes do `ExigeSessao`. */}
        <Route path="/definir-senha" element={<TelaDeSenha aoEntrar={recarregar} />} />
        <Route
          path="*"
          element={
            <ExigeSessao eu={eu}>
              {eu?.precisaTrocarSenha ? (
                // Senha → wizard → produto (ADR-0016, Emenda 1 §3). A troca é
                // trava de SEGURANÇA e vem primeiro; o servidor cobra a mesma
                // ordem, e a tela só reflete.
                <TrocarSenha aoTrocar={recarregar} />
              ) : pendente || eu?.produto?.onboardingPendente ? (
                <Wizard aoConcluir={recarregar} />
              ) : (
              <Moldura eu={eu!} aoSair={recarregar} aoAtualizar={recarregar} tema={tema} aoTrocarTema={trocarTema} />
              )}
            </ExigeSessao>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

function TelaDeSenha({ aoEntrar }: { aoEntrar: () => void }) {
  const navegar = useNavigate();
  const token = new URLSearchParams(useLocation().search).get('t') ?? '';
  if (!token) return <Navigate to="/login" replace />;
  return (
    <DefinirSenha
      token={token}
      aoEntrar={() => {
        aoEntrar();
        navegar('/inbox', { replace: true });
      }}
    />
  );
}

/** Sem sessão, vai para /login — guardando de onde veio, para voltar depois. */
function ExigeSessao({ eu, children }: { eu: Eu | null; children: JSX.Element }) {
  const local = useLocation();
  if (!eu) return <Navigate to="/login" replace state={{ de: local.pathname + local.search }} />;
  return children;
}

/** Quem já tem sessão não fica na tela de login: volta para onde queria ir. */
function TelaDeLogin({ eu, aoEntrar }: { eu: Eu | null; aoEntrar: () => void }) {
  const local = useLocation() as { state?: { de?: string } };
  const destino = local.state?.de && local.state.de !== '/login' ? local.state.de : '/inbox';
  if (eu) return <Navigate to={destino} replace />;
  return <Login aoEntrar={aoEntrar} />;
}

/**
 * Grupo retrátil da barra lateral (o `groups` do desenho).
 *
 * O estado é por navegador e por grupo: quem trabalha só em Atendimento fecha os
 * outros dois e não os reabre a cada visita.
 */
function Grupo({ chave, rotulo, children }: { chave: string; rotulo: string; children: React.ReactNode }) {
  const [aberto, setAberto] = useState(() => localStorage.getItem(`leadshug:grupo:${chave}`) !== 'fechado');

  function alternar() {
    const novo = !aberto;
    localStorage.setItem(`leadshug:grupo:${chave}`, novo ? 'aberto' : 'fechado');
    setAberto(novo);
  }

  return (
    <div className="grupo">
      <button type="button" className="rotulo" onClick={alternar} aria-expanded={aberto}>
        <span>{rotulo}</span>
        <span className={`seta ${aberto ? 'aberta' : ''}`}>▾</span>
      </button>
      {aberto && children}
    </div>
  );
}

function Item({ para, rotulo }: { para: string; rotulo: string }) {
  return (
    <NavLink to={para} className={({ isActive }) => (isActive ? 'ativo' : '')}>
      {rotulo}
    </NavLink>
  );
}

/**
 * A moldura do `LeadsHug.dc`: barra lateral com três grupos.
 *
 * O menu é MONTADO a partir de `produto.modulos` e do papel — módulo desligado
 * não é escondido por CSS, a rota não existe (ADR-0016 §6).
 */
function Moldura({
  eu,
  aoSair,
  aoAtualizar,
  tema,
  aoTrocarTema,
}: {
  eu: Eu;
  aoSair: () => void;
  aoAtualizar: () => void;
  tema: 'claro' | 'escuro';
  aoTrocarTema: () => void;
}) {
  const navegar = useNavigate();
  const podeAdministrar = eu.papel === 'ADMIN' || eu.papel === 'OWNER';
  const marca = eu.produto?.marca?.nome || 'LeadsHug';
  const logo = urlDoArquivo(eu.produto?.marca?.logo);

  async function sair() {
    await api.post('/auth/logout');
    aoSair();
    navegar('/login', { replace: true });
  }

  return (
    <div className="casca">
      <aside className="lateral">
        <div className="marca">
          {logo ? (
            <img src={logo} alt={marca} />
          ) : (
            <span className="selo">{marca.slice(0, 1).toUpperCase()}</span>
          )}
          <strong>{marca}</strong>
        </div>

        <Grupo chave="op" rotulo="OPERAÇÃO">
          <Item para="/painel" rotulo="Painel" />
          <Item para="/inbox" rotulo="Atendimento" />
          <Item para="/consultar" rotulo="Consultar" />
          {podeAdministrar && <Item para="/historico" rotulo="Histórico" />}
        </Grupo>

        <Grupo chave="cad" rotulo="CADASTROS">
          {podeAdministrar && <Item para="/pessoas" rotulo="Pessoas" />}
          <Item para="/numeros" rotulo="Números" />
          <Item para="/setores" rotulo="Setores" />
        </Grupo>

        {podeAdministrar && (
          <Grupo chave="cfg" rotulo="CONFIGURAÇÕES">
            <Item para="/integracao" rotulo="Meta / WABA" />
          <Item para="/identidade-visual" rotulo="Identidade visual" />
            <Item para="/typebot" rotulo="Typebot" />
          </Grupo>
        )}

        <div className="rodape">
          <NavLink
            to="/perfil"
            aria-label="Meu perfil"
            className={({ isActive }) => (isActive ? 'ativo' : '')}
          >
            <span>
              {eu.nome}
              <br />
              <span className="suave">{eu.papel}</span>
            </span>
          </NavLink>
          <div className="linha">
            <button onClick={aoTrocarTema} aria-label="Alternar tema">
              {tema === 'escuro' ? 'Tema claro' : 'Tema escuro'}
            </button>
            <button onClick={sair}>Sair</button>
          </div>
        </div>
      </aside>

      <div className="painel">
        <main>
          <Routes>
            {/* Entrar cai no ATENDIMENTO, não no Painel: é a tela que mostra
                em nome de quem se está trabalhando, e é o trabalho do dia. O
                Painel é resumo — resumo não confirma nada a quem acabou de
                entrar. */}
            <Route path="/" element={<Navigate to="/inbox" replace />} />
            <Route path="/painel" element={<Painel />} />
            <Route path="/inbox" element={<Inbox eu={eu} />} />
            <Route path="/consultar" element={<Consultar />} />
            <Route path="/numeros" element={<Numeros eu={eu} />} />
            <Route path="/setores" element={<Setores podeAdministrar={podeAdministrar} />} />
            {/* Só monta o que o papel alcança: rota que existiria e responderia
                403 é convite para descobrir a permissão por tentativa. */}
            {podeAdministrar && <Route path="/pessoas" element={<Usuarios />} />}
            {podeAdministrar && <Route path="/historico" element={<Historico />} />}
            <Route path="/perfil" element={<Perfil eu={eu} aoSalvar={aoSair} />} />
            {podeAdministrar && <Route path="/integracao" element={<Integracao />} />}
            {podeAdministrar && <Route path="/identidade-visual" element={<IdentidadeVisual aoSalvar={aoAtualizar} />} />}
            {podeAdministrar && <Route path="/typebot" element={<Typebot />} />}
            <Route path="*" element={<Navigate to="/inbox" replace />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}
````

## Snapshot: web-app/package.json

Original SHA256: fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de

````text
{
  "name": "@leadshug/web",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview",
    "test": "vitest run",
    "test:tela": "npm run build && playwright test",
    "test:tela:ui": "playwright test --ui"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.28.0"
  },
  "devDependencies": {
    "@playwright/test": "^1.62.1",
    "@types/react": "^18.3.12",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.3.4",
    "typescript": "^5.6.0",
    "vite": "^5.4.11",
    "vitest": "^2.1.0"
  }
}
````

## Snapshot: web-app/playwright.config.ts

Original SHA256: d69c084d15cfef29ad23851036cb90309c60aa7a7b16c6810e3ae9b0adbbdd98

````text
import { defineConfig } from '@playwright/test';

/** Porta própria: a 3000 desta máquina é de outro projeto. */
const PORTA_DA_API = process.env.LEADSHUG_API_PORT ?? '3100';
const API = `http://127.0.0.1:${PORTA_DA_API}`;
const DATABASE_URL = process.env.LEADSHUG_E2E_DATABASE_URL;
if (!DATABASE_URL) throw new Error('LEADSHUG_E2E_DATABASE_URL precisa apontar para o banco descartável dedicado.');

/**
 * Teste de navegador contra a tela **buildada**, não contra o dev server.
 *
 * O que ele existe para pegar é justamente o que o teste de API não pega: erro
 * de renderização, tela branca, rota que não leva a lugar nenhum. Foi assim que
 * "Cannot read properties of undefined" apareceu — depois de o QA topar com ela.
 *
 * Sobe dois processos: a API (com o Postgres local do docker compose) e o
 * `vite preview` servindo o `dist`. Mesma origem, como em desenvolvimento.
 */
export default defineConfig({
  globalSetup: './e2e/timeline-freshness.ts',
  testDir: './e2e',
  timeout: 30_000,
  fullyParallel: false,
  workers: 1,
  use: {
    baseURL: 'http://127.0.0.1:4173',
    trace: 'retain-on-failure',
  },
  webServer: [
    {
      command: 'node ../api-app/test/timeline-fixtures.cjs',
      url: 'http://127.0.0.1:3101/health',
      reuseExistingServer: false,
      timeout: 30_000,
      stdout: 'pipe',
      stderr: 'pipe',
      env: {
        DATABASE_URL,
        LEADSHUG_E2E_DATABASE_URL: DATABASE_URL,
        LEADSHUG_API_PORT: PORTA_DA_API,
        LEADSHUG_FIXTURE_PORT: '3101',
      },
    },
    {
      // `build &&` NÃO é zelo: `npm run start` da api é `node dist/main.js`, e
      // sem construir antes o teste de tela valida uma API VELHA — que é o
      // oposto do que ele existe para fazer. Foi assim que uma mudança de schema
      // passou por aqui reportando 500 de um dist de duas fases atrás.
      command: 'npm --prefix ../api-app run build && node ../api-app/test/browser-server.cjs',
      url: `${API}/health`,
      // Não reaproveitar: esta máquina roda outros serviços, e "já tem algo na
      // porta" foi o que fez a primeira corrida testar o projeto vizinho.
      reuseExistingServer: false,
      // 60s cobriam só o `start`; o comando passou a incluir o build, e num
      // runner frio isso não cabia.
      timeout: 180_000,
      // O log do servidor SOBE para a saída do teste.
      //
      // Sem isto, uma falha de boot aparece só como "Timed out waiting from
      // config.webServer" — sem uma linha do que a API disse. Foi exatamente
      // assim que este erro chegou do CI: um timeout, e nenhuma pista.
      stdout: 'pipe',
      stderr: 'pipe',
      env: {
        // O `.env` da API pode apontar para outro Postgres local (por exemplo,
        // o serviço legado na 5433). O harness deve ser determinístico e falar
        // com o Postgres deste compose, publicado na 55433.
        DATABASE_URL,
        LEADSHUG_E2E_DATABASE_URL: DATABASE_URL,
        SESSION_SECRET: 'segredo-de-e2e',
        INTERNAL_SERVICE_TOKEN: 'token-de-e2e',
        // O canal oficial é o PISO do produto: sem ele o processo não sobe
        // (ADR-0016, Emenda 2 §1).
        WHATSAPP_TOKEN: 'token-de-e2e',
        // Volume de arquivo (ADR-0024). Sem ele o produto recusa upload — e o
        // teste de tela precisa exercitar o caminho que EXISTE em stage.
        LH_ARQUIVOS_DIR: '/tmp/leadshug-arquivos-e2e',
        // O link do convite é montado com isto (ADR-0025): sem ele, o e-mail sai
        // com caminho relativo, que não abre em lugar nenhum.
        WEB_ORIGIN: 'http://127.0.0.1:4173',
        PORT: PORTA_DA_API,
      },
    },
    {
      // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`,
      // e quem resolve esse nome é o sistema. Nesta máquina ele dá só IPv4; no
      // runner do GitHub o `/etc/hosts` põe `::1` primeiro, o servidor sobe em
      // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em
      // porta fechada. O log mostrava o preview NO AR e o teste estourando 60s.
      //
      // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o
      // CORS da API. Só a ponta que ESCUTA ficava a cargo do resolvedor.
      command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort',
      stdout: 'pipe',
      stderr: 'pipe',
      env: { LEADSHUG_API: API },
      url: 'http://127.0.0.1:4173',
      reuseExistingServer: false,
      timeout: 60_000,
    },
  ],
});
````
