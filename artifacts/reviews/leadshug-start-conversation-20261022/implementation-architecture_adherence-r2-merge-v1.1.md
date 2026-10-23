# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-architecture_adherence-r2-dispatch-v1.1.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `Resolve these findings within the current TODO, add focused regressions and refresh affected validation and review evidence. Then proceed through separately authorized preserved-local activation, source/image verification, migration preflight and assisted channel proof. DOD-11/12/13, module consolidation and the canonical diff guard remain open gates.`

## Merged Findings
### F-91766E02 [medium] Initial preview ignores per-template observation availability
- **Reviewers:** fresh-bounded-architecture-reviewer-r2
- **Category:** `adherence`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Require the selected observation's availability in preview and new-attempt preparation without using supported or eligible as initial-send support flags. Add a producer-to-consumer regression with a fresh catalog page, an unavailable APPROVED observation and zero dispatch; retain positive POSITIONAL coverage with supported=false and available=true.
- **Rationale:** TemplateObservationService can mark an individual observation unavailable while retaining its APPROVED status and leaving its catalog page fresh and available. getCatalog then returns page.available=true with item.available=false. InitialMessageService.preview and submit check page availability and item status, but never item.available. They therefore accept an observation that the preserved ST05 owner explicitly reports unavailable, contrary to the normative requirement to consume observation freshness and availability independently of authoring support flags. Fresh dispatch revalidation reduces external risk but does not correct this local consumer divergence.

### F-9D491F93 [medium] Changing BU during manual open can leave the dialog permanently busy
- **Reviewers:** fresh-bounded-architecture-reviewer-r2
- **Category:** `operational_fit`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Give the dialog fresh state when its BU changes, for example through BU-keyed mounting, while retaining the late-response fence. Add a browser regression that holds an actual open response, changes BU and verifies that the current dialog remains usable and the previous response cannot open a conversation.
- **Rationale:** Inbox keeps the same NovaConversa instance mounted when trocarBu changes buId. NovaConversa advances openGeneration, but retains saving=true from an outstanding request. The old request's finally deliberately skips setSaving(false) after that generation change. Its late response is safely ignored, but both the submit and Fechar buttons remain disabled in the new BU, leaving the dialog unusable.

### F-2A26268E [medium] Admission persistence failures can erase ordinary transport outcomes
- **Reviewers:** fresh-bounded-architecture-reviewer-r2
- **Category:** `adherence`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Preserve the established transport outcome and diagnostic handling when admission persistence fails, while retaining conservative exclusion and avoiding provider retries. Add fault cases for settlement/release exceptions after UNKNOWN, ACK_WITHOUT_ID and definitive refusal; verify safe response metadata, diagnostic persistence and unchanged provider counters.
- **Rationale:** OutboundService.send handles settlement failure for the corrected ACCEPTED success path, but its BLOCKED, REJECTED and UNKNOWN branches still await settleOrdinary or releasePrepared without protecting the established transport result. An inconclusive admission write/readback can therefore escape as ADMISSION_COMMIT_UNCONFIRMED or another exception without the required outcome/evidence. For ACK_WITHOUT_ID, it also prevents finishUnknown from executing the preserved diagnostic path. This diverges from SCOPE-09 and D-07 caller compatibility.

## Reviewer Summaries
### fresh-bounded-architecture-reviewer-r2
- **Assessment:** Changes required. The core implementation preserves the approved transport, acceptance, catalog and recovery owners. The visible r1 corrections and terminal E54 evidence support the candidate, but three remaining failure-path and consumer gaps need correction. The activation proposal preserves existing data and keeps approval boundaries explicit; activation and final delivery remain unproven.
- **Recommended path:** `Resolve these findings within the current TODO, add focused regressions and refresh affected validation and review evidence. Then proceed through separately authorized preserved-local activation, source/image verification, migration preflight and assisted channel proof. DOD-11/12/13, module consolidation and the canonical diff guard remain open gates.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] ARCH-ST04-R2-01 Admission persistence failures can erase ordinary transport outcomes: OutboundService.send handles settlement failure for the corrected ACCEPTED success path, but its BLOCKED, REJECTED and UNKNOWN branches still await settleOrdinary or releasePrepared without protecting the established transport result. An inconclusive admission write/readback can therefore escape as ADMISSION_COMMIT_UNCONFIRMED or another exception without the required outcome/evidence. For ACK_WITHOUT_ID, it also prevents finishUnknown from executing the preserved diagnostic path. This diverges from SCOPE-09 and D-07 caller compatibility.
  - [medium] ARCH-ST04-R2-02 Changing BU during manual open can leave the dialog permanently busy: Inbox keeps the same NovaConversa instance mounted when trocarBu changes buId. NovaConversa advances openGeneration, but retains saving=true from an outstanding request. The old request's finally deliberately skips setSaving(false) after that generation change. Its late response is safely ignored, but both the submit and Fechar buttons remain disabled in the new BU, leaving the dialog unusable.
  - [medium] ARCH-ST04-R2-03 Initial preview ignores per-template observation availability: TemplateObservationService can mark an individual observation unavailable while retaining its APPROVED status and leaving its catalog page fresh and available. getCatalog then returns page.available=true with item.available=false. InitialMessageService.preview and submit check page availability and item status, but never item.available. They therefore accept an observation that the preserved ST05 owner explicitly reports unavailable, contrary to the normative requirement to consume observation freshness and availability independently of authoring support flags. Fresh dispatch revalidation reduces external risk but does not correct this local consumer divergence.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

