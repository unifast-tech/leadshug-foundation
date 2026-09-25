# LeadsHug — estudo conceitual de canais e atendimento do whatsflow_v2

**Status:** evidência de referência, não canônica e sem autoridade de implementação.
**Escopo:** ST-03; leitura sanitizada do snapshot congelado em 2026-09-25.
**Separação obrigatória:** `legacy_observation` descreve somente o legado; `leadshug_constraint` reproduz contrato já canônico; `recommendation` é uma hipótese de desenho para ST-04; `future_decision` requer novo TODO e aprovação.

## Manifesto reprodutível e protocolo de evidência

| Item | Resultado |
| --- | --- |
| Referência | `/mnt/c/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2` (somente leitura) |
| Baseline | objeto local verificado `3a36436c83ebefc6839380eb8fac1a6f13f4700a` (a etiqueta local `origin/stage` coincide neste checkout) |
| Tree | `6befe605dda039a7066a7fd48403807ea93f8408` |
| Landmark | `origin/main@cfe0aa120503687943ee81930172994a1ea9ab1a`, tree `d739d0a517651a4ed1621940c62e7a3107ee29ef`; `stage` está 59 commits à frente |
| Verificação | `status --short --branch`: `stage...origin/stage`, sem paths; `HEAD=3a36436…`; `rev-parse 3a36436^{tree}=6befe605…` |
| Frescura remota | não confirmada: `git fetch --all --prune` não autenticou. Este estudo depende apenas dos objetos locais imutáveis verificados, não afirma que o remoto permanece nessa ponta. |
| Superfícies admitidas | componentes/hooks de inbox e chat, funções serverless de webhook/automação, migrations SQL de conversa/SLA, testes correlatos e documentação de contexto do próprio snapshot. Nada de `.env`, dumps, valores de segredo, payloads ou dados de clientes. |

Uma referência abaixo usa a forma `whatsflow_v2@3a36436:path:símbolo/linhas`. Ela é reproduzível com `git show 3a36436:path`; linhas são do blob congelado. Força `direct` significa que o artefato contém o contrato/ação; `corroborated` requer uma segunda superfície; `conflicting` identifica contratos incompatíveis; `inferred` nunca é promovido a caminho operacional.

### Alcance, supersessão e call paths

| Afirmação / caminho | Evidência e natureza | Resolução |
| --- | --- | --- |
| Listagem de inbox e filtros | `src/components/whatsapp/WhatsAppLayout.tsx:34-57,131-187` chama `useConversations`, aplica filtro de canal em memória e expõe `assignConversation`/`resolveConversation`; `src/components/mensageria/inbox/InboxTab.tsx:9-96` seleciona abas. `direct`, `effective_runtime` para o caminho de UI, mas não prova transação de banco. | `partial`: é call path executável de interface; autorização/atomicidade são não demonstradas por ele. Schema efetivo: `not_applicable` para a mera seleção de aba. |
| Atribuição e resolução | `WhatsAppLayout.tsx:175-187` encaminha ações ao hook; `src/components/whatsapp/panels/ChatPanel.tsx:32-35,110-111` restringe envio por `assignedTo` e mostra ação de transferir. `corroborated`, `effective_runtime`. | `partial`: há fluxo de UI, mas nenhuma prova admitida de compare-and-set, winner/loser ou log append-only. |
| Transferência | `ChatPanel.tsx:272-278` declara estado de transferência para atendente ou `department`; a mesma superfície contém o handler de transferência. `direct`, `effective_runtime` de UI. | `partial`: origem/destino e razão aparecem na interface, mas a persistência/auditoria efetiva não foi estabelecida; não equivaler `department` a Setor LeadsHug. |
| Conversa materializada | `20260501320000` criou a projeção tenant-keyed, mas foi supersedida por `20260806005000` account-keyed; o teste CSP-04D corrobora a substituição estática. | `partial`: persistence-backed, schema final é E-17; nem migration nem teste provam execução em runtime. |
| SLA inicial | `supabase/migrations/20260422240000_sla_runtime_engine.sql:evaluate_conversation_sla` usa `conversations`/`chat_messages`. `direct`, `superseded`. | Não sustenta operação atual: a migration seguinte documenta que a RPC recebia chave incompatível e falhava. |
| SLA do painel WA | `supabase/migrations/20260423120000_sla_whatsapp_engine.sql:1-224:evaluate_whatsapp_conv_sla` substitui a chave por `instance_name,jid`, consulta `whatsapp_leads`/`whatsapp_messages` e resolve tenant da instância. `direct`, `effective_schema`; a nota de substituição é `corroborated`, `documentation`. | `partial`: o schema e a intenção do caminho são diretos; não houve execução de runtime. A função antiga permanece como anti-padrão histórico, não evidência concorrente de comportamento. |
| Departamento vinculado à instância | `supabase/migrations/20260625120000_whatsapp_instances_department.sql:1-10` adiciona `department_id`, pois o manager já lia/escrevia coluna antes ausente. `direct`, `effective_schema` + `historical`. | `conflicting/limitation`: o acoplamento foi introduzido para reparar divergência entre UI e schema; não prova modelo estável de roteamento. |
| Filtros de SLA | `src/components/whatsapp/left/InboxFilterDrawer.tsx:312-317` registra que opções antigas tinham itens mortos e mantém duas escolhas. `direct`, `effective_runtime`. | `limitation`: UI não representa todo o estado calculado pelo motor; não usar filtros como prova de lifecycle SLA. |
| Capacidade, presença, round-robin ou claim atômico | Inventário limitado de superfícies admitidas não resolve estes mecanismos. | `unknown after bounded inspection`; não inferir destes nomes, estados ou componentes estáticos. |

