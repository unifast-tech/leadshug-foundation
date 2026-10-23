# LeadsHug Scope Governance
**Version:** 1.0

## Canonical hierarchy

`Mantenedora -> Setor -> Business Unit (operação de atendimento) -> Conversa/Contato`.

The Business Unit is the minimum authorization and data-isolation boundary. A user may hold grants for one or
more BUs; no controller, service, repository or frontend adapter may infer access from UI state alone.

A mesma BU pode reunir conexões de WhatsApp e Instagram sob os mesmos vendedores e grants. A conta/perfil ou número do canal não cria outro escopo de autorização: a conexão pertence à BU autorizada. A [decisão de BU operacional](../decisions/leadshug-multichannel-identity-decisions.md) define a arquitetura alvo; a adoção no produto e os contratos de identidade/roteamento exigem TODO próprio, sem criar nova superfície por inferência.

## Runtime surfaces

| Surface | Authentication | Responsibility |
| --- | --- | --- |
| `/api/bff` | session | authenticated web application |
| `/api/v1` | partner API key | public integrations |
| `/api/internal` | service credential | trusted internal calls |
| `/webhooks` | provider verification | inbound channel events |
| /privacidade.html | public static document | Institutional privacy information only; no tenant/account/BU resolution, forms, SDK or business-data access. |

Outbound provider adapters are integration boundaries, not public runtime surfaces.

## Rules

- New scope or surface requires a TODO and constitution update.
- Every route documents tenant, account and BU resolution.
- Cross-BU reads fail closed and are covered by tests.
- Frontend routes do not define authorization; backend guards do.
