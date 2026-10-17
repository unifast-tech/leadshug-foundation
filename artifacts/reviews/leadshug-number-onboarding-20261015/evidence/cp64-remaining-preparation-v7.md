# cp64 v7 terminal receipt correction

The immutable v6 helper remains `2ba4a442faf06b8ae34dbf2e5c81cb9fec42d7ce0f7f6655b4a33401046cbc66`. New helper `T/cp64-activate-origin-api-web-v7.ps1` is `5e31094320fd2b45392a8436223517ac124d837062530190cab14adec8accb47`. Byte comparison confirms exactly one replacement in the terminal rollback receipt: the inaccurate combined `noGatewayReloadOrRecreate=true` becomes `gatewayReloadAttempted=<actual flag>`, `noGatewayReload=<inverse actual flag>`, and `noGatewayRecreate=true`. No other bytes or recovery logic changed.

Windows PowerShell parser reported zero errors; plan-only and the existing 2-positive/9-negative predicate checks passed. Predicate mode made no Docker/network calls and no private reads. No ApplyAll, runtime mutation, gateway reload, or activation was performed.

Evidence JSON: `cp64-remaining-preparation-v7.json`. This is a narrow supplement to the already completed v6 review; root remains the only authority for any operation.
