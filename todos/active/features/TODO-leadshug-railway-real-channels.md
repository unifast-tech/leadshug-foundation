# TODO — LeadsHug: homologação Railway com canais reais

## Title
ST-OPS-01 — Ambiente online persistente para desenvolvimento e provas dos canais

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`
- **Lifecycle state:** `Review`
- **Created:** 2026-11-09, America/Sao_Paulo.
- **Responsible:** Lucas Paifer, autoridade de produto e recursos; Delphi prepara contrato e evidências.
- **Template:** `delphi-ai/templates/todo_template.md`, copiado antes do preenchimento. Contrato em revisão; execução depende dos gates e da aprovação explícita abaixo.

## Context
Publicar homologação completa, independente da máquina local e de túneis, com WhatsApp oficial, Instagram e WhatsApp não oficial via Evolution. O ambiente servirá para acompanhar telas e preparar provas da Meta. A prioridade humana permite manter esta frente aberta junto ao [TODO de telas](TODO-leadshug-project-screens.md), sem transferir sua autoridade.

Lucas confirmou preservar histórico e vínculos existentes. Informou que existe um projeto Railway antigo, com outro banco e outra versão; identidade, dados, domínios, custo e estado remoto não foram verificados. O projeto antigo permanece observe-only; não é destino implícito nem backup comprovado. Em2026-11-09, Lucas escolheu criar um projeto Railway novo, usar domínio gerado pela plataforma e o plano Pro já existente. Workspace, região, identificadores e disponibilidade remota ainda não foram verificados; o plano informado não estabelece um teto de consumo.

## Framing Source & Story Slice
- **Feature brief:** rascunho transitório em `foundation_documentation/artifacts/tmp/leadshug-railway-real-channels-framing-20261109.md`; todo conteúdo necessário está reproduzido neste contrato. Promover enquadramento persistente na fase documental autorizada.
- **Primary story ID:** ST-OPS-01.
- **Why this is the right current slice:** um objetivo operacional: ambiente persistente completo para testar o produto e seus canais reais. Infraestrutura, migração e cutover são checkpoints subordinados; infraestrutura acessível sozinha não satisfaz o aceite final.
- **Framing decision:** feature-brief-required, preparado como rascunho. Submissão/decisão de App Review é frente posterior independente, sem criar outro TODO executável agora.

## Contract Boundary
O acordo humano autoriza organizar as duas frentes e preparar este TODO. Este contrato ainda não concede execução, deploy, configuração remota, exportação de dados, mudança Meta ou mensagens reais. Escopo/caminhos/baseline, decisões, revisões e autoridade precisam estar definidos antes de execução. Novas correções de domínio/segurança materialmente independentes devem receber contrato próprio, sem crescer silenciosamente este TODO.

## Implementation Intent
- **Current delivery:** proposta fechada de implementação da homologação; gates de revisão em andamento.
- **Planned next steps:** preparar implantação, migração, publicação e provas dentro do contrato aprovado; depois preparar submissão Meta específica.
- **Anticipatory implementation authorized now:** none.
- **Rationale:** publicar o produto entregue e suas dependências, preservando os invariantes existentes e sem antecipar funcionalidades futuras.

## Delivery Status Canon (Required)
- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** congelar/publicar somente este TODO para revisão independente, integrar os achados e executar os guards de planejamento antes de solicitar APROVADO.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** review
- **Why this state now:** plano concretizado, sem implementação ou prova de release; revisão independente e guards pendentes.
- **Exit condition:** decisões materiais fechadas, pacote revisado, preflight-go e aprovação de execução registrados.

## Scope
- [ ] SCOPE-01 Definir projeto/ambiente Railway isolado, serviços, região, fonte/revisão, domínio, orçamento e owner das configurações.
- [ ] SCOPE-02 Preparar Web, API, PostgreSQL, anexos persistentes e Evolution com seu banco/cache/sessões; rede interna e ingresso HTTPS conforme contrato.
- [ ] SCOPE-03 Migrar histórico/vínculos, anexos e dependências criptográficas com backup e restauração conferidos; impedir split-brain entre local e remoto.
- [ ] SCOPE-04 Validar login, sessão, isolamento por BU, navegador, atualizações em tempo real e controles de acesso no endereço publicado.
- [ ] SCOPE-05 Transferir callbacks/retornos de autorização dos canais reais de forma controlada e provar IN/OUT oficial, Instagram e Evolution com contas elegíveis e operador.
- [ ] SCOPE-06 Definir publicação de revisão validada, owner único de migrations, persistência após novo deploy e plano de reversão compatível com dados.
- [ ] SCOPE-07 Caracterizar requisitos e preparar roteiro/acesso/documentos para as provas Meta do app exato, sem declarar aprovação.

## Out of Scope
- [ ] Reescrever domínio, telas ou schema por causa da hospedagem; CRM/campanhas/Typebot adicionais.
- [ ] Alterar banco, versão, domínio ou serviço do projeto Railway antigo sem contrato concreto aprovado.
- [ ] Desconectar/reinscrever recursos Meta, girar chaves ou descartar sessões como atalho para implantação.
- [ ] Expor tooling de desenvolvimento, fixtures, seeds, banco, Redis ou a administração Evolution ao público por conveniência.
- [ ] Submeter/publicar o app Meta ou prometer liberação, receber clientes de produção, criar worktrees/cópias auxiliares ou publicar histórico/segredos em evidências.

## Parallel Coordination — ST-UI-01 / ST-OPS-01
1. Manter os dois TODOs abertos; ST-UI-01 continua sua implementação/validação isolada. Não esperar todas as telas para preparar homologação.
2. Principal checkout, um único writer de produto/runtime de cada vez entre root/API/Web/configurações; intercalar trabalho quando testes liberarem a janela de escrita, sem alterar fontes congeladas consumidas por testes em andamento.
3. Owners Foundation distintos só podem editar simultaneamente TODOs distintos. Roadmap, módulos, este TODO e artifacts compartilhados precisam de serialização explícita.
4. CP-P1: acordar baseline e arquivos sob escrita antes de qualquer alteração executável; não reivindicar mudanças preexistentes como delta Railway.
5. CP-P2: reservar validação consolidada e publicar somente API/Web por revisão identificada com gates pertinentes aceitos. Mudanças locais ainda não publicadas continuam locais.
6. CP-P3: reservar janela operacional única para dados, callbacks e provas reais. Um consumer ativo por recurso; o ambiente local não permanece writer concorrente depois do corte.
7. CP-P4: aceitar os três canais e persistência após redeploy; registrar a versão publicada. Uma nova jornada de telas entra por publicação posterior, com suas próprias evidências.
8. Revisores internos sem contexto são exigidos pelos workflows de crítica/arquitetura; isso não autoriza worktrees nem writers simultâneos. Somente este TODO pode receber commit/push Foundation de freeze pelos guards e workflow; Git de produto, mensagens e mutações remotas exigem a autoridade pertinente.

## Definition of Done
- [ ] DOD-01 Destino exato, serviços, domínios, rede, custos/limites e revisões publicados documentados sem segredos; projeto antigo preservado.
- [ ] DOD-02 Histórico/vínculos/anexos restaurados e conferidos com critérios de integridade; chaves compatíveis; backup recuperável, sem tokens em artefatos.
- [ ] DOD-03 Login, autorização/BU, Inbox e atualização em tempo real funcionando no bundle e backend comprovadamente publicados.
- [ ] DOD-04 WhatsApp oficial recebe e responde; operador confirma entrega e persistência sem reenvio automático.
- [ ] DOD-05 Instagram recebe e responde em conta/modo elegíveis; não inferir correção de descoberta/portfólio pela hospedagem.
- [ ] DOD-06 Evolution recebe e responde; transferência de sessão verificada ou reconexão autorizada separadamente se necessária.
- [ ] DOD-07 Novo deploy preserva dados e configurações; migrations e rollback/forward-fix têm owner e ordem definidos.
- [ ] DOD-08 Restrições herdadas de exposição possuem disposição aceita e evidenciada antes do corte; nenhuma dispensa implícita.
- [ ] DOD-09 Roteiro de provas Meta, acesso de avaliação e URLs/documentos aplicáveis preparados para o app exato; liberação externa separada.
- [ ] DOD-10 Evidências por critério, CI equivalente aplicável, auditorias e guards de entrega aceitos; nenhuma alegação de produção geral.

## Validation Steps
- [ ] VAL-01 Inventário redigido e leitura do destino; registrar fonte, config owner e estado atual sem exportar valores privados.
- [ ] VAL-02 Restaurar e testar migrations em alvo isolado, conferir integridade e compatibilidade de chaves/anexos antes de restaurar no destino aprovado.
- [ ] VAL-03 Executar suites canônicas pertinentes no estado consolidado, com fixtures isoladas; browser com bundle/backend frescos e regressão BU/autorização.
- [ ] VAL-04 Provar HTTPS, login, WebSocket e readback no destino; sem fixtures ou endpoints seed publicados.
- [ ] VAL-05 Capturar provas assistidas IN/OUT dos três canais, proveniência e persistência; não repetir mutações ambíguas.
- [ ] VAL-06 Conferir continuidade após novo deploy e procedimento de reversão com um único dono dos canais.
- [ ] VAL-07 Conferir contrato Meta aplicável e restrições públicas herdadas; submeter somente sob escopo/autoridade próprios.

## Complexity
- **Level:** big.
- **Checkpoint policy:** section-by-section; CP-P1..P4 e gates antes de dados, cutover e mensagens.
- **Why this level:** migração de estado privado e sessões, três canais reais, dependências externas e mudança de superfície pública.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`.
- **Secondary module docs:** `modules/identity-and-tenancy.md`, `modules/inbox-and-conversations.md`, `modules/audit-and-history.md`.
- **Module decision consolidation targets:** Canais: operação hospedada, dependências e limites; Identidade: sessão/origens; Inbox/Auditoria: integridade e proveniência. Topologia e runbook pertencem ao projeto.
- **Constitution:** stack já declara Railway; preservar invariantes. Necessidade de alteração será avaliada sem mudar o canon por este Draft.
- **Roadmap:** propor homologação em paralelo à iniciativa visual; edição compartilhada adiada até coordenação e contrato refinado.

