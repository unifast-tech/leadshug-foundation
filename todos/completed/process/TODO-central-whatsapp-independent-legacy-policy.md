# TODO — Central-Whatsapp: independent legacy policy

## Approval

- **Approved by:** `Gabriel / user — 2026-09-15 — "Vamos formalizá-lo como legado"`
- **Approval scope:** formally classify `Central-Whatsapp/api-oficial` and `Central-Whatsapp/hub-whatsapp` as independent legacy repositories retained for behavioral and operational inspiration while LeadsHug is the sole target architecture; do not archive, delete, freeze, deploy, alter source code or change repository permissions.
- **Renewed approval required when:** an archive/freeze action, deployment/runtime change, code change in a legacy repository, data migration, cutover, or ownership transfer is proposed.

## Scope

- [x] Create the canonical Foundation policy defining permitted and prohibited use of Central-Whatsapp as independent legacy reference repositories.
- [x] Reconcile the architecture-boundary matrix with the approved policy and record the remaining retirement decision explicitly.
- [x] Preserve the user-only authority over a future freeze, archive or retirement event.

## Definition of Done

- [x] Central-Whatsapp is explicitly classified as independent legacy/reference, not a LeadsHug dependency or implementation source.
- [x] The policy permits requirements and operational lessons while prohibiting code/database/deployment synchronization or copying.
- [x] The completed evidence states that no operational or repository state was changed.

## Validation Steps

- [x] Review policy and matrix against the approved user decision and ADR-0013 boundary.
- [x] Run `git diff --check` and the Codex–Claude delivery guard after a read-only Claude review.

## Codex–Claude Delivery Cycle

- **User approval evidence:** `Gabriel / user — 2026-09-15 — "Vamos formalizá-lo como legado msm pq tiraremos inspirações do Central-Whatsapp".`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `completed`
- **Claude final review status:** `no_material_findings`
- **Claude final review evidence:** `Claude Code read-only review session 357ef8b5-be34-438b-be56-5162d6d90299 on 2026-09-15; policy review recorded in policies/central_whatsapp_independent_legacy_policy.md.`
- **Material findings disposition:** `No material findings. The policy correctly preserves ADR-0013 and explicitly gates archive, freeze, deployment, code copying, synchronization and ownership changes behind renewed user approval.`
- **Continuity rule:** `Continue local documentation and review-driven repairs without pausing.`
- **Escalate to user only if:** `a freeze, archive, deployment, code, data, repository-permission, cutover or ownership change is proposed.`
