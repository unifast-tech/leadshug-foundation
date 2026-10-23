# ST-CON-04 v1.1 implementation review candidate — fresh cutover integrity audit challenge

Selected checkpoint: E74; actual canonical ALL exit0, full259 postseal/recheck, 93-record browser freshness, current images, same-run CI parity and 18 PCV metrics are bound below. Fingerprint `589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e`. Phase metrics: api_unit=368, api_postgresql=456, web_unit=54, browser=89, migrations=28. R6 collection/results are hash-crosschecked.

R6 identified F-CF091066 (missing managedLifecycle qualification), F-5E961B39 (malformed native statistics defaulted to zero), and an insufficiently substantive TQA report. Current root resolutions bind both causal corrections; this packet preserves the complete audit workload and requires a full eight-section TQA. PCV statistics remain test-only; package preparation is not an independent review.

Chronology: E65/E66 actual RED; E67 lint failure; E68 import failure; E69 unit368/368 and PostgreSQL449/451; E70 RED on active-admission ordering/stale native-index expectation; E71 historical GREEN; E72 actual test-only API RED reaching both causal assertions (unit368/368, PostgreSQL451/456; browser unreached); E73 actual ALL GREEN with967 tests and recovered93-record browser freshness, but lost stdout and no PCV metrics. E73 is historical only; selected E74 stdout, seal/recheck, images, browser, CI and PCV govern current status.

The immutable R6 body retains original15 findings, three R4 findings, R1–R3 chronology, approved contract and E64 module baselines. The verified R7 documentation patch and separate hash-bound E74 activation proposal are included; neither is applied or approved. Independent current reviews, module application, runtime/operator own-channel proof, private-boundary full diff guard and final delivery remain pending. No private env/files, process data, logs, business rows or provider effects are public evidence.

## Current selected-checkpoint receipts


## Historical R6 package context, findings, and chronology (immutable; not current status)

The following complete prefix is retained from the hash-verified R6 package. Its run-specific status and metrics describe R6/E71 only; the selected current checkpoint above and receipts below govern this package.

# ST-CON-04 v1.1 implementation review candidate r6

This is a fresh no-context internal challenge package built only after the explicitly named terminal ALL checkpoint exits 0 and the independent full259 positive-source postseal matches its source seal. Do not call tools or edit files. Assess this bounded evidence and the exact approved intent. Return only the dispatch-required JSON. Findings first by severity. Bounded summaries are marked with exact source hashes and explain their limits. Source is frozen from the principal checkout. This fresh r6 round evaluates the current corrected candidate and original r1/r2/r3 findings; it has no inherited chat context. Prior reviews are challenge evidence, not approval authority.

Stage: implementation candidate, delivery Pending. The complete implementation is being evaluated for readiness to request a separately bounded preserved-local activation; no actual new runtime/operator proof or final delivery is claimed. DOD11/12/13 and full canonical diff-guard remain pending. Identify those as explicit follow-up gates; do not invent a completion claim. Product defects, missing producer/consumer implementation or insufficient implementation proof are material findings even at this stage.

Approved: user APROVADO; subsequent exact Typebot/PCV test fixture adjustments validated; own template reported APPROVED by human, not remote verified. Public roots only; no actual .env, .local-files, process/env/log or business-row inspection. The canonical recursive capability helper and full diff guard cannot silently cross that boundary. No product Git writes/worktree/provider routing or automated contact.

Chronology is mixed and must be judged honestly: E03 was absent-module RED; E04 included actual renderer RED plus a separately disclosed post-hoc reversion diagnostic, never retroactive test-first. E11 valid union RED, E21/22 ordinary dispatch RED, E25 coordinator module RED, E35 real-BFF/browser missing-first-flow assertion RED, E41 actual UI/uncertainty defects, E44 exact snapshot-read data-loss assertion RED before E45 UI fix. Most later fault/protocol/boundary tests were alongside/post-implementation. No causal proof is claimed for an assertion not reached. Explicit qualification: E03/E15/E25 absent-module RED is not business assertion RED; E04 reversion is post-hoc. E50 actual PG/BFF projection/interlock/COUNT/settlement/realtime assertions and E51 positional Unicode snapshot assertion precede the r1 product fixes. E48/E49 test-support failures are not product RED. Detailed exact chronology and fresh corrected full-all proof are embedded. E18 editing during an old live run invalidated that old candidate; source-freeze and full independent inventory/byte postseals govern current evidence. E02 broad discovery and E35a .gitmodules read deviations are preserved, not hidden behind full-compliance language.

Inherited constraints SEC-R6-04 (ST05 recovery-budget debt), OPS-R4-01 and TQA-ST05-03 remain assigned to their prior scopes; no future work is implemented here. The already-approved initial-send union and trusted-IN window deliberately supersede prior ST06 text-only/createdAt behavior; ST05 authoring payload/flags remain sealed and independent. Public/BOT preserve existing diagnostic/error semantics; they do not gain global idempotency. One POST per captured initial attempt is the claim, never end-to-end external exactly-once.

Evidence boundaries: real disposable PostgreSQL, actual BFF/session/CSRF and fresh served React browser. External provider is an owned fake. Port invocation counters are not provider TCP request counts. Full preserved runtime/source/image/migration and human own-channel first-send/reply tests are later required gates.

E70 actually terminated RED: its recent-intent query used an ordered index for 11 rows, but both active-admission options and conversation-wide conflict EXPLAIN sorted/scanned 2,304 rows over 2,048 released plus 256 active admissions; a separate native metadata test retained a stale old-index expectation. Six window/pin/refresh probes passed, browser phase was not reached. The E71 preflight introduced SQL-only partial ordered-index metadata and corrected expectations. No E71 partial run is promoted to review-ready proof; the selected later terminal ALL checkpoint and its PCV receipts below define current status. The repository baseline includes inherited uncommitted ST05/ST06 sources. Exact inherited hashes precede ST04 changes; 38 protected/exact-companion records remain equal. Git HEAD alone does not identify those dirty bytes. Current source hashes and original seals bind the candidate. A Git-baseline aggregate diff must not be misrepresented as an isolated ST04 patch; full current changed relevant source, exact changed schema models/migration, and hash-bound summaries of unchanged supporting sources plus explicit initial-seal classification are embedded here.

Current source fingerprint: `4f35237f1d6aaf55f98e129631e17184d8f5b196249f6c56c10f210add52daf4`, 259 complete positive public records.

## Exact approved governing contract excerpts

## Context

ST-CON-06 entregou o transporte abstrato textual, adapters Meta/Evolution, resolução scoped e um `OutboundService` compartilhado; ST-CON-05 entregou autoria/submissão e o catálogo/projetor compartilhado de templates. Ambos permanecem contratos entregues e evidência de dependência, não aprovação desta história. A inbox ainda não permite iniciar atendimento manual por contato e conduzir o primeiro envio oficial de modo recuperável.

Este v1.1 substitui a autoridade ativa da minuta revisada em 2026-10-19. O original e suas decisões/reviews são preservados pelo owner do pacote como `historical-planning-20261019-20261020.md`; nada daquele ciclo é evidência de revisão, guard, aprovação ou execução deste texto. Os handoffs de ST-CON-06 e ST-CON-05 continuam como contexto factual.

**Perfil desta etapa:** Strategic / CTO-Tech-Lead; escopo ativo NestJS, React, Vite, PostgreSQL, Prisma e Docker. Genesis foi rejeitado: o projeto canônico já existe. Próximo handoff planejado: Operational / Coder após contrato congelado, reviews/guards atuais e aprovação humana explícita. Supporting profiles: Assurance / Tester-Quality, Assurance / Security-Adversarial e Operational / DevOps para os respectivos gates. Seleção declarada conforme `delphi-ai/workflows/docker/profile-selection-method.md`.


## Contract Boundary

- Este TODO define **WHAT** será entregue; `Assumptions Preview` e `Execution Plan` registram a proposta **HOW** para revisão.
- O escopo é fechado ao início manual e primeiro envio de uma conversa. Qualquer alteração material de Scope, DoD, validação, contrato público ou decisões requer retorno à revisão e nova aprovação antes de execução.
- “Aceito” significa ID externo válido persistido; não significa entrega ao aparelho nem leitura.
- Baseline inicial publicado antes dos primeiros guards/review; parecer arquitetural r1 integrado abaixo. Mudanças materiais decorrentes do parecer serão publicadas em novo freeze antes da crítica. Nenhuma implementação ou aprovação humana é reivindicada.


## Scope

- [ ] **SCOPE-01 — Abrir/reusar conversa:** sessão BFF com CSRF e papel ATENDENTE+; criar/reusar atomicamente a conversa única por BU+contato, com telefone obrigatório normalizado a 8–15 dígitos sem inferir país/DDI. Sem CRM. Abrir não envia, não reivindica atendimento, não reabre/fecha, não marca leitura e não altera timeline existente. Conversa nova começa `QUEUED`, `unreadCount=0`, `lastMessageAt=null`; listagem ordena por `COALESCE(lastMessageAt, createdAt)` sem data fictícia. Abrir nunca dispara automação. Preservar NOVA_CONVERSA baseado em criação persistida: primeiro IN posterior a uma abertura manual vazia não o dispara; PALAVRA_CHAVE mantém sua regra atual.
- [ ] **SCOPE-02 — Primeiro envio durável:** endpoints autenticados BFF para opções, preview, criação de intenção, leitura/reconciliação/acknowledgment; UUID idempotency por BU+ator; slot ativo por conversa; request/context/fingerprint imutáveis. Fallback automático entre canais é proibido.
- [ ] **SCOPE-03 — Política de texto e janela:** manter readiness e `requiresWindow`; introduzir `Message.officialInboundAt` nullable somente de IN Meta assinada e verificada com timestamp inteiro positivo, não futuro e identidade/resource gerenciados. Janela por maior valor confiável na conversa e recurso atualmente selecionado, com limite estrito `<24h`; não inferir de `createdAt`, payload bruto, importação ou fonte não oficial. Dados ausentes/malformados/futuros permanecem null sem descartar a mensagem. Timeline/cursor seguem `createdAt`.
- [ ] **SCOPE-04 — Primeiro envio por canal abstrato:** proposta sob revisão: estender a única abstração `Channel.sendMessage` a um union discriminado `text | approved-template`, acompanhado de `readonly supportedKinds`; Meta declara ambos; Evolution declara text e responde `BLOCKED/UNSUPPORTED_KIND` antes de qualquer HTTP para template. Adapter Meta formata destinatário como `+` seguido do DDI completo; identidade/storage do domínio continua dígitos canônicos. Cobrir destinatários do mesmo país e de outro país e preservar a semântica de envio de texto existente, verificando explicitamente sua formatação wire compartilhada. Resolver seleciona canal explicitamente com contexto immutable e versão atual da credencial. Não criar `sendTemplate`, branches por provider em domínio/consumers, casts/`instanceof`, plataforma genérica de plugins ou integrações futuras.
- [ ] **SCOPE-05 — Catálogo e composição:** reutilizar exatamente `GET/POST /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` e seu domínio, projector, lease/fence, TTL de 300s e parser de enum entregues por ST-CON-05. Remover da proposta anterior o duplicado `GET /conversations/:id/channels/:channelId/templates`. TemplateManagement permanece capability estreita sem método de envio a destinatário. Preview POST é local/read-only, sessão+CSRF, sem DB write/provider call; retorna texto escapado e fingerprint determinístico ligado a conversa/contato/contexto atual.
- [ ] **SCOPE-06 — Subconjunto de template:** BODY textual NAMED/POSITIONAL, header/footer somente estáticos; sem botão, mídia, auth, flows, arbitrary Graph payload ou ampliação de categorias suportadas. Texto final 1–4096 chars; até 20 parâmetros de 1–1024 chars; snapshot total até 4096. Catálogo é observação, nunca autorização de envio: antes de cada novo envio validar remotamente asset/status atual da mesma conta; detectar mudança/pausa/unknown e falhar fechado. `getTemplate(id)` isolado não prova vínculo de conta; usar listagem existente por nome salvo na observação confiável, filtrada em até 2 páginas de 50, com correspondência exata ID/nome/idioma/semântica e resultado esgotado. Cursor/URL do browser nunca autoriza fetch.
- [ ] **SCOPE-07 — Saga local e owner:** coordenador de intenção vive no domínio inbox e chama o `OutboundService` comum; reutilizar seu dispatch abstrato e `MessageAcceptanceService` como único owner de Message. Se necessário, permitir que esse mesmo owner aceite via transação scoped, preservando wrapper existente; hoje `OutboundService.finalize` separado e `MessageAcceptanceService.accept` transacional não devem ser descritos como já integrados. Efeitos de status/owner do novo fluxo só por CAS contra `updatedAt/state` capturados antes do HTTP e owner ativo; preservar claim/close concorrentes, sem roubo.
- [ ] **SCOPE-08 — Estados e recuperação:** UUID keyed por BU+actor; replay do request canônico acontece antes de leituras de provider, respeitando grant atual. Slot único ativo separado do outcome. `PREPARED` lease 90s; `SENDING` só após todos os reads remotos de elegibilidade/grant/phone preflight e claim CAS persistido pelo abstract dispatch-fence hook imediatamente antes do POST; no máximo um POST externo por tentativa e nenhuma repetição automática. Falha/expiração comprovadamente pré-dispatch → `REJECTED`, slot liberado por CAS. SENDING abandonado/timeout/resultado desconhecido/ID faltante → `AMBIGUOUS`, slot bloqueado. ID conhecido → `EXTERNAL_ACCEPTED` persistido separado da Message local; recuperação apenas local. Não fazer provider GET/POST, fuzzy echo matching ou criar Message sem externalID. `EXTERNAL_ACCEPTED_LOCAL_BLOCKED` conserva o fato e ID, sem falsificar sucesso. Acknowledgment apenas após classificação de incerteza/bloqueio e DBnow >= dispatchDeadlineAt imutável (mesmo deadline da lease90s original, nunca renovado), inclusive para EXTERNAL_ACCEPTED_LOCAL_BLOCKED, com risco explícito de duplicata e liberação irreversível; resultado tardio não readquire slot nem altera owner/status corrente.
- [ ] **SCOPE-09 — Compatibilidade de callers:** composer BFF existente deve bloquear, antes de qualquer HTTP, conversa nova/vazia ou qualquer slot inicial não resolvido. BFF público e BOT também consultam/respeitam slot ativo antes de dispatch para evitar duplicação; manter suas atuais formas de aceitação/erro e não lhes atribuir idempotência global. Interlock finito definido no aditivo normativo r1 abaixo: tokens ordinários por owner, compatíveis entre si, excluem reserva inicial até settlement ou acknowledgment explícito de incerteza. Expiração de SENDING nunca libera por relógio. Preservar semântica diagnóstica de ACK nulo de ST-CON-06 para callers antigos; regra de Message sem externalID aplica-se ao novo coordenador.
- [ ] **SCOPE-10 — Bounded I/O, prova e limites:** readiness permanece RECEIPT/identidade própria/epoch/estado CONECTADO/`activeCredentialVersion`; management purpose não desvia a prova de envio. Reutilizar reads estreitos ST-05 e client de protocolo de template-send dentro do adapter Meta; nenhum HTTP Meta no inbox. Até 6 GETs no novo template dispatch: 1 grant management + 2 páginas filtered templates + 1 messaging grant + 2 membership pages; no máximo 1 POST. Timeout por request 10s, orçamento total 75s dentro de lease 90s. Reutilizar grant por request-bound adapter sem probe oculto/double count. Limites de nova intenção: 10/min por ator e 60/h por namespace canônico de conta/recurso, inclusive links locais entre BUs/tenants da mesma conta, sem expor dados estrangeiros. Leituras de catálogo preservam limites/dívidas privadas de ST-05; recovery tem zero rede.
- [ ] **SCOPE-11 — Prova assistida futura:** depois de candidate GREEN, assurance de imagens e migration descartável/local, validar primeiro envio assistido não oficial, template oficial realmente `APPROVED` próprio e reply do destinatário. A ausência de asset elegível bloqueia conclusão; fixture não prova aprovação. Nenhum contato automático.
- [ ] **SCOPE-12 — Harness e consumidores:** dependency/fake substitutability, testes negativos Evolution zero HTTP, regressões de texto BFF/public/BOT, janela/projeções batched, timeline/cursor e performance. Preservar SEC-R6-04, OPS-R4-01 e TQA-ST05-03 como limitações entregues; não implementar backlog dessas histórias aqui.


## Out of Scope

- CRM, lead/funnel, campanhas, broadcast, importação de histórico, sender automático ou criação automática de contato/conversa.
- Gestão/autoria/submissão/status de templates, novo projector/cache/catalog DTO, refresh oculto/polling, nova rota de catálogo ou nova capability provider genérica.
- Novos providers, envio outbound em lote, retry automático, exactly-once externo, outbox/event platform, fuzzy matching ou qualquer envio no browser.
- Modificar credenciais/routing Meta, nova modalidade de cadastro, consultar conta real nesta fase, Railway/promoção/deploy. Código/runtime/testes só após APROVADO deste contrato; ativação local futura limitada à evidência abaixo.
- Corrigir SEC-R6-04, OPS-R4-01, TQA-ST05-03 ou demais backlog ST-05/ST-06 sem decisão própria.
- Ler/listar/stat/hash/traversar/montar `api-app/.local-files/`, `.env` ou `.env.testing`; ler argumentos/process env/logs/linhas de negócio.
- Código fora da lista aprovada, worktrees/cópias auxiliares, gitlinks/.gitmodules, alterações Delphi, commit/push de produto. Foundation main pode publicar apenas TODO e pacote de planejamento/revisão pelos guardas documentais próprios.


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
| foundation | foundation_documentation | 197e7a0713c132c6213e218748655bcda5a19c72 | working_tree |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | prisma/migrations/20261021130000_message_template_drafts/migration.sql | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | prisma/migrations/20261021150000_message_template_operations/migration.sql | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | prisma/schema.prisma | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/channels/channel-credential-resolver.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/channels/channel-credential-resolver.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/historico/catalogo.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/historico/cobertura.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/message-templates/template-definition.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-definition.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-draft.service.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-management.dependencies.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-management.ports.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-management.ports.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-observation.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/message-templates/template-submission.service.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/message-templates/template-transaction-boundary.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/message-templates/template-management.module.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/message-templates/template-management.resolver.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/meta/message-template.client.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/meta/message-template.client.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/bff/bff.module.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/surfaces/bff/message-templates.controller.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/browser-server.cjs | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | test/helpers.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | test/message-template-bff.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/message-template-drafts.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/message-template-management.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/number-onboarding-bci.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/number-onboarding-pcv.e2e-spec.ts | M | Human-validated E23 bounded test-only synthetic signed timestamp/current-resource alignment and corresponding trusted-window EXPLAIN per window-fixture-companion-admission-v1.1.patch; all other baseline bytes/scenarios/counters preserved |
| api | test/timeline-fixtures.cjs | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | e2e/message-templates.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| web | e2e/number-onboarding-freshness.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | e2e/timeline-freshness.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/App.tsx | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| web | src/api.spec.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/api.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/telas/Modelos.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| web | src/telas/Modelos.tsx | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| root | .github/workflows/ci.yml | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| root | scripts/test-channels-local.sh | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| root | scripts/check-channels-ci-parity.py | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/inbox/conversations.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/incoming.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/incoming.typebot.integration.spec.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: qualified window, shared admission and manual-open first-inbound automation regression only; initial hash mandatory before FIRST change |
| api | src/integrations/evolution/evolution.client.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/evolution/evolution.client.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/meta/meta.client.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/integrations/meta/meta.client.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/bff/conversations.controller.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: BFF manual open/options/preview/intent/admission-recovery endpoints and scoped ACL; initial hash mandatory before FIRST change |
| api | src/surfaces/public/conversations.controller.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/public/public.module.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/surfaces/webhooks/webhooks.module.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | test/api-publica.e2e-spec.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: ordinary public text/window/admission mappings; initial hash mandatory before FIRST change |
| api | test/number-onboarding-typebot.e2e-spec.ts | M | Human-validated E23 bounded test-only synthetic signed timestamp/current-resource alignment and corresponding trusted-window EXPLAIN per window-fixture-companion-admission-v1.1.patch; all other baseline bytes/scenarios/counters preserved |
| api | prisma/migrations/20261020170000_message_inbound_window_index/migration.sql | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/channels/transport/channel-dependencies.spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
| api | src/domain/channels/transport/channel.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/outbound.service.spec.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/domain/inbox/outbound.service.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/channel-adapter-factory.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/channel-adapter-registry.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/channel-transport.module.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/evolution-channel.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/meta-channel.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | src/integrations/channels/prisma-channel-resolver.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| api | test/channel-transport.e2e-spec.ts | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | src/telas/Inbox.tsx | any | Inherited exact baseline with bounded ST04 mutation proposed after APROVADO for the named journey; initial hash still mandatory before FIRST change |
| web | e2e/channel-transport.spec.ts | any | Inherited exact baseline with bounded ST04 mutation after APROVADO: inherited ordinary text/window browser regressions; initial hash mandatory before FIRST change |
| api | src/domain/inbox/initial-message* | any | intent/selection/renderer/state, exact scoped services and specs; no second Message or catalog owner |
| api | src/domain/inbox/conversation-start* | any | open/reuse and tests |
| api | src/domain/inbox/channel-window-policy* | any | one trusted-window query and its tests |
| api | src/domain/inbox/message-acceptance.service.spec.ts | any | same owner transaction and sender/echo contract |
| api | src/domain/inbox/conversations.service.spec.ts | any | list/open/empty/read effects |
| api | src/domain/channels/transport/channel*.spec.ts | any | union/fence/substitution architecture harness |
| api | src/integrations/channels/account-reference.ts | A, ?? | extract exact existing opaque hash helper |
| api | src/integrations/meta/initial-message.client*.ts | any | provider-private protocol preflight/text/template for new attempts inside same Meta Channel; old client interface preserved |
| api | src/surfaces/webhooks/meta.controller.ts | M | signed timestamp extraction only |
| api | prisma/migrations/*_initial_message*/migration.sql | A, ?? | additive intent/timestamp/index migration; no unrelated migration edit |
| api | test/initial-message* | any | real PG/BFF/PCV/scoped account and durability fault contracts |
| api | test/conversation-start* | any | open races and list SQL |
| api | test/atendimento.e2e-spec.ts | M | common BFF sender/window compatibility |
| api | test/webhooks.e2e-spec.ts | M | timestamp signature and origin/resource proof |
| web | src/componentes/NovaConversa* | any | local form/confirmation and tests |
| web | src/telas/Inbox.spec.ts* | any | composer/freshness/recovery regression |
| web | e2e/start-conversation.spec.ts | A, ?? | new real-BFF browser mutation flow |
| foundation | todos/active/features/TODO-leadshug-start-conversation-by-contact.md | M, D, R | contract and approved lifecycle closeout |
| foundation | todos/completed/features/TODO-leadshug-start-conversation-by-contact.md | A, ??, R | only after delivery gates |
| foundation | artifacts/reviews/leadshug-start-conversation-20261022/** | any | planning/review/implementation evidence |
| foundation | modules/inbox-and-conversations.md | M | stable contracts after approval/delivery |
| foundation | modules/integrations-and-channels.md | M | approved payload/window supersede after delivery |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | factual story sequence |
| foundation | backlog/README.md | M | current gate only |
| foundation | artifacts/dependency-readiness.md | M | redacted runtime readiness only |
| api | src/domain/inbox/message-acceptance.service.ts | M | Same acceptance owner tx-capable primitive and original-CAS ordering; existing bytes sealed in supplemental-source-seal-v1.1.json before first mutation |
| api | src/domain/inbox/dispatch-admission*.ts | A, ?? | Finite ordinary admission/exclusive-initial interlock and unit cases, no global operation platform |
| api | test/dispatch-admission*.e2e-spec.ts | A, ?? | Real PG interlock/expiry/owner-CAS/commit certainty barriers |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .local-files/** | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| api | .env* | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | .env* | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | .gitmodules | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | api-app | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | web-app | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| root | delphi-ai | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |
| web | dist/** | any | private/derived/pipeline-owned or methodology; no mutation or inspection of private surfaces |

### Initial inheritance admission
Closed68-file inventory: evidence/inherited-source-seal-v1.1.json. Before first implementation/test compare ALL68 hashes and3 product HEADs. Thereafter only specifically admitted paths may change for04; every remaining inherited record stays byte-exact. No broad discovery of private files. Root and source repositories remain principal single-checkout. Planned companion extraction shares the exact opaque account-reference algorithm without changing existing ST05 keys. Historical source files/receipts are never reclassified as new04 work.


## Bounded But Elastic Guardrails

- **May stay inside this TODO:** local details of open/reuse, bounded preview, initial attempt lifecycle, current account eligibility, and tests needed to prove this same first-contact flow.
- **Must update or split the TODO:** CRM/import, authoring/catalog changes, new transport/provider, automated sending, campaign or any global sender/idempotency redesign.


## Definition of Done

- [ ] **DOD-01:** opening invokes no automation; manual-open-without-send then first inbound leaves NOVA_CONVERSA false while keyword automation retains its predicate; authorized operator opens/reuses BU/contact atomically; no side effects listed in SCOPE-01 occur; new conversation has truthful empty state and deterministic list ordering.
- [ ] **DOD-02:** stale/foreign BU, actor, slot, selected channel, grant, credential epoch/version, conversation generation, template fingerprint, or policy context fails closed before external dispatch.
- [ ] **DOD-03:** Preview is escaped, deterministic, local/read-only and context-bound; supported textual subset and exact limits are enforced server-side.
- [ ] **DOD-04:** existing Channel consumers remain substitutable; Meta supports declared text/template kinds; Evolution template is typed unsupported with zero HTTP; no second send method/provider branching outside adapters or DI cycle; immutable descriptor plus same-operation fence preserves common dispatch.
- [ ] **DOD-05:** prove commit certainty at reservation/dispatch-claim/receipt/release, including real commit with lost ACK and real rollback; every remote eligibility/grant/phone GET completes before durable SENDING claim; the abstract fence CAS-claims immediately before one POST, and expiry of PREPARED during delayed preflight produces zero POST. Each initial attempt dispatches at most one POST; failures are classified truthfully; known provider ID is durably separate from local Message; recovery never contacts provider and never creates a Message without external ID.
- [ ] **DOD-06:** initial transaction locks identity then conversation, checks original pre-HTTP status/owner CAS before acceptance mutates updatedAt, permits eligible acceptance when status CAS fails, and recovers unique conflict by whole-local-transaction rollback/readback/re-entry at most once; MessageAcceptance remains sole Message owner and existing sender/error behavior is preserved; CAS prevents late initial outcome from changing concurrent claim/close/owner or reacquiring released slot. Initial acknowledgment in either allowed state waits for immutable dispatchDeadlineAt; before it409 ACK_TOO_EARLY and zero release.
- [ ] **DOD-07:** official window uses only qualified trusted Meta IN timestamp for selected resource; all current BFF/public/BOT availability and send policy consumers use the same rule; timeline/cursors and performance bounds hold.
- [ ] **DOD-08:** owner-scoped ordinary admissions and exclusive initial reservation serialize under the same conversation lock without serializing ordinary-versus-ordinary sends; uncertain dispatched tokens block initial reservation until settlement or explicit risk acknowledgment, never time takeover; late owner release cannot touch successor; existing composer is blocked before HTTP for new/empty/unresolved slot; public/BOT respect slot and retain existing mappings; text regressions pass.
- [ ] **DOD-09:** NAMED and POSITIONAL initial support is derived by the initial text renderer from the unchanged catalog components/format, independently of inherited authoring flags; exact full context binds management descriptor to selected transport and final text-window fence; current eligibility is checked before every new official template dispatch via bounded same-account reads; template is actually APPROVED; Meta request pins server-captured `messaging_account_id`, uses `+` plus full DDI, and preserves existing ordinary text semantics. Tests cover same-country and cross-country recipients. Official raw reference receipt confirms account pin and recipient formatting; actual own-account readiness remains unverified.
- [ ] **DOD-10:** per actor/account limits, tenant isolation, request/deadline budgets and zero-network recovery are demonstrated with real bounded counters/barriers.
- [ ] **DOD-11:** additive migration passes explicit preflight and disposable local validation without reset/drop; current source/image/API freshness and approved local validation topology are proven.
- [ ] **DOD-12:** assisted proof: operator sends first unofficial message, an actually APPROVED official template, receives a reply; no auto-contact; if eligible approved asset is unavailable, completion remains blocked.
- [ ] **DOD-13:** architecture/adherence/security/performance/TQA/final/cutover/debt and delivery guards pass at their required stages; no open P1/P2; constraints SEC-R6-04, OPS-R4-01, TQA-ST05-03 remain truthfully carried.


## Validation Steps

- [ ] **VAL-01:** include real PG integration open-without-send→first inbound with isolated NOVA_CONVERSA trigger (no bot start), separate PALAVRA_CHAVE fixture (retained), and no automation on open; after approval only, run contract/unit/dependency harness and exact existing BFF/public/BOT textual regressions; no test execution is part of this planning draft.
- [ ] **VAL-02:** initial acknowledgment before deadline rejects without release; at/after deadline permits only classified states, successor admission and late original result stay fenced; PostgreSQL race/barrier and fault injection for unique BU/contact creation, idempotent replay, delayed remote preflight vs PREPARED expiry with zero POST, claim immediately before POST, claim/close during HTTP, timeout/late provider result, ack/release then successor; assert provider counters and no lock-held HTTP; both ordinary/initial admission orderings, ordinary concurrency preserved, suspension before/after claim, uncertain token never expires into takeover, owner-CAS late release; real rollback/commit-ACK-loss at all four local boundaries; pre-acceptance CAS and echo-first conflicts.
- [ ] **VAL-03:** adapter substitution and raw protocol tests; Evolution template unsupported produces zero requests; Meta pages/status/account membership limits and same-account exact tuple are bounded; NAMED and POSITIONAL end-to-end order; closed-window template allowed, text-window expiry during preflight blocked, every descriptor/context dimension mismatch blocked before POST.
- [ ] **VAL-04:** signed webhook cases for valid, absent, malformed, future, nonofficial, duplicate and old timestamps; assert nullable provenance and unchanged timeline/cursors.
- [ ] **VAL-05:** same trusted-window policy across BFF/public/BOT availability and dispatch; EXPLAIN/query count for large OUT-heavy and no-IN histories; enforce batched consumer bounds.
- [ ] **VAL-06:** Playwright on freshly served React/Vite bundle + real BFF/PostgreSQL: open/reuse, preview, stale context, create/replay/read/reconcile/ack, safe errors, refresh, composer block, preserve draft, keyboard flow.
- [ ] **VAL-07:** migrations: explicit additive preflight, lock timeout 5s, statement timeout 60s, disposable TEST target, migration deploy/status and rollback assessment; never reset/drop or run before separate authorized implementation stage.
- [ ] **VAL-08:** local source-bound API/Web activation and owned stable/temporary HTTPS only under later approved runtime plan; assisted own-channel proofs as DOD-12.
- [ ] **VAL-09:** run appropriate architecture, critique, assumption/code, review drift, decision adherence, module consistency, security, performance/concurrency, TQA, final, cutover and completion guards after their proper lifecycle stages. Architecture planning r1 exists; other planning/delivery gates require their actual current artifacts. No implementation validation is claimed.


## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/inbox-and-conversations.md`
- **Secondary module docs:** `foundation_documentation/modules/integrations-and-channels.md`; completed ST-CON-05 owner TODO reference (no new template module).
- **Planned decision promotion targets:** inbox module first-send/open/recovery and trusted-window sections; integrations module Channel payload/capability and scoped resolver section.
- **Module decision consolidation targets:** same sections only after implementation and reviews; no module docs edited in this planning slice.


## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling (`Preserve|Supersede (Intentional)|Out of Scope`) | Evidence |
| --- | --- | --- | --- |
| inbox-and-conversations: BU/contact uniqueness | Conversation unique by BU+contact | Preserve | current Prisma source, exact anchor to be captured in fresh package |
| inbox-and-conversations: ST-CON-01 message acceptance | one MessageAcceptance owner; no exactly-once external/outbox | Preserve; narrow scoped transaction collaboration proposed | module handoff and current source |
| integrations-and-channels: ST-CON-06 Channel | one text sendMessage / adapter resolver | Supersede (Intentional) only text-only payload limit if C accepted | module ST-CON-06 contract and sealed source |
| integrations-and-channels: current window rule | latest IN stored createdAt, unfiltered by transport | Supersede (Intentional) with trusted official timestamp/resource selection | module ST-CON-06 handoff; exact code anchor pending freeze |
| integrations-and-channels: ST-CON-05 management/catalog | narrow separate management resolver + shared catalog projector | Preserve; remove duplicate route proposal | completed ST-CON-05 TODO and current files |
| ST-ATT-01 timeline | createdAt/cursor behavior and read acknowledgement | Preserve | inbox module contract |
| SEC-R6-04 / OPS-R4-01 / TQA-ST05-03 | delivered constraints/debts | Preserve | ST-CON-05 completed handoff; no cleanup in this slice |


## Decision Baseline (Frozen Before Implementation)

Proposta selecionada abaixo deve coincidir com o freeze publicado e os reviews atuais. APROVADO e authority pós-ingestão ainda necessários.

- [ ] D-01 — preserve BU+contact uniqueness and current grant; required 8–15 digit normalized DDI without country guess. No CRM/provider side effects on open. New conversation `QUEUED`, unread zero, lastMessageAt null; order empty rows by COALESCE(lastMessageAt,createdAt).
- [ ] D-02 — alternatives: **A)** a second `sendTemplate` Channel method (splits the abstract operation and adds obligations to every adapter); **B)** parallel concrete sender (bypasses scoped resolver/common acceptance); **C)** one `sendMessage` with discriminated text/template union and readonly `supportedKinds` (selected proposal). C intentionally supersedes ST-CON-06's delivered text-only payload while retaining one method. Avoid DI cycle: `TemplateManagementModule` already imports `ChannelTransportModule`, therefore `ChannelTransportModule`/`OutboundService` must not import or inject management. Initial orchestration composes both, reuses `listTemplates/getTemplate`, and passes a validated immutable provider-agnostic descriptor plus optional generic per-attempt dispatch fence through the same `sendMessage`; management port gets no send method. Meta send client completes its remaining grant/phone GETs, then calls the fence to CAS-claim immediately before POST, chained with current-context guard. No network/retry in fence/transaction, provider branching in domain/consumers, casts/`instanceof`, or generic plugin platform. Reviewer assesses substitutability, dependency/harness, blast, maintenance and performance.
- [ ] D-03 — initial-intent coordinator belongs to inbox; calls common `OutboundService` dispatch and sole `MessageAcceptanceService`. If needed, add scoped transaction collaboration to that owner while preserving current wrapper. Do not copy sender, acceptance or finalization into coordinator; no claim existing transaction integration already exists. Normative r1 explicit initial selection/context equality and payload/window-specific fence below are part of this decision.
- [ ] D-04 — new nullable officialInboundAt is written only from verified signed Meta IN timestamp passing positive integer/nonfuture/resource identity checks. No backfill. Window is max trusted IN on selected current resource and conversation `<24h`; same policy for sender and availability/batched BFF/public/BOT projections. Preserve createdAt timeline/cursors; use bounded index and retain ST06 index.
- [ ] D-05 — shared ST-05 catalog route/projector only. Preview route `POST /api/bff/conversations/:id/initial-message-preview` is local/read-only. Before each new template send, recheck same-account current asset by trusted observed name using existing `listTemplates`, at most two filtered pages, and require exhausted exact ID/name/language/semantic match; `getTemplate(id)` alone does not prove account membership. Official raw reference receipt confirms optional supported `messaging_account_id`; pin the server-captured account. Meta recipient wire format is `+` plus full DDI while domain identity remains canonical digits; no fallback/retry on rejection. Normative r1 initial renderer validates POSITIONAL independently of inherited authoring flags and fingerprints unchanged catalog components.
- [ ] D-06 — endpoints: `POST /conversations/:id/initial-messages`; `GET start-options`; `GET attempt`; authenticated `POST reconcile` and `POST acknowledge`. UUID per BU+actor; replay canonical request before provider reads after current grant check. PREPARED lease 90s. All remote asset/grant/phone preflight GETs complete before the SENDING claim; a generic dispatch-fence hook on the same `sendMessage` CAS-claims immediately before the sole POST. Expiry during preflight proves zero POST. Pre-dispatch failure rejects/releases; uncertain SENDING locks slot as AMBIGUOUS. Persist known external ID separately before local acceptance; recovery is local-only, with no fuzzy echo or missing-ID Message. Acknowledgment follows explicit classification and irreversibly releases; a late result cannot reacquire slot or mutate newer owner/status. Normative r1 transaction ordering and exact readback/one local re-entry applies. Initial risk acknowledgment for either allowed state waits until original persisted dispatchDeadlineAt=reservationDBtime+90s, never renewed; early409 ACK_TOO_EARLY.
- [ ] D-07 — composer BFF blocks new/empty/unresolved slot before any HTTP; public/BOT must honor same active slot before dispatch without global durable-intent conversion; preserve existing mappings outside this bounded change. O resultado novo é BLOCKED, code INITIAL_SEND_IN_PROGRESS, HTTP409, somente attemptId local autorizado e safe state; nenhuma rede. Sem slot, callers antigos seguem fluxo anterior. BFF /messages em conversa sem mensagem de transporte retorna INITIAL_SEND_REQUIRED409; API pública/BOT sem slot preservam seu fluxo próprio existente. Ver Dispatch Interlock abaixo. Normative r1 owner-token admission, no time takeover of uncertain dispatch and separate local-only token recovery applies.
- [ ] D-08 — template renderer supports text BODY NAMED/POSITIONAL, static header/footer only, <=20 params and stated length bounds. Preview binds exact conversation/contact/context/fingerprint, escaped and read-only. Catalog observation at most 300s is not send authorization.
- [ ] D-09 — maximum six GETs / one POST per new official template attempt, 10s each, 75s budget <90s lease; limits 10/min actor, 60/hour canonical account/resource. Official raw-contract receipt confirms account pinning and recipient formatting; actual account/asset readiness remains unknown. Disposable local TEST migration only after approval, explicit preflight, lock5s/statement60s, no reset/drop. Local proof sequence as DOD-12.
- [ ] D-10 — Certeza local: reserva, claim, persistência de ID externo/recibo e release de slot exigem confirmação positiva ou readback exato da chave capturada após erro de commit. Erro Prisma não prova rollback. Sem confirmação de claim original não há POST; persistência incerta não libera slot nem admite nova tentativa. ACK externo conhecido permanece CONFIRMED e nunca vira recusa por falha local. Persistência do fato/Message e projeção/realtime são dimensões separadas, sem falso RECORDED. Provar rollback real e commit real com perda do ACK em cada fronteira com PG, sem protocolo genérico de operações. Hash opaco canônico de conta usa o namespace existente meta-waba+NUL+accountId; extrair helper de integração preservando bytes/ST05observations, e expor só referência opaca no contexto do canal, nunca aceitar accountId do browser.


## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability:** `required`
- **Why this applies:** contract introduces durable first-send ownership and intentionally proposes two narrow supersedes to Channel payload and official-window timestamp truth.
- **Deviation / debt being retired:** split/missing first-send lifecycle; current timestamp selection can use unrelated stored IN; Channel's delivered payload is text-only.
- **Target steady-state after closeout:** one Channel send abstraction; one common Outbound dispatch; sole MessageAcceptance owner; one template-management/catalog owner; one initial-intent coordinator; current selected resource's trusted official window; monotonic attempt and slot recovery.
- **Temporary exceptions allowed:** none proposed.
- **Cutover / removal condition:** no duplicate channel/template routes or send owners; only after all current callers and projections share the approved policy and regression matrix passes.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Channel operation selected through abstract resolver | ST-CON-06 module contract | adapters/domain | provider choice remains scoped and substituted by contract |
| one MessageAcceptance owner keyed by external ID | ST-CON-01 module contract | all new Message writes | sender/echo converge without duplicate owner |
| shared ST-05 projector and management capability | ST-CON-05 completed TODO | catalog reads | one observation/freshness authority |
| transaction-free provider I/O | ST-CON-05/06 contracts | all HTTP | DB locks never span network calls |
| idempotent local intent, no external exactly-once claim | this proposed contract | initial attempts | uncertainty cannot become blind resend |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why Forbidden | Exception Policy |
| --- | --- | --- | --- |
| second Channel send method or parallel sender | API/adherence search and dependency contract | splits abstract transport/common acceptance | none unless renewed approval |
| provider if/instanceof in domain/consumers or casts | architecture guard/grep/code review | leaks concrete provider details | none |
| duplicate catalog projector/route/cache/DTO owner | route/DI/dependency tests | splits ST-05 ownership | none |
| fallback to alternate connected channel | resolver/request test | may dispatch under unconfirmed account | none |
| timestamp fallback to createdAt/raw/import/nonofficial | window tests/code inspection | manufactures 24h eligibility | none |
| automatic retry/fuzzy match/missing-ID Message | fault-injection tests | may duplicate external contact | none |
| HTTP inside DB transaction or hidden extra probe | request counter/transaction barriers | violates bounded latency/locks | none |
| generic future provider/plugin framework | architecture review | adds unrequested platform | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| dependency/substitutability tests | Channel/factories | existing harness plus new typed-kind cases | concrete branching, new required methods, wrong support declaration | implement-in-this-TODO | contract and fake tests |
| adapter protocol tests | Meta/Evolution | request recorder, no live provider | extra/unbounded HTTP; Evolution template HTTP | implement-in-this-TODO | exact counters and payload fixtures |
| architecture/adherence check | inbox/integrations | canonical project guard after freeze | duplicate owners, provider leak, wrong route owner | implement-in-this-todo | post-implementation review |
| DB race/fault harness | attempt/slot/Message | PG barriers and CAS checks | duplicate POST, slot reacquisition, status/owner steal | implement-in-this-TODO | real disposable PG |
| schema/migration gate | Prisma | migrate deploy/status with bounded preflight | destructive or blocking migration | implement-in-this-TODO | authorized local DB only |
| consumer regressions | BFF/public/BOT/Web | existing API/E2E/Playwright suites | broken text send/window/timeline/UI recovery | implement-in-this-TODO | exact commands after approval |


## Audit Trigger Matrix

- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/audit-floor-after-architecture-v1.1.json; actual guard GO with high review issue signal; finite deadline/automation clarifications do not change trigger matrix; no implementation audit claimed.

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
| high_severity_plan_review_issue | yes | escopo ST-CON-04; derivar após freeze |
| explicit_three_lane_request | no | escopo ST-CON-04; derivar após freeze |


## Security Risk Assessment

- **Risk level:** high
- **Why this risk level:** cross-tenant first-contact external side effect, account selection, credentials and irreversible ambiguity.
- **Attack surface in scope:** session/CSRF, BU/contact/channel/template/account/attempt IDs, parameter renderer, stale contexts, payload/key/rate limits, sender-slot races.
- **Attack simulation decision:** required
- **Review evidence:** Actual E64 negative synthetic scenarios and source-bound map evidence/security-candidate-map-e64-v1.1.json reviewed by architecture/security r4. Three new source-supported claim/lock/query hypotheses require safe causal simulation; see implementation-r4-finding-triage-v1.1.json. No live provider/runtime query performed.
- **Residual security risk:** private existing local cohort only. Delivered SEC-R6-04 recovery-budget debt remains outside04;04 recovery does no external reads. OPS-R4-01 and TQA-ST05-03 retain their dispositions. A fresh current approved template is not presumed.


## Performance & Concurrency Risk Assessment

- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** escrita externa e concorrência com webhook e UI.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | running | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | running | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-E3 | running | external ambiguity explicit | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E1 | running | none | none |

### Lane Detail Packet Template
#### EPS
- **Trigger rationale:** listagem de conversas vazias/ordem e lookup scoped/intenção; EXPLAIN ANALYZE com amostra cardinalidade, limite de página e budget externo. Sem N+1/catalog fan-out.
- **Recorded at (UTC):** 2026-10-22T23:00:47.612421+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-eps-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `08138da3019c4a4269e82701d38732f84fcd7ae0476c37127e84257b7c868ab5`; sample EPS-SP-STRONG; acceptance EPS-A2. Independent assessment pending; no delivery/runtime/provider claim.

#### FRC
- **Trigger rationale:** duas submissões e atraso em troca BU/canal/draft; Playwright real, rastrear requests e estado no backend.
- **Recorded at (UTC):** 2026-10-22T23:00:47.620028+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-frc-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `994c5487144cd1be2301b4099b0c7d05af4f88aa5955b9441e5b9910736f0e4a`; sample FRC-SP-H; acceptance FRC-A1. Independent assessment pending; no delivery/runtime/provider claim.

#### BCI
- **Trigger rationale:** barreiras PG e contador HTTP externo, crash antes/depois POST, replay e echo; provar invariantes D-06/07.
- **Recorded at (UTC):** 2026-10-22T23:00:47.626397+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-bci-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `c505c53965ac7a15999d0f91915e75dac1fac6e9c3a0fca6694a3078f54aa5f2`; sample BCI-SP-H; acceptance BCI-A1. Independent assessment pending; no delivery/runtime/provider claim.

#### RLS
- **Trigger rationale:** pequeno ensaio de concorrência/load bounded do novo fluxo/listagem no PG descartável; não claim SLO ou produção.
- **Recorded at (UTC):** 2026-10-22T23:00:47.632810+00:00
- **Executor ID:** stcon04_continuation; root-independent-source-and-output-collector
- **Evidence object:** candidate actual execution: `artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-rls-e54-v1.1.json`; schema pcv-1; run E54-canonical-all-2734; SHA256 `25f71eadd5ac094b794fbf1ffb694a49d3031791486f4cb473537d08698c7fb8`; sample RLS-SP-L; acceptance RLS-A1. Independent assessment pending; no delivery/runtime/provider claim.


## Verification Debt Assessment

Required at closeout. Explicitly carry ST-05 `SEC-R6-04`, `OPS-R4-01`, and `TQA-ST05-03` as accepted delivered limitations unless the owning TODO changes them. No backlog fix is admitted here. Record newly found debt and owner before Completed; no claim that it was cleared by this plan.


## Approval

- **Approval status:** approved — APROVADO
- **Approver:** current human user/task authority
- **Approval reference:** user reply “APROVADO” on2026-10-22 after current reviewed ST-CON-04 request; evidence/approval-execution-admission-v1.1.json; reviewed Foundation fbbdfa6fd4faf3a1d4cdb62297a06e57676d9cd3
- **Approval scope:** ST-CON-04 v1.1 SCOPE-01..12 and D-01..10 including normative architecture-r1/critique-r1 contracts, strict file admission, local-only validation/activation sequence and every required delivery gate. Supplemental human validation E23 admits ONLY the two exact test fixture adjustments in window-fixture-companion-admission-v1.1.patch (SHA c35143d98838f25e7b44eafd24085ca5dd08b8869985120c6125a14359f07957), reply “Validar os dois ajustes de teste”. No delivery or provider success is inferred.
- **Exclusions:** all existing Out of Scope constraints remain; no private file/data inspection, automatic real recipient actions, product Git/promotion/Railway, worktrees/auxiliary copies, unrelated debt fixes or implicit broader exposure.
- **Renewed-approval trigger:** material scope/decision/API/schema/validation change, strict path deviation, new private/public exposure or independently testable objective outside the approved journey.


## API Endpoint Definitions — proposed ST-CON-04 v1.1

All new routes are BFF session routes, BU/conversation resolved server-side. ATENDENTE+ means current BU grant; missing session401, insufficient known BU403, inaccessible conversation/channel/attempt404. Every POST requires CSRF; strict unknown-field rejection/UUID parsing. Never accept protocol URL/token/account ID, foreign BU context or arbitrary Graph payload.

| Method / path under /api/bff | Request / effect | Safe response |
| --- | --- | --- |
| POST /business-units/:buId/conversations/open | required telefone string max40, DDI explicit; normalize only spaces/parens/hyphen/dot and optional initial +; digits8..15 firstnonzero; current local ready-channel metadata required only for new row |201 created or200 reused: {conversaId,criada,contact}; no external I/O, no read/claim/status side effect |
| GET /conversations/:id/start-options | observational local channel capabilities/readiness/window and one active attempt+up to10recent ordered by createdAt/id; separate truncated flag |200 safe channel generation/epoch/credential-version metadata and attempt IDs; no credentials, keys or external I/O |
| POST /conversations/:id/initial-message-preview | channelId UUID, expectedGeneration positive integer, mensagem typed text or template with templateId/language/catalogAfter?/expectedDefinitionFingerprint/parameters |200 rendered text and context-bound request fingerprint; local reads only, no persistence/network; stale or unsupported409 |
| POST /conversations/:id/initial-messages | same immutable message payload plus preview fingerprint; Idempotency-Key UUID; explicit selected channel, expected generation |201 new locally accepted result;200 replay terminal;202 active lease;409 blocked/conflict/ambiguous with safe attemptId/state;503 local or remote inconclusive; no recipient-delivery claim |
| GET /conversations/:id/initial-messages/:attemptId | observational scoped lookup, no browser key needed |200 safe state/provenance/local persistence/action metadata; no effects or external I/O |
| POST /conversations/:id/initial-messages/:attemptId/reconcile | empty body; same persisted attempt; current authorization, CAS |202 live lease;200 local classified/recovered state; expired PREPARED closes undispatched, expired SENDING becomes uncertain; zero external calls |
| POST /conversations/:id/initial-messages/:attemptId/acknowledge | empty body; explicit operator confirmation of duplication risk |200 irreversible slot release only for AMBIGUOUS/EXTERNAL_ACCEPTED_LOCAL_BLOCKED and DBnow >= original persisted dispatchDeadlineAt; before deadline409 ACK_TOO_EARLY + eligibleAt, no release; repeat already released idempotent; no resend/outcome rewrite |

Shared catalog continues existing GET/POST /business-units/:buId/channels/:channelId/message-template-catalog with its existing exact DTO/owner/lease/fence. No second templates route. Renderer preview never authorizes dispatch: fresh same-account eligibility and current grant/context/window are checked again for a new attempt.

**Field Definitions**
- Initial state: PREPARED (no dispatch claim), SENDING (durable claim, external result may be unknown), EXTERNAL_ACCEPTED (known external ID; local work may remain), EXTERNAL_ACCEPTED_LOCAL_BLOCKED (known acceptance, current identity/fence prevents local finalization), SUCCEEDED (Message persisted; delivery not implied), REJECTED (proven pre-dispatch or proven external refusal), AMBIGUOUS (dispatch outcome unknown).
- Slot: active while no slotReleasedAt; release is irreversible independently of outcome. One active row per conversation by partial unique index/transactionally equivalent constraint.
- Provider acceptance: CONFIRMED only with captured valid ID; otherwise UNKNOWN. receiptPersistence/localMessageState: RECORDED only after positive commit or exact readback; otherwise UNCONFIRMED. No failed DB ACK becomes REJECTED by inference.
- Content: TEXTO text1..4096; TEMPLATE reference to currently observed supported MARKETING/UTILITY, language max16 and remoteID max128, exactly matching NAMED keys or POSITIONAL1..N; maximum20 values1..1024 and rendered snapshot4096. No components outside text BODY and static TEXT header/footer.
- Channel contract: one sendMessage with text/approved-template discriminant and supportedKinds; optional generic dispatch fence is awaited once after remote preflight, directly before POST. Unsupported kind is BLOCKED/UNSUPPORTED_KIND with zero external requests. Domain receives no token/phone protocol address/raw account ID.


## Dispatch Interlock and Transaction Boundary — proposed

The new initial coordinator reserves an intent and immutable request/scope, not a Message. Common OutboundService alone resolves/binds the abstract channel and performs dispatch; common MessageAcceptanceService alone creates/reconciles keyed Message. Extend that SAME acceptance owner with an explicit tx-capable primitive, keeping its existing accept wrapper. A shared Outbound finalization collaboration consumes it for initial local acceptance/intent state/CAS effects in one short transaction, preserving the existing sender wrappers. Initial orchestration composes transport and management modules; transport never imports management, preventing a DI cycle. The Meta initial protocol client is an integration detail of the SAME bound Meta Channel, never a parallel application sender.

Before every ordinary dispatch and exclusive initial reservation, use the owner-token admission defined in the normative r1 integration below. The earlier lock-or-lease alternative is closed; no time takeover of uncertain dispatched tokens and no ordinary-versus-ordinary serialization.

For a new initial attempt, all provider preflight reads precede its SENDING claim. The same-method fence rechecks live user/grant/channel/resource/generation/epoch/active credential and payload fingerprint in the short claim transaction. A failed/expired PREPARED claim does zero POST. Positive original-claim commit/readback is the only dispatch authority. Exactly one POST per attempt; no transport mutation retry. A fresh independent credential/account/template preflight remains outside the transaction. This fence constrains local authority and cannot retract an HTTP call already accepted externally.

Only an active initial slot holder may finalize status/owner via CAS against pre-HTTP updatedAt/state/owner; explicit concurrent claim/close wins. Late accepted outcomes may add the exact original receipt/Message via same acceptance owner when current fence permits, but never reclaim a released slot, steal owner or reopen a later close. Unknown outcomes stay in the intent, not a Message without ID. Sender/echo reconciliation uses exact providerResourceIdentityId+externalID, not text/time/contact heuristics. Readback and reconcile are observational/local respectively; neither repeats provider I/O.


## Normative architecture r1 integration — exact bounded contracts

This section is part of SCOPE-02/04/06/07/08/09/10 and D-03/05/06/07/10; it resolves ARCH-R1-01..04 and overrides earlier open-ended interlock alternatives, never the private boundary. These are proposed contract changes awaiting human APROVADO.

### Ordinary admission and exclusive initial reservation

Use a small durable per-send `DispatchAdmission` record for ordinary sends, separate from initial-message intent. Fields: id/token, conversation/BU, caller kind and current attributable actor, immutable selected context, owner nonce, `PREPARED|SENDING|SETTLED|UNCERTAIN`, deadline and irreversible releasedAt. This record authorizes exclusion only; it is not ordinary-send idempotency, retry, Message acceptance, provider lookup or a second operation owner. Every BFF/public/BOT dispatch obtains its own token under the SAME conversation row lock used by initial-slot reservation. Existing ordinary tokens can coexist; ordinary-versus-ordinary concurrency and response mappings remain unchanged. Any unreleased ordinary token blocks initial reservation; active initial slot blocks admission of a new ordinary send. Initial and ordinary admissions never pass each other through a SELECT race.

Ordinary PREPARED admission has 90s deadline; bounded provider preflight completes before a same-operation fence validates current owner/context/applicable trusted window and positively commits SENDING. If expiry wins while still PREPARED, classify/release as undispatched and fence produces zero POST. No automatically released dispatched token: SENDING expiry, process death, timeout or missing provider ID becomes UNCERTAIN and still blocks INITIAL reservation. Known accepted/refused/blocked result settles only that owner's token; unknown result keeps the token while existing caller outcome/diagnostic behavior remains unchanged. No automatic retry or provider recovery is added. All normal finally/catch release uses token+owner CAS; a late release never releases an initial slot or another owner's token.

A small local-only recovery surface exists solely to unblock initial admission: `GET start-options` adds up to10 active ordinary admissions plus truncated flag; `POST /conversations/:id/dispatch-admissions/:admissionId/reconcile` locally closes expired PREPARED or classifies expired SENDING, and `POST .../acknowledge` irreversibly releases only UNCERTAIN after its 90s dispatch deadline, current ATENDENTE+ and CSRF, with explicit duplicate-risk confirmation/audit. Never expose service principals/foreign state. Acknowledgment cannot cancel an already-claimed HTTP request; suspension after the fence or late response can still cause an external effect, which is the stated risk, not a guarantee. It never retries or changes ordinary response/Message. Known result can subsequently settle only its original token; release remains irreversible. Initial reservation seeing active token returns BLOCKED/ORDINARY_SEND_IN_PROGRESS409 with authorized local token IDs; missing/unconfirmed admission or SENDING commit means zero POST. Exact captured-key readback, no inference of rollback from an exception, applies to reserve/claim/settle/release. Local readback inconclusive keeps exclusion conservative.

Admission rows live in the same short conversation transaction as exclusive-slot checks, but never hold DB locks over HTTP. Rate limits and active-token read bounds apply; bounded row/index queries only. Preserve caller compatibility outside this narrowly reviewed admission change. Tests prove both orderings, multiple ordinary sends remain concurrent, suspension before/after fence, PREPARED expiry vs late fence, uncertain dispatch without time takeover, manual risk release, successor and late owner-CAS release. This finite recovery is included here, not delegated to an unspecified future interlock.

### Initial resolution and dispatch descriptor

Add narrow abstract `resolveForInitial` reference to ChannelResolver: current conversation/BU, explicit selected channel, expected immutable channel/resource/generation/epoch/credential-version/account-reference context and message kind. Resolve explicit channel, never infer latest origin or fallback. Approved-template resolution does not apply the free-text window; text resolution and final claim do. Existing ordinary resolver methods preserve current semantics except the explicitly superseded qualified window rule.

Initial coordinator composes transport and management and gives common dispatch an immutable descriptor containing normalized recipient from the stored conversation, complete scoped channel context, payload kind, exact template ID/name/language/category/format/canonical text components and ordered/keyed parameter values, rendered snapshot and request fingerprint. Validated management context MUST equal selected transport context in BU, channel, resource identity, opaque account reference, generation, pairing epoch and active credential version. Browser provides neither account/protocol address nor a credential. Keep transport independent of management DI. Fresh exact same-account definition/status verification completes first; generic same-send fence then verifies current user/grant, full context equality, immutable payload fingerprint, slot/owner/deadline and applicable trusted text-window at claim time, immediately before one POST. Window expiry during preflight rejects text before dispatch; closed-window approved template remains allowed. External status can change after check; provider refusal is not converted to success/fallback/retry.

### Transaction ordering and local recovery

Keep the known external receipt committed separately before local Message work. Reuse `MessageAcceptanceService.acceptInTransaction` (proposed name) as SAME owner primitive; current `accept` remains wrapper with its existing observable behavior. Initial short local completion obtains current verified-identity lock first, BU/contact advisory lock where required, then conversation row lock, then intent/admission rows in that order; no reverse acquisition in new collaborators. Under that row lock evaluate ORIGINAL pre-HTTP updatedAt/status/owner + active initial-slot CAS BEFORE acceptance's own lastMessageAt/updatedAt mutation. Capture the boolean; do not refresh expected values from a newer/echo-first conversation. A false status/owner CAS skips those effects but does not reject an otherwise eligible keyed Message. Same owner accepts/reconciles exact resource+external ID, and same transaction records initial completion and slot release. Echo-first may conservatively suppress assignment/reopen; never steal/reopen on a newly captured baseline.

Unique conflict aborts the entire local transaction. Do not query/reconcile inside an aborted transaction. After rollback, exact positive readback of receipt/Message/intent then at most ONE fresh whole-local transaction may reconcile through the same primitive and original CAS context; no external call. Commit-ACK loss first uses exact readback; if still unconfirmed, keep truthful CONFIRMED external acceptance, UNCONFIRMED local projection and unreleased slot. Local-only later reconcile can resume after current identity/grant checks. Old wrapper's acceptance/error/unknown mapping stays covered. Realtime emits only for the Message creation winner after confirmed local commit; crash-gap remains best-effort (no outbox claim).

### Initial template subset over unchanged ST-05 catalogue

The delivered `supported`, `eligible` and `semanticFingerprint` fields describe ST-05 authoring support and mark POSITIONAL unsupported. They are preserved byte/semantics-compatible and are NOT authorization or complete initial-send support flags. New initial text renderer consumes existing sanitized `TemplateSummary.components`, `parameterFormat`, account-bound observation freshness/availability/status and exact ID/name/language/category. It validates its own strictly narrower text-send grammar: one BODY, max one static TEXT HEADER and FOOTER, no other/unknown component, no placeholder in header/footer; NAMED unique keys or POSITIONAL contiguous keys1..N with repeated occurrences mapped consistently. Every supplied value must exactly match the required names/positions and existing bounds. Unknown/unsupported syntax fails closed. This renderer is not a second catalogue/projector and writes no remote observation.

Derive an initial-only semantic fingerprint from a fixed canonical versioned representation of the existing sanitized ID/name/language/category/parameterFormat/text components, then combine context, recipient and ordered/keyed values into preview/request fingerprint. Do not reuse null ST-05 positional fingerprint or silently treat eligible=false as send permission. Initial UI labels subset support based on this same renderer/preview, not inherited authoring flags. Fresh bounded same-account reads pass through the SAME renderer and must exactly match selected initial semantics and APPROVED status before POST. No shared parser/DTO/authoring change admitted. If actual raw semantics cannot be represented unambiguously by sanitized components, reject that template rather than broaden parser scope. End-to-end POSITIONAL and NAMED catalog→preview→fresh-check→wire-order tests are required.


## Normative critique r1 integration — acknowledgment and automation

**Initial deadline:** reserve PREPARED with leaseExpiresAt = reservation DB timestamp +90s. The successful original SENDING claim persists dispatchDeadlineAt equal to that same leaseExpiresAt; never extend or reset either timestamp during replay/read/reconcile/failure classification. All preflight and claim must fit before expiry. This original deadline governs initial risk acknowledgment; it does not promise remote cancellation.

For a never-released initial attempt, acknowledgment requires current authorization/CSRF, classified AMBIGUOUS or EXTERNAL_ACCEPTED_LOCAL_BLOCKED, captured non-null dispatchDeadlineAt and database time at/after it. This uniform timing applies even to a confirmed external acceptance blocked locally: no earlier exception. Before it, return409 ACK_TOO_EARLY with safe eligibleAt and leave slot/outcome unchanged. Unknown transaction/readback never supplies release authority. After it, explicit duplication-risk confirmation may irreversibly release; a request paused after claim may still produce a late external effect, so this is knowingly accepted risk, never a cancellation guarantee. Repeat acknowledgment on a previously released attempt is idempotent; late improvement of that attempt cannot reclaim its slot or alter successor state. Reconcile before deadline does not expire a live SENDING claim; an explicit transport timeout may already classify AMBIGUOUS but still cannot be acknowledged early. Cases at deadline-1ms, equality, +1ms, PREPARED with no claim, active SENDING, both classified states, lost release ACK, successor and late original response must be tested.

**Automation preservation:** current IncomingService calls NOVA_CONVERSA with acceptance.conversationCreated, not 'first inbound ever'. Manual open creates the row without any bot/provider side effect. A later first inbound into that manually opened empty row therefore does not fire NOVA_CONVERSA, even if the seller abandoned the draft. Keep that delivered predicate; no new first-inbound semantic, automation execution on open or trigger migration is admitted. Keyword automation retains its current matching predicate. Add focused real-PG/domain integration fixtures: open-without-send then first inbound with only NOVA_CONVERSA configured produces no bot start; the corresponding keyword trigger still matches. Browser validates open/readback without automation. No production automation behavior change beyond the explicit consequence of manually creating the conversation.


## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces

Candidate only: inbox domain/services/schema, BFF and inbound webhook boundary, Channel abstract contract and concrete adapters/resolver, Meta template protocol adapter, React Inbox, focused contract/E2E/Playwright harness. Exact proposed admission is in the strict inventory, including r1 supplemental acceptance-owner seal; any further deviation returns to review. No template authoring/catalog owner, no credentials/config, no runtime routing changes.

### Ordered Steps

1. Freeze this v1.1 TODO and sealed baseline through root-owned Foundation workflow; preserve the v1.0 archive untouched.
2. Fresh architecture opinion challenges D-01..10 and compares A/B/C with cost, risk, blast radius, maintenance, performance, elegance and structural quality.
3. Fresh independent critique; integrate findings in TODO and regenerate only affected package; run assumption/code and scope-drift guards. All statuses are not_run until actually produced.
4. Use the verified official raw contract: pin the server-captured `messaging_account_id`, format Meta recipients as `+` + full DDI, keep storage/domain identity provider-neutral digits, and test same-country/cross-country plus existing ordinary text semantics. Never fallback/retry if pinned request is rejected.
5. Human explicitly approves the converged v1.1, then authority guard must return go before implementation begins.
6. Operational/Coder implements admitted exact paths; keep all sealed non-admitted bytes exact, no worktrees or second writer.
7. Additive migration only after explicit candidate/environment preflight on approved disposable TEST DB, lock timeout 5s, statement timeout 60s; no reset/drop.
8. Run targeted domain/contract/PG tests and full existing BFF/public/BOT regressions; Playwright fresh bundle against real backend; bounded counters and performance evidence.
9. After candidate GREEN and runtime provenance assurance, run own local channel checks and assisted unofficial/official APPROVED/reply proof. If no eligible asset exists, do not claim complete.
10. Fresh delivery assurance/reviews/guards, reconcile stable module decisions and closeout only after all criteria have exact evidence.

### Test Strategy

- **Strategy:** test-first
- **Why:** irreversible external side effects, shared dispatch contract and concurrency require causal fail-first proof.
- **Fail-first targets:** open/reuse authorization and races; typed unsupported zero HTTP; trusted resource window; intent/dispatch/readback fault barriers; real-BFF initiation/recovery browser flow. Capture RED after approval and before the corresponding production change.

No implementation tests have been run for this planning draft. Future tests are those in VAL-01..09, including substitutability, zero-HTTP negative case, PG barriers, one-POST counters, signature/timestamp provenance, current account list membership, endpoint ACL/CSRF, consumer regressions, freshness and real browser mutation. Never substitute mocks for the required real BFF/PG flow or an actual approved-asset proof.

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 open/reuse + empty list | creates persisted conversation; changes list projection and NOVA_CONVERSA behavior on later first inbound | web-only | Playwright mutation | yes | yes | start-conversation.spec.ts with real BFF/PG, parallel open/readback, truthful empty list and open-without-send→first inbound NOVA_CONVERSA/keyword fixtures | n/a |
| DOD-03/09 catalog and preview | safe DTO, rendered text, freshness, current supported template | web-only | Playwright mutation | yes | yes | existing shared catalog + preview request counter, persisted observation fixture and escaped DOM | n/a |
| DOD-02/04/05/06 initial send | external effect, persisted outcome and conversation ownership | web-only | Playwright mutation | yes | yes | real BFF/PG and protocol-bound fake, exact POST counter, ID/Message/owner readback | n/a |
| DOD-05 recovery/reconcile/ack | safe state/actions persist after reload; irreversible slot release | web-only | Playwright mutation | yes | yes | timeout/ACK-loss fixtures, reload, local reconcile/ack before/after immutable deadline, late-result barrier | n/a |
| DOD-07 qualified window | affects options/composer and public/BOT send eligibility | web-only | Playwright mutation | yes | yes | signed-provider fixture and selected resource, boundary timestamp, unchanged timeline/cursor | n/a |
| DOD-08 ordinary composer interlock | send must block on initial activity, preserve normal text callers | web-only | Playwright mutation | yes | yes | backend races/counters and real browser error/recovery; API/BOT contract tests | n/a |
| DOD-10/11 rate/schema/runtime | safe errors and persisted state; served bundle must match source | web-only | Playwright mutation | yes | yes | migration/provenance + tenant/rate test fixture and refreshed served bundle | n/a |
| DOD-12 own unofficial and approved official | actual channel capability, provider acceptance and recipient reply | web-only | Playwright readonly | no | yes | later explicitly authorized operator first-send + reply, own preserved local source-bound runtime | operator performs actual sends; no browser automation contacts real recipients |

### Frontend / Consumer Matrix

| Producer / contract | Existing consumer / owner | Required preservation or deliberate change | Planned proof |
| --- | --- | --- | --- |
| conversation open/list | React Inbox + BFF conversations controller | no implicit send/read/claim; empty ordering based on COALESCE, stable createdAt/id | PG contract + real browser create/reuse/list |
| shared template catalog | Inbox selector + delivered Modelos | same ST-05 DTO, projector, lease/fence/TTL; authoring behavior stays sealed | catalog dependency and inherited authoring regressions |
| preview/new attempt state | new NovaConversa + Inbox | explicit channel; context generations and draft ownership; escaped rendering | real-BFF Playwright A-B-A/role revoke/late response |
| attempt read/reconcile/ack | recovery controls | local state only; no credentials; irreversible release and duplicate risk stated | real PG/readback + browser reload/recovery |
| Channel.sendMessage | common OutboundService + bound Meta/Evolution/fakes | one operation; text regression; declared kinds and unsupported zero HTTP | substitutability/dependency/raw protocol |
| common outbound dispatch interlock | BFF /messages, public API, incoming BOT | same shared dispatch boundary; typed safe block while unresolved; existing outside-slot mappings | parallel PG barriers + endpoint/BOT regressions |
| signed officialInboundAt | sender policy + availability projections | one trusted current-resource rule, batch/index bounds; no createdAt fallback | signed timestamp cases, API DTO and browser options |
| keyed MessageAcceptance | sender and verified provider echo | sole owner, exact identity/externalID dedup; no missing-ID Message for new flow | PG dual-order barriers and realtime winner count |
| manual-open row creation then first inbound | IncomingService / Typebot trigger | opening invokes no automation; NOVA_CONVERSA remains tied to actual row creation, so manual-open empty row means false on subsequent inbound; keyword rule preserved | PG integration and real-BFF open/readback; isolated new-conversation/keyword trigger fixtures |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status (completion projection) | Evidence Artifact / Command | Status (authority projection) | Notes | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| api / lint/build/unit/PG | schema/domain/adapters/BFF/webhook | bash scripts/test-channels-local.sh all | Local-Implemented | planned | api-app/test/initial-message*.e2e-spec.ts; new source-owned unit/adapter suites | planned | no test run during planning | open/contact/slot/claim/ACK loss/echo/CAS/account/qualified window and existing public/BOT/BFF regressions | own disposable Node22/PG16; bound fake external provider; real BFF/PG; concurrent actor/BU/tenant/account cases |
| web / build/unit/Playwright | new manual initiation and recovery | bash scripts/test-channels-local.sh all | Local-Implemented | planned | web-app/e2e/start-conversation.spec.ts (new) and inherited suites | planned | source-owned mutation and readonly journeys | open/reuse/preview/explicit channel/text/template/refresh/reconcile/ack; stale A-B-A and role revocation | same disposable BFF/PG; new rebuilt served bundle attested before browser; fake external boundary only |
| root / canonical parity and public boundary | existing runner remains execution owner | bash scripts/test-channels-local.sh all | Local-Implemented | planned | scripts/test-channels-local.sh; scripts/check-channels-ci-parity.py | planned | inherited scripts stay byte-exact; already use public inventory | full suite ownership/bootstrap/build/cleanup/provenance, no .local-files traversal | existing owned validation namespace only; no actual env/private read |

### Runtime / Rollout Notes

No config/credential/routing mutation during planning. Future local proof only after candidate GREEN, disposable migration assurance, source/image/runtime binding and approval. Owned local HTTPS origin only. No public/Railway promotion authorized.



## Bounded unchanged canonical module context: foundation_documentation/modules/inbox-and-conversations.md

Full-file SHA256 `24b3f1edd8f10bf991d61135be2364b49679c43e5894ce024c2d5169921756a2`. Complete applicable module decisions are embedded in the exact approved TODO baseline above; this concise context is a faithful summary of unchanged supporting module material.

Bounded unchanged supporting summary: this module defines Inbox/conversation ownership, timeline and message responsibilities, including ST01 acceptance and ST06 window behavior. The complete ST04-relevant module decision snapshot and supersession mapping are reproduced in the approved TODO contract above. Detailed timeline paging material is outside this initial-send audit slice; this package does not waive or alter it.

## Bounded unchanged canonical module context: foundation_documentation/modules/integrations-and-channels.md

Full-file SHA256 `6b1865ab4f27458e1e1e225535e2f4a713e987e18344ca86d3f9411fa6c6f168`. Complete applicable module decisions are embedded in the exact approved TODO baseline above; this concise context is a faithful summary of unchanged supporting module material.

Bounded unchanged supporting summary: this module defines channel invariants, abstract transport ownership, and template-operation responsibilities relevant to dispatch admission and outbound delivery. The full ST04-relevant module decision snapshot, preserved ST05 constraints, and explicit ST06 supersession mapping are reproduced in the approved TODO contract above. Unrelated provider onboarding and template lifecycle details are unchanged and outside this audit slice.

Trace every legacy BFF/PUBLIC/BOT consumer to the common trusted window and outbound interlock. Check there is one Message owner and one abstract send method; distinguish authorized ordinary-vs-initial compatibility behavior and the private initial Meta preflight from unapproved fallback/dual policy stitching. Module consolidation is still a later explicit gate; historical ST05 decisions must not be rewritten as if they originally permitted sends.

## Bounded source and original-seal classification


### api-app/src/domain/channels/transport/channel.ts

SHA256 `49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import type { TemplateManagementContext, TemplateSummary } from '../../message-templates/template-management.ports';
import type { Prisma } from '@prisma/client';

export type ChannelOrigin = 'OFICIAL' | 'NAO_OFICIAL';

export type ChannelAvailabilityReason =
  | 'CANAL_AUSENTE'
  | 'CANAL_AMBIGUO'
  | 'CANAL_SELECIONADO_INDISPONIVEL'
  | 'CHANNEL_IDENTITY_NOT_VERIFIED'
  | 'CHANNEL_NOT_READY'
  | 'PENDING_CREDENTIAL'
  | 'JANELA_FECHADA'
  | 'UNSUPPORTED_KIND';

export type ChannelSendResult =
  | { outcome: 'ACCEPTED'; externalMessageId: string }
  | { outcome: 'BLOCKED'; reason: ChannelAvailabilityReason | 'CHANNEL_CONTEXT_CHANGED' }
  | { outcome: 'REJECTED'; code: string }
  | { outcome: 'UNKNOWN'; evidence: 'ACK_WITHOUT_ID' | 'TRANSPORT_UNCONFIRMED'; legacyCode: string };

export interface TextMessage {
  kind: 'text';
  recipientRef: string;
  text: string;
}

export interface ApprovedTemplateMessage {
  kind: 'approved-template';
  recipientRef: string;
  template: {
    readonly summary: TemplateSummary;
    readonly values: Readonly<Record<string, string>> | readonly string[];
    readonly managementContext: TemplateManagementContext;
    readonly renderedText: string;
    readonly semanticFingerprint: string;
  };
}

export type ChannelMessage = TextMessage | ApprovedTemplateMessage;
export type ChannelMessageKind = ChannelMessage['kind'];

export interface ChannelSendOptions {
  /** Initial dispatch carries its durable claim fence into the provider adapter. */
  readonly purpose?: 'initial';
  /** Generic dispatch fence; invoked at the final provider boundary for ordinary and initial sends. */
  readonly beforeDispatch?: () => Promise<boolean>;
}

export abstract class Channel {
  abstract readonly supportedKinds: readonly ChannelMessageKind[];
  abstract sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult>;
}

/** Safe storage provenance captured for one send; never includes provider credentials or protocol addresses. */
export interface ChannelOperationContext {
  readonly channelId: string;
  readonly buId: string;
  readonly channelOrigin: ChannelOrigin;
  readonly providerResourceIdentityId: string;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
  readonly requiresWindow: boolean;
  readonly providerAccountReference: string | null;
}

/** Parse the provider-neutral operation context persisted by the admission owner. */
export function parseChannelOperationContext(value: Prisma.JsonValue): ChannelOperationContext | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const row = value as Record<string, Prisma.JsonValue>;
  if (typeof row.channelId !== 'string' || !row.channelId
    || typeof row.buId !== 'string' || !row.buId
    || (row.channelOrigin !== 'OFICIAL' && row.channelOrigin !== 'NAO_OFICIAL')
    || typeof row.providerResourceIdentityId !== 'string' || !row.providerResourceIdentityId
    || typeof row.generation !== 'number' || !Number.isSafeInteger(row.generation) || row.generation < 1
    || typeof row.pairingEpoch !== 'number' || !Number.isSafeInteger(row.pairingEpoch) || row.pairingEpoch < 0
    || row.activeCredentialVersion !== null && (typeof row.activeCredentialVersion !== 'number'
      || !Number.isSafeInteger(row.activeCredentialVersion) || row.activeCredentialVersion < 1)
    || typeof row.requiresWindow !== 'boolean'
    || row.providerAccountReference !== null && (typeof row.providerAccountReference !== 'string' || !row.providerAccountReference)) return null;
  return {
    channelId: row.channelId,
    buId: row.buId,
    channelOrigin: row.channelOrigin,
    providerResourceIdentityId: row.providerResourceIdentityId,
    generation: row.generation,
    pairingEpoch: row.pairingEpoch,
    activeCredentialVersion: row.activeCredentialVersion,
    requiresWindow: row.requiresWindow,
    providerAccountReference: row.providerAccountReference,
  };
}

export interface ResolvedChannelOperation {
  readonly channel: Channel;
  readonly context: ChannelOperationContext;
}

export interface ChannelAvailability {
  available: boolean;
  reason: ChannelAvailabilityReason | null;
  channelOrigin: ChannelOrigin | null;
  requiresWindow: boolean;
  windowOpen: boolean;
  expiresAt: Date | null;
}

export interface ConversationChannelReference {
  conversationId: string;
  buId: string;
}

export interface InitialChannelReference extends ConversationChannelReference {
  readonly channelId: string;
  readonly kind: ChannelMessageKind;
}

export interface ConversationAvailabilityReference extends ConversationChannelReference {
  latestMessageOrigin: ChannelOrigin | null;
}

export interface VerifiedIngressChannelReference extends ConversationChannelReference {
  channelId: string;
  providerResourceIdentityId: string;
  channelOrigin: ChannelOrigin;
  generation: number;
  pairingEpoch: number;
}

export abstract class ChannelResolver {
  abstract resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation>;
  abstract resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation>;
  /** Explicit channel selection for first-message intent; never infers or falls back. */
  abstract resolveForInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation>;
  /** Bind one explicitly selected channel for bounded, local initial-message options. */
  abstract resolveForInitialOptions(reference: ConversationChannelReference & { channelId: string }): Promise<ResolvedChannelOperation>;
  abstract inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability>;
  abstract inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>>;
  abstract hasReadyChannelForNewConversation(buId: string): Promise<boolean>;
  /** Revalidates the immutable captured transport tuple using the caller's already locked local transaction. */
  abstract validateOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedContext: Prisma.JsonValue,
  ): Promise<boolean>;
  /** Validates a known accepted operation for local-only Message recovery; credential/readiness may rotate after provider ACK. */
  abstract validateAcceptedOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedContext: Prisma.JsonValue,
  ): Promise<boolean>;
  abstract contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'>;
}
```

### api-app/src/domain/inbox/channel-window-policy.ts

SHA256 `46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';

const WINDOW_MS = 24 * 60 * 60 * 1000;

export function officialWindowState(timestamp: Date | null, now = new Date()): OfficialWindowState {
  if (!timestamp || !Number.isFinite(timestamp.getTime()) || timestamp.getTime() <= 0 || timestamp.getTime() > now.getTime()) {
    return { open: false, expiresAt: null };
  }
  const expiresAt = new Date(timestamp.getTime() + WINDOW_MS);
  return { open: expiresAt.getTime() > now.getTime(), expiresAt };
}

export function qualifiedMetaInboundTimestamp(value: unknown, now = new Date()): Date | null {
  if (typeof value !== 'string' && typeof value !== 'number') return null;
  if (typeof value === 'string' && !/^\d+$/.test(value)) return null;
  const seconds = typeof value === 'number' ? value : Number(value);
  if (!Number.isSafeInteger(seconds) || seconds <= 0) return null;
  const timestamp = new Date(seconds * 1000);
  if (!Number.isFinite(timestamp.getTime()) || timestamp.getTime() > now.getTime()) return null;
  return timestamp;
}

export interface OfficialInboundWindowEvidence {
  readonly direction: 'IN' | 'OUT';
  readonly channelOrigin: 'OFICIAL' | 'NAO_OFICIAL';
  readonly providerResourceIdentityId: string | null;
  readonly officialInboundAt: Date | null;
  /** Kept in callers' row shape to make it explicit that this is never a policy fallback. */
  readonly createdAt?: Date;
}

export interface OfficialWindowReference {
  readonly conversationId: string;
  readonly providerResourceIdentityId: string;
}

export interface OfficialWindowState {
  readonly open: boolean;
  readonly expiresAt: Date | null;
}

/** The single indexed query boundary used by outbound and every availability projection. */
@Injectable()
export class OfficialChannelWindowPolicy {
  constructor(private readonly prisma: PrismaService) {}

  async inspect(reference: OfficialWindowReference, now = new Date()): Promise<OfficialWindowState> {
    return this.inspectWith(this.prisma, reference, now);
  }

  /** Same current-resource query and expiry calculation inside a dispatch claim transaction. */
  async inspectInTransaction(
    tx: Prisma.TransactionClient,
    reference: OfficialWindowReference,
  ): Promise<OfficialWindowState> {
    const clock = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    if (!clock[0] || !(clock[0].now instanceof Date)) return { open: false, expiresAt: null };
    return this.inspectWith(tx, reference, clock[0].now);
  }

  private async inspectWith(
    client: PrismaService | Prisma.TransactionClient,
    reference: OfficialWindowReference,
    now: Date,
  ): Promise<OfficialWindowState> {
    const row = await client.message.findFirst({
      where: {
        conversationId: reference.conversationId,
        providerResourceIdentityId: reference.providerResourceIdentityId,
        direction: 'IN',
        channelOrigin: 'OFICIAL',
        officialInboundAt: { not: null, lte: now },
      },
      orderBy: [{ officialInboundAt: 'desc' }, { id: 'desc' }],
      select: { officialInboundAt: true },
    });
    return this.state(row?.officialInboundAt ?? null, now);
  }

  async inspectMany(references: readonly OfficialWindowReference[], now = new Date()): Promise<Map<string, OfficialWindowState>> {
    if (!references.length) return new Map();
    const conversationIds = references.map(({ conversationId }) => conversationId);
    const resourceIds = references.map(({ providerResourceIdentityId }) => providerResourceIdentityId);
    const rows = await this.prisma.$queryRaw<Array<{ conversation_id: string; official_inbound_at: Date }>>`
      SELECT requested.conversation_id, latest.official_inbound_at
      FROM unnest(ARRAY[${Prisma.join(conversationIds)}]::text[], ARRAY[${Prisma.join(resourceIds)}]::text[])
        AS requested(conversation_id, provider_resource_identity_id)
      CROSS JOIN LATERAL (
        SELECT message.official_inbound_at
        FROM messages AS message
        WHERE message.conversation_id = requested.conversation_id
          AND message.provider_resource_identity_id = requested.provider_resource_identity_id
          AND message.direction = 'IN' AND message.channel_origin = 'OFICIAL'
          AND message.official_inbound_at IS NOT NULL AND message.official_inbound_at <= ${now}
        ORDER BY message.official_inbound_at DESC, message.id DESC
        LIMIT 1
      ) AS latest
    `;
    const latest = new Map(rows.map((row) => [row.conversation_id, row.official_inbound_at]));
    return new Map(references.map((reference) => [reference.conversationId, this.state(latest.get(reference.conversationId) ?? null, now)]));
  }

  private state(timestamp: Date | null, now: Date): OfficialWindowState {
    return officialWindowState(timestamp, now);
  }
}

/** Applies the current selected managed resource's already-qualified Meta IN timestamps only. */
export function isOfficialWindowOpen(
  evidence: readonly OfficialInboundWindowEvidence[],
  selectedResourceIdentityId: string,
  now = new Date(),
): boolean {
  const latest = evidence.reduce<Date | null>((current, row) => {
    const timestamp = row.officialInboundAt;
    if (row.direction !== 'IN' || row.channelOrigin !== 'OFICIAL'
      || row.providerResourceIdentityId !== selectedResourceIdentityId || !timestamp
      || !Number.isFinite(timestamp.getTime()) || timestamp.getTime() <= 0 || timestamp.getTime() > now.getTime()) return current;
    return !current || timestamp.getTime() > current.getTime() ? timestamp : current;
  }, null);
  return officialWindowState(latest, now).open;
}
```

### api-app/src/domain/inbox/conversation-start.service.ts

SHA256 `97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelResolver } from '../channels/transport/channel';

const PHONE_FORMAT = /^\+?[0-9 ().-]+$/;

export function normalizeContactPhone(value: unknown): string {
  if (typeof value !== 'string' || value.length > 40 || !PHONE_FORMAT.test(value)) {
    throw new BadRequestException({ code: 'TELEFONE_INVALIDO' });
  }
  const digits = value.replace(/\D/g, '');
  if (!/^[1-9]\d{7,14}$/.test(digits)) {
    throw new BadRequestException({ code: 'TELEFONE_INVALIDO' });
  }
  return digits;
}

/** Opens or reuses a BU/contact conversation without changing an existing one. */
@Injectable()
export class ConversationStartService {
  constructor(private readonly prisma: PrismaService, private readonly channels: ChannelResolver) {}

  async start(buId: string, phone: unknown) {
    if (!buId) throw new BadRequestException({ code: 'BU_INVALIDA' });
    const contact = normalizeContactPhone(phone);
    const existingBeforeReadiness = await this.prisma.conversation.findUnique({ where: { buId_contact: { buId, contact } } });
    if (existingBeforeReadiness) return { conversation: existingBeforeReadiness, created: false };
    // Readiness uses the resolver's narrow local metadata only. Run before the
    // row lock/transaction so concurrent same-contact requests never hold a
    // database connection while waiting for a second resolver connection.
    const ready = await this.channels.hasReadyChannelForNewConversation(buId);
    return this.prisma.$transaction(async (tx) => {
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${JSON.stringify([buId, contact])}, 0))::text AS locked`;
      const existing = await tx.conversation.findUnique({ where: { buId_contact: { buId, contact } } });
      if (existing) return { conversation: existing, created: false };
      if (!ready) {
        throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
      }
      const conversation = await tx.conversation.create({ data: {
        buId,
        contact,
        contactType: 'PESSOA',
        status: 'QUEUED',
        unreadCount: 0,
        lastMessageAt: null,
      } });
      return { conversation, created: true };
    });
  }
}
```

### api-app/src/domain/inbox/initial-message.service.ts

SHA256 `61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { ConflictException, HttpException, Injectable, NotFoundException, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type InitialMessageIntent } from '@prisma/client';
import { createHash, randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { OutboundService } from './outbound.service';
import { DispatchAdmissionService } from './dispatch-admission.service';
import { TEMPLATE_MANAGEMENT_RESOLVER, type TemplateManagementResolver, type TemplateManagementContext, type TemplateSummary } from '../message-templates/template-management.ports';
import { TemplateObservationService } from '../message-templates/template-observation.service';
import { InitialTemplateRenderError, renderInitialTemplate } from './initial-message-template-renderer';
import type { ChannelMessage, ChannelOperationContext } from '../channels/transport/channel';
import { Inject } from '@nestjs/common';

type TextRequest = { channelId: string; expectedGeneration: number; kind: 'text'; text: string; previewFingerprint: string };
type TemplateRequest = { channelId: string; expectedGeneration: number; kind: 'approved-template'; remoteTemplateId: string; language: string; catalogAfter: string | null; expectedDefinitionFingerprint: string; values: Readonly<Record<string, string>> | readonly string[]; previewFingerprint: string };
type ObservedTemplateSummary = TemplateSummary & { readonly available: boolean };
type InitialRequest = TextRequest | TemplateRequest;
type PreviewRequest = Omit<TextRequest, 'previewFingerprint'> | Omit<TemplateRequest, 'previewFingerprint'>;
const canonical = (value: unknown): string => {
  if (Array.isArray(value)) return `[${value.map(canonical).join(',')}]`;
  if (value && typeof value === 'object') return `{${Object.keys(value as object).sort().map((key) => `${JSON.stringify(key)}:${canonical((value as Record<string, unknown>)[key])}`).join(',')}}`;
  return JSON.stringify(value) ?? 'null';
};
const fingerprint = (value: unknown) => createHash('sha256').update(canonical(value)).digest('hex');

@Injectable()
export class InitialMessageService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly outbound: OutboundService,
    private readonly admissions: DispatchAdmissionService,
    @Inject(TEMPLATE_MANAGEMENT_RESOLVER) private readonly templates: TemplateManagementResolver,
    private readonly observations: TemplateObservationService,
  ) {}

  async assertOrdinaryDispatchAllowed(conversationId: string, buId: string): Promise<void> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: conversationId, buId }, select: { id: true },
    });
    if (!conversation) throw new NotFoundException({ code: 'CONVERSATION_NOT_FOUND' });
    const [existingMessage, active] = await Promise.all([
      this.prisma.message.findFirst({ where: { conversationId }, select: { id: true } }),
      this.prisma.initialMessageIntent.findFirst({ where: { conversationId, buId, slotReleasedAt: null }, select: { id: true, state: true } }),
    ]);
    if (active) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: active.id, state: active.state });
    if (!existingMessage) throw new ConflictException({ code: 'INITIAL_SEND_REQUIRED' });
  }

  async preview(input: { conversationId: string; buId: string; actorId: string; message: PreviewRequest }) {
    const conversation = await this.conversation(input.conversationId, input.buId);
    const operation = await this.outbound.prepareInitial({ conversationId: conversation.id, buId: conversation.buId, channelId: input.message.channelId, kind: input.message.kind });
    this.assertGeneration(operation.context, input.message.expectedGeneration);
    let text: string;
    let semantics: unknown;
    let managementContext: TemplateManagementContext | undefined;
    if (input.message.kind === 'text') {
      if (typeof input.message.text !== 'string' || !input.message.text.trim() || [...input.message.text].length > 4096) throw new ConflictException({ code: 'INITIAL_PREVIEW_INVALID' });
      text = input.message.text;
      semantics = { kind: 'text', text };
    } else {
      const templateRequest = input.message;
      const resolved = await this.templates.resolve({ buId: input.buId, channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration });
      managementContext = resolved.context;
      this.assertManagementContext(operation.context, resolved.context);
      const catalog = await this.observations.getCatalog(input.actorId, input.buId, input.message.channelId, input.message.catalogAfter);
      const observation = (catalog.items as ObservedTemplateSummary[]).find((item) => item.remoteTemplateId === templateRequest.remoteTemplateId && item.language === templateRequest.language);
      if (!catalog.available || !observation || !observation.available || observation.status !== 'APPROVED' || !managementContext.accountReference) throw new ConflictException({ code: 'INITIAL_TEMPLATE_UNAVAILABLE' });
      const summary = observation;
      const rendered = this.renderTemplate(summary, input.message.values);
      if (rendered.semanticFingerprint !== input.message.expectedDefinitionFingerprint) throw new ConflictException({ code: 'INITIAL_TEMPLATE_CHANGED' });
      text = rendered.text;
      semantics = { kind: 'approved-template', remoteTemplateId: summary.remoteTemplateId, language: input.message.language,
        values: input.message.values, semanticFingerprint: rendered.semanticFingerprint };
    }
    const previewFingerprint = fingerprint({ version: 'initial-preview-v1', context: operation.context, recipient: conversation.contact, semantics });
    return { text, previewFingerprint,
      channel: { channelId: operation.context.channelId, channelOrigin: operation.context.channelOrigin,
        generation: operation.context.generation, requiresWindow: operation.context.requiresWindow },
      ...(managementContext ? { template: { available: true } } : {}) };
  }

  async submit(input: {
    conversationId: string; buId: string; actorId: string; actorName: string; idempotencyKey: string;
    message: InitialRequest; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>;
  }) {
    if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(input.idempotencyKey)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_INVALID' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const conversation = await this.conversation(input.conversationId, input.buId);
    const canonicalRequest = { ...input.message, recipient: conversation.contact };
    const requestFingerprint = fingerprint(canonicalRequest);
    const ownerNonce = randomUUID();
    const replay = await this.admissions.findInitialReplay({
      conversationId: input.conversationId, buId: input.buId, actorId: input.actorId,
      idempotencyKey: input.idempotencyKey, requestFingerprint, ownerNonce,
      selectedChannelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration,
    });
    if (replay) {
      const stored = this.requestRecord(replay.intent.request);
      if (canonical(stored?.canonicalRequest) !== canonical(canonicalRequest)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
      if (replay.intent.state === 'AMBIGUOUS' || replay.intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') {
        throw new ConflictException({ code: 'INITIAL_SEND_UNCERTAIN', attemptId: replay.intent.id, state: replay.intent.state });
      }
      return { replay: true, attempt: this.projectIntent(replay.intent), expiredPrepared: replay.intent.state === 'PREPARED' && replay.intent.leaseExpiresAt <= new Date() };
    }

    let preview: Awaited<ReturnType<InitialMessageService['preview']>>;
    let operation: Awaited<ReturnType<OutboundService['prepareInitial']>>;
    let payload: ChannelMessage;
    let finalSemantics: unknown;
    try {
      preview = await this.preview({ conversationId: input.conversationId, buId: input.buId, actorId: input.actorId, message: input.message.kind === 'text'
        ? { channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration, kind: 'text', text: input.message.text }
        : { channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration, kind: 'approved-template', remoteTemplateId: input.message.remoteTemplateId, language: input.message.language, catalogAfter: input.message.catalogAfter, expectedDefinitionFingerprint: input.message.expectedDefinitionFingerprint, values: input.message.values } });
      if (preview.previewFingerprint !== input.message.previewFingerprint) throw new ConflictException({ code: 'PREVIEW_CONTEXT_CHANGED' });
      operation = await this.outbound.prepareInitial({ conversationId: input.conversationId, buId: input.buId, channelId: input.message.channelId, kind: input.message.kind });
      this.assertGeneration(operation.context, input.message.expectedGeneration);
      if (input.message.kind === 'text') {
        payload = { kind: 'text', recipientRef: conversation.contact, text: input.message.text };
        finalSemantics = { kind: 'text', text: input.message.text };
      } else {
        const templateRequest = input.message;
        const management = await this.templates.resolve({ buId: input.buId, channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration });
        this.assertManagementContext(operation.context, management.context);
        const catalog = await this.observations.getCatalog(input.actorId, input.buId, input.message.channelId, input.message.catalogAfter);
        const observation = (catalog.items as ObservedTemplateSummary[]).find((item) => item.remoteTemplateId === templateRequest.remoteTemplateId && item.language === templateRequest.language);
        if (!catalog.available || !observation || !observation.available || observation.status !== 'APPROVED') throw new ConflictException({ code: 'INITIAL_TEMPLATE_UNAVAILABLE' });
        const summary = observation;
        const rendered = this.renderTemplate(summary, input.message.values);
        if (rendered.semanticFingerprint !== input.message.expectedDefinitionFingerprint) throw new ConflictException({ code: 'INITIAL_TEMPLATE_CHANGED' });
        finalSemantics = { kind: 'approved-template', remoteTemplateId: summary.remoteTemplateId, language: input.message.language,
          values: input.message.values, semanticFingerprint: rendered.semanticFingerprint };
        payload = { kind: 'approved-template', recipientRef: conversation.contact, template: {
          summary, values: input.message.values, managementContext: management.context,
          renderedText: rendered.text, semanticFingerprint: rendered.semanticFingerprint,
        } };
      }
      const context = operation.context;
      if (fingerprint({ version: 'initial-preview-v1', context, recipient: conversation.contact, semantics: finalSemantics }) !== input.message.previewFingerprint) {
        throw new ConflictException({ code: 'PREVIEW_CONTEXT_CHANGED' });
      }
    } catch (error) {
      if (error instanceof HttpException) {
        const response = error.getResponse();
        const body = response && typeof response === 'object' && !Array.isArray(response)
          ? response as Record<string, unknown> : {};
        const marked = {
          ...(typeof body.code === 'string' ? { code: body.code } : { code: 'INITIAL_PRE_ADMISSION_REJECTED' }),
          ...(typeof body.message === 'string' ? { message: body.message } : {}),
          ...(typeof body.error === 'string' ? { error: body.error } : {}),
          preAdmission: true,
        };
        throw new HttpException(marked, error.getStatus());
      }
      throw error;
    }
    const context = operation.context;
    const originalConversation = { updatedAt: conversation.updatedAt.toISOString(), status: conversation.status,
      attendantUserId: conversation.attendantUserId, attendantName: conversation.attendantName, attendantOrigin: conversation.attendantOrigin };
    const storedRequest = { canonicalRequest, originalConversation, renderedText: preview.text, originalActorName: input.actorName } as unknown as Prisma.InputJsonValue;
    const reservation = await this.admissions.reserveInitial({
      conversationId: input.conversationId, buId: input.buId, contact: conversation.contact, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
      ownerNonce, selectedContext: context as unknown as Prisma.InputJsonValue,
      requestFingerprint, request: storedRequest,
    });
    if (!reservation.created) {
      const stored = this.requestRecord(reservation.intent.request);
      if (canonical(stored?.canonicalRequest) !== canonical(canonicalRequest)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
      if (reservation.intent.state === 'AMBIGUOUS' || reservation.intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') {
        throw new ConflictException({ code: 'INITIAL_SEND_UNCERTAIN', attemptId: reservation.intent.id, state: reservation.intent.state });
      }
      return { replay: true, attempt: this.projectIntent(reservation.intent), expiredPrepared: reservation.intent.state === 'PREPARED' && reservation.intent.leaseExpiresAt <= new Date() };
    }
    const result = await this.outbound.sendInitial({
      conversationId: input.conversationId, buId: input.buId, channelId: input.message.channelId,
      kind: input.message.kind, intent: reservation.intent, ownerNonce, operation, payload,
      request: storedRequest,
      originalConversation: { updatedAt: conversation.updatedAt, status: conversation.status, attendantUserId: conversation.attendantUserId,
        attendantName: conversation.attendantName, attendantOrigin: conversation.attendantOrigin },
      actorId: input.actorId, actorName: input.actorName, validateActorInTransaction: input.validateActorInTransaction,
    });
    let finalIntent: InitialMessageIntent | null;
    try {
      finalIntent = await this.admissions.getInitialForScopedAttempt({ id: reservation.intent.id, conversationId: input.conversationId, buId: input.buId });
    } catch {
      finalIntent = null;
    }
    if (!finalIntent) throw new ServiceUnavailableException({ code: 'INITIAL_ATTEMPT_READBACK_UNCONFIRMED', attemptId: reservation.intent.id,
      providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED', localMessageState: 'RECORDED', recoveryAction: 'RECONCILE' });
    return { replay: false, expiredPrepared: false, attempt: this.projectIntent(finalIntent),
      message: { id: result.id, channelOrigin: result.channelOrigin, createdAt: result.createdAt } };
  }

  async options(input: { conversationId: string; buId: string }) {
    const conversation = await this.conversation(input.conversationId, input.buId);
    const [channels, active, admissions, recent] = await Promise.all([
      this.prisma.buChannel.findMany({ where: { buId: input.buId }, select: { id: true, type: true, generation: true }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], take: 10 }),
      this.prisma.initialMessageIntent.findFirst({ where: { conversationId: conversation.id, slotReleasedAt: null }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }] }),
      this.admissions.listActiveAdmissions({ conversationId: conversation.id, buId: input.buId, limit: 10 }),
      this.prisma.initialMessageIntent.findMany({ where: { conversationId: conversation.id, buId: input.buId }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], take: 11 }),
    ]);
    const channelOptions = await Promise.all(channels.map(async ({ id, type, generation }) => {
      try {
        const { operation, windowOpen, expiresAt } = await this.outbound.prepareInitialOptions({ conversationId: conversation.id, buId: input.buId, channelId: id });
        const supportedKinds = operation.channel.supportedKinds;
        return { id, type, generation, pairingEpoch: operation.context.pairingEpoch,
          activeCredentialVersion: operation.context.activeCredentialVersion, supportedKinds,
          availability: { text: !operation.context.requiresWindow || windowOpen ? null : 'JANELA_FECHADA',
            'approved-template': supportedKinds.includes('approved-template') ? null : 'UNSUPPORTED_KIND' },
          ...(expiresAt ? { windowExpiresAt: expiresAt } : {}) };
      } catch (error) {
        const response = error instanceof ConflictException ? error.getResponse() : null;
        const code = response && typeof response === 'object' ? (response as Record<string, unknown>).code : null;
        return { id, type, generation, supportedKinds: [], availability: { text: typeof code === 'string' ? code : 'CHANNEL_NOT_READY', 'approved-template': typeof code === 'string' ? code : 'CHANNEL_NOT_READY' } };
      }
    }));
    return { conversationId: conversation.id,
      channels: channelOptions,
      activeAttempt: active ? this.projectIntent(active) : null,
      ordinaryAdmissions: admissions.items.map(({ id, state, expiresAt, dispatchDeadlineAt, createdAt }) => ({ id, state, expiresAt, dispatchDeadlineAt, createdAt })),
      admissionsTruncated: admissions.truncated,
      recentAttempts: recent.slice(0, 10).map((intent) => this.projectIntent(intent)),
      attemptsTruncated: recent.length > 10 };
  }

  async getAttempt(input: { id: string; conversationId: string; buId: string }) {
    const intent = await this.admissions.getInitialForScopedAttempt(input);
    if (!intent) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    return this.projectIntent(intent);
  }

  async reconcile(input: { id: string; conversationId: string; buId: string; actorId: string; actorName: string; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean> }) {
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const intent = await this.admissions.reconcileInitial({ ...input, validateActor: input.validateActorInTransaction });
    if (!intent) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    if (intent.externalMessageId && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) {
      const message = await this.outbound.reconcileInitial({ intent, actorId: input.actorId, actorName: input.actorName, validateActorInTransaction: input.validateActorInTransaction });
      const current = await this.admissions.getInitialForScopedAttempt(input);
      return { ...this.projectIntent(current ?? intent), ...(message ? { message: { id: message.id, channelOrigin: message.channelOrigin, createdAt: message.createdAt } } : {}) };
    }
    return this.projectIntent(intent);
  }

  async acknowledge(input: { id: string; conversationId: string; buId: string; actorId: string; confirmed: boolean; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>; auditInTransaction: (tx: Prisma.TransactionClient) => Promise<void> }) {
    if (input.confirmed !== true) throw new ConflictException({ code: 'DUPLICATION_RISK_CONFIRMATION_REQUIRED' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const window = await this.admissions.initialRiskWindow(input);
    if (!window) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    if (window.eligibleAt && !window.eligible) throw new ConflictException({ code: 'ACK_TOO_EARLY', eligibleAt: window.eligibleAt });
    if (!await this.admissions.acknowledgeInitialRisk({ id: input.id, actorId: input.actorId, ownerNonce: window.intent.ownerNonce,
      validateActor: input.validateActorInTransaction, audit: input.auditInTransaction })) throw new ConflictException({ code: 'ACK_NOT_ELIGIBLE' });
    return this.getAttempt(input);
  }

  async reconcileOrdinary(input: { id: string; conversationId: string; buId: string; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean> }) {
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const result = await this.admissions.reconcileOrdinary({ ...input, validateActor: input.validateActorInTransaction });
    if (!result) throw new NotFoundException({ code: 'ADMISSION_NOT_FOUND' });
    const { id, state, expiresAt, dispatchDeadlineAt, createdAt, releasedAt, riskAcknowledgedAt } = result;
    return { id, state, expiresAt, dispatchDeadlineAt, createdAt, releasedAt, riskAcknowledgedAt };
  }

  async acknowledgeOrdinary(input: { id: string; conversationId: string; buId: string; actorId: string; confirmed: boolean; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>; auditInTransaction: (tx: Prisma.TransactionClient) => Promise<void> }) {
    if (!input.confirmed) throw new ConflictException({ code: 'DUPLICATION_RISK_CONFIRMATION_REQUIRED' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const window = await this.admissions.ordinaryRiskWindow(input);
    if (!window) throw new NotFoundException({ code: 'ADMISSION_NOT_FOUND' });
    if (window.eligibleAt && !window.eligible) throw new ConflictException({ code: 'ACK_TOO_EARLY', eligibleAt: window.eligibleAt });
    if (!await this.admissions.acknowledgeOrdinaryRisk({ ...input, validateActor: input.validateActorInTransaction, audit: input.auditInTransaction })) throw new ConflictException({ code: 'ACK_NOT_ELIGIBLE' });
    const { admission } = window;
    return { id: admission.id, acknowledged: true };
  }

  private async conversation(id: string, buId: string) {
    const conversation = await this.prisma.conversation.findFirst({ where: { id, buId } });
    if (!conversation) throw new NotFoundException({ code: 'CONVERSATION_NOT_FOUND' });
    return conversation;
  }
  private projectIntent(intent: InitialMessageIntent) {
    return {
      id: intent.id, state: intent.state, createdAt: intent.createdAt, updatedAt: intent.updatedAt,
      leaseExpiresAt: intent.leaseExpiresAt, dispatchDeadlineAt: intent.dispatchDeadlineAt,
      eligibleAt: ['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state) && intent.slotReleasedAt === null
        ? intent.dispatchDeadlineAt : null,
      slotReleasedAt: intent.slotReleasedAt, externalAccepted: intent.externalMessageId !== null,
      providerAcceptance: intent.externalMessageId !== null ? 'CONFIRMED' : ['SENDING', 'AMBIGUOUS'].includes(intent.state) ? 'UNKNOWN' : 'NOT_ACCEPTED',
      receiptPersistence: intent.externalMessageId !== null ? 'RECORDED' : 'NOT_RECORDED',
      localMessageState: intent.state === 'SUCCEEDED' ? 'RECORDED' : 'UNCONFIRMED',
      recoveryAction: ['PREPARED', 'SENDING', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)
        ? 'RECONCILE' : intent.state === 'AMBIGUOUS' ? 'ACK_AFTER_DEADLINE' : null,
      riskAcknowledgementAvailable: intent.slotReleasedAt === null && ['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state),
    };
  }
  private requestRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value) ? value as Record<string, Prisma.JsonValue> : null;
  }
  private renderTemplate(summary: TemplateSummary, values: Readonly<Record<string, string>> | readonly string[]) {
    try { return renderInitialTemplate(summary, values); }
    catch (error) {
      if (error instanceof InitialTemplateRenderError) throw new ConflictException({ code: error.code });
      throw error;
    }
  }
  private assertGeneration(context: ChannelOperationContext, expected: number) {
    if (context.generation !== expected) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
  }
  private assertManagementContext(operation: ChannelOperationContext, management: TemplateManagementContext) {
    if (operation.channelId !== management.channelId || operation.buId !== management.buId
      || operation.providerResourceIdentityId !== management.providerResourceIdentityId || operation.generation !== management.generation
      || operation.pairingEpoch !== management.pairingEpoch || operation.activeCredentialVersion !== management.activeCredentialVersion
      || operation.providerAccountReference !== management.accountReference) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
  }
}
```

### api-app/src/domain/inbox/dispatch-admission.service.ts

SHA256 `2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { ConflictException, Injectable, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type DispatchAdmission, type InitialMessageIntent } from '@prisma/client';
import { randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';

const TOKEN_LEASE_MS = 90_000;

export interface DispatchClaimEligibility {
  readonly eligible: boolean;
  /** Trusted channel-window edge captured by the sole window-policy owner. */
  readonly windowExpiresAt: Date | null;
}

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (value && typeof value === 'object') {
    const record = value as Record<string, unknown>;
    const entries = Object.keys(record).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(record[key])}`);
    return `{${entries.join(',')}}`;
  }
  return JSON.stringify(value);
}

export function isInitialRiskAcknowledgmentEligible(
  state: InitialMessageIntent['state'], deadline: Date | null, databaseNow: Date,
): boolean {
  return (state === 'AMBIGUOUS' || state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED')
    && deadline !== null && databaseNow.getTime() >= deadline.getTime();
}

export interface ReserveOrdinaryAdmissionInput {
  conversationId: string;
  buId: string;
  caller: 'BFF' | 'PUBLIC' | 'BOT';
  actorId: string;
  ownerNonce: string;
  selectedContext: Prisma.InputJsonValue;
}

export interface ReserveInitialIntentInput {
  conversationId: string;
  buId: string;
  contact: string;
  actorId: string;
  idempotencyKey: string;
  ownerNonce: string;
  selectedContext: Prisma.InputJsonValue;
  requestFingerprint: string;
  request: Prisma.InputJsonValue;
}

export interface InitialReplayLookup {
  conversationId: string;
  buId: string;
  actorId: string;
  idempotencyKey: string;
  requestFingerprint: string;
  selectedChannelId: string;
  expectedGeneration: number;
  ownerNonce: string;
}

@Injectable()
export class DispatchAdmissionService {
  constructor(private readonly prisma: PrismaService) {}

  /** Idempotency replay lookup happens before channel binding or provider preflight. */
  async findInitialReplay(input: InitialReplayLookup): Promise<{ intent: InitialMessageIntent; ownerNonce: string } | null> {
    const intent = await this.prisma.initialMessageIntent.findUnique({ where: {
      buId_actorId_idempotencyKey: { buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey },
    } });
    if (!intent) return null;
    if (intent.conversationId !== input.conversationId || intent.requestFingerprint !== input.requestFingerprint) {
      throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
    }
    const context = this.contextRecord(intent.selectedContext);
    if (!context || context.channelId !== input.selectedChannelId || context.generation !== input.expectedGeneration) {
      throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
    }
    return { intent, ownerNonce: input.ownerNonce };
  }

  /** Create a finite owner token under the shared conversation row lock. */
  async reserveOrdinary(input: ReserveOrdinaryAdmissionInput): Promise<{ admission: DispatchAdmission; ownerNonce: string }> {
    const admissionId = randomUUID();
    try {
      const admission = await this.prisma.$transaction(async (tx) => {
        const { now } = await this.lockConversation(tx, input.conversationId, input.buId);
        const initial = await tx.initialMessageIntent.findFirst({
          where: { conversationId: input.conversationId, slotReleasedAt: null },
          select: { id: true, state: true },
        });
        if (initial) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: initial.id, state: initial.state });
        return tx.dispatchAdmission.create({ data: {
          id: admissionId,
          conversationId: input.conversationId,
          buId: input.buId,
          caller: input.caller,
          actorId: input.actorId,
          ownerNonce: input.ownerNonce,
          selectedContext: input.selectedContext,
          state: 'PREPARED',
          expiresAt: new Date(now.getTime() + TOKEN_LEASE_MS),
        } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      return { admission, ownerNonce: input.ownerNonce };
    } catch (error) {
      const admission = await this.readAdmission(admissionId);
      if (admission && this.sameOrdinaryOwner(admission, input)) return { admission, ownerNonce: input.ownerNonce };
      throw error;
    }
  }

  /** Reserve the exclusive first-send slot and immutable request under that same row lock. */
  async reserveInitial(input: ReserveInitialIntentInput): Promise<{ intent: InitialMessageIntent; ownerNonce: string; created: boolean }> {
    const intentId = randomUUID();
    try {
      return await this.prisma.$transaction(async (tx) => {
      const replay = await tx.initialMessageIntent.findUnique({
        where: { buId_actorId_idempotencyKey: {
          buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
        } },
      });
      if (replay) {
        if (replay.conversationId !== input.conversationId || replay.requestFingerprint !== input.requestFingerprint) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        if (canonicalJson(this.canonicalRequestFromStored(replay.request)) !== canonicalJson(this.canonicalRequestFromStored(input.request))) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        // Never adopt a nonce read from an idempotent replay. The caller keeps
        // the nonce it captured before this request; a stale/replayed owner
        // cannot pass a later CAS with the new nonce.
        return { intent: replay, ownerNonce: input.ownerNonce, created: false };
      }

      const selected = this.contextRecord(input.selectedContext as Prisma.JsonValue);
      if (!selected || typeof selected.providerResourceIdentityId !== 'string' || typeof selected.channelId !== 'string') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      }
      const identity = await tx.$queryRaw<Array<{ id: string }>>`
        SELECT id FROM provider_resource_identities
        WHERE id = ${selected.providerResourceIdentityId} AND bu_id = ${input.buId} AND current_channel_id = ${selected.channelId}
        FOR SHARE
      `;
      if (!identity[0]) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      const contactLockKey = JSON.stringify([input.buId, input.contact]);
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactLockKey}, 0))::text AS locked`;
      const { now, contact } = await this.lockConversation(tx, input.conversationId, input.buId);
      if (contact !== input.contact) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });

      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'initial-actor:' + input.actorId}, 0))::text AS locked`;
      const contextForRate = this.contextRecord(input.selectedContext as Prisma.JsonValue);
      const accountNamespace = typeof contextForRate?.providerAccountReference === 'string'
        ? contextForRate.providerAccountReference
        : typeof contextForRate?.providerResourceIdentityId === 'string' ? contextForRate.providerResourceIdentityId : null;
      if (!accountNamespace) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'initial-account:' + accountNamespace}, 0))::text AS locked`;
      const rateNow = await this.databaseNow(tx);
      const actorRate = await tx.$queryRaw<Array<{ count: number }>>`
        SELECT count(*)::int AS count FROM initial_message_intents
        WHERE actor_id = ${input.actorId} AND created_at >= ${new Date(rateNow.getTime() - 60_000)}
      `;
      const accountRate = await tx.$queryRaw<Array<{ count: number }>>`
        SELECT count(*)::int AS count FROM initial_message_intents
        WHERE COALESCE(selected_context->>'providerAccountReference', selected_context->>'providerResourceIdentityId') = ${accountNamespace}
          AND created_at >= ${new Date(rateNow.getTime() - 60 * 60_000)}
      `;
      if ((actorRate[0]?.count ?? 0) >= 10 || (accountRate[0]?.count ?? 0) >= 60) {
        throw new ConflictException({ code: 'INITIAL_RATE_LIMIT' });
      }

      // PREPARED means no provider claim occurred, so its immutable lease can
      // close it safely. SENDING/UNCERTAIN are never released by elapsed time.
      await tx.dispatchAdmission.updateMany({
        where: { conversationId: input.conversationId, releasedAt: null, state: 'PREPARED', expiresAt: { lte: now } },
        data: { state: 'SETTLED', releasedAt: now },
      });
      const ordinary = await tx.dispatchAdmission.findMany({
        where: { conversationId: input.conversationId, releasedAt: null },
        orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
        select: { id: true, state: true }, take: 11,
      });
      if (ordinary.length) throw new ConflictException({ code: 'ORDINARY_SEND_IN_PROGRESS', outcome: 'BLOCKED',
        ordinaryAdmissions: ordinary.slice(0, 10).map(({ id, state }) => ({ id, state })), admissionsTruncated: ordinary.length > 10 });

      const active = await tx.initialMessageIntent.findFirst({
        where: { conversationId: input.conversationId, slotReleasedAt: null },
        select: { id: true, state: true },
      });
      if (active) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: active.id, state: active.state });

      const intent = await tx.initialMessageIntent.create({ data: {
        id: intentId,
        conversationId: input.conversationId,
        buId: input.buId,
        actorId: input.actorId,
        idempotencyKey: input.idempotencyKey,
        ownerNonce: input.ownerNonce,
        requestFingerprint: input.requestFingerprint,
        request: input.request,
        selectedContext: input.selectedContext,
        state: 'PREPARED',
        leaseExpiresAt: new Date(now.getTime() + TOKEN_LEASE_MS),
      } });
      return { intent, ownerNonce: input.ownerNonce, created: true };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const intent = await this.readIntent(intentId);
      if (intent && this.sameInitialOwner(intent, input)) return { intent, ownerNonce: input.ownerNonce, created: true };
      const replay = await this.prisma.initialMessageIntent.findUnique({ where: { buId_actorId_idempotencyKey: {
        buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
      } } });
      if (replay) {
        if (replay.conversationId !== input.conversationId || replay.requestFingerprint !== input.requestFingerprint
          || canonicalJson(this.canonicalRequestFromStored(replay.request)) !== canonicalJson(this.canonicalRequestFromStored(input.request))
          || canonicalJson(replay.selectedContext) !== canonicalJson(input.selectedContext)) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        return { intent: replay, ownerNonce: input.ownerNonce, created: false };
      }
      throw error;
    }
  }

  /** Same-owner CAS after preflight; all external reads must already be complete. */
  async claimOrdinary(input: {
    id: string;
    ownerNonce: string;
    /** Must perform only bounded, transaction-local checks; all remote preflight is already complete. */
    validate: (tx: Prisma.TransactionClient, selectedContext: Prisma.JsonValue) => Promise<DispatchClaimEligibility>;
  }): Promise<boolean> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return false;
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string' || typeof context.channelId !== 'string') return false;
        // Identity retirement/renewal takes the same lock first in acceptance.
        // Preserve the global identity -> conversation -> admission order.
        const identities = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null }>>`
          SELECT id, bu_id, current_channel_id
          FROM provider_resource_identities
          WHERE id = ${context.providerResourceIdentityId}
            AND bu_id = ${hint.buId}
            AND current_channel_id = ${context.channelId}
          FOR SHARE
        `;
        if (!identities[0]) return false;
        const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${hint.conversationId} AND bu_id = ${hint.buId}`;
        if (!contactRows[0]) return false;
        const contactKey = JSON.stringify([hint.buId, contactRows[0].contact]);
        await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || current.state !== 'PREPARED'
          || current.releasedAt !== null || current.expiresAt.getTime() <= now.getTime()) return false;
        const eligibility = await input.validate(tx, current.selectedContext);
        if (!eligibility.eligible) return false;
        const claimNow = await this.databaseNow(tx);
        if (current.expiresAt.getTime() <= claimNow.getTime()) return false;
        const claimed = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE dispatch_admissions
          SET state = 'SENDING'::"DispatchAdmissionState",
              dispatch_deadline_at = expires_at,
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state = 'PREPARED'::"DispatchAdmissionState"
            AND released_at IS NULL
            AND expires_at > clock_timestamp()
            AND (${eligibility.windowExpiresAt}::timestamptz IS NULL OR ${eligibility.windowExpiresAt}::timestamptz > clock_timestamp())
          RETURNING id
        `;
        return claimed.length === 1;
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SENDING'
        && current.dispatchDeadlineAt?.getTime() === current.expiresAt.getTime()) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.releasedAt === null) return false;
      throw error;
    }
  }

  /** Initial claim shares the identity→conversation→intent lock order and immutable 90s deadline. */
  async claimInitial(input: {
    id: string;
    ownerNonce: string;
    validate: (tx: Prisma.TransactionClient, selectedContext: Prisma.JsonValue, request: Prisma.JsonValue) => Promise<DispatchClaimEligibility>;
  }): Promise<boolean> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.initialMessageIntent.findUnique({ where: { id: input.id } });
        if (!hint) return false;
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string' || typeof context.channelId !== 'string') return false;
        const identities = await tx.$queryRaw<Array<{ id: string }>>`
          SELECT id
          FROM provider_resource_identities
          WHERE id = ${context.providerResourceIdentityId}
            AND bu_id = ${hint.buId}
            AND current_channel_id = ${context.channelId}
          FOR SHARE
        `;
        if (!identities[0]) return false;
        const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${hint.conversationId} AND bu_id = ${hint.buId}`;
        if (!contactRows[0]) return false;
        const contactKey = JSON.stringify([hint.buId, contactRows[0].contact]);
        await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.initialMessageIntent.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || current.state !== 'PREPARED'
          || current.slotReleasedAt !== null || current.leaseExpiresAt.getTime() <= now.getTime()) return false;
        const eligibility = await input.validate(tx, current.selectedContext, current.request);
        if (!eligibility.eligible) return false;
        const eligibleAtClaim = await this.databaseNow(tx);
        if (current.leaseExpiresAt.getTime() <= eligibleAtClaim.getTime()) return false;
        const claimed = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE initial_message_intents
          SET state = 'SENDING'::"InitialMessageIntentState",
              dispatch_deadline_at = lease_expires_at,
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state = 'PREPARED'::"InitialMessageIntentState"
            AND slot_released_at IS NULL
            AND lease_expires_at > clock_timestamp()
            AND (${eligibility.windowExpiresAt}::timestamptz IS NULL OR ${eligibility.windowExpiresAt}::timestamptz > clock_timestamp())
          RETURNING id
        `;
        return claimed.length === 1;
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SENDING'
        && current.dispatchDeadlineAt?.getTime() === current.leaseExpiresAt.getTime()) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.slotReleasedAt === null) return false;
      throw error;
    }
  }

  async rejectInitial(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null
          || !['PREPARED', 'SENDING'].includes(current.state) || current.externalMessageId !== null) return { count: 0 };
        const now = await this.databaseNow(tx);
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: current.state, slotReleasedAt: null, externalMessageId: null },
          data: { state: 'REJECTED', slotReleasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null) return true;
      throw error;
    }
  }

  /** Releases only an owner positively known to be PREPARED; never guesses after a claim commit ACK loss. */
  async rejectPreparedInitial(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null || current.state !== 'PREPARED') return { count: 0 };
        const now = await this.databaseNow(tx);
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'PREPARED', slotReleasedAt: null, externalMessageId: null },
          data: { state: 'REJECTED', slotReleasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null) return true;
      throw error;
    }
  }

  async recordInitialExternalAccepted(input: { id: string; ownerNonce: string; externalMessageId: string }): Promise<boolean> {
    if (!input.externalMessageId.trim()) return false;
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce) return { count: 0 };
        if (current.externalMessageId === input.externalMessageId
          && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state)) {
          return { count: 1 };
        }
        if (current.externalMessageId !== null || !['SENDING', 'AMBIGUOUS'].includes(current.state)) return { count: 0 };
        // A late known provider receipt improves only this original intent. If
        // risk acknowledgment already released its slot, retain that release
        // and classify the local projection as blocked; never reacquire a slot.
        const nextState = current.slotReleasedAt === null ? 'EXTERNAL_ACCEPTED' : 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED';
        return tx.initialMessageIntent.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: current.state,
            externalMessageId: null, slotReleasedAt: current.slotReleasedAt,
          },
          data: { state: nextState, externalMessageId: input.externalMessageId },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.externalMessageId === input.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state);
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.externalMessageId === input.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state)) return true;
      throw error;
    }
  }

  async markInitialAmbiguous(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null) return { count: 0 };
        if (current.state === 'AMBIGUOUS') return { count: 1 };
        if (current.state !== 'SENDING' || current.externalMessageId !== null) return { count: 0 };
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'SENDING', externalMessageId: null, slotReleasedAt: null },
          data: { state: 'AMBIGUOUS' },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'AMBIGUOUS' && current.slotReleasedAt === null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'AMBIGUOUS' && current.slotReleasedAt === null) return true;
      throw error;
    }
  }

  async acknowledgeInitialRisk(input: { id: string; ownerNonce: string; actorId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean>; audit?: (tx: Prisma.TransactionClient) => Promise<void> }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null
          || !['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(current.state)
          || !current.dispatchDeadlineAt) return { count: 0 };
        if (input.validateActor && !await input.validateActor(tx)) return { count: 0 };
        const rows = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE initial_message_intents
          SET slot_released_at = clock_timestamp(),
              risk_acknowledged_at = clock_timestamp(),
              risk_acknowledged_by_actor_id = ${input.actorId},
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state IN ('AMBIGUOUS'::"InitialMessageIntentState", 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'::"InitialMessageIntentState")
            AND external_message_id IS NOT DISTINCT FROM ${current.externalMessageId}
            AND slot_released_at IS NULL
            AND dispatch_deadline_at IS NOT NULL
            AND clock_timestamp() >= dispatch_deadline_at
          RETURNING id
        `;
        if (rows.length === 1 && input.audit) await input.audit(tx);
        return { count: rows.length };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.slotReleasedAt !== null
        && current.riskAcknowledgedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.slotReleasedAt !== null
        && current.riskAcknowledgedAt !== null) return true;
      throw error;
    }
  }

  async listActiveAdmissions(input: { conversationId: string; buId: string; limit?: number }): Promise<{ items: DispatchAdmission[]; truncated: boolean }> {
    const limit = input.limit ?? 10;
    const rows = await this.prisma.dispatchAdmission.findMany({
      where: { conversationId: input.conversationId, buId: input.buId, releasedAt: null },
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], take: limit + 1,
    });
    return { items: rows.slice(0, limit), truncated: rows.length > limit };
  }

  async reconcileOrdinary(input: { id: string; conversationId: string; buId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean> }): Promise<DispatchAdmission | null> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return null;
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string') return null;
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} FOR SHARE`;
        await this.lockConversation(tx, input.conversationId, input.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.conversationId !== input.conversationId || current.buId !== input.buId) return null;
        if (input.validateActor && !await input.validateActor(tx)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        const now = await this.databaseNow(tx);
        if (current.state === 'PREPARED' && current.releasedAt === null && current.expiresAt <= now) {
          await tx.dispatchAdmission.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'PREPARED', releasedAt: null },
            data: { state: 'SETTLED', releasedAt: now },
          });
        } else if (current.state === 'SENDING' && current.releasedAt === null
          && current.dispatchDeadlineAt !== null && current.dispatchDeadlineAt <= now) {
          await tx.dispatchAdmission.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'SENDING', releasedAt: null, dispatchDeadlineAt: current.dispatchDeadlineAt },
            data: { state: 'UNCERTAIN' },
          });
        }
        return tx.dispatchAdmission.findUnique({ where: { id: current.id } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof ConflictException) throw error;
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      if (current && ((current.state === 'SETTLED' && current.releasedAt !== null)
        || ['SENDING', 'UNCERTAIN'].includes(current.state))) return current;
      throw new ServiceUnavailableException({ code: 'ADMISSION_RECONCILE_UNCONFIRMED' });
    }
  }

  async acknowledgeOrdinaryRisk(input: { id: string; conversationId: string; buId: string; actorId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean>; audit?: (tx: Prisma.TransactionClient) => Promise<void> }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return { count: 0 };
        const context = this.contextRecord(hint.selectedContext);
        if (!context || typeof context.providerResourceIdentityId !== 'string') return { count: 0 };
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} FOR SHARE`;
        const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId}`;
        if (!contactRows[0]) return { count: 0 };
        const contactKey = JSON.stringify([input.buId, contactRows[0].contact]);
        await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
        await this.lockConversation(tx, input.conversationId, input.buId);
        if (input.validateActor && !await input.validateActor(tx)) return { count: 0 };
        const rows = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE dispatch_admissions
          SET released_at = clock_timestamp(), risk_acknowledged_at = clock_timestamp(),
              risk_acknowledged_by_actor_id = ${input.actorId}, updated_at = clock_timestamp()
          WHERE id = ${input.id} AND conversation_id = ${input.conversationId} AND bu_id = ${input.buId}
            AND state = 'UNCERTAIN'::"DispatchAdmissionState" AND released_at IS NULL
            AND dispatch_deadline_at IS NOT NULL AND clock_timestamp() >= dispatch_deadline_at
          RETURNING id
        `;
        if (rows.length === 1 && input.audit) await input.audit(tx);
        return { count: rows.length };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      return Boolean(current?.releasedAt && current.riskAcknowledgedAt);
    } catch {
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      if (current?.releasedAt && current.riskAcknowledgedAt) return true;
      throw new ServiceUnavailableException({ code: 'ADMISSION_RELEASE_UNCONFIRMED' });
    }
  }

  async reconcileInitial(input: { id: string; conversationId: string; buId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean> }): Promise<InitialMessageIntent | null> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.initialMessageIntent.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return null;
        const current = await this.lockInitialOwner(tx, hint.id);
        if (!current) return null;
        if (input.validateActor && !await input.validateActor(tx)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        const now = await this.databaseNow(tx);
        if (current.state === 'PREPARED' && current.slotReleasedAt === null && current.leaseExpiresAt <= now) {
          await tx.initialMessageIntent.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'PREPARED', slotReleasedAt: null },
            data: { state: 'REJECTED', slotReleasedAt: now },
          });
        } else if (current.state === 'SENDING' && current.slotReleasedAt === null
          && current.dispatchDeadlineAt !== null && current.dispatchDeadlineAt <= now) {
          await tx.initialMessageIntent.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'SENDING', slotReleasedAt: null, dispatchDeadlineAt: current.dispatchDeadlineAt },
            data: { state: 'AMBIGUOUS' },
          });
        }
        return tx.initialMessageIntent.findUnique({ where: { id: current.id } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof ConflictException) throw error;
      const current = await this.getInitialForScopedAttempt(input);
      if (current && ['PREPARED', 'SENDING', 'AMBIGUOUS', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED', 'REJECTED'].includes(current.state)) return current;
      throw new ServiceUnavailableException({ code: 'INITIAL_RECONCILE_UNCONFIRMED' });
    }
  }

  async getInitialForActor(input: { id: string; conversationId: string; buId: string; actorId: string }): Promise<InitialMessageIntent | null> {
    return this.prisma.initialMessageIntent.findFirst({ where: {
      id: input.id, conversationId: input.conversationId, buId: input.buId, actorId: input.actorId,
    } });
  }

  async getInitialForScopedAttempt(input: { id: string; conversationId: string; buId: string }): Promise<InitialMessageIntent | null> {
    return this.prisma.initialMessageIntent.findFirst({ where: {
      id: input.id, conversationId: input.conversationId, buId: input.buId,
    } });
  }

  async initialRiskWindow(input: { id: string; conversationId: string; buId: string }): Promise<{ intent: InitialMessageIntent; eligibleAt: Date | null; eligible: boolean } | null> {
    const intent = await this.getInitialForScopedAttempt(input);
    if (!intent) return null;
    const rows = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    const now = rows[0]?.now;
    if (!(now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    const allowedState = intent.state === 'AMBIGUOUS' || intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED';
    return { intent, eligibleAt: allowedState ? intent.dispatchDeadlineAt : null,
      eligible: isInitialRiskAcknowledgmentEligible(intent.state, intent.dispatchDeadlineAt, now) };
  }

  async ordinaryRiskWindow(input: { id: string; conversationId: string; buId: string }): Promise<{ admission: DispatchAdmission; eligibleAt: Date | null; eligible: boolean } | null> {
    const admission = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
    if (!admission) return null;
    const rows = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    const now = rows[0]?.now;
    if (!(now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    return { admission, eligibleAt: admission.dispatchDeadlineAt, eligible: Boolean(admission.dispatchDeadlineAt && now.getTime() >= admission.dispatchDeadlineAt.getTime()) };
  }

  async markInitialLocalBlocked(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || !current.externalMessageId) return { count: 0 };
        if (current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') return { count: 1 };
        if (current.state !== 'EXTERNAL_ACCEPTED') return { count: 0 };
        return tx.initialMessageIntent.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: 'EXTERNAL_ACCEPTED',
            externalMessageId: current.externalMessageId, slotReleasedAt: current.slotReleasedAt,
          },
          data: { state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED' },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'
        && current.externalMessageId !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'
        && current.externalMessageId !== null) return true;
      throw error;
    }
  }

  /** Settle only the original owner; a late completion cannot release a successor token. */
  async settleOrdinary(input: { id: string; ownerNonce: string; state: 'SETTLED' | 'UNCERTAIN' }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return { count: 0 };
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || !['SENDING', 'UNCERTAIN'].includes(current.state)) return { count: 0 };
        return tx.dispatchAdmission.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: { in: ['SENDING', 'UNCERTAIN'] }, releasedAt: current.releasedAt,
          },
          data: {
            state: input.state,
            ...(input.state === 'SETTLED' ? { releasedAt: current.releasedAt ?? now } : {}),
          },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readAdmission(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === input.state
        && (input.state === 'UNCERTAIN' ? current.releasedAt === null : current.releasedAt !== null);
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === input.state
        && (input.state === 'UNCERTAIN' ? current.releasedAt === null : current.releasedAt !== null)) return true;
      if (current?.ownerNonce === input.ownerNonce && ['SENDING', 'UNCERTAIN'].includes(current.state) && current.releasedAt === null) return false;
      throw error;
    }
  }

  /** A confirmed pre-dispatch abort releases only this still-PREPARED owner. */
  async releasePrepared(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return { count: 0 };
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        return tx.dispatchAdmission.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'PREPARED', releasedAt: null },
          data: { state: 'SETTLED', releasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readAdmission(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'SETTLED' && current.releasedAt !== null;
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SETTLED' && current.releasedAt !== null) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.releasedAt === null) return false;
      throw error;
    }
  }

  private async lockConversation(tx: Prisma.TransactionClient, conversationId: string, buId: string) {
    const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; contact: string }>>`
      SELECT id, bu_id, contact
      FROM conversations
      WHERE id = ${conversationId} AND bu_id = ${buId}
      FOR UPDATE
    `;
    const row = rows[0];
    if (!row) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    return { now: await this.databaseNow(tx), contact: row.contact };
  }

  /** Preserve identity→conversation→intent order for all initial lifecycle mutations. */
  private async lockInitialOwner(tx: Prisma.TransactionClient, id: string): Promise<InitialMessageIntent | null> {
    const hint = await tx.initialMessageIntent.findUnique({ where: { id } });
    if (!hint) return null;
    const context = this.contextRecord(hint.selectedContext);
    if (!context || typeof context.providerResourceIdentityId !== 'string') return null;
    await tx.$queryRaw<Array<{ id: string }>>`
      SELECT id FROM provider_resource_identities
      WHERE id = ${context.providerResourceIdentityId}
      FOR SHARE
    `;
    const contactRows = await tx.$queryRaw<Array<{ contact: string }>>`SELECT contact FROM conversations WHERE id = ${hint.conversationId} AND bu_id = ${hint.buId}`;
    if (!contactRows[0]) return null;
    const contactKey = JSON.stringify([hint.buId, contactRows[0].contact]);
    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactKey}, 0))::text AS locked`;
    await this.lockConversation(tx, hint.conversationId, hint.buId);
    return tx.initialMessageIntent.findUnique({ where: { id } });
  }

  private async databaseNow(tx: Prisma.TransactionClient): Promise<Date> {
    const rows = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    if (!rows[0] || !(rows[0].now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    return rows[0].now;
  }

  private contextRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value)
      ? value as Record<string, Prisma.JsonValue>
      : null;
  }

  private canonicalRequestFromStored(value: Prisma.JsonValue | Prisma.InputJsonValue): unknown {
    const record = value && typeof value === 'object' && !Array.isArray(value)
      ? value as Record<string, unknown>
      : null;
    return record && Object.hasOwn(record, 'canonicalRequest') ? record.canonicalRequest ?? null : value;
  }

  private async readAdmission(id: string): Promise<DispatchAdmission | null> {
    try { return await this.prisma.dispatchAdmission.findUnique({ where: { id } }); }
    catch { throw new ServiceUnavailableException({ code: 'ADMISSION_COMMIT_UNCONFIRMED' }); }
  }

  private async readIntent(id: string): Promise<InitialMessageIntent | null> {
    try { return await this.prisma.initialMessageIntent.findUnique({ where: { id } }); }
    catch { throw new ServiceUnavailableException({ code: 'INITIAL_INTENT_COMMIT_UNCONFIRMED' }); }
  }

  private sameOrdinaryOwner(row: DispatchAdmission, input: ReserveOrdinaryAdmissionInput): boolean {
    return Boolean(row.id) && row.ownerNonce === input.ownerNonce && row.conversationId === input.conversationId
      && row.buId === input.buId && row.caller === input.caller && row.actorId === input.actorId
      && canonicalJson(row.selectedContext) === canonicalJson(input.selectedContext);
  }

  private sameInitialOwner(row: InitialMessageIntent, input: ReserveInitialIntentInput): boolean {
    return row.ownerNonce === input.ownerNonce && row.conversationId === input.conversationId
      && row.buId === input.buId && row.actorId === input.actorId && row.idempotencyKey === input.idempotencyKey
      && row.requestFingerprint === input.requestFingerprint
      && canonicalJson(row.selectedContext) === canonicalJson(input.selectedContext)
      && canonicalJson(row.request) === canonicalJson(input.request);
  }
}
```

### api-app/src/domain/inbox/outbound.service.ts

SHA256 `cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { BadRequestException, ConflictException, HttpException, Injectable, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type InitialMessageIntent } from '@prisma/client';
import { randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelResolver, parseChannelOperationContext, type ChannelMessage, type ChannelOperationContext, type InitialChannelReference, type ResolvedChannelOperation, type VerifiedIngressChannelReference } from '../channels/transport/channel';
import type { ChannelSendResult } from '../channels/transport/channel';
import { MessageAcceptanceService, type MessageAcceptanceInput } from './message-acceptance.service';
import { DispatchAdmissionService, type DispatchClaimEligibility } from './dispatch-admission.service';
import { RealtimeService } from '../../realtime/realtime.service';
import { OfficialChannelWindowPolicy } from './channel-window-policy';

const FIXED_UNKNOWN = 'Resultado do envio não confirmado; confira a conversa antes de tentar novamente.';
const FIXED_LOCAL_INCOMPLETE = 'O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente.';
const FIXED_REJECTED = 'O canal recusou o envio.';
type OutboundConversation = Prisma.ConversationGetPayload<object>;

type InitialConversationSnapshot = Pick<OutboundConversation, 'updatedAt' | 'status' | 'attendantUserId' | 'attendantName' | 'attendantOrigin'>;
type InitialActorFence = (tx: Prisma.TransactionClient) => Promise<boolean>;

export type OutboundAttribution =
  | { kind: 'BFF'; userId: string; name: string }
  | { kind: 'PUBLIC'; name: string }
  | { kind: 'BOT'; name: string };

export interface SendOutboundInput {
  conversationId: string;
  buId: string;
  text: string;
  attribution: OutboundAttribution;
  ingress?: Omit<VerifiedIngressChannelReference, 'conversationId' | 'buId'>;
}

@Injectable()
export class OutboundService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly resolver: ChannelResolver,
    private readonly acceptance: MessageAcceptanceService,
    private readonly realtime: RealtimeService,
    private readonly windows: OfficialChannelWindowPolicy,
    private readonly admissions: DispatchAdmissionService,
  ) {}

  async prepareInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation> {
    return this.resolver.resolveForInitial(reference);
  }

  async prepareInitialOptions(reference: { conversationId: string; buId: string; channelId: string }) {
    const operation = await this.resolver.resolveForInitialOptions(reference);
    const window = operation.context.requiresWindow
      ? await this.windows.inspect({ conversationId: reference.conversationId, providerResourceIdentityId: operation.context.providerResourceIdentityId })
      : { open: true, expiresAt: null };
    return { operation, windowOpen: window.open, expiresAt: window.expiresAt };
  }

  /** Local-only completion of a separately persisted known Meta/Evolution receipt. */
  async reconcileInitial(input: {
    readonly intent: InitialMessageIntent;
    readonly actorId: string;
    readonly actorName: string;
    readonly validateActorInTransaction: InitialActorFence;
  }) {
    const intent = input.intent;
    if (!intent.externalMessageId || !['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) return null;
    const context = parseChannelOperationContext(intent.selectedContext);
    const stored = this.initialRequestRecord(intent.request);
    const canonicalRequest = stored?.canonicalRequest;
    const renderedText = stored?.renderedText;
    const original = this.originalConversationSnapshot(stored?.originalConversation);
    const originalActorName = stored?.originalActorName;
    if (!context || !original || typeof renderedText !== 'string' || !renderedText || typeof originalActorName !== 'string' || !originalActorName) {
      await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(intent.id, 'RECORDED');
    }
    const conversation = await this.prisma.conversation.findFirst({ where: { id: intent.conversationId, buId: intent.buId } });
    if (!conversation || !canonicalRequest || typeof canonicalRequest !== 'object' || Array.isArray(canonicalRequest)) {
      throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    }
    const acceptanceInput: MessageAcceptanceInput = {
      externalMessageId: intent.externalMessageId, providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId, generation: context.generation, pairingEpoch: context.pairingEpoch,
      buId: context.buId, channelOrigin: context.channelOrigin, contact: conversation.contact,
      contactType: conversation.contactType, conversationId: conversation.id, direction: 'OUT', messageType: 'TEXTO',
      content: renderedText, authorUserId: intent.actorId, authorName: originalActorName, senderResult: true,
    };
    const complete = (tx: Prisma.TransactionClient) => this.acceptance.acceptInTransaction(tx, acceptanceInput,
      async (transaction, priorExists) => {
        if (!await this.resolver.validateAcceptedOperationContextInTransaction(transaction, context, intent.selectedContext)) {
          throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
        }
        if (!await input.validateActorInTransaction(transaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        await this.finalizeInitialInTransaction(transaction, {
          conversationId: conversation.id, buId: conversation.buId, intent, ownerNonce: intent.ownerNonce,
          originalConversation: original, actorId: intent.actorId, actorName: originalActorName,
          conversation, externalMessageId: intent.externalMessageId!, priorExists,
        });
      });
    try {
      const accepted = await this.prisma.$transaction(complete, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (accepted.creationWinner) {
        try {
          this.realtime.publicarNaBu(conversation.buId, {
            tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
            direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
          });
        } catch { /* Durable local completion is authoritative; realtime is best effort. */ }
      }
      return accepted.message;
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        const prior = await this.readBack(conversation, context, intent.externalMessageId);
        if (prior) {
          try {
            const retried = await this.prisma.$transaction(complete, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
            if (retried.creationWinner) {
              try {
                this.realtime.publicarNaBu(conversation.buId, {
                  tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
                  direcao: 'OUT', canal: retried.message.channelOrigin, naoLidas: retried.conversation.unreadCount,
                });
              } catch { /* Durable local completion is authoritative; realtime is best effort. */ }
            }
            return retried.message;
          } catch {
            await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
            throw this.initialLocalIncomplete(intent.id, 'RECORDED');
          }
        }
      } else {
        const message = await this.readBack(conversation, context, intent.externalMessageId);
        const current = await this.admissions.getInitialForScopedAttempt({ id: intent.id, conversationId: intent.conversationId, buId: intent.buId }).catch(() => null);
        if (message && current?.state === 'SUCCEEDED' && current.externalMessageId === intent.externalMessageId) return message;
      }
      await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(intent.id, 'RECORDED');
    }
  }

  /** Dispatches one already-reserved initial intent through the common channel and Message owners. */
  async sendInitial(input: {
    readonly conversationId: string;
    readonly buId: string;
    readonly channelId: string;
    readonly kind: ChannelMessage['kind'];
    readonly intent: InitialMessageIntent;
    readonly ownerNonce: string;
    readonly operation: ResolvedChannelOperation;
    readonly payload: ChannelMessage;
    readonly request: Prisma.InputJsonValue;
    readonly originalConversation: InitialConversationSnapshot;
    readonly actorId: string;
    readonly actorName: string;
    readonly validateActorInTransaction: InitialActorFence;
  }) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: input.conversationId, buId: input.buId },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    let operation: ResolvedChannelOperation;
    try {
      operation = await this.resolver.resolveForInitial({
        conversationId: conversation.id, buId: conversation.buId, channelId: input.channelId, kind: input.kind,
      });
    } catch (error) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
      throw error;
    }
    if (!sameContext(operation.context, input.operation.context)) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
    }

    let claimed = false;
    type InitialClaimOutcome = 'NOT_ATTEMPTED' | 'CLAIMED' | 'NOT_CLAIMED' | 'UNKNOWN';
    const claimStatus: { value: InitialClaimOutcome } = { value: 'NOT_ATTEMPTED' };
    const claimOutcome = (): InitialClaimOutcome => claimStatus.value;
    let claimPromise: Promise<boolean> | null = null;
    const beforeDispatch = async () => {
      if (!claimPromise) {
        claimPromise = this.admissions.claimInitial({
          id: input.intent.id,
          ownerNonce: input.ownerNonce,
          validate: async (tx, selectedContext, request) => {
            if (canonicalJson(request) !== canonicalJson(input.request)) return { eligible: false, windowExpiresAt: null };
            const eligibility = await this.validateDispatchContext(tx, operation.context, selectedContext, conversation.id, input.kind === 'text');
            if (!eligibility.eligible || !await input.validateActorInTransaction(tx)) {
              return { ...eligibility, eligible: false };
            }
            return eligibility;
          },
        }).then((value) => { claimStatus.value = value ? 'CLAIMED' : 'NOT_CLAIMED'; return value; }, () => { claimStatus.value = 'UNKNOWN'; return false; });
      }
      claimed = await claimPromise;
      return claimed;
    };

    let result: ChannelSendResult;
    try {
      result = await operation.channel.sendMessage(input.payload, { purpose: 'initial', beforeDispatch });
    } catch {
      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
    }

    if (result.outcome === 'BLOCKED') {
      if (claimOutcome() === 'NOT_ATTEMPTED' || claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'CLAIMED') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw this.blocked(result.reason);
    }
    if (result.outcome === 'REJECTED') {
      if (claimOutcome() === 'NOT_ATTEMPTED' || claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'CLAIMED') await this.admissions.rejectInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
    }
    if (result.outcome === 'UNKNOWN') {
      if (!claimed) {
        if (claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
        else if (claimOutcome() === 'UNKNOWN') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
        throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_UNCONFIRMED', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
      }
      let classified = false;
      try {
        classified = await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      } catch { /* a lost write acknowledgment needs a positive scoped readback */ }
      if (!classified) {
        const persisted = await this.admissions.getInitialForScopedAttempt({
          id: input.intent.id, conversationId: input.conversationId, buId: input.buId,
        }).catch(() => null);
        classified = persisted?.ownerNonce === input.ownerNonce && persisted.state === 'AMBIGUOUS'
          && persisted.slotReleasedAt === null;
      }
      if (!classified) {
        throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_UNCONFIRMED', outcome: 'UNKNOWN', attemptId: input.intent.id, error: FIXED_UNKNOWN });
      }
      throw new ConflictException({ code: 'INITIAL_SEND_AMBIGUOUS', outcome: 'AMBIGUOUS', state: 'AMBIGUOUS', attemptId: input.intent.id, error: FIXED_UNKNOWN });
    }
    if (!claimed) {
      if (claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'UNKNOWN') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_FENCE_MISSING', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
    }

    let receipt: boolean;
    try {
      receipt = await this.admissions.recordInitialExternalAccepted({
        id: input.intent.id, ownerNonce: input.ownerNonce, externalMessageId: result.externalMessageId,
      });
    } catch {
      const exact = await this.admissions.getInitialForScopedAttempt({
        id: input.intent.id, conversationId: input.conversationId, buId: input.buId,
      }).catch(() => null);
      receipt = exact?.ownerNonce === input.ownerNonce && exact.externalMessageId === result.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(exact.state);
        if (!receipt) throw this.initialLocalIncomplete(input.intent.id, 'UNCONFIRMED', 'INITIAL_RECEIPT_UNCONFIRMED');
    }
    if (!receipt) {
      await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(input.intent.id, 'UNCONFIRMED', 'INITIAL_RECEIPT_UNCONFIRMED');
    }

    const acceptanceInput = this.initialAcceptanceInput(input, conversation, operation.context, result.externalMessageId);
    const completeInitial = async (transaction: Prisma.TransactionClient, priorExists: boolean) => {
      const valid = await this.resolver.validateAcceptedOperationContextInTransaction(transaction, operation.context, input.intent.selectedContext);
      if (!valid) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      if (!await input.validateActorInTransaction(transaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
      await this.finalizeInitialInTransaction(transaction, {
        ...input, conversation, externalMessageId: result.externalMessageId, priorExists,
      });
    };
    let accepted: Awaited<ReturnType<MessageAcceptanceService['acceptInTransaction']>>;
    try {
      accepted = await this.prisma.$transaction(async (tx) => this.acceptance.acceptInTransaction(
        tx,
        acceptanceInput,
        completeInitial,
      ), { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        const prior = await this.findConfirmedOutbound({
          providerResourceIdentityId: operation.context.providerResourceIdentityId,
          externalMessageId: result.externalMessageId,
          conversationId: conversation.id, buId: conversation.buId,
          contact: conversation.contact, channelOrigin: operation.context.channelOrigin,
        }).catch(() => null);
        if (prior) {
          try {
            accepted = await this.prisma.$transaction(async (tx) => this.acceptance.acceptInTransaction(
              tx,
              acceptanceInput,
              completeInitial,
            ), { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
          } catch {
            await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
            throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
          }
        } else {
          await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
          throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
        }
      } else {
        const message = await this.readBack(conversation, operation.context, result.externalMessageId).catch(() => null);
        if (message) {
          const row = await this.admissions.getInitialForScopedAttempt({
            id: input.intent.id, conversationId: conversation.id, buId: conversation.buId,
          }).catch(() => null);
          if (row?.state === 'SUCCEEDED' && row.externalMessageId === result.externalMessageId) {
            return message;
          }
        }
        await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
        throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
      }
    }

    if (accepted.creationWinner) {
      try {
        this.realtime.publicarNaBu(conversation.buId, {
          tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
          direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
        });
      } catch { /* Message commit is authoritative; realtime is best effort. */ }
    }
    return accepted.message;
  }

  async send(input: SendOutboundInput) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: input.conversationId, buId: input.buId },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });

    let operation: ResolvedChannelOperation;
    try {
      operation = input.ingress
        ? await this.resolver.resolveForIngress({
            conversationId: conversation.id, buId: conversation.buId, ...input.ingress,
          })
        : await this.resolver.resolveForConversation({ conversationId: conversation.id, buId: conversation.buId });
    } catch (error) {
      if (error instanceof HttpException) throw this.asBlocked(error);
      throw error;
    }

    if (operation.context.requiresWindow && !(await this.windows.inspect({
      conversationId: conversation.id,
      providerResourceIdentityId: operation.context.providerResourceIdentityId,
    })).open) {
      throw new ConflictException({ code: 'JANELA_FECHADA', outcome: 'BLOCKED', error: 'Fora da janela de 24h da última mensagem recebida.' });
    }

    const attribution = input.attribution;
    const actorId = attribution.kind === 'BFF' ? attribution.userId
      : attribution.kind === 'PUBLIC' ? `public:${conversation.buId}`
        : `bot:${attribution.name}`;
    const reservation = await this.admissions.reserveOrdinary({
      conversationId: conversation.id,
      buId: conversation.buId,
      caller: attribution.kind,
      actorId,
      ownerNonce: randomUUID(),
      selectedContext: operation.context as unknown as Prisma.InputJsonValue,
    });
    let claimed = false;
    let claimPromise: Promise<boolean> | null = null;
    const beforeDispatch = async () => {
      if (!claimPromise) {
        claimPromise = this.admissions.claimOrdinary({
          id: reservation.admission.id,
          ownerNonce: reservation.ownerNonce,
          validate: (tx, selectedContext) => this.validateDispatchContext(
            tx, operation.context, selectedContext, conversation.id,
          ),
        });
      }
      claimed = await claimPromise;
      return claimed;
    };

    let result: ChannelSendResult;
    try {
      result = await operation.channel.sendMessage(
        { kind: 'text', recipientRef: conversation.contact, text: input.text },
        { beforeDispatch },
      );
    } catch {
      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
    }
    if (result.outcome === 'BLOCKED') {
      try {
        if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
        else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      } catch { /* Preserve the established BLOCKED projection; uncertain bookkeeping retains its slot. */ }
      throw this.blocked(result.reason);
    }
    if (result.outcome === 'REJECTED') {
      try {
        if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
        else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      } catch { /* The provider refusal is definitive; uncertain bookkeeping cannot retry it. */ }
      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
    }
    if (result.outcome === 'UNKNOWN') {
      try {
        if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'UNCERTAIN' });
        else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      } catch { /* Preserve the provider uncertainty and never infer a released slot. */ }
      return this.finishUnknown(input, conversation, operation.context, result);
    }
    if (!claimed) {
      // An adapter may not report acceptance unless the durable owner fence ran.
      try { await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce }); }
      catch { /* Keep the fence failure projection; an unconfirmed reservation remains conservative. */ }
      throw new ServiceUnavailableException({ code: 'OUTBOUND_DISPATCH_FENCE_MISSING', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
    }

    const contextState = await this.contextState(operation.context);
    if (contextState !== 'CURRENT') {
      const message = await this.readBack(conversation, operation.context, result.externalMessageId);
      try { await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: message ? 'SETTLED' : 'UNCERTAIN' }); }
      catch { /* Keep the confirmed provider result projection below. */ }
      throw this.acceptedIncomplete(contextState, message ? 'RECORDED' : 'UNCONFIRMED');
    }

    const acceptanceInput = this.acceptanceInput(input, conversation, operation.context, result.externalMessageId);
    let accepted: Awaited<ReturnType<MessageAcceptanceService['accept']>>;
    try {
      accepted = await this.acceptance.accept(acceptanceInput);
    } catch {
      const [after, message] = await Promise.all([
        this.contextState(operation.context),
        this.readBack(conversation, operation.context, result.externalMessageId),
      ]);
      try { await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: message ? 'SETTLED' : 'UNCERTAIN' }); }
      catch { /* Preserve the confirmed remote ACK and local Message readback. */ }
      throw this.acceptedIncomplete(after, message ? 'RECORDED' : 'UNCONFIRMED');
    }

    let settled = false;
    try {
      settled = await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
    } catch {
      // The provider ACK and accepted Message are already durable; settlement uncertainty
      // must preserve that projection without retrying the provider operation.
    }
    if (!settled) throw this.acceptedIncomplete(await this.contextState(operation.context), 'RECORDED');

    let localFailure = false;
    if (accepted.creationWinner) {
      try {
        this.realtime.publicarNaBu(conversation.buId, {
          tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
          direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
        });
      } catch { localFailure = true; }
    }
    try {
      await this.finalizeOutbound({
        conversationId: conversation.id, buId: conversation.buId, contact: conversation.contact,
        contactType: conversation.contactType, attribution: input.attribution,
      });
    } catch { localFailure = true; }
    if (localFailure) {
      throw this.acceptedIncomplete(await this.contextState(operation.context), 'RECORDED');
    }
    return accepted.message;
  }

  private initialAcceptanceInput(
    input: { actorId: string; actorName: string; payload: ChannelMessage },
    conversation: OutboundConversation,
    context: ChannelOperationContext,
    externalMessageId: string,
  ): MessageAcceptanceInput {
    const content = input.payload.kind === 'text' ? input.payload.text : input.payload.template.renderedText;
    return {
      externalMessageId, providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId, generation: context.generation, pairingEpoch: context.pairingEpoch,
      buId: context.buId, channelOrigin: context.channelOrigin, contact: conversation.contact,
      contactType: conversation.contactType, conversationId: conversation.id, direction: 'OUT',
      messageType: 'TEXTO', content, authorUserId: input.actorId, authorName: input.actorName, senderResult: true,
    };
  }

  private async finalizeInitialInTransaction(
    tx: Prisma.TransactionClient,
    input: {
      conversationId: string; buId: string; intent: InitialMessageIntent; ownerNonce: string;
      originalConversation: InitialConversationSnapshot; actorId: string; actorName: string;
      conversation: OutboundConversation; externalMessageId: string; priorExists: boolean;
    },
  ): Promise<void> {
    const contactLockKey = JSON.stringify([input.buId, input.conversation.contact]);
    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${contactLockKey}, 0))::text AS locked`;
    const rows = await tx.$queryRaw<Array<{ id: string; updated_at: Date; status: string; attendant_user_id: string | null; attendant_name: string | null; attendant_origin: string | null }>>`
      SELECT id, updated_at, status::text AS status, attendant_user_id
        , attendant_name, attendant_origin
      FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId} FOR UPDATE
    `;
    await tx.$queryRaw`SELECT id FROM initial_message_intents WHERE id = ${input.intent.id} FOR UPDATE`;
    const intent = await tx.initialMessageIntent.findUnique({ where: { id: input.intent.id } });
    const current = rows[0];
    if (!current || !intent || intent.ownerNonce !== input.ownerNonce
      || intent.externalMessageId !== input.externalMessageId
      || !['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) {
      throw new ConflictException({ code: 'INITIAL_INTENT_CONTEXT_CHANGED' });
    }

    const original = input.originalConversation;
    const originalCas = current.updated_at.getTime() === original.updatedAt.getTime()
      && current.status === original.status && current.attendant_user_id === original.attendantUserId
      && current.attendant_name === original.attendantName && current.attendant_origin === original.attendantOrigin;
    const ownsSlot = intent.slotReleasedAt === null;
    const hasOwner = current.attendant_user_id !== null || current.attendant_name !== null || current.attendant_origin !== null;
    const canAssign = !input.priorExists && originalCas && ownsSlot && (!hasOwner || current.attendant_user_id === input.actorId);
    if (canAssign) {
      await tx.conversation.updateMany({
        where: {
          id: input.conversationId, buId: input.buId, updatedAt: original.updatedAt,
          status: original.status as never, attendantUserId: original.attendantUserId,
          attendantName: original.attendantName, attendantOrigin: original.attendantOrigin,
        },
        data: { status: 'IN_SERVICE', attendantUserId: input.actorId, attendantName: input.actorName, attendantOrigin: 'INTERNO' },
      });
    }
    const completed = await tx.$queryRaw<Array<{ id: string }>>`
      UPDATE initial_message_intents
      SET state = 'SUCCEEDED'::"InitialMessageIntentState",
          slot_released_at = CASE WHEN slot_released_at IS NULL THEN clock_timestamp() ELSE slot_released_at END,
          updated_at = clock_timestamp()
      WHERE id = ${input.intent.id}
        AND owner_nonce = ${input.ownerNonce}
        AND external_message_id = ${input.externalMessageId}
        AND state IN ('EXTERNAL_ACCEPTED'::"InitialMessageIntentState", 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'::"InitialMessageIntentState")
        AND slot_released_at IS NOT DISTINCT FROM ${intent.slotReleasedAt}
      RETURNING id
    `;
    if (completed.length !== 1) throw new ConflictException({ code: 'INITIAL_INTENT_CONTEXT_CHANGED' });
  }

  private async finishUnknown(
    input: SendOutboundInput,
    conversation: OutboundConversation,
    context: ChannelOperationContext,
    result: Extract<ChannelSendResult, { outcome: 'UNKNOWN' }>,
  ): Promise<never> {
    if (result.evidence === 'TRANSPORT_UNCONFIRMED') {
      const state = await this.contextState(context);
      if (state === 'CHANGED') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
      }
      throw new BadRequestException({ code: result.legacyCode, outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
    }

    if (await this.contextState(context) === 'CHANGED') {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
    }

    try {
      await this.acceptance.recordAmbiguousOutbound(this.acceptanceInput(input, conversation, context));
    } catch {
      const state = await this.contextState(context);
      if (state === 'CHANGED') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
      }
      throw new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
    }

    const state = await this.contextState(context);
    if (state === 'CHANGED') {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'RECORDED', error: FIXED_UNKNOWN });
    }
    throw new ConflictException({
      code: 'EXTERNAL_MESSAGE_ID_MISSING', outcome: 'AMBIGUOUS_SEND_RECORDED', evidence: 'ACK_WITHOUT_ID',
      diagnosticPersistence: 'RECORDED', error: 'O canal aceitou o envio sem confirmar o ID externo. Verifique a conversa antes de tentar novamente.',
    });
  }

  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
    externalMessageId: string,
  ): MessageAcceptanceInput;
  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
  ): Omit<MessageAcceptanceInput, 'externalMessageId'>;
  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
    externalMessageId?: string,
  ): MessageAcceptanceInput | Omit<MessageAcceptanceInput, 'externalMessageId'> {
    const attribution = input.attribution;
    return {
      ...(externalMessageId ? { externalMessageId } : {}),
      providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId,
      generation: context.generation,
      pairingEpoch: context.pairingEpoch,
      buId: context.buId,
      channelOrigin: context.channelOrigin,
      contact: conversation.contact,
      contactType: conversation.contactType,
      conversationId: conversation.id,
      direction: 'OUT',
      messageType: 'TEXTO',
      content: input.text,
      authorUserId: attribution.kind === 'BFF' ? attribution.userId || null : null,
      authorName: attribution.name,
      senderResult: true,
    };
  }

  private async contextState(context: ChannelOperationContext) {
    try { return await this.resolver.contextAfterDispatch(context); }
    catch { return 'UNKNOWN' as const; }
  }

  private async validateDispatchContext(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
    conversationId: string,
    checkWindow = true,
  ): Promise<DispatchClaimEligibility> {
    const current = await this.resolver.validateOperationContextInTransaction(tx, expected, selectedValue);
    if (!current) return { eligible: false, windowExpiresAt: null };
    if (!checkWindow || !expected.requiresWindow) return { eligible: true, windowExpiresAt: null };
    const window = await this.windows.inspectInTransaction(tx, {
      conversationId,
      providerResourceIdentityId: expected.providerResourceIdentityId,
    });
    return { eligible: window.open, windowExpiresAt: window.expiresAt };
  }

  private initialRequestRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value) ? value as Record<string, Prisma.JsonValue> : null;
  }

  private originalConversationSnapshot(value: Prisma.JsonValue | undefined): InitialConversationSnapshot | null {
    if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
    const row = value as Record<string, Prisma.JsonValue>;
    const updatedAt = typeof row.updatedAt === 'string' ? new Date(row.updatedAt) : null;
    if (!updatedAt || !Number.isFinite(updatedAt.getTime()) || typeof row.status !== 'string'
      || row.attendantUserId !== null && typeof row.attendantUserId !== 'string'
      || row.attendantName !== null && typeof row.attendantName !== 'string'
      || row.attendantOrigin !== null && typeof row.attendantOrigin !== 'string') return null;
    return { updatedAt, status: row.status as InitialConversationSnapshot['status'],
      attendantUserId: row.attendantUserId as string | null, attendantName: row.attendantName as string | null,
      attendantOrigin: row.attendantOrigin as InitialConversationSnapshot['attendantOrigin'] };
  }

  private async readBack(
    conversation: { id: string; buId: string; contact: string },
    context: ChannelOperationContext,
    externalMessageId: string,
  ) {
    try {
      return await this.findConfirmedOutbound({
        providerResourceIdentityId: context.providerResourceIdentityId,
        externalMessageId, conversationId: conversation.id, buId: conversation.buId,
        contact: conversation.contact, channelOrigin: context.channelOrigin,
      });
    } catch { return null; }
  }

  private async findConfirmedOutbound(input: {
    providerResourceIdentityId: string; externalMessageId: string; conversationId: string;
    buId: string; contact: string; channelOrigin: 'OFICIAL' | 'NAO_OFICIAL';
  }) {
    const message = await this.prisma.message.findUnique({
      where: { providerResourceIdentityId_externalId: {
        providerResourceIdentityId: input.providerResourceIdentityId,
        externalId: input.externalMessageId,
      } }, include: { conversation: true },
    });
    if (!message || message.direction !== 'OUT' || message.buId !== input.buId
      || message.channelOrigin !== input.channelOrigin || message.conversation.contact !== input.contact
      || message.conversationId !== input.conversationId) return null;
    return message;
  }

  private async finalizeOutbound(input: {
    conversationId: string; buId: string; contact: string; contactType: 'PESSOA' | 'GRUPO'; attribution: OutboundAttribution;
  }) {
    return this.prisma.$transaction(async (tx) => {
      await tx.$queryRaw`SELECT id FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId} FOR UPDATE`;
      const current = await tx.conversation.findFirst({
        where: { id: input.conversationId, buId: input.buId, contact: input.contact },
      });
      if (!current || current.contactType !== input.contactType) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
      if (input.attribution.kind === 'BOT') return current;

      const hasOwner = current.attendantUserId !== null || current.attendantName !== null || current.attendantOrigin !== null;
      return tx.conversation.update({ where: { id: current.id }, data: {
        lastMessageAt: new Date(),
        status: input.contactType === 'GRUPO' ? undefined : 'IN_SERVICE',
        ...(hasOwner || input.contactType === 'GRUPO' ? {} : input.attribution.kind === 'BFF'
          ? { attendantUserId: input.attribution.userId || null, attendantName: input.attribution.name, attendantOrigin: 'INTERNO' }
          : { attendantUserId: null, attendantName: input.attribution.name, attendantOrigin: 'EXTERNO' }),
      } });
    });
  }

  private asBlocked(error: HttpException): HttpException {
    const response = error.getResponse();
    const detail = typeof response === 'object' && response !== null ? response as Record<string, unknown> : { error: response };
    return new HttpException({ ...detail, outcome: 'BLOCKED' }, error.getStatus());
  }

  private blocked(reason: Extract<ChannelSendResult, { outcome: 'BLOCKED' }>['reason']): HttpException {
    if (reason === 'CANAL_AUSENTE') return new BadRequestException({ code: reason, outcome: 'BLOCKED', error: 'Esta BU não tem canal conectado.' });
    return new ConflictException({ code: reason, outcome: 'BLOCKED', error: 'O canal selecionado não está disponível para envio.' });
  }

  private acceptedIncomplete(contextState: 'CURRENT' | 'CHANGED' | 'UNKNOWN', localMessageState: 'RECORDED' | 'UNCONFIRMED'): HttpException {
    if (contextState === 'CHANGED') {
      return new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
    }
    return new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
  }

  private initialLocalIncomplete(attemptId: string, receiptPersistence: 'RECORDED' | 'UNCONFIRMED', code = 'INITIAL_LOCAL_ACCEPTANCE_UNCONFIRMED') {
    return new ServiceUnavailableException({
      code, outcome: 'ACCEPTED_LOCAL_INCOMPLETE', attemptId, state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED',
      providerAcceptance: 'CONFIRMED', receiptPersistence,
      localMessageState: 'UNCONFIRMED', recoveryAction: 'RECONCILE', error: FIXED_LOCAL_INCOMPLETE,
    });
  }
}

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (value && typeof value === 'object') {
    const record = value as Record<string, unknown>;
    return `{${Object.keys(record).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(record[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}

function sameContext(a: ChannelOperationContext, b: ChannelOperationContext): boolean {
  return canonicalJson(a) === canonicalJson(b);
}
```

### api-app/src/domain/inbox/message-acceptance.service.ts

SHA256 `285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
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
  /** Present only when derived from a verified signed Meta inbound message. */
  officialInboundAt?: Date | null;
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
    this.validateAcceptanceInput(input);
    try {
      return await this.prisma.$transaction((tx) => this.acceptInTransaction(tx, input), {
        isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted,
      });
    } catch (error) {
      // A concurrent insert may win after our initial lookup. The whole failed
      // transaction has rolled back before the exact-key readback and retry.
      if (!isUniqueViolation(error)) throw error;
      const prior = await this.prisma.message.findUnique({
        where: { providerResourceIdentityId_externalId: {
          providerResourceIdentityId: input.providerResourceIdentityId,
          externalId: input.externalMessageId,
        } }, include: { conversation: true },
      });
      if (!prior) throw error;
      return this.prisma.$transaction((tx) => this.acceptInTransaction(tx, input), {
        isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted,
      });
    }
  }

  /**
   * The same Message owner primitive used by normal acceptance and initial-send
   * completion. The caller owns the short transaction; no provider I/O belongs
   * here. `beforeConversationMutation` runs after identity validation and before
   * this method mutates the conversation timestamp, allowing initial completion
   * to apply its captured pre-HTTP owner/status CAS in the required order.
   */
  async acceptInTransaction(
    tx: Prisma.TransactionClient,
    input: MessageAcceptanceInput,
    beforeConversationMutation?: (tx: Prisma.TransactionClient, priorExists: boolean) => Promise<void>,
  ): Promise<MessageAcceptanceResult> {
    this.validateAcceptanceInput(input);
    const managedLifecycle = await this.lockAndValidateCurrentIdentity(tx, input);
    const key = { providerResourceIdentityId: input.providerResourceIdentityId, externalId: input.externalMessageId };
    const prior = await tx.message.findUnique({ where: { providerResourceIdentityId_externalId: key }, include: { conversation: true } });
    await beforeConversationMutation?.(tx, Boolean(prior));
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
        officialInboundAt: this.qualifiedOfficialTimestamp(input, managedLifecycle),
        authorUserId: input.senderResult ? input.authorUserId ?? null : null,
        authorName: input.senderResult ? input.authorName ?? null : null,
      },
    });
    if (input.direction === 'IN') await this.confirmInboundReceipt(tx, input);
    return { conversation, message, creationWinner: true, reconciled: false, conversationCreated, reopened };
  }

  private validateAcceptanceInput(input: MessageAcceptanceInput): void {
    if (!input.externalMessageId?.trim()) throw new BadRequestException({ code: 'EXTERNAL_MESSAGE_ID_REQUIRED' });
    if (!input.providerResourceIdentityId || !input.channelId || !input.buId) {
      throw new BadRequestException({ code: 'VERIFIED_RESOURCE_REQUIRED' });
    }
  }

  private async confirmInboundReceipt(tx: Prisma.TransactionClient, input: MessageAcceptanceInput): Promise<void> {
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

  private qualifiedOfficialTimestamp(input: MessageAcceptanceInput, managedLifecycle: boolean): Date | null {
    const timestamp = input.officialInboundAt;
    if (!managedLifecycle || input.direction !== 'IN' || input.channelOrigin !== 'OFICIAL' || !(timestamp instanceof Date)) return null;
    const value = timestamp.getTime();
    return Number.isSafeInteger(value) && value > 0 && value <= Date.now() ? timestamp : null;
  }

  /** Persist an explicitly ambiguous result after a provider accepted a send but returned no key. */
  async recordAmbiguousOutbound(input: Omit<MessageAcceptanceInput, 'externalMessageId' | 'status'>): Promise<Prisma.MessageGetPayload<object>> {
    if (input.direction !== 'OUT' || !input.senderResult) throw new BadRequestException({ code: 'OUTBOUND_RESULT_REQUIRED' });
    return this.prisma.$transaction(async (tx) => {
      await this.lockAndValidateCurrentIdentity(tx, input);
      const conversation = await tx.conversation.findFirst({ where: { id: input.conversationId, buId: input.buId, contact: input.contact } });
      if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
      await tx.conversation.update({ where: { id: conversation.id }, data: { lastMessageAt: new Date() } });
      return tx.message.create({ data: {
        conversationId: conversation.id, buId: input.buId, direction: 'OUT', messageType: input.messageType,
        content: input.content ?? null, channelOrigin: input.channelOrigin, status: 'FALHOU', externalId: null,
        providerResourceIdentityId: input.providerResourceIdentityId, authorUserId: input.authorUserId ?? null,
        authorName: input.authorName ?? null,
      } });
    });
  }

  private async lockAndValidateCurrentIdentity(tx: Prisma.TransactionClient, input: VerifiedResourceContext): Promise<boolean> {
    // Retirement/renewal must update this same identity row before changing the
    // channel epoch. The lock is held through message commit as the ingress fence.
    const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null; managed_lifecycle: boolean }>>`
      SELECT id, bu_id, current_channel_id, managed_lifecycle
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
    return identity.managed_lifecycle === true;
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

### api-app/src/domain/inbox/conversations.service.ts

SHA256 `6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c`. Exact byte-identical E64 unchanged support; full source was reviewed in E64/r5; selected current seal confirms unchanged bytes.

Exact E64-unchanged conversation service, previously reviewed in full E64/r5 and bound to the current source hash. Its scoped load/list methods restrict access to authorized BU IDs, provide ordered conversation summaries, and its timeline method implements cursor pagination plus explicit read marking. It also resolves one or many window states and delegates ordinary reply, assignment and closure through the inbox boundary. Current changed BFF endpoints/controller, channel-window policy and full current E2E behavior remain supplied; this unchanged supporting service is summarized under its sealed E64 baseline.

Complete current case declaration list from the exact unchanged file:


### api-app/src/domain/inbox/incoming.service.ts

SHA256 `390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { Inject, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { RealtimeService } from '../../realtime/realtime.service';
import { TYPEBOT_CLIENT, TypebotClient } from '../../integrations/typebot/typebot.client';
import { MessageAcceptanceService } from './message-acceptance.service';
import { OutboundService } from './outbound.service';
import type { ChannelOrigin } from '../channels/transport/channel';

export type CanalDeOrigem = ChannelOrigin;

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
  officialInboundAt?: Date | null;
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
    @Inject(TYPEBOT_CLIENT) private readonly typebot: TypebotClient,
    private readonly acceptance: MessageAcceptanceService,
    private readonly outbound: OutboundService,
  ) {}

  async registrar(m: MensagemRecebida) {
    const accepted = await this.acceptance.accept({
      providerResourceIdentityId: m.providerResourceIdentityId, channelId: m.channelId, generation: m.generation,
      pairingEpoch: m.pairingEpoch, buId: m.buId, channelOrigin: m.canal, externalMessageId: m.externalId ?? '',
      contact: m.contato, contactType: m.ehGrupo ? 'GRUPO' : 'PESSOA', displayName: m.nomeExibicao,
      direction: m.direcao, messageType: m.tipo, content: m.conteudo, authorName: m.autorNome,
      officialInboundAt: m.officialInboundAt,
    });
    const { conversation: conversa, message: mensagem, creationWinner } = accepted;
    if (creationWinner) {
      this.realtime.publicarNaBu(m.buId, { tipo: 'mensagem', conversaId: conversa.id, contato: conversa.contact, direcao: m.direcao, canal: m.canal, naoLidas: conversa.unreadCount });
      if (m.direcao === 'IN' && m.tipo === 'TEXTO' && m.conteudo?.trim()) {
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
    const botId = gatilho.bot.publishedTypebotId;
    if (!botId) return;
    const atual = await this.prisma.typebotSession.findUnique({ where: { botId_buId_contato: { botId: gatilho.botId, buId, contato } } });
    if (atual && (atual.mantenedoraId !== bu.mantenedoraId || atual.buId !== buId || atual.botId !== gatilho.botId || gatilho.bot.mantenedoraId !== bu.mantenedoraId)) return;
    const resposta = atual?.ativo ? await this.typebot.continuar(atual.sessionId, texto) : await this.typebot.iniciar(botId, contato, texto);
    const sessionId = 'sessionId' in resposta && typeof resposta.sessionId === 'string' ? resposta.sessionId : null;
    if (!atual && sessionId) await this.prisma.typebotSession.create({ data: { botId: gatilho.botId, mantenedoraId: gatilho.bot.mantenedoraId, buId, contato, sessionId } });
    for (const mensagem of resposta.messages) {
      const saida = textoDaRespostaTypebot(mensagem);
      if (!saida) continue;
      await this.outbound.send({
        conversationId,
        buId,
        text: saida,
        attribution: { kind: 'BOT', name: 'Typebot' },
        ingress: {
          channelId: incoming.channelId,
          providerResourceIdentityId: incoming.providerResourceIdentityId,
          channelOrigin: incoming.canal,
          generation: incoming.generation,
          pairingEpoch: incoming.pairingEpoch,
        },
      });
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

### api-app/src/integrations/channels/meta-channel.ts

SHA256 `99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import type { Channel, ChannelMessage, ChannelMessageKind, ChannelSendOptions, ChannelSendResult } from '../../domain/channels/transport/channel';
import type { MetaClient } from '../meta/meta.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';
import { MetaInitialMessageClient } from '../meta/initial-message.client';
import { metaAccountReference } from './account-reference';

class BoundMetaChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: MetaClient,
    private readonly initialClient: MetaInitialMessageClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  readonly supportedKinds: readonly ChannelMessageKind[] = Object.freeze(['text', 'approved-template']);

  async sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult> {
    // Approved templates always use the initial protocol path; text selects
    // that path explicitly so ordinary text retains its legacy wire format.
    if (options?.purpose === 'initial' || message.kind === 'approved-template') {
      const claimFence = options?.beforeDispatch;
      if (!claimFence) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
      if (!this.credential.phoneNumberId || !this.credential.wabaId || !this.credential.accessToken) {
        return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
      }
      if (!/^\d{8,15}$/.test(message.recipientRef)) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
      const template = message.kind === 'approved-template' ? message.template : null;
      const managementContext = template?.managementContext;
      return this.initialClient.sendInitialMessage({
        wabaId: this.credential.wabaId,
        phoneNumberId: this.credential.phoneNumberId,
        recipientE164: `+${message.recipientRef}`,
        accessToken: this.credential.accessToken,
        accountReference: metaAccountReference(this.credential.wabaId),
        payload: message,
        ...(managementContext ? { managementContext } : {}),
        beforeDispatch: async () => {
          const contextCurrent = await this.beforeDispatch().catch(() => false);
          if (!contextCurrent) return false;
          try { return await claimFence(); } catch { return false; }
        },
      });
    }
    if (message.kind !== 'text') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    if (!this.credential.phoneNumberId || !this.credential.accessToken) {
      return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
    }
    if (options?.beforeDispatch) {
      let dispatched: boolean;
      try { dispatched = await options.beforeDispatch(); } catch { dispatched = false; }
      if (!dispatched) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    try {
      return await this.client.enviarTexto(
        this.credential.phoneNumberId,
        message.recipientRef,
        message.text,
        this.credential.accessToken,
      );
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
    }
  }
}

export class MetaChannelFactory extends ChannelAdapterFactory {
  readonly origin = 'OFICIAL' as const;
  constructor(private readonly client: MetaClient, private readonly initialClient: MetaInitialMessageClient) { super(); }
  locallyConfigured(): boolean { return this.client.canSendText(); }
  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundMetaChannel(credential, this.client, this.initialClient, beforeDispatch);
  }
}
```

### api-app/src/integrations/channels/evolution-channel.ts

SHA256 `6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import type { Channel, ChannelMessage, ChannelMessageKind, ChannelSendOptions, ChannelSendResult } from '../../domain/channels/transport/channel';
import type { EvolutionClient } from '../evolution/evolution.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';

class BoundEvolutionChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: EvolutionClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  readonly supportedKinds: readonly ChannelMessageKind[] = Object.freeze(['text']);

  async sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult> {
    if (message.kind !== 'text') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    if (options?.purpose === 'initial' && !options.beforeDispatch) {
      return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (options?.beforeDispatch) {
      let dispatched: boolean;
      try { dispatched = await options.beforeDispatch(); } catch { dispatched = false; }
      if (!dispatched) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (!this.credential.evolutionInstanceName) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    try {
      return await this.client.enviarTexto(this.credential.evolutionInstanceName, message.recipientRef, message.text);
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
    }
  }
}

export class EvolutionChannelFactory extends ChannelAdapterFactory {
  readonly origin = 'NAO_OFICIAL' as const;
  constructor(private readonly client: EvolutionClient) { super(); }
  locallyConfigured(): boolean { return this.client.configurado(); }
  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundEvolutionChannel(credential, this.client, beforeDispatch);
  }
}
```

### api-app/src/integrations/channels/prisma-channel-resolver.ts

SHA256 `bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver, type ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import {
  ChannelResolver,
  type ChannelAvailability,
  type InitialChannelReference,
  type ConversationAvailabilityReference,
  type ChannelOperationContext,
  type ChannelOrigin,
  type ConversationChannelReference,
  type ResolvedChannelOperation,
  type VerifiedIngressChannelReference,
} from '../../domain/channels/transport/channel';
import { ChannelAdapterRegistry } from './channel-adapter-registry';
import { OfficialChannelWindowPolicy, type OfficialWindowState } from '../../domain/inbox/channel-window-policy';
import { metaAccountReference } from './account-reference';

type Candidate = {
  id: string;
  buId: string;
  type: ChannelOrigin;
  status: string;
  generation: number;
  pairingEpoch: number;
  verifiedEpoch: number | null;
  ownNumberVerified: boolean;
  providerConnectionState: string;
  receiptVerifiedAt: Date | null;
  requiresWindow: boolean;
  wabaId: string | null;
  providerIdentities: Array<{ id: string; buId: string; provider: ChannelOrigin; currentChannelId: string | null; managedLifecycle: boolean }>;
};

@Injectable()
export class PrismaChannelResolver extends ChannelResolver {
  constructor(
    private readonly prisma: PrismaService,
    private readonly credentials: ChannelCredentialResolver,
    private readonly adapters: ChannelAdapterRegistry,
    private readonly windows: OfficialChannelWindowPolicy,
  ) { super(); }

  async resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation> {
    const { candidate } = await this.selectForConversation(reference);
    return this.bind(candidate);
  }

  async resolveForInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    if (!candidate) this.throwUnavailable('CANAL_SELECIONADO_INDISPONIVEL');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    const operation = await this.bind(candidate);
    if (!operation.channel.supportedKinds.includes(reference.kind)) this.throwUnavailable('UNSUPPORTED_KIND');
    if (reference.kind === 'text' && operation.context.requiresWindow) {
      const window = await this.windows.inspect({
        conversationId: conversation.id,
        providerResourceIdentityId: operation.context.providerResourceIdentityId,
      });
      if (!window.open) this.throwUnavailable('JANELA_FECHADA');
    }
    return operation;
  }

  async resolveForInitialOptions(reference: ConversationChannelReference & { channelId: string }): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId }, select: { id: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    if (!candidate) this.throwUnavailable('CANAL_SELECIONADO_INDISPONIVEL');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    return this.bind(candidate);
  }

  async resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true, contact: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    const identity = candidate?.providerIdentities.find((item) => item.id === reference.providerResourceIdentityId);
    if (!candidate || candidate.type !== reference.channelOrigin || candidate.generation !== reference.generation
      || candidate.pairingEpoch !== reference.pairingEpoch || !identity || identity.buId !== reference.buId
      || identity.provider !== reference.channelOrigin || identity.currentChannelId !== reference.channelId
      || !identity.managedLifecycle) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    return this.bind(candidate);
  }

  async hasReadyChannelForNewConversation(buId: string): Promise<boolean> {
    const candidates = await this.channels(buId);
    for (const candidate of candidates) {
      if (!await this.inspectCandidate(candidate)) return true;
    }
    return false;
  }

  async inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability> {
    try {
      const conversation = await this.prisma.conversation.findFirst({
        where: { id: reference.conversationId, buId: reference.buId }, select: { id: true },
      });
      if (!conversation) return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
      const { candidate, selectionReason, selectedOrigin } = await this.selectCandidate(reference);
      if (!candidate) {
        return this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL');
      }
      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      let reason: ChannelAvailability['reason'] = null;
      if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
        || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
        reason = 'CHANNEL_IDENTITY_NOT_VERIFIED';
      } else if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
        || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
        || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
        || !this.adapters.locallyConfigured(candidate.type)) {
        reason = 'CHANNEL_NOT_READY';
      } else if (candidate.type === 'OFICIAL') {
        const credential = await this.credentials.inspectActiveCredential(candidate.id, candidate.generation);
        if (!credential.ready) reason = 'PENDING_CREDENTIAL';
      }

      const currentIdentity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      const window = candidate.requiresWindow && currentIdentity
        ? await this.windows.inspect({ conversationId: reference.conversationId, providerResourceIdentityId: currentIdentity.id })
        : { open: !candidate.requiresWindow, expiresAt: null };
      if (!reason && candidate.requiresWindow && !window.open) reason = 'JANELA_FECHADA';
      return {
        available: reason === null,
        reason,
        channelOrigin: candidate.type,
        requiresWindow: candidate.requiresWindow,
        windowOpen: window.open,
        expiresAt: window.expiresAt,
      };
    } catch {
      return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
    }
  }

  /** Batch-only GET view: BU bindings and credential metadata are read once for the page. */
  async inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>> {
    if (!references.length) return new Map();
    const buId = references[0].buId;
    if (references.some((reference) => reference.buId !== buId)) {
      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
    }
    try {
      const ids = references.map(({ conversationId }) => conversationId);
      const channels = await this.channels(buId);
      const credentialState = await this.credentials.inspectActiveCredentials(channels
        .filter((candidate) => candidate.type === 'OFICIAL')
        .map(({ id, generation }) => ({ channelId: id, generation })));
      const selectedById = new Map<string, {
        candidate: Candidate | null;
        selectedOrigin: ChannelOrigin | null;
        selectionReason: ChannelAvailability['reason'] | null;
      }>();
      for (const reference of references) {
        let selectedOrigin = reference.latestMessageOrigin;
        let candidate: Candidate | null;
        let selectionReason: ChannelAvailability['reason'] | null = null;
        if (selectedOrigin) {
          candidate = channels.find((item) => item.type === selectedOrigin) ?? null;
          if (!candidate) selectionReason = 'CANAL_SELECIONADO_INDISPONIVEL';
        } else if (channels.length === 0) {
          candidate = null; selectionReason = 'CANAL_AUSENTE';
        } else if (channels.length > 1) {
          candidate = null; selectionReason = 'CANAL_AMBIGUO';
        } else {
          candidate = channels[0]; selectedOrigin = candidate.type;
        }
        selectedById.set(reference.conversationId, { candidate, selectedOrigin, selectionReason });
      }
      const windowRefs = references.flatMap(({ conversationId }) => {
        const candidate = selectedById.get(conversationId)?.candidate;
        const identity = candidate?.providerIdentities.find((item) => item.currentChannelId === candidate.id);
        return candidate?.requiresWindow && identity
          ? [{ conversationId, providerResourceIdentityId: identity.id }]
          : [];
      });
      const windows = windowRefs.length
        ? await this.windows.inspectMany(windowRefs)
        : new Map<string, OfficialWindowState>();
      const result = new Map<string, ChannelAvailability>();
      for (const id of ids) {
        const { candidate, selectedOrigin, selectionReason } = selectedById.get(id)!;
        if (!candidate) {
          result.set(id, this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL'));
          continue;
        }
        const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
        let reason: ChannelAvailability['reason'] = null;
        if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
          || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
          reason = 'CHANNEL_IDENTITY_NOT_VERIFIED';
        } else if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
          || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
          || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
          || !this.adapters.locallyConfigured(candidate.type)) {
          reason = 'CHANNEL_NOT_READY';
        } else if (candidate.type === 'OFICIAL' && !credentialState.get(candidate.id)?.ready) {
          reason = 'PENDING_CREDENTIAL';
        }
        let windowOpen = true;
        let expiresAt: Date | null = null;
        if (candidate.requiresWindow) {
          const state = windows.get(id);
          windowOpen = state?.open ?? false;
          expiresAt = state?.expiresAt ?? null;
          if (!reason && !windowOpen) reason = 'JANELA_FECHADA';
        }
        result.set(id, {
          available: reason === null, reason, channelOrigin: candidate.type,
          requiresWindow: candidate.requiresWindow, windowOpen, expiresAt,
        });
      }
      return result;
    } catch {
      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
    }
  }

  async contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
    try {
      const status = await this.contextStatus(context, false);
      return status;
    } catch {
      return 'UNKNOWN';
    }
  }

  async validateOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
  ): Promise<boolean> {
    if (!selectedValue || typeof selectedValue !== 'object' || Array.isArray(selectedValue)) return false;
    const selected = selectedValue as Record<string, Prisma.JsonValue>;
    const tuple = [
      'channelId', 'buId', 'channelOrigin', 'providerResourceIdentityId', 'generation',
      'pairingEpoch', 'activeCredentialVersion', 'requiresWindow', 'providerAccountReference',
    ] as const;
    if (tuple.some((key) => selected[key] !== expected[key])) return false;

    // Pin mutable readiness/bindings without waiting after identity acquisition.
    // ST-05 observation refresh takes channel/credential locks before identity;
    // NOWAIT keeps this established identity-first path finite and cycle-safe.
    const businessUnits = await tx.$queryRaw<Array<{ id: string }>>`
      SELECT id FROM business_units WHERE id = ${expected.buId} AND status = 'ATIVO' FOR SHARE NOWAIT`;
    if (!businessUnits[0]) return false;
    const channelPins = await tx.$queryRaw<Array<{ id: string }>>`
      SELECT id FROM bu_channels WHERE id = ${expected.channelId} AND bu_id = ${expected.buId} FOR SHARE NOWAIT`;
    if (!channelPins[0]) return false;
    if (expected.channelOrigin === 'OFICIAL') {
      const credentialPins = await tx.$queryRaw<Array<{ channel_id: string }>>`
        SELECT channel_id FROM channel_credentials WHERE channel_id = ${expected.channelId} FOR SHARE NOWAIT`;
      if (!credentialPins[0]) return false;
    }

    const identity = await tx.providerResourceIdentity.findFirst({
      where: {
        id: expected.providerResourceIdentityId,
        buId: expected.buId,
        provider: expected.channelOrigin,
        currentChannelId: expected.channelId,
        managedLifecycle: true,
      },
      select: { id: true, externalResourceId: true },
    });
    if (!identity) return false;

    const channel = await tx.buChannel.findFirst({
      where: {
        id: expected.channelId,
        buId: expected.buId,
        type: expected.channelOrigin,
        generation: expected.generation,
        pairingEpoch: expected.pairingEpoch,
        ownNumberVerified: true,
        verifiedEpoch: expected.pairingEpoch,
        status: 'CONECTADO',
        receiptVerifiedAt: { not: null },
        providerConnectionState: expected.channelOrigin === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
      },
      select: {
        wabaId: true,
        phoneNumberId: true,
        evolutionInstanceName: true,
        requiresWindow: true,
        credential: { select: { generation: true, version: true } },
      },
    });
    const providerResource = expected.channelOrigin === 'OFICIAL' ? channel?.phoneNumberId : channel?.evolutionInstanceName;
    if (!channel || channel.requiresWindow !== expected.requiresWindow || providerResource !== identity.externalResourceId
      || (channel.wabaId ? metaAccountReference(channel.wabaId) : null) !== expected.providerAccountReference) return false;
    if (expected.channelOrigin === 'OFICIAL' && (!channel.credential
      || channel.credential.generation !== expected.generation
      || channel.credential.version !== expected.activeCredentialVersion)) return false;
    return true;
  }

  async validateAcceptedOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
  ): Promise<boolean> {
    if (!selectedValue || typeof selectedValue !== 'object' || Array.isArray(selectedValue)) return false;
    const selected = selectedValue as Record<string, Prisma.JsonValue>;
    const tuple = ['channelId', 'buId', 'channelOrigin', 'providerResourceIdentityId', 'generation', 'pairingEpoch',
      'activeCredentialVersion', 'requiresWindow', 'providerAccountReference'] as const;
    if (tuple.some((key) => selected[key] !== expected[key])) return false;
    const [businessUnit, identity, channel] = await Promise.all([
      tx.businessUnit.findFirst({ where: { id: expected.buId, status: 'ATIVO' }, select: { id: true } }),
      tx.providerResourceIdentity.findFirst({ where: {
        id: expected.providerResourceIdentityId, buId: expected.buId, provider: expected.channelOrigin,
        currentChannelId: expected.channelId, managedLifecycle: true,
      }, select: { id: true, externalResourceId: true } }),
      tx.buChannel.findFirst({ where: {
        id: expected.channelId, buId: expected.buId, type: expected.channelOrigin,
        generation: expected.generation, pairingEpoch: expected.pairingEpoch,
        ownNumberVerified: true, verifiedEpoch: expected.pairingEpoch,
      }, select: { wabaId: true, phoneNumberId: true, evolutionInstanceName: true, requiresWindow: true } }),
    ]);
    if (!businessUnit || !identity || !channel || channel.requiresWindow !== expected.requiresWindow) return false;
    const providerResource = expected.channelOrigin === 'OFICIAL' ? channel.phoneNumberId : channel.evolutionInstanceName;
    return providerResource === identity.externalResourceId
      && (channel.wabaId ? metaAccountReference(channel.wabaId) : null) === expected.providerAccountReference;
  }

  private async bind(candidate: Candidate): Promise<ResolvedChannelOperation> {
    const availability = await this.inspectCandidate(candidate);
    if (availability) this.throwUnavailable(availability);
    const credential = await this.credentials.resolve(candidate.id);
    const context: ChannelOperationContext = Object.freeze({
      channelId: candidate.id,
      buId: candidate.buId,
      channelOrigin: candidate.type,
      providerResourceIdentityId: credential.providerResourceIdentityId,
      generation: credential.generation,
      pairingEpoch: credential.pairingEpoch,
      activeCredentialVersion: credential.activeCredentialVersion,
      requiresWindow: candidate.requiresWindow,
      providerAccountReference: credential.wabaId ? metaAccountReference(credential.wabaId) : null,
    });
    if (!this.sameCredentialContext(candidate, credential)) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    const factory = this.adapters.get(candidate.type);
    if (!factory) throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
    const channel = factory.create(credential, async () => {
      try { return (await this.contextStatus(context, true)) === 'CURRENT'; }
      catch { return false; }
    });
    return { channel, context };
  }

  private async inspectCandidate(candidate: Candidate): Promise<ChannelAvailability['reason']> {
    const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
    if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
      || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
      return 'CHANNEL_IDENTITY_NOT_VERIFIED';
    }
    if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
      || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
      || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
      || !this.adapters.locallyConfigured(candidate.type)) return 'CHANNEL_NOT_READY';
    if (candidate.type === 'OFICIAL' && !(await this.credentials.inspectActiveCredential(candidate.id, candidate.generation)).ready) {
      return 'PENDING_CREDENTIAL';
    }
    return null;
  }

  private async selectForConversation(reference: ConversationChannelReference) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true, contact: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const { candidate, selectionReason } = await this.selectCandidate(reference);
    if (!candidate) this.throwUnavailable(selectionReason ?? 'CANAL_AUSENTE');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    if (candidate.requiresWindow) {
      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      const window = identity
        ? await this.windows.inspect({ conversationId: conversation.id, providerResourceIdentityId: identity.id })
        : { open: false, expiresAt: null };
      if (!window.open) this.throwUnavailable('JANELA_FECHADA');
    }
    return { conversation, candidate };
  }

  private async selectCandidate(reference: ConversationChannelReference): Promise<{
    candidate: Candidate | null; selectedOrigin: ChannelOrigin | null; selectionReason: ChannelAvailability['reason'] | null;
  }> {
    const latest = await this.prisma.message.findFirst({
      where: { conversationId: reference.conversationId },
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
      select: { channelOrigin: true },
    });
    const channels = await this.channels(reference.buId);
    if (latest) {
      const selectedOrigin = latest.channelOrigin as ChannelOrigin;
      const candidate = channels.find((channel) => channel.type === selectedOrigin) ?? null;
      return { candidate, selectedOrigin, selectionReason: candidate ? null : 'CANAL_SELECIONADO_INDISPONIVEL' };
    }
    if (channels.length === 0) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AUSENTE' };
    if (channels.length > 1) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AMBIGUO' };
    return { candidate: channels[0], selectedOrigin: channels[0].type, selectionReason: null };
  }

  private async channels(buId: string): Promise<Candidate[]> {
    return this.prisma.buChannel.findMany({
      where: { buId },
      select: {
        id: true, buId: true, type: true, wabaId: true, status: true, generation: true, pairingEpoch: true,
        verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
        receiptVerifiedAt: true, requiresWindow: true,
        providerIdentities: { select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } },
      },
    }) as unknown as Promise<Candidate[]>;
  }

  private async findCandidate(channelId: string, buId: string): Promise<Candidate | null> {
    const rows = await this.prisma.buChannel.findMany({ where: { id: channelId, buId }, select: {
      id: true, buId: true, type: true, wabaId: true, status: true, generation: true, pairingEpoch: true,
      verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
      receiptVerifiedAt: true, requiresWindow: true,
      providerIdentities: { select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } },
    } });
    return (rows[0] as unknown as Candidate | undefined) ?? null;
  }

  private async contextStatus(context: ChannelOperationContext, beforeDispatch: boolean): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
    const where: Prisma.BuChannelWhereInput = {
      id: context.channelId, buId: context.buId, type: context.channelOrigin,
      generation: context.generation, pairingEpoch: context.pairingEpoch,
      ownNumberVerified: true, verifiedEpoch: context.pairingEpoch,
      ...(beforeDispatch ? {
        status: 'CONECTADO', receiptVerifiedAt: { not: null },
        providerConnectionState: context.channelOrigin === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
      } : {}),
    };
    const channel = await this.prisma.buChannel.findFirst({
      where,
      select: { id: true, wabaId: true, credential: { select: { version: true, generation: true } },
        providerIdentities: { where: { id: context.providerResourceIdentityId }, select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } } },
    });
    const identity = channel?.providerIdentities[0];
    if (!channel || !identity || identity.buId !== context.buId || identity.provider !== context.channelOrigin
      || identity.currentChannelId !== context.channelId || !identity.managedLifecycle) {
      return 'CHANGED';
    }
    const currentAccountReference = channel.wabaId ? metaAccountReference(channel.wabaId) : null;
    if (currentAccountReference !== context.providerAccountReference) return 'CHANGED';
    if (context.channelOrigin === 'OFICIAL') {
      const credential = channel.credential;
      if (!credential || credential.generation !== context.generation) return 'CHANGED';
      if (beforeDispatch && credential.version !== context.activeCredentialVersion) return 'CHANGED';
    }
    return 'CURRENT';
  }

  private sameCredentialContext(candidate: Candidate, credential: ResolvedChannelCredential): boolean {
    const identity = candidate.providerIdentities.find((item) => item.id === credential.providerResourceIdentityId);
    return credential.channelId === candidate.id && credential.buId === candidate.buId
      && credential.provider === candidate.type && credential.generation === candidate.generation
      && (credential.wabaId ? metaAccountReference(credential.wabaId) : null) === (candidate.wabaId ? metaAccountReference(candidate.wabaId) : null)
      && credential.pairingEpoch === candidate.pairingEpoch && identity?.currentChannelId === candidate.id
      && identity?.buId === candidate.buId && identity.provider === candidate.type;
  }

  private unavailable(channelOrigin: ChannelOrigin | null, reason: ChannelAvailability['reason']): ChannelAvailability {
    return { available: false, reason, channelOrigin, requiresWindow: false, windowOpen: false, expiresAt: null };
  }

  private throwUnavailable(reason: ChannelAvailability['reason']): never {
    if (reason === 'CANAL_AUSENTE') throw new BadRequestException({ code: reason, error: 'Esta BU não tem canal conectado.' });
    if (reason === 'CANAL_AMBIGUO') throw new ConflictException({ code: reason, error: 'Selecione uma origem de conversa antes de responder.' });
    throw new ConflictException({ code: reason, error: reason === 'JANELA_FECHADA'
      ? 'Fora da janela de 24h da última mensagem recebida.'
      : 'O canal selecionado não está disponível para envio.' });
  }
}
```

### api-app/src/integrations/meta/initial-message.client.ts

SHA256 `e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721`. Exact byte-identical E64 unchanged support; full source was reviewed in E64/r5; selected current seal confirms unchanged bytes.

Exact E64-unchanged Meta protocol adapter, previously reviewed in full E64/r5 TQA and hash-bound to current bytes. It implements the private initial-message port with a final before-dispatch guard, verifies a template definition against the current catalog under a deadline, maps only the typed text or approved-template payload to Meta Graph wire format, and preserves unknown outcomes when preflight or POST cannot establish acceptance. It uses the pinned sender/resource supplied by the resolver and keeps ordinary transport on its legacy path. The unchanged client unit case names and wire assertions are summarized in the adjacent protocol-spec summary; current changed resolver/clock/pin and full causal tests remain present.

Complete current case declaration list from the exact unchanged file:


### api-app/src/integrations/message-templates/template-management.resolver.ts

SHA256 `1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { ConflictException, Injectable } from '@nestjs/common';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
import type {
  MessageTemplateProvider,
  ResolvedTemplateManagement,
  TemplateManagementContext,
  TemplateManagementResolver,
  TemplateReference,
} from '../../domain/message-templates/template-management.ports';
import { BoundMetaMessageTemplateProvider, MetaTemplateClient, TemplateManagementProviderError } from '../meta/message-template.client';
import { metaAccountReference } from '../channels/account-reference';

interface TemplateProviderFactory {
  create(context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider;
}

class OfficialTemplateProviderFactory implements TemplateProviderFactory {
  create(context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider {
    return new BoundMetaMessageTemplateProvider(context, credential, wabaId, new MetaTemplateClient());
  }
}

/** Explicit allowlist: unsupported origins have no placeholder/no-op provider. */
class TemplateProviderFactoryRegistry {
  private readonly factories = new Map([['OFICIAL', new OfficialTemplateProviderFactory()]]);

  create(origin: string, context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider {
    const factory = this.factories.get(origin);
    if (!factory) throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    return factory.create(context, credential, wabaId);
  }
}

@Injectable()
export class ScopedTemplateManagementResolver implements TemplateManagementResolver {
  private readonly factories = new TemplateProviderFactoryRegistry();

  constructor(private readonly prisma: PrismaService, private readonly credentials: ChannelCredentialResolver) {}

  async resolve(reference: TemplateReference, options?: { readonly transaction?: Prisma.TransactionClient }): Promise<ResolvedTemplateManagement> {
    const database = options?.transaction ?? this.prisma;
    const channel = await database.buChannel.findFirst({
      where: { id: reference.channelId, buId: reference.buId },
      include: { providerIdentities: true, bu: { select: { mantenedoraId: true } } },
    });
    if (!channel || channel.generation !== reference.expectedGeneration || channel.type !== 'OFICIAL'
      || !channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const identity = channel.providerIdentities.find((row) => row.currentChannelId === channel.id);
    if (!identity || !identity.managedLifecycle || identity.provider !== 'OFICIAL' || identity.buId !== channel.buId
      || !channel.phoneNumberId || identity.externalResourceId !== channel.phoneNumberId || !channel.wabaId) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const credentialMetadata = await this.credentials.inspectActiveCredential(channel.id, channel.generation, { provider: 'OFICIAL', buId: channel.buId }, options?.transaction);
    if (!credentialMetadata.ready || credentialMetadata.version === null) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const context: TemplateManagementContext = Object.freeze({
      mantenedoraId: channel.bu.mantenedoraId,
      buId: channel.buId,
      channelId: channel.id,
      providerResourceIdentityId: identity.id,
      generation: channel.generation,
      pairingEpoch: channel.pairingEpoch,
      activeCredentialVersion: credentialMetadata.version,
      accountReference: metaAccountReference(channel.wabaId),
    });
    const credential = async (): Promise<string> => {
      const current = await this.credentials.resolve(channel.id, 'template-management');
      if (current.provider !== 'OFICIAL' || current.buId !== context.buId || current.channelId !== context.channelId
        || current.providerResourceIdentityId !== context.providerResourceIdentityId || current.generation !== context.generation
        || current.pairingEpoch !== context.pairingEpoch || current.activeCredentialVersion !== context.activeCredentialVersion
        || current.wabaId !== channel.wabaId || current.phoneNumberId !== channel.phoneNumberId
        || metaAccountReference(current.wabaId ?? '') !== context.accountReference || !current.accessToken) {
        throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
      }
      return current.accessToken;
    };
    const provider = this.factories.create(channel.type, context, credential, channel.wabaId);
    return Object.freeze({ context, provider });
  }
}
```

### api-app/src/domain/message-templates/template-observation.service.ts

SHA256 `41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488`. Exact byte-identical E64 unchanged support; full source was reviewed in E64/r5; selected current seal confirms unchanged bytes.

This protected unchanged ST05 observation owner supplies the actual producer and lock ordering exercised by the new ST04 overlap regressions. It authorizes current user/BU/binding, derives a complete context key, acquires a bounded owner/fence lease, performs remote reads outside transaction, then applies observation/page or unavailable outcomes only under current authorization/context and exact lease fencing. Its persisted per-item available flag remains separate from page availability and authoring supported/eligible; old positional authoring flags are not recipient-send permission. TTL is 300 seconds with a minimum refresh interval; empty/malformed remote outcomes are explicit unavailable, not fresh usable templates. Exact readback classifies lost commit acknowledgment, keeps uncertainty and releases only its lease owner; no recipient send exists. The exact refreshDraft method plus complete ownsLease and authorization-transaction helpers must be embedded in the summary source references because those unchanged locks/availability guards matter directly to the new tests. Other unchanged ST05 recovery/projector/catalog detail is summarized here, with its exact full-source hash bound and prior full E64/r5 source review. ST04 renderer/coordinator/current resolver and all changed tests are supplied in full.

Complete current case declaration list from the exact unchanged file:


### api-app/src/surfaces/bff/conversations.controller.ts

SHA256 `0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { BadRequestException, Body, ConflictException, Controller, Get, HttpCode, NotFoundException, Param, Post, Query, Req, Res } from '@nestjs/common';
import type { Request, Response } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { RegistroDeAtividade } from '../../domain/historico/registro.service';
import { ator } from './setores.controller';
import { validarConsultaTimeline } from '../../domain/inbox/timeline-pagination';
import { ConversationStartService } from '../../domain/inbox/conversation-start.service';
import { InitialMessageService } from '../../domain/inbox/initial-message.service';
import { SessionService } from '../../infra/session/session.service';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';

const ABAS = ['QUEUED', 'IN_SERVICE', 'CLOSED'] as const;

/** A inbox por BU (ADR-0009): uma tela para os dois canais. */
@Controller('api/bff')
export class ConversationsController {
  constructor(
    private readonly access: AccessService,
    private readonly conversas: ConversationsService,
    private readonly registro: RegistroDeAtividade,
    private readonly conversationStart: ConversationStartService,
    private readonly initialMessages: InitialMessageService,
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
  ) {}

  @Post('business-units/:buId/conversations/open')
  @HttpCode(200)
  async abrirPorContato(
    @Param('buId') buId: string,
    @Body() body: { telefone?: unknown },
    @Req() req: Request,
    @Res({ passthrough: true }) response: Response,
  ) {
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    await this.assertActorTenant(req, buId);
    if (!body || typeof body !== 'object' || Object.keys(body).some((key) => key !== 'telefone')
      || typeof body.telefone !== 'string') {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    const result = await this.conversationStart.start(buId, body.telefone);
    if (result.created) {
      await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.conversa.aberta', ator(req), {
        buId,
        entidadeId: result.conversation.id,
        frase: { contato: result.conversation.contact },
      });
    }
    response.status(result.created ? 201 : 200);
    return {
      conversaId: result.conversation.id,
      criada: result.created,
      contact: result.conversation.contact,
    };
  }

  @Get('conversations/:id/start-options')
  async startOptions(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    return this.initialMessages.options({ conversationId: conversa.id, buId: conversa.buId });
  }

  @Post('conversations/:id/initial-message-preview')
  @HttpCode(200)
  async initialPreview(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    const message = this.initialMessageRequest(body, false);
    return this.initialMessages.preview({ conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id, message });
  }

  @Post('conversations/:id/initial-messages')
  async initialSend(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) response: Response) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    const key = req.header('Idempotency-Key') ?? '';
    const message = this.initialMessageRequest(body, true);
    const result = await this.initialMessages.submit({
      conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id, actorName: req.usuario!.nome,
      idempotencyKey: key, message: message as never,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
    });
    const { expiredPrepared, ...safeResult } = result;
    const active = ['SENDING', 'EXTERNAL_ACCEPTED'].includes(result.attempt.state)
      || result.attempt.state === 'PREPARED' && !expiredPrepared;
    response.status(result.expiredPrepared ? 409 : active ? 202 : result.replay ? 200 : result.attempt.state === 'SUCCEEDED' ? 201 : 409);
    return expiredPrepared ? { ...safeResult, code: 'INITIAL_ATTEMPT_EXPIRED' } : safeResult;
  }

  @Get('conversations/:id/initial-messages/:attemptId')
  async initialAttempt(@Param('id') id: string, @Param('attemptId') attemptId: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertUuid(attemptId);
    return this.initialMessages.getAttempt({ id: attemptId, conversationId: conversa.id, buId: conversa.buId });
  }

  @Post('conversations/:id/initial-messages/:attemptId/reconcile')
  @HttpCode(200)
  async reconcileInitial(@Param('id') id: string, @Param('attemptId') attemptId: string, @Body() body: unknown, @Req() req: Request, @Res({ passthrough: true }) response: Response) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(attemptId);
    const result = await this.initialMessages.reconcile({ id: attemptId, conversationId: conversa.id, buId: conversa.buId,
      actorId: req.usuario!.id, actorName: req.usuario!.nome,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx) });
    if (['PREPARED', 'SENDING'].includes(result.state)) response.status(202);
    return result;
  }

  @Post('conversations/:id/initial-messages/:attemptId/acknowledge')
  @HttpCode(200)
  async acknowledgeInitial(@Param('id') id: string, @Param('attemptId') attemptId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(attemptId);
    return this.initialMessages.acknowledge({ id: attemptId, conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id,
      confirmed: req.header('X-Confirm-Duplication-Risk') === 'true', validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
      auditInTransaction: (tx) => this.registro.registrar(tx, req.usuario!.mantenedoraId, 'atendimento.initial.risk_acknowledged', ator(req), { buId: conversa.buId, entidadeId: attemptId }) });
  }

  @Post('conversations/:id/dispatch-admissions/:admissionId/reconcile')
  @HttpCode(200)
  async reconcileAdmission(@Param('id') id: string, @Param('admissionId') admissionId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(admissionId);
    return this.initialMessages.reconcileOrdinary({ id: admissionId, conversationId: conversa.id, buId: conversa.buId,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx) });
  }

  @Post('conversations/:id/dispatch-admissions/:admissionId/acknowledge')
  @HttpCode(200)
  async acknowledgeAdmission(@Param('id') id: string, @Param('admissionId') admissionId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(admissionId);
    return this.initialMessages.acknowledgeOrdinary({ id: admissionId, conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id,
      confirmed: req.header('X-Confirm-Duplication-Risk') === 'true', validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
      auditInTransaction: (tx) => this.registro.registrar(tx, req.usuario!.mantenedoraId, 'atendimento.dispatch.risk_acknowledged', ator(req), { buId: conversa.buId, entidadeId: admissionId }) });
  }

  private initialMessageRequest(body: Record<string, unknown>, includeFingerprint: boolean) {
    if (!body || typeof body !== 'object' || Array.isArray(body)) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    const allowed = ['channelId', 'expectedGeneration', 'mensagem', ...(includeFingerprint ? ['previewFingerprint'] : [])];
    if (Object.keys(body).some((key) => !allowed.includes(key)) || typeof body.channelId !== 'string'
      || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(body.channelId)
      || !Number.isSafeInteger(body.expectedGeneration) || (body.expectedGeneration as number) < 1
      || includeFingerprint && (typeof body.previewFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(body.previewFingerprint))) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    const message = body.mensagem;
    if (!message || typeof message !== 'object' || Array.isArray(message)) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    const row = message as Record<string, unknown>;
    const base = { channelId: body.channelId, expectedGeneration: body.expectedGeneration as number };
    const preview = includeFingerprint ? { previewFingerprint: body.previewFingerprint as string } : {};
    if (row.tipo === 'TEXTO') {
      if (Object.keys(row).some((key) => !['tipo', 'texto'].includes(key)) || typeof row.texto !== 'string'
        || !row.texto.trim() || [...row.texto].length > 4096) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
      return { ...base, kind: 'text' as const, text: row.texto, ...preview };
    }
    if (row.tipo !== 'TEMPLATE' || Object.keys(row).some((key) => !['tipo', 'templateId', 'language', 'catalogAfter', 'expectedDefinitionFingerprint', 'parameters'].includes(key))
      || typeof row.templateId !== 'string' || !row.templateId || row.templateId.length > 128
      || typeof row.language !== 'string' || !row.language || row.language.length > 16
      || row.catalogAfter !== undefined && (typeof row.catalogAfter !== 'string' || row.catalogAfter.length < 1 || row.catalogAfter.length > 512)
      || typeof row.expectedDefinitionFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(row.expectedDefinitionFingerprint)
      || !row.parameters || typeof row.parameters !== 'object'
      || Array.isArray(row.parameters) && (row.parameters.length > 20 || row.parameters.some((value) => typeof value !== 'string' || !value || [...value].length > 1024))
      || !Array.isArray(row.parameters) && (Object.keys(row.parameters as object).length > 20 || Object.values(row.parameters as Record<string, unknown>).some((value) => typeof value !== 'string' || !value || [...value].length > 1024))) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    return { ...base, kind: 'approved-template' as const, remoteTemplateId: row.templateId, language: row.language,
      catalogAfter: typeof row.catalogAfter === 'string' ? row.catalogAfter : null,
      expectedDefinitionFingerprint: row.expectedDefinitionFingerprint,
      values: row.parameters as Record<string, string> | string[], ...preview };
  }

  private assertEmptyBody(body: unknown): void {
    if (body !== undefined && (!body || typeof body !== 'object' || Array.isArray(body) || Object.keys(body).length !== 0)) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
  }

  private assertUuid(value: string): void {
    if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(value)) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
  }

  private async currentActorHasGrant(req: Request, buId: string, tx: Prisma.TransactionClient): Promise<boolean> {
    const cookie = this.sessions.extrairDoCabecalho(req.headers.cookie);
    const claimsAtRequest = this.sessions.verificar(cookie);
    if (!claimsAtRequest || claimsAtRequest.uid !== req.usuario!.id) return false;
    let rows: Array<{ id: string; user_status: string; password_changed_at: Date | null;
      user_mantenedora_id: string; bu_status: string; bu_mantenedora_id: string; role: string }>;
    try {
      rows = await tx.$queryRaw<Array<{ id: string; user_status: string; password_changed_at: Date | null;
        user_mantenedora_id: string; bu_status: string; bu_mantenedora_id: string; role: string }>>`
        SELECT u.id, u.status::text AS user_status, u.password_changed_at,
          u.mantenedora_id AS user_mantenedora_id, b.status::text AS bu_status,
          b.mantenedora_id AS bu_mantenedora_id, r.role::text AS role
        FROM app_users u
        JOIN user_bu_roles r ON r.user_id = u.id AND r.bu_id = ${buId}
        JOIN business_units b ON b.id = r.bu_id
        WHERE u.id = ${claimsAtRequest.uid}
        FOR SHARE OF u, r, b NOWAIT`;
    } catch (error) {
      const candidate = error as { code?: unknown; meta?: { code?: unknown; message?: unknown }; cause?: { code?: unknown } };
      const lockCode = candidate.meta?.code ?? candidate.cause?.code ?? candidate.code;
      if (lockCode === '55P03' || candidate.meta?.message === '55P03'
        || typeof candidate.meta?.message === 'string' && candidate.meta.message.includes('55P03')) {
        throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
      }
      throw error;
    }
    const current = rows[0];
    const claimsNow = this.sessions.verificar(cookie);
    return Boolean(current && claimsNow && claimsNow.uid === claimsAtRequest.uid
      && claimsNow.iat === claimsAtRequest.iat && claimsNow.exp === claimsAtRequest.exp
      && claimsNow.exp > Date.now() && current.user_status === 'ATIVO'
      && current.bu_status === 'ATIVO' && current.user_mantenedora_id === current.bu_mantenedora_id
      && (!current.password_changed_at || current.password_changed_at.getTime() <= claimsNow.iat)
      && ['ATENDENTE', 'ADMIN', 'OWNER'].includes(current.role));
  }

  /** New initial-contact routes require the actor's home tenant to match the BU. */
  private async assertActorTenant(req: Request, buId: string): Promise<void> {
    const rows = await this.prisma.$queryRaw<Array<{ user_id: string; user_mantenedora_id: string; bu_mantenedora_id: string; user_status: string; bu_status: string }>>`
      SELECT u.id AS user_id, u.mantenedora_id AS user_mantenedora_id,
        b.mantenedora_id AS bu_mantenedora_id, u.status::text AS user_status,
        b.status::text AS bu_status
      FROM app_users u CROSS JOIN business_units b
      WHERE u.id = ${req.usuario!.id} AND b.id = ${buId}`;
    const row = rows[0];
    if (!row || row.user_status !== 'ATIVO' || row.bu_status !== 'ATIVO'
      || row.user_mantenedora_id !== row.bu_mantenedora_id) throw new NotFoundException();
  }

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
        disponivel: janela.disponivel,
        motivo: janela.motivoIndisponibilidade,
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

    await this.initialMessages.assertOrdinaryDispatchAllowed(conversa.id, conversa.buId);

    const m = await this.conversas.responder(conversa.id, conversa.buId, texto, {
      kind: 'BFF',
      userId: req.usuario!.id,
      name: req.usuario!.nome,
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

### api-app/src/surfaces/public/conversations.controller.ts

SHA256 `bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
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
import { Prisma } from '@prisma/client';
import { ApiKeyService } from '../../domain/integration/api-key.service';
import { RateLimitService } from '../../domain/integration/rate-limit.service';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { PrismaService } from '../../infra/prisma/prisma.service';

const TETO = 500;

function limitePublico(valor: unknown, padrao: number): number {
  if (typeof valor !== 'string' || valor.trim() === '') return padrao;
  const numero = Number(valor);
  if (!Number.isFinite(numero) || numero <= 0) return padrao;
  const inteiro = Math.floor(numero);
  if (inteiro < 1) return padrao;
  return Math.min(inteiro, TETO);
}

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
    const limite = limitePublico(q.limit, 200);

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
      select: { id: true, contact: true, displayName: true, status: true, attendantName: true, lastMessageAt: true, unreadCount: true },
    });

    const pagina = linhas.slice(0, limite);
    type LatestMessage = {
      conversationId: string;
      content: string | null;
      direction: 'IN' | 'OUT' | null;
      channelOrigin: 'OFICIAL' | 'NAO_OFICIAL' | null;
    };
    const mensagensRecentes = pagina.length
      ? await this.prisma.$queryRaw<LatestMessage[]>`
        SELECT requested.conversation_id AS "conversationId",
          latest.content,
          latest.direction::text AS "direction",
          latest.channel_origin::text AS "channelOrigin"
        FROM unnest(ARRAY[${Prisma.join(pagina.map((conversation) => conversation.id))}]::text[]) AS requested(conversation_id)
        LEFT JOIN LATERAL (
          SELECT candidate.content, candidate.direction, candidate.channel_origin
          FROM (
            (
              SELECT message.id, message.content, message.direction, message.channel_origin, message.created_at
              FROM messages AS message
              WHERE message.conversation_id = requested.conversation_id AND message.direction = 'IN'
              ORDER BY message.created_at DESC, message.id DESC
              LIMIT 1
            )
            UNION ALL
            (
              SELECT message.id, message.content, message.direction, message.channel_origin, message.created_at
              FROM messages AS message
              WHERE message.conversation_id = requested.conversation_id AND message.direction = 'OUT'
              ORDER BY message.created_at DESC, message.id DESC
              LIMIT 1
            )
          ) AS candidate
          ORDER BY candidate.created_at DESC, candidate.id DESC
          LIMIT 1
        ) AS latest ON TRUE
      `
      : [];
    const mensagemPorConversa = new Map(mensagensRecentes.map((message) => [message.conversationId, message]));
    const estados = await this.conversas.estadosDasJanelas(pagina.map((c) => ({
      conversationId: c.id, buId, latestMessageOrigin: mensagemPorConversa.get(c.id)?.channelOrigin ?? null,
    })));
    const conversas = pagina.map((c) => {
        const janela = estados.get(c.id);
        const mensagem = mensagemPorConversa.get(c.id);
        return {
          telefone: c.contact,
          nome_whatsapp: c.displayName,
          status: c.status,
          atendendo: c.attendantName,
          ultima_mensagem: mensagem?.content ?? null,
          ultima_direcao: mensagem?.direction ? (mensagem.direction === 'OUT' ? 'enviada' : 'recebida') : null,
          ultima_em: c.lastMessageAt?.toISOString() ?? null,
          nao_lidas: c.unreadCount,
          // Campo generalizado: quem integrou só o Hub recebe `true` e não muda
          // nada; quem integrou a Central continua lendo o que já lia.
          janela_aberta: janela?.windowOpen ?? false,
          janela_expira_em: janela?.expiresAt?.toISOString() ?? null,
          envio_disponivel: janela?.available ?? false,
          motivo_indisponibilidade: janela ? janela.reason : 'CANAL_SELECIONADO_INDISPONIVEL',
        };
      });

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
    const limite = limitePublico(q.limit, 100);

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
      envio_disponivel: janela.disponivel,
      motivo_indisponibilidade: janela.motivoIndisponibilidade,
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
    const m = await this.conversas.responder(conversa.id, buId, texto, { kind: 'PUBLIC', name: atendente });

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

### api-app/src/surfaces/webhooks/meta.controller.ts

SHA256 `261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { Controller, ForbiddenException, Get, HttpCode, Post, Query, Req, ServiceUnavailableException } from '@nestjs/common';
import type { RawBodyRequest } from '@nestjs/common';
import type { Request } from 'express';
import { createHmac, timingSafeEqual } from 'node:crypto';
import { IncomingService, MensagemRecebida } from '../../domain/inbox/incoming.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { qualifiedMetaInboundTimestamp } from '../../domain/inbox/channel-window-policy';

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
      const rawContact = typeof msg.from === 'string' ? msg.from : '';
      // This slice supports WhatsApp phone contacts only. Opaque Meta IDs
      // (including BSUID-style identifiers) are rejected until their mapping
      // contract is implemented; never turn letters into another phone.
      if (!/^\+?[1-9]\d{7,14}$/.test(rawContact)) continue;
      const contact = rawContact.replace(/^\+/, '');
      await this.incoming.registrar({
        buId: identity.buId,
        canal: 'OFICIAL',
        contato: contact,
        ehGrupo: false,
        nomeExibicao: nome,
        direcao: 'IN',
        tipo: tipoDaMensagem(msg.type),
        conteudo: conteudoDaMensagem(msg),
        officialInboundAt: qualifiedMetaInboundTimestamp(msg.timestamp),
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
  timestamp?: string | number;
  type?: string;
  text?: { body?: string };
  button?: { text?: string };
  interactive?: { button_reply?: { title?: string }; list_reply?: { title?: string } };
}
```

### web-app/src/componentes/NovaConversa.tsx

SHA256 `2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd`. Exact byte-identical E64 unchanged support; full source was reviewed in E64/r5; selected current seal confirms unchanged bytes.

Exact E64-unchanged UI support, previously reviewed in the full E64/r5 TQA and bound to the same current bytes. It opens or reuses a conversation only on explicit submit with a required DDI and protects late responses across BU changes. PrimeiraMensagem provides the explicit text or approved-template first-send flow, channel/readiness/window selection, paged template catalog and preview. Template preview fingerprinting sorts canonical semantic values and includes HEADER/BODY/FOOTER components; client code does not decide server grammar or authorize dispatch. It persists a bounded exact idempotency snapshot in sessionStorage before POST, validates restored snapshots, avoids automatic resend on reload/unknown outcome, consults BFF attempt/ordinary-admission state, and exposes reconciliation or deadline-qualified risk acknowledgment. Per-component request latches and generation checks prevent stale previews/submits. Current changed coordinator, resolver, admission service and E2E causal tests remain full; this unchanged support is only summarized because its exact E64 hash matches current.

Complete current case declaration list from the exact unchanged file:


### web-app/src/telas/Inbox.tsx

SHA256 `66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737`. Exact byte-identical E64 unchanged support; full source was reviewed in E64/r5; selected current seal confirms unchanged bytes.

Exact E64-unchanged Inbox UI, previously reviewed in full E64/r5 and bound to the same current source hash. It scopes BU and queue tabs, opens a selected conversation, pages older timeline entries, and guards late list/thread responses with selected BU/conversation generations. Timeline refresh reconciles overlapping recent pages before applying them, preserves newer rows and cursor state, and exposes continuation only for authorized recovery; ordinary read-mark behavior remains explicit in the BFF query. The first-message panel appears for empty conversations or active initial/ordinary attempts, consumes start-options and recovery status, and prevents ordinary reply while the initial outcome is unresolved. Full current BFF controller/resolver/services and changed E2E assertions remain in the packet; the exact E64 unchanged UI is summarized with its sealed hash.

Complete current case declaration list from the exact unchanged file:


### web-app/src/api.ts

SHA256 `7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c`. Exact byte-identical E64 unchanged support; full source was reviewed in E64/r5; selected current seal confirms unchanged bytes.

Exact E64-unchanged BFF client support, previously reviewed in full E64/r5 TQA and hash-bound to current bytes. All calls use credentials; state-changing calls add the required X-Requested-With header. The common parser rejects non-JSON/static-server responses, emits session-expired/product-changed events for known states, and retains structured attempt, provider, receipt, acceptance and recovery fields in ErroDaApi while validating typed IDs/timestamps. This client serializes template catalog/preview/draft/operation/reconciliation/refresh shapes and the ordinary BFF API surface. Current BFF controller, resolver, admission logic and changed tests are full sources; api.spec remains available as an exact test-name/oracle summary.

Complete current case declaration list from the exact unchanged file:


### api-app/src/surfaces/bff/bff.module.ts

SHA256 `8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { MiddlewareConsumer, Module, NestModule, RequestMethod } from '@nestjs/common';
import { AccessService } from '../../domain/access/access.service';
import { IdentityService } from '../../domain/identity/identity.service';
import { LoginAttemptService } from '../../domain/identity/login-attempt.service';
import { PasswordService } from '../../domain/identity/password.service';
import { SessionService } from '../../infra/session/session.service';
import { ChannelsService } from '../../domain/channels/channels.service';
import { NumberRegistrationService } from '../../domain/channels/number-registration.service';
import { NumberRegistrationsController } from './number-registrations.controller';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { ConversationStartService } from '../../domain/inbox/conversation-start.service';
import { InitialMessageService } from '../../domain/inbox/initial-message.service';
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
import { ChannelTransportModule } from '../../integrations/channels/channel-transport.module';
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
import { TemplateManagementModule } from '../../integrations/message-templates/template-management.module';
import { TemplateDraftService } from '../../domain/message-templates/template-draft.service';
import { TemplateSubmissionService } from '../../domain/message-templates/template-submission.service';
import { PrismaTemplateTransactionBoundary, TEMPLATE_TRANSACTION_BOUNDARY } from '../../domain/message-templates/template-transaction-boundary';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { MessageTemplatesController } from './message-templates.controller';
import { TEMPLATE_OBSERVATION_CLOCK, TemplateObservationService } from '../../domain/message-templates/template-observation.service';

/**
 * Superfície BFF (ADR-0006): o que as telas consomem, autenticado por sessão.
 *
 * O middleware é montado no PREFIXO. É isso que faz o guard ser da superfície e
 * não da rota, e é o que impede o defeito que já mordeu os dois sistemas: no
 * Hub, um router.use(requireAuth) sem path interceptou o webhook público.
 */
@Module({
  imports: [ChannelTransportModule, TemplateManagementModule],
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
    MessageTemplatesController,
  ],
  providers: [
    SessionService,
    IdentityService,
    PasswordService,
    LoginAttemptService,
    AccessService,
    TemplateDraftService,
    TemplateSubmissionService,
    TemplateObservationService,
    { provide: TEMPLATE_OBSERVATION_CLOCK, useValue: { now: () => new Date() } },
    { provide: TEMPLATE_TRANSACTION_BOUNDARY, useFactory: (prisma: PrismaService) => new PrismaTemplateTransactionBoundary(prisma), inject: [PrismaService] },
    ChannelsService,
    NumberRegistrationService,
    ConversationsService,
    ConversationStartService,
    InitialMessageService,
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

### api-app/src/integrations/message-templates/template-management.module.ts

SHA256 `aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { Module } from '@nestjs/common';
import { TEMPLATE_MANAGEMENT_RESOLVER } from '../../domain/message-templates/template-management.ports';
import { ChannelTransportModule } from '../channels/channel-transport.module';
import { ScopedTemplateManagementResolver } from './template-management.resolver';

@Module({
  imports: [ChannelTransportModule],
  providers: [
    ScopedTemplateManagementResolver,
    { provide: TEMPLATE_MANAGEMENT_RESOLVER, useExisting: ScopedTemplateManagementResolver },
  ],
  exports: [TEMPLATE_MANAGEMENT_RESOLVER],
})
export class TemplateManagementModule {}
```

### api-app/src/domain/channels/transport/channel-dependencies.spec.ts

SHA256 `f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3`. selected-candidate full source; bound to selected 259-file source seal.

```typescript
import { readdirSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

const inboxDirectory = resolve(dirname(fileURLToPath(import.meta.url)), '../../inbox');
const consumerPaths = [
  resolve(inboxDirectory, 'conversations.service.ts'),
  resolve(inboxDirectory, 'incoming.service.ts'),
  ...readdirSync(inboxDirectory)
    .filter((name) => /^outbound.*\.ts$/.test(name))
    .map((name) => resolve(inboxDirectory, name)),
];

function providerDispatchViolations(source: string): string[] {
  const rules: Array<[string, RegExp]> = [
    ['provider client or adapter import', /from\s+['"][^'"]*integrations\/(?:meta|evolution|channels)\/[^'"]+['"]/],
    ['credential resolver import', /from\s+['"][^'"]*channel-credential-resolver['"]/],
    ['provider injection token', /\b(?:META_CLIENT|EVOLUTION_CLIENT)\b/],
    ['provider text dispatch', /\.enviarTexto\s*\(/],
    ['provider-specific branch', /\.(?:provider|channelOrigin|type)\s*(?:===|!==|==|!=)\s*['"](?:OFICIAL|NAO_OFICIAL)['"]|switch\s*\(\s*[^)]*\.(?:provider|channelOrigin|type)\s*\)/],
  ];
  return rules.filter(([, expression]) => expression.test(source)).map(([name]) => name);
}

describe('common outbound dependency boundary', () => {
  it('keeps provider clients and dispatch inside channel adapters', () => {
    const violations = consumerPaths.flatMap((path) => {
      const source = readFileSync(path, 'utf8');
      return providerDispatchViolations(source).map((rule) => `${path}: ${rule}`);
    });
    expect(violations).toEqual([]);
  });

  it.each([
    "import { MetaClient } from '../../integrations/meta/meta.client';",
    "import { MetaChannelFactory } from '../../integrations/channels/meta-channel';",
    "import { ChannelCredentialResolver } from '../channels/channel-credential-resolver';",
    "if (context.channelOrigin === 'OFICIAL') return sendMeta();",
    "switch (binding.type) { case 'NAO_OFICIAL': return sendEvolution(); }",
    "const send = context.channelOrigin === 'OFICIAL' ? sendMeta() : sendEvolution();",
    "switch (context.provider) { case 'OFICIAL': return sendMeta(); }",
  ])('detects synthetic provider coupling outside the adapter allowlist: %s', (source) => {
    expect(providerDispatchViolations(source).length).toBeGreaterThan(0);
  });
});
```

### capability-owner-evidence-e44-v1.1.json

```json
{"kind":"Exact known manifest capability/command evidence; not canonical discovery-tool GO","recorded_at_utc":"2026-10-22T22:07:59.025596+00:00","source_seal":"browser-source-seal-e44-v1.1.json","owners":[{"manifest":"api-app/package.json","manifest_sha256":"df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d","lockfile":"api-app/package-lock.json","lockfile_sha256":"d1e45274c4b10d134469d7ec63e88777ec26b917d48197a03a4b97cefda047c7","capability_dependencies":{"nestjs":{"@nestjs/core":"^11.0.0"},"prisma":{"@prisma/client":"^6.0.0","prisma":"^6.0.0"}},"required_scripts":{"build":"nest build","lint":"eslint \"{src,test}/**/*.ts\"","test":"vitest run --config vitest.config.ts","test:e2e":"vitest run --config vitest.config.e2e.ts --no-file-parallelism --maxWorkers=1","prisma:generate":"prisma generate","prisma:migrate":"prisma migrate deploy"},"execution_owner":"bash scripts/test-channels-local.sh all","observed_last_complete_phases":"E43 build/lint/unit/realPG andWebunit passed;browserRED3; no broad parity claim."},{"manifest":"web-app/package.json","manifest_sha256":"fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de","lockfile":"web-app/package-lock.json","lockfile_sha256":"546aec97be8273cf195a16b75c0127474ea3a5042668f8d4c93aab96c1619c8f","capability_dependencies":{"react":{"react":"^18.3.1","react-dom":"^18.3.1"},"vite":{"vite":"^5.4.11"},"browser":{"@playwright/test":"^1.62.1"}},"required_scripts":{"build":"tsc -b && vite build","test":"vitest run","test:tela":"npm run build && playwright test"},"execution_owner":"bash scripts/test-channels-local.sh all","observed_last_complete_phases":"E43 build/lint/unit/realPG andWebunit passed;browserRED3; no broad parity claim."}],"canonical_helper_not_executed":{"path":"delphi-ai/tools/node_capability_surface_audit.py","reason":"Even --manifest first calls load_manifests(root), whose manifest_paths os.walk recursively enumerates repository directories. It has no private-directory prune for .local-files; this conflicts with explicit approved no-private-traversal boundary.","source_references":["manifest_paths:155-169","audit:229-246"],"handling":"Read only2explicit known public package.json/locks and attest against full source seal, owning dependencies/scripts and actual canonical runner. No modified/copied repository, monkeypatch, filtered faux GO, user waiver or silent private discovery."},"scope_limit":"This establishes only these known project owners and current declared commands; it does not inventory unknown packages or certify the whole actual filesystem. Fresh independent TQA still required."}
```

### test-causality-chronology-r1-v1.1.json

```json
{"kind":"Honest test causality and regression chronology","version":"1.1","recorded_at_utc":"2026-10-23T02:09:44.526169+00:00","finding":"TQA-ST04-04","scope":"ST-CON-04 whole approved journey, including inherited and new verification","adjudication":"Test-first coverage is partial. Final-state regression, post-hoc controlled reversion, module loading and causal assertion failures are distinct evidence classes. No retroactive reversion or repeated run solely to fabricate chronology.","rows":[{"checkpoint":"E03","source_receipt":"executor-red-e03-v1.1.json","classification":"module-loading only","observed_fact":"New modules absent; 3 suites fail to load, 284 existing tests pass and zero behavior assertions fail.","claim_limit":"No business-level test-first proof."},{"checkpoint":"E04","source_receipt":"TODO#E04","classification":"mixed chronology","observed_fact":"After compile-only repair, RED3 reaches two renderer assertions before their fixes; later RED4 temporarily reverts a preliminary implementation and reaches six failures.","claim_limit":"RED3 causal only for reached renderer assertions; RED4 controlled post-hoc verification, never original test-first."},{"checkpoint":"E11","source_receipt":"transport-valid-red-e11-v1.1.json","classification":"causal assertion RED","observed_fact":"Corrected transport fixture reaches three failures before transport implementation: unsupported Evolution dispatch and missing Meta protocol delegation.","claim_limit":"Earlier invalid protocol fixture is not product RED; later pin/fence assertions not reached."},{"checkpoint":"E15","source_receipt":"dispatch-admission-red-e15-v1.1.json","classification":"module-loading only","observed_fact":"Absent new admission implementation prevents suite loading; 311 existing unit tests pass.","claim_limit":"Admission behavior and PostgreSQL assertions not reached."},{"checkpoint":"E21/E22","source_receipt":"outbound-causal-red-e21-v1.1.json; outbound-valid-red-e22-v1.1.json","classification":"causal assertion RED","observed_fact":"Before ordinary sender admission wiring, split tests reach missing reserve/claim, prepared release, uncertain settlement and refusal settlement assertions.","claim_limit":"Unit boundary proof only; real PG/concurrency is later regression verification."},{"checkpoint":"E25","source_receipt":"initial-coordinator-red-e25-v1.1.json","classification":"module-loading plus unrelated assertion failures","observed_fact":"Coordinator import is absent-module failure; two actual assertions fail in admission/protocol suites.","claim_limit":"No request/idempotency/coordinator business assertion RED; other failures require their own causal classification."},{"checkpoint":"E35","source_receipt":"browser-result-e35-v1.1.json","classification":"causal browser assertion RED","observed_fact":"Actual first-message field is missing before new initial-send UI implementation. Real BFF open/empty PG/zero-provider assertions passed first.","claim_limit":"Existing manual-open UI/backend predates test; later ordinary-composer assertion not reached."},{"checkpoint":"E41","source_receipt":"all-result-e41-v1.1.json","classification":"mixed product and test-support failures","observed_fact":"Actual UI reuse state loss and missing AMBIGUOUS state projection fail before their corrections.","claim_limit":"Fixture reassignment/audit omission/cumulative counters/mapping expectations are not product behavior REDs; shell exit metadata unavailable, no invented exit code."},{"checkpoint":"E44/E45","source_receipt":"storage-read-recovery-evidence-loop-v1.1.json","classification":"causal browser regression RED then full GREEN","observed_fact":"Actual accepted-send/lost-response/storage-read failure deletes original replay snapshot; failure precedes fix preserving key/body and blocking unsafe actions; full E45 all passes.","claim_limit":"Only named storage recovery behavior has this causal history; whole suite does not inherit it."},{"checkpoint":"E46/E47","source_receipt":"browser-result-e46-v1.1.json; browser-result-e47-v1.1.json","classification":"post-implementation recovery coverage","observed_fact":"New ordinary recovery case first fails an invalid fake-effects counter; narrow correction followed by full86browser pass.","claim_limit":"Counter failure is not production RED. Added ordinary UI recovery coverage is post-implementation regression proof."},{"checkpoint":"E48/E49","source_receipt":"api-result-e48-v1.1.json; api-result-e49-v1.1.json","classification":"test-support failures before target regressions","observed_fact":"E48 lint fails on spy assertion capture in finally; E49 lint/build pass, 362unit tests pass and one negative-control detector test fails because axios.post is not recognized. PostgreSQL never reached.","claim_limit":"Neither failure proves a production defect. PREPARED payload and r1 behavior assertion RED still pending. Product unchanged; detector and contract tests are being corrected before next run."},{"checkpoint":"E50","source_receipt":"api-result-e50-v1.1.json; api-source-recheck-e50-v1.1.json; prepared-recovery-live-payload-e50-v1.1.json","classification":"causal real PostgreSQL/BFF assertion RED","observed_fact":"Before product fixes, four integration tests fail on PREPARED action/active-slot safe metadata and wrong ordinary code, full-history COUNT, omitted realtime creation-winner event and ordinary201 after actual settlement rollback. 363unit and435otherPG tests pass.","claim_limit":"Actual owned synthetic state and payload proof, no real provider/preserved runtime claim. Local PREPARED live202 and expired REJECTED release steps passed; missing browser action proof still pending."},{"checkpoint":"E51","source_receipt":"web-result-e51-v1.1.json; web-source-recheck-e51-v1.1.json","classification":"causal Unicode snapshot assertion RED","observed_fact":"Valid1024astral POSITIONAL parameter is rejected before product fix; prior text4096/4097 code-point checks pass. Build and53otherWebunit tests pass.","claim_limit":"Later NAMED branch and positional1025 assertion were not reached in combined test; require final complete passing unit and actual input/browser proof."},{"checkpoint":"E52/E53/E54","source_receipt":"candidate-source-preflight-e52-v1.1.json; all-result-e53-v1.1.json; all-result-e54-v1.1.json; all-source-recheck-e54-v1.1.json","classification":"faithful fixture/source preflight and post-implementation test baseline repair","observed_fact":"E52 did not run: fixture corrected to real owner reservation with90s lease and full canonical data, early UIACK tests actual BFF409 rather than adding an unapproved timer feature. E53 product regressions pass (364unit/438PG); new late-old test incorrectly compares to pre-ACK null timestamp, while actual late state is SUCCEEDED and release remains nonnull. E54 changes only that test to exact post-ACK timestamp and reruns full ALL.","claim_limit":"E53 stale expectation is not product RED. E54 actually completed exit0:364unit/439PG/54Web/88browser, full259source postseal and93manifest freshness checks. Fresh independent reviews subsequently found additional gaps; E54 GREEN did not close delivery."},{"checkpoint":"E55/E56","source_receipt":"candidate-source-preflight-e55-v1.1.json; api-result-e56-v1.1.json","classification":"E55 no-run fixture preflight; E56 four causal ordinary unit failures before product fix","observed_fact":"E56 actual unit364pass/4fail; persistence errors replace captured BLOCKED/REJECTED/UNKNOWN/ACK_WITHOUT_ID projection. Later per-case counters and PG were not reached.","claim_limit":"Do not label E55 as runtime RED or E56 as real-PG causal before-fix proof."},{"checkpoint":"E57","source_receipt":"api-result-e57-v1.1.json; api-source-recheck-e57-v1.1.json","classification":"ordinary fix verified; new observation setup failed before intended consumer assertions","observed_fact":"368unit and443PG tests pass; one PG setup expected200→409 at originalPreview line476. Four independently seeded protocol groups pass.","claim_limit":"Unavailable observation and BU-switch defects still source-confirmed, not runtime-reproduced. No Web/browser run."},{"checkpoint":"E58","source_receipt":"api-result-e58-v1.1.json; api-source-recheck-e58-v1.1.json","classification":"new observation fixture draft-validation failure; not product RED","observed_fact":"368unit/443PG pass; valid original preview now passes, draft creation returns500 from unsupported en_US authoring language before unavailable producer transition.","claim_limit":"No availability consumer assertion reached. pt_BR-only and body-edge rules are preserved authoring constraints, not authority to broaden ST05."},{"checkpoint":"E59","source_receipt":"api-result-e59-v1.1.json; api-source-recheck-e59-v1.1.json","classification":"causal real-PG/BFF availability-consumer assertion and side-effect RED before consumer fix","observed_fact":"Valid actual ST05 create/catalog/individual-failure transition leaves page fresh and APPROVED item unavailable. Initial preview200 and submit201 SUCCEEDED produce1messagePOST/intent/OUT where409 pre-admission and zero were required. All8soft failure assertions reached; other443PG/368unit pass.","claim_limit":"Disposable owned fake provider, not real Meta delivery. Earlier E57/E58 setup failures remain setup-only, never retroactively causal. BU browser still not run."},{"checkpoint":"E60","source_receipt":"browser-result-e60-v1.1.json; browser-source-recheck-e60-v1.1.json","classification":"implementation type-boundary compile failure before browser","observed_fact":"API build TS2339 after adding availability guard to a TemplateSummary-cast item. Provider summary intentionally lacks observation metadata; current source did not compile.","claim_limit":"No Playwright/globalSetup/freshness or BU causal RED; no availability after-fix result. Narrow consumer correction preserves inferred observation before Summary cast."},{"checkpoint":"E61","source_receipt":"browser-result-e61-v1.1.json; browser-source-recheck-e61-v1.1.json","classification":"implementation projection assertion compile failure, not UI RED","observed_fact":"TS2352 rejects root-proposed direct item cast because JsonValue components and provider component union differ. Build fails before browser.","claim_limit":"No cases/freshness/consumer GREEN. E62 uses the existing array boundary plus local boolean metadata view, preserving producer/provider types and no unknown/any widening."},{"checkpoint":"E62","source_receipt":"browser-result-e62-v1.1.json; browser-failure-triage-e62-v1.1.json; browser-source-recheck-e62-v1.1.json","classification":"causal BU UI assertion RED plus separate test-consumer synchronization failure","observed_fact":"87/89pass,2fail. CurrentBU dialog remains visible but Fechar disabled after held old response, actual5s assertion before UI fix. Existing replay test observes storage too early while DOM Enviando; samekey/body/postCount2 passed but later audit/provider bounds not reached.","claim_limit":"No retroactive test-first claim for timing repair; availability after-fix API-PG remains pending. Source full259 and93manifest/bundle match."},{"checkpoint":"E63/E64","source_receipt":"all-result-e63-v1.1.json; all-source-recheck-e63-v1.1.json; all-source-seal-e64-v1.1.json","classification":"incomplete old unit observation fixture, faithful one-field correction then pending consolidatedALL","observed_fact":"E63 actual367unitpass/1fail because unsupported-component item omitted available metadata. E64 adds available:true only, preserving expected unsupported rejection; real producer always provides that field.","claim_limit":"E63 PG/Web/browser not reached. E64 is currently running; no full/current GREEN inferred."}],"broader_coverage":"Most PostgreSQL fault/commit/protocol/boundary/rate/concurrency cases were added alongside or after their production implementation. They are meaningful final-state regression evidence, not universally pre-implementation causal RED.","review_correction":"The broad r1 reviewer shorthand naming E03/E25 as selected causal RED is qualified here by exact receipts: their new coordinator/admission behavior failed to load and did not reach business assertions. Original raw review results remain immutable.","method_assessment":"No generic rule/analyzer edit is warranted solely by chronology. Preserve evidence classification and add actual causal regressions for newly found bugs before fixing those bugs.","resolution":"Explicit chronology correction complete. Current newly found product regressions now have actual causal E50/E51 assertions before their fixes; original alongside/post-implementation chronology remains unchanged. Independent reassessment pending."}
```

### implementation-r1-resolution-v1.1.json

```json
{"kind":"Actual integrated r1 finding resolutions for fresh independent r2 challenge","recorded_at_utc":"2026-10-23T00:47:04.414607+00:00","source_seal":"all-source-seal-e54-v1.1.json","rows":[{"finding_id":"F-511FF1D6","source_finding_id":"ARCH-ST04-R1-06","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Current coordinator dependency harness added with actual-source import/HTTP protection and synthetic forbidden controls.","source":{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-8E89FC19","source_finding_id":"ARCH-ST04-R1-02","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Ordinary local settlement must be positive; false/throw returns known accepted/local incomplete preserving Message and ACK; actual PG rollback regression passed.","source":{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-ED2FCC37","source_finding_id":"ARCH-ST04-R1-03","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Only confirmed local creationWinner publishes best-effort realtime after commit; replay/echo/uncertain readback do not duplicate.","source":{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-C8AF5811","source_finding_id":"ARCH-ST04-R1-05","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Ordinary BFF uses bounded findFirst select id rather than whole-history COUNT; query-event regression passed.","source":{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-3E65B77F","source_finding_id":"ARCH-ST04-R1-01","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"PREPARED safe action RECONCILE; actual E50 before payload RED and full E54 PG/UI live/expired zero-network proof.","source":{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-F7C06078","source_finding_id":"ARCH-ST04-R1-04","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Active initial conflict includes scoped safe attemptId/state and BLOCKED; empty remains REQUIRED; ordinary admissions use bounded scoped10+truncation.","source":{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-B25EB3CF","source_finding_id":"TQA-ST04-02","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"E47 actually terminated86pass with cleanup/postseal; current corrected E54 now actually terminated88pass with full259/93 source/bundle binding.","source":{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-8D9F2A1C","source_finding_id":"TQA-ST04-01","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Input clamps and named/positional snapshot validation use code points; E51 causal RED then current unit and Unicode browser proof; separate JSON bound preserved.","source":{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-9EFF5F01","source_finding_id":"TQA-ST04-04","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Chronology corrected explicitly: absent-module/fixture/detector failures and post-hoc reversion never business assertion test-first; mixed sequencing remains disclosed, not retroactively fixed.","source":{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."},{"finding_id":"F-B360C531","source_finding_id":"TQA-ST04-03","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Actual EALB early UI409 unchanged slot, disposable expiry ACK200, successor and late-old local reconciliation isolating owner/provider verified in full E54.","source":{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"],"limits":"Fresh r2 challenge still required; no delivery/real-provider claim."}],"chronology":"test-causality-chronology-r1-v1.1.json","remaining":"Runtime/operator/module/guard/final review gates remain; no waiver or unsupported completion."}
```

### implementation-r2-r3-resolution-v1.1.json

```json
{"kind":"Current integrated r1/r2/r3 finding resolutions for fresh r4 challenge; no delivery clearance","recorded_at_utc":"2026-10-23T02:40:40.174649+00:00","source_seal":"all-source-seal-e64-v1.1.json","source_fingerprint":"70c038f24f15cf4a26a65c545bc9e3fba336a67a9cde7bfcb8cdec9910949340","rows":[{"finding_id":"F-511FF1D6","source_finding_id":"ARCH-ST04-R1-06","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Current coordinator dependency harness added with actual-source import/HTTP protection and synthetic forbidden controls.","source":{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-8E89FC19","source_finding_id":"ARCH-ST04-R1-02","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Ordinary local settlement must be positive; false/throw returns known accepted/local incomplete preserving Message and ACK; actual PG rollback regression passed.","source":{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"1056f18f9767dc5d425a3504c70252f92c91dbf07dc1bbe558ee6a03d9032867"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-ED2FCC37","source_finding_id":"ARCH-ST04-R1-03","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Only confirmed local creationWinner publishes best-effort realtime after commit; replay/echo/uncertain readback do not duplicate.","source":{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"1056f18f9767dc5d425a3504c70252f92c91dbf07dc1bbe558ee6a03d9032867"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"0fe7e51f992c7582493db1f5611685e6fb6928394c6e61f3b2e2a9f6aab7bdb1"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-C8AF5811","source_finding_id":"ARCH-ST04-R1-05","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Ordinary BFF uses bounded findFirst select id rather than whole-history COUNT; query-event regression passed.","source":{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-3E65B77F","source_finding_id":"ARCH-ST04-R1-01","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"PREPARED safe action RECONCILE; actual E50 before payload RED and full E54 PG/UI live/expired zero-network proof.","source":{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"ba61c0777b72ad0e8ba7d42a7d444d152a3cdb00f6327223bf7d3c0e8ab4b8e6"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-F7C06078","source_finding_id":"ARCH-ST04-R1-04","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Active initial conflict includes scoped safe attemptId/state and BLOCKED; empty remains REQUIRED; ordinary admissions use bounded scoped10+truncation.","source":{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"bebcc9813d5b5b03121c1da1844e85f11251aa261e2bf7665e1b894de0b4d7fc"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-B25EB3CF","source_finding_id":"TQA-ST04-02","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Current corrected E64 actually terminated89browserpass with owned cleanup/full259source postseal/93manifest and exact served-dist binding; earlier E47/E54 terminal chronology remains historical.","source":{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-8D9F2A1C","source_finding_id":"TQA-ST04-01","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Input clamps and named/positional snapshot validation use code points; E51 causal RED then current unit and Unicode browser proof; separate JSON bound preserved.","source":{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-9EFF5F01","source_finding_id":"TQA-ST04-04","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Chronology corrected explicitly: absent-module/fixture/detector failures and post-hoc reversion never business assertion test-first; mixed sequencing remains disclosed, not retroactively fixed.","source":{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"5721d1a154f493d239fe1ae942b740ff24ea9eac1dd4a3eba9e69a3a4b3b7f35"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"a549c2dc260906480d3a8c513349c36a15d9cd46df1a7493b3d784592f838b74"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-B360C531","source_finding_id":"TQA-ST04-03","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Actual EALB early UI409 unchanged slot, disposable expiry ACK200, successor and late-old local reconciliation isolating owner/provider verified in full E54.","source":{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"},"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json"],"limits":"Current exact source and complete regression revalidated; independent fresh r4 challenge still required. Original chronology/source references stay historical, no actual provider/delivery proof.","historical_source_and_proof":{"source":{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"16f1027b323f55805b4b26a2addbaf849001acb6ced8e7dda9044b6a6a039649"},"proof":["all-result-e54-v1.1.json","all-source-recheck-e54-v1.1.json"]}},{"finding_id":"F-2A26268E","source_finding_id":"ARCH-ST04-R2-01","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Captured ordinary BLOCKED/REJECTED/UNKNOWN typed outcome and ACK_WITHOUT_ID diagnostic survive bounded local settlement/release errors; no slot release/retry fabricated. Existing positive ACCEPTED settlement proof retained.","sources":[{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"1056f18f9767dc5d425a3504c70252f92c91dbf07dc1bbe558ee6a03d9032867"},{"path":"api-app/src/domain/inbox/outbound.service.spec.ts","sha256":"748be057ff4b3cfe1215b87108d7708ca02ed97d7a7d129d9cada5fc1aef8d81"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"8493ee59713c1e1cf445c8c1c325d918ac1193f460b4187f15a27b62d481de3f"}],"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json"],"actual_causal_or_quality_evidence":"E56 actual four unit causal failures precede product fix; E57/E58/E59 and E64 unit+real PostgreSQL diagnostic/rollback assertions pass.","limits":"Current source implementation/evidence integrated, fresh complete independent r4 challenge pending. No runtime/operator/module/guard/final-delivery clearance.","historical_causal_receipt":"api-result-e56-v1.1.json"},{"finding_id":"F-9D491F93","source_finding_id":"ARCH-ST04-R2-02","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"BU keyed dialog mount reuses existing unmount/generation guards; held old response cannot control current BU or keep its controls busy.","sources":[{"path":"web-app/src/telas/Inbox.tsx","sha256":"66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"},{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"}],"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","browser-freshness-collection-e64-v1.1.json","browser-failure-triage-e62-v1.1.json"],"actual_causal_or_quality_evidence":"E62 actual browser assertion failed with Fechar disabled after BU switch; E64 case4 passes after keyed mount.","limits":"Current source implementation/evidence integrated, fresh complete independent r4 challenge pending. No runtime/operator/module/guard/final-delivery clearance.","historical_causal_receipt":"browser-result-e62-v1.1.json"},{"finding_id":"F-91766E02","source_finding_id":"ARCH-ST04-R2-03","review_kind":"architecture_adherence","resolution":"Integrated","resolution_evidence":"Existing JSON-to-renderer boundary preserves typed item available metadata; preview and second new-submit preparation require page and selected item available plus APPROVED. Authoring supported/eligible flags stay independent; available POSITIONAL remains valid. Idempotent replay still precedes new eligibility.","sources":[{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"5721d1a154f493d239fe1ae942b740ff24ea9eac1dd4a3eba9e69a3a4b3b7f35"}],"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json"],"actual_causal_or_quality_evidence":"E59 actual producer/BFF failure reached all8soft assertions and observed unintended1providerPOST/intent/OUT. E64 now rejects both local consumers before effects. Protected ST05 producer/ports/harness unchanged.","limits":"Current source implementation/evidence integrated, fresh complete independent r4 challenge pending. No runtime/operator/module/guard/final-delivery clearance.","historical_causal_receipt":"api-result-e59-v1.1.json"},{"finding_id":"F-D7518029","source_finding_id":"TQA-R3-02","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Split compound template scenario into four independently seeded groups: claim/preflight fences, owner CAS race, protocol shapes, and seven isolated eligibility negatives. Preserve original counters, deterministic barriers, all positive/negative assertions and cleanup.","sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"5721d1a154f493d239fe1ae942b740ff24ea9eac1dd4a3eba9e69a3a4b3b7f35"}],"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json"],"actual_causal_or_quality_evidence":"E64 full real PostgreSQL444passes; exact new test groups are in current full source for fresh TQA challenge, not a historical test-first claim.","limits":"Current source implementation/evidence integrated, fresh complete independent r4 challenge pending. No runtime/operator/module/guard/final-delivery clearance."},{"finding_id":"F-EB21E40D","source_finding_id":"TQA-R3-01","review_kind":"test_quality_audit","resolution":"Integrated","resolution_evidence":"Canonical full four-root raw scan remains high/exit2. Every255current match has exact path/line/current sourceSHA, matched source, test anchor, individual classification/rationale/concrete support. Rechecked current support including unchanged no-key predicate now polled for body completion. No category blanket waiver, analyzer edit, narrowed scope or raw PASS.","sources":[],"proof":["all-result-e64-v1.1.json","all-source-recheck-e64-v1.1.json","test-quality-public-roots-e64-v1.1.json","test-quality-signal-inventory-e64-v1.1.json","test-quality-signal-dispositions-e64-v1.1.json"],"actual_causal_or_quality_evidence":"Full current inventory and all255dispositions are supplied for independent challenge; root review alone does not close test-quality gate.","limits":"Current source implementation/evidence integrated, fresh complete independent r4 challenge pending. No runtime/operator/module/guard/final-delivery clearance."}],"chronology":"test-causality-chronology-r1-v1.1.json","bounded_test_support_corrections":["E62 actual lost-response browser failure was a one-shot read before response body/snapshot cleanup; identical predicate uses default-bounded expect.poll, same key/body/request count/provider1effect/Message1 retained, E64 case9 passes.","E63 unsupported-component unit expected unavailable due missing actual producer metadata. Only available:true added to fixture; unsupported shape/error assertion unchanged, E64 API368passes."],"inherited_observation":["E58 fixture used unsupported authoring language en_US and received500 before submission. ST05 sealed authoring behavior is outside this current approved story; this is observed follow-up candidate, not a waiver or authority to mutate it. Correct current pt_BR/punctuated BODY fixture reaches actual consumer assertion."],"remaining":["Fresh substantive independent architecture/security/TQA/cutover review, actual preserved runtime and operator own-channel initial sends/replies, canonical module consolidation, full canonical diff guard exception and final delivery guards/review."]}
```

### additive-migration-assessment-e45-v1.1.json

```json
{"kind":"Bounded additive migration assessment, disposable proof only","recorded_at_utc":"2026-10-22T23:07:06.928239+00:00","source_seal":"all-source-seal-e45-v1.1.json","migrations":[{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","sha256":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437","bounded_transaction":true},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","sha256":"78963dce996b2cec9e0990812a5091725238f9995e892c196e614ce9b2a6464f","bounded_transaction":true},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","sha256":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544","bounded_transaction":true}],"source_findings":["Nullable official_inbound_at is added without fabricated backfill/default timestamp; selected-resource direction/origin timestamp index added.","New finite dispatch admission and initial intent tables/enums; existing conversation FK references preserved with declared cascade only on future explicit parent deletion. No data deletion is executed by migration.","SQL-only unreleased-slot partial unique, JSONB account-rate expression and COALESCE inbox-order indexes are explicit; ordinary admission owner nonce and initial BU+actor+key unique indexes remain represented.","Nonconcurrent CREATE INDEX may take table write locks;5s lock wait/60s statement bound means local migration can fail. Never treat additive as lock-free, auto-retry, reset or skip unexpected pending drift."],"actual_disposable_evidence":{"receipt":"all-result-e45-v1.1.json","freshness":"browser-freshness-collection-e45-v1.1.json","completed_migrations":28,"schema_assertions":"dispatch-admission.e2e-spec.ts:87 asserts new columns/native precision/enums and intentional SQL-only indexes; actual PG tests include admission uniqueness and transaction barriers.","explain_receipt":"pcv-eps-e45-v1.1.json"},"scope_limits":["No whole-database schema equivalence claim from bounded new-column/index assertions.","No migration, preflight connection, dump or data read on the preserved user test runtime has been performed.","Apply only under the later approved local plan after exact local database identity/status/source preflight; stop on mismatch/lock failure.","No destructive rollback. An older API lacks the new interlock; do not blindly revert after possible send or unresolved intent."],"independent_status":"Candidate assessment submitted for fresh architecture/TQA/cutover challenge, not self-certified final delivery."}
```

### local-activation-proof-plan-proposal-v1.1.json

```json
{"kind":"Reviewable future local activation/proof plan; NOT approved or executed","governing_todo":"foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md","preconditions":["Frozen complete candidate passes canonical all with identical pre/post public source manifest.","Required independent implementation/migration/security/architecture assessments resolve material findings.","Full diff guard inspection exception is separately explicit; no inferred private inspection.","Reconfirm preserved local project identity from exact approved public topology and safe selected Docker metadata; stop on unexpected topology/resources."],"proposed_target":{"project":"leadshug_channels_local","profile":"channels-local","public_composition":["docker-compose.yml","docker-compose.channels.yml"],"operator_origin":"existing loopback gateway on127.0.0.1:8083; current availability unknown","services_to_replace":["api","web"],"services_to_preserve":["postgres","gateway","evolution-postgres","evolution-redis","evolution"],"data":"All existing volumes, BUs, channels, credentials and conversation history preserved. No reset/drop/truncate/deletion."},"build_provenance":["Use explicit positive public build-input inventory from principal checkout; no root-wide context capture or private traversal.","No copied writable checkout/worktree; disposable build context/archive is a generated build artifact only.","Record approved public input hashes, image IDs/digests, API compiled hashes and Web built/served bundle equality.","Do not claim an unbuilt source fingerprint as the served image. Fresh attestation must precede interpreting operator/browser proof.","Public Dockerfiles were inspected for this proposal: API explicitly COPYs package/lock,prisma,src,tsconfigs,nest-cli and docker/entrypoint; Web uses COPY . . in its builder, so its generated build context must contain only individually admitted public inputs (never the whole checkout). These Dockerfiles are not mutated. Actual Alpine image health is required; Debian disposable-suite results alone do not establish native runtime compatibility."],"proposed_private_exception":{"purpose":"Mechanical Compose consumption of the existing private test configuration to preserve current runtime settings.","allowed":"Only existing .env.testing as an opaque input to existing Compose; no printing/copying/dumping values. Local migration process may use its existing DB connection in-memory.","forbidden":"No .local-files access; no process argument/env/log dumps; no manual token/provider probe; no credential/session password read by agent; no private-file edits unless separately concrete and approved.","unknown":"HTTPS current hostname/process state unknown; no existing tunnel adopted/killed by assumption. If origin change requires private-file mutation, prepare exact bounded change first."},"migration":["Only three approved additive initial_message migrations from sealed source after disposable deploy/status/schema proof.","Preflight exact local TEST database/service; record migration names/checksums/status and no unexpected pending drift.","SET lock_timeout5s and statement_timeout60s as in approved SQL; stop on lock/migration failure; no blind retry/reset.","No destructive down migration; rollback assessment is application compatibility plus preserved data, not dropping new tables/columns.","Rollback assessment: an older API does not enforce the new initial-intent interlock. Do not automatically revert to an old API after a possible dispatch or while an initial outcome is unresolved; stop outbound use, preserve data and review the exact attempt in the normal UI. No destructive down/reset or blind migration retry is admitted. Initial activation checks precede operator sends."],"activation":["Recreate only selected API/Web using newly verified local images, no pull/restart of preserved providers or databases.","Verify health and compiled/bundle equality through the existing gateway.","Public gateway config uses static upstream host resolution. After API/Web replacement, validate nginx config and gracefully reload only the existing gateway process so it resolves current API/Web container addresses; preserve its container/network/volume. Record health and served bundle after reload, not an old cached upstream. No provider/database restart.","If a new owned temporary HTTPS tunnel is needed, validate DNS/TLS/health/assets and then have operator update Meta callback/privacy URLs; no automatic provider configuration changes."],"assisted_proof":["Operator logs in normally; agent does not extract OWNER password or enumerate live business rows.","In the nonofficial BU, operator opens a consenting test contact with explicit DDI, previews and confirms one first text; recipient replies.","In the official BU, operator selects the already-approved own-account text template through the shared catalog, fills fictitious/test values, previews and confirms once; recipient replies.","Record only safe outcome/state/timestamps and source-runtime attestation. Do not persist phone/contact/body/token.","No automated sends, new contacts, routing changes, migration/registration at Meta, or Railway deployment."],"current_status":"E64 complete candidate and images are historical. Architecture r4 identifies3open claim/lock/query blockers; causal tests/compatible remediation pending. No activation request until fresh corrected proof/images/assessment.","build_context_positive_inputs":{"api":{"roots":["api-app/src","api-app/prisma"],"exact_files":["api-app/Dockerfile","api-app/package.json","api-app/package-lock.json","api-app/tsconfig.json","api-app/tsconfig.build.json","api-app/nest-cli.json","api-app/docker/entrypoint.sh"]},"web":{"roots":["web-app/src"],"exact_files":["web-app/Dockerfile","web-app/package.json","web-app/package-lock.json","web-app/tsconfig.json","web-app/vite.config.ts","web-app/index.html","web-app/nginx/default.conf.template","web-app/docker/40-config-js.sh","web-app/public/config.js","web-app/public/privacidade.html"]},"policy":"Reject symlinks; hash each positive input, produce generated archive only. Exclude every .env, node_modules, existing dist, e2e/test artifacts and all unlisted paths. Add no extra file by discovery or implicit COPY context. Source specs under admitted src remain public build inputs; build exclusions remain canonical."},"prepared_build_context_receipt":"positive-build-contexts-e64-v1.1.json","entrypoint_scope":"Existing API entrypoint mechanically keeps ownership of the preserved named file volume at /dados/arquivos, then runs as node. No host .local-files bind, agent content inspection, payload mutation or file deletion is proposed.","candidate_receipt":"all-result-e64-v1.1.json","build_context_current_recheck":"image-build-root-collection-e64-v1.1.json","concrete_images":{"api":{"tag":"leadshug-stcon04-api:e64","id":"sha256:0b6d31296ca7ac8aee3ddfc2ce93a8c8e6af453af23a4218c5c4c416e0974a83"},"web":{"tag":"leadshug-stcon04-web:e64","id":"sha256:9787da8f734123e4f2875ce9b47c7bb23b45a8d64bbba98a830d51dd05f9f53b"}},"concrete_image_evidence":["image-build-attestation-e64-v1.1.json","image-build-root-collection-e64-v1.1.json"],"current_source_fingerprint":"70c038f24f15cf4a26a65c545bc9e3fba336a67a9cde7bfcb8cdec9910949340","current_web_bundle_sha256":"f8e97efa6777dbc496b74cd527b1bae78e7766e4a4d58f752f7816cb62444343","recorded_at_utc":"2026-10-23T02:41:54.779940+00:00","historical_images":"E54 images remain historical build proof only and must not activate this changed candidate."}
```

### final-diff-guard-boundary-proposal-v1.1.json

```json
{"kind":"Concrete proposed one-time delivery inspection exception; NOT approved or executed","governing_todo":"foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md","existing_restriction":"The approved TODO forbids reading/listing/stat/hash/traversal/mount of private paths, and permits only positive public inspection. No exception has been inferred.","why_needed":"The required unmodified canonical todo_diff_expectation_guard.py enumerates real tracked and non-ignored untracked differences for all four declared repositories. It has no positive-pathspec/private-prune argument. A public-only inventory cannot truthfully substitute for that guard.","proposed_exception":{"purpose":"One-time canonical delivery diff inspection, after the functional candidate and reviewable evidence are complete.","scope":"Only operations the canonical guard and its Git subprocesses require for declared root/api/web/foundation repository baselines.","private_access":"May enumerate/stat private paths and internally read/hash tracked file bytes as Git requires to compare changes or detect renames. No private file content is printed or published.","mutations":"None: no private-file edits/deletes, Git staging/commit, topology changes or service/provider changes are authorized by this exception.","raw_result_destination":"Restricted local /tmp files, mode0600; do not commit raw stdout/JSON or private filenames.","public_receipt":"Tool-source hash, exact canonical arguments, terminal exit/outcome, counts and stable violation codes only. No private path values or content.","on_failure":"Classify and report the guard failure; do not erase private files, silently filter violations, edit Delphi or claim GO.","scope_lifetime":"One completed canonical guard run and redacted collection; follow-up private inspection requires its own established authority."},"canonical_command_proposed":["python3","delphi-ai/tools/todo_diff_expectation_guard.py","foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md","--repo-root","/mnt/c/unifast/leadshug/leadshug_now_docker","--json-output","/tmp/stcon04-final-diff-guard-private.json"],"approval_handling":"Present the concrete candidate and this exact exception to the user before any private inspection. If explicitly approved, record the limited exception in the governing TODO and re-run normal authority before executing. No implementation scope, DoD or classifier weakening is proposed.","current_status":"Proposal only. Implementation and positively bounded test work continue. Full diff-guard GO remains absent.","other_closeout_helpers_assessment":{"todo_completion_guard":"Use explicit governing TODO argument, not --all-completed; inspected helper reads documentary TODO/evidence, no Git/private product enumeration.","todo_closeout_guard":"Use canonical --repo foundation_documentation with explicit governing TODO. Inspected git_context invokes full status only on that selected Foundation repository; this is the authorized documentary authority, not root/API/Web private-product repositories. No private-product exception inferred for closeout.","scope_lifetime":"Only the full diff guard remains the proposed one-time private inspection exception. Runtime opaque Compose configuration access is separately named in the activation proposal."}}
```

### verification-debt-preclosure-e46-v1.1.json

```json
{"kind":"Pre-closure verification-debt audit, complete positive public roots","recorded_at_utc":"2026-10-22T22:57:26.296530+00:00","command":["bash","delphi-ai/tools/verification_debt_audit.sh","--todo","foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md","--path","api-app/src","--path","api-app/test","--path","api-app/prisma","--path","web-app/src","--path","web-app/e2e"],"actual_exit_code":2,"stdout_sha256":"c565d5609b509e0c37371c9b3851c353a3b58bcba81280e5560ad6f5dfb7d4d4","raw_public_output":"verification-debt-output-e46-v1.1.txt","summary_lines":["Inline code TODO debt classification: none","Unchecked checklist items:","Counts: waiver=42 blocker=58 unchecked=45 accepted_inline=0 canonical_link_missing=0 cleanup_required=0"],"boundary":"No --scan-git-modified, no actual env/private paths. Exact TODO plus five public source roots.","stage":"Pending implementation assurance; unchecked delivery criteria and later runtime/guard approval are explicit gates, not hidden debt or evidence of completion.","retained_prior_debt":["SEC-R6-04","OPS-R4-01","TQA-ST05-03"],"final_disposition":"Not final clean closure; classify reported evidence/inline findings before delivery.","outcome":"high","inline_code_todo_debt_classification":"none","classification":[{"signals":"42waiver/58blocker/45unchecked, raw heuristic counts","meaning":"Planning/history language, explicit n/a and currently open delivery gates match broad regex; counts do not imply42 granted waivers. No closure was claimed.","disposition":"Preserve current pending gates; re-audit at actual final closeout."},{"signals":"Inline markers in five complete public roots","meaning":"No TODO/FIXME/HACK/TBD/XXX marker requiring inline cleanup.","disposition":"none"},{"signals":"Stable architecture decisions not yet promoted to module docs","meaning":"Approved module consolidation gate follows implementation/assurance and has not run.","disposition":"Concrete module mapping/consolidation remains required before completion."}]}
```

### context-rehydration-boundary-disclosure-e57-v1.1.json

```json
{"recorded_at_utc":"2026-10-23T01:24:45.581666+00:00","command":"rg --files -g AGENTS.md -g !node_modules -g !**/.env* -g !**/.local-files/**","cwd":"workspace parent","actual_exit":1,"actual_stdout":"empty","classification":"root-wide file discovery was broader than the approved positive public roots; procedural lapse","limits":"No private values or returned filenames were observed. Empty output does not prove which directories ripgrep traversed. No product/runtime mutation.","correction":"Stopped broad discovery. Exact ancestor AGENTS reads and declared positive public source/evidence paths only thereafter."}
```

### implementation-review-collection-r4-r5-v1.1.json

```json
{"kind":"R4 architecture/security/cutover plus full R5 test-quality collection","recorded_at_utc":"2026-10-23T03:12:43.466012+00:00","architecture":{"session_id":84697,"actual_exit_code":0,"actual_turns":1,"actual_tools":0,"result":"implementation-architecture_adherence-r4-result-v1.1.json","result_sha256":"f3b5c72fb4b131f2287743d259d568c39131cd507f60bb8debec7127f117baf7","assessment":"Three concrete source-supported blockers, including high final eligibility/lock wait. Full security lens maps high-risk boundaries/safe simulations/threat sources/residuals without claiming independent runtime execution; fresh correction/proof required."},"test_quality":{"session_id":63065,"actual_exit_code":0,"actual_turns":1,"actual_tools":0,"result":"implementation-test_quality_audit-r5-result-v1.1.json","result_sha256":"f14c9cd89242943fcb99f36052d4659bdcbd362b54ec84d21cbb7f0ff61b4b96","assessment":"Full eight-section workload present: five questions, all255signals, causal chronology, independent template groups, DI/fallback, command/CI/platform statuses and performance/security/structural/residuals. Credible E64 test-quality candidate, not final delivery. New architecture schedules/plans still require tests and fresh affected audit.","adjudication":["TQA-R5-01 integrated for actual DOD11-13/runtime/operator/module/fullguard/final gates; remain open.","Remote CI is not evidenced and no promotion/production claim is made. Challenge its phrasing as an added REQUIRED gate for this local-only TODO: approved VAL/DoD require canonical CI-equivalent local evidence and assisted own-channel proof, not product Git/promotion/remote CI authority. No remote operation is added.","Report section8 attaches inaccurate D02-D10 shorthand labels. Frozen exact TODO decisions and current decision-module map remain authority; no blanket 1-to-1 Adherent gate is closed from those labels."]},"cutover":{"session_id":8244,"actual_exit_code":0,"actual_turns":1,"actual_tools":0,"result":"implementation-cutover_integrity_audit-r4-result-v1.1.json","result_sha256":"df1b6f45bf0169cbd98275f976401bbd4f03deba0118e47761a3a6375c2738a8","assessment":"No additional code-integrity defect, two required delivery gate cards remain open and integrated into pending work."},"tqa_r4":"Actual terminal0/schema-valid paragraph retained and strictly merged but not accepted as full-workload gate. No live reviewer interruption; R5 includes same complete current source plus explicit output checklist and actual same-run CI marker.","source_recheck":"after-review-source-recheck-e64-v1.1.json","stage":"InProgress/Pending; no activation, private inspection, module consolidation or final delivery."}
```

### candidate-source-preflight-e70-v1.1.json

```json
{"kind":"E70 bounded index refinement and faithful session/performance fixture preflight; actual validation pending","recorded_at_utc":"2026-10-23T04:19:49.099445+00:00","source_seal":"all-source-seal-e70-v1.1.json","source_fingerprint":"0867ad4ad9eefb75d2a9d7ea7a1a04db605fd49c2364549c6774d876e5c1286a","exact_delta":["api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","api-app/prisma/schema.prisma","api-app/test/initial-message.e2e-spec.ts"],"decisions":["Retain one active-admission index, order conversation/released/createdDESC/idDESC/BU to serve both scoped options and conversation-wide conflict lookup. Preserve whole-conversation exclusion and every existingquota/unique index. Same admittedschema/disposable-only150000 migration;5s/60s unchanged.","Actual real producer context from existing prepareInitial seeds representative rows. Keep256active admissions, add2048released history; released attempts/admissions2hoursold avoid independently testing quota refusal before intended conflict query. No quota bypass or result weakening.","Defaultplanner, actualPrismaSQL/params, native indexdef and plan costs/rows/buffers captured. Original noSort/≤11strictoracles remain, extended to actualconflictPOST query with same10/truncation andzeroactualport/Messageeffects. HistoricalE69small-table scan retained; no universal planner/latency claim.","Existing SessionService explicit-clock seam used only after phoneGETbarrier. Real signed verifier called with future time; provider clock untouched. Retain409exactcode/zeroPOST/OUT plusnewactualexpiredclockcall and persistedREJECTED/nodispatch/releasedslot proofs. ProtectedSessionService unchanged."],"causality":"E65/E66 are actual pre-fix claim/lock/planRED. E67lint andE68import failures are distinct. E69actual6raceprobes passed; representative-volume/clock fixes added after genuine support mismatch, no retroactive testfirst or new-volume causalRED claim.","scope":"Same approved WHAT/lockorder/publiccontract; exact3sourcechanges. Currentfixed claim sources unchangedE69. No preservedruntime/private/provider access; all38protected exact."}
```


### Omitted R6 receipt-block references (bounded deduplication)

Each item names a receipt block omitted from this repeated R6 evidence section; its full historical source remains at the named evidence path. E70/E71 results and E72/E73 causal receipts are embedded with exact hashes in the history section below.

- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-result-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-source-recheck-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/browser-freshness-collection-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/producer-consumer-crosswalk-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/candidate-criterion-index-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/security-candidate-map-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/decision-module-candidate-map-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/image-build-attestation-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-r4-resolution-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/ci-parity-current-marker-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/current-synthetic-pcv-samples-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/candidate-source-preflight-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-result-e70-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/api-result-e65-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/api-result-e66-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-result-e67-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-result-e68-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-result-e69-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/remaining-failure-triage-e69-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-eps-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-frc-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-bci-e71-v1.1.json` SHA256 `hash not embedded`
- `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/pcv-rls-e71-v1.1.json` SHA256 `hash not embedded`

## Current concrete R7 module-consolidation proposal and unified patch (pending application/runtime/guard/final review)

### module-consolidation-r7-proposal-v1.1.md

SHA256 `acc77074e913bd87e2e037f920b5a226178466f970ee1ae1df9fba85362de16f`. verified fenced metadata; concrete draft only, not applied module proof.

```markdown
# ST-CON-04 — concrete module consolidation proposal

This proposal is a reviewable patch, not canonical module authority or delivery proof. It replaces the r6 narrative proposal as the concrete candidate for later review/application; all historical artifacts stay immutable.

```json
{
  "kind": "Concrete two-module documentation patch proposal; not applied",
  "recorded_at_utc": "2026-10-23T05:27:03.083992+00:00",
  "patch": "module-consolidation-r7-v1.1.patch",
  "patch_sha256": "70b6d9fc91f037556b936be2b143601aa10339d3313d67b2fe692acada5ace9f",
  "paths": [
    {
      "path": "foundation_documentation/modules/inbox-and-conversations.md",
      "baseline_sha256": "24b3f1edd8f10bf991d61135be2364b49679c43e5894ce024c2d5169921756a2",
      "proposed_lf_text_sha256": "a6711b55b173f2f8b3f6bf83ed4fbb55e6a7e2ffa0132dfd80f594d838d75d44"
    },
    {
      "path": "foundation_documentation/modules/integrations-and-channels.md",
      "baseline_sha256": "6b1865ab4f27458e1e1e225535e2f4a713e987e18344ca86d3f9411fa6c6f168",
      "proposed_lf_text_sha256": "3dfd99329d974e5a1aac22f04745017764d4c94b2566e0c63383151b1ef7459f"
    }
  ],
  "application_conditions": [
    "Actual corrected fullGREEN, independent findings resolved and decision/module consistency review.",
    "Apply only at the authorized delivery/consolidation stage; retain truthful runtime/operator/fullguard/final gates until actually satisfied.",
    "Preserve historical ST05/ST06 text and clearly identify the two approved supersedes. No constitution/roadmap/product/private changes.",
    "Closeout must update the active TODO link only when the TODO is actually moved; no broken future-completion links now."
  ],
  "current_state": "Drafted during E73 ALL; this proposal establishes no test result or application. Selected later actual receipts govern readiness."
}
```

The patch supplies the complete nine-route BFF contract, states and field definitions; manual open/no-send semantics; durable intent, admission and local recovery; exact Channel union and protocol ownership; trusted managed-resource IN provenance and `requiresWindow`; clock/lock/CAS bounds; same-account catalog subset and explicit historical supersession mapping. No canonical module has been changed.
```

### module-consolidation-r7-v1.1.patch

SHA256 `70b6d9fc91f037556b936be2b143601aa10339d3313d67b2fe692acada5ace9f`. literal unified diff; SHA256 verified against proposal metadata.

```text
--- a/foundation_documentation/modules/inbox-and-conversations.md
+++ b/foundation_documentation/modules/inbox-and-conversations.md
@@ -13,6 +13,44 @@
 ## API Endpoint Definitions
 
 BFF routes use `/api/bff`; public integrations use `/api/v1`; webhook contracts use `/webhooks`.
+
+### Iniciar conversa e primeiro envio — ST-CON-04
+
+Contrato v1.1 aprovado no [TODO ST-CON-04](../todos/active/features/TODO-leadshug-start-conversation-by-contact.md). O TODO registra a execução, os resultados e o estágio de entrega; esta definição não transforma aceitação do provedor em entrega ao destinatário.
+
+A abertura manual exige telefone com DDI explícito e autorização ATENDENTE ou superior na BU. Normalizar somente espaços, parênteses, hífen, ponto e um `+` inicial; aceitar 8–15 dígitos, primeiro diferente de zero, sem inventar país. BU/contato continuam uma identidade única. Nova conversa fica QUEUED, unreadCount=0 e lastMessageAt=null; a reutilização conserva o estado existente. Abrir não envia, marca leitura, assume atendimento, reabre/fecha, nem dispara bot. A primeira IN conserva os triggers existentes; nenhum trigger é inventado para a abertura manual.
+
+Todos os endpoints abaixo usam a sessão BFF assinada e a interseção do tenant do usuário com a BU; ATENDENTE+ exige grant atual. POST exige CSRF, campos conhecidos e IDs válidos. Sem sessão401; grant insuficiente em BU conhecida403; conversa/canal/tentativa fora do escopo404. Nenhum corpo aceita URL de protocolo, segredo, ID bruto de conta Meta ou payload Graph arbitrário. Leituras e preview são locais; disponibilidade não substitui autorização nem a revalidação de um novo envio.
+
+| Método / caminho sob `/api/bff` | Corpo / condição | Resposta / efeito |
+| --- | --- | --- |
+| `POST /business-units/:buId/conversations/open` | `{telefone}` string até40caracteres; readiness local exigida somente ao criar |201 nova ou200 reutilizada: `{conversaId,criada,contact}`; sem I/O externo e sem efeitos de atendimento/leitura/envio |
+| `GET /conversations/:id/start-options` | Sem corpo; contexto autorizado |200 capacidades/readiness/janela locais, tentativa ativa, até10tentativas recentes e até10admissões ordinárias ativas, ordenadas por createdAt/id com flags de truncamento; sem chaves/credenciais ou I/O externo |
+| `POST /conversations/:id/initial-message-preview` | `channelId` UUID, `expectedGeneration` inteiro positivo, `mensagem` TEXTO ou TEMPLATE |200 texto renderizado e `previewFingerprint` vinculado ao contexto; não grava nem chama provedor; stale/unsupported409 |
+| `POST /conversations/:id/initial-messages` | Mesmo corpo imutável, `previewFingerprint` de64hex e `Idempotency-Key` UUID |201 aceitação local nova;200 replay terminal;202 tentativa ativa;409 bloqueio/conflito/ambiguidade com estado seguro;503 resultado local/remoto inconclusivo. Nenhum sucesso afirma entrega/leitura no aparelho |
+| `GET /conversations/:id/initial-messages/:attemptId` | Lookup scoped; não exige a chave do navegador |200 estado/proveniência/persistência/ações seguras; sem escrita ou I/O externo |
+| `POST /conversations/:id/initial-messages/:attemptId/reconcile` | Corpo vazio; autorização atual e CAS |202 lease viva;200 classificação/recuperação local; PREPARED expirada fecha sem envio; SENDING expirada vira incerteza. Zero chamadas externas |
+| `POST /conversations/:id/initial-messages/:attemptId/acknowledge` | Corpo vazio; `X-Confirm-Duplication-Risk: true` |200 liberação irreversível somente AMBIGUOUS/EXTERNAL_ACCEPTED_LOCAL_BLOCKED e relógio do banco >= deadline original; antes409 ACK_TOO_EARLY com eligibleAt; repetição já liberada idempotente. Não reenvia nem reescreve o resultado |
+| `POST /conversations/:id/dispatch-admissions/:admissionId/reconcile` | Corpo vazio; autorização atual |200 classificação local de admissão ordinária; PREPARED expirada é liberada e SENDING expirada continua excluída como UNCERTAIN. Zero chamadas externas |
+| `POST /conversations/:id/dispatch-admissions/:admissionId/acknowledge` | Corpo vazio; mesmo header explícito de risco, autorização/auditoria atuais |200 liberação irreversível somente UNCERTAIN após deadline original; antes409; não cancela HTTP já reivindicado, reenvia ou modifica Message |
+
+**Field Definitions**
+
+- `mensagem`: `{tipo:"TEXTO",texto}` não vazio com até4096pontos de código Unicode, ou `{tipo:"TEMPLATE",templateId,language,catalogAfter?,expectedDefinitionFingerprint,parameters}`. TEMPLATE usa ID remoto até128caracteres, idioma até16, cursor opcional até512 e fingerprint64hex; parameters é mapa NAMED ou array POSITIONAL, máximo20valores não vazios até1024pontos de código cada; snapshot renderizado até4096. Envelope JSON tem limite próprio, sem ampliar esses limites de conteúdo.
+- Estado inicial: PREPARED sem claim; SENDING claim durável; EXTERNAL_ACCEPTED ID externo conhecido; EXTERNAL_ACCEPTED_LOCAL_BLOCKED aceitação conhecida com conclusão local bloqueada; SUCCEEDED Message persistida; REJECTED prova de não despacho/recusa estável; AMBIGUOUS resultado externo desconhecido. SUCCEEDED não equivale a entrega/leitura.
+- Admissão ordinária: PREPARED ainda sem claim; SENDING reivindicada; SETTLED resultado conhecido; UNCERTAIN resultado desconhecido e exclusão mantida. Não se cria idempotência global para envios ordinários.
+- `providerAcceptance=CONFIRMED` requer ID válido capturado; caso contrário UNKNOWN. `receiptPersistence` e `localMessageState` são RECORDED somente após commit positivo ou readback exato; caso contrário UNCONFIRMED. Falha de ACK do banco não prova rollback.
+- Slot é ativo enquanto `slotReleasedAt` é null; liberação é irreversível, independente do resultado tardio. Cada tentativa/admissão mantém owner nonce e deadline imutável de90s; passagem de tempo não autoriza takeover de envio incerto.
+
+O domínio inbox coordena intenção durável, sem copiar sender, catálogo ou aceitação. OutboundService mantém o único envio comum; MessageAcceptanceService mantém a única gravação/reconciliação keyed de Message. A reserva verifica atomicamente a exclusão na mesma conversa: slot inicial ativo bloqueia nova admissão ordinária; qualquer admissão ordinária não liberada bloqueia reserva inicial. Envios ordinários entre si conservam concorrência e contratos BFF/público/BOT, inclusive diagnóstico legado sem ID. O token ordinário não é retry ou lookup de provedor.
+
+Um novo envio captura canal/contexto/requisição e fingerprint imutáveis. O replay canônico da mesma chave ocorre antes de nova elegibilidade. Preview não autoriza envio. Finalizar status/owner depende do CAS original anterior ao HTTP, avaliado antes de a aceitação alterar timestamps da conversa; claim/close concorrente vence. Aceitação externa é gravada separadamente antes de concluir Message/slot localmente. Unique conflict desfaz a transação inteira; depois há readback exato e no máximo uma nova tentativa da transação local, sem repetir HTTP. Realtime pertence só ao vencedor de criação após commit confirmado; a lacuna de crash permanece best-effort, sem outbox/exactly-once externo.
+
+A recuperação explícita é local e zero-rede. PREPARED viva conserva exclusão; expiração comprovadamente anterior ao claim permite rejeitar/liberar. Aceitação conhecida pode ser concluída localmente sob autorização atual. ACK de risco nunca promete cancelar HTTP ou impedir duplicação externa tardia. Resultado tardio não retoma slot liberado, não altera sucessor e não rouba owner/reabre close posterior. Cada novo envio continua sujeito aos limites aprovados por ator/conta e aos orçamentos de consulta/rede.
+
+O diálogo e o snapshot original pertencem a ator/BU/conversa; mudança de BU desmonta o contexto, inclusive resposta atrasada e A→B→A. Recarregar recupera a mesma chave/corpo sem POST automático. Falha de storage retém estado conservador e ação local explícita; erro/incerteza preserva rascunho e controles de recuperação, com preview escapado e operação por teclado. Nada contacta destinatários automaticamente.
+
+A janela textual vigente e a capacidade do Channel estão em [primeiro envio e proveniência](integrations-and-channels.md#primeiro-envio-e-proveniência--st-con-04). Timeline/cursor continuam por createdAt/id e seu contrato anterior é preservado.
 
 ## Contrato aprovado da timeline da inbox
 
@@ -73,6 +111,8 @@
 
 BFF, partner public API and Typebot consume one OutboundService. Trusted BFF human/public EXTERNO/bot source intent is established before dispatch. MessageAcceptanceService remains the sole keyed writer for provider-ID Messages and sender/echo convergence. Human/public completion conditionally updates the current owner, preserves a newer concurrent claim and sets IN_SERVICE except existing group behavior. Bot retains queue/status/human owner/unread semantics and stops without replay after uncertain or blocked output.
 
+**Baseline histórico ST-CON-06:** as referências abaixo a ST-CON-04 ainda não implementado e à janela por latest-IN/createdAt registram a fatia entregue. Para o contrato vigente, as duas substituições aprovadas estão em [ST-CON-04](#iniciar-conversa-e-primeiro-envio--st-con-04); seleção ordinária de origem e demais invariantes permanecem.
+
 Human/public responses use the deterministic latest message origin ordered by createdAt DESC,id DESC. An unavailable selected origin is not replaced by another connected channel. Without history, only a sole binding can be selected; zero and multiple bindings have explicit absent/ambiguous errors. Bot responses remain pinned to their accepted verified ingress even if another channel becomes the latest origin. The selected binding's free-text-window requirement applies to all senders before every text. Existing latest-IN stored timestamp without transport filtering is preserved and must be revisited in ST-CON-04.
 
 ST-CON-04 first-send, if separately approved, consumes the shared template catalogue owned by [Integrations and Channels — ST-CON-05](integrations-and-channels.md). Before every first-send it independently revalidates that the selected template is currently eligible (`APPROVED`, observation at most 300 seconds old) for the current selected account/channel context and rechecks the existing send policy. It adds no template authoring/catalogue, sender, or route here. ST-CON-04 remains unimplemented and requires its own TODO and approval.
--- a/foundation_documentation/modules/integrations-and-channels.md
+++ b/foundation_documentation/modules/integrations-and-channels.md
@@ -110,6 +110,8 @@
 
 Contrato v1.3 aprovado e exercitado localmente: all93791 passou613testes, revisões independentes de aderência/segurança/cutover/TQA e Performance convergiram, com uma dívida baixa explícita de precisão de métrica de teste. O operador confirmou nova IN e resposta OUT nos vínculos oficial e não oficial após ativação das imagens atuais; a proveniência fonte→imagem→container→HTTP foi conferida antes e depois. A revisão final e os guards de closeout são registrados no [TODO governante](../todos/completed/features/TODO-leadshug-channel-abstraction.md). Evidências: [validação automatizada](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/v13r4-final-validation.json), [ativação](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-activation-provenance-v13r4-final.json), [prova assistida](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-operator-proof-v13r4.json) e [proveniência posterior](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/post-operator-readback-v13r4.json). Não é prova de produção, disponibilidade contínua ou redes futuras.
 
+**Baseline histórico ST-CON-06:** o texto abaixo registra o envio textual e os limites entregues nessa fatia. As únicas substituições vigentes aprovadas são a união de payload e a janela qualificada de [ST-CON-04](#primeiro-envio-e-proveniência--st-con-04); o catálogo/management ST05 continua separado.
+
 Channel is the domain text-send abstraction. TextMessage carries kind:text, opaque recipientRef and text; sendMessage returns a discriminated result. Current Meta/Evolution adapters encapsulate protocol addresses and credentials in an immutable operation instance created by an explicitly registered factory. ChannelResolver is injected through one ChannelTransportModule; existing BFF/Public/Webhooks composition shares its resolver and outbound orchestration. Common senders do not import concrete clients, switch on provider, use service location, mutate singleton credentials, or retain an old dispatch shim. Registration/protocol clients remain legitimate narrow consumers outside the common send boundary.
 
 A server-authorized conversation/BU or accepted verified bot ingress selects the binding. The context captures channel/BU, resource identity, generation, epoch and official credential version. Before the sole external POST, local owner/identity/readiness/version checks fail closed. Same-resource REAUTORIZAR changes generation; it is distinct from a credential-version-only reseal after dispatch. Captured context is never rebound to a newer identity. No HTTP occurs in a DB transaction, and no automatic external retry or per-send external probe is introduced. The local-check-to-network interval and crash recovery remain explicit limitations.
@@ -151,6 +153,32 @@
 ### Consumidores seguintes e limites
 
 ST-CON-05 is approved and implemented locally; its durable contract is consolidated below. The seller creates and submits directly for Meta review; no administrator intermediary is inserted. ST-CON-04 may later consume eligible templates for first-send outside the official window, but needs its own approval and must independently revalidate current eligibility and account/channel context. Existing public POST conversation creation before attempted send remains unchanged. Local channel activation and assisted IN/OUT evidence belong to their respective TODOs and do not establish production readiness.
+
+## Primeiro envio e proveniência — ST-CON-04
+
+Contrato v1.1 aprovado no [TODO ST-CON-04](../todos/active/features/TODO-leadshug-start-conversation-by-contact.md); estado/evidência de entrega pertencem ao TODO. Owner de abertura/intenção/recuperação e [endpoints BFF](inbox-and-conversations.md#iniciar-conversa-e-primeiro-envio--st-con-04): inbox-and-conversations. Este módulo mantém transporte, resolução scoped e catálogo/observação, sem segunda API de modelos.
+
+O Channel continua a abstração única de envio: `sendMessage` recebe a união discriminada `text | approved-template`, com `supportedKinds` readonly. Consumidores dependem do abstrato; factory/registry injetam concretos imutáveis por operação. Meta implementa os dois tipos e seu protocolo; Evolution declara somente text e rejeita template com resultado tipado e zero HTTP. Instagram, Messenger e Telegram continuam pontos futuros de extensão, sem implementação, métodos no-op, casts concretos ou service locator. Transporte não importa management; o coordenador inbox compõe as duas capacidades estreitas, preservando DI acíclica.
+
+O início usa seleção explícita de canal, não latest-origin/fallback. Resolução, descriptor e catálogo devem coincidir em tenant/BU/canal, identidade de recurso, geração, pairing epoch, referência opaca da conta e versão da credencial ativa. Endereço de protocolo, token e ID bruto de conta são encapsulados pelas integrações. Envios ordinários continuam com sua seleção de origem/ingresso verificado e DTOs/diagnósticos anteriores, observando o interlock compartilhado.
+
+Readiness e `requiresWindow` são preservados. Quando o canal exige janela para texto, usar somente o maior `Message.officialInboundAt` qualificado da conversa e do recurso atualmente selecionado, com limite estrito de24horas. A origem deve ser IN Meta assinada, identidade atual/verificada e sob gestão; timestamp inteiro positivo e não futuro. No owner de aceitação, a qualificação managed vem da mesma linha de identidade já bloqueada até o commit. Mensagem de recurso fora de gestão continua aceita, mas seu timestamp confiável fica null; ativação posterior ou replay não promovem essa proveniência. Ausência/má formação/futuro, createdAt, importação e IN não oficial não abrem a janela. Timeline/cursor continuam createdAt/id; a configuração herdada `requiresWindow=false` conserva sua exceção. Template oficial elegível não exige a janela de texto.
+
+Todos os consumidores de disponibilidade/envio usam a mesma política; leitura não chama provedor nem autoriza POST. No CAS PREPARED→SENDING, janela aplicável e lease são comparadas ao relógio atual do banco na mesma atualização de owner/slot. Readiness BU ativa, binding de canal e versão de credencial são protegidos por pins compartilhados; pins e fence de usuário/grant usam NOWAIT para não inverter a ordem identidade→advisory de contato→conversa→intenção nem formar ciclo com o owner ST05 inalterado. Conflito de lock aborta/rollback, sem consultas numa transação abortada. Aceitação externa conhecida continua explícita se a conclusão local for bloqueada; nenhum lock fica aberto durante HTTP.
+
+O catálogo ST05 segue como único owner de observações/TTL/leases/fences e flags de autoria. Página disponível não basta: o item selecionado precisa estar disponível, APPROVED e no contexto atual. Flags `supported/eligible` de autoria são preservadas e não descrevem todo suporte de primeiro envio; um POSITIONAL disponível pode ser válido para o renderer inicial mesmo quando autoria o marca unsupported. Renderer textual local aceita somente BODY e no máximo HEADER/FOOTER TEXT estáticos, rejeita componente desconhecido/mídia/botão e placeholders fora de BODY. NAMED exige chaves exatas; POSITIONAL exige1..N contíguos, com repetições consistentes. Fingerprint inicial é próprio e vincula definição/contexto/contato/valores; preview escapado permanece sem efeitos.
+
+Cada nova tentativa oficial verifica remotamente, antes do claim, a definição exata e APPROVED na mesma conta através das leituras limitadas existentes. O mesmo Channel Meta encapsula o cliente inicial privado; não há sender paralelo. O POST usa a conta de mensagens capturada e destinatário `+` com DDI completo, inclusive entre países, mantendo o caminho textual ordinário anterior. Orçamentos: no máximo6GETs e1POST,10s por operação e75s totais dentro do deadline de90s; redirects, dados inválidos, erro transitório e timeout não autorizam fallback/retry. Depois do claim, mudança externa pode produzir recusa/incerteza e não é convertida em sucesso.
+
+Recuperação de tentativa é local, sem nova chamada de provedor. ID válido é aceitação externa, não entrega/leitura; recibo e Message têm persistências separadas. Preservar os limites SEC-R6-04, OPS-R4-01 e TQA-ST05-03: esta fatia não amplia recovery ST05 para público/Railway nem reescreve sua causalidade histórica.
+
+A persistência acrescenta proveniência nullable, intenção e admissão duráveis, unicidade/quotas e índices de ordem aprovados. Opções de tentativa usam `(conversation_id,bu_id,created_at DESC,id DESC)`; admissões ativas usam um único índice SQL parcial `(conversation_id,created_at DESC,id DESC,bu_id) WHERE released_at IS NULL`. O conflito ordinário conserva escopo da conversa inteira. LIMIT11 produz10itens e truncamento; EXPLAIN de SQL realmente capturado diferencia linhas retornadas, filtradas/examinadas e buffers. As medições sintéticas não são SLO/capacidade de produção. Migrações aditivas exigem alvo/autorização próprios, lock5s/statement60s, sem reset/drop/down/resolve ou retry cego.
+
+### Substituições e decisões preservadas
+
+- A propriedade text-only do Channel entregue em ST-CON-06 é substituída pela união única acima; o princípio de depender da abstração e o único sender são preservados.
+- A janela por latest-IN/createdAt do baseline ST-CON-06 é substituída pela proveniência qualificada atual; ordenação/cursor e seleção ordinária de origem permanecem.
+- ST-CON-05 D09 continua documentado como decisão histórica daquela fatia: capability estreita de management, sem recipient-send. A nova união é responsabilidade de ST-CON-04, não uma ampliação de métodos do catálogo/autor.
 
 ## Modelos textuais — ST-CON-05
```

## R6 actual review collection and hash-bound individual results

### implementation-review-collection-r6-v1.1.json

SHA256 `4a27aa722196bbe1f02db0c37de0b8421fb2647fa3f1c300e8504ccc8711aa9f`

```json
{"kind":"Actual terminal independent r6 collection and root disposition","recorded_at_utc":"2026-10-23T05:08:44.112208+00:00","source_seal":"all-source-seal-e71-v1.1.json","reviews":[{"kind":"architecture_adherence","actual_session_id":8723,"actual_exit_code":0,"actual_turns":1,"actual_tools":0,"result":"implementation-architecture_adherence-r6-result-v1.1.json","result_sha256":"7ab3f292fbc7d812733225605b79e91489a76800b156965c086bd0b20ede00fa","finding_ids":["ARCH-ST04-R6-01"]},{"kind":"test_quality_audit","actual_session_id":81829,"actual_exit_code":0,"actual_turns":1,"actual_tools":0,"result":"implementation-test_quality_audit-r6-result-v1.1.json","result_sha256":"8ac37114ee7c8ba04e838012b6531f764cf0128e05e1d86624fedf2b84112844","finding_ids":["F-035510C8","TQA-R6-01"]},{"kind":"cutover_integrity_audit","actual_session_id":21413,"actual_exit_code":0,"actual_turns":1,"actual_tools":0,"result":"implementation-cutover_integrity_audit-r6-result-v1.1.json","result_sha256":"454787177a18cbe96e7ac6c77be468c2f4de0796e8c0a6ce903f3cc8f149fa54","finding_ids":["F-035510C8","F-91F64098","F-300A50BF"]}],"root_disposition":["Architecture accepts the three corrected r4 behaviors at the bounded synthetic level; new ARCH-ST04-R6-01 is source-confirmed by root, Integrated for a narrow managed-lifecycle timestamp writer fix with causal signed-webhook/real-PG proof before mutation. Keep message acceptance compatible; null trusted timestamp for unmanaged identity.","TQA-R6-01 is Integrated: required native deadlock statistics must not default missing/malformed data to zero. Add a focused failure regression before helper fix.","TQA r6 has useful material findings and actual terminal/schema output, but does not deliver its requested complete eight-section whole-workload assessment. It is NOT accepted as the full independent TQA gate. Obtain a complete fresh audit against the corrected candidate; exact five questions,267/current signals, command/platform/DI/CI, causal chronology and decisions must be substantive text within permitted JSON fields.","Cutover finds no new code cutover defect; its runtime/operator/module/fullguard/final delivery gates remain integrated and open. Repeated F-ids are qualified by review/source; no pending gate is silently closed.","Current E71 images and activation proposal are now historical candidate proof until the two new findings are corrected and fresh source-bound validation/images/reviews exist. No activation/private-inspection request is issued."],"remaining":"InProgress/Pending; code release after exact test-only handoff/authority, immutable E71 receipts preserved."}
```
### implementation-architecture_adherence-r6-result-v1.1.json

SHA256 `7ab3f292fbc7d812733225605b79e91489a76800b156965c086bd0b20ede00fa`; byte hash verified against the collection result_sha256.

```json
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-architecture_adherence-r6-dispatch-v1.1.json","review_kind":"architecture_adherence","reviewer_label":"independent-no-context-architecture-r6","overall_assessment":"Changes required for one source-supported D-04 qualification gap. The bounded E71 evidence supports the three r4 corrections: final database-clock window predicates, shared mutable-context pins with nonwaiting authorization locks, and ordered recovery queries. Their causal failures, intermediate support failures and final regression results are distinguished honestly. No regression justifies reopening the other recorded resolved findings.\n\nD-01 preserves atomic opening, normalization and automation semantics. D-02 retains one Channel operation and avoids the management/transport DI cycle. D-03 preserves common outbound dispatch and sole MessageAcceptance ownership. D-04 centralizes window reads correctly, but the timestamp writer omits the explicit managed-lifecycle qualification described in the finding. D-05 preserves shared catalog ownership, fresh same-account verification and protocol pinning. D-06 implements durable intent, conservative uncertainty and local recovery. D-07 retains the approved finite ordinary/initial interlock and legacy outcome mappings. D-08 implements the bounded textual renderer independently of authoring flags. D-09 has bounded synthetic request, quota and migration evidence; preserved-runtime proof remains pending. D-10 separates receipt certainty from Message persistence and preserves the opaque account namespace.\n\nSecurity risk remains high; safe attack simulation is required. The supplied simulations cover session/CSRF, tenant and object authorization, descriptor/credential boundaries, persistence uncertainty, provider eligibility, replay, acknowledgment and browser ownership races. Forged grants, expired/revoked authorization, stale context, unavailable templates and duplicate-action schedules have reported disposable BFF/PG/browser evidence. The unmanaged-identity timestamp hypothesis below is source-supported but has not been reproduced in this package. No independent execution, live-provider exploitation or private-runtime inspection was performed. Supplied threat intelligence maps object authorization to https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/ and resource bounds to https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/; those sources were not independently refreshed here.\n\nPerformance is acceptable within the measured fixtures: current recovery queries avoid sorting and report 11 examined records, window projections are batched, and transaction boundaries exclude provider I/O. These observations establish neither production capacity nor a latency SLO. The finite admission design fits the approved intent without requiring an architectural redesign. Residual risks include external ambiguity, best-effort realtime, inherited SEC-R6-04/OPS-R4-01/TQA-ST05-03, outstanding TQA adjudication and the explicitly pending delivery gates.","recommended_path":"Add the narrow managed-resource timestamp protection and capture a causal signed-webhook/PostgreSQL regression before fixing it. Revalidate the affected behavior against a sealed candidate and obtain the required independent assessments. Preserve the three r4 resolutions. Implementation readiness must remain conditional until the new finding is resolved. Keep F-91F64098, F-300A50BF and F-035510C8 open for their recorded delivery gates: preserved-runtime migration/health/provenance, assisted own-channel sends and replies, module consolidation, separately authorized canonical diff inspection, and final assurance/closure. Refresh the activation proposal's historical E64 image/source references to the selected corrected candidate before presenting it for approval. E71 offline images and synthetic GREEN do not authorize activation or establish delivery; remote CI is not an additional required gate for this local-only scope.","performance_position":"acceptable","elegance_position":"acceptable","structural_soundness_position":"mixed","operational_fit_position":"mixed","findings":[{"finding_id":"ARCH-ST04-R6-01","severity":"medium","category":"adherence","formalizable_hint":"yes","candidate_rule_level":"project","title":"Trusted timestamp persistence does not require a managed resource identity","rationale":"SCOPE-03 and D-04 require officialInboundAt to originate from a signed, verified Meta IN event for a managed resource. MetaWebhookController checks the signature, current association and own-number verification, but never checks identity.managedLifecycle before forwarding the timestamp. MessageAcceptanceService.lockAndValidateCurrentIdentity likewise omits managedLifecycle, while qualifiedOfficialTimestamp checks only direction, origin and date validity. Consequently, a currently associated, verified identity with managedLifecycle=false satisfies the supplied writer code and receives a non-null trusted timestamp. Resolver-side managedLifecycle checks prevent immediate dispatch through that identity, but do not repair the stored provenance; a subsequent transition to managed status could make that previously unqualified timestamp eligible. This is a source-confirmed missing predicate, not a reproduced public exploit. Exploitability depends on the lifecycle state being reachable; the package supplies no invariant excluding it. The affected boundary is trusted-window provenance, rather than cross-tenant access.","suggested_action":"Qualify timestamp persistence using managedLifecycle from the existing locked identity validation boundary. Preserve compatible message acceptance by storing officialInboundAt=null when this qualification fails. Add a signed-webhook/real-PG regression with an unmanaged but currently associated and verified identity: retain the Message, persist no trusted timestamp, and demonstrate that later management activation cannot open the window from that row. Retain the managed positive case and existing malformed/future/duplicate cases, then provide current source-bound regression evidence.","affected_paths":["api-app/src/surfaces/webhooks/meta.controller.ts","api-app/src/domain/inbox/message-acceptance.service.ts","api-app/test/webhooks.e2e-spec.ts"]}]}
```
### implementation-test_quality_audit-r6-result-v1.1.json

SHA256 `8ac37114ee7c8ba04e838012b6531f764cf0128e05e1d86624fedf2b84112844`; byte hash verified against the collection result_sha256.

```json
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-test_quality_audit-r6-dispatch-v1.1.json","review_kind":"test_quality_audit","reviewer_label":"fresh_no_context_tqa_r6","overall_assessment":"mixed: E71 supplies strong source-bound unit, real PostgreSQL/BFF, and fresh-browser evidence; changed tests generally assert durable state, provider counters, negative effects, and race outcomes rather than status alone. The package honestly records mixed fail-first chronology and has no demonstrated pass-the-test shortcut in the current candidate, but one harness fallback can mask missing database statistics and delivery evidence remains incomplete.","recommended_path":"fix the required-statistics fallback and rerun the affected test/audit evidence; then complete the explicitly pending runtime, module, canonical-diff-guard, operator, and final delivery gates before any delivery claim.","performance_position":"mixed","elegance_position":"acceptable","structural_soundness_position":"mixed","operational_fit_position":"mixed","findings":[{"finding_id":"F-035510C8","severity":"high","title":"Required delivery evidence remains pending","rationale":"E71 proves a disposable PostgreSQL/BFF/browser candidate with owned fake providers, not preserved-runtime activation, operator-assisted sends/replies, applied module consolidation, or the required canonical full diff guard. DOD-11 through DOD-13 therefore remain open.","suggested_action":"Do not promote or mark delivery complete; execute the separately authorized remaining gates and record their source/runtime bindings.","category":"operational_fit","formalizable_hint":"no","candidate_rule_level":"none"},{"finding_id":"TQA-R6-01","severity":"medium","title":"Deadlock-statistics helper silently treats a missing row as zero","rationale":"The current deadlock probe uses `rows[0]?.deadlocks ?? 0n`. Although E65/E66 demonstrate that the statistic is available in the observed environment, an absent or malformed `pg_stat_database` result would be interpreted as no deadlocks and could falsely pass the ST05-overlap regression.","suggested_action":"Require one valid statistics row and fail loudly when it is absent or malformed; add a focused regression for that harness failure mode.","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"required-db-statistics-must-not-default-to-zero","affected_paths":["api-app/test/initial-message.e2e-spec.ts"]}]}
```
### implementation-cutover_integrity_audit-r6-result-v1.1.json

SHA256 `454787177a18cbe96e7ac6c77be468c2f4de0796e8c0a6ce903f3cc8f149fa54`; byte hash verified against the collection result_sha256.

```json
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-cutover_integrity_audit-r6-dispatch-v1.1.json","review_kind":"cutover_integrity_audit","reviewer_label":"fresh_no_context_cutover_reviewer_r6","overall_assessment":"conditionally_ready_for_pending_delivery_gates","recommended_path":"preserve_the_current_canonical_cutover_and_complete_the_explicit_delivery_gates","performance_position":"acceptable","elegance_position":"acceptable","structural_soundness_position":"acceptable","operational_fit_position":"mixed","findings":[{"finding_id":"F-035510C8","severity":"high","title":"Final delivery gate remains open","rationale":"The E71 candidate supplies strong disposable PG/BFF/browser and source-bound image evidence, but DOD-13 remains explicitly incomplete: independent delivery assessments, the canonical full diff guard, final review, and closure must not be inferred from candidate GREEN.","suggested_action":"Do not mark the TODO delivered or activate the candidate. Complete and adjudicate the required independent delivery/final guards under their approved boundaries.","category":"residual_risk","formalizable_hint":"partial","candidate_rule_level":"paced"},{"finding_id":"F-91F64098","severity":"medium","title":"Preserved-runtime and assisted operator proof remain pending","rationale":"The package expressly limits E71 to a disposable database and fake provider. DOD-11/DOD-12 still require approved preserved-local activation, additive migration validation in that target, assisted first sends, and recipient replies; no real provider or recipient result is evidenced.","suggested_action":"After the separately approved runtime plan and preflight, obtain the bounded source/runtime attestation and operator-assisted nonofficial and approved-template send/reply evidence without automated contact actions.","category":"operational_fit","formalizable_hint":"no","candidate_rule_level":"none"},{"finding_id":"F-300A50BF","severity":"medium","title":"Canonical documentation consolidation and full diff inspection remain open","rationale":"The module consolidation is only a proposal, and the canonical cross-repository diff guard has not run because its required private-boundary exception is not approved. The current code does not present an unauthorized compatibility bridge, but these governance gates remain necessary before closeout.","suggested_action":"Obtain explicit authority for the bounded diff inspection if still needed, run the canonical guard, then consolidate the approved supersessions into canonical modules and complete the associated consistency review.","category":"adherence","formalizable_hint":"partial","candidate_rule_level":"project"}]}
```

### all-result-e74-v1.1.json

SHA256 `e8c56ed6745b3a1d66f9bf2dde86704a5a58f8d936e1ff763f7e75b0e3386818`

```json
{"checkpoint":"E74 unchanged corrected candidate full canonical GREEN; durable output retained","recorded_at_utc":"2026-10-23T12:20:26.725226+00:00","command":"bash scripts/test-channels-local.sh all","executor_session_id":66605,"exit_code":0,"actual_exit_code":0,"terminal_authority":"Owning executor reported actual terminal/cleanup; root independently parsed retained stdout aggregates, matched all259source bytes and93current per-run browser records.","phases":{"migrations":28,"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"duration_seconds":4.39},"api_postgresql":{"files":33,"tests":456,"duration_seconds":309.13},"web_unit":{"files":7,"tests":54,"duration_seconds":0.927},"browser":{"tests":89,"passed":89,"duration_minutes":16.2}},"stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","source_recheck":"all-source-recheck-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","full259source_postseal":true,"freshness":"browser-freshness-collection-e74-v1.1.json","owned_cleanup_observed":true,"repeat_rationale":"E73 passed967 with source/freshness checked, but raw stdout vanished before PCV extraction. Exact source unchanged. This justified repeat retains current complete metrics; no code/test rewrite.","limits":["Synthetic provider/DB/BFF/browser only.","Fresh complete independent r7 review, images, module consolidation, private-boundary full-diff exception, preserved runtime/operator and final gates remain."]}
```

### all-source-seal-e74-v1.1.json

SHA256 `40ad3c8844a20d2d688269ac60f0b2648460bb3c26d6e6bf2fe912fcd5694d4c`

```json
{"checkpoint":"E74 unchanged corrected candidate, repeat only to retain lost actual stdout/current metrics","capture_stage":"Before actual runner, no result inferred","captured_at_utc":"2026-10-23T05:22:26.589721+00:00","owner":"root independent public source collector","command_planned":"bash scripts/test-channels-local.sh all","synthetic_stdout_planned":"/tmp/stcon04-executor-all-e73.txt","fresh_git_identity":{"root":"80e3940126f22a941f90dba4f5e801b6c0eb2f58\nHEAD -> feature/number-onboarding","api":"db5a86758a165fac8a1ab587599c37b17890530c\nHEAD -> feature/number-onboarding","web":"74b9d4b714044829796f875d00553f077c1c329d\nHEAD -> feature/number-onboarding","foundation":"34236ecf498fe3d8f62e168b7ece570327ad3ebc\nHEAD -> main, origin/main, origin/HEAD"},"positive_public_roots":["api-app/src","api-app/test","api-app/prisma","web-app/src","web-app/e2e"],"exact_public_files":[".github/workflows/ci.yml","api-app/package.json","api-app/package-lock.json","scripts/check-channels-ci-parity.py","scripts/test-channels-local.sh","web-app/package.json","web-app/package-lock.json"],"count":259,"fingerprint_algorithm":"SHA256 canonical JSON sorted keys compact separators of sorted path+sha256 records","fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","records":[{"path":".github/workflows/ci.yml","sha256":"16acaf6d4b807a806a50a31c75715b14e8b2e220e0e17e2bac43ec4b740318e5"},{"path":"api-app/package-lock.json","sha256":"d1e45274c4b10d134469d7ec63e88777ec26b917d48197a03a4b97cefda047c7"},{"path":"api-app/package.json","sha256":"df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d"},{"path":"api-app/prisma/migrations/20260818125556_nucleo_v1_tenancy_identidade_atendimento/migration.sql","sha256":"680ff78cf5c8dab2bc5ec51688b83252bb86d214e8af7817356ee125ed47daa4"},{"path":"api-app/prisma/migrations/20260821175101_modulos_e_marca_por_mantenedora/migration.sql","sha256":"fe2155893de7a9ade15493617e36e77e299bcffc9b86ec19ad813a15bfd1c6bc"},{"path":"api-app/prisma/migrations/20260821180000_tres_papeis_owner_admin_atendente/migration.sql","sha256":"ecf379d151e2f73ff1b81baef00c27561b2b9f1acc885599144603541987b7f7"},{"path":"api-app/prisma/migrations/20260821190000_setor_e_proveniencia_do_grant/migration.sql","sha256":"968394573271ce426d3011db774ce9a219750dc5822f251fdea291e588d12d59"},{"path":"api-app/prisma/migrations/20260821190500_concessao_de_setor_e_fato_proprio/migration.sql","sha256":"176c7664c7c1458f0e06beb33f21359db72511e6cd20f1da5fb63b7eec50cdbf"},{"path":"api-app/prisma/migrations/20260821200000_historico_de_atividades/migration.sql","sha256":"3a87e44c2cc8a3a7f91fc59819bae065e9a1f1eeacfc28685710e8d5d7e18a75"},{"path":"api-app/prisma/migrations/20260821210000_wizard_de_onboarding/migration.sql","sha256":"013d4428d36afe752966762ae8a2d6195032d88c57ab9d18b2c147df21865735"},{"path":"api-app/prisma/migrations/20260821220000_preserva_modulo_ja_em_uso/migration.sql","sha256":"a33a51234e7097f95e10452c3652b33e9e5c5c1b488a4545404222711d5abec5"},{"path":"api-app/prisma/migrations/20260824122559_perfil_do_proprio_usuario/migration.sql","sha256":"5f14615eef62afaa05be2f6e1a144667c30e4c2f618f899ade8c108c7ae9a80e"},{"path":"api-app/prisma/migrations/20260824125224_arquivos_logo_e_avatar/migration.sql","sha256":"4a8bb54855ff5de7c89632df84f92c5589ffd99cd9e8c5001a080d01f7c121d1"},{"path":"api-app/prisma/migrations/20260824125227_arquivos_dono/migration.sql","sha256":"864ced863cd894f7df333f16a6eaafe0870d72f263c18600b7cf4985e5c8120a"},{"path":"api-app/prisma/migrations/20260824125334_avatar_e_do_usuario_nao_da_bu/migration.sql","sha256":"297f051ce252e4e6abc6b7dde2ded19a126c5db074e74c29b937ef7787f0cfa8"},{"path":"api-app/prisma/migrations/20260824161138_convite_e_recuperacao_de_senha/migration.sql","sha256":"a46e62f79cd2e0f4d818bada129caf89f800fc372d963da4bbac6b9e597229c3"},{"path":"api-app/prisma/migrations/20260827170000_cor_secundaria/migration.sql","sha256":"01d41f5e3772b4278b41511b2a7efbb39bd76a62e31f67b2a4967de4e6357380"},{"path":"api-app/prisma/migrations/20260831130000_cores_primarias_por_tema/migration.sql","sha256":"03cecfbf50ed896fed322d63dbb1fea40126685b9193d08e677a4e598c5b4e30"},{"path":"api-app/prisma/migrations/20260901120000_typebot_bots_and_triggers/migration.sql","sha256":"62188240b4f2f7db65a3f2e8d45cf866b5c22311225782a669bf6389d517a8a9"},{"path":"api-app/prisma/migrations/20260901130000_typebot_sessions/migration.sql","sha256":"47fa9f58f4b89cf038eda3cf54cd576d3ab4cd3b2e54be1f7474c94a2f43f795"},{"path":"api-app/prisma/migrations/20261015120000_number_onboarding_foundation/migration.sql","sha256":"55d84f5eef1b9b9e9a22891695812e522fe4e405041341218984507426ef0946"},{"path":"api-app/prisma/migrations/20261015130000_number_onboarding_provider_resource_ownership_immutable/migration.sql","sha256":"a6fa9ad9e99a0b55ed5d9e86b99d42b603b404c13f41f97ac718e6443f29a3fe"},{"path":"api-app/prisma/migrations/20261015140000_number_onboarding_channel_operation_fence/migration.sql","sha256":"e484edd01e78133bcaf23f12fb47e44e92cba44a89b29803eff1530b103bc496"},{"path":"api-app/prisma/migrations/20261015150000_number_onboarding_managed_cleanup/migration.sql","sha256":"27a07435e3327f004ad8d46cd4c18eec57b89ce3cdbf51c39631b248555214ad"},{"path":"api-app/prisma/migrations/20261016160000_number_onboarding_current_channel_identity_index/migration.sql","sha256":"aadefab2ce66f3484661e66fdf918f5e295926bf9b89b0af4c3e2c8c5c78b740"},{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","sha256":"586e709e07736eca0908ab5dcc668cf0e0b317189b4c963b361399848a3c9710"},{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","sha256":"3feab40fed1c9be1bac9e43464fd587d57693424c4b3012d8c4b8536661d51dd"},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","sha256":"2822bff860b5aa3476e7614f6a5d5515520dfd8e40708767d1bc4c5bfe2d991d"},{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","sha256":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437"},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","sha256":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a"},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","sha256":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544"},{"path":"api-app/prisma/migrations/migration_lock.toml","sha256":"bc487c02c71ad9cae8694647129e3ea7f32b1fe7007d0a6ced064e51022cd3fb"},{"path":"api-app/prisma/schema.prisma","sha256":"19ea60e6e5a1675a4ff12581237b2f91c2359b61d7b8bcb9e8bf1c1ebf26435d"},{"path":"api-app/src/app.module.ts","sha256":"a59880adc1bd8250fdbf5d52637fc38fe3177a2615e1b25389716946da7ad420"},{"path":"api-app/src/domain/access/access.service.ts","sha256":"2ef3761a138d7c8c386c5ddb4bf2a2000c960328789834bde5e12135a1ea66e7"},{"path":"api-app/src/domain/access/require-role.ts","sha256":"1281da1ad31748e2bd78bffdf2962376d3413c7b37cfe6102448710cc7d7ce61"},{"path":"api-app/src/domain/access/role.spec.ts","sha256":"7d5400e3af84896ba021aa220908ad7ac995f2f0af1405cf53c72f5ef7a6a8d8"},{"path":"api-app/src/domain/access/role.ts","sha256":"ec92764e75c52b754e430355d196137ca90de89b4c5ed6f3fb49a05da10e1b42"},{"path":"api-app/src/domain/access/scope.spec.ts","sha256":"e3386d1e27d27c38ebbf8f3c06222c50c0cd5d164c29437ec83fcafbf14919c3"},{"path":"api-app/src/domain/access/scope.ts","sha256":"412f68eb157328855c87cb86b6b89cc1c267eee7068dc59c0abbe085074db26d"},{"path":"api-app/src/domain/acesso/convites.service.ts","sha256":"089931bcf9acd7b3807364e9b7eefbbbcfa14c41e649a3f87e74ca81cb83d211"},{"path":"api-app/src/domain/acesso/limite-de-recuperacao.service.ts","sha256":"9661ebd71ab182f177743295bd15d1e857970025587c7a8c8566c9c43532ae16"},{"path":"api-app/src/domain/acesso/tokens.service.ts","sha256":"00f5f240ba10ad2a0178e4c583ac4e6f04fb07b8a3fc7e55c58ab5ce6702c180"},{"path":"api-app/src/domain/channels/channel-credential-crypto.spec.ts","sha256":"eda02a1bf69f40eb07309184adad8d2f1862f563c33afa03fb1657991d29faf1"},{"path":"api-app/src/domain/channels/channel-credential-crypto.ts","sha256":"4a438a1e73903c011d212962f41b38dfb2a999c539112b6831156664de6d9ef4"},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","sha256":"a60d142fcc335de43c5a697d9f7758f722883a1725c824dd0a4b4f0a2f7fb03b"},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","sha256":"7782792bb945701cc6f6d0ac1460d0504356fa8d73a4261f37112f7c892a23ac"},{"path":"api-app/src/domain/channels/channels.service.ts","sha256":"e910b2b395abc0ebca74deea917cf107dd36eca58491f1b0893efb702e1dfcf5"},{"path":"api-app/src/domain/channels/number-registration.service.ts","sha256":"be53f7f1feb00c0bacb36ce0cf5d60915bb398ed011f69d28d3d4987f83417dc"},{"path":"api-app/src/domain/channels/receipt-attempt-convergence.ts","sha256":"ca8cb841fab2574866c3508ab41aa0a269608a20658db18840b2b89f0c281512"},{"path":"api-app/src/domain/channels/safe-redaction.spec.ts","sha256":"b35f2c689ee22cf0f8ebe50b4979ca7e25a708e0bd6930c93c376fbf57a3ff6a"},{"path":"api-app/src/domain/channels/safe-redaction.ts","sha256":"704539c0a9aabd17dd5fc19826f5079da816c2bc5e22d438b8672662b9998606"},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","sha256":"f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3"},{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},{"path":"api-app/src/domain/channels/transport/channel.ts","sha256":"49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9"},{"path":"api-app/src/domain/historico/atividades.service.ts","sha256":"9a081318375268d76839a83502d194bb12bfc1fb619a3cb6badab80c425d4609"},{"path":"api-app/src/domain/historico/catalogo.ts","sha256":"7cc5d9b1a76019b99161334ca05cb899be961c73192cf0d47437763b1837823f"},{"path":"api-app/src/domain/historico/cobertura.ts","sha256":"8f8208f0a22a9ea78d5d244e1a4eafd78ff04138e1c0ff25b8c66856f0db64e5"},{"path":"api-app/src/domain/historico/registro.service.ts","sha256":"3826c4b841af898c4824fc53b64249f17f929157ac60769fb72336574d5d9c32"},{"path":"api-app/src/domain/identity/identity.service.ts","sha256":"e839d6be1e2f1a5e1db681e742c31f5de0efb3a224cb1013ae81a21e8caf8e3a"},{"path":"api-app/src/domain/identity/login-attempt.service.ts","sha256":"979b1c873319d3d8142e4aeb13c71f502c332c7dda862c0ae758948e763d34fa"},{"path":"api-app/src/domain/identity/password.service.spec.ts","sha256":"3ec4ae1217e76e8191fb713f762c2041e588e1e88bbfb2dd0ef913a9a58289f1"},{"path":"api-app/src/domain/identity/password.service.ts","sha256":"6aecadaf5295c909d8f399b38d78c72b5aed90b72a0aea68fe39a648bf371d0e"},{"path":"api-app/src/domain/identity/usuarios.service.ts","sha256":"ff82f54a7aa6e495c5ce20626e88221fc20f4474a5ec84ff2f257b081f803364"},{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","sha256":"e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"},{"path":"api-app/src/domain/inbox/channel-window-policy.ts","sha256":"46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e"},{"path":"api-app/src/domain/inbox/conversation-start.service.spec.ts","sha256":"e72060157628dbd2c27d27bc2c55d3d2a2f40d6f56ba344c97c97e69b80d0fc2"},{"path":"api-app/src/domain/inbox/conversation-start.service.ts","sha256":"97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118"},{"path":"api-app/src/domain/inbox/conversations.service.ts","sha256":"6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.spec.ts","sha256":"687345771d8394ef8317142f38736876e730fc28cfdddd974a0fdd363fa7b78d"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"},{"path":"api-app/src/domain/inbox/historico.service.spec.ts","sha256":"eb1ca83e588c58382a332aee0fdda200f3eb6cb5f8c0cbd430e9790623393ec0"},{"path":"api-app/src/domain/inbox/historico.service.ts","sha256":"811212eeb5b9e8318ef344eb6660385382707cb6d6882c5e9f84e8d4951ccfaa"},{"path":"api-app/src/domain/inbox/incoming.service.ts","sha256":"390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b"},{"path":"api-app/src/domain/inbox/incoming.typebot.integration.spec.ts","sha256":"7b0e7d75fc5809b8c950896818779402fe2bf32ef37a94d970fe081240562975"},{"path":"api-app/src/domain/inbox/incoming.typebot.spec.ts","sha256":"faedadd6fdf05bf445b846e89dd17c608b0cc3599e3463c89f6338f6febad72f"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","sha256":"c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","sha256":"a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"},{"path":"api-app/src/domain/inbox/initial-message.service.spec.ts","sha256":"e472bc1048f1c24c8edbe3004baceb15cc5a78956653bb2e30ade45843e2ee92"},{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/domain/inbox/message-acceptance.service.spec.ts","sha256":"f6561e2e2dce670f94ce95510f97da0680249ff2484b0c1098d5e6a3b1232ee6"},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/src/domain/inbox/outbound.service.spec.ts","sha256":"748be057ff4b3cfe1215b87108d7708ca02ed97d7a7d129d9cada5fc1aef8d81"},{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f"},{"path":"api-app/src/domain/inbox/timeline-pagination.spec.ts","sha256":"a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d"},{"path":"api-app/src/domain/inbox/timeline-pagination.ts","sha256":"d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af"},{"path":"api-app/src/domain/integration/api-key.service.spec.ts","sha256":"41ef8944d57caec1a6db7bc7c0c05c9e4936a7cb5992bf45f26ecd646df3c976"},{"path":"api-app/src/domain/integration/api-key.service.ts","sha256":"bde94ae81c4a17c4cf6cb8b28d8e9d2cdb22feb1def06848f6f125e8018917c5"},{"path":"api-app/src/domain/integration/outbound-webhook.service.ts","sha256":"fdc13f9aadcc8f0e9c566643b7da08cf7cb0aec63c821ef98025e4f2a3baee1b"},{"path":"api-app/src/domain/integration/rate-limit.service.spec.ts","sha256":"88e910431be104406fb84c375ddc83153755a9d7b4a81a9c098b0b7cfd2cbb12"},{"path":"api-app/src/domain/integration/rate-limit.service.ts","sha256":"0579e073c05f57f9a87cf0f96f0301d01661957bea2490140c1e63566686503f"},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","sha256":"9a60549d1c79d73889fd2d47b7ea3bb25b8a0bf140da805f64216decc6ff9d97"},{"path":"api-app/src/domain/message-templates/template-definition.ts","sha256":"1f28bfd19454b1e187b854c4f2e9785b59e7726032c20f82d62460d87401203c"},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","sha256":"429a078fb48d5a66601d83883275dcc12cea659692e463e94a17d41d5cdf0713"},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","sha256":"a03a567e5b96a348b4ab40bb18282a555d30ad3533e6efb929c5d2f2614c82b2"},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","sha256":"ddf581459b66bf0eb26ec710ded050f45713e5dd5317066cea574dacf57a68bc"},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","sha256":"c7ed169d87a4224f82f8d1abe109bfa02b913bb2cb63303fc6477673f45ed693"},{"path":"api-app/src/domain/message-templates/template-observation.service.ts","sha256":"41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488"},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","sha256":"a2b8b33ecfb0af165c2b94b50703d18a364d5b64ef581bbdd7659325bc631709"},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","sha256":"ea3e0550ad5c82b263391dbfb3dae6b9e8656d219f18aa0d7c55cd5668722123"},{"path":"api-app/src/domain/painel/painel.service.ts","sha256":"d916a08d748336f2f17af8204504707c49db7396642c2c79067a6f71be68609d"},{"path":"api-app/src/domain/produto/modulos.service.ts","sha256":"1283ac1879467c3ebb079daaf29bfd5cda9f0ca02fd45a1b3f8ec865c7d5544e"},{"path":"api-app/src/domain/produto/onboarding.service.ts","sha256":"3b643a474a51b4ef0050f520d5059067897572843317e4a632cf0e37a6228c5e"},{"path":"api-app/src/domain/setor/setor.service.ts","sha256":"d8cb22d68452d1ab9ea9daa69fe9660d867612f81db8e9e9a7fb34a6e56cda84"},{"path":"api-app/src/domain/tenancy/tenancy.service.ts","sha256":"c9348f86f1f2bcfd4af3f9bd3e91cb5218d81cf13098989b5f6ea64acbb41398"},{"path":"api-app/src/health/health.controller.ts","sha256":"92bdd3eeecdd69ed564e7089a910e6d6d667e55e3f6f3965898911e575b98b20"},{"path":"api-app/src/health/health.module.ts","sha256":"9ce204c0535a897d545388170bcb6e308716d70a16074fbe94330787c8a95489"},{"path":"api-app/src/infra/arquivos/armazenamento.ts","sha256":"de7a13259b03599c709b9c0097a4ddc84d07990f1a48ceb7f2aca86a826416a6"},{"path":"api-app/src/infra/config/modulos.spec.ts","sha256":"57d60337ce3564e071b019e127ab6d409759eea8ae77e2d45095e4fea877928e"},{"path":"api-app/src/infra/config/modulos.ts","sha256":"fd1ccabf7bee088f230a12d773c56a5d41fc07642d04262b55a6497a7b9c2a03"},{"path":"api-app/src/infra/http/body-parsers.ts","sha256":"0f65f24e300b2204362fff3ee1c799a35baecb1c57d141fe0ac0957091a5e624"},{"path":"api-app/src/infra/http/origens.ts","sha256":"db66c02e2ce21f725d445e6c4137a1d8462ffd85827a1cf4a211850e502c79b8"},{"path":"api-app/src/infra/prisma/banco-atrasado.filter.ts","sha256":"e4329ef4ccc2b91596afe82137286dbb7328f64ceec786440f28c7b8e45b0eba"},{"path":"api-app/src/infra/prisma/migracoes.ts","sha256":"d416bab2e0c7cdaef7313b92195a1d58b18ac665afb86d3b1e05ffad0bd7ae62"},{"path":"api-app/src/infra/prisma/prisma.module.ts","sha256":"14d19dcd7848e4d134cd9eaa205818d5e0302123a5fc5ea2440d358a39f2fd25"},{"path":"api-app/src/infra/prisma/prisma.service.ts","sha256":"8c6034455186bfc6497b329f94af7c867fb6f28b9226d54db5716a907db6e200"},{"path":"api-app/src/infra/session/session.service.spec.ts","sha256":"dbb215e931a5856269b07057ce74c7af7ee66c4947961fbf1a01f903f3c7f4fb"},{"path":"api-app/src/infra/session/session.service.ts","sha256":"884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200"},{"path":"api-app/src/integrations/channels/account-reference.ts","sha256":"da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24"},{"path":"api-app/src/integrations/channels/channel-adapter-factory.ts","sha256":"e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc"},{"path":"api-app/src/integrations/channels/channel-adapter-registry.ts","sha256":"655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b"},{"path":"api-app/src/integrations/channels/channel-transport.module.ts","sha256":"4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d"},{"path":"api-app/src/integrations/channels/evolution-channel.ts","sha256":"6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34"},{"path":"api-app/src/integrations/channels/meta-channel.ts","sha256":"99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26"},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","sha256":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943"},{"path":"api-app/src/integrations/email/email.client.spec.ts","sha256":"ea88b5a7243aec296b461ffe612b41ba40f141b8608e81e071f605ee659ce2c5"},{"path":"api-app/src/integrations/email/email.client.ts","sha256":"95d89c14c2022a0ff9ea87e2acc173f319abfe766875156999cd55e347dc934a"},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","sha256":"119d962fdcd9c895b75845dca74d8506147e11480d74b82e8c37f29f97c04081"},{"path":"api-app/src/integrations/evolution/evolution.client.ts","sha256":"b0824e8fd4f801a239521855aaa02da5e0943a8c86c4ac8778e2f1f352821698"},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","sha256":"aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd"},{"path":"api-app/src/integrations/message-templates/template-management.resolver.ts","sha256":"1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00"},{"path":"api-app/src/integrations/meta/initial-message.client.spec.ts","sha256":"0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057"},{"path":"api-app/src/integrations/meta/initial-message.client.ts","sha256":"e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","sha256":"6b42b44577e2c06ae73fb0525dac10b99f7364a04e2c04184dc303c6d47872b8"},{"path":"api-app/src/integrations/meta/message-template.client.ts","sha256":"8dff223f7a97632cf228800cdbbb12ce6f5b151efc5fa30411d03e5ec3280cb5"},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","sha256":"d7e76f5c392afab1638363d3c851f8ce8c5223ff27c64801a79fdc8ec00d5e7a"},{"path":"api-app/src/integrations/meta/meta.client.ts","sha256":"9f954f6c1c2bd10030f5eed0cb42e493d6e480106bcfc3f44977cb97a716d34f"},{"path":"api-app/src/integrations/typebot/typebot.client.spec.ts","sha256":"1d78eaa3e63fa27550be7a74bb59dca841bb738db46ced76cd41136648231e74"},{"path":"api-app/src/integrations/typebot/typebot.client.ts","sha256":"fe5c461b56d9c363953ba301129b3e78b0f3f408c510e0ac03ce8ec2c96ab873"},{"path":"api-app/src/main.spec.ts","sha256":"082a0836f57481e22d2c2dd655f65cca40d008016561e49543b82b8e3430dc5b"},{"path":"api-app/src/main.ts","sha256":"05ff096cdcf67a8a153736264ed46a7faf9f5c0f45325c2d3fed95188fb2b1ad"},{"path":"api-app/src/realtime/realtime.module.ts","sha256":"c8ed324d8e8861fe9b97538161639aedade82420a55d53bb25b9d27441029139"},{"path":"api-app/src/realtime/realtime.service.ts","sha256":"69d43aa7b694fa744819823f7e24071c250b390ad54d09446b2f2c797a7f3829"},{"path":"api-app/src/rotinas/agendador.service.ts","sha256":"b639a996ce541ace79c139cd525229367f198dac2aa769ba0dfa8b0194dcbec2"},{"path":"api-app/src/rotinas/expurgo-de-webhook.rotina.ts","sha256":"b0cac2efff44dc5f3b652f0a3f384c9e8cf4801f31319442b13454963b2951a6"},{"path":"api-app/src/rotinas/rotina-periodica.ts","sha256":"71a72d85b993a99c317a962f3b3477129cf265ac3ec54c9f092c3c704d3dc06c"},{"path":"api-app/src/rotinas/rotinas.module.ts","sha256":"44c7a4949922e7194fc0584381c0d7606517a05ae5179274a50e1cb1b59fac44"},{"path":"api-app/src/surfaces/bff/arquivos.controller.ts","sha256":"4c5119ee8aa8c77cffa72b5ac0d0b4a98db872c8784dfc037fa5937a32210d65"},{"path":"api-app/src/surfaces/bff/atividades.controller.ts","sha256":"71b8f699c7ff2a0884d4f4e6c999470769ee8d21e123e86b181c985f84f86b3c"},{"path":"api-app/src/surfaces/bff/auth.controller.ts","sha256":"1cd884fe1a716d82b67ffbcc1a4c6cbcf237a30111a6bd0a2a92c48ad7d32381"},{"path":"api-app/src/surfaces/bff/bff.module.ts","sha256":"8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a"},{"path":"api-app/src/surfaces/bff/channels.controller.ts","sha256":"c7a3917c84ac1921b757fd7bca5a9b0b29ab2078312fcf2fd421104ef41a6182"},{"path":"api-app/src/surfaces/bff/conversations.controller.ts","sha256":"0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3"},{"path":"api-app/src/surfaces/bff/historico.controller.ts","sha256":"3bab5868bfabde5d37be8b4d2579c8dc417307904d53c743c8a7ce522526b84a"},{"path":"api-app/src/surfaces/bff/integracao.controller.ts","sha256":"d060c6fec31f188950193a163ddf7093f9613c65e0e8d27ca597b09c2b6c2bdb"},{"path":"api-app/src/surfaces/bff/integracao.typebot.spec.ts","sha256":"38cf0dd1746b00e6d7ec110e549fe29fad24e9fd8f4554465877f756a242af6b"},{"path":"api-app/src/surfaces/bff/me.controller.ts","sha256":"0edd826d4e9a3c0b8cde4334bf2e88f360f5f5e9d5db99e5dfc4382b5bf71bb0"},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","sha256":"0e0449a80852a4513f626d0df7b1a5bb17b034eeceb50f53842fb91454ff4491"},{"path":"api-app/src/surfaces/bff/number-registrations.controller.ts","sha256":"c57797667ff26a4ea74aa939e4972a8cd8f442c9beafa166b1bdf808e19c236e"},{"path":"api-app/src/surfaces/bff/onboarding.controller.ts","sha256":"beb15af03cdeec8a5202ec0dff529c41fb991b4b874bd10ee3e4cd684c478240"},{"path":"api-app/src/surfaces/bff/painel.controller.ts","sha256":"3894286559507f9fcae0ddedf3f66cdd879e4871d4a5f835855aa4a33458fa3d"},{"path":"api-app/src/surfaces/bff/session.middleware.ts","sha256":"80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211"},{"path":"api-app/src/surfaces/bff/setores.controller.ts","sha256":"b94cdefcf0c28accd0c0fdf9088ba695bb10a7bd434d6732bab9bd32c71d0558"},{"path":"api-app/src/surfaces/bff/usuarios.controller.ts","sha256":"09a4125968a55021ecb9942d1466fbc80ff61fc71f69995dc231c814ce7cb846"},{"path":"api-app/src/surfaces/internal/internal.module.ts","sha256":"6fbb35d40890862af9cfdc1b8b87f7ebd2b2e8d0e256f454f68a1053eef34f04"},{"path":"api-app/src/surfaces/internal/mantenedoras.controller.ts","sha256":"35359bd6185a43ca148fba1dfb7edc048f25d7890e377602c8f2222d78924c77"},{"path":"api-app/src/surfaces/internal/service-credential.middleware.ts","sha256":"b2db1b715a65995d8a21b3da296de93930292cc6bd23f72b4cba24d6cdfe093b"},{"path":"api-app/src/surfaces/public/api-key.middleware.ts","sha256":"f76cd8854c8145c4b456e8c9d2d1ab000c17bc5278af76997745b5696edd9877"},{"path":"api-app/src/surfaces/public/conversations.controller.ts","sha256":"bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1"},{"path":"api-app/src/surfaces/public/public.module.ts","sha256":"00a96d54fde7061f61f4ddf2b9cef836a02ad77ca29b62ea422695b9d8f90ef8"},{"path":"api-app/src/surfaces/webhooks/evolution.controller.ts","sha256":"12139a5b50b4dacf43492e038c91f006c9db999d0f6a76fd5d73e45ee987a041"},{"path":"api-app/src/surfaces/webhooks/meta.controller.ts","sha256":"261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f"},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","sha256":"abc8fd7960fcca1ce43d21d44a90f8d4708d47e07bde9a48c0009e02dc0503a6"},{"path":"api-app/test/api-publica.e2e-spec.ts","sha256":"2aaa1d0a83ef75a6c757ca7389bd3a7afa1c9096711dc117b6f549b8d72a9510"},{"path":"api-app/test/arquivos.e2e-spec.ts","sha256":"892a39c0749d190e867a154e345f6f8f7b0b196534fdb7d87578c0f4577bf3ed"},{"path":"api-app/test/atendimento.e2e-spec.ts","sha256":"45262ea86ced88b7fc4550f7364b6d04d2fccd5930223e30090207377ad05a9b"},{"path":"api-app/test/banco-atrasado.e2e-spec.ts","sha256":"49c6aad018109cba22ab46352823197d2fd4fddae3a72f36386d8e63844aec45"},{"path":"api-app/test/browser-server.cjs","sha256":"02354237e3c0c5f8d918f65cbb833270e2ce02469cfe3e926e3a6790abc106dc"},{"path":"api-app/test/canais.e2e-spec.ts","sha256":"a0a09f0cf84ce5883bbc51a0e448e85f644354dc6a44a519b780a877ac9e7551"},{"path":"api-app/test/channel-transport.e2e-spec.ts","sha256":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"},{"path":"api-app/test/cobertura-do-catalogo.e2e-spec.ts","sha256":"74bc6f01986dbc895a9fbc2add01f2403d896b0ecbd3633bb676ebab9ef59080"},{"path":"api-app/test/conversation-start.e2e-spec.ts","sha256":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"},{"path":"api-app/test/convites.e2e-spec.ts","sha256":"cab83877449c2bc9e2cafaf2f825b783063b4992ee09c68063838c4332d70031"},{"path":"api-app/test/cross-tenant.e2e-spec.ts","sha256":"681cb81ceaefe9974ff8051f42196cbd68f60f25f200679d25b402f392f1a170"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"},{"path":"api-app/test/helpers.ts","sha256":"117e4f85c81dda37ab30e7eb23704b31538c8c5161aa7562a844eaf11de6819c"},{"path":"api-app/test/historico-atividades.e2e-spec.ts","sha256":"cf91005abba689fa6b1227a65e2453a590fb0c687d647b802abe9f24fa761333"},{"path":"api-app/test/historico.e2e-spec.ts","sha256":"edbe852f763861aee8e3a12b29c949336e05461b9df1ca52ce06e0a0a56b10ff"},{"path":"api-app/test/identidade.e2e-spec.ts","sha256":"691b89858fb34bb2bbc97465895f61abcc43bb02c5200a9b74b74334201da1f6"},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"},{"path":"api-app/test/message-template-bff.e2e-spec.ts","sha256":"e0212463856dace44908e3762aa206d1ed86deeb95ebbdc926a354d1518902e4"},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","sha256":"1a7367fc0a97fb9f727276b38186cddb796fc965ce4a9ec9e1078603670f2996"},{"path":"api-app/test/message-template-management.e2e-spec.ts","sha256":"788fe852c821c62533f560eaa14057789ebb5d2e1ed8fb57affa74b5f7e31d1a"},{"path":"api-app/test/modulos.e2e-spec.ts","sha256":"2a6b2540dcbb2e1de61d3d03e444ec201c2ed740646255c00166d4af7ed17ee4"},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","sha256":"779ad4f9f201ef366cd66c2692098957290a15857179d2a5b249415aef1c7bbd"},{"path":"api-app/test/number-onboarding-caller-scoping.e2e-spec.ts","sha256":"1adb1663295c551da9134729c09d6101c690d717da99a84cd543304bb47738fc"},{"path":"api-app/test/number-onboarding-flow.e2e-spec.ts","sha256":"650b233c9dafd9730f14170ce6bd6961d6277b9a131a6eb816cb8edd39341fae"},{"path":"api-app/test/number-onboarding-message-acceptance.e2e-spec.ts","sha256":"c8b29c16412938b64fb8e2555729f0777d9e3eb69a57d29df3d65b56443c4bac"},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","sha256":"3825b0286f9906781e83666616caa05417647ee47c022763fc76e39a3c4ddca0"},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","sha256":"7526f755280fa99adb9cb91dd5062810f239c0e7d4e047af3bdb91444433c74d"},{"path":"api-app/test/onboarding.e2e-spec.ts","sha256":"fad7b377724d903c5c3faccba6eb81e1881da4fb59744b9a686a85cca68d4d24"},{"path":"api-app/test/painel.e2e-spec.ts","sha256":"c2e030984418012d6c74a35ff0440b7d463bfe6df42d088d7087ec09985ecbbb"},{"path":"api-app/test/realtime.e2e-spec.ts","sha256":"cf9335f7bfefecf708d69ab966533bf3b65ed7cc5615533691f7f2a841275422"},{"path":"api-app/test/rotinas.e2e-spec.ts","sha256":"b86f5a13a3946a3ea12a06ec0b20b9c05075bd3fb5b69249cda76e5082313c9b"},{"path":"api-app/test/setores.e2e-spec.ts","sha256":"e45b7ab64ee06975afc07232fac788a73b9a6d66ffb60cd42ea6824b450247ec"},{"path":"api-app/test/setup-env.ts","sha256":"bfb97c57f39e252868b544437c6bf3128efa70613e5a7765d0aefb52f5b6a849"},{"path":"api-app/test/surfaces.e2e-spec.ts","sha256":"5b90e539e15859990f9aead1ad1307f8cf3683f92c8d65e73d465f8fd2ab2c22"},{"path":"api-app/test/timeline-fixtures.cjs","sha256":"a8239426ffb80dd430d38fe9f3dfc29d5ad346f77f519320be25e37c1f853d81"},{"path":"api-app/test/usuarios.e2e-spec.ts","sha256":"a16677d4cc7669057c4ba07aa114505dabf995d8b5d28fa7e0b39f46e8167a34"},{"path":"api-app/test/webhooks.e2e-spec.ts","sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"},{"path":"scripts/check-channels-ci-parity.py","sha256":"d838d557177bf47423a063dfb0cb12b6cdf1e319986c4340286ada097742ce13"},{"path":"scripts/test-channels-local.sh","sha256":"de580538f3257a85448cb3ce5030c85b90f65507da53737e4491fdf543091e42"},{"path":"web-app/e2e/channel-transport.spec.ts","sha256":"6960a14dbd30f317253ae577196bc62c252c0446b5c75885b82d08f1753b3542"},{"path":"web-app/e2e/message-templates.spec.ts","sha256":"95b6c55145dbd40b8aff0e59484781bf1450eb3f174b1f7ce2ee7dbf9474d68f"},{"path":"web-app/e2e/number-onboarding-freshness.ts","sha256":"880b49f8fa428568692b92a883dd00c5ce76214b1f2db5b35cafb9b0553ed9ad"},{"path":"web-app/e2e/number-onboarding.spec.ts","sha256":"47fdb27c0b592dfe8df31b8ad1be219d96720abdc00660bc15f6b2c03096f31b"},{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"},{"path":"web-app/e2e/telas.spec.ts","sha256":"ee4911de7148eebee35d5ddcc7d9bbbcc6faf051f0ea3f415e338d6809bb9d59"},{"path":"web-app/e2e/timeline-freshness.ts","sha256":"3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53"},{"path":"web-app/e2e/timeline.spec.ts","sha256":"36e51ccf9df361ff0f6704660cdf3fe86b821b4845e264a649c9d2583e0e1e4e"},{"path":"web-app/package-lock.json","sha256":"546aec97be8273cf195a16b75c0127474ea3a5042668f8d4c93aab96c1619c8f"},{"path":"web-app/package.json","sha256":"fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de"},{"path":"web-app/src/App.tsx","sha256":"2d9f3b3d03658a8d6d6132986346f3be8f36a2582faca29285b3d46c9920307e"},{"path":"web-app/src/EnvioDeImagem.tsx","sha256":"23dabf408b9a42f823b645f5cff7f4381a24088c387b4c2b276181cd8626c0d8"},{"path":"web-app/src/Erro.tsx","sha256":"72920e0bccd28660e93413d9c422b47c222f2fcfa27d69535dcd609b9b203c0c"},{"path":"web-app/src/api.spec.ts","sha256":"9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9"},{"path":"web-app/src/api.ts","sha256":"7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c"},{"path":"web-app/src/cadastroNumero.lifecycle.spec.ts","sha256":"a340c48e30c712cafecb1d35fe20bd3841c46e2dfbda21645fc8ef3ed6977834"},{"path":"web-app/src/cadastroNumero.lifecycle.ts","sha256":"5c60a8fc7456c82a7d782b3484ba447bda826e65bf93a9175a991dc50be254a3"},{"path":"web-app/src/cadastroNumero.spec.ts","sha256":"9c2581c1886d108c4c153d485fd77f017805c2e3b813a9536d21d0296f2a1ecb"},{"path":"web-app/src/cadastroNumero.ts","sha256":"584401ed8ab1ce1d53950998e85765a35d55d7ac4961286924f98e4132edcb6b"},{"path":"web-app/src/componentes/CadastroNumero.tsx","sha256":"9afbe4f419dcf4b5133f8103a0082b6eaa32837aaaf307ffbc61489c50f8cb78"},{"path":"web-app/src/componentes/NovaConversa.spec.ts","sha256":"84184865db156d6c147e382982e235ea82f16ea9892cb0cc6e59f16ac1393757"},{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"},{"path":"web-app/src/config.ts","sha256":"ca30d02d04774b79d6e62715c83c49dd23f1db02f0b49ec6781634acbf09befb"},{"path":"web-app/src/estilo.css","sha256":"a86305e2303f640345c07d2b9f7ed9274b328d7459e714225e7f05885255809a"},{"path":"web-app/src/main.tsx","sha256":"42d0c9e45f19eb88f8cdbfd81343004becacf4b47c248f4d03d52bb9f951b9f3"},{"path":"web-app/src/telas/Consultar.tsx","sha256":"b65ce0320a082df811796ca66c73990fd57512ee123802fd2123f8dfad90fd89"},{"path":"web-app/src/telas/DefinirSenha.tsx","sha256":"7b3a3eeafe8af2f315d299cc40f612568a5216b9d99a5a52b50925cffbc466cd"},{"path":"web-app/src/telas/Historico.tsx","sha256":"a950e2571adc86cf5a390f7602ae2193d4b0de45d1c1f5b7640697308d398414"},{"path":"web-app/src/telas/IdentidadeVisual.tsx","sha256":"2b9720d7eaf3b0ef078ee6827d3d7fb3c93aa0b4c209662fbf143468c51cefa2"},{"path":"web-app/src/telas/Inbox.tsx","sha256":"66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"},{"path":"web-app/src/telas/Integracao.tsx","sha256":"66e87b87fbd35596fe064079be121c25f0d942c1b50b6b3b239fe765493fa59b"},{"path":"web-app/src/telas/Login.tsx","sha256":"3b62a752d0e4f71679dab3427862884bb8ebc5863d16d240a0c84d1d0b1ce923"},{"path":"web-app/src/telas/Modelos.spec.ts","sha256":"123e1b345342bdba0d1e9de07886c5116fd21c66d92d77a9fd814478142adf52"},{"path":"web-app/src/telas/Modelos.tsx","sha256":"ec5410d1e38a5dd963fe48d3ba715697d9c49cd574875c784fa8e6300275771c"},{"path":"web-app/src/telas/Numeros.tsx","sha256":"22cf5877d6336e4c22b8650402c5913b064278b9ba639e20e10f9a80c00fc791"},{"path":"web-app/src/telas/Painel.tsx","sha256":"7b678b29d8467dd8c22c4d8fa3667483b157c1495fb23b1368a34c48b2c6fdb2"},{"path":"web-app/src/telas/Perfil.tsx","sha256":"f425279d3598d14a609050d960b8848447afc3bace89fc0761f1cec2f045df0f"},{"path":"web-app/src/telas/Setores.tsx","sha256":"94280910f7ba31bd964350fe513d3d492b7e56b4a09931c29b9d727c8a734472"},{"path":"web-app/src/telas/TrocarSenha.tsx","sha256":"c9079fd57f8d28d61e313152f53dd85fbc48f74ea09a2bfbbdb88ed8a85df31f"},{"path":"web-app/src/telas/Typebot.tsx","sha256":"1088336e7ca1cfe29ff7a3dfdad66ec630d550f08387fc937cddb607fcc2ceee"},{"path":"web-app/src/telas/Usuarios.tsx","sha256":"3fc7c7a17004e17b9788c0d9f89083aa954893a60ab57827e6dd55a1bf882b18"},{"path":"web-app/src/telas/Wizard.tsx","sha256":"edbd2bb875874eb4bbd5dccdfc7a50e297e070ca9b16eeead771a1853327d2d1"},{"path":"web-app/src/tempoReal.spec.ts","sha256":"378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5"},{"path":"web-app/src/tempoReal.ts","sha256":"118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf"},{"path":"web-app/src/timeline.test.ts","sha256":"16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4"},{"path":"web-app/src/timeline.ts","sha256":"0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311"},{"path":"web-app/src/vite-env.d.ts","sha256":"6436117a885784b650c7d4fa2e8701fac64f15196680a65ad4072973063c9b8f"}],"protected_and_exact_companion_checks":[{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.ts","matches":true},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","matches":true},{"path":"api-app/test/message-template-bff.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-management.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","matches":true},{"path":"web-app/e2e/message-templates.spec.ts","matches":true},{"path":"web-app/src/App.tsx","matches":true},{"path":"web-app/src/telas/Modelos.spec.ts","matches":true},{"path":"web-app/src/telas/Modelos.tsx","matches":true},{"path":".github/workflows/ci.yml","matches":true},{"path":"scripts/test-channels-local.sh","matches":true},{"path":"scripts/check-channels-ci-parity.py","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.ts","matches":true},{"path":"api-app/src/surfaces/public/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/public.module.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","matches":true},{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","matches":true},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","matches":true},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","matches":true}],"previous_seal":"api-source-seal-e72-v1.1.json","exact_delta_from_previous":["api-app/src/domain/inbox/message-acceptance.service.ts","api-app/test/initial-message.e2e-spec.ts"],"delta_from_e54":["api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","api-app/prisma/schema.prisma","api-app/src/domain/inbox/dispatch-admission.service.spec.ts","api-app/src/domain/inbox/dispatch-admission.service.ts","api-app/src/domain/inbox/initial-message.service.spec.ts","api-app/src/domain/inbox/initial-message.service.ts","api-app/src/domain/inbox/message-acceptance.service.ts","api-app/src/domain/inbox/outbound.service.spec.ts","api-app/src/domain/inbox/outbound.service.ts","api-app/src/integrations/channels/prisma-channel-resolver.ts","api-app/src/surfaces/bff/conversations.controller.ts","api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts","api-app/test/webhooks.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts","web-app/src/telas/Inbox.tsx"],"limits":"Positive public files only. Preserve immutable earlier run receipts; no private/runtime/provider proof or current execution result inferred.","recorded_at_utc":"2026-10-23T11:51:45.878551+00:00","exact_source_delta_from_e73":[],"repeat_rationale":"E73 actual967pass/postseal/recoveredfreshness are retained. All known task/tmp output/helpers disappeared before raw PCV extraction. Repeat exact shared runner with durable owned Foundationtmp stdout and current per-run artifact collection; no code/test/source change."}
```

### all-source-recheck-e74-v1.1.json

SHA256 `fa70b64281a66dceb274d39986c02d4268e2d91a5d4fec9079c3d9535d2ee0dd`

```json
{"checkpoint":"E74 actual terminal independent full positive source recheck","stage":"After actual terminal/owned cleanup before release","count":259,"fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","matches_preseal_full_inventory_and_bytes":true,"record_reference":"all-source-seal-e74-v1.1.json#records","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","executor_reported_exit_code":0,"recorded_at_utc":"2026-10-23T12:20:26.725226+00:00","boundary":"Only declared positive public roots/exact files and owned synthetic artifacts; no private inputs/process/business rows."}
```

### candidate-source-preflight-e74-v1.1.json

SHA256 `8c5fd77ce98657366ad8099bd99c0bfa72bddadd4f069892cf837406cd77457e`

```json
{"kind":"E74 unchanged source preflight for durable repeat validation","recorded_at_utc":"2026-10-23T11:53:03Z","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","source_count":259,"current_source_recheck":{"checked_count":259,"changed_paths":[],"all_protected_and_exact_companion_checks_match":true},"exact_delta_from_e73":[],"repeat_rationale":"E73 canonical ALL reached exit 0, but its owned /tmp stdout and metrics disappeared after the terminal receipt. Repeat once without source changes to retain durable actual stdout and the current-run browser attestation.","normal_authority":"authority-e74-v1.1.json","routing":"routing-e74-v1.1.json","command":"bash scripts/test-channels-local.sh all","durable_stdout":"foundation_documentation/artifacts/tmp/stcon04-e74/executor-all-e74.txt","durable_browser_attestation":"foundation_documentation/artifacts/tmp/stcon04-e74/browser-attestation-e74.json","freeze":"No product or test source edits during the runner; wait for actual terminal and independent root postseal.","limits":"This is a repeat solely for durable evidence retention; no promotion, preserved-runtime activation, or real provider interaction is authorized."}
```

### browser-freshness-collection-e74-v1.1.json

SHA256 `c29fee4f7cabb0164361dd8424dbc39a9d369faa723f410b04333ec7521cafb0`

```json
{"kind":"Independent current exact per-run browser attestation collection","checkpoint":"E74","source_seal":"all-source-seal-e74-v1.1.json","attestation_sha256":"db7f75da51a0505e0efb046121b80efb24f6ba16c8d62ba095ed1d2db9a9251a","run_id":"2026-10-23T12-02-38-838Z","captured_at_utc":"2026-10-23T12:02:38.839Z","runtime":"v22.23.3","completed_migrations":28,"current_api_head":"db5a86758a165fac8a1ab587599c37b17890530c","current_web_head":"74b9d4b714044829796f875d00553f077c1c329d","served_dist_bundle_equal":true,"served_bundle_sha256":"f8e97efa6777dbc496b74cd527b1bae78e7766e4a4d58f752f7816cb62444343","manifest_count":93,"all_manifest_records_match_presealed_sources":true,"manifest_checks":[{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","matches":true},{"path":"api-app/prisma/schema.prisma","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","matches":true},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","matches":true},{"path":"api-app/src/domain/channels/transport/channel.ts","matches":true},{"path":"api-app/src/domain/historico/catalogo.ts","matches":true},{"path":"api-app/src/domain/historico/cobertura.ts","matches":true},{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/channel-window-policy.ts","matches":true},{"path":"api-app/src/domain/inbox/conversation-start.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/conversation-start.service.ts","matches":true},{"path":"api-app/src/domain/inbox/conversations.service.ts","matches":true},{"path":"api-app/src/domain/inbox/dispatch-admission.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","matches":true},{"path":"api-app/src/domain/inbox/incoming.service.ts","matches":true},{"path":"api-app/src/domain/inbox/incoming.typebot.integration.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message.service.ts","matches":true},{"path":"api-app/src/domain/inbox/message-acceptance.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","matches":true},{"path":"api-app/src/domain/inbox/outbound.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/outbound.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-observation.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","matches":true},{"path":"api-app/src/integrations/channels/account-reference.ts","matches":true},{"path":"api-app/src/integrations/channels/channel-adapter-factory.ts","matches":true},{"path":"api-app/src/integrations/channels/channel-adapter-registry.ts","matches":true},{"path":"api-app/src/integrations/channels/channel-transport.module.ts","matches":true},{"path":"api-app/src/integrations/channels/evolution-channel.ts","matches":true},{"path":"api-app/src/integrations/channels/meta-channel.ts","matches":true},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.resolver.ts","matches":true},{"path":"api-app/src/integrations/meta/initial-message.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/initial-message.client.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.ts","matches":true},{"path":"api-app/src/surfaces/bff/bff.module.ts","matches":true},{"path":"api-app/src/surfaces/bff/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/public.module.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/meta.controller.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","matches":true},{"path":"api-app/test/api-publica.e2e-spec.ts","matches":true},{"path":"api-app/test/atendimento.e2e-spec.ts","matches":true},{"path":"api-app/test/browser-server.cjs","matches":true},{"path":"api-app/test/channel-transport.e2e-spec.ts","matches":true},{"path":"api-app/test/conversation-start.e2e-spec.ts","matches":true},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","matches":true},{"path":"api-app/test/helpers.ts","matches":true},{"path":"api-app/test/initial-message.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-bff.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-management.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","matches":true},{"path":"api-app/test/timeline-fixtures.cjs","matches":true},{"path":"api-app/test/webhooks.e2e-spec.ts","matches":true},{"path":"web-app/e2e/channel-transport.spec.ts","matches":true},{"path":"web-app/e2e/message-templates.spec.ts","matches":true},{"path":"web-app/e2e/number-onboarding-freshness.ts","matches":true},{"path":"web-app/e2e/start-conversation.spec.ts","matches":true},{"path":"web-app/e2e/timeline-freshness.ts","matches":true},{"path":"web-app/src/api.spec.ts","matches":true},{"path":"web-app/src/api.ts","matches":true},{"path":"web-app/src/App.tsx","matches":true},{"path":"web-app/src/componentes/NovaConversa.spec.ts","matches":true},{"path":"web-app/src/componentes/NovaConversa.tsx","matches":true},{"path":"web-app/src/telas/Inbox.tsx","matches":true},{"path":"web-app/src/telas/Modelos.spec.ts","matches":true},{"path":"web-app/src/telas/Modelos.tsx","matches":true}],"limits":"Owned disposable database and fake provider; not preserved runtime/actual WhatsApp proof."}
```

### image-build-attestation-e74-v1.1.json

SHA256 `991451ac0dab27a8c552b61df54a8936b0ed8e39a8e481511debad985199d312`

```json
{"evidenceType":"local-public-image-build-and-offline-inspection","run":"E74","recordedAtUtc":"2026-10-23T12:24:24.479786+00:00","sourceSeal":"all-source-seal-e74-v1.1.json","sourceFingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","builds":{"api":{"sessionId":42492,"exitCode":0,"command":"docker.exe build -t leadshug-stcon04-api:e74 - < foundation_documentation/artifacts/tmp/stcon04-e74/build-context-api-e74.tar","archivePath":"foundation_documentation/artifacts/tmp/stcon04-e74/build-context-api-e74.tar","archiveSha256":"ec671cbe971395d1d4c2fe4f3cc99920fcb347d9ce5dc3c07ca154060ea042db","stdoutPath":"foundation_documentation/artifacts/tmp/stcon04-e74/build-api-e74.txt","stdoutSha256":"9917c1843439f0bdc837a4d2393a81a77ba00d22498c58695eea915479e4c422","imageId":"sha256:092005eb90275c3ab55e14c6ff2fe5fde241d4bde15324ce84bfb21f0a11c2f2","platform":"linux/amd64","entrypoint":["/entrypoint.sh"],"cmd":["node","dist/main.js"],"workingDirectory":"/app"},"web":{"sessionId":null,"exitCode":0,"command":"docker.exe build -t leadshug-stcon04-web:e74 - < foundation_documentation/artifacts/tmp/stcon04-e74/build-context-web-e74.tar","archivePath":"foundation_documentation/artifacts/tmp/stcon04-e74/build-context-web-e74.tar","archiveSha256":"959355f4dfc16824cdc8a83632dfda673c8ba71a7d8170d055164e89180152c7","stdoutPath":"foundation_documentation/artifacts/tmp/stcon04-e74/build-web-e74.txt","stdoutSha256":"8935a1bc0b08403603a34f523c321fdbdb6115023e3b9f5001df481c08507f62","imageId":"sha256:9787da8f734123e4f2875ce9b47c7bb23b45a8d64bbba98a830d51dd05f9f53b","platform":"linux/amd64","entrypoint":["/docker-entrypoint.sh"],"cmd":["nginx","-g","daemon off;"],"workingDirectory":"/"}},"offlineInspection":{"network":"none","filesystem":"read-only","entrypointOverridden":true,"applicationEntrypointStarted":false,"api":{"inspectionReceiptPath":"foundation_documentation/artifacts/tmp/stcon04-e74/inspect-api-e74.json","inspectionReceiptSha256":"eb4d8f980b37319031e193bfffb5a0b29d90fe9a324d80dbe90571433111b9c5","nodeVersion":"v22.23.3","prismaClientVersion":"6.19.3","distJsCount":106,"distManifestAggregateSha256":"8c04e9efd81751e93e251867b19864d05baa95c0aaf9809ae5a8b92d47fa7c4b","distManifestAggregateMethod":"SHA-256 of sorted lines: relative-js-path, space, file SHA-256, newline","distMainJsSha256":"4939123b00a86d0fb47ed2483ee13cb8ec0fbc374e565653c32724e920c2b9f0","messageAcceptanceServiceJsSha256":"c39417b3b901d3347014f1735e3881194dadf5da3a5a8049540b6568e7f2d019","initialMessageServiceJsSha256":"702084dc0a0135af7d31fef56e342145e7925aafc65594eafa20112e8e012b16","outboundServiceJsSha256":"3ac0314c34de5bdb33b48e90cb52ddcad849fb1697af5cf34e7e8135b3e558a5","dispatchAdmissionServiceJsSha256":"fdc8586bd835931c11fcfd541db58a32b90ff6515d244b32474a5d88ea495dc1","prismaSchemaSha256":"19ea60e6e5a1675a4ff12581237b2f91c2359b61d7b8bcb9e8bf1c1ebf26435d","migrationSha256":{"20261020170000_message_inbound_window_index":"586e709e07736eca0908ab5dcc668cf0e0b317189b4c963b361399848a3c9710","20261022140000_initial_message_orchestration":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437","20261022150000_initial_message_admissions":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a","20261022160000_initial_message_inbox_order":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544"}},"web":{"inspectionReceiptPath":"foundation_documentation/artifacts/tmp/stcon04-e74/inspect-web-e74.txt","inspectionReceiptSha256":"ffe0df470a936034f3e83663d17f8cbf6f9b4bb129dc85bd11e9cd18ce13e9ba","indexHtmlSha256":"cf24ab6c9ad71d0260042ff483c208f8e087aac7ef14c3f0c9ead052831656dc","bundlePath":"/usr/share/nginx/html/assets/index-DPFJ9ybt.js","bundleSha256":"f8e97efa6777dbc496b74cd527b1bae78e7766e4a4d58f752f7816cb62444343","equalsCurrentServedAndDistBundle":true}},"freshness":{"attestationPath":"foundation_documentation/artifacts/tmp/stcon04-e74/browser-attestation-e74.json","attestationSha256":"db7f75da51a0505e0efb046121b80efb24f6ba16c8d62ba095ed1d2db9a9251a","runId":"2026-10-23T12-02-38-838Z","servedBundleSha256":"f8e97efa6777dbc496b74cd527b1bae78e7766e4a4d58f752f7816cb62444343","distBundleSha256":"f8e97efa6777dbc496b74cd527b1bae78e7766e4a4d58f752f7816cb62444343"},"limitations":["No application entrypoint was started.","No Compose, private env/input, database, provider, tunnel, or preserved runtime was used.","Build artifacts are local; no deployment or delivery claim is made.","A preliminary shell input-redirection attempt for the API archive failed on WSL ACL permissions before docker.exe started; after access was restored, the recorded successful API build used the sealed archive hash."]}
```

### seal-metadata-provenance-e74-v1.1.json

SHA256 `fa2b3af11345813164c624cb5f67ae0d65413740b0c93723c83fa556ea76636c`

```json
{"kind":"Explicit metadata provenance for unchanged-source E74 repeat preseal","recorded_at_utc":"2026-10-23T12:11:10.364179+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_seal_sha256":"40ad3c8844a20d2d688269ac60f0b2648460bb3c26d6e6bf2fe912fcd5694d4c","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","source_delta_from_e73":[],"current_exact_public_git_heads":{"root":"80e3940126f22a941f90dba4f5e801b6c0eb2f58","api":"db5a86758a165fac8a1ab587599c37b17890530c","web":"74b9d4b714044829796f875d00553f077c1c329d","foundation":"d32e07ed98a6bb9eae42d5f0e45e81d07d466cc7"},"current_stdout_path":"foundation_documentation/artifacts/tmp/stcon04-e74/executor-all-e74.txt","current_preworker_attestation_path":"foundation_documentation/artifacts/tmp/stcon04-e74/browser-attestation-e74.json","disclosure":"E74 seal was copied from E73 after root re-enumerated and matched all259 current source records. Its recorded_at_utc/checkpoint/exact_source_delta/repeat_rationale are E74-specific. The retained captured_at_utc, synthetic_stdout_planned, previous_seal, exact_delta_from_previous and fresh_git_identity fields describe the historical E73 seal lineage, not a newly invoked E74 capture. This supplement makes current stream/identity explicit without rewriting immutable seal bytes. Current terminal receipt and independent postseal must bind actual E74 stdout before review."}
```

### implementation-r4-resolution-e74-v1.1.json

SHA256 `e85078f17668a92ba2e32b31a18a48db5394cbe72810c25286da2f403470017f`

```json
{"kind":"Root current-source revalidation of the three reproduced r4 corrections; independent r7 remains required","recorded_at_utc":"2026-10-23T12:20:47.197456+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","all_result":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","rows":[{"finding_id":"F-1DF50690","source_finding_id":"ARCH-ST04-R4-01","severity":"high","resolution":"Integrated","problem":"Trusted window/context validation could precede a lock wait and expire or rotate before the durable SENDING transition.","correction":"Preserve the established lock order. Both ordinary and initial claim carry the single-policy trusted expiry into the same owner/slot/lease-scoped SENDING SQL CAS and compare it to clock_timestamp(). The existing resolver holds NOWAIT shared BU/channel/credential pins through that transaction; mutable readiness and credential validation cannot be invalidated before commit.","sources":[{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9","lines":[258,272,315,329]},{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f","lines":[184,189,628,634]},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","sha256":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943","lines":[259,268]}],"actual_proof_markers":["ST04_FINAL_WINDOW_CAS ","ST04_ORDINARY_FINAL_WINDOW_CAS ","ST04_CREDENTIAL_PIN ","ST04_BU_READINESS_PIN "],"limits":"Ordinary direct CAS probe measures claimGranted, not a provider POST. Credential/BU mutation waits on an actual held pin; after commit a later mutation is validly ordered after dispatch authorization, so truthful201 SUCCEEDED or503 known-acceptance/local-blocked are both asserted. Zero POST is required while pinned, not after the mutation is serialized later.","actual_markers":{"ST04_FINAL_WINDOW_CAS ":{"inspectedOpen":true,"expiresAt":"2026-10-23T11:56:54.450Z","databaseClockExpired":true,"databaseNow":"2026-10-23T11:56:54.456Z","postsDeltaWhilePaused":0,"postsDelta":0,"outMessagesDelta":0,"finalState":"REJECTED","leaseBudgetMs":90000},"ST04_ORDINARY_FINAL_WINDOW_CAS ":{"capturedEligible":true,"databaseWindowExpiredBeforeClaimUpdate":true,"claimGranted":false,"state":"PREPARED","dispatchDeadlineAt":null,"releasedAt":null},"ST04_CREDENTIAL_PIN ":{"validationSucceeded":true,"credentialUpdateWaited":true,"credentialVersionAdvanced":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":1,"sendStatus":201,"finalState":"SUCCEEDED"},"ST04_BU_READINESS_PIN ":{"validationSucceeded":true,"readinessUpdateWaited":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":0,"sendStatus":503,"buStatusAfterUpdate":"INATIVO","intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"}}},{"finding_id":"F-3119C7D6","source_finding_id":"ARCH-ST04-R4-02","severity":"medium","resolution":"Integrated","problem":"Initial identity-first locks and protected ST05 user/BU/grant/channel-before-identity refresh locks formed an actual cycle.","correction":"Preserve identity→contact advisory→conversation→intent relative order and the unchanged ST05 owner. Mutable context pins and actor/grant shared locks use NOWAIT. SQL55P03 throws a conflict to roll back, never continues queries in an aborted transaction. Existing actor tenant/session/version checks remain. Known provider acceptance survives blocked local completion.","sources":[{"path":"api-app/src/surfaces/bff/conversations.controller.ts","sha256":"0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3","lines":[196,235]},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","sha256":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943","lines":[259,268]}],"actual_proof_markers":["ST04_ST05_CLAIM_OVERLAP ","ST04_ST05_LOCAL_OVERLAP "],"limits":"NOWAIT applies to row locks; PostgreSQL table-level locks may still wait within existing transaction bounds. Tests overlap the actual unmodified ST05 owner, observe its lock wait, and compare real database deadlock counters. No provider retry is introduced.","actual_markers":{"ST04_ST05_CLAIM_OVERLAP ":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":409,"deadlocksDelta":0,"postsDelta":0,"outMessages":0,"intentState":"REJECTED","receiptState":"NONE"},"ST04_ST05_LOCAL_OVERLAP ":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":503,"deadlocksDelta":0,"postsDelta":1,"localOutMessages":0,"intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"}}},{"finding_id":"F-7C61C9F4","source_finding_id":"ARCH-ST04-R4-03","severity":"medium","resolution":"Integrated","problem":"Latest11 recovery options and ordinary conversation conflict could sort/scan accumulated history despite bounded returned rows.","correction":"Use ordered intent index (conversation_id,bu_id,created_at DESC,id DESC) plus one SQL-only active admission partial ordered index (conversation_id,created_at DESC,id DESC,bu_id) WHERE released_at IS NULL. Both actual active queries retain their literal active predicate and whole-conversation conflict semantics. Existing uniqueness/quota indexes stay unchanged.","sources":[{"path":"api-app/prisma/schema.prisma","sha256":"19ea60e6e5a1675a4ff12581237b2f91c2359b61d7b8bcb9e8bf1c1ebf26435d","lines":[443,493]},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","sha256":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a","lines":[35,39,70,71]},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d","lines":[269,377],"line_reference_note":"HistoricalE71 anchors; current full source/actual SQL markers govern."},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f","lines":[93,115]}],"actual_proof_markers":["ST04_OPTIONS_PLAN ","ST04_ACTIVE_CONFLICT_PLAN "],"limits":"Actual captured Prisma SQL/params use default planner, ANALYZE,2048 old released intents,2048 old released admissions and256 active admissions. No planner forcing, threshold relaxation or extra full redundant index. The current migration has only run on disposable targets; preserved-local additive migration remains separately gated.","actual_markers":{"ST04_OPTIONS_PLAN ":{"recent":{"sql":"SELECT \"public\".\"initial_message_intents\".\"id\", \"public\".\"initial_message_intents\".\"conversation_id\", \"public\".\"initial_message_intents\".\"bu_id\", \"public\".\"initial_message_intents\".\"actor_id\", \"public\".\"initial_message_intents\".\"idempotency_key\", \"public\".\"initial_message_intents\".\"owner_nonce\", \"public\".\"initial_message_intents\".\"request_fingerprint\", \"public\".\"initial_message_intents\".\"request\", \"public\".\"initial_message_intents\".\"selected_context\", \"public\".\"initial_message_intents\".\"state\"::text, \"public\".\"initial_message_intents\".\"lease_expires_at\", \"public\".\"initial_message_intents\".\"dispatch_deadline_at\", \"public\".\"initial_message_intents\".\"external_message_id\", \"public\".\"initial_message_intents\".\"slot_released_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_by_actor_id\", \"public\".\"initial_message_intents\".\"created_at\", \"public\".\"initial_message_intents\".\"updated_at\" FROM \"public\".\"initial_message_intents\" WHERE (\"public\".\"initial_message_intents\".\"conversation_id\" = $1 AND \"public\".\"initial_message_intents\".\"bu_id\" = $2) ORDER BY \"public\".\"initial_message_intents\".\"created_at\" DESC, \"public\".\"initial_message_intents\".\"id\" DESC LIMIT $3 OFFSET $4","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1","f68505b5-e15f-4950-aa6c-2a98e053bdcd",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.28,"totalCost":4.02,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0},{"type":"Index Scan","relation":"initial_message_intents","index":"initial_message_intents_options_order_idx","startupCost":0.28,"totalCost":697.54,"estimatedRows":2048,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0}]},"active":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"conversation_id\", \"public\".\"dispatch_admissions\".\"bu_id\", \"public\".\"dispatch_admissions\".\"caller\"::text, \"public\".\"dispatch_admissions\".\"actor_id\", \"public\".\"dispatch_admissions\".\"owner_nonce\", \"public\".\"dispatch_admissions\".\"selected_context\", \"public\".\"dispatch_admissions\".\"state\"::text, \"public\".\"dispatch_admissions\".\"expires_at\", \"public\".\"dispatch_admissions\".\"dispatch_deadline_at\", \"public\".\"dispatch_admissions\".\"released_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_by_actor_id\", \"public\".\"dispatch_admissions\".\"created_at\", \"public\".\"dispatch_admissions\".\"updated_at\" FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"bu_id\" = $2 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $3 OFFSET $4","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1","f68505b5-e15f-4950-aa6c-2a98e053bdcd",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.27,"totalCost":14.25,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":8,"sharedReadBlocks":0},{"type":"Index Scan","relation":"dispatch_admissions","index":"dispatch_admissions_options_order_idx","startupCost":0.27,"totalCost":325.64,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":8,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, created_at DESC, id DESC, bu_id) WHERE (released_at IS NULL)","releasedHistory":2048,"activeHistory":256}},"ST04_ACTIVE_CONFLICT_PLAN ":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"state\"::text FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $2 OFFSET $3","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.27,"totalCost":14.17,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0},{"type":"Index Scan","relation":"dispatch_admissions","index":"dispatch_admissions_options_order_idx","startupCost":0.27,"totalCost":323.72,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, created_at DESC, id DESC, bu_id) WHERE (released_at IS NULL)","providerPostDelta":0,"providerCallDelta":0,"messageDelta":0}}}],"causal_evidence":["api-result-e65-v1.1.json","api-result-e66-v1.1.json"],"intermediate_evidence":["all-result-e67-v1.1.json","all-result-e68-v1.1.json","all-result-e69-v1.1.json","all-result-e70-v1.1.json"],"test_support_corrections":["E67 unused binding lint and E68 missing import compile support failures are not test RED.","E69 global Date clock tripped transport deadline rather than final session oracle. E70 uses the existing real SessionService verifier clock parameter after the remote-GET barrier, preserving the actual signed verification and real transport clock.","E70 uses2048 released admission rows2h old, so rate limits do not prevent the intended ordinary conflict query. Actual E70 ordered full index still scanned/sorted2304 rows. E71 changes the same admitted migration to a partial index, preserving data, actual-query and no-side-effect assertions; native metadata expectations match the intended actual partial definition.","Original E65/E66 precommit credential mutation tests proved the unpinned defect. Current held-pin tests assert that real mutation waits and later completes; postclaim mutation is correctly permitted while preserving known provider receipt/local recovery semantics."],"remaining":["Fresh complete architecture/security, eight-section TQA and cutover review","Current source-bound images, approved preserved-local activation, canonical module consolidation, full canonical diff exception, operator and final delivery gates"],"assurance_boundary":"Owned disposable PostgreSQL/BFF/served browser and fake provider only. No private inputs, preserved business rows, provider requests or completed delivery inferred."}
```

### implementation-r6-resolution-e74-v1.1.json

SHA256 `b437befd4b4b1915d2181b10d1f5681de077fc8216fde7559bf8d3a1be2e7c7b`

```json
{"kind":"Root resolution of both r6 causal findings against current full source-bound proof; independent r7 remains required","recorded_at_utc":"2026-10-23T12:20:47.197456+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","all_result":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","rows":[{"finding_id":"F-CF091066","source_finding_id":"ARCH-ST04-R6-01","severity":"medium","resolution":"Integrated","problem":"Current verified identity could qualify a trusted timestamp while its managed lifecycle was false.","correction":"Read managed_lifecycle in the existing same FOR SHARE identity projection; pass only that locked boolean to private timestamp qualification. Preserve Message/receipt acceptance; duplicate reconciliation never promotes a prior null timestamp. No extra query, caller flag, lock-order change or provider call.","sources":[{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","lines":[120,148,188,212],"sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/test/webhooks.e2e-spec.ts","lines":[123,144,149,152,163],"sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"}],"actual_proof_markers":["does not promote an inbound timestamp received while the current resource is unmanaged"],"actual_proof":"Signed-webhook/PG matrix passes: retained IN/unread and null trusted timestamp, closed window before/after lifecycle activation, duplicate without promotion, later new managed IN opens window, zero provider effects.","causal_evidence":"api-result-e72-v1.1.json","limits":"Actual E72 read-projection defect, not an outbound exploit or actual provider effect."},{"finding_id":"F-5E961B39","source_finding_id":"TQA-R6-01","severity":"medium","resolution":"Integrated","problem":"Native deadlock statistics silently defaulted to zero on invalid results.","correction":"Test helper requires exactly one row and a nonnegative native bigint; malformed/missing/ambiguous results fail the test. Real counter overlap probes remain.","sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","lines":[78,145,149,1280,1318,1357,1399],"sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}],"actual_proof_markers":["fails closed when native deadlock statistics are","ST04_ST05_CLAIM_OVERLAP ","ST04_ST05_LOCAL_OVERLAP "],"actual_proof":"All four isolated empty/malformed/multiple/negative fixtures reject; actual unchanged ST05-owner claim/local overlap probes pass with native zero-deadlock deltas.","causal_evidence":"api-result-e72-v1.1.json","limits":"One helper query is substituted once and restored in finally. This test-only helper does not authorize product dispatch; no actual missing native statistics are claimed."}],"r6_collection":"implementation-review-collection-r6-v1.1.json","test_first_boundary":"E72 actual test-only API RED reached four statistics failures and four lifecycle soft assertions before the two exact E73 fixes. E73 actual967pass/postseal/browser is retained; unchanged E74 repeats only to retain lost raw stdout/metrics. No earlier unreached assertion or actual outbound exploit is relabeled.","remaining":["Fresh complete eight-section TQA; terse r6 response insufficient","Current architecture/security/cutover and module review","Current offline images plus approved preserved runtime/operator/full-diff/final gates"],"boundary":"Positive public sources and owned synthetic evidence only; no private environment/business/provider inspection."}
```

### ci-parity-current-marker-e74-v1.1.json

SHA256 `0568a5972438e5a026326190ea73c97c619acc1ca792a7d7ff3c134760d5bcf5`

```json
{"kind":"Actual selected ALL mandatory CI-parity self-test marker; no extra invocation","source_seal":"all-source-seal-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","marker":{"guard":"channels-ci-parity-v1","mutations_rejected":["missing-pr-trigger","missing-channels-job","missing-retained-guard","weakened-job-gate","swallowed-job-errors","skipped-validate-step","swallowed-retained-job","skipped-retained-admission","missing-retained-private-checkout","missing-common-guard","swallowed-common-guard-failure","missing-e2e","swallowed-e2e-failure","missing-browser","missing-migrate","missing-generate","missing-lint","reordered-suite","missing-shell-guard","widened-wsl-socket","changed-wsl-host-prefix","wrong-wsl-mask-source","missing-wsl-overlay"],"outer_wrapper":{"collision_control":{"compose_calls":0,"exit_code":1},"empty_config_control":{"compose_calls":[["compose","--project-name","leadshug_channels_validation","--env-file","/workspace/.env.example","--env-file","/tmp/tmp.WFqNa0EnEB","-f","/workspace/docker-compose.yml","-f","/workspace/docker-compose.channels.yml","--profile","validation","config","--quiet"]],"exit_code":0},"inventory_failures":{"network":{"compose_calls":0,"docker_calls":3,"exit_code":1},"ps":{"compose_calls":0,"docker_calls":1,"exit_code":1},"volume":{"compose_calls":0,"docker_calls":2,"exit_code":1}},"mandatory_failure_cleanup":{"cleanup_observed":true,"compose_lifecycle":["run","down"],"exit_code":42,"provider_or_real_docker_invoked":false,"required_leaf":"fake python3 reached through actual RUNNER_SCRIPT and returned 42"},"native_path_control":{"exit_code":0,"overlay_added":false,"posix_bind_paths_preserved":true},"unsupported_wsl_socket_control":{"docker_calls":0,"exit_code":1},"wsl_bind_path_control":{"skipped":"self-test checkout is not on a WSL-mounted drive"}},"yaml":"safe-no-alias-no-duplicates"},"limits":"Local shared-runner/CI and wrapper failure/cleanup controls; remote CI unknown, no preserved-runtime proof."}
```

### current-synthetic-pcv-samples-e74-v1.1.json

SHA256 `75595b6d8884606d36279d02bce24a6f82bb2e695b72707bbd62be6018ca39ae`

```json
{"kind":"Actual same-run18 synthetic marker values from retained current canonical ALL stdout","recorded_at_utc":"2026-10-23T12:20:40.734967+00:00","evidence_receipt":"all-result-e74-v1.1.json","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","current_recovery_options_plans":{"recent":{"sql":"SELECT \"public\".\"initial_message_intents\".\"id\", \"public\".\"initial_message_intents\".\"conversation_id\", \"public\".\"initial_message_intents\".\"bu_id\", \"public\".\"initial_message_intents\".\"actor_id\", \"public\".\"initial_message_intents\".\"idempotency_key\", \"public\".\"initial_message_intents\".\"owner_nonce\", \"public\".\"initial_message_intents\".\"request_fingerprint\", \"public\".\"initial_message_intents\".\"request\", \"public\".\"initial_message_intents\".\"selected_context\", \"public\".\"initial_message_intents\".\"state\"::text, \"public\".\"initial_message_intents\".\"lease_expires_at\", \"public\".\"initial_message_intents\".\"dispatch_deadline_at\", \"public\".\"initial_message_intents\".\"external_message_id\", \"public\".\"initial_message_intents\".\"slot_released_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_by_actor_id\", \"public\".\"initial_message_intents\".\"created_at\", \"public\".\"initial_message_intents\".\"updated_at\" FROM \"public\".\"initial_message_intents\" WHERE (\"public\".\"initial_message_intents\".\"conversation_id\" = $1 AND \"public\".\"initial_message_intents\".\"bu_id\" = $2) ORDER BY \"public\".\"initial_message_intents\".\"created_at\" DESC, \"public\".\"initial_message_intents\".\"id\" DESC LIMIT $3 OFFSET $4","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1","f68505b5-e15f-4950-aa6c-2a98e053bdcd",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.28,"totalCost":4.02,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0},{"type":"Index Scan","relation":"initial_message_intents","index":"initial_message_intents_options_order_idx","startupCost":0.28,"totalCost":697.54,"estimatedRows":2048,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0}]},"active":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"conversation_id\", \"public\".\"dispatch_admissions\".\"bu_id\", \"public\".\"dispatch_admissions\".\"caller\"::text, \"public\".\"dispatch_admissions\".\"actor_id\", \"public\".\"dispatch_admissions\".\"owner_nonce\", \"public\".\"dispatch_admissions\".\"selected_context\", \"public\".\"dispatch_admissions\".\"state\"::text, \"public\".\"dispatch_admissions\".\"expires_at\", \"public\".\"dispatch_admissions\".\"dispatch_deadline_at\", \"public\".\"dispatch_admissions\".\"released_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_by_actor_id\", \"public\".\"dispatch_admissions\".\"created_at\", \"public\".\"dispatch_admissions\".\"updated_at\" FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"bu_id\" = $2 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $3 OFFSET $4","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1","f68505b5-e15f-4950-aa6c-2a98e053bdcd",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.27,"totalCost":14.25,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":8,"sharedReadBlocks":0},{"type":"Index Scan","relation":"dispatch_admissions","index":"dispatch_admissions_options_order_idx","startupCost":0.27,"totalCost":325.64,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":8,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, created_at DESC, id DESC, bu_id) WHERE (released_at IS NULL)","releasedHistory":2048,"activeHistory":256}},"current_claim_and_refresh_probes":{"ST04_ACTIVE_CONFLICT_PLAN ":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"state\"::text FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $2 OFFSET $3","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.27,"totalCost":14.17,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0},{"type":"Index Scan","relation":"dispatch_admissions","index":"dispatch_admissions_options_order_idx","startupCost":0.27,"totalCost":323.72,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, created_at DESC, id DESC, bu_id) WHERE (released_at IS NULL)","providerPostDelta":0,"providerCallDelta":0,"messageDelta":0},"ST04_FINAL_WINDOW_CAS ":{"inspectedOpen":true,"expiresAt":"2026-10-23T11:56:54.450Z","databaseClockExpired":true,"databaseNow":"2026-10-23T11:56:54.456Z","postsDeltaWhilePaused":0,"postsDelta":0,"outMessagesDelta":0,"finalState":"REJECTED","leaseBudgetMs":90000},"ST04_ORDINARY_FINAL_WINDOW_CAS ":{"capturedEligible":true,"databaseWindowExpiredBeforeClaimUpdate":true,"claimGranted":false,"state":"PREPARED","dispatchDeadlineAt":null,"releasedAt":null},"ST04_CREDENTIAL_PIN ":{"validationSucceeded":true,"credentialUpdateWaited":true,"credentialVersionAdvanced":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":1,"sendStatus":201,"finalState":"SUCCEEDED"},"ST04_BU_READINESS_PIN ":{"validationSucceeded":true,"readinessUpdateWaited":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":0,"sendStatus":503,"buStatusAfterUpdate":"INATIVO","intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"},"ST04_ST05_CLAIM_OVERLAP ":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":409,"deadlocksDelta":0,"postsDelta":0,"outMessages":0,"intentState":"REJECTED","receiptState":"NONE"},"ST04_ST05_LOCAL_OVERLAP ":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":503,"deadlocksDelta":0,"postsDelta":1,"localOutMessages":0,"intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"}},"limits":"Owned disposable PG/BFF/browser/fake provider only. These port/fixture effects are not TCP provider delivery, SLO or real-preserved runtime proof.","samples":{"[EPS-EVIDENCE]":{"policy_schema_version":"pcv-1","lane_id":"EPS","trigger_result":"required","trigger_severity":"medium","trigger_reason_code":"EPS-DATA-PATH-CHANGED","gate_deadline":"before_local_implemented","min_evidence_rule_id":"EPS-E2","acceptance_rule_id":"EPS-A2","sample_profile":"EPS-SP-STRONG","strong_query_evidence_type":"EXPLAIN (FORMAT JSON) plus bounded endpoint timings","access_pattern_classification":{"registrationGet":"one attempt by id and Mantenedora; no provider calls","idempotencyReplay":"unique lookup by Mantenedora and Idempotency-Key","channelList":"BU-filtered projection; no provider fan-out"},"touched_path_audit_summary":"NumberRegistrationService direct attempt reads and ChannelsController BU-filtered channel list; existing unique/index definitions in Prisma schema.","seededAttempts":25,"explain":[{"Plan":{"Node Type":"Index Scan","Parallel Aware":false,"Async Capable":false,"Scan Direction":"Forward","Index Name":"channel_registration_attempts_mantenedora_id_idempotency_key_ke","Relation Name":"channel_registration_attempts","Alias":"channel_registration_attempts","Startup Cost":0.14,"Total Cost":8.16,"Plan Rows":1,"Plan Width":32,"Index Cond":"((mantenedora_id = '96e432df-2766-4566-a41e-582afad4a589'::text) AND (idempotency_key = 'e0000000-e000-4000-8000-000000000001'::text))"}}],"timing":{"samples":20,"minMs":7.024422999999842,"medianMs":7.932076000000052,"p95Ms":9.50621000000001,"maxMs":11.118535000000065},"limits":"Local disposable PostgreSQL observation only; no latency threshold or capacity/SLO claim."},"[CHANNEL-EPS-EVIDENCE]":{"exact_value_sha256":"193d7d3c0499d31570b942bcfe17aa52530b0e6745ef36f024327fbcb43978c6","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"[CHANNEL-LATEST-MESSAGE-EVIDENCE]":{"exact_value_sha256":"1ccdad9a191a930dd96b6b05dbd624a0eafe95bce8c47bdacb50a0286407fe23","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"[CHANNEL-HISTORY-SCAN-EVIDENCE]":{"exact_value_sha256":"f81406412154c1cbcf1819cc55610d08c24e71470d7a7e3b8812650820376d47","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"[CHANNEL-WINDOW-SCOPE-EVIDENCE]":{"exact_value_sha256":"5e3b37138a82f6cdd34c70d3d663ea278a89e064b7d4e8ac2f10c8482f9c3d5d","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"[INBOX-ORDER-EXPLAIN]":{"exact_value_sha256":"fb1ab26168d67740bcd98f9232e2c7f41b0f6e339174b88341107e47250e23e8","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"[INBOX-OUT-HEAVY-QUERY-COUNT]":{"exact_value_sha256":"91bc685c275601251aa275d90ff58c4470c6894f9cdcc1d396d1fd7526aa2b69","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"[CONVERSATION-OPEN-BCI]":{"exact_value_sha256":"04315e0ec4d92cf2f10c5b62437eadd48f4b10c93f7036243678cfae6ea4ad90","exact_duplicate_in":"pcv-bci-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_BCI_5x20 ":{"exact_value_sha256":"867bc8394a19d1b8aa3d78ae3e8484d9aa221fe2d612ed0cec9df89b9ddbeed0","exact_duplicate_in":"pcv-bci-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"[FRC-COMPOSER-EVIDENCE]":{"exact_value_sha256":"f9a85994e2d78301bd72ba3523730206dd55e6f7d3e12401264492f1c67a2ad7","exact_duplicate_in":"pcv-frc-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_OPTIONS_PLAN ":{"exact_value_sha256":"be77bc511fb8b01a76e5c413cd2be3b8a68adc2251792c9c6e91cba5305a9bc4","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_ACTIVE_CONFLICT_PLAN ":{"exact_value_sha256":"013aaff2afa004eaad3cb6bf288c369974bb4da75594c68a588aa235e945374f","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_FINAL_WINDOW_CAS ":{"exact_value_sha256":"862446d1052cca9327d3e25c9813a8158cd23df60ea7c4fe0567d16e27e33901","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_ORDINARY_FINAL_WINDOW_CAS ":{"exact_value_sha256":"ebd137e25380df70dfa0e97b769ee885d354f08dcd9b1483defdc79c8d8cd0d3","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_CREDENTIAL_PIN ":{"exact_value_sha256":"94c6f4c75688c15d4622ac3389b71a5e7a5e8891cdbdc06afcb93c7ba1103cfa","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_BU_READINESS_PIN ":{"exact_value_sha256":"f63d821f90675b0990c9e1213b5c37396509ac37e372bc14e740703e240421cf","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_ST05_CLAIM_OVERLAP ":{"exact_value_sha256":"cea3b39207847afee2e4ba1166a12d7063e0d5bb165ecd99086c16348b6af2d9","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."},"ST04_ST05_LOCAL_OVERLAP ":{"exact_value_sha256":"2bc0fcc716eaf80014996efc7c6a2c5a34630b30dab348d2787772265600ba7f","exact_duplicate_in":"pcv-eps-e74-v1.1.json","note":"Exact value is included in the named full same-run PCV artifact_payload."}},"deduplication_note":"Each marker key is retained. Values are either embedded verbatim or referenced by exact canonical-JSON SHA256 to a full same-run PCV artifact payload included below."}
```

### local-activation-proof-plan-e74-proposal-v1.1.json

SHA256 `d950dfda0196fe60208ac141f19ea6189488294465e4680c6083ab83c3d090f8`

```json
{"kind":"Concrete corrected E74 preserved-local activation and operator proof proposal; not approved or executed","governing_todo":"foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md","preconditions":["Frozen complete candidate passes canonical all with identical pre/post public source manifest.","Required independent implementation/migration/security/architecture assessments resolve material findings.","Full diff guard inspection exception is separately explicit; no inferred private inspection.","Reconfirm preserved local project identity from exact approved public topology and safe selected Docker metadata; stop on unexpected topology/resources."],"proposed_target":{"project":"leadshug_channels_local","profile":"channels-local","public_composition":["docker-compose.yml","docker-compose.channels.yml"],"operator_origin":"existing loopback gateway on127.0.0.1:8083; current availability unknown","services_to_replace":["api","web"],"services_to_preserve":["postgres","gateway","evolution-postgres","evolution-redis","evolution"],"data":"All existing volumes, BUs, channels, credentials and conversation history preserved. No reset/drop/truncate/deletion."},"build_provenance":["Use explicit positive public build-input inventory from principal checkout; no root-wide context capture or private traversal.","No copied writable checkout/worktree; disposable build context/archive is a generated build artifact only.","Record approved public input hashes, image IDs/digests, API compiled hashes and Web built/served bundle equality.","Do not claim an unbuilt source fingerprint as the served image. Fresh attestation must precede interpreting operator/browser proof.","Public Dockerfiles were inspected for this proposal: API explicitly COPYs package/lock,prisma,src,tsconfigs,nest-cli and docker/entrypoint; Web uses COPY . . in its builder, so its generated build context must contain only individually admitted public inputs (never the whole checkout). These Dockerfiles are not mutated. Actual Alpine image health is required; Debian disposable-suite results alone do not establish native runtime compatibility."],"proposed_private_exception":{"purpose":"Mechanical Compose consumption of the existing private test configuration to preserve current runtime settings.","allowed":"Only existing .env.testing as an opaque input to existing Compose; no printing/copying/dumping values. Local migration process may use its existing DB connection in-memory.","forbidden":"No .local-files access; no process argument/env/log dumps; no manual token/provider probe; no credential/session password read by agent; no private-file edits unless separately concrete and approved.","unknown":"HTTPS current hostname/process state unknown; no existing tunnel adopted/killed by assumption. If origin change requires private-file mutation, prepare exact bounded change first."},"migration":["Only three approved additive initial_message migrations from sealed source after disposable deploy/status/schema proof.","Preflight exact local TEST database/service; record migration names/checksums/status and no unexpected pending drift.","SET lock_timeout5s and statement_timeout60s as in approved SQL; stop on lock/migration failure; no blind retry/reset.","No destructive down migration; rollback assessment is application compatibility plus preserved data, not dropping new tables/columns.","Rollback assessment: an older API does not enforce the new initial-intent interlock. Do not automatically revert to an old API after a possible dispatch or while an initial outcome is unresolved; stop outbound use, preserve data and review the exact attempt in the normal UI. No destructive down/reset or blind migration retry is admitted. Initial activation checks precede operator sends."],"activation":["Recreate only selected API/Web using newly verified local images, no pull/restart of preserved providers or databases.","Verify health and compiled/bundle equality through the existing gateway.","Public gateway config uses static upstream host resolution. After API/Web replacement, validate nginx config and gracefully reload only the existing gateway process so it resolves current API/Web container addresses; preserve its container/network/volume. Record health and served bundle after reload, not an old cached upstream. No provider/database restart.","If a new owned temporary HTTPS tunnel is needed, validate DNS/TLS/health/assets and then have operator update Meta callback/privacy URLs; no automatic provider configuration changes."],"assisted_proof":["Operator logs in normally; agent does not extract OWNER password or enumerate live business rows.","In the nonofficial BU, operator opens a consenting test contact with explicit DDI, previews and confirms one first text; recipient replies.","In the official BU, operator selects the already-approved own-account text template through the shared catalog, fills fictitious/test values, previews and confirms once; recipient replies.","Record only safe outcome/state/timestamps and source-runtime attestation. Do not persist phone/contact/body/token.","No automated sends, new contacts, routing changes, migration/registration at Meta, or Railway deployment."],"current_status":"E74 actual complete967pass, full259source/93browser proof,18actualmetrics/CI23controls/4PCV lanes and current offline images independently verified. Three fresh r7 reviews are being prepared; all material findings must resolve first. No preserved-local activation or full private-boundary diff inspection approval yet.","build_context_positive_inputs":{"api":{"roots":["api-app/src","api-app/prisma"],"exact_files":["api-app/Dockerfile","api-app/package.json","api-app/package-lock.json","api-app/tsconfig.json","api-app/tsconfig.build.json","api-app/nest-cli.json","api-app/docker/entrypoint.sh"]},"web":{"roots":["web-app/src"],"exact_files":["web-app/Dockerfile","web-app/package.json","web-app/package-lock.json","web-app/tsconfig.json","web-app/vite.config.ts","web-app/index.html","web-app/nginx/default.conf.template","web-app/docker/40-config-js.sh","web-app/public/config.js","web-app/public/privacidade.html"]},"policy":"Reject symlinks; hash each positive input, produce generated archive only. Exclude every .env, node_modules, existing dist, e2e/test artifacts and all unlisted paths. Add no extra file by discovery or implicit COPY context. Source specs under admitted src remain public build inputs; build exclusions remain canonical."},"prepared_build_context_receipt":"positive-build-contexts-e74-v1.1.json","entrypoint_scope":"Existing API entrypoint mechanically keeps ownership of the preserved named file volume at /dados/arquivos, then runs as node. No host .local-files bind, agent content inspection, payload mutation or file deletion is proposed.","candidate_receipt":"all-result-e74-v1.1.json","build_context_current_recheck":"image-build-root-collection-e74-v1.1.json","concrete_images":{"api":{"tag":"leadshug-stcon04-api:e74","image_id":"sha256:092005eb90275c3ab55e14c6ff2fe5fde241d4bde15324ce84bfb21f0a11c2f2","archive_sha256":"ec671cbe971395d1d4c2fe4f3cc99920fcb347d9ce5dc3c07ca154060ea042db"},"web":{"tag":"leadshug-stcon04-web:e74","image_id":"sha256:9787da8f734123e4f2875ce9b47c7bb23b45a8d64bbba98a830d51dd05f9f53b","archive_sha256":"959355f4dfc16824cdc8a83632dfda673c8ba71a7d8170d055164e89180152c7"}},"concrete_image_evidence":["positive-build-contexts-e74-v1.1.json","image-build-attestation-e74-v1.1.json","image-build-root-collection-e74-v1.1.json"],"current_source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","current_web_bundle_sha256":"f8e97efa6777dbc496b74cd527b1bae78e7766e4a4d58f752f7816cb62444343","recorded_at_utc":"2026-10-23T12:35:55.710536+00:00","historical_images":"E71/E64 images are historical. Only the exact corrected E74 API and verified equivalent Web ID below are proposed for activation.","approved_additive_migration_inputs":[{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","sha256":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437"},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","sha256":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a"},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","sha256":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544"}],"canonical_guard_private_exception":{"status":"not approved; not executed","purpose":"One exact canonical full read-only TODO diff guard at final validation; its Git enumeration may list/stat/read/hash actual private paths, unlike the permitted positive-only collectors.","command":"python3 delphi-ai/tools/todo_diff_expectation_guard.py foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md --repo-root /mnt/c/unifast/leadshug/leadshug_now_docker --json-output /tmp/stcon04-final-diff-guard-private.json","restrictions":"Raw output remains0600owned/tmp; report only counts/codes/hashes/outcome. No manual env/token reads, private-file edits/deletions, business-row or process/env/log inspection. Stop and classify actual violations; do not prune the guard or remove private files to make it pass.","governing_boundary":"TODO Out of Scope forbids private file enumeration/stat/hash/traversal; VAL-08 separately gates preserved-local activation. These are exact exceptions for a later bounded human approval, not inferred code approval."},"readiness_stop_conditions":["Expected project/service/labels/images/volumes differ or gateway ownership is not established by selected safe metadata.","Pending migration set/checksums differ from the three approved inputs, or any migration lock/statement/status check fails; no automatic retry/reset/resolve/down.","Current source fingerprint, built API, served Web, native health or TLS/DNS binding fails.","A private config edit or provider/routing/registration change is needed; prepare exact separate change instead of inspecting secrets.","Any unresolved material current review finding, missing approved same-account template or unavailable consensual test contact prevents the corresponding real proof."],"approval_bundle":"Only after all already-authorized candidate/review work is concrete: preserve data/peers and activate these two images, apply only the three exact additive migrations, safe gateway reload and owned HTTPS, opaque existing .env.testing Compose input, operator-driven own-channel first sends/replies, plus the one canonical read-only full diff guard exception. No Railway/product Git/provider routing or automated recipient contact.","current_proof_evidence":["all-result-e74-v1.1.json","all-source-recheck-e74-v1.1.json","browser-freshness-collection-e74-v1.1.json","current-synthetic-pcv-samples-e74-v1.1.json","implementation-r6-resolution-e74-v1.1.json","seal-metadata-provenance-e74-v1.1.json"],"current_reviews":"Pending fresh r7 architecture/security, full eight-section TQA and cutover; the plan is concrete input for that review, not a verdict.","governing_explicit_approval_reason":{"todo":"foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md","validation_step":"VAL-08 — local source-bound API/Web activation and owned stable/temporary HTTPS only under later approved runtime plan","private_boundary_quote":"Ler/listar/stat/hash/traversar/montar api-app/.local-files/, .env ou .env.testing; ler argumentos/process env/logs/linhas de negócio.","meaning":"Original implementation approval excludes these surfaces. Only the precisely proposed opaque Compose test input and one full canonical read-only diff guard are requested exceptions; no manual secret inspection or business-row inspection."},"new_migration_count":3,"related_inherited_migration_note":"The offline image attests four related hashes including the inherited ST06 window index. Only the three exact20261022 additive migrations listed here may be applied; the fourth is not new authorization."}
```

### pcv-eps-e74-v1.1.json

SHA256 `394d50914ecb7b4ba80b60615ec80fb823c153fad1fdb101f24b03668042748a`

```json
{"policy_schema_version":"pcv-1","schema_version":"pcv-1","todo_id":"ST-CON-04","run_id":"E74-canonical-all-66605","environment_id":"owned-disposable-node22-postgresql16-real-BFF-fake-external-provider","executor_id":"stcon04_continuation","reviewer_id":"root-independent-source-and-output-collector; formal lane assessment pending","recorded_at_utc":"2026-10-23T12:20:40.734967+00:00","lane_id":"EPS","evidence_type":"explain-and-query-log","sample_profile_id":"EPS-SP-STRONG","acceptance_rule_id":"EPS-A2","result_summary":"Disposable PostgreSQL EXPLAIN and bounded projection counts satisfy the declared page/query shape; no N+1 credential/provider probe.","artifact_payload":{"evidence_receipt":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","terminal_exit_code":0,"assessment_status":"Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.","access_pattern_classification":"Scoped exact open/intent/admission lookups and batched indexed page projection of current-resource trusted IN timestamps. Empty-conversation ordering uses additive expression index.","touched_path_audit_summary":{"list_order_fixture_conversations":15000,"list_returned_rows":50,"out_heavy_fixture_conversations":60,"out_heavy_returned_rows":50,"conversation_query_count":3,"standalone_message_hydration_query_count":0,"counts_limit":"Three queries touching conversations, not total SQL count.","trusted_window_fixture_conversations":30,"history_rows_per_conversation":24,"current_resource_batch_counts":{"buChannelFindMany":1,"channelCredentialFindMany":1,"latestAnyMessageProjection":1,"latestInboundWindowProjection":1},"provider_probe_count":0},"strong_query_evidence_type":"EXPLAIN ANALYZE BUFFERS plus Prisma query-event counts","inbox_order":{"rowCount":50,"plan":"Limit  (cost=0.41..9.32 rows=50 width=45) (actual time=0.015..0.030 rows=50 loops=1)\n  Buffers: shared hit=7\n  ->  Index Scan using conversations_inbox_order_idx on conversations  (cost=0.41..2673.78 rows=15000 width=45) (actual time=0.014..0.025 rows=50 loops=1)\n        Index Cond: ((bu_id = '53f7244c-a018-4cb6-b02b-1ee25b35a320'::text) AND (contact_type = 'PESSOA'::\"ContactType\"))\n        Filter: (status = 'QUEUED'::\"ConversationStatus\")\n        Buffers: shared hit=7\nPlanning:\n  Buffers: shared hit=70\nPlanning Time: 0.222 ms\nExecution Time: 0.043 ms"},"trusted_window":{"policy_schema_version":"pcv-1","lane_id":"EPS","trigger_result":"required","trigger_severity":"medium","trigger_reason_code":"EPS-DATA-PATH-CHANGED","gate_deadline":"before_local_implemented","min_evidence_rule_id":"EPS-E2","acceptance_rule_id":"EPS-A2","sample_profile":"EPS-SP-STRONG","access_pattern_classification":"Public conversation page loads selected BU channels once, official credential metadata once, one bounded latest-any-message projection for returned page IDs, and one batched indexed selected-resource trusted Meta IN timestamp query when selected bindings require a window; no provider credentials are decrypted or probed.","pageConversations":30,"historyRowsPerConversation":24,"availabilitySample":[{"available":true,"reason":null,"windowOpen":true},{"available":true,"reason":null,"windowOpen":true},{"available":true,"reason":null,"windowOpen":true}],"queryCounts":{"buChannelFindMany":1,"channelCredentialFindMany":1,"latestAnyMessageProjection":1,"latestInboundWindowProjection":1},"elapsedMs":15.3134799999998,"explainLatestInboundProjection":[{"Plan":{"Node Type":"Nested Loop","Parallel Aware":false,"Async Capable":false,"Join Type":"Inner","Startup Cost":0.28,"Total Cost":93.94,"Plan Rows":30,"Plan Width":40,"Actual Startup Time":0.033,"Actual Total Time":0.227,"Actual Rows":30,"Actual Loops":1,"Inner Unique":false,"Shared Hit Blocks":90,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Function Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Function Name":"unnest","Alias":"requested","Startup Cost":0,"Total Cost":0.3,"Plan Rows":30,"Plan Width":32,"Actual Startup Time":0.005,"Actual Total Time":0.007,"Actual Rows":30,"Actual Loops":1,"Shared Hit Blocks":0,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},{"Node Type":"Limit","Parent Relationship":"Inner","Parallel Aware":false,"Async Capable":false,"Startup Cost":0.28,"Total Cost":3.1,"Plan Rows":1,"Plan Width":45,"Actual Startup Time":0.007,"Actual Total Time":0.007,"Actual Rows":1,"Actual Loops":30,"Shared Hit Blocks":90,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Index Only Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Scan Direction":"Backward","Index Name":"messages_conversation_trusted_window_idx","Relation Name":"messages","Alias":"message","Startup Cost":0.28,"Total Cost":70.87,"Plan Rows":25,"Plan Width":45,"Actual Startup Time":0.007,"Actual Total Time":0.007,"Actual Rows":1,"Actual Loops":30,"Index Cond":"((conversation_id = requested.conversation_id) AND (provider_resource_identity_id = '32619ceb-839d-463c-9502-40da2eec30c1'::text) AND (direction = 'IN'::\"MessageDirection\") AND (channel_origin = 'OFICIAL'::\"ChannelType\") AND (official_inbound_at IS NOT NULL) AND (official_inbound_at <= CURRENT_TIMESTAMP))","Rows Removed by Index Recheck":0,"Heap Fetches":30,"Shared Hit Blocks":90,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0}]}]},"Planning":{"Shared Hit Blocks":68,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},"Planning Time":0.272,"Triggers":[],"Execution Time":0.243}],"providerCallsBefore":{"meta":0,"evolution":0},"providerCallsAfter":{"meta":0,"evolution":0},"limits":"Disposable PostgreSQL and one bounded 30-conversation public page; local query count/plan observation, not a capacity or latency SLO claim."},"sources":[{"path":"api-app/test/conversation-start.e2e-spec.ts","sha256":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","sha256":"3825b0286f9906781e83666616caa05417647ee47c022763fc76e39a3c4ddca0"}],"bounded_existence_query":"New actual query-event regression asserts findFirst bounded existence instead of whole-history COUNT; no new path-specific EXPLAIN claim.","historical_plan_samples":"Existing exact EXPLAIN samples below are from E45; unchanged plan-test source executed again E71. They are historical samples, not relabeled current measured costs.","current_raw_metrics_reference":"current-synthetic-pcv-samples-e74-v1.1.json","latest_message_projection":{"policy_schema_version":"pcv-1","finding_id":"PERF-R3-01","trigger_result":"required","trigger_severity":"high","trigger_reason_code":"PUBLIC-LIST-NESTED-MESSAGE-HYDRATION","gate_deadline":"before_local_implemented","pageLimit":4,"returnedParents":4,"hasLookahead":true,"parentCount":25,"historyRowsPerConversation":500,"totalFixtureMessages":12500,"queryCounts":{"nestedMessageHydration":0,"boundedLatestMessageBatch":1},"measuredSqlShape":"\n        SELECT requested.conversation_id AS \"conversationId\",\n          latest.content,\n          latest.direction::text AS \"direction\",\n          latest.channel_origin::text AS \"channelOrigin\"\n        FROM unnest(ARRAY[$?,$?,$?,$?]::text[]) AS requested(conversation_id)\n        LEFT JOIN LATERAL (\n          SELECT candidate.content, candidate.direction, candidate.channel_origin\n          FROM (\n            (\n              SELECT message.id, message.content, message.direction, message.channel_origin, message.created_at\n              FROM messages AS message\n              WHERE message.conversation_id = requested.conversation_id AND message.direction = 'IN'\n              ORDER BY message.created_at DESC, message.id DESC\n              LIMIT 1\n            )\n            UNION ALL\n            (\n              SELECT message.id, message.content, message.direction, message.channel_origin, message.created_at\n              FROM messages AS message\n              WHERE message.conversation_id = requested.conversation_id AND message.direction = 'OUT'\n              ORDER BY message.created_at DESC, message.id DESC\n              LIMIT 1\n            )\n          ) AS candidate\n          ORDER BY candidate.created_at DESC, candidate.id DESC\n          LIMIT 1\n        ) AS latest ON TRUE\n      ","parameterCount":4,"plan":{"Plan":{"Node Type":"Nested Loop","Parallel Aware":false,"Async Capable":false,"Join Type":"Left","Startup Cost":0.83,"Total Cost":17.71,"Plan Rows":4,"Plan Width":114,"Actual Startup Time":0.047,"Actual Total Time":0.09,"Actual Rows":4,"Actual Loops":1,"Inner Unique":false,"Shared Hit Blocks":32,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Function Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Function Name":"unnest","Alias":"requested","Startup Cost":0,"Total Cost":0.04,"Plan Rows":4,"Plan Width":32,"Actual Startup Time":0.005,"Actual Total Time":0.006,"Actual Rows":4,"Actual Loops":1,"Shared Hit Blocks":0,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},{"Node Type":"Limit","Parent Relationship":"Inner","Parallel Aware":false,"Async Capable":false,"Startup Cost":0.83,"Total Cost":4.39,"Plan Rows":1,"Plan Width":70,"Actual Startup Time":0.02,"Actual Total Time":0.02,"Actual Rows":1,"Actual Loops":4,"Shared Hit Blocks":32,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Merge Append","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Startup Cost":0.83,"Total Cost":7.95,"Plan Rows":2,"Plan Width":70,"Actual Startup Time":0.02,"Actual Total Time":0.02,"Actual Rows":1,"Actual Loops":4,"Sort Key":["\"*SELECT* 1\".created_at DESC","\"*SELECT* 1\".id DESC"],"Shared Hit Blocks":32,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Subplans Removed":0,"Plans":[{"Node Type":"Subquery Scan","Parent Relationship":"Member","Parallel Aware":false,"Async Capable":false,"Alias":"*SELECT* 1","Startup Cost":0.41,"Total Cost":3.94,"Plan Rows":1,"Plan Width":70,"Actual Startup Time":0.012,"Actual Total Time":0.012,"Actual Rows":1,"Actual Loops":4,"Shared Hit Blocks":16,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Limit","Parent Relationship":"Subquery","Parallel Aware":false,"Async Capable":false,"Startup Cost":0.41,"Total Cost":3.93,"Plan Rows":1,"Plan Width":70,"Actual Startup Time":0.011,"Actual Total Time":0.011,"Actual Rows":1,"Actual Loops":4,"Shared Hit Blocks":16,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Index Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Scan Direction":"Backward","Index Name":"messages_conversation_direction_created_id_idx","Relation Name":"messages","Alias":"message","Startup Cost":0.41,"Total Cost":446.93,"Plan Rows":127,"Plan Width":70,"Actual Startup Time":0.011,"Actual Total Time":0.011,"Actual Rows":1,"Actual Loops":4,"Index Cond":"((conversation_id = requested.conversation_id) AND (direction = 'IN'::\"MessageDirection\"))","Rows Removed by Index Recheck":0,"Shared Hit Blocks":16,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0}]}]},{"Node Type":"Subquery Scan","Parent Relationship":"Member","Parallel Aware":false,"Async Capable":false,"Alias":"*SELECT* 2","Startup Cost":0.41,"Total Cost":3.98,"Plan Rows":1,"Plan Width":70,"Actual Startup Time":0.007,"Actual Total Time":0.007,"Actual Rows":1,"Actual Loops":4,"Shared Hit Blocks":16,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Limit","Parent Relationship":"Subquery","Parallel Aware":false,"Async Capable":false,"Startup Cost":0.41,"Total Cost":3.97,"Plan Rows":1,"Plan Width":70,"Actual Startup Time":0.007,"Actual Total Time":0.007,"Actual Rows":1,"Actual Loops":4,"Shared Hit Blocks":16,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Index Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Scan Direction":"Backward","Index Name":"messages_conversation_direction_created_id_idx","Relation Name":"messages","Alias":"message_1","Startup Cost":0.41,"Total Cost":402.65,"Plan Rows":113,"Plan Width":70,"Actual Startup Time":0.007,"Actual Total Time":0.007,"Actual Rows":1,"Actual Loops":4,"Index Cond":"((conversation_id = requested.conversation_id) AND (direction = 'OUT'::\"MessageDirection\"))","Rows Removed by Index Recheck":0,"Shared Hit Blocks":16,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0}]}]}]}]}]},"Planning":{"Shared Hit Blocks":0,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},"Planning Time":0.205,"Triggers":[],"Execution Time":0.138},"simpleAllDirectionCandidatePlan":[{"Plan":{"Node Type":"Nested Loop","Parallel Aware":false,"Async Capable":false,"Join Type":"Left","Startup Cost":3.6,"Total Cost":26.73,"Plan Rows":4,"Plan Width":94,"Actual Startup Time":0.043,"Actual Total Time":0.083,"Actual Rows":4,"Actual Loops":1,"Inner Unique":false,"Shared Hit Blocks":19,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Function Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Function Name":"unnest","Alias":"requested","Startup Cost":0,"Total Cost":0.04,"Plan Rows":4,"Plan Width":32,"Actual Startup Time":0.002,"Actual Total Time":0.003,"Actual Rows":4,"Actual Loops":1,"Shared Hit Blocks":0,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},{"Node Type":"Limit","Parent Relationship":"Inner","Parallel Aware":false,"Async Capable":false,"Startup Cost":3.6,"Total Cost":6.65,"Plan Rows":1,"Plan Width":70,"Actual Startup Time":0.019,"Actual Total Time":0.019,"Actual Rows":1,"Actual Loops":4,"Shared Hit Blocks":19,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Incremental Sort","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Startup Cost":3.6,"Total Cost":739.02,"Plan Rows":241,"Plan Width":70,"Actual Startup Time":0.019,"Actual Total Time":0.019,"Actual Rows":1,"Actual Loops":4,"Sort Key":["message.created_at DESC","message.id DESC"],"Presorted Key":["message.created_at"],"Full-sort Groups":{"Group Count":4,"Sort Methods Used":["quicksort"],"Sort Space Memory":{"Average Sort Space Used":25,"Peak Sort Space Used":25}},"Shared Hit Blocks":19,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Index Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Scan Direction":"Backward","Index Name":"messages_conversation_id_created_at_idx","Relation Name":"messages","Alias":"message","Startup Cost":0.41,"Total Cost":728.6,"Plan Rows":241,"Plan Width":70,"Actual Startup Time":0.013,"Actual Total Time":0.014,"Actual Rows":2,"Actual Loops":4,"Index Cond":"(conversation_id = requested.conversation_id)","Rows Removed by Index Recheck":0,"Shared Hit Blocks":16,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0}]}]}]},"Planning":{"Shared Hit Blocks":0,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},"Planning Time":0.078,"Triggers":[],"Execution Time":0.094}],"messageScanSummary":[{"nodeType":"Index Scan","index":"messages_conversation_direction_created_id_idx","actualRows":1,"actualLoops":4,"rowsRemovedByIndexRecheck":0,"sharedHitBlocks":16,"sharedReadBlocks":0},{"nodeType":"Index Scan","index":"messages_conversation_direction_created_id_idx","actualRows":1,"actualLoops":4,"rowsRemovedByIndexRecheck":0,"sharedHitBlocks":16,"sharedReadBlocks":0}],"sortSummary":[],"actualRowsEmitted":8,"rowsRemovedByFilter":0,"rowsRemovedByIndexRecheck":0,"executionMs":0.138,"metricPrecision":"Actual Rows × Actual Loops is a per-node emitted-row total derived from PostgreSQL per-loop row counts, which EXPLAIN rounds; it is not rows visited. Removed-by-filter/recheck and buffer counters remain separate. Summarized elapsed time is rounded to 3 decimals while raw EXPLAIN is retained; no capacity claim.","limits":"Real public endpoint SQL and EXPLAIN ANALYZE on disposable PostgreSQL; bounded fixture evidence, no production capacity/latency SLO claim."},"out_heavy_history_scan":{"finding_id":"PERF-01","policy_schema_version":"pcv-1","fixture":{"conversations":500,"outSuffixLength":500,"hasOlderInbound":true,"hasOutOnlyHistory":true,"equalTimeTie":true,"pageAtMaximum":true},"actual":{"rowsRemovedByFilter":0,"sharedHitBlocks":1502,"sharedReadBlocks":0,"executionMs":2.328,"scanNodes":[{"type":"Index Only Scan","relation":"messages","actualRows":0,"loops":500,"index":"messages_conversation_direction_created_id_idx","indexCondition":"((conversation_id = requested.conversation_id) AND (direction = 'IN'::\"MessageDirection\"))"}]},"plan":[{"Plan":{"Node Type":"Nested Loop","Parallel Aware":false,"Async Capable":false,"Join Type":"Inner","Startup Cost":0.41,"Total Cost":2001.92,"Plan Rows":500,"Plan Width":40,"Actual Startup Time":0.051,"Actual Total Time":2.313,"Actual Rows":2,"Actual Loops":1,"Inner Unique":false,"Shared Hit Blocks":1502,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Function Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Function Name":"unnest","Alias":"requested","Startup Cost":0,"Total Cost":5,"Plan Rows":500,"Plan Width":32,"Actual Startup Time":0.026,"Actual Total Time":0.048,"Actual Rows":500,"Actual Loops":1,"Shared Hit Blocks":0,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},{"Node Type":"Limit","Parent Relationship":"Inner","Parallel Aware":false,"Async Capable":false,"Startup Cost":0.41,"Total Cost":3.97,"Plan Rows":1,"Plan Width":44,"Actual Startup Time":0.004,"Actual Total Time":0.004,"Actual Rows":0,"Actual Loops":500,"Shared Hit Blocks":1502,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0,"Plans":[{"Node Type":"Index Only Scan","Parent Relationship":"Outer","Parallel Aware":false,"Async Capable":false,"Scan Direction":"Backward","Index Name":"messages_conversation_direction_created_id_idx","Relation Name":"messages","Alias":"message","Startup Cost":0.41,"Total Cost":431.63,"Plan Rows":121,"Plan Width":44,"Actual Startup Time":0.004,"Actual Total Time":0.004,"Actual Rows":0,"Actual Loops":500,"Index Cond":"((conversation_id = requested.conversation_id) AND (direction = 'IN'::\"MessageDirection\"))","Rows Removed by Index Recheck":0,"Heap Fetches":2,"Shared Hit Blocks":1502,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0}]}]},"Planning":{"Shared Hit Blocks":66,"Shared Read Blocks":0,"Shared Dirtied Blocks":0,"Shared Written Blocks":0,"Local Hit Blocks":0,"Local Read Blocks":0,"Local Dirtied Blocks":0,"Local Written Blocks":0,"Temp Read Blocks":0,"Temp Written Blocks":0},"Planning Time":0.304,"Triggers":[],"Execution Time":2.328}],"limits":"Real disposable PostgreSQL EXPLAIN ANALYZE/BUFFERS with one older-IN history behind OUT rows and one OUT-only history; bounded fixture observation, not a production outage or capacity/SLO claim."},"current_window_scope":{"finding_id":"PERF-01","policy_schema_version":"pcv-1","selectedReference":{"conversationFound":true,"latestDirection":"recebida","requiresWindow":false,"available":true},"officialWindowBindingsPresentInBu":true,"latestInboundWindowQueries":0,"latestAnyMessageQueries":1,"expectedLatestInboundWindowQueries":0,"limits":"One real public-list request against disposable PostgreSQL; metadata batching remains operation-local."},"current_inbox_out_heavy_counts":{"rows":60,"listed":50,"conversationQueries":3,"messageQueries":0},"current_recovery_options_plans":{"recent":{"sql":"SELECT \"public\".\"initial_message_intents\".\"id\", \"public\".\"initial_message_intents\".\"conversation_id\", \"public\".\"initial_message_intents\".\"bu_id\", \"public\".\"initial_message_intents\".\"actor_id\", \"public\".\"initial_message_intents\".\"idempotency_key\", \"public\".\"initial_message_intents\".\"owner_nonce\", \"public\".\"initial_message_intents\".\"request_fingerprint\", \"public\".\"initial_message_intents\".\"request\", \"public\".\"initial_message_intents\".\"selected_context\", \"public\".\"initial_message_intents\".\"state\"::text, \"public\".\"initial_message_intents\".\"lease_expires_at\", \"public\".\"initial_message_intents\".\"dispatch_deadline_at\", \"public\".\"initial_message_intents\".\"external_message_id\", \"public\".\"initial_message_intents\".\"slot_released_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_by_actor_id\", \"public\".\"initial_message_intents\".\"created_at\", \"public\".\"initial_message_intents\".\"updated_at\" FROM \"public\".\"initial_message_intents\" WHERE (\"public\".\"initial_message_intents\".\"conversation_id\" = $1 AND \"public\".\"initial_message_intents\".\"bu_id\" = $2) ORDER BY \"public\".\"initial_message_intents\".\"created_at\" DESC, \"public\".\"initial_message_intents\".\"id\" DESC LIMIT $3 OFFSET $4","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1","f68505b5-e15f-4950-aa6c-2a98e053bdcd",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.28,"totalCost":4.02,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0},{"type":"Index Scan","relation":"initial_message_intents","index":"initial_message_intents_options_order_idx","startupCost":0.28,"totalCost":697.54,"estimatedRows":2048,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0}]},"active":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"conversation_id\", \"public\".\"dispatch_admissions\".\"bu_id\", \"public\".\"dispatch_admissions\".\"caller\"::text, \"public\".\"dispatch_admissions\".\"actor_id\", \"public\".\"dispatch_admissions\".\"owner_nonce\", \"public\".\"dispatch_admissions\".\"selected_context\", \"public\".\"dispatch_admissions\".\"state\"::text, \"public\".\"dispatch_admissions\".\"expires_at\", \"public\".\"dispatch_admissions\".\"dispatch_deadline_at\", \"public\".\"dispatch_admissions\".\"released_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_by_actor_id\", \"public\".\"dispatch_admissions\".\"created_at\", \"public\".\"dispatch_admissions\".\"updated_at\" FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"bu_id\" = $2 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $3 OFFSET $4","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1","f68505b5-e15f-4950-aa6c-2a98e053bdcd",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.27,"totalCost":14.25,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":8,"sharedReadBlocks":0},{"type":"Index Scan","relation":"dispatch_admissions","index":"dispatch_admissions_options_order_idx","startupCost":0.27,"totalCost":325.64,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":8,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, created_at DESC, id DESC, bu_id) WHERE (released_at IS NULL)","releasedHistory":2048,"activeHistory":256}},"current_claim_and_refresh_probes":{"ST04_ACTIVE_CONFLICT_PLAN ":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"state\"::text FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $2 OFFSET $3","params":["e7ddb4a0-2591-4f50-ab33-a5db0809a3d1",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.27,"totalCost":14.17,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0},{"type":"Index Scan","relation":"dispatch_admissions","index":"dispatch_admissions_options_order_idx","startupCost":0.27,"totalCost":323.72,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, created_at DESC, id DESC, bu_id) WHERE (released_at IS NULL)","providerPostDelta":0,"providerCallDelta":0,"messageDelta":0},"ST04_FINAL_WINDOW_CAS ":{"inspectedOpen":true,"expiresAt":"2026-10-23T11:56:54.450Z","databaseClockExpired":true,"databaseNow":"2026-10-23T11:56:54.456Z","postsDeltaWhilePaused":0,"postsDelta":0,"outMessagesDelta":0,"finalState":"REJECTED","leaseBudgetMs":90000},"ST04_ORDINARY_FINAL_WINDOW_CAS ":{"capturedEligible":true,"databaseWindowExpiredBeforeClaimUpdate":true,"claimGranted":false,"state":"PREPARED","dispatchDeadlineAt":null,"releasedAt":null},"ST04_CREDENTIAL_PIN ":{"validationSucceeded":true,"credentialUpdateWaited":true,"credentialVersionAdvanced":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":1,"sendStatus":201,"finalState":"SUCCEEDED"},"ST04_BU_READINESS_PIN ":{"validationSucceeded":true,"readinessUpdateWaited":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":0,"sendStatus":503,"buStatusAfterUpdate":"INATIVO","intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"},"ST04_ST05_CLAIM_OVERLAP ":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":409,"deadlocksDelta":0,"postsDelta":0,"outMessages":0,"intentState":"REJECTED","receiptState":"NONE"},"ST04_ST05_LOCAL_OVERLAP ":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":503,"deadlocksDelta":0,"postsDelta":1,"localOutMessages":0,"intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"}}},"artifact_sha256":"ae5aad222a6539464073000e92dc968d249558f24c5af7885099b3f9211aa451"}
```

### pcv-frc-e74-v1.1.json

SHA256 `818ee62c65785b3cdf1cf09dd8eca83e9e8781de11301bacb43a2ae967c47d5e`

```json
{"policy_schema_version":"pcv-1","schema_version":"pcv-1","todo_id":"ST-CON-04","run_id":"E74-canonical-all-66605","environment_id":"owned-disposable-node22-postgresql16-real-BFF-fake-external-provider","executor_id":"stcon04_continuation","reviewer_id":"root-independent-source-and-output-collector; formal lane assessment pending","recorded_at_utc":"2026-10-23T12:20:40.734967+00:00","lane_id":"FRC","evidence_type":"deterministic-real-browser-real-BFF-post-readback","sample_profile_id":"FRC-SP-H","acceptance_rule_id":"FRC-A1","result_summary":"Five independent first-send flows each receive20 synchronous open/confirm triggers; assertions require1open/1initialPOST/1provider invocation/1persistedOUT per flow.","artifact_payload":{"evidence_receipt":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","terminal_exit_code":0,"assessment_status":"Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.","concurrency_policy":"drop duplicate","burst_profile_observed":{"bursts":5,"triggers_per_burst":20,"open_requests_per_burst":1,"initial_posts_per_burst":1,"provider_invocations_per_burst":1,"persisted_out_per_burst":1,"observation_type":"Exact loop/assertions in current E74 test passed; not separately emitted metric trace."},"runner_or_manual_path":"bash scripts/test-channels-local.sh all -> Playwright start-conversation.spec.ts: cinco envios recebem vinte gatilhos síncronos cada sem duplicar o POST","additional_race_coverage":"Current E74 includes A-B-A, storage refusal, same-key replay, actual90s ordinary recovery, valid PREPARED and EALB successor/late-old UI proof. Current full run also passes held-old-BU busy-state fix and explicit snapshot-replay cleanup synchronized to browser completion.","sources":[{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"}],"limits":"Route delays a real BFF response after actual route.fetch(); external provider fake. No real WhatsApp/SLO claim.","per_action_policy":[{"action":"Manual open and initial confirmation","policy":"drop duplicate","proof":"Synchronous latches; five20-trigger browser waves with real BFF and one provider invocation/Message per flow."},{"action":"Preview/channel/BU/draft-dependent options and completion","policy":"last-write-wins","scope":"Only matching mounted owner/generation/conversation/draft; an older same-text A→B→A result cannot update newer ownership.","proof":"Delayed preview, context switches and late-body/completion browser cases passed E45."},{"action":"Initial read/reconcile/acknowledge","policy":"drop duplicate","scope":"Busy latch plus mounted owner/generation; explicit actions and immutable key/deadline.","proof":"Initial uncertainty/read and known-receipt local-reconcile browser cases passed E45; no provider operation."},{"action":"Ordinary recovery reconcile/acknowledge","policy":"drop duplicate","scope":"Same local action latch/owner fence; checkbox and immutable deadline required.","proof":"Dedicated actual E74 real BFF/browser case passed through actual90s risk acknowledgment and composer return."},{"action":"Saved snapshot reread","policy":"serialize","scope":"Explicit synchronous local storage read only; failed read blocks writes and preserves original key/body.","proof":"Causal E44 read-loss RED then E45 actual failed/successful local reread and same-key replay PASS."}],"current_raw_metrics_reference":"current-synthetic-pcv-samples-e74-v1.1.json","additional_actual_composer_wave_sample":{"waves":[{"requests":1,"retriggers":20,"outcome":"accepted","draftPreserved":false,"messageCount":1},{"requests":1,"retriggers":20,"outcome":"unknown","draftPreserved":true,"messageCount":1},{"requests":1,"retriggers":20,"outcome":"accepted","draftPreserved":false,"messageCount":1},{"requests":1,"retriggers":20,"outcome":"unknown","draftPreserved":true,"messageCount":1},{"requests":1,"retriggers":20,"outcome":"accepted","draftPreserved":false,"messageCount":1}],"limits":"Five real BFF/PostgreSQL submits held after the actual response; twenty user-form submit events per in-flight send; one request per wave; no capacity/SLO claim."}},"artifact_sha256":"0b1faaf809b4bed8721ee08179daf5458fce6e4c016172f537c0aeb68bd47bc3"}
```

### pcv-bci-e74-v1.1.json

SHA256 `65e424d1522b786408828f1593e875e618c6a9b0b4303d3b0a821a741f8ded34`

```json
{"policy_schema_version":"pcv-1","schema_version":"pcv-1","todo_id":"ST-CON-04","run_id":"E74-canonical-all-66605","environment_id":"owned-disposable-node22-postgresql16-real-BFF-fake-external-provider","executor_id":"stcon04_continuation","reviewer_id":"root-independent-source-and-output-collector; formal lane assessment pending","recorded_at_utc":"2026-10-23T12:20:40.734967+00:00","lane_id":"BCI","evidence_type":"real-concurrent-BFF-PG-barrier-and-state-readback","sample_profile_id":"BCI-SP-H","acceptance_rule_id":"BCI-A1","result_summary":"Five20-request same-key waves each persist one intent and one Message, dispatch once and return19 in-flight replays; manual open five20-request waves create five rows and send zero messages.","artifact_payload":{"evidence_receipt":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","terminal_exit_code":0,"assessment_status":"Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.","invariant_id":"ST04-one-owned-active-slot-and-at-most-one-POST-per-immutable-initial-intent","concurrency_policy":"idempotent same-key replay","probe_profile_observed":{"waves":5,"overlapping_requests_per_wave":20,"same_key_initial_waves":[{"wave":1,"requests":20,"replay202":19,"posts":1,"messages":1,"elapsedMs":182},{"wave":2,"requests":20,"replay202":19,"posts":1,"messages":1,"elapsedMs":170},{"wave":3,"requests":20,"replay202":19,"posts":1,"messages":1,"elapsedMs":162},{"wave":4,"requests":20,"replay202":19,"posts":1,"messages":1,"elapsedMs":160},{"wave":5,"requests":20,"replay202":19,"posts":1,"messages":1,"elapsedMs":154}],"manual_open":{"waves":5,"requests_per_wave":20,"created":5,"reused":95,"distinct_conversations":5,"provider_call_delta":0,"message_count":0}},"additional_barriers":"Ordinary-vs-initial admission, unique echo race, CAS owner/closed preservation, commit ACK loss versus rollback and after-deadline local risk acknowledgment passed actual PG suites. E74 also proves settlement rollback after provider ACK, EALB early/late acknowledgment and late-old isolation.","sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"},{"path":"api-app/test/conversation-start.e2e-spec.ts","sha256":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"}],"limits":"posts in ST04_BCI_5x20 are Evolution fake-port invocations, not external TCP requests. Durable external exactly-once is not claimed.","current_raw_metrics_reference":"current-synthetic-pcv-samples-e74-v1.1.json","manual_open_actual_emitted_sample":{"waves":5,"opensPerWave":20,"openCount":100,"createdCount":5,"reusedCount":95,"createdPerWave":[1,1,1,1,1],"statusCounts":{"200":95,"201":5},"providerCallDelta":0}},"artifact_sha256":"59a3d08a1f5f438913d66a086de95ae23cac0a949a91e44978d4315aff6b3d59"}
```

### pcv-rls-e74-v1.1.json

SHA256 `507e7790cf3aea01fef2c09ee53f6cabe3849ad72116bce10bd7bd2e0c59a0fd`

```json
{"policy_schema_version":"pcv-1","schema_version":"pcv-1","todo_id":"ST-CON-04","run_id":"E74-canonical-all-66605","environment_id":"owned-disposable-node22-postgresql16-real-BFF-fake-external-provider","executor_id":"stcon04_continuation","reviewer_id":"root-independent-source-and-output-collector; formal lane assessment pending","recorded_at_utc":"2026-10-23T12:20:40.734967+00:00","lane_id":"RLS","evidence_type":"bounded-disposable-one-stage-concurrent-load","sample_profile_id":"RLS-SP-L","acceptance_rule_id":"RLS-A1","result_summary":"Declared bounded stage of20 overlapping initial requests repeated five times stays below15000ms per wave; not a production capacity/SLO measurement.","artifact_payload":{"evidence_receipt":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","terminal_exit_code":0,"assessment_status":"Observed acceptance assertions passed; candidate evidence for independent assessment, no delivery/runtime/provider claim.","stage_profile_observed":{"stages":1,"concurrency":20,"waves":5,"request_count":100,"request_type":"same-key BFF initial sends with held first provider operation"},"thresholds":{"wave_elapsed_ms_strictly_less_than":15000,"definition_time":"Predeclared expect(durationMs).toBeLessThan(15_000), present in frozen source before E45 runner."},"metrics_summary":{"elapsed_ms":[182,170,162,160,154],"max_elapsed_ms":182,"all_five_below_threshold":true,"per_wave_provider_invocations":1,"per_wave_persisted_OUT":1},"sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}],"limits":"Reuses explicitly bound BCI stage metrics as allowed by pcv-1; fake provider held by deterministic barrier. No throughput saturation, live provider latency or production SLO claim.","current_raw_metrics_reference":"current-synthetic-pcv-samples-e74-v1.1.json"},"artifact_sha256":"c0756caa6b9f768537a3ab457db9ebf98f806b7c750b99d122aab7057db9b94b"}
```

### test-quality-public-roots-e74-v1.1.json

SHA256 `8ceca6d20b90f37f0e6665918e028fc329dc7b12b0ecb66c33a457e96013364c`

```json
{"kind":"Complete current public-root static-signal scan receipt; dispositions and independent TQA pending","recorded_at_utc":"2026-10-23T12:20:53.430547+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","command":["bash","delphi-ai/tools/test_quality_audit.sh","--path","api-app/src","--path","api-app/test","--path","web-app/src","--path","web-app/e2e"],"exit_code":2,"actual_exit_code":2,"raw_sha256":"1a096a509c618914002d492fc97203c6520aea4a3d7b38a482218f77e84f72e3","stdout_sha256":"1a096a509c618914002d492fc97203c6520aea4a3d7b38a482218f77e84f72e3","counts":{"hard_bypass":5,"test_support":0,"auth_shortcut":0,"status_only":201,"no_exception_only":4,"ambient_subject_fallback":21,"di_override":0,"mock_hint":37},"durable_raw":"test-quality-public-roots-output-e74-v1.1.txt","individual_inventory":"test-quality-signal-inventory-e74-v1.1.json","individual_dispositions":"test-quality-signal-dispositions-e74-v1.1.json","remaining_signals":"All268 actual raw signals retain source-bound per-row root judgments; complete independent TQA challenge remains. Raw high/exit2 is unchanged.","limits":"Actual E74 full ALL0 and independent full259 source recheck, same-run93 browser freshness. Static scan is a separate public-root command, not ALL stdout, not current PCV, and not delivery proof.","raw_outcome_line":"Outcome heuristic: high","exact_test_focus_skip_crosscheck":{"exit_code":1,"matches":0,"scope":"Same four complete positive public roots; supplementary only."}}
```

### test-quality-signal-inventory-e74-v1.1.json

SHA256 `62ac33e33af4e71e570720bc6c769355422f3f33a7508073b5499ffdfbdc6457`

```json
{"kind":"Complete current canonical-pattern signal inventory; individual root adjudication required","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","raw_receipt_sha256":"62ac33e33af4e71e570720bc6c769355422f3f33a7508073b5499ffdfbdc6457","row_count":268,"counts":{"HARD_BYPASS":5,"TEST_ONLY_ROUTE":0,"AUTH_SHORTCUT":0,"STATUS_ONLY":201,"NO_EXCEPTION":4,"AMBIENT_SUBJECT_FALLBACK":21,"DI_OVERRIDE":0,"MOCK_HINT":37},"raw_scanner_exit_code":2,"raw_outcome_line":"Outcome heuristic: high","deduplication":"Complete row values are reproduced losslessly in the TQA encoded inventory section for the same selected source fingerprint; this bound summary removes only duplicate JSON serialization.","signal_ids":["HARD_BYPASS:api-app/src/domain/identity/usuarios.service.ts:51","HARD_BYPASS:api-app/src/domain/setor/setor.service.ts:35","HARD_BYPASS:api-app/src/domain/historico/atividades.service.ts:53","HARD_BYPASS:api-app/src/domain/inbox/historico.service.ts:38","HARD_BYPASS:api-app/src/domain/inbox/historico.service.ts:101","STATUS_ONLY:web-app/e2e/telas.spec.ts:18","STATUS_ONLY:web-app/e2e/telas.spec.ts:353","STATUS_ONLY:web-app/e2e/telas.spec.ts:379","STATUS_ONLY:web-app/e2e/number-onboarding.spec.ts:108","STATUS_ONLY:web-app/e2e/number-onboarding.spec.ts:162","STATUS_ONLY:web-app/e2e/number-onboarding.spec.ts:206","STATUS_ONLY:web-app/e2e/number-onboarding.spec.ts:273","STATUS_ONLY:web-app/e2e/timeline.spec.ts:9","STATUS_ONLY:web-app/e2e/timeline.spec.ts:41","STATUS_ONLY:web-app/e2e/timeline.spec.ts:43","STATUS_ONLY:web-app/e2e/timeline.spec.ts:153","STATUS_ONLY:web-app/e2e/timeline.spec.ts:212","STATUS_ONLY:web-app/e2e/timeline.spec.ts:235","STATUS_ONLY:web-app/e2e/timeline.spec.ts:256","STATUS_ONLY:web-app/e2e/timeline.spec.ts:281","STATUS_ONLY:web-app/e2e/timeline.spec.ts:301","STATUS_ONLY:web-app/e2e/timeline.spec.ts:365","STATUS_ONLY:web-app/e2e/timeline.spec.ts:376","STATUS_ONLY:web-app/e2e/timeline.spec.ts:445","STATUS_ONLY:web-app/e2e/timeline.spec.ts:516","STATUS_ONLY:web-app/e2e/timeline.spec.ts:717","STATUS_ONLY:web-app/e2e/timeline.spec.ts:718","STATUS_ONLY:web-app/e2e/channel-transport.spec.ts:7","STATUS_ONLY:web-app/e2e/channel-transport.spec.ts:143","STATUS_ONLY:web-app/e2e/channel-transport.spec.ts:206","STATUS_ONLY:web-app/e2e/channel-transport.spec.ts:209","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:8","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:105","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:137","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:182","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:208","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:220","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:226","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:231","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:243","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:249","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:280","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:344","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:353","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:460","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:481","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:513","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:558","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:574","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:589","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:669","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:698","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:722","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:750","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:758","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:783","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:790","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:798","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:815","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:823","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:839","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:843","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:851","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:855","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:879","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:887","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:901","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:904","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:911","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:919","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:944","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:948","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:956","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:968","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:980","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:1004","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:1091","STATUS_ONLY:web-app/e2e/start-conversation.spec.ts:1125","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:83","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:152","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:180","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:187","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:191","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:261","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:287","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:294","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:382","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:394","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:403","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:491","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:506","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:520","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:523","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:561","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:586","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:622","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:634","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:663","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:666","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:678","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:761","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:769","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:787","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:799","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:888","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:897","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:905","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:914","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:916","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1034","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1042","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1050","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1059","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1061","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1132","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1165","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1169","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1252","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1286","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1303","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1315","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1321","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1336","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1345","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1361","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1374","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1379","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1391","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1415","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1435","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1488","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1498","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1535","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1572","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1596","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1612","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1627","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1633","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1698","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1812","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1934","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1941","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1954","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1956","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:1992","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2003","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2013","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2047","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2066","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2080","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2107","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2118","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2133","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2202","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2209","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2224","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2242","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2264","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2367","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2377","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2389","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2404","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2431","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2514","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2521","STATUS_ONLY:web-app/e2e/message-templates.spec.ts:2532","STATUS_ONLY:api-app/test/surfaces.e2e-spec.ts:28","STATUS_ONLY:api-app/test/surfaces.e2e-spec.ts:34","STATUS_ONLY:api-app/test/number-onboarding-typebot.e2e-spec.ts:82","STATUS_ONLY:api-app/test/number-onboarding-typebot.e2e-spec.ts:108","STATUS_ONLY:api-app/test/number-onboarding-typebot.e2e-spec.ts:126","STATUS_ONLY:api-app/test/number-onboarding-pcv.e2e-spec.ts:562","STATUS_ONLY:api-app/test/atendimento.e2e-spec.ts:235","STATUS_ONLY:api-app/test/atendimento.e2e-spec.ts:284","STATUS_ONLY:api-app/test/atendimento.e2e-spec.ts:677","STATUS_ONLY:api-app/test/dispatch-admission.e2e-spec.ts:715","STATUS_ONLY:api-app/test/number-onboarding-flow.e2e-spec.ts:377","STATUS_ONLY:api-app/test/number-onboarding-flow.e2e-spec.ts:687","STATUS_ONLY:api-app/test/number-onboarding-flow.e2e-spec.ts:895","STATUS_ONLY:api-app/test/number-onboarding-bci.e2e-spec.ts:58","STATUS_ONLY:api-app/test/number-onboarding-bci.e2e-spec.ts:80","STATUS_ONLY:api-app/test/number-onboarding-bci.e2e-spec.ts:139","STATUS_ONLY:api-app/test/api-publica.e2e-spec.ts:305","STATUS_ONLY:api-app/test/api-publica.e2e-spec.ts:315","STATUS_ONLY:api-app/test/initial-message.e2e-spec.ts:473","STATUS_ONLY:api-app/test/initial-message.e2e-spec.ts:682","STATUS_ONLY:api-app/test/initial-message.e2e-spec.ts:698","STATUS_ONLY:api-app/test/initial-message.e2e-spec.ts:1320","STATUS_ONLY:api-app/test/initial-message.e2e-spec.ts:1401","STATUS_ONLY:api-app/test/initial-message.e2e-spec.ts:1468","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:409","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:415","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:430","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:431","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:450","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:487","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:508","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:522","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:523","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:542","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:543","STATUS_ONLY:api-app/test/message-template-management.e2e-spec.ts:610","STATUS_ONLY:api-app/test/channel-transport.e2e-spec.ts:304","STATUS_ONLY:api-app/test/channel-transport.e2e-spec.ts:305","STATUS_ONLY:api-app/test/channel-transport.e2e-spec.ts:344","STATUS_ONLY:api-app/test/channel-transport.e2e-spec.ts:430","NO_EXCEPTION:api-app/src/infra/config/modulos.spec.ts:39","NO_EXCEPTION:api-app/src/infra/config/modulos.spec.ts:43","NO_EXCEPTION:api-app/src/infra/config/modulos.spec.ts:54","NO_EXCEPTION:api-app/src/infra/config/modulos.spec.ts:76","AMBIENT_SUBJECT_FALLBACK:web-app/e2e/timeline-freshness.ts:92","AMBIENT_SUBJECT_FALLBACK:api-app/test/dispatch-admission.e2e-spec.ts:431","AMBIENT_SUBJECT_FALLBACK:api-app/test/initial-message.e2e-spec.ts:58","AMBIENT_SUBJECT_FALLBACK:api-app/test/initial-message.e2e-spec.ts:72","AMBIENT_SUBJECT_FALLBACK:api-app/test/initial-message.e2e-spec.ts:84","AMBIENT_SUBJECT_FALLBACK:api-app/test/initial-message.e2e-spec.ts:96","AMBIENT_SUBJECT_FALLBACK:api-app/test/initial-message.e2e-spec.ts:327","AMBIENT_SUBJECT_FALLBACK:api-app/test/atendimento.e2e-spec.ts:215","AMBIENT_SUBJECT_FALLBACK:api-app/test/atendimento.e2e-spec.ts:261","AMBIENT_SUBJECT_FALLBACK:api-app/src/integrations/channels/prisma-channel-resolver.ts:443","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/outbound.service.ts:500","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/dispatch-admission.service.ts:610","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/dispatch-admission.service.ts:621","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/dispatch-admission.service.ts:715","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/dispatch-admission.service.ts:741","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/dispatch-admission.service.ts:742","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/message-acceptance.service.ts:77","AMBIENT_SUBJECT_FALLBACK:api-app/src/domain/inbox/message-acceptance.service.ts:221","AMBIENT_SUBJECT_FALLBACK:api-app/src/surfaces/bff/conversations.controller.ts:224","AMBIENT_SUBJECT_FALLBACK:api-app/src/surfaces/bff/conversations.controller.ts:242","AMBIENT_SUBJECT_FALLBACK:api-app/src/surfaces/bff/message-templates.controller.ts:162","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:402","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:730","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:752","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:803","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:850","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:922","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:998","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:1580","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:1983","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:2057","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:2152","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:2223","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:2231","MOCK_HINT:api-app/test/message-template-management.e2e-spec.ts:2352","MOCK_HINT:api-app/test/message-template-bff.e2e-spec.ts:194","MOCK_HINT:api-app/test/message-template-bff.e2e-spec.ts:337","MOCK_HINT:api-app/test/number-onboarding-typebot.e2e-spec.ts:167","MOCK_HINT:api-app/test/number-onboarding-flow.e2e-spec.ts:112","MOCK_HINT:api-app/test/number-onboarding-flow.e2e-spec.ts:157","MOCK_HINT:api-app/test/number-onboarding-flow.e2e-spec.ts:915","MOCK_HINT:api-app/test/atendimento.e2e-spec.ts:140","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:151","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:550","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:670","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:981","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:1032","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:1113","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:1209","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:1279","MOCK_HINT:api-app/test/initial-message.e2e-spec.ts:1356","MOCK_HINT:api-app/test/dispatch-admission.e2e-spec.ts:541","MOCK_HINT:api-app/test/dispatch-admission.e2e-spec.ts:618","MOCK_HINT:api-app/test/dispatch-admission.e2e-spec.ts:677","MOCK_HINT:api-app/test/dispatch-admission.e2e-spec.ts:703","MOCK_HINT:api-app/test/dispatch-admission.e2e-spec.ts:730","MOCK_HINT:api-app/src/integrations/meta/initial-message.client.spec.ts:24","MOCK_HINT:api-app/src/domain/channels/transport/channel-initial-message.spec.ts:330"]}
```

### test-quality-signal-dispositions-e74-v1.1.json

SHA256 `2a300bd83329068b9d59013d29e6cf8495402ceb6067043886d74cae2d0815d1`

```json
{"kind":"Current source-bound static dispositions with explicit root row adjudication","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","raw_receipt_sha256":"2a300bd83329068b9d59013d29e6cf8495402ceb6067043886d74cae2d0815d1","row_count":268,"counts":{"production_pagination_not_test_skip":5,"fixture_precondition":7,"intermediate_status_with_state_or_ui_oracle":190,"fixture_control_precondition":3,"reachability_contract_only":1,"void_validation_positive_contract":4,"scoped_or_singleton_query_not_ambient_subject":15,"explicit_owned_fault_or_observation_boundary":43},"raw_scanner_exit_code":2,"raw_outcome_line":"Outcome heuristic: high","deduplication":"Complete row values are reproduced losslessly in the TQA encoded inventory section for the same selected source fingerprint; this bound summary removes only duplicate JSON serialization."}
```

### producer-consumer-crosswalk-e74-v1.1.json

SHA256 `d252d9827b22d28c9b7c9d0a539e18e54460d1c631b16c13ef61ac434ba03313`

```json
{"kind":"Current E74 full-execution producer-to-consumer crosswalk","recorded_at_utc":"2026-10-23T12:22:57.829870+00:00","source_seal":"all-source-seal-e74-v1.1.json","state":"Actual E74 canonical ALL terminal exit0 with full259 postseal; current execution metrics are in same-run receipt. This is test-only evidence and does not authorize product dispatch, runtime, or delivery.","rows":[{"id":"manual-open","producer":"ConversationStartService atomically returns created/reused row without send/read/claim/automation","consumers":["NovaConversa dialog POST and onOpened","Inbox selected manual conversation / truthful list order"],"exact_test_references":["api-app/test/conversation-start.e2e-spec.ts:25","api-app/test/conversation-start.e2e-spec.ts:64","api-app/test/conversation-start.e2e-spec.ts:153","api-app/test/conversation-start.e2e-spec.ts:177","web-app/e2e/start-conversation.spec.ts:74"],"consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json","browser-freshness-collection-e74-v1.1.json"],"historical_evidence":"E45 atomic PG5x20/no automation and real browser open/reuse passed; E46 corresponding browser regression passed.","evidence_and_limit":"Relevant API/PG/served-browser scenarios passed full E74. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."},{"id":"qualified-window","producer":"Verified signed Meta IN timestamp accepted only for current managed identity; Message.officialInboundAt nullable","consumers":["PrismaChannelResolver.inspectForConversation","PrismaChannelResolver.inspectManyForConversations via BFF/public listing","OutboundService ordinary BFF/PUBLIC/BOT","Initial text dispatch claim in transaction"],"exact_test_references":["api-app/src/domain/inbox/channel-window-policy.spec.ts","api-app/test/webhooks.e2e-spec.ts","api-app/test/number-onboarding-pcv.e2e-spec.ts","api-app/test/number-onboarding-typebot.e2e-spec.ts","api-app/test/api-publica.e2e-spec.ts","web-app/e2e/channel-transport.spec.ts"],"consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json","browser-freshness-collection-e74-v1.1.json"],"historical_evidence":"E45 signed timestamp/resource policy, BFF/public/BOT projected/send regressions and raw/substitution tests passed; public index/query counts in actual PCV receipt.","evidence_and_limit":"Relevant API/PG/served-browser scenarios passed full E74. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."},{"id":"shared-template-catalog","producer":"ST05 bounded catalog projector/lease/TTL remains owner; initial renderer consumes unchanged components","consumers":["Shared catalog route and PrimeiraMensagem template selector","Read-only local preview/escaped React text","Fresh same-account remote eligibility before new dispatch"],"exact_test_references":["api-app/src/domain/inbox/initial-message-template-renderer.spec.ts:18","api-app/src/domain/inbox/initial-message-template-renderer.spec.ts:64","api-app/test/initial-message.e2e-spec.ts:329","web-app/e2e/start-conversation.spec.ts:447"],"consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json","browser-freshness-collection-e74-v1.1.json"],"historical_evidence":"E45 renderer exact bounds/NAMED/POSITIONAL, real catalog refresh, escaped read-only preview, same-account fresh membership before dispatch passed. Protected authoring/catalog browser cases passed E46.","evidence_and_limit":"Relevant API/PG/served-browser scenarios passed full E74. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."},{"id":"abstract-channel-union","producer":"One Channel.sendMessage(text|approved-template), readonly supportedKinds, awaited operation fence","consumers":["OutboundService ordinary calls","Initial coordinator through same OutboundService","Meta adapter concrete formatter","Evolution adapter text-only typed refusal"],"exact_test_references":["api-app/src/domain/channels/transport/channel-dependencies.spec.ts","api-app/src/domain/channels/transport/channel-initial-message.spec.ts:46","api-app/src/domain/channels/transport/channel-initial-message.spec.ts:62","api-app/test/channel-transport.e2e-spec.ts"],"consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json","browser-freshness-collection-e74-v1.1.json"],"historical_evidence":"E45 dependency/substitution, Evolution typed zeroHTTP, raw Meta account/recipient protocol and ordinary BFF/public/BOT text regressions passed.","evidence_and_limit":"Relevant API/PG/served-browser scenarios passed full E74. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."},{"id":"durable-intent-outcome","producer":"Immutable original key/body/context and truthful persisted receipt/uncertainty/state projection","consumers":["Scoped BFF create/read/reconcile/ack routes with session+grant+CSRF","api.ts safe closed error metadata","PrimeiraMensagem explicit recovery/exact retry and actor+BU+conversation sessionStorage"],"exact_test_references":["api-app/test/dispatch-admission.e2e-spec.ts:165","api-app/test/dispatch-admission.e2e-spec.ts:196","api-app/test/initial-message.e2e-spec.ts:95","api-app/test/initial-message.e2e-spec.ts:206","web-app/e2e/start-conversation.spec.ts:198","web-app/e2e/start-conversation.spec.ts:266","web-app/e2e/start-conversation.spec.ts:599"],"consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json","browser-freshness-collection-e74-v1.1.json"],"historical_evidence":"E45 actual PG barriers/readback/CAS and browser read/reconcile/ACK, failed local storage read/write, lost-response original-key replay passed. E46 those browser cases pass.","evidence_and_limit":"Relevant API/PG/served-browser scenarios passed full E74. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."},{"id":"shared-admission-interlock","producer":"Ordinary per-owner tokens and exclusive initial slot use same conversation lock; no SENDING clock takeover","consumers":["BFF ordinary composer empty/unresolved gate","PUBLIC ordinary sender through ConversationsService","BOT ordinary sender through IncomingService","Initial reservation and explicit local risk release controls","OrdinaryRecovery actual scoped reconcile/acknowledge controls on reopened thread"],"exact_test_references":["api-app/test/dispatch-admission.e2e-spec.ts:328","api-app/test/dispatch-admission.e2e-spec.ts:367","api-app/test/dispatch-admission.e2e-spec.ts:379","api-app/test/dispatch-admission.e2e-spec.ts:434","api-app/test/dispatch-admission.e2e-spec.ts:457","api-app/test/channel-transport.e2e-spec.ts","api-app/test/api-publica.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts:531"],"consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json","browser-freshness-collection-e74-v1.1.json"],"historical_evidence":"E45 real PG races/ordinary concurrency, public/BOT and empty BFF mapping pass; E47 actual ordinary BFF browser uncertain send→reopen→reconcile→real90s risk ACK→composer return with unchanged provider/audit snapshots passed.","evidence_and_limit":"Relevant API/PG/served-browser scenarios passed full E74. Exact test file references remain source anchors; historical line numbers describe older source and are not asserted as current positions."},{"id":"prepared-safe-action","producer":"Valid durable PREPARED projected as RECONCILE, GET read-only","consumers":["PrimeiraMensagem existing local recovery action","Scoped BFF reconcile"],"exact_test_references":["api-app/test/initial-message.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"evidence_and_limit":"Current full E74: live202 unchanged slot then synthetic DB expiry local reject/release, zero provider/Message. Actual compiled reserveInitial fixture uses canonical request/fingerprint and90s lease.","consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json"]},{"id":"known-ack-local-blocked-risk-release","producer":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED safe state, immutable original deadline, scoped409 metadata","consumers":["Actual UI early acknowledgment409","Explicit after-deadline acknowledgment200","Successor and late-old local recovery"],"exact_test_references":["api-app/test/initial-message.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"evidence_and_limit":"E74 real BFF early ACK_TOO_EARLY409 leaves slot/provider/Message unchanged; synthetic disposable deadline expiry permits one successor, later original local completion never reacquires slot or changes current owner. No disabled-button requirement invented.","consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json"]},{"id":"unicode-contract","producer":"Server code-point limits4096 text/1024 template values","consumers":["NovaConversa input clamp","Scoped session snapshot restore","Escaped preview and actual initial POST"],"exact_test_references":["web-app/src/componentes/NovaConversa.spec.ts","web-app/e2e/start-conversation.spec.ts"],"evidence_and_limit":"E51 real positional snapshot RED precedes fix; E74 named and positional1024/1025 plus text4096/4097 unit bounds, actual4096-text and1024-positional browser input/preview/send. No separate named full-browser1024 claim.","consumer_state":"implemented + evidenced","actual_receipts":["all-result-e74-v1.1.json","web-result-e51-v1.1.json"]}],"external_proof_boundary":"Synthetic provider boundary plus real disposable BFF/PostgreSQL/browser. User attests own template APPROVED; same-account first-template actual send/reply and nonofficial first-send/reply are pending source-bound local activation.","assurance_boundary":"No full diff-guard, required implementation reviews, runtime activation or criterion checkbox promoted.","remaining_required_gates":["Fresh architecture/TQA/cutover assessment and material finding resolution","Concrete Alpine images then separately approved preserved-local activation/migrations/operator first-send/reply","Modules, full canonical diff inspection exception/guard and final closure gates"],"current_remediation_reference":"implementation-r6-resolution-e74-v1.1.json","prior_remediation_reference":"implementation-r2-r3-resolution-v1.1.json","rebind_method":"Current terminal fullALL, independent full259source postseal and93browser manifest binding. Historical-labelled evidence remains historical; source hashes in current path records rebound. Current automated proof does not close operator/runtime/module/review/guard gates.","current_r4_correction_proof":{"reference":"implementation-r4-resolution-e74-v1.1.json","same_run_pcv_reference":"pcv-eps-e74-v1.1.json","claim_window":"Both ordinary and initial SENDING CAS enforce captured trusted expiry against the actual DB clock.","mutable_context":"Actual BU/channel/credential pins and actor/grant NOWAIT fence preserve the approved lock order and fail closed under contention.","st05_overlap":"Actual unmodified ST05 refresh races at claim and known-acceptance local completion have zero deadlocks and retain truthful outcomes.","access_paths":"Actual captured-query EXPLAIN uses one partial ordered active-admission index for options and whole-conversation conflict and an ordered intent index; exact metrics are in current PCV."},"current_additional_crossings":["ST05 per-item availability→initial preview and new-submit guards; actual producer transition plus zero effects.","Captured ordinary outcome→local bookkeeping→safe legacy error/diagnostic owner; real PostgreSQL rollback.","BU selection→dialog key/unmount generation→held real BFF result; actual UI controls and stale-response fencing."],"source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","current_r6_correction_proof":{"artifact":"implementation-r6-resolution-e74-v1.1.json","sha256":"b437befd4b4b1915d2181b10d1f5681de077fc8216fde7559bf8d3a1be2e7c7b","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","finding_ids":["F-CF091066","F-5E961B39"],"resolution":{"kind":"Root resolution of both r6 causal findings against current full source-bound proof; independent r7 remains required","recorded_at_utc":"2026-10-23T12:20:47.197456+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","all_result":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","rows":[{"finding_id":"F-CF091066","source_finding_id":"ARCH-ST04-R6-01","severity":"medium","resolution":"Integrated","problem":"Current verified identity could qualify a trusted timestamp while its managed lifecycle was false.","correction":"Read managed_lifecycle in the existing same FOR SHARE identity projection; pass only that locked boolean to private timestamp qualification. Preserve Message/receipt acceptance; duplicate reconciliation never promotes a prior null timestamp. No extra query, caller flag, lock-order change or provider call.","sources":[{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","lines":[120,148,188,212],"sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/test/webhooks.e2e-spec.ts","lines":[123,144,149,152,163],"sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"}],"actual_proof_markers":["does not promote an inbound timestamp received while the current resource is unmanaged"],"actual_proof":"Signed-webhook/PG matrix passes: retained IN/unread and null trusted timestamp, closed window before/after lifecycle activation, duplicate without promotion, later new managed IN opens window, zero provider effects.","causal_evidence":"api-result-e72-v1.1.json","limits":"Actual E72 read-projection defect, not an outbound exploit or actual provider effect."},{"finding_id":"F-5E961B39","source_finding_id":"TQA-R6-01","severity":"medium","resolution":"Integrated","problem":"Native deadlock statistics silently defaulted to zero on invalid results.","correction":"Test helper requires exactly one row and a nonnegative native bigint; malformed/missing/ambiguous results fail the test. Real counter overlap probes remain.","sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","lines":[78,145,149,1280,1318,1357,1399],"sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}],"actual_proof_markers":["fails closed when native deadlock statistics are","ST04_ST05_CLAIM_OVERLAP ","ST04_ST05_LOCAL_OVERLAP "],"actual_proof":"All four isolated empty/malformed/multiple/negative fixtures reject; actual unchanged ST05-owner claim/local overlap probes pass with native zero-deadlock deltas.","causal_evidence":"api-result-e72-v1.1.json","limits":"One helper query is substituted once and restored in finally. This test-only helper does not authorize product dispatch; no actual missing native statistics are claimed."}],"r6_collection":"implementation-review-collection-r6-v1.1.json","test_first_boundary":"E72 actual test-only API RED reached four statistics failures and four lifecycle soft assertions before the two exact E73 fixes. E73 actual967pass/postseal/browser is retained; unchanged E74 repeats only to retain lost raw stdout/metrics. No earlier unreached assertion or actual outbound exploit is relabeled.","remaining":["Fresh complete eight-section TQA; terse r6 response insufficient","Current architecture/security/cutover and module review","Current offline images plus approved preserved runtime/operator/full-diff/final gates"],"boundary":"Positive public sources and owned synthetic evidence only; no private environment/business/provider inspection."},"status_note":"Root-authored resolution artifact reproduced as supplied; map rebinding does not independently adjudicate it."},"current_same_run_pcv_reference":{"artifact":"current-synthetic-pcv-samples-e74-v1.1.json","sha256":"75595b6d8884606d36279d02bce24a6f82bb2e695b72707bbd62be6018ca39ae","metric_count":18,"source_seal":"all-source-seal-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751"},"current_actual_all_result":{"artifact":"all-result-e74-v1.1.json","sha256":"e8c56ed6745b3a1d66f9bf2dde86704a5a58f8d936e1ff763f7e75b0e3386818","exit_code":0,"source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","phases":{"migrations":28,"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"duration_seconds":4.39},"api_postgresql":{"files":33,"tests":456,"duration_seconds":309.13},"web_unit":{"files":7,"tests":54,"duration_seconds":0.927},"browser":{"tests":89,"passed":89,"duration_minutes":16.2}}},"current_statistics_test_only_boundary":"Statistics helper metrics are test-only evidence and are not product dispatch authorization.","collection_rebinding_note":"Root corrected stale current-checkpoint strings/r4 refs/source hashes in the staged generic map. Historical-labelled/approved-criterion fields remain exact. Current rows bind actualE74 ALL/PCV/source/freshness; no measurement or closure is invented.","staged_original_sha256":"cab114f553f67ee5a12c8fd902f3dc9beace7227c33f5e2bb5203883146d5f24"}
```

### candidate-criterion-index-e74-v1.1.json

SHA256 `dad974d4ba2b8ffe6c771e47536d4dcb7a83b62b53f45d473c5f811551b2df83`

```json
{"kind":"Current E74 criterion-specific full execution index; not delivery closure","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","execution_state":"Actual E74 canonical ALL terminal exit0 with full259 postseal; current execution metrics are in same-run receipt. This is test-only evidence and does not authorize product dispatch, runtime, or delivery.","interpretation":"Exact approved criterion wording is retained. Current full execution replaces former composite proof; no claim that these checkboxes are closed before independent reviews/runtime/modules/guards.","criteria":[{"criterion_id":"DOD-01","approved_criterion":"opening invokes no automation; manual-open-without-send then first inbound leaves NOVA_CONVERSA false while keyword automation retains its predicate; authorized operator opens/reuses BU/contact atomically; no side effects listed in SCOPE-01 occur; new conversation has truthful empty state and deterministic list ordering.","candidate_source_references":["api-app/test/conversation-start.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"proof_target":["Atomic open/reuse,5x20 open requests, no trigger on open/first IN and separate keyword case.","Browser empty-open and reuse-before-send audit."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["API atomic5x20/empty-state/keyword and NOVA_CONVERSA cases plus browser create/reuse pass. Independent exact criterion review remains."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."],"current_additional_proof":"Actual BU-change held old response now leaves current dialog controls usable; old result cannot close/select into current BU."},{"criterion_id":"DOD-02","approved_criterion":"stale/foreign BU, actor, slot, selected channel, grant, credential epoch/version, conversation generation, template fingerprint, or policy context fails closed before external dispatch.","candidate_source_references":["api-app/src/domain/channels/transport/channel-initial-message.spec.ts","api-app/test/initial-message.e2e-spec.ts","api-app/test/dispatch-admission.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"proof_target":["Nine-field immutable-context mismatch unit matrix.","BFF forged grant/current session/grant/preflight deadline and owner/close fences.","Browser stale A-B-A preview and permission recovery."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Nine-field mismatch, forged-tenant/session/grant/remote preflight fences and browser A-B-A pass; independent security/adherence remains."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."]},{"criterion_id":"DOD-03","approved_criterion":"Preview is escaped, deterministic, local/read-only and context-bound; supported textual subset and exact limits are enforced server-side.","candidate_source_references":["api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","api-app/src/domain/inbox/initial-message.service.spec.ts","api-app/test/initial-message.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"proof_target":["NAMED/POSITIONAL ordering/repeats/static component order/unsupported subset.","Local preview and changed-context preAdmission rejection.","React preview and explicit confirmation."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["New exact renderer4096/4097,1024/1025 Unicode and20/21 parameter bounds pass; escaped inert markup/read-only preview passes. Independent assessment remains."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable.","Server and snapshot code-point bounds plus actual Unicode browser input/preview/send passed; separate JSON storage guard remains."]},{"criterion_id":"DOD-04","approved_criterion":"existing Channel consumers remain substitutable; Meta supports declared text/template kinds; Evolution template is typed unsupported with zero HTTP; no second send method/provider branching outside adapters or DI cycle; immutable descriptor plus same-operation fence preserves common dispatch.","candidate_source_references":["api-app/src/domain/channels/transport/channel-dependencies.spec.ts","api-app/src/domain/channels/transport/channel-initial-message.spec.ts","api-app/test/channel-transport.e2e-spec.ts"],"proof_target":["Inherited sealed dependency harness; union substitution and unsupported Evolution0HTTP.","Ordinary legacy text and initial protocol in same bound Channel."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Dependency/substitution/typed Evolution0HTTP/raw Meta union/text regressions pass; independent architecture/cutover remains."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."],"current_additional_proof":"Actual ST05 individually unavailable APPROVED observation is rejected at preview/newsubmit, before intent/provider/OUT; authoring flags stay independent."},{"criterion_id":"DOD-05","approved_criterion":"prove commit certainty at reservation/dispatch-claim/receipt/release, including real commit with lost ACK and real rollback; every remote eligibility/grant/phone GET completes before durable SENDING claim; the abstract fence CAS-claims immediately before one POST, and expiry of PREPARED during delayed preflight produces zero POST. Each initial attempt dispatches at most one POST; failures are classified truthfully; known provider ID is durably separate from local Message; recovery never contacts provider and never creates a Message without external ID.","candidate_source_references":["api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"proof_target":["Actual PG commit-with-lost-ACK versus actual rollback at reservation/claim/receipt/release/completion.","Delayed remote GET expiry0POST, bounded protocol and same-key5x20.","Browser unknown response, reload and same-key replay/storage failure."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Actual PG commit/rollback distinction and browser E44 causal read-failure RED -> E45 full GREEN pass; exact replay preserves1effect/Message. No external exactly-once claim; independent assessment remains."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."],"current_additional_proof":"Captured ordinary transport outcome and ACK_WITHOUT_ID diagnostic survive real local settlement rollback/readback uncertainty."},{"criterion_id":"DOD-06","approved_criterion":"initial transaction locks identity then conversation, checks original pre-HTTP status/owner CAS before acceptance mutates updatedAt, permits eligible acceptance when status CAS fails, and recovers unique conflict by whole-local-transaction rollback/readback/re-entry at most once; MessageAcceptance remains sole Message owner and existing sender/error behavior is preserved; CAS prevents late initial outcome from changing concurrent claim/close/owner or reacquiring released slot. Initial acknowledgment in either allowed state waits for immutable dispatchDeadlineAt; before it409 ACK_TOO_EARLY and zero release.","candidate_source_references":["api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts","api-app/src/domain/inbox/dispatch-admission.service.spec.ts","api-app/src/domain/inbox/message-acceptance.service.spec.ts"],"proof_target":["Original owner/status CAS, competing echo P2002 in local reconciliation, known receipt local completion.","Risk ACK before/after DB deadline; exact deadline-1/equality/+1 deterministic unit predicate."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Actual PG owner/CAS/whole-tx P2002/readback/local retry and irreversible deadline release cases pass. Exact equality is deterministic unit proof, not PG wall-clock equality. Independent transaction assessment remains."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable.","Actual BFF/UI EALB early409 and after synthetic expiry200, successor/late-old isolation passed; ordinary recovery separately waited actual90s."]},{"criterion_id":"DOD-07","approved_criterion":"official window uses only qualified trusted Meta IN timestamp for selected resource; all current BFF/public/BOT availability and send policy consumers use the same rule; timeline/cursors and performance bounds hold.","candidate_source_references":["api-app/src/domain/inbox/channel-window-policy.spec.ts","api-app/test/webhooks.e2e-spec.ts","api-app/test/number-onboarding-pcv.e2e-spec.ts","api-app/test/number-onboarding-typebot.e2e-spec.ts","api-app/test/api-publica.e2e-spec.ts","web-app/e2e/channel-transport.spec.ts"],"proof_target":["Signed timestamp provenance, duplicate immutability, selected resource strict24h.","Single inspect/inspectMany boundary, batched public projection and OUT-heavy/no-IN EXPLAIN.","Preserved timeline/cursor suites included in all."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Signed timestamp/current-resource, BFF/PUBLIC/BOT/window projections and full timeline/cursor regressions pass; SQL/index query bounds measured. Independent cross-consumer assessment remains."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."]},{"criterion_id":"DOD-08","approved_criterion":"owner-scoped ordinary admissions and exclusive initial reservation serialize under the same conversation lock without serializing ordinary-versus-ordinary sends; uncertain dispatched tokens block initial reservation until settlement or explicit risk acknowledgment, never time takeover; late owner release cannot touch successor; existing composer is blocked before HTTP for new/empty/unresolved slot; public/BOT respect slot and retain existing mappings; text regressions pass.","candidate_source_references":["api-app/src/domain/inbox/outbound.service.spec.ts","api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/channel-transport.e2e-spec.ts","api-app/test/atendimento.e2e-spec.ts","api-app/test/api-publica.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"proof_target":["Ordinary per-owner overlap and exclusive initial slot; SENDING never time takeover.","BFF empty gate, PUBLIC/BOT mappings, owner-scoped settlement and late release.","Browser empty/unresolved composer block and risk controls."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Actual ordinary browser send/reopen/reconcile/risk ACK after90s/composer return passes E47; API/PG public/BOT interlock regressions pass E45. Current full E47 regression/independent assessment still pending."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."],"current_additional_proof":"Same captured-outcome interlock/diagnostic regression passes; no provider retry or slot release is fabricated."},{"criterion_id":"DOD-09","approved_criterion":"NAMED and POSITIONAL initial support is derived by the initial text renderer from the unchanged catalog components/format, independently of inherited authoring flags; exact full context binds management descriptor to selected transport and final text-window fence; current eligibility is checked before every new official template dispatch via bounded same-account reads; template is actually APPROVED; Meta request pins server-captured `messaging_account_id`, uses `+` plus full DDI, and preserves existing ordinary text semantics. Tests cover same-country and cross-country recipients. Official raw reference receipt confirms account pin and recipient formatting; actual own-account readiness remains unverified.","candidate_source_references":["api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","api-app/src/domain/channels/transport/channel-initial-message.spec.ts","api-app/src/integrations/meta/initial-message.client.spec.ts","api-app/test/initial-message.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts"],"proof_target":["ST05 catalog flags remain unchanged; initial renderer independent.","Pinned account,+fullDDI,same/cross-country raw protocol,6GET/1POST upper case.","Negative current status/account/definition/membership bounds."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["API NAMED/POSITIONAL same-account tuple and raw recipient/account-pin cases + realBFF/browser POSITIONAL flow pass. Actual own-account approved template send/reply remains required."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."],"current_additional_proof":"Available POSITIONAL supported=false remains eligible for initial renderer; fresh page plus unavailable individual item rejects locally; new remote preflight limits unchanged."},{"criterion_id":"DOD-10","approved_criterion":"per actor/account limits, tenant isolation, request/deadline budgets and zero-network recovery are demonstrated with real bounded counters/barriers.","candidate_source_references":["api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts","api-app/src/integrations/meta/initial-message.client.spec.ts"],"proof_target":["10/min actor,60/h opaque canonical account, retained released attempts; forged grant rejection.","75s bounded preflight, immutable90s lease, no-retry provider counters, local-only recovery."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Real bounded actor/account quota/barriers/zero-network recovery pass. Independent security/PCV and same-source evidence assessment remain."],"remaining_or_limit":["Current relevant automated scenario passed full E74; independent criterion assessment remains. Runtime/own-account/operator/module/guard gates stay open as applicable."]},{"criterion_id":"DOD-11","approved_criterion":"additive migration passes explicit preflight and disposable local validation without reset/drop; current source/image/API freshness and approved local validation topology are proven.","candidate_source_references":["api-app/prisma/schema.prisma","api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","api-app/test/dispatch-admission.e2e-spec.ts","web-app/e2e/timeline-freshness.ts"],"proof_target":["Disposable migrate deploy/status; ST04 columns/native types/enum/constraints/index facts.","5s lock timeout/60s statement timeout; positive-public source pre/post seals."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Disposable28migrations deploy/status and bounded ST04 schema/index checks pass; served bundle/source manifest match. Actual preserved local image/native runtime/migration and approved activation remain."],"remaining_or_limit":["Disposable28migration/source/served-bundle proof passed. Actual Alpine images/preserved local activation/migration not executed."]},{"criterion_id":"DOD-12","approved_criterion":"assisted proof: operator sends first unofficial message, an actually APPROVED official template, receives a reply; no auto-contact; if eligible approved asset is unavailable, completion remains blocked.","candidate_source_references":[],"proof_target":["User reports own prior model APPROVED; human attestation only, not provider query or send."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Only human attestation of APPROVED template; actual first nonofficial send + official approved template send + replies remain unperformed."],"remaining_or_limit":["Actual own-resource first-send/reply, required modules/reviews/guards remain uncompleted; no delivery claim."]},{"criterion_id":"DOD-13","approved_criterion":"architecture/adherence/security/performance/TQA/final/cutover/debt and delivery guards pass at their required stages; no open P1/P2; constraints SEC-R6-04, OPS-R4-01, TQA-ST05-03 remain truthfully carried.","candidate_source_references":[],"proof_target":["Chronology/deviations E02/E04/E18/E35a and inherited SEC-R6-04/OPS-R4-01/TQA-ST05-03 explicitly preserved."],"state":"actual test proof indexed; criterion not closed","current_checkpoint":"all-result-e74-v1.1.json; browser-freshness-collection-e74-v1.1.json","historical_remaining_or_limit":["Independent implementation assessments, current full E47 terminal, canonical diff-guard inspection exception, module consolidation, actual local runtime/operator proof and final delivery gates remain."],"remaining_or_limit":["Fresh complete independent r7 challenge, actual own-channel/runtime proof, module consolidation, canonical private-boundary diff guard and final delivery checks remain; no current gate clearance inferred."]}],"validation_crosswalk":{"VAL-01":["DOD-01","DOD-04","DOD-08"],"VAL-02":["DOD-02","DOD-05","DOD-06","DOD-08","DOD-10"],"VAL-03":["DOD-02","DOD-04","DOD-09"],"VAL-04":["DOD-07"],"VAL-05":["DOD-07","DOD-10"],"VAL-06":["DOD-01","DOD-02","DOD-03","DOD-05","DOD-08"],"VAL-07":["DOD-11"],"VAL-08":["DOD-11","DOD-12"],"VAL-09":["DOD-13"]},"causality":"Do not retroactively claim test-first: only documented actual causal REDs qualify. Most added fault/protocol/storage cases are alongside/post-implementation.","validation_rows":[{"criterion_id":"VAL-01","mapped_dod_ids":["DOD-01","DOD-04","DOD-08"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-02","mapped_dod_ids":["DOD-02","DOD-05","DOD-06","DOD-08","DOD-10"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-03","mapped_dod_ids":["DOD-02","DOD-04","DOD-09"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-04","mapped_dod_ids":["DOD-07"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-05","mapped_dod_ids":["DOD-07","DOD-10"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-06","mapped_dod_ids":["DOD-01","DOD-02","DOD-03","DOD-05","DOD-08"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-07","mapped_dod_ids":["DOD-11"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-08","mapped_dod_ids":["DOD-11","DOD-12"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"},{"criterion_id":"VAL-09","mapped_dod_ids":["DOD-13"],"state":"Current E74 automated proofs mapped; independent assessment and applicable preserved runtime/operator/closure gates remain, not closed.","criterion_source":"Approved TODO Validation Steps, not inferred from aggregate counts","current_checkpoint":"all-result-e74-v1.1.json"}],"recorded_at_utc":"2026-10-23T12:22:57.858927+00:00","current_remediation_reference":"implementation-r6-resolution-e74-v1.1.json","prior_remediation_reference":"implementation-r2-r3-resolution-v1.1.json","rebind_method":"Current terminal fullALL, independent full259source postseal and93browser manifest binding. Historical-labelled evidence remains historical; source hashes in current path records rebound. Current automated proof does not close operator/runtime/module/review/guard gates.","current_r4_correction_proof":{"reference":"implementation-r4-resolution-e74-v1.1.json","same_run_pcv_reference":"pcv-eps-e74-v1.1.json","claim_window":"Both ordinary and initial SENDING CAS enforce captured trusted expiry against the actual DB clock.","mutable_context":"Actual BU/channel/credential pins and actor/grant NOWAIT fence preserve the approved lock order and fail closed under contention.","st05_overlap":"Actual unmodified ST05 refresh races at claim and known-acceptance local completion have zero deadlocks and retain truthful outcomes.","access_paths":"Actual captured-query EXPLAIN uses one partial ordered active-admission index for options and whole-conversation conflict and an ordered intent index; exact metrics are in current PCV."},"current_r6_correction_proof":{"artifact":"implementation-r6-resolution-e74-v1.1.json","sha256":"b437befd4b4b1915d2181b10d1f5681de077fc8216fde7559bf8d3a1be2e7c7b","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","finding_ids":["F-CF091066","F-5E961B39"],"resolution":{"kind":"Root resolution of both r6 causal findings against current full source-bound proof; independent r7 remains required","recorded_at_utc":"2026-10-23T12:20:47.197456+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","all_result":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","rows":[{"finding_id":"F-CF091066","source_finding_id":"ARCH-ST04-R6-01","severity":"medium","resolution":"Integrated","problem":"Current verified identity could qualify a trusted timestamp while its managed lifecycle was false.","correction":"Read managed_lifecycle in the existing same FOR SHARE identity projection; pass only that locked boolean to private timestamp qualification. Preserve Message/receipt acceptance; duplicate reconciliation never promotes a prior null timestamp. No extra query, caller flag, lock-order change or provider call.","sources":[{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","lines":[120,148,188,212],"sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/test/webhooks.e2e-spec.ts","lines":[123,144,149,152,163],"sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"}],"actual_proof_markers":["does not promote an inbound timestamp received while the current resource is unmanaged"],"actual_proof":"Signed-webhook/PG matrix passes: retained IN/unread and null trusted timestamp, closed window before/after lifecycle activation, duplicate without promotion, later new managed IN opens window, zero provider effects.","causal_evidence":"api-result-e72-v1.1.json","limits":"Actual E72 read-projection defect, not an outbound exploit or actual provider effect."},{"finding_id":"F-5E961B39","source_finding_id":"TQA-R6-01","severity":"medium","resolution":"Integrated","problem":"Native deadlock statistics silently defaulted to zero on invalid results.","correction":"Test helper requires exactly one row and a nonnegative native bigint; malformed/missing/ambiguous results fail the test. Real counter overlap probes remain.","sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","lines":[78,145,149,1280,1318,1357,1399],"sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}],"actual_proof_markers":["fails closed when native deadlock statistics are","ST04_ST05_CLAIM_OVERLAP ","ST04_ST05_LOCAL_OVERLAP "],"actual_proof":"All four isolated empty/malformed/multiple/negative fixtures reject; actual unchanged ST05-owner claim/local overlap probes pass with native zero-deadlock deltas.","causal_evidence":"api-result-e72-v1.1.json","limits":"One helper query is substituted once and restored in finally. This test-only helper does not authorize product dispatch; no actual missing native statistics are claimed."}],"r6_collection":"implementation-review-collection-r6-v1.1.json","test_first_boundary":"E72 actual test-only API RED reached four statistics failures and four lifecycle soft assertions before the two exact E73 fixes. E73 actual967pass/postseal/browser is retained; unchanged E74 repeats only to retain lost raw stdout/metrics. No earlier unreached assertion or actual outbound exploit is relabeled.","remaining":["Fresh complete eight-section TQA; terse r6 response insufficient","Current architecture/security/cutover and module review","Current offline images plus approved preserved runtime/operator/full-diff/final gates"],"boundary":"Positive public sources and owned synthetic evidence only; no private environment/business/provider inspection."},"status_note":"Root-authored resolution artifact reproduced as supplied; map rebinding does not independently adjudicate it."},"current_same_run_pcv_reference":{"artifact":"current-synthetic-pcv-samples-e74-v1.1.json","sha256":"75595b6d8884606d36279d02bce24a6f82bb2e695b72707bbd62be6018ca39ae","metric_count":18,"source_seal":"all-source-seal-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751"},"current_actual_all_result":{"artifact":"all-result-e74-v1.1.json","sha256":"e8c56ed6745b3a1d66f9bf2dde86704a5a58f8d936e1ff763f7e75b0e3386818","exit_code":0,"source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","phases":{"migrations":28,"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"duration_seconds":4.39},"api_postgresql":{"files":33,"tests":456,"duration_seconds":309.13},"web_unit":{"files":7,"tests":54,"duration_seconds":0.927},"browser":{"tests":89,"passed":89,"duration_minutes":16.2}}},"current_statistics_test_only_boundary":"Statistics helper metrics are test-only evidence and are not product dispatch authorization.","collection_rebinding_note":"Root corrected stale current-checkpoint strings/r4 refs/source hashes in the staged generic map. Historical-labelled/approved-criterion fields remain exact. Current rows bind actualE74 ALL/PCV/source/freshness; no measurement or closure is invented.","staged_original_sha256":"e13b4d53d023f0cac7df70fa88b9ab160f0833685480dacf05927014c0f006c0"}
```

### security-candidate-map-e74-v1.1.json

SHA256 `72fb6dae512a01c7ebaea38328bd8c0f18155dd1a4f333a176b70e0ad05a5391`

```json
{"kind":"Current E74 executed adversarial proof map for fresh independent challenge","risk_level":"high","attack_simulation_decision":"required","source_seal":"all-source-seal-e74-v1.1.json","execution_state":"Actual E74 canonical ALL terminal exit0 with full259 postseal; current execution metrics are in same-run receipt. This is test-only evidence and does not authorize product dispatch, runtime, or delivery.","threat_intelligence":[{"source":"OWASP API1:2023 Broken Object Level Authorization","url":"https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/","consulted_date":"2026-10-22","paraphrase":"Every object-based action needs permission checks for that object. A valid login and an opaque UUID alone do not establish authorization.","applies_to":"BU/conversation/channel/template/attempt/admission ownership; forged grants and foreign references."},{"source":"OWASP API4:2023 Unrestricted Resource Consumption","url":"https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/","consulted_date":"2026-10-22","paraphrase":"Bound execution time, pages, operation counts and third-party resource use. Concurrent valid calls can consume provider and server resources.","applies_to":"Actor/account limits, bounded template/membership pages, overall lease/preflight budget, one external POST, local-only recovery."}],"surfaces":[{"entry":"Authenticated BFF open/options/preview/initial/read/reconcile/ack","boundary":"Session+CSRF+current home-tenant/BU role before detailed validation; current grant after awaits/inside mutation","abuse":"Forge cross-tenant BU grant; change object IDs; revoke session/role while provider GET held","source_tests":["api-app/test/initial-message.e2e-spec.ts"],"current_receipt":"all-result-e74-v1.1.json; all-source-recheck-e74-v1.1.json","historical_e45_status":"Actual forged cross-tenant grant case295 and current session/grant negative scenarios in approved-template compound329 passed E45; exact BFF current grant/CSRF tested with real PG.","status":"Corresponding negative scenarios passed again in full E74; source tests are bound to current seal. Historical description is retained separately, not current line numbering.","source_hashes":[{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}]},{"entry":"Selected Channel descriptor and scoped credential","boundary":"Immutable BU/channel/origin/resource/generation/epoch/version/account/window context; no browser credentials/account override","abuse":"Confuse descriptor/transport account or use rotated/retired resource before POST","source_tests":["api-app/src/domain/channels/transport/channel-initial-message.spec.ts","api-app/test/channel-transport.e2e-spec.ts"],"current_receipt":"all-result-e74-v1.1.json; all-source-recheck-e74-v1.1.json","historical_e45_status":"Actual nine-field immutable context/substitution tests and channel-transport regressions passed E45; no real credential/provider probing.","status":"Corresponding negative scenarios passed again in full E74; source tests are bound to current seal. Historical description is retained separately, not current line numbering.","source_hashes":[{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},{"path":"api-app/test/channel-transport.e2e-spec.ts","sha256":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"}]},{"entry":"Template catalog/preview/provider preflight","boundary":"Sanitized shared catalog, exact bounded renderer, fresh same-account eligibility/status and grant membership","abuse":"Use paused/unknown/off-account/changed/duplicate template; unbounded pages; inject provider fields","source_tests":["api-app/test/initial-message.e2e-spec.ts","api-app/src/domain/inbox/initial-message-template-renderer.spec.ts"],"current_receipt":"all-result-e74-v1.1.json; all-source-recheck-e74-v1.1.json","historical_e45_status":"Actual approved-template compound329 covers off-account/paused/unknown/changed/duplicate/unexhausted and no-dispatch counters; renderer length/parameter boundaries passed356API.","status":"Corresponding negative scenarios passed again in full E74; source tests are bound to current seal. Historical description is retained separately, not current line numbering.","source_hashes":[{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","sha256":"c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"}]},{"entry":"Initial/ordinary dispatch admissions and local acceptance","boundary":"Durable owned slot, immutable key/request/context, positive claim readback; exactly one POST maximum per intent, no automatic retry","abuse":"Concurrent replay, delayed preflight after expiry, commit ACK loss, late outcome after explicit risk release, echo unique conflict","source_tests":["api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts"],"current_receipt":"all-result-e74-v1.1.json; all-source-recheck-e74-v1.1.json","historical_e45_status":"Actual dispatch-admission commit/rollback and immutable deadline, late-receipt/successor/echo barriers passed435PG; five20-request waves preserve1dispatch/Message each.","status":"Corresponding negative scenarios passed again in full E74; source tests are bound to current seal. Historical description is retained separately, not current line numbering.","source_hashes":[{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}]},{"entry":"Signed official webhook timestamp","boundary":"Verified signature/current resource/positive integer nonfuture timestamp; no createdAt/nonofficial fallback","abuse":"Manufacture free-text window with invalid/future/foreign/duplicate/nonofficial IN","source_tests":["api-app/test/webhooks.e2e-spec.ts","api-app/src/domain/inbox/channel-window-policy.spec.ts"],"current_receipt":"all-result-e74-v1.1.json; all-source-recheck-e74-v1.1.json","historical_e45_status":"Timestamp policy invalid/future/nonofficial/foreign-resource cases and signed webhook tests passed E45; source-bound BFF/public/BOT regression preserved.","status":"Corresponding negative scenarios passed again in full E74; source tests are bound to current seal. Historical description is retained separately, not current line numbering.","source_hashes":[{"path":"api-app/test/webhooks.e2e-spec.ts","sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"},{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","sha256":"e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"}]},{"entry":"Browser compose/recovery/storage and safe errors","boundary":"Actor/BU/conversation-scoped immutable snapshot, explicit confirmation, no automatic POST on reload; escaped React text, closed safe error fields","abuse":"Double-trigger, stale A-B-A preview, quota/storage failure before dispatch, lost response followed by context refusal and new key","source_tests":["web-app/e2e/start-conversation.spec.ts","web-app/src/api.spec.ts"],"current_receipt":"all-result-e74-v1.1.json; all-source-recheck-e74-v1.1.json","historical_e45_status":"Actual escaped preview, delayed A-B-A, session refusal, storage write/read failure and lost-response same-key replay passed85browser. Ordinary recovery action proof still pending E46.","status":"Actual PREPARED UI, ordinary90s recovery, EALB early409/expired acknowledgment/successor/late-old isolation, Unicode input/preview/send, storage read/write and same-key replay passed full E74. EALB/PREPARED expiry is explicit disposable fixture arrangement; ordinary90s case uses actual wait.","source_hashes":[{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"},{"path":"web-app/src/api.spec.ts","sha256":"9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9"}]}],"validation_safety":"Owned disposable synthetic DB/provider boundary only. No actual provider probes, contacts, private data/env/log inspection or destructive test.","residuals":["SEC-R6-04 existing management recovery read budget debt not silently resolved; new initial recovery performs no provider I/O.","OPS-R4-01 and TQA-ST05-03 retained.","Procedural E02/E04/E18/E35a stay in independent assurance packet; no blanket privacy compliance claim.","Candidate map does not replace final security findings/decision, independent review, actual runtime proof or canonical guards.","Canonical npm ci emitted inherited dependency audit warnings; package/lock source remains unchanged and no dependency remediation/scope expansion or blanket dependency-clean claim is made.","No actual preserved local activation, real provider eligibility/send or recipient reply proof for ST04 yet."],"promotion_candidates":"None proposed; no Delphi edits.","findings_state":"R1 corrections have actual full current regression proof; fresh r2 independent security/architecture and final runtime/closure gates remain.","recorded_at_utc":"2026-10-23T12:22:57.885756+00:00","current_remediation_reference":"implementation-r6-resolution-e74-v1.1.json","prior_remediation_reference":"implementation-r2-r3-resolution-v1.1.json","rebind_method":"Current terminal fullALL, independent full259source postseal and93browser manifest binding. Historical-labelled evidence remains historical; source hashes in current path records rebound. Current automated proof does not close operator/runtime/module/review/guard gates.","current_r4_correction_proof":{"reference":"implementation-r4-resolution-e74-v1.1.json","same_run_pcv_reference":"pcv-eps-e74-v1.1.json","claim_window":"Both ordinary and initial SENDING CAS enforce captured trusted expiry against the actual DB clock.","mutable_context":"Actual BU/channel/credential pins and actor/grant NOWAIT fence preserve the approved lock order and fail closed under contention.","st05_overlap":"Actual unmodified ST05 refresh races at claim and known-acceptance local completion have zero deadlocks and retain truthful outcomes.","access_paths":"Actual captured-query EXPLAIN uses one partial ordered active-admission index for options and whole-conversation conflict and an ordered intent index; exact metrics are in current PCV."},"current_additional_attack_proof":["Individually unavailable cached observation cannot authorize a new preview/reservation/POST.","Local settlement failure cannot erase captured BLOCKED/REJECTED/UNKNOWN/ACK_WITHOUT_ID; uncertain admission stays excluded.","BU dialog owner switches cannot let held old response control current UI."],"source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","current_r6_correction_proof":{"artifact":"implementation-r6-resolution-e74-v1.1.json","sha256":"b437befd4b4b1915d2181b10d1f5681de077fc8216fde7559bf8d3a1be2e7c7b","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","finding_ids":["F-CF091066","F-5E961B39"],"resolution":{"kind":"Root resolution of both r6 causal findings against current full source-bound proof; independent r7 remains required","recorded_at_utc":"2026-10-23T12:20:47.197456+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","all_result":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","rows":[{"finding_id":"F-CF091066","source_finding_id":"ARCH-ST04-R6-01","severity":"medium","resolution":"Integrated","problem":"Current verified identity could qualify a trusted timestamp while its managed lifecycle was false.","correction":"Read managed_lifecycle in the existing same FOR SHARE identity projection; pass only that locked boolean to private timestamp qualification. Preserve Message/receipt acceptance; duplicate reconciliation never promotes a prior null timestamp. No extra query, caller flag, lock-order change or provider call.","sources":[{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","lines":[120,148,188,212],"sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/test/webhooks.e2e-spec.ts","lines":[123,144,149,152,163],"sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"}],"actual_proof_markers":["does not promote an inbound timestamp received while the current resource is unmanaged"],"actual_proof":"Signed-webhook/PG matrix passes: retained IN/unread and null trusted timestamp, closed window before/after lifecycle activation, duplicate without promotion, later new managed IN opens window, zero provider effects.","causal_evidence":"api-result-e72-v1.1.json","limits":"Actual E72 read-projection defect, not an outbound exploit or actual provider effect."},{"finding_id":"F-5E961B39","source_finding_id":"TQA-R6-01","severity":"medium","resolution":"Integrated","problem":"Native deadlock statistics silently defaulted to zero on invalid results.","correction":"Test helper requires exactly one row and a nonnegative native bigint; malformed/missing/ambiguous results fail the test. Real counter overlap probes remain.","sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","lines":[78,145,149,1280,1318,1357,1399],"sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}],"actual_proof_markers":["fails closed when native deadlock statistics are","ST04_ST05_CLAIM_OVERLAP ","ST04_ST05_LOCAL_OVERLAP "],"actual_proof":"All four isolated empty/malformed/multiple/negative fixtures reject; actual unchanged ST05-owner claim/local overlap probes pass with native zero-deadlock deltas.","causal_evidence":"api-result-e72-v1.1.json","limits":"One helper query is substituted once and restored in finally. This test-only helper does not authorize product dispatch; no actual missing native statistics are claimed."}],"r6_collection":"implementation-review-collection-r6-v1.1.json","test_first_boundary":"E72 actual test-only API RED reached four statistics failures and four lifecycle soft assertions before the two exact E73 fixes. E73 actual967pass/postseal/browser is retained; unchanged E74 repeats only to retain lost raw stdout/metrics. No earlier unreached assertion or actual outbound exploit is relabeled.","remaining":["Fresh complete eight-section TQA; terse r6 response insufficient","Current architecture/security/cutover and module review","Current offline images plus approved preserved runtime/operator/full-diff/final gates"],"boundary":"Positive public sources and owned synthetic evidence only; no private environment/business/provider inspection."},"status_note":"Root-authored resolution artifact reproduced as supplied; map rebinding does not independently adjudicate it."},"current_same_run_pcv_reference":{"artifact":"current-synthetic-pcv-samples-e74-v1.1.json","sha256":"75595b6d8884606d36279d02bce24a6f82bb2e695b72707bbd62be6018ca39ae","metric_count":18,"source_seal":"all-source-seal-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751"},"current_actual_all_result":{"artifact":"all-result-e74-v1.1.json","sha256":"e8c56ed6745b3a1d66f9bf2dde86704a5a58f8d936e1ff763f7e75b0e3386818","exit_code":0,"source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","phases":{"migrations":28,"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"duration_seconds":4.39},"api_postgresql":{"files":33,"tests":456,"duration_seconds":309.13},"web_unit":{"files":7,"tests":54,"duration_seconds":0.927},"browser":{"tests":89,"passed":89,"duration_minutes":16.2}}},"current_statistics_test_only_boundary":"Statistics helper metrics are test-only evidence and are not product dispatch authorization.","collection_rebinding_note":"Root corrected stale current-checkpoint strings/r4 refs/source hashes in the staged generic map. Historical-labelled/approved-criterion fields remain exact. Current rows bind actualE74 ALL/PCV/source/freshness; no measurement or closure is invented.","staged_original_sha256":"0e93d697d31e6e5b7f7bd856d6fe61e83b4078bfa4c963bcdf3488ff80178243"}
```

### decision-module-candidate-map-e74-v1.1.json

SHA256 `c8948707d07675adb084af6d5a9546d2c9ae45b8007574695dfd09549ab456cd`

```json
{"kind":"Current E74 executed decision/module map for fresh independent challenge","recorded_at_utc":"2026-10-23T12:22:57.911672+00:00","approved_baseline":"TODO Decision Baseline (Frozen Before Implementation), D-01 through D-10 exact wording remains authority","source_seal":"all-source-seal-e74-v1.1.json","execution_receipt":"all-result-e74-v1.1.json","current_status":"Actual E74 canonical ALL terminal exit0 with full259 postseal; current execution metrics are in same-run receipt. This is test-only evidence and does not authorize product dispatch, runtime, or delivery.","canonical_module_baselines":[{"path":"foundation_documentation/modules/inbox-and-conversations.md","sha256":"24b3f1edd8f10bf991d61135be2364b49679c43e5894ce024c2d5169921756a2"},{"path":"foundation_documentation/modules/integrations-and-channels.md","sha256":"6b1865ab4f27458e1e1e225535e2f4a713e987e18344ca86d3f9411fa6c6f168"}],"rows":[{"decision_id":"D-01","proposed_handling":"Preserve","implementation_claim":"BU/contact unique, normalization and no-send manual open; COALESCE order for empty rows.","implementation_sources":[{"path":"api-app/src/domain/inbox/conversation-start.service.ts","sha256":"97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118"},{"path":"api-app/src/domain/inbox/conversations.service.ts","sha256":"6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c"},{"path":"api-app/src/domain/inbox/incoming.service.ts","sha256":"390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b"}],"test_sources":[{"path":"api-app/test/conversation-start.e2e-spec.ts","sha256":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"}],"promotion_target":"inbox: manual open and truthful empty state","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-02","proposed_handling":"Supersede (Intentional)","implementation_claim":"Text-only payload restriction becomes one discriminated sendMessage union with declared kinds; narrow management capability remains separate.","implementation_sources":[{"path":"api-app/src/domain/channels/transport/channel.ts","sha256":"49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9"},{"path":"api-app/src/integrations/channels/meta-channel.ts","sha256":"99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26"},{"path":"api-app/src/integrations/channels/evolution-channel.ts","sha256":"6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34"},{"path":"api-app/src/integrations/channels/channel-transport.module.ts","sha256":"4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d"}],"test_sources":[{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","sha256":"f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3"}],"promotion_target":"integrations: ST06 payload supersede, historical ST05 D09 unchanged","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-03","proposed_handling":"Preserve","implementation_claim":"Inbox coordinator uses common OutboundService and same MessageAcceptance owner; transactional collaboration stays there.","implementation_sources":[{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f"},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"}],"test_sources":[{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"}],"promotion_target":"inbox: first-send ownership and tx boundaries","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-04","proposed_handling":"Supersede (Intentional)","implementation_claim":"Qualified signed Meta IN timestamp replaces historical createdAt latest-IN window; timeline timestamp/cursors preserved.","implementation_sources":[{"path":"api-app/src/domain/inbox/channel-window-policy.ts","sha256":"46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e"},{"path":"api-app/src/surfaces/webhooks/meta.controller.ts","sha256":"261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f"},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","sha256":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943"}],"test_sources":[{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","sha256":"e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"},{"path":"api-app/test/webhooks.e2e-spec.ts","sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","sha256":"3825b0286f9906781e83666616caa05417647ee47c022763fc76e39a3c4ddca0"}],"promotion_target":"inbox/integrations: trusted-window provenance and bounded query","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-05","proposed_handling":"Preserve with bounded initial-send addition","implementation_claim":"Same ST05 catalog; local preview and independent renderer/current same-account eligibility; Meta wire account pin/full international recipient.","implementation_sources":[{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","sha256":"a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"},{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/integrations/meta/initial-message.client.ts","sha256":"e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"}],"test_sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"},{"path":"api-app/test/channel-transport.e2e-spec.ts","sha256":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"}],"promotion_target":"inbox/integrations: eligible template first-send, no authoring changes","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-06","proposed_handling":"New bounded first-send contract","implementation_claim":"Captured request/key/slot/context; all GET preflight then same-operation claim and onePOST; local-only reconciliation and explicit elapsed-deadline risk ACK.","implementation_sources":[{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"},{"path":"api-app/src/surfaces/bff/conversations.controller.ts","sha256":"0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3"}],"test_sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"}],"promotion_target":"inbox: immutable intent and local recovery","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-07","proposed_handling":"Preserve ordinary semantics with explicit interlock","implementation_claim":"Owner tokens exclude initial intent while ordinary requests remain concurrent; uncertain token never expires into blind takeover. BFF empty thread requires first flow, public/BOT legacy behavior retained without slot.","implementation_sources":[{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"},{"path":"web-app/src/telas/Inbox.tsx","sha256":"66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"}],"test_sources":[{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"},{"path":"api-app/test/channel-transport.e2e-spec.ts","sha256":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"},{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"}],"promotion_target":"inbox/integrations: ordinary interlock and finite recovery; browser proof pending","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-08","proposed_handling":"New bounded textual subset","implementation_claim":"NAMED/POSITIONAL plain text from unchanged catalog components; static header/footer, <=20values, Unicode length and context-bound escaped read-only preview.","implementation_sources":[{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","sha256":"a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"},{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"}],"test_sources":[{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","sha256":"c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"},{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"}],"promotion_target":"inbox: template subset and preview safety","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-09","proposed_handling":"New bounded budgets/local proof","implementation_claim":"Max6GET+1POST,10s/request75s aggregate90s immutable reservation; actor10/min,account60/hour. Additive migration and later approved preserved local proof.","implementation_sources":[{"path":"api-app/src/integrations/meta/initial-message.client.ts","sha256":"e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"}],"test_sources":[{"path":"api-app/src/integrations/meta/initial-message.client.spec.ts","sha256":"0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"}],"promotion_target":"integrations/inbox: budget invariants; actual-runtime proof pending","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."},{"decision_id":"D-10","proposed_handling":"Preserve sole Message owner and explicit local certainty","implementation_claim":"Positive commit/captured-key exact readback distinguishes ACK loss vs rollback; no claim/noPOST, no fake RECORDED or unsafe release; canonical opaque account hash namespace remains byte-compatible.","implementation_sources":[{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"},{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/src/integrations/channels/account-reference.ts","sha256":"da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24"}],"test_sources":[{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}],"promotion_target":"inbox/integrations: commit certainty, CAS, known receipt and opaque account","assessment":"Current full E74 candidate proof; original frozen decision remains authority, independent r2 assessment pending."}],"current_remediation_reference":"implementation-r6-resolution-e74-v1.1.json","prior_remediation_reference":"implementation-r2-r3-resolution-v1.1.json","rebind_method":"Current terminal fullALL, independent full259source postseal and93browser manifest binding. Historical-labelled evidence remains historical; source hashes in current path records rebound. Current automated proof does not close operator/runtime/module/review/guard gates.","current_r4_correction_proof":{"reference":"implementation-r4-resolution-e74-v1.1.json","same_run_pcv_reference":"pcv-eps-e74-v1.1.json","claim_window":"Both ordinary and initial SENDING CAS enforce captured trusted expiry against the actual DB clock.","mutable_context":"Actual BU/channel/credential pins and actor/grant NOWAIT fence preserve the approved lock order and fail closed under contention.","st05_overlap":"Actual unmodified ST05 refresh races at claim and known-acceptance local completion have zero deadlocks and retain truthful outcomes.","access_paths":"Actual captured-query EXPLAIN uses one partial ordered active-admission index for options and whole-conversation conflict and an ordered intent index; exact metrics are in current PCV."},"source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","current_r6_correction_proof":{"artifact":"implementation-r6-resolution-e74-v1.1.json","sha256":"b437befd4b4b1915d2181b10d1f5681de077fc8216fde7559bf8d3a1be2e7c7b","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","finding_ids":["F-CF091066","F-5E961B39"],"resolution":{"kind":"Root resolution of both r6 causal findings against current full source-bound proof; independent r7 remains required","recorded_at_utc":"2026-10-23T12:20:47.197456+00:00","source_seal":"all-source-seal-e74-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","all_result":"all-result-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","rows":[{"finding_id":"F-CF091066","source_finding_id":"ARCH-ST04-R6-01","severity":"medium","resolution":"Integrated","problem":"Current verified identity could qualify a trusted timestamp while its managed lifecycle was false.","correction":"Read managed_lifecycle in the existing same FOR SHARE identity projection; pass only that locked boolean to private timestamp qualification. Preserve Message/receipt acceptance; duplicate reconciliation never promotes a prior null timestamp. No extra query, caller flag, lock-order change or provider call.","sources":[{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","lines":[120,148,188,212],"sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/test/webhooks.e2e-spec.ts","lines":[123,144,149,152,163],"sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"}],"actual_proof_markers":["does not promote an inbound timestamp received while the current resource is unmanaged"],"actual_proof":"Signed-webhook/PG matrix passes: retained IN/unread and null trusted timestamp, closed window before/after lifecycle activation, duplicate without promotion, later new managed IN opens window, zero provider effects.","causal_evidence":"api-result-e72-v1.1.json","limits":"Actual E72 read-projection defect, not an outbound exploit or actual provider effect."},{"finding_id":"F-5E961B39","source_finding_id":"TQA-R6-01","severity":"medium","resolution":"Integrated","problem":"Native deadlock statistics silently defaulted to zero on invalid results.","correction":"Test helper requires exactly one row and a nonnegative native bigint; malformed/missing/ambiguous results fail the test. Real counter overlap probes remain.","sources":[{"path":"api-app/test/initial-message.e2e-spec.ts","lines":[78,145,149,1280,1318,1357,1399],"sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"}],"actual_proof_markers":["fails closed when native deadlock statistics are","ST04_ST05_CLAIM_OVERLAP ","ST04_ST05_LOCAL_OVERLAP "],"actual_proof":"All four isolated empty/malformed/multiple/negative fixtures reject; actual unchanged ST05-owner claim/local overlap probes pass with native zero-deadlock deltas.","causal_evidence":"api-result-e72-v1.1.json","limits":"One helper query is substituted once and restored in finally. This test-only helper does not authorize product dispatch; no actual missing native statistics are claimed."}],"r6_collection":"implementation-review-collection-r6-v1.1.json","test_first_boundary":"E72 actual test-only API RED reached four statistics failures and four lifecycle soft assertions before the two exact E73 fixes. E73 actual967pass/postseal/browser is retained; unchanged E74 repeats only to retain lost raw stdout/metrics. No earlier unreached assertion or actual outbound exploit is relabeled.","remaining":["Fresh complete eight-section TQA; terse r6 response insufficient","Current architecture/security/cutover and module review","Current offline images plus approved preserved runtime/operator/full-diff/final gates"],"boundary":"Positive public sources and owned synthetic evidence only; no private environment/business/provider inspection."},"status_note":"Root-authored resolution artifact reproduced as supplied; map rebinding does not independently adjudicate it."},"current_same_run_pcv_reference":{"artifact":"current-synthetic-pcv-samples-e74-v1.1.json","sha256":"75595b6d8884606d36279d02bce24a6f82bb2e695b72707bbd62be6018ca39ae","metric_count":18,"source_seal":"all-source-seal-e74-v1.1.json","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751"},"current_actual_all_result":{"artifact":"all-result-e74-v1.1.json","sha256":"e8c56ed6745b3a1d66f9bf2dde86704a5a58f8d936e1ff763f7e75b0e3386818","exit_code":0,"source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","stdout_sha256":"73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751","phases":{"migrations":28,"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"duration_seconds":4.39},"api_postgresql":{"files":33,"tests":456,"duration_seconds":309.13},"web_unit":{"files":7,"tests":54,"duration_seconds":0.927},"browser":{"tests":89,"passed":89,"duration_minutes":16.2}}},"current_statistics_test_only_boundary":"Statistics helper metrics are test-only evidence and are not product dispatch authorization.","collection_rebinding_note":"Root corrected stale current-checkpoint strings/r4 refs/source hashes in the staged generic map. Historical-labelled/approved-criterion fields remain exact. Current rows bind actualE74 ALL/PCV/source/freshness; no measurement or closure is invented.","staged_original_sha256":"681c83072a066108f7c12fbb05e9ac32a3c8809fe046366bbef292f2397039ba"}
```

### executor-all-e74.txt

Exact durable current stdout path: `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/stcon04-e74/executor-all-e74.txt`. SHA256 `73a5f43f7ed69e9e00271c55d6cb12e96917f0cb8bed587b3c33e403b62b9751`; this binds the result and source recheck. Actual phase counts are in `all-result-e74-v1.1.json`; full per-run PCV metrics and plan payloads are shown once in the current sample references and four same-run lane artifacts below. The complete stdout is available at the bound path and is not duplicated in the prompt.

### test-quality-public-roots-output-e74-v1.1.txt

Exact raw scan path: `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-output-e74-v1.1.txt`. SHA256 `1a096a509c618914002d492fc97203c6520aea4a3d7b38a482218f77e84f72e3`; the static receipt preserves the actual full-root high/exit2 outcome and category counts. Complete per-row values appear in the lossless TQA inventory section; raw scan text is available at the bound path and is not duplicated here.

### selected-source-seal-compact-view-e74

Exact raw receipt path: `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-source-seal-e74-v1.1.json`. SHA256 `40ad3c8844a20d2d688269ac60f0b2648460bb3c26d6e6bf2fe912fcd5694d4c`

```json
{"checkpoint":"E74 unchanged corrected candidate, repeat only to retain lost actual stdout/current metrics","fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","count":259,"positive_public_roots":["api-app/src","api-app/test","api-app/prisma","web-app/src","web-app/e2e"],"protected_and_exact_companion_check_count":38,"protected_and_exact_companion_checks":[{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.ts","matches":true},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","matches":true},{"path":"api-app/test/message-template-bff.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-management.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","matches":true},{"path":"web-app/e2e/message-templates.spec.ts","matches":true},{"path":"web-app/src/App.tsx","matches":true},{"path":"web-app/src/telas/Modelos.spec.ts","matches":true},{"path":"web-app/src/telas/Modelos.tsx","matches":true},{"path":".github/workflows/ci.yml","matches":true},{"path":"scripts/test-channels-local.sh","matches":true},{"path":"scripts/check-channels-ci-parity.py","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.ts","matches":true},{"path":"api-app/src/surfaces/public/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/public.module.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","matches":true},{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","matches":true},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","matches":true},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","matches":true}],"current_package_source_hashes":{"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437","api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a","api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544","api-app/prisma/schema.prisma":"19ea60e6e5a1675a4ff12581237b2f91c2359b61d7b8bcb9e8bf1c1ebf26435d","api-app/src/domain/channels/transport/channel-dependencies.spec.ts":"f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3","api-app/src/domain/channels/transport/channel-initial-message.spec.ts":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa","api-app/src/domain/channels/transport/channel.ts":"49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9","api-app/src/domain/inbox/channel-window-policy.spec.ts":"e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692","api-app/src/domain/inbox/channel-window-policy.ts":"46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e","api-app/src/domain/inbox/conversation-start.service.ts":"97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118","api-app/src/domain/inbox/conversations.service.ts":"6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c","api-app/src/domain/inbox/dispatch-admission.service.spec.ts":"687345771d8394ef8317142f38736876e730fc28cfdddd974a0fdd363fa7b78d","api-app/src/domain/inbox/dispatch-admission.service.ts":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9","api-app/src/domain/inbox/incoming.service.ts":"390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b","api-app/src/domain/inbox/initial-message-template-renderer.spec.ts":"c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0","api-app/src/domain/inbox/initial-message-template-renderer.ts":"a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf","api-app/src/domain/inbox/initial-message.service.spec.ts":"e472bc1048f1c24c8edbe3004baceb15cc5a78956653bb2e30ade45843e2ee92","api-app/src/domain/inbox/initial-message.service.ts":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e","api-app/src/domain/inbox/message-acceptance.service.ts":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4","api-app/src/domain/inbox/outbound.service.spec.ts":"748be057ff4b3cfe1215b87108d7708ca02ed97d7a7d129d9cada5fc1aef8d81","api-app/src/domain/inbox/outbound.service.ts":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f","api-app/src/domain/message-templates/template-observation.service.ts":"41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488","api-app/src/infra/session/session.service.ts":"884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200","api-app/src/integrations/channels/account-reference.ts":"da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24","api-app/src/integrations/channels/channel-adapter-factory.ts":"e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc","api-app/src/integrations/channels/channel-adapter-registry.ts":"655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b","api-app/src/integrations/channels/channel-transport.module.ts":"4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d","api-app/src/integrations/channels/evolution-channel.ts":"6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34","api-app/src/integrations/channels/meta-channel.ts":"99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26","api-app/src/integrations/channels/prisma-channel-resolver.ts":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943","api-app/src/integrations/message-templates/template-management.module.ts":"aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd","api-app/src/integrations/message-templates/template-management.resolver.ts":"1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00","api-app/src/integrations/meta/initial-message.client.spec.ts":"0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057","api-app/src/integrations/meta/initial-message.client.ts":"e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721","api-app/src/surfaces/bff/bff.module.ts":"8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a","api-app/src/surfaces/bff/conversations.controller.ts":"0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3","api-app/src/surfaces/bff/session.middleware.ts":"80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211","api-app/src/surfaces/public/conversations.controller.ts":"bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1","api-app/src/surfaces/webhooks/meta.controller.ts":"261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f","api-app/test/browser-server.cjs":"02354237e3c0c5f8d918f65cbb833270e2ce02469cfe3e926e3a6790abc106dc","api-app/test/channel-transport.e2e-spec.ts":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011","api-app/test/conversation-start.e2e-spec.ts":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11","api-app/test/dispatch-admission.e2e-spec.ts":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f","api-app/test/helpers.ts":"117e4f85c81dda37ab30e7eb23704b31538c8c5161aa7562a844eaf11de6819c","api-app/test/initial-message.e2e-spec.ts":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d","api-app/test/timeline-fixtures.cjs":"a8239426ffb80dd430d38fe9f3dfc29d5ad346f77f519320be25e37c1f853d81","api-app/test/webhooks.e2e-spec.ts":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5","web-app/e2e/start-conversation.spec.ts":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284","web-app/e2e/timeline-freshness.ts":"3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53","web-app/src/api.spec.ts":"9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9","web-app/src/api.ts":"7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c","web-app/src/componentes/NovaConversa.spec.ts":"84184865db156d6c147e382982e235ea82f16ea9892cb0cc6e59f16ac1393757","web-app/src/componentes/NovaConversa.tsx":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd","web-app/src/telas/Inbox.tsx":"66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"},"omission_limit":"The full259 raw seal is identified by SHA256 and exact path foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/all-source-seal-e74-v1.1.json; this view omits unrelated source records only. Critical review source paths are listed with exact current hashes."}
```

### all-source-seal-e71-v1.1.json — historical bounded source-seal view

SHA256 `cc2d52752008aa9f26f1ffe56666d3ceaa81446bae720d0008f07f0d6cf0473e`

```json
{"checkpoint":"E71 positive public candidate before canonical all","capture_stage":"Before actual runner, no result inferred","captured_at_utc":"2026-10-23T04:28:37.233294+00:00","owner":"root independent public source collector","command_planned":"bash scripts/test-channels-local.sh all","synthetic_stdout_planned":"/tmp/stcon04-executor-all-e71.txt","fresh_git_identity":{"root":"80e3940126f22a941f90dba4f5e801b6c0eb2f58\nHEAD -> feature/number-onboarding","api":"db5a86758a165fac8a1ab587599c37b17890530c\nHEAD -> feature/number-onboarding","web":"74b9d4b714044829796f875d00553f077c1c329d\nHEAD -> feature/number-onboarding","foundation":"32e421863a59492ead3db1ccd2d07ae7030097e2\nHEAD -> main, origin/main, origin/HEAD"},"positive_public_roots":["api-app/src","api-app/test","api-app/prisma","web-app/src","web-app/e2e"],"exact_public_files":[".github/workflows/ci.yml","api-app/package.json","api-app/package-lock.json","scripts/check-channels-ci-parity.py","scripts/test-channels-local.sh","web-app/package.json","web-app/package-lock.json"],"count":259,"fingerprint_algorithm":"SHA256 canonical JSON sorted keys compact separators of sorted path+sha256 records","fingerprint":"4f35237f1d6aaf55f98e129631e17184d8f5b196249f6c56c10f210add52daf4","protected_and_exact_companion_checks":[{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.ts","matches":true},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","matches":true},{"path":"api-app/test/message-template-bff.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-management.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","matches":true},{"path":"web-app/e2e/message-templates.spec.ts","matches":true},{"path":"web-app/src/App.tsx","matches":true},{"path":"web-app/src/telas/Modelos.spec.ts","matches":true},{"path":"web-app/src/telas/Modelos.tsx","matches":true},{"path":".github/workflows/ci.yml","matches":true},{"path":"scripts/test-channels-local.sh","matches":true},{"path":"scripts/check-channels-ci-parity.py","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.ts","matches":true},{"path":"api-app/src/surfaces/public/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/public.module.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","matches":true},{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","matches":true},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","matches":true},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","matches":true}],"previous_seal":"all-source-seal-e70-v1.1.json","exact_delta_from_previous":["api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","api-app/prisma/schema.prisma","api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts"],"delta_from_e54":["api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","api-app/prisma/schema.prisma","api-app/src/domain/inbox/dispatch-admission.service.spec.ts","api-app/src/domain/inbox/dispatch-admission.service.ts","api-app/src/domain/inbox/initial-message.service.spec.ts","api-app/src/domain/inbox/initial-message.service.ts","api-app/src/domain/inbox/outbound.service.spec.ts","api-app/src/domain/inbox/outbound.service.ts","api-app/src/integrations/channels/prisma-channel-resolver.ts","api-app/src/surfaces/bff/conversations.controller.ts","api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts","web-app/src/telas/Inbox.tsx"],"limits":"Positive public files only. Preserve immutable earlier run receipts; no private/runtime/provider proof or current execution result inferred.","records":[{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","sha256":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437"},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","sha256":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a"},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","sha256":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544"},{"path":"api-app/prisma/schema.prisma","sha256":"19ea60e6e5a1675a4ff12581237b2f91c2359b61d7b8bcb9e8bf1c1ebf26435d"},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","sha256":"f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3"},{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},{"path":"api-app/src/domain/channels/transport/channel.ts","sha256":"49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9"},{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","sha256":"e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"},{"path":"api-app/src/domain/inbox/channel-window-policy.ts","sha256":"46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e"},{"path":"api-app/src/domain/inbox/conversation-start.service.ts","sha256":"97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118"},{"path":"api-app/src/domain/inbox/conversations.service.ts","sha256":"6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.spec.ts","sha256":"687345771d8394ef8317142f38736876e730fc28cfdddd974a0fdd363fa7b78d"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"},{"path":"api-app/src/domain/inbox/incoming.service.ts","sha256":"390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","sha256":"c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","sha256":"a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"},{"path":"api-app/src/domain/inbox/initial-message.service.spec.ts","sha256":"e472bc1048f1c24c8edbe3004baceb15cc5a78956653bb2e30ade45843e2ee92"},{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","sha256":"71194c70b12cb920054586a7a86266d90f8eca0b7008b1b5688627e0694979f1"},{"path":"api-app/src/domain/inbox/outbound.service.spec.ts","sha256":"748be057ff4b3cfe1215b87108d7708ca02ed97d7a7d129d9cada5fc1aef8d81"},{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f"},{"path":"api-app/src/domain/message-templates/template-observation.service.ts","sha256":"41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488"},{"path":"api-app/src/infra/session/session.service.ts","sha256":"884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200"},{"path":"api-app/src/integrations/channels/account-reference.ts","sha256":"da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24"},{"path":"api-app/src/integrations/channels/channel-adapter-factory.ts","sha256":"e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc"},{"path":"api-app/src/integrations/channels/channel-adapter-registry.ts","sha256":"655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b"},{"path":"api-app/src/integrations/channels/channel-transport.module.ts","sha256":"4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d"},{"path":"api-app/src/integrations/channels/evolution-channel.ts","sha256":"6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34"},{"path":"api-app/src/integrations/channels/meta-channel.ts","sha256":"99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26"},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","sha256":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943"},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","sha256":"aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd"},{"path":"api-app/src/integrations/message-templates/template-management.resolver.ts","sha256":"1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00"},{"path":"api-app/src/integrations/meta/initial-message.client.spec.ts","sha256":"0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057"},{"path":"api-app/src/integrations/meta/initial-message.client.ts","sha256":"e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"},{"path":"api-app/src/surfaces/bff/bff.module.ts","sha256":"8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a"},{"path":"api-app/src/surfaces/bff/conversations.controller.ts","sha256":"0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3"},{"path":"api-app/src/surfaces/bff/session.middleware.ts","sha256":"80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211"},{"path":"api-app/src/surfaces/public/conversations.controller.ts","sha256":"bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1"},{"path":"api-app/src/surfaces/webhooks/meta.controller.ts","sha256":"261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f"},{"path":"api-app/test/browser-server.cjs","sha256":"02354237e3c0c5f8d918f65cbb833270e2ce02469cfe3e926e3a6790abc106dc"},{"path":"api-app/test/channel-transport.e2e-spec.ts","sha256":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"},{"path":"api-app/test/conversation-start.e2e-spec.ts","sha256":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"},{"path":"api-app/test/helpers.ts","sha256":"117e4f85c81dda37ab30e7eb23704b31538c8c5161aa7562a844eaf11de6819c"},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"44ce516d60168219ddc5aec66ef89ecbb7483b36959a5c3f3620174f0eaf5e55"},{"path":"api-app/test/timeline-fixtures.cjs","sha256":"a8239426ffb80dd430d38fe9f3dfc29d5ad346f77f519320be25e37c1f853d81"},{"path":"api-app/test/webhooks.e2e-spec.ts","sha256":"e9f80894181676b2fcb4ec18339a6ebdb1e189f3f13374cd1c2e77d13e647f4a"},{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"},{"path":"web-app/e2e/timeline-freshness.ts","sha256":"3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53"},{"path":"web-app/src/api.spec.ts","sha256":"9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9"},{"path":"web-app/src/api.ts","sha256":"7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c"},{"path":"web-app/src/componentes/NovaConversa.spec.ts","sha256":"84184865db156d6c147e382982e235ea82f16ea9892cb0cc6e59f16ac1393757"},{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"},{"path":"web-app/src/telas/Inbox.tsx","sha256":"66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"}],"raw_receipt_sha256":"cc2d52752008aa9f26f1ffe56666d3ceaa81446bae720d0008f07f0d6cf0473e","omission_note":"Faithful bounded view: all 259 original records are retained in the raw receipt identified by raw_receipt_sha256; this view omits 205 unrelated repeated records and preserves exact hashes for 54 critical review paths."}
```

### api-source-seal-e72-v1.1.json — historical bounded source-seal view

SHA256 `b252d8b50abae47c254512c6536951bb59f6490e98aa2dc2fe118ae6876f054d`

```json
{"checkpoint":"E72 positive public candidate before canonical api","capture_stage":"Before actual runner, no result inferred","captured_at_utc":"2026-10-23T05:12:51.403731+00:00","owner":"root independent public source collector","command_planned":"bash scripts/test-channels-local.sh api","synthetic_stdout_planned":"/tmp/stcon04-executor-api-e72.txt","fresh_git_identity":{"root":"80e3940126f22a941f90dba4f5e801b6c0eb2f58\nHEAD -> feature/number-onboarding","api":"db5a86758a165fac8a1ab587599c37b17890530c\nHEAD -> feature/number-onboarding","web":"74b9d4b714044829796f875d00553f077c1c329d\nHEAD -> feature/number-onboarding","foundation":"34236ecf498fe3d8f62e168b7ece570327ad3ebc\nHEAD -> main"},"positive_public_roots":["api-app/src","api-app/test","api-app/prisma","web-app/src","web-app/e2e"],"exact_public_files":[".github/workflows/ci.yml","api-app/package.json","api-app/package-lock.json","scripts/check-channels-ci-parity.py","scripts/test-channels-local.sh","web-app/package.json","web-app/package-lock.json"],"count":259,"fingerprint_algorithm":"SHA256 canonical JSON sorted keys compact separators of sorted path+sha256 records","fingerprint":"0f92d1121f2a2d67d29d1d4ba4c976af2648ef2a633932c11cf4f86876f84031","protected_and_exact_companion_checks":[{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.ts","matches":true},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","matches":true},{"path":"api-app/test/message-template-bff.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-management.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","matches":true},{"path":"web-app/e2e/message-templates.spec.ts","matches":true},{"path":"web-app/src/App.tsx","matches":true},{"path":"web-app/src/telas/Modelos.spec.ts","matches":true},{"path":"web-app/src/telas/Modelos.tsx","matches":true},{"path":".github/workflows/ci.yml","matches":true},{"path":"scripts/test-channels-local.sh","matches":true},{"path":"scripts/check-channels-ci-parity.py","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.ts","matches":true},{"path":"api-app/src/surfaces/public/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/public.module.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","matches":true},{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","matches":true},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","matches":true},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","matches":true}],"previous_seal":"all-source-seal-e71-v1.1.json","exact_delta_from_previous":["api-app/test/initial-message.e2e-spec.ts","api-app/test/webhooks.e2e-spec.ts"],"delta_from_e54":["api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","api-app/prisma/schema.prisma","api-app/src/domain/inbox/dispatch-admission.service.spec.ts","api-app/src/domain/inbox/dispatch-admission.service.ts","api-app/src/domain/inbox/initial-message.service.spec.ts","api-app/src/domain/inbox/initial-message.service.ts","api-app/src/domain/inbox/outbound.service.spec.ts","api-app/src/domain/inbox/outbound.service.ts","api-app/src/integrations/channels/prisma-channel-resolver.ts","api-app/src/surfaces/bff/conversations.controller.ts","api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts","api-app/test/webhooks.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts","web-app/src/telas/Inbox.tsx"],"limits":"Positive public files only. Preserve immutable earlier run receipts; no private/runtime/provider proof or current execution result inferred.","records":[{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","sha256":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437"},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","sha256":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a"},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","sha256":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544"},{"path":"api-app/prisma/schema.prisma","sha256":"19ea60e6e5a1675a4ff12581237b2f91c2359b61d7b8bcb9e8bf1c1ebf26435d"},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","sha256":"f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3"},{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},{"path":"api-app/src/domain/channels/transport/channel.ts","sha256":"49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9"},{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","sha256":"e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"},{"path":"api-app/src/domain/inbox/channel-window-policy.ts","sha256":"46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e"},{"path":"api-app/src/domain/inbox/conversation-start.service.ts","sha256":"97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118"},{"path":"api-app/src/domain/inbox/conversations.service.ts","sha256":"6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.spec.ts","sha256":"687345771d8394ef8317142f38736876e730fc28cfdddd974a0fdd363fa7b78d"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"},{"path":"api-app/src/domain/inbox/incoming.service.ts","sha256":"390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","sha256":"c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","sha256":"a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"},{"path":"api-app/src/domain/inbox/initial-message.service.spec.ts","sha256":"e472bc1048f1c24c8edbe3004baceb15cc5a78956653bb2e30ade45843e2ee92"},{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","sha256":"71194c70b12cb920054586a7a86266d90f8eca0b7008b1b5688627e0694979f1"},{"path":"api-app/src/domain/inbox/outbound.service.spec.ts","sha256":"748be057ff4b3cfe1215b87108d7708ca02ed97d7a7d129d9cada5fc1aef8d81"},{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f"},{"path":"api-app/src/domain/message-templates/template-observation.service.ts","sha256":"41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488"},{"path":"api-app/src/infra/session/session.service.ts","sha256":"884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200"},{"path":"api-app/src/integrations/channels/account-reference.ts","sha256":"da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24"},{"path":"api-app/src/integrations/channels/channel-adapter-factory.ts","sha256":"e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc"},{"path":"api-app/src/integrations/channels/channel-adapter-registry.ts","sha256":"655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b"},{"path":"api-app/src/integrations/channels/channel-transport.module.ts","sha256":"4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d"},{"path":"api-app/src/integrations/channels/evolution-channel.ts","sha256":"6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34"},{"path":"api-app/src/integrations/channels/meta-channel.ts","sha256":"99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26"},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","sha256":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943"},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","sha256":"aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd"},{"path":"api-app/src/integrations/message-templates/template-management.resolver.ts","sha256":"1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00"},{"path":"api-app/src/integrations/meta/initial-message.client.spec.ts","sha256":"0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057"},{"path":"api-app/src/integrations/meta/initial-message.client.ts","sha256":"e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"},{"path":"api-app/src/surfaces/bff/bff.module.ts","sha256":"8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a"},{"path":"api-app/src/surfaces/bff/conversations.controller.ts","sha256":"0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3"},{"path":"api-app/src/surfaces/bff/session.middleware.ts","sha256":"80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211"},{"path":"api-app/src/surfaces/public/conversations.controller.ts","sha256":"bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1"},{"path":"api-app/src/surfaces/webhooks/meta.controller.ts","sha256":"261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f"},{"path":"api-app/test/browser-server.cjs","sha256":"02354237e3c0c5f8d918f65cbb833270e2ce02469cfe3e926e3a6790abc106dc"},{"path":"api-app/test/channel-transport.e2e-spec.ts","sha256":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"},{"path":"api-app/test/conversation-start.e2e-spec.ts","sha256":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"},{"path":"api-app/test/helpers.ts","sha256":"117e4f85c81dda37ab30e7eb23704b31538c8c5161aa7562a844eaf11de6819c"},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"2028da4679615c7bf7e04aeafc84c02eec194541384163719e9d616981608865"},{"path":"api-app/test/timeline-fixtures.cjs","sha256":"a8239426ffb80dd430d38fe9f3dfc29d5ad346f77f519320be25e37c1f853d81"},{"path":"api-app/test/webhooks.e2e-spec.ts","sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"},{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"},{"path":"web-app/e2e/timeline-freshness.ts","sha256":"3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53"},{"path":"web-app/src/api.spec.ts","sha256":"9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9"},{"path":"web-app/src/api.ts","sha256":"7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c"},{"path":"web-app/src/componentes/NovaConversa.spec.ts","sha256":"84184865db156d6c147e382982e235ea82f16ea9892cb0cc6e59f16ac1393757"},{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"},{"path":"web-app/src/telas/Inbox.tsx","sha256":"66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"}],"raw_receipt_sha256":"b252d8b50abae47c254512c6536951bb59f6490e98aa2dc2fe118ae6876f054d","omission_note":"Faithful bounded view: all 259 original records are retained in the raw receipt identified by raw_receipt_sha256; this view omits 205 unrelated repeated records and preserves exact hashes for 54 critical review paths."}
```

### all-source-seal-e73-v1.1.json — historical bounded source-seal view

SHA256 `164e31d019f8d9b30adeb5020b9c87a46bd141d8aa1c1d68e598b40cced55ebb`

```json
{"checkpoint":"E73 positive public candidate before canonical all","capture_stage":"Before actual runner, no result inferred","captured_at_utc":"2026-10-23T05:22:26.589721+00:00","owner":"root independent public source collector","command_planned":"bash scripts/test-channels-local.sh all","synthetic_stdout_planned":"/tmp/stcon04-executor-all-e73.txt","fresh_git_identity":{"root":"80e3940126f22a941f90dba4f5e801b6c0eb2f58\nHEAD -> feature/number-onboarding","api":"db5a86758a165fac8a1ab587599c37b17890530c\nHEAD -> feature/number-onboarding","web":"74b9d4b714044829796f875d00553f077c1c329d\nHEAD -> feature/number-onboarding","foundation":"34236ecf498fe3d8f62e168b7ece570327ad3ebc\nHEAD -> main, origin/main, origin/HEAD"},"positive_public_roots":["api-app/src","api-app/test","api-app/prisma","web-app/src","web-app/e2e"],"exact_public_files":[".github/workflows/ci.yml","api-app/package.json","api-app/package-lock.json","scripts/check-channels-ci-parity.py","scripts/test-channels-local.sh","web-app/package.json","web-app/package-lock.json"],"count":259,"fingerprint_algorithm":"SHA256 canonical JSON sorted keys compact separators of sorted path+sha256 records","fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","protected_and_exact_companion_checks":[{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.ts","matches":true},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","matches":true},{"path":"api-app/test/message-template-bff.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-management.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","matches":true},{"path":"web-app/e2e/message-templates.spec.ts","matches":true},{"path":"web-app/src/App.tsx","matches":true},{"path":"web-app/src/telas/Modelos.spec.ts","matches":true},{"path":"web-app/src/telas/Modelos.tsx","matches":true},{"path":".github/workflows/ci.yml","matches":true},{"path":"scripts/test-channels-local.sh","matches":true},{"path":"scripts/check-channels-ci-parity.py","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.ts","matches":true},{"path":"api-app/src/surfaces/public/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/public.module.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","matches":true},{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","matches":true},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","matches":true},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","matches":true}],"previous_seal":"api-source-seal-e72-v1.1.json","exact_delta_from_previous":["api-app/src/domain/inbox/message-acceptance.service.ts","api-app/test/initial-message.e2e-spec.ts"],"delta_from_e54":["api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","api-app/prisma/schema.prisma","api-app/src/domain/inbox/dispatch-admission.service.spec.ts","api-app/src/domain/inbox/dispatch-admission.service.ts","api-app/src/domain/inbox/initial-message.service.spec.ts","api-app/src/domain/inbox/initial-message.service.ts","api-app/src/domain/inbox/message-acceptance.service.ts","api-app/src/domain/inbox/outbound.service.spec.ts","api-app/src/domain/inbox/outbound.service.ts","api-app/src/integrations/channels/prisma-channel-resolver.ts","api-app/src/surfaces/bff/conversations.controller.ts","api-app/test/dispatch-admission.e2e-spec.ts","api-app/test/initial-message.e2e-spec.ts","api-app/test/webhooks.e2e-spec.ts","web-app/e2e/start-conversation.spec.ts","web-app/src/telas/Inbox.tsx"],"limits":"Positive public files only. Preserve immutable earlier run receipts; no private/runtime/provider proof or current execution result inferred.","records":[{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","sha256":"a8b26d5dfc7eb8f658cf703cee0f1f6061b5afa2ad84ca0f37cd4baec9d68437"},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","sha256":"41df36b473c3163e9e29ea1cc6c12df3376994081698be83c83e50a812e3922a"},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","sha256":"60e7f76b8ccbee5e51dd939bdf126eeecaa1b1c1871f393a4363add94274a544"},{"path":"api-app/prisma/schema.prisma","sha256":"19ea60e6e5a1675a4ff12581237b2f91c2359b61d7b8bcb9e8bf1c1ebf26435d"},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","sha256":"f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3"},{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","sha256":"46d9c0806eb418401dfbd2e538e78b2ee24e8d674a3962fb88802ecb5923a5fa"},{"path":"api-app/src/domain/channels/transport/channel.ts","sha256":"49b24179666a0fa90becfb2bf24ebc31acde7bf342b34d3b110a42465ccb69f9"},{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","sha256":"e20eaefd11256c8ca9f2156560ac23a1478f333b3932e865d1d52666cbd78692"},{"path":"api-app/src/domain/inbox/channel-window-policy.ts","sha256":"46dfcf887f2ad4ed0670664186e918816699e6541d1670aa9c32ac79a193e43e"},{"path":"api-app/src/domain/inbox/conversation-start.service.ts","sha256":"97ee440ce06007eac1aed98e0afe4997056722c8d62508a0698655a2de5d1118"},{"path":"api-app/src/domain/inbox/conversations.service.ts","sha256":"6dba438e7e59dff56b2b98413532210bac62b7d744cf1b80c5a2c748923b431c"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.spec.ts","sha256":"687345771d8394ef8317142f38736876e730fc28cfdddd974a0fdd363fa7b78d"},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","sha256":"2c3e19f9bcacd75d047ee73e5913ad77e9a8700a43427af27556b801234bcda9"},{"path":"api-app/src/domain/inbox/incoming.service.ts","sha256":"390d48de06ad863b9d9c47344c1eb2919d0ba07aa96626b0ef1596fcbde4795b"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","sha256":"c783e835575ab8cf89af5524e0f02402956975f80faecf6b9d1467c1a8a0bdf0"},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","sha256":"a5ce98823c8f0a4480386bc755e392b5f6287107cbfc0ad13ad50c06bc234ecf"},{"path":"api-app/src/domain/inbox/initial-message.service.spec.ts","sha256":"e472bc1048f1c24c8edbe3004baceb15cc5a78956653bb2e30ade45843e2ee92"},{"path":"api-app/src/domain/inbox/initial-message.service.ts","sha256":"61a52116f29e5753ed27bae607dbebd5dfdb5b1fd1dc8954a02602e8d81a8e6e"},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","sha256":"285647f1dee08b14dbae8661743c75198f1be85d5b523e9f73c7d51dfbe30ff4"},{"path":"api-app/src/domain/inbox/outbound.service.spec.ts","sha256":"748be057ff4b3cfe1215b87108d7708ca02ed97d7a7d129d9cada5fc1aef8d81"},{"path":"api-app/src/domain/inbox/outbound.service.ts","sha256":"cb4b2e68c7377411991960c65e3d15cef8bc1aea927049cd99345e523433bd9f"},{"path":"api-app/src/domain/message-templates/template-observation.service.ts","sha256":"41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488"},{"path":"api-app/src/infra/session/session.service.ts","sha256":"884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200"},{"path":"api-app/src/integrations/channels/account-reference.ts","sha256":"da2b4572b07477407f9adf08c30c3876d10f92ae157cfadb3b8bdc5fc99d0d24"},{"path":"api-app/src/integrations/channels/channel-adapter-factory.ts","sha256":"e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc"},{"path":"api-app/src/integrations/channels/channel-adapter-registry.ts","sha256":"655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b"},{"path":"api-app/src/integrations/channels/channel-transport.module.ts","sha256":"4aa42bb2e873c576b63b5ac1f50db368fbecb189fe91be19f3b7fb726733370d"},{"path":"api-app/src/integrations/channels/evolution-channel.ts","sha256":"6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34"},{"path":"api-app/src/integrations/channels/meta-channel.ts","sha256":"99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26"},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","sha256":"bd6b455d06fd6a5c2b4f09ca7d15ea4a55670a0555abc2744309c68072b6e943"},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","sha256":"aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd"},{"path":"api-app/src/integrations/message-templates/template-management.resolver.ts","sha256":"1d26d05183645def5b0ef4ba317f7d024b3a08c610c910593a35308309e99e00"},{"path":"api-app/src/integrations/meta/initial-message.client.spec.ts","sha256":"0467fbad2f0b8666491d93b6efb0b648037fde08ee0655ffb4500747e68fd057"},{"path":"api-app/src/integrations/meta/initial-message.client.ts","sha256":"e21efb3df6910c0b740afec40da919542f672302429217268fdb56c282446721"},{"path":"api-app/src/surfaces/bff/bff.module.ts","sha256":"8591bf48dbc3275cc24bb57b5c94d0e492dbd7c1c9aac9f7f58c91013a24cc8a"},{"path":"api-app/src/surfaces/bff/conversations.controller.ts","sha256":"0967a901f8fca2fb275c1423a5ccd4d3185b9f55544862d3565c91bb528f19f3"},{"path":"api-app/src/surfaces/bff/session.middleware.ts","sha256":"80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211"},{"path":"api-app/src/surfaces/public/conversations.controller.ts","sha256":"bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1"},{"path":"api-app/src/surfaces/webhooks/meta.controller.ts","sha256":"261bf12e6ef021e00d90000a714ff54c66e3753f85d287a95015035fb584518f"},{"path":"api-app/test/browser-server.cjs","sha256":"02354237e3c0c5f8d918f65cbb833270e2ce02469cfe3e926e3a6790abc106dc"},{"path":"api-app/test/channel-transport.e2e-spec.ts","sha256":"a143b1fdb4ba23883b731b58c78008f06714d80e16b5f077b0bf9763056ba011"},{"path":"api-app/test/conversation-start.e2e-spec.ts","sha256":"35ead6bdea966ab05a3c9b792316867a918929194570b766767bacebb5bf4f11"},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","sha256":"da6ae029d8ade6c3e7cc67809e2d971d6585a5888c72d99b294f6fd0a920324f"},{"path":"api-app/test/helpers.ts","sha256":"117e4f85c81dda37ab30e7eb23704b31538c8c5161aa7562a844eaf11de6819c"},{"path":"api-app/test/initial-message.e2e-spec.ts","sha256":"197aeba4c765168c7fba66ec56209241025a8bfc09475e3100f4be1995d0a13d"},{"path":"api-app/test/timeline-fixtures.cjs","sha256":"a8239426ffb80dd430d38fe9f3dfc29d5ad346f77f519320be25e37c1f853d81"},{"path":"api-app/test/webhooks.e2e-spec.ts","sha256":"2da81767ab4366d90ccbd214b12c9570027ea102ee9b5fb27f89aa4db129cdb5"},{"path":"web-app/e2e/start-conversation.spec.ts","sha256":"95143e86de9ffec726a95f015f24d8f7dc580f1be92a098a4cbbbb33c34c8284"},{"path":"web-app/e2e/timeline-freshness.ts","sha256":"3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53"},{"path":"web-app/src/api.spec.ts","sha256":"9712bf3c1409754f3d802f7364cb5756d92762177a0ecc01f7f09120cd38aee9"},{"path":"web-app/src/api.ts","sha256":"7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c"},{"path":"web-app/src/componentes/NovaConversa.spec.ts","sha256":"84184865db156d6c147e382982e235ea82f16ea9892cb0cc6e59f16ac1393757"},{"path":"web-app/src/componentes/NovaConversa.tsx","sha256":"2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"},{"path":"web-app/src/telas/Inbox.tsx","sha256":"66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"}],"raw_receipt_sha256":"164e31d019f8d9b30adeb5020b9c87a46bd141d8aa1c1d68e598b40cced55ebb","omission_note":"Faithful bounded view: all 259 original records are retained in the raw receipt identified by raw_receipt_sha256; this view omits 205 unrelated repeated records and preserves exact hashes for 54 critical review paths."}
```

### all-result-e70-v1.1.json — historical, not current metrics

SHA256 `d4f39cd2d44d826f7674fd69145c178ae36fbe9630098580c60f184edbd0a629`

```json
{"checkpoint":"E70 real session/race proofs pass; full ordered index fails actual accumulated-history plans","recorded_at_utc":"2026-10-23T04:29:26.411256+00:00","command":"bash scripts/test-channels-local.sh all","executor_session_id":11043,"exit_code":1,"stdout_sha256":"a2ab485cc48ace98373ddc6c444dd7aceb6f18d628d93db2c52ad2046b7e40d5","source_fingerprint":"0867ad4ad9eefb75d2a9d7ea7a1a04db605fd49c2364549c6774d876e5c1286a","full259source_postseal":true,"owned_cleanup_observed":true,"phases":{"api_lint_build":"passed","api_unit":{"files":34,"passed_tests":368},"postgresql":{"passed_files":31,"failed_files":2,"passed_tests":449,"failed_tests":2,"total_tests":451},"web_browser":"not reached"},"actual_options_plans":{"recent":{"sql":"SELECT \"public\".\"initial_message_intents\".\"id\", \"public\".\"initial_message_intents\".\"conversation_id\", \"public\".\"initial_message_intents\".\"bu_id\", \"public\".\"initial_message_intents\".\"actor_id\", \"public\".\"initial_message_intents\".\"idempotency_key\", \"public\".\"initial_message_intents\".\"owner_nonce\", \"public\".\"initial_message_intents\".\"request_fingerprint\", \"public\".\"initial_message_intents\".\"request\", \"public\".\"initial_message_intents\".\"selected_context\", \"public\".\"initial_message_intents\".\"state\"::text, \"public\".\"initial_message_intents\".\"lease_expires_at\", \"public\".\"initial_message_intents\".\"dispatch_deadline_at\", \"public\".\"initial_message_intents\".\"external_message_id\", \"public\".\"initial_message_intents\".\"slot_released_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_at\", \"public\".\"initial_message_intents\".\"risk_acknowledged_by_actor_id\", \"public\".\"initial_message_intents\".\"created_at\", \"public\".\"initial_message_intents\".\"updated_at\" FROM \"public\".\"initial_message_intents\" WHERE (\"public\".\"initial_message_intents\".\"conversation_id\" = $1 AND \"public\".\"initial_message_intents\".\"bu_id\" = $2) ORDER BY \"public\".\"initial_message_intents\".\"created_at\" DESC, \"public\".\"initial_message_intents\".\"id\" DESC LIMIT $3 OFFSET $4","params":["d71730fb-7bde-4a7e-a075-67965c7827e1","4302dccc-6fa1-498a-bf49-2ba6cfb396c5",11,0],"nodeTypes":["Limit","Index Scan"],"scannedRows":11,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":0.28,"totalCost":4.02,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0},{"type":"Index Scan","relation":"initial_message_intents","index":"initial_message_intents_options_order_idx","startupCost":0.28,"totalCost":697.54,"estimatedRows":2048,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":4,"sharedReadBlocks":0}]},"active":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"conversation_id\", \"public\".\"dispatch_admissions\".\"bu_id\", \"public\".\"dispatch_admissions\".\"caller\"::text, \"public\".\"dispatch_admissions\".\"actor_id\", \"public\".\"dispatch_admissions\".\"owner_nonce\", \"public\".\"dispatch_admissions\".\"selected_context\", \"public\".\"dispatch_admissions\".\"state\"::text, \"public\".\"dispatch_admissions\".\"expires_at\", \"public\".\"dispatch_admissions\".\"dispatch_deadline_at\", \"public\".\"dispatch_admissions\".\"released_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_at\", \"public\".\"dispatch_admissions\".\"risk_acknowledged_by_actor_id\", \"public\".\"dispatch_admissions\".\"created_at\", \"public\".\"dispatch_admissions\".\"updated_at\" FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"bu_id\" = $2 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $3 OFFSET $4","params":["d71730fb-7bde-4a7e-a075-67965c7827e1","4302dccc-6fa1-498a-bf49-2ba6cfb396c5",11,0],"nodeTypes":["Limit","Sort","Seq Scan"],"scannedRows":2304,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":220.83,"totalCost":220.86,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":182,"sharedReadBlocks":0},{"type":"Sort","relation":null,"index":null,"startupCost":220.83,"totalCost":221.47,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":182,"sharedReadBlocks":0},{"type":"Seq Scan","relation":"dispatch_admissions","index":null,"startupCost":0,"totalCost":215.12,"estimatedRows":256,"actualRows":256,"loops":1,"rowsRemoved":2048,"sharedHitBlocks":182,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, released_at, created_at DESC, id DESC, bu_id)","releasedHistory":2048,"activeHistory":256}},"actual_conflict_plan":{"sql":"SELECT \"public\".\"dispatch_admissions\".\"id\", \"public\".\"dispatch_admissions\".\"state\"::text FROM \"public\".\"dispatch_admissions\" WHERE (\"public\".\"dispatch_admissions\".\"conversation_id\" = $1 AND \"public\".\"dispatch_admissions\".\"released_at\" IS NULL) ORDER BY \"public\".\"dispatch_admissions\".\"created_at\" DESC, \"public\".\"dispatch_admissions\".\"id\" DESC LIMIT $2 OFFSET $3","params":["d71730fb-7bde-4a7e-a075-67965c7827e1",11,0],"nodeTypes":["Limit","Sort","Seq Scan"],"scannedRows":2304,"nodes":[{"type":"Limit","relation":null,"index":null,"startupCost":213.79,"totalCost":213.82,"estimatedRows":11,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":178,"sharedReadBlocks":0},{"type":"Sort","relation":null,"index":null,"startupCost":213.79,"totalCost":214.43,"estimatedRows":256,"actualRows":11,"loops":1,"rowsRemoved":null,"sharedHitBlocks":178,"sharedReadBlocks":0},{"type":"Seq Scan","relation":"dispatch_admissions","index":null,"startupCost":0,"totalCost":208.08,"estimatedRows":256,"actualRows":256,"loops":1,"rowsRemoved":2048,"sharedHitBlocks":178,"sharedReadBlocks":0}],"nativeIndex":"CREATE INDEX dispatch_admissions_options_order_idx ON public.dispatch_admissions USING btree (conversation_id, released_at, created_at DESC, id DESC, bu_id)","providerPostDelta":0,"providerCallDelta":0,"messageDelta":0},"actual_claim_probes":{"ST04_FINAL_WINDOW_CAS":{"inspectedOpen":true,"expiresAt":"2026-10-23T04:22:36.648Z","databaseClockExpired":true,"databaseNow":"2026-10-23T04:22:36.650Z","postsDeltaWhilePaused":0,"postsDelta":0,"outMessagesDelta":0,"finalState":"REJECTED","leaseBudgetMs":90000},"ST04_CREDENTIAL_PIN":{"validationSucceeded":true,"credentialUpdateWaited":true,"credentialVersionAdvanced":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":1,"sendStatus":201,"finalState":"SUCCEEDED"},"ST04_BU_READINESS_PIN":{"validationSucceeded":true,"readinessUpdateWaited":true,"postsDeltaWhilePinned":0,"postsDelta":1,"outMessagesDelta":0,"sendStatus":503,"buStatusAfterUpdate":"INATIVO","intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"},"ST04_ST05_CLAIM_OVERLAP":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":409,"deadlocksDelta":0,"postsDelta":0,"outMessages":0,"intentState":"REJECTED","receiptState":"NONE"},"ST04_ST05_LOCAL_OVERLAP":{"st05WaitedOnChannel":true,"actorGrantWaitObserved":false,"refreshStatus":200,"sendStatus":503,"deadlocksDelta":0,"postsDelta":1,"localOutMessages":0,"intentState":"EXTERNAL_ACCEPTED_LOCAL_BLOCKED","receiptState":"RECORDED"},"ST04_ORDINARY_FINAL_WINDOW_CAS":{"capturedEligible":true,"databaseWindowExpiredBeforeClaimUpdate":true,"claimGranted":false,"state":"PREPARED","dispatchDeadlineAt":null,"releasedAt":null}},"actual_assertion_reachability":["Options active no-sort and≤11 scanned fail softly; recent IndexScan11passes. Nativefullindex definition is actualexpectedneworder, yet activequerysorts/scans2304.","Conflict POST returned correct10/truncated ordinary tokens and zeroactualfakeport/Message effects; actualEXPLAINsorted/scanned2304. Its hard noSort predicate fails; subsequent≤11 predicate not reached, although metric2304 was actually emitted.","Separate native metadata test retains oldBU-leading index expectation atdispatch-admission.e2e:114; actualnewfullindex order differs. This is staleexpectation, not newDDLfailure.","Scoped real-session verifier clock and finalREJECTED/null-deadline/releasedslot assertions nowPASS. All6window/pin/refreshprobes PASS."],"classification":"Actualperformance assertion failure persists with representative accumulated released+active history; disproves tiny-table-only explanation. No cardinality/threshold/forceplanner workaround accepted. Separate stale native-metadata assertion disclosed.","next":"One SQL-only partial ordered active index and two explicitmetadata expectations, preservestrictrealplan/effect/sessiontests; freshE71ALL. No currentGREEN/browser/runtime proof."}
```

### all-source-recheck-e70-v1.1.json — historical, not current metrics

SHA256 `0599127cbf4731999ea95e3a9b6e6ceb275c68bf280d72b6a25ad03cee422a75`

```json
{"checkpoint":"E70 terminal full positive source recheck","stage":"After actual executor terminal and owned cleanup; BEFORE writer release","count":259,"fingerprint":"0867ad4ad9eefb75d2a9d7ea7a1a04db605fd49c2364549c6774d876e5c1286a","matches_preseal_full_inventory_and_bytes":true,"record_reference":"all-source-seal-e70-v1.1.json#records","stdout_sha256":"a2ab485cc48ace98373ddc6c444dd7aceb6f18d628d93db2c52ad2046b7e40d5","executor_reported_exit_code":1,"recorded_at_utc":"2026-10-23T04:27:28.333034+00:00","boundary":"Only declared positive public roots and7 exact publicfiles; no actual env/data/process inspection."}
```

### all-result-e71-v1.1.json — historical, not current metrics

SHA256 `585dc49758845a8e2e96aa33106ca8b99d03e581bc6d89f217c0315d6988157a`

```json
{"checkpoint":"E71 corrected r4 full canonical candidate GREEN","recorded_at_utc":"2026-10-23T04:54:41.212310+00:00","command":"bash scripts/test-channels-local.sh all","executor_session_id":17070,"exit_code":0,"actual_exit_code":0,"terminal_authority":"Actual terminal exit0 and owned cleanup reported by owning executor; root independently checked actual stdout aggregates, full259 inventory/bytes and93browser manifest records.","phases":{"migrations":28,"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"duration_seconds":4.02},"api_postgresql":{"files":33,"tests":451,"duration_seconds":278.62},"web_unit":{"files":7,"tests":54,"duration_seconds":0.662},"browser":{"tests":89,"passed":89,"duration_minutes":15.8}},"stdout_sha256":"9ba7f1567d32b3be71e2f6cf232e4d6786e776f4100f144036dfb424fb7a4042","source_recheck":"all-source-recheck-e71-v1.1.json","source_fingerprint":"4f35237f1d6aaf55f98e129631e17184d8f5b196249f6c56c10f210add52daf4","full259source_postseal":true,"freshness":"browser-freshness-collection-e71-v1.1.json","owned_cleanup_observed":true,"specific_proofs":["Both initial and ordinary final trusted-window CAS reject after actual database-clock expiry, within the live original lease.","Actual active BU and credential updates wait on held shared pins; current session validation uses the actual signed verifier clock seam after remote preflight.","Actual unmodified ST05 refresh overlaps claim/local completion without increasing database deadlocks; known acceptance is retained when local completion cannot commit.","Recent intents, active options and whole-conversation conflict actual captured queries each use no-sort indexed access examining11records; zero provider/Message effects in conflict.","All existing first-send, recovery, lost-response, idempotency, ownership, template, window, public/BOT, timeline and browser journeys pass in the complete shared runner."],"limits":["Disposable synthetic database and owned fake provider, not actual WhatsApp delivery.","Root integration findings require fresh complete independent r6 challenge; no review approval is inferred from tests.","No preserved runtime activation, canonical module consolidation, full canonical private-boundary diff guard, assisted own-channel first send or completed delivery."]}
```

### all-source-recheck-e71-v1.1.json — historical, not current metrics

SHA256 `02992ab892715a5e2d0135c1b9c7e9bbba9e2f14fe29d4f6a6a80e17dddeb005`

```json
{"checkpoint":"E71 terminal full positive source recheck","stage":"After actual executor terminal and owned cleanup; BEFORE writer release","count":259,"fingerprint":"4f35237f1d6aaf55f98e129631e17184d8f5b196249f6c56c10f210add52daf4","matches_preseal_full_inventory_and_bytes":true,"record_reference":"all-source-seal-e71-v1.1.json#records","stdout_sha256":"9ba7f1567d32b3be71e2f6cf232e4d6786e776f4100f144036dfb424fb7a4042","executor_reported_exit_code":0,"recorded_at_utc":"2026-10-23T04:54:17.502967+00:00","boundary":"Only declared positive public roots and7 exact publicfiles; no actual env/data/process inspection."}
```

### api-result-e72-v1.1.json — historical, not current metrics

SHA256 `21c5eec5a701f7daa3e46495745f2a190461bf3f31684ccd3b197415b76cdf98`

```json
{"checkpoint":"E72 causal test-only API RED for two r6 findings","recorded_at_utc":"2026-10-23T05:20:34.578740+00:00","command":"bash scripts/test-channels-local.sh api","executor_session_id":42676,"exit_code":1,"actual_exit_code":1,"stdout_sha256":"8bad3c08ed817a791d9fd7d10016e84da1e535e8050e3c7c34cb422618ec7030","source_fingerprint":"0f92d1121f2a2d67d29d1d4ba4c976af2648ef2a633932c11cf4f86876f84031","source_seal":"api-source-seal-e72-v1.1.json","source_recheck":"api-source-recheck-e72-v1.1.json","full259source_postseal":true,"all38protected_and_companion_bytes_match":true,"product_bytes_unchanged_from_e71":true,"owned_cleanup_observed":true,"phases":{"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"passed":368},"api_postgresql":{"files":33,"tests":456,"passed":451,"failed":5},"web_and_browser":"not reached/not part of API command"},"findings":[{"finding_id":"F-5E961B39","source_finding_id":"TQA-R6-01","classification":"actual reached causal assertion RED","actual":"All four owned helper-only malformed-row fixtures resolve instead of rejecting: empty, malformed string, multiple rows and negative bigint. One-call spy restored in finally. Existing helper is unchanged.","limits":"Does not claim actual native statistics were absent; explicitly injected required-read failure shapes in the owned fixture."},{"finding_id":"F-CF091066","source_finding_id":"ARCH-ST04-R6-01","classification":"actual reached signed-webhook/real-PostgreSQL causal assertion RED","actual":"Current associated/verified identity managedLifecycle=false receives a retained IN with non-null officialInboundAt; resolver reports windowOpen=true both before and after managed=true; duplicate replay retains that timestamp. Four soft assertions fail, while whole matrix reaches subsequent new-managed-IN positive, unread/duplicate counts and zero provider effects.","limits":"No actual outbound attempt or real provider exploit is claimed. Timestamp/window read projection is observed, not immediate dispatch authority."}],"remaining_positive_proof":"Existing final-window CAS, BU/credential pins and both actual ST05 refresh overlap cases pass, preserving original E71 fix evidence.","next":"Bounded Message acceptance owner qualification and strict statistics helper fix, preserving causal tests, protected ST05 and all source/runner/private boundaries; reseal full ALL before review/images/runtime plan."}
```

### candidate-source-preflight-e72-v1.1.json — historical, not current metrics

SHA256 `b4075ab8793abf51d96adc0d58511413f57aaf1ef2ddd84d1d5af7a5c3527659`

```json
{"kind":"E72 actual root public candidate preflight before causal API run; no test result","recorded_at_utc":"2026-10-23T05:12:51.480887+00:00","source_seal":"api-source-seal-e72-v1.1.json","source_fingerprint":"0f92d1121f2a2d67d29d1d4ba4c976af2648ef2a633932c11cf4f86876f84031","authority":"authority-e72-v1.1.json","routing":"routing-e72-v1.1.json","prior_full_candidate":"all-result-e71-v1.1.json","exact_delta":["api-app/test/initial-message.e2e-spec.ts","api-app/test/webhooks.e2e-spec.ts"],"expected_assertions":["Four missing/malformed/multiple/negative native statistics calls must reject; helper currently unchanged from E71.","Signed unmanaged current verified resource IN is retained with null provenance; management activation and duplicate replay cannot open window/upgrade old timestamp; fresh qualified managed IN does. Soft assertions reach the whole matrix."],"product_source_unchanged_from_e71":true,"all38protected_and_companions_match":true,"freeze":"No edits from preseal through actual terminal cleanup and independent full259 postseal.","limits":"Owned disposable API/PG only; no Web/browser/runtime/provider proof inferred."}
```

### api-source-recheck-e72-v1.1.json — historical, not current metrics

SHA256 `8ae8d4b89deec5199e4dd9043e99fc426ce9aa3e462db78fe0789a0cf82e9cbd`

```json
{"checkpoint":"E72 terminal full positive source recheck","stage":"After actual executor terminal and owned cleanup; BEFORE writer release","count":259,"fingerprint":"0f92d1121f2a2d67d29d1d4ba4c976af2648ef2a633932c11cf4f86876f84031","matches_preseal_full_inventory_and_bytes":true,"record_reference":"api-source-seal-e72-v1.1.json#records","stdout_sha256":"8bad3c08ed817a791d9fd7d10016e84da1e535e8050e3c7c34cb422618ec7030","executor_reported_exit_code":1,"recorded_at_utc":"2026-10-23T05:20:34.502349+00:00","boundary":"Only declared positive public roots and7 exact publicfiles; no actual env/data/process inspection."}
```

### all-result-e73-v1.1.json — historical, not current metrics

SHA256 `1d499bd79b5fe07c1de076f7ef0e68751efee8edf5fd2005f23ce54672c65087`

```json
{"checkpoint":"E73 corrected r6 actual full canonical aggregate GREEN; metrics stdout subsequently lost","recorded_at_utc":"2026-10-23T11:51:43.401697+00:00","command":"bash scripts/test-channels-local.sh all","executor_session_id":13693,"exit_code":0,"actual_exit_code":0,"terminal_authority":"Actual executor terminal0/owned cleanup; root read stdout unit/PG/Web aggregates and independently checked all259 sources and recovered actual93record browser manifest. Raw stdout later disappeared from exact owned/tmp path before PCV extraction; phase aggregates and prior hash remain observed, raw current metrics are not invented.","phases":{"migrations":28,"lint_and_build":"passed","api_unit":{"files":34,"tests":368,"duration_seconds":3.68},"api_postgresql":{"files":33,"tests":456,"duration_seconds":279.65},"web_unit":{"files":7,"tests":54,"duration_seconds":0.637},"browser":{"tests":89,"passed":89,"duration_minutes":15.8}},"stdout_sha256":"d6540b2284788bbb2333b44ae0b4cf928141fff81f191e07ed4bbda6caa11617","source_recheck":"all-source-recheck-e73-v1.1.json","source_fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","full259source_postseal":true,"freshness":"browser-freshness-collection-e73-v1.1.json","owned_cleanup_observed":true,"specific_proofs":["All967tests passed, including the five actual E72 causal regressions after the exact two bounded corrections.","Full259source freeze matches; actualE73 per-run original freshness artifact recovered and93records/bundle equality independently verified."],"limits":["Owned disposable PostgreSQL and fake provider only.","Current complete stdout/PCV extraction cannot be reconstructed after loss of the temporary output. Historical E71 metrics remain historical. Source remains frozen for a justified repeat with durable owned output.","No actual preserved runtime/provider/operator proof, completed independent r7 review, canonical module application or full-diff guard."]}
```

### all-source-recheck-e73-v1.1.json — historical, not current metrics

SHA256 `e6767e8dc2674ea603ce0212ad9535cd10e28871ba47ff053a870a4d7aceffc4`

```json
{"checkpoint":"E73 terminal full positive source recheck","stage":"After actual executor terminal and owned cleanup; BEFORE writer release","count":259,"fingerprint":"589c753670cfcf54020b785e6bae6b85ec1a8b4bab707f333f8e64d8aaf38c8e","matches_preseal_full_inventory_and_bytes":true,"record_reference":"all-source-seal-e73-v1.1.json#records","stdout_sha256":"d6540b2284788bbb2333b44ae0b4cf928141fff81f191e07ed4bbda6caa11617","executor_reported_exit_code":0,"recorded_at_utc":"2026-10-23T05:48:24.150039+00:00","boundary":"Only declared positive public roots and7 exact publicfiles; no actual env/data/process inspection."}
```

### browser-freshness-collection-e73-v1.1.json — historical, not current metrics

SHA256 `7ea0d45d3bd3b5003bf60b1c572a7a2b56b2e42dfa0d45d611ebe418c919fc62`

```json
{"kind":"Independent root recovered actual E73 pre-worker browser attestation collection","checkpoint":"E73","source_seal":"all-source-seal-e73-v1.1.json","attestation_sha256":"eaf31a6c2176294c877fe2fade88ef034b2cc562a851359440e38041c0ccec19","run_id":"2026-10-23T05-30-49-426Z","captured_at_utc":"2026-10-23T05:30:49.426Z","runtime":"v22.23.3","completed_migrations":28,"current_api_head":"db5a86758a165fac8a1ab587599c37b17890530c","current_web_head":"74b9d4b714044829796f875d00553f077c1c329d","served_dist_bundle_equal":true,"served_bundle_sha256":"f8e97efa6777dbc496b74cd527b1bae78e7766e4a4d58f752f7816cb62444343","manifest_count":93,"all_manifest_records_match_presealed_sources":true,"manifest_checks":[{"path":"api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261022140000_initial_message_orchestration/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261022150000_initial_message_admissions/migration.sql","matches":true},{"path":"api-app/prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql","matches":true},{"path":"api-app/prisma/schema.prisma","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.spec.ts","matches":true},{"path":"api-app/src/domain/channels/channel-credential-resolver.ts","matches":true},{"path":"api-app/src/domain/channels/transport/channel-dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/channels/transport/channel-initial-message.spec.ts","matches":true},{"path":"api-app/src/domain/channels/transport/channel.ts","matches":true},{"path":"api-app/src/domain/historico/catalogo.ts","matches":true},{"path":"api-app/src/domain/historico/cobertura.ts","matches":true},{"path":"api-app/src/domain/inbox/channel-window-policy.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/channel-window-policy.ts","matches":true},{"path":"api-app/src/domain/inbox/conversation-start.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/conversation-start.service.ts","matches":true},{"path":"api-app/src/domain/inbox/conversations.service.ts","matches":true},{"path":"api-app/src/domain/inbox/dispatch-admission.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/dispatch-admission.service.ts","matches":true},{"path":"api-app/src/domain/inbox/incoming.service.ts","matches":true},{"path":"api-app/src/domain/inbox/incoming.typebot.integration.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message-template-renderer.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/initial-message.service.ts","matches":true},{"path":"api-app/src/domain/inbox/message-acceptance.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/message-acceptance.service.ts","matches":true},{"path":"api-app/src/domain/inbox/outbound.service.spec.ts","matches":true},{"path":"api-app/src/domain/inbox/outbound.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-definition.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-draft.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.dependencies.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.spec.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-management.ports.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-observation.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-submission.service.ts","matches":true},{"path":"api-app/src/domain/message-templates/template-transaction-boundary.ts","matches":true},{"path":"api-app/src/integrations/channels/account-reference.ts","matches":true},{"path":"api-app/src/integrations/channels/channel-adapter-factory.ts","matches":true},{"path":"api-app/src/integrations/channels/channel-adapter-registry.ts","matches":true},{"path":"api-app/src/integrations/channels/channel-transport.module.ts","matches":true},{"path":"api-app/src/integrations/channels/evolution-channel.ts","matches":true},{"path":"api-app/src/integrations/channels/meta-channel.ts","matches":true},{"path":"api-app/src/integrations/channels/prisma-channel-resolver.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.spec.ts","matches":true},{"path":"api-app/src/integrations/evolution/evolution.client.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.module.ts","matches":true},{"path":"api-app/src/integrations/message-templates/template-management.resolver.ts","matches":true},{"path":"api-app/src/integrations/meta/initial-message.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/initial-message.client.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/message-template.client.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.spec.ts","matches":true},{"path":"api-app/src/integrations/meta/meta.client.ts","matches":true},{"path":"api-app/src/surfaces/bff/bff.module.ts","matches":true},{"path":"api-app/src/surfaces/bff/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/bff/message-templates.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/conversations.controller.ts","matches":true},{"path":"api-app/src/surfaces/public/public.module.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/meta.controller.ts","matches":true},{"path":"api-app/src/surfaces/webhooks/webhooks.module.ts","matches":true},{"path":"api-app/test/api-publica.e2e-spec.ts","matches":true},{"path":"api-app/test/atendimento.e2e-spec.ts","matches":true},{"path":"api-app/test/browser-server.cjs","matches":true},{"path":"api-app/test/channel-transport.e2e-spec.ts","matches":true},{"path":"api-app/test/conversation-start.e2e-spec.ts","matches":true},{"path":"api-app/test/dispatch-admission.e2e-spec.ts","matches":true},{"path":"api-app/test/helpers.ts","matches":true},{"path":"api-app/test/initial-message.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-bff.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-drafts.e2e-spec.ts","matches":true},{"path":"api-app/test/message-template-management.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-bci.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-pcv.e2e-spec.ts","matches":true},{"path":"api-app/test/number-onboarding-typebot.e2e-spec.ts","matches":true},{"path":"api-app/test/timeline-fixtures.cjs","matches":true},{"path":"api-app/test/webhooks.e2e-spec.ts","matches":true},{"path":"web-app/e2e/channel-transport.spec.ts","matches":true},{"path":"web-app/e2e/message-templates.spec.ts","matches":true},{"path":"web-app/e2e/number-onboarding-freshness.ts","matches":true},{"path":"web-app/e2e/start-conversation.spec.ts","matches":true},{"path":"web-app/e2e/timeline-freshness.ts","matches":true},{"path":"web-app/src/api.spec.ts","matches":true},{"path":"web-app/src/api.ts","matches":true},{"path":"web-app/src/App.tsx","matches":true},{"path":"web-app/src/componentes/NovaConversa.spec.ts","matches":true},{"path":"web-app/src/componentes/NovaConversa.tsx","matches":true},{"path":"web-app/src/telas/Inbox.tsx","matches":true},{"path":"web-app/src/telas/Modelos.spec.ts","matches":true},{"path":"web-app/src/telas/Modelos.tsx","matches":true}],"recovery":{"original_actual_synthetic_artifact":"foundation_documentation/artifacts/tmp/inbox-timeline-execution/attestation-browser-2026-10-23T05-30-49-426Z.json","original_and_recovered_bytes_equal":true,"rejected_export":"browser-attestation-rejected-e73-v1.1.json","method":"Exact known positive Foundation artifact generated during E73 globalSetup, recovered after the executor initially copied a stale authority file. Current per-run original independently read and compared byte-for-byte by root. No source mutation/rerun/reconstructed runtime attestation. Underlying stale-container-path cause remains unproven."},"limits":"Disposable synthetic proof only; existing declaredBaseline fields do not replace approved baselines. No preserved runtime/provider proof."}
```
