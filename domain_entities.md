# LeadsHug — Domain Entities
**Version:** 1.0

## Core vocabulary

- **Mantenedora:** organização cliente que administra unidades de negócio.
- **Setor:** agrupamento operacional de BUs dentro de uma Mantenedora.
- **Business Unit (BU):** operação de atendimento e unidade mínima de permissão, histórico e dados. Pode reunir contas e números de diferentes canais sob os mesmos vendedores e grants; sua identidade não depende de telefone.
- **Usuário:** pessoa autenticada que opera o LeadsHug com papel e grants de BU.
- **Contato:** pessoa externa que conversa com uma BU.
- **Conversa:** relação única entre BU e contato, independente do transporte.
- **Mensagem:** evento recebido ou enviado dentro de uma conversa.
- **Canal (Channel):** abstração de comportamento de comunicação; suas implementações concretas atendem protocolos específicos.
- **Conexão de canal:** vínculo de uma BU com uma implementação e um recurso externo autorizado, como número WhatsApp ou conta Instagram. Número e perfil são identidades externas da conexão, não a identidade da BU.
- **Lead:** relacionamento qualificado em evolução, a formalizar no módulo CRM.
- **Atividade:** registro auditável de ação humana ou sistêmica.

## Identity rule

A BU representa a operação de atendimento. Número e perfil pertencem às conexões de canais dessa BU; uma nova plataforma não exige outra BU quando a equipe e as permissões pertencem à mesma operação. A escolha foi confirmada pelo usuário e consolidada em [DEC-bu-operational-multichannel](decisions/leadshug-multichannel-identity-decisions.md).

Essa é a arquitetura alvo. Os contratos entregues ST-CON continuam operando sobre WhatsApp; esta definição não declara migração de schema, cadastro Instagram ou suporte a novas plataformas em execução. A identidade de contato/conversa entre plataformas e a seleção de rota estão propostas no mesmo registro de decisões e exigem contrato próprio antes de implementação.
