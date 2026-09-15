# Legacy Reconciliation — 2026-09-15

## Active Authority Outcome

`leadshug-engineering` and `leadshug-foundation` are the only active LeadsHug working authorities. No noncanonical Belluga product material or inactive Flutter/Laravel/Cline surface was added to either repository.

## Classified Working-Tree Coverage

| Legacy source | Already migrated | Superseded by curated baseline | Archived outside active repos | Result |
| --- | ---: | ---: | ---: | --- |
| `delphi-ai` | 13 | 53 | 829 | 895 accounted items |
| `belluga_now_foundation_documentation` | 29 | 2 | 0 | 31 accounted items |

The 53 Delphi same-path divergences are intentionally owned by the curated LeadsHug Engineering baseline. The two Foundation divergences are intentionally owned by the newer Foundation baseline. The remaining Delphi material belongs to the other project or inactive stack surfaces and is retained only in the verified archive selected by the user.

## Verified Archive

- Root: `C:\Unifast\LeadsHug\.migration-staging\20260915\legacy-backup-v1`
- Full Git histories: `delphi-ai.all-refs.bundle` and `belluga-now-foundation-documentation.all-refs.bundle`, both verified with `git bundle verify`.
- Working-tree archives: one `tar.gz` archive for each legacy source, preserving the pre-migration working content.
- Manifest: `backup-manifest.json`, with SHA-256 for every archive artifact.
- Inventory: `C:\Unifast\LeadsHug\.migration-staging\20260915\legacy-inventory-v2`, including per-file SHA-256 manifests, Git status snapshots and final classification CSVs.

## Integrity Confirmation

Immediately before requesting deletion authorization, both legacy directories were checked again against the verified manifests. `delphi-ai` remained at 895 files and `belluga_now_foundation_documentation` at 31; no file was added, removed or hash-changed. Delphi retains two explicitly recorded LX reparse-point exceptions (`rules/docker/core` and `rules/docker/local`); they are preserved by the working-tree archive and are not active LeadsHug surfaces.

The textual `git status --porcelain` snapshots now expand a few previously collapsed untracked directories into their individual files (Delphi: 168 snapshot entries / 166 current entries; Foundation: 2,125 / 2,111). The complete manifest comparison confirms this is presentation-only: every expected working-tree file is still present and byte-identical. No source directory was edited by the migration.

`leadshug-engineering` also passed `bash tools/self_check.sh`: stack-capability validation, native-link fallback test, agent-role routing guard, Codex–Claude delivery guard and the Engineering self-check all returned OK.

## Retirement Boundary

The reconciliation does not authorize deletion. A separate explicit user approval is required before permanently removing the legacy directories. The verified archive must remain available until that approval is executed and a final recovery check passes.
