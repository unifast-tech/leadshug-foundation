# Workspace link stabilization — closure evidence

Date: 2026-09-15  
Scope: `LeadsHug`, `leadshug-engineering`, and `leadshug-foundation`

## Authority topology

| Consumer surface | Native Windows type | Authority target |
| --- | --- | --- |
| `LeadsHug/delphi-ai` | Junction | `C:\Unifast\LeadsHug\leadshug-engineering` |
| `LeadsHug/foundation_documentation` | Junction | `C:\Unifast\LeadsHug\leadshug-foundation` |
| Root `.agents` layered surfaces | Junctions | Engineering core; Foundation local rules and deterministic data |
| Root/API/Web Claude directories | Junctions | `leadshug-engineering/.claude` |
| Root/API/Web `CLAUDE.md` and settings | Hard links | corresponding `leadshug-engineering` files |

## Git policy applied

The user approved generated installation surfaces as the canonical policy. Product commit `d83ec11` removes only `CLAUDE.md`, `.claude/settings.json`, and `.agents/.sync_agent_links.lock` from the index, preserving their history and working files. Precise `.gitignore` entries keep generated links, repair backups, and app-level installation surfaces out of the product worktree while Engineering remains the active source.

## Native replay — PowerShell

The canonical command was executed twice from native Windows PowerShell on 2026-09-15:

```powershell
Set-Location -LiteralPath 'C:\Unifast\LeadsHug\LeadsHug'
powershell -NoProfile -ExecutionPolicy Bypass -File ..\leadshug-engineering\tools\bootstrap_leadshug_workspace.ps1 -ProjectRoot .
```

Both executions produced the expected managed `JUNCTION` and `HARDLINK` entries, including the two compatibility junctions, root/API/Web agent and Claude surfaces, and ended with:

```text
Claude Code artifacts: OK
Ecosystem packages YAML: OK
Local packages YAML: OK
Environment Verified: PACED-Ready.
Workspace bootstrap complete with native Windows links: C:\Unifast\LeadsHug\LeadsHug
```

The follow-up native PowerShell validation used `-ErrorAction Stop` for all expected root/API/Web paths and completed with:

```text
Windows-native reads: 18 directories and 6 files OK
delphi-ai: Junction
foundation_documentation: Junction
```

The Bash bootstrap intentionally fails closed when it cannot invoke native Windows link tooling; it directs the user to the PowerShell bootstrap rather than creating LX/WSL links.

## Engineering regression suite

`bash tools/self_check.sh` passed after the implementation changes, including native-link creation, bootstrap syntax, agent-role routing, Codex–Claude delivery guard, and stack capability validation. `git diff --check` passed before the local commits.

## Claude Code senior review

Reviewer: Claude Code, session `bbdad2c6-2e3a-44fe-aa92-6ce473970610` (read-only, 2026-09-15).

The reviewer found the implementation fail-closed for unmanaged paths and divergent content, accepted the generated Git policy, and found no safety or correctness defect that blocks release. It initially returned a process blocker because the Foundation TODO had not yet recorded the two native replays or reconciled its pending evidence fields. This artifact and the completed TODO address that finding.

Accepted operational notes:

- A fresh clone needs the documented bootstrap before agent guardrail files are present.
- The Windows bootstrap may call `bash` only to unlink an existing LX/WSL reparse point; it otherwise creates and validates native Windows links itself.

Final review disposition: `findings_integrated`.
