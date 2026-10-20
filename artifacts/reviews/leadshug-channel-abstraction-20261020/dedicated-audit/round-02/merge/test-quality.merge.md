# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/round-02/dispatch/test-quality.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `return_for_targeted_public_contract_coverage_and_required_operational_gate_completion`

## Merged Findings
### F-B32947BC [high] Required real-provider official and unofficial IN/OUT gate remains unexecuted
- **Reviewers:** fresh_no_context_tqa_round02
- **Category:** `operational_fit`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** After authorized local activation and HTTPS restoration, collect fresh redacted IN/OUT and canonical readback evidence for both owned bindings against the reviewed source. Keep remote CI separately not_run unless later authorized promotion executes it.
- **Rationale:** The package correctly distinguishes controlled-provider, real-BFF/PostgreSQL evidence from external-provider proof, but DOD-07 and VAL-04 still require fresh post-activation official and unofficial operator IN/OUT. No waiver is supplied, so automated fixture success cannot close the delivery-integrity gap.

### F-D333D5E8 [high] Public availability contract lacks negative-path and thread-endpoint regression coverage
- **Reviewers:** fresh_no_context_tqa_round02
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `public-contract-field-negative-and-endpoint-coverage`
- **Suggested action:** Add real-PostgreSQL public API tests covering available and deterministic unavailable selected bindings. Assert exact list and thread availability/reason fields, then assert POST blocks without provider calls or a new OUT Message for the unavailable case.
- **Rationale:** The public controller adds `envio_disponivel` and `motivo_indisponibilidade` to both list and thread responses, but the supplied `api-publica.e2e-spec.ts` asserts only an available list row. A broken or omitted thread projection, or an unavailable selected binding reported as available, can pass all supplied tests despite violating D07 and the public contract.

## Reviewer Summaries
### fresh_no_context_tqa_round02
- **Assessment:** # Complete test-quality assessment — return for targeted remediation

## Framing

This is a big, cross-stack NestJS/React/Prisma change covering public API semantics, external-send outcome handling, tenant isolation, async UI behavior, a managed PostgreSQL index, and CI-equivalent lifecycle ownership. The package credibly supports the limited claim that the frozen candidate passed its local disposable Linux CI-equivalent run: `194` API unit, `312` real-PostgreSQL E2E, `29` Web unit, and `50` Chromium tests, with source and served-bundle provenance. It does not support a Local-Implemented, real-provider, remote-CI, or production claim; those are expressly pending and not waived.

Test effectiveness is mixed rather than acceptable for closure. Most high-risk behavior has meaningful multi-layer proof, including real PostgreSQL, BFF/browser flow, adapter-level raw HTTP classification, causal omission mutants, and no-retry assertions. However, the changed public availability contract lacks negative-path and thread-endpoint assertions, so an externally visible D07 behavior could regress while the supplied suite remains green. Required real official/unofficial operator IN/OUT evidence is also still blocked, so this audit cannot be used as delivery completion evidence.

## Architecture

The package shows one shared `Channel` / `ChannelResolver` / `OutboundService` path and retains `MessageAcceptanceService` as the sole keyed Message writer. `channel-dependencies.spec.ts` scans the common consumer area and proves its detector using synthetic violating imports and provider branches. The opaque-recipient E2E test uses the real resolver, BFF, PostgreSQL, and a registered adapter factory, rather than testing a second artificial sender path.

No final cutover fallback, dual write, test-only production route, provider switch in common consumers, or singleton credential mutation is evidenced. Protocol-specific clients remain in adapters and registration paths, consistent with D01, D06, D08, and D09.

## Code Quality

The code separates adapter classification, dispatch fences, acceptance, finalization, and presentation cleanly. Typed result states prevent transport ambiguity from being silently treated as success or refusal. The test code is generally readable and uses owned fixtures, fixed barriers, direct persisted-state checks, and descriptive negative controls.

There is some necessary harness complexity in the Docker transport and causal-browser test. It is proportionate to the topology and race being proven: the production bundle is not instrumented, the fetch wrapper preserves the real response, and the exact guard-removal mutant fails the intended assertion. The remaining concern is coverage, not a pass-the-test implementation shortcut.

