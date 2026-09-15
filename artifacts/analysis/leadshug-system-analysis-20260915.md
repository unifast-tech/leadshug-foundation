# LeadsHug — system analysis and modernization plan

Date: 2026-09-15
Status: decision-ready analysis; no product implementation performed

## Executive conclusion

LeadsHug already has a credible, testable **unified-core** foundation. It must be treated as the only active target architecture: NestJS 11, PostgreSQL/Prisma, a React BFF, explicit multi-tenant and Business Unit scope, provider adapters, and four isolated entry surfaces. It is not yet the complete CRM/campaign product described in its vision.

The immediate risk is not a lack of ideas or code volume. It is losing architectural focus through three competing sources: the embedded legacy trees inside `LeadsHug`, the newer but divergent `Central-Whatsapp` references, and `whatsflow_v2`. They contain useful behaviour and operational lessons, but none is an implementation template for the core.

Recommended sequence: establish current-state truth and cutover evidence; close the already-approved Typebot operational gap; complete the security/scope audit; then decide CRM before implementing it. Campaigns, groups and bulk/automation infrastructure follow those boundaries rather than preceding them.

## Evidence collected

### Current product

| Area | Verified state | Evidence |
| --- | --- | --- |
| Core architecture | NestJS API, PostgreSQL through Prisma, React web app, Railway deployment definitions | `LeadsHug/apps/api`, `LeadsHug/apps/web`, `docs/adr/0002`, `0003`, `0006` |
| Domain model | Mantenedora → Setor → Business Unit, scoped users/grants, channels, conversations/messages, API keys, activity log, Typebot and file models | `apps/api/prisma/schema.prisma` |
| Entry surfaces | BFF (`/api/bff`), public integration (`/api/v1`), webhooks (`/webhooks`), internal provisioning (`/api/internal`) | `apps/api/src/surfaces` |
| Core capabilities | Identity, roles, channel connection, unified inbox, history, assignments, API keys/webhook, onboarding, branding and Typebot management/runtime | API controllers and services; product README |
| Local verification on 2026-09-15 | API unit tests: 104 passed; Web unit tests: 16 passed; both production builds passed | `npm test` and `npm run build` in each app |
| Delivery automation | GitHub CI installs, builds, migrates and runs API unit/E2E/coverage, web tests/Playwright and guardrails | `.github/workflows/ci.yml` |

The following were **not** re-executed in this analysis: PostgreSQL E2E suite, Playwright browser suite, Railway deployment, real official WhatsApp traffic, and any production/security audit. Documentation claiming these as complete is historical context, not fresh evidence.

## Architectural map

```text
React web
  -> BFF /api/bff (cookie session, product UX)
NestJS core
  -> domain: tenancy, access, channels, inbox, history, integration, product
  -> Prisma/PostgreSQL: Mantenedora > Setor > Business Unit > number/channel
  -> adapters: Meta, Evolution, Typebot, email
  -> public /api/v1 (partner contract), /webhooks (provider ingress), /api/internal
  -> realtime and periodic routine facilities
```

The central invariant is sound and must remain non-negotiable: a conversation is keyed by Business Unit and contact, rather than by transport; providers are adapters; permissions are materialized at the Business Unit boundary. This agrees with the Foundation modules `identity-and-tenancy`, `inbox-and-conversations`, and `integrations-and-channels`.

## Findings and priority

| Priority | Finding | Why it matters | Recommended bounded follow-up |
| --- | --- | --- |
| P0 — truth/operations | `docs/arquitetura.md` calls itself authoritative but is a 2026-08 pre-unification/legacy snapshot. Product README, contracts and `TODO.md` contain later claims, some still marked draft or pending stage proof. | Engineers can make an apparently justified decision from obsolete state. | Reconcile architecture, contract and TODO status against code, tests and stage evidence; define ownership/freeze status for each legacy tree. |
| P0 — active integration closeout | The approved Typebot TODO has automated coverage but still requires one real official-channel exchange and an explicit correlation/delivery/failure audit decision. | This is live message behaviour; a green mocked path is not a delivery proof. | Finish the existing Typebot TODO before expanding automation scope. |
| P0 — security proof | The product TODO already schedules a first scope audit and a stage retention/expurgo proof. These are not current analysis evidence. | Tenant leakage and retained conversational payloads are core trust risks. | Run the existing audit and stage procedures as separate approved operational TODOs; attach dated evidence. |
| P1 — legacy ownership ambiguity | `LeadsHug/api-oficial` and `LeadsHug/hub-whatsapp` differ substantially from the top-level `Central-Whatsapp` copies. The embedded copies are frozen while the top-level repositories continued shipping changes, contrary to ADR-0001's read-only-mirror plan. | Copying a feature from a path chosen by convenience can reintroduce incompatible security, data or delivery semantics. | Create a compatibility/retirement matrix: runtime owner, deployment owner, cutover condition, read-only/frozen status and allowed extraction method. |
| P1 — CRM is a product decision, not a screen backlog | The Prisma core has no CRM lead/pipeline/card model; ADR-0019 remains proposed. `whatsflow_v2` demonstrates dynamic CRM patterns but uses a different tenancy/control-plane model. | Implementing a Kanban first would define data ownership implicitly and risk corrupting the unified conversation model. | Decide CRM domain contract first: contact identity, lead lifecycle, pipeline ownership, event/audit model, field extensibility and migration/cutover boundaries. |
| P2 — campaigns and groups | Templates/campaigns remain in the official legacy system and groups remain in the unofficial Hub. | Both require channel-specific compliance, retry and rate-control rules; they cannot be a generic “send message” feature. | Write a unified outbound-delivery ADR before code: template/window enforcement, consent, queue ownership, idempotency, throttling, retries/DLQ and audit. |
| P2 — documentation/tooling debt | Active Foundation TODOs plus `project_constitution.md` and `README.md` still contain obsolete `delphi-ai` authority references; product TODO says some historical debts are open while CI now exists. | The new authority topology can be bypassed by stale instructions. | Run a documentation authority rebase after the state-reconciliation work, preserving historical facts but updating operating instructions. |

