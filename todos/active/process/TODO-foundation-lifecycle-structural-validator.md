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
- **Tactical TODO lifecycle state:** `In-Progress`
- **Qualifiers:** `none`
- **Next exact step:** complete the fresh final-review rerun, verification-debt audit and atomic closeout guards.

## Active Work State

- **Work state:** `review`
- **Why this state now:** implementation and package-matched architecture/test-quality audits are complete; final evidence and closeout gates remain.
- **Exit condition:** simplified decisions validated/frozen, pre-approval gates green, explicit `APROVADO`, implementation/evidence complete, and TODO promoted to `completed/`.

## Trigger Evidence

- Completed ST-01 established canonical lifecycle owners and exact structural checks.
- The current check surface is difficult to reuse because it is embedded in a completed TODO.
- No production runtime, API, UI, database or deployment behavior is involved.

## Scope

- [x] `S-01` Implement `deterministic/validate_foundation_lifecycle.py` as a read-only Python standard-library CLI.
- [x] `S-02` Implement bounded structural parsing in `deterministic/foundation_lifecycle/parser.py`.
- [x] `S-03` Validate live backlog, decision index/records, lifecycle schemas and roadmap gate-evidence structure.
- [x] `S-04` Enforce ID uniqueness, required headings/tables, exact columns, allowed states, reference resolution and root confinement.
- [x] `S-05` Preserve the historical-document exception: only admitted live owners are scanned as authorities.
- [x] `S-06` Add independent positive and mutation tests using temporary fixtures.
- [x] `S-07` Document the CLI, structural boundary, exit behavior and canonical owners.
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

- **Current lane:** `implementation/delivery-validation`
- **Execution authority:** `granted by explicit APROVADO; todo_authority_guard outcome go`
- **Topology:** `principal checkout, single writer, no worktrees`
- **Implementation owner after approval:** `routine-executor / Operational Coder`; implementation completed locally.
- **Assurance handoff:** `Assurance / Tester-Quality`; fresh delivery audits in progress.

## Promotion Evidence

- **Branch:** `main`
- **Promotion target:** `foundation_documentation:main`
- **Current claim:** local implementation under validation; no delivery/closeout claim.

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

- [x] `DOD-01` CLI validates the real live Foundation owner graph and returns zero.
- [x] `DOD-02` Every structural rule has a positive control and meaningful mutation test.
- [x] `DOD-03` Input trees remain byte-for-byte unchanged on success and failure.
- [x] `DOD-04` Minimal bootstrap kernel detects removal/rename of required owners, headings, schemas and enums without copying live records.
- [x] `DOD-05` Paths/references are root-confined and diagnostics do not echo sensitive content.
- [x] `DOD-06` README/lifecycle/decision guidance names the validator without duplicating live state.
- [x] `DOD-07` Legacy ST-01 checks are classified as parity evidence or retired controls, not embedded implementation.
- [ ] `DOD-08` Required audits/reviews and deterministic TODO guards pass before closeout.

## Validation Steps

