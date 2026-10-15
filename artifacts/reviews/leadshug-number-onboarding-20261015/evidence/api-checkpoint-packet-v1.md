# Frozen API checkpoint review v1 — ST-CON-01

Derived, non-authoritative review packet. Sole API writer explicitly stopped after final validation. This is a bounded API correctness/security/adherence checkpoint BEFORE Web/runtime implementation, NOT the final delivery review or a passed security/PCV gate. Overall TODO remains Pending.

## Review objective and boundaries

Independently identify concrete implementation defects, adversarial paths, and missing API protection tests relative to the approved contracts. Review candidate/active credential transitions, grant/session checks before and after provider I/O, retained resource ownership, lease/fencing/cleanup recovery, ingress/raw partitioning/secrets, exact own-number proof, keyed sender/echo acceptance, and Typebot tenant/session behavior. Evaluate maintainability where it creates concrete correctness risk. Do not change product code, run tests, contact providers, read private env/auth files, or create worktrees/goals. Report only to the designated JSON artifact.

Full Web, gateway/runtime, external provider proof, and strengthened PCV probes are acknowledged future phases, not claims made by this API checkpoint. Their absence still blocks final delivery, but do not misclassify that acknowledged phase boundary as an API code defect. Identify missing API tests needed before the checkpoint can be safely consumed by Web. The handoff lists explicit unrun adversarial/PCV cases; green aggregate suites do not certify those cases. No real Meta app or HTTPS exists yet. No external provider or number was contacted.

Current local API branch feature/number-onboarding at baseline ae6a9662c29b77276351aa9de653a47276372246 plus the frozen uncommitted source. Final build/lint,130unit tests and234serial PostgreSQL E2E passed;20migrations. Root verified all42source hashes. API tests use real Nest/session/PG with only external provider ports substituted. Browser and real-device proof do not exist yet. The snapshot includes all42changed files plus essential untouched auth/caller/bootstrap context. Source SHA values refer to original bytes; display blocks normalize line endings to LF.

One root-observed test-quality concern is intentionally open: test/modulos.e2e-spec.ts positive connection tests now assert only legacy409 while titles still claim operation. The exact path was admitted as necessary contract-test work; this is not a waiver of the positive module/piso proof. Independently assess this and any other risks; no conclusion is prescribed. Runtime test image emitted Prisma OpenSSL detection warnings despite passing PG tests; final source-owned runner/runtime remains to be established.

The current TODO contains routine execution HOW concretizations (bounded after cursor, stronger PCV floor, exact fixture-path admissions). They preserve the approved user objective and D-01..10; no new product capability or legacy/runtime adoption is authorized. New conversation by manually supplied contact is ST-CON-04 and excluded.

Read this COMPLETE packet incrementally without truncated tool output. The external manifest records byte hashes and file offsets. Return the native subagent-review-result-v1 JSON schema for review_kind architecture_adherence, with findings including stable IDs, severity, affected paths, concrete exploit/race path, and discrimination test. Overall assessment must explicitly say bounded API review, not finalTODOapproval, and record packet SHA/read completeness. Pure speculative scaling/formatting is not a blocker; classify concrete auth/isolation/credential loss/data corruption or false-readiness defects candidly.


## Frozen file: foundation_documentation/project_constitution.md

Original SHA-256: `f9b8d3397a4f78c74f4c29739eb509d12bfc9ccda84a50fed718bfe7a668566a`; bytes:4345.

```text
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

```

## Frozen file: foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md

Original SHA-256: `84fff496269398ba658e9fb9a4d9b0c072a15dde66ec9d244cd2efba0f62d6f0`; bytes:98708.

```text
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
- **Next exact step:** revisar a API congelada do checkpoint2, resolver achados e completar probes; depois implementar UI e fazer handoff DevOps para o runtime local.

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
| operational-coder | operational-devops | Configurar e provar callback/target de teste se necessário. | Compose local/variáveis/callback e instância própria | planned; target local confirmado, nenhuma infraestrutura alterada. |

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


Adicional de coerência do autor: envelope raw redigido e code/PIN transitórios explicitados, sem alterar modelo de autorização; REG-SEC-08/09.

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

```

## Frozen file: foundation_documentation/modules/integrations-and-channels.md

Original SHA-256: `a248d9b05789689a2f9882e7888458973713821d1183ddfed517d42cfca2034c`; bytes:17675.

```text
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

Um serviço de aceitação de mensagem no domínio inbox é o owner da chave (providerResourceIdentityId,externalMessageId) para TODAS as novas gravações com ID: entrada, eco OUT, resultado de envio BFF/público e Typebot. Sender captura a identidade do canal autenticado, faz HTTP fora de transação e depois cria-ou-reconcilia pelo mesmo índice PostgreSQL. Sender-first, echo-first e ecos concorrentes devolvem o MESMO Message.id; conflito de unique não pode virar segundo registro nulo nem erro de inserção depois do envio bem sucedido. Validar owner BU/conversa/contato/direção na reconciliação; incompatibilidade é erro/quarentena de identidade, sem sobrescrever outro recurso. Registro local sem externalId confirmado conserva pendência/erro explícitos, sem inventar ID, retry externo ou garantia de deduplicação por ID inexistente.

Eco primeiro cria OUT sem autoria humana inventada; resultado interno enriquece o mesmo registro com conteúdo/autoria humana ou Typebot comprovados pelo caller. Eco posterior não apaga/substitui essa autoria e não muda createdAt/ID. Só criação vencedora emite evento de nova mensagem; enriquecimento preserva a identidade e usa refresh/projeção existente, sem novo IN, unread ou bot. Retorno BFF/público mantém seus contratos e contém o registro reconciliado. Invariantes de janela, permissão, conversa BU/contato, ordenação e timeline permanecem. Nenhum cache de ecos em memória ou lookup-antes-insert substitui o índice/transação. Continua explícito o limite de crash depois do commit e antes da publicação; não há claim exactly-once externo.

### Segredos transitórios e webhook raw

Code SDK e PIN podem existir transitoriamente no formulário/memória do browser e seguir via BFF HTTPS; nunca em URL, storage, trace, screenshot, log ou DTO de retorno. Token, chave e envelope ficam somente no backend. Antes de persistir evento raw de provider autenticado, redigir recursivamente apikey, token, authorization, code, PIN, QR e componentes secretos de URLs; erros/audit usam catálogo e metadados allowlisted. Evento sem identidade verificada não persiste conteúdo. Harness envia envelope Evolution com apikey fictícia e comprova sua ausência em raw/audit/DTO/erro. QR só é devolvido efemeramente ao administrador no POST autorizado. Gateway Nginx, proxy e logs de aplicação não registram URI/token do callback Evolution: política explícita remove caminho secreto e query de access/error logs, inclusive erros; harness passa segredo fictício pelo gateway real e inspeciona logs/artefatos. Callback por header só se suportado e comprovado no provider fixado, sem presumir capacidade.

Meta raw é particionado por recurso verificado/BU, não por corpo de request inteiro. Batch assinado com entry/change/value de BUs diferentes produz registros scoped separados; fragmento desconhecido/retirado/sem identidade contribui apenas metadados allowlisted, sem conteúdo. Assinatura é verificada sobre o corpo original antes de parse/partição. REG-SEC-12/13 concretizam requisitos já existentes de segredo/owner, sem novo armazenamento genérico.

```

## Frozen file: foundation_documentation/modules/identity-and-tenancy.md

Original SHA-256: `604371cc509981d4561ce3cf404857990e5d30126ea04bda2a766aa0eeee1c91`; bytes:2014.

```text
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

```

## Frozen file: foundation_documentation/modules/inbox-and-conversations.md

Original SHA-256: `592313ddd91cf00b76208b63c4fcdce3ec150109c23bd083301744431529fa5f`; bytes:12019.

```text
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

APROVADO em2026-10-15; **implementação/verificação pendentes**, sem alterar o contrato de timeline verificado acima. Owner inbox-and-conversations; identidade externa e pareamento pertencem a [canais](integrations-and-channels.md#cadastro-de-números-st-con-01). Execução no [TODO](../todos/active/features/TODO-leadshug-channel-connection-readiness.md).

Entrada aceita exige externalMessageId não vazio e chave única PostgreSQL (providerResourceIdentityId,externalMessageId); identidade já incorpora provider. Mesmo ID em recursos diferentes não colide. `Message` legado pode manter FK/chave nulas; não inventar IDs nem apagar duplicatas históricas. Só backfill inequivocamente comprovado é admitido. Novas entradas sem ID ficam rejeitadas com erro seguro antes de efeito de domínio. Após identidade validada, transação curta aceita Message e cria/reusa conversa BU/contato com incremento unread; conflito de unique desfaz os efeitos daquela tentativa. Somente a transação vencedora publica realtime e aciona automação. Echo OUT e resultado do sender compartilham a mesma aceitação transacional por identidade/ID, inclusive quando o echo chega primeiro; não criam outra Message, IN ou unread. Contrato detalhado abaixo. Replay sequencial/concorrente retorna sucesso idempotente para evento já aceito. Não se promete exactly-once externo: crash depois do commit pode deixar publicação/automação ausente; não repetir bot automaticamente nem introduzir plataforma de jobs/outbox neste recorte. Essa limitação precisa constar do runbook.

IncomingService deriva Mantenedora da BU verificada. Busca de trigger exige bot.mantenedoraId desse tenant e buId exata OU trigger global dentro do MESMO tenant. Sessão retomada deve pertencer à mesma Mantenedora/BU/contato; sessão estrangeira falha fechado antes de texto externo. Criação deriva owner do contexto verificado, não de um bot arbitrário. Dois tenants com triggers globais concorrentes não compartilham bot, texto, sessão, saída ou credencial. São defeitos preexistentes na superfície tocada, cuja correção fica expressamente incluída para sustentar o recebimento deste cadastro.

Um serviço de aceitação de mensagem no domínio inbox é o owner da chave (providerResourceIdentityId,externalMessageId) para TODAS as novas gravações com ID: entrada, eco OUT, resultado de envio BFF/público e Typebot. Sender captura a identidade do canal autenticado, faz HTTP fora de transação e depois cria-ou-reconcilia pelo mesmo índice PostgreSQL. Sender-first, echo-first e ecos concorrentes devolvem o MESMO Message.id; conflito de unique não pode virar segundo registro nulo nem erro de inserção depois do envio bem sucedido. Validar owner BU/conversa/contato/direção na reconciliação; incompatibilidade é erro/quarentena de identidade, sem sobrescrever outro recurso. Registro local sem externalId confirmado conserva pendência/erro explícitos, sem inventar ID, retry externo ou garantia de deduplicação por ID inexistente.

Eco primeiro cria OUT sem autoria humana inventada; resultado interno enriquece o mesmo registro com conteúdo/autoria humana ou Typebot comprovados pelo caller. Eco posterior não apaga/substitui essa autoria e não muda createdAt/ID. Só criação vencedora emite evento de nova mensagem; enriquecimento preserva a identidade e usa refresh/projeção existente, sem novo IN, unread ou bot. Retorno BFF/público mantém seus contratos e contém o registro reconciliado. Invariantes de janela, permissão, conversa BU/contato, ordenação e timeline permanecem. Nenhum cache de ecos em memória ou lookup-antes-insert substitui o índice/transação. Continua explícito o limite de crash depois do commit e antes da publicação; não há claim exactly-once externo.

A verificação final de mapping/epoch deve ser sincronizada à gravação de conteúdo, incluindo webhook em voo atravessando RENEW/remove-recreate. A projeção existente após refresh mostra o mesmo ID enriquecido; se exigir diff hoje excluído, registrar a falha antes de admitir mudança de escopo. Não há autorização para Nova conversa manual, importação, sequenciamento de bot para mensagens distintas, worker ou outbox.

```

## Frozen file: foundation_documentation/modules/audit-and-history.md

Original SHA-256: `e17c81ff017a21865e052f903b4ae4712c7c9313cae4505ff54a4cab6004a886`; bytes:1612.

```text
# Module: Audit and History
**Version:** 1.0

Owns durable activity history, message auditability, exports and access to historical relationship data.

## Invariants

- History is append-oriented and is not silently discarded.
- Every record is tenant- and BU-scoped.
- Read permission is evaluated independently from write permission.


## Cadastro e diagnóstico de canais — ST-CON-01

APROVADO em2026-10-15, **implementação/verificação pendentes** no [TODO](../todos/active/features/TODO-leadshug-channel-connection-readiness.md). Canais é o owner das etapas; audit-and-history governa seus registros duráveis.

- Atividade de cadastro/autorizar/confirmar/parear/verificar/cancelar preserva ator, Mantenedora/BU, etapa, correlação e erro de catálogo, sem segredo, QR ou conteúdo externo bruto no audit.
- Só conteúdo de recurso com owner/identidade verificados entra em raw scoped. Batch Meta é particionado por recurso/BU depois de validar assinatura do corpo original; partes desconhecidas/retiradas conservam apenas metadados allowlisted.
- Token, apikey, authorization, code/PIN/QR e componentes secretos de URLs são removidos antes de raw, audit, erro ou logs. Proteger URI Evolution e hub.verify_token Meta também no gateway/access/error/application logs.
- Payload sem identidade corrente, inclusive webhook velho pausado através da aposentadoria, não grava conteúdo. Rejeição/pending só registra metadados seguros.
- Cancelamento/remoção/repareamento não apagam BU, conversas ou histórico; tombstones de identidade preservam owner. Sem merge/delete silencioso na migration.

```

## Frozen file: foundation_documentation/artifacts/validation-plans/leadshug-channel-readiness-20261015.md

Original SHA-256: `34d6a013db00b5db9b696d24c0bede282efb9d9eca3037c9a37cbd938c74611e`; bytes:16117.

```text
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

## Notas de execução aceitas na revisão delta v3

Concretização de requisitos congelados, sem novo produto/arquitetura ou dispensa:

- REG-SEC-10/BCI: pausar webhook antigo DEPOIS do lookup preliminar e antes de raw/conteúdo; RENEW aposenta mapping e invalida prova. Liberar webhook e comprovar que o guard final sincronizado com aceitação impede conteúdo/receipt/unread/realtime/bot. Repetir remove/recreate. Não rotular sender antigo como recurso novo.
- REG-SEC-12: atravessar gateway também com hub.verify_token Meta fictício, aceito e rejeitado; segredo ausente em access/error/application logs e artefatos, preservando challenge/autenticação.
- REG-SEC-11/browser: mostrar OUT echo-first antes da resposta do sender, fazer refresh/pós-ação existente e conferir uma linha com mesmo Message.id/createdAt e autoria/conteúdo confiáveis, sem cursor/unread alterados. Se o cliente atual não satisfizer a projeção, registrar falha e admitir diff/escopo pelo processo normal antes de tocar Inbox.tsx excluído; a nota não autoriza tal edição.

Todos os casos continuam planned, com fonte/DB/backend reais na execução autorizada. Nenhuma prova executada nesta revisão documental.

```

## Frozen file: foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/checkpoint2-api-handoff.md

Original SHA-256: `4209faafdc1a2e64ef8e1d1d4b8c7140805e158538221dd2844247a60ae0aac0`; bytes:6860.

```text
# Checkpoint 2 — API onboarding and caller cutover

Status: implementation handoff for independent API review. The bounded API checkpoint is implemented and validated; the larger TODO remains open. No commit or push has been made. Product edits are stopped pending root review.

## Source and validation

- Checkout: `api-app`, branch `feature/number-onboarding`, baseline `ae6a9662c29b77276351aa9de653a47276372246`.
- Source manifest and SHA-256: `checkpoint2-api-source-hashes.sha256` (42 product files, including three additive migrations).
- Validation source tree: the same checkout/source hashes above. Node runner: `node:22.23.3-slim`; PostgreSQL 16 container: `leadshug-number-onboarding-pg16-final`; isolated database `leadshug_timeline_onboarding`; reusable dependency volume `leadshug-number-onboarding-node-modules`.
- Fresh disposable database migration deployment: 20 migrations found; third new migration `20261015140000_number_onboarding_channel_operation_fence` applied successfully. Raw output: `checkpoint2-api-migrate-deploy-final.log`.
- Final source command: `npm run build && npm run lint && npm test && npm run test:e2e` in the Node 22 container, with `DATABASE_URL` explicitly pointed at that isolated PG16 database. Raw output: `checkpoint2-api-final-source-validation.log`.
- Final results: build PASS; lint PASS; unit 20 files / 130 tests PASS; serial PostgreSQL E2E 22 files / 234 tests PASS. Targeted lifecycle evidence is also retained in `checkpoint2-api-lifecycle-targeted-rerun.log` (two selected lifecycle tests PASS). The earlier deliberately failing recovery probe is retained as `checkpoint2-api-lifecycle-targeted-failed.log`; it identified the stale-session check after subscription and was corrected before the final full validation.
- `checkpoint2-evolution-first-in-pg.log` preserves the initial targeted Evolution run. `checkpoint2-api-full-e2e-rerun1.log` is an earlier full-suite run (232 tests, before the last two lifecycle cases); it is superseded by the final source run.

## API contract for Web

`GET /api/bff/number-registrations/capabilities` returns installation/module availability for `oficial` and `naoOficial` with safe reason codes. `POST /api/bff/number-registrations` accepts `tipo`, `operation` (`NOVO` or `REAUTORIZAR`), and exactly one of `buId` or `novaBu`; reauthorization also requires `channelId` and `expectedGeneration`. It requires `Idempotency-Key` UUID and returns `{ attempt, nonce, replay }`. The nonce is a one-use correlation value; replay returns it only for the same user/session while pending and valid.

`GET /:id` returns only the allowlisted registration DTO: `{ id, buId, channelId, tipo, operation, state, stage, errorCode, expiresAt, version, generation }`. It excludes attempts' nonce/session hashes, lease data, candidate envelopes, and provider credentials. `POST /:id/authorize` takes `{ nonce, code }`; `GET /:id/options?wabaId=…&after=…` returns the bounded resource page and cursor; `POST /:id/confirm` takes `{ wabaId, phoneNumberId, modoRegistro: "NOVO"|"JA_REGISTRADO", pin?, after? }`; `POST /:id/advance`, `/retry`, and `/cancel` take empty objects.

Safe channel projections in `/api/bff/business-units`, `/api/bff/business-units/:buId`, and `GET /api/bff/business-units/:buId/channels` carry `id`, `type`, `status`, `generation`, `currentAttemptId`, `ownNumberVerified`, `providerConnectionState`, `receiptVerifiedAt`, `requiresWindow`, and `connectedAt`; the business-unit list also carries the user's direct `papel` for that BU. They do not expose provider resource IDs or private credentials.

Evolution pairing is `POST /api/bff/business-units/:buId/channels/nao-oficial/pair` with `{ intent: "INITIAL"|"RENEW", expectedGeneration? }`. `POST /:tipo/verify` verifies the current provider identity. Legacy channel create responds with deterministic `409 USE_NUMBER_REGISTRATIONS`; legacy QR GET responds `405 QR_GET_REMOVED`. Delete is `DELETE /api/bff/business-units/:buId/channels/:tipo`.

## Configuration names

Official Meta install capability: `META_APP_ID`, private `META_APP_SECRET`, `META_SIGNUP_CONFIG_ID`, `GRAPH_VERSION`, `PUBLIC_ORIGIN`, `WEBHOOK_VERIFY_TOKEN`, and `META_APP_SECRET` for signed webhook verification. Credential encryption uses `CHANNEL_CREDENTIAL_KEY_ID` plus `CHANNEL_CREDENTIAL_KEY` (canonical base64 encoding of exactly 32 random bytes). Evolution install capability uses `EVOLUTION_API_URL`, private `EVOLUTION_API_KEY`, `EVOLUTION_WEBHOOK_URL`, and `EVOLUTION_WEBHOOK_SECRET`. Names and placeholder values are documented in `api-app/.env.example`; no real `.env` was written. Global `WHATSAPP_TOKEN` is no longer required or used for channel sending.

## Behavior delivered

The API now has durable registration attempts, separate encrypted candidate/active credentials, unique immutable provider-resource ownership, a persisted per-channel 45-second operation fence, BU/session/grant checks, nonce/idempotency/expiry handling, post-promotion recovery under a fresh valid session, bounded Meta resource paging and selected-page revalidation, scoped credential resolution, signed Meta ingress, fenced Evolution ingress/diagnostics, keyed IN/OUT message acceptance, sender/echo reconciliation, and safe DTO/redaction paths. Existing BFF, public API, Typebot, webhook and inbox writers now route through current mapped identities and the acceptance service; channel readiness requires the applicable own-identity, subscription and receipt evidence. No provider network is inside a database transaction.

## Remaining evidence and dependencies

- Real Meta setup and external proof are still blocked on the user's Meta app/configuration and public HTTPS webhook origin. Fixtures never assert a real `CONNECTED` Meta account, and no external provider call or phone-number change was made. The Meta source contract has been checked against the pinned/provider references recorded in the preceding evidence, but runtime behavior for a real app remains unverified.
- Root's separate final PCV gate calls for 20 operations × 5 repetitions for the high FRC/BCI probes. The existing timeline E2E in this final run executes its established three batches; this API handoff does not claim that strengthened PCV gate.
- Additional stress evidence remains for same-idempotency-key concurrent replay barriers, cancellation/renewal while external requests are paused, stale Evolution cleanup/ambiguous-create recovery under lease expiry, candidate-resource mismatch preserving an already active credential, all per-tenant grant/session revocation interleavings, and real Meta app/scopes/audience. The full suite passing does not substitute for those unrun REG-SEC/PCV probes.
- No final TODO acceptance claim is made. Web integration, root review, final adversarial probe expansion, and real provider setup/proof remain outstanding.

```

## Frozen file: foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/checkpoint2-api-source-hashes.sha256

Original SHA-256: `4b3ea19dc8e72858360cb1775b3aeeb86012d192eac6938296b003ac5428fb53`; bytes:4506.

```text
774be234aa4da8cba07f7482e8998c3296ac81bc6f4d28952953565624be7ebd  .env.example
55d84f5eef1b9b9e9a22891695812e522fe4e405041341218984507426ef0946  prisma/migrations/20261015120000_number_onboarding_foundation/migration.sql
a6fa9ad9e99a0b55ed5d9e86b99d42b603b404c13f41f97ac718e6443f29a3fe  prisma/migrations/20261015130000_number_onboarding_provider_resource_ownership_immutable/migration.sql
e484edd01e78133bcaf23f12fb47e44e92cba44a89b29803eff1530b103bc496  prisma/migrations/20261015140000_number_onboarding_channel_operation_fence/migration.sql
e0701807a0fac3477f327adc60127f76320e8a7681f146b6177bc33546e89a9c  prisma/schema.prisma
bdc829c987de4d8944ce417aea03c76e5484091f7ad4612246807bd22e524efb  src/domain/channels/channel-credential-crypto.spec.ts
4a438a1e73903c011d212962f41b38dfb2a999c539112b6831156664de6d9ef4  src/domain/channels/channel-credential-crypto.ts
7a780d39cfdb42cf5bc6a99f89ec7191211dfc4f03a31f6b4c13d3ef2c0e24b3  src/domain/channels/channel-credential-resolver.ts
63f679ad3a3ff77c6b763c4ee459973c0e679d13108ead1b29942f465a392e29  src/domain/channels/channels.service.ts
4f24fc7cf518685e61d42c300332df9dd64b140f9eeef57901e91ba6a5ff04f4  src/domain/channels/number-registration.service.ts
f4b96c233ef4cda079ee80d04a413444902061efd88935220df550771722693e  src/domain/channels/safe-redaction.spec.ts
66cbcf018a7723849dac83b7f3a6db15c1e795fec11c3f409c7e7d3b69e02123  src/domain/channels/safe-redaction.ts
093f2a2926322ce68c4d7a66f174f7a6c13735c8ce7399ba863766295d1cdbee  src/domain/historico/cobertura.ts
aed31180b6fb58442850421233bd61a62552144642bbac88e7fbef0efa1d1890  src/domain/inbox/conversations.service.ts
57eaf64ba4c896016f83d8ebff1f9cea5ee696d8c9b546f3cc30d53e94af525e  src/domain/inbox/incoming.service.ts
229cd0805d0543b5cbb38cecf97492e1d8a225fa65e166c5fd96547a587edede  src/domain/inbox/incoming.typebot.integration.spec.ts
c959930ad04633d1423be35727070dca2cd52e592549d9f7c40fc00252da07d4  src/domain/inbox/message-acceptance.service.ts
c9348f86f1f2bcfd4af3f9bd3e91cb5218d81cf13098989b5f6ea64acbb41398  src/domain/tenancy/tenancy.service.ts
e33f72f28f4d41b8899a2b48ea13eacf519e0669d88663d74a818f0f8ae80a59  src/infra/config/modulos.spec.ts
42c3fcb8205cb77356da28c756eebc510f8c2597c28ebf22c7314f625359a61c  src/infra/config/modulos.ts
4de63e227810736164c30fee397d1f47133f292f3733e0864264c7f51d1b5c23  src/integrations/evolution/evolution.client.spec.ts
78e810e77d489576b721db10ed629f0145f023d737b3b33ef5efa73f1352763f  src/integrations/evolution/evolution.client.ts
e013ee76b4ba471d5e3b942483e60bc11a6219397fe495f4dc702571b7d2ae13  src/integrations/meta/meta.client.spec.ts
e355cde3a8708723193035659ef89d3ae640c5746dc76f50a623f7c899a500c8  src/integrations/meta/meta.client.ts
1addd7e3cb12d6607d488b17734d4ae85eeb2ec0ae951c7ecaebd65d35c09203  src/surfaces/bff/bff.module.ts
773bbb76dc1377b29430f6b5d6e43e9568b24a5e61121b1ca3237cee9f7641f1  src/surfaces/bff/channels.controller.ts
0edd826d4e9a3c0b8cde4334bf2e88f360f5f5e9d5db99e5dfc4382b5bf71bb0  src/surfaces/bff/me.controller.ts
c57797667ff26a4ea74aa939e4972a8cd8f442c9beafa166b1bdf808e19c236e  src/surfaces/bff/number-registrations.controller.ts
b4fc1da7caadb9e8edb0d719b11783227aa35ee55853f4d0e9f1e06065603936  src/surfaces/public/public.module.ts
156f96ed98e332b0469acd85b2101f2153bcdbfc28917057b8785ac67a5f1a7d  src/surfaces/webhooks/evolution.controller.ts
0ce602e50bf51325f0cf41776eba2ce4f6cd84e9db3856778e8491deee7bdf9b  src/surfaces/webhooks/meta.controller.ts
75cbae0a89be972e98a3b4d7b9358864b9888a1ddff91ba1ea7a4483a9bfd7ac  src/surfaces/webhooks/webhooks.module.ts
c880c8365a5ac6862ae176e2add24b008e4c622ac3136605a287a35257d694b4  test/api-publica.e2e-spec.ts
20db8f160c957c7bfffea6f88b965f9d498dc088683247c02f6aaea99ad75035  test/atendimento.e2e-spec.ts
fd85fa666489fc8b5bf688362e5d142db62e5637384c1606f86b3ecf25c8180e  test/browser-server.cjs
ad54bc3f69a722c6f8454b3f6250d64875940c46afc8b8407bc2dae97d8f903b  test/canais.e2e-spec.ts
828ff79c0ed7f15298b5fe220c1082882a9e6425a0d62fdc4d5a3ff9dd00031c  test/helpers.ts
e54caf54ce08a237abeb0b5bae6d6483662d9cc6bda323f35eece637817cdf00  test/modulos.e2e-spec.ts
ed2d7b6dfd23169280bfad8babe5728bd8b0c6de01158197998a45b858d0c4ae  test/number-onboarding-flow.e2e-spec.ts
c8b29c16412938b64fb8e2555729f0777d9e3eb69a57d29df3d65b56443c4bac  test/number-onboarding-message-acceptance.e2e-spec.ts
cf9335f7bfefecf708d69ab966533bf3b65ed7cc5615533691f7f2a841275422  test/realtime.e2e-spec.ts
0de3e64e4dac55fd4224b7ebf087ad95a0d857eaf058fd95251a6c8caebb0d9f  test/webhooks.e2e-spec.ts

```

## Frozen file: foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/security-reference-refresh.json

Original SHA-256: `e63c9b3a298b9c2ef39af472b370a3b66d583eed003c7591be564af96674d338`; bytes:3246.

```text
{
  "recorded_on": "2026-10-15",
  "artifact_role": "Review preparation and primary-source refresh; not a security gate pass or a vulnerability report",
  "security_risk_level": "high",
  "attack_simulation_decision": "required",
  "simulation_status": "pending final REG-SEC-01..13 evidence and independent review",
  "sources": [
    {
      "url": "https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/",
      "review_relevance": "Object identifiers require authorization for the particular action and object; unpredictable IDs alone do not establish permission.",
      "mapped_surfaces": ["attempt and channel IDs", "BU and tenant grants", "provider resource ownership", "Typebot session ownership"],
      "required_project_evidence": ["cross-tenant and role negatives", "immutable owner conflict before external mutation", "foreign Typebot trigger/session rejection"]
    },
    {
      "url": "https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html",
      "review_relevance": "Authorization transactions need correlation and replay protection; token audience, resource and action restrictions must be enforced.",
      "mapped_surfaces": ["Meta SDK callback lifecycle", "session-bound attempt and one-use nonce/code", "app/scopes/WABA verification", "encrypted candidate promotion"],
      "required_project_evidence": ["stale callback and consumed-code rejection", "app and per-resource scope negatives", "candidate cannot replace another number or the active credential"],
      "limit": "General OAuth guidance does not prove Meta SDK or Graph-version capabilities. Do not invent PKCE/DPoP parameters, expand permissions or replace the approved provider flow without provider evidence. Meta app eligibility and real authorization remain unverified."
    },
    {
      "url": "https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html",
      "review_relevance": "The server must validate workflow transitions and reject out-of-order execution. Sensitive request values require protection from URLs/logs; errors and audit metadata must avoid disclosure.",
      "mapped_surfaces": ["authorize/confirm/advance/retry/cancel", "channel operation lease and generation CAS", "POST-only pairing", "gateway access/error logs", "partitioned provider raw data"],
      "required_project_evidence": ["overlap and stale completion barriers", "invalid-stage and missing-CSRF rejection", "fictitious callback secrets absent from actual gateway/application logs", "signed mixed-owner batch partitioning"],
      "limit": "Provider-mandated query/path secret exceptions require explicit redaction proof; this guidance does not itself waive or certify the approved callback contract."
    }
  ],
  "safety_boundary": "Only public documentation was retrieved for this artifact. No real provider account, number, app, credentials or production target was scanned or mutated. Runtime attack probes remain confined to the approved isolated local harness.",
  "interpretation": "Sources inform independent review hypotheses. They do not add product scope, authorize new platform security features, replace the governing TODO or establish that the current implementation is secure."
}

```

## Frozen file: foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/provider-contract-source-verification.json

Original SHA-256: `efdc248c3d584d8743b4356152ed831ff3c4e55780e21d43aa9a5483df4525b7`; bytes:3849.

```text
{
  "date_local": "2026-10-15",
  "scope": "Public primary source investigation only, no provider account/credential/instance calls",
  "evolution": {
    "tag": "2.3.7",
    "tag_object": "6a398a6a08e59eb87dcf98b0f389e8decaf08689",
    "commit": "cd800f2976e1e5b682fbf86a01ee4d85ae61f370",
    "image": "evoapicloud/evolution-api:v2.3.7@sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339",
    "sources": [
      {
        "url": "https://raw.githubusercontent.com/evolution-foundation/evolution-api/2.3.7/src/api/routes/instance.router.ts",
        "sha256": "961a89e70ac160ccbf59f3a3027220217cb6401060a37c6841f4ece1d1b27b7f",
        "facts": [
          "fetchInstances is GET and accepts instanceName/instanceId filter through InstanceDto.",
          "Provider connect is GET with external side effect; LeadsHug BFF must expose only its administrative POST."
        ]
      },
      {
        "url": "https://raw.githubusercontent.com/evolution-foundation/evolution-api/2.3.7/src/api/services/monitor.service.ts",
        "sha256": "f9b3583c5b70a95f402e7594247ecd42a3825a99e2283c75d336833ef2f9ba17",
        "facts": [
          "Filtered instanceInfo uses the exact supplied instance name and returns stored instance details.",
          "Projection must allowlist identity/status only; do not persist/return/log complete fetchInstances response because it can contain provider credentials."
        ]
      },
      {
        "url": "https://raw.githubusercontent.com/evolution-foundation/evolution-api/2.3.7/src/api/dto/instance.dto.ts",
        "sha256": "8eaa94a823b4e5bcd1e5172e3de1191e0c1f6f355458cf5265afa14d63c875e3",
        "facts": [
          "Instance shape includes ownerJid, connectionStatus and name, and supports per-instance webhook headers."
        ]
      },
      {
        "url": "https://raw.githubusercontent.com/evolution-foundation/evolution-api/2.3.7/src/api/integrations/event/webhook/webhook.controller.ts",
        "sha256": "8d7dd73a3d658cca0a827fdf97f674446c33fc8372fa9f89462921215c5df090",
        "facts": [
          "Configured per-instance headers are attached to outbound webhook requests.",
          "Header authentication is therefore source-supported as the optional callback mechanism already allowed by the approved plan; no runtime proof or selected route change is claimed here."
        ]
      }
    ],
    "limit": "Pinned source contract is evidence for adapter construction, not identity/connection readiness of any running instance or proof that the pinned image was exercised."
  },
  "meta": {
    "sources": [
      {
        "url": "https://www.postman.com/meta/whatsapp-business-platform/collection/du6gzjv/embedded-signup",
        "facts": [
          "Signup requires subsequent integration steps; installation eligibility and HTTPS remain prerequisites."
        ]
      },
      {
        "url": "https://www.postman.com/meta/whatsapp-business-platform/request/mk4p87j/register-phone-number",
        "facts": [
          "Explicit phone registration uses six-digit PIN; no unregister/migration or forced re-registration is authorized."
        ]
      },
      {
        "url": "https://www.postman.com/meta/whatsapp-business-platform/request/0yubu4i/subscribe-app-to-whatsapp-business-account",
        "facts": [
          "WABA subscription is a distinct POST after webhook configuration; no callback takeover."
        ]
      }
    ],
    "direct_developers_documentation": "429 rate limited during this inspection",
    "limit": "Older generic Postman collection includes BSP credit-line material outside the approved Tech Provider scope; do not adopt that workflow. Actual app configuration/Graph permissions/token exchange/register/subscription still need real proof. Do not invent unsupported readiness fields or use global WHATSAPP_TOKEN."
  }
}

```

## Frozen file: api-app/.env.example

Original SHA-256: `774be234aa4da8cba07f7482e8998c3296ac81bc6f4d28952953565624be7ebd`; bytes:3210.

```text
# Copie para .env no ambiente local. Em produção, as variáveis vivem no serviço
# da Railway — nunca no repositório (regra 4 do CLAUDE.md).

NODE_ENV=development
PORT=3000

# --- Banco (ADR-0003) ---
# Local: docker compose do repositório. Railway: referência ao serviço postgres.
# ATENÇÃO (ADR-0002): a rede privada da Railway é IPv6 (*.railway.internal só
# publica AAAA). Nenhum cliente pode forçar family: 4.
DATABASE_URL=postgresql://leadshug:leadshug@localhost:5433/leadshug?schema=public

# --- Superfície interna (ADR-0006, Emenda 1) ---
# Sem esta variável a superfície interna NEGA TUDO — ausência de configuração é
# negação, nunca liberação.
INTERNAL_SERVICE_TOKEN=

# --- Sessão do BFF (ADR-0007) ---
# Cookie assinado por HMAC. Gerar com: openssl rand -hex 32
SESSION_SECRET=

# --- Front em serviço próprio (ADR-0015) ---
# Em desenvolvimento, o proxy do Vite deixa tudo na mesma origem e estas duas
# não são necessárias. Em stage/produção elas são obrigatórias, e os dois
# serviços precisam ficar sob o MESMO domínio.
# WEB_ORIGIN=https://app.seudominio.com.br
# COOKIE_DOMAIN=.seudominio.com.br
#
# Stage nos domínios da Railway: up.railway.app é sufixo público, então os dois
# serviços são SITES diferentes e o cookie Lax não viaja. Nesse caso, omita o
# COOKIE_DOMAIN e ligue:
# COOKIE_SAMESITE=None
# Proibido em produção — com None o CSRF depende só do X-Requested-With.

# --- Capacidade de instalação Meta Embedded Signup ---
# Todos ausentes mantém a administração disponível e informa capacidade indisponível.
# META_APP_ID=
# META_APP_SECRET=
# META_SIGNUP_CONFIG_ID=
# GRAPH_VERSION=v21.0
# PUBLIC_ORIGIN=https://api.example.invalid
# CHANNEL_CREDENTIAL_KEY_ID=local-key-v1
# CHANNEL_CREDENTIAL_KEY=<canonical-base64-of-exactly-32-random-bytes>

# --- Typebot Cloud (automação via WhatsApp oficial) ---
# O token permanece somente no backend. Nunca enviar ao navegador.
# TYPEBOT_API_URL=https://app.typebot.io/api/v1
# TYPEBOT_API_TOKEN=
# TYPEBOT_WORKSPACE_ID=

# --- Módulos da instalação (o TETO) ---
# A env diz o que ESTA instalação é capaz de fazer; a Mantenedora escolhe dentro
# dele, no wizard, e o efetivo é a interseção (ADR-0016). Só existe flag para
# módulo que TEM código atrás: CRM está fora da v1.1, disparo é v2, e o
# histórico deixou de ser módulo — nenhum deles tem variável.
# LH_CHANNEL_UNOFFICIAL=false

# --- Canal não oficial (Evolution API) ---
# Serviço interno do projeto Railway, SEM domínio público.
# Exigidas quando LH_CHANNEL_UNOFFICIAL=true, e verificadas NO BOOT: ligar o
# módulo sem a credencial dele é erro de implantação, não 503 no meio do fluxo.
# EVOLUTION_API_URL=http://evolution-api.railway.internal:8080
# EVOLUTION_API_KEY=
# EVOLUTION_WEBHOOK_URL=https://api.example.invalid/webhooks/evolution/<installation-secret>

# --- Webhooks de entrada ---
# SEM estas, a superfície de webhooks recusa tudo (403). É proposital: aceitar
# evento não verificado seria reabrir o risco S2 por conveniência.
# META_APP_SECRET=
# WEBHOOK_VERIFY_TOKEN=
# EVOLUTION_WEBHOOK_SECRET=

```

## Frozen file: api-app/prisma/migrations/20261015120000_number_onboarding_foundation/migration.sql

Original SHA-256: `55d84f5eef1b9b9e9a22891695812e522fe4e405041341218984507426ef0946`; bytes:6681.

