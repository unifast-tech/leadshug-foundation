# CP29 HTTPS recovery handoff

At 2026-10-16 18:03:34 UTC, the old hostname `mistress-spencer-mozilla-sciences.trycloudflare.com` did not resolve in WSL or Windows; direct public DNS at 1.1.1.1 returned NXDOMAIN. Its cp22-owned process was still alive with the expected pinned executable and local-gateway target, but had no active transport sockets. The reason its DNS record disappeared is unknown.

One new detached Windows-owned `wsl.exe` process now holds cloudflared 2026.10.0 (SHA-256 `d33ff2d14475178d2012c2c56beba87389ac5ded27649519f198a7d3134a99db`) targeting only `http://127.0.0.1:8083`. The generated HTTPS host is `operating-brussels-internship-interviews.trycloudflare.com`. WSL and Windows resolve it; `/` and `/health` return 200 in both contexts, and the local gateway `/health` returns 200.

Windows owner PID 29132 and WSL supervisor/child PIDs 77581/77593 survived launcher completion. The stream filter continuously drained stdout/stderr and retained only the generated public hostname; raw tunnel logs were not persisted. After new HTTPS 200 and lifecycle evidence were captured, I sent SIGTERM only to the old child after executable path, pinned SHA-256, PPID, target, and saved supervisor-script guards matched. Its supervisor and Windows owner exited naturally; the new process remains the only active cloudflared PID.

No private origin, application container, source, database, or Meta configuration changed. No persistent tunnel/DNS, OAuth, provider operation, device pairing, or QR action occurred. Keep the new host as a temporary process-bound endpoint; application origin change requires the separate root activation.
