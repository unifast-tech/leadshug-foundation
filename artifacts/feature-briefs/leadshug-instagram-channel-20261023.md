# LeadsHug — Atendimento pelo Instagram

**Version:** 1.0. **Data:** 2026-10-23. **Perfil:** Strategic / CTO-Tech-Lead. Escopo de análise: NestJS, React, PostgreSQL e Prisma. Enquadramento baseado em `delphi-ai/templates/feature_brief_template.md` e `workflows/docker/feature-framing-method.md`.

## Artifact Role

- **Why this brief exists now:** o usuário pediu Instagram como próxima frente funcional, antes do histórico, para exercitar a abstração Channel com outro meio de conversação. Há decisões de identidade e autorização que precisam preceder o contrato de implementação.
- **What this brief is not:** contrato de execução, mudança vigente da definição de BU, capacidade entregue ou aprovação de runtime. A disposição do candidato pertence ao backlog; a sequência pertence ao roadmap; contratos e invariantes pertencem aos módulos e à constituição.

## Source Idea / Request

Pedido do usuário em2026-10-23: colocar a integração Instagram primeiro na fila, para testar o conceito de canais e disponibilizar outra opção de conversação. Referência de candidato: `BLG-leadshug-instagram-channel` em [backlog](../../backlog/README.md).

O usuário confirmou em2026-10-23 que possui uma conta profissional disponível para testes e acesso para autorizá-la. Essa confirmação estabelece disponibilidade do recurso; a concessão efetiva ao app e sua elegibilidade técnica ainda serão verificadas no fluxo próprio, sem solicitar credenciais no chat.

Na definição seguinte, confirmou também: **“Sim, reunir os canais na mesma BU”**. A decisão de BU operacional está consolidada como arquitetura alvo em [DEC-bu-operational-multichannel](../../decisions/leadshug-multichannel-identity-decisions.md). O [desenho de identidade e roteamento](../analysis/leadshug-multichannel-identity-definition-20261023.md) tem parecer independente e propostas técnicas para o contrato; não é implementação nem aprovação dessas propostas.

## Problem / Desired Outcome

- **Problem:** os dois transportes WhatsApp passaram pelos testes reais, mas não exercitam uma identidade externa sem telefone. A abstração de envio existe; identidade, resolução e cadastro ainda contêm regras específicas de WhatsApp.
- **Desired outcome:** conectar explicitamente uma conta profissional Instagram ao escopo autorizado, receber uma DM no Atendimento e responder por Channel, mantendo isolamento, autoria, persistência e origem correta.
- **Why now:** validar a extensibilidade com um caso real e entregar uma nova entrada de atendimento antes de ampliar importação histórica.

## Constraints / Non-Goals

- A arquitetura alvo confirmada é BU = operação de atendimento; número/perfil pertencem às conexões. A definição foi consolidada em domínio, constituição, política de escopo e Tenancy. O produto atual continua WhatsApp, com cadastro/identidade vinculados a telefone; antes do código, congelar o contrato de adoção e as propostas de contato/ownership/rota. Não inventar telefone nem transformar ID Instagram em E.164.
- Não presumir que uma pessoa no Instagram é o mesmo contato do WhatsApp. Definir identidade qualificada por plataforma e conta/recurso, com IDs opacos; nome, username ou coincidência numérica não autorizam união de históricos.
- Atendimento e automações comuns dependem de Channel/ChannelResolver; seleção, credenciais, HTTP e payloads específicos pertencem à integração. Respeitar capacidades: suporte a texto não implica templates WhatsApp, gestão de modelos ou outras operações.
- Resolução de resposta precisa identificar o vínculo exato: apenas a origem/tipo não basta se forem admitidas várias contas do mesmo canal na BU. Registrar a cardinalidade escolhida e provar que uma resposta não sai por outro vínculo.
- Reutilizar a aceitação persistente de mensagens e a deduplicação por identidade externa/mensagem; não criar inbox paralelo, repetir envios incertos ou prometer exactly-once externo.
- Primeiro percurso proposto: uma pessoa envia DM à conta autorizada; o vendedor lê e responde texto no Atendimento. Conferir as políticas e a janela próprias da API escolhida antes de congelar o contrato; não aplicar automaticamente a política WhatsApp.
- Fora do primeiro percurso: publicação de posts/reels, comentários e automações de comentário para DM, campanhas, prospecção por username, anexos, importação histórica, fusão automática de contatos, Facebook/Messenger, Telegram e implantação Railway.
- Preservar os vínculos WhatsApp e suas provas. Credenciais ficam privadas; nenhuma leitura de `.env*`, mudança Meta, desconexão, envio, túnel ou alteração de serviço faz parte deste enquadramento.

## Canonical Touchpoints

- **Constitution impact:** decisão de BU operacional consolidada; demais decisões de contato/ownership/rota e contrato de adoção ainda precisam de validação antes de implementar.
- **Roadmap impact:** sim — Instagram antecede a frente de histórico; ver [roadmap](../../system_roadmap.md).
- **Primary module:** [integrations-and-channels](../../modules/integrations-and-channels.md).
- **Secondary modules:** [identity-and-tenancy](../../modules/identity-and-tenancy.md), [inbox-and-conversations](../../modules/inbox-and-conversations.md), [audit-and-history](../../modules/audit-and-history.md).
- **Outros alvos da decisão de identidade:** [domínio](../../domain_entities.md), [constituição](../../project_constitution.md), [política de escopo](../../policies/scope_subscope_governance.md).

## Evidence / References

Leitura delimitada do estado atual em2026-10-23, sem executar runtime:

