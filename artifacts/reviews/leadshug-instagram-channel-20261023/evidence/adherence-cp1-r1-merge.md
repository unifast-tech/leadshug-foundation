# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence-cp1-r1-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `unknown`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Repair the CP1 identity, ownership, linkage and lookup defects below, strengthen the bounded PostgreSQL proof, and adapt the two remaining invalid bulk fixtures without weakening their assertions. Capture a complete stable-source API rerun and re-review CP1. Preserve the approved architecture and the existing CP2–CP6 sequence; this checkpoint does not confer delivery, cutover, runtime or Meta acceptance.`

## Merged Findings
### F-E2D1DF19 [high] Verified WhatsApp registration still bypasses durable business ownership
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Introduce one transactional owner for claims of the normalized, provider-proved WhatsApp business number. Invoke it before verification or credential promotion in both adapters, link both persisted identities, and reject a foreign durable owner or another retained WhatsApp resource. Add a real concurrent PostgreSQL test crossing adapters and BUs, including disconnected ownership, with unchanged credentials and grants for the loser.
- **Rationale:** The production ownership reservation in api-app/src/domain/channels/number-registration.service.ts:264 claims only provider=OFICIAL plus phoneNumberId, then promotes the credential at :357 without creating or checking BusinessChannelIdentity. Evolution's verified-number transaction in api-app/src/domain/channels/channels.service.ts:230 likewise checks only the local BU.phone and marks the channel verified at :239. Neither path associates channel/provider rows with the new business owner. The same proved phone can consequently be accepted through official in BU A and a different Evolution instance in BU B: the provider keys differ, BU.phone has no global uniqueness, and the new business-identity constraints see no rows. api-app/test/instagram-identity.e2e-spec.ts:67 proves only stand-alone identity-row cardinality, not this resource-claim path. This is the explicit CP1 durable ownership obligation, separate from scheduled CP3 outbound and consumer integration.

### F-BB2E2776 [high] Provider attachment does not enforce the channel's BU, resource or adapter
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `security`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Enforce the complete current attachment relationship through scoped composite constraints and centralized transactional validation, preserving explicitly unmapped legacy rows. Test same-BU wrong-resource attachment, cross-BU attachment and provider/adapter mismatch directly in PostgreSQL. Keep this repair within CP1's association invariant; no CP3 sender implementation is required to prove it.
- **Rationale:** api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:65 and :71 add separate business-identity FKs and a provider tuple UNIQUE, but no FK or trigger equates that tuple with the currently attached BuChannel. api-app/prisma/schema.prisma:276 retains a currentChannel relation referencing only channel ID. A provider identity linked to business resource A can therefore reference a channel linked to resource B, including another BU, while all new constraints pass. The tuple UNIQUE does not enforce an association. The exact admitted historical dependencies were checked: 20261015120000_number_onboarding_foundation/migration.sql:115 supplies the single-ID FK; 20261015130000_number_onboarding_provider_resource_ownership_immutable/migration.sql:9 protects only provider/resource/BU updates; the admitted operation-fence and current-channel-index migrations add no association enforcement. The route tests create no channel/provider tuple and cannot detect this defect.

### F-698F710C [high] Manual opening does not reuse the qualified identity established by backfill
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `architecture`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Resolve existing WhatsApp PERSON identity and its conversation by the qualified canonical key before readiness, and repeat the canonical lookup under the creation fence. Add service/request regression cases for the preserved formatted legacy contact, readiness changes, and equal external strings belonging to other namespaces or platforms.
- **Rationale:** api-app/src/domain/inbox/conversation-start.service.ts:27 and :35 still search Conversation.contact strings. Only after both misses does :40 resolve the canonical peer, followed by an unconditional conversation.create at :41. The actual migration fixture at api-app/test/instagram-migration.e2e-spec.ts:83 deliberately preserves '+55 (11) 99999-0000' while backfilling its canonical digits. Opening that phone through the service misses the preserved string; an unavailable channel incorrectly blocks reuse, and a ready channel reaches the existing ContactIdentity then violates unique(buId,contactId). The new identity test at api-app/test/instagram-identity.e2e-spec.ts:94 calls the helper directly rather than exercising ConversationStartService, so its title overstates service-level reuse. Raw string lookup can also select an unrelated platform or group after the old string uniqueness is removed.

