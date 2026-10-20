# Tactical TODO — ST-CON-06

## Title
LeadsHug — ST-CON-06: Channel abstrato extensível e cutover do envio comum

## Artifact Identity
- **Artifact type:** tactical_execution_contract
- **Status:** NotStarted
- **Version:** 1.0
- **Created:** 2026-10-20
- **Template provenance:** copied delphi-ai/templates/todo_template.md before population.

## Context
Usuário confirmou Channel abstrato/concretos e extensibilidade para Instagram, Facebook/Messenger, Telegram e outros; em2026-10-20 autorizou avançar ao contrato. Este TODO entrega o cutover do envio textual comum atual, não novos provedores reais. MetaClient/EvolutionClient já são interfaces injetadas, mas Conversa/Typebot conhecem ambos e seus parâmetros. O parecer de enquadramento identificou outcomes falsamente tratados como recusa, escopo/versionamento insuficientemente expresso e fallback de canal divergente da política. Decisões abaixo concretizam esses pontos antes da revisão tática. O parecer anterior não satisfaz os gates deste contrato e concordância com conceito não é APROVADO específico.

## Framing Source & Story Slice
- **Feature brief:** foundation_documentation/artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md
- **Primary story ID:** ST-CON-06
- **Why this is the right current slice:** um owner de transporte comum para todos os senders existentes, antes de modelos ST-CON-05 e primeiro envio ST-CON-04.
- **Direct-to-TODO rationale (required when `Feature brief = direct-to-todo`):** n/a; brief e parecer prévios publicados.

## Contract Boundary
- This TODO defines **WHAT** must be delivered and what counts as done.
- `Assumptions Preview` and `Execution Plan` below define **HOW** Delphi currently intends to deliver this contract.
- This TODO is **bounded but elastic**: Delphi may absorb local discoveries only while they remain inside the same primary objective and the same main approval/review/promotion conversation. Secondary modules may still be touched when they are subordinate to that same slice.
- If any assumption or plan step changes `Scope`, `Out of Scope`, `Definition of Done`, required validation semantics, public contract, or frozen decisions, update the TODO contract first and request renewed approval before execution continues.
- If the intended path explicitly authorizes a compatibility shim, fallback bridge, dual-read/dual-write period, or another non-canonical temporary construct, record that authorization in the TODO with exact scope, rationale, and removal/closeout condition. Reviewers must be able to distinguish an approved temporary exception from accidental workaround drift.

## Implementation Intent
- **Current delivery:** contrato abstrato de envio textual, resolução scoped, implementações atuais e orquestração compartilhada, com política/outcomes/consumers/testes coerentes.
- **Planned next steps:** reconvergir ST-CON-05 para capacidades de modelos e ST-CON-04 para primeiro envio/intent; redes adicionais em histórias próprias.
- **Anticipatory implementation authorized now:** somente o ponto de extensão e fake de teste exigidos no D01/08; nenhuma implementação/capacidade real futura.
- **Rationale:** dependências apontam ao domínio abstrato; protocolo e segredo ficam nos adapters, aceitação/política no domínio.

## Delivery Status Canon (Required)
- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** publicar freeze deste TODO, architecture_opinion e crítica independentes, guardas pré-aprovação; pedir APROVADO antes de produto.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** review
- **Why this state now:** preparação do contrato tático; código/runtime intactos.
- **Exit condition:** pacote convergido + APROVADO específico + reload binding + authority go.

## Scope
- [ ] SCOPE-01 — Channel/ChannelResolver abstratos de domínio, registro explícito e instâncias por operação, concretos oficial/não oficial e extensão verificada com fake não WhatsApp.
- [ ] SCOPE-02 — Migrar envios de Conversa BFF/API pública e respostas Typebot para a mesma orquestração, mantendo autenticações próprias, política e MessageAcceptanceService único.
- [ ] SCOPE-03 — Contexto autorizado e owner BU/canal, segredos privados, credencial/identidade correntes e fences explícitos; nenhuma troca silenciosa do canal selecionado.
- [ ] SCOPE-04 — Outcomes tipados verdadeiros, projeção pública explícita de erro/disponibilidade e UI honesta; sem retry externo automático ou garantia de exactly-once.
- [ ] SCOPE-05 — Runner de inventário positivo antes de testes, harness durável de imports/contrato/PG/Playwright, regressões completas e prova real assistida nos dois vínculos próprios; consolidação/revisões de entrega.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)
n/a; sem entrega de produto reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)
Planejamento não bloqueado; readiness de runtime/túnel/aparelhos revalidada depois da aprovação. Ausência de template aprovado não bloqueia esta história textual em janela válida.

## Execution Lane Tracking (Required)
- **Local implementation branches:** root/api/web:feature/number-onboarding, confirmar antes de executor; Foundation:main.
- **Promotion lane path:** local feature → dev → stage → main; nenhum push/deploy de produto nesta autorização local proposta.
- **Lane-promoted threshold for this TODO:** dev, fora do escopo atual.
- **Production-ready threshold for this TODO:** main e gates próprios, sem claim atual.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)
n/a; só Foundation main é autoridade documental autônoma nesta preparação.

## Out of Scope
- [ ] Instagram/Messenger/Telegram reais, alteração de identidade/BU/contato/schema ou enums de persistência para novas redes; fake não prova integração real.
- [ ] Criação/envio de templates, Nova conversa manual/novo intent, importação, campanhas, anexos ou novos fluxos Typebot; ST-CON-05/04 permanecem separados.
- [ ] Reescrever OAuth/QR/cadastro/lifecycle, rotacionar credenciais, desconectar vínculos ou criar sondagem externa por envio.
- [ ] Worker/outbox/fila, durable intent/exactly-once externo, retry automático de POST, heurística para unir eco sem ID.
- [ ] Delphi, worktrees/cópias, gitlinks/.gitmodules, deploy/push de produto, leitura de .env/.env.testing e qualquer read/list/stat/hash/traversal/mount/stage api-app/.local-files.

