# Catálogo comparativo de capacidades — LeadsHug × Central-Whatsapp

**Data:** 2026-09-25
**Story:** `ST-02`
**Status:** análise executada sobre snapshots congelados; recomendações não são prioridade nem autorização de implementação.

## 1. Resultado executivo

O LeadsHug já absorveu corretamente o núcleo que deveria ser comum aos dois produtos antigos: identidade única, escopo por Mantenedora/BU, canais oficial e não oficial como adaptadores, inbox única, conversa independente do transporte, claim externo/interno, encerramento/reabertura, histórico, exportação CSV, API keys e API pública de conversas. Portanto, o ganho agora não está em recompor os dois sistemas legados nem em copiar suas árvores.

Os gaps mais substantivos são domínios ainda deliberadamente futuros no LeadsHug: ciclo de modelos oficiais, motor de campanhas/disparos, CRM, relatórios operacionais, gestão avançada de grupos/comunidades e onboarding oficial por Embedded Signup. Também apareceram extensões que merecem estudo dentro desses domínios — mídia ponta a ponta, status de entrega/leitura/falha, custo de campanha, importação seletiva de grupos, agrupamentos reutilizáveis, assistente automatizado e central de ajuda.

Há três alertas importantes. Primeiro, “presente no legado” não significa “desejável”: papel somente leitura separado, autenticação cruzada entre dois produtos e heurística para descartar respostas automáticas são exemplos que conflitam com decisões atuais ou falharam no próprio legado. Segundo, várias capacidades do Central são monolíticas e acoplam UI, persistência, provedor e regra de negócio; qualquer adoção futura deve ser redesenhada nos módulos do LeadsHug. Terceiro, grupos e comunidades do transporte não oficial carregam risco operacional e de política distinto das campanhas oficiais.

## 2. Método e limites

- Fontes Central foram lidas somente por objetos Git congelados e pathspecs allowlisted. Nenhum conteúdo de `secrets/**` foi listado ou lido.
- Código, schema, configuração, infraestrutura e payloads não foram copiados. As evidências abaixo são referências `repo@sha:path:locator`.
- A população é composta por 129 commits não-merge oficiais, 66 commits não-merge do hub e 1 commit do overlay legado. Cinco commits não tocam qualquer allowlist e entram apenas como exclusões `outside_st02`, sem inspeção de caminhos.
- O estado LeadsHug foi verificado no API `5db3fbe2043428749895fc3ff6441e9457467dd0` e Web `6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9`.
- `not_found_after_protocol` significa ausência após busca estática dirigida; não afirma inexistência em produção ou em branches posteriores.
- `candidate_st04` significa somente que o item pode entrar na comparação de priorização futura do ST-04.

## 3. Manifesto reproduzível

| Identity | Base SHA | Head SHA | Head tree | Allowed paths / role |
| --- | --- | --- | --- | --- |
| `leadshug-api` | `n/a` | `5db3fbe2043428749895fc3ff6441e9457467dd0` | `4386ac3c732702c9d869f8a9482ccd99750e6ef8` | `src/** prisma/** test/** package.json README.md`; alvo |
| `leadshug-web` | `n/a` | `6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9` | `8b83239b57e31ec34bfbf911d35af035866e3ff0` | `src/** e2e/** public/** package.json README.md`; alvo |
| `central-official` | `6517f197c97d0b5bcad886d26eb0d28a813b47ca` | `337f3e4839cef8ca400de87b3de088a79d512944` | `1ee054a4630b0448b4432429e8b68b30f6e87ed5` | `src/** public/** migrations/** docs/** clientes/** package.json schema.sql wrangler.jsonc README.md CONTEXTO-CONTINUIDADE.txt`; origem oficial |
| `central-hub` | `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2` | `51bc16e544c7625a71c3012d8adef656c6392c37` | `e8823e402d1110d3fec0f6d2923490536f97254a` | `backend/** frontend/** docs/** docker-compose.yml README.md Caddyfile .env.backend.example .env.evolution.example .env.example`; origem hub; `secrets/**` não admitido |
| `legacy-hub-overlay` | `beb655cd3109fc3a537fca38c2b49f8c64853e7b` | `994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2` | `ff142200b038ae642f24c467b8f084cbc78e6229` | `hub-whatsapp/{backend,frontend,docs}/**` e arquivos raiz allowlisted; overlay histórico |

### 3.1 Comandos de verificação

```bash
git -C api-app rev-parse 5db3fbe2043428749895fc3ff6441e9457467dd0^{tree}
git -C web-app rev-parse 6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9^{tree}
git.exe -C "C:/Unifast/LeadsHug/Inspirações LeadsHug/Central-Whatsapp/api-oficial" rev-list --count --no-merges 6517f197c97d0b5bcad886d26eb0d28a813b47ca..337f3e4839cef8ca400de87b3de088a79d512944
git.exe -C "C:/Unifast/LeadsHug/Inspirações LeadsHug/Central-Whatsapp/hub-whatsapp" rev-list --count --no-merges 94ce80aa96d2c2ee004abc4d7ddf2c99a331def2..51bc16e544c7625a71c3012d8adef656c6392c37
git -C "/mnt/c/Unifast/LeadsHug/Backup LeadsHug/LeadsHug" rev-list --count --no-merges beb655cd3109fc3a537fca38c2b49f8c64853e7b..994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2 -- hub-whatsapp/backend hub-whatsapp/frontend hub-whatsapp/docs hub-whatsapp/docker-compose.yml hub-whatsapp/README.md hub-whatsapp/Caddyfile hub-whatsapp/.env.backend.example hub-whatsapp/.env.evolution.example hub-whatsapp/.env.example
```

Resultados observados: `129`, `66` e `1`. Com pathspec funcional, `126` oficiais e `64` do hub; os cinco restantes não tocaram allowlists.

## 4. Catálogo normalizado

### 4.1 Identidade, época e estado

