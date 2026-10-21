# PACED Subagent Review Merge: critique

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/critique-v1.1.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `acceptable`

## Recommended Paths
- `Retain D09's narrow resolver/provider capability, dedicated Meta adapter and single existing credential owner; this is a simple, faithful DIP design without a generic capability platform. Resolve the shared observation fence, reconverge the affected freeze/review evidence, complete the pending planning guards and obtain specific human approval. Performance planning is acceptable: bounded provider calls, pagination, durable quotas, quota-aware fixtures and scan/filter/recheck/buffer measurements are explicit. Operational planning is also acceptable: source admission, additive migration checks, independent wire tests, real PostgreSQL/browser validation and assisted provider proof remain mandatory and unexecuted.`

## Merged Findings
### F-343FB759 [medium] Catalog and individual refreshes need an explicit shared observation fence
- **Reviewers:** fresh-internal-critique-v1.1
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Before APROVADO, require both refresh paths to use a shared observation ordering rule within the authorized account/context. An account/context lease shared by both paths or a common observation-version fence would suffice; preserve scoped business data and the single projector. Explicitly prevent an older in-flight result from superseding a newer observation. Add planned real-PostgreSQL held-response cases in both directions between catalog and individual refresh, proving that APPROVED→PAUSED remains PAUSED and ineligible through GET and reload.
- **Rationale:** D07 specifies resource/context leases and fences against changed generations, accounts and credential versions. The API matrix nevertheless introduces two producers of status for the same remote template: catalog refresh and individual draft refresh. Their shared ordering rule is unspecified. A catalog request can capture APPROVED and stall, an individual refresh can record PAUSED, and the older catalog result can then replace that observation while every identity field remains current. UI response fences cannot protect persisted state subsequently returned by GET or reload. This could restore observedEligible=true despite a newer known PAUSED observation, conflicting with DOD-04/05. The existing historical resolutions do not establish ordering across these two producers.

## Reviewer Summaries
### fresh-internal-critique-v1.1
- **Assessment:** One material planning gap remains before APROVADO. Otherwise, the complete contract adheres to seller submission without an administrator intermediary, preserves management versus message readiness, and keeps recipient sending and future capabilities outside this slice. AR-V11-01 is resolved at the planning-contract level through positive original-claim confirmation, bounded captured readback, truthful persistence certainty and retained external acceptance. AR-V11-02 is resolved through global canonical account/name/language coordination with scoped business data and safe conflicts. AR-V11-03 is resolved through initial verification of all 41 hashes and three HEADs, followed by 30 sealed files and reviewed shared deltas. These conclusions establish no implementation or runtime pass.
- **Recommended path:** `Retain D09's narrow resolver/provider capability, dedicated Meta adapter and single existing credential owner; this is a simple, faithful DIP design without a generic capability platform. Resolve the shared observation fence, reconverge the affected freeze/review evidence, complete the pending planning guards and obtain specific human approval. Performance planning is acceptable: bounded provider calls, pagination, durable quotas, quota-aware fixtures and scan/filter/recheck/buffer measurements are explicit. Operational planning is also acceptable: source admission, additive migration checks, independent wire tests, real PostgreSQL/browser validation and assisted provider proof remain mandatory and unexecuted.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `acceptable`
- **Findings:**
  - [medium] CR-V11-01 Catalog and individual refreshes need an explicit shared observation fence: D07 specifies resource/context leases and fences against changed generations, accounts and credential versions. The API matrix nevertheless introduces two producers of status for the same remote template: catalog refresh and individual draft refresh. Their shared ordering rule is unspecified. A catalog request can capture APPROVED and stall, an individual refresh can record PAUSED, and the older catalog result can then replace that observation while every identity field remains current. UI response fences cannot protect persisted state subsequently returned by GET or reload. This could restore observedEligible=true despite a newer known PAUSED observation, conflicting with DOD-04/05. The existing historical resolutions do not establish ordering across these two producers.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

