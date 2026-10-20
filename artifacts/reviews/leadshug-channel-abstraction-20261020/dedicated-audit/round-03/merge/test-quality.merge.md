# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/round-03/dispatch/test-quality.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `high`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `acceptable`

## Recommended Paths
- `changes_required_targeted_typebot_and_pagination_contract_regressions_then_rerun`

## Merged Findings
### F-C9555DF9 [high] No regression proves Typebot stops a multi-message response round after the first failed outbound send
- **Reviewers:** fresh-internal-no-context-tqa-round03
- **Category:** `tests`
- **Formalizable hint:** `partial`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Add a real PostgreSQL webhook/integration test with at least two Typebot text outputs. Force the first shared outbound operation to return UNKNOWN and assert one provider attempt, no second text dispatch, expected diagnostic or absence of authoritative OUT as applicable, and successful containment of the webhook round. Cover applicable BLOCKED and REJECTED variants or document their common-path equivalence with direct tests.
- **Rationale:** D05 explicitly requires Typebot to stop the round without replay on uncertain, blocked, or refused output. The implementation awaits each outbound send inside a loop and the enclosing execution is caught, but supplied Typebot tests exercise only one text output. They do not prove that a first failure prevents a later message in the same provider response, nor verify provider-call and persisted-effect bounds for that failure mode.

### F-A9DAEFCC [medium] Public pagination tests do not cover all normalizer input partitions
- **Reviewers:** fresh-internal-no-context-tqa-round03
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `n/a`
- **Suggested action:** Add table-driven request-level cases for omitted, blank, non-finite, zero, sub-one fractional, positive fractional, exact-cap, and over-cap limits on list and thread endpoints. Retain the call-through Prisma observation for the query bound and list look-ahead semantics.
- **Rationale:** The shared normalizer defines contract behavior for omitted, blank, non-finite, nonpositive, sub-one fractional, positive fractional, and over-cap values. The changed real HTTP/PG tests effectively protect the discovered negative-limit bypass and a normal positive value, but do not protect the rest of the newly centralized public-input contract.

## Reviewer Summaries
### fresh-internal-no-context-tqa-round03
- **Assessment:** # Test-quality audit — ST-CON-06 v1.3 round 03

## Scope and claim framing

This is a big, cross-stack NestJS/React/PostgreSQL/Docker audit. The package supports an **automated candidate** only: Linux CI-equivalent validation passed with 194 API-unit, 315 real-PostgreSQL E2E, 29 web-unit, and 50 Chromium tests. It does not claim remote CI execution, preserved-local-DB activation, HTTPS restoration, or physical official/unofficial operator IN/OUT. Those remain correctly held behind OrderedStep6 and DOD-07/VAL-04; their absence is not treated as an automated-candidate failure.

The source freeze is credible for the test/build inputs: 60 explicit product/context paths match the pre-run snapshot; the one differing TODO record is separately evidenced as non-executable progress metadata. The browser bundle, dist bundle, and preserved served copy match. This is not represented here as a 61/61 source match.

## Architecture and code quality

The candidate has a simple, faithful boundary: common senders depend on `Channel`/`ChannelResolver` and `OutboundService`; adapter factories bind operation-scoped credentials; `MessageAcceptanceService` remains the keyed persistence owner. The dependency-boundary test includes synthetic forbidden-import and direct-dispatch cases, while the opaque-recipient fake goes through real resolver, BFF, and PostgreSQL wiring. That is effective evidence against a pass-the-test abstraction that merely renames provider branches.

The v13r3 public pagination repair is proportionate. `limitePublico` is a small shared normalizer, rather than separate controller patches, and preserves list look-ahead semantics. The parity guard likewise remains bounded: it checks the shared runner and selected bypass mutations rather than claiming formal verification of arbitrary shell programs.

## Tests: alignment, effectiveness, efficiency, and shortcuts

1. **Real contract change versus pass-the-test repair:** the negative-limit repair maps to a demonstrated request-level defect: pre-fix real HTTP/PostgreSQL runs observed list `take=-999999` and thread `take=-1000000`. The replacement test drives actual authenticated public endpoints and a real Prisma delegate. The public availability repair also tests real HTTP, PostgreSQL state, selected-origin behavior, blocked POST, provider counters, and absence of new OUT rows.
2. **Pass-the-test shortcut risk:** no material shortcut is evidenced in the changed pagination tests. Their `mockImplementation` observers call the original bound Prisma method and restore in `finally`; they observe query bounds rather than fabricate database results. The static audit reports no hard bypass, test-only support route, auth shortcut, DI override, or no-exception-only pattern in its bounded scan. It remains a heuristic rather than proof beyond its listed paths.
3. **Assertion effectiveness:** outcome/client tests assert semantic outcomes, external IDs, malformed envelopes, provider-call counts, persistence effects, tenant ownership, and real HTTP status/body behavior. Browser tests use a fresh real BFF/PG stack and prove the stale-draft fence with a native-body/task barrier plus an actual guard-removal mutant. The CI guard has both mutation controls for swallowed commands and an executable fake-Docker proof that a mandatory leaf failure exits 42 and still performs cleanup.
4. **Assertion efficiency:** the broad `all` runner is the sole full lifecycle owner; narrow direct tests are used for classifier, database-plan, wrapper, and mutation evidence. The pagination spy is narrowly scoped, call-through, and restored. No redundant alternate runner is introduced.
5. **Coverage sufficiency:** coverage is strong for BFF/public/adapter/PG/browser paths, but it is incomplete for the explicit D05 Typebot stop-the-round behavior when a multi-text bot response encounters a failed first outbound send. This is a material backend-mutation coverage gap and blocks acceptance of the automated candidate.

