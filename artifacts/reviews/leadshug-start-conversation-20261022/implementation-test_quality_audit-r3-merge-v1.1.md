# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-start-conversation-20261022/evidence/implementation-test_quality_audit-r3-dispatch-v1.1.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`

## Recommended Paths
- `return_for_targeted_test_quality_remediation_and_evidence_completion`

## Merged Findings
### F-D7518029 [medium] The main approved-template E2E test is an overlarge sequential scenario with coupled failure reachability
- **Reviewers:** fresh-no-context-tqa-r3
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `none`
- **Candidate rule id:** `n/a`
- **Suggested action:** A) Split this scenario into independently seeded E2E cases grouped by template eligibility, claim/preflight fencing, owner race, protocol payload, and negative no-POST behavior; recommended. B) Retain common helpers but make each behavior an independently runnable test with local setup and explicit counter baseline. C) Keep the monolith unchanged and accept reduced failure localization and reachability; not recommended. Rerun the affected suites and canonical all after restructuring.
- **Rationale:** Evidence: api-app/test/initial-message.e2e-spec.ts contains one long test beginning “previews and sends approved NAMED and POSITIONAL templates...” that shares mutable fake-provider modes, latches, catalog state, grant revocation, deadline manipulation, owner races, positive wire assertions, and seven negative cases. An early failure prevents later contract assertions from being reached, which the chronology already demonstrates can obscure what was actually proved. Current green status does not remove this diagnostic and maintenance risk.

### F-EB21E40D [medium] Remaining high-heuristic static TQA signals are not individually dispositioned
- **Reviewers:** fresh-no-context-tqa-r3
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `paced`
- **Candidate rule id:** `tqa-static-signal-disposition-required`
- **Suggested action:** A) Attach a bounded machine-readable inventory for every remaining signal with path, line, classification, and rationale, then rerun this independent TQA review; recommended. B) Narrow the scan only with an approved, semantics-preserving rule that still reports every excluded signal and reason. C) Leave aggregate high signals unresolved; this is not acceptable for TQA gate completion.
- **Rationale:** Evidence: test-quality-public-roots-e54-v1.1.json reports exit 2 with 196 status-only, 4 no-exception-only, 16 ambient-subject, and 29 mock hints. It convincingly explains the five hard-bypass matches as Prisma pagination arguments, but the package provides neither locations nor adjacent-assertion dispositions for the remaining signals. The audit rubric requires those patterns to be assessed, especially for a high-risk cross-stack delivery claim.

## Reviewer Summaries
### fresh-no-context-tqa-r3
- **Assessment:** Assessment: mixed; the candidate has unusually substantive functional test evidence, but this TQA gate should return for targeted evidence completion and test-structure remediation. Product/test delta alignment is generally strong: manual open, trusted-window provenance, union transport behavior, initial-intent durability, ordinary/initial interlock, local-only recovery, Unicode limits, and browser recovery are exercised through assertions on persisted rows, safe API responses, provider-effect counters, and served UI state. The E50, E51, and E44 records are credible causal regressions for their stated defects. The documented E03/E15/E25 module-load failures, E04 post-hoc reversion, and later alongside/post-implementation tests must remain classified as partial or retrofit evidence rather than universal test-first proof.

Pass-the-test risk is constrained but not absent. The E23 timestamp fixture adjustments are narrowly explained as synthetic signed/current-resource alignment; E48/E49 are correctly identified as test-support failures rather than product REDs; and E50/E51 product repairs have pre-fix assertions. The owned provider fake is explicit, bounded, and paired with real PostgreSQL, Nest BFF, session/CSRF, and a freshly served React bundle. No embedded evidence shows a production test-only route, skip, focused test, silent live-service fallback, or ambient live-data selection. The production DI graph is retained while META_CLIENT, EVOLUTION_CLIENT, and TYPEBOT_CLIENT are overridden by their normal tokens; browser proof uses compiled AppModule with the same boundary tokens. This is appropriate boundary substitution, not claimed real-provider parity.