```text
-- Detect ambiguous pre-existing external-resource ownership before inserting
-- durable mappings or enforcing their unique key. Report counts only.
DO $$
DECLARE conflict_count BIGINT;
BEGIN
  SELECT COUNT(*) INTO conflict_count FROM (
    SELECT provider, external_resource_id
    FROM (
      SELECT 'OFICIAL'::text AS provider, phone_number_id AS external_resource_id, bu_id
      FROM bu_channels WHERE phone_number_id IS NOT NULL
      UNION ALL
      SELECT 'NAO_OFICIAL'::text, evolution_instance_name, bu_id
      FROM bu_channels WHERE evolution_instance_name IS NOT NULL
    ) resources
    GROUP BY provider, external_resource_id
    HAVING COUNT(DISTINCT bu_id) > 1
  ) conflicts;
  IF conflict_count > 0 THEN
    RAISE EXCEPTION 'number onboarding migration aborted: % conflicting provider resource ownership groups', conflict_count
      USING ERRCODE = '23505';
  END IF;
END $$;

CREATE TYPE "ChannelRegistrationState" AS ENUM (
  'PENDING_AUTH', 'PENDING_NUMBER', 'REGISTERING', 'PENDING_RECEIPT', 'CONNECTED', 'ERROR', 'CANCELLED'
);
CREATE TYPE "ChannelRegistrationOperation" AS ENUM ('NOVO', 'REAUTORIZAR');

ALTER TABLE "bu_channels"
  ADD COLUMN "generation" INTEGER NOT NULL DEFAULT 1,
  ADD COLUMN "current_attempt_id" TEXT,
  ADD COLUMN "pairing_epoch" INTEGER NOT NULL DEFAULT 0,
  ADD COLUMN "own_number_verified" BOOLEAN NOT NULL DEFAULT false,
  ADD COLUMN "verified_epoch" INTEGER,
  ADD COLUMN "provider_connection_state" TEXT NOT NULL DEFAULT 'PENDING',
  ADD COLUMN "receipt_verified_at" TIMESTAMP(3);

CREATE TABLE "channel_registration_attempts" (
  "id" TEXT NOT NULL,
  "mantenedora_id" TEXT NOT NULL,
  "bu_id" TEXT NOT NULL,
  "channel_id" TEXT,
  "type" "ChannelType" NOT NULL,
  "operation" "ChannelRegistrationOperation" NOT NULL DEFAULT 'NOVO',
  "user_id" TEXT NOT NULL,
  "session_hash" TEXT NOT NULL,
  "nonce_hash" TEXT,
  "idempotency_key" TEXT NOT NULL,
  "request_hash" TEXT NOT NULL,
  "state" "ChannelRegistrationState" NOT NULL DEFAULT 'PENDING_AUTH',
  "version" INTEGER NOT NULL DEFAULT 1,
  "generation" INTEGER NOT NULL DEFAULT 1,
  "pairing_epoch" INTEGER,
  "lease_until" TIMESTAMP(3),
  "expires_at" TIMESTAMP(3) NOT NULL,
  "stage" TEXT NOT NULL DEFAULT 'RESERVED',
  "safe_error_code" TEXT,
  "candidate_key_id" TEXT,
  "candidate_nonce" BYTEA,
  "candidate_ciphertext" BYTEA,
  "candidate_tag" BYTEA,
  "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP(3) NOT NULL,
  CONSTRAINT "channel_registration_attempts_pkey" PRIMARY KEY ("id")
);
CREATE UNIQUE INDEX "channel_registration_attempts_mantenedora_id_idempotency_key_key"
  ON "channel_registration_attempts"("mantenedora_id", "idempotency_key");
CREATE INDEX "channel_registration_attempts_bu_id_type_state_idx"
  ON "channel_registration_attempts"("bu_id", "type", "state");
CREATE INDEX "channel_registration_attempts_state_expires_at_idx"
  ON "channel_registration_attempts"("state", "expires_at");
CREATE UNIQUE INDEX "bu_channels_current_attempt_id_key" ON "bu_channels"("current_attempt_id");
ALTER TABLE "bu_channels" ADD CONSTRAINT "bu_channels_current_attempt_id_fkey"
  FOREIGN KEY ("current_attempt_id") REFERENCES "channel_registration_attempts"("id") ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE "channel_registration_attempts"
  ADD CONSTRAINT "channel_registration_attempts_mantenedora_id_fkey" FOREIGN KEY ("mantenedora_id") REFERENCES "mantenedoras"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT "channel_registration_attempts_bu_id_fkey" FOREIGN KEY ("bu_id") REFERENCES "business_units"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT "channel_registration_attempts_channel_id_fkey" FOREIGN KEY ("channel_id") REFERENCES "bu_channels"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE "channel_credentials" (
  "id" TEXT NOT NULL,
  "channel_id" TEXT NOT NULL,
  "provider" "ChannelType" NOT NULL,
  "bu_id" TEXT NOT NULL,
  "generation" INTEGER NOT NULL,
  "version" INTEGER NOT NULL DEFAULT 1,
  "key_id" TEXT NOT NULL,
  "nonce" BYTEA NOT NULL,
  "ciphertext" BYTEA NOT NULL,
  "tag" BYTEA NOT NULL,
  "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP(3) NOT NULL,
  CONSTRAINT "channel_credentials_pkey" PRIMARY KEY ("id")
);
CREATE UNIQUE INDEX "channel_credentials_channel_id_key" ON "channel_credentials"("channel_id");
CREATE INDEX "channel_credentials_bu_id_provider_idx" ON "channel_credentials"("bu_id", "provider");
ALTER TABLE "channel_credentials"
  ADD CONSTRAINT "channel_credentials_channel_id_fkey" FOREIGN KEY ("channel_id") REFERENCES "bu_channels"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE "provider_resource_identities" (
  "id" TEXT NOT NULL,
  "provider" "ChannelType" NOT NULL,
  "external_resource_id" TEXT NOT NULL,
  "bu_id" TEXT NOT NULL,
  "current_channel_id" TEXT,
  "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "retired_at" TIMESTAMP(3),
  CONSTRAINT "provider_resource_identities_pkey" PRIMARY KEY ("id")
);
CREATE UNIQUE INDEX "provider_resource_identities_provider_external_resource_id_key"
  ON "provider_resource_identities"("provider", "external_resource_id");
CREATE INDEX "provider_resource_identities_bu_id_idx" ON "provider_resource_identities"("bu_id");
ALTER TABLE "provider_resource_identities"
  ADD CONSTRAINT "provider_resource_identities_bu_id_fkey" FOREIGN KEY ("bu_id") REFERENCES "business_units"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT "provider_resource_identities_current_channel_id_fkey" FOREIGN KEY ("current_channel_id") REFERENCES "bu_channels"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- Existing channel mappings have an unambiguous local BU owner once the
-- preflight above passes. No historical Message.external_id is backfilled.
INSERT INTO "provider_resource_identities" ("id", "provider", "external_resource_id", "bu_id", "current_channel_id")
SELECT gen_random_uuid()::text, 'OFICIAL'::"ChannelType", "phone_number_id", "bu_id", "id"
FROM "bu_channels" WHERE "phone_number_id" IS NOT NULL
UNION ALL
SELECT gen_random_uuid()::text, 'NAO_OFICIAL'::"ChannelType", "evolution_instance_name", "bu_id", "id"
FROM "bu_channels" WHERE "evolution_instance_name" IS NOT NULL;

ALTER TABLE "messages" ADD COLUMN "provider_resource_identity_id" TEXT;
CREATE UNIQUE INDEX "messages_provider_resource_identity_id_external_id_key"
  ON "messages"("provider_resource_identity_id", "external_id");
ALTER TABLE "messages"
  ADD CONSTRAINT "messages_provider_resource_identity_id_fkey" FOREIGN KEY ("provider_resource_identity_id") REFERENCES "provider_resource_identities"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

```

## Frozen file: api-app/prisma/migrations/20261015130000_number_onboarding_provider_resource_ownership_immutable/migration.sql

Original SHA-256: `a6fa9ad9e99a0b55ed5d9e86b99d42b603b404c13f41f97ac718e6443f29a3fe`; bytes:880.

```text
-- Provider resource ownership is an append-only identity decision. The current
-- channel attachment may be detached/reattached by an approved same-BU flow;
-- the provider/resource/BU tuple itself can never be transferred or rewritten.
CREATE FUNCTION enforce_provider_resource_identity_immutable_owner()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  IF NEW.provider IS DISTINCT FROM OLD.provider
    OR NEW.external_resource_id IS DISTINCT FROM OLD.external_resource_id
    OR NEW.bu_id IS DISTINCT FROM OLD.bu_id THEN
    RAISE EXCEPTION 'provider resource ownership is immutable'
      USING ERRCODE = '23514';
  END IF;
  RETURN NEW;
END;
$$;

CREATE TRIGGER provider_resource_identity_immutable_owner
BEFORE UPDATE OF provider, external_resource_id, bu_id ON provider_resource_identities
FOR EACH ROW EXECUTE FUNCTION enforce_provider_resource_identity_immutable_owner();

```

## Frozen file: api-app/prisma/migrations/20261015140000_number_onboarding_channel_operation_fence/migration.sql

Original SHA-256: `e484edd01e78133bcaf23f12fb47e44e92cba44a89b29803eff1530b103bc496`; bytes:270.

```text
ALTER TABLE "bu_channels"
  ADD COLUMN "operation_lease_token" TEXT,
  ADD COLUMN "operation_lease_until" TIMESTAMP(3),
  ADD COLUMN "pending_cleanup_instance_name" TEXT;

CREATE INDEX "bu_channels_operation_lease_until_idx"
  ON "bu_channels"("operation_lease_until");

```

## Frozen file: api-app/prisma/schema.prisma

Original SHA-256: `e0701807a0fac3477f327adc60127f76320e8a7681f146b6177bc33546e89a9c`; bytes:26384.

```text
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
  messages Message[]

  @@unique([provider, externalResourceId])
  @@index([buId])
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
  providerResourceIdentityId String? @map("provider_resource_identity_id")
  providerResourceIdentity ProviderResourceIdentity? @relation(fields: [providerResourceIdentityId], references: [id], onDelete: Restrict)
  /// Autoria: FK opcional SetNull + snapshot (ADR-0007). O payload cru NÃO
  /// mora aqui — só no log de webhook, com expurgo (ADR-0009 §7).
  authorUserId String?  @map("author_user_id")
  authorName   String?  @map("author_name")
  createdAt    DateTime @default(now()) @map("created_at")

  @@index([conversationId, createdAt])
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

```

## Frozen file: api-app/src/domain/channels/channel-credential-crypto.spec.ts

Original SHA-256: `bdc829c987de4d8944ce417aea03c76e5484091f7ad4612246807bd22e524efb`; bytes:2354.

```text
import { randomBytes } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { loadChannelCredentialKey, openChannelCredential, sealChannelCredential } from './channel-credential-crypto';
import { redactProviderData } from './safe-redaction';

describe('channel credential envelope', () => {
  const key = randomBytes(32);
  const aad = {
    purpose: 'candidate' as const, provider: 'OFICIAL' as const, buId: 'bu-1',
    channelId: 'channel-1', generation: 4, attemptId: 'attempt-1',
  };

  it('round trips with candidate-bound AAD and a fresh nonce', () => {
    const one = sealChannelCredential('fake-token-fixture', 'test-key-v1', key, aad);
    const two = sealChannelCredential('fake-token-fixture', 'test-key-v1', key, aad);
    expect(one.nonce).not.toEqual(two.nonce);
    expect(openChannelCredential(one, new Map([['test-key-v1', key]]), aad).toString()).toBe('fake-token-fixture');
  });

  it('fails closed for missing keys, tampering, and a different attempt context', () => {
    const envelope = sealChannelCredential('fake-token-fixture', 'test-key-v1', key, aad);
    expect(() => openChannelCredential(envelope, new Map(), aad)).toThrow('unavailable or invalid');
    expect(() => openChannelCredential({ ...envelope, ciphertext: Buffer.from('changed') }, new Map([['test-key-v1', key]]), aad))
      .toThrow('unavailable or invalid');
    expect(() => openChannelCredential(envelope, new Map([['test-key-v1', key]]), { ...aad, attemptId: 'attempt-2' }))
      .toThrow('unavailable or invalid');
  });

  it('loads only an exact 32-byte canonical base64 key under the private config names', () => {
    const encoded = key.toString('base64');
    expect(loadChannelCredentialKey({ CHANNEL_CREDENTIAL_KEY_ID: 'fixture-v1', CHANNEL_CREDENTIAL_KEY: encoded }).key).toEqual(key);
    expect(() => loadChannelCredentialKey({ CHANNEL_CREDENTIAL_KEY_ID: 'fixture-v1', CHANNEL_CREDENTIAL_KEY: 'short' }))
      .toThrow('not configured');
  });

  it('redacts nested provider credentials and secret URL components', () => {
    expect(redactProviderData({ apikey: 'fake-apikey-fixture', nested: { Authorization: 'Bearer fake', callback: 'https://x.test/hook?token=fake' } }))
      .toEqual({ apikey: '[REDACTED]', nested: { Authorization: '[REDACTED]', callback: 'https://x.test/hook?token=[REDACTED]' } });
  });
});

```

## Frozen file: api-app/src/domain/channels/channel-credential-crypto.ts

Original SHA-256: `4a438a1e73903c011d212962f41b38dfb2a999c539112b6831156664de6d9ef4`; bytes:3649.

```text
import { createCipheriv, createDecipheriv, randomBytes } from 'node:crypto';

export type CredentialPurpose = 'candidate' | 'active';

export interface CredentialAad {
  purpose: CredentialPurpose;
  provider: 'OFICIAL' | 'NAO_OFICIAL';
  buId: string;
  channelId: string;
  generation: number;
  attemptId?: string;
  version?: number;
}

export interface CredentialEnvelope {
  keyId: string;
  nonce: Buffer;
  ciphertext: Buffer;
  tag: Buffer;
}

export class CredentialDecryptionError extends Error {
  constructor() {
    super('Channel credential is unavailable or invalid.');
    this.name = 'CredentialDecryptionError';
  }
}

/**
 * Private runtime contract: CHANNEL_CREDENTIAL_KEY_ID and
 * CHANNEL_CREDENTIAL_KEY (canonical base64 for exactly 32 bytes).
 * The caller should load these from private config and never log either value.
 */
export function loadChannelCredentialKey(config: Readonly<Record<string, string | undefined>>): { keyId: string; key: Buffer } {
  const keyId = config.CHANNEL_CREDENTIAL_KEY_ID?.trim();
  const encoded = config.CHANNEL_CREDENTIAL_KEY;
  if (!keyId || !encoded || !/^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(encoded)) {
    throw new Error('Channel credential encryption is not configured.');
  }
  const key = Buffer.from(encoded, 'base64');
  if (key.byteLength !== 32 || key.toString('base64') !== encoded) {
    throw new Error('Channel credential encryption is not configured.');
  }
  return { keyId, key };
}

/** AES-256-GCM; use a dedicated 32-byte key and a fresh 96-bit nonce per seal. */
export function sealChannelCredential(
  plaintext: string | Uint8Array,
  keyId: string,
  key: Uint8Array,
  aad: CredentialAad,
): CredentialEnvelope {
  validateKey(key, keyId);
  const nonce = randomBytes(12);
  const cipher = createCipheriv('aes-256-gcm', key, nonce, { authTagLength: 16 });
  cipher.setAAD(serializeAad(aad));
  const ciphertext = Buffer.concat([cipher.update(plaintext), cipher.final()]);
  return { keyId, nonce, ciphertext, tag: cipher.getAuthTag() };
}

/** Missing keys, wrong AAD and tampering all fail closed with one safe error. */
export function openChannelCredential(
  envelope: CredentialEnvelope,
  keysById: ReadonlyMap<string, Uint8Array>,
  aad: CredentialAad,
): Buffer {
  const key = keysById.get(envelope.keyId);
  try {
    if (!key || key.byteLength !== 32 || envelope.nonce.byteLength !== 12 || envelope.tag.byteLength !== 16) {
      throw new CredentialDecryptionError();
    }
    const decipher = createDecipheriv('aes-256-gcm', key, envelope.nonce, { authTagLength: 16 });
    decipher.setAAD(serializeAad(aad));
    decipher.setAuthTag(envelope.tag);
    return Buffer.concat([decipher.update(envelope.ciphertext), decipher.final()]);
  } catch {
    throw new CredentialDecryptionError();
  }
}

function validateKey(key: Uint8Array, keyId: string): void {
  if (!keyId.trim() || key.byteLength !== 32) throw new Error('Channel credential encryption is not configured.');
}

function serializeAad(aad: CredentialAad): Buffer {
  if (!aad.buId || !aad.channelId || !Number.isSafeInteger(aad.generation)) {
    throw new Error('Invalid channel credential context.');
  }
  if (aad.purpose === 'candidate' && !aad.attemptId) throw new Error('Invalid candidate credential context.');
  if (aad.purpose === 'active' && !Number.isSafeInteger(aad.version)) throw new Error('Invalid active credential context.');
  return Buffer.from([
    'leadshug-channel-credential-v1', aad.purpose, aad.provider, aad.buId,
    aad.channelId, String(aad.generation), aad.attemptId ?? '', String(aad.version ?? ''),
  ].join('\0'));
}

```

## Frozen file: api-app/src/domain/channels/channel-credential-resolver.ts

Original SHA-256: `7a780d39cfdb42cf5bc6a99f89ec7191211dfc4f03a31f6b4c13d3ef2c0e24b3`; bytes:3087.

```text
import { ConflictException, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { loadChannelCredentialKey, openChannelCredential } from './channel-credential-crypto';

export interface ResolvedChannelCredential {
  channelId: string;
  buId: string;
  provider: 'OFICIAL' | 'NAO_OFICIAL';
  generation: number;
  pairingEpoch: number;
  providerResourceIdentityId: string;
  externalResourceId: string;
  accessToken?: string;
  phoneNumberId?: string;
  wabaId?: string;
  evolutionInstanceName?: string;
}

/** Resolves only a currently verified, owned channel and decrypts its own credential. */
@Injectable()
export class ChannelCredentialResolver {
  constructor(private readonly prisma: PrismaService) {}

  async resolve(channelId: string, purpose: 'send' | 'registration' | 'verify' = 'send'): Promise<ResolvedChannelCredential> {
    const channel = await this.prisma.buChannel.findUnique({
      where: { id: channelId }, include: { credential: true, providerIdentities: true },
    });
    if (!channel || (purpose !== 'verify' && (!channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch))) {
      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
    }
    if (purpose === 'send' && (channel.status !== 'CONECTADO' || !channel.receiptVerifiedAt)) {
      throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
    }
    const identity = channel.providerIdentities.find((row) => row.currentChannelId === channel.id);
    if (!identity) throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
    const result: ResolvedChannelCredential = {
      channelId: channel.id, buId: channel.buId, provider: channel.type, generation: channel.generation,
      pairingEpoch: channel.pairingEpoch, providerResourceIdentityId: identity.id,
      externalResourceId: identity.externalResourceId,
      ...(channel.phoneNumberId ? { phoneNumberId: channel.phoneNumberId } : {}),
      ...(channel.wabaId ? { wabaId: channel.wabaId } : {}),
      ...(channel.evolutionInstanceName ? { evolutionInstanceName: channel.evolutionInstanceName } : {}),
    };
    if (channel.type === 'OFICIAL') {
      if (!channel.credential || channel.credential.generation !== channel.generation) {
        throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      }
      const { keyId, key } = loadChannelCredentialKey(process.env);
      if (channel.credential.keyId !== keyId) throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      const plaintext = openChannelCredential({
        ...channel.credential, nonce: Buffer.from(channel.credential.nonce),
        ciphertext: Buffer.from(channel.credential.ciphertext), tag: Buffer.from(channel.credential.tag),
      }, new Map([[keyId, key]]), {
        purpose: 'active', provider: channel.type, buId: channel.buId, channelId: channel.id,
        generation: channel.generation, version: channel.credential.version,
      });
      result.accessToken = plaintext.toString('utf8');
    }
    return result;
  }
}

```

## Frozen file: api-app/src/domain/channels/channels.service.ts

Original SHA-256: `63f679ad3a3ff77c6b763c4ee459973c0e679d13108ead1b29942f465a392e29`; bytes:23356.