## Tests

### Five mandatory audit answers

1. **Real contract change versus test repair:** The outcome, dispatch-fence, batching/index, CI-admission, and composer tests align with real behavior changes. The indexless RED, real adapter-callback omission mutants, and stale-draft guard-removal mutant establish that these tests are not merely accepting the final state.
2. **Pass-the-test workaround risk:** No brittle production-only hook, test-only product endpoint, ambient first-row selection, skip, focused test, broad success stub, retry acceptance, or silent mock fallback was found in the supplied material. Test fixture routes are isolated in `api-app/test`, guarded by owned fixture subjects and disposable databases, and browser requests still traverse the actual BFF and PostgreSQL.
3. **Assertion effectiveness:** Strong for adapter envelopes, one-POST behavior, zero-provider-call blocked paths, tenant/resource pairing, Message persistence, echo reconciliation, generation fencing, draft preservation, and index scan conditions. Weak for the new public availability fields because only the positive public-list case is asserted.
4. **Assertion efficiency:** Efficient overall. The real-PostgreSQL and browser cases are serialized intentionally, while the test suite avoids redundant provider calls and uses bounded subjects. The 500-reference plan probe and five-by-twenty concurrency probes are purposeful, not timing-only performance theater.
5. **Coverage of required behavior and failure modes:** Strong across BFF, Typebot, public mutation, clients, persistence, browser behavior, and runner lifecycle. Incomplete for public API availability reasons and the public thread response, plus the explicitly pending real-provider operator gate.

### Fail-first, test-after, and retrofit status

| Critical change | Status | Evidence |
| --- | --- | --- |
| Meta contradictory success classification | Fail-first remediation | Recorded R05 RED preceded the conservative UNKNOWN behavior; raw-client and real-PG persistence tests cover it. |
| Adapter pre-dispatch fencing | Mutation-proven | Removing the shipping Meta/Evolution callback causes the expected `409` versus `201` failure and is restored byte-exactly. |
| A-to-B-to-A stale draft fence | Mutation-proven retrofit remediation | The native `response.text()` settlement plus browser-task barrier is followed by an exact generation-guard omission mutant that fails only the intended draft assertion. |
| Direction-constrained latest-IN index | Fail-first remediation | Indexless OUT-heavy/no-IN RED is retained; the fresh query plan checks index condition, buffers, tie behavior, expired IN, and no-IN behavior. |
| Shared CI admission guard | Direct negative-control coverage | YAML/lifecycle mutations, Docker inventory failures, collision refusal, config-only control, and cleanup behavior are exercised through the actual wrapper. |
| Initial port/consumer cutover | Partial historical fail-first provenance | The package records a dependency-guard RED and extensive final behavior evidence, but does not provide a separate pre-change failing assertion for every original contract behavior. The subsequent mutants substantially reduce retrofit risk; this is not the current release-blocking defect. |

### Bypass, fallback, and fixture ownership

The static audit records zero hard bypasses, support-route markers, auth shortcuts, no-exception-only assertions, DI overrides, and mock/fallback hints. Its status-only hints are paired with state, ownership, readback, or negative-effect assertions. The one aggregate fallback is a controlled migration-count aggregate, not business-data selection.

The controlled fixture owns its data, accepts only its private fixture token, restricts audit readback to seeded conversation identifiers, and uses a disposable `leadshug_timeline_*` database family. `send-mode`, `select-evolution`, and audit helpers live under test support, not the shipped application surface. They are legitimate provider controls, but are not substitutes for the outstanding real-provider operator proof.

### DI token, scope, and failure semantics

The E2E setup overrides the same `META_CLIENT`, `EVOLUTION_CLIENT`, and `TYPEBOT_CLIENT` tokens used by production composition; the registry still creates operation-scoped adapters around those token implementations. The independent opaque factory validates extension through the actual resolver and BFF. Raw Meta/Evolution HTTP tests separately exercise the real client classification code with controlled fetch responses. Failure tests distinguish BLOCKED, REJECTED, UNKNOWN, acknowledged-without-ID diagnostic persistence, accepted-local-incomplete, and changed context; they also assert provider-call absence where dispatch must be blocked.

