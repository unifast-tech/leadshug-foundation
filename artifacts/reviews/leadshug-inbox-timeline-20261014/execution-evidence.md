# Evidência de execução ST-ATT-01

Produto e provas aceitos nas revisões independentes de aderência, TQA e final, sem achados materiais pendentes. Aprovação humana em2026-10-14; validação local em2026-10-15. API/Web em feature/inbox-timeline-pagination, checkout principal com executor único /root/timeline_executor_resume; Foundation main. Guardas, commits e publicação documental são registrados no fechamento do mesmo TODO. Publicação operacional de produto está fora desta entrega.

## Fonte e runtime observados

[Resumo final revision6](evidence/executor-revision6-summary.json). Root comparou os16 arquivos atuais (API7/Web9) byte a byte às duas attestations finais. Produto permanece igual à revisão4 aceita; revisões5/6 alteraram apenas e2e/timeline.spec.ts. API7 permanece idêntico à fonte das115unidades/224E2E/EPS/BCI/RLS. Nenhuma mudança de schema/migration, providers, público/Consultar, env/compose/CI ou gitlinks.

LinuxNode22.23.3, Playwright1.62.1/Chromium/Noble com binárioNode22, PostgreSQL16.14 descartável leadshug-timeline-postgres-20261014/DB leadshug_timeline_20261014,17migrations; DB5432 somente na rede Docker, sem host publish. Dependências Linux provisionadas por npmci/volumes próprios; módulos Windows não foram usados. API3100,fixtures3101,preview http://127.0.0.1:4173 no runner descartável. Usuários do DB e builds/runners foram serializados.

[Attestation full](evidence/attestation-browser-web-authority-revision6-final-full-20261015.json),2026-10-15T04:59:11.580Z; [attestation FRC](evidence/attestation-browser-web-authority-revision6-final-frc3-20261015.json),2026-10-15T05:00:22.318Z. Ambas ANTES dos workers, com branch/diff/sourceManifest, manifestsAPI/dist,17migrations e health API/fixture/preview200. Bundle servido==dist SHA2567cf5c91378614d35eabf83b7ba2f29aa33b339aaed8ad4c96f960f4037e170e2. Captura posterior não substituiu o requisito temporal.

## Resultados por owner

| Superfície | Comando próprio | Resultado | Raw |
| --- | --- | --- | --- |
| API CI leafs | npm run prisma:generate; npm run lint; npm run build; npm test |4leafsexit0,115/115unit,17arquivos | [stdout completo](evidence/api-ci-light-revision2-20261015.log) |
| API PostgreSQL completo | npm run test:e2e |224/224,20arquivos,111.92s,exit0 | [suite serializada](evidence/api-e2e-authority.log) |
| Web CI leafs | npm run build; npm test |buildexit0,20/20unit,3arquivos | [full final6](evidence/web-authority-revision6-final-full-20261015.log) |
| Browser adicional | npm run test:tela |36/36,1.0m,exit0 | [full final6](evidence/web-authority-revision6-final-full-20261015.log) |
| FRC repetido | npx playwright test e2e/timeline.spec.ts --grep="preserva o piso T" --repeat-each=3 |3/3,exit0 | [FRC final6](evidence/web-authority-revision6-final-frc3-20261015.log) |

CI-equivalent cobre os jobs API/Web tocados; PG/browser são validações locais adicionais requeridas. [Admissão](test-surface-admission.md) registra descoberta/config/owners. Bootstrap usa AppModule/sessão/grants/domínio/PostgreSQL/WebSocket reais; doubles apenas Meta/Evolution externos. Suporte em test/ recusa DB não descartável e não existe no entrypoint de produção. Browser segura respostas BFF reais e usa abort explícito; não fabrica payload BFF.

## Comportamentos e contraprovas

API:251IDs, limites/cursores/empates, scoped401/404/400 e precedência de autorização, sem escrita quando auth/query falham. ACK atômico precede SELECT; cursor/backfill e background são neutros. Public API/Consultar e regressões existentes preservados.

