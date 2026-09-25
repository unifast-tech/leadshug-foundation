# LeadsHug — estudo conceitual de canais e atendimento do whatsflow_v2

**Status:** evidência de referência, não canônica e sem autoridade de implementação.
**Escopo:** ST-03; leitura sanitizada do snapshot congelado em 2026-09-25.
**Separação obrigatória:** `legacy_observation` descreve somente o legado; `leadshug_constraint` reproduz contrato já canônico; `recommendation` é uma hipótese de desenho para ST-04; `future_decision` requer novo TODO e aprovação.

## Manifesto reprodutível e protocolo de evidência

| Item | Resultado |
| --- | --- |
| Referência | `/mnt/c/Unifast/LeadsHug/Inspirações LeadsHug/whatsflow_v2` (somente leitura) |
| Baseline | `origin/stage@3a36436c83ebefc6839380eb8fac1a6f13f4700a` |
| Tree | `6befe605dda039a7066a7fd48403807ea93f8408` |
| Landmark | `origin/main@cfe0aa120503687943ee81930172994a1ea9ab1a`, tree `d739d0a517651a4ed1621940c62e7a3107ee29ef`; `stage` está 59 commits à frente |
| Verificação | `status --short --branch`: `stage...origin/stage`, sem paths; `HEAD` e `origin/stage` coincidem |
| Fetch | tentou `git fetch --all --prune`; indisponível por ausência de credencial interativa. Os refs locais acima já existiam e foram comparados; nenhum ref, checkout ou arquivo foi alterado. |
| Superfícies admitidas | componentes/hook de inbox e chat, migrations SQL de conversa/SLA, testes correlatos e documentação de contexto do próprio snapshot. Nada de `.env`, dumps, valores de segredo, payloads ou dados de clientes. |

Uma referência abaixo usa a forma `whatsflow_v2@3a36436:path:símbolo/linhas`. Ela é reproduzível com `git show 3a36436:path`; linhas são do blob congelado. Força `direct` significa que o artefato contém o contrato/ação; `corroborated` requer uma segunda superfície; `conflicting` identifica contratos incompatíveis; `inferred` nunca é promovido a caminho operacional.

### Alcance, supersessão e call paths

