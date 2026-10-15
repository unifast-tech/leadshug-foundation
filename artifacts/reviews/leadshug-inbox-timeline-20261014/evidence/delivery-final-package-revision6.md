# ST-ATT-01 bounded-summary final delivery review
Fresh internal no-context final reviewer, not implementing agent or previous reviewer. UserAPROVADO2026-10-14. Frozen Foundation plan649372fbe81f6cccc0f8902b52fe32e2ecfc061a; API baseline5db3fbe2043428749895fc3ff6441e9457467dd0; Web baseline6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9. This final pass follows TERMINAL architecture adherence and full applicable TQA resolutions, embedded below. Only approved API7/Web9, primary checkout/single code writer; no worktrees/copies, production deployment, remote product push or CI claim. Foundation docs/main commit-push is documentary workflow. Product source revision4 unchanged during test-only revision6; retained API115/224/EPS/BCI/RLS source identity verified; current Web full suite and FRC match all16files and served==dist. No waivers or deferred verification. Commit/Verified local/guard closeout remain procedural final actions, not permission for remote product promotion.

## Frozen/current TODO Scope

- [x] Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API.
- [x] Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor.
- [x] Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores.
- [x] Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID.
- [x] Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada.
- [x] Preservar histórico, cursor histórico, metadados atuais e draft correto durante envio, claim, close, backfill, poll e eventos/reconexão de socket.
- [x] Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens.
- [x] Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo.
- [x] Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado.



## Frozen/current TODO Out of Scope

- Transferência, exclusividade de resposta, SLA, distribuição de agentes, novas equipes e papéis.
- Estados de entrega/leitura/falha e deduplicação de recebimento por externalId.
- Mídia, templates, campanhas, CRM e automações Typebot.
- Mudanças nos contratos da API pública ou da tela Consultar.
- Redesenho da lista de conversas ou paginação da lista; a story cobre mensagens de uma conversa.
- Expansão de infraestrutura, uso de dados reais, integração com runtime legado ou publicação.



## Frozen/current TODO Definition of Done

- [x] DOD-01: contrato aprovado e consolidado no módulo responsável.
- [x] DOD-02: histórico maior que 200 é alcançável sem lacunas/repetições, inicial recente, empates estáticos e inserções empatadas durante recuperação.
- [x] DOD-03: autorização/cursor não permitem outra conversa, BU ou Mantenedora; recurso inacessível é 404 antes de query inválida.
- [x] DOD-04: backfill, envio/refresh/close, troca rápida, reconexão sem evento posterior e recuperação mantêm histórico, posição, cursores, metadados e draft corretos.
- [x] DOD-05: limite/cursor/marcarLida, vazio/fim, falha/retry e recuperação pendente têm contrato/UI verificados; entradas posteriores à fronteira de abertura continuam não lidas.
- [x] DOD-06: suites API/Web/Playwright passam no backend real e banco isolado; plano SQL recente/profundo/empates registra custo e decisão de índice; migrate deploy validado se houver migração.
- [ ] DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão.



## Frozen/current TODO Validation Steps

- [x] VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional.
- [x] VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e.
- [x] VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos.
- [x] VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL.
- [x] VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada.
- [x] VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado.
- [ ] VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout.
- [x] VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha.



## Frozen/current TODO Decision Baseline (Frozen Before Implementation)

Proposta técnica congelada para crítica em 2026-10-14 após integração ARCH-TL-01..06: superfície BFF, parâmetros/limites, reconhecimento atômico, recuperação bounded, estado por conversa, paths, DoD e provas reais deste TODO. A referência de versão publicada está em Gate: Review Baseline Freeze. O congelamento original não concedia implementação; a autorização posterior está registrada em Approval, pelo “APROVADO” explícito de 2026-10-14.



## Frozen/current TODO Decision Adherence Validation (Mandatory Before Delivery)

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



## Frozen/current TODO Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Canonical owner / decision | Implementation | Status |
| --- | --- | --- |
| inbox-and-conversations / thread BFF paginada | controller + timeline-pagination + ConversationsService.timeline | Adherent; contrato anterior ao código4cabc467,API224,parecer independente aceito. |
| inbox-and-conversations / recuperação e contexto | Inbox + timeline + tempoReal | Adherent; código revision4 aceito, mesmo produto na provaWeb36/FRC3; Verified local no módulo owner; TQA causal aceitou as provas atuais. |
| identity-and-tenancy / BU e grant | Resolver/AccessService existentes | Adherent; nenhuma decisão canônica mudou, negativos reais401/404/400 e readback. |
| audit-and-history / autoria e ações | responder/claim/close existentes | Adherent; autoria/audit preservados, regressões reais e destinations. |



## Frozen/current TODO Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface | Focus | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| Orquestrador / inspeção bounded | API auth/read-state e UI races; runner/frescor | passed | implementation-observations.md; execution-evidence.md; source manifest revision5 | fixed IMPL-01..14 e ARCH-DEL-01-ERR; sem P1/P2 aberto de produto | Correções fiéis comprovadas, produto aceito pela aderência; TQA independente ainda julga provas reforçadas. |
| CI API local | Leaf scripts do job tocado | passed | evidence/api-ci-light-revision2-20261015.log; evidence/api-e2e-authority.log; test-surface-admission.md | 0 falhas na execução final | generate/lint/build/unit115 e PostgreSQL224 adicionais, serializados. |
| Revisão independente | Aderência, segurança, desempenho e provável P1/P2 | passed | delivery-adherence-resolution.json; delivery-tqa-causal-resolution.json | no findings; P1/P2 anteriores fixed | Aderência/TQA convergidas; final review é gate separado antes de entrega. |



## Frozen/current TODO Rule-Spirit Anti-Pattern Hunt

| Rule Surface | Lens | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| NestJS / parser e limites | Validação runtime, grant antes cursor, ACK e queries bounded | passed | API224; delivery-adherence-resolution.json; scansAPI finais | no findings materiais; hints HTTP acompanhados de readback | Sessão/grants/domínio/PG reais, ACKbarreira e sem mudança público/Consultar. |
| React / Inbox e socket | Owner/generation, piso T, cursor, lifecycle e poll | passed | delivery-adherence-resolution.json; Web36/FRC3; implementation-observations.md | fixed IMPL-01..14,ARCH-DEL-01..04/ERR | Sem cacheframework/fetchall/budgetrenewal; fonte de produto aceita inalterada. |
| Scan heurístico API/Web | Domínios/targets e bypass disfarçado | passed | scan-triage-api.json e scan-triage-web.json; rawscansAPI/Webrev5; aderência aceita | no findings materiais; API30/15 e Web42/21 triados | by-design/no-action para loopback/.test de fixture e regexHTML preexistente, sem allowlist/supressão; TQA é gate separado. |



## Frozen/current TODO Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

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



## Frozen/current TODO Security Risk Assessment (Mandatory Before Delivery)

- **Gate decision:** required
- **Why this decision:** cursor, grants e mudança de contexto.
- Autorizar primeiro; resolver cursor na conversa; limitar sua forma/tamanho e queries. Testar cursor de outra conversa autorizada, outra BU sem grant no mesmo tenant e outro tenant, separadamente.
- Banco descartável dedicado; bootstrap com sessão/guards/domínio/persistência reais e dublês só nas portas externas. Não mascarar BFF nem expor suporte de teste em produção.
- API224 comprovou precedência401/404, cursor scoped400 e ausência de escrita em query inválida; testes negativos distintos e readback PostgreSQL. Parser rejeita array/repetição e limite/tamanho inválidos. Bootstrap/fixtures estão em test/, recusam DB não descartável, sem rotas de suporte em produção. Aderência round1 confirmou a fronteira API/segurança; delta julga efeitos de contexto Web corrigidos. Sem alegação de pentest ou provider externo validado.



## Frozen/current TODO Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

Auditoria executada: artifacts/reviews/leadshug-inbox-timeline-20261014/verification-debt.md e evidence/verification-debt-pre-final.log. Helper lexical high/exit2 por termos do template/histórico; classificação manual: inline none, nenhum waiver/dívida material escondida de produto/testes. Gates independentes/guardas e consolidação ainda abertos, sem claim de closeout; reavaliar após convergência.



## Frozen/current TODO Delivery Confidence Gate (Required for `✅ Production-Ready`)

Entrega local-only; sem autorização de publicação, promoção operacional ou claim Production-Ready. SLO, tráfego/provider externo e capacidade de produção não foram validados.



## Frozen/current TODO Module Consolidation Gate (Required Before `Completed`)

Contrato consolidado antes do código no owner modules/inbox-and-conversations.md; coleta atualAPI115/224,Web20/36,FRC3 e SQL/BCI/RLS pronta. Estado Verified local consolidado no owner com API115/224,Web20/36,FRC3,SQL/BCI/RLS e aderência/TQA aceitas. Registrar SHA dos commits no closeout; outros módulos preservam decisões.



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

