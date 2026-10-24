# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-adherence35b-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Scoped Lane B review: inspected all 32 enclosed source bodies, all four governing contract excerpts, and all supplied evidence. No tools or additional reads. Obligation map: (1) Channel remains sendMessage/supportedKinds with actual adapter and abstract operation-policy DI; (2) strict V2 parsing, captured route tuples and transactional validation are present, with remaining authorization and query findings below; (3) the qualified captured address reaches both ordinary known-ACK and UNKNOWN acceptance, supporting the ROOT08 repair, while known-ACK credential coupling remains under ROOT02; (4) verified WhatsApp ingress establishes routes and canonical peer equality preserves legacy presentation, supporting ROOT05/06, but shared lock coordination remains incomplete under ROOT07; (5) qualified resource windows, Instagram human-only textual replies and initial/automation exclusion are present, with the existing 1000-character norm retained; (6) exact V1 readers and initial accepted-fact recovery avoid provider redispatch and current credential dependence; (7) inspected public, Typebot, Consultar and legacy BU consumers qualify WhatsApp identities, with ROOT03 query/export and planned CP4 work still open; (8) complete signed-batch preflight, four peer workers, per-peer ordering, collision serial execution and failure draining are implemented; (9) static performance, elegance and structural concerns are identified below, without a current benchmark claim; (10) CP4 consumers and all subsequent assurance/runtime gates remain mandatory. Repair the current source findings within the approved owners, then reconcile fresh canonical validation and the complementary Lane A review against the same freeze. API29 supplies qualified historical evidence, including the successful 1000-update case, but was not complete GREEN. Repairs30/32/34 remain behaviorally unproved in this package; their revised test bodies require Lane A inspection. API35 outcomes are excluded and unknown here. This result cannot independently accept CP3 or delivery.`

## Merged Findings
### F-BFF3F352 [high] V2 admission and acceptance paths use different peer mutexes
- **Reviewers:** cp3-adherence35b-fresh-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use the shared qualified-address locking owner consistently for applicable V2 admission, claim and completion paths, preserving the approved order. Handle historical recovery through its proved association. Verify contention using formatted WhatsApp presentation and identical Instagram peer strings under different accounts, without weakening the native P2002 oracle.
- **Rationale:** Acceptance uses lockContactIdentityAddress with the qualified address object. reserveInitial instead locks JSON.stringify([buId, contactIdentityId]); claimOrdinary, claimInitial, lockInitialOwner and acknowledgeOrdinaryRisk use [buId, Conversation.contact]; finalizeInitialInTransaction uses that legacy presentation key too. reserveOrdinary takes the conversation lock without the canonical peer mutex. These keys cannot coordinate as the shared provider identity → canonical peer → conversation protocol required by obligation4 and ROOT07. Provider/conversation locks still provide protection; this finding does not assert a demonstrated production deadlock or attribute API29's defective P2002 fixture to production.

### F-82713822 [high] Selected-route resolution still hydrates every channel in the BU
- **Reviewers:** cp3-adherence35b-fresh-reviewer
- **Category:** `performance`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Resolve an explicit selection through its exact route/channel identifiers. Bound legacy and initial choices to the qualified WhatsApp resource and its permitted adapters, adjudicating incompatibility before readiness. Add query-scope coverage with twelve Instagram accounts while preserving native public API and PCV limits.
- **Rationale:** PrismaChannelResolver.selectCandidate calls channels(buId) before handling an explicit routeId/channelId. That query loads every channel and its provider identities. initialOptions and hasReadyChannelForNewConversation also load all channel types before filtering WhatsApp. This directly conflicts with IG-ARCH-R1-04's exact selected-binding and bounded WhatsApp lookup requirements. The batch availability improvement does not close this remaining ROOT01 query path. The current code also lacks the required explicit WhatsApp cardinality adjudication before readiness in these paths.

### F-F0195119 [high] Ordinary known-ACK persistence still depends on current credential usability
- **Reviewers:** cp3-adherence35b-fresh-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use the captured accepted-operation association proof for ordinary local acceptance without requiring current credential usability. Preserve genuine ownership conflicts, explicit incomplete outcomes and zero redispatch. Prove known-ACK persistence when credentials disappear or cross the safety margin while the single POST is held.
- **Rationale:** After ACCEPTED, OutboundService.send calls contextAfterDispatch before attempting Message acceptance. contextStatus(context, false) still requires a current credential and, for Instagram, more than sixty seconds of remaining validity. Credential removal or crossing that safety margin during a successful HTTP request therefore prevents local Message creation even when the captured ownership/address tuple remains valid. The code returns ACCEPTED_LOCAL_INCOMPLETE and retains exclusion, but unnecessarily blocks recording the known fact. This leaves part of ROOT02 unresolved against the approved separation between dispatch eligibility and accepted-fact validation.

