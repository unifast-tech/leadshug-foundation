# LeadsHug Query Path Guardrails
**Version:** 1.0

- Lookups by unique ID, slug or external key use query paths dedicated to that key.
- Production request paths must not load unbounded collections to filter, sort, paginate or resolve identity in memory.
- Pagination, filtering, sorting and search belong to PostgreSQL/Prisma query contracts.
- `fetchAll`, page loops and local collection scans are forbidden in interactive runtime paths.
- Jobs, migrations, exports and explicit reconciliation flows may iterate in chunks when documented.
- Every query touching relationship data must carry the tenant/account/BU scope at the repository boundary.
- Missing query contracts must be implemented at the source; temporary fallback scans are not permitted.
