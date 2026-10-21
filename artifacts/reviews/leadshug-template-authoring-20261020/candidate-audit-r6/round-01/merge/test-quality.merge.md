# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/candidate-audit-r6/round-01/dispatch/test-quality.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `return_for_resolution`

## Merged Findings
### F-52E9D4E7 [high] FRC browser probe permits the exact provider-call amplification it is meant to prevent
- **Reviewers:** fresh-no-context-test-quality-reviewer
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: assert the deterministic expected effect count for the uninterrupted 5×20 burst (currently 1), plus safe outcomes for blocked refreshes; recommended. B: split batches with an explicit documented timing model and assert the exact allowed effect count per batch. C: retain the <=100 assertion; this leaves the required anti-amplification behavior unprotected.
- **Rationale:** `web-app/e2e/message-templates.spec.ts` records 100 rapid catalog-refresh triggers but accepts any provider-list effect count from 1 through 100. The observed run happened to produce 1, yet a regression that lets every trigger reach Meta would still pass. This does not effectively protect D07's shared lease/debounce contract.

### F-BEB97992 [high] Changed-account explicit-copy journey lacks real BFF/browser coverage
- **Reviewers:** fresh-no-context-test-quality-reviewer
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: add a real BFF/Playwright scenario that creates a draft, changes account context through an approved normal setup path, observes the safe block, and copies the authorized historical definition into a new current-context draft; recommended. B: provide an approved, non-product-route fixture mechanism that changes the durable context while preserving the same BFF/browser boundary. C: accept compositional evidence only; this leaves D04's user-facing recovery contract unproven.
- **Rationale:** D04 requires that an account change blocks the historical draft with `CONTA_ALTERADA` and permits an explicit new copy. `api-app/test/message-template-management.e2e-spec.ts` proves the backend rejection, while `web-app/e2e/message-templates.spec.ts` proves copy/reload for same-account correlated recovery. The package explicitly acknowledges that no changed-account browser flow is retained; static UI mapping is not a substitute for validating this user-visible integration path.

### F-BE7A6592 [medium] Test-first claim is not supported by retained fail-first evidence
- **Reviewers:** fresh-no-context-test-quality-reviewer
- **Category:** `tests`
- **Formalizable hint:** `no`
- **Candidate rule level:** `none`
- **Candidate rule id:** `n/a`
- **Suggested action:** Record the delivery as test-after/unknown in the governing evidence and do not represent it as test-first. For future behavior-defining changes, retain the failing behavioral target before implementation. Do not manufacture retrospective RED evidence.
- **Rationale:** The package candidly records that primary feature tests were authored during implementation and that not all behavioral RED evidence was retained, despite the TODO declaring a test-first strategy. Final green real-PostgreSQL and browser evidence is strong, but this remains test-after/unknown rather than demonstrated test-first alignment.

## Reviewer Summaries
### fresh-no-context-test-quality-reviewer
- **Assessment:** blocking_findings
- **Recommended path:** `return_for_resolution`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] TQA-ST05-01 FRC browser probe permits the exact provider-call amplification it is meant to prevent: `web-app/e2e/message-templates.spec.ts` records 100 rapid catalog-refresh triggers but accepts any provider-list effect count from 1 through 100. The observed run happened to produce 1, yet a regression that lets every trigger reach Meta would still pass. This does not effectively protect D07's shared lease/debounce contract.
  - [high] TQA-ST05-02 Changed-account explicit-copy journey lacks real BFF/browser coverage: D04 requires that an account change blocks the historical draft with `CONTA_ALTERADA` and permits an explicit new copy. `api-app/test/message-template-management.e2e-spec.ts` proves the backend rejection, while `web-app/e2e/message-templates.spec.ts` proves copy/reload for same-account correlated recovery. The package explicitly acknowledges that no changed-account browser flow is retained; static UI mapping is not a substitute for validating this user-visible integration path.
  - [medium] TQA-ST05-03 Test-first claim is not supported by retained fail-first evidence: The package candidly records that primary feature tests were authored during implementation and that not all behavioral RED evidence was retained, despite the TODO declaring a test-first strategy. Final green real-PostgreSQL and browser evidence is strong, but this remains test-after/unknown rather than demonstrated test-first alignment.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