### F-F97726DF [high] Ordinary dispatch does not revalidate the human actor's current authority
- **Reviewers:** cp3-adherence35b-fresh-reviewer
- **Category:** `security`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Carry trusted caller authority into ordinary dispatch and revalidate it at the protected claim and final dispatch boundary. Preserve existing ordinary concurrency and API v1 behavior. Add a native session/PostgreSQL revocation case with a held preparation boundary and zero provider POSTs.
- **Rationale:** OutboundService.send captures a BFF userId, but its ordinary claim callback validates only transport context, credential and window. Neither claimOrdinary nor finalProviderFence checks the actor's current grant/session, and SendOutboundInput carries no authority validator. A grant revoked after surface authorization and during asynchronous preparation therefore does not prevent the common owner from authorizing the POST. IG-ARCH-R1-01 explicitly requires current grant validation before dispatch. The initial-send path already demonstrates an authority-validation mechanism; the ordinary path omits it.

### F-8BD62946 [medium] Recorded CP4 consumer obligations remain open
- **Reviewers:** cp3-adherence35b-fresh-reviewer
- **Category:** `residual_risk`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Carry these exact follow-ups into CP4 and complete their native consumer/browser proofs before delivery acceptance. Preserve the open primary subscription-observation, OAuth browser/gateway, human UTF-8/privacy decisions and CP5/CP6 gates. Do not treat this backend review as feature acceptance.
- **Rationale:** The recorded follow-up paths are cp4-connections-preparation21-root-qualified.json, cp4-safe-display-preparation22.json and cp4-readonly-preparation29-root-qualified.json. They explicitly retain connection catalogue/verify/disconnect, safe account identity, strict V2 React composition and native realtime work. Current replyOptions selects the latest authorization username without durable mapping qualification, and InstagramWebhookController calls acceptance directly without the IncomingService realtime publication path. React, gateway/browser, CI/freshness and remaining assurance/runtime evidence are absent. These are acknowledged subsequent-checkpoint obligations, not newly discovered CP3 implementation regressions or approved waivers.

### F-E5AF5A76 [medium] CSV export still loads the complete matching history
- **Reviewers:** cp3-adherence35b-fresh-reviewer
- **Category:** `performance`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Resolve this within the approved consumer/performance work while preserving CSV contents and filters: concretize bounded reads and output handling, then measure their limits. If the existing full-string contract requires an exception, obtain an explicit contract disposition before claiming complete adherence; do not silently truncate exports.
- **Rationale:** HistoricoService.csv performs unbounded conversation and message findMany calls, retains all conversations in a map, and accumulates every CSV row. Its WhatsApp qualification is present, but this does not satisfy obligation7's whole-history restriction. The supplied PCV probes do not establish export bounds. The package does not establish that this behavior is a new regression, so its provenance must remain qualified.

