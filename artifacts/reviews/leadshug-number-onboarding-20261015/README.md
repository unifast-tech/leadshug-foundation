# Cadastro de números — planejamento ST-CON-01

Contrato governante: [TODO](../../../todos/active/features/TODO-leadshug-channel-connection-readiness.md). Proposta em preparação para revisão; nenhuma execução de produto ou aprovação reivindicada.

Escopo: cadastro guiado oficial Meta e não oficial Evolution/QR, integração com BU, recebimento e primeira conversa recebida para validar o vínculo. Nova conversa proativa é ST-CON-04, próximo recorte solicitado pelo usuário; importação segue depois.

Baseline de fonte: API `ae6a9662c29b77276351aa9de653a47276372246`; Web `4e56f6c1f4515b918d05b8c87e890d42e8542c56`; workspace `cab23188ec796f79131467dcce0a16acedab8d4f`. Foundation baseline/freeze será registrado após commit/push do pacote completo.

Fontes primárias consultadas em2026-10-15:

- [Meta: Embedded Signup](https://www.postman.com/meta/whatsapp-business-platform/collection/du6gzjv/embedded-signup): autorizar cliente é seguido de etapas de integração; elegibilidade do app continua dependência externa.
- [Meta: registro do número](https://www.postman.com/meta/whatsapp-business-platform/request/mk4p87j/register-phone-number): registro separado, com PIN de seis dígitos. Cadastro/autorização não bastam para afirmar canal pronto.
- [Meta: assinatura da WABA](https://www.postman.com/meta/whatsapp-business-platform/request/0yubu4i/subscribe-app-to-whatsapp-business-account): assinatura integra o recebimento. Não autoriza trocar callback de número em outro sistema silenciosamente.
- [Meta: janela de suporte](https://www.postman.com/meta/whatsapp-business-platform/folder/fuaee8l/statuses-object): abertura proativa oficial exige tratamento de templates fora da janela; ST-CON-04 terá contrato próprio. Campos de preço históricos dessa fonte não são adotados.
- [Evolution: releases oficiais](https://github.com/evolution-foundation/evolution-api/releases): v2.3.7 stable; versão2.4 pre-release não foi escolhida.

Consulta read-only ao registry confirmou `evoapicloud/evolution-api:v2.3.7` com índice OCI `sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`; runtime novo deve registrar a versão efetiva antes de prova. Não se adota o container legado.

As páginas developers.facebook.com continuam limitadas; coleção primária da Meta em Postman foi acessível. A configuração efetiva do app, Graph version admitida, WABA de teste e callback devem ser verificadas antes da prova externa; referência histórica não substitui verificação.
