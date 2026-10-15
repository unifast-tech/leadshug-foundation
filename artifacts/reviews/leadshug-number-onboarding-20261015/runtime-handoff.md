# ST-CON-01 — local runtime handoff

Prepared by the orchestrator on 2026-10-15. This is a planned handoff within the approved TODO, not evidence that the runtime exists or is healthy. The API executor remains the sole product writer until its checkpoint is complete. Start runtime edits only after an explicit serialized handoff to `operational-devops`.

## Authority and owned files

Follow the active `TODO-leadshug-channel-connection-readiness.md`, its exact expected paths, the constitution, `dependency-readiness.md`, the environment-readiness workflow, and the DevOps profile. Use the principal checkout. No worktrees, auxiliary source copies, legacy resources, pipeline-owned gitlink writes, source pushes, Railway deployment, or CI expansion.

Runtime scope is the approved root Compose file/overlay, gateway template, two local scripts, Makefile, root README and root `.env.example`. Product code requires a separate handoff to the coder. Root owns canonical TODO/module updates; the executor may write only its designated evidence artifacts under this review folder.

## Observed starting point

- The existing root Compose supplies PostgreSQL 16, API and Web. It requires the old global `WHATSAPP_TOKEN`; remove that requirement in favor of the implemented channel-scoped credential contract.
- Existing Dockerfiles build with Node 22. The Web final image serves runtime `config.js`; `apiUrl: ""` is supported for a shared origin.
- Docker is available through Windows `docker.exe`. A WSL `/mnt/c/...` source bind resolved to an empty directory in the Windows daemon during checkpoint 1; using `wslpath -w` fixed the bind. Verify the mounted source before trusting commands or hashes.
- Checkpoint 1 used an isolated disposable PostgreSQL 16 database and a Linux named dependency volume. Do not reuse an operational database for destructive fixture cleanup. The second migration directory was renamed to match the approved `*number_onboarding*` glob; prove the final migration set on a fresh disposable database.
- Existing ignored `.env` files are private operational authority. Do not print, replace, remove, or normalize them. Do not infer that a preexisting token belongs to this test.
- Root `.gitignore` explicitly ignores `.env.local` and `.env.testing`; it does not broadly ignore `.env.*`. If the runner creates private test configuration, use an already ignored destination, first verify it is absent, refuse replacement of an existing file, and never include its contents in logs or evidence. Do not invent an unignored secret-file name.

## Required local topology

Use a separate LeadsHug test project/network/volumes. Provide the API, Web, gateway and a LeadsHug-owned Evolution with its own database/cache/persistent storage. Do not attach legacy containers or volumes. Pin Evolution to:

`evoapicloud/evolution-api:v2.3.7@sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`

The planned gateway port is 8082, configurable. Resolve conflicts before startup and record actual handles. UI, API, realtime and callbacks share the same origin. Forward the routes actually used by the implemented app, including WebSocket upgrade and original Meta webhook bytes. Do not add an interactive authentication wall to provider callbacks.

Gateway access/error logs and application errors must omit the Evolution secret path and Meta query token on success and failure. Exercise both through the actual gateway using fictitious secrets and inspect resulting logs. A safe access format alone does not prove error-log redaction.

Check the pinned provider's own QR/logging behavior before real pairing. Do not collect a real QR or credential-bearing provider response into Docker-log evidence, browser traces or screenshots. Any logging adjustment must be supported by that exact image and verified; this note does not assert that a particular provider switch exists.

Wire the final API configuration, not an independently invented env contract. Current confirmed names are `META_APP_ID`, `META_APP_SECRET`, `META_SIGNUP_CONFIG_ID`, `GRAPH_VERSION`, `WEBHOOK_VERIFY_TOKEN`, `PUBLIC_ORIGIN`, `CHANNEL_CREDENTIAL_KEY_ID` and `CHANNEL_CREDENTIAL_KEY`, plus the existing Evolution/session/module settings. Verify final names with the API handoff. Missing all Meta onboarding configuration leaves that modality unavailable; partial configuration must surface an actionable error. Never pass secrets into the browser bundle or `config.js`.

## Validation runner

The source-owned runner must use Node 22/PostgreSQL 16, explicit disposable database ownership and serial destructive suites. Include migration deploy/status, API lint/build/unit/E2E, Web build/unit and the declared Playwright projects. Browser fixtures use the real API/session/database; only the external SDK/provider port may be a test double. Preserve existing timeline behavior.

Before browser workers, record branch/base SHA plus dirty-source hashes, built asset hashes, runtime target and served asset hash comparison. Do not accept a stale container/bundle. Capture meaningful test output and exact commands, without `.env`, session cookies, QR/code/PIN/token or private key values. A successful aggregate suite does not replace the REG-SEC-01..13 behavior matrix.

## HTTPS and operator dependency

The user confirmed no Meta app/Embedded Signup or public HTTPS address yet and authorized preparing them. [Local setup](local-setup.md) records the account-side prerequisites. App creation, business eligibility/permissions and phone authorization require the user's own account; do not claim they were performed.

A temporary Quick Tunnel is an allowed test option once the isolated local gateway and served build have been verified. Do not create persistent tunnel/DNS infrastructure. Record the actual generated hostname, process/container handle, target and lifetime. An ephemeral hostname must be updated in the Meta configuration when it changes. Do not guess a public hostname or call tunnel startup proof of provider registration.

Real QR pairing, confirmed own-number identity, incoming message in the correct BU and outgoing reply received by the interlocutor remain operator/provider proof. Until those observations exist for each modality, keep their evidence rows pending and the overall TODO active.
