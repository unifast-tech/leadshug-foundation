# TODO — Foundation lifecycle structural validator

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` (`ST-01`)
- **Direct-to-TODO rationale:** one bounded Foundation-maintenance slice: replace fragile structural checks with one reusable project-owned validator.
- **Primary profile:** `Strategic / CTO-Tech-Lead`
- **Implementation handoff:** `Operational / Coder`
- **Technical scope:** `docker/Foundation documentary tooling`
- **Code-touch boundary:** `Foundation validator, tests and directly affected canonical Foundation docs only`

## Context

The Foundation lifecycle is already defined by canonical documents, but important structural invariants are protected mainly by long snippets embedded in the completed ST-01 TODO. The project needs a small reusable validator that derives current state from canonical owners and fails clearly when their structure drifts.

This TODO previously expanded into a custom attestation/provenance runner. That design was deliberately retired before approval because its implementation and maintenance cost was disproportionate to a documentation validator.

## Framing Source & Story Slice

- **Program:** `ST-01 — Evolução do foundation_documentation`
- **Story:** establish a deterministic, read-only structural validator for the live Foundation lifecycle.
- **Primary value:** detect broken IDs, tables, references, paths and lifecycle relationships before documentation changes are considered complete.
- **Non-goal:** build CI infrastructure, an execution sandbox, a provenance system or a cryptographic delivery protocol.

## Contract Boundary

The validator checks objective structure only. It does not decide whether a product/architecture decision is good, whether evidence is semantically sufficient, or whether a TODO should be approved.

## Implementation Intent

Create one Python standard-library CLI with a small parser module and focused unittest suite. It reads canonical Foundation files, emits bounded diagnostics, returns nonzero on structural failure and never rewrites input.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Tactical TODO lifecycle state:** `Review`
- **Qualifiers:** `none`
- **Next exact step:** run the remaining pre-approval critique/coherence/scope/authority gates and request `APROVADO` before implementation.

## Active Work State

- **Work state:** `review`
- **Why this state now:** the user-validated simplified contract is frozen and its architecture opinion converged; the remaining pre-approval gates are in progress.
- **Exit condition:** simplified decisions validated/frozen, pre-approval gates green, explicit `APROVADO`, implementation/evidence complete, and TODO promoted to `completed/`.

## Trigger Evidence

- Completed ST-01 established canonical lifecycle owners and exact structural checks.
- The current check surface is difficult to reuse because it is embedded in a completed TODO.
- No production runtime, API, UI, database or deployment behavior is involved.

## Scope

- [ ] `S-01` Implement `deterministic/validate_foundation_lifecycle.py` as a read-only Python standard-library CLI.
- [ ] `S-02` Implement bounded structural parsing in `deterministic/foundation_lifecycle/parser.py`.
- [ ] `S-03` Validate live backlog, decision index/records, lifecycle schemas and roadmap gate-evidence structure.
- [ ] `S-04` Enforce ID uniqueness, required headings/tables, exact columns, allowed states, reference resolution and root confinement.
- [ ] `S-05` Preserve the historical-document exception: only admitted live owners are scanned as authorities.
- [ ] `S-06` Add independent positive and mutation tests using temporary fixtures.
- [ ] `S-07` Document the CLI, structural boundary, exit behavior and canonical owners.
- [ ] `S-08` Align directly affected lifecycle/index/roadmap guidance and retarget the validator-adoption decision at closeout.

## Out of Scope

- `OOS-01` Product code or runtime behavior.
- `OOS-02` CI/CD workflows or mandatory remote automation.
- `OOS-03` Custom subprocess runner, command registry or toolchain provenance.
- `OOS-04` Commit-message envelopes, tree materialization or cryptographic attestation.
- `OOS-05` Sandboxing, process supervision, executable allowlists or Delphi commit pinning.
- `OOS-06` Semantic judgment of decision quality, evidence sufficiency or approval readiness.
- `OOS-07` Retroactive normalization of historical/completed documents outside the live graph.
- `OOS-08` External Markdown-renderer compatibility beyond the narrow declared grammar.

## Execution Lane Tracking

- **Current lane:** `planning/review`
- **Execution authority:** `none`
- **Topology:** `principal checkout, single writer, no worktrees`
- **Implementation owner after approval:** `routine-executor / Operational Coder`
- **Assurance handoff:** `Assurance / Tester-Quality` after implementation.

## Promotion Evidence

- **Branch:** `main`
- **Promotion target:** `foundation_documentation:main`
- **Current claim:** planning only; no implementation claim.

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `.` | `80aaab403d4214262142bda64d63354c229f527a` | `working_tree` |

### Expected Changed Paths

| Repository | Pattern | Change Types | Purpose |
| --- | --- | --- | --- |
| Foundation | `deterministic/validate_foundation_lifecycle.py` | `A/M` | public CLI |
| Foundation | `deterministic/foundation_lifecycle/__init__.py` | `A/M` | package boundary only |
| Foundation | `deterministic/foundation_lifecycle/parser.py` | `A/M` | structural parsing/rules |
| Foundation | `deterministic/tests/test_validate_foundation_lifecycle.py` | `A/M` | CLI/rule tests |
| Foundation | `deterministic/tests/test_foundation_parser.py` | `A/M` | parser mutation tests |
| Foundation | `deterministic/README.md` | `A/M` | usage and boundary |
| Foundation | `evolution_lifecycle.md` | `M` | validator adoption/canonical grammar alignment |
| Foundation | `README.md` | `M` | entrypoint discovery |
| Foundation | `decisions/README.md` | `M` | current decision membership rule if required |
| Foundation | `decisions/ST-01-foundation-lifecycle-decisions.md` | `M` | validator-adoption target/evidence at closeout |
| Foundation | `system_roadmap.md` | `M` | canonical gate-evidence guidance link if required |
| Foundation | `todos/active/process/TODO-foundation-lifecycle-structural-validator.md` | `M/D` | evidence then atomic move |
| Foundation | `todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` | `A` | closeout destination |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `../delphi-ai/**` | `any` | Engineering changes are outside this TODO. |
| Foundation | `.github/**` | `any` | CI integration requires a separate future TODO. |
| Foundation | `modules/**` | `any` | Product-domain modules are outside this validator. |
| Foundation | `contracts/**` | `any` | Product contracts are outside this validator. |
| Foundation | `artifacts/**` | `any` | No persistent analysis or delivery artifact is required. |
| Foundation | `**/attestation.py` | `any` | Attestation infrastructure was deliberately retired. |
| Foundation | `**/runner.py` | `any` | Process-runner infrastructure was deliberately retired. |

### Diff Deviation Analysis

Any unclassified path blocks delivery until classified as scope deviation, necessary need or noise. Necessary scope expansion requires renewed human validation and `APROVADO`.

## Bounded But Elastic Guardrails

- Parser helpers may be reorganized inside the declared package if no new responsibility is introduced.
- A new dependency, CI surface, process runner, canonical owner or expanded historical scan is material scope expansion.
- Diagnostics may improve autonomously if they remain bounded, deterministic and non-sensitive.

## Definition of Done

- [ ] `DOD-01` CLI validates the real live Foundation owner graph and returns zero.
- [ ] `DOD-02` Every structural rule has a positive control and meaningful mutation test.
- [ ] `DOD-03` Input trees remain byte-for-byte unchanged on success and failure.
- [ ] `DOD-04` Minimal bootstrap kernel detects removal/rename of required owners, headings, schemas and enums without copying live records.
- [ ] `DOD-05` Paths/references are root-confined and diagnostics do not echo sensitive content.
- [ ] `DOD-06` README/lifecycle/decision guidance names the validator without duplicating live state.
- [ ] `DOD-07` Legacy ST-01 checks are classified as parity evidence or retired controls, not embedded implementation.
- [ ] `DOD-08` Required audits/reviews and deterministic TODO guards pass before closeout.

## Validation Steps

- [ ] `VAL-01` `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- [ ] `VAL-02` `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'`
- [ ] `VAL-03` Run mutations for IDs, tables, links, paths, observable current-row state/target/evidence, roadmap evidence and read-only behavior.
- [ ] `VAL-04` Run a no-write compile check with `python3 -B` over delivered Python files.
- [ ] `VAL-05` Run compatible ST-01 checks once as migration parity evidence and record retired assertions.
- [ ] `VAL-06` Run `git diff --check`, diff expectation, authority and completion guards at required phases.
- [ ] `VAL-07` Confirm the final diff contains no runner, attestation, registry, subprocess/provenance or CI implementation.

