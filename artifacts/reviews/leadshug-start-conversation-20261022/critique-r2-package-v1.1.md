# ST-CON-04 v1.1 — current no-code planning review

You are a fresh internal no-context reviewer, not an implementer. No tools/edits/provider calls. Assess this bounded packet and return required JSON. This is planning on delivered local ST-CON-06 and ST-CON-05, NOT executable approval or delivery review. User requested the next planned step: initiate a conversation by contact and initial text/approved-template send. Explicit APROVADO for THIS current04 is still absent. Existing05 APROVADO and proof do not approve04. Foundation baseline freeze was committed and pushed before this review. Earlier19/20 planning is historical, not current authority.

Diagnosis (current sources embedded): Channel has only sendMessage(TextMessage); abstract resolver scopes ordinary conversational origin/verified ingress. Common OutboundService owns send and existing outcome mapping, MessageAcceptanceService owns keyed Message transaction, then outbound finalization currently uses separate transaction. No manual BFF open route. Conversation unique(buId,contact) already exists. Stored-IN-createdAt currently opens window without official/provider-resource qualification. Signed Meta webhook currently discards provider timestamp. Management capability/catalogue/projector now exists and must be reused; getTemplate(id) alone checks grant/object ID but not fresh parent-account membership. Management module imports transport for credential owner, so reverse management injection into common transport would cycle. UI current Inbox has monotonic generation/draft ownership. All68 inherited dirty source hashes and3 product HEADs match delivered code; no code/tests/runtime/env/private paths touched for planning.

Root-selected proposal for challenge: one Channel.sendMessage text|approved-template union plus declared supportedKinds; typed unsupported BLOCKED zeroHTTP, same abstract method with optional generic beforeDispatch fence (no concrete branch/noop/cast). Explicitly supersede only text-only payload restriction, preserving DIP and management segregation. Common Outbound dispatch/sole MessageAcceptance retained with tx-capable collaboration; initial coordinator composes both modules without cycle. Shared catalogue observation<=300s never authorizes send: new attempts do bounded same-account current filtered reads and exact definition/status match. Dedicated Meta initial protocol client remains inside SAME bound Meta Channel. All remote preflight before positively committed initial dispatch claim; one POST, no auto retry; local-only recovery, irreversible slot release, no fuzzy echo. Nullable signed officialInboundAt+current resource drives all consumers, with no backfill and preserved timeline createdAt. Code has none of this04 functionality yet.

Current r1 architecture opinion recommends C with four finite material corrections integrated before critique-r1, which confirmed they are addressed at contract level. Critique-r1 requested only a medium initial acknowledgment deadline clarification and low inherited automation compatibility case. Both are integrated in the current normative appendix and matching Scope/DoD/Val/consumer/strict path contracts, published in refreshed freeze a107a6ab. Initial dispatchDeadlineAt equals original reservation DBtime+90s; both allowed uncertain/blocked states wait until it, before it409 ACK_TOO_EARLY with no release, no renewal. Opening invokes no bot and preserves NOVA_CONVERSA=row creation, so later first inbound into manual empty row does not trigger it; keyword behavior preserved, focused integration cases added. This fresh affected critique-r2 carries both prior reviews and dispositions forward and checks the finite clarification plus any actually exposed material regressions across the complete gate-satisfying packet. Do not reopen accepted architecture merely as style preference or ignore explicit initial deadline defined at the end of current TODO. Exact full-context explicit initial resolver/final text-window fence; original CAS before same-owner acceptance self-mutation and whole-local-tx rollback/readback/one re-entry; POSITIONAL initial renderer over unchanged catalog components/authoring flags; per-owner ordinary admission tokens coexist but exclude initial reservation under same conversation lock. PREPARED can expire only before positive SENDING claim; uncertain SENDING never time-takes-over, only settlement or explicit local risk acknowledgment after deadline. Late owner-CAS release cannot touch successor. Ordinary mappings and concurrency remain outside the bounded admission change, no ordinary retry/idempotency platform. No DB locks across HTTP. Supplemental acceptance owner source seal is included. Current critique must assess the actual integrated design and completeness of Scope/DoD/Val/strict paths/risk/matrices, carry prior rationale forward, and reopen only materially unresolved loci. No generic operation/outbox/plugin expansion. Old architecture r1 packet is immutable historical input to this current critique; the current TODO and resolution govern the proposed changes.

Future validation is planned, not executed. Canonical runner bash scripts/test-channels-local.sh all is already public-only and must stay sealed unless real new approved need. Existing802 are05 baseline only, never04 proof. Future test-first domain/raw protocol/real PostgreSQL barriers+commit ACK faults; real-BFF Playwright fresh bundle; candidate security/performance/PCV/TQA/adherence/final/cutover; preserved local additive migration only after disposable GREEN; source-image-running proof; assisted unofficial first text+reply and actual APPROVED official template+reply. Unknown approval enum/current runtime readiness cannot be inferred. No actual provider operation before explicit own-contact test authorization. Private existing local cohort only, no product Git/promotion/Railway. OPS-R4-01/SEC-R6-04/TQA-ST05-03 carried accepted limits, not new fixes or broader exposure.

Primary external verification: official Meta text/Markdown anonymous200 after web-reader429, receipt URLs/hashes in packet. Templates are Messaging-account assets; only APPROVED status sends, NAMED/POSITIONAL have different value ordering. send-messages and managing-messaging-accounts document optional messaging_account_id in2026, required to disambiguate token access to multiple accounts on same phone; choosing server-bound intended account explicitly avoids automatic ambiguity. Meta recommends + and full country code on recipient wire (domain storage stays digits). API acceptance is separate from delivery. Source policy and local proposal deliberately exclude calls and other window openers. No third-party search results used for protocol decisions; no real account/credential checked. Public doc summaries are distinct from live provider proof.

Review full applicable architecture/planning rubric: correctness/adherence, concrete scope+DTO/state transitions, security and uncertainty, bounded query/HTTP budgets, performance, elegance and structural soundness, operational fit, realistic validation/failure modes and dependency ownership. Findings first severity ordered and exact paths. The current TODO describes selected proposals and still-required review/guard fields, not false review success. Do not rewrite whole architecture absent material defect or insufficient concrete contract. No field can derive execution authority from this review. Full exact current sources and TODO follow.


---
## foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
SHA256 ede1f80fc4d30427c49ad39ed419ef1c233cd78c6a4bf0f9134fd7799bb40919

```
# Tactical TODO — ST-CON-04

## Title

LeadsHug — ST-CON-04: abrir conversa por contato e conduzir o primeiro envio com segurança

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** NotStarted
- **Version:** 1.1
- **Created:** 2026-10-19; materially rebased 2026-10-22
- **Template provenance:** copied from `delphi-ai/templates/todo_template.md` before refinement.
- **Authority:** this is a planning contract only. No current `APROVADO` exists for ST-CON-04.

## Context

ST-CON-06 entregou o transporte abstrato textual, adapters Meta/Evolution, resolução scoped e um `OutboundService` compartilhado; ST-CON-05 entregou autoria/submissão e o catálogo/projetor compartilhado de templates. Ambos permanecem contratos entregues e evidência de dependência, não aprovação desta história. A inbox ainda não permite iniciar atendimento manual por contato e conduzir o primeiro envio oficial de modo recuperável.

Este v1.1 substitui a autoridade ativa da minuta revisada em 2026-10-19. O original e suas decisões/reviews são preservados pelo owner do pacote como `historical-planning-20261019-20261020.md`; nada daquele ciclo é evidência de revisão, guard, aprovação ou execução deste texto. Os handoffs de ST-CON-06 e ST-CON-05 continuam como contexto factual.

**Perfil desta etapa:** Strategic / CTO-Tech-Lead; escopo ativo NestJS, React, Vite, PostgreSQL, Prisma e Docker. Genesis foi rejeitado: o projeto canônico já existe. Próximo handoff planejado: Operational / Coder após contrato congelado, reviews/guards atuais e aprovação humana explícita. Supporting profiles: Assurance / Tester-Quality, Assurance / Security-Adversarial e Operational / DevOps para os respectivos gates. Seleção declarada conforme `delphi-ai/workflows/docker/profile-selection-method.md`.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md`
- **Primary story ID:** ST-CON-04
- **Why this is the right current slice:** sequência humana confirmada: cadastro → preparar/submeter template em ST-CON-05 → abrir/reusar conversa e conduzir primeiro contato → importação/histórico em fatia futura. Um fluxo inicial assistido, sem CRM, campanha ou operação em lote.
- **Direct-to-TODO rationale:** n/a; brief existente.

## Contract Boundary

- Este TODO define **WHAT** será entregue; `Assumptions Preview` e `Execution Plan` registram a proposta **HOW** para revisão.
- O escopo é fechado ao início manual e primeiro envio de uma conversa. Qualquer alteração material de Scope, DoD, validação, contrato público ou decisões requer retorno à revisão e nova aprovação antes de execução.
- “Aceito” significa ID externo válido persistido; não significa entrega ao aparelho nem leitura.
- Baseline inicial publicado antes dos primeiros guards/review; parecer arquitetural r1 integrado abaixo. Mudanças materiais decorrentes do parecer serão publicadas em novo freeze antes da crítica. Nenhuma implementação ou aprovação humana é reivindicada.

## Implementation Intent

- **Current delivery:** propor abertura/reuso BU+contato e um primeiro envio de texto livre quando a política permite ou de template textual Meta aprovado quando necessária a janela oficial, com intenção durável e recuperação sem reenvio cego.
- **Planned next steps:** congelar esta revisão; executar fresh architecture opinion, crítica independente e guards de planejamento; resolver findings; somente então submeter o contrato para APROVADO humano.
- **Anticipatory implementation authorized now:** none.
- **Rationale:** reaproveitar os owners existentes de conversa, transporte, aceitação de Message e catálogo. O fluxo novo coordenará uma intenção durável; não duplicará sender, aceitação ou catálogo.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** publicar o contrato com as duas clarificações da crítica r1 e conferir a revisão afetada antes dos guards finais de planejamento.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** parecer arquitetural e crítica r1 concluídos; clarificações finitas de deadline e automação estão integradas, aguardando freeze atualizado e crítica r2.
- **Exit condition:** review/guards do texto corrente convergidos e decisão humana explícita; execução exige ainda authority guard `go`.

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

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; não há entrega reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

n/a; planning draft em revisão, não marcado blocked.

## Execution Lane Tracking (Required)

- **Local implementation branches:** api/web/root conforme branch declarada pelo owner no handoff; Foundation permanece `main`. Não executar nesta etapa.
- **Promotion lane path:** local → lanes definidas pelos TODOs/repos após approval; não assumidas neste planejamento.
- **Lane-promoted threshold:** pending contract/review.
- **Production-ready threshold:** fora da autorização atual.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

n/a nesta etapa; nenhum código, promoção ou implantação autorizado.

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
| api | test/number-onboarding-pcv.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
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
| api | test/number-onboarding-typebot.e2e-spec.ts | any | Inherited baseline ONLY, NO new mutation; byte-exact seal required |
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

## Scope Planning Matrix

| Scope ID | Contract outcome | Owner/boundary | Planned evidence after approval | Planning status |
| --- | --- | --- | --- | --- |
| SCOPE-01 | sessão BFF com CSRF e papel ATENDENTE+; criar/reusar atomicamente a conversa única por BU+contato, com telefone obrigatório normalizado a 8–15 dígitos sem inferir país/DDI | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-02 | endpoints autenticados BFF para opções, preview, criação de intenção, leitura/reconciliação/acknowledgment; UUID idempotency por BU+ator; slot ativo por conversa; request/context/fingerprint imutáveis | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-03 | manter readiness e `requiresWindow`; introduzir `Message.officialInboundAt` nullable somente de IN Meta assinada e verificada com timestamp inteiro positivo, não futuro e identidade/resource gerenciados | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-04 | proposta sob revisão: estender a única abstração `Channel.sendMessage` a um union discriminado `text | approved-template`, acompanhado de `readonly supportedKinds`; Meta declara ambos; Evolution declara text e responde `BLOCKED/UNSUPPORTED_KIND` antes de qualquer HTTP para template | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-05 | reutilizar exatamente `GET/POST /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` e seu domínio, projector, lease/fence, TTL de 300s e parser de enum entregues por ST-CON-05 | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-06 | BODY textual NAMED/POSITIONAL, header/footer somente estáticos; sem botão, mídia, auth, flows, arbitrary Graph payload ou ampliação de categorias suportadas | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-07 | coordenador de intenção vive no domínio inbox e chama o `OutboundService` comum; reutilizar seu dispatch abstrato e `MessageAcceptanceService` como único owner de Message | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-08 | UUID keyed por BU+actor; replay do request canônico acontece antes de leituras de provider, respeitando grant atual | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-09 | composer BFF existente deve bloquear, antes de qualquer HTTP, conversa nova/vazia ou qualquer slot inicial não resolvido | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-10 | readiness permanece RECEIPT/identidade própria/epoch/estado CONECTADO/`activeCredentialVersion`; management purpose não desvia a prova de envio | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-11 | depois de candidate GREEN, assurance de imagens e migration descartável/local, validar primeiro envio assistido não oficial, template oficial realmente `APPROVED` próprio e reply do destinatário | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |
| SCOPE-12 | dependency/fake substitutability, testes negativos Evolution zero HTTP, regressões de texto BFF/public/BOT, janela/projeções batched, timeline/cursor e performance | named owners/boundaries in Scope | exact domain/contract/PG/browser evidence from this criterion | planned; no current evidence |

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

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | opening invokes no automation; manual-open-without-send then first inbound leaves NOVA_CONVERSA false while keyword automation retains its predicate; authorized operator opens/reuses BU/contact atomically; no side effects listed in SCOPE-01 occur; new conversation has truthful empty state and deterministic list ordering. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-02 | Definition of Done | stale/foreign BU, actor, slot, selected channel, grant, credential epoch/version, conversation generation, template fingerprint, or policy context fails closed before external dispatch. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-03 | Definition of Done | Preview is escaped, deterministic, local/read-only and context-bound; supported textual subset and exact limits are enforced server-side. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-04 | Definition of Done | existing Channel consumers remain substitutable; Meta supports declared text/template kinds; Evolution template is typed unsupported with zero HTTP; no second send method/provider branching outside adapters or DI cycle; immutable descriptor plus same-operation fence preserves common dispatch. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-05 | Definition of Done | prove commit certainty at reservation/dispatch-claim/receipt/release, including real commit with lost ACK and real rollback; every remote eligibility/grant/phone GET completes before durable SENDING claim; the abstract fence CAS-claims immediately before one POST, and expiry of PREPARED during delayed preflight produces zero POST. Each initial attempt dispatches at most one POST; failures are classified truthfully; known provider ID is durably separate from local Message; recovery never contacts provider and never creates a Message without external ID. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-06 | Definition of Done | initial transaction locks identity then conversation, checks original pre-HTTP status/owner CAS before acceptance mutates updatedAt, permits eligible acceptance when status CAS fails, and recovers unique conflict by whole-local-transaction rollback/readback/re-entry at most once; MessageAcceptance remains sole Message owner and existing sender/error behavior is preserved; CAS prevents late initial outcome from changing concurrent claim/close/owner or reacquiring released slot. Initial acknowledgment in either allowed state waits for immutable dispatchDeadlineAt; before it409 ACK_TOO_EARLY and zero release. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-07 | Definition of Done | official window uses only qualified trusted Meta IN timestamp for selected resource; all current BFF/public/BOT availability and send policy consumers use the same rule; timeline/cursors and performance bounds hold. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-08 | Definition of Done | owner-scoped ordinary admissions and exclusive initial reservation serialize under the same conversation lock without serializing ordinary-versus-ordinary sends; uncertain dispatched tokens block initial reservation until settlement or explicit risk acknowledgment, never time takeover; late owner release cannot touch successor; existing composer is blocked before HTTP for new/empty/unresolved slot; public/BOT respect slot and retain existing mappings; text regressions pass. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-09 | Definition of Done | NAMED and POSITIONAL initial support is derived by the initial text renderer from the unchanged catalog components/format, independently of inherited authoring flags; exact full context binds management descriptor to selected transport and final text-window fence; current eligibility is checked before every new official template dispatch via bounded same-account reads; template is actually APPROVED; Meta request pins server-captured `messaging_account_id`, uses `+` plus full DDI, and preserves existing ordinary text semantics. Tests cover same-country and cross-country recipients. Official raw reference receipt confirms account pin and recipient formatting; actual own-account readiness remains unverified. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-10 | Definition of Done | per actor/account limits, tenant isolation, request/deadline budgets and zero-network recovery are demonstrated with real bounded counters/barriers. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-11 | Definition of Done | additive migration passes explicit preflight and disposable local validation without reset/drop; current source/image/API freshness and approved local validation topology are proven. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-12 | Definition of Done | assisted proof: operator sends first unofficial message, an actually APPROVED official template, receives a reply; no auto-contact; if eligible approved asset is unavailable, completion remains blocked. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| DOD-13 | Definition of Done | architecture/adherence/security/performance/TQA/final/cutover/debt and delivery guards pass at their required stages; no open P1/P2; constraints SEC-R6-04, OPS-R4-01, TQA-ST05-03 remain truthfully carried. | test/runtime/review/migration | exact future artifact/command to be frozen after approval | local disposable PG + real BFF/browser + owned local origin | planned | no v1.1 execution evidence exists |
| VAL-01 | Validation Steps | include real PG integration open-without-send→first inbound with isolated NOVA_CONVERSA trigger (no bot start), separate PALAVRA_CHAVE fixture (retained), and no automation on open; after approval only, run contract/unit/dependency harness and exact existing BFF/public/BOT textual regressions; no test execution is part of this planning draft. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-02 | Validation Steps | initial acknowledgment before deadline rejects without release; at/after deadline permits only classified states, successor admission and late original result stay fenced; PostgreSQL race/barrier and fault injection for unique BU/contact creation, idempotent replay, delayed remote preflight vs PREPARED expiry with zero POST, claim immediately before POST, claim/close during HTTP, timeout/late provider result, ack/release then successor; assert provider counters and no lock-held HTTP; both ordinary/initial admission orderings, ordinary concurrency preserved, suspension before/after claim, uncertain token never expires into takeover, owner-CAS late release; real rollback/commit-ACK-loss at all four local boundaries; pre-acceptance CAS and echo-first conflicts. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-03 | Validation Steps | adapter substitution and raw protocol tests; Evolution template unsupported produces zero requests; Meta pages/status/account membership limits and same-account exact tuple are bounded; NAMED and POSITIONAL end-to-end order; closed-window template allowed, text-window expiry during preflight blocked, every descriptor/context dimension mismatch blocked before POST. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-04 | Validation Steps | signed webhook cases for valid, absent, malformed, future, nonofficial, duplicate and old timestamps; assert nullable provenance and unchanged timeline/cursors. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-05 | Validation Steps | same trusted-window policy across BFF/public/BOT availability and dispatch; EXPLAIN/query count for large OUT-heavy and no-IN histories; enforce batched consumer bounds. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-06 | Validation Steps | Playwright on freshly served React/Vite bundle + real BFF/PostgreSQL: open/reuse, preview, stale context, create/replay/read/reconcile/ack, safe errors, refresh, composer block, preserve draft, keyboard flow. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-07 | Validation Steps | migrations: explicit additive preflight, lock timeout 5s, statement timeout 60s, disposable TEST target, migration deploy/status and rollback assessment; never reset/drop or run before separate authorized implementation stage. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-08 | Validation Steps | local source-bound API/Web activation and owned stable/temporary HTTPS only under later approved runtime plan; assisted own-channel proofs as DOD-12. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |
| VAL-09 | Validation Steps | run appropriate architecture, critique, assumption/code, review drift, decision adherence, module consistency, security, performance/concurrency, TQA, final, cutover and completion guards after their proper lifecycle stages. Architecture planning r1 exists; other planning/delivery gates require their actual current artifacts. No implementation validation is claimed. | test/runtime/review/manual | exact future artifact/command to be frozen after approval | n/a until approved execution | planned | no v1.1 execution evidence exists |

## External Reference Evidence

Official primary references consulted 2026-10-22: [WhatsApp Send Messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages/), [Messaging account model](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/messaging/), and [Template fundamentals](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview/). Raw response provenance, hashes, lengths and paraphrased facts are in root-owned `artifacts/reviews/leadshug-start-conversation-20261022/evidence/meta-primary-reference-receipt-v1.1.json`. These docs establish protocol facts, not own-account readiness or actual asset approval.

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status (`unknown|healthy|degraded|failing|rate-limited|stale`) | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Meta official raw contract/docs | confirm exact send wire fields and recipient formatting | `healthy` | 2026-10-22 | anonymous official HTTP `Accept: text/markdown`; provenance receipt above | pin server-captured `messaging_account_id`; use `+` plus full DDI; no fallback/retry on rejection |
| Meta own account approved asset | real proof requires actually APPROVED eligible template | `unknown` | not probed in this planning turn | future operator-assisted proof only | no fixture substitutes; unavailable asset prevents completed claim |
| Existing local runtime/readiness | delivery needs current clean candidate and disposable validation | `stale` | not reprobed for this task | future DevOps handoff | source-bound assurances and topology re-resolution required |
| ST-CON-05 catalog | shared template observation/lease/fence/TTL and remote port | inherited delivered contract | 2026-10-22 handoff | completed TODO, not re-run here | reuse unchanged; any required mutation returns to review |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto` for this rebase; future implementation `operational-coder` after approval.
- **Active technical scope:** `nestjs`, `react`, `vite`, `postgresql`, `prisma`, `docker`.
- **Expected supporting profiles:** `assurance-tester-quality`, `assurance-security-adversarial`, `operational-devops` at their gates.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto` (not run in this planning task).

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Operational / Coder | after v1.1 contract freeze, fresh reviews/guards, and explicit APROVADO | scoped product paths in diff contract | planned; no implementation authority |
| Operational / Coder | Assurance / Tester-Quality + Security | independent delivery evidence after implementation | harness/evidence package | planned |
| Operational / Coder | Operational / DevOps | disposable migration, source-bound local activation and assisted proof | approved local runtime only | planned |

## Complexity