### F-B1A54BA6 [high] An immutable route can still change its recipient through ContactIdentity
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `architecture`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Defend the qualified ContactIdentity address and its contact ownership against mutation in PostgreSQL. Add a negative PostgreSQL case that creates a valid route, then attempts to change the referenced external peer and namespace while retaining the route ID; both operations must fail.
- **Rationale:** api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:143 binds the route to identity ID, BU, contact, platform and scope, while api-app/prisma/schema.prisma:485 leaves namespace and externalPeerId independently mutable. The mutation trigger at migration.sql:203 protects only conversation_routes. Updating a referenced contact_identities.external_peer_id to a previously unused peer therefore preserves every route FK and every captured identity ID while changing the resolved recipient. Changing its namespace is likewise unprotected. This violates the immutable peer/route requirement in foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md:739.

### F-EFBD915B [medium] Two retained performance regressions fail before reaching their assertions
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Adapt these two preparations through the canonical bulk contact/conversation fixture, retaining all dataset sizes, query counters, EXPLAIN assertions and HTTP assertions. Capture a complete full API result and independently identify the remaining reported failure.
- **Rationale:** api-app/test/conversation-start.e2e-spec.ts:99 and :124 still call prisma.conversation.createMany with no contactId, although api-app/prisma/schema.prisma:432 now requires it. Both tests therefore fail while preparing their 15,000-row and 60-row datasets, before validating the inbox index or batched query behavior. The canonical bulk fixture helper already exists at api-app/test/helpers.ts:34 but is not used here. These are concrete unresolved fixture defects, not evidence that the performance assertions passed, and this review does not assume they explain all three reported API failures.

### F-5DF8D90E [medium] The passing migration fixture covers only part of the required CP1 cohort
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Expand the actual historical-schema fixture to both adapters, groups, incomplete message/resource provenance, the remaining persisted states and safe conflict aborts. Compare all original conversation/message/provider/intent/admission facts, including timestamps, keys, receipts and deadlines. Keep state-specific service recovery and zero-provider-dispatch integration assigned to CP3; this finding concerns migration preservation proof only.
- **Rationale:** api-app/test/instagram-migration.e2e-spec.ts:79 seeds one official channel/provider and only PESSOA conversations. Its seeded state matrix at :89 includes ordinary PREPARED/SENDING/SETTLED and initial PREPARED/SENDING/EXTERNAL_ACCEPTED_LOCAL_BLOCKED/SUCCEEDED, but no groups, Evolution history, ordinary UNCERTAIN, initial AMBIGUOUS or EXTERNAL_ACCEPTED. Full original conversation-row equality is checked for only the main conversation at :136, although the other conversations carry pending snapshots. No conflict/normalized-collision abort case is present. The supplementary cp1-diagnostic-green.json:35 correctly acknowledges limited VAL-02 coverage; its green result should not close the broader CP1 migration-preservation criterion.

### F-C6F7B3E7 [medium] Business ownership is update-protected but can still be deleted and reclaimed
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Make business ownership append-only through a retained tombstone or explicit deletion guard. Test deletion and attempted reclaim under another BU, as well as retained WhatsApp cardinality after disconnection. Synthetic cleanup can use an explicitly bounded table reset rather than weakening product deletion protection.
- **Rationale:** api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:153 defines an ownership trigger that runs only BEFORE UPDATE at :166. There is no deletion protection for a business identity without dependent rows. Deleting such an owner allows the same qualified resource to be inserted under another BU and releases the retained WhatsApp cardinality restriction. The FK from an identity to its BU at :51 prevents deletion of the parent BU, not deletion of the identity. This leaves the new durable ownership primitive weaker than its stated contract.

