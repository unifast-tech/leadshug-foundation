# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/security-round2.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `Repair the pre-dispatch tests to exercise the production adapters and synchronize the delayed-response browser assertions with application processing. These are changes within the approved protection harness, requiring no redesign or new product capability. Obtain candidate-bound validation and reconverge review before closing the findings. Preserve the pending delivery gates and the approved local-check-to-network, crash recovery, null-ID deduplication and observational availability limits; fixtures cannot establish external readiness.`

## Merged Findings
### F-BA9C5EC6 [medium] Pre-dispatch probes substitute the adapter that must enforce the fence
- **Reviewers:** fresh-no-context-security-reconvergence-reviewer
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Place the mutation immediately before delegation to a Channel created by the production MetaChannelFactory, retaining the real resolver callback and injected provider double. Assert BLOCKED/CHANNEL_CONTEXT_CHANGED, zero provider invocations and zero OUT writes for each mutation. Protect the Evolution adapter's invocation of the same fence as well. The scenarios should fail if the production adapter omits its check.
- **Rationale:** channel-transport.e2e-spec.ts:30-50 implements the pre-dispatch check inside FencedDispatchChannel, and lines 115-151 replace the production registry with that implementation. The probes exercise the real resolver callback and PostgreSQL changes, but would remain green if BoundMetaChannel stopped invoking beforeDispatch. Zero provider-client calls are also inherent in this substitute. Source inspection shows the production check exists today; this is a protection gap in the newly added D03/R04 scenario, not a demonstrated vulnerability.

### F-DFF7AA8A [medium] Draft preservation can be asserted before the stale completion is processed
- **Reviewers:** fresh-no-context-security-reconvergence-reviewer
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Synchronize with completion of the original response body and its browser-side application processing before checking the retained draft and absent alert. Use a deterministic completion signal without adding production DTO fields or arbitrary sleeps, and verify that removing the generation guard makes this scenario fail.
- **Rationale:** web-app/e2e/channel-transport.spec.ts:90-96 enters the replacement draft before releasing the response, then waits only for the response event and status. That event does not establish completion of api.ts body consumption or Inbox's continuation. Both assertions already hold before release, so they can pass before an unfenced continuation clears the same-text draft. The navigation correction is sound, but the changed scenario still lacks reliable evidence that the draft survives application processing.

## Reviewer Summaries
### fresh-no-context-security-reconvergence-reviewer
- **Assessment:** Changes required in two protection scenarios. The supplied implementation follows the approved domain port, operation-scoped adapters, common orchestration and sole MessageAcceptance owner. The original Meta and Evolution classifier counterexamples are corrected without architectural expansion. Reviewed surfaces include BFF session/CSRF/BU authorization, public API-key ownership, verified bot ingress, credential and identity fences, concurrent credential isolation, provider response trust, redirects, retries, error rendering and acceptance provenance. Security risk remains high; attack simulation is required. The owner-supplied OWASP API1 and API10 references informed authorization and provider-consumption hypotheses; they were not independently retrieved. No execution, exploit reproduction, tenant breakout or credential disclosure is established by this review. API results are writer-reported, and final all/browser, PCV, dedicated audits and post-activation operator IN/OUT remain pending. Performance is acceptable at source level: metadata remains batched and dispatch adds no external probes or retries; measured performance is not certified.
- **Recommended path:** `Repair the pre-dispatch tests to exercise the production adapters and synchronize the delayed-response browser assertions with application processing. These are changes within the approved protection harness, requiring no redesign or new product capability. Obtain candidate-bound validation and reconverge review before closing the findings. Preserve the pending delivery gates and the approved local-check-to-network, crash recovery, null-ID deduplication and observational availability limits; fixtures cannot establish external readiness.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] ADH-R2-01 Pre-dispatch probes substitute the adapter that must enforce the fence: channel-transport.e2e-spec.ts:30-50 implements the pre-dispatch check inside FencedDispatchChannel, and lines 115-151 replace the production registry with that implementation. The probes exercise the real resolver callback and PostgreSQL changes, but would remain green if BoundMetaChannel stopped invoking beforeDispatch. Zero provider-client calls are also inherent in this substitute. Source inspection shows the production check exists today; this is a protection gap in the newly added D03/R04 scenario, not a demonstrated vulnerability.
  - [medium] ADH-R2-02 Draft preservation can be asserted before the stale completion is processed: web-app/e2e/channel-transport.spec.ts:90-96 enters the replacement draft before releasing the response, then waits only for the response event and status. That event does not establish completion of api.ts body consumption or Inbox's continuation. Both assertions already hold before release, so they can pass before an unfenced continuation clears the same-text draft. The navigation correction is sound, but the changed scenario still lacks reliable evidence that the draft survives application processing.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
