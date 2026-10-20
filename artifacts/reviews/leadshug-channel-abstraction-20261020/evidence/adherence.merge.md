# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/adherence.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Correct the classifier and browser scenario within the approved D04/D10 boundaries, then review the updated candidate and obtain the required validation evidence. No architectural redesign is indicated.`

## Merged Findings
### F-C3556CEA [high] Meta refusal classification ignores contradictory IDs after the first message
- **Reviewers:** fresh-internal-architecture-reviewer
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Validate the complete relevant response shape before classification and detect contradictory acceptance markers throughout the messages array. Return UNKNOWN/TRANSPORT_UNCONFIRMED for malformed or contradictory payloads. Add direct HTTP-client regression cases for a non-first external ID and a malformed message ID, retaining the one-request invariant.
- **Rationale:** api-app/src/integrations/meta/meta.client.ts:219-234 extracts an ID only from messages[0] and uses its absence to establish REJECTED. HTTP 400 with a valid non-transient Graph error code 100 and messages:[{}, {id:'external-ack'}] therefore becomes REJECTED despite containing a contradictory external ID. A malformed first ID, such as messages:[{id:42}], can also reach REJECTED. Frozen D04 requires malformed or contradictory responses to remain UNKNOWN; a definitive refusal here could encourage an unsafe repeat send.

### F-1055E2F1 [medium] The delayed-response browser scenario loses its return-navigation target
- **Reviewers:** fresh-internal-architecture-reviewer
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Arrange navigation so both conversations remain reachable through the appropriate status tabs. Wait for a unique active-thread selector to confirm B and then A have opened before releasing the held response. Assert that the stale completion preserves a newly entered draft and does not introduce an error, then rerun the complete browser/all gate.
- **Rationale:** web-app/e2e/channel-transport.spec.ts:59-81 first completes an accepted human send, then attempts A→B→A using the Cliente Timeline sidebar button. OutboundService.finalizeOutbound at api-app/src/domain/inbox/outbound.service.ts:233-238 moves A to IN_SERVICE, while Inbox starts on QUEUED and refreshes that filtered list after success. Once refreshed, A is absent from the sidebar, so the return click cannot reliably execute. The line 79 getByText assertion also does not establish that B finished opening: it can match the sidebar alone or become ambiguous with the thread heading. This leaves the required D10 stale-response scenario unreliable.

## Reviewer Summaries
### fresh-internal-architecture-reviewer
- **Assessment:** Changes required. The operation-bound adapters, shared outbound orchestration, scoped resolution and single acceptance owner substantially follow the frozen architecture. A D04 response-classification defect and an unreliable D10 browser scenario remain. Pending final-all, PCV and post-cutover operator evidence are not treated as completed gates.
- **Recommended path:** `Correct the classifier and browser scenario within the approved D04/D10 boundaries, then review the updated candidate and obtain the required validation evidence. No architectural redesign is indicated.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] ADH-01 Meta refusal classification ignores contradictory IDs after the first message: api-app/src/integrations/meta/meta.client.ts:219-234 extracts an ID only from messages[0] and uses its absence to establish REJECTED. HTTP 400 with a valid non-transient Graph error code 100 and messages:[{}, {id:'external-ack'}] therefore becomes REJECTED despite containing a contradictory external ID. A malformed first ID, such as messages:[{id:42}], can also reach REJECTED. Frozen D04 requires malformed or contradictory responses to remain UNKNOWN; a definitive refusal here could encourage an unsafe repeat send.
  - [medium] ADH-02 The delayed-response browser scenario loses its return-navigation target: web-app/e2e/channel-transport.spec.ts:59-81 first completes an accepted human send, then attempts A→B→A using the Cliente Timeline sidebar button. OutboundService.finalizeOutbound at api-app/src/domain/inbox/outbound.service.ts:233-238 moves A to IN_SERVICE, while Inbox starts on QUEUED and refreshes that filtered list after success. Once refreshed, A is absent from the sidebar, so the return click cannot reliably execute. The line 79 getByText assertion also does not establish that B finished opening: it can match the sidebar alone or become ambiguous with the thread heading. This leaves the required D10 stale-response scenario unreliable.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
