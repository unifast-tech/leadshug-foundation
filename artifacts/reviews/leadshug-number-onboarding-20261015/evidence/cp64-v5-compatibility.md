# cp64 v5 compatibility evidence

A new helper was prepared without changing v4. Both v5 Docker wrappers temporarily set `ErrorActionPreference` to `Continue`, suppress native stderr (and mutation stdout), capture `$LASTEXITCODE` immediately, restore the caller's preference in `finally`, then raise a sanitized nonzero result after restoration. A fresh Windows PowerShell 5.1 probe confirmed the exact wrapper bodies with harmless `cmd.exe` commands emitting both streams and exiting 0 and 7: both actual exit codes were retained and the caller's `Stop` preference restored.

The exact constant JavaScript expression with embedded double quotes failed safely with exit 1 on the known API. Its quote-free single-quoted equivalent returned the expected JSON string. V5's production-origin boolean snippets use the same quote-free form; no environment variable or private runtime value was read in the compatibility probe. The known API's selected ID/image/health/owner/project/service were checked using only selective inspect fields.

A dummy sink test exercised `Write-SafeStageReceipt`: ordinary/preflight sink failure raises a sanitized error; failure-path `-NoThrow` records `receiptWriteFailure` and returns so recovery control flow proceeds. No real Docker mutation or private access occurred.

V5 helper SHA-256: `29eed5fbdd3868d6a382d542ae840be36088eb956aa83b49c4e2ec5843781459`. Native wrapper test: `a4487b3a07e8ac9f379e98d0e3023b7d6f5e0e226a312c3bbfbcd82a7e733215`. Constant-argv read-only test: `4cad9a1925d301d555ad7d46e6aa86b69d8a22ff87116ddbf1b84b4e5c071701`. Receipt-sink test: `792d5fbd38efc7fff93981ee202d7393c7724d63196e0dd23f3e2150b6705dfb`.

Stop for fresh review and root GO before any private-origin edit or API/Web recreation.