## Fail-first and retrofit assessment

| Critical locus | Classification | Evidence assessment |
| --- | --- | --- |
| Dependency boundary / abstract transport | test-first | The package records the original dependency-guard RED and synthetic violation checks. |
| Meta contradictory-success classification | test-first | R05 has a recorded pre-fix failing case and final raw-client plus real-path coverage. |
| Adapter pre-dispatch fence | test-after with causal proof | Shipping Meta/Evolution callback omission mutants fail with 409-versus-201 behavior and are restored exactly. |
| Browser stale completion / same-text draft | test-after with causal proof | The native `response.text()` barrier and guard-omission mutant demonstrate that removal empties the new draft. |
| Latest-IN index and selected-window work | test-first | Index-less RED, actual indexed plan evidence, and selected non-window query-count evidence are preserved. |
| Public negative pagination | test-first | Two separated real endpoint failures precede the normalizer; final tests prove positive and negative request paths. |
| CI shell failure parity | post-fix causal control | The in-memory omission control is honestly post-fix, but the actual wrapper control proves propagation and cleanup. |
| Typebot multi-output failure stop | missing | Existing Typebot coverage exercises one output at a time; it does not prove that a failed first output prevents later outputs in the same returned batch. |

The remaining retrofit risk is therefore localized to the Typebot failure path. The new public availability assertions are test-after coverage hardening of an already-present behavior, not evidence of a source-only replacement; their real HTTP/PG assertions substantially reduce that risk.

## Real-boundary, DI, fallback, and failure-parity assessment

Real PostgreSQL is used for the authorization, scoped ownership, public availability, acceptance, echo, pagination, index, and browser-backed flows. Browser tests use a controlled provider boundary but a real built API, BFF, PostgreSQL database, and served web bundle. Unit client tests appropriately fake `fetch` to classify provider envelopes; they do not claim a live-provider result.

Provider DI replacements preserve the production tokens in the integration harness. The opaque fake is explicitly a port-substitution test, not a claim that a future network works. There is no claimed fallback from required provider behavior to ambient data or a test-only product route. The real-provider physical boundary remains pending DOD-07, correctly not substituted by fixtures.

Failure parity is credible for the runner: `set -eu`, standalone parity guard/E2E commands, synthetic `|| true` mutations, failed inventories, collision refusal, and the fake mandatory-guard exit-42 cleanup path are all covered. This is bounded executable protection, not a universal shell-proof claim.

## Performance and PCV

Performance evidence is adequate for the automated candidate. The selected-window projection uses the managed `(conversation_id, direction, created_at, id)` index. The 500-reference OUT-heavy/no-IN evidence reports direction-constrained index probes, zero rows removed by filter, 500 loops, 1,003 shared-hit blocks, and 2.343 ms in the disposable observation. The selected non-window path records zero latest-IN queries. The public list uses bounded pagination and one batched binding query, one credential-metadata query, and one latest-IN projection for the observed 30-row page.

The index cost is not overstated: the package records a bounded sample of 6,856,704 index bytes and writes of roughly 15.9 ms with the index versus 6.5 ms without it, explicitly without an SLO/capacity claim. Disposable rollback probes distinguish the configured 5 s lock / 60 s statement settings from accelerated test limits and observe SQLSTATE `55P03` and `57014` with no surviving aborted indexes.

The PCV candidate artifacts contain the applicable floors: EPS-E2 real query evidence; FRC high profile with five waves of 20 retriggers and one request per wave; BCI high profile with five batches of 20 distinct owned conversations and per-conversation row assertions; and RLS-E1 bounded stage/metrics evidence. Their TODO lane states properly remain pending until independent disposition; this audit does not convert them to passed.

## Security and operational fit

The tests cover session/CSRF denial, foreign API-key account denial, tenant-separated in-flight credentials, verified ingress pinning, changed identity/generation/epoch fences, and no-provider/no-OUT behavior on blocked public sends. The source avoids exposing credential material through the common transport contract. No security regression is established from the changed test delta.