Web:recente/backfill completo e âncora com chegada durante await; autoria persistida/draft novo; close versus histórico; reconnect/poll60 retoma>3páginas; abertura+IN enquanto threadnull; seis destinos conversa/BU×envioantigo com sucesso/falha/backfill preservam seleção/draft/erro/IDs/metadados/scroll. Erro recovery desaparece ao completar cobertura; erro de envio mais recente sobrevive à limpeza tardia.

Vazio pausado: backlog no passado, dois IN reais mais novos, retomada exige primeira query recente/neutra/semantes,162IDs/unread2 e status IN_SERVICE visível após claim BFF real. Abertura/reconnect: PRIMEIRO frame autenticado antes da seleção; GETreal já buscado retido; crescimento silenciosoPG; close na instância WebSocket NATIVA registrada; SEGUNDO frame autenticado enquantoGETainda retido; depoisrelease. Nenhum evento de mensagem ou clock/poll posterior; recoveryneutro/IDs/unread verificados. Instrumentação conserva o transporte nativo e o servidor real.

FRC:Toriginal comH>T, lateIDmenor emT atrás de cursor percorrido,10gatilhos repetidos mais inicial e evento na terceiraquery,12frames/unread por repetição. Counts exatamente3requests automáticos/máximo1emvoo; eventos/falhas não renovam saldo, Continue/poll autorizam rodada. Erro histórico comdirty exige headrestart sem novo trigger; IDs completos após cobertura.

Test-after honesto, sem TDD retroativo. Controles temporários separados, restaurados byteexact em finally antes das suites canônicas:

| Mutação | Falha discriminante | Raw/restauração |
| --- | --- | --- |
| ACK depois do SELECT |expected10/received0 | [negativo](evidence/bci-mutation-control.log), [canônico restaurado](evidence/bci-canonical-after-mutation.log), [SHA](evidence/bci-source-restored.sha256) |
| Débito após await |3esperadas/5requests | [negativo](evidence/web-revision3-budget-negative-control-20261015.log), [restore](evidence/web-revision3-budget-negative-control-20261015.restore) |
| Sem restart no catch histórico |2esperadas/1recent | [negativo](evidence/web-revision3-cursor-negative-control-20261015.log), [restore](evidence/web-revision3-cursor-negative-control-20261015.restore) |
| Cursor vazio antigo conservado |temCursor=true, exigidofalse | [negativo](evidence/web-revision5-empty-cursor-negative-control-20261015.log), [restore](evidence/web-revision5-empty-cursor-negative-control-20261015.restore) |
| Primeirocallback preservado,reconnect suprimido |0recoveryrequests, exigido>0 | [negativo](evidence/web-revision6-reconnect-negative-control-20261015.log), [restore](evidence/web-revision6-reconnect-negative-control-20261015.restore) |

Negativos antigos possuem hashes da respectiva geração; os16 fontes finais restaurados são os das attestations final6. Suites targeted não substituem full36.

## Performance e concorrência

[EPS](pcv-eps.json): [SQL exato](evidence/explain-timeline-exact.sql)/[planos](evidence/explain-timeline-exact.log),20382mensagens/1000empates. Âncoras constantes resolvidas fora da medição: recente1.094ms/37buffers; profundo3.442ms/357buffers/10001linhas filtradas; empate0.850ms/37buffers. [Trial composto](evidence/explain-index-trial.log) profundo3.942ms/9832buffers com mesmo filtro: removido, sem migration justificada. PredicadoOR ainda filtra linhas mais recentes; sem SLO de produção.

[BCI](pcv-bci.json): SELECT real bloqueado, ACK observado antes da query em pg_stat_activity,10incrementos atômicos concorrentes preservados antes/depois da resposta em3lotes; INreal posterior eleva11. NegativoACK demonstra eficácia contra reset tardio.

[RLS](pcv-rls.json): [runner](evidence/rls-read-sample.mjs)/[raw](evidence/rls-read-sample.log), uma etapa5concorrentes×6lotes,30/30HTTP200/50mensagens/zeroerros; p5023.36ms/p9564.26ms/max68.5ms. Unread7 e251messages preservados. Conversa estrangeira com limite=invalid404; nome raw MalformedCursor está incorreto, representa limite inválido. Cursores têm negativos distintosAPIE2E. Correção/read-neutral definidos antes do estágio; latência observada sem promessa de capacidade.

