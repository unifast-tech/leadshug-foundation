# LeadsHug atendimento com histórico completo transferência anexos e estados

**Version:** 1.0
**Data:** 2026-10-14
**Estado:** decomposição da frente de atendimento escolhida pelo usuário. A execução de ST-ATT-01 foi aprovada no [TODO de histórico](../../todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md); os demais recortes aguardam contratos e aprovação próprios.

## Artifact Role

Este brief organiza quatro entregas de atendimento para transformar as capacidades úteis do Central-Whatsapp em contratos do LeadsHug. É evidência de planejamento; backlog, módulos e TODOs continuam sendo os donos de disposição, contratos e execução.

## Source Idea / Request

O usuário escolheu “Atendimento: transferência, histórico completo, anexos e estados das mensagens” ao definir a primeira frente de incorporação das capacidades do Central-Whatsapp. A escolha autoriza o enquadramento dessa frente; não registra aprovação de um contrato de implementação ainda não apresentado.

## Problem / Desired Outcome

- **Problem:** a thread operacional lê as primeiras 200 mensagens; o usuário não alcança mensagens posteriores em conversas longas. Atribuição tem leitura e escrita separadas, transferência não tem contrato próprio, mensagens não têm mídia ponta a ponta e eventos de entrega/leitura não são projetados na inbox.
- **Desired outcome:** atender uma conversa com acesso ao histórico completo, responsabilidade identificável, transferência auditável, anexos acessíveis e andamento de cada mensagem compreensível.
- **Why now:** o núcleo já tem conversa por BU/contato, grants, mensagens, integração de canais e auditoria; o catálogo ST-02 e o estudo ST-03 oferecem evidência para definir essas extensões.

## Constraints / Non-Goals

- Mantenedora e grants da BU delimitam cada operação, consulta e evento.
- Transferência de responsabilidade preserva BU, contato e identidade da conversa. Setor continua sendo agrupamento de BUs. Equipes, filas especializadas e transferência entre equipes dependem de decisão própria.
- Meta e Evolution permanecem adapters. Diferenças de capability devem aparecer nos contratos e na interface.
- Observações do legado serão redesenhadas e testadas no LeadsHug, conforme a política de referência independente.
- CRM, campanhas, templates, distribuição automática, SLA, liderança, importação de histórico do dispositivo e automação Typebot ficam fora deste pacote.
- Cada entrega terá TODO, evidência e closeout próprios. A ST-04 geral continua no backlog e não recebe status de concluída por este recorte.

## Canonical Touchpoints

- **Constitution impact:** a proposta preserva os invariantes atuais; qualquer nova regra sistêmica exige decisão e consolidação antes de implementação.
- **Roadmap impact:** o recorte se relaciona ao núcleo unificado e ao endurecimento operacional; a ordem abaixo é proposta deste pacote, sem datas ou avanço dos exit gates.
- **Primary module:** [Inbox and Conversations](../../modules/inbox-and-conversations.md).
- **Secondary modules:** [Identity and Tenancy](../../modules/identity-and-tenancy.md), [Integrations and Channels](../../modules/integrations-and-channels.md), [Audit and History](../../modules/audit-and-history.md).
- **Candidate record:** `BLG-leadshug-attendance-evolution`, no [backlog](../../backlog/README.md).

## Evidence / References

- [Catálogo ST-02](../analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md): CAP-010 histórico incremental, CAP-013 ownership/transferência, CAP-016 estados e CAP-007 mídia.
- [Estudo ST-03](../analysis/leadshug-whatsflow-channel-attendance-conceptual-model-20260925.md): separação de BU, transporte, equipe e autorização; concorrência e proveniência.
- [Política Central-Whatsapp](../../policies/central_whatsapp_independent_legacy_policy.md).
- [Serviço de conversas](../../../api-app/src/domain/inbox/conversations.service.ts): `thread`, `assumir`, `responder`.
- [Recebimento](../../../api-app/src/domain/inbox/incoming.service.ts): persistência sem deduplicação por identificador externo.
- [Schema](../../../api-app/prisma/schema.prisma): Conversation, Message, MessageStatus, mediaRef e ActivityLog.
- [Inbox](../../../web-app/src/telas/Inbox.tsx): abertura, atualização por socket e resposta carregam a thread novamente.
- [Playwright](../../../web-app/playwright.config.ts): caminho antigo `../api`, a ajustar antes de validar qualquer entrega web.

## Ambiguities To Resolve Before TODO