## Reference-system extraction policy

### Central-Whatsapp

Useful source of **behavioural requirements**, not architecture:

- official-channel templates, the 24-hour Meta window, and approved-template lifecycle;
- unofficial-channel QR pairing, group operations, assignment/claim workflow and channel-specific anti-ban pacing;
- public integration and outgoing-webhook compatibility concerns;
- operational runbooks for provider and volume recovery.

Do not copy its Cloudflare/D1 single-worker or Express/VPS implementation into the NestJS core. It predates the active tenancy and test contracts and remains a parallel production system until a documented cutover condition is satisfied.

### whatsflow_v2

Useful source of **failure lessons and patterns**, not a dependency or target platform:

- durable queue separation, retry/DLQ, observability, heartbeat, catch-up and idempotent recovery for message intake;
- explicit tenant-isolation auditing and repeatable operational runbooks;
- a potential future pattern for configurable CRM fields and pipelines.

Do not inherit its Nexus/WhiteLabel/tenant hierarchy, Supabase/RLS control plane, or broad AI configuration model. Those conflict with the current Foundation contract of Mantenedora → Setor → Business Unit and would introduce a second authorization model. The user reports that its earlier infrastructure/engineering failed; therefore every borrowed idea requires a LeadsHug-specific contract and test, never direct migration.

## Recommended execution sequence

1. **System truth and legacy-boundary reconciliation** — documentation-only plus a deployment/runtime ownership inventory. This removes contradictory sources before more product work.
2. **Typebot production proof and audit closure** — complete the existing approved TODO through a real official message and a correlation/delivery/failure decision.
3. **Security and operational evidence** — execute the existing scope audit and stage retention proof; remediate only findings with an approved tactical TODO.
4. **CRM foundation ADR and contract** — user decision first, then schema/API/UI in independently testable slices.
5. **Unified outbound delivery ADR** — use the reference lessons to define channel policy and durable work before campaigns, groups or large-scale automation.
6. **Documentation authority rebase** — complete when the truth/reconciliation work supplies the canonical current state.

## Decisions required from the user before implementation

1. Confirm whether the first active implementation should be the P0 **system truth and legacy-boundary reconciliation**. It is low-risk and removes ambiguity, but it will update product/Foundation documentation.
2. Before CRM: choose the initial business scope (one pipeline versus configurable pipelines; manual lead creation versus conversion from conversation; required contact fields; and whether legacy data migrates).
3. Before campaigns/groups: choose whether official campaigns or unofficial group operations is the next commercial priority after CRM, and establish acceptable operational risk for the unofficial provider.

## Explicit non-conclusions

- This analysis does not assert that stage is currently healthy; no deployment or external provider action was performed.
- It does not assert that legacy systems are secure or ready for new feature work.
- It does not approve a CRM, campaign, queue, RLS, AI or infrastructure design. Each needs a bounded approved TODO and contract.

## Senior technical review

Claude Code performed a read-only independent review on 2026-09-15 (session `db8c3f1e-7821-41e2-a788-e3435374905a`). Verdict: `no_material_findings`.

The review independently corroborated the core-stack claims, legacy divergence, reference-system boundaries, priority order, and approval constraints. It also confirmed two non-blocking governance details integrated above: the Central/embedded divergence conflicts with ADR-0001's intended read-only-mirror model, and stale `delphi-ai` references still exist in Foundation operating documents.