- [x] `VAL-01` `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- [x] `VAL-02` `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=foundation_documentation/deterministic python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'`
- [x] `VAL-03` Run mutations for IDs, tables, links, paths, observable current-row state/target/evidence, roadmap evidence and read-only behavior.
- [x] `VAL-04` Run a no-write compile check with `python3 -B` over delivered Python files.
- [x] `VAL-05` Run compatible ST-01 checks once as migration parity evidence and record retired assertions.
- [ ] `VAL-06` Run `git diff --check`, diff expectation, authority and completion guards at required phases.
- [x] `VAL-07` Confirm the final diff contains no runner, attestation, registry, subprocess/provenance or CI implementation.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01` | Scope | `S-01` Implement `deterministic/validate_foundation_lifecycle.py` as a read-only Python standard-library CLI. | code+test | live CLI exit 0; read-only fixture manifests | local | passed | public CLI implemented |
| `S-02` | Scope | `S-02` Implement bounded structural parsing in `deterministic/foundation_lifecycle/parser.py`. | code+review | parser + architecture audit v9 | local | passed | bounded admitted grammar |
| `S-03` | Scope | `S-03` Validate live backlog, decision index/records, lifecycle schemas and roadmap gate-evidence structure. | test | 110-test T-01..T-13 suite against lifecycle schema artifacts with owner-specific mutations | local | passed | each owner has positive/mutation coverage |
| `S-04` | Scope | `S-04` Enforce ID uniqueness, required headings/tables, exact columns, allowed states, reference resolution and root confinement. | test | parser suite + independent adversarial probes | local | passed | fail-closed cases green |
| `S-05` | Scope | `S-05` Preserve the historical-document exception: only admitted live owners are scanned as authorities. | test | excluded-history vs live-owner paired test | local | passed | history remains non-authoritative |
| `S-06` | Scope | `S-06` Add independent positive and mutation tests using temporary fixtures. | test+audit | independent parser/CLI fixtures; test-quality audit v10 | local | passed | no shared production oracle |
| `S-07` | Scope | `S-07` Document the CLI, structural boundary, exit behavior and canonical owners. | doc+review | `deterministic/README.md` and root guidance diff | n/a | passed | commands and boundaries explicit |
| `S-08` | Scope | `S-08` Align directly affected lifecycle/index/roadmap guidance and retarget the validator-adoption decision at closeout. | doc+move | canonical docs aligned; decision retarget waits for atomic completed-path move | n/a | pending | closeout-only remaining scope item |
| `DOD-01` | Definition of Done | `DOD-01` CLI validates the real live Foundation owner graph and returns zero. | test | exact VAL-01 exit 0 | local | passed | no diagnostics on live graph |
| `DOD-02` | Definition of Done | `DOD-02` Every structural rule has a positive control and meaningful mutation test. | test+audit | 110 tests; test-quality audit v10 approved exact snapshot | local | passed | T-01..T-13 substantive |
| `DOD-03` | Definition of Done | `DOD-03` Input trees remain byte-for-byte unchanged on success and failure. | test | success/failure manifest tests | local | passed | no source writes |
| `DOD-04` | Definition of Done | `DOD-04` Minimal bootstrap kernel detects removal/rename of required owners, headings, schemas and enums without copying live records. | test | five machines, identifiers, authority/transition schemas | local | passed | section-anchored; no live rows/counts |
| `DOD-05` | Definition of Done | `DOD-05` Paths/references are root-confined and diagnostics do not echo sensitive content. | test | symlink/escape/redaction/cap mutations | local | passed | absolute/raw content absent |
| `DOD-06` | Definition of Done | `DOD-06` README/lifecycle/decision guidance names the validator without duplicating live state. | doc+review | strict doc diff + architecture audit v9 | n/a | passed | links and structural rules only |
| `DOD-07` | Definition of Done | `DOD-07` Legacy ST-01 checks are classified as parity evidence or retired controls, not embedded implementation. | parity+review | Legacy Check Transition + compatible link/module/secret checks | local | passed | fixed snapshots/history scans retired |
| `DOD-08` | Definition of Done | `DOD-08` Required audits/reviews and deterministic TODO guards pass before closeout. | guard+review | authority/diff go; final review/completion/closeout pending | local | pending | procedural final gates only |
| `VAL-01` | Validation Steps | `VAL-01` `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | test | exact command exit 0 | local | passed | live acceptance |
| `VAL-02` | Validation Steps | `VAL-02` `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=foundation_documentation/deterministic python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` | test | exact command: 110/110 | local | passed | no bytecode residue |
| `VAL-03` | Validation Steps | `VAL-03` Run mutations for IDs, tables, links, paths, observable current-row state/target/evidence, roadmap evidence and read-only behavior. | test+audit | T-01..T-13 suite and independent probes | local | passed | all demonstrated false greens fixed |
| `VAL-04` | Validation Steps | `VAL-04` Run a no-write compile check with `python3 -B` over delivered Python files. | test | five Python sources compile in memory | local | passed | no pyc/pyo |
| `VAL-05` | Validation Steps | `VAL-05` Run compatible ST-01 checks once as migration parity evidence and record retired assertions. | migration parity | legacy links, module diff and secret scan exit 0 as migration parity evidence | local | passed | incompatible snapshots intentionally retired |
| `VAL-06` | Validation Steps | `VAL-06` Run `git diff --check`, diff expectation, authority and completion guards at required phases. | guard | diff/authority go; completion/closeout pending atomic move | local | pending | rerun at final closeout |
| `VAL-07` | Validation Steps | `VAL-07` Confirm the final diff contains no runner, attestation, registry, subprocess/provenance or CI implementation. | review+scan | strict diff + rule-spirit 0 findings + reviews | local | passed | test subprocess only invokes CLI |

