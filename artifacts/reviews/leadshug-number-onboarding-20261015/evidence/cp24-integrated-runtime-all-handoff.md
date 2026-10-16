# cp24 integrated runtime and all handoff

**Status:** GREEN with one authorized origin-precedence follow-up pending root activation.

Canonical operator update completed; API migrations applied: 22. Canonical `all` exited 0: API 138 unit + 286 PostgreSQL, Web 28 unit, browser 46 (498 total). Raw log SHA-256: `c7f2a6c70384bea881ba5106787b4a1911e8fdc763760e80a8a8eb34faa73277`.

Public source manifest: 230 entries / 228 unique paths, pre/post identical; branch heads unchanged. The only missing entry is the approved historical deletion `api-app/src/domain/channels/channels.service.spec.ts`. No private or operational payload paths were read or hashed.

Runtime API/Web/gateway images: `sha256:c2e8d62bde2c85305deb9d72569f773072e77292465e09ed7283051b40ed4f4f`, `sha256:d11a882849dc806e0d4728ca90a8fc8655aebc77421acefac63054b4fbb89365`, `sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109`. Evolution remains pinned v2.3.7. All owned services running; persistent DB state preserved.

HTTPS root/login/me returned 200; cookie is Secure, HttpOnly, SameSite=Lax and host-only. Capability response remains 409 `ONBOARDING_PENDENTE`; no module/billing bypass. The saved HTTPS origin is present and matches current tunnel, but effective API `WEB_ORIGIN` remains loopback HTTP because wrapper default shadows saved origin. Same-origin HTTPS works. Separate bounded wrapper correction is pending root activation; no config was changed here.

Production image `npm audit --omit=dev` reports 8 findings (1 critical, 6 high, 1 moderate); no upgrades or lockfile edits. Known private values were scanned in-memory against operator, validation, API, gateway and Evolution logs; no matches. Logs were not persisted by the scan.

Meta allowlists are saved and callback verified. Messages subscription and normal owner Wizard completion remain unconfirmed. No real OAuth, QR, pairing, IN/OUT, Meta submission, or module/billing mutation occurred.

Freshness limitation: no dedicated pre-worker timestamped attestation was captured before the canonical browser worker. The post-run HTTPS served JavaScript hash matches the Web image content and the validation log records a successful Web build before Playwright, but this is not represented as a pre-worker proof.

## Evidence SHA-256

- `cp24-source-manifest-before.json` — `60b0af3ef1140ce3a8b3a351ffdc04b4ac3df86e4835197a3605e3ca7521abe2`
- `cp24-source-manifest-after.json` — `1667735c749f873f9ffca59dab22cf5e2484f2f850efcb6fdcb8a8be6c18aa5b`
- `cp24-source-manifest-comparison.json` — `052fb37e6673fbe5aadd53d88c0844a07d312c6848fcefbfed48c77a9f274e49`
- `cp24-operator-up.log` — `6226220b62fb18d3ca5262a7a90b4ac2ec044e8894b494fae5fafe489bd80856`
- `cp24-final-all.log` — `c7f2a6c70384bea881ba5106787b4a1911e8fdc763760e80a8a8eb34faa73277`
- `cp24-operator-runtime-proof.json` — `fc1cd11254e731837e27bc58fe3fbea01d2f746d3c52fb79dfe3151b08006bf3`
- `cp24-served-bundle-proof.json` — `522e25a8047981759137b606cbd3449ebd2b7318a40f9006d05f3f6b46b77ae0`
- `cp24-https-session-capability-proof.json` — `7b6946b0bfe9530d7f7668d7ea8fee66f86da653b2ab31352e91ca288bae0116`
- `cp24-origin-precedence-diagnostic.json` — `a1455295870e2710009cdc23a5c3a3e478180e8e3f4d7a9d759beb89ed23a85f`
- `cp24-log-hygiene-scan.json` — `63601615cf9b4f17983ea024c213cce44c8bdecb5d8e331d966be3806d1c944f`
- `cp24-production-image-npm-audit.json` — `7f6bc7ab3cf20edfcfb2de6bd1753e56ebb0bc9153c0e5a62f02d59332511366`
