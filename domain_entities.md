# LeadsHug — Domain Entities
**Version:** 1.0

## Core vocabulary

- **Mantenedora:** organização cliente que administra unidades de negócio.
- **Setor:** agrupamento operacional de números dentro de uma Mantenedora.
- **Business Unit (BU):** número de WhatsApp e unidade mínima de permissão, histórico e atendimento.
- **Usuário:** pessoa autenticada que opera o LeadsHug com papel e grants de BU.
- **Contato:** pessoa externa que conversa com uma BU.
- **Conversa:** relação única entre BU e contato, independente do transporte.
- **Mensagem:** evento recebido ou enviado dentro de uma conversa.
- **Canal:** transporte oficial ou não oficial usado por uma BU.
- **Lead:** relacionamento qualificado em evolução, a formalizar no módulo CRM.
- **Atividade:** registro auditável de ação humana ou sistêmica.

## Identity rule

A BU é o número. O canal é uma propriedade de integração e não cria uma segunda organização de trabalho para
a mesma conversa.
