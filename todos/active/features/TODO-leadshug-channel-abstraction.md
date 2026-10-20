# Tactical TODO — ST-CON-06

## Title
LeadsHug — ST-CON-06: Channel abstrato extensível e cutover do envio comum

## Artifact Identity
- **Artifact type:** tactical_execution_contract
- **Status:** InProgress
- **Version:** 1.3
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
- **Next exact step:** Reconvergir planejamento v1.3 com freeze publicado, arquitetura/crítica e guards; solicitar renovação humana para o índice específico e CI admission. Somente a correção já autorizada v1.2 de selected-window e leitura por conversa termina em paralelo; nenhum Prisma/CI/runtime antes de nova aprovação.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** review
- **Why this state now:** v1.2 e os dois companions foram aprovados; PERF-01/CIADM-01 exigem renovação material v1.3. Revisão do contrato ampliado, sem autoridade implícita para índice/CI. O checkpoint selected-window/per-conversation já autorizado v1.2 pode terminar antes do freeze de código.
- **Exit condition:** implementação aderente com all/assurance/pcv e prova real pós-publicação local; nenhum bloqueador de review aberto antes de entrega.

## Scope
- [ ] SCOPE-01 — Channel/ChannelResolver abstratos de domínio, registro explícito e instâncias por operação, concretos oficial/não oficial e extensão verificada com fake não WhatsApp.
- [ ] SCOPE-02 — Migrar envios de Conversa BFF/API pública e respostas Typebot para a mesma orquestração, mantendo autenticações próprias, política e MessageAcceptanceService único.
- [ ] SCOPE-03 — Contexto autorizado e owner BU/canal, segredos privados, credencial/identidade correntes e fences explícitos; nenhuma troca silenciosa do canal selecionado.
- [ ] SCOPE-04 — Outcomes tipados verdadeiros, projeção pública explícita de erro/disponibilidade e UI honesta; sem retry externo automático ou garantia de exactly-once.
- [ ] SCOPE-05 — Runner de inventário positivo antes de testes, harness durável de imports/contrato/PG/Playwright, regressões completas e prova real assistida nos dois vínculos próprios; consolidação/revisões de entrega.

- [ ] SCOPE-06 — Corrigir PERF-01 com um único índice Prisma-managed de Message e seleção de referências que realmente exigem janela; admitir a família PG/browser no CI pelo mesmo runner/lifecycle, com guard fail-closed de paridade e replay local isolado. Escopo exato: artifacts/reviews/leadshug-channel-abstraction-20261020/scope-renewal-v1.3-proposal.md; pendente APROVADO v1.3.

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
- [ ] Instagram/Messenger/Telegram reais, alteração de identidade/BU/contato/schema ou enums de persistência para novas redes (única exceção: índice Message nomeado em D07, sem campo/tabela/enum novo); fake não prova integração real.
- [ ] Criação/envio de templates, Nova conversa manual/novo intent, importação, campanhas, anexos ou novos fluxos Typebot; ST-CON-05/04 permanecem separados.
- [ ] Reescrever OAuth/QR/cadastro/lifecycle, rotacionar credenciais, desconectar vínculos ou criar sondagem externa por envio.
- [ ] Worker/outbox/fila, durable intent/exactly-once externo, retry automático de POST, heurística para unir eco sem ID.
- [ ] Delphi, worktrees/cópias, gitlinks/.gitmodules, deploy/push de produto, leitura de .env/.env.testing e qualquer read/list/stat/hash/traversal/mount/stage api-app/.local-files.