- **Level (`small|medium|big`):** `big`
- **Checkpoint policy:** one writer, principal checkout, explicit review checkpoints; no worktrees/copies.
- **Why this level:** cross-module public contract, persistence, transport, authentication, external side effect and recovery semantics.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/inbox-and-conversations.md`
- **Secondary module docs:** `foundation_documentation/modules/integrations-and-channels.md`; completed ST-CON-05 owner TODO reference (no new template module).
- **Planned decision promotion targets:** inbox module first-send/open/recovery and trusted-window sections; integrations module Channel payload/capability and scoped resolver section.
- **Module decision consolidation targets:** same sections only after implementation and reviews; no module docs edited in this planning slice.

## Decision Pending (Resolve Before Freeze)

Nenhuma escolha de produto delegada ao operador nesta etapa: recomendações D-01..D-10 abaixo definem a proposta concreta. Revisores devem desafiar defeitos materiais antes de APROVADO. Readiness/asset APPROVED e prova física são dependências futuras explícitas, não fatos presumidos.

## Decisions (Resolved Before Freeze)

Decisões selecionadas para revisão, ainda sem aprovação de execução. A alternativa C de D-02 é a recomendação concreta. Mudança material após reviews exige reconvergência e freeze atualizado antes de pedir aprovação.

- [x] D-01 — preserve BU+contact uniqueness and current grant; required 8–15 digit normalized DDI without country guess. No CRM/provider side effects on open. New conversation `QUEUED`, unread zero, lastMessageAt null; order empty rows by COALESCE(lastMessageAt,createdAt).
- [x] D-02 — alternatives: **A)** a second `sendTemplate` Channel method (splits the abstract operation and adds obligations to every adapter); **B)** parallel concrete sender (bypasses scoped resolver/common acceptance); **C)** one `sendMessage` with discriminated text/template union and readonly `supportedKinds` (selected proposal). C intentionally supersedes ST-CON-06's delivered text-only payload while retaining one method. Avoid DI cycle: `TemplateManagementModule` already imports `ChannelTransportModule`, therefore `ChannelTransportModule`/`OutboundService` must not import or inject management. Initial orchestration composes both, reuses `listTemplates/getTemplate`, and passes a validated immutable provider-agnostic descriptor plus optional generic per-attempt dispatch fence through the same `sendMessage`; management port gets no send method. Meta send client completes its remaining grant/phone GETs, then calls the fence to CAS-claim immediately before POST, chained with current-context guard. No network/retry in fence/transaction, provider branching in domain/consumers, casts/`instanceof`, or generic plugin platform. Reviewer assesses substitutability, dependency/harness, blast, maintenance and performance.
- [x] D-03 — initial-intent coordinator belongs to inbox; calls common `OutboundService` dispatch and sole `MessageAcceptanceService`. If needed, add scoped transaction collaboration to that owner while preserving current wrapper. Do not copy sender, acceptance or finalization into coordinator; no claim existing transaction integration already exists. Normative r1 explicit initial selection/context equality and payload/window-specific fence below are part of this decision.
- [x] D-04 — new nullable officialInboundAt is written only from verified signed Meta IN timestamp passing positive integer/nonfuture/resource identity checks. No backfill. Window is max trusted IN on selected current resource and conversation `<24h`; same policy for sender and availability/batched BFF/public/BOT projections. Preserve createdAt timeline/cursors; use bounded index and retain ST06 index.
- [x] D-05 — shared ST-05 catalog route/projector only. Preview route `POST /api/bff/conversations/:id/initial-message-preview` is local/read-only. Before each new template send, recheck same-account current asset by trusted observed name using existing `listTemplates`, at most two filtered pages, and require exhausted exact ID/name/language/semantic match; `getTemplate(id)` alone does not prove account membership. Official raw reference receipt confirms optional supported `messaging_account_id`; pin the server-captured account. Meta recipient wire format is `+` plus full DDI while domain identity remains canonical digits; no fallback/retry on rejection. Normative r1 initial renderer validates POSITIONAL independently of inherited authoring flags and fingerprints unchanged catalog components.
- [x] D-06 — endpoints: `POST /conversations/:id/initial-messages`; `GET start-options`; `GET attempt`; authenticated `POST reconcile` and `POST acknowledge`. UUID per BU+actor; replay canonical request before provider reads after current grant check. PREPARED lease 90s. All remote asset/grant/phone preflight GETs complete before the SENDING claim; a generic dispatch-fence hook on the same `sendMessage` CAS-claims immediately before the sole POST. Expiry during preflight proves zero POST. Pre-dispatch failure rejects/releases; uncertain SENDING locks slot as AMBIGUOUS. Persist known external ID separately before local acceptance; recovery is local-only, with no fuzzy echo or missing-ID Message. Acknowledgment follows explicit classification and irreversibly releases; a late result cannot reacquire slot or mutate newer owner/status. Normative r1 transaction ordering and exact readback/one local re-entry applies. Initial risk acknowledgment for either allowed state waits until original persisted dispatchDeadlineAt=reservationDBtime+90s, never renewed; early409 ACK_TOO_EARLY.
- [x] D-07 — composer BFF blocks new/empty/unresolved slot before any HTTP; public/BOT must honor same active slot before dispatch without global durable-intent conversion; preserve existing mappings outside this bounded change. O resultado novo é BLOCKED, code INITIAL_SEND_IN_PROGRESS, HTTP409, somente attemptId local autorizado e safe state; nenhuma rede. Sem slot, callers antigos seguem fluxo anterior. BFF /messages em conversa sem mensagem de transporte retorna INITIAL_SEND_REQUIRED409; API pública/BOT sem slot preservam seu fluxo próprio existente. Ver Dispatch Interlock abaixo. Normative r1 owner-token admission, no time takeover of uncertain dispatch and separate local-only token recovery applies.
- [x] D-08 — template renderer supports text BODY NAMED/POSITIONAL, static header/footer only, <=20 params and stated length bounds. Preview binds exact conversation/contact/context/fingerprint, escaped and read-only. Catalog observation at most 300s is not send authorization.
- [x] D-09 — maximum six GETs / one POST per new official template attempt, 10s each, 75s budget <90s lease; limits 10/min actor, 60/hour canonical account/resource. Official raw-contract receipt confirms account pinning and recipient formatting; actual account/asset readiness remains unknown. Disposable local TEST migration only after approval, explicit preflight, lock5s/statement60s, no reset/drop. Local proof sequence as DOD-12.

- [x] D-10 — Certeza local: reserva, claim, persistência de ID externo/recibo e release de slot exigem confirmação positiva ou readback exato da chave capturada após erro de commit. Erro Prisma não prova rollback. Sem confirmação de claim original não há POST; persistência incerta não libera slot nem admite nova tentativa. ACK externo conhecido permanece CONFIRMED e nunca vira recusa por falha local. Persistência do fato/Message e projeção/realtime são dimensões separadas, sem falso RECORDED. Provar rollback real e commit real com perda do ACK em cada fronteira com PG, sem protocolo genérico de operações. Hash opaco canônico de conta usa o namespace existente meta-waba+NUL+accountId; extrair helper de integração preservando bytes/ST05observations, e expor só referência opaca no contexto do canal, nunca aceitar accountId do browser.

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

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/architecture-r1.merge.json + architecture-r1-resolution.md; four material findings integrated into the contract, subject to fresh critique before approval
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **No-go handling:** unresolved material divergence returns to contract/review; no approval or completion claim.

## Gate: Review Baseline Freeze

- **Gate decision:** required
- **Why this decision:** current proposed04 package must be published before reviews.
- **Trigger stage:** before first planning review/guard
- **Baseline branch:** main
- **Baseline commit:** a107a6ab73172c70ef18dc3a34c8681d5e1b5f31
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** architecture r1 and critique r1 completed; both finite critique clarifications published in refreshed freeze a107a6ab before affected fresh critique r2; only gate metadata added afterward.
- **Evidence / reference:** Foundation main a107a6ab73172c70ef18dc3a34c8681d5e1b5f31 pushed origin/main, exit0; evidence/freeze-after-critique-r1-v1.1.json records actual publication.
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
- **Findings summary:** current v1.1 proposed baseline; guard not_run until fresh review convergence.
- **Evidence / reference:** new package evidence only; previous20261019 outputs are historical
- **Waiver authority / reference (required if waived):** n/a

## Questions To Close

- [x] Architecture option C, explicit initial resolver and descriptor-to-context equality: selected by r1 and frozen in normative r1 contract; fresh critique still required.
- [x] MessageAcceptance transaction collaboration and CAS-before-own-mutation: fixed ordering and bounded whole-local-tx recovery defined in normative r1 contract.
- [x] Ordinary-versus-initial race: per-owner admissions with no uncertain time takeover; same lock admission, independent token release and explicit local risk acknowledgment, detailed below.
- [x] POSITIONAL consumption: initial renderer validates existing components without changing ST-05 flags/parser/projector.
- [x] Exact source admission: same acceptance owner explicitly included with supplemental pre-edit seal; other allowed paths remain in strict inventory.
- [ ] Future execution dependency only: actual own-account APPROVED asset and healthy disposable/runtime source binding; no current enum/runtime claim. Required proof cannot be waived by mocks or this planning approval.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Conversation unique BU/contact; list current order lastMessageAt and no manual-open BFF route | api-app/prisma/schema.prisma:389; api-app/src/domain/inbox/conversations.service.ts:61; api-app/src/surfaces/bff/conversations.controller.ts:20 | reconverge upsert/list and API before approval | High; source inspection only | Keep as Assumption |
| A-02 | Channel only text today; bound factories/current-context guard exist | api-app/src/domain/channels/transport/channel.ts:28; api-app/src/integrations/channels/meta-channel.ts:13; api-app/src/integrations/channels/evolution-channel.ts:13 | reconverge explicit supersede and dependency harness | High; source inspection only | Keep as Assumption |
| A-03 | Acceptance owns its own transaction; common sender finalization is separate | api-app/src/domain/inbox/message-acceptance.service.ts:82; api-app/src/domain/inbox/outbound.service.ts:83 | do not pretend tx collaboration exists; adapt same owner explicitly | High; source inspection only | Keep as Assumption |
| A-04 | Catalog and template provider owner already delivered; read-ID alone lacks fresh parent membership proof | api-app/src/domain/message-templates/template-observation.service.ts:115; api-app/src/integrations/meta/message-template.client.ts:118 | do not duplicate catalog or assume ID grants account scope | High; source inspection only | Keep as Assumption |
| A-05 | Window currently uses stored createdAt/latest any IN; signed Meta adapter discards provider timestamp | api-app/src/domain/inbox/outbound.service.ts:244; api-app/src/integrations/channels/prisma-channel-resolver.ts:68; api-app/src/surfaces/webhooks/meta.controller.ts:103 | reconverge all projections/consumers before approval | High; source inspection only | Keep as Assumption |
| A-06 | Template management depends on transport for its single credential resolver, so reverse import would cycle | api-app/src/integrations/message-templates/template-management.module.ts:1; api-app/src/integrations/channels/channel-transport.module.ts:1 | composition of initial flow imports both; no reverse dependency | High; source inspection only | Keep as Assumption |
| A-07 | Browser has context generations and shared catalog API wrapper | web-app/src/telas/Inbox.tsx:50; web-app/src/api.ts:352 | reuse actual guards and freeze new flow-specific freshness | High; source inspection only | Keep as Assumption |
| A-08 | Current canonical opaque management account reference uses a private hash helper | api-app/src/integrations/message-templates/template-management.resolver.ts:83 | extract exact byte-compatible integration helper; no protocol IDs in domain input | High; source inspection only | Keep as Assumption |

External facts and actual readiness are dependency records, not fictitious code-backed assumptions: official primary docs verified200 anonymously via Accept:text/markdown on2026-10-22; approved asset enum/current runtime not queried.

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

## Plan Review Gate

- **Complexity:** big
- **Checkpoint policy:** section-by-section architecture/contract, schema/concurrency, adapter/security, browser/performance and final adherence. Planning reviews precede APROVADO; delivery checkpoints require their own actual evidence.

- **Decision:** required, fresh after freeze
- **Status:** `running`
- **Baseline history:** initial freeze published; r1 material integration queued for refreshed freeze before critique
- **Review sections:** architecture, quality, tests, performance, security, elegance and structural design.

### Scoped Review Questions

| ID | Section | Finding / question to challenge | Options / tradeoff | Required disposition |
| --- | --- | --- | --- | --- |
| ARCH-01 | Architecture | Is one union send method plus supportedKinds a sound abstraction? | A second method expands the abstract contract; B parallel sender forks policy/acceptance; C one discriminated operation keeps one abstract method but widens payload and all adapter contracts | Compare substitution, consumers, dependencies/harness, blast and future extension; no future plugin framework |
| ARCH-02 | Architecture | Can initial coordinator reuse shared sender while durable acceptance spans external I/O, without a TemplateManagementModule ↔ ChannelTransportModule cycle? | composition imports ChannelTransportModule and TemplateManagementModule only at initial-flow boundary; pass provider-agnostic descriptor to sender. Common OutboundService does not inject management resolver. Reuse listTemplates/getTemplate; no send method on management port. | Preserve one MessageAcceptance owner and existing wrapper semantics; no HTTP in transaction |
| ARCH-03 | Architecture | How capture immutable selected channel/resource/credential context and enforce current version immediately before POST, after every remote preflight GET? | all bounded grant/phone/template GETs first, then abstract attempt fence/CAS immediately before POST, chained with current-context fence; test expired PREPARED zero POST | Selected same identity only; current-version/CAS checks; stale context fails closed |
| ARCH-04 | Architecture | Does one trusted timestamp policy cover sender and every availability projection? | nullable qualified Meta timestamp + bounded index vs old createdAt rule | no fallback/backfill; preserve timeline; prove all BFF/public/BOT consumers |
| ARCH-05 | Architecture | Does same-account list-by-trusted-name prove current exact remote asset with finite reads? | bounded two filtered pages + exact semantics vs ID-only GET | reject partial/exhaustion/ambiguous/status unknown; no browser cursor authority |
| QUALITY-01 | Quality | Are durable outcomes and acknowledgment truthful and monotonic after timeout, process death, late result and slot release? | single POST, AMBIGUOUS lock, explicit irreversible ack vs retry convenience | prove state transition table and no status/owner steal |
| QUALITY-02 | Quality | Are open/reuse and empty-conversation UI truthful with no implicit send/read/claim? | atomic idempotent create/reuse; explicit user confirmation | role/tenant, race and refresh UX |
| TEST-01 | Tests | Are tests proving absence of provider call, no duplicate POST, current-resource membership and no missing-ID Message? | real counters/barriers and typed fakes vs happy-path mocks | adversarial integration cases and substitutability harness |
| TEST-02 | Tests | Are existing BFF/public/BOT text paths and composer errors preserved? | focused regression matrix vs broad rewritten tests | exact mapping and endpoint response assertions |
| PERF-01 | Performance | Are read budgets, list/index query, lease and API limits mutually consistent under concurrency? | max6 GET/1POST, 10s each, 75s total, lease90s; bounded rate keys | measure counts/queries/latency; no network while locked |
| PERF-02 | Performance | Does trusted-window projection remain batched and index-backed at scale? | direction/resource-filtered indexed query vs per-row hydration | query count, examined rows and EXPLAIN under OUT-heavy/no-IN fixtures |
| SEC-01 | Security | Can actor, BU, contact, selected resource, remote asset, or attempt ID be confused across tenants/accounts? | scoped authorization and canonical account namespace | no foreign existence leaks; stale/foreign before effects; safe DTO only |
| SEC-02 | Security | Are preview/template params bounded and safe, and recovery authenticated/CSRF protected? | text-only grammar and explicit ack risk vs arbitrary provider payload | parser bounds, escaping, no secrets/provider body, replay ordering after grant |
| ELEGANCE-01 | Elegance | Does proposal use existing owners with minimal new concepts? | one coordinator + one common sender + one acceptance + shared catalog vs duplicates | explain each boundary; no parallel template authoring or platform abstraction |
| STRUCT-01 | Structural | Are modules and dependency direction coherent across inbox, channels, templates and BFF? | inbox orchestrates ports; adapters own provider protocol; catalog stays ST-05 | no domain Meta HTTP/provider branches; no new owner for Message/template observation |
| STRUCT-02 | Structural | Are schema, transaction and external side-effect boundaries explicit and recoverable? | durable states/slot/unique constraints/CAS vs locks or memory state | migration and crash matrix; no pretending at-most-once means exactly-once |

### Plan Review Issue Cards — full option comparison

The recommended options below include the r1 fixes. These are plan-review choices, not implemented evidence. Cost means relative implementation/test work for this bounded slice. All impacts are predicted; runtime performance is unmeasured. No material finding is hidden by a low-cost option.

| Issue ID / axis | Severity | Concrete evidence | Why now | Recommendation |
| --- | --- | --- | --- | --- |
| PR-ARCH / Architecture | high | api-app/src/domain/channels/transport/channel.ts:24; integrations/channel composition; ARCH-R1-03 | template outside window needs explicit scoped selection, one abstract method and no dependency cycle | C |
| PR-QUAL / Code Quality | high | api-app/src/domain/inbox/message-acceptance.service.ts:82,231; ARCH-R1-02 | self-mutated updatedAt and aborted transaction must not fake a current CAS | A |
| PR-TEST / Tests | high | api-app/src/domain/inbox/outbound.service.spec.ts:1; test/channel-transport.e2e-spec.ts; ARCH-R1-01 | mocks cannot prove exclusion or real commit/rollback ACK certainty | A |
| PR-PERF / Performance | medium | api-app/src/domain/inbox/outbound.service.ts:244; integrations/channels/prisma-channel-resolver.ts:68 | new window/account validation must be index-backed, batched and finitely bounded | A |
| PR-SEC / Security | high | api-app/src/surfaces/bff/conversations.controller.ts:20; integrations/message-templates/template-management.resolver.ts:83 | external first contact binds tenant/actor/context and exact current account/template | A |
| PR-ELEG / Elegance | medium | api-app/src/integrations/message-templates/template-management.module.ts:1; channel-transport.module.ts | avoid a second sender/projector or provider plugin platform | A |
| PR-STRUCT / Structural Soundness | high | api-app/src/domain/inbox/outbound.service.ts:37; ARCH-R1-01/02 | exclusive initial intent must coexist with ordinary callers without HTTP locks or unsafe lease takeover | A |

| Issue | Option / outcome | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-ARCH | A: second Channel.sendTemplate operation | medium | medium | cross-module | medium | neutral vs C | regresses: operation-specific expansion | mixed: ownership possible but broader contract |
| PR-ARCH | B: parallel concrete template sender | medium | high | cross-module | high | unknown, duplicate preflight likely | regresses | regresses: bypasses common scoped dispatch/acceptance |
| PR-ARCH | C recommended: discriminated same sendMessage + supportedKinds + explicit initial resolver/fence | high | medium | cross-module | medium | bounded extra validation; measured later | improves coherence | improves: one operation and owner graph |
| PR-QUAL | A recommended: same acceptance owner, pre-acceptance CAS, bounded whole-local-tx re-entry | medium | medium | module | low | extra short row lock; no network lock | improves | improves: truthful atomic local completion |
| PR-QUAL | B: duplicate Message/finalizer in initial service | medium | high | cross-module | high | unknown duplication | regresses | regresses: two mutation owners |
| PR-QUAL | C: do nothing; finalize after acceptance with stale updatedAt | low | high | module | high | fewer checks, invalid behavior | regresses | regresses: self-invalidating CAS |
| PR-TEST | A recommended: causal RED + real PG barriers/ACK faults + protocol recorder + real BFF browser | high | medium | cross-stack | medium | test time increases within owned runner | improves confidence without product workaround | improves |
| PR-TEST | B: happy-path mocks only | low | high | module | medium | faster tests, no concurrency proof | mixed | regresses: required failure states unproved |
| PR-TEST | C: weaken assertions to existing behavior | low | high | module | high | no valid improvement claim | regresses | regresses: test-only shortcut |
| PR-PERF | A recommended: filtered two-page account reads, shared request grant, bounded index/batched window | medium | medium | cross-module | medium | bounded extra latency/query work; measure | improves predictable limits | improves |
| PR-PERF | B: full account scan / per-row IN queries | medium | high | cross-module | high | regresses unbounded work/N+1 | regresses | regresses |
| PR-PERF | C: trust stale local catalog and createdAt window | low | high | cross-module | high | fewer reads with false authorization | regresses | regresses |
| PR-SEC | A recommended: current auth/CSRF, immutable full context, fresh exact account eligibility, local-only recovery | high | medium | cross-module | medium | bounded extra checks | improves explicit authority | improves |
| PR-SEC | B: accept arbitrary browser Graph payload/account/URL | low | high | cross-stack | high | unknown/unbounded | regresses | regresses: crosses credential/tenant boundary |
| PR-SEC | C: do nothing; no manual first contact capability | low | low | local | low | neutral | neutral | preserves baseline but does not deliver agreed story |
| PR-ELEG | A recommended: inbox coordinator composes delivered transport and management; one acceptance/projector | medium | medium | cross-module | low | avoids duplicated HTTP/cache | improves | improves |
| PR-ELEG | B: new generic provider/plugin/workflow platform | high | high | cross-stack | high | unknown overhead | regresses incidental complexity | mixed, unauthorized future platform |
| PR-ELEG | C: scattered provider branches in Inbox/domain | low | high | cross-stack | high | unknown drift | regresses | regresses DIP |
| PR-STRUCT | A recommended: per-owner ordinary tokens coexist, exclude initial slot; uncertain dispatch never expires into takeover | high | medium | cross-module | medium | short admission writes, ordinary concurrency preserved | acceptable bounded safety state | improves truthful exclusion |
| PR-STRUCT | B: one exclusive send lease for every caller | high | high | cross-module | high | regresses ordinary concurrency; unsafe expiry unless expanded recovery | regresses unnecessary platform | mixed, changes ordinary compatibility |
| PR-STRUCT | C: early SELECT or auto-expire SENDING | low | high | cross-module | high | superficially cheap but permits concurrent dispatch | regresses | regresses external-effect safety |

## Failure Modes & Edge Cases

- actor loses grant after creating PREPARED; replay must verify grant before exposing or dispatching but must not reread provider before canonical replay resolution.
- lease expires while remote validation is slow; claim CAS prevents any later dispatch.
- provider accepts but response is lost or ID malformed; AMBIGUOUS remains locked and never retries.
- known ID cannot be locally accepted due changed resource/generation; preserve ID as `EXTERNAL_ACCEPTED_LOCAL_BLOCKED`; quarantine/no Message without ID.
- operator acknowledges uncertainty, starts successor, then old ID arrives; old intent may improve its own local record only if still eligible but cannot take slot or change successor status/owner.
- simultaneous human claim/close while HTTP is in flight; final CAS respects the current owner/state.
- selected template changes status or semantic definition after catalog observation; fresh same-account check rejects before POST.
- selected phone shares a Messaging account; send must pin the captured account and correctly format full international recipient.
- signature invalid, timestamp missing/zero/fractional/future, imported or nonofficial IN; never open window from those records.
- official selected identity changes during send; no substitution/fallback to a newer connected channel.
- public/BOT/outbound composer races the active slot; all dispatch boundaries enforce slot policy with their existing response mapping.
- same phone contact with optional DDI input normalizes consistently without guessing country; validation and unique index handle concurrent creation.
- no eligible approved asset/account is available; honest blocker, never fixture-based completion.

## Residual Unknowns / Risks

- The current official own account and eligible APPROVED asset are not verified; documentation evidence does not establish account readiness.
- No current own-account APPROVED template availability is asserted.
- Runtime state/current validation owner is intentionally not reprobed during this planning-only slice.
- Exact current source anchors and consumer matrix are attached; final implementations must still prove inherited public/BOT mappings and ordinary concurrency.
- This contract proposes a material Channel supersede; architecture reviewer can reject C and require a revised draft/reapproval.

## Additional Architectural Opinions

Fresh internal no-context r1 completed: option C recommended, four material findings integrated as normative contract below. Raw/strict merge and resolution in current review package. Performance mixed/unmeasured; elegance acceptable; structural and operational fit mixed until r1 fixes are validated. Fresh critique must assess those fixes, not reuse old19/20 opinions. Root owns serialized documentation orchestration.

## Planning Finding Resolution Ledger

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-R1-01 / F-E3C20901 | Integrated | useful | partial | project | n/a | Normative r1 owner-token interlock, explicit ordinary compatibility, no uncertain expiry takeover, local-only risk recovery and complete barriers; Scope09/DoD08/Val02 updated. |
| ARCH-R1-02 / F-2D3CB947 | Integrated | useful | yes | project | n/a | Same acceptance owner explicitly admitted/sealed; original CAS before self-mutation; identity/conversation lock order; whole-local-tx rollback/readback/one re-entry; Scope07/DoD06/Val02. |
| ARCH-R1-03 / F-0715A55A | Integrated | useful | yes | project | n/a | Explicit initial resolver, exact management/transport full context equality, parameter/semantic descriptor, applicable text-window check at final fence; DoD09/Val03. |
| ARCH-R1-04 / F-E2F76277 | Integrated | useful | yes | project | n/a | Initial renderer over unchanged existing catalog components; separate initial semantic fingerprint and POSITIONAL ordering; no authoring/parser/projector flag change; DoD09/Val03. |

These dispositions amend proposed contract only. Fresh no-context critique must assess them after refreshed freeze. They do not assert production fixes or grant execution authority.

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

## Independent No-Context Critique Gate

- **Critique decision:** required
- **Why this decision:** big/cross-stack/escrita externa scoped.
- **Impact signals in scope:** public contract/schema/api; auth; realtime; intentional module supersede
- **Package mode:** bounded-file-set
- **Package minimum contents:** TODO congelado, fontes públicas limitadas, decisões/matriz/issue cards/riscos, parecer arquitetural e resolução.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; novo agente, não executor, aguardar terminal sem prazo artificial
- **Critique lenses:** correctness,performance,elegance,structural-soundness,risk
- **Critique status:** findings_integrated
- **Findings summary:** fresh critique r1 confirms four architecture findings integrated; its medium initial-deadline clarification and low automation compatibility case integrated; fresh focused critique r2 required before APROVADO
- **Resolution ledger:** machine-checkable critique dispositions below; architecture ledger retained separately
- **Evidence / reference:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/critique-r1.merge.json + critique-r1-resolution.md; raw and strict merge immutable; old reviews historical
- **Waiver authority / reference (required if waived):** n/a

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CR-R1-01 | Integrated | useful | yes | project | n/a | Uniform immutable90s dispatchDeadlineAt predicate for AMBIGUOUS and EXTERNAL_ACCEPTED_LOCAL_BLOCKED; endpoint, Scope08/DoD06/Val02 and normative r2 appendix aligned; merged F-49CD0618. |
| CR-R1-02 | Integrated | useful | partial | project | n/a | Preserve actual NOVA_CONVERSA row-creation predicate and keyword behavior; no automation on manual open; Scope01/DoD01/Val01, consumer/flow and existing admitted Typebot test scope aligned; merged F-4ACC72C3. |

## Rules Acknowledgement / Ingestion

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

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Routing evidence:** artifacts/reviews/leadshug-start-conversation-20261022/evidence/routing-planning-writer-v1.1.json; proposed product executor same tuple, new GO required after APROVADO
- **Execution topology:** primary-checkout-single-writer
- **Subagent / delegation authorization:** repository workflow authorizes executors/reviewers; no product execution yet
- **Git isolation authorization:** not-authorized
- **Worktree authorization:** not-authorized
- **Worktree authorization reference:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

## Decision Adherence Validation

Pending implementation; not run.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

Pending implementation; not run. Every frozen decision must map one-to-one to module decision handling before delivery.

## Pipeline/Copilot P1/P2 Preflight

Pending required delivery stage; not run for planning.

## Rule-Spirit Anti-Pattern Hunt

Pending required delivery stage; not run for planning.

## Promotion Finding Routing Ledger

No promotion review exists for v1.1. Root-owned review artifacts are authoritative after freeze.

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** current v1.1 contract awaits fresh published review convergence and explicit APROVADO.
- **Post-commit/push status:** pending
- **Next path/status action:** remain active/NotStarted/review; no implementation until authorized.

## Security Risk Assessment

- **Risk level:** high
- **Why this risk level:** cross-tenant first-contact external side effect, account selection, credentials and irreversible ambiguity.
- **Attack surface in scope:** session/CSRF, BU/contact/channel/template/account/attempt IDs, parameter renderer, stale contexts, payload/key/rate limits, sender-slot races.
- **Attack simulation decision:** required
- **Review evidence:** planned after implementation; no live provider/runtime query performed.
- **Residual security risk:** private existing local cohort only. Delivered SEC-R6-04 recovery-budget debt remains outside04;04 recovery does no external reads. OPS-R4-01 and TQA-ST05-03 retain their dispositions. A fresh current approved template is not presumed.

## Performance & Concurrency Risk Assessment

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
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256 antes da entrega, não existe execução ainda.
#### FRC
- **Trigger rationale:** duas submissões e atraso em troca BU/canal/draft; Playwright real, rastrear requests e estado no backend.
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### BCI
- **Trigger rationale:** barreiras PG e contador HTTP externo, crash antes/depois POST, replay e echo; provar invariantes D-06/07.
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### RLS
- **Trigger rationale:** pequeno ensaio de concorrência/load bounded do novo fluxo/listagem no PG descartável; não claim SLO ou produção.
- **Recorded at (UTC):** 2026-10-22T00:00:00Z (planning date marker, not execution time)
- **Executor ID:** planned-executor-st-con-04
- **Evidence object:** pending; resolver recomendação com evidência ou waiver válido até o deadline, sem deixar pendente na entrega.

## Verification Debt Assessment

Required at closeout. Explicitly carry ST-05 `SEC-R6-04`, `OPS-R4-01`, and `TQA-ST05-03` as accepted delivered limitations unless the owning TODO changes them. No backlog fix is admitted here. Record newly found debt and owner before Completed; no claim that it was cleared by this plan.

## Independent Test Quality Audit Gate

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
- **Findings summary:** no current delivery review performed
- **Evidence / reference:** planned current implementation evidence only; prior planning artifacts historical
- **Waiver authority / reference (required if waived):** n/a

## Independent No-Context Final Review Gate

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
- **Findings summary:** no current delivery review performed
- **Evidence / reference:** planned current implementation evidence only; prior planning artifacts historical
- **Waiver authority / reference (required if waived):** n/a

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** required
- **Why this decision:** intentionally replace the Channel text-only payload restriction and stored-createdAt window rule without duplicate dispatch/catalog/Message owners.
- **Cutover signals in scope:** canonical cutover; legacy-path retirement
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** planned after implementation; no current delivery review
- **Audit focus:** one abstract send operation, qualified window in every caller/projection, sole acceptance owner, zero hidden fallback
- **Cutover audit status:** not_run
- **Findings summary:** implementation has not begun
- **Resolution ledger:** delivery-stage findings will be recorded with disposition and evidence
- **Evidence / reference:** current delivered source and future implemented diff; no cutover evidence yet
- **Waiver authority / reference (required if waived):** n/a

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Not applicable to planning; future production confidence is outside current authorized scope.

## Module Consolidation Gate (Required Before `Completed`)

Pending after delivery evidence. Update inbox/channels module docs only after accepted reviews and implementation truth; no module mutation in this task.

## Commands (Run Locally)

Planning-only review/guard and Foundation main publication commands are recorded in current evidence. No product/test/runtime command was run or authorized by this planning slice. Future product commands use the declared canonical suite and approved disposable/local topology after APROVADO.

## Files Expected (Compatibility Note)

Root owns this active TODO, archive and review/evidence artifacts; the terminal draft author previously owned only the TODO. The 68-file source seal is planning evidence; no source edits are made now.

## COMENTÁRIO

Planning draft only. Human decision requested only after root has frozen it and completed fresh review/guard work; this text itself does not ask for approval.

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** premissas de implementação dependem de fontes atuais.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01..08
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md
- **Gate status:** not_run
- **Findings summary:** fresh source-backed assumptions await current reviews and guard
- **Evidence / reference:** new current package, after review convergence
- **Waiver authority / reference (required if waived):** n/a

## Approval

- **Approval status:** not-approved
- **Approver:** human task authority
- **Approval reference:** none for current v1.1; user authorized advance planning, not implementation
- **Approved scope:** none until explicit APROVADO of current reviewed04
- **Exclusions:** product source/tests/runtime/Meta actions remain untouched during planning
- **Renewed-approval trigger:** material scope/decision/API/schema/validation change or new private/public exposure.

## Prior-cycle provenance and sequencing handoffs

- The original 2026-10-19 planning/review record is archived by root at `foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/historical-planning-20261019-20261020.md`; retain its content unmodified.
- ST-CON-06 v1.3 and ST-CON-05 v1.1 are completed locally with their own evidence and limits. Their reviews do not transfer approval to ST-CON-04.
- The old separate `GET /conversations/:id/channels/:channelId/templates` is superseded in this proposal by the one ST-05 catalog route/projector.
- The 2026-10-19 assumption-code, review, critique, and preflight outcomes remain historical only. Current v1.1 evidence is recorded gate by gate; original pending-freeze statements are authoring history, not current success evidence.

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

## Planned operational admission and proof

After explicit APROVADO and current authority GO: test-first admitted public paths only; full canonical all suite; current security/PCV/TQA/adherence assurance; disposable migration deploy/status, then one bounded local preserved TEST preflight/apply with5s lock/60s command limits, no reset/drop/resolve retry; source-bound API/Web images/runtime/static proof, preserve peers/volumes. Temporary owned HTTPS only after those gates; never adopt/kill unknown processes or require raw env/log reads. Assisted operator tests use only already designated private test channels/contacts; no automatic real send. Both unofficial first text+reply and official genuinely APPROVED template+reply are completion requirements; operator authorizes actual recipient tests at that stage. Publication/promotion of product/Railway remains excluded. Actual approval enum is currently unknown, and current runtime health has not been reprobed. Existing SEC-R6-04/OPS-R4-01/TQA-ST05-03 remain bounded, not fixed or generalized here.

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

```


---
## foundation_documentation/project_constitution.md
SHA256 abfafa5576d051da58583e2be57499320c8ad155c4ae741f259c730bcca98390

```
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
- Documentos institucionais estáticos explicitamente autorizados, como /privacidade.html, são públicos e não resolvem tenant/BU nem consultam dados de negócio. Não alteram a autenticação das superfícies acima. Sua publicação local não autoriza publicação do app Meta ou produção.
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


---
## foundation_documentation/policies/scope_subscope_governance.md
SHA256 aa18357e37417617b63ec5e58aba87c0f8c1e7518d6834d5cadfeda0a561dd84

```
# LeadsHug Scope Governance
**Version:** 1.0

## Canonical hierarchy

`Mantenedora -> Setor -> Business Unit (número) -> Conversa/Contato`.

The Business Unit is the minimum authorization and data-isolation boundary. A user may hold grants for one or
more BUs; no controller, service, repository or frontend adapter may infer access from UI state alone.

## Runtime surfaces

| Surface | Authentication | Responsibility |
| --- | --- | --- |
| `/api/bff` | session | authenticated web application |
| `/api/v1` | partner API key | public integrations |
| `/api/internal` | service credential | trusted internal calls |
| `/webhooks` | provider verification | inbound channel events |
| /privacidade.html | public static document | Institutional privacy information only; no tenant/account/BU resolution, forms, SDK or business-data access. |

Outbound provider adapters are integration boundaries, not public runtime surfaces.

## Rules

- New scope or surface requires a TODO and constitution update.
- Every route documents tenant, account and BU resolution.
- Cross-BU reads fail closed and are covered by tests.
- Frontend routes do not define authorization; backend guards do.

```


---
## foundation_documentation/modules/inbox-and-conversations.md
SHA256 24b3f1edd8f10bf991d61135be2364b49679c43e5894ce024c2d5169921756a2

```
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