## Modelo conceitual proposto para discussão posterior

```text
Mantenedora 1 ── * Setor 1 ── * BU ── * Canal/Provider-adapter
                                 │ 1
                                 │
                                 * Conversa (BU, Contato) ── * Mensagem / Atividade append-oriented
                                 │ 0..1
                           ownership/atendimento
                                 │
                         0..* Unidade de atendimento ── * Equipe/associação ── * Usuário
                                 │
                               0..* Fila ── 1 Política de roteamento
```

O diagrama é uma linguagem de análise, não uma taxonomia nova: **BU** continua o número e a fronteira mínima de permissão/histórico; **Canal** continua transporte; **Setor** continua agrupamento de BUs. “Unidade de atendimento”, “equipe”, “fila” e “política” são candidatos deliberadamente neutros, sem assumir que um `department` legado seja Setor.

| Termo | Legado observado | Constraint LeadsHug | Leitura conceitual / cardinalidade |
| --- | --- | --- | --- |
| conexão/provedor | instância, provider e UI de conexões aparecem em `ConnectionCard`/`WhatsAppConnectionsTab`; SLA resolve tenant por `whatsapp_instances`. | Provider é adapter e falha é determinística. | Uma BU pode ter `0..*` configurações de transporte ao longo do tempo; uma conversa não muda de identidade ao trocar transporte. |
| BU/número | legado usa `instance_name` como parte da chave de conversa. | BU é número, unidade mínima de atendimento, grants e histórico. | Uma BU tem `0..*` canais; um canal não cria outra organização de trabalho. |
| conversa | schema final observado usa `(account_id, instance_name, remote_jid)`; a projeção tenant-keyed é histórica/superseded e a UI mistura projeções/estados. | Única por `(BU, contato)`, independente de transporte. | Uma conversa tem `1..*` mensagens e `0..*` atividades; no máximo um ownership ativo. |
| department / setor | instância recebeu `department_id` depois que UI e schema divergiram. | Setor agrupa BUs, não é sinônimo aprovado de `department`. | Unidade/equipe de atendimento deve ser `0..*` por BU somente após decisão explícita. |
| agente/grant | UI carrega/seleciona atendentes; controle de envio considera `assignedTo`. | Papéis OWNER/ADMIN/ATENDENTE e grants materializados na BU. | Usuário pode ter `0..*` grants; membership de equipe não concede visibilidade fora da BU. |
| fila/política | abas de fila e atendimento existem, sem algoritmo operacional de distribuição comprovado. | Tenant/BU e autorização são sempre resolvidos. | Uma conversa pode entrar em `0..1` fila ativa; uma fila usa uma política, cuja seleção ainda é decisão futura. |

### Estados e transições de atendimento (modelo, não estado canônico)

`aberta/entrada -> pendente-em-fila -> em-atendimento -> resolvida`; nova entrada pode produzir `reaberta`; `transferindo` é uma transição, não um segundo owner. Pausas de SLA são relógios, não permissões. Estados `unknown`/`conflicting` do legado não devem ser convertidos em estados LeadsHug.