## Diff Expectation Contract
Required before delivery. Heading normalized for canonical parser; contract obligation unchanged.
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
| api | test/channel-transport* | A, ?? | PG/contrato/corridas |
| api | test/helpers.ts | M | fakes/DI de contrato |
| api | test/timeline-fixtures.cjs | M | provider controlado de browser |
| api | test/browser-server.cjs | M | bootstrap real |
| api | test/*.e2e-spec.ts | M | suites consumidoras da interface alterada, sem afrouxar assertivas |
| api | src/domain/inbox/*.spec.ts | M | consumo abstrato e regressões |
| web | src/api.ts | M | DTO aditivo disponibilidade |
| web | src/api.spec.ts | M | companion de metadados seguros D10; admissão humana2026-10-20 |
| web | src/telas/Inbox.tsx | M | composer indisponível/motivo e erro |
| web | src/telas/Inbox*.test.tsx | any | render/estado |
| web | e2e/channel-transport* | A, ?? | mutation BFF real |
| web | e2e/number-onboarding-freshness.ts | M | manifesto se afetado |
| web | e2e/timeline-freshness.ts | M | companion chamado antes do manifesto; pathspec positivo antes de discovery; admissão humana2026-10-20 |
| root | scripts/test-channels-local.sh | M | inventário positivo e único lifecycle Windows/local + Linux/CI, somente após renovação v1.3 |
| root | .github/workflows/ci.yml | M | admissão PG/browser PR não-main isolada, jobs existentes preservados; v1.3 pendente |
| root | scripts/check-channels-ci-parity.py | A, ?? | guard fail-closed YAML/lifecycle + controles negativos; v1.3 pendente |
| api | prisma/schema.prisma | M | somente índice messages_conversation_direction_created_id_idx; v1.3 pendente |
| api | prisma/migrations/20261020170000_message_inbound_window_index/migration.sql | A, ?? | somente CREATE INDEX sobre campos existentes; v1.3 pendente |
| foundation | todos/active/features/TODO-leadshug-channel-abstraction.md | A, M | governança/evidências |
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
| root | .env* | any | privado |
| root | .gitmodules | any | pipeline-owned |
| root | api-app | any | gitlink pipeline-owned |
| root | web-app | any | gitlink pipeline-owned |
| root | delphi-ai | any | sem self-improvement |
| web | dist/** | any | gerado, não fonte |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
Guard público preliminar executado com fonte canônica inalterada e invocações Git limitadas ANTES da descoberta por pathspecs positivos (API/Web/root); não é guard final de entrega ou prova dos paths excluídos. Primeiro título com sufixo não foi reconhecido pelo parser; normalizado sem alterar obrigação. A segunda execução encontrou 88 mudanças públicas,85 esperadas e3 diferenças mecânicas de tipo, zero path proibido ou novo path fora do escopo.

| Finding | Classification | Resolution / authority |
| --- | --- | --- |
| api:test/channel-transport.e2e-spec.ts aparece ?? e já era adição A aprovada | noise; by-design/no-action in product | Comparação working_tree inclui arquivo ainda não staged; adicionar ?? ao mesmo glob já aprovado representa a mesma adição, não amplia paths nem produto; não stagear fonte por conveniência do guard |
| web:e2e/channel-transport.spec.ts aparece ?? e já era adição A aprovada | noise; by-design/no-action in product | Mesmo ajuste mecânico A,?? no mesmo glob aprovado, sem mudar cobertura ou permissão funcional |
| Foundation TODO aparece A contra baseline82fa66b e constava só M | noise; by-design/no-action in product | O contrato foi criado depois da baseline, portanto A,M expressa a criação/modificação documental já autorizada; nenhum novo artefato/escopo |

Evidência histórica: evidence/public-diff-working-tree-type-no-go.json. Ajuste de representação Git não muda Scope/DoD/decisões/risco/paths e não exige nova aprovação material; as duas admissões de paths reais permanecem validadas separadamente pelo usuário. Descoberta de path real não aprovado continua bloqueada e exige validação humana. Rerun preliminar e final ainda necessários.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** DI, DTO/fixture/componente subordinados ao mesmo envio comum e preservação de seus invariantes.
- **Must update or split the TODO:** schema/novo provedor/capacidade real, template/intent novo, mudança de política fora das decisões e novos endpoints.

## Definition of Done
- [ ] DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real.
- [ ] DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes.
- [ ] DOD-03 — Seleção humana/pública segue última origem determinística ou único vínculo; bot fica no ingresso verificado; policy/janela comuns, ausência/ambiguidade sem fallback e disponibilidade/UI honestas preservam rascunho.
- [ ] DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout.
- [ ] DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; finalização pública/humana não rouba claim e bot conserva fila/owner; falhas locais pós-ACK e unknown estão explícitas.
- [ ] DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot; índice latest-IN e referências selected-window têm prova OUT-heavy/no-IN, família CI PG/browser compartilha all/lifecycle/guard e topologia Linux isolada validada, sem claim de execução remota.
- [ ] DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede.
- [ ] DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção.

## Validation Steps
- [ ] VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo e admissão de paridade/invalidating drift, sem subset como aceite, com API/PG reais, migration/index latest-IN e bundle servido fresco; replay isolado do transporte Linux obrigatório para validar a topologia CI.
- [ ] VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco.
- [ ] VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa.
- [ ] VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto.
- [ ] VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff.

## Completion Evidence Matrix (Required Before Delivery Claim)
| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real. | canonical tests / source / review | channel-dependencies.spec synthetic negative; independent opaque Channel via real resolver/BFF/PG in channel-transport.e2e; ChannelTransportModule composition; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | No real future network claimed; current storage provenance preserved |
| DOD-02 | Definition of Done | DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes. | canonical tests / source / review | channel-transport.e2e denied session/CSRF/key, crossBU/ingress, simultaneous twoTENANT token/resource/localMessage probes; actualMeta/Evo fence omission failures then restored; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Scoped immutable operation context; local-check-to-network interval remains |
| DOD-03 | Definition of Done | DOD-03 — Seleção humana/pública segue última origem determinística ou único vínculo; bot fica no ingresso verificado; policy/janela comuns, ausência/ambiguidade sem fallback e disponibilidade/UI honestas preservam rascunho. | canonical tests / source / review | channel-transport.e2e origin tie/sole/absent/multi/ingress pinning; Typebot window expiry; channel-transport browser unavailable/unknown/A-B-A and FRC5x20; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Source/served hash attestation80903; no blind fallback or retry |
| DOD-04 | Definition of Done | DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout. | canonical tests / source / review | meta.client.spec/evolution.client.spec complete raw envelopes and onePOST; outbound.service.spec local incomplete; PG contradictory200 persistednothing; browserunknown draft; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | R01/R03/R05 counterexamples fixed; ACCEPTED is acknowledgement, not handset delivery |
| DOD-05 | Definition of Done | DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; finalização pública/humana não rouba claim e bot conserva fila/owner; falhas locais pós-ACK e unknown estão explícitas. | canonical tests / source / review | api-publica.e2e public/echo provenance; channel-transport.e2e claim/public-BFF overlap; number-onboarding-typebot.e2e pinned reply/queue/echo; unchanged keyedAcceptance owner hash; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Same Message writer, captured-key readback only; crash/nullID dedupe limits preserved |
| DOD-06 | Definition of Done | DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot; índice latest-IN e referências selected-window têm prova OUT-heavy/no-IN, família CI PG/browser compartilha all/lifecycle/guard e topologia Linux isolada validada, sem claim de execução remota. | canonical tests / source / review | evidence/runner-checkpoint.json before RED; canonical all80903 terminal0 194unit+309PG+29Web+50browser; rawlog778f8589; source/served/dist bundle27c5db46; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | pending | One frozen principal checkout; realPG/Chromium, provider boundaries controlled; run80903 histórico; v1.3 índice/paridade/novos testes ainda pendentes |
| DOD-07 | Definition of Done | DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede. | runtime / audit | New image/runtime attestation and assisted IN/OUT official+unofficial receipt not yet collected; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | Requires localactivation/newHTTPS/operator; CP108 and fixtures do not substitute |
| DOD-08 | Definition of Done | DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção. | runtime / audit | Dedicated audit session active; PCV candidates measured; final review/modules/guards/closeout and05/04handoff pending; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | No Local-Implemented or production/promotion claim |
| VAL-01 | Validation Steps | VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo e admissão de paridade/invalidating drift, sem subset como aceite, com API/PG reais, migration/index latest-IN e bundle servido fresco; replay isolado do transporte Linux obrigatório para validar a topologia CI. | canonical tests / source / review | bash scripts/test-channels-local.sh all; run80903 exit0, exact sourceafter/36changedsource manifest matches and served/dist/preserved JS match; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | pending | Node22.23.3, PostgreSQL16; run80903 histórico; admissão/replay Linux e finalall v1.3 pendentes |
| VAL-02 | Validation Steps | VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco. | canonical tests / source / review | RawMeta/Evo HTTP unit; channel-transport realPG auth/factory/generation/version/key/claim; bot/public/acceptance suites in all80903; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Fake opaque recipient proves internal substitution; shipping adapters omitted-guard mutants detect regressions |
| VAL-03 | Validation Steps | VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa. | canonical tests / source / review | web-app/e2e/channel-transport.spec.ts in browser50/50 all80903; real BFF/PG, nativebody/task barrier; guardmutant30246 expected draftempty failure49/50; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Exact browserfixture source hashes andserved publicbundle attested; no production test route or DTOhook |
| VAL-04 | Validation Steps | VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto. | runtime / audit | Pending API/Web activation, newHTTPS and operator IN/OUT on both existingbindings; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | No channelreregistration/secretrotation/dbreset authorized |
| VAL-05 | Validation Steps | VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff. | runtime / audit | IndependentPerformance/TQA/Cutover running; sourcepublicdiff171expected/0forbidden/0unclassified; finalreview/consolidation/guards remain; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | Current source stable; no audit waivers or new sibling implementation |

## External Dependency Readiness (Required When External Systems Matter)
| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| runner Docker próprio | regressões completas | ready | 2026-10-20 all80903 | positive bind inventory beforetests,194/309/29/50passed; source/served proof | Node22.23.3/PG16 disposable; privatehostinputs excluded |
| vínculos de teste oficial/QR | prova real de resposta | unknown | CP108 histórico2026-10-19 | prova passada não é saúde atual | revalidar runtime/túnel/operador depois de aprovação |
| semântica de erros de provider | evitar falsa recusa | partial | fontes locais2026-10-20 | adapter atual colapsa falhas | classifier conservador D04, sem inferir de string |
| redes futuras | extensibilidade | unknown | nenhuma integração | só fake independente | contratos próprios de identidade/capacidades, sem alegar funcionamento |

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs,react,vite,postgresql,prisma,docker
- **Expected supporting profiles:** strategic-cto,operational-devops,assurance-tester-quality,assurance-security-adversarial
- **Scope-check command:** python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Gate 0:** Genesis rejeitado; contexto canônico existente. Genesis rejeitado pelo canon existente; ativo operational-coder com handoffs DevOps/assurance planejados.

### Handoff Log (Update when execution crosses profile boundaries)
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | APROVADO explícito recebido2026-10-20 | API/Web/runner/harness | active; binding reload + authority-execution.json |
| operational-coder | operational-devops | readiness/publicação local | imagem própria e recursos de teste | planned |
| operational-coder | assurance-tester-quality | aderência/cutover/TQA/final | pacote público bounded | active; dedicated-audit/session.json, round01; primary80903passed |
| operational-coder | assurance-security-adversarial | isolamento/segredos/DI | resolução e surfaces | rounds1/2/3 terminal; findings integrated, R02 proof/finalTQA pending |

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
- [x] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST não há rollback externo: somente mudança de credentialVersion com identidade/generation/epoch TODOS inalterados permite aceitar o recibo capturado. REAUTORIZAR real incrementa generation, mesmo no mesmo recurso; não substituir a generation antiga. Mudança de identidade/generation/epoch depois do efeito não rebind/migra conteúdo:409 CHANNEL_CONTEXT_CHANGED; ACK conhecido conserva outcome ACCEPTED_LOCAL_INCOMPLETE e localMessageState RECORDED ou UNCONFIRMED conforme D05; sem ID, UNKNOWN. MessageAcceptance conserva seu fence. Testar REAUTORIZAR real concorrente e version-only separadamente. Janela entre leitura/CAS local e rede existe, sem fence atômico externo ou nova operação durável.
- [x] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
- [x] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID tenta recordAmbiguousOutbound uma vez por execução: somente commit confirmado permite409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, diagnóstico FALHOU/null-ID, nunca Message ENVIADA. Precedência: mudança detectada de identidade/generation/epoch após dispatch sem ID, inclusive antes ou durante o fence de recordAmbiguousOutbound, devolve409 CHANNEL_CONTEXT_CHANGED/outcome UNKNOWN; não rebind nem grava diagnóstico sob contexto novo. Somente OUTRAS falhas/commit incerto do diagnóstico devolvem503 OUTBOUND_LOCAL_INCOMPLETE/outcome UNKNOWN/evidence ACK_WITHOUT_ID/diagnosticPersistence UNCONFIRMED, sem afirmar diagnóstico gravado; no409 só declarar diagnóstico gravado com evidência positiva do commit capturado, senão UNCONFIRMED. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa. ACK externo válido seguido de QUALQUER falha local de aceitação/reconciliação/finalização conserva outcome ACCEPTED_LOCAL_INCOMPLETE;409 CHANNEL_CONTEXT_CHANGED se fence alterado, senão503 OUTBOUND_LOCAL_INCOMPLETE. Texto fixo O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente. localMessageState RECORDED somente com commit de Message confirmado ou readback positivo pelo owner/chave/proveniência capturados; nos demais casos UNCONFIRMED, inclusive rollback local confirmado pois eco pode ter gravado em paralelo. No máximo um readback local bounded, sem rebind ou nova chamada externa. Falha após Message commit mantém RECORDED mesmo se atribuição/status falhar; nenhum erro local vira recusa externa. Propagação transient do recibo não cria intent/outbox/schema/segundo owner. UI preserva draft e nunca reenvia automaticamente; Typebot interrompe a rodada, sem replay de saídas. Sem durabilidade/recuperação prometida nem união heurística de Message nula ao eco; dedupe sem ID continua limite para ST-CON-04.
- [x] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), política extraída sem ciclo DI com ConversationsService, executa policy/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/autoria/publicação. Input trusted distingue BFF humano, API EXTERNO com snapshot e bot; autoria/intenção de atribuição entram ANTES do dispatch. Remover message.update e conversation.update de conclusão no controller público; não limpar autoria comprovada no sender/echo. Para respostas humanas/públicas, atribuição após ACCEPTED é condicional sobre owner corrente, nunca snapshot semDono: claim concorrente é preservado, inclusive público vs claim humano e overlap BFF/público. Status humano/público move IN_SERVICE (grupo preservado); resposta aceita após close concorrente pode reabrir sem roubar novo owner. Bot conserva autoria/unread/status de fila/owner humano e não executa essa finalização humana. Toda falha local pós-ACK segue D05 mesmo após Message commit. MessageAcceptance, índices existentes e unique keys preservados; única extensão de schema é o índice D07 nomeado para seek latest-IN, sem campo/tabela/enum novo;04 reconverge primeiro envio depois.
- [x] D-07 — Seleção para resposta BFF/API pública usa última mensagem por createdAt DESC,id DESC (ordenação DB, mesma timeline); se seu vínculo falta, nunca substitui por primeiro/outro conectado. Sem última origem: único vínculo pode ser usado; zero CANAL_AUSENTE400, múltiplos CANAL_AMBIGUO409. Origem sem vínculo CANAL_SELECIONADO_INDISPONIVEL409. Bot usa exclusivamente channelId/identidade do ingresso aceito/verificado, mesmo se outra entrada mais recente vier por outro transporte; sem fallback/rebind. Policy comum avalia readiness e requiresWindow do binding selecionado para TODOS, inclusive bot: corrigir explicitamente bypass atual do Typebot. Reavaliar janela antes de cada texto do bot; expiração bloqueia zeroPOST e interrompe rodada, sem replay. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. disponivel observa localmente seleção/policy/trust/conexão/credencial cadastrada, não prova provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem token/rede/mutação; reutilizar metadados da BU na lista, sem novo fan-out por conversa, medir EPS. Projetar latest-IN somente para referências cujo binding selecionado requiresWindow; um índice Prisma-managed @@index([conversationId,direction,createdAt,id], map: messages_conversation_direction_created_id_idx) suporta seek ordenado por conversa/direção, inclusive OUT-heavy/no-IN, com prova PG de loops/filtros/buffers em profundidades crescentes. Preservar timestamp expirado do histórico inteiro e ausência de filtro de transporte; não substituir por predicado de últimas24h. GET thread não falha por canal ausente: janela mantém exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null se seleção impossível. Lista pública mantém campos e acrescenta envio_disponivel/motivo_indisponibilidade. API pública mantém criação prévia da conversa, inclusive vazia em erro; mudar isso é contrato04.
- [x] D-08 — Extensão aberta por factories/registro DI tipado, inicialmente dois providers. Fake com recipientRef user:opaque não telefônico passa pelo mesmo resolver/owner/BFF com conversa seeded e bot/internal fixtures, sem alterar branches/interfaces dos senders. Regressão pública conserva telefone numérico/normalização atual; não exigir handle Telegram no POST /api/v1/messages. Enum físico OFICIAL/NAO_OFICIAL permanece no adapter de binding; fixture pode mapear slot existente ao fake, sem flag de produto nem alegar rede nova persistida. Registrar adapter estende o port; identidade/BU/contato/credenciais/ingress de redes futuras exigem contratos próprios. Capacidades terão ports pequenos em05/04 e lifecycle futuro, sem no-op/NotImplemented/casts/concrete instanceof nos consumers; não implementar runtime antecipado.
- [x] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
- [x] D-10 — UI Inbox e ErroDaApi em api.ts preservam outcome e metadados safe de incerteza do backend, exibem texto fixo honesto, bloqueiam composer por disponibilidade/motivo e mantêm draft em qualquer erro/UNKNOWN/ACCEPTED_LOCAL_INCOMPLETE; sem sucesso ou retry automático. Respostas atrasadas em troca BU/conversa conservam fencing monotônico atual. HTTP sucesso/DTOs de mensagem preservados; disponibilidade/outcome aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts positivos/descartáveis. all completo em leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais INOUT assistida dos dois vínculos. Admitir o mesmo all/lifecycle no job CI PR não-main por seleção explícita de transporte Linux; default local Windows preservado. Guard scripts/check-channels-ci-parity.py parseia YAML de forma segura, rejeita bypass/alias/duplicatas e divergência de suite/ordem/bootstrap/cleanup; controles negativos reais. Provar topologia executável Linux isolada, não só YAML; execução remota fica not_run até publicação de fonte autorizada. Consolidar owners/limites e rebase05/04 só após gates.

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
- [ ] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST não há rollback externo: somente mudança de credentialVersion com identidade/generation/epoch TODOS inalterados permite aceitar o recibo capturado. REAUTORIZAR real incrementa generation, mesmo no mesmo recurso; não substituir a generation antiga. Mudança de identidade/generation/epoch depois do efeito não rebind/migra conteúdo:409 CHANNEL_CONTEXT_CHANGED; ACK conhecido conserva outcome ACCEPTED_LOCAL_INCOMPLETE e localMessageState RECORDED ou UNCONFIRMED conforme D05; sem ID, UNKNOWN. MessageAcceptance conserva seu fence. Testar REAUTORIZAR real concorrente e version-only separadamente. Janela entre leitura/CAS local e rede existe, sem fence atômico externo ou nova operação durável.
- [ ] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
- [ ] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID tenta recordAmbiguousOutbound uma vez por execução: somente commit confirmado permite409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, diagnóstico FALHOU/null-ID, nunca Message ENVIADA. Precedência: mudança detectada de identidade/generation/epoch após dispatch sem ID, inclusive antes ou durante o fence de recordAmbiguousOutbound, devolve409 CHANNEL_CONTEXT_CHANGED/outcome UNKNOWN; não rebind nem grava diagnóstico sob contexto novo. Somente OUTRAS falhas/commit incerto do diagnóstico devolvem503 OUTBOUND_LOCAL_INCOMPLETE/outcome UNKNOWN/evidence ACK_WITHOUT_ID/diagnosticPersistence UNCONFIRMED, sem afirmar diagnóstico gravado; no409 só declarar diagnóstico gravado com evidência positiva do commit capturado, senão UNCONFIRMED. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa. ACK externo válido seguido de QUALQUER falha local de aceitação/reconciliação/finalização conserva outcome ACCEPTED_LOCAL_INCOMPLETE;409 CHANNEL_CONTEXT_CHANGED se fence alterado, senão503 OUTBOUND_LOCAL_INCOMPLETE. Texto fixo O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente. localMessageState RECORDED somente com commit de Message confirmado ou readback positivo pelo owner/chave/proveniência capturados; nos demais casos UNCONFIRMED, inclusive rollback local confirmado pois eco pode ter gravado em paralelo. No máximo um readback local bounded, sem rebind ou nova chamada externa. Falha após Message commit mantém RECORDED mesmo se atribuição/status falhar; nenhum erro local vira recusa externa. Propagação transient do recibo não cria intent/outbox/schema/segundo owner. UI preserva draft e nunca reenvia automaticamente; Typebot interrompe a rodada, sem replay de saídas. Sem durabilidade/recuperação prometida nem união heurística de Message nula ao eco; dedupe sem ID continua limite para ST-CON-04.
- [ ] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), política extraída sem ciclo DI com ConversationsService, executa policy/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/autoria/publicação. Input trusted distingue BFF humano, API EXTERNO com snapshot e bot; autoria/intenção de atribuição entram ANTES do dispatch. Remover message.update e conversation.update de conclusão no controller público; não limpar autoria comprovada no sender/echo. Para respostas humanas/públicas, atribuição após ACCEPTED é condicional sobre owner corrente, nunca snapshot semDono: claim concorrente é preservado, inclusive público vs claim humano e overlap BFF/público. Status humano/público move IN_SERVICE (grupo preservado); resposta aceita após close concorrente pode reabrir sem roubar novo owner. Bot conserva autoria/unread/status de fila/owner humano e não executa essa finalização humana. Toda falha local pós-ACK segue D05 mesmo após Message commit. MessageAcceptance, índices existentes e unique keys preservados; única extensão de schema é o índice D07 nomeado para seek latest-IN, sem campo/tabela/enum novo;04 reconverge primeiro envio depois.
- [ ] D-07 — Seleção para resposta BFF/API pública usa última mensagem por createdAt DESC,id DESC (ordenação DB, mesma timeline); se seu vínculo falta, nunca substitui por primeiro/outro conectado. Sem última origem: único vínculo pode ser usado; zero CANAL_AUSENTE400, múltiplos CANAL_AMBIGUO409. Origem sem vínculo CANAL_SELECIONADO_INDISPONIVEL409. Bot usa exclusivamente channelId/identidade do ingresso aceito/verificado, mesmo se outra entrada mais recente vier por outro transporte; sem fallback/rebind. Policy comum avalia readiness e requiresWindow do binding selecionado para TODOS, inclusive bot: corrigir explicitamente bypass atual do Typebot. Reavaliar janela antes de cada texto do bot; expiração bloqueia zeroPOST e interrompe rodada, sem replay. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. disponivel observa localmente seleção/policy/trust/conexão/credencial cadastrada, não prova provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem token/rede/mutação; reutilizar metadados da BU na lista, sem novo fan-out por conversa, medir EPS. Projetar latest-IN somente para referências cujo binding selecionado requiresWindow; um índice Prisma-managed @@index([conversationId,direction,createdAt,id], map: messages_conversation_direction_created_id_idx) suporta seek ordenado por conversa/direção, inclusive OUT-heavy/no-IN, com prova PG de loops/filtros/buffers em profundidades crescentes. Preservar timestamp expirado do histórico inteiro e ausência de filtro de transporte; não substituir por predicado de últimas24h. GET thread não falha por canal ausente: janela mantém exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null se seleção impossível. Lista pública mantém campos e acrescenta envio_disponivel/motivo_indisponibilidade. API pública mantém criação prévia da conversa, inclusive vazia em erro; mudar isso é contrato04.
- [ ] D-08 — Extensão aberta por factories/registro DI tipado, inicialmente dois providers. Fake com recipientRef user:opaque não telefônico passa pelo mesmo resolver/owner/BFF com conversa seeded e bot/internal fixtures, sem alterar branches/interfaces dos senders. Regressão pública conserva telefone numérico/normalização atual; não exigir handle Telegram no POST /api/v1/messages. Enum físico OFICIAL/NAO_OFICIAL permanece no adapter de binding; fixture pode mapear slot existente ao fake, sem flag de produto nem alegar rede nova persistida. Registrar adapter estende o port; identidade/BU/contato/credenciais/ingress de redes futuras exigem contratos próprios. Capacidades terão ports pequenos em05/04 e lifecycle futuro, sem no-op/NotImplemented/casts/concrete instanceof nos consumers; não implementar runtime antecipado.
- [ ] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
- [ ] D-10 — UI Inbox e ErroDaApi em api.ts preservam outcome e metadados safe de incerteza do backend, exibem texto fixo honesto, bloqueiam composer por disponibilidade/motivo e mantêm draft em qualquer erro/UNKNOWN/ACCEPTED_LOCAL_INCOMPLETE; sem sucesso ou retry automático. Respostas atrasadas em troca BU/conversa conservam fencing monotônico atual. HTTP sucesso/DTOs de mensagem preservados; disponibilidade/outcome aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts positivos/descartáveis. all completo em leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais INOUT assistida dos dois vínculos. Admitir o mesmo all/lifecycle no job CI PR não-main por seleção explícita de transporte Linux; default local Windows preservado. Guard scripts/check-channels-ci-parity.py parseia YAML de forma segura, rejeita bypass/alias/duplicatas e divergência de suite/ordem/bootstrap/cleanup; controles negativos reais. Provar topologia executável Linux isolada, não só YAML; execução remota fica not_run até publicação de fonte autorizada. Consolidar owners/limites e rebase05/04 só após gates.

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
- **Decision review status:** findings_integrated
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-channel-abstraction-20261020/architecture-opinion.md; parecer tático terminal no-go inicial, AR01..04 e obrigações integrados pelo owner antes da crítica; sem claim de implementação.
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** findings_integrated
- **Adherence review evidence / resolution:** artifacts/reviews/leadshug-channel-abstraction-20261020/implementation-round-1/2/3-resolution.md; roundsfresh terminal/strictmerged. R01/R03/R04/R05 corrigidas no snapshot revisado; ST06-R02 permanece bloqueador até correção/evidência independente do harness.
- **No-go handling:** reconvergir contrato, sem waiver automático.

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Why this decision:** publicar autoridade do contrato antes de review/guard.
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** pending-v1.3-freeze
- **Baseline push reference:** origin/main
- **Gate status:** pending
- **Findings summary:** v1.3 prepared-pre-freeze; publicar contrato antes dos novos reviews. Freeze anterior v1.2 permanece histórico.
- **Evidence / reference:** origin/maina35f676c696e21ec8b4e8ed5cbe6eafbe8da482c push terminal0 em2026-10-20; CR01/02 integrados antes de reconvergência do reviewer.
- **Waiver authority / reference (required if waived):** n/a

## Gate: Review Scope Drift
- **Gate decision:** required
- **Why this decision:** aprovação usa o pacote efetivamente revisado.
- **Trigger stage:** after the planning-side review/guard cycle converges and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Material sections compared:** Context|Scope|Out of Scope|Definition of Done|Validation Steps|Decisions|Decision Baseline|Assumptions Preview|Execution Plan|Security Risk Assessment|Performance & Concurrency Risk Assessment
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **No-go handling rule:** reconvergir review/freeze, sem código.
- **Gate status:** pending
- **Findings summary:** rerun requerido contra baseline v1.3 publicada/revisada; resultado v1.2 preservado como histórico.
- **Evidence / reference:** foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/review-scope-drift.json
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
2. Test-first: harness dependências com negativa sintética, contrato Channel/fake opaco, raw HTTP/resultados/scopes/seleção. PG barriers/readbacks próprios; contexto muda antes do diagnóstico null-ID e durante seu fence vs falha ordinária/commit incerto:409/503/outcome/metadados, um POST e nenhum replay.
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
| root / runner topology | positive inventory + host-transport/CI parity | bash scripts/test-channels-local.sh all | Local-Implemented | planned | manifests/masks fictícios; nenhuma leitura dotenv/.local-files | planned | sem namespace humano; v1.3 guard/YAML + Linux replay pendentes | safe mount/config e origem da principal | leadshug_channels_validation inexistente antes do run, dados descartáveis |

### Runtime / Rollout Notes
Única migration nova: 20261020170000_message_inbound_window_index, um CREATE INDEX versionado e espelhado em schema.prisma; sem campo/tabela/enum/retention novo. Deploy/status em PG descartável antes de aplicar ao DB local de testes preservado. Custo de armazenamento/escrita e breve bloqueio durante CREATE INDEX devem ser registrados; falha interrompe ativação, sem reset/drop. CI compartilha all/lifecycle, PR não-main com fixtures; remoto not_run até publicação autorizada. Local Windows preservado; replay Linux isolado sem privateenv ou dados humanos faz parte da renovação proposta. Namespace validation exclusivo, bundles/builds da principal. Runtime humano somente publicação local planejada e prova assistida depois de readiness; banco/canais preservados, sem reset ou rotação. Nenhum transporte real futuro ou status externo de entrega presumido.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)
### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

Revisão de planejamento concluída: architecture_opinion findings_integrated e crítica fresh terminal go. Checkboxes representam análise do plano, não execução/testes/medição do produto. PLAN01/02 opçãoA adotada; AR01..04/CR01..02 resolvidos nos relatórios.

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
- [ ] eco antes/depois do sender; público vs claim humano/overlap BFF; Typebot retido enquanto outra origem chega, janela expira ou contexto muda; empate de createdAt entre transportes.
- [ ] falha antes de acceptance, commit incerto, Message commit seguido de erro na finalização e diagnóstico null-ID sem commit: projeções D03/05, sem replay.
- [ ] UI troca A→B→A durante erro/envio; nenhum retry ou limpeza de draft de outra conversa.

### Residual Unknowns / Risks
- [ ] Cutover sem intent durável conserva limite de crash antes da aceitação/publicação e diagnósticos null-ID sem dedupe; ST-CON-04 deve reconvergir esse limite, não inferir exactly-once.
- [ ] Port extensível não significa persistência/contato/ingress de rede nova pronto; fake só prova substituição interna.
- [ ] Readiness real e medições só depois de aprovação; coorte privada continua, sem produção/usuário não confiável liberado.
- [ ] Arquitetura integrada e crítica fresh reconvergida go no pacote v1.2; guardas finais de planejamento abaixo, toda prova de produto permanece planned.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)
- **Needed:** no
- **Why ambiguity remains:** diagnóstico teve parecer independente de enquadramento; agora gate architecture_opinion desafia D01..10, sem tratá-lo como duplicado satisfeito.
- **Opinion count:** 1 framing advisory,1 tactical terminal com achados integrados
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required na gate tática
- **Required lenses:** correctness,performance,elegance,structural-soundness,operational-fit

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)
- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/audit-floor.json; go/fa884bf1d2e7

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
- **Critique status:** pending
- **Findings summary:** v1.2 convergido historicamente; renovar crítica fresh no contrato completo v1.3 após arquitetura da correção index/CI.
- **Resolution ledger:** artifacts/reviews/leadshug-channel-abstraction-20261020/critique.md
- **Evidence / reference:** artifacts/reviews/leadshug-channel-abstraction-20261020/critique.md; fresh /root/stcon06_critique gpt-6.1-sol/max, inicial81d56f5e + reconvergência terminala35f676c.
- **Waiver authority / reference (required if waived):** n/a

## Gate: Assumption Code Coherence
- **Gate decision:** required
- **Why this decision:** premissas concretas de senders/resolver/aceitação/runtime.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A01..05
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Gate status:** pending
- **Findings summary:** revisão semântica A01..05 ancorada em fonte pública e conferida por arquitetura/crítica; adequações são trabalho explícito, sem fingir garantias atuais.
- **Evidence / reference:** foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/source-assumptions.json; architecture-opinion.md; critique.md; evidence/assumption-coherence.json, guard go/5 premissas.
- **Waiver authority / reference (required if waived):** n/a

## Approval
- **Approved by:** usuário para v1.2; renovação v1.3 pendente
- **Approval reference:** resposta literal APROVADO nesta conversa em2026-10-20, após apresentação do contrato v1.2 publicado em Foundation781ea16e51e0db2a654e6956ea633a03dd509dfd (freeze materiala35f676c).
- **Approval scope:** v1.2 ST-CON-06/SCOPE01..05/D01..10 e dois companions validados. SCOPE06/índice/CI e mudanças materiais v1.3 NÃO aprovados; nenhuma autoridade nova presumida.
- **Execution not authorized by approval:** todo Out of Scope, redes futuras,05/04, push/deploy de produto ou mudanças privadas.
- **Renewed approval required when:** decisões/DoD/paths/risco/contrato mudarem materialmente.
- **Pre-approval readiness evidence:** artifacts/reviews/leadshug-channel-abstraction-20261020/README.md; authority-preapproval.json = preflight-go, execution_authority_granted=false; estrutura PASS. APROVADO específico recebido; authority normal pós-ingestão registrado em evidence/authority-execution.json.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)
Binding reload realizado após APROVADO em2026-10-20 pelo orquestrador: fontes da tabela relidas; constituição/política/módulos recarregados e verify_context PACED-Ready. Executor relerá as regras técnicas pertinentes antes dos edits. Ingestão não é evidência de implementação/testes. Nenhum GOAL persistente foi criado.

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
- **Guard outcome:** go
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

Terminal architecture/security findings classified by review-finding-classification. All current-slice findings remain blockers until fixed and evidenced; no waiver/debt accepted. Exact text and deduplication: artifacts/reviews/leadshug-channel-abstraction-20261020/implementation-round-1-resolution.md.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| ST06-R01 (ADH-01=SEC-01) | high | release-blocker | same-todo | Original non-first/malformed-ID counterexample corrected; new flag case tracked R05 | resolved in round2 snapshot; finalvalidation pending | implementation-round-1-resolution.md; existing D04 approval |
| ST06-R02 (ADH-02) | medium | release-blocker | same-todo | Navigation corrected; await body/handler completion and prove same-text draft fence catches removal | resolved reviewed snapshot; new PERF blocker separate | implementation-round-3-resolution.md; dedicated round01 Performance/TQA confirm harness |
| ST06-R03 (SEC-02) | medium | release-blocker | same-todo | D04/05 Evolution empty object is not ACK; key:{} preserved | resolved in round2 snapshot; finalvalidation pending | implementation-round-1-resolution.md; existing D04/05 approval |
| ST06-R04 (SEC-03) | medium | release-blocker | same-todo | Denied mutations/twoTENANT proof added; preDispatch must exercise real Meta/Evo adapters and detect omitted callback | resolved reviewed snapshot; final assurance pending | implementation-round-3-resolution.md; existing scope/validation approval |
| ST06-R05 (adherence-round2 ADH-R2-01) | medium | release-blocker | same-todo | D04 explicit false/malformed success flag contradicts positive ACK; UNKNOWN/no authoritative write | resolved reviewed snapshot; final assurance pending | implementation-round-3-resolution.md; D04 existing approval |
| PERF-01 (dedicated round01) | high | release-blocker | same-todo | OUT-heavy/no-IN latest-IN scan unbounded; preserve expiry semantics, need actual plan and potentially narrowly approved index | open; reproduction and renewed scope proposal | dedicated-round1-adjudication-draft.md; schema not authorized by v1.2 |
| PERF-02 (dedicated round01) | low | follow-up-hardening | same-todo | Unsupported per-subject RLS threshold requires exact perconversation readback; bounded admitted test correction | open; inline evidence correction | dedicated-round1-adjudication-draft.md; no schema change |
| TQA-01 (dedicated round01) | high | release-blocker | same-todo | CI-admission contradiction requires canonical rule/scope adjudication; no automatic waiver | open; fresh governance opinion84759 | ci-admission-challenge-package.md; no CI edits authorized |


## TODO Closeout Disposition
- **Disposition:** keep-active
- **Disposition reason:** contrato aprovado, implementação e validação em execução; não encerrar antes de todos gates.
- **Post-commit/push status:** baseline materiala35f676c publicada/revisada; pacote documental finalizado com guardas pré-aprovação; produto Pending.
- **Next path/status action:** executar ST-CON-06 aprovado, manter active até evidências e gates de entrega.

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
- **Audit session / round evidence (when protocol used):** artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/session.json; round01 active
- **Audit status:** blocked
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
- **Canonical method:** wf-docker-independent-final-review-method
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
- **Cutover audit status:** no_material_findings
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
| IncomingService Typebot text response | existing bot sessions | accepted ingress exact channel/identity/tenant, no fabricated human user | same shared outbound/window/result/acceptance; preserve queue/status/human owner, stop on unknown/block/refusal, no replay |

**Fixed availability reasons:** CANAL_AUSENTE, CANAL_AMBIGUO, CANAL_SELECIONADO_INDISPONIVEL, CHANNEL_IDENTITY_NOT_VERIFIED, CHANNEL_NOT_READY, PENDING_CREDENTIAL, JANELA_FECHADA; null when observed available. Availability never grants authority or guarantees external delivery. Existing input limit4096/request phone normalization stays at current product boundaries; the Channel port has no universal WhatsApp address requirement. No new public route or channel choice field is introduced in06.

## Planning references / provenance

Direction and extension requirements are explicit user statements2026-10-20. Initial framing opinion is artifacts/analysis/leadshug-channel-abstraction-framing-opinion-20261020.md (advisory only). Primary conceptual sources: NestJS custom providers https://docs.nestjs.com/fundamentals/custom-providers and Liskov/Wing1994 https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf, previously consulted. Provider error source consulted by owner (bounded public reference; reviewer independently hit429): https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes/. Local code proves current behavior, not future platform integration or live readiness.

## Execution Checkpoints

| Checkpoint | State | Evidence / limit |
| --- | --- | --- |
| CP01 — runner antes de testes | passed precondition | artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/runner-checkpoint.json; allowlist antes de stat, sem varredura ampla; bash-n/diffcheck/mock config-only. Nenhum teste de produto ou Docker real executado neste checkpoint. |
| CP02 — Channel/outbound/consumers + Web/tests | implementation, not delivered | Executor único; artifacts/tmp/stcon06-executor-* e evidence/executor-validation.json reservados. Initial RED dependencyguard175pass/1fail. all33610 terminal0:194unit/308PG/29Web/50browser, snapshot anterior agora insuficiente pelas findings round2. |
| CP03 — independent adherence/security rounds1/2/3 | terminal; R02 protection gap open | R01/R03/R04/R05 corrected in reviewed snapshot; shippingadapter omission mutants fail409vs201 then exactrestored. R02 needs causal response.text/handler barrier. Full implementation-round-1/2/3-resolution.md; no waiver/debt or physicalproof. |
| CP04 — actual R05 regression RED | reproduced before fix | Canonical API49493 terminal1: Meta200 success:false+ID expectedUNKNOWN/TRANSPORT_UNCONFIRMED, actualACCEPTED;20otherunitfiles green. Executor will preserve exact log/provenance and correct source after terminal. Not blanket RED for other cases. |

## Supplemental Expected-Path Validation — 2026-10-20

User explicitly replied **“Validar os dois arquivos de apoio”** to the exact bounded proposal [test-companion-path-admission.md](../../../artifacts/reviews/leadshug-channel-abstraction-20261020/test-companion-path-admission.md). This validates only Web `src/api.spec.ts` and `e2e/timeline-freshness.ts` as M companions for D10/SCOPE05. Scope, DoD, public behavior, frozen D01..10, private-data prohibition and required checks are unchanged. The direct client test was already added before the path omission was noticed; its admission is explicit here. The nested helper correction was not applied or run before this validation. Executor remains sole product writer; browser/all may proceed only after both freshness inventories use positive pathspecs before discovery.

## Implementation Assurance — Round 1

Architecture adherence and separate security reviews completed through canonical subagent_review_run.py, gpt-6.1-sol/xhigh, closed embedded source packages; strict merge passed. Architecture: changes required; security: source-only classification defects and evidence gaps, no demonstrated tenant breakout or credential disclosure. Artifacts: evidence/adherence.raw.json, adherence.merge.json; security.raw.json, security.merge.json. Reviews did not certify final all or physical proof. No live review was cancelled or repackaged. All findings integrated as approved-contract remediation, with delivery still Pending.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ADH-01 | Integrated | useful | yes | project | n/a | ST06-R01; D04 complete-envelope classification, remediation open |
| SEC-01 | Integrated | useful | yes | project | n/a | duplicate ADH-01 consolidated ST06-R01; same open blocker, not ignored |
| ADH-02 | Integrated | useful | partial | project | n/a | ST06-R02; independently confirms browser navigation defect, remediation open |
| SEC-02 | Integrated | useful | yes | project | n/a | ST06-R03; supported ACK structure vs malformed empty object, remediation open |
| SEC-03 | Integrated | useful | yes | project | n/a | ST06-R04; reconcile source/proofs and add only missing local negative/isolation cases |


## Implementation Assurance — Round 2

Both canonical CLI reviews terminal0, strict merge passed: evidence/adherence-round2.raw.json and security-round2.raw.json. Full adjudication and exact overlapping ID bindings: implementation-round-2-resolution.md. Original R01/R03 counterexamples resolved at source; R02/R04 protection gaps remain and R05 is a new classifier case. No architecture expansion, waiver/debt or delivery claim. Runner33610 must terminate before further product edits.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| adherence-round2:ADH-R2-01 | Integrated | useful | yes | project | n/a | ST06-R05 Meta success:false contradiction; approved D04 remediation open |
| adherence-round2:ADH-R2-02 | Integrated | useful | partial | project | n/a | ST06-R02 headers-only wait can falsely pass before stale completion |
| adherence-round2:ADH-R2-03 | Integrated | useful | yes | project | n/a | ST06-R04 testfake owns guard, must exercise shipping adapter callback |
| security-round2:ADH-R2-01 | Integrated | useful | yes | project | n/a | duplicate ST06-R04, same shipping-adapter harness gap |
| security-round2:ADH-R2-02 | Integrated | useful | partial | project | n/a | duplicate ST06-R02, same browser completion gap |

## Review round3 findings resolution

| Finding ID | Disposition | Usefulness | Formalizable | Candidate Rule Level | Rule Update | Evidence / limit |
| --- | --- | --- | --- | --- | --- | --- |
| adherence-round3:ADH-R3-01 | Integrated | useful | partial | project | n/a | ST06-R02; test-only native body-read task barrier, mutation proof and revised canonical validation pending |
| security-round3:ST06-R02 | Integrated | useful | partial | project | n/a | same ST06-R02; no demonstrated production vulnerability, D10 protection gap retained blocking |

## CP05 — causal browser protection proof

Corrected test b3604496…8e0f3 observes native text-read settlement and a following browser task before assertions. Diagnostic63018 passed50/50. Actual guard-replacement mutant30246 failed only the intended same-text draft assertion after body counts1/1/1;49other browser cases passed. Full captured log/root source/restoration/served-bundle provenance: artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/browser-causal-*.json. Source restoration is byte-exact. Failed64345 ordering attempt and63018 diagnostic are not mislabeled as mutation proof. Canonical finalall80903 remains running; no Local-Implemented or physical-channel delivery claim.

## CP06 — final automated validation and dedicated audit dispatch

Canonical all80903 terminal0:194APIunit/309realPG/29Webunit/50browser. Root verified unchanged product/runner bytes against causal-final-source-before-all80903.json and36changedpublicsource manifest hashes plus served/dist/preserved bundle27c5db46. Full log SHA778f858923f4df7457d32908a98dfda31d0b4351579acabdc1fb90515bec8554. Dedicated Performance(gpt-6.1-sol/xhigh), TQA and Cutover(both gpt-5.6-terra/xhigh per normalrouting) freshly dispatched with complete bounded package and mandatory consumer/fullTQAworkload; no audit result presumed. Runtime/source commit/push/deploy remains untouched except Foundation main documents.

## Scope Renewal v1.3 — pending explicit approval

Concrete contract: [scope-renewal-v1.3-proposal.md](../../../artifacts/reviews/leadshug-channel-abstraction-20261020/scope-renewal-v1.3-proposal.md). Existing APROVADO v1.2 and user validation of both companions are preserved, not repurposed as v1.3 approval. Authority for new schema/CI paths is pending.

- Confirmed PERF01 RED15524:194 unit pass/309 E2E pass/2 exact new failures; 200 direction-filtered OUT rows, and unnecessary window query for selected non-window channel. Raw log SHA8b2fc6510dafe4be8a10de73d150695a82a667bcb4255067e3b64da9b87ae248.
- CIADM01 integrated current configuration/admission blocker. CIADM02 challenges only the implication that remote execution or waiver is needed for local milestone; remote remains not_run, future CI/promotion owner, no source push now. Fresh opinion raw/strictmerge in evidence/ci-admission-challenge.*.
- PERF02 precision fixed inline in admitted test:5waves×20 per-conversation counts exactly1. No external same-key exactly-once claim.
- New risks: B-tree storage/write maintenance; brief write lock during local CREATE INDEX; Linux/Windows path transport and checkout metadata; increased CI duration and existing private token availability. Mitigate with disposable migration/plan/concurrency proof, one common lifecycle/guard, no secret files, exact branch/source/served hashes and explicit unrun remote state.
- Execution order after APROVADO: ingest revised rules/routing/authority; implement only exact admitted index/CI remediation; deploy/status disposable PG; verify real and mutated drift guards and Linux isolated topology; invalidate/replay broad all; fresh full audits/PCV; rebuild/migrate one local test DB/activate API-Web; new HTTPS/operator INOUT both; consolidation/final guards. No schema/CI/runtime before renewed approval.
- Required rules added to ingestion: delphi-ai/skills/ci-equivalent-governance/SKILL.md; delphi-ai/skills/ci-equivalent-test-surface-admission/SKILL.md; delphi-ai/workflows/docker/update-ci-pipeline-method.md; existing Prisma/PostgreSQL rules. Actual binding reload after renewed approval.
- Planning renewal status: prepared-pre-freeze; architecture_opinion + independent critique + assumption/scope/auditfloor/preapproval guards pending. No waiver.