| Afirmação / caminho | Evidência e natureza | Resolução |
| --- | --- | --- |
| Listagem de inbox e filtros | `src/components/whatsapp/WhatsAppLayout.tsx:34-57,131-187` chama `useConversations`, aplica filtro de canal em memória e expõe `assignConversation`/`resolveConversation`; `src/components/mensageria/inbox/InboxTab.tsx:9-96` seleciona abas. `direct`, `effective_runtime` para o caminho de UI, mas não prova transação de banco. | `partial`: é call path executável de interface; autorização/atomicidade são não demonstradas por ele. Schema efetivo: `not_applicable` para a mera seleção de aba. |
| Atribuição e resolução | `WhatsAppLayout.tsx:175-187` encaminha ações ao hook; `src/components/whatsapp/panels/ChatPanel.tsx:32-35,110-111` restringe envio por `assignedTo` e mostra ação de transferir. `corroborated`, `effective_runtime`. | `partial`: há fluxo de UI, mas nenhuma prova admitida de compare-and-set, winner/loser ou log append-only. |
| Transferência | `ChatPanel.tsx:272-278` declara estado de transferência para atendente ou `department`; a mesma superfície contém o handler de transferência. `direct`, `effective_runtime` de UI. | `partial`: origem/destino e razão aparecem na interface, mas a persistência/auditoria efetiva não foi estabelecida; não equivaler `department` a Setor LeadsHug. |
| Conversa materializada | `supabase/migrations/20260501320000_conversations_populate_trigger.sql:15-87` cria unicidade `(tenant_id,instance_name,remote_jid)` e trigger de upsert de `whatsapp_messages`. `direct`, `effective_schema`. | `partial`: persistence-backed, schema resolvido; a migration declara que o front ainda fazia montagem dinâmica, logo não prova que a projeção era o único caminho efetivo. |
| SLA inicial | `supabase/migrations/20260422240000_sla_runtime_engine.sql:evaluate_conversation_sla` usa `conversations`/`chat_messages`. `direct`, `superseded`. | Não sustenta operação atual: a migration seguinte documenta que a RPC recebia chave incompatível e falhava. |
| SLA do painel WA | `supabase/migrations/20260423120000_sla_whatsapp_engine.sql:1-224:evaluate_whatsapp_conv_sla` substitui a chave por `instance_name,jid`, consulta `whatsapp_leads`/`whatsapp_messages` e resolve tenant da instância. `direct`, `effective_schema`; a nota de substituição é `corroborated`, `documentation`. | `partial`: o schema e a intenção do caminho são diretos; não houve execução de runtime. A função antiga permanece como anti-padrão histórico, não evidência concorrente de comportamento. |
| Departamento vinculado à instância | `supabase/migrations/20260625120000_whatsapp_instances_department.sql:1-11` adiciona `department_id`, pois o manager já lia/escrevia coluna antes ausente. `direct`, `effective_schema` + `historical`. | `conflicting/limitation`: o acoplamento foi introduzido para reparar divergência entre UI e schema; não prova modelo estável de roteamento. |
| Filtros de SLA | `src/components/whatsapp/left/InboxFilterDrawer.tsx:312-317` registra que opções antigas tinham itens mortos e mantém duas escolhas. `direct`, `effective_runtime`. | `limitation`: UI não representa todo o estado calculado pelo motor; não usar filtros como prova de lifecycle SLA. |
| Capacidade, presença, round-robin ou claim atômico | Busca admitida em código, migrations/schema e docs de contexto não encontrou call path atual que os prove. | `not_found_after_protocol`; não inferir destes nomes, estados ou componentes estáticos. |

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
| conversa | schema legado usa `(tenant, instance, jid)`; UI mistura projeções/estados. | Única por `(BU, contato)`, independente de transporte. | Uma conversa tem `1..*` mensagens e `0..*` atividades; no máximo um ownership ativo. |
| department / setor | instância recebeu `department_id` depois que UI e schema divergiram. | Setor agrupa BUs, não é sinônimo aprovado de `department`. | Unidade/equipe de atendimento deve ser `0..*` por BU somente após decisão explícita. |
| agente/grant | UI carrega/seleciona atendentes; controle de envio considera `assignedTo`. | Papéis OWNER/ADMIN/ATENDENTE e grants materializados na BU. | Usuário pode ter `0..*` grants; membership de equipe não concede visibilidade fora da BU. |
| fila/política | abas de fila e atendimento existem, sem algoritmo operacional de distribuição comprovado. | Tenant/BU e autorização são sempre resolvidos. | Uma conversa pode entrar em `0..1` fila ativa; uma fila usa uma política, cuja seleção ainda é decisão futura. |

### Estados e transições de atendimento (modelo, não estado canônico)

`aberta/entrada -> pendente-em-fila -> em-atendimento -> resolvida`; nova entrada pode produzir `reaberta`; `transferindo` é uma transição, não um segundo owner. Pausas de SLA são relógios, não permissões. Estados `unknown`/`conflicting` do legado não devem ser convertidos em estados LeadsHug.

Transições exigidas para decisão futura: entrada idempotente cria/localiza conversa por `(BU, contato)`; claim compare-and-set escolhe exatamente um owner; transferência revoga/reserva ownership de forma atômica; resolver libera capacidade e escreve atividade; reabertura não apaga proveniência. Falha de provider só altera disponibilidade/erro do adapter, nunca a identidade da conversa ou a autorização.

## Matriz única de cobertura C-01..C-12

### Registro de referências congeladas e protocolo de ausência

As linhas da matriz citam este registro como `E-xx`; cada entrada é uma referência exata ao snapshot `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a`, não uma referência ao checkout vivo.

