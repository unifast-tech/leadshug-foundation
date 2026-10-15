# Self-contained bounded delivery audit package ST-ATT-01
Fresh internal no-context technical reviewer. All applicable contract, touched sources, test sources, real evidence and rubric are embedded. Findings first, with exact locus/causal counterexample. Do not invent executions. Review framing: medium, Architecture/Code Quality/Tests/Performance/Security. This is local branch delivery, no deployment, no remote CI claim. Files are consolidated in the principal checkout; one product-code writer.

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-package.md

```
# Pacote bounded de revisão de entrega ST-ATT-01

Estado: fonte congelada, execução completa e atestada em2026-10-15; gates independentes a executar. Executor confirmou ausência de edição/teste em curso. Este artefato deriva autoridade/evidência, não concede aprovação nem altera produto.

## Autoridade e invariantes

Usuário aprovou “APROVADO” em 2026-10-14. TODO: foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md. Baseline técnica de planejamento publicada: 649372fbe81f6cccc0f8902b52fe32e2ecfc061a. Aprovação/canon e classificação PCV registrados em Foundation 4cabc467. Leia TODO completo, constituição, módulo inbox-and-conversations e somente os módulos identity-and-tenancy/audit-and-history quando necessários.

Recorte: histórico da inbox ST-ATT-01. Não redesenhar transferência, ownership, anexos, status, Typebot, branding, API pública, Consultar, incoming, infra/CI ou deploy. API e Web estão em feature/inbox-timeline-pagination no checkout principal, um executor de código. Não há worktree, cópia de repo ou ambiente de produção em prova.

Contrato obrigatório: autorização antes query/cursor; 1..100/default50, antes scoped/versionado; abertura humana com único UPDATE atômico antes da página, background read-neutral; `(createdAt,id)` e N+1. UI por conversa/ID; backfill e recuperação têm cursores distintos; recuperação conserva piso T mesmo após H>T e dirty, atravessa todo grupo T, máximo3 queries/rodada, uma passagem em voo, pendência/retry visíveis. Contexto/geração/versionamento protege metadados/draft/erros/scroll. Callback de conexão/reconexão sem evento adicional; poll60s.

## Fontes permitidas

- Diff API desde 5db3fbe2043428749895fc3ff6441e9457467dd0 e Web desde 6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9, incluindo arquivos novos ainda não staged.
- API src/domain/inbox/conversations.service.ts, src/domain/inbox/*pagination*.ts/spec.ts, src/surfaces/bff/conversations.controller.ts, test/atendimento.e2e-spec.ts, test/*timeline*.e2e-spec.ts, test/browser-server.cjs, test/timeline-fixtures.cjs; schema e eventual migração *timeline*; manifest/vitest config/infra bootstrap/helper de teste para conferir wiring.
- Web src/api.ts, src/telas/Inbox.tsx, src/*timeline*, src/tempoReal.ts/spec.ts, src/estilo.css, e2e/telas.spec.ts, e2e/*timeline*.spec.ts, e2e/timeline-freshness.ts, playwright.config.ts; manifest/vitest config/config.ts somente para conferir runner e endpoints.
- API controller público/Consultar e IncomingService somente como consumidores/invariantes preservados; não são autorização de diff.
- Foundation TODO, módulo canônico, brief, backlog e este diretório de revisão. architecture-review.json/critique-resolution.json documentam contrato aprovado; implementation-observations.md documenta inspeção preliminar, sem substituir revisão independente.
- Delphi skills: test-quality-audit, verification-debt-audit, ci-equivalent-governance, review-finding-classification; regras NestJS/React e PCV-1 para rubric específico.
- .github/workflows/ci.yml somente leitura para conferir jobs API/Web declarados.

Não ler .env/secrets/dados operacionais ou corpus histórico sem relação. Não editar código/docs, executar git writes, instalar novas dependências ou alterar runtime/DB. Probes adicionais dependem de coordenação do executor e usam somente o banco descartável declarado.

## Validação e frescor

Fontes/provas congeladas: execution-evidence.md e evidence/executor-final-summary.json. API: lint/build/generate/unit115 exit0 (stdout de CI observado mas não preservado, attestation explícita), E2E224/224 em111.92s, log bruto retido. Web: unit20/20, fullbrowser31/31 em48.6s e FRC10 gatilhos×3 repetições (3/3). Node22.23.3, Chromium Playwright1.62.1, PG16 dedicado17 migrations; somente portas externas falsas. Attestations full-final31-20261015 e frc-strong-final-20261015 capturadas antes dos workers têm todos16 hashes de fonte idênticos e JS servido==dist549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8. CLI scripts/configs/package owners e CI declarada estão no pacote.

EPS:20382 mensagens/ties1000, EXPLAIN equivalente recente1.094ms/profundo3.442ms/tie0.850ms; índice composto trial piorou deep3.942ms/9832buffers versus357 e foi removido; sem schema/migration nova, residual de varredura profunda declarado. BCI:3 barreiras PostgreSQL reais,10 incrementos cada após ACK durante SELECT bloqueado; todos permanecem, IN seguinte11. Mutação ACK depois SELECT falha10vs0; fonte restaurada byte-exata e caso canônico1/1 green. RLS:30 reads,5concorrentes×6,p95=64.26ms,zeroerros/unread/history inalterados; uma etapa local sem SLO prometido.

PCV pcv-eps/frc/bci/rls.json contêm payloads/hashes; estado running até sua avaliação independente, reviewer_id destinado delivery-adherence-native. Testes/statuses/artefatos históricos invalidados não são autoridade. Cobertura e limites da coleta estão explícitos; examine-os criticamente. Pré-review P1/P2/rule-spirit estão running e serão concluídos com seu parecer. Assess também o mapeamento transparente do guard Flutter-only para runner React npm run test:tela, sem inventar execução Flutter; os testes reais e a obrigação de prova não são reduzidos.

## Parecer solicitado

Achados primeiro, severidade/locus/contraprova/recomendação concreta. Não presumir green, aprovação de exceções ou completude pela prosa do TODO. Julgar código e evidência atuais contra o contrato congelado. Relatar proteção arquitetural ausente, divergência, regressão, isolamento/read-state, custo SQL, orçamento/amplificação, races/scroll/draft e fragilidade de testes. Incluir segurança, performance, Pipeline/Copilot P1/P2 e rule-spirit como lentes de suporte; revisão formal de testes/final permanecem gates distintos.

Para TQA executar todo rubric aplicável: alinhamento produto/testes; risco de workaround/retrofit; eficácia/eficiência de asserts; suficiência; fail-first/test-after honesto; comandos/topologia/frescor; DI real com dublês só de portas externas; flags skip/only/fallback; positivos/negativos/readback; fixture owned; suites completas. Não aceitar status-only, scroll>=0 ou inserção late-tie antes da caminhada como prova dos critérios fortes.

Retornar JSON canônico conforme dispatch, sem arquivos modificados. Nenhuma revisão de entrega foi concluída na preparação deste pacote.

## Static audit support
Final rule-spirit source-only scan: API30 observations/15 loci; Web42/21. Scan triage JSONs are inline in the self-contained packet, no allowlist/suppression. Test-quality static API exit0 (one status hint paired with readback), Web exit2 (six status hints paired with later business assertions; migration COUNT rows[0] aggregate is not ambient fixture selection). Independently evaluate these signals; the scans do not decide gate sufficiency.

```

## foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md

```
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

- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** concluir suites e provas PostgreSQL/browser, revisar independentemente e resolver achados antes do closeout.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** review
- **Why this state now:** fonte congelada, suites/probes completos e atestados; gates de aderência/TQA/final em curso.
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

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

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
- [ ] DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão.

## Validation Steps

- [x] VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional.
- [x] VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e.
- [x] VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos.
- [x] VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL.
- [x] VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada.
- [x] VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado.
- [ ] VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout.
- [x] VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha.

## Completion Evidence Matrix (Required Before Delivery Claim)

Um registro por critério de Scope, Definition of Done e Validation Steps; texto integral preserva rastreabilidade. Status não são promovidos por resultado intermediário ou execução contaminada.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API. | doc | Foundation4cabc467 + modules/inbox-and-conversations.md | Foundation main | passed | Contrato consolidado antes do executor alterar API; não é só nota tática. |
| SCOPE-02 | Scope | Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor. | PostgreSQL integration | test/atendimento.e2e-spec.ts:317,365,371; api-e2e-authority.log | Node22 / PG16 descartável | passed | Cursor alheio em recurso autorizado400; recurso sem grant404 antes da query; sem sessão401; unread readback preservado. |
| SCOPE-03 | Scope | Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282; api-e2e-authority.log | Node22 / PG16 descartável | passed | 251 IDs, limite37 e grupo empatado; comparação de IDs na ordem real do banco, página recente e continuação bounded. |
| SCOPE-04 | Scope | Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID. | Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | carregar anteriores,251IDs,mesclar envio e âncora estável inclusive chegada em await; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| SCOPE-05 | Scope | Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada. | Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | troca de conversa e BU durante resposta real POST atrasada; destino conserva seleção/coleção/draft; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| SCOPE-06 | Scope | Preservar histórico, cursor histórico, metadados atuais e draft correto durante envio, claim, close, backfill, poll e eventos/reconexão de socket. | Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | close vence backfill; envio/autoria/draft; reconexão sem evento; poll retoma cursor; IDs completos; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| SCOPE-07 | Scope | Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens. | PostgreSQL + source-owned Playwright | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | fixture251,empates>página,limites/cursores/escopo e11 cenários timeline; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| SCOPE-08 | Scope | Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo. | source + integration | playwright.config.ts + test/browser-server.cjs + test/timeline-fixtures.cjs; execution-evidence.md | backend Nest real / DB exclusivo | passed | Path ../api-app; somente Meta/Evolution fake, sem flags ou rotas de teste no entrypoint de produção; autoria persistida observada. |
| SCOPE-09 | Scope | Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado. | SQL EXPLAIN + API e2e | evidence/explain-timeline-exact.sql/.log; evidence/explain-index-trial.sql/.log; pcv-eps.json; atendimento.e2e-spec.ts | PG16 /20382 mensagens/1000 empatadas | passed | Recent1.094ms/deep3.442ms/tie0.850ms; trial composto deep3.942ms e9832buffers contra357 existente. Sem migration nova: condição de índice não demonstrou ganho. Risco de varredura profunda explícito; avaliação independente pendente. |
| DOD-01 | Definition of Done | DOD-01: contrato aprovado e consolidado no módulo responsável. | doc | TODO + modules/inbox-and-conversations.md | foundation | passed | APROVADO explícito e contrato consolidado em modules/inbox-and-conversations.md. |
| DOD-02 | Definition of Done | DOD-02: histórico maior que 200 é alcançável sem lacunas/repetições, inicial recente, empates estáticos e inserções empatadas durante recuperação. | PostgreSQL + source-owned Playwright | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | 251IDs ordenados e grupoT/H>T/lateID após cursor,10eventos×3; comparação DB/UI completa; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| DOD-03 | Definition of Done | DOD-03: autorização/cursor não permitem outra conversa, BU ou Mantenedora; recurso inacessível é 404 antes de query inválida. | PostgreSQL integration | test/atendimento.e2e-spec.ts:317,365; api-e2e-authority.log | Node22 / PG16 descartável | passed | Negativos distintos: outra conversa autorizada, outra BU da mesma Mantenedora sem grant e outra Mantenedora. |
| DOD-04 | Definition of Done | DOD-04: backfill, envio/refresh/close, troca rápida, reconexão sem evento posterior e recuperação mantêm histórico, posição, cursores, metadados e draft corretos. | Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | backfill/close/envio/BU/conversa/scroll/draft/reconnect/poll; respostas reais atrasadas e readback; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| DOD-05 | Definition of Done | DOD-05: limite/cursor/marcarLida, vazio/fim, falha/retry e recuperação pendente têm contrato/UI verificados; entradas posteriores à fronteira de abertura continuam não lidas. | PostgreSQL + Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | parser400/escopo404 antesquery,loading/vazio/fim/retry/acessoperdido; ACKbarreira10×3,INposterior11; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| DOD-06 | Definition of Done | DOD-06: suites API/Web/Playwright passam no backend real e banco isolado; plano SQL recente/profundo/empates registra custo e decisão de índice; migrate deploy validado se houver migração. | scripts + SQL + Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | APIunit115/E2E224;Webunit20/browser31;SQL20382/ties1000;sem migration justificada,trial removido; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| DOD-07 | Definition of Done | DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão. | review | VAL-07 | foundation | planned | Gates não executados. |
| VAL-01 | Validation Steps | VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional. | runtime + migration | api-e2e-authority.log + attestation-browser-full-final-20261015.json; execution-evidence.md | postgres:16-alpine / leadshug_timeline_20261014 | passed | 17 migrations; porta5432 somente rede Docker, sem host publish; DATABASE_URL explícita e guard de DB descartável antes do cleanup. |
| VAL-02 | Validation Steps | VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e. | scripts completos | api-e2e-authority.log; execution-evidence.md | Linux Node22 / principal checkout | passed | npm ci no volume Linux; generate/lint/build/unit115/E2E224 exit0. Sem execução simultânea de browser no DB. |
| VAL-03 | Validation Steps | VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282,317,365,371; api-e2e-authority.log | PG16 dedicado | passed | 251 IDs e empates; negativos scoped e consulta inválida sem efeitos de leitura. |
| VAL-04 | Validation Steps | VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL. | Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | npmci volumeLinux;npmrunbuild/test/test:tela;Nestreal mesmo LEADSHUG_E2E_DATABASE_URL; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| VAL-05 | Validation Steps | VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada. | Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | e2e/timeline.spec.ts cenários1..11:autoria,eventos reais,close/contextos,reconnect,H>T/dirty/lateID,poll/scroll/draft;31/31; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |
| VAL-06 | Validation Steps | VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado. | SQL EXPLAIN + API e2e | evidence/explain-timeline-exact.sql/.log; evidence/explain-index-trial.sql/.log; pcv-eps.json; atendimento.e2e-spec.ts | PG16 /20382 mensagens/1000 empatadas | passed | Recent1.094ms/deep3.442ms/tie0.850ms; trial composto deep3.942ms e9832buffers contra357 existente. Sem migration nova: condição de índice não demonstrou ganho. Risco de varredura profunda explícito; avaliação independente pendente. |
| VAL-07 | Validation Steps | VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout. | test/runtime/review | Validation Steps e relatório específico na execução | local isolado / foundation | planned | Prova futura; não executada nesta revisão. |
| VAL-08 | Validation Steps | VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha. | PostgreSQL + Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-final31.log; evidence/attestation-browser-full-final31-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | atendimento.e2e:371/415/482 e timeline.spec.ts:108/133/168:background/read-neutral;3lotesACK,10incrementos preservados,IN=>11;errosauth/querysemescrita; Playwright mutation em branch non-main; web-app build fresco e served bundle SHA549f99... idêntico ao dist. |

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
- **Adherence review status:** not_run
- **Adherence review evidence:** executar após implementação, antes de Completed.
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
- **Evidence / reference:** executar após convergência da revisão contra o baseline publicado
- **Waiver authority / reference (required if waived):** none

## Questions To Close

Aprovação humana única do contrato final após crítica convergida; reabertura ARCH-TL-03 foi integrada no mesmo recorte e será verificada no delta. Questões de transferência, mídia e status continuam nas stories posteriores; não serão resolvidas por esta implementação.

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

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| API / CI api | BFF e parser alterados | npm ci; npm run prisma:generate; npm run lint; npm run build; npm test | Local-Implemented | passed | api-e2e-authority.log; execution-evidence.md | Linux Node22,115 unitários; equivalente somente ao job API tocado. |
| API / PostgreSQL local adicional | Persistência/escopo/concorrência | npm run test:e2e | Local-Implemented | passed | api-e2e-authority.log; atendimento.e2e-spec.ts | 224 testes/20 arquivos; DB exclusivo,17 migrations; não é claim de CI remoto. |
| Web / CI web | Consumidor/estado/realtime | npm ci; npm run build; npm test | Local-Implemented | passed | evidence/web-authority-final31.log; evidence/web-precheck-socket-fix.log; execution-evidence.md | LinuxNode22;Webunit20/browser31;attestation pré-workers source/build/served; prova local dos jobs/fluxos declarados, sem CI remoto. |
| Web / browser local adicional | Navegação/rolagem/races reais | npm run test:tela | Local-Implemented | passed | evidence/web-authority-final31.log; evidence/web-precheck-socket-fix.log; execution-evidence.md | LinuxNode22;Webunit20/browser31;attestation pré-workers source/build/served; prova local dos jobs/fluxos declarados, sem CI remoto. |

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

Inspeção de suporte em andamento; parecer independente ainda obrigatório.

| Decision | Status | Evidence |
| --- | --- | --- |
| Autorização antes de paginação/cursor; erros scoped | Adherent na inspeção | controller thread/resolver e atendimento.e2e:317/365; API224 passa. |
| Últimas N, N+1, ordem DB e cursor de conversa | Adherent na inspeção | ConversationsService.timeline e atendimento.e2e:282; parser unitário. |
| ACK atômico anterior à query; background neutro | Adherent na inspeção | timeline/updateMany antes findMany; teste PostgreSQL com SELECT bloqueado e mutação negativa. |
| Coleção ativa por ID; piso T conservado e orçamento3 | A confirmar no runtime final/review | Inbox.tsx + timeline.spec.ts forte H>T/lateID/dirty; prova inicial passou. |
| Contexto/metadados/draft/scroll e socket/poll | A confirmar no runtime final/review | IMPL-01..06/09/13 e cenários browser específicos. |
| Índice condicionado ao EXPLAIN | Pendente | Medições recente/profundo/empates serão registradas; não presumir índice existente suficiente. |
| API pública/Consultar e outras stories fora | Adherent na inspeção | Sem diff nesses consumidores; regressões API224. |

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Canonical owner / decision | Implementation | Status |
| --- | --- | --- |
| inbox-and-conversations / thread BFF paginada | controller + timeline-pagination + ConversationsService.timeline | Contrato consolidado em4cabc467 antes do código; implementação API validada. |
| inbox-and-conversations / recuperação e contexto | Inbox + timeline + tempoReal | Contrato preservado; consolidação Verified depende de browser final e review. |
| identity-and-tenancy / BU e grant | Resolver/AccessService existentes | Sem mudança canônica; negativos reais de escopo passaram. |
| audit-and-history / autoria e ações | responder/claim/close existentes | Sem alteração contratual; persistência e regressões cobertas. |

Revisão independente ainda deve julgar a correspondência e os riscos restantes.

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface | Focus | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| Orquestrador / inspeção bounded | API auth/read-state e UI races; runner/frescor | running | implementation-observations.md; execution-evidence.md | IMPL-01..14 | Correções no mesmo TODO; browser final, SQL e reviews ainda pendentes. |
| CI API local | Leaf scripts do job tocado | passed | api-e2e-authority.log; test-surface-admission.md | 0 falhas na execução final | generate/lint/build/unit115 e PostgreSQL224 adicionais, serializados. |
| Revisão independente | Aderência, segurança, desempenho e provável P1/P2 | pending | delivery-package.md preparado | Ainda não executada | Não declarar clean antes do parecer e tratamento de achados. |

## Rule-Spirit Anti-Pattern Hunt

| Rule Surface | Lens | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| NestJS / parser e limites | Validação runtime, grant antes cursor, ACK e queries bounded | running | código + API224; test-quality-static-api.log | Inspeção sem bypass; avaliação independente pendente | Fonte/guards/session/persistência reais, sem alterar público/Consultar. |
| React / Inbox e socket | Owner/generation, piso T, cursor, lifecycle e poll | running | implementation-observations.md e cenários browser | IMPL-01..06/09/13/14 | Correções fiéis ao contrato; aguardar prova final. |
| Scan heurístico API/Web | Domínios/targets e bypass disfarçado | running | scan-triage-api.json e scan-triage-web.json | API30 observações/15 loci; Web40/20 na primeira captura só de fontes | Proposta by-design para fixtures localhost/.test e regex estática preexistente; sem allowlist. Rerun na fonte final e revisão independentes pendentes. |

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-TL-01..03 | high | release-blocker | fix in current TODO | Contrato de leitura/recuperação pertence à mesma story | fixed | architecture-review.json e Proposed API Contract, a verificar na crítica |
| ARCH-TL-04..06 | medium | release-blocker | fix in current TODO | Estado/consulta/provas necessários ao mesmo contrato | fixed | architecture-review.json e testes planejados, a verificar na crítica |

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** contrato aprovado em implementação, provas de entrega ainda necessárias.
- **Post-commit/push status:** revisão publicada; registro de aprovação/contrato canônico em execução.
- **Next path/status action:** implementar, validar e revisar; mover para completed somente com evidência/guardas de closeout.

## Security Risk Assessment (Mandatory Before Delivery)

- **Gate decision:** required
- **Why this decision:** cursor, grants e mudança de contexto.
- Autorizar primeiro; resolver cursor na conversa; limitar sua forma/tamanho e queries. Testar cursor de outra conversa autorizada, outra BU sem grant no mesmo tenant e outro tenant, separadamente.
- Banco descartável dedicado; bootstrap com sessão/guards/domínio/persistência reais e dublês só nas portas externas. Não mascarar BFF nem expor suporte de teste em produção.
- API224 comprovou precedência401/404, cursor scoped400 e ausência de escrita em query inválida; testes negativos distintos e readback PostgreSQL. Parser rejeita array/repetição e limite/tamanho inválidos. Bootstrap/fixtures estão em test/, recusam DB não descartável, sem rotas de suporte em produção. Revisão independente de segurança segue pendente, sem alegação de pentest ou provider externo validado.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Gate decision:** required
- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** medium
- **Why this level:** paginação e cursores alteram queries; abertura e entrada concorrem na contagem de não lidas; contexto/realtime/ações assíncronas atualizam o histórico visível. Nenhuma promessa de SLO/capacidade foi aprovada.
- **Current delivery stage at review time:** Pending
- Registro de classificação na execução do contrato aprovado; não expande funcionalidade nem reduz obrigações de validação.

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `medium` | `EPS-QUERY-SHAPE-CHANGED` | `before_local_implemented` | `EPS-E2` | `running` | Custo depende da distribuição real de mensagens. | `none` |
| `FRC` | `frontend-race-condition-validation` | `required` | `medium` | `FRC-STALE-RESPONSE` | `before_local_implemented` | `FRC-E2` | `running` | Estados assíncronos requerem provas determinísticas de overlap. | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `required` | `medium` | `BCI-LOST-UPDATE-RISK` | `before_local_implemented` | `BCI-E2` | `running` | Reconhecimento e incrementos devem linearizar no PostgreSQL. | `none` |
| `RLS` | `runtime-load-stress-validation` | `recommended` | `medium` | `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED` | `before_production_ready` | `RLS-E1` | `running` | Amostra local não estabelece capacidade de produção. | `none` |

### Lane Details

#### EPS

- **Trigger rationale:** consulta recente e keyset mudam ordenação, limite e predicado; classificar acesso, auditar caminhos e registrar EXPLAIN recente/profundo/empates mesmo sem migração.
- **Recorded at (UTC):** `2026-10-15T03:36:56Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; execução observada e artefato consolidado, aguardando avaliação independente antes de passed.
- **Evidence object:**
  - `evidence_type`: `explain`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `explain-exact-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-eps.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `f20722cdaae0a7cddea80dbcb2df929035d742f47b49ab7f64a17444a9a79c83`
  - `sample_profile_id`: `EPS-SP-STRONG`
  - `acceptance_rule_id`: `EPS-A2`
  - `result_summary`: `Measured recent/deep/tied pages on20382 rows,1000 ties; existing index retained after candidate trial. Independent judgment pending.`
  - `reviewer_id`: `delivery-adherence-native`

#### FRC

- **Trigger rationale:** backfill, recuperação, fechamento, envio e troca de contexto podem sobrepor respostas; uma recuperação em voo e contexto/geração/versionamento de draft protegem o estado.
- **Recorded at (UTC):** `2026-10-15T03:42:20Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; full31 e FRC3 executados em fonte idêntica, aguardando julgamento independente antes de passed.
- **Evidence object:**
  - `evidence_type`: `source-owned-playwright-real-backend-races`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-chromium-disposable`
  - `run_id`: `frc-strong-final-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-frc.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `9206858a99052977dfb684109d540a1a9e2dd896a34182aea864b0cb3a8e8233`
  - `sample_profile_id`: `FRC-SP-M`
  - `acceptance_rule_id`: `FRC-A1`
  - `result_summary`: `10 real repeated incoming pushes×3 independent browser repetitions passed; original T survives H>T and dirty late-ID insertion. Full31/31 and poll-resume regression pass on identical final source/build. Independent judgment pending.`
  - `reviewer_id`: `delivery-adherence-native`

#### BCI

- **Trigger rationale:** o UPDATE de reconhecimento precede a query, concorrendo com incrementos de entrada; incrementos posteriores devem permanecer não lidos e leituras de background nunca escrever.
- **Recorded at (UTC):** `2026-10-15T03:36:56Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; execução observada e artefato consolidado, aguardando avaliação independente antes de passed.
- **Evidence object:**
  - `evidence_type`: `postgresql-overlap-probe`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `bci-ack-barrier-canonical-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-bci.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `93eeac265b3c77b17e6fee0cbd20223a56cbe44fe17489052b9b4feeffa37995`
  - `sample_profile_id`: `BCI-SP-M`
  - `acceptance_rule_id`: `BCI-A1`
  - `result_summary`: `Three deterministic real PostgreSQL barrier batches retain10 increments after ACK; regression mutation fails10vs0 and exact source restoration passes. Independent judgment pending.`
  - `reviewer_id`: `delivery-adherence-native`

#### RLS

- **Trigger rationale:** consultas sensíveis a índice e recuperação realtime têm pressão de runtime; amostra de leitura neutra medirá erros, limites e latência sem promessa de SLO.
- **Recorded at (UTC):** `2026-10-15T03:39:44Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; amostra executada, revisão independente pendente antes de passed.
- **Evidence object:**
  - `evidence_type`: `one-stage-authenticated-read-load`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `rls-read-stage1-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-rls.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `b9b05d0bd9127e4347e04685a91379924153c7c3a4f9b7445e8fa5ed9f548b3c`
  - `sample_profile_id`: `RLS-SP-L`
  - `acceptance_rule_id`: `RLS-A1`
  - `result_summary`: `30/30 reads,5 concurrent×6; p50 23.36ms,p95 64.26ms,max68.5ms; page50,unread7 unchanged,251 messages unchanged,foreign malformed request404. Review pending, no production SLO claim.`
  - `reviewer_id`: `delivery-adherence-native`

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

Pendentes contrato, runner, provas PostgreSQL/browser e revisões. Não reivindicar implementação ou fechamento com evidência histórica de outro TODO.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Audit decision:** required
- **Why this decision:** API/escopo/consulta e UI interativa com races
- **Audit status:** not_run
- **Critique status:** not_run
- **Evidence / reference:** revisão de entrega após testes completos; pacote de planejamento não substitui TQA. O roteamento technical_review exige gpt-5.6-terra. Na retomada, o catálogo nativo do Codex confirmou esse modelo, embora não seja selecionável via ferramenta collaboration. Será usado o runner interno subagent_review_run.py com o modelo prescrito e effort max; guard específico go em artifacts/tmp/inbox-timeline-execution/routing-tqa-native.json e probe nativo ephemeral/read-only exit0 MODEL_AVAILABLE (native-model-probe-events.jsonl). Exceção/substituição não é necessária e não foi presumida.
- **Waiver authority / reference:** none

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Final review decision:** required
- **Why this decision:** API/escopo/consulta e UI interativa com races
- **Final review status:** not_run
- **Critique status:** not_run
- **Evidence / reference:** pacote ainda prepared-pre-freeze; executar revisão no gate correspondente
- **Waiver authority / reference:** none

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** not_needed
- **Cutover audit status:** no_material_findings
- **Why this decision:** recorte de paginação no BFF/inbox atuais; não há substituição de runtime legado, dual-read/dual-write ou exceção de compatibilidade temporária.
- **Evidence / reference:** Out of Scope e pareceres de arquitetura/crítica mantêm o produto atual como alvo único; nenhuma auditoria de cutover reivindicada.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Module Consolidation Gate (Required Before `Completed`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Commands (Run Locally)

Comandos exatos e resultados efetivos: artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md. API generate/lint/build/unit115/E2E224 passou em Node22/PG16 descartável; browser final, medições e revisões ainda pendentes. Nunca apontar helpers para bancos operacionais.

## Files Expected (Compatibility Note)

O contrato de paths e baselines está no Diff Expectation Contract.

## COMENTÁRIO:

n/a; nenhum comentário pendente do usuário neste arquivo.


```

## foundation_documentation/project_constitution.md

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

## foundation_documentation/modules/inbox-and-conversations.md

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

Aprovado pelo usuário em 2026-10-14 no [TODO ST-ATT-01](../todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md). Este módulo é o owner do contrato; implementação e verificação são registradas no TODO. Estado de verificação inicial: Documented; nenhuma implementação/evidência de execução reivindicada neste momento.

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

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md

```
# Evidência de execução ST-ATT-01

Estado: fonte e provas de execução congeladas para revisão independente; gates de entrega ainda abertos. Fonte de produto no checkout principal, branches locais `feature/inbox-timeline-pagination`, um único executor `/root/timeline_executor_resume`. Foundation permanece `main`.

## API

`artifacts/tmp/inbox-timeline-execution/api-e2e-authority.log`: execução serializada Linux Node22 sobre PostgreSQL16 descartável `leadshug-timeline-postgres-20261014`, DB `leadshug_timeline_20261014`, 17 migrations. Comandos próprios: `npm run prisma:generate`, `npm run lint`, `npm run build`, `npm test` (17 arquivos, 115 testes) e `npm run test:e2e` (20 arquivos, 224 testes, 111.92s). Todos exit0, conforme attestation do executor em evidence/executor-final-summary.json. O stdout detalhado de generate/lint/build/unit foi observado no executor e não foi preservado separadamente; o log E2E completo foi retido. Essa limitação é explícita para os auditores. Instalação `npm ci` pertence ao provisionamento do volume de dependências Linux; não foi substituída por módulos Windows.

A suite inclui paginação de 251 IDs, limite/cursor/read-state, isolamentos de conversa/BU/Mantenedora e precedência de autorização, regressões dos consumidores e concorrência. O teste forte de reconhecimento bloqueia o SELECT real no PostgreSQL e observa dez incrementos após ACK em três lotes; o contador permanece10 depois da resposta e uma entrada real posterior eleva a11.

Controle de regressão test-after: `bci-mutation-control.log` mostra falha quando o reconhecimento é temporariamente movido para depois da leitura (expected10/received0). `bci-source-restored.sha256` registra restauração exata da fonte; `bci-canonical-after-mutation.log` registra cenário canônico1/1 passando após restauração. Não houve commit da mutação e não se alega TDD anterior à implementação.

## Navegador

Suite própria `npm run test:tela`, Chromium Playwright1.62.1/Noble com Node22.23.3, backend Nest real e mesmo DB descartável. Somente portas Meta/Evolution são substituídas por adapters determinísticos; sessão, guards, grants, domínio, persistência e WebSocket são reais. Atrasos usam respostas BFF reais; erros de rede são aborts explícitos; acesso perdido remove grant de fixture. Nenhum endpoint de teste existe no entrypoint de produção.

A prova final usa `evidence/web-authority-final31.log`: **31/31**,48.6s,exit0, incluindo11 cenários próprios da timeline e20 regressões de telas. O build foi reconstruído pelos webServers do runner antes dos workers. `evidence/attestation-browser-full-final31-20261015.json`, capturada em **2026-10-15T03:39:29.661Z**, registra branch@HEAD, diff e hashes de todos os fontes novos/alterados, manifests API/dist e JS servido==dist SHA256 `549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8`. Todos os16 fontes registrados (API7/Web9) foram conferidos byte a byte após a suite, sem divergência. Validação em `http://127.0.0.1:4173` dentro do runner descartável, API3100 e fixtures3101; nenhuma URL operacional foi usada.

O teste de poll avança o relógio do navegador em60s, retoma recuperação maior que3 páginas sem clicar Continue e compara IDs completos/read-state. O socket permanece estável durante mudanças de filtro/BU, protege callbacks após cleanup e notificações onopen; logout targeted5/5 e suite completa passaram. Unidade Web20/20 em3 arquivos; `web-precheck-socket-fix.log` contém build/unit e a suite browser reconstrói o consumidor final. FRC final: evidence/web-frc-strong-final-3x.log,3/3 em22.7s; attestation imutável frc-strong-final-20261015 capturada antes dos workers, fonte e bundle idênticos ao full31,10 gatilhos reais por repetição mais o gatilho inicial,11 frames exigidos em cada uma. pcv-frc.json liga políticas por ação e provas.

## Medições e revisão

`evidence/explain-timeline-exact.sql/.log`:20382 mensagens e1000 no maior empate. Planos equivalentes à produção, com âncoras constantes resolvidas antes da medição: recente1.094ms, profundo3.442ms (10001 removidas pelo filtro), empate0.850ms. Candidato composto medido no DB descartável: profundo3.942ms e9832buffers contra357 existente; removido, nenhuma migration justificada. A primeira captura com subqueries OFFSET dentro do EXPLAIN foi diagnóstico de seleção de âncora e não é evidência autoritativa. O custo ainda cresce com a profundidade do predicado OR; as medições locais não estabelecem capacidade de produção.

`evidence/rls-read-sample.log/.mjs`: uma etapa,5 leituras concorrentes×6 lotes,30/30 respostas200 com50 mensagens, p50=23.36ms,p95=64.26ms,max=68.5ms, zero erros; unread7 e251 mensagens preservados. Query inválida em conversa estrangeira devolveu404. O campo raw com nome MalformedCursor representa `limite=invalid`, como documentado em pcv-rls.json; cursores reais são cobertos no E2E API. Limiar de correção/limite/read-neutral fixado no runner; latência é observada, sem SLO de produção.

PCV: EPS/BCI/RLS têm artefatos JSON canônicos com SHA; FRC final também consolidado. Todos permanecem running aguardando julgamento independente. Architecture adherence, TQA e final review são obrigatórios; pareceres de planejamento não satisfazem esses gates. TQA usará `gpt-5.6-terra/max` no runner interno nativo verificado, sem waiver.

## Execuções invalidadas

API/browser simultâneos no mesmo DB, tentativas Node24, execuções interrompidas e diagnósticos parciais não contam para entrega. Logs são retidos para causalidade; nenhuma saída parcial, retry ou correção de fixture é rotulada como suite completa green. Não há claim de CI remoto, deploy, promoção de código ou capacidade de produção.

## Limitações de metadados e mapeamento de runners

O resumo bruto do executor identifica incorretamente a primeira execução220/222 como sobreposta ao browser; aquela falhou por duas expectativas de fixture e foi corrigida. A execução223/223 foi a sobreposta e é inválida. A autoridade final é224/224 serializada. Esta correção de indexação preserva o resumo bruto, os resultados e os logs; nenhuma execução é reclassificada green.

O guard compartilhado todo_completion_guard possui detecção de runner Playwright com literais de Flutter. Neste projeto React, a capacidade `run_web_navigation_smoke` é satisfeita pelo owner `web-app/package.json`, script **npm run test:tela**, conforme constituição e test-surface-admission.md. O nome genérico nos registros representa esse mapeamento explícito; nenhum script/caminho Flutter foi invocado ou adicionado. A evidência continua sendo31 testes source-owned Playwright, backend real, DB exclusivo, build/served fingerprint e mutações em feature branch. Revisores devem julgar a equivalência e não presumir um comando inexistente.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/test-surface-admission.md

```
# Admissão dos testes e significado da prova local

ST-ATT-01, 2026-10-14. Artefato derivado; não reivindica suites green antes dos relatórios de execução.

| Superfície | Owner / leaf command | Delta | Relação com CI / prova |
| --- | --- | --- | --- |
| API unit | api-app/package.json, `npm test` | parser/cursor e asserts scoped | CI API já usa este script; novos specs são descobertos por config própria sem wrapper divergente. |
| API real PostgreSQL | api-app/package.json, `npm run test:e2e` | contrato/paginação/neutralidade/overlap | Prova adicional obrigatória do TODO, script completo. Não há claim de inclusão no pipeline existente. |
| Web unit/build | web-app/package.json, `npm test` e `npm run build` | merge/piso/socket e consumidor tipado | CI Web já usa esses leaf commands; specs atuais pertencem à descoberta do runner. |
| Browser readonly/mutation | web-app/package.json, `npm run test:tela` | histórico/races/fixture/bootstrap/path correto | Suite completa adicional obrigatória. API Nest real, mesmo PG dedicado, provider fake somente nas portas externas. Não há claim de estágio remoto. |
| Runtime/bootstrap | playwright.config.ts, API test/browser-server.cjs e test/timeline-fixtures.cjs | rebuild/API path e recusa de DB não descartável | Test-only, fora de src/entrypoint de produção; fontes no checkout principal. Bundles construídos e prova de identidade do runtime exigidos. |

API e Web têm manifests donos auditados pelo node_capability_surface_audit, exit0, em artifacts/tmp/inbox-timeline-execution/api-capability-audit.json e web-capability-audit.json. Nenhum comando de aplicação foi executado por esse audit estático.

A CI-Equivalent deste recorte é limitada aos jobs API/Web tocados: install/lint/build/unit de API e install/build/unit de Web conforme .github/workflows/ci.yml. PostgreSQL e Playwright são validações locais adicionais, mais fortes e requeridas pelo TODO. Não declarar stage-full, pipeline remoto green ou promoção; não alterar .github, compose/env ou root gitlinks. API e Web estão em feature/inbox-timeline-pagination, não main, para provas de mutação.

Descoberta de testes usa os scripts/configs dos manifests. Fixtures e cleanup são executados no banco exclusivo leadshug_timeline_*, nunca herdados de ambiente operacional. Uma suite targeted permanece diagnóstico, e um teste adicionado depois de o processo carregar o arquivo exige resultado novo sobre a fonte consolidada. Os artefatos de execução devem registrar test-after/falhas observadas honestamente, evitando alegação retroativa de TDD.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/implementation-observations.md

```
# Observações preliminares da implementação

Inspeção de suporte do orquestrador em 2026-10-14/15, durante implementação e validação; revisão independente permanece um gate separado. Nenhuma conclusão de entrega reivindicada. Todos os pontos pertencem ao contrato já aprovado e foram enviados ao único executor.

| ID | Locus | Cenário / defeito observado | Correção solicitada | Situação |
| --- | --- | --- | --- | --- |
| IMPL-01 | Inbox.tsx/responder | `texto === textoEnviado` compara valores da mesma closure e limpa texto digitado durante await. | Ref/versão de input e prova browser de edição enquanto envio pendente. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-02 | Inbox.tsx/abrir e trocarBu | finally antigo descartado por geração deixa flags de envio/backfill presas no destino. | Reset das flags no novo contexto e prova de navegação com request atrasado. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-03 | Inbox.tsx/reconciliar | Thread vazia inicia múltiplas consultas fora do objeto de single-flight. | Usar o mesmo contexto de recuperação para vazio. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-04 | Inbox.tsx/executarRecuperacao catch | Erro tardio de conversa anterior escreve erro/pendência no destino. | Verificar geração e ID em respostas e erros. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-05 | tempoReal.ts/onopen | Só reconexão posterior dispara atualização, mas contrato inclui primeira conexão estabelecida. | Callback em todo onopen. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-06 | Inbox.tsx/carregarLista | Resposta de aba antiga da mesma BU pode sobrescrever aba nova. | Capturar filtro/contexto e rejeitar resultado antigo. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-07 | test/browser-server.cjs | Provider falso usa fake.enviadas, objeto define enviados; envio lançaria erro. | Uniformizar propriedade e validar persistência/autoria real no browser. | Correção presente; browser persistiu envio e autoria no PostgreSQL, sem chamar transporte externo. |
| IMPL-08 | Runner de validação compartilhando DB | Na retomada Playwright começou enquanto API E2E ainda executava; seed/deleteMany poderiam interferir. Agregado API223/223 e browser interrompido são diagnósticos inválidos. | Interromper browser, invalidar artefatos contaminados e executar API completa, depois Playwright, EXPLAIN e RLS serializados. | API completa serializada final: 20 arquivos / 224 testes, exit0, api-e2e-authority.log. Browser e medições são executados depois, sem concorrência de suites no DB. |

| IMPL-09 | Inbox.tsx/backfill/scroll | Capturar a posição antes de await ignora rolagem/chegadas enquanto a resposta real aguarda. | Capturar a âncora imediatamente antes de prepend; comparar deslocamento relativo do mesmo ID. | Confirmado no full31 final: mesmo ID/offset relativo com delta<2px, incluindo chegada durante await. |
| IMPL-10 | Runner browser | Imagem Playwright Noble fornece Node24; contrato exige Node22. | Derivar runner descartável com binário Node22 e manter browser/deps da versão instalada; sem Dockerfile do produto alterado. | Runner verifica v22.23.3 antes de executar; Node24 anterior é diagnóstico inválido. |
| IMPL-11 | test/atendimento.e2e-spec.ts | Assert 0..10 após chegadas concorrentes não distingue select-depois-reset. | Barreira PostgreSQL real: bloquear SELECT de messages depois do ack e executar 10 incrementos, três lotes. | API224 passa; controle negativo moveu ack depois do SELECT e falhou expected10/received0; restauração byte-exata e cenário canônico 1/1 passou. Não é alegação retroativa de TDD. |
| IMPL-12 | Freshness do browser | Attestation com nome fixo era sobrescrita por uma execução posterior. | Nome imutável por run_id, prova capturada no globalSetup antes dos workers e fonte/build/served SHA vinculados. | Full31 final e FRC3 têm attestations imutáveis pré-workers;16 hashes de fontes e bundle iguais conferidos após execução. |
| IMPL-13 | Inbox.tsx/effect realtime | Fullbrowser posterior: 29/30; logout encontrou handshake de socket ainda em curso. Efeito misturava carga/filtro/BU e recriação de socket. | Diagnosticar lifecycle e estabilizar socket com callbacks atuais; manter consumidores/cleanup, sem filtro que esconda erro de console. | Corrigido separando socket dos efeitos de carga/filtro/BU e protegendo callbacks após cleanup. Logout5/5, unidade lifecycle e full31 passaram. App/global exploratórios foram descartados, sem diff fora do recorte. |

| IMPL-14 | Inbox.tsx/poll60/reconciliar | Poll acionava reconciliar e zerava cursor de recuperação pendente; backlog maior que3 páginas repetiria a cabeça indefinidamente sem Continue. | Poll deve retomar cursor/piso pendentes; eventos/ações/conexão continuam marcando dirty. Provar avanço de60s no browser sem clique Continue. | Corrigido: poll retoma recuperação pendente, eventos mantêm dirty. Cenário específico avança60s sem Continue/evento adicional e compara382 IDs; targeted1/1 e full31 passaram. |

Essas observações não substituem architecture_adherence, test_quality_audit ou final_review independentes. A resolução final depende dos arquivos consolidados, testes e revisores.

```

## Tracked diff api-app from 5db3fbe2043428749895fc3ff6441e9457467dd0
```diff
diff --git a/src/domain/inbox/conversations.service.ts b/src/domain/inbox/conversations.service.ts
index c549098..002a002 100644
--- a/src/domain/inbox/conversations.service.ts
+++ b/src/domain/inbox/conversations.service.ts
@@ -9,6 +9,7 @@ import { PrismaService } from '../../infra/prisma/prisma.service';
 import { EVOLUTION_CLIENT, EvolutionClient } from '../../integrations/evolution/evolution.client';
 import { META_CLIENT, MetaClient } from '../../integrations/meta/meta.client';
 import { CanalDeOrigem } from './incoming.service';
+import { criarCursorTimeline, lerCursorTimeline } from './timeline-pagination';
 
 export const JANELA_MS = 24 * 60 * 60 * 1000;
 
@@ -86,24 +87,63 @@ export class ConversationsService {
     return { total, pagina, temMais: pagina * limite < total, conversas };
   }
 
-  /** Abrir a thread marca como lida — abrir É atender (diferente de Consultar). */
-  async thread(conversaId: string) {
-    const mensagens = await this.prisma.message.findMany({
-      where: { conversationId: conversaId },
-      orderBy: { createdAt: 'asc' },
-      take: 200,
+  /** Página bounded da timeline; o reconhecimento é uma atualização atômica anterior à leitura. */
+  async timeline(conversaId: string, limite: number, cursor: string | null, marcarLida: boolean) {
+    let ancora: { id: string; createdAt: Date } | null = null;
+    if (cursor) {
+      const decodificado = lerCursorTimeline(cursor);
+      if (decodificado.conversaId !== conversaId) {
+        throw new BadRequestException({
+          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
+        });
+      }
+      ancora = await this.prisma.message.findFirst({
+        where: { id: decodificado.mensagemId, conversationId: conversaId },
+        select: { id: true, createdAt: true },
+      });
+      if (!ancora) {
+        throw new BadRequestException({
+          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
+        });
+      }
+    }
+
+    if (marcarLida) {
+      await this.prisma.conversation.updateMany({
+        where: { id: conversaId }, data: { unreadCount: 0 },
+      });
+    }
+
+    const where = ancora
+      ? {
+          conversationId: conversaId,
+          OR: [
+            { createdAt: { lt: ancora.createdAt } },
+            { createdAt: ancora.createdAt, id: { lt: ancora.id } },
+          ],
+        }
+      : { conversationId: conversaId };
+    const encontradas = await this.prisma.message.findMany({
+      where,
+      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
+      take: limite + 1,
       select: {
-        id: true,
-        direction: true,
-        messageType: true,
-        content: true,
-        channelOrigin: true,
-        authorName: true,
-        createdAt: true,
+        id: true, direction: true, messageType: true, content: true,
+        channelOrigin: true, authorName: true, createdAt: true,
       },
     });
-    await this.prisma.conversation.update({ where: { id: conversaId }, data: { unreadCount: 0 } });
-    return mensagens;
+    const temAnteriores = encontradas.length > limite;
+    const messages = encontradas.slice(0, limite).reverse();
+    return {
+      messages,
+      paginacao: {
+        limite,
+        temAnteriores,
+        cursorAnterior: temAnteriores && messages.length
+          ? criarCursorTimeline(conversaId, messages[0].id)
+          : null,
+      },
+    };
   }
 
   /**
diff --git a/src/surfaces/bff/conversations.controller.ts b/src/surfaces/bff/conversations.controller.ts
index 22b50d1..e2f56cb 100644
--- a/src/surfaces/bff/conversations.controller.ts
+++ b/src/surfaces/bff/conversations.controller.ts
@@ -5,6 +5,7 @@ import { exigirPapelNaBu } from '../../domain/access/require-role';
 import { ConversationsService } from '../../domain/inbox/conversations.service';
 import { RegistroDeAtividade } from '../../domain/historico/registro.service';
 import { ator } from './setores.controller';
+import { validarConsultaTimeline } from '../../domain/inbox/timeline-pagination';
 
 const ABAS = ['QUEUED', 'IN_SERVICE', 'CLOSED'] as const;
 
@@ -46,8 +47,14 @@ export class ConversationsController {
   }
 
   @Get('conversations/:id/messages')
-  async thread(@Param('id') id: string, @Req() req: Request) {
+  async thread(@Param('id') id: string, @Query() q: Record<string, unknown>, @Req() req: Request) {
     const { conversa } = await this.resolver(id, req);
+    // Validar somente depois do resolver: recurso fora do escopo permanece 404,
+    // mesmo quando os parâmetros enviados são inválidos.
+    const consulta = validarConsultaTimeline(q);
+    const timeline = await this.conversas.timeline(
+      conversa.id, consulta.limite, consulta.antes, consulta.marcarLida,
+    );
 
     const janela = await this.conversas.estadoDaJanela(conversa.id, conversa.buId);
     return {
@@ -65,7 +72,8 @@ export class ConversationsController {
         expiraEm: janela.expiraEm,
         canal: janela.canal?.type ?? null,
       },
-      messages: await this.conversas.thread(conversa.id),
+      messages: timeline.messages,
+      paginacao: timeline.paginacao,
     };
   }
 
diff --git a/test/atendimento.e2e-spec.ts b/test/atendimento.e2e-spec.ts
index 41b0fde..1a73778 100644
--- a/test/atendimento.e2e-spec.ts
+++ b/test/atendimento.e2e-spec.ts
@@ -1,278 +1,506 @@
-import { INestApplication } from '@nestjs/common';
-import { createHmac } from 'node:crypto';
-import request from 'supertest';
-import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
-import { PrismaService } from '../src/infra/prisma/prisma.service';
-import {
-  META_APP_SECRET,
-  criarMantenedora,
-  criarUsuario,
-  evolutionFake,
-  limparBanco,
-  login,
-  metaFake,
-  subirApp,
-} from './helpers';
-
-describe('atendimento', () => {
-  let app: INestApplication;
-  let prisma: PrismaService;
-  let A: Awaited<ReturnType<typeof criarMantenedora>>;
-  let B: Awaited<ReturnType<typeof criarMantenedora>>;
-  let cookieOwner: string;
-  let conversaId: string;
-
-  const PHONE_A = 'phone-alfa';
-  const CONTATO = '5584911112222';
-
-  const receber = async (texto: string, phoneNumberId = PHONE_A) => {
-    const corpo = {
-      entry: [
-        {
-          changes: [
-            {
-              field: 'messages',
-              value: {
-                metadata: { phone_number_id: phoneNumberId },
-                contacts: [{ profile: { name: 'Cliente' } }],
-                messages: [{ id: `wamid-${texto}`, from: CONTATO, type: 'text', text: { body: texto } }],
-              },
-            },
-          ],
-        },
-      ],
-    };
-    await request(app.getHttpServer())
-      .post('/webhooks/meta')
-      .set('content-type', 'application/json')
-      .set('x-hub-signature-256', 'sha256=' + createHmac('sha256', META_APP_SECRET).update(JSON.stringify(corpo)).digest('hex'))
-      .send(corpo)
-      .expect(200);
-  };
-
-  const responder = (cookie: string, id: string, texto = 'oi, tudo bem?') =>
-    request(app.getHttpServer())
-      .post(`/api/bff/conversations/${id}/messages`)
-      .set('Cookie', cookie).set('x-requested-with', 'teste')
-      .send({ texto });
-
-  beforeAll(async () => {
-    ({ app, prisma } = await subirApp());
-  });
-
-  afterAll(async () => {
-    await limparBanco(prisma);
-    await app?.close();
-  });
-
-  beforeEach(async () => {
-    await limparBanco(prisma);
-    metaFake.enviados = [];
-    evolutionFake.enviados = [];
-    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
-    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');
-    await prisma.buChannel.create({
-      data: { buId: A.businessUnit.id, type: 'OFICIAL', phoneNumberId: PHONE_A, requiresWindow: true, status: 'CONECTADO' },
-    });
-    cookieOwner = await login(app, 'dono@alfa.test');
-    await receber('oi');
-    conversaId = (await prisma.conversation.findFirstOrThrow()).id;
-  });
-
-  describe('POST conversations/:id/messages — o trio (ADR-0012 §2)', () => {
-    it('autorizado: responde, envia pelo canal e assume a conversa', async () => {
-      const res = await responder(cookieOwner, conversaId).expect(201);
-      expect(res.body.canal).toBe('OFICIAL');
-      expect(metaFake.enviados).toEqual([{ para: CONTATO, texto: 'oi, tudo bem?' }]);
-
-      const conversa = await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
-      expect(conversa.status).toBe('IN_SERVICE');
-      expect(conversa.attendantOrigin).toBe('INTERNO');
-    });
-
-    // Os dois testes que aqui provavam CAPACIDADE_AUSENTE e "VIEWER lê mas não
-    // responde" SUMIRAM com o ADR-0018: o eixo de capacidades foi dissolvido e o
-    // papel VIEWER deixou de existir. Não é cobertura perdida — é comportamento
-    // que o produto não tem mais. A dívida está escrita no ADR §Negativas: quem
-    // precisa acompanhar sem responder passa a ser ATENDENTE, e nada o impede de
-    // responder; o substituto é o histórico de atividades (ADR-0020).
-
-    it('ATENDENTE no escopo responde — estar na BU BASTA (ADR-0018 §3)', async () => {
-      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'atendente@alfa.test', 'ATENDENTE');
-      const cookie = await login(app, 'atendente@alfa.test');
-
-      await responder(cookie, conversaId).expect(201);
-      expect(metaFake.enviados).toHaveLength(1);
-    });
-
-    it('CROSS-TENANT: o dono de Beta recebe 404 na conversa da BU de Alfa', async () => {
-      const cookieBeta = await login(app, 'dono@beta.test');
-      const res = await responder(cookieBeta, conversaId).expect(404);
-      expect(res.body.code).toBe('NAO_ENCONTRADO');
-      expect(metaFake.enviados).toHaveLength(0);
-      expect(B.businessUnit.id).toBeTruthy();
-    });
-  });
-
-  describe('janela de 24h — atributo do CANAL (ADR-0009 §3)', () => {
-    it('recusa com JANELA_FECHADA quando a última mensagem do contato passou de 24h', async () => {
-      await prisma.message.updateMany({
-        where: { conversationId: conversaId },
-        data: { createdAt: new Date(Date.now() - 25 * 60 * 60 * 1000) },
-      });
-
-      const res = await responder(cookieOwner, conversaId).expect(409);
-      expect(res.body.code).toBe('JANELA_FECHADA');
-      expect(metaFake.enviados).toHaveLength(0);
-    });
-
-    it('a thread informa o estado da janela, para a tela saber que responder está indisponível', async () => {
-      await prisma.message.updateMany({
-        where: { conversationId: conversaId },
-        data: { createdAt: new Date(Date.now() - 25 * 60 * 60 * 1000) },
-      });
-      const res = await request(app.getHttpServer())
-        .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
-
-      expect(res.body.janela).toMatchObject({ exigida: true, aberta: false, canal: 'OFICIAL' });
-    });
-
-    it('no canal NÃO oficial não existe janela: responde mesmo com a conversa velha', async () => {
-      const geral = await prisma.setor.findFirstOrThrow({ where: { mantenedoraId: A.mantenedora.id } });
-      const bu2 = await prisma.businessUnit.create({
-        data: { mantenedoraId: A.mantenedora.id, setorId: geral.id, name: 'Número não oficial' },
-      });
-      await prisma.buChannel.create({
-        data: { buId: bu2.id, type: 'NAO_OFICIAL', evolutionInstanceName: 'inst-alfa', requiresWindow: false, status: 'CONECTADO' },
-      });
-      await prisma.userBuRole.create({
-        data: {
-          userId: A.owner.id,
-          buId: bu2.id,
-          role: 'OWNER',
-          grantedViaTipo: 'MANTENEDORA',
-          grantedViaId: A.mantenedora.id,
-        },
-      });
-      const conversa = await prisma.conversation.create({
-        data: { buId: bu2.id, contact: '5584933334444', contactType: 'PESSOA', status: 'QUEUED' },
-      });
-      await prisma.message.create({
-        data: {
-          conversationId: conversa.id, buId: bu2.id, direction: 'IN', messageType: 'TEXTO',
-          content: 'antiga', channelOrigin: 'NAO_OFICIAL', status: 'RECEBIDA',
-          createdAt: new Date(Date.now() - 72 * 60 * 60 * 1000),
-        },
-      });
-
-      await responder(cookieOwner, conversa.id).expect(201);
-      expect(evolutionFake.enviados).toHaveLength(1);
-      expect(metaFake.enviados).toHaveLength(0);
-    });
-  });
-
-  describe('fila', () => {
-    it('assumir trava para outro agente (409), e finalizar libera', async () => {
-      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro@alfa.test', 'ATENDENTE');
-      const cookieOutro = await login(app, 'outro@alfa.test');
-
-      await request(app.getHttpServer())
-        .post(`/api/bff/conversations/${conversaId}/claim`)
-        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
-
-      const conflito = await request(app.getHttpServer())
-        .post(`/api/bff/conversations/${conversaId}/claim`)
-        .set('Cookie', cookieOutro).set('x-requested-with', 'teste').expect(409);
-      expect(conflito.body.code).toBe('JA_ATENDIDA');
-
-      await request(app.getHttpServer())
-        .post(`/api/bff/conversations/${conversaId}/close`)
-        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
-
-      await request(app.getHttpServer())
-        .post(`/api/bff/conversations/${conversaId}/claim`)
-        .set('Cookie', cookieOutro).set('x-requested-with', 'teste').expect(201);
-    });
-
-    it('responder NÃO rouba conversa de quem já está atendendo', async () => {
-      await request(app.getHttpServer())
-        .post(`/api/bff/conversations/${conversaId}/claim`)
-        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
-
-      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro2@alfa.test', 'ATENDENTE');
-      const cookieOutro = await login(app, 'outro2@alfa.test');
-      await responder(cookieOutro, conversaId, 'me intrometi').expect(201);
-
-      const conversa = await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
-      expect(conversa.attendantUserId).toBe(A.owner.id);
-    });
-
-    it('abrir a thread zera as não lidas — abrir É atender', async () => {
-      await receber('mais uma');
-      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(2);
-
-      await request(app.getHttpServer())
-        .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
-
-      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(0);
-    });
-
-    it('a lista filtra por aba e só enxerga a BU pedida', async () => {
-      const res = await request(app.getHttpServer())
-        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?aba=QUEUED`)
-        .set('Cookie', cookieOwner).expect(200);
-      expect(res.body.conversations).toHaveLength(1);
-
-      const emAtendimento = await request(app.getHttpServer())
-        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?aba=IN_SERVICE`)
-        .set('Cookie', cookieOwner).expect(200);
-      expect(emAtendimento.body.conversations).toHaveLength(0);
-    });
-  });
-
-  describe('a inbox pagina — teto silencioso é o que vira "sumiram conversas"', () => {
-    it('devolve total e temMais, e a segunda página traz o resto', async () => {
-      for (let i = 0; i < 5; i++) {
-        await prisma.conversation.create({
-          data: {
-            buId: A.businessUnit.id,
-            contact: `55119000000${i}0`,
-            contactType: 'PESSOA',
-            status: 'QUEUED',
-            lastMessageAt: new Date(Date.now() - i * 1000),
-          },
-        });
-      }
-
-      const p1 = await request(app.getHttpServer())
-        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=2`)
-        .set('Cookie', cookieOwner)
-        .expect(200);
-
-      expect(p1.body.conversations).toHaveLength(2);
-      expect(p1.body.total).toBeGreaterThanOrEqual(5);
-      // O que faltava: a resposta DIZ que há mais. Antes o take era 200 fixo e o
-      // corte era invisível.
-      expect(p1.body.temMais).toBe(true);
-
-      const p2 = await request(app.getHttpServer())
-        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=2&pagina=2`)
-        .set('Cookie', cookieOwner)
-        .expect(200);
-
-      expect(p2.body.pagina).toBe(2);
-      const ids1 = p1.body.conversations.map((c: { id: string }) => c.id);
-      const ids2 = p2.body.conversations.map((c: { id: string }) => c.id);
-      expect(ids1.some((id: string) => ids2.includes(id))).toBe(false);
-    });
-
-    it('limite acima do teto é aparado, não obedecido', async () => {
-      const r = await request(app.getHttpServer())
-        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=99999`)
-        .set('Cookie', cookieOwner)
-        .expect(200);
-      // Um cliente não escolhe quanto o banco carrega de uma vez.
-      expect(r.body.conversations.length).toBeLessThanOrEqual(200);
-    });
-  });
-});
+import { INestApplication } from '@nestjs/common';
+import { createHmac } from 'node:crypto';
+import request from 'supertest';
+import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
+import { PrismaService } from '../src/infra/prisma/prisma.service';
+import {
+  META_APP_SECRET,
+  criarMantenedora,
+  criarUsuario,
+  evolutionFake,
+  limparBanco,
+  login,
+  metaFake,
+  subirApp,
+} from './helpers';
+import { lerCursorTimeline } from '../src/domain/inbox/timeline-pagination';
+
+describe('atendimento', () => {
+  let app: INestApplication;
+  let prisma: PrismaService;
+  let A: Awaited<ReturnType<typeof criarMantenedora>>;
+  let B: Awaited<ReturnType<typeof criarMantenedora>>;
+  let cookieOwner: string;
+  let conversaId: string;
+
+  const PHONE_A = 'phone-alfa';
+  const CONTATO = '5584911112222';
+
+  const receber = async (texto: string, phoneNumberId = PHONE_A) => {
+    const corpo = {
+      entry: [
+        {
+          changes: [
+            {
+              field: 'messages',
+              value: {
+                metadata: { phone_number_id: phoneNumberId },
+                contacts: [{ profile: { name: 'Cliente' } }],
+                messages: [{ id: `wamid-${texto}`, from: CONTATO, type: 'text', text: { body: texto } }],
+              },
+            },
+          ],
+        },
+      ],
+    };
+    await request(app.getHttpServer())
+      .post('/webhooks/meta')
+      .set('content-type', 'application/json')
+      .set('x-hub-signature-256', 'sha256=' + createHmac('sha256', META_APP_SECRET).update(JSON.stringify(corpo)).digest('hex'))
+      .send(corpo)
+      .expect(200);
+  };
+
+  const responder = (cookie: string, id: string, texto = 'oi, tudo bem?') =>
+    request(app.getHttpServer())
+      .post(`/api/bff/conversations/${id}/messages`)
+      .set('Cookie', cookie).set('x-requested-with', 'teste')
+      .send({ texto });
+
+  beforeAll(async () => {
+    ({ app, prisma } = await subirApp());
+  });
+
+  afterAll(async () => {
+    await limparBanco(prisma);
+    await app?.close();
+  });
+
+  beforeEach(async () => {
+    await limparBanco(prisma);
+    metaFake.enviados = [];
+    evolutionFake.enviados = [];
+    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');
+    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');
+    await prisma.buChannel.create({
+      data: { buId: A.businessUnit.id, type: 'OFICIAL', phoneNumberId: PHONE_A, requiresWindow: true, status: 'CONECTADO' },
+    });
+    cookieOwner = await login(app, 'dono@alfa.test');
+    await receber('oi');
+    conversaId = (await prisma.conversation.findFirstOrThrow()).id;
+  });
+
+  describe('POST conversations/:id/messages — o trio (ADR-0012 §2)', () => {
+    it('autorizado: responde, envia pelo canal e assume a conversa', async () => {
+      const res = await responder(cookieOwner, conversaId).expect(201);
+      expect(res.body.canal).toBe('OFICIAL');
+      expect(metaFake.enviados).toEqual([{ para: CONTATO, texto: 'oi, tudo bem?' }]);
+
+      const conversa = await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
+      expect(conversa.status).toBe('IN_SERVICE');
+      expect(conversa.attendantOrigin).toBe('INTERNO');
+    });
+
+    // Os dois testes que aqui provavam CAPACIDADE_AUSENTE e "VIEWER lê mas não
+    // responde" SUMIRAM com o ADR-0018: o eixo de capacidades foi dissolvido e o
+    // papel VIEWER deixou de existir. Não é cobertura perdida — é comportamento
+    // que o produto não tem mais. A dívida está escrita no ADR §Negativas: quem
+    // precisa acompanhar sem responder passa a ser ATENDENTE, e nada o impede de
+    // responder; o substituto é o histórico de atividades (ADR-0020).
+
+    it('ATENDENTE no escopo responde — estar na BU BASTA (ADR-0018 §3)', async () => {
+      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'atendente@alfa.test', 'ATENDENTE');
+      const cookie = await login(app, 'atendente@alfa.test');
+
+      await responder(cookie, conversaId).expect(201);
+      expect(metaFake.enviados).toHaveLength(1);
+    });
+
+    it('CROSS-TENANT: o dono de Beta recebe 404 na conversa da BU de Alfa', async () => {
+      const cookieBeta = await login(app, 'dono@beta.test');
+      const res = await responder(cookieBeta, conversaId).expect(404);
+      expect(res.body.code).toBe('NAO_ENCONTRADO');
+      expect(metaFake.enviados).toHaveLength(0);
+      expect(B.businessUnit.id).toBeTruthy();
+    });
+  });
+
+  describe('janela de 24h — atributo do CANAL (ADR-0009 §3)', () => {
+    it('recusa com JANELA_FECHADA quando a última mensagem do contato passou de 24h', async () => {
+      await prisma.message.updateMany({
+        where: { conversationId: conversaId },
+        data: { createdAt: new Date(Date.now() - 25 * 60 * 60 * 1000) },
+      });
+
+      const res = await responder(cookieOwner, conversaId).expect(409);
+      expect(res.body.code).toBe('JANELA_FECHADA');
+      expect(metaFake.enviados).toHaveLength(0);
+    });
+
+    it('a thread informa o estado da janela, para a tela saber que responder está indisponível', async () => {
+      await prisma.message.updateMany({
+        where: { conversationId: conversaId },
+        data: { createdAt: new Date(Date.now() - 25 * 60 * 60 * 1000) },
+      });
+      const res = await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
+
+      expect(res.body.janela).toMatchObject({ exigida: true, aberta: false, canal: 'OFICIAL' });
+    });
+
+    it('no canal NÃO oficial não existe janela: responde mesmo com a conversa velha', async () => {
+      const geral = await prisma.setor.findFirstOrThrow({ where: { mantenedoraId: A.mantenedora.id } });
+      const bu2 = await prisma.businessUnit.create({
+        data: { mantenedoraId: A.mantenedora.id, setorId: geral.id, name: 'Número não oficial' },
+      });
+      await prisma.buChannel.create({
+        data: { buId: bu2.id, type: 'NAO_OFICIAL', evolutionInstanceName: 'inst-alfa', requiresWindow: false, status: 'CONECTADO' },
+      });
+      await prisma.userBuRole.create({
+        data: {
+          userId: A.owner.id,
+          buId: bu2.id,
+          role: 'OWNER',
+          grantedViaTipo: 'MANTENEDORA',
+          grantedViaId: A.mantenedora.id,
+        },
+      });
+      const conversa = await prisma.conversation.create({
+        data: { buId: bu2.id, contact: '5584933334444', contactType: 'PESSOA', status: 'QUEUED' },
+      });
+      await prisma.message.create({
+        data: {
+          conversationId: conversa.id, buId: bu2.id, direction: 'IN', messageType: 'TEXTO',
+          content: 'antiga', channelOrigin: 'NAO_OFICIAL', status: 'RECEBIDA',
+          createdAt: new Date(Date.now() - 72 * 60 * 60 * 1000),
+        },
+      });
+
+      await responder(cookieOwner, conversa.id).expect(201);
+      expect(evolutionFake.enviados).toHaveLength(1);
+      expect(metaFake.enviados).toHaveLength(0);
+    });
+  });
+
+  describe('fila', () => {
+    it('assumir trava para outro agente (409), e finalizar libera', async () => {
+      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro@alfa.test', 'ATENDENTE');
+      const cookieOutro = await login(app, 'outro@alfa.test');
+
+      await request(app.getHttpServer())
+        .post(`/api/bff/conversations/${conversaId}/claim`)
+        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
+
+      const conflito = await request(app.getHttpServer())
+        .post(`/api/bff/conversations/${conversaId}/claim`)
+        .set('Cookie', cookieOutro).set('x-requested-with', 'teste').expect(409);
+      expect(conflito.body.code).toBe('JA_ATENDIDA');
+
+      await request(app.getHttpServer())
+        .post(`/api/bff/conversations/${conversaId}/close`)
+        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
+
+      await request(app.getHttpServer())
+        .post(`/api/bff/conversations/${conversaId}/claim`)
+        .set('Cookie', cookieOutro).set('x-requested-with', 'teste').expect(201);
+    });
+
+    it('responder NÃO rouba conversa de quem já está atendendo', async () => {
+      await request(app.getHttpServer())
+        .post(`/api/bff/conversations/${conversaId}/claim`)
+        .set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
+
+      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro2@alfa.test', 'ATENDENTE');
+      const cookieOutro = await login(app, 'outro2@alfa.test');
+      await responder(cookieOutro, conversaId, 'me intrometi').expect(201);
+
+      const conversa = await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
+      expect(conversa.attendantUserId).toBe(A.owner.id);
+    });
+
+    it('abrir a thread zera as não lidas — abrir É atender', async () => {
+      await receber('mais uma');
+      // O beforeEach já deixou a primeira mensagem recebida como não lida.
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(2);
+
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
+
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(0);
+    });
+
+    it('a lista filtra por aba e só enxerga a BU pedida', async () => {
+      const res = await request(app.getHttpServer())
+        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?aba=QUEUED`)
+        .set('Cookie', cookieOwner).expect(200);
+      expect(res.body.conversations).toHaveLength(1);
+
+      const emAtendimento = await request(app.getHttpServer())
+        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?aba=IN_SERVICE`)
+        .set('Cookie', cookieOwner).expect(200);
+      expect(emAtendimento.body.conversations).toHaveLength(0);
+    });
+  });
+
+  describe('a inbox pagina — teto silencioso é o que vira "sumiram conversas"', () => {
+    it('devolve total e temMais, e a segunda página traz o resto', async () => {
+      for (let i = 0; i < 5; i++) {
+        await prisma.conversation.create({
+          data: {
+            buId: A.businessUnit.id,
+            contact: `55119000000${i}0`,
+            contactType: 'PESSOA',
+            status: 'QUEUED',
+            lastMessageAt: new Date(Date.now() - i * 1000),
+          },
+        });
+      }
+
+      const p1 = await request(app.getHttpServer())
+        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=2`)
+        .set('Cookie', cookieOwner)
+        .expect(200);
+
+      expect(p1.body.conversations).toHaveLength(2);
+      expect(p1.body.total).toBeGreaterThanOrEqual(5);
+      // O que faltava: a resposta DIZ que há mais. Antes o take era 200 fixo e o
+      // corte era invisível.
+      expect(p1.body.temMais).toBe(true);
+
+      const p2 = await request(app.getHttpServer())
+        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=2&pagina=2`)
+        .set('Cookie', cookieOwner)
+        .expect(200);
+
+      expect(p2.body.pagina).toBe(2);
+      const ids1 = p1.body.conversations.map((c: { id: string }) => c.id);
+      const ids2 = p2.body.conversations.map((c: { id: string }) => c.id);
+      expect(ids1.some((id: string) => ids2.includes(id))).toBe(false);
+    });
+
+    it('limite acima do teto é aparado, não obedecido', async () => {
+      const r = await request(app.getHttpServer())
+        .get(`/api/bff/business-units/${A.businessUnit.id}/conversations?limite=99999`)
+        .set('Cookie', cookieOwner)
+        .expect(200);
+      // Um cliente não escolhe quanto o banco carrega de uma vez.
+      expect(r.body.conversations.length).toBeLessThanOrEqual(200);
+    });
+  });
+
+  describe('timeline paginada do atendimento', () => {
+    it('caminha por 251 mensagens na ordem do banco e mantém a página limitada', async () => {
+      const base = new Date('2026-01-01T12:00:00.000Z');
+      const mensagens = Array.from({ length: 251 }, (_, i) => ({
+        conversationId: conversaId,
+        buId: A.businessUnit.id,
+        direction: 'IN' as const,
+        messageType: 'TEXTO' as const,
+        content: `mensagem ${i}`,
+        channelOrigin: 'OFICIAL' as const,
+        status: 'RECEBIDA' as const,
+        createdAt: new Date(base.getTime() + Math.floor(i / 7) * 1000),
+      }));
+      await prisma.message.deleteMany({ where: { conversationId: conversaId } });
+      await prisma.message.createMany({ data: mensagens });
+      const esperados = await prisma.message.findMany({
+        where: { conversationId: conversaId }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true },
+      });
+
+      const recebidos: string[] = [];
+      let antes: string | null = null;
+      do {
+        const query = antes ? `?limite=37&marcarLida=false&antes=${encodeURIComponent(antes)}` : '?limite=37&marcarLida=false';
+        const pagina = await request(app.getHttpServer())
+          .get(`/api/bff/conversations/${conversaId}/messages${query}`).set('Cookie', cookieOwner).expect(200);
+        expect(pagina.body.messages.length).toBeLessThanOrEqual(37);
+        expect(pagina.body.paginacao.limite).toBe(37);
+        recebidos.unshift(...pagina.body.messages.map((m: { id: string }) => m.id));
+        antes = pagina.body.paginacao.cursorAnterior;
+        expect(pagina.body.paginacao.temAnteriores).toBe(Boolean(antes));
+      } while (antes);
+
+      expect(recebidos).toEqual(esperados.map((m) => m.id));
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
+    });
+
+    it('valida parâmetros depois da autorização e rejeita cursor de outra conversa autorizada', async () => {
+      await prisma.message.create({ data: {
+        conversationId: conversaId, buId: A.businessUnit.id, direction: 'IN', messageType: 'TEXTO',
+        content: 'página de cursor', channelOrigin: 'OFICIAL', status: 'RECEBIDA',
+        createdAt: new Date(Date.now() - 1000),
+      } });
+      const segunda = await prisma.conversation.create({ data: {
+        buId: A.businessUnit.id, contact: '5584999999999', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 3,
+      } });
+      const cursorFonte = await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?limite=1`).set('Cookie', cookieOwner).expect(200);
+      const cursor = cursorFonte.body.paginacao.cursorAnterior;
+      if (!cursor) throw new Error('A fixture precisa produzir continuação.');
+
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${segunda.id}/messages?antes=${encodeURIComponent(cursor)}&marcarLida=false`)
+        .set('Cookie', cookieOwner).expect(400).expect(({ body }) => expect(body.code).toBe('PAGINACAO_INVALIDA'));
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: segunda.id } })).unreadCount).toBe(3);
+      await receber('antes de cursor inválido');
+      const anchor = lerCursorTimeline(cursor);
+      await prisma.message.delete({ where: { id: anchor.mensagemId } });
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?antes=${encodeURIComponent(cursor)}&marcarLida=false`)
+        .set('Cookie', cookieOwner).expect(400).expect(({ body }) => expect(body.code).toBe('PAGINACAO_INVALIDA'));
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
+      const conversaOutraMantenedora = await prisma.conversation.create({ data: {
+        buId: B.businessUnit.id, contact: '5584666666666', contactType: 'PESSOA', status: 'QUEUED',
+      } });
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaOutraMantenedora.id}/messages?limite=0&antes=x`)
+        .set('Cookie', cookieOwner).expect(404);
+      const setor = await prisma.setor.findFirstOrThrow({ where: { mantenedoraId: A.mantenedora.id } });
+      const buSemGrant = await prisma.businessUnit.create({ data: {
+        mantenedoraId: A.mantenedora.id, setorId: setor.id, name: 'BU sem grant',
+      } });
+      const conversaSemGrant = await prisma.conversation.create({ data: {
+        buId: buSemGrant.id, contact: '5584777777777', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 3,
+      } });
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaSemGrant.id}/messages?limite=0&antes=x`)
+        .set('Cookie', cookieOwner).expect(404);
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaSemGrant.id } })).unreadCount).toBe(3);
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?limite=0`)
+        .set('Cookie', cookieOwner).expect(400).expect(({ body }) => expect(body.code).toBe('PAGINACAO_INVALIDA'));
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
+    });
+
+    it('exige sessão antes de validar query e não altera unread', async () => {
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?limite=0&antes=x`).expect(401);
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
+    });
+
+    it('rejeita cursor/limite repetidos e mantém refresh e backfill sem efeito de leitura', async () => {
+      await receber('entrada extra');
+      const invalid = await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?limite=1&limite=2`)
+        .set('Cookie', cookieOwner).expect(400);
+      expect(invalid.body.code).toBe('PAGINACAO_INVALIDA');
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?antes=a&antes=b`)
+        .set('Cookie', cookieOwner).expect(400);
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(2);
+
+      const aberta = await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?limite=1`).set('Cookie', cookieOwner).expect(200);
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(0);
+      const cursor = aberta.body.paginacao.cursorAnterior;
+      if (cursor) {
+        await request(app.getHttpServer())
+          .get(`/api/bff/conversations/${conversaId}/messages?antes=${encodeURIComponent(cursor)}`)
+          .set('Cookie', cookieOwner).expect(200);
+      }
+      await receber('nova durante leitura');
+      await request(app.getHttpServer())
+        .get(`/api/bff/conversations/${conversaId}/messages?marcarLida=false`)
+        .set('Cookie', cookieOwner).expect(200);
+      expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(1);
+    });
+
+    it('serializa dez chegadas concorrentes com a fronteira de abertura em três lotes', async () => {
+      for (let lote = 0; lote < 3; lote++) {
+        await request(app.getHttpServer())
+          .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
+        const chegadas = Array.from({ length: 10 }, (_, i) => receber(`concorrente-${lote}-${i}`));
+        const abertura = request(app.getHttpServer())
+          .get(`/api/bff/conversations/${conversaId}/messages`).set('Cookie', cookieOwner).expect(200);
+        await Promise.all([...chegadas, abertura]);
+
+        const aposConcorrencia = (await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount;
+        expect(aposConcorrencia).toBeGreaterThanOrEqual(0);
+        expect(aposConcorrencia).toBeLessThanOrEqual(10);
+        await receber(`apos-fronteira-${lote}`);
+        expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(aposConcorrencia + 1);
+      }
+    });
+
+    it('preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes', async () => {
+      for (let lote = 0; lote < 3; lote++) {
+        await prisma.conversation.update({ where: { id: conversaId }, data: { unreadCount: 0 } });
+        let marcouLock!: () => void;
+        let liberaLock!: () => void;
+        const lockAdquirido = new Promise<void>((resolve) => { marcouLock = resolve; });
+        const aguardaLiberação = new Promise<void>((resolve) => { liberaLock = resolve; });
+        const transacaoLock = prisma.$transaction(async (tx) => {
+          await tx.$executeRawUnsafe('LOCK TABLE "messages" IN ACCESS EXCLUSIVE MODE');
+          marcouLock();
+          await aguardaLiberação;
+        }, { timeout: 30_000 });
+        await lockAdquirido;
+
+        const inicioLeitura = performance.now();
+        const leitura = request(app.getHttpServer())
+          .get(`/api/bff/conversations/${conversaId}/messages`)
+          .set('Cookie', cookieOwner).then((res) => res);
+        let esperaNoSelect = false;
+        let consultas = 0;
+        for (let tentativa = 0; tentativa < 100; tentativa++) {
+          const bloqueadas = await prisma.$queryRaw<Array<{ count: number }>>`
+            SELECT COUNT(*)::int AS count
+            FROM pg_stat_activity
+            WHERE datname = current_database()
+              AND wait_event_type = 'Lock'
+              AND query ILIKE '%messages%'
+              AND query ILIKE '%SELECT%'
+          `;
+          consultas++;
+          if (Number(bloqueadas[0]?.count ?? 0) > 0) {
+            esperaNoSelect = true;
+            break;
+          }
+          await new Promise((resolve) => setTimeout(resolve, 20));
+        }
+
+        try {
+          expect(esperaNoSelect, `GET precisa estar bloqueado no SELECT de messages no lote ${lote + 1}`).toBe(true);
+          const inicioIncrementos = performance.now();
+          await Promise.all(Array.from({ length: 10 }, () => prisma.conversation.updateMany({
+            where: { id: conversaId }, data: { unreadCount: { increment: 1 } },
+          })));
+          const aposIncrementos = (await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount;
+          expect(aposIncrementos).toBe(10);
+          liberaLock();
+          const resposta = await leitura;
+          expect(resposta.status).toBe(200);
+          const persistido = (await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount;
+          expect(persistido).toBe(10);
+          console.info(JSON.stringify({
+            prova: 'BCI_ACK_COM_SELECT_BLOQUEADO', lote: lote + 1,
+            bloqueioDetectado: esperaNoSelect, sondagens: consultas,
+            ackAteSelectBloqueadoMs: Math.round(performance.now() - inicioLeitura),
+            dezIncrementosMs: Math.round(performance.now() - inicioIncrementos),
+            unreadEnquantoSelectBloqueado: aposIncrementos, unreadDepoisDaResposta: persistido,
+          }));
+        } finally {
+          liberaLock();
+          await leitura.catch(() => undefined);
+          await transacaoLock;
+        }
+        await receber(`apos-ack-bloqueado-${lote}`);
+        expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).unreadCount).toBe(11);
+      }
+    });
+
+    it('permite leituras de cursor concorrentes com close sem reescrever status', async () => {
+      for (let lote = 0; lote < 3; lote++) {
+        const mensagens = Array.from({ length: 10 }, (_, i) => prisma.message.create({ data: {
+          conversationId: conversaId, buId: A.businessUnit.id, direction: 'IN', messageType: 'TEXTO',
+          content: `corrida ${lote}-${i}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
+          createdAt: new Date(Date.now() + i),
+        } }));
+        await Promise.all(mensagens);
+        const primeira = await request(app.getHttpServer())
+          .get(`/api/bff/conversations/${conversaId}/messages?limite=1&marcarLida=false`)
+          .set('Cookie', cookieOwner).expect(200);
+        const cursor = primeira.body.paginacao.cursorAnterior;
+        expect(cursor).toBeTruthy();
+        const leituras = Array.from({ length: 10 }, () => request(app.getHttpServer())
+          .get(`/api/bff/conversations/${conversaId}/messages?limite=1&marcarLida=false&antes=${encodeURIComponent(cursor)}`)
+          .set('Cookie', cookieOwner).expect(200));
+        const fechamento = request(app.getHttpServer())
+          .post(`/api/bff/conversations/${conversaId}/close`).set('Cookie', cookieOwner).set('x-requested-with', 'teste').expect(201);
+        const respostas = await Promise.all([...leituras, fechamento]);
+        expect(respostas.slice(0, 10).every((r) => r.body.messages.length <= 1)).toBe(true);
+        expect((await prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } })).status).toBe('CLOSED');
+      }
+    });
+  });
+});

```

## api-app/src/domain/inbox/conversations.service.ts

```
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

    const externalId = await this.enviarPeloCanal(janela.canal, conversa.contact, texto);

    const mensagem = await this.prisma.message.create({
      data: {
        conversationId: conversa.id,
        buId: conversa.buId,
        direction: 'OUT',
        messageType: 'TEXTO',
        content: texto,
        channelOrigin: janela.canal.type,
        status: 'ENVIADA',
        externalId,
        authorUserId: atendente.userId,
        // Snapshot: a autoria sobrevive à exclusão do usuário (ADR-0007).
        authorName: atendente.nome,
      },
    });

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
    canal: { type: string; phoneNumberId: string | null; evolutionInstanceName: string | null },
    contato: string,
    texto: string,
  ): Promise<string | null> {
    try {
      if (canal.type === 'OFICIAL') {
        if (!canal.phoneNumberId) {
          throw new BadRequestException({ error: 'Canal sem número de envio.', code: 'CANAL_SEM_NUMERO' });
        }
        return await this.meta.enviarTexto(canal.phoneNumberId, contato, texto);
      }
      if (!canal.evolutionInstanceName) {
        throw new BadRequestException({ error: 'Canal sem instância.', code: 'CANAL_SEM_INSTANCIA' });
      }
      return await this.evolution.enviarTexto(canal.evolutionInstanceName, contato, texto);
    } catch (e) {
      if (e instanceof BadRequestException || e instanceof ConflictException) throw e;
      // Os dois códigos ficam DISTINTOS de propósito: quem trata o erro quer
      // saber qual plataforma recusou, porque o contorno é diferente (ADR-0010).
      throw new BadRequestException({
        error: e instanceof Error ? e.message : 'O canal recusou o envio.',
        code: canal.type === 'OFICIAL' ? 'META_RECUSOU' : 'EVOLUTION_RECUSOU',
      });
    }
  }
}

```

## api-app/src/surfaces/bff/conversations.controller.ts

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

## api-app/test/atendimento.e2e-spec.ts

```
import { INestApplication } from '@nestjs/common';
import { createHmac } from 'node:crypto';
import request from 'supertest';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import {
  META_APP_SECRET,
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
    await prisma.buChannel.create({
      data: { buId: A.businessUnit.id, type: 'OFICIAL', phoneNumberId: PHONE_A, requiresWindow: true, status: 'CONECTADO' },
    });
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
      await prisma.buChannel.create({
        data: { buId: bu2.id, type: 'NAO_OFICIAL', evolutionInstanceName: 'inst-alfa', requiresWindow: false, status: 'CONECTADO' },
      });
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

## api-app/src/domain/inbox/timeline-pagination.spec.ts

```
import { describe, expect, it } from 'vitest';
import { criarCursorTimeline, lerCursorTimeline, validarConsultaTimeline } from './timeline-pagination';

describe('consulta da timeline', () => {
  it('usa 50 por padrão e limita páginas a 100', () => {
    expect(validarConsultaTimeline({})).toEqual({ limite: 50, antes: null, marcarLida: true });
    expect(validarConsultaTimeline({ limite: '100', marcarLida: 'false' })).toEqual({
      limite: 100, antes: null, marcarLida: false,
    });
  });

  it.each([
    { limite: '0' }, { limite: '101' }, { limite: '1.0' }, { limite: '+1' },
    { limite: ['2', '3'] }, { antes: ['cursor', 'cursor'] }, { marcarLida: 'TRUE' },
    { antes: 'cursor', marcarLida: 'true' }, { desconhecida: 'aceita' },
  ])('rejeita entrada inválida %#', (query) => {
    if ('desconhecida' in query) {
      expect(validarConsultaTimeline(query)).toMatchObject({ marcarLida: true });
    } else {
      expect(() => validarConsultaTimeline(query)).toThrow();
    }
  });

  it('emite cursor versionado, canônico e escopado', () => {
    const cursor = criarCursorTimeline('conversa-1', 'mensagem-1');
    expect(cursor.startsWith('v1.')).toBe(true);
    expect(lerCursorTimeline(cursor)).toEqual({ conversaId: 'conversa-1', mensagemId: 'mensagem-1' });
    expect(() => lerCursorTimeline('v1.eyJjIjoiYyIsIm0iOiJtIn0=')).toThrow();
  });
});

```

## api-app/src/domain/inbox/timeline-pagination.ts

```
import { BadRequestException } from '@nestjs/common';

export const LIMITE_TIMELINE_PADRAO = 50;
export const LIMITE_TIMELINE_MAXIMO = 100;
const PREFIXO_CURSOR = 'v1.';

export interface ConsultaTimeline {
  limite: number;
  antes: string | null;
  marcarLida: boolean;
}

function invalida(): never {
  throw new BadRequestException({ error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA' });
}

function unico(q: Record<string, unknown>, chave: string): string | undefined {
  const valor = q[chave];
  if (valor === undefined) return undefined;
  if (typeof valor !== 'string') return invalida();
  return valor;
}

export function validarConsultaTimeline(q: Record<string, unknown>): ConsultaTimeline {
  const rawLimite = unico(q, 'limite');
  let limite = LIMITE_TIMELINE_PADRAO;
  if (rawLimite !== undefined) {
    if (!/^(0|[1-9][0-9]*)$/.test(rawLimite)) return invalida();
    limite = Number(rawLimite);
    if (!Number.isSafeInteger(limite) || limite < 1 || limite > LIMITE_TIMELINE_MAXIMO) return invalida();
  }

  const antes = unico(q, 'antes');
  if (antes !== undefined && (antes.length === 0 || antes.length > 256)) return invalida();
  const rawMarcarLida = unico(q, 'marcarLida');
  if (rawMarcarLida !== undefined && rawMarcarLida !== 'true' && rawMarcarLida !== 'false') return invalida();
  if (antes !== undefined && rawMarcarLida === 'true') return invalida();

  return { limite, antes: antes ?? null, marcarLida: antes === undefined && rawMarcarLida !== 'false' };
}

export function criarCursorTimeline(conversaId: string, mensagemId: string): string {
  return PREFIXO_CURSOR + Buffer.from(JSON.stringify({ c: conversaId, m: mensagemId })).toString('base64url');
}

export function lerCursorTimeline(cursor: string): { conversaId: string; mensagemId: string } {
  if (!cursor.startsWith(PREFIXO_CURSOR) || cursor.length > 256) return invalida();
  try {
    const encoded = cursor.slice(PREFIXO_CURSOR.length);
    const json = Buffer.from(encoded, 'base64url').toString('utf8');
    const valor: unknown = JSON.parse(json);
    if (
      !valor || typeof valor !== 'object' ||
      typeof (valor as { c?: unknown }).c !== 'string' ||
      typeof (valor as { m?: unknown }).m !== 'string' ||
      Buffer.from(json).toString('base64url') !== encoded
    ) return invalida();
    return { conversaId: (valor as { c: string }).c, mensagemId: (valor as { m: string }).m };
  } catch {
    return invalida();
  }
}

```

## api-app/test/browser-server.cjs

```
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
  process.env.WHATSAPP_TOKEN = 'token-de-e2e';
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

## api-app/test/timeline-fixtures.cjs

```
const http = require('node:http');
const { createHmac } = require('node:crypto');
const bcrypt = require('bcryptjs');
const { PrismaClient } = require('@prisma/client');

const databaseUrl = process.env.DATABASE_URL;
const dedicatedUrl = process.env.LEADSHUG_E2E_DATABASE_URL;
const fixturePort = Number(process.env.LEADSHUG_FIXTURE_PORT ?? '3101');
const apiPort = Number(process.env.LEADSHUG_API_PORT ?? '3100');
if (!databaseUrl || databaseUrl !== dedicatedUrl) throw new Error('Fixtures exigem DATABASE_URL igual ao banco descartável de E2E.');
if (!new URL(databaseUrl).pathname.slice(1).split('?')[0].startsWith('leadshug_timeline_')) throw new Error('Fixtures aceitam apenas banco leadshug_timeline_* descartável.');

const prisma = new PrismaClient({ datasources: { db: { url: databaseUrl } } });
const json = (res, status, body) => { res.writeHead(status, { 'content-type': 'application/json' }); res.end(JSON.stringify(body)); };
const bodyOf = (req) => new Promise((resolve, reject) => {
  let raw = '';
  req.on('data', (chunk) => { raw += chunk; if (raw.length > 100_000) reject(new Error('body too large')); });
  req.on('end', () => { try { resolve(JSON.parse(raw || '{}')); } catch (e) { reject(e); } });
  req.on('error', reject);
});

async function seed(data) {
  const suffix = `${Date.now()}-${Math.random().toString(16).slice(2)}`;
  const mantenedora = await prisma.mantenedora.create({ data: { name: `Timeline ${suffix}` } });
  const setor = await prisma.setor.create({ data: { mantenedoraId: mantenedora.id, name: 'Geral' } });
  const businessUnit = await prisma.businessUnit.create({ data: { mantenedoraId: mantenedora.id, setorId: setor.id, name: 'Número timeline', phone: `5584${String(Date.now()).slice(-8)}` } });
  await prisma.mantenedoraSettings.create({ data: { mantenedoraId: mantenedora.id, onboardingConcluido: true, modulos: { canalNaoOficial: false } } });
  const email = `timeline-${suffix}@teste.local`;
  const user = await prisma.appUser.create({ data: {
    mantenedoraId: mantenedora.id, name: 'Atendente Timeline', email,
    passwordHash: await bcrypt.hash('senha-de-teste-1', 10),
  } });
  await prisma.userBuRole.create({ data: { userId: user.id, buId: businessUnit.id, role: 'OWNER', grantedViaTipo: 'DIRETO' } });
  const phoneNumberId = `timeline-phone-${suffix}`;
  await prisma.buChannel.create({ data: { buId: businessUnit.id, type: 'OFICIAL', phoneNumberId, requiresWindow: false, status: 'CONECTADO' } });
  const conversation = await prisma.conversation.create({ data: { buId: businessUnit.id, contact: '5584911112222', displayName: 'Cliente Timeline', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 0 } });
  const otherConversation = await prisma.conversation.create({ data: { buId: businessUnit.id, contact: '5584933334444', displayName: 'Cliente Secundário', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 0 } });
  const otherBu = await prisma.businessUnit.create({ data: { mantenedoraId: mantenedora.id, setorId: setor.id, name: 'Número alternativo', phone: `5585${String(Date.now()).slice(-8)}` } });
  await prisma.userBuRole.create({ data: { userId: user.id, buId: otherBu.id, role: 'OWNER', grantedViaTipo: 'DIRETO' } });
  const otherBuPhoneNumberId = `timeline-phone-other-${suffix}`;
  await prisma.buChannel.create({ data: { buId: otherBu.id, type: 'OFICIAL', phoneNumberId: otherBuPhoneNumberId, requiresWindow: false, status: 'CONECTADO' } });
  const otherBuConversation = await prisma.conversation.create({ data: { buId: otherBu.id, contact: '5585555555555', displayName: 'Cliente Outra BU', contactType: 'PESSOA', status: 'QUEUED' } });
  const count = Math.max(0, Math.min(Number(data.count ?? 251), 10_000));
  const tiedAt = new Date('2026-10-14T12:00:00.000Z');
  const messages = Array.from({ length: count }, (_, i) => ({
    conversationId: conversation.id, buId: businessUnit.id, direction: 'IN', messageType: 'TEXTO',
    content: `histórico ${i + 1}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
    createdAt: data.tied === true ? tiedAt : new Date(tiedAt.getTime() + i * 1000),
  }));
  if (messages.length) await prisma.message.createMany({ data: messages });
  const expectedIds = await prisma.message.findMany({ where: { conversationId: conversation.id }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true } });
  return { email, password: 'senha-de-teste-1', userId: user.id, mantenedoraId: mantenedora.id, businessUnitId: businessUnit.id, conversationId: conversation.id, otherConversationId: otherConversation.id, otherBusinessUnitId: otherBu.id, otherBuConversationId: otherBuConversation.id, otherBuPhoneNumberId, phoneNumberId, count, expectedIds: expectedIds.map((m) => m.id) };
}

async function incoming(data) {
  const id = String(data.id ?? `timeline-event-${Date.now()}`);
  const payload = { entry: [{ changes: [{ field: 'messages', value: {
    metadata: { phone_number_id: data.phoneNumberId },
    contacts: [{ profile: { name: 'Cliente Timeline' } }],
    messages: [{ id, from: '5584911112222', type: 'text', text: { body: String(data.text ?? id) } }],
  } }] }] };
  const raw = JSON.stringify(payload);
  const signature = 'sha256=' + createHmac('sha256', 'segredo-do-app-meta').update(raw).digest('hex');
  const response = await fetch(`http://127.0.0.1:${apiPort}/webhooks/meta`, {
    method: 'POST', headers: { 'content-type': 'application/json', 'x-hub-signature-256': signature }, body: raw,
  });
  return { status: response.status, body: await response.text() };
}

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === 'GET' && req.url === '/health') return json(res, 200, { status: 'ok' });
    const data = await bodyOf(req);
    if (req.method === 'GET' && req.url.startsWith('/audit?')) {
      const query = new URL(req.url, 'http://localhost').searchParams;
      const conversationId = query.get('conversationId');
      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
      const messages = await prisma.message.findMany({ where: { conversationId }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true, content: true, direction: true, authorName: true, createdAt: true } });
      return json(res, 200, { status: conversation.status, unreadCount: conversation.unreadCount, messages });
    }
    if (req.method === 'POST' && req.url === '/seed') return json(res, 201, await seed(data));
    if (req.method === 'POST' && req.url === '/incoming') return json(res, 200, await incoming(data));
    if (req.method === 'POST' && req.url === '/late-tie') {
      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: data.conversationId } });
      const message = await prisma.message.create({ data: {
        id: String(data.id), conversationId: conversation.id, buId: conversation.buId,
        direction: 'IN', messageType: 'TEXTO', content: 'inserção empatada tardia',
        channelOrigin: 'OFICIAL', status: 'RECEBIDA', createdAt: new Date(data.createdAt),
      } });
      return json(res, 201, { id: message.id });
    }
    if (req.method === 'POST' && req.url === '/revoke') {
      await prisma.userBuRole.deleteMany({ where: { userId: data.userId, buId: data.businessUnitId } });
      return json(res, 200, { revoked: true });
    }
    if (req.method === 'POST' && req.url === '/burst') {
      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: data.conversationId } });
      const count = Math.max(1, Math.min(Number(data.count ?? 120), 500));
      const base = new Date(data.createdAt ?? Date.now());
      await prisma.message.createMany({ data: Array.from({ length: count }, (_, i) => ({
        conversationId: conversation.id, buId: conversation.buId, direction: 'IN', messageType: 'TEXTO',
        content: `burst ${i + 1}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
        createdAt: new Date(base.getTime() + i),
      })) });
      return json(res, 201, { count });
    }
    return json(res, 404, { error: 'not found' });
  } catch (error) {
    console.error(error);
    return json(res, 500, { error: error instanceof Error ? error.message : String(error) });
  }
});
server.listen(fixturePort, '127.0.0.1', () => console.log(`timeline fixtures listening on 127.0.0.1:${fixturePort}`));
process.on('SIGTERM', () => server.close(() => prisma.$disconnect().finally(() => process.exit(0))));
process.on('SIGINT', () => server.close(() => prisma.$disconnect().finally(() => process.exit(0))));

```

## api-app/package.json

```
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

## api-app/vitest.config.ts

```
import swc from 'unplugin-swc';
import { defineConfig } from 'vitest/config';

// Testes de unidade. E2E tem configuração própria (vitest.config.e2e.ts),
// porque e2e precisa de banco e unidade não — ADR-0012 §1.
export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['src/**/*.spec.ts'],
  },
  plugins: [swc.vite({ module: { type: 'es6' } })],
});

```

## Tracked diff web-app from 6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9
```diff
diff --git a/playwright.config.ts b/playwright.config.ts
index 7b3c767..9cfec78 100644
--- a/playwright.config.ts
+++ b/playwright.config.ts
@@ -3,6 +3,8 @@ import { defineConfig } from '@playwright/test';
 /** Porta própria: a 3000 desta máquina é de outro projeto. */
 const PORTA_DA_API = process.env.LEADSHUG_API_PORT ?? '3100';
 const API = `http://127.0.0.1:${PORTA_DA_API}`;
+const DATABASE_URL = process.env.LEADSHUG_E2E_DATABASE_URL;
+if (!DATABASE_URL) throw new Error('LEADSHUG_E2E_DATABASE_URL precisa apontar para o banco descartável dedicado.');
 
 /**
  * Teste de navegador contra a tela **buildada**, não contra o dev server.
@@ -15,6 +17,7 @@ const API = `http://127.0.0.1:${PORTA_DA_API}`;
  * `vite preview` servindo o `dist`. Mesma origem, como em desenvolvimento.
  */
 export default defineConfig({
+  globalSetup: './e2e/timeline-freshness.ts',
   testDir: './e2e',
   timeout: 30_000,
   fullyParallel: false,
@@ -24,12 +27,26 @@ export default defineConfig({
     trace: 'retain-on-failure',
   },
   webServer: [
+    {
+      command: 'node ../api-app/test/timeline-fixtures.cjs',
+      url: 'http://127.0.0.1:3101/health',
+      reuseExistingServer: false,
+      timeout: 30_000,
+      stdout: 'pipe',
+      stderr: 'pipe',
+      env: {
+        DATABASE_URL,
+        LEADSHUG_E2E_DATABASE_URL: DATABASE_URL,
+        LEADSHUG_API_PORT: PORTA_DA_API,
+        LEADSHUG_FIXTURE_PORT: '3101',
+      },
+    },
     {
       // `build &&` NÃO é zelo: `npm run start` da api é `node dist/main.js`, e
       // sem construir antes o teste de tela valida uma API VELHA — que é o
       // oposto do que ele existe para fazer. Foi assim que uma mudança de schema
       // passou por aqui reportando 500 de um dist de duas fases atrás.
-      command: 'npm --prefix ../api run build && npm --prefix ../api run start',
+      command: 'npm --prefix ../api-app run build && node ../api-app/test/browser-server.cjs',
       url: `${API}/health`,
       // Não reaproveitar: esta máquina roda outros serviços, e "já tem algo na
       // porta" foi o que fez a primeira corrida testar o projeto vizinho.
@@ -48,7 +65,8 @@ export default defineConfig({
         // O `.env` da API pode apontar para outro Postgres local (por exemplo,
         // o serviço legado na 5433). O harness deve ser determinístico e falar
         // com o Postgres deste compose, publicado na 55433.
-        DATABASE_URL: process.env.LEADSHUG_E2E_DATABASE_URL ?? 'postgresql://leadshug:leadshug@127.0.0.1:55433/leadshug?schema=public',
+        DATABASE_URL,
+        LEADSHUG_E2E_DATABASE_URL: DATABASE_URL,
         SESSION_SECRET: 'segredo-de-e2e',
         INTERNAL_SERVICE_TOKEN: 'token-de-e2e',
         // O canal oficial é o PISO do produto: sem ele o processo não sobe
diff --git a/src/api.ts b/src/api.ts
index 1a6b5d0..7115238 100644
--- a/src/api.ts
+++ b/src/api.ts
@@ -243,4 +243,5 @@ export interface Thread {
   conversa: { id: string; contato: string; nome: string | null; status: string; atendente: string | null };
   janela: { exigida: boolean; aberta: boolean; expiraEm: string | null; canal: string | null };
   messages: Mensagem[];
+  paginacao: { limite: number; temAnteriores: boolean; cursorAnterior: string | null };
 }
diff --git a/src/telas/Inbox.tsx b/src/telas/Inbox.tsx
index 88320b4..b320258 100644
--- a/src/telas/Inbox.tsx
+++ b/src/telas/Inbox.tsx
@@ -1,196 +1,409 @@
-import { FormEvent, useEffect, useState } from 'react';
-import { BusinessUnit, Conversa, ErroDaApi, Eu, Thread, api, ignorarSessaoMorta } from '../api';
-import { ouvirTempoReal } from '../tempoReal';
-
-const ABAS = [
-  { id: 'QUEUED', rotulo: 'Na fila' },
-  { id: 'IN_SERVICE', rotulo: 'Em atendimento' },
-  { id: 'CLOSED', rotulo: 'Finalizadas' },
-  { id: 'GRUPO', rotulo: 'Grupos' },
-];
-
-export default function Inbox({ eu }: { eu: Eu }) {
-  const [bus, setBus] = useState<BusinessUnit[]>([]);
-  const [buId, setBuId] = useState<string>('');
-  const [aba, setAba] = useState('QUEUED');
-  const [conversas, setConversas] = useState<Conversa[]>([]);
-  const [aberta, setAberta] = useState<Thread | null>(null);
-  const [texto, setTexto] = useState('');
-  const [erro, setErro] = useState<string | null>(null);
-
-  useEffect(() => {
-    api
-      .get<{ businessUnits: BusinessUnit[] }>('/business-units')
-      .then((r) => {
-        // Lista ausente vira lista vazia: `undefined[0]` derruba a tela inteira,
-        // e uma resposta fora do formato esperado não pode custar isso.
-        const lista = r.businessUnits ?? [];
-        setBus(lista);
-        setBuId((atual) => atual || lista[0]?.id || '');
-      })
-      .catch(ignorarSessaoMorta);
-  }, []);
-
-  const carregarLista = async (id = buId, filtro = aba) => {
-    if (!id) return;
-    const r = await api.get<{ conversations: Conversa[] }>(
-      `/business-units/${id}/conversations?aba=${filtro}`,
-    );
-    setConversas(r.conversations);
-  };
-
-  useEffect(() => {
-    carregarLista().catch(ignorarSessaoMorta);
-    // Push com escopo por BU (o servidor só manda o que a pessoa pode ver). O
-    // poll longo fica como rede: se o socket cair entre a queda e a reconexão,
-    // a tela ainda se atualiza sozinha.
-    const parar = ouvirTempoReal((evento) => {
-      if (evento.buId !== buId) return;
-      carregarLista().catch(ignorarSessaoMorta);
-      if (aberta?.conversa.id === evento.conversaId) abrir(evento.conversaId).catch(ignorarSessaoMorta);
-    });
-    const t = setInterval(() => carregarLista().catch(ignorarSessaoMorta), 60_000);
-    return () => {
-      parar();
-      clearInterval(t);
-    };
-  }, [buId, aba, aberta?.conversa.id]);
-
-  async function abrir(id: string) {
-    setErro(null);
-    setAberta(await api.get<Thread>(`/conversations/${id}/messages`));
-    void carregarLista();
-  }
-
-  async function agir(acao: () => Promise<unknown>) {
-    setErro(null);
-    try {
-      await acao();
-      if (aberta) setAberta(await api.get<Thread>(`/conversations/${aberta.conversa.id}/messages`));
-      await carregarLista();
-    } catch (e) {
-      setErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
-    }
-  }
-
-  async function responder(e: FormEvent) {
-    e.preventDefault();
-    if (!aberta || !texto.trim()) return;
-    await agir(async () => {
-      await api.post(`/conversations/${aberta.conversa.id}/messages`, { texto });
-      setTexto('');
-    });
-  }
-
-  // Estar no escopo BASTA para atender (ADR-0018 §3): o eixo de capacidades foi
-  // dissolvido, e o papel VIEWER — que era o único que lia sem responder —
-  // deixou de existir. A comparação com 'VIEWER' que morava aqui era sempre
-  // verdadeira desde a fase 2.
-  const podeResponder = true;
-  const janelaFechada = aberta?.janela.exigida && !aberta.janela.aberta;
-
-  return (
-    <div className="grade">
-      <div className="linha">
-        <select value={buId} onChange={(e) => setBuId(e.target.value)} style={{ maxWidth: 280 }}>
-          {bus.map((b) => (
-            <option key={b.id} value={b.id}>
-              {b.name}
-            </option>
-          ))}
-        </select>
-        {erro && <span className="erro">{erro}</span>}
-      </div>
-
-      <div className="abas">
-        {ABAS.map((a) => (
-          <button key={a.id} className={aba === a.id ? 'ativa' : ''} onClick={() => setAba(a.id)}>
-            {a.rotulo}
-          </button>
-        ))}
-      </div>
-
-      <div className="inbox">
-        <div className="cartao lista" style={{ padding: 0 }}>
-          {conversas.map((c) => (
-            <button
-              key={c.id}
-              className={`item ${aberta?.conversa.id === c.id ? 'ativo' : ''}`}
-              onClick={() => void abrir(c.id)}
-            >
-              <div className="linha">
-                <strong>{c.displayName ?? c.contact}</strong>
-                {c.unreadCount > 0 && <span className="suave">({c.unreadCount})</span>}
-              </div>
-              <div className="suave">{c.attendantName ?? 'sem atendente'}</div>
-            </button>
-          ))}
-          {conversas.length === 0 && <p className="suave" style={{ padding: 12 }}>Nada aqui.</p>}
-        </div>
-
-        <div className="cartao grade">
-          {!aberta && <p className="suave">Escolha uma conversa.</p>}
-          {aberta && (
-            <>
-              <div className="linha">
-                <strong>{aberta.conversa.nome ?? aberta.conversa.contato}</strong>
-                <span className="suave">{aberta.conversa.status}</span>
-                <span className="suave" style={{ marginLeft: 'auto' }}>
-                  {aberta.janela.canal}
-                </span>
-              </div>
-
-              <div className="bolhas">
-                {aberta.messages.map((m) => (
-                  <div key={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>
-                    <div>{m.content}</div>
-                    <div className="suave">
-                      {new Date(m.createdAt).toLocaleString('pt-BR')}
-                      {m.authorName ? ` · ${m.authorName}` : ''}
-                    </div>
-                  </div>
-                ))}
-              </div>
-
-              {janelaFechada && (
-                <div className="aviso">
-                  Fora da janela de 24h da Meta: só dá para responder texto livre até 24h após a última
-                  mensagem da pessoa. A alternativa é disparar um modelo aprovado — isso ainda vive na
-                  Central de Modelos.
-                </div>
-              )}
-
-              {podeResponder ? (
-                <form className="linha" onSubmit={responder}>
-                  <input
-                    value={texto}
-                    onChange={(e) => setTexto(e.target.value)}
-                    placeholder={janelaFechada ? 'Janela fechada' : 'Escreva uma resposta'}
-                    disabled={janelaFechada}
-                    maxLength={4096}
-                  />
-                  <button className="primario" disabled={janelaFechada}>
-                    Enviar
-                  </button>
-                </form>
-              ) : (
-                <p className="suave">Seu papel permite ler, não responder.</p>
-              )}
-
-              {podeResponder && aberta.conversa.status !== 'CLOSED' && (
-                <div className="linha">
-                  <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/claim`))}>
-                    Atender
-                  </button>
-                  <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/close`))}>
-                    Finalizar
-                  </button>
-                </div>
-              )}
-            </>
-          )}
-        </div>
-      </div>
-    </div>
-  );
-}
+import { FormEvent, useCallback, useEffect, useRef, useState } from 'react';
+import { BusinessUnit, Conversa, ErroDaApi, Eu, Mensagem, Thread, api, ignorarSessaoMorta } from '../api';
+import { ouvirTempoReal } from '../tempoReal';
+import { cruzouPiso, mesclarMensagens } from '../timeline';
+
+const ABAS = [
+  { id: 'QUEUED', rotulo: 'Na fila' },
+  { id: 'IN_SERVICE', rotulo: 'Em atendimento' },
+  { id: 'CLOSED', rotulo: 'Finalizadas' },
+  { id: 'GRUPO', rotulo: 'Grupos' },
+];
+
+interface Recuperacao {
+  id: string;
+  geracao: number;
+  piso: string;
+  cursor: string | null;
+  dirty: boolean;
+  eventos: number;
+  emVoo: boolean;
+  vazio?: boolean;
+}
+
+export default function Inbox({ eu }: { eu: Eu }) {
+  const [bus, setBus] = useState<BusinessUnit[]>([]);
+  const [buId, setBuId] = useState<string>('');
+  const [aba, setAba] = useState('QUEUED');
+  const [conversas, setConversas] = useState<Conversa[]>([]);
+  const [aberta, setAberta] = useState<Thread | null>(null);
+  const [abrindo, setAbrindo] = useState(false);
+  const [texto, setTexto] = useState('');
+  const [erro, setErro] = useState<string | null>(null);
+  const [carregandoAnteriores, setCarregandoAnteriores] = useState(false);
+  const [recuperacaoPendente, setRecuperacaoPendente] = useState(false);
+  const [enviando, setEnviando] = useState(false);
+  const textoRef = useRef('');
+  const geracao = useRef(0);
+  const buAtual = useRef('');
+  const conversaAtual = useRef<string | null>(null);
+  const abaAtual = useRef('QUEUED');
+  const threadAtual = useRef<Thread | null>(null);
+  const recuperacao = useRef<Recuperacao | null>(null);
+  const executarRecuperacaoRef = useRef<() => Promise<void>>(async () => {});
+  const versaoMetadados = useRef(0);
+  const bolhas = useRef<HTMLDivElement>(null);
+  const carregarListaRef = useRef<(id?: string, filtro?: string) => Promise<void>>(async () => {});
+  const reconciliarRef = useRef<() => void>(() => {});
+
+  const guardarThread = (thread: Thread | null) => {
+    threadAtual.current = thread;
+    setAberta(thread);
+  };
+
+  const guardarTexto = (valor: string) => {
+    textoRef.current = valor;
+    setTexto(valor);
+  };
+
+  useEffect(() => {
+    api.get<{ businessUnits: BusinessUnit[] }>('/business-units').then((r) => {
+      const lista = r.businessUnits ?? [];
+      setBus(lista);
+      const inicial = lista[0]?.id ?? '';
+      buAtual.current = inicial;
+      setBuId(inicial);
+    }).catch(ignorarSessaoMorta);
+  }, []);
+
+  const carregarLista = useCallback(async (id = buAtual.current, filtro = aba) => {
+    if (!id) return;
+    try {
+      const r = await api.get<{ conversations: Conversa[] }>(`/business-units/${id}/conversations?aba=${filtro}`);
+      if (buAtual.current === id && abaAtual.current === filtro) setConversas(r.conversations);
+    } catch (e) {
+      if (buAtual.current === id && abaAtual.current === filtro) throw e;
+    }
+  }, [aba]);
+
+  const aplicarPaginaRecente = useCallback((id: string, geracaoDaChamada: number, versao: number, response: Thread) => {
+    if (conversaAtual.current !== id || geracao.current !== geracaoDaChamada) return;
+    const anterior = threadAtual.current;
+    const novo: Thread = {
+      ...response,
+      messages: mesclarMensagens(anterior?.messages ?? [], response.messages),
+      // O cursor de reconciliação recente não substitui o cursor do histórico.
+      paginacao: anterior && anterior.messages.length > 0 ? anterior.paginacao : response.paginacao,
+      conversa: versaoMetadados.current === versao ? response.conversa : anterior?.conversa ?? response.conversa,
+      janela: versaoMetadados.current === versao ? response.janela : anterior?.janela ?? response.janela,
+    };
+    guardarThread(novo);
+  }, []);
+
+  const executarRecuperacao = useCallback(async () => {
+    const r = recuperacao.current;
+    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
+    r.emVoo = true;
+    const eventosNoInicio = r.eventos;
+    r.dirty = false;
+    let paginas = 3;
+    let cruzou = false;
+    try {
+      if (r.vazio) {
+        if (r.cursor === null && paginas > 0) {
+          const versao = versaoMetadados.current;
+          const inicial = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
+          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
+          aplicarPaginaRecente(r.id, r.geracao, versao, inicial);
+          r.cursor = inicial.paginacao.cursorAnterior;
+          paginas -= 1;
+          if (!inicial.paginacao.temAnteriores) r.cursor = null;
+        }
+        while (r.cursor && paginas > 0) {
+          const cursor = r.cursor;
+          const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
+          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
+          const atual = threadAtual.current;
+          if (atual) guardarThread({
+            ...atual,
+            messages: mesclarMensagens(atual.messages, pagina.messages),
+            paginacao: pagina.paginacao,
+          });
+          r.cursor = pagina.paginacao.cursorAnterior;
+          paginas -= 1;
+        }
+        if (r.eventos !== eventosNoInicio || r.dirty) {
+          r.cursor = null;
+          setRecuperacaoPendente(true);
+        } else if (!r.cursor) {
+          recuperacao.current = null;
+          setRecuperacaoPendente(false);
+        } else {
+          setRecuperacaoPendente(true);
+        }
+        return;
+      }
+      if (r.cursor === null) {
+        const versao = versaoMetadados.current;
+        const recente = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
+        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
+        aplicarPaginaRecente(r.id, r.geracao, versao, recente);
+        r.cursor = recente.paginacao.cursorAnterior;
+        paginas -= 1;
+        cruzou = cruzouPiso(recente.messages, r.piso) || !recente.paginacao.temAnteriores;
+      }
+      while (!cruzou && r.cursor && paginas > 0) {
+        const cursor = r.cursor;
+        const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
+        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
+        const atual = threadAtual.current;
+        if (atual) guardarThread({
+          ...atual,
+          messages: mesclarMensagens(atual.messages, pagina.messages),
+        });
+        r.cursor = pagina.paginacao.cursorAnterior;
+        paginas -= 1;
+        cruzou = cruzouPiso(pagina.messages, r.piso) || !pagina.paginacao.temAnteriores;
+      }
+
+      if (r.eventos !== eventosNoInicio || r.dirty) {
+        // Um evento concorrente exige nova passagem recente e preserva o piso.
+        r.cursor = null;
+        setRecuperacaoPendente(true);
+      } else if (cruzou) {
+        recuperacao.current = null;
+        setRecuperacaoPendente(false);
+      } else {
+        setRecuperacaoPendente(true);
+      }
+    } catch (e) {
+      if (r.geracao === geracao.current && r.id === conversaAtual.current) {
+        setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível atualizar o histórico. Tente novamente.');
+        setRecuperacaoPendente(true);
+      }
+    } finally {
+      r.emVoo = false;
+      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.geracao === geracao.current) {
+        queueMicrotask(() => void executarRecuperacaoRef.current());
+      }
+    }
+  }, [aplicarPaginaRecente]);
+
+  useEffect(() => { executarRecuperacaoRef.current = executarRecuperacao; }, [executarRecuperacao]);
+
+  const reconciliar = useCallback(() => {
+    const thread = threadAtual.current;
+    const id = conversaAtual.current;
+    if (!thread || !id) return;
+    let r = recuperacao.current;
+    if (!r || r.id !== id || r.geracao !== geracao.current) {
+      const mensagens = thread.messages;
+      if (mensagens.length === 0) {
+        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, vazio: true };
+        recuperacao.current = r;
+        void executarRecuperacao();
+        return;
+      }
+      const piso = mensagens.reduce((max, m) => Date.parse(m.createdAt) > Date.parse(max) ? m.createdAt : max, mensagens[0].createdAt);
+      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false };
+      recuperacao.current = r;
+      setRecuperacaoPendente(true);
+    } else {
+      r.dirty = true;
+      r.eventos += 1;
+      if (!r.emVoo && !r.vazio) r.cursor = null;
+      setRecuperacaoPendente(true);
+    }
+    void executarRecuperacao();
+  }, [aplicarPaginaRecente, executarRecuperacao]);
+
+  useEffect(() => {
+    carregarListaRef.current = carregarLista;
+    reconciliarRef.current = reconciliar;
+  }, [carregarLista, reconciliar]);
+
+  useEffect(() => {
+    void carregarLista().catch(ignorarSessaoMorta);
+    const t = setInterval(() => {
+      void carregarLista().catch(ignorarSessaoMorta);
+      if (recuperacao.current) void executarRecuperacaoRef.current();
+      else reconciliar();
+    }, 60_000);
+    return () => clearInterval(t);
+  }, [buId, aba, carregarLista, reconciliar]);
+
+  useEffect(() => {
+    // Espera a lista inicial de BUs e mantém o socket apesar de filtros, BUs ou
+    // callbacks locais mudarem. Isso evita reconectar durante o mesmo login.
+    if (bus.length === 0) return;
+    const parar = ouvirTempoReal((evento) => {
+      if (evento.buId !== buAtual.current) return;
+      void carregarListaRef.current().catch(ignorarSessaoMorta);
+      if (evento.conversaId === conversaAtual.current) reconciliarRef.current();
+    }, () => reconciliarRef.current());
+    return parar;
+  }, [eu.id, bus.length]);
+
+  function trocarBu(novoBu: string) {
+    geracao.current += 1;
+    buAtual.current = novoBu;
+    conversaAtual.current = null;
+    recuperacao.current = null;
+    guardarThread(null);
+    setAbrindo(false);
+    guardarTexto('');
+    setEnviando(false);
+    setCarregandoAnteriores(false);
+    setErro(null);
+    setRecuperacaoPendente(false);
+    setConversas([]);
+    setBuId(novoBu);
+  }
+
+  async function abrir(id: string) {
+    const gen = ++geracao.current;
+    conversaAtual.current = id;
+    recuperacao.current = null;
+    versaoMetadados.current += 1;
+    guardarThread(null);
+    setAbrindo(true);
+    guardarTexto('');
+    setEnviando(false);
+    setCarregandoAnteriores(false);
+    setErro(null);
+    setRecuperacaoPendente(false);
+    try {
+      const response = await api.get<Thread>(`/conversations/${id}/messages`);
+      if (gen !== geracao.current || conversaAtual.current !== id) return;
+      response.messages = mesclarMensagens(response.messages);
+      guardarThread(response);
+      setAbrindo(false);
+      void carregarLista().catch(ignorarSessaoMorta);
+    } catch (e) {
+      if (gen === geracao.current) {
+        guardarThread(null);
+        setAbrindo(false);
+        setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível carregar a conversa.');
+      }
+    }
+  }
+
+  async function carregarAnteriores() {
+    const atual = threadAtual.current;
+    const id = conversaAtual.current;
+    const cursor = atual?.paginacao.cursorAnterior;
+    if (!atual || !id || !cursor || carregandoAnteriores) return;
+    const gen = geracao.current;
+    setCarregandoAnteriores(true);
+    setErro(null);
+    try {
+      const pagina = await api.get<Thread>(`/conversations/${id}/messages?antes=${encodeURIComponent(cursor)}`);
+      if (gen !== geracao.current || id !== conversaAtual.current || !threadAtual.current) return;
+      // Inclua alterações legítimas que chegaram enquanto a página estava no ar.
+      const alturaAntes = bolhas.current?.scrollHeight ?? 0;
+      const topoAntes = bolhas.current?.scrollTop ?? 0;
+      const corrente = threadAtual.current;
+      guardarThread({ ...corrente, messages: mesclarMensagens(corrente.messages, pagina.messages), paginacao: pagina.paginacao });
+      requestAnimationFrame(() => {
+        if (gen === geracao.current && bolhas.current) bolhas.current.scrollTop = topoAntes + (bolhas.current.scrollHeight - alturaAntes);
+      });
+    } catch (e) {
+      if (gen === geracao.current) setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Falha ao carregar mensagens anteriores.');
+    } finally {
+      if (gen === geracao.current) setCarregandoAnteriores(false);
+    }
+  }
+
+  async function agir(acao: () => Promise<unknown>) {
+    const id = conversaAtual.current;
+    const gen = geracao.current;
+    if (!id) return;
+    versaoMetadados.current += 1;
+    setErro(null);
+    try {
+      await acao();
+      if (gen !== geracao.current || id !== conversaAtual.current) return;
+      void carregarLista().catch(ignorarSessaoMorta);
+      reconciliar();
+    } catch (e) {
+      if (gen === geracao.current) setErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
+    }
+  }
+
+  async function responder(e: FormEvent) {
+    e.preventDefault();
+    const id = conversaAtual.current;
+    const gen = geracao.current;
+    const textoEnviado = textoRef.current;
+    if (!id || !textoEnviado.trim() || enviando) return;
+    setEnviando(true);
+    setErro(null);
+    try {
+      await api.post(`/conversations/${id}/messages`, { texto: textoEnviado });
+      if (gen !== geracao.current || id !== conversaAtual.current) return;
+      if (textoRef.current === textoEnviado) guardarTexto('');
+      void carregarLista().catch(ignorarSessaoMorta);
+      reconciliar();
+    } catch (e) {
+      if (gen === geracao.current) setErro(e instanceof ErroDaApi ? e.message : 'Falha ao enviar mensagem.');
+    } finally {
+      if (gen === geracao.current) setEnviando(false);
+    }
+  }
+
+  const janelaFechada = aberta?.janela.exigida && !aberta.janela.aberta;
+
+  return (
+    <div className="grade">
+      <div className="linha">
+        <select aria-label="Business Unit" value={buId} onChange={(e) => trocarBu(e.target.value)} style={{ maxWidth: 280 }}>
+          {bus.map((b) => <option key={b.id} value={b.id}>{b.name}</option>)}
+        </select>
+        {erro && <span className="erro" role="alert">{erro}</span>}
+      </div>
+
+      <div className="abas">
+        {ABAS.map((a) => <button key={a.id} className={aba === a.id ? 'ativa' : ''} onClick={() => { abaAtual.current = a.id; setAba(a.id); }}>{a.rotulo}</button>)}
+      </div>
+
+      <div className="inbox">
+        <div className="cartao lista" style={{ padding: 0 }}>
+          {conversas.map((c) => <button key={c.id} className={`item ${aberta?.conversa.id === c.id ? 'ativo' : ''}`} onClick={() => void abrir(c.id)}>
+            <div className="linha"><strong>{c.displayName ?? c.contact}</strong>{c.unreadCount > 0 && <span className="suave">({c.unreadCount})</span>}</div>
+            <div className="suave">{c.attendantName ?? 'sem atendente'}</div>
+          </button>)}
+          {conversas.length === 0 && <p className="suave" style={{ padding: 12 }}>Nada aqui.</p>}
+        </div>
+
+        <div className="cartao grade">
+          {!aberta && (abrindo
+            ? <p className="suave" role="status" aria-live="polite">Abrindo conversa…</p>
+            : <p className="suave">Escolha uma conversa.</p>)}
+          {aberta && <>
+            <div className="linha">
+              <strong>{aberta.conversa.nome ?? aberta.conversa.contato}</strong>
+              <span className="suave">{aberta.conversa.status}</span>
+              <span className="suave" style={{ marginLeft: 'auto' }}>{aberta.janela.canal}</span>
+            </div>
+            <div className="linha">
+              {aberta.paginacao.temAnteriores
+                ? <button onClick={() => void carregarAnteriores()} disabled={carregandoAnteriores} aria-label="Carregar mensagens anteriores">
+                    {carregandoAnteriores ? 'Carregando…' : 'Carregar anteriores'}
+                  </button>
+                : <span className="suave">Início do histórico</span>}
+              {recuperacaoPendente && <span className="suave" role="status">Atualização pendente. O histórico pode ter uma lacuna.</span>}
+              {recuperacaoPendente && <button onClick={() => void executarRecuperacao()}>Continuar atualização</button>}
+            </div>
+            <div className="bolhas" ref={bolhas} aria-live="polite">
+              {aberta.messages.map((m: Mensagem) => <div key={m.id} data-message-id={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>
+                <div>{m.content}</div>
+                <div className="suave">{new Date(m.createdAt).toLocaleString('pt-BR')}{m.authorName ? ` · ${m.authorName}` : ''}</div>
+              </div>)}
+              {aberta.messages.length === 0 && <p className="suave">Nenhuma mensagem nesta conversa.</p>}
+            </div>
+
+            {janelaFechada && <div className="aviso">Fora da janela de 24h da Meta: só dá para responder texto livre até 24h após a última mensagem da pessoa. A alternativa é disparar um modelo aprovado — isso ainda vive na Central de Modelos.</div>}
+            <form className="linha" onSubmit={responder}>
+              <input value={texto} onChange={(e) => guardarTexto(e.target.value)} placeholder={janelaFechada ? 'Janela fechada' : 'Escreva uma resposta'} disabled={Boolean(janelaFechada)} maxLength={4096} />
+              <button className="primario" disabled={Boolean(janelaFechada) || enviando || !texto.trim()}>{enviando ? 'Enviando…' : 'Enviar'}</button>
+            </form>
+            {aberta.conversa.status !== 'CLOSED' && <div className="linha">
+              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/claim`))}>Atender</button>
+              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/close`))}>Finalizar</button>
+            </div>}
+          </>}
+        </div>
+      </div>
+    </div>
+  );
+}
diff --git a/src/tempoReal.spec.ts b/src/tempoReal.spec.ts
index 65c2abf..df964e3 100644
--- a/src/tempoReal.spec.ts
+++ b/src/tempoReal.spec.ts
@@ -1,5 +1,7 @@
-import { describe, expect, it } from 'vitest';
-import { enderecoDoSocket } from './tempoReal';
+import { afterEach, describe, expect, it, vi } from 'vitest';
+import { enderecoDoSocket, ouvirTempoReal } from './tempoReal';
+
+afterEach(() => vi.unstubAllGlobals());
 
 describe('enderecoDoSocket', () => {
   it('https vira wss', () => {
@@ -17,4 +19,64 @@ describe('enderecoDoSocket', () => {
   it('barra sobrando não vira //ws', () => {
     expect(enderecoDoSocket('https://api.leadshug.com.br/', 'x')).toBe('wss://api.leadshug.com.br/ws');
   });
+
+  it('notifica a recuperação ao estabelecer e restabelecer a conexão', () => {
+    const sockets: Array<{ onopen?: () => void; onclose?: () => void; close: () => void }> = [];
+    class SocketFake {
+      onopen?: () => void;
+      onclose?: () => void;
+      constructor() { sockets.push(this); }
+      close() {}
+    }
+    const timers: Array<() => void> = [];
+    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() });
+    vi.stubGlobal('WebSocket', SocketFake as unknown as typeof WebSocket);
+    const reconnect = vi.fn();
+    const stop = ouvirTempoReal(vi.fn(), reconnect);
+
+    sockets[0].onopen?.();
+    expect(reconnect).toHaveBeenCalledTimes(1);
+    sockets[0].onclose?.();
+    timers.shift()?.();
+    sockets[1].onopen?.();
+    expect(reconnect).toHaveBeenCalledTimes(2);
+    stop();
+  });
+
+  it('descarta callbacks tardios e reconexão quando desmonta ainda conectando', () => {
+    const sockets: Array<{ onopen?: () => void; onclose?: () => void; onmessage?: (event: { data: string }) => void; close: () => void }> = [];
+    class SocketFake {
+      onopen?: () => void;
+      onclose?: () => void;
+      onmessage?: (event: { data: string }) => void;
+      close = vi.fn();
+      constructor() { sockets.push(this); }
+    }
+    const timers: Array<() => void> = [];
+    const clearTimeout = vi.fn();
+    const setTimeout = vi.fn((fn: () => void) => { timers.push(fn); return timers.length; });
+    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout });
+    vi.stubGlobal('WebSocket', SocketFake as unknown as typeof WebSocket);
+    const receive = vi.fn();
+    const reconnect = vi.fn();
+    const stop = ouvirTempoReal(receive, reconnect);
+    const lateOpen = sockets[0].onopen;
+    const lateMessage = sockets[0].onmessage;
+    sockets[0].onclose?.();
+    const lateClose = sockets[0].onclose;
+
+    stop();
+    timers[0]?.();
+    lateOpen?.();
+    lateMessage?.({ data: JSON.stringify({ tipo: 'mensagem', buId: 'bu', conversaId: 'conv', contato: 'x', direcao: 'IN', naoLidas: 1 }) });
+    lateClose?.();
+
+    expect(sockets).toHaveLength(1);
+    expect(receive).not.toHaveBeenCalled();
+    expect(reconnect).not.toHaveBeenCalled();
+    expect(setTimeout).toHaveBeenCalledTimes(1);
+    expect(clearTimeout).toHaveBeenCalledWith(1);
+    expect(sockets[0].close).toHaveBeenCalledTimes(2);
+  });
+
 });
diff --git a/src/tempoReal.ts b/src/tempoReal.ts
index faa1e3a..5bdafd5 100644
--- a/src/tempoReal.ts
+++ b/src/tempoReal.ts
@@ -32,7 +32,10 @@ export function enderecoDoSocket(base: string, origem: string): string {
   return `${raiz.replace(/^http/, 'ws')}/ws`;
 }
 
-export function ouvirTempoReal(aoReceber: (evento: EventoDeMensagem) => void): () => void {
+export function ouvirTempoReal(
+  aoReceber: (evento: EventoDeMensagem) => void,
+  aoReconectar?: () => void,
+): () => void {
   const url = enderecoDoSocket(BASE, window.location.origin);
 
   let ws: WebSocket | null = null;
@@ -50,7 +53,15 @@ export function ouvirTempoReal(aoReceber: (evento: EventoDeMensagem) => void): (
       console.warn('tempo real indisponível:', e);
       return;
     }
+    ws.onopen = () => {
+      if (!vivo) {
+        ws?.close();
+        return;
+      }
+      aoReconectar?.();
+    };
     ws.onmessage = (e) => {
+      if (!vivo) return;
       const evento = JSON.parse(e.data as string);
       if (evento?.tipo === 'mensagem') aoReceber(evento as EventoDeMensagem);
     };
@@ -65,6 +76,7 @@ export function ouvirTempoReal(aoReceber: (evento: EventoDeMensagem) => void): (
   return () => {
     vivo = false;
     window.clearTimeout(reconectar);
+    reconectar = undefined;
     ws?.close();
   };
 }

```

## web-app/playwright.config.ts

```
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

```

## web-app/src/api.ts

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
  setor?: { id: string; name: string } | null;
  channels: { type: string; status: string }[];
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

```

## web-app/src/telas/Inbox.tsx

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

interface Recuperacao {
  id: string;
  geracao: number;
  piso: string;
  cursor: string | null;
  dirty: boolean;
  eventos: number;
  emVoo: boolean;
  vazio?: boolean;
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
  const geracao = useRef(0);
  const buAtual = useRef('');
  const conversaAtual = useRef<string | null>(null);
  const abaAtual = useRef('QUEUED');
  const threadAtual = useRef<Thread | null>(null);
  const recuperacao = useRef<Recuperacao | null>(null);
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
    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
    r.emVoo = true;
    const eventosNoInicio = r.eventos;
    r.dirty = false;
    let paginas = 3;
    let cruzou = false;
    try {
      if (r.vazio) {
        if (r.cursor === null && paginas > 0) {
          const versao = versaoMetadados.current;
          const inicial = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          aplicarPaginaRecente(r.id, r.geracao, versao, inicial);
          r.cursor = inicial.paginacao.cursorAnterior;
          paginas -= 1;
          if (!inicial.paginacao.temAnteriores) r.cursor = null;
        }
        while (r.cursor && paginas > 0) {
          const cursor = r.cursor;
          const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          const atual = threadAtual.current;
          if (atual) guardarThread({
            ...atual,
            messages: mesclarMensagens(atual.messages, pagina.messages),
            paginacao: pagina.paginacao,
          });
          r.cursor = pagina.paginacao.cursorAnterior;
          paginas -= 1;
        }
        if (r.eventos !== eventosNoInicio || r.dirty) {
          r.cursor = null;
          setRecuperacaoPendente(true);
        } else if (!r.cursor) {
          recuperacao.current = null;
          setRecuperacaoPendente(false);
        } else {
          setRecuperacaoPendente(true);
        }
        return;
      }
      if (r.cursor === null) {
        const versao = versaoMetadados.current;
        const recente = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        aplicarPaginaRecente(r.id, r.geracao, versao, recente);
        r.cursor = recente.paginacao.cursorAnterior;
        paginas -= 1;
        cruzou = cruzouPiso(recente.messages, r.piso) || !recente.paginacao.temAnteriores;
      }
      while (!cruzou && r.cursor && paginas > 0) {
        const cursor = r.cursor;
        const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        const atual = threadAtual.current;
        if (atual) guardarThread({
          ...atual,
          messages: mesclarMensagens(atual.messages, pagina.messages),
        });
        r.cursor = pagina.paginacao.cursorAnterior;
        paginas -= 1;
        cruzou = cruzouPiso(pagina.messages, r.piso) || !pagina.paginacao.temAnteriores;
      }

      if (r.eventos !== eventosNoInicio || r.dirty) {
        // Um evento concorrente exige nova passagem recente e preserva o piso.
        r.cursor = null;
        setRecuperacaoPendente(true);
      } else if (cruzou) {
        recuperacao.current = null;
        setRecuperacaoPendente(false);
      } else {
        setRecuperacaoPendente(true);
      }
    } catch (e) {
      if (r.geracao === geracao.current && r.id === conversaAtual.current) {
        setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível atualizar o histórico. Tente novamente.');
        setRecuperacaoPendente(true);
      }
    } finally {
      r.emVoo = false;
      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.geracao === geracao.current) {
        queueMicrotask(() => void executarRecuperacaoRef.current());
      }
    }
  }, [aplicarPaginaRecente]);

  useEffect(() => { executarRecuperacaoRef.current = executarRecuperacao; }, [executarRecuperacao]);

  const reconciliar = useCallback(() => {
    const thread = threadAtual.current;
    const id = conversaAtual.current;
    if (!thread || !id) return;
    let r = recuperacao.current;
    if (!r || r.id !== id || r.geracao !== geracao.current) {
      const mensagens = thread.messages;
      if (mensagens.length === 0) {
        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, vazio: true };
        recuperacao.current = r;
        void executarRecuperacao();
        return;
      }
      const piso = mensagens.reduce((max, m) => Date.parse(m.createdAt) > Date.parse(max) ? m.createdAt : max, mensagens[0].createdAt);
      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false };
      recuperacao.current = r;
      setRecuperacaoPendente(true);
    } else {
      r.dirty = true;
      r.eventos += 1;
      if (!r.emVoo && !r.vazio) r.cursor = null;
      setRecuperacaoPendente(true);
    }
    void executarRecuperacao();
  }, [aplicarPaginaRecente, executarRecuperacao]);

  useEffect(() => {
    carregarListaRef.current = carregarLista;
    reconciliarRef.current = reconciliar;
  }, [carregarLista, reconciliar]);

  useEffect(() => {
    void carregarLista().catch(ignorarSessaoMorta);
    const t = setInterval(() => {
      void carregarLista().catch(ignorarSessaoMorta);
      if (recuperacao.current) void executarRecuperacaoRef.current();
      else reconciliar();
    }, 60_000);
    return () => clearInterval(t);
  }, [buId, aba, carregarLista, reconciliar]);

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
    guardarThread(null);
    setAbrindo(false);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    setErro(null);
    setRecuperacaoPendente(false);
    setConversas([]);
    setBuId(novoBu);
  }

  async function abrir(id: string) {
    const gen = ++geracao.current;
    conversaAtual.current = id;
    recuperacao.current = null;
    versaoMetadados.current += 1;
    guardarThread(null);
    setAbrindo(true);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    setErro(null);
    setRecuperacaoPendente(false);
    try {
      const response = await api.get<Thread>(`/conversations/${id}/messages`);
      if (gen !== geracao.current || conversaAtual.current !== id) return;
      response.messages = mesclarMensagens(response.messages);
      guardarThread(response);
      setAbrindo(false);
      void carregarLista().catch(ignorarSessaoMorta);
    } catch (e) {
      if (gen === geracao.current) {
        guardarThread(null);
        setAbrindo(false);
        setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível carregar a conversa.');
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
    setErro(null);
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
      if (gen === geracao.current) setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Falha ao carregar mensagens anteriores.');
    } finally {
      if (gen === geracao.current) setCarregandoAnteriores(false);
    }
  }

  async function agir(acao: () => Promise<unknown>) {
    const id = conversaAtual.current;
    const gen = geracao.current;
    if (!id) return;
    versaoMetadados.current += 1;
    setErro(null);
    try {
      await acao();
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) setErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
    }
  }

  async function responder(e: FormEvent) {
    e.preventDefault();
    const id = conversaAtual.current;
    const gen = geracao.current;
    const textoEnviado = textoRef.current;
    if (!id || !textoEnviado.trim() || enviando) return;
    setEnviando(true);
    setErro(null);
    try {
      await api.post(`/conversations/${id}/messages`, { texto: textoEnviado });
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      if (textoRef.current === textoEnviado) guardarTexto('');
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) setErro(e instanceof ErroDaApi ? e.message : 'Falha ao enviar mensagem.');
    } finally {
      if (gen === geracao.current) setEnviando(false);
    }
  }

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
              {recuperacaoPendente && <button onClick={() => void executarRecuperacao()}>Continuar atualização</button>}
            </div>
            <div className="bolhas" ref={bolhas} aria-live="polite">
              {aberta.messages.map((m: Mensagem) => <div key={m.id} data-message-id={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>
                <div>{m.content}</div>
                <div className="suave">{new Date(m.createdAt).toLocaleString('pt-BR')}{m.authorName ? ` · ${m.authorName}` : ''}</div>
              </div>)}
              {aberta.messages.length === 0 && <p className="suave">Nenhuma mensagem nesta conversa.</p>}
            </div>

            {janelaFechada && <div className="aviso">Fora da janela de 24h da Meta: só dá para responder texto livre até 24h após a última mensagem da pessoa. A alternativa é disparar um modelo aprovado — isso ainda vive na Central de Modelos.</div>}
            <form className="linha" onSubmit={responder}>
              <input value={texto} onChange={(e) => guardarTexto(e.target.value)} placeholder={janelaFechada ? 'Janela fechada' : 'Escreva uma resposta'} disabled={Boolean(janelaFechada)} maxLength={4096} />
              <button className="primario" disabled={Boolean(janelaFechada) || enviando || !texto.trim()}>{enviando ? 'Enviando…' : 'Enviar'}</button>
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

## web-app/src/tempoReal.spec.ts

```
import { afterEach, describe, expect, it, vi } from 'vitest';
import { enderecoDoSocket, ouvirTempoReal } from './tempoReal';

afterEach(() => vi.unstubAllGlobals());

describe('enderecoDoSocket', () => {
  it('https vira wss', () => {
    expect(enderecoDoSocket('https://api.leadshug.com.br', 'x')).toBe('wss://api.leadshug.com.br/ws');
  });

  it('http vira ws', () => {
    expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws');
  });

  it('base vazia cai na origem da página', () => {
    expect(enderecoDoSocket('', 'https://app.leadshug.com.br')).toBe('wss://app.leadshug.com.br/ws');
  });

  it('barra sobrando não vira //ws', () => {
    expect(enderecoDoSocket('https://api.leadshug.com.br/', 'x')).toBe('wss://api.leadshug.com.br/ws');
  });

  it('notifica a recuperação ao estabelecer e restabelecer a conexão', () => {
    const sockets: Array<{ onopen?: () => void; onclose?: () => void; close: () => void }> = [];
    class SocketFake {
      onopen?: () => void;
      onclose?: () => void;
      constructor() { sockets.push(this); }
      close() {}
    }
    const timers: Array<() => void> = [];
    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() });
    vi.stubGlobal('WebSocket', SocketFake as unknown as typeof WebSocket);
    const reconnect = vi.fn();
    const stop = ouvirTempoReal(vi.fn(), reconnect);

    sockets[0].onopen?.();
    expect(reconnect).toHaveBeenCalledTimes(1);
    sockets[0].onclose?.();
    timers.shift()?.();
    sockets[1].onopen?.();
    expect(reconnect).toHaveBeenCalledTimes(2);
    stop();
  });

  it('descarta callbacks tardios e reconexão quando desmonta ainda conectando', () => {
    const sockets: Array<{ onopen?: () => void; onclose?: () => void; onmessage?: (event: { data: string }) => void; close: () => void }> = [];
    class SocketFake {
      onopen?: () => void;
      onclose?: () => void;
      onmessage?: (event: { data: string }) => void;
      close = vi.fn();
      constructor() { sockets.push(this); }
    }
    const timers: Array<() => void> = [];
    const clearTimeout = vi.fn();
    const setTimeout = vi.fn((fn: () => void) => { timers.push(fn); return timers.length; });
    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout });
    vi.stubGlobal('WebSocket', SocketFake as unknown as typeof WebSocket);
    const receive = vi.fn();
    const reconnect = vi.fn();
    const stop = ouvirTempoReal(receive, reconnect);
    const lateOpen = sockets[0].onopen;
    const lateMessage = sockets[0].onmessage;
    sockets[0].onclose?.();
    const lateClose = sockets[0].onclose;

    stop();
    timers[0]?.();
    lateOpen?.();
    lateMessage?.({ data: JSON.stringify({ tipo: 'mensagem', buId: 'bu', conversaId: 'conv', contato: 'x', direcao: 'IN', naoLidas: 1 }) });
    lateClose?.();

    expect(sockets).toHaveLength(1);
    expect(receive).not.toHaveBeenCalled();
    expect(reconnect).not.toHaveBeenCalled();
    expect(setTimeout).toHaveBeenCalledTimes(1);
    expect(clearTimeout).toHaveBeenCalledWith(1);
    expect(sockets[0].close).toHaveBeenCalledTimes(2);
  });

});

```

## web-app/src/tempoReal.ts

```
import { API_BASE as BASE } from './config';

/**
 * Conexão de tempo real com o BFF.
 *
 * A autenticação é o COOKIE, mandado no handshake — nada de token na URL, que
 * vaza em log de proxy (ADR-0007). Isso funciona porque o front é subdomínio do
 * mesmo domínio da API (ADR-0015).
 *
 * O servidor só entrega evento de BU em que a pessoa tem grant, então aqui não
 * há filtro a fazer: o que chegar, chegou porque podia.
 */

export interface EventoDeMensagem {
  tipo: 'mensagem';
  buId: string;
  conversaId: string;
  contato: string;
  direcao: 'IN' | 'OUT';
  naoLidas: number;
}

/**
 * Monta o endereço do socket por texto, e não mexendo em `url.protocol`.
 *
 * Trocar o esquema de um `URL` já construído é onde isso quebra em silêncio: se
 * a troca não pega, sobra `https://…` e o `new WebSocket` lança — dentro de um
 * efeito, o que derruba a tela inteira.
 */
export function enderecoDoSocket(base: string, origem: string): string {
  const raiz = (base || origem).replace(/\/+$/, '');
  return `${raiz.replace(/^http/, 'ws')}/ws`;
}

export function ouvirTempoReal(
  aoReceber: (evento: EventoDeMensagem) => void,
  aoReconectar?: () => void,
): () => void {
  const url = enderecoDoSocket(BASE, window.location.origin);

  let ws: WebSocket | null = null;
  let reconectar: number | undefined;
  let vivo = true;

  const conectar = () => {
    if (!vivo) return;
    // Tempo real é conforto, não requisito: se ele falhar, a tela continua de
    // pé com o poll. Um throw aqui derrubaria a aplicação inteira, porque isto
    // roda dentro de um efeito.
    try {
      ws = new WebSocket(url);
    } catch (e) {
      console.warn('tempo real indisponível:', e);
      return;
    }
    ws.onopen = () => {
      if (!vivo) {
        ws?.close();
        return;
      }
      aoReconectar?.();
    };
    ws.onmessage = (e) => {
      if (!vivo) return;
      const evento = JSON.parse(e.data as string);
      if (evento?.tipo === 'mensagem') aoReceber(evento as EventoDeMensagem);
    };
    // Reconecta sozinho: deploy, queda de rede e suspensão do notebook fecham o
    // socket, e a tela não pode ficar muda esperando um F5.
    ws.onclose = () => {
      if (vivo) reconectar = window.setTimeout(conectar, 3000);
    };
  };
  conectar();

  return () => {
    vivo = false;
    window.clearTimeout(reconectar);
    reconectar = undefined;
    ws?.close();
  };
}

```

## web-app/e2e/timeline-freshness.ts

```
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
import { mkdir, readdir, readFile, writeFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';

const hash = (value: Buffer | string) => createHash('sha256').update(value).digest('hex');

async function manifest(directory: string): Promise<Array<{ path: string; sha256: string }>> {
  const entries: Array<{ path: string; sha256: string }> = [];
  async function visit(current: string): Promise<void> {
    for (const entry of await readdir(current, { withFileTypes: true })) {
      const absolute = join(current, entry.name);
      if (entry.isDirectory()) await visit(absolute);
      else entries.push({ path: absolute.slice(directory.length + 1), sha256: hash(await readFile(absolute)) });
    }
  }
  await visit(directory);
  return entries.sort((a, b) => a.path.localeCompare(b.path));
}

function changedSourceFiles(directory: string): Array<{ path: string; sha256: string }> {
  const gitArgs = ['-c', `safe.directory=${directory}`, '-C', directory];
  const changed = execFileSync('git', [...gitArgs, 'diff', '--name-only', '--diff-filter=ACDMRTUXB'], { encoding: 'utf8' }).trim().split('\n').filter(Boolean);
  const untracked = execFileSync('git', [...gitArgs, 'ls-files', '--others', '--exclude-standard'], { encoding: 'utf8' }).trim().split('\n').filter(Boolean);
  const files = [...new Set([...changed, ...untracked])].filter((path) => /^(src\/|test\/|e2e\/|[^/]*config\.[^/]+$)/.test(path));
  return files.sort().map((path) => ({ path, sha256: hash(readFileSync(resolve(directory, path))) }));
}

export default async function timelineFreshness(): Promise<void> {
  const web = process.cwd();
  const root = resolve(web, '..');
  const api = join(root, 'api-app');
  const runtime = process.version;
  if (!/^v22\./.test(runtime)) throw new Error(`Attestation timeline exige Node 22; recebeu ${runtime}`);

  const databaseUrl = process.env.LEADSHUG_E2E_DATABASE_URL;
  if (!databaseUrl) throw new Error('LEADSHUG_E2E_DATABASE_URL ausente durante attestation.');
  const db = new URL(databaseUrl);
  const database = decodeURIComponent(db.pathname.slice(1));
  if (!database.startsWith('leadshug_timeline_')) throw new Error(`Banco fora da família descartável: ${database}`);

  const apiPort = process.env.LEADSHUG_API_PORT ?? '3100';
  const apiEndpoint = `http://127.0.0.1:${apiPort}`;
  const [apiHealth, fixtureHealth, htmlResponse] = await Promise.all([
    fetch(`${apiEndpoint}/health`),
    fetch('http://127.0.0.1:3101/health'),
    fetch('http://127.0.0.1:4173/'),
  ]);
  for (const [label, response] of [['API', apiHealth], ['fixtures', fixtureHealth], ['preview', htmlResponse]] as const) {
    if (!response.ok) throw new Error(`${label} indisponível na attestation: HTTP ${response.status}`);
  }
  const html = await htmlResponse.text();
  const asset = html.match(/src="([^"]+\.js)"/);
  if (!asset) throw new Error('HTML servido não referencia o bundle JavaScript esperado.');
  const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173'));
  if (!jsResponse.ok) throw new Error(`Bundle servido retornou HTTP ${jsResponse.status}`);
  const servedJs = Buffer.from(await jsResponse.arrayBuffer());
  const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`);
  const distJs = await readFile(servedPath);
  if (hash(servedJs) !== hash(distJs)) throw new Error('Bundle servido não corresponde ao artefato em web-app/dist.');

  const gitArgs = (directory: string, ...args: string[]) => ['-c', `safe.directory=${directory}`, '-C', directory, ...args];
  const git = (directory: string, ...args: string[]) => execFileSync('git', gitArgs(directory, ...args), { encoding: 'utf8' }).trim();
  const diffHash = (directory: string) => hash(execFileSync('git', gitArgs(directory, 'diff', '--no-ext-diff', '--binary')));
  const requireFromApi = createRequire(join(api, 'package.json'));
  const { PrismaClient } = requireFromApi('@prisma/client') as { PrismaClient: new (options: { datasources: { db: { url: string } } }) => any };
  const prisma = new PrismaClient({ datasources: { db: { url: databaseUrl } } });
  let completedMigrations: number;
  try {
    const rows = await prisma.$queryRawUnsafe('SELECT COUNT(*)::int AS count FROM "_prisma_migrations" WHERE finished_at IS NOT NULL AND rolled_back_at IS NULL') as Array<{ count: number }>;
    completedMigrations = Number(rows[0]?.count ?? 0);
  } finally {
    await prisma.$disconnect();
  }

  const artifactDirectory = resolve(root, 'foundation_documentation/artifacts/tmp/inbox-timeline-execution');
  await mkdir(artifactDirectory, { recursive: true });
  await writeFile(join(artifactDirectory, 'served-index-authority.html'), html);
  await writeFile(join(artifactDirectory, 'served-app-authority.js'), servedJs);
  const runId = process.env.LEADSHUG_ATTESTATION_RUN_ID ?? new Date().toISOString().replace(/[:.]/g, '-');
  if (!/^[A-Za-z0-9_-]+$/.test(runId)) throw new Error('LEADSHUG_ATTESTATION_RUN_ID contém caracteres inválidos.');
  const attestation = {
    capturedAtUtc: new Date().toISOString(),
    runId,
    branch: {
      api: { name: git(api, 'branch', '--show-current'), head: git(api, 'rev-parse', 'HEAD'), diffSha256: diffHash(api), sourceManifest: changedSourceFiles(api) },
      web: { name: git(web, 'branch', '--show-current'), head: git(web, 'rev-parse', 'HEAD'), diffSha256: diffHash(web), sourceManifest: changedSourceFiles(web) },
    },
    runtime,
    database: { name: database, endpoint: `${db.protocol}//${db.hostname}:${db.port || '5432'}/${database}`, completedMigrations },
    endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname },
    servedBundleSha256: hash(servedJs),
    distBundleSha256: hash(distJs),
    apiBuildManifest: await manifest(join(api, 'dist')),
    webDistManifest: await manifest(join(web, 'dist')),
  };
  const serialized = `${JSON.stringify(attestation, null, 2)}\n`;
  await writeFile(join(artifactDirectory, `attestation-browser-${runId}.json`), serialized);
  await writeFile(join(artifactDirectory, 'attestation-browser-authority.json'), serialized);
}

```

## web-app/e2e/timeline.spec.ts

```
import { expect, test, type Page, type APIRequestContext } from '@playwright/test';

const FIXTURES = 'http://127.0.0.1:3101';
const TOKEN_INTERNO = 'token-de-e2e';
const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`;

async function seed(request: APIRequestContext, count = 251, tied = false) {
  const response = await request.post(`${FIXTURES}/seed`, { data: { count, tied } });
  expect(response.status()).toBe(201);
  return response.json() as Promise<{
    email: string; password: string; userId: string; businessUnitId: string; conversationId: string;
    otherConversationId: string; otherBusinessUnitId: string; otherBuConversationId: string;
    phoneNumberId: string; expectedIds: string[];
  }>;
}

async function login(page: Page, email: string, password: string, businessUnitId: string) {
  await page.context().clearCookies();
  await page.goto('/login');
  await page.getByLabel('E-mail').fill(email);
  await page.getByLabel('Senha').fill(password);
  await page.getByRole('button', { name: 'Entrar' }).click();
  await expect(page).toHaveURL(/\/inbox$/);
  await page.getByLabel('Business Unit').selectOption(businessUnitId);
}

async function abrirTimeline(page: Page, request: APIRequestContext, count = 251, tied = false) {
  const fixture = await seed(request, count, tied);
  await login(page, fixture.email, fixture.password, fixture.businessUnitId);
  await page.getByRole('button', { name: 'Cliente Timeline' }).click();
  await expect(page.locator('.bolha')).toHaveCount(Math.min(50, count));
  return fixture;
}

async function audit(request: APIRequestContext, conversationId: string) {
  return request.get(`${FIXTURES}/audit?conversationId=${encodeURIComponent(conversationId)}`).then((r) => r.json());
}

async function triggerIncoming(request: APIRequestContext, data: Record<string, unknown>) {
  const response = await request.post(`${FIXTURES}/incoming`, { data });
  expect(response.status()).toBe(200);
  const webhook = await response.json() as { status: number; body: string };
  expect(webhook.status).toBe(200);
  expect(webhook.body).toBe('EVENT_RECEIVED');
}

test.describe('timeline da inbox com backend e PostgreSQL reais', () => {
  test.describe.configure({ timeout: 120_000 });
  let pageErrors: string[];
  test.beforeEach(async ({ page }) => {
    pageErrors = [];
    page.on('pageerror', (e) => pageErrors.push(e.message));
  });
  test.afterEach(async () => expect(pageErrors).toEqual([]));

  test('expõe o estado de abertura enquanto a primeira página aguarda o backend', async ({ page, request }) => {
    const fixture = await seed(request, 3);
    await login(page, fixture.email, fixture.password, fixture.businessUnitId);
    let liberar!: () => void;
    let iniciou!: () => void;
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const solicitacao = new Promise<void>((resolve) => { iniciou = resolve; });
    const rotaAbertura = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route(rotaAbertura, async (route) => {
      const response = await route.fetch();
      iniciou();
      await continua;
      await route.fulfill({ response });
    });
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    await solicitacao;
    await expect(page.getByRole('status').filter({ hasText: 'Abrindo conversa…' })).toBeVisible();
    liberar();
    await expect(page.locator('.bolha')).toHaveCount(3);
  });

  test('abre a página recente, carrega todas as páginas anteriores e preserva posição', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251, true);
    const timeline = page.locator('.bolhas');
    await timeline.evaluate((el) => { el.scrollTop = 90; });
    const anchor = await timeline.evaluate((el) => {
      const box = el.getBoundingClientRect();
      const child = [...el.querySelectorAll<HTMLElement>('.bolha')].find((item) => item.getBoundingClientRect().bottom > box.top);
      return child ? { id: child.dataset.messageId, offset: child.getBoundingClientRect().top - box.top } : null;
    });
    expect(anchor).not.toBeNull();
    let paginas = 0;
    while (await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).count()) {
      await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
      await expect(page.locator('.bolha')).toHaveCount(Math.min(251, 50 * (paginas + 2)));
      if (paginas === 0 && anchor) {
        await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));
        const depois = await timeline.locator(`[data-message-id="${anchor.id}"]`).evaluate((el) => {
          const pai = el.parentElement!;
          return el.getBoundingClientRect().top - pai.getBoundingClientRect().top;
        });
        expect(Math.abs(depois - anchor.offset)).toBeLessThan(2);
      }
      paginas += 1;
      expect(paginas).toBeLessThan(8);
    }
    await expect(page.getByText('Início do histórico')).toBeVisible();
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(fixture.expectedIds);
    expect(await audit(request, fixture.conversationId).then((r) => r.messages.length)).toBe(251);
  });

  test('reconecta sem evento posterior e recupera 130 mensagens em mais de uma rodada', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251, true);
    const timeline = page.locator('.bolhas');
    const cdp = await page.context().newCDPSession(page);
    await cdp.send('Network.enable');
    await cdp.send('Network.emulateNetworkConditions', { offline: true, latency: 0, downloadThroughput: 0, uploadThroughput: 0 });
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 130, createdAt: Date.now() + 10_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-reconnect-event', text: 'evento para disparar a reconexão' });
    await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: 0, downloadThroughput: -1, uploadThroughput: -1 });

    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible({ timeout: 25_000 });
    // A passagem excedeu o orçamento de três páginas; cada continuação mantém o piso T.
    for (let i = 0; i < 10 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i++) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(150);
    }
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await timeline.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toHaveLength(382);
    expect(expected.unreadCount).toBe(1);
  });

  test('o poll retoma uma rodada pendente sem evento novo nem clique de continuação', async ({ page, request }) => {
    await page.clock.install();
    const fixture = await abrirTimeline(page, request, 251, true);
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 130, createdAt: Date.now() + 10_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-poll-head', text: 'evento que inicia a recuperação via poll' });
    const pending = page.getByText('Atualização pendente. O histórico pode ter uma lacuna.');
    await expect(pending).toBeVisible({ timeout: 25_000 });
    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();

    for (let i = 0; i < 5 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
      await page.clock.fastForward(60_000);
      await expect.poll(async () => await page.locator('.bolha').count()).toBeGreaterThan(50 + i * 100);
    }
    await expect(pending).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toHaveLength(382);
    expect(expected.unreadCount).toBe(1);
  });

  test('recupera o histórico completo após uma thread vazia receber mais de uma página', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 0);
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 130, createdAt: Date.now() - 10_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-first-after-empty', text: 'primeira mensagem depois da abertura vazia' });
    await expect(page.locator('.bolha')).toHaveCount(131, { timeout: 25_000 });
    await expect(page.getByText('Início do histórico')).toBeVisible();
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(expected.unreadCount).toBe(1);
  });

  test('preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido', async ({ page, request }) => {
    const fixture = await seed(request, 251, true);
    let mensagensRecebidas = 0;
    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
      try {
        const frame = JSON.parse(String(payload)) as { tipo?: string; conversaId?: string };
        if (frame.tipo === 'mensagem' && frame.conversaId === fixture.conversationId) mensagensRecebidas += 1;
      } catch { /* os frames de conexão não representam mensagens */ }
    }));
    await login(page, fixture.email, fixture.password, fixture.businessUnitId);
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    await expect(page.locator('.bolha')).toHaveCount(50);
    let pagesBeforeCursor = 0;
    let liberar!: () => void;
    let aguardeSegundaPagina!: () => void;
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const segundaPagina = new Promise<void>((resolve) => { aguardeSegundaPagina = resolve; });
    let lateId = '';
    const piso = new Date('2026-10-14T12:00:00.000Z').toISOString();
    const rotaPaginaAnterior = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
    await page.route(rotaPaginaAnterior, async (route) => {
      pagesBeforeCursor += 1;
      if (pagesBeforeCursor !== 2) return route.continue();
      const response = await route.fetch();
      const cursor = new URL(route.request().url()).searchParams.get('antes')!;
      const cursorPayload = JSON.parse(Buffer.from(cursor.slice(3), 'base64url').toString('utf8')) as { m: string };
      const min = BigInt(`0x${cursorPayload.m.replaceAll('-', '')}`);
      const max = BigInt(`0x${fixture.expectedIds.at(-1)!.replaceAll('-', '')}`);
      lateId = ((min + max) / 2n).toString(16).padStart(32, '0').replace(/(.{8})(.{4})(.{4})(.{4})(.{12})/, '$1-$2-$3-$4-$5');
      expect(lateId > cursorPayload.m).toBe(true);
      expect(lateId < fixture.expectedIds.at(-1)!).toBe(true);
      expect(fixture.expectedIds).not.toContain(lateId);
      await request.post(`${FIXTURES}/late-tie`, { data: { conversationId: fixture.conversationId, id: lateId, createdAt: piso } });
      // Dez mensagens reais chegam enquanto a passagem está aberta. O navegador
      // recebe cada push e deve coalescer a recuperação sem perder o piso T.
      for (let i = 1; i <= 10; i += 1) {
        await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-dirty-${i}`, text: `evento coalescido ${i}` });
      }
      await expect.poll(() => mensagensRecebidas).toBe(11); // H + dez eventos durante a passagem
      aguardeSegundaPagina();
      await continua;
      await route.fulfill({ response });
    });
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-head-H', text: 'nova cabeça H maior que T' });
    await segundaPagina;
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
    liberar();
    for (let i = 0; i < 12 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i++) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(100);
    }
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toContain(lateId);
    expect(expected.unreadCount).toBe(11);
  });

  test('preserva a âncora quando uma mensagem chega durante o backfill atrasado', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251);
    const timeline = page.locator('.bolhas');
    let iniciar!: () => void;
    let liberar!: () => void;
    const chegou = new Promise<void>((resolve) => { iniciar = resolve; });
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const rota = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
    await page.route(rota, async (route) => {
      const response = await route.fetch();
      iniciar();
      await continua;
      await route.fulfill({ response });
    });
    await timeline.evaluate((el) => { el.scrollTop = 80; });
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await chegou;
    await timeline.evaluate((el) => { el.scrollTop = 130; });
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-arrival-during-backfill', text: 'mensagem recebida durante backfill' });
    await expect(page.locator('.bolha')).toHaveCount(51, { timeout: 25_000 });
    const anchor = await timeline.evaluate((el) => {
      const bounds = el.getBoundingClientRect();
      const visible = [...el.querySelectorAll<HTMLElement>('.bolha')].find((item) => item.getBoundingClientRect().bottom > bounds.top);
      return visible ? { id: visible.dataset.messageId, offset: visible.getBoundingClientRect().top - bounds.top } : null;
    });
    expect(anchor).not.toBeNull();
    liberar();
    await expect(page.locator('.bolha')).toHaveCount(101);
    await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));
    const offset = await timeline.locator(`[data-message-id="${anchor!.id}"]`).evaluate((el) => el.getBoundingClientRect().top - el.parentElement!.getBoundingClientRect().top);
    expect(Math.abs(offset - anchor!.offset)).toBeLessThan(2);
  });

  test('mescla envio real com autoria e mantém o novo draft digitado durante o envio', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 4);
    let liberado!: () => void;
    let capturado!: () => void;
    const pronta = new Promise<void>((resolve) => { capturado = resolve; });
    const trava = new Promise<void>((resolve) => { liberado = resolve; });
    await page.route(`**/api/bff/conversations/${fixture.conversationId}/messages`, async (route) => {
      if (route.request().method() !== 'POST') return route.continue();
      const response = await route.fetch();
      capturado();
      await trava;
      await route.fulfill({ response });
    });
    const input = page.getByPlaceholder('Escreva uma resposta');
    await input.fill('resposta persistida');
    await page.getByRole('button', { name: 'Enviar' }).click();
    await pronta;
    await input.fill('rascunho novo');
    liberado();
    await expect(page.locator('.bolha').filter({ hasText: 'resposta persistida' })).toHaveCount(1);
    await expect(input).toHaveValue('rascunho novo');
    const gravado = await audit(request, fixture.conversationId);
    expect(gravado.messages.some((m: { content: string; direction: string; authorName: string }) =>
      m.content === 'resposta persistida' && m.direction === 'OUT' && m.authorName === 'Atendente Timeline')).toBe(true);
  });

  test('mostra thread vazia/fim, falha recuperável e acesso perdido', async ({ page, request }) => {
    const vazia = await abrirTimeline(page, request, 0);
    await expect(page.getByText('Nenhuma mensagem nesta conversa.')).toBeVisible();
    await expect(page.getByText('Início do histórico')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Carregar mensagens anteriores' })).toHaveCount(0);

    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    const cheia = await audit(request, vazia.conversationId);
    expect(cheia.messages).toHaveLength(0);

    const fixture = await abrirTimeline(page, request, 51);
    const caminho = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
    await page.route(caminho, (route) => route.abort('failed'));
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await expect(page.getByText('Falha ao carregar mensagens anteriores.')).toBeVisible();
    await page.unroute(caminho);
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await expect(page.locator('.bolha')).toHaveCount(51);
    await expect(page.getByText('Início do histórico')).toBeVisible();

    const perdida = await abrirTimeline(page, request, 51);
    await request.post(`${FIXTURES}/revoke`, { data: { userId: perdida.userId, businessUnitId: perdida.businessUnitId } });
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await expect(page.getByText('Acesso à conversa perdido.')).toBeVisible();
  });

  test('close vence resposta de backfill atrasada', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251);
    let liberarBackfill!: () => void;
    let backfillRecebido!: () => void;
    const continua = new Promise<void>((resolve) => { liberarBackfill = resolve; });
    const chegou = new Promise<void>((resolve) => { backfillRecebido = resolve; });
    const rotaBackfill = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
    await page.route(rotaBackfill, async (route) => {
      const response = await route.fetch();
      backfillRecebido();
      await continua;
      await route.fulfill({ response });
    });
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await chegou;
    await page.getByRole('button', { name: 'Finalizar' }).click();
    await expect.poll(async () => (await audit(request, fixture.conversationId)).status).toBe('CLOSED');
    liberarBackfill();
    await expect(page.getByText('CLOSED', { exact: true })).toBeVisible();
  });

  test('troca de conversa e BU protege resposta atrasada de envio', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251);
    let liberarEnvio!: () => void;
    let envioRecebido!: () => void;
    const continuaEnvio = new Promise<void>((resolve) => { liberarEnvio = resolve; });
    const chegouEnvio = new Promise<void>((resolve) => { envioRecebido = resolve; });
    await page.route(`**/api/bff/conversations/${fixture.otherConversationId}/messages`, async (route) => {
      if (route.request().method() !== 'POST') return route.continue();
      const response = await route.fetch();
      envioRecebido();
      await continuaEnvio;
      await route.fulfill({ response });
    });
    // A chamada persistida chega atrasada ao cliente, depois de o usuário trocar de conversa.
    const outra = fixture.otherConversationId;
    await page.getByRole('button', { name: 'Cliente Secundário' }).click();
    const draft = page.getByPlaceholder('Escreva uma resposta');
    await draft.fill('envio durante troca');
    await page.getByRole('button', { name: 'Enviar' }).click();
    await chegouEnvio;
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    liberarEnvio();
    await expect(page.locator('.item.ativo')).toContainText('Cliente Timeline');
    await expect(page.locator('.bolha').filter({ hasText: 'envio durante troca' })).toHaveCount(0);
    const enviado = await audit(request, outra);
    expect(enviado.messages.some((m: { content: string; direction: string }) => m.content === 'envio durante troca' && m.direction === 'OUT')).toBe(true);

    let liberarEnvioBu!: () => void;
    let envioBuRecebido!: () => void;
    const continuaBu = new Promise<void>((resolve) => { liberarEnvioBu = resolve; });
    const chegouBu = new Promise<void>((resolve) => { envioBuRecebido = resolve; });
    const buRequest = `**/api/bff/conversations/${fixture.otherConversationId}/messages`;
    await page.route(buRequest, async (route) => {
      if (route.request().method() !== 'POST') return route.continue();
      const response = await route.fetch();
      envioBuRecebido();
      await continuaBu;
      await route.fulfill({ response });
    });
    await page.getByRole('button', { name: 'Em atendimento' }).click();
    await page.getByRole('button', { name: 'Cliente Secundário' }).click();
    await page.getByPlaceholder('Escreva uma resposta').fill('envio durante troca de BU');
    await page.getByRole('button', { name: 'Enviar' }).click();
    await chegouBu;
    await page.getByLabel('Business Unit').selectOption({ label: 'Número alternativo' });
    await page.getByRole('button', { name: 'Na fila' }).click();
    await page.getByRole('button', { name: 'Cliente Outra BU' }).click();
    liberarEnvioBu();
    await expect(page.locator('.item.ativo')).toContainText('Cliente Outra BU');
    await expect(page.locator('.bolha').filter({ hasText: 'envio durante troca de BU' })).toHaveCount(0);
    const crossBuSent = await audit(request, fixture.otherConversationId);
    expect(crossBuSent.messages.some((m: { content: string }) => m.content === 'envio durante troca de BU')).toBe(true);
  });
});

```

## web-app/src/timeline.test.ts

```
import { describe, expect, it } from 'vitest';
import { cruzouPiso, mesclarMensagens } from './timeline';
import type { Mensagem } from './api';

const msg = (id: string, createdAt: string): Mensagem => ({
  id, createdAt, direction: 'IN', content: id, channelOrigin: 'OFICIAL', authorName: null,
});

describe('timeline da inbox', () => {
  it('mescla por ID e ordena estavelmente por timestamp e ID', () => {
    const empatada = '2026-01-01T00:00:00.000Z';
    expect(mesclarMensagens([msg('b', empatada), msg('a', empatada)], [msg('b', empatada), msg('c', '2026-01-02T00:00:00.000Z')]).map((m) => m.id))
      .toEqual(['a', 'b', 'c']);
  });

  it('só cruza a cobertura quando alcança timestamp estritamente anterior ao piso', () => {
    expect(cruzouPiso([msg('x', '2026-01-01T00:00:00.000Z')], '2026-01-01T00:00:00.000Z')).toBe(false);
    expect(cruzouPiso([msg('x', '2025-12-31T23:59:59.999Z')], '2026-01-01T00:00:00.000Z')).toBe(true);
  });
});

```

## web-app/src/timeline.ts

```
import type { Mensagem } from './api';

export function mesclarMensagens(...grupos: Mensagem[][]): Mensagem[] {
  const porId = new Map<string, Mensagem>();
  for (const grupo of grupos) for (const mensagem of grupo) porId.set(mensagem.id, mensagem);
  return [...porId.values()].sort((a, b) => {
    const tempo = Date.parse(a.createdAt) - Date.parse(b.createdAt);
    return tempo || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
  });
}

export function cruzouPiso(mensagens: Mensagem[], piso: string): boolean {
  return mensagens.some((mensagem) => Date.parse(mensagem.createdAt) < Date.parse(piso));
}

```

## web-app/package.json

```
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

```

## api-app/test/helpers.ts

```
import { INestApplication } from '@nestjs/common';
import { Test } from '@nestjs/testing';
import type { NestExpressApplication } from '@nestjs/platform-express';
import request from 'supertest';
import { AppModule } from '../src/app.module';
import { configurarBodyParsers } from '../src/infra/http/body-parsers';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { EVOLUTION_CLIENT, EvolutionClient } from '../src/integrations/evolution/evolution.client';
import { META_CLIENT, MetaClient } from '../src/integrations/meta/meta.client';

/** Dublês das portas de saída: o teste prova permissão, não a Meta. */
export const metaFake: MetaClient & { wabaRecusada: string | null; enviados: { para: string; texto: string }[] } = {
  wabaRecusada: null,
  enviados: [],
  async enviarTexto(_phoneNumberId: string, para: string, texto: string) {
    metaFake.enviados.push({ para, texto });
    return `wamid-enviado-${metaFake.enviados.length}`;
  },
  configurado: () => true,
  async numerosDaWaba(wabaId: string) {
    if (metaFake.wabaRecusada === wabaId) throw new Error('WABA recusada');
    return [{ id: `phone-${wabaId}`, telefone: '5584999990000', nomeVerificado: 'Teste' }];
  },
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

## api-app/src/surfaces/bff/bff.module.ts

```
import { MiddlewareConsumer, Module, NestModule, RequestMethod } from '@nestjs/common';
import { AccessService } from '../../domain/access/access.service';
import { IdentityService } from '../../domain/identity/identity.service';
import { LoginAttemptService } from '../../domain/identity/login-attempt.service';
import { PasswordService } from '../../domain/identity/password.service';
import { SessionService } from '../../infra/session/session.service';
import { ChannelsService } from '../../domain/channels/channels.service';
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

## api-app/src/surfaces/public/conversations.controller.ts

```
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

## api-app/src/domain/inbox/incoming.service.ts

```
import { Inject, Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { RealtimeService } from '../../realtime/realtime.service';
import { META_CLIENT, MetaClient } from '../../integrations/meta/meta.client';
import { TYPEBOT_CLIENT, TypebotClient } from '../../integrations/typebot/typebot.client';

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
  ) {}

  async registrar(m: MensagemRecebida) {
    const existente = await this.prisma.conversation.findUnique({
      where: { buId_contact: { buId: m.buId, contact: m.contato } },
    });

    // Mensagem nova do contato REABRE a conversa fechada e solta a atribuição:
    // ela volta "ao balcão", não necessariamente para quem atendeu antes. Uma
    // conversa em atendimento NÃO é rebaixada por mensagem nova (ADR-0009 §2).
    const reabrindo = existente?.status === 'CLOSED' && m.direcao === 'IN' && !m.ehGrupo;

    const conversa = await this.prisma.conversation.upsert({
      where: { buId_contact: { buId: m.buId, contact: m.contato } },
      create: {
        buId: m.buId,
        contact: m.contato,
        contactType: m.ehGrupo ? 'GRUPO' : 'PESSOA',
        displayName: m.nomeExibicao ?? null,
        status: m.direcao === 'IN' ? 'QUEUED' : 'IN_SERVICE',
        unreadCount: m.direcao === 'IN' ? 1 : 0,
        lastMessageAt: new Date(),
      },
      update: {
        displayName: m.nomeExibicao ?? undefined,
        lastMessageAt: new Date(),
        unreadCount: m.direcao === 'IN' ? { increment: 1 } : undefined,
        status: reabrindo ? 'QUEUED' : undefined,
        attendantUserId: reabrindo ? null : undefined,
        attendantName: reabrindo ? null : undefined,
        attendantOrigin: reabrindo ? null : undefined,
      },
    });

    const mensagem = await this.prisma.message.create({
      data: {
        conversationId: conversa.id,
        // Denormalizado do conversation para que TODA tabela de dado de negócio
        // tenha bu_id — é o que a regra 0 exige para poder filtrar sempre.
        buId: m.buId,
        direction: m.direcao,
        messageType: m.tipo,
        content: m.conteudo ?? null,
        channelOrigin: m.canal,
        status: m.direcao === 'IN' ? 'RECEBIDA' : 'ENVIADA',
        externalId: m.externalId ?? null,
        authorName: m.autorNome ?? null,
      },
    });

    // Só quem tem grant nesta BU recebe. O push respeita o mesmo escopo do REST.
    this.realtime.publicarNaBu(m.buId, {
      tipo: 'mensagem',
      conversaId: conversa.id,
      contato: conversa.contact,
      direcao: m.direcao,
      canal: m.canal,
      naoLidas: conversa.unreadCount,
    });

    if (m.canal === 'OFICIAL' && m.direcao === 'IN' && m.tipo === 'TEXTO' && m.conteudo?.trim()) {
      await this.executarTypebot(m.buId, m.contato, m.conteudo.trim(), !existente).catch(() => undefined);
    }

    return { conversa, mensagem, reabriu: reabrindo };
  }

  private async executarTypebot(buId: string, contato: string, texto: string, novaConversa: boolean): Promise<void> {
    const gatilhos = await this.prisma.typebotTrigger.findMany({
      where: { active: true, bot: { status: 'ATIVO' }, OR: [{ buId: null }, { buId }] },
      include: { bot: true }, orderBy: { createdAt: 'asc' },
    });
    const normalized = texto.toLocaleLowerCase('pt-BR');
    const gatilho = gatilhos.find((g) => gatilhoCombina(g.kind, g.value, normalized, novaConversa));
    if (!gatilho || !this.typebot.configurado()) return;
    const canal = await this.prisma.buChannel.findFirst({ where: { buId, type: 'OFICIAL', status: 'CONECTADO' }, select: { phoneNumberId: true } });
    if (!canal?.phoneNumberId) return;
    const botId = gatilho.bot.publishedTypebotId;
    if (!botId) return;
    const atual = await this.prisma.typebotSession.findUnique({ where: { botId_buId_contato: { botId: gatilho.botId, buId, contato } } });
    const resposta = atual?.ativo ? await this.typebot.continuar(atual.sessionId, texto) : await this.typebot.iniciar(botId, contato, texto);
    const sessionId = 'sessionId' in resposta && typeof resposta.sessionId === 'string' ? resposta.sessionId : null;
    if (!atual && sessionId) await this.prisma.typebotSession.create({ data: { botId: gatilho.botId, mantenedoraId: gatilho.bot.mantenedoraId, buId, contato, sessionId } });
    for (const mensagem of resposta.messages) {
      const saida = textoDaRespostaTypebot(mensagem);
      if (!saida) continue;
      const externalId = await this.meta.enviarTexto(canal.phoneNumberId, contato, saida);
      await this.registrar({ buId, canal: 'OFICIAL', contato, ehGrupo: false, direcao: 'OUT', tipo: 'TEXTO', conteudo: saida, externalId, autorNome: 'Typebot' });
    }
  }

  /** Registra o evento cru. É o ÚNICO lugar com payload bruto (ADR-0009 §7). */
  async registrarEventoCru(canal: CanalDeOrigem, tipo: string, payload: unknown, buId?: string | null) {
    await this.prisma.webhookEvent.create({
      data: { channel: canal, eventType: tipo, payload: payload as object, buId: buId ?? null },
    });
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

## web-app/src/config.ts

```
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

```

## web-app/e2e/telas.spec.ts

```
import { expect, test } from '@playwright/test';

const TOKEN_INTERNO = 'token-de-e2e';
const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`;
const SENHA = 'senha-de-teste-1';

/** Cada corrida cria a própria conta: o banco local é compartilhado. */
async function contaNova(request: import('@playwright/test').APIRequestContext) {
  const email = `qa-${Date.now()}@teste.local`;
  const res = await request.post(`${API}/api/internal/mantenedoras`, {
    headers: { 'x-internal-token': TOKEN_INTERNO, 'x-requested-with': 'e2e' },
    data: {
      nome: `QA ${Date.now()}`,
      bu: { nome: 'Número de QA' },
      owner: { nome: 'QA', email, senha: SENHA },
    },
  });
  expect(res.status()).toBe(201);
  return { email, ...(await res.json()) };
}

/**
 * Entra e passa pelo WIZARD, que toda conta nova encontra (ADR-0016 §4).
 *
 * A conta nasce com o onboarding pendente, e o BFF responde 409 em tudo até ele
 * terminar — então "entrar" só chega ao produto depois desta etapa. É o mesmo
 * caminho que uma pessoa de verdade percorre.
 */
async function entrar(page: import('@playwright/test').Page, email: string) {
  await page.getByLabel('E-mail').fill(email);
  await page.getByLabel('Senha').fill(SENHA);
  await page.getByRole('button', { name: 'Entrar' }).click();

  await expect(page.getByRole('heading', { name: 'Configuração inicial' })).toBeVisible();
  for (let i = 0; i < 4; i++) await page.getByRole('button', { name: 'Continuar' }).click();
  await page.getByRole('button', { name: 'Concluir' }).click();
  // Concluir dispara um /me novo e remonta o app. Sem esperar a moldura, o
  // teste seguinte procura links que ainda não existem.
  await expect(page.getByRole('link', { name: 'Atendimento' })).toBeVisible();
}

test.describe('as telas, no navegador', () => {
  // Exceção de JavaScript é falha SEMPRE: é ela que produz a tela branca.
  let excecoes: string[] = [];
  // Já o 401 que o navegador registra quando não há sessão é esperado — é o
  // caminho normal de quem ainda não entrou. Filtrar isso é o que separa
  // "defeito" de "ruído de rede".
  let errosDeConsole: string[] = [];
  /**
   * Recusas que ESTE teste provoca de propósito.
   *
   * O filtro fixo isenta 401 e 403 — o caminho de quem ainda não entrou. Uma
   * recusa deliberada (um upload inválido, por exemplo) é da mesma natureza, mas
   * abrir 400 para todos os testes esconderia defeito de verdade. Então quem
   * provoca, declara.
   */
  let recusasEsperadas: number[] = [];

  test.beforeEach(async ({ page }) => {
    excecoes = [];
    errosDeConsole = [];
    recusasEsperadas = [];
    page.on('pageerror', (e) => excecoes.push(e.message));
    page.on('console', (m) => {
      if (m.type() !== 'error') return;
      const texto = m.text();
      if (/Failed to load resource.*(401|403)/.test(texto)) return;
      if (recusasEsperadas.some((s) => texto.includes(String(s)))) return;
      errosDeConsole.push(texto);
    });
  });

  test.afterEach(async () => {
    expect(excecoes, 'a tela não pode lançar exceção no navegador').toEqual([]);
    expect(errosDeConsole, 'a tela não pode registrar erro no console').toEqual([]);
  });

  test('sem sessão, qualquer URL leva ao login', async ({ page }) => {
    await page.goto('/inbox');
    await expect(page).toHaveURL(/\/login$/);
    await expect(page.getByRole('button', { name: 'Entrar' })).toBeVisible();
  });

  test('entrar leva de volta para a página que se queria abrir', async ({ page, request }) => {
    const conta = await contaNova(request);

    await page.goto('/consultar');
    await expect(page).toHaveURL(/\/login$/);

    await entrar(page, conta.email);

    await expect(page).toHaveURL(/\/consultar$/);
    await expect(page.getByRole('heading', { name: 'Consultar' })).toBeVisible();
  });

  test('conta nova cai no wizard, e a Revisão diz qual é o próximo passo', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await page.getByLabel('E-mail').fill(conta.email);
    await page.getByLabel('Senha').fill(SENHA);
    await page.getByRole('button', { name: 'Entrar' }).click();

    // O produto não aparece antes do wizard: painel sem módulo escolhido não tem
    // o que mostrar.
    await expect(page.getByRole('heading', { name: 'Configuração inicial' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Atendimento' })).toHaveCount(0);

    // O canal oficial é o PISO: aparece como incluído, e não como opção.
    await page.getByRole('button', { name: 'Continuar' }).click();
    await page.getByRole('button', { name: 'Continuar' }).click();
    await expect(page.getByText('Sempre incluído')).toBeVisible();

    await page.getByRole('button', { name: 'Continuar' }).click();
    await page.getByRole('button', { name: 'Continuar' }).click();
    // Quem terminar esperando mensagem chegando precisa saber que falta conectar.
    await expect(page.getByText('conectar seu primeiro número')).toBeVisible();

    await page.getByRole('button', { name: 'Concluir' }).click();
    await expect(page.getByRole('link', { name: 'Atendimento' })).toBeVisible();

    // O painel avisa o que falta, em vez de deixar a pessoa concluir que quebrou.
    await page.getByRole('link', { name: 'Painel' }).click();
    await expect(page.getByText('sem canal conectado')).toBeVisible();
  });

  /**
   * A varredura — a guarda que faltava.
   *
   * O defeito que levou `Pessoas` quebrada para stage é estrutural: as
   * interfaces do front são cópias À MÃO da resposta da API. Quando a API mudou,
   * o front continuou compilando, porque ele acredita na própria interface. O
   * typecheck não tem como pegar isso.
   *
   * Este teste abre TODA tela do menu, e o `afterEach` reprova qualquer exceção
   * de página. Uma tela nova entra aqui sozinha se estiver no menu — que é o que
   * o teste por tela, um a um, não garante.
   */
  test('toda tela do menu abre sem quebrar', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    // Pelo `href`, não pelo texto: o link do rodapé mostra nome e papel em duas
    // linhas, e o nome acessível dele não é um rótulo de menu.
    const destinos = await page.locator('.lateral a').evaluateAll((as) =>
      as.map((a) => a.getAttribute('href')).filter((h): h is string => !!h),
    );
    expect(destinos.length, 'a barra lateral não tem itens').toBeGreaterThan(5);

    for (const destino of destinos) {
      await page.locator(`.lateral a[href="${destino}"]`).click();
      await expect(page).toHaveURL(new RegExp(`${destino}$`));
      // Cada tela precisa PINTAR algo — nem branco, nem preso em "carregando…".
      await expect(page.locator('.painel main')).not.toBeEmpty();
      await expect(page.getByText('carregando…')).toHaveCount(0, { timeout: 5000 });
    }
  });

  /**
   * A paleta derivou em silêncio: a v1 nasceu azul-escura, e os nomes do desenho
   * foram mapeados para aquela paleta em vez de trazerem os VALORES dele. Nada
   * afirmava a cor, então nada reclamou.
   *
   * Os valores abaixo vêm de `docs/prd/LeadsHug.dc.html`. Se o desenho mudar,
   * este teste é o lugar onde a mudança precisa passar.
   */
  test('a paleta é a do desenho, e o tema segue a marca da conta', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    const token = (nome: string) =>
      page.evaluate(
        (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim(),
        nome,
      );

    // Verde-petróleo, tema claro — o `:root` do desenho.
    expect(await token('--brand')).toBe('#0E7363');
    expect(await token('--bg')).toBe('#EEF1F1');
    expect(await token('--text')).toBe('#12211D');
    expect(await page.locator('html').getAttribute('data-theme')).toBeNull();

    // Trocar o tema em Configurações troca o bloco inteiro de tokens.
    await page.getByRole('link', { name: 'Painel' }).click();
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    expect(await token('--brand')).toBe('#22A18A');
    expect(await token('--bg')).toBe('#121212');
  });

  test('os grupos do menu retraem, e a escolha sobrevive à navegação', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    await expect(page.getByRole('link', { name: 'Números' })).toBeVisible();
    await page.getByRole('button', { name: 'CADASTROS' }).click();
    await expect(page.getByRole('link', { name: 'Números' })).toHaveCount(0);

    // Fechado continua fechado depois de trocar de tela — quem trabalha só no
    // Atendimento não reabre os outros a cada visita.
    await page.getByRole('link', { name: 'Painel' }).click();
    await expect(page.getByRole('link', { name: 'Números' })).toHaveCount(0);

    await page.getByRole('button', { name: 'CADASTROS' }).click();
    await expect(page.getByRole('link', { name: 'Números' })).toBeVisible();
  });

  test('o tema é escolha de quem olha, e persiste', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    const bg = () =>
      page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--bg').trim());

    expect(await bg()).toBe('#EEF1F1');
    await page.getByRole('button', { name: 'Alternar tema' }).click();
    expect(await bg()).toBe('#121212');

    // Sobrevive ao recarregamento: é preferência da pessoa, guardada no
    // navegador — não configuração da conta.
    await page.reload();
    expect(await bg()).toBe('#121212');
  });

  test('Meu perfil abre pelo rodapé e salva o próprio nome', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    await page.getByRole('link', { name: 'Meu perfil' }).click();
    await expect(page.getByRole('heading', { name: 'Meu perfil' })).toBeVisible();

    // O e-mail é identidade de login: aparece, e não se edita aqui.
    await expect(page.getByLabel('E-mail')).toHaveAttribute('readonly', '');

    await page.getByLabel('Nome completo').fill('Gabriel Moura');
    await page.getByRole('button', { name: 'Salvar perfil' }).click();
    await expect(page.getByText('Perfil salvo.')).toBeVisible();

    // O nome novo aparece na barra lateral, que lê do /me.
    await expect(page.locator('.lateral')).toContainText('Gabriel Moura');
  });

  test('a foto de perfil sobe, e a recusa do servidor aparece na tela', async ({ page, request }) => {
    const conta = await contaNova(request);
    // O SVG abaixo é recusado com 400, e é isso que o teste está provando.
    recusasEsperadas = [400];

    await page.goto('/login');
    await entrar(page, conta.email);
    await page.getByRole('link', { name: 'Meu perfil' }).click();

    // PNG de 1x1 — válido pelos BYTES, que é como o servidor confere.
    const png = Buffer.from(
      'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==',
      'base64',
    );
    await page.getByLabel('Foto').setInputFiles({ name: 'foto.png', mimeType: 'image/png', buffer: png });
    await expect(page.locator('.previa img')).toBeVisible();

    await page.getByRole('button', { name: 'Salvar perfil' }).click();
    await expect(page.getByText('Perfil salvo.')).toBeVisible();

    // SVG é recusado, e a recusa é DITA: upload que some sem avisar é pior que
    // upload que não acontece.
    await page.getByLabel('Foto').setInputFiles({
      name: 'x.svg',
      mimeType: 'image/svg+xml',
      buffer: Buffer.from('<svg xmlns="http://www.w3.org/2000/svg"></svg>'),
    });
    await expect(page.getByText(/PNG, JPEG ou WebP/).last()).toBeVisible();
  });

  test('a barra lateral tem os três grupos do desenho', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    // `exact` porque o Painel também escreve "Cadastros → Números" no aviso de
    // número sem canal, e a busca por substring casaria com os dois.
    await expect(page.getByText('OPERAÇÃO', { exact: true })).toBeVisible();
    await expect(page.getByText('CADASTROS', { exact: true })).toBeVisible();
    await expect(page.getByText('CONFIGURAÇÕES', { exact: true })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Setores' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Histórico' })).toBeVisible();
  });

  test('Setores abre com o Geral, e o Histórico já mostra o que aconteceu', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    await page.getByRole('link', { name: 'Setores' }).click();
    await expect(page.getByRole('cell', { name: 'Geral' })).toBeVisible();

    await page.getByRole('link', { name: 'Histórico' }).click();
    await expect(page.getByText('concluiu a configuração inicial')).toBeVisible();
  });

  test('a inbox abre, com o número no seletor e sem conversa nenhuma', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    // Entrar cai no Atendimento.
    await expect(page).toHaveURL(/\/inbox$/);
    await expect(page.getByRole('combobox')).toContainText('Número de QA');
    await expect(page.getByText('Nada aqui.')).toBeVisible();
  });

  /**
   * As telas de CADASTROS não tinham teste de navegador, e foi por isso que
   * `Pessoas` foi para stage lendo `capacidades` — um campo que a fase 2 removeu
   * da API. O typecheck não pega: a interface era do front, e ele acreditava
   * nela. Só o navegador percorrendo a tela pega.
   */
  test('Pessoas abre, lista quem já existe e oferece os papéis que existem', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    await page.getByRole('link', { name: 'Pessoas' }).click();
    await expect(page.getByRole('heading', { name: 'Pessoas' })).toBeVisible();

    // O OWNER seedado aparece — é a linha que quebrava.
    await expect(page.getByRole('cell', { name: conta.email })).toBeVisible();

    // Três papéis, e OWNER não se concede.
    const papel = page.getByLabel('Papel');
    await expect(papel).toContainText('ATENDENTE');
    await expect(papel).toContainText('ADMIN');
    await expect(papel).not.toContainText('MEMBRO');
    await expect(papel).not.toContainText('VIEWER');
  });

  test('adicionar uma pessoa e conceder um setor a ela', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    await page.getByRole('link', { name: 'Pessoas' }).click();
    await page.getByPlaceholder('Nome').fill('Ana');
    await page.getByPlaceholder('E-mail').fill(`ana-${Date.now()}@teste.local`);
    await page.getByRole('button', { name: 'Convidar' }).click();

    await expect(page.getByRole('cell', { name: 'Ana', exact: true })).toBeVisible();

    // O `Geral` existe desde o bootstrap, então a concessão por setor já é
    // possível na primeira visita.
    await page.getByLabel('Conceder setor a Ana').selectOption({ label: 'Geral' });
    // A concessão recarrega a lista; a pessoa continua lá, agora com o acesso.
    await expect(page.getByRole('cell', { name: 'Ana', exact: true })).toBeVisible();
  });

  test('convidar mostra o LINK quando o e-mail não sai, e ele leva a definir a senha', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);
    await page.getByRole('link', { name: 'Pessoas' }).click();

    await page.getByPlaceholder('Nome').fill('Bia');
    await page.getByPlaceholder('E-mail').fill(`bia-${Date.now()}@teste.local`);
    await page.getByRole('button', { name: 'Convidar' }).click();

    // Sem RESEND_API_KEY no e2e, o envio falha — e a pessoa é criada assim
    // mesmo, com o link para repassar (ADR-0025 §4).
    await expect(page.getByText('O e-mail não saiu.')).toBeVisible();
    const link = await page.locator('code').first().textContent();
    expect(link).toContain('/definir-senha?t=');

    // O link funciona, e leva para a tela de definir senha — mesmo com a sessão
    // do ADMIN aberta neste navegador.
    const alvo = new URL(link!);
    await page.goto(alvo.pathname + alvo.search);
    await expect(page.getByRole('heading', { name: /Bem-vindo, Bia/ })).toBeVisible();
  });

  test('esqueci minha senha responde igual, exista a conta ou não', async ({ page }) => {
    await page.goto('/login');

    await page.getByLabel('E-mail').fill('ninguem@lugar-nenhum.test');
    await page.getByRole('button', { name: 'Esqueci minha senha' }).click();

    // A tela NÃO diz se a conta existe — dizer "enviamos" só quando existe
    // seria a mesma enumeração que o servidor recusa (ADR-0025 §5).
    await expect(page.getByText(/Se existir uma conta com esse e-mail/)).toBeVisible();
  });

  test('a tela de números mostra a BU e os dois canais desconectados', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);
    await page.getByRole('link', { name: 'Números' }).click();

    await expect(page.getByText('Número de QA')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Conectar WABA' })).toBeVisible();
  });

  test('sair volta para o login', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);
    await expect(page).toHaveURL(/\/inbox$/);

    await page.getByRole('button', { name: 'Sair' }).click();
    await expect(page).toHaveURL(/\/login$/);
  });

  test('identidade visual carrega e salva os campos pós-onboarding', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);
    await page.getByRole('link', { name: 'Identidade visual' }).click();
    await expect(page.getByRole('heading', { name: 'Identidade visual' })).toBeVisible();
    await page.getByLabel('Cor primária — modo claro').fill('#123456');
    await page.getByLabel('Cor primária — modo escuro').fill('#abcdef');
    await page.locator('select').selectOption('escuro');
    await page.getByRole('button', { name: 'Salvar identidade visual' }).click();
    await expect(page.getByRole('heading', { name: 'Identidade visual' })).toBeVisible();
    await page.reload();
    await expect(page.getByRole('heading', { name: 'Identidade visual' })).toBeVisible();
    await expect(page.getByLabel('Cor primária — modo claro')).toHaveValue('#123456');
    await expect(page.getByLabel('Cor primária — modo escuro')).toHaveValue('#abcdef');
    await expect.poll(async () => page.locator('html').evaluate((el) => getComputedStyle(el).getPropertyValue('--bg').trim())).toBe('#121212');
    await expect.poll(async () => page.locator('html').evaluate((el) => getComputedStyle(el).getPropertyValue('--brand').trim())).toBe('#abcdef');
  });

  test('Typebot permite buscar, abrir o editor e configurar um gatilho', async ({ page, request }) => {
    const conta = await contaNova(request);
    await page.goto('/login');
    await entrar(page, conta.email);

    // A tela Ã© testada de forma determinÃ­stica: o contrato com o provedor
    // externo jÃ¡ Ã© coberto na API, e o E2E prova a jornada do administrador.
    await page.route('**/api/bff/integracao/typebot', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          configurado: true,
          createUrl: 'https://app.typebot.com/typebots/create',
          bots: [{ id: 'bot-1', name: 'Boas-vindas', editorUrl: 'https://app.typebot.com/typebots/bot-1/edit' }],
        }),
      });
    });
    await page.route('**/api/bff/integracao/typebot/triggers', async (route) => {
      if (route.request().method() === 'POST') {
        await route.fulfill({
          status: 201,
          contentType: 'application/json',
          body: JSON.stringify({ id: 'trigger-2', botId: 'bot-1', tipo: 'PALAVRA_CHAVE', valor: 'novo', ativo: true }),
        });
        return;
      }
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ triggers: [{ id: 'trigger-1', bot: { id: 'bot-1', name: 'Boas-vindas' }, tipo: 'PALAVRA_CHAVE', valor: 'ajuda', ativo: true }] }),
      });
    });

    await page.getByRole('link', { name: 'Typebot' }).click();
    await expect(page.getByRole('heading', { name: 'Typebot' })).toBeVisible();
    await expect(page.getByText('Boas-vindas')).toBeVisible();

    await page.getByLabel('Buscar bot').fill('inexistente');
    await expect(page.getByText('Nenhum bot encontrado.')).toBeVisible();
    await page.getByLabel('Buscar bot').fill('boas');

    const editor = page.waitForEvent('popup');
    await page.getByRole('button', { name: 'Abrir editor' }).click();
    await expect((await editor).url()).toBe('https://app.typebot.com/typebots/bot-1/edit');

    const novoBot = page.waitForEvent('popup');
    await page.getByRole('button', { name: 'Criar novo bot' }).click();
    await expect((await novoBot).url()).toBe('https://app.typebot.com/typebots/create');

    await page.getByRole('button', { name: 'Configurar gatilho' }).click();
    await page.getByLabel('Tipo de gatilho de Boas-vindas').selectOption('PALAVRA_CHAVE');
    await page.getByLabel('Valor do gatilho de Boas-vindas').fill('novo');
    await page.getByRole('button', { name: 'Salvar' }).click();
    await expect(page.getByText('Gatilho salvo para Boas-vindas.')).toBeVisible();
  });
});

```

## api-app/prisma/schema.prisma

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

  @@unique([buId, type])
  @@map("bu_channels")
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
  /// Autoria: FK opcional SetNull + snapshot (ADR-0007). O payload cru NÃO
  /// mora aqui — só no log de webhook, com expurgo (ADR-0009 §7).
  authorUserId String?  @map("author_user_id")
  authorName   String?  @map("author_name")
  createdAt    DateTime @default(now()) @map("created_at")

  @@index([conversationId, createdAt])
  @@index([buId, createdAt])
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

## .github/workflows/ci.yml

```
name: Verify workspace

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  compose:
    name: Validate Compose
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate the runtime topology
        env:
          SESSION_SECRET: ci-session-secret
          INTERNAL_SERVICE_TOKEN: ci-internal-token
          WHATSAPP_TOKEN: ci-whatsapp-token
        run: docker compose config --quiet

  api:
    name: API
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Checkout the private API submodule
        env:
          SUBMODULES_REPO_TOKEN: ${{ secrets.SUBMODULES_REPO_TOKEN }}
        run: |
          test -n "$SUBMODULES_REPO_TOKEN" || {
            echo "SUBMODULES_REPO_TOKEN must read the private LeadsHug submodules." >&2
            exit 1
          }
          git config --global url."https://x-access-token:${SUBMODULES_REPO_TOKEN}@github.com/".insteadOf "https://github.com/"
          git submodule sync -- api-app
          git submodule update --init --depth=1 api-app
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: api-app/package-lock.json
      - name: Install, lint, build, and test API
        working-directory: api-app
        run: |
          npm ci
          npm run lint
          npm run build
          npm test

  web:
    name: Web
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Checkout the private Web submodule
        env:
          SUBMODULES_REPO_TOKEN: ${{ secrets.SUBMODULES_REPO_TOKEN }}
        run: |
          test -n "$SUBMODULES_REPO_TOKEN" || {
            echo "SUBMODULES_REPO_TOKEN must read the private LeadsHug submodules." >&2
            exit 1
          }
          git config --global url."https://x-access-token:${SUBMODULES_REPO_TOKEN}@github.com/".insteadOf "https://github.com/"
          git submodule sync -- web-app
          git submodule update --init --depth=1 web-app
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: web-app/package-lock.json
      - name: Install, build, and test Web
        working-directory: web-app
        run: |
          npm ci
          npm run build
          npm test

```

## delphi-ai/skills/test-quality-audit/SKILL.md

```
---
name: test-quality-audit
description: "Audit stack-aware test quality and test-first alignment so bypasses, weak assertions, false parity, and retrofit risk are blocked."
---

# Test Quality Audit

## Purpose

Detect bypasses, weak assertions, false environment parity, and retrofit risk across project-declared stacks. Judge evidence against the behavior and boundary claimed, without imposing an unrelated framework, runner, database, transport, browser, or device.

## Scope Controls

- This skill never bypasses TODO governance. If project artifacts change, follow TODO and `APROVADO` gates first.
- Treat tests as executable specifications. Prefer fail-first evidence for verifiable bugfixes, regressions, and behavior-defining changes.
- Classify audit complexity as `small|medium|big`; medium/big audits include Architecture, Code Quality, Tests, Performance, and Security framing.
- Resolve active capabilities, owning manifests, project-owned commands, and affected boundaries before applying stack-specific checks.
- Pair with `bug-fix-evidence-loop`, `test-creation-standard`, `verification-debt-audit`, or `frontend-race-condition-validation` when their scopes apply.

## Preferred Deterministic Helpers

- Run `bash delphi-ai/tools/test_quality_audit.sh`, optionally with `--scan-git-modified` or repeatable `--path <test-path>`.
- For Node/TypeScript capability ownership, run `python3 delphi-ai/tools/node_capability_surface_audit.py --repo <project-root> --expect <capability> [--manifest <relative/package.json>] [--require-script <script>]` before judging runner or script coverage.
- Exit code `2` from the static audit means medium/high signals were found. Review them; do not weaken the scope to clear the signal.

## Generic Guardrails

- `GF-01` Preflight, harness, and environment failures are blocked evidence, not product failures by default.
- `GF-02` Shared-lane validation uses canonical product surfaces; test-only product endpoints are forbidden.
- `GF-03` Parse and contract failures in reference assertions hard-fail.
- `GF-04` Required promotion gates cannot pass with flaky or retry-only outcomes.
- `GF-05` Artifact fallback paths that mask ownership or permission faults are forbidden.
- `GF-06` A narrow test or mocked boundary cannot substantiate a broader compatibility or end-to-end claim.

## Audit Workflow

1. **Frame the audit**
   - Record active capabilities, compatibility intent, changed behaviors, affected boundaries, topology, and relevant baseline decisions.
   - For large or architectural changes, require unit/provider/component plus integration/module/adapter evidence for each affected critical path.
2. **Check fail-first alignment**
   - Identify `test-first`, `test-after`, `not-applicable`, or `unknown` and the concrete assertion that demonstrates the pre-change failure.
   - Classify final-state-only tests that would not expose the bug as `retrofit-risk` unless a coherent non-applicability rationale exists.
3. **Scan for bypass flags**
   - Block committed skips, focused-test markers such as `test.only`/`describe.only`, CI golden-update bypasses, and shared-lane test-only routes.
4. **Match evidence to the claim**
   - Require real infrastructure only when compatibility or the contract crosses that boundary.
   - Verify both reachability and identity/authentication paths when those are part of the claim.
   - Do not accept unit-only evidence for a changed wiring, serialization, persistence, transport, or runtime boundary.
5. **Check fallback logic**
   - Block silent fallback from required real calls to mocks, from an owned fixture to ambient live data, or from canonical artifact paths to fallback directories.
6. **Verify dependency-injection parity**
   - Test replacements must preserve the relevant production token, scope/lifecycle, and failure semantics unless an explicit documented exception is itself asserted.
7. **Validate failure behavior**
   - Require loud failures for error payloads, empty required responses, parse errors, contract mismatches, and rejected dependencies.
   - Block no-exception-only and transport-status-only assertions when business semantics matter.
8. **Validate assertion quality**
   - Assert externally meaningful outcomes and explicit negative states.
   - Cover retriggerable asynchronous races when applicable.
   - Use deterministic owned proof subjects; do not rely on first-row, first-page, or first-candidate ambient data.
9. **Confirm environment and command parity**
   - Verify the exact project-owned runner/package-manager scripts and the topology prerequisites for the active capability.
   - Treat live hosted services, hardcoded production targets, or undeclared local substitutions as findings unless the approved baseline explicitly requires them.
10. **Audit build and runtime integrity when applicable**
    - Confirm authored tests are not stored in compiled output.
    - Match bundle/artifact metadata to the source revision and prove that manual/browser/device targets serve that build.
11. **Audit the claimed platform matrix**
    - Require evidence only for platforms in the claim, but mark any missing required platform `blocked`, never `passed`.
12. **Write issue cards for material findings**
    - Include issue ID, severity, `file:line` evidence, why-now, options A/B/C including do-nothing when reasonable, and recommendation.
13. **Record failure modes and uncertainty**
    - State likely edge cases, assumptions, unknowns, and confidence.
14. **Validate decision adherence**
    - Map each active baseline decision to `Adherent` or `Exception` with evidence. An unresolved exception is not delivery-ready.

## Conditional Stack Checks

- **NestJS:** test provider/use-case behavior, testing-module wiring, provider tokens/scopes/exports, and externally visible contracts at the chosen transport. Use the owning manifest's runner; do not assume Jest, Vitest, HTTP, Express, Fastify, Prisma, or PostgreSQL.
- **Laravel:** use the project-owned safe runner. Require a local MongoDB replica set and prohibit Atlas only when MongoDB is the declared test datastore.
- **Flutter:** require unit, widget, integration, web, or mobile lanes only where the change and platform claim demand them; use project-owned domain/scheme overrides.
- **Browser/Web:** keep test sources outside compiled bundles, use the project-owned browser runner, and require runtime freshness before accepting observations.

## Common Bypass Patterns (Block)

- Catching exceptions and continuing without failing.
- Tests that codify current buggy behavior instead of intended behavior.
- Mock or live-service fallbacks that hide required-boundary failures.
- Dependency-injection scope/token changes without explicit validation.
- Environment flags that disable required integration behavior in CI.
- Overly broad stubs that always succeed.
- Assertions that pass on empty data or ignore required state transitions.
- Ambient live-data selection for release-gating proof subjects.
- End-to-end or architectural safety claimed from unit-only evidence.
- Flaky required gates accepted as pass.
- Behavior-defining changes with no fail-first target and no rationale.

## Required Evidence

- Capability and owning-command inventory.
- Coverage/evidence matrix with deliberate exclusions.
- Proof of the real declared boundary where compatibility requires it.
- Fail-first target or explicit non-applicability rationale.
- Dependency-injection parity evidence or documented/asserted exception.
- Required platform status as `passed|blocked|failed|flaky`.
- Decision-adherence table when baseline decisions are in scope.

## Done Criteria

- No bypass remains in changed tests.
- No unresolved retrofit risk remains for behavior-defining work.
- Evidence layers substantiate, and do not overstate, the compatibility or architecture claim.
- Required real-boundary tests fail loudly on mismatch.
- Exact commands and topology match the declared project surface.
- Material findings have actionable issue cards.
- Required platform and decision evidence is complete or explicitly dispositioned.

```

## delphi-ai/skills/verification-debt-audit/SKILL.md

```
---
name: verification-debt-audit
description: "Audit verification debt across TODO evidence, tactical-note drift, waivers, and inline code TODO hygiene before closure."
---

# Verification Debt Audit

## Purpose
Detect closure-time debt that makes future maintenance slower or less trustworthy even when the immediate feature appears to work.

## Scope Controls
- This skill audits closure quality; it does not bypass TODO governance for code/doc changes.
- If the audit finds debt that requires project changes, follow the active TODO lane and approval rules before fixing it.
- Pair with `test-quality-audit` when the main debt signal is weak or retrofitted tests.
- Typical triggers:
  - `medium|big` TODOs
  - shared contract or cross-module changes
  - TODOs with waivers or provisional notes
  - code changes that introduce or leave inline `TODO|FIXME|HACK|TBD`

## Preferred Deterministic Helper
- Default audit path for TODO evidence + inline debt scanning:
  - `bash delphi-ai/tools/verification_debt_audit.sh --todo <todo-path>`
- Include changed/untracked files from the current branch in the inline debt scan:
  - `bash delphi-ai/tools/verification_debt_audit.sh --todo <todo-path> --scan-git-modified`
- Add explicit scan targets when the touched scope is narrower than the whole branch:
  - `bash delphi-ai/tools/verification_debt_audit.sh --todo <todo-path> --path <touched-path> [--path <touched-path> ...]`
- Exit code `2` means the audit completed and found `medium|high` debt signals. Treat that as evidence to review, not as automatic permission to rewrite scope.

## Debt Categories
- **Evidence debt**: claims in the TODO lack concrete proof.
- **Validation debt**: promised validation steps were skipped, weakened, or left ambiguous.
- **Waiver debt**: too many waivers, or waivers without a clear reason and expiration.
- **Promotion debt**: durable knowledge still trapped in tactical TODO notes instead of module docs.
- **Inline code TODO debt**: source contains `TODO|FIXME|HACK|TBD|XXX` without owner/next action/canonical link.
- **Closure drift**: TODO looks complete, but blockers/provisional status/evidence still indicate unresolved work.

## Audit Workflow
1. **Frame the audit**
   - Capture the active/completing TODO and its delivery stage.
   - Note whether the change touched shared contracts, cross-module surfaces, or critical user journeys.
2. **Check TODO evidence completeness**
   - Verify `Definition of Done`, `Validation Steps`, adherence tables, security risk assessment, and promotion evidence are complete enough to justify closure.
   - Flag any statement that claims success without artifact, command output, test evidence, or doc traceability.
3. **Check waiver quality**
   - Identify every waiver, `N/A`, explicit skip, or deferred verification item.
   - Flag waivers that lack:
     - why the waiver is safe now
     - what risk remains
     - when or how the waiver should be revisited
4. **Check promotion discipline**
   - Compare the TODO against touched module docs.
   - Flag durable conclusions still trapped in the TODO or comments instead of canonical docs.
5. **Scan code TODO hygiene**
   - Search touched files for inline debt markers:
     - `TODO`
     - `FIXME`
     - `HACK`
     - `TBD`
     - `XXX`
   - Classify each hit:
     - `acceptable`: local marker with clear next action and owner/context
     - `cleanup-required`: vague or stale marker that should be resolved now
     - `canonical-link-missing`: marker represents roadmap/contract knowledge but has no link to canonical docs/TODO
6. **Classify audit outcome**
   - `none`: no meaningful verification debt remains
   - `low`: minor debt, explicitly accepted with low maintenance risk
   - `medium`: debt is present and should be scheduled/tracked explicitly
   - `high`: closure should be blocked until debt is reduced
7. **Issue cards for material debt**
   - For each material finding record:
     - `Issue ID`
     - severity
     - evidence (`file:line`, TODO section, command/log)
     - why it matters
     - fix options `A/B/C`
     - recommended option

## Recommended Search Heuristics
- TODO/waiver scan:
  - `rg -n "waiver|not run|not needed|n/a|TODO|FIXME|HACK|TBD|blocked|provisional" foundation_documentation/todos/active foundation_documentation/todos/completed`
- Inline code debt:
  - `rg -n "\\b(TODO|FIXME|HACK|TBD|XXX)\\b" <touched-paths...>`

## Required Outputs
- Audit outcome: `none|low|medium|high`
- Short rationale for the outcome
- Inline code TODO debt classification: `none|accepted|cleanup-required`
- Evidence or artifact path for the audit
- Accepted residual debt, if any

## Done Criteria
- Closure is not declared clean while material evidence/promotion/waiver debt remains hidden.
- Inline code TODO debt is either cleaned up or explicitly classified and justified.
- Durable knowledge is promoted into canonical docs instead of staying trapped in tactical artifacts.
- Any remaining verification debt is explicit enough to survive future sessions without rediscovery.

```

## delphi-ai/skills/review-finding-classification/SKILL.md

```
---
name: review-finding-classification
description: "Canonical post-review triage for internal no-context, CI, remote-check, and promotion findings using the repo taxonomy and Promotion Finding Routing Ledger."
---

# Review Finding Classification

Use this skill after findings have already been collected and deduplicated from:
- Copilot real
- Copilot mimic / `copilot-pr-review`
- internal no-context audits
- CI checks
- promotion preflight or promotion PR reviews

This skill does **not** change how reviewers detect issues. It only governs the post-detection triage and ledger routing.

## Canonical Sources

Read these before classifying:
- `foundation_documentation/todos/README.md` section `Review Finding Classification`
- `foundation_documentation/project_constitution.md` review/promotion classification bullets
- the governing TODO, especially:
  - approved objective
  - decisions / non-goals
  - validation matrix
  - `Promotion Finding Routing Ledger`

If prior findings already exist, also derive carry-forward context:

```bash
python3 delphi-ai/tools/finding_carry_forward_extract.py --todo <todo-path>
```

## Classification Contract

1. Freeze the exact finding first.
   - reviewer surface
   - exact text / locus
   - current evidence
   - whether the current bounded package actually changed that locus/behavior
2. Cross-check the finding against the governing TODO.
   - approved objective
   - explicit decisions
   - accepted by-design behavior
   - non-goals
   - validation/evidence expectations
3. Classify the finding as exactly one of:
   - `release-blocker`
     - real defect/risk for the current delivery or promotion claim
     - must be fixed, explicitly challenged as by-design, or re-approved before the lane is clean
   - `follow-up-fast-follow`
     - real issue, but not a blocker for the current release/package
     - requires an explicit TODO under the project-approved active classification/version topology
   - `follow-up-hardening`
     - real issue, but not a blocker for the current release/package
     - requires an explicit TODO under the project-approved active classification/version topology
   - `by-design/no-action`
     - expected behavior, reviewer noise, or already-approved intent
     - requires rationale tied back to approved scope/decision/evidence
4. Record every classified finding in the governing TODO `Promotion Finding Routing Ledger`.
   - repeated findings stay historical/noise unless the current bounded package materially changed the same locus/behavior or the prior rationale is objectively insufficient
   - only `release-blocker` rows block the current delivery/promotion claim
   - non-blocking real findings are not disposable; split or cite the explicit follow-up owner before calling the lane clean
   - when the project uses both classification families and version packages, classification chooses the family root while package authority decides whether the follow-up joins an immediate version wave or remains outside the current package

## Deterministic Support

Use the narrow helper only for ledger scaffolding, never for blocker authority:

```bash
python3 delphi-ai/tools/review_finding_routing_scaffold.py --input <findings.json> --section
```

The helper renders guard-compatible `Promotion Finding Routing Ledger` rows/sections from operator-supplied metadata. It does **not** decide the classification for you.

## Expected Ledger Shape

The current enforced ledger columns are:
- `Finding ID`
- `Severity`
- `Classification`
- `Routing Decision`
- `Same TODO / Split Rationale`
- `Status`
- `Approval / Follow-up Reference`

Keep rows concrete and non-placeholder before any delivery or promotion-clean claim.

## Non-Negotiables

- Do not weaken reviewer prompts or heuristics just to reduce findings.
- Do not reopen work solely because a reviewer repeated an already adjudicated finding on an unchanged locus/behavior.
- Do not leave real non-blocking findings as vague notes.
- Do not let the helper script become a second policy source.
- Do not let Copilot/Codex/CI comments outrank an approved TODO decision without explicit re-check against the governing TODO.

```

## delphi-ai/rules/stacks/nestjs/nestjs-architecture-always-on.md

```
---
trigger: always_on
description: Preserve explicit NestJS module, boundary, validation, configuration, and testing contracts without activating unrelated capabilities.
---

## Rule

Apply these rules whenever the project activates the `nestjs` capability:

- Organize application behavior around explicit domain or use-case modules. Treat a module's exported providers as its public interface; do not export internal providers merely to bypass a boundary.
- Keep transport adapters thin. Controllers, resolvers, gateways, message handlers, and scheduled entrypoints validate/map inputs, invoke application behavior, and map results; they do not become the authoritative home of business rules.
- Use dependency injection through explicit provider tokens/contracts at infrastructure boundaries. Do not couple application behavior directly to a specific ORM, database, queue, HTTP adapter, deployment platform, or frontend unless that capability is also project-declared.
- Make provider lifetime deliberate. Singleton is the ordinary NestJS scope; request/transient scope requires a documented need and validation proportional to its runtime cost and state semantics.
- Validate every externally controlled boundary using runtime-capable schemas, pipes, parsers, or equivalent project-declared mechanisms. TypeScript types alone are not runtime validation. Unknown-field, coercion, defaulting, and rejection behavior must be explicit.
- Validate required configuration during bootstrap and fail before serving work when required values are missing or invalid. Record variable names and semantics, never secret values.
- Keep authentication and authorization transport-aware and explicit through the project's guards/policies/contracts. NestJS activation does not imply HTTP, JWT, RBAC, tenancy, or any particular identity provider.
- Map domain failures to stable boundary errors without leaking stack traces, credentials, database details, or framework internals.
- Keep persistence and external integrations behind owned adapters. NestJS does not imply Prisma, PostgreSQL, Docker, Railway, React, or Vite.
- Test changed behavior at the narrowest faithful layer: provider/use-case tests for business decisions, module integration tests for wiring and adapters, and application-level tests for externally visible contracts. Use the project-declared runner; NestJS does not mandate Jest or Vitest.
- Use the project-declared package manager, lockfile, scripts, Node version, module system, and build/start contract. Never invent universal commands from Delphi examples.

## Rationale

Nest modules encapsulate providers by default and expose dependencies through explicit exports. Preserving that boundary keeps domain behavior testable and prevents framework, transport, persistence, or deployment choices from silently coupling otherwise independent capabilities.

## Enforcement

- Run `python3 delphi-ai/tools/node_capability_surface_audit.py --repo <repo-root> --expect nestjs` before relying on a detected NestJS surface.
- Add `--require-script <script-name>` for each package script required by the project-owned validation contract. When multiple manifests match, select the owning package explicitly with `--manifest <relative/package.json>`; never aggregate scripts across packages.
- Review module exports, provider scopes, runtime validation, bootstrap configuration, authorization boundaries, and test evidence for every changed entrypoint.

## Notes

Follow `delphi-ai/workflows/nestjs/change-application-boundary-method.md` when adding or changing a controller, resolver, gateway, consumer, command, scheduled entrypoint, or module-owned public contract.

```

## delphi-ai/rules/stacks/react/react-architecture-always-on.md

```
---
trigger: always_on
description: Preserve explicit React component, state, effect, accessibility, and testing boundaries without activating a build tool, backend, or deployment platform.
---

## Rule

Apply these rules whenever the project activates the `react` capability:

- Keep components and hooks pure during render. Do not mutate props, state, hook arguments, module globals, or external systems while rendering.
- Model each piece of state with one intentional owner. Avoid contradictory, redundant, duplicated, or unnecessarily deep state; derive renderable values from existing inputs instead of synchronizing duplicate state.
- Use effects only to synchronize with systems outside React. Put user-triggered work in event handlers and compute render-only transformations during render. Include every reactive dependency; refactor the effect or surrounding code instead of suppressing dependency lint.
- Follow the Rules of Hooks and the project's version/lint contract. Call ordinary hooks only at the top level of React components or custom hooks; apply the documented conditional/loop exception for the `use` API only when the project's React version supports it, while preserving its remaining restrictions.
- Separate UI rendering, interaction/application behavior, and external data adapters at boundaries proportionate to the feature. Do not hide domain rules or transport details inside reusable visual components.
- Represent loading, empty, success, validation, authorization, and failure states explicitly when the user flow can reach them. Prevent stale responses and duplicate actions where asynchronous work can race.
- Preserve semantic HTML, keyboard operation, focus behavior, accessible names, and error/status announcements for affected interactions.
- Keep server data, URL/navigation state, form state, and ephemeral presentation state distinct unless the project contract deliberately unifies them.
- Use stable identity for list keys and state preservation. Index keys are acceptable only when ordering and identity cannot change in a way that affects behavior.
- Test observable component and user behavior with the project-declared runner and rendering/browser tools. React does not imply Vitest, Jest, Testing Library, Playwright, Vite, a router, or a state library.
- Use the project-declared package manager, owning manifest, scripts, TypeScript/JavaScript mode, rendering target, and build/runtime contract. Never infer Vite, a browser-only target, server rendering, or a backend from React alone.

## Enforcement

- Run `python3 delphi-ai/tools/node_capability_surface_audit.py --repo <repo-root> --expect react` before relying on detected React evidence.
- Add `--require-script <script-name>` for project-required checks and select the owning package with `--manifest <relative/package.json>` when more than one manifest matches.
- Review state ownership, render purity, effects, asynchronous races, accessibility, stable identity, and observable test evidence for each changed UI boundary.

## Notes

Follow `delphi-ai/workflows/react/change-ui-boundary-method.md` when adding or changing a component, hook, context/provider, form, route-facing view, or interactive state boundary.

```

## delphi-ai/workflows/docker/performance-concurrency-validation-method.md

```
---
description: Define the versioned four-lane performance/concurrency policy package for tactical TODOs, including closed registries, lane state machine, artifact hashing rules, and gate deadlines.
---

# Method: Performance & Concurrency Validation Lanes

## Policy Schema Version
- `pcv-1`

This workflow is the canonical policy package for tactical TODO performance/concurrency validation. The closed registries, JSON normalization rules, and lane artifact contracts in this document are immutable within `pcv-1`.

## Scope Anchor
- This policy applies only to tactical TODOs under `foundation_documentation/todos/active/` that use the tactical TODO template and require explicit `APROVADO` before implementation.
- `Approval authority` means the explicit approving user or an explicitly delegated human approver recorded by the user.
- `Executor` means the agent performing the work.
- `Approver` must differ from `executor`.

## Lane Set
Every tactical TODO must contain exactly four lane rows:
- `EPS` = `endpoint-performance-scrutiny`
- `FRC` = `frontend-race-condition-validation`
- `BCI` = `backend-concurrency-idempotency-validation`
- `RLS` = `runtime-load-stress-validation`

No lane row may be missing or duplicated.

## Closed Registries

### Lane IDs
| ID | Meaning |
| --- | --- |
| `EPS` | Endpoint/query access-path scrutiny |
| `FRC` | Frontend race-condition validation |
| `BCI` | Backend concurrency/idempotency validation |
| `RLS` | Runtime load/stress validation |

### Trigger Results
| ID | Meaning |
| --- | --- |
| `required` | The lane must be resolved by its gate deadline. |
| `recommended` | The lane must still be resolved by its gate deadline, but waiver governance is lighter. |
| `not_needed` | The validated surface is absent for this TODO. |

### Gate Deadlines
| ID | Meaning |
| --- | --- |
| `before_local_implemented` | The lane must be gate-satisfying before the TODO may move to `Current delivery stage = Local-Implemented`. |
| `before_production_ready` | The lane must be gate-satisfying before the TODO may move to `Current delivery stage = Production-Ready`. |

### Lane States
| ID | Meaning |
| --- | --- |
| `not_applicable` | Valid only when `trigger_result = not_needed`; terminal. |
| `pending` | Triggered lane not yet started. |
| `running` | Validation execution in progress. |
| `blocked` | Validation cannot currently run due to a concrete blocker. |
| `passed` | Minimum evidence and acceptance rule satisfied. |
| `waived` | Explicitly accepted exception path with governance fields completed. |
| `expired` | Waiver expired; lane no longer satisfies gate. |
| `missed_gate` | The lane missed its deadline while unresolved. |

### Uncertainty Reason Codes
| Code | Meaning |
| --- | --- |
| `none` | No uncertainty claimed. |
| `U-QUERY-PATH-UNKNOWN` | Query/data-access path could not be classified with confidence. |
| `U-ASYNC-SURFACE-UNKNOWN` | Async UI overlap/lifecycle behavior could not be classified with confidence. |
| `U-WRITE-OVERLAP-UNKNOWN` | Write overlap or idempotency exposure is uncertain. |
| `U-RUNTIME-PRESSURE-UNKNOWN` | Runtime pressure/capacity impact is uncertain. |
| `U-EVIDENCE-EQUIVALENCE-CLAIM` | A non-default stronger evidence profile is being used instead of the floor profile. |

If `uncertainty_reason_code != none`, `trigger_result` cannot be `not_needed`.

## Objective Trigger Glossary
- `exact_lookup_surface_changed`
  - Changed code creates/modifies/deletes a path retrieving exactly one entity by key (`slug|id|uuid|code|handle|key`) or changes its API/repository contract.
- `query_shape_changed`
  - Changed code creates/modifies/deletes filtering, sorting, pagination, grouping, aggregation, join behavior, index expectation, cardinality, number of backend calls, or direct-lookup-vs-list-traversal behavior.
- `retriggerable_async_write`
  - The changed UI surface can issue overlapping mutations from the same visible action path.
- `retriggerable_async_read_with_order_dependence`
  - Overlapping reads can update the same visible state and later responses can overwrite newer intent.
- `lifecycle_async_effect`
  - Navigation/dispose/unmount can occur while async work still targets visible UI state or visible side effects.
- `overlapping_write_surface`
  - The changed system allows two or more requests/jobs/webhooks to mutate the same logical resource concurrently.
- `runtime_pressure_surface`
  - The changed code touches queue/worker/realtime fan-out, batch/bulk path, cache/index-sensitive request path, or the TODO explicitly claims latency/throughput/capacity/SLO impact.

## Severity Scale
| ID | Meaning |
| --- | --- |
| `low` | Localized, reversible, non-core flow. |
| `medium` | User-visible or business-relevant degradation/corruption risk. |
| `high` | Payment, reservation, inventory, auth-critical, realtime core path, or TODO runtime impact explicitly classified high. |

## Row Schema

### Always-Required Row Fields
- `policy_schema_version`
- `lane_id`
- `trigger_result`
- `trigger_severity`
- `trigger_reason_code`
- `trigger_rationale`
- `gate_deadline`
- `min_evidence_rule_id`
- `state`
- `residual_risk`
- `uncertainty_reason_code`
- `recorded_at_utc`
- `executor_id`

### Conditional Objects
- `evidence`
  - Required only when `state in {running, passed}`.
- `blocker`
  - Required only when `state = blocked`.
- `waiver`
  - Required only when `state in {waived, expired}`.
- `classification_change`
  - Required only when `trigger_result` changed after `APROVADO`.

## Gate-Satisfying States
- For `required`: only `passed` or `waived`
- For `recommended`: only `passed` or `waived`
- For `not_needed`: only `not_applicable`
- `blocked`, `pending`, `running`, `expired`, and `missed_gate` never satisfy a gate.

## State Machine
- Initial state:
  - `not_applicable` only when `trigger_result = not_needed`
  - `pending` when `trigger_result in {required, recommended}`
- Allowed transitions:
  - `pending -> running|blocked|waived|missed_gate`
  - `running -> passed|blocked|waived|missed_gate`
  - `blocked -> running|waived|missed_gate`
  - `waived -> expired`
  - `expired -> pending`
  - `missed_gate -> running|waived`
  - `passed -> terminal`
  - `not_applicable -> terminal`
- No row may transition to `not_applicable` after `APROVADO`.

## Classification Control
- After `APROVADO`, `trigger_result` may only change `required <-> recommended`.
- Any change that reduces obligation (`required -> recommended`) requires renewed `APROVADO`.
- `recommended -> required` requires a recorded change, but not renewed approval unless the user explicitly constrains the prior lighter path.
- `required -> not_needed` and `recommended -> not_needed` are forbidden after `APROVADO`.
- `classification_change` object fields:
  - `previous_trigger_result`
  - `new_trigger_result`
  - `classification_changed_by`
  - `classification_changed_at_utc`
  - `classification_change_reason`
  - `approval_reference`

## Waiver Control
- Any gate-satisfying waiver requires:
  - `waiver_reason_code`
  - `waiver_reason`
  - `waiver_expiry_utc`
  - `approver_id`
  - `approval_reference`
  - `follow_up_task_id`
  - `follow_up_owner`
  - `mitigation_summary`
- `approver_id` must differ from `executor_id`.
- Required-lane waiver additionally requires `reviewer_id`, and `reviewer_id` must differ from both `executor_id` and `approver_id`.
- Expired waiver automatically reopens the lane as `pending`.

## Blocker Control
- `blocker` object fields:
  - `blocker_reason_code`
  - `blocker_reason`
  - `unblock_condition`
  - `follow_up_task_id`
  - `follow_up_owner`
- If a gate deadline is reached while the lane is still `pending|running|blocked`, the state must become `missed_gate`.

## Evidence Control
- Prose-only evidence is invalid.
- Each `evidence` object must include:
  - `evidence_type`
  - `environment_id`
  - `run_id`
  - `artifact_uri`
  - `artifact_schema_version`
  - `artifact_sha256`
  - `sample_profile_id`
  - `acceptance_rule_id`
  - `result_summary`
  - `reviewer_id`
- The artifact at `artifact_uri` must be a machine-checkable JSON document.
- The artifact JSON must include:
  - `policy_schema_version`
  - `schema_version`
  - `lane_id`
  - `todo_id`
  - `run_id`
  - `environment_id`
  - `executor_id`
  - `reviewer_id`
  - `recorded_at_utc`
  - `evidence_type`
  - `sample_profile_id`
  - `acceptance_rule_id`
  - `result_summary`
  - `artifact_payload`
  - `artifact_sha256`
- `artifact_sha256` must be the `SHA-256` hash of the full canonical JSON serialization excluding the `artifact_sha256` field itself.
- Canonical JSON normalization for hashing in `pcv-1`:
  - UTF-8 encoding
  - sorted object keys at every depth
  - arrays preserved in declared order
  - no insignificant whitespace
  - no comments or trailing commas
- If one artifact is reused by multiple lanes, each lane row must reference it explicitly, and the artifact payload must satisfy every referenced lane's required evidence fields and rules.

## Lane Policies

### EPS
**Trigger Reason Codes**
- `EPS-EXACT-LOOKUP-SURFACE-CHANGED`
- `EPS-QUERY-SHAPE-CHANGED`
- `EPS-LIST-SEARCH-SEMANTICS-CHANGED`
- `EPS-DATA-PATH-CHANGED`

**Classification**
- `required` when `exact_lookup_surface_changed` or `query_shape_changed` is true
- `recommended` when a read path changed but neither `exact_lookup_surface_changed` nor `query_shape_changed` is true
- `not_needed` when no read/data-access/query surface changed

**Gate Deadline**
- `before_local_implemented`

**Closed Evidence Rules**
| Rule ID | Required Evidence |
| --- | --- |
| `EPS-E1` | Access-pattern classification + touched-path audit artifact |
| `EPS-E2` | `EPS-E1` plus `explain|query-log|benchmark-equivalent` artifact |

**Closed Acceptance Rules**
| Rule ID | Pass Requirement |
| --- | --- |
| `EPS-A1` | Low-severity row satisfies `EPS-E1`. |
| `EPS-A2` | Medium/high-severity row satisfies `EPS-E2`. |

**Closed Sample Profiles**
| ID | Meaning |
| --- | --- |
| `EPS-SP-AUDIT` | Touched-path audit profile |
| `EPS-SP-STRONG` | Strong query evidence profile |

### FRC
**Trigger Reason Codes**
- `FRC-DUPLICATE-MUTATION`
- `FRC-STALE-RESPONSE`
- `FRC-LIFECYCLE-ASYNC-EFFECT`
- `FRC-RETRIGGERABLE-LIST`
- `FRC-OPTIMISTIC-RECONCILE`

**Classification**
- `required` when `retriggerable_async_write`, `retriggerable_async_read_with_order_dependence`, or `lifecycle_async_effect` is true on the changed UI surface
- `recommended` when only low-risk retriggerable async read behavior changed and no mutation/lifecycle risk applies
- `not_needed` when no retriggerable/lifecycle-sensitive async UI surface changed

**Gate Deadline**
- `before_local_implemented`

**Closed Evidence Rules**
| Rule ID | Required Evidence |
| --- | --- |
| `FRC-POLICY` | `concurrency_policy` enum present in artifact payload |
| `FRC-E1` | `FRC-POLICY` + low floor profile evidence |
| `FRC-E2` | `FRC-POLICY` + medium floor profile evidence |
| `FRC-E3` | `FRC-POLICY` + high floor profile evidence |

**Closed Acceptance Rules**
| Rule ID | Pass Requirement |
| --- | --- |
| `FRC-A1` | Required lane row cannot pass without concurrency policy plus deterministic runner/manual evidence artifact. |
| `FRC-A2` | Alternate stronger profile allowed only with `U-EVIDENCE-EQUIVALENCE-CLAIM` and explicit rationale. |

**Closed Sample Profiles**
| ID | Meaning |
| --- | --- |
| `FRC-SP-L` | `5` repeated triggers x `2` repetitions |
| `FRC-SP-M` | `10` repeated triggers x `3` repetitions |
| `FRC-SP-H` | `20` repeated triggers x `5` repetitions |

### BCI
**Trigger Reason Codes**
- `BCI-NON-IDEMPOTENT-WRITE`
- `BCI-IRREVERSIBLE-SIDE-EFFECT`
- `BCI-LOST-UPDATE-RISK`
- `BCI-DUPLICATE-SUBMIT-OR-REPLAY`
- `BCI-JOB-WEBHOOK-API-OVERLAP`
- `BCI-EXACT-ONCE-SEMANTICS`

**Classification**
- `required` when `overlapping_write_surface` is true and a closed `BCI` reason code applies
- `recommended` when `overlapping_write_surface` may exist but changed code only strengthens protections without altering write semantics
- `not_needed` when no write surface changed and no overlapping mutation surface exists

**Gate Deadline**
- `before_local_implemented`

**Closed Evidence Rules**
| Rule ID | Required Evidence |
| --- | --- |
| `BCI-INV` | `invariant_id` present in artifact payload |
| `BCI-POLICY` | `concurrency_policy` enum present in artifact payload |
| `BCI-E1` | `BCI-INV` + `BCI-POLICY` + low floor profile evidence |
| `BCI-E2` | `BCI-INV` + `BCI-POLICY` + medium floor profile evidence |
| `BCI-E3` | `BCI-INV` + `BCI-POLICY` + high floor profile evidence |

**Closed Acceptance Rules**
| Rule ID | Pass Requirement |
| --- | --- |
| `BCI-A1` | Required row cannot pass without invariant and deterministic overlapping-operation probe artifact. |
| `BCI-A2` | Alternate stronger profile allowed only with `U-EVIDENCE-EQUIVALENCE-CLAIM` and explicit rationale. |

**Closed Sample Profiles**
| ID | Meaning |
| --- | --- |
| `BCI-SP-L` | `5` overlapping operations x `2` batches |
| `BCI-SP-M` | `10` overlapping operations x `3` batches |
| `BCI-SP-H` | `20` overlapping operations x `5` batches |

### RLS
**Trigger Reason Codes**
- `RLS-SLO-CLAIM`
- `RLS-QUEUE-WORKER-REALTIME-CHANGED`
- `RLS-BATCH-OR-BULK-PATH-CHANGED`
- `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED`

**Classification**
- `required` when `runtime_pressure_surface` is true and either the TODO includes explicit latency/throughput/capacity/SLO acceptance or TODO runtime impact is classified `high`
- `recommended` when `runtime_pressure_surface` is true but no explicit performance commitment exists and runtime impact is `low|medium`
- `not_needed` when no runtime-pressure surface changed

**Gate Deadline**
- `before_production_ready` by default
- `before_local_implemented` only when the TODO `Definition of Done` explicitly includes runtime capacity/performance acceptance

**Closed Evidence Rules**
| Rule ID | Required Evidence |
| --- | --- |
| `RLS-E1` | One stage profile + thresholds + metrics artifact |
| `RLS-E2` | Two stage profiles + thresholds + metrics artifact |
| `RLS-E3` | Three stage profiles + thresholds + metrics artifact |

**Closed Acceptance Rules**
| Rule ID | Pass Requirement |
| --- | --- |
| `RLS-A1` | Required row cannot pass without thresholds, stage profile, and metrics comparison artifact. |

**Closed Sample Profiles**
| ID | Meaning |
| --- | --- |
| `RLS-SP-L` | One stage load profile |
| `RLS-SP-M` | Two stage load profile |
| `RLS-SP-H` | Three stage load profile |

## Required Artifact Payload Fields By Lane
- `EPS`
  - `access_pattern_classification`
  - `touched_path_audit_summary`
  - For `EPS-E2`, `strong_query_evidence_type`
- `FRC`
  - `concurrency_policy`
  - `burst_profile_observed`
  - `runner_or_manual_path`
- `BCI`
  - `invariant_id`
  - `concurrency_policy`
  - `probe_profile_observed`
- `RLS`
  - `stage_profile_observed`
  - `thresholds`
  - `metrics_summary`

## Representation In Tactical TODOs
- Tactical TODOs may represent the always-required row fields in a matrix and place conditional objects under per-lane subsections, as long as all required fields from this workflow remain present and unambiguous.
- The tactical TODO template provides the canonical markdown representation for `pcv-1`.

## Known v1 Limits
- `required -> recommended` renewal language remains slightly asymmetric and may be tightened in a future schema version.
- Some classification heuristics still depend on human judgment; this is acceptable for `pcv-1` because the policy now constrains the exploitable parts (state, waiver, evidence, and deadline behavior).

```

## delphi-ai/schemas/subagent_review_result.schema.json

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://paced.internal/schemas/subagent_review_result.schema.json",
  "title": "PACED Subagent Review Result",
  "type": "object",
  "required": [
    "schema_version",
    "artifact_kind",
    "dispatch_path",
    "review_kind",
    "reviewer_label",
    "overall_assessment",
    "recommended_path",
    "performance_position",
    "elegance_position",
    "structural_soundness_position",
    "operational_fit_position",
    "findings"
  ],
  "properties": {
    "schema_version": {
      "const": "subagent-review-result-v1"
    },
    "artifact_kind": {
      "const": "subagent_review_result"
    },
    "dispatch_path": {
      "type": "string",
      "minLength": 1
    },
    "review_kind": {
      "enum": [
        "architecture_opinion",
        "architecture_adherence",
        "critique",
        "test_quality_audit",
        "final_review",
        "cutover_integrity_audit"
      ]
    },
    "reviewer_label": {
      "type": "string",
      "minLength": 1
    },
    "overall_assessment": {
      "type": "string",
      "minLength": 1
    },
    "recommended_path": {
      "type": "string",
      "minLength": 1
    },
    "performance_position": {
      "$ref": "#/$defs/position"
    },
    "elegance_position": {
      "$ref": "#/$defs/position"
    },
    "structural_soundness_position": {
      "$ref": "#/$defs/position"
    },
    "operational_fit_position": {
      "$ref": "#/$defs/position"
    },
    "findings": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/finding"
      }
    }
  },
  "additionalProperties": false,
  "$defs": {
    "position": {
      "enum": [
        "strong_positive",
        "acceptable",
        "mixed",
        "regresses",
        "unknown",
        "not_evaluated"
      ]
    },
    "finding": {
      "type": "object",
      "required": [
        "severity",
        "title",
        "rationale",
        "suggested_action"
      ],
      "properties": {
        "finding_id": {
          "type": "string",
          "minLength": 1
        },
        "severity": {
          "enum": [
            "low",
            "medium",
            "high"
          ]
        },
        "title": {
          "type": "string",
          "minLength": 1
        },
        "rationale": {
          "type": "string",
          "minLength": 1
        },
        "category": {
          "enum": [
            "architecture",
            "adherence",
            "tests",
            "performance",
            "security",
            "elegance",
            "structural_soundness",
            "operational_fit",
            "residual_risk",
            "other"
          ]
        },
        "formalizable_hint": {
          "enum": [
            "yes",
            "partial",
            "no",
            "unknown"
          ]
        },
        "candidate_rule_level": {
          "enum": [
            "paced",
            "project",
            "none",
            "unknown"
          ]
        },
        "candidate_rule_id": {
          "type": "string"
        },
        "affected_paths": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "suggested_action": {
          "type": "string",
          "minLength": 1
        }
      },
      "additionalProperties": false
    }
  }
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-eps.json

```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "EPS",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "explain-exact-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-native",
  "recorded_at_utc": "2026-10-15T03:36:56Z",
  "evidence_type": "explain",
  "sample_profile_id": "EPS-SP-STRONG",
  "acceptance_rule_id": "EPS-A2",
  "result_summary": "Measured recent/deep/tied pages on20382 rows,1000 ties; existing index retained after candidate trial. Independent judgment pending.",
  "artifact_payload": {
    "access_pattern_classification": {
      "authorization": "exact conversation/grant lookup before query validation",
      "anchor": "scoped message id lookup",
      "page": "conversation_id + strict lexicographic before + DESC(created_at,id) + LIMIT51",
      "response": "ascending order,50 messages max"
    },
    "touched_path_audit_summary": "BFF resolver/parser/service and active-conversation UI consumer; no public API/Consultar changes.",
    "strong_query_evidence_type": "explain",
    "fixture": {
      "conversation_rows": 20382,
      "maximum_timestamp_tie": 1000,
      "deep_anchor_offset_for_selection_only": 10000
    },
    "measurements": [
      {
        "scenario": "recent",
        "execution_ms": 1.094,
        "rows_returned": 51,
        "index_rows": 1001,
        "shared_hit_buffers": 37,
        "sort": "incremental/top-N"
      },
      {
        "scenario": "deep",
        "execution_ms": 3.442,
        "rows_returned": 51,
        "index_rows_surviving": 1000,
        "rows_removed_by_filter": 10001,
        "shared_hit_buffers": 357,
        "sort": "incremental/top-N"
      },
      {
        "scenario": "tie",
        "execution_ms": 0.85,
        "rows_returned": 51,
        "index_rows_surviving": 500,
        "rows_removed_by_filter": 501,
        "shared_hit_buffers": 37,
        "sort": "incremental/top-N"
      }
    ],
    "candidate_index": {
      "columns": [
        "conversation_id",
        "created_at DESC",
        "id DESC"
      ],
      "deep_execution_ms": 3.942,
      "deep_shared_hit_buffers": 9832,
      "rows_removed_by_filter": 10001,
      "decision": "not retained; same OR predicate still filters depth, heap access larger than existing index; no measured need for production migration"
    },
    "residual_risk": "Deep OR keyset still filters newer rows; timings are local warm data, not a production capacity or SLO claim.",
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-timeline-exact.sql",
        "sha256": "30b7477601cd109ffd3af7d38e9df1e5fbf8a6af56bf90cf52a42f4779ee0cb8"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-timeline-exact.log",
        "sha256": "6e346b5b0609de7f347481fb2b4eccc93e4ddf8b41219bb1348fbf169af9b9b6"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-index-trial.sql",
        "sha256": "8ac4343ac0633b5b1535e171ec7466e58c5c6488d1de8abc516b15f6e6b914a3"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-index-trial.log",
        "sha256": "43251847c09a71819a11aa135c8710b72a3eb4af2188f07bd3c071bfa980171c"
      }
    ]
  },
  "artifact_sha256": "f20722cdaae0a7cddea80dbcb2df929035d742f47b49ab7f64a17444a9a79c83"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-frc.json

```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "FRC",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "frc-strong-final-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-chromium-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-native",
  "recorded_at_utc": "2026-10-15T03:42:20Z",
  "evidence_type": "source-owned-playwright-real-backend-races",
  "sample_profile_id": "FRC-SP-M",
  "acceptance_rule_id": "FRC-A1",
  "result_summary": "10 real repeated incoming pushes×3 independent browser repetitions passed; original T survives H>T and dirty late-ID insertion. Full31/31 and poll-resume regression pass on identical final source/build. Independent judgment pending.",
  "artifact_payload": {
    "concurrency_policy": "serialize",
    "policy_by_action": [
      {
        "action": "recovery",
        "policy": "serialize",
        "guard": "single-flight per generation,coalesce dirty,next pass retains pendingT,max3pagequeries per round"
      },
      {
        "action": "context switch",
        "policy": "cancel previous",
        "guard": "logical cancellation by BU/conversation/generation on responses/errors/draft/scroll"
      },
      {
        "action": "backfill/send",
        "policy": "drop duplicate",
        "guard": "in-flight flags and current-generation draft ref"
      },
      {
        "action": "metadata",
        "policy": "last-write-wins",
        "guard": "version-controlled current response; historical pages never overwrite metadata"
      }
    ],
    "burst_profile_observed": {
      "triggers_per_repetition": 10,
      "repetitions": 3,
      "cases_passed": 3,
      "pushes_asserted_per_repetition": 11,
      "pushes_note": "one real head trigger plus10 repeated real inbound webhooks while traversal blocked; browser waits for11 message frames",
      "full_suite": {
        "cases_passed": 31,
        "duration_seconds": 48.6
      },
      "strong_case_duration_seconds": 22.7
    },
    "runner_or_manual_path": "web-app/e2e/timeline.spec.ts:168; npx playwright test e2e/timeline.spec.ts --grep=\"preserva o piso T\" --repeat-each=3; full suite: npm run test:tela",
    "race_matrix": [
      {
        "surface": "history",
        "case": "251 IDs; prepend same visible anchor offset delta<2px, including arrival while delayed actual response"
      },
      {
        "surface": "recovery",
        "case": "H>T; walkthrough already behind cursor in original T; late lower UUID behind walked range; dirty from10 real pushes; new coalesced pass retains T; full database/UI ID equality and unread11"
      },
      {
        "surface": "reconnect",
        "case": "real network disconnect and burst130 while offline; recover without subsequent message event"
      },
      {
        "surface": "poll",
        "case": "60s clock advancement resumes pending>3page recovery without more events or Continue click,full382 IDs"
      },
      {
        "surface": "send/draft/context",
        "case": "delay actual POST response; persisted author; typed-new draft preserved; switch conversation and BU rejects old response"
      },
      {
        "surface": "metadata",
        "case": "close wins over delayed historical response; no stale status restoration"
      },
      {
        "surface": "states",
        "case": "loading,empty,end,error/retry and grant-loss404; no fabricated BFF payloads"
      }
    ],
    "runtime_freshness": {
      "captured_before_workers": "2026-10-15T03:40:28.312Z",
      "served_equals_dist_sha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8",
      "full_attestation_captured_at": "2026-10-15T03:39:29.661Z",
      "source_manifest_matches_full_suite": true,
      "root_verified_all16_current_source_hashes": true
    },
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-frc-strong-final-3x.log",
        "sha256": "8cd7c693430ccd215c495b438ae4c39d0824dc0487dd11e3cf279bbdda9572f4"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-frc-strong-final-20261015.json",
        "sha256": "926ea3cf6fe140f0b79fea2a235b6a9b8e68352e33bcd1e774dcc1bbb144d723"
      }
    ],
    "residual_risk": "Bounded active-conversation memory grows as user loads history; no cache of other conversations. Backdated imports earlier thanT group and production traffic/provider transport are outside this approved slice."
  },
  "artifact_sha256": "9206858a99052977dfb684109d540a1a9e2dd896a34182aea864b0cb3a8e8233"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-bci.json

```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "BCI",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "bci-ack-barrier-canonical-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-native",
  "recorded_at_utc": "2026-10-15T03:36:56Z",
  "evidence_type": "postgresql-overlap-probe",
  "sample_profile_id": "BCI-SP-M",
  "acceptance_rule_id": "BCI-A1",
  "result_summary": "Three deterministic real PostgreSQL barrier batches retain10 increments after ACK; regression mutation fails10vs0 and exact source restoration passes. Independent judgment pending.",
  "artifact_payload": {
    "invariant_id": "ST-ATT-01-ACK-BEFORE-PAGE-PRESERVES-LATER-INCREMENTS",
    "concurrency_policy": "serialize",
    "probe_profile_observed": {
      "overlapping_operations_per_batch": 10,
      "batches": 3,
      "barrier": "ACCESS EXCLUSIVE on messages; pg_stat_activity proves page SELECT blocked, Conversation updates remain unblocked",
      "records": [
        {
          "prova": "BCI_ACK_COM_SELECT_BLOQUEADO",
          "lote": 1,
          "bloqueioDetectado": true,
          "sondagens": 2,
          "ackAteSelectBloqueadoMs": 83,
          "dezIncrementosMs": 42,
          "unreadEnquantoSelectBloqueado": 10,
          "unreadDepoisDaResposta": 10
        },
        {
          "prova": "BCI_ACK_COM_SELECT_BLOQUEADO",
          "lote": 2,
          "bloqueioDetectado": true,
          "sondagens": 2,
          "ackAteSelectBloqueadoMs": 55,
          "dezIncrementosMs": 24,
          "unreadEnquantoSelectBloqueado": 10,
          "unreadDepoisDaResposta": 10
        },
        {
          "prova": "BCI_ACK_COM_SELECT_BLOQUEADO",
          "lote": 3,
          "bloqueioDetectado": true,
          "sondagens": 2,
          "ackAteSelectBloqueadoMs": 53,
          "dezIncrementosMs": 26,
          "unreadEnquantoSelectBloqueado": 10,
          "unreadDepoisDaResposta": 10
        }
      ]
    },
    "mutation_control": {
      "change": "Move ACK after SELECT (old regression)",
      "observed": "Expected10, received0; failed regression assertion",
      "restoration": "Exact original bytes restored in finally; SHA log retained; canonical targeted1/1 passes; broad API224 passed before byte-identical mutation/restoration",
      "test_first_classification": "test-after with negative control, not retroactive TDD"
    },
    "coverage": "FullAPI224 also covers real incoming overlap, post-boundary IN=>11, auth/query errors without writes, background neutral and close/read overlap.",
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/api-e2e-authority.log",
        "sha256": "b508ca43e5157fea8fbf6951b2bd2b7c2b860ebde3e4c2dca1971094436317db"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-mutation-control.log",
        "sha256": "0c2b211c2078240a09519eeff76f2a32a358135090e32df1bb871c619d4e327d"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-canonical-after-mutation.log",
        "sha256": "90fe5dd92cf6098fc7375258ba7452a29c4d74255d10fafd2efcc4c8b4866b4c"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-source-restored.sha256",
        "sha256": "c9f7e6985e02086dfc2a79cdf10dc4204ec5b61db7bb3b8913a9abee25bc0625"
      }
    ]
  },
  "artifact_sha256": "93eeac265b3c77b17e6fee0cbd20223a56cbe44fe17489052b9b4feeffa37995"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-rls.json

```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "RLS",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "rls-read-stage1-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-native",
  "recorded_at_utc": "2026-10-15T03:39:44Z",
  "evidence_type": "one-stage-authenticated-read-load",
  "sample_profile_id": "RLS-SP-L",
  "acceptance_rule_id": "RLS-A1",
  "result_summary": "30/30 reads,5 concurrent×6; p50 23.36ms,p95 64.26ms,max68.5ms; page50,unread7 unchanged,251 messages unchanged,foreign malformed request404. Review pending, no production SLO claim.",
  "artifact_payload": {
    "stage_profile_observed": {
      "mode": "load",
      "stages": 1,
      "concurrency": 5,
      "batches": 6,
      "requests": 30,
      "dataset_messages": 251,
      "transport": "real authenticated BFF HTTP on disposable test Nest runtime"
    },
    "thresholds": {
      "errors": {
        "expected": 0,
        "actual": 0,
        "passed": true
      },
      "response_rows": {
        "expected": 50,
        "actual": 50,
        "passed": true
      },
      "has_previous": {
        "expected": true,
        "actual": true,
        "passed": true
      },
      "read_neutral": {
        "expected_unread": 7,
        "before": 7,
        "after": 7,
        "passed": true
      },
      "history_unchanged": {
        "before": 251,
        "after": 251,
        "passed": true
      },
      "authorization_first": {
        "expected": 404,
        "actual": 404,
        "passed": true
      },
      "latency": "measured only; no production SLO threshold authorized"
    },
    "metrics_summary": {
      "runId": "rls-read-stage1-20261015",
      "sample": {
        "requests": 30,
        "concurrency": 5,
        "batches": 6,
        "statusCounts": {
          "200": 30,
          "errors": 0
        },
        "p50Ms": 23.36,
        "p95Ms": 64.26,
        "maxMs": 68.5,
        "messagesPerResponse": 50,
        "hasPrevious": true
      },
      "scope": {
        "accessibleConversation": "200 x30",
        "foreignConversationWithMalformedCursor": 404,
        "unreadBefore": 7,
        "unreadAfter": 7,
        "messagesBefore": 251,
        "messagesAfter": 251
      },
      "conclusion": "small disposable one-stage read-neutral sample; no production SLO inferred"
    },
    "scope_probe_parameter": "Actual runner sends limite=invalid; raw output key foreignConversationWithMalformedCursor is an imprecise label for malformed query, not a cursor probe. Dedicated API E2E covers actual malformed/foreign cursors.",
    "threshold_origin": "Fixed stage loops and hard-failing assertions in raw runner before execution; no post-hoc latency acceptance invented.",
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rls-read-sample.log",
        "sha256": "5b68b1b5f450153c7fa6c36c277aa19d5846860f63ef8124a1eaeb32dd3941fc"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rls-read-sample.mjs",
        "sha256": "d59fa9f53ffeb97aec02b32ccf91584868f1e2b1ebcd644278f00881ae3a3321"
      }
    ],
    "residual_risk": "Small warm disposable one-stage sample; no stress, spike, soak, throughput or production capacity certification."
  },
  "artifact_sha256": "b9b05d0bd9127e4347e04685a91379924153c7c3a4f9b7445e8fa5ed9f548b3c"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/scan-triage-api.json

```
{
  "schema_version": "leadshug-rule-spirit-triage-v1",
  "status": "final frozen-source supporting triage, pending independent review",
  "repository": "api-app",
  "raw_observations": 30,
  "deduplicated_locations": 15,
  "allowlist": "none",
  "findings": [
    {
      "location": "test/timeline-fixtures.cjs:64",
      "evidence": "  const response = await fetch(`http://127.0.0.1:${apiPort}/webhooks/meta`, {",
      "scanner_keys": [
        "fdfea179a243ad7f",
        "37bfde4a277e7c3d"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/timeline-fixtures.cjs:75",
      "evidence": "      const query = new URL(req.url, 'http://localhost').searchParams;",
      "scanner_keys": [
        "18168c16c1dedf03",
        "56b00be64ca0e1ee"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/timeline-fixtures.cjs:113",
      "evidence": "server.listen(fixturePort, '127.0.0.1', () => console.log(`timeline fixtures listening on 127.0.0.1:${fixturePort}`));",
      "scanner_keys": [
        "846e6036025e845c",
        "7f3ff2bf85a898ae"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/browser-server.cjs:22",
      "evidence": "  process.env.WEB_ORIGIN = 'http://127.0.0.1:4173';",
      "scanner_keys": [
        "0979048a3d65a061",
        "ebc11589454fe381"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/browser-server.cjs:40",
      "evidence": "  app.enableCors({ origin: ['http://127.0.0.1:4173'], credentials: true });",
      "scanner_keys": [
        "4fbbb42b5cb59875",
        "0917bac08ff24b2c"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:73",
      "evidence": "    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');",
      "scanner_keys": [
        "222e4dc3ac247da7",
        "62cfef2ea2d4aa2b"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:74",
      "evidence": "    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');",
      "scanner_keys": [
        "ec8ad555564a5583",
        "443d317681c98942"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:78",
      "evidence": "    cookieOwner = await login(app, 'dono@alfa.test');",
      "scanner_keys": [
        "58b70f0495d8269d",
        "97671a27f5ffbb15"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:102",
      "evidence": "      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'atendente@alfa.test', 'ATENDENTE');",
      "scanner_keys": [
        "1f221a9d5648bf5e",
        "7d6f9d558588c7ab"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:103",
      "evidence": "      const cookie = await login(app, 'atendente@alfa.test');",
      "scanner_keys": [
        "fdb84b2351f2613d",
        "06c90369c5fa2c4c"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:110",
      "evidence": "      const cookieBeta = await login(app, 'dono@beta.test');",
      "scanner_keys": [
        "2b23b50e8f4a1f3d",
        "8dbcd394cef3e576"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:177",
      "evidence": "      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro@alfa.test', 'ATENDENTE');",
      "scanner_keys": [
        "7c7334b879b47440",
        "1b2227ad2236611a"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:178",
      "evidence": "      const cookieOutro = await login(app, 'outro@alfa.test');",
      "scanner_keys": [
        "7d35f697f2bcba03",
        "4febe17e8bc29011"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:203",
      "evidence": "      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro2@alfa.test', 'ATENDENTE');",
      "scanner_keys": [
        "da6f914e2b0bf405",
        "73a91c5681c0199a"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:204",
      "evidence": "      const cookieOutro = await login(app, 'outro2@alfa.test');",
      "scanner_keys": [
        "8a6ad3385f150106",
        "f435ef941f2b1e00"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    }
  ]
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/scan-triage-web.json

```
{
  "schema_version": "leadshug-rule-spirit-triage-v1",
  "status": "final frozen-source supporting triage, pending independent review",
  "repository": "web-app",
  "raw_observations": 42,
  "deduplicated_locations": 21,
  "allowlist": "none",
  "findings": [
    {
      "location": "e2e/timeline.spec.ts:3",
      "evidence": "const FIXTURES = 'http://127.0.0.1:3101';",
      "scanner_keys": [
        "2c1ee4d9b92a0c18",
        "bc9bc14a55d2591e"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline.spec.ts:5",
      "evidence": "const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`;",
      "scanner_keys": [
        "9e49f12c9c12faf6",
        "c72e0b5f5b133197"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "src/tempoReal.spec.ts:12",
      "evidence": "    expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws'); ",
      "scanner_keys": [
        "2a8f09410b6f9592",
        "edf231b3eac47db3"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "src/tempoReal.spec.ts:32",
      "evidence": "    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() }); ",
      "scanner_keys": [
        "11de67ec67e28377",
        "3ae03706d1c501fb"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "src/tempoReal.spec.ts:58",
      "evidence": "    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout }); ",
      "scanner_keys": [
        "ecd8c6244fc918e1",
        "ac44ff645d061b9b"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "src/api.ts:75",
      "evidence": "    const pareceEstatico = res.status === 405 || /^\\s*<(!doctype|html)/i.test(bruto); ",
      "scanner_keys": [
        "3c3ff59eaca3694e",
        "3ebdb512aa908de7"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Unchanged baseline HTML detector regular expression; not a domain/runtime target. Delta here adds only Thread.paginacao."
    },
    {
      "location": "playwright.config.ts:5",
      "evidence": "const API = `http://127.0.0.1:${PORTA_DA_API}`; ",
      "scanner_keys": [
        "d0ac253aa5ff151c",
        "d8e95984315f8f6b"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:26",
      "evidence": "    baseURL: 'http://127.0.0.1:4173', ",
      "scanner_keys": [
        "2a29ea59c22e2638",
        "61883216dd8dc12f"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:32",
      "evidence": "      url: 'http://127.0.0.1:3101/health', ",
      "scanner_keys": [
        "59d1ac46cac22135",
        "405b3e41f6cda288"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:80",
      "evidence": "        WEB_ORIGIN: 'http://127.0.0.1:4173', ",
      "scanner_keys": [
        "a1e456347a8821fd",
        "8a5b48f8f8c6bee4"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:85",
      "evidence": "      // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`, ",
      "scanner_keys": [
        "4b7be4c40850487c",
        "8994854a4b272f6f"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:88",
      "evidence": "      // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em ",
      "scanner_keys": [
        "5e12863dffbccf69",
        "a06bafeb722161e4"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:91",
      "evidence": "      // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o ",
      "scanner_keys": [
        "2698063e108a0609",
        "1a0d611415fc6996"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:93",
      "evidence": "      command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort', ",
      "scanner_keys": [
        "ac41a31312e558bd",
        "164bf04d7b0bbb19"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:97",
      "evidence": "      url: 'http://127.0.0.1:4173', ",
      "scanner_keys": [
        "70831863fa683675",
        "3c89510b83ba01a9"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:45",
      "evidence": "  const apiEndpoint = `http://127.0.0.1:${apiPort}`;",
      "scanner_keys": [
        "e4d3b43c6a981645",
        "1c70b5070fab5314"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:48",
      "evidence": "    fetch('http://127.0.0.1:3101/health'),",
      "scanner_keys": [
        "02ced4490c6f1ae3",
        "a129a7b950a8f0ec"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:49",
      "evidence": "    fetch('http://127.0.0.1:4173/'),",
      "scanner_keys": [
        "65dcca001d2e41a7",
        "e5308c3cb7d2f03f"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:57",
      "evidence": "  const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173'));",
      "scanner_keys": [
        "69c95e087f673536",
        "75ba7c8469649337"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:60",
      "evidence": "  const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`);",
      "scanner_keys": [
        "350a9bebcb085e01",
        "0ceda0f2bb2a2a57"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:93",
      "evidence": "    endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname }",
      "scanner_keys": [
        "0b3266de3272c907",
        "ea4c693cfacd5dc5"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only localhost/loopback target or reserved .test identity; no operational target or secret; no suppression."
    }
  ]
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/audit-floor.json

```
{
  "schema_version": "audit-escalation-guard-v1",
  "artifact_kind": "audit_escalation_decision",
  "rule_id": "paced.audit-escalation.requirements",
  "outcome": "go",
  "blocked": false,
  "todo_path": "/mnt/c/Unifast/LeadsHug/leadshug_now_docker/foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md",
  "trigger_matrix_fingerprint": "2f62d6657e20",
  "trigger_matrix": {
    "complexity": "medium",
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
      "decision": "not_needed",
      "lifecycle_gate": "before_completed",
      "workflow": "audit-protocol-triple-review",
      "replacement_policy": "additive_only",
      "reason_codes": [
        "DEDICATED-AUDIT-NOT-TRIGGERED"
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

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/api-e2e-authority.log

```

> @leadshug/api@0.1.0 test:e2e
> vitest run --config vitest.config.e2e.ts --no-file-parallelism --maxWorkers=1

[33mThe CJS build of Vite's Node API is deprecated. See https://vite.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.[39m

 RUN  v2.1.9 /workspace/api-app

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":1,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":53,"dezIncrementosMs":26,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":2,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":48,"dezIncrementosMs":21,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":3,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":51,"dezIncrementosMs":24,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

 ✓ test/atendimento.e2e-spec.ts (19 tests) 7720ms
   ✓ atendimento > POST conversations/:id/messages — o trio (ADR-0012 §2) > autorizado: responde, envia pelo canal e assume a conversa 424ms
   ✓ atendimento > POST conversations/:id/messages — o trio (ADR-0012 §2) > ATENDENTE no escopo responde — estar na BU BASTA (ADR-0018 §3) 493ms
   ✓ atendimento > POST conversations/:id/messages — o trio (ADR-0012 §2) > CROSS-TENANT: o dono de Beta recebe 404 na conversa da BU de Alfa 380ms
   ✓ atendimento > janela de 24h — atributo do CANAL (ADR-0009 §3) > no canal NÃO oficial não existe janela: responde mesmo com a conversa velha 308ms
   ✓ atendimento > fila > assumir trava para outro agente (409), e finalizar libera 516ms
   ✓ atendimento > fila > responder NÃO rouba conversa de quem já está atendendo 463ms
   ✓ atendimento > fila > abrir a thread zera as não lidas — abrir É atender 307ms
   ✓ atendimento > fila > a lista filtra por aba e só enxerga a BU pedida 323ms
   ✓ atendimento > a inbox pagina — teto silencioso é o que vira "sumiram conversas" > devolve total e temMais, e a segunda página traz o resto 328ms
   ✓ atendimento > timeline paginada do atendimento > caminha por 251 mensagens na ordem do banco e mantém a página limitada 480ms
   ✓ atendimento > timeline paginada do atendimento > valida parâmetros depois da autorização e rejeita cursor de outra conversa autorizada 381ms
   ✓ atendimento > timeline paginada do atendimento > exige sessão antes de validar query e não altera unread 310ms
   ✓ atendimento > timeline paginada do atendimento > rejeita cursor/limite repetidos e mantém refresh e backfill sem efeito de leitura 364ms
   ✓ atendimento > timeline paginada do atendimento > serializa dez chegadas concorrentes com a fronteira de abertura em três lotes 546ms
   ✓ atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes 509ms
   ✓ atendimento > timeline paginada do atendimento > permite leituras de cursor concorrentes com close sem reescrever status 485ms
 ✓ test/setores.e2e-spec.ts (26 tests) 10430ms
   ✓ setores (ADR-0017) > o Geral nasce com a Mantenedora > a primeira BU já vem num setor — nenhum número fica sem 356ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > autorizado: OWNER cria, renomeia e inativa 345ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > papel insuficiente: ATENDENTE recebe 403 ao criar 462ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > cross-tenant: setor da Mantenedora B responde 404 para o OWNER de A 368ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > o nome é único DENTRO da Mantenedora — duas contas podem ter "Comercial" 407ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > setor COM número não é excluído — só inativado 305ms
   ✓ setores (ADR-0017) > concessão por setor é EXPANSÃO (ADR-0017 §2) > materializa uma linha POR NÚMERO do setor, com proveniência SETOR 433ms
   ✓ setores (ADR-0017) > concessão por setor é EXPANSÃO (ADR-0017 §2) > BU criada DEPOIS, no setor concedido, já nasce com o grant (regra 3) 411ms
   ✓ setores (ADR-0017) > concessão por setor é EXPANSÃO (ADR-0017 §2) > revogar o setor NÃO remove grant direto nem o da Mantenedora 400ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > autorizado: lista quem recebeu o setor, com papel e desde quando 375ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > papel insuficiente: ATENDENTE recebe 403 436ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > cross-tenant: setor da Mantenedora B responde 404 362ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > a lista de pessoas diz DE QUAL ORIGEM veio cada acesso 401ms
   ✓ setores (ADR-0017) > renomear e inativar o número > papel insuficiente: ATENDENTE recebe 403 478ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > quem tinha pelo setor antigo perde; quem tem o novo ganha 513ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > o grant DIRETO sobrevive à mudança de setor 574ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > recusa quando mover deixaria o número sem OWNER 495ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > cross-setor: o atendente do Comercial recebe 404 na conversa do Suporte 566ms
   ✓ setores (ADR-0017) > conceder um setor VAZIO é lembrado — o número criado depois já nasce com o acesso 381ms
   ✓ setores (ADR-0017) > revogar apaga a CONCESSÃO — o próximo número não ressuscita o acesso 393ms
   ✓ setores (ADR-0017) > setor INATIVO não interrompe atendimento — só some do cadastro 329ms
[31m[Nest] 965  - [39m10/15/2026, 3:20:45 AM [31m  ERROR[39m [38;5;3m[Recuperacao] [39m[31mToken de recuperação emitido para dono@alfa.test, mas o e-mail NÃO saiu.[39m
[31m[Nest] 965  - [39m10/15/2026, 3:20:47 AM [31m  ERROR[39m [38;5;3m[Recuperacao] [39m[31mToken de recuperação emitido para dono@alfa.test, mas o e-mail NÃO saiu.[39m
 ✓ test/convites.e2e-spec.ts (18 tests) 4799ms
   ✓ convite e recuperação de senha (ADR-0025) > convite substitui a senha provisória > criar pessoa NÃO aceita mais senha, e envia o convite 341ms
   ✓ convite e recuperação de senha (ADR-0025) > convite substitui a senha provisória > usar o link define a senha e já entra logado 377ms
   ✓ convite e recuperação de senha (ADR-0025) > o token é de uso único > o mesmo link não funciona duas vezes 380ms
   ✓ convite e recuperação de senha (ADR-0025) > o token é de uso único > pedir recuperação DUAS vezes deixa só o último link vivo 370ms
   ✓ convite e recuperação de senha (ADR-0025) > o token é de uso único > definir a senha mata TODOS os pendentes — inclusive o convite antigo 369ms
 ✓ test/webhooks.e2e-spec.ts (15 tests) 3457ms
   ✓ webhooks de entrada > o dado recebido respeita o escopo > CROSS-TENANT: o dono de Beta não enxerga a conversa que entrou na BU de Alfa 303ms
 ✓ test/identidade.e2e-spec.ts (17 tests) 3660ms
   ✓ identidade > login > bloqueia o e-mail na quinta tentativa errada 513ms
   ✓ identidade > troca obrigatória de senha > trava tudo menos /me e a troca, e destrava depois de trocar 461ms
 ✓ test/api-publica.e2e-spec.ts (13 tests) 5082ms
   ✓ API pública v1 > autenticação pela chave > a chave sai em claro UMA vez, e o prefixo é lh_ 374ms
   ✓ API pública v1 > autenticação pela chave > sem chave: 401 NAO_AUTENTICADO 310ms
   ✓ API pública v1 > autenticação pela chave > cookie de sessão NÃO substitui a chave 374ms
   ✓ API pública v1 > autenticação pela chave > chave revogada responde igual a inexistente 384ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > escopo nulo devolve só as BUs DESTA Mantenedora 310ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > CROSS-TENANT: pedir a BU de Beta com a chave de Alfa dá 403 SEM_ACESSO_A_CONTA 364ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > escopo restrito não alcança outra BU da MESMA Mantenedora 421ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > criar chave com escopo apontando para BU de outra Mantenedora é recusado 414ms
   ✓ API pública v1 > contrato > conversations traz janela_aberta e datas em ISO-8601 UTC 349ms
   ✓ API pública v1 > contrato > messages aceita since para sincronização incremental 342ms
   ✓ API pública v1 > contrato > POST messages envia e marca a conversa como atendida por EXTERNO 326ms
   ✓ API pública v1 > contrato > fora da janela, POST messages recusa com JANELA_FECHADA 306ms
   ✓ API pública v1 > limite de taxa (ADR-0010 §7) — fecha o buraco de ritmo do S3 > estoura em 429 LIMITE_DE_TAXA com Retry-After 636ms
 ✓ test/usuarios.e2e-spec.ts (13 tests) 4676ms
   ✓ gestão de usuários > criar — o trio (ADR-0012 §2) > autorizado: cria com papel e escopo, e SEM credencial — quem entra define a senha 359ms
   ✓ gestão de usuários > criar — o trio (ADR-0012 §2) > papel insuficiente: MEMBRO não gerencia pessoas 512ms
   ✓ gestão de usuários > invariantes do modelo > ninguém concede papel maior que o próprio (ADR-0008 §4) 464ms
   ✓ gestão de usuários > invariantes do modelo > ADMIN não mexe em quem é OWNER — papel ≥ o do alvo (ADR-0008 §4) 481ms
   ✓ gestão de usuários > reenvio de acesso > reenviar o acesso derruba a sessão e emite um LINK, não uma senha 396ms
   ✓ gestão de usuários > a lista pagina e filtra > busca por nome ou e-mail 309ms
 ✓ test/historico.e2e-spec.ts (11 tests) 4003ms
   ✓ histórico (Consultar) > o par número → número > a resposta traz os DOIS números do par, não só o contato 423ms
   ✓ histórico (Consultar) > o par número → número > filtra pelo número do contato 336ms
   ✓ histórico (Consultar) > paginação — 20 é o corpo da página, não o tamanho do que existe > devolve as ÚLTIMAS 20 e avisa que há mais 371ms
   ✓ histórico (Consultar) > paginação — 20 é o corpo da página, não o tamanho do que existe > a segunda página traz o resto e fecha 332ms
   ✓ histórico (Consultar) > consultar não é atender > ler o histórico NÃO zera as não lidas 301ms
   ✓ histórico (Consultar) > CSV > usa os mesmos filtros e sai uma linha por mensagem 300ms
   ✓ histórico (Consultar) > permissão — o trio (ADR-0012 §2) > autorizado: ATENDENTE no escopo consulta — o grant é a permissão (ADR-0018) 441ms
   ✓ histórico (Consultar) > permissão — o trio (ADR-0012 §2) > CROSS-TENANT: o dono de Beta recebe 404 no histórico da BU de Alfa 363ms
   ✓ histórico (Consultar) > permissão — o trio (ADR-0012 §2) > CROSS-TENANT: o CSV também é barrado, e não vaza no corpo 352ms
 ✓ test/historico-atividades.e2e-spec.ts (13 tests) 4533ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o CHECK torna o vazamento IRREPRESENTÁVEL (ADR-0020 §1.1) > escopo BU sem bu_id falha NO BANCO, não no serviço 394ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o CHECK torna o vazamento IRREPRESENTÁVEL (ADR-0020 §1.1) > escopo CONTA COM bu_id falha pelo mesmo CHECK 303ms
   ✓ histórico de atividades (ADR-0020 e 0022) > a escrita acontece dentro da transação > criar setor grava EXATAMENTE uma linha, com a frase pronta 314ms
   ✓ histórico de atividades (ADR-0020 e 0022) > a escrita acontece dentro da transação > falhar a transação NÃO deixa linha 319ms
   ✓ histórico de atividades (ADR-0020 e 0022) > a escrita acontece dentro da transação > mover número grava MOVER com de/para preenchidos 325ms
   ✓ histórico de atividades (ADR-0020 e 0022) > leitura — o trio (ADR-0012 §2) > papel insuficiente: ATENDENTE recebe 403 — gravar é do produto, ler é de quem administra 452ms
   ✓ histórico de atividades (ADR-0020 e 0022) > leitura — o trio (ADR-0012 §2) > cross-tenant: o ADMIN de A não vê NENHUMA linha de B 364ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o que NÃO entra > trocar a própria senha não gera linha 420ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o que NÃO entra > listar e filtrar não geram linha — leitura não registra 304ms
 ✓ test/onboarding.e2e-spec.ts (13 tests) 4652ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > antes de concluir, o resto do BFF responde 409 ONBOARDING_PENDENTE 427ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > o /me, a troca de senha e o próprio wizard continuam respondendo 352ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > a troca de senha vem ANTES do wizard — nunca preso entre os dois portões 640ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > ninguém pode ser convidado antes do wizard — o caso deixa de existir 301ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o wizard oferece SÓ o que a instalação tem > o canal oficial NÃO aparece — ele é o piso, não uma escolha 306ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > só o OWNER conclui, e o produto passa a responder 320ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > recusa papel de convite OWNER — seria transferência disfarçada de cadastro 302ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > recusa módulo fora do teto — pedido inválido é ERRO, não preferência ignorada 329ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > recusa módulo que não existe nesta instalação 335ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > grava a conclusão no histórico 335ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > adicionar e remover módulo depois — mesmo serviço, outra porta > ADMIN edita, e a mudança aparece no /me 346ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > adicionar e remover módulo depois — mesmo serviço, outra porta > RECUSA desligar canal que ainda tem número conectado 358ms
 ✓ test/canais.e2e-spec.ts (10 tests) 3738ms
   ✓ canais da BU > POST channels — o trio (ADR-0012 §2) > autorizado: OWNER conecta o canal oficial, e o phone_number_id é capturado na mesma ida 372ms
   ✓ canais da BU > POST channels — o trio (ADR-0012 §2) > papel insuficiente: MEMBRO recebe 403 — a BU é dele, o poder é que não alcança 472ms
   ✓ canais da BU > canal não oficial > cria a instância e devolve o QR, com a janela DESLIGADA 301ms
   ✓ canais da BU > regras do vínculo > a BU aceita um canal de cada tipo, e recusa o segundo do mesmo tipo 311ms
   ✓ canais da BU > regras do vínculo > remover exige ADMIN e libera o tipo para ser conectado de novo 491ms
   ✓ canais da BU > regras do vínculo > listar canais é leitura: VIEWER enxerga 494ms
 ✓ test/cross-tenant.e2e-spec.ts (9 tests) 3039ms
   ✓ escopo entre Mantenedoras > GET /api/bff/business-units/:buId > autorizado: o dono enxerga a BU da própria Mantenedora 342ms
   ✓ escopo entre Mantenedoras > GET /api/bff/business-units > CROSS-TENANT: usuário sem grant nenhum recebe lista VAZIA, nunca "todas" 366ms
   ✓ escopo entre Mantenedoras > o grant do fundador nasce como expansão (ADR-0008 §4, importado já corrigido) > quem tem grant DIRETO não é alcançado pela expansão — e cai para VIEWER na Mantenedora 469ms
 ✓ test/realtime.e2e-spec.ts (7 tests) 5664ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > quem tem grant na BU recebe a mensagem que chegou 317ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > CROSS-TENANT: o dono de Beta NÃO recebe evento da BU de Alfa 1863ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > usuário da MESMA Mantenedora sem grant naquela BU também não recebe 1983ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > o socket some da lista quando o cliente desconecta 589ms
 ✓ test/modulos.e2e-spec.ts (8 tests) 2892ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > o /me devolve o produto já interseccionado > teto ligado + contratado = ligado, e a marca vem junto 452ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > o /me devolve o produto já interseccionado > a Mantenedora NÃO amplia o teto: contratado sem teto continua desligado 345ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > o /me devolve o produto já interseccionado > sem nada contratado, o produto nasce sem módulo e com tema padrão 315ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a migração PRESERVA o módulo de quem já usa o canal — repetível, e é o que sobe em stage 353ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > autorizado: com teto e contrato, conecta o canal não oficial 357ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > módulo fora do teto da instalação: 404 MODULO_DESLIGADO, nunca 403 383ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > teto ligado mas a Mantenedora não contratou: 404 igual 355ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > o canal OFICIAL nunca é barrado por módulo — ele é o PISO do produto 329ms
 ✓ test/arquivos.e2e-spec.ts (8 tests) 2772ms
   ✓ arquivos (ADR-0024) > SEM volume, recusa explicitamente — e o resto do produto funciona 426ms
   ✓ arquivos (ADR-0024) > com volume > guarda com nome de uuid — o nome do cliente NÃO chega ao disco 309ms
   ✓ arquivos (ADR-0024) > com volume > recusa .png que não é PNG por dentro — o tipo vem dos BYTES 333ms
   ✓ arquivos (ADR-0024) > com volume > devolve o arquivo para quem é da mesma Mantenedora 310ms
   ✓ arquivos (ADR-0024) > com volume > cross-tenant: arquivo de A responde 404 para B 507ms
   ✓ arquivos (ADR-0024) > com volume > id que não é uuid não vira caminho 346ms
[31m[Nest] 1517  - [39m10/15/2026, 3:21:59 AM [31m  ERROR[39m [38;5;3m[Rotina] [39m[31m{"nome":"rotina-quebrada","linhas":0,"lotes":0,"pulouPorLock":false,"erro":"estourei de propósito","duracaoMs":2}[39m
 ✓ test/rotinas.e2e-spec.ts (5 tests) 762ms
 ✓ test/surfaces.e2e-spec.ts (9 tests) 198ms
 ✓ test/cobertura-do-catalogo.e2e-spec.ts (4 tests) 294ms
 ✓ test/painel.e2e-spec.ts (4 tests) 1680ms
   ✓ painel > conta o atendimento e avisa do número sem canal 384ms
   ✓ painel > cross-tenant: NENHUM número da Mantenedora B entra na conta de A 311ms
   ✓ painel > o ATENDENTE vê os números, e NÃO vê o extrato de atividades 500ms
   ✓ painel > o ADMIN vê o extrato 318ms
[31m[Nest] 1688  - [39m10/15/2026, 3:22:08 AM [31m  ERROR[39m [38;5;3m[Banco] [39m[31mBANCO ATRÁS DA IMAGEM: "public.tokens_de_acesso" não existe (P2021). Rode `npx prisma migrate deploy` de dentro do serviço.[39m
 ✓ test/banco-atrasado.e2e-spec.ts (2 tests) 500ms
   ✓ banco atrás da imagem > tabela ausente vira 503 DIZENDO a causa, não 500 opaco 312ms

 Test Files  20 passed (20)
      Tests  224 passed (224)
   Start at  03:20:12
   Duration  111.92s (transform 6.83s, setup 184ms, collect 33.04s, tests 74.55s, environment 4ms, prepare 1.29s)


```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/api-runtime-authority.txt

```
v22.23.3

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-frc-strong-final-20261015.json

```
{
  "capturedAtUtc": "2026-10-15T03:40:28.312Z",
  "runId": "frc-strong-final-20261015",
  "branch": {
    "api": {
      "name": "feature/inbox-timeline-pagination",
      "head": "5db3fbe2043428749895fc3ff6441e9457467dd0",
      "diffSha256": "d3d84c015c24348b1dbc885a90d66ff8f88eadf35a75b0a256a38c3f1230708b",
      "sourceManifest": [
        {
          "path": "src/domain/inbox/conversations.service.ts",
          "sha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.spec.ts",
          "sha256": "a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.ts",
          "sha256": "d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af"
        },
        {
          "path": "src/surfaces/bff/conversations.controller.ts",
          "sha256": "0b5c46a78aafd8085b609ad711bcdb7626263094f434240f37b8700f20291565"
        },
        {
          "path": "test/atendimento.e2e-spec.ts",
          "sha256": "1bb4acb19fc522b397424b319ab04563e3608605dcfe307970eecdd0d464b5b8"
        },
        {
          "path": "test/browser-server.cjs",
          "sha256": "031e9d1e282603c098c4bb594fb13a08ab2bc2f301c9a3ebb5a6362cae6fe42b"
        },
        {
          "path": "test/timeline-fixtures.cjs",
          "sha256": "bc15f1758ec574dec1f1c66330e0cc9804705e103fb5abab7f9015e5e8563f9f"
        }
      ]
    },
    "web": {
      "name": "feature/inbox-timeline-pagination",
      "head": "6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9",
      "diffSha256": "5b716dd27f498bfc11f5b7910922ce32fd628973e6039306a9b6159c7e9097d1",
      "sourceManifest": [
        {
          "path": "e2e/timeline-freshness.ts",
          "sha256": "ad41153df34c53f6674325b72887e701259ba7a8e752afd38ff4cdd8728c4cd0"
        },
        {
          "path": "e2e/timeline.spec.ts",
          "sha256": "266f63fc22a5de3482952b588d463388a048f2d98d13fa06a8107f298779a552"
        },
        {
          "path": "playwright.config.ts",
          "sha256": "d69c084d15cfef29ad23851036cb90309c60aa7a7b16c6810e3ae9b0adbbdd98"
        },
        {
          "path": "src/api.ts",
          "sha256": "87ba36bd21518725ba0e42221030d77b723144ef8d0581fddb2d9102233e7db2"
        },
        {
          "path": "src/telas/Inbox.tsx",
          "sha256": "8076cfabb46c92bc877b4975d70fca4b5d5928babc630f0683c3ace92172c945"
        },
        {
          "path": "src/tempoReal.spec.ts",
          "sha256": "378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5"
        },
        {
          "path": "src/tempoReal.ts",
          "sha256": "118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf"
        },
        {
          "path": "src/timeline.test.ts",
          "sha256": "16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4"
        },
        {
          "path": "src/timeline.ts",
          "sha256": "0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311"
        }
      ]
    }
  },
  "runtime": "v22.23.3",
  "database": {
    "name": "leadshug_timeline_20261014",
    "endpoint": "postgresql://timeline-postgres:5432/leadshug_timeline_20261014",
    "completedMigrations": 17
  },
  "endpoints": {
    "apiHealth": 200,
    "fixtureHealth": 200,
    "preview": 200,
    "servedBundle": "/assets/index-DSeTAho8.js"
  },
  "servedBundleSha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8",
  "distBundleSha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8",
  "apiBuildManifest": [
    {
      "path": "app.module.js",
      "sha256": "b45cdd1214f89b90539d28eeb418e4710fc116f777b75e2b2219dcf396ea9a2e"
    },
    {
      "path": "app.module.js.map",
      "sha256": "cb02d4de3cdc3f1000f0ff7c26ad36fbd86e5e2212ec8304cbc076a6505b97ca"
    },
    {
      "path": "domain/access/access.service.js",
      "sha256": "8d7aa42ad6374707bd7597b0a7276ddd8641099937b57d5f31acff6aadc3b0cd"
    },
    {
      "path": "domain/access/access.service.js.map",
      "sha256": "555328219c06254d5b93f46c93c1bc8ef5f3d62c09677d7ce81963301b21fcd7"
    },
    {
      "path": "domain/access/require-role.js",
      "sha256": "01c8962096c66d0e1451d28f29f7cec9512a173685f8b73c09d5b6dec8b02a48"
    },
    {
      "path": "domain/access/require-role.js.map",
      "sha256": "de3d20ccd31b78807a32b6c843542ceb1c440cd4615cb0b38612a43e9b7dff3d"
    },
    {
      "path": "domain/access/role.js",
      "sha256": "ebfb47023cc3fbd63a8978efb9711dde0734e039ab61b7efbcfc3028707b564f"
    },
    {
      "path": "domain/access/role.js.map",
      "sha256": "8af552827a54836af4dec449ae223196d5e76019a758aa358bd99d93b281c7b3"
    },
    {
      "path": "domain/access/scope.js",
      "sha256": "2131a69cd9981aa6e235f4e1c8685cfdb7a3afc1b6b6171230acc15fac787b2b"
    },
    {
      "path": "domain/access/scope.js.map",
      "sha256": "e3668a7eb951d51f3da971f6d0ac90760a6f7b6a7bf682518fcbe38c10022775"
    },
    {
      "path": "domain/acesso/convites.service.js",
      "sha256": "37ef502137d0554f62b0f78c38b6e8f32ed54eb559c52af2e8d7611aa2c4285d"
    },
    {
      "path": "domain/acesso/convites.service.js.map",
      "sha256": "7d545de6a0797e3c8a324f92f11357c137771a33ea198ac28eb46c4ee02b1ee0"
    },
    {
      "path": "domain/acesso/limite-de-recuperacao.service.js",
      "sha256": "20da372c4de39f758b4a88cca70ca60f7d0e55a8024a16662de33d682ffe6837"
    },
    {
      "path": "domain/acesso/limite-de-recuperacao.service.js.map",
      "sha256": "c713c0bea0f3a883cdd78a783aeb928dfc3bfcd0fc61f8e6309411aa459b05bc"
    },
    {
      "path": "domain/acesso/tokens.service.js",
      "sha256": "80a6613caba01ee3051869f181945d9be17393f2e91bdfa3c73c255beea5c20e"
    },
    {
      "path": "domain/acesso/tokens.service.js.map",
      "sha256": "bb13e9a30922a994cc554525410a8d4e3f94cbfe8318067235ee54c2af993abb"
    },
    {
      "path": "domain/channels/channels.service.js",
      "sha256": "a2b17f3924de628ad471e5ea122619d7a60ff086950b7c5bf8b62e8459572a47"
    },
    {
      "path": "domain/channels/channels.service.js.map",
      "sha256": "260ad189778024daffb305ed7edd192a1cedb8e5f7fa305af7e154212ec68fbd"
    },
    {
      "path": "domain/historico/atividades.service.js",
      "sha256": "a925f7d06685a4142777fffaa8e4a3ba2a80bc902a9ef1603006ff108043227e"
    },
    {
      "path": "domain/historico/atividades.service.js.map",
      "sha256": "fc7c911fab76f47f2cf5bb4e6e7e24c372d872018f07c7efd14cd69711de63f7"
    },
    {
      "path": "domain/historico/catalogo.js",
      "sha256": "757682151b3be088b5f20842b2f80e03e52ed791e92f9a1c8409a8c8cf21f1c8"
    },
    {
      "path": "domain/historico/catalogo.js.map",
      "sha256": "3d9258407b8bdc35299a01b018debca964c06d3c4f0816152056077446a8dc4a"
    },
    {
      "path": "domain/historico/cobertura.js",
      "sha256": "e9c4ca8f0e8447f96d1f00d597ae8fd8c0753f9da90609ad7a2560d016c0c78e"
    },
    {
      "path": "domain/historico/cobertura.js.map",
      "sha256": "fe86439fafc087adea6625ec18c71a30691e5c06b3bb06591fe519bd044d9c38"
    },
    {
      "path": "domain/historico/registro.service.js",
      "sha256": "b50329210510d0f926eb26c3f816322c2e21a846c1798cd1d451b162e256c893"
    },
    {
      "path": "domain/historico/registro.service.js.map",
      "sha256": "b1248b9d897f4617d07306037f6e73e1ca9cb3d5ae2e13c333569c4fca5359d1"
    },
    {
      "path": "domain/identity/identity.service.js",
      "sha256": "698d8817dd63f1b5d12676683fbdf397a70af9b817b2c4373d6d6bd87d3a97c9"
    },
    {
      "path": "domain/identity/identity.service.js.map",
      "sha256": "1c29611ba01e37e891af0519669f21dc5812ab407cd0cdff9a2cb3786e735c4e"
    },
    {
      "path": "domain/identity/login-attempt.service.js",
      "sha256": "42f01773f7a4e03801288db3d5d170f82c77b27b319a308bfdf732060b4cf766"
    },
    {
      "path": "domain/identity/login-attempt.service.js.map",
      "sha256": "7a7fda26f838aa279c66907df89ac53a0f6eba4232b67bd2990a32c84db9afca"
    },
    {
      "path": "domain/identity/password.service.js",
      "sha256": "68ca98aa0d8a7129b032637fb3c7af964c5e3278b538b107846b0b4ce8c62aa3"
    },
    {
      "path": "domain/identity/password.service.js.map",
      "sha256": "a38f9e4fbdffe1578aab0d387a1ff3d67839bbda60324a3ac039a0406804af77"
    },
    {
      "path": "domain/identity/usuarios.service.js",
      "sha256": "b0554e647531537d035be9442db457a2e6e99f361c6bf16cc017cbbec12f6bf1"
    },
    {
      "path": "domain/identity/usuarios.service.js.map",
      "sha256": "c62b2a565cb3107a56bf157935f2dd89dc3282a61482e17d0774efef1e8eebe9"
    },
    {
      "path": "domain/inbox/conversations.service.js",
      "sha256": "3e0d010ca0d6a9481f095530453630a88f92de59f3a891340098c907c839f877"
    },
    {
      "path": "domain/inbox/conversations.service.js.map",
      "sha256": "9d6370b1e0f86562e16b2e09f42b96f0b9c3f9725edb0ff05bc4a239230d156f"
    },
    {
      "path": "domain/inbox/historico.service.js",
      "sha256": "2a6dfb49672caa7d6756cfb4acb4cd922103824424da1284785e395ed1c44b1d"
    },
    {
      "path": "domain/inbox/historico.service.js.map",
      "sha256": "75abbfb0f0465b4746def75f67aa2f0457654b3dd787415b472cb17162d52b89"
    },
    {
      "path": "domain/inbox/incoming.service.js",
      "sha256": "916ae4596693e76dc13ca3d0ee47afd6a5c7d06009f21f0fcc6523003c54f91b"
    },
    {
      "path": "domain/inbox/incoming.service.js.map",
      "sha256": "192df1468c70ffffac7edd7e173772229ede92e6316627b580db207fc7af121c"
    },
    {
      "path": "domain/inbox/timeline-pagination.js",
      "sha256": "976fe29a100cdbdc97d7800f7c1cd0983ffd78709194ad251bb85668ef457f4f"
    },
    {
      "path": "domain/inbox/timeline-pagination.js.map",
      "sha256": "177eb534c3737e17e118702ea7d5b005cfe11ee7c0de421efc03400f88d7d466"
    },
    {
      "path": "domain/integration/api-key.service.js",
      "sha256": "5c073dab7bd47f48bc87a711613a1556365cea969473e87e4acfbbb5bfa2c3e2"
    },
    {
      "path": "domain/integration/api-key.service.js.map",
      "sha256": "cd1b37444884618cc316d0e2e69bcc42a0afaa47f8ebadfdf711cb4a115cbb22"
    },
    {
      "path": "domain/integration/outbound-webhook.service.js",
      "sha256": "f3053779b4df7125e3155cf58c325f9ece72e8148b2816f0c783d577d09f460b"
    },
    {
      "path": "domain/integration/outbound-webhook.service.js.map",
      "sha256": "21e303146e5075d3dbe2d9f2a22643b7fd885c03835270dd926bbbb55a5d292a"
    },
    {
      "path": "domain/integration/rate-limit.service.js",
      "sha256": "76e2e5a4553142e1aefeadb0dc9c2e722d37a1819b945bd3a926477145916349"
    },
    {
      "path": "domain/integration/rate-limit.service.js.map",
      "sha256": "6d26d5363e9a16ad6a5e136d6b6db9d24a1ceac70c2da47a90e9662068763c16"
    },
    {
      "path": "domain/painel/painel.service.js",
      "sha256": "323162d57a84bec6daa10851a13629eab4b7ac95d9ef22d3245cabdeb2fe4930"
    },
    {
      "path": "domain/painel/painel.service.js.map",
      "sha256": "0ed3af5c4ee2b5eef7484294e5f14d7a590e128233295b55a92b197157d09290"
    },
    {
      "path": "domain/produto/modulos.service.js",
      "sha256": "8c728689339ddadb96328ceffbd230cafb5760d2af960678ff7da19c7d1caef1"
    },
    {
      "path": "domain/produto/modulos.service.js.map",
      "sha256": "81565c0beed723136e11f9b21bd5f6251f553a9b43465a3f0ea1862142b1795f"
    },
    {
      "path": "domain/produto/onboarding.service.js",
      "sha256": "297dfeae78d8a8a6af3708b2ee50556ef137713c86b7b12742949a76f1da2dbd"
    },
    {
      "path": "domain/produto/onboarding.service.js.map",
      "sha256": "9b5505a8feb98e2ff700b1f9d76dc9cc8ea15032269abd8f51fcf2facebb0710"
    },
    {
      "path": "domain/setor/setor.service.js",
      "sha256": "b6b5dcac241025885ba48be11a9c9175171e13440befa5bd9156a7b5119d17a6"
    },
    {
      "path": "domain/setor/setor.service.js.map",
      "sha256": "23b9320cc47578dcd4bf83921c9028f479c346d7b2a61db407fcb6c214fd2a49"
    },
    {
      "path": "domain/tenancy/tenancy.service.js",
      "sha256": "f4c5e52974c3d1cdf46499adf1d6f9e2e6401396c54d63ac0f09ac6cbc0a14f6"
    },
    {
      "path": "domain/tenancy/tenancy.service.js.map",
      "sha256": "9f592bce0a19ce930e7b00d0cc75194b028b524a6852831e1aba6ac7b9efd4a9"
    },
    {
      "path": "health/health.controller.js",
      "sha256": "8a1b0a6d628ae4745e2f8ade580f930091bcdea034fc32a32efed67072eb3ad1"
    },
    {
      "path": "health/health.controller.js.map",
      "sha256": "c5da7192c39037fc7cf06c69b06e95da4e77ba77dc969e6464e2fced2d67183f"
    },
    {
      "path": "health/health.module.js",
      "sha256": "efe431d857e37b6198f8a0e0aaca4c706b1a71fc1e90b94799d1b8e312101a3d"
    },
    {
      "path": "health/health.module.js.map",
      "sha256": "1f3b309c98f10686086b882833440c24c2ceb285b01bb98d74a263edfa3e106f"
    },
    {
      "path": "infra/arquivos/armazenamento.js",
      "sha256": "d64de1bf42bdd06d1b807ed983e9469a0d020a4a18953510475c4c969496495d"
    },
    {
      "path": "infra/arquivos/armazenamento.js.map",
      "sha256": "02bbf78ee3a5bad06d271f1852412c6bc8766e2509e7108fce96c0b1fbd0d635"
    },
    {
      "path": "infra/config/modulos.js",
      "sha256": "4d4eeaa481bb6a7c179f34d5101355cd54cd1e6ae710d1542602c3be89b954c7"
    },
    {
      "path": "infra/config/modulos.js.map",
      "sha256": "3fd96019064df2936747894d6d636cc0eab19c0b056a8a8a2fa6c6748ae6125e"
    },
    {
      "path": "infra/http/body-parsers.js",
      "sha256": "74ac17e839b9e59f5089c4275d354432a92dddf06437c39169d578a930f6887b"
    },
    {
      "path": "infra/http/body-parsers.js.map",
      "sha256": "bb68e5ff63bcdff952f5e8514225ba8a67692b9ffcd45d76032a4143dfcdca67"
    },
    {
      "path": "infra/http/origens.js",
      "sha256": "bb01d013d47881c4680c144cfff3675151a8bf6ec04ab11855449f130a522de6"
    },
    {
      "path": "infra/http/origens.js.map",
      "sha256": "344419b2e200165016933f63e5816b80977d31121475977f109218fc100564ee"
    },
    {
      "path": "infra/prisma/banco-atrasado.filter.js",
      "sha256": "000132808c610f7388a4debba13892382649498f5fa5299c0e5b59df49c0078f"
    },
    {
      "path": "infra/prisma/banco-atrasado.filter.js.map",
      "sha256": "cf4a1d22cff6bda36814f9b7e408030a1e48c8cf3d971a72e095c0c69849d13c"
    },
    {
      "path": "infra/prisma/migracoes.js",
      "sha256": "6858e42cdac13a0e0c1a640137fa00c7d44bb9fd00b4fe249491306aff24f82e"
    },
    {
      "path": "infra/prisma/migracoes.js.map",
      "sha256": "a1b2b565ea637fb6fcb1214bbb0e8bdbe6b307a5acb5d55d0207ffb9e6ee13e4"
    },
    {
      "path": "infra/prisma/prisma.module.js",
      "sha256": "bd50cc179c8ded790745340f8e9b3f68dbc45a6dd9e5cc6db5e6927b72695278"
    },
    {
      "path": "infra/prisma/prisma.module.js.map",
      "sha256": "b04a741b3ecaecda405ef018ecfd373f1103e6653339cd64ffeee0b5a7d3b9e0"
    },
    {
      "path": "infra/prisma/prisma.service.js",
      "sha256": "d62e2bd3aabe40f217750b9d2648f180b208f8fde190ab154080df4cf0482010"
    },
    {
      "path": "infra/prisma/prisma.service.js.map",
      "sha256": "07b44c0e1ddd5c0d9b97c4831558f8f121f5a6d6b412110aa7234c7d75271b5e"
    },
    {
      "path": "infra/session/session.service.js",
      "sha256": "d2faf29db0146fff05629985e1e53c2bb0460e1cfd565869f362c45ae382344a"
    },
    {
      "path": "infra/session/session.service.js.map",
      "sha256": "86da7c6fe2742c3da84b855551a5f17e3e543a0c738e5108d497f97728437444"
    },
    {
      "path": "integrations/email/email.client.js",
      "sha256": "401225fff6a75f28bceca207b3e48a4d72e37b2688efd824d979cc5cc68cc446"
    },
    {
      "path": "integrations/email/email.client.js.map",
      "sha256": "2d64c712daa0b2711154b8b8895f0e0eacc48133855b1c44e356fc757e48be7e"
    },
    {
      "path": "integrations/evolution/evolution.client.js",
      "sha256": "8a1092b6c6078d718a29f5c0e5766b4b77ba71b441f91f75d4089d887909eb7a"
    },
    {
      "path": "integrations/evolution/evolution.client.js.map",
      "sha256": "47ebb570237451aa7d8fe156900336afeae7857caf6e6e5e297302b7166c4d4b"
    },
    {
      "path": "integrations/meta/meta.client.js",
      "sha256": "f30b8ca9327610aab072c690dda672d30676338bb24401571750f9231fab5a98"
    },
    {
      "path": "integrations/meta/meta.client.js.map",
      "sha256": "3fa37d0950e8b86459c8d80832f09eca5d508bf29e69832913314c2456ebcd1b"
    },
    {
      "path": "integrations/typebot/typebot.client.js",
      "sha256": "6617d233eba4994712cbfa0ff2b843f5fa553744af58182291d08deb4aa23980"
    },
    {
      "path": "integrations/typebot/typebot.client.js.map",
      "sha256": "723422a6f4f38c1d76ae50bb5fee8b2d97c0fc9a275db5d64adfac6bd77da4a9"
    },
    {
      "path": "main.js",
      "sha256": "4939123b00a86d0fb47ed2483ee13cb8ec0fbc374e565653c32724e920c2b9f0"
    },
    {
      "path": "main.js.map",
      "sha256": "d3471d745ee6e99a137b76043ba27cd743dc23ebb6b33e5eab854a1dc54be6ed"
    },
    {
      "path": "realtime/realtime.module.js",
      "sha256": "97bbba1dac2ec12e212252752b4668d308e75ecc1abab53562e6131907ae47a1"
    },
    {
      "path": "realtime/realtime.module.js.map",
      "sha256": "587e6fc05bd203f154986eb313bd999c8a1200dab11ee4760a5b7f0c24244678"
    },
    {
      "path": "realtime/realtime.service.js",
      "sha256": "584e1fdaf42605d4977f947746299626c90be7c9f4082ce66cbcba16a6c3b91d"
    },
    {
      "path": "realtime/realtime.service.js.map",
      "sha256": "467dbf83b7f870839cb14941868bd9d62f467c3cba209fde4c9280a4b3038cc0"
    },
    {
      "path": "rotinas/agendador.service.js",
      "sha256": "ac67fc82e61e4623ad4df1b1780e402ccbc0506c73364c10879a82a2c63bd646"
    },
    {
      "path": "rotinas/agendador.service.js.map",
      "sha256": "89253785a30b2339ff1f5aa102d25c8037337f0a98ff75c9a27566feaee1d8d5"
    },
    {
      "path": "rotinas/expurgo-de-webhook.rotina.js",
      "sha256": "c5b63269edbb6addfb2992b121d4fec9c86cd8ca6886eaf12e57ab36122a1031"
    },
    {
      "path": "rotinas/expurgo-de-webhook.rotina.js.map",
      "sha256": "ba156b796c84a40c9d9abd3ceb482a2a64ce8abeb8a24c171b68dffbdb384827"
    },
    {
      "path": "rotinas/rotina-periodica.js",
      "sha256": "b4308c664abf488ac88794d3c70beb53f85c2ded0d389cfe93db4b6fe05372aa"
    },
    {
      "path": "rotinas/rotina-periodica.js.map",
      "sha256": "79d8de9057bd81f38591141bd00cd03b7f3eb6707743326114b939e15a0cf87a"
    },
    {
      "path": "rotinas/rotinas.module.js",
      "sha256": "477fa6ea09780db6846e6c98b1ae5d3c49d0dd4d1da83d35a89b3d10cc44f787"
    },
    {
      "path": "rotinas/rotinas.module.js.map",
      "sha256": "2794be593c229ca6539fb72bda23e25f419f5e53402fa54b05c8611eca6e64b0"
    },
    {
      "path": "surfaces/bff/arquivos.controller.js",
      "sha256": "1611c531ab804d52bfaa9ee863d300f36de51b2440dfc9b8c7158ec4cb0627ac"
    },
    {
      "path": "surfaces/bff/arquivos.controller.js.map",
      "sha256": "a90116d7c2052cb30ce29b767b47d0c477177bc7c18a96b2e4b6d1a967661864"
    },
    {
      "path": "surfaces/bff/atividades.controller.js",
      "sha256": "e1a42ca0f779cd9b0c7cab5f06ef566dd36f601405316a1d8b30f80ce3126cfe"
    },
    {
      "path": "surfaces/bff/atividades.controller.js.map",
      "sha256": "35f6e290937064a113530f13275eda28185c2523a5ea4378edc490f9087beccd"
    },
    {
      "path": "surfaces/bff/auth.controller.js",
      "sha256": "487de6414692719df868e029dc9767d607807586d432df7061990256204bdbf0"
    },
    {
      "path": "surfaces/bff/auth.controller.js.map",
      "sha256": "16e1931fb9f197ebfb0d11272b3abdafb18458cd4aae2b18b55c0c030f10df73"
    },
    {
      "path": "surfaces/bff/bff.module.js",
      "sha256": "2db12a7c3febbab49dbda42ad5aa493b1a5461b0b7370ae8f04fc5848ea865cc"
    },
    {
      "path": "surfaces/bff/bff.module.js.map",
      "sha256": "9ef9c4bad62151efb3605d5eddb7202e4825e95775caf7c93d1cc0421429536b"
    },
    {
      "path": "surfaces/bff/channels.controller.js",
      "sha256": "4e4641c1c5371fd54d78889ed9525e616a0df633b55e246bef797cf46e906ff0"
    },
    {
      "path": "surfaces/bff/channels.controller.js.map",
      "sha256": "d371a6c76268b76b107b43853cfbb45ad2555aec5bdaa04db1ab27a3828152df"
    },
    {
      "path": "surfaces/bff/conversations.controller.js",
      "sha256": "8ccfbe252ce3fdb54ae0c7f820e88f5b0fb957e69a526e4819813e9269e8a3a9"
    },
    {
      "path": "surfaces/bff/conversations.controller.js.map",
      "sha256": "2769319b467fbcf28443fb05a554a52ffa2004b0e4f8573f2a7987e8008a7144"
    },
    {
      "path": "surfaces/bff/historico.controller.js",
      "sha256": "e982961367a40c41df247787c7f5d5aaa22b929374fc88028bfc4464c9b89c0f"
    },
    {
      "path": "surfaces/bff/historico.controller.js.map",
      "sha256": "d46e0b29e0a107e68df060a4c311beb83dc0e285ec956677ba2e0b68501ae4b5"
    },
    {
      "path": "surfaces/bff/integracao.controller.js",
      "sha256": "431e5820de4421360ce679a9a748b9d3f500999a1474c2ef096635ff94b460f7"
    },
    {
      "path": "surfaces/bff/integracao.controller.js.map",
      "sha256": "3703f5815637d4c9f3d4ee72df6d3c9a9da967620d09aac93119485e8ea66891"
    },
    {
      "path": "surfaces/bff/me.controller.js",
      "sha256": "c9a3bed3ed8db1d1a12f745fd97c2f069f0d5773dcbe7ca1231a07029a3f2121"
    },
    {
      "path": "surfaces/bff/me.controller.js.map",
      "sha256": "3f6474a5d8cd01d7fe793fc5df4ee3d97ce9a94bf6592ef6452adcebccc7f09d"
    },
    {
      "path": "surfaces/bff/onboarding.controller.js",
      "sha256": "835092e537421aa6c666fa60ec1e38422e6b502f87e93c6d30a5870bb18e2caf"
    },
    {
      "path": "surfaces/bff/onboarding.controller.js.map",
      "sha256": "1e235e3b3ed6aad63a0796fe267f089b409fd9717df4bf3f51635d0016ec711d"
    },
    {
      "path": "surfaces/bff/painel.controller.js",
      "sha256": "1e46acc3988aa590790118b4fbd0adf77b7a91bc44096f8e9627b823ac3cdf83"
    },
    {
      "path": "surfaces/bff/painel.controller.js.map",
      "sha256": "26a638493c43fe3a5b4b612e96454ecbd46c1e8ef2d19751861ebb9ff9a18775"
    },
    {
      "path": "surfaces/bff/session.middleware.js",
      "sha256": "fc5af440f1309c0925e430cf490bd32ca5ddbdf96d8d0736ffbe6af541d27e67"
    },
    {
      "path": "surfaces/bff/session.middleware.js.map",
      "sha256": "4a172b78eeecffbecdf47b5f54bf92ed16fe93b4daadd59b0a03c86206763c41"
    },
    {
      "path": "surfaces/bff/setores.controller.js",
      "sha256": "cdf8e88792b0908cdca31d1b9a36283fa7971bedd021bc3ebeb9951c28cbd038"
    },
    {
      "path": "surfaces/bff/setores.controller.js.map",
      "sha256": "4960b4cb8e2ef36100f14be5dd9623c152039d5172bf44eaa7c1b4b390064205"
    },
    {
      "path": "surfaces/bff/usuarios.controller.js",
      "sha256": "9af33d16920d3bad25b9b74819b29013a438e0d92080ca772f3b7510299b4aa2"
    },
    {
      "path": "surfaces/bff/usuarios.controller.js.map",
      "sha256": "bc689d7705c8e8f957ef06102d24f4515a13d8e1851d27f7cac73e95fff05920"
    },
    {
      "path": "surfaces/internal/internal.module.js",
      "sha256": "c92b694a24980f6b2b370174de2004ebcfc102949e25dc814c6b6c4a636d9689"
    },
    {
      "path": "surfaces/internal/internal.module.js.map",
      "sha256": "e2a4cf18bf19eaf05b995543bd037509ffb5283dbb791b569840a9850ab33f6f"
    },
    {
      "path": "surfaces/internal/mantenedoras.controller.js",
      "sha256": "e45802cd4ffff98bf828560878ee6611123f3a45344c6f2152e2ca9ecb39210c"
    },
    {
      "path": "surfaces/internal/mantenedoras.controller.js.map",
      "sha256": "da1dc19549b3a3441d0ce92469dcaabb6e6098e9650182a5f54081c3ffdcdc35"
    },
    {
      "path": "surfaces/internal/service-credential.middleware.js",
      "sha256": "2084df02fec5029971c695e61b6add89cbf76bf9806a6da56a32194a171d0274"
    },
    {
      "path": "surfaces/internal/service-credential.middleware.js.map",
      "sha256": "cc6d9edb635d5b900bd73bb4b2213b6bbfeda116902f2b1fa092cab09091eae3"
    },
    {
      "path": "surfaces/public/api-key.middleware.js",
      "sha256": "51c1ba5b526dbeac89707d3718f47cedc11c6c72d32f7224fc587ecd40e04465"
    },
    {
      "path": "surfaces/public/api-key.middleware.js.map",
      "sha256": "9fea00ba3bdbedf267e127603196a558f1f943bdb057a064e6ec96fad746a3de"
    },
    {
      "path": "surfaces/public/conversations.controller.js",
      "sha256": "c1b62747445c0e7608d8d9f0b6292d2b8d17fd9163e062ff2ce572bd290591a2"
    },
    {
      "path": "surfaces/public/conversations.controller.js.map",
      "sha256": "e08ca8d6202135f9b5f02e34b8d0e09533236f005ff9cb8d8e50187cd0f9b440"
    },
    {
      "path": "surfaces/public/public.module.js",
      "sha256": "a793879d1bd1d3124eeb114b0bcf360b64376b3cede6a5c195cb091876fecaf2"
    },
    {
      "path": "surfaces/public/public.module.js.map",
      "sha256": "48ff48355c8e2255d3f0bf2cfc88170ecd836a688d91c12357f938011128a15d"
    },
    {
      "path": "surfaces/webhooks/evolution.controller.js",
      "sha256": "cae5cc1c2d450fbfcd4a53f7dc0533e12331b8d128ce29481ab4b339682c519a"
    },
    {
      "path": "surfaces/webhooks/evolution.controller.js.map",
      "sha256": "98d074ad8fc18cd77710480b6e2c759f2d101ec7568f109279163c0a3fe4ea96"
    },
    {
      "path": "surfaces/webhooks/meta.controller.js",
      "sha256": "6b7c5626a5b26df2c46569b57a2dc6366768d70bfaac9362ac77fbd824eff2a7"
    },
    {
      "path": "surfaces/webhooks/meta.controller.js.map",
      "sha256": "aad8612ff69766ad3b0b4a24628110699380954fc30c2eb52c1a5a4f92f7789f"
    },
    {
      "path": "surfaces/webhooks/webhooks.module.js",
      "sha256": "9a4733bab8a15183b73388e634b5b268264c760aab3eb4506c653ea0772ca38f"
    },
    {
      "path": "surfaces/webhooks/webhooks.module.js.map",
      "sha256": "84b554deba5b1a2c5caf1a02e275d705eb6411720618cf429a9ee9113afe44cb"
    },
    {
      "path": "tsconfig.build.tsbuildinfo",
      "sha256": "e3fc9e379512559037a5c89d767290a4c84db13fd7668a56499b596a282649ce"
    }
  ],
  "webDistManifest": [
    {
      "path": "assets/index-DSeTAho8.js",
      "sha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8"
    },
    {
      "path": "assets/index-wuzy3kMN.css",
      "sha256": "38f979314555cda8b834189ed5c64826bbc309e294091c9f5c54ee5f8bd2aadd"
    },
    {
      "path": "config.js",
      "sha256": "1ad17fefa4173ed847cabd79e7fdc1b262fa19ea4ff33c3ef435e141275fb532"
    },
    {
      "path": "index.html",
      "sha256": "610b0638ae994cde6f35d2bff22c0a4a94c213b0da9a5e67f94680436670a538"
    }
  ]
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-full-final31-20261015.json

```
{
  "capturedAtUtc": "2026-10-15T03:39:29.661Z",
  "runId": "full-final31-20261015",
  "branch": {
    "api": {
      "name": "feature/inbox-timeline-pagination",
      "head": "5db3fbe2043428749895fc3ff6441e9457467dd0",
      "diffSha256": "d3d84c015c24348b1dbc885a90d66ff8f88eadf35a75b0a256a38c3f1230708b",
      "sourceManifest": [
        {
          "path": "src/domain/inbox/conversations.service.ts",
          "sha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.spec.ts",
          "sha256": "a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.ts",
          "sha256": "d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af"
        },
        {
          "path": "src/surfaces/bff/conversations.controller.ts",
          "sha256": "0b5c46a78aafd8085b609ad711bcdb7626263094f434240f37b8700f20291565"
        },
        {
          "path": "test/atendimento.e2e-spec.ts",
          "sha256": "1bb4acb19fc522b397424b319ab04563e3608605dcfe307970eecdd0d464b5b8"
        },
        {
          "path": "test/browser-server.cjs",
          "sha256": "031e9d1e282603c098c4bb594fb13a08ab2bc2f301c9a3ebb5a6362cae6fe42b"
        },
        {
          "path": "test/timeline-fixtures.cjs",
          "sha256": "bc15f1758ec574dec1f1c66330e0cc9804705e103fb5abab7f9015e5e8563f9f"
        }
      ]
    },
    "web": {
      "name": "feature/inbox-timeline-pagination",
      "head": "6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9",
      "diffSha256": "5b716dd27f498bfc11f5b7910922ce32fd628973e6039306a9b6159c7e9097d1",
      "sourceManifest": [
        {
          "path": "e2e/timeline-freshness.ts",
          "sha256": "ad41153df34c53f6674325b72887e701259ba7a8e752afd38ff4cdd8728c4cd0"
        },
        {
          "path": "e2e/timeline.spec.ts",
          "sha256": "266f63fc22a5de3482952b588d463388a048f2d98d13fa06a8107f298779a552"
        },
        {
          "path": "playwright.config.ts",
          "sha256": "d69c084d15cfef29ad23851036cb90309c60aa7a7b16c6810e3ae9b0adbbdd98"
        },
        {
          "path": "src/api.ts",
          "sha256": "87ba36bd21518725ba0e42221030d77b723144ef8d0581fddb2d9102233e7db2"
        },
        {
          "path": "src/telas/Inbox.tsx",
          "sha256": "8076cfabb46c92bc877b4975d70fca4b5d5928babc630f0683c3ace92172c945"
        },
        {
          "path": "src/tempoReal.spec.ts",
          "sha256": "378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5"
        },
        {
          "path": "src/tempoReal.ts",
          "sha256": "118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf"
        },
        {
          "path": "src/timeline.test.ts",
          "sha256": "16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4"
        },
        {
          "path": "src/timeline.ts",
          "sha256": "0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311"
        }
      ]
    }
  },
  "runtime": "v22.23.3",
  "database": {
    "name": "leadshug_timeline_20261014",
    "endpoint": "postgresql://timeline-postgres:5432/leadshug_timeline_20261014",
    "completedMigrations": 17
  },
  "endpoints": {
    "apiHealth": 200,
    "fixtureHealth": 200,
    "preview": 200,
    "servedBundle": "/assets/index-DSeTAho8.js"
  },
  "servedBundleSha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8",
  "distBundleSha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8",
  "apiBuildManifest": [
    {
      "path": "app.module.js",
      "sha256": "b45cdd1214f89b90539d28eeb418e4710fc116f777b75e2b2219dcf396ea9a2e"
    },
    {
      "path": "app.module.js.map",
      "sha256": "cb02d4de3cdc3f1000f0ff7c26ad36fbd86e5e2212ec8304cbc076a6505b97ca"
    },
    {
      "path": "domain/access/access.service.js",
      "sha256": "8d7aa42ad6374707bd7597b0a7276ddd8641099937b57d5f31acff6aadc3b0cd"
    },
    {
      "path": "domain/access/access.service.js.map",
      "sha256": "555328219c06254d5b93f46c93c1bc8ef5f3d62c09677d7ce81963301b21fcd7"
    },
    {
      "path": "domain/access/require-role.js",
      "sha256": "01c8962096c66d0e1451d28f29f7cec9512a173685f8b73c09d5b6dec8b02a48"
    },
    {
      "path": "domain/access/require-role.js.map",
      "sha256": "de3d20ccd31b78807a32b6c843542ceb1c440cd4615cb0b38612a43e9b7dff3d"
    },
    {
      "path": "domain/access/role.js",
      "sha256": "ebfb47023cc3fbd63a8978efb9711dde0734e039ab61b7efbcfc3028707b564f"
    },
    {
      "path": "domain/access/role.js.map",
      "sha256": "8af552827a54836af4dec449ae223196d5e76019a758aa358bd99d93b281c7b3"
    },
    {
      "path": "domain/access/scope.js",
      "sha256": "2131a69cd9981aa6e235f4e1c8685cfdb7a3afc1b6b6171230acc15fac787b2b"
    },
    {
      "path": "domain/access/scope.js.map",
      "sha256": "e3668a7eb951d51f3da971f6d0ac90760a6f7b6a7bf682518fcbe38c10022775"
    },
    {
      "path": "domain/acesso/convites.service.js",
      "sha256": "37ef502137d0554f62b0f78c38b6e8f32ed54eb559c52af2e8d7611aa2c4285d"
    },
    {
      "path": "domain/acesso/convites.service.js.map",
      "sha256": "7d545de6a0797e3c8a324f92f11357c137771a33ea198ac28eb46c4ee02b1ee0"
    },
    {
      "path": "domain/acesso/limite-de-recuperacao.service.js",
      "sha256": "20da372c4de39f758b4a88cca70ca60f7d0e55a8024a16662de33d682ffe6837"
    },
    {
      "path": "domain/acesso/limite-de-recuperacao.service.js.map",
      "sha256": "c713c0bea0f3a883cdd78a783aeb928dfc3bfcd0fc61f8e6309411aa459b05bc"
    },
    {
      "path": "domain/acesso/tokens.service.js",
      "sha256": "80a6613caba01ee3051869f181945d9be17393f2e91bdfa3c73c255beea5c20e"
    },
    {
      "path": "domain/acesso/tokens.service.js.map",
      "sha256": "bb13e9a30922a994cc554525410a8d4e3f94cbfe8318067235ee54c2af993abb"
    },
    {
      "path": "domain/channels/channels.service.js",
      "sha256": "a2b17f3924de628ad471e5ea122619d7a60ff086950b7c5bf8b62e8459572a47"
    },
    {
      "path": "domain/channels/channels.service.js.map",
      "sha256": "260ad189778024daffb305ed7edd192a1cedb8e5f7fa305af7e154212ec68fbd"
    },
    {
      "path": "domain/historico/atividades.service.js",
      "sha256": "a925f7d06685a4142777fffaa8e4a3ba2a80bc902a9ef1603006ff108043227e"
    },
    {
      "path": "domain/historico/atividades.service.js.map",
      "sha256": "fc7c911fab76f47f2cf5bb4e6e7e24c372d872018f07c7efd14cd69711de63f7"
    },
    {
      "path": "domain/historico/catalogo.js",
      "sha256": "757682151b3be088b5f20842b2f80e03e52ed791e92f9a1c8409a8c8cf21f1c8"
    },
    {
      "path": "domain/historico/catalogo.js.map",
      "sha256": "3d9258407b8bdc35299a01b018debca964c06d3c4f0816152056077446a8dc4a"
    },
    {
      "path": "domain/historico/cobertura.js",
      "sha256": "e9c4ca8f0e8447f96d1f00d597ae8fd8c0753f9da90609ad7a2560d016c0c78e"
    },
    {
      "path": "domain/historico/cobertura.js.map",
      "sha256": "fe86439fafc087adea6625ec18c71a30691e5c06b3bb06591fe519bd044d9c38"
    },
    {
      "path": "domain/historico/registro.service.js",
      "sha256": "b50329210510d0f926eb26c3f816322c2e21a846c1798cd1d451b162e256c893"
    },
    {
      "path": "domain/historico/registro.service.js.map",
      "sha256": "b1248b9d897f4617d07306037f6e73e1ca9cb3d5ae2e13c333569c4fca5359d1"
    },
    {
      "path": "domain/identity/identity.service.js",
      "sha256": "698d8817dd63f1b5d12676683fbdf397a70af9b817b2c4373d6d6bd87d3a97c9"
    },
    {
      "path": "domain/identity/identity.service.js.map",
      "sha256": "1c29611ba01e37e891af0519669f21dc5812ab407cd0cdff9a2cb3786e735c4e"
    },
    {
      "path": "domain/identity/login-attempt.service.js",
      "sha256": "42f01773f7a4e03801288db3d5d170f82c77b27b319a308bfdf732060b4cf766"
    },
    {
      "path": "domain/identity/login-attempt.service.js.map",
      "sha256": "7a7fda26f838aa279c66907df89ac53a0f6eba4232b67bd2990a32c84db9afca"
    },
    {
      "path": "domain/identity/password.service.js",
      "sha256": "68ca98aa0d8a7129b032637fb3c7af964c5e3278b538b107846b0b4ce8c62aa3"
    },
    {
      "path": "domain/identity/password.service.js.map",
      "sha256": "a38f9e4fbdffe1578aab0d387a1ff3d67839bbda60324a3ac039a0406804af77"
    },
    {
      "path": "domain/identity/usuarios.service.js",
      "sha256": "b0554e647531537d035be9442db457a2e6e99f361c6bf16cc017cbbec12f6bf1"
    },
    {
      "path": "domain/identity/usuarios.service.js.map",
      "sha256": "c62b2a565cb3107a56bf157935f2dd89dc3282a61482e17d0774efef1e8eebe9"
    },
    {
      "path": "domain/inbox/conversations.service.js",
      "sha256": "3e0d010ca0d6a9481f095530453630a88f92de59f3a891340098c907c839f877"
    },
    {
      "path": "domain/inbox/conversations.service.js.map",
      "sha256": "9d6370b1e0f86562e16b2e09f42b96f0b9c3f9725edb0ff05bc4a239230d156f"
    },
    {
      "path": "domain/inbox/historico.service.js",
      "sha256": "2a6dfb49672caa7d6756cfb4acb4cd922103824424da1284785e395ed1c44b1d"
    },
    {
      "path": "domain/inbox/historico.service.js.map",
      "sha256": "75abbfb0f0465b4746def75f67aa2f0457654b3dd787415b472cb17162d52b89"
    },
    {
      "path": "domain/inbox/incoming.service.js",
      "sha256": "916ae4596693e76dc13ca3d0ee47afd6a5c7d06009f21f0fcc6523003c54f91b"
    },
    {
      "path": "domain/inbox/incoming.service.js.map",
      "sha256": "192df1468c70ffffac7edd7e173772229ede92e6316627b580db207fc7af121c"
    },
    {
      "path": "domain/inbox/timeline-pagination.js",
      "sha256": "976fe29a100cdbdc97d7800f7c1cd0983ffd78709194ad251bb85668ef457f4f"
    },
    {
      "path": "domain/inbox/timeline-pagination.js.map",
      "sha256": "177eb534c3737e17e118702ea7d5b005cfe11ee7c0de421efc03400f88d7d466"
    },
    {
      "path": "domain/integration/api-key.service.js",
      "sha256": "5c073dab7bd47f48bc87a711613a1556365cea969473e87e4acfbbb5bfa2c3e2"
    },
    {
      "path": "domain/integration/api-key.service.js.map",
      "sha256": "cd1b37444884618cc316d0e2e69bcc42a0afaa47f8ebadfdf711cb4a115cbb22"
    },
    {
      "path": "domain/integration/outbound-webhook.service.js",
      "sha256": "f3053779b4df7125e3155cf58c325f9ece72e8148b2816f0c783d577d09f460b"
    },
    {
      "path": "domain/integration/outbound-webhook.service.js.map",
      "sha256": "21e303146e5075d3dbe2d9f2a22643b7fd885c03835270dd926bbbb55a5d292a"
    },
    {
      "path": "domain/integration/rate-limit.service.js",
      "sha256": "76e2e5a4553142e1aefeadb0dc9c2e722d37a1819b945bd3a926477145916349"
    },
    {
      "path": "domain/integration/rate-limit.service.js.map",
      "sha256": "6d26d5363e9a16ad6a5e136d6b6db9d24a1ceac70c2da47a90e9662068763c16"
    },
    {
      "path": "domain/painel/painel.service.js",
      "sha256": "323162d57a84bec6daa10851a13629eab4b7ac95d9ef22d3245cabdeb2fe4930"
    },
    {
      "path": "domain/painel/painel.service.js.map",
      "sha256": "0ed3af5c4ee2b5eef7484294e5f14d7a590e128233295b55a92b197157d09290"
    },
    {
      "path": "domain/produto/modulos.service.js",
      "sha256": "8c728689339ddadb96328ceffbd230cafb5760d2af960678ff7da19c7d1caef1"
    },
    {
      "path": "domain/produto/modulos.service.js.map",
      "sha256": "81565c0beed723136e11f9b21bd5f6251f553a9b43465a3f0ea1862142b1795f"
    },
    {
      "path": "domain/produto/onboarding.service.js",
      "sha256": "297dfeae78d8a8a6af3708b2ee50556ef137713c86b7b12742949a76f1da2dbd"
    },
    {
      "path": "domain/produto/onboarding.service.js.map",
      "sha256": "9b5505a8feb98e2ff700b1f9d76dc9cc8ea15032269abd8f51fcf2facebb0710"
    },
    {
      "path": "domain/setor/setor.service.js",
      "sha256": "b6b5dcac241025885ba48be11a9c9175171e13440befa5bd9156a7b5119d17a6"
    },
    {
      "path": "domain/setor/setor.service.js.map",
      "sha256": "23b9320cc47578dcd4bf83921c9028f479c346d7b2a61db407fcb6c214fd2a49"
    },
    {
      "path": "domain/tenancy/tenancy.service.js",
      "sha256": "f4c5e52974c3d1cdf46499adf1d6f9e2e6401396c54d63ac0f09ac6cbc0a14f6"
    },
    {
      "path": "domain/tenancy/tenancy.service.js.map",
      "sha256": "9f592bce0a19ce930e7b00d0cc75194b028b524a6852831e1aba6ac7b9efd4a9"
    },
    {
      "path": "health/health.controller.js",
      "sha256": "8a1b0a6d628ae4745e2f8ade580f930091bcdea034fc32a32efed67072eb3ad1"
    },
    {
      "path": "health/health.controller.js.map",
      "sha256": "c5da7192c39037fc7cf06c69b06e95da4e77ba77dc969e6464e2fced2d67183f"
    },
    {
      "path": "health/health.module.js",
      "sha256": "efe431d857e37b6198f8a0e0aaca4c706b1a71fc1e90b94799d1b8e312101a3d"
    },
    {
      "path": "health/health.module.js.map",
      "sha256": "1f3b309c98f10686086b882833440c24c2ceb285b01bb98d74a263edfa3e106f"
    },
    {
      "path": "infra/arquivos/armazenamento.js",
      "sha256": "d64de1bf42bdd06d1b807ed983e9469a0d020a4a18953510475c4c969496495d"
    },
    {
      "path": "infra/arquivos/armazenamento.js.map",
      "sha256": "02bbf78ee3a5bad06d271f1852412c6bc8766e2509e7108fce96c0b1fbd0d635"
    },
    {
      "path": "infra/config/modulos.js",
      "sha256": "4d4eeaa481bb6a7c179f34d5101355cd54cd1e6ae710d1542602c3be89b954c7"
    },
    {
      "path": "infra/config/modulos.js.map",
      "sha256": "3fd96019064df2936747894d6d636cc0eab19c0b056a8a8a2fa6c6748ae6125e"
    },
    {
      "path": "infra/http/body-parsers.js",
      "sha256": "74ac17e839b9e59f5089c4275d354432a92dddf06437c39169d578a930f6887b"
    },
    {
      "path": "infra/http/body-parsers.js.map",
      "sha256": "bb68e5ff63bcdff952f5e8514225ba8a67692b9ffcd45d76032a4143dfcdca67"
    },
    {
      "path": "infra/http/origens.js",
      "sha256": "bb01d013d47881c4680c144cfff3675151a8bf6ec04ab11855449f130a522de6"
    },
    {
      "path": "infra/http/origens.js.map",
      "sha256": "344419b2e200165016933f63e5816b80977d31121475977f109218fc100564ee"
    },
    {
      "path": "infra/prisma/banco-atrasado.filter.js",
      "sha256": "000132808c610f7388a4debba13892382649498f5fa5299c0e5b59df49c0078f"
    },
    {
      "path": "infra/prisma/banco-atrasado.filter.js.map",
      "sha256": "cf4a1d22cff6bda36814f9b7e408030a1e48c8cf3d971a72e095c0c69849d13c"
    },
    {
      "path": "infra/prisma/migracoes.js",
      "sha256": "6858e42cdac13a0e0c1a640137fa00c7d44bb9fd00b4fe249491306aff24f82e"
    },
    {
      "path": "infra/prisma/migracoes.js.map",
      "sha256": "a1b2b565ea637fb6fcb1214bbb0e8bdbe6b307a5acb5d55d0207ffb9e6ee13e4"
    },
    {
      "path": "infra/prisma/prisma.module.js",
      "sha256": "bd50cc179c8ded790745340f8e9b3f68dbc45a6dd9e5cc6db5e6927b72695278"
    },
    {
      "path": "infra/prisma/prisma.module.js.map",
      "sha256": "b04a741b3ecaecda405ef018ecfd373f1103e6653339cd64ffeee0b5a7d3b9e0"
    },
    {
      "path": "infra/prisma/prisma.service.js",
      "sha256": "d62e2bd3aabe40f217750b9d2648f180b208f8fde190ab154080df4cf0482010"
    },
    {
      "path": "infra/prisma/prisma.service.js.map",
      "sha256": "07b44c0e1ddd5c0d9b97c4831558f8f121f5a6d6b412110aa7234c7d75271b5e"
    },
    {
      "path": "infra/session/session.service.js",
      "sha256": "d2faf29db0146fff05629985e1e53c2bb0460e1cfd565869f362c45ae382344a"
    },
    {
      "path": "infra/session/session.service.js.map",
      "sha256": "86da7c6fe2742c3da84b855551a5f17e3e543a0c738e5108d497f97728437444"
    },
    {
      "path": "integrations/email/email.client.js",
      "sha256": "401225fff6a75f28bceca207b3e48a4d72e37b2688efd824d979cc5cc68cc446"
    },
    {
      "path": "integrations/email/email.client.js.map",
      "sha256": "2d64c712daa0b2711154b8b8895f0e0eacc48133855b1c44e356fc757e48be7e"
    },
    {
      "path": "integrations/evolution/evolution.client.js",
      "sha256": "8a1092b6c6078d718a29f5c0e5766b4b77ba71b441f91f75d4089d887909eb7a"
    },
    {
      "path": "integrations/evolution/evolution.client.js.map",
      "sha256": "47ebb570237451aa7d8fe156900336afeae7857caf6e6e5e297302b7166c4d4b"
    },
    {
      "path": "integrations/meta/meta.client.js",
      "sha256": "f30b8ca9327610aab072c690dda672d30676338bb24401571750f9231fab5a98"
    },
    {
      "path": "integrations/meta/meta.client.js.map",
      "sha256": "3fa37d0950e8b86459c8d80832f09eca5d508bf29e69832913314c2456ebcd1b"
    },
    {
      "path": "integrations/typebot/typebot.client.js",
      "sha256": "6617d233eba4994712cbfa0ff2b843f5fa553744af58182291d08deb4aa23980"
    },
    {
      "path": "integrations/typebot/typebot.client.js.map",
      "sha256": "723422a6f4f38c1d76ae50bb5fee8b2d97c0fc9a275db5d64adfac6bd77da4a9"
    },
    {
      "path": "main.js",
      "sha256": "4939123b00a86d0fb47ed2483ee13cb8ec0fbc374e565653c32724e920c2b9f0"
    },
    {
      "path": "main.js.map",
      "sha256": "d3471d745ee6e99a137b76043ba27cd743dc23ebb6b33e5eab854a1dc54be6ed"
    },
    {
      "path": "realtime/realtime.module.js",
      "sha256": "97bbba1dac2ec12e212252752b4668d308e75ecc1abab53562e6131907ae47a1"
    },
    {
      "path": "realtime/realtime.module.js.map",
      "sha256": "587e6fc05bd203f154986eb313bd999c8a1200dab11ee4760a5b7f0c24244678"
    },
    {
      "path": "realtime/realtime.service.js",
      "sha256": "584e1fdaf42605d4977f947746299626c90be7c9f4082ce66cbcba16a6c3b91d"
    },
    {
      "path": "realtime/realtime.service.js.map",
      "sha256": "467dbf83b7f870839cb14941868bd9d62f467c3cba209fde4c9280a4b3038cc0"
    },
    {
      "path": "rotinas/agendador.service.js",
      "sha256": "ac67fc82e61e4623ad4df1b1780e402ccbc0506c73364c10879a82a2c63bd646"
    },
    {
      "path": "rotinas/agendador.service.js.map",
      "sha256": "89253785a30b2339ff1f5aa102d25c8037337f0a98ff75c9a27566feaee1d8d5"
    },
    {
      "path": "rotinas/expurgo-de-webhook.rotina.js",
      "sha256": "c5b63269edbb6addfb2992b121d4fec9c86cd8ca6886eaf12e57ab36122a1031"
    },
    {
      "path": "rotinas/expurgo-de-webhook.rotina.js.map",
      "sha256": "ba156b796c84a40c9d9abd3ceb482a2a64ce8abeb8a24c171b68dffbdb384827"
    },
    {
      "path": "rotinas/rotina-periodica.js",
      "sha256": "b4308c664abf488ac88794d3c70beb53f85c2ded0d389cfe93db4b6fe05372aa"
    },
    {
      "path": "rotinas/rotina-periodica.js.map",
      "sha256": "79d8de9057bd81f38591141bd00cd03b7f3eb6707743326114b939e15a0cf87a"
    },
    {
      "path": "rotinas/rotinas.module.js",
      "sha256": "477fa6ea09780db6846e6c98b1ae5d3c49d0dd4d1da83d35a89b3d10cc44f787"
    },
    {
      "path": "rotinas/rotinas.module.js.map",
      "sha256": "2794be593c229ca6539fb72bda23e25f419f5e53402fa54b05c8611eca6e64b0"
    },
    {
      "path": "surfaces/bff/arquivos.controller.js",
      "sha256": "1611c531ab804d52bfaa9ee863d300f36de51b2440dfc9b8c7158ec4cb0627ac"
    },
    {
      "path": "surfaces/bff/arquivos.controller.js.map",
      "sha256": "a90116d7c2052cb30ce29b767b47d0c477177bc7c18a96b2e4b6d1a967661864"
    },
    {
      "path": "surfaces/bff/atividades.controller.js",
      "sha256": "e1a42ca0f779cd9b0c7cab5f06ef566dd36f601405316a1d8b30f80ce3126cfe"
    },
    {
      "path": "surfaces/bff/atividades.controller.js.map",
      "sha256": "35f6e290937064a113530f13275eda28185c2523a5ea4378edc490f9087beccd"
    },
    {
      "path": "surfaces/bff/auth.controller.js",
      "sha256": "487de6414692719df868e029dc9767d607807586d432df7061990256204bdbf0"
    },
    {
      "path": "surfaces/bff/auth.controller.js.map",
      "sha256": "16e1931fb9f197ebfb0d11272b3abdafb18458cd4aae2b18b55c0c030f10df73"
    },
    {
      "path": "surfaces/bff/bff.module.js",
      "sha256": "2db12a7c3febbab49dbda42ad5aa493b1a5461b0b7370ae8f04fc5848ea865cc"
    },
    {
      "path": "surfaces/bff/bff.module.js.map",
      "sha256": "9ef9c4bad62151efb3605d5eddb7202e4825e95775caf7c93d1cc0421429536b"
    },
    {
      "path": "surfaces/bff/channels.controller.js",
      "sha256": "4e4641c1c5371fd54d78889ed9525e616a0df633b55e246bef797cf46e906ff0"
    },
    {
      "path": "surfaces/bff/channels.controller.js.map",
      "sha256": "d371a6c76268b76b107b43853cfbb45ad2555aec5bdaa04db1ab27a3828152df"
    },
    {
      "path": "surfaces/bff/conversations.controller.js",
      "sha256": "8ccfbe252ce3fdb54ae0c7f820e88f5b0fb957e69a526e4819813e9269e8a3a9"
    },
    {
      "path": "surfaces/bff/conversations.controller.js.map",
      "sha256": "2769319b467fbcf28443fb05a554a52ffa2004b0e4f8573f2a7987e8008a7144"
    },
    {
      "path": "surfaces/bff/historico.controller.js",
      "sha256": "e982961367a40c41df247787c7f5d5aaa22b929374fc88028bfc4464c9b89c0f"
    },
    {
      "path": "surfaces/bff/historico.controller.js.map",
      "sha256": "d46e0b29e0a107e68df060a4c311beb83dc0e285ec956677ba2e0b68501ae4b5"
    },
    {
      "path": "surfaces/bff/integracao.controller.js",
      "sha256": "431e5820de4421360ce679a9a748b9d3f500999a1474c2ef096635ff94b460f7"
    },
    {
      "path": "surfaces/bff/integracao.controller.js.map",
      "sha256": "3703f5815637d4c9f3d4ee72df6d3c9a9da967620d09aac93119485e8ea66891"
    },
    {
      "path": "surfaces/bff/me.controller.js",
      "sha256": "c9a3bed3ed8db1d1a12f745fd97c2f069f0d5773dcbe7ca1231a07029a3f2121"
    },
    {
      "path": "surfaces/bff/me.controller.js.map",
      "sha256": "3f6474a5d8cd01d7fe793fc5df4ee3d97ce9a94bf6592ef6452adcebccc7f09d"
    },
    {
      "path": "surfaces/bff/onboarding.controller.js",
      "sha256": "835092e537421aa6c666fa60ec1e38422e6b502f87e93c6d30a5870bb18e2caf"
    },
    {
      "path": "surfaces/bff/onboarding.controller.js.map",
      "sha256": "1e235e3b3ed6aad63a0796fe267f089b409fd9717df4bf3f51635d0016ec711d"
    },
    {
      "path": "surfaces/bff/painel.controller.js",
      "sha256": "1e46acc3988aa590790118b4fbd0adf77b7a91bc44096f8e9627b823ac3cdf83"
    },
    {
      "path": "surfaces/bff/painel.controller.js.map",
      "sha256": "26a638493c43fe3a5b4b612e96454ecbd46c1e8ef2d19751861ebb9ff9a18775"
    },
    {
      "path": "surfaces/bff/session.middleware.js",
      "sha256": "fc5af440f1309c0925e430cf490bd32ca5ddbdf96d8d0736ffbe6af541d27e67"
    },
    {
      "path": "surfaces/bff/session.middleware.js.map",
      "sha256": "4a172b78eeecffbecdf47b5f54bf92ed16fe93b4daadd59b0a03c86206763c41"
    },
    {
      "path": "surfaces/bff/setores.controller.js",
      "sha256": "cdf8e88792b0908cdca31d1b9a36283fa7971bedd021bc3ebeb9951c28cbd038"
    },
    {
      "path": "surfaces/bff/setores.controller.js.map",
      "sha256": "4960b4cb8e2ef36100f14be5dd9623c152039d5172bf44eaa7c1b4b390064205"
    },
    {
      "path": "surfaces/bff/usuarios.controller.js",
      "sha256": "9af33d16920d3bad25b9b74819b29013a438e0d92080ca772f3b7510299b4aa2"
    },
    {
      "path": "surfaces/bff/usuarios.controller.js.map",
      "sha256": "bc689d7705c8e8f957ef06102d24f4515a13d8e1851d27f7cac73e95fff05920"
    },
    {
      "path": "surfaces/internal/internal.module.js",
      "sha256": "c92b694a24980f6b2b370174de2004ebcfc102949e25dc814c6b6c4a636d9689"
    },
    {
      "path": "surfaces/internal/internal.module.js.map",
      "sha256": "e2a4cf18bf19eaf05b995543bd037509ffb5283dbb791b569840a9850ab33f6f"
    },
    {
      "path": "surfaces/internal/mantenedoras.controller.js",
      "sha256": "e45802cd4ffff98bf828560878ee6611123f3a45344c6f2152e2ca9ecb39210c"
    },
    {
      "path": "surfaces/internal/mantenedoras.controller.js.map",
      "sha256": "da1dc19549b3a3441d0ce92469dcaabb6e6098e9650182a5f54081c3ffdcdc35"
    },
    {
      "path": "surfaces/internal/service-credential.middleware.js",
      "sha256": "2084df02fec5029971c695e61b6add89cbf76bf9806a6da56a32194a171d0274"
    },
    {
      "path": "surfaces/internal/service-credential.middleware.js.map",
      "sha256": "cc6d9edb635d5b900bd73bb4b2213b6bbfeda116902f2b1fa092cab09091eae3"
    },
    {
      "path": "surfaces/public/api-key.middleware.js",
      "sha256": "51c1ba5b526dbeac89707d3718f47cedc11c6c72d32f7224fc587ecd40e04465"
    },
    {
      "path": "surfaces/public/api-key.middleware.js.map",
      "sha256": "9fea00ba3bdbedf267e127603196a558f1f943bdb057a064e6ec96fad746a3de"
    },
    {
      "path": "surfaces/public/conversations.controller.js",
      "sha256": "c1b62747445c0e7608d8d9f0b6292d2b8d17fd9163e062ff2ce572bd290591a2"
    },
    {
      "path": "surfaces/public/conversations.controller.js.map",
      "sha256": "e08ca8d6202135f9b5f02e34b8d0e09533236f005ff9cb8d8e50187cd0f9b440"
    },
    {
      "path": "surfaces/public/public.module.js",
      "sha256": "a793879d1bd1d3124eeb114b0bcf360b64376b3cede6a5c195cb091876fecaf2"
    },
    {
      "path": "surfaces/public/public.module.js.map",
      "sha256": "48ff48355c8e2255d3f0bf2cfc88170ecd836a688d91c12357f938011128a15d"
    },
    {
      "path": "surfaces/webhooks/evolution.controller.js",
      "sha256": "cae5cc1c2d450fbfcd4a53f7dc0533e12331b8d128ce29481ab4b339682c519a"
    },
    {
      "path": "surfaces/webhooks/evolution.controller.js.map",
      "sha256": "98d074ad8fc18cd77710480b6e2c759f2d101ec7568f109279163c0a3fe4ea96"
    },
    {
      "path": "surfaces/webhooks/meta.controller.js",
      "sha256": "6b7c5626a5b26df2c46569b57a2dc6366768d70bfaac9362ac77fbd824eff2a7"
    },
    {
      "path": "surfaces/webhooks/meta.controller.js.map",
      "sha256": "aad8612ff69766ad3b0b4a24628110699380954fc30c2eb52c1a5a4f92f7789f"
    },
    {
      "path": "surfaces/webhooks/webhooks.module.js",
      "sha256": "9a4733bab8a15183b73388e634b5b268264c760aab3eb4506c653ea0772ca38f"
    },
    {
      "path": "surfaces/webhooks/webhooks.module.js.map",
      "sha256": "84b554deba5b1a2c5caf1a02e275d705eb6411720618cf429a9ee9113afe44cb"
    },
    {
      "path": "tsconfig.build.tsbuildinfo",
      "sha256": "e3fc9e379512559037a5c89d767290a4c84db13fd7668a56499b596a282649ce"
    }
  ],
  "webDistManifest": [
    {
      "path": "assets/index-DSeTAho8.js",
      "sha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8"
    },
    {
      "path": "assets/index-wuzy3kMN.css",
      "sha256": "38f979314555cda8b834189ed5c64826bbc309e294091c9f5c54ee5f8bd2aadd"
    },
    {
      "path": "config.js",
      "sha256": "1ad17fefa4173ed847cabd79e7fdc1b262fa19ea4ff33c3ef435e141275fb532"
    },
    {
      "path": "index.html",
      "sha256": "610b0638ae994cde6f35d2bff22c0a4a94c213b0da9a5e67f94680436670a538"
    }
  ]
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-canonical-after-mutation.log

```
[33mThe CJS build of Vite's Node API is deprecated. See https://vite.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.[39m

 RUN  v2.1.9 /workspace/api-app

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":1,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":83,"dezIncrementosMs":42,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":2,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":55,"dezIncrementosMs":24,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":3,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":53,"dezIncrementosMs":26,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

 ✓ test/atendimento.e2e-spec.ts (19 tests | 18 skipped) 826ms
   ✓ atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes 637ms

 Test Files  1 passed (1)
      Tests  1 passed | 18 skipped (19)
   Start at  03:23:25
   Duration  8.66s (transform 6.07s, setup 45ms, collect 7.55s, tests 826ms, environment 0ms, prepare 75ms)

npm notice
npm notice New major version of npm available! 10.9.9 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-mutation-control.log

```

 RUN  v2.1.9 /workspace/api-app

 ❯ test/atendimento.e2e-spec.ts (19 tests | 1 failed | 18 skipped) 701ms
   × atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes 502ms
     → expected +0 to be 10 // Object.is equality

 Test Files  1 failed (1)
      Tests  1 failed | 18 skipped (19)
   Start at  03:22:45
   Duration  8.45s (transform 5.90s, setup 45ms, collect 7.43s, tests 701ms, environment 0ms, prepare 87ms)

[33mThe CJS build of Vite's Node API is deprecated. See https://vite.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.[39m
⎯⎯⎯⎯⎯⎯⎯ Failed Tests 1 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
AssertionError: expected +0 to be 10 // Object.is equality

- Expected
+ Received

- 10
+ 0

 ❯ test/atendimento.e2e-spec.ts:464:30
    462|           expect(resposta.status).toBe(200);
    463|           const persistido = (await prisma.conversation.findUniqueOrTh…
    464|           expect(persistido).toBe(10);
       |                              ^
    465|           console.info(JSON.stringify({
    466|             prova: 'BCI_ACK_COM_SELECT_BLOQUEADO', lote: lote + 1,

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/1]⎯

npm notice
npm notice New major version of npm available! 10.9.9 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-source-restored.sha256

```
93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e  api-app/src/domain/inbox/conversations.service.ts

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/browser-runtime-authority.txt

```
v22.23.3

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/diff-frozen.json

```
{
  "blocked": false,
  "context": {
    "actual_change_count": 60,
    "contract_repository_count": 3,
    "expected_change_count": 60,
    "forbidden_change_count": 0,
    "repo_root": "/mnt/c/unifast/leadshug/leadshug_now_docker",
    "repositories": {
      "api": {
        "actual_change_count": 7,
        "baseline_commit": "5db3fbe2043428749895fc3ff6441e9457467dd0",
        "path": "/mnt/c/unifast/leadshug/leadshug_now_docker/api-app"
      },
      "foundation": {
        "actual_change_count": 44,
        "baseline_commit": "40828a20f2d6c3a1443e7ee132f42483840d6abb",
        "path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation"
      },
      "web": {
        "actual_change_count": 9,
        "baseline_commit": "6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9",
        "path": "/mnt/c/unifast/leadshug/leadshug_now_docker/web-app"
      }
    },
    "todo_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md",
    "unclassified_change_count": 0
  },
  "violations": []
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/executor-final-summary.json

```
{
  "task": "ST-ATT-01 inbox timeline pagination executor evidence",
  "capturedAtUtc": "2026-10-15T03:40:28.312Z",
  "status": "source frozen for independent review; no commit/push",
  "runtimeAndDatabase": {
    "node": "v22.23.3",
    "postgres": "PostgreSQL 16.14",
    "database": "leadshug_timeline_20261014",
    "migrations": 17,
    "endpoint": "timeline-postgres:5432 (credentials redacted)",
    "disposable": true
  },
  "source": {
    "api": {
      "branch": "feature/inbox-timeline-pagination",
      "head": "5db3fbe2043428749895fc3ff6441e9457467dd0",
      "diffSha256": "d3d84c015c24348b1dbc885a90d66ff8f88eadf35a75b0a256a38c3f1230708b",
      "manifestSha256": "4722038d60e7b73ac3dc04d2adbbd7af9f2a71fda6d2f9f59c87214ca3d70125",
      "files": [
        {
          "path": "src/domain/inbox/conversations.service.ts",
          "sha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.spec.ts",
          "sha256": "a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.ts",
          "sha256": "d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af"
        },
        {
          "path": "src/surfaces/bff/conversations.controller.ts",
          "sha256": "0b5c46a78aafd8085b609ad711bcdb7626263094f434240f37b8700f20291565"
        },
        {
          "path": "test/atendimento.e2e-spec.ts",
          "sha256": "1bb4acb19fc522b397424b319ab04563e3608605dcfe307970eecdd0d464b5b8"
        },
        {
          "path": "test/browser-server.cjs",
          "sha256": "031e9d1e282603c098c4bb594fb13a08ab2bc2f301c9a3ebb5a6362cae6fe42b"
        },
        {
          "path": "test/timeline-fixtures.cjs",
          "sha256": "bc15f1758ec574dec1f1c66330e0cc9804705e103fb5abab7f9015e5e8563f9f"
        }
      ]
    },
    "web": {
      "branch": "feature/inbox-timeline-pagination",
      "head": "6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9",
      "diffSha256": "5b716dd27f498bfc11f5b7910922ce32fd628973e6039306a9b6159c7e9097d1",
      "manifestSha256": "1dbc5fd0d5cea01c31c4779c40aca4fe6d354623d8321773fef56da234d6c384",
      "files": [
        {
          "path": "e2e/timeline-freshness.ts",
          "sha256": "ad41153df34c53f6674325b72887e701259ba7a8e752afd38ff4cdd8728c4cd0"
        },
        {
          "path": "e2e/timeline.spec.ts",
          "sha256": "266f63fc22a5de3482952b588d463388a048f2d98d13fa06a8107f298779a552"
        },
        {
          "path": "playwright.config.ts",
          "sha256": "d69c084d15cfef29ad23851036cb90309c60aa7a7b16c6810e3ae9b0adbbdd98"
        },
        {
          "path": "src/api.ts",
          "sha256": "87ba36bd21518725ba0e42221030d77b723144ef8d0581fddb2d9102233e7db2"
        },
        {
          "path": "src/telas/Inbox.tsx",
          "sha256": "8076cfabb46c92bc877b4975d70fca4b5d5928babc630f0683c3ace92172c945"
        },
        {
          "path": "src/tempoReal.spec.ts",
          "sha256": "378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5"
        },
        {
          "path": "src/tempoReal.ts",
          "sha256": "118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf"
        },
        {
          "path": "src/timeline.test.ts",
          "sha256": "16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4"
        },
        {
          "path": "src/timeline.ts",
          "sha256": "0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311"
        }
      ]
    },
    "manifestRecheckAfterRuns": "all 7 API and 9 Web entries match full and FRC attestations; zero mismatches",
    "gitDiffCheck": "passes with cr-at-eol whitespace configuration; project files use CRLF"
  },
  "buildFreshness": {
    "fullRunId": "full-final31-20261015",
    "capturedAtUtc": "2026-10-15T03:39:29.661Z",
    "frcRunId": "frc-strong-final-20261015",
    "frcCapturedAtUtc": "2026-10-15T03:40:28.312Z",
    "apiHealth": 200,
    "fixtureHealth": 200,
    "preview": 200,
    "servedBundle": "/assets/index-DSeTAho8.js",
    "servedBundleSha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8",
    "distBundleSha256": "549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8",
    "sameServedAssetForFrc": true,
    "fullAttestation": "attestation-browser-full-final31-20261015.json",
    "frcAttestation": "attestation-browser-frc-strong-final-20261015.json"
  },
  "apiAuthority": {
    "command": "npm run prisma:generate && npm run lint && npm run build && npm test && npm run test:e2e",
    "exitCode": 0,
    "unitTests": {
      "files": 17,
      "passed": 115,
      "failed": 0,
      "stdoutPersisted": false
    },
    "e2e": {
      "files": 20,
      "passed": 224,
      "failed": 0,
      "durationSeconds": 111.92,
      "log": "api-e2e-authority.log"
    },
    "runtimeLog": "api-runtime-authority.txt",
    "note": "generate/lint/build/unit stdout was observed in executor output but not separately persisted; detailed final E2E log retained. No rerun after Web-only edits."
  },
  "webAuthority": {
    "unit": {
      "command": "npm test",
      "exitCode": 0,
      "files": 3,
      "passed": 20,
      "failed": 0
    },
    "browser": {
      "command": "npm run test:tela",
      "exitCode": 0,
      "passed": 31,
      "failed": 0,
      "durationSeconds": 48.6,
      "log": "web-authority-final31.log"
    },
    "frc": {
      "command": "npx playwright test e2e/timeline.spec.ts --grep=\"preserva o piso T\" --repeat-each=3",
      "exitCode": 0,
      "passed": 3,
      "failed": 0,
      "realWebhookTriggersPerRepeat": 10,
      "log": "web-frc-strong-final-3x.log"
    },
    "pollTargeted": {
      "command": "npx playwright test e2e/timeline.spec.ts --grep=\"poll retoma uma rodada pendente\"",
      "exitCode": 0,
      "passed": 1,
      "log": "web-poll-targeted.log"
    },
    "logoutTargeted": {
      "repeatEach": 5,
      "passed": 5,
      "exitCode": 0,
      "log": "web-logout-lifecycle-5x.log"
    }
  },
  "bci": {
    "fullApiE2eIncludesThreeRealPostgresBatches": true,
    "invariant": "10 unread increments after atomic ack while Message page SELECT waits on a lock; unread stays 10 before/after page; later real inbound makes 11",
    "negativeControl": "temporarily moved ack after findMany; targeted test failed expected 10 vs actual 0; restored exact saved bytes; canonical focused test passed",
    "negativeControlLog": "bci-mutation-control.log",
    "canonicalLog": "bci-canonical-after-mutation.log",
    "restoredServiceSha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
  },
  "eps": {
    "conversationRows": 20382,
    "largestEqualTimestampGroup": 1000,
    "recent": {
      "executionMs": 1.094,
      "sharedBuffersHit": 37
    },
    "deepCursorOffset": 10000,
    "deep": {
      "executionMs": 3.442,
      "sharedBuffersHit": 357,
      "rowsRemovedByFilter": 10001
    },
    "largeTieCursorOffset": 500,
    "largeTie": {
      "executionMs": 0.85,
      "sharedBuffersHit": 37,
      "rowsRemovedByFilter": 501
    },
    "candidateIndexTrial": {
      "index": "(conversation_id, created_at DESC, id DESC)",
      "executionMs": 3.942,
      "sharedBuffersHit": 9832,
      "rowsRemovedByFilter": 10001,
      "decision": "no index or migration; trial index removed; existing index retains deep scan residual"
    },
    "sql": "explain-timeline-exact.sql",
    "log": "explain-timeline-exact.log",
    "candidateSql": "explain-index-trial.sql",
    "candidateLog": "explain-index-trial.log"
  },
  "rlsReadSample": {
    "requests": 30,
    "concurrency": 5,
    "batches": 6,
    "status200": 30,
    "errors": 0,
    "messagesPerResponse": 50,
    "p50Ms": 23.36,
    "p95Ms": 64.26,
    "maxMs": 68.5,
    "foreignConversationWithMalformedLimitStatus": 404,
    "unreadBefore": 7,
    "unreadAfter": 7,
    "messagesBefore": 251,
    "messagesAfter": 251,
    "script": "rls-read-sample.mjs",
    "log": "rls-read-sample.log",
    "scopeNote": "foreign request used ?limite=invalid; raw JSON label says malformedCursor but malformed field is limite",
    "productionSloClaim": false
  },
  "historicalDiagnostics": {
    "invalidEarlierApiRun": "220/222 overlapped Browser cleanup/seed; not authoritative; later clean run 224/224 is authority",
    "earlierBrowserRun": "29/30 with initial WebSocket logout handshake issue; targeted logout 5/5 and final 31/31 pass after stable Inbox socket lifecycle",
    "incompleteFrcRepeat": "all-case repeat stopped at 20/30; not evidence; final strong FRC passed 3/3"
  },
  "cleanupAndResources": {
    "generatedWebTestResultsRemoved": true,
    "databaseContainer": "leadshug-timeline-postgres-20261014 remains running for reviewer",
    "dependencyVolumes": [
      "leadshug-timeline-api-node-modules-20261014",
      "leadshug-timeline-web-node-modules-20261014"
    ],
    "noOtherTimelineRunnerContainers": true,
    "sourceChangesFrozen": true,
    "disposableProbeRowsKeptForReview": true
  },
  "logSha256": {
    "api-e2e-authority.log": "b508ca43e5157fea8fbf6951b2bd2b7c2b860ebde3e4c2dca1971094436317db",
    "web-authority-final31.log": "e3a38d01e61fc232878774b78490184c100a9828ce5fde4d2a44140d6d8df482",
    "web-frc-strong-final-3x.log": "8cd7c693430ccd215c495b438ae4c39d0824dc0487dd11e3cf279bbdda9572f4",
    "web-poll-targeted.log": "14a49953f93214f078e30f4f449423a01fb2994188e8b60878b0b0580c8978df",
    "web-logout-lifecycle-5x.log": "4d21a8d1f11eba483a316fd5d15c4a1fc2c35ffca728433b9e00d7edb21a4047",
    "bci-mutation-control.log": "0c2b211c2078240a09519eeff76f2a32a358135090e32df1bb871c619d4e327d",
    "bci-canonical-after-mutation.log": "90fe5dd92cf6098fc7375258ba7452a29c4d74255d10fafd2efcc4c8b4866b4c",
    "explain-timeline-exact.sql": "30b7477601cd109ffd3af7d38e9df1e5fbf8a6af56bf90cf52a42f4779ee0cb8",
    "explain-timeline-exact.log": "6e346b5b0609de7f347481fb2b4eccc93e4ddf8b41219bb1348fbf169af9b9b6",
    "explain-index-trial.sql": "8ac4343ac0633b5b1535e171ec7466e58c5c6488d1de8abc516b15f6e6b914a3",
    "explain-index-trial.log": "43251847c09a71819a11aa135c8710b72a3eb4af2188f07bd3c071bfa980171c",
    "rls-read-sample.mjs": "d59fa9f53ffeb97aec02b32ccf91584868f1e2b1ebcd644278f00881ae3a3321",
    "rls-read-sample.log": "5b68b1b5f450153c7fa6c36c277aa19d5846860f63ef8124a1eaeb32dd3941fc"
  }
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-index-trial.log

```
CREATE INDEX
ANALYZE
=== EXACT_DEEP_CURSOR_WITH_CANDIDATE_INDEX ===
                                                                                                         QUERY PLAN                                                                                                         
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=0.41..14.33 rows=51 width=103) (actual time=3.875..3.913 rows=51 loops=1)
   Buffers: shared hit=9832
   ->  Index Scan using messages_conversation_created_at_id_timeline_trial_idx on messages  (cost=0.41..3173.07 rows=11630 width=103) (actual time=3.875..3.909 rows=51 loops=1)
         Index Cond: (conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673'::text)
         Filter: ((created_at < '2026-10-15 03:34:03.183+00'::timestamp with time zone) OR ((created_at = '2026-10-15 03:34:03.183+00'::timestamp with time zone) AND (id < 'fffb7cf1-cc91-4748-b3b1-d2d91d056f8f'::text)))
         Rows Removed by Filter: 10001
         Buffers: shared hit=9832
 Planning:
   Buffers: shared hit=29
 Planning Time: 0.353 ms
 Execution Time: 3.942 ms
(11 rows)


```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-index-trial.sql

```
\set ON_ERROR_STOP on
CREATE INDEX messages_conversation_created_at_id_timeline_trial_idx ON messages (conversation_id, created_at DESC, id DESC);
ANALYZE messages;
SELECT created_at AS anchor_created_at, id AS anchor_id FROM messages WHERE conversation_id='f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC OFFSET 10000 LIMIT 1 \gset
\echo === EXACT_DEEP_CURSOR_WITH_CANDIDATE_INDEX ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' AND (created_at < :'anchor_created_at'::timestamptz OR (created_at = :'anchor_created_at'::timestamptz AND id < :'anchor_id'::text)) ORDER BY created_at DESC, id DESC LIMIT 51;

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-timeline-exact.log

```
DROP INDEX
ANALYZE
=== RECENT production-equivalent, conversation_id + order + limit+1 ===
                                                                                    QUERY PLAN                                                                                     
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=3.51..11.09 rows=51 width=103) (actual time=0.976..0.984 rows=51 loops=1)
   Buffers: shared hit=37
   ->  Incremental Sort  (cost=3.51..3033.76 rows=20382 width=103) (actual time=0.975..0.978 rows=51 loops=1)
         Sort Key: created_at DESC, id DESC
         Presorted Key: created_at
         Full-sort Groups: 1  Sort Method: quicksort  Average Memory: 33kB  Peak Memory: 33kB
         Pre-sorted Groups: 1  Sort Method: top-N heapsort  Average Memory: 35kB  Peak Memory: 35kB
         Buffers: shared hit=37
         ->  Index Scan Backward using messages_conversation_id_created_at_idx on messages  (cost=0.29..2296.08 rows=20382 width=103) (actual time=0.035..0.429 rows=1001 loops=1)
               Index Cond: (conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673'::text)
               Buffers: shared hit=37
 Planning:
   Buffers: shared hit=17
 Planning Time: 0.383 ms
 Execution Time: 1.094 ms
(15 rows)

=== DEEP production-equivalent cursor constants ===
                                                                                                            QUERY PLAN                                                                                                            
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=3.40..15.79 rows=51 width=103) (actual time=3.375..3.381 rows=51 loops=1)
   Buffers: shared hit=357
   ->  Incremental Sort  (cost=3.40..2830.16 rows=11630 width=103) (actual time=3.374..3.377 rows=51 loops=1)
         Sort Key: created_at DESC, id DESC
         Presorted Key: created_at
         Full-sort Groups: 1  Sort Method: quicksort  Average Memory: 33kB  Peak Memory: 33kB
         Pre-sorted Groups: 1  Sort Method: top-N heapsort  Average Memory: 34kB  Peak Memory: 34kB
         Buffers: shared hit=357
         ->  Index Scan Backward using messages_conversation_id_created_at_idx on messages  (cost=0.29..2448.94 rows=11630 width=103) (actual time=2.611..2.974 rows=1000 loops=1)
               Index Cond: (conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673'::text)
               Filter: ((created_at < '2026-10-15 03:34:03.183+00'::timestamp with time zone) OR ((created_at = '2026-10-15 03:34:03.183+00'::timestamp with time zone) AND (id < 'fffb7cf1-cc91-4748-b3b1-d2d91d056f8f'::text)))
               Rows Removed by Filter: 10001
               Buffers: shared hit=357
 Planning:
   Buffers: shared hit=13
 Planning Time: 0.313 ms
 Execution Time: 3.442 ms
(17 rows)

=== LARGE_TIMESTAMP_TIE production-equivalent cursor constants ===
                                                                                                            QUERY PLAN                                                                                                            
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=3.66..11.86 rows=51 width=103) (actual time=0.787..0.793 rows=51 loops=1)
   Buffers: shared hit=37
   ->  Incremental Sort  (cost=3.66..3152.18 rows=19570 width=103) (actual time=0.786..0.789 rows=51 loops=1)
         Sort Key: created_at DESC, id DESC
         Presorted Key: created_at
         Full-sort Groups: 1  Sort Method: quicksort  Average Memory: 33kB  Peak Memory: 33kB
         Pre-sorted Groups: 1  Sort Method: top-N heapsort  Average Memory: 34kB  Peak Memory: 34kB
         Buffers: shared hit=37
         ->  Index Scan Backward using messages_conversation_id_created_at_idx on messages  (cost=0.29..2448.94 rows=19570 width=103) (actual time=0.040..0.479 rows=500 loops=1)
               Index Cond: (conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673'::text)
               Filter: ((created_at < '2026-10-15 03:34:13.183+00'::timestamp with time zone) OR ((created_at = '2026-10-15 03:34:13.183+00'::timestamp with time zone) AND (id < '82e12262-6e30-4bd3-affc-47df29d4a9c5'::text)))
               Rows Removed by Filter: 501
               Buffers: shared hit=37
 Planning Time: 0.132 ms
 Execution Time: 0.850 ms
(15 rows)


```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-timeline-exact.sql

```
\set ON_ERROR_STOP on
DROP INDEX IF EXISTS messages_conversation_created_at_id_timeline_trial_idx;
ANALYZE messages;
SELECT created_at AS deep_created_at, id AS deep_id FROM messages WHERE conversation_id='f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC OFFSET 10000 LIMIT 1 \gset
SELECT created_at AS tie_created_at, id AS tie_id FROM messages WHERE conversation_id='f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC OFFSET 500 LIMIT 1 \gset
\echo === RECENT production-equivalent, conversation_id + order + limit+1 ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC LIMIT 51;
\echo === DEEP production-equivalent cursor constants ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' AND (created_at < :'deep_created_at'::timestamptz OR (created_at = :'deep_created_at'::timestamptz AND id < :'deep_id'::text)) ORDER BY created_at DESC, id DESC LIMIT 51;
\echo === LARGE_TIMESTAMP_TIE production-equivalent cursor constants ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' AND (created_at < :'tie_created_at'::timestamptz OR (created_at = :'tie_created_at'::timestamptz AND id < :'tie_id'::text)) ORDER BY created_at DESC, id DESC LIMIT 51;

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rls-read-sample.log

```
v22.23.3
{
  "runId": "rls-read-stage1-20261015",
  "sample": {
    "requests": 30,
    "concurrency": 5,
    "batches": 6,
    "statusCounts": {
      "200": 30,
      "errors": 0
    },
    "p50Ms": 23.36,
    "p95Ms": 64.26,
    "maxMs": 68.5,
    "messagesPerResponse": 50,
    "hasPrevious": true
  },
  "scope": {
    "accessibleConversation": "200 x30",
    "foreignConversationWithMalformedCursor": 404,
    "unreadBefore": 7,
    "unreadAfter": 7,
    "messagesBefore": 251,
    "messagesAfter": 251
  },
  "conclusion": "small disposable one-stage read-neutral sample; no production SLO inferred"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rls-read-sample.mjs

```
import { createRequire } from 'node:module';
import { performance } from 'node:perf_hooks';
const requireFromApi = createRequire('/workspace/api-app/package.json');
const requireFromWeb = createRequire('/workspace/web-app/package.json');
const { PrismaClient } = requireFromApi('@prisma/client');
const { request } = requireFromWeb('@playwright/test');
const base = 'http://127.0.0.1:3100';
const fixtureBase = 'http://127.0.0.1:3101';
const product = await request.newContext({ baseURL: base });
const fixtureApi = await request.newContext({ baseURL: fixtureBase });
const prisma = new PrismaClient({ datasources: { db: { url: process.env.LEADSHUG_E2E_DATABASE_URL } } });
try {
  const seededResponse = await fixtureApi.post('/seed', { data: { count: 251, tied: true } });
  if (seededResponse.status() !== 201) throw new Error(`seed falhou: ${seededResponse.status()}`);
  const seeded = await seededResponse.json();
  const foreignResponse = await fixtureApi.post('/seed', { data: { count: 2 } });
  if (foreignResponse.status() !== 201) throw new Error(`seed estrangeira falhou: ${foreignResponse.status()}`);
  const foreign = await foreignResponse.json();
  await prisma.conversation.update({ where: { id: seeded.conversationId }, data: { unreadCount: 7 } });
  const login = await product.post('/api/bff/auth/login', { data: { email: seeded.email, senha: seeded.password }, headers: { origin: 'http://127.0.0.1:4173', 'x-requested-with': 'XMLHttpRequest' } });
  if (login.status() !== 200) throw new Error(`login falhou: ${login.status()} ${(await login.text()).slice(0, 300)}`);
  const before = await (await fixtureApi.get(`/audit?conversationId=${seeded.conversationId}`)).json();
  const accessUrl = `/api/bff/conversations/${seeded.conversationId}/messages?limite=50&marcarLida=false`;
  const timings = [];
  const statuses = [];
  for (let batch = 0; batch < 6; batch += 1) {
    const results = await Promise.all(Array.from({ length: 5 }, async () => {
      const started = performance.now();
      const response = await product.get(accessUrl);
      const elapsedMs = performance.now() - started;
      const body = await response.json();
      return { status: response.status(), elapsedMs, count: body.messages?.length, hasPrevious: body.paginacao?.temAnteriores };
    }));
    for (const result of results) { statuses.push(result.status); timings.push(result.elapsedMs); if (result.status !== 200 || result.count !== 50 || result.hasPrevious !== true) throw new Error(`resposta inesperada: ${JSON.stringify(result)}`); }
  }
  const denied = await product.get(`/api/bff/conversations/${foreign.conversationId}/messages?limite=invalid`);
  const after = await (await fixtureApi.get(`/audit?conversationId=${seeded.conversationId}`)).json();
  if (denied.status() !== 404) throw new Error(`conversa sem grant devia ocultar-se como404; recebeu ${denied.status()}`);
  if (before.unreadCount !== 7 || after.unreadCount !== 7 || before.messages.length !== after.messages.length) throw new Error('leitura alterou estado ou histórico.');
  const sorted = timings.toSorted((a, b) => a - b);
  const percentile = (p) => Number(sorted[Math.ceil(p * sorted.length) - 1].toFixed(2));
  console.log(JSON.stringify({ runId: 'rls-read-stage1-20261015', sample: { requests: timings.length, concurrency: 5, batches: 6, statusCounts: { '200': statuses.filter((x) => x === 200).length, errors: statuses.filter((x) => x !== 200).length }, p50Ms: percentile(0.50), p95Ms: percentile(0.95), maxMs: Number(Math.max(...timings).toFixed(2)), messagesPerResponse: 50, hasPrevious: true }, scope: { accessibleConversation: '200 x30', foreignConversationWithMalformedCursor: denied.status(), unreadBefore: before.unreadCount, unreadAfter: after.unreadCount, messagesBefore: before.messages.length, messagesAfter: after.messages.length }, conclusion: 'small disposable one-stage read-neutral sample; no production SLO inferred' }, null, 2));
} finally {
  await prisma.$disconnect();
  await product.dispose();
  await fixtureApi.dispose();
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/test-quality-static-api.log

```
Test Quality Audit
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/api-app
Outcome heuristic: medium

Scan paths:
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/atendimento.e2e-spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/browser-server.cjs
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/timeline-fixtures.cjs
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/src/domain/inbox/timeline-pagination.spec.ts

Hard bypass markers:
  - none

Test-only support route usage:
  - none

Auth shortcut hints:
  - none

Status-only assertion hints:
  - 462:          expect(resposta.status).toBe(200);

No-exception-only assertion hints:
  - none

Ambient subject fallback hints:
  - none

DI override hints:
  - none

Mock / fallback hints:
  - none

Counts: hard_bypass=0 test_support=0 auth_shortcut=0 status_only=1 no_exception_only=0 ambient_subject_fallback=0 di_override=0 mock_hint=0

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/test-quality-static-web.log

```
Test Quality Audit
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/web-app
Outcome heuristic: medium

Scan paths:
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline-freshness.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/tempoReal.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/timeline.test.ts

Hard bypass markers:
  - none

Test-only support route usage:
  - none

Auth shortcut hints:
  - none

Status-only assertion hints:
  - 9:  expect(response.status()).toBe(201);
  - 41:  expect(response.status()).toBe(200);
  - 43:  expect(webhook.status).toBe(200);
  - 115:    expect(burst.status()).toBe(201);
  - 137:    expect(burst.status()).toBe(201);
  - 158:    expect(burst.status()).toBe(201);

No-exception-only assertion hints:
  - none

Ambient subject fallback hints:
  - 73:    completedMigrations = Number(rows[0]?.count ?? 0);

DI override hints:
  - none

Mock / fallback hints:
  - none

Counts: hard_bypass=0 test_support=0 auth_shortcut=0 status_only=6 no_exception_only=0 ambient_subject_fallback=1 di_override=0 mock_hint=0

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-final31.log

```
v22.23.3

> @leadshug/web@0.1.0 test
> vitest run


 RUN  v2.1.9 /workspace/web-app

 ✓ src/timeline.test.ts (2 tests) 3ms
 ✓ src/tempoReal.spec.ts (6 tests) 7ms
 ✓ src/api.spec.ts (12 tests) 47ms

 Test Files  3 passed (3)
      Tests  20 passed (20)
   Start at  03:39:11
   Duration  591ms (transform 289ms, setup 0ms, collect 402ms, tests 57ms, environment 1ms, prepare 268ms)

npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

> @leadshug/web@0.1.0 test:tela
> npm run build && playwright test


> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-DSeTAho8.js   223.33 kB │ gzip: 69.58 kB
✓ built in 1.40s
[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 31 tests using 1 worker

  ✓   1 e2e/telas.spec.ts:78:3 › as telas, no navegador › sem sessão, qualquer URL leva ao login (231ms)
  ✓   2 e2e/telas.spec.ts:84:3 › as telas, no navegador › entrar leva de volta para a página que se queria abrir (1.0s)
  ✓   3 e2e/telas.spec.ts:96:3 › as telas, no navegador › conta nova cai no wizard, e a Revisão diz qual é o próximo passo (969ms)
  ✓   4 e2e/telas.spec.ts:138:3 › as telas, no navegador › toda tela do menu abre sem quebrar (1.6s)
  ✓   5 e2e/telas.spec.ts:167:3 › as telas, no navegador › a paleta é a do desenho, e o tema segue a marca da conta (875ms)
  ✓   6 e2e/telas.spec.ts:191:3 › as telas, no navegador › os grupos do menu retraem, e a escolha sobrevive à navegação (1.0s)
  ✓   7 e2e/telas.spec.ts:209:3 › as telas, no navegador › o tema é escolha de quem olha, e persiste (945ms)
  ✓   8 e2e/telas.spec.ts:227:3 › as telas, no navegador › Meu perfil abre pelo rodapé e salva o próprio nome (1.0s)
  ✓   9 e2e/telas.spec.ts:246:3 › as telas, no navegador › a foto de perfil sobe, e a recusa do servidor aparece na tela (985ms)
  ✓  10 e2e/telas.spec.ts:276:3 › as telas, no navegador › a barra lateral tem os três grupos do desenho (787ms)
  ✓  11 e2e/telas.spec.ts:290:3 › as telas, no navegador › Setores abre com o Geral, e o Histórico já mostra o que aconteceu (878ms)
  ✓  12 e2e/telas.spec.ts:302:3 › as telas, no navegador › a inbox abre, com o número no seletor e sem conversa nenhuma (980ms)
  ✓  13 e2e/telas.spec.ts:319:3 › as telas, no navegador › Pessoas abre, lista quem já existe e oferece os papéis que existem (1.1s)
  ✓  14 e2e/telas.spec.ts:338:3 › as telas, no navegador › adicionar uma pessoa e conceder um setor a ela (1.1s)
  ✓  15 e2e/telas.spec.ts:357:3 › as telas, no navegador › convidar mostra o LINK quando o e-mail não sai, e ele leva a definir a senha (1.0s)
  ✓  16 e2e/telas.spec.ts:380:3 › as telas, no navegador › esqueci minha senha responde igual, exista a conta ou não (248ms)
  ✓  17 e2e/telas.spec.ts:391:3 › as telas, no navegador › a tela de números mostra a BU e os dois canais desconectados (872ms)
  ✓  18 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (906ms)
  ✓  19 e2e/telas.spec.ts:411:3 › as telas, no navegador › identidade visual carrega e salva os campos pós-onboarding (1.1s)
  ✓  20 e2e/telas.spec.ts:430:3 › as telas, no navegador › Typebot permite buscar, abrir o editor e configurar um gatilho (1.3s)
  ✓  21 e2e/timeline.spec.ts:56:3 › timeline da inbox com backend e PostgreSQL reais › expõe o estado de abertura enquanto a primeira página aguarda o backend (732ms)
  ✓  22 e2e/timeline.spec.ts:77:3 › timeline da inbox com backend e PostgreSQL reais › abre a página recente, carrega todas as páginas anteriores e preserva posição (1.2s)
  ✓  23 e2e/timeline.spec.ts:108:3 › timeline da inbox com backend e PostgreSQL reais › reconecta sem evento posterior e recupera 130 mensagens em mais de uma rodada (1.4s)
  ✓  24 e2e/timeline.spec.ts:133:3 › timeline da inbox com backend e PostgreSQL reais › o poll retoma uma rodada pendente sem evento novo nem clique de continuação (1.0s)
  ✓  25 e2e/timeline.spec.ts:155:3 › timeline da inbox com backend e PostgreSQL reais › recupera o histórico completo após uma thread vazia receber mais de uma página (787ms)
  ✓  26 e2e/timeline.spec.ts:168:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.2s)
  ✓  27 e2e/timeline.spec.ts:227:3 › timeline da inbox com backend e PostgreSQL reais › preserva a âncora quando uma mensagem chega durante o backfill atrasado (912ms)
  ✓  28 e2e/timeline.spec.ts:260:3 › timeline da inbox com backend e PostgreSQL reais › mescla envio real com autoria e mantém o novo draft digitado durante o envio (903ms)
  ✓  29 e2e/timeline.spec.ts:286:3 › timeline da inbox com backend e PostgreSQL reais › mostra thread vazia/fim, falha recuperável e acesso perdido (2.0s)
  ✓  30 e2e/timeline.spec.ts:312:3 › timeline da inbox com backend e PostgreSQL reais › close vence resposta de backfill atrasada (913ms)
  ✓  31 e2e/timeline.spec.ts:333:3 › timeline da inbox com backend e PostgreSQL reais › troca de conversa e BU protege resposta atrasada de envio (1.3s)

  31 passed (48.6s)

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-frc-strong-final-3x.log

```
v22.23.3
[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 3 tests using 1 worker

  ✓  1 e2e/timeline.spec.ts:168:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.7s)
  ✓  2 e2e/timeline.spec.ts:168:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.6s)
  ✓  3 e2e/timeline.spec.ts:168:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.6s)

  3 passed (22.7s)
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-logout-lifecycle-5x.log

```
v22.23.3

> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-CydUyPfN.js   223.31 kB │ gzip: 69.58 kB
✓ built in 1.47s
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice
[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 5 tests using 1 worker

  ✓  1 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (977ms)
  ✓  2 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (986ms)
  ✓  3 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (1.0s)
  ✓  4 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (982ms)
  ✓  5 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (1.0s)

  5 passed (23.7s)

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-poll-targeted.log

```
v22.23.3

> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-DSeTAho8.js   223.33 kB │ gzip: 69.58 kB
✓ built in 1.36s
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice
[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 1 test using 1 worker

  ✓  1 e2e/timeline.spec.ts:133:3 › timeline da inbox com backend e PostgreSQL reais › o poll retoma uma rodada pendente sem evento novo nem clique de continuação (1.5s)

  1 passed (16.5s)

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-precheck-socket-fix.log

```
v22.23.3

> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-CydUyPfN.js   223.31 kB │ gzip: 69.58 kB
✓ built in 1.44s
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

> @leadshug/web@0.1.0 test
> vitest run


 RUN  v2.1.9 /workspace/web-app

 ✓ src/timeline.test.ts (2 tests) 3ms
 ✓ src/tempoReal.spec.ts (6 tests) 7ms
 ✓ src/api.spec.ts (12 tests) 45ms

 Test Files  3 passed (3)
      Tests  20 passed (20)
   Start at  03:29:46
   Duration  561ms (transform 417ms, setup 0ms, collect 485ms, tests 55ms, environment 1ms, prepare 289ms)


```

## Required full applicable test audit workload
Assess product/test delta alignment, workaround/retrofit risk, assert efficacy AND efficiency, enough negative/positive coverage and exclusions, honest test-after/negative control rather than fabricated TDD; module DI/wiring scopes/tokens and doubles only external Meta/Evolution ports; auth/grants/real PG and browser transport identity; owning package scripts and CI comparison; Node22/runtime provenance captured before tests, source including untracked new files, builds and served JS match; no skips/focused markers/fallbacks; fixture owns every proof subject; persistence/readback/business outcomes rather than status alone. Strong race target must combine H>T, dirty traversal already behind T cursor, late UUID inserted behind walked range, original T retained through coalesced pass, whole IDs compare, max3queries per round, one in flight. Review finite test count/log status and all evidence layers against exact claims. Distinguish invalid diagnostics from authority. EPS SQL predicates/data distribution/index decision, BCI SELECT barrier + negative control and restoration, FRC10events×3 and RLS measured one-stage correctness/bounds/latency. Coverage must justify loading/empty/end/error/retry/access, context and draft, metadata/scroll, initial+reconnect, selected-thread poll. Assess lifecycle cleanup and callback refs. A required test-quality audit must contain conclusions on all applicable rubric axes, not a short verdict. Fit detailed axis conclusions and decision mapping in overall_assessment/recommended_path strings as schema permits. If material gaps exist, return actionable findings ordered high->low with IDs, file:line evidence, why-now/options/recommendation. No waivers inferred. Final JSON must follow embedded schema, additionalProperties=false.