Aprovado pelo usuário em 2026-10-14 no [TODO ST-ATT-01](../todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md). Este módulo é o owner do contrato; implementação e verificação são registradas no TODO. Estado de verificação: **Verified local**, em2026-10-15. API115unit/224E2E, Web20unit/36browser e FRC3 passaram em Node22/PG16 descartável com fontes/build servido conferidos. Aderência e TQA independentes convergiram; [evidência e limites](../artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md). O closeout documental depende do final review/guardas; não há promoção operacional ou Production-Ready.

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

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-adherence-resolution.json
```
{
  "findings": [],
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-adherence-resolution-dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "delivery-adherence-resolution-native",
  "overall_assessment": "Accept revision4 for this bounded architecture-adherence resolution. ARCH-DEL-04 is resolved on the supplied source and evidence. No new material divergence from the frozen contract or Decision Baseline is demonstrated. Final delivery acceptance remains conditional on the outstanding independent gates.\n\nThe error lifecycle now has explicit ownership. All Inbox error writes pass through definirErro, which advances the shared version and records recovery ownership only for recovery failures. Both empty and non-empty successful coverage paths call limparErroRecuperacao. That helper clears only the still-current recovery-owned error for the matching generation. Other action starts, clears and failures invalidate that ownership, so successful recovery cannot erase a later send error. Existing generation and conversation checks remain at the asynchronous call sites, and context changes reset error ownership. The change implements the approved failure/retry behavior without changing retry policy or requiring renewed architecture approval.\n\nThe protection harness directly distinguishes the reported defect: both existing recovery-failure regressions now require the alert to disappear after successful coverage. The additional test holds a real successful recovery response, aborts a concurrent send, observes its failure alert, then requires that alert to survive completed recovery. Full ordered DB/UI IDs, unread preservation and absence of the aborted outbound message accompany the presentation assertions. These are meaningful behavioral oracles. Development is honestly classified as test-after; the package does not establish a revision4 fail-first execution or retroactive TDD.\n\nARCH-DEL-01, ARCH-DEL-02, ARCH-DEL-03 and ARCH-DEL-01-ERR remain resolved. The current delta preserves debit before await, the shared three-attempt round budget, single-flight ownership, dirty restart, original pending T, empty-thread notifications and opening invalidations. Existing tests retain direct request-count and concurrency assertions, including failed attempts and an event after the third request. The six conversation/BU destination transitions retain draft, error, selection, messages, metadata and scroll checks. The carried budget and cursor mutation controls remain supporting historical evidence; no regression at those loci is shown.\n\nDecision adherence remains supported for the active-conversation collection, ID merge, complete timestamp-boundary traversal, separate historical/recovery cursors, historical metadata isolation and stale-context protection. The unchanged API assessment is carried forward using the supplied seven-file identity attestation and terminal audit: authorization before pagination validation, conversation-scoped cursor resolution, deterministic createdAt/id ordering, N+1 bounded reads, atomic opening ACK and read-neutral background reads. Public API, Consultar and excluded stories retain their reviewed boundaries. No temporary exception, fetch-all fallback or anticipatory implementation is evidenced.\n\nStructural soundness and elegance are acceptable. Error ownership stays within the existing active-thread owner, uses small stable callbacks and adds constant-time bookkeeping. It introduces no new service ownership, provider scope, cache framework or infrastructure path. The existing empty/non-empty traversal branches do not justify an unrelated refactor during this focused correction.\n\nTest quality is acceptable for this adherence resolution. Source-owned discovery and project scripts remain intact. Real BFF responses are delayed or explicitly aborted rather than fabricated. The declared harness retains real session, grants, domain, PostgreSQL and WebSocket behavior, with replacements limited to authorized external Meta/Evolution ports. Fixtures own their subjects and remain outside production entrypoints. No changed-test skip, focus marker, required-boundary mock fallback or ambient proof-subject selection is evidenced. Status assertions are accompanied by business outcomes and readbacks. The scanner's medium result is triaged rather than suppressed: loopback targets belong to tests, the HTML detector is pre-existing, and the migration COUNT is an aggregate. The lexical debt warning does not itself demonstrate a waiver.\n\nOperational fit is acceptable within the declared local scope. Embedded revision4 logs report Web20/20, browser35/35 and FRC3/3. The supplied pre-worker attestation summary binds both browser runs to current source and matching served/dist bundle hashes under Node22 and disposable PostgreSQL16. Unchanged API115/224 and retained CI leaf evidence can be reused without another broad API run. The React npm run test:tela mapping is appropriate. I assessed only the embedded package and did not execute commands or independently recompute hashes. This assessment supports the recorded TQA remediations but does not replace or terminate the separate live TQA review.\n\nPerformance is acceptable within the approved evidence scope. Revision4 adds no page requests or query changes, and refreshed FRC preserves the scheduling bounds. Carried EPS measures recent, deep and tied access and records the deep predicate's 10,001 filtered rows. Rejecting the measured worse composite index follows the conditional index decision. BCI supplies three deterministic batches retaining ten increments after ACK, with a discriminating negative control. RLS supplies thirty reads at concurrency five with correctness and read-neutral checks. These establish the bounded local claims, without production capacity or SLO certification. Active-conversation memory growth, backdating outside T and external-provider limits remain explicit.",
  "recommended_path": "Record ARCH-DEL-04 as fixed and accept this bounded adherence resolution. Preserve the prior resolved architecture findings and frozen design; no redesign or renewed product approval is warranted. Consolidate the revision4 evidence references and finding ledger. Let the existing TQA review reach its terminal result before starting any further TQA gate, and provide it the revision4 test delta for its own adjudication. Complete the remaining required independent reviews, final review, canonical consolidation and execution/closeout guards before checking DOD-07 or VAL-07 and claiming local completion. Retain unchanged API/EPS/BCI/RLS evidence and their stated limits; repeat validation only if subsequent changes or findings invalidate it.",
  "performance_position": "acceptable",
  "elegance_position": "acceptable",
  "structural_soundness_position": "acceptable",
  "operational_fit_position": "acceptable"
}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-tqa-causal-resolution.json
```
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-tqa-causal-dispatch.json","review_kind":"test_quality_audit","reviewer_label":"delivery-tqa-causal-native-no-context","overall_assessment":"Accept the bounded TQA causal resolution. ARCH-DEL-03-EVID is resolved: the scenario establishes the first authenticated socket frame before conversation selection, holds a real initial BFF GET after its backend fetch, persists silent growth, closes the established native socket, requires the second authenticated frame before releasing the opening response, and observes recovery without a later message event or poll/clock advance. It asserts a cursorless read-neutral recovery request plus complete DB/UI ID and unread readback. The focused mutation preserving the first callback while suppressing reconnect callbacks fails with zero recovery requests, and byte-exact restoration is evidenced before canonical runs. This is a discriminating causal regression test, not pass-the-test repair. Test effectiveness is strong for the changed locus; test efficiency is acceptable through one focused scenario, a targeted mutation control, full browser execution, and retained repeated FRC evidence. Test-after status is stated honestly. No skip/focus, fabricated BFF payload, auth shortcut, ambient subject, production hook, or relevant DI-parity bypass is evidenced. Structural soundness and elegance are acceptable: the test-only sequencing/instrumentation preserves the real transport and leaves accepted product code unchanged. Operational fit is acceptable for the declared local scope, with owned commands, real Nest/session/grant/PostgreSQL/WebSocket boundaries, current-source manifests, and served-bundle freshness. Performance remains mixed but unchanged and candidly bounded by the documented deep-keyset residual and absence of a production-capacity claim. Previously resolved TQA findings remain closed; no fresh regression is demonstrated.","recommended_path":"Record ARCH-DEL-03-EVID as fixed for this TQA gate and continue the remaining independent closeout, final-review, and governance gates. Preserve the current evidence and stated local-performance/production-scope limits; no redesign, additional test repair, or renewed approval is warranted unless source or scope changes.","performance_position":"mixed","elegance_position":"acceptable","structural_soundness_position":"acceptable","operational_fit_position":"acceptable","findings":[]}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md
```
# Evidência de execução ST-ATT-01

Estado atual: código revision6-final congelado e validado; aderência convergida, resolução TQA causal em execução. Aprovação humana em2026-10-14. API/Web na branch local feature/inbox-timeline-pagination, checkout principal com executor único /root/timeline_executor_resume. Foundation main. Nenhum deploy, push de produto, stage-full ou capacidade de produção reivindicados.

## Fontes e runtime atuais

Fonte de verdade da coleta: [resumo revision6](evidence/executor-revision6-summary.json). Todos os16 arquivos alterados/novos (API7/Web9) foram comparados byte a byte pelo root às duas attestations finais. API7 também é idêntico à geração que produziu224E2E/EPS/BCI/RLS. Sem alteração de schema/migration, providers, público/Consultar, env/compose/CI ou gitlinks.

Linux Node22.23.3, PostgreSQL16.14 descartável leadshug-timeline-postgres-20261014/DB leadshug_timeline_20261014,17migrations, sem host publish do DB. Dependências Linux via npmci/volumes próprios; módulos Windows não foram usados. Chromium Playwright1.62.1/Noble com Node22 substituindo somente o binário24 da imagem oficial. API3100, fixtures3101, navegador http://127.0.0.1:4173 dentro do runner descartável. Testes que usam DB foram serializados.

Attestations pré-workers:

- [Full36](evidence/attestation-browser-web-authority-revision6-final-full-20261015.json),2026-10-15T04:59:11.580Z.
- [FRC3](evidence/attestation-browser-web-authority-revision6-final-frc3-20261015.json),2026-10-15T05:00:22.318Z.

Ambas registram fonte/branch/diff, manifest API/dist,17migrations e health API/fixture/preview200. Bundle servido==dist SHA2567cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2 nas duas. Builds frescos precedem os workers; não se usa captura posterior como substituta dessa prova.

## Resultados por owner

| Superfície | Comando próprio | Resultado | Raw |
| --- | --- | --- | --- |
| API CI leafs | npm run prisma:generate; npm run lint; npm run build; npm test |4leafs exit0;115/115unit,17arquivos | [stdout completo rev2](evidence/api-ci-light-revision2-20261015.log) |
| API PostgreSQL | npm run test:e2e |224/224,20arquivos,111.92s,exit0 | [suite serializada](evidence/api-e2e-authority.log) |
| Web CI leafs | npm run build; npm test |build exit0;20/20unit,3arquivos | [full revision6-final](evidence/web-authority-revision6-final-full-20261015.log) |
| Web browser adicional | npm run test:tela |36/36,1.0m,exit0 | [full revision6-final](evidence/web-authority-revision6-final-full-20261015.log) |
| FRC repetido | npx playwright test e2e/timeline.spec.ts --grep="preserva o piso T" --repeat-each=3 |3/3,23.1s,exit0 | [FRC atual](evidence/web-authority-revision6-final-frc3-20261015.log) |

API cobre251IDs, limites/cursores, empates, neutralidade e precedência de autorização401/404/400, sem escrita quando auth/query falham; consumidores existentes mantêm contrato. Bootstrap usa AppModule/session/grants/domínio/PG/WebSocket reais; dublês apenas Meta/Evolution externos. Suporte está em test/, recusa DB não descartável e não existe no entrypoint de produção. Browser atrasa respostas BFF reais e usa abort explícito para erro; nunca fabrica payload BFF.

Web cobre página recente/backfill completo, âncora com chegada durante await, autoria persistida/draft digitado durante envio, close versus backfill, reconnect sem evento posterior e poll60 que retoma recuperação>3páginas sem Continue. Inclui abertura+evento enquanto threadnull, empty>3páginas+evento entre rodadas e seis transições conversa/BU × resposta antiga de envio com sucesso/falha/backfill; seleção/draft/erro/IDs/metadados/scroll do destino são comparados após release.

FRC forte retém T original com H>T e ID menor inserido atrás do cursor percorrido,10gatilhos repetidos mais inicial e evento após terceira query,12frames/unread por repetição. Conta exatamente3consultas automáticas antes de Continue, máximo1emvoo; evento não renova saldo. Testes específicos cobram3GETs abortados no orçamento e exigem restart recente após erro histórico com dirty, sem outro trigger; IDs completos/read-state comparados após continuations.

## Contraprovas e integridade

Implementação/testes são test-after; não se reivindica TDD retroativo. Mutações locais temporárias foram restauradas em finally, com prova byteexact/SHA, sem commit:

- ACK movido para depois do SELECT: [negativo](evidence/bci-mutation-control.log) falha10vs0; [canônico restaurado](evidence/bci-canonical-after-mutation.log) passa1/1 com3lotes; [SHA](evidence/bci-source-restored.sha256).
- Débito de saldo após await: [negativo](evidence/web-revision3-budget-negative-control-20261015.log) falha3esperadas/5requests; [restauração](evidence/web-revision3-budget-negative-control-20261015.restore).
- Guarda restart removida do catch histórico: [negativo](evidence/web-revision3-cursor-negative-control-20261015.log) falha2esperadas/1recent; [restauração](evidence/web-revision3-cursor-negative-control-20261015.restore).

- Cursor vazio antigo retido: [negativo](evidence/web-revision5-empty-cursor-negative-control-20261015.log) falha temCursor=true quando a retomada deve ser recente; [restauração](evidence/web-revision5-empty-cursor-negative-control-20261015.restore).

As fontes finais restauradas passam no full36 e têm os hashes das attestations. Nenhuma prova targeted substitui a suite completa atual.

## Performance e concorrência

[EPS](pcv-eps.json): [SQL exato](evidence/explain-timeline-exact.sql)/[planos](evidence/explain-timeline-exact.log),20382mensagens,1000empates. Âncoras constantes resolvidas fora da medição; recente1.094ms/37buffers, profundo3.442ms/357buffers/10001linhas filtradas, empate0.850ms/37buffers. [Trial composto](evidence/explain-index-trial.log) profundo3.942ms/9832buffers e mesmo filtro; removido, sem migration justificada. Predicado OR ainda filtra linhas mais recentes: risco explícito, sem SLO de produção.

[BCI](pcv-bci.json): real SELECT de messages bloqueado por lock, ACK observado antes da query em pg_stat_activity. Dez incrementos atômicos concorrentes preservados antes/depois da resposta em3lotes; IN real posterior eleva a11. Negativo acima demonstra eficácia contra reset tardio.

[RLS](pcv-rls.json): [runner](evidence/rls-read-sample.mjs)/[raw](evidence/rls-read-sample.log), uma etapa5concorrentes×6lotes,30/30HTTP200,50mensagens,zeroerros; p5023.36ms/p9564.26ms/max68.5ms. Unread7 e251messages preservados. Conversa estrangeira com limite=invalid devolve404; o nome raw MalformedCursor está incorreto, representa limite inválido. Cursores reais têm negativos distintos no APIE2E. Regras de correção/read-neutral fixadas no runner; latência observada, sem promessa de capacidade.

[FRC atual](pcv-frc.json) liga políticas por ação e provas finais; [geração1](pcv-frc-generation1.json) preserva payload anterior. EPS/BCI/RLS passaram com parecer independente; FRC corrente aguarda resolução TQA. Residual: coleção cresce apenas na conversa ativa, backdating foraT e transport/provider/produção fora deste contrato.

## Revisões e scans

Round1 de [aderência](delivery-adherence-round-1.json) e [TQA](delivery-tqa-round-1.json), ambos internos stateless no-context/max e terminais com turn.completed/schema/merge, exigiram orçamento3 real, notificações de vazio/abertura, efeitos de contexto e retenção stdoutAPI. Todos foram corrigidos dentro do mesmo TODO; nenhum escopo de arquitetura foi reaberto. Duas variantes de erro foram identificadas/corrigidas antes de qualquer delta.

Delta atual self-contained SHA2564e52264e5990846b635c7631450e23dae184ca5e7c66b127a7dbe9864f58da59,410938bytes. Gpt-6.1-sol/max e gpt-5.6-terra/max em execução via runner interno nativo, após fonte congelada34/FRC3. Nenhuma revisão live foi interrompida, substituída ou reduzida. Final review ocorrerá após resolução dos deltas; sem waiver.

Scans finais só dos16 fontes: API30observações/15loci e Web42/21, sem allowlist/supressão. [Triage API](scan-triage-api.json)/[Web](scan-triage-web.json): loopback/.test pertencem a fixtures; regex HTML src/api.ts preexistente. Raw em evidence/rule-spirit-final-*.json/.log. Helper test-quality retorna exit2/medium: API1status, Web13status+1COUNT; status acompanha outcomes/readback/IDs/unread e COUNT não é sujeito ambiente. Nenhum hardbypass, skip/focus, authshortcut, no-exception-only, DIoverride ou mockfallback detectado. Logs raw preservados para TQA independente. [Auditoria de dívida](verification-debt.md) distingue linguagem lexical de waiver efetivo; inline debt none.

## Limites e diagnósticos históricos

CI-equivalent cobre somente jobs API/Web tocados; PG/browser são validações locais adicionais requeridas. [Admissão](test-surface-admission.md) registra owners. O completion guard genérico hardcodeia literais Flutter; neste React, a capacidade run_web_navigation_smoke corresponde explicitamente a npm run test:tela. Nenhum comando Flutter foi executado ou inventado; provas são specs Playwright source-owned/build fresco/URL descartável/mutação em feature non-main. Round1 de aderência aceitou esse mapeamento transparente.

220/222API falhou por duas expectativas de fixture;223/223 sobrepôs browser no mesmo DB e é inválido. O resumo bruto inicial troca essas causas; preservado sem corrigir raw. Só224serializado é autoridade. Node24, execuções interrompidas, primeiros EXPLAIN com OFFSET dentro da medição e gerações antigas Web31/32/33 são diagnósticos/história, nunca prova atual. Harness de contexto teve rótulo BU e representação de texto corrigidos; timeout global30s preservado. Primeiro target budget exigia toda fixture sem empate: oracle corrigido para grupoT empatado, sem ampliar cobertura contratual.

Saídas web/test-results foram removidas após runners terminarem. Banco/volumes próprios mantidos até revisões; cleanup somente desses recursos após retenção das provas. Não se afirma sessão/provedor WhatsApp externo ou runtime operacional validado.

## Revisão4: autoridade atual após ARCH-DEL-04

O delta de aderência delivery-adherence-delta.json terminou e confirmou todos os achados anteriores, mas encontrou alerta de recovery persistente após sucesso. Foi corrigido dentro do mesmo owner com versão/geração do erro; qualquer write posterior de outra ação invalida sua limpeza tardia. Os testes agora exigem ausência do erro de recovery ao completar a cobertura e preservação de erro mais recente de envio abortado durante retry, com IDs/readback e envio ausente no DB.

Autoridade corrente substitui revision3: evidence/executor-revision4-summary.json, Web20/20, browser35/35, FRC3/3, Node22.23.3; logs e attestations revision4-final. Root comparou diretamente todos16 hashes atuais às duas attestations; API7 continua igual à autoridade224. Bundle servido==dist SHA2567cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. PCV FRC atualizado; pcv-frc-generation3.json preserva a observação anterior. Scans atuais Web em evidence/*revision4-web-app.*; API fonte idêntica conserva scan anterior. Nenhum waiver nem runner ativo; código congelado para resolução independente. TQA delta anterior segue live contra pacote imutável revision3, sem interrupção ou substituição.

## Revisão5: prova final das transições de vazio e reconexão

Fonte de produto idêntica à revision4 aceita por delivery-adherence-resolution.json (findings vazio), alterado somente e2e/timeline.spec.ts. Targeted2/2: backlog do vazio no passado, primeira retomada recente/neutra/semantes,162IDs/unread2 e status IN_SERVICE visível após claim BFF real enquanto pausado. Negativo mantendo cursor antigo falha temCursor=true; Inbox restaurado byteexact antes dos runs finais. Abertura: GET real já buscado retido, instância WebSocket NATIVA apenas registrada pelo construtor, close real, segunda conexão autenticada pelo frame servidor conectado ANTES do release; sem evento mensagem ou avanço de clock depois, headreadneutro/IDs/unread provados. Instrumentação não substitui transporte/socket/servidor.

Autoridade atual: evidence/executor-revision5-summary.json; Webunit20/20,browser36/36,FRC3/3,Node22.23.3. Duas attestations revision5-final vinculam os16 fontes atuais e bundle servido==dist7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2, mesmo produto da revisão4. Root verificou todos16 hashes e igualdade API7; nenhum rerunAPI/SQL/RLS necessário. Scans Web finais:42observações/21loci; testquality exit2/medium por15status+1COUNT,zero hardbypass/authshortcut/mockfallback; outcomes/readbacks acompanham os hints. Roteamento para resolução TQA completa no modelo prescrito, após revisão anterior terminal, sem waiver. Saídas test-results removidas, nenhum runner ativo; fontes congeladas.

## Revisão6: isolamento causal confirmado no runner

Último gap de prova isolado: primeiro frame autenticado conectado obrigatoriamente ANTES da seleção da conversa. Somente depois GETreal retido, crescimento silencioso, fechamento nativo e segundo frame autenticado antes release. Contraprova preserva primeiro onopen e suprime apenas callbacks posteriores: falha com zero requests de recuperação; tempoReal.ts restaurado byteexact. Targeted2/2, Web20/36 e FRC3/3 finais exit0; attestations pré-workers04:59:11.580Z/05:00:22.318Z, fonte16conferida pelo root, mesmo bundle7cf5c913…170e2 e mesmo produto revision4 aceito. Evidência: executor-revision6-summary.json e raw revision6-final/negative/restore em evidence/. API/SQL/RLS não repetidos por fonte invariável.

TQA causal fresh/internal no-context gpt-5.6-terra/max em execução sobre bounded-summary completo SHA0a5532c90082359214df6bb086e5b12b5182f68b7f8f944aa617e6e6bc908383. Todas as revisões anteriores eram terminais; nenhum gate live foi substituído ou reduzido. Só após convergência seguem final review e closeout.

Convergência TQA causal: delivery-tqa-causal-resolution.json, findings vazio, aceitou ARCH-DEL-03-EVID e preservou todos os resolvidos. Aderência/TQA completas; PCV4lanespassed com hashes canônicos e pareceres. Final review e guardas permanecem gates antes do closeout.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/verification-debt.md
```
# Verificação de dívida ST-ATT-01