```text
import { createHash, randomUUID } from 'node:crypto';
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
import { META_CLIENT, MetaClient } from '../../integrations/meta/meta.client';
import { ChannelCredentialResolver } from './channel-credential-resolver';

export type TipoDeCanal = 'OFICIAL' | 'NAO_OFICIAL';
const OPERATION_LEASE_MS = 45_000;
const ATTEMPT_TTL_MS = 10 * 60_000;

interface PairActor { userId: string; mantenedoraId: string; sessionHash: string; }

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
    private readonly credentials: ChannelCredentialResolver,
  ) {}

  async conectarOficial(buId: string, wabaId: string) {
    void buId; void wabaId;
    throw new ConflictException({ code: 'USE_NUMBER_REGISTRATIONS', message: 'Use o fluxo de onboarding de números.' });
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

  /** POST-only Evolution pairing. Trust is reset in the database before any provider call. */
  async parearNaoOficial(buId: string, intent: 'INITIAL' | 'RENEW', expectedGeneration: number | undefined, revalidate: (() => Promise<void>) | undefined, actor: PairActor) {
    if (!this.evolution.configurado() || !process.env.EVOLUTION_WEBHOOK_URL?.trim()) {
      throw new ServiceUnavailableException({ code: 'EVOLUTION_NOT_CONFIGURED' });
    }
    const leaseToken = randomUUID();
    const reservation = await this.prisma.$transaction(async (tx) => {
      let channel = await tx.buChannel.findUnique({ where: { buId_type: { buId, type: 'NAO_OFICIAL' } } });
      if (intent === 'RENEW' && !channel) throw new ConflictException({ code: 'CHANNEL_AUSENTE' });
      if (!channel) channel = await tx.buChannel.create({ data: { buId, type: 'NAO_OFICIAL', status: 'CONECTANDO' } });
      if (expectedGeneration !== undefined && channel.generation !== expectedGeneration) throw new ConflictException({ code: 'GENERATION_CONFLICT' });
      const now = new Date();
      const lease = await tx.buChannel.updateMany({
        where: { id: channel.id, generation: channel.generation, OR: [{ operationLeaseUntil: null }, { operationLeaseUntil: { lte: now } }] },
        data: { operationLeaseToken: leaseToken, operationLeaseUntil: new Date(now.getTime() + OPERATION_LEASE_MS) },
      });
      if (!lease.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
      const canResume = Boolean(channel.evolutionInstanceName && channel.pairingEpoch > 0
        && channel.providerConnectionState === 'PENDING' && !channel.ownNumberVerified);
      if (intent === 'INITIAL' && channel.evolutionInstanceName && !canResume) throw new ConflictException({ code: 'CHANNEL_SLOT_OCCUPIED' });
      if (intent === 'RENEW' && channel.pendingCleanupInstanceName) throw new ConflictException({ code: 'CLEANUP_RECOVERY_REQUIRED' });
      if (canResume) {
        const identity = await tx.providerResourceIdentity.findFirst({ where: { currentChannelId: channel.id, externalResourceId: channel.evolutionInstanceName! } });
        if (!identity) throw new ConflictException({ code: 'IDENTITY_NOT_MAPPED' });
        if (channel.currentAttemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: channel.currentAttemptId, generation: channel.generation, pairingEpoch: channel.pairingEpoch }, data: { stage: channel.pendingCleanupInstanceName ? 'CLEANUP_AMBIGUOUS' : 'PAIRING', state: channel.pendingCleanupInstanceName ? 'ERROR' : 'PENDING_NUMBER', version: { increment: 1 } } });
        const leased = await tx.buChannel.findUniqueOrThrow({ where: { id: channel.id } });
        return { channel: leased, identityId: identity.id, name: channel.evolutionInstanceName!, generation: channel.generation, epoch: channel.pairingEpoch, resume: true, cleanupName: channel.pendingCleanupInstanceName, leaseToken, attemptId: channel.currentAttemptId };
      }
      await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE current_channel_id = ${channel.id} FOR UPDATE`;
      const oldIdentity = await tx.providerResourceIdentity.findFirst({ where: { currentChannelId: channel.id, provider: 'NAO_OFICIAL' } });
      const oldName = oldIdentity?.externalResourceId ?? null;
      if (oldName && oldName !== channel.evolutionInstanceName) throw new ConflictException({ code: 'IDENTITY_MAPPING_MISMATCH' });
      const epoch = channel.pairingEpoch + 1;
      const generation = intent === 'RENEW' ? channel.generation + 1 : channel.generation;
      const name = `lh-${channel.id.replace(/-/g, '')}-${epoch}`;
      await tx.providerResourceIdentity.updateMany({ where: { currentChannelId: channel.id }, data: { currentChannelId: null, retiredAt: new Date() } });
      const attemptId = randomUUID();
      const attempt = await tx.channelRegistrationAttempt.create({ data: {
        id: attemptId, mantenedoraId: actor.mantenedoraId, buId, channelId: channel.id,
        type: 'NAO_OFICIAL', operation: intent === 'RENEW' ? 'REAUTORIZAR' : 'NOVO', userId: actor.userId,
        sessionHash: actor.sessionHash, idempotencyKey: `evolution:${channel.id}:${epoch}`,
        requestHash: createHash('sha256').update(`${intent}:${channel.id}:${epoch}`).digest('hex'),
        state: 'PENDING_NUMBER', stage: 'PAIRING', generation, pairingEpoch: epoch,
        expiresAt: new Date(Date.now() + ATTEMPT_TTL_MS),
      } });
      const updated = await tx.buChannel.update({
        where: { id: channel.id },
        data: { generation, pairingEpoch: epoch, evolutionInstanceName: name, currentAttemptId: attempt.id, ownNumberVerified: false, verifiedEpoch: null, providerConnectionState: 'PENDING', receiptVerifiedAt: null, connectedAt: null, status: 'CONECTANDO', pendingCleanupInstanceName: oldName },
      });
      const identity = await tx.providerResourceIdentity.create({ data: { provider: 'NAO_OFICIAL', externalResourceId: name, buId, currentChannelId: channel.id } });
      return { channel: updated, identityId: identity.id, name, generation, epoch, resume: false, cleanupName: oldName, leaseToken, attemptId: attempt.id };
    });
    try {
      return await this.completePairing(buId, reservation, revalidate);
    } finally {
      await this.prisma.buChannel.updateMany({
        where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, operationLeaseToken: leaseToken },
        data: { operationLeaseToken: null, operationLeaseUntil: null },
      });
    }
  }

  private async completePairing(
    buId: string,
    reservation: { channel: { id: string }; identityId: string; name: string; generation: number; epoch: number; resume: boolean; cleanupName: string | null; leaseToken: string; attemptId: string | null },
    revalidate?: () => Promise<void>,
  ) {
    if (reservation.cleanupName) {
      try {
        const prior = await this.evolution.consultarInstancia(reservation.cleanupName);
        await revalidate?.();
        if (prior?.name === reservation.cleanupName) {
          await this.evolution.apagarInstancia(reservation.cleanupName);
          await revalidate?.();
        }
      } catch {
        if (reservation.attemptId) await this.prisma.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'CLEANUP_AMBIGUOUS', safeErrorCode: 'CLEANUP_AMBIGUOUS', version: { increment: 1 } } });
        return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CLEANUP_AMBIGUOUS', qrcode: null };
      }
      await this.prisma.buChannel.updateMany({
        where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, operationLeaseToken: reservation.leaseToken, pendingCleanupInstanceName: reservation.cleanupName },
        data: { pendingCleanupInstanceName: null },
      });
      return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CLEANUP_COMPLETED_RETRY_PAIR', qrcode: null };
    }
    let created: { qrcode: string | null };
    let observed = reservation.resume ? await this.evolution.consultarInstancia(reservation.name).catch(() => null) : null;
    if (reservation.resume) await revalidate?.();
    if (reservation.resume && !observed) {
      if (reservation.attemptId) await this.prisma.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'CREATE_AMBIGUOUS', safeErrorCode: 'CREATE_AMBIGUOUS', version: { increment: 1 } } });
      return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CREATE_AMBIGUOUS', qrcode: null };
    }
    if (!reservation.resume) {
      try {
        created = await this.evolution.criarInstancia(reservation.name);
      } catch {
        await revalidate?.();
        observed = await this.evolution.consultarInstancia(reservation.name).catch(() => null);
        await revalidate?.();
        if (!observed) {
          if (reservation.attemptId) await this.prisma.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'CREATE_AMBIGUOUS', safeErrorCode: 'CREATE_AMBIGUOUS', version: { increment: 1 } } });
          return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CREATE_AMBIGUOUS', qrcode: null };
        }
        created = { qrcode: null };
      }
      await revalidate?.();
    } else created = { qrcode: null };
    let qr = created.qrcode;
    if (!qr) { qr = await this.evolution.qrDaInstancia(reservation.name).catch(() => null); await revalidate?.(); }
    if (!observed) { observed = await this.evolution.consultarInstancia(reservation.name).catch(() => null); await revalidate?.(); }
    if (observed?.name !== reservation.name) observed = null;
    if (observed?.connectionStatus?.toLowerCase() === 'open' && observed.ownerJid) {
      const ownerPhone = parseEvolutionOwnerPhone(observed.ownerJid);
      const bu = await this.prisma.businessUnit.findUniqueOrThrow({ where: { id: buId }, select: { phone: true } });
      await revalidate?.();
      if (!ownerPhone || (bu.phone && ownerPhone !== bu.phone)) {
        await this.prisma.$transaction(async (tx) => {
          await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${reservation.identityId} FOR UPDATE`;
          await tx.buChannel.updateMany({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { providerConnectionState: 'IDENTITY_QUARANTINED' } });
          if (reservation.attemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'IDENTITY_QUARANTINED', safeErrorCode: 'IDENTITY_QUARANTINED', version: { increment: 1 } } });
        });
        throw new ConflictException({ code: 'IDENTITY_QUARANTINED' });
      }
      await this.prisma.$transaction(async (tx) => {
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${reservation.identityId} AND current_channel_id = ${reservation.channel.id} FOR UPDATE`;
        const current = await tx.buChannel.findFirst({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch }, select: { receiptVerifiedAt: true, currentAttemptId: true } });
        await tx.buChannel.updateMany({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { ownNumberVerified: true, verifiedEpoch: reservation.epoch, providerConnectionState: 'CONNECTED', ...(current?.receiptVerifiedAt ? { status: 'CONECTADO', connectedAt: new Date() } : {}) } });
        if (current?.currentAttemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: current.currentAttemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: { in: ['PENDING_NUMBER', 'PENDING_RECEIPT'] } }, data: { state: current.receiptVerifiedAt ? 'CONNECTED' : 'PENDING_RECEIPT', stage: current.receiptVerifiedAt ? 'RECEIPT_VERIFIED' : 'MAPPED_PENDING_RECEIPT', version: { increment: 1 } } });
        if (!bu.phone) await tx.businessUnit.updateMany({ where: { id: buId, phone: null }, data: { phone: ownerPhone } });
      });
    }
    return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: observed?.connectionStatus?.toLowerCase() === 'open' ? 'PENDING_RECEIPT' : 'PENDING_IDENTITY', qrcode: qr };
  }

  async verificar(buId: string, tipo: TipoDeCanal, revalidate?: () => Promise<void>) {
    const channel = await this.prisma.buChannel.findUnique({ where: { buId_type: { buId, type: tipo } } });
    if (!channel) throw new ConflictException({ code: 'CHANNEL_AUSENTE' });
    const leaseToken = randomUUID();
    const now = new Date();
    const lease = await this.prisma.buChannel.updateMany({
      where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, OR: [{ operationLeaseUntil: null }, { operationLeaseUntil: { lte: now } }] },
      data: { operationLeaseToken: leaseToken, operationLeaseUntil: new Date(now.getTime() + OPERATION_LEASE_MS) },
    });
    if (!lease.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
    try {
    const identity = await this.prisma.providerResourceIdentity.findFirst({ where: { currentChannelId: channel.id, provider: tipo } });
    if (!identity) throw new ConflictException({ code: 'IDENTITY_NOT_MAPPED' });
    let verifiedPhone: string | null = null;
    let connectionOpen = false;
    if (tipo === 'OFICIAL') {
      if (!channel.wabaId || !channel.phoneNumberId) throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
      const credential = await this.credentials.resolve(channel.id, 'verify');
      if (!credential.accessToken) throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      const number = await this.meta.confirmarNumero(channel.wabaId, channel.phoneNumberId, credential.accessToken);
      await revalidate?.();
      if (!number) throw new ConflictException({ code: 'PROVIDER_RESOURCE_NOT_FOUND' });
      verifiedPhone = number.telefone;
    } else {
      if (!channel.evolutionInstanceName) throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
      const observed = await this.evolution.consultarInstancia(channel.evolutionInstanceName);
      await revalidate?.();
      if (!observed || observed.name !== identity.externalResourceId) throw new ConflictException({ code: 'PROVIDER_RESOURCE_NOT_FOUND' });
      const ownerPhone = observed.ownerJid ? parseEvolutionOwnerPhone(observed.ownerJid) : null;
      connectionOpen = observed.connectionStatus?.toLowerCase() === 'open';
      if (!ownerPhone || !connectionOpen) throw new ConflictException({ code: 'PENDING_IDENTITY' });
      verifiedPhone = ownerPhone;
    }
    const bu = await this.prisma.businessUnit.findUniqueOrThrow({ where: { id: buId }, select: { phone: true } });
    await revalidate?.();
    if (bu.phone && verifiedPhone && bu.phone !== verifiedPhone) {
      await this.prisma.$transaction(async (tx) => {
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${identity.id} FOR UPDATE`;
        await tx.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken }, data: { ownNumberVerified: false, verifiedEpoch: null, providerConnectionState: 'IDENTITY_QUARANTINED' } });
      });
      throw new ConflictException({ code: 'IDENTITY_QUARANTINED' });
    }
    await this.prisma.$transaction(async (tx) => {
      const locked = await tx.$queryRaw<Array<{ id: string }>>`SELECT id FROM provider_resource_identities WHERE id = ${identity.id} AND current_channel_id = ${channel.id} FOR UPDATE`;
      if (!locked.length) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
      const updated = await tx.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken }, data: { ownNumberVerified: true, verifiedEpoch: channel.pairingEpoch, providerConnectionState: tipo === 'NAO_OFICIAL' ? 'CONNECTED' : channel.providerConnectionState === 'SUBSCRIBED' ? 'SUBSCRIBED' : 'VERIFIED' } });
      if (!updated.count) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
      if (!bu.phone && verifiedPhone) await tx.businessUnit.updateMany({ where: { id: buId, phone: null }, data: { phone: verifiedPhone } });
      if (channel.receiptVerifiedAt && (tipo === 'NAO_OFICIAL' || channel.providerConnectionState === 'SUBSCRIBED')) {
        await tx.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken }, data: { status: 'CONECTADO', connectedAt: new Date() } });
        if (channel.currentAttemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: channel.currentAttemptId, generation: channel.generation, pairingEpoch: channel.pairingEpoch, state: { in: ['PENDING_NUMBER', 'PENDING_RECEIPT'] } }, data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', version: { increment: 1 } } });
      }
    });
    return { status: connectionOpen ? 'PENDING_RECEIPT' : 'IDENTITY_VERIFIED', ownNumberVerified: true, receiptVerified: Boolean(channel.receiptVerifiedAt) };
    } finally {
      await this.prisma.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken }, data: { operationLeaseToken: null, operationLeaseUntil: null } });
    }
  }

  async desconectar(buId: string, tipo: TipoDeCanal) {
    const canal = await this.prisma.buChannel.findUnique({ where: { buId_type: { buId, type: tipo } } });
    if (!canal) return false;

    await this.prisma.$transaction(async (tx) => {
      const current = await tx.buChannel.findUnique({ where: { id: canal.id }, select: { operationLeaseUntil: true, generation: true } });
      if (!current) return;
      if (current.operationLeaseUntil && current.operationLeaseUntil > new Date()) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
      await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE current_channel_id = ${canal.id} FOR UPDATE`;
      await tx.providerResourceIdentity.updateMany({ where: { currentChannelId: canal.id }, data: { currentChannelId: null, retiredAt: new Date() } });
      await tx.channelRegistrationAttempt.updateMany({ where: { channelId: canal.id }, data: { channelId: null } });
      await tx.channelCredential.deleteMany({ where: { channelId: canal.id } });
      await tx.buChannel.delete({ where: { id: canal.id } });
    });
    // External cleanup follows the local fence. A late event can no longer
    // pass the same identity row lock even if provider deletion times out.
    if (tipo === 'NAO_OFICIAL' && canal.evolutionInstanceName && this.evolution.configurado()) {
      await this.evolution.apagarInstancia(canal.evolutionInstanceName).catch(() => undefined);
    }
    return true;
  }

  private async exigirCanalLivre(buId: string, tipo: TipoDeCanal): Promise<void> {
    const existente = await this.prisma.buChannel.findUnique({ where: { buId_type: { buId, type: tipo } } });
    if (existente) {
      throw new ConflictException({ error: 'Esta BU já tem um canal desse tipo.', code: 'CANAL_JA_EXISTE' });
    }
  }
}

function parseEvolutionOwnerPhone(ownerJid: string): string | null {
  if (!ownerJid.endsWith('@s.whatsapp.net')) return null;
  const local = ownerJid.split('@')[0].split(':')[0];
  return /^\d{8,15}$/.test(local) ? local : null;
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

```

## Frozen file: api-app/src/domain/channels/number-registration.service.ts

Original SHA-256: `4f24fc7cf518685e61d42c300332df9dd64b140f9eeef57901e91ba6a5ff04f4`; bytes:36044.

```text
import { createHash, createHmac, randomBytes, timingSafeEqual } from 'node:crypto';
import { BadRequestException, ConflictException, ForbiddenException, Injectable, NotFoundException, ServiceUnavailableException } from '@nestjs/common';
import { ChannelRegistrationAttempt, ChannelRegistrationOperation, ChannelRegistrationState, ChannelType } from '@prisma/client';
import { AccessService } from '../access/access.service';
import { exigirPapelNaBu } from '../access/require-role';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { META_CLIENT, MetaClient } from '../../integrations/meta/meta.client';
import { Inject } from '@nestjs/common';
import { sealChannelCredential, loadChannelCredentialKey, openChannelCredential } from './channel-credential-crypto';
import { ChannelCredentialResolver } from './channel-credential-resolver';
import { TenancyService } from '../tenancy/tenancy.service';
import { ModulosService } from '../produto/modulos.service';
import { atLeast } from '../access/role';
import { SessionService } from '../../infra/session/session.service';

const SAFE = /^[A-Za-z0-9_-]{1,128}$/;
const ATTEMPT_TTL_MS = 10 * 60_000;
const LEASE_MS = 45_000;

export interface RegistrationActor { id: string; mantenedoraId: string; nome: string; email: string; sessionToken: string; }
export interface CreateRegistrationInput {
  buId?: string;
  novaBu?: { nome: string; setorId?: string };
  tipo: 'OFICIAL' | 'NAO_OFICIAL';
  operation: 'NOVO' | 'REAUTORIZAR';
  channelId?: string;
  expectedGeneration?: number;
}

/** State machine for bounded number registration and credential promotion. */
@Injectable()
export class NumberRegistrationService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly access: AccessService,
    @Inject(META_CLIENT) private readonly meta: MetaClient,
    private readonly credentials: ChannelCredentialResolver,
    private readonly tenancy: TenancyService,
    private readonly modulos: ModulosService,
    private readonly sessions: SessionService,
  ) {}

  async capabilities(mantenedoraId: string) {
    const meta = this.meta.capabilities();
    const evolutionAvailable = Boolean(process.env.EVOLUTION_API_URL?.trim() && process.env.EVOLUTION_API_KEY?.trim() && process.env.EVOLUTION_WEBHOOK_URL?.trim());
    const cryptoAvailable = (() => { try { loadChannelCredentialKey(process.env); return true; } catch { return false; } })();
    const product = await this.modulos.produto(mantenedoraId);
    const moduleAvailable = product.modulos.canalNaoOficial;
    return {
      oficial: { ...meta, available: meta.available && cryptoAvailable, reason: meta.available ? (cryptoAvailable ? 'AVAILABLE' : 'CREDENTIAL_ENCRYPTION_UNAVAILABLE') : meta.reason },
      naoOficial: { available: evolutionAvailable && moduleAvailable, reason: !evolutionAvailable ? 'NOT_CONFIGURED' : moduleAvailable ? 'AVAILABLE' : 'MODULE_NOT_CONTRACTED' },
    };
  }

  async authorizeCreateScope(actor: RegistrationActor, body: unknown) {
    if (body && typeof body === 'object' && !Array.isArray(body)) {
      const data = body as Record<string, unknown>;
      if (typeof data.buId === 'string') await this.requireAdmin(actor.id, data.buId);
      else {
        const role = await this.access.papelNaMantenedoraDoUsuario(actor.id, actor.mantenedoraId);
        if (!role || !atLeast(role, 'ADMIN')) throw new ForbiddenException({ code: 'TENANT_ADMIN_REQUIRED' });
      }
    } else {
      const role = await this.access.papelNaMantenedoraDoUsuario(actor.id, actor.mantenedoraId);
      if (!role || !atLeast(role, 'ADMIN')) throw new ForbiddenException({ code: 'TENANT_ADMIN_REQUIRED' });
    }
  }

  async create(actor: RegistrationActor, sessionHash: string, key: string, input: CreateRegistrationInput) {
    if (!SAFE.test(key) || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(key)) throw new BadRequestException({ code: 'IDEMPOTENCY_KEY_INVALID' });
    if ((Boolean(input.buId) === Boolean(input.novaBu)) || !['OFICIAL', 'NAO_OFICIAL'].includes(input.tipo)
      || !['NOVO', 'REAUTORIZAR'].includes(input.operation)) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    if (input.novaBu && (input.operation !== 'NOVO' || !input.novaBu.nome?.trim() || input.channelId || input.expectedGeneration !== undefined)) {
      throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    }
    const capabilities = await this.capabilities(actor.mantenedoraId);
    const capability = input.tipo === 'OFICIAL' ? capabilities.oficial : capabilities.naoOficial;
    if (!capability.available) throw new ServiceUnavailableException({ code: capability.reason, error: 'Este canal não está configurado nesta instalação.' });
    if (input.tipo === 'NAO_OFICIAL') await this.modulos.exigir(actor.mantenedoraId, 'canalNaoOficial');
    if (input.novaBu) {
      const tenantRole = await this.access.papelNaMantenedoraDoUsuario(actor.id, actor.mantenedoraId);
      if (!tenantRole || !atLeast(tenantRole, 'ADMIN')) throw new ForbiddenException({ code: 'TENANT_ADMIN_REQUIRED' });
    }
    const payloadHash = hash(JSON.stringify({ ...input, novaBu: input.novaBu ? { ...input.novaBu, nome: input.novaBu.nome.trim() } : undefined }));
    const sessionDigest = hash(actor.sessionToken);
    const now = new Date();
    const prior = await this.prisma.channelRegistrationAttempt.findUnique({ where: { mantenedoraId_idempotencyKey: { mantenedoraId: actor.mantenedoraId, idempotencyKey: key } } });
    if (prior) {
      return this.replayCreate(actor, prior, payloadHash, sessionDigest);
    }
    if (input.buId) await this.requireAdmin(actor.id, input.buId);
    const attemptId = cryptoRandomId();
    const nonce = nonceForAttempt(actor.sessionToken, attemptId);
    let attempt: ChannelRegistrationAttempt;
    try {
    attempt = await this.prisma.$transaction(async (tx) => {
      const buId = input.buId ?? (input.novaBu ? (await this.tenancy.criarBusinessUnitNaTransacao(tx, actor.mantenedoraId, input.novaBu.nome, input.novaBu.setorId, { id: actor.id, nome: actor.nome, email: actor.email })).bu.id : null);
      if (!buId) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
      const bu = await tx.businessUnit.findFirst({ where: { id: buId, mantenedoraId: actor.mantenedoraId }, select: { id: true } });
      if (!bu) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
      let channelId: string;
      let generation = 1;
      if (input.operation === 'REAUTORIZAR') {
        if (!input.channelId || !Number.isSafeInteger(input.expectedGeneration)) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
        const channel = await tx.buChannel.findFirst({ where: { id: input.channelId, buId, type: input.tipo } });
        if (!channel) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
        if (channel.generation !== input.expectedGeneration) throw new ConflictException({ code: 'GENERATION_CONFLICT' });
        if (channel.operationLeaseUntil && channel.operationLeaseUntil > new Date()) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
        channelId = channel.id; generation = channel.generation;
      } else {
        const existing = await tx.buChannel.findUnique({ where: { buId_type: { buId, type: input.tipo } } });
        if (existing) throw new ConflictException({ code: 'CHANNEL_SLOT_OCCUPIED' });
        const channel = await tx.buChannel.create({ data: { buId, type: input.tipo, status: input.tipo === 'OFICIAL' ? 'CONECTANDO' : 'DESCONECTADO' } });
        channelId = channel.id;
      }
      const row = await tx.channelRegistrationAttempt.create({ data: {
        id: attemptId, mantenedoraId: actor.mantenedoraId, buId, channelId,
        type: input.tipo, operation: input.operation as ChannelRegistrationOperation, userId: actor.id,
        sessionHash: sessionDigest, nonceHash: hash(nonce), idempotencyKey: key, requestHash: payloadHash,
        state: input.tipo === 'OFICIAL' ? 'PENDING_AUTH' : 'PENDING_NUMBER', generation,
        expiresAt: new Date(now.getTime() + ATTEMPT_TTL_MS), stage: 'RESERVED',
      } });
      if (channelId) {
        const current = input.operation === 'REAUTORIZAR'
          ? await tx.buChannel.findUniqueOrThrow({ where: { id: channelId }, select: { generation: true, currentAttemptId: true } })
          : { generation, currentAttemptId: null };
        const claimed = await tx.buChannel.updateMany({
          where: { id: channelId, generation: current.generation, currentAttemptId: current.currentAttemptId, OR: [{ operationLeaseUntil: null }, { operationLeaseUntil: { lte: new Date() } }] },
          data: { currentAttemptId: row.id },
        });
        if (!claimed.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
      }
      return row;
    });
    } catch (error) {
      if (!error || typeof error !== 'object' || !('code' in error) || error.code !== 'P2002') throw error;
      const committed = await this.prisma.channelRegistrationAttempt.findUnique({ where: { mantenedoraId_idempotencyKey: { mantenedoraId: actor.mantenedoraId, idempotencyKey: key } } });
      if (committed) return this.replayCreate(actor, committed, payloadHash, sessionDigest);
      if (input.buId) {
        const occupied = await this.prisma.buChannel.findUnique({ where: { buId_type: { buId: input.buId, type: input.tipo } } });
        if (occupied) throw new ConflictException({ code: 'CHANNEL_SLOT_OCCUPIED' });
      }
      throw error;
    }
    return { attempt: this.dto(attempt), nonce, replay: false };
  }

  private async replayCreate(actor: RegistrationActor, prior: { id: string; requestHash: string; buId: string; userId: string; sessionHash: string; state: ChannelRegistrationState; expiresAt: Date; nonceHash: string | null; version: number; type: ChannelType; operation: ChannelRegistrationOperation; channelId: string | null; stage: string; safeErrorCode: string | null; generation: number }, payloadHash: string, sessionDigest: string) {
    if (prior.requestHash !== payloadHash) throw new ConflictException({ code: 'IDEMPOTENCY_CONFLICT' });
    await this.requireAdmin(actor.id, prior.buId);
    if (prior.userId !== actor.id || !constantTime(prior.sessionHash, sessionDigest)) throw new ConflictException({ code: 'ATTEMPT_SESSION_MISMATCH' });
    if (prior.state === 'PENDING_AUTH' && prior.expiresAt > new Date() && prior.nonceHash) {
      const nonce = nonceForAttempt(actor.sessionToken, prior.id);
      if (constantTime(prior.nonceHash, hash(nonce))) return { attempt: this.dto(prior), nonce, replay: true };
    }
    return { attempt: this.dto(prior), nonce: null, replay: true };
  }

  async get(actor: RegistrationActor, id: string) {
    const attempt = await this.prisma.channelRegistrationAttempt.findFirst({ where: { id, mantenedoraId: actor.mantenedoraId } });
    if (!attempt) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    await this.requireAdmin(actor.id, attempt.buId);
    await this.assertActorSession(actor);
    if (attempt.channelId && !await this.prisma.buChannel.findFirst({ where: { id: attempt.channelId, currentAttemptId: id, generation: attempt.generation } })) throw new ConflictException({ code: 'ATTEMPT_STALE' });
    return this.dto(attempt);
  }

  async authorize(actor: RegistrationActor, id: string, sessionHash: string, nonce: string, code: string) {
    const attempt = await this.requireCurrent(actor, id, sessionHash);
    if (attempt.type !== 'OFICIAL' || attempt.state !== 'PENDING_AUTH' || attempt.expiresAt <= new Date()
      || !attempt.nonceHash || hash(nonce) !== attempt.nonceHash) throw new ConflictException({ code: 'AUTHORIZATION_EXPIRED_OR_USED' });
    const leaseToken = await this.acquireChannelLease(attempt);
    try {
      const claimed = await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, version: attempt.version, state: 'PENDING_AUTH', nonceHash: attempt.nonceHash }, data: { state: 'PENDING_NUMBER', stage: 'CODE_CONSUMED', nonceHash: null, version: { increment: 1 } } });
      if (!claimed.count) throw new ConflictException({ code: 'AUTHORIZATION_REPLAYED' });
      try {
      const exchanged = await this.meta.exchangeCode(code);
      const afterExchange = await this.requireCurrent(actor, id);
      if (afterExchange.version !== attempt.version + 1 || afterExchange.stage !== 'CODE_CONSUMED') throw new ConflictException({ code: 'ATTEMPT_STALE' });
      const key = loadChannelCredentialKey(process.env);
      const envelope = sealChannelCredential(exchanged.accessToken, key.keyId, key.key, {
        purpose: 'candidate', provider: 'OFICIAL', buId: attempt.buId, channelId: attempt.channelId!, generation: attempt.generation, attemptId: attempt.id,
      });
      const updated = await this.prisma.channelRegistrationAttempt.updateMany({
        where: { id, state: 'PENDING_NUMBER', stage: 'CODE_CONSUMED', version: attempt.version + 1, expiresAt: { gt: new Date() } },
        data: { candidateKeyId: envelope.keyId, candidateNonce: dbBytes(envelope.nonce), candidateCiphertext: dbBytes(envelope.ciphertext), candidateTag: dbBytes(envelope.tag), stage: 'AUTHORIZED', version: { increment: 1 } },
      });
      if (!updated.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
      return this.get(actor, id);
    } catch {
      await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, stage: 'CODE_CONSUMED' }, data: { state: 'ERROR', stage: 'AMBIGUOUS_CODE_EXCHANGE', safeErrorCode: 'AUTHORIZATION_AMBIGUOUS', version: { increment: 1 } } });
      throw new ConflictException({ code: 'AUTHORIZATION_AMBIGUOUS' });
      }
    } finally {
      await this.releaseChannelLease(attempt, leaseToken);
    }
  }

  async options(actor: RegistrationActor, id: string, wabaId?: string, after?: string) {
    const attempt = await this.requireCurrent(actor, id);
    if (attempt.state !== 'PENDING_NUMBER' || attempt.stage !== 'AUTHORIZED' || !attempt.candidateCiphertext) throw new ConflictException({ code: 'AUTHORIZATION_REQUIRED' });
    const leaseToken = await this.acquireChannelLease(attempt);
    try {
      const token = this.openCandidate(attempt);
      const result = await this.meta.recursos(token, wabaId, after);
      const fresh = await this.requireCurrent(actor, id);
      if (fresh.version !== attempt.version || fresh.stage !== 'AUTHORIZED' || fresh.state !== 'PENDING_NUMBER') throw new ConflictException({ code: 'ATTEMPT_STALE' });
      return result;
    } finally { await this.releaseChannelLease(attempt, leaseToken); }
  }

  async confirm(actor: RegistrationActor, id: string, body: { wabaId: string; phoneNumberId: string; modoRegistro: 'NOVO' | 'JA_REGISTRADO'; pin?: string; after?: string }) {
    const attempt = await this.requireCurrent(actor, id);
    if (attempt.type !== 'OFICIAL' || attempt.state !== 'PENDING_NUMBER' || attempt.stage !== 'AUTHORIZED'
      || !/^\d{5,}$/.test(body.wabaId) || !/^\d{5,}$/.test(body.phoneNumberId)
      || !['NOVO', 'JA_REGISTRADO'].includes(body.modoRegistro) || (body.modoRegistro === 'NOVO' && !/^\d{6}$/.test(body.pin ?? ''))
      || (body.modoRegistro === 'JA_REGISTRADO' && body.pin !== undefined)
      || (body.after !== undefined && (typeof body.after !== 'string' || body.after.length < 1 || body.after.length > 512))) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    const leaseToken = await this.acquireChannelLease(attempt);
    try {
    const token = this.openCandidate(attempt);
    const activeBefore = attempt.channelId ? await this.prisma.channelCredential.findUnique({ where: { channelId: attempt.channelId }, select: { version: true } }) : null;
    const number = await this.meta.confirmarNumero(body.wabaId, body.phoneNumberId, token, body.after);
    if (!number) throw new ConflictException({ code: 'PROVIDER_RESOURCE_NOT_FOUND' });
    const afterLookup = await this.requireCurrent(actor, id);
    if (afterLookup.version !== attempt.version || afterLookup.stage !== 'AUTHORIZED' || afterLookup.state !== 'PENDING_NUMBER') throw new ConflictException({ code: 'ATTEMPT_STALE' });
    const priorOwner = await this.prisma.providerResourceIdentity.findUnique({
      where: { provider_externalResourceId: { provider: 'OFICIAL', externalResourceId: body.phoneNumberId } },
      select: { buId: true, currentChannelId: true },
    });
    if (priorOwner && (priorOwner.buId !== attempt.buId || (priorOwner.currentChannelId && priorOwner.currentChannelId !== attempt.channelId))) {
      throw new ConflictException({ code: 'RESOURCE_OWNED' });
    }
    const existingBu = await this.prisma.businessUnit.findUniqueOrThrow({ where: { id: attempt.buId }, select: { phone: true } });
    if (!number.telefone || (existingBu.phone && existingBu.phone !== number.telefone)) throw new ConflictException({ code: 'PHONE_MISMATCH' });
    // Reserve immutable BU ownership before any provider-side register call.
    // The unique provider/resource key arbitrates concurrent BUs; this short
    // transaction contains no network operation and does not activate trust.
    if (attempt.channelId) {
      try {
        await this.prisma.$transaction(async (tx) => {
          const owner = await tx.providerResourceIdentity.findUnique({
            where: { provider_externalResourceId: { provider: 'OFICIAL', externalResourceId: body.phoneNumberId } },
          });
          if (owner && (owner.buId !== attempt.buId || (owner.currentChannelId && owner.currentChannelId !== attempt.channelId))) {
            throw new ConflictException({ code: 'RESOURCE_OWNED' });
          }
          if (owner) {
            const claimed = await tx.providerResourceIdentity.updateMany({
              where: { id: owner.id, buId: attempt.buId, OR: [{ currentChannelId: null }, { currentChannelId: attempt.channelId }] },
              data: { currentChannelId: attempt.channelId, retiredAt: null },
            });
            if (!claimed.count) throw new ConflictException({ code: 'RESOURCE_OWNED' });
          } else {
            await tx.providerResourceIdentity.create({ data: {
              provider: 'OFICIAL', externalResourceId: body.phoneNumberId, buId: attempt.buId,
              currentChannelId: attempt.channelId,
            } });
          }
        });
      } catch (error) {
        if (error instanceof ConflictException) throw error;
        if (error && typeof error === 'object' && 'code' in error && error.code === 'P2002') {
          throw new ConflictException({ code: 'RESOURCE_OWNED' });
        }
        throw error;
      }
    }
    if (body.modoRegistro === 'NOVO') {
      const beforeRegister = await this.requireCurrent(actor, id);
      if (beforeRegister.version !== attempt.version || beforeRegister.stage !== 'AUTHORIZED' || beforeRegister.state !== 'PENDING_NUMBER') throw new ConflictException({ code: 'ATTEMPT_STALE' });
      const started = await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, version: attempt.version, state: 'PENDING_NUMBER', stage: 'AUTHORIZED' }, data: { stage: 'REGISTERING', version: { increment: 1 } } });
      if (!started.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
      try {
        await this.meta.registrarNumero(body.phoneNumberId, body.pin!, token);
        const afterRegistration = await this.requireCurrent(actor, id);
        if (afterRegistration.version !== attempt.version + 1 || afterRegistration.stage !== 'REGISTERING') throw new ConflictException({ code: 'ATTEMPT_STALE' });
        await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, stage: 'REGISTERING', version: attempt.version + 1 }, data: { stage: 'AUTHORIZED', version: { increment: 1 } } });
      } catch {
        await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, stage: 'REGISTERING' }, data: { state: 'ERROR', stage: 'REGISTER_AMBIGUOUS', safeErrorCode: 'REGISTRATION_AMBIGUOUS', version: { increment: 1 } } });
        throw new ConflictException({ code: 'REGISTRATION_AMBIGUOUS' });
      }
    }
    const freshAttempt = await this.requireCurrent(actor, id);
    if (freshAttempt.sessionHash !== attempt.sessionHash || freshAttempt.stage !== 'AUTHORIZED') throw new ConflictException({ code: 'ATTEMPT_STALE' });
    await this.prisma.$transaction(async (tx) => {
      const current = await tx.channelRegistrationAttempt.findUniqueOrThrow({ where: { id } });
      if (current.version !== freshAttempt.version || current.state !== 'PENDING_NUMBER' || current.stage !== 'AUTHORIZED' || current.expiresAt <= new Date()) throw new ConflictException({ code: 'ATTEMPT_STALE' });
      const channel = await tx.buChannel.findFirst({ where: { id: current.channelId!, currentAttemptId: id, generation: current.generation } });
      if (!channel) throw new ConflictException({ code: 'ATTEMPT_STALE' });
      const nextGeneration = channel.generation + (current.operation === 'REAUTORIZAR' ? 1 : 0);
      const key = loadChannelCredentialKey(process.env);
      const plaintext = this.openCandidate(current);
      const version = (await tx.channelCredential.findUnique({ where: { channelId: channel.id }, select: { version: true } }))?.version ?? 0;
      if (version !== (activeBefore?.version ?? 0)) throw new ConflictException({ code: 'ACTIVE_CREDENTIAL_CHANGED' });
      const envelope = sealChannelCredential(plaintext, key.keyId, key.key, {
        purpose: 'active', provider: 'OFICIAL', buId: current.buId, channelId: channel.id, generation: nextGeneration, version: version + 1,
      });
      const owner = await tx.providerResourceIdentity.findUnique({ where: { provider_externalResourceId: { provider: 'OFICIAL', externalResourceId: body.phoneNumberId } } });
      if (owner && (owner.buId !== current.buId || (owner.currentChannelId && owner.currentChannelId !== channel.id))) throw new ConflictException({ code: 'RESOURCE_OWNED' });
      const mapping = owner ?? await tx.providerResourceIdentity.create({ data: { provider: 'OFICIAL', externalResourceId: body.phoneNumberId, buId: current.buId, currentChannelId: channel.id } });
      await tx.providerResourceIdentity.updateMany({ where: { currentChannelId: channel.id, id: { not: mapping.id } }, data: { currentChannelId: null, retiredAt: new Date() } });
      await tx.providerResourceIdentity.update({ where: { id: mapping.id }, data: { currentChannelId: channel.id, retiredAt: null } });
      await tx.buChannel.update({ where: { id: channel.id }, data: { generation: nextGeneration, wabaId: body.wabaId, phoneNumberId: body.phoneNumberId, ownNumberVerified: true, verifiedEpoch: channel.pairingEpoch, providerConnectionState: 'PENDING', receiptVerifiedAt: null, connectedAt: null, status: 'CONECTANDO', requiresWindow: true } });
      await tx.channelCredential.upsert({ where: { channelId: channel.id }, create: { channelId: channel.id, provider: 'OFICIAL', buId: current.buId, generation: nextGeneration, version: version + 1, keyId: envelope.keyId, nonce: dbBytes(envelope.nonce), ciphertext: dbBytes(envelope.ciphertext), tag: dbBytes(envelope.tag) }, update: { generation: nextGeneration, version: version + 1, keyId: envelope.keyId, nonce: dbBytes(envelope.nonce), ciphertext: dbBytes(envelope.ciphertext), tag: dbBytes(envelope.tag) } });
      if (!existingBu.phone && number.telefone) await tx.businessUnit.updateMany({ where: { id: current.buId, phone: null }, data: { phone: number.telefone } });
      await tx.channelRegistrationAttempt.update({ where: { id }, data: { generation: nextGeneration, state: 'PENDING_RECEIPT', stage: body.modoRegistro === 'NOVO' ? 'REGISTERED_PENDING_RECEIPT' : 'MAPPED_PENDING_RECEIPT', candidateKeyId: null, candidateNonce: null, candidateCiphertext: null, candidateTag: null, version: { increment: 1 } } });
    });
    return { registration: await this.get(actor, id) };
    } finally { await this.releaseChannelLease(attempt, leaseToken); }
  }

  async advance(actor: RegistrationActor, id: string) { return this.runAdvance(actor, id); }
  async retry(actor: RegistrationActor, id: string) {
    const attempt = await this.requireCurrent(actor, id, undefined, true);
    if (attempt.stage.endsWith('_AMBIGUOUS') || attempt.stage === 'SUBSCRIBING') throw new ConflictException({ code: 'MANUAL_RECOVERY_REQUIRED' });
    return this.runAdvance(actor, id);
  }

  async cancel(actor: RegistrationActor, id: string) {
    const attempt = await this.requireCurrent(actor, id, undefined, true);
    if (attempt.state === 'CONNECTED') throw new ConflictException({ code: 'ATTEMPT_ALREADY_CONNECTED' });
    const leaseToken = attempt.channelId ? await this.acquireChannelLease(attempt) : null;
    try {
    await this.prisma.$transaction(async (tx) => {
      const channel = attempt.channelId ? await tx.buChannel.findFirst({ where: { id: attempt.channelId, currentAttemptId: id, generation: attempt.generation }, select: { operationLeaseToken: true } }) : null;
      if (attempt.channelId && channel?.operationLeaseToken !== leaseToken) throw new ConflictException({ code: 'ATTEMPT_STALE' });
      await tx.channelRegistrationAttempt.update({ where: { id }, data: { state: 'CANCELLED', stage: attempt.stage === 'RESERVED' ? 'CANCELLED' : 'PARTIAL_CLEANUP_REQUIRED', candidateKeyId: null, candidateNonce: null, candidateCiphertext: null, candidateTag: null, version: { increment: 1 } } });
      if (attempt.operation === 'NOVO' && attempt.stage === 'RESERVED' && attempt.channelId) {
        await tx.channelRegistrationAttempt.update({ where: { id }, data: { channelId: null } });
        await tx.buChannel.deleteMany({ where: { id: attempt.channelId, currentAttemptId: id, status: { in: ['CONECTANDO', 'DESCONECTADO'] } } });
      }
    });
    return this.dto(await this.prisma.channelRegistrationAttempt.findUniqueOrThrow({ where: { id } }));
    } finally { if (leaseToken) await this.releaseChannelLease(attempt, leaseToken); }
  }

  private async runAdvance(actor: RegistrationActor, id: string) {
    const attempt = await this.requireCurrent(actor, id, undefined, true);
    if (attempt.state !== 'PENDING_RECEIPT' || !attempt.channelId) throw new ConflictException({ code: 'CONFIRMATION_REQUIRED' });
    if (attempt.stage === 'SUBSCRIBED') {
      const channel = await this.prisma.buChannel.findFirst({ where: { id: attempt.channelId, currentAttemptId: id, receiptVerifiedAt: { not: null } } });
      if (!channel) throw new ConflictException({ code: 'PENDING_RECEIPT' });
      await this.prisma.$transaction(async (tx) => {
        await tx.channelRegistrationAttempt.updateMany({ where: { id, state: 'PENDING_RECEIPT', stage: 'SUBSCRIBED', version: attempt.version }, data: { state: 'CONNECTED', version: { increment: 1 } } });
        await tx.buChannel.updateMany({ where: { id: channel.id, currentAttemptId: id }, data: { status: 'CONECTADO', connectedAt: new Date() } });
      });
      return this.get(actor, id);
    }
    if (attempt.stage === 'SUBSCRIBING' || attempt.stage.endsWith('_AMBIGUOUS')) throw new ConflictException({ code: 'PENDING_RECEIPT' });
    if (attempt.leaseUntil && attempt.leaseUntil > new Date()) throw new ConflictException({ code: 'REGISTRATION_BUSY' });
    const now = new Date();
    const lease = await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, version: attempt.version, OR: [{ leaseUntil: null }, { leaseUntil: { lte: now } }] }, data: { leaseUntil: new Date(now.getTime() + LEASE_MS), version: { increment: 1 } } });
    if (!lease.count) throw new ConflictException({ code: 'REGISTRATION_BUSY' });
    let channelLeaseToken: string | null = null;
    try {
      channelLeaseToken = await this.acquireChannelLease(attempt);
      const context = await this.credentials.resolve(attempt.channelId, 'registration');
      if (!context.accessToken || !context.wabaId || !context.phoneNumberId) throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      const started = await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, version: attempt.version + 1, leaseUntil: { gt: new Date() } }, data: { stage: 'SUBSCRIBING', version: { increment: 1 } } });
      if (!started.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
      await this.meta.inscreverWaba(context.wabaId, context.accessToken);
      const afterProvider = await this.requireCurrent(actor, id, undefined, true);
      if (afterProvider.version !== attempt.version + 2 || afterProvider.stage !== 'SUBSCRIBING') throw new ConflictException({ code: 'ATTEMPT_STALE' });
      await this.prisma.$transaction(async (tx) => {
        const currentChannel = await tx.buChannel.findFirst({ where: { id: context.channelId, currentAttemptId: id, generation: context.generation }, select: { receiptVerifiedAt: true } });
        const receiptSeen = Boolean(currentChannel?.receiptVerifiedAt);
        const committed = await tx.channelRegistrationAttempt.updateMany({ where: { id, version: attempt.version + 2, stage: 'SUBSCRIBING', leaseUntil: { gt: new Date() } }, data: { stage: 'SUBSCRIBED', leaseUntil: null, safeErrorCode: null, version: { increment: 1 } } });
        if (!committed.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
        await tx.buChannel.updateMany({ where: { id: context.channelId, generation: context.generation, currentAttemptId: id }, data: { providerConnectionState: 'SUBSCRIBED', ...(receiptSeen ? { status: 'CONECTADO', connectedAt: new Date() } : {}) } });
        if (receiptSeen) await tx.channelRegistrationAttempt.updateMany({ where: { id, state: 'PENDING_RECEIPT', stage: 'SUBSCRIBED' }, data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', version: { increment: 1 } } });
      });
      return this.get(actor, id);
    } catch {
      await this.prisma.channelRegistrationAttempt.updateMany({ where: { id, stage: 'SUBSCRIBING', leaseUntil: { not: null } }, data: { leaseUntil: null, safeErrorCode: 'PROVIDER_STEP_FAILED', stage: 'SUBSCRIPTION_AMBIGUOUS', version: { increment: 1 } } });
      throw new ConflictException({ code: 'PROVIDER_STEP_FAILED' });
    } finally {
      if (channelLeaseToken) await this.releaseChannelLease(attempt, channelLeaseToken);
    }
  }

  private async requireCurrent(actor: RegistrationActor, id: string, sessionHash?: string, recovery = false) {
    const attempt = await this.prisma.channelRegistrationAttempt.findFirst({ where: { id, mantenedoraId: actor.mantenedoraId } });
    if (!attempt) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    await this.requireAdmin(actor.id, attempt.buId);
    if (recovery) await this.assertActorSession(actor);
    else {
      await this.assertSession(actor, attempt);
      if (attempt.userId !== actor.id || (sessionHash && !constantTime(attempt.sessionHash, sessionHash))) throw new ConflictException({ code: 'ATTEMPT_SESSION_MISMATCH' });
      if (attempt.expiresAt <= new Date() && !['CONNECTED', 'CANCELLED'].includes(attempt.state)) throw new ConflictException({ code: 'ATTEMPT_EXPIRED' });
    }
    if (attempt.channelId) {
      const current = await this.prisma.buChannel.findFirst({ where: { id: attempt.channelId, currentAttemptId: id, generation: attempt.generation } });
      if (!current) throw new ConflictException({ code: 'ATTEMPT_STALE' });
    }
    return attempt;
  }

  private async requireAdmin(userId: string, buId: string) { return exigirPapelNaBu(this.access, userId, buId, 'ADMIN'); }
  private async acquireChannelLease(attempt: { channelId: string | null; generation: number; id: string }) {
    if (!attempt.channelId) throw new ConflictException({ code: 'ATTEMPT_STALE' });
    const now = new Date();
    const leaseToken = cryptoRandomId();
    const claimed = await this.prisma.buChannel.updateMany({
      where: { id: attempt.channelId, currentAttemptId: attempt.id, generation: attempt.generation, OR: [{ operationLeaseUntil: null }, { operationLeaseUntil: { lte: now } }] },
      data: { operationLeaseToken: leaseToken, operationLeaseUntil: new Date(now.getTime() + LEASE_MS) },
    });
    if (!claimed.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
    return leaseToken;
  }
  private async releaseChannelLease(attempt: { channelId: string | null; generation: number; id: string }, leaseToken: string) {
    if (!attempt.channelId) return;
    const current = await this.prisma.buChannel.findFirst({ where: { id: attempt.channelId, currentAttemptId: attempt.id }, select: { generation: true } });
    if (!current) return;
    await this.prisma.buChannel.updateMany({
      where: { id: attempt.channelId, currentAttemptId: attempt.id, generation: current.generation, operationLeaseToken: leaseToken },
      data: { operationLeaseToken: null, operationLeaseUntil: null },
    });
  }
  private async assertSession(actor: RegistrationActor, attempt: { userId: string; sessionHash: string }) {
    const claims = this.sessions.verificar(actor.sessionToken);
    const user = claims?.uid === actor.id ? await this.prisma.appUser.findUnique({ where: { id: actor.id }, select: { status: true, passwordChangedAt: true } }) : null;
    if (!claims || !user || user.status !== 'ATIVO' || (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat)
      || !constantTime(attempt.sessionHash, hash(actor.sessionToken))) throw new ConflictException({ code: 'ATTEMPT_SESSION_MISMATCH' });
  }
  private async assertActorSession(actor: RegistrationActor) {
    const claims = this.sessions.verificar(actor.sessionToken);
    const user = claims?.uid === actor.id ? await this.prisma.appUser.findUnique({ where: { id: actor.id }, select: { status: true, passwordChangedAt: true } }) : null;
    if (!claims || !user || user.status !== 'ATIVO' || (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat)) throw new ConflictException({ code: 'SESSION_INVALID' });
  }
  private openCandidate(attempt: { candidateKeyId: string | null; candidateNonce: Uint8Array | null; candidateCiphertext: Uint8Array | null; candidateTag: Uint8Array | null; buId: string; channelId: string | null; generation: number; id: string }) {
    if (!attempt.candidateKeyId || !attempt.candidateNonce || !attempt.candidateCiphertext || !attempt.candidateTag || !attempt.channelId) throw new ConflictException({ code: 'CANDIDATE_CREDENTIAL_MISSING' });
    const { keyId, key } = loadChannelCredentialKey(process.env);
    if (keyId !== attempt.candidateKeyId) throw new ConflictException({ code: 'CANDIDATE_CREDENTIAL_MISSING' });
    return openChannelCredential({ keyId, nonce: Buffer.from(attempt.candidateNonce), ciphertext: Buffer.from(attempt.candidateCiphertext), tag: Buffer.from(attempt.candidateTag) }, new Map([[keyId, key]]), { purpose: 'candidate', provider: 'OFICIAL', buId: attempt.buId, channelId: attempt.channelId, generation: attempt.generation, attemptId: attempt.id }).toString('utf8');
  }
  private dto(row: { id: string; buId: string; channelId: string | null; type: ChannelType; operation: ChannelRegistrationOperation; state: ChannelRegistrationState; stage: string; safeErrorCode: string | null; expiresAt: Date; version: number; generation: number }) {
    return { id: row.id, buId: row.buId, channelId: row.channelId, tipo: row.type, operation: row.operation, state: row.state, stage: row.stage, errorCode: row.safeErrorCode, expiresAt: row.expiresAt, version: row.version, generation: row.generation };
  }
}

function hash(value: string) { return createHash('sha256').update(value).digest('hex'); }
function nonceForAttempt(sessionToken: string, attemptId: string) { return createHmac('sha256', sessionToken).update(`channel-registration-nonce-v1\0${attemptId}`).digest('base64url'); }
function constantTime(a: string, b: string) { const aa = Buffer.from(a); const bb = Buffer.from(b); return aa.length === bb.length && timingSafeEqual(aa, bb); }
function cryptoRandomId() { return randomBytes(16).toString('hex'); }
function dbBytes(value: Uint8Array): Uint8Array<ArrayBuffer> { return new Uint8Array(value); }

```

## Frozen file: api-app/src/domain/channels/safe-redaction.spec.ts

Original SHA-256: `f4b96c233ef4cda079ee80d04a413444902061efd88935220df550771722693e`; bytes:735.

```text
import { describe, expect, it } from 'vitest';
import { redactProviderData } from './safe-redaction';

describe('provider diagnostic redaction', () => {
  it('removes QR and webhook secrets while preserving safe stage metadata', () => {
    const value = redactProviderData({
      stage: 'SUBSCRIBED',
      qrcode: { base64: 'dummyQR', code: 'dummyPairing' },
      webhook: { headers: { authorization: 'Bearer dummy' }, verify_token: 'dummyVerify' },
      callback: 'https://api.invalid/webhooks/evolution/dummyPath?access_token=dummyToken',
    });
    expect(JSON.stringify(value)).not.toMatch(/dummyQR|dummyPairing|dummyVerify|dummyPath|dummyToken/);
    expect((value as { stage: string }).stage).toBe('SUBSCRIBED');
  });
});

```

## Frozen file: api-app/src/domain/channels/safe-redaction.ts

Original SHA-256: `66cbcf018a7723849dac83b7f3a6db15c1e795fec11c3f409c7e7d3b69e02123`; bytes:1447.

```text
const SECRET_KEY = /^(?:api.?key|access.?token|refresh.?token|token|authorization|secret|password|code|pin|qr|qr.?code|qrcode|ciphertext|nonce|auth.?tag|private.?key|client.?secret|verify.?token|hub\.verify_token)$/i;
const URL_SECRET = /([?&](?:access_token|client_secret|appsecret_proof|hub\.verify_token|verify_token|token|code|key|apikey)=)[^&#\s]*/gi;
const BEARER = /\bBearer\s+[^\s,;]+/gi;
const EVOLUTION_SECRET_PATH = /(\/webhooks\/evolution\/)[^/?#\s]+/gi;
const MAX_STRING = 16_384;
const MAX_ITEMS = 500;

/** Recursively remove secret-bearing fields and scrub secret URL components. */
export function redactProviderData<T = unknown>(value: T): T {
  return redact(value, new WeakSet<object>()) as T;
}

function redact(value: unknown, seen: WeakSet<object>, depth = 0): unknown {
  if (typeof value === 'string') return value.slice(0, MAX_STRING).replace(URL_SECRET, '$1[REDACTED]').replace(EVOLUTION_SECRET_PATH, '$1[REDACTED]').replace(BEARER, 'Bearer [REDACTED]');
  if (depth > 20) return '[REDACTED_DEPTH]';
  if (!value || typeof value !== 'object') return value;
  if (seen.has(value)) return '[REDACTED_CIRCULAR]';
  seen.add(value);
  if (Array.isArray(value)) return value.slice(0, MAX_ITEMS).map((item) => redact(item, seen, depth + 1));
  return Object.fromEntries(Object.entries(value).slice(0, MAX_ITEMS).map(([key, item]) => [
    key,
    SECRET_KEY.test(key) ? '[REDACTED]' : redact(item, seen, depth + 1),
  ]));
}

```

## Frozen file: api-app/src/domain/historico/cobertura.ts

Original SHA-256: `093f2a2926322ce68c4d7a66f174f7a6c13735c8ce7399ba863766295d1cdbee`; bytes:7505.

```text
import { ChaveDoCatalogo } from './catalogo';

/**
 * A regra de manutenção do catálogo (ADR-0022 §4), em forma executável.
 *
 * > Toda rota que escreve dado de negócio nasce com a sua linha no catálogo, ou
 * > com a justificativa de por que não tem — no mesmo commit.
 *
 * O teste em `test/cobertura-do-catalogo.e2e-spec.ts` percorre as rotas de
 * escrita de verdade, do roteador em execução, e **falha** quando alguma não
 * está aqui. É o que impede o catálogo de envelhecer em silêncio: a ausência de
 * uma linha de rastro não gera sintoma, e ninguém descobre pelo uso.
 */
export type Cobertura = { registra: ChaveDoCatalogo[] } | { isento: string };

export const COBERTURA_DE_ROTAS: Record<string, Cobertura> = {
  // --- BFF: identidade ---
  'POST /api/bff/auth/login': {
    isento:
      'ADR-0022 §2 exclui login do histórico. ATENÇÃO: a justificativa do ADR ' +
      '(“LoginAttempt já testemunha”) é falsa para login BEM-SUCEDIDO — ' +
      'LoginAttempt guarda só falhas. Precisa de decisão.',
  },
  'POST /api/bff/auth/logout': { isento: 'ADR-0022 §2 — logout não muda estado de negócio.' },
  'PATCH /api/bff/me': {
    isento:
      'ADR-0022 §2 — o próprio nome e telefone são ato sobre si mesmo, pela mesma ' +
      'razão que trocar a própria senha não entra. Mudar o cadastro DE OUTRA pessoa ' +
      'entra: é `usuario.atualizado`, e é poder exercido sobre terceiro.',
  },
  'POST /api/bff/auth/recuperar': {
    isento:
      'Pedir recuperação da PRÓPRIA senha é ato sobre si mesmo (ADR-0025 §Negativas), ' +
      'como trocar a própria senha. Cai na mesma lacuna já registrada do login ' +
      'bem-sucedido, que segue sem decisão.',
  },
  'POST /api/bff/auth/token/:token': {
    isento:
      'Definir a própria senha por convite ou recuperação — ato sobre si mesmo. ' +
      'A CRIAÇÃO da pessoa, que é ato de terceiro, já entra como `usuario.criado`.',
  },
  'POST /api/bff/me/password': {
    isento: 'ADR-0022 §2 — trocar a PRÓPRIA senha é ato sobre si mesmo; password_changed_at testemunha.',
  },

  'POST /api/bff/arquivos': {
    isento:
      'ADR-0024 — enviar um arquivo não muda estado de negócio por si só; o que muda é ' +
      'a marca ou o perfil que passa a apontar para ele, e ESSAS ações já estão no catálogo.',
  },
  'POST /api/bff/onboarding': { registra: ['mantenedora.configurada'] },
  'PUT /api/bff/onboarding': { registra: ['mantenedora.modulos'] },

  // --- BFF: números, canais e setores ---
  'POST /api/bff/business-units': { registra: ['numero.criado'] },
  'PATCH /api/bff/business-units/:buId': { registra: ['numero.editado'] },
  'POST /api/bff/business-units/:buId/setor': { registra: ['numero.movido'] },
  'POST /api/bff/business-units/:buId/channels': {
    isento: 'Rota legada aposentada com resposta determinística USE_NUMBER_REGISTRATIONS; não executa gravação nem chamada ao provider.',
  },
  'POST /api/bff/number-registrations': {
    isento: 'Fluxo técnico de autorização e verificação; o estado durável e as transições seguras ficam em channel_registration_attempts e channel_credentials. Só canal efetivamente pronto produz atividade de negócio.',
  },
  'POST /api/bff/number-registrations/:id/authorize': {
    isento: 'Consome código OAuth de uso único e atualiza tentativa técnica; não representa ainda um canal conectado.',
  },
  'POST /api/bff/number-registrations/:id/confirm': {
    isento: 'Verifica recurso e promove credencial candidata dentro do fluxo de tentativa; readiness permanece pendente até confirmação do provider.',
  },
  'POST /api/bff/number-registrations/:id/advance': {
    isento: 'Avanço idempotente do workflow técnico; o recebimento confirmado é evento de provider, não ação de usuário do catálogo.',
  },
  'POST /api/bff/number-registrations/:id/retry': {
    isento: 'Tentativa técnica de avanço; ambiguidades exigem recuperação manual sem repetir efeitos externos.',
  },
  'POST /api/bff/number-registrations/:id/cancel': {
    isento: 'Cancela tentativa de onboarding com estado persistido; não apaga nem reatribui identidade de provider.',
  },
  'POST /api/bff/business-units/:buId/channels/nao-oficial/pair': {
    isento: 'Pareamento e rotação de identidade Evolution são etapas técnicas; readiness depende de prova de identidade e receipt do provider.',
  },
  'POST /api/bff/business-units/:buId/channels/:tipo/verify': {
    isento: 'Consulta de prova de identidade no provider; só atualiza estado técnico verificado, sem afirmar conexão pronta.',
  },
  'DELETE /api/bff/business-units/:buId/channels/:tipo': { registra: ['canal.removido'] },
  'POST /api/bff/setores': { registra: ['setor.criado'] },
  'PATCH /api/bff/setores/:setorId': { registra: ['setor.renomeado', 'setor.status'] },
  'DELETE /api/bff/setores/:setorId': { registra: ['setor.excluido'] },
  'POST /api/bff/setores/:setorId/grants': { registra: ['acesso.concedido'] },
  'DELETE /api/bff/setores/:setorId/grants/:userId': { registra: ['acesso.revogado'] },

  // --- BFF: pessoas ---
  'POST /api/bff/usuarios': { registra: ['usuario.criado'] },
  'PATCH /api/bff/usuarios/:id': { registra: ['usuario.atualizado'] },
  'PUT /api/bff/usuarios/:id/grants': { registra: ['usuario.papel'] },
  'POST /api/bff/usuarios/:id/acesso': { registra: ['usuario.senha'] },

  // --- BFF: integração ---
  'POST /api/bff/integracao/api-keys': { registra: ['integracao.chave.criada'] },
  'DELETE /api/bff/integracao/api-keys/:id': { registra: ['integracao.chave.revogada'] },
  'PATCH /api/bff/integracao/webhook': { registra: ['integracao.webhook'] },
  'POST /api/bff/integracao/typebot/triggers': { registra: ['integracao.typebot.gatilho.criado'] },
  'PATCH /api/bff/integracao/typebot/triggers/:id': { registra: ['integracao.typebot.gatilho.status'] },

  // --- BFF: atendimento ---
  'POST /api/bff/conversations/:id/claim': { registra: ['atendimento.assumido'] },
  'POST /api/bff/conversations/:id/close': { registra: ['atendimento.encerrado'] },
  'POST /api/bff/conversations/:id/messages': {
    isento:
      'ADR-0022 §2 — a mensagem JÁ É `Message`, com autoria e horário. Duplicá-la ' +
      'faria o histórico virar um segundo log de conversa e afogar as outras categorias.',
  },

  // --- Superfície pública: quem age por ela não é usuário daqui ---
  'POST /api/v1/messages': { isento: 'ADR-0022 §2 — envio de mensagem já é `Message`.' },
  'POST /api/v1/conversations/:telefone/claim': {
    isento:
      'A API pública ainda não registra atendimento no histórico. É lacuna conhecida: ' +
      'o ADR-0022 §1 prevê ator_id null com o rótulo da chave, e isso entra quando ' +
      'a superfície pública for revisitada.',
  },
  'POST /api/v1/conversations/:telefone/release': {
    isento: 'Mesma lacuna do claim da API pública: a superfície pública ainda não registra atendimento.',
  },

  // --- Superfície interna e webhooks ---
  'POST /api/internal/mantenedoras': { registra: ['mantenedora.criada'] },
  'POST /webhooks/meta': { isento: 'ADR-0022 §2 — evento de terceiro, não ação de usuário; vive em webhook_events.' },
  'POST /webhooks/evolution/:segredo': {
    isento: 'Como o webhook da Meta: evento de terceiro, não ação de usuário; vive em webhook_events.',
  },
};

```

## Frozen file: api-app/src/domain/inbox/conversations.service.ts

Original SHA-256: `aed31180b6fb58442850421233bd61a62552144642bbac88e7fbef0efa1d1890`; bytes:13051.

```text
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
import { MessageAcceptanceService } from './message-acceptance.service';
import { ChannelCredentialResolver } from '../channels/channel-credential-resolver';
import { RealtimeService } from '../../realtime/realtime.service';

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
    private readonly acceptance: MessageAcceptanceService,
    private readonly credentials: ChannelCredentialResolver,
    private readonly realtime: RealtimeService,
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

    const scoped = await this.credentials.resolve(janela.canal.id);
    const externalId = await this.enviarPeloCanal(scoped, conversa.contact, texto);
    if (!externalId) throw new ConflictException({ code: 'EXTERNAL_MESSAGE_ID_MISSING' });
    const accepted = await this.acceptance.accept({
      providerResourceIdentityId: scoped.providerResourceIdentityId, channelId: scoped.channelId,
      generation: scoped.generation, pairingEpoch: scoped.pairingEpoch, buId: scoped.buId,
      channelOrigin: scoped.provider, externalMessageId: externalId, contact: conversa.contact,
      contactType: conversa.contactType, conversationId: conversa.id, direction: 'OUT', messageType: 'TEXTO',
      content: texto, authorUserId: atendente.userId || null, authorName: atendente.nome, senderResult: true,
    });
    const mensagem = accepted.message;
    if (accepted.creationWinner) this.realtime.publicarNaBu(conversa.buId, { tipo: 'mensagem', conversaId: conversa.id, contato: conversa.contact, direcao: 'OUT', canal: mensagem.channelOrigin, naoLidas: accepted.conversation.unreadCount });

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
    canal: Awaited<ReturnType<ChannelCredentialResolver['resolve']>>,
    contato: string,
    texto: string,
  ): Promise<string | null> {
    try {
      if (canal.provider === 'OFICIAL') {
        if (!canal.phoneNumberId || !canal.accessToken) {
          throw new BadRequestException({ error: 'Canal sem número de envio.', code: 'CANAL_SEM_NUMERO' });
        }
        return await this.meta.enviarTexto(canal.phoneNumberId, contato, texto, canal.accessToken);
      }
      if (!canal.evolutionInstanceName) {
        throw new BadRequestException({ error: 'Canal sem instância.', code: 'CANAL_SEM_INSTANCIA' });
      }
      return await this.evolution.enviarTexto(canal.evolutionInstanceName, contato, texto);
    } catch (e) {
      if (e instanceof BadRequestException || e instanceof ConflictException) throw e;
      // Os dois códigos ficam DISTINTOS de propósito: quem trata o erro quer
      // saber qual plataforma recusou, porque o contorno é diferente (ADR-0010).
      throw new BadRequestException({ error: 'O canal recusou o envio.', code: canal.provider === 'OFICIAL' ? 'META_RECUSOU' : 'EVOLUTION_RECUSOU' });
    }
  }
}

```

## Frozen file: api-app/src/domain/inbox/incoming.service.ts

Original SHA-256: `57eaf64ba4c896016f83d8ebff1f9cea5ee696d8c9b546f3cc30d53e94af525e`; bytes:6927.

```text
import { Inject, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { RealtimeService } from '../../realtime/realtime.service';
import { META_CLIENT, MetaClient } from '../../integrations/meta/meta.client';
import { TYPEBOT_CLIENT, TypebotClient } from '../../integrations/typebot/typebot.client';
import { MessageAcceptanceService } from './message-acceptance.service';
import { ChannelCredentialResolver } from '../channels/channel-credential-resolver';

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
    @Inject(META_CLIENT) private readonly meta: MetaClient,
    @Inject(TYPEBOT_CLIENT) private readonly typebot: TypebotClient,
    private readonly acceptance: MessageAcceptanceService,
    private readonly credentials: ChannelCredentialResolver,
  ) {}

  async registrar(m: MensagemRecebida) {
    const accepted = await this.acceptance.accept({
      providerResourceIdentityId: m.providerResourceIdentityId, channelId: m.channelId, generation: m.generation,
      pairingEpoch: m.pairingEpoch, buId: m.buId, channelOrigin: m.canal, externalMessageId: m.externalId ?? '',
      contact: m.contato, contactType: m.ehGrupo ? 'GRUPO' : 'PESSOA', displayName: m.nomeExibicao,
      direction: m.direcao, messageType: m.tipo, content: m.conteudo, authorName: m.autorNome,
    });
    const { conversation: conversa, message: mensagem, creationWinner } = accepted;
    if (creationWinner) {
      this.realtime.publicarNaBu(m.buId, { tipo: 'mensagem', conversaId: conversa.id, contato: conversa.contact, direcao: m.direcao, canal: m.canal, naoLidas: conversa.unreadCount });
      if (m.canal === 'OFICIAL' && m.direcao === 'IN' && m.tipo === 'TEXTO' && m.conteudo?.trim()) {
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
    const channel = await this.prisma.buChannel.findUnique({ where: { id: incoming.channelId } });
    if (!channel?.phoneNumberId) return;
    const scoped = await this.credentials.resolve(channel.id);
    if (!scoped.accessToken) return;
    const botId = gatilho.bot.publishedTypebotId;
    if (!botId) return;
    const atual = await this.prisma.typebotSession.findUnique({ where: { botId_buId_contato: { botId: gatilho.botId, buId, contato } } });
    if (atual && (atual.mantenedoraId !== bu.mantenedoraId || atual.buId !== buId || atual.botId !== gatilho.botId)) return;
    const resposta = atual?.ativo ? await this.typebot.continuar(atual.sessionId, texto) : await this.typebot.iniciar(botId, contato, texto);
    const sessionId = 'sessionId' in resposta && typeof resposta.sessionId === 'string' ? resposta.sessionId : null;
    if (!atual && sessionId) await this.prisma.typebotSession.create({ data: { botId: gatilho.botId, mantenedoraId: gatilho.bot.mantenedoraId, buId, contato, sessionId } });
    for (const mensagem of resposta.messages) {
      const saida = textoDaRespostaTypebot(mensagem);
      if (!saida) continue;
      const externalId = await this.meta.enviarTexto(channel.phoneNumberId, contato, saida, scoped.accessToken);
      if (!externalId) continue;
      const accepted = await this.acceptance.accept({
        providerResourceIdentityId: scoped.providerResourceIdentityId, channelId: scoped.channelId, generation: scoped.generation,
        pairingEpoch: scoped.pairingEpoch, buId, channelOrigin: 'OFICIAL', externalMessageId: externalId,
        contact: contato, contactType: 'PESSOA', conversationId, direction: 'OUT', messageType: 'TEXTO', content: saida,
        authorName: 'Typebot', senderResult: true,
      });
      if (accepted.creationWinner) this.realtime.publicarNaBu(buId, { tipo: 'mensagem', conversaId: conversationId, contato, direcao: 'OUT', canal: 'OFICIAL', naoLidas: accepted.conversation.unreadCount });
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

## Frozen file: api-app/src/domain/inbox/incoming.typebot.integration.spec.ts

Original SHA-256: `229cd0805d0543b5cbb38cecf97492e1d8a225fa65e166c5fd96547a587edede`; bytes:4973.

```text
import { describe, expect, it, vi } from 'vitest';
import { IncomingService } from './incoming.service';

describe('ponte de evento Meta → Typebot → Meta', () => {
  it('inicia a sessão no primeiro evento e grava a resposta do bot', async () => {
    const registrarSessao = vi.fn();
    const publicar = vi.fn();
    const prisma = {
      businessUnit: { findUnique: vi.fn().mockResolvedValue({ mantenedoraId: 'tenant-1' }) },
      conversation: { count: vi.fn().mockResolvedValue(0) },
      typebotTrigger: { findMany: vi.fn().mockResolvedValue([{
        id: 'trigger-1', botId: 'bot-1', kind: 'NOVA_CONVERSA', value: '*', buId: null,
        bot: { id: 'bot-1', mantenedoraId: 'tenant-1', status: 'ATIVO', publishedTypebotId: 'public-1' },
      }]) },
      buChannel: { findUnique: vi.fn().mockResolvedValue({ phoneNumberId: 'phone-1' }) },
      typebotSession: { findUnique: vi.fn().mockResolvedValue(null), create: registrarSessao },
      webhookEvent: { create: vi.fn() },
    };
    const typebot = {
      configurado: () => true,
      iniciar: vi.fn().mockResolvedValue({ sessionId: 'session-1', messages: [{ type: 'text', content: { richText: ['Olá!'] } }] }),
      continuar: vi.fn(),
    };
    const meta = { enviarTexto: vi.fn().mockResolvedValue('meta-message-1') };
    const accepted = vi.fn()
      .mockResolvedValueOnce({ conversation: { id: 'conversation-1', contact: '5584999990000', unreadCount: 1 }, message: { id: 'message-1' }, creationWinner: true, reconciled: false, conversationCreated: true, reopened: false })
      .mockResolvedValueOnce({ conversation: { id: 'conversation-1', contact: '5584999990000', unreadCount: 1 }, message: { id: 'out-1' }, creationWinner: true, reconciled: false, conversationCreated: false, reopened: false });
    const credentials = { resolve: vi.fn().mockResolvedValue({ accessToken: 'scoped-token', providerResourceIdentityId: 'identity-1', channelId: 'channel-1', generation: 1, pairingEpoch: 1 }) };
    const service = new IncomingService(prisma as never, { publicarNaBu: publicar } as never, meta as never, typebot as never, { accept: accepted } as never, credentials as never);

    await service.registrar({ buId: 'bu-1', canal: 'OFICIAL', contato: '5584999990000', ehGrupo: false, direcao: 'IN', tipo: 'TEXTO', conteudo: 'oi', externalId: 'in-1', providerResourceIdentityId: 'identity-1', channelId: 'channel-1', generation: 1, pairingEpoch: 1 });

    expect(typebot.iniciar).toHaveBeenCalledWith('public-1', '5584999990000', 'oi');
    expect(registrarSessao).toHaveBeenCalledWith({ data: expect.objectContaining({ botId: 'bot-1', buId: 'bu-1', sessionId: 'session-1' }) });
    expect(meta.enviarTexto).toHaveBeenCalledWith('phone-1', '5584999990000', 'Olá!', 'scoped-token');
    expect(accepted).toHaveBeenCalledTimes(2);
    expect(accepted.mock.calls[1][0]).toMatchObject({ direction: 'OUT', externalMessageId: 'meta-message-1', senderResult: true });
    expect(publicar).toHaveBeenCalled();
  });

  it('continua a sessão existente sem iniciar outra', async () => {
    const prisma = {
      businessUnit: { findUnique: vi.fn().mockResolvedValue({ mantenedoraId: 't' }) },
      conversation: { count: vi.fn().mockResolvedValue(1) },
      typebotTrigger: { findMany: vi.fn().mockResolvedValue([{ botId: 'b', kind: 'PALAVRA_CHAVE', value: 'ajuda', buId: 'bu', bot: { mantenedoraId: 't', status: 'ATIVO', publishedTypebotId: 'public' } }]) },
      buChannel: { findUnique: vi.fn().mockResolvedValue({ phoneNumberId: 'phone' }) },
      typebotSession: { findUnique: vi.fn().mockResolvedValue({ botId: 'b', mantenedoraId: 't', buId: 'bu', sessionId: 'session', ativo: true }), create: vi.fn() },
      webhookEvent: { create: vi.fn() },
    };
    const typebot = { configurado: () => true, iniciar: vi.fn(), continuar: vi.fn().mockResolvedValue({ messages: [] }) };
    const meta = { enviarTexto: vi.fn() };
    const accepted = vi.fn().mockResolvedValue({ conversation: { id: 'c', contact: '1', unreadCount: 1 }, message: { id: 'm' }, creationWinner: true, reconciled: false, conversationCreated: false, reopened: false });
    const credentials = { resolve: vi.fn().mockResolvedValue({ accessToken: 'scoped-token', providerResourceIdentityId: 'identity-1', channelId: 'channel-1', generation: 1, pairingEpoch: 1 }) };
    const service = new IncomingService(prisma as never, { publicarNaBu: vi.fn() } as never, meta as never, typebot as never, { accept: accepted } as never, credentials as never);
    await service.registrar({ buId: 'bu', canal: 'OFICIAL', contato: '1', ehGrupo: false, direcao: 'IN', tipo: 'TEXTO', conteudo: 'preciso de AJUDA', externalId: 'in-1', providerResourceIdentityId: 'identity-1', channelId: 'channel-1', generation: 1, pairingEpoch: 1 });
    expect(typebot.continuar).toHaveBeenCalledWith('session', 'preciso de AJUDA');
    expect(typebot.iniciar).not.toHaveBeenCalled();
  });
});

```

## Frozen file: api-app/src/domain/inbox/message-acceptance.service.ts

Original SHA-256: `c959930ad04633d1423be35727070dca2cd52e592549d9f7c40fc00252da07d4`; bytes:14448.

```text
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
    if (!input.externalMessageId?.trim()) {
      throw new BadRequestException({ code: 'EXTERNAL_MESSAGE_ID_REQUIRED' });
    }
    if (!input.providerResourceIdentityId || !input.channelId || !input.buId) {
      throw new BadRequestException({ code: 'VERIFIED_RESOURCE_REQUIRED' });
    }

    try {
      return await this.prisma.$transaction(async (tx) => {
        await this.lockAndValidateCurrentIdentity(tx, input);
        const key = { providerResourceIdentityId: input.providerResourceIdentityId, externalId: input.externalMessageId };
        const prior = await tx.message.findUnique({
          where: { providerResourceIdentityId_externalId: key }, include: { conversation: true },
        });
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
            authorUserId: input.senderResult ? input.authorUserId ?? null : null,
            authorName: input.senderResult ? input.authorName ?? null : null,
          },
        });
        if (input.direction === 'IN') {
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
        return { conversation, message, creationWinner: true, reconciled: false, conversationCreated, reopened };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      // A concurrent insert may win after our initial lookup. Its transaction
      // rolled back this attempt's conversation/unread effects atomically.
      if (!isUniqueViolation(error)) throw error;
      const prior = await this.prisma.message.findUnique({
        where: {
          providerResourceIdentityId_externalId: {
            providerResourceIdentityId: input.providerResourceIdentityId,
            externalId: input.externalMessageId,
          },
        }, include: { conversation: true },
      });
      if (!prior) throw error;
      return this.prisma.$transaction(async (tx) => {
        await this.lockAndValidateCurrentIdentity(tx, input);
        const current = await tx.message.findUniqueOrThrow({
          where: {
            providerResourceIdentityId_externalId: {
              providerResourceIdentityId: input.providerResourceIdentityId,
              externalId: input.externalMessageId,
            },
          }, include: { conversation: true },
        });
        return this.reconcile(tx, current, input);
      });
    }
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

## Frozen file: api-app/src/domain/tenancy/tenancy.service.ts

Original SHA-256: `c9348f86f1f2bcfd4af3f9bd3e91cb5218d81cf13098989b5f6ea64acbb41398`; bytes:10923.

```text
import { BadRequestException, ConflictException, Injectable, NotFoundException } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { PasswordService } from '../identity/password.service';
import { RegistroDeAtividade } from '../historico/registro.service';
import { Prisma } from '@prisma/client';

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

  /** Same grant/setor rule as criarBusinessUnit, reusable in a larger atomic reservation. */
  async criarBusinessUnitNaTransacao(
    tx: Prisma.TransactionClient,
    mantenedoraId: string,
    nome: string,
    setorId?: string,
    ator?: { id: string | null; nome: string; email?: string | null },
  ) {
    const setor = setorId
      ? await tx.setor.findFirst({ where: { id: setorId, mantenedoraId } })
      : ((await tx.setor.findFirst({ where: { mantenedoraId, name: SETOR_PADRAO } })) ?? await tx.setor.create({ data: { mantenedoraId, name: SETOR_PADRAO } }));
    if (!setor) throw new NotFoundException({ error: 'Setor não encontrado.', code: 'NAO_ENCONTRADO' });
    const bu = await tx.businessUnit.create({ data: { mantenedoraId, setorId: setor.id, name: nome.trim() } });
    const tenantGrants = await tx.userBuRole.findMany({ where: { grantedViaTipo: 'MANTENEDORA', grantedViaId: mantenedoraId }, select: { userId: true, role: true }, distinct: ['userId'] });
    const sectorGrants = await tx.setorGrant.findMany({ where: { setorId: setor.id }, select: { userId: true, role: true } });
    const tenantUsers = new Set(tenantGrants.map((row) => row.userId));
    const grants = [
      ...tenantGrants.map((row) => ({ userId: row.userId, buId: bu.id, role: row.role, grantedViaTipo: 'MANTENEDORA' as const, grantedViaId: mantenedoraId })),
      ...sectorGrants.filter((row) => !tenantUsers.has(row.userId)).map((row) => ({ userId: row.userId, buId: bu.id, role: row.role, grantedViaTipo: 'SETOR' as const, grantedViaId: setor.id })),
    ];
    if (grants.length) await tx.userBuRole.createMany({ data: grants });
    if (ator) await this.registro.registrar(tx, mantenedoraId, 'numero.criado', ator, { buId: bu.id, entidadeId: bu.id, frase: { nome: bu.name } });
    return { bu, setor, herdaram: grants.length };
  }
}

```

## Frozen file: api-app/src/infra/config/modulos.spec.ts

Original SHA-256: `e33f72f28f4d41b8899a2b48ea13eacf519e0669d88663d74a818f0f8ae80a59`; bytes:4445.

```text
import { describe, expect, it } from 'vitest';
import {
  REGISTRO_DE_MODULOS,
  efetivos,
  lerContratados,
  lerModulos,
  verificarConfiguracao,
} from './modulos';

const COM_PISO = {} as NodeJS.ProcessEnv;

describe('registro de módulos (ADR-0016, Emenda 2)', () => {
  it('só contém módulo que TEM código atrás', () => {
    // CRM está fora da v1.1, disparo é v2, e o histórico deixou de ser módulo.
    // Flag que nunca pode ser verdadeira é código que mente sobre o produto.
    expect(REGISTRO_DE_MODULOS.map((m) => m.chave)).toEqual(['canalNaoOficial']);
    expect(REGISTRO_DE_MODULOS.map((m) => m.env)).not.toContain('LH_MODULE_CRM');
    expect(REGISTRO_DE_MODULOS.map((m) => m.env)).not.toContain('LH_MODULE_AUDIT');
  });

  it('o canal oficial NÃO é módulo — é o piso', () => {
    expect(REGISTRO_DE_MODULOS.map((m) => m.env)).not.toContain('LH_CHANNEL_OFFICIAL');
    expect(lerModulos({} as NodeJS.ProcessEnv)).not.toHaveProperty('canalOficial');
  });
});

describe('teto da instalação', () => {
  it('lê a flag em várias grafias, e o resto é desligado', () => {
    expect(lerModulos({ LH_CHANNEL_UNOFFICIAL: 'true' } as NodeJS.ProcessEnv).canalNaoOficial).toBe(true);
    expect(lerModulos({ LH_CHANNEL_UNOFFICIAL: '1' } as NodeJS.ProcessEnv).canalNaoOficial).toBe(true);
    expect(lerModulos({ LH_CHANNEL_UNOFFICIAL: 'SIM' } as NodeJS.ProcessEnv).canalNaoOficial).toBe(true);
    expect(lerModulos({ LH_CHANNEL_UNOFFICIAL: 'false' } as NodeJS.ProcessEnv).canalNaoOficial).toBe(false);
    expect(lerModulos({} as NodeJS.ProcessEnv).canalNaoOficial).toBe(false);
  });
});

describe('verificação de boot', () => {
  it('sem capacidade Meta configurada, ainda sobe para administrar vínculos', () => {
    expect(() => verificarConfiguracao({} as NodeJS.ProcessEnv)).not.toThrow();
  });

  it('com o piso e nenhum módulo, sobe', () => {
    expect(() => verificarConfiguracao(COM_PISO)).not.toThrow();
  });

  it('ligar o canal não oficial SEM credencial é erro de boot, não 503 depois', () => {
    const env = { ...COM_PISO, LH_CHANNEL_UNOFFICIAL: 'true' } as NodeJS.ProcessEnv;
    expect(() => verificarConfiguracao(env)).toThrow(/EVOLUTION_API_URL/);

    const meio = { ...env, EVOLUTION_API_URL: 'http://evo:8080' } as NodeJS.ProcessEnv;
    expect(() => verificarConfiguracao(meio)).toThrow(/EVOLUTION_API_KEY/);

    const completo = { ...meio, EVOLUTION_API_KEY: 'chave' } as NodeJS.ProcessEnv;
    expect(() => verificarConfiguracao(completo)).not.toThrow();
  });

  it('a mensagem lista TUDO que falta, não só a primeira', () => {
    const env = { LH_CHANNEL_UNOFFICIAL: 'true' } as NodeJS.ProcessEnv;
    try {
      verificarConfiguracao(env);
      expect.unreachable('devia ter estourado');
    } catch (e) {
      const msg = (e as Error).message;
      expect(msg).toContain('EVOLUTION_API_URL');
      expect(msg).toContain('EVOLUTION_API_KEY');
    }
  });

  it('recusa conjuntos parciais de configuração Meta e chave de cifra', () => {
    expect(() => verificarConfiguracao({ META_APP_ID: 'fake' } as NodeJS.ProcessEnv)).toThrow(/META_APP_ID/);
    expect(() => verificarConfiguracao({ CHANNEL_CREDENTIAL_KEY_ID: 'fake' } as NodeJS.ProcessEnv)).toThrow(/CHANNEL_CREDENTIAL_KEY_ID/);
  });
});

describe('interseção: env é o teto, a Mantenedora escolhe dentro dele', () => {
  it('a Mantenedora NÃO amplia o teto', () => {
    const teto = { canalNaoOficial: false };
    expect(efetivos(teto, { canalNaoOficial: true }).canalNaoOficial).toBe(false);
  });

  it('o teto sozinho não liga nada — precisa ter sido contratado', () => {
    const teto = { canalNaoOficial: true };
    expect(efetivos(teto, {}).canalNaoOficial).toBe(false);
    expect(efetivos(teto, { canalNaoOficial: false }).canalNaoOficial).toBe(false);
    expect(efetivos(teto, { canalNaoOficial: true }).canalNaoOficial).toBe(true);
  });

  it('ignora chave desconhecida vinda do banco em vez de estourar', () => {
    // Um módulo removido do registro deixa lixo na coluna; a LEITURA convive com
    // ele. É a escrita que recusa o desconhecido (MODULO_FORA_DA_INSTALACAO).
    expect(lerContratados({ crm: true, canalNaoOficial: true })).toEqual({ canalNaoOficial: true });
    expect(lerContratados(null)).toEqual({});
    expect(lerContratados('nada disso')).toEqual({});
  });
});

```

## Frozen file: api-app/src/infra/config/modulos.ts

Original SHA-256: `42c3fcb8205cb77356da28c756eebc510f8c2597c28ebf22c7314f625359a61c`; bytes:4329.

```text
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

  const metaFields = ['META_APP_ID', 'META_APP_SECRET', 'META_SIGNUP_CONFIG_ID'];
  const metaPresent = metaFields.filter((field) => String(env[field] ?? '').trim()).length;
  if (metaPresent !== 0 && metaPresent !== metaFields.length) {
    faltando.push('META_APP_ID, META_APP_SECRET e META_SIGNUP_CONFIG_ID devem estar todos definidos ou todos ausentes');
  }
  const cryptoFields = ['CHANNEL_CREDENTIAL_KEY_ID', 'CHANNEL_CREDENTIAL_KEY'];
  const cryptoPresent = cryptoFields.filter((field) => String(env[field] ?? '').trim()).length;
  if (cryptoPresent !== 0 && cryptoPresent !== cryptoFields.length) {
    faltando.push('CHANNEL_CREDENTIAL_KEY_ID e CHANNEL_CREDENTIAL_KEY devem estar ambos definidos ou ambos ausentes');
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

```

## Frozen file: api-app/src/integrations/evolution/evolution.client.spec.ts

Original SHA-256: `4de63e227810736164c30fee397d1f47133f292f3733e0864264c7f51d1b5c23`; bytes:3025.

```text
import { afterEach, describe, expect, it, vi } from 'vitest';
import { EvolutionHttpClient, EvolutionIndisponivelError } from './evolution.client';

describe('EvolutionHttpClient instance creation response', () => {
  const before = {
    url: process.env.EVOLUTION_API_URL,
    key: process.env.EVOLUTION_API_KEY,
    webhook: process.env.EVOLUTION_WEBHOOK_URL,
  };
  afterEach(() => {
    vi.unstubAllGlobals();
    if (before.url === undefined) delete process.env.EVOLUTION_API_URL; else process.env.EVOLUTION_API_URL = before.url;
    if (before.key === undefined) delete process.env.EVOLUTION_API_KEY; else process.env.EVOLUTION_API_KEY = before.key;
    if (before.webhook === undefined) delete process.env.EVOLUTION_WEBHOOK_URL; else process.env.EVOLUTION_WEBHOOK_URL = before.webhook;
  });

  it('returns only QR material when create confirms the exact instance name', async () => {
    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
    process.env.EVOLUTION_API_KEY = 'fixture-key';
    process.env.EVOLUTION_WEBHOOK_URL = 'https://api.invalid/webhooks/evolution/fixture';
    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => ({
      instance: { instanceName: 'lh-channel-1' }, hash: 'must-not-escape', qrcode: { base64: 'fixture-qr' },
    }) });
    vi.stubGlobal('fetch', fetchFake);
    const result = await new EvolutionHttpClient().criarInstancia('lh-channel-1');
    expect(result).toEqual({ qrcode: 'fixture-qr' });
    expect(JSON.stringify(result)).not.toContain('must-not-escape');
    expect(fetchFake).toHaveBeenCalledTimes(1);
  });

  it.each([
    {},
    { instance: { instanceName: 'another-instance' }, qrcode: { base64: 'must-not-escape' } },
  ])('rejects a successful HTTP response without exact created identity confirmation', async (payload) => {
    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
    process.env.EVOLUTION_API_KEY = 'fixture-key';
    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => payload });
    vi.stubGlobal('fetch', fetchFake);
    await expect(new EvolutionHttpClient().criarInstancia('lh-requested-instance')).rejects.toBeInstanceOf(EvolutionIndisponivelError);
  });

  it('requires an explicit SUCCESS response for exact-instance cleanup', async () => {
    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
    process.env.EVOLUTION_API_KEY = 'fixture-key';
    const fetchFake = vi.fn()
      .mockResolvedValueOnce({ ok: true, json: async () => ({ status: 'SUCCESS', error: false }) })
      .mockResolvedValueOnce({ ok: true, json: async () => ({ status: 'SUCCESS', error: true }) });
    vi.stubGlobal('fetch', fetchFake);
    const client = new EvolutionHttpClient();
    await expect(client.apagarInstancia('lh-exact-name')).resolves.toBeUndefined();
    await expect(client.apagarInstancia('lh-exact-name')).rejects.toBeInstanceOf(EvolutionIndisponivelError);
    expect(String(fetchFake.mock.calls[0][0])).toContain('/instance/delete/lh-exact-name');
  });
});

```

## Frozen file: api-app/src/integrations/evolution/evolution.client.ts

Original SHA-256: `78e810e77d489576b721db10ed629f0145f023d737b3b33ef5efa73f1352763f`; bytes:4973.

```text
import { Injectable } from '@nestjs/common';

export const EVOLUTION_CLIENT = Symbol('EVOLUTION_CLIENT');

export interface InstanciaCriada {
  qrcode: string | null;
}
export interface InstanciaObservada { name: string; ownerJid: string | null; connectionStatus: string | null; }

/**
 * Porta do canal não oficial. Adaptador de SAÍDA — a Evolution API é serviço
 * interno do projeto, **sem domínio público** (ADR-0002).
 */
export interface EvolutionClient {
  configurado(): boolean;
  criarInstancia(nome: string): Promise<InstanciaCriada>;
  qrDaInstancia(nome: string): Promise<string | null>;
  estadoDaInstancia(nome: string): Promise<string>;
  consultarInstancia(nome: string): Promise<InstanciaObservada | null>;
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
    const payload = data as { instance?: { instanceName?: unknown }; qrcode?: { base64?: string } | string; base64?: string };
    if (!payload.instance || payload.instance.instanceName !== nome) {
      throw new EvolutionIndisponivelError('A Evolution não confirmou a identidade da instância solicitada.');
    }
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

  async consultarInstancia(nome: string): Promise<InstanciaObservada | null> {
    const query = new URLSearchParams({ instanceName: nome });
    const data = await this.chamar('GET', `/instance/fetchInstances?${query.toString()}`);
    const instances = Array.isArray(data) ? data : [];
    const found = instances.find((item) => item && typeof item === 'object' && (item as { name?: unknown }).name === nome) as Record<string, unknown> | undefined;
    if (!found) return null;
    return {
      name: typeof found.name === 'string' ? found.name : nome,
      ownerJid: typeof found.ownerJid === 'string' ? found.ownerJid : null,
      connectionStatus: typeof found.connectionStatus === 'string' ? found.connectionStatus : null,
    };
  }

  async apagarInstancia(nome: string): Promise<void> {
    const result = await this.chamar('DELETE', `/instance/delete/${encodeURIComponent(nome)}`) as { status?: unknown; error?: unknown };
    if (result.status !== 'SUCCESS' || result.error !== false) throw new EvolutionIndisponivelError('A Evolution não confirmou a remoção da instância.');
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
      signal: AbortSignal.timeout(10_000),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      void data;
      throw new EvolutionIndisponivelError('A Evolution API recusou a operação.');
    }
    return data;
  }
}

```

## Frozen file: api-app/src/integrations/meta/meta.client.spec.ts

Original SHA-256: `e013ee76b4ba471d5e3b942483e60bc11a6219397fe495f4dc702571b7d2ae13`; bytes:7607.

```text
import { afterEach, describe, expect, it, vi } from 'vitest';
import { MetaHttpClient, MetaIndisponivelError } from './meta.client';

describe('MetaHttpClient scoped credentials', () => {
  const vars = ['META_APP_ID', 'META_APP_SECRET', 'META_SIGNUP_CONFIG_ID', 'GRAPH_VERSION', 'WHATSAPP_TOKEN'];
  const before = new Map(vars.map((key) => [key, process.env[key]]));
  afterEach(() => {
    vi.unstubAllGlobals();
    for (const key of vars) {
      const value = before.get(key);
      if (value === undefined) delete process.env[key]; else process.env[key] = value;
    }
  });

  it('exposes only public installation capability and is unavailable when unset', () => {
    delete process.env.META_APP_ID;
    delete process.env.META_APP_SECRET;
    delete process.env.META_SIGNUP_CONFIG_ID;
    process.env.WHATSAPP_TOKEN = 'fake-legacy-token';
    expect(new MetaHttpClient().capabilities()).toMatchObject({ available: false, reason: 'NOT_CONFIGURED', appId: null, configId: null });
  });

  it('rejects partial installation setup without returning its secret', () => {
    process.env.META_APP_ID = 'fake-app-id';
    process.env.META_APP_SECRET = '';
    process.env.META_SIGNUP_CONFIG_ID = '';
    expect(new MetaHttpClient().capabilities()).toMatchObject({ available: false, reason: 'PARTIAL_CONFIGURATION', appId: 'fake-app-id' });
  });

  it('exchanges code in a POST body and never places it in the URL', async () => {
    process.env.META_APP_ID = 'fake-id';
    process.env.META_APP_SECRET = 'fake-secret';
    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
    const fetchFake = vi.fn()
      .mockResolvedValueOnce({ ok: true, json: async () => ({ access_token: 'candidate-token' }) })
      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [{ scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] }] } }) });
    vi.stubGlobal('fetch', fetchFake);
    const result = await new MetaHttpClient().exchangeCode('sensitive-code');
    expect(result.accessToken).toBe('candidate-token');
    expect(fetchFake.mock.calls[0][0]).not.toContain('sensitive-code');
    expect(String(fetchFake.mock.calls[0][1].body)).toContain('code=sensitive-code');
  });

  it('does not use legacy token and emits a safe error for provider details', async () => {
    process.env.WHATSAPP_TOKEN = 'legacy-token-must-not-be-used';
    const fetchFake = vi.fn().mockResolvedValue({ ok: false, status: 400, json: async () => ({ error: { message: 'secret provider detail' } }) });
    vi.stubGlobal('fetch', fetchFake);
    await expect(new MetaHttpClient().enviarTexto('phone-id', '558400000000', 'hello')).rejects.toBeInstanceOf(MetaIndisponivelError);
    expect(fetchFake).not.toHaveBeenCalled();
  });

  it('requires both scoped permissions on the same WABA before listing phone numbers', async () => {
    process.env.META_APP_ID = 'fake-id';
    process.env.META_APP_SECRET = 'fake-secret';
    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
    const tokenInfo = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
      { scope: 'whatsapp_business_management', target_ids: ['123456'] },
      { scope: 'whatsapp_business_messaging', target_ids: ['654321'] },
    ] } };
    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => tokenInfo });
    vi.stubGlobal('fetch', fetchFake);
    const client = new MetaHttpClient();
    await expect(client.recursos('candidate', '123456')).rejects.toBeInstanceOf(MetaIndisponivelError);
    expect(fetchFake).toHaveBeenCalledTimes(1);
  });

  it('verifies the selected phone on the provider-returned page cursor and rejects a foreign phone', async () => {
    process.env.META_APP_ID = 'fake-id';
    process.env.META_APP_SECRET = 'fake-secret';
    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
    const fetchFake = vi.fn()
      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
        { scope: 'whatsapp_business_management', target_ids: ['123456'] },
        { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
      ] } }) })
      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] }) });
    vi.stubGlobal('fetch', fetchFake);
    const client = new MetaHttpClient();
    const number = await client.confirmarNumero('123456', '987654321', 'candidate', 'provider-cursor-page-2');
    expect(number).toMatchObject({ id: '987654321', telefone: '5584999990000' });
    const edgeUrl = String(fetchFake.mock.calls[1][0]);
    expect(edgeUrl).toContain('/v21.0/123456/phone_numbers');
    expect(new URL(edgeUrl).searchParams.get('after')).toBe('provider-cursor-page-2');
    expect(String(fetchFake.mock.calls[0][1].headers.authorization)).toBe('Bearer fake-id|fake-secret');

    const foreign = vi.fn()
      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
        { scope: 'whatsapp_business_management', target_ids: ['123456'] },
        { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
      ] } }) })
      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321' }] }) });
    vi.stubGlobal('fetch', foreign);
    await expect(client.confirmarNumero('123456', '111111111', 'candidate', 'provider-cursor-page-2')).resolves.toBeNull();
  });

  it('does not query a WABA outside the currently validated app grant', async () => {
    process.env.META_APP_ID = 'fake-id';
    process.env.META_APP_SECRET = 'fake-secret';
    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
      { scope: 'whatsapp_business_management', target_ids: ['123456'] },
      { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
    ] } }) });
    vi.stubGlobal('fetch', fetchFake);
    await expect(new MetaHttpClient().confirmarNumero('654321', '987654321', 'candidate')).resolves.toBeNull();
    expect(fetchFake).toHaveBeenCalledTimes(1);
  });

  it.each([
    ['register', 'registrarNumero'],
    ['subscription', 'inscreverWaba'],
  ] as const)('requires an explicit provider success acknowledgement for %s', async (_label, method) => {
    const client = new MetaHttpClient();
    for (const response of [
      { success: false },
      {},
    ]) {
      vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: async () => response }));
      await expect(method === 'registrarNumero'
        ? client.registrarNumero('phone-id', '123456', 'scoped-token')
        : client.inscreverWaba('waba-id', 'scoped-token')).rejects.toBeInstanceOf(MetaIndisponivelError);
    }
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: async () => ({ success: true }) }));
    await expect(method === 'registrarNumero'
      ? client.registrarNumero('phone-id', '123456', 'scoped-token')
      : client.inscreverWaba('waba-id', 'scoped-token')).resolves.toBeUndefined();
  });
});

