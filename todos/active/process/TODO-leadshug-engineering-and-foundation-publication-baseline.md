# TODO — LeadsHug: baselines limpos para Engineering e Foundation

## Approval

- **Approved by:** `Gabriel / user — 2026-09-14 — APROVADO`
- **Approval scope:** preparar, em diretórios de staging descartáveis, os manifestos selecionados, a checagem de dependências, a varredura de segredos e a prova de instalação limpa para dois novos repositórios LeadsHug: Engineering e Foundation.
- **Authority model:** o usuário aprova o TODO; Codex executa e consolida a evidência; Claude Code realiza revisão técnica sênior nos checkpoints e na entrega final.
- **Not authorized by this TODO:** criar repositórios remotos, fazer push, definir visibilidade/licença/owner, apagar o histórico existente ou publicar credenciais.
- **Renewed approval required when:** a seleção exigir descartar material LeadsHug potencialmente canônico, revelar segredo/dado privado, exigir nova infraestrutura/credencial, ou alterar o escopo dos dois repositórios.

## Remote Publication Authorization

- **Approved by:** `Gabriel / user — 2026-09-14 — APROVADO`
- **Authorized action:** create `unifast-tech/leadshug-engineering` and `unifast-tech/leadshug-foundation` as private repositories, without a public license, with protected `main`.
- **Human merger approver:** `Gabriel / user`

## Delivery Status Canon

- **Current delivery stage:** `Remote-Published`
- **Qualifiers:** `Branch-Protection-Blocked-By-GitHub-Plan + Remote-Hardening-Pending`
- **Next exact step:** retain both repositories as private and decide whether to upgrade the `unifast-tech` GitHub plan to enable the approved `main` branch protection; do not reduce repository privacy as a workaround.

## Objective

Create evidence-backed clean baselines for two future repositories, without inheriting historical Belluga/Flutter/Laravel material by accident:

1. `leadshug-engineering` (working name): Codex-first method, Claude Code senior review, Docker, NestJS, React, PostgreSQL/Prisma and Railway.
2. `leadshug-foundation` (working name): LeadsHug mandate, constitution, domain, modules, policies, contracts, active TODOs and relevant evidence.

## Scope

- [x] Produce explicit selected-file manifests for Engineering and Foundation from the current working material.
- [x] Trace the Engineering manifest dependency closure: bootloaders, configuration, rules, workflows, templates, tools, tests and generated agent surfaces.
- [x] Exclude/quarantine inactive legacy stacks and alternate agent runtimes, old Belluga product material, stale bootloader references, caches, generated local state and non-authoritative backups.
- [x] Scan the staged content for credentials, tokens, private endpoints and accidental environment exports.
- [x] Create disposable clean staging directories; initialize independent local Git repositories only after the manifests pass review.
- [x] Run Engineering self-check, linker/routing/Claude-cycle checks and a downstream clean-install smoke test.
- [x] Run Foundation structural/authority checks, ensuring active TODOs and contracts are LeadsHug-specific.
- [x] Produce a final publication-readiness report listing the exact human decisions still needed: GitHub owner/name, visibility, license and branch protection.

## Explicit Exclusions

- No remote GitHub repository, commit, push, PR, deployment, secret creation or billing action.
- No destructive cleanup of either current dirty source repository.
- No product-code change in `LeadsHug`.
- No replacement of the user's approval authority by Codex or Claude.

## Decision Baseline

| ID | Decision | Status | Evidence |
| --- | --- | --- | --- |
| `D-01` | Use two separate repositories, not a monorepo. | approved direction | user conversation |
| `D-02` | Foundation starts from selected current LeadsHug documentation, not the old repository history. | approved direction | user conversation + current Foundation audit |
| `D-03` | First Engineering cut supports Docker, NestJS, React, PostgreSQL/Prisma and Railway. | approved direction | user conversation |
| `D-04` | Codex is execution lead; Claude Code is senior technical reviewer; user remains final human authority. | approved direction | user conversation |
| `D-05` | Publication occurs only after a clean, tested baseline and explicit remote metadata decisions. | approved direction | user conversation |
| `D-06` | Publish private repositories `unifast-tech/leadshug-engineering` and `unifast-tech/leadshug-foundation`, with no public license and protected `main`; user is the human approver. | approved | user approval — 2026-09-14 |
| `D-07` | Keep both repositories private when GitHub rejects branch protection on the current plan; require an explicit user decision before any plan upgrade or visibility change. | applied | GitHub REST response 403 — 2026-09-15 |

