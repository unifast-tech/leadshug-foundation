# cp25 origin precedence and runtime handoff

**Status:** targeted GREEN; STOP for independent review.

Changed only `scripts/start-channels-local.sh` (`af8b59b851f8fc135451b8ba9d112b142743497ca98007644069ffbe335bdc80` → `a8b7790f68da1154a85eb3108ac7b1365e9b1d881af21fe089620db881377de5`). The complete 230-reference public manifest has 229 unchanged references and one changed script reference; branch heads stayed fixed. No private or operational payload path was read or hashed.

The config-only matrix passed for actual saved HTTPS origin/port, explicit caller origin/port, nondefault synthetic saved-file origin and port, Compose fallback, WSLENV sentinels with modifiers, and invalid ports. The fake-input case rewrote only `--env-file` to a public synthetic fixture and forwarded to real Windows Docker Compose. No runtime resources were created by config tests.

Only the API container was recreated with `--no-deps --no-build` using the existing validated image. API health is green; all other owned container IDs, database state and Evolution services were preserved. HTTPS health/root/login/me returned 200 with Secure, HttpOnly, SameSite=Lax host-only cookie; exact-origin CORS preflight returned 204 with credentials and expected headers/methods. The capability route remains 409 `ONBOARDING_PENDENTE`.

Private Meta/OWNER/keys/token/ACL values were not changed or emitted. Safe in-memory log scans found no known private-value matches; effective Nginx config still has global `access_log off` and the allowlisted safe server format. No full `all` rerun was needed: cp24's 498-test run and 22-migration evidence remain immutable; cp25 changes one operator wrapper path only and validates its config/runtime effect directly.

Root separately retained and verified the actual cp24 pre-worker/browser attestations. Messages subscription and normal OWNER Wizard completion remain pending; no real OAuth, pairing, QR, IN/OUT, module or billing action occurred.

## Evidence SHA-256

- `cp25-config-precedence-proof.json` — `8f280a20cf48e3947b43382aa3f6b7a9ec29204bcf94656a7b03f79a0a003653`
- `cp25-before-api-recreate.json` — `7046fb6145ef120f94ce3da7f9e19207ff31402940e547a92d4ab93d8e148338`
- `cp25-https-runtime-proof.json` — `8b8a0041162ed4404b74bb6c90f75771e900eaad2c225dca37bdc6ace4c3c6c4`
- `cp25-after-api-recreate-runtime-state.json` — `797b3528f0f17e0dec116ea5d315642c8e7c2be7dbf265baa290665ab10b2d4d`
- `cp25-log-hygiene-scan.json` — `f6393f8a42e31a990d916051bc3a70c224d05139faaa92b10a1c42b45402733e`
- `cp25-source-manifest-before.json` — `1667735c749f873f9ffca59dab22cf5e2484f2f850efcb6fdcb8a8be6c18aa5b`
- `cp25-source-manifest-after.json` — `43cd84f4e3d14e40ecc5e7b546b732273a79744a558278c98b6feeb9dfc3fd44`
- `cp25-source-delta-comparison.json` — `e550f67a74967b2d2777b5f9e9ea047b00363fea7e8064b4085ca31e53a367b5`
