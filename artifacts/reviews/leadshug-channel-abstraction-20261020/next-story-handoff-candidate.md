# ST-CON-06 — next-story handoff preparation

Derived candidate only; ST-CON-06 remains Pending and must close its current blockers/validation/operator gates before either successor starts. No ST-CON-05/ST-CON-04 implementation authority is granted by this document.

## ST-CON-05 — seller template authoring

Preserve the explicit user decision: the seller creates the draft **and submits it to Meta for approval**. Do not insert an administrator approval step. The operator currently has no approved text template in the account used by LeadsHug.

Rebase the planning contract on Channel/ChannelResolver, common outbound outcomes and scoped credential ownership once06 converges. Template authoring/catalog/submission is a separate narrow capability contract: it must not add unsupported methods, no-op implementations, concrete instanceof checks or protocol fields to the universal text Channel port. No real future-network implementation is implied by this extension point.

The contract still needs to define the seller's authorized BU/channel scope, draft ownership, validation, submission/approval/rejection states, version/edit/resubmission semantics, parameter rules, safe errors, Meta status synchronization and user-facing mutation evidence. A saved draft or submitted request is not an approved template. Approval material and external requirements must be verified from current primary Meta sources during that story's planning, rather than inferred from06 text-send tests.

## ST-CON-04 — starting a conversation by contact

Keep the user's selected behavior: the seller can start a conversation in LeadsHug by supplying the contact. Rebase this story after05: approved-template selection and parameters may be required when the official free-text window is closed. No template bypass or weakening of requiresWindow is authorized by06.

Use the common abstract transport/orchestration and sole MessageAcceptance owner. Current public POST still creates the conversation before attempting a send and may leave it empty on failure;06 intentionally preserves this behavior. Any new intent/durability, deduplication, conversation-creation timing or recovery policy belongs in04's reviewed contract. ACCEPTED means a valid provider message ID, not handset delivery; UNKNOWN and ACCEPTED_LOCAL_INCOMPLETE forbid blind resend and require truthful UI/draft handling.

Explicit residuals to reconverge: current latest-IN window uses stored createdAt without transport filtering; null-ID diagnostics cannot safely merge with echoes by heuristics; local-check-to-network and crash gaps remain. Do not silently substitute the latest/current channel identity into a captured dispatch. Resolve these against first-send requirements before renewed APROVADO, without portraying them as already solved in06.

## Later channel/history work

Additional networks need independent identity/contact/credential/ingress/lifecycle contracts; registry substitution of an opaque fake proves only the existing internal port. Importing historical messages, attachments and delivery/read states remain later attendance slices. None follows automatically from current successful message sends or the Channel abstraction.
