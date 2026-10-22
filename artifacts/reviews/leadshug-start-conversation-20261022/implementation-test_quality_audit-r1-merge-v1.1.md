# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-test_quality_audit-r1-dispatch-v1.1.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `Correct the Unicode client/server contract mismatch, add focused regression coverage for it and for both acknowledgement-eligible states, then obtain a terminal full E47 run with cleanup and independent postseal before advancing to the separately required runtime and delivery gates.`

## Merged Findings
### F-B25EB3CF [high] Required full browser-platform evidence is not terminal for the current E47 source seal
- **Reviewers:** fresh-no-context-tqa-r1
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `paced`
- **Candidate rule id:** `terminal-required-platform-evidence`
- **Suggested action:** Wait for or rerun the complete E47 browser command on the frozen source, retain terminal output and cleanup evidence, and perform the independent postseal before treating browser coverage as passed or requesting activation/delivery review.
- **Rationale:** The individual E47 ordinary-recovery case is meaningful and passed, while E45 and the pre-existing 85 E46 browser cases provide strong composite evidence. Nevertheless, the remaining E47 browser run is explicitly RUNNING, with no terminal exit, cleanup, or independent postseal for fingerprint 603cc71. The required browser platform must remain blocked rather than be inferred from the individual case. Actual preserved-runtime and operator proof are also explicitly later gates, not validated by the owned fake-provider topology.

### F-8D9F2A1C [high] Browser snapshot and input limits use UTF-16 length while server template validation uses Unicode code points
- **Reviewers:** fresh-no-context-tqa-r1
- **Category:** `structural_soundness`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `client-server-unicode-length-parity`
- **Suggested action:** Make browser input and snapshot validation enforce the same code-point limits as the server, preserving JSON-size protection separately. Add unit and real-browser cases accepting exactly 1,024/4,096 astral characters where applicable and rejecting one additional code point; rerun the canonical browser suite.
- **Rationale:** The renderer deliberately counts values and rendered text with Array.from, so 1,024 astral Unicode characters are valid. NovaConversa instead applies HTML maxLength={1024} and snapshot validation item.length > 1024, both UTF-16-code-unit based; the same mismatch exists for the 4,096-character text textarea. Existing tests cover 1,024 control characters and server-side emoji handling, but not the cross-layer astral-character boundary. A contract-valid message can consequently be blocked by the browser and the tests will not detect it.

### F-9EFF5F01 [medium] Test-first evidence is partial; most behavior-defining fault and protocol coverage is retrofit evidence
- **Reviewers:** fresh-no-context-tqa-r1
- **Category:** `tests`
- **Formalizable hint:** `no`
- **Candidate rule level:** `none`
- **Candidate rule id:** `n/a`
- **Suggested action:** Keep the causal chronology matrix and classify post-implementation cases as regression evidence only. Do not promote them to fail-first proof; require fail-first evidence for future behavior changes and preserve this limitation through final TQA and delivery assessment.
- **Rationale:** The record honestly establishes selected causal REDs, notably E03, E04 renderer/UI findings, E11, E21/22, E25, E35, E41, and E44. It also explicitly records that most later fault, protocol, boundary, and concurrency tests were written alongside or after implementation. Those tests are useful final-state regression coverage, but cannot support a broad claim that the entire approved behavior was developed test-first.

### F-B360C531 [medium] Acknowledgement coverage does not fully exercise EXTERNAL_ACCEPTED_LOCAL_BLOCKED through the BFF lifecycle
- **Reviewers:** fresh-no-context-tqa-r1
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `acknowledge-both-initial-risk-states`
- **Suggested action:** Add a real PostgreSQL/BFF test that reaches EXTERNAL_ACCEPTED_LOCAL_BLOCKED, proves ACK_TOO_EARLY with no release, then proves post-deadline release, successor isolation, and zero additional provider calls. A focused browser recovery case is appropriate if that state is actionable in the UI.
- **Rationale:** The pure eligibility predicate covers both AMBIGUOUS and EXTERNAL_ACCEPTED_LOCAL_BLOCKED, and AMBIGUOUS is exercised through BFF acknowledgement. The supplied endpoint/browser flows do not similarly prove early rejection, post-deadline irreversible release, successor fencing, and no resend for EXTERNAL_ACCEPTED_LOCAL_BLOCKED. The governing critique explicitly requires both classified states because the latter contains a known external acceptance and is an irreversible release path.

