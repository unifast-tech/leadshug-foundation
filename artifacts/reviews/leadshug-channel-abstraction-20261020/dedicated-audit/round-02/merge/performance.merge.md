# PACED Subagent Review Merge: critique

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/round-02/dispatch/performance.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `Correct the public limit bound within the admitted controller/test paths, obtain candidate-bound canonical validation and review the correction before operational activation. Keep drift-guard hardening non-blocking and preserve all recorded external delivery gates.`

## Merged Findings
### F-C78B648B [high] Negative public limits bypass the claimed 500-row workload bound
- **Reviewers:** fresh-no-context-performance-reviewer
- **Category:** `performance`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Validate or normalize limits to a finite positive integer within 1..500 before either Prisma query, preserving supported positive inputs and defaults. Add real HTTP regressions for negative limits, including a large negative value, proving rejection or bounded normalization before history/relation loading. Revalidate through the canonical runner on the corrected frozen candidate.
- **Rationale:** PublicConversationsController.conversations computes Math.min(Number(q.limit) || 200, TETO) without a positive lower bound. For limit=-1000000, Prisma receives take=-999999. Negative take requests reverse-direction pagination, so this can retrieve tenant-scale conversation data and nested messages before slice(0, limite) discards the result. The messages endpoint retains the same parser and can request a million history rows directly. These are authenticated, request-controlled high-cardinality reads rather than speculative scaling concerns. Although the parser predates this diff, it is present on the changed listing path and concretely invalidates the bounded-page premise used by the new batching and performance assessment. D07 preserves legitimate public pagination behavior; it does not explicitly authorize oversized negative reads. This is a separate finding from resolved PERF-01 and is source-derived, not experimentally reproduced by this reviewer.

### F-14470CB8 [medium] Lifecycle drift guard accepts commands whose failures are swallowed
- **Reviewers:** fresh-no-context-performance-reviewer
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Add synthetic mutations that swallow the common guard and suite failures, and require their rejection. Validate the executable command form or narrowly compare the required command lines rather than accepting their presence as substrings. Keep the correction within the admitted guard/runner paths.
- **Rationale:** validate_contract checks ordered substrings in RUNNER_SCRIPT. Appending '|| true' to npm run test:e2e or to the common guard invocation preserves those substrings and their order, so the validator accepts the weakened lifecycle. Existing swallowed-error controls exercise workflow continue-on-error, not these shell-level cases. The current shipping runner does propagate failures, so this is non-blocking protection debt rather than evidence of a presently bypassed suite or grounds to reopen CIADM-01 wholesale.

## Reviewer Summaries
### fresh-no-context-performance-reviewer
- **Assessment:** Changes are required for one concrete request-controlled resource risk: the public limit parser does not enforce the claimed 500-row bound. This is retained code on the changed listing path, not a regression caused by the new index. The indexed latest-IN remediation itself is supported and does not warrant reopening historical PERF-01.

Performance: the embedded evidence reports one binding query, one credential-metadata query and one latest-IN statement for the 30-conversation page. Its backward index scan constrains both conversation_id and direction=IN, with 30 loops, 90 shared-hit blocks and 30 heap fetches. The 500-reference probe reports the same direction-constrained index access, 500 loops, zero filter removals, 1003 shared-hit blocks, zero shared reads and two heap fetches. The reported Actual Rows=0 at the inner node is a rounded per-loop average; the outer result contains two rows. Older expired IN timestamps and descending-ID ties remain observable. The actual public-list non-window selection produces zero window queries despite another official binding in the BU.

These observations establish the corrected access path, not production capacity. Only two histories have 500-row OUT suffixes; most of the 500 references have no history. Buffers are warm, and the endpoint evidence does not characterize every parent/relation query. The write probe reports approximately 6.86 MB of index storage and 17.62 ms versus 6.33 ms for successive 1000-row inserts on a simplified table. Those single samples demonstrate maintenance cost without establishing a production multiplier. Ordinary CREATE INDEX write blocking is explicitly approved for the local test database, bounded by the recorded transaction-local settings, with accelerated SQLSTATE-specific rollback evidence distinguished from the actual 5s/60s settings.

Elegance and structural soundness are acceptable. The narrow Channel port, explicit factories, operation-bound credentials, shared OutboundService and sole keyed MessageAcceptance owner form a coherent design. Repeated readiness/window reads add bounded work; they do not establish an N+1 or fetch-all defect. Typebot reevaluation before each actual output preserves the approved policy. Retired identities detach currentChannelId, so retained tombstones do not inherently become an unbounded channel relation. No additional provider, lifecycle, durable intent or compatibility bridge is needed.

Operational fit is mixed because of the public limit exposure and a non-blocking weakness in the new drift guard. Otherwise, the package truthfully separates the reported Linux same-engine all2564 success, Windows API evidence, synthetic native-path controls and unexecuted remote CI. The shared runner reports 585 passing tests, matching source/bundle provenance and empty disposable resources after cleanup. Remote CI remains not_run under the recorded adjudication and is not a newly imposed local prerequisite.

Adherence: the named index and CI/runner additions have explicit v1.3 approval. Existing timestamp semantics, provider-specific registration clients, single external POST, bounded captured-key readback and declared crash/null-ID limits are preserved. Historical resolved findings remain closed. PCV artifacts are candidates with reviewer disposition pending; preserved-database migration, API/Web activation, HTTPS, fresh operator IN/OUT, consolidation and final review remain required external gates. This review used only the embedded package and performed no execution or independent hash verification.
- **Recommended path:** `Correct the public limit bound within the admitted controller/test paths, obtain candidate-bound canonical validation and review the correction before operational activation. Keep drift-guard hardening non-blocking and preserve all recorded external delivery gates.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] PERF-R2-01 Negative public limits bypass the claimed 500-row workload bound: PublicConversationsController.conversations computes Math.min(Number(q.limit) || 200, TETO) without a positive lower bound. For limit=-1000000, Prisma receives take=-999999. Negative take requests reverse-direction pagination, so this can retrieve tenant-scale conversation data and nested messages before slice(0, limite) discards the result. The messages endpoint retains the same parser and can request a million history rows directly. These are authenticated, request-controlled high-cardinality reads rather than speculative scaling concerns. Although the parser predates this diff, it is present on the changed listing path and concretely invalidates the bounded-page premise used by the new batching and performance assessment. D07 preserves legitimate public pagination behavior; it does not explicitly authorize oversized negative reads. This is a separate finding from resolved PERF-01 and is source-derived, not experimentally reproduced by this reviewer.
  - [medium] PERF-R2-02 Lifecycle drift guard accepts commands whose failures are swallowed: validate_contract checks ordered substrings in RUNNER_SCRIPT. Appending '|| true' to npm run test:e2e or to the common guard invocation preserves those substrings and their order, so the validator accepts the weakened lifecycle. Existing swallowed-error controls exercise workflow continue-on-error, not these shell-level cases. The current shipping runner does propagate failures, so this is non-blocking protection debt rather than evidence of a presently bypassed suite or grounds to reopen CIADM-01 wholesale.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

