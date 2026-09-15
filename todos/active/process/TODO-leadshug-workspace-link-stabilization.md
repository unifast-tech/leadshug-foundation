# TODO — LeadsHug: estabilização do workspace conectado

## Approval

- **Approved by:** `Gabriel / user — 2026-09-15 — APROVADO`
- **Approval scope:** estabilizar a instalação local que conecta `LeadsHug` a `leadshug-engineering` e `leadshug-foundation`, definindo links nativos Windows, bootstrap reproduzível, política de Git para superfícies geradas e evidência de leitura por Codex e Claude Code.
- **Authority model:** o usuário aprova o contrato; Codex implementa e consolida evidências; Claude Code faz revisão técnica sênior; o usuário continua como autoridade final.
- **Not authorized by this TODO:** apagar ou sobrescrever alterações existentes no worktree de `LeadsHug`, alterar comportamento funcional do produto, publicar dados, mudar repositórios/remotos, criar infraestrutura ou enfraquecer regras de revisão.
- **Renewed approval required when:** a estabilização exigir mudar arquivos de produto rastreados sem uma política documentada, introduzir dependência/infraestrutura nova, descartar backup ou alterar a topologia ativa além de `LeadsHug` + os dois repositórios de autoridade.

## Delivery Status Canon

- **Current delivery stage:** `Awaiting-Native-Replay-Evidence`
- **Qualifiers:** `Native-Links-Installed + Inventory-Complete + Generated-Installation-Policy-Applied + Bootstrap-Implemented`
- **Next exact step:** replay the canonical bootstrap twice from a Windows-integrated user shell, capture both outputs, then run Claude technical review and closeout guards.

## Objective

Tornar repetível e segura a conexão local do projeto principal com as duas autoridades publicadas:

| Consumer path in `LeadsHug` | Active authority | Required link behavior |
| --- | --- | --- |
| `delphi-ai/` | `..\\leadshug-engineering` | Junction nativo Windows de compatibilidade para ferramentas existentes. |
| `foundation_documentation/` | `..\\leadshug-foundation` | Junction nativo Windows de compatibilidade para regras, mandato e TODOs. |
| `.agents/` | Engineering + Foundation em camadas | Junctions nativos para `skills`, `workflows`, `rules/{core,local}` e `deterministic/{core,local}`. |
| `.claude/`, `CLAUDE.md`, `apps/{api,web}/.claude/` | Engineering | Junctions nativos para diretórios e hard links nativos para arquivos. |

Os nomes de compatibilidade `delphi-ai` e `foundation_documentation` não representam repositórios legados: devem resolver exclusivamente para `leadshug-engineering` e `leadshug-foundation`.

## Scope

- [x] Inventariar links, arquivos reais, reparse points, backups de reparação e o `git status` inicial de `LeadsHug`, sem apagar nem sobrescrever conteúdo; evidence recorded below.
- [x] Definir a política canônica de versionamento para artefatos de instalação: o que deve ser rastreado, ignorado, regenerado ou preservado como alteração do usuário.
- [x] Implementar um bootstrap idempotente e documentado para uma nova máquina/clone, usando apenas os dois repositórios de autoridade locais e links legíveis pelo Windows; native replay remains pending external-shell evidence.
- [x] Ajustar os scripts de Engineering somente quando necessário para que `verify_context.sh --repair` e `sync_agent_rules.sh` não recriem links LX/WSL nem apontem para superfícies ausentes.
- [x] Preservar a regra em camadas de `.agents/rules/`; não substituir esse diretório por um único link de regras.
- [x] Validar no projeto raiz, API e Web que PowerShell/Git/Claude Code conseguem ler cada superfície vinculada.
- [ ] Registrar topologia, política Git, comandos de bootstrap, exceções e evidências no Foundation e no Engineering corretos.
- [ ] Executar checkpoint e revisão final do Claude Code; integrar qualquer finding material antes do encerramento.

## Explicit Exclusions

- Não executar `git reset`, checkout destrutivo, remoção recursiva ou limpeza de arquivos do worktree do produto.
- Não assumir que os `M` atuais de `CLAUDE.md` e `.claude/settings.json` são gerados: classificá-los antes de ignorar, substituir ou versionar.
- Não copiar conteúdo histórico dos diretórios aposentados; os únicos provedores ativos são os dois repositórios novos.
- Não transformar junctions/hard links locais em substitutos silenciosos de um processo de bootstrap documentado.

## Inventory Evidence — 2026-09-15

- `delphi-ai/` and `foundation_documentation/` are native Windows junctions resolving only to `leadshug-engineering` and `leadshug-foundation` respectively.
- The root, API and Web surfaces contain the expected 18 directory junctions and six file hard links; a direct PowerShell read check passed for every one.
- `CLAUDE.md` and `.claude/settings.json` are already tracked by the product. Their current hard-linked Engineering content differs from `LeadsHug` HEAD by 7/179 and 6/159 lines respectively. They were already modified before this TODO's execution and therefore remain user-owned until classified.
- `.agents/.sync_agent_links.lock` is also tracked even though it is a generated synchronization lock. The remaining `.agents/`, `.claude/rules`, `.claude/skills`, API and Web installation surfaces are currently untracked and not ignored.
- `rules.backup_20260827/` is an untracked historical repair backup. It must be preserved during this TODO and cannot be deleted as cleanup.

## Git Policy Decision Required

The current topology cannot become clean and reproducible without choosing one of these policies for the three tracked workspace artifacts:

