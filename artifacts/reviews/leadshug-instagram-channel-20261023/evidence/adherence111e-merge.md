# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence111e-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `unknown`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Correct the new CP5 protection harness within this TODO, then obtain frozen current canonical ALL evidence and fresh affected review. The findings do not require redesigning the approved Channel/Outbound/Acceptance architecture. Current performance is unproved; retain the recorded primary subscription, complete browser, CP6 and independent assurance gates without reopening supported historical closures or inferring feature acceptance.`

## Merged Findings
### F-2D76DF0A [high] The retained-cohort guard rejects legitimate messages added by earlier cases
- **Reviewers:** fresh_no_context_adherence111e
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Track the original message IDs or external IDs and count only those in the preservation guard. Retain exact conversation/route preservation checks and separately assert each workload's additional message and unread effects. Do not reset the cohort between cases.
- **Rationale:** assertRetainedCohort labels its message count original_in but counts every qualifying Instagram IN message, without restricting it to the original seeded messages. The replay case intentionally adds one message, then calls this guard expecting exactly 10000 messages per BU. On the intended successful behavior, BU A instead has 10001. Subsequent resource, RLS and batch cases encounter the same failing entry guard. This defeats the required six independent workloads over one retained cohort.

### F-B1EABFAD [high] The batch identity assertion places peer fields on the wrong Prisma model
- **Reviewers:** fresh_no_context_adherence111e
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Place the peer namespace, scope and externalPeerId predicates on the outer ContactIdentity filter. Use conversationRoutes.some for the exact expected route ID, conversation, BU and business identity, preserving all 1000 association assertions.
- **Rationale:** The 1000-message case passes externalPeerId, namespace and scopeReference inside conversationRoutes.some. The enclosed schema defines these fields on ContactIdentity, while ConversationRoute has contactScopeReference and businessScopeReference. The argument is incompatible with ConversationRouteWhereInput and would be rejected by Prisma at runtime if type checking were bypassed. This blocks the per-peer assertion before the latency and replay proof can finish.

### F-42098C7F [high] Resource-claim telemetry references an undeclared identifier
- **Reviewers:** fresh_no_context_adherence111e
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Bind the telemetry property to the actual observed unsettledClaimsAtRelease value. Preserve the assertion of twenty unsettled calls and execute the corrected case through canonical validation.
- **Rationale:** The resource-claim case declares and asserts unsettledClaimsAtRelease, but its final JSON log uses the undeclared shorthand unsettledClaimsAtBarrierRelease. This is a static identifier error and would also throw ReferenceError if the spec were transpiled without type checking. Even successful ownership assertions cannot complete this case as written. The supplied qualification explicitly records no compilation or execution.

### F-1129B043 [medium] Zero-provider-HTTP assertions omit supported provider boundaries
- **Reviewers:** fresh_no_context_adherence111e
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Capture Instagram, Meta and Evolution counter baselines before the relevant read or ingress workloads, including isolated EPS probes and warmups, and assert unchanged counters afterward. Preserve expected OAuth/setup calls outside those measurement intervals.
- **Rationale:** EPS records only instagramFake.calls, and establishes that baseline after the isolated request probes and initial list/plan request. Meta and Evolution calls during EPS would escape its no-HTTP oracle. Replay, RLS and batch check Instagram and Meta but omit evolutionFake.providerCalls. The approved zero-external-HTTP and ingress isolation protections cover the shared system, so these counters can report success despite an unintended WhatsApp provider call.

### F-C1541847 [medium] The spec introduces hard query caps beyond the recorded page-budget contract
- **Reviewers:** fresh_no_context_adherence111e
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Apply the approved eight-query cap to list pages. Preserve lookup/options p95 limits, actual query telemetry and concrete bounded-query/no-N+1 protection without silently introducing new numeric acceptance limits. Any intended additional hard cap needs explicit contract reconciliation.
- **Rationale:** The governing TODO's fixture70 resolution explicitly preserves at most eight domain queries per conversation page while keeping options/thread query counts as telemetry with no N+1. measureRequest applies the eight-query assertion to lookup and reply-options as well as list pages, and the RLS companion imposes it on thread requests again. These additional hard gates are not established by that resolution or the frozen lookup/options latency thresholds.

### F-1173D8D1 [medium] The index protection oracle enforces only incidental route index use
- **Reviewers:** fresh_no_context_adherence111e
- **Category:** `performance`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Capture the actual relevant peer and owner lookup SQL as well as the route/display SQL, retain original parameters, and add workload-appropriate assertions for qualifying index definitions, bounded predicates and plan cardinality. Allow justified sequential scans on the small owner cohort; do not force the planner or claim all joins must use indexes.
- **Rationale:** The EPS case captures a real display-query plan, but only requires that each named table have some index and that some conversation_routes scan use an index. Every table's primary-key index satisfies the availability test. Peer/owner plan entries are merely logged, and a route-count lateral subquery can satisfy the route assertion even if another important scan regresses. This does not enforce the recorded source110a correction for qualified peer/owner/route lookup plans, bounded predicates and cardinality.

