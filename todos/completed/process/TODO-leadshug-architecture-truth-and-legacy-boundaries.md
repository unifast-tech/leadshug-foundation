# TODO — LeadsHug: architecture truth and legacy boundaries

## Approval

- **Approved by:** `Gabriel / user — 2026-09-15 — APROVADO`
- **Approval scope:** reconcile the documented current architecture and define ownership, runtime, freeze, cutover and extraction boundaries for the embedded legacy trees and `Central-Whatsapp`, without modifying, moving, deleting or deploying any legacy or product code.
- **Renewed approval required when:** a conclusion requires changing runtime ownership, deployment, code, database, infrastructure, a remote repository, credentials, cutover execution, or an architecture decision.

## Scope

- [x] Inventory each active and legacy tree's repository identity, current branch/head, runtime/deployment evidence, and relation to LeadsHug.
- [x] Reconcile the current-state portions of product documentation with verified code and approved ADRs, preserving historical documents as historical records.
- [x] Define a canonical compatibility/retirement matrix: authority, runtime owner, mutation status, cutover condition, and allowed extraction method per tree.
- [x] Define a safe procedure for borrowing a legacy capability without copying implementation or bypassing LeadsHug contracts.
- [x] Record unresolved decisions explicitly; do not make cutover or implementation decisions in this cycle.

## Definition of Done

- [x] One Foundation artifact is the navigation point for the verified architecture and legacy-boundary matrix.
- [x] Every analyzed tree has an explicit status and permitted use.
- [x] Documentation distinguishes current target architecture, active parallel runtime, frozen embedded snapshot, and reference-only system.
- [x] The user receives decision-ready options for any remaining ownership or cutover choice.

## Validation Steps

- [x] Verify repository identity and history, package/deployment manifests, product ADRs and references without changing their working trees.
- [x] Validate the artifact's claims against direct local evidence and run `git diff --check` for Foundation changes.
- [x] Submit the final artifact to a read-only Claude Code review and run the Codex–Claude delivery guard.

## Codex–Claude Delivery Cycle

- **User approval evidence:** `Gabriel / user — 2026-09-15 — APROVADO.`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `completed`
- **Claude final review status:** `no_material_findings`
- **Claude final review evidence:** `Claude Code read-only review session fc781c38-0000-44ea-8603-45e5ae195e4c on 2026-09-15; recorded in artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md.`
- **Material findings disposition:** `No material findings. The reviewer independently verified Git identity/head evidence and the relevant ADR interpretations; one non-material Foundation contracts-directory observation is documented in the artifact.`
- **Continuity rule:** `Continue local analysis, documentation and review-driven repairs without pausing.`
- **Escalate to user only if:** `a runtime, deployment, repository, architecture, data or cutover decision becomes necessary.`
