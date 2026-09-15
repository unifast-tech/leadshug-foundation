# TODO — LeadsHug: migração de autoridade dos legados para os repositórios novos

## Approval

- **Approved by:** `Gabriel / user — 2026-09-15 — APROVADO`
- **Approval scope:** inventariar e migrar toda informação canônica e relevante para LeadsHug de `delphi-ai` e `belluga_now_foundation_documentation` para `leadshug-engineering` e `leadshug-foundation`; preservar evidência verificável antes de qualquer descarte.
- **Authorized by this approval:** read-only inventory, verified backup and reversible migration of classified LeadsHug content into the correct new repository.
- **Not authorized by this TODO:** permanent deletion of legacy directories, rewriting Git history, publishing private data or changing the active architecture beyond classified migration work.
- **Separate final authorization required:** remover definitivamente `delphi-ai` e `belluga_now_foundation_documentation`, mesmo após a migração passar nas validações.
- **Renewed approval required when:** um artefato não puder ser classificado, a migração exigir expor segredo/dado privado, houver conflito entre autoridade antiga e nova, ou a classificação alterar o escopo/arquitetura LeadsHug.

## Delivery Status Canon

- **Current delivery stage:** `Archive-Strategy-Decision-Pending`
- **Qualifiers:** `Verified-Inventory-Complete + Verified-Backup-Complete + Final-Deletion-Approval-Pending`
- **Next exact step:** choose where noncanonical historical material will live: a verified local archive, a dedicated private legacy repository, or `legacy/` paths inside the two active repositories.

## Objective

Fazer de `leadshug-engineering` e `leadshug-foundation` as únicas fontes de trabalho ativo, sem perder dados úteis dos diretórios legados:

1. `C:\Unifast\LeadsHug\delphi-ai` → `C:\Unifast\LeadsHug\leadshug-engineering`
2. `C:\Unifast\LeadsHug\belluga_now_foundation_documentation` → `C:\Unifast\LeadsHug\leadshug-foundation`

Todo artefato do legado deve terminar com uma classificação verificável: `migrated`, `superseded`, `archived-outside-active-repos`, `private-security-hold` ou `excluded-with-reason`. Nenhum arquivo será simplesmente ignorado ou destruído.

## Migration Principles

- Preserve a autoridade LeadsHug atual; não reintroduzir regras, produto, stacks ou histórico Belluga/Flutter/Laravel descontinuados como instrução ativa.
- Migrar arquivos canônicos para o destino correto: método, ferramentas e regras para Engineering; mandato, domínio, módulos, contratos, políticas e TODOs para Foundation.
- Manter material histórico ou não canônico fora das superfícies ativas, com inventário e motivo de retenção; não copiar segredos, caches, dependências instaladas ou estado gerado.
- Tratar alterações não commitadas, arquivos não rastreados e deleções pendentes como dados do usuário até serem classificados.
- Usar commits pequenos, verificáveis e revisados; Codex escreve, Claude Code revisa tecnicamente e o usuário continua autoridade final.

## Scope

- [x] Congelar um inventário somente leitura dos dois legados: arquivo, tamanho, hash, status Git, origem e classificação preliminar.
- [x] Comparar o inventário com os dois novos repositórios e registrar a lacuna de cobertura por destino.
- [x] Classificar cada lacuna como Engineering, Foundation, arquivo externo, segurança/privacidade ou exclusão justificada; classifications requiring archive strategy remain pending user direction.
- [x] Criar backup verificável dos legados e um manifesto de recuperação antes da primeira movimentação.
- [ ] Migrar conteúdo Engineering aprovado em commits temáticos para `leadshug-engineering`.
- [ ] Migrar conteúdo Foundation aprovado em commits temáticos para `leadshug-foundation`.
- [ ] Migrar ou registrar formalmente alterações não commitadas, arquivos não rastreados e deleções pendentes.
- [ ] Rodar validações de contexto, regras, YAML, links nativos, testes de cada pacote e varredura de segredos após cada lote.
- [ ] Executar revisão técnica do Claude Code e integrar findings antes do fechamento.
- [ ] Produzir relatório de reconciliação com a classificação de todos os itens e hashes de backup.
- [ ] Solicitar autorização final separada antes de arquivar ou apagar os dois diretórios legados.

## Explicit Exclusions

