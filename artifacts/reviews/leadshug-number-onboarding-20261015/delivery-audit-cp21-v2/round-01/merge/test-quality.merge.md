# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/delivery-audit-cp21-v2/round-01/dispatch/test-quality.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `Accept the local test suite as evidence of implementation readiness, including the final manifest and targeted WSLENV config-only validation; do not attribute that post-all script delta to the earlier all run. Keep the governing TODO active and do not claim completion or production readiness until VAL-05 executes with real Meta authorization, actual device pairing, and real IN/OUT evidence for both modalities. Preserve the delivery's mixed/test-after provenance rather than reconstructing historical RED evidence.`

## Merged Findings
### F-5BF94B94 [high] VAL-05 real-provider and device proof remains an overall-close blocker
- **Reviewers:** cp21-native-test-quality
- **Category:** `residual_risk`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `VAL-05`
- **Suggested action:** Keep the TODO active and execute the approved external VAL-05 matrix when authorized test targets are available: Embedded Signup and selected official resource, QR/device pairing and identity verification, authenticated IN to the correct BU/inbox, actual OUT received by the interlocutor, and permitted recovery for each modality. Record redacted build/target/time outcomes; do not substitute provider doubles or repeat audits merely to restate this known gap.
- **Rationale:** DOD-05 and VAL-05 require actual Meta authorization, real QR/device pairing, and real IN/OUT plus recovery per modality. The packet and handoff explicitly record that no real Meta authorization, pairing, or real IN/OUT occurred; current runtime evidence is limited to configuration booleans and synthetic provider/header/ingress probes. The passing local suite establishes local behavior and harness fidelity, not this external boundary. This does not invalidate local implementation readiness, but it blocks overall TODO closure.

### F-8CD8BF35 [medium] Fail-first provenance is incomplete despite effective final regression coverage
- **Reviewers:** cp21-native-test-quality
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Classify the slice as mixed/test-after in closeout and do not fabricate historical RED evidence. For a future behavior-defining change or defect correction, capture a failing product-level test before the fix or record an explicit not-applicable rationale; retain the present barriers and negative controls as final regression protection.
- **Rationale:** The delivery history correctly identifies the cp18 fail-first log as a Compose preflight failure and the cp20 former-guard exercise as reconstructed test-after evidence. Browser FRC did expose a genuine defect, and the final tests are substantive rather than pass-the-test assertions, but no authentic pre-fix RED covers every behavior-defining contract. This is verification-process debt, not evidence that the current local behavior lacks regression protection.

## Reviewer Summaries
### cp21-native-test-quality
- **Assessment:** Local implementation readiness is acceptable, with strong regression protection but not overall TODO closure. The source-owned canonical runner passed 21 migrations, 138 API unit tests, 282 PostgreSQL E2E tests, 28 web unit tests, and 44 Playwright tests using real BFF, session, PostgreSQL, and served-bundle paths. Assertions cover meaningful state, database effects, authorization negatives, provider-call counts, CAS/lease barriers, stale UI responses, and the local clauses of REG-SEC-01..13; external SDK/provider doubles remain confined to adapter boundaries and preserve production DI tokens. Bounded scans found no skip/focus bypasses or inline verification-debt markers in the changed review scope. Performance evidence is appropriately bounded and honest: no provider fan-out was observed for scoped listing, while EPS makes no unsupported SLO or capacity claim. D-01..D-10 appear locally adhered to, including the approved migrated-slot exception. Fail-first provenance is mixed: final regression coverage is effective, but the delivery cannot honestly be called wholly test-first.
- **Recommended path:** `Accept the local test suite as evidence of implementation readiness, including the final manifest and targeted WSLENV config-only validation; do not attribute that post-all script delta to the earlier all run. Keep the governing TODO active and do not claim completion or production readiness until VAL-05 executes with real Meta authorization, actual device pairing, and real IN/OUT evidence for both modalities. Preserve the delivery's mixed/test-after provenance rather than reconstructing historical RED evidence.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] TQA-CP21-01 VAL-05 real-provider and device proof remains an overall-close blocker: DOD-05 and VAL-05 require actual Meta authorization, real QR/device pairing, and real IN/OUT plus recovery per modality. The packet and handoff explicitly record that no real Meta authorization, pairing, or real IN/OUT occurred; current runtime evidence is limited to configuration booleans and synthetic provider/header/ingress probes. The passing local suite establishes local behavior and harness fidelity, not this external boundary. This does not invalidate local implementation readiness, but it blocks overall TODO closure.
  - [medium] TQA-CP21-02 Fail-first provenance is incomplete despite effective final regression coverage: The delivery history correctly identifies the cp18 fail-first log as a Compose preflight failure and the cp20 former-guard exercise as reconstructed test-after evidence. Browser FRC did expose a genuine defect, and the final tests are substantive rather than pass-the-test assertions, but no authentic pre-fix RED covers every behavior-defining contract. This is verification-process debt, not evidence that the current local behavior lacks regression protection.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

