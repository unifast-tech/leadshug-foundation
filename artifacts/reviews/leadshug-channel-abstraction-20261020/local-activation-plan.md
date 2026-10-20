# ST-CON-06 — bounded local activation preparation

Derived preparation for approved Ordered Step6, not execution evidence or a new deployment authorization. Final frozen all and review disposition must be evaluated before activation. One product/runtime writer remains responsible. API/Web only in the existing `leadshug_channels_local` project; no Railway/code push, private dotenv read/write, database reset/migration, credential rotation or provider lifecycle mutation.

## Readiness and source inputs

Resolve exact running service names/IDs/images and health by project labels. Do not enumerate process argv or container environment to output. Confirm the current gateway on127.0.0.1:8083 and preserve the five non-target containers, network and named storage volumes. The preliminary readback is historical by activation time and must be refreshed.

Build API/Web using positive input archives streamed to Windows Docker, not either application root as a build context. API input roots: Dockerfile, package.json/package-lock.json, prisma, src, tsconfig.json/tsconfig.build.json/nest-cli.json, docker/entrypoint.sh. Web input roots: Dockerfile, package.json/package-lock.json, index.html, tsconfig.json/vite.config.ts, src, public, nginx/default.conf.template, docker/40-config-js.sh. Verify actual Dockerfile COPY requirements first. Archive symlinks as symlinks; never dereference or add another root. No .git, dotenv, local data, node_modules or prior dist is input. Input hashes and before/after source manifests must match the validated/reviewed candidate. Build artifacts are not auxiliary writable checkouts.

Tag local images with a source-manifest identity and record image IDs plus actual Node/compiler outputs. Keep prior images for rollback. No dependency/schema change is authorized. Existing Dockerfiles/package locks govern image builds; validation Node22.23.3/PG16 and actual image runtime versions must be distinguished honestly.

## Preserve effective runtime configuration

Avoid the normal env-file-reading startup wrapper. If existing effective environment is required to recreate the two containers, obtain only their exact Config.Env values programmatically into process memory, with no printing, file serialization, command-line secret arguments or traceback of values. Preserve values exactly; do not use this as permission to change private configuration. Construct a literal Compose JSON fragment in memory and pass via stdin, with an explicit null env-file, so Compose does not discover private dotenv. No interpolation placeholders may be introduced. Only API/Web service definitions belong in this fragment, with their existing network aliases, restart/health behavior and external named upload volume. Verify resolved names against public Compose topology; refuse unknown mount/network/port arrangements.

Escape every literal dollar in copied values for the Compose interpolation parser and verify effective values in memory after recreation; do not print their bytes or hashes. Refuse any mismatch. Run only the explicit existing-project API/Web recreation with no dependency startup, no build and no orphan removal. Do not touch other projects or remove volumes. Keep the in-memory prior image references for rollback if either service fails health. If gateway DNS needs refresh after container replacement, a tested Nginx reload is bounded integration work; no unrelated gateway/source/config edits are authorized.

This procedure preserves operational values without reading `.env` or `.env.testing`. It never needs a path, directory listing, metadata read, content read or mount from `api-app/.local-files`. Existing named upload storage is a distinct declared Docker volume and is not a source/build input.

## Runtime freshness and access

After API health, compare exact changed public compiled-module hashes in the running API with the new built image. For Web compare index/asset names and hashes from image and gateway-served bytes. Record source→image→container→HTTP provenance separately; build success alone is insufficient. Confirm unchanged IDs for PostgreSQL, Evolution/PostgreSQL, Redis and gateway unless a separately recorded bounded reload was needed. Do not emit conversations, phone numbers or credentials while checking health/configuration.

Restore one exact-owned native Quick Tunnel to the operator gateway, using the previously reviewed cloudflared/supervisor binary hashes and empty configuration, a fresh runtime-state directory and bounded exact-executable process checks. Do not adopt or kill unknown processes. Historical cp73 helper reads no dotenv but hard-codes a used runtime directory; inspect and adapt only that lifecycle bookkeeping before reuse, preserving provenance checks. Verify current DNS, ordinary TLS, health, privacy page and callback reachability before presenting a public URL. Do not tunnel validation ports3100/3101/4173.

Ask the operator to update the Meta callback and privacy URL to the verified current hostname, retaining `messages` and the same local verification token. OAuth/SDK domains need updating only if new authorization is actually needed; existing-channel IN/OUT does not authorize repeating registration. For the unofficial binding preserve its private Compose callback; inspect only safe URL scheme/host/path metadata if necessary, without a secret or provider mutation.

## Physical proof and close condition

Once current access and callback are confirmed, operator performs one new real IN and one LeadsHug OUT on each existing official/unofficial test binding, reporting only results. Preserve current conversations and credentials. New proof must bind the activated source/image/runtime; CP108, old browser results and provider fixtures do not replace it. Record remaining limitations and continue final assurance/closeout. Never claim production, continuous availability, external exactly-once or a new channel network from this proof.