## Completion Evidence Matrix

| Criterion | Required Evidence | Status |
| --- | --- | --- |
| `DOD-01` | real repository CLI output | planned |
| `DOD-02` | unittest output + mutation mapping | planned |
| `DOD-03` | fixture manifest/hash before and after success/failure | planned |
| `DOD-04` | bootstrap deletion/rename mutations | planned |
| `DOD-05` | confinement/redaction mutations | planned |
| `DOD-06` | final documentation diff review | planned |
| `DOD-07` | legacy transition table + parity output | planned |
| `DOD-08` | gate/guard evidence in this TODO | planned |
| `VAL-01..VAL-07` | exact command outputs or criterion-specific evidence | planned |

## External Dependency Readiness

- Python 3 and Git are existing local prerequisites.
- No network, hosted service, external package or sibling-repository runtime dependency is required.
- Delphi guards remain external workflow tools and are not imported or executed by validator code.

## Profile Scope & Handoffs

- **Primary planning profile:** `Strategic / CTO-Tech-Lead`
- **Implementation profile:** `Operational / Coder`
- **Assurance profile:** `Assurance / Tester-Quality`
- **Scope overlay:** `docker/Foundation documentary tooling`

### Handoff Log

| From | To | Purpose | Status |
| --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Operational / Coder | implement bounded validator/tests after approval | planned |
| Operational / Coder | Assurance / Tester-Quality | challenge mutations, false greens and read-only behavior | planned |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** one consolidated plan/critique checkpoint before approval and normal delivery reviews after implementation.
- **Why this level:** several Markdown owners and mutation cases, but no runtime, subprocess, provenance or CI subsystem.

