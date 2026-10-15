# LeadsHug Backlog

**Version:** 1.0

The backlog is the canonical home for candidate work that is not approved for execution. It owns each candidate's disposition and next gate. A candidate is not a tactical TODO; neither this record nor a `Selected-for-Planning` state authorizes implementation.

## Record schema

Each new record carries an immutable ID, title, state, source/evidence, value/risk, dependencies, disposition owner, and next gate. Lifecycle definitions and transitions live in [`../evolution_lifecycle.md`](../evolution_lifecycle.md).

## Candidates

| Immutable ID | Title | State | Source / evidence | Value / risk | Dependencies | Disposition owner | Next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BLG-leadshug-evolution-synthesis | LeadsHug evolution synthesis (ST-04) | Selected-for-Planning | [pre-code evolution brief](../artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md) | synthesize evidence only after both independent studies; early synthesis risks false priority | ST-01, ST-02 and ST-03 completed | strategic steward | frame/refine ST-04 separately; no implementation or prioritization is authorized |
| BLG-leadshug-attendance-evolution | Atendimento com transferência histórico completo anexos e estados | Selected-for-Planning | [brief de atendimento](../artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md) | ampliar o atendimento existente; preservar isolamento, ownership e ordenação dos eventos | contratos por recorte, validação local isolada e decisões de transferência/mídia/status | strategic steward | ST-ATT-01 Local-Implemented e revisado no [TODO de histórico](../todos/completed/features/TODO-leadshug-inbox-message-timeline-pagination.md); ST-ATT-02/03/04 aguardam contratos e aprovação próprios; prioridade seguinte passou a conexões/testes em BLG-leadshug-channel-readiness-and-history por concordância do usuário em2026-10-15 |
| BLG-leadshug-channel-readiness-and-history | Conexões verificáveis e histórico dos canais oficial e não oficial | Selected-for-Planning | [brief de canais](../artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md) | tornar testes reais de atendimento confiáveis; evitar falso conectado, duplicatas e ordem histórica incorreta | ambiente/versão Evolution, modalidade/WABA, acesso e callbacks de teste; dois canais oferecidos pelo usuário | strategic steward | refinar [ST-CON-01 draft](../todos/active/features/TODO-leadshug-channel-connection-readiness.md), resolver dependências, congelar/revisar contrato antes de APROVADO; ST-CON-02/03 seguem com contratos próprios |

The IDs above are references for future planning; their live disposition and next gate remain only in this table.

## Fulfilled candidate handoffs

| Immutable ID | Fulfilled by | Evidence | Downstream use |
| --- | --- | --- | --- |
| BLG-central-whatsapp-capability-study | [completed ST-02 TODO](../todos/completed/features/TODO-leadshug-central-whatsapp-capability-study.md) | [27-capability catalog and 204-unit ledger](../artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md) | input to ST-04 after ST-03; no capability is prioritized or authorized by this handoff |
| BLG-whatsflow-channel-attendance-study | [completed ST-03 TODO](../todos/completed/features/TODO-leadshug-whatsflow-channel-attendance-study.md) | [conceptual channel and attendance model](../artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-20260925.md) | input to ST-04; recommendations remain unprioritized and do not authorize product changes |
