# PACED Subagent Dispatch: architecture_adherence

## Dispatch Identity
- **Artifact kind:** `subagent_review_dispatch`
- **Authoritative:** `false`
- **Edit policy:** `derived_dispatch_packet`
- **Review kind:** `architecture_adherence`
- **Bounded package:** `foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence-cp1-r8-package.json`
- **Reviewer count:** `1`
- **No-context required:** `true`

## Required Axes
- `adherence`
- `structural_soundness`
- `operational_fit`
- `performance`
- `elegance`

## Focus Points
- Compare the delivered bounded package against the frozen Architecture Change Governance contract and Decision Baseline.
- Identify any implementation path, temporary exception, or missing protection harness that diverges from the approved target steady-state.
- Do not redesign the approved architecture unless the delivered evidence exposes a material defect or an approval-breaking divergence.
- For each material finding, add category and formalizable-hint when you can judge them honestly.
- When assessing design, seek the simplest faithful Clean Code/SOLID design for the approved intent. Do not invent future-facing work or erase explicit TODO intent. Planning review may challenge proposed intent; delivery review must preserve approved intent or return for renewed approval.

## Required Result Fields
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings[].finding_id (optional)`
- `findings[].category (optional)`
- `findings[].formalizable_hint (optional)`
- `findings[].candidate_rule_level (optional)`
- `findings[]`

## Required Result Binding
The reviewer result's `dispatch_path` must equal this exact dispatch JSON path:
`/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/adherence-cp1-r8-dispatch.json`
Do not substitute the bounded package path, governing TODO path, or reviewer output path.

## Related TODO
`foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md`

Reviewers must cross-check findings against the governing TODO's explicit decisions, approved exceptions, compatibility mandates, and non-goals before classifying something as blocking drift.

## Historical Finding Carry-Forward
Previously adjudicated findings are historical context, not automatic reopening triggers.
- Resolved findings are historical context only. Do not reopen them unless the current bounded package materially changes the same locus/behavior or fresh evidence shows regression.
- Challenged findings stay closed unless the current bounded package materially changes the same locus/behavior or the prior rationale is objectively insufficient.
- Deferred findings must cite the recorded follow-up/waiver path first. Re-raise them only when the current bounded package changes the same locus or closure now depends on that deferred risk.
- Unresolved findings remain valid to re-raise until they are fixed, challenged, or formally deferred with authority.

### Recorded Dispositions
- `promotion_routing / IG-CP1-R1-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r2
  - Summary: immutable qualified peer is SCOPE-02/DOD-01
  - Reference: adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance
- `promotion_routing / IG-CP1-R1-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r3
  - Summary: current provider attachment equality is SCOPE-02/DOD-01
  - Reference: adherence-cp1-r3-result.json; final persisted association defect repaired; actual official confirmation proved
- `promotion_routing / IG-CP1-R1-03` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r5
  - Summary: durable cross-adapter resource ownership is SCOPE-02/DOD-01
  - Reference: adherence-cp1-r5-result.json; exact current quarantine recovery after actual prior receipt
- `promotion_routing / IG-CP1-R1-04` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r2
  - Summary: qualified contact reuse is SCOPE-02,03
  - Reference: adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance
- `promotion_routing / IG-CP1-R1-05` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r2
  - Summary: retained ownership/cardinality is SCOPE-02/DOD-01
  - Reference: adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance
- `promotion_routing / IG-CP1-R1-06` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r2
  - Summary: safe canonical migration is DOD-02/VAL-02
  - Reference: adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance
- `promotion_routing / IG-CP1-R1-07` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r5
  - Summary: preserved regression tests are SCOPE-08/DOD-09
  - Reference: cp1-frozen-full-api-green-r5.json; complete379unit/483e2e GREEN on matching37sources
- `promotion_routing / IG-CP1-R1-08` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r2
  - Summary: required historical cohort is DOD-02/VAL-02
  - Reference: adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance
- `promotion_routing / IG-CP1-R2-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r3
  - Summary: one coherent WA business scope is SCOPE-02/DOD-01
  - Reference: adherence-cp1-r3-result.json; WA business scope BU agrees with CHECK/FK and actual positive route
- `promotion_routing / IG-CP1-R2-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r3
  - Summary: honest unverified renewal staging is SCOPE-02/DOD-01
  - Reference: adherence-cp1-r3-result.json; original reservation/proof defect repaired; distinct pending lifecycle findings remain below
- `promotion_routing / IG-CP1-R3-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r5
  - Summary: single-create/read-before-retry after pending renewal is SCOPE-02/08
  - Reference: adherence-cp1-r5-result.json; single create and read-before-retry retained
