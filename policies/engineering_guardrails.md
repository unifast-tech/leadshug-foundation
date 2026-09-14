# LeadsHug Engineering Guardrails
**Version:** 1.0

## Repository boundaries

- `apps/api` owns NestJS production backend, Prisma schema and migrations.
- `apps/web` owns React/Vite production client.
- `api-oficial` and `hub-whatsapp` are frozen reference systems; do not modify them from this project workflow.
- `.claude` contains project guardrails and may inform Delphi, but project-specific facts remain in this foundation.

## Backend

- Controllers translate transport contracts; domain services own business rules.
- Every business read/write carries tenant and BU scope unless an explicit internal/webhook exemption is documented.
- Provider payloads are normalized at integration adapters.
- New endpoints require module documentation, authorization behavior, tests and TODO evidence.

## Frontend

- All BFF calls go through `apps/web/src/api.ts`.
- React never accesses the database, provider APIs or secrets.
- Authorization is enforced by the backend; UI checks are usability only.

## Validation

- Unit and API e2e tests use Vitest and the local PostgreSQL container.
- Browser behavior uses Playwright against the project-owned build.
- Prisma schema changes require validation and migration evidence.
- Deploy and Railway changes require a dedicated TODO and explicit operational approval.
