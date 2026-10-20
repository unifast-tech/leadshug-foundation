# ST-CON-06 — bounded CI-admission contradiction challenge

Derived planning/adjudication opinion only, not TQA gate satisfaction or implementation authorization. Actual three-lane round1 returned PerformancePERF01high history scan (integrated blocker, being reproduced), PERFlow aggregate-claim gap (being corrected), cleanCutover and TQA01high missingremotePG/browserjobs. TQAassessment claims good tests but does not report the entire mandatory skill workload; a complete independentTQA remains required after remediation. No live review is recycled; all three sessions terminal, strictrecord/merge completed.

Question: does the approved local-only milestone mandate adding remoteCI PG/browserjob(s) now under these exact CIgovernance/testsurfaceadmission rules, or is that a separate promotion obligation outside this TODO? Preserve the actual rules and approvedcontract; do not settle by owner preference or assume that either a reviewer or scope exclusion silently waives a mandatory requirement. Determine whether TQA01isblockinghere, legitimatefollowup needingexplicitowner, or bydesign; distinguish CIconfiguration, locally exercised parity, actualremoteexecution and merge/promotion claims. Suggest the smallest compliant path, including explicitnarrow approval expansion if required, without authorizing codepush/deploy/gitlink edits. No test/resource secrets or production operations.

Evidence: canonicallocalall80903passed194/309/29/50 with exactsource/served attestation; remoteCIcurrentlyonlyunit/build, not falselyclaimedotherwise. Physicaloperator/activation/finalreviewpending. Userapprovedv1.2 no schema/CIpaths; explicitcompanionvalidationonly2testpaths. No remote sourcecommit/push/deploy authorized in current execution. Canonical testallrunner requiresWindowsDocker+wslpath, so directUbuntu invocation is not presently valid; equivalentpipelineleafcommands would require concreteisolatedNode22/PG16/productionbundleChromium topology and provenance, not YAML-only pretendexecution.


## Exact authority / source delphi-ai/skills/ci-equivalent-governance/SKILL.md

---
name: ci-equivalent-governance
description: "Canonical definition of CI Equivalent and broad local stage-parity gates such as `stage-full`. Load whenever a workflow, skill, or operator is designing, invoking, reviewing, or claiming CI-equivalent evidence."
---

# CI Equivalent Governance

Use this skill whenever a workflow, skill, TODO, execution plan, or promotion lane says `CI Equivalent`, claims `stage-full`-style parity, or needs to decide whether local evidence is truly pipeline-equivalent instead of merely diagnostic.

## Purpose
Freeze the meaning of `CI Equivalent` as current-branch local product proof on the authoritative branch under evaluation. This skill owns the shared taxonomy so promotion, test orchestration, TODO delivery, pipeline updates, and reconciliation do not redefine it differently.

## Canonical Model
- `CI Equivalent` is local proof, not published-lane proof.
- It runs on the current authoritative branch under evaluation (`feature/*`, `review/*`, `sequence/*`, `reconcile/*`, version/package branch such as `v0.2.0+8-rc`, or equivalent).
- It uses the project-owned local build/publish/runtime path and the same product-facing suites/jobs the pipeline uses for that scope on that branch.
- It is scope-complete for the touched repo/job family. A targeted rerun, representative smoke path, or single happy path is diagnostic evidence unless the approved matrix explicitly says that narrower scope is complete.
- Published `stage` or `main` probes are separate evidence. They never replace `CI Equivalent`.
- `CI Equivalent` is a generic proof concept. Reconciliation is only one possible execution topology.
- If the required local runtime surface for a broad gate is unavailable, hung, or ambiguous, the `CI Equivalent` claim is `blocked`, not `passed`, and published-lane evidence still does not replace it.

## Authoritative Branch And Wrapper Discipline
- The branch under test is the current authoritative branch for the claim being made.
- For package/version promotion lanes, the authoritative source branch is the exact branch recorded in the governing TODO `Current Branch Authority`, typically the version `*-rc` branch. Example: `v0.2.0+8-rc`.
- In those package/version lanes, the first promotion-grade `CI Equivalent` run must pass on that authoritative `*-rc` branch before any derived `review/*` remediation branch is opened.
- Reconcile-only wrappers are valid only on real `reconcile/*` states or an explicitly recorded same-commit reconcile alias.
- In real orchestration, the consolidated `reconcile/*` branch is authoritative until green; after that, replay the accepted net effect onto the recorded canonical return branch before promotion or non-orchestration closeout resumes.
- In TODO sequencing, a `sequence/*` branch may be authoritative for the one integrated package-closeout broad local gate only when that branch is the current principal-checkout authoritative branch under evaluation and owns the real local runtime/browser surface. Individual TODO checkpoints use their recorded affected-area bundles and must not invoke or claim the broad gate by default. The sequencing branch is checkpoint-only topology and is never itself a promotable source branch.
- If `sequence/*` exists only inside an isolated linked worktree while the principal checkout is reserved for another lane, treat it as non-authoritative implementation topology only: it may run an explicitly narrower checkpoint prefix gate, but it must not run or claim the parity-complete broad local gate until the accepted net effect is replayed onto the principal authoritative branch.
- Review/remediation branches may run `CI Equivalent` for their own validation loop, but they are evidence branches rather than promotable source authority.
- A `review/*` pass never substitutes for the missing authoritative `*-rc` pass. It is an additional gate.
- After replay from `review/*` back onto the authoritative `*-rc` branch, rerun `CI Equivalent` there whenever the replay was not a pure fast-forward or otherwise introduced branch-local change.

## Broad Local Stage Gate Rule
When a repo exposes a named broad local stage gate such as `stage-full`, that name is reserved for the parity-complete local mirror of the stage pipeline for the touched scope on that branch.

That parity must include both:
- the complete repo-owned suite/job family that the stage pipeline executes for that scope; and
- any pipeline-owned lifecycle work outside the inner smoke commands, such as build/publish/provenance, fixture/bootstrap seed, host-override management, cleanup/teardown, restore/readback preparation, or equivalent pre/post steps.

A local bundle is not valid `stage-full` parity when any of these are true:
- it omits an in-scope stage suite/job that the pipeline still runs for that scope;
- it runs only inner smoke commands while the pipeline owns required outer lifecycle steps;
- it passes only because prior state already had healthy fixtures, seed data, runtime overrides, or published artifacts;
- it silently changes branch/topology semantics just to satisfy a reconcile-only wrapper.

Narrower diagnostic bundles must use distinct names and must not be reported as the broad stage gate.

If an isolated sequencing worktree uses a prefix derived from `stage-full`, that prefix must stop before `browser-stage-full`. That cutoff means the isolated state never enters `local-public-web-build`, readonly smoke, or mutation smoke, and it must not claim any of those surfaces. Any request to cross that cutoff from the isolated worktree is out of contract and must be refused until replay onto the principal authoritative branch.

When a broad local gate such as `stage-full` cannot complete because the local runtime surface is unhealthy or non-responsive:
- treat the gate as a blocking local infrastructure failure, not as a soft warning;
- do not continue promotion, replay, or closeout on the theory that remote `stage` or `main` evidence is "good enough";
- do not reinterpret targeted local checks as a substitute for the missing broad gate;
- only explicit human waiver may authorize progression without that gate;
- emit a PACED/TEACH stop response that names the blocked gate, the failing runtime surface, why evolution is disallowed, and the next local recovery action.

## Mutation And Production Semantics
- Mutation validation belongs only on an approved non-`main` lane.
- If the touched behavior includes mutation, `CI Equivalent` must include corresponding local mutation evidence on that non-production lane.
- Production/main semantics may intentionally forbid mutation. Prove that separately with a production-lane proof surface such as `main-proof`; do not weaken non-main `CI Equivalent` to avoid running mutation locally.

## Required Evidence Hygiene
Before claiming `CI Equivalent`, record:
- authoritative branch under evaluation;
- governing TODO branch authority when package/version promotion is in scope, including the exact `*-rc` branch name and validated `branch@sha` when applicable;
- exact local commands or contract profiles run;
- runtime freshness attestation for every manual/browser/device proof surface: authoritative `branch@sha`, local build/publish artifact or fingerprint, served target URL/device/tunnel, and the comparison/probe proving the served target matched that build before the test result was interpreted;
- touched repo/job family covered;
- runtime topology, publish path, domains, tenants, and credentials lane when relevant;
- whether readonly and mutation behaviors were both required;
- whether pipeline-owned lifecycle steps were executed locally as part of the same contract;
- evidence artifacts proving the current build/branch state was the one actually served.

Browser/device evidence is invalid if it cannot prove the current build, bundle, or runtime state was what the runner exercised. Freshness must be proven before the test result is trusted, not reconstructed afterward from assumption.

## Promotable Documentation Preflight
For a promotable broad gate, validate required delivery documentation before starting the expensive execution contract. This is a precondition of execution, not a second kind of post-execution CI-equivalent proof.

- The preflight must fail closed when a TODO or delivery record that should already describe completed implementation/evidence remains `Pending`, `Open`, or otherwise stale.
- The preflight must allow the one explicitly declared pending item that the current broad gate itself will produce (for example, the pending `promotable-stage-full` evidence row). It must not require future execution evidence before the execution that creates it.
- Correcting a scope-neutral documentation drift found by this preflight happens before `stage-full`; after the correction, run the preflight again and then run `stage-full` once on the final documented state.
- Do not make a completed `stage-full` rerun merely because a later promotion guard exposed a scope-neutral documentation omission that the preflight should have caught. Harden the preflight and correct the documentation instead.
- If the documentation correction changes declared scope, behavior, acceptance criteria, runtime contract, or another execution-relevant claim, it is no longer documentation-only: reassess the execution evidence and rerun the broad gate when the project-owned invalidation policy requires it.

## Evidence Reuse And Invalidation
- Exact `branch@sha` remains the traceability anchor for CI-equivalent and promotion claims. Do not stop recording it.
- SHA drift alone is not the canonical rerun trigger once a passed CI-equivalent artifact already exists.
- Reuse is allowed only when a deterministic, project-owned invalidation/reuse guard proves the current authoritative branch differs from that passed baseline only on explicitly safe-reuse surfaces.
- Rerun is required when the guard reports any invalidating drift in product code, test ownership, wrappers, lifecycle steps, build/publish/provenance paths, runtime/bootstrap/config, or other stage-facing surfaces.
- Manual admission/authority refresh is required when the current branch is dirty, diverged from the baseline topology, or the baseline artifact/TODO/policy no longer line up deterministically.
- Backward-compatibility note: if an older report artifact lacks recorded repo head metadata, the guard may fall back to the governing TODO `branch@sha` entries, but that is weaker than artifact-native repo-state evidence and should be phased out.

## Relationship To Other Skills
- `ci-equivalent-test-surface-admission` decides how new or changed tests, wrappers, lifecycle steps, and suite rows enter the canonical stage-facing surface without local/pipeline drift.
- `ci_equivalent_evidence_invalidation_guard.py` decides whether a previously passed CI-equivalent artifact is still reusable on the current heads or whether the broad gate must rerun.
- `test-orchestration-suite` decides the concrete suite matrix and execution order.
- `wf-docker-todo-delivery-gates-method` uses this skill when deciding whether TODO evidence really counts as `CI Equivalent`.
- `github-stage-promotion-orchestrator` and `github-main-promotion-orchestrator` use this skill before any promotion-ready claim.
- `wf-docker-update-ci-pipeline-method` uses this skill whenever a pipeline edit changes stage-facing suite/job ownership or lifecycle steps.
- `wf-docker-subagent-worktree-reconciliation-method` uses this skill to keep reconcile topology from hijacking the generic definition.

## Required Operator Actions
1. Load this skill before designing, invoking, or claiming a `CI Equivalent` surface.
2. If a named broad stage gate already exists, compare it against the actual stage pipeline job family for the touched scope.
3. If the local gate is narrower, rename it or expand it; do not keep a misleading broad name.
4. If suite membership, wrapper ownership, lifecycle steps, or readonly/mutation rows changed, load `ci-equivalent-test-surface-admission` and complete that admission before claiming parity.
5. Record any deliberate same-commit reconcile alias or waiver explicitly.
6. Treat published-lane checks as additional evidence only.
7. When the current sequencing lane is an isolated worktree and the broad local gate is `stage-full`, record the exact pre-browser prefix that runs now, explicitly note that the skipped boundary starts at `local-public-web-build`, and record the deferred principal-authoritative broad gate that still remains mandatory after replay.
8. Before any manual/browser/device validation lane, produce or refresh the runtime freshness attestation and stop immediately if the served target cannot be proven fresh for the current authoritative build.
9. For a promotable broad gate, run the documentation preflight before the execution contract. It must reject stale prerequisite delivery documentation while allowing only the explicitly designated future-evidence row for this exact gate.
10. Before rerunning or reusing an already-passed broad local gate such as `stage-full`, run the project-owned evidence invalidation/reuse guard and record whether the outcome was `reusable`, `rerun-required`, or `manual-admission-required`.
11. If the required broad local gate is unavailable, hung, or fails for local runtime-health reasons, stop the lane and report it as a blocked local infrastructure surface. Do not convert to remote-lane progression or completion claims without an explicit human waiver.

## Done Criteria
- The in-scope local matrix is current-branch local proof, not proxy evidence.
- Any `stage-full`-style gate is parity-complete for the touched scope.
- Required lifecycle/precondition steps are executed by the same local contract rather than assumed from prior state.
- Delivery or promotion claims do not rest on published-lane proof or targeted reruns alone.
- Missing or non-responsive runtime surfaces block the claim rather than silently downgrading the local proof requirement.


## Exact authority / source delphi-ai/skills/ci-equivalent-test-surface-admission/SKILL.md

---
name: ci-equivalent-test-surface-admission
description: "Canonical admission workflow for adding or changing tests, wrappers, lifecycle steps, or suite rows that affect CI Equivalent or broad local stage gates such as `stage-full`."
---

# CI Equivalent Test-Surface Admission

Use this skill whenever a change adds, removes, rehomes, renames, or materially rewires any test, wrapper, fixture/bootstrap step, lifecycle step, or suite row that contributes to `CI Equivalent` or a broad local stage gate such as `stage-full`.

