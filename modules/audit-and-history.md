# Module: Audit and History
**Version:** 1.0

Owns durable activity history, message auditability, exports and access to historical relationship data.

## Invariants

- History is append-oriented and is not silently discarded.
- Every record is tenant- and BU-scoped.
- Read permission is evaluated independently from write permission.