### F-9A097A9D [medium] Backfill silently adopts invalid person addresses as canonical WhatsApp identities
- **Reviewers:** instagram_cp1_adherence_r1
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use one explicit WhatsApp person-address normalization and validation contract. Reject or safely diagnose unprovable legacy person addresses before committing the migration, preserving original rows and receipts. Cover invalid, empty, overlong and normalized-collision inputs with abort-and-preservation cases.
- **Rationale:** api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:85 removes every nondigit from each PESSOA contact and inserts the result at :100 without validating phone syntax or E.164 length. Values such as 'customer42' become '42', and nonnumeric values become an empty canonical peer; neither is rejected by the new schema. api-app/src/domain/inbox/contact-identity.ts:21 uses the same unrestricted transformation, with only a nonblank check in the resolver at :39. This differs from the explicit bounded phone grammar in conversation-start.service.ts:8 and promotes uncertain legacy addresses into asserted canonical identities instead of blocking adoption.

## Reviewer Summaries
### instagram_cp1_adherence_r1
- **Assessment:** changes_required for CP1. All 33 source hashes and the governing TODO hash matched before and after review. The exact v1 reader, v2 tuple parser, scoped conversation/contact FKs and preservative migration direction are sound foundations. Architecture/adherence, security and structural soundness still have concrete defects; code quality and elegance are mixed because canonical identities coexist with operational string lookups and incomplete association enforcement. Performance remains unknown; no measurements were inferred. The supplementary diagnostic receipt reports eight passing Instagram cases, but does not establish the broader migration cohort or repair the recorded full API failures. Operational fit remains mixed. This is a read-only checkpoint review, without tests, runtime or private access. The complete Frontend/Consumer Matrix was considered; CP2–CP6, including CP3 writer/consumer/recovery integration and final audits, remain scheduled obligations rather than newly discovered missing scope. Inherited restrictions remain unchanged.
- **Recommended path:** `Repair the CP1 identity, ownership, linkage and lookup defects below, strengthen the bounded PostgreSQL proof, and adapt the two remaining invalid bulk fixtures without weakening their assertions. Capture a complete stable-source API rerun and re-review CP1. Preserve the approved architecture and the existing CP2–CP6 sequence; this checkpoint does not confer delivery, cutover, runtime or Meta acceptance.`
- **Performance:** `unknown`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] IG-CP1-R1-01 An immutable route can still change its recipient through ContactIdentity: api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:143 binds the route to identity ID, BU, contact, platform and scope, while api-app/prisma/schema.prisma:485 leaves namespace and externalPeerId independently mutable. The mutation trigger at migration.sql:203 protects only conversation_routes. Updating a referenced contact_identities.external_peer_id to a previously unused peer therefore preserves every route FK and every captured identity ID while changing the resolved recipient. Changing its namespace is likewise unprotected. This violates the immutable peer/route requirement in foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md:739.
  - [high] IG-CP1-R1-02 Provider attachment does not enforce the channel's BU, resource or adapter: api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:65 and :71 add separate business-identity FKs and a provider tuple UNIQUE, but no FK or trigger equates that tuple with the currently attached BuChannel. api-app/prisma/schema.prisma:276 retains a currentChannel relation referencing only channel ID. A provider identity linked to business resource A can therefore reference a channel linked to resource B, including another BU, while all new constraints pass. The tuple UNIQUE does not enforce an association. The exact admitted historical dependencies were checked: 20261015120000_number_onboarding_foundation/migration.sql:115 supplies the single-ID FK; 20261015130000_number_onboarding_provider_resource_ownership_immutable/migration.sql:9 protects only provider/resource/BU updates; the admitted operation-fence and current-channel-index migrations add no association enforcement. The route tests create no channel/provider tuple and cannot detect this defect.
  - [high] IG-CP1-R1-03 Verified WhatsApp registration still bypasses durable business ownership: The production ownership reservation in api-app/src/domain/channels/number-registration.service.ts:264 claims only provider=OFICIAL plus phoneNumberId, then promotes the credential at :357 without creating or checking BusinessChannelIdentity. Evolution's verified-number transaction in api-app/src/domain/channels/channels.service.ts:230 likewise checks only the local BU.phone and marks the channel verified at :239. Neither path associates channel/provider rows with the new business owner. The same proved phone can consequently be accepted through official in BU A and a different Evolution instance in BU B: the provider keys differ, BU.phone has no global uniqueness, and the new business-identity constraints see no rows. api-app/test/instagram-identity.e2e-spec.ts:67 proves only stand-alone identity-row cardinality, not this resource-claim path. This is the explicit CP1 durable ownership obligation, separate from scheduled CP3 outbound and consumer integration.
  - [high] IG-CP1-R1-04 Manual opening does not reuse the qualified identity established by backfill: api-app/src/domain/inbox/conversation-start.service.ts:27 and :35 still search Conversation.contact strings. Only after both misses does :40 resolve the canonical peer, followed by an unconditional conversation.create at :41. The actual migration fixture at api-app/test/instagram-migration.e2e-spec.ts:83 deliberately preserves '+55 (11) 99999-0000' while backfilling its canonical digits. Opening that phone through the service misses the preserved string; an unavailable channel incorrectly blocks reuse, and a ready channel reaches the existing ContactIdentity then violates unique(buId,contactId). The new identity test at api-app/test/instagram-identity.e2e-spec.ts:94 calls the helper directly rather than exercising ConversationStartService, so its title overstates service-level reuse. Raw string lookup can also select an unrelated platform or group after the old string uniqueness is removed.
  - [medium] IG-CP1-R1-05 Business ownership is update-protected but can still be deleted and reclaimed: api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:153 defines an ownership trigger that runs only BEFORE UPDATE at :166. There is no deletion protection for a business identity without dependent rows. Deleting such an owner allows the same qualified resource to be inserted under another BU and releases the retained WhatsApp cardinality restriction. The FK from an identity to its BU at :51 prevents deletion of the parent BU, not deletion of the identity. This leaves the new durable ownership primitive weaker than its stated contract.
  - [medium] IG-CP1-R1-06 Backfill silently adopts invalid person addresses as canonical WhatsApp identities: api-app/prisma/migrations/20261023190000_instagram_identity_routes/migration.sql:85 removes every nondigit from each PESSOA contact and inserts the result at :100 without validating phone syntax or E.164 length. Values such as 'customer42' become '42', and nonnumeric values become an empty canonical peer; neither is rejected by the new schema. api-app/src/domain/inbox/contact-identity.ts:21 uses the same unrestricted transformation, with only a nonblank check in the resolver at :39. This differs from the explicit bounded phone grammar in conversation-start.service.ts:8 and promotes uncertain legacy addresses into asserted canonical identities instead of blocking adoption.
  - [medium] IG-CP1-R1-07 Two retained performance regressions fail before reaching their assertions: api-app/test/conversation-start.e2e-spec.ts:99 and :124 still call prisma.conversation.createMany with no contactId, although api-app/prisma/schema.prisma:432 now requires it. Both tests therefore fail while preparing their 15,000-row and 60-row datasets, before validating the inbox index or batched query behavior. The canonical bulk fixture helper already exists at api-app/test/helpers.ts:34 but is not used here. These are concrete unresolved fixture defects, not evidence that the performance assertions passed, and this review does not assume they explain all three reported API failures.
  - [medium] IG-CP1-R1-08 The passing migration fixture covers only part of the required CP1 cohort: api-app/test/instagram-migration.e2e-spec.ts:79 seeds one official channel/provider and only PESSOA conversations. Its seeded state matrix at :89 includes ordinary PREPARED/SENDING/SETTLED and initial PREPARED/SENDING/EXTERNAL_ACCEPTED_LOCAL_BLOCKED/SUCCEEDED, but no groups, Evolution history, ordinary UNCERTAIN, initial AMBIGUOUS or EXTERNAL_ACCEPTED. Full original conversation-row equality is checked for only the main conversation at :136, although the other conversations carry pending snapshots. No conflict/normalized-collision abort case is present. The supplementary cp1-diagnostic-green.json:35 correctly acknowledges limited VAL-02 coverage; its green result should not close the broader CP1 migration-preservation criterion.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