Transições exigidas para decisão futura: entrada idempotente cria/localiza conversa por `(BU, contato)`; claim compare-and-set escolhe exatamente um owner; transferência revoga/reserva ownership de forma atômica; resolver libera capacidade e escreve atividade; reabertura não apaga proveniência. Falha de provider só altera disponibilidade/erro do adapter, nunca a identidade da conversa ou a autorização.

## Matriz única de cobertura C-01..C-12

### Registro de referências congeladas e inventário limitado

As linhas da matriz citam este registro como `E-xx`; cada entrada é uma referência exata ao snapshot `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a`, não uma referência ao checkout vivo.

| ID | Referência congelada exata | Alcance |
| --- | --- | --- |
| E-01 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/WhatsAppLayout.tsx:WhatsAppLayout:34-57,131-187` | inbox, filtro de canal, encaminhamento de assign/resolve |
| E-02 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260423120000_sla_whatsapp_engine.sql:evaluate_whatsapp_conv_sla:1-224` | motor SLA WA e chave instância/JID |
| E-03 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260501320000_conversations_populate_trigger.sql:upsert_conversation_from_message:15-87` | histórico/superseded: projeção tenant-keyed substituída por E-17; não sustenta schema final |
| E-04 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260625120000_whatsapp_instances_department.sql:1-10` | vínculo tardio instância–department |
| E-05 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/agents/DepartmentManager.tsx:DepartmentManager` é superfície declarativa; `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/agents/AgentSectorAssignment.tsx:AgentSectorAssignment:1-209` é `orphaned` após busca congelada sem importador externo (somente self-reference). Nenhuma prova autorização efetiva. |
| E-06a | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/panels/ChatPanel.tsx:ChatPanel/canSend:104-111,877-884` | gate de envio na UI por `assignedTo`; não é autorização server-side |
| E-06b | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/panels/ChatPanel.tsx:openTransfer:329-360` | carrega candidatos e departments para o diálogo de transferência |
| E-06c | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/panels/ChatPanel.tsx:doTransfer:362-411` | atualização estática para atendente e inserção posterior de mensagem de sistema |
| E-06d | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/panels/ChatPanel.tsx:doTransferToSector:413-460` | atualização estática para department/fila e inserção posterior de mensagem de sistema |
| E-07 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260422240000_sla_runtime_engine.sql:evaluate_conversation_sla:1-196` | motor SLA anterior, classificado superseded pela E-02 |
| E-08 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/left/InboxFilterDrawer.tsx:SLA_CHOICES:312-317` | redução de estados de SLA na UI |
| E-09 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/inbox/InboxTab.tsx:InboxTab:9-96` | abas declaradas de atendimento/fila |
| E-10 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/panels/ChatPanel.tsx:ConversationNote:82-88` | forma de nota exibida; não prova evento de claim/transferência |
| E-11 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/hooks/whatsapp/useConversations.ts:buildContext:93-160,352-362` | caminho de presença de **provider**: lê `whatsapp_instances.status`, marca instâncias não `connected/open` e projeta `deviceDisconnected`; é distinto de presença/capacidade de atendente |
| E-12 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/inbox/ChatArea.tsx:ChatArea/handleSend:88-124` | fallback local “sent” quando não há instância e `catch` vazio que também marca “sent”; superfície estática, não prova caminho atual do painel principal |
| E-13 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/hooks/whatsapp/useConversations.ts:assignConversation:631-720` | upsert estático de `assigned_attendant_id` e mensagem posterior; sem predicado CAS/winner-loser no blob |
| E-14 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/pages/MensageriaPage.tsx:MensageriaPage/renderContent:63-107` | monta `AgentDashboard` e `DepartmentManager` por aba; prova caminho de UI, não algoritmo de distribuição |
| E-15 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/agents/AgentDashboard.tsx:AgentDashboard:65-130,172-199` | lê/polling `agent_status`, deriva contagens ativas de `whatsapp_leads`, e faz upsert do status próprio; leitura/configuração direta, sem prova de TTL/freshness/reserva |
| E-16 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/agents/DepartmentManager.tsx:DIST_LABELS/saveMutation:32-35,87-103,211-219` | configura/guarda `round_robin`, `least_busy` ou `manual`; valor declarativo, sem consumer/scheduler demonstrado |
| E-17 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260806005000_csp04d_conversations_account_projection.sql:upsert_conversation_from_message:3-96` | schema final observado: remove índice tenant-keyed, cria unicidade `(account_id,instance_name,remote_jid)` e trigger account-scoped |
| E-18 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/__tests__/csp04d_typebot_account_authority_contract.test.ts:CSP-04D:121-150` | teste estático corrobora presença do account projection; não é execução de banco/runtime |
| E-19 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/functions/meta-webhook/index.ts:handleWhatsAppWebhook:110-150,222-312` | ingress Meta no happy path resolve integração/conta, escreve mensagem/lead e faz fan-out; falha parcial pode continuar e exceção responde HTTP 200 para suprimir retry do provider. Recuperação interna e durabilidade permanecem unknown/limitation. |
| E-20 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/functions/uazapi-webhook/index.ts:Deno.serve:352-650,1340-1355` | ingress Uazapi no happy path resolve instância/conta e persiste; catch absorve exceções e responde HTTP 200 para suprimir retry do provider. Recuperação interna e durabilidade permanecem unknown/limitation. |
| E-21 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/functions/automation-router/index.ts:resolveAutomationRequestScope/Deno.serve/actions/handoff:68-200,229-360,446-508,734-845,1262-1369` | router resolve escopo canônico de conta, seleciona automação e contém caminhos estáticos de assign/transfer/handoff/spread; não prova CAS de atendimento nem execução transacional |
| E-22 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/hooks/useSectorAccess.ts:useSectorAccess/filterBySector:44-114` | fail-open legado de UI: zero departments → view-all, `department_id` nulo visível e atribuição direta visível; filtro de UI, não grant LeadsHug nem autorização server-side |
| E-23 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/hooks/whatsapp/useConversations.ts:resolveConversation:724-772` | resolve faz `update whatsapp_leads` e, após sucesso, `insert whatsapp_messages` sequencial sem tratar seu erro; mesmo quando o update falha, o estado UI é marcado `resolved` após o branch. Não há transação, CAS ou predicate explícito de account no update. |
| E-24 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/panels/ChatPanel.tsx:ChatPanel:1-12,740-752`; `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/sla/SlaBadge.tsx:SlaBadge:1-50`; `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/hooks/useConversationSla.ts:useConversationSla:42-80` | caminho atual da conversa selecionada: `ChatPanel -> SlaBadge -> useConversationSla -> evaluate_whatsapp_conv_sla`; RPC/fonte ainda é estática, sem execução runtime comprovada |
| E-25 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/hooks/whatsapp/useConversations.ts:useConversations:300-338` | cálculo local de breach para listagem, com `slaMap`, `updated_at` e `first_response_minutes`; não é a RPC da conversa selecionada |
| E-26 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/panels/LeftPanel.tsx:LeftPanel/SLA-filter:1-18,184-235,298-317` | caminho atual de listagem/filtros; usa `slaBreach` calculado localmente e documenta a retirada do RPC por item, sem substituir a avaliação RPC da conversa selecionada |
| E-27 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/left/NewConversationDialog.tsx:NewConversationDialog:347-376` | auto-atribuição estática ao usuário atual por upsert de `whatsapp_leads`; sem CAS, reserva ou autorização server-side demonstrada |
| E-28a | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/functions/uazapi-webhook/index.ts:Deno.serve:1021-1082` | reabertura/assignment de lead em upsert sequencial; sem prova de transação, CAS ou predicate account completo |
| E-28b | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/functions/uazapi-webhook/index.ts:Deno.serve:1090-1127` | bloco de métricas/`claimed_at` é `orphaned/unreachable` no caminho: a flag é `false` na linha 34 e a linha 1099 faz `continue`; não sustenta comportamento runtime |
| E-30 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260804151000_csp04c_whatsapp_runtime_account_rls.sql:3-62` | `effective_schema` estático para backfill e RLS account-scoped de `whatsapp_messages`/`whatsapp_leads`; não prova runtime, grants ou autorização por operação |
| E-31 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260805233000_csp04d_account_authority_followup.sql:9-22,204-247,467-545,547-553,615-632,674-700` | `effective_schema` estático: account_id, índices/triggers/RLS para departments, agent_departments e agent_status; runtime, grants e auth de operação continuam desconhecidos |
| E-29 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/functions/automation-router/index.ts:handleSpreadBlock:1344-1363` | spread escolhe aleatoriamente candidato e faz upsert de atribuição; não demonstra modo `least_busy`, scheduler, reserva, CAS ou execução runtime |
| E-NF-01 | Inventário de busca **limitado**: `git -C '<snapshot>' grep -n -I -E -e 'round.?robin' -e 'least_busy' -e 'distribution_mode' -e 'agent_status' -e 'assigned_attendant_id' -e 'max_conversations' -e 'current_conversations' -e 'last_activity_at' -e 'heartbeat' -e 'last_seen' -e 'claim' -e 'scheduler' -e 'ttl' -e 'fresh' 3a36436c83ebefc6839380eb8fac1a6f13f4700a -- 'src/hooks/whatsapp/useConversations.ts' 'src/components/whatsapp/panels/ChatPanel.tsx' 'src/components/mensageria/agents/AgentDashboard.tsx' 'src/components/mensageria/agents/DepartmentManager.tsx' 'supabase/functions/uazapi-webhook/index.ts' 'supabase/functions/automation-router/index.ts'`; exclui deliberadamente corpus bruto/documental como `docs/memorandos/**`, `docs/**` não nomeados e `_user_prompts_raw.json`. | Inventário observa status/configuração/atribuições nos E-13/E-15/E-16/E-27/E-28a/E-29. Consumer/scheduler, CAS, reserva/capacidade e freshness de atendente ficam `unknown after bounded inspection`; provider-presence não é parte desta incógnita. |

| ID / conceito | Superfícies; natureza/força/estado | Constraint LeadsHug; relações/estados; cenário | Disposição; recomendação / future_decision; conclusão |
| --- | --- | --- | --- |
| C-01 conexão/provedor | [E-01], [E-02], [E-11], [E-12], [E-19], [E-20], [E-30]; `direct/corroborated`, `partial`. E-11 prova presença de **provider**, não presença/capacidade de atendente. | adapter ≠ workflow; BU `0..*` canais no estado operacional atual (ausência de canal também é possível); mínimo `1..*` para BU atendível é `future_decision`. Simular provider indisponível e troca mantendo conversa. | `limitation`: derivar tenant de instância conflita com account context; E-02 usa instance/JID sem predicate account explícito. E-12 é fallback/catch silencioso. Nada disso é padrão de autorização/runtime. |
| C-02 BU/número e canal | [E-17], [E-18], [E-19], [E-20]; `direct/corroborated`, `effective_schema/test`, `partial`. E-03 é superseded. | BU é número; canal é transporte; cardinalidade operacional `BU 0..* Canal`; requisito de BU atendível `1..*` canal é `future_decision`. Mesma BU troca provider sem nova conversa. | `limitation`: chave legado é account/instância/JID. `recommendation`: manter chave canônica BU/contato. |
| C-03 entrada/identidade/continuidade | [E-17], [E-18], [E-19], [E-20]; `corroborated`, `effective_schema/test`, `partial`. | conversa única BU/contato; webhook idempotente. Duplicata/reordenação não duplica mensagem/efeito nem regride estado. | `limitation`: E-19/E-20 admitem falha parcial e suprimem retry do provider com HTTP 200; recuperação interna/durabilidade são unknown. `anti_pattern`: tomar chave account/instância/JID por identidade universal. `future_decision`: dedupe/reorder. |
| C-04 unidade/equipe | [E-04], [E-05], [E-22], [E-31]; `direct`, `partial`. Claim UI/membership não requer schema; E-31 resolve schema/RLS account-scoped estático de departments/agent_departments, não runtime ou autorização de operação. | não reutilizar Setor; unidade/equipe especializa atendimento e só se relaciona a BUs explicitamente. **Positivo:** membership da unidade *e* grant da BU satisfazem condições necessárias de elegibilidade, nunca são suficientes para atender; resultado/papel é `future_decision`. **Negativo:** membership isolado ou `department_id` legado coincidente não satisfaz grant. | `anti_pattern`: `department` legado = Setor. E-22 é fail-open de UI, não auth server-side. `future_decision`: entidade/ownership da unidade. |
| C-05 associação/cobertura | [E-06a], [E-06b], [E-22], [E-31]; `direct`, `partial`. Gate/diálogo UI são `not_applicable` a schema; E-31 é schema/RLS account-scoped estático de `agent_departments`, sem provar grant BU ou auth por operação. | `leadshug_constraint`: grants na BU; leitura independente. `legacy_observation`: filtro/membership UI não prova grant. | `limitation`: E-22 permite view-all sem departments, `department_id` nulo e atribuição direta no filtro UI; não demonstra grant. |
| C-06 fila/elegibilidade | [E-01], [E-09], [E-19], [E-20], [E-28a], [E-22], [E-30]; `direct`, `partial`. Abas/filtros UI são `not_applicable`; E-30 resolve schema/RLS account-scoped estático de leads, não elegibilidade autorizada. | `leadshug_constraint`: fila scoped tenant/BU e fila livre não concede acesso. Webhook pode abrir/pendenciar lead; filtro UI não é eligibilidade autorizada. | `unknown after bounded inspection`: predicado de elegibilidade/grant não demonstrado. |
| C-07 roteamento | [E-14], [E-16], [E-19], [E-20], [E-21], [E-29], [E-31], [E-NF-01]; `direct/declarative_only`, `partial`. UI/configuração é `not_applicable`; E-31 resolve schema/RLS estático do `departments`, mas não consumer/scheduler; router/webhook writes são `partial`. | `leadshug_constraint`: provider não escolhe agente. Cenário: modo/status nunca concede grant BU nem prova execução do algoritmo, freshness ou capacidade reservada. | `limitation`: configuração/fan-out/spread aleatório ≠ distribuição autorizada. `unknown after bounded inspection`: scheduler, critérios e fallback. |
| C-08 claim/atribuição/presença/capacidade | [E-01], [E-06a], [E-13], [E-15], [E-19], [E-20], [E-22], [E-27], [E-28a], [E-29], [E-30], [E-31], [E-NF-01]; `partial`. UI/status são `not_applicable`; E-30/E-31 resolvem schema/RLS estático account-scoped, não CAS, reserva, TTL/freshness, grant ou runtime. | `leadshug_constraint`: único owner e grants BU. Cenário: status/contagem/configuração nunca concede BU nem prova freshness/capacidade; dois claims exigem winner/loser. | `unknown after bounded inspection`: scheduler/CAS/reserva/capacidade/freshness; UI/polling/upsert não é mutex. |
| C-09 transferência/handoff | [E-06b], [E-06c], [E-06d], [E-19], [E-20], [E-21], [E-28a], [E-29], [E-30]; `declarative_only`, `partial`. Diálogo UI é `not_applicable`; E-30 resolve schema/RLS estático de leads, mas auth/transação de handoff permanecem desconhecidas. | `leadshug_constraint`: origem/destino autorizados e uma posse. | `limitation`: updates/notes sequenciais não são transação/CAS. |
| C-10 lifecycle | [E-01], [E-02], [E-07], [E-09], [E-23], [E-28a], [E-28b], [E-30]; `conflicting`, `partial`. E-23 pode divergir UI/persistência; E-28a observa reopen; E-28b é orphaned; E-30 é schema/RLS estático. E-07 é superseded. | aberto, pendente, em atendimento, resolvido, reaberto; ownership explícito. Entrada após resolve reabre sem apagar histórico. | `anti_pattern`: UI↔persistence divergence e fundir status de UI/SLA/ownership. `future_decision`: transições autorizadas. |
| C-11 SLA/escalonamento | [E-02], [E-07], [E-08], [E-24], [E-25], [E-26]; `direct`, `partial`. E-24 é RPC do item selecionado; E-25 é cálculo local da listagem; E-26 é caminho atual de painel/lista; E-07 é superseded. | clock/custo bounded; pausas definidas; alert/breach auditáveis. Sem regra, pausa e breach não criam acesso. | `limitation`: fonte atual selecionada e cálculo de lista divergem; não há prova runtime/freshness. `future_decision`: calendário, escalonamento e avaliação incremental. |
| C-12 auditoria/histórico | [E-06c], [E-06d], [E-10], [E-13], [E-23], [E-28a], [E-30]; `direct`, `partial`; writes/inserts posteriores são persistência estática/sequencial, não prova de log append-only atômico/em runtime, nem predicate account completo. | append-oriented, tenant/BU scoped, leitura independente. Cross-tenant/cross-BU e write-sem-read são negativos obrigatórios. | `unknown after bounded inspection`: evento operacional completo. `recommendation`: eventos imutáveis por transição. |

### Aplicabilidade de schema e matriz ator × operação

`not_applicable` vale somente para uma alegação sem persistência (por exemplo: aba/diálogo/gate de UI, status exibido, configuração declarativa). Onde a mesma linha contém write ou leitura persistente, schema aplicável é `effective_schema` estático em E-17/E-30/E-31 (ou `partial/unknown` se não houver DDL/RLS congelado). Assim C-04..C-09/C-12 não recebem `not_applicable` global: a interface não prova schema; cada write é avaliado separadamente. Mesmo `effective_schema` não prova runtime, grant, autorização de operação, atomicidade ou freshness.

| Ator / operação | Constraint canônica LeadsHug | Exercício requerido, sem resultado por papel presumido | Limite negativo canônico | Evidência legado |
| --- | --- | --- | --- | --- |
| OWNER/ADMIN/ATENDENTE × view | tenant/account e grants BU; leitura é independente | testar cada papel; mapeamento papel→view é `future_decision/unknown` | cross-tenant/cross-BU/null-scope não satisfaz a constraint | E-22 é filtro UI fail-open, não prova grant/ACL |
| OWNER/ADMIN/ATENDENTE × claim | grant BU e ownership único | testar cada papel; mapeamento papel→claim e winner/loser são `future_decision/unknown` | sem escopo/grant não satisfaz a constraint; corrida exige CAS futuro | E-13/E-27/E-29 são upserts estáticos; CAS é `unknown after bounded inspection` |
| OWNER/ADMIN/ATENDENTE × assign | tenant/account, grant BU e regra de operação explícita | testar cada papel; nenhum allow/deny por papel é inferido | tenant/account/grant/null-scope devem ser avaliados separadamente | E-06c/E-19/E-28a observam write, não autorização |
| OWNER/ADMIN/ATENDENTE × transfer | origem/destino e BU autorizados | testar cada papel; mapeamento é `future_decision/unknown` | origem/destino cross-BU, cross-tenant ou null-scope não satisfazem constraint | E-06c/d/E-21 são sequenciais, não matriz de auth |
| OWNER/ADMIN/ATENDENTE × resolve | tenant/account, grant BU e regra explícita | testar cada papel; mapeamento papel→resolve é `future_decision/unknown` | cross-BU/cross-tenant/null-scope não satisfazem constraint | E-23 faz update+mensagem sequenciais, sem transaction/CAS/account predicate explícito |
| OWNER/ADMIN/ATENDENTE × configure | tenant/account, grant BU e regra explícita | testar cada papel; mapeamento papel→configure é `future_decision/unknown` | escopo inválido/nulo não satisfaz constraint; sem afirmar deny para um papel | E-16 é configuração declarativa, não auth |

## Walkthrough 1:1 dos invariantes já canônicos

| Invariante | Walkthrough positivo | Negativo / resultado do estudo |
| --- | --- | --- |
| conversa BU/contato, independente de transporte | mesma BU/contato troca adapter e localiza a mesma conversa | chave legado instância/JID é limitação; não adotá-la como identidade LeadsHug. |
| webhook idempotente | duplicata/reordenação preserva uma mensagem/efeito lógico | trigger de projeção não prova dedupe do webhook; decisão futura deve defini-lo. |
| saída respeita janela/capability | envio fora da janela ou sem capability falha determinísticamente | UI/legado não é prova de capability; não usar fallback silencioso. |
| provider é adapter | falha/troca não altera fila, identidade ou assignment | modelo legado mistura instância em chaves; risco registrado. |
| segredos excluídos | artefato só contém caminhos/símbolos | revisão sanitizada não contém valores/payloads. |
| falha determinística | indisponibilidade devolve erro explícito | nenhuma observação autoriza entrega local silenciosa. |
| um tenant por operação | view/claim/configure resolve tenant antes de operar | cross-tenant é negativo obrigatório; tenant da instância legado não substitui account context LeadsHug. |
| grants na BU | membership da unidade e grant BU são condições necessárias de elegibilidade | associação de equipe não satisfaz grant nem, junto do grant, autoriza operação por si só. |
| OWNER/ADMIN/ATENDENTE | a matriz ator × operação acima separa view, claim, assign, transfer, resolve e configure | papéis legado não são mapeados; os cenários são constraints LeadsHug, não prova de enforcement no legado. |
| histórico append-oriented | claim/transfer/handoff/resolve produzem eventos | UI não provou eventos completos: requisito futuro, não fato legado. |
| histórico tenant/BU scoped | consultas filtram ambas fronteiras | projeções de mensagens do legado não autorizam omissão de BU. |
| leitura independente da escrita | operador e leitor são avaliados separadamente | `canSend` de UI não prova leitura; manter checks distintos. |

## Rubrica de concorrência e desempenho documental

| Risco | Invariante/resultado requerido | Evidência/disposição |
| --- | --- | --- |
| dois claims | CAS por versão/owner vazio; um winner e loser determinístico | C-08 `anti_pattern`: UI não é mutex; `recommendation` server-side. |
| capacidade | reserva por unidade explicitada; compensação e liberação em transfer/resolve/disconnect | E-15 mostra apenas contagens/polling; `limitation`: não prova capacidade reservada nem limite aplicável. |
| claim × transfer/resolve | precedência ou CAS; ownership nunca perdido | C-09 `recommendation`; ausência de prova de transação é limitação. |
| automação × humano | handoff idempotente, uma posse e mensagem sem duplicata | E-21/E-29 observam fan-out/spread estáticos; C-09 permanece `unknown`, sem precedência/atomicidade demonstrada. |
| presença obsoleta | TTL/heartbeat, fallback explícito; ausência ≠ grant/capacidade infinita | E-15 registra polling e status, mas não TTL/freshness; status nunca concede grant BU. |
| filas/listas/contagens | paginação/bounds e agregação server-side; evitar scan client ilimitado | E-15 deriva contagens por polling; E-16 configura modos mas não prova scheduler. `WhatsAppLayout` ainda filtra canais em memória: `limitation`, não padrão escalável. |
| SLA | relógio e fonte de verdade únicos; avaliação bounded/escalonamento explícito | E-24 é a RPC atual da conversa selecionada; E-25 é cálculo local de listagem e E-26 é caminho de painel atual. Não inferir equivalência, freshness ou custo runtime. |
| realtime/polling | dedupe, backpressure e escopo tenant/BU | migration do SLA registra loop de socket histórico: `anti_pattern` superseded; não é saúde atual. |

## Padrões, limitações, anti-padrões e incógnitas

| Classe | Evidência | Uso permitido |
| --- | --- | --- |
| pattern | trigger de projeção de conversa e retorno SLA explícito | inspirar projeções e estados explícitos, após contrato próprio. |
| limitation | legacy UI, schema e lifecycle não são uma única fonte; filtros SLA reduzem estados; E-22 é fail-open de UI (zero departments → view-all; `department_id` nulo visível; atribuição direta visível). | não tratar filtro UI como autorização server-side ou especificação. |
| anti_pattern | migration de SLA documenta RPC antiga com chave incompatível/loop; E-22 permite visibilidade fail-open na UI. | proibir inferência por artefato estático, UI fail-open e migração cega de vocabulário. |
| unknown | consumer/scheduler dos modos RR/menor carga, claim atômico, TTL/freshness de presença do atendente, capacidade reservada, evento completo de transferência e read ACL independente. | permanecer `unknown after bounded inspection`; status de atendente e configuração dos modos são observados em E-15/E-16, mas não resolvem essas lacunas. |

## Recomendações sem priorização

1. `recommendation`: ST-04 pode comparar um núcleo de conversa `(BU, contato)` com adapters de transporte, mantendo Setor/BU/Canal intactos. **Dependências:** decisão de identidade externa e dedupe. **Risco:** migrar a chave instância/JID como verdade do domínio.
2. `recommendation`: separar membership de unidade/equipe de grants de BU e de permissão de leitura histórica. **Dependências:** matriz de papéis/operações. **Risco:** vazamento por associação implícita.
3. `recommendation`: definir assignment/transfer como operações atômicas com eventos append-only e capacidade reservável. **Dependências:** máquina de estados e semântica de winner/loser. **Risco:** dupla atribuição/perda de ownership.
4. `recommendation`: manter SLA como serviço de relógio com fonte de verdade, pausas e custo bounded, não como filtro de UI. **Dependências:** calendário e estratégia de escalonamento. **Risco:** loops, varredura e estado divergente.

As seguintes são somente `future_decision`: significados e cardinalidades de unidade/equipe/fila; política de distribuição; capacidade/presença; transições e precedência; mapping de identidade de provider; calendário/SLA; modelo de eventos e leitura. Nenhuma recebe prioridade, status Accepted, alteração de módulo ou autorização de implementação por este artefato.

## Sanitização e limites

Foram retidos somente caminhos, símbolos, nomes de tabelas/funções e comportamento resumido. Não há segredo, token, PII, payload real, dump, patch ou cópia extensa de código legado. A evidência é estática e documental; não afirma saúde de produção nem executa runtime do legado.
