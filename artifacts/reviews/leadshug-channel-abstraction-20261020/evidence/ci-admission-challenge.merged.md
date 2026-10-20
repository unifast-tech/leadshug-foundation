# PACED Subagent Review Merge: architecture_opinion

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/ci-admission-challenge.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `strong_positive`
- **Operational fit:** `mixed`

## Recommended Paths
- `Choose narrowly approved CI admission using the existing canonical leaf-command family. Prepare a concrete, path-enumerated TODO amendment for .github/workflows/ci.yml and necessary contract/drift-guard support, and obtain renewed approval before implementation. Preserve the Windows local all runner; specify concrete isolated Node 22/PostgreSQL 16, migration/bootstrap, API/provider, production-bundle Chromium, freshness and cleanup orchestration for Linux CI using the same suites and ordered lifecycle. This costs configuration and topology maintenance but avoids an unnecessary cross-platform runner rewrite. Validate the executable topology locally, run the evidence invalidation guard, and rerun the authoritative broad local contract as required by admission. Record configuration, local parity, actual remote execution and promotion separately. Assign later remote execution to an explicit CI/promotion owner and leave it not_run until authorized source publication and execution occur. Complete the full fresh independent TQA after remediation. This opinion authorizes no edits, push, deploy, gitlink change or waiver.`

## Merged Findings
### F-2CAFC241 [high] Changed CI-equivalent test surfaces lack corresponding pipeline admission
- **Reviewers:** fresh-no-context-ci-admission-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Integrate this portion of TQA-01 as a current admission blocker. Obtain renewed approval for the smallest concrete configuration and guard amendment, align suite membership and lifecycle ownership, and collect the required authoritative local evidence. If expansion is declined, retain the blocker; a promotion follow-up ticket alone does not satisfy the current admission rule.
- **Rationale:** The admission skill explicitly forbids adding tests only to a local wrapper while leaving the pipeline on different leaf commands, and requires corresponding stage-surface and drift-guard updates in the same change. TODO SCOPE-05, DOD-06, D10 and its local matrix include the changed PG/browser protections in the required CI-equivalent all surface. The supplied workflow executes only build/unit surfaces. No approved exception removes these admission obligations. Conversely, the approved diff paths contain no CI workflow or admission-guard expansion, so the reviewer cannot authorize the necessary edits. The mismatch blocks completion of the admission/parity claim; it does not erase the reported all80903 local results.

### F-765A9380 [medium] TQA-01 conflates pipeline admission with remote execution and audit waiver
- **Reviewers:** fresh-no-context-ci-admission-reviewer
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `paced`
- **Candidate rule id:** `n/a`
- **Suggested action:** Challenge the implication that missing remote execution necessarily requires a TQA waiver for local completion. Preserve the valid configuration finding, record remote execution as a separately owned later obligation, and prohibit remote-success or promotion claims without actual evidence. Do not invoke the Windows-dependent all runner directly on Ubuntu or accept YAML alone as topology proof. Obtain the complete independent TQA after remediation; this architecture opinion cannot satisfy or waive that gate.
- **Rationale:** CI-equivalent governance defines CI Equivalent as current-authoritative-branch local proof and treats published-lane evidence separately. Admission requires aligned configuration and an authoritative local rerun when applicable; it does not require a successful remote run before this local milestone. The TODO explicitly excludes product push/deploy and makes promotion a later obligation. Thus all80903 supports its frozen local execution claim, while configuration alignment and remote execution remain separate facts. A workflow edit alone proves neither executable Linux topology nor remote success. The package also records an incomplete full-workload TQA, which remains independently unsatisfied regardless of this adjudication.

## Reviewer Summaries
### fresh-no-context-ci-admission-reviewer
- **Assessment:** Changes required for admission. TQA-01 is partially sustained: the changed stage-facing PG/browser family requires corresponding pipeline configuration and drift protection in this change. It is not merely a future promotion obligation. However, successful remote execution is not a stated prerequisite of the approved local-only milestone, and its absence does not itself require a TQA waiver. Local-only scope restricts implementation authority; it does not waive mandatory admission rules. The recommended path improves elegance and structural soundness through shared command ownership, leaves product runtime performance unchanged, and adds CI execution and maintenance cost. PERF-01 and the remaining delivery gates remain independently open.
- **Recommended path:** `Choose narrowly approved CI admission using the existing canonical leaf-command family. Prepare a concrete, path-enumerated TODO amendment for .github/workflows/ci.yml and necessary contract/drift-guard support, and obtain renewed approval before implementation. Preserve the Windows local all runner; specify concrete isolated Node 22/PostgreSQL 16, migration/bootstrap, API/provider, production-bundle Chromium, freshness and cleanup orchestration for Linux CI using the same suites and ordered lifecycle. This costs configuration and topology maintenance but avoids an unnecessary cross-platform runner rewrite. Validate the executable topology locally, run the evidence invalidation guard, and rerun the authoritative broad local contract as required by admission. Record configuration, local parity, actual remote execution and promotion separately. Assign later remote execution to an explicit CI/promotion owner and leave it not_run until authorized source publication and execution occur. Complete the full fresh independent TQA after remediation. This opinion authorizes no edits, push, deploy, gitlink change or waiver.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `strong_positive`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] CIADM-01 Changed CI-equivalent test surfaces lack corresponding pipeline admission: The admission skill explicitly forbids adding tests only to a local wrapper while leaving the pipeline on different leaf commands, and requires corresponding stage-surface and drift-guard updates in the same change. TODO SCOPE-05, DOD-06, D10 and its local matrix include the changed PG/browser protections in the required CI-equivalent all surface. The supplied workflow executes only build/unit surfaces. No approved exception removes these admission obligations. Conversely, the approved diff paths contain no CI workflow or admission-guard expansion, so the reviewer cannot authorize the necessary edits. The mismatch blocks completion of the admission/parity claim; it does not erase the reported all80903 local results.
  - [medium] CIADM-02 TQA-01 conflates pipeline admission with remote execution and audit waiver: CI-equivalent governance defines CI Equivalent as current-authoritative-branch local proof and treats published-lane evidence separately. Admission requires aligned configuration and an authoritative local rerun when applicable; it does not require a successful remote run before this local milestone. The TODO explicitly excludes product push/deploy and makes promotion a later obligation. Thus all80903 supports its frozen local execution claim, while configuration alignment and remote execution remain separate facts. A workflow edit alone proves neither executable Linux topology nor remote success. The package also records an incomplete full-workload TQA, which remains independently unsatisfied regardless of this adjudication.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