### Real backend and provider boundary

The PostgreSQL E2E and browser lanes are real application/backend/database tests, not repository mocks. Provider protocol clients have raw HTTP unit coverage and browser/E2E use controlled provider doubles through the real DI boundary. That is sufficient for the narrow automated contract claim, but not for the declared real external-provider claim. The package correctly leaves post-activation official and unofficial IN/OUT as blocked rather than presenting fixture success as WhatsApp evidence.

## Performance

The performance evidence is credible for its bounded claim. The selected-window optimization executes zero latest-IN projection queries when the selected binding does not require a window. The 500-reference OUT-heavy/no-IN probe shows a direction-constrained backward `Index Only Scan` on `messages_conversation_direction_created_id_idx`, zero rows removed by filter, `500` loops, and `1003` shared-hit blocks. Equal-time ID ordering, expired IN retention, older IN behind an OUT suffix, and no-IN references are exercised.

The migration probe confirms SQLSTATE `55P03` and `57014`, no surviving aborted probe indexes, preserved rows, and explicitly distinguishes accelerated test timeouts from the approved five-second lock and sixty-second statement settings. The observed write/storage delta is correctly descriptive only. No production capacity, latency, provider throughput, or SLO claim is justified or made.

PCV evidence meets the local floors represented by the package: EPS strong query evidence; FRC five waves of twenty retriggers; BCI five batches of twenty distinct owned conversations with one OUT row each; and an RLS bounded stage. These do not prove same-key external exactly-once, crash recovery, saturation, or live-provider capacity.

## Security

The reviewed tests cover session and CSRF denial, public-key tenant denial, distinct-tenant credential/resource pairing, verified-ingress rejection, identity retirement, generation/epoch changes, raw malformed provider envelopes, redacted diagnostics, and no unauthorized provider side effect. No credential leak, tenant fallback, or ambient data selection is evidenced in the package. Remaining real-provider activation proof is operational evidence, not a reason to lower the existing isolation standard.

## Operational fit, commands, freshness, and platform status

The canonical successful command is `CHANNELS_DOCKER_TRANSPORT=linux bash scripts/test-channels-local.sh all`. It runs the shared lifecycle: source/mask checks, Prisma generate and migrate/status, lint, build, unit, PostgreSQL E2E, Web unit, Chromium install, browser E2E, and source/served-bundle freshness checks. The reported final run is source-stable, served/dist bundle-matched, and cleaned its disposable namespace to zero containers, networks, and volumes.

The common runner executes `python3 /workspace/scripts/check-channels-ci-parity.py --self-test` before product work. The retained CI Compose job independently runs `python3 scripts/check-channels-ci-parity.py --self-test` before Compose validation. The guard rejects twenty-one workflow/lifecycle mutations, YAML aliases and duplicate keys, failed inventory listings, namespace collisions, invalid WSL socket paths, and weakened cleanup/order controls.

Required platform status:

| Platform or gate | Status | Assessment |
| --- | --- | --- |
| Disposable Linux local CI-equivalent, PG16, Chromium | passed | Candidate-bound, fresh, source and bundle attested. |
| Windows default transport | not re-executed in this package | Preserved topology only; not needed to relabel the verified Linux run. |
| Remote GitHub CI execution | blocked/not_run | Workflow admission is configured, but remote execution is deliberately not claimed and belongs to later authorized promotion. |
| Local human DB migration, API/Web activation, HTTPS restoration | blocked/not_run | Explicit required operational gate. |
| Official and unofficial real provider IN/OUT | blocked/not_run | Required DOD-07 / VAL-04 evidence; fixtures do not substitute. |

## D01–D10 adherence

