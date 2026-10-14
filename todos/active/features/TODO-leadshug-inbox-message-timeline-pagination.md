# TODO LeadsHug histórico completo e paginado na inbox

## Quick Start

Rascunho criado a partir de delphi-ai/templates/todo_template.md; ainda não autoriza execução.

## Title

Histórico completo e paginado na inbox do LeadsHug.

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Tactical state:** `Review`
- **Prepared on:** 2026-10-14.
- **Scope selection source:** atendimento selecionado pelo usuário; revisão e preparação de aprovação autorizadas por “Pode seguir para revisão e aprovação”, em 2026-10-14.
- **Implementation approval:** pendente da apresentação do contrato revisado e do APROVADO final.

## Context

A thread da inbox busca as primeiras 200 mensagens em ordem crescente, sem metadados de continuação. Uma conversa longa oculta mensagens recentes. A tela Consultar já pagina, mas atende outro contrato e não marca leitura. Esta entrega torna todo o histórico acessível na inbox, preservando BU, sessão, janela de resposta e autoria.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md`
- **Primary story ID:** `ST-ATT-01`
- **Why this is the right current slice:** CAP-010 estende um fluxo existente, com aceitação verificável e sem depender das decisões ainda abertas de transferência, mídia e estados.
- **Direct-to-TODO rationale:** n/a; há feature brief para o pacote.

## Contract Boundary

Este rascunho define o primeiro recorte proposto. Alterações em contrato, autorização, escopo ou validação devem ser resolvidas antes do congelamento e da aprovação. O planejamento das demais stories não concede execução neste TODO.

## Implementation Intent

- **Current delivery:** leitura paginada da thread BFF e navegação incremental na inbox.
- **Planned next steps:** transferência/ownership, estados e mídia, em TODOs próprios.
- **Anticipatory implementation authorized now:** none.
- **Rationale:** reutilizar Conversation/Message e as fronteiras existentes; acrescentar abstrações apenas quando necessárias ao contrato de paginação e mesclagem.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Blocked`
- **Next exact step:** publicar baseline documental, executar revisão independente e guardas, integrar achados e apresentar contrato para APROVADO.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `blocked`
- **Why this state now:** o TODO está em Draft; execução depende da revisão e aprovação do contrato.
- **Exit condition:** pacote de aprovação completo, aprovação explícita e authority guard em go.

## Scope

- [ ] Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API.
- [ ] Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor.
- [ ] Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores.
- [ ] Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID.
- [ ] Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada.
- [ ] Preservar histórico carregado após envio, claim, close e eventos de tempo real.
- [ ] Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens.
- [ ] Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo.
- [ ] Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado.

## Proposed API Contract

### GET /api/bff/conversations/:id/messages

- Autenticação por sessão e grant ATENDENTE ou superior na BU; recurso fora do escopo continua 404.
- Query proposta: `limite` inteiro 1..100, padrão 50; `antes` cursor opaco opcional. Valor malformado ou cursor que não pertença à conversa autorizada recebe 400 `PAGINACAO_INVALIDA`, sem revelar recurso alheio. Query desconhecida não altera comportamento.
- Resposta mantém `conversa`, `janela` e `messages`; acrescenta `paginacao: { limite, temAnteriores, cursorAnterior }`.
- Sem cursor, selecionar as últimas N mensagens. Devolver cada página em ordem crescente por `(createdAt, id)`.
- Cursor usa uma referência estável à mensagem-limite; resolve data/ID dentro da conversa autorizada. Mensagens anteriores usam comparação estrita pelo par de ordenação.
- `cursorAnterior` aponta ao limite mais antigo da página somente quando existe continuação; caso contrário é null. Consulta busca no máximo N+1 registros para calcular continuação.
- Página vazia devolve `messages: []`, `temAnteriores: false` e cursor null.
- A abertura inicial mantém o efeito atual de marcar a conversa como lida; paginação para trás não marca novas mensagens como lidas. Sem novo efeito na consulta de auditoria.
- Atualizações e resposta preservam a coleção de histórico já carregada; deduplicação por ID no cliente é mesclagem de páginas, não prova de idempotência de webhook.
- Após reconexão ou chegada de mais de uma página de mensagens novas, buscar páginas de continuidade até alcançar a fronteira já carregada. Não apresentar uma coleção como contínua se houver lacuna; preservar contexto e permitir retry explícito da recuperação.
- Cursor não é credencial nem concede acesso. Contratos da API pública e Consultar permanecem sob seus owners atuais.

