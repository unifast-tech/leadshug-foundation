# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence114f-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Repair both gaps within this TODO and obtain current native regression evidence, followed by canonical ALL validation. Preserve historical closures and keep the recorded primary-protocol, browser, CP5 assurance and separately approved CP6 physical-proof obligations open.`

## Merged Findings
### F-A46C8045 [medium] The successor UPDATE remains lazy while its waiter is observed
- **Reviewers:** fresh-no-context-adherence114f
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Start the real UPDATE immediately by attaching a handled promise continuation before polling. Preserve the queued PostgreSQL update, exact-token assertions and unconditional cleanup, then execute the expiry, successor and live-control cases.
- **Rationale:** The new verification test assigns prisma.$executeRaw directly to successorUpdate, then awaits waitForResourceWaiter(..., 'UPDATE'). $executeRaw returns a lazy PrismaPromise; assignment does not execute it. Its first consumption occurs after the waiter assertion or in finally, which releases the COMMIT barrier first. The intended queued successor therefore cannot be observed, and this branch cannot prove successor preservation required by IG-ADHERENCE111A-01.

### F-154196BB [medium] Cancellation still hides a completed account's proven label
- **Reviewers:** fresh-no-context-adherence114f
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Preserve completed mapped label evidence through permitted cancellation using the exact BU, channel, immutable resource and app-scope checks. Add native catalog/list/thread coverage for cancellation after confirmation, including multiple distinguishable accounts and unchanged readiness.
- **Rationale:** cancel accepts MAPPED_PENDING_SUBSCRIPTION and MAPPED_PENDING_RECEIPT even when confirmationState is COMPLETED. It changes status to CANCELLED while retaining the mapped resource and active credential. Both display queries require the completed attempt's status to remain one of those two mapped states. Cancelling an account's sole completed attempt therefore replaces its known username with generic Instagram labels despite retained ownership and proof. This is a residual gap in A03's last-proven-label requirement under SCOPE-07/DOD-06.

## Reviewer Summaries
### fresh-no-context-adherence114f
- **Assessment:** changes_required: The enclosed acquisition cleanup and UUID module admission align with the approved architecture. Two material gaps remain: the successor regression does not start its database contender before observing it, and completed-attempt cancellation still removes retained account labels. These are static findings; no execution or hash verification is claimed.
- **Recommended path:** `Repair both gaps within this TODO and obtain current native regression evidence, followed by canonical ALL validation. Preserve historical closures and keep the recorded primary-protocol, browser, CP5 assurance and separately approved CP6 physical-proof obligations open.`
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-ADHERENCE114F-01 The successor UPDATE remains lazy while its waiter is observed: The new verification test assigns prisma.$executeRaw directly to successorUpdate, then awaits waitForResourceWaiter(..., 'UPDATE'). $executeRaw returns a lazy PrismaPromise; assignment does not execute it. Its first consumption occurs after the waiter assertion or in finally, which releases the COMMIT barrier first. The intended queued successor therefore cannot be observed, and this branch cannot prove successor preservation required by IG-ADHERENCE111A-01.
  - [medium] IG-ADHERENCE114F-02 Cancellation still hides a completed account's proven label: cancel accepts MAPPED_PENDING_SUBSCRIPTION and MAPPED_PENDING_RECEIPT even when confirmationState is COMPLETED. It changes status to CANCELLED while retaining the mapped resource and active credential. Both display queries require the completed attempt's status to remain one of those two mapped states. Cancelling an account's sole completed attempt therefore replaces its known username with generic Instagram labels despite retained ownership and proof. This is a residual gap in A03's last-proven-label requirement under SCOPE-07/DOD-06.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