## Purpose
Prevent local-only, pipeline-only, or order-divergent test additions from drifting the broad stage-parity contract over time.

## Load First
- Load `ci-equivalent-governance` before deciding whether the touched surface is part of `CI Equivalent` or a broad stage gate.

## Required Decisions
1. Classify the owning surface:
   - repo-owned Flutter workspace tests
   - browser/navigation readonly
   - browser/navigation mutation
   - runtime/build/preflight lifecycle
   - other explicit stage-facing suite family
2. Decide whether the change affects:
   - suite membership
   - execution order
   - wrapper/leaf-command ownership
   - bootstrap/fixture/cleanup lifecycle
   - readonly vs mutation coverage
3. Record whether the touched branch is the authoritative branch for the claim being made.

## Admission Rules
- Do not add the test only to a local wrapper while leaving the pipeline on different leaf commands.
- Do not add the test only to the pipeline while leaving the broad local stage gate narrower.
- Keep local parity contracts and stage workflow ownership aligned through the same canonical wrapper or leaf command family.
- Preserve explicit ordering when the pipeline depends on ordered lifecycle work.
- If mutation coverage is required, keep it on the approved non-`main` lane. Do not move mutation validation onto production/main proof surfaces.
- If the change is narrower than the broad stage gate, give it a narrower name instead of silently expanding or shrinking `stage-full`.

## Required Operator Actions
1. Update the owning suite/wrapper/contract surface.
2. Update the corresponding pipeline-owned stage surface in the same change when the stage-facing family changed.
3. Update fail-closed drift guards or audits that prove the two surfaces stay aligned.
4. Rerun the broad local CI-equivalent contract on the authoritative branch when the admission affects that branch's claim.
5. Record the exact commands/contracts used as evidence.

## Relationship To Other Skills
- `test-creation-standard` defines what coverage should exist.
- This skill decides how new coverage enters the canonical CI/pipeline surface without drift.
- `test-orchestration-suite` executes the resulting matrix.
- `wf-docker-update-ci-pipeline-method` uses this skill when CI workflow changes affect stage-facing test ownership.
- Promotion skills use this skill when remediation changes stage-facing test/harness surfaces before claiming the lane is ready.

## Done Criteria
- The new or changed test surface has one clear owner.
- Local broad-stage parity and stage pipeline use the same suite family and ordered lifecycle steps for that surface.
- Readonly/mutation semantics remain explicit and lane-correct.
- Drift guards/audits were updated when the expected stage-facing shape changed.
- The authoritative local CI-equivalent rerun is green before readiness or promotion is claimed.


## Exact authority / source delphi-ai/skills/test-quality-audit/SKILL.md

---
name: test-quality-audit
description: "Audit stack-aware test quality and test-first alignment so bypasses, weak assertions, false parity, and retrofit risk are blocked."
---

# Test Quality Audit

## Purpose

Detect bypasses, weak assertions, false environment parity, and retrofit risk across project-declared stacks. Judge evidence against the behavior and boundary claimed, without imposing an unrelated framework, runner, database, transport, browser, or device.

## Scope Controls

- This skill never bypasses TODO governance. If project artifacts change, follow TODO and `APROVADO` gates first.
- Treat tests as executable specifications. Prefer fail-first evidence for verifiable bugfixes, regressions, and behavior-defining changes.
- Classify audit complexity as `small|medium|big`; medium/big audits include Architecture, Code Quality, Tests, Performance, and Security framing.
- Resolve active capabilities, owning manifests, project-owned commands, and affected boundaries before applying stack-specific checks.
- Pair with `bug-fix-evidence-loop`, `test-creation-standard`, `verification-debt-audit`, or `frontend-race-condition-validation` when their scopes apply.

## Preferred Deterministic Helpers

- Run `bash delphi-ai/tools/test_quality_audit.sh`, optionally with `--scan-git-modified` or repeatable `--path <test-path>`.
- For Node/TypeScript capability ownership, run `python3 delphi-ai/tools/node_capability_surface_audit.py --repo <project-root> --expect <capability> [--manifest <relative/package.json>] [--require-script <script>]` before judging runner or script coverage.
- Exit code `2` from the static audit means medium/high signals were found. Review them; do not weaken the scope to clear the signal.

## Generic Guardrails

- `GF-01` Preflight, harness, and environment failures are blocked evidence, not product failures by default.
- `GF-02` Shared-lane validation uses canonical product surfaces; test-only product endpoints are forbidden.
- `GF-03` Parse and contract failures in reference assertions hard-fail.
- `GF-04` Required promotion gates cannot pass with flaky or retry-only outcomes.
- `GF-05` Artifact fallback paths that mask ownership or permission faults are forbidden.
- `GF-06` A narrow test or mocked boundary cannot substantiate a broader compatibility or end-to-end claim.

## Audit Workflow

1. **Frame the audit**
   - Record active capabilities, compatibility intent, changed behaviors, affected boundaries, topology, and relevant baseline decisions.
   - For large or architectural changes, require unit/provider/component plus integration/module/adapter evidence for each affected critical path.
2. **Check fail-first alignment**
   - Identify `test-first`, `test-after`, `not-applicable`, or `unknown` and the concrete assertion that demonstrates the pre-change failure.
   - Classify final-state-only tests that would not expose the bug as `retrofit-risk` unless a coherent non-applicability rationale exists.
3. **Scan for bypass flags**
   - Block committed skips, focused-test markers such as `test.only`/`describe.only`, CI golden-update bypasses, and shared-lane test-only routes.
4. **Match evidence to the claim**
   - Require real infrastructure only when compatibility or the contract crosses that boundary.
   - Verify both reachability and identity/authentication paths when those are part of the claim.
   - Do not accept unit-only evidence for a changed wiring, serialization, persistence, transport, or runtime boundary.
5. **Check fallback logic**
   - Block silent fallback from required real calls to mocks, from an owned fixture to ambient live data, or from canonical artifact paths to fallback directories.
6. **Verify dependency-injection parity**
   - Test replacements must preserve the relevant production token, scope/lifecycle, and failure semantics unless an explicit documented exception is itself asserted.
7. **Validate failure behavior**
   - Require loud failures for error payloads, empty required responses, parse errors, contract mismatches, and rejected dependencies.
   - Block no-exception-only and transport-status-only assertions when business semantics matter.
8. **Validate assertion quality**
   - Assert externally meaningful outcomes and explicit negative states.
   - Cover retriggerable asynchronous races when applicable.
   - Use deterministic owned proof subjects; do not rely on first-row, first-page, or first-candidate ambient data.
9. **Confirm environment and command parity**
   - Verify the exact project-owned runner/package-manager scripts and the topology prerequisites for the active capability.
   - Treat live hosted services, hardcoded production targets, or undeclared local substitutions as findings unless the approved baseline explicitly requires them.
10. **Audit build and runtime integrity when applicable**
    - Confirm authored tests are not stored in compiled output.
    - Match bundle/artifact metadata to the source revision and prove that manual/browser/device targets serve that build.
11. **Audit the claimed platform matrix**
    - Require evidence only for platforms in the claim, but mark any missing required platform `blocked`, never `passed`.
12. **Write issue cards for material findings**
    - Include issue ID, severity, `file:line` evidence, why-now, options A/B/C including do-nothing when reasonable, and recommendation.
13. **Record failure modes and uncertainty**
    - State likely edge cases, assumptions, unknowns, and confidence.
14. **Validate decision adherence**
    - Map each active baseline decision to `Adherent` or `Exception` with evidence. An unresolved exception is not delivery-ready.

## Conditional Stack Checks

- **NestJS:** test provider/use-case behavior, testing-module wiring, provider tokens/scopes/exports, and externally visible contracts at the chosen transport. Use the owning manifest's runner; do not assume Jest, Vitest, HTTP, Express, Fastify, Prisma, or PostgreSQL.
- **Laravel:** use the project-owned safe runner. Require a local MongoDB replica set and prohibit Atlas only when MongoDB is the declared test datastore.
- **Flutter:** require unit, widget, integration, web, or mobile lanes only where the change and platform claim demand them; use project-owned domain/scheme overrides.
- **Browser/Web:** keep test sources outside compiled bundles, use the project-owned browser runner, and require runtime freshness before accepting observations.

## Common Bypass Patterns (Block)

- Catching exceptions and continuing without failing.
- Tests that codify current buggy behavior instead of intended behavior.
- Mock or live-service fallbacks that hide required-boundary failures.
- Dependency-injection scope/token changes without explicit validation.
- Environment flags that disable required integration behavior in CI.
- Overly broad stubs that always succeed.
- Assertions that pass on empty data or ignore required state transitions.
- Ambient live-data selection for release-gating proof subjects.
- End-to-end or architectural safety claimed from unit-only evidence.
- Flaky required gates accepted as pass.
- Behavior-defining changes with no fail-first target and no rationale.

## Required Evidence

- Capability and owning-command inventory.
- Coverage/evidence matrix with deliberate exclusions.
- Proof of the real declared boundary where compatibility requires it.
- Fail-first target or explicit non-applicability rationale.
- Dependency-injection parity evidence or documented/asserted exception.
- Required platform status as `passed|blocked|failed|flaky`.
- Decision-adherence table when baseline decisions are in scope.

## Done Criteria

- No bypass remains in changed tests.
- No unresolved retrofit risk remains for behavior-defining work.
- Evidence layers substantiate, and do not overstate, the compatibility or architecture claim.
- Required real-boundary tests fail loudly on mismatch.
- Exact commands and topology match the declared project surface.
- Material findings have actionable issue cards.
- Required platform and decision evidence is complete or explicitly dispositioned.


## Exact authority / source delphi-ai/workflows/docker/independent-test-quality-audit-method.md

---
description: Define the canonical no-context independent test-quality audit gate for end-of-implementation review, including trigger rules, package hygiene, retry discipline, and resolution handling.
---

# Method: Independent Test Quality Audit

## Purpose
Provide a dedicated end-of-implementation audit focused on the integrity and quality of the tests that justify delivery confidence.

This method exists to detect pass-the-test workarounds, weak assertions, retrofit-only coverage, brittle test rewrites, and other changes that can make validation look green without proving the product behavior that actually matters.
It is stricter than generic final review: it is specifically about whether the tests changed for the right reasons and whether the affected test surface is effective and efficient.
Gate-satisfying evidence must cover the full applicable `test-quality-audit` workload for the scoped stack and risk profile, not just a short answer to a few review questions.

## When It Applies
- Run this method whenever `wf-docker-audit-escalation-method` marks `test_quality_audit` as `required|recommended`.
- The audit-escalation guard is the minimum decision authority for whether this lane is needed.
- If implementation changed test or delivery-risk triggers materially, rerun the audit-escalation guard before trusting the old decision.

## Inputs
- Tactical TODO under `foundation_documentation/todos/active/`.
- Frozen decisions / approved expectations.
- Bounded implementation diff.
- Bounded test diff, or an explicit record that no test diff exists.
- Validation evidence already collected.
- Expected behaviors / Definition of Done still in force.
- Residual risks or uncertainty that still matter to test confidence.

## Audit Lens
- Use `test-quality-audit` as the primary audit lens.
- The audit must explicitly answer:
  - whether changed test logic reflects a real product or contract change;
  - whether any changed test logic appears to exist mainly to make the suite pass;
  - whether the assertions are effective enough to catch the intended regression or behavior break;
  - whether the assertions and coverage are efficient rather than bloated, redundant, or brittle;
  - whether the changed and nearby tests actually cover the required behaviors and failure modes.
- When applicable, also challenge:
  - fail-first or test-first alignment;
  - bypass patterns (`skip`, overly broad stubs, test-only routes, silent mock fallbacks, DI/test harness shortcuts);
  - assertions that only prove transport status or absence of exceptions while missing business outcomes;
  - fixture/runner changes that quietly weaken the guarantees of the suite.

## Minimum Gate-Satisfying Outputs
- The audit evidence must include every applicable output expected by `test-quality-audit`, including:
  - audit framing for target stacks, compatibility intent, and critical user journeys in scope;
  - fail-first / test-first alignment assessment when bugfix, regression, or behavior-defining work is involved;
  - bypass scan results for skips, test-only shortcuts, overly broad stubs, silent fallbacks, and similar masking patterns;
  - real-backend, fallback, DI parity, CI parity, and platform-matrix checks whenever the scoped change or claim makes them relevant;
  - issue cards for every material finding;
  - failure modes / uncertainty notes that still matter to delivery confidence;
  - decision-adherence evidence when active TODO decisions are in scope.
- The five explicit audit questions in this method are mandatory, but they are not sufficient by themselves when the underlying `test-quality-audit` scope requires more.

## Package Hygiene
- The audit package must be bounded. Do not hand the full session transcript or diffuse conversational history to the reviewer.
- Prefer one of these package shapes:
  - `bounded-file-set`: only the implementation/test surfaces and evidence needed for the audit;
  - `bounded-summary`: a concise structured summary of the test-relevant package.
- If using a `bounded-summary`, it must include at minimum:
  - frozen baseline / approved expectations;
  - approved scope boundary;
  - bounded implementation summary;
  - bounded test summary with explicit changed files or explicit `no test diff`;
  - validation evidence index;
  - expected behaviors / Definition of Done;
  - residual risks / unknowns still relevant to validation confidence;
  - any existing blockers or waivers already affecting the test lane.
- Preserve concrete test deltas and expectations instead of paraphrasing them into soft language.

## Required-Gate Waiver Control
- If a `required` independent test-quality audit cannot be completed after an objectively terminal failed attempt and one retry of the complete gate-satisfying package, a `blocked` record alone does not permit `Completed` or `Production-Ready`.
- Only the current human approval authority for the TODO may waive a required test-quality audit gate.
- The waiver record must include:
  - `waiver_reason`
  - `approver_id`
  - `approval_reference`
  - `mitigation_summary`
  - `follow_up_owner`
  - `follow_up_task_id`