| ID | Ambiguity | Why It Matters | Current Evidence | Handling |
| --- | --- | --- | --- | --- |
| AMB-ATT-01 | Quem pode transferir e para quais destinatários? | Define autorização e comportamento com owner interno/externo. | Papéis/grants existem; transferência ainda não tem regra canônica. | Propor responsável atual e ADMIN/OWNER da BU para destinatários ativos com grant na mesma BU; resolver no TODO de transferência. |
| AMB-ATT-02 | O histórico completo inclui quais superfícies? | BFF, consulta e API pública têm respostas e efeitos diferentes. | Thread BFF tem teto 200; consulta já pagina; API pública tem contrato próprio. | Primeiro recorte proposto: inbox BFF; manter os outros contratos e testar regressões. |
| AMB-ATT-03 | Escopo de mídia por canal, formatos, limites e retenção. | Define storage, custo, segurança, capabilities e prova externa. | Tipos/mediaRef existem, mas adapters/UI não completam o fluxo. | Resolver no TODO de mídia, sem supor suporte idêntico dos provedores. |
| AMB-ATT-04 | Como ordenar estados e representar falha após envio aceito? | Evento duplicado ou atrasado não pode regredir entrega/leitura nem induzir retry duplicado. | MessageStatus existe; parser Meta processa mensagens e não `statuses`. | Definir máquina de estados, identidade de evento, auditoria e retries no TODO de status. |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-ATT-01 | Ler as mensagens recentes e acessar todo o histórico da inbox. | inbox-and-conversations | audit-and-history, identity-and-tenancy | Página inicial recente, cursor determinístico, carregar anteriores, mesclar atualização sem perder histórico e rejeitar acesso/cursor alheio. | PostgreSQL com mais de 200 mensagens, timestamps empatados e Playwright com navegação, resposta e troca rápida de conversa. | create-now: [TODO de histórico](../../todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md) | Validação isolada/harness corretos; API115/224,Web20/36,FRC3 e reviews aceitos. | Local-Implemented em2026-10-15; commits locais na feature/inbox-timeline-pagination. |
| ST-ATT-02 | Transferir responsabilidade com exclusividade e trilha auditável. | inbox-and-conversations | identity-and-tenancy, audit-and-history | Operação atômica, grants de origem/destino, um vencedor em corrida, eventos com ator e responsável anterior/novo. | E2E de disputa claim/transfer/close, negações por BU/tenant e fluxo web de transferência/readback. | defer | Resolver AMB-ATT-01 e definir contrato de ownership; validar concorrência existente dentro desse recorte. | Avaliar uso do ActivityLog antes de criar outra tabela de auditoria. |
| ST-ATT-03 | Ver o andamento real de envio entrega leitura e falha. | integrations-and-channels | inbox-and-conversations, audit-and-history | Correlação scoped entre evento/mensagem, idempotência, precedência dos estados, timestamps e falhas explícitas. | Webhooks sintéticos assinados, duplicatas, reordenação, falha tardia e UI; prova externa separada por canal admitido. | defer | Resolver AMB-ATT-04; contrato de identidade/deduplicação e adapters. | Reutilizar MessageStatus quando adequado; não inferir equivalência entre provedores. |
| ST-ATT-04 | Receber visualizar e enviar anexos no atendimento. | inbox-and-conversations | integrations-and-channels, audit-and-history | Storage privado e scoped, formatos/limites definidos, download autenticado, envio/recebimento e erros por capability. | E2E de upload/download e isolamento, browser com anexos e troca externa em cada canal admitido. | defer | Resolver AMB-ATT-03; usar correlação/status do ST-ATT-03 para auditar resultado de entrega. | Arquivo de marca/avatar existente não prova o contrato de mídia de mensagens. |

## Estruturas propostas por entrega

1. **Histórico:** estender o contrato da thread com metadados de paginação e cursor; ordenar por `createdAt` e `id`; manter uma coleção de mensagens por conversa na UI. Avaliar o índice composto na consulta real antes de acrescentar migração.
2. **Responsabilidade:** definir atualização condicional do owner e eventos atômicos; avaliar histórico de ciclos de atendimento somente se necessário ao contrato. Uma nova tabela não é pré-condição presumida.
3. **Estados:** correlacionar identificador externo dentro da BU/canal, definir transições/timestamps e registro de falhas. Persistência e retries dependem das decisões desse recorte.
4. **Mídia:** definir referência de arquivo da mensagem, metadados, storage privado e adapters de upload/download/envio; limites e retenção serão explícitos.

## Retire This Brief When

Os recortes tiverem disposição no backlog/TODOs, contratos consolidados nos módulos e nenhuma decisão viva depender deste brief. A ordem e os campos propostos não concedem autoridade de execução por si só.

## Execução ST-ATT-01 em2026-10-15

Histórico da inbox entregue Local-Implemented, com contrato e decisões Verified local no módulo owner, fontes commitadas e provas/reviews no [pacote de entrega](../reviews/leadshug-inbox-timeline-20261014/README.md). As evidências de teto200/path../api acima descrevem a baseline do estudo em2026-10-14. ST-ATT-02/03/04 preservam as decisões/contratos e aprovações próprias.
