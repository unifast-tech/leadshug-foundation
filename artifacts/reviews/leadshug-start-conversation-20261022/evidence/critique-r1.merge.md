# PACED Subagent Review Merge: critique

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/critique-r1.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Retain option C, the existing catalogue and acceptance owners, explicit initial resolution, transaction ordering and per-owner ordinary admissions. Resolve the initial acknowledgment deadline contract, record the inherited NOVA_CONVERSA behavior for manually opened conversations, and update the affected validation criteria. Publish any material revision and complete current planning guards before seeking explicit APROVADO. Preserve the recorded ST-CON-05 limits and future approved-asset/runtime proof requirements.`

## Merged Findings
### F-49CD0618 [medium] Initial acknowledgment lacks a consistent deadline predicate
- **Reviewers:** fresh-internal-critique-r1
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Identify the persisted deadline governing initial SENDING claims and freeze the acknowledgment predicate for SENDING-derived AMBIGUOUS attempts. State separately whether confirmed EXTERNAL_ACCEPTED_LOCAL_BLOCKED attempts may be acknowledged earlier. Reconcile the summary, endpoint table, state rules, DoD and validation cases. Test acknowledgment before and after the chosen deadline, successor admission and a late original result. If earlier initial acknowledgment is intentional, record that exception explicitly before approval.
- **Rationale:** The packet summary specifies explicit risk acknowledgment after the dispatch deadline, and the normative ordinary-admission contract enforces that condition. The initial-attempt contract instead permits acknowledgment for AMBIGUOUS or EXTERNAL_ACCEPTED_LOCAL_BLOCKED without identifying an applicable dispatch deadline or requiring it to have passed. A transport timeout can classify an initial attempt as AMBIGUOUS before its lease expires, so the endpoint description permits release while reconciliation would still treat the claim as live. Explicit duplicate-risk confirmation is already required, but the permitted release timing remains inconsistent.

### F-4ACC72C3 [low] Cover first-inbound automation after manual conversation creation
- **Reviewers:** fresh-internal-critique-r1
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Record the expected NOVA_CONVERSA behavior for a manually opened empty conversation and add a focused planned integration case covering open without send followed by the first inbound message. Assert that opening itself invokes no automation. Preserve the delivered trigger predicate unless a different product behavior is explicitly reviewed and admitted.
- **Rationale:** IncomingService passes acceptance.conversationCreated into the NOVA_CONVERSA trigger predicate. Manual open creates the conversation before any Message exists; consequently, the first later inbound message will have conversationCreated=false and will not activate that trigger, including when the operator opened the conversation and abandoned the initial send. This follows the inherited implementation, but the current consumer and validation matrices do not explicitly record this observable consequence of the new journey.

## Reviewer Summaries
### fresh-internal-critique-r1
- **Assessment:** Request a bounded planning clarification before APROVADO. The four architecture-r1 findings are addressed at contract level, and option C preserves coherent ownership and dependency direction. Scope, future validation, private operational boundaries and inherited exceptions are substantially explicit. Initial acknowledgment timing remains inconsistent across the packet, and manual-open effects on existing automation deserve a focused compatibility case. Performance remains unmeasured; the stated budgets and planned PostgreSQL/browser evidence are appropriate. This review grants no execution authority.
- **Recommended path:** `Retain option C, the existing catalogue and acceptance owners, explicit initial resolution, transaction ordering and per-owner ordinary admissions. Resolve the initial acknowledgment deadline contract, record the inherited NOVA_CONVERSA behavior for manually opened conversations, and update the affected validation criteria. Publish any material revision and complete current planning guards before seeking explicit APROVADO. Preserve the recorded ST-CON-05 limits and future approved-asset/runtime proof requirements.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] CR-R1-01 Initial acknowledgment lacks a consistent deadline predicate: The packet summary specifies explicit risk acknowledgment after the dispatch deadline, and the normative ordinary-admission contract enforces that condition. The initial-attempt contract instead permits acknowledgment for AMBIGUOUS or EXTERNAL_ACCEPTED_LOCAL_BLOCKED without identifying an applicable dispatch deadline or requiring it to have passed. A transport timeout can classify an initial attempt as AMBIGUOUS before its lease expires, so the endpoint description permits release while reconciliation would still treat the claim as live. Explicit duplicate-risk confirmation is already required, but the permitted release timing remains inconsistent.
  - [low] CR-R1-02 Cover first-inbound automation after manual conversation creation: IncomingService passes acceptance.conversationCreated into the NOVA_CONVERSA trigger predicate. Manual open creates the conversation before any Message exists; consequently, the first later inbound message will have conversationCreated=false and will not activate that trigger, including when the operator opened the conversation and abandoned the initial send. This follows the inherited implementation, but the current consumer and validation matrices do not explicitly record this observable consequence of the new journey.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

