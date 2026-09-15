# LeadsHug — architecture truth and legacy boundaries

Date: 2026-09-15
Status: verified local repository evidence; deployment and production-runtime status intentionally not asserted

## Canonical target architecture

`LeadsHug/apps/api` and `LeadsHug/apps/web` are the sole active **target architecture** for new product work. The target is supported by accepted ADRs 0002 (Railway/NestJS), 0003 (PostgreSQL/Prisma), 0006 (entry surfaces), 0013 (abandon rather than runtime-couple the old environment), and by the Foundation domain contracts.

```text
React web -> BFF /api/bff -> NestJS domains -> Prisma/PostgreSQL
                         -> adapters (Meta, Evolution, Typebot, email)
                         -> public /api/v1, provider /webhooks, internal /api/internal
```

The following do not change with this document:

- Mantenedora → Setor → Business Unit remains the tenancy hierarchy.
- A conversation is unique by Business Unit and contact, independent of transport.
- The Meta, Evolution, Typebot and email integrations are adapters, not system authorities.
- Any product, schema, deployment, provider or cutover change requires its own approved tactical TODO.

## Evidence and terminology

| Term | Meaning in this artifact |
| --- | --- |
| **Target architecture** | The approved architecture for all new LeadsHug capability work. It does not prove that a deployment is currently healthy. |
| **Embedded snapshot** | A legacy tree tracked inside the LeadsHug product repository, without its own `.git`; it is not an independent repository checkout. |
| **Legacy repository** | An independent checkout with its own Git identity and remote. Its local commit history proves code evolution, not deployed runtime health. |
| **Reference-only** | May supply a requirement, failure lesson or acceptance scenario; it may not supply code, tenancy, deployment or authorization architecture by copying. |
| **Cutover** | A user-approved operational event. This document defines no date, action or authorization for one. |

## Repository and runtime-boundary matrix

| Tree | Local Git evidence, 2026-09-15 | Verified role | Mutation status for LeadsHug work | Allowed use now | Cutover/runtime condition |
| --- | --- | --- | --- | --- | --- |
| `LeadsHug/apps/{api,web}` | Product repo `unifast-tech/LeadsHug`, branch `add_typeform_cloud`, head `d83ec11` | **Canonical target architecture** | Active only through approved product TODOs | Implement bounded LeadsHug work under Foundation/Engineering contracts | Deployment health and release remain independently evidenced and manually approved |
| `LeadsHug/api-oficial` | No nested `.git`; last path import `4ac8dde`, 2026-08-17 | **Embedded legacy snapshot** | Frozen; no feature extraction by copying | Historical behaviour, old data/schema vocabulary and regression ideas | Not a current-source declaration; never deploy or edit it as part of a new-core TODO without renewed approval |
| `LeadsHug/hub-whatsapp` | No nested `.git`; last product-path change `994e1e8`, 2026-08-28 | **Embedded legacy snapshot** | Frozen; no feature extraction by copying | Historical behaviour, provider payloads, user-flow and operations lessons | Not a current-source declaration; never deploy or edit it as part of a new-core TODO without renewed approval |
| `Central-Whatsapp/api-oficial` | Independent repo `unifast-tech/api-oficial`, `main`, head `9368421`, 2026-09-11 | **Independent legacy/reference repository** | Out of LeadsHug write scope | Behavioral requirements for official templates, campaign lifecycle and Meta constraints | Its deployed status is not verified locally. User must explicitly decide any formal ownership, freeze or retirement action |
| `Central-Whatsapp/hub-whatsapp` | Independent repo `unifast-tech/hub-whatsapp`, `main`, head `51bc16e`, 2026-09-10 | **Independent legacy/reference repository** | Out of LeadsHug write scope | Behavioural requirements for unofficial connection, groups, inbox assignment, rate controls and recovery | Its deployed status is not verified locally. User must explicitly decide any formal ownership, freeze or retirement action |
| `whatsflow_v2` | Independent repo `UnifastTech/whatsflow_v2`, `stage`, head `3a36436c`, 2026-08-13 | **Reference-only system** | Out of LeadsHug write scope | Failure lessons: durable queues, idempotency, catch-up, DLQ/observability and tenancy-test patterns | No integration or migration boundary exists; user-reported former runtime does not establish a current deployment |