Auditoria manual sobre o contrato aprovado,16 fontes atuais, provas de execução, testes e consolidação. Evidência raw: evidence/verification-debt-pre-final6.log. O helper é lexical e reporta high/exit2 por termos waiver/n/a/pending/release-blocker na linguagem do template, contratos e histórico. O resultado raw permanece íntegro; não equivale à descoberta de waiver efetivo ou defeito atual.

- Dívida inline: none. Nenhum TODO/FIXME/HACK/TBD/XXX nos16 fontes; nenhuma supressão.
- Evidência: fonte API idêntica à suite224/SQL/BCI/RLS; stdout API CI faltante no round1 foi recolhido com os4leafs/115unit rev2. Web20/36 e FRC3 atuais estão ligados aos16hashes e ao build/served pré-workers, conferidos pelo root. Negativos de ACK, orçamento, restart histórico/vazio e reconnect-only são separados e restaurados, sem reivindicação de TDD.
- Validação: nenhum teste prometido foi removido ou waived. Suites targeted/gerações antigas/fixtures diagnósticas não substituem o full36. CI-equivalent permanece limitada aos jobs API/Web; PostgreSQL/browser adicionais explícitos. Sem stage-full/deploy/produção presumidos.
- Waivers: nenhum. n/a e not_needed descrevem contratos fora deste recorte (cutover, produção/remoto), sem reduzir gates required. Termos de pendência no contrato descrevem UI/recovery ou estados históricos; achados originais permanecem registrados para resolução independente, não adiados.
- Promoção canônica: contrato já consolidado no módulo owner antes do código; estado Verified local e links de closeout só serão promovidos após pareceres independentes. Transferência/mídia/status têm stories separadas e não são dívida desta entrega.
- Risco residual: deep keyset ainda filtra linhas mais recentes; EXPLAIN e trial justificam ausência de migration, sem SLO de produção. Coleção cresce só na conversa ativa; backdating foraT/provider externo/produção estão fora do contrato aprovado.

Classificação de suporte antes do final: nenhuma dívida material escondida de produto/testes; fechamento ainda condicionado aos resolução TQA causal (anteriores terminais), final review, consolidação Verified e guardas. Os dois itens governance DOD-07/VAL-07 continuam unchecked enquanto esses gates são efetivamente executados. Não há waiver nem deferred verification; após convergência, atualizar o mesmo artefato e repetir somente o helper documental final.

Convergência independente: delivery-adherence-resolution.json e delivery-tqa-causal-resolution.json aceitam produto/provas atuais; nenhuma dívida material de produto/testes ou waiver. Contrato e decisões verificadas já consolidados no módulo owner como Verified local. Restam somente final review e seus guardas/commits de closeout; DOD-07/VAL-07 ficam unchecked até execução real desses gates.

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
  "reviewer_id": "delivery-adherence-resolution-native",
  "recorded_at_utc": "2026-10-15T03:36:56Z",
  "evidence_type": "explain",
  "sample_profile_id": "EPS-SP-STRONG",
  "acceptance_rule_id": "EPS-A2",
  "result_summary": "Measured recent/deep/tied pages on20382 rows,1000 ties; existing index retained after candidate trial. Independently accepted by delivery-adherence-resolution.json; local scope only.",
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
    ],
    "independent_review": {
      "reference": "delivery-adherence-resolution.json",
      "reviewer_id": "delivery-adherence-resolution-native",
      "assessment": "acceptable within bounded local evidence; API source unchanged"
    }
  },
  "artifact_sha256": "248ea237489683aaa67371eb58efecab9e237c9aac08e36f3717b064f4825dfc"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-frc.json
