# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r6-adherence.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Resolve findings ADH-R6-01 through ADH-R6-06 within the approved architecture before activation. Retain failing behavioral assertions for the uncovered cases, refresh the source freeze, run the required canonical validation, and obtain affected independent assurance. Route ADH-R6-07 to the security and credential owner for explicit disposition. Preserve Pending delivery status until the approved metadata preflight, migration, source-bound activation, assisted provider proof, required gate records and fresh final review are complete.`

## Merged Findings
### F-BC740DD4 [high] Contradictory provider read envelopes can authorize submission or certify an observation
- **Reviewers:** fresh-internal-no-context-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: Reject contradictory/error-bearing success wrappers in the shared read validator. B: Introduce strict operation-specific envelope validation for list and individual reads. C: Retain current permissiveness; this is unsuitable for absence or approval evidence. Recommend A with operation-specific shape checks retained. Verify contradictory preflight produces zero POSTs, and contradictory catalog/individual responses preserve prior content while marking it unavailable and ineligible.
- **Rationale:** api-app/src/integrations/meta/message-template.client.ts:225 accepts every HTTP-success JSON object in readObject. Unlike loadGrant and createTemplate, listTemplates and getTemplate do not reject an error envelope accompanying otherwise plausible data. Consequently HTTP 200 with error plus data:[] passes preflight as proven absence and permits POST; error plus a plausible APPROVED template can become an eligible observation. This violates D05's inconclusive-response prohibition and D07's requirement that provider errors preserve prior observations without fabricating an empty or successful result.

### F-A126DD89 [high] A completed correlation prevents the original ACK from improving the operation
- **Reviewers:** fresh-internal-no-context-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: Permit a captured original claim to atomically upgrade matching correlated acceptance to acknowledged acceptance and append its receipt. B: Retain confirmed original-ACK evidence separately when association cannot safely change, with explicit projection semantics and no silent rebinding. C: Leave current behavior; this cannot satisfy the frozen late-result contract. Recommend A for matching IDs and an explicit disposition for conflicting IDs. Verify both completion orders, matching and differing IDs, durable receipts, unchanged reservations and exactly one POST.
- **Rationale:** In api-app/src/domain/message-templates/template-submission.service.ts:564, recordOutcome updates only SENDING or AMBIGUOUS operations. If reconciliation commits CORRELATED_BY_DEFINITION first, a subsequent valid original ACK cannot update even an identical remote ID. Its readback also requires ACKNOWLEDGED provenance, so the request returns local-incomplete without retaining an ACK receipt, while persisted providerAcceptance remains UNKNOWN. D06 and CR-01 require monotonic enrichment of the same operation. The retained late-ACK test exercises ACK completion before the held recovery response, leaving the inverse ordering unprotected.

### F-A6F77CFC [medium] The disclosed connector credential incident remains operationally unresolved
- **Reviewers:** fresh-internal-no-context-reviewer
- **Category:** `residual_risk`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `paced`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: Have the credential owner revoke/reissue it and record a secret-free confirmation. B: Obtain explicit security-owner acceptance with scope, owner and follow-up deadline if rotation cannot yet occur. C: Take no further action; retain the incident as unresolved. Recommend A. Verify disposition and continued exclusion of inherited connector configuration from reviewer startup without reproducing the secret or inspecting protected product paths. This finding does not require redesigning template management.
- **Rationale:** evidence/executor-startup-secret-redaction-v1.1.json:4 records credential disclosure in rendered startup diagnostics, and its actions record artifact scrubbing and operator notification. The package explicitly states that rotation is unconfirmed and previously rendered output cannot be retracted. These mitigations do not establish credential invalidation. This is a residual operational security issue, not evidence that the template architecture or Meta credentials were compromised, and it must not be silently closed.

### F-86490436 [medium] Submission recovery can overwrite text edited while the request was pending
- **Reviewers:** fresh-internal-no-context-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: Capture editEpoch at mutation start and check it before every later form replacement. B: Preserve the current form throughout recovery and adopt only durable identity, revision and savedDefinition. C: Leave the captured dirty check; this retains reproducible text loss. Recommend A, matching the existing save protection. Verify held submit followed by an edit and uncertain/local-incomplete recovery preserves the edited form, durable operation identity and no-replay behavior.
- **Rationale:** web-app/src/telas/Modelos.tsx:454 and :482 use captured dirty values before replacing the form with authoritative.definition. enviar starts only when dirty is false, while editor fields remain writable until a later response locks the draft. If the seller edits during a held submission and its 503 recovery reads succeed, the old closure still executes setForm and erases those newer edits. Context/editor fences do not detect edits within the same editor. This contradicts D08's monotonic edit protection and the approved preservation of current text.

