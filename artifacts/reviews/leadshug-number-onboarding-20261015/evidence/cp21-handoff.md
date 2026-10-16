# cp21 runtime handoff

**Status:** STOP. Runtime and the scoped WSL environment bridge are complete; root can run independent reviews.

The canonical `bash scripts/test-channels-local.sh all` completed before the final shell-only WSLENV bridge: 21 migrations, 138 API unit tests, 282 API e2e tests, 28 Web unit tests, and 44 browser tests passed. Its raw log SHA256 is `b5466cf71c12cd882e189f8aa1ad333233edea969dfebb46b809f6eff4149725`. Freshness was recorded after API e2e and before Web build/browser, as documented; it is not labeled pre-all.

The only source delta after that run is `scripts/start-channels-local.sh`, which now carries four non-secret caller overrides through WSLENV while preserving existing WSLENV entries and modifiers. `bash -n`, `git diff --check`, and config-only validation passed with a free test port, fictitious origin, and different NODE_ENV; all three overrides were effective in Docker Compose config. No resources were created, runtime was not recreated, and `.env.testing` was unchanged. The bridge proof is `cp21-wslenv-override-proof.json`.

The final public manifest covers 214 inputs: 213 match the post-all snapshot and one approved absent API spec remains absent since cp5. The sole changed input is the start script. The eight authorized runtime-source hashes and artifact hashes are recorded in `cp21-handoff.json`.

Current API is healthy with completed local OWNER bootstrap and four Meta config values present; the Meta client reports available. Private values and identifiers are not recorded. The effective runtime is production with exact HTTPS origin, secure HttpOnly SameSite=Lax cookie, loopback-only gateway, and unofficial ceiling enabled. `PUBLIC_ORIGIN` remains blank. The API image runs Node v22.23.3 and OpenSSL 3.5.9. Evolution is pinned to `evoapicloud/evolution-api:v2.3.7@sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`; the controlled header probe used `qrcode:false`, removed both exact probe instances, and did not pair.

The temporary Quick Tunnel remains alive as PID 12615 at `https://seafood-sku-papers-contractor.trycloudflare.com`, targeting only `127.0.0.1:8083`; `/` and `/health` return 200. It is process-bound; no DNS or persistent tunnel was created. Secure-cookie and current-handle proofs are retained.

No Meta callback registration or submission, real-number onboarding, QR pairing, or fixture exposure occurred. No API local-files payload was read or hashed. Independent root review remains outstanding.