```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "FRC",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "web-authority-revision6-final-frc3-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-chromium-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-tqa-causal-native-no-context",
  "recorded_at_utc": "2026-10-15T05:01:37Z",
  "evidence_type": "source-owned-playwright-real-backend-races",
  "sample_profile_id": "FRC-SP-M",
  "acceptance_rule_id": "FRC-A1",
  "result_summary": "Web20unit/36browser and FRC3/3 passed on identical final source/build; scheduling, notification, error ownership and destination races independently accepted by delivery-tqa-causal-resolution.json. Local evidence, no production claim.",
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
      "pushes_asserted_per_repetition": 12,
      "pushes_note": "one initial head,10 real incoming webhooks during blocked traversal,one new event after third query;12 frames/unread; only3 automatic requests and max1 in flight before explicit Continue",
      "full_suite": {
        "cases_passed": 36,
        "duration_observed": "1.0m"
      }
    },
    "runner_or_manual_path": "web-app/e2e/timeline.spec.ts; npm run test:tela; npx playwright test e2e/timeline.spec.ts --grep=\"preserva o piso T\" --repeat-each=3",
    "race_matrix": [
      {
        "surface": "history",
        "case": "251 IDs; prepend same visible anchor offset delta<2px, including arrival while delayed actual response"
      },
      {
        "surface": "recovery",
        "case": "H>T,late lower UUID inT behind walked cursor,dirty restart retains originalT; first authorized round exactly3requests/max1inflight, third-request event cannot mintbudget; full DB/UI ID equality and unread12 after Continue"
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
        "case": "actual delayed POST, persisted author and typednewdraft preservation; full sixsubcase destination protection described below"
      },
      {
        "surface": "metadata",
        "case": "close wins over delayed historical response; no stale status restoration"
      },
      {
        "surface": "states",
        "case": "loading,empty,end,error/retry and grant-loss404; no fabricated BFF payloads"
      },
      {
        "surface": "budget/error",
        "case": "3 aborted actual GETs with real events consume3 attempts, no4th beforeContinue; negative control post-await debit fails3vs5; canonical restoration and full suite green"
      },
      {
        "surface": "historical error/restart",
        "case": "actual older page aborted while real new head arrives; recent-query restart required without another event, full tied-group IDs/unread after authorized continuations; negative control removedguard fails2vs1 recent reads"
      },
      {
        "surface": "opening",
        "case": "real initial GET snapshot held, real inbound frame during opening, read-neutral recovery without later trigger; unread preserved"
      },
      {
        "surface": "empty paused recovery",
        "case": "initiallyempty>3pages plus between-round inbound, retains recent restart through full IDs/currentmetadata"
      },
      {
        "surface": "recovery error lifecycle",
        "case": "successful coverage clears the current recovery error; newer unrelated send error survives; generation/version ownership and real browser negative-path assertions"
      },
      {
        "surface": "empty resume proof",
        "case": "past-timestamp backlog and real newer inbound; first authorized resume must be recent/readneutral/noantes, fullIDs/unread and current metadata; old-empty-cursor mutation fails and exact bytes restore"
      },
      {
        "surface": "opening reconnect proof",
        "case": "first authenticated real socket frame occurs before selecting; then actual GET held, silent DB growth, native socket close and second authenticated frame before release; reconnect-only callback mutation fails with exact restoration; no later event/poll, IDs/unread verified"
      },
      {
        "surface": "context destination",
        "case": "BOTH BU and conversation, old send success/network failure and backfill; destination selection/draft/error/IDs/metadata/scroll compared after release"
      }
    ],
    "runtime_freshness": {
      "captured_before_workers": "2026-10-15T05:00:22.318Z",
      "served_equals_dist_sha256": "7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2",
      "full_attestation_captured_at": "2026-10-15T04:59:11.580Z",
      "source_manifest_matches_full_suite": true,
      "root_verified_all16_current_source_hashes": true
    },
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision6-final-full-20261015.log",
        "sha256": "b0ea73876b3b9156eac85bbff5358c0101935017443ebf7e170263478419eab1"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision6-final-frc3-20261015.log",
        "sha256": "ddb8ecfc4b4008688c92ea85abb9734ffb548085669e9934dfda90925913900c"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-web-authority-revision6-final-full-20261015.json",
        "sha256": "d65dd1e089196fe83cdf2b3b4fc47d5208af28a55a89da45793b11013edf7270"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-web-authority-revision6-final-frc3-20261015.json",
        "sha256": "e63c9fe324edd2a390051aad88bd0d494ac71ec2856a2b2a756af12aae5731ae"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/executor-revision6-summary.json",
        "sha256": "472ba112563d191710792d41fdca8a145d4c10aebf1e0037b90f0c24628130e2"
      }
    ],
    "residual_risk": "Bounded active-conversation memory grows as user loads history; no cache of other conversations. Backdated imports earlier thanT group and production traffic/provider transport are outside this approved slice.",
    "independent_review": {
      "reference": "delivery-tqa-causal-resolution.json",
      "reviewer_id": "delivery-tqa-causal-native-no-context",
      "recorded_at_utc": "2026-10-15T05:05:29.176106+00:00",
      "assessment": "full applicable test-quality resolution accepted without findings"
    }
  },
  "artifact_sha256": "3148b1ccf77cc0d4f1f980b74077133878a735e20115c941c92313fecb55823c"
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
  "reviewer_id": "delivery-adherence-resolution-native",
  "recorded_at_utc": "2026-10-15T03:36:56Z",
  "evidence_type": "postgresql-overlap-probe",
  "sample_profile_id": "BCI-SP-M",
  "acceptance_rule_id": "BCI-A1",
  "result_summary": "Three deterministic real PostgreSQL barrier batches retain10 increments after ACK; regression mutation fails10vs0 and exact source restoration passes. Independently accepted by delivery-adherence-resolution.json; local scope only.",
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
    ],
    "independent_review": {
      "reference": "delivery-adherence-resolution.json",
      "reviewer_id": "delivery-adherence-resolution-native",
      "assessment": "acceptable within bounded local evidence; API source unchanged"
    }
  },
  "artifact_sha256": "5ff9ba52415aeb420acf1b805a7ccece7d59194c127b97aa3ce2e22af12842b4"
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
  "reviewer_id": "delivery-adherence-resolution-native",
  "recorded_at_utc": "2026-10-15T03:39:44Z",
  "evidence_type": "one-stage-authenticated-read-load",
  "sample_profile_id": "RLS-SP-L",
  "acceptance_rule_id": "RLS-A1",
  "result_summary": "30/30 reads,5 concurrent×6; p50 23.36ms,p95 64.26ms,max68.5ms; page50,unread7 unchanged,251 messages unchanged,foreign malformed request404. Independently accepted by delivery-adherence-resolution.json; no production SLO claim.",
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
    "residual_risk": "Small warm disposable one-stage sample; no stress, spike, soak, throughput or production capacity certification.",
    "independent_review": {
      "reference": "delivery-adherence-resolution.json",
      "reviewer_id": "delivery-adherence-resolution-native",
      "assessment": "acceptable within bounded local evidence; API source unchanged"
    }
  },
  "artifact_sha256": "eb0ec62492de2af2d52c5dc40eaa1defc776d9996d62048d554ce890a9991939"
}

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
  return webhook;
}

test.describe('timeline da inbox com backend e PostgreSQL reais', () => {
  let pageErrors: string[];
  test.beforeEach(async ({ page }) => {
    pageErrors = [];
    page.on('pageerror', (e) => pageErrors.push(e.message));
  });
  test.afterEach(async () => expect(pageErrors).toEqual([]));

  test('expõe o estado de abertura enquanto a primeira página aguarda o backend', async ({ page, request }) => {
    const fixture = await seed(request, 3);
    let mensagensRecebidas = 0;
    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
      try {
        const frame = JSON.parse(String(payload)) as { tipo?: string; conversaId?: string };
        if (frame.tipo === 'mensagem' && frame.conversaId === fixture.conversationId) mensagensRecebidas += 1;
      } catch { /* frames de conexão não são mensagens */ }
    }));
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
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-opening-invalidation', text: 'mensagem chega durante abertura atrasada' });
    await expect.poll(() => mensagensRecebidas).toBe(1);
    liberar();
    await expect(page.locator('.bolha')).toHaveCount(4);
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(expected.unreadCount).toBe(1);
  });

  test('reconecta durante a abertura retida e lê a cabeça sem novo evento', async ({ page, request }) => {
    const fixture = await seed(request, 3);
    await page.addInitScript(() => {
      const registro = [] as WebSocket[];
      const original = window.WebSocket;
      class WebSocketInstrumentado extends original {
        constructor(url: string | URL, protocolos?: string | string[]) {
          if (protocolos === undefined) super(url);
          else super(url, protocolos);
          registro.push(this);
        }
      }
      Object.defineProperty(window, '__timelineSockets', { value: registro });
      window.WebSocket = WebSocketInstrumentado;
    });
    const sockets: import('@playwright/test').WebSocket[] = [];
    let fechamentos = 0;
    let conexoesAutenticadas = 0;
    let mensagensRecebidas = 0;
    page.on('websocket', (socket) => {
      sockets.push(socket);
      socket.on('close', () => { fechamentos += 1; });
      socket.on('framereceived', ({ payload }) => {
        try {
          const frame = JSON.parse(String(payload)) as { tipo?: string; conversaId?: string };
          if (frame.tipo === 'conectado') conexoesAutenticadas += 1;
          if (frame.tipo === 'mensagem' && frame.conversaId === fixture.conversationId) mensagensRecebidas += 1;
        } catch { /* frames não JSON são controle do socket */ }
      });
    });
    await login(page, fixture.email, fixture.password, fixture.businessUnitId);
    // Establish that the first onopen completed before the opening generation
    // exists; only the later native reconnect may invalidate this opening.
    await expect.poll(() => conexoesAutenticadas).toBe(1);
    expect(sockets).toHaveLength(1);

    let liberar!: () => void;
    let iniciou!: () => void;
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const solicitacao = new Promise<void>((resolve) => { iniciou = resolve; });
    let chamadas = 0;
    const recuperacoes: URL[] = [];
    const rotaAbertura = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route(rotaAbertura, async (route) => {
      chamadas += 1;
      if (chamadas === 1) {
        const response = await route.fetch();
        iniciou();
        await continua;
        await route.fulfill({ response });
        return;
      }
      recuperacoes.push(new URL(route.request().url()));
      await route.continue();
    });
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    await solicitacao;
    await expect(page.getByRole('status').filter({ hasText: 'Abrindo conversa…' })).toBeVisible();
    expect(conexoesAutenticadas).toBe(1);

    // A primeira leitura já foi buscada e permanece retida no navegador. Estas
    // mensagens só entram no PostgreSQL; nenhum webhook ou evento as anuncia.
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 2, createdAt: Date.now() + 10_000 } });
    expect(burst.status()).toBe(201);
    await page.evaluate(() => {
      const instrumentada = window as Window & { __timelineSockets?: WebSocket[] };
      instrumentada.__timelineSockets?.[0]?.close(1000, 'reconexão E2E durante abertura');
    });
    await expect.poll(() => fechamentos).toBe(1);
    await expect.poll(() => sockets.length).toBe(2, { timeout: 10_000 });
    await expect.poll(() => conexoesAutenticadas).toBe(2, { timeout: 10_000 });

    liberar();
    await expect.poll(() => recuperacoes.length).toBeGreaterThan(0, { timeout: 10_000 });
    expect(recuperacoes[0].searchParams.get('marcarLida')).toBe('false');
    expect(recuperacoes[0].searchParams.has('antes')).toBe(false);
    await expect(page.locator('.bolha')).toHaveCount(5);
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(expected.unreadCount).toBe(0);
    expect(mensagensRecebidas).toBe(0);
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
    await expect(page.getByRole('alert')).toHaveCount(0);
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

  test('retoma thread vazia após evento entre rodadas e inclui toda a cabeça sem reler', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 0);
    let paginasRecuperacao = 0;
    let capturandoRetomada = false;
    const requisicoesRetomada: Array<{ marcarLida: string | null; temCursor: boolean }> = [];
    const rotaRecuperacao = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.get('marcarLida') === 'false';
    await page.route(rotaRecuperacao, async (route) => {
      paginasRecuperacao += 1;
      if (capturandoRetomada) {
        const url = new URL(route.request().url());
        requisicoesRetomada.push({ marcarLida: url.searchParams.get('marcarLida'), temCursor: url.searchParams.has('antes') });
      }
      await route.continue();
    });
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 160, createdAt: Date.now() - 60_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-empty-first-head', text: 'primeira cabeça da thread vazia' });
    const pending = page.getByText('Atualização pendente. O histórico pode ter uma lacuna.');
    await expect(pending).toBeVisible({ timeout: 25_000 });
    await expect(page.locator('.bolha')).toHaveCount(150);
    expect(paginasRecuperacao).toBe(3);

    capturandoRetomada = true;
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-empty-between-rounds', text: 'evento enquanto a thread vazia está pausada' });
    await expect.poll(async () => (await audit(request, fixture.conversationId)).unreadCount).toBe(2);
    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
    const claimStatus = await page.evaluate(async (conversationId) => {
      const response = await fetch(`/api/bff/conversations/${conversationId}/claim`, {
        method: 'POST',
        credentials: 'include',
        headers: { 'content-type': 'application/json', 'x-requested-with': 'leadshug-web' },
        body: '{}',
      });
      return { statusCode: response.status, body: await response.json() as { status?: string } };
    }, fixture.conversationId);
    expect(claimStatus.statusCode).toBe(201);
    expect(claimStatus.body.status).toBe('IN_SERVICE');
    await page.getByRole('button', { name: 'Continuar atualização' }).click();
    await expect.poll(() => requisicoesRetomada.length).toBeGreaterThan(0);
    expect(requisicoesRetomada[0]).toEqual({ marcarLida: 'false', temCursor: false });
    for (let i = 0; i < 5 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
      if (i > 0) await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(100);
    }
    await expect(pending).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toHaveLength(162);
    expect(expected.unreadCount).toBe(2);
    expect(expected.status).toBe('IN_SERVICE');
    await expect(page.locator('.inbox > .cartao.grade').getByText('IN_SERVICE', { exact: true })).toBeVisible();
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
    let requestsRecovery = 0;
    let requestsAtivo = 0;
    let maxRequestsAtivo = 0;
    let captureRequests = true;
    let liberar!: () => void;
    let aguardeSegundaPagina!: () => void;
    let aguardeTerceiraPagina!: () => void;
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const segundaPagina = new Promise<void>((resolve) => { aguardeSegundaPagina = resolve; });
    const terceiraPagina = new Promise<void>((resolve) => { aguardeTerceiraPagina = resolve; });
    let lateId = '';
    const piso = new Date('2026-10-14T12:00:00.000Z').toISOString();
    const rotaTimeline = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route(rotaTimeline, async (route) => {
      if (!captureRequests) return route.continue();
      requestsRecovery += 1;
      requestsAtivo += 1;
      maxRequestsAtivo = Math.max(maxRequestsAtivo, requestsAtivo);
      const pageNumber = requestsRecovery;
      if (new URL(route.request().url()).searchParams.has('antes')) pagesBeforeCursor += 1;
      try {
        const response = await route.fetch();
        if (pageNumber === 2) {
          const cursor = new URL(route.request().url()).searchParams.get('antes')!;
          const cursorPayload = JSON.parse(Buffer.from(cursor.slice(3), 'base64url').toString('utf8')) as { m: string };
          const min = BigInt(`0x${cursorPayload.m.replaceAll('-', '')}`);
          const max = BigInt(`0x${fixture.expectedIds.at(-1)!.replaceAll('-', '')}`);
          lateId = ((min + max) / 2n).toString(16).padStart(32, '0').replace(/(.{8})(.{4})(.{4})(.{4})(.{12})/, '$1-$2-$3-$4-$5');
          expect(lateId > cursorPayload.m).toBe(true);
          expect(lateId < fixture.expectedIds.at(-1)!).toBe(true);
          expect(fixture.expectedIds).not.toContain(lateId);
          const lateTie = await request.post(`${FIXTURES}/late-tie`, { data: { conversationId: fixture.conversationId, id: lateId, createdAt: piso } });
          expect(lateTie.status()).toBe(201);
          for (let i = 1; i <= 10; i += 1) {
            await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-dirty-${i}`, text: `evento coalescido ${i}` });
          }
          await expect.poll(() => mensagensRecebidas).toBe(11);
          aguardeSegundaPagina();
          await continua;
        } else if (pageNumber === 3) {
          expect(new URL(route.request().url()).searchParams.has('antes')).toBe(false);
          aguardeTerceiraPagina();
          const webhook = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-dirty-after-third-page-start', text: 'evento depois de iniciar a terceira consulta' });
          expect(webhook.status).toBe(200);
          await expect.poll(() => mensagensRecebidas).toBe(12);
        }
        await route.fulfill({ response });
      } finally {
        requestsAtivo -= 1;
      }
    });
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-head-H', text: 'nova cabeça H maior que T' });
    await segundaPagina;
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
    liberar();
    await terceiraPagina;
    await expect.poll(() => requestsRecovery).toBe(3);
    await expect.poll(() => requestsAtivo).toBe(0);
    expect(maxRequestsAtivo).toBe(1);
    await page.waitForTimeout(250);
    expect(requestsRecovery).toBe(3);
    captureRequests = false;
    for (let i = 0; i < 12 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i++) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(100);
    }
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toContain(lateId);
    expect(expected.unreadCount).toBe(12);
  });

  test('falhas de recuperação consomem o orçamento e exigem continuação explícita', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251, true);
    const attemptsStarted: Array<() => void> = [];
    const attemptSignals = Array.from({ length: 3 }, () => new Promise<void>((resolve) => attemptsStarted.push(resolve)));
    const releases: Array<() => void> = [];
    const gates = Array.from({ length: 3 }, () => new Promise<void>((resolve) => releases.push(resolve)));
    let attempts = 0;
    let inFlight = 0;
    let maxInFlight = 0;
    let recoveryRequests = 0;
    let failFirstThree = true;
    const path = `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route((url) => url.pathname === path, async (route) => {
      const url = new URL(route.request().url());
      if (!url.searchParams.has('marcarLida') || url.searchParams.get('marcarLida') !== 'false') return route.continue();
      recoveryRequests += 1;
      inFlight += 1;
      maxInFlight = Math.max(maxInFlight, inFlight);
      const currentAttempt = recoveryRequests;
      try {
        const response = await route.fetch();
        if (failFirstThree && currentAttempt <= 3) {
          attempts += 1;
          attemptsStarted[currentAttempt - 1]();
          await gates[currentAttempt - 1];
          await route.abort('failed');
        } else {
          await route.fulfill({ response });
        }
      } finally {
        inFlight -= 1;
      }
    });

    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-fail-budget-start', text: 'inicia atualização com resposta que falha' });
    for (let i = 0; i < 3; i += 1) {
      await attemptSignals[i];
      const event = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-fail-budget-dirty-${i}`, text: `evento durante falha ${i + 1}` });
      expect(event.status).toBe(200);
      releases[i]();
    }

    await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
    expect(attempts).toBe(3);
    expect(recoveryRequests).toBe(3);
    expect(maxInFlight).toBe(1);
    await page.waitForTimeout(300);
    expect(recoveryRequests).toBe(3);

    failFirstThree = false;
    for (let i = 0; i < 8 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(100);
    }
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
    await expect(page.getByRole('alert')).toHaveCount(0);
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(expected.unreadCount).toBe(4);
    expect(maxInFlight).toBe(1);
  });

  test('erro no cursor histórico reinicia pela cabeça após evento novo', async ({ page, request }) => {
    let mensagensRecebidas = 0;
    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
      try {
        if ((JSON.parse(String(payload)) as { tipo?: string }).tipo === 'mensagem') mensagensRecebidas += 1;
      } catch { /* frames de conexão não representam mensagens */ }
    }));
    const fixture = await abrirTimeline(page, request, 251, true);
    let liberarFalha!: () => void;
    let iniciarPagina!: () => void;
    const barreira = new Promise<void>((resolve) => { liberarFalha = resolve; });
    const paginaIniciada = new Promise<void>((resolve) => { iniciarPagina = resolve; });
    let requestsRecentes = 0;
    let requestsHistoricos = 0;
    let inFlight = 0;
    let maxInFlight = 0;
    const path = `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route((url) => url.pathname === path, async (route) => {
      const url = new URL(route.request().url());
      if (url.searchParams.get('marcarLida') !== 'false') return route.continue();
      const historica = url.searchParams.has('antes');
      if (historica) requestsHistoricos += 1;
      else requestsRecentes += 1;
      inFlight += 1;
      maxInFlight = Math.max(maxInFlight, inFlight);
      try {
        const response = await route.fetch();
        if (historica && requestsHistoricos === 1) {
          iniciarPagina();
          await barreira;
          await route.abort('failed');
        } else {
          await route.fulfill({ response });
        }
      } finally {
        inFlight -= 1;
      }
    });

    try {
      await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-cursor-failure-head', text: 'cabeça antes da falha histórica' });
      await expect.poll(() => mensagensRecebidas).toBe(1);
      await paginaIniciada;
      const secondEvent = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-cursor-failure-during-page', text: 'nova cabeça durante falha histórica' });
      expect(secondEvent.status).toBe(200);
      await expect.poll(() => mensagensRecebidas).toBe(2);
      liberarFalha();

      await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
      await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
      await expect.poll(() => requestsRecentes).toBe(2);
      await expect.poll(() => inFlight).toBe(0);
      expect(requestsHistoricos).toBe(1);
      expect(maxInFlight).toBe(1);

      for (let i = 0; i < 8 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
        await page.getByRole('button', { name: 'Continuar atualização' }).click();
        await page.waitForTimeout(100);
      }
      await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
      await expect(page.getByRole('alert')).toHaveCount(0);
      const expected = await audit(request, fixture.conversationId);
      const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
      expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
      expect(expected.unreadCount).toBe(2);
      expect(maxInFlight).toBe(1);
    } finally {
      liberarFalha();
      await page.unrouteAll({ behavior: 'wait' });
    }
  });

  test('sucesso da recuperação não apaga erro mais recente de envio', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251, true);
    let liberarRetry!: () => void;
    let iniciarRetry!: () => void;
    const retryGate = new Promise<void>((resolve) => { liberarRetry = resolve; });
    const retryStarted = new Promise<void>((resolve) => { iniciarRetry = resolve; });
    let recoveryRequests = 0;
    let sendsAborted = 0;
    const path = `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route((url) => url.pathname === path, async (route) => {
      if (route.request().method() === 'POST') {
        sendsAborted += 1;
        await route.abort('failed');
        return;
      }
      const url = new URL(route.request().url());
      if (url.searchParams.get('marcarLida') !== 'false') return route.continue();
      recoveryRequests += 1;
      const response = await route.fetch();
      if (recoveryRequests === 1) {
        await route.abort('failed');
      } else if (recoveryRequests === 2) {
        iniciarRetry();
        await retryGate;
        await route.fulfill({ response });
      } else {
        await route.fulfill({ response });
      }
    });

    try {
      await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-recovery-error-owner', text: 'evento que inicia a recuperação falha' });
      await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
      await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await retryStarted;

      await page.getByPlaceholder('Escreva uma resposta').fill('envio abortado durante retry');
      await page.getByRole('button', { name: 'Enviar' }).click();
      await expect(page.getByRole('alert')).toHaveText('Falha ao enviar mensagem.');
      expect(sendsAborted).toBe(1);

      liberarRetry();
      for (let i = 0; i < 8 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
        await page.getByRole('button', { name: 'Continuar atualização' }).click();
        await page.waitForTimeout(100);
      }
      await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
      await expect(page.getByRole('alert')).toHaveText('Falha ao enviar mensagem.');
      const expected = await audit(request, fixture.conversationId);
      const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
      expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
      expect(expected.unreadCount).toBe(1);
      expect(expected.messages.some((message: { content: string }) => message.content === 'envio abortado durante retry')).toBe(false);
    } finally {
      liberarRetry();
      await page.unrouteAll({ behavior: 'wait' });
    }
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
    test.setTimeout(30_000);
    const fixture = await abrirTimeline(page, request, 251);
    const secundaria = fixture.otherConversationId;
    const outraBu = fixture.otherBuConversationId;
    const populateSecondary = await request.post(`${FIXTURES}/burst`, { data: { conversationId: secundaria, count: 80, createdAt: Date.now() - 10_000 } });
    const populateOtherBu = await request.post(`${FIXTURES}/burst`, { data: { conversationId: outraBu, count: 80, createdAt: Date.now() - 10_000 } });
    expect(populateSecondary.status()).toBe(201);
    expect(populateOtherBu.status()).toBe(201);

    const holdRequest = async (conversationId: string, method: 'POST' | 'GET', fail = false) => {
      let release!: () => void;
      let started!: () => void;
      let settled!: () => void;
      const gate = new Promise<void>((resolve) => { release = resolve; });
      const received = new Promise<void>((resolve) => { started = resolve; });
      const finished = new Promise<void>((resolve) => { settled = resolve; });
      const predicate = (url: URL) => url.pathname === `/api/bff/conversations/${conversationId}/messages` && (method === 'POST' ? url.search === '' : url.searchParams.has('antes'));
      await page.route(predicate, async (route) => {
        if (route.request().method() !== method) return route.continue();
        if (method === 'GET' && !new URL(route.request().url()).searchParams.has('antes')) return route.continue();
        try {
          const response = fail ? undefined : await route.fetch();
          started();
          await gate;
          if (fail) await route.abort('failed');
          else await route.fulfill({ response });
        } finally {
          settled();
        }
      });
      return { predicate, started: received, release, finished, remove: () => page.unroute(predicate) };
    };

    const destinationSnapshot = async (draftText: string) => {
      const draft = page.getByPlaceholder('Escreva uma resposta');
      await expect(draft).toBeVisible();
      await draft.fill(draftText);
      const timeline = page.locator('.bolhas');
      const scrollTop = await timeline.evaluate((el) => {
        el.scrollTop = Math.min(120, el.scrollHeight - el.clientHeight);
        return el.scrollTop;
      });
      return {
        draftText,
        active: await page.locator('.item.ativo').innerText(),
        metadata: await page.locator('.inbox > .cartao.grade .linha').first().innerText(),
        ids: await timeline.evaluate((el) => [...el.querySelectorAll<HTMLElement>('.bolha')].map((item) => item.dataset.messageId)),
        scrollTop,
      };
    };
    const expectDestinationUnchanged = async (snapshot: Awaited<ReturnType<typeof destinationSnapshot>>) => {
      expect((await page.locator('.item.ativo').innerText()).replace(/\s+/g, ' ').trim()).toBe(snapshot.active.replace(/\s+/g, ' ').trim());
      expect((await page.locator('.inbox > .cartao.grade .linha').first().innerText()).replace(/\s+/g, ' ').trim()).toBe(snapshot.metadata.replace(/\s+/g, ' ').trim());
      await expect(page.getByPlaceholder('Escreva uma resposta')).toHaveValue(snapshot.draftText);
      await expect(page.getByRole('alert')).toHaveCount(0);
      const timeline = page.locator('.bolhas');
      expect(await timeline.evaluate((el) => [...el.querySelectorAll<HTMLElement>('.bolha')].map((item) => item.dataset.messageId))).toEqual(snapshot.ids);
      expect(await timeline.evaluate((el) => el.scrollTop)).toBe(snapshot.scrollTop);
    };
    const openConversation = async (name: string, tab: 'Na fila' | 'Em atendimento' = 'Na fila', count = 50) => {
      await page.getByRole('button', { name: tab }).click();
      await page.getByRole('button', { name }).click();
      await expect(page.locator('.bolha')).toHaveCount(count);
    };
    const openOtherBu = async () => {
      await page.getByLabel('Business Unit').selectOption(fixture.otherBusinessUnitId);
      await page.getByRole('button', { name: 'Na fila' }).click();
      await page.getByRole('button', { name: 'Cliente Outra BU' }).click();
      await expect(page.locator('.bolha')).toHaveCount(50);
    };
    const sendAndSwitch = async (context: 'conversation' | 'bu', fail: boolean, text: string, draftText: string) => {
      const hold = await holdRequest(secundaria, 'POST', fail);
      const input = page.getByPlaceholder('Escreva uma resposta');
      await input.fill(text);
      await page.getByRole('button', { name: 'Enviar' }).click();
      try {
        await hold.started;
        if (context === 'conversation') await openConversation('Cliente Timeline', 'Na fila', 50);
        else await openOtherBu();
        const snapshot = await destinationSnapshot(draftText);
        hold.release();
        await hold.finished;
        await page.waitForTimeout(100);
        await expectDestinationUnchanged(snapshot);
        return snapshot;
      } finally {
        hold.release();
        await hold.remove();
      }
    };

    await openConversation('Cliente Secundário');
    await sendAndSwitch('conversation', false, 'envio antigo sucesso conversa', 'rascunho destino conversa');
    const afterSuccess = await audit(request, secundaria);
    expect(afterSuccess.messages.some((m: { content: string; direction: string }) => m.content === 'envio antigo sucesso conversa' && m.direction === 'OUT')).toBe(true);

    await openConversation('Cliente Secundário', 'Em atendimento');
    await sendAndSwitch('conversation', true, 'envio antigo falho conversa', 'rascunho apos falha conversa');
    const afterFailure = await audit(request, secundaria);
    expect(afterFailure.messages.some((m: { content: string }) => m.content === 'envio antigo falho conversa')).toBe(false);

    const holdBackfillConversation = await holdRequest(fixture.conversationId, 'GET');
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    try {
      await holdBackfillConversation.started;
      await openConversation('Cliente Secundário', 'Em atendimento');
      const backfillDestination = await destinationSnapshot('rascunho apos backfill conversa');
      holdBackfillConversation.release();
      await holdBackfillConversation.finished;
      await expectDestinationUnchanged(backfillDestination);
    } finally {
      holdBackfillConversation.release();
      await holdBackfillConversation.remove();
    }

    await sendAndSwitch('bu', false, 'envio antigo sucesso BU', 'rascunho destino BU');
    const buSuccess = await audit(request, secundaria);
    expect(buSuccess.messages.some((m: { content: string; direction: string }) => m.content === 'envio antigo sucesso BU' && m.direction === 'OUT')).toBe(true);

    await page.getByLabel('Business Unit').selectOption(fixture.businessUnitId);
    await openConversation('Cliente Secundário', 'Em atendimento');
    await sendAndSwitch('bu', true, 'envio antigo falho BU', 'rascunho apos falha BU');
    const buFailure = await audit(request, secundaria);
    expect(buFailure.messages.some((m: { content: string }) => m.content === 'envio antigo falho BU')).toBe(false);

    await page.getByLabel('Business Unit').selectOption(fixture.businessUnitId);
    await openConversation('Cliente Timeline', 'Na fila', 50);
    const holdBackfillBu = await holdRequest(fixture.conversationId, 'GET');
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    try {
      await holdBackfillBu.started;
      await openOtherBu();
      const otherBuSnapshot = await destinationSnapshot('rascunho apos backfill BU');
      holdBackfillBu.release();
      await holdBackfillBu.finished;
      await expectDestinationUnchanged(otherBuSnapshot);
    } finally {
      holdBackfillBu.release();
      await holdBackfillBu.remove();
    }
  });
});

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