```

## Frozen file: api-app/src/integrations/meta/meta.client.ts

Original SHA-256: `e355cde3a8708723193035659ef89d3ae640c5746dc76f50a623f7c899a500c8`; bytes:9361.

```text
import { Injectable } from '@nestjs/common';

export const META_CLIENT = Symbol('META_CLIENT');

export interface MetaNumber {
  id: string;
  telefone: string | null;
  nomeVerificado: string | null;
}

export interface MetaCapabilities {
  appId: string | null;
  configId: string | null;
  graphVersion: string;
  available: boolean;
  reason: 'AVAILABLE' | 'NOT_CONFIGURED' | 'PARTIAL_CONFIGURATION';
}

/** Every customer operation is explicitly scoped to a decrypted channel token. */
export interface MetaClient {
  configurado(): boolean;
  capabilities(): MetaCapabilities;
  exchangeCode(code: string): Promise<{ accessToken: string }>;
  recursos(accessToken: string, wabaId?: string, after?: string): Promise<{ wabas: Array<{ id: string; name: string | null }>; numbers: MetaNumber[]; next: string | null }>;
  numerosDaWaba(wabaId: string, accessToken?: string, after?: string): Promise<{ data: MetaNumber[]; next: string | null }>;
  confirmarNumero(wabaId: string, phoneNumberId: string, accessToken: string, after?: string): Promise<MetaNumber | null>;
  registrarNumero(phoneNumberId: string, pin: string, accessToken: string): Promise<void>;
  inscreverWaba(wabaId: string, accessToken: string): Promise<void>;
  enviarTexto(phoneNumberId: string, para: string, texto: string, accessToken?: string): Promise<string | null>;
}

