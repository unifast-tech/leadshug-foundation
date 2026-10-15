# ST-CON-01 — local runtime handoff

Prepared by the orchestrator on 2026-10-15. This is a planned handoff within the approved TODO, not evidence that the runtime exists or is healthy. The API executor remains the sole product writer until its checkpoint is complete. Start runtime edits only after an explicit serialized handoff to `operational-devops`.

## Authority and owned files

Follow the active `TODO-leadshug-channel-connection-readiness.md`, its exact expected paths, the constitution, `dependency-readiness.md`, the environment-readiness workflow, and the DevOps profile. Use the principal checkout. No worktrees, auxiliary source copies, legacy resources, pipeline-owned gitlink writes, source pushes, Railway deployment, or CI expansion.

Runtime scope is the approved root Compose file/overlay, gateway template, two local scripts, Makefile, root README and root `.env.example`. Product code requires a separate handoff to the coder. Root owns canonical TODO/module updates; the executor may write only its designated evidence artifacts under this review folder.

## Observed starting point

- The existing root Compose supplies PostgreSQL 16, API and Web. It requires the old global `WHATSAPP_TOKEN`; remove that requirement in favor of the implemented channel-scoped credential contract.
- Existing Dockerfiles build with Node 22 and install OpenSSL for Prisma. Checkpoint2 tests passed on Node22.23.3-slim but emitted OpenSSL detection warnings; the final source-owned runner must establish a supported explicit OpenSSL setup and regenerate Prisma before validating its runtime. The Web final image serves runtime `config.js`; `apiUrl: ""` is supported for a shared origin.
- Docker is available through Windows `docker.exe`. A WSL `/mnt/c/...` source bind resolved to an empty directory in the Windows daemon during checkpoint 1; using `wslpath -w` fixed the bind. Verify the mounted source before trusting commands or hashes.
- Checkpoint 1 used an isolated disposable PostgreSQL 16 database and a Linux named dependency volume. Do not reuse an operational database for destructive fixture cleanup. The second migration directory was renamed to match the approved `*number_onboarding*` glob; prove the final migration set on a fresh disposable database.
- Existing ignored `.env` files are private operational authority. Do not print, replace, remove, or normalize them. Do not infer that a preexisting token belongs to this test.
- Root `.gitignore` explicitly ignores `.env.local` and `.env.testing`; it does not broadly ignore `.env.*`. If the runner creates private test configuration, use an already ignored destination, first verify it is absent, refuse replacement of an existing file, and never include its contents in logs or evidence. Do not invent an unignored secret-file name.

## Required local topology

Use two separately owned namespaces: actual operator/provider testing uses Compose project `leadshug_channels_local` and database `leadshug_channels_local`; destructive automated validation uses project `leadshug_channels_validation` and database `leadshug_timeline_channels_ci`. These are new planned resources, not authority to adopt existing resources with matching names. Verify ownership and absence before creation, and record actual handles. Each has separate networks/volumes. The actual database is deliberately outside the fixture reset allowlist; never reset a device-paired runtime through automated fixtures.

Provide the actual runtime with API, Web, gateway and a LeadsHug-owned Evolution with its own database/cache/persistent storage. Keep browser fixture/seed servers inside the validation network, never behind the actual public gateway or tunnel. Validation fake configuration must be independent of the operator's ignored private `.env.testing`. A full source bind must not let Prisma/Vite automatically ingest private submodule `.env` files: mask such inputs inside validation containers with nonsecret fixture/empty files, without reading or changing private host files. Check production build `.dockerignore` coverage as well. Do not attach legacy containers or volumes. Pin Evolution to:

`evoapicloud/evolution-api:v2.3.7@sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`

The initial planned gateway port8082 was found occupied by another project's listener during read-only preflight;3000 and55433 are also occupied. Preserve those resources. Use configurable default8083 for the isolated gateway only after verifying it is free immediately before startup, and record actual handles. The two existing disposable onboarding PG containers are separate checkpoint resources, not permission to attach other systems. UI, API, realtime and callbacks share the same origin. Forward the routes actually used by the implemented app, including WebSocket upgrade and original Meta webhook bytes. Do not add an interactive authentication wall to provider callbacks.

Gateway access/error logs and application errors must omit secret-bearing request values on success and failure. Exercise header-authenticated Evolution callbacks and Meta query-token verification through the actual gateway using fictitious markers; include auth failure, upstream failure and malformed requests rejected before location selection. Inspect resulting logs. A safe access format or location-only error-log policy alone does not prove parser-level error-log redaction. Preserve useful aggregate request/status/upstream diagnostics without secret-bearing URIs or headers.

Pinned-source preflight confirmed QR terminal rendering goes through the LOG level and full webhook body logging requires WEBHOOKS. Use explicit LOG_LEVEL=ERROR,WARN, excluding LOG/WEBHOOKS, and verify the pinned runtime before real pairing. Callback failures still log the configured URL at ERROR; therefore path-secret authentication would leak at the provider even with a safe gateway. The already conditional header alternative is now source-confirmed and selected: callback URL `/webhooks/evolution` without secret, per-instance `headers: {"x-leadshug-webhook-secret": <private installation secret>}`. API-owned wiring/tests must land before this runtime is activated, and actual pinned-provider callback plus failure logs must prove it. No real QR or credential-bearing provider response may enter Docker-log evidence, browser traces or screenshots. Preserve useful ERROR/WARN diagnostics rather than hiding all provider errors.

Wire the final API configuration, not an independently invented env contract. Current confirmed names are `META_APP_ID`, `META_APP_SECRET`, `META_SIGNUP_CONFIG_ID`, `GRAPH_VERSION`, `WEBHOOK_VERIFY_TOKEN`, `PUBLIC_ORIGIN`, `CHANNEL_CREDENTIAL_KEY_ID` and `CHANNEL_CREDENTIAL_KEY`, plus the existing Evolution/session/module settings. Verify final names with the API handoff. Missing all Meta onboarding configuration leaves that modality unavailable; partial configuration must surface an actionable error. Never pass secrets into the browser bundle or `config.js`.

## Validation runner

The source-owned runner must use Node 22/PostgreSQL 16, explicit disposable database ownership and serial destructive suites. Include migration deploy/status, API lint/build/unit/E2E, Web build/unit and the declared Playwright projects. Browser fixtures use the real API/session/database; only the external SDK/provider port may be a test double. Preserve existing timeline behavior.

Before browser workers, record branch/base SHA plus dirty-source hashes, built asset hashes, runtime target and served asset hash comparison. Do not accept a stale container/bundle. Capture meaningful test output and exact commands, without `.env`, session cookies, QR/code/PIN/token or private key values. A successful aggregate suite does not replace the REG-SEC-01..13 behavior matrix.

## HTTPS and operator dependency

The user has now created a Meta app with WhatsApp and obtained the sandbox account; Embedded Signup configuration and public HTTPS remain unconfirmed. [Local setup](local-setup.md) records the account-side prerequisites and observed dashboard. Business eligibility/permissions and phone authorization require the user's own account; do not infer them from app creation or sandbox availability.

A temporary Quick Tunnel is an allowed test option once the isolated local gateway and served build have been verified. Do not create persistent tunnel/DNS infrastructure. Record the actual generated hostname, process/container handle, target and lifetime. An ephemeral hostname must be updated in the Meta configuration when it changes. Do not guess a public hostname or call tunnel startup proof of provider registration.

Real QR pairing, confirmed own-number identity, incoming message in the correct BU and outgoing reply received by the interlocutor remain operator/provider proof. Until those observations exist for each modality, keep their evidence rows pending and the overall TODO active.