## Current validation/source/freshness attestation summary
```json
{
  "task": "ST-ATT-01 inbox timeline pagination executor evidence",
  "capturedAtUtc": "2026-10-15T05:00:49.228940+00:00",
  "runtimeAndDatabase": {
    "node": "22.23.3",
    "postgres": "PostgreSQL 16.14",
    "database": "leadshug_timeline_20261014",
    "migrations": 17,
    "endpoint": "postgresql://timeline-postgres:5432/leadshug_timeline_20261014 (credentials redacted)",
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
      "diffSha256": "fcd20d7351338a4703340664f0033fb76e3185fa2cc8f90a93b998bbdf4aa199",
      "manifestSha256": "dac1c005db2bde9fb82951ee4b06af69c9cb770c67d7a1fd4ef539a497bb5981",
      "files": [
        {
          "path": "e2e/timeline-freshness.ts",
          "sha256": "ad41153df34c53f6674325b72887e701259ba7a8e752afd38ff4cdd8728c4cd0"
        },
        {
          "path": "e2e/timeline.spec.ts",
          "sha256": "36e51ccf9df361ff0f6704660cdf3fe86b821b4845e264a649c9d2583e0e1e4e"
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
          "sha256": "c499895fee74325e5357052186dd5de9d46c7bc867174e614a9950009ced57ae"
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
    "manifestRecheckAfterRuns": "All API/Web entries match both immutable revision 6 attestations and current checkout; no mismatch.",
    "gitDiffCheck": "passes with cr-at-eol whitespace configuration; project files use CRLF"
  },
  "buildFreshness": {
    "fullRunId": "web-authority-revision6-final-full-20261015",
    "capturedAtUtc": "2026-10-15T04:59:11.580Z",
    "frcRunId": "web-authority-revision6-final-frc3-20261015",
    "frcCapturedAtUtc": "2026-10-15T05:00:22.318Z",
    "apiHealth": 200,
    "fixtureHealth": 200,
    "preview": 200,
    "servedBundle": "/assets/index-BFoOk2qo.js",
    "servedBundleSha256": "7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2",
    "distBundleSha256": "7cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2",
    "sameServedAssetForFrc": true,
    "fullAttestation": "attestation-browser-web-authority-revision6-final-full-20261015.json",
    "frcAttestation": "attestation-browser-web-authority-revision6-final-frc3-20261015.json",
    "attestationSha256": {
      "attestation-browser-web-authority-revision6-final-full-20261015.json": "d65dd1e089196fe83cdf2b3b4fc47d5208af28a55a89da45793b11013edf7270",
      "attestation-browser-web-authority-revision6-final-frc3-20261015.json": "e63c9fe324edd2a390051aad88bd0d494ac71ec2856a2b2a756af12aae5731ae"
    }
  },
  "apiAuthority": {
    "command": "npm run prisma:generate && npm run lint && npm run build && npm test (API E2E remains the unchanged authoritative 224/224 run)",
    "exitCode": 0,
    "unitTests": {
      "files": 17,
      "passed": 115,
      "failed": 0,
      "stdoutPersisted": true,
      "log": "api-ci-light-revision2-20261015.log"
    },
    "e2e": {
      "files": 20,
      "passed": 224,
      "failed": 0,
      "durationSeconds": 111.92,
      "log": "api-e2e-authority.log",
      "sourceUnchanged": true
    },
    "runtimeLog": "api-runtime-authority.txt",
    "note": "Raw stdout retained for all four commands against unchanged API source; API E2E not repeated.",
    "revision2LightCommands": [
      {
        "command": "npm run prisma:generate",
        "exitCode": 0
      },
      {
        "command": "npm run lint",
        "exitCode": 0
      },
      {
        "command": "npm run build",
        "exitCode": 0
      },
      {
        "command": "npm test",
        "exitCode": 0,
        "files": 17,
        "passed": 115,
        "failed": 0
      }
    ],
    "revision2Log": "api-ci-light-revision2-20261015.log",
    "revision2LogSha256": "07f3536876fff3e4bf1e6e8caa39ed0215422b44daa6c52b138384b4797ef270"
  },
  "webAuthority": {
    "unit": {
      "command": "npm test",
      "exitCode": 0,
      "files": 3,
      "passed": 20,
      "failed": 0,
      "log": "web-authority-revision6-final-full-20261015.log"
    },
    "browser": {
      "command": "npm run test:tela",
      "exitCode": 0,
      "passed": 36,
      "failed": 0,
      "duration": "1.0m",
      "log": "web-authority-revision6-final-full-20261015.log"
    },
    "frc": {
      "command": "npx playwright test e2e/timeline.spec.ts --grep=\"preserva o piso T\" --repeat-each=3",
      "exitCode": 0,
      "passed": 3,
      "failed": 0,
      "realWebhookTriggersPerRepeat": 10,
      "log": "web-authority-revision6-final-frc3-20261015.log"
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
    },
    "revision2Targeted": {
      "archRecoveryRegressions": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"(abertura|thread vazia|piso T)\"",
        "exitCode": 0,
        "passed": 3,
        "log": "web-arch-targeted-second.log"
      },
      "contextRaces": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"troca de conversa e BU\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-context-revision2-target-20261015b.log"
      },
      "contextCoverage": "Both conversation and BU switches cover delayed old-send success, aborted old-send network failure, and delayed real backfill. Destination draft, error absence, IDs/messages, metadata, selection and scroll remain asserted."
    },
    "revision3Targeted": {
      "failedRecoveryBudget": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"falhas de recuperação consomem\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-revision3-failed-budget-target-20261015b.log"
      },
      "historicalCursorRestart": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"erro no cursor histórico\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-revision3-cursor-failure-target-20261015.log"
      },
      "contextRaces": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"troca de conversa e BU\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-context-revision2-target-20261015b.log"
      }
    },
    "revision4Targeted": {
      "recoveryErrorLifecycle": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"(falhas de recuperação consomem|erro no cursor histórico|sucesso da recuperação não apaga)\"",
        "exitCode": 0,
        "passed": 3,
        "failed": 0,
        "log": "web-revision4-error-lifecycle-target-20261015.log"
      },
      "expectedAlerts": "Both recovery failure tests assert alert visible before Continue and absent after successful coverage; a separate test asserts a newer send failure remains visible after coverage."
    },
    "revision5Targeted": {
      "command": "npm run build && npx playwright test e2e/timeline.spec.ts --grep=\"(reconecta durante a abertura retida|retoma thread vazia após evento entre rodadas)\"",
      "exitCode": 0,
      "passed": 2,
      "failed": 0,
      "log": "web-revision5-targeted-discriminating-20261015.log",
      "openingReconnect": "The actual initial GET response was held after backend fetch. The native WebSocket was closed through a source-injected reference; a second real authenticated server `conectado` frame was required before releasing the opening response. No later message event or clock advance; recent read-neutral fetch recovered new persisted IDs and preserved unread.",
      "emptyPausedRestart": "160-message backlog predates two real inbound events. The first post-event Continue request is asserted to be marcarLida=false and without antes; all 162 ordered IDs and unread=2 are checked, plus visible IN_SERVICE status after a real BFF claim during the pause."
    },
    "revision6Targeted": {
      "command": "npm run build && npx playwright test e2e/timeline.spec.ts --grep=\"(reconecta durante a abertura retida|retoma thread vazia após evento entre rodadas)\"",
      "exitCode": 0,
      "passed": 2,
      "failed": 0,
      "log": "web-revision6-targeted-20261015.log",
      "openingReconnect": "First authenticated connected frame is awaited before clicking/opening; the initial real GET is held after backend fetch; silent PG growth follows; native established socket is closed and the second authenticated frame is awaited before releasing the opening response. Recovery has no later message event or clock advance, is read-neutral without cursor, and verifies full IDs/unread."
    }
  },
  "revision4Finding": {
    "ARCH-DEL-04": "Recovery errors are versioned by owner and generation. Successful completion clears only the recovery-owned error if its exact version is still current. Other action starts, clears and errors advance the shared error version and invalidate the recovery marker, so late recovery completion cannot clear a newer unrelated error.",
    "targetedProof": "Budget failure and historical cursor failure regressions assert old recovery alert removal after completion. A real network-aborted send during held successful retry produces `Falha ao enviar mensagem.`; after recovery completes and full ordered IDs are recovered, that newer error remains visible and no outbound row was persisted.",
    "testDevelopment": "Test-after implementation; no retroactive TDD claim."
  },
  "revision6Evidence": {
    "finding": "ARCH-DEL-03-EVID causal sequencing",
    "targetedRun": "web-revision6-targeted-20261015.log",
    "negativeControl": {
      "mutation": "Preserved first onopen callback, suppressed callback for every subsequent socket open.",
      "result": "Expected failure after opening response release: zero recovery requests observed, so no message head recovery occurred.",
      "exitCode": 1,
      "log": "web-revision6-reconnect-negative-control-20261015.log",
      "restore": "tempoReal.ts restored byte-exactly before canonical full run.",
      "restoreProof": "expectedSha256=118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf\nrestoredSha256=118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf\nrestoredBytesExact=True"
    },
    "sourceChange": "Test-only ordering change in e2e/timeline.spec.ts; runtime/API sources unchanged from revision 5.",
    "testDevelopment": "Test-after evidence repair; no retroactive TDD claim.",
    "runExitFiles": [
      "web-authority-revision6-final-full-20261015.exit",
      "web-authority-revision6-final-frc3-20261015.exit",
      "web-revision6-targeted-20261015.exit",
      "web-revision6-reconnect-negative-control-20261015.exit"
    ]
  }
}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/verification-debt-pre-final6.log
```
Verification Debt Audit
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker
TODO: /mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md
Outcome heuristic: high
Inline code TODO debt classification: none

