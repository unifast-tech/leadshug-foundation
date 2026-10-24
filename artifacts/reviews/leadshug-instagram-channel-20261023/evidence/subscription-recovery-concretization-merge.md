# PACED Subagent Review Merge: architecture_opinion

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/subscription-recovery-concretization-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `strong_positive`
- **Structural soundness:** `strong_positive`
- **Operational fit:** `mixed`

## Recommended Paths
- `Implement and source-review the durable first-dispatch fence, documented success handling, explicit advance boundary, and narrow subscription observer now. Persist dispatch intent before HTTP and conservatively retain uncertainty after any possibly dispatched mutation whose outcome was not durably established. Preserve that fence across authorization attempts for the same resource. Model observation as own-confirmed, conclusively-absent, or UNKNOWN; until the GET contract is established, do not invent parsing, identity comparisons, or absence evidence. UNKNOWN preserves pending and permits no further subscription mutation. Keep the actual own-account-read obligation explicitly incomplete where its protocol is unavailable. Establish GET support, response envelope, own-app identification, visibility and completeness semantics before accepting that obligation or enabling absence-based repeat POST. Continue independent CP3 work without changing the remaining checkpoint requirements. The main tradeoff is reduced automatic progress after uncertainty in exchange for truthful state and prevention of unsupported repeat mutation. A narrow state machine improves elegance and structural soundness; request limits keep performance acceptable without a measured throughput claim.`

## Merged Findings
### F-D74DFFA8 [high] The uncertainty fence must belong to the resource lifecycle
- **Reviewers:** instagram_subscription_recovery_opinion
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Preserve dispatch history and uncertainty across attempts for the same verified resource. Permit the first POST only with durable evidence that no prior dispatch is recorded. After uncertainty, permit another POST only through a fresh authorized claim supported by primary-established conclusive own absence. Keep HTTP outside transactions and retain existing lease, authorization, ownership, budget, cooldown and receipt gates.
- **Rationale:** A new attempt, reauthorization, expired lease, or crash cannot prove that an earlier subscription POST did not reach Meta. A durable dispatch claim provides an at-most-once local dispatch policy, not an exactly-once provider outcome. Recording intent before HTTP can leave an operation uncertain even when a crash prevented transmission; that conservative loss of progress is consistent with the proposed no-repeat rule. A documented success:true confirms the subscription request but still does not replace the required authenticated ingress receipt.

### F-1057FD45 [high] The primary GET contract remains an acceptance prerequisite
- **Reviewers:** instagram_subscription_recovery_opinion
- **Category:** `architecture`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Carry IG-SUBPROTO-01 forward explicitly through independent CP3 work. Require the supported observation contract and corresponding implementation proof before recovery-criterion acceptance and final delivery. Keep all CP2 obligations and CP4 through CP6 requirements intact.
- **Rationale:** The bounded package expressly retains this finding as open. The documented POST does not establish GET support, response shape, own-app identity, visibility, pagination completeness, or when an empty result proves absence. Conservative UNKNOWN handling preserves safety while these facts are missing, but does not close the unresolved observation requirement. Neither omission from documentation nor an installation-specific response establishes the missing universal contract.

### F-071FE5E2 [medium] UNKNOWN is a valid recovery outcome, but does not erase the read obligation
- **Reviewers:** instagram_subscription_recovery_opinion
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Retain the explicit advance observation boundary and typed UNKNOWN outcome. If the protocol is unavailable, report that limitation truthfully and keep the observation criterion open instead of issuing guessed requests or treating a no-op as a completed read. Once supported, perform only the bounded own-account observation within the approved request, timeout and lease limits; never inspect or mutate other-app subscriptions.
- **Rationale:** Nothing in the approved clauses guarantees eventual automatic success after every uncertain mutation. Honest durable pending is therefore valid when evidence remains inconclusive. However, a handler that permanently returns UNKNOWN without an implemented supported observation path cannot be accepted as delivery of the explicit own-account-read requirement. Avoiding a speculative GET is a reasonable interim safety choice; claiming that this completes recovery would dilute approved scope.

