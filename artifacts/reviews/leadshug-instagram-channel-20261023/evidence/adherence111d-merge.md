# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence111d-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Repair the findings within the approved TODO, preserve existing policy exceptions and recovery invariants, and obtain native behavioral coverage followed by current canonical ALL/browser validation. Keep the recorded primary-protocol, assurance, human-admission and CP6 gates open. This complementary review covers enclosed bodies; the browser-server implementation is represented only by metadata and cannot be independently certified here. No previously closed finding is reopened.`

## Merged Findings
### F-72B20E9F [high] The channel gateway rejects valid Instagram webhook bodies above 2 MiB
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Apply the approved 8 MiB ceiling specifically to the effective Instagram webhook paths while preserving other route limits. Exercise the actual disposable gateway with valid bodies above 2 MiB, at the permitted boundary, and above 8 MiB; verify rejection produces no domain effects.
- **Rationale:** The frozen contract permits Instagram webhook bodies up to 8 MiB and requires that ceiling specifically at the parser and gateway. The enclosed gateway sets client_max_body_size 2m for the server, while /webhooks/ has no Instagram override. Valid bodies between 2 and 8 MiB therefore receive 413 before reaching authenticated ingress. The native HTTPS browser harness does not establish this Nginx boundary.

### F-E6D7EC37 [medium] Uncertain authorization creation has no usable recovery path
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Retain the actor/BU/binding-qualified creation key and body before dispatch. Provide explicit recovery through replay of that same idempotent creation request, then consult the returned safe attempt ID. Clear uncertainty only after a conclusive observation. Cover a response lost after durable creation without creating another attempt.
- **Rationale:** InstagramConnections.begin generates its creation key inside the request and retains neither that key nor the creation intent after a lost response. It sets creationUncertain, permanently disabling connection and reauthorization actions for the mounted component. Atualizar conexões only reads catalog/capabilities and cannot recover the attempt or clear this state. Reloading loses the uncertainty and generates a different key. The instruction to consult the attempt is therefore unactionable precisely when the response containing its ID was lost.

### F-E0F9CD4E [medium] Textarea maxlength reduces the approved Unicode character limits
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Make interactive input enforce the existing code-point limits consistently with the server and draft owner. Preserve Instagram 1000 characters and WhatsApp 4096 characters. Add native supplementary-plane input and boundary coverage without applying the pending byte-limit proposal.
- **Rationale:** The controller and draft helpers count Unicode code points using Array.from or spread syntax, but the reply textarea also applies HTML maxLength, which counts UTF-16 code units. Consequently, users can enter only 500 supplementary-plane characters under Instagram's 1000 setting, and only 2048 under WhatsApp's 4096 setting. This reduces both current character contracts independently of the unapplied UTF-8-byte proposal; the enclosed boundary tests use ASCII and miss the discrepancy.

### F-5DADB457 [medium] Ordinary recovery state survives replacement of its admission
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Bind the recovery component's state lifetime to admission.id, or explicitly reset all admission-owned state on replacement while retaining stale-result fencing. Test replacement during a held recovery response and require a fresh risk confirmation for the replacement admission.
- **Rationale:** Inbox keys OrdinaryRecovery by actor/BU/conversation/navigation but omits admission.id. When another ordinary admission becomes selected, the component increments actionOwner without resetting busy, confirmRisk or notices. If replacement occurs during an outstanding action, the stale finally refuses to clear busy, leaving the new admission's controls disabled. A checked risk confirmation can also carry from the previous admission. Multiple ordinary admissions are expressly preserved by the approved concurrency contract.

### F-AAEE3018 [medium] Inbox discards conversation-list continuation
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Consume the existing bounded pagination contract with actor/BU/filter/navigation ownership and explicit continuation controls. Preserve page-size and query budgets, and prove access beyond the first 50 conversations through the real BFF and PostgreSQL.
- **Rationale:** The producer returns total, pagina and temMais and accepts pagina/limite. Inbox requests only the default page, retains only conversations, and renders no continuation control. Once a filter contains more than 50 conversations, older Instagram conversations cannot be reached through this consumer. Instagram also has no approved phone-based Consultar alternative. This leaves the declared Inbox pagination consumer incomplete.

### F-BCD09DF2 [medium] Failed admission metadata can enable the ordinary composer
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Keep admission metadata explicitly unresolved after failure and retain a blocked send surface with an actionable refresh/reconnect path. Enable the appropriate composer or recovery controls only after a current successful start-options observation. Add native coverage with an existing active admission and a failed metadata read.
- **Rationale:** When start-options fails, Inbox sets startOptionsFor to the current conversation but leaves startOptions null. For a nonempty conversation, startOptionsLoading then becomes false and the final rendering branch mounts an unblocked InstagramReplyComposer. A successful reply-options read can enable sending although the initial/ordinary admission state remains unknown. Backend fences may refuse the request, but the consumer has bypassed its required admission-state protection and recovery presentation.

### F-42685ECA [medium] Admission-state publishers do not share request-start ordering
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Allocate admission-read ownership when each request starts and require every publisher to carry that ownership through completion. Invalidate preceding reads at the relevant action boundary. Prove that an older actual BFF response cannot overwrite a newer admission observation or enable sending.
- **Rationale:** Parent start-options requests capture startOptionsIntent before awaiting, but PrimeiraMensagem.reloadOptions and OrdinaryRecovery.refresh publish through receiveOptions without that ticket. receiveOptions increments the parent clock when the response arrives. An older held recovery read can therefore overwrite a newer observation or invalidate a newer request still in flight. Actor, navigation and conversation checks do not prevent this same-context stale publication, which can hide a newer admission or restore obsolete recovery state.