## Decision Pending (Resolve Before Freeze)
Nenhuma pergunta de produto impede revisar a proposta abaixo. Nomes/limites técnicos são decisões propostas para o APROVADO, não fatos já provisionados. Workspace/IDs, inventário privado, medições de volume e estado Meta são gates de execução com critério de parada explícito; não podem ser adivinhados.

## Decisions (Resolved Before Freeze)
- D-R1 Usuário confirmou trabalho em paralelo com TODOs separados e checkpoints compartilhados, em2026-11-09: “Perfeito vamos seguir dessa forma então”.
- D-R2 Usuário confirmou “Preservar histórico e vínculos atuais (recomendado)” na resposta assíncrona de2026-11-09.
- D-R3 Usuário informou “Até existe mas é um projeto antigo com outro banco e outra versão”. Não houve consulta remota nem autorização de substituição.
- D-R4 Objetivo final inclui canais reais; subir apenas frontend ou infraestrutura não satisfaz este contrato.
- D-R5 Em2026-11-09, na resposta assíncrona a call_be8afe1c180148e1b8d30124b431c539, Lucas escolheu “Criar um projeto Railway novo (recomendado)”. O projeto antigo fica preservado.
- D-R6 Na mesma resposta, Lucas determinou usar o domínio gerado pelo Railway e informou o plano Pro existente. Isso resolve a preferência de hospedagem; não comprova saldo, workspace, configuração remota, teto de uso ou provisionamento.

## Decision Baseline (Frozen Before Implementation)
D-01..D-12 são a proposta a revisar e aprovar; não substituem D-R1..6, que preservam as decisões humanas.