export class MetaIndisponivelError extends Error {
  readonly code = 'META_INDISPONIVEL';
  constructor(readonly detalhe = 'A Meta recusou a operação.') { super(detalhe); }
}

@Injectable()
export class MetaHttpClient implements MetaClient {
  private readonly appId = process.env.META_APP_ID ?? '';
  private readonly appSecret = process.env.META_APP_SECRET ?? '';
  private readonly configId = process.env.META_SIGNUP_CONFIG_ID ?? '';
  private readonly graphVersion = process.env.GRAPH_VERSION ?? 'v21.0';

  capabilities(): MetaCapabilities {
    const configured = [this.appId, this.appSecret, this.configId].filter(Boolean).length;
    return {
      appId: this.appId || null,
      configId: this.configId || null,
      graphVersion: this.graphVersion,
      available: configured === 3,
      reason: configured === 3 ? 'AVAILABLE' : configured === 0 ? 'NOT_CONFIGURED' : 'PARTIAL_CONFIGURATION',
    };
  }

  /** Compatibility probe for callers being retired; never supplies a credential. */
  configurado(): boolean { return this.capabilities().available; }

  async exchangeCode(code: string): Promise<{ accessToken: string }> {
    if (!this.capabilities().available) throw new MetaIndisponivelError('Autorização Meta indisponível.');
    const body = new URLSearchParams({
      client_id: this.appId,
      client_secret: this.appSecret,
      code,
    });
    const result = await this.request('/oauth/access_token', undefined, 'POST', body);
    const accessToken = typeof result.access_token === 'string' ? result.access_token : '';
    if (!accessToken) throw new MetaIndisponivelError('A Meta não concluiu a autorização.');
    await this.validateAccessToken(accessToken);
    return { accessToken };
  }

  async recursos(accessToken: string, wabaId?: string, after?: string) {
    if (!accessToken) throw new MetaIndisponivelError('Credencial scoped do canal necessária.');
    const data = await this.debugToken(accessToken);
    this.assertCurrentGrant(data);
    const wabas = wabaTargets(data);
    if (!wabaId) return { wabas: wabas.slice(0, 100).map((id) => ({ id, name: null })), numbers: [], next: null };
    if (!wabas.includes(wabaId)) throw new MetaIndisponivelError('WABA não pertence à autorização atual.');
    const page = await this.numerosDaWaba(wabaId, accessToken, after);
    return { wabas: [{ id: wabaId, name: null }], numbers: page.data.slice(0, 100), next: page.next };
  }

  private async validateAccessToken(accessToken: string) {
    const data = await this.debugToken(accessToken);
    this.assertCurrentGrant(data);
  }

  private assertCurrentGrant(data: Record<string, unknown>) {
    const scopes = new Set([...(data.scopes as string[] ?? []), ...(data.granular_scopes as Array<{ scope?: string }> ?? []).map((scope) => scope.scope ?? '')]);
    if (data.app_id !== this.appId || data.is_valid !== true || !scopes.has('whatsapp_business_management') || !scopes.has('whatsapp_business_messaging') || wabaTargets(data).length === 0) {
      throw new MetaIndisponivelError('A autorização não concede identidade e escopos Meta necessários.');
    }
  }

  private async debugToken(inputToken: string) {
    const query = new URLSearchParams({ input_token: inputToken });
    const response = await this.request(`/debug_token?${query.toString()}`, `${this.appId}|${this.appSecret}`);
    return (response.data ?? {}) as Record<string, unknown>;
  }

  async numerosDaWaba(wabaId: string, accessToken: string, after?: string) {
    if (!accessToken) throw new MetaIndisponivelError('Credencial scoped do canal necessária.');
    const url = new URL(`/${encodeURIComponent(wabaId)}/phone_numbers`, `https://graph.facebook.com/${this.graphVersion}`);
    url.searchParams.set('fields', 'id,display_phone_number,verified_name');
    url.searchParams.set('limit', '100');
    if (after) url.searchParams.set('after', after);
    const result = await this.request(url.pathname + url.search, accessToken);
    const payload = result as { data?: Array<Record<string, unknown>>; paging?: { next?: string; cursors?: { after?: string } } };
    const data = (payload.data ?? []).flatMap((row) => {
      if (typeof row.id !== 'string') return [];
      const digits = typeof row.display_phone_number === 'string' ? row.display_phone_number.replace(/\D/g, '') : '';
      return [{ id: row.id, telefone: digits || null, nomeVerificado: typeof row.verified_name === 'string' ? row.verified_name : null }];
    });
    return { data, next: payload.paging?.cursors?.after ?? null };
  }

  async confirmarNumero(wabaId: string, phoneNumberId: string, accessToken: string, after?: string) {
    const grant = await this.debugToken(accessToken);
    this.assertCurrentGrant(grant);
    const targets = wabaTargets(grant);
    if (!targets.includes(wabaId)) return null;
    const page = await this.numerosDaWaba(wabaId, accessToken, after);
    return page.data.find((item) => item.id === phoneNumberId) ?? null;
  }

  async registrarNumero(phoneNumberId: string, pin: string, accessToken: string) {
    const result = await this.request(`/${encodeURIComponent(phoneNumberId)}/register`, accessToken, 'POST', { messaging_product: 'whatsapp', pin });
    if (result.success !== true) throw new MetaIndisponivelError('A Meta não confirmou o registro do número.');
  }

  async inscreverWaba(wabaId: string, accessToken: string) {
    const result = await this.request(`/${encodeURIComponent(wabaId)}/subscribed_apps`, accessToken, 'POST', {});
    if (result.success !== true) throw new MetaIndisponivelError('A Meta não confirmou a inscrição do webhook.');
  }

  async enviarTexto(phoneNumberId: string, para: string, texto: string, accessToken: string) {
    if (!accessToken) throw new MetaIndisponivelError('Credencial scoped do canal necessária.');
    const result = await this.request(`/${encodeURIComponent(phoneNumberId)}/messages`, accessToken, 'POST', {
      messaging_product: 'whatsapp', to: para, type: 'text', text: { body: texto },
    }) as { messages?: Array<{ id?: string }> };
    return result.messages?.[0]?.id ?? null;
  }

  private async request(path: string, accessToken?: string, method: 'GET' | 'POST' = 'GET', body?: unknown) {
    const headers: Record<string, string> = { accept: 'application/json' };
    if (accessToken) headers.authorization = `Bearer ${accessToken}`;
    if (body instanceof URLSearchParams) headers['content-type'] = 'application/x-www-form-urlencoded';
    else if (body !== undefined) headers['content-type'] = 'application/json';
    let response: Response;
    try {
      response = await fetch(`https://graph.facebook.com/${this.graphVersion}${path}`, {
        method, headers, body: body instanceof URLSearchParams ? body.toString() : body === undefined ? undefined : JSON.stringify(body),
        signal: AbortSignal.timeout(10_000),
      });
    } catch {
      throw new MetaIndisponivelError('A Meta está temporariamente indisponível.');
    }
    const payload = await response.json().catch(() => ({})) as Record<string, unknown>;
    if (!response.ok) throw new MetaIndisponivelError('A Meta recusou a operação.');
    return payload;
  }
}

function wabaTargets(data: Record<string, unknown>): string[] {
  const granular = Array.isArray(data.granular_scopes) ? data.granular_scopes as Array<{ scope?: string; target_ids?: string[] }> : [];
  const byScope = new Map<string, Set<string>>();
  for (const item of granular) {
    if (!['whatsapp_business_management', 'whatsapp_business_messaging'].includes(item.scope ?? '')) continue;
    const targets = byScope.get(item.scope!) ?? new Set<string>();
    for (const id of item.target_ids ?? []) if (/^\d{5,}$/.test(id)) targets.add(id);
    byScope.set(item.scope!, targets);
  }
  const management = byScope.get('whatsapp_business_management') ?? new Set<string>();
  const messaging = byScope.get('whatsapp_business_messaging') ?? new Set<string>();
  return [...management].filter((id) => messaging.has(id)).slice(0, 100);
}

```

## Frozen file: api-app/src/surfaces/bff/bff.module.ts

Original SHA-256: `1addd7e3cb12d6607d488b17734d4ae85eeb2ec0ae951c7ecaebd65d35c09203`; bytes:5345.

```text
import { MiddlewareConsumer, Module, NestModule, RequestMethod } from '@nestjs/common';
import { AccessService } from '../../domain/access/access.service';
import { IdentityService } from '../../domain/identity/identity.service';
import { LoginAttemptService } from '../../domain/identity/login-attempt.service';
import { PasswordService } from '../../domain/identity/password.service';
import { SessionService } from '../../infra/session/session.service';
import { ChannelsService } from '../../domain/channels/channels.service';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
import { NumberRegistrationService } from '../../domain/channels/number-registration.service';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { NumberRegistrationsController } from './number-registrations.controller';
import { ConversationsService } from '../../domain/inbox/conversations.service';
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
import { EVOLUTION_CLIENT, EvolutionHttpClient } from '../../integrations/evolution/evolution.client';
import { META_CLIENT, MetaHttpClient } from '../../integrations/meta/meta.client';
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

/**
 * Superfície BFF (ADR-0006): o que as telas consomem, autenticado por sessão.
 *
 * O middleware é montado no PREFIXO. É isso que faz o guard ser da superfície e
 * não da rota, e é o que impede o defeito que já mordeu os dois sistemas: no
 * Hub, um router.use(requireAuth) sem path interceptou o webhook público.
 */