[FRC](pcv-frc.json) atual liga políticas por ação, provas final6 e aceitação TQA; artefatos generation1/3/4/5 preservam observações históricas. As quatro lanes passaram com hashes canônicos conferidos. Crescimento da coleção só na conversa ativa, backdating foraT e transport/provider/produção são limites explícitos.

## Revisões e dívida

[Aderência aceita](delivery-adherence-resolution.json), [TQA causal aceita](delivery-tqa-causal-resolution.json) e [final aceito](delivery-final.json), internos fresh/no-context com modelos/effort prescritos, turn.completed/schema/merge, sem achados pendentes e sem waiver. JSONs de rounds/deltas e pacotes imutáveis completos em evidence/ preservam a causalidade das correções. Todos os anteriores terminaram antes de novo TQA; nenhum review live foi interrompido, substituído ou reduzido.

Scans fonte final: API30observações/15loci e Web42/21, sem allowlist/supressão, [triageAPI](scan-triage-api.json)/[Web](scan-triage-web.json). Loopback/.test de fixture e regexHTML preexistente foram aceitos by-design. Helper testquality exit2/medium: API1status,Web15status+COUNT, acompanhados de outcomes/readbacks; COUNT agregado não é sujeito ambiente. Zero hardbypass/skip/focus/authshortcut/no-exception-only/DIoverride/mockfallback. [Dívida](verification-debt.md) distingue heuristic lexical high de dívida real: inline none, nenhum waiver/dívida material de produto/testes; decisões verificadas promovidas ao módulo owner.

O guard genérico hardcodeia literaisFlutter; neste React a capacidade run_web_navigation_smoke corresponde explicitamente a npm run test:tela. Nenhum comandoFlutter foi executado/inventado. Specs source-owned, build fresco, URL descartável e mutação em feature non-main comprovam a equivalência aceita pelos revisores.

## Diagnósticos históricos e escopo

220/222API falhou por duas expectativas de fixture;223/223 sobrepôs browser no DB e é inválido. O resumo bruto inicial troca essas causas; só224serializado é autoridade. Node24, runs interrompidos, primeiroEXPLAIN comOFFSETna medição e suitesWeb anteriores são diagnósticos/história. Harness de contexto teve rótuloBU/representação de texto corrigidos; timeoutglobal30s preservado. Primeirooraclebudget sem empate foi corrigido ao grupoT; reconnectoffline/CDP não fechava socket e foi substituído por fechamento nativo real, depois isolado do primeiroonopen. Nenhum diagnóstico foi promovido a fullgreen.

Sem deploy, remoteCI, promoção remota de código, SLO, pentest ou provider externo validado. Limite de entrega: branchlocalAPI/Web e publicação documentalFoundation; próximos recortes transferência/estados/mídia permanecem em stories próprias. Artefatos de source/commit/guardas no mesmo diretório completam o closeout, preservando os snapshots de validação originais.

## Commits locais e limpeza

APIae6a9662c29b77276351aa9de653a47276372246 e Web4e56f6c1f4515b918d05b8c87e890d42e8542c56, ambos feature/inbox-timeline-pagination, sem push. Root conferiu todos16 blobs HEAD:path e bytes atuais contra as attestations: evidence/committed-source-attestation.json; repositórios limpos. Os snapshots pre-worker originais não foram reescritos. Nenhuma suite foi repetida sem alteração de bytes. Postgres/network dedicados removidos após retenção das provas; volumes Linux de dependências e imagem Node22 preservados como cache, sem cleanup de recursos operacionais.

Verificação de whitespace da documentação distingue prose editada de saídas brutas. Logs, dispatches/merges gerados e pacotes imutáveis contêm espaços/newlines emitidos pelas ferramentas; preservados byteexact para manter hashes/proveniência. git diff --check passa nos documentos autorais e nos16 fontes de produto; o blanket check dos artefatos raw retorna avisos de formatação, triados by-design/no-action, sem alterar os dados.