- Nenhuma exclusão definitiva, `rm`, `Remove-Item`, `git reset`, rebase de histórico ou troca de visibilidade remota sem autorização específica do usuário.
- Nenhuma cópia cega de `.git`, caches, `node_modules`, builds, credenciais, tokens, arquivos `.env` ou dados pessoais para os repositórios publicados.
- Nenhuma reativação de Flutter, Laravel, Cline ou Gemini na superfície ativa sem decisão arquitetural posterior.

## Inventory and Backup Evidence

- **Inventory root:** `C:\Unifast\LeadsHug\.migration-staging\20260915\legacy-inventory-v2`
- **Delphi working tree:** 895 files, 5,210,782 bytes; 893 SHA-256 hashes and two explicitly recorded native-unreadable LX reparse points (`rules/docker/core` and `rules/docker/local`); 168 Git-status entries.
- **Foundation legacy working tree:** 31 files, 154,911 bytes; all SHA-256 hashed; 2,125 Git-status entries, largely historical deletions relative to the old Belluga history.
- **Coverage:** current Foundation files are all represented in the new Foundation (29 equal and two intentionally newer/diverged). Delphi has 13 identical active files, 53 same-path divergences requiring review, 517 Engineering review candidates, 16 potential Foundation candidates, 294 inactive/history surfaces proposed for archival, and two native-link repair candidates.
- **Sensitive-content scan:** no credential was identified. Three pattern matches were reviewed as code/test identifiers, not secrets; raw scan paths remain only in the local inventory.
- **Backup root:** `C:\Unifast\LeadsHug\.migration-staging\20260915\legacy-backup-v1`
- **Recovery proof:** complete Git bundles verified for both source histories, plus working-tree tar archives. SHA-256 values are in `backup-manifest.json`; the Belluga history bundle is 65,954,956 bytes and the Delphi bundle is 2,662,930 bytes.

## Archive Strategy Decision Required

The two active repositories were intentionally kept free of legacy Belluga product history and inactive Flutter/Laravel/Cline surfaces. The verified backup preserves all of it, but permanent retirement of the legacy directories requires one of these explicit destinations:

1. **Recommended:** retain the verified local archive outside the active repositories and migrate only classified LeadsHug canonical content.
2. Create one dedicated private `leadshug-legacy-archive` repository for the bundles and historical material.
3. Add explicit `legacy/` archive paths to the two active repositories, accepting that this expands their size and historical surface.

## Definition of Done

- [ ] Cada arquivo legado está presente em um inventário com classificação e destino/justificativa.
- [ ] Todo conteúdo LeadsHug canônico está commitado e enviado ao repositório novo correto.
- [ ] Todo conteúdo histórico necessário possui backup recuperável e hash verificado fora das superfícies ativas.
- [ ] Nenhum segredo, dado privado indevido, cache ou artefato gerado foi publicado.
- [ ] `leadshug-engineering` e `leadshug-foundation` passam em suas verificações e testes aplicáveis após a migração.
- [ ] Claude Code conclui revisão técnica final como `no_material_findings` ou `findings_integrated`.
- [ ] O usuário recebe o relatório de reconciliação e aprova explicitamente qualquer arquivamento/descarte dos legados.

## Validation Steps

- [ ] Gerar manifestos com hashes SHA-256 antes e depois de cada lote.
- [ ] Confirmar `git status`, `git diff --check` e histórico de commits de ambos os repositórios novos.
- [ ] Rodar `bash tools/self_check.sh` e `bash tools/verify_context.sh` em `leadshug-engineering` quando as superfícies correspondentes forem alteradas.
- [ ] Rodar verificações estruturais, de referências e de segredo em `leadshug-foundation` após cada lote documental.
- [ ] Rodar o smoke nativo Windows para links quando scripts de contexto/linker forem migrados ou modificados.
- [ ] Executar `python3 tools/codex_claude_delivery_guard.py <todo-path> --require-final-review` a partir de `leadshug-engineering` antes de declarar a migração pronta.

## Codex–Claude Delivery Cycle

- **User approval evidence:** `Gabriel / user — 2026-09-15 — APROVADO`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `not_run`
- **Claude final review status:** `not_run`
- **Claude final review evidence:** `<pending>`
- **Material findings disposition:** `<pending>`
- **Continuity rule:** `After approval, continue through inventory, migration, tests and review-driven repairs without pausing except for a material classification/security/architecture finding or the final deletion authorization.`
- **Escalate to user only if:** `a classification is ambiguous, a secret/private datum is found, a conflict changes LeadsHug authority, or the final archival/deletion decision is reached.`

## First Approval Gate

Reply `APROVADO` to authorize the read-only inventory and the reversible backup/migration phases. This does **not** authorize permanent deletion of either legacy directory.
