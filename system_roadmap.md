# LeadsHug — System Roadmap

**Version:** 1.0

The roadmap owns strategic theme/phase, relative horizon, expected outcome, dependencies, and exit gate. It is not execution authority and does not duplicate candidate disposition, TODO evidence, capability maturity, or module-local truth. Lifecycle semantics live in [evolution_lifecycle.md](evolution_lifecycle.md).

## Horizon rule

`Now`, `Next`, `Later`, and `Unscheduled` are relative planning horizons, not dates, releases, or delivery promises. A roadmap phase is a strategic theme; it is orthogonal to horizon and capability maturity. Dates or release commitments require separate explicit approval.

`Gate status` is a derived roadmap signal, not a sixth lifecycle state machine and not a projection of capability state. It is `Open` while the row's exit gate lacks accepted evidence and becomes `Exit-Gate-Met` only when links to the responsible canonical module/TODO evidence satisfy that gate. It cannot be advanced by editing this table alone.

| Phase / theme | Horizon | Gate status | Dependencies | Expected outcome | Exit gate |
| --- | --- | --- | --- | --- | --- |
| Phase 1 — Unified core | Now | Open | Foundation lifecycle and approved tactical slices | Identity, multi-tenancy, BUs/numbers, channels, receipt, inbox, queue, assignment, response, history, and public API are coherently planned through responsible modules. | Responsible module truth and approved TODO evidence establish the intended core slice. |
| Phase 2 — Operational hardening | Next | Open | coherent core boundaries | Observability, audit, sending limits, safe retention, scope validation, contracts, and Railway operation are planned as governed operational capabilities. | Each admitted capability has its module/contract owner and accepted validation evidence. |
| Phase 3 — CRM foundation | Later | Open | unified history and stable operational boundaries | Consolidated contact, lead, funnel, relationship record, activities, and history-oriented automation are strategically framed. | A separately approved roadmap/TODO package names stable domain and module boundaries. |
| Phase 4 — Relationship campaigns | Unscheduled | Open | CRM foundation and applicable WhatsApp policy constraints | Approved templates, lists, sends, campaigns, and automation are strategically framed without promising delivery. | Responsible contracts, policy fit, and approved tactical execution evidence exist. |

Gate status is evidence-derived and never claims that a capability is implemented. Capability state remains solely in responsible module records. Every implementation still requires an approved tactical TODO, explicit `APROVADO`, and the applicable authority guard.