APROVADO em2026-10-15; implementação exercitada localmente em2026-10-16 ([all499/22migrações e fonte/freshness](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp27-receipt.json)); architecture/security, Performance/cutover e TQA independentes aceitos no escopo local. Final review local aceito; source commits/bridge byteexact registrados, prova externa local dos dois canais concluída CP106-108; encerramento local concluído CP108 no TODO, sem alterar o contrato de timeline verificado acima. Owner inbox-and-conversations; identidade externa e pareamento pertencem a [canais](integrations-and-channels.md#cadastro-de-números-st-con-01). Execução no [TODO](../todos/completed/features/TODO-leadshug-channel-connection-readiness.md).

Entrada aceita exige externalMessageId não vazio e chave única PostgreSQL (providerResourceIdentityId,externalMessageId); identidade já incorpora provider. Mesmo ID em recursos diferentes não colide. `Message` legado pode manter FK/chave nulas; não inventar IDs nem apagar duplicatas históricas. Só backfill inequivocamente comprovado é admitido. Novas entradas sem ID ficam rejeitadas com erro seguro antes de efeito de domínio. Após identidade validada, transação curta aceita Message e cria/reusa conversa BU/contato com incremento unread; conflito de unique desfaz os efeitos daquela tentativa. Somente a transação vencedora publica realtime e aciona automação. Echo OUT e resultado do sender compartilham a mesma aceitação transacional por identidade/ID, inclusive quando o echo chega primeiro; não criam outra Message, IN ou unread. Contrato detalhado abaixo. Replay sequencial/concorrente retorna sucesso idempotente para evento já aceito. Não se promete exactly-once externo: crash depois do commit pode deixar publicação/automação ausente; não repetir bot automaticamente nem introduzir plataforma de jobs/outbox neste recorte. Essa limitação precisa constar do runbook.

IncomingService deriva Mantenedora da BU verificada. Busca de trigger exige bot.mantenedoraId desse tenant e buId exata OU trigger global dentro do MESMO tenant. Sessão retomada deve pertencer à mesma Mantenedora/BU/contato; sessão estrangeira falha fechado antes de texto externo. Criação deriva owner do contexto verificado, não de um bot arbitrário. Dois tenants com triggers globais concorrentes não compartilham bot, texto, sessão, saída ou credencial. São defeitos preexistentes na superfície tocada, cuja correção fica expressamente incluída para sustentar o recebimento deste cadastro.

Um serviço de aceitação de mensagem no domínio inbox é o owner da chave (providerResourceIdentityId,externalMessageId) para TODAS as novas gravações com ID: entrada, eco OUT, resultado de envio BFF/público e Typebot. Sender captura a identidade do canal autenticado, faz HTTP fora de transação e depois cria-ou-reconcilia pelo mesmo índice PostgreSQL. Sender-first, echo-first e ecos concorrentes devolvem o MESMO Message.id; conflito de unique não pode virar segundo registro nulo nem erro de inserção depois do envio bem sucedido. Validar owner BU/conversa/contato/direção na reconciliação; incompatibilidade é erro/quarentena de identidade, sem sobrescrever outro recurso. Registro local sem externalId confirmado conserva pendência/erro explícitos, sem inventar ID, retry externo ou garantia de deduplicação por ID inexistente.

Eco primeiro cria OUT sem autoria humana inventada; resultado interno enriquece o mesmo registro com conteúdo/autoria humana ou Typebot comprovados pelo caller. Eco posterior não apaga/substitui essa autoria e não muda createdAt/ID. Só criação vencedora emite evento de nova mensagem; enriquecimento preserva a identidade e usa refresh/projeção existente, sem novo IN, unread ou bot. Retorno BFF/público mantém seus contratos e contém o registro reconciliado. Invariantes de janela, permissão, conversa BU/contato, ordenação e timeline permanecem. Nenhum cache de ecos em memória ou lookup-antes-insert substitui o índice/transação. Continua explícito o limite de crash depois do commit e antes da publicação; não há claim exactly-once externo.

A verificação final de mapping/epoch deve ser sincronizada à gravação de conteúdo, incluindo webhook em voo atravessando RENEW/remove-recreate. A projeção existente após refresh mostra o mesmo ID enriquecido; se exigir diff hoje excluído, registrar a falha antes de admitir mudança de escopo. Não há autorização para Nova conversa manual, importação, sequenciamento de bot para mensagens distintas, worker ou outbox.


## Channel abstrato e envio comum — ST-CON-06

Contrato v1.3 aprovado e exercitado localmente: all93791 passou613testes, revisões independentes de aderência/segurança/cutover/TQA e Performance convergiram, com uma dívida baixa explícita de precisão de métrica de teste. O operador confirmou nova IN e resposta OUT nos vínculos oficial e não oficial após ativação das imagens atuais; a proveniência fonte→imagem→container→HTTP foi conferida antes e depois. A revisão final e os guards de closeout são registrados no [TODO governante](../todos/completed/features/TODO-leadshug-channel-abstraction.md). Evidências: [validação automatizada](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/v13r4-final-validation.json), [ativação](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-activation-provenance-v13r4-final.json), [prova assistida](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-operator-proof-v13r4.json) e [proveniência posterior](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/post-operator-readback-v13r4.json). Não é prova de produção, disponibilidade contínua ou redes futuras.

BFF, partner public API and Typebot consume one OutboundService. Trusted BFF human/public EXTERNO/bot source intent is established before dispatch. MessageAcceptanceService remains the sole keyed writer for provider-ID Messages and sender/echo convergence. Human/public completion conditionally updates the current owner, preserves a newer concurrent claim and sets IN_SERVICE except existing group behavior. Bot retains queue/status/human owner/unread semantics and stops without replay after uncertain or blocked output.

Human/public responses use the deterministic latest message origin ordered by createdAt DESC,id DESC. An unavailable selected origin is not replaced by another connected channel. Without history, only a sole binding can be selected; zero and multiple bindings have explicit absent/ambiguous errors. Bot responses remain pinned to their accepted verified ingress even if another channel becomes the latest origin. The selected binding's free-text-window requirement applies to all senders before every text. Existing latest-IN stored timestamp without transport filtering is preserved and must be revisited in ST-CON-04.

ST-CON-04 first-send, if separately approved, consumes the shared template catalogue owned by [Integrations and Channels — ST-CON-05](integrations-and-channels.md). Before every first-send it independently revalidates that the selected template is currently eligible (`APPROVED`, observation at most 300 seconds old) for the current selected account/channel context and rechecks the existing send policy. It adds no template authoring/catalogue, sender, or route here. ST-CON-04 remains unimplemented and requires its own TODO and approval.

Availability is safe local metadata, separate from authorization and dispatch revalidation. BFF thread adds disponivel/motivo; public list/thread adds envio_disponivel/motivo_indisponibilidade. Batched public availability reads BU bindings/credential metadata at most once per page and latest-IN only for references whose actually selected binding requires a window, without decrypting secrets or calling providers. The managed Message index `(conversation_id,direction,created_at,id)` supports direction-constrained latest-IN lookup, including OUT-heavy/no-IN histories and equal-time ID ordering; it does not change the historical timestamp rule or imply a production capacity/SLO. The public list loads parent metadata with one-row lookahead, slices the returned page, then reads latest-any-message metadata in one parameterized batch restricted to those returned IDs. Direction-constrained top-one IN/OUT probes use the approved index and choose the larger createdAt/id tuple from at most2candidates per parent, preserving null message/direction for an empty history. This is separate from the selected-window latest-IN projection and never hydrates full histories. Public list and message-thread pagination normalize the optional limit before Prisma: maximum500, defaults200/list and100/thread for absent, blank, non-string/repeated, nonfinite, nonpositive or sub-one-after-floor values; finite positive fractions are floored. The list may fetch one additional row solely to report truncado, then projects availability for at most500 returned conversations. These bounds were exercised by request-level PostgreSQL regression cases and all93791; measured emitted rows must remain distinct from general scan/filter/recheck work (PERF-R4-01). Existing thread read-marker behavior is retained; only the availability projection is observational. No new route, user-supplied provider selection or Message DTO status field is introduced.

Inbox shows fixed truthful explanations, disables unavailable sends, retains draft on uncertainty/local incomplete/error, and never automatically resends. Monotonic BU/conversation generations fence late completions, including A→B→A with a newly edited identical draft. Composer duplicate triggers are dropped while a send is in flight.

Contrato de campos e erros: [canais e envio comum](integrations-and-channels.md#channel-abstrato-e-envio-comum--st-con-06).

```


---
## foundation_documentation/modules/integrations-and-channels.md
SHA256 6b1865ab4f27458e1e1e225535e2f4a713e987e18344ca86d3f9411fa6c6f168

```
# Module: Integrations and Channels
**Version:** 1.0

Owns Meta Cloud API, Evolution/Baileys, outbound webhooks, API keys and transport adapters.

## Invariants

- Providers are adapters; business workflows do not depend on provider payload shape.
- Secrets never enter logs, docs, fixtures or client bundles.
- Provider failures become deterministic application errors.


## Cadastro de números ST-CON-01

Contrato aprovado pelo usuário em2026-10-15 no [TODO governante](../todos/completed/features/TODO-leadshug-channel-connection-readiness.md), documentação publicada3302964c. Estado: **Approved; implementação exercitada localmente em2026-10-16 ([all499/22migrações e fonte/freshness](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp27-receipt.json)); architecture/security, Performance/cutover e TQA independentes aceitos no escopo local. Final review local aceito; source commits/bridge byteexact registrados, prova externa dos dois canais concluída CP106-108; encerramento local concluído CP108 no TODO**. Owner: integrations-and-channels, escopo Mantenedora/BU; mantém constituição e políticas de isolamento. O módulo é autoridade do contrato; o TODO registra execução/evidência. Fonte API em api-app; Web em web-app.

### Disposição do complemento técnico de teste (CP84)

O [complemento ST-CON-01-TESTAUTH](../todos/active/features/TODO-leadshug-meta-api-test-number-binding.md) foi **Cancelled por decisão humana em 2026-10-18**, antes de qualquer implementação de produto. A entrada técnica por token privado do Test Number não integra o contrato entregue deste módulo. Seu planejamento/diagnósticos permanecem históricos; retoma-se ST-CON-01 por Embedded Signup; primeira prova oficial de recebimento passou em cp106 e recuperação com nova troca física passou em cp107-108. Inscrição ausente foi descoberta relatada pelo operador e corrige a premissa anterior; acesso/elegibilidade, callback e roteamento devem ser conferidos no contexto atual. Nenhum suporte de standby/handover é declarado ou implementado por esta disposição.

### BFF e autorização

Contexto do provedor conferido em2026-10-19: no [modelo atual da Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/), WhatsApp account (WAAC) representa o telefone; Messaging account contém templates, billing e inscrições de webhook. Na fase atual, o WABA ID existente identifica a Messaging account e os phoneNumberIds/APIs continuam compatíveis. O [onboarding padrão](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/onboarding/) cria uma Messaging account por parceiro e permite compartilhar um telefone já registrado com outro parceiro. Duas Messaging accounts no mesmo telefone ou ausência de templates de outro parceiro não comprovam erro do vínculo. Conferir autorização, associação do recurso e inscrição efetivas, além do roteamento no contexto atual. Registro do mesmo telefone e seleção da conta antiga são operações distintas; elegibilidade precisa ser observada na resposta real da Meta.

IDs/endpoints próprios de WAAC e transições obrigatórias futuras não são tratados como APIs disponíveis nesta entrega. O [parâmetro messaging_account_id](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/messaging/) deve ser avaliado quando a credencial tem acesso de envio a mais de uma Messaging account no mesmo telefone; não é causa presumida de falta de entrada nem autorização para mudança antecipada de schema/consumer. Cadastro, primeira troca oficial e retomada local passaram cp106-108; encerramento local está registrado no TODO ST-CON-01 concluído.

- `GET /api/bff/number-registrations/capabilities`: sessão válida; expõe apenas appId/configId/Graph version e disponibilidade/explicação por modalidade, nunca app secret/token/chave. Não chama provider. A modalidade oficial depende de versão Graph explícita no formato `vXX.0` e do conjunto Meta completo da instalação; valores ausentes, vazios ou malformados não anunciam disponibilidade, sem fallback de versão presumida. A configuração Meta inteira ausente mantém a administração disponível; configuração parcial é erro de implantação.
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

A verificação administrativa de um número oficial já vinculado revalida app, escopos e WABA da credencial ativa uma vez; procura o ID exato em no máximo duas páginas de números, sem seguir URLs de continuação. O limite total é uma consulta de grant e duas páginas, cada request com timeout10s sob lease45s. O confirm do cadastro continua relendo somente a página escolhida pelo operador. Ausência só é conclusiva quando uma lista estruturalmente válida se esgota; JSON inválido, data ausente/não-array, linha inválida, paginação inconsistente, continuação além do limite, ciclo ou cursor inválido mantêm a observação anterior e devolve503/codeMETA_INDISPONIVEL com mensagem fixa segura. O serviço traduz apenas a falha Meta reconhecida, preserva erros de autorização/concorrência e libera o próprio lease; não expõe erro bruto nem promove status por consulta inconclusiva. O reparo cp36g valida também a estrutura do grant antes de iterar os escopos/alvos e usa a interseção completa de autorização para verificar o número persistido; o limite100 permanece na apresentação de opções. A validação corrente cp36j passou 174 testes unitários e 288 E2E PostgreSQL pelo runner canônico. Web28/browser47 são evidências cp36h reaproveitadas por fontes consumidoras idênticas, sem alegar novo browser ou all537. Os testes diretos de grant revogado e app_id estrangeiro, com os demais campos válidos, foram aceitos no TQA completo e na revisão final independente j. A imagem servida continua i: somente o teste excluído do build mudou, com ponte explícita de bytes/compilados, sem novo build ou rótulo j. A retomada automática não oficial e a troca posterior real estão comprovadas cp49/cp52; a nova conversa foi de outro contato e o histórico anterior foi preservado. A primeira troca oficial IN/OUT e o recebimento foram comprovados em cp106, com readback canônico CONECTADO/identidade verificada/SUBSCRIBED/receipt confirmado; recuperação oficial foi comprovada por restart permitido da API e nova IN/OUT cp107-108. O baseline histórico cp60 ainda não tinha receipt; cp106 o confirmou na BU Local Test Ofc. CP107 retomou a API e preservou os estados; CP108 confirmou nova troca física após interrupção. Entrega geral Pending e restrição privada de dependências preservadas.

### Persistência e recuperação

`ChannelRegistrationAttempt` guarda id, Mantenedora/BU/canal, tipo, userId, hash de sessão, nonce hash, idempotencyKey+requestHash, estado, versão, leaseUntil, expiresAt, stage e erro safe. Unique Mantenedora/idempotencyKey e slot BuChannel(buId,type) já existente. IDs externos únicos por tipo; migrations detectam conflito preexistente antes de impor constraint. IDs internos podem ser prealocados sem compromisso de provider.

`ChannelCredential` mantém token/PIN em envelope com keyId/version/nonce/ciphertext/tag, ligado ao canal da BU e geração; não inventar vault genérico nem refletir o envelope no model público. AAD inclui provider/BU/channelID/generation. Tamper/decrypt/key ausente falha fechado, nunca fallback global. Passar credencial por interface de adapter, sem vazá-la a audit ou payload de domínio. Não copiar secrets do ambiente legado.

Cadastro pode ficar `PENDING_AUTH`, `PENDING_NUMBER`, `REGISTERING`, `PENDING_RECEIPT`, `CONNECTED`, `ERROR`, `CANCELLED`, com dimensão de providerConnection/receipt/credential e timestamps. O enum físico e mapeamento para status atual devem ser explícitos na migração; nenhum label mágico na UI. `CONNECTED` exige etapas aplicáveis concluídas, identidade correta e conexão confirmada; oficial já registrado sem endpoint conclusivo não recebe falso CONNECTED só pela lista de números. Primeira IN autenticada pode comprovar recebimento, não validade permanente do token de saída. Teste IN/OUT externo certifica somente a execução observada, não saúde contínua.

Reconexão e verificação administrativa repetida devem convergir de forma idempotente quando a tentativa corrente da mesma geração e do marcador de pareamento aplicável já está `CONNECTED`/`RECEIPT_VERIFIED`. No canal oficial, a tentativa conserva `pairingEpoch=null`, pois não há pareamento QR; no não oficial, exige o epoch numérico exato da rodada corrente. Essa aplicabilidade vem da modalidade confiável do canal, sem aceitar null como alternativa genérica para Evolution. Repetir essa observação não promove novamente nem incrementa a versão da tentativa; receipt e identidade existentes permanecem. Tentativa cancelada, etapa incompatível ou geração/epoch divergente falha fechada e não restaura estado do canal. A aceitação continua condicionada aos locks, owner, vínculo corrente e receipt; estado persistido durante indisponibilidade é a última observação, não garantia de saúde contínua.

Reserva idempotente da instância Evolution usa nome derivado de channelId+pairingEpoch persistida, estável durante retries desse epoch; nunca nome do operador+timestamp. Nova rodada de pareamento usa identidade externa distinta, conforme contrato de confiança abaixo. Se create retorna timeout, consultar a mesma identidade antes de retry; nenhuma segunda instância. Webhook deve ser configurado e verificado antes de concluir. Leitura de estado e evento usam geração e versionamento; retry de geração anterior não escreve após remove/recreate. Desconectar não apaga histórico. Callback tardio de instância sem vínculo não cria BU/tenant.

A tentativa expira em10min enquanto espera autorização. Após credencial ativa promovida, operações de recuperação do canal são administrativas e reautorizam grant/sessão corrente; não reaproveitam code/nonce antigos. Lease expirado não é sucesso e requer reconciliação; nenhuma transação DB é mantida durante rede. Não criar worker global ou sistema genérico de jobs neste slice.

### UI e integrações

Wizard: nome/BU → modalidade → janela Meta ou QR → confirmar número → mostrar cadastro/recebimento e ação de retry quando parcial. Cancelar popup, trocar BU, desmontar tela ou nova tentativa invalida callbacks/efeitos antigos no cliente; backend ainda revalida scope. A UI não consome mensagens postMessage para autorização ou seleção; somente o callback do SDK correlacionado à operação atual inicia a troca do code. IDs externos são obtidos e confirmados pelas leituras autorizadas no backend. Callback de login fica preso à geração/attempt/nonce corrente; prova server-side da credencial/ID é obrigatória.

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

A regra de não adotar instâncias Evolution não gerenciadas não impede a reautorização oficial já contratada no slot migrado. Mapping OFICIAL backfilled conserva somente ownership local, sem credencial nem confiança. Uma nova REAUTORIZAR explícita por ADMIN, no mesmo slot/BU/telefone e com recurso e credencial novamente comprovados na Meta, pode estabelecer o vínculo pelo fluxo canônico atual e suas condições de promoção. Backfill isolado, recurso de outra BU/slot e instância Evolution legada continuam recusados; não há adoção ou cleanup externo por inferência de nome/mapping.

### Segredos transitórios e webhook raw

Code SDK e PIN podem existir transitoriamente no formulário/memória do browser e seguir via BFF HTTPS; nunca em URL, storage, trace, screenshot, log ou DTO de retorno. Token, chave e envelope ficam somente no backend. Antes de persistir evento raw de provider autenticado, redigir recursivamente apikey, token, authorization, code, PIN, QR e componentes secretos de URLs; erros/audit usam catálogo e metadados allowlisted. Evento sem identidade verificada não persiste conteúdo. Harness envia envelope Evolution com apikey fictícia e comprova sua ausência em raw/audit/DTO/erro. QR só é devolvido efemeramente ao administrador no POST autorizado. Gateway Nginx, proxy e logs de aplicação não registram URI/token do callback Evolution: política explícita remove caminho secreto e query de access/error logs, inclusive erros; harness passa segredo fictício pelo gateway real e inspeciona logs/artefatos. Callback por header só se suportado e comprovado no provider fixado, sem presumir capacidade.

Meta raw é particionado por recurso verificado/BU, não por corpo de request inteiro. Batch assinado com entry/change/value de BUs diferentes produz registros scoped separados; fragmento desconhecido/retirado/sem identidade contribui apenas metadados allowlisted, sem conteúdo. Assinatura é verificada sobre o corpo original antes de parse/partição. REG-SEC-12/13 concretizam requisitos já existentes de segredo/owner, sem novo armazenamento genérico.

O suporte condicional de header foi confirmado no source fixado Evolution2.3.7 (`webhook.controller.ts` do commit cd800f2976e1e5b682fbf86a01ee4d85ae61f370): o provider aplica webhook.headers ao callback, mas registra URL em erros. Para cumprir a regra secret-free, o callback desta instalação usa URL sem segredo `POST /webhooks/evolution` e header privado `x-leadshug-webhook-secret`, comparado de modo timing-safe com EVOLUTION_WEBHOOK_SECRET. Não manter autenticação alternativa por path. Essa concretização exige teste real de callback/logs no runtime fixado antes da prova de aparelho; confirmação apenas de source não certifica execução. O segredo continua privado no adapter/backend, sem DTO/audit/raw/config.js.

Na prova privada cp49 de2026-10-17, a imagem API com a convergência corrigida recebeu o retorno automático da mesma Evolution após stop/start: connectedAt novo posterior ao start, identidade/geração/epoch/receipt atuais e tentativa já concluída v2 preservados, sem verificação administrativa posterior. A mesma conversa e suas duas mensagens anteriores permaneceram. Isso comprova somente essa retomada observada; INOUT02 humana e fluxo oficial continuam requisitos separados no TODO, e a cobertura isolada de app_id estrangeiro está sendo concluída antes da etapa oficial.


### Documento público de privacidade da instalação de testes

O complemento cp63 autorizado pelo usuário disponibiliza /privacidade.html como asset estático do Web, sem autenticação, resolução de Mantenedora/BU, formulários, SDK ou leitura de dados de negócio. A UNIFAST e o contato público unitech@unifast.com.br foram informados pelo responsável. A política distingue tokens oficiais cifrados de outras credenciais, histórico persistente de diagnósticos de webhook da API (rotina90dias), e cópias/estado mantidos pela integração, cuja retenção efetiva não foi demonstrada. Solicitações são tratadas por e-mail, sem promessa de exclusão integral automática. O documento descreve somente a instalação privada de testes; sua URL pública não autoriza publicação Meta/produção nem admissão de usuários não confiáveis.

Fonte cp63: único asset web-app/public/privacidade.html byteexact com cp63-privacy-policy.accepted.html SHA d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d. Crítica independente terminal integrada; build e28testes Web passaram uma vez. A candidata6f teve prova direta/layout e final distinto aceitos; no HTTPS houve transformação Cloudflare, resolvida cp64 pela location exata no-transform da candidata cfd5. Prova pública independente root40f8df7d... confirma20012865/d0 sem scripts/formulários/CFmarkers/cookies/redirect; roothealth200 e JSd143. API segue mesma imagemfe5 com origem atual alinhada; publicação do mesmo app Meta autorizada cp66 e confirmada pelo operador cp67. Baseline posterior permanece semreceipt/connectedAt e IN0/OUT0 na identidade oficial atual; teste real02 não apareceu, readbackcp68 ainda semmensagens e GETMeta confirma appinscrito naWABA. Destinatário/tiques atuais aguardam conferência; causaaberta. O build transitório não foi tratado como prova de dist/HTTP. Evidência no pacote de revisão ST-CON-01.

Histórico operacional (cp106,2026-10-19): o operador concluiu o cadastro oficial Já registrado pelo fluxo atual e confirmou IN visível em Atendimento Local Test Ofc e OUT recebida no WhatsApp do interlocutor. BFF canônico confirmou BU ativa/OWNER, canal oficial CONECTADO/geração2/identidade própria verificada/SUBSCRIBED/receipt confirmado; IDs externos não são expostos nesse DTO. O QR da Local Test BU foi preservado CONECTADO/geração1/identidade e recebimento verificados; sua INOUT e retomada anteriores cp49/52 continuam válidas. Provas antigas de controle sintético e falhas cp62/68 são históricas. A hipótese de proprietário da conversa antiga não foi comprovada. Recuperação oficial CON-12/VAL05 e closeout permanecem pendentes; nenhuma prontidão geral, operação contínua ou conclusão do TODO é declarada. Evidência: artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp106-official-inout-readback.json.

Atualização operacional cp107 (2026-10-19): um único restart autorizado da API preservou seu ID/imagem e mudou StartedAt; health local e HTTPS voltaram200. BFF antes/depois preservou canais oficial/QR, gerações2/1, tentativas, identidade, provider SUBSCRIBED/CONNECTED e receipt true. Nenhuma alteração de fonte/configuração/Meta/credencial/banco. Isso comprova retomada do backend observado, sem comprovar nova IN/OUT ou reconexão da conta Meta. Nova troca física foi solicitada ao mesmo interlocutor alternativo; CON-12/VAL05 e closeout seguem pendentes. [Evidência cp107](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp107-api-restart-recovery.json).

Estado operacional CP108 (2026-10-19): usuário confirmou nova IN visível em Atendimento Local Test Ofc e resposta OUT recebida no WhatsApp após o reinício autorizado da API. Readback confirma o mesmo processo reiniciado, BUs ativas/OWNER, oficial CONECTADO/geração2/SUBSCRIBED/identidade e receipt true, QR preservado CONECTADO/geração1/CONNECTED/receipt true. Com CP106/107 e não oficial CP33/49/52, VAL05 físico local por ambos os canais está satisfeito. Contador Meta POST200 agregado é evidência separada de transporte, sem atribuição de conteúdo/conta. Encerramento local concluído CP108; sem alegar produção, disponibilidade contínua ou importação de histórico. Próximo recorte de produto permanece ST-CON-04 Nova conversa por contato, sujeito a contrato próprio. [Prova CP108](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp108-post-restart-official-inout.json).


## Channel abstrato e envio comum — ST-CON-06

Contrato v1.3 aprovado e exercitado localmente: all93791 passou613testes, revisões independentes de aderência/segurança/cutover/TQA e Performance convergiram, com uma dívida baixa explícita de precisão de métrica de teste. O operador confirmou nova IN e resposta OUT nos vínculos oficial e não oficial após ativação das imagens atuais; a proveniência fonte→imagem→container→HTTP foi conferida antes e depois. A revisão final e os guards de closeout são registrados no [TODO governante](../todos/completed/features/TODO-leadshug-channel-abstraction.md). Evidências: [validação automatizada](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/v13r4-final-validation.json), [ativação](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-activation-provenance-v13r4-final.json), [prova assistida](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/local-operator-proof-v13r4.json) e [proveniência posterior](../artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/post-operator-readback-v13r4.json). Não é prova de produção, disponibilidade contínua ou redes futuras.

Channel is the domain text-send abstraction. TextMessage carries kind:text, opaque recipientRef and text; sendMessage returns a discriminated result. Current Meta/Evolution adapters encapsulate protocol addresses and credentials in an immutable operation instance created by an explicitly registered factory. ChannelResolver is injected through one ChannelTransportModule; existing BFF/Public/Webhooks composition shares its resolver and outbound orchestration. Common senders do not import concrete clients, switch on provider, use service location, mutate singleton credentials, or retain an old dispatch shim. Registration/protocol clients remain legitimate narrow consumers outside the common send boundary.

A server-authorized conversation/BU or accepted verified bot ingress selects the binding. The context captures channel/BU, resource identity, generation, epoch and official credential version. Before the sole external POST, local owner/identity/readiness/version checks fail closed. Same-resource REAUTORIZAR changes generation; it is distinct from a credential-version-only reseal after dispatch. Captured context is never rebound to a newer identity. No HTTP occurs in a DB transaction, and no automatic external retry or per-send external probe is introduced. The local-check-to-network interval and crash recovery remain explicit limitations.

ACCEPTED requires a valid nonempty provider message ID and does not mean handset delivery. BLOCKED occurs locally before dispatch. Meta definitive REJECTED uses only the approved stable Graph envelope allowlist; contradictory/malformed/timeout/redirect/transient results remain UNKNOWN. A supported acknowledgement without ID can yield a positively committed failed/null-ID diagnostic. Arbitrary2xx objects do not establish that acknowledgement. Legacy HTTP codes remain compatible while outcome/evidence accurately describe uncertainty. Known provider acceptance followed by any local failure remains ACCEPTED_LOCAL_INCOMPLETE, with RECORDED only on positive commit or bounded captured-key readback. No blind resend, durable outbox or null-ID echo merge is promised.

Future networks register a concrete implementation against the same narrow port. The current physical origin enum is storage provenance, not a declaration that Instagram/Messenger/Telegram identity, credentials, ingress or lifecycle are implemented. New capabilities, including template authoring/catalog/submission in ST-CON-05, require narrow contracts rather than no-op methods or concrete casts on Channel.

### Contratos de API e resultados seguros

Existing authorization remains upstream of channel resolution: session/BU grant and CSRF for BFF mutations; scoped partner key/account for the public API; accepted verified ingress for Typebot. Availability grants no access and the POST revalidates the bound context. Message and success DTOs are preserved.

| Surface | Contract addition / preserved result |
|---|---|
| GET `/api/bff/conversations/:id/messages` | `janela.disponivel:boolean`, `janela.motivo:AvailabilityReason|null`; existing `exigida`, `aberta`, `expiraEm`, `canal` and timeline pagination retained. Existing authorized read-marker semantics remain separate from observational availability. |
| POST `/api/bff/conversations/:id/messages` | Existing `{texto}` and201 `{id,canal,em}`; shared outbound policy/acceptance and safe uncertainty projection below. |
| GET `/api/v1/conversations` | Add `envio_disponivel:boolean`, `motivo_indisponibilidade:AvailabilityReason|null` per row; retain window/timeline fields. Bindings/credential metadata batched, latest-IN only for actually selected window-requiring origins. |
| GET `/api/v1/conversations/:telefone/messages` | Add `envio_disponivel`, `motivo_indisponibilidade`; existing message/window fields and scoped lookup retained. |
| POST `/api/v1/messages` | Existing numeric phone normalization, account/key scope, rate limit, `{account_id,telefone,texto,atendente?}` and201 `{ok:true,message_id,canal}` retained. Existing conversation creation before attempted send remains; first-send intent belongs to04. |
| Accepted Typebot text output | Same bound abstract send/policy, exact verified ingress, no fabricated human actor, no external replay after refusal/uncertainty/block. |

**Field Definitions**

- `AvailabilityReason`: `CANAL_AUSENTE` no binding; `CANAL_AMBIGUO` multiple bindings without selecting history; `CANAL_SELECIONADO_INDISPONIVEL` selected origin has no usable binding; `CHANNEL_IDENTITY_NOT_VERIFIED` identity proof missing; `CHANNEL_NOT_READY` connection/receipt not ready; `PENDING_CREDENTIAL` credential metadata not active; `JANELA_FECHADA` applicable free-text window closed. Available observation has `motivo=null`.
- Transport `ChannelSendResult.outcome`: `ACCEPTED` valid provider ID; `BLOCKED` local pre-dispatch failure; `REJECTED` proven synchronous refusal; `UNKNOWN` inconclusive dispatched result. Accepted does not mean handset delivery.
- Safe error `outcome`: `BLOCKED`, `REJECTED`, `UNKNOWN`, plus `AMBIGUOUS_SEND_RECORDED` only a positively committed ACK-without-ID diagnostic, and `ACCEPTED_LOCAL_INCOMPLETE` known external acceptance with incomplete local conclusion.
- `evidence`: `ACK_WITHOUT_ID` structurally supported acknowledgement missing ID, or `TRANSPORT_UNCONFIRMED` inconclusive transport result. `localMessageState` and `diagnosticPersistence`: `RECORDED` only positive commit/captured-key readback evidence; otherwise `UNCONFIRMED`. No raw provider text, token, URL, credential envelope or callback data enters these fields.

| Safe error case | HTTP/code and state |
|---|---|
| Proven refusal |400 provider mapper code, `outcome=REJECTED`, fixed refusal text. |
| Unconfirmed transport |Legacy400/code retained with `outcome=UNKNOWN`, `evidence=TRANSPORT_UNCONFIRMED`; no authoritative sent Message. A changed captured context instead takes409 `CHANNEL_CONTEXT_CHANGED`. |
| ACK without ID, positive diagnostic commit |409 `EXTERNAL_MESSAGE_ID_MISSING`, `outcome=AMBIGUOUS_SEND_RECORDED`, `evidence=ACK_WITHOUT_ID`, `diagnosticPersistence=RECORDED`; diagnostic is failed/null-ID, never a sent Message. |
| ACK without ID, diagnostic/context failure |Changed captured context takes409 `CHANNEL_CONTEXT_CHANGED`, `outcome=UNKNOWN`; other diagnostic failure takes503 `OUTBOUND_LOCAL_INCOMPLETE`, `outcome=UNKNOWN`. Persistence metadata reflects only observed commit. |
| Valid provider ID, any local acceptance/finalization failure |409 `CHANNEL_CONTEXT_CHANGED` when captured identity/generation/epoch changed; otherwise503 `OUTBOUND_LOCAL_INCOMPLETE`. Both retain `outcome=ACCEPTED_LOCAL_INCOMPLETE` and truthful `localMessageState`. No extra provider call/rebind. |

The Inbox retains drafts for every error, uses fixed safe text for uncertainty/local-incomplete outcomes, drops duplicate in-flight submit triggers and fences late body/completion effects by BU/conversation generation. Consumers must inspect outcome/evidence rather than infer rejection from a legacy400. No automatic retry is authorized.

### Consumidores seguintes e limites

ST-CON-05 is approved and implemented locally; its durable contract is consolidated below. The seller creates and submits directly for Meta review; no administrator intermediary is inserted. ST-CON-04 may later consume eligible templates for first-send outside the official window, but needs its own approval and must independently revalidate current eligibility and account/channel context. Existing public POST conversation creation before attempted send remains unchanged. Local channel activation and assisted IN/OUT evidence belong to their respective TODOs and do not establish production readiness.

## Modelos textuais — ST-CON-05

This section owns the stable template-management contract. The completed [ST-CON-05 TODO](../todos/completed/features/TODO-leadshug-official-template-authoring.md) remains authoritative for execution, validation, evidence, and closeout. The seller is the submitter; submitted assets belong to the shared remote Messaging account and are not private to their creator. The initial product surface supports official-channel management only. It does not send a template to a recipient or implement ST-CON-04.

### Ownership and persisted records

The `message-templates` domain owns drafts, immutable revisions, submissions, status observations, and the account catalog projection. Its persistence is scoped by the authorized Mantenedora/BU, creator, channel, and server-resolved account. The account-level name reservation is a coordination record across all local links to the same remote account; it carries no draft content and grants no access to another tenant's draft or operation.

| Record | Durable responsibility and invariant |
| --- | --- |
| Draft and revision | Creator, BU, channel, resolved account, monotonic revision, and immutable definition snapshot. `DRAFT` is editable; `LOCKED` is frozen while dispatch or an uncertain/accepted external result is being resolved. No credential is stored here. |
| Submission operation | Scoped idempotency key, request fingerprint, immutable revision reference, phase/outcome, lease/fence, dispatch claim, and safe receipt metadata. A request key replays its original operation; it never authorizes a second POST. |
| Account/name reservation | Canonical remote-account/name/language namespace, coordinated globally for that account. Reservation and release use CAS and positive local commit certainty; conflicts reveal no foreign tenant, owner, content, or counts. |
| Remote observation and catalog projection | Remote ID, account/context identity, supported definition/status fields, observation time, eligibility/freshness, and bounded-page cursor metadata. Individual refresh and catalog refresh update the same observation owner. |

The domain depends on narrow `TemplateManagementResolver` and `MessageTemplateProvider` ports. The resolver receives an already-authorized BU/channel reference and returns an operation-bound provider plus immutable safe context (BU, channel, resource identity, generation, epoch, active credential version, and opaque account reference). The provider exposes template create/list/query operations only. Protocol IDs, addresses, and credentials stay inside the integration adapter. The Meta template adapter has a dedicated client and explicit registration; template services do not import HTTP or concrete Meta clients. Channel and `ChannelResolver` remain text-send contracts and gain no template methods, no-op capability, casts, or provider branches. Management reuses the existing credential resolver/crypto with purpose `template-management`; it does not weaken the `send` purpose or readiness checks.

### API Endpoint Definitions

All endpoints are BFF session routes under `/api/bff`. Reads require an authenticated session and a grant in the resolved BU. Mutations also require CSRF protection. Role shorthand: `ATENDENTE+` means ATENDENTE, ADMIN, or OWNER with a grant in the target BU; `owner/admin` means the draft creator or an ADMIN/OWNER authorized for that BU. A known insufficient role is 403; an absent session is 401; an inaccessible resource/owner is 404. Account, channel, generation, and active credential version are resolved and checked server-side; client IDs never grant scope.

| Method and path | Authorization and request | Outcome and effect |
| --- | --- | --- |
| `GET /api/bff/business-units/:buId/channels/:channelId/message-template-capabilities` | Session, `ATENDENTE+`; no body. | 200 with safe capability, reason, and current generation from local context only. No provider call or credential material. |
| `GET /api/bff/business-units/:buId/message-templates?view=mine&page=1` | Session, creator-scoped `mine`; `view=bu` requires ADMIN/OWNER; page size defaults to 20 and is capped at 50. | 200 local page ordered by `(createdAt,id)`, with `hasMore`; no provider fan-out. |
| `POST /api/bff/business-units/:buId/message-templates/preview` | Session/CSRF, `ATENDENTE+`; `{channelId,expectedGeneration,draftId?,expectedRevision?,definition}`. | 200 normalized definition, plain-text preview, and request fingerprint bound to current context. Zero DB writes and zero provider calls. An unsaved preview is explicitly unpersisted and cannot authorize submit. |
| `POST /api/bff/business-units/:buId/message-templates` | Session/CSRF, `ATENDENTE+`; `{clientRequestId,channelId,expectedGeneration,name,language,category,body,header?,footer?,examples}`. | 201 for a new DRAFT revision 1; account is derived server-side and no Meta POST occurs. Idempotent replay returns the original safe result. |
| `GET /api/bff/message-templates/:id` | Session; own draft or ADMIN/OWNER in its BU. | 200 safe draft/revision/operation projection. Observational only; no provider call or transition. |
| `PATCH /api/bff/message-templates/:id` | Session/CSRF; own editable draft or ADMIN/OWNER; `{expectedRevision,definition}`. | 200 on CAS save with a new immutable revision/fingerprint; 409 on revision/state conflict. No remote mutation. |
| `POST /api/bff/message-templates/:id/submit` | Session/CSRF; owner/admin; `Idempotency-Key` UUID and `{expectedRevision,expectedGeneration,expectedDefinitionFingerprint}`. | At most one Meta POST per durably claimed operation. 201 when newly accepted for processing; 202 while its lease is active; replay returns the same operation/receipt. No `/messages` call. |
| `GET /api/bff/message-templates/:id/operations/:operationId` | Session; same BU and owner/admin. No browser idempotency key. | 200 safe receipt, phase, lease expiry, and server-derived recovery action. Observational; no provider call. |
| `POST /api/bff/message-templates/:id/operations/:operationId/reconcile` | Session/CSRF; owner/admin, same persisted operation. | 202 for a live lease. Expired PREPARED is CAS-closed as REJECTED without dispatch. Expired SENDING/AMBIGUOUS uses bounded GET-only recovery; it never repeats the POST. |
| `POST /api/bff/message-templates/:id/refresh` | Session/CSRF; owner/admin; server-resolved original account/context. | Bounded remote read updates the shared observation only under the current account lease/fence. Stale or failed reads preserve the prior observation and report it unavailable/stale. |
| `GET /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` | Session, `ATENDENTE+`; local page, optional bounded `after` cursor. | 200 cached local catalog page (maximum 50); no remote fan-out. |
| `POST /api/bff/business-units/:buId/channels/:channelId/message-template-catalog` | Session/CSRF, `ATENDENTE+`; `{after?}`. | One bounded remote page per explicit action, through the same account lease/fence and observation projector as individual refresh. No caller-supplied provider URL/cursor URL. |

Common safe HTTP outcomes: 400 for invalid definition/request; 401 unauthenticated; 403 insufficient role on a known BU; 404 inaccessible resource; 409 for revision, account, name, key, or context conflict; 200 for reads/replays; 201 for a newly created draft or accepted operation; 202 for an in-progress operation; 429 with safe `Retry-After`; 503 for an inconclusive provider/local result. Provider text, raw payloads, URLs, tokens, and credential envelopes never appear in responses or logs. Meta review rejection is a `ProviderApprovalStatus.REJECTED` observation, not transport failure or failed creation.

### Field Definitions

Create supports `pt_BR`, `MARKETING` or `UTILITY`, a normalized name matching `[a-z][a-z0-9_]{0,127}`, required BODY text of 1–1024 characters, optional static TEXT HEADER/FOOTER of at most 60 characters each, and up to 20 unique named BODY variables matching `[a-z][a-z_]{0,31}`. Each variable has one fictional text example of 1–128 characters. Unsupported components, malformed/unpaired braces, variables at the start/end, and definitions over 16 KiB are rejected. Preview is backend-validated; React renders escaped text and fences debounced responses by monotonically changing context/revision ownership.

| Field | Values and meaning |
| --- | --- |
| Draft state | `DRAFT` is editable before external submission; `LOCKED` is immutable while submitted, accepted, or uncertain. A proven pre-dispatch rejection can reopen by CAS for a new revision/key; a later Meta analysis rejection does not reopen an accepted revision. |
| Submission outcome | `PREPARED` means no dispatch; `SENDING` means a durable dispatch claim; `ACCEPTED` means a known nonempty remote ID; `REJECTED` means proven refusal; `AMBIGUOUS` means external outcome is unknown. |
| Provider approval status | `PENDING`, `APPROVED`, `REJECTED`, `PAUSED`, `DISABLED`, `ARCHIVED`, `DELETED`, `IN_APPEAL`, `PENDING_DELETION`, `LIMIT_EXCEEDED`, or `UNKNOWN`. `UNKNOWN` is never approval. Requested category and provider-effective category remain separate. |
| Observation eligibility | Only an observed `APPROVED` status in the current account/channel/generation/epoch/managed-identity/credential-version context, no older than 300 seconds by server time, is `observedEligible=true`. Stale, failed, malformed, or context-mismatched refresh preserves prior status but marks it unavailable/stale. ST-CON-04 must independently revalidate before sending. |
| Fingerprints | `requestFingerprint` binds the full immutable local request, account/context, revision, and examples. `remoteSemanticFingerprint` compares exact supported remote semantics and excludes only provider metadata and examples. Content is not trimmed or normalized to force a match. |
| Acceptance provenance | `ACKNOWLEDGED` records a known provider creation ID; `CORRELATED_BY_DEFINITION` records an exact recovery match without proving authorship. `providerAcceptance=CONFIRMED` requires a known acknowledged ID; correlation alone leaves it `UNKNOWN`. A later different acknowledged ID preserves both facts and reports `PROVIDER_ACK_CONFLICT` rather than silently replacing the association. |
| Error/receipt metadata | Template creation returns `ACCEPTED`, proven `REJECTED`, or `AMBIGUOUS`; the operation also has the pre-dispatch phases `PREPARED` and `SENDING`. Post-dispatch uncertainty reports `TEMPLATE_SUBMISSION_UNCERTAIN` with phase `AMBIGUOUS` and outcome `PROVIDER_RESULT_UNCERTAIN`. Local incompleteness reports `TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE`, preserving known acceptance separately. `receiptPersistence=RECORDED` requires positive commit or exact captured-key readback; otherwise it is `UNCONFIRMED`. A recorded receipt can coexist with `projectionPersistence=UNCONFIRMED`. No raw provider text or secret is included. |

### Dispatch, recovery, and shared observation rules

Submission reserves the canonical account/name/language and operation in a short transaction, then performs HTTP outside the transaction. The namespace coordinates every local link to the same remote account, including different BUs/tenants, while all business drafts, operations, and observations remain tenant/BU/creator scoped. Submit performs at most three bounded GETs (grant plus up to two filtered pages) and one POST; each external request times out at 10 seconds, total work is budgeted to 45 seconds under a 60-second operation lease, and durable limits are 10 attempts/minute per actor and 60 dispatches/hour per canonical account namespace. The server performs exact name/language checks; it never scans the full catalog or trusts client/provider continuation URLs. An incomplete filtered listing fails closed without POST. A confirmed claim commit is required before HTTP; uncertain persistence retains the reservation and cannot authorize another POST.

The `PREPARED → SENDING` transition is a CAS over revision, lease, dispatch claim, and captured account context. A durable operation makes at most one POST. A structurally valid response with a nonempty ID is `ACCEPTED`; acceptance and local receipt persistence are separate facts. If an ACK is known but persisting its receipt/association is unconfirmed, the submit endpoint returns 503 `TEMPLATE_SUBMISSION_LOCAL_INCOMPLETE` with outcome/phase `ACCEPTED`, `providerAcceptance=CONFIRMED`, and `receiptPersistence=UNCONFIRMED`; retain the reservation and recover the same operation without another POST. This error response does not include `acceptanceProvenance`; persisted operation/receipt projections expose provenance separately when available. If the receipt is confirmed but its projection is incomplete, keep `receiptPersistence=RECORDED` and report `projectionPersistence=UNCONFIRMED`. A creation response without an ID remains `AMBIGUOUS`, never acknowledged acceptance. A synchronous refusal is `REJECTED` only when the response shape/code proves no creation; timeout, malformed or missing ID, 5xx/429 after dispatch, redirect, transient/unknown code, or crash is `AMBIGUOUS`. No automatic POST retry is allowed.

Reconcile is the sole explicit recovery mutation. A live lease returns 202 without provider access. Expired PREPARED is CAS-closed as `REJECTED(dispatched=false)` and cannot later dispatch. Expired SENDING and AMBIGUOUS recovery are GET-only, under a new lease/fence, against the original account, bounded by grant plus two name-filtered pages. Exactly one semantic match may be recorded as `CORRELATED_BY_DEFINITION`; it does not prove who created the remote asset or that examples were accepted. Missing, multiple, divergent, inaccessible, or incompletely paginated results remain `AMBIGUOUS`, locked, and reserved. Late dispatch results may enrich only their original receipt monotonically; they cannot change a newer revision or context. Existing remote assets found before dispatch conflict and are never adopted or deleted.

Individual refresh and catalog refresh share one persistent lease and monotonic fence per authorized account/context, one 10-second debounce window, and one observation projector. Each writer captures BU, channel, resource identity, generation, epoch, managed identity, and active credential version. Only the owner of the live current fence may update observations, status, `observedAt`, eligibility, or its page cursor. A stale response cannot overwrite newer `APPROVED → PAUSED` or other status. Refresh failure retains the previous status/time/fence/content but marks the current availability unavailable; an explicit later refresh can recover it. Catalog page size is at most 50 and does not fan out per item.

### Decision mapping and accepted limits

The approved D01–D09 and review resolutions AR-01..05 / CR-01..03 are consolidated here; detailed execution criteria remain in the completed TODO:

| Decision | Stable module contract |
| --- | --- |
| D01 | Seller-owned create/submit; existing OWNER/ADMIN/ATENDENTE grants; admin/owner BU view; inaccessible drafts are hidden; remote assets are account-shared, with no approval intermediary. |
| D02 | Backend-authoritative subset, preview, normalization, examples, and fingerprint; no cross-repository import or client-side authoritative parser; no approval guarantee. |
| D03 | `message-templates` owns durable draft/revision/operation/observation/catalog; immutable revisions and CAS; no prior draft decision is replaced. |
| D04 | Explicit `template-management` purpose on the current official managed identity and active credential version; no receipt/readiness bypass and no weakening of `send`. |
| D05 | Durable scoped idempotency, canonical account-wide name namespace, positive commit before HTTP, bounded preflight and one POST maximum. |
| D06 | Typed refusal/acceptance/ambiguity, GET-only recovery, truthful persistence certainty, no automatic mutation retry or external exactly-once claim. |
| D07 | Meta owns approval state; local GET is observational; explicit bounded refresh, shared fenced projector, and 300-second freshness. |
| D08 | UI state belongs to BU/channel/draft/revision/generation/credential-version and monotonic UI context; A→B→A stale results are fenced; no recipient send or premature first-send action. |
| D09 | Narrow template resolver/provider capability is independently registered; Channel/ChannelResolver/OutboundService remain text-only and unchanged. |

AR-01 fixes current credential-version/context CAS, 300-second stale behavior, and ST-CON-04 revalidation. AR-02 makes preview backend-authoritative and unable to authorize submission. AR-03 requires exact server-side name lookup with bounded exhaustion. AR-04 keeps local request and remote semantic fingerprints distinct and preserves examples without claiming authorship. AR-05 preserves existing roles and negative grant/foreign-draft behavior. CR-01 defines observational GET, expired-lease recovery and late-result monotonicity; CR-02 defines evidence-based typed outcomes and default post-dispatch ambiguity; CR-03 permits authorized preview reads while forbidding writes/provider calls. The API contract/raw adapter cases and race harness remain governed by the completed TODO.

Accepted limits: OPS-R4-01 preserves prior status/time/fence/content and reports unavailable after a late failure; explicit refresh can recover. SEC-R6-04 keeps recovery within the current private local cohort until its read-budget follow-up is completed before public/untrusted or Railway exposure. TQA-ST05-03 retains the original test-after/unknown classification; no retrospective RED is claimed. The operator's real own-account proof records creation, status query, and persistence after reload on the owned local HTTPS origin. The actual Meta approval enum, remote receipt/ID, payload, and latency were not reported; this is not evidence of `APPROVED`, recipient delivery, ST-CON-04, public/Railway admission, production readiness, or continuing availability. See [assisted-provider proof](../artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-r42-assisted-provider-proof-v1.1.json), [source/image/running acceptance](../artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-r41-source-image-running-acceptance-v1.1.json), and [assurance disposition](../artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-candidate-r41-assurance-disposition-v1.1.json). Independent final reviews completed; their two documentation findings were integrated against the exact template source. The approved scope is complete locally; closure evidence remains in the completed TODO.

```


---
## foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/inherited-source-seal-v1.1.json
SHA256 25ab222f8fb25cb4e995a4fb08edc2b44363a61159162b77012215f91eb1ac0e

```
{
  "schema": "stcon04.inherited-working-tree.v1.1",
  "recorded_at_utc": "2026-10-22T14:07:45.090002+00:00",
  "scope": "closed positive public files only;68 current feature/inherited paths; no actual env/private traversal",
  "heads": {
    "root": "80e3940126f22a941f90dba4f5e801b6c0eb2f58",
    "api": "db5a86758a165fac8a1ab587599c37b17890530c",
    "web": "74b9d4b714044829796f875d00553f077c1c329d",
    "foundation": "197e7a0713c132c6213e218748655bcda5a19c72"
  },
  "records": [
    {
      "path": "api-app/prisma/migrations/20261021130000_message_template_drafts/migration.sql",
      "sha256": "3feab40fed1c9be1bac9e43464fd587d57693424c4b3012d8c4b8536661d51dd",
      "bytes": 4453,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/prisma/migrations/20261021150000_message_template_operations/migration.sql",
      "sha256": "2822bff860b5aa3476e7614f6a5d5515520dfd8e40708767d1bc4c5bfe2d991d",
      "bytes": 12940,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/prisma/schema.prisma",
      "sha256": "fcbeb82ee13f96fd71ec83eb18b29749ba51bfcdd86fe82108d6e8a3b96efd69",
      "bytes": 38957,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.spec.ts",
      "sha256": "a60d142fcc335de43c5a697d9f7758f722883a1725c824dd0a4b4f0a2f7fb03b",
      "bytes": 4021,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.ts",
      "sha256": "7782792bb945701cc6f6d0ac1460d0504356fa8d73a4261f37112f7c892a23ac",
      "bytes": 6500,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/historico/catalogo.ts",
      "sha256": "5e218ba32cab9f289c77741d43b7c3af7aa93f63cbb58aa52573c6097d77db22",
      "bytes": 7494,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/historico/cobertura.ts",
      "sha256": "b0813176bf1c8fe124a3e17cdaf825433301d0ed8c753dccb228ac098c962e24",
      "bytes": 7676,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-definition.spec.ts",
      "sha256": "9a60549d1c79d73889fd2d47b7ea3bb25b8a0bf140da805f64216decc6ff9d97",
      "bytes": 7219,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-definition.ts",
      "sha256": "1f28bfd19454b1e187b854c4f2e9785b59e7726032c20f82d62460d87401203c",
      "bytes": 9341,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-draft.service.ts",
      "sha256": "429a078fb48d5a66601d83883275dcc12cea659692e463e94a17d41d5cdf0713",
      "bytes": 29240,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.dependencies.spec.ts",
      "sha256": "a03a567e5b96a348b4ab40bb18282a555d30ad3533e6efb929c5d2f2614c82b2",
      "bytes": 3510,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.ports.spec.ts",
      "sha256": "ddf581459b66bf0eb26ec710ded050f45713e5dd5317066cea574dacf57a68bc",
      "bytes": 2963,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-management.ports.ts",
      "sha256": "c7ed169d87a4224f82f8d1abe109bfa02b913bb2cb63303fc6477673f45ed693",
      "bytes": 4562,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-observation.service.ts",
      "sha256": "41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488",
      "bytes": 39343,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-submission.service.ts",
      "sha256": "a2b8b33ecfb0af165c2b94b50703d18a364d5b64ef581bbdd7659325bc631709",
      "bytes": 63540,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/message-templates/template-transaction-boundary.ts",
      "sha256": "ea3e0550ad5c82b263391dbfb3dae6b9e8656d219f18aa0d7c55cd5668722123",
      "bytes": 978,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/message-templates/template-management.module.ts",
      "sha256": "aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd",
      "bytes": 595,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/message-templates/template-management.resolver.ts",
      "sha256": "2a2a57355ff9fa29774cd4dfef33d9d3fd876bdf5d8a8fe654f0c0435284b59a",
      "bytes": 5094,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/meta/message-template.client.spec.ts",
      "sha256": "6b42b44577e2c06ae73fb0525dac10b99f7364a04e2c04184dc303c6d47872b8",
      "bytes": 22687,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/meta/message-template.client.ts",
      "sha256": "8dff223f7a97632cf228800cdbbb12ce6f5b151efc5fa30411d03e5ec3280cb5",
      "bytes": 21888,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/surfaces/bff/bff.module.ts",
      "sha256": "d4e24c7c1a5c88d4a39903383403de742a61700cb208133a77c2d6d5967c0d41",
      "bytes": 6047,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/surfaces/bff/message-templates.controller.ts",
      "sha256": "0e0449a80852a4513f626d0df7b1a5bb17b034eeceb50f53842fb91454ff4491",
      "bytes": 11822,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/browser-server.cjs",
      "sha256": "a5da3c6eb80d5344a383b6079a7a38b107a2794825fc4189891335f9c79fd600",
      "bytes": 12270,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/helpers.ts",
      "sha256": "117e4f85c81dda37ab30e7eb23704b31538c8c5161aa7562a844eaf11de6819c",
      "bytes": 18758,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/message-template-bff.e2e-spec.ts",
      "sha256": "e0212463856dace44908e3762aa206d1ed86deeb95ebbdc926a354d1518902e4",
      "bytes": 29434,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/message-template-drafts.e2e-spec.ts",
      "sha256": "1a7367fc0a97fb9f727276b38186cddb796fc965ce4a9ec9e1078603670f2996",
      "bytes": 14814,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/message-template-management.e2e-spec.ts",
      "sha256": "788fe852c821c62533f560eaa14057789ebb5d2e1ed8fb57affa74b5f7e31d1a",
      "bytes": 178069,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/number-onboarding-bci.e2e-spec.ts",
      "sha256": "779ad4f9f201ef366cd66c2692098957290a15857179d2a5b249415aef1c7bbd",
      "bytes": 14452,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/number-onboarding-pcv.e2e-spec.ts",
      "sha256": "cc5b2c440abe2e6389ee4f4a612a9f01f2584338dc3fc4e5ee4605339ffa0bf9",
      "bytes": 43808,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/timeline-fixtures.cjs",
      "sha256": "181c76e232c560474ff520440ce3a4c089e84ce9bba01bfd4b6d67c283eb12b3",
      "bytes": 31080,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/e2e/message-templates.spec.ts",
      "sha256": "95b6c55145dbd40b8aff0e59484781bf1450eb3f174b1f7ce2ee7dbf9474d68f",
      "bytes": 171505,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/e2e/number-onboarding-freshness.ts",
      "sha256": "880b49f8fa428568692b92a883dd00c5ce76214b1f2db5b35cafb9b0553ed9ad",
      "bytes": 5059,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/e2e/timeline-freshness.ts",
      "sha256": "3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53",
      "bytes": 8499,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/src/App.tsx",
      "sha256": "2d9f3b3d03658a8d6d6132986346f3be8f36a2582faca29285b3d46c9920307e",
      "bytes": 12285,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/src/api.spec.ts",
      "sha256": "5df822dbb810b823a7922dd15e1568b9e8a6f4e5b16541ca5452daaca642d75f",
      "bytes": 7167,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/src/api.ts",
      "sha256": "177d660cccb7d74e47ef1dd180d9e74f830bce97b631c896c4e82fa39ae44a84",
      "bytes": 16058,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/src/telas/Modelos.spec.ts",
      "sha256": "123e1b345342bdba0d1e9de07886c5116fd21c66d92d77a9fd814478142adf52",
      "bytes": 26616,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/src/telas/Modelos.tsx",
      "sha256": "ec5410d1e38a5dd963fe48d3ba715697d9c49cd574875c784fa8e6300275771c",
      "bytes": 58744,
      "active_mutation_admitted": false
    },
    {
      "path": ".github/workflows/ci.yml",
      "sha256": "16acaf6d4b807a806a50a31c75715b14e8b2e220e0e17e2bac43ec4b740318e5",
      "bytes": 4049,
      "active_mutation_admitted": false
    },
    {
      "path": "scripts/test-channels-local.sh",
      "sha256": "de580538f3257a85448cb3ce5030c85b90f65507da53737e4491fdf543091e42",
      "bytes": 12799,
      "active_mutation_admitted": false
    },
    {
      "path": "scripts/check-channels-ci-parity.py",
      "sha256": "d838d557177bf47423a063dfb0cb12b6cdf1e319986c4340286ada097742ce13",
      "bytes": 29038,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/inbox/conversations.service.ts",
      "sha256": "c7d84f983ed61c6022424d4648e07282e7eb53c40fa9aba249618d77b3c223de",
      "bytes": 8137,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/inbox/incoming.service.ts",
      "sha256": "b0ec43187b1f48720aa899e40f979dd0ae447321581d675b84ef9c71dbd0ff42",
      "bytes": 6076,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/inbox/incoming.typebot.integration.spec.ts",
      "sha256": "7b0e7d75fc5809b8c950896818779402fe2bf32ef37a94d970fe081240562975",
      "bytes": 7081,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.spec.ts",
      "sha256": "119d962fdcd9c895b75845dca74d8506147e11480d74b82e8c37f29f97c04081",
      "bytes": 6530,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.ts",
      "sha256": "b0824e8fd4f801a239521855aaa02da5e0943a8c86c4ac8778e2f1f352821698",
      "bytes": 7214,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.spec.ts",
      "sha256": "d7e76f5c392afab1638363d3c851f8ce8c5223ff27c64801a79fdc8ec00d5e7a",
      "bytes": 38572,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.ts",
      "sha256": "9f954f6c1c2bd10030f5eed0cb42e493d6e480106bcfc3f44977cb97a716d34f",
      "bytes": 17388,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/surfaces/bff/conversations.controller.ts",
      "sha256": "53d3cffaa258ba1ad45c21eae4ab8712e2011255b7ca14965f73221edd0cc002",
      "bytes": 5626,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/surfaces/public/conversations.controller.ts",
      "sha256": "bbb5ebf085e59840f3a9e9cbc1f07c57cdc58d1a5b6f846f934fb526cc29bfd1",
      "bytes": 12059,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/surfaces/public/public.module.ts",
      "sha256": "00a96d54fde7061f61f4ddf2b9cef836a02ad77ca29b62ea422695b9d8f90ef8",
      "bytes": 1208,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/surfaces/webhooks/webhooks.module.ts",
      "sha256": "abc8fd7960fcca1ce43d21d44a90f8d4708d47e07bde9a48c0009e02dc0503a6",
      "bytes": 1111,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/api-publica.e2e-spec.ts",
      "sha256": "353497daddfe6ca072ee697aa60d6e9d5762dd869f164d0d3b5b7fbee1d44060",
      "bytes": 20607,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/number-onboarding-typebot.e2e-spec.ts",
      "sha256": "8c23956a13336c4091d62b9aee7383065f81c5e6575661729b044048626cbd8e",
      "bytes": 19718,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/prisma/migrations/20261020170000_message_inbound_window_index/migration.sql",
      "sha256": "586e709e07736eca0908ab5dcc668cf0e0b317189b4c963b361399848a3c9710",
      "bytes": 212,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
      "sha256": "f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3",
      "bytes": 2383,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/channels/transport/channel.ts",
      "sha256": "432796b8685d07dcc53c3a699a7b9d1469ac4fb110aea080766ec207bec8621f",
      "bytes": 2678,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.spec.ts",
      "sha256": "ae1f9208d660c684dca9b1ac5727001d8e57c4c9504be9be1d20ecba32e01805",
      "bytes": 8314,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.ts",
      "sha256": "63bcf773e2b4c5a5ddd688a1bb13745a0a206d995fafc665925df3fecaf394aa",
      "bytes": 13056,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-factory.ts",
      "sha256": "e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc",
      "bytes": 440,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-registry.ts",
      "sha256": "655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b",
      "bytes": 975,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/channels/channel-transport.module.ts",
      "sha256": "32203d3b8393a34a9effab4266683c389651d7ec197e8f9d704a77a6a37f40dc",
      "bytes": 1663,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/channels/evolution-channel.ts",
      "sha256": "60faf1ea40fe17ad62495b0f42a2cf958defcb41e3ad72d3d2213751539b460c",
      "bytes": 1561,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/channels/meta-channel.ts",
      "sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138",
      "bytes": 1613,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/src/integrations/channels/prisma-channel-resolver.ts",
      "sha256": "acf779d89162d339e37af2abe2aa91fd1a1b292d7f5208bb672090c87a23bf4d",
      "bytes": 19223,
      "active_mutation_admitted": false
    },
    {
      "path": "api-app/test/channel-transport.e2e-spec.ts",
      "sha256": "69ddc87cbc9328136f92ea1c1cf9293b0bc2296ad383836322c6feb4b27c6015",
      "bytes": 34765,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/src/telas/Inbox.tsx",
      "sha256": "d70bde9ede67759d479f644598356e46aac2916a12b2ed1770c17a169118586c",
      "bytes": 21225,
      "active_mutation_admitted": false
    },
    {
      "path": "web-app/e2e/channel-transport.spec.ts",
      "sha256": "b3604496727a85d7ce12c2cb6e7a479575356a61ef4c529d385047e066a8e0f3",
      "bytes": 12119,
      "active_mutation_admitted": false
    }
  ],
  "admission_policy": "This initial read is a planning seal, not execution. New approved mutable paths must be explicitly admitted before first implementation; remaining entries must stay byte-exact. No inherited change is silently attributed to ST-CON-04.",
  "source": "closed accepted ST-CON-05 source38 and protected ST-CON-06 inherited30; all match"
}

```


---
## foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/meta-primary-reference-receipt-v1.1.json
SHA256 7e0f20411a6bbe2a8d20282eda55885a14060fdf223357aa49aeb5bebdeec0df

```
{
  "recorded_at_utc": "2026-10-22T14:11:11.501568+00:00",
  "results": [
    {
      "url": "https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/messaging/",
      "status": 200,
      "content_type": "text/markdown; charset=utf-8",
      "bytes": 7321,
      "sha256": "d681158244a335981a9e243533d6d2d095de0cf531b98dd0d244f6063383feaa",
      "method": "anonymous public HTTP Accept:text/markdown; no credentials or provider operations"
    },
    {
      "url": "https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-phone-number/message-api",
      "status": 200,
      "content_type": "text/markdown; charset=utf-8",
      "bytes": 13661,
      "sha256": "55ac95f3f363f325808abe095f85997df7b188cf86441b74f0677823e51a6988",
      "method": "anonymous public HTTP Accept:text/markdown; no credentials or provider operations"
    },
    {
      "url": "https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview/",
      "status": 200,
      "content_type": "text/markdown; charset=utf-8",
      "bytes": 17202,
      "sha256": "636489f74cb2267cb7cdd642ffd11b0f5946a627444044afe83ca403f786dafc",
      "method": "anonymous public HTTP Accept:text/markdown; no credentials or provider operations"
    },
    {
      "url": "https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages/",
      "status": 200,
      "content_type": "text/markdown; charset=utf-8",
      "bytes": 18483,
      "sha256": "08f39dc8aa09d1cd1247fcb9b00bf2aa8a337c9b8c8b8cd33770bd4f8b622a2c",
      "method": "anonymous public HTTP Accept:text/markdown; no credentials or provider operations"
    }
  ],
  "provenance": "web reader initially returned429; official server Markdown representation succeeded anonymously200; not a live account check",
  "facts": [
    "Meta templates are account assets; only APPROVED supports send; NAMED and POSITIONAL parameter semantics are distinct",
    "Service messaging bounded by actual customer interaction window; calls are a platform feature outside this slice",
    "Shared-number multiple messaging-account access requires explicit server-bound messaging_account_id; exactly-one scope omits it and Meta resolves",
    "Meta recommends explicit plus and country code for API recipient; storage identity stays normalized digits",
    "API acceptance is separate from delivery status"
  ],
  "quoted_material_saved": false
}

```


---
## foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/freeze-after-critique-r1-v1.1.json
SHA256 43eefc71b6ad0426b7710becbb035e608c41637331d2d7b9630dde28af3d51fb

```
{
  "created_at_utc": "2026-10-22T14:52:37.091628+00:00",
  "baseline_branch": "main",
  "baseline_commit": "a107a6ab73172c70ef18dc3a34c8681d5e1b5f31",
  "push_reference": "origin/main",
  "push_exit_code": 0,
  "scope": "planning only; both finite critique-r1 clarifications published before affected fresh critique-r2; no product mutation",
  "prior_freeze": "ef1ff014ab158760aadd6436e7c7f3542870c0ab"
}

```


---
## api-app/src/domain/channels/transport/channel.ts
SHA256 432796b8685d07dcc53c3a699a7b9d1469ac4fb110aea080766ec207bec8621f

```
export type ChannelOrigin = 'OFICIAL' | 'NAO_OFICIAL';

export type ChannelAvailabilityReason =
  | 'CANAL_AUSENTE'
  | 'CANAL_AMBIGUO'
  | 'CANAL_SELECIONADO_INDISPONIVEL'
  | 'CHANNEL_IDENTITY_NOT_VERIFIED'
  | 'CHANNEL_NOT_READY'
  | 'PENDING_CREDENTIAL'
  | 'JANELA_FECHADA';

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

export abstract class Channel {
  abstract sendMessage(message: TextMessage): Promise<ChannelSendResult>;
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
  abstract inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability>;
  abstract inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>>;
  abstract contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'>;
}

```


---
## api-app/src/domain/channels/channel-credential-resolver.ts
SHA256 7782792bb945701cc6f6d0ac1460d0504356fa8d73a4261f37112f7c892a23ac

```
import { ConflictException, Injectable } from '@nestjs/common';
import type { Prisma } from '@prisma/client';
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
  activeCredentialVersion: number | null;
  accessToken?: string;
  phoneNumberId?: string;
  wabaId?: string;
  evolutionInstanceName?: string;
}

/** Resolves only a currently verified, owned channel and decrypts its own credential. */
@Injectable()
export class ChannelCredentialResolver {
  constructor(private readonly prisma: PrismaService) {}

  /** Metadata-only check for GET availability; it never decrypts the credential. */
  async inspectActiveCredential(
    channelId: string,
    generation: number,
    expected?: { readonly provider: 'OFICIAL' | 'NAO_OFICIAL'; readonly buId: string },
    transaction?: Prisma.TransactionClient,
  ): Promise<{ version: number | null; ready: boolean }> {
    if (!transaction) return (await this.inspectActiveCredentials([{ channelId, generation, ...expected }])).get(channelId) ?? { version: null, ready: false };
    const credential = await transaction.channelCredential.findUnique({
      where: { channelId }, select: { version: true, generation: true, keyId: true, provider: true, buId: true },
    });
    let currentKeyId: string | null = null;
    try { currentKeyId = loadChannelCredentialKey(process.env).keyId; } catch { /* absent key makes the credential unavailable */ }
    const ready = Boolean(credential && currentKeyId && credential.keyId === currentKeyId
      && credential.generation === generation && (!expected?.provider || credential.provider === expected.provider)
      && (!expected?.buId || credential.buId === expected.buId));
    return { version: credential?.version ?? null, ready };
  }

  /** One metadata-only credential read for a public conversation page. */
  async inspectActiveCredentials(bindings: readonly { channelId: string; generation: number; provider?: 'OFICIAL' | 'NAO_OFICIAL'; buId?: string }[]): Promise<Map<string, { version: number | null; ready: boolean }>> {
    const ids = [...new Set(bindings.map((binding) => binding.channelId))];
    if (!ids.length) return new Map();
    const credentials = await this.prisma.channelCredential.findMany({
      where: { channelId: { in: ids } }, select: { channelId: true, version: true, generation: true, keyId: true, provider: true, buId: true },
    });
    let currentKeyId: string | null = null;
    try {
      currentKeyId = loadChannelCredentialKey(process.env).keyId;
    } catch { /* absent key makes every official channel unavailable */ }
    const byId = new Map(credentials.map((credential) => [credential.channelId, credential]));
    return new Map(bindings.map(({ channelId, generation, provider, buId }) => {
      const credential = byId.get(channelId);
      return [channelId, {
        version: credential?.version ?? null,
        ready: Boolean(credential && credential.generation === generation && currentKeyId && credential.keyId === currentKeyId
          && (!provider || credential.provider === provider) && (!buId || credential.buId === buId)),
      }];
    }));
  }

  async resolve(channelId: string, purpose: 'send' | 'registration' | 'verify' | 'template-management' = 'send'): Promise<ResolvedChannelCredential> {
    const channel = await this.prisma.buChannel.findUnique({
      where: { id: channelId }, include: { credential: true, providerIdentities: true },
    });
    if (!channel || (purpose !== 'verify' && (!channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch))) {
      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
    }
    if (purpose === 'send' && (channel.status !== 'CONECTADO' || !channel.receiptVerifiedAt
      || (channel.type === 'OFICIAL' && channel.providerConnectionState !== 'SUBSCRIBED')
      || (channel.type === 'NAO_OFICIAL' && channel.providerConnectionState !== 'CONNECTED'))) {
      throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
    }
    if (purpose === 'template-management' && channel.type !== 'OFICIAL') {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const identity = channel.providerIdentities.find((row) => row.currentChannelId === channel.id);
    if (!identity || !identity.managedLifecycle || identity.provider !== channel.type || identity.buId !== channel.buId) {
      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
    }
    const result: ResolvedChannelCredential = {
      channelId: channel.id, buId: channel.buId, provider: channel.type, generation: channel.generation,
      pairingEpoch: channel.pairingEpoch, providerResourceIdentityId: identity.id,
      externalResourceId: identity.externalResourceId,
      activeCredentialVersion: channel.type === 'OFICIAL' ? channel.credential?.version ?? null : null,
      ...(channel.phoneNumberId ? { phoneNumberId: channel.phoneNumberId } : {}),
      ...(channel.wabaId ? { wabaId: channel.wabaId } : {}),
      ...(channel.evolutionInstanceName ? { evolutionInstanceName: channel.evolutionInstanceName } : {}),
    };
    if (channel.type === 'OFICIAL') {
      if (!channel.credential || channel.credential.generation !== channel.generation
        || (purpose === 'template-management' && (channel.credential.provider !== channel.type || channel.credential.buId !== channel.buId))) {
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


---
## api-app/src/domain/inbox/outbound.service.ts
SHA256 63bcf773e2b4c5a5ddd688a1bb13745a0a206d995fafc665925df3fecaf394aa

```
import { BadRequestException, ConflictException, HttpException, Injectable, ServiceUnavailableException } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelResolver, type ChannelOperationContext, type VerifiedIngressChannelReference } from '../channels/transport/channel';
import type { ChannelSendResult, ResolvedChannelOperation } from '../channels/transport/channel';
import { MessageAcceptanceService, type MessageAcceptanceInput } from './message-acceptance.service';
import { RealtimeService } from '../../realtime/realtime.service';

const FIXED_UNKNOWN = 'Resultado do envio não confirmado; confira a conversa antes de tentar novamente.';
const FIXED_LOCAL_INCOMPLETE = 'O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente.';
const FIXED_REJECTED = 'O canal recusou o envio.';
const ACK_TIMEOUT_MS = 24 * 60 * 60 * 1000;
type OutboundConversation = Prisma.ConversationGetPayload<object>;

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
  ) {}

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

    if (operation.context.requiresWindow && !await this.windowOpen(conversation.id)) {
      throw new ConflictException({ code: 'JANELA_FECHADA', outcome: 'BLOCKED', error: 'Fora da janela de 24h da última mensagem recebida.' });
    }

    let result: ChannelSendResult;
    try {
      result = await operation.channel.sendMessage({ kind: 'text', recipientRef: conversation.contact, text: input.text });
    } catch {
      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
    }
    if (result.outcome === 'BLOCKED') throw this.blocked(result.reason);
    if (result.outcome === 'REJECTED') {
      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
    }
    if (result.outcome === 'UNKNOWN') return this.finishUnknown(input, conversation, operation.context, result);

    const contextState = await this.contextState(operation.context);
    if (contextState !== 'CURRENT') {
      const message = await this.readBack(conversation, operation.context, result.externalMessageId);
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
      throw this.acceptedIncomplete(after, message ? 'RECORDED' : 'UNCONFIRMED');
    }

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

  private async windowOpen(conversationId: string): Promise<boolean> {
    const lastInbound = await this.prisma.message.findFirst({
      where: { conversationId, direction: 'IN' },
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
      select: { createdAt: true },
    });
    return Boolean(lastInbound && lastInbound.createdAt.getTime() + ACK_TIMEOUT_MS > Date.now());
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
}

```


---
## api-app/src/domain/inbox/message-acceptance.service.ts
SHA256 b053744ee44b7e91fd45b5c146f759f55c70b8e517b8fbb1cab39806407335e1

```
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


---
## api-app/src/domain/inbox/conversations.service.ts
SHA256 c7d84f983ed61c6022424d4648e07282e7eb53c40fa9aba249618d77b3c223de

```
import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { criarCursorTimeline, lerCursorTimeline } from './timeline-pagination';
import { OutboundService } from './outbound.service';
import { ChannelResolver, type ChannelOrigin } from '../channels/transport/channel';
import type { OutboundAttribution } from './outbound.service';

export const JANELA_MS = 24 * 60 * 60 * 1000;

export interface Atendente {
  userId: string;
  nome: string;
}

@Injectable()
export class ConversationsService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly outbound: OutboundService,
    private readonly channelResolver: ChannelResolver,
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
  async estadoDaJanela(conversaId: string, buId: string) {
    const estado = await this.channelResolver.inspectForConversation({ conversationId: conversaId, buId });
    return {
      canal: estado.channelOrigin ? { type: estado.channelOrigin } : null,
      exigeJanela: estado.requiresWindow,
      aberta: estado.windowOpen,
      expiraEm: estado.expiresAt,
      disponivel: estado.available,
      motivoIndisponibilidade: estado.reason,
    };
  }

  async estadosDasJanelas(references: readonly { conversationId: string; buId: string; latestMessageOrigin: ChannelOrigin | null }[]) {
    return this.channelResolver.inspectManyForConversations(references);
  }

  async responder(conversaId: string, buId: string, texto: string, attribution: OutboundAttribution) {
    return this.outbound.send({ conversationId: conversaId, buId, text: texto, attribution });
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
}

```


---
## api-app/src/domain/inbox/incoming.service.ts
SHA256 b0ec43187b1f48720aa899e40f979dd0ae447321581d675b84ef9c71dbd0ff42

```
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


---
## api-app/src/integrations/channels/prisma-channel-resolver.ts
SHA256 acf779d89162d339e37af2abe2aa91fd1a1b292d7f5208bb672090c87a23bf4d

```
import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver, type ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import {
  ChannelResolver,
  type ChannelAvailability,
  type ConversationAvailabilityReference,
  type ChannelOperationContext,
  type ChannelOrigin,
  type ConversationChannelReference,
  type ResolvedChannelOperation,
  type VerifiedIngressChannelReference,
} from '../../domain/channels/transport/channel';
import { ChannelAdapterRegistry } from './channel-adapter-registry';

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
  providerIdentities: Array<{ id: string; buId: string; provider: ChannelOrigin; currentChannelId: string | null; managedLifecycle: boolean }>;
};

@Injectable()
export class PrismaChannelResolver extends ChannelResolver {
  constructor(
    private readonly prisma: PrismaService,
    private readonly credentials: ChannelCredentialResolver,
    private readonly adapters: ChannelAdapterRegistry,
  ) { super(); }

  async resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation> {
    const { candidate } = await this.selectForConversation(reference);
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

      const window = candidate.requiresWindow ? await this.window(reference.conversationId) : { open: true, expiresAt: null };
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
      const windowIds = references
        .filter(({ conversationId }) => selectedById.get(conversationId)?.candidate?.requiresWindow)
        .map(({ conversationId }) => conversationId);
      const windows = windowIds.length
        ? await this.latestInboundByConversation(windowIds)
        : new Map<string, Date>();
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
          const lastInbound = windows.get(id);
          windowOpen = Boolean(lastInbound && lastInbound.getTime() + 24 * 60 * 60 * 1000 > Date.now());
          expiresAt = lastInbound ? new Date(lastInbound.getTime() + 24 * 60 * 60 * 1000) : null;
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
      const window = await this.window(conversation.id);
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
        id: true, buId: true, type: true, status: true, generation: true, pairingEpoch: true,
        verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
        receiptVerifiedAt: true, requiresWindow: true,
        providerIdentities: { select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } },
      },
    }) as unknown as Promise<Candidate[]>;
  }

  private async findCandidate(channelId: string, buId: string): Promise<Candidate | null> {
    const rows = await this.prisma.buChannel.findMany({ where: { id: channelId, buId }, select: {
      id: true, buId: true, type: true, status: true, generation: true, pairingEpoch: true,
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
      select: { id: true, credential: { select: { version: true, generation: true } },
        providerIdentities: { where: { id: context.providerResourceIdentityId }, select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } } },
    });
    const identity = channel?.providerIdentities[0];
    if (!channel || !identity || identity.buId !== context.buId || identity.provider !== context.channelOrigin
      || identity.currentChannelId !== context.channelId || !identity.managedLifecycle) {
      return 'CHANGED';
    }
    if (context.channelOrigin === 'OFICIAL') {
      const credential = channel.credential;
      if (!credential || credential.generation !== context.generation) return 'CHANGED';
      if (beforeDispatch && credential.version !== context.activeCredentialVersion) return 'CHANGED';
    }
    return 'CURRENT';
  }

  private async window(conversationId: string): Promise<{ open: boolean; expiresAt: Date | null }> {
    const lastInbound = await this.prisma.message.findFirst({
      where: { conversationId, direction: 'IN' }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], select: { createdAt: true },
    });
    if (!lastInbound) return { open: false, expiresAt: null };
    const expiresAt = new Date(lastInbound.createdAt.getTime() + 24 * 60 * 60 * 1000);
    return { open: expiresAt.getTime() > Date.now(), expiresAt };
  }

  private async latestInboundByConversation(conversationIds: string[]): Promise<Map<string, Date>> {
    if (!conversationIds.length) return new Map();
    const rows = await this.prisma.$queryRaw<Array<{ conversation_id: string; created_at: Date }>>`
      SELECT requested.conversation_id, latest.created_at
      FROM unnest(ARRAY[${Prisma.join(conversationIds)}]::text[]) AS requested(conversation_id)
      CROSS JOIN LATERAL (
        SELECT message.created_at
        FROM messages AS message
        WHERE message.conversation_id = requested.conversation_id AND message.direction = 'IN'
        ORDER BY message.created_at DESC, message.id DESC
        LIMIT 1
      ) AS latest
    `;
    return new Map(rows.map((row) => [row.conversation_id, row.created_at]));
  }

  private sameCredentialContext(candidate: Candidate, credential: ResolvedChannelCredential): boolean {
    const identity = candidate.providerIdentities.find((item) => item.id === credential.providerResourceIdentityId);
    return credential.channelId === candidate.id && credential.buId === candidate.buId
      && credential.provider === candidate.type && credential.generation === candidate.generation
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


---
## api-app/src/integrations/channels/meta-channel.ts
SHA256 997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138

```
import type { Channel, ChannelSendResult, TextMessage } from '../../domain/channels/transport/channel';
import type { MetaClient } from '../meta/meta.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';

class BoundMetaChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: MetaClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  async sendMessage(message: TextMessage): Promise<ChannelSendResult> {
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    if (!this.credential.phoneNumberId || !this.credential.accessToken) {
      return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
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
  constructor(private readonly client: MetaClient) { super(); }
  locallyConfigured(): boolean { return this.client.canSendText(); }
  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundMetaChannel(credential, this.client, beforeDispatch);
  }
}

```


---
## api-app/src/integrations/channels/evolution-channel.ts
SHA256 60faf1ea40fe17ad62495b0f42a2cf958defcb41e3ad72d3d2213751539b460c

```
import type { Channel, ChannelSendResult, TextMessage } from '../../domain/channels/transport/channel';
import type { EvolutionClient } from '../evolution/evolution.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';

class BoundEvolutionChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: EvolutionClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  async sendMessage(message: TextMessage): Promise<ChannelSendResult> {
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
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


---
## api-app/src/integrations/channels/channel-adapter-factory.ts
SHA256 e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc

```
import type { Channel, ChannelOrigin } from '../../domain/channels/transport/channel';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';

export abstract class ChannelAdapterFactory {
  abstract readonly origin: ChannelOrigin;
  abstract locallyConfigured(): boolean;
  abstract create(
    credential: ResolvedChannelCredential,
    beforeDispatch: () => Promise<boolean>,
  ): Channel;
}

```


---
## api-app/src/integrations/channels/channel-transport.module.ts
SHA256 32203d3b8393a34a9effab4266683c389651d7ec197e8f9d704a77a6a37f40dc

```
import { Module } from '@nestjs/common';
import { ChannelResolver } from '../../domain/channels/transport/channel';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
import { OutboundService } from '../../domain/inbox/outbound.service';
import { EVOLUTION_CLIENT, EvolutionHttpClient } from '../evolution/evolution.client';
import { META_CLIENT, MetaHttpClient } from '../meta/meta.client';
import { ChannelAdapterRegistry } from './channel-adapter-registry';
import { EvolutionChannelFactory } from './evolution-channel';
import { MetaChannelFactory } from './meta-channel';
import { PrismaChannelResolver } from './prisma-channel-resolver';

@Module({
  providers: [
    MessageAcceptanceService,
    ChannelCredentialResolver,
    MetaHttpClient,
    EvolutionHttpClient,
    { provide: META_CLIENT, useExisting: MetaHttpClient },
    { provide: EVOLUTION_CLIENT, useExisting: EvolutionHttpClient },
    {
      provide: ChannelAdapterRegistry,
      useFactory: (meta: MetaHttpClient, evolution: EvolutionHttpClient) => new ChannelAdapterRegistry([
        new MetaChannelFactory(meta),
        new EvolutionChannelFactory(evolution),
      ]),
      inject: [META_CLIENT, EVOLUTION_CLIENT],
    },
    PrismaChannelResolver,
    { provide: ChannelResolver, useExisting: PrismaChannelResolver },
    OutboundService,
  ],
  exports: [
    MessageAcceptanceService,
    ChannelCredentialResolver,
    META_CLIENT,
    EVOLUTION_CLIENT,
    ChannelResolver,
    OutboundService,
  ],
})
export class ChannelTransportModule {}

```


---
## api-app/src/integrations/message-templates/template-management.module.ts
SHA256 aabfb344eab0b244772f0a2a8066dbae71bb24973a0a498c69af676c17f0acdd

```
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


---
## api-app/src/integrations/message-templates/template-management.resolver.ts
SHA256 2a2a57355ff9fa29774cd4dfef33d9d3fd876bdf5d8a8fe654f0c0435284b59a

```
import { ConflictException, Injectable } from '@nestjs/common';
import { createHash } from 'node:crypto';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
import type {
  MessageTemplateProvider,
  ResolvedTemplateManagement,
  TemplateAccountReference,
  TemplateManagementContext,
  TemplateManagementResolver,
  TemplateReference,
} from '../../domain/message-templates/template-management.ports';
import { BoundMetaMessageTemplateProvider, MetaTemplateClient, TemplateManagementProviderError } from '../meta/message-template.client';

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
      accountReference: this.accountReference(channel.wabaId),
    });
    const credential = async (): Promise<string> => {
      const current = await this.credentials.resolve(channel.id, 'template-management');
      if (current.provider !== 'OFICIAL' || current.buId !== context.buId || current.channelId !== context.channelId
        || current.providerResourceIdentityId !== context.providerResourceIdentityId || current.generation !== context.generation
        || current.pairingEpoch !== context.pairingEpoch || current.activeCredentialVersion !== context.activeCredentialVersion
        || current.wabaId !== channel.wabaId || current.phoneNumberId !== channel.phoneNumberId
        || this.accountReference(current.wabaId ?? '') !== context.accountReference || !current.accessToken) {
        throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
      }
      return current.accessToken;
    };
    const provider = this.factories.create(channel.type, context, credential, channel.wabaId);
    return Object.freeze({ context, provider });
  }

  private accountReference(wabaId: string): TemplateAccountReference {
    return createHash('sha256').update(`meta-waba\0${wabaId}`).digest('hex') as TemplateAccountReference;
  }
}

```


---
## api-app/src/integrations/meta/message-template.client.ts
SHA256 8dff223f7a97632cf228800cdbbb12ce6f5b151efc5fa30411d03e5ec3280cb5

```
import { createHash } from 'node:crypto';
import type {
  MessageTemplateProvider,
  TemplateComponentSummary,
  TemplateCreateOutcome,
  TemplateDefinition,
  TemplateDispatchGuard,
  TemplateManagementContext,
  TemplatePage,
  TemplateSummary,
} from '../../domain/message-templates/template-management.ports';

const PROVEN_REFUSAL_CODES = new Set([10, 100, 190, 2388040, 2388047, 2388072, 2388073, 2388293, 2388299]);
const PROVIDER_FIELDS = 'id,name,language,status,category,parameter_format,components';
const OPERATION_BUDGET_MS = 45_000;
const MAX_PROVIDER_RESPONSE_BYTES = 1024 * 1024;

export class TemplateManagementProviderError extends Error {
  constructor(readonly code: 'TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE' | 'TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE') {
    super(code === 'TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE'
      ? 'A autorização atual não permite gerenciar modelos.'
      : 'A resposta do provedor de modelos está indisponível.');
    this.name = 'TemplateManagementProviderError';
  }
}

type GraphError = { readonly type: string; readonly message: string; readonly code: number; readonly is_transient?: boolean };
type Grant = { readonly appId: string; readonly valid: boolean; readonly expiresAt?: number; readonly scopes: readonly string[]; readonly targets: readonly string[] };

class RequestNotDispatchedError extends Error {}

/** Private, operation-scoped Graph client. One instance belongs to one resolved context. */
export class MetaTemplateClient {
  private readonly appId = process.env.META_APP_ID?.trim() ?? '';
  private readonly appSecret = process.env.META_APP_SECRET ?? '';
  private readonly graphVersion = process.env.GRAPH_VERSION?.trim() ?? '';
  private startedAt: number | null = null;
  private grantPromise: Promise<Grant> | null = null;
  private boundToken: string | null = null;
  private boundWaba: string | null = null;

  async createTemplate(input: { accessToken: string; wabaId: string; definition: TemplateDefinition; dispatchGuard?: TemplateDispatchGuard }): Promise<TemplateCreateOutcome> {
    const { accessToken, wabaId, definition } = input;
    try { await this.grant(accessToken, wabaId); } catch {
      return { kind: 'REJECTED', dispatched: false, code: 'PRE_DISPATCH_UNAVAILABLE' };
    }
    const components: Record<string, unknown>[] = [];
    if (definition.header !== undefined) components.push({ type: 'HEADER', format: 'TEXT', text: definition.header });
    const namedExamples = Object.keys(definition.examples).sort().map((paramName) => ({
      param_name: paramName,
      example: definition.examples[paramName],
    }));
    components.push({
      type: 'BODY', text: definition.body,
      ...(namedExamples.length ? { example: { body_text_named_params: namedExamples } } : {}),
    });
    if (definition.footer !== undefined) components.push({ type: 'FOOTER', text: definition.footer });

    let response: Response;
    let payload: unknown;
    try {
      try { await input.dispatchGuard?.beforeDispatch(); } catch { throw new RequestNotDispatchedError(); }
      response = await this.request(`/${encodeURIComponent(wabaId)}/message_templates`, accessToken, 'POST', {
        name: definition.name, language: definition.language, category: definition.category,
        parameter_format: 'NAMED', components,
      });
      payload = await this.readJson(response);
    } catch (error) {
      if (error instanceof RequestNotDispatchedError) return { kind: 'REJECTED', dispatched: false, code: 'PRE_DISPATCH_UNAVAILABLE' };
      return { kind: 'AMBIGUOUS', dispatched: true, code: 'PROVIDER_RESULT_UNCERTAIN' };
    }
    if (!isRecord(payload)) return { kind: 'AMBIGUOUS', dispatched: true, code: 'PROVIDER_RESULT_UNCERTAIN' };
    const hasGraphError = payload.error !== undefined;
    const validId = typeof payload.id === 'string' && payload.id.trim().length > 0 && payload.id.length <= 128;
    const hasAnyId = Object.hasOwn(payload, 'id');
    const contradicted = Object.hasOwn(payload, 'success') || Object.hasOwn(payload, 'data') || Object.hasOwn(payload, 'messages');
    if (response.ok && validId && !hasGraphError && !contradicted) {
      return { kind: 'ACCEPTED', dispatched: true, remoteTemplateId: payload.id as string };
    }
    const graphError = parseGraphError(payload.error);
    if ([400, 401, 403].includes(response.status) && graphError && PROVEN_REFUSAL_CODES.has(graphError.code)
      && graphError.is_transient !== true && !hasAnyId && !contradicted) {
      return { kind: 'REJECTED', dispatched: true, provenNoCreation: true, code: 'PROVIDER_REFUSED' };
    }
    return { kind: 'AMBIGUOUS', dispatched: true, code: 'PROVIDER_RESULT_UNCERTAIN' };
  }

  async listTemplates(input: {
    readonly context: TemplateManagementContext;
    readonly accessToken: string;
    readonly wabaId: string;
    readonly name?: string;
    readonly after: string | null;
    readonly limit: number;
  }): Promise<TemplatePage> {
    if (!Number.isSafeInteger(input.limit) || input.limit < 1 || input.limit > 50
      || (input.name !== undefined && (input.name.length < 1 || input.name.length > 128))
      || (input.after !== null && (input.after.length < 1 || input.after.length > 512))) {
      throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    }
    await this.grant(input.accessToken, input.wabaId);
    const templates: TemplateSummary[] = [];
    const query = new URLSearchParams({ fields: PROVIDER_FIELDS, limit: String(input.limit) });
    if (input.after) query.set('after', input.after);
    if (input.name) query.set('name', input.name);
    const result = await this.readObject(await this.request(`/${encodeURIComponent(input.wabaId)}/message_templates?${query}`, input.accessToken));
    if (!Array.isArray(result.data) || result.data.length > input.limit) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    for (const row of result.data) {
      const summary = parseTemplateSummary(row);
      if (input.name !== undefined && summary.name !== input.name) {
        throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
      }
      templates.push(summary);
    }
    return { templates, nextCursor: parseNextCursor(result.paging) };
  }

  async getTemplate(input: {
    readonly context: TemplateManagementContext;
    readonly accessToken: string;
    readonly wabaId: string;
    readonly remoteTemplateId: string;
  }): Promise<TemplateSummary> {
    if (!input.remoteTemplateId || input.remoteTemplateId.length > 128) {
      throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    }
    await this.grant(input.accessToken, input.wabaId);
    const query = new URLSearchParams({ fields: PROVIDER_FIELDS });
    const result = await this.request(`/${encodeURIComponent(input.remoteTemplateId)}?${query}`, input.accessToken);
    const summary = parseTemplateSummary(await this.readObject(result));
    if (summary.remoteTemplateId !== input.remoteTemplateId) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    return summary;
  }

  private async grant(token: string, wabaId: string): Promise<Grant> {
    if (!token || !wabaId || wabaId.length > 128 || !this.appId || !this.appSecret || !/^v\d+\.0$/.test(this.graphVersion)) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    if (this.boundToken !== null && (this.boundToken !== token || this.boundWaba !== wabaId)) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    this.boundToken = token;
    this.boundWaba = wabaId;
    this.grantPromise ??= this.loadGrant(token, wabaId);
    return this.grantPromise;
  }

  private async loadGrant(token: string, wabaId: string): Promise<Grant> {
    let payload: Record<string, unknown>;
    try {
      const query = new URLSearchParams({ input_token: token });
      const result = await this.request(`/debug_token?${query}`, `${this.appId}|${this.appSecret}`);
      const wrapper = await this.readObject(result);
      if (wrapper.error !== undefined || !isRecord(wrapper.data)) throw new Error('invalid');
      payload = wrapper.data;
    } catch {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    const appId = typeof payload.app_id === 'string' ? payload.app_id : '';
    const valid = payload.is_valid === true;
    if ((Object.hasOwn(payload, 'expires_at') && typeof payload.expires_at !== 'number')
      || (Object.hasOwn(payload, 'data_access_expires_at') && typeof payload.data_access_expires_at !== 'number')) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    const scopes = Array.isArray(payload.scopes) && payload.scopes.every((item) => typeof item === 'string')
      ? payload.scopes as string[] : [];
    const granular = Array.isArray(payload.granular_scopes) ? payload.granular_scopes : [];
    const targets = granular.flatMap((entry) => isRecord(entry) && entry.scope === 'whatsapp_business_management'
      && Array.isArray(entry.target_ids) && entry.target_ids.every((item) => typeof item === 'string')
      ? entry.target_ids as string[] : []);
    const expiresAt = typeof payload.expires_at === 'number' ? payload.expires_at : undefined;
    const dataExpiresAt = typeof payload.data_access_expires_at === 'number' ? payload.data_access_expires_at : undefined;
    const now = Math.floor(Date.now() / 1000);
    const expiryValid = (expiresAt === undefined || expiresAt === 0 || expiresAt > now)
      && (dataExpiresAt === undefined || dataExpiresAt === 0 || dataExpiresAt > now);
    if (appId !== this.appId || !valid || !scopes.includes('whatsapp_business_management')
      || !targets.includes(wabaId) || !expiryValid) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    return { appId, valid, expiresAt: expiresAt ?? dataExpiresAt, scopes, targets };
  }

  private async request(path: string, accessToken?: string, method: 'GET' | 'POST' = 'GET', body?: unknown): Promise<Response> {
    const startedAt = this.startedAt ?? (this.startedAt = Date.now());
    const remainingMs = OPERATION_BUDGET_MS - (Date.now() - startedAt);
    if (remainingMs <= 0 || !/^v\d+\.0$/.test(this.graphVersion)) {
      throw new RequestNotDispatchedError();
    }
    const headers: Record<string, string> = { accept: 'application/json' };
    if (accessToken) headers.authorization = `Bearer ${accessToken}`;
    if (body !== undefined) headers['content-type'] = 'application/json';
    try {
      return await fetch(`https://graph.facebook.com/${this.graphVersion}${path}`, {
        method, headers, body: body === undefined ? undefined : JSON.stringify(body),
        signal: AbortSignal.timeout(Math.max(1, Math.min(10_000, remainingMs))), redirect: 'error',
      });
    } catch {
      throw new Error('unavailable');
    }
  }

  private async readJson(response: Response): Promise<unknown> {
    const reader = response.body?.getReader();
    if (!reader) return null;
    const chunks: Uint8Array[] = [];
    let byteLength = 0;
    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        byteLength += value.byteLength;
        if (byteLength > MAX_PROVIDER_RESPONSE_BYTES) {
          await reader.cancel();
          return null;
        }
        chunks.push(value);
      }
      return JSON.parse(new TextDecoder().decode(Buffer.concat(chunks, byteLength))) as unknown;
    } catch {
      try { await reader.cancel(); } catch { /* body already aborted */ }
      return null;
    }
  }

  private async readObject(response: Response): Promise<Record<string, unknown>> {
    if (!response.ok) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    const payload = await this.readJson(response);
    if (!isRecord(payload) || Object.hasOwn(payload, 'error')) {
      throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    }
    return payload;
  }
}

/** Adapter facade only; all network policy and translation stay in MetaTemplateClient. */
export class BoundMetaMessageTemplateProvider implements MessageTemplateProvider {
  constructor(
    private readonly context: TemplateManagementContext,
    private readonly accessToken: () => Promise<string>,
    private readonly wabaId: string,
    private readonly client: MetaTemplateClient,
  ) {}

  async createTemplate(input: { context: TemplateManagementContext; definition: TemplateDefinition; dispatchGuard?: TemplateDispatchGuard }): Promise<TemplateCreateOutcome> {
    this.assertContext(input.context);
    let accessToken: string;
    try { accessToken = await this.accessToken(); }
    catch { return { kind: 'REJECTED', dispatched: false, code: 'PRE_DISPATCH_UNAVAILABLE' }; }
    return this.client.createTemplate({ accessToken, wabaId: this.wabaId, definition: input.definition, dispatchGuard: input.dispatchGuard });
  }

  async listTemplates(input: { context: TemplateManagementContext; name?: string; after: string | null; limit: number }): Promise<TemplatePage> {
    this.assertContext(input.context);
    const accessToken = await this.accessToken();
    return this.client.listTemplates({ ...input, context: this.context, accessToken, wabaId: this.wabaId });
  }

  async getTemplate(input: { context: TemplateManagementContext; remoteTemplateId: string }): Promise<TemplateSummary> {
    this.assertContext(input.context);
    const accessToken = await this.accessToken();
    return this.client.getTemplate({ ...input, context: this.context, accessToken, wabaId: this.wabaId });
  }

  private assertContext(context: TemplateManagementContext): void {
    if (!sameContext(this.context, context)) throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
  }
}

function parseGraphError(value: unknown): GraphError | null {
  if (!isRecord(value) || typeof value.type !== 'string' || value.type.trim().length === 0
    || typeof value.message !== 'string' || value.message.trim().length === 0
    || typeof value.code !== 'number' || !Number.isSafeInteger(value.code) || value.code < 0
    || (value.is_transient !== undefined && typeof value.is_transient !== 'boolean')) return null;
  return { type: value.type, message: value.message, code: value.code, ...(typeof value.is_transient === 'boolean' ? { is_transient: value.is_transient } : {}) };
}

function parseTemplateSummary(value: unknown): TemplateSummary {
  if (!isRecord(value) || typeof value.id !== 'string' || value.id.trim().length === 0 || value.id.length > 128) {
    throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  }
  const statusValues = new Set(['PENDING', 'APPROVED', 'REJECTED', 'PAUSED', 'DISABLED', 'ARCHIVED', 'DELETED', 'IN_APPEAL', 'PENDING_DELETION', 'LIMIT_EXCEEDED']);
  const categoryValues = new Set(['MARKETING', 'UTILITY', 'AUTHENTICATION']);
  if (Array.isArray(value.components) && value.components.length > 16) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  const components: TemplateComponentSummary[] = Array.isArray(value.components) ? value.components.map(parseComponent) : [{ type: 'UNKNOWN', providerType: 'UNKNOWN', semanticFingerprint: createHash('sha256').update('missing-components').digest('hex') }];
  const summary: Omit<TemplateSummary, 'supported' | 'semanticFingerprint'> = {
    remoteTemplateId: value.id,
    status: typeof value.status === 'string' && statusValues.has(value.status) ? value.status as TemplateSummary['status'] : 'UNKNOWN',
    name: typeof value.name === 'string' && characterCount(value.name) > 0 && characterCount(value.name) <= 128 ? value.name : null,
    language: typeof value.language === 'string' && characterCount(value.language) > 0 && characterCount(value.language) <= 35 ? value.language : null,
    category: typeof value.category === 'string' && categoryValues.has(value.category) ? value.category as TemplateSummary['category'] : 'UNKNOWN',
    parameterFormat: value.parameter_format === 'NAMED' || value.parameter_format === 'POSITIONAL' ? value.parameter_format : 'UNKNOWN',
    components,
  };
  const bodies = components.filter((component) => component.type === 'BODY');
  const headers = components.filter((component) => component.type === 'HEADER');
  const footers = components.filter((component) => component.type === 'FOOTER');
  const noUnknown = components.every((component) => component.type !== 'UNKNOWN');
  const headerSupported = headers.every((component) => component.type === 'HEADER' && component.format === 'TEXT');
  const namedParameters = components.every((component) => component.type === 'UNKNOWN'
    || !('parameters' in component) || component.parameters.every((parameter) => !/^[1-9][0-9]{0,1}$/.test(parameter)));
  const supportable = summary.name !== null && summary.language !== null
    && (summary.category === 'UTILITY' || summary.category === 'MARKETING')
    && summary.parameterFormat === 'NAMED' && bodies.length === 1 && headers.length <= 1
    && footers.length <= 1 && noUnknown && headerSupported && namedParameters
    && bodies[0]?.type === 'BODY' && bodies[0].text.trim().length > 0;
  const semanticFingerprint = supportable ? createHash('sha256').update(canonicalSemanticJson({
      name: summary.name, language: summary.language, category: summary.category,
      parameterFormat: summary.parameterFormat, components: value.components,
    })).digest('hex') : null;
  return { ...summary, supported: supportable, semanticFingerprint };
}

function parseComponent(value: unknown): TemplateComponentSummary {
  if (!isRecord(value) || typeof value.type !== 'string') return unknownComponent(value, 'UNKNOWN');
  const supportedKeys = value.type === 'HEADER'
    ? new Set(['type', 'format', 'text', 'example'])
    : value.type === 'BODY' || value.type === 'FOOTER'
      ? new Set(['type', 'text', 'example'])
      : new Set(['type', 'example']);
  if (Object.keys(value).some((key) => !supportedKeys.has(key))) return unknownComponent(value, 'OTHER');
  if (value.type === 'HEADER') {
    if (value.format === 'TEXT' && typeof value.text === 'string' && characterCount(value.text) <= 60) {
      const parameters = parseRemoteParameters(value.text);
      if (parameters) return { type: 'HEADER', format: 'TEXT', text: value.text, parameters };
      return unknownComponent(value, 'OTHER');
    }
    if (value.text !== undefined) return unknownComponent(value, 'OTHER');
    const format = value.format === 'IMAGE' || value.format === 'VIDEO' || value.format === 'DOCUMENT' ? value.format : 'UNKNOWN';
    if (format === 'UNKNOWN') return unknownComponent(value, 'OTHER');
    return { type: 'HEADER', format, text: null };
  }
  if ((value.type === 'BODY' || value.type === 'FOOTER') && typeof value.text === 'string'
    && characterCount(value.text) <= (value.type === 'BODY' ? 1024 : 60)) {
    const parameters = parseRemoteParameters(value.text);
    if (parameters && (value.type !== 'FOOTER' || parameters.length === 0)) return { type: value.type, text: value.text, parameters };
  }
  return unknownComponent(value, 'OTHER');
}

function parseRemoteParameters(text: string): string[] | null {
  const tokens: string[] = [];
  const pattern = /\{\{([^{}]+)\}\}/g;
  for (const match of text.matchAll(pattern)) {
    if (!/^(?:[a-z][a-z_]{0,31}|[1-9][0-9]{0,1})$/.test(match[1])) return null;
    tokens.push(match[1]);
  }
  if (/[{}]/.test(text.replace(pattern, ''))) return null;
  return tokens;
}

function characterCount(value: string): number {
  return Array.from(value).length;
}

function unknownComponent(value: unknown, providerType: 'OTHER' | 'UNKNOWN'): TemplateComponentSummary {
  return {
    type: 'UNKNOWN', providerType,
    semanticFingerprint: createHash('sha256').update(canonicalSemanticJson(value)).digest('hex'),
  };
}

function canonicalSemanticJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalSemanticJson).join(',')}]`;
  if (isRecord(value)) return `{${Object.keys(value).filter((key) => key !== 'example').sort()
    .map((key) => `${JSON.stringify(key)}:${canonicalSemanticJson(value[key])}`).join(',')}}`;
  return JSON.stringify(value) ?? 'null';
}

function parseNextCursor(value: unknown): string | null {
  if (value === undefined || value === null) return null;
  if (!isRecord(value)) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  if (value.next === undefined || value.next === null || value.next === '') return null;
  if (typeof value.next !== 'string') throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  if (!isRecord(value.cursors)) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  const after = value.cursors.after;
  if (typeof after !== 'string' || after.trim().length === 0 || after.length > 512) {
    throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  }
  return after;
}

function sameContext(a: TemplateManagementContext, b: TemplateManagementContext): boolean {
  return a.mantenedoraId === b.mantenedoraId && a.buId === b.buId && a.channelId === b.channelId && a.providerResourceIdentityId === b.providerResourceIdentityId
    && a.generation === b.generation && a.pairingEpoch === b.pairingEpoch
    && a.activeCredentialVersion === b.activeCredentialVersion && a.accountReference === b.accountReference;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

```


