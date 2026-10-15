# LeadsHug — conexões confiáveis e histórico dos canais

**Data:** 2026-10-15
**Perfil:** Strategic / CTO-Tech-Lead; escopos NestJS, React, PostgreSQL, Prisma e Docker. Projeto existente: Genesis não se aplica.
**Origem do formato:** `delphi-ai/templates/feature_brief_template.md`.

## Artifact Role

- **Why this brief exists now:** conectar, provar operação externa e importar histórico são objetivos relacionados com fronteiras e capacidades diferentes. Precisam de entregas verificáveis antes de retomar transferência de atendimento.
- **What this brief is not:** contrato canônico de módulo, aprovação de implementação ou prova de funcionamento externo. Disposição e próximo gate pertencem ao backlog; execução pertence a cada TODO.

## Source Idea / Request

Em 2026-10-15 o usuário concordou em priorizar confiabilidade de conexão, preparo dos testes e histórico antes de transferência: “Concordo até para poder realizar os testes corretamente e ficar mais fácil”. Confirmou também: “Posso disponibilizar oficial e não oficial”. Isso confirma disponibilidade potencial de números de teste; acesso, configuração e saúde não foram verificados. Em seguida definiu: “Podemos fazer nos dois ambientes mas inicialmente local”. O primeiro ciclo usa backend local; Railway será uma etapa posterior. Correção posterior do usuário: o objetivo imediato é reproduzir **os processos de cadastro dos números oficiais e não oficiais**. A interpretação inicial centrada em diagnóstico foi revista antes de aprovação.

## Problem / Desired Outcome

- **Problem:** oficial recebe CONECTADO após consulta de números da WABA; não oficial depende de eventos de conexão sem reconciliação ativa; não existe importador de histórico do aparelho. A paginação concluída consulta somente mensagens já persistidas.
- **Desired outcome:** cadastrar e conectar o número numa jornada guiada: oficial pela autorização Meta e não oficial por QR; confirmar identidade/resultado e facilitar os testes. Histórico será importado em recortes posteriores.
- **Why now:** os dois canais serão disponibilizados para teste e o fluxo é pré-requisito prático da validação das próximas entregas de atendimento.

## Constraints / Non-Goals

- Preservar Mantenedora, grants, BU/número e conversa por BU/contato; um canal continua sendo transporte.
- Não reaproveitar dados, instâncias, credenciais, configuração ou runtime do Central-Whatsapp.
- Nunca equiparar conexão de navegador com backend à conexão entre WhatsApp e provedor.
- Cloud API oficial e Evolution/Baileys têm contratos independentes. Não prometer histórico completo do aparelho para o oficial sem confirmar modalidade, elegibilidade e contrato documentado.
- Histórico importado não é mensagem nova: não pode acionar bot, aumentar não lidas, reabrir atendimento ou conceder janela de resposta por data de ingestão.
- Não incluir transferência, anexos binários, templates, campanhas, CRM, Typebot novo, troca automática de provedor ou deploy de produção.
- Alterações de schema exigem migração; observações por canal/instância devem impedir que resposta antiga reative vínculo removido ou substituído.

## Canonical Touchpoints

- **Constitution impact:** nenhuma alteração proposta; preservar invariantes atuais.
- **Roadmap impact:** suporte ao núcleo unificado e endurecimento operacional; sem mudança de horizonte ou alegação de exit gate atendido.
- **Primary module candidates:** [Integrations and Channels](../../modules/integrations-and-channels.md).
- **Secondary module candidates:** [Inbox and Conversations](../../modules/inbox-and-conversations.md), [Identity and Tenancy](../../modules/identity-and-tenancy.md), [Audit and History](../../modules/audit-and-history.md).
- **Candidate record:** `BLG-leadshug-channel-readiness-and-history`, no [backlog](../../backlog/README.md).

## Evidence / References

[Leitura específica das jornadas de cadastro e proposta](../analysis/leadshug-number-registration-reference-flows-20261015.md): botão Conectar pela Meta e cadastro manual administrativo no oficial; apelido e QR no Hub; experiência alternativa Uazapi no WhatsFlow.

Leitura de código em API `ae6a9662c29b77276351aa9de653a47276372246`, Web `4e56f6c1f4515b918d05b8c87e890d42e8542c56`; nenhuma mudança de produto neste enquadramento.

| Constatação atual | Evidência local | Limite da inferência |
| --- | --- | --- |
| Oficial consulta WABA, escolhe primeiro número e grava CONECTADO | `api-app/src/domain/channels/channels.service.ts:31-74` | Não prova registro, assinatura de webhook, credencial válida depois da consulta ou troca real. Seleção explícita de número deve entrar no contrato. |
| Evolution cria instância com QR e assina MESSAGES_UPSERT/CONNECTION_UPDATE | `api-app/src/integrations/evolution/evolution.client.ts:35-68` | Há método de connectionState sem consumidor de domínio; versão externa não fixada na topologia lida. |
| Parser não oficial trata somente upsert e conexão | `api-app/src/surfaces/webhooks/evolution.controller.ts:40-49` | Sem MESSAGES_SET/importador. Compatibilidade de payload deve ser provada na versão admitida. |
| Entrada grava mensagem sem data externa nem dedupe | `api-app/src/domain/inbox/incoming.service.ts:41-87`; `api-app/prisma/schema.prisma:310-334` | Reusar este fluxo diretamente para importação produziria efeitos de entrada nova. |
| Tela atualiza dados salvos a cada cinco segundos | `web-app/src/telas/Numeros.tsx:12-19` | Poll de banco não é prova de saúde do provedor. |
| Testes de canais substituem clientes externos | `api-app/test/helpers.ts:75-79` | Testes locais são válidos para contrato interno, não certificam aparelho/Meta/Evolution reais. |
| CAP-022 registra a lacuna de importação | [Catálogo ST-02](../analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md) | Referência comportamental; não autoriza copiar importador legado. |