## Diff Expectation Contract (Required Before Delivery)
- **Contract status:** required
- **Policy:** strict; forbidden/unclassified blocks delivery
- **User validation:** required on deviation
- **Comparison mode:** working_tree

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| root | . | 80e3940126f22a941f90dba4f5e801b6c0eb2f58 | working_tree |
| api | api-app | db5a86758a165fac8a1ab587599c37b17890530c | working_tree |
| web | web-app | 74b9d4b714044829796f875d00553f077c1c329d | working_tree |
| foundation | foundation_documentation | 82fa66b33b81b31024dc8cebef9e72e9253964a7 | working_tree |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/domain/channels/transport/** | any | ports/resolver/orquestração/registro e harness |
| api | src/integrations/channels/** | any | concretos e projeções privadas |
| api | src/domain/channels/channel-credential-resolver.ts | M | contexto/versionamento privado, send protegido |
| api | src/domain/inbox/outbound*.ts | any | política/orquestração sem ciclo DI com Conversations |
| api | src/domain/inbox/conversations.service.ts | M | seleção/política e consumo abstrato |
| api | src/domain/inbox/incoming.service.ts | M | Typebot usa saída comum |
| api | src/integrations/meta/meta.client.ts | M | texto com resultado tipado; cadastro preservado |
| api | src/integrations/meta/*.spec.ts | any | wire/erro real do adapter |
| api | src/integrations/evolution/evolution.client.ts | M | texto com resultado tipado |
| api | src/integrations/evolution/*.spec.ts | any | wire/classificação conservadora |
| api | src/surfaces/bff/conversations.controller.ts | M | contexto autorizado e DTO disponibilidade |
| api | src/surfaces/public/conversations.controller.ts | M | contexto API key e projeção compatível |
| api | src/surfaces/bff/bff.module.ts | M | DI da composição única |
| api | src/surfaces/public/public.module.ts | M | DI preservando auth |
| api | src/surfaces/webhooks/webhooks.module.ts | M | DI Typebot/ingress |
| api | test/channel-transport* | A | PG/contrato/corridas |
| api | test/helpers.ts | M | fakes/DI de contrato |
| api | test/timeline-fixtures.cjs | M | provider controlado de browser |
| api | test/browser-server.cjs | M | bootstrap real |
| api | test/*.e2e-spec.ts | M | suites consumidoras da interface alterada, sem afrouxar assertivas |
| api | src/domain/inbox/*.spec.ts | M | consumo abstrato e regressões |
| web | src/api.ts | M | DTO aditivo disponibilidade |
| web | src/telas/Inbox.tsx | M | composer indisponível/motivo e erro |
| web | src/telas/Inbox*.test.tsx | any | render/estado |
| web | e2e/channel-transport* | A | mutation BFF real |
| web | e2e/number-onboarding-freshness.ts | M | manifesto se afetado |
| root | scripts/test-channels-local.sh | M | inventário positivo seguro antes de testes |
| foundation | todos/active/features/TODO-leadshug-channel-abstraction.md | M | governança/evidências |
| foundation | todos/completed/features/TODO-leadshug-channel-abstraction.md | A | closeout após gates |
| foundation | todos/active/features/TODO-leadshug-official-template-authoring.md | M | handoff sem execução |
| foundation | todos/active/features/TODO-leadshug-start-conversation-by-contact.md | M | handoff sem execução |
| foundation | artifacts/reviews/leadshug-channel-abstraction-20261020/** | any | reviews/evidências |
| foundation | artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md | M | link do contrato |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | sequência |
| foundation | backlog/README.md | M | próximo gate |
| foundation | artifacts/dependency-readiness.md | M | readiness observada |
| foundation | modules/integrations-and-channels.md | M | ports/outcomes/cutover após entrega |
| foundation | modules/inbox-and-conversations.md | M | política/consumers após entrega |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .local-files/** | any | privado, nem percorrer |
| api | .env* | any | segredo/config intocados |
| api | prisma/** | any | sem mudança de persistência/migration |
| root | .env* | any | privado |
| root | .gitmodules | any | pipeline-owned |
| root | api-app | any | gitlink pipeline-owned |
| root | web-app | any | gitlink pipeline-owned |
| root | delphi-ai | any | sem self-improvement |
| web | dist/** | any | gerado, não fonte |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
Guard de entrega ainda não executado. API exige inventário positivo de paths públicos; não executar guard que percorra API inteira. Descoberta fora do inventário exige reconvergência/aprovação.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** DI, DTO/fixture/componente subordinados ao mesmo envio comum e preservação de seus invariantes.
- **Must update or split the TODO:** schema/novo provedor/capacidade real, template/intent novo, mudança de política fora das decisões e novos endpoints.

## Definition of Done
- [ ] DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real.
- [ ] DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes.
- [ ] DOD-03 — Seleção de canal segue última origem ou único vínculo sem origem; ausência/ambiguidade falha sem fallback, leitura expõe disponibilidade e UI explica bloqueio preservando rascunho.
- [ ] DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout.
- [ ] DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; política e finalização não roubam claim concorrente; diferenças de unknown/retirada estão explícitas.
- [ ] DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot.
- [ ] DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede.
- [ ] DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção.

## Validation Steps
- [ ] VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo, sem subset como aceite, com API/PG reais e bundle servido fresco.
- [ ] VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco.
- [ ] VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa.
- [ ] VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto.
- [ ] VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff.

## Completion Evidence Matrix (Required Before Delivery Claim)
| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| DOD-02 | Definition of Done | DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| DOD-03 | Definition of Done | DOD-03 — Seleção de canal segue última origem ou único vínculo sem origem; ausência/ambiguidade falha sem fallback, leitura expõe disponibilidade e UI explica bloqueio preservando rascunho. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| DOD-04 | Definition of Done | DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| DOD-05 | Definition of Done | DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; política e finalização não roubam claim concorrente; diferenças de unknown/retirada estão explícitas. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| DOD-06 | Definition of Done | DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| DOD-07 | Definition of Done | DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| DOD-08 | Definition of Done | DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| VAL-01 | Validation Steps | VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo, sem subset como aceite, com API/PG reais e bundle servido fresco. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| VAL-02 | Validation Steps | VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| VAL-03 | Validation Steps | VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| VAL-04 | Validation Steps | VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
| VAL-05 | Validation Steps | VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |

## External Dependency Readiness (Required When External Systems Matter)
| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| runner Docker próprio | regressões completas | unknown | fonte2026-10-20 | find amplo confirmado, não executado | corrigir antes de RED; Node22/PG16/namespace validation |
| vínculos de teste oficial/QR | prova real de resposta | unknown | CP108 histórico2026-10-19 | prova passada não é saúde atual | revalidar runtime/túnel/operador depois de aprovação |
| semântica de erros de provider | evitar falsa recusa | partial | fontes locais2026-10-20 | adapter atual colapsa falhas | classifier conservador D04, sem inferir de string |
| redes futuras | extensibilidade | unknown | nenhuma integração | só fake independente | contratos próprios de identidade/capacidades, sem alegar funcionamento |

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs,react,vite,postgresql,prisma,docker
- **Expected supporting profiles:** strategic-cto,operational-devops,assurance-tester-quality,assurance-security-adversarial
- **Scope-check command:** python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Gate 0:** Genesis rejeitado; contexto canônico existente. Atual strategic-cto documental, sem produto.

### Handoff Log (Update when execution crosses profile boundaries)
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | depois de APROVADO | API/Web/runner/harness | planned |
| operational-coder | operational-devops | readiness/publicação local | imagem própria e recursos de teste | planned |
| operational-coder | assurance-tester-quality | aderência/cutover/TQA/final | pacote público bounded | planned |
| operational-coder | assurance-security-adversarial | isolamento/segredos/DI | resolução e surfaces | planned |

## Complexity
- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section
- **Why this level:** cutover cross-stack de todos senders, auth/identidade e contratos de resultado externo, com mudanças funcionais expressas e regressão real.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** foundation_documentation/modules/integrations-and-channels.md
- **Secondary module docs (if any):** foundation_documentation/modules/inbox-and-conversations.md
- **Planned decision promotion targets (module sections):** Integrations: Channel/resolução/DI/outcomes/extensão; Inbox: seleção/disponibilidade/saída comum e limites.
- **Module decision consolidation targets (required):** mesmos targets com provenance D01..10, retirar descrição de dispatch direto; invariantes de BU/aceitação/segredo preservados.

## Decision Pending (Resolve Before Freeze)
Nenhuma decisão de produto aberta. Assinaturas e semântica material congeladas abaixo para challenge tático; readiness externa continua desconhecida.

## Decisions (Resolved Before Freeze)
- [x] D-01 — Channel é abstract class no domínio, sendMessage recebe {kind:text,recipientRef:string,text:string} e retorna ChannelSendResult discriminado. recipientRef é opaco ao port; sem E164/WABA/phoneNumberId/instância/QR como contrato universal. Limites4096 atuais permanecem nos consumers atuais, não são requisito universal da abstração. ChannelResolver abstrato retorna implementação registrada; seleção por registro explícito, sem if/provider nos senders. Concretos atuais usam clients HTTP; nenhum new no domínio, global useClass único, ModuleRef/service locator ou singleton mutável de BU/token.
- [x] D-02 — Resolução recebe referência de conversa/BU/canal carregada server-side após autorização de sessão ou API key OU referência do ingresso já verificado para Typebot; não aceita declaração de provider/owner/credencial do body. Validar owner BU/Mantenedora do vínculo e identidade corrente, ownNumberVerified/verifiedEpoch/readiness/receipt e envelope atuais usando o owner de credenciais existente. Expor somente binding/proveniência safe para aceitação; tokens/IDs de protocolo ficam privados ao concreto. Resolver atual não autoriza ator e não retorna versão: adequação explícita, sem fingir garantia já existente. Auth por sessão/API key/bot mantém fontes diferentes, nunca exigir usuário humano no bot ou tomar disponibilidade como grant.
- [x] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST, não há rollback externo: rotação no mesmo identity/epoch não invalida recibo conhecido já autorizado; MessageAcceptance conserva fence de identidade/generation/epoch. Retirada/epoch alterado após efeito não rebind/migra conteúdo: erro409 CHANNEL_CONTEXT_CHANGED com outcome ACCEPTED_UNRECORDED se ID conhecido, UNKNOWN se não; sem retry. Janela entre commit local e rede existe e será declarada/testada, sem promessa de fence atômico externo ou operação durável nova.
- [x] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
- [x] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID conserva caminho diagnóstico existente: recordAmbiguousOutbound uma vez por execução,409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, sem Message ENVIADA. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa; consumers seguem outcome/texto, nunca retry automático. Esses dois efeitos locais distintos preservam compatibilidade histórica e ficam explícitos, não dependem do provider no consumer. Sem durabilidade/recuperação de request prometida, sem unir Message nula a eco por heurística; dedupe externo sem ID continua limite, tratado pelo futuro intent ST-CON-04. Typebot interrompe a rodada no erro/bloqueio/incerteza, não reexecuta as saídas automaticamente nem cria sucesso local.
- [x] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), com política extraída sem dependência circular em ConversationsService, executa política/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/publicação. BFF/API pública e Typebot usam o mesmo owner, preservando autoria humana/externa/bot, unread e sender/echo. A atribuição do atendente após ACCEPTED usa condição sobre owner corrente da conversa, não snapshot semDono: claim concorrente é preservado. Status após resposta segue ação atual que move IN_SERVICE (grupo preservado); a resposta aceita após close concorrente é ação posterior e pode reabrir, sem roubar novo owner. Esta ordem é explícita; ST-CON-04 reconverge seu primeiro envio depois. MessageAcceptance e índices não são reimplementados, nenhum schema novo.
- [x] D-07 — Política seleciona exatamente o tipo da última mensagem; se esse vínculo falta, não substitui por primeiro ou outro conectado. Sem última origem: único vínculo pode ser usado; zero bloqueia CANAL_AUSENTE400, múltiplos bloqueiam CANAL_AMBIGUO409. Última origem ausente bloqueia CANAL_SELECIONADO_INDISPONIVEL409. Readiness/janela vêm de requisitos atuais como requiresWindow, não branch de dispatch. disponivel é observação local de seleção/política/trust/conexão/credencial cadastrada, não prova de provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem descriptografar token. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. GET thread não falha por canal ausente: janela conserva exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null quando seleção impossível. Lista pública conserva campos de janela, acrescenta envio_disponivel e motivo_indisponibilidade. Sem rede/mutação provider nos GETs. API pública que já cria conversa antes da resposta mantém essa ordem, inclusive conversa vazia em erro; remover esse efeito é contrato04, não mudança silenciosa.
- [x] D-08 — Extensão é aberta por factories/registro DI tipado, inicialmente dois providers. Fake de teste com recipientRef como user:opaque não telefônico e implementação diferente passa pelo mesmo resolver e consumers, sem modificar branches/interfaces de envio para o fake. Map físico atual enum OFICIAL/NAO_OFICIAL permanece no adapter de binding; teste pode usar mapping de fixture para fake sem alegar persistência de rede nova. Registrar adapter é a extensão do port; identidade/BU/contato/credenciais/ingress de Instagram/Messenger/Telegram exigem contratos futuros. Capacidades específicas terão ports pequenos em05/04 e futuros lifecycle, não métodos no-op/NotImplemented nem casts/concrete instanceof nos consumers. Não implementar runtime de template/capabilities antecipadamente.
- [x] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
- [x] D-10 — UI Inbox consome disponibilidade/motivo, bloqueia composer quando indisponível e mantém rascunho em qualquer erro/UNKNOWN; não anuncia sucesso nem reenvia. Respostas atrasadas em troca BU/conversa seguem fencing monotônico existente. HTTP sucesso e DTOs de mensagem atuais preservados; campos de disponibilidade/outcome são aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts de validação continuam positivos e descartáveis. all completo no namespace leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais prova INOUT assistida dos dois vínculos. Consolidação dos novos owners/limites e rebase05/04 só após gates.

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| constitution#system-invariants | BU/número, domínio backend, superfícies separadas | Preserve | D01/02/08/09 |
| integrations#invariants | providers adapters, erros determinísticos, segredo privado | Preserve | D01/03/04/05 |
| integrations#send-ST-CON-01 | consumer usa credencial scoped/current/receipt | Preserve | novo binding privado, send readiness intacta |
| inbox#aceitação-ST-CON-01 | MessageAcceptance único, identity/gen/epoch, sender/echo | Preserve | D03/06, sem schema |
| inbox#seleção/atribuição | sem troca automática/sem roubar claim | Preserve | corrigir desvio de fallback e snapshot de owner |
| integrations/inbox#projeção-erros | código técnico específico distingue plataformas | Preserve | mapper explícito, outcome aditivo, sem false refusal de UNKNOWN |
| ST-CON-05/04 pending | modelos/primeiro envio em contratos próprios | Preserve | só handoff/reconvergência, sem execução |

## Decision Baseline (Frozen Before Implementation)
- [ ] D-01 — Channel é abstract class no domínio, sendMessage recebe {kind:text,recipientRef:string,text:string} e retorna ChannelSendResult discriminado. recipientRef é opaco ao port; sem E164/WABA/phoneNumberId/instância/QR como contrato universal. Limites4096 atuais permanecem nos consumers atuais, não são requisito universal da abstração. ChannelResolver abstrato retorna implementação registrada; seleção por registro explícito, sem if/provider nos senders. Concretos atuais usam clients HTTP; nenhum new no domínio, global useClass único, ModuleRef/service locator ou singleton mutável de BU/token.
- [ ] D-02 — Resolução recebe referência de conversa/BU/canal carregada server-side após autorização de sessão ou API key OU referência do ingresso já verificado para Typebot; não aceita declaração de provider/owner/credencial do body. Validar owner BU/Mantenedora do vínculo e identidade corrente, ownNumberVerified/verifiedEpoch/readiness/receipt e envelope atuais usando o owner de credenciais existente. Expor somente binding/proveniência safe para aceitação; tokens/IDs de protocolo ficam privados ao concreto. Resolver atual não autoriza ator e não retorna versão: adequação explícita, sem fingir garantia já existente. Auth por sessão/API key/bot mantém fontes diferentes, nunca exigir usuário humano no bot ou tomar disponibilidade como grant.
- [ ] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST, não há rollback externo: rotação no mesmo identity/epoch não invalida recibo conhecido já autorizado; MessageAcceptance conserva fence de identidade/generation/epoch. Retirada/epoch alterado após efeito não rebind/migra conteúdo: erro409 CHANNEL_CONTEXT_CHANGED com outcome ACCEPTED_UNRECORDED se ID conhecido, UNKNOWN se não; sem retry. Janela entre commit local e rede existe e será declarada/testada, sem promessa de fence atômico externo ou operação durável nova.
- [ ] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
- [ ] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID conserva caminho diagnóstico existente: recordAmbiguousOutbound uma vez por execução,409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, sem Message ENVIADA. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa; consumers seguem outcome/texto, nunca retry automático. Esses dois efeitos locais distintos preservam compatibilidade histórica e ficam explícitos, não dependem do provider no consumer. Sem durabilidade/recuperação de request prometida, sem unir Message nula a eco por heurística; dedupe externo sem ID continua limite, tratado pelo futuro intent ST-CON-04. Typebot interrompe a rodada no erro/bloqueio/incerteza, não reexecuta as saídas automaticamente nem cria sucesso local.
- [ ] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), com política extraída sem dependência circular em ConversationsService, executa política/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/publicação. BFF/API pública e Typebot usam o mesmo owner, preservando autoria humana/externa/bot, unread e sender/echo. A atribuição do atendente após ACCEPTED usa condição sobre owner corrente da conversa, não snapshot semDono: claim concorrente é preservado. Status após resposta segue ação atual que move IN_SERVICE (grupo preservado); a resposta aceita após close concorrente é ação posterior e pode reabrir, sem roubar novo owner. Esta ordem é explícita; ST-CON-04 reconverge seu primeiro envio depois. MessageAcceptance e índices não são reimplementados, nenhum schema novo.
- [ ] D-07 — Política seleciona exatamente o tipo da última mensagem; se esse vínculo falta, não substitui por primeiro ou outro conectado. Sem última origem: único vínculo pode ser usado; zero bloqueia CANAL_AUSENTE400, múltiplos bloqueiam CANAL_AMBIGUO409. Última origem ausente bloqueia CANAL_SELECIONADO_INDISPONIVEL409. Readiness/janela vêm de requisitos atuais como requiresWindow, não branch de dispatch. disponivel é observação local de seleção/política/trust/conexão/credencial cadastrada, não prova de provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem descriptografar token. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. GET thread não falha por canal ausente: janela conserva exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null quando seleção impossível. Lista pública conserva campos de janela, acrescenta envio_disponivel e motivo_indisponibilidade. Sem rede/mutação provider nos GETs. API pública que já cria conversa antes da resposta mantém essa ordem, inclusive conversa vazia em erro; remover esse efeito é contrato04, não mudança silenciosa.
- [ ] D-08 — Extensão é aberta por factories/registro DI tipado, inicialmente dois providers. Fake de teste com recipientRef como user:opaque não telefônico e implementação diferente passa pelo mesmo resolver e consumers, sem modificar branches/interfaces de envio para o fake. Map físico atual enum OFICIAL/NAO_OFICIAL permanece no adapter de binding; teste pode usar mapping de fixture para fake sem alegar persistência de rede nova. Registrar adapter é a extensão do port; identidade/BU/contato/credenciais/ingress de Instagram/Messenger/Telegram exigem contratos futuros. Capacidades específicas terão ports pequenos em05/04 e futuros lifecycle, não métodos no-op/NotImplemented nem casts/concrete instanceof nos consumers. Não implementar runtime de template/capabilities antecipadamente.
- [ ] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
- [ ] D-10 — UI Inbox consome disponibilidade/motivo, bloqueia composer quando indisponível e mantém rascunho em qualquer erro/UNKNOWN; não anuncia sucesso nem reenvia. Respostas atrasadas em troca BU/conversa seguem fencing monotônico existente. HTTP sucesso e DTOs de mensagem atuais preservados; campos de disponibilidade/outcome são aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts de validação continuam positivos e descartáveis. all completo no namespace leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais prova INOUT assistida dos dois vínculos. Consolidação dos novos owners/limites e rebase05/04 só após gates.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)
- **Applicability (`required|not_needed`):** required
- **Why this applies:** estabelece port comum e retira dispatch específico duplicado dos negócios.
- **Deviation / debt being retired:** Consumers dependem de dois providers/IDs e mapeiam toda falha como recusa; seleção/atribuição violam intenção canônica.
- **Target steady-state after closeout:** Channel/Resolver de domínio, registro/adapters privados, uma saída comum e aceitação única.
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** nenhum sender comum usa provider client/dispatch antigo; cadastro/protocolo específicos permanecem legítimos e não são compat shim.

### Patterns To Enforce (Required when applicability = `required`)
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| consumidor depende do Channel | D01/08/09 | outbound | extensibilidade verificável |
| contexto privado por operação | D02/03 | resolver/concretos | sem vazamento ou cross-BU |
| aceitação única | ST-CON-01/D06 | todos senders | dedupe/autoria/epoch |

### Prohibited Anti-Patterns (Required when applicability = `required`)
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| adicionar interface e manter branch no sender | dependency harness/AST | falso DIP | none |
| singleton que troca token/BU | barriers concorrentes | cross-tenant | none |
| timeout como recusa ou retry POST | raw HTTP count | efeito externo incerto | none |
| mega-interface com no-op/cast específico | shared contract/fake | quebra substituição/segregação | none |

### Architecture Protection Harness (Required when applicability = `required`)
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| dependency guard/test | api src/domain/channels/transport/channel-dependencies.spec.ts | all + violation fixture | imports/dispatch diretos fora allowlist | implement-in-this-todo | DOD01/06/08 |
| shared contract/PG | api test/channel-transport.e2e-spec.ts | all | substituição/scopes/identity/unknown/echo/claim | implement-in-this-todo | DOD02..06/VAL02 |
| browser real BFF | web e2e/channel-transport.spec.ts | all | disponibilidade/envio/erro/rascunho/freshness | implement-in-this-todo | DOD03/04/06/VAL03 |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)
- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** not_run
- **Decision review evidence / resolution:** pending-freeze; parecer de enquadramento não substitui esta revisão.
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** not_run
- **Adherence review evidence / resolution:** planned after implementation
- **No-go handling:** reconvergir contrato, sem waiver automático.

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Why this decision:** publicar autoridade do contrato antes de review/guard.
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** pending-freeze
- **Baseline push reference:** origin/main
- **Gate status:** not_run
- **Findings summary:** prepared-pre-freeze, não executar lane antes do push terminal.
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Gate: Review Scope Drift
- **Gate decision:** required
- **Why this decision:** aprovação usa o pacote efetivamente revisado.
- **Trigger stage:** after the planning-side review/guard cycle converges and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Material sections compared:** Context|Scope|Out of Scope|Definition of Done|Validation Steps|Decisions|Decision Baseline|Assumptions Preview|Execution Plan|Security Risk Assessment|Performance & Concurrency Risk Assessment
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **No-go handling rule:** reconvergir review/freeze, sem código.
- **Gate status:** not_run
- **Findings summary:** pending-freeze
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Questions To Close
Nenhuma decisão funcional de produto aberta; D01..10 cobrem limites para challenge independente. Readiness real não é aprovação de escopo.

## Pattern References (Optional; Enforced When Cited)
n/a; decisões/canon citados diretamente, sem ID de catálogo presumido.

## Assumptions Preview (Required Before Plan Review)
| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | dois senders comuns escolhem diretamente Meta/Evolution. | api-app/src/domain/inbox/conversations.service.ts; api-app/src/domain/inbox/incoming.service.ts | ampliar inventário/reconvergir | High | Keep as Assumption |
| A-02 | credential resolver não verifica actor grant e não retorna active version. | api-app/src/domain/channels/channel-credential-resolver.ts | reutilizar mecanismo real, sem duplicação | High | Keep as Assumption |
| A-03 | aceitação é owner único keyed e faz fence de identidade. | api-app/src/domain/inbox/message-acceptance.service.ts | corrigir boundary antes de cutover | High | Keep as Assumption |
| A-04 | BFF/API pública respondem pelo ConversationsService; compose DI repetida. | api-app/src/surfaces/bff/conversations.controller.ts; api-app/src/surfaces/public/conversations.controller.ts; api-app/src/surfaces/bff/bff.module.ts | adaptar todos consumers legítimos | High | Keep as Assumption |
| A-05 | browser usa backend real/build e runner faz find amplo. | web-app/playwright.config.ts; scripts/test-channels-local.sh | readiness antes de teste | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)
### Touched Surfaces
Somente Diff Expectation Contract; nenhuma superfície privada/produto modificada durante preparação.

### Ordered Steps
1. APROVADO específico, reload binding e authority/routing go, executor único no checkout principal. Corrigir runner para inventário positivo ANTES de qualquer teste, inclusive RED; não executar find antigo.
2. Test-first: harness dependências com negativa sintética, contrato Channel/fake opaco, raw HTTP/resultados/scopes/seleção. PG barriers e readbacks sobre fixture própria.
3. Ports/concretos/registro/binding privado com credencial owner existente; revalidar contexto e classificar outcomes, sem duplicar aceitação.
4. Orquestração/cutover BFF/Public/Typebot, política/projeção/DTO e UI indisponível/unknown; retirar dispatch antigo e adaptar fakes/DI de suites existentes.
5. CI-equivalent all completo em recursos descartáveis, Playwright real/fonte-servido e pcv. Não testar ambiente humano por conveniência.
6. DevOps revalida runtime/túnel e publica API/Web locais do código aprovado, conservando banco/canais; operador valida INOUT dos dois vínculos próprios. Nenhuma rotação/repareamento automático.
7. Adherence/cutover/security/TQA/final/debt/diff/authority/completion/closeout, módulos e handoff05/04; nenhum push/deploy de produto automático.

### Test Strategy
- **Strategy:** test-first
- **Why:** cutover de side effects externos/auth e substituição real.
- **Fail-first target(s) (when required):** dependency guard, fake opaco, raw unknown, owner/contexto e política seleção/claim.

### Pre-APROVADO RED Evidence Capture (Optional for bugfix/regression)
- **Decision (`required|recommended|not_needed|waived`):** not_needed
- **Why now:** direção nova com diagnóstico por fonte suficiente; sem execução para congelar hipótese.
- **Target symptom:** n/a
- **Allowed surfaces:** none
- **Forbidden surfaces reaffirmed:** production code|runtime/config/deploy|canonical project docs outside TODO authoring
- **Planned command / target:** n/a
- **Status (`not_run|running|red_reproduced|red_not_reproduced|blocked|waived`):** not_run
- **Findings summary:** nenhuma execução de produto/testes atual.

### Flow Evidence Planning Matrix (Required Before `APROVADO`)
| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD01/02 substituição/scope | refactor/auth/context | web-only | API PG + browser mutation | yes | yes | channel-transport.e2e/spec e shared contracts | n/a |
| DOD03/04 disponibilidade/outcome | DTO/composer/persistência | web-only | Playwright mutation | yes | yes | e2e/channel-transport.spec.ts com BFF real | n/a |
| DOD05/06 + VAL01/02/03 | aceitação/claim/echo/cutover | web-only | PG barriers + browser mutation | yes | yes | suites completas e served freshness | n/a |
| DOD07/VAL04 | recursos verdadeiros | web-only | operador local | yes | yes | receipt redigido de INOUT dos dois vínculos | fake não substitui |
| DOD08/VAL05 | consolidação/qualidade | web-only | audits + provas anteriores | yes | yes | pacote/guards por critério | n/a |

### Local CI-Equivalent Suite Matrix (Required Before `APROVADO` and Before Delivery Claim)
Colunas Status duplicadas projetam o mesmo fato para leitores determinísticos de índices distintos; evidence inclui ressalvas.

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status (completion projection) | Evidence Artifact / Command | Status (authority projection) | Notes | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| api / all PG/units/contracts | cutover/DI/auth/HTTP | bash scripts/test-channels-local.sh all | Local-Implemented | planned | npm ci/lint/build/unit/E2E completos + migration deploy/status de baseline | planned | subset só diagnóstico | Channel contract/opaque fake/unknown/scope/current identity/echo/claim | Node22/PG16 próprios; dois tenants/BUs; api-key e actor humano/bot; lease barriers/provider controlado |
| web / all build/unit/browser | DTO/composer/erro | bash scripts/test-channels-local.sh all | Local-Implemented | planned | spec channel-transport e regressões completas, BFF não mockado | planned | mesmo all | positivo ambos, canal ausente/ambíguo, draft unknown e contexto atrasado | Web4173/API3100/provider3101, mesma DB/resolução da CI, bundle fresco |
| root / runner topology | positive inventory | bash scripts/test-channels-local.sh all | Local-Implemented | planned | manifests/masks fictícios; nenhuma leitura dotenv/.local-files | planned | sem namespace humano | safe mount/config e origem da principal | leadshug_channels_validation inexistente antes do run, dados descartáveis |

### Runtime / Rollout Notes
Sem migration nova/schema/enum. Migrations existentes deploy/status em PG descartável fazem parte de all. Namespace validation exclusivo, bundles/builds da principal. Runtime humano somente publicação local planejada e prova assistida depois de readiness; banco/canais preservados, sem reset ou rotação. Nenhum transporte real futuro ou status externo de entrega presumido.

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
  - **Severity:** high
  - **Evidence:** conversations.service.ts:300; incoming.service.ts:94; resolver:24 não autoriza ator.
  - **Why it matters now:** falsa abstração ou singleton de token mantém acoplamento/vaza escopo.
  - **Option A (Recommended):** ports de domínio, contexto por operação, registro explícito e auth trusted-scoped.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** cross-module; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** wrapper com switch no próprio consumer e config global.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** manter providers atuais; **Effort:** low; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** regresses.
  - **Recommendation:** A; direção humana expressa e menor mecanismo fiel ao escopo.
- **Issue ID:** PLAN-02
  - **Severity:** high
  - **Evidence:** clients atuais string/null e generic errors, fallback canais[0].
  - **Why it matters now:** contrato de substituição precisa outcomes e política verdadeiros, não apenas nomes iguais.
  - **Option A (Recommended):** D03..07 com UNKNOWN conservador, projeção compatível e seleção explícita.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** cross-stack; **Maintenance burden:** medium; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** ocultar falhas como recusa e trocar canal para enviar.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-stack; **Maintenance burden:** high; **Performance impact:** regresses; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** adiar o cutover; **Effort:** low; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** A; sem plataforma de operação durável antecipada.

### Failure Modes & Edge Cases
- [ ] BUs concorrentes, actor sem grant, bot de tenant alheio, owner de canal divergente e stale epoch/version.
- [ ] selected channel removido, dois vínculos sem última origem, leitura segura sem envio habilitado e draft preservado.
- [ ] POST efeito seguido de timeout/5xx/malformed, ID ausente e receipt tardio após rotação/retirada.
- [ ] eco antes/depois do sender, claim concorrente e close anterior ao resultado: outcomes/persistência conforme D03/06.
- [ ] UI troca A→B→A durante erro/envio; nenhum retry ou limpeza de draft de outra conversa.

### Residual Unknowns / Risks
- [ ] Cutover sem intent durável conserva limite de crash antes da aceitação/publicação e diagnósticos null-ID sem dedupe; ST-CON-04 deve reconvergir esse limite, não inferir exactly-once.
- [ ] Port extensível não significa persistência/contato/ingress de rede nova pronto; fake só prova substituição interna.
- [ ] Readiness real e medições só depois de aprovação; coorte privada continua, sem produção/usuário não confiável liberado.
- [ ] Pacote prepared-pre-freeze; reviews/guardas próprios ainda não executados.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)
- **Needed:** no
- **Why ambiguity remains:** diagnóstico teve parecer independente de enquadramento; agora gate architecture_opinion desafia D01..10, sem tratá-lo como duplicado satisfeito.
- **Opinion count:** 1 framing only,0 tactical
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required na gate tática
- **Required lenses:** correctness,performance,elegance,structural-soundness,operational-fit

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)
- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Latest TEACH evidence / artifact:** pending-freeze

| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | cutover completo do envio comum |
| blast_radius | cross-stack | API/Web/runner |
| behavioral_change_or_bugfix | yes | política/erros/claim explícitos |
| changes_public_contract | yes | campos aditivos/erro honesto |
| touches_auth_or_tenant | yes | resolver e contexto |
| touches_runtime_or_infra | yes | runner/publicação local |
| touches_tests | yes | harness/suites |
| critical_user_journey | yes | respostas reais |
| release_or_promotion_critical | no | só local |
| high_severity_plan_review_issue | yes | PLAN01/02 |
| explicit_three_lane_request | no | floor derivado |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)
- **Critique decision:** required
- **Why this decision:** big/cross-stack/auth/side effect e cutover arquitetural.
- **Impact signals in scope:** public contract/schema/api|auth|runtime
- **Package mode:** bounded-file-set
- **Package minimum contents:** TODO publicado, fontes públicas exatas, parecer/disposição e matrizes/risco.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required, não executor; aguardar terminal sem prazo rígido.
- **Critique lenses:** correctness,performance,elegance,structural-soundness,risk
- **Critique status:** not_run
- **Findings summary:** pending-freeze
- **Resolution ledger:** nenhuma revisão tática executada
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Gate: Assumption Code Coherence
- **Gate decision:** required
- **Why this decision:** premissas concretas de senders/resolver/aceitação/runtime.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A01..05
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Gate status:** not_run
- **Findings summary:** pending-freeze
- **Evidence / reference:** pending-freeze
- **Waiver authority / reference (required if waived):** n/a

## Approval
- **Approved by:** pending
- **Approval reference:** pending
- **Approval scope:** ST-CON-06/SCOPE01..05/D01..10, depois da convergência do pacote concreto; concordância com conceito não substitui APROVADO.
- **Execution not authorized by approval:** todo Out of Scope, redes futuras,05/04, push/deploy de produto ou mudanças privadas.
- **Renewed approval required when:** decisões/DoD/paths/risco/contrato mudarem materialmente.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)
Ingestão de planejamento; reload binding obrigatório após APROVADO antes de produto. Registro de regra/template não é evidência de execução.

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
- **Subagent / delegation authorization:** AGENTS/main instructions/workflows exigem reviews internos e executor; código só após APROVADO.
- **Execution topology:** primary-checkout-single-writer
- **Worktree / auxiliary-checkout authorization:** not-authorized
- **Worktree authorization evidence:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** pending
- **Waiver / exception reference:** n/a

Reviewers architecture_opinion e critique: gpt-6.1-sol/max, fresh fork_turns none, routing go distinto antes de dispatch. Primário não se declara outro modelo. Nenhum GOAL persistente criado sem pedido humano.

## Decision Adherence Validation (Mandatory Before Delivery)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Pipeline/Copilot P1/P2 Preflight
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Rule-Spirit Anti-Pattern Hunt
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## TODO Closeout Disposition
- **Disposition:** keep-active
- **Disposition reason:** preparação e reviews pré-aprovação.
- **Post-commit/push status:** pending-freeze
- **Next path/status action:** apresentar contrato convergido para APROVADO; não há entrega de produto.

## Security Risk Assessment (Mandatory Before Delivery)
- **Risk level:** high
- **Why this risk level:** canal/credencial de múltiplos tenants e side effect externo.
- **Attack surface in scope:** sessão/key/bot, BU/channel/contexto, singleton/mapping forjado, rawerro/token, adapter recipient/URL e DI.
- **Attack simulation decision:** required
- **Review evidence:** planned após implementação, com actor sem grant/BU alheia/ingress falso/version stale e concorrência.
- **Residual security risk:** coorte privada atual preservada; nenhum usuário não confiável ou produção autorizado.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)
- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** cutover de envio/identidade/aceitação/DI com concorrência real.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | pending | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | pending | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-E3 | pending | external ambiguity explicit | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E1 | pending | none | none |

### Lane Detail Packet Template
#### EPS
- **Trigger rationale:** medir seleção/resolução scoped e projections de disponibilidade; EXPLAIN ANALYZE e cardinalidade representativa. Nenhuma chamada externa nova em GET e um POST por dispatch.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
- **Evidence object:** pending; JSON pcv-1 com sha256 antes da entrega, não existe execução ainda.
#### FRC
- **Trigger rationale:** envio/erro e troca BU/conversa; draft, requests e readback BFF real.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### BCI
- **Trigger rationale:** barreiras PG/contador HTTP de BUs/credencial/identidade/claim/eco; provar D02..07 e ausência de retry. Crash recovery durável novo não é contratado.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### RLS
- **Trigger rationale:** ensaio bounded de concorrência no envio fake/PG, sem claim SLO/produção.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
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
- **Cutover audit decision:** required
- **Why this decision:** migra todos senders comuns para owner/port canônicos e elimina dispatch antigo, mantendo protocolos legítimos separados.
- **Cutover signals in scope:** intentional canonical boundary change|shared dispatch replacement
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** audit-protocol-triple-review
- **Cutover audit status:** not_run
- **Findings summary:** planned after implementation
- **Evidence / reference:** harness D09 e módulos/sources consolidados, sem shim temporário
- **Waiver authority / reference (required if waived):** n/a

## Delivery Confidence Gate (Required for `✅ Production-Ready`)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Module Consolidation Gate (Required Before `Completed`)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Commands (Run Locally)
Guardas de planejamento após freeze. Produto somente após APROVADO: bash scripts/test-channels-local.sh all, depois do boundary positivo. Nenhum teste/runtime/account call nesta preparação.

## Files Expected (Compatibility Note)
Diff Expectation Contract governa os paths, sem autorização de mudanças além dele.

## COMENTÁRIO:
Nenhuma pergunta de produto material pendente.


## Producer / Consumer Contract Matrix

| Producer | Consumers | Auth / fields | Planned effect / constraint |
| --- | --- | --- | --- |
| Channel.sendMessage internal | OutboundService | opaque recipientRef/text; operation-bound implementation, no raw token | normalized result D04; one external POST, no retry, no DB message write by adapter |
| ChannelResolver internal | OutboundService/policy | trusted reference derived from authorized session/API-key conversation or verified bot ingress; owner DB rechecked | Channel plus safe storage-provenance binding; no caller provider selection/secret |
| GET /api/bff/conversations/:id/messages | Inbox | existing session/BU lookup, timeline fields unchanged; janela adds disponivel/motivo | observational availability, no external calls/secret decrypt; unavailable composer with fixed reason |
| POST /api/bff/conversations/:id/messages | Inbox | existing session/CSRF/ATENDENTE+ and {texto}; success201 existing {id,canal,em} | shared outbound; D05 errors additive outcome, honest text; preserve draft and no auto resend |
| GET /api/v1/conversations | public API clients | existing partner key scope; existing fields, adds envio_disponivel/motivo_indisponibilidade | existing window values remain, unavailable selection returns false/null rather than failing whole list |
| GET /api/v1/conversations/:telefone/messages | public API client | existing partner key/BU and phone conversation lookup; timeline/window fields unchanged | disponibilidade aditiva como listagem, sem provider GET/segredo |
| POST /api/v1/messages | public API client | existing API key/account_id, telefone/texto/atendente and rate limit | request shape/success unchanged; same shared outbound, source authorization and EXTERNO authorship; D05 error mapping |
| IncomingService Typebot text response | existing bot sessions | already accepted ingress/tenant/bot ownership, no fabricated human user | same shared outbound/result/acceptance; no human assignment, stop on unknown/block/refusal, no automatic replay |

**Fixed availability reasons:** CANAL_AUSENTE, CANAL_AMBIGUO, CANAL_SELECIONADO_INDISPONIVEL, CHANNEL_IDENTITY_NOT_VERIFIED, CHANNEL_NOT_READY, PENDING_CREDENTIAL, JANELA_FECHADA; null when observed available. Availability never grants authority or guarantees external delivery. Existing input limit4096/request phone normalization stays at current product boundaries; the Channel port has no universal WhatsApp address requirement. No new public route or channel choice field is introduced in06.

## Planning references / provenance

Direction and extension requirements are explicit user statements2026-10-20. Initial framing opinion is artifacts/analysis/leadshug-channel-abstraction-framing-opinion-20261020.md (advisory only). Primary conceptual sources: NestJS custom providers https://docs.nestjs.com/fundamentals/custom-providers and Liskov/Wing1994 https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf, previously consulted. Provider error source to recheck before tactical review: https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes/. Local code proves current behavior, not future platform integration or live readiness.
