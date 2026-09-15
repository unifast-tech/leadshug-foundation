# TODO — LeadsHug: authority and technology documentation rebase

## Approval

- **Approved by:** `Gabriel / user — 2026-09-15 — APROVADO: escopo recomendado nos dois pontos`
- **Approval scope:** update active operating documentation so it names `leadshug-engineering` and `leadshug-foundation` as the current authorities and describes the active LeadsHug technology baseline, while preserving historical ADRs, completed TODOs, migration evidence and compatibility paths.
- **Renewed approval required when:** the rebase changes an accepted architectural decision, an executable compatibility path, product code, deployment/infrastructure configuration, an active feature contract beyond reference correction, or historical evidence.

## Objective

Make the current operating documentation unambiguous about both governance and technology without rewriting history:

```text
Engineering authority: leadshug-engineering
Product/governance authority: leadshug-foundation
Target product: LeadsHug/apps/api + LeadsHug/apps/web
Active baseline: NestJS 11, Prisma 6, PostgreSQL 16, React 18/Vite 5, Railway
Provider adapters: Meta Cloud API, Evolution/Baileys, Typebot Cloud, transactional email
```

## Classification rules

| Reference class | Treatment |
| --- | --- |
| Active operational authority (`delphi-ai` in Foundation README, constitution, TODO instructions and active TODOs) | Replace with the new authority and current tool paths. |
| Compatibility surface (`LeadsHug/delphi-ai` junction, script target, user-facing bootstrap output) | Preserve as a compatibility name; document its target as `leadshug-engineering`. |
| Historical evidence (completed TODOs, migration artifacts, command output, ADR context) | Preserve verbatim; add no retroactive rewrite. |
| Architecture history (`docs/arquitetura.md`, legacy descriptions) | Preserve historical sections; add or link a current-state navigation layer rather than silently changing past facts. |
| Technology claim | Verify against package manifests, deployment definitions and approved ADRs before documenting it as current. |

## Proposed scope

- [x] Rebase Foundation active operating documents: `README.md`, `project_constitution.md`, `todos/README.md`, and active TODO authority/rule references.
- [x] Add a concise maintained technology-baseline document in Foundation that links to the authoritative ADRs, package manifests and deployment definitions.
- [x] Add navigation from the Foundation documentation to the architecture-truth matrix and Central-Whatsapp legacy policy.
- [x] Rebase Engineering user-facing instructions only where they identify an authority or active technology incorrectly; preserve executable compatibility paths and Windows bootstrap instructions.
- [x] Choose the Product documentation treatment: add a current-state navigation layer in Foundation and leave `LeadsHug/README.md`, `docs/arquitetura.md`, `TODO.md` and active product contracts unchanged in this rebase.
- [x] Preserve product code, configuration, legacy repositories, completed TODOs, migration evidence and accepted ADR decisions without edits.

## Decisions required before execution

1. **Product documentation scope — resolved (recommended):**
   - **Recommended:** update Foundation/Engineering operational documents and add a current-state navigation document for LeadsHug; leave product historical documents unchanged in this first rebase.
   - **Expanded:** also correct current-state framing in LeadsHug README, architecture guide, TODO and active contracts, preserving historical sections with explicit timestamps.
2. **Active TODO cleanup — resolved (recommended):**
   - **Recommended:** correct authority/rule paths in all active TODOs, preserving their feature scope and approval state.
   - **Minimal:** correct only Foundation top-level operating documents; leave active TODOs for their own future closeout.

## Definition of Done

- [x] Active operators can identify the two current authorities and the target product stack without relying on a legacy name.
- [x] Compatibility links continue to work and are not represented as legacy authorities.
- [x] Every changed technology statement is traceable to a manifest, deployment definition or accepted ADR.
- [x] Historical evidence remains intact and distinguishable from current instructions.
- [x] Claude Code review, documentation checks and the Codex–Claude delivery guard pass.

## Validation Steps

- [x] Search active operating documents for obsolete authority references and classify each result before changing it (`rg` found only preserved compatibility/historical evidence after the rebase).
- [x] Check changed Markdown/YAML/JSON for broken relative links and run `git diff --check` (17 local documentation links resolved; no whitespace errors).
- [x] Run Engineering self-checks affected by documentation/tool-path changes and bootstrap/verification checks if an executable instruction changes (`bash tools/self_check.sh` passed; no executable instruction changed).
- [x] Complete a read-only Claude review and `python3 tools/codex_claude_delivery_guard.py <todo-path> --require-final-review` (guard outcome: `go`).

## Codex–Claude Delivery Cycle

- **User approval evidence:** `Gabriel / user — 2026-09-15 — APROVADO: escopo recomendado nos dois pontos`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `not_run` (a documentação não exigiu checkpoint intermediário; a revisão final examinou o diff completo)
- **Claude final review status:** `findings_integrated`
- **Claude final review evidence:** `Claude Code Sonnet 4.6, read-only session e2f1921f-632f-42e5-9067-516580b60725, 2026-09-15; final verdict findings_integrated_required with F1–F3.`
- **Material findings disposition:** `F2 integrated by recording validation steps 1–3. F3 integrated by replacing the inline template path with a resolvable relative link. F1 is a low-severity closure observation about TODO-ci-contract-and-migration-test-gates; it is recorded but intentionally not moved/closed because this approved TODO must preserve the scope and approval state of active feature/process TODOs. No authority, compatibility, technology or historical-evidence finding remained.`
- **Continuity rule:** `After approval, continue local documentation, verification and review-driven repairs without pausing.`
- **Escalate to user only if:** `the rebase changes product architecture, code, deployment, a compatibility path, a feature contract or historical evidence.`
