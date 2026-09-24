# LeadsHug Decisions

**Version:** 1.0

This index is the canonical home for durable decision rationale, provenance, alternatives, and supersession history. It is not the current truth for a module, roadmap, constitution, candidate, or TODO.

## Decision record rule

New decision records use an immutable `DEC-<slug>` ID and identify the question, alternatives, rationale, evidence/provenance, state, and named canonical targets. Lifecycle state definitions and transitions live in [`../evolution_lifecycle.md`](../evolution_lifecycle.md).

`## Records` indexes every current root-level decision record in this directory exactly once; historical and completed material is not admitted as a current decision owner. Each indexed record has one nonempty file-level `Provenance` field, and its decision table keeps one positional target-consolidation-evidence segment per named canonical target.

An `Accepted` decision is effective only after its named canonical targets are consolidated. Until then it records a chosen direction but does not override those targets. A superseded decision retains its provenance and links its immutable successor.

## Records

- [ST-01 Foundation lifecycle decisions](ST-01-foundation-lifecycle-decisions.md) — eleven accepted decisions with alternatives, rationale, provenance, named targets, and target-consolidation evidence.