| ID | Contrato proposto |
| --- | --- |
| D-01 | Projeto novo `leadshug-homolog`, ambiente `homologacao`, no workspace Pro do operador. Antes da criação, leitura autenticada identifica owner/workspace; se houver mais de um candidato ou colisão de nome, parar e obter seleção, sem reutilizar projeto antigo. Registrar IDs reais em evidência privada/redigida. |
| D-02 | Sete serviços em uma região: `gateway`, `web`, `api`, `postgres`, `evolution`, `evolution-postgres`, `evolution-redis`. Propor US East Metal/Virginia `us-east4-eqdc4a`, disponível na documentação consultada; não é região já validada para a conta. Se indisponível, retornar para decisão antes de criar volumes. |
| D-03 | Somente gateway tem domínio gerado Railway/TLS. API/Web/PG/Evolution/Redis sem domínio público e sem TCP proxy permanente. Gateway encaminha UI, `/api/bff`, `/api/v1`, `/ws` e webhooks autorizados; `/api/internal` e demais rotas não admitidas recebem negação explícita. Bootstrap/rotinas internas usam rede privada, nunca a URL pública. |
| D-04 | Ingresso de mesma origem: `LEADSHUG_API_URL` vazio, `WEB_ORIGIN`/`PUBLIC_ORIGIN` no HTTPS gerado, `COOKIE_SAMESITE=Lax`, sem `COOKIE_DOMAIN`. Preservar raw body/HMAC, limites atuais de upload/webhook e logs sem query/corpo/tokens. WebSocket deve comprovar upgrade/autenticação/reconexão. Validar cadeia de proxies/IP/Forwarded: não confiar cabeçalhos arbitrários do cliente nem prometer rate limiting por IP sem prova. |
| D-05 | Infraestrutura declarativa atual em `.railway/railway.ts`, owner exclusivo no root; SDK TypeScript e CLI fixados por lock/version. `railway.json` dos submódulos fica como histórico não consumido. A documentação atual depreca Config as Code para novos serviços. Plano remoto redigido antes de apply, sem deletes ou alteração do projeto antigo. |
| D-06 | API/Web continuam imagens Docker separadas. Publicação por imagens OCI privadas no GHCR, fixadas por digest, com manifesto de fontes/build/evidência; gateway tem imagem própria de contexto mínimo. Evolution conserva imagem/digest do Compose; PG16 e Redis7.4 conservam major e recebem digest registrado, sem upgrade de provedor nesta fatia. Autoupdate desativado, sem `latest`. Nenhum deploy automático por commit nesta primeira entrega. |
| D-07 | Uma réplica por serviço, sem autoscaling/serverless/sleep; mesma região. API preserva Node22, Prisma/OpenSSL e entrypoint de permissões. API health `/health`, web health `/`, gateway health verifica API e a disponibilidade estática do Web; prazo inicial de startup120s, restart ON_FAILURE/3 e captura redigida da falha. Health de banco/cache por conexão nativa privada; Evolution por endpoint compatível com a imagem pinada. Graceful shutdown/drenagem serão comprovados, sem inferir suporte por configuração. |
| D-08 | Volumes independentes: PG do produto, PG Evolution, Redis persistente, `/dados/arquivos` API e `/evolution/instances` Evolution. Medir usados antes de alocar; provisionar capacidade maior que o usado com folga de50%, arredondada ao GiB seguinte, mínimo1GiB. Registrar custo/capacidade antes do apply, sem resize destrutivo. Backups diários e semanais dos volumes, com prova de restore; cópia consistente de migração adicional cifrada sob custódia do operador. |
| D-09 | Preservar histórico, IDs, grants, chaves de credenciais, arquivos, instâncias/sessões e configurações necessárias. Novo destino recebe restauração da fonte local canônica, nunca do banco antigo Railway. Preservar segredos de decriptação; não rotacionar credenciais durante migração. `.env.testing` não é copiada integralmente; valores passam por canal privado, referências entre serviços permanecem referências. |
| D-10 | Release owner único (executor DevOps). Builds/validações consomem fontes congeladas do principal checkout; manifesto inclui commits-base, dirty hashes públicos e hashes dos inputs efetivos. Fonte de ST-UI-01 só entra quando seu owner aceitar evidências; baseline Git antiga não representa seu candidato local. Imagem válida é a testada/atestada pelo manifesto; mudar qualquer input invalida a prova. Publicar OCI exige autorização de checkpoint, sem tornar imagem pública por fallback. |
| D-11 | Implantar bancos/volumes primeiro; restauração ensaiada antes do snapshot final. API só inicia após restore e `npx prisma migrate deploy` do mesmo digest, um owner por vez, `migrate status` e integridade conferidos. Evolution do destino só inicia após origem quiescente e snapshot coerente; nunca ligar duas instâncias na mesma sessão. Backend/gateway público só abre após segurança e prova de readiness privada. |
| D-12 | Preservar plano Pro e políticas/limites de cobrança existentes do workspace; sem mudar subscription, spending cap ou orçamento global. Antes de recurso cobrável, apresentar alocação, projeção e custo incremental no checkpoint de provisionamento. Valor mensal ainda não é compromisso autorizado; não presumir que Pro cobre o consumo. Sem novos provedores além de GHCR/Railway existentes sem revisão de acesso/custo. |

## Proposed Runtime Topology
Todos os nomes abaixo são proposta, não identidade remota validada. Construção e rede privada precisam de prova antes do corte.

| Serviço | Fonte/start e porta interna | Estado e rede |
| --- | --- | --- |
| gateway | `docker/railway-gateway/Dockerfile`, Nginx/PORT; upstreams por referência Railway | Único HTTPS público; DNS interno re-resolvido após redeploy; upgrade WS; internal deny; sem volume |
| web | Dockerfile atual Web, entrypoint Nginx/PORT | Privado; bundle estático + config.js sem segredos; sem Node dev server |
| api | Dockerfile atual API, `/entrypoint.sh node dist/main.js`, PORT3000 | Privado; PG produto e anexos; verificar IPv4/IPv6 e trust-proxy sem alterar domínio por inferência |
| postgres | PostgreSQL16 fixado por digest | Somente privado; volume DB produto e usuário de privilégio delimitado |
| evolution | Imagem2.3.7/digest já no Compose, porta8080 | Somente privado; callback API privado `/webhooks/evolution`, secret header e sessão persistente |
| evolution-postgres | PostgreSQL16 fixado por digest | DB separado do produto, somente privado |
| evolution-redis | Redis7.4 fixado por digest, AOF | Privado, autenticação e volume; preservar semântica de cache/sessão, sem expor Redis |

### Variable Inventory — names only
| Grupo/owner | Nomes ou referências | Regra |
| --- | --- | --- |
| API/base | NODE_ENV, PORT, DATABASE_URL, WEB_ORIGIN, PUBLIC_ORIGIN, SESSION_SECRET, INTERNAL_SERVICE_TOKEN, LH_ARQUIVOS_DIR, COOKIE_SAMESITE | NODE_ENV production; banco privado; secrets preservados/selados, nunca em config.js |
| Criptografia/API | CHANNEL_CREDENTIAL_KEY_ID, CHANNEL_CREDENTIAL_KEY | Preservar compatibilidade com os ciphertexts migrados; ausência/erro bloqueia corte |
| WhatsApp/API | META_APP_ID, META_APP_SECRET, META_SIGNUP_CONFIG_ID, GRAPH_VERSION, WEBHOOK_VERIFY_TOKEN | Mesmo app/config vigente; versão contratada, sem upgrade por hospedagem |
| Instagram/API | INSTAGRAM_AUTH_MODE, INSTAGRAM_CONFIG_ID, INSTAGRAM_CLIENT_ID, INSTAGRAM_CLIENT_SECRET, INSTAGRAM_REDIRECT_URI, INSTAGRAM_API_VERSION, INSTAGRAM_WEBHOOK_APP_SECRET, INSTAGRAM_WEBHOOK_VERIFY_TOKEN | Unified conforme módulo; callback exato derivado da rota fonte; sem fallback WhatsApp |
| Evolution/API | LH_CHANNEL_UNOFFICIAL, EVOLUTION_API_URL, EVOLUTION_API_KEY, EVOLUTION_WEBHOOK_URL, EVOLUTION_WEBHOOK_SECRET | URLs privadas por referência, header e chave compatíveis |
| Evolution/serviço | DATABASE_CONNECTION_URI, CACHE_REDIS_URI, AUTHENTICATION_API_KEY, SERVER_URL, LOG_LEVEL | Inventário privado por allowlist do Compose; nenhuma leitura genérica de Config.Env em logs |
| Web/gateway | LEADSHUG_API_URL vazio; PORT; API_UPSTREAM, WEB_UPSTREAM e referências privadas | Nenhum segredo no browser; variáveis de upstream novas pertencem só ao gateway |
| Release | RAILWAY_TOKEN, autenticação GHCR, IDs de alvo e digests | Custódia privada; tokens mínimos por projeto/ambiente; sem valores no TODO/manifesto |