| ID | Referência congelada exata | Alcance |
| --- | --- | --- |
| E-01 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/whatsapp/WhatsAppLayout.tsx:WhatsAppLayout:34-57,131-187` | inbox, filtro de canal, encaminhamento de assign/resolve |
| E-02 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260423120000_sla_whatsapp_engine.sql:evaluate_whatsapp_conv_sla:1-224` | motor SLA WA e chave instância/JID |
| E-03 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260501320000_conversations_populate_trigger.sql:upsert_conversation_from_message:15-87` | projeção/upsert de conversa e unicidade legado |
| E-04 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:supabase/migrations/20260625120000_whatsapp_instances_department.sql:1-11` | vínculo tardio instância–department |
| E-05 | `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/agents/DepartmentManager.tsx:DepartmentManager` e `whatsflow_v2@3a36436c83ebefc6839380eb8fac1a6f13f4700a:src/components/mensageria/agents/AgentSectorAssignment.tsx:AgentSectorAssignment` | superfícies declarativas de gestão/associação; não provam autorização efetiva |
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
| E-NF-01 | Protocolo reproduzível, allowlist sanitizada: `git -C '<snapshot>' grep -n -I -E 'round.?robin|least_busy|least.?load|distribution_mode|agent_status|assigned_attendant_id|capacity|attendant.?presence|claim|scheduler' 3a36436c83ebefc6839380eb8fac1a6f13f4700a -- 'src/hooks/whatsapp/useConversations.ts' 'src/components/whatsapp/WhatsAppLayout.tsx' 'src/components/whatsapp/panels/ChatPanel.tsx' 'src/components/mensageria/inbox/InboxTab.tsx' 'src/pages/MensageriaPage.tsx' 'src/components/mensageria/agents/AgentDashboard.tsx' 'src/components/mensageria/agents/DepartmentManager.tsx' ':(glob)supabase/migrations/*.sql' '.context/05_database_schema.md' '.context/15_known_issues_and_debt.md'`; revisão manual dos resultados para call path, migrations/schema e os dois documentos admitidos. A allowlist exclui deliberadamente `docs/memorandos/**`, `docs/**` não nomeados e `_user_prompts_raw.json`. | E-15 prova polling/leitura de status e contagens atuais; E-16 prova configuração de modo. Nenhum resultado revisado estabelece **consumer/scheduler** que execute o modo, claim atômico, reserva/capacidade ou TTL/freshness de presença de atendente. Status/configuração não concedem grant de BU. Presença de provider não faz parte desta ausência: ela é observada em E-11. |

