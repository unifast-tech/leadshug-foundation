# Central-Whatsapp independent legacy policy

## Status

Approved by Gabriel on 2026-09-15. This policy applies to:

- `Central-Whatsapp/api-oficial`
- `Central-Whatsapp/hub-whatsapp`

They are **independent legacy repositories**, retained as sources of behavioral and operational inspiration while `LeadsHug/apps/api` and `LeadsHug/apps/web` remain the sole target architecture for new product work.

## Permitted use

- Read a legacy system to understand user workflows, provider constraints, incident history, runbooks, acceptance scenarios and operational lessons.
- Translate a useful observation into a new LeadsHug requirement, ADR, tactical TODO, acceptance criterion or regression test.
- Perform maintenance in a legacy repository only under a separately approved task scoped to that repository and its own operational owner.

## Prohibited use

- Treat a Central-Whatsapp repository as a LeadsHug runtime dependency, rollout path, rollback path or source of live reads/writes.
- Copy source files, database schema, environment configuration, dependency manifests, secrets, infrastructure topology or deployment configuration into LeadsHug.
- Synchronize, subtree-merge, migrate data from, archive, freeze, delete, deploy or alter permissions of either legacy repository under a LeadsHug task without renewed user approval.
- Implement a new product capability in Central-Whatsapp when its intended destination is LeadsHug.

## Extraction contract

Every inspiration extracted from Central-Whatsapp must first be restated as a LeadsHug-owned problem and must identify the applicable tenancy, Business Unit, conversation, provider-adapter, audit and channel-policy constraints. It is then designed, implemented and tested only through an approved LeadsHug contract and TODO.

## Future retirement

This policy neither freezes nor archives the repositories and does not assert their deployed health. A future retirement, freeze, archive, ownership transfer or deployment change is a user-approved operational decision. ADR-0013 remains the governing LeadsHug boundary: the new product does not synchronize with or use the legacy environment as rollback.

## Senior technical review

Claude Code reviewed this policy, the boundary matrix and its governing TODO on 2026-09-15 (session `357ef8b5-be34-438b-be56-5162d6d90299`). Verdict: `no_material_findings`. The review confirmed that the policy retains Central-Whatsapp for inspiration while explicitly withholding archive, freeze, deployment, copying, synchronization and ownership authority.