### Migration and Cutover Contract
1. CP0/readiness: conferir fonte local canônica pelo owner `leadshug_channels_local`, volumes, versão real PG, migrations/checksums, tamanho e destinos. Conferir por nomes/presença e metadados privados; não imprimir mensagens, contas, tokens ou hashes de segredos. Não confundir DB descartável de testes com fonte operacional.
2. Ensaio: backups lógicos PG custom format com ferramentas PG16 compatíveis e cópia cifrada de anexos/sessões; restore em infraestrutura isolada, sem egress de provedor e sem callbacks. Verificar tabelas/contagens, FKs, IDs locais, migrations, acesso BU e decriptação em memória. Saída só booleans/contagens redigidas. Ensaio não inicia Evolution com sessão viva.
3. Cutover com operador: confirmar ownership dos apps/callbacks e se o app atende terceiros; alterações compartilhadas não são presumidas autorizadas. Reservar janela, impedir novos envios/mutações no local, drenar requisições aceitas/receipts/jobs e conservar operações UNKNOWN sem replay externo. Registrar ponto consistente dos dois bancos/anexos/cache/sessão após quiescência.
4. Ingresso antigo durante janela: não responder2xx a webhook que não foi duravelmente persistido. Verificar comportamento documentado de retry dos provedores; não assumir retenção infinita ou zero perda. Interromper se não houver rota de retry/retomada verificável e contabilização dos eventos em trânsito. Não executar envios de teste antes do gate próprio.
5. Restaurar snapshot final no novo alvo e validar; iniciar API privada só após migrations; iniciar Evolution somente com origem parada. Configurar callback interno Evolution com autenticação preservada, sem recriar/remover instância. Se sessão não retomar, registrar falha e retornar ao operador antes de solicitar QR ou reinscrição.
6. Trocar origens/retornos/callbacks Meta no checkpoint autorizado, sem troca de tokens/app/recurso por conveniência. Provar challenge/HMAC, recebimento, idempotência e persistência; old ingress não permanece processador canônico concorrente.
7. Abrir gateway e realizar login/BU/WS e IN/OUT assistida nos três canais; readback e novo deploy controlado. O domínio gerado permanece estável entre publicações do mesmo serviço; não recriar serviço/domain para cada release.
8. Rollback antes de qualquer escrita no destino: retomar origem a partir do snapshot consistente e restabelecer callbacks com autorização. Após primeira escrita no destino: congelar remoto, preservar eventos novos e reconciliar/dump reverso antes de retorno; forward-fix é preferido se houver migrations incompatíveis. Nunca restaurar snapshot antigo sobre mensagens novas nem apontar callbacks para DB defasado. Manter origem parada e backup preservado após aceite; sem apagar volumes automaticamente.

## Assumptions Preview (Required Before Plan Review)
| ID | Assumption | Evidence | Impact if wrong | Risk | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Web suporta base vazia e WebSocket same-origin | `web-app/docker/40-config-js.sh`, `web-app/src/tempoReal.ts` | Gateway precisaria alterar contrato Web | medium | Keep as Assumption |
| A-02 | API/consumers têm portas/configuração privadas separáveis | `api-app/src/main.ts`, `api-app/src/infra/config/modulos.ts`, `api-app/docker/entrypoint.sh` | Acesso privado ou startup falha | high | Keep as Assumption |
| A-03 | Owner/source canônico é selecionável sem ler segredos em stdout | `scripts/start-channels-local.sh`, `scripts/test-channels-local.sh` | Confundir runtime com DB de teste compromete migração | high | Keep as Assumption |
| A-04 | Snapshot de sessão Evolution pode ser transportado | `docker-compose.channels.yml` | Reconexão poderá exigir decisão/ato do operador | high | Promote to contract: preservar estado e parar se restore não retomar |

## Execution Plan (Required Before APROVADO)
1. Refinamento/revisões (agora): congelar somente este TODO, revisar arquitetura e crítica sem contexto, integrar resoluções e guards; obter APROVADO para implementação local delimitada.
2. Implementação local: configurar IaC, gateway, publicação verificável, migração e teste de ingresso sem tocar runtime operacional. Nenhuma leitura de credenciais/DB de clientes por testes. Ensaios usam somente fixtures isoladas.
3. Validação: suites locais canônicas + ingress/volumes/restore isolados; gerar pacote concreto de provisionamento com custos/IDs/fontes/artefatos redigidos. Gate de segurança herdada precisa estar satisfeito antes da publicação pública.
4. Checkpoint P: apresentar projeto/ambiente/workspace, plano IaC sem deletes, recursos/custos, digests e configuração de acesso e obter autoridade para criação/configuração/OCI/deploy. Se o alvo ainda não existir, criar projeto novo só neste checkpoint e revalidar IDs após criação antes das demais mutações. Não requer terminar todas as telas; usar candidato aceito e congelado.
5. Checkpoint M: apresentar inventário/custódia do backup, ensaio e plano de corte; obter autoridade específica para ler/exportar/restaurar dados/chaves/sessões, parar origem e alterar callbacks. Testes reais só após alvo e contas explicitados com operador.
6. Aceite: provar DODs, atualizar owners/documentação no escopo autorizado, auditorias finais e guards; manter App Review como processo externo posterior. Submissão do app Meta continua fora desta autoridade.