Waiver / skip signals:
  - 1:# TODO LeadsHug histórico completo e paginado na inbox
  - 9:Histórico completo e paginado na inbox do LeadsHug.
  - 21:A thread da inbox busca as primeiras 200 mensagens em ordem crescente, sem metadados de continuação. Uma conversa longa oculta mensagens recentes. A tela Consultar já pagina, mas atende outro contrato e não marca leitura. Esta entrega torna todo o histórico acessível na inbox, preservando BU, sessão, janela de resposta e autoria.
  - 28:- **Direct-to-TODO rationale:** n/a; há feature brief para o pacote
  - 36:- **Current delivery:** leitura paginada da thread BFF e navegação incremental na inbox
  - 50:- **Why this state now:** produto aceito na aderência; último gap de reconexão isolado com primeiroframe antes do clique e negativo reconnect-only que falha. Web20/36,FRC3 e fonte6 congelados para revisão.
  - 56:- [x] Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor.
  - 69:- Sessão e grant ATENDENTE ou superior na BU; resolver/autorizar a conversa antes de validar ou consultar cursores. Sem sessão: 401. Recurso fora do escopo: 404, inclusive com query/cursor malformado.
  - 75:- Cursor versionado identifica a mensagem-âncora; resolver seus dados somente na conversa autorizada. Paginação anterior usa comparação estrita do par, busca no máximo N+1 registros e nunca escreve não lidas.
  - 82:- Na atualização, capturar uma fronteira fixa T igual ao timestamp da mensagem mais recente conhecida antes da passagem. Buscar página recente sem marcar leitura e caminhar para trás até alcançar timestamp estritamente menor que T, ou esgotar mensagens. Incluir integralmente o grupo empatado em T; encontrar um ID conhecido não encerra a recuperação.
  - 106:- `n/a once moved out of active`: use after the TODO moves to `promotion_lane/` or `completed/`.
  - 110:n/a; nenhuma entrega parcial é reivindicada.
  - 114:n/a; nenhuma decisão material bloqueando execução no início.
  - 119:- **Promotion lane path:** branches locais -> validação local -> evidência/closeout na Foundation; deploy e promoção remota de código fora do recorte
  - 120:- **Lane-promoted threshold for this TODO:** n/a; entrega local validada
  - 249:- [x] VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos.
  - 263:| SCOPE-02 | Scope | Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor. | PostgreSQL integration | test/atendimento.e2e-spec.ts:317,365,371; api-e2e-authority.log | Node22 / PG16 descartável | passed | Cursor alheio em recurso autorizado400; recurso sem grant404 antes da query; sem sessão401; unread readback preservado. |
  - 264:| SCOPE-03 | Scope | Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282; api-e2e-authority.log | Node22 / PG16 descartável | passed | 251 IDs, limite37 e grupo empatado; comparação de IDs na ordem real do banco, página recente e continuação bounded. |
  - 280:| VAL-03 | Validation Steps | VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282,317,365,371; api-e2e-authority.log | PG16 dedicado | passed | 251 IDs e empates; negativos scoped e consulta inválida sem efeitos de leitura. |
  - 328:- Primeiro recorte BFF de mensagens na inbox; API pública, Consultar e demais stories ficam fora.
  - 330:- Marcação atômica antes da consulta somente na abertura humana; refresh/backfill/recuperação são explicitamente read-neutral.
  - 341:| Grants materializados na BU | modules/identity-and-tenancy.md | preserved | Negativos de tenant/BU no banco real. |
  - 390:- **Adherence review evidence:** delivery-adherence-round-1.json → delivery-adherence-delta.json → delivery-adherence-resolution.json, todos internos gpt-6.1-sol/max no-context, terminais turn.completed/schema/merge. ARCH-DEL-01..04/ERR corrigidos e aceitos, sem novo desvio. Revision5 altera apenas provas browser requeridas pela TQA; conservar parecer por identidade dos fontes de produto. Pacotes imutáveis generation1/revision3/revision4 em evidence/. Nenhum waiver.
  - 401:- **Waiver authority / reference (required if waived):** none
  - 408:- **Waiver authority / reference (required if waived):** none
  - 416:n/a; nenhum ID de pattern é reivindicado.
  - 460:Compatibilidade de representação: completion guard lê status na coluna5, authority guard na coluna7. Os mesmos resultados são espelhados como Status/Authority status; notas permanecem na coluna8. Nenhuma validação ou comando é substituído.
  - 493:Custo do grupo empatado é medido e cada rodada limitada; inserções concurrentes exigem nova passagem e UI de recuperação. Runners e suites serão provados na implementação. Nenhuma suite green ou aprovação material é presumida.
  - 522:| high_severity_plan_review_issue | yes | ARCH-TL-01..03 reportados e integrados na proposta |
  - 534:- **Waiver authority / reference:** none
  - 538:| ARCH-TL-03 | Integrated | useful | yes | project | n/a | Piso pendente T conservado entre passagens/dirty/retry e promoção somente após cobertura sem evento pendente; crítica delta critique-resolution.json confirmou a resolução do plano, agora testada no browser. |
  - 547:- **Findings summary:** revisão independente confirmou A-01/A-02/A-04/A-05 e, no delta, A-03 na query própria do controller público.
  - 549:- **Waiver authority / reference:** none
  - 567:| delphi-ai/rules/stacks/nestjs/nestjs-architecture-always-on.md | API | input runtime e serviço de domínio | regra de negócio na UI | Validar cursor/limites |
  - 607:| inbox-and-conversations / recuperação e contexto | Inbox + timeline + tempoReal | Adherent; código revision4 aceito, mesmo produto na provaWeb36/FRC3; consolidar Verified local apósTQA. |
  - 616:| CI API local | Leaf scripts do job tocado | passed | evidence/api-ci-light-revision2-20261015.log; evidence/api-e2e-authority.log; test-surface-admission.md | 0 falhas na execução final | generate/lint/build/unit115 e PostgreSQL224 adicionais, serializados. |
  - 631:| ARCH-TL-01..03 | high | release-blocker | fix in current TODO | Contrato de leitura/recuperação pertence à mesma story | fixed | architecture-review.json e Proposed API Contract, a verificar na crítica |
  - 632:| ARCH-TL-04..06 | medium | release-blocker | fix in current TODO | Estado/consulta/provas necessários ao mesmo contrato | fixed | architecture-review.json e testes planejados, a verificar na crítica |
  - 633:| ARCH-DEL-01 | medium | release-blocker | fix in current TODO | Budget3 por rodada deve abranger coalescing; evento não renova automaticamente consultas | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |
  - 634:| ARCH-DEL-02 | medium | release-blocker | fix in current TODO | Thread inicialmente vazia e notificação entre rodadas devem conservar restart pendente até fetch recente | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |
  - 635:| ARCH-DEL-03 | medium | release-blocker | fix in current TODO | Notificação durante abertura pertence à geração selecionada e deve recuperar sem esperar outroevento/poll | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |
  - 639:| ARCH-DEL-01-ERR | medium | release-blocker | fix with ARCH-DEL-01 | Variante objetiva: saldo era debitado após await; falha+dirty não debitava e permitia mais de3tentativas. Consumir no despacho e provar3aborts+eventos sem4aautomática; erro histórico com dirty deve conservar restart recente, não consumir a notificação ao retomar cursor antigo | fixed | delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada. |
  - 643:| ARCH-DEL-02-EVID | medium | release-blocker | repair tests in current TODO | TQA delta: burst futuro tornava IN mais antigo e cursor velho ainda alcançava IDs; semear passado, assert headread no resume e controle negativo | fixed | delivery-tqa-resolution.json aceitou pastbacklog/headread/metadata/negativeoldcursor na revision5. |
  - 657:- Autorizar primeiro; resolver cursor na conversa; limitar sua forma/tamanho e queries. Testar cursor de outra conversa autorizada, outra BU sem grant no mesmo tenant e outro tenant, separadamente.
  - 666:- **Why this level:** paginação e cursores alteram queries; abertura e entrada concorrem na contagem de não lidas; contexto/realtime/ações assíncronas atualizam o histórico visível. Nenhuma promessa de SLO/capacidade foi aprovada.
  - 668:- Registro de classificação na execução do contrato aprovado; não expande funcionalidade nem reduz obrigações de validação.
  - 753:Auditoria executada: artifacts/reviews/leadshug-inbox-timeline-20261014/verification-debt.md e evidence/verification-debt-pre-final.log. Helper lexical high/exit2 por termos do template/histórico; classificação manual: inline none, nenhum waiver/dívida material escondida de produto/testes. Gates independentes/guardas e consolidação ainda abertos, sem claim de closeout; reavaliar após convergência.
  - 761:- **Evidence / reference:** revisão de entrega após testes completos; pacote de planejamento não substitui TQA. O roteamento technical_review exige gpt-5.6-terra. Na retomada, o catálogo nativo do Codex confirmou esse modelo, embora não seja selecionável via ferramenta collaboration. Será usado o runner interno subagent_review_run.py com o modelo prescrito e effort max; guard específico go em artifacts/tmp/inbox-timeline-execution/routing-tqa-native.json e probe nativo ephemeral/read-only exit0 MODEL_AVAILABLE (native-model-probe-events.jsonl). Exceção/substituição não é necessária e não foi presumida.
  - 762:- **Waiver authority / reference:** none
  - 764:Runner interno gpt-5.6-terra/max coletou round1 e delta3 com turn.completed/schema/merge: delivery-tqa-round-1.json e delivery-tqa-delta.json. TQA-TL-01/TL-02/EVID-03 resolvidos pelo delta; gaps ARCH-DEL-02/03-EVID foram corrigidos nas provas revision5 (pastbacklog+headrequest+status; reconnect real autenticado durante opening retido), Web20/36/FRC3 e negativo oldcursor. Resolução TQA5 terminou, aceitou vazio/metadata/contraprova e preservou correções anteriores; resta isolar reconnect do primeiroonopen, ver delivery-tqa-resolution.json/merge. Nova prova revision6 em execução; dispatch anterior delivery-tqa-resolution-dispatch.json; pacote imutável SHA4dfcd1c55d2d040432e8b7880ed14363159d9b62414039ed118f2b3f84426cc7 em evidence/delivery-tqa-resolution-package-revision5.md. Sem waiver ou substituição de revisão live.
  - 768:| TQA-TL-01 | Integrated | useful | yes | project | n/a | Counts3/max1 e eventos/falhas não renovam saldo; delta3 confirmou. |
  - 769:| TQA-TL-02 | Integrated | useful | yes | project | n/a | Seis destinos conversa/BU×sucesso/falha/backfill com draft/erro/scroll/metadados; delta3 confirmou. |
  - 770:| TQA-EVID-03 | Integrated | useful | no | n/a | n/a | Stdout dos4leafsAPI115 retido; API224 fonte idêntica, delta3 confirmou. |
  - 779:- **Waiver authority / reference:** none
  - 806:n/a; nenhum comentário pendente do usuário neste arquivo.