### F-2850A6AF [medium] The proposed two-GET investigation provides bounded empirical evidence
- **Reviewers:** instagram_subscription_recovery_opinion
- **Category:** `operational_fit`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `none`
- **Candidate rule id:** `n/a`
- **Suggested action:** Treat the plan solely as a separately authorized operator investigation: at most the two proposed GETs, an already eligible token, the stated host and version, no retries or additional credential acquisition, and stop if prerequisites are unavailable. Report only the proposed sanitized classifications, allowing multiple local identity matches where applicable. Use results to refine the primary-contract question, not to clear the uncertainty fence or close IG-SUBPROTO-01. This opinion grants no execution authority.
- **Rationale:** The proposed operator sequence can materially clarify whether the selected installation accepts the requested endpoint and fields, what response shape and paging markers appear, and which locally known identifiers equal returned identifiers. It cannot establish general GET support, identifier namespace semantics, complete own-app visibility, consistency after uncertain POST, or conclusive absence. Two requests leave no allowance for following pagination. An empty response cannot authorize another POST; an error code cannot by itself prove endpoint non-support. Local identifier equality is an observed equality, not a general identity contract.

## Reviewer Summaries
### instagram_subscription_recovery_opinion
- **Assessment:** The conservative first-POST plus durable UNCERTAIN/UNKNOWN fence is the simplest faithful interim architecture. The approved clauses require safe explicit recovery and an own-account observation capability; they do not guarantee successful automatic recovery independently of provider evidence. Independent CP3 implementation may proceed while IG-SUBPROTO-01 remains explicitly open. That sequencing does not complete CP2, accept the recovery criterion, waive any consumer obligation, or authorize provider activity. This is an architecture opinion, not current-source adherence or delivery acceptance.
- **Recommended path:** `Implement and source-review the durable first-dispatch fence, documented success handling, explicit advance boundary, and narrow subscription observer now. Persist dispatch intent before HTTP and conservatively retain uncertainty after any possibly dispatched mutation whose outcome was not durably established. Preserve that fence across authorization attempts for the same resource. Model observation as own-confirmed, conclusively-absent, or UNKNOWN; until the GET contract is established, do not invent parsing, identity comparisons, or absence evidence. UNKNOWN preserves pending and permits no further subscription mutation. Keep the actual own-account-read obligation explicitly incomplete where its protocol is unavailable. Establish GET support, response envelope, own-app identification, visibility and completeness semantics before accepting that obligation or enabling absence-based repeat POST. Continue independent CP3 work without changing the remaining checkpoint requirements. The main tradeoff is reduced automatic progress after uncertainty in exchange for truthful state and prevention of unsupported repeat mutation. A narrow state machine improves elegance and structural soundness; request limits keep performance acceptable without a measured throughput claim.`
- **Performance:** `acceptable`
- **Elegance:** `strong_positive`
- **Structural soundness:** `strong_positive`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] IG-SUBPROTO-01 The primary GET contract remains an acceptance prerequisite: The bounded package expressly retains this finding as open. The documented POST does not establish GET support, response shape, own-app identity, visibility, pagination completeness, or when an empty result proves absence. Conservative UNKNOWN handling preserves safety while these facts are missing, but does not close the unresolved observation requirement. Neither omission from documentation nor an installation-specific response establishes the missing universal contract.
  - [high] IG-SUBREC-02 The uncertainty fence must belong to the resource lifecycle: A new attempt, reauthorization, expired lease, or crash cannot prove that an earlier subscription POST did not reach Meta. A durable dispatch claim provides an at-most-once local dispatch policy, not an exactly-once provider outcome. Recording intent before HTTP can leave an operation uncertain even when a crash prevented transmission; that conservative loss of progress is consistent with the proposed no-repeat rule. A documented success:true confirms the subscription request but still does not replace the required authenticated ingress receipt.
  - [medium] IG-SUBREC-03 UNKNOWN is a valid recovery outcome, but does not erase the read obligation: Nothing in the approved clauses guarantees eventual automatic success after every uncertain mutation. Honest durable pending is therefore valid when evidence remains inconclusive. However, a handler that permanently returns UNKNOWN without an implemented supported observation path cannot be accepted as delivery of the explicit own-account-read requirement. Avoiding a speculative GET is a reasonable interim safety choice; claiming that this completes recovery would dilute approved scope.
  - [medium] IG-SUBREC-04 The proposed two-GET investigation provides bounded empirical evidence: The proposed operator sequence can materially clarify whether the selected installation accepts the requested endpoint and fields, what response shape and paging markers appear, and which locally known identifiers equal returned identifiers. It cannot establish general GET support, identifier namespace semantics, complete own-app visibility, consistency after uncertain POST, or conclusive absence. Two requests leave no allowance for following pagination. An empty response cannot authorize another POST; an error code cannot by itself prove endpoint non-support. Local identifier equality is an observed equality, not a general identity contract.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

