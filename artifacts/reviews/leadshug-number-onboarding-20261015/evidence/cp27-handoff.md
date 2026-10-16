# CP27 validation handoff

Canonical `bash scripts/test-channels-local.sh all` completed once with exit code 0. The suite passed 499 checks: 138 API unit, 286 API/PostgreSQL E2E, 28 Web unit, and 47 browser tests; all 22 migrations applied.

The complete public-input inventory contains 230 entries across 228 unique paths. Before and after manifests are identical; source heads did not move. No private dotenv or `.local-files` payload was read or hashed.

Freshness attestation ran before browser workers. Disposable database/API/fixture/preview health was 200, with 22 migrations. The served Web JavaScript SHA-256 matches the built `dist` bundle. The operator runtime was not rebuilt, recreated, or changed.

Artifacts and SHA-256 values are recorded in `cp27-handoff.json`. The full runner output is retained byte-for-byte in `cp27-final-all.log`.

Limits: this proves the bounded local PostgreSQL/fake-provider/browser validation only; it is not a production capacity or provider-delivery guarantee. No production OAuth, QR pairing, or real-number inbound/outbound operation was performed.