## Flow Evidence Planning Matrix
| ID | Fluxo/cenário | Evidência planejada | Preconditions / alvo |
| --- | --- | --- | --- |
| F01 | Login/logout/retorno, acesso negado e grant BU | Browser de imagem fresca e readback; teste de cookie Secure/Lax e /ws sem sessão negado | Fixture isolada com duas BUs e conta autorizada/negada; depois smoke hospedado sem seed |
| F02 | HTTP/API/WebSocket e HMAC pelo gateway | Upgrade101, mensagens recebidas no browser, reconnect pós-deploy, request sem/assinatura inválida recusado; /api/internal e fixtures negados | Gateway Docker isolado, API real e providers falsos; TLS no destino após checkpoint |
| F03 | WhatsApp oficial IN/OUT | Prova assistida, persistência/readback e confirmação humana de recebimento | Conta oficial vigente, sem retry de POST; checkpoint M |
| F04 | Instagram IN/OUT Unified | Mesma conversa/rota/BU, leitura após reabrir e confirmação humana | Conta elegível conforme módulo; EMPTY_LIST ou portfólio incompatível não são resolvidos por deploy |
| F05 | Evolution IN/OUT e retomada | Identidade e sessão retomadas, callback autenticado e readback; sem novo pareamento implícito | Origem parada, DB/sessão restaurados; reconexão nova exige decisão |
| F06 | Restore e novo deploy | Restore íntegro + migrações + arquivos/decriptação + estado antes/depois; eventos novos não sobrescritos | DB/cache/volumes descartáveis no ensaio; snapshot real somente M |
| F07 | Provas Meta | Roteiro e URLs de privacidade/exclusão/retornos exigidos pelo app, credencial de avaliação via canal privado | App exato e permissão descritos; conteúdo ausente vira pendência material, sem declaração fictícia |

## Local CI-Equivalent Suite Matrix
Matriz de execução planejada, não prova passada. Runner Docker/Node22/PG16 do projeto; sem `make up`/`migrate` do ambiente operacional como teste. Fixar versão das ferramentas e ligar o browser ao mesmo DB/endpoint da suite.

| Suite / Job | Intended behavior / scenario | Fixture / bootstrap / lifecycle preconditions | Command / owner | Authoritative target | Status |
| --- | --- | --- | --- | --- | --- |
| root / Compose | Compose resolve sem expor novas portas/segredos; API/Web mantidos | Env sintética; `docker compose config --quiet` nos overlays sem stdout com valores | `.github/workflows/ci.yml` + `scripts/check-channels-ci-parity.py --self-test` | Principal checkout, Docker seguro | planned |
| root / API | Lint/build/unit API usados pelo CI root | Node22/OpenSSL, dependências lockadas, sem dotenv privado | Leaf commands do job API: npm ci/lint/build/test dentro do runner | API consolidada | planned |
| root / Web | Build/unit Web usados pelo CI root | Node22/lock e API config pública sintética | Leaf commands do job Web: npm ci/build/test dentro do runner | Web consolidada | planned |
| root / channels-validation | Contratos API/PG e jornadas browser existentes sem regressão | DB descartável, migrations, providers falsos, bundle/API compilados frescos, recibos e cleanup | `bash scripts/test-channels-local.sh all` | Principal checkout; fonte congelada | planned |
| infra / Railway topology | IaC tipos/lint e invariantes:1ingresso, internal deny, volumes/refs, digests e ausência de segredo | SDK/CLI pinados; fixtures de plan redigido, sem conta remota para testes | `bash scripts/railway/validate.sh`; mesmo wrapper no novo job infra do CI root | `.railway/` + gateway/config | planned |
| infra / gateway and restore | Provar F01/F02/F06 por Docker/browser real: spoofed headers, WS, limites/HMAC, restore e falha de migração | Stack isolada; sem produção/Meta/Evolution vivo; fixtures públicas e backup sintético | `bash scripts/railway/test-isolated.sh`; mesmo wrapper no CI root | Novo contrato narrow infra, somado à matriz ampla | planned |

Admissão de novo wrapper/job por `ci-equivalent-test-surface-admission`; preservar jobs/lifecycle atuais. Não chamar somente o novo wrapper de CI equivalente completo. API/Web não possuem `.github/` no checkout observado; não inventar checks de fonte-repo ou presumir que Wait for CI conhece o job do root. Publish wrapper exige recibos das linhas aplicáveis + manifesto dos mesmos inputs, inclusive alterações locais aceitas.

## Frontend / Consumer Matrix
| Producer | Consumers | Contract / evidence |
| --- | --- | --- |
| API/BFF/sessão | Web publicado, login e Inbox | F01/F02 e bundle/digest verificado; não alterar shape/domínio |
| Gateway/WebSocket | Browser autorizado e negado | Upgrade, cookie e eventos por BU; F01/F02 |
| Webhooks/OAuth | Meta/Instagram/Evolution e configuração do operador | F03..05, assinatura/raw body/owner único |
| DB/arquivos/chaves | API, histórico, attachments e operador de restore | F06 e conferência privada de integridade/decriptação |
| IaC/release manifest | CLI Railway e executor DevOps | Wrapper validado, plano sem deletes e digests/IDs conferidos no checkpoint P |
| Material Meta | Operador/revisor externo | F07; não substituir uso real por provider falso |

