# cp64 independent public DNS diagnosis

Cloudflare and Google DNS-over-HTTPS were queried over normally validated HTTPS for A, AAAA and CNAME records of `comments-heart-gale-muscles.trycloudflare.com`. Every query returned HTTPS 200 with DNS RCODE 3 (NXDOMAIN), zero answers, one authority record containing SOA. No auth, cookies or redirects were used. This establishes public DNS absence, not merely a local resolver failure. The reason the ephemeral hostname is absent remains unknown.

The exact known Cloudflared process was checked with a native Windows process handle and native `StartTime` ticks, plus executable path/hash, parent PID and an in-memory target boolean. PID 21180 has start time `2026-10-16T23:41:33.2385742Z`, native ticks `639277908932385742`, exactly matching the pinned cp46 timestamp; executable hash and target `127.0.0.1:8083` also match. Its parent PID 22836 remains absent, as previously known. Raw argv was not emitted or persisted. The guarded stop script was not run or bypassed.

All seven owner containers and five volumes remain present. Live Web still uses old image `sha256:d11a882849dc806e0d4728ca90a8fc8655aebc77421acefac63054b4fbb89365`; accepted candidate `sha256:6f4b2500e02d1523f99b423a08b6a166e319d5f3246ad516ef8f4a56d30001ed` remains separately tagged. No activation or tunnel recovery occurred.

Recommendation: use the separately planned, already-authorized owned local test setup to recover/diagnose the same host if possible, then recheck public DoH and normal-TLS root/health/JS before any activation. This read-only task did not apply DNS overrides, replace the child process, bypass the guarded stop script or rotate the hostname.

Machine-readable evidence: `cp64-dns-diagnosis.json`.
