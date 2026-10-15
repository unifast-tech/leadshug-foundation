# ST-ATT-01 complete bounded-summary TQA causal resolution, revision6
Fresh internal no-context reviewer, not executor. All previous reviews are objectively TERMINAL. This new packet repairs the single concrete causal evidence gap identified by terminal TQA revision5; no live review was shrunk, replaced or interrupted. Apply the FULL applicable TQA rubric, not merely a yes/no verdict. Carry forward complete prior audits on unchanged loci; challenge any genuinely new regression. This is a bounded-summary as permitted by independent-test-quality-audit-method, with approved expectations, scope, exact implementation/test delta, evidence index, behaviors/DoD, risks, waivers and all required output axes.

UserAPROVADO2026-10-14; frozen Foundation649372fbe81f6cccc0f8902b52fe32e2ecfc061a. API baseline5db3fbe2043428749895fc3ff6441e9457467dd0; Web baseline6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9. Product revision4 has terminal adherence acceptance; revision5/6 change only e2e/timeline.spec.ts. The complete file-to-file delta5→6 is embedded, plus the entire relevant real-browser scenario. Full prior test source/audit packet5 SHA4dfcd1c55d2d040432e8b7880ed14363159d9b62414039ed118f2b3f84426cc7 is retained unchanged in evidence/delivery-tqa-resolution-package-revision5.md. Other test bodies/harness/product source remain byte-identical; all16 current source files are compared by root to both new attestations, and product bundle stays revision4. Full36 browser, Web20unit, required FRC3 use current manifest; API7 identical to API115/224/EPS/BCI/RLS. No remoteCI/deploy/production/SLO/provider certification, no waiver or deferred verification, no worktrees; one code writer.

The previous unresolved finding is ARCH-DEL-03-EVID: initial onopen could invalidate held opening, making reconnect causal routing unproven. Revision6 must require FIRST authenticated connected frame before selecting conversation, then hold actual initialGET, grow DB silently, close native real socket, require SECOND authenticated connected frame while GET is held, release and recover without any later message/poll. A mutation suppressing ONLY reconnect callback while retaining first callback must fail; source must restore byte-exact before canonical runs. Judge that causality and all applicable carried test-quality axes explicitly.

## Frozen/current Scope

- [x] Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API.
- [x] Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor.
- [x] Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores.
- [x] Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID.
- [x] Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada.
- [x] Preservar histórico, cursor histórico, metadados atuais e draft correto durante envio, claim, close, backfill, poll e eventos/reconexão de socket.
- [x] Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens.
- [x] Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo.
- [x] Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado.



## Frozen/current Proposed API Contract

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



## Frozen/current Out of Scope

- Transferência, exclusividade de resposta, SLA, distribuição de agentes, novas equipes e papéis.
- Estados de entrega/leitura/falha e deduplicação de recebimento por externalId.
- Mídia, templates, campanhas, CRM e automações Typebot.
- Mudanças nos contratos da API pública ou da tela Consultar.
- Redesenho da lista de conversas ou paginação da lista; a story cobre mensagens de uma conversa.
- Expansão de infraestrutura, uso de dados reais, integração com runtime legado ou publicação.



## Frozen/current Definition of Done

- [x] DOD-01: contrato aprovado e consolidado no módulo responsável.
- [x] DOD-02: histórico maior que 200 é alcançável sem lacunas/repetições, inicial recente, empates estáticos e inserções empatadas durante recuperação.
- [x] DOD-03: autorização/cursor não permitem outra conversa, BU ou Mantenedora; recurso inacessível é 404 antes de query inválida.
- [x] DOD-04: backfill, envio/refresh/close, troca rápida, reconexão sem evento posterior e recuperação mantêm histórico, posição, cursores, metadados e draft corretos.
- [x] DOD-05: limite/cursor/marcarLida, vazio/fim, falha/retry e recuperação pendente têm contrato/UI verificados; entradas posteriores à fronteira de abertura continuam não lidas.
- [x] DOD-06: suites API/Web/Playwright passam no backend real e banco isolado; plano SQL recente/profundo/empates registra custo e decisão de índice; migrate deploy validado se houver migração.
- [ ] DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão.



## Frozen/current Validation Steps

- [x] VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional.
- [x] VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e.
- [x] VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos.
- [x] VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL.
- [x] VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada.
- [x] VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado.
- [ ] VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout.
- [x] VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha.



## Frozen/current Decision Adherence Validation (Mandatory Before Delivery)

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