## External Dependency Readiness

- Python 3 and Git are existing local prerequisites.
- No network, hosted service, external package or sibling-repository runtime dependency is required.
- Delphi guards remain external workflow tools and are not imported or executed by validator code.

## Package-First Assessment

- **Queries executed:** `bash delphi-ai/tools/query_packages.sh --project-root /mnt/c/unifast/leadshug/leadshug_now_docker --search "markdown validator"`; same command with `--search "foundation"`.
- **Relevant packages found:** `none` in local or ecosystem registries.
- **READMEs read:** `none required`.
- **Decision:** local Foundation implementation in the approved `deterministic/` surface; no new proprietary or external package.
- **Rationale:** the bounded grammar is Foundation-specific and Python stdlib is frozen by SD-06.

## Profile Scope & Handoffs

- **Primary planning profile:** `Strategic / CTO-Tech-Lead`
- **Implementation profile:** `Operational / Coder`
- **Assurance profile:** `Assurance / Tester-Quality`
- **Scope overlay:** `docker/Foundation documentary tooling`

### Handoff Log

| From | To | Purpose | Status |
| --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Operational / Coder | implement bounded validator/tests after approval | completed |
| Operational / Coder | Assurance / Tester-Quality | challenge mutations, false greens and read-only behavior | completed |

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

