# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence113f-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `The E01–E06 corrections are supported statically. Complete the remaining E07 protection in the admitted CP5 spec, then obtain frozen canonical ALL and actual six-case CP5 evidence. Source113a has not executed, and ALL112 stopped at lint. Preserve the recorded primary-protocol, complete consumer/browser, assurance and CP6 obligations; this focused review grants no checkpoint or feature acceptance.`

## Merged Findings
### F-CB7FD86B [medium] Whole-cohort scans can still satisfy the revised index oracle
- **Reviewers:** fresh_no_context_adherence113f
- **Category:** `performance`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Retain E07 as open. Distinguish the main route access from the lateral count access and validate the relevant access predicates, index usage and scan work, including loops and rows removed, for the large route/peer cohort. Continue allowing justified sequential scans of the small owner cohort. Preserve existing latency thresholds and the list-only eight-query cap; do not force planner settings or introduce unrelated numeric gates. Validate the resulting assertions against actual canonical execution.
- **Rationale:** The revised EPS case captures genuine SQL, parameters and qualifying index definitions, but its scan assertions still permit the original incidental-index weakness. routeScans.some can be satisfied by the indexed rr route-count lateral subquery while the main r lookup scans the retained cohort. Actual Rows measures emitted rows per loop: a scan filtering 20000 rows down to one or fifty can satisfy every <=50 assertion, and the reply-options root Actual Rows=1 checks have the same limitation. Rows removed, loop counts and the identity of the main access node are not checked. Consequently, the harness can pass a whole-cohort route or peer scan despite the approved bounded-query/index protection. This is a protection-harness gap, not evidence that current runtime plans regress.

## Reviewer Summaries
### fresh_no_context_adherence113f
- **Assessment:** changes_required
- **Recommended path:** `The E01–E06 corrections are supported statically. Complete the remaining E07 protection in the admitted CP5 spec, then obtain frozen canonical ALL and actual six-case CP5 evidence. Source113a has not executed, and ALL112 stopped at lint. Preserve the recorded primary-protocol, complete consumer/browser, assurance and CP6 obligations; this focused review grants no checkpoint or feature acceptance.`
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-CP5-111E-07 Whole-cohort scans can still satisfy the revised index oracle: The revised EPS case captures genuine SQL, parameters and qualifying index definitions, but its scan assertions still permit the original incidental-index weakness. routeScans.some can be satisfied by the indexed rr route-count lateral subquery while the main r lookup scans the retained cohort. Actual Rows measures emitted rows per loop: a scan filtering 20000 rows down to one or fifty can satisfy every <=50 assertion, and the reply-options root Actual Rows=1 checks have the same limitation. Rows removed, loop counts and the identity of the main access node are not checked. Consequently, the harness can pass a whole-cohort route or peer scan despite the approved bounded-query/index protection. This is a protection-harness gap, not evidence that current runtime plans regress.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