### F-9DD31CD5 [medium] Individual refresh completion loses the draft owner/admin authorization requirement
- **Reviewers:** fresh-internal-no-context-reviewer
- **Category:** `security`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: Recheck the captured draft's ownership and current BU role inside the completion transaction. B: Pass a producer-specific authorization predicate into the shared lease completion path, retaining ATENDENTE access for catalog refresh. C: Keep existence-only revalidation; this leaves the authorization exception unresolved. Recommend A or B without raising catalog permissions. Verify a held individual response after ADMIN-to-ATENDENTE downgrade cannot write or disclose the draft-specific result; retain positive owner and catalog cases.
- **Rationale:** TemplateObservationService.authorizeDraft initially checks ownership or ADMIN, but ownsLease at api-app/src/domain/message-templates/template-observation.service.ts:314 revalidates only an active actor, active BU and grant existence; its grant query selects userId without role. An administrator refreshing another seller's draft can therefore be downgraded to ATENDENTE during provider I/O and still commit and receive the individual result. The row locks preserve a grant that no longer authorizes that draft-specific operation. D01 and the frozen individual-refresh contract require owner/admin access.

### F-CB40348A [medium] Failed individual refresh leaves previously approved UI copies eligible
- **Reviewers:** fresh-internal-no-context-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: Under the current UI fence, preserve prior content but invalidate availability and eligibility across its individual and catalog copies. B: Read back the shared persisted observation through an observational endpoint, keeping eligibility disabled until confirmed. C: Preserve the present eligible display; this violates the error-state contract. Recommend A, optionally followed by B. Verify APPROVED followed by individual timeout/malformed response immediately becomes unavailable and ineligible, and that an older error cannot invalidate a newer success.
- **Rationale:** At web-app/src/telas/Modelos.tsx:519, atualizarStatus handles failure by setting an error only. The backend marks the shared observation unavailable and observedEligible=false, but the browser retains its prior APPROVED individualStatus and catalog copies with available=true. Unlike catalog refresh failure, this path does not set a blocking availability flag or reload the persisted observation. The screen can continue displaying eligibility until TTL expiry despite a known current refresh failure, contrary to D07.

### F-9FD4929D [medium] Draft and operation GETs omit the shared persisted observation
- **Reviewers:** fresh-internal-no-context-reviewer
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A: Reuse the observation owner's bounded read projector in draft/operation DTOs and restore that state when opening the draft. B: Seek renewed approval for reduced GET/reload semantics; no such exception currently exists. C: Leave the omission and keep this contract unmet. Recommend A without provider calls or writes in GET. Verify individual PAUSED with no catalog page survives draft GET, operation GET and browser reload; also verify TTL, changed-context ineligibility and both producer directions.
- **Rationale:** TemplateDraftService.projectWithOperations returns draft/operation/receipt data at api-app/src/domain/message-templates/template-draft.service.ts:255, and TemplateSubmissionService.projectOperation at :663 likewise omits observations. Opening a draft clears individualStatus in Modelos.tsx:302. Thus an individual PAUSED observation obtained before any catalog page exists cannot be recovered after reload without another provider refresh. D07, the operation GET contract and CR-V11-01 explicitly require draft/catalog/GET/reload projections to derive from the same observation. The browser reload scenario refreshes remotely before asserting individual PAUSED, so its pass does not close this gap.

## Reviewer Summaries
### fresh-internal-no-context-reviewer
- **Assessment:** Changes required before candidate adherence can pass. The delivered architecture substantially preserves D01 seller submission without an administrator intermediary, D02 backend validation and escaped previews, D03 persistent ownership and immutable revisions, and D09 the separate narrow capability and sole credential owner. No compatibility shim or generic future-network platform is evident. Concrete exceptions remain in current authorization, D05 malformed-read handling, D06 late-result convergence, D07 observation projections, and D08 preservation of edits.

Audit complexity is big. The supplied canonical all success, 38 source matches, real disposable PostgreSQL, fresh served bundle, provider wire tests and real-BFF browser tests provide substantial candidate evidence. Required ownership and command boundaries are identifiable. Test changes generally match actual contract changes: explicit listener lifetime, complete refusal envelopes, descending receipt sequence, deeper history fixtures and the 150-buffer bound retain meaningful business assertions. No committed skip, focused test, silent provider fallback or production test-only route is evident. Transaction and clock controls preserve real PostgreSQL work. Assertion efficiency and bounded SQL are acceptable, but the uncovered counterexamples below prevent coverage sufficiency. Most feature tests remain test-after or unknown; the retained nullable-projection failure supplies behavioral RED only for that repair. Infrastructure failures do not supply behavioral RED.