## Canonical Module Anchors

- **Primary canonical anchor:** `foundation_documentation/evolution_lifecycle.md`
- **Secondary anchors:** `foundation_documentation/backlog/README.md`; `foundation_documentation/decisions/README.md`; root-level current decision records; `foundation_documentation/system_roadmap.md`; `foundation_documentation/README.md`
- **Canonical Coverage Status:** `Complete for the touched lifecycle surface`
- **Decision consolidation targets:** `evolution_lifecycle.md`; `decisions/README.md`; `deterministic/README.md`; `README.md`
- **Module docs:** `n/a — no product module behavior changes`

### Validator Source Graph

| Owner | Admitted Surface | Structural Boundary |
| --- | --- | --- |
| `evolution_lifecycle.md` | identifiers and authority/state-machine tables | required headings/schemas/enums and narrow identifier grammar |
| `backlog/README.md` | `## Candidates` table | exact columns, unique `BLG-*`, allowed state, valid links |
| `decisions/README.md` | root-level current-record index/rule | exact index ↔ root `decisions/*.md` membership |
| indexed root decision records | decision tables + one file provenance field | unique `DEC-*`, state and target/evidence shape; successor topology remains review-owned until a canonical field exists |
| `system_roadmap.md` | exclusive owner of roadmap columns, gate states and exit-gate evidence grammar | exact columns/state and structural exit-gate evidence |

### Narrow Markdown Grammar

- UTF-8 strict input; reject hidden format controls in identifiers, states and paths.
- Required headings/tables are unique and use exact declared columns.
- Tables are parsed structurally with bounded inline-code/link awareness; ambiguity fails closed.
- Markdown destinations use relative POSIX syntax only: no scheme/network form, backslash, angle-bracket destination, query or percent encoding; an optional fragment must match `[a-z0-9]+(?:-[a-z0-9]+)*`.
- Links resolve from their source file and canonical targets from Foundation root. In-root `..` traversal from nested owners is allowed; absolute paths, normalized/realpath escape, symlink escape and missing targets fail.
- Diagnostics expose only a stable rule code, Foundation-relative owner path and structural coordinate; never raw cell/link content or an absolute path. Findings are sorted by `(path, coordinate, rule)` and capped at 100 plus an omitted-count summary.
- Historical/completed/artifact documents may be link targets without becoming live owners.

### Decision State Grammar