## Simplified Replacement Decision Set

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
- **Replacement status:** `SD-01..SD-10 and post-review refinements validated by the user on 2026-09-24`
- **Freeze status:** `renewed post-review baseline frozen at pushed commit e3642929 including schema-only preflight normalization`
- **Validation evidence:** exact user tokens `VALIDO SD-01..SD-10` and `VALIDO SD-01..SD-10 POS-REVIEW`
- **Implementation authority:** `granted by explicit APROVADO; normal authority guard returned go on 2026-09-24`

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `required`
- **Why this applies:** establishes the permanent project-owned structural command while preserving canonical documents as the only live truth owners.
- **Deviation / debt being retired:** structural checks embedded in a completed TODO and the rejected runner/attestation/provenance-subsystem design.
- **Target steady-state after closeout:** one read-only stdlib CLI plus focused tests; no duplicated live records or infrastructure subsystem.
- **Temporary exceptions allowed:** compatible ST-01 checks may run once for migration parity only.
- **Cutover / removal condition:** real repository and mutation suite green, parity classified, directly affected docs aligned, and required delivery gates complete.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| canonical-source derivation | `SD-01/SD-02` | validator/parser | avoid copied live state |
| single-field authority | `DEC-single-field-authority` | parser constants | no live IDs/counts/content hard-coded in Python |
| fail-closed structure | `SD-03` | CLI diagnostics/exit | invalid admitted structure cannot pass silently |
| historical boundary | `SD-01/SD-08` | source graph | excluded history cannot become competing authority |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| hard-coded current BLG/DEC snapshots | review/tests find live IDs/counts in Python | duplicates canonical state | none |
| permissive regex-only acceptance | malformed-table mutation returns zero | creates false greens | none |
| warning-only structural failure | invalid fixture exits zero | violates fail-closed behavior | none |
| source rewriting | fixture manifest changes | validator must remain read-only | none |
| runner/attestation/provenance subsystem or CI | imports/files/diff exceed declared boundary | reintroduces disproportionate infrastructure | separate need-driven TODO and approval |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| guard | live Foundation | `deterministic/validate_foundation_lifecycle.py` | broken admitted structure | implement-in-this-todo | live CLI output |
| test | parser/rules | unittest mutation suite | false greens and parser drift | implement-in-this-todo | test output + mutation mapping |
| documentation | usage/boundary | `deterministic/README.md` | undocumented scope/exit behavior | implement-in-this-todo | final doc review |
| audit | delivered diff | critique, test-quality audit and final review | scope creep and weak tests | implement-in-this-todo | TODO gate evidence |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after simplified decisions are validated/frozen and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** `fresh no-context architecture_opinion requested two localized contract corrections; integrated preservation of concrete evidence for Accepted→Rejected, deterministic structural roadmap-link classes and explicit file-level provenance cardinality in dc66744b. Fresh no-context revalidation on 2026-09-24 returned approve_with_findings with no blockers; the sole low finding was this transient metadata cleanup. Direction approved as proportional, elegant, linear-cost and structurally sound.`
- **Architecture adherence review:** `required`
- **Adherence review status:** `no_material_findings`
- **Adherence review evidence:** fresh no-context architecture review `/root/foundation_validator_arch_audit_v9` approved the exact 110-test snapshot on 2026-09-24 after strict-Markdown, outerless-table and lexical/resolved-confinement findings were integrated; SD-01..SD-10 remain adherent and proportional.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** reviews must evaluate a stable simplified contract.
- **Trigger stage:** `after VALIDO SD-01..SD-10 and before formal critique`
- **Baseline branch:** `main`
- **Baseline commit:** `e3642929`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** `post-review contract, human revalidation record and semantically equivalent preflight-schema normalization are committed and pushed before final guards`
- **Evidence / reference:** original validation freeze `f3deae28`; reviewed candidate `9a2c677f`; renewed validation `4b1158d5`; schema-normalized freeze `e3642929`; exact token `VALIDO SD-01..SD-10 POS-REVIEW`; all published on `origin/main` on 2026-09-24
- **Waiver authority / reference (required if waived):** `not applicable`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** prevents expansion back into infrastructure or semantic governance.
- **Trigger stage:** `after formal review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** `0/22 material sections differ from the schema-normalized renewed baseline; no scope drift remains`
- **Evidence / reference:** `2026-09-24 review_scope_drift_guard outcome go against foundation_documentation:main@e3642929`
- **Waiver authority / reference (required if waived):** `not applicable`

## Questions To Close

- None before the remaining deterministic pre-approval guards; post-review refinements were revalidated with exact token `VALIDO SD-01..SD-10 POS-REVIEW`.

## Assumptions Preview

| ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | `deterministic/` is the Foundation tooling surface. | directory + adoption decision | path/diff changes | High | Promote to Decision |
| `A-02` | Python 3 stdlib is available. | ST-01 checks/Delphi tools | runtime choice changes | High | Promote to Decision |
| `A-03` | canonical owners expose sufficient structure. | lifecycle/index/roadmap | bounded doc alignment | High | Promote to Decision |
| `A-04` | no Foundation CI must change now. | repository tree + simplification direction | separate CI TODO | High | Promote to Decision |
| `A-05` | product/runtime is unaffected. | expected diff/scope | split/renew approval | High | Promote to Decision |

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

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation documentary validator | local Foundation code/docs changed, but this repository owns no CI job | n/a — no repo-owned CI-equivalent surface exists | n/a | `n/a` | Local-Implemented | n/a | local CLI, 110 unittests and deterministic guards are validation evidence, not CI equivalence | do not claim CI equivalence; future CI adoption is a separate approved TODO |

### Local Validation Matrix

| Behavior | Preconditions | Command | Status |
| --- | --- | --- | --- |
| live structure | canonical checkout | validator CLI | passed |
| mutations | independent temporary fixtures | unittest discovery | passed — 110 tests |
| syntax/no artifacts | delivered Python + `-B` | no-write compile | passed — five files, no pyc/pyo |
| diff/process | final expected diff | Delphi guards | passed so far — diff expectation go; completion/closeout rerun at final gate |

### Runtime / Rollout Notes

- No product runtime rollout.
- CLI runs locally on demand.
- CI adoption is separate if repeated drift justifies it.
- Rollback is a normal Git revert.

## Plan Review Gate

- **Status:** `converged; architecture and critique gates have no blocking findings`
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
- **Findings summary:** `fresh critique blockers were integrated by further reducing scope. Final fresh revalidation against e5bb735a/92c24770 returned approve_with_findings with no blocker. CF-01 (low) is Challenged as lexical only: OOS-03/SD-07/VAL-07 exclude an execution/toolchain provenance subsystem, while the explicitly retained file-level Provenance field is canonical decision metadata.`
- **Evidence / reference:** `formal critique and two fresh revalidations on 2026-09-24; final position approve_with_findings; no critical/high/medium/blocking findings; performance, security, test-oracle independence, elegance and structural soundness accepted`
- **Waiver authority / reference (required if waived):** `not applicable`

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `CF-01` | Challenged | noise | no | none | `n/a` | lexical provenance hit; SD-07/OOS-03 exclude a toolchain-provenance subsystem while file-level decision provenance remains intentional metadata |
| `FV-TQA-01..03` | Integrated | useful | yes | project | `T-01..T-13` | independent mutations and assertions integrated; superseded by exact-snapshot audit v10 |
| `FV-ARCH-01..N` | Integrated | useful | yes | project | `SD-01..SD-10` | strict Markdown, owner and confinement findings integrated; superseded by architecture audit v9 |
| `FV-FINAL-01..06` | Integrated | useful | yes | project | `SD-03` | entity/path/table/autolink/reference-definition bypasses closed with regressions |
| `FV-FINAL-V3-01..05` | Integrated | useful | yes | project | `T-02,T-05,T-06,T-12` | multiline links, separators, CAP kernel and canonical aliases fail closed |
| `FV-FINAL-V3-06` | Integrated | useful | yes | paced | `delivery-gates` | machine-checkable resolution rows and criterion-specific evidence normalized; final guards remain explicit until atomic closeout |
| `FV-TQA-V8-01` | Integrated | useful | yes | project | `T-04,T-06` | state/evidence branch mutations and Open/terminal positive controls added |
| `FV-ARCH-V7-01` | Integrated | useful | yes | project | `T-01` | canonical tables reject outerless GFM rows and duplicate tables |
| `FV-ARCH-V8-01` | Integrated | useful | yes | project | `T-05` | normalized lexical and resolved confinement enforced independently |
| `FV-TQA-V9-01` | Integrated | useful | yes | project | `T-06` | Accepted/Rejected/Superseded supported evidence forms have positive controls |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** assumptions govern owners, runtime and CI boundary.
- **Trigger stage:** `after formal critique convergence and before APROVADO`
- **Guard scope:** `A-01..A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** `A-01..A-05 are no longer live assumptions: their boundaries are frozen in SD-01/SD-02/SD-06/SD-10 plus Scope/Out of Scope; no unsupported code assumption remains.`
- **Evidence / reference:** `2026-09-24 assumption_code_coherence_guard outcome go; zero live assumptions; A-01..A-05 normalized to Promote to Decision`
- **Waiver authority / reference (required if waived):** `not applicable`

