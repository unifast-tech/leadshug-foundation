# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-adherence35a-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Fix the identified source and protection-harness defects within the approved architecture and this TODO. Re-freeze the affected candidate, obtain canonical validation and affected independent review, then combine both complementary reviews through root union/freeze reconciliation. Preserve every recorded CP2, CP4–CP6, ALL, assurance and runtime gate.`

## Merged Findings
### F-01366BED [high] The final send boundary does not revalidate current authorization
- **Reviewers:** cp3-adherence35a-no-context
- **Category:** `security`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Carry a server-owned authorization fence through the shared ordinary and initial send paths and revalidate it at the final provider boundary after claim completion. Preserve short transactions, HTTP outside transactions and existing error ordering. Add native delayed-boundary tests for grant revocation and session expiry, with zero-POST assertions and matched live controls.
- **Rationale:** IG-ARCH-R1-01 requires current grants before provider POST. Ordinary replies enter OutboundService with attribution only: claimOrdinary validates route, credential and policy, while finalProviderFence checks context, window and deadlines without checking the session, actor or current grant. Initial sends validate the actor during the claim transaction, but subsequent post-commit context/window awaits also have no final actor check. Revocation or session expiry during those waits can therefore leave dispatch authorized.

### F-77E0CE1F [high] Ordinary known-ACK completion still depends on current credential availability
- **Reviewers:** cp3-adherence35a-no-context
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Separate pre-dispatch credential eligibility from post-ACK association proof. Complete known receipts through the existing acceptance owner using the captured immutable tuple without requiring a currently usable credential. Retain genuine ownership/generation conflict fences. Prove paused-HTTP credential removal, rotation and safety-margin crossing with one POST and exact local receipt ownership.
- **Rationale:** contextStatus(context, false) still requires an official/Instagram credential and, for Instagram, more than 60 seconds of remaining validity. OutboundService calls this after receiving ACCEPTED and refuses Message acceptance when it returns CHANGED. A credential removed during the request, or an Instagram token crossing the safety margin during an otherwise valid POST, prevents local completion of the exact known receipt despite unchanged route/resource ownership. This retains the credential-coupling residual forbidden by the frozen post-ACK contract.

### F-440846A6 [high] Explicit route selection and WhatsApp options still hydrate every BU connection
- **Reviewers:** cp3-adherence35a-no-context
- **Category:** `performance`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Resolve explicit selections by their exact scoped IDs. Query only compatible WhatsApp bindings for initial options/readiness and explicitly reject excess cardinality before readiness filtering. Preserve page-scoped batching and add native query/admission assertions using the approved twelve-account cohort; retain the frozen EPS/RLS measurements as outstanding.
- **Rationale:** selectCandidate calls channels(buId), which loads all BU bindings and their provider identities even when routeId/channelId are explicitly supplied. initialOptions and hasReadyChannelForNewConversation also load that complete multichannel collection before filtering WhatsApp in memory. This directly contradicts IG-ARCH-R1-04's exact selected lookups and bounded WhatsApp-only options. The batched window implementation and API29 ingress timings do not establish compliance for these reads.

### F-143DDD90 [medium] V2 admission owners do not share the canonical peer advisory lock
- **Reviewers:** cp3-adherence35a-no-context
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use the shared qualified-address lock owner consistently for affected V2 lifecycle paths before conversation locking. Preserve the explicitly bounded V1 compatibility behavior. Add native lock-order coverage across admission and acceptance owners without changing the P2002 assertions, counters or transaction timeout.
- **Rationale:** MessageAcceptance uses lockContactIdentityAddress with the qualified address object, matching the repaired native P2002 fixture. reserveInitial instead hashes [buId, contactIdentityId]; claimOrdinary, claimInitial and lockInitialOwner hash [buId, Conversation.contact]; reserveOrdinary proceeds directly from provider identity to conversation locking. finalizeInitialInTransaction also acquires the legacy contact-string key. These keys do not serialize with the canonical peer lock required by the dispatch's shared identity→peer→conversation invariant. The new P2002 fixture proves only the acceptance key, and remains NOTRUN here; no production deadlock is inferred.

### F-98B8C588 [medium] The dependency protection harness omits Instagram coupling
- **Reviewers:** cp3-adherence35a-no-context
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Extend the existing bounded harness to cover Instagram clients/tokens and relevant send consumers. Add negative fixtures for dispatch coupling through adapterOrigin and direct concrete policy dependencies, while allowing legitimate qualified-address validation. Keep the solution small and specific to the approved boundary.
- **Rationale:** channel-dependencies.spec.ts rejects imports under integrations/meta, evolution and channels, but permits integrations/instagram imports. Its injection-token fixtures omit Instagram, and concrete comparison detection omits the new adapterOrigin property. InitialMessageService is also outside its inspected consumer set. Thus the mandated protection harness can remain green after introducing an Instagram client or dispatch-specific concrete dependency into a business send consumer, despite the current DI composition being structurally appropriate.