Blocker / provisional / closure drift signals:
  - 43:- **Current delivery stage:** Pending
  - 84:- Evento durante a recuperação marca uma nova passagem necessária desde a página recente, ainda com o piso pendente T; terminar a caminhada atual não confirma cobertura. Só promover o piso confirmado quando uma passagem atravessar todo T sem evento/trabalho concorrente pendente. Se houver dirty/pending, conservar T e a indicação de atualização, com o mesmo orçamento de três queries por rodada. Não promover pelo máximo da coleção nem por um poll enquanto houver recuperação pendente.
  - 94:- `Pending`: no meaningful delivery milestone has been reached yet.
  - 98:- `Provisional`: delivery is intentionally partial/incomplete but useful for unblocking dependent work.
  - 99:- `Blocked`: work cannot currently proceed; `Blocker Notes` become mandatory.
  - 105:- `blocked`: execution is paused on an explicit blocker; `Blocker Notes` are mandatory.
  - 108:## Provisional Notes (Required if `Qualifiers` includes `Provisional`)
  - 112:## Blocker Notes (Required if `Qualifiers` includes `Blocked`)
  - 320:## Decision Pending (Resolve Before Freeze)
  - 377:| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
  - 629:| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
  - 667:- **Current delivery stage at review time:** Pending
  - 684:- **State transition:** pending -> running -> passed; artefato e medição aceitos no parecer independente delivery-adherence-resolution.json, sem mudança da fonte API.
  - 702:- **State transition:** pending -> running; provas finais revision5 executadas em fonte idêntica, aguardando julgamento independente antes de passed.
  - 712:  - `result_summary`: `Full36/36 and FRC3/3 passed on identical current source/build; shared3-attempt budget incl failures, retained T/restart, opening/empty notifications, six context races and recovery-error ownership covered. Independent delta judgment pending.`
  - 720:- **State transition:** pending -> running -> passed; artefato e medição aceitos no parecer independente delivery-adherence-resolution.json, sem mudança da fonte API.
  - 738:- **State transition:** pending -> running -> passed; artefato e medição aceitos no parecer independente delivery-adherence-resolution.json, sem mudança da fonte API.

