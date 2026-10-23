# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-test_quality_audit-r5-dispatch-v1.1.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `hold_for_required_delivery_gates`

## Merged Findings
### F-035510C8 [high] Required delivery evidence remains incomplete
- **Reviewers:** fresh-no-context-r5-tqa
- **Category:** `operational_fit`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `paced`
- **Candidate rule id:** `n/a`
- **Suggested action:** Keep the TODO and delivery state Pending. Execute the remaining gates in their approved order, including any separately authorized canonical diff inspection and preserved-local activation; record passed, blocked, or failed evidence without converting the local candidate into a delivery claim.
- **Rationale:** The package proves a local disposable candidate only. It explicitly lacks the required preserved-runtime migration/source-image validation, operator-assisted own-channel initial sends and replies, remote CI evidence, canonical full diff guard, final review/debt/module closeout, and DOD-11 through DOD-13 evidence. Local E64 success, fake-provider coverage, and image build evidence cannot substitute for those gates.

## Reviewer Summaries
### fresh-no-context-r5-tqa
- **Assessment:** 1. Framing
This is a high-complexity NestJS/Prisma/PostgreSQL plus React/Vite/Docker change. Critical journeys are manual open/reuse without automation, trusted-window enforcement, one bounded initial dispatch, ordinary/initial interlock, recovery/acknowledgement, and compatibility for BFF/public/BOT callers. The meaningful compatibility boundaries are real BFF/session/CSRF/PostgreSQL and a fresh served browser bundle; the external provider is deliberately an owned fake.

2. Five method questions
Q1—Behavior/test delta: the tests reflect real contract changes: durable initial intent/slot state, trusted official timestamps, Channel payload union, exact account/template eligibility, and UI recovery. They assert persisted rows, slot/owner state, query shape, provider-call counts, and browser-visible behavior.
Q2—Pass-the-test workaround risk: no current evidence shows a production test-only route, focused/skipped test, hidden live-provider fallback, or broad always-success stub. Provider doubles are explicit ports; product paths still traverse AppModule, BFF auth/CSRF, Prisma, and PostgreSQL.
Q3—Assertion efficacy: strong locally. Examples include one POST/one Message under same-key concurrency, zero POST for expired/preflight/template-negative cases, known-receipt versus rollback state, owner/CAS preservation, actual signed webhook timestamps, and browser snapshot/reload behavior. These are materially stronger than status-only assertions.
Q4—Assertion efficiency: acceptable. The four Meta-template journeys are independently seeded as claim/preflight, owner-CAS, protocol-shape, and seven eligibility-negative groups, avoiding cross-scenario state dependence while retaining precise counters. The actual 90-second ordinary-risk browser wait is expensive but proportionate to proving that UI deadline behavior.
Q5—Required positive/negative/fault coverage: positive text/template flows, negative context/grant/window/template cases, transaction ACK-loss/rollback, races, stale UI responses, replay, unavailable observations, unknown receipts, and zero-network recovery are covered. Real external provider delivery and preserved-runtime proof are correctly excluded rather than simulated as complete.

3. Chronology
The package does not overstate test-first history. E56/E59/E62 are causal regressions for their named behaviors; E03/E15 are module-loading failures, E04/E25 are mixed/limited, and setup/type/timing/fixture failures are separately classified. Historical resolutions remain closed: nothing in this package materially reopens their loci.

4. Static bypass audit
The complete four-root scan remains high/exit 2 and must not be treated as a raw pass. All 255 reported signals are individually dispositioned: 5 pagination-pattern matches are production pagination rather than skipped tests; 199 status assertions have stated state/UI/persistence/counter companions; 4 no-exception assertions are narrow boot-validation contracts with negative throw coverage; 16 ambient-subject matches are scoped IDs, database clocks, or owned fixture barriers; and 31 mock hints are explicit fault/protocol/port boundaries. The supplemental focused/skipped scan reports zero matches. The supplied dispositions are credible for this candidate; root-level disposition remains review evidence, not independent approval.

5. Dependency injection and fallback
Nest tests compile the real AppModule and deliberately replace META_CLIENT, EVOLUTION_CLIENT, and Typebot ports. Registry overrides test substitutability rather than creating a production route. Real BFF/session/CSRF/PostgreSQL remains in scope; fake-provider counters are not misrepresented as provider TCP calls. No silent mock-to-live fallback is evidenced. Fake-provider parity cannot establish actual Meta/Evolution behavior, which is appropriately left for later operator proof.

6. CI, commands, and platform matrix
Passed locally: canonical `bash scripts/test-channels-local.sh all` at E64, including 28 migrations, lint/build, API unit 368, PostgreSQL 444, web unit 54, and browser 89; the browser run has served-bundle/dist equality and owned cleanup evidence. The local parity self-test is also passed. Alpine image build/offline inspection is evidenced only as a candidate artifact. Remote CI is unknown. Preserved local runtime activation, migration preflight against that runtime, real provider proof, and operator-assisted send/reply are not evidenced.

7. Positions and residuals
Performance is acceptable for the bounded local evidence: indexed plans, batched projections, six-GET/one-POST limits, bounded counters, and deterministic concurrency samples are meaningful, but are not capacity or production-SLO evidence. The design is acceptably narrow: one Channel operation, one Message owner, no provider branching in the coordinator, and no new generic platform. Structural soundness is acceptable based on CAS/readback, owner-token, and DI-contract coverage. Residual inherited debts SEC-R6-04, OPS-R4-01, and TQA-ST05-03 remain carried, not cleared.

8. D01–D10 adherence and delivery boundary
D01 candidate-adherent: atomic manual open/reuse, truthful empty state, no automation, and keyword preservation are tested. D02 candidate-adherent: stale grant/context/channel/credential cases fail before dispatch. D03 candidate-adherent: local escaped preview and server limits are covered. D04 candidate-adherent: union/substitutability, Meta formatting, and Evolution zero-HTTP refusal are covered. D05 candidate-adherent: claim-before-POST, rollback/readback, one-POST, and recovery constraints are tested. D06 candidate-adherent: transaction ordering, echo race, immutable deadline, and owner preservation are covered. D07 candidate-adherent: signed/current-resource official window policy and consumer regressions are covered. D08 candidate-adherent: ordinary/initial exclusion and uncertainty recovery are covered. D09 candidate-adherent: current template eligibility, account pinning, recipient formatting, NAMED/POSITIONAL behavior, and bounded reads are covered. D10 candidate-adherent: limits, bounded budgets, zero-network recovery, and concurrency counters are covered.

This is an acceptable local test-quality candidate, not a delivery conclusion. DOD-11 through DOD-13, remote CI evidence, preserved-runtime/operator proof, module consolidation, and the canonical diff guard remain blocking delivery gates.
- **Recommended path:** `hold_for_required_delivery_gates`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] TQA-R5-01 Required delivery evidence remains incomplete: The package proves a local disposable candidate only. It explicitly lacks the required preserved-runtime migration/source-image validation, operator-assisted own-channel initial sends and replies, remote CI evidence, canonical full diff guard, final review/debt/module closeout, and DOD-11 through DOD-13 evidence. Local E64 success, fake-provider coverage, and image build evidence cannot substitute for those gates.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

