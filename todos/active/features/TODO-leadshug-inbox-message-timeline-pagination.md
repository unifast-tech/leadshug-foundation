# TODO LeadsHug histórico completo e paginado na inbox

## Quick Start

Contrato criado a partir de delphi-ai/templates/todo_template.md, revisado, congelado e aprovado pelo usuário em 2026-10-14. Execução autorizada pelo authority guard normal; validação e reviews de entrega estão em andamento.

## Title

Histórico completo e paginado na inbox do LeadsHug.

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Tactical state:** `In-Progress`
- **Prepared on:** 2026-10-14
- **Scope selection source:** atendimento selecionado pelo usuário; revisão e preparação de aprovação autorizadas por “Pode seguir para revisão e aprovação”, em 2026-10-14
- **Implementation approval:** APROVADO explícito do usuário em 2026-10-14; ver Approval e authority guard normal go

## Context

A thread da inbox busca as primeiras 200 mensagens em ordem crescente, sem metadados de continuação. Uma conversa longa oculta mensagens recentes. A tela Consultar já pagina, mas atende outro contrato e não marca leitura. Esta entrega torna todo o histórico acessível na inbox, preservando BU, sessão, janela de resposta e autoria.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md`
- **Primary story ID:** `ST-ATT-01`
- **Why this is the right current slice:** CAP-010 estende um fluxo existente, com aceitação verificável e sem depender das decisões ainda abertas de transferência, mídia e estados
- **Direct-to-TODO rationale:** n/a; há feature brief para o pacote

## Contract Boundary

Este contrato aprovado define somente ST-ATT-01. Mudanças materiais de contrato, autorização, escopo ou obrigação de validação precisam da governança de escopo e aprovação; refinamentos locais fiéis ao contrato são tratados nesta execução. O planejamento das demais stories não concede execução neste TODO.

## Implementation Intent

- **Current delivery:** leitura paginada da thread BFF e navegação incremental na inbox
- **Planned next steps:** transferência/ownership, estados e mídia, em TODOs próprios
- **Anticipatory implementation authorized now:** none
- **Rationale:** reutilizar Conversation/Message e as fronteiras existentes; acrescentar abstrações apenas quando necessárias ao contrato de paginação e mesclagem

## Delivery Status Canon (Required)

- **Current delivery stage:** Local-Implemented
- **Qualifiers:** none
- **Next exact step:** validar e publicar as evidências/documentação na Foundation main; depois mover o mesmo TODO para completed e publicar a relocação.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** review
- **Why this state now:** entrega Local-Implemented validada/revisada e fonte commitada; documentação/evidências de closeout prontas para publicação e relocação.
- **Exit condition:** pareceres independentes resolvidos, guardas e consolidação canônica completos para closeout local.

## Scope

- [x] Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API.
- [x] Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor.
- [x] Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores.
- [x] Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID.
- [x] Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada.
- [x] Preservar histórico, cursor histórico, metadados atuais e draft correto durante envio, claim, close, backfill, poll e eventos/reconexão de socket.
- [x] Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens.
- [x] Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo.
- [x] Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado.

## Proposed API Contract

### GET /api/bff/conversations/:id/messages

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

n/a; nenhuma decisão material bloqueando execução no início.

## Execution Lane Tracking (Required)

- **Local implementation branches:** api-app:feature/inbox-timeline-pagination; web-app:feature/inbox-timeline-pagination no checkout principal. Foundation:main
- **Promotion lane path:** branches locais -> validação local -> evidência/closeout na Foundation; deploy e promoção remota de código fora do recorte
- **Lane-promoted threshold for this TODO:** n/a; entrega local validada
- **Production-ready threshold for this TODO:** não reivindicado; publicação requer contrato separado
- **Execution topology:** primary-checkout-single-writer
- **Git isolation authorization:** not-requested; sem worktrees/cópias auxiliares
- **Subagent / delegation authorization:** revisão independente requerida pelo skill local wf-docker-todo-approval-gates-method e seu workflow; executor de código será o routine-executor predeclarado somente após APROVADO deste contrato
- **Documentation git-write authority:** git_write_authority_guard retornou go para git-commit e git-push de Foundation main; autorização autônoma documental conforme workflow local

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

Esta entrega é local-only: não há autorização/promoção de ambiente ou claim Production-Ready. Provas locais não são SLO ou validação operacional.

## Out of Scope

- Transferência, exclusividade de resposta, SLA, distribuição de agentes, novas equipes e papéis.
- Estados de entrega/leitura/falha e deduplicação de recebimento por externalId.
- Mídia, templates, campanhas, CRM e automações Typebot.
- Mudanças nos contratos da API pública ou da tela Consultar.
- Redesenho da lista de conversas ou paginação da lista; a story cobre mensagens de uma conversa.
- Expansão de infraestrutura, uso de dados reais, integração com runtime legado ou publicação.

## Diff Expectation Contract

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
| api | src/domain/inbox/conversations.service.ts | A,M,?? | Consulta bounded e cursor validado. |
| api | src/domain/inbox/*pagination*.ts | A,M,?? | Consulta bounded e cursor validado. |
| api | src/domain/inbox/*pagination*.spec.ts | A,M,?? | Consulta bounded e cursor validado. |
| api | src/surfaces/bff/conversations.controller.ts | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/atendimento.e2e-spec.ts | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/*timeline*.e2e-spec.ts | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/browser-server.cjs | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/timeline-fixtures.cjs | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | prisma/schema.prisma | A,M,?? | Somente índice de paginação, se necessário e justificado por plano de consulta. |
| api | prisma/migrations/*timeline*/migration.sql | A,M,?? | Somente índice de paginação, se necessário e justificado por plano de consulta. |
| web | src/api.ts | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/telas/Inbox.tsx | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/*timeline* | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/estilo.css | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/tempoReal.ts | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/tempoReal.spec.ts | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | e2e/telas.spec.ts | A,M,?? | Fluxo real e correção do path da API. |
| web | e2e/*timeline*.spec.ts | A,M,?? | Fluxo real e correção do path da API. |
| web | playwright.config.ts | A,M,?? | Fluxo real e correção do path da API. |
| web | e2e/timeline-freshness.ts | A,M,?? | globalSetup canônico valida build/runtime servido antes dos testes, suporte de prova já autorizado. |
| foundation | todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md | A,M,D,R,?? | Contrato, framing e evidência específicos. |
| foundation | artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md | A,M,?? | Contrato, framing e evidência específicos. |
| foundation | artifacts/reviews/leadshug-inbox-timeline-20261014/** | A,M,?? | Contrato, framing e evidência específicos. |
| foundation | backlog/README.md | A,M,?? | Contrato, framing e evidência específicos. |
| foundation | modules/inbox-and-conversations.md | A,M,?? | Contrato, framing e evidência específicos. |
| foundation | todos/completed/features/TODO-leadshug-inbox-message-timeline-pagination.md | A,M,R,?? | Relocação do mesmo TODO no closeout aprovado, após provas e guardas. |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/integrations/** | any | Providers, API pública e recebimento fora do recorte. |
| api | src/surfaces/public/** | any | Providers, API pública e recebimento fora do recorte. |
| api | src/domain/inbox/incoming.service.ts | any | Providers, API pública e recebimento fora do recorte. |
| web | src/telas/Typebot.tsx | any | Funcionalidades independentes. |
| web | src/telas/IdentidadeVisual.tsx | any | Funcionalidades independentes. |
| foundation | project_mandate.md | any | Preservar história e autoridades não alteradas por este recorte. |
| foundation | project_constitution.md | any | Preservar história e autoridades não alteradas por este recorte. |
| foundation | system_roadmap.md | any | Preservar história e autoridades não alteradas por este recorte. |
| foundation | local_packages.yaml | any | Preservar história e autoridades não alteradas por este recorte. |
| api | .env* | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | .gitmodules | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | docker-compose.yml | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | .git/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | .github/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .env* | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .gitmodules | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | docker-compose.yml | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .git/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .github/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .env* | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .gitmodules | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | docker-compose.yml | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .git/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .github/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | node_modules/** | any | Saídas locais de validação não são entrega versionada. |
| api | dist/** | any | Saídas locais de validação não são entrega versionada. |
| api | artifacts/tmp/** | any | Saídas locais de validação não são entrega versionada. |
| web | node_modules/** | any | Saídas locais de validação não são entrega versionada. |
| web | dist/** | any | Saídas locais de validação não são entrega versionada. |
| web | artifacts/tmp/** | any | Saídas locais de validação não são entrega versionada. |
| foundation | node_modules/** | any | Saídas locais de validação não são entrega versionada. |
| foundation | dist/** | any | Saídas locais de validação não são entrega versionada. |
| foundation | artifacts/tmp/** | any | Saídas locais de validação não são entrega versionada. |

### Diff Deviation Analysis

Análise preliminar: o guard identificou incompatibilidade de representação (heading com sufixo, vários globs numa célula e labels workspace/all não declarados), sem desvio de produto. Corrigida a representação para título exato, um glob por linha e regras por repositório; os mesmos paths e baselines aprovados foram preservados. O tipo `??` explicita o estado ainda não staged dos arquivos novos já autorizados como A; não autoriza novos caminhos. A relocação do próprio TODO active → completed é o closeout já autorizado, sem alterar outros registros históricos. Guard final e diff real serão registrados antes da entrega.

Concretização de suporte de prova em 2026-10-15: `web-app/e2e/timeline-freshness.ts` implementa globalSetup de frescor já exigido pelo contrato aprovado (build fresco, backend real e evidência runtime), pois capturar do host falha quando preview é isolado no container e uma captura posterior à suite não satisfaz a regra temporal. A alternativa de arquivo temporário obrigatório faria clones dependerem de arquivo ausente; o helper versionado é a escolha local reproduzível. Acrescentado somente este path ao contrato. Não há nova story, comportamento de produto, provider, ambiente operacional ou obrigação de validação; é o HOW do suporte de teste já autorizado em Approval, VAL-04/05 e no pedido de continuidade. Sem exceção de modelo/topologia e sem nova aprovação de produto necessária.


## Bounded But Elastic Guardrails

Ajustes locais de cursor, queries, mesclagem e CSS podem permanecer neste objetivo. Alterar a API pública, papéis, unread semantics além do contrato proposto, providers, retries ou topology exige recorte/decisão próprios.

## Definition of Done

- [x] DOD-01: contrato aprovado e consolidado no módulo responsável.
- [x] DOD-02: histórico maior que 200 é alcançável sem lacunas/repetições, inicial recente, empates estáticos e inserções empatadas durante recuperação.
- [x] DOD-03: autorização/cursor não permitem outra conversa, BU ou Mantenedora; recurso inacessível é 404 antes de query inválida.
- [x] DOD-04: backfill, envio/refresh/close, troca rápida, reconexão sem evento posterior e recuperação mantêm histórico, posição, cursores, metadados e draft corretos.
- [x] DOD-05: limite/cursor/marcarLida, vazio/fim, falha/retry e recuperação pendente têm contrato/UI verificados; entradas posteriores à fronteira de abertura continuam não lidas.
- [x] DOD-06: suites API/Web/Playwright passam no backend real e banco isolado; plano SQL recente/profundo/empates registra custo e decisão de índice; migrate deploy validado se houver migração.
- [x] DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão.

## Validation Steps

- [x] VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional.
- [x] VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e.
- [x] VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos.
- [x] VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL.
- [x] VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada.
- [x] VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado.
- [x] VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout.
- [x] VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha.

## Completion Evidence Matrix (Required Before Delivery Claim)

Um registro por critério de Scope, Definition of Done e Validation Steps; texto integral preserva rastreabilidade. Status não são promovidos por resultado intermediário ou execução contaminada.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API. | doc | Foundation4cabc467 + modules/inbox-and-conversations.md | Foundation main | passed | Contrato consolidado antes do executor alterar API; não é só nota tática. |
| SCOPE-02 | Scope | Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor. | PostgreSQL integration | test/atendimento.e2e-spec.ts:317,365,371; api-e2e-authority.log | Node22 / PG16 descartável | passed | Cursor alheio em recurso autorizado400; recurso sem grant404 antes da query; sem sessão401; unread readback preservado. |
| SCOPE-03 | Scope | Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282; api-e2e-authority.log | Node22 / PG16 descartável | passed | 251 IDs, limite37 e grupo empatado; comparação de IDs na ordem real do banco, página recente e continuação bounded. |
| SCOPE-04 | Scope | Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | 251IDs, prepend preserva âncora inclusive chegada durante await, merge porID e cursor histórico separado. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| SCOPE-05 | Scope | Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Seis subcenários de contexto: conversa/BU × envio antigo com sucesso/falha/backfill. Destino mantém seleção, draft, erro, IDs, metadados e scroll. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| SCOPE-06 | Scope | Preservar histórico, cursor histórico, metadados atuais e draft correto durante envio, claim, close, backfill, poll e eventos/reconexão de socket. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Close vence backfill; autoria/draft/ref; reconnect sem evento; poll60 retoma progresso; T fixo, budget3 inclusive erros e restart obrigatório. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| SCOPE-07 | Scope | Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens. | PostgreSQL + source-owned Playwright | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Fixtures próprias251+, empates acima de página, grupoT/H>T/lateID, burst e readback DB completo; testes source-owned, sem payload BFF fabricado. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| SCOPE-08 | Scope | Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo. | source + integration | playwright.config.ts + test/browser-server.cjs + test/timeline-fixtures.cjs; execution-evidence.md | backend Nest real / DB exclusivo | passed | Path ../api-app; somente Meta/Evolution fake, sem flags ou rotas de teste no entrypoint de produção; autoria persistida observada. |
| SCOPE-09 | Scope | Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado. | SQL EXPLAIN + API e2e | evidence/explain-timeline-exact.sql/.log; evidence/explain-index-trial.sql/.log; pcv-eps.json; atendimento.e2e-spec.ts | PG16 /20382 mensagens/1000 empatadas | passed | Recent1.094ms/deep3.442ms/tie0.850ms; trial composto deep3.942ms e9832buffers contra357 existente. Sem migration nova: condição de índice não demonstrou ganho. Risco de varredura profunda explícito; aceito em delivery-adherence-resolution.json, sem SLO de produção. |
| DOD-01 | Definition of Done | DOD-01: contrato aprovado e consolidado no módulo responsável. | doc | TODO + modules/inbox-and-conversations.md | foundation | passed | APROVADO explícito e contrato consolidado em modules/inbox-and-conversations.md. |
| DOD-02 | Definition of Done | DOD-02: histórico maior que 200 é alcançável sem lacunas/repetições, inicial recente, empates estáticos e inserções empatadas durante recuperação. | PostgreSQL + source-owned Playwright | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | 251IDs ordenados e grupoT completo com H>T/lateID/dirty; full IDs DB/UI depois de cobertura; FRC10gatilhos×3rep,12frames/unread. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| DOD-03 | Definition of Done | DOD-03: autorização/cursor não permitem outra conversa, BU ou Mantenedora; recurso inacessível é 404 antes de query inválida. | PostgreSQL integration | test/atendimento.e2e-spec.ts:317,365; api-e2e-authority.log | Node22 / PG16 descartável | passed | Negativos distintos: outra conversa autorizada, outra BU da mesma Mantenedora sem grant e outra Mantenedora. |
| DOD-04 | Definition of Done | DOD-04: backfill, envio/refresh/close, troca rápida, reconexão sem evento posterior e recuperação mantêm histórico, posição, cursores, metadados e draft corretos. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Backfill/envio/close/contextos/reconnect/poll/draft/scroll, mais falha histórica+evento com restart recente sem novo trigger. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| DOD-05 | Definition of Done | DOD-05: limite/cursor/marcarLida, vazio/fim, falha/retry e recuperação pendente têm contrato/UI verificados; entradas posteriores à fronteira de abertura continuam não lidas. | PostgreSQL + Browser / Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Parser/escopo/neutralidade API224; loading/vazio/fim/retry/acesso e pendência browser; abertura+evento não se perde, empty>3pages+evento entre rodadas. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| DOD-06 | Definition of Done | DOD-06: suites API/Web/Playwright passam no backend real e banco isolado; plano SQL recente/profundo/empates registra custo e decisão de índice; migrate deploy validado se houver migração. | scripts + SQL + Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | API115unit/224E2E; Web20unit/36browser; FRC3; SQL20382rows/1000ties. Sem migration: índice candidato não justificou custo. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| DOD-07 | Definition of Done | DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão. | independent review + deterministic guards | delivery-adherence-resolution.json; delivery-tqa-causal-resolution.json; delivery-final.json; evidence/authority-final.json; evidence/completion-final.json; evidence/closeout-final.json; evidence/committed-source-attestation.json | checkout principal; API/Web feature; Foundation main; reviewers internos no-context | passed | Reviews terminais aceitos; fonte16 commitada idêntica à validada. Guardas de execução/conclusão/closeout rodados antes da transição final. |
| VAL-01 | Validation Steps | VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional. | runtime + migration | evidence/api-e2e-authority.log; evidence/attestation-browser-web-authority-revision5-final-full-20261015.json; execution-evidence.md | postgres:16-alpine / leadshug_timeline_20261014 | passed | 17 migrations; porta5432 somente rede Docker, sem host publish; DATABASE_URL explícita e guard de DB descartável antes do cleanup. |
| VAL-02 | Validation Steps | VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e. | scripts completos | evidence/api-ci-light-revision2-20261015.log; evidence/api-e2e-authority.log; evidence/executor-revision5-summary.json; execution-evidence.md | Linux Node22 / principal checkout | passed | npmci no volume Linux; rawgenerate/lint/build/unit115 retido; API224 serializado e mesmafonte7 até revision5. Sem browser concorrente no DB. |
| VAL-03 | Validation Steps | VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282,317,365,371; api-e2e-authority.log | PG16 dedicado | passed | 251 IDs e empates; negativos scoped e consulta inválida sem efeitos de leitura. |
| VAL-04 | Validation Steps | VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | npmci em volumesLinux; npmrunbuild/test/test:tela; Node22.23.3 e Nest/PG16 reais no mesmo DB descartável exclusivo. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| VAL-05 | Validation Steps | VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Autoria persistida, eventos/reconnect reais, close/contextos e todos os estados de recuperação. Counts3/max1, erros cobrados no despacho, restart histórico, seis efeitos de destino. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |
| VAL-06 | Validation Steps | VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado. | SQL EXPLAIN + API e2e | evidence/explain-timeline-exact.sql/.log; evidence/explain-index-trial.sql/.log; pcv-eps.json; atendimento.e2e-spec.ts | PG16 /20382 mensagens/1000 empatadas | passed | Recent1.094ms/deep3.442ms/tie0.850ms; trial composto deep3.942ms e9832buffers contra357 existente. Sem migration nova: condição de índice não demonstrou ganho. Risco de varredura profunda explícito; aceito em delivery-adherence-resolution.json, sem SLO de produção. |
| VAL-07 | Validation Steps | VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout. | review/security/performance/debt/guards | delivery-adherence-resolution.json; delivery-tqa-causal-resolution.json; delivery-final.json; pcv-eps.json/pcv-frc.json/pcv-bci.json/pcv-rls.json; verification-debt.md; evidence/authority-final.json; evidence/completion-final.json; evidence/closeout-final.json | Node22/PG16 descartável; Foundation; native no-context reviewers | passed | Segurança API224/escopo/ACK, PCV4passed, scans triados e dívida inline none; reviewers aceitos sem achados. Comandos dos guardas efetivos registrados no closeout. |
| VAL-08 | Validation Steps | VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha. | PostgreSQL + Browser / Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | ACK atômico10incrementos×3lotes e INposterior11; background neutro; abertura+INpreserva1; recuperação forte12; erros auth/query sem escrita. Navegador Chromium, Playwright mutation em branch non-main; build fresco/served==dist SHA7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Aderência/TQA aceitas; final review é gate separado. |

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Docker local | Runner e PostgreSQL isolado | healthy | 2026-10-14 | Daemon 27.1.1 respondeu | Containers operacionais não são alvos de testes. |
| Node.js 22 | Build/suites | healthy | 2026-10-14 | node.exe v22.22.2 disponível; node Linux ausente | Execução planejada em runner Linux Node 22 compatível com Dockerfiles; não misturar npm Windows com processos Linux. |
| Auditor interno TQA | Modelo prescrito gpt-5.6-terra | healthy | 2026-10-14 | codex exec ephemeral/read-only com effort max: exit0 MODEL_AVAILABLE; artifacts/tmp/inbox-timeline-execution/native-model-probe-events.jsonl | Usar runner nativo interno; nenhuma exceção de modelo é necessária. |
| Meta/Evolution externos | Interfaces de transporte preservadas | unknown | 2026-10-14 | Nenhum probe externo | Bootstrap de teste usa backend real e substitui somente portas externas; não enviar mensagens reais. |

Execução local planejada: runner Linux temporário Node 22, conforme imagens Node 22 dos Dockerfiles; PostgreSQL 16 descartável exclusivo deste TODO, com DB/porta registrados antes de E2E e DATABASE_URL explícita. Sem editar .env/Compose do produto. API e browser compartilham o mesmo DB de teste. A implementação pode acrescentar suporte de teste nos paths previstos; prontidão efetiva será provada antes da suite.

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Current profile:** Operational / Coder para execução delegada e consolidação local; Assurance / Tester-Quality para os gates independentes, mantendo owners serializados.
- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs, react, vite, postgresql, prisma, docker.
- **Handoff:** executor único implementa/testa API/Web; orchestrator mantém TODO/evidência; reviewers read-only nas fases derivadas.
- **Execution topology:** primary-checkout-single-writer; Foundation main, API/Web feature/inbox-timeline-pagination, sem worktrees.
- **Rule ingestion on 2026-10-14:** TODO, constituição/módulos e fontes da tabela Rules Acknowledgement recarregados após APROVADO; também boundary/orchestration e regras de schemas/migrations serão carregadas se houver índice.

## Complexity

- **Level:** medium
- **Checkpoint policy:** contrato e API, UI integrada, prova browser e closeout; cada checkpoint tem evidência afetada, sem alegar suite ampla antes de sua execução
- **Why this level:** alteração de API persistente consumida por UI com cursores, autorização e races de realtime

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** foundation_documentation/modules/inbox-and-conversations.md
- **Secondary module docs:** identity-and-tenancy.md e audit-and-history.md, para preservar invariantes
- **Consolidation target:** somente contrato local da thread e regras de cursor/paginação no módulo inbox-and-conversations
- **Source capability:** CAP-010 no catálogo ST-02, referência de evidência e não ID de capacidade canônica nova

## Decision Pending (Resolve Before Freeze)

Nenhuma decisão de produto permanece pendente: o usuário aprovou o contrato congelado com “APROVADO” em 2026-10-14. A implementação segue o recorte ST-ATT-01. A decisão condicional de índice depende dos planos SQL previstos; não amplia o contrato.

## Decisions (Resolved Before Freeze)

Decisões consolidadas após ARCH-TL-01..06 e aprovadas pelo usuário em 2026-10-14:

- Primeiro recorte BFF de mensagens na inbox; API pública, Consultar e demais stories ficam fora.
- Cursor anterior scoped, ordem createdAt/id, padrão 50 e teto 100. Não acrescentar cursor depois: ele não elimina a necessidade de sobreposição em timestamps empatados.
- Marcação atômica antes da consulta somente na abertura humana; refresh/backfill/recuperação são explicitamente read-neutral.
- Recuperação cruza integralmente o piso pendente de timestamp, preservado entre passagens coalescidas/retomadas/retry até cobertura sem trabalho concorrente; três queries por rodada, progresso/retry e reconexão/poll.
- Coleção por conversa, cursor de histórico separado do progresso de recuperação e versionamento local de metadados/efeitos; não criar framework ou cache de todas as conversas.
- Backend real, PostgreSQL descartável e providers fake somente nas portas externas; query plan obrigatório mesmo sem índice novo.
- Foundation main; código em branches locais com single writer; sem worktrees, deploy ou mensagens externas reais.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Decision | Source | Status | Handling / consolidation |
| --- | --- | --- | --- |
| Conversa única BU/contato | modules/inbox-and-conversations.md | preserved | Cursor consulta somente conversa autorizada. |
| Grants materializados na BU | modules/identity-and-tenancy.md | preserved | Negativos de tenant/BU no banco real. |
| Histórico e leitura scoped | modules/audit-and-history.md | preserved | Consulta de auditoria não ganha efeito de atendimento. |
| Janela/capability de envio | modules/inbox-and-conversations.md | preserved | Envio e API pública têm suites de regressão. |
| Paginação da thread | contrato proposto deste TODO | extend-local-contract | Contrato aprovado consolidado em modules/inbox-and-conversations.md antes da implementação. |

## Decision Baseline (Frozen Before Implementation)

Proposta técnica congelada para crítica em 2026-10-14 após integração ARCH-TL-01..06: superfície BFF, parâmetros/limites, reconhecimento atômico, recuperação bounded, estado por conversa, paths, DoD e provas reais deste TODO. A referência de versão publicada está em Gate: Review Baseline Freeze. O congelamento original não concedia implementação; a autorização posterior está registrada em Approval, pelo “APROVADO” explícito de 2026-10-14.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability:** required
- **Why this applies:** estabelece acesso paginado scoped e mesclagem consistente para uma thread operacional antes truncada
- **Deviation / debt being retired:** teto silencioso de 200 mensagens e substituição da coleção após refresh
- **Target steady-state after closeout:** acesso determinístico bounded e atualização sem perda de histórico/contexto
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** BFF e inbox adotam o contrato aprovado juntos, com regressões passando; nenhum fallback para carregar todas as mensagens

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

- **Architecture decision review:** required
- **Decision review status:** findings_integrated
- **Decision review evidence:** artifacts/reviews/leadshug-inbox-timeline-20261014/architecture-review.json; resolução ARCH-TL-01..06 neste TODO e critique-resolution.json verificam a integração no plano.
- **Architecture adherence review:** required
- **Adherence review status:** findings_integrated
- **Adherence review evidence:** delivery-adherence-round-1.json → delivery-adherence-delta.json → delivery-adherence-resolution.json, todos internos gpt-6.1-sol/max no-context, terminais turn.completed/schema/merge. ARCH-DEL-01..04/ERR corrigidos e aceitos, sem novo desvio. Revision5 altera apenas provas browser requeridas pela TQA; conservar parecer por identidade dos fontes de produto. Pacotes imutáveis generation1/revision3/revision4 em evidence/. Nenhum waiver.
- **Dedicated multi-lane audit:** not_needed pelo piso atual; não substitui crítica, segurança/performance, TQA e final review requeridos.

## Gate: Review Baseline Freeze

- **Gate decision:** required
- **Gate status:** no_material_findings
- **Baseline branch:** main
- **Baseline commit:** 649372fbe81f6cccc0f8902b52fe32e2ecfc061a
- **Baseline push reference:** origin/main
- **Evidence / reference:** git.exe push origin main completado; baseline 649372fb com integração ARCH-TL-01..06 e resolução da crítica publicado em 2026-10-14; git_write_authority_guard go para commit/push
- **Waiver authority / reference (required if waived):** none

## Gate: Review Scope Drift

- **Gate decision:** required
- **Gate status:** no_material_findings
- **Evidence / reference:** scope-drift.json documenta o freeze de planejamento antes de APROVADO; fidelity de execução foi julgada em delivery-adherence-resolution.json/final e no diff guard, sem desvio de produto
- **Waiver authority / reference (required if waived):** none

## Questions To Close

Aprovação do contrato resolvida: APROVADO em2026-10-14, após crítica convergida; ARCH-TL-03 foi integrado e confirmado no delta, com contraprova de execução agora registrada. Questões de transferência, mídia e status continuam nas stories posteriores; não serão resolvidas por esta implementação.

## Pattern References (Optional; Enforced When Cited)

n/a; nenhum ID de pattern é reivindicado.

## Assumptions Preview (Required Before Plan Review)

| ID | Assumption | Evidence | Risk | Validation / Impact | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Thread pega primeiras 200 mensagens | api-app/src/domain/inbox/conversations.service.ts:88 | Oculta recente | Fixture 251; query/contrato | Keep as Assumption |
| A-02 | Refresh substitui coleção da thread | web-app/src/telas/Inbox.tsx:59 | Perda de páginas | Browser envio/refresh/troca | Keep as Assumption |
| A-03 | API pública lista mensagens em query própria | api-app/src/surfaces/public/conversations.controller.ts:103 | Regressão contrato | Suites atuais sem mudança de shape | Keep as Assumption |
| A-04 | Helpers E2E apagam dados do banco apontado | api-app/test/helpers.ts:112 | Perda de dados | PostgreSQL dedicado descartável | Keep as Assumption |
| A-05 | Harness precisa corrigir caminho e provider determinístico para provar envio | web-app/playwright.config.ts:32; api-app/test/helpers.ts:68 | Suite inválida ou envio externo | Backend real com portas externas fake em suporte de teste | Keep as Assumption |

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
| Reconectar sem evento posterior | Burst acima de 100 e socket cortado | backend persiste; callback/poll recupera IDs completos | nenhuma mensagem extra para disparar a recuperação |
| Timestamps empatados | Cabeça H>T, grupo T maior que página, ID menor inserido atrás do cursor | Passagem coalescida conserva T e recupera todos os IDs | dirty durante caminhada e mais de três páginas não promovem piso prematuramente |
| Não lidas | IN antes/depois da abertura atômica | readback no PostgreSQL; background preserva contador | autorização/query inválida não escreve |
| Mesmo contexto em paralelo | Backfill atrasado e close/envio/refresh | cursor histórico e metadados/draft atuais preservados | resposta real atrasada não restaura estado |
| Trocar conversa/BU | Duas conversas e dois tenants | browser seleciona destino e conserva contexto | resposta antiga atrasada não substitui destino; sem grant falha |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Authority status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| API / CI api | BFF e parser alterados | npm ci; npm run prisma:generate; npm run lint; npm run build; npm test | Local-Implemented | passed | evidence/api-ci-light-revision2-20261015.log; execution-evidence.md | passed | Raw dos4leafsexit0/115unit; LinuxNode22,API7semalteração. Equivalente somente ao job API tocado. |
| API / PostgreSQL local adicional | Persistência/escopo/concorrência | npm run test:e2e | Local-Implemented | passed | api-e2e-authority.log; atendimento.e2e-spec.ts | passed | 224 testes/20 arquivos; DB exclusivo,17 migrations; não é claim de CI remoto. |
| Web / CI web | Consumidor/estado/realtime | npm ci; npm run build; npm test | Local-Implemented | passed | evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; execution-evidence.md | passed | LinuxNode22;Webunit20/browser36; source/build/served antes dos workers; prova local sem CI remoto. |
| Web / browser local adicional | Navegação/rolagem/races reais | npm run test:tela | Local-Implemented | passed | evidence/web-authority-revision6-final-full-20261015.log; evidence/attestation-browser-web-authority-revision6-final-full-20261015.json; execution-evidence.md | passed | LinuxNode22;Webunit20/browser36; source/build/served antes dos workers; prova local sem CI remoto. |

Compatibilidade de representação: completion guard lê status na coluna5, authority guard na coluna7. Os mesmos resultados são espelhados como Status/Authority status; notas permanecem na coluna8. Nenhuma validação ou comando é substituído.

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

- **Status:** findings_integrated; crítica inicial e resolução delta concluídas sem achados materiais pendentes.
- **Review output:** parecer de arquitetura no arquivo architecture-review.json.

### Issue Cards

| Finding ID | Severity | Scenario | Resolution | Status |
| --- | --- | --- | --- | --- |
| ARCH-TL-01 | high | Background zera não lidas; select/reset perde entrada concorrente | marcarLida=false e abertura atômica antes da query; VAL-08 | Integrated |
| ARCH-TL-02 | high | Socket retorna sem evento e thread não recupera | Callback de reconexão + poll da thread, paths de tempoReal explicitados | Integrated |
| ARCH-TL-03 | high | ID menor empatado pode entrar atrás do cursor após cabeça avançar | Cruzar grupo inteiro e conservar piso pendente T em todas as passagens coalescidas; promover só sem trabalho concorrente; teste H>T/ID atrás do cursor | Integrated; verified by critique delta |
| ARCH-TL-04 | medium | Mesmo contexto mistura cursores/metadados/draft | Estado mínimo com owners separados, geração e coalescing; races reais | Integrated |
| ARCH-TL-05 | medium | Índice existente aceito sem plano representativo | EXPLAIN obrigatório recente/profundo/empates mesmo sem migração | Integrated |
| ARCH-TL-06 | medium | Cursor errado não testado porque recurso já é 404 | Fixtures negativas distintas + browser backend real | Integrated |

### Residual Risks

Custo do grupo empatado é medido e cada rodada limitada; inserções concurrentes exigem nova passagem e UI de recuperação. Runners e suites serão provados na implementação. Nenhuma suite green ou aprovação material é presumida.

### Resultado da revisão pré-aprovação

- Revisão de arquitetura: seis achados integrados; crítica e delta encerrados sem achados materiais pendentes.
- Assumption code coherence: go; cinco premissas com fontes reais verificadas.
- Review scope drift: go; 23 seções comparadas, zero mudanças materiais após baseline 649372fb.
- Validação estrutural do TODO: PASS; lifecycle Foundation: exit 0.
- Authority preflight: preflight-go; execution_authority_granted=false.
- Evidências: artifacts/reviews/leadshug-inbox-timeline-20261014/README.md.
- Implementação e testes de aplicação continuam pendentes de autorização; nenhum gate de entrega é reivindicado.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

Parecer independente concluído em 2026-10-14, modelo gpt-6.1-sol/max, sem contexto herdado. Recomenda cursor anterior com fronteira inteira de timestamp e recuperação bounded com piso pendente conservado; alternativa bidirecional aumenta contrato sem resolver inserções empatadas. Resultado validado pelo subagent_review_merge; arquivo: artifacts/reviews/leadshug-inbox-timeline-20261014/architecture-review.json.

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
| high_severity_plan_review_issue | yes | ARCH-TL-01..03 reportados e integrados na proposta |
| explicit_three_lane_request | no | Revisão solicitada, sem pedido de três lanes |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

- **Critique decision:** required
- **Why this decision:** piso de audit_escalation_guard; API/escopo/realtime e UI com races.
- **Package mode:** bounded-file-set
- **Critique isolation mode:** fresh internal no-context reviewer; resolução delta pelo mesmo crítico independente, sem contexto de implementação.
- **Critique status:** findings_integrated
- **Gate status:** findings_integrated
- **Evidence / reference:** artifacts/reviews/leadshug-inbox-timeline-20261014/critique-round-1.json e critique-resolution.json; primeiro parecer reabriu ARCH-TL-03; delta verificou resolução e retornou findings vazio. Baseline revisada 649372fb.
- **Waiver authority / reference:** none

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-TL-03 | Integrated | useful | yes | project | n/a | Piso pendente T conservado entre passagens/dirty/retry e promoção somente após cobertura sem evento pendente; crítica delta critique-resolution.json confirmou a resolução do plano, agora testada no browser. |

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** A-01..05 exigem evidência de código real antes de aprovação.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01,A-02,A-03,A-04,A-05
- **Gate status:** no_material_findings
- **Findings summary:** revisão independente confirmou A-01/A-02/A-04/A-05 e, no delta, A-03 na query própria do controller público.
- **Evidence / reference:** artifacts/reviews/leadshug-inbox-timeline-20261014/critique-resolution.json; execução do guard registrada no mesmo diretório.
- **Waiver authority / reference:** none

## Approval

- **Approved by:** usuário, APROVADO explícito nesta conversa em 2026-10-14, após revisão e preflight-go.
- **Approval scope:** implementar e validar ST-ATT-01 conforme contrato revisado: BFF paginado/read-neutral, inbox/realtime/recovery/estado e suporte de teste, eventual índice justificado por SQL e documentação/evidência/closeout. Executor routine-executor predeclarado autorizado pelo contrato aprovado.
- **Execution not authorized by approval:** transferência, mídia, estados, CRM/campanhas/Typebot, mudanças da API pública/Consultar, worktrees/cópias auxiliares e deploy/promoção remota de código.
- **Renewed approval required when:** objetivo, contrato, autorização, escopo, riscos ou validação mudarem materialmente; detalhes locais necessários ao mesmo contrato permanecem no TODO.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

Ingestão vinculante após APROVADO realizada em 2026-10-14; fontes da tabela recarregadas para execução, preservando contrato e guards.

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

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Subagent / delegation authorization:** executor autorizado por APROVADO de 2026-10-14; revisão independente já requerida pelo workflow local invocado
- **Git isolation authorization:** not-authorized
- **Guard outcome:** go
- **Guard evidence:** agent_role_routing_guard avaliado em 2026-10-14 para este único tuple; go de routing não é autorização de implementação

Review lane separado: formal-reviewer, architecture_opinion/critique, gpt-6.1-sol, max, declared. Guard de critique retornou go; guard específico será executado antes do dispatch de arquitetura.

## Decision Adherence Validation (Mandatory Before Delivery)

Aderência independente convergida em delivery-adherence-resolution.json (gpt-6.1-sol/max). Revision5 altera somente o teste e mantém os fontes de produto e o bundle aceitos. TQA resolução das novas provas permanece em execução.

| Decision | Status | Evidence |
| --- | --- | --- |
| Autorização antes de paginação/cursor; erros scoped | Adherent | API224, parser/cursor e controller; delivery-adherence-resolution.json. |
| Últimas N, N+1, ordem DB e cursor de conversa | Adherent | API224 e source identity7; delivery-adherence-resolution.json. |
| ACK atômico anterior à query; background neutro | Adherent | pcv-bci.json,3barreiras10incrementos/IN11,negativoACK e restauração; parecer aceito. |
| Coleção ativa por ID; piso T conservado e orçamento3 | Adherent | Inbox/timeline, Web36/FRC3; counts3/max1,erro-budget/restart, source invariance revision4aceita. |
| Contexto/metadados/draft/scroll e socket/poll | Adherent | Seis destinos,owner de errogeração/versão,reconnect/poll; aderência aceita; provasvazio/reconnectreforçadas aguardamTQA. |
| Índice condicionado ao EXPLAIN | Adherent |20382rows/1000ties, planos exatos e trial composto pior removido; pcv-eps.json e parecer aceito. |
| API pública/Consultar e outras stories fora | Adherent | DiffcontractAPI7/Web9, API224, sem mudança dos consumidores excluídos. |

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Canonical owner / decision | Implementation | Status |
| --- | --- | --- |
| inbox-and-conversations / thread BFF paginada | controller + timeline-pagination + ConversationsService.timeline | Adherent; contrato anterior ao código4cabc467,API224,parecer independente aceito. |
| inbox-and-conversations / recuperação e contexto | Inbox + timeline + tempoReal | Adherent; código revision4 aceito, mesmo produto na provaWeb36/FRC3; Verified local no módulo owner; TQA causal aceitou as provas atuais. |
| identity-and-tenancy / BU e grant | Resolver/AccessService existentes | Adherent; nenhuma decisão canônica mudou, negativos reais401/404/400 e readback. |
| audit-and-history / autoria e ações | responder/claim/close existentes | Adherent; autoria/audit preservados, regressões reais e destinations. |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface | Focus | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| Orquestrador / inspeção bounded | API auth/read-state e UI races; runner/frescor | passed | implementation-observations.md; execution-evidence.md; source manifest revision5 | fixed IMPL-01..14 e ARCH-DEL-01-ERR; sem P1/P2 aberto de produto | Correções fiéis comprovadas, produto aceito pela aderência; TQA independente ainda julga provas reforçadas. |
| CI API local | Leaf scripts do job tocado | passed | evidence/api-ci-light-revision2-20261015.log; evidence/api-e2e-authority.log; test-surface-admission.md | 0 falhas na execução final | generate/lint/build/unit115 e PostgreSQL224 adicionais, serializados. |
| Revisão independente | Aderência, segurança, desempenho e provável P1/P2 | passed | delivery-adherence-resolution.json; delivery-tqa-causal-resolution.json | no findings; P1/P2 anteriores fixed | Aderência/TQA convergidas; final review é gate separado antes de entrega. |

## Rule-Spirit Anti-Pattern Hunt

| Rule Surface | Lens | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| NestJS / parser e limites | Validação runtime, grant antes cursor, ACK e queries bounded | passed | API224; delivery-adherence-resolution.json; scansAPI finais | no findings materiais; hints HTTP acompanhados de readback | Sessão/grants/domínio/PG reais, ACKbarreira e sem mudança público/Consultar. |
| React / Inbox e socket | Owner/generation, piso T, cursor, lifecycle e poll | passed | delivery-adherence-resolution.json; Web36/FRC3; implementation-observations.md | fixed IMPL-01..14,ARCH-DEL-01..04/ERR | Sem cacheframework/fetchall/budgetrenewal; fonte de produto aceita inalterada. |
| Scan heurístico API/Web | Domínios/targets e bypass disfarçado | passed | scan-triage-api.json e scan-triage-web.json; rawscansAPI/Webrev5; aderência aceita | no findings materiais; API30/15 e Web42/21 triados | by-design/no-action para loopback/.test de fixture e regexHTML preexistente, sem allowlist/supressão; TQA é gate separado. |

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-TL-01..03 | high | release-blocker | fix in current TODO | Contrato de leitura/recuperação pertence à mesma story | fixed | architecture-review.json e Proposed API Contract, a verificar na crítica |
| ARCH-TL-04..06 | medium | release-blocker | fix in current TODO | Estado/consulta/provas necessários ao mesmo contrato | fixed | architecture-review.json e testes planejados, a verificar na crítica |
| ARCH-DEL-01 | medium | release-blocker | fix in current TODO | Budget3 por rodada deve abranger coalescing; evento não renova automaticamente consultas | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |
| ARCH-DEL-02 | medium | release-blocker | fix in current TODO | Thread inicialmente vazia e notificação entre rodadas devem conservar restart pendente até fetch recente | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |
| ARCH-DEL-03 | medium | release-blocker | fix in current TODO | Notificação durante abertura pertence à geração selecionada e deve recuperar sem esperar outroevento/poll | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |
| TQA-TL-01 | medium | release-blocker | fix with ARCH-DEL-01 | Mesmo defeito de budget/single-flight; harness deve contar requests e passagens em voo, não só comparar IDs | fixed | delivery-tqa-delta.json confirmou resolução com counts/maxinflight, seis destinos e stdout API leafs; API224 idêntico mantido. |
| TQA-TL-02 | medium | release-blocker | fix in current TODO | Prova de geração exige draft/erro/scroll/metadados do destino em trocas conversa/BU com sucesso/falha/backfill antigos | fixed | delivery-tqa-delta.json confirmou resolução com counts/maxinflight, seis destinos e stdout API leafs; API224 idêntico mantido. |
| TQA-EVID-03 | low | release-blocker | retain exact CI leaf outputs now | Lacuna de evidência do claim CI atual; repetir somente generate/lint/build/unit API com logs imutáveis antes do browser final | fixed | delivery-tqa-delta.json confirmou resolução com counts/maxinflight, seis destinos e stdout API leafs; API224 idêntico mantido. |
| ARCH-DEL-01-ERR | medium | release-blocker | fix with ARCH-DEL-01 | Variante objetiva: saldo era debitado após await; falha+dirty não debitava e permitia mais de3tentativas. Consumir no despacho e provar3aborts+eventos sem4aautomática; erro histórico com dirty deve conservar restart recente, não consumir a notificação ao retomar cursor antigo | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |

| ARCH-DEL-04 | medium | release-blocker | fix in current TODO | Retry bem-sucedido deve encerrar alerta do próprio recovery sem apagar erro posterior não relacionado; assert ausência no fim dos casos existentes | fixed | delivery-adherence-resolution.json confirmou ownership geração/versão e os3oracles de erro; revision4Web20/35,FRC3 sem achados novos. |

| ARCH-DEL-02-EVID | medium | release-blocker | repair tests in current TODO | TQA delta: burst futuro tornava IN mais antigo e cursor velho ainda alcançava IDs; semear passado, assert headread no resume e controle negativo | fixed | delivery-tqa-causal-resolution.json aceitou provas revision6, Web36/FRC3 e source identity; ARCH-DEL-02/03 de produto permanecem corrigidos. |
| ARCH-DEL-03-EVID | medium | release-blocker | repair tests in current TODO | TQA delta: falta reconnect real enquanto openingGET retido/threadnull; provar read-neutral sem outroevento/poll | fixed | delivery-tqa-causal-resolution.json aceitou provas revision6, Web36/FRC3 e source identity; ARCH-DEL-02/03 de produto permanecem corrigidos. |

| GIT-RAW-WS | low | by-design/no-action | preserve immutable evidence | Whitespace emitido por ferramentas em logs/pacotes deve permanecer byteexact para preservar hashes; prose e fonte são verificadas separadamente | accepted | evidence/git-whitespace-evidence-triage.json; nenhuma alteração de produto ou regra compartilhada |

## TODO Closeout Disposition

- **Disposition:** move-completed
- **Disposition reason:** limiar local concluído e guardas go; publicar evidências na Foundation main e mover o mesmo TODO após o push, sem promoção remota de produto.
- **Post-commit/push status:** pending
- **Next path/status action:** após push documental, mover para todos/completed/features e atualizar links/estado do mesmo TODO.

## Security Risk Assessment (Mandatory Before Delivery)

- **Gate decision:** required
- **Why this decision:** cursor, grants e mudança de contexto.
- Autorizar primeiro; resolver cursor na conversa; limitar sua forma/tamanho e queries. Testar cursor de outra conversa autorizada, outra BU sem grant no mesmo tenant e outro tenant, separadamente.
- Banco descartável dedicado; bootstrap com sessão/guards/domínio/persistência reais e dublês só nas portas externas. Não mascarar BFF nem expor suporte de teste em produção.
- API224 comprovou precedência401/404, cursor scoped400 e ausência de escrita em query inválida; testes negativos distintos e readback PostgreSQL. Parser rejeita array/repetição e limite/tamanho inválidos. Bootstrap/fixtures estão em test/, recusam DB não descartável, sem rotas de suporte em produção. Aderência round1 confirmou a fronteira API/segurança; delta julga efeitos de contexto Web corrigidos. Sem alegação de pentest ou provider externo validado.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Gate decision:** required
- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** medium
- **Why this level:** paginação e cursores alteram queries; abertura e entrada concorrem na contagem de não lidas; contexto/realtime/ações assíncronas atualizam o histórico visível. Nenhuma promessa de SLO/capacidade foi aprovada.
- **Current delivery stage at review time:** Pending
- Registro de classificação na execução do contrato aprovado; não expande funcionalidade nem reduz obrigações de validação.

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `medium` | `EPS-QUERY-SHAPE-CHANGED` | `before_local_implemented` | `EPS-E2` | `passed` | Custo depende da distribuição real de mensagens. | `none` |
| `FRC` | `frontend-race-condition-validation` | `required` | `medium` | `FRC-STALE-RESPONSE` | `before_local_implemented` | `FRC-E2` | `passed` | Estados assíncronos requerem provas determinísticas de overlap. | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `required` | `medium` | `BCI-LOST-UPDATE-RISK` | `before_local_implemented` | `BCI-E2` | `passed` | Reconhecimento e incrementos devem linearizar no PostgreSQL. | `none` |
| `RLS` | `runtime-load-stress-validation` | `recommended` | `medium` | `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED` | `before_production_ready` | `RLS-E1` | `passed` | Amostra local não estabelece capacidade de produção. | `none` |

### Lane Details

#### EPS

- **Trigger rationale:** consulta recente e keyset mudam ordenação, limite e predicado; classificar acesso, auditar caminhos e registrar EXPLAIN recente/profundo/empates mesmo sem migração.
- **Recorded at (UTC):** `2026-10-15T03:36:56Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running -> passed; artefato e medição aceitos no parecer independente delivery-adherence-resolution.json, sem mudança da fonte API.
- **Evidence object:**
  - `evidence_type`: `explain`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `explain-exact-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-eps.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `248ea237489683aaa67371eb58efecab9e237c9aac08e36f3717b064f4825dfc`
  - `sample_profile_id`: `EPS-SP-STRONG`
  - `acceptance_rule_id`: `EPS-A2`
  - `result_summary`: `Measured recent/deep/tied pages on20382 rows,1000 ties; existing index retained after candidate trial. Independently accepted by delivery-adherence-resolution.json; local scope only.`
  - `reviewer_id`: `delivery-adherence-resolution-native`

#### FRC

- **Trigger rationale:** backfill, recuperação, fechamento, envio e troca de contexto podem sobrepor respostas; uma recuperação em voo e contexto/geração/versionamento de draft protegem o estado.
- **Recorded at (UTC):** `2026-10-15T05:01:37Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running -> passed; provas revision6 e correções de oracles aceitas em delivery-tqa-causal-resolution.json, sem waiver.
- **Evidence object:**
  - `evidence_type`: `source-owned-playwright-real-backend-races`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-chromium-disposable`
  - `run_id`: `web-authority-revision6-final-frc3-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-frc.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `3148b1ccf77cc0d4f1f980b74077133878a735e20115c941c92313fecb55823c`
  - `sample_profile_id`: `FRC-SP-M`
  - `acceptance_rule_id`: `FRC-A1`
  - `result_summary`: `Web20unit/36browser and FRC3/3 passed on identical final source/build; scheduling, notification, error ownership and destination races independently accepted by delivery-tqa-causal-resolution.json. Local evidence, no production claim.`
  - `reviewer_id`: `delivery-tqa-causal-native-no-context`

