# Module: Audit and History
**Version:** 1.0

Owns durable activity history, message auditability, exports and access to historical relationship data.

## Invariants

- History is append-oriented and is not silently discarded.
- Every record is tenant- and BU-scoped.
- Read permission is evaluated independently from write permission.


## Cadastro e diagnóstico de canais — ST-CON-01

APROVADO em2026-10-15, implementação exercitada localmente em2026-10-16 ([all499/22migrações e fonte/freshness](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp27-receipt.json)); architecture/security, Performance/cutover e TQA independentes aceitos no escopo local. Final review local aceito; source commits/bridge byteexact registrados, closeout geral e prova externa permanecem pendentes no TODO no [TODO](../todos/active/features/TODO-leadshug-channel-connection-readiness.md). Canais é o owner das etapas; audit-and-history governa seus registros duráveis.

- Atividade de cadastro/autorizar/confirmar/parear/verificar/cancelar preserva ator, Mantenedora/BU, etapa, correlação e erro de catálogo, sem segredo, QR ou conteúdo externo bruto no audit.
- Só conteúdo de recurso com owner/identidade verificados entra em raw scoped. Batch Meta é particionado por recurso/BU depois de validar assinatura do corpo original; partes desconhecidas/retiradas conservam apenas metadados allowlisted.
- Token, apikey, authorization, code/PIN/QR e componentes secretos de URLs são removidos antes de raw, audit, erro ou logs. Proteger URI Evolution e hub.verify_token Meta também no gateway/access/error/application logs.
- Payload sem identidade corrente, inclusive webhook velho pausado através da aposentadoria, não grava conteúdo. Rejeição/pending só registra metadados seguros.
- Cancelamento/remoção/repareamento não apagam BU, conversas ou histórico; tombstones de identidade preservam owner. Sem merge/delete silencioso na migration.
