# PACED Subagent Dispatch: test_quality_audit

## Dispatch Identity
- **Artifact kind:** `subagent_review_dispatch`
- **Authoritative:** `false`
- **Edit policy:** `derived_dispatch_packet`
- **Review kind:** `test_quality_audit`
- **Bounded package:** `foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/candidate-audit-r6/round-04/round-package.md`
- **Reviewer count:** `1`
- **No-context required:** `true`

## Required Axes
- `test_effectiveness`
- `test_efficiency`
- `performance`
- `structural_soundness`
- `operational_fit`

## Focus Points
- Verify whether changed tests reflect real behavior/contract change or only pass-the-test repair.
- Assess whether assertions are effective and efficient.
- State whether the audit sees brittle test-only shortcuts or weak coverage.
- For each material finding, add category and formalizable-hint when you can judge them honestly.
- When assessing design, seek the simplest faithful Clean Code/SOLID design for the approved intent. Do not invent future-facing work or erase explicit TODO intent. Planning review may challenge proposed intent; delivery review must preserve approved intent or return for renewed approval.

## Required Result Fields
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings[].finding_id (optional)`
- `findings[].category (optional)`
- `findings[].formalizable_hint (optional)`
- `findings[].candidate_rule_level (optional)`
- `findings[]`

## Required Result Binding
The reviewer result's `dispatch_path` must equal this exact dispatch JSON path:
`/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r35-test-quality-complete.dispatch.json`
Do not substitute the bounded package path, governing TODO path, or reviewer output path.

## Goal
Complete affected independent TQA with ALL embedded method/skill outputs. The output must be substantive, not a terse zero-finding verdict. Put structured sections inside overall_assessment (JSON string) to respect the strict schema: (1) capabilities/critical journeys/compatibility scope, (2) exact owning commands and topology, (3) coverage/evidence matrix plus exclusions and platform status passed/blocked/failed/flaky, (4) original test-after/unknown versus actual r31-r34 causal RED and capture/oracle limits, (5) explicit answers to ALL FIVE mandatory audit questions, (6) skip/focus/bypass/auth/fallback/DI token-scope-lifecycle parity/CI parity/source-served checks, (7) decision-by-decision adherence TABLE D01-D09, CR-01/02, AR-V11-01/02/03, CR-V11-01 with evidence, (8) uncertainty/residual limits and gate readiness. Assess full changed code/test/diffs and negative gates, including common failure flag removal and unchanged recovered DOM oracle; distinguish real PostgreSQL/BFF from external provider fixtures and actual pending Meta. Do not claim tool reproduction. If an applicable required output cannot be established, state it clearly. Concrete material issue cards require path:line, severity, why-now, A/B/C and recommendation using allowed finding fields. Prior unchanged accepted design/debt remains carried; zero unresolved BLOCKING is the objective, not cosmetic zero findings. This is output-completeness supplementation to the terse first current TQA; no source change or suite rerun occurred. Full applicable workload remains required.

## Related TODO
`foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md`

Reviewers must cross-check findings against the governing TODO's explicit decisions, approved exceptions, compatibility mandates, and non-goals before classifying something as blocking drift.

## Historical Finding Carry-Forward
Previously adjudicated findings are historical context, not automatic reopening triggers.
- Resolved findings are historical context only. Do not reopen them unless the current bounded package materially changes the same locus/behavior or fresh evidence shows regression.
- Challenged findings stay closed unless the current bounded package materially changes the same locus/behavior or the prior rationale is objectively insufficient.
- Deferred findings must cite the recorded follow-up/waiver path first. Re-raise them only when the current bounded package changes the same locus or closure now depends on that deferred risk.
- Unresolved findings remain valid to re-raise until they are fixed, challenged, or formally deferred with authority.

## Result Contract
Return exactly one JSON object and no Markdown fence or prose.
Do not emit `null`; omit optional fields that do not apply.
No top-level fields other than the following are allowed:
- `schema_version`: `subagent-review-result-v1`
- `artifact_kind`: `subagent_review_result`
- `dispatch_path`: the exact binding shown above
- `review_kind`: `test_quality_audit`
- `reviewer_label`
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings`

Every `*_position` value must be one of: `strong_positive`, `acceptable`, `mixed`, `regresses`, `unknown`, `not_evaluated`.
Each finding may contain only these fields:
- required: `severity`, `title`, `rationale`, `suggested_action`
- optional: `finding_id`, `category`, `formalizable_hint`, `candidate_rule_level`, `candidate_rule_id`, `affected_paths`
- `severity` values: `low`, `medium`, `high`
- `category` values: `architecture`, `adherence`, `tests`, `performance`, `security`, `elegance`, `structural_soundness`, `operational_fit`, `residual_risk`, `other`
- `formalizable_hint` values: `yes`, `partial`, `no`, `unknown`
- `candidate_rule_level` values: `paced`, `project`, `none`, `unknown`

