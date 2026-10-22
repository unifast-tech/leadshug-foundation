# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-architecture_adherence-r1-dispatch-v1.1.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Keep E47 frozen through terminal execution, cleanup and independent postseal before releasing the writer. Resolve the findings and run canonical all against the revised frozen candidate. The activation proposal preserves data and provider services and correctly leaves private configuration consumption and full diff inspection subject to separate approval. DOD-11/12/13, actual Alpine image/runtime provenance, preserved-database migration preflight, assisted first-send/reply proofs, module consolidation and final guards remain required gates.`

## Merged Findings
### F-511FF1D6 [medium] The dependency protection harness omits the new initial coordinator
- **Reviewers:** fresh-bounded-reviewer-r1
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Add an admitted companion architecture test covering the initial coordinator and synthetic forbidden provider coupling while retaining sealed inherited harness bytes. Include this protection in the canonical suite and evidence mapping.
- **Rationale:** The supplied channel-dependencies harness scans conversations.service, incoming.service and outbound-prefixed files only. It never scans initial-message.service, the newly introduced orchestration locus that must remain free of concrete provider imports and dispatch. Thus its passing result does not protect a central boundary required by the Architecture Protection Harness, although the current coordinator itself shows no concrete provider dispatch.

### F-8E89FC19 [medium] Ordinary success ignores an unconfirmed settlement result
- **Reviewers:** fresh-bounded-reviewer-r1
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Require a positively confirmed settlement result before reporting complete ordinary success. Preserve known provider acceptance and recorded Message metadata when settlement remains unconfirmed. Add an actual rollback case through OutboundService.send, alongside commit-ACK-loss readback coverage.
- **Rationale:** settleOrdinary can return false after a real transaction rollback leaves the token SENDING and unreleased. OutboundService.send awaits settlement but ignores that boolean, then finalizes and returns success. Its catch handles thrown failures only. Consequently, an ordinary send can report successful completion while retaining exclusion that later requires uncertainty recovery, contrary to the approved positive-confirmation requirement at settlement/release.

### F-ED2FCC37 [medium] Local initial reconciliation omits realtime publication for its creation winner
- **Reviewers:** fresh-bounded-reviewer-r1
- **Category:** `adherence`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Apply the same post-commit winner-only publication rule to successful local reconciliation. Verify one event for a recovered creation winner, zero additional events for an existing echo or replay, and zero provider I/O.
- **Rationale:** reconcileInitial can create and commit the first Message through acceptInTransaction, but returns accepted.message without inspecting creationWinner or publishing realtime. The normal sendInitial path performs that publication. Recovery therefore deterministically omits the event even after a positively confirmed creation commit; this exceeds the approved best-effort crash-gap limitation and leaves other consumers waiting for polling.

### F-C8AF5811 [medium] Every ordinary BFF send counts the complete message history
- **Reviewers:** fresh-bounded-reviewer-r1
- **Category:** `performance`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `paced`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use an indexed, bounded existence lookup with the approved transport-message predicate. Verify the ordinary-send admission path against a large history without counting or hydrating that history.
- **Rationale:** assertOrdinaryDispatchAllowed uses message.count where it only needs to establish whether a transport message exists. This introduces history-proportional database work on every ordinary BFF response. The supplied list/window EXPLAIN evidence does not exercise this new sender lookup.

### F-3E65B77F [medium] An abandoned PREPARED attempt has no usable browser recovery action
- **Reviewers:** fresh-bounded-reviewer-r1
- **Category:** `operational_fit`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Expose explicit local reconciliation for PREPARED, preserving the live-lease 202 behavior and expired undispatched release. Add a real-BFF/browser case covering abandoned reservation, reload, expiry, reconciliation and successor admission with zero provider calls.
- **Rationale:** projectIntent assigns PREPARED a null recoveryAction. PrimeiraMensagem treats its active slot as locked and renders local reconciliation only for recoveryAction=RECONCILE. Consultar estado performs observational reads, so even after lease expiry the browser cannot invoke the endpoint that rejects and releases expired PREPARED. A crash after reservation and before dispatch can therefore strand the conversation despite the approved finite recovery contract.