## Approval

- **Approved by:** `user on 2026-09-24 with exact token APROVADO`
- **Approval scope:** `implement only the validated SD-01..SD-10 Foundation validator, focused tests and directly affected canonical Foundation docs declared by the strict diff contract`
- **Execution not authorized by approval:** `CI/CD, product/runtime, Delphi changes, worktrees, attestation/provenance/runner infrastructure`
- **Execution authority:** `granted; normal todo_authority_guard outcome go on 2026-09-24`
- **Prior tokens:** D-01..D-55 history is provenance only and does not authorize the replacement contract.
- **Validation evidence:** exact `VALIDO SD-01..SD-10` received on 2026-09-24.
- **Renewed approval rule:** not required for the approved package; only a material scope deviation requires renewed validation and `APROVADO`.

## Rules Acknowledgement / Ingestion

Reloaded after `APROVADO` on 2026-09-24; the normal authority guard returned `go` before implementation.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | tactical execution | approval/diff/evidence | implementation before authority | keep execution behind guards |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | lifecycle orchestration | phase order | skipped gates | follow approval→execution→delivery order |
| `delphi-ai/workflows/docker/todo-contract-refinement-method.md` | frozen contract | bounded scope | speculative expansion | renew approval on material change |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | current phase | freeze/reviews/preflight | premature approval | require preflight-go before request |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | new tests | meaningful mutations | happy-path-only tests | test-first independent fixtures |
| `foundation_documentation/project_constitution.md` | project authority | TODO hierarchy | product drift | Foundation-only changes |
| `foundation_documentation/evolution_lifecycle.md` | semantic owner | schemas/owners/history | competing code owner | parser derives bounded structure |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `authorized by APROVADO against the published routine-executor implementation plan on 2026-09-24`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status (`Adherent`/`Exception`) | Evidence | Notes |
| --- | --- | --- | --- |
| `SD-01` | Adherent | parser admits only lifecycle, backlog, decision index/records and roadmap | history remains link-target-only |
| `SD-02` | Adherent | section-anchored bootstrap tests for identifiers, authority table and five schemas/enums/transitions | no live IDs, row contents or counts copied |
| `SD-03` | Adherent | read-only manifest tests, confinement probes and redacted/capped diagnostics | malformed or ambiguous Markdown fails closed |
| `SD-04` | Adherent | exact Records grammar, root membership, global DEC uniqueness, provenance and positional evidence tests | successor topology remains review-owned |
| `SD-05` | Adherent | roadmap requires resolvable Markdown module and completed-TODO links | semantic sufficiency remains review-owned |
| `SD-06` | Adherent | stdlib-only CLI/parser and independent parser/CLI fixtures; 110 tests | no external dependency or shared oracle |
| `SD-07` | Adherent | public surface is only `validate_foundation_lifecycle.py --root` | no production subprocess/runner/registry/attestation |
| `SD-08` | Adherent | compatible legacy links/modules/secret checks passed once; rigid snapshots retired | transition documented under Legacy Check Transition |
| `SD-09` | Adherent | normal TODO evidence, commits and guards only | publication/closeout remains normal Git workflow |
| `SD-10` | Adherent | no `.github` or CI path in strict diff | CI future remains separately governed |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status (`Preserved|Superseded (Approved)|Regression`) | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `DEC-validator-adoption-trigger` | satisfy with simple validator | Preserved | `evolution_lifecycle.md`; live CLI; strict diff | closeout retarget remains S-08 |
| `DEC-single-field-authority` | derive from canonical owners | Preserved | parser contains schemas/enums only, no live rows/IDs/counts | owner graph explicit |
| `DEC-historical-adoption-boundary` | scan only admitted live graph | Preserved | invalid completed history ignored while same live mutation fails | history is not authority |
| `DEC-decision-effectiveness-after-consolidation` | enforce structural target/evidence mapping | Preserved | positional target/evidence and canonical-target tests | semantic effectiveness remains review-owned |
| `DEC-immutable-lifecycle-identifiers` | enforce declared grammar | Preserved | BLG/DEC grammar and uniqueness mutations | declarations section-anchored |
| `DEC-provider-neutral-lifecycle-roles` | avoid provider behavior | Preserved | no provider-specific implementation; module files unchanged | tooling remains an adapter |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| bounded validator + tests + docs diff | false greens, parser fragility, confinement and scope creep | passed | architecture audit v9 + test-quality audit v10; 110 tests; live CLI; diff guard | all implementation findings integrated; none remaining | fresh final no-context rerun remains the distinct closeout gate |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| single-field authority | live records/IDs/counts duplicated in Python | passed | parser inspection + architecture audit v9 | none | only structural schema/enums are bootstrapped |
| simplicity | runner/attestation/provenance/CI reintroduced | passed | `bash <(sed 's/\r$//' delphi-ai/tools/rule_spirit_anti_pattern_scan.sh) --repo foundation_documentation --stack docker` exit 0; `Findings: 0` | none | one CLI, parser and tests only; CR-stripped read-only invocation works around pre-existing wrapper line endings |
| historical boundary | broad ignore hides live failure | passed | paired excluded-history/live-owner mutations | none | explicit graph stays authoritative |
| fail-closed | invalid input returns zero/warning | passed | 110 tests + independent adversarial probes | none remaining | ambiguous unsupported Markdown is rejected |
| strict diff | unrelated paths changed | passed | `python3 delphi-ai/tools/todo_diff_expectation_guard.py --repo-root foundation_documentation foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md` exit 0 with `Overall outcome: go` | none | 12 classified changed paths, 0 forbidden/unclassified |

