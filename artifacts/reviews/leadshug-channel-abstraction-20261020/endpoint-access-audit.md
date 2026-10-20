# ST-CON-06 — scoped access-path audit

Derived source/measurement review for the Performance lane. This is not a capacity certification. The available exact_lookup_anti_pattern_audit.sh implements PHP/Dart patterns only; running it over TypeScript would not establish Prisma/Nest coverage, so no such clean-scan claim is used. Explicit source inspection and real query-log/EXPLAIN evidence replace that inapplicable lens, not the required runtime evidence.

| Access surface | Classification | Actual path / bound | Index / evidence |
|---|---|---|---|
| ConversationChannelReference ownership | exact lookup | Conversation findFirst by id+buId; no list walking | Conversation primary key plus BU predicate; realPG crossBU denial |
| Verified ingress binding | exact lookup | BuChannel id+BU, then selected identity/context; findMany wherePK yields at most1 row | BuChannel primary key; resource currentChannelId index; ingress mismatch/retirement regression |
| Selected human/public origin | ordered exact lookup + bounded BU list | latest Message by conversationId createdAt DESC,id DESC; list channels restricted to selected BU, current unique(buId,type) slots; no provider fallback | messages_conversation_id_created_at_idx; existing current-channel slots preserve physical provenance |
| Operation identity/version fence | exact lookup | channel id/BU/type/generation/epoch + selected identityId; officialcredential relation only metadata afterdispatch | primary keys/resource currentChannelId; actual shipping callback omission mutants detect missedcheck |
| Credential resolve/inspect | exact lookup / scoped batch | existing owner resolver; metadata inspect constrained to selected channel/gen; envelope decrypt only actualsend | credential/channel identity keys; twotenants distinctsealedsend inputs |
| Public page availability | bounded paginated list + batched metadata | same selected BU; one binding query, one credentialmetadata query, one SQL latestIN projection; no perconversation provider or credentiallookup | actual CHANNEL-EPS:30conversations x24history, querycounts1/1/1, LATERAL LIMIT1 with indexscan30loops |
| Required free-text window | exact latest-IN per conversation / scoped batch | storedtimestamp existingalgorithm, directionIN; LATERAL top1 for page; no fetchallhistory in application | existing messageconversation timestamp index; no new migration; transportfilter/newtrustedtimestamp explicitly04 |
| Accepted message readback | exact lookup | at mostone readback by captured provider identity/externalID/provenance afterlocalfailure | existing unique(providerResourceIdentityId,externalId); no callback retry or providerquery |

Expected query cost: one indexed probe per requestedconversation inside one SQL statement, plus two scoped metadata queries per page. The EXPLAIN records incremental sort on the timestamp/id tie key; it is not described as a new covering index. Current relation retrieval must still be challenged by Performance against actual resource-retirement invariants; no universal bound for future channel networks is inferred from current slot count.

No endpoint latency SLO is approved. Observed elapsed and EXPLAIN milliseconds are one disposable local sample. Five20operation concurrent batches and the separate scoped-read stage prove their declared local integrity/thresholds only, not live-provider capacity, saturation, soak or external exactlyonce.