### F-B2ABE699 [medium] The PostgreSQL waiter observer can queue behind the claims it must observe
- **Reviewers:** fresh_no_context_adherence111e
- **Category:** `structural_soundness`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Use an independently connected synthetic PostgreSQL observer or otherwise guarantee observer capacity before launching all twenty claims. Preserve twenty genuine pending claim invocations, numeric observed waiters, one winner, nineteen ownership conflicts and unconditional draining; do not solve this by reducing contention or extending timeouts.
- **Rationale:** The holder, twenty claim transactions and pg_stat_activity polling all use the same Prisma pool. With at most twenty-one connections, the holder and blocked contenders can occupy every connection while remaining claim acquisitions precede the observer in the pool queue. The observer then cannot establish the required waiter evidence until finally releases the holder, which occurs only after observation fails. The package supplies no guaranteed spare observer capacity. Counting submitted unsettled calls honestly accommodates pool queuing, but does not resolve this observation dependency.

## Reviewer Summaries
### fresh_no_context_adherence111e
- **Assessment:** changes_required
- **Recommended path:** `Correct the new CP5 protection harness within this TODO, then obtain frozen current canonical ALL evidence and fresh affected review. The findings do not require redesigning the approved Channel/Outbound/Acceptance architecture. Current performance is unproved; retain the recorded primary subscription, complete browser, CP6 and independent assurance gates without reopening supported historical closures or inferring feature acceptance.`
- **Performance:** `unknown`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] IG-CP5-111E-01 Resource-claim telemetry references an undeclared identifier: The resource-claim case declares and asserts unsettledClaimsAtRelease, but its final JSON log uses the undeclared shorthand unsettledClaimsAtBarrierRelease. This is a static identifier error and would also throw ReferenceError if the spec were transpiled without type checking. Even successful ownership assertions cannot complete this case as written. The supplied qualification explicitly records no compilation or execution.
  - [high] IG-CP5-111E-02 The batch identity assertion places peer fields on the wrong Prisma model: The 1000-message case passes externalPeerId, namespace and scopeReference inside conversationRoutes.some. The enclosed schema defines these fields on ContactIdentity, while ConversationRoute has contactScopeReference and businessScopeReference. The argument is incompatible with ConversationRouteWhereInput and would be rejected by Prisma at runtime if type checking were bypassed. This blocks the per-peer assertion before the latency and replay proof can finish.
  - [high] IG-CP5-111E-03 The retained-cohort guard rejects legitimate messages added by earlier cases: assertRetainedCohort labels its message count original_in but counts every qualifying Instagram IN message, without restricting it to the original seeded messages. The replay case intentionally adds one message, then calls this guard expecting exactly 10000 messages per BU. On the intended successful behavior, BU A instead has 10001. Subsequent resource, RLS and batch cases encounter the same failing entry guard. This defeats the required six independent workloads over one retained cohort.
  - [medium] IG-CP5-111E-04 The PostgreSQL waiter observer can queue behind the claims it must observe: The holder, twenty claim transactions and pg_stat_activity polling all use the same Prisma pool. With at most twenty-one connections, the holder and blocked contenders can occupy every connection while remaining claim acquisitions precede the observer in the pool queue. The observer then cannot establish the required waiter evidence until finally releases the holder, which occurs only after observation fails. The package supplies no guaranteed spare observer capacity. Counting submitted unsettled calls honestly accommodates pool queuing, but does not resolve this observation dependency.
  - [medium] IG-CP5-111E-05 The spec introduces hard query caps beyond the recorded page-budget contract: The governing TODO's fixture70 resolution explicitly preserves at most eight domain queries per conversation page while keeping options/thread query counts as telemetry with no N+1. measureRequest applies the eight-query assertion to lookup and reply-options as well as list pages, and the RLS companion imposes it on thread requests again. These additional hard gates are not established by that resolution or the frozen lookup/options latency thresholds.
  - [medium] IG-CP5-111E-06 Zero-provider-HTTP assertions omit supported provider boundaries: EPS records only instagramFake.calls, and establishes that baseline after the isolated request probes and initial list/plan request. Meta and Evolution calls during EPS would escape its no-HTTP oracle. Replay, RLS and batch check Instagram and Meta but omit evolutionFake.providerCalls. The approved zero-external-HTTP and ingress isolation protections cover the shared system, so these counters can report success despite an unintended WhatsApp provider call.
  - [medium] IG-CP5-111E-07 The index protection oracle enforces only incidental route index use: The EPS case captures a real display-query plan, but only requires that each named table have some index and that some conversation_routes scan use an index. Every table's primary-key index satisfies the availability test. Peer/owner plan entries are merely logged, and a route-count lateral subquery can satisfy the route assertion even if another important scan regresses. This does not enforce the recorded source110a correction for qualified peer/owner/route lookup plans, bounded predicates and cardinality.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