---
## api-app/src/domain/message-templates/template-management.ports.ts
SHA256 c7ed169d87a4224f82f8d1abe109bfa02b913bb2cb63303fc6477673f45ed693

```
import type { Prisma } from '@prisma/client';

export type TemplateCategory = 'MARKETING' | 'UTILITY';
export type TemplateCategorySummary = TemplateCategory | 'AUTHENTICATION' | 'UNKNOWN';
export type TemplateParameterFormat = 'NAMED' | 'POSITIONAL' | 'UNKNOWN';

export type TemplateApprovalStatus =
  | 'PENDING'
  | 'APPROVED'
  | 'REJECTED'
  | 'PAUSED'
  | 'DISABLED'
  | 'ARCHIVED'
  | 'DELETED'
  | 'IN_APPEAL'
  | 'PENDING_DELETION'
  | 'LIMIT_EXCEEDED'
  | 'UNKNOWN';

declare const templateAccountReferenceBrand: unique symbol;

/** Opaque server-created account identity; it is not a provider address or credential. */
export type TemplateAccountReference = string & {
  readonly [templateAccountReferenceBrand]: true;
};

export interface TemplateDefinition {
  readonly name: string;
  readonly language: 'pt_BR';
  readonly category: TemplateCategory;
  readonly header?: string;
  readonly body: string;
  readonly footer?: string;
  readonly examples: Readonly<Record<string, string>>;
}

/** Safe identity captured by a template-management operation, without secrets or protocol addresses. */
export interface TemplateManagementContext {
  readonly mantenedoraId: string;
  readonly buId: string;
  readonly channelId: string;
  readonly providerResourceIdentityId: string;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
  readonly accountReference: TemplateAccountReference;
}

/** The caller must authorize the BU/channel grant before asking the resolver. */
export interface TemplateReference {
  readonly buId: string;
  readonly channelId: string;
  readonly expectedGeneration: number;
}

export interface ResolvedTemplateManagement {
  readonly context: TemplateManagementContext;
  /** Adapter is already bound to the resolved operation and account. */
  readonly provider: MessageTemplateProvider;
}

/** Local, per-operation fence invoked by the adapter after its grant and immediately before POST. */
export interface TemplateDispatchGuard {
  beforeDispatch(): Promise<void>;
}

export interface TemplatePage {
  readonly templates: readonly TemplateSummary[];
  readonly nextCursor: string | null;
}

export interface TemplateSummary {
  readonly remoteTemplateId: string;
  readonly status: TemplateApprovalStatus;
  readonly name: string | null;
  readonly language: string | null;
  readonly category: TemplateCategorySummary;
  readonly parameterFormat: TemplateParameterFormat;
  readonly components: readonly TemplateComponentSummary[];
  readonly supported: boolean;
  readonly semanticFingerprint: string | null;
}

export type TemplateComponentSummary =
  | { readonly type: 'HEADER'; readonly format: 'TEXT'; readonly text: string; readonly parameters: readonly string[] }
  | { readonly type: 'HEADER'; readonly format: 'IMAGE' | 'VIDEO' | 'DOCUMENT' | 'UNKNOWN'; readonly text: null }
  | { readonly type: 'BODY' | 'FOOTER'; readonly text: string; readonly parameters: readonly string[] }
  | { readonly type: 'UNKNOWN'; readonly providerType: 'OTHER' | 'UNKNOWN'; readonly semanticFingerprint?: string };

export type TemplateCreateOutcome =
  | { readonly kind: 'ACCEPTED'; readonly dispatched: true; readonly remoteTemplateId: string }
  | { readonly kind: 'REJECTED'; readonly dispatched: false; readonly code: 'PRE_DISPATCH_UNAVAILABLE' }
  | { readonly kind: 'REJECTED'; readonly dispatched: true; readonly provenNoCreation: true; readonly code: 'PROVIDER_REFUSED' }
  | { readonly kind: 'AMBIGUOUS'; readonly dispatched: true; readonly code: 'PROVIDER_RESULT_UNCERTAIN' };

export const TEMPLATE_MANAGEMENT_RESOLVER = Symbol('TEMPLATE_MANAGEMENT_RESOLVER');

export interface TemplateManagementResolver {
  resolve(reference: TemplateReference, options?: { readonly transaction?: Prisma.TransactionClient }): Promise<ResolvedTemplateManagement>;
}

/** Narrow capability for official template assets; it cannot send messages or accept credentials. */
export interface MessageTemplateProvider {
  createTemplate(input: {
    readonly context: TemplateManagementContext;
    readonly definition: TemplateDefinition;
    readonly dispatchGuard?: TemplateDispatchGuard;
  }): Promise<TemplateCreateOutcome>;
  listTemplates(input: {
    readonly context: TemplateManagementContext;
    readonly name?: string;
    readonly after: string | null;
    readonly limit: number;
  }): Promise<TemplatePage>;
  getTemplate(input: {
    readonly context: TemplateManagementContext;
    readonly remoteTemplateId: string;
  }): Promise<TemplateSummary>;
}


```