## Frozen/current Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Canonical owner / decision | Implementation | Status |
| --- | --- | --- |
| inbox-and-conversations / thread BFF paginada | controller + timeline-pagination + ConversationsService.timeline | Adherent; contrato anterior ao código4cabc467,API224,parecer independente aceito. |
| inbox-and-conversations / recuperação e contexto | Inbox + timeline + tempoReal | Adherent; código revision4 aceito, mesmo produto na provaWeb36/FRC3; consolidar Verified local apósTQA. |
| identity-and-tenancy / BU e grant | Resolver/AccessService existentes | Adherent; nenhuma decisão canônica mudou, negativos reais401/404/400 e readback. |
| audit-and-history / autoria e ações | responder/claim/close existentes | Adherent; autoria/audit preservados, regressões reais e destinations. |



## Frozen/current Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface | Focus | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| Orquestrador / inspeção bounded | API auth/read-state e UI races; runner/frescor | passed | implementation-observations.md; execution-evidence.md; source manifest revision5 | fixed IMPL-01..14 e ARCH-DEL-01-ERR; sem P1/P2 aberto de produto | Correções fiéis comprovadas, produto aceito pela aderência; TQA independente ainda julga provas reforçadas. |
| CI API local | Leaf scripts do job tocado | passed | evidence/api-ci-light-revision2-20261015.log; evidence/api-e2e-authority.log; test-surface-admission.md | 0 falhas na execução final | generate/lint/build/unit115 e PostgreSQL224 adicionais, serializados. |
| Revisão independente | Aderência, segurança, desempenho e provável P1/P2 | running | delivery-adherence-resolution.json; delivery-tqa-delta.json; resoluçãoTQA revision5 live | Produto fixed; duas lacunas de testes corrigidas, aguardando julgamento | Final review e guardas ainda exigidos; não declarar entrega antes da convergência. |



## Frozen/current Rule-Spirit Anti-Pattern Hunt

| Rule Surface | Lens | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| NestJS / parser e limites | Validação runtime, grant antes cursor, ACK e queries bounded | passed | API224; delivery-adherence-resolution.json; scansAPI finais | no findings materiais; hints HTTP acompanhados de readback | Sessão/grants/domínio/PG reais, ACKbarreira e sem mudança público/Consultar. |
| React / Inbox e socket | Owner/generation, piso T, cursor, lifecycle e poll | passed | delivery-adherence-resolution.json; Web36/FRC3; implementation-observations.md | fixed IMPL-01..14,ARCH-DEL-01..04/ERR | Sem cacheframework/fetchall/budgetrenewal; fonte de produto aceita inalterada. |
| Scan heurístico API/Web | Domínios/targets e bypass disfarçado | passed | scan-triage-api.json e scan-triage-web.json; rawscansAPI/Webrev5; aderência aceita | no findings materiais; API30/15 e Web42/21 triados | by-design/no-action para loopback/.test de fixture e regexHTML preexistente, sem allowlist/supressão; TQA é gate separado. |



## Frozen/current Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

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

| ARCH-DEL-02-EVID | medium | release-blocker | repair tests in current TODO | TQA delta: burst futuro tornava IN mais antigo e cursor velho ainda alcançava IDs; semear passado, assert headread no resume e controle negativo | fixed | delivery-tqa-resolution.json aceitou pastbacklog/headread/metadata/negativeoldcursor na revision5. |
| ARCH-DEL-03-EVID | medium | release-blocker | repair tests in current TODO | TQA delta: falta reconnect real enquanto openingGET retido/threadnull; provar read-neutral sem outroevento/poll | open | delivery-tqa-delta.json finding ARCH-DEL-03; callback comum já implementado, gap de prova browser |



## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-tqa-round-1.json
```
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-tqa-dispatch.json","review_kind":"test_quality_audit","reviewer_label":"delivery-tqa-native","overall_assessment":"Test effectiveness is mixed. The package strongly aligns most tests to the approved contract: real Nest/session/grant/PostgreSQL paths, owned fixtures, distinct scope negatives, complete ordered-ID readbacks, real browser/WebSocket flows, fresh served-bundle provenance, and external doubles limited to Meta/Evolution ports. The original-T scenario genuinely combines H>T, partial traversal, late tied UUID insertion, dirty events, and DB/UI ID comparison; the ACK barrier plus failing post-SELECT mutation is strong and honestly test-after rather than retroactive TDD. Status hints are paired with meaningful body/readback assertions, and no authoritative-run skip, focus marker, fake BFF payload, ambient proof subject, or production test hook is evidenced. Test efficiency is acceptable: full project-owned API and browser commands are used, with targeted repeated FRC evidence rather than redundant broad reruns. Performance evidence is mixed: EPS measures representative recent/deep/tied paths and documents the no-index decision, but the deep predicate still filters 10,001 rows locally and establishes no production capacity claim. Operational provenance is otherwise sound (Node 22, disposable PG, source manifests, fresh API/browser builds, served JS equals dist), although API generate/lint/build/unit raw stdout was not retained. The audit cannot pass yet because two explicit recovery/context invariants are asserted only indirectly or not at all.","recommended_path":"Return for focused test repair, not a design rewrite: make recovery page-call budget and single-flight behavior directly observable, then add destination-context assertions for stale draft/error/scroll effects. Rerun the full browser suite and repeated FRC case on the corrected test source. Preserve per-command API CI-equivalent raw logs or machine-readable results on the next authoritative run. Keep the documented EPS deep-scan residual explicit; it does not itself justify an unmeasured index change.","performance_position":"mixed","elegance_position":"acceptable","structural_soundness_position":"mixed","operational_fit_position":"acceptable","findings":[{"finding_id":"TQA-TL-01","severity":"medium","title":"Recovery tests do not directly prove the three-page round budget or single-flight invariant","rationale":"At web-app/e2e/timeline.spec.ts:108, :133, and :168, the pending banner and eventual full-ID equality only infer bounded recovery. With the 382-message setup, an implementation making more than three page requests can still remain pending before it reaches a timestamp below T, and parallel recoveries can deduplicate to the same final IDs. The tests do not count page GETs per round or prove that ten dirty events cannot start a second walk while the delayed walk is in flight. This leaves the approved maximum of three page queries per round and one in-flight pass unprotected.","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"timeline-recovery-observable-round-limits","affected_paths":["web-app/e2e/timeline.spec.ts"],"suggested_action":"Observe actual BFF page requests around a held real response: assert no more than three recovery page GETs before the pending state, and assert no second traversal starts while the held request remains in flight. Then release it, verify Continue/poll starts the next bounded round, and retain the existing full ordered-ID and unread readbacks."},{"finding_id":"TQA-TL-02","severity":"medium","title":"Context-switch race coverage omits target draft, stale-error, and stale-scroll assertions","rationale":"At web-app/e2e/timeline.spec.ts:333, the delayed-send test switches conversation and BU but releases the old response before placing any draft in the destination; it asserts selection, source persistence, and absence of the old bubble only. The delayed-backfill scroll test at :227 remains in the same context, while the same-context draft test at :260 does not exercise generation invalidation. A stale completion, failure, or delayed backfill callback that clears a destination draft, writes its error, or adjusts its scroll after a context switch could therefore pass despite the explicit contract requiring those effects to be ignored.","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"timeline-context-generation-observable-effects","affected_paths":["web-app/e2e/timeline.spec.ts"],"suggested_action":"Extend real-response race tests to switch context, type a destination draft, capture destination scroll/state, then release both prior success and failure/backfill responses. Assert the destination draft, error state, messages, metadata, and scroll remain unchanged for both conversation and BU changes."},{"finding_id":"TQA-EVID-03","severity":"low","title":"API CI-equivalent non-E2E command output is attested but not retained","rationale":"execution-evidence.md and executor-final-summary.json attest successful prisma generate, lint, build, and 115 API unit tests, but explicitly state that their raw stdout was not preserved. The retained E2E and browser logs are strong complementary evidence, but they do not independently demonstrate unit-test discovery or lint/build output for the frozen source.","category":"operational_fit","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"ci-equivalent-command-output-retention","affected_paths":["foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md","foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/executor-final-summary.json"],"suggested_action":"On the next authoritative run, retain immutable per-command stdout or machine-readable test reports with command, exit status, source manifest, and run identifier; keep the executor attestation as an index rather than the sole record."}]}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-tqa-delta.json
```
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-tqa-delta-dispatch.json","review_kind":"test_quality_audit","reviewer_label":"delivery-tqa-delta-native-no-context","overall_assessment":"Return for focused test-evidence repair. TQA-TL-01 is resolved: final-source browser tests directly count three requests, maximum one in flight, third-request dirty behavior, failure-budget consumption, explicit continuation, and complete ID/unread readback; the post-await-debit negative control fails 3 versus 5. The dirty historical-cursor restart has an equally discriminating negative control. TQA-TL-02 is resolved through the six real destination cases covering conversation/BU times delayed send success, network failure, and backfill with draft, error, IDs, metadata, selection, and scroll assertions. TQA-EVID-03 is resolved by retained raw API generate/lint/build/unit output; unchanged API identity makes the retained API224 evidence proportionate.\n\nTest effectiveness remains mixed because two prior transition obligations are not directly discriminated: the empty-thread between-round test orders its burst after the inbound events, and opening coverage does not combine an actual reconnect with the held opening response. Test efficiency is otherwise acceptable: source-owned full commands, targeted mutation controls, and three repetitions of the high-risk FRC case are proportionate. The package uses real Nest/session/grant/PostgreSQL/WebSocket boundaries, owned fixtures, fresh served-bundle attestation, and no skip/focus, fake BFF payload, ambient proof subject, or broad fallback.\n\nPerformance is mixed but honestly bounded: EPS records the deep 10,001-row residual and a worse composite-index trial without claiming a production SLO; BCI's real PostgreSQL barrier and 10-by-3 mutation control are strong; RLS is correctly described as a limited local sample. The React owner remains a simple faithful implementation rather than a new cache/framework. Operational fit is otherwise sound: Node 22, disposable PostgreSQL, real browser runner, retained leaf logs, and no remote-CI/deployment claim. ARCH-DEL-01, ARCH-DEL-01-ERR, TQA-TL-01, TQA-TL-02, and TQA-EVID-03 are closed by this package; ARCH-DEL-02 and ARCH-DEL-03 remain open as test-evidence gaps.","recommended_path":"Keep the approved architecture and repair only the two missing browser regressions. Make the paused-empty scenario use chronologically older backlog data, assert that the first post-event resume is a fresh head request rather than an old-cursor request, and add a failing old-cursor mutation control. Add a held-opening real reconnect scenario with no later message trigger. Rerun the affected tests, the full project-owned npm run test:tela suite, and the repeated FRC evidence against the resulting source manifest; retain existing unchanged API evidence. Then request a bounded delta review.","performance_position":"mixed","elegance_position":"acceptable","structural_soundness_position":"mixed","operational_fit_position":"acceptable","findings":[{"finding_id":"ARCH-DEL-02","severity":"medium","title":"[P2] Empty-thread recovery test does not prove restart from the new head","rationale":"web-app/e2e/timeline.spec.ts:181 seeds the 160-message burst at Date.now()+10_000, then sends both inbound webhooks through a fixture that supplies no message timestamp (api-app/test/timeline-fixtures.cjs:57). The final run completes far inside that ten-second offset, so receipt-time inbound messages are older than the entire burst. A broken paused-empty branch that retains its old cursor can load the remaining ten burst rows plus the two older inbound rows after Continue, still reach 162 IDs and unread=2, and never issue the required fresh-head read. The test counts only the initial three requests and never asserts that the first request after the between-round event has no antes cursor. It therefore does not discriminate the ARCH-DEL-02 regression or prove current metadata refresh in that path.","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"timeline-empty-paused-recovery-must-restart-at-head","affected_paths":["web-app/e2e/timeline.spec.ts","api-app/test/timeline-fixtures.cjs"],"suggested_action":"A (recommended): seed the burst in the past so each real inbound event is newer, instrument the resumed request and require a read-neutral recent-page request without antes before any older traversal, then retain complete ID/unread and visible current-metadata assertions. Add a mutation that retains the old empty-thread cursor and require this regression to fail. B: provide explicit inbound timestamps later than the burst with the same request-level assertion. C: retain final-state equality alone, which leaves the reviewed stale-cursor behavior unprotected."},{"finding_id":"ARCH-DEL-03","severity":"medium","title":"[P2] Opening-race coverage omits reconnect while the initial response is held","rationale":"web-app/e2e/timeline.spec.ts:56 proves a real inbound message during a held opening response, but not an onopen/reconnect callback in that same threadAtual-null state. src/tempoReal.spec.ts:25 uses a fake socket to prove callback emission, while the browser reconnect case at web-app/e2e/timeline.spec.ts:121 begins after opening has completed. A regression that suppresses or misroutes the reconnect callback only while invalidacaoAbertura is active would pass all supplied assertions, despite the approved requirement that reconnection recover without a further event or poll.","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"timeline-opening-reconnect-must-trigger-recovery","affected_paths":["web-app/e2e/timeline.spec.ts","web-app/src/tempoReal.spec.ts","web-app/src/telas/Inbox.tsx"],"suggested_action":"A (recommended): hold the actual opening GET after its backend fetch, force a real socket reconnect while it remains pending, and require a read-neutral recovery without a later message event or clock advance; assert current IDs and unread after release. B: add an equivalent browser-level controllable real-socket integration case. C: rely on the helper unit test plus the post-opening reconnect test, which does not protect this opening-generation transition."}]}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-tqa-resolution.json
```
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-tqa-resolution-dispatch.json","review_kind":"test_quality_audit","reviewer_label":"delivery-tqa-resolution-native-no-context","findings":[{"finding_id":"ARCH-DEL-03-EVID","severity":"medium","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"timeline-opening-reconnect-must-trigger-recovery","title":"[P2] Held-opening reconnect coverage does not isolate the reconnect callback as the recovery trigger","rationale":"The revision5 scenario starts the held opening before it proves that the initial socket's authenticated connection/onopen has completed; it waits only for sockets.length===1 after opening is already pending. Therefore the first onopen can occur while threadAtual is null and increment invalidacaoAbertura. Concrete counterexample: a regression suppresses the callback only on a subsequent reconnect, while the first connection opens during the held request. The test still observes a second authenticated server frame, then recovery after release caused by the first opening callback, so its read-neutral request and ID assertions pass. This proves that a reconnect coexisted with recovery, but not that the reconnect-onopen caused recovery in the required opening-generation state. This is the remaining unresolved ARCH-DEL-03 evidence gap; it does not reopen the resolved implementation finding.","affected_paths":["web-app/e2e/timeline.spec.ts","web-app/src/tempoReal.ts"],"suggested_action":"A (recommended): before selecting the conversation, require the first authenticated socket frame so its onopen has run while no conversation is opening. Then hold the actual initial GET, persist the silent DB growth, close that established native socket, require the second authenticated frame, and only then release the response; retain the no-event/no-poll, read-neutral no-antes, full-ID, and unread assertions. Add a focused negative control that suppresses only the reconnect callback and must fail. B: use equivalent real-socket instrumentation that records the callback phase without replacing transport behavior. C: retain the current sequencing, which leaves reconnect-specific routing regressions able to pass."}],"overall_assessment":"Return for one focused browser-evidence repair. ARCH-DEL-02-EVID is resolved: the backlog predates both inbound events, the first authorized resume is required to be read-neutral and cursorless, current metadata is checked, and the retained-old-cursor mutation fails with exact restoration. ARCH-DEL-04 remains adequately protected by recovery-error disappearance assertions and the distinct newer-send-error preservation case. TQA-TL-01, TQA-TL-02, and TQA-EVID-03 remain resolved through direct budget/single-flight checks, six destination-context cases, and retained API command output.\n\nTest effectiveness is otherwise strong but mixed because the new opening-reconnect scenario has the causal gap above. Test efficiency is acceptable: it uses project-owned commands, real Nest/session/grant/PostgreSQL/WebSocket paths, owned fixtures, held real BFF responses, and targeted repetition without a fabricated BFF payload, skip/focus marker, or production test hook. Test-after status is stated honestly; the retained mutation controls materially discriminate the empty-cursor, budget, cursor-restart, and ACK protections.\n\nPerformance evidence is mixed but candid: EPS documents the deep 10,001-row residual and rejects a worse measured index candidate, while BCI and RLS substantiate bounded local concurrency/read-neutral claims without asserting production capacity. The React owner, recovery-error ownership, DI topology, fresh served-bundle provenance, and source-invariant API reuse are structurally and operationally appropriate on the embedded evidence.","recommended_path":"Repair only the reconnect test sequencing; no product redesign or renewed approval is warranted. Rerun the targeted opening and empty scenarios, the full project-owned Web unit/browser suite, and the required FRC repetitions against a fresh manifest and served-bundle attestation. Preserve the unchanged API, EPS, BCI, and RLS evidence while source identity remains established. Then request a bounded TQA resolution review; do not mark the delivery review gates complete until this remaining evidence gap is closed.","performance_position":"mixed","elegance_position":"acceptable","structural_soundness_position":"acceptable","operational_fit_position":"acceptable"}
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

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/verification-debt.md
```
# Verificação de dívida ST-ATT-01

