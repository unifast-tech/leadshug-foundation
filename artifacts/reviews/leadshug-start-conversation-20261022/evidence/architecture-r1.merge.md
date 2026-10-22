# PACED Subagent Review Merge: architecture_opinion

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/architecture-r1.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Choose C: one discriminated Channel.sendMessage, declared supportedKinds, an explicit initial-selection resolver contract, one per-attempt dispatch fence, inbox orchestration composing management and transport, and transaction collaboration through the existing MessageAcceptanceService and common Outbound finalizer. A could preserve ownership but adds a second abstract operation without reducing provider I/O. B, as described, violates scoped resolution and common acceptance. C offers the smallest faithful ownership graph. Its main tradeoff is widening adapter/fake contracts and adding bounded preflight and admission costs to preserve safe external dispatch. Resolve these finite contracts before implementation; retain the existing catalogue owner, local-only initial recovery, and explicit external uncertainty.`

## Merged Findings
### F-E3C20901 [high] Ordinary-dispatch admission has no safe expiry and takeover contract
- **Reviewers:** fresh-internal-architecture-r1
- **Category:** `architecture`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Freeze one bounded admission design: ordinary sends receive owner-specific admission tokens under the same conversation transaction that reserves the exclusive initial slot; initial reservation conflicts with every outstanding ordinary token. Preserve ordinary-versus-ordinary behavior unless an explicit compatibility change is reviewed. Define pre-POST token validation, deadlines, owner-CAS release and commit certainty. Expiry may safely clear proven undispatched admissions; uncertain dispatched admissions must continue blocking initial reservation until settlement or an explicitly reviewed duplicate-risk release. Add barriers for both admission orderings, process suspension, timeout, expired tokens and late release. Keep database locks outside HTTP.
- **Rationale:** The proposed interlock correctly rejects an early SELECT as sufficient, but still leaves conversation locking versus a dispatch lease unresolved. A bounded logical claim does not establish exclusion after expiry: an ordinary request may remain pending externally or resume before POST while an initial attempt reserves the conversation. A local lease cannot fence the provider. A single exclusive lease could also change ordinary-versus-ordinary behavior despite D-07 preserving callers without an initial slot. These are central correctness and operational questions, not global idempotency requirements.

### F-2D3CB947 [high] Acceptance mutates the token needed by the proposed finalization CAS
- **Reviewers:** fresh-internal-architecture-r1
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Freeze a short transaction sequence that evaluates the original conversation CAS while holding the row lock and before acceptance's own conversation mutation. Preserve concurrent claim/close outcomes without refreshing the expected timestamp. A failed status/owner CAS should skip those effects while permitting otherwise eligible keyed Message acceptance. Keep the known external receipt committed separately, then atomically record Message acceptance, attempt completion and slot release. Define bounded whole-local-transaction recovery for unique conflicts and commit-ACK loss, with no repeated provider call. Retain accept as the existing wrapper over the same owner primitive. Explicitly admit and baseline message-acceptance.service.ts before approval.
- **Rationale:** The packet proposes one local acceptance/finalization transaction but does not settle its ordering. Existing MessageAcceptanceService.loadOutboundConversation updates lastMessageAt and therefore Conversation.updatedAt before returning. Calling that primitive and then applying the prescribed pre-HTTP updatedAt CAS would invalidate the CAS through the initial flow's own write. Echo-first acceptance can also change that timestamp and must not justify refreshing the captured baseline. Additionally, the existing acceptance wrapper handles unique conflicts after transaction rollback; that recovery cannot simply be moved inside an already-aborted caller transaction. The strict path contract also admits the acceptance spec but omits message-acceptance.service.ts itself.

### F-E2F76277 [medium] POSITIONAL sending needs an explicit consumption contract for the inherited catalogue
- **Reviewers:** fresh-internal-architecture-r1
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Define initial-send eligibility and descriptor fingerprinting over the existing TemplateSummary components and parameterFormat, preserving ST-CON-05 catalogue DTOs and authoring flags. The bounded initial renderer should validate static header/footer, exact NAMED keys or contiguous POSITIONAL 1..N values, and exact supported semantics before producing its context-bound fingerprint. State explicitly that inherited supported/eligible flags do not authorize or fully describe initial-send support. Plan end-to-end POSITIONAL cases through catalogue selection, local preview, fresh same-account validation and raw send ordering. If shared parser changes prove necessary, admit and review those exact changes before approval.
- **Rationale:** SCOPE-06 promises NAMED and POSITIONAL sending while preserving the delivered catalogue/parser. The embedded parseTemplateSummary marks every POSITIONAL template unsupported and assigns a null semanticFingerprint; the shared projector consequently reports it ineligible. Its components and parameterFormat remain available, so preserving ST-CON-05 is feasible, but the packet does not specify how initial-send support and fingerprints differ from the inherited authoring-oriented flags. Reusing those flags would exclude the promised POSITIONAL path; ignoring them without a declared validator would weaken exact-definition checking.

### F-0715A55A [medium] Explicit initial resolution and descriptor-to-fence binding remain unspecified
- **Reviewers:** fresh-internal-architecture-r1
- **Category:** `architecture`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Specify the narrow initial resolver reference and common dispatch input before freeze: explicit selected channel, expected immutable context, discriminated payload and required initial-attempt fence. Bind the selected channel without applying free-text policy to approved-template payloads. Require exact equality between validated management context and transport context, including opaque account reference, resource identity, generation, epoch and credential version. Bind template semantics and parameter values to that descriptor. Complete remote reads first, then validate current authorization, payload and applicable trusted text window in the claim transaction. Define preflight/fence failures as proven non-dispatch outcomes and test closed-window template success, text-window expiry during preflight and mismatched descriptor contexts.
- **Rationale:** The delivered resolveForConversation selects conversational origin and enforces the text window before binding; OutboundService repeats that window check. Neither delivered resolver entry point represents a manually selected initial channel carrying an approved-template payload outside the window. Widening sendMessage alone therefore cannot provide the journey. The proposed immutable descriptor also lacks a concrete contract joining management validation to the exact transport resource, opaque account reference and credential version. The final fence's enumerated checks omit an explicit text-window recheck after potentially lengthy preflight.

## Reviewer Summaries
### fresh-internal-architecture-r1
- **Assessment:** Request changes before APROVADO. Option C is the strongest architectural direction, but ordinary-dispatch admission expiry, transactional finalization ordering, explicit initial-channel resolution, and POSITIONAL consumption need concrete resolution. Performance is mixed: bounded preflight and shared admission add latency and database work; improvement is unmeasured. Elegance and structural soundness improve relative to duplicate send operations or owners, subject to the findings below. The planned validation and private operational boundary are appropriate; actual asset and runtime readiness remain legitimate future dependencies. This review grants no execution authority.
- **Recommended path:** `Choose C: one discriminated Channel.sendMessage, declared supportedKinds, an explicit initial-selection resolver contract, one per-attempt dispatch fence, inbox orchestration composing management and transport, and transaction collaboration through the existing MessageAcceptanceService and common Outbound finalizer. A could preserve ownership but adds a second abstract operation without reducing provider I/O. B, as described, violates scoped resolution and common acceptance. C offers the smallest faithful ownership graph. Its main tradeoff is widening adapter/fake contracts and adding bounded preflight and admission costs to preserve safe external dispatch. Resolve these finite contracts before implementation; retain the existing catalogue owner, local-only initial recovery, and explicit external uncertainty.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] ARCH-R1-01 Ordinary-dispatch admission has no safe expiry and takeover contract: The proposed interlock correctly rejects an early SELECT as sufficient, but still leaves conversation locking versus a dispatch lease unresolved. A bounded logical claim does not establish exclusion after expiry: an ordinary request may remain pending externally or resume before POST while an initial attempt reserves the conversation. A local lease cannot fence the provider. A single exclusive lease could also change ordinary-versus-ordinary behavior despite D-07 preserving callers without an initial slot. These are central correctness and operational questions, not global idempotency requirements.
  - [high] ARCH-R1-02 Acceptance mutates the token needed by the proposed finalization CAS: The packet proposes one local acceptance/finalization transaction but does not settle its ordering. Existing MessageAcceptanceService.loadOutboundConversation updates lastMessageAt and therefore Conversation.updatedAt before returning. Calling that primitive and then applying the prescribed pre-HTTP updatedAt CAS would invalidate the CAS through the initial flow's own write. Echo-first acceptance can also change that timestamp and must not justify refreshing the captured baseline. Additionally, the existing acceptance wrapper handles unique conflicts after transaction rollback; that recovery cannot simply be moved inside an already-aborted caller transaction. The strict path contract also admits the acceptance spec but omits message-acceptance.service.ts itself.
  - [medium] ARCH-R1-03 Explicit initial resolution and descriptor-to-fence binding remain unspecified: The delivered resolveForConversation selects conversational origin and enforces the text window before binding; OutboundService repeats that window check. Neither delivered resolver entry point represents a manually selected initial channel carrying an approved-template payload outside the window. Widening sendMessage alone therefore cannot provide the journey. The proposed immutable descriptor also lacks a concrete contract joining management validation to the exact transport resource, opaque account reference and credential version. The final fence's enumerated checks omit an explicit text-window recheck after potentially lengthy preflight.
  - [medium] ARCH-R1-04 POSITIONAL sending needs an explicit consumption contract for the inherited catalogue: SCOPE-06 promises NAMED and POSITIONAL sending while preserving the delivered catalogue/parser. The embedded parseTemplateSummary marks every POSITIONAL template unsupported and assigns a null semanticFingerprint; the shared projector consequently reports it ineligible. Its components and parameterFormat remain available, so preserving ST-CON-05 is feasible, but the packet does not specify how initial-send support and fingerprints differ from the inherited authoring-oriented flags. Reusing those flags would exclude the promised POSITIONAL path; ignoring them without a declared validator would weaken exact-definition checking.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

