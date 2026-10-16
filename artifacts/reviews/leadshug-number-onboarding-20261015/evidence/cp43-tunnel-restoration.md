# cp43 temporary HTTPS transport restoration

Started one new detached Windows-owned `wsl.exe` process for the observed Ubuntu distribution. The pinned cloudflared 2026.10.0 binary (`d33ff2d1…`) targets only `http://127.0.0.1:8083`. Its filtered stream wrote only the generated hostname, `minority-influenced-veterans-ready.trycloudflare.com`; raw tunnel output was not persisted. The Windows owner and WSL supervisor/child remained alive after the launcher command and tool calls completed. Process identity is recorded with the Windows executable, creation time, command, WSL boot ID and process start ticks. The previous cp29 Windows and WSL processes remain untouched.

WSL and Windows DNS both resolve the new hostname. HTTPS root and `/health` returned 200 in both contexts. The served JavaScript SHA-256 is `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd` in both contexts, matching the previously accepted bundle. All seven operator containers and five local volumes match cp38 exactly and remain running/present.

A guarded rollback is available in `cloudflared-cp43/stop-tunnel.ps1` and `stop-tunnel.py`; it checks the exact Windows owner and WSL boot ID/start ticks, process parent, executable, script/binary hashes and target before sending SIGTERM only to the new cloudflared child. It allows the supervisor and owner to exit naturally. The rollback was not executed because restoration passed.

No API/app origin, Meta setting, source, Git, container, volume, database or provider state changed. This restores temporary transport only; the new hostname has not been applied to the application or Meta. Application origin work remains gated on fresh reviews and a separate activation.