## Reviewer Summaries
### cp3-adherence35b-fresh-reviewer
- **Assessment:** changes_required
- **Recommended path:** `Scoped Lane B review: inspected all 32 enclosed source bodies, all four governing contract excerpts, and all supplied evidence. No tools or additional reads. Obligation map: (1) Channel remains sendMessage/supportedKinds with actual adapter and abstract operation-policy DI; (2) strict V2 parsing, captured route tuples and transactional validation are present, with remaining authorization and query findings below; (3) the qualified captured address reaches both ordinary known-ACK and UNKNOWN acceptance, supporting the ROOT08 repair, while known-ACK credential coupling remains under ROOT02; (4) verified WhatsApp ingress establishes routes and canonical peer equality preserves legacy presentation, supporting ROOT05/06, but shared lock coordination remains incomplete under ROOT07; (5) qualified resource windows, Instagram human-only textual replies and initial/automation exclusion are present, with the existing 1000-character norm retained; (6) exact V1 readers and initial accepted-fact recovery avoid provider redispatch and current credential dependence; (7) inspected public, Typebot, Consultar and legacy BU consumers qualify WhatsApp identities, with ROOT03 query/export and planned CP4 work still open; (8) complete signed-batch preflight, four peer workers, per-peer ordering, collision serial execution and failure draining are implemented; (9) static performance, elegance and structural concerns are identified below, without a current benchmark claim; (10) CP4 consumers and all subsequent assurance/runtime gates remain mandatory. Repair the current source findings within the approved owners, then reconcile fresh canonical validation and the complementary Lane A review against the same freeze. API29 supplies qualified historical evidence, including the successful 1000-update case, but was not complete GREEN. Repairs30/32/34 remain behaviorally unproved in this package; their revised test bodies require Lane A inspection. API35 outcomes are excluded and unknown here. This result cannot independently accept CP3 or delivery.`
- **Performance:** `mixed`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] IG-CP3-B35-01 Selected-route resolution still hydrates every channel in the BU: PrismaChannelResolver.selectCandidate calls channels(buId) before handling an explicit routeId/channelId. That query loads every channel and its provider identities. initialOptions and hasReadyChannelForNewConversation also load all channel types before filtering WhatsApp. This directly conflicts with IG-ARCH-R1-04's exact selected-binding and bounded WhatsApp lookup requirements. The batch availability improvement does not close this remaining ROOT01 query path. The current code also lacks the required explicit WhatsApp cardinality adjudication before readiness in these paths.
  - [high] IG-CP3-B35-02 V2 admission and acceptance paths use different peer mutexes: Acceptance uses lockContactIdentityAddress with the qualified address object. reserveInitial instead locks JSON.stringify([buId, contactIdentityId]); claimOrdinary, claimInitial, lockInitialOwner and acknowledgeOrdinaryRisk use [buId, Conversation.contact]; finalizeInitialInTransaction uses that legacy presentation key too. reserveOrdinary takes the conversation lock without the canonical peer mutex. These keys cannot coordinate as the shared provider identity → canonical peer → conversation protocol required by obligation4 and ROOT07. Provider/conversation locks still provide protection; this finding does not assert a demonstrated production deadlock or attribute API29's defective P2002 fixture to production.
  - [high] IG-CP3-B35-03 Ordinary dispatch does not revalidate the human actor's current authority: OutboundService.send captures a BFF userId, but its ordinary claim callback validates only transport context, credential and window. Neither claimOrdinary nor finalProviderFence checks the actor's current grant/session, and SendOutboundInput carries no authority validator. A grant revoked after surface authorization and during asynchronous preparation therefore does not prevent the common owner from authorizing the POST. IG-ARCH-R1-01 explicitly requires current grant validation before dispatch. The initial-send path already demonstrates an authority-validation mechanism; the ordinary path omits it.
  - [high] IG-CP3-B35-04 Ordinary known-ACK persistence still depends on current credential usability: After ACCEPTED, OutboundService.send calls contextAfterDispatch before attempting Message acceptance. contextStatus(context, false) still requires a current credential and, for Instagram, more than sixty seconds of remaining validity. Credential removal or crossing that safety margin during a successful HTTP request therefore prevents local Message creation even when the captured ownership/address tuple remains valid. The code returns ACCEPTED_LOCAL_INCOMPLETE and retains exclusion, but unnecessarily blocks recording the known fact. This leaves part of ROOT02 unresolved against the approved separation between dispatch eligibility and accepted-fact validation.
  - [medium] IG-CP3-B35-05 CSV export still loads the complete matching history: HistoricoService.csv performs unbounded conversation and message findMany calls, retains all conversations in a map, and accumulates every CSV row. Its WhatsApp qualification is present, but this does not satisfy obligation7's whole-history restriction. The supplied PCV probes do not establish export bounds. The package does not establish that this behavior is a new regression, so its provenance must remain qualified.
  - [medium] IG-CP3-B35-06 Recorded CP4 consumer obligations remain open: The recorded follow-up paths are cp4-connections-preparation21-root-qualified.json, cp4-safe-display-preparation22.json and cp4-readonly-preparation29-root-qualified.json. They explicitly retain connection catalogue/verify/disconnect, safe account identity, strict V2 React composition and native realtime work. Current replyOptions selects the latest authorization username without durable mapping qualification, and InstagramWebhookController calls acceptance directly without the IncomingService realtime publication path. React, gateway/browser, CI/freshness and remaining assurance/runtime evidence are absent. These are acknowledged subsequent-checkpoint obligations, not newly discovered CP3 implementation regressions or approved waivers.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

