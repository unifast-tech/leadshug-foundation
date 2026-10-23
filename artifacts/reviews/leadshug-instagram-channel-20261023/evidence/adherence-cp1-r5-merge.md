# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence-cp1-r5-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Preserve the supported original-defect closures and the invalidated r4 history. Adjudicate the distinct inherited cleanup finding against the approved contract and preservation boundary; this review does not authorize editing immutable adapter files. Preserve cleanup uncertainty until absence or successful exact-resource deletion is proved, and add causal coverage through the real observation boundary. Collect and reconcile terminal full API evidence on the same frozen37sources before closing R1-07/R4-01 or accepting CP1. Retain the source/TODO freeze until both lanes are terminal. CP2–CP6, SEC-R6-04/OPS-R4-01/TQA-ST05-03 restrictions and separately approved real-runtime proof remain required.`

## Merged Findings
### F-EE025E74 [medium] Terminal complete API proof remains pending for the current frozen source
- **Reviewers:** instagram_cp1_adherence_r5
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Collect the validation-only lane's terminal full API receipt, summaries and exact-source/TODO checks. Close this finding and the remaining R4-01 proof obligation only if that evidence establishes the required stable-source result; otherwise preserve every failure and repair it through a later serialized handoff. Do not substitute targeted GREEN or the invalidated r4 observations.
- **Rationale:** The current canonical fixtures retain the15000/60-row datasets, EXPLAIN/query assertions, actual reauthorization transition and staged connection/quarantine/ingress assertions. The source conflict identified in r4's staged connection handler is repaired without granting identity or receipt trust. However, the package supplies only current targeted379unit/25Instagram GREEN; its most recent complete API result is RED on earlier bytes. The new validation-only full API lane was still running when this assessment became terminal. This is missing evidence, not a reviewer-observed current API failure. The new matching source/TODO checks satisfy this review's freeze component but cannot alone close the complete-validation portion of IG-CP1-R4-01.

### F-A153D5D4 [medium] Malformed Evolution observations can release managed cleanup without proving absence
- **Reviewers:** instagram_cp1_adherence_r5
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Keep cleanup pending when observation is inconclusive. Distinguish validated absence from malformed or contradictory responses, or require positively confirmed exact-resource deletion before clearing the fence. Add a causal lifecycle case using the real adapter with synthetic HTTP responses, proving malformed observation preserves the cleanup record and blocks another create while a valid absence/deletion can complete recovery. Obtain explicit source admission before changing the immutable adapter dependency if that repair requires it.
- **Rationale:** EvolutionHttpClient.consultarInstancia at evolution.client.ts:79–84 treats every non-array successful response as an empty inventory and returns null; chamar at :145 also converts invalid JSON to {}. ChannelsService interprets that null as conclusive absence and records CLEANED at channels.service.ts:61, :174 and :484 without successful deletion. Thus a successful HTTP response with malformed or contradictory content can clear CLEANUP_PENDING for an existing managed instance, after which another INITIAL may create a replacement without resolving the old resource. The current staged-unlink repair depends on this shared observation contract, while its fake returns null only for actual inventory absence and does not expose the distinction. The adapter and the older INITIAL null-to-CLEANED behavior predate CP1 and remain byte-exact inherited source; this is not attributed as a CP1-introduced regression. No explicit disposition or waiver of malformed observation semantics was found. It nevertheless limits the current claim that cleanup uncertainty survives until reconciliation.