The owning command is `CHANNELS_DOCKER_TRANSPORT=linux bash scripts/test-channels-local.sh all`. It owns prerequisite installation, parity self-test, Prisma generation/migration/status, lint, API unit/E2E, web build/unit, Playwright, freshness checks, and namespace cleanup. Linux same-engine execution passed. Remote CI is `not_run`; no fresh broad Windows execution or physical provider run is claimed. Operator IN/OUT is still a required later gate, not a waived condition.

## Decision adherence

| Decision | Assessment |
| --- | --- |
| D01 | Adherent: abstract port, registry, opaque fake, and dependency guard evidence exist. |
| D02 | Adherent: real-PG scope/auth/tenant and ingress tests cover the changed boundary. |
| D03 | Adherent: generation, epoch, credential-version, and shipping-adapter fence probes are present. |
| D04 | Adherent: conservative Meta/Evolution classification and one-dispatch outcome assertions are present. |
| D05 | Exception — test evidence is incomplete for stopping a multi-message Typebot batch after the first failed output; see TQA-R03-01. |
| D06 | Adherent: one acceptance owner and public/BFF/echo/claim regressions are evidenced. |
| D07 | Adherent in the candidate: selected-origin availability, no fallback, pagination bound, and indexed latest-IN evidence are present; broaden input-partition coverage per TQA-R03-02. |
| D08 | Adherent: opaque fake demonstrates internal substitutability without claiming a real future provider. |
| D09 | Adherent: common composition and executable dependency/CI guard checks are present. |
| D10 | Adherent for the automated candidate: draft fence, fresh served bundle, CI lifecycle guard, and cleanup controls are evidenced. |

## Issue cards

### TQA-R03-01 — high — missing Typebot multi-output stop regression

**Evidence:** `api-app/src/domain/inbox/incoming.service.ts` iterates `resposta.messages` and catches the enclosing Typebot execution failure; `api-app/test/number-onboarding-typebot.e2e-spec.ts` exercises single-output replies only. D05 requires that Typebot stop the round without replay after uncertain, blocked, or refused output.

- Option A: add a real-PG/webhook regression whose Typebot response has at least two text messages, force the first shared outbound result to fail, and assert exactly one provider attempt, no second output, correct persisted state, and stable webhook response. Cover UNKNOWN at minimum and the applicable BLOCKED/REJECTED paths.
- Option B: add only a mocked `IncomingService` unit test. This is faster but insufficient alone for the persistence/provider-count contract.
- Option C: do nothing. This leaves an explicit D05 failure mode without executable regression protection.

Recommendation: Option A.

### TQA-R03-02 — medium — pagination normalizer lacks full request-partition coverage

**Evidence:** `api-app/src/surfaces/public/conversations.controller.ts` defines behavior for blank, non-finite, nonpositive, sub-one fractional, finite fractional, and over-cap limits. `api-app/test/api-publica.e2e-spec.ts` currently proves one positive integer and one large negative value per endpoint.

- Option A: add table-driven real HTTP/PG cases for omitted, blank, non-finite, zero, fractional below one, positive fractional, exact cap, and over-cap inputs; assert the bounded delegate take and retained list look-ahead semantics.
- Option B: assert only HTTP success for those inputs. This is weaker because it can miss an oversized query.
- Option C: do nothing. The current negative-limit regression remains protected, but the complete public normalization contract is not.

Recommendation: Option A.

## Residual risk, uncertainty, and confidence

No package evidence establishes continuous provider availability, remote workflow execution, production capacity, exactly-once external delivery, or real operator IN/OUT after activation; the TODO accurately leaves these unclaimed and gated. Confidence is high in the automated runner, real-PG, adapter, and browser evidence; medium-high in the test-quality conclusion because the review is package-based and the Typebot multi-output failure scenario is absent. The candidate should return for the two targeted regressions, then rerun the affected real-PG suite and canonical `all` before fresh final disposition.
- **Recommended path:** `changes_required_targeted_typebot_and_pagination_contract_regressions_then_rerun`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `acceptable`
- **Findings:**
  - [high] TQA-R03-01 No regression proves Typebot stops a multi-message response round after the first failed outbound send: D05 explicitly requires Typebot to stop the round without replay on uncertain, blocked, or refused output. The implementation awaits each outbound send inside a loop and the enclosing execution is caught, but supplied Typebot tests exercise only one text output. They do not prove that a first failure prevents a later message in the same provider response, nor verify provider-call and persisted-effect bounds for that failure mode.
  - [medium] TQA-R03-02 Public pagination tests do not cover all normalizer input partitions: The shared normalizer defines contract behavior for omitted, blank, non-finite, nonpositive, sub-one fractional, positive fractional, and over-cap values. The changed real HTTP/PG tests effectively protect the discovered negative-limit bypass and a normal positive value, but do not protect the rest of the newly centralized public-input contract.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