## Procedure
1. Use the latest successful `wf-docker-audit-escalation-method` output as the minimum decision authority for this gate.
2. Build the bounded test-audit package.
   - If orchestration tooling is desired, derive a dispatch packet with `python3 delphi-ai/tools/subagent_review_dispatch.py --review-kind test_quality_audit ...`.
3. Run one fresh internal audit with no inherited thread context.
   - This audit pass must use a fresh internal no-context reviewer/subagent with `fork_context=false`; it must not be the implementing agent.
   - Internal no-context reviewer availability inside the active client is treated as operationally mandatory. If no free reviewer slot is available, close/recycle only a terminal inactive review lane and open a fresh reviewer instead of downgrading to self-review; a live reviewer is never recyclable.
   - Do not invoke or treat an external provider as gate-satisfying review evidence.
   - In other environments, use the closest internal equivalent that guarantees no prior thread contamination.
   - Reviewer lifecycle is status-based, not elapsed-time-based. While status is `pending_init` or `running`, wait without a rigid deadline.
   - A polling timeout means only that no terminal event arrived during that polling window. Do not interrupt, close, recycle, replace, duplicate, or repackage/shrink a live review.
4. Prompt the reviewer to return findings first, ordered by severity, and to stay focused on test quality rather than reopen the full architecture.
   - Require explicit positions on:
     - product/test delta alignment;
     - pass-the-test workaround risk;
     - assertion efficacy;
     - assertion efficiency;
     - coverage sufficiency for required behaviors and failure modes;
     - fail-first/test-first alignment when relevant.
5. Treat the audit as challenge evidence only:
   - advisory, never authoritative by itself;
   - it may block closure if it exposes weak or misleading validation, but it does not replace the TODO contract or user approval model.
6. If the first no-context audit attempt reaches objective terminal failure, retry once with the same complete gate-satisfying package by default. Change the package only to repair a concrete proven package defect while preserving the full rubric; a polling timeout while the reviewer remains live requires continued waiting.
7. If a `required` audit still cannot be obtained after an objectively terminal failed attempt and one retry:
   - record the tooling limitation explicitly;
   - do not silently treat bounded self-review as equivalent to a true fresh internal no-context audit;
   - require either a blocker state or an explicit waiver before `Completed` or `Production-Ready`;
   - treat `blocked` as non-satisfying until the gate is actually run or explicitly waived by the approval authority.
8. Resolve every material finding explicitly in the TODO as one of:
   - `Integrated`
   - `Challenged`
   - `Deferred with rationale`
   - If structured reviewer JSON was used, merge it with `python3 delphi-ai/tools/subagent_review_merge.py ...` before recording the authoritative resolution.
   - Prefer the machine-checkable resolution table from `templates/todo_template.md`, then derive `*-resolution.json` with `python3 delphi-ai/tools/gate_finding_resolution_extract.py --review-kind test_quality_audit ...` when metrics are in scope.
9. If the audit invalidates the claimed Definition of Done or shows that test changes do not map to real product change, treat delivery confidence as broken until the tests or scope are corrected.

## Outputs
- A recorded audit decision (`required|recommended|not_needed`) with rationale.
- A bounded audit package reference.
- Findings summarized in the TODO with explicit resolution status.
- A blocker or waiver record if a required independent audit could not be executed.

## Non-Authority Rule
- Fresh internal audits are intentionally independent, but they do not own the decision.
- Delivery authority remains the tactical TODO, the decision-adherence gates, and the normal approval model.


## Exact authority / source foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md

# Tactical TODO — ST-CON-06

## Title
LeadsHug — ST-CON-06: Channel abstrato extensível e cutover do envio comum

## Artifact Identity
- **Artifact type:** tactical_execution_contract
- **Status:** InProgress
- **Version:** 1.2
- **Created:** 2026-10-20
- **Template provenance:** copied delphi-ai/templates/todo_template.md before population.

## Context
Usuário confirmou Channel abstrato/concretos e extensibilidade para Instagram, Facebook/Messenger, Telegram e outros; em2026-10-20 autorizou avançar ao contrato. Este TODO entrega o cutover do envio textual comum atual, não novos provedores reais. MetaClient/EvolutionClient já são interfaces injetadas, mas Conversa/Typebot conhecem ambos e seus parâmetros. O parecer de enquadramento identificou outcomes falsamente tratados como recusa, escopo/versionamento insuficientemente expresso e fallback de canal divergente da política. Decisões abaixo concretizam esses pontos antes da revisão tática. O parecer anterior não satisfaz os gates deste contrato e concordância com conceito não é APROVADO específico.

## Framing Source & Story Slice
- **Feature brief:** foundation_documentation/artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md
- **Primary story ID:** ST-CON-06
- **Why this is the right current slice:** um owner de transporte comum para todos os senders existentes, antes de modelos ST-CON-05 e primeiro envio ST-CON-04.
- **Direct-to-TODO rationale (required when `Feature brief = direct-to-todo`):** n/a; brief e parecer prévios publicados.

## Contract Boundary
- This TODO defines **WHAT** must be delivered and what counts as done.
- `Assumptions Preview` and `Execution Plan` below define **HOW** Delphi currently intends to deliver this contract.
- This TODO is **bounded but elastic**: Delphi may absorb local discoveries only while they remain inside the same primary objective and the same main approval/review/promotion conversation. Secondary modules may still be touched when they are subordinate to that same slice.
- If any assumption or plan step changes `Scope`, `Out of Scope`, `Definition of Done`, required validation semantics, public contract, or frozen decisions, update the TODO contract first and request renewed approval before execution continues.
- If the intended path explicitly authorizes a compatibility shim, fallback bridge, dual-read/dual-write period, or another non-canonical temporary construct, record that authorization in the TODO with exact scope, rationale, and removal/closeout condition. Reviewers must be able to distinguish an approved temporary exception from accidental workaround drift.

## Implementation Intent
- **Current delivery:** contrato abstrato de envio textual, resolução scoped, implementações atuais e orquestração compartilhada, com política/outcomes/consumers/testes coerentes.
- **Planned next steps:** reconvergir ST-CON-05 para capacidades de modelos e ST-CON-04 para primeiro envio/intent; redes adicionais em histórias próprias.
- **Anticipatory implementation authorized now:** somente o ponto de extensão e fake de teste exigidos no D01/08; nenhuma implementação/capacidade real futura.
- **Rationale:** dependências apontam ao domínio abstrato; protocolo e segredo ficam nos adapters, aceitação/política no domínio.

## Delivery Status Canon (Required)
- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** aguardar as três auditorias dedicadas e adjudicar; ativar API/Web locais preservando dados/canais, restaurar HTTPS e obter INOUT assistida; concluir PCV/módulos/finalreview/guardas antes de Local-Implemented.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** review
- **Why this state now:** APROVADO específico recebido e binding recarregado; seguir Ordered Steps com executor único e autoridade normal go antes de código.
- **Exit condition:** implementação aderente com all/assurance/pcv e prova real pós-publicação local; nenhum bloqueador de review aberto antes de entrega.

## Scope
- [ ] SCOPE-01 — Channel/ChannelResolver abstratos de domínio, registro explícito e instâncias por operação, concretos oficial/não oficial e extensão verificada com fake não WhatsApp.
- [ ] SCOPE-02 — Migrar envios de Conversa BFF/API pública e respostas Typebot para a mesma orquestração, mantendo autenticações próprias, política e MessageAcceptanceService único.
- [ ] SCOPE-03 — Contexto autorizado e owner BU/canal, segredos privados, credencial/identidade correntes e fences explícitos; nenhuma troca silenciosa do canal selecionado.
- [ ] SCOPE-04 — Outcomes tipados verdadeiros, projeção pública explícita de erro/disponibilidade e UI honesta; sem retry externo automático ou garantia de exactly-once.
- [ ] SCOPE-05 — Runner de inventário positivo antes de testes, harness durável de imports/contrato/PG/Playwright, regressões completas e prova real assistida nos dois vínculos próprios; consolidação/revisões de entrega.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)
n/a; sem entrega de produto reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)
Planejamento não bloqueado; readiness de runtime/túnel/aparelhos revalidada depois da aprovação. Ausência de template aprovado não bloqueia esta história textual em janela válida.

## Execution Lane Tracking (Required)
- **Local implementation branches:** root/api/web:feature/number-onboarding, confirmar antes de executor; Foundation:main.
- **Promotion lane path:** local feature → dev → stage → main; nenhum push/deploy de produto nesta autorização local proposta.
- **Lane-promoted threshold for this TODO:** dev, fora do escopo atual.
- **Production-ready threshold for this TODO:** main e gates próprios, sem claim atual.

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)
n/a; só Foundation main é autoridade documental autônoma nesta preparação.

## Out of Scope
- [ ] Instagram/Messenger/Telegram reais, alteração de identidade/BU/contato/schema ou enums de persistência para novas redes; fake não prova integração real.
- [ ] Criação/envio de templates, Nova conversa manual/novo intent, importação, campanhas, anexos ou novos fluxos Typebot; ST-CON-05/04 permanecem separados.
- [ ] Reescrever OAuth/QR/cadastro/lifecycle, rotacionar credenciais, desconectar vínculos ou criar sondagem externa por envio.
- [ ] Worker/outbox/fila, durable intent/exactly-once externo, retry automático de POST, heurística para unir eco sem ID.
- [ ] Delphi, worktrees/cópias, gitlinks/.gitmodules, deploy/push de produto, leitura de .env/.env.testing e qualquer read/list/stat/hash/traversal/mount/stage api-app/.local-files.

