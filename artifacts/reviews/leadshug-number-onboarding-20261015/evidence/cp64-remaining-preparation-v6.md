# cp64 activation helper v6 preparation

The new helper is `T/cp64-activate-origin-api-web-v6.ps1`, SHA-256 `2ba4a442faf06b8ae34dbf2e5c81cb9fec42d7ce0f7f6655b4a33401046cbc66`. v5 is unchanged.

v6 adds only the root-admitted conditional 502 diagnosis gate. Before any operation mutation it binds API, Web and gateway to the same exact owned network and stores each endpoint IP. It verifies the gateway's active managed config hash against the public template hash. After an observed public 502, and before any nginx command, it stores selected direct local endpoint statuses and expected policy/JS hash booleans in the failure receipt. One reload can occur only when the relevant direct service is healthy, the correct Web asset is served where relevant, its backend IP changed, the same owned gateway and network remain, and the active config is still identical to the public template. Otherwise it skips reload and follows the original guarded rollback. It never edits or recreates the gateway.

Validation: Windows PowerShell parser reported zero errors; plan-only mode passed. The pure predicate passed positive API and policy-route cases and nine negative cases. These predicate tests made zero Docker or network calls. No `-ApplyAll` execution occurred.

Runtime readiness and limitations are in `cp64-step7-readonly-preflight.json`. Fresh independent v6 review and root operation GO remain prerequisites.
