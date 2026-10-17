# cp64 native-output compatibility probe

In Windows PowerShell 5.1.26100.9711 with `$ErrorActionPreference = 'Stop'`, a harmless `cmd.exe` dummy emitted both stdout and stderr, then exited 0 or 7. The tested wrapper shape was the same native invocation/redirection used by the candidate helper:

`$null = & $Native @Arguments *> $null`

For both exit codes, PowerShell raised a native-stderr exception before the wrapper assigned `$LASTEXITCODE`. The wrapper's capture field therefore remained null; `$LASTEXITCODE` observed after the exception was `-1`, not the command's actual status. This is a concrete compatibility issue: stderr from Compose can interrupt the helper before it records the real exit code. V4 was not edited; no Docker command ran.

The temporary probe is `T/cp64-native-output-compatibility.ps1` (SHA-256 `1031819185ee002fb7195899db2c0fde27681d578f9f5afed1e07984b4629c22`). No raw dummy output was persisted.