@Module({
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
  ],
  providers: [
    SessionService,
    IdentityService,
    PasswordService,
    LoginAttemptService,
    AccessService,
    ChannelsService,
    ChannelCredentialResolver,
    NumberRegistrationService,
    MessageAcceptanceService,
    ConversationsService,
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
    { provide: META_CLIENT, useClass: MetaHttpClient },
    { provide: EVOLUTION_CLIENT, useClass: EvolutionHttpClient },
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

## Frozen file: api-app/src/surfaces/bff/channels.controller.ts

Original SHA-256: `773bbb76dc1377b29430f6b5d6e43e9568b24a5e61121b1ca3237cee9f7641f1`; bytes:6531.

```text
import { BadRequestException, Body, Controller, Delete, Get, HttpCode, HttpException, Param, Post, Req, UnauthorizedException } from '@nestjs/common';
import type { Request } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { ChannelsService, TipoDeCanal } from '../../domain/channels/channels.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ModulosService } from '../../domain/produto/modulos.service';
import { ChaveDoCatalogo } from '../../domain/historico/catalogo';
import { RegistroDeAtividade } from '../../domain/historico/registro.service';
import { SessionService } from '../../infra/session/session.service';
import { createHash } from 'node:crypto';

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
    private readonly sessions: SessionService,
  ) {}

  @Get()
  async listar(@Param('buId') buId: string, @Req() req: Request) {
    // Ver os canais é leitura: basta estar no escopo.
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    const canais = await this.prisma.buChannel.findMany({
      where: { buId },
      select: {
        id: true, type: true, status: true, generation: true, currentAttemptId: true,
        ownNumberVerified: true, providerConnectionState: true, receiptVerifiedAt: true,
        requiresWindow: true, connectedAt: true,
      },
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
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ADMIN');
    const tipo = String(body?.tipo ?? '').toUpperCase().replace('-', '_');
    if (tipo === 'NAO_OFICIAL') await this.modulos.exigir(req.usuario!.mantenedoraId, 'canalNaoOficial');
    void body;
    throw new HttpException({ error: 'Use POST /api/bff/number-registrations para iniciar o cadastro.', code: 'USE_NUMBER_REGISTRATIONS' }, 409);
  }

  /** QR de pareamento — só o canal não oficial tem. */
  @Get('nao-oficial/qr')
  async qr(@Param('buId') buId: string, @Req() req: Request) {
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ADMIN');
    throw new HttpException({ error: 'Use POST /api/bff/business-units/:buId/channels/nao-oficial/pair para iniciar ou renovar o pareamento.', code: 'QR_GET_REMOVED' }, 405);
  }

  @Post('nao-oficial/pair')
  @HttpCode(200)
  async pair(
    @Param('buId') buId: string,
    @Body() body: Record<string, unknown>,
    @Req() req: Request,
  ) {
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ADMIN');
    await this.modulos.exigir(req.usuario!.mantenedoraId, 'canalNaoOficial');
    const keys = Object.keys(body ?? {});
    if (!body || typeof body !== 'object' || Array.isArray(body)
      || !keys.includes('intent') || keys.some((key) => !['intent', 'expectedGeneration'].includes(key))
      || !['INITIAL', 'RENEW'].includes(String(body.intent))
      || (body.expectedGeneration !== undefined && (!Number.isSafeInteger(body.expectedGeneration) || Number(body.expectedGeneration) < 1))) {
      throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    }
    const cookieSession = this.sessions.extrairDoCabecalho(req.headers.cookie);
    const actor = { userId: req.usuario!.id, mantenedoraId: req.usuario!.mantenedoraId, sessionHash: createHash('sha256').update(cookieSession ?? '').digest('hex') };
    return this.channels.parearNaoOficial(buId, body.intent as 'INITIAL' | 'RENEW', body.expectedGeneration as number | undefined, () => this.revalidar(req, buId), actor);
  }

  @Post(':tipo/verify')
  @HttpCode(200)
  async verificar(@Param('buId') buId: string, @Param('tipo') tipoParam: string, @Req() req: Request) {
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ADMIN');
    const tipo = tipoParam.toUpperCase().replace('-', '_') as TipoDeCanal;
    if (!TIPOS.includes(tipo)) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    if (tipo === 'NAO_OFICIAL') await this.modulos.exigir(req.usuario!.mantenedoraId, 'canalNaoOficial');
    return this.channels.verificar(buId, tipo, () => this.revalidar(req, buId));
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

  private async revalidar(req: Request, buId: string): Promise<void> {
    const claims = this.sessions.verificar(this.sessions.extrairDoCabecalho(req.headers.cookie));
    const user = claims ? await this.prisma.appUser.findUnique({ where: { id: claims.uid }, select: { id: true, status: true, passwordChangedAt: true } }) : null;
    if (!claims || !user || user.status !== 'ATIVO' || (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat)) {
      throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    }
    await exigirPapelNaBu(this.access, user.id, buId, 'ADMIN');
  }
}

```

## Frozen file: api-app/src/surfaces/bff/me.controller.ts

Original SHA-256: `0edd826d4e9a3c0b8cde4334bf2e88f360f5f5e9d5db99e5dfc4382b5bf71bb0`; bytes:9442.

```text
import {
  BadRequestException,
  Body,
  Controller,
  ForbiddenException,
  Get,
  HttpCode,
  NotFoundException,
  Param,
  Patch,
  Post,
  Req,
  Res,
} from '@nestjs/common';
import type { Request, Response } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { atLeast } from '../../domain/access/role';
import { TenancyService } from '../../domain/tenancy/tenancy.service';
import { IdentityService } from '../../domain/identity/identity.service';
import { PasswordService } from '../../domain/identity/password.service';
import { SessionService } from '../../infra/session/session.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ModulosService } from '../../domain/produto/modulos.service';
import { SetorService } from '../../domain/setor/setor.service';
import { ator } from './setores.controller';

@Controller('api/bff/me')
export class MeController {
  constructor(
    private readonly access: AccessService,
    private readonly identity: IdentityService,
    private readonly passwords: PasswordService,
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
    private readonly modulos: ModulosService,
  ) {}

  @Get()
  async me(@Req() req: Request) {
    const u = req.usuario!;
    const mantenedora = await this.prisma.mantenedora.findUnique({
      where: { id: u.mantenedoraId },
      select: { id: true, name: true },
    });

    return {
      id: u.id,
      nome: u.nome,
      email: u.email,
      precisaTrocarSenha: u.precisaTrocarSenha,
      mantenedora,
      // Papel na Mantenedora é CALCULADO a cada leitura, nunca armazenado.
      papel: await this.access.papelNaMantenedoraDoUsuario(u.id, u.mantenedoraId),
      escopo: await this.access.escopo(u.id),
      // O que ESTA instalação e ESTA Mantenedora oferecem, já interseccionado
      // (ADR-0016 §6). O front monta o roteador a partir daqui: módulo desligado
      // não é escondido por CSS, a rota não é montada.
      produto: await this.modulos.produto(u.mantenedoraId),
      ...(await this.identity.perfil(u.id)),
    };
  }

  /**
   * O perfil da própria pessoa (o "Meu perfil" do desenho).
   *
   * **O e-mail não é editável aqui.** Ele é a identidade de login, único dentro
   * da Mantenedora (ADR-0008 §3), e trocá-lo por conta própria é trocar de quem
   * se é — não é ajuste de cadastro. Quem muda é `ADMIN`, pela tela de Pessoas.
   */
  @Patch()
  async atualizarPerfil(
    @Body() body: { nome?: string; telefone?: string; avatar?: string | null },
    @Req() req: Request,
  ) {
    const nome = typeof body?.nome === 'string' ? body.nome.trim() : undefined;
    if (nome !== undefined && !nome) {
      throw new BadRequestException({ error: 'O nome não pode ficar vazio.', code: 'PAYLOAD_INVALIDO' });
    }
    return this.identity.atualizarPerfil(req.usuario!.id, {
      nome,
      telefone: typeof body?.telefone === 'string' ? body.telefone.trim() : undefined,
      avatar: body?.avatar === null || typeof body?.avatar === 'string' ? body.avatar : undefined,
    });
  }

  @Post('password')
  @HttpCode(200)
  async trocarSenha(
    @Body() body: { atual?: string; nova?: string },
    @Req() req: Request,
    @Res({ passthrough: true }) res: Response,
  ) {
    const u = req.usuario!;
    const atual = String(body?.atual ?? '');
    const nova = String(body?.nova ?? '');

    const invalida = this.passwords.invalida(nova);
    if (invalida) {
      res.status(400);
      return { error: invalida, code: 'SENHA_INVALIDA' };
    }
    if (atual === nova) {
      res.status(400);
      return { error: 'A nova senha precisa ser diferente da atual.', code: 'SENHA_INVALIDA' };
    }

    const ok = await this.identity.trocarPropriaSenha(u.id, atual, nova);
    if (!ok) {
      res.status(400);
      return { error: 'A senha atual está incorreta.', code: 'CREDENCIAL_INVALIDA' };
    }

    // Trocar a PRÓPRIA senha não entra no catálogo (ADR-0022 §2): é ato sobre si
    // mesmo, e `password_changed_at` testemunha. Redefinir a senha DE OUTRO
    // entra — é poder exercido sobre terceiro.

    // A troca derruba as sessões anteriores; esta ganha cookie novo para quem
    // trocou continuar logado aqui e cair nos outros dispositivos.
    res.setHeader('Set-Cookie', this.sessions.cookie(this.sessions.assinar(u.id)));
    return { ok: true };
  }
}

@Controller('api/bff/business-units')
export class BusinessUnitsController {
  constructor(
    private readonly access: AccessService,
    private readonly prisma: PrismaService,
    private readonly tenancy: TenancyService,
    private readonly setores: SetorService,
  ) {}

  /**
   * Conectar um número novo é ação da Mantenedora, então exige papel ADMIN
   * **nela** — que é calculado, e só existe para quem tem ADMIN em todas as BUs.
   */
  @Post()
  @HttpCode(201)
  async criar(@Body() body: { nome?: string; telefone?: string; setorId?: string }, @Req() req: Request) {
    const papel = await this.access.papelNaMantenedoraDoUsuario(req.usuario!.id, req.usuario!.mantenedoraId);
    if (!papel || !atLeast(papel, 'ADMIN')) {
      throw new ForbiddenException({
        error: 'Esta ação exige papel ADMIN na Mantenedora.',
        code: 'PAPEL_INSUFICIENTE',
      });
    }
    const nome = String(body?.nome ?? '').trim();
    if (!nome) throw new BadRequestException({ error: 'Dê um nome à Business Unit.', code: 'PAYLOAD_INVALIDO' });

    const r = await this.tenancy.criarBusinessUnit(
      req.usuario!.mantenedoraId,
      nome,
      body?.telefone,
      body?.setorId,
      ator(req),
    );
    return { id: r.bu.id, nome: r.bu.name, setor: { id: r.setor.id, nome: r.setor.name }, herdaramGrant: r.herdaram };
  }

  /** Só as BUs do escopo do usuário. Sem grant, lista vazia — nunca "todas". */
  @Get()
  async listar(@Req() req: Request) {
    const escopo = await this.access.escopo(req.usuario!.id);
    const bus = await this.prisma.businessUnit.findMany({
      where: { id: { in: escopo }, status: 'ATIVO' },
      select: {
        id: true,
        name: true,
        phone: true,
        setor: { select: { id: true, name: true } },
        channels: { select: {
          id: true, type: true, status: true, generation: true, currentAttemptId: true,
          ownNumberVerified: true, providerConnectionState: true, receiptVerifiedAt: true,
          requiresWindow: true, connectedAt: true,
        } },
      },
      orderBy: { name: 'asc' },
    });
    const grants = await this.access.grantsDoUsuario(req.usuario!.id);
    const roles = new Map(grants.map((grant) => [grant.buId, grant.role]));
    return { businessUnits: bus.map((bu) => ({ ...bu, papel: roles.get(bu.id) ?? null })) };
  }

  /** Renomear ou inativar o número. Inativar NÃO apaga: a BU é dona das conversas. */
  @Patch(':buId')
  async atualizar(
    @Param('buId') buId: string,
    @Body() body: { nome?: string; status?: 'ATIVO' | 'INATIVO' },
    @Req() req: Request,
  ) {
    const papel = await this.access.papelNaMantenedoraDoUsuario(req.usuario!.id, req.usuario!.mantenedoraId);
    if (!papel || !atLeast(papel, 'ADMIN')) {
      throw new ForbiddenException({
        error: 'Esta ação exige papel ADMIN na Mantenedora.',
        code: 'PAPEL_INSUFICIENTE',
      });
    }
    return this.tenancy.atualizarBusinessUnit(req.usuario!.mantenedoraId, buId, body ?? {}, ator(req));
  }

  /**
   * Mover o número de setor — a única escrita que reescreve permissão de gente
   * que não está na requisição (ADR-0017 §2, regra 5).
   */
  @Post(':buId/setor')
  async moverDeSetor(
    @Param('buId') buId: string,
    @Body() body: { setorId?: string },
    @Req() req: Request,
  ) {
    const papel = await this.access.papelNaMantenedoraDoUsuario(req.usuario!.id, req.usuario!.mantenedoraId);
    if (!papel || !atLeast(papel, 'ADMIN')) {
      throw new ForbiddenException({
        error: 'Esta ação exige papel ADMIN na Mantenedora.',
        code: 'PAPEL_INSUFICIENTE',
      });
    }
    const r = await this.setores.moverNumero(req.usuario!.mantenedoraId, buId, String(body?.setorId ?? ''), ator(req));
    return { setor: { id: r.setor.id, nome: r.setor.name }, concedidas: r.movidas, revogadas: r.removidas };
  }

  /**
   * BU fora do escopo responde 404, não 403 — inclusive quando ela é de outra
   * Mantenedora. Um 403 confirmaria a quem varre identificadores que o recurso
   * existe, só que alheio.
   */
  @Get(':buId')
  async detalhe(@Param('buId') buId: string, @Req() req: Request) {
    const bu = await this.access.resolverBu(req.usuario!.id, buId);
    if (!bu) throw new NotFoundException({ error: 'Não encontrado.', code: 'NAO_ENCONTRADO' });

    const canais = await this.prisma.buChannel.findMany({
      where: { buId: bu.id },
      select: {
        id: true, type: true, status: true, generation: true, currentAttemptId: true,
        ownNumberVerified: true, providerConnectionState: true, receiptVerifiedAt: true,
        requiresWindow: true, connectedAt: true,
      },
    });
    return { id: bu.id, nome: bu.name, papel: bu.papel, canais };
  }
}

```

## Frozen file: api-app/src/surfaces/bff/number-registrations.controller.ts

Original SHA-256: `c57797667ff26a4ea74aa939e4972a8cd8f442c9beafa166b1bdf808e19c236e`; bytes:5003.

```text
import { BadRequestException, Body, Controller, Get, Headers, HttpCode, Param, Post, Query, Req } from '@nestjs/common';
import type { Request } from 'express';
import { createHash } from 'node:crypto';
import { NumberRegistrationService, CreateRegistrationInput } from '../../domain/channels/number-registration.service';
import { SessionService } from '../../infra/session/session.service';

const exact = (value: unknown, required: string[], optional: string[] = []) => {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
  const keys = Object.keys(value as object);
  if (required.some((key) => !keys.includes(key)) || keys.some((key) => !required.includes(key) && !optional.includes(key))) {
    throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
  }
};

@Controller('api/bff/number-registrations')
export class NumberRegistrationsController {
  constructor(private readonly registrations: NumberRegistrationService, private readonly sessions: SessionService) {}

  @Get('capabilities') capabilities(@Req() req: Request) { return this.registrations.capabilities(req.usuario!.mantenedoraId); }

  @Post()
  @HttpCode(201)
  async create(@Body() body: Record<string, unknown>, @Headers('idempotency-key') key: string, @Req() req: Request) {
    const actor = this.actor(req);
    await this.registrations.authorizeCreateScope(actor, body);
    if (typeof body?.novaBu === 'object' && body.novaBu !== null) exact(body.novaBu, ['nome'], ['setorId']);
    exact(body, ['tipo', 'operation'], ['buId', 'novaBu', 'channelId', 'expectedGeneration']);
    return this.registrations.create(actor, createHash('sha256').update(actor.sessionToken).digest('hex'), key, body as unknown as CreateRegistrationInput);
  }

  @Get(':id') get(@Param('id') id: string, @Req() req: Request) { return this.registrations.get(this.actor(req), id); }

  @Post(':id/authorize')
  @HttpCode(200)
  async authorize(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    const actor = this.actor(req);
    await this.registrations.get(actor, id);
    exact(body, ['nonce', 'code']);
    if (typeof body.nonce !== 'string' || body.nonce.length < 32 || body.nonce.length > 128 || typeof body.code !== 'string' || body.code.length < 1 || body.code.length > 4096) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    const digest = createHash('sha256').update(actor.sessionToken).digest('hex');
    return this.registrations.authorize(actor, id, digest, body.nonce, body.code);
  }

  @Get(':id/options') async options(@Param('id') id: string, @Query() query: Record<string, string>, @Req() req: Request) {
    const actor = this.actor(req);
    await this.registrations.get(actor, id);
    exact(query, [], ['wabaId', 'after']);
    const wabaId = query.wabaId;
    const after = query.after;
    if ((after !== undefined && (after.length < 1 || after.length > 512)) || (wabaId !== undefined && !/^\d{5,}$/.test(wabaId))) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    return this.registrations.options(actor, id, wabaId, after);
  }

  @Post(':id/confirm') @HttpCode(200)
  async confirm(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    const actor = this.actor(req);
    await this.registrations.get(actor, id);
    exact(body, ['wabaId', 'phoneNumberId', 'modoRegistro'], ['pin', 'after']);
    if (typeof body.wabaId !== 'string' || typeof body.phoneNumberId !== 'string' || typeof body.modoRegistro !== 'string' || (body.pin !== undefined && typeof body.pin !== 'string') || (body.after !== undefined && typeof body.after !== 'string')) throw new BadRequestException({ code: 'PAYLOAD_INVALIDO' });
    return this.registrations.confirm(actor, id, body as { wabaId: string; phoneNumberId: string; modoRegistro: 'NOVO' | 'JA_REGISTRADO'; pin?: string; after?: string });
  }

  @Post(':id/advance') @HttpCode(200) async advance(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) { const actor = this.actor(req); await this.registrations.get(actor, id); exact(body, []); return this.registrations.advance(actor, id); }
  @Post(':id/retry') @HttpCode(200) async retry(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) { const actor = this.actor(req); await this.registrations.get(actor, id); exact(body, []); return this.registrations.retry(actor, id); }
  @Post(':id/cancel') @HttpCode(200) async cancel(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) { const actor = this.actor(req); await this.registrations.get(actor, id); exact(body, []); return this.registrations.cancel(actor, id); }

  private actor(req: Request) { return { id: req.usuario!.id, mantenedoraId: req.usuario!.mantenedoraId, nome: req.usuario!.nome, email: req.usuario!.email, sessionToken: this.sessions.extrairDoCabecalho(req.headers.cookie) ?? '' }; }
}

```

## Frozen file: api-app/src/surfaces/public/public.module.ts

Original SHA-256: `b4fc1da7caadb9e8edb0d719b11783227aa35ee55853f4d0e9f1e06065603936`; bytes:1636.

```text
import { MiddlewareConsumer, Module, NestModule, RequestMethod } from '@nestjs/common';
import { ApiKeyService } from '../../domain/integration/api-key.service';
import { RateLimitService } from '../../domain/integration/rate-limit.service';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { EVOLUTION_CLIENT, EvolutionHttpClient } from '../../integrations/evolution/evolution.client';
import { META_CLIENT, MetaHttpClient } from '../../integrations/meta/meta.client';
import { ApiKeyMiddleware } from './api-key.middleware';
import { PublicConversationsController } from './conversations.controller';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';

/**
 * Superfície pública (ADR-0010): `/api/v1` no host novo, chave `lh_` da
 * Mantenedora. É o único contrato **versionado** — quebra dele é conversa com um
 * terceiro, não refatoração.
 */
@Module({
  controllers: [PublicConversationsController],
  providers: [
    ApiKeyService,
    RateLimitService,
    ConversationsService,
    MessageAcceptanceService,
    ChannelCredentialResolver,
    { provide: META_CLIENT, useClass: MetaHttpClient },
    { provide: EVOLUTION_CLIENT, useClass: EvolutionHttpClient },
  ],
  exports: [ApiKeyService],
})
export class PublicApiModule implements NestModule {
  configure(consumer: MiddlewareConsumer): void {
    consumer.apply(ApiKeyMiddleware).forRoutes({ path: 'api/v1/{*path}', method: RequestMethod.ALL });
  }
}

```

## Frozen file: api-app/src/surfaces/webhooks/evolution.controller.ts

Original SHA-256: `156f96ed98e332b0469acd85b2101f2153bcdbfc28917057b8785ac67a5f1a7d`; bytes:7904.

```text
import { Body, Controller, ForbiddenException, HttpCode, Param, Post } from '@nestjs/common';
import { timingSafeEqual } from 'node:crypto';
import { IncomingService } from '../../domain/inbox/incoming.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { ServiceUnavailableException, ConflictException } from '@nestjs/common';

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
    private readonly acceptance: MessageAcceptanceService,
  ) {}

  @Post(':segredo')
  @HttpCode(200)
  async receber(@Param('segredo') segredo: string, @Body() body: EvolutionEvent) {
    this.exigirSegredo(segredo);

    const evento = body?.event;
    const instancia = body?.instance;
    if (!evento || !instancia) return { received: true };

    const identity = await this.prisma.providerResourceIdentity.findUnique({
      where: { provider_externalResourceId: { provider: 'NAO_OFICIAL', externalResourceId: instancia } },
      include: { currentChannel: true },
    });
    const canal = identity?.currentChannel;
    if (!identity || !canal || canal.evolutionInstanceName !== instancia) return { received: true };
    const context = { providerResourceIdentityId: identity.id, buId: identity.buId, channelId: canal.id, generation: canal.generation, pairingEpoch: canal.pairingEpoch, channelOrigin: 'NAO_OFICIAL' as const };
    if (canal.ownNumberVerified && canal.verifiedEpoch === canal.pairingEpoch) {
      await this.acceptance.persistVerifiedDiagnostic(context, evento, { instance: instancia, data: body.data });
    } else {
      const metadata = evento === 'connection.update' ? (body.data as ConnectionData | undefined)?.state : 'PENDING_IDENTITY';
      await this.acceptance.persistCurrentResourceMetadata(context, evento, { instance: instancia, state: typeof metadata === 'string' ? metadata.slice(0, 40) : 'PENDING_IDENTITY' });
    }

    // Os nomes de evento vêm em minúsculo com ponto no payload ENTREGUE, e em
    // maiúsculo com underscore quando são REGISTRADOS. São strings diferentes
    // para a mesma coisa — o parser do Hub já comparou contra o formato errado
    // uma vez (hub-whatsapp/docs/evolution-api-payloads.md).
    switch (evento) {
      case 'messages.upsert':
        if (!canal.ownNumberVerified || canal.verifiedEpoch !== canal.pairingEpoch) throw new ServiceUnavailableException({ code: 'PENDING_IDENTITY' });
        await this.tratarMensagem(context, body.data as UpsertData);
        break;
      case 'connection.update':
        await this.tratarConexao(context, body.data as ConnectionData);
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

  private async tratarMensagem(context: { buId: string; channelId: string; providerResourceIdentityId: string; generation: number; pairingEpoch: number }, data: UpsertData | undefined): Promise<void> {
    const jid = data?.key?.remoteJid;
    if (!jid) return;

    const ehGrupo = jid.endsWith('@g.us');
    if (!ehGrupo && !jid.endsWith('@s.whatsapp.net')) return; // LID identity is ambiguous; never extract digits from @lid.
    if (!data?.key?.id?.trim()) return;
    const daGente = Boolean(data?.key?.fromMe);
    const texto = data?.message?.conversation ?? data?.message?.extendedTextMessage?.text ?? '';

    // `pushName` é o nome de QUEM MANDOU aquela mensagem, não o nome do contato
    // da conversa. Numa mensagem nossa ele é o nome do próprio número — usá-lo
    // aqui é o bug que troca o nome do contato pelo do responsável (corrigido
    // no Hub em 756bd91, e não repetido aqui).
    const nome = !ehGrupo && !daGente ? (data?.pushName ?? null) : null;

    await this.incoming.registrar({
      buId: context.buId,
      canal: 'NAO_OFICIAL',
      // O JID é detalhe de transporte e não entra no domínio (ADR-0009 §1).
      contato: ehGrupo ? jid : jid.split('@')[0],
      ehGrupo,
      nomeExibicao: nome,
      direcao: daGente ? 'OUT' : 'IN',
      tipo: 'TEXTO',
      conteudo: texto,
      externalId: data?.key?.id ?? null,
      providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId,
      generation: context.generation,
      pairingEpoch: context.pairingEpoch,
    });
  }

  private async tratarConexao(context: { channelId: string; providerResourceIdentityId: string; buId: string; generation: number; pairingEpoch: number }, data: ConnectionData | undefined): Promise<void> {
    const estado = data?.state;
    if (!['open', 'connecting', 'close'].includes(estado ?? '')) return;
    await this.prisma.$transaction(async (tx) => {
      const rows = await tx.$queryRaw<Array<{ id: string }>>`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} AND current_channel_id = ${context.channelId} AND bu_id = ${context.buId} FOR UPDATE`;
      if (!rows.length) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
      const channel = await tx.buChannel.findFirst({ where: { id: context.channelId, buId: context.buId, generation: context.generation, pairingEpoch: context.pairingEpoch }, select: { ownNumberVerified: true, verifiedEpoch: true, receiptVerifiedAt: true, currentAttemptId: true } });
      if (!channel) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
      const data = await tx.buChannel.updateMany({
        where: { id: context.channelId, buId: context.buId, generation: context.generation, pairingEpoch: context.pairingEpoch },
        data: { providerConnectionState: estado === 'open' ? 'CONNECTED' : estado === 'connecting' ? 'CONNECTING' : 'DISCONNECTED' },
      });
      if (!data.count) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
      if (estado === 'open' && channel.ownNumberVerified && channel.verifiedEpoch === context.pairingEpoch && channel.receiptVerifiedAt) {
        await tx.buChannel.updateMany({ where: { id: context.channelId, generation: context.generation, pairingEpoch: context.pairingEpoch }, data: { status: 'CONECTADO', connectedAt: new Date() } });
        if (channel.currentAttemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: channel.currentAttemptId, generation: context.generation, pairingEpoch: context.pairingEpoch, state: { in: ['PENDING_NUMBER', 'PENDING_RECEIPT'] } }, data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', version: { increment: 1 } } });
      }
    });
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

```

## Frozen file: api-app/src/surfaces/webhooks/meta.controller.ts

Original SHA-256: `0ce602e50bf51325f0cf41776eba2ce4f6cd84e9db3856778e8491deee7bdf9b`; bytes:6673.

```text
import { Controller, ForbiddenException, Get, HttpCode, Post, Query, Req, ServiceUnavailableException } from '@nestjs/common';
import type { RawBodyRequest } from '@nestjs/common';
import type { Request } from 'express';
import { createHmac, timingSafeEqual } from 'node:crypto';
import { IncomingService, MensagemRecebida } from '../../domain/inbox/incoming.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';

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
      const contact = (msg.from ?? '').replace(/\D/g, '');
      if (!contact) continue;
      await this.incoming.registrar({
        buId: identity.buId,
        canal: 'OFICIAL',
        contato: contact,
        ehGrupo: false,
        nomeExibicao: nome,
        direcao: 'IN',
        tipo: tipoDaMensagem(msg.type),
        conteudo: conteudoDaMensagem(msg),
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
  type?: string;
  text?: { body?: string };
  button?: { text?: string };
  interactive?: { button_reply?: { title?: string }; list_reply?: { title?: string } };
}

```

## Frozen file: api-app/src/surfaces/webhooks/webhooks.module.ts

Original SHA-256: `75cbae0a89be972e98a3b4d7b9358864b9888a1ddff91ba1ea7a4483a9bfd7ac`; bytes:1353.

```text
import { Module } from '@nestjs/common';
import { IncomingService } from '../../domain/inbox/incoming.service';
import { EvolutionWebhookController } from './evolution.controller';
import { MetaWebhookController } from './meta.controller';
import { META_CLIENT, MetaHttpClient } from '../../integrations/meta/meta.client';
import { TYPEBOT_CLIENT, TypebotHttpClient } from '../../integrations/typebot/typebot.client';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';

/**
 * Superfície de webhooks (ADR-0006): terceiros empurrando evento.
 *
 * A autenticação é POR ORIGEM e por isso NÃO existe um middleware único de
 * prefixo aqui: a Meta assina o corpo (X-Hub-Signature-256) e a Evolution não
 * assina nada, o que exige segredo no caminho. Cada controller traz a sua — é a
 * única superfície onde isso é correto, e está escrito para não parecer
 * esquecimento.
 */
@Module({
  controllers: [MetaWebhookController, EvolutionWebhookController],
  providers: [IncomingService, MessageAcceptanceService, ChannelCredentialResolver, { provide: META_CLIENT, useClass: MetaHttpClient }, { provide: TYPEBOT_CLIENT, useClass: TypebotHttpClient }],
})
export class WebhooksModule {}

```

## Frozen file: api-app/test/api-publica.e2e-spec.ts

Original SHA-256: `c880c8365a5ac6862ae176e2add24b008e4c622ac3136605a287a35257d694b4`; bytes:9039.

```text
import { INestApplication } from '@nestjs/common';
import { createHmac } from 'node:crypto';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { RateLimitService } from '../src/domain/integration/rate-limit.service';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { META_APP_SECRET, criarCanalVerificado, criarMantenedora, limparBanco, login, metaFake, subirApp } from './helpers';

describe('API pública v1', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let A: Awaited<ReturnType<typeof criarMantenedora>>;
  let B: Awaited<ReturnType<typeof criarMantenedora>>;
  let chaveA: string;

  const PHONE_A = 'phone-alfa';
  const CONTATO = '5584911112222';

  const comChave = (chave: string) => ({ Authorization: `Bearer ${chave}` });

  const criarChave = async (cookie: string, nome: string, buIds: string[] = []) => {
    const res = await request(app.getHttpServer())
      .post('/api/bff/integracao/api-keys')
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ nome, buIds })
      .expect(201);
    return res.body.chave as string;
  };

  const receber = async (texto: string) => {
    const corpo = {
      entry: [{ changes: [{ field: 'messages', value: {
        metadata: { phone_number_id: PHONE_A },
        contacts: [{ profile: { name: 'Cliente' } }],
        messages: [{ id: `wamid-${texto}`, from: CONTATO, type: 'text', text: { body: texto } }],
      } }] }],
    };
    await request(app.getHttpServer())
      .post('/webhooks/meta')
      .set('content-type', 'application/json')
      .set('x-hub-signature-256', 'sha256=' + createHmac('sha256', META_APP_SECRET).update(JSON.stringify(corpo)).digest('hex'))
      .send(corpo).expect(200);
  };

  beforeAll(async () => {
    ({ app, prisma } = await subirApp());
  });

  afterAll(async () => {
    await limparBanco(prisma);
    await app?.close();
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    app.get(RateLimitService).limpar();
    metaFake.enviados = [];
    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');
    await criarCanalVerificado(prisma, A.businessUnit.id, 'OFICIAL', PHONE_A, { requiresWindow: true });
    chaveA = await criarChave(await login(app, 'dono@alfa.test'), 'Campuzz');
    await receber('oi');
  });

  describe('autenticação pela chave', () => {
    it('a chave sai em claro UMA vez, e o prefixo é lh_', () => {
      expect(chaveA.startsWith('lh_')).toBe(true);
    });

    it('sem chave: 401 NAO_AUTENTICADO', async () => {
      const res = await request(app.getHttpServer()).get('/api/v1/accounts').expect(401);
      expect(res.body.code).toBe('NAO_AUTENTICADO');
    });

    it('cookie de sessão NÃO substitui a chave', async () => {
      const cookie = await login(app, 'dono@alfa.test');
      await request(app.getHttpServer()).get('/api/v1/accounts').set('Cookie', cookie).expect(401);
    });

    it('chave revogada responde igual a inexistente', async () => {
      const cookie = await login(app, 'dono@alfa.test');
      const lista = await request(app.getHttpServer()).get('/api/bff/integracao/api-keys').set('Cookie', cookie).expect(200);
      await request(app.getHttpServer())
        .delete(`/api/bff/integracao/api-keys/${lista.body.keys[0].id}`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').expect(204);

      const revogada = await request(app.getHttpServer()).get('/api/v1/accounts').set(comChave(chaveA)).expect(401);
      const inexistente = await request(app.getHttpServer()).get('/api/v1/accounts').set(comChave('lh_naoexiste')).expect(401);
      expect(revogada.body).toEqual(inexistente.body);
    });
  });

  describe('escopo — a Mantenedora sai da CHAVE, nunca do request', () => {
    it('escopo nulo devolve só as BUs DESTA Mantenedora', async () => {
      const res = await request(app.getHttpServer()).get('/api/v1/accounts').set(comChave(chaveA)).expect(200);
      expect(res.body.accounts).toHaveLength(1);
      expect(res.body.accounts[0].id).toBe(A.businessUnit.id);
    });

    it('CROSS-TENANT: pedir a BU de Beta com a chave de Alfa dá 403 SEM_ACESSO_A_CONTA', async () => {
      const res = await request(app.getHttpServer())
        .get(`/api/v1/conversations?account_id=${B.businessUnit.id}`)
        .set(comChave(chaveA))
        .expect(403);
      expect(res.body.code).toBe('SEM_ACESSO_A_CONTA');
    });

    it('escopo restrito não alcança outra BU da MESMA Mantenedora', async () => {
      const cookie = await login(app, 'dono@alfa.test');
      // Pelo caminho real: a BU nova HERDA a expansão, senão o dono cairia para
      // VIEWER na Mantenedora (ADR-0008 §4, regra 3).
      const nova = await request(app.getHttpServer())
        .post('/api/bff/business-units').set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ nome: 'Segunda BU' }).expect(201);
      expect(nova.body.herdaramGrant).toBe(1);

      const restrita = await criarChave(cookie, 'Restrita', [A.businessUnit.id]);

      await request(app.getHttpServer())
        .get(`/api/v1/conversations?account_id=${nova.body.id}`).set(comChave(restrita)).expect(403);
      await request(app.getHttpServer())
        .get(`/api/v1/conversations?account_id=${A.businessUnit.id}`).set(comChave(restrita)).expect(200);
    });

    it('criar chave com escopo apontando para BU de outra Mantenedora é recusado', async () => {
      const cookie = await login(app, 'dono@alfa.test');
      await request(app.getHttpServer())
        .post('/api/bff/integracao/api-keys')
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ nome: 'Maliciosa', buIds: [B.businessUnit.id] })
        .expect(400);
    });
  });

  describe('contrato', () => {
    it('conversations traz janela_aberta e datas em ISO-8601 UTC', async () => {
      const res = await request(app.getHttpServer())
        .get(`/api/v1/conversations?account_id=${A.businessUnit.id}`).set(comChave(chaveA)).expect(200);

      const c = res.body.conversations[0];
      expect(c.telefone).toBe(CONTATO);
      expect(c.janela_aberta).toBe(true);
      expect(c.ultima_em).toMatch(/^\d{4}-\d{2}-\d{2}T.*Z$/);
    });

    it('messages aceita since para sincronização incremental', async () => {
      await receber('segunda');
      const todas = await request(app.getHttpServer())
        .get(`/api/v1/conversations/${CONTATO}/messages?account_id=${A.businessUnit.id}`)
        .set(comChave(chaveA)).expect(200);
      expect(todas.body.messages).toHaveLength(2);

      const desde = todas.body.messages[0].em;
      const depois = await request(app.getHttpServer())
        .get(`/api/v1/conversations/${CONTATO}/messages?account_id=${A.businessUnit.id}&since=${desde}`)
        .set(comChave(chaveA)).expect(200);
      expect(depois.body.messages).toHaveLength(1);
    });

    it('POST messages envia e marca a conversa como atendida por EXTERNO', async () => {
      await request(app.getHttpServer())
        .post('/api/v1/messages').set(comChave(chaveA))
        .send({ account_id: A.businessUnit.id, telefone: CONTATO, texto: 'resposta do parceiro', atendente: 'Campuzz' })
        .expect(201);

      expect(metaFake.enviados).toHaveLength(1);
      const conversa = await prisma.conversation.findFirstOrThrow();
      expect(conversa.attendantOrigin).toBe('EXTERNO');
      expect(conversa.attendantName).toBe('Campuzz');
    });

    it('fora da janela, POST messages recusa com JANELA_FECHADA', async () => {
      await prisma.message.updateMany({ data: { createdAt: new Date(Date.now() - 25 * 60 * 60 * 1000) } });
      const res = await request(app.getHttpServer())
        .post('/api/v1/messages').set(comChave(chaveA))
        .send({ account_id: A.businessUnit.id, telefone: CONTATO, texto: 'tarde demais' })
        .expect(409);
      expect(res.body.code).toBe('JANELA_FECHADA');
      expect(metaFake.enviados).toHaveLength(0);
    });
  });

  describe('limite de taxa (ADR-0010 §7) — fecha o buraco de ritmo do S3', () => {
    it('estoura em 429 LIMITE_DE_TAXA com Retry-After', async () => {
      const enviar = () =>
        request(app.getHttpServer())
          .post('/api/v1/messages').set(comChave(chaveA))
          .send({ account_id: A.businessUnit.id, telefone: CONTATO, texto: 'em rajada' });

      const limite = Number(process.env.API_V1_ENVIOS_POR_MINUTO ?? 20);
      for (let i = 0; i < limite; i++) await enviar().expect(201);

      const estourou = await enviar().expect(429);
      expect(estourou.body.code).toBe('LIMITE_DE_TAXA');
      expect(estourou.headers['retry-after']).toBeTruthy();
      expect(metaFake.enviados).toHaveLength(limite);
    });
  });
});

```

## Frozen file: api-app/test/atendimento.e2e-spec.ts

Original SHA-256: `20db8f160c957c7bfffea6f88b965f9d498dc088683247c02f6aaea99ad75035`; bytes:24673.

```text
import { INestApplication } from '@nestjs/common';
import { createHmac } from 'node:crypto';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import {
  META_APP_SECRET,
  criarCanalVerificado,
  criarMantenedora,
  criarUsuario,
  evolutionFake,
  limparBanco,
  login,
  metaFake,
  subirApp,
} from './helpers';
import { lerCursorTimeline } from '../src/domain/inbox/timeline-pagination';

describe('atendimento', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let A: Awaited<ReturnType<typeof criarMantenedora>>;
  let B: Awaited<ReturnType<typeof criarMantenedora>>;
  let cookieOwner: string;
  let conversaId: string;

  const PHONE_A = 'phone-alfa';
  const CONTATO = '5584911112222';

  const receber = async (texto: string, phoneNumberId = PHONE_A) => {
    const corpo = {
      entry: [
        {
          changes: [
            {
              field: 'messages',
              value: {
                metadata: { phone_number_id: phoneNumberId },
                contacts: [{ profile: { name: 'Cliente' } }],
                messages: [{ id: `wamid-${texto}`, from: CONTATO, type: 'text', text: { body: texto } }],
              },
            },
          ],
        },
      ],
    };
    await request(app.getHttpServer())
      .post('/webhooks/meta')
      .set('content-type', 'application/json')
      .set('x-hub-signature-256', 'sha256=' + createHmac('sha256', META_APP_SECRET).update(JSON.stringify(corpo)).digest('hex'))
      .send(corpo)
      .expect(200);
  };

  const responder = (cookie: string, id: string, texto = 'oi, tudo bem?') =>
    request(app.getHttpServer())
      .post(`/api/bff/conversations/${id}/messages`)
      .set('Cookie', cookie).set('x-requested-with', 'teste')
      .send({ texto });

  beforeAll(async () => {
    ({ app, prisma } = await subirApp());
  });

  afterAll(async () => {
    await limparBanco(prisma);
    await app?.close();
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    metaFake.enviados = [];
    evolutionFake.enviados = [];
    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');
    await criarCanalVerificado(prisma, A.businessUnit.id, 'OFICIAL', PHONE_A, { requiresWindow: true });
    cookieOwner = await login(app, 'dono@alfa.test');
    await receber('oi');
    conversaId = (await prisma.conversation.findFirstOrThrow()).id;
  });

  describe('POST conversations/:id/messages — o trio (ADR-0012 §2)', () => {
    it('autorizado: responde, envia pelo canal e assume a conversa', async () => {
      const res = await responder(cookieOwner, conversaId).expect(201);
      expect(res.body.canal).toBe('OFICIAL');
      expect(metaFake.enviados).toEqual([{ para: CONTATO, texto: 'oi, tudo bem?' }]);

      const conversa = await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
      expect(conversa.status).toBe('IN_SERVICE');
      expect(conversa.attendantOrigin).toBe('INTERNO');
    });

    // Os dois testes que aqui provavam CAPACIDADE_AUSENTE e "VIEWER lê mas não
    // responde" SUMIRAM com o ADR-0018: o eixo de capacidades foi dissolvido e o
    // papel VIEWER deixou de existir. Não é cobertura perdida — é comportamento
    // que o produto não tem mais. A dívida está escrita no ADR §Negativas: quem
    // precisa acompanhar sem responder passa a ser ATENDENTE, e nada o impede de
    // responder; o substituto é o histórico de atividades (ADR-0020).

    it('ATENDENTE no escopo responde — estar na BU BASTA (ADR-0018 §3)', async () => {
      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'atendente@alfa.test', 'ATENDENTE');
      const cookie = await login(app, 'atendente@alfa.test');

      await responder(cookie, conversaId).expect(201);
      expect(metaFake.enviados).toHaveLength(1);
    });

    it('CROSS-TENANT: o dono de Beta recebe 404 na conversa da BU de Alfa', async () => {
      const cookieBeta = await login(app, 'dono@beta.test');
      const res = await responder(cookieBeta, conversaId).expect(404);
      expect(res.body.code).toBe('NAO_ENCONTRADO');
      expect(metaFake.enviados).toHaveLength(0);
      expect(B.businessUnit.id).toBeTruthy();
    });
  });

  describe('janela de 24h — atributo do CANAL (ADR-0009 §3)', () => {
    it('recusa com JANELA_FECHADA quando a última mensagem do contato passou de 24h', async () => {
      await prisma.message.updateMany({
        where: { conversationId: conversaId },
        data: { createdAt: new Date(Date.now() - 25 * 60 * 60 * 1000) },
      });

      const res = await responder(cookieOwner, conversaId).expect(409);
      expect(res.body.code).toBe('JANELA_FECHADA');
      expect(metaFake.enviados).toHaveLength(0);
    });

    it('a thread informa o estado da janela, para a tela saber que responder está indisponível', async () => {
      await prisma.message.updateMany({
        where: { conversationId: conversaId },
        data: { createdAt: new Date(Date.now() - 25 * 60 * 60 * 1000) },
      });
      const res = await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);

      expect(res.body.janela).toMatchObject({ exigida: true, aberta: false, canal: 'OFICIAL' });
    });

    it('no canal NÃO oficial não existe janela: responde mesmo com a conversa velha', async () => {
      const geral = await prisma.setor.findFirstOrThrow({ where: { mantenedoraId: A.mantenedora.id } });
      const bu2 = await prisma.businessUnit.create({
        data: { mantenedoraId: A.mantenedora.id, setorId: geral.id, name: 'Número não oficial' },
      });
      await criarCanalVerificado(prisma, bu2.id, 'NAO_OFICIAL', 'inst-alfa', { requiresWindow: false });
      await prisma.userBuRole.create({
        data: {
          userId: A.owner.id,
          buId: bu2.id,
          role: 'OWNER',
          grantedViaTipo: 'MANTENEDORA',
          grantedViaId: A.mantenedora.id,
        },
      });
      const conversa = await prisma.conversation.create({
        data: { buId: bu2.id, contact: '5584933334444', contactType: 'PESSOA', status: 'QUEUED' },
      });
      await prisma.message.create({
        data: {
          conversationId: conversa.id, buId: bu2.id, direction: 'IN', messageType: 'TEXTO',
          content: 'antiga', channelOrigin: 'NAO_OFICIAL', status: 'RECEBIDA',
          createdAt: new Date(Date.now() - 72 * 60 * 60 * 1000),
        },
      });

      await responder(cookieOwner, conversa.id).expect(201);
      expect(evolutionFake.enviados).toHaveLength(1);
      expect(metaFake.enviados).toHaveLength(0);
    });
  });

  describe('fila', () => {
    it('assumir trava para outro agente (409), e finalizar libera', async () => {
      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro@alfa.test', 'ATENDENTE');
      const cookieOutro = await login(app, 'outro@alfa.test');

      await request(app.getHttpServer())
        .post(`/api/bff/conversations/${conversaId}/claim`)
        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);

      const conflito = await request(app.getHttpServer())
        .post(`/api/bff/conversations/${conversaId}/claim`)
        .set('Cookie', cookieOutro).set('x-requested-with', 'teste').expect(409);
      expect(conflito.body.code).toBe('JA_ATENDIDA');

      await request(app.getHttpServer())
        .post(`/api/bff/conversations/${conversaId}/close`)
        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);

      await request(app.getHttpServer())
        .post(`/api/bff/conversations/${conversaId}/claim`)
        .set('Cookie', cookieOutro).set('x-requested-with', 'teste').expect(201);
    });

    it('responder NÃO rouba conversa de quem já está atendendo', async () => {
      await request(app.getHttpServer())
        .post(`/api/bff/conversations/${conversaId}/claim`)
        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);

      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro2@alfa.test', 'ATENDENTE');
      const cookieOutro = await login(app, 'outro2@alfa.test');
      await responder(cookieOutro, conversaId, 'me intrometi').expect(201);

      const conversa = await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
      expect(conversa.attendantUserId).toBe(A.owner.id);
    });

    it('abrir a thread zera as não lidas — abrir É atender', async () => {
      await receber('mais uma');
      // O beforeEach já deixou a primeira mensagem recebida como não lida.
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(2);

      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);

      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(0);
    });

    it('a lista filtra por aba e só enxerga a BU pedida', async () => {
      const res = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?aba=QUEUED`)
        .set('Cookie', cookieOwner).expect(200);
      expect(res.body.conversations).toHaveLength(1);

      const emAtendimento = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?aba=IN_SERVICE`)
        .set('Cookie', cookieOwner).expect(200);
      expect(emAtendimento.body.conversations).toHaveLength(0);
    });
  });

  describe('a inbox pagina — teto silencioso é o que vira "sumiram conversas"', () => {
    it('devolve total e temMais, e a segunda página traz o resto', async () => {
      for (let i = 0; i < 5; i++) {
        await prisma.conversation.create({
          data: {
            buId: A.businessUnit.id,
            contact: `55119000000${i}0`,
            contactType: 'PESSOA',
            status: 'QUEUED',
            lastMessageAt: new Date(Date.now() - i * 1000),
          },
        });
      }

      const p1 = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=2`)
        .set('Cookie', cookieOwner)
        .expect(200);

      expect(p1.body.conversations).toHaveLength(2);
      expect(p1.body.total).toBeGreaterThanOrEqual(5);
      // O que faltava: a resposta DIZ que há mais. Antes o take era 200 fixo e o
      // corte era invisível.
      expect(p1.body.temMais).toBe(true);

      const p2 = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=2&pagina=2`)
        .set('Cookie', cookieOwner)
        .expect(200);

      expect(p2.body.pagina).toBe(2);
      const ids1 = p1.body.conversations.map((c: { id: string }) => c.id);
      const ids2 = p2.body.conversations.map((c: { id: string }) => c.id);
      expect(ids1.some((id: string) => ids2.includes(id))).toBe(false);
    });

    it('limite acima do teto é aparado, não obedecido', async () => {
      const r = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=99999`)
        .set('Cookie', cookieOwner)
        .expect(200);
      // Um cliente não escolhe quanto o banco carrega de uma vez.
      expect(r.body.conversations.length).toBeLessThanOrEqual(200);
    });
  });

  describe('timeline paginada do atendimento', () => {
    it('caminha por 251 mensagens na ordem do banco e mantém a página limitada', async () => {
      const base = new Date('2026-01-01T12:00:00.000Z');
      const mensagens = Array.from({ length: 251 }, (_, i) => ({
        conversationId: conversaId,
        buId: A.businessUnit.id,
        direction: 'IN' as const,
        messageType: 'TEXTO' as const,
        content: `mensagem ${i}`,
        channelOrigin: 'OFICIAL' as const,
        status: 'RECEBIDA' as const,
        createdAt: new Date(base.getTime() + Math.floor(i / 7) * 1000),
      }));
      await prisma.message.deleteMany({ where: { conversationId: conversaId } });
      await prisma.message.createMany({ data: mensagens });
      const esperados = await prisma.message.findMany({
        where: { conversationId: conversaId }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true },
      });

      const recebidos: string[] = [];
      let antes: string | null = null;
      do {
        const query = antes ? `?limite=37&marcarLida=false&antes=${encodeURIComponent(antes)}` : '?limite=37&marcarLida=false';
        const pagina = await request(app.getHttpServer())
          .get(`/api/bff/conversations/${conversaId}/messages${query}`).set('Cookie', cookieOwner).expect(200);
        expect(pagina.body.messages.length).toBeLessThanOrEqual(37);
        expect(pagina.body.paginacao.limite).toBe(37);
        recebidos.unshift(...pagina.body.messages.map((m: { id: string }) => m.id));
        antes = pagina.body.paginacao.cursorAnterior;
        expect(pagina.body.paginacao.temAnteriores).toBe(Boolean(antes));
      } while (antes);

      expect(recebidos).toEqual(esperados.map((m) => m.id));
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
    });

    it('valida parâmetros depois da autorização e rejeita cursor de outra conversa autorizada', async () => {
      await prisma.message.create({ data: {
        conversationId: conversaId, buId: A.businessUnit.id, direction: 'IN', messageType: 'TEXTO',
        content: 'página de cursor', channelOrigin: 'OFICIAL', status: 'RECEBIDA',
        createdAt: new Date(Date.now() - 1000),
      } });
      const segunda = await prisma.conversation.create({ data: {
        buId: A.businessUnit.id, contact: '5584999999999', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 3,
      } });
      const cursorFonte = await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?limite=1`).set('Cookie', cookieOwner).expect(200);
      const cursor = cursorFonte.body.paginacao.cursorAnterior;
      if (!cursor) throw new Error('A fixture precisa produzir continuação.');

      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${segunda.id}/messages?antes=${encodeURIComponent(cursor)}&marcarLida=false`)
        .set('Cookie', cookieOwner).expect(400).expect(({ body }) => expect(body.code).toBe('PAGINACAO_INVALIDA'));
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: segunda.id } })).unreadCount).toBe(3);
      await receber('antes de cursor inválido');
      const anchor = lerCursorTimeline(cursor);
      await prisma.message.delete({ where: { id: anchor.mensagemId } });
      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?antes=${encodeURIComponent(cursor)}&marcarLida=false`)
        .set('Cookie', cookieOwner).expect(400).expect(({ body }) => expect(body.code).toBe('PAGINACAO_INVALIDA'));
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
      const conversaOutraMantenedora = await prisma.conversation.create({ data: {
        buId: B.businessUnit.id, contact: '5584666666666', contactType: 'PESSOA', status: 'QUEUED',
      } });
      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaOutraMantenedora.id}/messages?limite=0&antes=x`)
        .set('Cookie', cookieOwner).expect(404);
      const setor = await prisma.setor.findFirstOrThrow({ where: { mantenedoraId: A.mantenedora.id } });
      const buSemGrant = await prisma.businessUnit.create({ data: {
        mantenedoraId: A.mantenedora.id, setorId: setor.id, name: 'BU sem grant',
      } });
      const conversaSemGrant = await prisma.conversation.create({ data: {
        buId: buSemGrant.id, contact: '5584777777777', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 3,
      } });
      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaSemGrant.id}/messages?limite=0&antes=x`)
        .set('Cookie', cookieOwner).expect(404);
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaSemGrant.id } })).unreadCount).toBe(3);
      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?limite=0`)
        .set('Cookie', cookieOwner).expect(400).expect(({ body }) => expect(body.code).toBe('PAGINACAO_INVALIDA'));
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
    });

    it('exige sessão antes de validar query e não altera unread', async () => {
      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?limite=0&antes=x`).expect(401);
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
    });

    it('rejeita cursor/limite repetidos e mantém refresh e backfill sem efeito de leitura', async () => {
      await receber('entrada extra');
      const invalid = await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?limite=1&limite=2`)
        .set('Cookie', cookieOwner).expect(400);
      expect(invalid.body.code).toBe('PAGINACAO_INVALIDA');
      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?antes=a&antes=b`)
        .set('Cookie', cookieOwner).expect(400);
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(2);

      const aberta = await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?limite=1`).set('Cookie', cookieOwner).expect(200);
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(0);
      const cursor = aberta.body.paginacao.cursorAnterior;
      if (cursor) {
        await request(app.getHttpServer())
          .get(`/api/bff/conversations/${conversaId}/messages?antes=${encodeURIComponent(cursor)}`)
          .set('Cookie', cookieOwner).expect(200);
      }
      await receber('nova durante leitura');
      await request(app.getHttpServer())
        .get(`/api/bff/conversations/${conversaId}/messages?marcarLida=false`)
        .set('Cookie', cookieOwner).expect(200);
      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
    });

    it('serializa dez chegadas concorrentes com a fronteira de abertura em três lotes', async () => {
      for (let lote = 0; lote < 3; lote++) {
        await request(app.getHttpServer())
          .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
        const chegadas = Array.from({ length: 10 }, (_, i) => receber(`concorrente-${lote}-${i}`));
        const abertura = request(app.getHttpServer())
          .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
        await Promise.all([...chegadas, abertura]);

        const aposConcorrencia = (await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount;
        expect(aposConcorrencia).toBeGreaterThanOrEqual(0);
        expect(aposConcorrencia).toBeLessThanOrEqual(10);
        await receber(`apos-fronteira-${lote}`);
        expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(aposConcorrencia + 1);
      }
    });

    it('preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes', async () => {
      for (let lote = 0; lote < 3; lote++) {
        await prisma.conversation.update({ where: { id: conversaId }, data: { unreadCount: 0 } });
        let marcouLock!: () => void;
        let liberaLock!: () => void;
        const lockAdquirido = new Promise<void>((resolve) => { marcouLock = resolve; });
        const aguardaLiberação = new Promise<void>((resolve) => { liberaLock = resolve; });
        const transacaoLock = prisma.$transaction(async (tx) => {
          await tx.$executeRawUnsafe('LOCK TABLE "messages" IN ACCESS EXCLUSIVE MODE');
          marcouLock();
          await aguardaLiberação;
        }, { timeout: 30_000 });
        await lockAdquirido;

        const inicioLeitura = performance.now();
        const leitura = request(app.getHttpServer())
          .get(`/api/bff/conversations/${conversaId}/messages`)
          .set('Cookie', cookieOwner).then((res) => res);
        let esperaNoSelect = false;
        let consultas = 0;
        for (let tentativa = 0; tentativa < 100; tentativa++) {
          const bloqueadas = await prisma.$queryRaw<Array<{ count: number }>>`
            SELECT COUNT(*)::int AS count
            FROM pg_stat_activity
            WHERE datname = current_database()
              AND wait_event_type = 'Lock'
              AND query ILIKE '%messages%'
              AND query ILIKE '%SELECT%'
          `;
          consultas++;
          if (Number(bloqueadas[0]?.count ?? 0) > 0) {
            esperaNoSelect = true;
            break;
          }
          await new Promise((resolve) => setTimeout(resolve, 20));
        }

        try {
          expect(esperaNoSelect, `GET precisa estar bloqueado no SELECT de messages no lote ${lote + 1}`).toBe(true);
          const inicioIncrementos = performance.now();
          await Promise.all(Array.from({ length: 10 }, () => prisma.conversation.updateMany({
            where: { id: conversaId }, data: { unreadCount: { increment: 1 } },
          })));
          const aposIncrementos = (await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount;
          expect(aposIncrementos).toBe(10);
          liberaLock();
          const resposta = await leitura;
          expect(resposta.status).toBe(200);
          const persistido = (await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount;
          expect(persistido).toBe(10);
          console.info(JSON.stringify({
            prova: 'BCI_ACK_COM_SELECT_BLOQUEADO', lote: lote + 1,
            bloqueioDetectado: esperaNoSelect, sondagens: consultas,
            ackAteSelectBloqueadoMs: Math.round(performance.now() - inicioLeitura),
            dezIncrementosMs: Math.round(performance.now() - inicioIncrementos),
            unreadEnquantoSelectBloqueado: aposIncrementos, unreadDepoisDaResposta: persistido,
          }));
        } finally {
          liberaLock();
          await leitura.catch(() => undefined);
          await transacaoLock;
        }
        await receber(`apos-ack-bloqueado-${lote}`);
        expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(11);
      }
    });

    it('permite leituras de cursor concorrentes com close sem reescrever status', async () => {
      for (let lote = 0; lote < 3; lote++) {
        const mensagens = Array.from({ length: 10 }, (_, i) => prisma.message.create({ data: {
          conversationId: conversaId, buId: A.businessUnit.id, direction: 'IN', messageType: 'TEXTO',
          content: `corrida ${lote}-${i}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
          createdAt: new Date(Date.now() + i),
        } }));
        await Promise.all(mensagens);
        const primeira = await request(app.getHttpServer())
          .get(`/api/bff/conversations/${conversaId}/messages?limite=1&marcarLida=false`)
          .set('Cookie', cookieOwner).expect(200);
        const cursor = primeira.body.paginacao.cursorAnterior;
        expect(cursor).toBeTruthy();
        const leituras = Array.from({ length: 10 }, () => request(app.getHttpServer())
          .get(`/api/bff/conversations/${conversaId}/messages?limite=1&marcarLida=false&antes=${encodeURIComponent(cursor)}`)
          .set('Cookie', cookieOwner).expect(200));
        const fechamento = request(app.getHttpServer())
          .post(`/api/bff/conversations/${conversaId}/close`).set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
        const respostas = await Promise.all([...leituras, fechamento]);
        expect(respostas.slice(0, 10).every((r) => r.body.messages.length <= 1)).toBe(true);
        expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).status).toBe('CLOSED');
      }
    });
  });
});

```

## Frozen file: api-app/test/browser-server.cjs

Original SHA-256: `fd85fa666489fc8b5bf688362e5d142db62e5637384c1606f86b3ecf25c8180e`; bytes:2830.

```text
const { Test } = require('@nestjs/testing');
const { AppModule } = require('../dist/app.module.js');
const { META_CLIENT } = require('../dist/integrations/meta/meta.client.js');
const { EVOLUTION_CLIENT } = require('../dist/integrations/evolution/evolution.client.js');
const { configurarBodyParsers } = require('../dist/infra/http/body-parsers.js');
const { RealtimeService } = require('../dist/realtime/realtime.service.js');
const { PrismaService } = require('../dist/infra/prisma/prisma.service.js');

async function main() {
  const db = process.env.DATABASE_URL;
  const fixtureDb = process.env.LEADSHUG_E2E_DATABASE_URL;
  if (!db || db !== fixtureDb) throw new Error('O servidor de browser requer DATABASE_URL igual ao banco dedicado de E2E.');
  const dbName = new URL(db).pathname.slice(1).split('?')[0];
  if (!dbName.startsWith('leadshug_timeline_')) throw new Error('O servidor de browser aceita apenas banco leadshug_timeline_* descartável.');
  process.env.SESSION_SECRET = 'segredo-de-e2e';
  process.env.INTERNAL_SERVICE_TOKEN = 'token-de-e2e';
  process.env.META_APP_SECRET = 'segredo-do-app-meta';
  process.env.EVOLUTION_WEBHOOK_SECRET = 'segredo-do-caminho-evolution';
  process.env.WEBHOOK_VERIFY_TOKEN = 'verify-token-de-teste';
  process.env.LH_ARQUIVOS_DIR = '/tmp/leadshug-arquivos-e2e';
  process.env.WEB_ORIGIN = 'http://127.0.0.1:4173';

  const fake = {
    configurado: () => true,
    async enviarTexto(_canal, _contato, texto) { fake.enviados.push(texto); return `e2e-${fake.enviados.length}`; },
    async numerosDaWaba(id) { return [{ id: `phone-${id}`, telefone: '5584999990000', nomeVerificado: 'E2E' }]; },
    async criarInstancia() { return { qrcode: 'data:image/png;base64,QR' }; },
    async qrDaInstancia() { return 'data:image/png;base64,QR'; },
    async estadoDaInstancia() { return 'open'; },
    async apagarInstancia() {},
    enviados: [],
  };
  const moduleRef = await Test.createTestingModule({ imports: [AppModule] })
    .overrideProvider(META_CLIENT).useValue(fake)
    .overrideProvider(EVOLUTION_CLIENT).useValue(fake)
    .compile();
  const app = moduleRef.createNestApplication({ bodyParser: false });
  configurarBodyParsers(app);
  app.enableCors({ origin: ['http://127.0.0.1:4173'], credentials: true });
  await app.init();
  app.get(RealtimeService).ligar(app.getHttpServer());
  await app.listen(Number(process.env.PORT ?? '3100'), '0.0.0.0');
  const close = async () => { await app.get(PrismaService).$disconnect(); await app.close(); };
  process.on('SIGTERM', () => void close().finally(() => process.exit(0)));
  process.on('SIGINT', () => void close().finally(() => process.exit(0)));
  console.log(`timeline test API listening on ${process.env.PORT ?? '3100'}; database ${dbName}`);
}

main().catch((error) => { console.error(error); process.exit(1); });

```

## Frozen file: api-app/test/canais.e2e-spec.ts

Original SHA-256: `ad54bc3f69a722c6f8454b3f6250d64875940c46afc8b8407bc2dae97d8f903b`; bytes:6329.

```text
import { INestApplication } from '@nestjs/common';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import {
  contratarCanalNaoOficial,
  criarCanalVerificado,
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
    it('a rota legada dá instrução determinística e não chama provider nem grava canal', async () => {
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(409);
      expect(res.body.code).toBe('USE_NUMBER_REGISTRATIONS');
      expect(await prisma.buChannel.count({ where: { buId: A.businessUnit.id } })).toBe(0);
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
    it('a rota legada não inicia pareamento', async () => {
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'NAO_OFICIAL' }).expect(409);
      expect(res.body.code).toBe('USE_NUMBER_REGISTRATIONS');
      expect(await prisma.buChannel.count({ where: { buId: A.businessUnit.id } })).toBe(0);
    });

    it('o GET de QR foi aposentado sem consulta ao provider', async () => {
      const res = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}/channels/nao-oficial/qr`)
        .set('Cookie', cookieOwnerA)
        .expect(405);
      expect(res.body.code).toBe('QR_GET_REMOVED');
    });
  });

  describe('regras do vínculo', () => {
    it('a BU aceita um canal de cada tipo, e recusa o segundo do mesmo tipo', async () => {
      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(409);
      await post(cookieOwnerA, A.businessUnit.id, { tipo: 'NAO_OFICIAL' }).expect(409);
      expect(await prisma.buChannel.count({ where: { buId: A.businessUnit.id } })).toBe(0);
    });

    it('recusa WABA ID que não é numérico, antes de falar com a Meta', async () => {
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: 'abc' }).expect(409);
      expect(res.body.code).toBe('USE_NUMBER_REGISTRATIONS');
      expect(metaFake.wabaRecusada).toBeNull();
    });

    it('repassa a recusa da Meta como META_RECUSOU', async () => {
      metaFake.wabaRecusada = '123456789';
      const res = await post(cookieOwnerA, A.businessUnit.id, { tipo: 'OFICIAL', wabaId: '123456789' }).expect(409);
      expect(res.body.code).toBe('USE_NUMBER_REGISTRATIONS');
    });

    it('remover exige ADMIN e libera o tipo para ser conectado de novo', async () => {
      await criarCanalVerificado(prisma, A.businessUnit.id, 'OFICIAL', 'phone-123456');

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

      await criarCanalVerificado(prisma, A.businessUnit.id, 'OFICIAL', 'phone-123456');
    });

    it('listar canais é leitura: VIEWER enxerga', async () => {
      await criarCanalVerificado(prisma, A.businessUnit.id, 'OFICIAL', 'phone-listable');
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

```

## Frozen file: api-app/test/helpers.ts

Original SHA-256: `828ff79c0ed7f15298b5fe220c1082882a9e6425a0d62fdc4d5a3ff9dd00031c`; bytes:10767.

```text
import { INestApplication } from '@nestjs/common';
import { Test } from '@nestjs/testing';
import type { NestExpressApplication } from '@nestjs/platform-express';
import request from 'supertest';
import { AppModule } from '../src/app.module';
import { configurarBodyParsers } from '../src/infra/http/body-parsers';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { EVOLUTION_CLIENT, EvolutionClient } from '../src/integrations/evolution/evolution.client';
import { META_CLIENT, MetaClient } from '../src/integrations/meta/meta.client';
import { sealChannelCredential } from '../src/domain/channels/channel-credential-crypto';

/** Dublês das portas de saída: o teste prova permissão, não a Meta. */
export const metaFake: MetaClient & { wabaRecusada: string | null; enviados: { para: string; texto: string }[]; registrosNumero: number; subscriptionHook: (() => Promise<void>) | null } = {
  wabaRecusada: null,
  enviados: [],
  registrosNumero: 0,
  subscriptionHook: null,
  capabilities: () => ({ appId: 'fixture-app', configId: 'fixture-config', graphVersion: 'v-test', available: true, reason: 'AVAILABLE' }),
  async exchangeCode() { return { accessToken: 'fixture-scoped-token' }; },
  async recursos(_accessToken, wabaId, after) { return { wabas: [{ id: wabaId ?? '123456789', name: 'Fixture' }], numbers: wabaId ? [{ id: '987654321', telefone: '5584999990000', nomeVerificado: 'Fixture' }] : [], next: after ? null : 'fixture-page-2' }; },
  async enviarTexto(_phoneNumberId: string, para: string, texto: string) {
    metaFake.enviados.push({ para, texto });
    return `wamid-enviado-${metaFake.enviados.length}`;
  },
  configurado: () => true,
  async numerosDaWaba(wabaId: string) {
    if (metaFake.wabaRecusada === wabaId) throw new Error('WABA recusada');
    return { data: [{ id: `phone-${wabaId}`, telefone: '5584999990000', nomeVerificado: 'Teste' }], next: null };
  },
  async confirmarNumero(wabaId, phoneNumberId) { return wabaId === '123456789' && phoneNumberId === '987654321' ? { id: phoneNumberId, telefone: '5584999990000', nomeVerificado: `WABA ${wabaId}` } : null; },
  async registrarNumero() { metaFake.registrosNumero += 1; },
  async inscreverWaba() { await metaFake.subscriptionHook?.(); },
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
  async consultarInstancia(nome) { return { name: nome, ownerJid: '5584999990000@s.whatsapp.net', connectionStatus: 'open' }; },
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
  process.env.CHANNEL_CREDENTIAL_KEY_ID = 'fixture-key-v1';
  process.env.CHANNEL_CREDENTIAL_KEY = Buffer.alloc(32, 17).toString('base64');

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
  await prisma.providerResourceIdentity.deleteMany();
  await prisma.channelRegistrationAttempt.deleteMany();
  await prisma.channelCredential.deleteMany();
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

/** Test channel fixture with the same durable ownership and credential invariants as production. */
export async function criarCanalVerificado(
  prisma: PrismaService,
  buId: string,
  type: 'OFICIAL' | 'NAO_OFICIAL',
  externalResourceId: string,
  options: { status?: 'CONECTADO' | 'CONECTANDO' | 'DESCONECTADO'; requiresWindow?: boolean } = {},
) {
  const channel = await prisma.buChannel.create({ data: {
    buId, type, status: options.status ?? 'CONECTADO', requiresWindow: options.requiresWindow ?? type === 'OFICIAL',
    ...(type === 'OFICIAL' ? { phoneNumberId: externalResourceId } : { evolutionInstanceName: externalResourceId }),
    ownNumberVerified: true, verifiedEpoch: 0, providerConnectionState: type === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
    receiptVerifiedAt: new Date(),
  } });
  const priorIdentity = await prisma.providerResourceIdentity.findUnique({
    where: { provider_externalResourceId: { provider: type, externalResourceId } },
  });
  if (priorIdentity && (priorIdentity.buId !== buId || priorIdentity.currentChannelId)) {
    throw new Error('Fixture resource identity is owned or active elsewhere.');
  }
  const identity = priorIdentity
    ? await prisma.providerResourceIdentity.update({ where: { id: priorIdentity.id }, data: { currentChannelId: channel.id, retiredAt: null } })
    : await prisma.providerResourceIdentity.create({ data: {
      provider: type, externalResourceId, buId, currentChannelId: channel.id,
    } });
  if (type === 'OFICIAL') {
    const keyId = process.env.CHANNEL_CREDENTIAL_KEY_ID!;
    const key = Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY!, 'base64');
    const envelope = sealChannelCredential('fixture-scoped-token', keyId, key, {
      purpose: 'active', provider: type, buId, channelId: channel.id, generation: channel.generation, version: 1,
    });
    await prisma.channelCredential.create({ data: {
      channelId: channel.id, provider: type, buId, generation: channel.generation, version: 1,
      keyId, nonce: new Uint8Array(envelope.nonce), ciphertext: new Uint8Array(envelope.ciphertext), tag: new Uint8Array(envelope.tag),
    } });
  }
  return { channel, identity };
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

```

## Frozen file: api-app/test/modulos.e2e-spec.ts

Original SHA-256: `e54caf54ce08a237abeb0b5bae6d6483662d9cc6bda323f35eece637817cdf00`; bytes:6041.

```text
import { INestApplication } from '@nestjs/common';
import request from 'supertest';
import { afterEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { criarMantenedora, limparBanco, login, subirApp } from './helpers';

/**
 * O teto da instalação é lido UMA vez, na construção do serviço — então cada
 * cenário sobe o app com a env que quer provar. É o mesmo que acontece em
 * produção: mudar módulo de instalação é deploy, não requisição.
 */
async function subirCom(canalNaoOficial: boolean) {
  process.env.LH_CHANNEL_UNOFFICIAL = canalNaoOficial ? 'true' : 'false';
  return subirApp();
}

describe('módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016)', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let A: Awaited<ReturnType<typeof criarMantenedora>>;
  let cookie: string;

  const conectar = (tipo: string, buId: string) =>
    request(app.getHttpServer())
      .post(`/api/bff/business-units/${buId}/channels`)
      .set('Cookie', cookie)
      .set('x-requested-with', 'teste')
      .send({ tipo, wabaId: '123456789' });

  async function cenario(teto: boolean, contratado: boolean | undefined) {
    ({ app, prisma } = await subirCom(teto));
    await limparBanco(prisma);
    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
    if (contratado !== undefined) {
      await prisma.mantenedoraSettings.upsert({
        where: { mantenedoraId: A.mantenedora.id },
        create: { mantenedoraId: A.mantenedora.id, modulos: { canalNaoOficial: contratado } },
        update: { modulos: { canalNaoOficial: contratado } },
      });
    }
    cookie = await login(app, 'dono@alfa.test');
  }

  afterEach(async () => {
    await limparBanco(prisma);
    await app?.close();
    process.env.LH_CHANNEL_UNOFFICIAL = 'false';
  });

  describe('o /me devolve o produto já interseccionado', () => {
    it('teto ligado + contratado = ligado, e a marca vem junto', async () => {
      await cenario(true, true);
      await prisma.mantenedoraSettings.update({
        where: { mantenedoraId: A.mantenedora.id },
        data: { marcaNome: 'Unifast', marcaCor: '#0a7', marcaTema: 'escuro' },
      });

      const res = await request(app.getHttpServer()).get('/api/bff/me').set('Cookie', cookie).expect(200);

      expect(res.body.produto.modulos).toEqual({ canalNaoOficial: true });
      expect(res.body.produto.marca).toEqual({ nome: 'Unifast', cor: '#0a7', corClaro: '#0a7', corEscuro: '#0a7', corSecundaria: '#121212', tema: 'escuro', logo: null });
    });

    it('a Mantenedora NÃO amplia o teto: contratado sem teto continua desligado', async () => {
      await cenario(false, true);
      const res = await request(app.getHttpServer()).get('/api/bff/me').set('Cookie', cookie).expect(200);
      expect(res.body.produto.modulos.canalNaoOficial).toBe(false);
    });

    it('sem nada contratado, o produto nasce sem módulo e com tema padrão', async () => {
      await cenario(true, undefined);
      const res = await request(app.getHttpServer()).get('/api/bff/me').set('Cookie', cookie).expect(200);
      expect(res.body.produto.modulos.canalNaoOficial).toBe(false);
      expect(res.body.produto.marca).toEqual({ nome: null, cor: null, corClaro: null, corEscuro: null, corSecundaria: '#121212', tema: 'claro', logo: null });
    });
  });

  it('a migração PRESERVA o módulo de quem já usa o canal — repetível, e é o que sobe em stage', async () => {
    await cenario(true, undefined); // instalação capaz, conta sem nada contratado
    await prisma.buChannel.create({
      data: {
        buId: A.businessUnit.id,
        type: 'NAO_OFICIAL',
        evolutionInstanceName: 'inst-antiga',
        requiresWindow: false,
        status: 'CONECTADO',
      },
    });

    // O mesmo UPDATE da migração 20260821220000. Uma conta que já usa o canal
    // não pode acordar com o módulo desligado sem ninguém ter desligado.
    await prisma.$executeRaw`
      UPDATE "mantenedora_settings" s
         SET "modulos" = jsonb_set(COALESCE(s."modulos", '{}'::jsonb), '{canalNaoOficial}', 'true'::jsonb, true)
       WHERE EXISTS (
         SELECT 1 FROM "bu_channels" c
           JOIN "business_units" b ON b."id" = c."bu_id"
          WHERE b."mantenedora_id" = s."mantenedora_id" AND c."type" = 'NAO_OFICIAL'
       )
    `;

    const res = await request(app.getHttpServer()).get('/api/bff/me').set('Cookie', cookie).expect(200);
    expect(res.body.produto.modulos.canalNaoOficial).toBe(true);
  });

  describe('a rota recusa o que o front não deveria nem ter oferecido', () => {
    it('autorizado: com teto e contrato, conecta o canal não oficial', async () => {
      await cenario(true, true);
      const res = await conectar('NAO_OFICIAL', A.businessUnit.id).expect(409);
      expect(res.body.code).toBe('USE_NUMBER_REGISTRATIONS');
    });

    it('módulo fora do teto da instalação: 404 MODULO_DESLIGADO, nunca 403', async () => {
      await cenario(false, true);
      const res = await conectar('NAO_OFICIAL', A.businessUnit.id).expect(404);
      expect(res.body.code).toBe('MODULO_DESLIGADO');
    });

    it('teto ligado mas a Mantenedora não contratou: 404 igual', async () => {
      await cenario(true, false);
      const res = await conectar('NAO_OFICIAL', A.businessUnit.id).expect(404);
      expect(res.body.code).toBe('MODULO_DESLIGADO');
    });

    it('o canal OFICIAL nunca é barrado por módulo — ele é o PISO do produto', async () => {
      // Instalação sem nenhum módulo, Mantenedora sem nada contratado: o canal
      // oficial continua funcionando. É o que a Emenda 2 §1 decidiu.
      await cenario(false, undefined);
      const res = await conectar('OFICIAL', A.businessUnit.id).expect(409);
      expect(res.body.code).toBe('USE_NUMBER_REGISTRATIONS');
    });
  });
});

```

## Frozen file: api-app/test/number-onboarding-flow.e2e-spec.ts

Original SHA-256: `ed2d7b6dfd23169280bfad8babe5728bd8b0c6de01158197998a45b858d0c4ae`; bytes:14017.

```text
import { INestApplication } from '@nestjs/common';
import { createHmac } from 'node:crypto';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { EVOLUTION_WEBHOOK_SECRET, META_APP_SECRET, contratarCanalNaoOficial, criarMantenedora, criarUsuario, limparBanco, login, metaFake, subirApp, tetoComCanalNaoOficial } from './helpers';

describe('BFF number registration workflow (PostgreSQL)', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let tenant: Awaited<ReturnType<typeof criarMantenedora>>;
  let cookie: string;

  beforeAll(async () => { tetoComCanalNaoOficial(); process.env.EVOLUTION_WEBHOOK_URL = 'https://example.test/webhooks/evolution'; ({ app, prisma } = await subirApp()); });
  afterAll(async () => { if (prisma) await limparBanco(prisma); await app?.close(); });
  beforeEach(async () => {
    await limparBanco(prisma);
    tenant = await criarMantenedora(app, 'Number registration', 'number-registration@example.test');
    cookie = await login(app, 'number-registration@example.test');
    metaFake.wabaRecusada = null;
    metaFake.registrosNumero = 0;
    metaFake.subscriptionHook = null;
  });

  const bff = (verb: 'get' | 'post', path: string) => {
    const req = request(app.getHttpServer())[verb](path).set('Cookie', cookie);
    return verb === 'post' ? req.set('x-requested-with', 'teste') : req;
  };

  it('recovers the same one-use nonce for idempotent create and connects only after provider subscribe plus receipt', async () => {
    const key = 'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa';
    const createBody = { buId: tenant.businessUnit.id, tipo: 'OFICIAL', operation: 'NOVO' };
    const first = await bff('post', '/api/bff/number-registrations').set('Idempotency-Key', key).send(createBody).expect(201);
    const replay = await bff('post', '/api/bff/number-registrations').set('Idempotency-Key', key).send(createBody).expect(201);
    expect(replay.body.attempt.id).toBe(first.body.attempt.id);
    expect(replay.body.nonce).toBe(first.body.nonce);
    expect(JSON.stringify(first.body)).not.toMatch(/nonceHash|sessionHash|candidateCiphertext|fixture-scoped-token/);

    const id = first.body.attempt.id as string;
    await bff('post', `/api/bff/number-registrations/${id}/authorize`).send({ nonce: first.body.nonce, code: 'fixture-oauth-code' }).expect(200);
    await bff('post', `/api/bff/number-registrations/${id}/authorize`).send({ nonce: first.body.nonce, code: 'fixture-oauth-code' }).expect(409);

    const options = await bff('get', `/api/bff/number-registrations/${id}/options?wabaId=123456789&after=fixture-page-1`).expect(200);
    expect(options.body.numbers).toEqual([{ id: '987654321', telefone: '5584999990000', nomeVerificado: 'Fixture' }]);
    expect(options.body.next).toBeNull();
    await bff('get', `/api/bff/number-registrations/${id}/options?wabaId=123456789&after=${'x'.repeat(513)}`).expect(400);

    const confirmed = await bff('post', `/api/bff/number-registrations/${id}/confirm`)
      .send({ wabaId: '123456789', phoneNumberId: '987654321', modoRegistro: 'JA_REGISTRADO', after: 'fixture-page-2' }).expect(200);
    expect(confirmed.body.registration).toMatchObject({ state: 'PENDING_RECEIPT', stage: 'MAPPED_PENDING_RECEIPT' });
    expect(JSON.stringify(confirmed.body)).not.toMatch(/fixture-scoped-token|candidateCiphertext|sessionHash/);

    const webhook = {
      entry: [{ changes: [{ field: 'messages', value: {
        metadata: { phone_number_id: '987654321' },
        messages: [{ id: 'wamid-registration-receipt', from: '5584997770000', type: 'text', text: { body: 'receipt' } }],
      } }] }],
    };
    const deliverReceipt = async () => {
      const signature = createHmac('sha256', META_APP_SECRET).update(JSON.stringify(webhook)).digest('hex');
      await request(app.getHttpServer()).post('/webhooks/meta').set('content-type', 'application/json')
        .set('x-hub-signature-256', `sha256=${signature}`).send(webhook).expect(200);
    };
    metaFake.subscriptionHook = deliverReceipt;
    const advanced = await bff('post', `/api/bff/number-registrations/${id}/advance`).send({}).expect(200);
    metaFake.subscriptionHook = null;
    expect(advanced.body).toMatchObject({ state: 'CONNECTED', stage: 'RECEIPT_VERIFIED' });
    const connected = await bff('get', `/api/bff/number-registrations/${id}`).expect(200);
    expect(connected.body).toMatchObject({ state: 'CONNECTED', stage: 'RECEIPT_VERIFIED' });
    const channel = await prisma.buChannel.findUniqueOrThrow({ where: { id: connected.body.channelId } });
    expect(channel.status).toBe('CONECTADO');
    expect(channel.receiptVerifiedAt).toBeInstanceOf(Date);
  });

  it('does not disclose registration state to a different tenant and rejects invalid provider resources', async () => {
    const key = 'bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb';
    const created = await bff('post', '/api/bff/number-registrations').set('Idempotency-Key', key)
      .send({ buId: tenant.businessUnit.id, tipo: 'OFICIAL', operation: 'NOVO' }).expect(201);
    const id = created.body.attempt.id as string;
    const other = await criarMantenedora(app, 'Another registration tenant', 'other-registration@example.test');
    const otherCookie = await login(app, 'other-registration@example.test');
    await request(app.getHttpServer()).get(`/api/bff/number-registrations/${id}`).set('Cookie', otherCookie).expect(404);
    await bff('post', `/api/bff/number-registrations/${id}/authorize`)
      .send({ nonce: created.body.nonce, code: 'fixture-oauth-code' }).expect(200);
    await bff('post', `/api/bff/number-registrations/${id}/confirm`)
      .send({ wabaId: '999999999', phoneNumberId: '987654321', modoRegistro: 'JA_REGISTRADO' }).expect(409);
    expect(await prisma.buChannel.count({ where: { buId: other.businessUnit.id } })).toBe(0);
  });

  it('recovers a promoted pending registration after expiry with a fresh authorized session', async () => {
    const key = 'bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbc';
    const created = await bff('post', '/api/bff/number-registrations').set('Idempotency-Key', key)
      .send({ buId: tenant.businessUnit.id, tipo: 'OFICIAL', operation: 'NOVO' }).expect(201);
    const id = created.body.attempt.id as string;
    await bff('post', `/api/bff/number-registrations/${id}/authorize`).send({ nonce: created.body.nonce, code: 'fixture-oauth-code' }).expect(200);
    await bff('post', `/api/bff/number-registrations/${id}/confirm`)
      .send({ wabaId: '123456789', phoneNumberId: '987654321', modoRegistro: 'JA_REGISTRADO' }).expect(200);
    await prisma.channelRegistrationAttempt.update({ where: { id }, data: { expiresAt: new Date(Date.now() - 1_000) } });
    const refreshedCookie = await login(app, 'number-registration@example.test');
    const recovered = request(app.getHttpServer()).get(`/api/bff/number-registrations/${id}`).set('Cookie', refreshedCookie);
    await recovered.expect(200).expect(({ body }) => expect(body).toMatchObject({ state: 'PENDING_RECEIPT', stage: 'MAPPED_PENDING_RECEIPT' }));
    await request(app.getHttpServer()).post(`/api/bff/number-registrations/${id}/advance`).set('Cookie', refreshedCookie)
      .set('x-requested-with', 'teste').send({}).expect(200).expect(({ body }) => expect(body).toMatchObject({ state: 'PENDING_RECEIPT', stage: 'SUBSCRIBED' }));
    const channel = await prisma.buChannel.findUniqueOrThrow({ where: { id: created.body.attempt.channelId } });
    expect(channel.providerConnectionState).toBe('SUBSCRIBED');
    expect(channel.status).toBe('CONECTANDO');
  });

  it('reserves immutable provider ownership before register and projects BU-scoped channel authority safely', async () => {
    const other = await criarMantenedora(app, 'Existing owner', 'resource-owner@example.test');
    const ownerChannel = await prisma.buChannel.create({ data: { buId: other.businessUnit.id, type: 'OFICIAL', phoneNumberId: '987654321' } });
    await prisma.providerResourceIdentity.create({ data: {
      provider: 'OFICIAL', externalResourceId: '987654321', buId: other.businessUnit.id, currentChannelId: ownerChannel.id,
    } });
    const key = 'cccccccc-cccc-4ccc-8ccc-cccccccccccc';
    const created = await bff('post', '/api/bff/number-registrations').set('Idempotency-Key', key)
      .send({ buId: tenant.businessUnit.id, tipo: 'OFICIAL', operation: 'NOVO' }).expect(201);
    await bff('post', `/api/bff/number-registrations/${created.body.attempt.id}/authorize`)
      .send({ nonce: created.body.nonce, code: 'fixture-oauth-code' }).expect(200);
    await bff('post', `/api/bff/number-registrations/${created.body.attempt.id}/confirm`)
      .send({ wabaId: '123456789', phoneNumberId: '987654321', modoRegistro: 'NOVO', pin: '123456' }).expect(409);
    expect(metaFake.registrosNumero).toBe(0);

    const tenantBu = await prisma.businessUnit.findUniqueOrThrow({ where: { id: tenant.businessUnit.id }, select: { setorId: true } });
    const secondBu = await prisma.businessUnit.create({ data: {
      mantenedoraId: tenant.mantenedora.id, name: 'Second BU', phone: null,
      setorId: tenantBu.setorId,
    } });
    const scopedUserId = await criarUsuario(prisma, tenant.mantenedora.id, secondBu.id, 'scoped-admin@example.test', 'ADMIN');
    const scopedCookie = await login(app, 'scoped-admin@example.test');
    const units = await request(app.getHttpServer()).get('/api/bff/business-units').set('Cookie', scopedCookie).expect(200);
    expect(units.body.businessUnits).toHaveLength(1);
    expect(units.body.businessUnits[0]).toMatchObject({ id: secondBu.id, papel: 'ADMIN' });
    expect(scopedUserId).toBeTruthy();
    const detail = await request(app.getHttpServer()).get(`/api/bff/business-units/${tenant.businessUnit.id}/channels`)
      .set('Cookie', cookie).expect(200);
    expect(detail.body.canais[0]).toMatchObject({ id: expect.any(String), type: 'OFICIAL', generation: 1, currentAttemptId: created.body.attempt.id });
    expect(JSON.stringify(detail.body)).not.toMatch(/wabaId|accessToken|ciphertext|sessionHash/);
  });

  it('allows only one BU to reserve a concurrently selected provider resource', async () => {
    const competitor = await criarMantenedora(app, 'Concurrent owner', 'concurrent-owner@example.test');
    const competitorCookie = await login(app, 'concurrent-owner@example.test');
    const createAndAuthorize = async (actorCookie: string, buId: string, idempotencyKey: string) => {
      const created = await request(app.getHttpServer()).post('/api/bff/number-registrations').set('Cookie', actorCookie)
        .set('x-requested-with', 'teste').set('Idempotency-Key', idempotencyKey)
        .send({ buId, tipo: 'OFICIAL', operation: 'NOVO' }).expect(201);
      await request(app.getHttpServer()).post(`/api/bff/number-registrations/${created.body.attempt.id}/authorize`)
        .set('Cookie', actorCookie).set('x-requested-with', 'teste')
        .send({ nonce: created.body.nonce, code: 'fixture-oauth-code' }).expect(200);
      return { id: created.body.attempt.id as string, actorCookie };
    };
    const [first, second] = await Promise.all([
      createAndAuthorize(cookie, tenant.businessUnit.id, 'dddddddd-dddd-4ddd-8ddd-dddddddddddd'),
      createAndAuthorize(competitorCookie, competitor.businessUnit.id, 'eeeeeeee-eeee-4eee-8eee-eeeeeeeeeeee'),
    ]);
    const confirm = ({ id, actorCookie }: { id: string; actorCookie: string }) => request(app.getHttpServer())
      .post(`/api/bff/number-registrations/${id}/confirm`).set('Cookie', actorCookie).set('x-requested-with', 'teste')
      .send({ wabaId: '123456789', phoneNumberId: '987654321', modoRegistro: 'NOVO', pin: '123456' });
    const outcomes = await Promise.all([confirm(first), confirm(second)]);
    expect(outcomes.filter((result) => result.status === 200)).toHaveLength(1);
    expect(outcomes.filter((result) => result.status === 409)).toHaveLength(1);
    expect(metaFake.registrosNumero).toBe(1);
    const identity = await prisma.providerResourceIdentity.findUniqueOrThrow({
      where: { provider_externalResourceId: { provider: 'OFICIAL', externalResourceId: '987654321' } },
    });
    expect([tenant.businessUnit.id, competitor.businessUnit.id]).toContain(identity.buId);
  });

  it('connects Evolution only after pairing proves its own identity and the first keyed inbound message arrives', async () => {
    await contratarCanalNaoOficial(prisma, tenant.mantenedora.id);
    const paired = await bff('post', `/api/bff/business-units/${tenant.businessUnit.id}/channels/nao-oficial/pair`)
      .send({ intent: 'INITIAL' }).expect(200);
    expect(paired.body).toMatchObject({ state: 'PENDING_RECEIPT', qrcode: 'data:image/png;base64,QR' });
    const channel = await prisma.buChannel.findUniqueOrThrow({ where: { id: paired.body.channelId } });
    expect(channel.ownNumberVerified).toBe(true);
    expect(channel.status).toBe('CONECTANDO');
    const attemptId = channel.currentAttemptId!;
    const body = {
      event: 'messages.upsert', instance: channel.evolutionInstanceName,
      data: { key: { remoteJid: '5584999777666@s.whatsapp.net', fromMe: false, id: 'evo-first-trusted-in' }, pushName: 'Cliente', message: { conversation: 'olá' } },
    };
    await request(app.getHttpServer()).post(`/webhooks/evolution/${EVOLUTION_WEBHOOK_SECRET}`).send(body).expect(200);
    const connected = await prisma.buChannel.findUniqueOrThrow({ where: { id: channel.id } });
    const attempt = await prisma.channelRegistrationAttempt.findUniqueOrThrow({ where: { id: attemptId } });
    expect(connected).toMatchObject({ status: 'CONECTADO', providerConnectionState: 'CONNECTED', ownNumberVerified: true });
    expect(connected.receiptVerifiedAt).toBeInstanceOf(Date);
    expect(attempt).toMatchObject({ state: 'CONNECTED', stage: 'RECEIPT_VERIFIED' });
    expect(await prisma.message.count({ where: { externalId: 'evo-first-trusted-in' } })).toBe(1);
  });
});

```

## Frozen file: api-app/test/number-onboarding-message-acceptance.e2e-spec.ts

Original SHA-256: `c8b29c16412938b64fb8e2555729f0777d9e3eb69a57d29df3d65b56443c4bac`; bytes:6700.

```text
import { INestApplication } from '@nestjs/common';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { MessageAcceptanceService } from '../src/domain/inbox/message-acceptance.service';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { criarMantenedora, limparBanco, subirApp } from './helpers';

describe('number onboarding keyed message acceptance (PostgreSQL)', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let acceptance: MessageAcceptanceService;
  let buId: string;
  let channelId: string;
  let identityId: string;

  beforeAll(async () => {
    ({ app, prisma } = await subirApp());
    await limparBanco(prisma);
    const tenant = await criarMantenedora(app, 'Acceptance fixture', 'acceptance-fixture@example.test');
    buId = tenant.businessUnit.id;
    const channel = await prisma.buChannel.create({
      data: { buId, type: 'OFICIAL', status: 'CONECTADO', phoneNumberId: 'phone-acceptance-fixture', ownNumberVerified: true, verifiedEpoch: 0 },
    });
    channelId = channel.id;
    const identity = await prisma.providerResourceIdentity.create({
      data: { provider: 'OFICIAL', externalResourceId: 'phone-acceptance-fixture', buId, currentChannelId: channelId },
    });
    identityId = identity.id;
    await prisma.conversation.create({
      data: { buId, contact: '5584999000002', contactType: 'PESSOA', status: 'IN_SERVICE' },
    });
    acceptance = new MessageAcceptanceService(prisma);
  });

  afterAll(async () => {
    if (prisma) {
      await prisma.message.deleteMany({ where: { providerResourceIdentityId: identityId } });
      await prisma.providerResourceIdentity.deleteMany({ where: { id: identityId } });
      await limparBanco(prisma);
    }
    await app?.close();
  });

  it('accepts one incoming key once, creating one conversation and unread increment', async () => {
    const input = baseInput({ externalMessageId: 'wamid-in-fixture-1', direction: 'IN', content: 'hello' });
    const [a, b] = await Promise.all([acceptance.accept(input), acceptance.accept(input)]);
    expect(a.message.id).toBe(b.message.id);
    expect([a.creationWinner, b.creationWinner].filter(Boolean)).toHaveLength(1);
    expect([a.reconciled, b.reconciled].filter(Boolean)).toHaveLength(1);
    expect(await prisma.message.count({ where: { providerResourceIdentityId: identityId, externalId: input.externalMessageId } })).toBe(1);
    const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: a.conversation.id } });
    expect(conversation.unreadCount).toBe(1);
  });

  it('reports the first conversation once and keeps a second immediate message in the same conversation', async () => {
    const first = await acceptance.accept(baseInput({ externalMessageId: 'wamid-in-first-conversation', contact: '5584999000003' }));
    const second = await acceptance.accept(baseInput({ externalMessageId: 'wamid-in-second-message', contact: '5584999000003' }));
    expect(first.conversationCreated).toBe(true);
    expect(first.reopened).toBe(false);
    expect(second.conversationCreated).toBe(false);
    expect(second.reopened).toBe(false);
    expect(second.conversation.id).toBe(first.conversation.id);
    expect(second.conversation.unreadCount).toBe(2);
  });

  it('echo-first and sender result reconcile to the same OUT row without changing its identity or createdAt', async () => {
    const echo = await acceptance.accept(baseInput({
      externalMessageId: 'wamid-out-fixture-1', direction: 'OUT', content: 'echo body', contact: '5584999000002',
    }));
    const createdAt = echo.message.createdAt;
    const sender = await acceptance.accept(baseInput({
      externalMessageId: 'wamid-out-fixture-1', direction: 'OUT', content: 'trusted sender body', conversationId: echo.conversation.id,
      contact: '5584999000002',
      senderResult: true, authorName: 'Support fixture',
    }));
    expect(sender.message.id).toBe(echo.message.id);
    expect(sender.message.createdAt).toEqual(createdAt);
    expect(sender.message.authorName).toBe('Support fixture');
    expect(sender.message.content).toBe('trusted sender body');
    expect(sender.creationWinner).toBe(false);
    expect(await prisma.message.count({ where: { providerResourceIdentityId: identityId, externalId: 'wamid-out-fixture-1' } })).toBe(1);
    expect(await prisma.conversation.count({ where: { id: echo.conversation.id } })).toBe(1);
    const laterEcho = await acceptance.accept(baseInput({
      externalMessageId: 'wamid-out-fixture-1', direction: 'OUT', content: 'untrusted later echo', contact: '5584999000002',
      conversationId: echo.conversation.id,
    }));
    expect(laterEcho.message.id).toBe(echo.message.id);
    expect(laterEcho.message.createdAt).toEqual(createdAt);
    expect(laterEcho.message.content).toBe('trusted sender body');
    expect(laterEcho.message.authorName).toBe('Support fixture');
  });

  it('persists redacted diagnostics only while the verified identity remains current', async () => {
    const context = {
      providerResourceIdentityId: identityId, buId, channelId, generation: 1, pairingEpoch: 0, channelOrigin: 'OFICIAL' as const,
    };
    await acceptance.persistVerifiedDiagnostic(context, 'messages.received', {
      providerId: 'safe-fixture', apikey: 'fake-apikey-fixture', nested: { access_token: 'fake-token-fixture' },
    });
    const event = await prisma.webhookEvent.findFirstOrThrow({ where: { buId, eventType: 'messages.received' } });
    expect(event.payload).toEqual({
      providerId: 'safe-fixture', apikey: '[REDACTED]', nested: { access_token: '[REDACTED]' },
    });
    await prisma.providerResourceIdentity.update({ where: { id: identityId }, data: { currentChannelId: null, retiredAt: new Date() } });
    await expect(acceptance.persistVerifiedDiagnostic(context, 'messages.late', { content: 'must not persist' }))
      .rejects.toMatchObject({ response: { code: 'IDENTITY_NOT_CURRENT' } });
    expect(await prisma.webhookEvent.count({ where: { buId, eventType: 'messages.late' } })).toBe(0);
    await expect(prisma.$executeRaw`UPDATE provider_resource_identities SET bu_id = 'different-owner-fixture' WHERE id = ${identityId}`)
      .rejects.toThrow();
  });

  function baseInput(overrides: Partial<Parameters<MessageAcceptanceService['accept']>[0]>) {
    return {
      providerResourceIdentityId: identityId, externalMessageId: 'fixture-id', buId, channelId,
      generation: 1, pairingEpoch: 0, contact: '5584999000001', contactType: 'PESSOA' as const,
      channelOrigin: 'OFICIAL' as const, messageType: 'TEXTO' as const, direction: 'IN' as const,
      content: 'fixture', ...overrides,
    };
  }
});

```

## Frozen file: api-app/test/realtime.e2e-spec.ts

Original SHA-256: `cf9335f7bfefecf708d69ab966533bf3b65ed7cc5615533691f7f2a841275422`; bytes:6059.

```text
import { INestApplication } from '@nestjs/common';
import { createHmac } from 'node:crypto';
import type { AddressInfo } from 'node:net';
import request from 'supertest';
import { WebSocket } from 'ws';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { RealtimeService } from '../src/realtime/realtime.service';
import { META_APP_SECRET, criarCanalVerificado, criarMantenedora, criarUsuario, limparBanco, login, subirApp } from './helpers';

/** Espera um evento do socket, ou desiste — o teste não pode pendurar. */
function esperarEvento(ws: WebSocket, tipo: string, ms = 3000): Promise<Record<string, unknown> | null> {
  return new Promise((resolve) => {
    const prazo = setTimeout(() => resolve(null), ms);
    ws.on('message', (dado) => {
      const evento = JSON.parse(String(dado)) as Record<string, unknown>;
      if (evento.tipo === tipo) {
        clearTimeout(prazo);
        resolve(evento);
      }
    });
  });
}

function conectar(porta: number, cookie: string): Promise<WebSocket> {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(`ws://127.0.0.1:${porta}/ws`, { headers: { Cookie: cookie } });
    // O 'conectado' só é enviado depois do registro; esperar por ele evita
    // asserção sobre um estado que ainda não existe.
    ws.on('message', () => resolve(ws));
    ws.on('error', reject);
    ws.on('close', (codigo) => reject(new Error(`fechou: ${codigo}`)));
  });
}

describe('push em tempo real — com escopo (fecha o risco S8)', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let porta: number;
  let A: Awaited<ReturnType<typeof criarMantenedora>>;
  let B: Awaited<ReturnType<typeof criarMantenedora>>;

  const PHONE_A = 'phone-alfa';

  const receber = async (texto: string) => {
    const corpo = {
      entry: [{ changes: [{ field: 'messages', value: {
        metadata: { phone_number_id: PHONE_A },
        contacts: [{ profile: { name: 'Cliente' } }],
        messages: [{ id: `wamid-${texto}`, from: '5584911112222', type: 'text', text: { body: texto } }],
      } }] }],
    };
    await request(app.getHttpServer())
      .post('/webhooks/meta').set('content-type', 'application/json')
      .set('x-hub-signature-256', 'sha256=' + createHmac('sha256', META_APP_SECRET).update(JSON.stringify(corpo)).digest('hex'))
      .send(corpo).expect(200);
  };

  beforeAll(async () => {
    ({ app, prisma } = await subirApp());
    app.get(RealtimeService).ligar(app.getHttpServer());
    await app.listen(0);
    porta = (app.getHttpServer().address() as AddressInfo).port;
  });

  afterAll(async () => {
    await limparBanco(prisma);
    await app?.close();
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');
    await criarCanalVerificado(prisma, A.businessUnit.id, 'OFICIAL', PHONE_A, { requiresWindow: true });
  });

  it('recusa ANTES do upgrade: sem sessão, o socket nem chega a abrir', async () => {
    // 401 no handshake, não "abre e fecha" — quem não tem acesso não recebe
    // conexão nenhuma, nem por um instante.
    await expect(conectar(porta, 'nada=1')).rejects.toThrow(/401/);
  });

  it('recusa cookie forjado', async () => {
    await expect(conectar(porta, 'lh_session=forjado.forjado')).rejects.toThrow(/401/);
  });

  it('recusa quem teve a conta inativada, mesmo com cookie válido', async () => {
    const cookie = await login(app, 'dono@alfa.test');
    await prisma.appUser.update({ where: { id: A.owner.id }, data: { status: 'INATIVO' } });
    await expect(conectar(porta, cookie)).rejects.toThrow(/401/);
  });

  it('quem tem grant na BU recebe a mensagem que chegou', async () => {
    const ws = await conectar(porta, await login(app, 'dono@alfa.test'));
    const evento = esperarEvento(ws, 'mensagem');

    await receber('oi');

    const recebido = await evento;
    expect(recebido).toMatchObject({ tipo: 'mensagem', buId: A.businessUnit.id, direcao: 'IN' });
    ws.close();
  });

  it('CROSS-TENANT: o dono de Beta NÃO recebe evento da BU de Alfa', async () => {
    const wsAlfa = await conectar(porta, await login(app, 'dono@alfa.test'));
    const wsBeta = await conectar(porta, await login(app, 'dono@beta.test'));

    const naAlfa = esperarEvento(wsAlfa, 'mensagem');
    const naBeta = esperarEvento(wsBeta, 'mensagem', 1500);

    await receber('segredo da alfa');

    expect(await naAlfa).toBeTruthy();
    // É este o vazamento que o Hub tem hoje: broadcast para todos os conectados.
    expect(await naBeta).toBeNull();
    expect(B.businessUnit.id).toBeTruthy();
    wsAlfa.close();
    wsBeta.close();
  });

  it('usuário da MESMA Mantenedora sem grant naquela BU também não recebe', async () => {
    const outraBu = await request(app.getHttpServer())
      .post('/api/bff/business-units').set('Cookie', await login(app, 'dono@alfa.test')).set('x-requested-with', 'teste')
      .send({ nome: 'Outro número' }).expect(201);

    await criarUsuario(prisma, A.mantenedora.id, outraBu.body.id, 'so-outra@alfa.test', 'ATENDENTE');
    const ws = await conectar(porta, await login(app, 'so-outra@alfa.test'));
    const evento = esperarEvento(ws, 'mensagem', 1500);

    await receber('não é para você');

    expect(await evento).toBeNull();
    ws.close();
  });

  it('o socket some da lista quando o cliente desconecta', async () => {
    const realtime = app.get(RealtimeService);
    const antes = realtime.contarAssinantes();
    const ws = await conectar(porta, await login(app, 'dono@alfa.test'));
    expect(realtime.contarAssinantes()).toBe(antes + 1);

    ws.close();
    await new Promise((r) => setTimeout(r, 300));
    expect(realtime.contarAssinantes()).toBe(antes);
  });
});

