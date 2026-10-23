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

## Identidade e rota aprovadas no ST-IG-03

Cada contato, identidade destinatária, conversa, rota, recurso empresarial e conexão deve resolver a mesma BU; a identidade destinatária também deve pertencer ao mesmo contato da conversa. Mesmo escopo de BU não permite trocar interlocutor ou conta atendida. Ownership empresarial não se transfere ao reconectar ou remover um adapter. O backend resolve peer e rota por referências confiáveis; parâmetros do browser não conferem identidade nem grant.

Esses invariantes foram aprovados no [contrato v1.3](../todos/active/features/TODO-leadshug-instagram-channel.md) em2026-10-23; implementação e validação estão em curso. As superfícies existentes não são ampliadas para novos públicos por essa aprovação.