## Reviewer Summaries
### fresh-no-context-tqa-r1
- **Assessment:** Mixed. The supplied evidence substantively exercises the changed contract through unit/adapter tests, real Nest BFF plus disposable PostgreSQL, and a freshly served React browser against an owned protocol fake. Assertions generally verify business state, durable rows, authorization, exact replay identity, provider counters, and negative effects rather than status-only outcomes. The E46 counter correction is aligned with actual fake instrumentation, not a pass-the-test product workaround; no supplied evidence shows focused/skipped tests, test-only product routes, silent real-boundary fallback, or DI-token bypass. However, browser/server Unicode-limit parity is untested and appears inconsistent, the irreversible EXTERNAL_ACCEPTED_LOCAL_BLOCKED acknowledgement path lacks full endpoint-level coverage, and most fault/protocol tests are post-implementation rather than causal fail-first evidence. E45 is terminal green, but full E47 remains nonterminal; therefore required browser-platform status is blocked and this candidate is not delivery-ready.
- **Recommended path:** `Correct the Unicode client/server contract mismatch, add focused regression coverage for it and for both acknowledgement-eligible states, then obtain a terminal full E47 run with cleanup and independent postseal before advancing to the separately required runtime and delivery gates.`
- **Performance:** `acceptable`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] TQA-ST04-01 Browser snapshot and input limits use UTF-16 length while server template validation uses Unicode code points: The renderer deliberately counts values and rendered text with Array.from, so 1,024 astral Unicode characters are valid. NovaConversa instead applies HTML maxLength={1024} and snapshot validation item.length > 1024, both UTF-16-code-unit based; the same mismatch exists for the 4,096-character text textarea. Existing tests cover 1,024 control characters and server-side emoji handling, but not the cross-layer astral-character boundary. A contract-valid message can consequently be blocked by the browser and the tests will not detect it.
  - [high] TQA-ST04-02 Required full browser-platform evidence is not terminal for the current E47 source seal: The individual E47 ordinary-recovery case is meaningful and passed, while E45 and the pre-existing 85 E46 browser cases provide strong composite evidence. Nevertheless, the remaining E47 browser run is explicitly RUNNING, with no terminal exit, cleanup, or independent postseal for fingerprint 603cc71. The required browser platform must remain blocked rather than be inferred from the individual case. Actual preserved-runtime and operator proof are also explicitly later gates, not validated by the owned fake-provider topology.
  - [medium] TQA-ST04-03 Acknowledgement coverage does not fully exercise EXTERNAL_ACCEPTED_LOCAL_BLOCKED through the BFF lifecycle: The pure eligibility predicate covers both AMBIGUOUS and EXTERNAL_ACCEPTED_LOCAL_BLOCKED, and AMBIGUOUS is exercised through BFF acknowledgement. The supplied endpoint/browser flows do not similarly prove early rejection, post-deadline irreversible release, successor fencing, and no resend for EXTERNAL_ACCEPTED_LOCAL_BLOCKED. The governing critique explicitly requires both classified states because the latter contains a known external acceptance and is an irreversible release path.
  - [medium] TQA-ST04-04 Test-first evidence is partial; most behavior-defining fault and protocol coverage is retrofit evidence: The record honestly establishes selected causal REDs, notably E03, E04 renderer/UI findings, E11, E21/22, E25, E35, E41, and E44. It also explicitly records that most later fault, protocol, boundary, and concurrency tests were written alongside or after implementation. Those tests are useful final-state regression coverage, but cannot support a broad claim that the entire approved behavior was developed test-first.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