## Execution Plan

1. Read the current source trees and create machine-reviewable selected-file manifests; no source deletion.
2. Build clean, disposable staging copies from those manifests and inspect their complete diff/contents.
3. Run secret scanning and dependency-closure checks; resolve every finding without weakening the exclusion boundary.
4. Validate Engineering from a separate disposable downstream checkout, including native-link readiness and Codex–Claude routing checks.
5. Validate Foundation structure and confirm that no old-product artifact was admitted.
6. Codex runs the Claude technical checkpoint review, repairs local findings, then obtains a final Claude review of the staging evidence.
7. Deliver one readiness report. Stop for the user only to decide repository metadata or handle a material scope/security discovery.

## Definition of Done

- [x] Each future repository has an explicit, reviewed selected-file manifest and dependency-closure evidence.
- [x] No source tree was destructively pruned and no remote repository was created.
- [x] Engineering staging passes self-check plus native-link, routing and Codex–Claude delivery-guard tests.
- [x] A clean downstream installation can load the intended Engineering surfaces through native Windows links.
- [x] Foundation staging contains only current LeadsHug authority material and passes structural checks.
- [x] Secret scan findings are resolved or escalated; no credential is staged.
- [x] Claude final technical review is `no_material_findings` or `findings_integrated`.
- [x] Final report identifies the exact GitHub metadata decisions required before publication.

## Validation Steps

- [x] Compare each staging tree to its manifest and inspect unexpected/forbidden paths.
- [x] Run `bash tools/self_check.sh` and focused Engineering guard tests from the staged Engineering checkout.
- [x] Run native Windows link verification from a Windows-integrated shell against the disposable downstream checkout.
- [x] Run Foundation authority/structure checks against the staged Foundation checkout.
- [x] Run credential/secret scanning on both staging trees.
- [x] Run `python3 delphi-ai/tools/codex_claude_delivery_guard.py <todo-path> --require-final-review` before delivery claim.

## Codex–Claude Delivery Cycle

- **User approval evidence:** `Gabriel / user — 2026-09-14 — APROVADO`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `findings_integrated`
- **Claude final review status:** `findings_integrated`
- **Claude final review evidence:** baseline: `C:\Unifast\LeadsHug\.publication-staging\20260914\engineering-clean\artifacts\claude-final-review-2.json` (Claude Opus, read-only, session `3fb84e3e-1152-4187-bb5d-84d2dfa4c5f9`); native-link supplement: `artifacts\claude-native-link-standard-review.json` (Claude Sonnet, read-only, session `d66eb199-eb7e-4a2d-9990-a02541a46c17`, outcome `go`)
- **Material findings disposition:** `B1/B2 integrated. Native review finding was documentation precision: Engineering deterministic/core/.gitkeep supports .agents/deterministic/core; Foundation deterministic/.gitkeep supports .agents/deterministic/local. This wording is now explicit. Non-blocking hardening is recorded below.`
- **Continuity rule:** `Continue local staging, validation and review-driven repairs without pausing for reconfirmation.`
- **Escalate to user only if:** `a finding materially changes approved scope, architecture, risk, external dependency, or requires a remote/publication decision.`

## Risks and Escalation

| Risk | Handling | Delivery Impact |
| --- | --- | --- |
| Old and current Foundation history describe different products. | Build a selected-file baseline; never fork the old history. | blocks staging if an artifact cannot be classified |
| Dirty source trees contain unrelated user work. | Read/copy selected paths only; do not reset, checkout or delete source changes. | blocks only ambiguous selected paths |
| Native Windows agent links can regress. | Verify from a Windows-integrated shell in the clean install. | blocks Engineering readiness |
| GitHub metadata is not chosen. | Keep publication local and report required decisions. | does not block local readiness; blocks remote publication |

## Execution Evidence and Review Finding Resolution