| ID | Capacidade LeadsHug-owned | `origins[]` | `origin_epochs{}` | Cross | Estado LeadsHug | Força | Disposição |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CAP-001` | Ciclo de modelos oficiais: criar, pré-visualizar, submeter e acompanhar aprovação | `official` | `official:preexisting_gap` | false | `not_found_after_protocol` (`NF-001`) | corroborated | `candidate_st04` |
| `CAP-002` | Extensões de modelos: cabeçalho de mídia, importação da Meta e API de criação/status | `official` | `official:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-002`) | corroborated | `study` |
| `CAP-003` | Motor de campanhas/disparos com listas, exclusões, teste, fila e agendamento | `official,hub` | `official:preexisting_gap; hub:preexisting_gap` | true | `not_found_after_protocol` (`NF-003`) | corroborated | `candidate_st04` |
| `CAP-004` | Campanha interativa: botões/fluxo, respostas, métricas, custo e roteamento para automação | `official` | `official:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-004`) | corroborated | `study` |
| `CAP-005` | API pública e chaves escopadas para contas, conversas, mensagens e claim/release | `official,hub` | `official:preexisting_gap; hub:preexisting_gap` | true | `observed_present` | direct | `discard` |
| `CAP-006` | Inbox única para canais oficial e não oficial, com conversa independente do transporte | `official,hub` | `official:preexisting_gap; hub:preexisting_gap` | true | `observed_present` | direct | `discard` |
| `CAP-007` | Mídia e anexos ponta a ponta em recebimento, resposta e API pública | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `partial` | direct | `candidate_st04` |
| `CAP-008` | Atendimento móvel responsivo com navegação lista ↔ conversa | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `partial` | direct | `study` |
| `CAP-009` | Aviso de nova versão para sessões abertas | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `not_found_after_protocol` (`NF-009`) | corroborated | `study` |
| `CAP-010` | Timeline paginada, abertura na mensagem recente e carregamento incremental | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `partial` | direct | `candidate_st04` |
| `CAP-011` | Consulta, busca transversal e exportação de conversas | `official,hub` | `official:preexisting_gap; hub:preexisting_gap` | true | `partial` | direct | `candidate_st04` |
| `CAP-012` | Relatórios operacionais por período, atendente, setor e trajetória do contato | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `partial` | corroborated | `candidate_st04` |
| `CAP-013` | Ownership de atendimento, exclusividade, transferência e visão de liderança | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `partial` | direct | `candidate_st04` |
| `CAP-014` | Finalização e reabertura automática do atendimento | `official` | `official:post_baseline_evolution` | false | `observed_present` | direct | `discard` |
| `CAP-015` | Funis e cards de CRM originados da conversa | `official` | `official:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-015`) | corroborated | `candidate_st04` |
| `CAP-016` | Estados de envio, entrega, leitura e falha visíveis e auditáveis | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `partial` | direct | `candidate_st04` |
| `CAP-017` | Onboarding e ciclo de canal: Embedded Signup oficial, QR não oficial e remoção segura | `official,hub` | `official:post_baseline_evolution; hub:preexisting_gap` | true | `partial` | direct | `candidate_st04` |
| `CAP-018` | Identidade única para operar modalidades oficial e não oficial | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `observed_present` | direct | `discard` |
| `CAP-019` | Assistente automatizado por produto, widget, handoff, horário e registro | `official` | `official:post_baseline_evolution` | false | `partial` | corroborated | `study` |
| `CAP-020` | Central de ajuda contextual dentro do produto | `official` | `official:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-020`) | corroborated | `study` |
| `CAP-021` | Gestão de grupos/comunidades: importar, criar, agrupar e disparar | `hub` | `hub:preexisting_gap` | false | `partial` | direct | `candidate_st04` |
| `CAP-022` | Importação controlada do histórico já existente no dispositivo | `hub` | `hub:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-022`) | corroborated | `study` |
| `CAP-023` | Prévia e edição de agendamento de disparos não oficiais | `hub` | `hub:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-023`) | corroborated | `study` |
| `CAP-024` | Papel operacional separado para leitura sem atendimento | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `not_found_after_protocol` (`NF-024`) | direct | `discard` |
| `CAP-025` | Identidade operacional do número: telefone, apelido, setor e localização da inbox | `official,hub` | `official:post_baseline_evolution; hub:post_baseline_evolution` | true | `partial` | direct | `study` |
| `CAP-026` | Superfícies públicas de privacidade, termos e solicitação de exclusão | `official` | `official:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-026`) | corroborated | `study` |
| `CAP-027` | Heurística para detectar e descartar resposta automática do contato | `official` | `official:post_baseline_evolution` | false | `not_found_after_protocol` (`NF-027`) | direct | `discard` |

### 4.2 Evidência, valor, riscos e dependências

| ID | `central_evidence[]` | `leadshug_evidence[]` | Valor ao usuário | `risks[]` | `dependencies[]` | `canonical_rejection_ref` / notas |
| --- | --- | --- | --- | --- | --- | --- |
| `CAP-001` | `central-official@6517f197:README.md:modelos`; `central-official@6517f197:public/index.html:view-modelos` | `NF-001` | operar templates sem ferramenta separada | Meta review, categoria e janela | contrato próprio de templates/campanhas | null |
| `CAP-002` | `central-official@c8f4acc0:migrations/029-cabecalho-de-midia.sql`; `central-official@ee42e050:public/index.html:importar-da-meta`; `central-official@9a0389c5:src/index.js:api-v1-templates` | `NF-002` | reduzir recadastro e suportar conteúdo rico | sincronização divergente e upload | `CAP-001`, adapter Meta, arquivos | null |
| `CAP-003` | `central-official@6517f197:public/index.html:view-disparos`; `central-hub@94ce80aa:backend/prisma/schema.prisma:ScheduledMessage` | `NF-003` | comunicação em escala com operação rastreável | opt-in, rate limit, janela e abuso | templates/listas, política por canal, auditoria | roadmap Phase 4 exige TODO próprio; não é rejeição |
| `CAP-004` | `central-official@90b733a5:migrations/023-disparo-com-fluxo.sql`; `central-official@d294466b:src/index.js:button-report`; `central-official@234d239c:public/index.html:campaign-cost`; `central-official@fdf0d0e5:migrations/033-disparo-com-agente.sql` | `NF-004` | medir reação e encaminhar respostas | custo errado, automação invasiva e acoplamento | `CAP-003`, analytics, automação | null |
| `CAP-005` | `central-official@6517f197:public/index.html:api-keys`; `central-hub@94ce80aa:backend/src/modules/apiV1/routes.ts:apiV1Router` | `api-app@5db3fbe:src/domain/integration/api-key.service.ts:ApiKeyService`; `api-app@5db3fbe:src/surfaces/public/conversations.controller.ts:PublicConversationsController` | integração segura com sistemas parceiros | rate limit em memória e escopo incorreto | tenancy/BU, audit, provider adapters | já implementado; preservar arquitetura atual |
| `CAP-006` | `central-official@6517f197:public/index.html:view-atendimento`; `central-hub@94ce80aa:backend/src/modules/inbox/routes.ts:inboxRouter` | `api-app@5db3fbe:src/domain/inbox/conversations.service.ts:ConversationsService`; `web-app@6c99c27:src/telas/Inbox.tsx:Inbox` | equipe opera transportes num único contexto | vazamento entre BUs e shape de provedor | conversation invariant, grants, adapters | já implementado; não reintroduzir dois produtos |
| `CAP-007` | `central-official@5fd5317a:migrations/015-midia-recebida.sql`; `central-hub@da7c336b:backend/src/modules/apiV1/routes.ts:media` | `api-app@5db3fbe:prisma/schema.prisma:MessageType/mediaRef`; `api-app@5db3fbe:src/surfaces/bff/conversations.controller.ts:responder(texto)` | receber e responder com documentos/áudio/imagem | malware, tamanho, retenção e codecs | storage, policy por provedor, UI segura | parcial: persistência/tipos existem; resposta BFF continua texto |
| `CAP-008` | `central-official@aed3c40a:public/index.html:mobile-chat`; `central-hub@3cd5b228:frontend/src/pages/Inbox.tsx:mobile-footer` | `web-app@6c99c27:src/estilo.css:@media inbox`; `web-app@6c99c27:src/telas/Inbox.tsx:Inbox` | atendimento utilizável no celular | regressão de navegação/foco | design responsivo e testes visuais | parcial: layout colapsa, sem fluxo explícito lista ↔ conversa |
| `CAP-009` | `central-official@c34c418d:public/index.html:version-notice`; `central-hub@354f4116:frontend/src/components/AvisoNovaVersao.tsx` | `NF-009` | evitar sessão presa em bundle incompatível | loops de reload e falsa atualização | version fingerprint/build publication | null |
| `CAP-010` | `central-official@f8823c90:src/index.js:message-pagination`; `central-hub@7e1a6e27:backend/src/modules/inbox/routes.ts:pagination` | `api-app@5db3fbe:src/domain/inbox/historico.service.ts:MENSAGENS_POR_PAGINA`; `api-app@5db3fbe:src/domain/inbox/conversations.service.ts:thread(take-200)` | histórico grande sem travar ou ocultar mensagens | ordenação, duplicação e lacunas | cursor/offset contract e UI incremental | parcial: consulta pagina; thread operacional tem teto fixo |
| `CAP-011` | `central-official@0997b331:src/index.js:global-search`; `central-hub@66d58ab0:backend/src/modules/inboxHistory/routes.ts:xlsx` | `api-app@5db3fbe:src/domain/inbox/historico.service.ts:FiltroDeHistorico/csv`; `web-app@6c99c27:src/telas/Consultar.tsx:Consultar` | localizar e exportar relação histórica | exportação de PII e consultas caras | audit, permissionamento, paginação | parcial: busca/CSV existem; XLSX e busca transversal exigem contrato |
| `CAP-012` | `central-official@e563d951:public/index.html:attendant-report`; `central-official@26c9a03b:src/index.js:sector-journey`; `central-hub@602afe8e:backend/src/modules/inboxHistory/report.ts` | `api-app@5db3fbe:src/domain/painel/painel.service.ts:PainelService`; `api-app@5db3fbe:src/domain/inbox/historico.service.ts:HistoricoService` | gestão de volume, produtividade e jornada | métricas ambíguas e incentivo perverso | eventos auditáveis e definição de métricas | parcial: painel/histórico existem, não os cortes analíticos observados |
| `CAP-013` | `central-official@c2febe73:migrations/018-transferencia-setores.sql`; `central-official@d9952aec:migrations/024-conversa-exclusiva.sql`; `central-official@e42c25c1:migrations/036-lider-de-setor.sql`; `central-hub@54c48b95:backend/src/modules/inbox/routes.ts:transfer` | `api-app@5db3fbe:src/domain/inbox/conversations.service.ts:assumir`; `api-app@5db3fbe:src/domain/access/scope.ts:escopo` | responsabilidade clara e colaboração segura | corrida de claim, escalada indevida, redefinição de Setor | ST-03, grants, audit e concorrência | parcial: claim exclusivo existe; transferência/liderança precisam modelo próprio |
| `CAP-014` | `central-official@bf1f139b:migrations/021-finalizar-atendimento.sql` | `api-app@5db3fbe:src/domain/inbox/conversations.service.ts:finalizar`; `api-app@5db3fbe:src/domain/inbox/incoming.service.ts:reabrindo` | limpar fila sem perder retorno do contato | encerramento incorreto | conversation state/audit | já implementado |
| `CAP-015` | `central-official@0b862ad1:migrations/019-crm.sql`; `central-official@6cf96922:public/index.html:crm-card-conversation` | `NF-015` | acompanhar lead da conversa ao funil | definir domínio por UI e duplicar contato | roadmap Phase 3, ADR/contrato CRM | roadmap exige definição própria; não é rejeição |
| `CAP-016` | `central-official@db218a55:migrations/027-entrega-e-leitura.sql`; `central-official@8d2c1088:migrations/028-entrega-nas-mensagens.sql`; `central-hub@fc73a262:backend/src/modules/webhooks/routes.ts:delivery-status` | `api-app@5db3fbe:prisma/schema.prisma:MessageStatus`; `api-app@5db3fbe:src/surfaces/webhooks/{meta,evolution}.controller.ts` | saber se a mensagem chegou, foi lida ou falhou | estados fora de ordem e diferenças de provedor | idempotência, externalId, adapter status mapping | parcial: enum existe; processamento ponta a ponta não está completo |
| `CAP-017` | `central-official@1398fa20:src/index.js:embedded-signup`; `central-official@b6adf9b8:src/index.js:auto-webhook`; `central-hub@d73a56a7:backend/src/modules/instances/routes.ts:delete-instance` | `api-app@5db3fbe:src/domain/channels/channels.service.ts:ChannelsService`; `web-app@6c99c27:src/telas/Numeros.tsx:Numeros` | conectar e administrar números sem operação manual externa | OAuth/configuração, deleção destrutiva, estado divergente | Meta onboarding, Evolution adapter, audit | parcial: QR/connect/disconnect existem; Embedded Signup não |
| `CAP-018` | `central-official@4ea2dd09:migrations/026-acesso-ao-hub.sql`; `central-hub@b7ab36a4:backend/src/auth/central.ts` | `api-app@5db3fbe:src/surfaces/bff/auth.controller.ts`; `api-app@5db3fbe:prisma/schema.prisma:BuChannel` | uma identidade para toda operação | acoplamento circular entre produtos | tenancy/identity core | `central_whatsapp_independent_legacy_policy.md`; LeadsHug já unifica sem login cruzado |
| `CAP-019` | `central-official@765b57d5:migrations/030-agente-ia.sql`; `central-official@1c0db642:public/widget.js`; `central-official@39c8d902:public/index.html:agent-log`; `central-official@43d080fa:migrations/037-agente-fora-do-horario.sql` | `api-app@5db3fbe:prisma/schema.prisma:TypebotBot/TypebotSession`; `api-app@5db3fbe:src/domain/inbox/incoming.service.ts:typebot` | automação com handoff e rastreabilidade | prompt/tool abuse, tenant leak, custo e falsa autonomia | corrigir isolamento Typebot, policy, audit, ST-03 | parcial: automação Typebot existe; agente generativo/widget não equivalem |
| `CAP-020` | `central-official@95820372:public/ajuda.js:help-center` | `NF-020` | reduzir dependência de suporte externo | conteúdo desatualizado | ownership editorial e versionamento | null |
| `CAP-021` | `central-hub@94ce80aa:backend/src/modules/groups/routes.ts:groupsRouter`; `central-hub@212dd8b3:backend/src/modules/groupBundles/routes.ts`; `central-hub@06f24f8b:backend/src/modules/groups/destino.ts:community` | `api-app@5db3fbe:prisma/schema.prisma:ContactType.GRUPO`; `api-app@5db3fbe:src/domain/inbox/conversations.service.ts:grupos` | operar comunicação coletiva reutilizável | banimento, consentimento, hierarquia de comunidade | policy não oficial, ST-03, rate limit/audit | parcial: inbox de grupos existe; gestão/importação/disparo não |
| `CAP-022` | `central-hub@00031957:backend/src/modules/instances/importHistory.ts` | `NF-022` | continuidade ao conectar número existente | volume, duplicata, PII e ordem histórica | idempotência, cursor, retention | null |
| `CAP-023` | `central-hub@fa56ecf6:backend/src/modules/scheduling/routes.ts:edit-schedule`; `central-hub@fa56ecf6:frontend/src/components/PreviaWhatsApp.tsx` | `NF-023` | revisar e corrigir envio antes de executar | corrida com worker e alteração tardia | `CAP-003`, scheduler, optimistic locking | null |
| `CAP-024` | `central-official@bfab20fd:migrations/017-modulo-consulta.sql`; `central-hub@34149751:backend/src/auth/access.ts:consult` | `api-app@5db3fbe:prisma/schema.prisma:Role`; `web-app@6c99c27:src/telas/Usuarios.tsx:roles`; `NF-024` | separar observação de atuação | matriz de permissão duplicada | modelo de acesso canônico | `ADR-0018` no código atual removeu `VIEWER`; descartar como papel, não a necessidade de consulta segura |
| `CAP-025` | `central-official@82250088:public/index.html:inbox-location`; `central-hub@0674d595:backend/src/modules/instances/routes.ts:rename`; `central-hub@7801d83f:frontend/src/pages/Inbox.tsx:phone-header` | `api-app@5db3fbe:prisma/schema.prisma:BusinessUnit/BuChannel`; `web-app@6c99c27:src/telas/Numeros.tsx` | reduzir erro operacional ao escolher canal/BU | nomes divergentes e confusão BU/Setor | canonical naming and channel inventory | parcial: telefone/BU/status existem; alias/localização podem melhorar UX |
| `CAP-026` | `central-official@089374c5:public/privacidade.html`; `central-official@50c0745f:public/termos.html`; `central-official@8edcd8f6:public/privacidade.html:data-deletion` | `NF-026` | transparência e requisitos de plataforma | texto jurídico incorreto/desatualizado | owner jurídico, privacy process | null |
| `CAP-027` | `central-official@0537da9a:src/index.js:auto-reply-filter`; `central-official@622da56c:src/index.js:disable-auto-reply-filter` | `NF-027` | intenção era reduzir ruído | falso positivo descartou mensagens legítimas | evidência semântica confiável inexistente | null; lição negativa: não reproduzir heurística textual/temporal |

## 5. Aplicabilidade da policy por capacidade

Cada célula usa `applies`, `not_applicable` ou `unknown`, seguida de justificativa/evidência curta.

| ID | tenancy | BU | conversation | provider_adapter | audit | channel_policy |
| --- | --- | --- | --- | --- | --- | --- |
| `CAP-001` | applies: owner tenant | applies: WABA/BU | not_applicable: definição | applies: Meta | applies: lifecycle | applies: template policy |
| `CAP-002` | applies | applies | not_applicable | applies: Meta/media | applies | applies |
| `CAP-003` | applies | applies | applies: resposta cria/continua relação | applies: official/hub | applies | applies: opt-in/rate/window |
| `CAP-004` | applies | applies | applies | applies | applies: response/cost | applies |
| `CAP-005` | applies: API key tenant | applies: scoped IDs | applies | applies | applies | applies |
| `CAP-006` | applies | applies | applies: core | applies | applies | applies |
| `CAP-007` | applies | applies | applies | applies: codecs/limits | applies | applies |
| `CAP-008` | not_applicable: apresentação | not_applicable | applies: UI | not_applicable | not_applicable | not_applicable |
| `CAP-009` | not_applicable | not_applicable | not_applicable | not_applicable | applies: build/version | not_applicable |
| `CAP-010` | applies | applies | applies | not_applicable | applies | not_applicable |
| `CAP-011` | applies | applies | applies | not_applicable | applies: export | not_applicable |
| `CAP-012` | applies | applies | applies | applies: metric semantics | applies | applies |
| `CAP-013` | applies | applies | applies | not_applicable | applies | not_applicable |
| `CAP-014` | applies | applies | applies | not_applicable | applies | not_applicable |
| `CAP-015` | applies | applies | applies: origin/link | not_applicable | applies | not_applicable |
| `CAP-016` | applies | applies | applies | applies: status mapping | applies | applies |
| `CAP-017` | applies | applies | not_applicable | applies: onboarding | applies | applies |
| `CAP-018` | applies | applies | not_applicable | applies | applies | not_applicable |
| `CAP-019` | applies | applies | applies | applies: automation transport | applies | applies: handoff/window |
| `CAP-020` | not_applicable | unknown: conteúdo pode variar | not_applicable | not_applicable | applies: editorial | not_applicable |
| `CAP-021` | applies | applies | applies: group thread | applies: Evolution | applies | applies: unofficial/community |
| `CAP-022` | applies | applies | applies | applies: Evolution history | applies | applies: retention |
| `CAP-023` | applies | applies | applies: outbound history | applies | applies | applies |
| `CAP-024` | applies | applies | applies: read boundary | not_applicable | applies | not_applicable |
| `CAP-025` | applies | applies | applies: displayed context | applies | applies | not_applicable |
| `CAP-026` | applies: controller identity | not_applicable | not_applicable | applies: platform review | applies: requests | applies |
| `CAP-027` | applies | applies | applies | applies: WhatsApp Business behavior | applies | applies |

## 6. Protocolos de ausência

Todos os protocolos usaram os snapshots completos allowlisted de `api-app` e `web-app`, além de `project_mandate.md`, `project_constitution.md`, `system_roadmap.md` e módulos âncora. A segunda checagem dirigida comparou modelos Prisma, controllers/surfaces, serviços de domínio e rotas/telas esperadas.

| ID | Fingerprint e sinônimos | Busca dirigida | Segunda checagem / resultado |
| --- | --- | --- | --- |
| `NF-001` | template, modelo, message_template, approval | `rg -i 'template|modelo|message_template' api-app/{src,prisma} web-app/{src,e2e}` | nenhum model/service/controller/tela; somente comentários/migração histórica: absent |
| `NF-002` | import template, media header, template status API | mesma superfície + `rg --files` | nenhum owner de template; absent |
| `NF-003` | campaign, campanha, disparo, broadcast, scheduled message | `rg -i 'campaign|campanha|disparo|broadcast|ScheduledMessage' ...` | `AgendadorService` declara motor futuro; nenhum model/route/UI: absent |
| `NF-004` | flow/button response, campaign metrics/cost/agent routing | busca por termos de campanha, custo, resposta e agente | sem motor de campanha ao qual anexar extensões: absent |
| `NF-009` | app version, new build, reload notice | `rg -i 'nova vers[aã]o|version.*notice|reload.*build' ...` | nenhum componente/fingerprint de build: absent |
| `NF-015` | crm, funnel, pipeline, card | `rg -i 'crm|funil|pipeline|card' ...` | apenas enum de auditoria/comentários que afirmam CRM fora da versão; absent |
| `NF-020` | help center, central de ajuda, contextual help | `rg -i 'central de ajuda|help center|ajuda' ...` + file-name scan | nenhuma rota/tela/conteúdo de ajuda: absent |
| `NF-022` | import existing/device history | `rg -i 'importHistory|import.*histor|history.*import' ...` | incoming registra somente eventos novos; nenhum importer: absent |
| `NF-023` | scheduled campaign edit/preview | `rg -i 'ScheduledMessage|campaign.*schedule|agendamento.*disparo' ...` | nenhum campaign scheduler; absent |
| `NF-024` | viewer, consult-only role | `rg -i 'VIEWER|consulta.*papel|read.?only role' ...` | comentários e ADR-0018 confirmam remoção deliberada; absent/by-design |
| `NF-026` | privacy, terms, deletion request | `rg -i 'privacidade|privacy|termos de servico|terms of service' ...` + public route scan | nenhuma página/rota correspondente: absent |
| `NF-027` | auto-reply detection/filter | `rg -i 'resposta automatica|auto.?reply|automatic.?reply' ...` | nenhum classificador/filtro; absent |

## 7. Ledger de unidades-fonte

O ledger abaixo contém uma unidade por commit atômico observado no histórico admitido, cinco sentinelas para commits fora da allowlist sem inspeção de path e o overlay histórico. O tipo de mapeamento é derivado das colunas `capability_ids[]`, `supports[]`, `duplicate_of[]` e `excluded_reason`; referências múltiplas são separadas por vírgula. Para sentinelas `outside_st02`, `path=@outside-allowlist` é permitido exclusivamente porque o path real não foi inspecionado.

### 7.1 Cobertura do ledger

- Unidades totais: `204` (`official=133`, `hub=70`, `legacy_overlay=1`).
- Unidades mapeadas para capacidade/suporte: `177`; exclusões justificadas: `27`.
- População de commits: `196/196`; superfícies baseline adicionais: `8`.

| source_unit_id | origin | sha | path | locator | source_unit_type | capability_ids[] | supports[] | duplicate_of[] | excluded_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SU-b4a10377939f8859` | `official` | `a85584f907ab3b235e480bb8252c63d165fe6285` | `@outside-allowlist` | `commit-a85584f907ab` | `commit_surface` | `[]` | `[]` | `[]` | `outside_st02: no admitted path touched` |
| `SU-f2546ace58bf9f45` | `official` | `6d4310104ce71515ad765454eb59ad7e9074ba87` | `@outside-allowlist` | `commit-6d4310104ce7` | `commit_surface` | `[]` | `[]` | `[]` | `outside_st02: no admitted path touched` |
| `SU-0efdb4210134a3ec` | `official` | `10be6a38992f7bd3e27adf2ff4e663607c9571e7` | `@outside-allowlist` | `commit-10be6a38992f` | `commit_surface` | `[]` | `[]` | `[]` | `outside_st02: no admitted path touched` |
| `SU-3be20c8c9ec95d16` | `official` | `aed3c40aaf673121d7dd6ea959f7ed68d61dcd21` | `public/index.html` | `commit-aed3c40aaf67` | `commit_surface` | `[CAP-008]` | `[]` | `[]` | `null` |
| `SU-1f6e1c3605655814` | `official` | `5fd5317aa546813d82ed08a60ce43cc7567cb0b7` | `migrations/015-midia-recebida.sql` | `commit-5fd5317aa546` | `commit_surface` | `[CAP-007]` | `[]` | `[]` | `null` |
| `SU-cb08ec3bc32b11c5` | `official` | `a9d10cd5216931ad2369616cced8bb9aac89172f` | `CONTEXTO-CONTINUIDADE.txt` | `commit-a9d10cd52169` | `commit_surface` | `[]` | `[CAP-007]` | `[]` | `null` |
| `SU-8a4963a068f5c264` | `official` | `c34c418d938ddc7f86e43c4352849283e80b8db0` | `src/index.js` | `commit-c34c418d938d` | `commit_surface` | `[CAP-009]` | `[]` | `[]` | `null` |
| `SU-cc504a9aa6e3ff6c` | `official` | `18882381321120f1e888f16a4211354f12138726` | `src/index.js` | `commit-188823813211` | `commit_surface` | `[CAP-003]` | `[]` | `[]` | `null` |
| `SU-7285650176d7dd3e` | `official` | `f8823c9013292b7ee7bd5c50ef476a9ee91faaa6` | `migrations/016-received-at-iso.sql` | `commit-f8823c901329` | `commit_surface` | `[CAP-010]` | `[]` | `[]` | `null` |
| `SU-1706c62716fe0dca` | `official` | `bfab20fd07127c6f92c4aac3184ee6ac4f86c5b0` | `migrations/017-modulo-consulta.sql` | `commit-bfab20fd0712` | `commit_surface` | `[CAP-011,CAP-024]` | `[]` | `[]` | `null` |
| `SU-6f0c025d7364509f` | `official` | `c2febe73ab2c74695ed9598433257cbe5a2d51bf` | `migrations/018-transferencia-setores.sql` | `commit-c2febe73ab2c` | `commit_surface` | `[CAP-013]` | `[]` | `[]` | `null` |
| `SU-5d2c9d636fad7c69` | `official` | `0b862ad1ea79097c2aeaa958ef5e003fe7009379` | `migrations/019-crm.sql` | `commit-0b862ad1ea79` | `commit_surface` | `[CAP-015]` | `[]` | `[]` | `null` |
| `SU-80df5c7d8fe52b6f` | `official` | `96c3eeee73189bd6b66521791023d82a3bc9611d` | `public/index.html` | `commit-96c3eeee7318` | `commit_surface` | `[CAP-024]` | `[]` | `[]` | `null` |
| `SU-33d6d5e6edfadf54` | `official` | `7ffd26600eea85212cbd7f6f40126d56734119c9` | `src/index.js` | `commit-7ffd26600eea` | `commit_surface` | `[CAP-003]` | `[]` | `[]` | `null` |
| `SU-c2d893fa034649f9` | `official` | `a10bb1481518242f442dc0b7f3ddc827e946f54d` | `src/index.js` | `commit-a10bb1481518` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-a00bfcfe859e2e02` | `official` | `e563d95159336955fd8b4ab434d89e66a81224bd` | `src/index.js` | `commit-e563d9515933` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-a45c2f7305104342` | `official` | `3e625645799dffdd3757928faf349e88c5c4078e` | `src/index.js` | `commit-3e625645799d` | `commit_surface` | `[CAP-012,CAP-003]` | `[]` | `[]` | `null` |
| `SU-a43695d00991db25` | `official` | `1cdfdd9535232409ef44ea69a3575fd7bd12c619` | `migrations/020-numero-visivel.sql` | `commit-1cdfdd953523` | `commit_surface` | `[CAP-025]` | `[]` | `[]` | `null` |
| `SU-fa56dc0cd7ddff35` | `official` | `26c9a03b7ffdd8ffdc7271a7f2c515965c3f2155` | `src/index.js` | `commit-26c9a03b7ffd` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-47d1b9b63022deb8` | `official` | `0997b3310c6ccf94261fe880e70eb6230d231ec0` | `src/index.js` | `commit-0997b3310c6c` | `commit_surface` | `[CAP-011]` | `[]` | `[]` | `null` |
| `SU-601c669d75885c92` | `official` | `a047c48e74969e95bddd52a92c76057250197b50` | `migrations/021-crm-hub.sql` | `commit-a047c48e7496` | `commit_surface` | `[CAP-015]` | `[]` | `[]` | `null` |
| `SU-42a947e477aa8674` | `official` | `536607e88d661670ced6cc3add62820f88f2b47f` | `migrations/022-hub-por-setor.sql` | `commit-536607e88d66` | `commit_surface` | `[CAP-015]` | `[]` | `[]` | `null` |
| `SU-2f4abf507c6557a8` | `official` | `6da85b8e13d8e8d2a503d4c07bf0dfe4b527e38a` | `src/index.js` | `commit-6da85b8e13d8` | `commit_surface` | `[CAP-011]` | `[]` | `[]` | `null` |
| `SU-943e5ce766b4074e` | `official` | `a277b1e8d449f6d43d7f20f866034be0afd6ce73` | `src/index.js` | `commit-a277b1e8d449` | `commit_surface` | `[CAP-003]` | `[]` | `[]` | `null` |
| `SU-ce6c73453fa2389d` | `official` | `bf1f139b93794cb4f3a3e09084f090f84bb370ad` | `migrations/021-finalizar-atendimento.sql` | `commit-bf1f139b9379` | `commit_surface` | `[CAP-014]` | `[]` | `[]` | `null` |
| `SU-dd50eb91b87e3def` | `official` | `7bba710dec0fa0fe78a71a5b9050525fc1c55e12` | `src/index.js` | `commit-7bba710dec0f` | `commit_surface` | `[CAP-007]` | `[]` | `[]` | `null` |
| `SU-2c3ef2677aecf52d` | `official` | `2a477b40b4ac20b7f1b2170e6de134ced81c533a` | `CONTEXTO-CONTINUIDADE.txt` | `commit-2a477b40b4ac` | `commit_surface` | `[]` | `[CAP-007]` | `[]` | `null` |
| `SU-4e07252238377732` | `official` | `04066ba323c64ec99b8572a7eb46da28fb2b3b11` | `CONTEXTO-CONTINUIDADE.txt` | `commit-04066ba323c6` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-0695274bcf8e9482` | `official` | `9582037200a2dfb146f55f50095e59c1e0b44784` | `public/index.html` | `commit-9582037200a2` | `commit_surface` | `[CAP-020]` | `[]` | `[]` | `null` |
| `SU-87d620314b5a5b21` | `official` | `15f95a6943cf19d6e995d1d2c013181f1ffb9cc1` | `docs/README.md` | `commit-15f95a6943cf` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-20904aad0b2a336f` | `official` | `cbeb6b4930a19f7cfad80e4cc7ea13ad3b138ab3` | `src/index.js` | `commit-cbeb6b4930a1` | `commit_surface` | `[CAP-003]` | `[]` | `[]` | `null` |
| `SU-a2a87f7e2f26fefd` | `official` | `4dc02047327e0ab8c1a80c7e0fdc53665e1f96c4` | `public/index.html` | `commit-4dc02047327e` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-457ffd486db97683` | `official` | `7af860116ddc679f048cc942f5da150fe4d1bb30` | `public/index.html` | `commit-7af860116ddc` | `commit_surface` | `[CAP-003]` | `[]` | `[]` | `null` |
| `SU-123f0b3565594428` | `official` | `f86a46fca49f01361a8a1155a65697cb76682d34` | `public/index.html` | `commit-f86a46fca49f` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-45588f6abf5d12b7` | `official` | `a7fc42a6a50a52be8f4920d7a691685fe2549ddf` | `public/index.html` | `commit-a7fc42a6a50a` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-02d6eb4b6b91a256` | `official` | `5d66ad00e6b910fa964090f3b81f6d05ec7236b2` | `public/index.html` | `commit-5d66ad00e6b9` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-dce310684560c1cc` | `official` | `f75abaae06344e6565b3e3526de31b49334f4297` | `public/index.html` | `commit-f75abaae0634` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-3eada8e805d436dc` | `official` | `c670c93f47795eaac18f888f2c517a88969bd77a` | `src/index.js` | `commit-c670c93f4779` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-1ceb2b6af68f48c5` | `official` | `6c145a081bec8dd412a11837a0e1106343292ad9` | `public/index.html` | `commit-6c145a081bec` | `commit_surface` | `[CAP-008]` | `[]` | `[]` | `null` |
| `SU-357b19f3fde42fab` | `official` | `288ed9e7d2051713f4dde7ff2593e204a40eb265` | `public/index.html` | `commit-288ed9e7d205` | `commit_surface` | `[CAP-008]` | `[]` | `[]` | `null` |
| `SU-135f8885a289831e` | `official` | `6ee56e475a41fa247d6d6a96a1641fb4f2463202` | `CONTEXTO-CONTINUIDADE.txt` | `commit-6ee56e475a41` | `commit_surface` | `[]` | `[CAP-003]` | `[]` | `null` |
| `SU-13abc4fdd31748d9` | `official` | `eb87b11a0cd560a0e0d7426fe64025b37d957bad` | `docs/api-conversas.html` | `commit-eb87b11a0cd5` | `commit_surface` | `[]` | `[CAP-007,CAP-003]` | `[]` | `null` |
| `SU-158cfff697bf3098` | `official` | `084b18e0672108ee8af0d49b3f5a08adc0d290f9` | `CONTEXTO-CONTINUIDADE.txt` | `commit-084b18e06721` | `commit_surface` | `[]` | `[CAP-005]` | `[]` | `null` |
| `SU-4b4b4c350f725ea6` | `official` | `90b733a5f948c1887004867ccbd9623a9b93ed04` | `migrations/023-disparo-com-fluxo.sql` | `commit-90b733a5f948` | `commit_surface` | `[CAP-007,CAP-004]` | `[]` | `[]` | `null` |
| `SU-8db882fba59bef2d` | `official` | `816c22b4956af824dff375bd552e3dec0fd4f1bb` | `docs/api-conversas.html` | `commit-816c22b4956a` | `commit_surface` | `[]` | `[CAP-004]` | `[]` | `null` |
| `SU-0280861125081068` | `official` | `edb795470f10a4ea3678e5c53057b8c4c4d44045` | `src/index.js` | `commit-edb795470f10` | `commit_surface` | `[CAP-013]` | `[]` | `[]` | `null` |
| `SU-243d253de28ff1d9` | `official` | `8986580c0bd45dd7bc65e885a0ebb30bbdd580b2` | `public/index.html` | `commit-8986580c0bd4` | `commit_surface` | `[CAP-013]` | `[]` | `[]` | `null` |
| `SU-774fb923110b7e66` | `official` | `d164c9b803619580f4aa606d8f607cc34cf450cb` | `CONTEXTO-CONTINUIDADE.txt` | `commit-d164c9b80361` | `commit_surface` | `[]` | `[CAP-013]` | `[]` | `null` |
| `SU-f23676cd7b79db99` | `official` | `d9952aec59a3e4b8650a9ca17ef1c0b268429dad` | `migrations/024-conversa-exclusiva.sql` | `commit-d9952aec59a3` | `commit_surface` | `[CAP-013]` | `[]` | `[]` | `null` |
| `SU-2b24449ce807e8af` | `official` | `155c4eca16263be95f348843a193366d2f3b4d35` | `CONTEXTO-CONTINUIDADE.txt` | `commit-155c4eca1626` | `commit_surface` | `[]` | `[CAP-013]` | `[]` | `null` |
| `SU-3a7d125251a33a55` | `official` | `e3c28d7e157bfbb650416740c78c371fb83bcdc0` | `public/index.html` | `commit-e3c28d7e157b` | `commit_surface` | `[CAP-004]` | `[]` | `[]` | `null` |
| `SU-dc5ac99b3acd5a3f` | `official` | `2ac248796882fe8c675078813bd4952e77f381f2` | `public/index.html` | `commit-2ac248796882` | `commit_surface` | `[CAP-004]` | `[]` | `[]` | `null` |
| `SU-073673c3162bbd6d` | `official` | `d294466bc8eb9f262437246136f4c8009e05e770` | `src/index.js` | `commit-d294466bc8eb` | `commit_surface` | `[CAP-012,CAP-004]` | `[]` | `[]` | `null` |
| `SU-84213b08fe0d60e1` | `official` | `d9b4764e6cbd0796676cef538c3e3d7cbd633878` | `CONTEXTO-CONTINUIDADE.txt` | `commit-d9b4764e6cbd` | `commit_surface` | `[]` | `[CAP-012]` | `[]` | `null` |
| `SU-08e874019d53273e` | `official` | `9e69b18e6ca6621729b1f1b065f2cd4a5a70d19e` | `src/index.js` | `commit-9e69b18e6ca6` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-caad49e9329ab0fe` | `official` | `6d0d2034186800e6a57db5d8b5b9cf09de128968` | `src/index.js` | `commit-6d0d20341868` | `commit_surface` | `[CAP-004]` | `[]` | `[]` | `null` |
| `SU-987e59dc930e67e9` | `official` | `26a881f5a616e8be2276592f235c1570546502aa` | `CONTEXTO-CONTINUIDADE.txt` | `commit-26a881f5a616` | `commit_surface` | `[]` | `[CAP-004]` | `[]` | `null` |
| `SU-cd62a1a76ffb878a` | `official` | `33de4bda706f51ba36a02c7c84a0a9c1c43bd260` | `migrations/025-disparo-de-teste.sql` | `commit-33de4bda706f` | `commit_surface` | `[CAP-004]` | `[]` | `[]` | `null` |
| `SU-9034638d43d67bb2` | `official` | `9037bfbb493e12e0f95e64afde8796b8e4bde986` | `CONTEXTO-CONTINUIDADE.txt` | `commit-9037bfbb493e` | `commit_surface` | `[]` | `[CAP-004]` | `[]` | `null` |
| `SU-e63cb98cd711c991` | `official` | `82250088d9b9e74a58a37f39b506b00272eb46ee` | `src/index.js` | `commit-82250088d9b9` | `commit_surface` | `[CAP-025]` | `[]` | `[]` | `null` |
| `SU-82786d138e1ff9aa` | `official` | `b2b5dd07bf7f66b62b0775a88b63f0c47c1ec226` | `CONTEXTO-CONTINUIDADE.txt` | `commit-b2b5dd07bf7f` | `commit_surface` | `[]` | `[CAP-025]` | `[]` | `null` |
| `SU-7b755a8e4c4687c2` | `official` | `108b668f7deda5444f37f4e4ec943e7ed9a8f63f` | `src/index.js` | `commit-108b668f7ded` | `commit_surface` | `[CAP-025]` | `[]` | `[]` | `null` |
| `SU-88751f90705da2c0` | `official` | `1f4b8a56ee9963bd5294d70178e0c5edd56b5f66` | `CONTEXTO-CONTINUIDADE.txt` | `commit-1f4b8a56ee99` | `commit_surface` | `[]` | `[CAP-025]` | `[]` | `null` |
| `SU-ac918031ce2721e7` | `official` | `4ea2dd0909cab3065950ed2e32095050013a3f90` | `migrations/026-acesso-ao-hub.sql` | `commit-4ea2dd0909ca` | `commit_surface` | `[CAP-018]` | `[]` | `[]` | `null` |
| `SU-4128e635acf49330` | `official` | `cb3a1360b6e131524fdc10c4b2d457e77527d408` | `CONTEXTO-CONTINUIDADE.txt` | `commit-cb3a1360b6e1` | `commit_surface` | `[]` | `[CAP-018]` | `[]` | `null` |
| `SU-8ed17a41d221fba3` | `official` | `b55fea8cd05728ee98e8dcb3793181ca193f410c` | `README.md` | `commit-b55fea8cd057` | `commit_surface` | `[CAP-009]` | `[]` | `[]` | `null` |
| `SU-2f0f263820ac65fa` | `official` | `b6adf9b8bbacbd961455d160fde11d3083f5aa65` | `src/index.js` | `commit-b6adf9b8bbac` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-6e711561717f4c01` | `official` | `58d44940febd4d42532deda0a2e360dc0bded7ea` | `CONTEXTO-CONTINUIDADE.txt` | `commit-58d44940febd` | `commit_surface` | `[]` | `[CAP-017]` | `[]` | `null` |
| `SU-e458f71c5343a4fc` | `official` | `f3ec7bab8b79e0f9e69b784b779c71ff9aaf57cd` | `CONTEXTO-CONTINUIDADE.txt` | `commit-f3ec7bab8b79` | `commit_surface` | `[]` | `[CAP-001]` | `[]` | `null` |
| `SU-89babca8fbaebd5b` | `official` | `13e4ae4296c36a5947a585a23fce17fea80f8d15` | `src/index.js` | `commit-13e4ae4296c3` | `commit_surface` | `[CAP-007,CAP-008]` | `[]` | `[]` | `null` |
| `SU-5c0c2fed68b58e09` | `official` | `846b6f4ea107e156d43cd45827d7f19b99c91f8c` | `CONTEXTO-CONTINUIDADE.txt` | `commit-846b6f4ea107` | `commit_surface` | `[]` | `[CAP-007]` | `[]` | `null` |
| `SU-4293d8fd2f728530` | `official` | `db218a55043845d89512c167b5386a478d70e019` | `migrations/027-entrega-e-leitura.sql` | `commit-db218a550438` | `commit_surface` | `[CAP-016,CAP-003]` | `[]` | `[]` | `null` |
| `SU-1865426226c75b67` | `official` | `d41e96066d4426512bb4d10f407d8d2d345feb4b` | `CONTEXTO-CONTINUIDADE.txt` | `commit-d41e96066d44` | `commit_surface` | `[]` | `[CAP-016]` | `[]` | `null` |
| `SU-b2928e76b4bb7293` | `official` | `1470a7d728270faca79dd4bf8bf67d32def1e29a` | `src/index.js` | `commit-1470a7d72827` | `commit_surface` | `[CAP-007]` | `[]` | `[]` | `null` |
| `SU-7b1192ceee0d8841` | `official` | `6e5847e95368220914914038fe8b15440279026d` | `CONTEXTO-CONTINUIDADE.txt` | `commit-6e5847e95368` | `commit_surface` | `[]` | `[CAP-007]` | `[]` | `null` |
| `SU-8286435c80060a32` | `official` | `8d2c1088073f624c3f051d0caa69a2f56115150f` | `migrations/028-entrega-nas-mensagens.sql` | `commit-8d2c1088073f` | `commit_surface` | `[CAP-016]` | `[]` | `[]` | `null` |
| `SU-b54d21b580d88a92` | `official` | `abc0dc182bac3c3df4028247ca2aba91a0fec747` | `docs/api-conversas.html` | `commit-abc0dc182bac` | `commit_surface` | `[]` | `[CAP-016]` | `[]` | `null` |
| `SU-e8b5c190235716e1` | `official` | `089374c5e463723f40721131af79996faaff814b` | `public/privacidade.html` | `commit-089374c5e463` | `commit_surface` | `[CAP-026]` | `[]` | `[]` | `null` |
| `SU-bbcbf2143cc3fcdc` | `official` | `1398fa20b229de06a0f9e362a6c941f4c6dcf785` | `src/index.js` | `commit-1398fa20b229` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-e3a04dfa5852b9bd` | `official` | `688af3e16ec07c2522eb02ac0f8a6308d06bff75` | `CONTEXTO-CONTINUIDADE.txt` | `commit-688af3e16ec0` | `commit_surface` | `[]` | `[CAP-017]` | `[]` | `null` |
| `SU-17122e7d703eaea2` | `official` | `99b0150255a15bef47d37bb2986cf18ce3316337` | `CONTEXTO-CONTINUIDADE.txt` | `commit-99b0150255a1` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-b55fa2cc55699849` | `official` | `c6f847eba80c29c4ddd0a7952303d38154649889` | `wrangler.jsonc` | `commit-c6f847eba80c` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-a8cbba0710f40830` | `official` | `16369a7927e6c87981e3f4f58d89bfc0d06ac440` | `wrangler.jsonc` | `commit-16369a7927e6` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-084726b2a5cd7a85` | `official` | `8edcd8f678d4860ed46dbec1a8b4b29ae1c0fcd3` | `public/privacidade.html` | `commit-8edcd8f678d4` | `commit_surface` | `[CAP-026]` | `[]` | `[]` | `null` |
| `SU-0b769e14a86f6489` | `official` | `50c0745fb6d6a917e5f4d276813fc54b5ae8cd21` | `public/termos.html` | `commit-50c0745fb6d6` | `commit_surface` | `[CAP-026]` | `[]` | `[]` | `null` |
| `SU-21c269073451f229` | `official` | `23d7bef6e01db04c07b151ccdbef68d4fb26932d` | `public/privacidade.html` | `commit-23d7bef6e01d` | `commit_surface` | `[CAP-026]` | `[]` | `[]` | `null` |
| `SU-0c7c4dac50619774` | `official` | `0c27c0256e5136f4047eee4bc13c7a207a3ca9ff` | `CONTEXTO-CONTINUIDADE.txt` | `commit-0c27c0256e51` | `commit_surface` | `[]` | `[CAP-026]` | `[]` | `null` |
| `SU-87411772f6813892` | `official` | `478be4f8418de833459dd544ca054b9bb04a085a` | `schema.sql` | `commit-478be4f8418d` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-8092dafeccce3b29` | `official` | `c8f4acc08fad3c84feff87d2e614ba3c154e08b9` | `migrations/029-cabecalho-de-midia.sql` | `commit-c8f4acc08fad` | `commit_surface` | `[CAP-001]` | `[]` | `[]` | `null` |
| `SU-cf32d3208e836a70` | `official` | `01c9f0f8f3f6bf14f41d1f7bb8391304456f8815` | `src/index.js` | `commit-01c9f0f8f3f6` | `commit_surface` | `[CAP-016]` | `[]` | `[]` | `null` |
| `SU-5c4296c2a4d76173` | `official` | `7e768094fc8397b86d2efc7984f70ef72bd17562` | `public/index.html` | `commit-7e768094fc83` | `commit_surface` | `[CAP-002]` | `[]` | `[]` | `null` |
| `SU-6ad09c052f08e30f` | `official` | `765b57d5e83f34d023b9364fffa19532ccdcd0a9` | `migrations/030-agente-ia.sql` | `commit-765b57d5e83f` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-cb1250afb688b9bc` | `official` | `1c0db64287fe5dee4a0f3c6e8962a7c54a0028b9` | `migrations/031-agente-widget.sql` | `commit-1c0db64287fe` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-c87837b0e5aafacb` | `official` | `a39bf02bab208efc21da05c181dbe0194e718e99` | `public/ajuda.js` | `commit-a39bf02bab20` | `commit_surface` | `[CAP-019,CAP-020]` | `[]` | `[]` | `null` |
| `SU-af6e06c285611930` | `official` | `932330f227d7fa762e1c9f752ae70326b5d40e6f` | `src/agente.js` | `commit-932330f227d7` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-8e9e465f1c60c669` | `official` | `0de4809695c0e912aa00bd5ff75685833fb8a549` | `src/agente.js` | `commit-0de4809695c0` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-e5487c57fcfb97f6` | `official` | `f64bba3b858828cfa0e1b85016fa5490b123529e` | `CONTEXTO-CONTINUIDADE.txt` | `commit-f64bba3b8588` | `commit_surface` | `[]` | `[CAP-019]` | `[]` | `null` |
| `SU-55b64da66a69dd82` | `official` | `8c2102288227fec4716e9d2b5ed5fcd3e8c535f8` | `migrations/032-agente-lixeira.sql` | `commit-8c2102288227` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-fba7631e55d429b8` | `official` | `39c8d902f7fe5f24ba2286e3fb33b6c0f6cb1a47` | `src/agente.js` | `commit-39c8d902f7fe` | `commit_surface` | `[CAP-019,CAP-011]` | `[]` | `[]` | `null` |
| `SU-8c0d37ad043c11b3` | `official` | `fdf0d0e5719d7c65ae9c066240921243cefdcdb3` | `migrations/033-disparo-com-agente.sql` | `commit-fdf0d0e5719d` | `commit_surface` | `[CAP-019,CAP-004]` | `[]` | `[]` | `null` |
| `SU-ff711d94230a372a` | `official` | `aa68e625b65a09363ea5f353f62daaf0ddf3564e` | `migrations/034-modulo-agentes.sql` | `commit-aa68e625b65a` | `commit_surface` | `[CAP-019,CAP-024]` | `[]` | `[]` | `null` |
| `SU-cb84b7402fb6f18a` | `official` | `6cf96922bc7b7445391bfc1d9b293e9f348325ee` | `src/index.js` | `commit-6cf96922bc7b` | `commit_surface` | `[CAP-015]` | `[]` | `[]` | `null` |
| `SU-93a6ffa649ed2b03` | `official` | `ad4c9314cec3a8b6cf6bcd04bc152a118f8a0d44` | `public/index.html` | `commit-ad4c9314cec3` | `commit_surface` | `[CAP-015]` | `[]` | `[]` | `null` |
| `SU-4245afd93581d8f5` | `official` | `ee42e0500cdf84acd6289a8b5d3e66e46004253a` | `src/index.js` | `commit-ee42e0500cdf` | `commit_surface` | `[CAP-002]` | `[]` | `[]` | `null` |
| `SU-6fcccd4ef399031b` | `official` | `5e427b1fd1a18b6d2c886248066c379e87041080` | `public/index.html` | `commit-5e427b1fd1a1` | `commit_surface` | `[CAP-002,CAP-004]` | `[]` | `[]` | `null` |
| `SU-8beea33eb313edd4` | `official` | `234d239c3b472506f8d063ba7d6180c16c4935dd` | `src/index.js` | `commit-234d239c3b47` | `commit_surface` | `[CAP-012,CAP-004]` | `[]` | `[]` | `null` |
| `SU-a9891460df66882a` | `official` | `14ad8ea92e730d246a627b60616dcc6cb52d5d15` | `src/index.js` | `commit-14ad8ea92e73` | `commit_surface` | `[CAP-004]` | `[]` | `[]` | `null` |
| `SU-a0b291aaaefaa6b2` | `official` | `834348da58605549c97334ed6617c5f00fc28f1e` | `src/index.js` | `commit-834348da5860` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-00f28a695ed8f660` | `official` | `fdcd5556487adb397320add78735b19abb512807` | `public/index.html` | `commit-fdcd5556487a` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-06b1f42b7594519c` | `official` | `dc2cf5b4dfeac92776d9207305f1229d8d1c17d7` | `public/index.html` | `commit-dc2cf5b4dfea` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-e0dbdaa1aa5d4305` | `official` | `98895122e265afdcbd9df0f90253d5455c021301` | `src/agente.js` | `commit-98895122e265` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-b17b55a8140e998c` | `official` | `9fc70cf1ce7a2589bf27b3079c238ab2af8a6fd4` | `migrations/035-agente-inicio-conversa.sql` | `commit-9fc70cf1ce7a` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-a7e91134c7be5acc` | `official` | `8cf6f26ed2c77e37695b981bb983c94b8b294ce9` | `src/agente.js` | `commit-8cf6f26ed2c7` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-53b5aeb6d1337ef2` | `official` | `9a0389c5bc9a5184779c575e566e71562259b700` | `src/index.js` | `commit-9a0389c5bc9a` | `commit_surface` | `[CAP-002]` | `[]` | `[]` | `null` |
| `SU-354488d6a7419444` | `official` | `81de8fdc1fb6817ac971c43cd7b96554a22ae6c9` | `src/index.js` | `commit-81de8fdc1fb6` | `commit_surface` | `[CAP-002]` | `[]` | `[]` | `null` |
| `SU-5172dd6ce158e333` | `official` | `c0f39b98a4bc9fb58cf22e44a61854315c700854` | `src/index.js` | `commit-c0f39b98a4bc` | `commit_surface` | `[CAP-013,CAP-024]` | `[]` | `[]` | `null` |
| `SU-42ed8bab8a9180c9` | `official` | `05e0bb68628755140ca4d9e68218819e20315f54` | `CONTEXTO-CONTINUIDADE.txt` | `commit-05e0bb686287` | `commit_surface` | `[]` | `[CAP-026,CAP-013]` | `[]` | `null` |
| `SU-4aa78be189afe000` | `official` | `e42c25c19a1bb4cd35c95b946b63e5ed06ba66b3` | `migrations/036-lider-de-setor.sql` | `commit-e42c25c19a1b` | `commit_surface` | `[CAP-013]` | `[]` | `[]` | `null` |
| `SU-09c3c517726bac94` | `official` | `a003c8b1655dbf9ec04d75697dd4634c540a5b99` | `CONTEXTO-CONTINUIDADE.txt` | `commit-a003c8b1655d` | `commit_surface` | `[]` | `[CAP-013]` | `[]` | `null` |
| `SU-1153388b826ddbb2` | `official` | `e170587741229eae5df14f24688eb90a10f276fb` | `clientes/_MODELO-wrangler.jsonc` | `commit-e17058774122` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-337e24b0492974a7` | `official` | `c1469c4a5d75483d09f57f36713c8c4ce05d2ebb` | `CONTEXTO-CONTINUIDADE.txt` | `commit-c1469c4a5d75` | `commit_surface` | `[]` | `[CAP-017]` | `[]` | `null` |
| `SU-fe3a2e0d80357ad0` | `official` | `ad30af3dce2ec6bb4b6fafc4d57205c3a33ba6bf` | `CONTEXTO-CONTINUIDADE.txt` | `commit-ad30af3dce2e` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-1e1ec02439769f76` | `official` | `ab87dc8e36082272366f5a96ea73b522b79abd4d` | `src/index.js` | `commit-ab87dc8e3608` | `commit_surface` | `[CAP-008]` | `[]` | `[]` | `null` |
| `SU-d0a769f7a4de2792` | `official` | `43d080fa1024aea87fec21e27b943b9a83cd54d5` | `migrations/037-agente-fora-do-horario.sql` | `commit-43d080fa1024` | `commit_surface` | `[CAP-019,CAP-004]` | `[]` | `[]` | `null` |
| `SU-4a8e0138a6c68617` | `official` | `ea49f55e480cfae52ca1234a9dc83cf5210128d6` | `src/agente.js` | `commit-ea49f55e480c` | `commit_surface` | `[CAP-004]` | `[]` | `[]` | `null` |
| `SU-eef1fe9b583e458e` | `official` | `0537da9af13fb46915184db8b4aa0404dce47927` | `migrations/038-resposta-automatica-do-contato.sql` | `commit-0537da9af13f` | `commit_surface` | `[CAP-027]` | `[]` | `[]` | `null` |
| `SU-d3ea5f5e93f6923c` | `official` | `1ca649541bc95b823f68a7136e691565ce33692e` | `src/index.js` | `commit-1ca649541bc9` | `commit_surface` | `[CAP-027]` | `[]` | `[]` | `null` |
| `SU-b68646866f7273e6` | `official` | `622da56ca8e2e58ae4c425e830d49b7c88a09243` | `src/index.js` | `commit-622da56ca8e2` | `commit_surface` | `[CAP-027]` | `[]` | `[]` | `null` |
| `SU-62d8941dacfb2e13` | `official` | `b84891e5658bbb7b61e054cd6268fe8feb90b688` | `src/agente.js` | `commit-b84891e5658b` | `commit_surface` | `[CAP-019]` | `[]` | `[]` | `null` |
| `SU-8a6d956710a52007` | `hub` | `f93965e37b6f975925fd21578d81d3071ad220f5` | `@outside-allowlist` | `commit-f93965e37b6f` | `commit_surface` | `[]` | `[]` | `[]` | `outside_st02: no admitted path touched` |
| `SU-7c4a382deaf90802` | `hub` | `49ff5a0359b8c0a7ae2d94bad61c56a7db875ca3` | `@outside-allowlist` | `commit-49ff5a0359b8` | `commit_surface` | `[]` | `[]` | `[]` | `outside_st02: no admitted path touched` |
| `SU-2a2cd246b70162fe` | `hub` | `7801d83f09eb7c2406dc10fde606c7e58e6a06df` | `frontend/src/pages/Inbox.tsx` | `commit-7801d83f09eb` | `commit_surface` | `[CAP-025]` | `[]` | `[]` | `null` |
| `SU-531ea3e65199d9c8` | `hub` | `3cd5b228e68b0a9e9ffd2b046b6cec891cc56767` | `frontend/src/styles.css` | `commit-3cd5b228e68b` | `commit_surface` | `[CAP-008]` | `[]` | `[]` | `null` |
| `SU-dbe4895995a9ac76` | `hub` | `bd1609e7c836fdfdad9ca55fd2e7eaf191ec7094` | `frontend/src/pages/Inbox.tsx` | `commit-bd1609e7c836` | `commit_surface` | `[CAP-006]` | `[]` | `[]` | `null` |
| `SU-8508af217993f358` | `hub` | `354f4116f17b3203674b776505dcd5a5d1846c13` | `backend/prisma/schema.prisma` | `commit-354f4116f17b` | `commit_surface` | `[CAP-007,CAP-009]` | `[]` | `[]` | `null` |
| `SU-bded64a7a9379c93` | `hub` | `6e6c44ba1c145737b4d8d94be615c9f4feabaadd` | `backend/src/modules/inbox/routes.ts` | `commit-6e6c44ba1c14` | `commit_surface` | `[CAP-007]` | `[]` | `[]` | `null` |
| `SU-f27f493fc74ef73c` | `hub` | `d73a56a7cbfcc7b694121024902f361f41335336` | `backend/src/modules/instances/routes.ts` | `commit-d73a56a7cbfc` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-eaf14f1511e63c18` | `hub` | `23cbc37ada51e19162809d8333065b5dfdc6c45a` | `backend/prisma/schema.prisma` | `commit-23cbc37ada51` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-1d4df4bfaa05bc39` | `hub` | `341497515f16c89319e3f942c2c0e8f67510643c` | `backend/prisma/schema.prisma` | `commit-341497515f16` | `commit_surface` | `[CAP-024]` | `[]` | `[]` | `null` |
| `SU-dd52f27834547a20` | `hub` | `7e1a6e274c0ebbb65b052ea4bdce607fa6b803f7` | `backend/src/modules/apiV1/routes.ts` | `commit-7e1a6e274c0e` | `commit_surface` | `[CAP-010]` | `[]` | `[]` | `null` |
| `SU-0ce1ef6402fa9047` | `hub` | `54c48b9578c7508a42e771c1fa08327f59cac51b` | `backend/prisma/schema.prisma` | `commit-54c48b9578c7` | `commit_surface` | `[CAP-013]` | `[]` | `[]` | `null` |
| `SU-2d2e15629321daa5` | `hub` | `82dd4866c43defcc0368b0af0c782be77f8d2649` | `frontend/src/pages/Usuarios.tsx` | `commit-82dd4866c43d` | `commit_surface` | `[CAP-024]` | `[]` | `[]` | `null` |
| `SU-fb33053c5bdd3b9f` | `hub` | `c21188c0a7f120323e1487e0f8e1a909767af090` | `backend/src/modules/instances/routes.ts` | `commit-c21188c0a7f1` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-9001fed5c80495a4` | `hub` | `6ec237a65d7dd1dad6c0c7912904cd99a1e1485a` | `frontend/src/pages/Consultar.tsx` | `commit-6ec237a65d7d` | `commit_surface` | `[CAP-011]` | `[]` | `[]` | `null` |
| `SU-49f137b6a62cb115` | `hub` | `00031957e8310b4fbb35e0bd422aa63f53552b30` | `backend/src/modules/instances/importHistory.ts` | `commit-00031957e831` | `commit_surface` | `[CAP-022,CAP-008]` | `[]` | `[]` | `null` |
| `SU-1c125a5d62b006ad` | `hub` | `0674d595160cc1fc9f817b2dfa95b8ed4593c706` | `backend/src/modules/instances/routes.ts` | `commit-0674d595160c` | `commit_surface` | `[CAP-025]` | `[]` | `[]` | `null` |
| `SU-1faf4224c4dbd5c8` | `hub` | `b561c855c6974d0c3c16e53d5a1b8c232368063f` | `frontend/src/pages/Login.tsx` | `commit-b561c855c697` | `commit_surface` | `[CAP-005]` | `[]` | `[]` | `null` |
| `SU-adaaa59b2c836523` | `hub` | `14948092faa3a537c2bab9323813c9db5933af8f` | `backend/src/modules/webhooks/routes.ts` | `commit-14948092faa3` | `commit_surface` | `[CAP-025]` | `[]` | `[]` | `null` |
| `SU-8964668e690f869b` | `hub` | `f87ecf5768d10470fa7e4ceee3a77c77800bd199` | `backend/src/modules/inbox/routes.ts` | `commit-f87ecf5768d1` | `commit_surface` | `[CAP-011]` | `[]` | `[]` | `null` |
| `SU-1769a43c0f6c3a9b` | `hub` | `602afe8e177ac93684c00483bba1f56568c4d648` | `backend/src/modules/inboxHistory/report.ts` | `commit-602afe8e177a` | `commit_surface` | `[CAP-011,CAP-012]` | `[]` | `[]` | `null` |
| `SU-1bbb215d42831a0d` | `hub` | `a118943b808bdc3d14d3f563b091e6541f737a67` | `docs/CONTINUIDADE.md` | `commit-a118943b808b` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-7e9b91cd76a3b2a0` | `hub` | `9c22ca0adc4cdf1c3bd7053c2f542eb3e781c618` | `backend/src/modules/apiV1/routes.ts` | `commit-9c22ca0adc4c` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-b99651166eda5634` | `hub` | `1f9293a8b9cb229c46af38e7ee730f3404b495dc` | `docs/CONTINUIDADE.md` | `commit-1f9293a8b9cb` | `commit_surface` | `[]` | `[CAP-012]` | `[]` | `null` |
| `SU-d966fe3f48469519` | `hub` | `3e3791115bcfd01c7ba1146f400605a792aacb74` | `backend/src/modules/apiV1/routes.ts` | `commit-3e3791115bcf` | `commit_surface` | `[CAP-012]` | `[]` | `[]` | `null` |
| `SU-0b0ce5d224e77d7d` | `hub` | `7ba4a7171162cc419545e64c3e948654abc564e3` | `docs/CONTINUIDADE.md` | `commit-7ba4a7171162` | `commit_surface` | `[]` | `[CAP-012]` | `[]` | `null` |
| `SU-6abb8ad01e981633` | `hub` | `66d58ab0b32b2d861c7d78905871a61e9d393806` | `backend/src/modules/inboxHistory/routes.ts` | `commit-66d58ab0b32b` | `commit_surface` | `[CAP-011]` | `[]` | `[]` | `null` |
| `SU-3e1e28859889275d` | `hub` | `0a965501ae9fa9b3aa67b2ef1e0cac0025a45f95` | `docs/CONTINUIDADE.md` | `commit-0a965501ae9f` | `commit_surface` | `[]` | `[CAP-011]` | `[]` | `null` |
| `SU-a00a492efdc62ce6` | `hub` | `5eee8ee438f6e8fe66d339e295bd2e879616c9c9` | `frontend/src/pages/Consultar.tsx` | `commit-5eee8ee438f6` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-d900aa027f0971ba` | `hub` | `05651c2f348027ed8aed7f06fda0b7b3574fea36` | `frontend/src/pages/Usuarios.tsx` | `commit-05651c2f3480` | `commit_surface` | `[CAP-024]` | `[]` | `[]` | `null` |
| `SU-3f376aa95b8b1597` | `hub` | `299915b128d9424e3eb8afcddd7f51f54d208f9e` | `docs/CONTINUIDADE.md` | `commit-299915b128d9` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-e2a03222ae5fd77a` | `hub` | `ae05aca381db2775a218f39405baf2a7fbf54ffa` | `backend/src/modules/apiV1/routes.ts` | `commit-ae05aca381db` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-9b044cc20cdce338` | `hub` | `f4061c854407751cb3526692a6bd4e5b23cd7ce7` | `docs/CONTINUIDADE.md` | `commit-f4061c854407` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-8ac1ab487925046b` | `hub` | `da7c336bd2628614a54940331f1a8b26ff2aaa2c` | `backend/prisma/schema.prisma` | `commit-da7c336bd262` | `commit_surface` | `[CAP-007,CAP-005]` | `[]` | `[]` | `null` |
| `SU-a43f730b9cd84450` | `hub` | `5230192f4d69a7caae51f1162c05dec17664b200` | `backend/src/modules/apiV1/routes.ts` | `commit-5230192f4d69` | `commit_surface` | `[CAP-007,CAP-005]` | `[]` | `[]` | `null` |
| `SU-e0b7bbbe2d4a09ad` | `hub` | `45137abb35337b428a363a3cb2bf1e96d84c81a9` | `docs/CONTINUIDADE.md` | `commit-45137abb3533` | `commit_surface` | `[]` | `[CAP-007,CAP-005]` | `[]` | `null` |
| `SU-b575afffddc1c983` | `hub` | `97d2985b0acda870b8255411be843b29ccdf5bc0` | `frontend/src/pages/Login.tsx` | `commit-97d2985b0acd` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-dbfe88990545738e` | `hub` | `83c6425b8e68089a589d48920b758b596da75970` | `frontend/src/components/Layout.tsx` | `commit-83c6425b8e68` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-15280bf571fe4c85` | `hub` | `0e0f201ea96632ed97dc7798008b2b04ea97aece` | `frontend/src/pages/Login.tsx` | `commit-0e0f201ea966` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-8471e91484555b06` | `hub` | `2a894c429ea612f0906db212bb72e90600a8d888` | `frontend/src/components/Layout.tsx` | `commit-2a894c429ea6` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-c766819a019f0595` | `hub` | `fdb0f0989ef10608217e9cbb4c29ed8241aa9716` | `backend/src/modules/apiV1/routes.ts` | `commit-fdb0f0989ef1` | `commit_surface` | `[]` | `[]` | `[]` | `non_behavioral_chore: cosmetic, documentation-only, generated-sync or out-of-catalog change` |
| `SU-6e82e4582308583a` | `hub` | `53ded7b2f233270cebf6b6f67b0b1d13707ea049` | `docs/CONTINUIDADE.md` | `commit-53ded7b2f233` | `commit_surface` | `[]` | `[CAP-008]` | `[]` | `null` |
| `SU-ce02209d98e03cde` | `hub` | `7f044057f531879588c0453b7ec725a296bed452` | `backend/prisma/schema.prisma` | `commit-7f044057f531` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-aca9a028a6fa0bef` | `hub` | `b7bb49f8df42de00f8528c2deb8b05d39c2b7d4f` | `docs/CONTINUIDADE.md` | `commit-b7bb49f8df42` | `commit_surface` | `[]` | `[CAP-021]` | `[]` | `null` |
| `SU-39bbe0defbb55b54` | `hub` | `bcc8918c795e928ac527eeacb817607e739c8cd4` | `backend/prisma/schema.prisma` | `commit-bcc8918c795e` | `commit_surface` | `[CAP-007,CAP-003]` | `[]` | `[]` | `null` |
| `SU-15db0a83a690f5e5` | `hub` | `9ef5c00aae97bb2ff993d40b0792452323346139` | `frontend/src/styles.css` | `commit-9ef5c00aae97` | `commit_surface` | `[CAP-007,CAP-008]` | `[]` | `[]` | `null` |
| `SU-69bf8a1db59dc46b` | `hub` | `48acb0ad2cbddd83751d2dfd08082d97b4b5de07` | `docs/CONTINUIDADE.md` | `commit-48acb0ad2cbd` | `commit_surface` | `[]` | `[CAP-007,CAP-003]` | `[]` | `null` |
| `SU-cf7044a7e6f5a9e1` | `hub` | `b7ab36a412dad4e3cc66c6bde429605a8a47e89b` | `backend/src/auth/central.ts` | `commit-b7ab36a412da` | `commit_surface` | `[CAP-018]` | `[]` | `[]` | `null` |
| `SU-610cb66cc08e34fb` | `hub` | `29021568fef00a27859c3dba58758a3fed86104e` | `docs/CONTINUIDADE.md` | `commit-29021568fef0` | `commit_surface` | `[]` | `[CAP-018]` | `[]` | `null` |
| `SU-5389ecda5a346dc4` | `hub` | `26d484ad11a43b2fc8ce709b957d3bf61d64c4a0` | `backend/src/modules/media/disparoStore.ts` | `commit-26d484ad11a4` | `commit_surface` | `[CAP-007,CAP-003]` | `[]` | `[]` | `null` |
| `SU-2639da94c5bbf5c4` | `hub` | `e3032d18a31e07526ab8c1cec990db56a31571d9` | `docs/CONTINUIDADE.md` | `commit-e3032d18a31e` | `commit_surface` | `[]` | `[CAP-007]` | `[]` | `null` |
| `SU-be21af7b7e0df6c4` | `hub` | `f973d9ca419e434a404a0804a997e48ada9c4025` | `backend/src/modules/apiV1/routes.ts` | `commit-f973d9ca419e` | `commit_surface` | `[CAP-007,CAP-005]` | `[]` | `[]` | `null` |
| `SU-890f3979c45ff346` | `hub` | `1dc2f6b61d954144e35f739e0923031a6d7d4fa1` | `docs/CONTINUIDADE.md` | `commit-1dc2f6b61d95` | `commit_surface` | `[]` | `[CAP-007,CAP-005]` | `[]` | `null` |
| `SU-b3d7590e075787b0` | `hub` | `fc73a262a7894c082f62f346af6ab6b159d5386a` | `backend/prisma/schema.prisma` | `commit-fc73a262a789` | `commit_surface` | `[CAP-016]` | `[]` | `[]` | `null` |
| `SU-4434239bacb7a213` | `hub` | `f7498759a4bbf894dead2738c0a330573ab9407a` | `backend/src/modules/webhooks/routes.ts` | `commit-f7498759a4bb` | `commit_surface` | `[CAP-016]` | `[]` | `[]` | `null` |
| `SU-50ddb4f4e1b06833` | `hub` | `6c6c79f2ba0a44093d84fee6cb0d0be0a32b9c8b` | `docs/CONTINUIDADE.md` | `commit-6c6c79f2ba0a` | `commit_surface` | `[]` | `[CAP-016]` | `[]` | `null` |
| `SU-57ac519eb7ecd71a` | `hub` | `ee64f842c421333219a6e41e6eccc2ee32261862` | `backend/prisma/schema.prisma` | `commit-ee64f842c421` | `commit_surface` | `[CAP-017]` | `[]` | `[]` | `null` |
| `SU-e9fb5b5cbc71ebd3` | `hub` | `e7579d51ac6b957d20e937e4a591da617a3a572b` | `backend/src/modules/groups/routes.ts` | `commit-e7579d51ac6b` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-2f9ba46c2106fd01` | `hub` | `68191aa1493f1c8eaec9395a8472626d2e912aba` | `backend/src/evolution-client/groups.ts` | `commit-68191aa1493f` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-30ec213271042819` | `hub` | `212dd8b3ac747f0ae198cf30fbdd7c17c2ebadae` | `backend/prisma/schema.prisma` | `commit-212dd8b3ac74` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-4dda8d11f61ee14c` | `hub` | `b07969494db55b2e165f692623ac96dc203de6d7` | `backend/prisma/schema.prisma` | `commit-b07969494db5` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-e9e23f883f8a6620` | `hub` | `587c9e19caf5dae46327151b905d859f9123d6aa` | `frontend/src/pages/Grupos.tsx` | `commit-587c9e19caf5` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-5f0aa719348127df` | `hub` | `2b2d499b666c14581b1238d63a81c1c238b2b591` | `frontend/src/pages/Grupos.tsx` | `commit-2b2d499b666c` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-055093f855fa95bf` | `hub` | `06f24f8b73c4cccb4396975d050c6eed19fd6383` | `backend/prisma/schema.prisma` | `commit-06f24f8b73c4` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-8aef21ecd0aa46e7` | `hub` | `61176730e4e03d0442426a8d3ce830411beaa3f9` | `backend/src/modules/groups/autoImport.ts` | `commit-61176730e4e0` | `commit_surface` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-49f13427528296bb` | `hub` | `fa56ecf649be46bf74a4029705992c0bcc896bbf` | `backend/src/modules/apiV1/routes.ts` | `commit-fa56ecf649be` | `commit_surface` | `[CAP-023,CAP-003]` | `[]` | `[]` | `null` |
| `SU-e509186cff261b61` | `official` | `6517f197c97d0b5bcad886d26eb0d28a813b47ca` | `README.md` | `modelos` | `documentation_behavior` | `[CAP-001]` | `[]` | `[]` | `null` |
| `SU-0847bd72ba78b201` | `official` | `6517f197c97d0b5bcad886d26eb0d28a813b47ca` | `public/index.html` | `view-disparos` | `ui_flow` | `[CAP-003]` | `[]` | `[]` | `null` |
| `SU-9c9ac219d3906bd8` | `official` | `6517f197c97d0b5bcad886d26eb0d28a813b47ca` | `public/index.html` | `view-atendimento` | `ui_flow` | `[CAP-006]` | `[]` | `[]` | `null` |
| `SU-d468a8f5a12df2f6` | `official` | `6517f197c97d0b5bcad886d26eb0d28a813b47ca` | `public/index.html` | `consulta-exportacao` | `ui_flow` | `[CAP-011]` | `[]` | `[]` | `null` |
| `SU-8394dc947ef9b1b4` | `hub` | `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2` | `backend/src/modules/apiV1/routes.ts` | `apiV1Router` | `code_symbol` | `[CAP-005]` | `[]` | `[]` | `null` |
| `SU-82896911a7b8dace` | `hub` | `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2` | `backend/src/modules/inbox/routes.ts` | `inboxRouter` | `code_symbol` | `[CAP-006]` | `[]` | `[]` | `null` |
| `SU-53138ff00f9ad334` | `hub` | `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2` | `backend/src/modules/groups/routes.ts` | `groupsRouter` | `code_symbol` | `[CAP-021]` | `[]` | `[]` | `null` |
| `SU-58bcfeefc97828c5` | `hub` | `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2` | `backend/prisma/schema.prisma` | `ScheduledMessage` | `migration_contract` | `[CAP-003]` | `[]` | `[]` | `null` |
| `SU-4b78629f9cae4e5e` | `legacy_overlay` | `994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2` | `hub-whatsapp/docker-compose.yml` | `commit-994e1e8ccb2a` | `commit_surface` | `[]` | `[]` | `[]` | `outside_st02: infrastructure composition is prohibited as product inspiration` |

## 8. Auditoria bidirecional

### 8.1 Catálogo → fontes

- Foram revisados 100% dos itens `not_found_after_protocol`, `partial`, cross-origin, `discard` e com implicação sensível.
- As 27 linhas têm ao menos uma evidência Central e uma evidência LeadsHug ou protocolo `NF-*` resolvível.
- Estados positivos foram confrontados com schema + serviço/controller + UI quando aplicável; presença apenas estrutural foi classificada `partial`, não `observed_present`.
- Amostra estratificada reproduzida (`23/27`): `CAP-001..CAP-018`, `CAP-020..CAP-024`. `CAP-019`, `CAP-025..CAP-027` ficaram fora da seleção hash, mas entraram na revisão integral de risco/estado acima.

### 8.2 Fontes → catálogo

- Todos os 196 commits da população resolvem para capacidade, suporte, duplicata ou exclusão.
- Os cinco commits fora das allowlists são exclusões fail-closed, sem inspeção de paths.
- O overlay `994e1e8` foi lido somente pelo path allowlisted `hub-whatsapp/docker-compose.yml` e excluído: composição de infraestrutura não é inspiração de produto neste TODO.
- Commits de documentação/continuidade que comprovam a mesma capacidade usam `support`; branding, renomeações cosméticas, correções puramente documentais e artefatos gerados usam exclusão justificada.
- Verificação automática resolveu `199/199` paths inspecionáveis no commit/snapshot correspondente; as cinco sentinelas foram validadas pela ausência em qualquer pathspec admitido.

### 8.3 Amostra determinística

A seleção usa `origin × epoch × implementation_state` no catálogo e `origin × source_unit_type × mapping-kind` no ledger. Estratos com até cinco itens foram revisados integralmente; nos demais, foram revisados os cinco primeiros IDs ordenados mais os IDs cujo primeiro byte do SHA-256 textual é divisível por quatro. A amostra não encontrou referência quebrada, unidade relevante sem destino ou exclusão injustificada.

- Amostra ledger: `83/204` unidades.
- IDs ordenados: `SU-00f28a695ed8f660, SU-0280861125081068, SU-02d6eb4b6b91a256, SU-055093f855fa95bf, SU-0695274bcf8e9482, SU-06b1f42b7594519c, SU-073673c3162bbd6d, SU-0847bd72ba78b201, SU-08e874019d53273e, SU-09c3c517726bac94, SU-0b0ce5d224e77d7d, SU-0b769e14a86f6489, SU-0c7c4dac50619774, SU-0ce1ef6402fa9047, SU-0efdb4210134a3ec, SU-123f0b3565594428, SU-135f8885a289831e, SU-13abc4fdd31748d9, SU-15280bf571fe4c85, SU-158cfff697bf3098, SU-15db0a83a690f5e5, SU-17122e7d703eaea2, SU-1769a43c0f6c3a9b, SU-1bbb215d42831a0d, SU-1c125a5d62b006ad, SU-1e1ec02439769f76, SU-21c269073451f229, SU-243d253de28ff1d9, SU-2639da94c5bbf5c4, SU-2f0f263820ac65fa, SU-354488d6a7419444, SU-3e1e28859889275d, SU-3eada8e805d436dc, SU-3f376aa95b8b1597, SU-4245afd93581d8f5, SU-42a947e477aa8674, SU-4434239bacb7a213, SU-49f13427528296bb, SU-49f137b6a62cb115, SU-4b78629f9cae4e5e, SU-50ddb4f4e1b06833, SU-53138ff00f9ad334, SU-531ea3e65199d9c8, SU-5389ecda5a346dc4, SU-55b64da66a69dd82, SU-58bcfeefc97828c5, SU-5d2c9d636fad7c69, SU-610cb66cc08e34fb, SU-6abb8ad01e981633, SU-774fb923110b7e66, SU-7c4a382deaf90802, SU-7e9b91cd76a3b2a0, SU-80df5c7d8fe52b6f, SU-82786d138e1ff9aa, SU-82896911a7b8dace, SU-8394dc947ef9b1b4, SU-8471e91484555b06, SU-87411772f6813892, SU-88751f90705da2c0, SU-890f3979c45ff346, SU-8a6d956710a52007, SU-8ac1ab487925046b, SU-8beea33eb313edd4, SU-8e9e465f1c60c669, SU-9001fed5c80495a4, SU-9c9ac219d3906bd8, SU-a43695d00991db25, SU-a45c2f7305104342, SU-adaaa59b2c836523, SU-b68646866f7273e6, SU-c2d893fa034649f9, SU-c766819a019f0595, SU-cd62a1a76ffb878a, SU-ce02209d98e03cde, SU-cf32d3208e836a70, SU-d468a8f5a12df2f6, SU-dce310684560c1cc, SU-dd50eb91b87e3def, SU-dd52f27834547a20, SU-e509186cff261b61, SU-e63cb98cd711c991, SU-eef1fe9b583e458e, SU-fba7631e55d429b8`.
- SHA-256 da lista acima separada por newline: `acb1de389730eb2fcb4b31615a9cc766364f2e4032aaf87738be03e7e553ae63`.

## 9. Lições negativas e exclusões

- Não reintroduzir dependência ou autenticação circular entre “oficial” e “hub”; o LeadsHug já é o produto unificado.
- Não copiar o papel `VIEWER`: a necessidade de consulta deve respeitar o modelo canônico de escopo/papéis, e não recriar um segundo eixo de capacidades.
- Não descartar mensagens por heurística de texto/tempo para “resposta automática”; o próprio Central desativou o filtro após falsos positivos.
- Não transportar topologia Cloudflare/Evolution/Postgres, schemas, workers ou segredos. Somente comportamento e lições entram no catálogo.
- Não confundir grupo/comunidade com conversa 1:1 nem aplicar política oficial ao transporte não oficial.
- Não usar métricas de produtividade sem definição semântica, contexto de volume e trilha auditável.

## 10. Conclusão para ST-04

Este estudo não prioriza. Para a futura comparação do ST-04, os candidatos ficam agrupados em cinco frentes, sem ordem aprovada:

1. templates e campanhas oficiais (`CAP-001..004`);
2. robustez do atendimento (`CAP-007..013`, `CAP-016`, `CAP-025`);
3. CRM e analytics (`CAP-012`, `CAP-015`);
4. onboarding/automação/ajuda (`CAP-017`, `CAP-019`, `CAP-020`, `CAP-026`);
5. grupos e campanhas não oficiais (`CAP-021..023`).

Qualquer implementação futura exige contrato próprio. O estudo de canais/formas de atendimento continua pertencendo ao ST-03.
