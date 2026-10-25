# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence142d-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Preserve the approved architecture and supported historical closures. Repair the two bounded defects below within this TODO, then obtain current native browser, API and full ALL evidence plus fresh affected review. The first-send attempt-scoping changes have source support, but Web144 establishes compiler/build/unit proof only. Existing protocol, performance, security, TQA, cutover, final-review and CP6 obligations remain open.`

## Merged Findings
### F-29E19C4E [medium] Post-send metadata failure attributes an intervening reconnect to the wrong read epoch
- **Reviewers:** fresh-internal-no-context-142D
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Capture the reconnect epoch when refreshOrdinaryOptions starts its GET and retain that captured value only if its shared ticket remains current. Apply the same request-start attribution consistently to explicit retry failures. Extend native coverage to hold a post-send metadata read across an actual socket reconnect, then fail it and verify one recovery read, preserved draft, cleared metadata blockage and no additional message POST.
- **Rationale:** Inbox's opening start-options read correctly captures its reconnect epoch at request start, but refreshOrdinaryOptions records metadataReconnectEpochRef.current only when the request fails. If a post-send metadata GET starts at epoch E0, remains pending through a real reconnect E1, then fails, its catch records E1. The reconnect recovery effect subsequently rejects E1 because it is not greater than the recorded failure epoch, losing the recovery opportunity that occurred during that read. This is a residual of the unresolved 111D request-start/recovery obligation. The enclosed reconnect test exercises the opening publisher; the post-send failure test exercises manual retry, leaving this combination unprotected. No runtime reproduction is claimed.

### F-86B65B79 [medium] BFF text normalization bypasses the original-input byte limit and changes valid payloads
- **Reviewers:** fresh-internal-no-context-142D
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Validate text type and nonemptiness without discarding the original Instagram string before policy validation. Enforce the approved byte limit and preserve valid Instagram payloads unchanged while retaining the explicit WhatsApp compatibility contract. Add native cases for over-limit padded text and valid leading/trailing whitespace, checking zero effects on rejection and exact text at the provider HTTP boundary.
- **Rationale:** ConversationsController.responder converts texto with String(...).trim() before passing it to the resolved policy and common sender. Consequently, 1000 ASCII characters followed by a space become a valid 1000-byte message although the submitted text contains 1001 bytes. Valid text with leading or trailing whitespace also reaches dispatch with different content. This conflicts with the human-admitted original-text UTF-8 boundary, whole invalid-draft preservation and exact valid-payload requirements. The new browser cases use unpadded inputs and therefore do not expose this divergence. This is a static finding at the materially changed validation boundary, not a claimed executed failure.

## Reviewer Summaries
### fresh-internal-no-context-142D
- **Assessment:** changes_required
- **Recommended path:** `Preserve the approved architecture and supported historical closures. Repair the two bounded defects below within this TODO, then obtain current native browser, API and full ALL evidence plus fresh affected review. The first-send attempt-scoping changes have source support, but Web144 establishes compiler/build/unit proof only. Existing protocol, performance, security, TQA, cutover, final-review and CP6 obligations remain open.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-ADHERENCE142D-01 BFF text normalization bypasses the original-input byte limit and changes valid payloads: ConversationsController.responder converts texto with String(...).trim() before passing it to the resolved policy and common sender. Consequently, 1000 ASCII characters followed by a space become a valid 1000-byte message although the submitted text contains 1001 bytes. Valid text with leading or trailing whitespace also reaches dispatch with different content. This conflicts with the human-admitted original-text UTF-8 boundary, whole invalid-draft preservation and exact valid-payload requirements. The new browser cases use unpadded inputs and therefore do not expose this divergence. This is a static finding at the materially changed validation boundary, not a claimed executed failure.
  - [medium] IG-ADHERENCE142D-02 Post-send metadata failure attributes an intervening reconnect to the wrong read epoch: Inbox's opening start-options read correctly captures its reconnect epoch at request start, but refreshOrdinaryOptions records metadataReconnectEpochRef.current only when the request fails. If a post-send metadata GET starts at epoch E0, remains pending through a real reconnect E1, then fails, its catch records E1. The reconnect recovery effect subsequently rejects E1 because it is not greater than the recorded failure epoch, losing the recovery opportunity that occurred during that read. This is a residual of the unresolved 111D request-start/recovery obligation. The enclosed reconnect test exercises the opening publisher; the post-send failure test exercises manual retry, leaving this combination unprotected. No runtime reproduction is claimed.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
