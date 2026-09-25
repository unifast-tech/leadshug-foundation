# LeadsHug Backlog

**Version:** 1.0

The backlog is the canonical home for candidate work that is not approved for execution. It owns each candidate's disposition and next gate. A candidate is not a tactical TODO; neither this record nor a `Selected-for-Planning` state authorizes implementation.

## Record schema

Each new record carries an immutable ID, title, state, source/evidence, value/risk, dependencies, disposition owner, and next gate. Lifecycle definitions and transitions live in [`../evolution_lifecycle.md`](../evolution_lifecycle.md).

## Candidates

| Immutable ID | Title | State | Source / evidence | Value / risk | Dependencies | Disposition owner | Next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BLG-leadshug-evolution-synthesis | LeadsHug evolution synthesis (ST-04) | Deferred | [pre-code evolution brief](../artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md) | synthesize evidence only after both independent studies; early synthesis risks false priority | ST-01/ST-02 completed; ST-03 content complete and in closeout | strategic steward | select for planning only after ST-03 closeout; no implementation or prioritization is authorized |

The IDs above are references for future planning; their live disposition and next gate remain only in this table.

## Fulfilled candidate handoffs

| Immutable ID | Fulfilled by | Evidence | Downstream use |
| --- | --- | --- | --- |
| BLG-central-whatsapp-capability-study | [completed ST-02 TODO](../todos/completed/features/TODO-leadshug-central-whatsapp-capability-study.md) | [27-capability catalog and 204-unit ledger](../artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md) | input to ST-04 after ST-03; no capability is prioritized or authorized by this handoff |
| BLG-whatsflow-channel-attendance-study | [ST-03 TODO em closeout](../todos/active/features/TODO-leadshug-whatsflow-channel-attendance-study.md) | [conceptual channel and attendance model](../artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-20260925.md) | conteúdo concluído e em final review; input para ST-04 somente após o closeout, sem autorização de produto |
