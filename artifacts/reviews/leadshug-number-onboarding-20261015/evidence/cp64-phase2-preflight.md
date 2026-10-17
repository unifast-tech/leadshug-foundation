# cp64 phase 2 fresh preflight

Observed 2026-10-17T13:56:07.112728+00:00. This is read-only, not operation authority: `rootAccepted=false`, `operationAuthority=PENDING`. It is bound to v7 `5e31094320fd2b45392a8436223517ac124d837062530190cab14adec8accb47` and fresh final review `81aee5d1342852a4bda7f18afbbd63f3ff0fadadcf58c40d4eaf809a657ffe4d`.

Both Windows and WSL normal-TLS probes of `addressing-mar-perform-hormone.trycloudflare.com` returned `/`, `/health`, and the expected JS with status 200, no redirect or Set-Cookie, and JS SHA `d1434360…6ff4bd`.

Native process continuity matches exact pins: supervisor 14708 at ticks 639278403605890201 and child 2148 at ticks 639278403607622938, with expected executable hashes/paths, parent IDs and complete argv. Both remain alive. Selected safe state fields report the same generated hostname, target `http://127.0.0.1:8083`, HTTP/2, one registered connection event and one error event; no exit, callback fault or state write failure.

The same seven expected containers are running and five expected volumes exist. API remains `fe5fb7…b4821`; Web service tag remains old `d11a8828…9365`; accepted candidate tag is `6f4b2500…01ed`; rollback tag is absent. API, Web and gateway remain on owned network `d48c8a9a…36925c20` at `.5`, `.4`, `.2`. Runtime gateway config SHA `93291313…3fe707` still equals the public template.

No private origin read, container/image/tag mutation, gateway test/reload, provider/database/session operation, or service restart occurred. Root must bind a fresh operation GO to this preflight and v7 before any ApplyAll execution.
