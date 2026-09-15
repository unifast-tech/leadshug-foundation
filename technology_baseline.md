# LeadsHug technology baseline

**Status:** maintained current-state navigation, verified from local repository evidence on 2026-09-15.
It describes the approved target architecture for new LeadsHug work. It does **not** claim that a
deployment, provider, or production runtime is healthy.

## Authorities and target

- **Product and governance authority:** `leadshug-foundation`.
- **Engineering-method authority:** `leadshug-engineering`.
- **Canonical product target:** `LeadsHug/apps/api` and `LeadsHug/apps/web`.
- **Compatibility note:** inside the product checkout, `delphi-ai/` and
  `foundation_documentation/` are native compatibility links to the two repositories above. They
  remain valid executable paths but are not authority names.

## Verified technology baseline

| Layer | Current target | Direct local evidence |
| --- | --- | --- |
| API | NestJS 11, TypeScript, Node.js 22+ | [`../LeadsHug/apps/api/package.json`](../LeadsHug/apps/api/package.json) |
| Data | PostgreSQL 16 through Prisma 6; versioned Prisma migrations | [`../LeadsHug/docker-compose.yml`](../LeadsHug/docker-compose.yml), [`../LeadsHug/apps/api/package.json`](../LeadsHug/apps/api/package.json), [ADR-0003](../LeadsHug/docs/adr/0003-postgres-unico-com-prisma.md) |
| Web | React 18, Vite 5 and TypeScript | [`../LeadsHug/apps/web/package.json`](../LeadsHug/apps/web/package.json), [ADR-0006](../LeadsHug/docs/adr/0006-quatro-superficies-de-entrada-e-front-react-separado.md) |
| Runtime and delivery | Docker local/deploy profile; Railway target topology with separate API and Web definitions | [`../LeadsHug/docker-compose.yml`](../LeadsHug/docker-compose.yml), [`../LeadsHug/apps/api/railway.json`](../LeadsHug/apps/api/railway.json), [`../LeadsHug/apps/web/railway.json`](../LeadsHug/apps/web/railway.json), [ADR-0002](../LeadsHug/docs/adr/0002-railway-como-infraestrutura-unica-e-nestjs-como-base.md), [ADR-0015](../LeadsHug/docs/adr/0015-o-front-e-servico-proprio-sob-o-mesmo-dominio.md) |
| Quality gates | Vitest for API/Web and Playwright for browser flows | [`../LeadsHug/apps/api/package.json`](../LeadsHug/apps/api/package.json), [`../LeadsHug/apps/web/package.json`](../LeadsHug/apps/web/package.json), [`../leadshug-engineering/main_instructions.md`](../leadshug-engineering/main_instructions.md) |

## Integration boundary

The target product owns tenancy, permissions, contacts, conversations, audit and channel policy.
Meta Cloud API, the Evolution/Baileys unofficial-channel path, Typebot Cloud and transactional email
are provider adapters; none is an authority or a runtime dependency on a legacy repository. The
target architecture and its four entry surfaces are defined by [ADR-0006](../LeadsHug/docs/adr/0006-quatro-superficies-de-entrada-e-front-react-separado.md).

Any change to a provider, schema, runtime topology or deployment still requires its own approved TODO;
this document is a navigation baseline, not an authorization to deploy or alter configuration.

## Boundaries and history

- The canonical target/legacy classification is in [architecture truth and legacy boundaries](artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md).
- `Central-Whatsapp` remains an independent legacy/reference source under its [explicit policy](policies/central_whatsapp_independent_legacy_policy.md).
- Historical product documents, accepted ADR text, completed TODOs and migration evidence are not
  rewritten by this baseline. Where their time horizon differs, this document and the architecture
  truth matrix are the maintained navigation layer.