Performance evidence supports bounded access paths and controlled concurrency, without establishing production capacity. The capability separation is a faithful, reasonably simple design; a broader redesign is unnecessary. Changed-account UI evidence remains compositional. Preserved-database migration, actual activation, provider proof, formal gate artifacts, module consolidation and final delivery review are honestly pending and are not classified as concealed omissions. The credential incident remains an explicit operational security risk.
- **Recommended path:** `Resolve findings ADH-R6-01 through ADH-R6-06 within the approved architecture before activation. Retain failing behavioral assertions for the uncovered cases, refresh the source freeze, run the required canonical validation, and obtain affected independent assurance. Route ADH-R6-07 to the security and credential owner for explicit disposition. Preserve Pending delivery status until the approved metadata preflight, migration, source-bound activation, assisted provider proof, required gate records and fresh final review are complete.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] ADH-R6-01 A completed correlation prevents the original ACK from improving the operation: In api-app/src/domain/message-templates/template-submission.service.ts:564, recordOutcome updates only SENDING or AMBIGUOUS operations. If reconciliation commits CORRELATED_BY_DEFINITION first, a subsequent valid original ACK cannot update even an identical remote ID. Its readback also requires ACKNOWLEDGED provenance, so the request returns local-incomplete without retaining an ACK receipt, while persisted providerAcceptance remains UNKNOWN. D06 and CR-01 require monotonic enrichment of the same operation. The retained late-ACK test exercises ACK completion before the held recovery response, leaving the inverse ordering unprotected.
  - [high] ADH-R6-02 Contradictory provider read envelopes can authorize submission or certify an observation: api-app/src/integrations/meta/message-template.client.ts:225 accepts every HTTP-success JSON object in readObject. Unlike loadGrant and createTemplate, listTemplates and getTemplate do not reject an error envelope accompanying otherwise plausible data. Consequently HTTP 200 with error plus data:[] passes preflight as proven absence and permits POST; error plus a plausible APPROVED template can become an eligible observation. This violates D05's inconclusive-response prohibition and D07's requirement that provider errors preserve prior observations without fabricating an empty or successful result.
  - [medium] ADH-R6-03 Individual refresh completion loses the draft owner/admin authorization requirement: TemplateObservationService.authorizeDraft initially checks ownership or ADMIN, but ownsLease at api-app/src/domain/message-templates/template-observation.service.ts:314 revalidates only an active actor, active BU and grant existence; its grant query selects userId without role. An administrator refreshing another seller's draft can therefore be downgraded to ATENDENTE during provider I/O and still commit and receive the individual result. The row locks preserve a grant that no longer authorizes that draft-specific operation. D01 and the frozen individual-refresh contract require owner/admin access.
  - [medium] ADH-R6-04 Submission recovery can overwrite text edited while the request was pending: web-app/src/telas/Modelos.tsx:454 and :482 use captured dirty values before replacing the form with authoritative.definition. enviar starts only when dirty is false, while editor fields remain writable until a later response locks the draft. If the seller edits during a held submission and its 503 recovery reads succeed, the old closure still executes setForm and erases those newer edits. Context/editor fences do not detect edits within the same editor. This contradicts D08's monotonic edit protection and the approved preservation of current text.
  - [medium] ADH-R6-05 Failed individual refresh leaves previously approved UI copies eligible: At web-app/src/telas/Modelos.tsx:519, atualizarStatus handles failure by setting an error only. The backend marks the shared observation unavailable and observedEligible=false, but the browser retains its prior APPROVED individualStatus and catalog copies with available=true. Unlike catalog refresh failure, this path does not set a blocking availability flag or reload the persisted observation. The screen can continue displaying eligibility until TTL expiry despite a known current refresh failure, contrary to D07.
  - [medium] ADH-R6-06 Draft and operation GETs omit the shared persisted observation: TemplateDraftService.projectWithOperations returns draft/operation/receipt data at api-app/src/domain/message-templates/template-draft.service.ts:255, and TemplateSubmissionService.projectOperation at :663 likewise omits observations. Opening a draft clears individualStatus in Modelos.tsx:302. Thus an individual PAUSED observation obtained before any catalog page exists cannot be recovered after reload without another provider refresh. D07, the operation GET contract and CR-V11-01 explicitly require draft/catalog/GET/reload projections to derive from the same observation. The browser reload scenario refreshes remotely before asserting individual PAUSED, so its pass does not close this gap.
  - [medium] ADH-R6-07 The disclosed connector credential incident remains operationally unresolved: evidence/executor-startup-secret-redaction-v1.1.json:4 records credential disclosure in rendered startup diagnostics, and its actions record artifact scrubbing and operator notification. The package explicitly states that rotation is unconfirmed and previously rendered output cannot be retracted. These mitigations do not establish credential invalidation. This is a residual operational security issue, not evidence that the template architecture or Meta credentials were compromised, and it must not be silently closed.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