Fontes primárias consultadas em 2026-10-15:

- [Documentação Evolution: webhooks](https://raw.githubusercontent.com/evolution-foundation/docs-evolution/main/v2/en/configuration/webhooks.mdx): distingue eventos de carga inicial e mensagem nova. A documentação deve ser confrontada com a versão instalada, não tratada como prova dessa instalação.
- [Evolution: enum de eventos](https://github.com/evolution-foundation/evolution-api/blob/main/src/api/types/wa.types.ts) e [schema de criação](https://github.com/evolution-foundation/evolution-api/blob/main/src/validate/instance.schema.ts): referências para verificar adapter/eventos/settings da versão escolhida. Não fixam a versão implantada.
- Documentação oficial Meta sobre onboarding de usuários do Business App: acesso retornou HTTP429 nesta sessão; modalidade e suporte de histórico permanecem **não verificados**. Não se assume suporte ou impossibilidade. Registrar retry e verificação antes do contrato correspondente.

## Ambiguities To Resolve Before TODO

| ID | Ambiguity | Why It Matters | Current Evidence | Handling |
| --- | --- | --- | --- | --- |
| AMB-CON-01 | Versão e preparo da Evolution própria no ambiente local confirmado | Endpoints, payloads, persistência e retomada variam. | Usuário escolheu local primeiro e Railway depois; Compose local não declara Evolution nem repassa variáveis dos webhooks. | Seleção de ambiente resolvida; fixar versão e wiring/callback antes do freeze. Inventário legado não define a versão do LeadsHug. |
| AMB-CON-02 | WABA/phone_number_id e modalidade do oficial | Evitar conectar número errado ou presumir sincronização do Business App. | Fluxo atual usa WABA manual e primeiro número; usuário disponibiliza oficial. | Confirmar WABA existente e modalidade; seleção explícita e confirmação de identidade são candidatas do ST-CON-01. |
| AMB-CON-03 | Destinos autorizados, acesso e callback público dos testes | Um número disponível não prova permissão técnica ou webhook alcançável. | Disponibilidade dos dois canais confirmada; nenhuma credencial acessada ou mensagem enviada. | Readiness separado e checklist por canal; enviar apenas a interlocutor de teste definido. |
| AMB-CON-04 | Volume, período e conteúdo disponíveis para importar | Provedor pode oferecer subconjunto; não prometer integralidade. | Não há importador; Evolution tem eventos e APIs que dependem da versão/configuração. | ST-CON-02 define limites, ordenação, checkpoint e resultado parcial visível após ST-CON-01. |
| AMB-CON-05 | Histórico oficial via modalidade admitida | Pode exigir onboarding e eventos ausentes do produto. | Doc Meta rate-limited; nenhuma prova de eligibility/coexistence. | ST-CON-03 depende de fonte oficial e verificação de conta; não inferir equivalência com QR. |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-CON-01 | Cadastrar e conectar números oficiais e não oficiais com jornada guiada | integrations-and-channels | identity-and-tenancy, audit-and-history | Autorização Meta/Embedded Signup no oficial e apelido/QR no não oficial; runtime local próprio e callback verificável; número correto; verificação explícita com erro/frescor; webhook e consulta reconciliados sem estado antigo reativar vínculo; QR/repareamento; checklist de operação real separado de estado técnico. | Testes de erro/race/tenant com PostgreSQL, Playwright de conexão/verificação e troca real IN/OUT para cada canal disponível. | create-now: [TODO draft](../../todos/active/features/TODO-leadshug-channel-connection-readiness.md) | Resolver AMB-CON-01/02 e target/destinatário de teste antes do freeze. | Primeira entrega proposta; sem alegar importação ou validação externa antecipada. |
| ST-CON-02 | Importar o histórico disponibilizado pela Evolution com retomada segura | integrations-and-channels | inbox-and-conversations, identity-and-tenancy, audit-and-history | Escopo por BU/canal; idempotência concorrente, timestamps externos, direções, backlog/realtime sem lacunas, lotes/checkpoint/progresso e falhas; nenhum efeito de entrada nova. | Replay e duplicatas concorrentes, interrupção/retomada, datas empatadas e antigas, timeline completa; amostra de aparelho confrontada com provedor e banco. | defer | ST-CON-01; versão/forma de histórico, retenção, limites e regra para mensagens sem ID. | Não resolve mídia binária ou status de entrega; não importar lote cego por IncomingService.registrar. |
| ST-CON-03 | Disponibilizar histórico oficial conforme capacidade comprovada da conta | integrations-and-channels | inbox-and-conversations, identity-and-tenancy | Matriz de elegibilidade/onboarding/consentimento; importação somente quando suportada; estado explícito quando indisponível. | Contrato oficial vigente, conta elegível e lote real; integridade/idempotência equivalentes ao importador. | split-further | ST-CON-01, leitura oficial Meta acessível e modalidade confirmada. | Coexistência/histórico não são presumidos; Embedded Signup de cadastro pertence ao ST-CON-01 após correção do usuário e não prova suporte a histórico. |

## Retire This Brief When

Todos os recortes tiverem contratos próprios e disposição no backlog; decisões estáveis forem consolidadas pelos módulos responsáveis. Nenhuma execução pode depender somente deste brief.
