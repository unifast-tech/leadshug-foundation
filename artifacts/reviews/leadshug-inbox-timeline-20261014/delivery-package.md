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

## Delta atual de entrega, revision3-final

O pacote de geração1 acima e seus dois pareceres completos são históricos e imutáveis. As correções fiéis à aprovação estão consolidadas nos16 fontes atuais (API7/Web9), sem arquitetura nova nem revisão interrompida. API source invariant mantém224E2E/EPS/BCI/RLS. API CI leaf stdout retido rev2 resolve a lacuna anterior. Webunit20/browser34/FRC3 são a autoridade atual, com duas attestations pré-workers e bundle servido==dist2da409a4…2589e.

Deltas no recovery: orçamento compartilhado3 consumido ANTES do await, evento não renova saldo; dirty conserva restart inclusive no catch histórico; vazio entre rodadas também reinicia recente; marcador de abertura sobrevive threadnull. Testes adicionais: counts/maxinflight,3aborts+eventos, falha histórica+headnovo, abertura+IN, empty>3pages+evento, seis transições conversa/BU × sucesso/falha/backfill com efeitos no destino. Dois negativos restaurados byteexact falham nos comportamentos antigos (3vs5requests,2vs1recent). Sem claim de TDD retroativo.

Pacote delta self-contained: artifacts/tmp/inbox-timeline-execution/delivery-delta-self-contained-package.md,410938bytes,SHA2564e52264e5990846b635c7631450e23dae184ca5e7c66b127a7dbe9864f58da59. Inclui auditorias originais integrais, contrato, diff exato geração1→3, fontes atuais, rubric TQA integral, raw leaf/runtime/negativos/scan e PCV canônicos. Internal stateless no-context/read-only com gpt-6.1-sol/max para aderência e gpt-5.6-terra/max para TQA; guards de routing go. Os processos foram despachados após o freeze34/FRC3; nenhuma revisão delta usou a geração intermediária2/3. Saídas serão acrescentadas após turn.completed, schema e merge.

## Resolução atual revision5

Produto revision4 aceito sem achados em delivery-adherence-resolution.json. TQA delta3 terminou e exigiu provas mais discriminantes de empty/reconnect; testes corrigidos com oracles request/metadata, handshake autenticada durante opening e negativo de cursor. Full36/FRC3 atual, manifest16/bundle7cf5c913…170e2. Resolução TQA interna fresca gpt-5.6-terra/max está live contra evidence/delivery-tqa-resolution-package-revision5.md, SHA4dfcd1c55d2d040432e8b7880ed14363159d9b62414039ed118f2b3f84426cc7; não substitui nenhuma revisão anterior live. Final review segue após convergência.