Auditoria manual sobre o contrato aprovado,16 fontes atuais, provas de execução, testes e consolidação. Evidência raw: evidence/verification-debt-pre-final.log. O helper é lexical e reporta high/exit2 por termos waiver/n/a/pending/release-blocker na linguagem do template, contratos e histórico. O resultado raw permanece íntegro; não equivale à descoberta de waiver efetivo ou defeito atual.

- Dívida inline: none. Nenhum TODO/FIXME/HACK/TBD/XXX nos16 fontes; nenhuma supressão.
- Evidência: fonte API idêntica à suite224/SQL/BCI/RLS; stdout API CI faltante no round1 foi recolhido com os4leafs/115unit rev2. Web20/34 e FRC3 atuais estão ligados aos16hashes e ao build/served pré-workers, conferidos pelo root. Negativos de ACK, orçamento e restart são separados e restaurados, sem reivindicação de TDD.
- Validação: nenhum teste prometido foi removido ou waived. Suites targeted/gerações antigas/fixtures diagnósticas não substituem o full34. CI-equivalent permanece limitada aos jobs API/Web; PostgreSQL/browser adicionais explícitos. Sem stage-full/deploy/produção presumidos.
- Waivers: nenhum. n/a e not_needed descrevem contratos fora deste recorte (cutover, produção/remoto), sem reduzir gates required. Termos de pendência no contrato descrevem UI/recovery ou estados históricos; achados originais permanecem registrados para resolução independente, não adiados.
- Promoção canônica: contrato já consolidado no módulo owner antes do código; estado Verified local e links de closeout só serão promovidos após pareceres independentes. Transferência/mídia/status têm stories separadas e não são dívida desta entrega.
- Risco residual: deep keyset ainda filtra linhas mais recentes; EXPLAIN e trial justificam ausência de migration, sem SLO de produção. Coleção cresce só na conversa ativa; backdating foraT/provider externo/produção estão fora do contrato aprovado.

