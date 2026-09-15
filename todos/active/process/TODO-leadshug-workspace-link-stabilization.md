# TODO — LeadsHug: estabilização do workspace conectado

## Approval

- **Approved by:** `<pending explicit APROVADO>`
- **Approval scope:** estabilizar a instalação local que conecta `LeadsHug` a `leadshug-engineering` e `leadshug-foundation`, definindo links nativos Windows, bootstrap reproduzível, política de Git para superfícies geradas e evidência de leitura por Codex e Claude Code.
- **Authority model:** o usuário aprova o contrato; Codex implementa e consolida evidências; Claude Code faz revisão técnica sênior; o usuário continua como autoridade final.
- **Not authorized by this TODO:** apagar ou sobrescrever alterações existentes no worktree de `LeadsHug`, alterar comportamento funcional do produto, publicar dados, mudar repositórios/remotos, criar infraestrutura ou enfraquecer regras de revisão.
- **Renewed approval required when:** a estabilização exigir mudar arquivos de produto rastreados sem uma política documentada, introduzir dependência/infraestrutura nova, descartar backup ou alterar a topologia ativa além de `LeadsHug` + os dois repositórios de autoridade.

## Delivery Status Canon

- **Current delivery stage:** `Awaiting-User-Approval`
- **Qualifiers:** `Native-Links-Installed + Git-Policy-Unresolved + Bootstrap-Not-Yet-Canonicalized`
- **Next exact step:** após `APROVADO`, inventariar as superfícies vinculadas e o estado Git existente antes de propor ou aplicar qualquer alteração de política.

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

- [ ] Inventariar links, arquivos reais, reparse points, backups de reparação e o `git status` inicial de `LeadsHug`, sem apagar nem sobrescrever conteúdo.
- [ ] Definir a política canônica de versionamento para artefatos de instalação: o que deve ser rastreado, ignorado, regenerado ou preservado como alteração do usuário.
- [ ] Implementar um bootstrap idempotente e documentado para uma nova máquina/clone, usando apenas os dois repositórios de autoridade locais e links legíveis pelo Windows.
- [ ] Ajustar os scripts de Engineering somente quando necessário para que `verify_context.sh --repair` e `sync_agent_rules.sh` não recriem links LX/WSL nem apontem para superfícies ausentes.
- [ ] Preservar a regra em camadas de `.agents/rules/`; não substituir esse diretório por um único link de regras.
- [ ] Validar no projeto raiz, API e Web que PowerShell/Git/Claude Code conseguem ler cada superfície vinculada.
- [ ] Registrar topologia, política Git, comandos de bootstrap, exceções e evidências no Foundation e no Engineering corretos.
- [ ] Executar checkpoint e revisão final do Claude Code; integrar qualquer finding material antes do encerramento.

## Explicit Exclusions

- Não executar `git reset`, checkout destrutivo, remoção recursiva ou limpeza de arquivos do worktree do produto.
- Não assumir que os `M` atuais de `CLAUDE.md` e `.claude/settings.json` são gerados: classificá-los antes de ignorar, substituir ou versionar.
- Não copiar conteúdo histórico dos diretórios aposentados; os únicos provedores ativos são os dois repositórios novos.
- Não transformar junctions/hard links locais em substitutos silenciosos de um processo de bootstrap documentado.

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