Unchecked checklist items:
  - 243:- [ ] DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão.
  - 253:- [ ] VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout.

Inline debt scan paths:
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/src/domain/inbox/conversations.service.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/src/domain/inbox/timeline-pagination.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/src/domain/inbox/timeline-pagination.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/src/surfaces/bff/conversations.controller.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/atendimento.e2e-spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/browser-server.cjs
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/timeline-fixtures.cjs
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline-freshness.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/playwright.config.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/api.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/telas/Inbox.tsx
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/tempoReal.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/tempoReal.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/timeline.test.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/timeline.ts

Inline debt accepted:
  - none

Inline debt canonical-link-missing:
  - none

Inline debt cleanup-required:
  - none

Counts: waiver=55 blocker=17 unchecked=2 accepted_inline=0 canonical_link_missing=0 cleanup_required=0

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision6-final-frc3-20261015.log
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

  ✓  1 e2e/timeline.spec.ts:320:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (2.1s)
  ✓  2 e2e/timeline.spec.ts:320:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.9s)
  ✓  3 e2e/timeline.spec.ts:320:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.9s)

  3 passed (22.1s)
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision6-final-full-20261015.log
```
v22.23.3

> @leadshug/web@0.1.0 test
> vitest run


 RUN  v2.1.9 /workspace/web-app

 ✓ src/timeline.test.ts (2 tests) 11ms
 ✓ src/tempoReal.spec.ts (6 tests) 14ms
 ✓ src/api.spec.ts (12 tests) 91ms

 Test Files  3 passed (3)
      Tests  20 passed (20)
   Start at  04:58:54
   Duration  652ms (transform 301ms, setup 0ms, collect 392ms, tests 117ms, environment 1ms, prepare 284ms)

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
dist/assets/index-BFoOk2qo.js   224.39 kB │ gzip: 69.79 kB
✓ built in 1.30s
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

Running 36 tests using 1 worker

  ✓   1 e2e/telas.spec.ts:78:3 › as telas, no navegador › sem sessão, qualquer URL leva ao login (253ms)
  ✓   2 e2e/telas.spec.ts:84:3 › as telas, no navegador › entrar leva de volta para a página que se queria abrir (982ms)
  ✓   3 e2e/telas.spec.ts:96:3 › as telas, no navegador › conta nova cai no wizard, e a Revisão diz qual é o próximo passo (994ms)
  ✓   4 e2e/telas.spec.ts:138:3 › as telas, no navegador › toda tela do menu abre sem quebrar (1.5s)
  ✓   5 e2e/telas.spec.ts:167:3 › as telas, no navegador › a paleta é a do desenho, e o tema segue a marca da conta (817ms)
  ✓   6 e2e/telas.spec.ts:191:3 › as telas, no navegador › os grupos do menu retraem, e a escolha sobrevive à navegação (972ms)
  ✓   7 e2e/telas.spec.ts:209:3 › as telas, no navegador › o tema é escolha de quem olha, e persiste (1.0s)
  ✓   8 e2e/telas.spec.ts:227:3 › as telas, no navegador › Meu perfil abre pelo rodapé e salva o próprio nome (929ms)
  ✓   9 e2e/telas.spec.ts:246:3 › as telas, no navegador › a foto de perfil sobe, e a recusa do servidor aparece na tela (957ms)
  ✓  10 e2e/telas.spec.ts:276:3 › as telas, no navegador › a barra lateral tem os três grupos do desenho (854ms)
  ✓  11 e2e/telas.spec.ts:290:3 › as telas, no navegador › Setores abre com o Geral, e o Histórico já mostra o que aconteceu (946ms)
  ✓  12 e2e/telas.spec.ts:302:3 › as telas, no navegador › a inbox abre, com o número no seletor e sem conversa nenhuma (860ms)
  ✓  13 e2e/telas.spec.ts:319:3 › as telas, no navegador › Pessoas abre, lista quem já existe e oferece os papéis que existem (942ms)
  ✓  14 e2e/telas.spec.ts:338:3 › as telas, no navegador › adicionar uma pessoa e conceder um setor a ela (965ms)
  ✓  15 e2e/telas.spec.ts:357:3 › as telas, no navegador › convidar mostra o LINK quando o e-mail não sai, e ele leva a definir a senha (972ms)
  ✓  16 e2e/telas.spec.ts:380:3 › as telas, no navegador › esqueci minha senha responde igual, exista a conta ou não (229ms)
  ✓  17 e2e/telas.spec.ts:391:3 › as telas, no navegador › a tela de números mostra a BU e os dois canais desconectados (825ms)
  ✓  18 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (906ms)
  ✓  19 e2e/telas.spec.ts:411:3 › as telas, no navegador › identidade visual carrega e salva os campos pós-onboarding (1.1s)
  ✓  20 e2e/telas.spec.ts:430:3 › as telas, no navegador › Typebot permite buscar, abrir o editor e configurar um gatilho (1.6s)
  ✓  21 e2e/timeline.spec.ts:56:3 › timeline da inbox com backend e PostgreSQL reais › expõe o estado de abertura enquanto a primeira página aguarda o backend (855ms)
  ✓  22 e2e/timeline.spec.ts:90:3 › timeline da inbox com backend e PostgreSQL reais › reconecta durante a abertura retida e lê a cabeça sem novo evento (4.8s)
  ✓  23 e2e/timeline.spec.ts:174:3 › timeline da inbox com backend e PostgreSQL reais › abre a página recente, carrega todas as páginas anteriores e preserva posição (1.3s)
  ✓  24 e2e/timeline.spec.ts:205:3 › timeline da inbox com backend e PostgreSQL reais › reconecta sem evento posterior e recupera 130 mensagens em mais de uma rodada (1.4s)
  ✓  25 e2e/timeline.spec.ts:231:3 › timeline da inbox com backend e PostgreSQL reais › o poll retoma uma rodada pendente sem evento novo nem clique de continuação (1.2s)
  ✓  26 e2e/timeline.spec.ts:253:3 › timeline da inbox com backend e PostgreSQL reais › recupera o histórico completo após uma thread vazia receber mais de uma página (842ms)
  ✓  27 e2e/timeline.spec.ts:266:3 › timeline da inbox com backend e PostgreSQL reais › retoma thread vazia após evento entre rodadas e inclui toda a cabeça sem reler (1.3s)
  ✓  28 e2e/timeline.spec.ts:320:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.8s)
  ✓  29 e2e/timeline.spec.ts:407:3 › timeline da inbox com backend e PostgreSQL reais › falhas de recuperação consomem o orçamento e exigem continuação explícita (1.5s)
  ✓  30 e2e/timeline.spec.ts:472:3 › timeline da inbox com backend e PostgreSQL reais › erro no cursor histórico reinicia pela cabeça após evento novo (1.2s)
  ✓  31 e2e/timeline.spec.ts:544:3 › timeline da inbox com backend e PostgreSQL reais › sucesso da recuperação não apaga erro mais recente de envio (1.1s)
  ✓  32 e2e/timeline.spec.ts:604:3 › timeline da inbox com backend e PostgreSQL reais › preserva a âncora quando uma mensagem chega durante o backfill atrasado (931ms)
  ✓  33 e2e/timeline.spec.ts:637:3 › timeline da inbox com backend e PostgreSQL reais › mescla envio real com autoria e mantém o novo draft digitado durante o envio (858ms)
  ✓  34 e2e/timeline.spec.ts:663:3 › timeline da inbox com backend e PostgreSQL reais › mostra thread vazia/fim, falha recuperável e acesso perdido (2.1s)
  ✓  35 e2e/timeline.spec.ts:689:3 › timeline da inbox com backend e PostgreSQL reais › close vence resposta de backfill atrasada (958ms)
  ✓  36 e2e/timeline.spec.ts:710:3 › timeline da inbox com backend e PostgreSQL reais › troca de conversa e BU protege resposta atrasada de envio (3.6s)

  36 passed (1.0m)

```

## Final review requirements
Assess frozen decision adherence, module consistency, implementation regressions, missing/weak/bypass-prone tests and completeness of terminal full TQA, security/auth/scope/cursor/readstate/ACK invariants, performance/concurrency/operational residuals and source/runtime freshness, verification debt/waivers, P1/P2 and rule-spirit, elegance/structure. Check simple faithful error-version ownership and repaired scheduling transitions; do not redesign outside approved story absent material defect. Current tests directly discriminate empty paused recent-restart with older backlog/metadata, real reconnect-onopen while opening response is held, failed-attempt budget, older-page-error/head restart, six context destinations and alert-ownerclear/newererrorretained. Mutation evidence is supporting test-after, not TDD. Source-owned React npm run test:tela transparently maps generic browser runner; no Flutter, remoteCI, provider transport, SLO or production claim. Explicitly identify any remaining blockers; no gate bypass through procedural final commitments. Return canonical JSON only, findings first with severity/locus/concretecounterexample/whynow/options/recommendation and four axis positions; put complete decision reasoning in overall_assessment/recommended_path.
