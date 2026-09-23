# LeadsHug Backlog

**Version:** 1.0

The backlog is the canonical home for candidate work that is not approved for execution. It owns each candidate's disposition and next gate. A candidate is not a tactical TODO; neither this record nor a `Selected-for-Planning` state authorizes implementation.

## Record schema

Each new record carries an immutable ID, title, state, source/evidence, value/risk, dependencies, disposition owner, and next gate. Lifecycle definitions and transitions live in [`../evolution_lifecycle.md`](../evolution_lifecycle.md).

## Candidates

| Immutable ID | Title | State | Source / evidence | Value / risk | Dependencies | Disposition owner | Next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BLG-central-whatsapp-capability-study | Central-Whatsapp capability study (ST-02) | Selected-for-Planning | [pre-code evolution brief](../artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md) | identify reusable capability gaps without mechanical porting | comparison baseline ambiguity | strategic steward | frame a separate study TODO after ST-01 |
| BLG-whatsflow-channel-attendance-study | whatsflow_v2 channel and attendance study (ST-03) | Selected-for-Planning | [pre-code evolution brief](../artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md) | clarify attendance concepts without importing legacy debt or vocabulary collisions | resolve attendance-model ambiguity before canonization | strategic steward | frame a separate study TODO after ST-01 |
| BLG-leadshug-evolution-synthesis | LeadsHug evolution synthesis (ST-04) | Deferred | [pre-code evolution brief](../artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md) | synthesize evidence only after both independent studies; early synthesis risks false priority | ST-02 and ST-03 | strategic steward | reassess after both studies conclude |

The IDs above are references for future planning; their live disposition and next gate remain only in this table.