## Reconciled facts and contradictions

### 1. ADR-0001 is historically accepted, but its mirror rule is not the observed present state

ADR-0001 correctly records the original subtree import and says that `api-oficial` and `hub-whatsapp` should stop receiving commits in their original remotes. The local evidence is different today: the embedded official snapshot ends at the 2026-08-17 import while `Central-Whatsapp/api-oficial` reached `9368421` on 2026-09-11; the embedded Hub path last changed on 2026-08-28 while `Central-Whatsapp/hub-whatsapp` reached `51bc16e` on 2026-09-10.

This is a **governance divergence**, not a synchronization task. Pulling, merging, subtree-splitting, copying, or deleting either side would choose an ownership model and is outside this TODO.

### 2. ADR-0013 controls the target relationship, not observed deployment state

ADR-0013 says the new product must not runtime-couple, synchronize or use the old environment as rollback. It also requires a future turn-off only after the replacement is sufficiently complete and the user-approved operational prerequisites exist. Therefore the embedded and Central legacy trees are not valid dependencies of the new runtime even if a legacy deployment still exists.

### 3. Product documents have different time horizons

`LeadsHug/docs/arquitetura.md` is a useful historical pre-unification inventory, but its self-description as the authoritative current state conflicts with newer code, ADRs, CI and Typebot work. `README.md`, contracts, deployment guides and `TODO.md` each record later slices, some with unverified stage claims. Historical documents stay preserved; this artifact is the navigation point until a separately approved documentation rebase aligns them.

### 4. Authority migration drift remains visible

Foundation documents still contain some `delphi-ai` references despite the completed retirement/migration. The current authorities are `leadshug-engineering` for engineering practice and `leadshug-foundation` for product/governance. Updating legacy references is documentation work, not a change to active product behavior.

## Safe legacy-capability extraction procedure

Every feature inspired by a legacy tree follows this order:

1. Write the desired user outcome and identify the relevant reference behaviour.
2. State which LeadsHug invariant applies: tenant/BU scope, conversation identity, provider adapter, public contract, audit, or channel policy.
3. Decide the new data and API contract in a LeadsHug ADR/TODO before touching code.
4. Implement only in `LeadsHug/apps/api` and/or `LeadsHug/apps/web`; do not import files, schemas, dependencies, environment configuration or deployment topology from a reference tree.
5. Add tests that prove LeadsHug's contract, including scope/isolation where data is involved and provider failure/idempotency where messages are involved.
6. Treat a production legacy system only as an external actor for manually approved validation; it never becomes a rollback path or source of live reads.

## Decisions deliberately left to the user

No decision is required to use the matrix above. The following choices remain material and must be approved separately:

1. **Legacy ownership policy:** formally freeze/archival-mark the two `Central-Whatsapp` repositories, or explicitly retain them as independently developed legacy products until a named retirement event.
2. **Documentation rebase scope:** update only Foundation/Engineering authority references first, or also revise the historical/current-state framing in the LeadsHug product documentation.
3. **Retirement trigger:** define the product and operational conditions that permit an eventual legacy shutdown. This cannot be inferred from local code or current commits.

## Next safe follow-up

The next low-risk implementation candidate is a documentation authority rebase. It would update stale `delphi-ai` operating references and establish a maintained index from product documents to this matrix, while retaining historical ADRs and legacy snapshots unchanged. It should be a separate approved TODO because it changes governed documentation across repositories.

## Senior technical review

Claude Code performed a read-only review on 2026-09-15 (session `fc781c38-0000-44ea-8603-45e5ae195e4c`). Verdict: `no_material_findings`.

The reviewer independently verified every repository identity, branch, head commit and date in the matrix, plus the ADR-0001, 0002, 0003, 0006 and 0013 interpretations. It confirmed that the artifact distinguishes local facts from runtime assumptions and leaves ownership/freeze/cutover choices with the user. The only non-material observation is that “Foundation contracts” is shorthand: the Foundation `contracts/` directory is still minimal and is not itself a populated contract source.