## Delivery Status Semantics

- `Pending`: no meaningful delivery milestone has been reached yet.
- `Local-Implemented`: work is implemented in a local branch and validated locally.
- `Lane-Promoted`: work has been merged through the declared lane threshold (usually `dev`).
- `Production-Ready`: final required lane threshold is complete and confidence gates are satisfied.
- `Provisional`: delivery is intentionally partial/incomplete but useful for unblocking dependent work.
- `Blocked`: work cannot currently proceed; `Blocker Notes` become mandatory.

## Active Work State Semantics

- `implementation`: the TODO is still gaining or changing implementation/test evidence.
- `review`: local implementation is materially complete, but the TODO remains in `active/` because package-wide review, Copilot-mimic, CI-equivalent, final validation, or explicit promotion-readiness scrutiny is still open.
- `blocked`: execution is paused on an explicit blocker; `Blocker Notes` are mandatory.
- `n/a once moved out of active`: use after the TODO moves to `promotion_lane/` or `completed/`.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; nenhuma entrega parcial é reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

- **Blocker:** aprovação final da implementação ainda pendente.
- **Why blocked now:** a autorização recebida cobre revisão e preparação da aprovação.
- **What unblocks it:** revisão convergida, preflight-go e APROVADO humano para este contrato.
- **Owner / source:** usuário; workflow local de aprovação de TODOs.
- **Last confirmed truth:** histórico da inbox tem teto de 200; código API/Web mantém as baselines registradas.

## Execution Lane Tracking (Required)

- **Local implementation branches:** api-app:feature/inbox-timeline-pagination; web-app:feature/inbox-timeline-pagination, a criar no checkout principal após aprovação. Foundation:main.
- **Promotion lane path:** branches locais -> validação local -> evidência/closeout na Foundation; deploy e promoção remota de código fora do recorte.
- **Lane-promoted threshold for this TODO:** n/a; entrega local validada.
- **Production-ready threshold for this TODO:** não reivindicado; publicação requer contrato separado.
- **Execution topology:** primary-checkout-single-writer.
- **Git isolation authorization:** not-requested; sem worktrees/cópias auxiliares.
- **Subagent / delegation authorization:** revisão independente requerida pelo skill local wf-docker-todo-approval-gates-method e seu workflow; executor de código será o routine-executor predeclarado somente após APROVADO deste contrato.
- **Documentation git-write authority:** git_write_authority_guard retornou go para git-commit e git-push de Foundation main; autorização autônoma documental conforme workflow local.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Out of Scope

- Transferência, exclusividade de resposta, SLA, distribuição de agentes, novas equipes e papéis.
- Estados de entrega/leitura/falha e deduplicação de recebimento por externalId.
- Mídia, templates, campanhas, CRM e automações Typebot.
- Mudanças nos contratos da API pública ou da tela Consultar.
- Redesenho da lista de conversas ou paginação da lista; a story cobre mensagens de uma conversa.
- Expansão de infraestrutura, uso de dados reais, integração com runtime legado ou publicação.