| State | Target/Evidence Shape | Validator Boundary |
| --- | --- | --- |
| `Proposed` | valid targets with positional `PENDING` | validate current row only |
| `Accepted` | one segment per target: `PENDING` or concrete target-prefixed evidence | validate current row only |
| `Superseded` | preserved target/evidence shape | validate current row; successor topology is not automated until its canonical field/cardinality exists |
| `Rejected` | one positional segment per preserved target: `PENDING` when never consolidated or the existing concrete evidence when previously consolidated | validate current row only |

Only observable current-state structure is enforced. Historical transition truth and semantic adequacy remain review-owned.

The lifecycle requires a supersession link, but the admitted decision table currently has no canonical successor field. Version 1 therefore does not scrape prose, invent a column or claim successor/cycle coverage. Adding that field and its validation requires a separately governed schema change.

For roadmap rows, `Open` requires no acceptance inference. `Exit-Gate-Met` requires the `Exit gate` cell to contain root-confined, resolvable relative links to at least one responsible canonical module under `modules/**` and at least one completed tactical TODO under `todos/completed/**`. The validator checks presence, resolution and target class only; whether those linked records semantically satisfy the gate remains review-owned.

The admitted current decision file uses one nonempty file-level `Provenance` field that applies to every decision row in that file. The validator does not infer different row-level provenance; a future need for mixed provenance in one file requires an explicit schema decision rather than parser guesswork.

### Legacy Check Transition

| Legacy Control | Handling |
| --- | --- |
| ID/table/state/link/path structural checks | replace with validator + tests after parity |
| fixed counts/ID sets/exact content snapshots | retire; they duplicate live state and block valid evolution |
| feature-brief/history scans outside live graph | retire from current structural authority |
| compatible link, whitespace and secret hygiene checks | keep as external delivery evidence where useful |

## Decision Pending — Simplified Replacement Set

| Decision ID | Direction | Why It Matters |
| --- | --- | --- |
| `SD-01` | Validate only the explicit live source graph; do not broad-scan history/artifacts. | prevents hidden authority expansion |
| `SD-02` | Keep a minimal bootstrap kernel for required owners/headings/schemas/enums, never live IDs/counts/content. | prevents self-weakening without duplicating truth |
| `SD-03` | Make validation read-only, fail-closed, root-confined and redacted. | protects integrity and makes failure actionable |
| `SD-04` | Enforce decision index ↔ root-record membership and observable current-row state/target/evidence grammar. | detects orphan, duplicate and structurally broken current records without inventing successor storage |
| `SD-05` | Enforce roadmap evidence structure while leaving semantic sufficiency review-owned. | separates structure from judgment |
| `SD-06` | Use Python stdlib, a thin CLI/parser and independent unittest fixtures/oracles. | keeps maintenance small |
| `SD-07` | Expose only ordinary `--root` validation; no runner, attestation, registry or provenance. | preserves the initial idea |
| `SD-08` | Use ST-01 checks only as one-time migration parity, then retire duplicated snapshots. | controlled simple cutover |
| `SD-09` | Use normal TODO evidence, Git commit/push and delivery guards; no special commit/tree protocol. | uses existing governance |
| `SD-10` | Keep adoption local; CI integration requires a separate future need and approval. | avoids premature automation |

## Decisions

- [x] `SD-01` Explicit live source graph only.
- [x] `SD-02` Minimal bootstrap kernel without live-state duplication.
- [x] `SD-03` Read-only, fail-closed, confined and redacted behavior.
- [x] `SD-04` Current-decision membership and observable lifecycle grammar.
- [x] `SD-05` Structural roadmap evidence only.
- [x] `SD-06` Standard-library thin CLI/parser plus independent unittests.
- [x] `SD-07` Ordinary validation only; no infrastructure subsystem.
- [x] `SD-08` One-time legacy parity and intentional retirement map.
- [x] `SD-09` Normal Git/TODO evidence without special commit protocol.
- [x] `SD-10` Local adoption only; future CI is separate.

## Module Decision Baseline Snapshot

| Canonical Decision | Planned Handling |
| --- | --- |
| `DEC-validator-adoption-trigger` | Preserve and satisfy with simple validator |
| `DEC-single-field-authority` | Preserve; derive from canonical owners |
| `DEC-historical-adoption-boundary` | Preserve via explicit source graph |
| `DEC-decision-effectiveness-after-consolidation` | Preserve structural target/evidence mapping |
| `DEC-immutable-lifecycle-identifiers` | Preserve identifier grammar |
| `DEC-provider-neutral-lifecycle-roles` | Preserve; no provider-specific behavior |

