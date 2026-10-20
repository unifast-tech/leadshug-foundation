# PACED Subagent Review Merge: architecture_opinion

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/scope-renewal-v1.3-architecture.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `strong_positive`
- **Structural soundness:** `strong_positive`
- **Operational fit:** `mixed`

## Recommended Paths
- `Choose the single Prisma-managed composite index plus selected-window-only projection, and extend host transport selection around the existing all/RUNNER_SCRIPT lifecycle. The managed index is preferable here to the viable partial-index alternative because schema and migration ownership remain explicit; its principal tradeoff is indexing OUT rows as well as IN rows. The shared runner is preferable to a separately duplicated Linux CI lifecycle because suites, ordering, fixtures, freshness and cleanup retain one executable owner; its tradeoff is transport-specific path and Docker-engine validation. The admitted paths suffice for this design. Freeze the guard invocation and enforcement boundary, accurately describe nonconcurrent migration locking, then complete the planning gates and request renewed approval. Require successful isolated Linux execution before local delivery; YAML inspection alone establishes configuration only.`

## Merged Findings
### F-8789F18E [medium] Nonconcurrent index locking is not necessarily brief
- **Reviewers:** fresh-internal-no-context-architecture-reviewer
- **Category:** `operational_fit`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Describe locking as lasting for the complete build, with duration dependent on the preserved table and concurrent activity. Define the local migration owner's permitted interruption and finite lock-wait/build limits, and validate representative locking and failure behavior on disposable PostgreSQL before activation. Keep the single approved CREATE INDEX and the stated stop-on-failure, data-preserving recovery boundary.
- **Rationale:** The exact migration uses ordinary CREATE INDEX, which blocks table writes for the duration of the index build and can first wait for conflicting transactions. The proposal acknowledges write locking but repeatedly characterizes it as brief without a measured duration or execution budget. Increasing-history read-plan proof does not establish the duration or operational impact of building the index on the preserved local database. This affects the interruption risk presented for renewed approval.

### F-D4A7CE68 [medium] Freeze the parity guard invocation and enforcement boundary
- **Reviewers:** fresh-internal-no-context-architecture-reviewer
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Specify the guard command and call site after its container prerequisites and before product execution, with failure propagated through the wrapper and cleanup. State whether missing-job protection is enforced by mandatory local admission or independently in CI. If independent CI enforcement is intended, specify its invocation from a retained workflow job using the already admitted workflow and guard paths. Include meaningful missing-job and skipped-invocation controls for the enforcement boundary actually claimed.
- **Rationale:** D10 and the proposal require the guard to fail before product suites, but the representative workflow invokes only all, and the proposal does not explicitly place the guard call within the wrapper or RUNNER_SCRIPT. Python/YAML installation is planned inside the container, which matters to that placement. Also, a guard reached exclusively through channels-validation cannot itself enforce remote failure when that entire job is deleted or skipped. Mandatory local admission can detect such drift, but that enforcement boundary should be explicit. This is an execution-contract ambiguity rather than a demonstrated implementation failure.

## Reviewer Summaries
### fresh-internal-no-context-architecture-reviewer
- **Assessment:** The architectural direction is sound and suitable for renewed human approval after the two planning clarifications below and the remaining critique/approval guards converge. The proposed composite index matches both latest-IN query shapes: conversation and direction equality followed by backward traversal of createdAt/id. It preserves expired timestamps, cross-transport history and existing acceptance ownership. Selected-window filtering addresses the separate unnecessary-query case. Shared lifecycle ownership improves elegance and structural soundness; expected read improvements carry additional index storage/write cost and CI execution cost. PERF-01 and CIADM-01 remain open delivery blockers. Required delivery evidence includes disposable migration/status, representative PostgreSQL plans and write costs, guard negative controls, executable Linux transport rehearsal, invalidation and final authoritative all, refreshed PCV and full independent audits, followed by authorized local activation and assisted IN/OUT. Actual remote execution remains separately owned and not_run until authorized publication; this opinion grants no execution or delivery authority.
- **Recommended path:** `Choose the single Prisma-managed composite index plus selected-window-only projection, and extend host transport selection around the existing all/RUNNER_SCRIPT lifecycle. The managed index is preferable here to the viable partial-index alternative because schema and migration ownership remain explicit; its principal tradeoff is indexing OUT rows as well as IN rows. The shared runner is preferable to a separately duplicated Linux CI lifecycle because suites, ordering, fixtures, freshness and cleanup retain one executable owner; its tradeoff is transport-specific path and Docker-engine validation. The admitted paths suffice for this design. Freeze the guard invocation and enforcement boundary, accurately describe nonconcurrent migration locking, then complete the planning gates and request renewed approval. Require successful isolated Linux execution before local delivery; YAML inspection alone establishes configuration only.`
- **Performance:** `mixed`
- **Elegance:** `strong_positive`
- **Structural soundness:** `strong_positive`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] ARCH13-01 Freeze the parity guard invocation and enforcement boundary: D10 and the proposal require the guard to fail before product suites, but the representative workflow invokes only all, and the proposal does not explicitly place the guard call within the wrapper or RUNNER_SCRIPT. Python/YAML installation is planned inside the container, which matters to that placement. Also, a guard reached exclusively through channels-validation cannot itself enforce remote failure when that entire job is deleted or skipped. Mandatory local admission can detect such drift, but that enforcement boundary should be explicit. This is an execution-contract ambiguity rather than a demonstrated implementation failure.
  - [medium] ARCH13-02 Nonconcurrent index locking is not necessarily brief: The exact migration uses ordinary CREATE INDEX, which blocks table writes for the duration of the index build and can first wait for conflicting transactions. The proposal acknowledges write locking but repeatedly characterizes it as brief without a measured duration or execution budget. Increasing-history read-plan proof does not establish the duration or operational impact of building the index on the preserved local database. This affects the interruption risk presented for renewed approval.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

