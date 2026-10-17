# cp64 remaining preparation v5

V5 resolves the bounded PowerShell native-output and argument-marshalling findings. The helper's parser passed. Fresh PowerShell 5.1 tests exercised both text and mutation wrapper bodies with dummy stdout/stderr and exit codes 0 and 7; they captured the exact status and restored the caller's `Stop` preference in every case. The known API's double-quoted constant JavaScript expression failed safely with exit 1, while a quote-free single-quoted equivalent returned the expected JSON string. The future production/origin booleans now use that quote-free literal pattern. A dummy unavailable receipt sink confirmed ordinary stage logging still aborts before its stage mutation, while failure-path best-effort logging records a boolean and allows dummy recovery control flow to continue.

V5 helper SHA-256 is `29eed5fbdd3868d6a382d542ae840be36088eb956aa83b49c4e2ec5843781459`. Supporting probes and detailed outcomes are in [cp64-v5-compatibility.json](cp64-v5-compatibility.json).

No v5 helper application, Docker mutation, private-origin access, provider/database/gateway action, source/Git work, or `.local-files` access occurred. Stop pending fresh v5 review and separate root GO.
