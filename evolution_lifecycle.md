# LeadsHug Evolution Lifecycle

**Version:** 1.0

This document owns the schemas, state machines, transition rules, and field-authority model for Foundation evolution. It does not own live candidate disposition, roadmap planning, module truth, TODO evidence, decision rationale, or contract inventory.

## Roles and authority

Roles are provider-neutral. A concrete person, team, or tool acts only as an adapter for the role; it does not acquire product authority by being named in a tool or workflow.

| Role | Authority |
| --- | --- |
| Human decision authority | Validates material product, scope, and approval decisions. |
| Strategic steward | Maintains cross-system direction, lifecycle coherence, and the roadmap. |
| Module owner | Maintains stable module-local ownership, invariants, capabilities, and contracts. |
| TODO owner/executor | Maintains the approved tactical contract, execution record, and evidence. |
| Assurance reviewer | Independently evaluates adherence and evidence; does not grant product authority. |

## Immutable identifiers

New lifecycle records use immutable lowercase slug identifiers: `BLG-<slug>` for backlog candidates, `DEC-<slug>` for decisions, and `CAP-<slug>` for capabilities. Titles and filenames may change; the identifier and supersession links do not. IDs are references, not a second store of a record's live fields.

## Authority matrix

| Field / truth | Canonical owner | Other surfaces |
| --- | --- | --- |
| Schemas, enums, transitions, role semantics | this lifecycle | link only |
| Candidate disposition and next gate | [`backlog/`](backlog/README.md) | link by immutable ID |
| Theme/phase, horizon, expected outcome, dependencies, exit gate | [`system_roadmap.md`](system_roadmap.md) | link only; gate status is derived from exit-gate evidence |
| Module ownership, invariants, stable capabilities, local contracts | [`modules/`](modules/README.md) | link only |
| Approval, execution state, validation, delivery evidence | [`todos/`](todos/README.md) | link only |
| Durable rationale, provenance, supersession history | [`decisions/`](decisions/README.md) | link only |
| Contract index and verification rule | [`contracts/`](contracts/README.md) | no duplicate contract status |
| Discovery observations and supporting evidence | [`artifacts/`](artifacts/README.md) | non-authoritative links only |

## Shared qualifier

`Blocked` is an orthogonal qualifier, never a destructive state. It records the preserved prior state, a reason, an owner, and an unblock condition. It neither approves work nor changes any state machine.

## State machines

### Candidates

**Schema:** immutable ID; title; state; source/evidence link; value/risk; dependencies; disposition owner; next gate.

**Field definitions:** `Proposed` is captured but not triaged; `Under-Review` is being assessed; `Selected-for-Planning` is eligible to be framed, not executed; `Deferred` waits on a named dependency or priority decision; `Rejected` is not being pursued.

**Enum:** `Proposed|Under-Review|Selected-for-Planning|Deferred|Rejected`

| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
| Proposed | strategic steward + discovery evidence | Under-Review | assessment begins |
| Under-Review | strategic steward + next-gate record | Selected-for-Planning | may produce a planning proposal, never execution |
| Under-Review or Selected-for-Planning | strategic steward + dependency/priority rationale | Deferred | preserves the candidate and named unblock condition |
| Proposed, Under-Review, Selected-for-Planning, or Deferred | human decision authority + rationale | Rejected | terminal unless a new candidate is created |
| Deferred | strategic steward + resolved unblock evidence | Under-Review | reopening is explicit |

Cancellation is represented by `Rejected`; reopening a rejected idea requires a new immutable candidate ID so its history is not rewritten.

### Capabilities

**Schema:** immutable ID; module owner; state; evidence; dependency links; intended outcome; retirement rationale when applicable.

**Field definitions:** `Not-Assessed` has no qualified evidence; `Discovery` is being investigated; `Planned` has an accepted direction but no delivery claim; `In-Progress` is under an approved TODO; `Delivered` has accepted evidence; `Retired` is intentionally no longer offered.

**Enum:** `Not-Assessed|Discovery|Planned|In-Progress|Delivered|Retired`

| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
| Not-Assessed | module owner + evidence | Discovery | investigation begins |
| Discovery | module owner + roadmap/TODO link | Planned | direction is recorded without delivery claim |
| Planned | TODO owner + explicit approval and authority guard `go` | In-Progress | execution authority is separate from planning |
| In-Progress | TODO owner + accepted evidence | Delivered | delivery evidence is linked |
| Delivered | module owner + rationale | Retired | retirement is explicit |
| Planned or In-Progress | module owner + changed evidence | Discovery | reopening returns to investigation |