```

## Frozen file: api-app/test/webhooks.e2e-spec.ts

Original SHA-256: `0de3e64e4dac55fd4224b7ebf087ad95a0d857eaf058fd95251a6c8caebb0d9f`; bytes:9995.

```text
import { INestApplication } from '@nestjs/common';
import { createHmac } from 'node:crypto';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import {
  EVOLUTION_WEBHOOK_SECRET,
  META_APP_SECRET,
  criarCanalVerificado,
  criarMantenedora,
  limparBanco,
  login,
  subirApp,
} from './helpers';

describe('webhooks de entrada', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let A: Awaited<ReturnType<typeof criarMantenedora>>;
  let B: Awaited<ReturnType<typeof criarMantenedora>>;

  const PHONE_A = 'phone-da-alfa';
  const INSTANCIA_A = 'instancia-da-alfa';

  const assinar = (corpo: object) =>
    'sha256=' + createHmac('sha256', META_APP_SECRET).update(JSON.stringify(corpo)).digest('hex');

  const eventoMeta = (de: string, texto: string, phoneNumberId = PHONE_A) => ({
    entry: [
      {
        changes: [
          {
            field: 'messages',
            value: {
              metadata: { phone_number_id: phoneNumberId },
              contacts: [{ profile: { name: 'Cliente' } }],
              messages: [{ id: `wamid-${texto}`, from: de, type: 'text', text: { body: texto } }],
            },
          },
        ],
      },
    ],
  });

  const postMeta = (corpo: object, assinatura?: string) => {
    const req = request(app.getHttpServer()).post('/webhooks/meta').set('content-type', 'application/json');
    if (assinatura !== undefined) req.set('x-hub-signature-256', assinatura);
    return req.send(corpo);
  };

  const postEvolution = (corpo: object, segredo = EVOLUTION_WEBHOOK_SECRET) =>
    request(app.getHttpServer()).post(`/webhooks/evolution/${segredo}`).send(corpo);

  beforeAll(async () => {
    ({ app, prisma } = await subirApp());
  });

  afterAll(async () => {
    await limparBanco(prisma);
    await app?.close();
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');
    await criarCanalVerificado(prisma, A.businessUnit.id, 'OFICIAL', PHONE_A, { requiresWindow: true });
    await criarCanalVerificado(prisma, A.businessUnit.id, 'NAO_OFICIAL', INSTANCIA_A, { requiresWindow: false });
  });

  describe('Meta — assinatura (fecha o risco S2)', () => {
    it('aceita o evento assinado corretamente e cria a conversa', async () => {
      const corpo = eventoMeta('5584999991111', 'oi');
      await postMeta(corpo, assinar(corpo)).expect(200);

      const conversa = await prisma.conversation.findFirstOrThrow({ where: { buId: A.businessUnit.id } });
      expect(conversa.contact).toBe('5584999991111');
      expect(conversa.status).toBe('QUEUED');
      expect(conversa.unreadCount).toBe(1);
      expect(conversa.displayName).toBe('Cliente');
    });

    it('RECUSA evento sem assinatura — é o que os dois sistemas antigos aceitam hoje', async () => {
      const corpo = eventoMeta('5584999992222', 'injetada');
      await postMeta(corpo).expect(403);
      expect(await prisma.conversation.count()).toBe(0);
    });

    it('RECUSA assinatura de outro segredo', async () => {
      const corpo = eventoMeta('5584999993333', 'forjada');
      const errada = 'sha256=' + createHmac('sha256', 'outro-segredo').update(JSON.stringify(corpo)).digest('hex');
      await postMeta(corpo, errada).expect(403);
      expect(await prisma.conversation.count()).toBe(0);
    });

    it('RECUSA corpo alterado depois de assinado — a prova é sobre os bytes brutos', async () => {
      const original = eventoMeta('5584999994444', 'valor-original');
      const assinatura = assinar(original);
      const adulterado = eventoMeta('5584999994444', 'valor-trocado');
      await postMeta(adulterado, assinatura).expect(403);
      expect(await prisma.conversation.count()).toBe(0);
    });

    it('a verificação de endpoint devolve o challenge só com o verify token certo', async () => {
      await request(app.getHttpServer())
        .get('/webhooks/meta?hub.mode=subscribe&hub.verify_token=verify-token-de-teste&hub.challenge=12345')
        .expect(200)
        .expect('12345');

      await request(app.getHttpServer())
        .get('/webhooks/meta?hub.mode=subscribe&hub.verify_token=errado&hub.challenge=12345')
        .expect(403);
    });
  });

  describe('Meta — alocação da BU', () => {
    it('número desconhecido não cria nada, e não encosta na outra Mantenedora', async () => {
      const corpo = eventoMeta('5584999995555', 'perdida', 'phone-que-ninguem-tem');
      await postMeta(corpo, assinar(corpo)).expect(200);

      expect(await prisma.conversation.count()).toBe(0);
      expect(await prisma.conversation.count({ where: { buId: B.businessUnit.id } })).toBe(0);
      // Sem uma identidade durável não há BU confiável para associar nem payload para reter.
      expect(await prisma.webhookEvent.count()).toBe(0);
    });

    it('a conversa pendura na BU dona do NÚMERO que recebeu', async () => {
      const corpo = eventoMeta('5584999996666', 'oi');
      await postMeta(corpo, assinar(corpo)).expect(200);

      const conversa = await prisma.conversation.findFirstOrThrow();
      expect(conversa.buId).toBe(A.businessUnit.id);
    });
  });

  describe('Evolution — segredo no caminho', () => {
    const upsert = (jid: string, texto: string, fromMe = false, pushName = 'Contato') => ({
      event: 'messages.upsert',
      instance: INSTANCIA_A,
      data: { key: { remoteJid: jid, fromMe, id: `evo-${texto}` }, pushName, message: { conversation: texto } },
    });

    it('recusa segredo errado', async () => {
      await postEvolution(upsert('5584999997777@s.whatsapp.net', 'x'), 'segredo-errado-mesmo-tamanho').expect(403);
      expect(await prisma.conversation.count()).toBe(0);
    });

    it('aceita com o segredo certo e grava o contato sem o JID', async () => {
      await postEvolution(upsert('5584999998888@s.whatsapp.net', 'oi')).expect(200);

      const conversa = await prisma.conversation.findFirstOrThrow();
      expect(conversa.contact).toBe('5584999998888');
      expect(conversa.contactType).toBe('PESSOA');
      expect(conversa.displayName).toBe('Contato');
    });

    it('mensagem NOSSA (fromMe) não usa pushName como nome do contato', async () => {
      await postEvolution(upsert('5584999999999@s.whatsapp.net', 'resposta', true, 'Nome do nosso número')).expect(200);

      const conversa = await prisma.conversation.findFirstOrThrow();
      expect(conversa.displayName).toBeNull();
      expect(conversa.unreadCount).toBe(0);
    });

    it('grupo entra como GRUPO e mantém o identificador', async () => {
      await postEvolution(upsert('123456789@g.us', 'no grupo')).expect(200);
      const conversa = await prisma.conversation.findFirstOrThrow();
      expect(conversa.contactType).toBe('GRUPO');
      expect(conversa.contact).toBe('123456789@g.us');
    });

    it('connection.update marca o canal como conectado e grava o número da wuid', async () => {
      await postEvolution({
        event: 'connection.update',
        instance: INSTANCIA_A,
        data: { state: 'open', wuid: '5584912345678@s.whatsapp.net' },
      }).expect(200);

      const canal = await prisma.buChannel.findFirstOrThrow({ where: { evolutionInstanceName: INSTANCIA_A } });
      expect(canal.status).toBe('CONECTADO');
      const bu = await prisma.businessUnit.findUniqueOrThrow({ where: { id: A.businessUnit.id } });
      // O wuid do webhook não substitui o telefone canônico confirmado na BU.
      expect(bu.phone).toBe('5584999990000');
    });
  });

  describe('fila de atendimento (ADR-0009 §2)', () => {
    const receber = async (texto: string) => {
      const corpo = eventoMeta('5584911112222', texto);
      await postMeta(corpo, assinar(corpo)).expect(200);
    };

    it('mensagem nova reabre conversa FECHADA e solta a atribuição', async () => {
      await receber('primeira');
      const conversa = await prisma.conversation.findFirstOrThrow();
      await prisma.conversation.update({
        where: { id: conversa.id },
        data: { status: 'CLOSED', attendantName: 'Fulano', attendantOrigin: 'INTERNO' },
      });

      await receber('voltei');

      const depois = await prisma.conversation.findUniqueOrThrow({ where: { id: conversa.id } });
      expect(depois.status).toBe('QUEUED');
      expect(depois.attendantName).toBeNull();
    });

    it('conversa EM ATENDIMENTO não é rebaixada por mensagem nova', async () => {
      await receber('primeira');
      const conversa = await prisma.conversation.findFirstOrThrow();
      await prisma.conversation.update({
        where: { id: conversa.id },
        data: { status: 'IN_SERVICE', attendantName: 'Fulano', attendantOrigin: 'INTERNO' },
      });

      await receber('mais uma');

      const depois = await prisma.conversation.findUniqueOrThrow({ where: { id: conversa.id } });
      expect(depois.status).toBe('IN_SERVICE');
      expect(depois.attendantName).toBe('Fulano');
      expect(depois.unreadCount).toBe(2);
    });
  });

  describe('o dado recebido respeita o escopo', () => {
    it('CROSS-TENANT: o dono de Beta não enxerga a conversa que entrou na BU de Alfa', async () => {
      const corpo = eventoMeta('5584933334444', 'segredo da alfa');
      await postMeta(corpo, assinar(corpo)).expect(200);

      const cookieBeta = await login(app, 'dono@beta.test');
      const res = await request(app.getHttpServer())
        .get(`/api/bff/business-units/${A.businessUnit.id}`)
        .set('Cookie', cookieBeta)
        .expect(404);
      expect(res.body.code).toBe('NAO_ENCONTRADO');
    });
  });
});

