# CP10 Web handoff

Status: Web product writes STOPPED pending the API/DevOps runner correction and a fresh serialized browser handoff. No API, runner, runtime, private environment, operational payload, Inbox, or package/lockfile source was edited. No source commit or push was made.

## Web changes

- Fixed shared timeline freshness binary hashing to compare against `HEAD` using explicit public-source pathspecs only. The API scope includes public `src`, `test`, `prisma`, `e2e`, `public`, package and build/test configuration, Docker files, and `.env.example`; private dotenv and `.local-files` are excluded. The evidence declares that omitted operational data is not a source deletion. Existing DB-family, health and served-versus-built bundle checks remain.
- Kept changed-source inventories scoped to relevant public source/configuration, with staged, unstaged, untracked, deletion status and read errors handled fail-closed. The number-onboarding helper preserves that boundary.
- Enabled “Ignorar resposta desta janela” while its popup operation owns pending state; invoking it invalidates ownership so later SDK callbacks cannot authorize.
- Unnamed WABAs now display `Conta <public WABA ID>`. Browser coverage supplies two null-name WABAs, asserts neither is auto-selected, and chooses the second explicitly.
- Added browser sources for SDK load retry, popup cancel/error/abandon, late callbacks after closing and changing BU, and new-BU idempotency retry following a deliberately dropped client response. Existing FRC 20×5 barriers, official cursor selection, role denial, ambiguous provider result, QR/identity/receipt and echo-inside-send tests remain.

No BFF response is mocked. Only the external SDK/provider fixture is faked; the idempotency retry discards the actual `route.fetch()` response after the real server has processed it. Registration-flow trace, screenshots and video remain disabled.

## Validation

The source-owned `bash scripts/test-channels-local.sh web` passed in the isolated Node 22.23.3 / OpenSSL 3.0.22 runner: production Web build passed and 27 unit tests passed across five files. `git diff --check` passed. Raw output: `cp10-web-validation.log` (SHA-256 `df738f11839ef9e8fcf3723d9576efc76977d639a680348e17cda556b5f8bba8`). The locked installs reported dependency audit advisories; no upgrade or audit fix was applied.

The serialized `bash scripts/test-channels-local.sh browser` run applied all 21 migrations and built Web, but Playwright stopped before workers/global setup. The API fixture process failed to load `../dist/domain/channels/channel-credential-crypto.js` from `test/timeline-fixtures.cjs` because the isolated API workspace had no compiled `dist`. Therefore no Playwright test ran, no pre-worker freshness attestation was emitted, and FRC/PCV results remain pending. Raw output: `cp10-browser-validation.log` (SHA-256 `2572d630a3a775851fe395daa729df4afa9db2d9858d5115ea4cf652ccc34de6`). This API fixture/build-order issue was reported to root and not changed by Web.

The runner tore down the isolated `leadshug_channels_validation` resources. Existing unrelated operator runtime containers were not touched.

## Source hashes and scope

`cp10-web-source-hashes.sha256` lists all 13 changed Web source files; `sha256sum -c` passed. Files: `.dockerignore`, `e2e/timeline-freshness.ts`, `e2e/number-onboarding-freshness.ts`, `e2e/number-onboarding.spec.ts`, `playwright.config.ts`, `src/api.ts`, `src/api.spec.ts`, `src/telas/Numeros.tsx`, `src/cadastroNumero.ts`, `src/cadastroNumero.spec.ts`, `src/cadastroNumero.lifecycle.ts`, `src/cadastroNumero.lifecycle.spec.ts`, and `src/componentes/CadastroNumero.tsx`.

Await explicit Web writer handoff after the API fixture startup/build-order correction. Do not treat the prepared browser sources as executed evidence.