### F-5BFC3E1C [low] Typing copies the entire retained draft index
- **Reviewers:** fresh-internal-no-context-111D
- **Category:** `performance`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use keyed updates and conversation-scoped lookup within the existing draft owner while preserving approved prior-binding draft access and revision fences. Measure the resulting behavior with a representative retained-draft cohort before asserting frontend performance acceptance.
- **Rationale:** Each changeText call invokes updateDraft, which spreads every retained draft, and then Object.assign copies that entire result back into the module-global store. Prior-draft rendering also scans the global store, including on the composer's one-second clock updates. Since records remain across conversations and binding revisions, active typing and rendering costs grow with accumulated session history. This is a static complexity finding; no measured latency failure is established.

## Reviewer Summaries
### fresh-internal-no-context-111D
- **Assessment:** changes_required
- **Recommended path:** `Repair the findings within the approved TODO, preserve existing policy exceptions and recovery invariants, and obtain native behavioral coverage followed by current canonical ALL/browser validation. Keep the recorded primary-protocol, assurance, human-admission and CP6 gates open. This complementary review covers enclosed bodies; the browser-server implementation is represented only by metadata and cannot be independently certified here. No previously closed finding is reopened.`
- **Performance:** `mixed`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] IG-ADHERENCE111D-01 The channel gateway rejects valid Instagram webhook bodies above 2 MiB: The frozen contract permits Instagram webhook bodies up to 8 MiB and requires that ceiling specifically at the parser and gateway. The enclosed gateway sets client_max_body_size 2m for the server, while /webhooks/ has no Instagram override. Valid bodies between 2 and 8 MiB therefore receive 413 before reaching authenticated ingress. The native HTTPS browser harness does not establish this Nginx boundary.
  - [medium] IG-ADHERENCE111D-02 Inbox discards conversation-list continuation: The producer returns total, pagina and temMais and accepts pagina/limite. Inbox requests only the default page, retains only conversations, and renders no continuation control. Once a filter contains more than 50 conversations, older Instagram conversations cannot be reached through this consumer. Instagram also has no approved phone-based Consultar alternative. This leaves the declared Inbox pagination consumer incomplete.
  - [medium] IG-ADHERENCE111D-03 Failed admission metadata can enable the ordinary composer: When start-options fails, Inbox sets startOptionsFor to the current conversation but leaves startOptions null. For a nonempty conversation, startOptionsLoading then becomes false and the final rendering branch mounts an unblocked InstagramReplyComposer. A successful reply-options read can enable sending although the initial/ordinary admission state remains unknown. Backend fences may refuse the request, but the consumer has bypassed its required admission-state protection and recovery presentation.
  - [medium] IG-ADHERENCE111D-04 Admission-state publishers do not share request-start ordering: Parent start-options requests capture startOptionsIntent before awaiting, but PrimeiraMensagem.reloadOptions and OrdinaryRecovery.refresh publish through receiveOptions without that ticket. receiveOptions increments the parent clock when the response arrives. An older held recovery read can therefore overwrite a newer observation or invalidate a newer request still in flight. Actor, navigation and conversation checks do not prevent this same-context stale publication, which can hide a newer admission or restore obsolete recovery state.
  - [medium] IG-ADHERENCE111D-05 Ordinary recovery state survives replacement of its admission: Inbox keys OrdinaryRecovery by actor/BU/conversation/navigation but omits admission.id. When another ordinary admission becomes selected, the component increments actionOwner without resetting busy, confirmRisk or notices. If replacement occurs during an outstanding action, the stale finally refuses to clear busy, leaving the new admission's controls disabled. A checked risk confirmation can also carry from the previous admission. Multiple ordinary admissions are expressly preserved by the approved concurrency contract.
  - [medium] IG-ADHERENCE111D-06 Uncertain authorization creation has no usable recovery path: InstagramConnections.begin generates its creation key inside the request and retains neither that key nor the creation intent after a lost response. It sets creationUncertain, permanently disabling connection and reauthorization actions for the mounted component. Atualizar conexões only reads catalog/capabilities and cannot recover the attempt or clear this state. Reloading loses the uncertainty and generates a different key. The instruction to consult the attempt is therefore unactionable precisely when the response containing its ID was lost.
  - [medium] IG-ADHERENCE111D-07 Textarea maxlength reduces the approved Unicode character limits: The controller and draft helpers count Unicode code points using Array.from or spread syntax, but the reply textarea also applies HTML maxLength, which counts UTF-16 code units. Consequently, users can enter only 500 supplementary-plane characters under Instagram's 1000 setting, and only 2048 under WhatsApp's 4096 setting. This reduces both current character contracts independently of the unapplied UTF-8-byte proposal; the enclosed boundary tests use ASCII and miss the discrepancy.
  - [low] IG-ADHERENCE111D-08 Typing copies the entire retained draft index: Each changeText call invokes updateDraft, which spreads every retained draft, and then Object.assign copies that entire result back into the module-global store. Prior-draft rendering also scans the global store, including on the composer's one-second clock updates. Since records remain across conversations and binding revisions, active typing and rendering costs grow with accumulated session history. This is a static complexity finding; no measured latency failure is established.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