1. **Recommended — generated installation surfaces:** remove `CLAUDE.md`, `.claude/settings.json` and `.agents/.sync_agent_links.lock` from the product Git index without deleting their working files; add precise ignore rules; retain the existing contents in Git history; and make bootstrap regenerate them from Engineering. This makes Engineering the sole active authority for agent configuration.
2. **Project-owned bridge files:** retain those three paths as tracked files in `LeadsHug`; replace hard links with deliberately versioned bridge/config files; and change bootstrap so it never overwrites them. This preserves product-local Git cleanliness but requires explicit synchronization whenever Engineering instructions/settings change.

No option has been applied. The decision is material because the existing tracked `CLAUDE.md` contains product context while the new Engineering bootloader contains the current agent authority.

## Git Policy Decision

- **Approved by:** `Gabriel / user — 2026-09-15 — Aprovo`
- **Decision:** apply option 1, generated installation surfaces. Remove `CLAUDE.md`, `.claude/settings.json` and `.agents/.sync_agent_links.lock` from the product index without deleting working files; add precise ignore rules; retain Git history; and bootstrap them only from Engineering.

## Execution Evidence — In Progress

- Product Git policy was committed locally as `d83ec11` on `LeadsHug/add_typeform_cloud`: the three approved paths were removed from the Git index only, their working files remain present as native hard links, and `.gitignore` now excludes only generated installation surfaces and repair backups.
- Engineering bootstrap was committed locally as `4f69edd`: `tools/bootstrap_leadshug_workspace.sh` creates only the two compatibility junctions, refuses real-directory conflicts, then runs repair/sync/verify. `README.md` and the tool manifest document the command.
- `tools/lib/native_links.sh` now resolves a file target relative to its link parent before identity comparison, and `native_link_creation_test.sh` covers the `../target-file.txt` pattern used by the synchronizer.
- Engineering validation passed locally: `bash tools/self_check.sh` returned `OK`, including native-link, bootstrap syntax, routing and delivery-guard tests.
- A direct PowerShell read check passed for all 18 linked directories and six linked files across root, API and Web after restoring native surfaces. The agent's noninteractive WSL lacks executable Windows-binary interop and is not valid evidence for the required bootstrap replay.

## Definition of Done

- [ ] Todo link da topologia acima aponta ao destino de autoridade correto e é legível por um cliente Windows nativo.
- [ ] Reexecutar o bootstrap não cria links LX/WSL, backups espúrios nem drift de destino.
- [ ] A política Git separa claramente artefatos de instalação gerados de alterações intencionais do produto, com decisão registrada para cada caminho atualmente alterado.
- [ ] Uma nova instalação local consegue executar o fluxo documentado e encerrar em `Environment Verified: PACED-Ready.`
- [ ] `leadshug-engineering` passa `bash tools/self_check.sh` após os ajustes necessários.
- [ ] Claude Code conclui a revisão final como `no_material_findings` ou `findings_integrated`.
- [ ] O TODO inclui evidência específica, é fechado em `todos/completed/process/` e os repositórios de autoridade ficam sincronizados.

## Validation Steps

- [ ] Capturar inventário pré-alteração: atributos/targets de reparse points, hashes de arquivos vinculados e `git status --porcelain=v1` do produto.
- [ ] Rodar em um shell Windows-integrado: `bash delphi-ai/tools/verify_context.sh --repair`, `bash delphi-ai/tools/sync_agent_rules.sh` e `bash delphi-ai/tools/verify_context.sh`.
- [ ] Ler, via PowerShell com `-ErrorAction Stop`, regras/skills/workflows e `CLAUDE.md` no root, `apps/api` e `apps/web`.
- [ ] Reexecutar a sequência de bootstrap e comparar destino, tipo de link e status Git contra o inventário esperado.
- [ ] Rodar `bash tools/self_check.sh` em `leadshug-engineering` e os testes focados alterados.
- [ ] Rodar `git diff --check`, os guardas aplicáveis e `python3 tools/codex_claude_delivery_guard.py <todo-path> --require-final-review` a partir de `leadshug-engineering` antes do fechamento.

## Evidence Plan

| Evidence | Owner | Required proof |
| --- | --- | --- |
| Workspace topology manifest | Codex | origem, destino, tipo de link e leitura nativa para cada superfície. |
| Git policy decision | Codex + user when classification is ambiguous | justificativa por caminho atualmente rastreado ou não rastreado. |
| Bootstrap replay | Codex | duas execuções consecutivas sem drift, link LX ou backup inesperado. |
| Engineering regression suite | Codex | `self_check.sh` e testes do sincronizador afetados. |
| Senior review | Claude Code | checkpoint e revisão final read-only com findings integrados. |

## Codex–Claude Delivery Cycle

- **User approval evidence:** `<pending explicit APROVADO>`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `not_run`
- **Claude final review status:** `not_run`
- **Claude final review evidence:** `<pending>`
- **Material findings disposition:** `<pending>`
- **Continuity rule:** `Após aprovação, continuar por inventário, implementação, testes e reparos guiados por revisão sem pausar, exceto por mudança material de escopo, arquitetura, risco, dependência ou classificação de alteração do usuário.`
- **Escalate to user only if:** `a política Git exigir descartar/sobrescrever alteração existente, uma classificação de arquivo for ambígua, ou a topologia exigir arquitetura/infraestrutura além do escopo.`

## First Approval Gate

Responda `APROVADO` para autorizar o inventário, a política de Git e a implementação reversível do bootstrap. Esta aprovação não autoriza apagar nem sobrescrever alterações existentes no repositório `LeadsHug`.
