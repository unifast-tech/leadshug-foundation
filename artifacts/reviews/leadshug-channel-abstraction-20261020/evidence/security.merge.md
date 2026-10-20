# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/security.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Resolve the response-classification findings within ST-CON-06, preserving the approved architecture, stable refusals, compatibility contracts and existing valid acknowledgement fixtures. Supply the exact local adversarial probes identified below, using provider doubles and disposable PostgreSQL without external attacks. Freeze the corrected candidate and obtain canonical all results bound to those bytes before closing the security gate; retain the separately pending assisted IN/OUT requirement. No new schema, durable intent, lifecycle rewrite or provider integration is warranted. Accepted residual limits remain the D03 local-check-to-network race, D05 crash/unknown-ID recovery limits and D07 observational availability; their recorded ST-CON-04 follow-up is not reopened.`

## Merged Findings
### F-D694BB5A [medium] Required pre-dispatch and cross-tenant attack probes are not evidenced
- **Reviewers:** fresh-no-context-security-reviewer
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Supply existing probe source and candidate-bound results, or add probes within admitted test paths: deny a BFF send without conversation grant and without the required CSRF header; deny a scoped API-key POST to a foreign account with zero provider calls; hold execution after binding, change credential version, generation or pairing epoch separately, then assert CHANNEL_CONTEXT_CHANGED/BLOCKED with zero POSTs and zero OUT writes; overlap sends from two tenants with distinct resources and scoped tokens and assert each exact token/resource pairing and tenant-local persistence. Preserve the separate successful post-dispatch version-only rotation test.
- **Rationale:** This is a bounded evidence gap, not a reproduced vulnerability. The supplied tests demonstrate forged internal ingress rejection, post-dispatch identity/generation changes and permitted post-dispatch credential-version rotation. They do not demonstrate rejection when version or epoch changes after binding but before the adapter's pre-dispatch check. The overlapping-send test uses one BU and the common fixture token, so it cannot expose cross-tenant credential reuse. The supplied public cross-tenant test exercises GET, and no denied BFF send/CSRF-negative mutation probe is shown. These are explicit D02/D03 and Security Risk Assessment attack-simulation obligations; the previous API pass and pending final all do not establish these particular observations.

### F-3C29D038 [medium] Meta can classify a contradictory response as a definite refusal
- **Reviewers:** fresh-no-context-security-reviewer
- **Category:** `security`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Validate the complete single-send response envelope before classifying ACCEPTED or REJECTED. Malformed message entries or contradictory acceptance evidence anywhere in the envelope must produce UNKNOWN/TRANSPORT_UNCONFIRMED. Add a local fetch-double test for an allowlisted refusal with an ID after the first entry, asserting one POST and UNKNOWN, while preserving ordinary allowlisted refusal behavior.
- **Rationale:** Source-only counterexample, not reproduced: meta.client.ts:219-234 examines only messages[0] when checking for an accepted ID. HTTP 400 with a valid allowlisted Graph error and messages:[{}, {id:'accepted-id'}] therefore returns REJECTED, despite an explicit contradictory ID elsewhere in the response. No validation rejects the multi-entry envelope first. Frozen D04 requires malformed or contradictory responses to remain UNKNOWN. The existing contradictory-ID test covers only the first entry. All outbound consumers can consequently receive a false definitive refusal, encouraging a manual resend after an uncertain external effect; no tenant escalation is asserted.

### F-9458C338 [medium] Evolution treats an acknowledgement-free object as proof of an acknowledgement
- **Reviewers:** fresh-no-context-security-reviewer
- **Category:** `security`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Require the supported acknowledgement envelope before returning ACK_WITHOUT_ID; an absent acknowledgement structure must remain UNKNOWN/TRANSPORT_UNCONFIRMED. Preserve the approved key:{} acknowledgement case. Add local tests contrasting 2xx {} with key:{}, asserting one POST in each case and no ambiguous-outbound diagnostic for the malformed response.
- **Rationale:** Source-only counterexample, not reproduced: evolution.client.ts:116-129 accepts any successful HTTP JSON object without a truthy error as ACK_WITHOUT_ID when key is absent. A malformed 2xx body of {} therefore reaches outbound.service.ts:128-145, persists a diagnostic and reports that the channel accepted the send without confirming its ID. HTTP success plus an arbitrary object does not establish the valid acknowledgement required by D04/D05. This does not falsely return send success, but it creates unsupported provider-trust metadata and a persistent diagnostic rather than retaining transport uncertainty.

