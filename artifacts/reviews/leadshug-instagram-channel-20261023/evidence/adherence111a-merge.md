# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence111a-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Fix these defects within this TODO, obtain focused native regression proof and complete current canonical ALL validation. Preserve historical closures. Keep own-subscription protocol/observation, complete Instagram browser and recovery proof, CP5 performance/security/TQA/cutover/final reviews and separately approved CP6 real-runtime proof open. Native109 and CP5 source110a remain unexecuted; pending privacy and UTF8 proposals confer no implementation authority.`

## Merged Findings
### F-07FFD00E [medium] UUID Evolution verification bypasses the existing product-module gate
- **Reviewers:** fresh-no-context-runtime111A
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Apply the existing unofficial-channel module admission to UUID verification before provider work, while preserving actor authorization and exact-binding checks. Add native enabled/disabled controls showing equivalent enforcement on both verification surfaces and zero provider calls when disabled.
- **Rationale:** The existing :tipo/verify controller calls modulos.exigir for NAO_OFICIAL before invoking ChannelsService.verificar. The new UUID verification path calls that same service without this check, and ChannelsService contains no equivalent module guard. An ADMIN with an existing Evolution binding can therefore reach provider verification and trust updates through the UUID endpoint while the tenant's unofficial-channel module is disabled. SCOPE-03 and DOD-07 require preservation of existing WhatsApp contracts; UUID addressing does not authorize removing this capability restriction.

### F-3965105A [medium] Durable verification can strand its binding lease after commit
- **Reviewers:** fresh-no-context-runtime111A
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Extend the exact-original-token cleanup lifecycle around verification acquisition itself, including rejection after a committed claim. Preserve successor leases and subscription-dispatch history. Prove natural signed-session expiry across an actual PostgreSQL commit with a matched live control and immediate original-holder cleanup.
- **Rationale:** verifyConnection awaits actorTransaction before entering its try/finally. That transaction commits the provider-resource lease, while actorTransaction performs another signed-session check after the awaited commit. If the session expires across commit, the await rejects before binding is assigned and before cleanup becomes active. The original lease remains until its 60-second expiry despite zero provider requests, blocking subsequent verification or credential promotion. This is the new CP4 verification path; the resolved subscribeAfterMapping acquisition repair remains closed.

### F-A225B87E [medium] Disconnecting Instagram removes its known readable account label
- **Reviewers:** fresh-no-context-runtime111A
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Project the last proven account label independently of current credential usability, retaining exact BU, channel, immutable resource and app-scope association checks. Verify that two disconnected accounts retain distinguishable known labels through catalog reload and reauthorization without exposing credentials or changing readiness.
- **Rationale:** Both display queries recover account_username only through a completed attempt matching the currently joined credential version and generation. disconnectConnection deletes that credential and increments generation, so the retained, proven username becomes unavailable to the projector. Multiple disconnected accounts consequently return the same generic Instagram accountLabel despite retained ownership and authorization evidence. This conflicts with SCOPE-07/DOD-06 and the catalog contract requiring a readable account alongside its local UUID, particularly when choosing a connection for reauthorization.

## Reviewer Summaries
### fresh-no-context-runtime111A
- **Assessment:** changes_required: The enclosed source preserves the shared Channel/Outbound/Acceptance design, strict V2 context, durable ownership and configured official-window exception. Three defects remain in the newer connection-management and presentation paths. These are static findings from the bounded package; no additional execution, hash verification, peer-lane inspection or runtime acceptance is claimed.
- **Recommended path:** `Fix these defects within this TODO, obtain focused native regression proof and complete current canonical ALL validation. Preserve historical closures. Keep own-subscription protocol/observation, complete Instagram browser and recovery proof, CP5 performance/security/TQA/cutover/final reviews and separately approved CP6 real-runtime proof open. Native109 and CP5 source110a remain unexecuted; pending privacy and UTF8 proposals confer no implementation authority.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-ADHERENCE111A-01 Durable verification can strand its binding lease after commit: verifyConnection awaits actorTransaction before entering its try/finally. That transaction commits the provider-resource lease, while actorTransaction performs another signed-session check after the awaited commit. If the session expires across commit, the await rejects before binding is assigned and before cleanup becomes active. The original lease remains until its 60-second expiry despite zero provider requests, blocking subsequent verification or credential promotion. This is the new CP4 verification path; the resolved subscribeAfterMapping acquisition repair remains closed.
  - [medium] IG-ADHERENCE111A-02 UUID Evolution verification bypasses the existing product-module gate: The existing :tipo/verify controller calls modulos.exigir for NAO_OFICIAL before invoking ChannelsService.verificar. The new UUID verification path calls that same service without this check, and ChannelsService contains no equivalent module guard. An ADMIN with an existing Evolution binding can therefore reach provider verification and trust updates through the UUID endpoint while the tenant's unofficial-channel module is disabled. SCOPE-03 and DOD-07 require preservation of existing WhatsApp contracts; UUID addressing does not authorize removing this capability restriction.
  - [medium] IG-ADHERENCE111A-03 Disconnecting Instagram removes its known readable account label: Both display queries recover account_username only through a completed attempt matching the currently joined credential version and generation. disconnectConnection deletes that credential and increments generation, so the retained, proven username becomes unavailable to the projector. Multiple disconnected accounts consequently return the same generic Instagram accountLabel despite retained ownership and authorization evidence. This conflicts with SCOPE-07/DOD-06 and the catalog contract requiring a readable account alongside its local UUID, particularly when choosing a connection for reauthorization.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