## Decision Baseline

- **Historical design:** D-01..D-55 and freeze `3f351daf` remain in Git history but are not the active implementation contract.
- **Retirement rationale:** D-25..D-55 expanded a documentation validator into a provenance/runner subsystem without a demonstrated need; related special-tree/attestation decisions retire with it.
- **Replacement status:** `SD-01..SD-10 validated by the user on 2026-09-24`
- **Freeze status:** `refreshed and frozen at pushed commit e5bb735a after final residual cleanup`
- **Validation evidence:** exact user token `VALIDO SD-01..SD-10`
- **Implementation authority:** `none`

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `required`
- **Why:** establishes the permanent project-owned structural command and retires duplicated ad hoc checks.
- **Target steady state:** one read-only CLI plus focused tests; canonical docs remain the only live truth owners.
- **Temporary exception:** compatible ST-01 checks may run once for migration parity.
- **Cutover condition:** real repository/mutation suite green, parity classified, docs aligned, reviews/guards complete.

### Patterns To Enforce

| Pattern | Enforcement |
| --- | --- |
| canonical-source derivation | source graph + bootstrap-deletion mutations |
| single-field authority | no live IDs/counts/content hard-coded in Python |
| fail-closed structure | negative fixtures return nonzero with rule/path diagnostics |
| historical boundary | invalid excluded history does not affect current validation |

### Prohibited Anti-Patterns

- hard-coded snapshot of current BLG/DEC records;
- regex-only parsing that silently accepts malformed tables;
- warning-only structural failures;
- rewriting source files;
- expansion into subprocess, provenance, attestation or CI infrastructure.

### Architecture Protection Harness

| Surface | Protection |
| --- | --- |
| live Foundation | validator CLI |
| parser/rules | unittest mutation suite |
| usage/boundary | `deterministic/README.md` |
| delivered diff | critique, test-quality audit and final review |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after simplified decisions are validated/frozen and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** `fresh no-context architecture_opinion requested two localized contract corrections; integrated preservation of concrete evidence for Accepted→Rejected, deterministic structural roadmap-link classes and explicit file-level provenance cardinality in dc66744b. Fresh no-context revalidation on 2026-09-24 returned approve_with_findings with no blockers; the sole low finding was this transient metadata cleanup. Direction approved as proportional, elegant, linear-cost and structurally sound.`
- **Architecture adherence review:** `required after implementation before Completed`
- **Adherence review status:** `not_run`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** reviews must evaluate a stable simplified contract.
- **Trigger stage:** `after VALIDO SD-01..SD-10 and before formal critique`
- **Baseline branch:** `main`
- **Baseline commit:** `e5bb735a`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** `user-validated SD-01..SD-10 direction plus architecture/critique reductions and final residual cleanup committed and pushed before final critique revalidation`
- **Evidence / reference:** original user-validated freeze `f3deae28`; architecture refresh `dc66744b`; critique reduction `728cb305`; final residual cleanup `e5bb735a`; all published on `origin/main` on 2026-09-24
- **Waiver authority / reference (required if waived):** `not applicable`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** prevents expansion back into infrastructure or semantic governance.
- **Trigger stage:** `after formal review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending formal review`
- **Waiver authority / reference (required if waived):** `not applicable`

## Questions To Close

- None before formal pre-approval review; the simplified set was validated with exact token `VALIDO SD-01..SD-10` on 2026-09-24.

## Assumptions Preview

| ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | `deterministic/` is the Foundation tooling surface. | directory + adoption decision | path/diff changes | High | promote as SD-06 |
| `A-02` | Python 3 stdlib is available. | ST-01 checks/Delphi tools | runtime choice changes | High | keep |
| `A-03` | canonical owners expose sufficient structure. | lifecycle/index/roadmap | bounded doc alignment | High | keep |
| `A-04` | no Foundation CI must change now. | repository tree + simplification direction | separate CI TODO | High | promote as SD-10 |
| `A-05` | product/runtime is unaffected. | expected diff/scope | split/renew approval | High | keep |

## Execution Plan

### Touched Surfaces

- CLI/parser package and two focused unittest files.
- `deterministic/README.md`.
- Only directly affected lifecycle/index/roadmap/README/decision/TODO documentation.

