# TODO — LeadsHug: system analysis and modernization plan

## Approval

- **Approved by:** `Gabriel / user — 2026-09-15 — APROVADO`
- **Approval scope:** read-only technical and product analysis of the current `LeadsHug` system, its governing authorities, `Central-Whatsapp`, and `whatsflow_v2`; produce an evidence-based modernization plan and proposed tactical implementation TODOs.
- **Renewed approval required when:** implementation would change product code, database schema, deployed infrastructure, credentials, external services, or the approved system architecture.

## Scope

- [x] Inventory current LeadsHug architecture, module boundaries, runtime/deployment assumptions, documentation, tests, and known debt.
- [x] Compare the active product to Foundation contracts and Engineering rules, identifying contradictions, stale records, and ungoverned areas.
- [x] Extract reusable capabilities and failure lessons from Central-Whatsapp and whatsflow_v2 without copying their legacy architecture into LeadsHug.
- [x] Rank findings by impact, urgency, dependency, and implementation risk; propose the smallest safe execution sequence.
- [x] Record the report and proposed follow-up TODOs in Foundation; do not implement product changes in this analysis cycle.

## Definition of Done

- [x] The report distinguishes verified current behavior from documentation claims and from reference-system ideas.
- [x] The report maps the core, integration/channel, CRM, campaign, security/tenancy, and operations concerns.
- [x] Each recommended next step is bounded, ordered, and states its required decision or evidence.
- [x] The user receives a concise decision-ready synthesis before any implementation TODO is opened for execution.

## Validation Steps

- [x] Read repository metadata, package manifests, architecture and contract documents, schema/migrations, service boundaries, and test/deployment configuration without changing them.
- [x] Verify each important finding against code or authoritative documentation, not only legacy documentation.
- [x] Check the analysis report for internal consistency and run `git diff --check` for Foundation artifacts.

## Codex–Claude Delivery Cycle

- **User approval evidence:** `Gabriel / user — 2026-09-15 — APROVADO.`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `completed`
- **Claude final review status:** `no_material_findings`
- **Claude final review evidence:** `Claude Code read-only review session db8c3f1e-7821-41e2-a788-e3435374905a on 2026-09-15; recorded in artifacts/analysis/leadshug-system-analysis-20260915.md.`
- **Material findings disposition:** `No material findings. Two non-blocking governance confirmations (ADR-0001 legacy divergence and stale Foundation delphi-ai authority references) were incorporated into the analysis report.`
- **Continuity rule:** `Continue local analysis, evidence collection and review-driven report repairs without pausing.`
- **Escalate to user only if:** `a conclusion requires a product, commercial, privacy, architecture, infrastructure or delivery-priority decision.`
