# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence127d-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Preserve the approved architecture and repair the residual consumer ownership and recovery defects plus the concrete protection-test defects below. Then obtain current canonical Web, full ALL, native browser proof and fresh affected review. Bounded pagination, indexed draft ownership, code-point input limits and admission-ID component keys are appropriate source improvements, but authored tests establish no runtime pass. Preserve the recorded scoped closures, official window-policy exception, pending human proposals, primary subscription-protocol obligation and remaining assurance/CP6 gates.`

## Merged Findings
### F-D2552EA7 [medium] The replacement-admission native test references an unimported createHash
- **Reviewers:** fresh-internal-no-context-127D
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Import createHash explicitly and execute the complete native case while preserving its real responses, hashes, deadlines, provider counters and cleanup requirements.
- **Rationale:** channel-transport.spec.ts imports only Playwright symbols but its new replacement-admission case calls createHash directly in both response handlers and subsequent assertions. The earlier case uses a dynamic crypto import, which does not define this identifier. The new mandatory case therefore encounters an unresolved identifier rather than completing its recovery proof; inside holdA this occurs before heldA is signalled.

### F-F54A03AA [medium] The old-admission assertions lack an application-completion barrier
- **Reviewers:** fresh-internal-no-context-127D
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Observe completion of the actual response consumption and ensuing metadata continuation before checking stale-state and stale-finally invariants. Retain unchanged real BFF responses and verify that A cannot publish, invalidate B's current read, clear B's busy state or carry risk confirmation.
- **Rationale:** The replacement-admission test releases A, waits for network completion and its route handler, then schedules a browser timer before asserting B's state. This does not establish completion of OrdinaryRecovery's application continuation, which awaits a further start-options request before its final state handling. The assertions can run while that continuation is still pending, missing the stale follow-up-read problem identified above. The earlier transport case explicitly instruments response.text; the new case does not provide an equivalent completion proof.

### F-D38D039B [medium] The failed-metadata native case targets an unavailable retry control
- **Reviewers:** fresh-internal-no-context-127D
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Align the native case with the supported explicit recovery path, or propagate the failed current read through the shared metadata owner and its retry surface. Preserve the assertions for blocked sending, retained draft, current successful metadata, visible admission recovery and zero extra POSTs.
- **Rationale:** After the unknown send, the composer calls refreshOrdinaryOptions. That function propagates its GET failure without setting the parent's startOptionsError; the composer suppresses that rejection and retains its own review fence. The new Instagram test nevertheless clicks Tentar novamente, which the parent renders only for its recorded unresolved/error state. With the preceding initial metadata read successful, that control is absent in this path. The composer remains blocked, but the authored recovery proof cannot complete as written.

### F-C1D7869D [medium] The 10,000-record draft test contradicts its own scoped cohort
- **Reviewers:** fresh-internal-no-context-127D
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Make the cohort and expected scoped membership agree, retaining all 10,000 original records and the revision/update checks. Execute the corrected test; keep measured frontend performance acceptance separate from functional membership assertions.
- **Rationale:** The cohort assigns both actor=id and conversation=id to record 9999, with buId=id. It then adds another target record in that same scope. forConversation(id,id,id) correctly returns both nonempty records, but the test expects only the added target, both before and after its update. This is a deterministic assertion defect, not evidence that the indexed owner scans unrelated conversations.

### F-643C7D69 [medium] Shared admission tickets do not fence every child continuation
- **Reviewers:** fresh-internal-no-context-127D
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Check current action and shared read ownership before allocating follow-up reads and before every local admission-state update. Give child continuations a reliable shared-ticket acceptance check. Add real-response ordering coverage for obsolete child-local updates and an old admission invalidating a newer pending read.
- **Rationale:** The parent now correctly rejects stale publications, but PrimeiraMensagem.reloadOptions updates recoveredAttempt before the parent checks its ticket. An older same-context response can therefore restore an obsolete active attempt locally after a newer parent observation released it. OrdinaryRecovery also calls refresh after its POST without first checking action ownership; refresh allocates a shared parent ticket before checking whether its admission component is still mounted. An old admission's continuation can invalidate a newer admission's pending read and then discard its own result. These are residual failures of the unresolved request-start ownership requirement.