### Ordered Steps

1. Validate/freeze `SD-01..SD-10`, run formal plan gates and obtain `APROVADO`.
2. Write independent fail-first fixtures/mutations.
3. Implement bootstrap kernel, parser, rules and bounded diagnostics.
4. Align directly affected canonical guidance and adoption target.
5. Run real acceptance, tests and compatible legacy parity.
6. Run delivery reviews/guards, record evidence, move TODO and publish through normal Git.

### Test Strategy

- **Strategy:** `test-first`
- Fixtures are manual temporary trees and do not reuse production helpers as oracle.
- Each rule has a positive and a mutation/negative case.

### Test Rule Matrix

| Rule | Positive | Required Mutations |
| --- | --- | --- |
| `T-01` headings/tables | exact admitted structure | missing, duplicate, columns/cardinality |
| `T-02` identifiers | unique valid BLG/DEC | bad grammar, duplicate owner, repeated reference allowed |
| `T-03` membership | index equals root record set | orphan/stale/missing/duplicate entry |
| `T-04` states | allowed states | unknown/case/hidden Unicode |
| `T-05` paths/links | confined relative POSIX target | scheme/network/absolute/backslash/query/percent/angle form, normalized or symlink escape, missing target, bad fragment |
| `T-06` target/evidence | positional mapping | missing/extra/duplicate/placeholder mismatch |
| `T-07` roadmap | Open or Exit-Gate-Met with resolvable module + completed-TODO links in `Exit gate` | missing either target class, unresolved/out-of-root link, forbidden target |
| `T-08` decision source evidence | one nonempty file-level Provenance applying to all rows in the admitted decision file | missing, duplicate, empty, misplaced, attempted implicit row-level override |
| `T-09` history boundary | invalid excluded history ignored | same invalid live owner fails |
| `T-10` read-only | identical fixture manifest | mutation on success/failure; production-file open modes are reviewed at closeout |
| `T-11` diagnostics | stable code + relative path + coordinate, sorted and capped at 100 | raw content, absolute path, unstable order, unbounded output |
| `T-12` bootstrap | owners/contracts present | owner/heading/schema/enum removal |
| `T-13` real repo | live Foundation passes | controlled live-copy mutation fails |

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Rationale:** new validator, not a regression requiring reproduction.

### Flow Evidence Planning Matrix

| Surface | User-flow impact | Evidence |
| --- | --- | --- |
| Foundation CLI/docs | none | structure-only waiver; unit/CLI evidence sufficient |

### Local CI-Equivalent Suite Matrix

| Repository | CI-Equivalent | Rationale |
| --- | --- | --- |
| Foundation | `n/a` | no repo-owned CI lane; do not claim CI equivalence |

### Local Validation Matrix

| Behavior | Preconditions | Command | Status |
| --- | --- | --- | --- |
| live structure | canonical checkout | validator CLI | planned |
| mutations | temporary fixtures | unittest discovery | planned |
| syntax/no artifacts | delivered Python + `-B` | no-write compile | planned |
| diff/process | final expected diff | Delphi guards | planned |

### Runtime / Rollout Notes

- No product runtime rollout.
- CLI runs locally on demand.
- CI adoption is separate if repeated drift justifies it.
- Rollback is a normal Git revert.

## Plan Review Gate

- **Status:** `formal critique findings integrated through additional scope reduction; fresh critique revalidation pending`
- **Required lenses:** Architecture, Code Quality, Tests, Performance, Security, Elegance, Structural Soundness.
- **Primary guardrail:** attestation, subprocess supervision, provenance, Registry-v1 or special commit mechanics require a separate demonstrated need/TODO.

### Failure Modes & Edge Cases

- malformed pipes/code spans; duplicate owner vs repeated reference; unsupported fragments; symlink/path escape; incomplete multi-target evidence; hidden Unicode; invalid history accidentally admitted; source mutation/content exposure.

### Residual Unknowns / Risks

- Small parser helpers may be needed but remain implementation-local.
- Semantic quality remains outside automation.
- Successor topology and future syntax changes require explicit canonical schema updates before automation.

## Additional Architectural Opinions