## Diff Expectation Contract (Required Before Delivery)
- **Contract status:** required
- **Policy:** strict; unclassified or forbidden paths block delivery
- **User validation:** required on deviation
- **Comparison mode:** working_tree
- **Preexisting changes:** inventário redigido em artifacts/tmp/railway-plan/source-baseline.json; alterações anteriores de root/API/Web/Foundation não são delta deste TODO. Capturar diff real por writer/manifesto, não tratar checkout sujo como branch limpa. Reclassificação necessária antes de execução se algum input mudar.

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| root | . | 80e3940126f22a941f90dba4f5e801b6c0eb2f58 | working_tree |
| api | api-app | db5a86758a165fac8a1ab587599c37b17890530c | working_tree |
| web | web-app | 74b9d4b714044829796f875d00553f077c1c329d | working_tree |
| foundation | foundation_documentation | a59185cd069935e00202e73ffb3a1a69dd648f8d | working_tree |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| root | .railway/** | A | IaC, SDK/lock, configuração pública/redigida e release manifest sem segredos |
| root | docker/railway-gateway/** | A | Gateway de contexto mínimo e negação de rotas internas |
| root | scripts/railway/** | A | Validação, release por digest, backup/restore e testes isolados com entradas privadas protegidas |
| root | .github/workflows/ci.yml | M | Adicionar somente jobs narrow infra; preservar suite/lifecycle anterior |
| root | README.md | M | Comandos e checkpoint de implantação sem valores privados |
| web | .dockerignore | M | Excluir .git/private/artefatos locais do contexto de imagem; não alterar telas |
| foundation | todos/active/features/TODO-leadshug-railway-real-channels.md | M | Contrato/evidências desta frente |
| foundation | artifacts/tmp/railway-plan/** | A,M | Evidência transitória ignorada e redigida |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/** | any | Segurança/domínio fora desta fatia; nova necessidade material exige contrato |
| api | prisma/** | any | Não criar schema ou migration por hospedagem |
| web | src/** | any | Fonte UI pertence a ST-UI-01; serializar e admitir a versão aceita |
| root | .gitmodules | any | Topologia existente preservada |
| root | .env* | any | Configuração privada não será editada/versionada por esta implementação local |
| foundation | todos/active/features/TODO-leadshug-project-screens.md | any | Outro owner/contrato |
| foundation | modules/** | any | Consolidação proposta abaixo exige fase documental delimitada, não mistura ao delta de implementação |
| foundation | system_roadmap.md | any | Fonte compartilhada; handoff estratégico próprio antes de editar |

Arquivos de secrets/backups não entram em diff ou Git. Adotar runtime/valores privados somente nos checkpoints de autoridade próprios. Módulos/roadmap e brief persistente receberão consolidação em fase documental explicitamente delimitada antes do fechamento; até lá este TODO é a autoridade tática e nenhuma publicação é alegada. Guard de diff exige classificar todo delta preexistente, não há waiver implícito.

## Bounded But Elastic Guardrails
Pode absorver ajustes de IaC, Nginx, release/migration tooling e testes nos paths acima que preservem o mesmo contrato. Novo domínio, remediação API/schema, substituição de provedor, mudança de identidade ou aceitação de risco exige novo contrato/renovação, sem contornar bloqueadores públicos.

## Module Decision Baseline Snapshot
| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| integrations-and-channels / SEC-R6-04 | Recovery de templates restrito à coorte privada local até budget persistente | Preserve | `modules/integrations-and-channels.md:263`, backlog BLG-leadshug-template-recovery-read-budget |
| integrations-and-channels / Instagram | Unified textual/local, restrições de elegibilidade/portfólio e prova real | Preserve | `modules/integrations-and-channels.md` seção Unified e limites de entrega |
| identity-and-tenancy / sessões e BU | Sessão e isolamento no backend | Preserve | `modules/identity-and-tenancy.md`, `policies/scope_subscope_governance.md` |
| inbox-and-conversations / rotas | Mesma BU/contato/recurso, sem duplicar efeito | Preserve | `modules/inbox-and-conversations.md` |

## Architecture Change Governance
- **Applicability:** required
- **Why this applies:** estabelece topologia hospedada e caminho repetível de release do projeto.
- **Deviation / debt being retired:** dependência de hostname efêmero e deploy sem contrato de estado consolidado.
- **Target steady-state after closeout:** ingresso único, fontes/digests verificáveis, estado persistente e um owner por canal.
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** aceite dos três canais/dados após novo deploy; não excluir origem automaticamente.

### Patterns To Enforce
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Same-origin e ingresso privado | D-03/D-04 e política de escopo | Gateway/API/Web | Sessão e raw body corretos sem internal público |
| Fonte por manifesto e digest | D-06/D-10 | Release | Publicar somente estado validado |
| Single writer e restore coerente | D-09/D-11 | Dados e canais | Impedir perda/reenvio por split-brain |

### Prohibited Anti-Patterns
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| Copy de .env no build, secrets em plan/show-values ou log | Validação e inspeção do contexto/logs | Vazamento privado | nenhuma |
| API/internal ou DB/Redis/Evolution públicos | IaC/gateway negative tests | Exposição indevida | nenhuma |
| Imagem flutuante ou fonte diferente do recibo | Manifesto/digest e freshness guard | Publicação sem prova | nenhuma |
| Snapshot antigo sobre eventos novos | Checklist/contagens/restore guard | Perda de histórico | nenhuma |

### Architecture Protection Harness
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | Gateway/IaC/release | `scripts/railway/validate.sh` | Ingresso extra, internal aberto, digest/secrets inválidos | implement-in-this-todo | Matriz CI e DOD08/VAL03 |
| test | Runtime/restore isolado | `scripts/railway/test-isolated.sh` | WS/sessão/HMAC quebrados, restore inconsistente | implement-in-this-todo | F01/F02/F06 e DOD02/03/07 |
| audit | Corte de canais | Gate cutover independente | Dois writers, rollback destrutivo | implement-in-this-todo | DOD10/VAL06; delivery review |

## Plan Review Gate
- **Status:** prepared-pre-freeze
- **Review depth:** full; arquitetura, segurança de dados/ingresso, evidência e operação.
| Issue ID | Severity | Problem / chosen handling | Status |
| --- | --- | --- | --- |
| PR01 | high | Mesmo cookie em hosts Railway distintos: adotar gateway same-origin e provar WS, headers e cookies | decisão proposta; teste antes de exposição |
| PR02 | high | Perda/split-brain na migração: quiescência, snapshot final, único consumidor e rollback com eventos novos | decisão proposta; ensaio e checkpoint M |
| PR03 | high | Fonte suja/sem CI source repo: manifesto de fontes aceitas e OCI por digest; gate root completo explícito | decisão proposta; bloquear publish sem recibos |
| PR04 | high | SEC-R6-04: bloquear gateway público até entrega do budget no contrato próprio | pré-requisito obrigatório, sem waiver/disable implícito |
| PR05 | medium | Novo SDK e rede privada/volumes: prova de compatibilidade e tipo/ingresso/restore antes de apply | falhar fechado e voltar ao plano em mudança material |

## Failure Modes & Residual Risks
- A API usa trust-proxy1 e adicionamos proxy: validar IP/origem/headers end-to-end. Se exigir mudança de fonte API, renovar escopo antes de implementar.
- Região/capacidade, acesso CLI/GHCR e conta Pro só serão conhecidos por leitura autenticada. CLI Railway não foi encontrada no PATH desta sessão; sem destino remoto consultado.
- Evolution pode exigir pareamento após transporte; preservar snapshot não garante sessão. Não prometer reconexão transparente nem deletar origem.
- Tokens/políticas/app/contas podem impedir prova real; disponibilidade local histórica não prova atual e domínio fixo não remove limitações Meta.
- Uma réplica com volumes pode ter indisponibilidade em deploy; não há promessa de zero downtime, SLA ou escala/HA.
- A remediação `BLG-leadshug-template-recovery-read-budget` é pré-requisito externo deste TODO antes de Railway público; precisa contrato próprio e provas sequenciais/concorrentes, sem excluir feature ou reduzir gate por conveniência.
- A suite browser existente inicializa servidores/fixtures locais; não apontá-la diretamente ao Railway. Smoke hospedado deve usar contrato específico sem seeds, com mutações reais somente pelo operador autorizado.

## Questions To Close
Não há pergunta humana adicional necessária para revisar este pacote. APROVADO aceitará as propostas técnicas D-01..12 para implementação local, sem conceder checkpoints P/M. Ambiguidade de workspace, nova correção API, estimativa de custo ou pré-requisito de segurança não resolvido interrompe o checkpoint afetado.

## Profile Scope & Handoffs
- **Current profile:** Strategic / CTO-Tech-Lead; Genesis excluído pelo canon existente.
- **Primary execution profile:** operational-devops após APROVADO; technical scope docker, railway e interfaces React/Vite/NestJS/PostgreSQL/Prisma.
- **Supporting profiles:** assurance para os gates; operational-coder só sob expansão delimitada aprovada.
| From Profile | To Profile | Why | Surfaces | State |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-devops | Executar contrato de infraestrutura | Paths esperados | planned |
| operational-devops | strategic-cto | Consolidar topologia/runbook/roadmap/módulos antes de closure | Foundation compartilhada | planned; serializar e delimitar diff |
| operational-devops | assurance-tester-quality | Evidência e gates de delivery | pacote congelado | planned |

## External Dependency Readiness
| Dependency | Status | Verification / handling |
| --- | --- | --- |
| Delphi | healthy | verify_context.sh exit0 na preparação atual |
| Railway / Pro | unknown | Relato humano; CLI ausente; leitura/autenticação privada necessária antes de P |
| GHCR / permissão de publish | unknown | Verificar por leitura; publicar só em P, sem fallback público |
| Domínio Railway | unknown | Modalidade escolhida; hostname real nasce em P |
| Meta/contas | unknown | Provas históricas; verificar ownership/estado em M |
| Backup/volumes reais | unknown | Inventário/ensaio real somente M; testes usam sintéticos |
| SEC-R6-04 | unknown | Restrição documental explícita; exigir contrato/evidência da remediação antes do público |

## Security Risk Assessment
- **Security review:** required; sessão/BU/dados privados e superfície pública.
- Pré-requisito de admissão: SEC-R6-04/BLG-leadshug-template-recovery-read-budget concluído com orçamento persistente e provas; gateway não abre antes. Não há autorização de correção API por este contrato.
- Preservar HMAC, raw body, integridade/criptografia, autorização BU, não repetição de POST e redaction. Testar header spoofing/rate limiting, internal deny e ausência de tooling/fixtures no destino.
- Reavaliar gatilhos da dívida de tooling Instagram à luz da plataforma/launcher e fonte das dependências; sem upgrade geral ou inferência de imunidade.
- **Evidence plan:** testes locais ingress/restore, auditoria de segurança da imagem/config e revisão antes do corte.

## Performance & Concurrency Risk Assessment
- **Performance/concurrency decision:** required conforme piso; evitar scans/list walks nos helpers e reuso do request body; medir overhead gateway/WS, memória e tempos de restore.
- Sem alteração em consultas de negócio nesta fatia. Manifesto/validação usa allowlist e coleta bounded; um release/migration owner, mutações remotas sem retry cego.
- Load tests de provedores reais não são autorizados; amostras isoladas com payload/limites contratados e budget explícito para smoke hospedado.

## Verification Debt Assessment
- **Decision:** required antes de closure; evidência histórica local não certifica Railway.
- Herdar restrições de Instagram/templates e divergências de fonte explicitamente; não dispensar as provas dos três canais.

## Audit Trigger Matrix
| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | Migração e três canais |
| blast_radius | cross-stack | Runtime/Web/API/dados |
| behavioral_change_or_bugfix | yes | Ingresso e ciclo de release |
| changes_public_contract | yes | Exposição pública e bloqueio internal |
| touches_auth_or_tenant | yes | Cookie/origem/BU |
| touches_runtime_or_infra | yes | Railway e volumes |
| touches_tests | yes | Wrappers/jobs narrow infra |
| critical_user_journey | yes | Login/Inbox/INOUT |
| release_or_promotion_critical | yes | Deploy/dados |
| high_severity_plan_review_issue | yes | PR01..04 |
| explicit_three_lane_request | no | Piso determinístico ainda se aplica |

## Architecture Review Gates
- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** not_run
- **Decision review evidence / resolution:** prepared-pre-freeze; fresh internal reviewer required
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** not_run
- **Adherence review evidence / resolution:** required at delivery

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Why this decision:** revisão precisa de baseline publicada e pertencente somente a este TODO.
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** pending-freeze
- **Baseline push reference:** origin/main
- **Gate status:** not_run
- **Findings summary:** somente este TODO será staged/committed/pushed; alterações anteriores e TODO de telas preservados.
- **Evidence / reference:** prepared-pre-freeze

## Gate: Review Scope Drift
- **Gate decision:** required
- **Why this decision:** comparar seções materiais com freeze publicado antes de aprovação.
- **Trigger stage:** after planning review and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Gate status:** not_run
- **Evidence / reference:** prepared-pre-freeze

## Independent No-Context Critique Gate
- **Critique decision:** required
- **Why this decision:** expanded cross-stack/dados/runtime/auth.
- **Package mode:** bounded-file-set
- **Critique isolation mode:** fresh internal no-context reviewer
- **Critique lenses:** correctness, performance, elegance, structural-soundness, risk
- **Critique status:** not_run
- **Findings summary:** prepared-pre-freeze
- **Evidence / reference:** prepared-pre-freeze
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review, delivery only after validation

## Gate: Assumption Code Coherence
- **Gate decision:** required
- **Why this decision:** A-01..03 precisam de paths de código e conferência antes de aprovação.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01,A-02,A-03
- **Gate status:** not_run
- **Findings summary:** prepared-pre-freeze
- **Evidence / reference:** prepared-pre-freeze

## Rules Acknowledgement / Ingestion
Fontes concretas previstas; reload vinculante depois de APROVADO, não prova de ingestão futura.
| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/workflows/railway/change-service-deployment-contract-method.md | Infra Railway | Identidade/alvo/config/owner | Mutação sem checkpoint | P/M com plano e prova |
| delphi-ai/rules/stacks/railway/railway-deployment-contract-always-on.md | Estado remoto | Referências privadas/redaction | show-values, deploy sem autoridade | Verificar IDs/revisão |
| delphi-ai/workflows/docker/update-runtime-and-ingress-method.md | Gateway/runtime | Rotas/HMAC/WS/cookies | Expor internal e fixtures | Teste proxy consolidado |
| delphi-ai/workflows/docker/update-ci-pipeline-method.md | Jobs novos | Matriz e lifecycle existentes | Job só local ou só CI | Wrapper compartilhado |
| delphi-ai/skills/ci-equivalent-governance/SKILL.md | Evidência ampla | Paridade da matriz | Smoke substituir ALL | Gates locais antes de P |
| delphi-ai/skills/ci-equivalent-test-surface-admission/SKILL.md | Admissão narrow infra | Mesmos comandos local/CI | Drift de suite | Admission e revalidação |
| delphi-ai/workflows/postgresql/change-relational-contract-method.md | Dump/restore/migrations | Integridade e transações | Reset/drop/overwrite | Ensaio e gate de dados |
| delphi-ai/workflows/prisma/change-schema-migration-contract-method.md | Migrate deploy/status | Histórico aplicado | Prisma dev/resolve/reset | Um owner de migrations |
| delphi-ai/workflows/docker/todo-execution-boundary-method.md | Autoridade tática | Paths/escopo aprovados | Expandir correção de API | Renovar se necessário |
| delphi-ai/workflows/docker/effort-selection-method.md | Roteamento | Modelo/papel concreto | Autorização Git inferida | agent_role_routing_guard.py antes de executar |

## Agent Routing Preflight
Tupla proposta de execução, distinta dos revisores de planejamento. Verificada pelo guard de routing em preparação; repetir após aprovação antes de despacho.
- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Subagent / delegation authorization:** workflow effort-selection/todo-execution-boundary após APROVADO; planejamento usa revisores internos exigidos por critique/architecture
- **Execution topology:** primary-checkout-single-writer
- **Worktree authorization:** not-authorized
- **Worktree authorization reference:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

## Execution Lane Tracking
- **Local implementation branches:** root/api/web `feature/number-onboarding` são contexto atual, não autorização para writes fora do contrato; Foundation `main`.
- **Promotion lane path:** publicação de homologação por OCI digest nos checkpoints P/M; Git de produto e promoção canônica separados, sem inferir dev/stage em todos os repositórios.
- **Lane-promoted threshold for this TODO:** homologação publicada com provas aceitas; não declarar merge canônico por deploy.
- **Production-ready threshold for this TODO:** não há produção de clientes no escopo; homologação completa exige DOD01..10 e entrega documental. Não rotular Production-Ready para contornar promoção Git.

## Approval
- **Planning authorization:** “Vamos fechar esse plano então”, Lucas Paifer, 2026-11-09, e decisões anteriores D-R1..6.
- **Approved by:** aguardando APROVADO após gates de planejamento.
- **Approval scope:** proposta de implementação local dos paths esperados e validação sintética. Checkpoint P concede publicação/provisionamento e M concede dados/callbacks/provas reais somente após pacote concreto e autoridade próprios.
- **Execution not authorized by approval:** projeto Railway antigo, produção clientes, submissão Meta, mudanças API/schema, worktrees, credenciais em chat/Git, mutações remotas antecipadas, alterações globais de cobrança ou Git/push de produto.
- **Renewed approval required when:** novo path, domínio/schema/auth, alteração de risco/validação, nova versão de provedor, exclusão de feature ou waiver material.

## Delivery Gates — Planned
| Gate | Decision | Status / completion condition |
| --- | --- | --- |
| Pipeline/Copilot P1/P2 e Rule-Spirit | required | Antes de delivery, sem achados materiais abertos |
| Test Quality Audit | required | Fresh reviewer após testes, incluindo helpers/CI/restore e evidência real |
| Final Review | required | Fresh no-context independente, pacote final |
| Architecture adherence | required | Conferir D01..12 na entrega |
| Dedicated multi-lane audit | required if derived floor | Performance + TQA + especialista runtime/security, após evidências primárias |
| Cutover integrity | required | Checar um owner, dados novos, rollback/forward-fix e nenhuma duplicação |
| Diff/authority/completion | required | Todos GO antes de claim/closure, sem waiver implícito |

## Completion Evidence Matrix
| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | DOD-01 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-02 | Definition of Done | DOD-02 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-03 | Definition of Done | DOD-03 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-04 | Definition of Done | DOD-04 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-05 | Definition of Done | DOD-05 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-06 | Definition of Done | DOD-06 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-07 | Definition of Done | DOD-07 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-08 | Definition of Done | DOD-08 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-09 | Definition of Done | DOD-09 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| DOD-10 | Definition of Done | DOD-10 integral | runtime/review | F01..07 + pacote por critério no delivery | alvo do critério | planned | Sem prova de implementação agora |
| VAL-01 | Validation Steps | VAL-01 integral | test/runtime | Matriz CI e checkpoints P/M com recibo específico | alvo do critério | planned | Rastrear evidência exata, não agregado |
| VAL-02 | Validation Steps | VAL-02 integral | test/runtime | Matriz CI e checkpoints P/M com recibo específico | alvo do critério | planned | Rastrear evidência exata, não agregado |
| VAL-03 | Validation Steps | VAL-03 integral | test/runtime | Matriz CI e checkpoints P/M com recibo específico | alvo do critério | planned | Rastrear evidência exata, não agregado |
| VAL-04 | Validation Steps | VAL-04 integral | test/runtime | Matriz CI e checkpoints P/M com recibo específico | alvo do critério | planned | Rastrear evidência exata, não agregado |
| VAL-05 | Validation Steps | VAL-05 integral | test/runtime | Matriz CI e checkpoints P/M com recibo específico | alvo do critério | planned | Rastrear evidência exata, não agregado |
| VAL-06 | Validation Steps | VAL-06 integral | test/runtime | Matriz CI e checkpoints P/M com recibo específico | alvo do critério | planned | Rastrear evidência exata, não agregado |
| VAL-07 | Validation Steps | VAL-07 integral | test/runtime | Matriz CI e checkpoints P/M com recibo específico | alvo do critério | planned | Rastrear evidência exata, não agregado |

## Sources Consulted — 2026-11-09
- Railway IaC: https://docs.railway.com/infrastructure-as-code e /reference; plan é read-only/redigido, apply é mutação e tem owner.
- Legacy config: https://docs.railway.com/config-as-code — novos serviços não adotam railway.json; corte legado informado para2026-12-01.
- Regiões: https://docs.railway.com/deployments/regions — US East Metal/Virginia disponível na documentação, sem inferir disponibilidade remota.
- Volumes/backups: https://docs.railway.com/volumes e https://docs.railway.com/volumes/backups; política diária/semanal proposta, restore precisa de prova.
- Pre-deploy: https://docs.railway.com/deployments/pre-deploy-command — processo separado, sem usar volume para migrar arquivos; migrations DB separadas do transporte de anexos/sessões.
- Fontes locais inspecionadas: README/Makefile, Compose/overlay, Dockerfiles/entrypoints, api main/config/realtime, Web runtime config/socket, root CI e runners; nenhum arquivo privado ou banco real aberto nesta etapa.

## TODO Closeout Disposition
Plano em revisão; somente este TODO e artifacts/tmp próprios mudaram. Sem implementação/provisionamento/migração/Meta/envio nesta etapa. Após freeze e revisões: solicitar APROVADO para implementação local. Pré-requisito de segurança e checkpoints P/M continuam explícitos; TODO de telas preservado.
