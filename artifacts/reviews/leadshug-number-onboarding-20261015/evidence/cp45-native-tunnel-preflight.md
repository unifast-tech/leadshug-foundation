# cp45 native tunnel preflight

Captured 2026-10-16T22:34:57Z; read-only only.

No `cloudflared.exe` was found on the Windows command path, so there was no trusted local Windows binary to version/hash or use for a `--help` check. The pinned official release reference is cloudflared 2026.10.0, Windows AMD64 SHA-256 `86aee4017b26625cee8484c113558f48effa4cd47f7aa05fcf425604e5d2b23c`.

The cp43 Windows owner PID and both recorded WSL PIDs were absent at this check. Their absence does not establish why the hostname stopped resolving. Local gateway health remained 200 and WSL TCP port 8083 was open; DNS failed in Windows (`ENOTFOUND`) and WSL (`EAI_NONAME`).

A later restoration could use the pinned portable native Windows binary with a detached Windows-owned process targeting only `http://127.0.0.1:8083`, an empty explicit config, and in-memory output filtering. Checking `--protocol http2` is possible only after the trusted binary is available. This is a proposal, not an action or a conclusion about the prior failure's cause.

No process, installation, source, runtime, private configuration, provider, or database was changed.
