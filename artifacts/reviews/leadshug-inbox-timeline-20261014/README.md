# Histórico paginado da inbox — ST-ATT-01

Implementação aprovada em2026-10-14 e validada localmente em2026-10-15. [TODO governante](../../../todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md). Estado atual: **Local-Implemented**; aderência, TQA e revisão final aceitas, guardas de entrega go. Commits locais registrados; publicação documental/relocação do TODO em fechamento.

A inbox abre as mensagens recentes e oferece todo o histórico por cursor. Atualizações preservam mensagens, leitura, posição, rascunho, contexto e metadados; recuperação pendente tem limite de consultas e continuação explícita. Contrato owner: [inbox-and-conversations](../../../modules/inbox-and-conversations.md).

| Prova local | Resultado | Evidência |
| --- | --- | --- |
| API leafs CI |generate/lint/build exit0,115unit | [stdout](evidence/api-ci-light-revision2-20261015.log) |
| API PostgreSQL completo |224/224 | [raw](evidence/api-e2e-authority.log) |
| Web unit + browser completo |20/20unit,36/36browser | [raw final6](evidence/web-authority-revision6-final-full-20261015.log) |
| FRC repetido |3/3 | [raw final6](evidence/web-authority-revision6-final-frc3-20261015.log) |
| Fonte/runtime |16hashes conferidos; servido==dist | [attestation full](evidence/attestation-browser-web-authority-revision6-final-full-20261015.json), [FRC](evidence/attestation-browser-web-authority-revision6-final-frc3-20261015.json) |
| SQL/concorrência/carga limitada | planos e invariantes registrados | [EPS](pcv-eps.json), [BCI](pcv-bci.json), [RLS](pcv-rls.json), [FRC](pcv-frc.json) |

[Execução e limites](execution-evidence.md) registra comandos, topology isolada, resultados, contraprovas restauradas e gerações históricas. [Resumo final do executor](evidence/executor-revision6-summary.json) liga os fontes às coletas. Testes source-owned usam Nest/session/grants/PostgreSQL/WebSocket reais e dublês apenas nas portas externas.

[Round1 de aderência](delivery-adherence-round-1.json) e [delta](delivery-adherence-delta.json) produziram correções do recovery/alerta; a [resolução independente](delivery-adherence-resolution.json) terminou sem novos achados e aceitou o produto. [TQA inicial](delivery-tqa-round-1.json) e [delta](delivery-tqa-delta.json) exigiram provas mais discriminantes; vazio e gatilho reconnect isolado do primeiroonopen aceitos na [TQA causal](delivery-tqa-causal-resolution.json), com negativo reconnect-only discriminante. [Final review](delivery-final.json) aceito sem achados materiais pendentes. Todos os pareceres são internos no-context, com raw/schema/merge; nenhum waiver.

[Admissão de testes](test-surface-admission.md), [dívida de verificação](verification-debt.md) e [observações](implementation-observations.md) distinguem escopo, evidência e limites. Os pacotes imutáveis em evidence/ preservam o material exato entregue aos revisores.

O closeout é local-only em feature/inbox-timeline-pagination para API/Web, com documentação Foundation main. Transferência, estados e anexos permanecem em stories próprias; deploy, promoção remota de produto e Production-Ready não fazem parte desta entrega.

Planejamento histórico: baseline congelada649372fbe81f6cccc0f8902b52fe32e2ecfc061a; [arquitetura](architecture-review.json), [crítica](critique-round-1.json), [resolução](critique-resolution.json), [premissas](assumption-coherence.json), [scope drift](scope-drift.json) e [pacote](package.md). O preflight de planejamento antecede APROVADO e não representa a autoridade atual de execução.

Commits locais: API`ae6a9662c29b77276351aa9de653a47276372246`; Web`4e56f6c1f4515b918d05b8c87e890d42e8542c56`, ambos feature/inbox-timeline-pagination. [Bridge16blobs](evidence/committed-source-attestation.json) liga commits aos snapshots de validação sem reescrevê-los. Guardas finais: [authority](evidence/authority-final.json), [completion](evidence/completion-final.json), [closeout](evidence/closeout-final.json).
