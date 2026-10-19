# Tactical TODO — ST-CON-04

## Quick Start

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Title

LeadsHug — ST-CON-04: Nova conversa por contato e primeiro envio seguro

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** NotStarted
- **Created:** 2026-10-19
- **Template provenance:** copied from `delphi-ai/templates/todo_template.md` before refinement.

## Context

ST-CON-01 encerrou a prova local de cadastro e troca real dos dois transportes, incluindo retomada. A inbox responde a conversas recebidas, mas o operador ainda não abre atendimento informando telefone. Este contrato propõe essa abertura e o primeiro envio conforme o canal. Não reabre a investigação histórica do webhook nem supõe que um primeiro OUT cria janela oficial.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md`
- **Primary story ID:** ST-CON-04
- **Why this is the right current slice:** sequência solicitada: cadastro concluído → Nova conversa por contato → importação. Um objetivo de usuário e um ciclo de aprovação.
- **Direct-to-TODO rationale (required when `Feature brief = direct-to-todo`):** n/a; brief existente.

## Contract Boundary

- This TODO defines **WHAT** must be delivered and what counts as done.
- `Assumptions Preview` and `Execution Plan` below define **HOW** Delphi currently intends to deliver this contract.
- This TODO is **bounded but elastic**: Delphi may absorb local discoveries only while they remain inside the same primary objective and the same main approval/review/promotion conversation. Secondary modules may still be touched when they are subordinate to that same slice.
- If any assumption or plan step changes `Scope`, `Out of Scope`, `Definition of Done`, required validation semantics, public contract, or frozen decisions, update the TODO contract first and request renewed approval before execution continues.
- If the intended path explicitly authorizes a compatibility shim, fallback bridge, dual-read/dual-write period, or another non-canonical temporary construct, record that authorization in the TODO with exact scope, rationale, and removal/closeout condition. Reviewers must be able to distinguish an approved temporary exception from accidental workaround drift.

## Implementation Intent

- **Current delivery:** abertura/reuso de conversa por telefone na BU e primeiro envio explícito pelo canal escolhido; texto livre permitido e template textual aprovado quando obrigatório.
- **Planned next steps:** Railway de testes; histórico ST-CON-02/03; demais recursos de atendimento, sem execução neste TODO.
- **Anticipatory implementation authorized now:** none
- **Rationale:** um serviço de domínio para resolução do contato, um caminho compartilhado de envio/aceitação; sem CRM, campanhas ou plataforma genérica de jobs.

## Delivery Status Canon (Required)

- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** congelar minuta, arquitetura e crítica independentes, guardas pré-aprovação e apresentar o contrato ao usuário; não implementar antes do APROVADO específico.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** review
- **Why this state now:** revisão do contrato antes da primeira implementação; nenhum produto foi alterado.
- **Exit condition:** aprovação explícita do pacote revisado + ingestão binding e authority go autorizam handoff operacional.

## Scope

- [ ] SCOPE-01 — Formulário Nova conversa em Atendimento, com BU explícita, telefone internacional normalizado e confirmação do destinatário; ATENDENTE ou superior, sessão e anti-CSRF.
- [ ] SCOPE-02 — Resolver/criar uma conversa PESSOA por BU/contato por upsert atômico; reuso preserva histórico, responsável, estado e não lidas; abertura isolada não envia mensagem.
- [ ] SCOPE-03 — Primeiro envio com canal selecionado explicitamente e credencial/identidade atuais; não oficial conectado aceita texto; oficial aceita texto apenas na janela de 24h derivada de IN oficial confiável.
- [ ] SCOPE-04 — Fora da janela oficial, selecionar template APPROVED de texto da Messaging account do canal; idioma e variáveis textuais NAMED ou POSITIONAL, prévia e revalidação antes do envio. Sem template elegível, explicar bloqueio.
- [ ] SCOPE-05 — Idempotência durável do envio iniciado pelo novo fluxo, reconciliação de echo pelo owner compartilhado, estados de falha/ambiguidade e proteção contra respostas tardias ou troca de BU.
- [ ] SCOPE-06 — Testes de contrato, PostgreSQL concorrente e Playwright com backend real/build fresco; documentação canônica, revisões, evidências e prova física dos dois canais quando recursos elegíveis disponíveis.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; nenhuma entrega parcial reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

Planejamento pode avançar. Operador confirmou em 2026-10-19 que ainda não tem template aprovado; prova física oficial fora de janela dependerá de template elegível. Se continuar ausente na entrega, registrar bloqueio desse critério, sem aprovar por fixtures nem declarar Completed.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `api-app:feature/number-onboarding`, `web-app:feature/number-onboarding`, `root:feature/number-onboarding`; confirmar nomes no handoff antes de editar; Foundation:main.
- **Promotion lane path:** local feature → dev → stage → main; apenas documentação Foundation main possui publicação autônoma nesta etapa.
- **Lane-promoted threshold for this TODO:** dev, fora da autorização local atual.
- **Production-ready threshold for this TODO:** main e gates operacionais próprios; nenhum deploy/push de produto autorizado agora.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

n/a nesta preparação; produto não implementado, nenhum PR ou promoção reivindicado.

## Out of Scope

- [ ] Gestão/criação/edição/submissão de templates, mídia, botões, autenticação OTP, campanhas ou lotes.
- [ ] Importação de histórico, CRM, migração/coexistência de número e nova integração Typebot.
- [ ] Transferência entre agentes/aplicativos, standby/handover/take_control ou remoção de parceiro.
- [ ] Railway/deploy/publicação de produto, troca de túnel, rotação/leitura de segredos ou modificação de contas Meta durante planejamento.
- [ ] Worktrees/cópias auxiliares, gitlinks/.gitmodules manuais, leitura/listagem/stat/hash/mount de api-app/.local-files; alterações Delphi.

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
| foundation | foundation_documentation | a826e379e35c964683abc039fccab2c88dc1f18b | working_tree |

### Expected Changed Paths
| Repository | Path glob | Change types (`A/M/D/R/any`) | Reason |
| --- | --- | --- | --- |
| api | src/domain/inbox/** | any | resolução, política de canal/janela, intenção durável e aceitação |
| api | src/surfaces/bff/conversations.controller.ts | M | adapters do novo contrato |
| api | src/integrations/meta/meta.client.ts | M | catálogo e envio de template textual |
| api | src/integrations/meta/*.spec.ts | any | contratos HTTP e erros seguros |
| api | src/app.module.ts | M | registro DI se necessário |
| api | prisma/schema.prisma | M | intenção idempotente e snapshot textual |
| api | prisma/migrations/*_conversation_start*/migration.sql | A | migration PostgreSQL versionada |
| api | test/*conversation* | any | contratos/concorrência real |
| api | test/timeline-fixtures.cjs | M | extensão do provider fixture existente |
| api | test/browser-server.cjs | M | bootstrap determinístico do novo cenário |
| web | src/telas/Inbox.tsx | M | entrada, estado e integração do formulário |
| web | src/componentes/NovaConversa* | A | formulário e testes subordinados |
| web | src/api.ts | M | DTOs explícitos e erro estruturado |
| web | src/*conversation* | A | helpers de estado e testes |
| web | e2e/start-conversation* | A | Playwright do fluxo |
| web | e2e/number-onboarding-freshness.ts | M | manifest de fonte/servido se necessário |
| root | scripts/test-channels-local.sh | M | validar apenas superfícies públicas sem percorrer payload privado |
| foundation | todos/active/features/TODO-leadshug-start-conversation-by-contact.md | M | contrato/evidência |
| foundation | artifacts/reviews/leadshug-start-conversation-20261019/** | any | pacote específico |
| foundation | modules/inbox-and-conversations.md | M | consolidação após aprovação/entrega |
| foundation | modules/integrations-and-channels.md | M | template/canal após aprovação/entrega |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | vínculo da história |
| foundation | artifacts/dependency-readiness.md | M | dependências observadas |
| foundation | todos/completed/features/TODO-leadshug-start-conversation-by-contact.md | A | fechamento com gates satisfeitos |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .local-files/** | any | privado: nem ler, percorrer, comparar ou montar |
| api | .env* | any | segredos não integram contrato |
| root | .env* | any | nenhum segredo/runtime config |
| root | .gitmodules | any | pipeline-owned |
| root | api-app | any | gitlink pipeline-owned |
| root | web-app | any | gitlink pipeline-owned |
| root | delphi-ai | any | sem alteração metodológica |
| web | dist/** | any | artefato gerado não é fonte |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
Nenhuma análise executada. Guard API exige inventário positivo de caminhos públicos; não executar wrapper que percorra `.local-files`. Não chamar isso prova do repositório privado inteiro.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** concretização de DI, normalização, índices/intenção e fixtures necessários ao mesmo primeiro envio, preservando decisões e paths.
- **Must update or split the TODO:** novo tipo de template, envio geral idempotente em outros callers, fallback de canal, claim exactly-once, handover, mudanças fora de paths ou novo objetivo exigem reconvergência e aprovação.

## Definition of Done

- [ ] DOD-01 — Nova conversa valida telefone internacional, mostra destinatário e BU, abre/reusa exatamente uma conversa sem enviar nem criar CRM; cancelar antes de Abrir não persiste.
- [ ] DOD-02 — Reuso preserva histórico, unread, status e responsável; conversa nova QUEUED com unread zero é visível após refresh sem falsificar lastMessageAt.
- [ ] DOD-03 — Canal explícito e autorização server-side bloqueiam tenant/BU/recurso incorretos, canal não pronto e texto oficial fora da janela; IN não oficial não abre janela oficial.
- [ ] DOD-04 — Catálogo paginado e envio validam template APPROVED textual da conta corrente, idioma, formato e parâmetros; catálogo vazio/indisponível e formato incompatível possuem estados seguros sem fallback.
- [ ] DOD-05 — Intenção durável impede duas chamadas externas com a mesma chave; corrida de abertura/webhook mantém uma conversa; echo-first/sender-first mantém uma Message e autoria; ambiguidade nunca reenvia automaticamente.
- [ ] DOD-06 — Troca de BU, conversa, canal, revisão de formulário e respostas tardias preservam o rascunho correto e não abrem destino alheio; erros não indicam sucesso nem apagam conteúdo.
- [ ] DOD-07 — Harness de arquitetura executável, migration deploy/status e suites CI-equivalent completas passam; Playwright mutation usa API/DB reais e bundle servido comprovadamente fresco.
- [ ] DOD-08 — Prova física de primeiro envio não oficial e oficial por template elegível, seguida de resposta recebida, registrada separadamente; ausência de template mantém critério bloqueado sem simular prova externa.
- [ ] DOD-09 — Módulos consolidados, decisões verificadas, auditorias derivadas e guardas de entrega satisfeitos, sem P1/P2 aberto nem promessa de produção.

## Validation Steps

- [ ] VAL-01 — Executar bash scripts/test-channels-local.sh all no target descartável com dotenv fictício, migrations deploy/status, lint/build/unit/E2E e Web/browser completos; registrar fonte/served fingerprint.
- [ ] VAL-02 — Executar testes PostgreSQL com barreiras de concorrência para BU/contato, intenção, echo, webhook e revogação/geração; nenhuma rede dentro de transação.
- [ ] VAL-03 — Executar web-app/e2e/start-conversation.spec.ts via runner canônico, incluindo abrir/reusar, primeiro OUT, template/empty/error, negativas e respostas atrasadas contra BFF real.
- [ ] VAL-04 — Após readiness confirmada, operador executa prova real privada dos dois canais, incluindo template aprovado da conta correta e retorno; nenhuma mensagem real automática nesta preparação.
- [ ] VAL-05 — Executar arquitetura/aderência, segurança, pcv-1, TQA, final review, dívida, diff público e authority/completion/closeout antes de qualquer claim de entrega.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | DOD-01 — Nova conversa valida telefone internacional, mostra destinatário e BU, abre/reusa exatamente uma conversa sem enviar nem criar CRM; cancelar antes de Abrir não persiste. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-02 | Definition of Done | DOD-02 — Reuso preserva histórico, unread, status e responsável; conversa nova QUEUED com unread zero é visível após refresh sem falsificar lastMessageAt. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-03 | Definition of Done | DOD-03 — Canal explícito e autorização server-side bloqueiam tenant/BU/recurso incorretos, canal não pronto e texto oficial fora da janela; IN não oficial não abre janela oficial. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-04 | Definition of Done | DOD-04 — Catálogo paginado e envio validam template APPROVED textual da conta corrente, idioma, formato e parâmetros; catálogo vazio/indisponível e formato incompatível possuem estados seguros sem fallback. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-05 | Definition of Done | DOD-05 — Intenção durável impede duas chamadas externas com a mesma chave; corrida de abertura/webhook mantém uma conversa; echo-first/sender-first mantém uma Message e autoria; ambiguidade nunca reenvia automaticamente. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-06 | Definition of Done | DOD-06 — Troca de BU, conversa, canal, revisão de formulário e respostas tardias preservam o rascunho correto e não abrem destino alheio; erros não indicam sucesso nem apagam conteúdo. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-07 | Definition of Done | DOD-07 — Harness de arquitetura executável, migration deploy/status e suites CI-equivalent completas passam; Playwright mutation usa API/DB reais e bundle servido comprovadamente fresco. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-08 | Definition of Done | DOD-08 — Prova física de primeiro envio não oficial e oficial por template elegível, seguida de resposta recebida, registrada separadamente; ausência de template mantém critério bloqueado sem simular prova externa. | test/runtime/review | Prova física assistida e receipt redigido; fixture não substitui. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-09 | Definition of Done | DOD-09 — Módulos consolidados, decisões verificadas, auditorias derivadas e guardas de entrega satisfeitos, sem P1/P2 aberto nem promessa de produção. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| VAL-01 | Validation Steps | VAL-01 — Executar bash scripts/test-channels-local.sh all no target descartável com dotenv fictício, migrations deploy/status, lint/build/unit/E2E e Web/browser completos; registrar fonte/served fingerprint. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| VAL-02 | Validation Steps | VAL-02 — Executar testes PostgreSQL com barreiras de concorrência para BU/contato, intenção, echo, webhook e revogação/geração; nenhuma rede dentro de transação. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| VAL-03 | Validation Steps | VAL-03 — Executar web-app/e2e/start-conversation.spec.ts via runner canônico, incluindo abrir/reusar, primeiro OUT, template/empty/error, negativas e respostas atrasadas contra BFF real. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| VAL-04 | Validation Steps | VAL-04 — Após readiness confirmada, operador executa prova real privada dos dois canais, incluindo template aprovado da conta correta e retorno; nenhuma mensagem real automática nesta preparação. | test/runtime/review | Prova física assistida e receipt redigido; fixture não substitui. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| VAL-05 | Validation Steps | VAL-05 — Executar arquitetura/aderência, segurança, pcv-1, TQA, final review, dívida, diff público e authority/completion/closeout antes de qualquer claim de entrega. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Template textual APPROVED da Messaging account do canal oficial | primeiro OUT fora de janela | failing | 2026-10-19 | usuário: ainda não tem template aprovado | planejamento e fixtures seguem; prova física fica pendente; não criar/submeter nesta etapa |
| Meta/Evolution e túnel local | prova física | unknown | última prova ST-CON-01 CP108 | nenhuma nova consulta neste TODO | revalidar readiness antes da prova, não reciclar host como garantia |
| Runner Docker/Node22/PG16 | integração e browser | unknown | fonte scripts/test-channels-local.sh | inspecionado, não executado aqui | corrigir varredura privada antes de executar |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs,react,vite,postgresql,prisma,docker
- **Expected supporting profiles:** strategic-cto,operational-devops,assurance-tester-quality,assurance-security-adversarial
- **Scope-check command:** python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto
- **Gate 0:** Genesis rejeitado; projeto e módulos canônicos existentes. Planejamento atual strategic-cto, sem código.

### Handoff Log (Update when execution crosses profile boundaries)
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | implementar após APROVADO | API/Web e testes | planned |
| operational-coder | operational-devops | publicação local e readiness | runner/containers próprios | planned |
| operational-coder | assurance-tester-quality | TQA e aderência | pacote limitado | planned |
| operational-coder | assurance-security-adversarial | auth/idempotência/segredos | BFF e adapter | planned |

## Complexity

- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section
- **Why this level:** primeira escrita BFF com side effect externo, templates novos, idempotência durável e races Web/PostgreSQL; um único objetivo apesar de múltiplas superfícies.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** foundation_documentation/modules/inbox-and-conversations.md
- **Secondary module docs (if any):** foundation_documentation/modules/integrations-and-channels.md
- **Planned decision promotion targets (module sections):** inbox: Nova conversa ST-CON-04; integrations: Catálogo/envio textual scoped ST-CON-04.
- **Module decision consolidation targets (required):** mesmos alvos, com ledger D-01..D-08 e referência ao TODO; não apresentar esta minuta como contrato já implementado.

## Decision Pending (Resolve Before Freeze)

Nenhuma decisão material aberta na proposta. Disponibilidade de template é dependência de prova, não permissão para contornar janela.

## Decisions (Resolved Before Freeze)

- [x] D-01 — Abrir/reusar por POST /api/bff/business-units/:buId/conversations/open com {telefone}. Telefone exige DDI explícito (+ opcional), remove apenas espaços/parênteses/hífen/ponto, rejeita letras/ramal/grupo, 8–15 dígitos e primeiro não zero. Não inferir país nem variantes de nono dígito. Autorizar BU/ATENDENTE antes de validação detalhada; 401/403/404 scoped. Retorno {conversaId,criada,contact}; nenhuma chamada externa. Snapshot: Constituição BU/Contato e inbox invariants preservados.
- [x] D-02 — Upsert pelo índice buId/contact existente; nova PESSOA QUEUED/unread0/lastMessageAt null; abrir não assume nem reabre existente. Ordenação usa COALESCE(lastMessageAt,createdAt) desc + id desc para listar vazias deterministicamente; não escrever data falsa. Abrir persiste mesmo se operador fechar depois: é atendimento vazio visível; antes de Abrir, cancelar não persiste. Nenhuma alteração em paginação de mensagens. Snapshot: ST-ATT-01 preservado; No Prior Decision para abertura manual.
- [x] D-03 — GET /api/bff/conversations/:id/start-options informa canais da BU com capacidade/explicação, geração e janela. Primeiro envio usa POST /api/bff/conversations/:id/initial-messages, Idempotency-Key UUID, {channelId,expectedGeneration,mensagem:{tipo:TEXTO,texto}|{tipo:TEMPLATE,templateId,language,parameters}}. Somente novo fluxo, não depender de ter zero mensagens. Backend resolve conta/telefone/credencial por canal, revalida readiness/epoch/grant. Sem canal[0] ou fallback. Delegar envio/aceitação a componentes compartilhados, não duplicar regra de negócio no controller. Snapshot: ST-CON-01 Preserve.
- [x] D-04 — Janela oficial exige última IN OFICIAL confiável com timestamp de evento, não data de ingestão; menos de24h no instante do envio. IN não oficial, abrir, OUT e template não abrem janela. Corrigir estadoDaJanela/responder apenas no filtro de IN OFICIAL onde necessário para coerência; manter contratos de resposta atuais e testar BFF/API pública. Sem reescrever todos callers ou autorização pública. Snapshot: regra24h preservada, restrição anterior a templates supersedida intencionalmente só pelo novo fluxo.
- [x] D-05 — GET /api/bff/conversations/:id/channels/:channelId/templates, cursor opaco validado limitado512, uma página de até50 por ação; timeout10s por chamada, máximo3 reads por envio (grant/recurso/template) e um POST de envio, sem seguir URLs arbitrárias. Conta deriva do canal. Somente APPROVED de categoria UTILITY ou MARKETING, BODY textual com variáveis textuais e HEADER TEXT/FOOTER estáticos opcionais; sem botões/mídia/OTP/Flow/carrossel. NAMED/POSITIONAL conforme definição, idioma exato; sem converter categorias/traduzir. Catálogo projeta id/nome/idioma/categoria/componentes suportados/porquê não suportado, nunca token. Revalidar pertencimento à conta, status, conteúdo e parâmetros imediatamente antes do envio. Mudança de definição entre prévia/envio exige nova confirmação. Snapshot: integrations invariants Preserve; No Prior Decision para catálogo.
- [x] D-06 — Uma intenção PostgreSQL durável por BU+usuário+Idempotency-Key, vinculada a conversa/canal/geração e fingerprint canônico da mensagem; autorização antes de lookup/replay. Mesma chave/payload devolve mesmo resultado; conflito409; processamento concorrente202 sem segundo POST. Estado PREPARED antes da rede → SENDING por CAS durável → SUCCEEDED/REJECTED/AMBIGUOUS. HTTP fora de transação. Crash/timeout em SENDING ou POST sem ID é ambíguo e nunca promove retry automático nem assume falha por timeout local. Limite: até uma invocação externa por intenção, não exactly-once de entrega nem dedupe de duas intenções diferentes. Nova tentativa explícita após ambiguidade informa risco e requer decisão do operador. Estado/readback pelo mesmo endpoint com mesma chave, sem novo POST externo. Snapshot: aceitação externa ST-CON-01 preservada, No Prior Decision para intenção.
- [x] D-07 — Registrar saída pela MessageAcceptanceService existente (identidade/externalId), enriquecer autoria se echo-first, uma Message/realtime vencedor/unread inalterado. Template persiste snapshot textual renderizado e metadados mínimos nome/idioma/templateId na Message ou intenção vinculada, tipo TEXTO sem quebrar timeline. Sucesso muda status/autoatribuição apenas conforme responder atual, sem roubar responsável. Falha de provider/ambiguidade explícita não marca entregue nem apaga draft. Validação final de geração é fence local, sem promessa de revogar HTTP já iniciado. Snapshot: inbox aceitação Preserve.
- [x] D-08 — Formulário vincula BU/contato/canal/revisão e conserva a mesma chave ao repetir o mesmo envio incerto; doubleclick desabilitado e proteção server-side obrigatória. Resposta velha não abre outra conversa nem limpa draft atual; mudança de conteúdo gera nova intenção só por ação explícita, nenhuma mensagem em background. Sem template elegível, texto oficial bloqueado fora da janela e estado orienta preparar template no Gerenciador Meta. Prova física template não pode ser substituída por Sandbox/fixture. Snapshot: ST-ATT-01 freshness Preserve; gestão de modelos permanece fora do escopo.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| project_constitution#system-invariants | BU/Contato unifica, domínio backend, templates só em TODO próprio | Preserve | D-01..08 e contrato próprio ST-CON-04 |
| inbox-and-conversations#contrato-aprovado-da-timeline-da-inbox | paginação e estado fresco | Preserve | D-02/D-08; sem alterar cursor/timeline |
| inbox-and-conversations#aceitação-de-mensagens-e-automação--st-con-01 | aceitação única e nenhum Nova conversa autorizado no recorte anterior | Supersede (Intentional) | apenas autorização de Nova conversa no NOVO TODO; dedupe/tenant/echo preservados |
| integrations-and-channels#cadastro-de-números-st-con-01 | credenciais e identidade scoped | Preserve | D-03/D-05/D-07 |
| integrations-and-channels#invariants | provider adapter e erro seguro | Preserve | catálogo/envio só no MetaClient |

## Decision Baseline (Frozen Before Implementation)

- [ ] D-01 — Abrir/reusar por POST /api/bff/business-units/:buId/conversations/open com {telefone}. Telefone exige DDI explícito (+ opcional), remove apenas espaços/parênteses/hífen/ponto, rejeita letras/ramal/grupo, 8–15 dígitos e primeiro não zero. Não inferir país nem variantes de nono dígito. Autorizar BU/ATENDENTE antes de validação detalhada; 401/403/404 scoped. Retorno {conversaId,criada,contact}; nenhuma chamada externa. Snapshot: Constituição BU/Contato e inbox invariants preservados.
- [ ] D-02 — Upsert pelo índice buId/contact existente; nova PESSOA QUEUED/unread0/lastMessageAt null; abrir não assume nem reabre existente. Ordenação usa COALESCE(lastMessageAt,createdAt) desc + id desc para listar vazias deterministicamente; não escrever data falsa. Abrir persiste mesmo se operador fechar depois: é atendimento vazio visível; antes de Abrir, cancelar não persiste. Nenhuma alteração em paginação de mensagens. Snapshot: ST-ATT-01 preservado; No Prior Decision para abertura manual.
- [ ] D-03 — GET /api/bff/conversations/:id/start-options informa canais da BU com capacidade/explicação, geração e janela. Primeiro envio usa POST /api/bff/conversations/:id/initial-messages, Idempotency-Key UUID, {channelId,expectedGeneration,mensagem:{tipo:TEXTO,texto}|{tipo:TEMPLATE,templateId,language,parameters}}. Somente novo fluxo, não depender de ter zero mensagens. Backend resolve conta/telefone/credencial por canal, revalida readiness/epoch/grant. Sem canal[0] ou fallback. Delegar envio/aceitação a componentes compartilhados, não duplicar regra de negócio no controller. Snapshot: ST-CON-01 Preserve.
- [ ] D-04 — Janela oficial exige última IN OFICIAL confiável com timestamp de evento, não data de ingestão; menos de24h no instante do envio. IN não oficial, abrir, OUT e template não abrem janela. Corrigir estadoDaJanela/responder apenas no filtro de IN OFICIAL onde necessário para coerência; manter contratos de resposta atuais e testar BFF/API pública. Sem reescrever todos callers ou autorização pública. Snapshot: regra24h preservada, restrição anterior a templates supersedida intencionalmente só pelo novo fluxo.
- [ ] D-05 — GET /api/bff/conversations/:id/channels/:channelId/templates, cursor opaco validado limitado512, uma página de até50 por ação; timeout10s por chamada, máximo3 reads por envio (grant/recurso/template) e um POST de envio, sem seguir URLs arbitrárias. Conta deriva do canal. Somente APPROVED de categoria UTILITY ou MARKETING, BODY textual com variáveis textuais e HEADER TEXT/FOOTER estáticos opcionais; sem botões/mídia/OTP/Flow/carrossel. NAMED/POSITIONAL conforme definição, idioma exato; sem converter categorias/traduzir. Catálogo projeta id/nome/idioma/categoria/componentes suportados/porquê não suportado, nunca token. Revalidar pertencimento à conta, status, conteúdo e parâmetros imediatamente antes do envio. Mudança de definição entre prévia/envio exige nova confirmação. Snapshot: integrations invariants Preserve; No Prior Decision para catálogo.
- [ ] D-06 — Uma intenção PostgreSQL durável por BU+usuário+Idempotency-Key, vinculada a conversa/canal/geração e fingerprint canônico da mensagem; autorização antes de lookup/replay. Mesma chave/payload devolve mesmo resultado; conflito409; processamento concorrente202 sem segundo POST. Estado PREPARED antes da rede → SENDING por CAS durável → SUCCEEDED/REJECTED/AMBIGUOUS. HTTP fora de transação. Crash/timeout em SENDING ou POST sem ID é ambíguo e nunca promove retry automático nem assume falha por timeout local. Limite: até uma invocação externa por intenção, não exactly-once de entrega nem dedupe de duas intenções diferentes. Nova tentativa explícita após ambiguidade informa risco e requer decisão do operador. Estado/readback pelo mesmo endpoint com mesma chave, sem novo POST externo. Snapshot: aceitação externa ST-CON-01 preservada, No Prior Decision para intenção.
- [ ] D-07 — Registrar saída pela MessageAcceptanceService existente (identidade/externalId), enriquecer autoria se echo-first, uma Message/realtime vencedor/unread inalterado. Template persiste snapshot textual renderizado e metadados mínimos nome/idioma/templateId na Message ou intenção vinculada, tipo TEXTO sem quebrar timeline. Sucesso muda status/autoatribuição apenas conforme responder atual, sem roubar responsável. Falha de provider/ambiguidade explícita não marca entregue nem apaga draft. Validação final de geração é fence local, sem promessa de revogar HTTP já iniciado. Snapshot: inbox aceitação Preserve.
- [ ] D-08 — Formulário vincula BU/contato/canal/revisão e conserva a mesma chave ao repetir o mesmo envio incerto; doubleclick desabilitado e proteção server-side obrigatória. Resposta velha não abre outra conversa nem limpa draft atual; mudança de conteúdo gera nova intenção só por ação explícita, nenhuma mensagem em background. Sem template elegível, texto oficial bloqueado fora da janela e estado orienta preparar template no Gerenciador Meta. Prova física template não pode ser substituída por Sandbox/fixture. Snapshot: ST-ATT-01 freshness Preserve; gestão de modelos permanece fora do escopo.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability (`required|not_needed`):** required
- **Why this applies:** novo contrato compartilhado de primeiro envio e intenção persistente; supersede limitado da exclusão manual/template do recorte anterior.
- **Deviation / debt being retired:** dependência de IN para abrir na inbox; repetição de HTTP não deve duplicar a primeira saída deste fluxo. Não alegar correção global dos senders.
- **Target steady-state after closeout:** domínio inbox único para abertura/intenção, MetaClient para provider e MessageAcceptanceService para registro; sem segundo owner de mensagem.
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** todo caller do novo fluxo usa intenção; sem rota técnica de token/Sandbox, fallback ou camada paralela.

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** not_run
- **Decision review evidence / resolution:** pending-freeze
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** not_run
- **Adherence review evidence / resolution:** planejado após implementação
- **No-go handling:** resolver divergência antes do gate correspondente; sem auto-waiver.

## Gate: Review Baseline Freeze

- **Gate decision:** required
- **Why this decision:** contrato multi-superfície deve entrar em revisão a partir da autoridade publicada.
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** pending-freeze
- **Baseline push reference:** origin/main
- **Gate status:** not_run
- **Findings summary:** prepared-pre-freeze; nenhuma revisão ou guarda de planejamento reivindicada.
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Gate: Review Scope Drift

- **Gate decision:** required
- **Why this decision:** conferir que aprovação usará pacote revisado.
- **Trigger stage:** after the planning-side review/guard cycle converges and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Material sections compared:** Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **No-go handling rule:** reconvergir pacote/review e renovar freeze, sem implementação.
- **Gate status:** not_run
- **Findings summary:** pending-freeze
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Questions To Close

Nenhuma pergunta material de produto aberta. Operador ainda preparará template elegível na Messaging account selecionada antes da prova física; este TODO não autoriza criar/submeter nem enviar agora.

## Pattern References (Optional; Enforced When Cited)

n/a; decisões canônicas citadas diretamente, sem IDs de catálogo presumidos.

## Assumptions Preview (Required Before Plan Review)

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Schema já impõe uma conversa por BU/contato. | api-app/prisma/schema.prisma:379 | rever upsert e migrations antes da aprovação | High | Keep as Assumption |
| A-02 | BFF atual só lista/timeline/responde, não abre contato manual. | api-app/src/surfaces/bff/conversations.controller.ts | reutilizar owner existente | High | Keep as Assumption |
| A-03 | MetaClient não possui catálogo/envio template. | api-app/src/integrations/meta/meta.client.ts | integrar componente existente, sem duplicar | High | Keep as Assumption |
| A-04 | Envio atual já converge sender/echo pelo serviço de aceitação. | api-app/src/domain/inbox/conversations.service.ts; api-app/src/domain/inbox/message-acceptance.service.ts | corrigir desenho antes de código | High | Keep as Assumption |
| A-05 | Inbox usa gerações/drafts e browser serve build com API/PG exclusivos. | web-app/src/telas/Inbox.tsx; web-app/playwright.config.ts | ajustar plano de fixture/freshness | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces
Paths positivos do Diff Expectation Contract; nenhum runtime/segredo lido neste planejamento.

### Ordered Steps
1. Após APROVADO: reload binding, routing/authority go, executor único na principal; conferir branches, baseline e limpeza por inventário positivo público.
2. Test-first: normalização, auth/CSRF, abertura/reuso, janela só oficial, schema/intenção e provider fixture; RED válido antes do código correspondente.
3. Resolver de conversa e migration da intenção; estado/resultado crash-safe; compatibilidade de sender/echo existente e API pública sem nova semântica de rota.
4. Catálogo Meta scoped, paginação limitada, parser de componentes/params e sender textual; manter erro fixo seguro e snapshot local.
5. Formulário NovaConversa e estado por contexto; integrar Inbox sem refazer timeline; mensagem de vazio/erro/bloqueio explícita.
6. Remover travessia do diretório privado do runner usando somente inventário público positivo; manter masks, Docker ownership e testes source-owned.
7. Runner all completo, DB/corridas, browser mutante e served freshness; nenhuma fixture prova Meta real. Readiness antes de publicar para operador.
8. Prova física privada; template ausente bloqueia apenas respectiva evidência, sem falsa conclusão. Aderência/segurança/pcv/TQA/final, consolidação dos módulos e guardas de entrega/fechamento.

### Test Strategy
- **Strategy:** test-first
- **Why:** contrato novo com side effect externo e disputa DB; falha antes de implementação prova assertions relevantes.
- **Fail-first target(s) (when required):** start-conversation.e2e-spec.ts e start-conversation.spec.ts, barreiras duas requisições/IN webhook/echo, stale BU, template sem elegibilidade.

### Pre-APROVADO RED Evidence Capture (Optional for bugfix/regression)
- **Decision (`required|recommended|not_needed|waived`):** not_needed
- **Why now:** feature nova; diagnóstico apoiado em fonte, nenhum bug sintomático ambíguo necessita testes antes de autorização.
- **Target symptom:** n/a
- **Allowed surfaces:** none
- **Forbidden surfaces reaffirmed:** production code|runtime/config/deploy|canonical project docs outside TODO authoring
- **Planned command / target:** n/a
- **Status (`not_run|running|red_reproduced|red_not_reproduced|blocked|waived`):** not_run
- **Findings summary:** não executar produto antes de APROVADO.

### Flow Evidence Planning Matrix (Required Before `APROVADO`)
| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01/02 abrir/reusar | criação e readback | web-only | Playwright mutation | yes | yes | e2e/start-conversation.spec.ts; POST e refresh contra BFF real | n/a |
| DOD-03/04/05 template/canal/idempotência | validação/envio/DTO persistidos | web-only | Playwright mutation + PostgreSQL concurrency | yes | yes | mesmo spec e test/start-conversation.e2e-spec.ts, provider fixture controlado | n/a |
| DOD-06 stale | draft/async | web-only | Playwright mutation | yes | yes | mesma spec com rede atrasada, sem mock BFF | n/a |
| DOD-08 prova física | entrega do provider | web-only | operador no runtime local | yes | yes | receipt redigido e evidência servidor scoped | não substitui browser determinístico |
| DOD-07/09 e VAL-01..05 | gates transversais | web-only | browser acima + auditorias específicas | yes | yes | evidências por critério, não contagem agregada | n/a |

### Local CI-Equivalent Suite Matrix (Required Before `APROVADO` and Before Delivery Claim)
As duas colunas de Status projetam o MESMO fato para leitores determinísticos distintos; Evidence mantém todas as ressalvas. Não são duas execuções nem resultados diferentes.

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status (completion projection) | Evidence Artifact / Command | Status (authority projection) | Notes | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| api / API + PostgreSQL E2E | domínio/adapter/schema | bash scripts/test-channels-local.sh all | Local-Implemented | planned | Nenhum teste executado nesta preparação; runner completo, não subset | planned | espelha npm ci/lint/build/test e amplia E2E | abrir, janela, template, intenção concorrente, negativos scoped, callers existentes | Node22/PG16 descartável, migration deploy/status, máscaras fictícias e provider fixture |
| web / Web + browser | fluxo de usuário | bash scripts/test-channels-local.sh all | Local-Implemented | planned | spec start-conversation e suites timeline/number-onboarding/telas; não simula BFF | planned | mesmo run all, sem repetição desnecessária | abrir/reusar/send, template/vazio/erro, trocas e duplo clique | bundle recém-buildado; 4173/3100/3101; mesmo DB e endpoint CI-equivalent; fonte+HTTP fresco comprovados |
| root / compose/runner | boundary privado/ownership | bash scripts/test-channels-local.sh all | Local-Implemented | planned | sem .local-files nem dotenv real; nenhuma execução atual | planned | validar config e proteções antes de container | bootstrap exclusivo sem tocar runtime de teste humano | namespace validation exclusivo; sem recursos preexistentes; inventário público positivo |

### Runtime / Rollout Notes
Migration aditiva versionada; deploy/status primeiro no PG descartável. Antes de eventual runtime privado, readiness e backup scoped próprios, sem reset. Limite: crash após HTTP pode permanecer ambíguo; não background retry, worker, outbox ou claim exactly-once. Fonte e API/DB/porta publicadas devem coincidir com CI-equivalent; não usar web-app/dist antigo. Nenhum restart, túnel ou envio real autorizado nesta preparação.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

### Review Sections
- [ ] Architecture
- [ ] Code Quality
- [ ] Tests
- [ ] Performance
- [ ] Security
- [ ] Elegance
- [ ] Structural Soundness

### Issue Cards
- **Issue ID:** PLAN-01
  - **Severity:** medium
  - **Evidence:** conversations.service.ts usa aceitação por externalId depois do HTTP; isso não impede duas invocações.
  - **Why it matters now:** primeiro envio repetido pode duplicar comunicação e cobrança.
  - **Option A (Recommended):** intenção durável dedicada ao novo fluxo, CAS e outcome ambíguo sem resend.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** medium; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** apenas botão desabilitado/Map em memória.
    - **Effort:** low; **Risk:** high; **Blast radius:** module; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** não entregar Nova conversa; **Effort:** low; **Risk:** medium; **Blast radius:** local; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** A, sem prometer exatamente uma entrega externa.
- **Issue ID:** PLAN-02
  - **Severity:** medium
  - **Evidence:** MetaClient sem templates; usuário sem template aprovado.
  - **Why it matters now:** primeiro OUT oficial fora de janela exige template elegível.
  - **Option A (Recommended):** templates textuais existentes com variáveis e validação server-side.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** medium; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** editor/gestão completa de modelos agora.
    - **Effort:** high; **Risk:** high; **Blast radius:** cross-module; **Maintenance burden:** high; **Performance impact:** unknown; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** limitar abertura oficial a janela e adiar primeiro contato.
    - **Effort:** low; **Risk:** low; **Blast radius:** local; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** A, recurso externo pendente não é evidência de produto.

### Failure Modes & Edge Cases
- [ ] Chave/payload divergente409; duplo envio concorrente202/replay, não segundo POST.
- [ ] Timeout/crash SENDING permanece ambíguo, sem reenviar; erro de provider não marca entregue.
- [ ] Template alterado/pausado, outra conta/idioma, página vazia com continuação: bloquear ou continuar explicitamente, nunca inferir catálogo completo.
- [ ] IN não oficial/histórico não abre janela oficial; instante24h revalidado no servidor.
- [ ] Auth revogada/canal renovado em voo: fence local, nunca anexar resposta a outro recurso.
- [ ] Conversa vazia após Abrir é intencional e listada sem lastMessageAt falso.

### Residual Unknowns / Risks
- [ ] Prova física oficial proativa depende de template elegível; operador não o possui agora.
- [ ] Meta pode recusar por thread ownership/billing/política mesmo com template aprovado: mostrar erro seguro, não tomar controle automaticamente.
- [ ] Até uma invocação por intenção não elimina duplicação entre chaves distintas ou a ambiguidade de crash externo.
- [ ] Revisões independentes ainda pending-freeze; esta lista é preparação de pacote, não aprovação de arquitetura.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

- **Needed:** no
- **Why ambiguity remains:** n/a; arquitetura obrigatória será examinada na gate architecture_opinion, sem opinião adicional duplicada.
- **Opinion count:** 0
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required na gate arquitetural
- **Required lenses:** correctness,performance,elegance,structural-soundness,operational-fit

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **Latest TEACH evidence / artifact:** pending-freeze

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
| high_severity_plan_review_issue | no | escopo ST-CON-04; derivar após freeze |
| explicit_three_lane_request | no | escopo ST-CON-04; derivar após freeze |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

- **Critique decision:** required
- **Why this decision:** big/cross-stack/escrita externa scoped.
- **Impact signals in scope:** public contract/schema/api; auth; realtime; intentional module supersede
- **Package mode:** bounded-file-set
- **Package minimum contents:** TODO congelado, fontes públicas limitadas, decisões/matriz/issue cards/riscos, parecer arquitetural e resolução.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; novo agente, não executor, aguardar terminal sem prazo artificial
- **Critique lenses:** correctness,performance,elegance,structural-soundness,risk
- **Critique status:** not_run
- **Findings summary:** pending-freeze
- **Resolution ledger:** nenhuma revisão executada
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Gate: Assumption Code Coherence

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Approval

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

Ingestão de planejamento; reload binding obrigatório após APROVADO antes de produto.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | autoridade e roteamento | executor único | código no planejamento | handoff após aprovação |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | aprovação | freeze/reviews/APROVADO | concordância genérica como execução | authority pré/post |
| delphi-ai/workflows/docker/effort-selection-method.md | routing | agent_role_routing_guard.py | fingir modelo primário | guard antes da lane |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | BFF/domínio | adapters finos | regra no controller | contratos E2E |
| delphi-ai/workflows/react/change-ui-boundary-method.md | formulário/estado | freshness/draft | resposta atrasada | Playwright mutation |
| delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | schema | migration versionada | reset operacional | deploy/status descartável |
| delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | intenção/locks | unique/CAS | HTTP em tx | barriers reais |
| foundation_documentation/project_constitution.md | multi-tenant | BU/Contato | credencial global | testes scoped |
| foundation_documentation/policies/scope_subscope_governance.md | rotas existentes | BFF sessão | endpoint fora do owner | contrato explícito |
| delphi-ai/workflows/docker/performance-concurrency-validation-method.md | pcv-1 | quatro lanes | prose sem artefato | JSON/hash antes entrega |

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Subagent / delegation authorization:** main_instructions.md e todo-approval-gates-method exigem executor e reviewers independentes; produto só após APROVADO.
- **Execution topology:** primary-checkout-single-writer
- **Worktree / auxiliary-checkout authorization:** not-authorized
- **Worktree authorization evidence:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** pending
- **Waiver / exception reference:** n/a

Formal-review architecture_opinion e critique: gpt-6.1-sol/max, fresh fork_turns none, guard distinto. Modelo da sessão primária não reconfigurado nem declarado como outro.

## Decision Adherence Validation (Mandatory Before Delivery)

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Pipeline/Copilot P1/P2 Preflight

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Rule-Spirit Anti-Pattern Hunt

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** revisão pré-implementação, nenhuma aprovação específica ainda.
- **Post-commit/push status:** pending
- **Next path/status action:** completar revisão/guardas e pedir APROVADO do contrato, não entrega.

## Security Risk Assessment (Mandatory Before Delivery)

- **Risk level:** high
- **Why this risk level:** endpoint autenticado multi-tenant com destinatário externo, credencial e pagamento potencial.
- **Attack surface in scope:** BFF auth/CSRF, BU/canal/template, cursor, idempotência/replay, erro/segredo.
- **Attack simulation decision:** required
- **Review evidence:** planned após implementação; negativos scoped/tokens/cursor e revisão independente.
- **Residual security risk:** falha externa/thread ownership não contornada; coorte privada segue limites da entrega anterior.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** escrita externa e concorrência com webhook e UI.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | pending | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | pending | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-E3 | pending | external ambiguity explicit | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E1 | pending | none | none |

### Lane Detail Packet Template
#### EPS
- **Trigger rationale:** listagem de conversas vazias/ordem e lookup scoped/intenção; EXPLAIN ANALYZE com amostra cardinalidade, limite de página e budget externo. Sem N+1/catalog fan-out.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256 antes da entrega, não existe execução ainda.
#### FRC
- **Trigger rationale:** duas submissões e atraso em troca BU/canal/draft; Playwright real, rastrear requests e estado no backend.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### BCI
- **Trigger rationale:** barreiras PG e contador HTTP externo, crash antes/depois POST, replay e echo; provar invariantes D-06/07.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### RLS
- **Trigger rationale:** pequeno ensaio de concorrência/load bounded do novo fluxo/listagem no PG descartável; não claim SLO ou produção.
- **Recorded at (UTC):** 2026-10-19T20:34:09Z
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; resolver recomendação com evidência ou waiver válido até o deadline, sem deixar pendente na entrega.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

- **Audit outcome:** high
- **Why this outcome:** não implementado; toda evidência de produto pendente, sem claim de entrega.
- **Inline code TODO debt:** none
- **Evidence / audit artifact:** planned após implementação
- **Accepted residual debt:** none; dependência externa não é waiver.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Audit decision:** required
- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
- **Required evidence matrix (when architectural):** unit|integration|web real-backend
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
- **Canonical method:** wf-docker-independent-test-quality-audit-method
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** planned após implementação
- **Audit status:** not_run
- **Findings summary:** none; nenhuma auditoria de entrega executada
- **Evidence / reference:** planned após implementação
- **Waiver authority / reference (required if waived):** n/a

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Final review decision:** required
- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
- **Required evidence matrix (when architectural):** unit|integration|web real-backend
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
- **Canonical method:** wf-docker-independent-test-quality-audit-method
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** planned após implementação
- **Final review status:** not_run
- **Findings summary:** none; nenhuma auditoria de entrega executada
- **Evidence / reference:** planned após implementação
- **Waiver authority / reference (required if waived):** n/a

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** not_needed
- **Why this decision:** rota aditiva sem dual-write/compatibilidade temporária ou remoção de legado; owner único preservado. Reclassificar se implementação introduzir bridge.
- **Cutover signals in scope:** none
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** n/a
- **Cutover audit status:** not_run
- **Findings summary:** none
- **Evidence / reference:** D-03/06/07 e arquitetura requerida
- **Waiver authority / reference (required if waived):** n/a

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Module Consolidation Gate (Required Before `Completed`)

Planejado para o gate correspondente após APROVADO e implementação; nenhuma evidência de entrega reivindicada.

## Commands (Run Locally)

Preparação: guardas de planejamento descritas acima. Execução futura: bash scripts/test-channels-local.sh all após correção de boundary público e autorização. Nenhum teste de produto executado agora.

## Files Expected (Compatibility Note)

Diff Expectation Contract é o inventário autoritativo.

## COMENTÁRIO:

Nenhum comentário ou questão material pendente.

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** premissas de implementação dependem de fontes atuais.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01..05
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **Gate status:** not_run
- **Findings summary:** pending-freeze
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Approval

- **Approved by:** pending
- **Approval reference:** pending
- **Approval scope:** proposta SCOPE-01..06/D-01..08 e critérios acima; ainda sem autorização de implementação.
- **Execution not authorized by approval:** todo Out of Scope, source push/deploy, ações Meta, worktrees/gitlinks e payload privado.
- **Renewed approval required when:** mudança material de escopo/decisão/risco/validação ou path não admitido.


## External Reference Evidence — consulted 2026-10-19

Meta primary: [Template fundamentals](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview/) consulted via official Markdown response; templates are Messaging account assets, require APPROVED status, support NAMED/POSITIONAL variables, exact language and approved component definition. Proposed support is deliberately narrower than full provider catalog. This is external reference evidence, not proof of a live account or delivery.

Source inspection: Prisma Conversation unique(buId,contact); BFF controller lacks manual-open route; MetaClient interface has enviarTexto but no template catalog/send; responder resolves channel from prior traffic and checks window; acceptance service already reconciles sender/echo. Existing public API conversation upsert stays its own authenticated adapter and shares the DB uniqueness.