Classificação de suporte antes do final: nenhuma dívida material escondida de produto/testes; fechamento ainda condicionado aos deltas independentes, final review, consolidação Verified e guardas. Os dois itens governance DOD-07/VAL-07 continuam unchecked enquanto esses gates são efetivamente executados. Não há waiver nem deferred verification; após convergência, atualizar o mesmo artefato e repetir somente o helper documental final.

```

## Exact COMPLETE file delta revision5→6 web-app/e2e/timeline.spec.ts
```diff
--- revision5/web-app/e2e/timeline.spec.ts
+++ revision6/web-app/e2e/timeline.spec.ts
@@ -118,6 +118,10 @@
       });
     });
     await login(page, fixture.email, fixture.password, fixture.businessUnitId);
+    // Establish that the first onopen completed before the opening generation
+    // exists; only the later native reconnect may invalidate this opening.
+    await expect.poll(() => conexoesAutenticadas).toBe(1);
+    expect(sockets).toHaveLength(1);
 
     let liberar!: () => void;
     let iniciou!: () => void;
@@ -141,7 +145,7 @@
     await page.getByRole('button', { name: 'Cliente Timeline' }).click();
     await solicitacao;
     await expect(page.getByRole('status').filter({ hasText: 'Abrindo conversa…' })).toBeVisible();