## Reviewer Summaries
### instagram_cp1_adherence_r5
- **Assessment:** changes_required for bounded CP1. All 37 source hashes and the frozen TODO matched before and after review; all 37 immutable inherited preservation rows also match. The current source supports closure of the original IG-CP1-R1-03 recovery defect: fresh correct proof can recover only the exact current ERROR/IDENTITY_QUARANTINED attempt under provider, BU, channel, generation, epoch, attempt and lease fences; incompatible or cancelled attempts cannot commit recovery. The actual prior-receipt regression preserves the historical receipt and message and accepts the previously rejected key once. The original IG-CP1-R3-02 staged-unlink and stale-snapshot defects are repaired: transactional snapshot comparison precedes cancellation/deletion, and fresh staged unlink retains managed cleanup ownership. Its scheduling wrapper calls the real helper and returns its unchanged DB snapshot. IG-CP1-R3-01 single-create, R3-03 valid wrong-number quarantine, R3-04 actual-winner assertions and ROOT-01 safe staged metadata/retryable503 repairs remain supported on these current bytes. Prior R1-01/02/04/05/06/08 and R2-01/02 closures remain supported, including final-row association constraints and actual historical-schema preservation. A distinct inherited observation weakness still undermines cleanup certainty, as detailed below. R1-07 and the validation component of R4-01 remain open because no terminal full API result was supplied before this review ended. Targeted379unit/25Instagram GREEN and the qualified causal RED receipts do not substitute for it. Architecture, code quality, tests, security, performance, elegance, structural soundness and operational fit were considered. No measured performance conclusion is available. The complete Frontend/Consumer Matrix and normative consumer contracts were considered; CP2–CP6 remain mandatory future checkpoint work without waivers or missing-CP1 UI inference. Additional public source reads comprised the exact28historical migration.sql paths enumerated in instagram-migration.e2e-spec.ts and these dependencies: api-app/src/domain/channels/receipt-attempt-convergence.ts; api-app/src/domain/channels/safe-redaction.ts; api-app/src/domain/inbox/incoming.service.ts; api-app/src/surfaces/bff/channels.controller.ts; api-app/src/integrations/evolution/evolution.client.ts; api-app/src/integrations/evolution/evolution.client.spec.ts. A bounded historical read of channels.service.ts at API baseline db5a86758a165fac8a1ab587599c37b17890530c confirmed the preexisting INITIAL cleanup behavior. No edits, tests, runtime, network or private-input access were performed.
- **Recommended path:** `Preserve the supported original-defect closures and the invalidated r4 history. Adjudicate the distinct inherited cleanup finding against the approved contract and preservation boundary; this review does not authorize editing immutable adapter files. Preserve cleanup uncertainty until absence or successful exact-resource deletion is proved, and add causal coverage through the real observation boundary. Collect and reconcile terminal full API evidence on the same frozen37sources before closing R1-07/R4-01 or accepting CP1. Retain the source/TODO freeze until both lanes are terminal. CP2–CP6, SEC-R6-04/OPS-R4-01/TQA-ST05-03 restrictions and separately approved real-runtime proof remain required.`
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-CP1-R5-01 Malformed Evolution observations can release managed cleanup without proving absence: EvolutionHttpClient.consultarInstancia at evolution.client.ts:79–84 treats every non-array successful response as an empty inventory and returns null; chamar at :145 also converts invalid JSON to {}. ChannelsService interprets that null as conclusive absence and records CLEANED at channels.service.ts:61, :174 and :484 without successful deletion. Thus a successful HTTP response with malformed or contradictory content can clear CLEANUP_PENDING for an existing managed instance, after which another INITIAL may create a replacement without resolving the old resource. The current staged-unlink repair depends on this shared observation contract, while its fake returns null only for actual inventory absence and does not expose the distinction. The adapter and the older INITIAL null-to-CLEANED behavior predate CP1 and remain byte-exact inherited source; this is not attributed as a CP1-introduced regression. No explicit disposition or waiver of malformed observation semantics was found. It nevertheless limits the current claim that cleanup uncertainty survives until reconciliation.
  - [medium] IG-CP1-R1-07 Terminal complete API proof remains pending for the current frozen source: The current canonical fixtures retain the15000/60-row datasets, EXPLAIN/query assertions, actual reauthorization transition and staged connection/quarantine/ingress assertions. The source conflict identified in r4's staged connection handler is repaired without granting identity or receipt trust. However, the package supplies only current targeted379unit/25Instagram GREEN; its most recent complete API result is RED on earlier bytes. The new validation-only full API lane was still running when this assessment became terminal. This is missing evidence, not a reviewer-observed current API failure. The new matching source/TODO checks satisfy this review's freeze component but cannot alone close the complete-validation portion of IG-CP1-R4-01.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

