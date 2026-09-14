# LeadsHug Scope Governance
**Version:** 1.0

## Canonical hierarchy

`Mantenedora -> Setor -> Business Unit (número) -> Conversa/Contato`.

The Business Unit is the minimum authorization and data-isolation boundary. A user may hold grants for one or
more BUs; no controller, service, repository or frontend adapter may infer access from UI state alone.

## Runtime surfaces

| Surface | Authentication | Responsibility |
| --- | --- | --- |
| `/api/bff` | session | authenticated web application |
| `/api/v1` | partner API key | public integrations |
| `/api/internal` | service credential | trusted internal calls |
| `/webhooks` | provider verification | inbound channel events |

Outbound provider adapters are integration boundaries, not public runtime surfaces.

## Rules

- New scope or surface requires a TODO and constitution update.
- Every route documents tenant, account and BU resolution.
- Cross-BU reads fail closed and are covered by tests.
- Frontend routes do not define authorization; backend guards do.