| Decision | Position |
| --- | --- |
| D01 | Adherent: narrow port, registry, opaque-recipient proof, and consumer dependency guard. |
| D02 | Adherent: authorized surfaces and verified ingress are covered by real-PG tenant and denial cases. |
| D03 | Adherent: immutable context and actual adapter pre-dispatch callback omission mutants are covered. |
| D04 | Adherent: raw Meta/Evolution classifications are conservative and one-call checked. |
| D05 | Adherent: uncertainty, diagnostic persistence, local-incomplete states, and no blind resend are asserted. |
| D06 | Adherent: common orchestration and sole keyed acceptance owner are exercised by sender/echo/claim cases. |
| D07 | Exception in evidence: source implements additive public list/thread availability, but tests do not cover unavailable public list semantics or either positive or negative public thread availability semantics. |
| D08 | Adherent: opaque fake verifies substitution without claiming a new provider. |
| D09 | Adherent: module composition and synthetic dependency-rule negatives prevent common-consumer provider dispatch. |
| D10 | Adherent for automated UI/runner/freshness behavior; real post-activation platform proof remains blocked. |

## Issue cards

### TQA-R02-01 — Public availability contract is incompletely specified by tests

- **Severity:** high
- **Evidence:** `api-app/src/surfaces/public/conversations.controller.ts:104` and `:128` add availability fields; `api-app/test/api-publica.e2e-spec.ts:140` asserts only the available public-list case.
- **Why now:** A regression could omit or misproject `envio_disponivel` or `motivo_indisponibilidade` on the public thread endpoint, or misreport unavailable selected bindings on the public list, while the supplied suite still passes. This is a changed external contract under D07 and a real-backend coverage gap.
- **Option A:** Add real-PostgreSQL public API tests for one deterministic unavailable selected binding and one available binding, asserting exact list and thread fields, POST blocking outcome, zero provider effects, and zero new OUT rows.
- **Option B:** Add only list and thread GET assertions, leaving mutation behavior to existing BFF/public send tests.
- **Option C:** Do nothing and rely on BFF/browser availability coverage.
- **Recommendation:** Option A. It is small, directly covers the public consumer contract, and verifies that observational GET availability and authoritative POST behavior do not diverge.

### TQA-R02-02 — Required real-provider/operator platform evidence remains absent

- **Severity:** high
- **Evidence:** governing TODO DOD-07 and VAL-04 remain pending; `v13-final-validation.json` expressly states human database activation, HTTPS restoration, and official/unofficial real IN/OUT are pending.
- **Why now:** Controlled provider doubles prove application behavior, not observed delivery through both owned external bindings. The TODO explicitly requires this before delivery and supplies no waiver.
- **Option A:** After authorized local activation, collect fresh redacted official and unofficial IN/OUT receipts plus canonical local readbacks for the activated source.
- **Option B:** Seek an explicit human waiver with mitigation and follow-up governance.
- **Option C:** Treat fixture/browser evidence as equivalent.
- **Recommendation:** Option A. Option C contradicts the approved contract; no waiver is present.

## Failure modes, uncertainty, and confidence

The remaining automation uncertainty is concentrated in public availability projection and unavailable-state semantics, not in the shared send path. External uncertainty remains the known local-check-to-network interval, null-ID deduplication limit, crash recovery limit, remote CI non-execution, and real-provider/operator gates. The package does not overstate these limitations.

Confidence is high that the local automated suite is real, fresh, and resistant to the principal prior regressions. Confidence is high that the public availability coverage gap exists from the supplied sources. Confidence is high that the real-provider gate is incomplete because the package explicitly labels it pending. Return for the two issue-card actions, then rerun the focused public API coverage and collect the authorized operational evidence before treating this audit as delivery-supporting closure.
- **Recommended path:** `return_for_targeted_public_contract_coverage_and_required_operational_gate_completion`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`
- **Findings:**
  - [high] TQA-R02-01 Public availability contract lacks negative-path and thread-endpoint regression coverage: The public controller adds `envio_disponivel` and `motivo_indisponibilidade` to both list and thread responses, but the supplied `api-publica.e2e-spec.ts` asserts only an available list row. A broken or omitted thread projection, or an unavailable selected binding reported as available, can pass all supplied tests despite violating D07 and the public contract.
  - [high] TQA-R02-02 Required real-provider official and unofficial IN/OUT gate remains unexecuted: The package correctly distinguishes controlled-provider, real-BFF/PostgreSQL evidence from external-provider proof, but DOD-07 and VAL-04 still require fresh post-activation official and unofficial operator IN/OUT. No waiver is supplied, so automated fixture success cannot close the delivery-integrity gap.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

