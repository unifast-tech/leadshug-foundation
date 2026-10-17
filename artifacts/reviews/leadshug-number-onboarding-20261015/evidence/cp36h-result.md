# cp36h test-only execution receipt

Status: terminal; source and runtime work stopped after the authorized validation.

The only source change is `api-app/src/integrations/meta/meta.client.spec.ts`. It adds direct malformed-grant cases for a missing `data` object, non-string `app_id`, and non-boolean `is_valid`; these assert one shared rejection’s `MetaIndisponivelError` class and `META_INDISPONIVEL` code, exactly one fixed-host debug-token fetch, and the expected authorization header. Two positive cases cover omitted `scopes` with required granular authorization and an irrelevant granular scope without `target_ids`; each returns the selected phone ID and normalized phone number after exactly two bounded fetches. These cases protect existing behavior; no implementation defect or RED was asserted.

The canonical command `bash scripts/test-channels-local.sh all` ran once and exited 0. The run applied 22 migrations and passed 172 API unit tests, 288 PostgreSQL API E2E tests, 28 Web unit tests, and 47 browser tests. The raw output is `cp36h-api-all.log` (SHA256 `588d37e0cd8ad19d2e8c3e0c15668f6f594560bab7e7f8a241de3d3c68b58925`); the exact command and exit code are preserved in their companion files.

The pre-worker freshness file was copied from the runner-emitted `foundation_documentation/artifacts/tmp/number-onboarding-execution/pre-worker-freshness.json` at `2026-10-16T23:56:42.251Z`. The browser attestation was copied from `foundation_documentation/artifacts/tmp/inbox-timeline-execution/attestation-browser-authority.json` at `2026-10-16T23:56:39.550Z`. Both attestations are genuine outputs of this run. Freshness lists exactly nine source entries whose hashes match `cp36h-source-after.sha256`. The browser attestation records 22 migrations and identical served/dist bundle SHA256 `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd`.

The before, pre-all, and after manifests each cover the same nine paths. Only the permitted test spec changed; all other eight paths remain byte-identical to cp36g. Source hashes and the changed-only proof are in `cp36h-source-before.sha256`, `cp36h-source-preall.sha256`, `cp36h-source-after.sha256`, and `cp36h-changed-only-unit-proof.json`; the source freeze is `cp36h-source-freeze.json`.

Independent fresh TQA and the distinct final review remain with root. This receipt does not claim external Meta/provider or operator recovery evidence.