Assertion efficacy is high for the supplied critical paths: tests check one-POST/one-Message effects, exact replay keys and bodies, owner/slot CAS outcomes, rollback versus commit-ACK-loss readback, safe error metadata, zero-network recovery, signed timestamp provenance, account pinning, wire recipient formatting, explicit unsupported Evolution behavior, and browser-visible recovery. Assertion efficiency is mixed. Query-plan and bounded-counter tests are targeted, and the 5x20 concurrency exercises are justified by the irreversible-side-effect risk. However, the enormous approved-template E2E scenario combines many unrelated behaviors behind one setup chain, so an early failure can make numerous later assertions unexecuted and diagnosis unnecessarily expensive.

Audit framing: complexity is big. Architecture evidence supports one transport operation, narrow DI substitution, and the sole MessageAcceptance owner. Code-quality evidence is generally faithful to the approved finite state model. Tests cover unit, protocol, real-PG/BFF, and browser layers. Performance evidence supports bounded query shape, indexed window access, bounded provider calls, and a declared non-SLO load check. Security evidence covers BFF authorization, current-grant fences, context binding, tenant boundaries, and safe error projection. Capability inventory is consistent with NestJS/Prisma/Vitest in api-app and React/Vite/Playwright in web-app; the declared owning command, bash scripts/test-channels-local.sh all, completed with API 364, PG 439, Web 54, and browser 88 passing.

The static public-root TQA scan remains unresolved as audit evidence: exit 2 correctly identifies five Prisma pagination false positives rather than test skips, and the supplemental skip/focus check found none. But the package supplies only aggregate counts for the remaining 196 status-only, 4 no-exception-only, 16 ambient-subject, and 29 mock hints. Without their locations and dispositions, this review cannot independently determine whether all are benign adjacent assertions. That blocks a complete claim that no weak assertions or fallback patterns remain across the stated public-root surface.

Platform status: API unit passed; disposable PostgreSQL/BFF/session/CSRF integration passed; Web unit passed; served React/Playwright freshness passed; fake-provider protocol boundary passed; local canonical CI-equivalent passed. Remote CI execution is not evidenced. Docker/Alpine image execution, preserved-local migration/runtime proof, actual approved-template/provider proof, operator replies, module consolidation, full diff guard, final delivery review, and DOD-11 through DOD-13 are blocked rather than passed; none is treated as a product-test success.

Decision adherence on the embedded evidence is Adherent for D-01 manual open, D-02 abstract union/context fence, D-03 common outbound and Message owner, D-04 qualified selected-resource window, D-05 shared catalog plus fresh same-account template check, D-06 durable intent and local recovery, D-07 ordinary/initial interlock, D-08 bounded renderer and escaped preview, D-09 bounded requests/rates, and D-10 commit-certainty/readback behavior. This is candidate-level adherence only. Remaining uncertainty includes fake-provider versus real-provider behavior, synthetic deadline manipulation for selected flows, unexecuted preserved-runtime proof, inherited SEC-R6-04/OPS-R4-01/TQA-ST05-03 debt, and the unresolved static-scan signal inventory. Confidence is moderate for local candidate behavior and insufficient for a completed independent TQA gate.
- **Recommended path:** `return_for_targeted_test_quality_remediation_and_evidence_completion`
- **Performance:** `acceptable`
- **Elegance:** `mixed`
- **Structural soundness:** `mixed`
- **Operational fit:** `mixed`
- **Findings:**
  - [medium] TQA-R3-01 Remaining high-heuristic static TQA signals are not individually dispositioned: Evidence: test-quality-public-roots-e54-v1.1.json reports exit 2 with 196 status-only, 4 no-exception-only, 16 ambient-subject, and 29 mock hints. It convincingly explains the five hard-bypass matches as Prisma pagination arguments, but the package provides neither locations nor adjacent-assertion dispositions for the remaining signals. The audit rubric requires those patterns to be assessed, especially for a high-risk cross-stack delivery claim.
  - [medium] TQA-R3-02 The main approved-template E2E test is an overlarge sequential scenario with coupled failure reachability: Evidence: api-app/test/initial-message.e2e-spec.ts contains one long test beginning “previews and sends approved NAMED and POSITIONAL templates...” that shares mutable fake-provider modes, latches, catalog state, grant revocation, deadline manipulation, owner races, positive wire assertions, and seven negative cases. An early failure prevents later contract assertions from being reached, which the chronology already demonstrates can obscure what was actually proved. Current green status does not remove this diagnostic and maintenance risk.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