---
## api-app/src/domain/message-templates/template-observation.service.ts
SHA256 41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488

```
import { ConflictException, ForbiddenException, Inject, Injectable, NotFoundException, ServiceUnavailableException, UnauthorizedException } from '@nestjs/common';
import { Prisma, type MessageTemplateDraft } from '@prisma/client';
import { createHash, randomUUID } from 'node:crypto';
import { AccessService } from '../access/access.service';
import { atLeast, type Role } from '../access/role';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { TEMPLATE_MANAGEMENT_RESOLVER, type TemplateDefinition, type TemplateManagementContext, type TemplateManagementResolver, type TemplateReference, type TemplateSummary } from './template-management.ports';
import { templateDefinitionSemanticFingerprint } from './template-definition';
import { TEMPLATE_TRANSACTION_BOUNDARY, type TemplateTransactionBoundary } from './template-transaction-boundary';

export const TEMPLATE_OBSERVATION_CLOCK = Symbol('TEMPLATE_OBSERVATION_CLOCK');
export interface TemplateObservationClock { now(): Date }
const LEASE_MS = 60_000;
const DEBOUNCE_MS = 10_000;
const FRESH_MS = 300_000;

class ObservationCommitUnconfirmedError extends Error {}
type ObservationAuthRevalidation = (tx: Prisma.TransactionClient) => Promise<void>;

interface ProjectedSavedObservation {
  remoteTemplateId: string;
  status: string;
  name: string | null;
  language: string | null;
  category: string;
  parameterFormat: string;
  components: Prisma.JsonValue;
  supported: boolean;
  semanticFingerprint: string | null;
  available: boolean;
  safeCode: string | undefined;
  observedAt: Date;
  observedFence: string;
  eligible: boolean;
}

export interface TemplateObservationBinding {
  readonly mantenedoraId: string;
  readonly buId: string;
  readonly channelId: string;
  readonly providerResourceIdentityId: string;
  readonly accountReference: string;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
}

@Injectable()
export class TemplateObservationService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly access: AccessService,
    @Inject(TEMPLATE_MANAGEMENT_RESOLVER) private readonly resolver: TemplateManagementResolver,
    @Inject(TEMPLATE_TRANSACTION_BOUNDARY) private readonly transactions: TemplateTransactionBoundary,
    @Inject(TEMPLATE_OBSERVATION_CLOCK) private readonly clock: TemplateObservationClock,
  ) {}

  async refreshDraft(actorId: string, draftId: string, revalidateAuth?: ObservationAuthRevalidation) {
    const { draft } = await this.authorizeDraft(actorId, draftId);
    const reference = await this.currentReference(actorId, draft.buId, draft.channelId);
    const resolved = await this.resolver.resolve(reference);
    this.assertBinding(draft, resolved.context);
    const operation = await this.prisma.messageTemplateOperation.findFirst({
      where: { draftId, buId: draft.buId, mantenedoraId: draft.mantenedoraId },
      orderBy: [{ revision: 'desc' }], select: { remoteTemplateId: true, acknowledgedRemoteTemplateId: true, phase: true },
    });
    if (!operation?.remoteTemplateId || !['ACCEPTED', 'AMBIGUOUS'].includes(operation.phase)) {
      throw new ConflictException({ code: 'TEMPLATE_REMOTE_ID_UNAVAILABLE' });
    }
    const lease = await this.acquire(resolved.context);
    if (!lease.acquired) return { phase: 'REFRESH_IN_PROGRESS', retryAfter: 10 };
    try {
      const summary = await resolved.provider.getTemplate({ context: resolved.context, remoteTemplateId: operation.remoteTemplateId });
      const applied = await this.applyObservation(actorId, resolved.context, lease, summary, draftId, revalidateAuth);
      if (!applied) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      const projected = await this.projectObservation(resolved.context, summary.remoteTemplateId, draft.definition);
      if (operation.acknowledgedRemoteTemplateId && operation.acknowledgedRemoteTemplateId !== operation.remoteTemplateId) {
        return { ...projected, eligible: false, eligibleForUse: false, safeCode: 'PROVIDER_ACK_CONFLICT' };
      }
      return projected;
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      if (error instanceof ConflictException && error.getResponse() && (error.getResponse() as { code?: string }).code === 'TEMPLATE_REFRESH_SUPERSEDED') throw error;
      if (error instanceof ObservationCommitUnconfirmedError) throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      if (!await this.markUnavailableSafely(actorId, resolved.context, lease, operation.remoteTemplateId, null, 'TEMPLATE_REFRESH_UNAVAILABLE', undefined, revalidateAuth, draftId)) {
        throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      }
      throw new ConflictException({ code: 'TEMPLATE_REFRESH_UNAVAILABLE' });
    }
  }

  async refreshCatalog(actorId: string, buId: string, channelId: string, after: string | null, revalidateAuth?: ObservationAuthRevalidation) {
    await this.authorizeBu(actorId, buId);
    const currentReference = await this.currentReference(actorId, buId, channelId);
    const resolved = await this.resolver.resolve(currentReference);
    const lease = await this.acquire(resolved.context);
    if (!lease.acquired) return { phase: 'REFRESH_IN_PROGRESS', retryAfter: 10 };
    const cursorHash = this.hash(after ?? 'first-page');
    try {
      const page = await resolved.provider.listTemplates({ context: resolved.context, after, limit: 50 });
      const applied = await this.applyCatalogPage(actorId, resolved.context, lease, cursorHash, after, page.templates, page.nextCursor, revalidateAuth);
      if (!applied) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      return this.getCatalog(actorId, buId, channelId, after);
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      if (error instanceof ConflictException && error.getResponse() && (error.getResponse() as { code?: string }).code === 'TEMPLATE_REFRESH_SUPERSEDED') throw error;
      if (error instanceof ObservationCommitUnconfirmedError) throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      if (!await this.markUnavailableSafely(actorId, resolved.context, lease, null, cursorHash, 'TEMPLATE_CATALOG_UNAVAILABLE', after, revalidateAuth)) {
        throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      }
      throw new ConflictException({ code: 'TEMPLATE_CATALOG_UNAVAILABLE' });
    }
  }

  async getCatalog(actorId: string, buId: string, channelId: string, after: string | null) {
    await this.authorizeBu(actorId, buId);
    const currentReference = await this.currentReference(actorId, buId, channelId);
    const resolved = await this.resolver.resolve(currentReference);
    const cursorHash = this.hash(after ?? 'first-page');
    const page = await this.prisma.messageTemplateCatalogPage.findUnique({ where: { contextKey_cursorHash: { contextKey: this.contextKey(resolved.context), cursorHash } } });
    if (!page) return { items: [], nextCursor: null, available: false, safeCode: 'TEMPLATE_CATALOG_NOT_OBSERVED', observedAt: null };
    const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
    if (ids.length > 50) return { items: [], nextCursor: null, available: false,
      safeCode: 'TEMPLATE_CATALOG_INVALID', observedAt: page.observedAt };
    const rows = ids.length ? await this.prisma.$queryRaw<Array<{
      remoteTemplateId: string; status: string; name: string | null; language: string | null; category: string;
      parameterFormat: string; components: Prisma.JsonValue; supported: boolean; semanticFingerprint: string | null;
      available: boolean; safeCode: string | null; observedEligible: boolean; observedAt: Date; observedFence: bigint;
    }>>(Prisma.sql`
      WITH requested AS (
        SELECT remote_template_id, ordinality
        FROM unnest(ARRAY[${Prisma.join(ids)}]::varchar(128)[]) WITH ORDINALITY AS request(remote_template_id, ordinality)
      )
      SELECT observation.remote_template_id AS "remoteTemplateId", observation.status, observation.name, observation.language, observation.category,
        observation.parameter_format AS "parameterFormat", observation.components, observation.supported,
        observation.semantic_fingerprint AS "semanticFingerprint", observation.available, observation.safe_code AS "safeCode",
        observation.observed_eligible AS "observedEligible", observation.observed_at AS "observedAt", observation.observed_fence AS "observedFence"
      FROM requested
      CROSS JOIN LATERAL (
        SELECT remote_template_id, status, name, language, category, parameter_format, components, supported,
          semantic_fingerprint, available, safe_code, observed_eligible, observed_at, observed_fence
        FROM message_template_remote_observations
        WHERE context_key = ${page.contextKey}::char(64)
          AND remote_template_id = requested.remote_template_id
        LIMIT 1
      ) observation
      ORDER BY requested.ordinality`) : [];
    const byId = new Map(rows.map((row) => [row.remoteTemplateId, row]));
    const fresh = this.clock.now().getTime() - page.observedAt.getTime() <= FRESH_MS;
    return { items: ids.flatMap((id) => { const row = byId.get(id); return row ? [this.projectRow(row)] : []; }),
      nextCursor: page.nextCursor, available: page.available && fresh, safeCode: page.safeCode ?? (!fresh ? 'TEMPLATE_CATALOG_STALE' : undefined), observedAt: page.observedAt };
  }

  async projectSavedObservation(binding: TemplateObservationBinding, remoteTemplateId: string,
    definitionValue: unknown, acknowledgedRemoteTemplateId?: string | null): Promise<(ProjectedSavedObservation & { matchesDefinition: boolean; eligibleForUse: boolean }) | null> {
    const historicalContextKey = this.hash({ mantenedoraId: binding.mantenedoraId, buId: binding.buId,
      channelId: binding.channelId, accountReference: binding.accountReference,
      generation: binding.generation, pairingEpoch: binding.pairingEpoch,
      providerResourceIdentityId: binding.providerResourceIdentityId,
      activeCredentialVersion: binding.activeCredentialVersion });
    let currentContext: TemplateManagementContext | null = null;
    try {
      const channel = await this.prisma.buChannel.findFirst({ where: { id: binding.channelId, buId: binding.buId }, select: { generation: true } });
      if (channel) {
        const resolved = await this.resolver.resolve({ buId: binding.buId, channelId: binding.channelId, expectedGeneration: channel.generation });
        const sameResourceAssociation = resolved.context.mantenedoraId === binding.mantenedoraId
          && resolved.context.buId === binding.buId && resolved.context.channelId === binding.channelId
          && resolved.context.providerResourceIdentityId === binding.providerResourceIdentityId
          && resolved.context.accountReference === binding.accountReference;
        if (sameResourceAssociation) currentContext = resolved.context;
      }
    } catch { /* historical detail remains readable, but a stale binding cannot be eligible */ }

    const currentContextKey = currentContext ? this.contextKey(currentContext) : null;
    const currentRow = currentContextKey ? await this.prisma.messageTemplateRemoteObservation.findUnique({
      where: { contextKey_remoteTemplateId: { contextKey: currentContextKey, remoteTemplateId } },
    }) : null;
    const row = currentRow ?? (currentContextKey === historicalContextKey ? null
      : await this.prisma.messageTemplateRemoteObservation.findUnique({
        where: { contextKey_remoteTemplateId: { contextKey: historicalContextKey, remoteTemplateId } },
      }));
    if (!row) return null;
    const currentObservation = currentRow !== null;

    let matchesDefinition = false;
    try { matchesDefinition = row.semanticFingerprint !== null
      && row.semanticFingerprint === this.definitionFingerprint(definitionValue as TemplateDefinition); }
    catch { /* unsupported historical definitions cannot be considered a match */ }
    const projected = this.projectRow(row);
    const available = currentObservation && projected.available;
    const ackMatchesAssociation = !acknowledgedRemoteTemplateId || acknowledgedRemoteTemplateId === remoteTemplateId;
    const eligible = available && matchesDefinition && ackMatchesAssociation && row.supported && row.status === 'APPROVED';
    return { ...projected, available, eligible,
      ...(!currentObservation ? { safeCode: 'TEMPLATE_CONTEXT_STALE' }
        : !ackMatchesAssociation ? { safeCode: 'PROVIDER_ACK_CONFLICT' } : {}),
      matchesDefinition, eligibleForUse: eligible };
  }

  private async acquire(context: TemplateManagementContext): Promise<{ acquired: boolean; ownerId: string; fence: bigint; contextKey: string }> {
    const contextKey = this.contextKey(context);
    const ownerId = randomUUID();
    try { return await this.transactions.run('observation', async (tx) => {
      const now = this.clock.now();
      await tx.messageTemplateObservationLease.createMany({ data: [{
        contextKey, mantenedoraId: context.mantenedoraId, buId: context.buId,
        channelId: context.channelId, accountReference: context.accountReference,
        channelGeneration: context.generation, pairingEpoch: context.pairingEpoch,
        providerResourceIdentityId: context.providerResourceIdentityId,
        activeCredentialVersion: context.activeCredentialVersion ?? 0, fence: 0n,
      }], skipDuplicates: true });
      const current = await tx.messageTemplateObservationLease.findUniqueOrThrow({ where: { contextKey } });
      const debounceDone = !current.lastStartedAt || current.lastStartedAt.getTime() <= now.getTime() - DEBOUNCE_MS;
      const updated = debounceDone ? await tx.messageTemplateObservationLease.updateMany({
        where: { contextKey, lastStartedAt: current.lastStartedAt, OR: [{ leaseUntil: null }, { leaseUntil: { lte: now } }] },
        data: { ownerId, fence: { increment: 1n }, leaseUntil: new Date(now.getTime() + LEASE_MS), lastStartedAt: now },
      }) : { count: 0 };
      const latest = await tx.messageTemplateObservationLease.findUniqueOrThrow({ where: { contextKey } });
      return { acquired: updated.count === 1, ownerId, fence: latest.fence, contextKey };
    }); } catch (error) {
      if (error instanceof ConflictException) throw error;
      throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
    }
  }

  private async applyObservation(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, summary: TemplateSummary, draftId: string, revalidateAuth?: ObservationAuthRevalidation): Promise<boolean> {
    const observedAt = this.clock.now();
    try {
      return await this.transactions.run('observation', async (tx) => {
        await revalidateAuth?.(tx);
        await this.assertTxObservationAccess(tx, actorId, context, draftId);
        if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
        await this.writeObservation(tx, lease, observedAt, summary);
        await this.releaseLease(tx, lease);
        return true;
      });
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      try { if (await this.observationCommitted(lease, observedAt, summary)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async applyCatalogPage(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, cursorHash: string, after: string | null, summaries: readonly TemplateSummary[], nextCursor: string | null, revalidateAuth?: ObservationAuthRevalidation): Promise<boolean> {
    const observedAt = this.clock.now();
    try { return await this.transactions.run('observation', async (tx) => {
      await revalidateAuth?.(tx);
      await this.assertTxObservationAccess(tx, actorId, context);
      if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
      const remoteTemplateIds = summaries.map((summary) => summary.remoteTemplateId);
      for (const summary of summaries) await this.writeObservation(tx, lease, observedAt, summary);
      await tx.messageTemplateCatalogPage.upsert({
        where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
        create: { contextKey: lease.contextKey, cursorHash, requestedCursor: after, remoteTemplateIds: remoteTemplateIds as Prisma.InputJsonValue,
          nextCursor, available: true, safeCode: null, observedAt, observedFence: lease.fence },
        update: { requestedCursor: after, remoteTemplateIds: remoteTemplateIds as Prisma.InputJsonValue, nextCursor,
          available: true, safeCode: null, observedAt, observedFence: lease.fence },
      });
      await this.releaseLease(tx, lease);
      return true;
    }); } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      try { if (await this.catalogPageCommitted(lease, cursorHash, observedAt, summaries, nextCursor)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async writeObservation(tx: Prisma.TransactionClient, lease: { fence: bigint; contextKey: string }, observedAt: Date, summary: TemplateSummary): Promise<void> {
    const observedEligible = summary.supported && summary.status === 'APPROVED';
    await tx.messageTemplateRemoteObservation.upsert({
      where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId } },
      create: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId, status: summary.status,
        name: summary.name, language: summary.language, category: summary.category, parameterFormat: summary.parameterFormat,
        components: summary.components as unknown as Prisma.InputJsonValue, semanticFingerprint: summary.semanticFingerprint,
        supported: summary.supported, available: true, safeCode: null, observedEligible, observedAt, observedFence: lease.fence },
      update: { status: summary.status, name: summary.name, language: summary.language, category: summary.category,
        parameterFormat: summary.parameterFormat, components: summary.components as unknown as Prisma.InputJsonValue,
        semanticFingerprint: summary.semanticFingerprint, supported: summary.supported, available: true,
        safeCode: null, observedEligible, observedAt, observedFence: lease.fence },
    });
  }

  private async observationCommitted(lease: { fence: bigint; contextKey: string }, observedAt: Date, summary: TemplateSummary): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    const row = await this.prisma.messageTemplateRemoteObservation.findUnique({
      where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId } },
      select: { observedAt: true, observedFence: true, semanticFingerprint: true, available: true,
        status: true, name: true, language: true, category: true, parameterFormat: true, components: true, supported: true },
    });
    return Boolean(row && row.observedFence === lease.fence && row.observedAt.getTime() === observedAt.getTime()
      && row.semanticFingerprint === summary.semanticFingerprint && row.available
      && this.sameSummary(row, summary));
  }

  private async catalogPageCommitted(lease: { fence: bigint; contextKey: string }, cursorHash: string, observedAt: Date, summaries: readonly TemplateSummary[], nextCursor: string | null): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    const page = await this.prisma.messageTemplateCatalogPage.findUnique({
      where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
      select: { observedAt: true, observedFence: true, available: true, nextCursor: true, remoteTemplateIds: true },
    });
    if (!page || page.observedFence !== lease.fence || page.observedAt.getTime() !== observedAt.getTime()
      || !page.available || page.nextCursor !== nextCursor) return false;
    const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds : [];
    if (ids.length !== summaries.length || !summaries.every((summary, i) => ids[i] === summary.remoteTemplateId)) return false;
    if (!ids.length) return true;
    const rows = await this.prisma.messageTemplateRemoteObservation.findMany({
      where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids as string[] }, observedFence: lease.fence, observedAt, available: true },
      select: { remoteTemplateId: true, status: true, name: true, language: true, category: true,
        parameterFormat: true, components: true, supported: true, semanticFingerprint: true },
    });
    const byId = new Map(rows.map((row) => [row.remoteTemplateId, row]));
    return rows.length === ids.length && summaries.every((summary) => {
      const row = byId.get(summary.remoteTemplateId);
      return Boolean(row && row.semanticFingerprint === summary.semanticFingerprint && this.sameSummary(row, summary));
    });
  }

  private async markUnavailable(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, remoteId: string | null, cursorHash: string | null, safeCode: string, requestedCursor: string | null = null, revalidateAuth?: ObservationAuthRevalidation, draftId?: string): Promise<boolean> {
    const observedAt = this.clock.now();
    try { return await this.transactions.run('observation', async (tx) => {
      await revalidateAuth?.(tx);
      await this.assertTxObservationAccess(tx, actorId, context, draftId);
      if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
      if (remoteId) await tx.messageTemplateRemoteObservation.updateMany({
        where: { contextKey: lease.contextKey, remoteTemplateId: remoteId },
        data: { available: false, observedEligible: false, safeCode, observedFence: lease.fence },
      });
      if (cursorHash) {
        const page = await tx.messageTemplateCatalogPage.findUnique({ where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } }, select: { remoteTemplateIds: true } });
        const ids = Array.isArray(page?.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
        if (ids.length) await tx.messageTemplateRemoteObservation.updateMany({
          where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids } },
          data: { available: false, observedEligible: false, safeCode, observedFence: lease.fence },
        });
        await tx.messageTemplateCatalogPage.upsert({
          where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
          create: { contextKey: lease.contextKey, cursorHash, requestedCursor,
            remoteTemplateIds: [] as unknown as Prisma.InputJsonValue, nextCursor: null,
            available: false, safeCode, observedAt, observedFence: lease.fence },
          update: { available: false, safeCode, observedFence: lease.fence },
        });
      }
      await this.releaseLease(tx, lease);
      return true;
    }); } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      try { if (await this.unavailableCommitted(lease, remoteId, cursorHash, safeCode)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async markUnavailableSafely(actorId: string, context: TemplateManagementContext,
    lease: { ownerId: string; fence: bigint; contextKey: string }, remoteId: string | null,
    cursorHash: string | null, safeCode: string, requestedCursor: string | null = null,
    revalidateAuth?: ObservationAuthRevalidation, draftId?: string): Promise<boolean> {
    try { return await this.markUnavailable(actorId, context, lease, remoteId, cursorHash, safeCode, requestedCursor, revalidateAuth, draftId); }
    catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      if (error instanceof ObservationCommitUnconfirmedError) {
        throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      }
      throw error;
    }
  }

  private async releaseLeaseAfterAuthorizationFailure(lease: { ownerId: string; fence: bigint; contextKey: string }): Promise<void> {
    try { await this.transactions.run('observation', (tx) => this.releaseLease(tx, lease)); }
    catch { /* authorization response remains authoritative; the bounded lease expires if cleanup cannot be confirmed */ }
  }

  private async unavailableCommitted(lease: { fence: bigint; contextKey: string }, remoteId: string | null, cursorHash: string | null, safeCode: string): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    if (remoteId) {
      const row = await this.prisma.messageTemplateRemoteObservation.findUnique({
        where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: remoteId } },
        select: { available: true, safeCode: true, observedFence: true },
      });
      return Boolean(row && !row.available && row.safeCode === safeCode && row.observedFence === lease.fence);
    }
    if (cursorHash) {
      const page = await this.prisma.messageTemplateCatalogPage.findUnique({
        where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
        select: { available: true, safeCode: true, observedFence: true, remoteTemplateIds: true },
      });
      if (!page || page.available || page.safeCode !== safeCode || page.observedFence !== lease.fence) return false;
      const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
      if (!ids.length) return true;
      const rows = await this.prisma.messageTemplateRemoteObservation.findMany({
        where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids }, available: false, safeCode, observedFence: lease.fence },
        select: { remoteTemplateId: true },
      });
      return rows.length === ids.length;
    }
    return false;
  }

  private sameSummary(row: { status: string; name: string | null; language: string | null; category: string;
    parameterFormat: string; components: Prisma.JsonValue; supported: boolean }, summary: TemplateSummary): boolean {
    return row.status === summary.status && row.name === summary.name && row.language === summary.language
      && row.category === summary.category && row.parameterFormat === summary.parameterFormat
      && row.supported === summary.supported
      && JSON.stringify(row.components) === JSON.stringify(summary.components);
  }

  private async ownsLease(tx: Prisma.TransactionClient, actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, now: Date): Promise<boolean> {
    const lock = await tx.$queryRaw<Array<{ contextKey: string }>>`SELECT context_key AS "contextKey" FROM message_template_observation_leases WHERE context_key = ${lease.contextKey} FOR UPDATE`;
    if (lock.length !== 1) return false;
    const current = await tx.messageTemplateObservationLease.findFirst({ where: {
      contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: now },
      mantenedoraId: context.mantenedoraId, buId: context.buId, channelId: context.channelId, accountReference: context.accountReference,
      channelGeneration: context.generation, pairingEpoch: context.pairingEpoch,
      providerResourceIdentityId: context.providerResourceIdentityId, activeCredentialVersion: context.activeCredentialVersion ?? 0,
    }, select: { contextKey: true } });
    if (!current) return false;
    // Pin all mutable inputs while resolver rechecks the same transaction snapshot.
    await tx.$queryRaw`SELECT id FROM app_users WHERE id = ${actorId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${context.buId} AND mantenedora_id = ${context.mantenedoraId} FOR UPDATE`;
    await tx.$queryRaw`SELECT user_id FROM user_bu_roles WHERE user_id = ${actorId} AND bu_id = ${context.buId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${context.channelId} AND bu_id = ${context.buId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} AND current_channel_id = ${context.channelId} FOR UPDATE`;
    await tx.$queryRaw`SELECT channel_id FROM channel_credentials WHERE channel_id = ${context.channelId} FOR UPDATE`;
    const checkedAt = this.clock.now();
    const stillOwned = await tx.messageTemplateObservationLease.findFirst({ where: {
      contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: checkedAt },
    }, select: { contextKey: true } });
    if (!stillOwned) return false;
    const [actor, bu, grant] = await Promise.all([
      tx.appUser.findFirst({ where: { id: actorId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.businessUnit.findFirst({ where: { id: context.buId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.userBuRole.findUnique({ where: { userId_buId: { userId: actorId, buId: context.buId } }, select: { userId: true } }),
    ]);
    if (!actor || !bu || !grant) return false;
    try {
      const actual = await this.resolver.resolve({ buId: context.buId, channelId: context.channelId, expectedGeneration: context.generation }, { transaction: tx });
      return this.sameContext(context, actual.context);
    } catch { return false; }
  }

  private async releaseLease(tx: Prisma.TransactionClient, lease: { ownerId: string; fence: bigint; contextKey: string }): Promise<void> {
    const checkedAt = this.clock.now();
    const released = await tx.messageTemplateObservationLease.updateMany({ where: { contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: checkedAt } }, data: { ownerId: null, leaseUntil: null } });
    if (released.count !== 1) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
  }

  private async projectObservation(context: TemplateManagementContext, remoteId: string, definitionValue: Prisma.JsonValue) {
    const row = await this.prisma.messageTemplateRemoteObservation.findUnique({ where: { contextKey_remoteTemplateId: { contextKey: this.contextKey(context), remoteTemplateId: remoteId } } });
    if (!row) throw new ConflictException({ code: 'TEMPLATE_REFRESH_UNAVAILABLE' });
    const definition = definitionValue as unknown as TemplateDefinition;
    const current = row.semanticFingerprint !== null && row.semanticFingerprint === this.definitionFingerprint(definition);
    return { ...this.projectRow(row), matchesDefinition: current,
      eligibleForUse: current && row.available && row.supported && row.status === 'APPROVED'
        && this.clock.now().getTime() - row.observedAt.getTime() <= FRESH_MS };
  }

  private projectRow(row: { remoteTemplateId: string; status: string; name: string | null; language: string | null; category: string; parameterFormat: string; components: Prisma.JsonValue; supported: boolean; semanticFingerprint: string | null; available: boolean; safeCode: string | null; observedEligible: boolean; observedAt: Date; observedFence: bigint }): ProjectedSavedObservation {
    const current = this.clock.now().getTime() - row.observedAt.getTime() <= FRESH_MS;
    return { remoteTemplateId: row.remoteTemplateId, status: row.status, name: row.name, language: row.language,
      category: row.category, parameterFormat: row.parameterFormat, components: row.components,
      supported: row.supported, semanticFingerprint: row.semanticFingerprint,
      available: row.available && current, safeCode: row.safeCode ?? undefined,
      observedAt: row.observedAt, observedFence: row.observedFence.toString(),
      eligible: row.available && current && row.observedEligible && row.supported && row.status === 'APPROVED' };
  }

  private async authorizeDraft(actorId: string, draftId: string) {
    const actor = await this.prisma.appUser.findUnique({ where: { id: actorId }, select: { mantenedoraId: true, status: true } });
    if (!actor || actor.status !== 'ATIVO') throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
    const grants = await this.access.grantsDoUsuario(actorId);
    const draft = await this.prisma.messageTemplateDraft.findFirst({ where: { id: draftId, mantenedoraId: actor.mantenedoraId, buId: { in: grants.map((grant) => grant.buId) } } });
    const grant = draft && grants.find((row) => row.buId === draft.buId);
    if (!draft || !grant || (draft.creatorUserId !== actorId && !atLeast(grant.role, 'ADMIN'))) throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
    return { draft, role: grant.role as Role };
  }

  private async assertTxObservationAccess(tx: Prisma.TransactionClient, actorId: string,
    context: TemplateManagementContext, draftId?: string): Promise<void> {
    const [actor, bu, grants] = await Promise.all([
      tx.appUser.findFirst({ where: { id: actorId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.businessUnit.findFirst({ where: { id: context.buId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.$queryRaw<Array<{ role: Role }>>`SELECT role::text AS role FROM user_bu_roles
        WHERE user_id = ${actorId} AND bu_id = ${context.buId} FOR SHARE`,
    ]);
    if (!actor) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    if (!bu) throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    const role = grants[0]?.role;
    if (!role) throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
    if (draftId) {
      const draft = await tx.messageTemplateDraft.findFirst({ where: {
        id: draftId, buId: context.buId, mantenedoraId: context.mantenedoraId,
        channelId: context.channelId, providerResourceIdentityId: context.providerResourceIdentityId,
        accountReference: context.accountReference,
      }, select: { creatorUserId: true } });
      if (!draft) throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
      if (draft.creatorUserId !== actorId && !atLeast(role, 'ADMIN')) {
        throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
      }
    } else if (!atLeast(role, 'ATENDENTE')) {
      throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
    }
  }

  private isAuthOrAccessFailure(error: unknown): boolean {
    return error instanceof UnauthorizedException || error instanceof ForbiddenException || error instanceof NotFoundException;
  }

  private async authorizeBu(actorId: string, buId: string): Promise<void> {
    const scoped = await this.access.resolverBu(actorId, buId);
    const actor = await this.prisma.appUser.findUnique({ where: { id: actorId }, select: { mantenedoraId: true, status: true } });
    const bu = await this.prisma.businessUnit.findUnique({ where: { id: buId }, select: { mantenedoraId: true, status: true } });
    if (!scoped || !actor || actor.status !== 'ATIVO' || !bu || bu.status !== 'ATIVO' || actor.mantenedoraId !== bu.mantenedoraId) {
      throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    }
  }

  private assertBinding(draft: MessageTemplateDraft, context: TemplateManagementContext): void {
    if (draft.mantenedoraId !== context.mantenedoraId || draft.channelId !== context.channelId || draft.providerResourceIdentityId !== context.providerResourceIdentityId) throw new ConflictException({ code: 'TEMPLATE_CHANNEL_CONTEXT_STALE' });
    if (draft.accountReference !== context.accountReference) throw new ConflictException({ code: 'CONTA_ALTERADA' });
  }

  private sameContext(a: TemplateManagementContext, b: TemplateManagementContext): boolean {
    return a.mantenedoraId === b.mantenedoraId && a.buId === b.buId && a.channelId === b.channelId && a.accountReference === b.accountReference
      && a.providerResourceIdentityId === b.providerResourceIdentityId && a.generation === b.generation
      && a.pairingEpoch === b.pairingEpoch && a.activeCredentialVersion === b.activeCredentialVersion;
  }

  private async currentReference(actorId: string, buId: string, channelId: string): Promise<TemplateReference> {
    await this.authorizeBu(actorId, buId);
    const channel = await this.prisma.buChannel.findFirst({ where: { id: channelId, buId }, select: { generation: true } });
    if (!channel) throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    return { buId, channelId, expectedGeneration: channel.generation };
  }
  private contextKey(context: TemplateManagementContext): string { return this.hash({ mantenedoraId: context.mantenedoraId, buId: context.buId, channelId: context.channelId, accountReference: context.accountReference, generation: context.generation, pairingEpoch: context.pairingEpoch, providerResourceIdentityId: context.providerResourceIdentityId, activeCredentialVersion: context.activeCredentialVersion }); }
  private hash(value: unknown): string { return createHash('sha256').update(this.canonicalJson(value)).digest('hex'); }
  private canonicalJson(value: unknown): string {
    if (Array.isArray(value)) return `[${value.map((item) => this.canonicalJson(item)).join(',')}]`;
    if (value && typeof value === 'object') {
      const row = value as Record<string, unknown>;
      return `{${Object.keys(row).filter((key) => key !== 'example').sort().map((key) => `${JSON.stringify(key)}:${this.canonicalJson(row[key])}`).join(',')}}`;
    }
    return JSON.stringify(value) ?? 'null';
  }
  private definitionFingerprint(definition: TemplateDefinition): string {
    return templateDefinitionSemanticFingerprint(definition);
  }
}

```


---
## api-app/src/surfaces/bff/conversations.controller.ts
SHA256 53d3cffaa258ba1ad45c21eae4ab8712e2011255b7ca14965f73221edd0cc002

```
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


---
## api-app/src/surfaces/bff/message-templates.controller.ts
SHA256 0e0449a80852a4513f626d0df7b1a5bb17b034eeceb50f53842fb91454ff4491

```
import { BadRequestException, Body, Controller, Get, Headers, HttpCode, HttpStatus, Param, Patch, Post, Query, Req, Res, UnauthorizedException } from '@nestjs/common';
import type { Prisma } from '@prisma/client';
import type { Request, Response } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { TemplateDraftService } from '../../domain/message-templates/template-draft.service';
import { TemplateSubmissionService } from '../../domain/message-templates/template-submission.service';
import { TemplateObservationService } from '../../domain/message-templates/template-observation.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { SessionService } from '../../infra/session/session.service';

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const DEFINITION_KEYS = ['name', 'language', 'category', 'body', 'header', 'footer', 'examples'];

@Controller('api/bff')
export class MessageTemplatesController {
  constructor(
    private readonly access: AccessService,
    private readonly drafts: TemplateDraftService,
    private readonly submissions: TemplateSubmissionService,
    private readonly observations: TemplateObservationService,
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
  ) {}

  @Get('business-units/:buId/channels/:channelId/message-template-capabilities')
  async capabilities(@Param('buId') buId: string, @Param('channelId') channelId: string, @Req() req: Request) {
    requireUuid(buId); requireUuid(channelId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    return this.drafts.capabilities(req.usuario!.id, buId, channelId);
  }

  @Get('business-units/:buId/message-templates')
  async list(@Param('buId') buId: string, @Query() query: Record<string, string>, @Req() req: Request) {
    requireUuid(buId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    if (Object.keys(query).some((key) => !['view', 'page', 'limit'].includes(key))) throw badRequest();
    const page = query.page === undefined ? undefined : Number(query.page);
    const limit = query.limit === undefined ? undefined : Number(query.limit);
    if ((page !== undefined && (!Number.isSafeInteger(page) || page < 1))
      || (limit !== undefined && (!Number.isSafeInteger(limit) || limit < 1 || limit > 50))) throw badRequest();
    if (query.view !== undefined && query.view !== 'mine' && query.view !== 'bu') throw badRequest();
    return this.drafts.listDrafts(req.usuario!.id, buId, { view: query.view as 'mine' | 'bu' | undefined, page, limit });
  }

  @Post('business-units/:buId/message-templates/preview')
  @HttpCode(HttpStatus.OK)
  async preview(@Param('buId') buId: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    requireUuid(buId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    strictKeys(body, ['channelId', 'expectedGeneration', 'draftId', 'expectedRevision', 'definition']);
    if (typeof body.channelId !== 'string' || typeof body.expectedGeneration !== 'number'
      || !Number.isSafeInteger(body.expectedGeneration) || body.expectedGeneration < 1 || !('definition' in body)) throw badRequest();
    requireUuid(body.channelId);
    return this.drafts.preview(req.usuario!.id, {
      buId, channelId: body.channelId, expectedGeneration: body.expectedGeneration,
      ...(body.draftId === undefined ? {} : { draftId: stringField(body.draftId) }),
      ...(body.expectedRevision === undefined ? {} : { expectedRevision: numberField(body.expectedRevision) }),
      definition: body.definition,
    });
  }

  @Post('business-units/:buId/message-templates')
  async create(@Param('buId') buId: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(buId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    strictKeys(body, ['clientRequestId', 'channelId', 'expectedGeneration', ...DEFINITION_KEYS]);
    if (!UUID.test(stringField(body.clientRequestId)) || typeof body.channelId !== 'string'
      || typeof body.expectedGeneration !== 'number' || !Number.isSafeInteger(body.expectedGeneration) || body.expectedGeneration < 1) throw badRequest();
    requireUuid(body.channelId);
    const result = await this.drafts.createDraft(req.usuario!.id, {
      buId, clientRequestId: body.clientRequestId as string, channelId: body.channelId,
      expectedGeneration: body.expectedGeneration as number, definition: definitionFrom(body),
    });
    if ('replayed' in result && result.replayed) res.status(HttpStatus.OK);
    return result;
  }

  @Get('message-templates/:id')
  get(@Param('id') id: string, @Req() req: Request) { requireUuid(id); return this.drafts.getDraftById(req.usuario!.id, id); }

  @Patch('message-templates/:id')
  async save(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    requireUuid(id);
    strictKeys(body, ['expectedRevision', 'definition']);
    if (!('definition' in body)) throw badRequest();
    return this.drafts.saveDraftById(req.usuario!.id, id, numberField(body.expectedRevision), body.definition);
  }

  @Post('message-templates/:id/submit')
  @HttpCode(HttpStatus.CREATED)
  async submit(@Param('id') id: string, @Headers('idempotency-key') key: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(id);
    strictKeys(body, ['expectedRevision', 'expectedGeneration', 'expectedDefinitionFingerprint']);
    if (!UUID.test(key ?? '') || typeof body.expectedDefinitionFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(body.expectedDefinitionFingerprint)) throw badRequest();
    const result = await this.submissions.submitDraft(req.usuario!.id, {
      draftId: id, expectedRevision: numberField(body.expectedRevision),
      expectedGeneration: numberField(body.expectedGeneration),
      expectedDefinitionFingerprint: body.expectedDefinitionFingerprint as string, idempotencyKey: key,
    }, this.authRevalidation(req));
    if (result.phase === 'PREPARED' || result.phase === 'SENDING' || ('recoveryInProgress' in result && result.recoveryInProgress === true)) res.status(HttpStatus.ACCEPTED);
    else if ('replayed' in result && result.replayed === true) res.status(HttpStatus.OK);
    return result;
  }

  @Get('message-templates/:id/operations/:operationId')
  operation(@Param('id') id: string, @Param('operationId') operationId: string, @Req() req: Request) {
    requireUuid(id); requireUuid(operationId);
    return this.submissions.getOperation(req.usuario!.id, id, operationId);
  }

  @Post('message-templates/:id/operations/:operationId/reconcile')
  @HttpCode(HttpStatus.OK)
  async reconcile(@Param('id') id: string, @Param('operationId') operationId: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(id); requireUuid(operationId);
    strictKeys(body ?? {}, []);
    const result = await this.submissions.reconcile(req.usuario!.id, id, operationId, this.authRevalidation(req));
    if ('recoveryInProgress' in result && result.recoveryInProgress === true) res.status(HttpStatus.ACCEPTED);
    return result;
  }

  @Post('message-templates/:id/refresh')
  @HttpCode(HttpStatus.OK)
  async refreshDraft(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(id);
    strictKeys(body ?? {}, []);
    const result = await this.observations.refreshDraft(req.usuario!.id, id, this.authRevalidation(req));
    if ('phase' in result && result.phase === 'REFRESH_IN_PROGRESS') res.status(HttpStatus.ACCEPTED);
    return result;
  }

  @Get('business-units/:buId/channels/:channelId/message-template-catalog')
  async getCatalog(@Param('buId') buId: string, @Param('channelId') channelId: string, @Query() query: Record<string, string>, @Req() req: Request) {
    requireUuid(buId); requireUuid(channelId);
    if (Object.keys(query).some((key) => key !== 'after') || (query.after !== undefined && (typeof query.after !== 'string' || query.after.length < 1 || query.after.length > 512))) throw badRequest();
    return this.observations.getCatalog(req.usuario!.id, buId, channelId, query.after ?? null);
  }

  @Post('business-units/:buId/channels/:channelId/message-template-catalog')
  @HttpCode(HttpStatus.OK)
  async refreshCatalog(@Param('buId') buId: string, @Param('channelId') channelId: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(buId); requireUuid(channelId);
    strictKeys(body ?? {}, ['after']);
    const after = body?.after === undefined ? null : stringField(body.after);
    if (after !== null && (after.length < 1 || after.length > 512)) throw badRequest();
    const result = await this.observations.refreshCatalog(req.usuario!.id, buId, channelId, after, this.authRevalidation(req));
    if ('phase' in result && result.phase === 'REFRESH_IN_PROGRESS') res.status(HttpStatus.ACCEPTED);
    return result;
  }

  private authRevalidation(req: Request): (tx?: Prisma.TransactionClient) => Promise<void> {
    const claimsAtRequest = this.sessions.verificar(this.sessions.extrairDoCabecalho(req.headers.cookie));
    if (!claimsAtRequest || claimsAtRequest.uid !== req.usuario!.id) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    return async (tx) => {
      const claims = this.sessions.verificar(this.sessions.extrairDoCabecalho(req.headers.cookie));
      let user: { id: string; status: string; passwordChangedAt: Date | null } | null = null;
      if (claims && claims.uid === claimsAtRequest.uid) {
        if (tx) {
          const rows = await tx.$queryRaw<Array<{ id: string; status: string; passwordChangedAt: Date | null }>>`
            SELECT id, status::text AS status, password_changed_at AS "passwordChangedAt"
            FROM app_users WHERE id = ${claims.uid} FOR UPDATE`;
          user = rows[0] ?? null;
        } else {
          user = await this.prisma.appUser.findUnique({ where: { id: claims.uid }, select: { id: true, status: true, passwordChangedAt: true } });
        }
      }
      if (!claims || claims.uid !== claimsAtRequest.uid || claims.iat !== claimsAtRequest.iat || claims.exp !== claimsAtRequest.exp
        || !user || user.status !== 'ATIVO' || (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat)) {
        throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
      }
    };
  }
}

function strictKeys(value: unknown, allowed: readonly string[]): asserts value is Record<string, unknown> {
  if (!value || typeof value !== 'object' || Array.isArray(value)
    || Object.keys(value).some((key) => !allowed.includes(key))) throw badRequest();
}
function requireUuid(value: unknown): asserts value is string { if (typeof value !== 'string' || !UUID.test(value)) throw badRequest(); }
function stringField(value: unknown): string { if (typeof value !== 'string') throw badRequest(); return value; }
function numberField(value: unknown): number { if (typeof value !== 'number' || !Number.isSafeInteger(value) || value < 1) throw badRequest(); return value; }
function definitionFrom(body: Record<string, unknown>): Record<string, unknown> {
  const definition: Record<string, unknown> = {};
  for (const key of DEFINITION_KEYS) if (key in body) definition[key] = body[key];
  return definition;
}
function badRequest(): BadRequestException { return new BadRequestException({ code: 'TEMPLATE_PAYLOAD_INVALID' }); }

```


---
## api-app/src/surfaces/webhooks/meta.controller.ts
SHA256 64fd78568c1dc99e74df8a3f5b3157c43c6467ef03544b7741f0b9c7dc11200b

```
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


---
## api-app/prisma/schema.prisma
SHA256 fcbeb82ee13f96fd71ec83eb18b29749ba51bfcdd86fe82108d6e8a3b96efd69

```
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
  messageTemplateDrafts MessageTemplateDraft[]
  messageTemplateOperations MessageTemplateOperation[]

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
  messageTemplateDrafts MessageTemplateDraft[]
  messageTemplateOperations MessageTemplateOperation[]
  messageTemplateObservationLeases MessageTemplateObservationLease[]

  @@unique([id, mantenedoraId])
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
  pendingCleanupIdentityId String? @map("pending_cleanup_identity_id")

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
  managedLifecycle Boolean @default(false) @map("managed_lifecycle")
  cleanupState String @default("UNMANAGED") @map("cleanup_state")
  cleanupLeaseToken String? @map("cleanup_lease_token")
  cleanupLeaseUntil DateTime? @map("cleanup_lease_until")
  messages Message[]
  messageTemplateDrafts MessageTemplateDraft[]

  @@unique([id, buId])
  @@unique([provider, externalResourceId])
  @@index([buId])
  @@index([currentChannelId])
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
  createdMessageTemplateDrafts MessageTemplateDraft[]
  messageTemplateOperations MessageTemplateOperation[]
  setorGrants SetorGrant[]
  tokens      TokenDeAcesso[]

  @@unique([id, mantenedoraId])
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
  @@index([conversationId, direction, createdAt, id], map: "messages_conversation_direction_created_id_idx")
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

enum MessageTemplateDraftState {
  DRAFT
  LOCKED
}

/// Safe local draft snapshot. Provider identities and account references stay server-side.
model MessageTemplateDraft {
  id String @id @default(uuid())
  mantenedoraId String @map("mantenedora_id")
  mantenedora Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Restrict, map: "mt_draft_mantenedora_fkey")
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_draft_bu_fkey")
  creatorUserId String @map("creator_user_id")
  creator AppUser @relation(fields: [creatorUserId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_draft_creator_fkey")
  /// Historical immutable BuChannel id; the channel row is transient and may be detached.
  channelId String @map("channel_id")
  providerResourceIdentityId String @map("provider_resource_identity_id")
  providerResourceIdentity ProviderResourceIdentity @relation(fields: [providerResourceIdentityId, buId], references: [id, buId], onDelete: Restrict, map: "mt_draft_identity_fkey")
  accountReference String @map("account_reference") @db.VarChar(128)
  channelGeneration Int @map("channel_generation")
  pairingEpoch Int @map("pairing_epoch")
  activeCredentialVersion Int? @map("active_credential_version")
  clientRequestId String @map("client_request_id") @db.VarChar(128)
  requestHash String @map("request_hash") @db.Char(64)
  state MessageTemplateDraftState @default(DRAFT)
  revision Int @default(1)
  definition Json
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  revisions MessageTemplateRevision[]
  operations MessageTemplateOperation[]

  @@unique([id, buId, mantenedoraId], map: "mt_draft_id_bu_tenant_uq")

  @@unique([buId, creatorUserId, clientRequestId], map: "mt_draft_bu_creator_req_uq")
  @@index([buId, creatorUserId, createdAt, id], map: "mt_draft_bu_creator_created_idx")
  @@index([buId, createdAt, id], map: "mt_draft_bu_created_idx")
  @@map("message_template_drafts")
}

model MessageTemplateRevision {
  id String @id @default(uuid())
  draftId String @map("draft_id")
  draft MessageTemplateDraft @relation(fields: [draftId], references: [id], onDelete: Cascade, map: "mt_revision_draft_fkey")
  revision Int
  definition Json
  createdAt DateTime @default(now()) @map("created_at")

  @@unique([draftId, revision], map: "mt_revision_draft_rev_uq")
  @@map("message_template_revisions")
}

enum MessageTemplateOperationPhase {
  PREPARED
  SENDING
  ACCEPTED
  REJECTED
  AMBIGUOUS
}

enum MessageTemplateAcceptanceProvenance {
  ACKNOWLEDGED
  CORRELATED_BY_DEFINITION
}

/// Durable, immutable submit intent. The provider request is always derived
/// from this snapshot and can never be rebound to a later credential/account.
model MessageTemplateOperation {
  id String @id @default(uuid())
  mantenedoraId String @map("mantenedora_id")
  mantenedora Mantenedora @relation(fields: [mantenedoraId], references: [id], onDelete: Restrict, map: "mt_ops_mantenedora_fkey")
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_ops_bu_fkey")
  draftId String @map("draft_id")
  draft MessageTemplateDraft @relation(fields: [draftId, buId, mantenedoraId], references: [id, buId, mantenedoraId], onDelete: Restrict, map: "mt_ops_draft_fkey")
  actorUserId String @map("actor_user_id")
  actor AppUser @relation(fields: [actorUserId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_ops_actor_fkey")
  idempotencyKey String @map("idempotency_key") @db.Uuid
  requestHash String @map("request_hash") @db.Char(64)
  expectedFingerprint String @map("expected_fingerprint") @db.Char(64)
  revision Int
  definitionSnapshot Json @map("definition_snapshot")
  channelId String @map("channel_id")
  providerResourceIdentityId String @map("provider_resource_identity_id")
  accountReference String @map("account_reference") @db.VarChar(128)
  channelGeneration Int @map("channel_generation")
  pairingEpoch Int @map("pairing_epoch")
  activeCredentialVersion Int? @map("active_credential_version")
  phase MessageTemplateOperationPhase @default(PREPARED)
  version Int @default(1)
  dispatchClaimId String? @unique(map: "mt_ops_dispatch_claim_uq") @map("dispatch_claim_id") @db.Uuid
  leaseOwnerId String? @map("lease_owner_id") @db.Uuid
  leaseUntil DateTime? @map("lease_until")
  recoveryOwnerId String? @map("recovery_owner_id") @db.Uuid
  recoveryLeaseUntil DateTime? @map("recovery_lease_until")
  remoteTemplateId String? @map("remote_template_id") @db.VarChar(128)
  acknowledgedRemoteTemplateId String? @map("acknowledged_remote_template_id") @db.VarChar(128)
  safeCode String? @map("safe_code") @db.VarChar(64)
  providerStatus String? @map("provider_status") @db.VarChar(32)
  acceptanceProvenance MessageTemplateAcceptanceProvenance? @map("acceptance_provenance")
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  receipts MessageTemplateSubmissionReceipt[]
  reservation MessageTemplateNameReservation?
  quotaEvents MessageTemplateQuotaEvent[]

  @@unique([buId, actorUserId, idempotencyKey], map: "mt_ops_bu_actor_key_uq")
  @@unique([draftId, revision], map: "mt_ops_draft_revision_uq")
  @@index([buId, actorUserId, createdAt, id], map: "mt_ops_bu_actor_created_idx")
  @@index([accountReference, phase, leaseUntil], map: "mt_ops_account_phase_lease_idx")
  @@index([phase, recoveryLeaseUntil], map: "mt_ops_recovery_lease_idx")
  @@map("message_template_operations")
}

/// Append-only evidence; APIs project the latest ten without deleting history.
model MessageTemplateSubmissionReceipt {
  id String @id @default(uuid())
  operationId String @map("operation_id")
  operation MessageTemplateOperation @relation(fields: [operationId], references: [id], onDelete: Restrict, map: "mt_receipt_operation_fkey")
  sequence Int
  phase MessageTemplateOperationPhase
  safeCode String? @map("safe_code") @db.VarChar(64)
  remoteTemplateId String? @map("remote_template_id") @db.VarChar(128)
  acceptanceProvenance MessageTemplateAcceptanceProvenance? @map("acceptance_provenance")
  createdAt DateTime @default(now()) @map("created_at")

  @@unique([operationId, sequence], map: "mt_receipt_op_sequence_uq")
  @@index([operationId, createdAt, id], map: "mt_receipt_op_created_idx")
  @@map("message_template_submission_receipts")
}

/// Global account/name lock contains no tenant payload or user-visible ids.
model MessageTemplateNameReservation {
  id String @id @default(uuid())
  accountReference String @map("account_reference") @db.VarChar(128)
  name String @db.VarChar(128)
  language String @db.VarChar(35)
  operationId String @unique(map: "mt_res_operation_uq") @map("operation_id")
  operation MessageTemplateOperation @relation(fields: [operationId], references: [id], onDelete: Restrict, map: "mt_reservation_operation_fkey")
  createdAt DateTime @default(now()) @map("created_at")

  @@unique([accountReference, name, language], map: "mt_res_account_name_lang_uq")
  @@index([accountReference, createdAt], map: "mt_res_account_created_idx")
  @@map("message_template_name_reservations")
}

/// Durable events counted under per-scope advisory locks for exact sliding windows.
model MessageTemplateQuotaEvent {
  id String @id @default(uuid())
  kind String @db.VarChar(16)
  scopeKey String @map("scope_key") @db.VarChar(128)
  operationId String? @map("operation_id")
  operation MessageTemplateOperation? @relation(fields: [operationId], references: [id], onDelete: Restrict, map: "mt_quota_operation_fkey")
  occurredAt DateTime @default(now()) @map("occurred_at")

  @@unique([kind, operationId], map: "mt_quota_kind_operation_uq")
  @@index([kind, scopeKey, occurredAt], map: "mt_quota_scope_time_idx")
  @@map("message_template_quota_events")
}

/// One lease/fence shared by individual refresh and each explicit catalogue page.
model MessageTemplateObservationLease {
  contextKey String @id @map("context_key") @db.Char(64)
  mantenedoraId String @map("mantenedora_id")
  buId String @map("bu_id")
  bu BusinessUnit @relation(fields: [buId, mantenedoraId], references: [id, mantenedoraId], onDelete: Restrict, map: "mt_lease_bu_fkey")
  channelId String @map("channel_id")
  accountReference String @map("account_reference") @db.VarChar(128)
  channelGeneration Int @map("channel_generation")
  pairingEpoch Int @map("pairing_epoch")
  providerResourceIdentityId String @map("provider_resource_identity_id")
  activeCredentialVersion Int @map("active_credential_version")
  ownerId String? @map("owner_id") @db.Uuid
  fence BigInt @default(0)
  leaseUntil DateTime? @map("lease_until")
  lastStartedAt DateTime? @map("last_started_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  observations MessageTemplateRemoteObservation[]
  pages MessageTemplateCatalogPage[]

  @@index([accountReference, leaseUntil], map: "mt_lease_account_expiry_idx")
  @@map("message_template_observation_leases")
}

/// The single semantic observation projector for both draft and catalog views.
model MessageTemplateRemoteObservation {
  id String @id @default(uuid())
  contextKey String @map("context_key") @db.Char(64)
  lease MessageTemplateObservationLease @relation(fields: [contextKey], references: [contextKey], onDelete: Restrict, map: "mt_observation_lease_fkey")
  remoteTemplateId String @map("remote_template_id") @db.VarChar(128)
  status String @db.VarChar(32)
  name String? @db.VarChar(128)
  language String? @db.VarChar(35)
  category String @db.VarChar(32)
  parameterFormat String @map("parameter_format") @db.VarChar(16)
  components Json
  semanticFingerprint String? @map("semantic_fingerprint") @db.Char(64)
  supported Boolean @default(false)
  available Boolean @default(true)
  safeCode String? @map("safe_code") @db.VarChar(64)
  observedEligible Boolean @default(false) @map("observed_eligible")
  observedAt DateTime @map("observed_at")
  observedFence BigInt @map("observed_fence")
  updatedAt DateTime @updatedAt @map("updated_at")

  @@unique([contextKey, remoteTemplateId], map: "mt_observation_context_remote_uq")
  @@index([contextKey, status, observedAt], map: "mt_observation_status_time_idx")
  @@map("message_template_remote_observations")
}

/// Cached explicit catalogue pages; GET never fans out to the provider.
model MessageTemplateCatalogPage {
  id String @id @default(uuid())
  contextKey String @map("context_key") @db.Char(64)
  lease MessageTemplateObservationLease @relation(fields: [contextKey], references: [contextKey], onDelete: Restrict, map: "mt_page_lease_fkey")
  cursorHash String @map("cursor_hash") @db.Char(64)
  requestedCursor String? @map("requested_cursor") @db.VarChar(512)
  remoteTemplateIds Json @map("remote_template_ids")
  nextCursor String? @map("next_cursor") @db.VarChar(512)
  available Boolean @default(true)
  safeCode String? @map("safe_code") @db.VarChar(64)
  observedAt DateTime @map("observed_at")
  observedFence BigInt @map("observed_fence")

  @@unique([contextKey, cursorHash], map: "mt_page_context_cursor_uq")
  @@index([contextKey, observedAt], map: "mt_page_context_time_idx")
  @@map("message_template_catalog_pages")
}

```


---
## web-app/src/telas/Inbox.tsx
SHA256 d70bde9ede67759d479f644598356e46aac2916a12b2ed1770c17a169118586c

```
import { FormEvent, useCallback, useEffect, useRef, useState } from 'react';
import { BusinessUnit, Conversa, ErroDaApi, Eu, Mensagem, Thread, api, ignorarSessaoMorta } from '../api';
import { ouvirTempoReal } from '../tempoReal';
import { cruzouPiso, mesclarMensagens } from '../timeline';

const ABAS = [
  { id: 'QUEUED', rotulo: 'Na fila' },
  { id: 'IN_SERVICE', rotulo: 'Em atendimento' },
  { id: 'CLOSED', rotulo: 'Finalizadas' },
  { id: 'GRUPO', rotulo: 'Grupos' },
];

function explicarMotivoEnvio(motivo: string | null): string {
  switch (motivo) {
    case 'CANAL_AUSENTE': return 'Não há um canal conectado para responder.';
    case 'CANAL_AMBIGUO': return 'Esta conversa ainda não tem um canal definido. Aguarde uma mensagem recebida para responder.';
    case 'CANAL_SELECIONADO_INDISPONIVEL': return 'O canal desta conversa não está disponível.';
    case 'CHANNEL_IDENTITY_NOT_VERIFIED': return 'A identidade do canal ainda precisa ser verificada.';
    case 'CHANNEL_NOT_READY': return 'O canal ainda não está pronto para enviar.';
    case 'PENDING_CREDENTIAL': return 'A credencial do canal precisa ser atualizada.';
    case 'JANELA_FECHADA': return 'A janela de 24 horas foi encerrada.';
    default: return 'O envio está temporariamente indisponível.';
  }
}

interface Recuperacao {
  id: string;
  geracao: number;
  piso: string;
  cursor: string | null;
  dirty: boolean;
  eventos: number;
  emVoo: boolean;
  paginasRestantes: number;
  vazio?: boolean;
}

interface InvalidacaoDeAbertura {
  id: string;
  geracao: number;
  eventos: number;
}

interface ErroDeRecuperacao {
  geracao: number;
  versao: number;
}

export default function Inbox({ eu }: { eu: Eu }) {
  const [bus, setBus] = useState<BusinessUnit[]>([]);
  const [buId, setBuId] = useState<string>('');
  const [aba, setAba] = useState('QUEUED');
  const [conversas, setConversas] = useState<Conversa[]>([]);
  const [aberta, setAberta] = useState<Thread | null>(null);
  const [abrindo, setAbrindo] = useState(false);
  const [texto, setTexto] = useState('');
  const [erro, setErro] = useState<string | null>(null);
  const [carregandoAnteriores, setCarregandoAnteriores] = useState(false);
  const [recuperacaoPendente, setRecuperacaoPendente] = useState(false);
  const [enviando, setEnviando] = useState(false);
  const textoRef = useRef('');
  const versaoErro = useRef(0);
  const erroRecuperacao = useRef<ErroDeRecuperacao | null>(null);
  const geracao = useRef(0);
  const buAtual = useRef('');
  const conversaAtual = useRef<string | null>(null);
  const abaAtual = useRef('QUEUED');
  const threadAtual = useRef<Thread | null>(null);
  const recuperacao = useRef<Recuperacao | null>(null);
  const invalidacaoAbertura = useRef<InvalidacaoDeAbertura | null>(null);
  const executarRecuperacaoRef = useRef<() => Promise<void>>(async () => {});
  const versaoMetadados = useRef(0);
  const bolhas = useRef<HTMLDivElement>(null);
  const carregarListaRef = useRef<(id?: string, filtro?: string) => Promise<void>>(async () => {});
  const reconciliarRef = useRef<() => void>(() => {});

  const guardarThread = (thread: Thread | null) => {
    threadAtual.current = thread;
    setAberta(thread);
  };

  const guardarTexto = (valor: string) => {
    textoRef.current = valor;
    setTexto(valor);
  };

  const definirErro = useCallback((mensagem: string | null, geracaoDaRecuperacao?: number) => {
    versaoErro.current += 1;
    erroRecuperacao.current = mensagem !== null && geracaoDaRecuperacao !== undefined
      ? { geracao: geracaoDaRecuperacao, versao: versaoErro.current }
      : null;
    setErro(mensagem);
  }, []);

  const limparErroRecuperacao = useCallback((geracaoDaRecuperacao: number) => {
    const erroAtual = erroRecuperacao.current;
    if (erroAtual?.geracao !== geracaoDaRecuperacao || erroAtual.versao !== versaoErro.current) return;
    erroRecuperacao.current = null;
    versaoErro.current += 1;
    setErro(null);
  }, []);

  useEffect(() => {
    api.get<{ businessUnits: BusinessUnit[] }>('/business-units').then((r) => {
      const lista = r.businessUnits ?? [];
      setBus(lista);
      const inicial = lista[0]?.id ?? '';
      buAtual.current = inicial;
      setBuId(inicial);
    }).catch(ignorarSessaoMorta);
  }, []);

  const carregarLista = useCallback(async (id = buAtual.current, filtro = aba) => {
    if (!id) return;
    try {
      const r = await api.get<{ conversations: Conversa[] }>(`/business-units/${id}/conversations?aba=${filtro}`);
      if (buAtual.current === id && abaAtual.current === filtro) setConversas(r.conversations);
    } catch (e) {
      if (buAtual.current === id && abaAtual.current === filtro) throw e;
    }
  }, [aba]);

  const aplicarPaginaRecente = useCallback((id: string, geracaoDaChamada: number, versao: number, response: Thread) => {
    if (conversaAtual.current !== id || geracao.current !== geracaoDaChamada) return;
    const anterior = threadAtual.current;
    const novo: Thread = {
      ...response,
      messages: mesclarMensagens(anterior?.messages ?? [], response.messages),
      // O cursor de reconciliação recente não substitui o cursor do histórico.
      paginacao: anterior && anterior.messages.length > 0 ? anterior.paginacao : response.paginacao,
      conversa: versaoMetadados.current === versao ? response.conversa : anterior?.conversa ?? response.conversa,
      janela: versaoMetadados.current === versao ? response.janela : anterior?.janela ?? response.janela,
    };
    guardarThread(novo);
  }, []);

  const executarRecuperacao = useCallback(async () => {
    const r = recuperacao.current;
    if (!r || r.emVoo || r.paginasRestantes <= 0 || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
    r.emVoo = true;
    const eventosNoInicio = r.eventos;
    r.dirty = false;
    let cruzou = false;
    try {
      if (r.vazio) {
        if (r.cursor === null && r.paginasRestantes > 0) {
          const versao = versaoMetadados.current;
          r.paginasRestantes -= 1;
          const inicial = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          aplicarPaginaRecente(r.id, r.geracao, versao, inicial);
          r.cursor = inicial.paginacao.cursorAnterior;
          if (!inicial.paginacao.temAnteriores) r.cursor = null;
        }
        while (r.cursor && r.paginasRestantes > 0 && !r.dirty) {
          const cursor = r.cursor;
          r.paginasRestantes -= 1;
          const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          const atual = threadAtual.current;
          if (atual) guardarThread({
            ...atual,
            messages: mesclarMensagens(atual.messages, pagina.messages),
            paginacao: pagina.paginacao,
          });
          r.cursor = pagina.paginacao.cursorAnterior;
        }
        if (r.eventos !== eventosNoInicio || r.dirty) {
          r.cursor = null;
          setRecuperacaoPendente(true);
        } else if (!r.cursor) {
          recuperacao.current = null;
          setRecuperacaoPendente(false);
          limparErroRecuperacao(r.geracao);
        } else {
          setRecuperacaoPendente(true);
        }
        return;
      }
      if (r.cursor === null && r.paginasRestantes > 0) {
        const versao = versaoMetadados.current;
        r.paginasRestantes -= 1;
        const recente = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        aplicarPaginaRecente(r.id, r.geracao, versao, recente);
        r.cursor = recente.paginacao.cursorAnterior;
        cruzou = cruzouPiso(recente.messages, r.piso) || !recente.paginacao.temAnteriores;
      }
      while (!cruzou && r.cursor && r.paginasRestantes > 0 && !r.dirty) {
        const cursor = r.cursor;
        r.paginasRestantes -= 1;
        const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        const atual = threadAtual.current;
        if (atual) guardarThread({
          ...atual,
          messages: mesclarMensagens(atual.messages, pagina.messages),
        });
        r.cursor = pagina.paginacao.cursorAnterior;
        cruzou = cruzouPiso(pagina.messages, r.piso) || !pagina.paginacao.temAnteriores;
      }

      if (r.eventos !== eventosNoInicio || r.dirty) {
        // Um evento concorrente exige nova passagem recente e preserva o piso.
        r.cursor = null;
        setRecuperacaoPendente(true);
      } else if (cruzou) {
        recuperacao.current = null;
        setRecuperacaoPendente(false);
        limparErroRecuperacao(r.geracao);
      } else {
        setRecuperacaoPendente(true);
      }
    } catch (e) {
      if (r.geracao === geracao.current && r.id === conversaAtual.current) {
        if (r.dirty || r.eventos !== eventosNoInicio) r.cursor = null;
        definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível atualizar o histórico. Tente novamente.', r.geracao);
        setRecuperacaoPendente(true);
      }
    } finally {
      r.emVoo = false;
      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.paginasRestantes > 0 && r.geracao === geracao.current) {
        queueMicrotask(() => void executarRecuperacaoRef.current());
      }
    }
  }, [aplicarPaginaRecente, definirErro, limparErroRecuperacao]);

  useEffect(() => { executarRecuperacaoRef.current = executarRecuperacao; }, [executarRecuperacao]);

  const reconciliar = useCallback(() => {
    const thread = threadAtual.current;
    const id = conversaAtual.current;
    if (!id) return;
    if (!thread) {
      const abertura = invalidacaoAbertura.current;
      if (abertura?.id === id && abertura.geracao === geracao.current) abertura.eventos += 1;
      return;
    }
    let r = recuperacao.current;
    if (!r || r.id !== id || r.geracao !== geracao.current) {
      const mensagens = thread.messages;
      if (mensagens.length === 0) {
        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3, vazio: true };
        recuperacao.current = r;
        void executarRecuperacao();
        return;
      }
      const piso = mensagens.reduce((max, m) => Date.parse(m.createdAt) > Date.parse(max) ? m.createdAt : max, mensagens[0].createdAt);
      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3 };
      recuperacao.current = r;
      setRecuperacaoPendente(true);
    } else {
      r.dirty = true;
      r.eventos += 1;
      if (!r.emVoo) r.cursor = null;
      setRecuperacaoPendente(true);
    }
    if (r.paginasRestantes > 0) void executarRecuperacao();
  }, [aplicarPaginaRecente, executarRecuperacao]);

  const iniciarRodadaAutorizada = useCallback(() => {
    const r = recuperacao.current;
    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
    r.paginasRestantes = 3;
    void executarRecuperacao();
  }, [executarRecuperacao]);

  useEffect(() => {
    carregarListaRef.current = carregarLista;
    reconciliarRef.current = reconciliar;
  }, [carregarLista, reconciliar]);

  useEffect(() => {
    void carregarLista().catch(ignorarSessaoMorta);
    const t = setInterval(() => {
      void carregarLista().catch(ignorarSessaoMorta);
      if (recuperacao.current) iniciarRodadaAutorizada();
      else reconciliar();
    }, 60_000);
    return () => clearInterval(t);
  }, [buId, aba, carregarLista, reconciliar, iniciarRodadaAutorizada]);

  useEffect(() => {
    // Espera a lista inicial de BUs e mantém o socket apesar de filtros, BUs ou
    // callbacks locais mudarem. Isso evita reconectar durante o mesmo login.
    if (bus.length === 0) return;
    const parar = ouvirTempoReal((evento) => {
      if (evento.buId !== buAtual.current) return;
      void carregarListaRef.current().catch(ignorarSessaoMorta);
      if (evento.conversaId === conversaAtual.current) reconciliarRef.current();
    }, () => reconciliarRef.current());
    return parar;
  }, [eu.id, bus.length]);

  function trocarBu(novoBu: string) {
    geracao.current += 1;
    buAtual.current = novoBu;
    conversaAtual.current = null;
    recuperacao.current = null;
    invalidacaoAbertura.current = null;
    guardarThread(null);
    setAbrindo(false);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    definirErro(null);
    setRecuperacaoPendente(false);
    setConversas([]);
    setBuId(novoBu);
  }

  async function abrir(id: string) {
    const gen = ++geracao.current;
    conversaAtual.current = id;
    recuperacao.current = null;
    invalidacaoAbertura.current = { id, geracao: gen, eventos: 0 };
    versaoMetadados.current += 1;
    guardarThread(null);
    setAbrindo(true);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    definirErro(null);
    setRecuperacaoPendente(false);
    try {
      const response = await api.get<Thread>(`/conversations/${id}/messages`);
      if (gen !== geracao.current || conversaAtual.current !== id) return;
      response.messages = mesclarMensagens(response.messages);
      guardarThread(response);
      setAbrindo(false);
      const invalidacao = invalidacaoAbertura.current;
      invalidacaoAbertura.current = null;
      void carregarLista().catch(ignorarSessaoMorta);
      if (invalidacao?.id === id && invalidacao.geracao === gen && invalidacao.eventos > 0) reconciliar();
    } catch (e) {
      if (gen === geracao.current) {
        invalidacaoAbertura.current = null;
        guardarThread(null);
        setAbrindo(false);
        definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível carregar a conversa.');
      }
    }
  }

  async function carregarAnteriores() {
    const atual = threadAtual.current;
    const id = conversaAtual.current;
    const cursor = atual?.paginacao.cursorAnterior;
    if (!atual || !id || !cursor || carregandoAnteriores) return;
    const gen = geracao.current;
    setCarregandoAnteriores(true);
    definirErro(null);
    try {
      const pagina = await api.get<Thread>(`/conversations/${id}/messages?antes=${encodeURIComponent(cursor)}`);
      if (gen !== geracao.current || id !== conversaAtual.current || !threadAtual.current) return;
      // Inclua alterações legítimas que chegaram enquanto a página estava no ar.
      const alturaAntes = bolhas.current?.scrollHeight ?? 0;
      const topoAntes = bolhas.current?.scrollTop ?? 0;
      const corrente = threadAtual.current;
      guardarThread({ ...corrente, messages: mesclarMensagens(corrente.messages, pagina.messages), paginacao: pagina.paginacao });
      requestAnimationFrame(() => {
        if (gen === geracao.current && bolhas.current) bolhas.current.scrollTop = topoAntes + (bolhas.current.scrollHeight - alturaAntes);
      });
    } catch (e) {
      if (gen === geracao.current) definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Falha ao carregar mensagens anteriores.');
    } finally {
      if (gen === geracao.current) setCarregandoAnteriores(false);
    }
  }

  async function agir(acao: () => Promise<unknown>) {
    const id = conversaAtual.current;
    const gen = geracao.current;
    if (!id) return;
    versaoMetadados.current += 1;
    definirErro(null);
    try {
      await acao();
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) definirErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
    }
  }

  async function responder(e: FormEvent) {
    e.preventDefault();
    const id = conversaAtual.current;
    const gen = geracao.current;
    const textoEnviado = textoRef.current;
    if (!id || !textoEnviado.trim() || enviando) return;
    setEnviando(true);
    definirErro(null);
    try {
      await api.post(`/conversations/${id}/messages`, { texto: textoEnviado });
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      if (textoRef.current === textoEnviado) guardarTexto('');
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) definirErro(e instanceof ErroDaApi ? e.message : 'Falha ao enviar mensagem.');
    } finally {
      if (gen === geracao.current) setEnviando(false);
    }
  }

  const envioIndisponivel = aberta ? !aberta.janela.disponivel : false;
  const janelaFechada = aberta?.janela.exigida && !aberta.janela.aberta;

  return (
    <div className="grade">
      <div className="linha">
        <select aria-label="Business Unit" value={buId} onChange={(e) => trocarBu(e.target.value)} style={{ maxWidth: 280 }}>
          {bus.map((b) => <option key={b.id} value={b.id}>{b.name}</option>)}
        </select>
        {erro && <span className="erro" role="alert">{erro}</span>}
      </div>

      <div className="abas">
        {ABAS.map((a) => <button key={a.id} className={aba === a.id ? 'ativa' : ''} onClick={() => { abaAtual.current = a.id; setAba(a.id); }}>{a.rotulo}</button>)}
      </div>

      <div className="inbox">
        <div className="cartao lista" style={{ padding: 0 }}>
          {conversas.map((c) => <button key={c.id} className={`item ${aberta?.conversa.id === c.id ? 'ativo' : ''}`} onClick={() => void abrir(c.id)}>
            <div className="linha"><strong>{c.displayName ?? c.contact}</strong>{c.unreadCount > 0 && <span className="suave">({c.unreadCount})</span>}</div>
            <div className="suave">{c.attendantName ?? 'sem atendente'}</div>
          </button>)}
          {conversas.length === 0 && <p className="suave" style={{ padding: 12 }}>Nada aqui.</p>}
        </div>

        <div className="cartao grade">
          {!aberta && (abrindo
            ? <p className="suave" role="status" aria-live="polite">Abrindo conversa…</p>
            : <p className="suave">Escolha uma conversa.</p>)}
          {aberta && <>
            <div className="linha">
              <strong>{aberta.conversa.nome ?? aberta.conversa.contato}</strong>
              <span className="suave">{aberta.conversa.status}</span>
              <span className="suave" style={{ marginLeft: 'auto' }}>{aberta.janela.canal}</span>
            </div>
            <div className="linha">
              {aberta.paginacao.temAnteriores
                ? <button onClick={() => void carregarAnteriores()} disabled={carregandoAnteriores} aria-label="Carregar mensagens anteriores">
                    {carregandoAnteriores ? 'Carregando…' : 'Carregar anteriores'}
                  </button>
                : <span className="suave">Início do histórico</span>}
              {recuperacaoPendente && <span className="suave" role="status">Atualização pendente. O histórico pode ter uma lacuna.</span>}
              {recuperacaoPendente && <button onClick={() => iniciarRodadaAutorizada()}>Continuar atualização</button>}
            </div>
            <div className="bolhas" ref={bolhas} aria-live="polite">
              {aberta.messages.map((m: Mensagem) => <div key={m.id} data-message-id={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>
                <div>{m.content}</div>
                <div className="suave">{new Date(m.createdAt).toLocaleString('pt-BR')}{m.authorName ? ` · ${m.authorName}` : ''}</div>
              </div>)}
              {aberta.messages.length === 0 && <p className="suave">Nenhuma mensagem nesta conversa.</p>}
            </div>

            {envioIndisponivel && <div className="aviso" role="status">{janelaFechada
              ? 'Fora da janela de 24h do canal selecionado. Texto livre está indisponível.'
              : explicarMotivoEnvio(aberta.janela.motivo)}</div>}
            <form className="linha" onSubmit={responder}>
              <input value={texto} onChange={(e) => guardarTexto(e.target.value)} placeholder={envioIndisponivel ? 'Envio indisponível' : 'Escreva uma resposta'} disabled={envioIndisponivel} maxLength={4096} />
              <button className="primario" disabled={envioIndisponivel || enviando || !texto.trim()}>{enviando ? 'Enviando…' : 'Enviar'}</button>
            </form>
            {aberta.conversa.status !== 'CLOSED' && <div className="linha">
              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/claim`))}>Atender</button>
              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/close`))}>Finalizar</button>
            </div>}
          </>}
        </div>
      </div>
    </div>
  );
}

```


---
## web-app/src/api.ts
SHA256 177d660cccb7d74e47ef1dd180d9e74f830bce97b631c896c4e82fa39ae44a84

```
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
    readonly outcome?: string,
    readonly evidence?: string,
    readonly localMessageState?: string,
    readonly diagnosticPersistence?: string,
    readonly operationId?: string,
    readonly phase?: string,
    readonly providerAcceptance?: string,
    readonly receiptPersistence?: string,
    readonly acceptanceProvenance?: string,
    readonly recoveryAction?: string,
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
  let corpo: Record<string, unknown>;
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
      typeof corpo.code === 'string' ? corpo.code : undefined,
      dito ? `${dito} (HTTP ${res.status})` : `A API respondeu ${res.status} sem explicar o motivo.`,
      typeof corpo.outcome === 'string' ? corpo.outcome : undefined,
      typeof corpo.evidence === 'string' ? corpo.evidence : undefined,
      typeof corpo.localMessageState === 'string' ? corpo.localMessageState : undefined,
      typeof corpo.diagnosticPersistence === 'string' ? corpo.diagnosticPersistence : undefined,
      typeof corpo.operationId === 'string' ? corpo.operationId : undefined,
      typeof corpo.phase === 'string' ? corpo.phase : undefined,
      typeof corpo.providerAcceptance === 'string' ? corpo.providerAcceptance : undefined,
      typeof corpo.receiptPersistence === 'string' ? corpo.receiptPersistence : undefined,
      typeof corpo.acceptanceProvenance === 'string' ? corpo.acceptanceProvenance : undefined,
      typeof corpo.recoveryAction === 'string' ? corpo.recoveryAction : undefined,
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

export interface TemplateDefinition {
  name: string;
  language: 'pt_BR';
  category: 'MARKETING' | 'UTILITY';
  body: string;
  header?: string;
  footer?: string;
  examples: Record<string, string>;
}

export interface TemplateReceipt {
  id: string;
  sequence: number;
  phase: string;
  safeCode: string | null;
  remoteTemplateId: string | null;
  acceptanceProvenance?: string | null;
  createdAt: string;
}

export interface TemplateOperation {
  id: string;
  phase: string;
  revision: number;
  providerAcceptance: 'CONFIRMED' | 'UNKNOWN';
  acceptanceProvenance?: 'ACKNOWLEDGED' | 'CORRELATED_BY_DEFINITION' | null;
  receiptPersistence: 'RECORDED' | 'UNCONFIRMED';
  safeCode?: string | null;
  remoteTemplateId: string | null;
  updatedAt: string;
  leaseExpiresAt: string | null;
  recoveryAction: 'WAIT' | 'RECONCILE' | null;
  savedObservation?: TemplateSummary | null;
  receipts?: TemplateReceipt[];
}

export interface TemplateDraft {
  id: string;
  mantenedoraId: string;
  buId: string;
  creatorUserId: string;
  channelId: string;
  revision: number;
  state: 'DRAFT' | 'LOCKED';
  definition: TemplateDefinition;
  definitionFingerprint?: string;
  savedObservation?: TemplateSummary | null;
  currentOperation?: TemplateOperation | null;
  recentOperations?: TemplateOperation[];
}

export interface TemplatePreview {
  definition: TemplateDefinition;
  renderedText: string;
  requestFingerprint: string;
  persistence: 'PERSISTED' | 'UNPERSISTED';
}

export interface TemplateSummary {
  remoteTemplateId: string;
  status: string;
  name: string | null;
  language: string | null;
  category: string;
  parameterFormat: string;
  components: unknown[];
  supported: boolean;
  semanticFingerprint: string | null;
  available: boolean;
  safeCode?: string;
  observedAt: string;
  observedFence: string;
  eligible: boolean;
  matchesDefinition?: boolean;
  eligibleForUse?: boolean;
}

export interface TemplateCatalogPage {
  items: TemplateSummary[];
  nextCursor: string | null;
  available: boolean;
  safeCode?: string;
  observedAt: string | null;
}
export interface TemplateRefreshInProgress { phase: 'REFRESH_IN_PROGRESS'; retryAfter: number }

export interface TemplateCapabilities {
  available: boolean;
  expectedGeneration: number;
  explanation: string | null;
}

export const templateApi = {
  capabilities: (buId: string, channelId: string) =>
    api.get<TemplateCapabilities>(`/business-units/${buId}/channels/${channelId}/message-template-capabilities`),
  listDrafts: (buId: string, view: 'mine' | 'bu' = 'mine', page = 1, limit = 20) =>
    api.get<{ items: TemplateDraft[]; page: number; limit: number; total: number; hasMore: boolean }>(
      `/business-units/${buId}/message-templates?view=${view}&page=${page}&limit=${limit}`),
  preview: (buId: string, input: { channelId: string; expectedGeneration: number; draftId?: string; expectedRevision?: number; definition: TemplateDefinition }) =>
    api.post<TemplatePreview>(`/business-units/${buId}/message-templates/preview`, input),
  createDraft: (buId: string, input: { clientRequestId: string; channelId: string; expectedGeneration: number } & TemplateDefinition) =>
    api.post<TemplateDraft & { replayed?: boolean }>(`/business-units/${buId}/message-templates`, input),
  getDraft: (draftId: string) => api.get<TemplateDraft>(`/message-templates/${draftId}`),
  saveDraft: (draftId: string, expectedRevision: number, definition: TemplateDefinition) =>
    api.patch<TemplateDraft>(`/message-templates/${draftId}`, { expectedRevision, definition }),
  submit: (draftId: string, idempotencyKey: string, input: { expectedRevision: number; expectedGeneration: number; expectedDefinitionFingerprint: string }) =>
    api.postWithHeaders<TemplateOperation & { replayed?: boolean; recoveryInProgress?: boolean }>(
      `/message-templates/${draftId}/submit`, input, { 'idempotency-key': idempotencyKey }),
  operation: (draftId: string, operationId: string) =>
    api.get<TemplateOperation>(`/message-templates/${draftId}/operations/${operationId}`),
  reconcile: (draftId: string, operationId: string) =>
    api.post<TemplateOperation & { recoveryInProgress?: boolean }>(`/message-templates/${draftId}/operations/${operationId}/reconcile`, {}),
  refreshDraft: (draftId: string) => api.post<(TemplateSummary & { matchesDefinition?: boolean; eligibleForUse?: boolean }) | TemplateRefreshInProgress>(`/message-templates/${draftId}/refresh`, {}),
  catalog: (buId: string, channelId: string, after: string | null = null) =>
    api.get<TemplateCatalogPage>(`/business-units/${buId}/channels/${channelId}/message-template-catalog${after ? `?after=${encodeURIComponent(after)}` : ''}`),
  refreshCatalog: (buId: string, channelId: string, after: string | null = null) =>
    api.post<TemplateCatalogPage | TemplateRefreshInProgress>(`/business-units/${buId}/channels/${channelId}/message-template-catalog`, after ? { after } : {}),
};

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
  janela: { exigida: boolean; aberta: boolean; expiraEm: string | null; canal: string | null; disponivel: boolean; motivo: string | null };
  messages: Mensagem[];
  paginacao: { limite: number; temAnteriores: boolean; cursorAnterior: string | null };
}

```


---
## Prior current review / resolution architecture-r1-resolution.md

```
# ST-CON-04 v1.1 — architecture r1 resolution

Fresh internal no-context opinion recommended C and requested four changes before approval. All four are integrated into the proposed TODO, not production source.

## Planning Finding Resolution Ledger

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-R1-01 / F-E3C20901 | Integrated | useful | partial | project | n/a | Normative r1 owner-token interlock, explicit ordinary compatibility, no uncertain expiry takeover, local-only risk recovery and complete barriers; Scope09/DoD08/Val02 updated. |
| ARCH-R1-02 / F-2D3CB947 | Integrated | useful | yes | project | n/a | Same acceptance owner explicitly admitted/sealed; original CAS before self-mutation; identity/conversation lock order; whole-local-tx rollback/readback/one re-entry; Scope07/DoD06/Val02. |
| ARCH-R1-03 / F-0715A55A | Integrated | useful | yes | project | n/a | Explicit initial resolver, exact management/transport full context equality, parameter/semantic descriptor, applicable text-window check at final fence; DoD09/Val03. |
| ARCH-R1-04 / F-E2F76277 | Integrated | useful | yes | project | n/a | Initial renderer over unchanged existing catalog components; separate initial semantic fingerprint and POSITIONAL ordering; no authoring/parser/projector flag change; DoD09/Val03. |

These dispositions amend proposed contract only. Fresh no-context critique must assess them after refreshed freeze. They do not assert production fixes or grant execution authority.


See normative architecture r1 section in the governing TODO for exact state, transaction, resolver and template-consumption contracts. Original raw/strict merge remain immutable. Next: publish refreshed freeze and obtain fresh independent critique.

```


---
## Prior current review / resolution evidence/architecture-r1.raw-attempt1.txt

```
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/architecture-r1.dispatch.json",
  "review_kind": "architecture_opinion",
  "reviewer_label": "fresh-internal-architecture-r1",
  "overall_assessment": "Request changes before APROVADO. Option C is the strongest architectural direction, but ordinary-dispatch admission expiry, transactional finalization ordering, explicit initial-channel resolution, and POSITIONAL consumption need concrete resolution. Performance is mixed: bounded preflight and shared admission add latency and database work; improvement is unmeasured. Elegance and structural soundness improve relative to duplicate send operations or owners, subject to the findings below. The planned validation and private operational boundary are appropriate; actual asset and runtime readiness remain legitimate future dependencies. This review grants no execution authority.",
  "recommended_path": "Choose C: one discriminated Channel.sendMessage, declared supportedKinds, an explicit initial-selection resolver contract, one per-attempt dispatch fence, inbox orchestration composing management and transport, and transaction collaboration through the existing MessageAcceptanceService and common Outbound finalizer. A could preserve ownership but adds a second abstract operation without reducing provider I/O. B, as described, violates scoped resolution and common acceptance. C offers the smallest faithful ownership graph. Its main tradeoff is widening adapter/fake contracts and adding bounded preflight and admission costs to preserve safe external dispatch. Resolve these finite contracts before implementation; retain the existing catalogue owner, local-only initial recovery, and explicit external uncertainty.",
  "performance_position": "mixed",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "ARCH-R1-01",
      "severity": "high",
      "title": "Ordinary-dispatch admission has no safe expiry and takeover contract",
      "rationale": "The proposed interlock correctly rejects an early SELECT as sufficient, but still leaves conversation locking versus a dispatch lease unresolved. A bounded logical claim does not establish exclusion after expiry: an ordinary request may remain pending externally or resume before POST while an initial attempt reserves the conversation. A local lease cannot fence the provider. A single exclusive lease could also change ordinary-versus-ordinary behavior despite D-07 preserving callers without an initial slot. These are central correctness and operational questions, not global idempotency requirements.",
      "suggested_action": "Freeze one bounded admission design: ordinary sends receive owner-specific admission tokens under the same conversation transaction that reserves the exclusive initial slot; initial reservation conflicts with every outstanding ordinary token. Preserve ordinary-versus-ordinary behavior unless an explicit compatibility change is reviewed. Define pre-POST token validation, deadlines, owner-CAS release and commit certainty. Expiry may safely clear proven undispatched admissions; uncertain dispatched admissions must continue blocking initial reservation until settlement or an explicitly reviewed duplicate-risk release. Add barriers for both admission orderings, process suspension, timeout, expired tokens and late release. Keep database locks outside HTTP.",
      "category": "architecture",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "affected_paths": [
        "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
        "api-app/src/domain/inbox/outbound.service.ts",
        "api-app/src/domain/channels/transport/channel.ts",
        "api-app/prisma/schema.prisma"
      ]
    },
    {
      "finding_id": "ARCH-R1-02",
      "severity": "high",
      "title": "Acceptance mutates the token needed by the proposed finalization CAS",
      "rationale": "The packet proposes one local acceptance/finalization transaction but does not settle its ordering. Existing MessageAcceptanceService.loadOutboundConversation updates lastMessageAt and therefore Conversation.updatedAt before returning. Calling that primitive and then applying the prescribed pre-HTTP updatedAt CAS would invalidate the CAS through the initial flow's own write. Echo-first acceptance can also change that timestamp and must not justify refreshing the captured baseline. Additionally, the existing acceptance wrapper handles unique conflicts after transaction rollback; that recovery cannot simply be moved inside an already-aborted caller transaction. The strict path contract also admits the acceptance spec but omits message-acceptance.service.ts itself.",
      "suggested_action": "Freeze a short transaction sequence that evaluates the original conversation CAS while holding the row lock and before acceptance's own conversation mutation. Preserve concurrent claim/close outcomes without refreshing the expected timestamp. A failed status/owner CAS should skip those effects while permitting otherwise eligible keyed Message acceptance. Keep the known external receipt committed separately, then atomically record Message acceptance, attempt completion and slot release. Define bounded whole-local-transaction recovery for unique conflicts and commit-ACK loss, with no repeated provider call. Retain accept as the existing wrapper over the same owner primitive. Explicitly admit and baseline message-acceptance.service.ts before approval.",
      "category": "structural_soundness",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "affected_paths": [
        "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
        "api-app/src/domain/inbox/message-acceptance.service.ts",
        "api-app/src/domain/inbox/outbound.service.ts"
      ]
    },
    {
      "finding_id": "ARCH-R1-03",
      "severity": "medium",
      "title": "Explicit initial resolution and descriptor-to-fence binding remain unspecified",
      "rationale": "The delivered resolveForConversation selects conversational origin and enforces the text window before binding; OutboundService repeats that window check. Neither delivered resolver entry point represents a manually selected initial channel carrying an approved-template payload outside the window. Widening sendMessage alone therefore cannot provide the journey. The proposed immutable descriptor also lacks a concrete contract joining management validation to the exact transport resource, opaque account reference and credential version. The final fence's enumerated checks omit an explicit text-window recheck after potentially lengthy preflight.",
      "suggested_action": "Specify the narrow initial resolver reference and common dispatch input before freeze: explicit selected channel, expected immutable context, discriminated payload and required initial-attempt fence. Bind the selected channel without applying free-text policy to approved-template payloads. Require exact equality between validated management context and transport context, including opaque account reference, resource identity, generation, epoch and credential version. Bind template semantics and parameter values to that descriptor. Complete remote reads first, then validate current authorization, payload and applicable trusted text window in the claim transaction. Define preflight/fence failures as proven non-dispatch outcomes and test closed-window template success, text-window expiry during preflight and mismatched descriptor contexts.",
      "category": "architecture",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "affected_paths": [
        "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
        "api-app/src/domain/channels/transport/channel.ts",
        "api-app/src/domain/inbox/outbound.service.ts",
        "api-app/src/integrations/channels/prisma-channel-resolver.ts",
        "api-app/src/integrations/channels/meta-channel.ts"
      ]
    },
    {
      "finding_id": "ARCH-R1-04",
      "severity": "medium",
      "title": "POSITIONAL sending needs an explicit consumption contract for the inherited catalogue",
      "rationale": "SCOPE-06 promises NAMED and POSITIONAL sending while preserving the delivered catalogue/parser. The embedded parseTemplateSummary marks every POSITIONAL template unsupported and assigns a null semanticFingerprint; the shared projector consequently reports it ineligible. Its components and parameterFormat remain available, so preserving ST-CON-05 is feasible, but the packet does not specify how initial-send support and fingerprints differ from the inherited authoring-oriented flags. Reusing those flags would exclude the promised POSITIONAL path; ignoring them without a declared validator would weaken exact-definition checking.",
      "suggested_action": "Define initial-send eligibility and descriptor fingerprinting over the existing TemplateSummary components and parameterFormat, preserving ST-CON-05 catalogue DTOs and authoring flags. The bounded initial renderer should validate static header/footer, exact NAMED keys or contiguous POSITIONAL 1..N values, and exact supported semantics before producing its context-bound fingerprint. State explicitly that inherited supported/eligible flags do not authorize or fully describe initial-send support. Plan end-to-end POSITIONAL cases through catalogue selection, local preview, fresh same-account validation and raw send ordering. If shared parser changes prove necessary, admit and review those exact changes before approval.",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "affected_paths": [
        "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
        "api-app/src/integrations/meta/message-template.client.ts",
        "api-app/src/domain/message-templates/template-management.ports.ts",
        "api-app/src/domain/message-templates/template-observation.service.ts"
      ]
    }
  ]
}
```


---
## Prior current review / resolution evidence/architecture-r1.merge.json

```
{
  "schema_version": "subagent-review-merge-v2",
  "artifact_kind": "subagent_review_merge",
  "authoritative": false,
  "edit_policy": "derived_merge_packet",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/architecture-r1.dispatch.json",
  "review_kind": "architecture_opinion",
  "review_count": 1,
  "reviewer_labels": [
    "fresh-internal-architecture-r1"
  ],
  "highest_finding_severity": "high",
  "axis_summary": {
    "performance": "mixed",
    "elegance": "acceptable",
    "structural_soundness": "mixed",
    "operational_fit": "mixed"
  },
  "recommended_paths": [
    "Choose C: one discriminated Channel.sendMessage, declared supportedKinds, an explicit initial-selection resolver contract, one per-attempt dispatch fence, inbox orchestration composing management and transport, and transaction collaboration through the existing MessageAcceptanceService and common Outbound finalizer. A could preserve ownership but adds a second abstract operation without reducing provider I/O. B, as described, violates scoped resolution and common acceptance. C offers the smallest faithful ownership graph. Its main tradeoff is widening adapter/fake contracts and adding bounded preflight and admission costs to preserve safe external dispatch. Resolve these finite contracts before implementation; retain the existing catalogue owner, local-only initial recovery, and explicit external uncertainty."
  ],
  "exact_next_step": "Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.",
  "findings": [
    {
      "finding_id": "F-E3C20901",
      "severity": "high",
      "title": "Ordinary-dispatch admission has no safe expiry and takeover contract",
      "rationale": "The proposed interlock correctly rejects an early SELECT as sufficient, but still leaves conversation locking versus a dispatch lease unresolved. A bounded logical claim does not establish exclusion after expiry: an ordinary request may remain pending externally or resume before POST while an initial attempt reserves the conversation. A local lease cannot fence the provider. A single exclusive lease could also change ordinary-versus-ordinary behavior despite D-07 preserving callers without an initial slot. These are central correctness and operational questions, not global idempotency requirements.",
      "suggested_action": "Freeze one bounded admission design: ordinary sends receive owner-specific admission tokens under the same conversation transaction that reserves the exclusive initial slot; initial reservation conflicts with every outstanding ordinary token. Preserve ordinary-versus-ordinary behavior unless an explicit compatibility change is reviewed. Define pre-POST token validation, deadlines, owner-CAS release and commit certainty. Expiry may safely clear proven undispatched admissions; uncertain dispatched admissions must continue blocking initial reservation until settlement or an explicitly reviewed duplicate-risk release. Add barriers for both admission orderings, process suspension, timeout, expired tokens and late release. Keep database locks outside HTTP.",
      "reviewer_labels": [
        "fresh-internal-architecture-r1"
      ],
      "source_finding_ids": [
        "ARCH-R1-01"
      ],
      "category": "architecture",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "candidate_rule_id": "n/a"
    },
    {
      "finding_id": "F-2D3CB947",
      "severity": "high",
      "title": "Acceptance mutates the token needed by the proposed finalization CAS",
      "rationale": "The packet proposes one local acceptance/finalization transaction but does not settle its ordering. Existing MessageAcceptanceService.loadOutboundConversation updates lastMessageAt and therefore Conversation.updatedAt before returning. Calling that primitive and then applying the prescribed pre-HTTP updatedAt CAS would invalidate the CAS through the initial flow's own write. Echo-first acceptance can also change that timestamp and must not justify refreshing the captured baseline. Additionally, the existing acceptance wrapper handles unique conflicts after transaction rollback; that recovery cannot simply be moved inside an already-aborted caller transaction. The strict path contract also admits the acceptance spec but omits message-acceptance.service.ts itself.",
      "suggested_action": "Freeze a short transaction sequence that evaluates the original conversation CAS while holding the row lock and before acceptance's own conversation mutation. Preserve concurrent claim/close outcomes without refreshing the expected timestamp. A failed status/owner CAS should skip those effects while permitting otherwise eligible keyed Message acceptance. Keep the known external receipt committed separately, then atomically record Message acceptance, attempt completion and slot release. Define bounded whole-local-transaction recovery for unique conflicts and commit-ACK loss, with no repeated provider call. Retain accept as the existing wrapper over the same owner primitive. Explicitly admit and baseline message-acceptance.service.ts before approval.",
      "reviewer_labels": [
        "fresh-internal-architecture-r1"
      ],
      "source_finding_ids": [
        "ARCH-R1-02"
      ],
      "category": "structural_soundness",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "candidate_rule_id": "n/a"
    },
    {
      "finding_id": "F-E2F76277",
      "severity": "medium",
      "title": "POSITIONAL sending needs an explicit consumption contract for the inherited catalogue",
      "rationale": "SCOPE-06 promises NAMED and POSITIONAL sending while preserving the delivered catalogue/parser. The embedded parseTemplateSummary marks every POSITIONAL template unsupported and assigns a null semanticFingerprint; the shared projector consequently reports it ineligible. Its components and parameterFormat remain available, so preserving ST-CON-05 is feasible, but the packet does not specify how initial-send support and fingerprints differ from the inherited authoring-oriented flags. Reusing those flags would exclude the promised POSITIONAL path; ignoring them without a declared validator would weaken exact-definition checking.",
      "suggested_action": "Define initial-send eligibility and descriptor fingerprinting over the existing TemplateSummary components and parameterFormat, preserving ST-CON-05 catalogue DTOs and authoring flags. The bounded initial renderer should validate static header/footer, exact NAMED keys or contiguous POSITIONAL 1..N values, and exact supported semantics before producing its context-bound fingerprint. State explicitly that inherited supported/eligible flags do not authorize or fully describe initial-send support. Plan end-to-end POSITIONAL cases through catalogue selection, local preview, fresh same-account validation and raw send ordering. If shared parser changes prove necessary, admit and review those exact changes before approval.",
      "reviewer_labels": [
        "fresh-internal-architecture-r1"
      ],
      "source_finding_ids": [
        "ARCH-R1-04"
      ],
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "candidate_rule_id": "n/a"
    },
    {
      "finding_id": "F-0715A55A",
      "severity": "medium",
      "title": "Explicit initial resolution and descriptor-to-fence binding remain unspecified",
      "rationale": "The delivered resolveForConversation selects conversational origin and enforces the text window before binding; OutboundService repeats that window check. Neither delivered resolver entry point represents a manually selected initial channel carrying an approved-template payload outside the window. Widening sendMessage alone therefore cannot provide the journey. The proposed immutable descriptor also lacks a concrete contract joining management validation to the exact transport resource, opaque account reference and credential version. The final fence's enumerated checks omit an explicit text-window recheck after potentially lengthy preflight.",
      "suggested_action": "Specify the narrow initial resolver reference and common dispatch input before freeze: explicit selected channel, expected immutable context, discriminated payload and required initial-attempt fence. Bind the selected channel without applying free-text policy to approved-template payloads. Require exact equality between validated management context and transport context, including opaque account reference, resource identity, generation, epoch and credential version. Bind template semantics and parameter values to that descriptor. Complete remote reads first, then validate current authorization, payload and applicable trusted text window in the claim transaction. Define preflight/fence failures as proven non-dispatch outcomes and test closed-window template success, text-window expiry during preflight and mismatched descriptor contexts.",
      "reviewer_labels": [
        "fresh-internal-architecture-r1"
      ],
      "source_finding_ids": [
        "ARCH-R1-03"
      ],
      "category": "architecture",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "candidate_rule_id": "n/a"
    }
  ]
}

```


---
## Prior current review / resolution critique-r1-resolution.md

```
# ST-CON-04 v1.1 — critique r1 disposition

Four architecture corrections accepted at planning-contract level. Bounded critique findings are integrated as exact acknowledgment timing and inherited automation compatibility; source remains untouched.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CR-R1-01 | Integrated | useful | yes | project | n/a | Uniform immutable90s dispatchDeadlineAt predicate for AMBIGUOUS and EXTERNAL_ACCEPTED_LOCAL_BLOCKED; endpoint, Scope08/DoD06/Val02 and normative r2 appendix aligned; merged F-49CD0618. |
| CR-R1-02 | Integrated | useful | partial | project | n/a | Preserve actual NOVA_CONVERSA row-creation predicate and keyword behavior; no automation on manual open; Scope01/DoD01/Val01, consumer/flow and existing admitted Typebot test scope aligned; merged F-4ACC72C3. |

Uniform initial acknowledgment waits until original persisted90s deadline in both allowed states. No early confirmed-acceptance exception. Preserve NOVA_CONVERSA actual row-creation predicate, no automation on open, and keyword behavior. See normative TODO appendix and matching Scope/DoD/Val/consumer matrix. Fresh critique r2 assesses this bounded update before approval.

```


---
## Prior current review / resolution evidence/critique-r1.raw-attempt1.txt

```
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/critique-r1.dispatch.json",
  "review_kind": "critique",
  "reviewer_label": "fresh-internal-critique-r1",
  "overall_assessment": "Request a bounded planning clarification before APROVADO. The four architecture-r1 findings are addressed at contract level, and option C preserves coherent ownership and dependency direction. Scope, future validation, private operational boundaries and inherited exceptions are substantially explicit. Initial acknowledgment timing remains inconsistent across the packet, and manual-open effects on existing automation deserve a focused compatibility case. Performance remains unmeasured; the stated budgets and planned PostgreSQL/browser evidence are appropriate. This review grants no execution authority.",
  "recommended_path": "Retain option C, the existing catalogue and acceptance owners, explicit initial resolution, transaction ordering and per-owner ordinary admissions. Resolve the initial acknowledgment deadline contract, record the inherited NOVA_CONVERSA behavior for manually opened conversations, and update the affected validation criteria. Publish any material revision and complete current planning guards before seeking explicit APROVADO. Preserve the recorded ST-CON-05 limits and future approved-asset/runtime proof requirements.",
  "performance_position": "mixed",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "CR-R1-01",
      "severity": "medium",
      "title": "Initial acknowledgment lacks a consistent deadline predicate",
      "rationale": "The packet summary specifies explicit risk acknowledgment after the dispatch deadline, and the normative ordinary-admission contract enforces that condition. The initial-attempt contract instead permits acknowledgment for AMBIGUOUS or EXTERNAL_ACCEPTED_LOCAL_BLOCKED without identifying an applicable dispatch deadline or requiring it to have passed. A transport timeout can classify an initial attempt as AMBIGUOUS before its lease expires, so the endpoint description permits release while reconciliation would still treat the claim as live. Explicit duplicate-risk confirmation is already required, but the permitted release timing remains inconsistent.",
      "suggested_action": "Identify the persisted deadline governing initial SENDING claims and freeze the acknowledgment predicate for SENDING-derived AMBIGUOUS attempts. State separately whether confirmed EXTERNAL_ACCEPTED_LOCAL_BLOCKED attempts may be acknowledged earlier. Reconcile the summary, endpoint table, state rules, DoD and validation cases. Test acknowledgment before and after the chosen deadline, successor admission and a late original result. If earlier initial acknowledgment is intentional, record that exception explicitly before approval.",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "affected_paths": [
        "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md"
      ]
    },
    {
      "finding_id": "CR-R1-02",
      "severity": "low",
      "title": "Cover first-inbound automation after manual conversation creation",
      "rationale": "IncomingService passes acceptance.conversationCreated into the NOVA_CONVERSA trigger predicate. Manual open creates the conversation before any Message exists; consequently, the first later inbound message will have conversationCreated=false and will not activate that trigger, including when the operator opened the conversation and abandoned the initial send. This follows the inherited implementation, but the current consumer and validation matrices do not explicitly record this observable consequence of the new journey.",
      "suggested_action": "Record the expected NOVA_CONVERSA behavior for a manually opened empty conversation and add a focused planned integration case covering open without send followed by the first inbound message. Assert that opening itself invokes no automation. Preserve the delivered trigger predicate unless a different product behavior is explicitly reviewed and admitted.",
      "category": "tests",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "affected_paths": [
        "foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
        "api-app/src/domain/inbox/incoming.service.ts",
        "api-app/src/domain/inbox/message-acceptance.service.ts"
      ]
    }
  ]
}
```


---
## Prior current review / resolution evidence/critique-r1.merge.json

```
{
  "schema_version": "subagent-review-merge-v2",
  "artifact_kind": "subagent_review_merge",
  "authoritative": false,
  "edit_policy": "derived_merge_packet",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/critique-r1.dispatch.json",
  "review_kind": "critique",
  "review_count": 1,
  "reviewer_labels": [
    "fresh-internal-critique-r1"
  ],
  "highest_finding_severity": "medium",
  "axis_summary": {
    "performance": "mixed",
    "elegance": "acceptable",
    "structural_soundness": "mixed",
    "operational_fit": "mixed"
  },
  "recommended_paths": [
    "Retain option C, the existing catalogue and acceptance owners, explicit initial resolution, transaction ordering and per-owner ordinary admissions. Resolve the initial acknowledgment deadline contract, record the inherited NOVA_CONVERSA behavior for manually opened conversations, and update the affected validation criteria. Publish any material revision and complete current planning guards before seeking explicit APROVADO. Preserve the recorded ST-CON-05 limits and future approved-asset/runtime proof requirements."
  ],
  "exact_next_step": "Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.",
  "findings": [
    {
      "finding_id": "F-49CD0618",
      "severity": "medium",
      "title": "Initial acknowledgment lacks a consistent deadline predicate",
      "rationale": "The packet summary specifies explicit risk acknowledgment after the dispatch deadline, and the normative ordinary-admission contract enforces that condition. The initial-attempt contract instead permits acknowledgment for AMBIGUOUS or EXTERNAL_ACCEPTED_LOCAL_BLOCKED without identifying an applicable dispatch deadline or requiring it to have passed. A transport timeout can classify an initial attempt as AMBIGUOUS before its lease expires, so the endpoint description permits release while reconciliation would still treat the claim as live. Explicit duplicate-risk confirmation is already required, but the permitted release timing remains inconsistent.",
      "suggested_action": "Identify the persisted deadline governing initial SENDING claims and freeze the acknowledgment predicate for SENDING-derived AMBIGUOUS attempts. State separately whether confirmed EXTERNAL_ACCEPTED_LOCAL_BLOCKED attempts may be acknowledged earlier. Reconcile the summary, endpoint table, state rules, DoD and validation cases. Test acknowledgment before and after the chosen deadline, successor admission and a late original result. If earlier initial acknowledgment is intentional, record that exception explicitly before approval.",
      "reviewer_labels": [
        "fresh-internal-critique-r1"
      ],
      "source_finding_ids": [
        "CR-R1-01"
      ],
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "candidate_rule_id": "n/a"
    },
    {
      "finding_id": "F-4ACC72C3",
      "severity": "low",
      "title": "Cover first-inbound automation after manual conversation creation",
      "rationale": "IncomingService passes acceptance.conversationCreated into the NOVA_CONVERSA trigger predicate. Manual open creates the conversation before any Message exists; consequently, the first later inbound message will have conversationCreated=false and will not activate that trigger, including when the operator opened the conversation and abandoned the initial send. This follows the inherited implementation, but the current consumer and validation matrices do not explicitly record this observable consequence of the new journey.",
      "suggested_action": "Record the expected NOVA_CONVERSA behavior for a manually opened empty conversation and add a focused planned integration case covering open without send followed by the first inbound message. Assert that opening itself invokes no automation. Preserve the delivered trigger predicate unless a different product behavior is explicitly reviewed and admitted.",
      "reviewer_labels": [
        "fresh-internal-critique-r1"
      ],
      "source_finding_ids": [
        "CR-R1-02"
      ],
      "category": "tests",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "candidate_rule_id": "n/a"
    }
  ]
}

```


---
## Prior current review / resolution evidence/supplemental-source-seal-v1.1.json

```
{
  "created_at_utc": "2026-10-22T14:34:54.560642+00:00",
  "scope": "existing clean acceptance owner omitted from initial path admission; no source mutation",
  "product_head": "db5a86758a165fac8a1ab587599c37b17890530c",
  "records": [
    {
      "path": "api-app/src/domain/inbox/message-acceptance.service.ts",
      "bytes": 15730,
      "sha256": "b053744ee44b7e91fd45b5c146f759f55c70b8e517b8fbb1cab39806407335e1",
      "bounded_mutation_proposed_after_approval": true
    }
  ]
}

```


---
## Prior current review / resolution evidence/audit-floor-after-architecture-v1.1.json

```
{
  "schema_version": "audit-escalation-guard-v1",
  "artifact_kind": "audit_escalation_decision",
  "rule_id": "paced.audit-escalation.requirements",
  "outcome": "go",
  "blocked": false,
  "todo_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/todos/active/features/TODO-leadshug-start-conversation-by-contact.md",
  "trigger_matrix_fingerprint": "fa884bf1d2e7",
  "trigger_matrix": {
    "complexity": "big",
    "blast_radius": "cross-stack",
    "behavioral_change_or_bugfix": "yes",
    "changes_public_contract": "yes",
    "touches_auth_or_tenant": "yes",
    "touches_runtime_or_infra": "yes",
    "touches_tests": "yes",
    "critical_user_journey": "yes",
    "release_or_promotion_critical": "no",
    "high_severity_plan_review_issue": "yes",
    "explicit_three_lane_request": "no"
  },
  "decisions": {
    "critique": {
      "decision": "required",
      "lifecycle_gate": "before_aprovado",
      "workflow": "wf-docker-independent-critique-method",
      "depth": "expanded",
      "reason_codes": [
        "CRITIQUE-BASELINE-ALWAYS",
        "CRITIQUE-EXPANDED-RISK-SIGNALS"
      ]
    },
    "test_quality_audit": {
      "decision": "required",
      "lifecycle_gate": "before_completed",
      "workflow": "wf-docker-independent-test-quality-audit-method",
      "depth": "full",
      "reason_codes": [
        "TQA-TESTS-TOUCHED",
        "TQA-BEHAVIOR-OR-BUGFIX",
        "TQA-PUBLIC-CONTRACT",
        "TQA-CRITICAL-JOURNEY"
      ]
    },
    "final_review": {
      "decision": "required",
      "lifecycle_gate": "before_completed",
      "workflow": "wf-docker-independent-final-review-method",
      "depth": "expanded",
      "reason_codes": [
        "FINAL-BASELINE-ALWAYS",
        "FINAL-EXPANDED-RISK-SIGNALS"
      ]
    },
    "triple_review": {
      "decision": "recommended",
      "lifecycle_gate": "before_completed",
      "workflow": "audit-protocol-triple-review",
      "replacement_policy": "additive_only",
      "reason_codes": [
        "DEDICATED-AUDIT-EXPANDED-CHALLENGE-RECOMMENDED"
      ]
    },
    "security_review": {
      "decision": "required",
      "lifecycle_gate": "before_completed",
      "workflow": "security-adversarial-review",
      "reason_codes": [
        "SEC-AUTH-OR-TENANT"
      ]
    },
    "performance_concurrency": {
      "decision": "required",
      "lifecycle_gate": "per_pcv1_gate_deadlines",
      "workflow": "wf-docker-performance-concurrency-validation-method",
      "reason_codes": [
        "PCV-RUNTIME-OR-INFRA"
      ]
    },
    "verification_debt": {
      "decision": "required",
      "lifecycle_gate": "before_completed",
      "workflow": "verification-debt-audit",
      "reason_codes": [
        "VDA-MEDIUM-BIG-OR-RELEASE"
      ]
    },
    "architecture_decision_review": {
      "decision": "required",
      "lifecycle_gate": "after_diagnosis_before_aprovado",
      "review_kind": "architecture_opinion",
      "workflow": "wf-docker-subagent-orchestration-method",
      "reason_codes": [
        "ARCHITECTURE-GOVERNANCE-REQUIRED"
      ]
    },
    "architecture_adherence_review": {
      "decision": "required",
      "lifecycle_gate": "after_implementation_before_completed",
      "review_kind": "architecture_adherence",
      "workflow": "wf-docker-subagent-orchestration-method",
      "reason_codes": [
        "ARCHITECTURE-GOVERNANCE-REQUIRED"
      ]
    }
  },
  "violations": []
}

```
