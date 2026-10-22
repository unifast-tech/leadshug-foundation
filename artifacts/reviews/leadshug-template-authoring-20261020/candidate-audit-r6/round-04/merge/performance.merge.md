# PACED Subagent Review Merge: critique

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/candidate-audit-r6/round-04/dispatch/performance.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Accept the performance portion without another performance-driven redesign. Route OPS-R4-01 to the observation/adherence owner for a narrow correction or explicit bounded disposition before declaring the affected failure-ordering behavior closed. Preserve existing debt restrictions and complete the remaining independent assurance, formal PCV, activation and actual-provider gates.`

## Merged Findings
### F-D567D4D5 [medium] An older failed refresh can invalidate a newer passive observation
- **Reviewers:** fresh-internal-no-context-performance-r4
- **Category:** `operational_fit`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** A (recommended): add a real-BFF regression holding the completed failure response until newer persisted success arrives through a passive read, then implement reviewed failure-authority comparison within the existing observation owner while preserving genuinely current unavailability. B: if the current safe error response lacks sufficient context/fence information, obtain a bounded HOW/contract review for that metadata instead of inferring authority from arrival order or suppressing every failure. C: explicitly defer the conservative false-negative with a named owner, recovery limitation and follow-up. Keep this nonblocking for the performance lane and preserve the existing opposite-order failure assertions.
- **Rationale:** Nonblocking under the severe-runtime threshold. In web-app/src/telas/Modelos.tsx:786, atualizarStatus dispatches unavailable using only the remote ID after completeMeaningfulIntent succeeds. The reducer then marks the currently cached observation unavailable without comparing failure authority with its persisted fence. A feasible ordering is: an individual refresh commits failure at fence 2 and its real 409 response is held; another authorized client persists successful APPROVED evidence at fence 3; an already pending passive catalogue GET delivers fence 3 to this screen; the held failure is then released. Passive adoption does not advance completedIntent, so the older intent remains admissible and invalidates the newer fence-3 observation, including its editor proof. No derived read follows this catch. The catalogue failure branch has the analogous unconditional catalogFailure veto. The new successful-response race cases and the existing newer-failure-versus-older-success case do not cover this reverse ordering. This is a source-derived counterexample, not an executed reproduction, and creates a conservative availability false-negative rather than demonstrated unauthorized use or server exhaustion.

## Reviewer Summaries
### fresh-internal-no-context-performance-r4
- **Assessment:** No concrete severe server/runtime performance blocker is established. One additional source-supported failure-ordering issue remains nonblocking under this dispatch's performance threshold. This review uses only the embedded package; no tools, tests or independent hash verification were performed.

Performance is acceptable. The changed reducer reconciles explicitly loaded observations without additional HTTP, provider fan-out or a third cache. Its temporary indexes and selection passes scale with loaded rows. Unchanged backend evidence shows parent pagination before child hydration, 20/50 operation probes for returned pages, zero child probes beyond the last page, detail hydration limited to 11 operations and 10 receipts each, and catalogue hydration through one statement with at most 50 indexed probes. Saved-observation projection performs bounded direct lookups rather than history scanning. Deep OFFSET, exact counts and bounded sequential catalogue writes retain their disclosed costs; this delta supplies no regression warranting reopening those decisions.

Adherence and elegance are generally acceptable. The small reducer is justified by atomic selection and retention of an omitted selected editor observation. Page membership and cursor metadata remain separate from observation selection. Current code substantively addresses the prior equal-fence common/draft eligibility defect, historical-classification laundering and both successful older-explicit versus newer-passive orderings. The r35 failure transform preserves genuine common unavailability while keeping eligibleForUse restricted to the individual projection. Seller submission, backend eligibility authority, immutable ACK associations, observational GETs and the narrow Channel boundary remain preserved. The remaining finding concerns an additional failed-response ordering within this changed owner.

The supplied current r35 acceptance reports 797 passing tests: 284 API unit, 398 PostgreSQL, 42 Web unit and 73 Playwright cases, including 72 browser cases. Source/runtime attestations report 38 matching sources, 30 inherited seals, three unchanged HEADs and matching served/dist bytes. The strengthened recovery assertions inspect the actual owned response and advancing fence before the unchanged DOM oracle. Both template FRC markers establish separate 100-BFF-request and 100-UI-attempt probes. The r31/r32/r33/r34 RED limits remain accurately distinguished; r34 is partial worker capture, not first-byte canonical evidence. These supplied attestations were not independently recomputed.

Operational fit remains mixed because an older failed response can still invalidate newer passive evidence. The five-tenant RLS stage demonstrates bounded functional outcomes, not capacity, latency percentiles or saturation. Formal pcv-1 disposition remains pending. SEC-R6-04 stays deferred through foundation_documentation/backlog/README.md#BLG-leadshug-template-recovery-read-budget for the private local cohort only; this delta does not reopen that debt. Original test-after/unknown debt and reported credential containment retain their recorded limits. Preserved TEST preflight/migrations, source-bound activation, assisted actual Meta submission/status and fresh final review remain mandatory; delivery remains Pending.
- **Recommended path:** `Accept the performance portion without another performance-driven redesign. Route OPS-R4-01 to the observation/adherence owner for a narrow correction or explicit bounded disposition before declaring the affected failure-ordering behavior closed. Preserve existing debt restrictions and complete the remaining independent assurance, formal PCV, activation and actual-provider gates.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] OPS-R4-01 An older failed refresh can invalidate a newer passive observation: Nonblocking under the severe-runtime threshold. In web-app/src/telas/Modelos.tsx:786, atualizarStatus dispatches unavailable using only the remote ID after completeMeaningfulIntent succeeds. The reducer then marks the currently cached observation unavailable without comparing failure authority with its persisted fence. A feasible ordering is: an individual refresh commits failure at fence 2 and its real 409 response is held; another authorized client persists successful APPROVED evidence at fence 3; an already pending passive catalogue GET delivers fence 3 to this screen; the held failure is then released. Passive adoption does not advance completedIntent, so the older intent remains admissible and invalidates the newer fence-3 observation, including its editor proof. No derived read follows this catch. The catalogue failure branch has the analogous unconditional catalogFailure veto. The new successful-response race cases and the existing newer-failure-versus-older-success case do not cover this reverse ordering. This is a source-derived counterexample, not an executed reproduction, and creates a conservative availability false-negative rather than demonstrated unauthorized use or server exhaustion.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