| Item | Status | Evidence |
| --- | --- | --- |
| Engineering staged manifest | passed | `C:\Unifast\LeadsHug\.publication-staging\20260914\engineering-clean\artifacts\publication-manifest.txt`; staged tree `e5c6b1bc8a17ab93bdee7fc0ad2a61ca89729cef` |
| Foundation staged manifest | passed | `C:\Unifast\LeadsHug\.publication-staging\20260914\foundation\artifacts\publication-manifest.txt`; local Git tree hash is recorded in external validation evidence to avoid self-referential package content |
| Engineering validation | passed | `engineering-clean/artifacts/engineering-self-check.log`, credential scan and active-stack scan artifacts; `git diff --cached --check` passed |
| Fresh downstream smoke | passed | v5 ran from the Windows-integrated shell; it created all eight required surfaces, ran sync, and both verification passes ended `Environment Verified: PACED-Ready.` |
| Foundation validation | passed | staged `git diff --cached --check` and credential-assignment scan passed; 31-file LeadsHug authority baseline including `deterministic/.gitkeep` |
| Claude routing | passed | `python3 ../delphi-ai/tools/agent_role_routing_guard.py --client claude-code --surface claude-senior-review --role formal-reviewer --model opus --effort xhigh --proof-mode artifact` returned `Overall outcome: go` |
| Claude B1 | integrated | `tools/sync_agent_rules.sh` preserves verifier-managed layered `.agents/rules/`; fresh smoke rebuilt from this staged source passed |
| Native link repair | passed | v5 proved UTF-16LE/base64 PowerShell link creation and native readability for every required installation surface |
| Deterministic contracts | integrated | Engineering `deterministic/core/.gitkeep` preserves the target of `.agents/deterministic/core`; Foundation `deterministic/.gitkeep` preserves the target of `.agents/deterministic/local` |
| Claude B2 | integrated | Engineering received the same diff check and credential scan as Foundation; both passed before tree hash capture |
| Remote publication | published | private `https://github.com/unifast-tech/leadshug-engineering` at `6d22f884ae7b7bfb004f9174db8581218e955c86`; private `https://github.com/unifast-tech/leadshug-foundation` initial baseline at `dbd7dded455182de6beb5803b47d8c336d440782`, with this follow-up recording the remote outcome |
| Main branch protection | blocked by GitHub plan | GitHub Branch Protection API returned HTTP 403: private repositories require GitHub Pro/Team or public visibility. Privacy is retained; no workaround was applied. |

## Hardening Follow-Ups Before Remote Publication

- Decide the license before creating a public remote.
- Keep `.gitattributes` enforcing LF for shell and instruction files.
- Add a minimal real NestJS/React fixture to future clean-install smoke tests; the current smoke validates package linking, not product runners.
- Keep the active-stack scan command and its historical-TODO allowance documented with the publication manifests.
- Detect an existing native Windows junction before the safe-backup branch of `verify_context.sh`, avoiding backup litter on repeated repairs when WSL does not classify a junction as `-L`.
- Preserve the suppressed native symlink creation error in a WARN-level diagnostic when the junction/hardlink fallback succeeds.
- After an approved `unifast-tech` plan upgrade, apply the intended `main` protection: one PR approval, stale-review dismissal, last-push approval, linear history, conversation resolution, and no force-push or deletion. Add required status checks only when CI workflows exist.

## Native Windows Smoke Evidence

Run from a Windows-integrated Git Bash/WSL shell at `C:\Unifast\LeadsHug\.publication-staging\20260914\downstream-smoke-v5`:

```bash
bash delphi-ai/tools/verify_context.sh --repair
bash delphi-ai/tools/sync_agent_rules.sh
bash delphi-ai/tools/verify_context.sh
```

All three commands completed successfully in v5. The repair created all required surfaces and the final verifier reported `Environment Verified: PACED-Ready.`.

## References

- `delphi-ai/artifacts/tmp/leadshug-fork-publication-plan.md`
- `delphi-ai/artifacts/tmp/self-improvement-work-ledger.md`
- `delphi-ai/workflows/docker/codex-claude-delivery-cycle-method.md`