### F-FFF98226 [medium] Recorded consumer and operational follow-ups remain delivery blockers
- **Reviewers:** cp3-adherence35a-no-context
- **Category:** `residual_risk`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Carry these recorded follow-ups through CP4 and the remaining approved gates without accepting a backend-only feature. Complete connection lifecycle, safe display, composer/context fencing, native WS/browser/freshness/CI coverage and ALL validation; retain independent assurance and separately approved real-runtime proof.
- **Rationale:** The recorded follow-up paths are cp4-connections-preparation21-root-qualified.json, cp4-safe-display-preparation22.json and cp4-readonly-preparation29-root-qualified.json. They explicitly retain missing paginated connection lifecycle surfaces, safe account/peer projections, strict V2 React consumers and shared Incoming/realtime delivery. The inspected replyOptions query still chooses the latest authorization username without durable mapped-account qualification, and the BFF now requires V2 fields that the recorded legacy UI does not send. These are planned CP4 obligations with no waiver. Primary subscription observation, OAuth browser/gateway proof, pending human proposals and CP5/CP6 validation also remain open.

## Reviewer Summaries
### cp3-adherence35a-no-context
- **Assessment:** Changes required within lane A. Reviewed all 37 enclosed source bodies, all four governing contract ranges and all 14 required evidence artifacts; no tools or additional reads. Obligations 1–6 show substantial alignment through actual Channel DI, operation-specific policies, strict V2 contexts, shared acceptance and local-only V1 recovery, but retain the defects below. ROOT-01/02/07 remain open in the identified respects; ROOT-05/06 have supporting canonical acceptance and route-establishment code, and sender25 supports ROOT-08 with qualified API29 native evidence. Obligations 7–8 require complementary lane B for full consumer and ingress-scheduler inspection; this lane assessed their common-owner interactions only. Obligation 9 remains mixed across performance, elegance, structure and operational fit. Obligation 10 remains mandatory through the recorded CP4–CP6 work. API29 was incomplete; repairs30/32/34 have no reconciled behavioral pass in this package. No lane-B, complete-52-source, CP3 or delivery acceptance is asserted.
- **Recommended path:** `Fix the identified source and protection-harness defects within the approved architecture and this TODO. Re-freeze the affected candidate, obtain canonical validation and affected independent review, then combine both complementary reviews through root union/freeze reconciliation. Preserve every recorded CP2, CP4–CP6, ALL, assurance and runtime gate.`
- **Performance:** `mixed`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] IG-CP3-A-01 The final send boundary does not revalidate current authorization: IG-ARCH-R1-01 requires current grants before provider POST. Ordinary replies enter OutboundService with attribution only: claimOrdinary validates route, credential and policy, while finalProviderFence checks context, window and deadlines without checking the session, actor or current grant. Initial sends validate the actor during the claim transaction, but subsequent post-commit context/window awaits also have no final actor check. Revocation or session expiry during those waits can therefore leave dispatch authorized.
  - [high] IG-CP3-ROOT-02 Ordinary known-ACK completion still depends on current credential availability: contextStatus(context, false) still requires an official/Instagram credential and, for Instagram, more than 60 seconds of remaining validity. OutboundService calls this after receiving ACCEPTED and refuses Message acceptance when it returns CHANGED. A credential removed during the request, or an Instagram token crossing the safety margin during an otherwise valid POST, prevents local completion of the exact known receipt despite unchanged route/resource ownership. This retains the credential-coupling residual forbidden by the frozen post-ACK contract.
  - [high] IG-CP3-ROOT-01 Explicit route selection and WhatsApp options still hydrate every BU connection: selectCandidate calls channels(buId), which loads all BU bindings and their provider identities even when routeId/channelId are explicitly supplied. initialOptions and hasReadyChannelForNewConversation also load that complete multichannel collection before filtering WhatsApp in memory. This directly contradicts IG-ARCH-R1-04's exact selected lookups and bounded WhatsApp-only options. The batched window implementation and API29 ingress timings do not establish compliance for these reads.
  - [medium] IG-CP3-ROOT-07 V2 admission owners do not share the canonical peer advisory lock: MessageAcceptance uses lockContactIdentityAddress with the qualified address object, matching the repaired native P2002 fixture. reserveInitial instead hashes [buId, contactIdentityId]; claimOrdinary, claimInitial and lockInitialOwner hash [buId, Conversation.contact]; reserveOrdinary proceeds directly from provider identity to conversation locking. finalizeInitialInTransaction also acquires the legacy contact-string key. These keys do not serialize with the canonical peer lock required by the dispatch's shared identity→peer→conversation invariant. The new P2002 fixture proves only the acceptance key, and remains NOTRUN here; no production deadlock is inferred.
  - [medium] IG-CP3-A-02 The dependency protection harness omits Instagram coupling: channel-dependencies.spec.ts rejects imports under integrations/meta, evolution and channels, but permits integrations/instagram imports. Its injection-token fixtures omit Instagram, and concrete comparison detection omits the new adapterOrigin property. InitialMessageService is also outside its inspected consumer set. Thus the mandated protection harness can remain green after introducing an Instagram client or dispatch-specific concrete dependency into a business send consumer, despite the current DI composition being structurally appropriate.
  - [medium] IG-CP3-ROOT-03 Recorded consumer and operational follow-ups remain delivery blockers: The recorded follow-up paths are cp4-connections-preparation21-root-qualified.json, cp4-safe-display-preparation22.json and cp4-readonly-preparation29-root-qualified.json. They explicitly retain missing paginated connection lifecycle surfaces, safe account/peer projections, strict V2 React consumers and shared Incoming/realtime delivery. The inspected replyOptions query still chooses the latest authorization username without durable mapped-account qualification, and the BFF now requires V2 fields that the recorded legacy UI does not send. These are planned CP4 obligations with no waiver. Primary subscription observation, OAuth browser/gateway proof, pending human proposals and CP5/CP6 validation also remain open.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

