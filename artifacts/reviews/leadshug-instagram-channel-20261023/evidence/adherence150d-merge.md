# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence150d-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Preserve the approved architecture. API146 preserves original text, and Web147 captures reconnect epochs at read start under current tickets. Correct the two browser protection defects and the remaining unmount continuation under existing 111D04, then obtain current compiler, native browser and full ALL evidence with fresh affected review. API148 is in progress; no result is inferred. Existing primary-protocol, security, performance, TQA, cutover, final-review and CP6 obligations remain open.`

## Merged Findings
### F-C7FA36AD [medium] The padded-text test still encounters an ambiguous normalized locator before its exact oracle
- **Reviewers:** fresh-internal-no-context-150D
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use the returned message UUID for the preliminary visibility assertion as well as the existing raw text equality assertion. Retain every valid/invalid boundary, exact provider payload check and zero-effect assertion.
- **Rationale:** The valid-text loop still calls expect(page.locator('.bolha').filter({ hasText: text })).toBeVisible() before checking the returned message UUID. For the padded sample, whitespace normalization reduces the match to 992 consecutive ASCII characters, which also occur in previously sent 1000-character and 997-character messages. The broad locator can therefore match multiple bubbles and fail before the UUID-specific raw text assertion or final provider trace checks. This contradicts the package's claimed removal of normalized substring ambiguity.

### F-61E5F5C2 [medium] Independent Instagram browser cases reuse an account already owned by another BU
- **Reviewers:** fresh-internal-no-context-150D
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Give independently seeded cases distinct synthetic account identities and corresponding fake grants. Preserve same-account continuity within each case, the two-account/same-peer checks, durable ownership constraints and exact provider counters; then execute the complete browser suite together.
- **Rationale:** Multiple cases call seed(), which creates a new tenant and BU, then connectAccount(..., 'a'), which always authorizes timeline-ig-account-a under the same configured Instagram app. The enclosed fixture retains prior database rows and provides no per-case ownership cleanup or account namespace change. After the first successful connection, the approved durable cross-BU resource ownership invariant requires subsequent connections of that account to fail. This prevents the complete browser suite from reaching its intended recovery and isolation assertions. This is a static test-isolation defect, not an observed runtime failure.

### F-7A0496A3 [medium] Explicit reply-options refresh can continue reading after its owner unmounts
- **Reviewers:** fresh-internal-no-context-150D
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Recheck mounted state and the captured options ticket immediately after the awaited parent refresh, before issuing the follow-up GET. Fence parent ticket allocation/acceptance after unmount and invalidate outstanding ownership during cleanup. Add a held-read navigation case proving that the obsolete continuation issues no follow-up read and cannot publish state.
- **Rationale:** The recorded 111D04 repair path remains open through source134/147 and native/fullALL review. InstagramReplyComposer.refreshOptions awaits onOutcomeNeedsReview(), then unconditionally starts inboxApi.replyOptions(). If navigation unmounts the composer during the first read, cleanup invalidates its options ticket, but that ticket and mounted state are checked only after the follow-up GET finishes. The publication fence protects local state while leaving the explicitly prohibited stale continuation active. Inbox.beginStartOptionsRead and startOptionsTicketIsCurrent also omit mounted-state eligibility. No incorrect provider dispatch or runtime reproduction is claimed.

## Reviewer Summaries
### fresh-internal-no-context-150D
- **Assessment:** changes_required
- **Recommended path:** `Preserve the approved architecture. API146 preserves original text, and Web147 captures reconnect epochs at read start under current tickets. Correct the two browser protection defects and the remaining unmount continuation under existing 111D04, then obtain current compiler, native browser and full ALL evidence with fresh affected review. API148 is in progress; no result is inferred. Existing primary-protocol, security, performance, TQA, cutover, final-review and CP6 obligations remain open.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-ADHERENCE150D-01 Independent Instagram browser cases reuse an account already owned by another BU: Multiple cases call seed(), which creates a new tenant and BU, then connectAccount(..., 'a'), which always authorizes timeline-ig-account-a under the same configured Instagram app. The enclosed fixture retains prior database rows and provides no per-case ownership cleanup or account namespace change. After the first successful connection, the approved durable cross-BU resource ownership invariant requires subsequent connections of that account to fail. This prevents the complete browser suite from reaching its intended recovery and isolation assertions. This is a static test-isolation defect, not an observed runtime failure.
  - [medium] IG-ADHERENCE150D-02 The padded-text test still encounters an ambiguous normalized locator before its exact oracle: The valid-text loop still calls expect(page.locator('.bolha').filter({ hasText: text })).toBeVisible() before checking the returned message UUID. For the padded sample, whitespace normalization reduces the match to 992 consecutive ASCII characters, which also occur in previously sent 1000-character and 997-character messages. The broad locator can therefore match multiple bubbles and fail before the UUID-specific raw text assertion or final provider trace checks. This contradicts the package's claimed removal of normalized substring ambiguity.
  - [medium] IG-ADHERENCE111D-04 Explicit reply-options refresh can continue reading after its owner unmounts: The recorded 111D04 repair path remains open through source134/147 and native/fullALL review. InstagramReplyComposer.refreshOptions awaits onOutcomeNeedsReview(), then unconditionally starts inboxApi.replyOptions(). If navigation unmounts the composer during the first read, cleanup invalidates its options ticket, but that ticket and mounted state are checked only after the follow-up GET finishes. The publication fence protects local state while leaving the explicitly prohibited stale continuation active. Inbox.beginStartOptionsRead and startOptionsTicketIsCurrent also omit mounted-state eligibility. No incorrect provider dispatch or runtime reproduction is claimed.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