Cancellation of planned work returns it to `Discovery` or leaves it `Not-Assessed`, with rationale; an in-progress cancellation is first recorded in its TODO, then reconciled by the module owner.

### Tactical TODOs

**Schema:** immutable TODO path/identity; objective; scope; state; approval evidence; owner; validation/evidence; delivery disposition.

**Field definitions:** `Draft` is authored but unreviewed; `Review` is being refined; `Approved` has an approved contract but may not yet be executing; `In-Progress` is executing only after explicit `APROVADO` and authority guard `go`; `Completed` has passed its applicable delivery/closeout gates; `Cancelled` records a stopped contract.

**Enum:** `Draft|Review|Approved|In-Progress|Completed|Cancelled`

| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
| Draft | TODO owner | Review | refinement begins |
| Review | human decision authority + explicit approval | Approved | scope is approved |
| Approved | TODO owner + explicit `APROVADO` and authority guard `go` | In-Progress | folder presence alone never authorizes execution |
| In-Progress | TODO owner + required evidence/gates | Completed | closeout remains a separate governed action |
| Draft, Review, Approved, or In-Progress | human decision authority + cancellation rationale | Cancelled | preserve prior evidence and reason |
| Cancelled | human decision authority + renewed scope/approval | Draft | reopening creates a new execution cycle |

### Decisions

**Schema:** immutable ID; question; alternatives; rationale; provenance/evidence; state; named canonical targets; target-consolidation evidence; supersession link when applicable.

**Field definitions:** `Proposed` is not settled; `Accepted` is chosen but becomes effective only after named canonical targets are consolidated; `Superseded` retains history and points to its successor; `Rejected` records a declined alternative.

**Enum:** `Proposed|Accepted|Superseded|Rejected`

| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
| Proposed | human decision authority + rationale | Accepted | name every canonical target; acceptance records the choice but does not alone make it effective |
| Proposed or Accepted | human decision authority + rationale | Rejected | preserve provenance |
| Accepted | human decision authority + successor decision | Superseded | link immutable successor |

Acceptance and effectiveness are intentionally distinct without adding another state: effectiveness is the deterministic condition that every named canonical target has recorded consolidation evidence. An accepted-but-not-consolidated decision is pending effect, not a competing source of current truth. Reopening requires a new `Proposed` decision that references the earlier ID.

### Contract verification

**Schema:** contract reference; responsible module; state; evidence link; verification scope; deprecation successor when applicable.

**Field definitions:** `Not-Assessed` has no documented assessment; `Documented` is defined by its module but not verified; `Verified` has scope-specific evidence; `Deprecated` is retained only with successor/retirement guidance.

**Enum:** `Not-Assessed|Documented|Verified|Deprecated`

| From | Actor / evidence | To | Rule |
| --- | --- | --- | --- |
| Not-Assessed | module owner | Documented | module defines the contract |
| Documented | TODO owner + verification evidence | Verified | verification scope and evidence are explicit |
| Documented or Verified | module owner + successor/retirement rationale | Deprecated | index points to the maintained location |
| Verified | module owner + changed contract/evidence | Documented | re-verification is required |

Cancellation means a proposed/unpublished contract remains absent from the index; reopening returns through the responsible module, not this README.

## Historical-document exception

This lifecycle governs new or materially changed records. Historical artifacts, completed TODOs, and untouched legacy documents retain their contextual form and are excluded from current structural checks until a separately authorized material update adopts the schema. They must not be retroactively rewritten merely to look current.

## Deterministic-adoption trigger

The strategic steward opens a follow-up tactical TODO for a permanent validator when either condition occurs: more than ten live records combined across backlog, decisions, and roadmap, or the first proven recurrence of schema/field-authority drift. ST-01 reached the volume threshold with 18 live records. The implemented control under validation is [`deterministic/validate_foundation_lifecycle.py`](deterministic/validate_foundation_lifecycle.py); its bounded source graph, read-only behavior, and exit contract are defined in [`deterministic/README.md`](deterministic/README.md). CI adoption remains a separately governed decision.

## Walkthroughs

### Positive: ST-03 remains planning-only

1. Discovery evidence is retained in the feature brief and does not create execution authority.
2. The backlog records the candidate as `Selected-for-Planning` with a next gate after ST-01.
3. A strategic steward may frame a future TODO in `Draft` or `Review`.
4. No execution occurs unless that future TODO receives explicit `APROVADO` and its authority guard returns `go`.

### Negative: an active-path TODO without approval

1. A document moved into `todos/active/` may be `Draft` or `Review`.
2. Without explicit `APROVADO` and authority guard `go`, it cannot transition to `In-Progress`.
3. The missing evidence is a blocking authority violation; moving the file does not override it.