## Diff Expectation Contract (Required Before Delivery)

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| api | api-app | 5db3fbe2043428749895fc3ff6441e9457467dd0 | working_tree |
| web | web-app | 6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9 | working_tree |
| foundation | foundation_documentation | 40828a20f2d6c3a1443e7ee132f42483840d6abb | working_tree |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/domain/inbox/conversations.service.ts; src/domain/inbox/*pagination*.ts; src/domain/inbox/*pagination*.spec.ts | A,M | Consulta bounded e cursor validado. |
| api | src/surfaces/bff/conversations.controller.ts; test/atendimento.e2e-spec.ts; test/*timeline*.e2e-spec.ts; test/browser-server.cjs; test/timeline-fixtures.cjs | A,M | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | prisma/schema.prisma; prisma/migrations/*timeline*/migration.sql | A,M | Somente índice de paginação, se necessário e justificado por plano de consulta. |
| web | src/api.ts; src/telas/Inbox.tsx; src/*timeline*; src/estilo.css | A,M | Types, coleção, navegação e posição da timeline. |
| web | e2e/telas.spec.ts; e2e/*timeline*.spec.ts; playwright.config.ts | A,M | Fluxo real e correção do path da API. |
| foundation | todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md; artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md; artifacts/reviews/leadshug-inbox-timeline-20261014/**; backlog/README.md; modules/inbox-and-conversations.md | A,M | Contrato, framing e evidência específicos. |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/integrations/**; src/surfaces/public/**; src/domain/inbox/incoming.service.ts | any | Providers, API pública e recebimento fora do recorte. |
| web | src/telas/Typebot.tsx; src/telas/IdentidadeVisual.tsx | any | Funcionalidades independentes. |
| foundation | todos/completed/**; project_mandate.md; project_constitution.md; system_roadmap.md; local_packages.yaml | any | Preservar história e autoridades não alteradas por este recorte. |
| workspace | .env*; .gitmodules; docker-compose.yml; .git/**; .github/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| all | node_modules/**; dist/**; artifacts/tmp/** | any | Saídas locais de validação não são entrega versionada. |

### Diff Deviation Analysis

Pendente; nenhum diff de implementação foi produzido. Baselines devem ser revalidadas antes do freeze se houver commits novos.

## Bounded But Elastic Guardrails

Ajustes locais de cursor, queries, mesclagem e CSS podem permanecer neste objetivo. Alterar a API pública, papéis, unread semantics além do contrato proposto, providers, retries ou topology exige recorte/decisão próprios.

## Definition of Done

- [ ] DOD-01: contrato aprovado e consolidado no módulo responsável.
- [ ] DOD-02: todas as mensagens de uma conversa com mais de 200 registros são alcançáveis sem lacunas ou repetições, com página inicial recente e desempate estável.
- [ ] DOD-03: autorização e cursor não permitem acesso a outra BU/Mantenedora.
- [ ] DOD-04: navegação, posição, atualização, envio e troca rápida de conversa preservam histórico e contexto corretos.
- [ ] DOD-05: limites, cursor inválido, vazio, falha/retry e sem continuação têm respostas e UI verificadas.
- [ ] DOD-06: suites API/Web e Playwright passam na topologia de validação isolada; migração de índice é validada se criada.
- [ ] DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão.

## Validation Steps

- [ ] VAL-01: provisionar banco local dedicado a testes e migrations atuais; confirmar DATABASE_URL e endpoint antes dos testes que executam deleteMany.
- [ ] VAL-02: API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e, dentro de api-app.
- [ ] VAL-03: fixtures com 251 mensagens, timestamps empatados, duas Mantenedoras, duas BUs e grants distintos; caminhar todas as páginas e comparar IDs esperados.
- [ ] VAL-04: Web: npm ci; npm run build; npm test; npm run test:tela, dentro de web-app, usando backend real fresco e banco dedicado via LEADSHUG_E2E_DATABASE_URL.
- [ ] VAL-05: browser abre recente, carrega anteriores, responde, recebe evento e muda conversa com requisição antiga pendente; verificar persistência/readback e isolamento.
- [ ] VAL-06: se acrescentado índice, executar prisma migrate deploy no banco dedicado e registrar plano de consulta representativo.
- [ ] VAL-07: executar as revisões e guardas exigidos pelos workflows vigentes, sem substituir prova de fluxo por build.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | Contrato aprovado/consolidado | doc | TODO + modules/inbox-and-conversations.md | foundation | planned | Sem aprovação registrada. |
| DOD-02 | Definition of Done | Histórico completo e ordenação | test | VAL-03 | PostgreSQL dedicado | planned | 251 mensagens e timestamps empatados. |
| DOD-03 | Definition of Done | BU/tenant/cursor | test | VAL-03 + test:e2e | PostgreSQL dedicado | planned | Negativos cross-BU/cross-tenant. |
| DOD-04 | Definition of Done | Fluxo e races de UI | runtime | VAL-05 + test:tela | browser/backend real | planned | Abertura/envio/refresh/troca. |
| DOD-05 | Definition of Done | Validação e estados de erro | test/runtime | VAL-03 + VAL-05 | API/browser | planned | Cursor inválido e retry. |
| DOD-06 | Definition of Done | Suites e índice condicional | test/migration | VAL-01..06 | local isolado | planned | Sem teste da aplicação executado neste planejamento. |
| DOD-07 | Definition of Done | Revisões e closeout | review | VAL-07 | foundation | planned | Gates não executados. |

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Docker local | Runner e PostgreSQL isolado | healthy | 2026-10-14 | Daemon 27.1.1 respondeu | Containers operacionais não são alvos de testes. |
| Node.js 22 | Build/suites | healthy | 2026-10-14 | node.exe v22.22.2 disponível; node Linux ausente | Execução planejada em runner Linux Node 22 compatível com Dockerfiles; não misturar npm Windows com processos Linux. |
| Meta/Evolution externos | Interfaces de transporte preservadas | unknown | 2026-10-14 | Nenhum probe externo | Bootstrap de teste usa backend real e substitui somente portas externas; não enviar mensagens reais. |

Execução local planejada: runner Linux temporário Node 22, conforme imagens Node 22 dos Dockerfiles; PostgreSQL 16 descartável exclusivo deste TODO, com DB/porta registrados antes de E2E e DATABASE_URL explícita. Sem editar .env/Compose do produto. API e browser compartilham o mesmo DB de teste. A implementação pode acrescentar suporte de teste nos paths previstos; prontidão efetiva será provada antes da suite.

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Current profile:** Strategic / CTO-Tech-Lead, preparação documental.
- **Primary execution profile:** operational-coder.
- **Active technical scope:** nestjs, react, vite, postgresql, prisma, docker.
- **Handoff:** Strategic -> Operational/Coder depois de contrato e aprovação; DevOps somente para resolver prontidão com contrato próprio; Assurance para revisão/evidência.
- **Execution topology:** principal checkout, single writer; Foundation main.

## Complexity

- **Level:** medium.
- **Checkpoint policy:** contrato e API, UI integrada, prova browser e closeout; cada checkpoint tem evidência afetada, sem alegar suite ampla antes de sua execução.
- **Why this level:** alteração de API persistente consumida por UI com cursores, autorização e races de realtime.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** foundation_documentation/modules/inbox-and-conversations.md.
- **Secondary module docs:** identity-and-tenancy.md e audit-and-history.md, para preservar invariantes.
- **Consolidation target:** somente contrato local da thread e regras de cursor/paginação no módulo inbox-and-conversations.
- **Source capability:** CAP-010 no catálogo ST-02, referência de evidência e não ID de capacidade canônica nova.

## Decision Pending (Resolve Before Freeze)

Nenhuma decisão de produto é declarada aprovada nesta preparação. O contrato revisado, inclusive parâmetros, superfície BFF e ordem inicial, será submetido em uma aprovação única. Runners e lanes estão definidos abaixo; a revisão pode corrigir detalhes antes do freeze final.

## Decisions (Resolved Before Freeze)

- Primeiro recorte proposto: histórico da inbox BFF; Consultar e API pública preservam seus contratos.
- Página padrão 50, limite máximo 100; ordenação createdAt/id e cursor scoped.
- Abrir conversa continua marcando leitura; histórico anterior e recuperação em background não devem apagar não lidas novas. Revisão independente deve verificar a expressão desse comportamento no contrato.
- Backend real e PostgreSQL descartável de teste, com dublês somente nas portas externas de provider, sem mocks do BFF no browser.
- Single writer no checkout principal; Foundation main; API/Web em branches locais fora main; sem worktrees, deploy ou mensagens reais externas.
- Essas decisões técnicas compõem a proposta congelável e passam a autoridade de execução apenas após APROVADO.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Decision | Source | Status | Handling / consolidation |
| --- | --- | --- | --- |
| Conversa única BU/contato | modules/inbox-and-conversations.md | preserved | Cursor consulta somente conversa autorizada. |
| Grants materializados na BU | modules/identity-and-tenancy.md | preserved | Negativos de tenant/BU no banco real. |
| Histórico e leitura scoped | modules/audit-and-history.md | preserved | Consulta de auditoria não ganha efeito de atendimento. |
| Janela/capability de envio | modules/inbox-and-conversations.md | preserved | Envio e API pública têm suites de regressão. |
| Paginação da thread | contrato proposto deste TODO | extend-local-contract | Consolidar no módulo após aprovação e antes da implementação. |

## Decision Baseline (Frozen Before Implementation)

Baseline técnico proposto em 2026-10-14: contrato, escopo, DoD, testes e fronteiras deste TODO. Congelamento definitivo acontece após convergência da revisão e antes da aprovação final. A aprovação final aceita o conteúdo revisado; não há aprovação antecipada das decisões.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability:** required.
- **Why this applies:** estabelece acesso paginado scoped e mesclagem consistente para uma thread operacional antes truncada.
- **Deviation / debt being retired:** teto silencioso de 200 mensagens e substituição da coleção após refresh.
- **Target steady-state after closeout:** acesso determinístico bounded e atualização sem perda de histórico/contexto.
- **Temporary exceptions allowed:** none.
- **Cutover / removal condition:** BFF e inbox adotam o contrato aprovado juntos, com regressões passando; nenhum fallback para carregar todas as mensagens.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Cursor dentro da conversa autorizada | constituição + contrato BFF | API | Cursor não amplia grants. |
| Ordem createdAt/id e query bounded | contrato proposto | API | Empates e inserções não duplicam páginas. |
| Estado por conversa e geração de request | regra React | Web | Resposta antiga não troca conversa/BU. |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| Aumentar teto fixo ou fetch-all | Consulta sem paginação | Repete truncamento ou leitura ilimitada. | No exceptions |
| Cursor sem escopo ou só timestamp | Negativos/empates falham | Pode vazar dados ou perder mensagens. | No exceptions |
| Refresh substitui histórico ou aceita contexto antigo | Browser perde mensagens | Quebra atendimento em atualização/troca. | No exceptions |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| PostgreSQL contract tests | BFF/cursor | npm run test:e2e | Teto/empate/escopo/limites | implement-in-this-todo | VAL-03, DOD-02/03/05 |
| Browser mutation/navigation | Inbox | npm run test:tela | Envio/refresh/troca/contexto | implement-in-this-todo | VAL-05, DOD-04/06 |
| Query plan | índice de Message | EXPLAIN representativo | Scan/sort sem acesso scoped adequado | implement-in-this-todo | VAL-06, registrar decisão do índice |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

Planejadas revisões de contrato/escopo, performance da query, races e integridade de evidência. Resultados pendentes; nenhuma revisão independente realizada nesta preparação.

## Gate: Review Baseline Freeze

pending-freeze; documentação preparada no checkout principal de Foundation main. Nenhum commit/push realizado ou autorizado por este rascunho.

## Gate: Review Scope Drift

pending-freeze; comparar baselines e caminhos esperados no pacote refinado antes da revisão.

## Questions To Close

Aprovação humana única do contrato final após revisão. Questões de transferência, mídia e status continuam nas stories posteriores; não serão resolvidas por esta implementação.

## Pattern References (Optional; Enforced When Cited)

n/a; nenhum ID de pattern é reivindicado.

## Assumptions Preview (Required Before Plan Review)

| ID | Assumption | Evidence | Risk | Validation / Impact | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Thread pega primeiras 200 mensagens | ../api-app/src/domain/inbox/conversations.service.ts:88 | Oculta recente | Fixture 251; query/contrato | Keep as Assumption |
| A-02 | Refresh substitui coleção da thread | ../web-app/src/telas/Inbox.tsx:59 | Perda de páginas | Browser envio/refresh/troca | Keep as Assumption |
| A-03 | API pública lista mensagens em query própria | ../api-app/src/surfaces/public/conversations.controller.ts:103 | Regressão contrato | Suites atuais sem mudança de shape | Keep as Assumption |
| A-04 | Helpers E2E apagam dados do banco apontado | ../api-app/test/helpers.ts:112 | Perda de dados | PostgreSQL dedicado descartável | Keep as Assumption |
| A-05 | Harness precisa corrigir caminho e provider determinístico para provar envio | ../web-app/playwright.config.ts:32; ../api-app/test/helpers.ts:68 | Suite inválida ou envio externo | Backend real com portas externas fake em suporte de teste | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

### Ordered Steps

1. Resolver DP-01..03, preparar revisão/freeze/aprovação conforme workflows; documentar contrato no módulo.
2. Reproduzir truncamento e testar cursor/limites/empates/escopo no PostgreSQL dedicado.
3. Implementar consulta bounded e contrato BFF; avaliar índice real e migrar somente se necessário.
4. Implementar coleção por conversa, páginas anteriores, posição, atualização e proteção contra respostas antigas.
5. Corrigir apenas o path do harness, construir API/Web frescos e executar fixtures/fluxos browser.
6. Validar regressões do núcleo, consolidar contrato/evidência e cumprir closeout.

### Flow Evidence Planning Matrix

| Flow | Fixture | Required evidence | Negative / race |
| --- | --- | --- | --- |
| Abrir/carregar anteriores | 251 mensagens | browser recente, scroll, alcançar primeira e última | empates, página vazia, cursor inválido |
| Enviar/atualizar | Histórico anterior carregado e canal fake | backend persiste e UI mantém coleção | resposta/evento repetido não duplica ID |
| Reconectar após burst | Mais de 100 mensagens novas entre snapshots | browser recupera páginas até cruzar a fronteira carregada | sem lacuna silenciosa nem perda de posição; erro permite retry |
| Trocar conversa/BU | Duas conversas e dois tenants | browser seleciona destino e conserva contexto | resposta antiga atrasada não substitui destino; sem grant falha |

### Local CI-Equivalent Suite Matrix

| Surface | Command | Preconditions | Intended behavior | Status |
| --- | --- | --- | --- | --- |
| API CI | npm run lint; npm run build; npm test | npm ci + Prisma gerado | Contrato/validação/build atuais | planned |
| API PostgreSQL | npm run test:e2e | migrations e banco dedicado com fixtures | Paginação, escopo, contrato e regressões | planned |
| Web CI | npm run build; npm test | npm ci | Types e lógica de coleção | planned |
| Web browser | npm run test:tela | path ../api-app corrigido, bundles frescos, banco dedicado, Chromium | Fluxos reais e races | planned |

### Frontend / Consumer Matrix

| Producer | Consumer | Impact / proof |
| --- | --- | --- |
| Thread BFF | web-app/src/api.ts e Inbox.tsx | Tipo paginacao e estado de páginas; teste contrato/browser |
| Evento WebSocket | Inbox.tsx | Refresh scoped preserva coleção; prova runtime |
| ConversationsService | BFF e operações existentes | Não alterar envio/claim/close/janela; suites de regressão |
| Consulta/public API | Consumidores existentes | Contrato independente preservado; suites atuais |

### Runtime / Rollout Notes

Backend de validação e Playwright usam o mesmo banco dedicado. Falta de runner ou banco impede prova de aplicação; não substituí-la por mocks de navegação. Publicação e envio real externo não integram este recorte.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

- **Status:** prepared-pre-freeze.
- **Required review:** full, por complexidade medium; avaliar contrato, segurança, paginação, custo da query e races.
- **Issue cards / residual risks:** DP-01..03, runners não resolvidos e possível índice. Nenhum resultado independente reivindicado.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

Pendente somente se o refinamento revelar ambiguidade material; não houve delegação/revisão externa nesta preparação.

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

| Trigger | Value | Evidence / Rationale |
| --- | --- | --- |
| complexity | medium | API e UI paginadas |
| blast_radius | cross-stack | BFF + React |
| behavioral_change_or_bugfix | yes | Primeiro carregamento passa a recente |
| changes_public_contract | yes | Contrato BFF consumido pela web |
| touches_auth_or_tenant | yes | Validação de cursor e grants |
| touches_runtime_or_infra | yes | Realtime e harness local |
| touches_tests | yes | API e browser |
| critical_user_journey | yes | Atendimento |
| release_or_promotion_critical | no | Sem release/deploy neste recorte |
| high_severity_plan_review_issue | no | Inicialmente sem finding formal |
| explicit_three_lane_request | no | Revisão solicitada, sem pedido de três lanes |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

- **Gate decision:** required.
- **Why this decision:** API/escopo/consulta e UI interativa com races.
- **Gate status:** not_run.
- **Critique status:** not_run.
- **Evidence / reference:** pacote ainda prepared-pre-freeze; executar revisão no gate correspondente.
- **Waiver authority / reference:** none.

## Gate: Assumption Code Coherence

- **Gate decision:** required.
- **Why this decision:** garantir que A-01..04 continuam verdadeiras no baseline refinado.
- **Trigger stage:** after critique convergence and before APROVADO.
- **Guard scope:** A-01,A-02,A-03,A-04.
- **Gate status:** not_run.
- **Evidence / reference:** prepared-pre-freeze; referências estáticas estão no Assumptions Preview.

## Approval

- **Approved by:** pending; não há APROVADO para este contrato.
- **Approval scope:** pendente; a seleção da frente não concede implementação deste Draft.
- **Execution not authorized by approval:** toda implementação até aprovação/guard; stories posteriores permanecem fora do recorte.
- **Renewed approval required when:** contrato, escopo, regras de leitura, validação ou risco mudarem materialmente.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

Preparação documental; recarregar fontes vinculantes após aprovação antes de execução.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| foundation_documentation/project_constitution.md | Produto | BU/conversa e teste real | inferir autorização da UI | Negativos scoped |
| delphi-ai/workflows/docker/todo-contract-refinement-method.md | Planejamento | matrizes/decisões | escopo implícito | Resolver Draft |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | Aprovação | freeze/revisão/evidência | declarar aprovação antes da revisão | Gates pendentes |
| delphi-ai/rules/stacks/nestjs/nestjs-architecture-always-on.md | API | input runtime e serviço de domínio | regra de negócio na UI | Validar cursor/limites |
| delphi-ai/rules/stacks/react/react-architecture-always-on.md | Inbox | owner de estado e races | resposta de conversa antiga | Browser real |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | BFF | contrato/guard | expandir API pública | Contrato local |
| delphi-ai/workflows/react/change-ui-boundary-method.md | UI | estados/acessibilidade | build como única prova | Fluxos browser |

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)

- **Client surface:** codex.
- **Current governed action:** implementation.
- **Selected role:** routine-executor.
- **Selected model:** gpt-6-luna.
- **Selected effort:** medium.
- **Proof mode:** declared.
- **Execution topology:** primary-checkout-single-writer.
- **Subagent / delegation authorization:** executor será solicitado por APROVADO para o contrato que predeclara esse handoff; revisão independente já requerida pelo workflow local invocado.
- **Git isolation authorization:** not-authorized.
- **Guard outcome:** go.
- **Guard evidence:** agent_role_routing_guard avaliado em 2026-10-14 para este único tuple; go de routing não é autorização de implementação.

Review lane separado: formal-reviewer, architecture_opinion/critique, gpt-6.1-sol, max, declared. Guard de critique retornou go; guard específico será executado antes do dispatch de arquitetura.

## Decision Adherence Validation (Mandatory Before Delivery)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Pipeline/Copilot P1/P2 Preflight

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Rule-Spirit Anti-Pattern Hunt

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## TODO Closeout Disposition

- **Disposition:** keep-active.
- **Disposition reason:** Draft aguardando refinamento/revisão/aprovação.
- **Post-commit/push status:** not-performed.
- **Next path/status action:** resolver DP-01..03; concluir somente depois de implementação/evidência e guardas.

## Security Risk Assessment (Mandatory Before Delivery)

Riscos: cursor alheio, scope bypass, resposta atrasada de outra conversa e testes contra banco operacional. Mitigar com autorização antes de cursor, filtro da conversa/BU, contexto de requisição e banco descartável dedicado. Evidência de implementação ainda planned.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

Queries bounded N+1 e ordem createdAt/id; evitar count/scan ilimitado para cada página. Verificar índice com fixture representativa. Inserção nova não desloca páginas anteriores por cursor. Mesclagem e scroll devem suportar chegada/refresh concorrentes; mudanças de ownership são story distinta.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

Pendentes contrato, runner, provas PostgreSQL/browser e revisões. Não reivindicar implementação ou fechamento com evidência histórica de outro TODO.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Gate decision:** required.
- **Why this decision:** API/escopo/consulta e UI interativa com races.
- **Gate status:** not_run.
- **Critique status:** not_run.
- **Evidence / reference:** pacote ainda prepared-pre-freeze; executar revisão no gate correspondente.
- **Waiver authority / reference:** none.

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Gate decision:** required.
- **Why this decision:** API/escopo/consulta e UI interativa com races.
- **Gate status:** not_run.
- **Critique status:** not_run.
- **Evidence / reference:** pacote ainda prepared-pre-freeze; executar revisão no gate correspondente.
- **Waiver authority / reference:** none.

## Independent Cutover Integrity Audit Gate

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Module Consolidation Gate (Required Before `Completed`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Commands (Run Locally)

Comandos de aplicação propostos estão em Validation Steps. Não executá-los contra bancos existentes nem reivindicar green nesta preparação.

## Files Expected (Compatibility Note)

O contrato de paths e baselines está no Diff Expectation Contract.

## COMENTÁRIO:

n/a; nenhum comentário pendente do usuário neste arquivo.