```

## Frozen file: api-app/src/infra/session/session.service.ts

Original SHA-256: `884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200`; bytes:5483.

```text
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

## Frozen file: api-app/src/surfaces/bff/session.middleware.ts

Original SHA-256: `80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211`; bytes:5651.

```text
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

## Frozen file: api-app/src/surfaces/public/api-key.middleware.ts

Original SHA-256: `f76cd8854c8145c4b456e8c9d2d1ab000c17bc5278af76997745b5696edd9877`; bytes:1274.

```text
import { Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common';
import type { NextFunction, Request, Response } from 'express';
import { ApiKeyService, ContextoDaChave } from '../../domain/integration/api-key.service';

declare global {
  // eslint-disable-next-line @typescript-eslint/no-namespace
  namespace Express {
    interface Request {
      chave?: ContextoDaChave;
    }
  }
}

/**
 * Guard da superfície pública (ADR-0006, ADR-0010): chave de parceiro, nunca
 * cookie. **A Mantenedora sai da CHAVE** — nunca do corpo, do path ou de
 * cabeçalho.
 */
@Injectable()
export class ApiKeyMiddleware implements NestMiddleware {
  constructor(private readonly chaves: ApiKeyService) {}

  async use(req: Request, _res: Response, next: NextFunction): Promise<void> {
    const header = req.headers.authorization ?? '';
    const match = /^Bearer\s+(.+)$/i.exec(header);
    const recusa = () => {
      throw new UnauthorizedException({
        error: 'Chave de API ausente, inválida ou revogada.',
        code: 'NAO_AUTENTICADO',
      });
    };

    if (!match) recusa();
    const ctx = await this.chaves.resolver(match![1].trim());
    if (!ctx) recusa();

    req.chave = ctx!;
    next();
  }
}

```

## Frozen file: api-app/src/domain/access/access.service.ts

Original SHA-256: `2ef3761a138d7c8c386c5ddb4bf2a2000c960328789834bde5e12135a1ea66e7`; bytes:2390.

```text
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { Role } from './role';
import { Grant, buNoEscopo, escopoDoUsuario, papelNaBu, papelNaMantenedora } from './scope';

/**
 * A única porta por onde um `bu_id` vindo do request pode passar.
 *
 * Regra 0 do CLAUDE.md: toda leitura de dado de negócio filtra por BU dentro do
 * escopo do usuário, e a Mantenedora intersecciona esse conjunto — nunca o soma.
 */
@Injectable()
export class AccessService {
  constructor(private readonly prisma: PrismaService) {}

  async grantsDoUsuario(userId: string): Promise<Grant[]> {
    const linhas = await this.prisma.userBuRole.findMany({
      where: { userId, bu: { status: 'ATIVO' } },
      select: { buId: true, role: true, grantedViaTipo: true, grantedViaId: true },
    });
    return linhas.map((l) => ({
      buId: l.buId,
      role: l.role as Role,
      origemTipo: l.grantedViaTipo,
      origemId: l.grantedViaId,
    }));
  }

  async escopo(userId: string): Promise<string[]> {
    return escopoDoUsuario(await this.grantsDoUsuario(userId));
  }

  /**
   * Resolve uma BU pedida contra os grants. Devolve null quando não pode ser
   * vista — e quem chama responde **404**, não 403: confirmar a existência de
   * recurso alheio entrega informação a quem varre identificadores.
   */
  async resolverBu(userId: string, buId: string): Promise<{ id: string; name: string; papel: Role } | null> {
    const grants = await this.grantsDoUsuario(userId);
    if (!buNoEscopo(grants, buId)) return null;

    const bu = await this.prisma.businessUnit.findFirst({
      where: { id: buId, status: 'ATIVO' },
      select: { id: true, name: true },
    });
    if (!bu) return null;

    const papel = papelNaBu(grants, buId);
    if (!papel) return null;
    return { id: bu.id, name: bu.name, papel };
  }

  /** Papel na Mantenedora: calculado, nunca armazenado (ADR-0008 §4). */
  async papelNaMantenedoraDoUsuario(userId: string, mantenedoraId: string): Promise<Role | null> {
    const grants = await this.grantsDoUsuario(userId);
    const bus = await this.prisma.businessUnit.findMany({
      where: { mantenedoraId, status: 'ATIVO' },
      select: { id: true },
    });
    return papelNaMantenedora(grants, bus.map((b) => b.id));
  }
}

```

## Frozen file: api-app/src/domain/access/scope.ts

Original SHA-256: `412f68eb157328855c87cb86b6b89cc1c267eee7068dc59c0abbe085074db26d`; bytes:5701.

```text
import { Role, atLeast, menorPapel } from './role';

// Escopo e papel derivado. A regra 0 do CLAUDE.md vive aqui: o escopo é o
// conjunto de BUs concedidas, e a Mantenedora INTERSECCIONA esse conjunto,
// nunca o soma.

/** De onde o grant veio (ADR-0017 §2). */
export type OrigemDoGrant = 'DIRETO' | 'SETOR' | 'MANTENEDORA';

export interface Grant {
  buId: string;
  role: Role;
  origemTipo: OrigemDoGrant;
  /** null quando DIRETO; o id do setor ou da Mantenedora quando é expansão. */
  origemId: string | null;
}

/** As BUs que o usuário enxerga. Sem grant, conjunto vazio — nunca "todas". */
export function escopoDoUsuario(grants: readonly Grant[]): string[] {
  return [...new Set(grants.map((g) => g.buId))];
}

/**
 * A BU pedida está no escopo? É a única porta por onde um bu_id vindo do
 * request pode passar.
 */
export function buNoEscopo(grants: readonly Grant[], buId: string): boolean {
  return grants.some((g) => g.buId === buId);
}

/** O papel numa BU específica. Ausência de grant é negação, não fallback. */
export function papelNaBu(grants: readonly Grant[], buId: string): Role | null {
  return grants.find((g) => g.buId === buId)?.role ?? null;
}

/**
 * Papel na Mantenedora — CALCULADO, nunca armazenado (ADR-0008 §4):
 *
 *  - sem grant em nenhuma BU  -> null (não enxerga)
 *  - grant em ALGUMAS         -> ATENDENTE (enxerga, mas não administra)
 *  - grant em TODAS           -> o MENOR papel entre elas
 *
 * Mantenedora sem BU nenhuma devolve null: "administrada por ninguém", não
 * "por qualquer um".
 *
 * O piso do grant parcial era `VIEWER` e passou a ser `ATENDENTE` (ADR-0018 §2).
 * **Isso não afrouxa nada:** quem tinha VIEWER derivado não administrava, e quem
 * tem ATENDENTE derivado também não — `podeAdministrarMantenedora` continua
 * exigindo >= ADMIN em TODAS as BUs. A derivação nunca concedeu acesso a BU
 * alguma; ela só resume.
 */
export function papelNaMantenedora(
  grants: readonly Grant[],
  todasAsBusDaMantenedora: readonly string[],
): Role | null {
  if (todasAsBusDaMantenedora.length === 0) return null;

  const doEscopo = grants.filter((g) => todasAsBusDaMantenedora.includes(g.buId));
  if (doEscopo.length === 0) return null;
  if (doEscopo.length < todasAsBusDaMantenedora.length) return 'ATENDENTE';

  return menorPapel(doEscopo.map((g) => g.role));
}

/**
 * Administrar o agrupamento (conceder em lote, renomear, integrações) exige
 * papel >= ADMIN em TODAS as BUs.
 *
 * O conjunto vazio é negado ANTES da contagem, de propósito: "em todas" seria
 * verdadeiro por vacuidade numa Mantenedora sem BU, o que daria a qualquer um o
 * direito de administrá-la.
 */
export function podeAdministrarMantenedora(
  grants: readonly Grant[],
  todasAsBusDaMantenedora: readonly string[],
): boolean {
  const papel = papelNaMantenedora(grants, todasAsBusDaMantenedora);
  return papel !== null && atLeast(papel, 'ADMIN');
}

/**
 * Expansão: cria uma linha por BU, e GRANT DIRETO VENCE EXPANSÃO — a expansão só
 * cria onde não existe **nenhum** grant (ADR-0008 §4, regra 1).
 *
 * Vale para as duas origens, Mantenedora e Setor: a regra é a mesma, e é isso
 * que faz o Setor não ser um eixo novo de permissão, só mais uma proveniência
 * (ADR-0017 §2).
 *
 * É também este ponto que faz o grant do fundador nascer como expansão em vez de
 * direto: no gateway_unifast o fundador recebeu grant direto, a replicação não o
 * enxergou, e ele perdeu a administração da conta que criou.
 */
export function expandir(
  grantsAtuais: readonly Grant[],
  bus: readonly string[],
  role: Role,
  origemTipo: Exclude<OrigemDoGrant, 'DIRETO'>,
  origemId: string,
): Grant[] {
  const jaTemGrant = new Set(grantsAtuais.map((g) => g.buId));
  return bus.filter((buId) => !jaTemGrant.has(buId)).map((buId) => ({ buId, role, origemTipo, origemId }));
}

/**
 * Revogar em lote remove só o que AQUELA origem criou. O grant direto sobrevive,
 * e o que veio de outra origem também (ADR-0008 §4 regra 2, ADR-0017 §2).
 */
export function revogarExpansao(
  grants: readonly Grant[],
  origemTipo: Exclude<OrigemDoGrant, 'DIRETO'>,
  origemId: string,
): Grant[] {
  return grants.filter((g) => !(g.origemTipo === origemTipo && g.origemId === origemId));
}

/**
 * Mover um número de setor reescreve **só as expansões de setor daquele número**
 * (ADR-0017 §2, regra 5).
 *
 * Sai o que o setor antigo concedia; entra o que o novo concede, onde não houver
 * grant. O grant DIRETO sobrevive — e o vindo da Mantenedora também: os dois
 * continuam valendo e, por isso, **bloqueiam** a expansão do setor novo, que é a
 * regra 1 aplicada aqui.
 *
 * A diferença que isso preserva é entre "perdeu porque o time mudou" e "perdeu
 * porque alguém arrumou o cadastro".
 */
export function reescreverExpansaoAoMover(
  grantsDaBu: readonly { userId: string; origemTipo: OrigemDoGrant; origemId: string | null }[],
  setorAntigo: string,
  expansoesDoSetorNovo: readonly { userId: string; role: Role }[],
): { remover: string[]; adicionar: { userId: string; role: Role }[] } {
  const remover: string[] = [];
  // Quem continua com grant nesta BU depois da remoção — e por isso não recebe
  // expansão do setor novo.
  const permanecem = new Set<string>();

  for (const g of grantsDaBu) {
    if (g.origemTipo === 'SETOR' && g.origemId === setorAntigo) remover.push(g.userId);
    else permanecem.add(g.userId);
  }

  return { remover, adicionar: expansoesDoSetorNovo.filter((e) => !permanecem.has(e.userId)) };
}

```

## Frozen file: api-app/src/domain/access/require-role.ts

Original SHA-256: `1281da1ad31748e2bd78bffdf2962376d3413c7b37cfe6102448710cc7d7ce61`; bytes:1142.

```text
import { ForbiddenException, NotFoundException } from '@nestjs/common';
import { AccessService } from './access.service';
import { Role, atLeast } from './role';

/**
 * Resolve a BU do path contra os grants e exige papel mínimo.
 *
 * As duas negações são diferentes de propósito (ADR-0008, ADR-0009):
 *  - **fora do escopo → 404**: confirmar que o recurso existe entrega informação
 *    a quem varre identificadores, e vale inclusive para BU de outra Mantenedora;
 *  - **dentro do escopo, papel insuficiente → 403**: o recurso é seu, o poder é
 *    que não alcança.
 */
export async function exigirPapelNaBu(
  access: AccessService,
  userId: string,
  buId: string,
  minimo: Role,
): Promise<{ id: string; name: string; papel: Role }> {
  const bu = await access.resolverBu(userId, buId);
  if (!bu) throw new NotFoundException({ error: 'Não encontrado.', code: 'NAO_ENCONTRADO' });

  if (!atLeast(bu.papel, minimo)) {
    throw new ForbiddenException({
      error: `Esta ação exige papel ${minimo} nesta Business Unit.`,
      code: 'PAPEL_INSUFICIENTE',
    });
  }
  return bu;
}

```

## Frozen file: api-app/src/domain/access/role.ts

Original SHA-256: `ec92764e75c52b754e430355d196137ca90de89b4c5ed6f3fb49a05da10e1b42`; bytes:1776.

```text
// Papéis e a aritmética deles. TRÊS (ADR-0018): o `VIEWER` saiu junto com o eixo
// de capacidades, e disponibilidade passou a ser MÓDULO (ADR-0016), não
// permissão de usuário.
//
// `ATENDENTE` fica em português no meio de valores em inglês pelo mesmo motivo
// que `MEMBRO` ficava (ADR-0011, Emenda 1): é o nome que a casa usa para a
// função, e traduzir inventaria um dialeto que ninguém fala.

export type Role = 'OWNER' | 'ADMIN' | 'ATENDENTE';

/** Rank crescente. Comparar papel é comparar rank, nunca string. */
const RANK: Record<Role, number> = {
  ATENDENTE: 0,
  ADMIN: 1,
  OWNER: 2,
};

export function rankOf(role: Role): number {
  return RANK[role];
}

/** `a` é pelo menos tão forte quanto `b`? */
export function atLeast(a: Role, b: Role): boolean {
  return RANK[a] >= RANK[b];
}

/**
 * O MENOR papel de um conjunto. Devolve null para conjunto vazio — a ausência
 * é negação, nunca "qualquer um" (ADR-0008 §4).
 */
export function menorPapel(roles: readonly Role[]): Role | null {
  if (roles.length === 0) return null;
  return roles.reduce((menor, atual) => (RANK[atual] < RANK[menor] ? atual : menor));
}

/**
 * Revogar ou rebaixar exige papel MAIOR OU IGUAL ao do alvo (ADR-0008 §4, que
 * importou a regra do gateway_unifast já corrigida). Sem isto, um ADMIN rebaixa o OWNER.
 */
export function podeRevogarOuRebaixar(ator: Role, alvo: Role): boolean {
  return atLeast(ator, alvo);
}

/**
 * Quem cria uma BU recebe NO MÁXIMO o próprio papel — fecha a auto-promoção na
 * criação (ADR-0008 §4).
 */
export function papelAoCriarBu(papelDoCriador: Role, papelPedido: Role): Role {
  return atLeast(papelPedido, papelDoCriador) ? papelDoCriador : papelPedido;
}

```

## Frozen file: api-app/src/infra/http/body-parsers.ts

Original SHA-256: `0f65f24e300b2204362fff3ee1c799a35baecb1c57d141fe0ac0957091a5e624`; bytes:1023.

```text
import type { RawBodyRequest } from '@nestjs/common';
import type { NestExpressApplication } from '@nestjs/platform-express';
import express from 'express';
import type { Request } from 'express';

/**
 * Guarda o corpo BRUTO junto do corpo parseado.
 *
 * A assinatura do webhook da Meta é verificada sobre os bytes que chegaram —
 * sobre JSON reserializado ela falharia, ou aceitaria um payload alterado com a
 * mesma semântica. O `rawBody: true` do NestFactory não populou `req.rawBody`
 * nesta versão (verificado por sonda no e2e), então a captura é explícita.
 *
 * Produção e teste chamam ESTA função: assim o e2e prova a fiação de verdade,
 * não uma parecida.
 */
export function configurarBodyParsers(app: NestExpressApplication): void {
  app.use(
    express.json({
      limit: '1mb',
      verify: (req, _res, buf) => {
        (req as RawBodyRequest<Request>).rawBody = Buffer.from(buf);
      },
    }),
  );
  app.use(express.urlencoded({ extended: true }));
}

```

## Frozen file: api-app/src/surfaces/public/conversations.controller.ts

Original SHA-256: `670e8bca048111b0b83d0700632980131a85c0342da3254772b5fe15e8f1c962`; bytes:9748.

```text
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
import { ApiKeyService } from '../../domain/integration/api-key.service';
import { RateLimitService } from '../../domain/integration/rate-limit.service';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { PrismaService } from '../../infra/prisma/prisma.service';

const TETO = 500;

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
    const limite = Math.min(Number(q.limit) || 200, TETO);

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
      include: { messages: { orderBy: { createdAt: 'desc' }, take: 1 } },
    });

    const conversas = await Promise.all(
      linhas.slice(0, limite).map(async (c) => {
        const janela = await this.conversas.estadoDaJanela(c.id, buId);
        return {
          telefone: c.contact,
          nome_whatsapp: c.displayName,
          status: c.status,
          atendendo: c.attendantName,
          ultima_mensagem: c.messages[0]?.content ?? null,
          ultima_direcao: c.messages[0] ? (c.messages[0].direction === 'OUT' ? 'enviada' : 'recebida') : null,
          ultima_em: c.lastMessageAt?.toISOString() ?? null,
          nao_lidas: c.unreadCount,
          // Campo generalizado: quem integrou só o Hub recebe `true` e não muda
          // nada; quem integrou a Central continua lendo o que já lia.
          janela_aberta: janela.aberta,
          janela_expira_em: janela.expiraEm?.toISOString() ?? null,
        };
      }),
    );

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
    const limite = Math.min(Number(q.limit) || 100, TETO);

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
    const m = await this.conversas.responder(conversa.id, texto, { userId: '', nome: atendente });

    // Quem responde pela API pública não é usuário daqui: fica só o snapshot do
    // nome, e a origem EXTERNO (ADR-0009 §2).
    await this.prisma.message.update({ where: { id: m.id }, data: { authorUserId: null } });
    await this.prisma.conversation.update({
      where: { id: conversa.id },
      data: { attendantOrigin: 'EXTERNO', attendantUserId: null, attendantName: atendente },
    });

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

## Frozen file: api-app/src/surfaces/bff/conversations.controller.ts

Original SHA-256: `0b5c46a78aafd8085b609ad711bcdb7626263094f434240f37b8700f20291565`; bytes:5502.

```text
import { BadRequestException, Body, Controller, Get, HttpCode, Param, Post, Query, Req } from '@nestjs/common';
import type { Request } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { RegistroDeAtividade } from '../../domain/historico/registro.service';
import { ator } from './setores.controller';
import { validarConsultaTimeline } from '../../domain/inbox/timeline-pagination';

const ABAS = ['QUEUED', 'IN_SERVICE', 'CLOSED'] as const;

/** A inbox por BU (ADR-0009): uma tela para os dois canais. */
@Controller('api/bff')
export class ConversationsController {
  constructor(
    private readonly access: AccessService,
    private readonly conversas: ConversationsService,
    private readonly registro: RegistroDeAtividade,
  ) {}

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

    const m = await this.conversas.responder(conversa.id, texto, {
      userId: req.usuario!.id,
      nome: req.usuario!.nome,
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

## Frozen file: api-app/src/main.ts

Original SHA-256: `05ff096cdcf67a8a153736264ed46a7faf9f5c0f45325c2d3fed95188fb2b1ad`; bytes:5963.

```text
import { Logger } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import type { NestExpressApplication } from '@nestjs/platform-express';
import { AppModule } from './app.module';
import { normalizarSameSite, valorDeSameSiteEhSuspeito } from './infra/session/session.service';
import { RealtimeService } from './realtime/realtime.service';
import { configurarBodyParsers } from './infra/http/body-parsers';
import { origensPermitidas, origensSemEsquema } from './infra/http/origens';
import { lerModulos, verificarConfiguracao } from './infra/config/modulos';
import { migracoesPendentes } from './infra/prisma/migracoes';
import { PrismaService } from './infra/prisma/prisma.service';

async function bootstrap(): Promise<void> {
  // ANTES de qualquer coisa: configuração incoerente é defeito de implantação, e
  // precisa aparecer na hora de implantar — não como 503 no meio de um
  // atendimento (ADR-0016 §2 e Emenda 2 §1).
  verificarConfiguracao();

  // bodyParser: false + parsers próprios: é assim que o corpo BRUTO sobrevive
  // até a verificação de assinatura do webhook da Meta (ver body-parsers.ts).
  const app = await NestFactory.create<NestExpressApplication>(AppModule, { bodyParser: false });
  configurarBodyParsers(app);

  // A Railway termina o TLS e encaminha; sem isto o IP visto é o do proxy, e o
  // bloqueio por tentativa de senha (ADR-0007) contaria o mundo inteiro como um
  // só endereço.
  app.set('trust proxy', 1);

  // O front é serviço próprio, num subdomínio do MESMO domínio (ADR-0015).
  // Origem fechada e credenciais ligadas: curinga é incompatível com cookie, e
  // trocar por "*" para "resolver CORS" faz o navegador recusar a sessão — o
  // sintoma vira "login não persiste".
  const origens = origensPermitidas(process.env.WEB_ORIGIN);

  // Origem sem esquema NUNCA casa com o cabeçalho Origin, e o sintoma é o
  // navegador bloqueando tudo sem citar a variável. Erro de digitação aqui não
  // pode virar um CORS mudo.
  const semEsquema = origensSemEsquema(origens);
  if (semEsquema.length) {
    throw new Error(
      `WEB_ORIGIN tem origem sem esquema: ${semEsquema.join(', ')}. ` +
        `Use https://${semEsquema[0]} — o navegador sempre manda o Origin com esquema, ` +
        'e sem ele a comparação nunca bate.',
    );
  }
  if (origens.length) {
    app.enableCors({ origin: origens, credentials: true });
  }

  // O WebSocket autentica pelo cookie no handshake e entrega só para quem tem
  // grant na BU do evento (ADR-0009 §5, fecha o risco S8).
  app.get(RealtimeService).ligar(app.getHttpServer());

  const log = new Logger('bootstrap');
  // Um aviso alto: quem herdar este ambiente precisa saber que a proteção de
  // CSRF está apoiada só no cabeçalho (ADR-0015, Emenda 1).
  if (normalizarSameSite(process.env.COOKIE_SAMESITE) === 'None') {
    log.warn(
      'COOKIE_SAMESITE=None — o cookie viaja cross-site e o CSRF depende só do X-Requested-With. ' +
        'Use apenas em stage sem domínio próprio. NUNCA em produção.',
    );
  }
  // Sem este aviso, um erro de digitação viraria o mesmo login mudo que a
  // variável existe para resolver — e ninguém suspeitaria da variável.
  if (valorDeSameSiteEhSuspeito(process.env.COOKIE_SAMESITE)) {
    log.error(
      `COOKIE_SAMESITE="${process.env.COOKIE_SAMESITE}" não é reconhecido; usando Lax. ` +
        'Os valores válidos são None, Lax e Strict.',
    );
  }

  // O teto da instalação, dito alto no boot: é o que separa "a Mantenedora não
  // contratou" de "esta instalação não sabe fazer" quando alguém for investigar
  // por que um módulo não aparece.
  const teto = lerModulos();
  const ligados = Object.entries(teto)
    .filter(([, v]) => v)
    .map(([k]) => k);
  log.log(
    `canal oficial: piso do produto (sempre ligado). ` +
      `Módulos desta instalação: ${ligados.length ? ligados.join(', ') : 'nenhum'}.`,
  );

  // Sem WEB_ORIGIN o CORS desliga E o link de convite sai relativo, que não abre
  // em caixa de entrada nenhuma (ADR-0025). Não é erro de boot — o
  // desenvolvimento roda em mesma origem, pelo proxy do Vite —, mas precisa ser
  // dito alto para não ser descoberto por um convite que ninguém consegue usar.
  if (!origens.length) {
    log.warn(
      'WEB_ORIGIN vazia: o CORS fica desligado e o link de convite sai SEM domínio. ' +
        'Em qualquer ambiente com front separado, defina-a.',
    );
  }

  // O aviso ANTES de qualquer requisição: banco atrás da imagem não aparece no
  // boot sozinho — aparece como 500 na primeira consulta que toca a tabela nova.
  // Custou duas rodadas em stage antes de virar esta mensagem.
  try {
    const pendentes = await migracoesPendentes(app.get(PrismaService));
    if (pendentes.length) {
      log.error(
        `BANCO ATRÁS DA IMAGEM: ${pendentes.length} migração(ões) pendente(s) — ` +
          `${pendentes.join(', ')}. Rode \`npx prisma migrate deploy\` de dentro do serviço. ` +
          'Até lá, as rotas que dependem delas respondem 503 BANCO_DESATUALIZADO.',
      );
    }
  } catch (e) {
    log.warn(`Não foi possível conferir as migrações pendentes: ${String(e)}`);
  }

  const port = Number(process.env.PORT ?? 3000);
  await app.listen(port, '0.0.0.0');
  console.log(
    `leadshug api ouvindo na porta ${port}` +
      (origens.length
        ? ` (CORS para ${origens.join(', ')})`
        : ' (sem WEB_ORIGIN: CORS desligado — só funciona se o front estiver na MESMA origem)'),
  );
}

void bootstrap().catch((e) => {
  // Configuração incoerente precisa sair com mensagem legível e código 1, não
  // com uma promessa rejeitada no meio de um stack trace do Nest.
  console.error(e instanceof Error ? e.message : String(e));
  process.exit(1);
});

```

## Frozen file: api-app/src/app.module.ts

Original SHA-256: `a59880adc1bd8250fdbf5d52637fc38fe3177a2615e1b25389716946da7ad420`; bytes:1857.

```text
import { Module } from '@nestjs/common';
import { APP_FILTER } from '@nestjs/core';
import { BancoAtrasadoFilter } from './infra/prisma/banco-atrasado.filter';
import { HealthModule } from './health/health.module';
import { PrismaModule } from './infra/prisma/prisma.module';
import { RealtimeModule } from './realtime/realtime.module';
import { RotinasModule } from './rotinas/rotinas.module';
import { BffModule } from './surfaces/bff/bff.module';
import { PublicApiModule } from './surfaces/public/public.module';
import { InternalModule } from './surfaces/internal/internal.module';
import { WebhooksModule } from './surfaces/webhooks/webhooks.module';

// Quatro superfícies de entrada, cada uma com guard próprio (ADR-0006), mais o
// /health, que não é superfície — é trava de plataforma (ADR-0002) — e as
// rotinas periódicas, que também não são superfície: ninguém as chama, elas
// acordam sozinhas (ADR-0023).
//
// NENHUM guard global é registrado aqui, e isso é deliberado: um APP_GUARD
// alcançaria também o /health, que precisa ser público, e a autenticação
// deixaria de ser propriedade da superfície.
@Module({
  imports: [
    PrismaModule,
    RealtimeModule,
    RotinasModule,
    HealthModule,
    BffModule,
    PublicApiModule,
    InternalModule,
    WebhooksModule,
  ],
  providers: [
    // Filtro de EXCEÇÃO registrado no MÓDULO, não no bootstrap: é assim que o
    // teste roda com a mesma fiação da produção. Registrado no `main.ts`, ele
    // existia só em produção — e o teste provaria outra coisa.
    //
    // Não é guard: não toca em autenticação, e o ADR-0006 continua valendo —
    // quem autentica é a superfície, pelo prefixo.
    { provide: APP_FILTER, useClass: BancoAtrasadoFilter },
  ],
})
export class AppModule {}

```

## Frozen file: api-app/test/setup-env.ts

Original SHA-256: `bfb97c57f39e252868b544437c6bf3128efa70613e5a7765d0aefb52f5b6a849`; bytes:795.

```text
// O e2e roda contra Postgres de verdade (ADR-0012 §4), então precisa do
// DATABASE_URL. Vitest não carrega .env sozinho; o Node carrega.
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';

const arquivo = resolve(__dirname, '..', '.env');
if (existsSync(arquivo)) {
  process.loadEnvFile(arquivo);
}

// O `.env` local pode habilitar o canal nÃ£o oficial para desenvolvimento.
// E2E precisa comeÃ§ar oficial-only e cada cenÃ¡rio que cobre o mÃ³dulo liga o
// teto explicitamente antes de subir o app.
// Use valores vazios/false, e nÃ£o `delete`: o Prisma pode recarregar o `.env`
// ao abrir a conexÃ£o e reintroduzir flags locais durante o boot do teste.
process.env.LH_CHANNEL_UNOFFICIAL = 'false';
process.env.LH_ARQUIVOS_DIR = '';

```

## Frozen file: api-app/vitest.config.e2e.ts

Original SHA-256: `ff76a3b94de4649d18f0f824a24bb45428afcbb751a872a6841a2e388f45f8ff`; bytes:683.

```text
import swc from 'unplugin-swc';
import { defineConfig } from 'vitest/config';

// E2E roda contra Postgres DE VERDADE (ADR-0012 §4): o que precisa ser provado
// é o filtro por BU dentro do SQL, e mock de repositório provaria só que o
// código chama o método.
export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['test/**/*.e2e-spec.ts'],
    testTimeout: 30_000,
    hookTimeout: 30_000,
    fileParallelism: false,
    maxWorkers: 1,
    minWorkers: 1,
    sequence: { concurrent: false, shuffle: false },
    setupFiles: ['./test/setup-env.ts'],
  },
  plugins: [swc.vite({ module: { type: 'es6' } })],
});

```

## Frozen file: api-app/package.json

Original SHA-256: `df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d`; bytes:1670.

```text
{
  "name": "@leadshug/api",
  "version": "0.1.0",
  "private": true,
  "description": "Núcleo unificado do LeadsHug — NestJS, quatro superfícies de entrada",
  "scripts": {
    "build": "nest build",
    "start": "node dist/main.js",
    "start:dev": "nest start --watch",
    "lint": "eslint \"{src,test}/**/*.ts\"",
    "test": "vitest run --config vitest.config.ts",
    "test:cov": "vitest run --coverage --config vitest.config.cov.ts",
    "test:e2e": "vitest run --config vitest.config.e2e.ts --no-file-parallelism --maxWorkers=1",
    "prisma:generate": "prisma generate",
    "prisma:migrate": "prisma migrate deploy",
    "prisma:dev": "prisma migrate dev"
  },
  "dependencies": {
    "@nestjs/common": "^11.0.0",
    "@nestjs/core": "^11.0.0",
    "@nestjs/platform-express": "^11.0.0",
    "@nestjs/schedule": "^6.1.3",
    "@prisma/client": "^6.0.0",
    "bcryptjs": "^2.4.3",
    "express": "^5.2.1",
    "prisma": "^6.0.0",
    "reflect-metadata": "^0.2.2",
    "rxjs": "^7.8.1",
    "ws": "^8.21.3"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@nestjs/cli": "^11.0.0",
    "@nestjs/schematics": "^11.0.0",
    "@nestjs/testing": "^11.0.0",
    "@types/bcryptjs": "^2.4.6",
    "@types/express": "^5.0.0",
    "@types/multer": "^2.2.0",
    "@types/node": "^22.0.0",
    "@types/supertest": "^6.0.2",
    "@types/ws": "^8.18.1",
    "@vitest/coverage-v8": "^2.1.0",
    "eslint": "^10.8.1",
    "supertest": "^7.0.0",
    "typescript": "^5.6.0",
    "typescript-eslint": "^8.67.0",
    "unplugin-swc": "^1.5.1",
    "vitest": "^2.1.0"
  },
  "engines": {
    "node": ">=22"
  }
}

```

# END OF COMPLETE FROZEN API PACKET