### F-F1CB033C [medium] Creation recovery conflates creation refusal with later observation failure
- **Reviewers:** fresh-internal-no-context-127D
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Separate creation-dispatch errors from observation and continuation errors. Preserve the original key/body after a successful or uncertain creation until a conclusive observation is handled explicitly. Permit a deliberate new attempt after an authoritative terminal outcome, and cover observation denial and terminal recovery without another unintended creation.
- **Rationale:** begin catches failures from both the creation POST and observeAndContinue. After creation succeeds, a structured 4xx from the subsequent GET causes retainCreation(null), losing the exact key/body even though creation is known to have committed. Conversely, a conclusive CANCELLED, FAILED_SAFE or EXPIRED observation throws a generic error and leaves recovery permanently uncertain, with new creation disabled. The retained snapshot is useful, but uncertainty must be resolved according to the phase and observed durable outcome.

## Reviewer Summaries
### fresh-internal-no-context-127D
- **Assessment:** changes_required
- **Recommended path:** `Preserve the approved architecture and repair the residual consumer ownership and recovery defects plus the concrete protection-test defects below. Then obtain current canonical Web, full ALL, native browser proof and fresh affected review. Bounded pagination, indexed draft ownership, code-point input limits and admission-ID component keys are appropriate source improvements, but authored tests establish no runtime pass. Preserve the recorded scoped closures, official window-policy exception, pending human proposals, primary subscription-protocol obligation and remaining assurance/CP6 gates.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-ADHERENCE111D-04 Shared admission tickets do not fence every child continuation: The parent now correctly rejects stale publications, but PrimeiraMensagem.reloadOptions updates recoveredAttempt before the parent checks its ticket. An older same-context response can therefore restore an obsolete active attempt locally after a newer parent observation released it. OrdinaryRecovery also calls refresh after its POST without first checking action ownership; refresh allocates a shared parent ticket before checking whether its admission component is still mounted. An old admission's continuation can invalidate a newer admission's pending read and then discard its own result. These are residual failures of the unresolved request-start ownership requirement.
  - [medium] IG-ADHERENCE111D-06 Creation recovery conflates creation refusal with later observation failure: begin catches failures from both the creation POST and observeAndContinue. After creation succeeds, a structured 4xx from the subsequent GET causes retainCreation(null), losing the exact key/body even though creation is known to have committed. Conversely, a conclusive CANCELLED, FAILED_SAFE or EXPIRED observation throws a generic error and leaves recovery permanently uncertain, with new creation disabled. The retained snapshot is useful, but uncertainty must be resolved according to the phase and observed durable outcome.
  - [medium] IG-ADHERENCE127D-01 The replacement-admission native test references an unimported createHash: channel-transport.spec.ts imports only Playwright symbols but its new replacement-admission case calls createHash directly in both response handlers and subsequent assertions. The earlier case uses a dynamic crypto import, which does not define this identifier. The new mandatory case therefore encounters an unresolved identifier rather than completing its recovery proof; inside holdA this occurs before heldA is signalled.
  - [medium] IG-ADHERENCE127D-02 The 10,000-record draft test contradicts its own scoped cohort: The cohort assigns both actor=id and conversation=id to record 9999, with buId=id. It then adds another target record in that same scope. forConversation(id,id,id) correctly returns both nonempty records, but the test expects only the added target, both before and after its update. This is a deterministic assertion defect, not evidence that the indexed owner scans unrelated conversations.
  - [medium] IG-ADHERENCE127D-03 The failed-metadata native case targets an unavailable retry control: After the unknown send, the composer calls refreshOrdinaryOptions. That function propagates its GET failure without setting the parent's startOptionsError; the composer suppresses that rejection and retains its own review fence. The new Instagram test nevertheless clicks Tentar novamente, which the parent renders only for its recorded unresolved/error state. With the preceding initial metadata read successful, that control is absent in this path. The composer remains blocked, but the authored recovery proof cannot complete as written.
  - [medium] IG-ADHERENCE127D-04 The old-admission assertions lack an application-completion barrier: The replacement-admission test releases A, waits for network completion and its route handler, then schedules a browser timer before asserting B's state. This does not establish completion of OrdinaryRecovery's application continuation, which awaits a further start-options request before its final state handling. The assertions can run while that continuation is still pending, missing the stale follow-up-read problem identified above. The earlier transport case explicitly instruments response.text; the new case does not provide an equivalent completion proof.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