- **Needed:** `no additional exploratory opinion; the simplified direction is dominant and directly addresses the user-requested overengineering reduction`
- **Formal opinion:** required after validated/frozen baseline.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Latest evidence:** `2026-09-24: guard outcome go; trigger fingerprint b82442926521; critique, test-quality audit, final review, verification-debt audit, architecture decision review and architecture adherence review required; triple/security/performance-concurrency reviews not triggered.`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | parser + mutation suite; no infrastructure subsystem |
| `blast_radius` | `cross-stack` | shared Foundation governance only |
| `behavioral_change_or_bugfix` | `yes` | new fail-closed local behavior |
| `changes_public_contract` | `no` | no product API/schema |
| `touches_auth_or_tenant` | `no` | none |
| `touches_runtime_or_infra` | `no` | none |
| `touches_tests` | `yes` | new unittest suite |
| `critical_user_journey` | `no` | internal governance |
| `release_or_promotion_critical` | `no` | no product promotion |
| `high_severity_plan_review_issue` | `yes` | formal critique found an undefined successor representation; resolved by removing unsupported successor automation from v1 |
| `explicit_three_lane_request` | `no` | none |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** medium shared-governance validator with fail-closed logic.
- **Package mode:** `bounded-file-set`
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Critique status:** `findings_integrated`
- **Findings summary:** `fresh critique blockers were integrated by removing unsupported successor automation, making system_roadmap.md the exclusive owner, defining a small link/confinement/diagnostic grammar, removing brittle symbol scanning and keeping read-only attempt detection as code-review evidence. First revalidation found two residual successor promises in VAL-03/SD-04; both were removed without scope expansion.`
- **Evidence / reference:** `formal critique on 2026-09-24 against dc66744b/181cac8f; first revalidation against 728cb305/be9c6d24; final fresh revalidation pending after residual cleanup`
- **Waiver authority / reference (required if waived):** `not applicable`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** assumptions govern owners, runtime and CI boundary.
- **Trigger stage:** `after formal critique convergence and before APROVADO`
- **Guard scope:** `A-01..A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending formal critique`
- **Waiver authority / reference (required if waived):** `not applicable`

## Approval

- **Approved by:** `pending`
- **Approval scope:** `pending architecture revalidation, critique and remaining pre-approval gates for SD-01..SD-10`
- **Execution not authorized by approval:** `CI/CD, product/runtime, Delphi changes, worktrees, attestation/provenance/runner infrastructure`
- **Execution authority:** `not_granted`
- **Prior tokens:** D-01..D-55 history is provenance only and does not authorize the replacement contract.
- **Validation evidence:** exact `VALIDO SD-01..SD-10` received on 2026-09-24.
- **Renewed approval required after gates:** exact `APROVADO`.

## Rules Acknowledgement / Ingestion

Predeclared for readiness; reload after `APROVADO`.

| Source | Applies To | Must Preserve | Must Avoid |
| --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | tactical execution | approval/diff/evidence | implementation before authority |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | lifecycle | phase order | skipped gates |
| `delphi-ai/workflows/docker/todo-contract-refinement-method.md` | planning | bounded contract | speculative expansion |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | next phase | freeze/reviews/preflight | premature approval |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | tests | meaningful mutations | happy-path-only tests |
| `foundation_documentation/project_constitution.md` | project authority | TODO hierarchy | product drift |
| `foundation_documentation/evolution_lifecycle.md` | semantic owner | schemas/owners/history | competing code owner |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Guard outcome:** `pending rerun before APROVADO`

## Decision Adherence Validation

| Decision Set | Status | Evidence |
| --- | --- | --- |
| `D-01..D-55` | retired-before-implementation | Git through `80aaab40`; user-directed simplification |
| `SD-01..SD-10` | validated | exact `VALIDO SD-01..SD-10` received on 2026-09-24 |

## Module Decision Consistency Validation

| Module Decision | Planned Handling | Status |
| --- | --- | --- |
| `DEC-validator-adoption-trigger` | Preserve | planned |
| `DEC-single-field-authority` | Preserve | planned |
| `DEC-historical-adoption-boundary` | Preserve | planned |
| `DEC-decision-effectiveness-after-consolidation` | Preserve | planned |
| `DEC-immutable-lifecycle-identifiers` | Preserve | planned |
| `DEC-provider-neutral-lifecycle-roles` | Preserve | planned |

