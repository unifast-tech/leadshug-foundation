# LeadsHug — Domain Entities
**Version:** 1.0

## Core vocabulary

- **Mantenedora:** organização cliente que administra unidades de negócio.
- **Setor:** agrupamento operacional de BUs dentro de uma Mantenedora.
- **Business Unit (BU):** operação de atendimento e unidade mínima de permissão, histórico e dados. Pode reunir contas e números de diferentes canais sob os mesmos vendedores e grants; sua identidade não depende de telefone.
- **Usuário:** pessoa autenticada que opera o LeadsHug com papel e grants de BU.
- **Contato:** interlocutor local da BU, com ID estável; a identidade externa não é sua chave primária.
- **Conversa:** agregado único por BU e contato local, com IDs/histórico preservados; transporte é determinado pela rota da interação.
- **Mensagem:** evento recebido ou enviado dentro de uma conversa.
- **Canal (Channel):** abstração de comportamento de comunicação; suas implementações concretas atendem protocolos específicos.
- **Conexão de canal:** vínculo de uma BU com uma implementação e um recurso externo autorizado, como número WhatsApp ou conta Instagram. Número e perfil são identidades externas da conexão, não a identidade da BU.
- **Identidade externa do contato:** plataforma, namespace, escopo de conta/app e referência opaca do peer; WhatsApp pessoa e grupo têm namespaces distintos. Instagram não é unido por username, telefone de perfil ou coincidência numérica.
- **Identidade empresarial do canal:** recurso atendido com owner durável único no LeadsHug, atravessando adapters comprovados do mesmo número; desconectar não transfere propriedade.
- **Identidade de provedor:** recurso técnico e namespace de deduplicação/proveniência de um adapter; conserva seu ID e não é colapsado ao compartilhar recurso empresarial.
- **Rota de conversa:** associação imutável da conversa à identidade destinatária e ao recurso empresarial da mesma BU/contato; o envio captura também a conexão, versão e geração.
- **Lead:** relacionamento qualificado em evolução, a formalizar no módulo CRM.
- **Atividade:** registro auditável de ação humana ou sistêmica.

## Identity rule

A BU representa a operação de atendimento. Número e perfil pertencem às conexões de canais dessa BU; uma nova plataforma não exige outra BU quando a equipe e as permissões pertencem à mesma operação. A escolha foi confirmada pelo usuário e consolidada em [DEC-bu-operational-multichannel](decisions/leadshug-multichannel-identity-decisions.md).

Essa é a arquitetura alvo. Os contratos entregues ST-CON continuam operando sobre WhatsApp; esta definição não declara migração de schema, cadastro Instagram ou suporte a novas plataformas em execução. Contato qualificado, ownership empresarial/provedor e rota explícita foram aprovados em2026-10-23 no [TODO ST-IG-03 v1.3](todos/active/features/TODO-leadshug-instagram-channel.md) e consolidados nos seus owners. A implementação está em curso e não há nova capacidade multicanal entregue por esta atualização documental. Na fatia aprovada, uma BU admite um recurso WhatsApp durável (oficial+Evolution comprovados sobre o mesmo número) e várias contas Instagram; não há merge entre plataformas.
