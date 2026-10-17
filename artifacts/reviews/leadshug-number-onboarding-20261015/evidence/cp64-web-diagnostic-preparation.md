# cp64 Web-only diagnostic preparation

This is preparation only. No image tag or running service was changed. The v8 operation at `web_recreate` received HTTP 200 but failed the accepted policy byte check; its helper reported verified API, Web, origin and resource rollback. The current Web is back on the old `d11a8828…` image, and no actual direct/public response hash was preserved by v8. No causal explanation is established.

The fresh read-only snapshot confirms the owned API (`f86d76…`) is healthy on `fe5fb7…`, Web (`be3b43…`) is running on old image `d11a8828…`, and the same owned gateway (`0c48d9…`) is running on `76090a…`. The API, Web and gateway remain on the same owned network; active gateway config SHA matches the public template (`932913…`). The other four owned services also passed exact owner/project/service checks and share the same network; all five named volumes are present. The candidate tag resolves to accepted image `6f4b25…`; the service tag and rollback tag both resolve to old Web image `d11a88…`.

The existing native tunnel owner and child still match the previously accepted exact process start ticks, paths, hashes, parent relation and target `127.0.0.1:8083`. The bound host is `addressing-mar-perform-hormone.trycloudflare.com`; root/health/JS normal-TLS was last confirmed at 14:02 UTC, so a fresh proof is required before a new operation GO.

If root later authorizes, the only mutation is to retag the accepted candidate onto the Web service tag and run the canonical `docker compose … up -d --no-build --no-deps --force-recreate web` command. The plan does not rewrite the public origin or recreate API/dependencies. It captures direct Web/gateway and public Windows/WSL metadata without persisting bodies. Collect direct Web plus Windows and WSL public metadata before any rollback decision. A byte mismatch or 502 leaves the candidate provisionally active for root diagnosis; this packet authorizes no gateway test, reload, or recreation.

The Cloudflare email-obfuscation explanation remains a hypothesis. No HTML or gateway configuration change is proposed.

- Windows probe SHA-256: `13e0446d188902cde1050707b06ffbf57922476ab60a02128d12432841c84962`
- WSL probe SHA-256: `51db711ac796298bb6b274838bbfccb1b54ec72bc19d3899c2217a66faed19b5`
- Preparation JSON SHA-256: `9811ed037176e94e8f49a6e63cbc37735bf720c0d0f0e254d593b1462940c3eb`

Stopped before mutation, pending root review and a new hash-bound operation GO.
