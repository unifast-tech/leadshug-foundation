# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/adherence-round2.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Correct the remaining Meta contradiction handling and strengthen the pre-dispatch and stale-response regression probes within existing approved paths. Preserve the current architecture and recorded compatibility limits. Obtain candidate-bound canonical validation and complete the separately required delivery gates before closeout.`

## Merged Findings
### F-32EA8B38 [medium] The stale-response assertions can finish before the Inbox consumes the response
- **Reviewers:** fresh-no-context-architecture-reviewer-round2
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Synchronize with complete response consumption and browser-side handling before evaluating the retained draft and error state. Demonstrate that the scenario fails when the stale-completion generation fence is removed, then run the exact final browser/all candidate.
- **Rationale:** The corrected browser scenario establishes reachable, uniquely opened B and A threads and enters a fresh same-text draft. However, channel-transport.spec.ts:91-96 waits only for Playwright's response event before asserting a value and alert count that already hold before release. That event does not establish completion of api.ts response-body consumption or the Inbox responder continuation. Both assertions can therefore pass before a defective stale continuation clears the draft or changes the error state, leaving the required D10 protection susceptible to a false green.

### F-F7A5ECC3 [medium] The new pre-dispatch probe substitutes the adapter that must enforce the fence
- **Reviewers:** fresh-no-context-architecture-reviewer-round2
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Exercise the shipping bound adapters in negative pre-dispatch probes. A test factory can delegate to the real factory while wrapping its callback to mutate the disposable binding after resolution. Assert CHANNEL_CONTEXT_CHANGED, zero provider calls and zero OUT writes, and ensure removing the shipping callback invocation makes the probe fail.
- **Rationale:** channel-transport.e2e-spec.ts:115-151 exercises the real resolver predicate, but replaces the shipping adapter with FencedDispatchChannel. That test-only channel itself invokes stillCurrent and blocks its synthetic effect. The probe remains green if BoundMetaChannel or BoundEvolutionChannel stops invoking its pre-dispatch callback. It establishes the resolver predicate's behavior without protecting the required D03 connection between that predicate and the actual provider dispatch. The shipping source currently contains the guard; this is a protection-harness gap, not a demonstrated vulnerability.

### F-B3B7CF0B [medium] Meta still accepts an envelope containing an explicit contradictory success flag
- **Reviewers:** fresh-no-context-architecture-reviewer-round2
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Validate explicit success indicators before either positive acknowledgement branch. Contradictory or malformed indicators should produce UNKNOWN/TRANSPORT_UNCONFIRMED. Add raw HTTP regressions for both contradictory envelopes, preserving valid responses without a success field, stable refusals, one POST and the absence of local acceptance or diagnostic writes for unconfirmed transport.
- **Rationale:** In meta.client.ts:225, HTTP 200 with {success:false,messages:[{id:'external-ack'}]} returns ACCEPTED because the positive branch checks only error absence and the message ID. Likewise, {success:false,messages:[{}]} reaches ACK_WITHOUT_ID at lines238-241. The success field is examined only when considering rejection. These contradictory envelopes therefore permit authoritative Message persistence or an acknowledgement diagnostic despite D04 requiring a valid acknowledgement and uncertainty for contradictory responses. This is a new counterexample at the changed classifier locus, distinct from the resolved non-first and malformed-ID cases.

## Reviewer Summaries
### fresh-no-context-architecture-reviewer-round2
- **Assessment:** Changes required within the approved architecture. The operation-bound adapters, common outbound owner, scoped credentials, single MessageAcceptance writer, deterministic selection and preserved consumer contracts remain consistent with D01..10. The original Meta and Evolution counterexamples are corrected. A remaining contradictory-response case and weaknesses in the new D03/D10 protection evidence require remediation. No material performance or elegance regression is apparent from source. This review performed no execution; final all, PCV, dedicated audits, final review and post-activation operator proof remain pending.
- **Recommended path:** `Correct the remaining Meta contradiction handling and strengthen the pre-dispatch and stale-response regression probes within existing approved paths. Preserve the current architecture and recorded compatibility limits. Obtain candidate-bound canonical validation and complete the separately required delivery gates before closeout.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] ADH-R2-01 Meta still accepts an envelope containing an explicit contradictory success flag: In meta.client.ts:225, HTTP 200 with {success:false,messages:[{id:'external-ack'}]} returns ACCEPTED because the positive branch checks only error absence and the message ID. Likewise, {success:false,messages:[{}]} reaches ACK_WITHOUT_ID at lines238-241. The success field is examined only when considering rejection. These contradictory envelopes therefore permit authoritative Message persistence or an acknowledgement diagnostic despite D04 requiring a valid acknowledgement and uncertainty for contradictory responses. This is a new counterexample at the changed classifier locus, distinct from the resolved non-first and malformed-ID cases.
  - [medium] ADH-R2-02 The stale-response assertions can finish before the Inbox consumes the response: The corrected browser scenario establishes reachable, uniquely opened B and A threads and enters a fresh same-text draft. However, channel-transport.spec.ts:91-96 waits only for Playwright's response event before asserting a value and alert count that already hold before release. That event does not establish completion of api.ts response-body consumption or the Inbox responder continuation. Both assertions can therefore pass before a defective stale continuation clears the draft or changes the error state, leaving the required D10 protection susceptible to a false green.
  - [medium] ADH-R2-03 The new pre-dispatch probe substitutes the adapter that must enforce the fence: channel-transport.e2e-spec.ts:115-151 exercises the real resolver predicate, but replaces the shipping adapter with FencedDispatchChannel. That test-only channel itself invokes stillCurrent and blocks its synthetic effect. The probe remains green if BoundMetaChannel or BoundEvolutionChannel stops invoking its pre-dispatch callback. It establishes the resolver predicate's behavior without protecting the required D03 connection between that predicate and the actual provider dispatch. The shipping source currently contains the guard; this is a protection-harness gap, not a demonstrated vulnerability.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
