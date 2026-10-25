# PACED Subagent Review Merge: critique

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/parser149-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Refine protocol149 before source authoring. Reusing the actual compiled parser in one owned loopback child is scope-faithful, simple, and bounded in resource use. Resolve the byte-vector, capture-contract, and evidence-state issues below, then implement only in the admitted integration test and validate through the canonical runner. Preserve existing gateway assertions and all remaining delivery gates; this review establishes no runtime or security acceptance.`

## Merged Findings
### F-034DB678 [medium] The remaining RED prerequisite conflicts with the applied exact-lock boundary
- **Reviewers:** fresh-internal-parser149
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `paced`
- **Candidate rule id:** `n/a`
- **Suggested action:** Rewrite the execution sequence consistently as postpatch-only validation. Preserve prepatch crash and causal RED as NOTRUN, distinguish harness/vector failures from process termination, and limit passing claims to the exact exercised current scenario. Remove the requirement to obtain old-version RED from this lane; any later old-version comparison requires a separately bounded admission.
- **Rationale:** The protocol state correctly records that lock153 is applied and no prepatch crash was executed. However, its open questions still require reproduction to be established by an actual canonical RED, and step 5 retains the obsolete 'unpatched current2.3.0' sequence. Under the governing TODO, only the exact admitted 2.4.0 lock is current, package substitution is prohibited, and historical causal RED cannot be inferred. Leaving both instructions active creates an impossible gate or pressure to exceed the authorized package boundary.

### F-5EE2D979 [medium] The form-parser rawBody oracle contradicts the actual configuration
- **Reviewers:** fresh-internal-parser149
- **Category:** `adherence`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Define expectations separately for all four parser contexts. Require exact inflated logical-byte capture and digest where captureRaw actually runs. For URL-encoded forms, assert the exact parsed structure and the existing absence of rawBody capture. Do not add a wrapper capture or production verify callback to satisfy this test.
- **Rationale:** Step 2 requests a rawBody digest from actual capture across the compatibility inputs. configurarBodyParsers installs captureRaw on shared JSON, OAuth JSON, and Instagram raw parsing, but express.urlencoded({ extended: true }) has no verify callback. A form request therefore supplies no captured rawBody. Satisfying a universal digest assertion would require fabricating a capture or changing the production configuration, contrary to the parser-only boundary.

### F-CF775D56 [medium] The decisive compressed-byte vector and completion sequence remain unresolved
- **Reviewers:** fresh-internal-parser149
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Specify one primary-supported deterministic vector: encoding, logical payload, complete compressed frame, marker, exact trailing bytes, and Content-Length equal to the complete wire body. Define the sequence as healthy compressed control, flushed prefix, correlated parser-completion IPC, trailing delivery and request end, complete 200 with exact payload/capture checks, same-child health, then graceful shutdown and natural exit 0. Handle already-ended request streams, reject aborts and premature closes, and treat every watchdog or forced termination as failure. Include the relevant primary test excerpt or explicitly limit the scenario to a constructed postpatch compatibility probe.
- **Rationale:** Step 3 permits either deflate or gzip, one zero marker, and unspecified remaining padding. The enclosed read.js diff identifies the cleanup locus, but the referenced maintainer regression test body is absent. Consequently, the package does not establish which exact prefix causes parser completion before HTTP completion or which later bytes exercise the intended decoder boundary. A successful patched run alone cannot establish that fidelity. Terminal success also needs an explicit rule preventing cleanup termination from masking a pending decoder failure.

## Reviewer Summaries
### fresh-internal-parser149
- **Assessment:** changes_required
- **Recommended path:** `Refine protocol149 before source authoring. Reusing the actual compiled parser in one owned loopback child is scope-faithful, simple, and bounded in resource use. Resolve the byte-vector, capture-contract, and evidence-state issues below, then implement only in the admitted integration test and validate through the canonical runner. Preserve existing gateway assertions and all remaining delivery gates; this review establishes no runtime or security acceptance.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] IG-PARSER149-01 The decisive compressed-byte vector and completion sequence remain unresolved: Step 3 permits either deflate or gzip, one zero marker, and unspecified remaining padding. The enclosed read.js diff identifies the cleanup locus, but the referenced maintainer regression test body is absent. Consequently, the package does not establish which exact prefix causes parser completion before HTTP completion or which later bytes exercise the intended decoder boundary. A successful patched run alone cannot establish that fidelity. Terminal success also needs an explicit rule preventing cleanup termination from masking a pending decoder failure.
  - [medium] IG-PARSER149-02 The form-parser rawBody oracle contradicts the actual configuration: Step 2 requests a rawBody digest from actual capture across the compatibility inputs. configurarBodyParsers installs captureRaw on shared JSON, OAuth JSON, and Instagram raw parsing, but express.urlencoded({ extended: true }) has no verify callback. A form request therefore supplies no captured rawBody. Satisfying a universal digest assertion would require fabricating a capture or changing the production configuration, contrary to the parser-only boundary.
  - [medium] IG-PARSER149-03 The remaining RED prerequisite conflicts with the applied exact-lock boundary: The protocol state correctly records that lock153 is applied and no prepatch crash was executed. However, its open questions still require reproduction to be established by an actual canonical RED, and step 5 retains the obsolete 'unpatched current2.3.0' sequence. Under the governing TODO, only the exact admitted 2.4.0 lock is current, package substitution is prohibited, and historical causal RED cannot be inferred. Leaving both instructions active creates an impossible gate or pressure to exceed the authorized package boundary.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