## Pipeline/Copilot P1/P2 Preflight

| Package | Focus | Status | Evidence |
| --- | --- | --- | --- |
| validator + tests + docs | false greens, parser fragility, scope creep | planned | fresh final review |

## Rule-Spirit Anti-Pattern Hunt

| Principle | Search | Status |
| --- | --- | --- |
| single-field authority | live records/enums duplicated in Python | planned |
| simplicity | runner/attestation/provenance/CI reintroduced | planned |
| historical boundary | broad ignore hides live failure | planned |
| fail-closed | invalid input returns zero/warning | planned |
| strict diff | unrelated paths changed | planned |

## Promotion Finding Routing Ledger

| Finding Group | Classification | Routing | Status |
| --- | --- | --- | --- |
| structural findings through D-24 | useful core requirements | consolidate into `SD-01..SD-06/SD-08` | retained-simplified |
| attestation/runner/provenance D-25..D-55 | disproportionate solution | retire; reopen only as separate need-driven initiative | retired-before-implementation |
| user overengineering correction | project-scope recalibration | simplify TODO and invalidate prior baseline | integrated |

## Security Risk Assessment

- **Risk level:** `low`
- **Why:** local read-only parser with no subprocess, network, auth or runtime integration.
- **Attack surface:** Markdown bytes and paths under supplied Foundation root.
- **Controls:** strict decoding, root/symlink confinement, bounded/redacted diagnostics, no rewriting.
- **Attack simulation decision:** `not_needed`; negative tests cover bounded parser/path risks.
- **Residual risk:** malformed docs can deny validation; semantic misinformation remains review-owned.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `low`
- **Why:** small local files, sequential read-only execution, no services/concurrent mutation.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | endpoint-performance-scrutiny | `not_needed` | `low` | no endpoint | before_local_implemented | `EPS-E1` | `not_applicable` | none | none |
| `FRC` | frontend-race-condition-validation | `not_needed` | `low` | no frontend | before_local_implemented | `FRC-POLICY` | `not_applicable` | none | none |
| `BCI` | backend-concurrency-idempotency-validation | `not_needed` | `low` | no backend mutation | before_local_implemented | `BCI-INV` | `not_applicable` | none | none |
| `RLS` | runtime-load-stress-validation | `not_needed` | `low` | local docs tool | before_production_ready | `RLS-E1` | `not_applicable` | none | none |

## Verification Debt Assessment

- **Audit decision:** `required because complexity=medium`
- **Audit status:** `not_run`
- **Why:** parser/rules can create false-green debt.
- **Evidence / audit artifact:** `pending implementation`
- **Accepted residual debt:** `none planned`

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** trust depends on independent mutations/negative assertions.
- **Trigger signals in scope:** `complexity=medium; touches_tests=yes; fail-closed enforcement`
- **Audit status:** `not_run`
- **Findings summary:** `pending implementation`
- **Evidence / reference:** `pending delivery audit`
- **Waiver authority / reference (required if waived):** `not applicable`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** shared structural enforcement needs post-implementation challenge.
- **Package mode:** `bounded-file-set`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Final review status:** `not_run`
- **Findings summary:** `pending implementation`
- **Evidence / reference:** `pending delivery review`
- **Waiver authority / reference (required if waived):** `not applicable`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** simplified SD-01..SD-10 direction remains validated; localized architecture findings were integrated and require refreshed freeze/revalidation before critique and approval.
- **Post-commit/push status:** final residual cleanup is published at `foundation_documentation:main@e5bb735a`; refreshed freeze annotation is pending publication.
- **Next path/status action:** publish the refreshed freeze annotation, rerun critique once, then run assumption/scope guards and authority preflight.

## Commands

### Planning / pre-approval

- `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md --pre-approval`
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py --repo-root foundation_documentation foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`

### Planned implementation validation

- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'`
- `git -C foundation_documentation diff --check`

## Files Expected

- `foundation_documentation/deterministic/validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/foundation_lifecycle/__init__.py`
- `foundation_documentation/deterministic/foundation_lifecycle/parser.py`
- `foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/tests/test_foundation_parser.py`
- `foundation_documentation/deterministic/README.md`
- directly affected canonical docs listed in Diff Expectation Contract
- this TODO moved from `active/process/` to `completed/process/` at closeout