## Reviewer Summaries
### fresh-no-context-security-reviewer
- **Assessment:** risk=high; attack_simulation=required. Reviewed BFF authorization and session/CSRF composition, public API-key scoping, verified Typebot ingress, Prisma ownership boundaries, identity/generation/epoch/credential fences, operation-local credentials, sender/echo attribution, provider response consumption, destinations, redirects, timeouts, retries and Inbox error rendering. The common outbound design follows the frozen architectural direction; no tenant breakout or credential disclosure was demonstrated. Two source-only provider-response classification defects and a required attack-evidence gap remain. This reviewer performed no execution; neither finding is independently reproduced. The earlier API pass is owner-reported historical evidence, while final frozen all/browser/freshness and assisted IN/OUT remain pending. Threat hypotheses use the owner-supplied OWASP API1 source https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/ and API10 source https://api-security.owasp.org/editions/2023/en/0xaa-unsafe-consumption-of-apis/; they were not independently retrieved.
- **Recommended path:** `Resolve the response-classification findings within ST-CON-06, preserving the approved architecture, stable refusals, compatibility contracts and existing valid acknowledgement fixtures. Supply the exact local adversarial probes identified below, using provider doubles and disposable PostgreSQL without external attacks. Freeze the corrected candidate and obtain canonical all results bound to those bytes before closing the security gate; retain the separately pending assisted IN/OUT requirement. No new schema, durable intent, lifecycle rewrite or provider integration is warranted. Accepted residual limits remain the D03 local-check-to-network race, D05 crash/unknown-ID recovery limits and D07 observational availability; their recorded ST-CON-04 follow-up is not reopened.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] SEC-01 Meta can classify a contradictory response as a definite refusal: Source-only counterexample, not reproduced: meta.client.ts:219-234 examines only messages[0] when checking for an accepted ID. HTTP 400 with a valid allowlisted Graph error and messages:[{}, {id:'accepted-id'}] therefore returns REJECTED, despite an explicit contradictory ID elsewhere in the response. No validation rejects the multi-entry envelope first. Frozen D04 requires malformed or contradictory responses to remain UNKNOWN. The existing contradictory-ID test covers only the first entry. All outbound consumers can consequently receive a false definitive refusal, encouraging a manual resend after an uncertain external effect; no tenant escalation is asserted.
  - [medium] SEC-02 Evolution treats an acknowledgement-free object as proof of an acknowledgement: Source-only counterexample, not reproduced: evolution.client.ts:116-129 accepts any successful HTTP JSON object without a truthy error as ACK_WITHOUT_ID when key is absent. A malformed 2xx body of {} therefore reaches outbound.service.ts:128-145, persists a diagnostic and reports that the channel accepted the send without confirming its ID. HTTP success plus an arbitrary object does not establish the valid acknowledgement required by D04/D05. This does not falsely return send success, but it creates unsupported provider-trust metadata and a persistent diagnostic rather than retaining transport uncertainty.
  - [medium] SEC-03 Required pre-dispatch and cross-tenant attack probes are not evidenced: This is a bounded evidence gap, not a reproduced vulnerability. The supplied tests demonstrate forged internal ingress rejection, post-dispatch identity/generation changes and permitted post-dispatch credential-version rotation. They do not demonstrate rejection when version or epoch changes after binding but before the adapter's pre-dispatch check. The overlapping-send test uses one BU and the common fixture token, so it cannot expose cross-tenant credential reuse. The supplied public cross-tenant test exercises GET, and no denied BFF send/CSRF-negative mutation probe is shown. These are explicit D02/D03 and Security Risk Assessment attack-simulation obligations; the previous API pass and pending final all do not establish these particular observations.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