## Promotion Finding Routing Ledger

| Finding ID | Finding Source | Severity | Classification | Required Action | Status | Rationale / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `PR-01` | planning review | medium | by-design/no-action | retain simplified structural core | accepted | SD-01..SD-10 validations on 2026-09-24 |
| `PR-02` | user-directed reduction | high | by-design/no-action | keep D-25..D-55 retired | accepted | reopen only under separate demonstrated need |
| `PR-03` | pre-approval review | high | release-blocker | replace overengineered baseline | fixed | `VALIDO SD-01..SD-10 POS-REVIEW` |
| `FV-TQA-01..03` | independent test-quality audits | medium/high | release-blocker | close false-green and mutation-evidence gaps in current TODO | fixed | test-quality v5 approved frozen 84-test package |
| `FV-ARCH-01..N` | architecture adherence adversarial review | medium/high | release-blocker | make narrow Markdown/source graph fail closed without scope expansion | fixed | architecture audit v4 approved with no material findings |
| `FV-FINAL-01..06` | first final-review lane | medium/high | release-blocker | close entity, unsafe-path, table-cell, autolink and reference-definition bypasses | fixed | 96-test intermediate package; superseded by later exact-snapshot reviews |
| `FV-FINAL-V3-01..05` | correctly routed final review v3 | high/P2 | release-blocker | close multiline-link, non-CommonMark-separator, CAP-kernel and canonical-alias gaps; refresh audits | fixed | parser/tests now cover each case; audits v9/v10 approve 110-test snapshot |
| `FV-FINAL-V3-06` | correctly routed final review v3 | P2 | release-blocker | complete finding ledger, verification-debt and deterministic closeout evidence | fixed | machine-checkable ledger and criterion-specific evidence normalized; final/debt guards remain ordinary closeout gates |
| `FV-TQA-V8-01` | test-quality audit v8 | high | release-blocker | add independent state/evidence branch mutations | fixed | invalid decision/roadmap states, Open, Proposed and Rejected branches covered |
| `FV-ARCH-V7-01` | architecture audit v7 | high | release-blocker | fail closed on outerless GFM canonical rows/tables | fixed | owner rows and duplicate-table mutation coverage; audit v9 approval |
| `FV-ARCH-V8-01` | architecture audit v8 | high | release-blocker | require lexical and resolved root confinement independently | fixed | three owner leave/reenter mutations; audit v9 approval |
| `FV-TQA-V9-01` | test-quality audit v9 | medium | release-blocker | add positive terminal-state evidence controls | fixed | Accepted/Rejected/Superseded PENDING/concrete matrix; audit v10 approval |
| `FV-FINAL-V4-01` | final review v4 | P2 | release-blocker | replace planned-sounding strict-diff evidence with concrete result | fixed | exact command records 12 classified paths, 0 forbidden/unclassified and guard `go` |
| `FV-FINAL-V4-02` | final review v4 | low/P2 | release-blocker | remove stale live pending-decision heading | fixed | heading now reflects frozen Simplified Replacement Decision Set |

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
- **Audit status:** `no_material_findings`
- **Why:** parser/rules can create false-green debt.
- **Evidence / audit artifact:** `verification_debt_audit.sh --scan-git-modified` executed through read-only CRLF normalization on 2026-09-24; heuristic `high` was manually adjudicated as the three explicit atomic-closeout items plus governed `TODO`/`PENDING` vocabulary in historical/templates, not hidden verification debt. Exact-snapshot architecture audit v9, test-quality audit v10, 110/110 tests and finding carry-forward extraction are green.
- **Inline code TODO debt:** `none`; the three deterministic-source matches are the required literal lifecycle schema phrase `immutable TODO path`, not debt markers.
- **Accepted residual debt:** `none`

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** trust depends on independent mutations/negative assertions.
- **Trigger signals in scope:** `complexity=medium; touches_tests=yes; fail-closed enforcement`
- **Audit status:** `no_material_findings`
- **Findings summary:** all T-01..T-13 areas substantive; prior membership, provenance, positional evidence, strict-Markdown and assertion-strength gaps integrated; no skips, bypasses or weak status-only assertions remain.
- **Evidence / reference:** `/root/foundation_validator_test_audit_v10`; exact current snapshot approved; live CLI and 110/110 tests passed on 2026-09-24.
- **Waiver authority / reference (required if waived):** `not applicable`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** shared structural enforcement needs post-implementation challenge.
- **Package mode:** `bounded-file-set`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Final review status:** `findings_integrated`
- **Findings summary:** final-review blockers through FV-FINAL-V3-06 were integrated within the approved parser/test/evidence boundary; a fresh clean verdict is still required.
- **Evidence / reference:** `/root/foundation_validator_final_review` and `/root/foundation_validator_final_review_v3`; remediation proven by 110-test package and exact-snapshot audits v9/v10; clean rerun pending.
- **Waiver authority / reference (required if waived):** `not applicable`

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `FV-FINAL-01..06` | Integrated | useful | yes | project | `SD-03` | entity/path/table/autolink/reference-definition bypasses closed with mutations |
| `FV-FINAL-V3-01..05` | Integrated | useful | yes | project | `T-02,T-05,T-06,T-12` | multiline links, separators, CAP kernel and canonical aliases fail closed |
| `FV-FINAL-V3-06` | Integrated | useful | yes | paced | `delivery-gates` | resolution/evidence contracts normalized; clean rerun remains required before closeout |
| `FV-FINAL-V4-01` | Integrated | useful | yes | paced | `completion-evidence` | strict-diff evidence states the concrete guard result without planned vocabulary |
| `FV-FINAL-V4-02` | Integrated | useful | yes | project | `SD-01..SD-10` | stale pending-decision heading renamed to match the frozen decision set |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** implementation and exact-snapshot architecture/test-quality audits are complete; final review, verification-debt and atomic closeout gates remain.
- **Post-commit/push status:** implementation evidence is uncommitted and unpublished.
- **Next path/status action:** run required delivery gates and reviews before any closeout action.

## Commands

### Planning / pre-approval

- `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md --pre-approval`
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py --repo-root foundation_documentation foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`

### Planned implementation validation

- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=foundation_documentation/deterministic python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'`
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
