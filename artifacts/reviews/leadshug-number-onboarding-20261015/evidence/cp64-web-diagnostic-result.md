# CP64 Web-only diagnostic result

The accepted Web candidate is provisionally active on the owned Web service. The API container remained unchanged and healthy. The operation wrapper could not format its final JSON receipt after the admitted Compose action, so its native exit code is unknown; no retry was made. A subsequent read-only service selection and inspect confirmed the exact candidate image and container.

Direct Web and gateway requests both returned HTTP 200 and the exact 12,865-byte source page (`d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d`). The public Windows identity-encoding, Windows default-encoding, and WSL probes each returned HTTP 200 with 13,396 bytes and showed Cloudflare email-obfuscation markers (`email-decode.min.js`, `/cdn-cgi/l/email-protection`, and `data-cfemail`), with one script and zero forms. All reported `no-store`, `DYNAMIC`, no content encoding, no redirect, and no Set-Cookie. Hashes are recorded in the JSON; response bodies were not saved, so no exact transformed-body diff is claimed.

This is direct evidence that the public edge response is transformed after the origin serves unchanged policy bytes, consistent with Cloudflare email obfuscation. No gateway reload, rollback, API/origin change, provider request, database operation, or tunnel change occurred. Seven owned containers and five volumes were preserved. The candidate remains provisional and is not marked ready.

The next admitted action is a candidate-only Web build with the narrowly scoped `Cache-Control: no-store, no-transform` header on `/privacidade.html`; this does not authorize activation.
