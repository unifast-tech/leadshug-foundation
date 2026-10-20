# Tactical TODO — ST-CON-04

## Title

LeadsHug — ST-CON-04: Nova conversa por contato e primeiro envio seguro

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** NotStarted
- **Created:** 2026-10-19
- **Template provenance:** copied from `delphi-ai/templates/todo_template.md` before refinement.

## Context

**Atualização material2026-10-20:** direção humana exige Channel abstrato/concretos e resolução scoped; este consumer depende do contrato/cutover ST-CON-06 e precisa novo refinamento/reviews/guardas antes de APROVADO. Evidências de planejamento2026-10-19 são históricas para a versão anterior.

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
- **Next exact step:** reconvergir este contrato com Channel abstrato solicitado em2026-10-20, após enquadramento/contrato ST-CON-06; revisões e preflight anteriores são históricos, sem aprovação de execução sobre a nova direção.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** review
- **Why this state now:** orientação humana de2026-10-20 estabelece Channel abstrato/concretos; contrato de consumo precisa reconvergir antes de nova revisão/solicitação de APROVADO.
- **Exit condition:** aprovação explícita do pacote revisado + ingestão binding e authority go autorizam handoff operacional.

## Scope

- [ ] SCOPE-01 — Formulário Nova conversa em Atendimento, com BU explícita, telefone internacional normalizado e confirmação do destinatário; ATENDENTE ou superior, sessão e anti-CSRF.
- [ ] SCOPE-02 — Resolver/criar uma conversa PESSOA por BU/contato por upsert atômico; resolução preserva histórico, responsável, estado e não lidas; leitura humana posterior segue marcação de lida vigente; abertura isolada não envia mensagem.
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
| api | src/surfaces/webhooks/meta.controller.ts | M | timestamp somente em Meta assinado/verificado |
| api | src/integrations/meta/*template*.ts | A | parser/projector e testes textuais subordinados |
| api | test/atendimento.e2e-spec.ts | M | janela BFF e compositor normal sem bypass |
| api | test/api-publica.e2e-spec.ts | M | expectativa de janela e interface provider preservadas |
| api | test/webhooks.e2e-spec.ts | M | observação temporal Meta autenticada |
| api | test/number-onboarding-*.e2e-spec.ts | M | fixtures/contratos diretamente afetados por timestamp/provider |
| api | test/helpers.ts | M | fixture de provider/evento confiável |
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
| foundation | backlog/README.md | M | próximo gate do candidato, sem autorizar implementação |
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
- [ ] DOD-02 — Resolver/abrir preserva histórico, unread, status e responsável; leitura posterior segue ST-ATT-01; conversa nova QUEUED com unread zero é visível após refresh sem falsificar lastMessageAt.
- [ ] DOD-03 — Canal explícito e autorização server-side bloqueiam tenant/BU/recurso incorretos, canal não pronto e texto oficial fora da janela; somente horário qualificado de IN Meta da identidade atual abre janela, preservando createdAt/timeline.
- [ ] DOD-04 — Catálogo paginado/envio validam template APPROVED textual da conta corrente, fingerprint confirmado, idioma, formato e parâmetros; messaging_account_id fixa a conta do canal, budget4GET+1POST é contado e catálogo vazio/indisponível/incompatível não ativa fallback.
- [ ] DOD-05 — Intenção durável impede duas chamadas externas por chave e bypass BFF após refresh; abertura/webhook mantém uma conversa; aceitação elegível por ID não duplica Message/autoria, dono e close concorrentes são preservados; PREPARED rejeitado/vencido, local recovery/quarentena e ack/release monotônico têm prova sem resend e sem reativar slot antigo.
- [ ] DOD-06 — Troca de BU, conversa, canal, revisão de formulário e respostas tardias preservam o rascunho correto e não abrem destino alheio; erros não indicam sucesso nem apagam conteúdo.
- [ ] DOD-07 — Harness de arquitetura executável, migration deploy/status e suites CI-equivalent completas passam; Playwright mutation usa API/DB reais e bundle servido comprovadamente fresco.
- [ ] DOD-08 — Prova física de primeiro envio não oficial e oficial por template elegível, seguida de resposta recebida, registrada separadamente; ausência de template mantém critério bloqueado sem simular prova externa.
- [ ] DOD-09 — Módulos consolidados, decisões verificadas, auditorias derivadas e guardas de entrega satisfeitos, sem P1/P2 aberto nem promessa de produção.

## Validation Steps

- [ ] VAL-01 — Executar bash scripts/test-channels-local.sh all no target descartável com dotenv fictício, migrations deploy/status, lint/build/unit/E2E e Web/browser completos; registrar fonte/served fingerprint.
- [ ] VAL-02 — Executar testes PostgreSQL com barreiras para BU/contato, intenção/echo/webhook, claim/close, PREPARED expirado versus validator, perda de chave/reconcile local, geração aposentada após ID conhecido e resposta tardia após ack/sucessora; nenhuma rede dentro de transação.
- [ ] VAL-03 — Executar web-app/e2e/start-conversation.spec.ts via runner canônico, incluindo abrir/reusar, primeiro OUT, template/empty/error, negativas e respostas atrasadas contra BFF real.
- [ ] VAL-04 — Após readiness confirmada, operador executa prova real privada dos dois canais, incluindo template aprovado da conta correta e retorno; nenhuma mensagem real automática nesta preparação.
- [ ] VAL-05 — Executar arquitetura/aderência, segurança, pcv-1, TQA, final review, dívida, diff público e authority/completion/closeout antes de qualquer claim de entrega.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | DOD-01 — Nova conversa valida telefone internacional, mostra destinatário e BU, abre/reusa exatamente uma conversa sem enviar nem criar CRM; cancelar antes de Abrir não persiste. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-02 | Definition of Done | DOD-02 — Resolver/abrir preserva histórico, unread, status e responsável; leitura posterior segue ST-ATT-01; conversa nova QUEUED com unread zero é visível após refresh sem falsificar lastMessageAt. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-03 | Definition of Done | DOD-03 — Canal explícito e autorização server-side bloqueiam tenant/BU/recurso incorretos, canal não pronto e texto oficial fora da janela; somente horário qualificado de IN Meta da identidade atual abre janela, preservando createdAt/timeline. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-04 | Definition of Done | DOD-04 — Catálogo paginado/envio validam template APPROVED textual da conta corrente, fingerprint confirmado, idioma, formato e parâmetros; messaging_account_id fixa a conta do canal, budget4GET+1POST é contado e catálogo vazio/indisponível/incompatível não ativa fallback. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-05 | Definition of Done | DOD-05 — Intenção durável impede duas chamadas externas por chave e bypass BFF após refresh; abertura/webhook mantém uma conversa; aceitação elegível por ID não duplica Message/autoria, dono e close concorrentes são preservados; PREPARED rejeitado/vencido, local recovery/quarentena e ack/release monotônico têm prova sem resend e sem reativar slot antigo. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-06 | Definition of Done | DOD-06 — Troca de BU, conversa, canal, revisão de formulário e respostas tardias preservam o rascunho correto e não abrem destino alheio; erros não indicam sucesso nem apagam conteúdo. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-07 | Definition of Done | DOD-07 — Harness de arquitetura executável, migration deploy/status e suites CI-equivalent completas passam; Playwright mutation usa API/DB reais e bundle servido comprovadamente fresco. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-08 | Definition of Done | DOD-08 — Prova física de primeiro envio não oficial e oficial por template elegível, seguida de resposta recebida, registrada separadamente; ausência de template mantém critério bloqueado sem simular prova externa. | test/runtime/review | Prova física assistida e receipt redigido; fixture não substitui. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| DOD-09 | Definition of Done | DOD-09 — Módulos consolidados, decisões verificadas, auditorias derivadas e guardas de entrega satisfeitos, sem P1/P2 aberto nem promessa de produção. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| VAL-01 | Validation Steps | VAL-01 — Executar bash scripts/test-channels-local.sh all no target descartável com dotenv fictício, migrations deploy/status, lint/build/unit/E2E e Web/browser completos; registrar fonte/served fingerprint. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
| VAL-02 | Validation Steps | VAL-02 — Executar testes PostgreSQL com barreiras para BU/contato, intenção/echo/webhook, claim/close, PREPARED expirado versus validator, perda de chave/reconcile local, geração aposentada após ID conhecido e resposta tardia após ack/sucessora; nenhuma rede dentro de transação. | test/runtime/review | web-app/e2e/start-conversation.spec.ts; bash scripts/test-channels-local.sh all; test/start-conversation.e2e-spec.ts; gates específicos conforme VAL-05. | local descartável e recursos privados apenas quando explícito | planned | Sem execução de produto neste planejamento. |
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

- [x] D-01 — Abrir/reusar por POST /api/bff/business-units/:buId/conversations/open com {telefone}. UI exige DDI explícito (sem país inferido); backend aceita + opcional, remove apenas espaços/parênteses/hífen/ponto, rejeita letras/ramal/grupo, 8–15 dígitos e primeiro não zero. Autorizar BU/ATENDENTE antes de validação detalhada; 401/403/404 scoped. Retorno {conversaId,criada,contact}; nenhuma chamada externa. Criação exige pelo menos um canal local atual apto; ausência retorna CANAL_INDISPONIVEL sem nova conversa. Reuso de conversa existente não concede envio. Snapshot: Constituição BU/Contato e inbox invariants preservados.
- [x] D-02 — Upsert pelo índice buId/contact existente; nova PESSOA QUEUED/unread0/lastMessageAt null; resolver/abrir não assume nem reabre existente e preserva unread. Leitura humana posterior da timeline segue marcação de lida ST-ATT-01. Ordenação da lista usa COALESCE(lastMessageAt,createdAt) desc + id desc, filtro/paginação no PostgreSQL, sem sort/merge em memória nem data falsa. Abrir persiste mesmo se operador fechar depois: atendimento vazio visível; cancelar antes de Abrir não persiste. Medir query/index via EPS; migration pode incluir índice de expressão se justificado. Snapshot: ST-ATT-01 preservado; No Prior Decision para abertura manual.
- [x] D-03 — GET /api/bff/conversations/:id/start-options informa canais da BU, capacidade/explicação, geração/janela e projeção segura limitada a uma tentativa com slot ativo mais até10recentes, ordenadas no DB por createdAt/id e indicador de truncamento; nunca varrer/devolver todos os recibos. Consulta por attemptId é lookup scoped separado, sem histórico completo implícito. POST /api/bff/conversations/:id/initial-messages exige Idempotency-Key UUID e {channelId,expectedGeneration,mensagem:{tipo:TEXTO,texto}|{tipo:TEMPLATE,templateId,language,catalogAfter?,expectedDefinitionFingerprint,parameters}}. parameters é mapa string→string: chaves nominais exatas em NAMED, índices 1..N em POSITIONAL; sem campos Graph arbitrários. Canal/conta/telefone/credencial derivam da BU vinculada; revalidar readiness/epoch/grant; preservar gate atual de ChannelCredentialResolver(send): CONECTADO, receiptVerifiedAt, própria identidade/epoch e SUBSCRIBED/CONNECTED. UI explica recebimento ainda pendente, sem enfraquecer ST-CON-01 nem usar purpose verify/registration para enviar. O novo fluxo não usa canal[0] nem fallback. Pode operar em conversa reutilizada não vazia. Com nenhuma mensagem de transporte autoritativo, UI reconstrói primeiro envio após refresh e POST BFF /messages é recusado no domínio com INITIAL_SEND_REQUIRED antes de rede. Nova intenção e BFF /messages recusam enquanto outra intenção possui o slot ativo da conversa, incluindo PREPARED/SENDING/EXTERNAL_ACCEPTED/AMBIGUOUS/EXTERNAL_ACCEPTED_LOCAL_BLOCKED não reconhecida; o guarda é server-side no domínio e na UI, não depende de estado transitório da aba. Public API/Typebot não ganham idempotência global nem nova rota. Snapshot: ST-CON-01 Preserve; No Prior Decision para jornada inicial.
- [x] D-04 — Adicionar Message.officialInboundAt nullable e proveniência confiável equivalente: somente msg.timestamp de IN OFICIAL no webhook Meta com assinatura válida e identidade/recurso verificados pode preenchê-lo via MensagemRecebida e MessageAcceptanceService. Aceitar como horário apenas segundos Unix inteiros positivos, data válida não futura relativamente ao recebimento; timestamp ausente/malformado/futuro permanece null, sem descartar a mensagem por isso. Legacy/import/OUT/não oficial não preenchem; sem backfill de createdAt/raw. Janela usa máximo horário qualificado IN/OFICIAL da identidade atual do canal escolhido e menos de24h no instante do POST. Abrir, OUT e template não abrem janela. Preservar Message.createdAt, ordem/cursor da timeline. Aplicar a política de horário ao responder compartilhado e testar BFF/API pública; registros antigos sem observação qualificada exigem nova IN oficial ou template, não janela por inferência. Sem suporte de chamada/importador. Snapshot: janela verdadeira preservada; supersede intencional da fonte de tempo de ingestão e da exclusão de template no novo fluxo.
- [x] D-05 — GET /api/bff/conversations/:id/channels/:channelId/templates usa conta derivada do canal e cursor after opaco limitado512, página até50 por ação, sem fan-out. Retorno por template inclui id/nome/idioma/categoria/componentes/parameter_format, suporte/porquê, catalogAfter da página e definitionFingerprint SHA256 canônico de canal/conta/geração/templateId/nome/idioma/categoria/status/componentes/formato. Suporte: APPROVED UTILITY ou MARKETING; BODY textual com variáveis textuais NAMED/POSITIONAL; HEADER TEXT/FOOTER estáticos opcionais; sem botões/mídia/OTP/Flow/carrossel. Texto livre1..4096; templateId até64 dígitos, language até16, fingerprint64hex, até20 parâmetros de1..1024 caracteres, snapshot renderizado até4096; formato maior/incompatível não enviável com razão explícita. Revalidar template e pertencimento lendo somente a página da conta indicada por catalogAfter: cursor/hash cliente são assertions, nunca autorização. Se ID/idioma saiu da página ou definição/fingerprint mudou, recusar e exigir nova seleção/prévia. Antes de um envio novo: no máximo4 GETs (grant1 + até2 páginas de telefones do canal +1 página de templates; texto não faz última leitura), mais1 POST, cada request timeout10s, budget total55s/lease75s. Lista inconclusiva ou recurso além de página2 falha seguro, sem scan até achar. Both official initial-text/template HTTP incluem messaging_account_id fixado pela conta verificada do canal; nenhum accountId vem do cliente. Replay existente é servido antes de provider reads. Snapshot: integrations invariants Preserve; No Prior Decision para catálogo/envio textual scoped.
- [x] D-06 — Intenção PostgreSQL durável por BU+usuário+Idempotency-Key UUID; payload canônico original inclui conversa/canal/geração, texto OU templateId/idioma/cursor/fingerprint/parâmetros, e contexto de recurso/conta resolvido no primeiro aceite. Autorizar antes de lookup/replay. Mesma chave/request canônico retorna mesma tentativa/resultado sem reler catálogo mutável; payload diferente409. Uma intenção por conversa possui o slot ativo, protegido por índice único parcial/condição equivalente transacional; slot é fato SEPARADO do outcome, com release monotônico e irreversível para aquela tentativa. PREPARED reserva lease75s de validação: qualquer falha de validação/grant/janela/template (inclusive indisponibilidade antes de dispatch) vira REJECTED(dispatched=false), sem Message/POST e libera slot. Expiração de PREPARED é CAS para REJECTED/VALIDATION_ABANDONED(dispatched=false); executor com lease vencido nunca consegue dispatch. Mesma chave replays resultado, nova confirmação corrigida exige nova chave explícita. CAS PREPARED→SENDING exige lease válido/dono, grava dispatched=true e é o único direito a um POST, sem retry de transporte. Após POST: ID conhecido persiste EXTERNAL_ACCEPTED antes da aceitação local; erro tipado que PROVA recusa persiste REJECTED; qualquer timeout/erro de protocolo/malformed success/ID ausente/crash em SENDING vira AMBIGUOUS, nunca falha presumida. EXTERNAL_ACCEPTED só pode recuperar trabalho LOCAL por identidade/externalId exatos, sem outro POST. Falha local temporária conserva esse estado recuperável. Conflito irrecuperável de identidade/geração/aposentadoria gera EXTERNAL_ACCEPTED_LOCAL_BLOCKED: conserva fato de aceite, identidade/ID originais e erro safe; nunca rebind na substituta, nunca vira recusa nem repete HTTP. Acknowledgment autorizado pode liberar seu slot, sem alterar esse fato. Uma vez liberado por resultado terminal/ack, slotReleasedAt/condição equivalente nunca volta a ativo: resultado tardio pode melhorar o outcome e reconciliar ID exato, mas não reassume slot nem bloqueia sucessora. SUCCEEDED é aceitação local com Message.id, não entrega ao aparelho. Retenção do recibo/key impede reutilização silenciosa, sem TTL que reenvie chave antiga. HTTP fora de transação; limite de uma invocação externa por intenção, não exactly-once de entrega nem dedupe entre intenções explicitamente diferentes. Snapshot: No Prior Decision para intenção; owner de Message preservado.
- [x] D-07 — Finalização local conhecida compõe uma transação curta com o owner MessageAcceptanceService, intenção e efeitos de atendimento: lock/validar identidade e linha atual; criação/reconciliação pelo índice identidade/externalId existente, autoria enriquecida no echo-first e uma Message/realtime vencedor, unread preservado pelo OUT. Status/autoatribuição somente enquanto a tentativa ainda detém o slot (nunca após release/ack) e por CAS contra updatedAt/estado capturados na reserva ANTES de HTTP, avaliando dono vivo; se linha mudou, preservar status/dono atuais e informar estado corrente, sem roubar claim nem desfazer close concorrente. CLOSED inalterado desde a reserva pode passar a IN_SERVICE após sucesso; CLOSED concorrente permanece. Sem nova ownership-revision global. Template grava snapshot textual e metadata mínima vinculada; tipo TEXTO preserva timeline. Novo fluxo NUNCA chama recordAmbiguousOutbound: incerteza sem ID fica só na intenção, não Message sem chave. Echo tardio com ID pode criar uma Message normal, mas não conclui intenção sem correlação comprovada; sem heurística texto/telefone/data. Fence de geração é local, não revoga HTTP iniciado. Preservar limite de crash pós-commit antes de realtime, sem outbox. Snapshot: aceitação ST-CON-01 Preserve; no-steal concretizado por CAS no novo fluxo.
- [x] D-08 — Estado do formulário usa BU/contato/canal/geração/revisão monotônica; respostas de revisão velha não abrem destino nem limpam draft atual, mesmo em mudança A→B→A. Repetir mesmo envio usa a mesma intenção; após refresh, GET start-options e GET /api/bff/conversations/:id/initial-messages/:attemptId retornam {attemptId,state,channelId,createdAt,messageId?,safeError?,acknowledgedAt?,slotReleasedAt?,needsReconciliation?}, sem exigir chave perdida no browser nem expor token/key/envelope. Projeção para ATENDENTE+ da BU; replay POST da chave continua restrito ao seu usuário. POST /api/bff/conversations/:id/initial-messages/:attemptId/reconcile exige sessão/CSRF/grant atual, é idempotente e estritamente LOCAL: classifica PREPARED vencido como REJECTED/VALIDATION_ABANDONED, SENDING abandonado como AMBIGUOUS e tenta aceitar ID conhecido EXTERNAL_ACCEPTED pelo owner corrente; conflito irrecuperável vira EXTERNAL_ACCEPTED_LOCAL_BLOCKED sem contornar fence. Nenhum provider GET/POST é feito por reconcile. GET readback é observacional; pode informar needsReconciliation/leaseExpired, nunca altera Message/outcome nem dispara reconciliação escondida. POST /api/bff/conversations/:id/initial-messages/:attemptId/acknowledge exige sessão/CSRF/grant atual e reconhece apenas AMBIGUOUS ou EXTERNAL_ACCEPTED_LOCAL_BLOCKED; preserva aceite/ambiguidade, registra ator/data e libera slot de forma irreversível, sem reenvio. PREPARED/SENDING ainda ativos não são reconhecíveis como falha; exigir reconciliação/classificação antes. Resposta tardia não readquire slot nem produz efeito de status/owner após release; CAS protege a sucessora. Bloqueio de inicial pendente/incerto vale na UI e na fronteira BFF/domínio, não só botão. Não copiar payload incerto ao composer comum; mostrar tentativa mesmo após refresh e risco de duplicação antes de acknowledgment/nova intenção. Catálogo vazio/indisponível/sem formato elegível informa motivo e mantém texto oficial bloqueado fora da janela. Template creation/submission e prova física não são simuladas. Snapshot: ST-ATT-01 freshness Preserve; No Prior Decision para recovery.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| project_constitution#system-invariants | BU/Contato unifica, domínio backend, templates só em TODO próprio | Preserve | D-01..08 e contrato próprio ST-CON-04 |
| inbox-and-conversations#contrato-aprovado-da-timeline-da-inbox | paginação e estado fresco | Preserve | D-02/D-08; sem alterar cursor/timeline |
| inbox-and-conversations#aceitação-de-mensagens-e-automação--st-con-01 | aceitação única e nenhum Nova conversa autorizado no recorte anterior | Supersede (Intentional) | apenas autorização de Nova conversa no NOVO TODO; dedupe/tenant/echo preservados |
| integrations-and-channels#cadastro-de-números-st-con-01 | credenciais e identidade scoped | Preserve | D-03/D-05/D-07 |
| integrations-and-channels#invariants | provider adapter e erro seguro | Preserve | catálogo/envio só no MetaClient |

## Decision Baseline (Frozen Before Implementation)

- [ ] D-01 — Abrir/reusar por POST /api/bff/business-units/:buId/conversations/open com {telefone}. UI exige DDI explícito (sem país inferido); backend aceita + opcional, remove apenas espaços/parênteses/hífen/ponto, rejeita letras/ramal/grupo, 8–15 dígitos e primeiro não zero. Autorizar BU/ATENDENTE antes de validação detalhada; 401/403/404 scoped. Retorno {conversaId,criada,contact}; nenhuma chamada externa. Criação exige pelo menos um canal local atual apto; ausência retorna CANAL_INDISPONIVEL sem nova conversa. Reuso de conversa existente não concede envio. Snapshot: Constituição BU/Contato e inbox invariants preservados.
- [ ] D-02 — Upsert pelo índice buId/contact existente; nova PESSOA QUEUED/unread0/lastMessageAt null; resolver/abrir não assume nem reabre existente e preserva unread. Leitura humana posterior da timeline segue marcação de lida ST-ATT-01. Ordenação da lista usa COALESCE(lastMessageAt,createdAt) desc + id desc, filtro/paginação no PostgreSQL, sem sort/merge em memória nem data falsa. Abrir persiste mesmo se operador fechar depois: atendimento vazio visível; cancelar antes de Abrir não persiste. Medir query/index via EPS; migration pode incluir índice de expressão se justificado. Snapshot: ST-ATT-01 preservado; No Prior Decision para abertura manual.
- [ ] D-03 — GET /api/bff/conversations/:id/start-options informa canais da BU, capacidade/explicação, geração/janela e projeção segura limitada a uma tentativa com slot ativo mais até10recentes, ordenadas no DB por createdAt/id e indicador de truncamento; nunca varrer/devolver todos os recibos. Consulta por attemptId é lookup scoped separado, sem histórico completo implícito. POST /api/bff/conversations/:id/initial-messages exige Idempotency-Key UUID e {channelId,expectedGeneration,mensagem:{tipo:TEXTO,texto}|{tipo:TEMPLATE,templateId,language,catalogAfter?,expectedDefinitionFingerprint,parameters}}. parameters é mapa string→string: chaves nominais exatas em NAMED, índices 1..N em POSITIONAL; sem campos Graph arbitrários. Canal/conta/telefone/credencial derivam da BU vinculada; revalidar readiness/epoch/grant; preservar gate atual de ChannelCredentialResolver(send): CONECTADO, receiptVerifiedAt, própria identidade/epoch e SUBSCRIBED/CONNECTED. UI explica recebimento ainda pendente, sem enfraquecer ST-CON-01 nem usar purpose verify/registration para enviar. O novo fluxo não usa canal[0] nem fallback. Pode operar em conversa reutilizada não vazia. Com nenhuma mensagem de transporte autoritativo, UI reconstrói primeiro envio após refresh e POST BFF /messages é recusado no domínio com INITIAL_SEND_REQUIRED antes de rede. Nova intenção e BFF /messages recusam enquanto outra intenção possui o slot ativo da conversa, incluindo PREPARED/SENDING/EXTERNAL_ACCEPTED/AMBIGUOUS/EXTERNAL_ACCEPTED_LOCAL_BLOCKED não reconhecida; o guarda é server-side no domínio e na UI, não depende de estado transitório da aba. Public API/Typebot não ganham idempotência global nem nova rota. Snapshot: ST-CON-01 Preserve; No Prior Decision para jornada inicial.
- [ ] D-04 — Adicionar Message.officialInboundAt nullable e proveniência confiável equivalente: somente msg.timestamp de IN OFICIAL no webhook Meta com assinatura válida e identidade/recurso verificados pode preenchê-lo via MensagemRecebida e MessageAcceptanceService. Aceitar como horário apenas segundos Unix inteiros positivos, data válida não futura relativamente ao recebimento; timestamp ausente/malformado/futuro permanece null, sem descartar a mensagem por isso. Legacy/import/OUT/não oficial não preenchem; sem backfill de createdAt/raw. Janela usa máximo horário qualificado IN/OFICIAL da identidade atual do canal escolhido e menos de24h no instante do POST. Abrir, OUT e template não abrem janela. Preservar Message.createdAt, ordem/cursor da timeline. Aplicar a política de horário ao responder compartilhado e testar BFF/API pública; registros antigos sem observação qualificada exigem nova IN oficial ou template, não janela por inferência. Sem suporte de chamada/importador. Snapshot: janela verdadeira preservada; supersede intencional da fonte de tempo de ingestão e da exclusão de template no novo fluxo.
- [ ] D-05 — GET /api/bff/conversations/:id/channels/:channelId/templates usa conta derivada do canal e cursor after opaco limitado512, página até50 por ação, sem fan-out. Retorno por template inclui id/nome/idioma/categoria/componentes/parameter_format, suporte/porquê, catalogAfter da página e definitionFingerprint SHA256 canônico de canal/conta/geração/templateId/nome/idioma/categoria/status/componentes/formato. Suporte: APPROVED UTILITY ou MARKETING; BODY textual com variáveis textuais NAMED/POSITIONAL; HEADER TEXT/FOOTER estáticos opcionais; sem botões/mídia/OTP/Flow/carrossel. Texto livre1..4096; templateId até64 dígitos, language até16, fingerprint64hex, até20 parâmetros de1..1024 caracteres, snapshot renderizado até4096; formato maior/incompatível não enviável com razão explícita. Revalidar template e pertencimento lendo somente a página da conta indicada por catalogAfter: cursor/hash cliente são assertions, nunca autorização. Se ID/idioma saiu da página ou definição/fingerprint mudou, recusar e exigir nova seleção/prévia. Antes de um envio novo: no máximo4 GETs (grant1 + até2 páginas de telefones do canal +1 página de templates; texto não faz última leitura), mais1 POST, cada request timeout10s, budget total55s/lease75s. Lista inconclusiva ou recurso além de página2 falha seguro, sem scan até achar. Both official initial-text/template HTTP incluem messaging_account_id fixado pela conta verificada do canal; nenhum accountId vem do cliente. Replay existente é servido antes de provider reads. Snapshot: integrations invariants Preserve; No Prior Decision para catálogo/envio textual scoped.
- [ ] D-06 — Intenção PostgreSQL durável por BU+usuário+Idempotency-Key UUID; payload canônico original inclui conversa/canal/geração, texto OU templateId/idioma/cursor/fingerprint/parâmetros, e contexto de recurso/conta resolvido no primeiro aceite. Autorizar antes de lookup/replay. Mesma chave/request canônico retorna mesma tentativa/resultado sem reler catálogo mutável; payload diferente409. Uma intenção por conversa possui o slot ativo, protegido por índice único parcial/condição equivalente transacional; slot é fato SEPARADO do outcome, com release monotônico e irreversível para aquela tentativa. PREPARED reserva lease75s de validação: qualquer falha de validação/grant/janela/template (inclusive indisponibilidade antes de dispatch) vira REJECTED(dispatched=false), sem Message/POST e libera slot. Expiração de PREPARED é CAS para REJECTED/VALIDATION_ABANDONED(dispatched=false); executor com lease vencido nunca consegue dispatch. Mesma chave replays resultado, nova confirmação corrigida exige nova chave explícita. CAS PREPARED→SENDING exige lease válido/dono, grava dispatched=true e é o único direito a um POST, sem retry de transporte. Após POST: ID conhecido persiste EXTERNAL_ACCEPTED antes da aceitação local; erro tipado que PROVA recusa persiste REJECTED; qualquer timeout/erro de protocolo/malformed success/ID ausente/crash em SENDING vira AMBIGUOUS, nunca falha presumida. EXTERNAL_ACCEPTED só pode recuperar trabalho LOCAL por identidade/externalId exatos, sem outro POST. Falha local temporária conserva esse estado recuperável. Conflito irrecuperável de identidade/geração/aposentadoria gera EXTERNAL_ACCEPTED_LOCAL_BLOCKED: conserva fato de aceite, identidade/ID originais e erro safe; nunca rebind na substituta, nunca vira recusa nem repete HTTP. Acknowledgment autorizado pode liberar seu slot, sem alterar esse fato. Uma vez liberado por resultado terminal/ack, slotReleasedAt/condição equivalente nunca volta a ativo: resultado tardio pode melhorar o outcome e reconciliar ID exato, mas não reassume slot nem bloqueia sucessora. SUCCEEDED é aceitação local com Message.id, não entrega ao aparelho. Retenção do recibo/key impede reutilização silenciosa, sem TTL que reenvie chave antiga. HTTP fora de transação; limite de uma invocação externa por intenção, não exactly-once de entrega nem dedupe entre intenções explicitamente diferentes. Snapshot: No Prior Decision para intenção; owner de Message preservado.
- [ ] D-07 — Finalização local conhecida compõe uma transação curta com o owner MessageAcceptanceService, intenção e efeitos de atendimento: lock/validar identidade e linha atual; criação/reconciliação pelo índice identidade/externalId existente, autoria enriquecida no echo-first e uma Message/realtime vencedor, unread preservado pelo OUT. Status/autoatribuição somente enquanto a tentativa ainda detém o slot (nunca após release/ack) e por CAS contra updatedAt/estado capturados na reserva ANTES de HTTP, avaliando dono vivo; se linha mudou, preservar status/dono atuais e informar estado corrente, sem roubar claim nem desfazer close concorrente. CLOSED inalterado desde a reserva pode passar a IN_SERVICE após sucesso; CLOSED concorrente permanece. Sem nova ownership-revision global. Template grava snapshot textual e metadata mínima vinculada; tipo TEXTO preserva timeline. Novo fluxo NUNCA chama recordAmbiguousOutbound: incerteza sem ID fica só na intenção, não Message sem chave. Echo tardio com ID pode criar uma Message normal, mas não conclui intenção sem correlação comprovada; sem heurística texto/telefone/data. Fence de geração é local, não revoga HTTP iniciado. Preservar limite de crash pós-commit antes de realtime, sem outbox. Snapshot: aceitação ST-CON-01 Preserve; no-steal concretizado por CAS no novo fluxo.
- [ ] D-08 — Estado do formulário usa BU/contato/canal/geração/revisão monotônica; respostas de revisão velha não abrem destino nem limpam draft atual, mesmo em mudança A→B→A. Repetir mesmo envio usa a mesma intenção; após refresh, GET start-options e GET /api/bff/conversations/:id/initial-messages/:attemptId retornam {attemptId,state,channelId,createdAt,messageId?,safeError?,acknowledgedAt?,slotReleasedAt?,needsReconciliation?}, sem exigir chave perdida no browser nem expor token/key/envelope. Projeção para ATENDENTE+ da BU; replay POST da chave continua restrito ao seu usuário. POST /api/bff/conversations/:id/initial-messages/:attemptId/reconcile exige sessão/CSRF/grant atual, é idempotente e estritamente LOCAL: classifica PREPARED vencido como REJECTED/VALIDATION_ABANDONED, SENDING abandonado como AMBIGUOUS e tenta aceitar ID conhecido EXTERNAL_ACCEPTED pelo owner corrente; conflito irrecuperável vira EXTERNAL_ACCEPTED_LOCAL_BLOCKED sem contornar fence. Nenhum provider GET/POST é feito por reconcile. GET readback é observacional; pode informar needsReconciliation/leaseExpired, nunca altera Message/outcome nem dispara reconciliação escondida. POST /api/bff/conversations/:id/initial-messages/:attemptId/acknowledge exige sessão/CSRF/grant atual e reconhece apenas AMBIGUOUS ou EXTERNAL_ACCEPTED_LOCAL_BLOCKED; preserva aceite/ambiguidade, registra ator/data e libera slot de forma irreversível, sem reenvio. PREPARED/SENDING ainda ativos não são reconhecíveis como falha; exigir reconciliação/classificação antes. Resposta tardia não readquire slot nem produz efeito de status/owner após release; CAS protege a sucessora. Bloqueio de inicial pendente/incerto vale na UI e na fronteira BFF/domínio, não só botão. Não copiar payload incerto ao composer comum; mostrar tentativa mesmo após refresh e risco de duplicação antes de acknowledgment/nova intenção. Catálogo vazio/indisponível/sem formato elegível informa motivo e mantém texto oficial bloqueado fora da janela. Template creation/submission e prova física não são simuladas. Snapshot: ST-ATT-01 freshness Preserve; No Prior Decision para recovery.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability (`required|not_needed`):** required
- **Why this applies:** novo contrato compartilhado de primeiro envio e intenção persistente; supersede limitado da exclusão manual/template do recorte anterior.
- **Deviation / debt being retired:** dependência de IN para abrir na inbox; repetição de HTTP não deve duplicar a primeira saída deste fluxo. Não alegar correção global dos senders.
- **Target steady-state after closeout:** domínio inbox único para abertura/intenção, MetaClient para provider e MessageAcceptanceService para registro; sem segundo owner de mensagem.
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** todo caller do novo fluxo usa intenção; sem rota técnica de token/Sandbox, fallback ou camada paralela.

### Patterns To Enforce (Required when applicability = `required`)

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| owner único de Message | inbox ST-CON-01; D-06/07 | inbox/envio/echo | chave transacional/autoria sem rota paralela |
| intenção persistente e HTTP fora da transação | D-06 | primeiro envio BFF | crash/replay não repete POST |
| evento oficial confiável separado da timeline | D-04; ST-ATT-01 | Meta/Message/janela | dado atrasado não reabre janela por ingestão |

### Prohibited Anti-Patterns (Required when applicability = `required`)

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| só botão/Map em memória | E2E restart/duplo POST | duplica saída | none |
| Message sem ID para nova ambiguidade | late echo test | duplica Message | none |
| createdAt como backfill de janela | evento antigo/missing/future | simula autoridade temporal | none |
| canal/conta default ou hash cliente como autoridade | BFF/provider contract tests | envia pelo recurso errado | none |

### Architecture Protection Harness (Required when applicability = `required`)

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | domínio/PG | api-app/test/start-conversation.e2e-spec.ts via bash scripts/test-channels-local.sh all | D-01..07 auth/window/intent/echo/claim/close/barriers | implement-in-this-todo | DOD-03/05/07 e VAL-01/02 |
| test | Web real BFF | web-app/e2e/start-conversation.spec.ts mesmo runner | refresh vazio/incerto, stale A→B→A, template/fingerprint, negative flow | implement-in-this-todo | DOD-01/04/06/07 e VAL-03 |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** not_run
- **Decision review evidence / resolution:** pareceres2026-10-19 preservados como histórico; nova revisão tática após contrato ST-CON-06 e reconvergência do consumer. Parecer de enquadramento2026-10-20 não satisfaz este gate.
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
- **Baseline commit:** 507ec7ebc394144b0f072e92459fa91e06921c50
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** contrato final aceito no delta f71a7d99; refresh apenas para acrescentar âncora SQL concreta de A01, que o parser de premissas reconhece. Nenhuma decisão/critério/escopo alterado.
- **Evidence / reference:** origin/main 507ec7ebc394144b0f072e92459fa91e06921c50 push terminal0; só metadata factual acrescentada após freeze. Baselines anteriores preservadas.
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
- **Findings summary:** Context material alterado em2026-10-20 pela direção Channel; baseline/guard anterior histórico. Requer reconvergência/review e novo freeze antes de aprovação.
- **Evidence / reference:** artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md; parecer de enquadramento artifacts/analysis/leadshug-channel-abstraction-framing-opinion-20261020.md; JSON go anterior é histórico, não resultado do ciclo atual.
- **Waiver authority / reference (required if waived):** n/a

## Questions To Close

Fechar consumo dos ports Channel/capacidade e novo baseline após ST-CON-06; reconvergir decisões, paths, DI e validação deste consumer. Requer revisões/guardas próprios antes de pedir APROVADO novamente.

## Pattern References (Optional; Enforced When Cited)

n/a; decisões canônicas citadas diretamente, sem IDs de catálogo presumidos.

## Assumptions Preview (Required Before Plan Review)

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Schema já impõe uma conversa por BU/contato. | api-app/prisma/schema.prisma:379; api-app/prisma/migrations/20260818125556_nucleo_v1_tenancy_identidade_atendimento/migration.sql:230 | rever upsert e migrations antes da aprovação | High | Keep as Assumption |
| A-02 | BFF atual só lista/timeline/responde, não abre contato manual. | api-app/src/surfaces/bff/conversations.controller.ts | reutilizar owner existente | High | Keep as Assumption |
| A-03 | MetaClient não possui catálogo/envio template. | api-app/src/integrations/meta/meta.client.ts | integrar componente existente, sem duplicar | High | Keep as Assumption |
| A-04 | Envio atual já converge sender/echo pelo serviço de aceitação. | api-app/src/domain/inbox/conversations.service.ts; api-app/src/domain/inbox/message-acceptance.service.ts | corrigir desenho antes de código | High | Keep as Assumption |
| A-05 | Inbox usa gerações/drafts e browser serve build com API/PG exclusivos. | web-app/src/telas/Inbox.tsx; web-app/playwright.config.ts | ajustar plano de fixture/freshness | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces
Paths positivos do Diff Expectation Contract; nenhum runtime/segredo lido neste planejamento.

### Ordered Steps
1. Após APROVADO: reload binding, routing/authority go, executor único na principal; conferir branches, baseline e limpeza por inventário positivo público.
2. Test-first: normalização, auth/CSRF, abertura/reuso, parser temporal Meta confiável (ausente/antigo/futuro), janela só oficial, schema/intenção e provider fixture; RED válido antes do código correspondente.
3. Resolver de conversa e migrations da intenção/officialInboundAt; estado/resultado crash-safe, EXTERNAL_ACCEPTED/local quarantine/recovery/acknowledgment, release monotônico de slot e CAS de atendimento; preservar owner de Message e rotas públicas existentes.
4. Catálogo Meta scoped, paginação limitada, parser de componentes/params e sender textual; manter erro fixo seguro e snapshot local.
5. Formulário NovaConversa com revisão monotônica, recuperação após refresh e bloqueio no BFF/domínio para composer comum sem transporte/intent incerta; integrar Inbox sem refazer timeline.
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
Migration aditiva versionada; deploy/status primeiro no PG descartável. Dados oficiais anteriores sem timestamp confiável não recebem janela inferida: nova IN oficial ou template será necessária. createdAt/cursor/histórico ficam intactos. Antes de eventual runtime privado, readiness e backup scoped próprios, sem reset. Limite: crash após HTTP pode permanecer ambíguo; não background retry, worker, outbox ou claim exactly-once. Fonte e API/DB/porta publicadas devem coincidir com CI-equivalent; não usar web-app/dist antigo. Nenhum restart, túnel ou envio real autorizado nesta preparação.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

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
- [ ] Arquitetura terminal encontrou seis blockers na minuta original, integrados na proposta; crítica encontrou três lacunas residuais de lifecycle e uma de projeção, integradas; delta final aceito no_remaining_approval_blockers, confirmado após âncora SQL507ec7eb; guardas de planejamento go/preflight-go, sem autoridade de implementação.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

- **Needed:** no
- **Why ambiguity remains:** n/a; arquitetura e crítica independentes concluídas com achados integrados e delta verificado, sem opinião adicional duplicada.
- **Opinion count:** 0
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required na gate arquitetural
- **Required lenses:** correctness,performance,elegance,structural-soundness,operational-fit

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **Latest TEACH evidence / artifact:** artifacts/tmp/st-con-04-audit-floor.json, go; crítica/arquitetura/segurança/pcv/TQA/final/dívida obrigatórias, multi-lane recomendado adotado.

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
- **Findings summary:** ciclo anterior2026-10-19 concluído, histórico; direção Channel2026-10-20 exige novo pacote tático/freeze e crítica antes de aprovação.
- **Resolution ledger:** Planning Finding Resolution Ledger
- **Evidence / reference:** artifacts/reviews/leadshug-start-conversation-20261019/critique.md
- **Waiver authority / reference (required if waived):** n/a

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
- **Guard outcome:** go
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
- **Post-commit/push status:** complete
- **Next path/status action:** pedir APROVADO do contrato, sem claim de implementação/entrega.

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
- **Gate status:** no_material_findings
- **Findings summary:** A-01..05 conferidas semanticamente nas fontes públicas correntes e pelos reviewers;13arquivos públicos nomeados byteexact com HEAD, incluindo SQL do índice único. NOGO inicial preservado: parser não reconhece extensão .prisma; adicionada migration.sql real que prova o MESMO índice, sem alterar premissa ou regra.
- **Evidence / reference:** artifacts/reviews/leadshug-start-conversation-20261019/source-assumptions.json; evidence/code-coherence-initial-no-go.json preservado; evidence/code-coherence.json final go para5premissas
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

## Frontend / Consumer Matrix

| Producer / contract | Consumer | Ownership / authorization | User-visible effect | Planned validation |
| --- | --- | --- | --- | --- |
| POST BU/conversations/open | NovaConversa + Inbox | BU atual/ATENDENTE/session/CSRF | novo/reuso, nenhum envio e nenhum mark-read implícito no resolver | browser abrir/reuso/readback; PG race |
| GET start-options e tentativa por ID | form/composer após refresh | conversa/BU atual; safe DTO sem key/secret | canal/janela e outcome persistente, INITIAL_SEND_REQUIRED quando sem transporte | browser refresh e stale tab POST real |
| GET templates | selector/preview | canal atual da mesma BU, conta server-side | próximo cursor/fingerprint/textual subset/empty/error | provider HTTP/schema + browser |
| POST initial-messages | confirmation/outcome | current grant/context + idempotency | uma intenção externa, não claim entregue | duplicate-key/late-echo/crash/foreign account tests |
| POST attempt/reconcile | explicit local recovery action | sessão/CSRF/ATENDENTE da BU | classifica expirado/aceita ID exato ou quarentena, nenhum provider call | lost-key browser/PG e provider count zero |
| POST attempt/acknowledge | explicit recovery action | sessão/CSRF/ATENDENTE da BU | preserva fato, libera slot permanentemente, nenhum resend | readback/late result/sucessora; provider count zero |
| Meta signed timestamp → Message.officialInboundAt | janela BFF/pública/primeiro envio | assinatura + identidade corrente, nullable trusted observation | somente IN qualificada abre24h; campos da timeline preservados | signed webhook E2E/missing/old/future; timeline regressão |
| new-flow official POST messaging_account_id | Meta | ID somente do canal resolvido | envio/template e atribuição na conta escolhida | fixture token com duas contas, request body asserted |

### Outcome projection / monotonic recovery

Intenção expõe somente outcome safe: PREPARED (validação ainda sem POST), SENDING (não repetir), EXTERNAL_ACCEPTED (ID durável, finalização apenas local), EXTERNAL_ACCEPTED_LOCAL_BLOCKED (aceite conhecido preservado, fence irrecuperável/quarentena), SUCCEEDED (Message persistida, não delivery), REJECTED (pré-dispatch comprovado ou recusa tipada do provider), AMBIGUOUS (resultado desconhecido). Slot é ortogonal e, após liberado, nunca readquirido pela tentativa antiga. Responses: 201 novo sucesso; 200 replay terminal/readback; 202 processamento; 409 conflito/initial-send-required/contexto/ambiguidade com safe attemptId e outcome, sem dados estrangeiros; falha externa inconclusiva503 com outcome safe. Never expose provider body/token. Readback usa GET observacional e mesma autorização de BU, não chave do browser. Reconciliação exige POST autenticado/CSRF e só operações locais, nunca chamada ao provider. Acknowledgment é idempotente por tentativa, vale para AMBIGUOUS ou EXTERNAL_ACCEPTED_LOCAL_BLOCKED e não converte ambos em REJECTED nem reinicia HTTP. Resultados tardios conhecidos podem concluir monotonicamente a MESMA intenção sem repetir POST; ausência de ID correlacionável conserva ambiguidade. Recibos de entrega continuam independentes.

## Planning Finding Resolution Ledger

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-01 | Integrated | useful | partial | project | none | D-04; timestamp nullable confiável + ingress paths/tests; sem backfill e timeline intacta |
| ARCH-02 | Integrated | useful | partial | project | none | D-03/08; BFF/domain guard e recuperação segura/ack separado após refresh |
| ARCH-03 | Integrated | useful | partial | project | none | D-03/05; fingerprint confirmado, página da conta, limites e shape finitos |
| ARCH-04 | Integrated | useful | partial | project | none | D-05/06/07; messaging_account_id server-side nos dois sends oficiais novos |
| ARCH-05 | Integrated | useful | partial | project | none | D-06/07; outcome tipado, EXTERNAL_ACCEPTED, sem Message ambígua e sem heurística |
| ARCH-06 | Integrated | useful | partial | project | none | D-07; lock/CAS de linha viva, concurrent claim/close preservados |
| ARCH-NOTES | Integrated | useful | partial | project | none | D-02/05; read versus resolve, quatro reads concretos e query/index EPS no DB |
| TEMPLATE-STRUCTURE | Integrated | useful | no | none | none | remover headings duplicados e acrescentar nested harness/consumer matrix omitidos na população inicial |

### Module coherence — one-to-one before approval

| Frozen decision | Prior module decision | Handling | Evidence / outcome |
| --- | --- | --- | --- |
| D-01 | Constitution/Inbox BU-contact | Preserve | mesmo índice/domínio, BFF sessão; sem novo runtime surface |
| D-02 | ST-ATT-01 timeline/read acknowledgement | Preserve | createdAt/cursor/read preservados; apenas ordenação de lista inclui vazio |
| D-03 | ST-CON-01 excludes manual in its slice | Supersede (Intentional) | nova autoridade apenas ST-CON-04, mantendo contrato anterior entregue |
| D-04 | official24h / persistent timeline | Supersede (Intentional) | fonte temporal passa de ingestão para observação confiável; dados legacy null sem backfill |
| D-05 | Integrations provider adapter/scoped credential | Preserve | catálogo e send no adapter, conta do canal |
| D-06 | ST-CON-01 no exactly-once/outbox | Preserve | intenção limitada ao novo fluxo, owner Message único |
| D-07 | ST-CON-01 echo/sender identity/author | Preserve | composição transacional e CAS, nenhuma cópia do owner |
| D-08 | ST-ATT-01 freshness/draft | Preserve | formulário por contexto/revisão, recovery persistente separado de resend |

Primary docs additionally consulted: [Messaging account selection](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/messaging/), [Template API](https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-account/message-template-api/), [Send messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages/). Public documentation only; no account/provider runtime calls.

## Critique Resolution — final lifecycle delta

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CRIT-01 | Integrated | useful | partial | project | none | D06/08; EXTERNAL_ACCEPTED_LOCAL_BLOCKED retém fato/ID/identidade; acknowledgment libera slot sem bypass/rebind/resend |
| CRIT-02 | Integrated | useful | partial | project | none | D06/07/08; slot separado do outcome, release irreversível; old late result sem readquirir slot nem mudar atendimento |
| CRIT-03 | Integrated | useful | partial | project | none | D03/06/08; PREPARED failure/expiry terminal dispatched=false; guard BFF; POST reconcile local-only, GET observacional |
| CRIT-04 | Integrated | useful | partial | project | none | D03; ativo + até10recentes no DB, truncamento explícito, query/EPS |

### Additional exact validation commitments

1. Pausar após provider ID, aposentar geração/identidade, concluir/reconciliar: uma chamada externa, nenhum aceite na identidade substituta, safe quarantine readback e acknowledgment/release explícito.
2. AMBIGUOUS → ack/release → sucessora ativa → ID tardio da antiga: sucessora mantém slot; antiga só melhora seu outcome/Message exata elegível, sem tocar owner/close atuais ou chamar rede novamente.
3. Mudar template/janela/grant antes de dispatch: terminal REJECTED(dispatched=false), zero Message/POST, slot liberado e nova confirmação/chave possível.
4. PREPARED com lease vencida concorrente com validator atrasado: CAS terminal impede dispatch; POST reconcile após refresh sem chave executa zero provider GET/POST.
5. start-options nunca retorna todos os recibos; uma ativa+até10recentes, truncamento e ordem/index/query medidos em EPS.
6. Readiness anterior ST-CON-01 preservada: sem receipt/own epoch/current credential/estado pronto, nenhum primeiro OUT, orientação explícita em start-options.

Delta altera a minuta ainda não aprovada para tornar sua própria recuperação executável; não autoriza implementação nem altera objetivo primário. Usuário avaliará este contrato final, não as minutas anteriores.

## Planning guard compatibility note

Assumption-code guard inicialmente retornou NO-GO apenas em A01: seu parser PATH_RE/CODE_EXTENSIONS não reconhece .prisma. A premissa continua sendo a unicidade BU/Contato. Acrescentou-se referência à migration.sql:230, CREATE UNIQUE INDEX conversations_bu_id_contact_key ON conversations(bu_id,contact), fonte real que o guard reconhece. Não houve alteração de Delphi, waiver, supressão do achado nem mudança de produto. NOGO inicial preservado em evidence/code-coherence-initial-no-go.json; guards finais serão reexecutados depois de publicar a âncora.

## Planning Readiness Summary — awaiting human approval

- Gate0: projeto estabelecido, Strategic/CTO; implementação planejada Operational/Coder após APROVADO, executor gpt-6-luna/medium, principal checkout único sem worktrees.
- Arquitetura independente: ARCH-01..06 Integrated; crítica fresh independente e delta: CRIT-01..04 Integrated, no_remaining_approval_blockers; confirmação final da âncora SQL507ec7eb mantém conclusões e rubrica, sem novo no-context claim.
- Assumption-code coherence: go,5premissas;13fontes públicas nomeadas byteexact com HEAD; diagnóstico inicial .prisma não reconhecido preservado e resolvido por migration.sql real, sem alterar guard.
- Review scope drift: go,23seções/0mudanças materiais contra baseline507ec7eb publicada. Guards finais anexados no pacote.
- Authority pre-approval: preflight-go, execution_authority_granted=false. Validação estrutural PASS. Nenhum teste de produto/build/browser executado neste planejamento e nenhum código/runtime/conta Meta alterado.
- Template aprovado: operador ainda não possui; essa prova real permanece pendente, não é satisfeita por fixture. Dados antigos sem observação oficial confiável não recebem janela inferida nem backfill de createdAt.
- Única próxima autorização: APROVADO humano específico deste contrato final; não reusar aprovação de ST-CON-01. Mudança material posterior exige reconvergência/aprovação, sem source push/deploy ou outras exclusões implícitas.

## Sequencing handoff — request2026-10-19

Usuário quer vendedor criar e enviar modelo para análise da Meta dentro do LeadsHug. Autoridade desse novo objetivo é o [TODO ST-CON-05](TODO-leadshug-official-template-authoring.md), não uma ampliação silenciosa deste sender. ST-CON-04 permanece sem aprovação/implementação e preserva suas exclusões de criação/gestão. Após entrega do ST-CON-05, rebasear premissas/source/diff/DI para consumir o mesmo domínio/catálogo, sem duplicá-lo; rerodar reviews afetados/guardas e pedir APROVADO do consumer então. Revisões/guardas anteriores continuam evidência histórica de seu próprio baseline, não autorização do programa ampliado.

## Reframing — Channel abstraction request, 2026-10-20

ST-CON-04 conserva o objetivo funcional e permanece sem APROVADO específico de implementação. Nova direção humana exige Channel abstrato, concretos de WhatsApp e resolução/injeção scoped; preparar ST-CON-06 antes deste consumer. [Enquadramento e evidência](../../../artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md).

Decisões, pareceres e guardas de2026-10-19 descrevem o pacote então revisado; não são aprovação/readiness do contrato que será rebaseado. Este registro apenas invalida a indicação anterior de pronto para aprovação e preserva o histórico; assinaturas/paths/baseline serão reconvergidos no próximo ciclo de refinamento/reviews/guardas, sem adaptar código antecipadamente.


## Handoff recebido de ST-CON-06 v1.3

Fonte/cutover e quatro PCV convergidos; all93791/613testes, ativação local e nova troca física IN/OUT nos dois canais confirmadas. ST-CON-06 está encerrado localmente: revisão final sem findings e guards GO registrados no mesmo TODO concluído. Consumir agora os contratos canônicos de Channel/Resolver e OutboundService em modules/integrations-and-channels.md e modules/inbox-and-conversations.md. Não há aprovação de implementação desta história: reconvergir seu próprio contrato, fonte/baseline e revisões antes de novo APROVADO.

Keep the user's selected behavior: the seller can start a conversation in LeadsHug by supplying the contact. Rebase this story after05: approved-template selection and parameters may be required when the official free-text window is closed. No template bypass or weakening of requiresWindow is authorized by06.

Use the common abstract transport/orchestration and sole MessageAcceptance owner. Current public POST still creates the conversation before attempting a send and may leave it empty on failure;06 intentionally preserves this behavior. Any new intent/durability, deduplication, conversation-creation timing or recovery policy belongs in04's reviewed contract. ACCEPTED means a valid provider message ID, not handset delivery; UNKNOWN and ACCEPTED_LOCAL_INCOMPLETE forbid blind resend and require truthful UI/draft handling.

Explicit residuals to reconverge: current latest-IN window uses stored createdAt without transport filtering; null-ID diagnostics cannot safely merge with echoes by heuristics; local-check-to-network and crash gaps remain. Do not silently substitute the latest/current channel identity into a captured dispatch. Resolve these against first-send requirements before renewed APROVADO, without portraying them as already solved in06.