- `promotion_routing / IG-CP1-R3-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r5
  - Summary: managed cleanup ownership survives staged unlink under SCOPE-02/08
  - Reference: adherence-cp1-r5-result.json; current staged unlink and stale snapshot fence repaired
- `promotion_routing / IG-CP1-R3-03` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r5
  - Summary: durable quarantine and later correct-proof recovery preserve existing channel contract
  - Reference: adherence-cp1-r5-result.json; wrong-number quarantine and correct-proof recovery retained
- `promotion_routing / IG-CP1-R3-04` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r5
  - Summary: required ownership concurrency proof cannot assume winner scheduling; fix assertions in this TODO
  - Reference: adherence-cp1-r5-result.json; actual-winner concurrency assertion retained
- `promotion_routing / IG-CP1-ROOT-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in this TODO; status=closed by r5
  - Summary: pending current ingress remains retryable without content/trust before proof
  - Reference: adherence-cp1-r5-result.json; metadata-only staged retry and accepted-key proof retained
- `promotion_routing / IG-CP1-R4-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=repeat affected proof in this TODO; status=closed by r5
  - Summary: four mutations violated the explicit r4 freeze; preserve evidence and validate current bytes anew
  - Reference: adherence-cp1-r5-result.json; cp1-frozen-full-api-green-r5.json; new stable proof replaces invalidated acceptance
- `promotion_routing / IG-CP1-R5-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=bounded companion in this TODO; protected path validation required; status=open; admitted guard applied, fresh proof/review pending
  - Summary: current staged cleanup guarantee depends on a truthful absence observation; inherited adapter weakness is not a new Instagram regression
  - Reference: evolution-observation-companion-user-validation.json; cp1-observation-r8-targeted-green.json
- `promotion_routing / IG-EVOCOMP-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix admitted caller lifecycle in this TODO; status=closed by r3/current full API; protected parser remains R5-01
  - Summary: conclusive cleanup must recover same reserved operation and permit one create, without widening protected paths
  - Reference: evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json
- `promotion_routing / IG-EVOCOMP-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=strengthen proposed tests before source admission; status=proposal resolved r2; implementation not admitted
  - Summary: independent malformed name/state and null projection branches need concrete proof plan
  - Reference: evolution-observation-companion-critique-r2-result.json
- `promotion_routing / IG-EVOCOMP-03` -> `resolved`
  - Disposition: classification=release-blocker; routing=correct proposal wording before validation; status=proposal resolved r2; implementation not admitted
  - Summary: exact subject and absence contract must be clear to approving user; small same-artifact correction
  - Reference: evolution-observation-companion-critique-r2-result.json
- `promotion_routing / IG-EVOCOMP-R2-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fence late failure mutation in same admitted caller/test paths; status=closed by r3/current full API
  - Summary: same-attempt recovery must retain later holder facts after lease takeover; inherited catch is not a new adapter regression
  - Reference: evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json
- `promotion_routing / IG-CP1-ROOT-R7-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=revalidate authorization before provider-error fact mutation in same admitted paths; status=closed by r3/current full API
  - Summary: live DB lease does not replace post-call session/grant revalidation; same existing lifecycle contract, no new middleware scope
  - Reference: evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json

## Result Contract
Return exactly one JSON object and no Markdown fence or prose.
Do not emit `null`; omit optional fields that do not apply.
No top-level fields other than the following are allowed:
- `schema_version`: `subagent-review-result-v1`
- `artifact_kind`: `subagent_review_result`
- `dispatch_path`: the exact binding shown above
- `review_kind`: `architecture_adherence`
- `reviewer_label`
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings`

Every `*_position` value must be one of: `strong_positive`, `acceptable`, `mixed`, `regresses`, `unknown`, `not_evaluated`.
Each finding may contain only these fields:
- required: `severity`, `title`, `rationale`, `suggested_action`
- optional: `finding_id`, `category`, `formalizable_hint`, `candidate_rule_level`, `candidate_rule_id`, `affected_paths`
- `severity` values: `low`, `medium`, `high`
- `category` values: `architecture`, `adherence`, `tests`, `performance`, `security`, `elegance`, `structural_soundness`, `operational_fit`, `residual_risk`, `other`
- `formalizable_hint` values: `yes`, `partial`, `no`, `unknown`
- `candidate_rule_level` values: `paced`, `project`, `none`, `unknown`

