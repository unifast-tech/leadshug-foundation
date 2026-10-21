# PACED Subagent Review Merge: architecture_opinion

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/architecture-v1.1.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Retain D09's narrow TemplateManagementResolver/MessageTemplateProvider capability, dedicated Meta adapter, single existing credential owner and template-domain ownership of durable operations and observations. This is the simplest faithful path presented. Its main tradeoff is additional persistent state and explicit recovery work in exchange for bounded dispatch and honest uncertainty. The separation improves elegance and structural soundness while preserving the textual Channel boundary. Existing send performance should remain neutral; management adds bounded sequential I/O, with no measured performance improvement established.`

## Merged Findings
### F-D4A176AF [medium] The inherited seal needs an initial check of all 41 records
- **Reviewers:** fresh-internal-architecture-v1.1
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Require an initial admission receipt comparing product HEADs and all 41 public file hashes before the first ST05 mutation or test. Thereafter, retain exact checks for the 30 sealed files and review admitted-file changes against immutable public evidence of the inherited baseline. Record checks at the required checkpoints without creating another checkout, committing product history or discovering private paths.
- **Rationale:** The manifest's enforcement checks exact hashes only for records with active_mutation_admitted=false. Consequently, unrelated drift already present in any of the 11 admitted shared files can pass the stated seal before ST05 starts. Strict path admission and later regression tests cannot establish that those initial contents were the reviewed ST06 baseline, particularly because product HEADs predate that baseline.

### F-012B2896 [medium] Local commit uncertainty needs an explicit submission contract
- **Reviewers:** fresh-internal-architecture-v1.1
- **Category:** `architecture`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Before APROVADO, specify positive confirmation of the original dispatch claim before HTTP, bounded readback using the captured operation/claim, and finalization rules distinguishing known external acceptance from confirmed local persistence. Unconfirmed persistence must preserve recovery and must not authorize another POST or premature reservation release. Add PostgreSQL fault cases for rollback before commit and successful commit with lost acknowledgement around reservation, dispatch claim and receipt finalization.
- **Rationale:** D05/D06 and CR-02 classify provider results and process crashes, but do not define behavior when reserving, claiming SENDING, or persisting the final receipt commits successfully while Prisma reports an error. A valid provider ID also establishes external acceptance before local receipt persistence is confirmed. The package currently lacks the response, readback and reservation rules for these cases. The historical recovery contract addresses lost processes and competing recoverers; it does not resolve uncertain transaction acknowledgements.

### F-DC811F7B [medium] Account-wide coordination assumes an unstated tenant ownership invariant
- **Reviewers:** fresh-internal-architecture-v1.1
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Resolve this topology before approval: either establish and prove an enforced exclusive WABA-to-mantenedora ownership invariant, or coordinate reservations and account quotas using a canonical remote-account namespace shared across every binding of that account. Preserve tenant/BU authorization and safe conflict responses. Require concurrency tests for the same account through different bindings, including the cross-tenant case if admitted, and prove that identical names in different accounts remain independent.
- **Rationale:** D05 namespaces reservations by mantenedora/account/name/language. The embedded schema enforces ownership of individual provider phone identities, but provides no exclusive WABA-to-mantenedora invariant. If distinct verified phones in the same WABA can belong to different mantenedoras, their reservations remain independent even though Meta's template namespace is shared. Both submissions can pass preflight and dispatch for the same remote name/language. Account quota enforcement needs the same canonical account identity.

## Reviewer Summaries
### fresh-internal-architecture-v1.1
- **Assessment:** The architectural direction is sound, but these planning gaps should be resolved before APROVADO. Seller authority, management versus send readiness, conservative correlation, status truth, UI fences and independent wire/real-backend validation are otherwise coherently specified. This assessment establishes no implementation or runtime pass.
- **Recommended path:** `Retain D09's narrow TemplateManagementResolver/MessageTemplateProvider capability, dedicated Meta adapter, single existing credential owner and template-domain ownership of durable operations and observations. This is the simplest faithful path presented. Its main tradeoff is additional persistent state and explicit recovery work in exchange for bounded dispatch and honest uncertainty. The separation improves elegance and structural soundness while preserving the textual Channel boundary. Existing send performance should remain neutral; management adds bounded sequential I/O, with no measured performance improvement established.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] AR-V11-01 Local commit uncertainty needs an explicit submission contract: D05/D06 and CR-02 classify provider results and process crashes, but do not define behavior when reserving, claiming SENDING, or persisting the final receipt commits successfully while Prisma reports an error. A valid provider ID also establishes external acceptance before local receipt persistence is confirmed. The package currently lacks the response, readback and reservation rules for these cases. The historical recovery contract addresses lost processes and competing recoverers; it does not resolve uncertain transaction acknowledgements.
  - [medium] AR-V11-02 Account-wide coordination assumes an unstated tenant ownership invariant: D05 namespaces reservations by mantenedora/account/name/language. The embedded schema enforces ownership of individual provider phone identities, but provides no exclusive WABA-to-mantenedora invariant. If distinct verified phones in the same WABA can belong to different mantenedoras, their reservations remain independent even though Meta's template namespace is shared. Both submissions can pass preflight and dispatch for the same remote name/language. Account quota enforcement needs the same canonical account identity.
  - [medium] AR-V11-03 The inherited seal needs an initial check of all 41 records: The manifest's enforcement checks exact hashes only for records with active_mutation_admitted=false. Consequently, unrelated drift already present in any of the 11 admitted shared files can pass the stated seal before ST05 starts. Strict path admission and later regression tests cannot establish that those initial contents were the reviewed ST06 baseline, particularly because product HEADs predate that baseline.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

