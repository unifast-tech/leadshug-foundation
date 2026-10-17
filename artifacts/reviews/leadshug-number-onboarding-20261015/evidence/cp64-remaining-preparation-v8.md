# cp64 activation helper v8 preparation

The frozen failed v7 candidate is unchanged (`5e31094320fd2b45392a8436223517ac124d837062530190cab14adec8accb47`); its failed-attempt artifact and v7 stage receipt remain intact. New v8 helper SHA-256: `01e198a7818b51fe447f46923f38b95d159e05aaeda4f3cdf27ae438f80b05b1`.

Byte comparison confirms exactly two literal replacements: (1) `Get-ContainerFacts` now uses the Docker-verified nil-safe health template `{{.Id}}|{{.Image}}|{{.State.Status}}|{{with index .State `Health`}}{{.Status}}{{end}}`; (2) the stage receipt path is `cp64-activation-stage-v8.json`, preserving v7's receipt. No other helper behavior changed.

Windows PowerShell parser reported zero errors; plan-only and unchanged 2-positive/9-negative pure predicate checks passed. The exact helper-fact functions and guarded read-only checks passed for all seven known containers and five expected volumes; no mutations or private reads occurred. The actual safe result is `cp64-v8-resource-readonly.json` (SHA-256 `1e51128465a04448281f5f2d486c1b1261faa17d7a93366ffb56bacecde8ce92`).

This remains preparation only. v7's GO was consumed by its single failed preflight invocation; v8 requires fresh bounded review and a new root operation GO.