| Evidência | Consequência para o planejamento |
| --- | --- |
| `api-app/src/domain/channels/transport/channel.ts`: Channel.sendMessage, supportedKinds, ChannelOrigin e ChannelResolver | contrato comum já existe; origem ainda é OFICIAL/NAO_OFICIAL. Avaliar ampliação tipada sem casts ou métodos fictícios. |
| `api-app/src/integrations/channels/channel-adapter-registry.ts`: registro de factories por origem | há composição explícita para um novo concreto; sua existência não prova suporte multicanal completo. |
| `api-app/src/integrations/channels/prisma-channel-resolver.ts`: seleção por latest.channelOrigin, readiness e contexto com WABA/epoch | adaptar resolução e política por contrato, sem espalhar condições Instagram nos consumidores. |
| `api-app/prisma/schema.prisma`: ChannelType, BusinessUnit.phone, BuChannel e unique(buId,type); Conversation.contact e unique(buId,contact) | identidade e cardinalidade exigem desenho explícito; não basta adicionar uma classe concreta. |
| [ST-CON-04 concluído](../../todos/completed/features/TODO-leadshug-start-conversation-by-contact.md) e [ST-CON-06 concluído](../../todos/completed/features/TODO-leadshug-channel-abstraction.md) | baseline local de envio/inbox e inversão de dependência; regressão dos dois WhatsApps integra a futura validação. |

Consulta pública: a [coleção oficial da Meta — Instagram Login](https://www.postman.com/meta/instagram/folder/6raa77c/instagram-api-with-instagram-login) documenta contas profissionais Business/Creator, ausência de exigência de Página Facebook nesse fluxo e os escopos `instagram_business_basic` e `instagram_business_manage_messages`. É o caminho recomendado para avaliar primeiro; o painel e a elegibilidade do app existente ainda precisam ser conferidos. Não misturar esse fluxo com permissões/tokens do Facebook Login ou WhatsApp.

Referências primárias para a revisão do contrato: [Instagram Login](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/) e [Messaging API](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api). A leitura direta dessas páginas foi limitada por HTTP429/throttling nesta análise; regras detalhadas de janela, acesso, assinatura, refresh e teste permanecem por verificar, não conclusões derivadas do histórico WhatsApp.

## Ambiguities To Resolve Before TODO

| ID | Ambiguidade | Por que importa | Evidência atual | Tratamento |
| --- | --- | --- | --- | --- |
| AMB-IG-01 | vínculo da conta e identidade externa do contato na BU operacional | define autorização e evita colisões/união indevida | BU operacional confirmada e consolidada; proposta de contato/ownership/rota revisada no documento de análise | validar propostas técnicas e congelar contrato de adoção no ST-IG-01 antes da implementação |
| AMB-IG-02 | conta profissional disponível e operador com autorização | condiciona a prova real | usuário confirmou conta profissional de teste e acesso para autorizá-la em2026-10-23 | disponibilidade confirmada; concessão efetiva e elegibilidade do app permanecem em AMB-IG-03/05 |
| AMB-IG-03 | Instagram Login no app existente ou app dedicado; versão e permissões | publicação WhatsApp não comprova elegibilidade Instagram | documentação oficial geral consultada; painel ainda não conferido | resolver no planejamento, antes de mudar Meta/runtime |
| AMB-IG-04 | cardinalidade, proveniência e regras de resposta | múltiplos vínculos e IDs numéricos não podem escolher destinatário/conta errados | proposta revisada define múltiplos vínculos, owner empresarial transversal e rota exata; resolver/schema atuais ainda dependem de tipo | validar propostas e definir desenho físico, cutover de snapshots legados e consultas limitadas no contrato ST-IG-01 |
| AMB-IG-05 | janela, remetentes elegíveis, webhooks, revogação e renovação | teste sintético ou OAuth não comprovam conversa real | documentação detalhada ainda por verificar | exigir evidência primária e contrato de estado/erros antes de aprovação |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-IG-01 | Definir identidade multicanal e o contrato do atendimento Instagram | integrations-and-channels | identity-and-tenancy; inbox-and-conversations | escolher vínculo BU/conta, identidade de contato/conversa, cardinalidade e caminho Meta; apresentar impactos canônicos e contrato de conexão/recebimento/resposta | coerência com código e provas atuais; revisão de isolamento, colisões e capacidades; decisão humana explícita | create-now: enquadramento e contrato, sem código/runtime | AMB-IG-01 a05 | primeira fatia recomendada; aprovação de prioridade não congela a decisão de domínio |
| ST-IG-02 | Conectar uma conta Instagram com estado verificável | integrations-and-channels | identity-and-tenancy; audit-and-history | autorização e credencial por vínculo, callback seguro, inscrições, cancelamento/revogação e estados honestos, UI sob grants | integração com fakes e PostgreSQL, testes de autorização/assinatura/replay/contexto; Playwright de conexão | defer até contrato aprovado | ST-IG-01 e recursos de teste confirmados | só implementar sob TODO próprio; OAuth concluído não equivale a recebimento comprovado |
| ST-IG-03 | Receber DM e responder texto pelo Atendimento usando Channel | inbox-and-conversations | integrations-and-channels; audit-and-history | entrada autenticada, identidade correta, persistência/realtime, envio/resposta pelo vínculo correto, capacidade/janela explícitas | testes comuns de Channel, integrações e Playwright; DM e resposta reais; regressão oficial/não oficial e retomada | defer até ST-IG-01; refinar em conjunto com ST-IG-02 | conexão autorizada e identidade aprovada | objetivo funcional da primeira entrega; não encerrar só com adapter/fake |

## Retire This Brief When

- O contrato ST-IG-01 tiver decisões e impactos revisados, referências canônicas e aprovação próprias; os TODOs seguintes devem ser delimitados a partir desse contrato. Este brief permanece como proveniência, sem substituir a autoridade dos módulos.
