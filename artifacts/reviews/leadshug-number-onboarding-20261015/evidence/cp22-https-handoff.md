# cp22 HTTPS recovery handoff

**Status:** STOP. HTTPS has been restored on the existing cp21 runtime; root can independently health-check and continue Meta setup.

Current temporary HTTPS origin: **https://mistress-spencer-mozilla-sciences.trycloudflare.com**. The Quick Tunnel points only to the gateway bound on `127.0.0.1:8083`. DNS resolves in WSL and Windows; root and `/health` returned 200. It remains process-bound and has no DNS record, named tunnel, account, or persistent tunnel resource.

A detached Windows-owned `wsl.exe` handle is PID `24396` (WSL distro `Ubuntu`), launched by PID `3468`, which has exited while the WSL handle stayed alive. Its WSL supervisor PID is `28234` and cloudflared PID is `28236`; both were alive at final capture. Cloudflared executable SHA256 is `d33ff2d14475178d2012c2c56beba87389ac5ded27649519f198a7d3134a99db`, version 2026.10.0. Exact stop command, guarded by the WSL PID's executable path, is in `cp22-https-lifecycle.json`; it was not run.

Tunnel output is drained through a filter that records only one startup hostname. Raw stdout/stderr and request output, query strings, codes, tokens, and log lines are not persisted. The first attempt was abandoned before adoption after the initial filter closed its output pipe; early EOF/SIGPIPE is the likely cause, not independently confirmed. Its hostname is omitted from versioned evidence. The second attempt keeps draining both streams and has remained alive after its launching PowerShell process exited.

To align the existing API image with the new temporary origin, only `CHANNELS_LOCAL_ORIGIN` was changed in-place in ignored `.env.testing`, with pre-write byte/stat comparison and inode preservation. The restricted Windows ACL remains protected. The API container alone was force-recreated with `--no-deps --no-build`; its image ID is unchanged (`sha256:96e9c741…`). Web, gateway, operator database and Evolution remain the existing cp21 containers; no build or migration ran. `NODE_ENV=production`, exact HTTPS `WEB_ORIGIN`, blank `PUBLIC_ORIGIN`, four nonempty local Meta fields, and valid credential-encryption prerequisites were confirmed as booleans without emitting private values.

HTTPS login returned 200 with `Secure; HttpOnly; SameSite=Lax; Path=/` and no Domain attribute. Same-origin `/api/bff/me` returned 200; CORS returned the exact origin and credentials enabled. An authenticated BFF capability check returned 409 `ONBOARDING_PENDENTE`; installation-level prerequisites do not establish the tenant's actual contracted module. No module, billing or onboarding state was changed.

The operator runtime remains the cp21 image with 21 migrations applied. API cp22 validation reached 22 migrations, lint/build and 138 unit tests, while PostgreSQL tests ended 284/286 with two new harness errors; that validation STOP source was not built or deployed.

Four locally saved Meta config fields are present, but OAuth/partner authorization is unproven. The user confirmed Meta callback and verify-token fields are empty. No callback registration/submission, real number, QR, pairing, WABA operation, or external Meta action occurred. Root should now perform the grouped allowlist update using the current origin, then handle the normal existing-product owner onboarding.