### F-F7C06078 [medium] Active-slot refusals do not implement the frozen interlock error contract
- **Reviewers:** fresh-bounded-reviewer-r1
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Keep INITIAL_SEND_REQUIRED for the BFF empty-conversation case and implement the approved active-slot and ordinary-admission conflict projections separately. Update BFF/public/BOT regressions to assert exact safe codes, outcomes, scoped identifiers and zero dispatch.
- **Rationale:** reserveOrdinary returns INITIAL_SEND_REQUIRED for an active initial slot, and assertOrdinaryDispatchAllowed conflates that condition with an empty conversation. Neither supplies the approved BLOCKED outcome, INITIAL_SEND_IN_PROGRESS code and authorized attempt/state metadata. Initial reservation blocked by ordinary admissions similarly omits the authorized token IDs specified by the normative contract. The embedded tests assert some of these divergent mappings rather than protecting the approved distinction.

## Reviewer Summaries
### fresh-bounded-reviewer-r1
- **Assessment:** Changes required. The implementation preserves the approved Channel, Outbound, MessageAcceptance and catalog owners, including the intentional union and trusted-window supersedes. The supplied negative proofs support the initial session, tenant, grant, webhook and bounded provider checks; no bypass is established by this review. However, recovery, settlement certainty and caller-contract defects remain. E45 and the explicitly bounded E46/E47 composite provide useful implementation evidence without establishing full E47 completion or preserved-runtime readiness.
- **Recommended path:** `Keep E47 frozen through terminal execution, cleanup and independent postseal before releasing the writer. Resolve the findings and run canonical all against the revised frozen candidate. The activation proposal preserves data and provider services and correctly leaves private configuration consumption and full diff inspection subject to separate approval. DOD-11/12/13, actual Alpine image/runtime provenance, preserved-database migration preflight, assisted first-send/reply proofs, module consolidation and final guards remain required gates.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] ARCH-ST04-R1-01 An abandoned PREPARED attempt has no usable browser recovery action: projectIntent assigns PREPARED a null recoveryAction. PrimeiraMensagem treats its active slot as locked and renders local reconciliation only for recoveryAction=RECONCILE. Consultar estado performs observational reads, so even after lease expiry the browser cannot invoke the endpoint that rejects and releases expired PREPARED. A crash after reservation and before dispatch can therefore strand the conversation despite the approved finite recovery contract.
  - [medium] ARCH-ST04-R1-02 Ordinary success ignores an unconfirmed settlement result: settleOrdinary can return false after a real transaction rollback leaves the token SENDING and unreleased. OutboundService.send awaits settlement but ignores that boolean, then finalizes and returns success. Its catch handles thrown failures only. Consequently, an ordinary send can report successful completion while retaining exclusion that later requires uncertainty recovery, contrary to the approved positive-confirmation requirement at settlement/release.
  - [medium] ARCH-ST04-R1-03 Local initial reconciliation omits realtime publication for its creation winner: reconcileInitial can create and commit the first Message through acceptInTransaction, but returns accepted.message without inspecting creationWinner or publishing realtime. The normal sendInitial path performs that publication. Recovery therefore deterministically omits the event even after a positively confirmed creation commit; this exceeds the approved best-effort crash-gap limitation and leaves other consumers waiting for polling.
  - [medium] ARCH-ST04-R1-04 Active-slot refusals do not implement the frozen interlock error contract: reserveOrdinary returns INITIAL_SEND_REQUIRED for an active initial slot, and assertOrdinaryDispatchAllowed conflates that condition with an empty conversation. Neither supplies the approved BLOCKED outcome, INITIAL_SEND_IN_PROGRESS code and authorized attempt/state metadata. Initial reservation blocked by ordinary admissions similarly omits the authorized token IDs specified by the normative contract. The embedded tests assert some of these divergent mappings rather than protecting the approved distinction.
  - [medium] ARCH-ST04-R1-05 Every ordinary BFF send counts the complete message history: assertOrdinaryDispatchAllowed uses message.count where it only needs to establish whether a transport message exists. This introduces history-proportional database work on every ordinary BFF response. The supplied list/window EXPLAIN evidence does not exercise this new sender lookup.
  - [medium] ARCH-ST04-R1-06 The dependency protection harness omits the new initial coordinator: The supplied channel-dependencies harness scans conversations.service, incoming.service and outbound-prefixed files only. It never scans initial-message.service, the newly introduced orchestration locus that must remain free of concrete provider imports and dispatch. Thus its passing result does not protect a central boundary required by the Architecture Protection Harness, although the current coordinator itself shows no concrete provider dispatch.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

