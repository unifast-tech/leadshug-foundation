# Cadastro de números — ST-CON-01

Contrato governante: [TODO](../../../todos/active/features/TODO-leadshug-channel-connection-readiness.md). APROVADO pelo usuário em2026-10-15 após a publicação3302964c. Implementação em andamento; entrega geral Pending e prova externa pendente.

Escopo: cadastro guiado oficial Meta e não oficial Evolution/QR, integração com BU, recebimento e primeira conversa recebida para validar o vínculo. Nova conversa proativa é ST-CON-04, próximo recorte solicitado pelo usuário; importação segue depois.

Baseline de fonte: API `ae6a9662c29b77276351aa9de653a47276372246`; Web `4e56f6c1f4515b918d05b8c87e890d42e8542c56`; workspace `cab23188ec796f79131467dcce0a16acedab8d4f`. Primeiro freeze Foundation publicado: `ae503c7b14c3fe51d9cb3488f2fc5df2c5d17301`. O recibo de freeze no TODO aponta a revisão vigente.

O parecer [architecture_opinion](planning-architecture.json) preserva o desenho e pede seis ajustes: isolamento Typebot, deduplicação da entrada, identidade antes do conteúdo Evolution, proprietário durável do recurso Meta, pairing via POST e reautorização com credencial candidata. A proposta integra todos no mesmo TODO, com REG-SEC-01..09 no plano de validação. `fixed-in-plan` no ledger é resolução documental, sem implementação. Pacote v1 e parecer bruto são imutáveis; a crítica independente recebe nova versão com o contrato revisado e esses achados completos.

A [crítica v2](planning-critique.json) leu o pacote completo e reconheceu as seis resoluções; pediu dois ajustes nas interações: invalidar a prova anterior ao reparear e compartilhar a aceitação da mensagem entre sender e echo OUT. Ambos foram integrados na proposta. O desenho usa instância por pairingEpoch, com identidade comprovada na instância nova antes de conteúdo; e aceitação compartilhada por todos os writers pela chave de recurso/mensagem, preservando ID/autoria/DTO. REG-SEC-10/11 são os testes discriminantes. Observações de logs, batch raw por owner e credencial observável sem segredo concretizam requisitos existentes em REG-SEC-12/13.

A [crítica delta v3](planning-critique-delta.json) aprovou o planejamento, com zero bloqueadores e quatro eixos nativos acceptable. Os oito achados estão resolvidos no contrato; três notas baixas detalham testes já exigidos: webhook pausado atravessando a invalidação, segredo da verificação Meta nos logs e refresh do mesmo ID após enriquecimento de autoria. Não autorizam alteração de Inbox.tsx fora do contrato. Código, provas externas e auditorias de entrega continuam pendentes.

Guarda de coerência: [go](evidence/code-coherence.json), quatro premissas com fonte real e caller search adicional. Escopo: [go](evidence/scope-drift-final.json), 23 seções comparadas com a baseline publicada `87c28c6b0f767edde5edf30d4143844f0acd5c2a`, zero mudanças materiais; cláusulas técnicas extras comparadas em [recibo manual](evidence/manual-frozen-contract-comparison.json). Autoridade prévia: [preflight-go](evidence/authority-preapproval-final.json), `execution_authority_granted=false`. As normalizações/merges são derivados com proveniência; pareceres brutos permanecem íntegros.

Execução autorizada: [aprovação registrada](evidence/approval-20261015.json), [routing go](evidence/routing-execution.json) e [authority go](evidence/authority-execution.json). Contratos owner consolidados antes do código. [Checkpoint1](evidence/checkpoint1-execution-evidence.md) concluiu persistência/cifra/aceitação keyed com119unitários e3testes PostgreSQL na fonte final desse checkpoint; não equivale à validação final. Checkpoint2 da API em andamento, seguido de UI/runtime, testes finais, reviews e prova real. [Preparação da conta Meta/HTTPS](local-setup.md) e [handoff de runtime planejado](runtime-handoff.md) registram as dependências ainda ausentes. Nova conversa por contato segue como ST-CON-04 antes da importação.

A validação estrutural v3 inicial encontrou um cabeçalho com prefixo de formatação incorreto na seção de coerência; corrigido sem mudar escopo. O recibo v3-corrected é o resultado PASS vigente; o primeiro resultado permanece como histórico.

Fontes primárias consultadas em2026-10-15:

- [Meta: Embedded Signup](https://www.postman.com/meta/whatsapp-business-platform/collection/du6gzjv/embedded-signup): autorizar cliente é seguido de etapas de integração; elegibilidade do app continua dependência externa.
- [Meta: registro do número](https://www.postman.com/meta/whatsapp-business-platform/request/mk4p87j/register-phone-number): registro separado, com PIN de seis dígitos. Cadastro/autorização não bastam para afirmar canal pronto.
- [Meta: assinatura da WABA](https://www.postman.com/meta/whatsapp-business-platform/request/0yubu4i/subscribe-app-to-whatsapp-business-account): assinatura integra o recebimento. Não autoriza trocar callback de número em outro sistema silenciosamente.
- [Meta: janela de suporte](https://www.postman.com/meta/whatsapp-business-platform/folder/fuaee8l/statuses-object): abertura proativa oficial exige tratamento de templates fora da janela; ST-CON-04 terá contrato próprio. Campos de preço históricos dessa fonte não são adotados.
- [Evolution: releases oficiais](https://github.com/evolution-foundation/evolution-api/releases): v2.3.7 stable; versão2.4 pre-release não foi escolhida.

Consulta read-only ao registry confirmou `evoapicloud/evolution-api:v2.3.7` com índice OCI `sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`; runtime novo deve registrar a versão efetiva antes de prova. Não se adota o container legado.

As páginas developers.facebook.com continuam limitadas; coleção primária da Meta em Postman foi acessível. A configuração efetiva do app, Graph version admitida, WABA de teste e callback devem ser verificadas antes da prova externa; referência histórica não substitui verificação.