#### BCI

- **Trigger rationale:** o UPDATE de reconhecimento precede a query, concorrendo com incrementos de entrada; incrementos posteriores devem permanecer não lidos e leituras de background nunca escrever.
- **Recorded at (UTC):** `2026-10-15T03:36:56Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running -> passed; artefato e medição aceitos no parecer independente delivery-adherence-resolution.json, sem mudança da fonte API.
- **Evidence object:**
  - `evidence_type`: `postgresql-overlap-probe`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `bci-ack-barrier-canonical-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-bci.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `5ff9ba52415aeb420acf1b805a7ccece7d59194c127b97aa3ce2e22af12842b4`
  - `sample_profile_id`: `BCI-SP-M`
  - `acceptance_rule_id`: `BCI-A1`
  - `result_summary`: `Three deterministic real PostgreSQL barrier batches retain10 increments after ACK; regression mutation fails10vs0 and exact source restoration passes. Independently accepted by delivery-adherence-resolution.json; local scope only.`
  - `reviewer_id`: `delivery-adherence-resolution-native`

#### RLS

- **Trigger rationale:** consultas sensíveis a índice e recuperação realtime têm pressão de runtime; amostra de leitura neutra medirá erros, limites e latência sem promessa de SLO.
- **Recorded at (UTC):** `2026-10-15T03:39:44Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running -> passed; artefato e medição aceitos no parecer independente delivery-adherence-resolution.json, sem mudança da fonte API.
- **Evidence object:**
  - `evidence_type`: `one-stage-authenticated-read-load`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `rls-read-stage1-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-rls.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `eb0ec62492de2af2d52c5dc40eaa1defc776d9996d62048d554ce890a9991939`
  - `sample_profile_id`: `RLS-SP-L`
  - `acceptance_rule_id`: `RLS-A1`
  - `result_summary`: `30/30 reads,5 concurrent×6; p50 23.36ms,p95 64.26ms,max68.5ms; page50,unread7 unchanged,251 messages unchanged,foreign malformed request404. Independently accepted by delivery-adherence-resolution.json; no production SLO claim.`
  - `reviewer_id`: `delivery-adherence-resolution-native`

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

