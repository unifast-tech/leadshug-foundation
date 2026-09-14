# LeadsHug Validation and Evidence Policy
**Version:** 1.0

## Required evidence by change

| Change | Required proof |
| --- | --- |
| NestJS service/controller | unit or API integration test plus contract review |
| Prisma schema/migration | `prisma validate`, migration review and scoped API test |
| Tenant/BU access | cross-tenant negative test and positive grant test |
| Webhook/provider adapter | idempotency test and provider payload contract test |
| React route/form/mutation | Playwright browser flow against the built client |
| Docker/runtime configuration | local compose smoke and configuration review |
| Railway deployment | explicit operational TODO and stage/runtime evidence |

## Canonical commands

Use the project `Taskfile.yml` as the command entrypoint. When a target does not exist, use the package-local
commands from `apps/api/package.json` or `apps/web/package.json` and record the exact command in the TODO.

## Evidence rules

- A green aggregate suite is not enough; evidence must prove the named criterion.
- Mock-only tests do not prove PostgreSQL query scope or provider behavior.
- Browser evidence must use the current built client, not stale generated output.
- Runtime and deployment evidence must identify the environment and commit.
- A structure-only documentation change may use a review/doc evidence waiver when recorded in the TODO.

## TODO relationship

Every development task must link its evidence rows to a governing TODO. The TODO remains active until all
Definition of Done and Validation Steps rows have criterion-specific evidence.
