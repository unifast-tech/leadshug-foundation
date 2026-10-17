# cp64 Web diagnostic v3 preflight

At 14:25 UTC, fresh read-only preflight passed. The API (`f86d…`) remains healthy on `fe5fb7…`; the Web (`be3b…`) remains on old image `d11a88…`; the candidate and rollback tags still resolve to `6f4b25…` and `d11a88…`. All seven services passed owner/project/service/image/state checks on the same owned network, and all five expected volumes exist. Gateway identity/image are unchanged; active config SHA equals the public template (`932913…`).

The exact native supervisor/child start ticks, parents, paths, hashes, and target `127.0.0.1:8083` still match. Fresh Windows and WSL normal-TLS requests to `addressing-mar-perform-hormone.trycloudflare.com` returned 200 for `/`, `/health`, and the expected JS. None redirected or set cookies; the JS SHA matched `d143436…`.

Both new Windows probe copies pass PowerShell parsing and dummy `HttpResponseMessage` tests. `Cache-Control` is sourced only from `response.Headers`; the unnecessary fallback is removed and `MaxResponseContentBufferSize` is 250,000 bytes. The identity-mode and default-mode copies differ by only the `Accept-Encoding: identity` request-header line. The exact previous regex-fix characterization is corrected in a separate artifact; originals remain untouched.

No policy request, image tag, service, origin, tunnel, private file, database, or provider state changed. Root acceptance and operation authority remain pending.

- Identity probe SHA-256: `440c43d08f73bf6c6f5d7aa82472f5128cbf1278034e104015ba6160632a1282`
- Default probe SHA-256: `58ddf7b1a6d3c4fcf3104bd7224b0c1b31abb4884804d122c6d831a40808d6fe`
- WSL probe SHA-256: `d1b2ff3cb2ebec09a00946128e476f2f53a0bb5551dfc4a7be7340e0cad06bea`
- Preflight JSON SHA-256: `c1b17674cf5e59611596930d3e34cee191f83a0019d26bb6d678daab3f6acd74`