| ID / conceito | Superfícies; natureza/força/estado | Constraint LeadsHug; relações/estados; cenário | Disposição; recomendação / future_decision; conclusão |
| --- | --- | --- | --- |
| C-01 conexão/provedor | [E-01], [E-02], [E-11], [E-12]; `direct/corroborated`, `effective_runtime/effective_schema`, `partial`. E-11 prova presença de **provider** por status de instância, não presença/capacidade de atendente. | adapter ≠ workflow; BU `1..*` canal; disponibilidade/falha/troca. Simular provider indisponível e troca mantendo conversa. | `pattern`: adapter e tenant derivado da instância. `limitation/anti_pattern`: E-12 marca envio como localmente “sent” sem instância e em `catch` vazio; não aceitar fallback silencioso. `recommendation`: isolar identidade externa e erro determinístico de adapter. `future_decision`: lifecycle/capabilities do canal. Conclusão: nenhum provider deve possuir fila/assignment. |
| C-02 BU/número e canal | [E-03]; `direct`, `effective_schema`, `partial`. | BU é número; canal é transporte; BU `1..*` canais. Mesma BU troca provider sem nova conversa. | `limitation`: chave legado é instância/JID. `recommendation`: manter chave canônica BU/contato. `future_decision`: mapeamento de identidades externas. |
| C-03 entrada/identidade/continuidade | [E-01], [E-03]; `corroborated`, `effective_schema/runtime`, `partial`. | conversa única BU/contato; webhook idempotente. Duplicata/reordenação não duplica mensagem/efeito nem regride estado. | `pattern`: upsert/projeção. `anti_pattern`: tomar `(instance,jid)` por identidade universal. `future_decision`: chave de dedupe e semântica de reorder. |
| C-04 unidade/equipe | [E-04], [E-05]; `direct`, `effective_runtime/schema`, `conflicting`. | não reutilizar Setor; unidade/equipe especializa atendimento e só se relaciona a BUs explicitamente. **Positivo:** agente com membership da unidade *e* grant da BU atende a BU vinculada. **Negativo:** membership isolado ou `department_id` legado coincidente não permite view/claim de uma BU sem grant. | `anti_pattern`: `department` legado = Setor. `recommendation`: nome neutro e vínculo explícito. `future_decision`: entidade/ownership da unidade. |
| C-05 associação/cobertura | [E-06a], [E-06b]; `direct`, `effective_runtime`, `partial`. | grants na BU; papéis fixos; view independente de write. Testar no-grant, cross-BU e null-scope negados. | `limitation`: seleção/gate de UI não demonstra grant. `recommendation`: membership separado de autorização. `future_decision`: matriz operação/papel/unidade. |
| C-06 fila/elegibilidade | [E-01], [E-09]; `direct`, `effective_runtime`, `partial`; sem consumer de distribuição. | fila scoped por tenant/BU; entrada/saída auditável; fila livre não concede acesso. | `unknown`: eligibilidade sem grant. `recommendation`: predicado server-side fail-closed. `future_decision`: fila livre e null-scope. |
| C-07 roteamento | [E-14], [E-16], [E-NF-01]; `direct`, `declarative_only`, `partial`. A página monta a configuração e E-16 persiste modo, mas não há consumer/scheduler que prove executar round-robin/least-busy/manual. | provider não define escolha; política recebe candidatos autorizados. **Cenário:** selecionar qualquer modo jamais concede grant de BU nem prova que algoritmo foi executado. | `limitation`: configuração ≠ distribuição. `recommendation`: estratégia explícita, server-side e testável. `future_decision`: critérios/pesos, scheduler e fallback. |
| C-08 claim/atribuição/presença/capacidade | [E-01], [E-06a], [E-13], [E-14], [E-15], [E-NF-01]; `corroborated`, `effective_runtime` para caminhos UI/polling e `declarative_only` para persistência/configuração estática; `partial`. E-15 mostra status/contagens atuais, não TTL/freshness nem capacidade reservada. | único owner; reserva/liberação; presença de atendente não implica acesso. **Cenário:** status ou contagem nunca concede grant BU; dois claims simultâneos exigem um winner e loser determinístico, não provados pelo legado. | `anti_pattern`: UI, polling ou upsert sem CAS como mutex/capacidade. `recommendation`: claim atômico no servidor. `future_decision`: unidade/TTL/freshness, limites de capacidade e presença de atendente. |
| C-09 transferência/handoff | [E-06b], [E-06c], [E-06d]; `direct`, `declarative_only` para updates e inserts estáticos; `partial`. As duas operações em sequência não provam transação atômica nem execução runtime observada. | origem/destino autorizados, atividade append-oriented, uma posse. Corrida claim×transfer×resolve e handoff automação×humano. | `limitation`: E-06c/E-06d mostram persistência pretendida, não atomicidade/auditoria efetiva. `recommendation`: CAS + evento imutável. `future_decision`: precedência e retorno à fila. |
| C-10 lifecycle | [E-01], [E-02], [E-07], [E-09]; `conflicting`, `effective_runtime/schema/superseded`. | aberto, pendente, em atendimento, resolvido, reaberto; ownership explícito. Entrada após resolve reabre sem apagar histórico. | `anti_pattern`: fundir status de UI/SLA/ownership. `recommendation`: máquina de estados separada. `future_decision`: transições autorizadas. |
| C-11 SLA/escalonamento | [E-02], [E-07], [E-08]; `direct`, `effective_schema`, `partial`. | clock/custo bounded; pausas definidas; alert/breach auditáveis. Sem regra, pausa e breach não criam acesso. | `pattern`: estados explícitos. `limitation`: regra de maior priority e wall-clock simplificados; filtros reduzem estados. `future_decision`: calendário, escalonamento e avaliação incremental. |
| C-12 auditoria/histórico | [E-03], [E-06c], [E-06d], [E-10], [E-13]; `direct`, `declarative_only`, `partial`; inserts de mensagens posteriores a updates são evidência estática, não prova de log append-only atômico/em runtime para claim/transferência. | append-oriented, tenant/BU scoped, leitura independente. Cross-tenant/cross-BU e write-sem-read são negativos obrigatórios. | `unknown`: evento operacional completo. `recommendation`: eventos imutáveis por transição. `future_decision`: retenção/projeções/permissão de leitura. |

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
| grants na BU | sem grant/cross-BU/null scope negados | associação de equipe não satisfaz grant. |
| OWNER/ADMIN/ATENDENTE | matriz futura separa view, claim, assign, transfer, resolve, configure | papéis legado não são mapeados. |
| histórico append-oriented | claim/transfer/handoff/resolve produzem eventos | UI não provou eventos completos: requisito futuro, não fato legado. |
| histórico tenant/BU scoped | consultas filtram ambas fronteiras | projeções de mensagens do legado não autorizam omissão de BU. |
| leitura independente da escrita | operador e leitor são avaliados separadamente | `canSend` de UI não prova leitura; manter checks distintos. |

