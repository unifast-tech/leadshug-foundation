# cp63 Web-only activation preflight stop

Activation stopped before any mutation. The pinned public hostname `comments-heart-gale-muscles.trycloudflare.com` returned WSL DNS `socket.gaierror` and Windows `nslookup` returned NXDOMAIN. Windows HTTPS attempts to `/`, `/health` and the known JS asset received no HTTP response. No TLS handshake or HTTP status could be recorded. The DNS record is unavailable; whether the ephemeral hostname expired or another DNS cause applies is unverified.

The pinned Cloudflared child remained present at PID 21180 with the recorded executable path/hash and target `127.0.0.1:8083`; its parent PID 22836 remained absent as previously known. CIM rendered its creation time as `2026-10-16T23:41:33.2385740Z`, differing from the preparation record by 0.2 microseconds; both values are retained.

Before stopping, the seven owner containers and five volumes were present. The live Web container and service tag still point to the old image `sha256:d11a882849dc806e0d4728ca90a8fc8655aebc77421acefac63054b4fbb89365`; the accepted candidate `sha256:6f4b2500e02d1523f99b423a08b6a166e319d5f3246ad516ef8f4a56d30001ed` remains separately tagged. No rollback tag was created, no image tag was changed, and no Compose operation ran.

Restoration is bounded to adjudicating DNS availability for this same hostname without rotating it or replacing the pinned child, then repeating normal-TLS preflight. After transport returns, activation requires a fresh decision and the corrected Web-only Compose command. The old image remains available; rollback is not needed because activation did not begin.

Machine-readable record: `cp63-web-activation.json` SHA-256 `272da4ef2540ce9835096e1c6ebc21ec82939f78373ac126b07b7c10f13f6955`.