-    await expect.poll(() => sockets.length).toBe(1);
+    expect(conexoesAutenticadas).toBe(1);
 
     // A primeira leitura já foi buscada e permanece retida no navegador. Estas
     // mensagens só entram no PostgreSQL; nenhum webhook ou evento as anuncia.

```

## Complete current held-opening reconnect scenario
```ts
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

## Current exact source/commands/freshness evidence
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

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rule-spirit-revision6-web-app.log
```
Rule-Spirit Anti-Pattern Scan
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/web-app
Stacks: all
Findings: 42
Max active severity: warning

| Stack | Severity | Search Lens | Location | Evidence |
| --- | --- | --- | --- | --- |
| shared | review | hard-coded local/domain target in source/config | `src/tempoReal.spec.ts:12` |     expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws');  |
| shared | review | hard-coded local/domain target in source/config | `src/tempoReal.spec.ts:32` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() });  |
| shared | review | hard-coded local/domain target in source/config | `src/tempoReal.spec.ts:58` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout });  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:5` | const API = `http://127.0.0.1:${PORTA_DA_API}`;  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:26` |     baseURL: 'http://127.0.0.1:4173',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:32` |       url: 'http://127.0.0.1:3101/health',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:80` |         WEB_ORIGIN: 'http://127.0.0.1:4173',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:85` |       // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`,  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:88` |       // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:91` |       // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:93` |       command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:97` |       url: 'http://127.0.0.1:4173',  |
| shared | review | hard-coded local/domain target in source/config | `src/api.ts:75` |     const pareceEstatico = res.status === 405 \|\| /^\s*<(!doctype\|html)/i.test(bruto);  |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:45` |   const apiEndpoint = `http://127.0.0.1:${apiPort}`; |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:48` |     fetch('http://127.0.0.1:3101/health'), |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:49` |     fetch('http://127.0.0.1:4173/'), |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:57` |   const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173')); |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:60` |   const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`); |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:93` |     endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname } |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline.spec.ts:3` | const FIXTURES = 'http://127.0.0.1:3101'; |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline.spec.ts:5` | const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/api.ts:75` |     const pareceEstatico = res.status === 405 \|\| /^\s*<(!doctype\|html)/i.test(bruto);  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/tempoReal.spec.ts:12` |     expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws');  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/tempoReal.spec.ts:32` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() });  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/tempoReal.spec.ts:58` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout });  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:5` | const API = `http://127.0.0.1:${PORTA_DA_API}`;  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:26` |     baseURL: 'http://127.0.0.1:4173',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:32` |       url: 'http://127.0.0.1:3101/health',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:80` |         WEB_ORIGIN: 'http://127.0.0.1:4173',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:85` |       // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`,  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:88` |       // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:91` |       // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:93` |       command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:97` |       url: 'http://127.0.0.1:4173',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline.spec.ts:3` | const FIXTURES = 'http://127.0.0.1:3101'; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline.spec.ts:5` | const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:45` |   const apiEndpoint = `http://127.0.0.1:${apiPort}`; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:48` |     fetch('http://127.0.0.1:3101/health'), |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:49` |     fetch('http://127.0.0.1:4173/'), |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:57` |   const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173')); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:60` |   const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:93` |     endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname } |

Note: this scanner supports the Rule-Spirit Anti-Pattern Hunt gate; it does not replace rule-specific review or P1/P2 judgment.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/test-quality-revision6-web-app.log
```
Test Quality Audit
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/web-app
Outcome heuristic: medium

Scan paths:
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline-freshness.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/playwright.config.ts
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
  - 153:    expect(burst.status()).toBe(201);
  - 212:    expect(burst.status()).toBe(201);
  - 235:    expect(burst.status()).toBe(201);
  - 256:    expect(burst.status()).toBe(201);
  - 281:    expect(burst.status()).toBe(201);
  - 301:    expect(claimStatus.statusCode).toBe(201);
  - 365:          expect(lateTie.status()).toBe(201);
  - 376:          expect(webhook.status).toBe(200);
  - 445:      expect(event.status).toBe(200);
  - 516:      expect(secondEvent.status).toBe(200);
  - 717:    expect(populateSecondary.status()).toBe(201);
  - 718:    expect(populateOtherBu.status()).toBe(201);

No-exception-only assertion hints:
  - none

Ambient subject fallback hints:
  - 73:    completedMigrations = Number(rows[0]?.count ?? 0);

DI override hints:
  - none

Mock / fallback hints:
  - none

Counts: hard_bypass=0 test_support=0 auth_shortcut=0 status_only=15 no_exception_only=0 ambient_subject_fallback=1 di_override=0 mock_hint=0

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

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-revision6-reconnect-negative-control-20261015.log
```

> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-Dw0MFlS2.js   224.40 kB │ gzip: 69.80 kB
✓ built in 1.46s
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

  ✘  1 e2e/timeline.spec.ts:90:3 › timeline da inbox com backend e PostgreSQL reais › reconecta durante a abertura retida e lê a cabeça sem novo evento (9.9s)


  1) e2e/timeline.spec.ts:90:3 › timeline da inbox com backend e PostgreSQL reais › reconecta durante a abertura retida e lê a cabeça sem novo evento 

    Error: expect(received).toBeGreaterThan(expected)

    Expected: > 0
    Received:   0

    Call Log:
    - Timeout 5000ms exceeded while waiting on the predicate

      161 |
      162 |     liberar();
    > 163 |     await expect.poll(() => recuperacoes.length).toBeGreaterThan(0, { timeout: 10_000 });
          |                                                  ^
      164 |     expect(recuperacoes[0].searchParams.get('marcarLida')).toBe('false');
      165 |     expect(recuperacoes[0].searchParams.has('antes')).toBe(false);
      166 |     await expect(page.locator('.bolha')).toHaveCount(5);
        at /workspace/web-app/e2e/timeline.spec.ts:163:50

    Error Context: test-results/timeline-timeline-da-inbox-75424-lê-a-cabeça-sem-novo-evento/error-context.md

    attachment #2: trace (application/zip) ─────────────────────────────────────────────────────────
    test-results/timeline-timeline-da-inbox-75424-lê-a-cabeça-sem-novo-evento/trace.zip
    Usage:

        npx playwright show-trace test-results/timeline-timeline-da-inbox-75424-lê-a-cabeça-sem-novo-evento/trace.zip

    ────────────────────────────────────────────────────────────────────────────────────────────────

  1 failed
    e2e/timeline.spec.ts:90:3 › timeline da inbox com backend e PostgreSQL reais › reconecta durante a abertura retida e lê a cabeça sem novo evento 

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-revision6-reconnect-negative-control-20261015.restore
```
expectedSha256=118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf
restoredSha256=118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf
restoredBytesExact=True

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-revision6-targeted-20261015.log
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
dist/assets/index-BFoOk2qo.js   224.39 kB │ gzip: 69.79 kB
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

Running 2 tests using 1 worker

  ✓  1 e2e/timeline.spec.ts:90:3 › timeline da inbox com backend e PostgreSQL reais › reconecta durante a abertura retida e lê a cabeça sem novo evento (5.0s)
  ✓  2 e2e/timeline.spec.ts:266:3 › timeline da inbox com backend e PostgreSQL reais › retoma thread vazia após evento entre rodadas e inclui toda a cabeça sem reler (1.3s)

  2 passed (20.9s)

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
  "reviewer_id": "delivery-tqa-causal-native",
  "recorded_at_utc": "2026-10-15T05:01:37Z",
  "evidence_type": "source-owned-playwright-real-backend-races",
  "sample_profile_id": "FRC-SP-M",
  "acceptance_rule_id": "FRC-A1",
  "result_summary": "Full36/36 and FRC3/3 passed on identical current source/build; shared3-attempt budget incl failures, retained T/restart, opening/empty notifications, six context races and recovery-error ownership covered. Independent delta judgment pending.",
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
    "residual_risk": "Bounded active-conversation memory grows as user loads history; no cache of other conversations. Backdated imports earlier thanT group and production traffic/provider transport are outside this approved slice."
  },
  "artifact_sha256": "f0db23ce2a47a0725721ab752ea5cf0fbfce9375350c930f2533a1c74104c92b"
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

## Complete audit framing and carried evidence index
Product/test alignment: only causal browser sequencing changes from revision5, plus discriminating reconnect-only mutation. Test-after is explicit; never claim retrospective TDD. Original suites and full terminal audits establish unchanged parser/API/auth/SQL/DI/test discovery and source-owned harness. Required journey coverage remains recent/history251IDs, T/H>T/equal-time lateID,3attempts/max1incl errors, dirty historical restart, initiallyempty>3pages with pastbacklog+freshhead/noantes+IN_SERVICE162IDs/unread2+negativeoldcursor, openingincoming, openingreconnect, postopeningreconnectwithoutlatertrigger,poll60progress,anchorbackfillarrival,author/draft,closemetadata, six conversation/BU×oldsend-success/networkfailure/backfill destination assertions, error-owner-clear/newer-error-preserved. Previous terminal TQA explicitly accepted all except opening-reconnect causality; do not casually reopen unchanged accepted loci.

Real boundaries: AppModule/sessions/grants/domain/PostgreSQL/WebSocket, external-only Meta/Evolution doubles. Owned disposable fixtures, no fabricated BFF response, actual response holds/explicit network aborts. Native socket constructor instrumentation returns real transport, only retains references to provoke close; authenticated connected frame proves server handshake. Scripts/discovery source-owned; no skips/focus/required-boundary mock fallback, ambient proof subject or auth shortcut. Static final scans API30/15 and Web42/21 are test-only loopback/.test and unchanged HTML regex, no suppression. Test-quality raw medium/exit2: API1status, Web15status+COUNT; paired business assertions/readbacks, COUNT aggregate not ambient subject. All currently changed code has no inline TODO/FIXME/HACK/TBD/XXX. Lexical debt high from template/history terms is classified manually, no actual waiver; final review/guards/canonical closeout are still mandatory, not deferred tests.

Runtime and performance: LinuxNode22.23.3, PW1.62.1Chromium, PG16.14 disposable DB leadshug_timeline_20261014/17migrations, same declared DB env; serial runners; new pre-worker source/build/served attestations. API115rawCI and224serial retained unchanged; EPS exact recent/deep/ties20382rows/1000ties with residual10001filtered, measured worse index removed, no migration/SLO. BCI3×10increments barrier+ACK-order negativecontrol/exactrestore; RLS30reads5concurrent×6,page50/unread7/history251 preserved,latencies observed no production threshold. FRC10repeatedrealtriggers×3 plus initial+thirdquery event,12frames/readstate,counts3/max1 and boundedcontinuations. Memory only active conversation; backdating outsideT, external provider transport/production excluded. Transparent React npm run test:tela mapping, no invented Flutter execution.

Return complete canonical JSON: explicit positions on product/test alignment, workaround risk, efficacy, efficiency, sufficiency, honest test-after; bypass/real-backend/DI/CI/platform/provenance, scope/security/PCV/elegance/structure/operational axes, residual uncertainty and decision adherence. Explicitly adjudicate ARCH-DEL-03-EVID and prior accepted findings. Findings first severity/locus/concretecounterexample/whynow/options/recommendation, four positions, detailed overall_assessment/recommended_path. No tools, no waiver inference.