## Rubrica de concorrência e desempenho documental

| Risco | Invariante/resultado requerido | Evidência/disposição |
| --- | --- | --- |
| dois claims | CAS por versão/owner vazio; um winner e loser determinístico | C-08 `anti_pattern`: UI não é mutex; `recommendation` server-side. |
| capacidade | reserva por unidade explicitada; compensação e liberação em transfer/resolve/disconnect | E-15 mostra apenas contagens/polling; `limitation`: não prova capacidade reservada nem limite aplicável. |
| claim × transfer/resolve | precedência ou CAS; ownership nunca perdido | C-09 `recommendation`; ausência de prova de transação é limitação. |
| automação × humano | handoff idempotente, uma posse e mensagem sem duplicata | C-09 `unknown`; decisão de precedência futura. |
| presença obsoleta | TTL/heartbeat, fallback explícito; ausência ≠ grant/capacidade infinita | E-15 registra polling e status, mas não TTL/freshness; status nunca concede grant BU. |
| filas/listas/contagens | paginação/bounds e agregação server-side; evitar scan client ilimitado | E-15 deriva contagens por polling; E-16 configura modos mas não prova scheduler. `WhatsAppLayout` ainda filtra canais em memória: `limitation`, não padrão escalável. |
| SLA | relógio e fonte de verdade únicos; avaliação bounded/escalonamento explícito | C-11: função por conversa e agregação em loop revelam risco de custo; não medir runtime. |
| realtime/polling | dedupe, backpressure e escopo tenant/BU | migration do SLA registra loop de socket histórico: `anti_pattern` superseded; não é saúde atual. |

## Padrões, limitações, anti-padrões e incógnitas

| Classe | Evidência | Uso permitido |
| --- | --- | --- |
| pattern | trigger de projeção de conversa e retorno SLA explícito | inspirar projeções e estados explícitos, após contrato próprio. |
| limitation | legacy UI, schema e lifecycle não são uma única fonte; filtros SLA reduzem estados. | usar como alerta de reconciliação, não como especificação. |
| anti_pattern | migration de SLA documenta RPC antiga com chave incompatível/loop; ligação UI/schema de `department_id` foi corrigida depois. | proibir inferência por artefato estático e migração cega de vocabulário. |
| unknown | RR, menor carga, claim atômico, presença, capacidade, evento completo de transferência e read ACL independente. | permanecer `unknown`/`not_found_after_protocol`; exige decisão/evidência futura. |

## Recomendações sem priorização

1. `recommendation`: ST-04 pode comparar um núcleo de conversa `(BU, contato)` com adapters de transporte, mantendo Setor/BU/Canal intactos. **Dependências:** decisão de identidade externa e dedupe. **Risco:** migrar a chave instância/JID como verdade do domínio.
2. `recommendation`: separar membership de unidade/equipe de grants de BU e de permissão de leitura histórica. **Dependências:** matriz de papéis/operações. **Risco:** vazamento por associação implícita.
3. `recommendation`: definir assignment/transfer como operações atômicas com eventos append-only e capacidade reservável. **Dependências:** máquina de estados e semântica de winner/loser. **Risco:** dupla atribuição/perda de ownership.
4. `recommendation`: manter SLA como serviço de relógio com fonte de verdade, pausas e custo bounded, não como filtro de UI. **Dependências:** calendário e estratégia de escalonamento. **Risco:** loops, varredura e estado divergente.

As seguintes são somente `future_decision`: significados e cardinalidades de unidade/equipe/fila; política de distribuição; capacidade/presença; transições e precedência; mapping de identidade de provider; calendário/SLA; modelo de eventos e leitura. Nenhuma recebe prioridade, status Accepted, alteração de módulo ou autorização de implementação por este artefato.

## Sanitização e limites

Foram retidos somente caminhos, símbolos, nomes de tabelas/funções e comportamento resumido. Não há segredo, token, PII, payload real, dump, patch ou cópia extensa de código legado. A evidência é estática e documental; não afirma saúde de produção nem executa runtime do legado.