## Diff Expectation Contract
Required before delivery. Heading normalized for canonical parser; contract obligation unchanged.
- **Contract status:** required
- **Policy:** strict; forbidden/unclassified blocks delivery
- **User validation:** required on deviation
- **Comparison mode:** working_tree

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| root | . | 80e3940126f22a941f90dba4f5e801b6c0eb2f58 | working_tree |
| api | api-app | db5a86758a165fac8a1ab587599c37b17890530c | working_tree |
| web | web-app | 74b9d4b714044829796f875d00553f077c1c329d | working_tree |
| foundation | foundation_documentation | 82fa66b33b81b31024dc8cebef9e72e9253964a7 | working_tree |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/domain/channels/transport/** | any | ports/resolver/orquestração/registro e harness |
| api | src/integrations/channels/** | any | concretos e projeções privadas |
| api | src/domain/channels/channel-credential-resolver.ts | M | contexto/versionamento privado, send protegido |
| api | src/domain/inbox/outbound*.ts | any | política/orquestração sem ciclo DI com Conversations |
| api | src/domain/inbox/conversations.service.ts | M | seleção/política e consumo abstrato |
| api | src/domain/inbox/incoming.service.ts | M | Typebot usa saída comum |
| api | src/integrations/meta/meta.client.ts | M | texto com resultado tipado; cadastro preservado |
| api | src/integrations/meta/*.spec.ts | any | wire/erro real do adapter |
| api | src/integrations/evolution/evolution.client.ts | M | texto com resultado tipado |
| api | src/integrations/evolution/*.spec.ts | any | wire/classificação conservadora |
| api | src/surfaces/bff/conversations.controller.ts | M | contexto autorizado e DTO disponibilidade |
| api | src/surfaces/public/conversations.controller.ts | M | contexto API key e projeção compatível |
| api | src/surfaces/bff/bff.module.ts | M | DI da composição única |
| api | src/surfaces/public/public.module.ts | M | DI preservando auth |
| api | src/surfaces/webhooks/webhooks.module.ts | M | DI Typebot/ingress |
| api | test/channel-transport* | A, ?? | PG/contrato/corridas |
| api | test/helpers.ts | M | fakes/DI de contrato |
| api | test/timeline-fixtures.cjs | M | provider controlado de browser |
| api | test/browser-server.cjs | M | bootstrap real |
| api | test/*.e2e-spec.ts | M | suites consumidoras da interface alterada, sem afrouxar assertivas |
| api | src/domain/inbox/*.spec.ts | M | consumo abstrato e regressões |
| web | src/api.ts | M | DTO aditivo disponibilidade |
| web | src/api.spec.ts | M | companion de metadados seguros D10; admissão humana2026-10-20 |
| web | src/telas/Inbox.tsx | M | composer indisponível/motivo e erro |
| web | src/telas/Inbox*.test.tsx | any | render/estado |
| web | e2e/channel-transport* | A, ?? | mutation BFF real |
| web | e2e/number-onboarding-freshness.ts | M | manifesto se afetado |
| web | e2e/timeline-freshness.ts | M | companion chamado antes do manifesto; pathspec positivo antes de discovery; admissão humana2026-10-20 |
| root | scripts/test-channels-local.sh | M | inventário positivo seguro antes de testes |
| foundation | todos/active/features/TODO-leadshug-channel-abstraction.md | A, M | governança/evidências |
| foundation | todos/completed/features/TODO-leadshug-channel-abstraction.md | A | closeout após gates |
| foundation | todos/active/features/TODO-leadshug-official-template-authoring.md | M | handoff sem execução |
| foundation | todos/active/features/TODO-leadshug-start-conversation-by-contact.md | M | handoff sem execução |
| foundation | artifacts/reviews/leadshug-channel-abstraction-20261020/** | any | reviews/evidências |
| foundation | artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md | M | link do contrato |
| foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | sequência |
| foundation | backlog/README.md | M | próximo gate |
| foundation | artifacts/dependency-readiness.md | M | readiness observada |
| foundation | modules/integrations-and-channels.md | M | ports/outcomes/cutover após entrega |
| foundation | modules/inbox-and-conversations.md | M | política/consumers após entrega |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | .local-files/** | any | privado, nem percorrer |
| api | .env* | any | segredo/config intocados |
| api | prisma/** | any | sem mudança de persistência/migration |
| root | .env* | any | privado |
| root | .gitmodules | any | pipeline-owned |
| root | api-app | any | gitlink pipeline-owned |
| root | web-app | any | gitlink pipeline-owned |
| root | delphi-ai | any | sem self-improvement |
| web | dist/** | any | gerado, não fonte |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
Guard público preliminar executado com fonte canônica inalterada e invocações Git limitadas ANTES da descoberta por pathspecs positivos (API/Web/root); não é guard final de entrega ou prova dos paths excluídos. Primeiro título com sufixo não foi reconhecido pelo parser; normalizado sem alterar obrigação. A segunda execução encontrou 88 mudanças públicas,85 esperadas e3 diferenças mecânicas de tipo, zero path proibido ou novo path fora do escopo.

| Finding | Classification | Resolution / authority |
| --- | --- | --- |
| api:test/channel-transport.e2e-spec.ts aparece ?? e já era adição A aprovada | noise; by-design/no-action in product | Comparação working_tree inclui arquivo ainda não staged; adicionar ?? ao mesmo glob já aprovado representa a mesma adição, não amplia paths nem produto; não stagear fonte por conveniência do guard |
| web:e2e/channel-transport.spec.ts aparece ?? e já era adição A aprovada | noise; by-design/no-action in product | Mesmo ajuste mecânico A,?? no mesmo glob aprovado, sem mudar cobertura ou permissão funcional |
| Foundation TODO aparece A contra baseline82fa66b e constava só M | noise; by-design/no-action in product | O contrato foi criado depois da baseline, portanto A,M expressa a criação/modificação documental já autorizada; nenhum novo artefato/escopo |

Evidência histórica: evidence/public-diff-working-tree-type-no-go.json. Ajuste de representação Git não muda Scope/DoD/decisões/risco/paths e não exige nova aprovação material; as duas admissões de paths reais permanecem validadas separadamente pelo usuário. Descoberta de path real não aprovado continua bloqueada e exige validação humana. Rerun preliminar e final ainda necessários.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** DI, DTO/fixture/componente subordinados ao mesmo envio comum e preservação de seus invariantes.
- **Must update or split the TODO:** schema/novo provedor/capacidade real, template/intent novo, mudança de política fora das decisões e novos endpoints.

## Definition of Done
- [ ] DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real.
- [ ] DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes.
- [ ] DOD-03 — Seleção humana/pública segue última origem determinística ou único vínculo; bot fica no ingresso verificado; policy/janela comuns, ausência/ambiguidade sem fallback e disponibilidade/UI honestas preservam rascunho.
- [ ] DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout.
- [ ] DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; finalização pública/humana não rouba claim e bot conserva fila/owner; falhas locais pós-ACK e unknown estão explícitas.
- [ ] DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot.
- [ ] DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede.
- [ ] DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção.

## Validation Steps
- [ ] VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo, sem subset como aceite, com API/PG reais e bundle servido fresco.
- [ ] VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco.
- [ ] VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa.
- [ ] VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto.
- [ ] VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff.

## Completion Evidence Matrix (Required Before Delivery Claim)
| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD-01 | Definition of Done | DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real. | canonical tests / source / review | channel-dependencies.spec synthetic negative; independent opaque Channel via real resolver/BFF/PG in channel-transport.e2e; ChannelTransportModule composition; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | No real future network claimed; current storage provenance preserved |
| DOD-02 | Definition of Done | DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes. | canonical tests / source / review | channel-transport.e2e denied session/CSRF/key, crossBU/ingress, simultaneous twoTENANT token/resource/localMessage probes; actualMeta/Evo fence omission failures then restored; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Scoped immutable operation context; local-check-to-network interval remains |
| DOD-03 | Definition of Done | DOD-03 — Seleção humana/pública segue última origem determinística ou único vínculo; bot fica no ingresso verificado; policy/janela comuns, ausência/ambiguidade sem fallback e disponibilidade/UI honestas preservam rascunho. | canonical tests / source / review | channel-transport.e2e origin tie/sole/absent/multi/ingress pinning; Typebot window expiry; channel-transport browser unavailable/unknown/A-B-A and FRC5x20; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Source/served hash attestation80903; no blind fallback or retry |
| DOD-04 | Definition of Done | DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout. | canonical tests / source / review | meta.client.spec/evolution.client.spec complete raw envelopes and onePOST; outbound.service.spec local incomplete; PG contradictory200 persistednothing; browserunknown draft; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | R01/R03/R05 counterexamples fixed; ACCEPTED is acknowledgement, not handset delivery |
| DOD-05 | Definition of Done | DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; finalização pública/humana não rouba claim e bot conserva fila/owner; falhas locais pós-ACK e unknown estão explícitas. | canonical tests / source / review | api-publica.e2e public/echo provenance; channel-transport.e2e claim/public-BFF overlap; number-onboarding-typebot.e2e pinned reply/queue/echo; unchanged keyedAcceptance owner hash; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Same Message writer, captured-key readback only; crash/nullID dedupe limits preserved |
| DOD-06 | Definition of Done | DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot. | canonical tests / source / review | evidence/runner-checkpoint.json before RED; canonical all80903 terminal0 194unit+309PG+29Web+50browser; rawlog778f8589; source/served/dist bundle27c5db46; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | One frozen principal checkout; realPG/Chromium, provider boundaries controlled; remoteCI not claimed |
| DOD-07 | Definition of Done | DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede. | runtime / audit | New image/runtime attestation and assisted IN/OUT official+unofficial receipt not yet collected; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | Requires localactivation/newHTTPS/operator; CP108 and fixtures do not substitute |
| DOD-08 | Definition of Done | DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção. | runtime / audit | Dedicated audit session active; PCV candidates measured; final review/modules/guards/closeout and05/04handoff pending; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | No Local-Implemented or production/promotion claim |
| VAL-01 | Validation Steps | VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo, sem subset como aceite, com API/PG reais e bundle servido fresco. | canonical tests / source / review | bash scripts/test-channels-local.sh all; run80903 exit0, exact sourceafter/36changedsource manifest matches and served/dist/preserved JS match; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Node22.23.3, PostgreSQL16; canonical local gate, not remoteCIexecution |
| VAL-02 | Validation Steps | VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco. | canonical tests / source / review | RawMeta/Evo HTTP unit; channel-transport realPG auth/factory/generation/version/key/claim; bot/public/acceptance suites in all80903; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Fake opaque recipient proves internal substitution; shipping adapters omitted-guard mutants detect regressions |
| VAL-03 | Validation Steps | VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa. | canonical tests / source / review | web-app/e2e/channel-transport.spec.ts in browser50/50 all80903; real BFF/PG, nativebody/task barrier; guardmutant30246 expected draftempty failure49/50; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_validation / API3100+Web4173 | passed | Exact browserfixture source hashes andserved publicbundle attested; no production test route or DTOhook |
| VAL-04 | Validation Steps | VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto. | runtime / audit | Pending API/Web activation, newHTTPS and operator IN/OUT on both existingbindings; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | No channelreregistration/secretrotation/dbreset authorized |
| VAL-05 | Validation Steps | VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff. | runtime / audit | IndependentPerformance/TQA/Cutover running; sourcepublicdiff171expected/0forbidden/0unclassified; finalreview/consolidation/guards remain; artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/causal-final-validation80903.json | leadshug_channels_local / own test channels | pending | Current source stable; no audit waivers or new sibling implementation |

## External Dependency Readiness (Required When External Systems Matter)
| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| runner Docker próprio | regressões completas | ready | 2026-10-20 all80903 | positive bind inventory beforetests,194/309/29/50passed; source/served proof | Node22.23.3/PG16 disposable; privatehostinputs excluded |
| vínculos de teste oficial/QR | prova real de resposta | unknown | CP108 histórico2026-10-19 | prova passada não é saúde atual | revalidar runtime/túnel/operador depois de aprovação |
| semântica de erros de provider | evitar falsa recusa | partial | fontes locais2026-10-20 | adapter atual colapsa falhas | classifier conservador D04, sem inferir de string |
| redes futuras | extensibilidade | unknown | nenhuma integração | só fake independente | contratos próprios de identidade/capacidades, sem alegar funcionamento |

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs,react,vite,postgresql,prisma,docker
- **Expected supporting profiles:** strategic-cto,operational-devops,assurance-tester-quality,assurance-security-adversarial
- **Scope-check command:** python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Gate 0:** Genesis rejeitado; contexto canônico existente. Genesis rejeitado pelo canon existente; ativo operational-coder com handoffs DevOps/assurance planejados.

### Handoff Log (Update when execution crosses profile boundaries)
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | APROVADO explícito recebido2026-10-20 | API/Web/runner/harness | active; binding reload + authority-execution.json |
| operational-coder | operational-devops | readiness/publicação local | imagem própria e recursos de teste | planned |
| operational-coder | assurance-tester-quality | aderência/cutover/TQA/final | pacote público bounded | active; dedicated-audit/session.json, round01; primary80903passed |
| operational-coder | assurance-security-adversarial | isolamento/segredos/DI | resolução e surfaces | rounds1/2/3 terminal; findings integrated, R02 proof/finalTQA pending |

## Complexity
- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section
- **Why this level:** cutover cross-stack de todos senders, auth/identidade e contratos de resultado externo, com mudanças funcionais expressas e regressão real.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** foundation_documentation/modules/integrations-and-channels.md
- **Secondary module docs (if any):** foundation_documentation/modules/inbox-and-conversations.md
- **Planned decision promotion targets (module sections):** Integrations: Channel/resolução/DI/outcomes/extensão; Inbox: seleção/disponibilidade/saída comum e limites.
- **Module decision consolidation targets (required):** mesmos targets com provenance D01..10, retirar descrição de dispatch direto; invariantes de BU/aceitação/segredo preservados.

## Decision Pending (Resolve Before Freeze)
Nenhuma decisão de produto aberta. Assinaturas e semântica material congeladas abaixo para challenge tático; readiness externa continua desconhecida.

## Decisions (Resolved Before Freeze)
- [x] D-01 — Channel é abstract class no domínio, sendMessage recebe {kind:text,recipientRef:string,text:string} e retorna ChannelSendResult discriminado. recipientRef é opaco ao port; sem E164/WABA/phoneNumberId/instância/QR como contrato universal. Limites4096 atuais permanecem nos consumers atuais, não são requisito universal da abstração. ChannelResolver abstrato retorna implementação registrada; seleção por registro explícito, sem if/provider nos senders. Concretos atuais usam clients HTTP; nenhum new no domínio, global useClass único, ModuleRef/service locator ou singleton mutável de BU/token.
- [x] D-02 — Resolução recebe referência de conversa/BU/canal carregada server-side após autorização de sessão ou API key OU referência do ingresso já verificado para Typebot; não aceita declaração de provider/owner/credencial do body. Validar owner BU/Mantenedora do vínculo e identidade corrente, ownNumberVerified/verifiedEpoch/readiness/receipt e envelope atuais usando o owner de credenciais existente. Expor somente binding/proveniência safe para aceitação; tokens/IDs de protocolo ficam privados ao concreto. Resolver atual não autoriza ator e não retorna versão: adequação explícita, sem fingir garantia já existente. Auth por sessão/API key/bot mantém fontes diferentes, nunca exigir usuário humano no bot ou tomar disponibilidade como grant.
- [x] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST não há rollback externo: somente mudança de credentialVersion com identidade/generation/epoch TODOS inalterados permite aceitar o recibo capturado. REAUTORIZAR real incrementa generation, mesmo no mesmo recurso; não substituir a generation antiga. Mudança de identidade/generation/epoch depois do efeito não rebind/migra conteúdo:409 CHANNEL_CONTEXT_CHANGED; ACK conhecido conserva outcome ACCEPTED_LOCAL_INCOMPLETE e localMessageState RECORDED ou UNCONFIRMED conforme D05; sem ID, UNKNOWN. MessageAcceptance conserva seu fence. Testar REAUTORIZAR real concorrente e version-only separadamente. Janela entre leitura/CAS local e rede existe, sem fence atômico externo ou nova operação durável.
- [x] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
- [x] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID tenta recordAmbiguousOutbound uma vez por execução: somente commit confirmado permite409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, diagnóstico FALHOU/null-ID, nunca Message ENVIADA. Precedência: mudança detectada de identidade/generation/epoch após dispatch sem ID, inclusive antes ou durante o fence de recordAmbiguousOutbound, devolve409 CHANNEL_CONTEXT_CHANGED/outcome UNKNOWN; não rebind nem grava diagnóstico sob contexto novo. Somente OUTRAS falhas/commit incerto do diagnóstico devolvem503 OUTBOUND_LOCAL_INCOMPLETE/outcome UNKNOWN/evidence ACK_WITHOUT_ID/diagnosticPersistence UNCONFIRMED, sem afirmar diagnóstico gravado; no409 só declarar diagnóstico gravado com evidência positiva do commit capturado, senão UNCONFIRMED. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa. ACK externo válido seguido de QUALQUER falha local de aceitação/reconciliação/finalização conserva outcome ACCEPTED_LOCAL_INCOMPLETE;409 CHANNEL_CONTEXT_CHANGED se fence alterado, senão503 OUTBOUND_LOCAL_INCOMPLETE. Texto fixo O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente. localMessageState RECORDED somente com commit de Message confirmado ou readback positivo pelo owner/chave/proveniência capturados; nos demais casos UNCONFIRMED, inclusive rollback local confirmado pois eco pode ter gravado em paralelo. No máximo um readback local bounded, sem rebind ou nova chamada externa. Falha após Message commit mantém RECORDED mesmo se atribuição/status falhar; nenhum erro local vira recusa externa. Propagação transient do recibo não cria intent/outbox/schema/segundo owner. UI preserva draft e nunca reenvia automaticamente; Typebot interrompe a rodada, sem replay de saídas. Sem durabilidade/recuperação prometida nem união heurística de Message nula ao eco; dedupe sem ID continua limite para ST-CON-04.
- [x] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), política extraída sem ciclo DI com ConversationsService, executa policy/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/autoria/publicação. Input trusted distingue BFF humano, API EXTERNO com snapshot e bot; autoria/intenção de atribuição entram ANTES do dispatch. Remover message.update e conversation.update de conclusão no controller público; não limpar autoria comprovada no sender/echo. Para respostas humanas/públicas, atribuição após ACCEPTED é condicional sobre owner corrente, nunca snapshot semDono: claim concorrente é preservado, inclusive público vs claim humano e overlap BFF/público. Status humano/público move IN_SERVICE (grupo preservado); resposta aceita após close concorrente pode reabrir sem roubar novo owner. Bot conserva autoria/unread/status de fila/owner humano e não executa essa finalização humana. Toda falha local pós-ACK segue D05 mesmo após Message commit. MessageAcceptance e índices preservados, nenhum schema novo;04 reconverge primeiro envio depois.
- [x] D-07 — Seleção para resposta BFF/API pública usa última mensagem por createdAt DESC,id DESC (ordenação DB, mesma timeline); se seu vínculo falta, nunca substitui por primeiro/outro conectado. Sem última origem: único vínculo pode ser usado; zero CANAL_AUSENTE400, múltiplos CANAL_AMBIGUO409. Origem sem vínculo CANAL_SELECIONADO_INDISPONIVEL409. Bot usa exclusivamente channelId/identidade do ingresso aceito/verificado, mesmo se outra entrada mais recente vier por outro transporte; sem fallback/rebind. Policy comum avalia readiness e requiresWindow do binding selecionado para TODOS, inclusive bot: corrigir explicitamente bypass atual do Typebot. Reavaliar janela antes de cada texto do bot; expiração bloqueia zeroPOST e interrompe rodada, sem replay. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. disponivel observa localmente seleção/policy/trust/conexão/credencial cadastrada, não prova provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem token/rede/mutação; reutilizar metadados da BU na lista, sem novo fan-out por conversa, medir EPS. GET thread não falha por canal ausente: janela mantém exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null se seleção impossível. Lista pública mantém campos e acrescenta envio_disponivel/motivo_indisponibilidade. API pública mantém criação prévia da conversa, inclusive vazia em erro; mudar isso é contrato04.
- [x] D-08 — Extensão aberta por factories/registro DI tipado, inicialmente dois providers. Fake com recipientRef user:opaque não telefônico passa pelo mesmo resolver/owner/BFF com conversa seeded e bot/internal fixtures, sem alterar branches/interfaces dos senders. Regressão pública conserva telefone numérico/normalização atual; não exigir handle Telegram no POST /api/v1/messages. Enum físico OFICIAL/NAO_OFICIAL permanece no adapter de binding; fixture pode mapear slot existente ao fake, sem flag de produto nem alegar rede nova persistida. Registrar adapter estende o port; identidade/BU/contato/credenciais/ingress de redes futuras exigem contratos próprios. Capacidades terão ports pequenos em05/04 e lifecycle futuro, sem no-op/NotImplemented/casts/concrete instanceof nos consumers; não implementar runtime antecipado.
- [x] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
- [x] D-10 — UI Inbox e ErroDaApi em api.ts preservam outcome e metadados safe de incerteza do backend, exibem texto fixo honesto, bloqueiam composer por disponibilidade/motivo e mantêm draft em qualquer erro/UNKNOWN/ACCEPTED_LOCAL_INCOMPLETE; sem sucesso ou retry automático. Respostas atrasadas em troca BU/conversa conservam fencing monotônico atual. HTTP sucesso/DTOs de mensagem preservados; disponibilidade/outcome aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts positivos/descartáveis. all completo em leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais INOUT assistida dos dois vínculos. Consolidar owners/limites e rebase05/04 só após gates.

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| constitution#system-invariants | BU/número, domínio backend, superfícies separadas | Preserve | D01/02/08/09 |
| integrations#invariants | providers adapters, erros determinísticos, segredo privado | Preserve | D01/03/04/05 |
| integrations#send-ST-CON-01 | consumer usa credencial scoped/current/receipt | Preserve | novo binding privado, send readiness intacta |
| inbox#aceitação-ST-CON-01 | MessageAcceptance único, identity/gen/epoch, sender/echo | Preserve | D03/06, sem schema |
| inbox#seleção/atribuição | sem troca automática/sem roubar claim | Preserve | corrigir desvio de fallback e snapshot de owner |
| integrations/inbox#projeção-erros | código técnico específico distingue plataformas | Preserve | mapper explícito, outcome aditivo, sem false refusal de UNKNOWN |
| ST-CON-05/04 pending | modelos/primeiro envio em contratos próprios | Preserve | só handoff/reconvergência, sem execução |

## Decision Baseline (Frozen Before Implementation)
- [ ] D-01 — Channel é abstract class no domínio, sendMessage recebe {kind:text,recipientRef:string,text:string} e retorna ChannelSendResult discriminado. recipientRef é opaco ao port; sem E164/WABA/phoneNumberId/instância/QR como contrato universal. Limites4096 atuais permanecem nos consumers atuais, não são requisito universal da abstração. ChannelResolver abstrato retorna implementação registrada; seleção por registro explícito, sem if/provider nos senders. Concretos atuais usam clients HTTP; nenhum new no domínio, global useClass único, ModuleRef/service locator ou singleton mutável de BU/token.
- [ ] D-02 — Resolução recebe referência de conversa/BU/canal carregada server-side após autorização de sessão ou API key OU referência do ingresso já verificado para Typebot; não aceita declaração de provider/owner/credencial do body. Validar owner BU/Mantenedora do vínculo e identidade corrente, ownNumberVerified/verifiedEpoch/readiness/receipt e envelope atuais usando o owner de credenciais existente. Expor somente binding/proveniência safe para aceitação; tokens/IDs de protocolo ficam privados ao concreto. Resolver atual não autoriza ator e não retorna versão: adequação explícita, sem fingir garantia já existente. Auth por sessão/API key/bot mantém fontes diferentes, nunca exigir usuário humano no bot ou tomar disponibilidade como grant.
- [ ] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST não há rollback externo: somente mudança de credentialVersion com identidade/generation/epoch TODOS inalterados permite aceitar o recibo capturado. REAUTORIZAR real incrementa generation, mesmo no mesmo recurso; não substituir a generation antiga. Mudança de identidade/generation/epoch depois do efeito não rebind/migra conteúdo:409 CHANNEL_CONTEXT_CHANGED; ACK conhecido conserva outcome ACCEPTED_LOCAL_INCOMPLETE e localMessageState RECORDED ou UNCONFIRMED conforme D05; sem ID, UNKNOWN. MessageAcceptance conserva seu fence. Testar REAUTORIZAR real concorrente e version-only separadamente. Janela entre leitura/CAS local e rede existe, sem fence atômico externo ou nova operação durável.
- [ ] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
- [ ] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID tenta recordAmbiguousOutbound uma vez por execução: somente commit confirmado permite409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, diagnóstico FALHOU/null-ID, nunca Message ENVIADA. Precedência: mudança detectada de identidade/generation/epoch após dispatch sem ID, inclusive antes ou durante o fence de recordAmbiguousOutbound, devolve409 CHANNEL_CONTEXT_CHANGED/outcome UNKNOWN; não rebind nem grava diagnóstico sob contexto novo. Somente OUTRAS falhas/commit incerto do diagnóstico devolvem503 OUTBOUND_LOCAL_INCOMPLETE/outcome UNKNOWN/evidence ACK_WITHOUT_ID/diagnosticPersistence UNCONFIRMED, sem afirmar diagnóstico gravado; no409 só declarar diagnóstico gravado com evidência positiva do commit capturado, senão UNCONFIRMED. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa. ACK externo válido seguido de QUALQUER falha local de aceitação/reconciliação/finalização conserva outcome ACCEPTED_LOCAL_INCOMPLETE;409 CHANNEL_CONTEXT_CHANGED se fence alterado, senão503 OUTBOUND_LOCAL_INCOMPLETE. Texto fixo O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente. localMessageState RECORDED somente com commit de Message confirmado ou readback positivo pelo owner/chave/proveniência capturados; nos demais casos UNCONFIRMED, inclusive rollback local confirmado pois eco pode ter gravado em paralelo. No máximo um readback local bounded, sem rebind ou nova chamada externa. Falha após Message commit mantém RECORDED mesmo se atribuição/status falhar; nenhum erro local vira recusa externa. Propagação transient do recibo não cria intent/outbox/schema/segundo owner. UI preserva draft e nunca reenvia automaticamente; Typebot interrompe a rodada, sem replay de saídas. Sem durabilidade/recuperação prometida nem união heurística de Message nula ao eco; dedupe sem ID continua limite para ST-CON-04.
- [ ] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), política extraída sem ciclo DI com ConversationsService, executa policy/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/autoria/publicação. Input trusted distingue BFF humano, API EXTERNO com snapshot e bot; autoria/intenção de atribuição entram ANTES do dispatch. Remover message.update e conversation.update de conclusão no controller público; não limpar autoria comprovada no sender/echo. Para respostas humanas/públicas, atribuição após ACCEPTED é condicional sobre owner corrente, nunca snapshot semDono: claim concorrente é preservado, inclusive público vs claim humano e overlap BFF/público. Status humano/público move IN_SERVICE (grupo preservado); resposta aceita após close concorrente pode reabrir sem roubar novo owner. Bot conserva autoria/unread/status de fila/owner humano e não executa essa finalização humana. Toda falha local pós-ACK segue D05 mesmo após Message commit. MessageAcceptance e índices preservados, nenhum schema novo;04 reconverge primeiro envio depois.
- [ ] D-07 — Seleção para resposta BFF/API pública usa última mensagem por createdAt DESC,id DESC (ordenação DB, mesma timeline); se seu vínculo falta, nunca substitui por primeiro/outro conectado. Sem última origem: único vínculo pode ser usado; zero CANAL_AUSENTE400, múltiplos CANAL_AMBIGUO409. Origem sem vínculo CANAL_SELECIONADO_INDISPONIVEL409. Bot usa exclusivamente channelId/identidade do ingresso aceito/verificado, mesmo se outra entrada mais recente vier por outro transporte; sem fallback/rebind. Policy comum avalia readiness e requiresWindow do binding selecionado para TODOS, inclusive bot: corrigir explicitamente bypass atual do Typebot. Reavaliar janela antes de cada texto do bot; expiração bloqueia zeroPOST e interrompe rodada, sem replay. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. disponivel observa localmente seleção/policy/trust/conexão/credencial cadastrada, não prova provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem token/rede/mutação; reutilizar metadados da BU na lista, sem novo fan-out por conversa, medir EPS. GET thread não falha por canal ausente: janela mantém exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null se seleção impossível. Lista pública mantém campos e acrescenta envio_disponivel/motivo_indisponibilidade. API pública mantém criação prévia da conversa, inclusive vazia em erro; mudar isso é contrato04.
- [ ] D-08 — Extensão aberta por factories/registro DI tipado, inicialmente dois providers. Fake com recipientRef user:opaque não telefônico passa pelo mesmo resolver/owner/BFF com conversa seeded e bot/internal fixtures, sem alterar branches/interfaces dos senders. Regressão pública conserva telefone numérico/normalização atual; não exigir handle Telegram no POST /api/v1/messages. Enum físico OFICIAL/NAO_OFICIAL permanece no adapter de binding; fixture pode mapear slot existente ao fake, sem flag de produto nem alegar rede nova persistida. Registrar adapter estende o port; identidade/BU/contato/credenciais/ingress de redes futuras exigem contratos próprios. Capacidades terão ports pequenos em05/04 e lifecycle futuro, sem no-op/NotImplemented/casts/concrete instanceof nos consumers; não implementar runtime antecipado.
- [ ] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
- [ ] D-10 — UI Inbox e ErroDaApi em api.ts preservam outcome e metadados safe de incerteza do backend, exibem texto fixo honesto, bloqueiam composer por disponibilidade/motivo e mantêm draft em qualquer erro/UNKNOWN/ACCEPTED_LOCAL_INCOMPLETE; sem sucesso ou retry automático. Respostas atrasadas em troca BU/conversa conservam fencing monotônico atual. HTTP sucesso/DTOs de mensagem preservados; disponibilidade/outcome aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts positivos/descartáveis. all completo em leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais INOUT assistida dos dois vínculos. Consolidar owners/limites e rebase05/04 só após gates.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)
- **Applicability (`required|not_needed`):** required
- **Why this applies:** estabelece port comum e retira dispatch específico duplicado dos negócios.
- **Deviation / debt being retired:** Consumers dependem de dois providers/IDs e mapeiam toda falha como recusa; seleção/atribuição violam intenção canônica.
- **Target steady-state after closeout:** Channel/Resolver de domínio, registro/adapters privados, uma saída comum e aceitação única.
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** nenhum sender comum usa provider client/dispatch antigo; cadastro/protocolo específicos permanecem legítimos e não são compat shim.

### Patterns To Enforce (Required when applicability = `required`)
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| consumidor depende do Channel | D01/08/09 | outbound | extensibilidade verificável |
| contexto privado por operação | D02/03 | resolver/concretos | sem vazamento ou cross-BU |
| aceitação única | ST-CON-01/D06 | todos senders | dedupe/autoria/epoch |

### Prohibited Anti-Patterns (Required when applicability = `required`)
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| adicionar interface e manter branch no sender | dependency harness/AST | falso DIP | none |
| singleton que troca token/BU | barriers concorrentes | cross-tenant | none |
| timeout como recusa ou retry POST | raw HTTP count | efeito externo incerto | none |
| mega-interface com no-op/cast específico | shared contract/fake | quebra substituição/segregação | none |

### Architecture Protection Harness (Required when applicability = `required`)
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| dependency guard/test | api src/domain/channels/transport/channel-dependencies.spec.ts | all + violation fixture | imports/dispatch diretos fora allowlist | implement-in-this-todo | DOD01/06/08 |
| shared contract/PG | api test/channel-transport.e2e-spec.ts | all | substituição/scopes/identity/unknown/echo/claim | implement-in-this-todo | DOD02..06/VAL02 |
| browser real BFF | web e2e/channel-transport.spec.ts | all | disponibilidade/envio/erro/rascunho/freshness | implement-in-this-todo | DOD03/04/06/VAL03 |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)
- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** findings_integrated
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-channel-abstraction-20261020/architecture-opinion.md; parecer tático terminal no-go inicial, AR01..04 e obrigações integrados pelo owner antes da crítica; sem claim de implementação.
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** findings_integrated
- **Adherence review evidence / resolution:** artifacts/reviews/leadshug-channel-abstraction-20261020/implementation-round-1/2/3-resolution.md; roundsfresh terminal/strictmerged. R01/R03/R04/R05 corrigidas no snapshot revisado; ST06-R02 permanece bloqueador até correção/evidência independente do harness.
- **No-go handling:** reconvergir contrato, sem waiver automático.

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Why this decision:** publicar autoridade do contrato antes de review/guard.
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** a35f676c696e21ec8b4e8ed5cbe6eafbe8da482c
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** contrato publicado antes dos reviews/guardas; somente freeze metadata factual acrescentada depois.
- **Evidence / reference:** origin/maina35f676c696e21ec8b4e8ed5cbe6eafbe8da482c push terminal0 em2026-10-20; CR01/02 integrados antes de reconvergência do reviewer.
- **Waiver authority / reference (required if waived):** n/a

## Gate: Review Scope Drift
- **Gate decision:** required
- **Why this decision:** aprovação usa o pacote efetivamente revisado.
- **Trigger stage:** after the planning-side review/guard cycle converges and before APROVADO
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Material sections compared:** Context|Scope|Out of Scope|Definition of Done|Validation Steps|Decisions|Decision Baseline|Assumptions Preview|Execution Plan|Security Risk Assessment|Performance & Concurrency Risk Assessment
- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **No-go handling rule:** reconvergir review/freeze, sem código.
- **Gate status:** no_material_findings
- **Findings summary:** guard go;23 seções materiais comparadas,0 alterações frente a baselinea35f676c publicada/revisada.
- **Evidence / reference:** foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/review-scope-drift.json
- **Waiver authority / reference (required if waived):** n/a

## Questions To Close
Nenhuma decisão funcional de produto aberta; D01..10 cobrem limites para challenge independente. Readiness real não é aprovação de escopo.

## Pattern References (Optional; Enforced When Cited)
n/a; decisões/canon citados diretamente, sem ID de catálogo presumido.

## Assumptions Preview (Required Before Plan Review)
| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | dois senders comuns escolhem diretamente Meta/Evolution. | api-app/src/domain/inbox/conversations.service.ts; api-app/src/domain/inbox/incoming.service.ts | ampliar inventário/reconvergir | High | Keep as Assumption |
| A-02 | credential resolver não verifica actor grant e não retorna active version. | api-app/src/domain/channels/channel-credential-resolver.ts | reutilizar mecanismo real, sem duplicação | High | Keep as Assumption |
| A-03 | aceitação é owner único keyed e faz fence de identidade. | api-app/src/domain/inbox/message-acceptance.service.ts | corrigir boundary antes de cutover | High | Keep as Assumption |
| A-04 | BFF/API pública respondem pelo ConversationsService; compose DI repetida. | api-app/src/surfaces/bff/conversations.controller.ts; api-app/src/surfaces/public/conversations.controller.ts; api-app/src/surfaces/bff/bff.module.ts | adaptar todos consumers legítimos | High | Keep as Assumption |
| A-05 | browser usa backend real/build e runner faz find amplo. | web-app/playwright.config.ts; scripts/test-channels-local.sh | readiness antes de teste | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)
### Touched Surfaces
Somente Diff Expectation Contract; nenhuma superfície privada/produto modificada durante preparação.

### Ordered Steps
1. APROVADO específico, reload binding e authority/routing go, executor único no checkout principal. Corrigir runner para inventário positivo ANTES de qualquer teste, inclusive RED; não executar find antigo.
2. Test-first: harness dependências com negativa sintética, contrato Channel/fake opaco, raw HTTP/resultados/scopes/seleção. PG barriers/readbacks próprios; contexto muda antes do diagnóstico null-ID e durante seu fence vs falha ordinária/commit incerto:409/503/outcome/metadados, um POST e nenhum replay.
3. Ports/concretos/registro/binding privado com credencial owner existente; revalidar contexto e classificar outcomes, sem duplicar aceitação.
4. Orquestração/cutover BFF/Public/Typebot, política/projeção/DTO e UI indisponível/unknown; retirar dispatch antigo e adaptar fakes/DI de suites existentes.
5. CI-equivalent all completo em recursos descartáveis, Playwright real/fonte-servido e pcv. Não testar ambiente humano por conveniência.
6. DevOps revalida runtime/túnel e publica API/Web locais do código aprovado, conservando banco/canais; operador valida INOUT dos dois vínculos próprios. Nenhuma rotação/repareamento automático.
7. Adherence/cutover/security/TQA/final/debt/diff/authority/completion/closeout, módulos e handoff05/04; nenhum push/deploy de produto automático.

### Test Strategy
- **Strategy:** test-first
- **Why:** cutover de side effects externos/auth e substituição real.
- **Fail-first target(s) (when required):** dependency guard, fake opaco, raw unknown, owner/contexto e política seleção/claim.

### Pre-APROVADO RED Evidence Capture (Optional for bugfix/regression)
- **Decision (`required|recommended|not_needed|waived`):** not_needed
- **Why now:** direção nova com diagnóstico por fonte suficiente; sem execução para congelar hipótese.
- **Target symptom:** n/a
- **Allowed surfaces:** none
- **Forbidden surfaces reaffirmed:** production code|runtime/config/deploy|canonical project docs outside TODO authoring
- **Planned command / target:** n/a
- **Status (`not_run|running|red_reproduced|red_not_reproduced|blocked|waived`):** not_run
- **Findings summary:** nenhuma execução de produto/testes atual.

### Flow Evidence Planning Matrix (Required Before `APROVADO`)
| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOD01/02 substituição/scope | refactor/auth/context | web-only | API PG + browser mutation | yes | yes | channel-transport.e2e/spec e shared contracts | n/a |
| DOD03/04 disponibilidade/outcome | DTO/composer/persistência | web-only | Playwright mutation | yes | yes | e2e/channel-transport.spec.ts com BFF real | n/a |
| DOD05/06 + VAL01/02/03 | aceitação/claim/echo/cutover | web-only | PG barriers + browser mutation | yes | yes | suites completas e served freshness | n/a |
| DOD07/VAL04 | recursos verdadeiros | web-only | operador local | yes | yes | receipt redigido de INOUT dos dois vínculos | fake não substitui |
| DOD08/VAL05 | consolidação/qualidade | web-only | audits + provas anteriores | yes | yes | pacote/guards por critério | n/a |

### Local CI-Equivalent Suite Matrix (Required Before `APROVADO` and Before Delivery Claim)
Colunas Status duplicadas projetam o mesmo fato para leitores determinísticos de índices distintos; evidence inclui ressalvas.

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status (completion projection) | Evidence Artifact / Command | Status (authority projection) | Notes | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| api / all PG/units/contracts | cutover/DI/auth/HTTP | bash scripts/test-channels-local.sh all | Local-Implemented | planned | npm ci/lint/build/unit/E2E completos + migration deploy/status de baseline | planned | subset só diagnóstico | Channel contract/opaque fake/unknown/scope/current identity/echo/claim | Node22/PG16 próprios; dois tenants/BUs; api-key e actor humano/bot; lease barriers/provider controlado |
| web / all build/unit/browser | DTO/composer/erro | bash scripts/test-channels-local.sh all | Local-Implemented | planned | spec channel-transport e regressões completas, BFF não mockado | planned | mesmo all | positivo ambos, canal ausente/ambíguo, draft unknown e contexto atrasado | Web4173/API3100/provider3101, mesma DB/resolução da CI, bundle fresco |
| root / runner topology | positive inventory | bash scripts/test-channels-local.sh all | Local-Implemented | planned | manifests/masks fictícios; nenhuma leitura dotenv/.local-files | planned | sem namespace humano | safe mount/config e origem da principal | leadshug_channels_validation inexistente antes do run, dados descartáveis |

### Runtime / Rollout Notes
Sem migration nova/schema/enum. Migrations existentes deploy/status em PG descartável fazem parte de all. Namespace validation exclusivo, bundles/builds da principal. Runtime humano somente publicação local planejada e prova assistida depois de readiness; banco/canais preservados, sem reset ou rotação. Nenhum transporte real futuro ou status externo de entrega presumido.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)
### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

Revisão de planejamento concluída: architecture_opinion findings_integrated e crítica fresh terminal go. Checkboxes representam análise do plano, não execução/testes/medição do produto. PLAN01/02 opçãoA adotada; AR01..04/CR01..02 resolvidos nos relatórios.

### Issue Cards
- **Issue ID:** PLAN-01
  - **Severity:** high
  - **Evidence:** conversations.service.ts:300; incoming.service.ts:94; resolver:24 não autoriza ator.
  - **Why it matters now:** falsa abstração ou singleton de token mantém acoplamento/vaza escopo.
  - **Option A (Recommended):** ports de domínio, contexto por operação, registro explícito e auth trusted-scoped.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** cross-module; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** wrapper com switch no próprio consumer e config global.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** manter providers atuais; **Effort:** low; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** regresses.
  - **Recommendation:** A; direção humana expressa e menor mecanismo fiel ao escopo.
- **Issue ID:** PLAN-02
  - **Severity:** high
  - **Evidence:** clients atuais string/null e generic errors, fallback canais[0].
  - **Why it matters now:** contrato de substituição precisa outcomes e política verdadeiros, não apenas nomes iguais.
  - **Option A (Recommended):** D03..07 com UNKNOWN conservador, projeção compatível e seleção explícita.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** cross-stack; **Maintenance burden:** medium; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** ocultar falhas como recusa e trocar canal para enviar.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-stack; **Maintenance burden:** high; **Performance impact:** regresses; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** adiar o cutover; **Effort:** low; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** A; sem plataforma de operação durável antecipada.

### Failure Modes & Edge Cases
- [ ] BUs concorrentes, actor sem grant, bot de tenant alheio, owner de canal divergente e stale epoch/version.
- [ ] selected channel removido, dois vínculos sem última origem, leitura segura sem envio habilitado e draft preservado.
- [ ] POST efeito seguido de timeout/5xx/malformed, ID ausente e receipt tardio após rotação/retirada.
- [ ] eco antes/depois do sender; público vs claim humano/overlap BFF; Typebot retido enquanto outra origem chega, janela expira ou contexto muda; empate de createdAt entre transportes.
- [ ] falha antes de acceptance, commit incerto, Message commit seguido de erro na finalização e diagnóstico null-ID sem commit: projeções D03/05, sem replay.
- [ ] UI troca A→B→A durante erro/envio; nenhum retry ou limpeza de draft de outra conversa.

### Residual Unknowns / Risks
- [ ] Cutover sem intent durável conserva limite de crash antes da aceitação/publicação e diagnósticos null-ID sem dedupe; ST-CON-04 deve reconvergir esse limite, não inferir exactly-once.
- [ ] Port extensível não significa persistência/contato/ingress de rede nova pronto; fake só prova substituição interna.
- [ ] Readiness real e medições só depois de aprovação; coorte privada continua, sem produção/usuário não confiável liberado.
- [ ] Arquitetura integrada e crítica fresh reconvergida go no pacote v1.2; guardas finais de planejamento abaixo, toda prova de produto permanece planned.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)
- **Needed:** no
- **Why ambiguity remains:** diagnóstico teve parecer independente de enquadramento; agora gate architecture_opinion desafia D01..10, sem tratá-lo como duplicado satisfeito.
- **Opinion count:** 1 framing advisory,1 tactical terminal com achados integrados
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required na gate tática
- **Required lenses:** correctness,performance,elegance,structural-soundness,operational-fit

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)
- **Canonical method:** wf-docker-audit-escalation-method
- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/audit-floor.json; go/fa884bf1d2e7

| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | cutover completo do envio comum |
| blast_radius | cross-stack | API/Web/runner |
| behavioral_change_or_bugfix | yes | política/erros/claim explícitos |
| changes_public_contract | yes | campos aditivos/erro honesto |
| touches_auth_or_tenant | yes | resolver e contexto |
| touches_runtime_or_infra | yes | runner/publicação local |
| touches_tests | yes | harness/suites |
| critical_user_journey | yes | respostas reais |
| release_or_promotion_critical | no | só local |
| high_severity_plan_review_issue | yes | PLAN01/02 |
| explicit_three_lane_request | no | floor derivado |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)
- **Critique decision:** required
- **Why this decision:** big/cross-stack/auth/side effect e cutover arquitetural.
- **Impact signals in scope:** public contract/schema/api|auth|runtime
- **Package mode:** bounded-file-set
- **Package minimum contents:** TODO publicado, fontes públicas exatas, parecer/disposição e matrizes/risco.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required, não executor; aguardar terminal sem prazo rígido.
- **Critique lenses:** correctness,performance,elegance,structural-soundness,risk
- **Critique status:** no_material_findings
- **Findings summary:** CR01/02 integrados; reconvergência terminal go no contrato completo v1.2/baselinea35f676c, nenhum achado material aberto. Parecer no-go original preservado no ledger.
- **Resolution ledger:** artifacts/reviews/leadshug-channel-abstraction-20261020/critique.md
- **Evidence / reference:** artifacts/reviews/leadshug-channel-abstraction-20261020/critique.md; fresh /root/stcon06_critique gpt-6.1-sol/max, inicial81d56f5e + reconvergência terminala35f676c.
- **Waiver authority / reference (required if waived):** n/a

## Gate: Assumption Code Coherence
- **Gate decision:** required
- **Why this decision:** premissas concretas de senders/resolver/aceitação/runtime.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A01..05
- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
- **Gate status:** no_material_findings
- **Findings summary:** revisão semântica A01..05 ancorada em fonte pública e conferida por arquitetura/crítica; adequações são trabalho explícito, sem fingir garantias atuais.
- **Evidence / reference:** foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/source-assumptions.json; architecture-opinion.md; critique.md; evidence/assumption-coherence.json, guard go/5 premissas.
- **Waiver authority / reference (required if waived):** n/a

## Approval
- **Approved by:** usuário — autoridade humana deste contrato
- **Approval reference:** resposta literal APROVADO nesta conversa em2026-10-20, após apresentação do contrato v1.2 publicado em Foundation781ea16e51e0db2a654e6956ea633a03dd509dfd (freeze materiala35f676c).
- **Approval scope:** ST-CON-06/SCOPE01..05/D01..10, depois da convergência do pacote concreto; concordância com conceito não substitui APROVADO.
- **Execution not authorized by approval:** todo Out of Scope, redes futuras,05/04, push/deploy de produto ou mudanças privadas.
- **Renewed approval required when:** decisões/DoD/paths/risco/contrato mudarem materialmente.
- **Pre-approval readiness evidence:** artifacts/reviews/leadshug-channel-abstraction-20261020/README.md; authority-preapproval.json = preflight-go, execution_authority_granted=false; estrutura PASS. APROVADO específico recebido; authority normal pós-ingestão registrado em evidence/authority-execution.json.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)
Binding reload realizado após APROVADO em2026-10-20 pelo orquestrador: fontes da tabela relidas; constituição/política/módulos recarregados e verify_context PACED-Ready. Executor relerá as regras técnicas pertinentes antes dos edits. Ingestão não é evidência de implementação/testes. Nenhum GOAL persistente foi criado.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | autoridade e roteamento | executor único | código no planejamento | handoff após aprovação |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | aprovação | freeze/reviews/APROVADO | concordância genérica como execução | authority pré/post |
| delphi-ai/workflows/docker/effort-selection-method.md | routing | agent_role_routing_guard.py | fingir modelo primário | guard antes da lane |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | BFF/domínio | adapters finos | regra no controller | contratos E2E |
| delphi-ai/workflows/react/change-ui-boundary-method.md | formulário/estado | freshness/draft | resposta atrasada | Playwright mutation |
| delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | schema | migration versionada | reset operacional | deploy/status descartável |
| delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | intenção/locks | unique/CAS | HTTP em tx | barriers reais |
| foundation_documentation/project_constitution.md | multi-tenant | BU/Contato | credencial global | testes scoped |
| foundation_documentation/policies/scope_subscope_governance.md | rotas existentes | BFF sessão | endpoint fora do owner | contrato explícito |
| delphi-ai/workflows/docker/performance-concurrency-validation-method.md | pcv-1 | quatro lanes | prose sem artefato | JSON/hash antes entrega |

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)
- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Subagent / delegation authorization:** AGENTS/main instructions/workflows exigem reviews internos e executor; código só após APROVADO.
- **Execution topology:** primary-checkout-single-writer
- **Worktree / auxiliary-checkout authorization:** not-authorized
- **Worktree authorization evidence:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

Reviewers architecture_opinion e critique: gpt-6.1-sol/max, fresh fork_turns none, routing go distinto antes de dispatch. Primário não se declara outro modelo. Nenhum GOAL persistente criado sem pedido humano.

## Decision Adherence Validation (Mandatory Before Delivery)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Pipeline/Copilot P1/P2 Preflight
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Rule-Spirit Anti-Pattern Hunt
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

Terminal architecture/security findings classified by review-finding-classification. All current-slice findings remain blockers until fixed and evidenced; no waiver/debt accepted. Exact text and deduplication: artifacts/reviews/leadshug-channel-abstraction-20261020/implementation-round-1-resolution.md.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| ST06-R01 (ADH-01=SEC-01) | high | release-blocker | same-todo | Original non-first/malformed-ID counterexample corrected; new flag case tracked R05 | resolved in round2 snapshot; finalvalidation pending | implementation-round-1-resolution.md; existing D04 approval |
| ST06-R02 (ADH-02) | medium | release-blocker | same-todo | Navigation corrected; await body/handler completion and prove same-text draft fence catches removal | fixed/evidenced; all80903 and independentTQA pending | implementation-round-3-resolution.md; existing D10 approval |
| ST06-R03 (SEC-02) | medium | release-blocker | same-todo | D04/05 Evolution empty object is not ACK; key:{} preserved | resolved in round2 snapshot; finalvalidation pending | implementation-round-1-resolution.md; existing D04/05 approval |
| ST06-R04 (SEC-03) | medium | release-blocker | same-todo | Denied mutations/twoTENANT proof added; preDispatch must exercise real Meta/Evo adapters and detect omitted callback | resolved reviewed snapshot; final assurance pending | implementation-round-3-resolution.md; existing scope/validation approval |
| ST06-R05 (adherence-round2 ADH-R2-01) | medium | release-blocker | same-todo | D04 explicit false/malformed success flag contradicts positive ACK; UNKNOWN/no authoritative write | resolved reviewed snapshot; final assurance pending | implementation-round-3-resolution.md; D04 existing approval |


## TODO Closeout Disposition
- **Disposition:** keep-active
- **Disposition reason:** contrato aprovado, implementação e validação em execução; não encerrar antes de todos gates.
- **Post-commit/push status:** baseline materiala35f676c publicada/revisada; pacote documental finalizado com guardas pré-aprovação; produto Pending.
- **Next path/status action:** executar ST-CON-06 aprovado, manter active até evidências e gates de entrega.

## Security Risk Assessment (Mandatory Before Delivery)
- **Risk level:** high
- **Why this risk level:** canal/credencial de múltiplos tenants e side effect externo.
- **Attack surface in scope:** sessão/key/bot, BU/channel/contexto, singleton/mapping forjado, rawerro/token, adapter recipient/URL e DI.
- **Attack simulation decision:** required
- **Review evidence:** planned após implementação, com actor sem grant/BU alheia/ingress falso/version stale e concorrência.
- **Residual security risk:** coorte privada atual preservada; nenhum usuário não confiável ou produção autorizado.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)
- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** cutover de envio/identidade/aceitação/DI com concorrência real.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | pending | none | none |
| FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | pending | none | none |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-E3 | pending | external ambiguity explicit | none |
| RLS | runtime-load-stress-validation | recommended | medium | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E1 | pending | none | none |

### Lane Detail Packet Template
#### EPS
- **Trigger rationale:** medir seleção/resolução scoped e projections de disponibilidade; EXPLAIN ANALYZE e cardinalidade representativa. Nenhuma chamada externa nova em GET e um POST por dispatch.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
- **Evidence object:** pending; JSON pcv-1 com sha256 antes da entrega, não existe execução ainda.
#### FRC
- **Trigger rationale:** envio/erro e troca BU/conversa; draft, requests e readback BFF real.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### BCI
- **Trigger rationale:** barreiras PG/contador HTTP de BUs/credencial/identidade/claim/eco; provar D02..07 e ausência de retry. Crash recovery durável novo não é contratado.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
- **Evidence object:** pending; JSON pcv-1 com sha256.
#### RLS
- **Trigger rationale:** ensaio bounded de concorrência no envio fake/PG, sem claim SLO/produção.
- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
- **Executor ID:** planned-executor-st-con-06
- **Evidence object:** pending; resolver recomendação com evidência ou waiver válido até o deadline, sem deixar pendente na entrega.

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)
- **Audit outcome:** high
- **Why this outcome:** não implementado; toda evidência de produto pendente, sem claim de entrega.
- **Inline code TODO debt:** none
- **Evidence / audit artifact:** planned após implementação
- **Accepted residual debt:** none; dependência externa não é waiver.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)
- **Audit decision:** required
- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
- **Required evidence matrix (when architectural):** unit|integration|web real-backend
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
- **Canonical method:** wf-docker-independent-test-quality-audit-method
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/session.json; round01 active
- **Audit status:** running
- **Findings summary:** none; nenhuma auditoria de entrega executada
- **Evidence / reference:** planned após implementação
- **Waiver authority / reference (required if waived):** n/a

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)
- **Final review decision:** required
- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
- **Required evidence matrix (when architectural):** unit|integration|web real-backend
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
- **Canonical method:** wf-docker-independent-final-review-method
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Audit session / round evidence (when protocol used):** planned após implementação
- **Final review status:** not_run
- **Findings summary:** none; nenhuma auditoria de entrega executada
- **Evidence / reference:** planned após implementação
- **Waiver authority / reference (required if waived):** n/a

## Independent Cutover Integrity Audit Gate
- **Cutover audit decision:** required
- **Why this decision:** migra todos senders comuns para owner/port canônicos e elimina dispatch antigo, mantendo protocolos legítimos separados.
- **Cutover signals in scope:** intentional canonical boundary change|shared dispatch replacement
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** audit-protocol-triple-review
- **Cutover audit status:** running
- **Findings summary:** planned after implementation
- **Evidence / reference:** harness D09 e módulos/sources consolidados, sem shim temporário
- **Waiver authority / reference (required if waived):** n/a

## Delivery Confidence Gate (Required for `✅ Production-Ready`)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Module Consolidation Gate (Required Before `Completed`)
Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.

## Commands (Run Locally)
Guardas de planejamento após freeze. Produto somente após APROVADO: bash scripts/test-channels-local.sh all, depois do boundary positivo. Nenhum teste/runtime/account call nesta preparação.

## Files Expected (Compatibility Note)
Diff Expectation Contract governa os paths, sem autorização de mudanças além dele.

## COMENTÁRIO:
Nenhuma pergunta de produto material pendente.


## Producer / Consumer Contract Matrix

| Producer | Consumers | Auth / fields | Planned effect / constraint |
| --- | --- | --- | --- |
| Channel.sendMessage internal | OutboundService | opaque recipientRef/text; operation-bound implementation, no raw token | normalized result D04; one external POST, no retry, no DB message write by adapter |
| ChannelResolver internal | OutboundService/policy | trusted reference derived from authorized session/API-key conversation or verified bot ingress; owner DB rechecked | Channel plus safe storage-provenance binding; no caller provider selection/secret |
| GET /api/bff/conversations/:id/messages | Inbox | existing session/BU lookup, timeline fields unchanged; janela adds disponivel/motivo | observational availability, no external calls/secret decrypt; unavailable composer with fixed reason |
| POST /api/bff/conversations/:id/messages | Inbox | existing session/CSRF/ATENDENTE+ and {texto}; success201 existing {id,canal,em} | shared outbound; D05 errors additive outcome, honest text; preserve draft and no auto resend |
| GET /api/v1/conversations | public API clients | existing partner key scope; existing fields, adds envio_disponivel/motivo_indisponibilidade | existing window values remain, unavailable selection returns false/null rather than failing whole list |
| GET /api/v1/conversations/:telefone/messages | public API client | existing partner key/BU and phone conversation lookup; timeline/window fields unchanged | disponibilidade aditiva como listagem, sem provider GET/segredo |
| POST /api/v1/messages | public API client | existing API key/account_id, telefone/texto/atendente and rate limit | request shape/success unchanged; same shared outbound, source authorization and EXTERNO authorship; D05 error mapping |
| IncomingService Typebot text response | existing bot sessions | accepted ingress exact channel/identity/tenant, no fabricated human user | same shared outbound/window/result/acceptance; preserve queue/status/human owner, stop on unknown/block/refusal, no replay |

**Fixed availability reasons:** CANAL_AUSENTE, CANAL_AMBIGUO, CANAL_SELECIONADO_INDISPONIVEL, CHANNEL_IDENTITY_NOT_VERIFIED, CHANNEL_NOT_READY, PENDING_CREDENTIAL, JANELA_FECHADA; null when observed available. Availability never grants authority or guarantees external delivery. Existing input limit4096/request phone normalization stays at current product boundaries; the Channel port has no universal WhatsApp address requirement. No new public route or channel choice field is introduced in06.

## Planning references / provenance

Direction and extension requirements are explicit user statements2026-10-20. Initial framing opinion is artifacts/analysis/leadshug-channel-abstraction-framing-opinion-20261020.md (advisory only). Primary conceptual sources: NestJS custom providers https://docs.nestjs.com/fundamentals/custom-providers and Liskov/Wing1994 https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf, previously consulted. Provider error source consulted by owner (bounded public reference; reviewer independently hit429): https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes/. Local code proves current behavior, not future platform integration or live readiness.

## Execution Checkpoints

| Checkpoint | State | Evidence / limit |
| --- | --- | --- |
| CP01 — runner antes de testes | passed precondition | artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/runner-checkpoint.json; allowlist antes de stat, sem varredura ampla; bash-n/diffcheck/mock config-only. Nenhum teste de produto ou Docker real executado neste checkpoint. |
| CP02 — Channel/outbound/consumers + Web/tests | implementation, not delivered | Executor único; artifacts/tmp/stcon06-executor-* e evidence/executor-validation.json reservados. Initial RED dependencyguard175pass/1fail. all33610 terminal0:194unit/308PG/29Web/50browser, snapshot anterior agora insuficiente pelas findings round2. |
| CP03 — independent adherence/security rounds1/2/3 | terminal; R02 protection gap open | R01/R03/R04/R05 corrected in reviewed snapshot; shippingadapter omission mutants fail409vs201 then exactrestored. R02 needs causal response.text/handler barrier. Full implementation-round-1/2/3-resolution.md; no waiver/debt or physicalproof. |
| CP04 — actual R05 regression RED | reproduced before fix | Canonical API49493 terminal1: Meta200 success:false+ID expectedUNKNOWN/TRANSPORT_UNCONFIRMED, actualACCEPTED;20otherunitfiles green. Executor will preserve exact log/provenance and correct source after terminal. Not blanket RED for other cases. |

## Supplemental Expected-Path Validation — 2026-10-20

User explicitly replied **“Validar os dois arquivos de apoio”** to the exact bounded proposal [test-companion-path-admission.md](../../../artifacts/reviews/leadshug-channel-abstraction-20261020/test-companion-path-admission.md). This validates only Web `src/api.spec.ts` and `e2e/timeline-freshness.ts` as M companions for D10/SCOPE05. Scope, DoD, public behavior, frozen D01..10, private-data prohibition and required checks are unchanged. The direct client test was already added before the path omission was noticed; its admission is explicit here. The nested helper correction was not applied or run before this validation. Executor remains sole product writer; browser/all may proceed only after both freshness inventories use positive pathspecs before discovery.

## Implementation Assurance — Round 1

Architecture adherence and separate security reviews completed through canonical subagent_review_run.py, gpt-6.1-sol/xhigh, closed embedded source packages; strict merge passed. Architecture: changes required; security: source-only classification defects and evidence gaps, no demonstrated tenant breakout or credential disclosure. Artifacts: evidence/adherence.raw.json, adherence.merge.json; security.raw.json, security.merge.json. Reviews did not certify final all or physical proof. No live review was cancelled or repackaged. All findings integrated as approved-contract remediation, with delivery still Pending.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ADH-01 | Integrated | useful | yes | project | n/a | ST06-R01; D04 complete-envelope classification, remediation open |
| SEC-01 | Integrated | useful | yes | project | n/a | duplicate ADH-01 consolidated ST06-R01; same open blocker, not ignored |
| ADH-02 | Integrated | useful | partial | project | n/a | ST06-R02; independently confirms browser navigation defect, remediation open |
| SEC-02 | Integrated | useful | yes | project | n/a | ST06-R03; supported ACK structure vs malformed empty object, remediation open |
| SEC-03 | Integrated | useful | yes | project | n/a | ST06-R04; reconcile source/proofs and add only missing local negative/isolation cases |


## Implementation Assurance — Round 2

Both canonical CLI reviews terminal0, strict merge passed: evidence/adherence-round2.raw.json and security-round2.raw.json. Full adjudication and exact overlapping ID bindings: implementation-round-2-resolution.md. Original R01/R03 counterexamples resolved at source; R02/R04 protection gaps remain and R05 is a new classifier case. No architecture expansion, waiver/debt or delivery claim. Runner33610 must terminate before further product edits.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| adherence-round2:ADH-R2-01 | Integrated | useful | yes | project | n/a | ST06-R05 Meta success:false contradiction; approved D04 remediation open |
| adherence-round2:ADH-R2-02 | Integrated | useful | partial | project | n/a | ST06-R02 headers-only wait can falsely pass before stale completion |
| adherence-round2:ADH-R2-03 | Integrated | useful | yes | project | n/a | ST06-R04 testfake owns guard, must exercise shipping adapter callback |
| security-round2:ADH-R2-01 | Integrated | useful | yes | project | n/a | duplicate ST06-R04, same shipping-adapter harness gap |
| security-round2:ADH-R2-02 | Integrated | useful | partial | project | n/a | duplicate ST06-R02, same browser completion gap |

## Review round3 findings resolution

| Finding ID | Disposition | Usefulness | Formalizable | Candidate Rule Level | Rule Update | Evidence / limit |
| --- | --- | --- | --- | --- | --- | --- |
| adherence-round3:ADH-R3-01 | Integrated | useful | partial | project | n/a | ST06-R02; test-only native body-read task barrier, mutation proof and revised canonical validation pending |
| security-round3:ST06-R02 | Integrated | useful | partial | project | n/a | same ST06-R02; no demonstrated production vulnerability, D10 protection gap retained blocking |

## CP05 — causal browser protection proof

Corrected test b3604496…8e0f3 observes native text-read settlement and a following browser task before assertions. Diagnostic63018 passed50/50. Actual guard-replacement mutant30246 failed only the intended same-text draft assertion after body counts1/1/1;49other browser cases passed. Full captured log/root source/restoration/served-bundle provenance: artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/browser-causal-*.json. Source restoration is byte-exact. Failed64345 ordering attempt and63018 diagnostic are not mislabeled as mutation proof. Canonical finalall80903 remains running; no Local-Implemented or physical-channel delivery claim.

## CP06 — final automated validation and dedicated audit dispatch

Canonical all80903 terminal0:194APIunit/309realPG/29Webunit/50browser. Root verified unchanged product/runner bytes against causal-final-source-before-all80903.json and36changedpublicsource manifest hashes plus served/dist/preserved bundle27c5db46. Full log SHA778f858923f4df7457d32908a98dfda31d0b4351579acabdc1fb90515bec8554. Dedicated Performance(gpt-6.1-sol/xhigh), TQA and Cutover(both gpt-5.6-terra/xhigh per normalrouting) freshly dispatched with complete bounded package and mandatory consumer/fullTQAworkload; no audit result presumed. Runtime/source commit/push/deploy remains untouched except Foundation main documents.


## Exact authority / source .github/workflows/ci.yml

name: Verify workspace

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  compose:
    name: Validate Compose
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate the runtime topology
        env:
          SESSION_SECRET: ci-session-secret
          INTERNAL_SERVICE_TOKEN: ci-internal-token
          WHATSAPP_TOKEN: ci-whatsapp-token
        run: docker compose config --quiet

  api:
    name: API
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Checkout the private API submodule
        env:
          SUBMODULES_REPO_TOKEN: ${{ secrets.SUBMODULES_REPO_TOKEN }}
        run: |
          test -n "$SUBMODULES_REPO_TOKEN" || {
            echo "SUBMODULES_REPO_TOKEN must read the private LeadsHug submodules." >&2
            exit 1
          }
          git config --global url."https://x-access-token:${SUBMODULES_REPO_TOKEN}@github.com/".insteadOf "https://github.com/"
          git submodule sync -- api-app
          git submodule update --init --depth=1 api-app
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: api-app/package-lock.json
      - name: Install, lint, build, and test API
        working-directory: api-app
        run: |
          npm ci
          npm run lint
          npm run build
          npm test

  web:
    name: Web
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Checkout the private Web submodule
        env:
          SUBMODULES_REPO_TOKEN: ${{ secrets.SUBMODULES_REPO_TOKEN }}
        run: |
          test -n "$SUBMODULES_REPO_TOKEN" || {
            echo "SUBMODULES_REPO_TOKEN must read the private LeadsHug submodules." >&2
            exit 1
          }
          git config --global url."https://x-access-token:${SUBMODULES_REPO_TOKEN}@github.com/".insteadOf "https://github.com/"
          git submodule sync -- web-app
          git submodule update --init --depth=1 web-app
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: web-app/package-lock.json
      - name: Install, build, and test Web
        working-directory: web-app
        run: |
          npm ci
          npm run build
          npm test


## Raw independentfinding test-quality.raw.json

```
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/round-01/dispatch/test-quality.dispatch.json","review_kind":"test_quality_audit","reviewer_label":"fresh-no-context-test-quality-reviewer","overall_assessment":"Changes required. The changed tests substantively cover the approved behavior: real PostgreSQL/BFF/browser paths, raw adapter contracts, negative mutation controls, and the repaired causal stale-response assertion are effective and not pass-the-test shortcuts. However, the required real-PG and browser regression gates are not executed by CI; the successful local canonical run does not establish CI execution.","recommended_path":"Keep the current local canonical evidence, but add CI execution of the canonical all gate or an equivalent isolated real-PG and freshly built-browser workflow. If that cannot be authorized, obtain an explicit human waiver before treating the required TQA gate as satisfied.","performance_position":"acceptable","elegance_position":"acceptable","structural_soundness_position":"acceptable","operational_fit_position":"mixed","findings":[{"finding_id":"TQA-01","severity":"high","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","title":"Required integration and browser regression gates are absent from CI execution","rationale":"The CI workflow runs API lint/build/unit tests and Web build/unit tests only; it does not run API E2E against PostgreSQL or Playwright. The command-parity evidence explicitly confirms that no root CI PG-E2E or Playwright job is asserted. The new critical protections—including adapter fences, cross-tenant mutation checks, and the causally synchronized A→B→A draft regression—therefore rely solely on the local all80903 run. This leaves future regressions able to merge without executing the tests that substantiate the changed contract.","suggested_action":"Add a project-owned CI job that invokes the canonical all runner or an equivalent isolated Node 22/PostgreSQL/served-bundle Chromium workflow, retaining source and bundle freshness attestation. Do not replace it with mocks or a retry-only gate; if CI expansion is outside authorized scope, record an explicit approval-authority waiver and leave the required audit gate unsatisfied until then.","affected_paths":[".github/workflows/ci.yml","scripts/test-channels-local.sh","web-app/e2e/channel-transport.spec.ts","api-app/test/channel-transport.e2e-spec.ts"]}]}
```


## Raw independentfinding performance.raw.json

```
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/round-01/dispatch/performance.dispatch.json",
  "review_kind": "critique",
  "reviewer_label": "fresh-internal-performance-critique-reviewer",
  "overall_assessment": "Changes required for one concrete query-work bound. Architecture and structural soundness otherwise follow D01..10: operation-bound adapters, shared outbound orchestration, separate authentication boundaries and sole keyed MessageAcceptance ownership remain intact. Exact lookups use database predicates; detached identity tombstones do not accumulate in the currentChannelId relation. Sends introduce no provider retries, external probes or HTTP inside transactions. However, the latest-IN projection bounds returned rows without bounding historical rows examined, and unnecessarily evaluates conversations whose selected channel requires no window. Code quality and elegance are acceptable; repeated readiness checks are minor debt. Tests correspond to approved behavior, with no evident pass-the-test workaround, committed bypass or silent real/mock fallback. Real PostgreSQL, production DI and served-browser evidence substantiate their declared boundaries; provider doubles do not establish physical delivery. The supplied R04 adapter omission controls and R02 native-body/task barrier, same-test mutant failure and exact restoration support keeping those historical findings closed. Final all80903 reports 194/309/29/50 passes with source and served-bundle attestations; this reviewer executed nothing. Fail-first history remains limited to the dependency guard and recorded R05 regression; other coverage is test-after. Assertion efficacy is weakened specifically by the all-IN performance fixture and aggregate-only load counts. Command/platform claims are appropriately bounded: local validation exceeds the root CI workflow, and no remote PostgreSQL/browser execution is claimed. Security probes cover denied mutations and concurrent scoped credentials without demonstrating a new vulnerability. Operational fit remains incomplete pending the declared activation, HTTPS, assisted IN/OUT, consolidation and final-review gates.",
  "recommended_path": "Resolve PERF-01 and obtain candidate-bound evidence for OUT-heavy and no-IN histories before accepting the performance lane. Preserve D07's selection, stored-time calculation and expiry fields. If the fix requires an index, obtain renewed approval for that narrow schema-path change rather than silently expanding scope. Address PERF-02 as non-blocking evidence debt. Continue the separately declared delivery gates without reopening resolved findings or claiming capacity certification.",
  "performance_position": "mixed",
  "elegance_position": "acceptable",
  "structural_soundness_position": "acceptable",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "PERF-01",
      "severity": "high",
      "category": "performance",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Latest-IN projection can scan complete histories for every conversation on a public page",
      "rationale": "prisma-channel-resolver.ts:115-118 requests windows for every page ID whenever any BU channel requires a window. At lines 318-329, direction='IN' is a filter beneath LIMIT 1, while schema.prisma:452 supplies only the conversationId/createdAt index. An arbitrarily long recent OUT suffix must therefore be examined to reach an older IN; an OUT-only conversation can require examining its entire history. This also affects selected NAO_OFICIAL conversations that require no window when an official binding exists alongside them. The public page permits up to 500 conversations, multiplying history-dependent database work in one request. The supplied EXPLAIN confirms direction is a filter, and the fixture at number-onboarding-pcv.e2e-spec.ts:113-122 seeds only IN messages, so its fast indexed result does not exercise this counterexample. This is a source-demonstrable unbounded historical scan, not a measured outage or marginal index optimization. D07 preserves temporal semantics and requires batched metadata; it does not expressly waive unbounded scan work. The prohibition on schema changes must still be respected.",
      "suggested_action": "Add deterministic OUT-heavy and no-IN histories and inspect actual rows examined and buffers for the endpoint's queries. Restrict window projection to references whose selected binding requires it, while also resolving the remaining official-history scan. Option A: obtain renewed approval for a narrowly scoped direction-aware ordered or partial index and validate its plan. Option B: demonstrate an equivalent bounded access path using the approved schema without changing expiry semantics. Do nothing retains the blocking runtime risk. Prefer the smallest proven solution; do not silently omit expired timestamps or alter channel selection.",
      "affected_paths": [
        "api-app/src/integrations/channels/prisma-channel-resolver.ts:115",
        "api-app/src/integrations/channels/prisma-channel-resolver.ts:318",
        "api-app/prisma/schema.prisma:452",
        "api-app/test/number-onboarding-pcv.e2e-spec.ts:105"
      ]
    },
    {
      "finding_id": "PERF-02",
      "severity": "low",
      "category": "tests",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Load artifact declares a per-conversation duplicate threshold that the probe does not measure",
      "rationale": "pcv-rls-candidate.json declares duplicate_rows_per_owned_subject=0, but channel-transport.e2e-spec.ts:510-516 checks only 20 successful responses and 20 aggregate OUT rows across 20 conversations. Those totals alone cannot distinguish one conversation missing its row from another containing two. The artifact comparison evaluates only accepted and recorded totals. This is non-blocking evidence precision debt, not a demonstrated persistence defect or a request for same-key external exactly-once guarantees.",
      "suggested_action": "Option A: assert exactly one matching OUT row for each owned conversation and include those observations in the artifact comparison. Option B: narrow the artifact threshold and summary to the aggregate property actually measured, provided the governing acceptance remains satisfied. Do nothing leaves an unsupported threshold claim. Prefer A within the admitted test path.",
      "affected_paths": [
        "api-app/test/channel-transport.e2e-spec.ts:484",
        "foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/pcv-rls-candidate.json"
      ]
    }
  ]
}
```


## Raw independentfinding cutover-integrity.raw.json

```
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/dedicated-audit/round-01/dispatch/cutover-integrity.dispatch.json","review_kind":"cutover_integrity_audit","reviewer_label":"fresh-no-context-cutover-integrity-reviewer","overall_assessment":"Cutover integrity passes. BFF, public API, and Typebot outbound paths converge through the shared OutboundService, resolver, operation-bound Channel port, and sole keyed MessageAcceptanceService writer. Retained provider-specific code is confined to approved protocol/registration clients, registered adapters, and physical storage provenance. No old-dispatch wrapper, dual read/write, silent fallback mirror, pseudo-canonical completion path, or query-time compatibility stitching was found. Pending activation, assisted IN/OUT, PCV adjudication, and final review remain external delivery gates, not cutover defects.","recommended_path":"Retain the canonical cutover design and complete the separately required delivery gates; do not represent this audit as external-runtime certification.","performance_position":"acceptable","elegance_position":"acceptable","structural_soundness_position":"strong_positive","operational_fit_position":"mixed","findings":[]}
```