Auditoria executada: artifacts/reviews/leadshug-inbox-timeline-20261014/verification-debt.md e evidence/verification-debt-pre-final.log. Helper lexical high/exit2 por termos do template/histórico; classificação manual: inline none, nenhum waiver/dívida material escondida de produto/testes. Gates independentes/guardas e consolidação ainda abertos, sem claim de closeout; reavaliar após convergência.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Audit decision:** required
- **Why this decision:** API/escopo/consulta e UI interativa com races
- **Audit status:** findings_integrated
- **Critique status:** findings_integrated
- **Evidence / reference:** delivery-tqa-round-1.json → delivery-tqa-delta.json → delivery-tqa-resolution.json → delivery-tqa-causal-resolution.json e merges. Quatro reviews internos no-context gpt-5.6-terra/max, terminais turn.completed, rubric completo. O catálogo nativo suporta o modelo prescrito; guard go e probe registrados, sem substituição. Produto revision4 aceito na aderência, somente testes alterados em revision5/6; Web20/36,FRC3 revision6 e16hashes/bundle conferidos. Pacotes imutáveis em evidence/.
- **Waiver authority / reference:** none

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| TQA-TL-01 | Integrated | useful | yes | project | n/a | Budget3/max1 inclusive falha/evento, negativos3vs5 e restart2vs1, IDs/unread; delta confirmou. |
| TQA-TL-02 | Integrated | useful | yes | project | n/a | Seis destinos conversa/BU×sucesso/falha/backfill com draft/erro/scroll/metadados; delta confirmou. |
| TQA-EVID-03 | Integrated | useful | no | none | n/a | Stdout4leafsAPI115 retido e API224 mesmafonte; delta confirmou. |
| ARCH-DEL-02 | Integrated | useful | yes | project | n/a | Ledger ARCH-DEL-02-EVID: backlog passado, headrequest semantes/neutra, status IN_SERVICE/162IDs/unread2 e negativo oldcursor falha; resolução TQA aceitou. |
| ARCH-DEL-03-EVID | Integrated | useful | yes | project | n/a | Ledger ARCH-DEL-03-EVID: primeiroframe autenticado antesseleção; socket nativo fechado/reconectado durante openingGETretido, segundoframe antesrelease, sem outroevento/poll e negativo reconnect-only falha; TQA causal aceitou. |

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Final review decision:** required
- **Why this decision:** API/escopo/consulta e UI interativa com races
- **Final review status:** no_material_findings
- **Critique status:** no_material_findings
- **Evidence / reference:** delivery-final.json/merge, interno fresh no-context gpt-6.1-sol/max, turn.completed/schema/merge, findings vazio. Aceitou produto/revisões/TQA/PCV/segurança/dívida e escopo local; remanescentes apenas guardas/commits/registros de closeout. Nenhum waiver.
- **Waiver authority / reference:** none

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** not_needed
- **Cutover audit status:** no_material_findings
- **Why this decision:** recorte de paginação no BFF/inbox atuais; não há substituição de runtime legado, dual-read/dual-write ou exceção de compatibilidade temporária.
- **Evidence / reference:** Out of Scope e pareceres de arquitetura/crítica mantêm o produto atual como alvo único; nenhuma auditoria de cutover reivindicada.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Entrega local-only; sem autorização de publicação, promoção operacional ou claim Production-Ready. SLO, tráfego/provider externo e capacidade de produção não foram validados.

## Module Consolidation Gate (Required Before `Completed`)

Contrato consolidado antes do código no owner modules/inbox-and-conversations.md; coleta atualAPI115/224,Web20/36,FRC3 e SQL/BCI/RLS pronta. Estado Verified local consolidado no owner com API115/224,Web20/36,FRC3,SQL/BCI/RLS e aderência/TQA aceitas. Commits locais APIae6a9662c29b77276351aa9de653a47276372246 e Web4e56f6c1f4515b918d05b8c87e890d42e8542c56 conferidos em evidence/committed-source-attestation.json; outros módulos preservam decisões.

## Commands (Run Locally)

Comandos exatos e resultados efetivos: artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md. API generate/lint/build/unit115/E2E224 passou em Node22/PG16 descartável; EPS/BCI/RLS executados com artefatos; Web revision6 passou20unit/36browser/FRC3; aderência/TQA/final aceitos. Fonte16 commitada com bridge hash e guardas de closeout específicos. Nunca apontar helpers para bancos operacionais.

## Files Expected (Compatibility Note)

O contrato de paths e baselines está no Diff Expectation Contract.

## COMENTÁRIO:

n/a; nenhum comentário pendente do usuário neste arquivo.
