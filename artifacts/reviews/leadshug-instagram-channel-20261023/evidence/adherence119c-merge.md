# PACED Subagent Review Merge: architecture_adherence

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence119c-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `Correct the completed-account metadata ordering and add native regression coverage within this TODO. Reconcile terminal API116 evidence separately; current ALL, browser, primary subscription observation and remaining assurance/CP6 gates stay open. This complementary review provides no checkpoint or feature acceptance.`

## Merged Findings
### F-7D47B745 [medium] Mutable attempt timestamps can select an older completed account label
- **Reviewers:** fresh-internal-no-context-119c
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Select the last completed mapping using durable mapping chronology or version ordering that cancellation cannot advance, retaining all existing ownership and app-scope predicates. Add a native case with two completed mappings, cancel the older one, and verify catalog/list/thread/reply-options retain the newer label with unchanged channel readiness and provider counters.
- **Rationale:** Both display queries now include completed CANCELLED mappings but select their label using ORDER BY ia.updated_at DESC, ia.id DESC. Cancellation updates that timestamp while preserving mapping evidence. Cancelling an earlier completed mapping after a newer successful reauthorization can therefore make the earlier username outrank the newer proven username. The BU/channel/resource/app-scope predicates establish ownership, but do not establish which mapping is newest. This is a distinct residual defect in the materially changed cancellation selector under SCOPE-07/DOD-06, rather than reopening the original missing-CANCELLED-label finding. The enclosed native case cancels only the newest mapping and does not exercise this ordering. No executed failure is claimed.

## Reviewer Summaries
### fresh-internal-no-context-119c
- **Assessment:** changes_required
- **Recommended path:** `Correct the completed-account metadata ordering and add native regression coverage within this TODO. Reconcile terminal API116 evidence separately; current ALL, browser, primary subscription observation and remaining assurance/CP6 gates stay open. This complementary review provides no checkpoint or feature acceptance.`
- **Performance:** `unknown`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-ADHERENCE119C-01 Mutable attempt timestamps can select an older completed account label: Both display queries now include completed CANCELLED mappings but select their label using ORDER BY ia.updated_at DESC, ia.id DESC. Cancellation updates that timestamp while preserving mapping evidence. Cancelling an earlier completed mapping after a newer successful reauthorization can therefore make the earlier username outrank the newer proven username. The BU/channel/resource/app-scope predicates establish ownership, but do not establish which mapping is newest. This is a distinct residual defect in the materially changed cancellation selector under SCOPE-07/DOD-06, rather than reopening the original missing-CANCELLED-label finding. The enclosed native case cancels only the newest mapping and does not exercise this ordering. No executed failure is claimed.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.
