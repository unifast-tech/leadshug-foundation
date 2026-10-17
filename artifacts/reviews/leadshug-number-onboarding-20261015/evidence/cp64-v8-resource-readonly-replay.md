# cp64 v8 retained read-only resource replay

Retained probe `T/cp64-v8-resource-readonly-replay.ps1` SHA-256 `facbe9f57e9df7ab2c9289208f094a96833654f0cfaeb37df03e649497534282` parses v8's AST and extracts only the allowlisted safe facts/guard functions and pinned constants: `Invoke-DockerText`, `Get-ImageId`, `Get-ContainerFacts`, `Assert-OwnedService`, and `Assert-PreservedResources`. It ran once with exit 0 and emitted one safe JSON object.

All seven known owned containers passed exact ID, image, running state, owner and project checks; API health is healthy while Web/Gateway correctly report no health value. The five expected volume names passed. API service tag remains fe5fb7…, Web service tag d11a8828…, accepted candidate tag 6f4b2500…; the rollback tag is absent. No private env, `Config.Env`, Compose, logs or mutation was used.

This replay is new evidence for current behavior. The earlier `cp64-v8-resource-readonly.json` was not rewritten or retrospectively attributed to this replay. v8 remains awaiting formal-review outcome and a new root GO.
