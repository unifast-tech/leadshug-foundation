# TODO — Foundation lifecycle structural validator

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`

## Context

O lifecycle da Foundation exige um validator permanente quando backlog, decisões e roadmap ultrapassarem dez registros vivos combinados ou quando houver recorrência comprovada de drift. O ST-01 consolidou 18 registros vivos — três candidatos, onze decisões e quatro linhas de roadmap — e acionou o primeiro limiar. Até este TODO ser aprovado e entregue, os exact checks versionados no TODO concluído do ST-01 continuam sendo o controle obrigatório.

## Framing Source & Story Slice

- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `n/a`
- **Why this is the right current slice:** materializar somente o follow-up obrigatório de `D-09` como um validador permanente, sem misturar evolução de produto, pipeline ou novos estudos.
- **Direct-to-TODO rationale:** o gatilho, o owner estratégico, os invariantes de origem e o resultado esperado já estão definidos em [evolution_lifecycle.md](../../../evolution_lifecycle.md#deterministic-adoption-trigger); não existe ambiguidade de decomposição que justifique outro feature brief.

## Contract Boundary

- Este TODO define **WHAT** deve ser protegido pelo validador e o que prova sua entrega.
- `Assumptions Preview` e `Execution Plan` definem **HOW** a implementação é recomendada; não concedem execução.
- O TODO é **bounded but elastic**: correções locais no parser, fixtures e mensagens podem permanecer aqui quando preservarem os mesmos invariantes e a mesma conversa de aprovação.
- Novo owner canônico, mudança de schema/lifecycle, integração com CI/CD, expansão para código de produto ou exceção histórica exigem atualização do contrato e novo `APROVADO`.
- O TODO permanece em `Review`; refinamento, reviews e guards de planejamento não equivalem a autorização de implementação.

## Implementation Intent

- **Current delivery:** estabelecer um validador Foundation fail-closed, project-owned e sem dependências externas, acompanhado de testes positivos/negativos e comando documental reproduzível.
- **Planned next steps:** avaliar integração com GitHub Actions/CI em TODO próprio após a superfície local provar estabilidade.
- **Anticipatory implementation authorized now:** `none`
- **Rationale:** separar o mecanismo local determinístico da adoção em CI evita ampliar este slice e permite validar a semântica antes de torná-la gate remoto.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Tactical TODO lifecycle state:** `Review`
- **Qualifiers:** `none`
- **Next exact step:** obter o token humano exato `VALIDO D-01..D-46`; então congelar/publicar a replacement baseline e executar os gates formais pós-freeze antes de solicitar `APROVADO`.

## Active Work State

- **Work state:** `review`
- **Why this state now:** R-11 completou arquitetura + duas críticas independentes sem decisão material nova; a convergência pré-freeze foi satisfeita em `D-01..D-46` e aguarda validação humana integral.
- **Exit condition:** decisões validadas, baseline congelada/publicada, reviews e guards pré-aprovação verdes, seguidos de `APROVADO` explícito ou cancelamento com racional.

## Trigger Evidence

- **Trigger:** mais de dez registros vivos combinados em backlog, decisões e roadmap.
- **Observed count:** `18` em 2026-09-23 (`3` candidatos + `11` decisões `Accepted` + `4` linhas de roadmap).
- **Source:** [ST-01 D-09](../../completed/process/TODO-leadshug-foundation-evolution-lifecycle.md) e [Deterministic-adoption trigger](../../../evolution_lifecycle.md#deterministic-adoption-trigger).
- **Execution authority:** `none`; abertura e refinamento do TODO não equivalem a `APROVADO`.

## Scope

- [ ] `S-01` Criar `deterministic/validate_foundation_lifecycle.py`, executável com Python standard library, que derive estado vivo dos owners canônicos e mantenha somente um bootstrap trust kernel versionado para provar que owners/surfaces/schemas obrigatórios não foram removidos.
- [ ] `S-02` Validar fail-closed o bootstrap kernel, headings/tabelas, schemas/colunas obrigatórias e enums do source graph enumerado para lifecycle, backlog, decisões e roadmap.
- [ ] `S-03` Validar sintaxe e unicidade dos IDs `BLG-*` e `DEC-*` somente nos registros autoritativos admitidos, permitindo referências repetidas fora do owner; `CAP-*` fica fora deste slice.
- [ ] `S-04` Validar owner singular por registro admitido, links Markdown e decision-target paths confinados/resolvíveis; campos de dependência/next-gate em prosa são obrigatórios, mas não fingem ser IDs resolvíveis.
- [ ] `S-05` Distinguir decisão `Accepted` válida porém `pending-effect` de structurally eligible for effectiveness por uma gramática posicional explícita: cada target possui exatamente um segmento de evidência; o sentinel literal `PENDING` é válido e mantém pending-effect; ausência, duplicidade, placeholder diferente do sentinel ou contradição falham.
- [ ] `S-06` Preservar a exceção histórica por construção e provar completude: o conjunto de links em `decisions/README.md` deve ser exatamente igual aos arquivos `decisions/*.md` no nível raiz, exceto `README.md`; subdiretórios permanecem históricos/não admitidos até TODO material alterar o boundary.
- [ ] `S-07` Criar testes test-first positivos e mutation/fail-first negativos, com oráculos independentes do parser, fixtures temporárias e prova byte-for-byte read-only.
- [ ] `S-08` Documentar owner, comando, cobertura, códigos de saída, contextos de execução, proveniência direta das ferramentas e mensagens de diagnóstico em `deterministic/README.md`, além de atualizar o lifecycle, roadmap e índice raiz com o handoff canônico.
- [ ] `S-09` Substituir os exact checks somente depois de candidate validation/reviews e de uma árvore terminal já contendo move, retarget, evidência e cutover passar integralmente antes do commit imutável.
- [ ] `S-10` Formalizar gramática por estado: decision records ganham coluna `Successor decision`; roadmap `Exit-Gate-Met` exige link obrigatório a TODO concluído e admite somente classes fechadas de evidência no próprio `Exit gate`; lifecycle define o slug ASCII exato.
- [ ] `S-11` No closeout, atualizar atomicamente `DEC-validator-adoption-trigger` para o path concluído e validar uma materialização read-only do tree OID final; o commit carrega trailer `Validated-Tree: <tree-oid>` e é publicado sem alterar a árvore testada.
- [ ] `S-12` Separar declarações in-tree de resultados terminais: a árvore concluída contém protocolo, argv registry e evidência pré-terminal; após validar seu OID, a interface fechada gera um self-attestation manifest estruturado no corpo/mensagem, com command IDs, exits e output digests, mais trailers que vinculam manifest, registry e tree OID sem alegar prova externa de execução.
- [ ] `S-13` Vincular cada command ID a um contexto fechado (`materialized-tree|foundation-index|workspace-governance`) e à proveniência direta de execução: Foundation tree/blob, checkout Delphi limpo com commit/tree capturados e todos os executáveis externos do registry resolvidos com versão+SHA-256; rejeitar context drift e limitar explicitamente a alegação contra hermeticidade/transitivos não capturados.
- [ ] `S-14` Implementar um CLI público fino sobre package interno com responsabilidades fechadas de parser, attestation e runner, preservando oráculos de teste independentes.

## Out of Scope

- [ ] `OOS-01` Alterar backend, frontend, banco, runtime, Docker, Railway, CI/CD ou contratos de produto do LeadsHug.
- [ ] `OOS-02` Editar workflows de GitHub Actions ou alegar integração remota neste TODO.
- [ ] `OOS-03` Reabrir/reformular as direções aceitas ou enums do ST-01; a extensão estrutural `Successor decision` e a atualização de target do validator são autorizadas somente pelo contrato `D-12/D-14`.
- [ ] `OOS-04` Retroajustar TODOs concluídos, artifacts históricos ou documentos legados apenas para fazê-los passar no novo validator.
- [ ] `OOS-05` Copiar contagens, títulos, disposições ou conteúdo específico do ST-01 para o código do validator como verdade permanente.
- [ ] `OOS-06` Criar configuração paralela editável ou copiar registros vivos; o bootstrap kernel v1 é uma assertion de compatibilidade versionada e só muda junto com uma alteração material do contrato canônico.
- [ ] `OOS-07` Integrar o validator aos guards genéricos do `delphi-ai`; esta entrega permanece project-specific em `foundation_documentation/`.
- [ ] `OOS-08` Validar registros `CAP-*`, módulos, TODOs ou contract-verification records neste slice; sua admissão futura exige source-graph/schema próprios.

## Execution Lane Tracking

- **Local implementation branches:** `foundation_documentation:main`
- **Promotion lane path:** `main -> origin/main`
- **Lane-promoted threshold for this TODO:** `origin/main`
- **Production-ready threshold for this TODO:** `origin/main` com gates de entrega e closeout verdes

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Foundation lifecycle validator | `main@pending` | `n/a — single-branch Foundation authority` | `n/a` | `direct push after governed gates` | planned |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `.` | `697864f6ec9e44a8c122a2963fcb9f9e7219b515` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `deterministic/validate_foundation_lifecycle.py` | `A` | entrypoint/CLI fino do validator |
| Foundation | `deterministic/foundation_lifecycle/__init__.py` | `A` | package marker sem lógica/autoritatividade |
| Foundation | `deterministic/foundation_lifecycle/parser.py` | `A` | source graph, Markdown grammar e diagnostics |
| Foundation | `deterministic/foundation_lifecycle/attestation.py` | `A` | registry/template codec e commit verifier |
| Foundation | `deterministic/foundation_lifecycle/runner.py` | `A` | context resolution, provenance e subprocess capture |
| Foundation | `deterministic/tests/test_validate_foundation_lifecycle.py` | `A` | acceptance/CLI/parser mutations |
| Foundation | `deterministic/tests/test_foundation_attestation.py` | `A` | byte grammar, registry e commit-verifier mutations |
| Foundation | `deterministic/tests/test_foundation_runner.py` | `A` | execution-context, provenance e read-only mutations |
| Foundation | `deterministic/README.md` | `A` | contrato de uso, owner, cobertura e diagnóstico |
| Foundation | `evolution_lifecycle.md` | `M` | consolidar gramática final de decisões e substituir o handoff temporário pelo comando permanente |
| Foundation | `README.md` | `M` | expor navegação e comando canônico sem duplicar regras |
| Foundation | `decisions/README.md` | `M` | canonicalizar membership e guidance que referencia a gramática owned pelo lifecycle |
| Foundation | `decisions/ST-01-foundation-lifecycle-decisions.md` | `M` | adicionar successor column e mover atomicamente o target do validator no closeout |
| Foundation | `system_roadmap.md` | `M` | remover a regra concorrente de gate evidence e apontar ao owner canônico no lifecycle |
| Foundation | `todos/active/process/TODO-foundation-lifecycle-structural-validator.md` | `M, D, R` | contrato, evidência e movimento de closeout |
| Foundation | `todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` | `A, M, R` | destino governado após todos os gates |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| Foundation | `project_constitution.md` | `any` | invariantes constitucionais já definidos; mudança exigiria nova decisão material |
| Foundation | `backlog/**` | `any` | registros vivos serão lidos, não reescritos |
| Foundation | `modules/**` | `any` | nenhum contrato de produto/módulo muda |
| Foundation | `contracts/**` | `any` | nenhum contrato de produto muda |
| Foundation | `artifacts/**` | `any` | artifacts históricos não serão retroajustados |
| Foundation | `.github/**` | `any` | integração CI/CD permanece fora do escopo |
| Foundation | `../delphi-ai/**` | `any` | validator específico do LeadsHug, sem self-maintenance Delphi |

### Diff Deviation Analysis

Preencher somente se o guard retornar `no-go`; qualquer novo path ou change type exige classificação e, quando ampliar escopo, validação humana e novo `APROVADO`.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** helpers dentro do package aprovado, fixtures, mensagens de diagnóstico, casos negativos adicionais e pequenas correções documentais nos paths esperados.
- **Must update or split the TODO:** integração com CI, novo schema/owner, alteração de dados vivos para fazê-los passar, adoção em `delphi-ai`, nova dependência ou expansão para validação de produto.

## Definition of Done

- [ ] `DOD-01` O validator retorna `0` para a Foundation canônica válida e código diferente de zero para qualquer violação coberta, sem alterar arquivos.
- [ ] `DOD-02` Cada regra enumerada na Test Rule Matrix possui fail-first positivo/negativo, mensagem/exit assertions e oráculo independente do helper sob teste.
- [ ] `DOD-03` Mutations detectam estrutura Markdown ambígua, ID inválido/duplicado, enum inválido, coluna/owner/proveniência ausente, link/anchor/target inválido, base de resolução trocada, path/symlink escape, successor ambíguo/não efetivo, shape Rejected inválido, evidência roadmap fora das classes admitidas, sentinel/evidência 1:1 ausente/duplicada/contraditória, staged/worktree split, segredo em qualquer surface entregue, bytecode/write residual, qualquer mudança portável no manifest completo da fixture e output não redigido; referências repetidas válidas e `PENDING` explícito passam.
- [ ] `DOD-04` O validator deriva estado vivo dos documentos canônicos e mantém apenas o bootstrap kernel v1 documentado — paths de owners, surfaces/headings, schemas/colunas e enums obrigatórios — sem copiar registros vivos, contagens, títulos ou disposições.
- [ ] `DOD-05` Testes provam igualdade bidirecional entre o index de decisões e `decisions/*.md`, com mutations de unlink, orphan e duplicate-link; histórico em subdiretórios fica ignorado até mudança material do boundary.
- [ ] `DOD-06` `deterministic/README.md`, `evolution_lifecycle.md` e `README.md` apontam para um único comando; lifecycle possui as gramáticas finais de decisão e roadmap, `decisions/README.md` possui membership/guidance canônicos, `system_roadmap.md` aponta ao owner sem regra concorrente e o ST-01 record usa a coluna successor e target correspondente à fase; CI remoto não foi alterado.
- [ ] `DOD-07` Proposed, Accepted, Superseded e Rejected obedecem à gramática state-conditioned; `Exit-Gate-Met` exige um TODO concluído e limita links adicionais a owners canônicos admitidos; identifiers obedecem ao slug ASCII canônico.
- [ ] `DOD-08` Diff expectation, decisões, evidence matrix e gates pré-terminais estão completos e verdes dentro da árvore; resultados que só existem após materializar/validar o tree OID ficam exclusivamente no attestation manifest imutável do commit, sem alegação circular dentro do TODO concluído.
- [ ] `DOD-09` A árvore final staged contém TODO movido, handoffs/cutover e target/evidence do validator apontando ao completed path; a interface fechada executa cada check no contexto declarado, prova o mesmo tree OID, scan completo, ambiente no-bytecode e proveniência direta de Foundation/Delphi/toolchain, o commit message contém o self-attestation manifest e trailers `Validated-Tree`/`Validation-Attestation-SHA256`, o verifier confirma os bindings, e o commit possui exatamente essa árvore e é publicado sem novo diff.

## Validation Steps

- [ ] `VAL-01` Executar `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` e exigir exit `0` com resumo determinístico.
- [ ] `VAL-02` Executar `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` e exigir todos os testes verdes.
- [ ] `VAL-03` Executar a Test Rule Matrix inteira, incluindo bootstrap deletion, unlink/orphan decision records, bases distintas de path, provenance, root confinement, symlink/`..` escape, anchor dialect, Unicode/HTML, read-only byte snapshot, staged/worktree split, `PENDING` válido e evidência contraditória.
- [ ] `VAL-04` Sob o overlay Python fechado, executar o compile oracle sem escrita `python3 -E -s -S -B -c "from pathlib import Path; import sys; [compile(Path(p).read_bytes(), p, 'exec') for p in sys.argv[1:]]"` sobre o entrypoint, os quatro package files e os três test files aprovados; nenhum `__pycache__`/`.pyc` pode existir ou ser criado.
- [ ] `VAL-05` Executar separadamente `git diff --check`, diff expectation guard e `delivery-secret-scan` sobre exatamente todos os arquivos regulares do final Expected Changed Paths; legacy VAL-10 permanece compatibilidade histórica e não substitui a cobertura terminal. Nenhum comando isolado pode alegar as três capacidades.
- [ ] `VAL-06` Executar diff, authority, completion e closeout guards; exigir `go` antes do movimento final e provar todos os deliverables esperados mais exclusividade `active XOR completed`.
- [ ] `VAL-07` Aplicar a matriz legada por fase: no baseline pré-migração executar ST-01 `VAL-01/02/08/10`; após a primeira mudança de schema/target, `VAL-02` fica explicitamente superseded por `T-15/T-18` e pelo novo validator, enquanto `VAL-01/08/10` permanecem obrigatórios no candidate e na camada Git terminal. Nenhum check pode ser omitido por interpretação livre de “aplicável”.
- [ ] `VAL-08` Montar e stagear a árvore final — TODO completed, handoffs/cutover e decisão target atualizada —; capturar `git write-tree`, materializar esse tree OID em diretório temporário read-only e executar ali somente os comandos `materialized-tree`; comandos `foundation-index` provam separadamente o mesmo index/tree OID e `workspace-governance` usam o checkout Delphi limpo capturado.
- [ ] `VAL-09` Após os checks, provar que o index ainda produz o mesmo tree OID, rejeitar divergência index/worktree e untracked files nas surfaces admitidas, executar os probes limitados, capturar/verificar commit+tree Delphi, toolchain direto e ambiente no-bytecode, usar `--run-attested-suite` para gerar o self-attestation, criar o commit com o envelope exato e então executar o Post-Commit Verification Protocol a partir da materialização read-only de HEAD; verificar `HEAD^{tree}`, working tree limpa e publicar esse commit imutado. Qualquer divergência exige restage e rerun integral.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01..S-14` | Scope | implementação e adoção documental do validator | code+test+doc | paths esperados + `VAL-01..VAL-06` | local Foundation | planned | expandir 1:1 após implementação |
| `DOD-01..DOD-09` | Definition of Done | critérios de entrega | test+review | comandos e gates correspondentes | local Foundation | planned | evidência agregada não substituirá linhas finais 1:1 |
| `VAL-01..VAL-09` | Validation Steps | comandos obrigatórios | test | stdout/exit, staged tree OID e commit trailer | local Foundation | planned | registrar candidate SHA, validated tree, closeout commit e resultado |

## External Dependency Readiness

- **Decision:** `required for terminal validation and publication; not needed for validator-unit implementation`
- **Rationale:** parser/tests usam Python standard library e arquivos Foundation; a suíte terminal exige Linux/WSL POSIX com process groups/signals/symlinks/`/dev/null`/permission operations/`C.UTF-8`, Git com object-format compatível, toolchain direto identificado (`python3`, `git`, `bash`, `rg`, `sort`), checkout irmão `delphi-ai` limpo e capturado por commit/tree, além de `origin/main` acessível para publicação. O platform preflight bloqueia antes da suíte; Windows Git pode somente publicar depois, nunca produzir o attestation.
- **Current evidence:** `origin/main` contains the historical D-01..D-20 freeze and the expanded pending-validation D-01..D-23 contract through `c5b91dd87c01de2631e5f49df6198ebc6feb337a`; validation must precede its replacement freeze.

## Profile Scope & Handoffs

- **Primary planning profile:** `Strategic / CTO-Tech-Lead`
- **Primary execution profile:** `routine-executor`
- **Active technical scope:** `cross-stack` documental/determinístico
- **Expected supporting profiles:** `Assurance / Tester-Quality`; `formal-reviewer`
- **Genesis Gate 0:** `rejected — canonical Foundation already exists and this is governed evolution`
- **Profile scope command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/evolution_lifecycle.md foundation_documentation/README.md foundation_documentation/deterministic/validate_foundation_lifecycle.py foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py foundation_documentation/deterministic/README.md`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `Strategic / CTO-Tech-Lead` | `routine-executor` | decisões são estratégicas; parser/testes são execução delimitada | `deterministic/**`; handoffs documentais | planned; depende de validação, preflight e `APROVADO` |
| `routine-executor` | `Assurance / Tester-Quality` | mutation coverage e fail-closed behavior exigem challenge independente | validator, tests, evidence packet | planned após implementação |
| `Assurance / Tester-Quality` | `formal-reviewer` | final review fecha aderência e dívida residual | pacote consolidado | planned |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** um review de plano antes do `APROVADO`, crítica independente após freeze e gates de entrega após implementação.
- **Why this level:** o diff é pequeno e docs-only quanto ao produto, mas estabelece enforcement compartilhado, parser estrutural e suíte de mutações sobre várias autoridades Foundation.

## Canonical Module Anchors

- **Primary canonical anchor:** `foundation_documentation/evolution_lifecycle.md`
- **Secondary anchors:** `foundation_documentation/backlog/README.md`; `foundation_documentation/decisions/README.md`; `foundation_documentation/decisions/ST-01-foundation-lifecycle-decisions.md`; `foundation_documentation/system_roadmap.md`; `foundation_documentation/README.md`
- **Canonical Coverage Status:** `Complete for the touched lifecycle surface`
- **Decision consolidation targets:** `evolution_lifecycle.md`; `deterministic/README.md`; `README.md`
- **Module docs:** `n/a — no product module behavior or contract changes`

### Validator Source Graph (Revised Contract)

| Owner Path | Unique Heading / Record Surface | Required Structure | Validation Boundary |
| --- | --- | --- | --- |
| bootstrap trust kernel v1 in validator | fixed identities for the four owner files; lifecycle `Immutable identifiers`, authority/state-machine and `Roadmap gate evidence grammar` headings; exact table columns; required current enums | removal, duplication or rename fails until a material contract update changes kernel and lifecycle together | immutable parser trust root only; never stores live record IDs/counts/titles/dispositions |
| `evolution_lifecycle.md` | `Immutable identifiers`, `Authority matrix`, five `State machines`, `Roadmap gate evidence grammar`, `Historical-document exception`, `Deterministic-adoption trigger` | kernel-required headings/schemas/enums present and unique; exact ASCII slug grammar; authority rows unique | canonical semantic owner; validator kernel proves the v1 contract was not silently weakened |
| `backlog/README.md` | `## Candidates` | exact eight-column table; unique `BLG-*`; state from Candidates enum; nonempty fields | Markdown links resolve; freeform Dependencies/Next gate are required prose, not IDs |
| `decisions/README.md` | `Decision record rule`, `## Records` | canonical rule declares root-level `decisions/*.md` current and indexed; normalized links are unique and exactly equal those files except README | physical membership is canonicalized here; subdirectories are historical/unadmitted until a material rule change |
| indexed root-level decision record files | unique decision table plus one unique `**Provenance:**` field before the table | exact seven columns including `Successor decision`; unique `DEC-*`; state from Decisions enum; nonempty file provenance explicitly applies to every row | state-conditioned targets/evidence/successor grammar below; semantics remain review-owned |
| `system_roadmap.md` | unique six-column roadmap table plus one authoring-guidance link to lifecycle `Roadmap gate evidence grammar` | unique phase rows; valid Horizon/Gate status; nonempty dependencies/outcome/exit gate; no competing local evidence rule | `Open` allows prose exit gate; `Exit-Gate-Met` requires at least one link to a completed tactical TODO and permits only additional canonical module/contract or completed-TODO evidence links |

### Narrow Markdown Grammar (Revised Contract)

- UTF-8 strict input; reject undecodable bytes and hidden Unicode format controls in identifiers, enum values and paths.
- Lifecycle IDs use exact ASCII grammar `^(BLG|DEC|CAP)-[a-z0-9]+(?:-[a-z0-9]+)*$`; this slice admits only `BLG-*` and `DEC-*` owners.
- Required headings/tables are unique; duplicate/missing/reordered headers or row cardinality mismatch fail closed.
- Pipe tables are parsed structurally with inline code/link awareness; ambiguous escaped pipes/code spans fail with a diagnostic instead of silent token shifting.
- Markdown link destinations resolve relative to the directory containing their source document. Inline-code canonical decision-target tokens resolve from the Foundation `--root`. Both classes must be relative, remain under `--root` after lexical normalization and symlink resolution, reject absolute paths and `..`/symlink escape, and never cause content echo in diagnostics.
- Fragment links use a constrained v1 dialect: ASCII heading text only; lowercase; spaces and ASCII punctuation become a single `-`; leading/trailing `-` removed; duplicate normalized headings fail; percent-encoded fragments, Unicode-derived fragments and HTML anchors are rejected rather than guessed.
- Discovery depth is exactly the source graph above. Historical/completed/artifact content can be a resolved reference target without becoming a scanned live owner.
- Decision targets and target-consolidation evidence are split on semicolons outside inline code/links and mapped positionally. Exactly one evidence segment is required per target: literal `PENDING` yields valid `pending-effect`; a concrete non-placeholder segment yields structural coverage; missing/extra/duplicate/contradictory segments fail. Complete structural coverage is `structurally-eligible`, never a semantic truth claim.

### Decision State Grammar

| State | Named canonical targets | Target-consolidation evidence | Successor decision |
| --- | --- | --- | --- |
| `Proposed` | one or more unique confined relative paths | exactly one literal `PENDING` per target | literal `N/A` |
| `Accepted` | one or more unique confined relative paths | one segment per target: literal `PENDING` or concrete evidence beginning with that exact inline-code target token plus non-placeholder text | literal `N/A` |
| `Superseded` | preserve one or more targets | same positional grammar as `Accepted` | exactly one no-fragment relative Markdown link whose label is the exact successor `DEC-*` ID and whose destination is its unique owner file; the acyclic immediate-successor chain terminates at one `Accepted` structurally eligible decision |
| `Rejected` | retain one or more structurally valid targets | exactly one literal `PENDING` per target, structurally representing no consolidation in the current record | literal `N/A` |

Placeholder tokens are the whole-segment, case-insensitive set `PENDING|N/A|TBD|TODO|UNKNOWN|-`; only exact uppercase `PENDING` and `N/A` are valid where the table permits them. Any other placeholder, missing/extra segment, label/destination owner mismatch, fragment, self/unresolved successor, successor cycle, or chain whose terminal is not Accepted+structurally-eligible fails. Lifecycle semantics reserve `Rejected` for an unconsolidated proposal and require an accepted decision to retire through `Superseded`, but the current-state validator enforces only the observable row shapes/graph; transition-history fidelity remains review-owned unless a future approved source graph admits canonical history.

### Validation-Attestation-v1 Byte Grammar

- The complete commit message is exactly: subject `feat(foundation): add lifecycle structural validator`, LF, one blank LF, `Validation-Attestation-v1-Begin`, LF, the payload, `Validation-Attestation-v1-End`, LF, one blank LF, `Validated-Tree: <tree-oid>`, LF, `Validation-Attestation-SHA256: <64-lowercase-hex>`, final LF and EOF. No preamble, unrelated body text/trailer, extra blank line, duplicate block or alternate final-newline form is allowed.
- Payload is UTF-8 without BOM, LF-only, ends with one LF, and uses fixed order: `version`, `git-object-format`, `tree`, `registry-sha256`, `environment-sha256`, `git-config-manifest-sha256`, `delphi-commit`, `delphi-tree`, `tool-count`, ordered tool records, `command-count`, then command records numbered from `01` without gaps. Tool IDs are exactly `bash`, `git`, `python3`, `rg`, `sort`; each record contains `id`, resolved-executable byte SHA-256 and SHA-256 over raw version-command stdout, one NUL byte, then raw stderr (`<tool> --version`, except `python3 --version`).
- Required command IDs, in order, are `platform-preflight`, `foundation-validator`, `foundation-unittest`, `foundation-compile-no-write`, `legacy-val01`, `legacy-val08`, `legacy-val10`, `delivery-secret-scan`, `git-diff-check`, `diff-expectation`, `authority-guard`, `completion-guard`, `closeout-guard`, `tree-consistency`.
- Each command record has fixed fields in order: `id`, `context` (`materialized-tree|foundation-index|workspace-governance`), `cwd` (`workspace|foundation|materialized-foundation`), `argv-sha256` over exact NUL-joined UTF-8 argv bytes, decimal `exit`, `stdout-sha256` over raw stdout bytes, and `stderr-sha256` over raw stderr bytes. No normalization is allowed.
- `Validation-Attestation-SHA256` hashes exactly the payload bytes between delimiters, including its final LF and excluding delimiters, trailers and the digest itself. Missing, duplicate, unknown, reordered or malformed fields/commands fail.
- Golden tests construct expected payload bytes and digests independently of the production serializer/parser; mutations cover field/command reorder, newline/encoding change, stream swap, missing/duplicate command, altered argv/output bytes and trailer mismatch.
- `deterministic/README.md` owns one exact argv registry and its command-contract digest. The validator exposes `--run-attested-suite --tree <oid> --materialized-root <path>` to execute that closed registry, capture raw streams and emit only the canonical block, plus `--verify-attestation --commit <sha>` to verify message grammar, tree/trailers, registry digest and internal digest consistency.
- Every registry entry declares exactly one execution context: `materialized-tree` reads only the read-only tree materialization; `foundation-index` may read Foundation Git metadata but must prove its index/tree equals the attested OID; `workspace-governance` may invoke the clean sibling Delphi checkout while binding its captured commit and tree. No registered command may silently cross contexts.
- Direct execution provenance is part of the registry digest: Foundation scripts bind through the attested tree/blob; Delphi guards bind a clean checkout commit+tree; every directly invoked external executable in the approved registry (`python3`, `git`, `bash`, `rg`, `sort`) binds resolved-path content SHA-256 plus exact version output where supported. Shell-evaluated strings are forbidden except the three immutable legacy code-fence expansions explicitly listed in the approved registry. The verifier checks these bindings before accepting the self-attestation.
- The manifest is an immutable self-attestation, not cryptographic proof that execution occurred: raw command outputs are intentionally not retained in-tree, so an independent verifier can validate structure and bindings but cannot recompute stream digests. No stronger provenance claim is permitted.
- This is not a hermetic environment claim: OS kernel, shared libraries and other transitive runtime inputs remain unbound and must be named as residual operational risk.

### Approved Attested Command Registry

- Registry templates are UTF-8/LF records in the table order below. Tokens are the only `{...}` forms allowed; unknown, nested or partially embedded tokens fail.
- `{PYTHON}`, `{GIT}` and `{BASH}` resolve once, before execution, to canonical realpath bytes of the executable selected from the parent launch environment; those exact bytes are executed and bound by provenance. `{TREE}` resolves to the lowercase captured tree OID. `{FOUNDATION}` is allowed only in `tree-consistency` and the post-commit verifier, resolving to the canonical principal Foundation root after the applicable divergence preflight. `{COMMIT}` exists only post-commit and resolves to the captured full lowercase commit OID. Absolute bytes are permitted only through executable-token expansion and the verified root token; no literal absolute workspace or temporary-directory path is admitted in child argv.
- `{ST01_VAL01}`, `{ST01_VAL08}` and `{ST01_VAL10}` expand to the exact bytes between the opening `bash` fence LF and the LF immediately before the closing fence under the uniquely named heading in the completed ST-01 TODO. The source blob/OID and expanded bytes digest are bound; these are the only allowed `bash -c` payloads.
- Execution context and cwd are orthogonal registry fields. `materialized-tree` authorizes only the read-only materialized Foundation inputs. `foundation-index` authorizes verified principal Foundation worktree/index/Git metadata and requires `git write-tree == {TREE}`; its normal cwd is `foundation`, while `tree-consistency` is the sole row with cwd `materialized-foundation`, materialized executable bytes and principal access only through `{FOUNDATION}` after runner divergence preflight. `workspace-governance` authorizes the bound clean Delphi checkout plus verified principal Foundation metadata and uses cwd `workspace`. No context implies a cwd or input not explicitly present in its row.
- Every child environment is constructed from empty, never inherited. Its complete allowlist is `PATH={TOOL_DIR}`, `HOME={EMPTY_HOME}`, `XDG_CONFIG_HOME={EMPTY_XDG}`, `TMPDIR={RUN_TMP}`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONNOUSERSITE=1`, `LC_ALL=C.UTF-8`, `LANG=C.UTF-8`, `TZ=UTC`, `TERM=dumb`, `GIT_CONFIG_NOSYSTEM=1`, `GIT_CONFIG_GLOBAL=/dev/null`, `GIT_TERMINAL_PROMPT=0`, `GIT_PAGER=cat` and `PAGER=cat`; no other variable is passed. `{EMPTY_HOME}`/`{EMPTY_XDG}` are empty read-only directories and `{RUN_TMP}` is the only writable scratch directory, all outside admitted repositories. All direct Python argv place `-E -s -S -B` immediately after `{PYTHON}`; their only non-stdlib import roots are the attested script directory/cwd. Canonical sorted `NAME=value\0` template bytes are part of `registry-sha256` and separately bound by `environment-sha256`; physical capsule paths are represented only by their literal tokens.
- The runner creates one private read-only `{TOOL_DIR}` for every registry command, containing only verified aliases for `git`, `rg`, `sort`, `bash` and a fixed `python3` launcher that `exec`s the bound `{PYTHON}` with `-E -s -S -B`. Direct argv still execute bound absolute token resolutions; every descendant PATH lookup, including Delphi guards, is confined to these aliases. Launcher template/digest and alias target identities are registry-bound; directory entries, targets and bytes are verified before and after each command. PATH shadowing, substitution, unknown executable demand or capsule mutation fails.
- Git user/system configuration and ambient repository override variables are absent by construction. Local repository configuration remains required Git metadata and is bound through `git-config-manifest-sha256`, calculated over canonical path/type/bytes records for each file returned by `git rev-parse --git-path config` and the optional `config.worktree` in Foundation and Delphi. Before execution, bound Git runs with `--includes=false` to detect case-insensitively any `include.path` or `includeIf.*.path`; any unconditional/conditional include is rejected rather than resolved. Any config drift between capture and post-command verification fails.
- Every registry row binds a monotonic timeout plus independent stdout/stderr byte caps. The runner streams each pipe in 64 KiB chunks directly into SHA-256 and bounded diagnostic buffers, counts raw bytes, and never accumulates an unbounded stream. On timeout or first cap breach it sends SIGTERM to the isolated process group, waits exactly 2 seconds, then SIGKILLs remaining descendants; it emits a redacted machine result with `outcome=timeout|stdout-overflow|stderr-overflow`, byte counts and command ID, emits no attestation, and removes `{TOOL_DIR}`, empty homes and `{RUN_TMP}` in `finally` on every outcome.
- Provenance probes run before the registry suite in tool-ID order with exact argv `{BASH} --version`, `{GIT} --version`, `{PYTHON} --version`, resolved `rg --version`, and resolved `sort --version`. Each uses the same from-empty environment/capsule/process-group/64 KiB streaming algorithm, a `10s` timeout and `256KiB` cap per stream, with executable bytes verified immediately before and after. Nonzero exit, timeout, overflow, identity drift, descendant survival or cleanup failure suppresses attestation.

### Post-Commit Verification Protocol

- After creating the exact-envelope commit and before any push, capture `HEAD` and `HEAD^{tree}`, require the latter equals `Validated-Tree`, materialize that committed tree read-only in a new capsule and reject principal HEAD/index/worktree ambiguity before executing verifier code.
- Execute from the committed materialization, under the same POSIX preflight, from-empty environment, verified tools/config, no-bytecode, timeout/output/process-group and cleanup controls: `{PYTHON} -E -s -S -B deterministic/validate_foundation_lifecycle.py --verify-attestation --principal-foundation {FOUNDATION} --commit {COMMIT}`. `{COMMIT}` is the captured full lowercase object ID and `{FOUNDATION}` is the already verified principal root.
- The verifier independently reads the exact commit message/tree through bound Git metadata, validates the complete envelope/payload/registry/tool/environment/config/stream/trailer bindings and never imports principal-worktree Python bytes. A principal-worktree mutation after commit must be rejected before execution; post-commit verification is publication-gate evidence and cannot be written back into the immutable commit.
- `argv-sha256` hashes fully expanded NUL-joined argv bytes. `registry-sha256` hashes the immutable templates and metadata, before `{TREE}`/legacy expansion. The verifier reconstructs both domains; it never trusts runner-supplied hashes. Relocating the materialization must not change either digest.
- The registry digest domain is `Registry-v1` followed by one NUL byte, then every row/field in table order (`id`, `context`, `cwd`, argv arguments in order, permitted-input/provenance cell, bounds cell, success/phase cell). Each field is encoded as eight lowercase hexadecimal UTF-8 byte-length digits, one colon, the exact field bytes, then one NUL. Markdown presentation markers are excluded; inline-code contents are the field values. Duplicate/missing fields or noncanonical encoding fail.

| Command ID | Context / cwd | Exact argv template | Permitted inputs / direct provenance | Bounds | Success / phase |
| --- | --- | --- | --- | --- | --- |
| `platform-preflight` | `materialized-tree` / `materialized-foundation` | `{PYTHON}` `-E` `-s` `-S` `-B` `deterministic/validate_foundation_lifecycle.py` `--platform-preflight` | attested Foundation tree + isolated Python + POSIX kernel/filesystem/locale capabilities | `30s`; `1MiB` each stream | exit `0` before any other registry command; terminal |
| `foundation-validator` | `materialized-tree` / `materialized-foundation` | `{PYTHON}` `-E` `-s` `-S` `-B` `deterministic/validate_foundation_lifecycle.py` `--root` `.` | attested Foundation tree + isolated Python | `60s`; `1MiB` each stream | exit `0`; terminal |
| `foundation-unittest` | `materialized-tree` / `materialized-foundation` | `{PYTHON}` `-E` `-s` `-S` `-B` `-m` `unittest` `discover` `-s` `deterministic/tests` `-p` `test_*.py` | attested Foundation tree + isolated Python | `180s`; `8MiB` each stream | exit `0`; terminal |
| `foundation-compile-no-write` | `materialized-tree` / `materialized-foundation` | `{PYTHON}` `-E` `-s` `-S` `-B` `-c` `from pathlib import Path; import sys; [compile(Path(p).read_bytes(), p, 'exec') for p in sys.argv[1:]]` `deterministic/validate_foundation_lifecycle.py` `deterministic/foundation_lifecycle/__init__.py` `deterministic/foundation_lifecycle/parser.py` `deterministic/foundation_lifecycle/attestation.py` `deterministic/foundation_lifecycle/runner.py` `deterministic/tests/test_validate_foundation_lifecycle.py` `deterministic/tests/test_foundation_attestation.py` `deterministic/tests/test_foundation_runner.py` | attested Foundation tree + isolated Python | `60s`; `1MiB` each stream | exit `0`, manifest unchanged; terminal |
| `legacy-val01` | `workspace-governance` / `workspace` | `{BASH}` `-c` `{ST01_VAL01}` | completed ST-01 blob + Bash + Python + Git | `120s`; `4MiB` each stream | exit `0`, exact final `OK`; terminal until cutover commit |
| `legacy-val08` | `workspace-governance` / `workspace` | `{BASH}` `-c` `{ST01_VAL08}` | completed ST-01 blob + Bash + Git | `120s`; `4MiB` each stream | exit `0`, exact final `OK`; terminal until cutover commit |
| `legacy-val10` | `workspace-governance` / `workspace` | `{BASH}` `-c` `{ST01_VAL10}` | completed ST-01 blob + Bash + Git + rg + sort | `120s`; `4MiB` each stream | exit `0`, exact final `OK`; terminal until cutover commit |
| `delivery-secret-scan` | `materialized-tree` / `materialized-foundation` | `{PYTHON}` `-E` `-s` `-S` `-B` `deterministic/validate_foundation_lifecycle.py` `--scan-delivery-secrets` `--root` `.` `--todo` `todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` | attested Foundation tree + isolated Python; scan set equals final Expected Changed Paths regular files, with active source absent and completed destination present | `60s`; `1MiB` each stream | exit `0`, redacted `OK`; terminal; legacy VAL-10 is compatibility only |
| `git-diff-check` | `foundation-index` / `foundation` | `{GIT}` `diff` `--cached` `--check` | matching Foundation index/tree + Git | `60s`; `2MiB` each stream | exit `0`; terminal |
| `diff-expectation` | `workspace-governance` / `workspace` | `{PYTHON}` `-E` `-s` `-S` `-B` `delphi-ai/tools/todo_diff_expectation_guard.py` `--repo-root` `foundation_documentation` `foundation_documentation/todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` | bound Delphi tree + matching Foundation index/tree + isolated Python/Git | `120s`; `4MiB` each stream | exit `0`, `Overall outcome: go`; terminal |
| `authority-guard` | `workspace-governance` / `workspace` | `{PYTHON}` `-E` `-s` `-S` `-B` `delphi-ai/tools/todo_authority_guard.py` `foundation_documentation/todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` `--require-delivery-gates` | bound Delphi tree + matching Foundation index/tree + isolated Python/Git | `120s`; `4MiB` each stream | exit `0`, `Overall outcome: go`; terminal |
| `completion-guard` | `workspace-governance` / `workspace` | `{PYTHON}` `-E` `-s` `-S` `-B` `delphi-ai/tools/todo_completion_guard.py` `foundation_documentation/todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` `--require-delivery` | bound Delphi tree + matching Foundation index/tree + isolated Python/Git | `120s`; `4MiB` each stream | exit `0`, no blocking violation; terminal |
| `closeout-guard` | `workspace-governance` / `workspace` | `{PYTHON}` `-E` `-s` `-S` `-B` `delphi-ai/tools/todo_closeout_guard.py` `foundation_documentation/todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` `--repo` `foundation_documentation` | bound Delphi tree + matching Foundation index/tree + isolated Python/Git | `120s`; `4MiB` each stream | exit `0`, no blocking violation; terminal |
| `tree-consistency` | `foundation-index` / `materialized-foundation` | `{PYTHON}` `-E` `-s` `-S` `-B` `deterministic/validate_foundation_lifecycle.py` `--verify-tree-context` `--root` `.` `--principal-foundation` `{FOUNDATION}` `--tree` `{TREE}` | executable/package bytes from attested materialization; read-only principal Foundation worktree/Git metadata + matching index/tree + isolated Python/Git | `60s`; `1MiB` each stream | exit `0`, exact tree binding and pre-execution worktree divergence rejection; terminal immediately before commit |

### Legacy VAL-02 Transition Map

| Legacy control family | Transition | Replacement / rationale |
| --- | --- | --- |
| BLG/DEC syntax, uniqueness, table cardinality, lifecycle enums, target/evidence structural mapping | `replaced after schema mutation` | new validator rules `T-01..T-10`, `T-13..T-19` |
| fixed decision row width, fixed record counts/ID sets, exact direction/rationale maps and exact target-content assertions | `intentionally retired after schema mutation` | incompatible with `D-12/D-14`; live records and semantics remain canonical/review-owned rather than copied into code |
| feature-brief handoff uniqueness and competing-state scans | `intentionally retired after schema mutation` | artifacts are evidence-only and excluded by `D-01/OOS-08`; current candidate state is owned by backlog |
| ST-01 `VAL-01`, `VAL-08`, `VAL-10` | `retained through terminal Git validation` | link, whitespace and secret controls remain compatible and independently useful until closeout |

## Decision Pending

| Decision ID | Expanded Recommended Direction | Review Finding Source | Human Validation Needed |
| --- | --- | --- | --- |
| `D-21` | Preserve immutable immediate successor edges; require each no-fragment link label to equal the successor `DEC-*` ID and its normalized destination to equal that ID's unique owner file; require an acyclic indexed chain terminating at one `Accepted` structurally eligible decision. | `C3-F01`, `R1-ARCH-01`, `C4-F01`, `R2-CRIT2-01` | confirm durable, unambiguous multi-hop successor invariant |
| `D-22` | Enforce the observable `Rejected` current-state shape: retained targets, exact positional `PENDING` and successor `N/A`. Lifecycle semantics reserve it for unconsolidated proposals and retire Accepted through Superseded, but historical transition fidelity is review-owned because no canonical prior-state source is admitted. | `C3-F02`, `R1-ARCH-03`, `C4-F02`, `R2-ARCH-01/02`, `R2-CRIT2-02`, `R9-CRIT2-01` | confirm truthful structural rule without unverifiable transition claim |
| `D-23` | Split read-only proof into a portable filesystem manifest (paths, entry types, regular bytes, symlink target bytes, directory presence) and a Git-backed tree/index manifest for tracked modes `100644|100755|120000`; exclude directory permissions and symlink chmod claims. | `C3-F03`, `R1-ARCH-04`, `C4-F03` | confirm two-layer portable oracle |
| `D-24` | Consolidate the final decision state/successor/rejection grammar in `evolution_lifecycle.md`; keep membership/usage guidance in `decisions/README.md`; the validator only enforces those owners. | `R1-ARCH-02` | confirm canonical-owner consolidation |
| `D-25` | Define `Validation-Attestation-v1` as a closed LF/UTF-8 payload grammar with fixed delimiters/field order, tree/object-format/registry and direct-tool provenance fields, ordered required command IDs, per-command context/cwd/argv digest/exit/raw stdout+stderr digests, duplicate rejection and a non-circular payload digest trailer verified by independent golden fixtures. | `C4-F04`, convergence critique 2 | confirm canonical attestation byte grammar |
| `D-26` | Decompose legacy `VAL-02`: replace structural ID/enum/cardinality/target-evidence checks with mapped new rules; intentionally retire fixed record/count/content maps, feature-brief state scans and target-content assertions at schema mutation because they duplicate live/semantic truth outside the admitted graph; retain ST-01 `VAL-01/08/10` through terminal Git validation. | convergence critique 2 | confirm per-control legacy retirement map |
| `D-27` | Use a project-owned closed attestation interface and exact argv registry: `--run-attested-suite` executes/captures the fixed suite and emits canonical bytes; `--verify-attestation` verifies commit/tree/registry/digest bindings. Classify the result explicitly as immutable self-attestation because raw streams are not retained for independent re-execution proof. | `R2-ARCH-03`, `R2-CRIT1-02`, `R2-CRIT2-03` | confirm executable interface and honest trust boundary |
| `D-28` | For `Exit-Gate-Met`, require at least one confined relative link to `todos/completed/**/TODO-*.md`; allow other evidence links only to `modules/*.md`, `contracts/*.md` or completed TODOs, and reject active TODO, artifact/history, README and roadmap-self targets. Semantic sufficiency remains review-owned. | `R2-CRIT1-01` | confirm closed structural roadmap-evidence classes |
| `D-29` | Partition the attested registry into closed execution contexts and bind direct tool provenance: attested Foundation tree/blob, matching Foundation index/tree, clean Delphi commit/tree, and every resolved registry-tool executable version+content digest. Reject drift, forbid unapproved shell strings, and state that OS/shared-library transitive inputs remain outside the non-hermetic self-attestation claim. | `R3-ARCH-01`, `R3-CRIT1-02`, `R3-CRIT2-01..03` | confirm executable provenance, substrate and bounded trust claim |
| `D-30` | Make lifecycle `Roadmap gate evidence grammar` the single semantic owner of `D-28`; admit `system_roadmap.md` as a changed path only to remove its broader local rule and link authoring guidance to that owner; validate absence of competing guidance. | `R3-CRIT1-01` | confirm canonical roadmap rule owner and expected-path expansion |
| `D-31` | Freeze the complete registry table above before approval: exact ordered argv templates, closed token/legacy-fence substitution grammar, contexts/cwds, permitted inputs, direct provenance, success and phase. Hash immutable templates separately from fully expanded NUL-joined argv; reject absolute/transient child paths and reconstruct all digests during verification. | `R4-CRIT1-01`, `R4-CRIT2-01` | confirm approval-complete command registry and relocation-stable digest domains |
| `D-32` | Keep one public CLI but split implementation into the bounded `foundation_lifecycle` package: `parser.py` owns parsing/diagnostics, `attestation.py` owns registry/codec/verifier, `runner.py` owns contexts/provenance/subprocess capture, and `__init__.py` has no logic; split tests by the same seams without sharing production oracle helpers. | `R4-CRIT1-03` | confirm modular implementation boundary and expanded expected paths |
| `D-33` | Add `delivery-secret-scan` to the terminal registry: derive an exact scan set from final Expected Changed Paths in the completed TODO, require active-source absence/completed-destination presence, scan every regular delivered file with redacted diagnostics, and treat legacy VAL-10 only as compatibility evidence. | `R5-CRIT1-01` | confirm complete terminal secret-scan coverage |
| `D-34` | Make no-bytecode execution part of the registry: fixed `PYTHONDONTWRITEBYTECODE=1` overlay for every child, explicit `-B` for direct Python argv, separately attested environment digest, and complete manifest equality around each materialized-tree command including privileged-runner tests. | `R5-CRIT2-01` | confirm deterministic read-only Python execution |
| `D-35` | Close Python startup influence: unset/reject Python path/home/startup/user variables, set no-user-site/no-bytecode, run every direct Python with `-E -s -S -B`, and admit only attested script/cwd plus system stdlib while keeping shared/system library code in the explicit non-hermetic residual boundary. | `R6-ARCH-01` | confirm controllable Python isolation boundary |
| `D-36` | Freeze the entire `Validation-Attestation-v1` commit-message envelope: exact subject, blank lines, delimiters, payload, two ordered trailers, final LF/EOF, and prohibition of any unrelated text/trailer or duplicate/alternate form. | `R6-CRIT1-01` | confirm canonical commit-message bytes |
| `D-37` | Execute nested legacy tools through a runner-created read-only PATH containing only verified aliases and a fixed isolated-Python launcher; bind launcher/alias templates and verify identities before/after, while canonicalizing the physical temp path as `{TOOL_DIR}`. | `R6-CRIT2-01` | confirm nested legacy executable identity |
| `D-38` | Construct every child environment from a complete explicit allowlist, use the verified private tool directory for all descendant lookups (including Delphi guards), isolate HOME/XDG/TMP/Git controls, bind local Git config manifests, and reject any ambient variable, unknown tool, PATH/config/capsule drift before acceptance. | `R7-ARCH-01`, `R7-CRIT1-01`, `R7-CRIT2-01` | confirm full descendant executable and inherited-environment closure |
| `D-39` | Reject any case-variant local `include.path` or `includeIf.*.path` in Foundation/Delphi config using bound Git with includes disabled; do not expand the trust graph to external config files. | `R8-ARCH-01`, `R8-CRIT2-01` | confirm closed Git config graph |
| `D-40` | Bind per-command monotonic timeout and per-stream byte caps; use 64 KiB streaming digests/bounded diagnostics, isolated process groups, SIGTERM then fixed 2-second SIGKILL escalation, no attestation on timeout/overflow and unconditional scratch cleanup. | `R8-CRIT1-01` | confirm deterministic runner resource/failure bounds |
| `D-41` | Execute `tree-consistency` code/package exclusively from the read-only materialized tree; runner must reject principal worktree/index divergence before execution and pass the verified principal root only as the dedicated `{FOUNDATION}` token for read-only metadata/data comparison. | `R8-CRIT2-02` | confirm verifier executes attested code bytes |
| `D-42` | Treat execution context and cwd as independent closed fields: context grants inputs/trust, cwd grants only location; `tree-consistency` is the sole `foundation-index` row with materialized cwd/code and principal access only through verified `{FOUNDATION}`. | `R9-ARCH-01`, `R9-CRIT2-02` | confirm unambiguous context/cwd semantics |
| `D-43` | Constrain terminal attested execution to a preflighted Linux/WSL POSIX substrate providing process groups, SIGTERM/SIGKILL, symlinks, `/dev/null`, permission operations and `C.UTF-8`; native Windows Git may publish the already-attested immutable commit only and cannot replace suite execution. | `R9-CRIT1-01` | confirm platform capability boundary |
| `D-44` | Distinguish canonical lifecycle transition policy from current-state enforcement: validator proves Rejected targets/PENDING/N/A and Superseded successor graphs, but never claims a historical Proposed→Rejected or Accepted→Superseded transition without an admitted history owner. | `R9-CRIT2-01` | confirm honest current-state validation boundary |
| `D-45` | After commit, materialize and execute verifier code only from the captured HEAD tree under the same closed runner controls; pass verified principal root and full commit OID as dedicated tokens, reject worktree ambiguity before execution and keep the result external to the immutable commit. | `R10-CRIT1-01` | confirm final acceptance uses committed code bytes |
| `D-46` | Run all five executable-version provenance probes through a closed ordered protocol with exact argv, from-empty environment, isolated process group, `10s` timeout, `256KiB` per-stream caps, streaming hashes, pre/post identity and unconditional cleanup; any abnormal outcome suppresses attestation. | `R10-CRIT2-01` | confirm bounded provenance capture |

## Decisions

- [x] `D-01` Keep the explicit BLG/DEC source graph and its declared exclusions.
- [x] `D-02` Include `Immutable identifiers` and the exact ASCII slug grammar in bootstrap trust kernel v1, without live records.
- [x] `D-03` Enforce read-only/fail-closed behavior, root confinement, byte preservation and redacted diagnostics.
- [x] `D-04` Canonicalize root-level current-decision membership in `decisions/README.md` and require exact index/file equality; keep subdirectories historical.
- [x] `D-05` Keep adoption local-only and CI-equivalent `n/a` in this slice.
- [x] `D-06` Use Python standard library plus unittest, test-first independent oracles and the mutation matrix.
- [x] `D-07` Keep ownership in Foundation, implementation routed to `routine-executor`, and make no Delphi changes.
- [x] `D-08` Use the terminal staged-tree protocol: validate the final tree, capture its OID, commit it unchanged with `Validated-Tree`, verify exact equality and push unchanged.
- [x] `D-09` Enforce positional target/evidence mapping and explicit `PENDING` under the state grammar.
- [x] `D-10` Require nonempty prose dependencies and resolve only explicit paths/fragments.
- [x] `D-11` Use the constrained ASCII anchor dialect.
- [x] `D-12` Extend decision records to seven columns with `Successor decision` and enforce the state-conditioned grammar plus closed placeholder dialect.
- [x] `D-13` Require `Exit-Gate-Met` roadmap rows to carry linked evidence in `Exit gate`; allow nonempty prose for `Open` (admissible evidence classes refined by `D-28`).
- [x] `D-14` Admit the ST-01 decision record as an expected closeout change and atomically retarget `DEC-validator-adoption-trigger` to the completed TODO path/evidence in the validated final tree.
- [x] `D-15` Bind all terminal validation to the exact captured tree OID through read-only materialization and unchanged-index/divergence proofs.
- [x] `D-16` Use distinct deterministic resolution bases for Markdown links and canonical decision-target tokens.
- [x] `D-17` Require one unique nonempty per-file provenance field applying to every decision row, without changing the seven-column schema.
- [x] `D-18` Bind post-validation outcomes outside the tree in an immutable structured commit attestation, while keeping only protocol/pre-terminal evidence in-tree.
- [x] `D-19` Replace ambiguous legacy “applicability” with the explicit phase/supersession matrix for ST-01 `VAL-01/02/08/10`.
- [x] `D-20` Require complete fixture-tree manifest equality for the read-only oracle on both success and failure.
- [ ] `D-21` Preserve immediate successor history, bind link label/destination to the unique successor owner and validate an acyclic multi-hop chain terminating at Accepted+structurally-eligible.
- [ ] `D-22` Enforce Rejected retained-target/exact-PENDING/N/A shape and keep unverifiable transition history review-owned.
- [ ] `D-23` Separate portable filesystem-content and Git-backed tracked-mode read-only oracles.
- [ ] `D-24` Consolidate final decision semantics into lifecycle/index owners before validator enforcement.
- [ ] `D-25` Use the closed canonical `Validation-Attestation-v1` byte grammar and independent golden oracle.
- [ ] `D-26` Classify every legacy VAL-02 subcontrol as replaced or intentionally retired, retaining VAL-01/08/10 through terminal validation.
- [ ] `D-27` Use a closed executable attestation interface/argv registry and state its self-attestation trust boundary without overstating independent proof.
- [ ] `D-28` Restrict Exit-Gate-Met evidence to completed tactical TODOs plus optional canonical module/contract evidence, with at least one completed TODO mandatory.
- [ ] `D-29` Bind every attested command to a closed execution context and direct tool provenance, with an explicit non-hermetic residual boundary.
- [ ] `D-30` Consolidate roadmap gate-evidence semantics in lifecycle and make system roadmap point to that owner without duplicating the rule.
- [ ] `D-31` Freeze the approval-complete command registry, token substitution grammar and separate template/resolved-argv digest domains.
- [ ] `D-32` Use a thin CLI plus bounded parser/attestation/runner modules and independently separated test files.
- [ ] `D-33` Add a terminal secret scan whose input set exactly covers every final delivered regular file; keep legacy VAL-10 as compatibility only.
- [ ] `D-34` Bind the fixed no-bytecode environment and Python `-B` argv into registry/attestation and prove no writes for every materialized command.
- [ ] `D-35` Isolate direct Python startup from mutable environment/user-site customization and bind the closed overlay/flags.
- [ ] `D-36` Enforce one exact complete commit-message envelope for Validation-Attestation-v1.
- [ ] `D-37` Route nested legacy executable lookup through a verified read-only tool directory with pre/post identity proof.
- [ ] `D-38` Build all child environments from a complete allowlist and close descendant tool/Git configuration identity across every command context.
- [ ] `D-39` Reject local Git config include/includeIf directives instead of admitting unbound external config graphs.
- [ ] `D-40` Bind command time/output limits, process-group termination and cleanup semantics into the registry.
- [ ] `D-41` Run tree-consistency from materialized code and reject worktree/index divergence before that code executes.
- [ ] `D-42` Make execution context and cwd orthogonal, with one explicit materialized-code foundation-index bridge.
- [ ] `D-43` Require a POSIX Linux/WSL terminal substrate preflight; reserve Windows Git for publication only.
- [ ] `D-44` Enforce only observable current-state rejection/supersession structure and avoid historical transition claims.
- [ ] `D-45` Execute post-commit attestation verification exclusively from a read-only materialization of the captured HEAD tree.
- [ ] `D-46` Apply the same closed resource/execution boundary to all executable provenance probes.

## Module Decision Baseline Snapshot

| Canonical Decision Ref | Current Direction | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `DEC-validator-adoption-trigger` | criar validator após limiar ou drift recorrente | Preserve | decisions record + lifecycle trigger |
| `DEC-single-field-authority` | um owner por campo e links/IDs fora dele | Preserve | ST-01 decisions record |
| `DEC-historical-adoption-boundary` | não retroajustar histórico intocado | Preserve | decisions record + historical exception |
| `DEC-decision-effectiveness-after-consolidation` | decisão só é efetiva após todos os targets | Preserve | decisions index + lifecycle |
| `DEC-immutable-lifecycle-identifiers` | IDs imutáveis com syntax canônica | Preserve | lifecycle immutable identifiers |
| `DEC-provider-neutral-lifecycle-roles` | papéis neutros de provider | Preserve | lifecycle roles and authority |

## Decision Baseline

- **Prior freezes:** `D-01..D-08@b685fb52` invalidated by `AR-01..05/F-01..11`; `D-01..D-10@504a9785` invalidated by `AR-R01..AR-R05/F-12..F-17`; `D-01..D-11@2562f62e` invalidated by `AR-F01..AR-F05/F-18..F-21`; `D-01..D-14@e26d7183` invalidated by `AR-N01/F-22..F-24`; `D-01..D-17@3dce63b3` invalidated by `C2-F01/C2-F02/C2-F04`; `D-01..D-20@0cd991e6` invalidated by `C3-F01..C3-F03`.
- **Freeze status:** `not_frozen — R-11 convergence clean; provisional D-01..D-46 await exact human validation token`
- **Frozen decisions:** `none current; D-01..D-20 remain validated provenance; D-01..D-46 are the converged provisional replacement set`
- **Current validation evidence:** Gabriel/user, 2026-09-24, exact phrase `VALIDO D-01..D-20`; preserved as provenance but superseded for approval by material review findings that introduced `D-21..D-23`.
- **Prior validation evidence:** Gabriel/user, 2026-09-24, exact phrase `VALIDO D-01..D-17`; preserved as provenance but superseded by material review findings that introduced `D-18..D-20`.
- **Prior validation evidence:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-14`; preserved as provenance but superseded for approval by material review findings that introduced `D-15..D-17`.
- **Latest prior validation evidence:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-11`; preserved as provenance but superseded by material full-owner findings.
- **Prior validation evidence:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-10`; preserved as provenance but superseded by the material review findings.
- **Historical validation evidence:** Gabriel/user, 2026-09-23, phrase `APROVADO`; preserved as provenance, not execution authority.

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `required`
- **Why this applies:** estabelece enforcement permanente de arquitetura documental compartilhada e aposenta checks ad hoc como controle corrente.
- **Deviation / debt being retired:** exact checks longos embutidos no TODO concluído do ST-01 e ausência de comando project-owned reutilizável.
- **Target steady-state after closeout:** um comando read-only, fail-closed, testado e documentado valida a Foundation viva sem duplicar verdade.
- **Temporary exceptions allowed:** `none`; os exact checks ST-01 permanecem somente como controle anterior até o cutover, não como implementação paralela permanente.
- **Cutover / removal condition:** validator e suíte publicados, acceptance real verde, reviews/audits obrigatórios limpos e lifecycle atualizado para apontar ao comando permanente.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| single-field authority | `DEC-single-field-authority` | owners e referências lifecycle | impede estado vivo concorrente |
| canonical-source derivation + trust root | `D-02` | parser e regras | deriva estado vivo e impede que o próprio contrato obrigatório seja silenciosamente removido |
| fail-closed diagnostics | `D-03` | CLI e gates | impede falso verde e torna falha acionável |
| historical adoption boundary | `DEC-historical-adoption-boundary` | seleção de entradas | preserva história sem esconder drift vivo |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| hard-coded ST-01 snapshot | novo registro válido exige editar validator | congela conteúdo transitório como regra | none |
| duplicated live-state catalog | enum/schema/owner copiado em config paralela | cria owner concorrente | none |
| regex-only validation without structural parsing | fixture estruturalmente inválida passa | aceita drift semântico/falsos verdes | regex pode apoiar parsing, nunca substituir estrutura |
| warning-only failures | input inválido retorna zero | não protege lifecycle | none |
| rewriting invalid source | hash/working tree muda durante validação | mascara drift e viola read-only | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| guard | live Foundation | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | schemas/IDs/owners/links/target-evidence mapping estrutural inválidos | implement-in-this-todo | `VAL-01`, `DOD-01/04` |
| test | validator rules | `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` | falsos verdes e regressões por mutation | implement-in-this-todo | `VAL-02/03`, `DOD-02/03/05` |
| rule | usage contract | `foundation_documentation/deterministic/README.md` | uso sem boundary/owner/exit semantics | implement-in-this-todo | `DOD-06` |
| audit | delivered package | critique + test-quality audit + final review | fragilidade, duplicação e dívida de verificação | implement-in-this-todo | gate evidence no TODO |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** fresh internal architecture review over complete nine-file byte snapshot, 2026-09-24: D-01..D-20 architecture coherent; `AR3-01` bookkeeping integrated. Material critique findings separately expanded the baseline to D-01..D-23, so rerun remains required after validation/freeze.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `AR-R01` | Integrated | useful | yes | project | n/a | bootstrap trust kernel v1 added without live-record duplication |
| `AR-R02` | Integrated | useful | yes | project | n/a | decisions index and root-level record set must be exactly equal |
| `AR-R03` | Integrated | useful | yes | project | n/a | explicit `PENDING` sentinel and positional mapping truth table added |
| `AR-R04` | Integrated | useful | yes | project | n/a | constrained ASCII heading-fragment dialect defined |
| `AR-R05` | Integrated | useful | yes | none | n/a | lifecycle/status fields returned to renewed-validation state |
| `AR-F01` | Integrated | useful | yes | paced | n/a | lifecycle fields returned to expanded-decision validation state |
| `AR-F02` | Integrated | useful | yes | project | n/a | decision and roadmap state-conditioned grammars added |
| `AR-F03` | Integrated | useful | yes | project | n/a | decision membership rule scheduled for canonical decisions index |
| `AR-F04` | Integrated | useful | partial | project | n/a | terminal validated-tree commit protocol replaces post-completion mutation |
| `AR-F05` | Integrated | useful | yes | project | n/a | immutable-identifier surface and exact slug grammar added to kernel |
| `AR-N01` | Integrated | useful | yes | paced | n/a | exact tree-OID materialization now binds tested bytes to committed bytes through `D-15` |
| `AR-N02` | Integrated | useful | yes | paced | n/a | lifecycle and closeout bookkeeping returned to the expanded-validation state |
| `AR-PKG-01` | Challenged | useful | yes | paced | `bounded-review-package-content-completeness` | package defect, not architecture finding; redispatch used exact eight-file byte snapshot with SHA-256 boundaries |
| `AR2-01` | Integrated | useful | yes | paced | n/a | current-state fields returned to D-01..D-20 validation/replacement-freeze state |
| `AR3-01` | Integrated | useful | yes | paced | n/a | current-state fields returned to D-01..D-23 validation/replacement-freeze state |

- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`
- **No-go handling:** `when either required review is absent, blocked, or exposes an unresolved approval-breaking divergence, return to the affected diagnosis/decision or delivery-evidence loop; do not claim APROVADO or Completed.`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** TODO medium de architecture enforcement requer pacote estável/publicado antes da crítica.
- **Trigger stage:** `after final converged decision-set validation and before renewed planning-side reviews`
- **Baseline branch:** `main`
- **Baseline commit:** `0cd991e61ff4d8ed1ff495c62113227db9c9f730`
- **Baseline push reference:** `origin/main contains 0cd991e61ff4d8ed1ff495c62113227db9c9f730; freeze bookkeeping published through 3a4e6e956070d8612540afe23adda81e8bfbb3cb`
- **Gate status:** `not_run`
- **Findings summary:** published D-01..D-20 freeze was invalidated; R-11 satisfied pre-freeze convergence with three clean exploratory reviewers over provisional D-01..D-46.
- **Evidence / reference:** commits `0cd991e61ff4d8ed1ff495c62113227db9c9f730` and `3a4e6e956070d8612540afe23adda81e8bfbb3cb`, pushed to origin/main on 2026-09-24.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** reviews podem revelar expansão acidental para CI, histórico ou owners.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **No-go handling rule:** `return to review, revalidate evolved scope, refresh pushed baseline when needed, and rerun affected review/guard lanes`
- **Gate status:** `not_run`
- **Findings summary:** `n/a`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close

- `VALIDO D-01..D-46` — required to validate the converged replacement decision set; this token does not grant implementation authority.

## Pre-Freeze Decision Convergence Cycle

- **Human direction:** exhaust decision discovery before requesting another `VALIDO`; user, 2026-09-24.
- **Cycle mode:** exploratory/refinement only; these reviews do not satisfy the post-freeze architecture or critique gates.
- **Round composition:** one fresh architecture opinion plus two fresh independent critiques over the same immutable complete snapshot.
- **Convergence criterion:** all three reviewers complete and the deduplicated round contains no new approval-material decision; bookkeeping and implementation-detail findings are resolved without expanding the decision set.
- **After convergence:** publish the integrated provisional contract, request one `VALIDO D-01..D-N`, freeze/publish it, rerun formal gates, obtain `APROVADO`, then implement.

| Round | Published Snapshot | Architecture | Critique A | Critique B | Material Decision Outcome | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `R-01` | `06c307d2` | `R1-ARCH-01..04` | `C4-F01..04` | `C4-F01..04` | refine `D-21..D-23`; add `D-24..D-26` | integrated; next round required |
| `R-02` | `f2ee3906` | `R2-ARCH-01..03` | `R2-CRIT1-01..03` | `R2-CRIT2-01..04` | refine `D-21/D-22/D-25`; add `D-27/D-28`; replace write-producing compile check | integrated; next round required |
| `R-03` | `e4cedcf9` | `R3-ARCH-01` | `R3-CRIT1-01..02` | `R3-CRIT2-01..03` | add `D-29/D-30`; bind direct tool/context provenance; admit roadmap guidance alignment | integrated; next round required |
| `R-04` | `f0e9e1ee` | `R4-ARCH-01` | `R4-CRIT1-01..03` | `R4-CRIT2-01` | add `D-31/D-32`; freeze full registry/substitution domains; modularize bounded implementation; reconcile surface lists | integrated; next round required |
| `R-05` | `0e72fd7a` | clean | `R5-CRIT1-01` | `R5-CRIT2-01` | add `D-33/D-34`; complete terminal secret coverage; bind no-bytecode environment/argv | integrated; next round required |
| `R-06` | `63f1fbee` | `R6-ARCH-01` | `R6-CRIT1-01` | `R6-CRIT2-01` | add `D-35..D-37`; isolate Python startup; freeze full commit envelope; verify nested legacy tools | integrated; next round required |
| `R-07` | `5bd89d41` | `R7-ARCH-01` | `R7-CRIT1-01` | `R7-CRIT2-01` | add `D-38`; construct closed child environments; extend verified tool/config closure to every command | integrated; next round required |
| `R-08` | `9202554b` | `R8-ARCH-01` | `R8-CRIT1-01` | `R8-CRIT2-01..02` | add `D-39..D-41`; reject Git config includes; bound resources; run verifier from materialized bytes | integrated; next round required |
| `R-09` | `3711727a` | `R9-ARCH-01` | `R9-CRIT1-01` | `R9-CRIT2-01..02` | add `D-42..D-44`; orthogonalize context/cwd; require POSIX substrate; narrow transition claims | integrated; next round required |
| `R-10` | `f6e1dd95` | clean | `R10-CRIT1-01` | `R10-CRIT2-01` | add `D-45/D-46`; execute post-commit verifier from HEAD bytes; bound provenance probes | integrated; next round required |
| `R-11` | `3465c130` | clean | clean | clean | no new approval-material decision | converged; request final human validation |

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | `deterministic/` é a superfície project-owned para enforcement local. | diretório versionado com `.gitkeep`; `DEC-validator-adoption-trigger`; expected diff | outro path exige renovar diff/handoff | High | Promote to Decision (`D-07`) |
| `A-02` | Python 3 está disponível no contexto de validação Foundation. | guards e exact checks ST-01 usam Python 3 | stack/commands precisam revisão | High | Keep as Assumption |
| `A-03` | Exact checks ST-01 são oráculo temporário de paridade, não código a copiar. | lifecycle trigger + `D-02/D-08` | cutover/test plan muda materialmente | High | Promote to Decision (`D-02,D-08`) |
| `A-04` | Não existe CI repo-owned Foundation a espelhar. | tree sem `.github/workflows`; `D-05` | exige handoff DevOps e renewed approval | High | Promote to Decision (`D-05`) |
| `A-05` | Nenhum fluxo de usuário/runtime é afetado. | diff/out-of-scope restritos a Foundation tooling/docs/tests | exige split e runtime evidence | High | Promote to Decision (`D-01,D-07`) |

## Execution Plan

### Touched Surfaces

- `foundation_documentation/deterministic/validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/foundation_lifecycle/__init__.py`
- `foundation_documentation/deterministic/foundation_lifecycle/parser.py`
- `foundation_documentation/deterministic/foundation_lifecycle/attestation.py`
- `foundation_documentation/deterministic/foundation_lifecycle/runner.py`
- `foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/tests/test_foundation_attestation.py`
- `foundation_documentation/deterministic/tests/test_foundation_runner.py`
- `foundation_documentation/deterministic/README.md`
- `foundation_documentation/evolution_lifecycle.md`
- `foundation_documentation/README.md`
- `foundation_documentation/decisions/README.md`
- `foundation_documentation/decisions/ST-01-foundation-lifecycle-decisions.md`
- `foundation_documentation/system_roadmap.md`
- `foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md` renamed to `foundation_documentation/todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` at closeout.

### Ordered Steps

1. Concluir o ciclo exploratório; após validação humana do conjunto final, congelar/publicar a baseline e repetir os gates formais com TODO + owners + exact contracts do ST-01 no pacote.
2. Após `APROVADO` e authority guard `go`, escrever fixtures/oráculos fail-first e implementar kernel/parser/diagnostics mais consolidações canônicas aprovadas.
3. Implementar até `T-01..T-42` convergir; manter o TODO ativo e o decision target apontando ao active path no candidate SHA.
4. Executar acceptance, old/new parity, adherence, test-quality audit e final review no candidate SHA.
5. Montar a árvore terminal com TODO movido, evidence final, handoffs/cutover e `DEC-validator-adoption-trigger` retargeted para completed; stagear tudo e capturar o tree OID.
6. Materializar o tree OID em diretório temporário read-only e executar os checks sobre esses bytes; guards dependentes de metadata Git provam o mesmo index/tree OID. Depois, provar OID inalterado e ausência de divergência relevante; qualquer diferença exige restage e rerun integral.
7. Executar `--run-attested-suite` contra o tree materializado para gerar o self-attestation determinístico fora da árvore; commitar a árvore imutável com o manifest no commit message e trailers `Validated-Tree`/`Validation-Attestation-SHA256`, executar `--verify-attestation`, confirmar working tree limpa e fazer push do mesmo commit; nenhuma declaração documental posterior é permitida.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** validator e testes podem compartilhar o mesmo erro; cada regra deve falhar contra uma fixture/mutation independente antes do código que a satisfaz.
- **Fail-first targets:** bootstrap weakening, identifier grammar, source graph/headers, index↔record completeness, table cardinality, BLG/DEC syntax+uniqueness, state-conditioned decision/roadmap rules, successor links, link/anchor/path confinement, `PENDING` versus structurally-eligible mapping, historical exclusion/admission, closeout target relocation, Unicode/HTML, bounded/redacted diagnostics e byte-for-byte read-only.
- Fixtures/oráculos são escritos manualmente em temporary directories e não reutilizam helpers internos do parser para construir o expected result.
- Real-repository acceptance e dual-run ST-01/new ocorrem somente após todos os fail-first cases convergirem.

### Test Rule Matrix

| Rule ID | Positive Control | Required Mutation / Negative Case | Required Assertion |
| --- | --- | --- | --- |
| `T-01` | unique required heading/table | missing, duplicate or reordered heading/header | non-zero + rule/path |
| `T-02` | exact row cardinality | missing/extra cell, ambiguous pipe/code span | non-zero + row locator |
| `T-03` | unique valid `BLG-*`/`DEC-*` owners | invalid case/slug, duplicate owner | non-zero + ID |
| `T-04` | repeated reference outside owner | duplicate reference only | remains zero |
| `T-05` | enum from lifecycle | invalid/hidden Unicode/HTML state | non-zero + normalized diagnostic |
| `T-06` | valid relative path under root | missing path, absolute, `..`, symlink escape | non-zero without content leak |
| `T-07` | one literal `PENDING` segment per pending target | explicit pending mapping | remains zero + pending-effect classification |
| `T-08` | complete 1:1 concrete mapping | missing/extra/duplicate/placeholder/contradictory segment | non-zero; never semantic-effective claim |
| `T-09` | invalid historical file in decision subdirectory | historical file remains unindexed | remains zero |
| `T-10` | index links equal root-level record files | unlink, orphan file or duplicate link | non-zero + membership diagnostic |
| `T-11` | bounded/redacted diagnostic | secret-like fixture payload | diagnostic omits value and respects limit |
| `T-12` | portable filesystem manifest plus Git-backed tracked-mode manifest before each pass/fail run | create/delete/rename entry; alter regular bytes, symlink target, or Git modes `100644|100755|120000` | filesystem path/type/bytes/target equality and separate index/tree mode equality; no directory-mode or symlink-chmod dependency |
| `T-13` | complete bootstrap kernel surfaces | remove mandatory owner, heading, schema column or enum member | non-zero + kernel/version diagnostic |
| `T-14` | valid constrained ASCII fragment | duplicate slug, Unicode/encoded/HTML fragment, punctuation/case mismatch | deterministic pass/fail per v1 dialect |
| `T-15` | valid current row for each decision state and acyclic successor chain | Rejected with concrete evidence, missing/forbidden target/evidence, successor label/owner mismatch, fragment, self/unresolved/cyclic successor, same-file multi-row ambiguity, or chain terminating Proposed/Rejected/pending-effect | non-zero + state/column/chain diagnostic; Rejected retained targets/exact PENDING and A→B→C with B Superseded and eligible C Accepted pass; no historical transition claim |
| `T-16` | `Open` roadmap prose and `Exit-Gate-Met` with completed-TODO proof plus optional canonical module/contract links | missing completed TODO; active TODO, artifact/history, README, roadmap-self, escape or other target class | non-zero + roadmap row/target-class diagnostic |
| `T-17` | exact ASCII lifecycle IDs | Unicode, empty component, repeated/leading/trailing separator or uppercase slug | non-zero + identifier diagnostic |
| `T-18` | active target in candidate and completed target in terminal tree | move without atomic decision target/evidence relocation | candidate/final tree each pass only in matching phase |
| `T-19` | document-relative Markdown link and root-relative canonical target both resolve | apply either base to the opposite class, normalized or symlink escape | correct-base controls pass; wrong-base/escape fails with class/path diagnostic |
| `T-20` | one unique nonempty file provenance applying to every decision row | missing, duplicate, empty or placed after the table | non-zero + provenance diagnostic |
| `T-21` | captured tree materialization exactly matches committed bytes | invalid staged/valid worktree split, relevant untracked input or index change after checks | terminal protocol fails before commit and requires full rerun |
| `T-22` | canonical `Validation-Attestation-v1` bytes bound to tree OID and exact argv registry | golden mutations for delimiters/order/encoding/newlines/commands/argv/registry/streams/digests/trailers | independent expected bytes/digest; `--verify-attestation` fails before publication and reports self-attestation trust boundary |
| `T-23` | explicit per-control legacy transition map | omit retained check, fail to replace structural subcontrol, or keep retired snapshot as blocker | deterministic replaced/retired/retained classification; no wholesale/freeform applicability |
| `T-24` | `--run-attested-suite` exact registry execution, closed contexts and canonical stdout | unknown/missing/reordered command, changed argv contract, context swap/escape, dirty or changed Delphi checkout, Foundation index/tree mismatch, changed registry-tool version or executable bytes, unexpected output or nonzero child | fail closed; direct provenance/context bindings and captured raw stream digests match independent fixture oracle; transitive OS/library inputs remain explicitly outside claim |
| `T-25` | no-write source compilation on read-only materialization | syntax mutation or any created `__pycache__`/`.pyc` entry | syntax failure is non-zero; valid run leaves complete filesystem manifest unchanged |
| `T-26` | roadmap authoring guidance links uniquely to lifecycle `Roadmap gate evidence grammar` | missing/duplicate owner link or competing broader local rule | non-zero + owner/guidance diagnostic; lifecycle remains the only semantic rule |
| `T-27` | implemented registry equals the approved table byte-for-byte and reconstructs both digest domains | unknown/reordered entry/field, unknown/nested token, literal transient/absolute path, relocation, legacy fence drift, token escape/substitution mismatch or template/resolved digest confusion | relocation passes without digest drift; every mutation fails before child execution |
| `T-28` | Touched Surfaces and Files Expected exactly cover the authoritative Expected Changed Paths | omit/add a delivery surface in either summary | deterministic equality assertion fails with missing/extra path |
| `T-29` | `delivery-secret-scan` covers every final delivered regular file including deterministic package/tests/docs and completed TODO | secret/private-key mutation in each class; omitted/missing/extra scan path; active/completed phase mismatch | non-zero with redacted path/rule diagnostic; exact scan-set equality; legacy VAL-10 alone cannot satisfy terminal coverage |
| `T-30` | fixed no-bytecode overlay plus Python `-B` on every applicable command | unset/override overlay, remove `-B`, import-heavy command, preexisting/new `.pyc` or `__pycache__`, privileged-runner write attempt | reject registry/env drift; complete before/after materialized-tree manifest equality for each command |
| `T-31` | isolated direct Python with closed unset/set overlay and `-E -s -S -B` | injected `PYTHONPATH`, `PYTHONHOME`, startup/user-site/sitecustomize/usercustomize module or removed flag | influence never loads; registry/env drift fails before execution; system stdlib-only residual is reported |
| `T-32` | exact complete commit-message envelope | changed subject/preamble, missing/extra blank line, unrelated/duplicate trailer or body, trailer reorder, text after trailers, missing/extra final LF | independent byte oracle and verifier reject every alternate envelope |
| `T-33` | verified read-only legacy `{TOOL_DIR}` aliases and isolated Python launcher | PATH shadow, missing/extra alias, alias/target/launcher replacement before or during execution, writable tool dir, unknown nested executable | fail before acceptance; pre/post identity matches bound tool and launcher digests |
| `T-34` | every command gets the complete from-empty environment, verified descendant tool directory and bound Git config manifest | unexpected inherited variable, `BASH_ENV`/`ENV`, Git override/config injection, HOME/XDG influence, alternate index/worktree/object dir, PATH shadow in Delphi guard, capsule/config mutation | fail before/during execution; exact allowlist and pre/post tool/config/capsule identities; scratch writes only under `{RUN_TMP}` |
| `T-35` | Foundation/Delphi local config without includes | unconditional/conditional, relative/absolute and case-variant `include.path`/`includeIf.*.path` | bound Git with `--includes=false` detects and rejects before suite execution; external config is never read |
| `T-36` | every registry command completes below its bound timeout/stream caps | hung child, hung descendant, stdout overflow, stderr overflow, TERM-resistant process and cleanup failure | bounded streaming memory; process-group TERM then 2s KILL; deterministic redacted outcome; no attestation; all capsule paths removed |
| `T-37` | `tree-consistency` entrypoint/package bytes come from materialized tree after runner preflight | unchanged staged tree with modified principal worktree verifier/package or worktree/index data drift | runner rejects before executing worktree code; materialized verifier can only read verified principal root through `{FOUNDATION}` |
| `T-38` | context and cwd independently match each registry row; only tree-consistency bridges materialized cwd to foundation-index inputs | infer cwd from context, give another command the bridge, omit `{FOUNDATION}` verification or admit undeclared input | verifier/runner reject before execution; registry digest preserves both independent fields |
| `T-39` | Linux/WSL POSIX platform provides process group/signals, symlink, `/dev/null`, chmod/read-only operations and `C.UTF-8` | each missing capability and native-Windows suite attempt | platform-preflight fails before remaining commands; Windows Git publication-only path cannot satisfy attestation |
| `T-40` | current-state Rejected shape and Superseded graph | concrete Rejected evidence or invalid successor graph; fixture claims prior state absent canonical history | structural failures are detected; validator emits no historical transition success/failure claim |
| `T-41` | post-commit verifier executes entrypoint/package from read-only captured HEAD materialization | mutate principal-worktree verifier/package after commit while HEAD remains unchanged; HEAD/tree/message mismatch | mutable bytes are never executed; divergence fails before verifier; committed verifier independently accepts only exact envelope/bindings |
| `T-42` | ordered bounded provenance probes for all five tool IDs | hang, forked descendant, stdout/stderr overflow, nonzero version exit, executable replacement during probe, cleanup failure | same streaming/process-group/failure semantics as commands; no attestation on any abnormal result |

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Rationale:** não é bug/regressão; falsos negativos serão provados por mutations durante implementação aprovada.

### Flow Evidence Planning Matrix

| Criterion | User-visible / Runtime Impact | Required Final Lane | Rationale |
| --- | --- | --- | --- |
| `S-01..S-14` | none | `n/a — structure-only` | somente parser/docs/tests Foundation; sem jornada de usuário |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation repository | nenhum job/suite CI repo-owned existe neste slice | `n/a — local validation only` | `n/a` | `n/a — no CI-equivalent claim` | APROVADO | n/a | source tree + `D-05` | validator/unittest ficam na matriz local abaixo |

### Local Validation Matrix

| Surface | Behavior / Scenario | Preconditions | Command | Required Before | Status |
| --- | --- | --- | --- | --- | --- |
| validator acceptance | source graph real válido | consolidated branch@sha | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | Local-Implemented | planned |
| unittest/mutations | `T-01..T-42` | isolated temporary fixtures | `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'` | Local-Implemented | planned |
| legacy transition matrix | pre-migration baseline runs ST-01 `VAL-01/02/08/10`; candidate/terminal Git layer runs `VAL-01/08/10`; `VAL-02` is superseded after approved schema/target mutation | exact contracts read from completed ST-01 TODO; phase identified deterministically | phase matrix `D-19/VAL-07/T-23` + new validator/tests | before delivery reviews | planned |
| terminal-tree confirmation | permanent checks stay green after atomic move/retarget/cutover | read-only materialization of captured tree OID with `active XOR completed`; unchanged index/OID proof and no relevant divergence | validator + unittest on materialized bytes; compatible guards there; Git-metadata guards against the same index/tree OID | before closeout commit | planned |
| immutable publication | committed tree equals validated staged tree and terminal outcomes are immutably self-attested outside that tree | commit body contains deterministic attestation manifest; trailers contain tree OID and manifest digest | materialize HEAD and run committed `--verify-attestation --commit <oid>` under Post-Commit Verification Protocol; verify tree, clean state and remote ref equality; do not claim externally reproducible execution proof | Production-Ready | planned |

### Runtime / Rollout Notes

- `n/a — no runtime, migration, deploy, secret, database, browser or device surface`
- Exact checks ST-01 permanecem requeridos até o novo comando passar e ser publicado.

## Plan Review Gate

- **Status:** `exploratory convergence satisfied — R-11 clean; provisional D-01..D-46 await human validation`
- **Required lenses:** Architecture, Code Quality, Tests, Performance, Security, Elegance, Structural Soundness.
- **Expected focus:** evitar parser frágil, catálogo duplicado, cobertura superficial, bypass histórico e expansão para CI.

### Review Sections

- [x] Architecture — canonical membership, state-conditioned grammar, immutable identifiers and validated-tree closeout integrated.
- [x] Code Quality — narrow grammar, confinement and diagnostics contract added.
- [x] Tests — test-first and `T-01..T-42` matrix added.
- [x] Performance — bounded linear scan; no specialized lane triggered.
- [x] Security — root/symlink confinement and redaction made mandatory.
- [x] Elegance — one project-owned stdlib validator; no parallel catalog.
- [x] Structural Soundness — atomic target relocation and terminal validated-tree commit protocol replace self-referential closeout.

### Issue Cards

- **Issue ID:** `PLAN-01` — decision validity/effectiveness conflated (`high`). Option A: structural `pending-effect`/eligible split (recommended, medium effort/low risk/local blast/low maintenance/neutral performance/high elegance+soundness); Option B: atomic Accepted (high effort/risk/cross-doc); Option C: do nothing (high false-block risk). **Resolution:** integrated into `D-09`, `S-05`, `T-07/08`.
- **Issue ID:** `PLAN-02` — open scan universe/history (`high`). Option A: explicit source graph + grammar (recommended, medium effort/low risk); Option B: hard-code snapshot (low effort/high maintenance); Option C: broad scan (high false-positive risk). **Resolution:** integrated into source graph, `D-01/02/04/10`.
- **Issue ID:** `PLAN-03` — parser/read-only/security proof incomplete (`high`). Option A: mandatory narrow grammar, confinement, redaction and byte snapshot (recommended, medium effort/low risk); Option B: external parser (medium supply-chain risk); Option C: do nothing (high false-green risk). **Resolution:** integrated into `D-03/06`, `T-01..T-12`.
- **Issue ID:** `PLAN-04` — cutover/test/routing evidence incomplete (`high`). Option A: test-first + dual-run + exact implementation routing (recommended, medium effort/low risk); Option B: cut over after new-only local green (medium risk); Option C: do nothing (control gap). **Resolution:** integrated into `D-05/07/08`, matrices and routing.
- **Issue ID:** `PLAN-05` — mutable source graph could self-weaken (`high`). Option A: minimal versioned bootstrap trust kernel (recommended, medium effort/low runtime risk); Option B: duplicate all live truth (high drift); Option C: self-derived only (high false-green risk). **Resolution:** integrated into `D-02`, source graph, `DOD-04`, `T-13`.
- **Issue ID:** `PLAN-06` — index-only decision admission permits silent unlink (`high`). Option A: exact equality with root-level decision files (recommended, low effort/low risk); Option B: dedicated directory migration (higher scope); Option C: keep index-only (false-green). **Resolution:** integrated into `D-04`, `S-06`, `DOD-05`, `T-10`.
- **Issue ID:** `PLAN-07` — pending mapping pass/fail contradiction (`high`). Option A: explicit positional `PENDING` sentinel (recommended, low effort/clear oracle); Option B: new schema columns (higher migration scope); Option C: infer from prose (ambiguous). **Resolution:** integrated into `D-09`, grammar, `T-07/08`.
- **Issue ID:** `PLAN-08` — renderer anchor dialect unspecified (`medium`). Option A: constrained ASCII v1 grammar (recommended, low complexity); Option B: emulate GitHub fully (higher maintenance); Option C: skip anchors (coverage gap). **Resolution:** integrated into `D-11`, grammar, `T-14`.
- **Issue ID:** `PLAN-09` — same-SHA cutover chronology impossible after TODO move (`medium`). Initial two-SHA resolution was invalidated by `AR-F04/F-20`; the authoritative replacement is `PLAN-12` terminal validated-tree protocol.
- **Issue ID:** `PLAN-10` — TODO relocation breaks a canonical decision target (`high`). Option A: atomically retarget the decision record in the terminal tree (recommended); Option B: retain active shim (violates XOR); Option C: broken target. **Resolution:** integrated into `D-14`, expected paths, `T-18`.
- **Issue ID:** `PLAN-11` — decision/roadmap state obligations under-specified (`high`). Option A: seven-column decision schema plus state truth table and Exit-Gate-Met link rule (recommended); Option B: parser heuristics (false-green risk); Option C: ignore lifecycle obligations. **Resolution:** integrated into `D-12/D-13`, grammar, `T-15/16`.
- **Issue ID:** `PLAN-12` — post-validation cutover write invalidates tested SHA (`high`). Option A: validate final staged tree and bind it in commit trailer (recommended); Option B: post-commit doc mutation (untested tree); Option C: external unbound prose. **Resolution:** integrated into `D-08`, `DOD-09`, `VAL-08/09`.
- **Issue ID:** `PLAN-13` — directory membership rule lacked canonical authority (`high`). Option A: consolidate it into decisions index (recommended); Option B: inferred filesystem policy (hidden authority); Option C: index-only omission risk. **Resolution:** integrated into `D-04` and expected canonical changes.
- **Issue ID:** `PLAN-14` — identifier kernel omitted its semantic owner (`medium`). Option A: include Immutable identifiers + exact grammar (recommended); Option B: code-only grammar; Option C: weak slug oracle. **Resolution:** integrated into `D-02`, source graph, `T-17`.
- **Issue ID:** `PLAN-15` — staged tree OID was not mechanically identical to bytes consumed by checks (`high`). Option A: materialize captured OID read-only and prove unchanged index/divergence state (recommended); Option B: trust working tree commands (false-green); Option C: auxiliary checkout/worktree (not authorized). **Resolution:** integrated into `D-15`, `VAL-08/09`, `T-21`.
- **Issue ID:** `PLAN-16` — Markdown links and canonical decision targets require distinct resolution bases (`high`). Option A: declare document-relative versus root-relative bases (recommended); Option B: infer heuristically (nondeterministic); Option C: reject an existing valid class. **Resolution:** integrated into `D-16`, grammar, `T-19`.
- **Issue ID:** `PLAN-17` — lifecycle-required decision provenance was not structurally enforced (`medium`). Option A: one unique per-file provenance field applying to all rows (recommended, preserves seven columns); Option B: add row column (larger schema change); Option C: omit enforcement. **Resolution:** integrated into `D-17`, source graph, `T-20`.
- **Issue ID:** `PLAN-18` — terminal results cannot exist inside the tree before that tree is validated (`high`). Option A: structured commit-message attestation bound to tree and manifest digests (recommended); Option B: mutate docs afterward (invalidates tree); Option C: omit result evidence. **Resolution:** integrated into `D-18`, `S-12`, `DOD-08/09`, `VAL-09`, `T-22`.
- **Issue ID:** `PLAN-19` — legacy exact-check “applicability” was ambiguous and `VAL-02` conflicts with approved schema/target evolution (`high`). Option A: explicit phase/supersession matrix (recommended); Option B: require incompatible dual-run; Option C: silently omit checks. **Resolution:** integrated into `D-19`, `VAL-07`, `T-23`.
- **Issue ID:** `PLAN-20` — byte hashes plus symlink metadata did not prove complete read-only behavior (`medium`). Option A: complete typed fixture-tree manifest equality (recommended); Option B: partial hashes; Option C: trust implementation. **Resolution:** integrated into `D-20`, `DOD-03`, `T-12`.
- **Issue ID:** `PLAN-21` — Superseded could point to a non-effective or ambiguous successor (`high`). Option A: bind exact DEC-ID label to its unique owner and require the chain to terminate Accepted+structurally-eligible (recommended); Option B: allow owner-file ambiguity; Option C: semantic review only. **Resolution:** integrated into `D-21`, decision grammar, `T-15`.
- **Issue ID:** `PLAN-22` — Rejected grammar could erase accepted history or fabricate prior consolidation (`high`). Option A: restrict rejection to Proposed with retained targets/exact PENDING and retire Accepted only via Superseded (recommended); Option B: depend on Git-history comparison; Option C: allow unverifiable current-state prose. **Resolution:** integrated into `D-22`, decision grammar, `T-15`.
- **Issue ID:** `PLAN-23` — symlink permission mutation was not portable (`medium`). Option A: compare target bytes and assert fixed Git mode 120000, with modes tested on regular files/directories (recommended); Option B: synthetic symlink chmod; Option C: skip metadata. **Resolution:** integrated into `D-23`, `T-12`.
- **Issue ID:** `PLAN-24` — final decision semantics risked living only in the tactical TODO/validator (`high`). Option A: consolidate state grammar in lifecycle and membership guidance in decisions index (recommended); Option B: validator-owned semantics; Option C: duplicated owners. **Resolution:** integrated into `D-24`, expected paths, `DOD-06`.
- **Issue ID:** `PLAN-25` — terminal attestation lacked a canonical digest byte domain (`high`). Option A: closed `Validation-Attestation-v1` grammar plus independent golden oracle (recommended); Option B: shared serializer/verifier assumptions; Option C: unbound prose. **Resolution:** integrated into `D-25`, byte grammar, `T-22`.
- **Issue ID:** `PLAN-26` — wholesale VAL-02 retirement hid controls outside the new source graph (`high`). Option A: per-control replaced/retired/retained map (recommended); Option B: impossible wholesale parity; Option C: silent retirement. **Resolution:** integrated into `D-26`, transition map, `T-23`.
- **Issue ID:** `PLAN-27` — attestation bytes lacked an executable command registry and could overstate independent proof (`high`). Option A: closed runner/verifier interface plus explicit self-attestation boundary (recommended); Option B: retain raw outputs externally (new artifact authority); Option C: unverifiable prose. **Resolution:** integrated into `D-27`, byte grammar, `VAL-09`, `T-22/T-24`.
- **Issue ID:** `PLAN-28` — any confined link could satisfy `Exit-Gate-Met` (`high`). Option A: require completed tactical TODO proof and close optional links to canonical module/contract owners (recommended); Option B: broad links plus semantic review; Option C: prose-only. **Resolution:** integrated into `D-28`, source graph, `DOD-07`, `T-16`.
- **Issue ID:** `PLAN-29` — argv and output digests did not bind external implementation bytes or execution substrate (`high`). Option A: closed contexts plus Foundation/Delphi/direct-toolchain provenance and an explicit non-hermetic boundary (recommended); Option B: downgrade external guards to advisory; Option C: claim hermeticity without evidence. **Resolution:** integrated into `D-29`, `S-13`, attestation grammar, `VAL-08/09`, `T-24`.
- **Issue ID:** `PLAN-30` — roadmap published a broader evidence rule while lifecycle/validator planned a closed one (`high`). Option A: lifecycle owns semantics and roadmap links to it without duplicating the rule (recommended); Option B: duplicate exact rules; Option C: hidden validator-only semantics. **Resolution:** integrated into `D-30`, expected paths, source graph, `DOD-06`, `T-26`.
- **Issue ID:** `PLAN-31` — registry named commands but left argv, substitutions and digest domains to post-approval implementation (`high`). Option A: freeze the complete table and closed token grammar now (recommended); Option B: implementation-owned registry semantics; Option C: unhashed transient paths. **Resolution:** integrated into `D-31`, approved registry section, `T-27`.
- **Issue ID:** `PLAN-32` — a single validator file would combine parser, runner, provenance and codec responsibilities (`medium`). Option A: thin CLI plus three bounded internal modules and parallel test seams (recommended); Option B: monolith; Option C: open-ended package. **Resolution:** integrated into `D-32`, expected paths and touched surfaces.
- **Issue ID:** `PLAN-33` — legacy VAL-10 omits new deterministic and completed-TODO delivery surfaces (`high`). Option A: add a terminal scan derived from exact final Expected Changed Paths and retain VAL-10 as compatibility only (recommended); Option B: extend historical script; Option C: claim incomplete coverage. **Resolution:** integrated into `D-33`, registry, `VAL-05`, `T-29`.
- **Issue ID:** `PLAN-34` — normal Python execution may create bytecode in a declared read-only materialization (`high`). Option A: global fixed no-bytecode overlay plus explicit `-B` and manifest proof (recommended); Option B: rely on permissions; Option C: ignore privileged runners. **Resolution:** integrated into `D-34`, payload/environment binding, registry and `T-30`.
- **Issue ID:** `PLAN-35` — bound Python executable still admitted mutable startup path/user customization (`high`). Option A: closed unset/set overlay plus `-E -s -S -B` (recommended); Option B: bind an entire virtualenv; Option C: call it transitive risk. **Resolution:** integrated into `D-35`, registry and `T-31`.
- **Issue ID:** `PLAN-36` — attestation payload grammar omitted the surrounding Git message byte envelope (`high`). Option A: exact subject/body/trailer/final-LF grammar (recommended); Option B: arbitrary preamble/trailers; Option C: rely on Git heuristics. **Resolution:** integrated into `D-36`, byte grammar and `T-32`.
- **Issue ID:** `PLAN-37` — legacy shell payloads could PATH-resolve different binaries from those attested (`high`). Option A: verified private read-only tool directory and isolated Python launcher (recommended); Option B: rewrite historical scripts; Option C: trust ambient PATH. **Resolution:** integrated into `D-37`, environment contract and `T-33`.
- **Issue ID:** `PLAN-38` — non-legacy guards and Bash/Git startup still admitted ambient environment and child lookup (`high`). Option A: construct all child environments from a complete allowlist, extend verified tool dir globally and bind local Git config (recommended); Option B: enumerate only known risky vars; Option C: treat controllable inputs as transitive risk. **Resolution:** integrated into `D-38`, payload/environment contract and `T-34`.
- **Issue ID:** `PLAN-39` — local Git configs could include unbound files (`high`). Option A: reject all include/includeIf directives (recommended); Option B: recursively bind external graph; Option C: ignore includes. **Resolution:** integrated into `D-39`, config contract and `T-35`.
- **Issue ID:** `PLAN-40` — attested children had no timeout/output/capture bounds (`high`). Option A: per-command limits, streaming digests and process-group termination (recommended); Option B: global unbound default; Option C: unbounded capture. **Resolution:** integrated into `D-40`, registry Bounds and `T-36`.
- **Issue ID:** `PLAN-41` — tree-consistency executed mutable worktree code (`high`). Option A: execute materialized code after runner divergence preflight (recommended); Option B: capsule indexed blobs separately; Option C: post-execution detection. **Resolution:** integrated into `D-41`, registry and `T-37`.
- **Issue ID:** `PLAN-42` — global context prose contradicted tree-consistency cwd/source (`high`). Option A: make trust context and cwd orthogonal with one explicit bridge (recommended); Option B: fourth context; Option C: implicit exception. **Resolution:** integrated into `D-42`, registry prose and `T-38`.
- **Issue ID:** `PLAN-43` — POSIX process/signal/filesystem/locale requirements were undeclared (`medium`). Option A: Linux/WSL capability preflight and Windows publication-only exception (recommended); Option B: cross-platform implementation expansion; Option C: late failure. **Resolution:** integrated into `D-43`, registry, readiness and `T-39`.
- **Issue ID:** `PLAN-44` — current sources cannot prove historical Proposed→Rejected transitions (`high`). Option A: enforce observable row/graph and keep history review-owned (recommended); Option B: admit canonical history source; Option C: overclaim. **Resolution:** integrated into refined `D-22`, `D-44`, state grammar and `T-15/T-40`.
- **Issue ID:** `PLAN-45` — post-commit verifier source bytes were not bound to HEAD (`high`). Option A: execute from read-only HEAD materialization under the closed runner (recommended); Option B: trust clean-worktree postcheck; Option C: workspace verifier. **Resolution:** integrated into `D-45`, post-commit protocol, `VAL-09`, `T-41`.
- **Issue ID:** `PLAN-46` — mandatory version probes were outside command resource bounds (`high`). Option A: exact ordered bounded probe protocol (recommended); Option B: trust tool responsiveness; Option C: omit version outputs. **Resolution:** integrated into `D-46`, probe protocol and `T-42`.

### Failure Modes & Edge Cases

- Markdown com coluna deslocada ou registro duplicado.
- IDs válidos referenciados várias vezes sem confundir com owner duplicado.
- Links com anchors, paths relativos e targets existentes.
- Decisão `Accepted` com múltiplos targets e evidência incompleta para um deles.
- Unicode/HTML ocultando enum/ID/estado inválido.
- Histórico inválido excluído versus registro vivo inválido ignorado indevidamente.
- Novo registro válido deve passar sem alteração do código.
- Validator nunca corrige/regrava entradas.

### Residual Unknowns / Risks

- Granularidade do parser pode exigir helper interno, sem justificar dependência externa ou mudança de contrato.
- Mensagens/estrutura interna são implementation details desde que preservem exit, diagnóstico e testes.

## Additional Architectural Opinions

- **Needed:** `no additional exploratory opinion; formal architecture/critique reruns remain required after validation and freeze`
- **Why ambiguity remains:** `none approval-material in R-11; implementation evidence is intentionally deferred until final validation, freeze, formal gates and APROVADO`.
- **Opinion count:** `R-01 through R-11 complete; R-11 architecture + critique A + critique B all clean`
- **Package mode:** `bounded-file-set`
- **Internal reviewer mandate:** `required after freeze; reviewer cannot implement`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Latest TEACH evidence / artifact:** `prepared-pre-freeze` diagnostic on revised package, 2026-09-23, fingerprint `b82442926521`; critique/test-quality/final/verification-debt/architecture decision/adherence `required`; triple/security/performance-concurrency `not_needed`; rerun after renewed freeze for gate evidence.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | shared enforcement + mutation suite |
| `blast_radius` | `cross-stack` | governa Foundation compartilhada, sem produto |
| `behavioral_change_or_bugfix` | `yes` | cria comportamento fail-closed |
| `changes_public_contract` | `no` | sem API/schema/route/auth público |
| `touches_auth_or_tenant` | `no` | sem auth/tenant |
| `touches_runtime_or_infra` | `no` | sem runtime/infra/CI |
| `touches_tests` | `yes` | nova suíte unittest/mutation |
| `critical_user_journey` | `no` | governança interna |
| `release_or_promotion_critical` | `no` | não promove produto |
| `high_severity_plan_review_issue` | `yes` | `PLAN-01..26` include integrated high findings; convergence and formal review still required |
| `explicit_three_lane_request` | `no` | não solicitado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** piso esperado para medium, cross-stack governance e test logic.
- **Impact signals in scope:** `cross-stack documentary governance; deterministic enforcement; tests`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** exact baseline-bound bytes plus SHA-256 boundaries for the frozen TODO, `evolution_lifecycle.md`, `backlog/README.md`, `decisions/README.md`, every linked root-level decision record, `system_roadmap.md`, `project_constitution.md`, `README.md`, and the referenced ST-01 Exact Check Command Contracts.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Canonical multi-lane audit protocol:** `n/a — deterministic floor says triple_review=not_needed`
- **Audit session / round evidence:** `n/a unless triggered`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `findings_integrated`
- **Findings summary:** prior findings remain resolved; substantive `C3-F01..C3-F03` expand the baseline to `D-01..D-23`, while `C3-F04` reconciles bookkeeping. Fresh critique remains required after replacement freeze.
- **Resolution ledger:** prior findings are recorded individually below for deterministic carry-forward.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `F-01` | Integrated | useful | yes | project | n/a | canonical six-column assumptions schema now covers `A-01..A-05` |
| `F-02` | Integrated | useful | yes | project | n/a | explicit source graph and opaque-prose dependency boundary added in `D-01/D-02/D-10` |
| `F-03` | Integrated | useful | partial | project | n/a | `D-09` separates valid `pending-effect` from structural eligibility and semantic truth |
| `F-04` | Integrated | useful | yes | project | n/a | historical admission is now decided only through the explicit source graph |
| `F-05` | Integrated | useful | yes | none | n/a | earlier review-order defect caused renewed validation, refreeze and fresh-review requirement |
| `F-06` | Integrated | useful | yes | project | n/a | cutover now requires same-SHA dual-run, deliverable existence and `active XOR completed` |
| `F-07` | Integrated | useful | yes | project | n/a | test-first strategy and `T-01..T-12` positive/mutation matrix added |
| `F-08` | Integrated | useful | yes | project | n/a | whitespace, diff-scope and secret hygiene validations are separated in `VAL-05` |
| `F-09` | Integrated | useful | yes | none | n/a | planned implementation routing now names `routine-executor` with single-writer/no-worktree topology |
| `F-10` | Integrated | useful | yes | project | n/a | CI-equivalent is explicitly `n/a`; local validator/unittest evidence has its own matrix |
| `F-11` | Integrated | useful | yes | none | n/a | lifecycle, freeze, approval and closeout state were reconciled before renewed validation |
| `F-12` | Integrated | useful | yes | paced | n/a | future dispatch package must contain the exact canonical owner files, not the TODO alone |
| `F-13` | Integrated | useful | yes | paced | n/a | all lifecycle fields now return to renewed-validation and replacement-freeze state |
| `F-14` | Integrated | useful | yes | project | n/a | explicit positional `PENDING` truth table removes pass/fail contradiction |
| `F-15` | Integrated | useful | yes | project | n/a | bidirectional decisions index/root-file equality proves live membership completeness |
| `F-16` | Integrated | useful | yes | project | n/a | initial two-SHA resolution was later invalidated; authoritative replacement is `F-20` terminal validated-tree protocol |
| `F-17` | Integrated | useful | yes | project | n/a | constrained ASCII fragment dialect supplies independent test oracle |
| `F-18` | Integrated | useful | yes | project | n/a | terminal tree atomically retargets validator decision to completed TODO path |
| `F-19` | Integrated | useful | yes | project | n/a | seven-column state grammar and closed placeholder dialect added |
| `F-20` | Integrated | useful | partial | paced | n/a | validated staged-tree OID is bound in immutable closeout commit trailer |
| `F-21` | Integrated | useful | yes | paced | n/a | operational fields returned to D-01..D-14 validation state |
| `F-22` | Integrated | useful | yes | paced | n/a | `D-15` binds checks to a materialized captured tree OID and rejects divergence |
| `F-23` | Integrated | useful | yes | project | n/a | `D-16` distinguishes document-relative Markdown links from root-relative canonical targets |
| `F-24` | Integrated | useful | yes | project | n/a | `D-17` requires unique nonempty per-file provenance applying to every decision row |
| `F-25` | Integrated | useful | partial | paced | n/a | operational fields returned to D-01..D-17 validation/replacement-freeze state |
| `F-26` | Challenged | useful | yes | paced | `bounded-review-package-content-completeness` | package defect, not plan finding; corrected snapshot embedded exact bytes and SHA-256 for every required file before redispatch |
| `C2-F01` | Integrated | useful | yes | paced | n/a | `D-18` separates in-tree protocol/pre-terminal evidence from immutable post-validation commit attestation |
| `C2-F02` | Integrated | useful | yes | project | n/a | `D-19` classifies every referenced ST-01 check by phase and explicit supersession |
| `C2-F03` | Integrated | useful | yes | paced | n/a | lifecycle fields returned to D-01..D-20 validation/replacement-freeze state |
| `C2-F04` | Integrated | useful | yes | project | n/a | `D-20` strengthens read-only proof to complete typed fixture-manifest equality |
| `C3-F01` | Integrated | useful | yes | project | n/a | `D-21` requires every Superseded successor to be Accepted and structurally eligible |
| `C3-F02` | Integrated | useful | yes | project | n/a | `D-22` preserves target/evidence history for Rejected decisions |
| `C3-F03` | Integrated | useful | yes | project | n/a | `D-23` replaces non-portable symlink-mode mutation with class-specific metadata rules |
| `C3-F04` | Integrated | useful | yes | paced | n/a | lifecycle fields returned to D-01..D-23 validation/replacement-freeze state |

- **Evidence / reference:** fresh internal critique over immutable nine-file snapshot at `bca7c106`, 2026-09-24; `overall_assessment=material_findings_present; approval_not_ready`.
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** assumptions `A-01..A-05` govern paths, interpreter, CI and runtime boundary.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03,A-04,A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending`
- **Approval scope:** `pending after convergence, final decision validation, replacement freeze and affected planning gates`
- **Execution not authorized by approval:** `CI/CD, product/runtime, historical rewrites, delphi-ai changes, worktrees or auxiliary checkouts unless separately named`
- **Renewed approval required when:** scope, invariant semantics, validation, expected paths, architecture, risk, exception or CI adoption changes materially.
- **Execution authority:** `not_granted`
- **Pre-gate human token:** Gabriel/user, 2026-09-23, `APROVADO`; it validated the superseded `D-01..D-08` only. Material findings require renewed validation and a new post-gate `APROVADO`.
- **Renewed validation token:** Gabriel/user, 2026-09-23, exact phrase `VALIDO D-01..D-10`; validates the revised decisions, but does not grant implementation authority.
- **Renewal status:** `R-11 convergence criterion satisfied; request exact token VALIDO D-01..D-46, then freeze/publish and rerun formal planning gates.`
- **Latest validation token:** Gabriel/user, 2026-09-24, exact phrase `VALIDO D-01..D-20`; validated and froze the historical baseline, now superseded for approval by `D-21..D-23`; it never granted implementation authority.

## Rules Acknowledgement / Ingestion

Predeclared for pre-approval readiness; reload and bind after `APROVADO`.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | tactical implementation | approval, strict diff, evidence, closeout | implementation before authority | Review until APROVADO + guard |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | phase transitions | phase order/evidence | merging gates | routes execution/closeout |
| `delphi-ai/workflows/docker/todo-contract-refinement-method.md` | current phase | decisions, assumptions, plan | guessed assumptions | approval-ready contract |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | next phase | freeze, reviews, preflight | premature approval request | blocks until ready |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | new tests | meaningful fail-first cases | happy-path-only | governs test design |
| `delphi-ai/skills/test-quality-audit/SKILL.md` | validator trust | adversarial mutations | false confidence | audit after implementation |
| `foundation_documentation/project_constitution.md` | project authority | TODO hierarchy | product drift | project precedence |
| `foundation_documentation/evolution_lifecycle.md` | primary anchor | schemas, owners, history | competing owner | derive from lifecycle |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `pending explicit inclusion in renewed APROVADO`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Routing evidence:** `agent_role_routing_guard.py`, 2026-09-23; `implementation/routine-executor/gpt-5.6-terra/medium/primary-checkout-single-writer/no-worktree`.
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01..D-20` | validated-historical | exact token `VALIDO D-01..D-20`; freeze `0cd991e6` | preserved directions; approval baseline superseded by convergence work |
| `D-21..D-46` | provisional-converged | R-01..R-11; R-11 three-lane clean round | awaiting exact full-set validation token before freeze |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `DEC-validator-adoption-trigger` | Preserve | planned | validator + lifecycle handoff | no module behavior |
| `DEC-single-field-authority` | Preserve | planned | derived-rule implementation | no second owner |
| `DEC-historical-adoption-boundary` | Preserve | planned | exclusion tests | no retroactive migration |
| `DEC-decision-effectiveness-after-consolidation` | Preserve | planned | target tests | all targets required |
| `DEC-immutable-lifecycle-identifiers` | Preserve | planned | ID tests | references may repeat |
| `DEC-provider-neutral-lifecycle-roles` | Preserve | planned | code/docs review | provider is not authority |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| validator + tests + docs + TODO evidence | false greens, parser fragility, path drift, missing mutations | planned | fresh no-context delivery review | pending | required before closeout |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| single-field authority | duplicated state/config in Python | planned | review + mutations | pending | blocker if found |
| historical boundary | broad ignore hiding live failures | planned | adversarial fixtures | pending | blocker if found |
| fail-closed | warnings/zero exit on invalid input | planned | negative CLI tests | pending | blocker if found |
| strict diff | unrelated Foundation/product/CI edits | planned | diff guard | pending | renewed approval on expansion |

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `AR-01..AR-05` | high/medium | release-blocker | integrate in current TODO | mesmos objetivo e boundary do validador; não requer split | fixed-pending-revalidation | revised `D-01..D-10`, source graph, grammar, tests and cutover |
| `F-01..F-08` | high/medium | release-blocker | integrate in current TODO | correções do mesmo contrato de planejamento e verificação | fixed-pending-revalidation | assumptions schema, boundary/effectiveness/history, tests, security and cutover revised |
| `F-09..F-11` | medium | release-blocker | integrate in current TODO | correções de routing, CI terminology, PCV/state bookkeeping | fixed-pending-revalidation | routing, CI terminology, PCV/state bookkeeping revised |
| `AR-R01..AR-R05` | high/medium | release-blocker | integrate in current TODO | mesma arquitetura do validator; trust root, membership, mapping, anchors e state bookkeeping | fixed-pending-revalidation | reconverged `D-02/D-04/D-08/D-09/D-11`; fresh review required |
| `F-12..F-17` | high/medium | release-blocker | integrate in current TODO | mesmos approval/readiness boundaries; nenhum split necessário | fixed-pending-revalidation | full-owner package, lifecycle state, mapping, membership, cutover and anchor grammar revised |
| `AR-F01..AR-F05` | high/medium | release-blocker | integrate in current TODO | same validator architecture and closeout boundary; no split needed | fixed-pending-revalidation | state grammar, canonical membership, identifiers and terminal commit protocol revised |
| `F-18..F-21` | high/medium | release-blocker | integrate in current TODO | same delivery contract and target lifecycle; no split needed | fixed-pending-revalidation | target relocation, state grammar, validated tree and bookkeeping revised |
| `AR-N01..AR-N02` | high/medium | release-blocker | integrate in current TODO | exact-byte closeout and bookkeeping remain inside the same validator boundary | fixed-revalidated | `D-15`; lifecycle state reconciled; exact token `VALIDO D-01..D-17` |
| `F-22..F-25` | high/medium | release-blocker | integrate in current TODO | exact-byte binding, path bases, provenance and bookkeeping are part of the existing validator contract | fixed-revalidated | `D-15..D-17`; exact token `VALIDO D-01..D-17` |
| `AR-PKG-01/F-26` | high | by-design/no-action | repair derived package and redispatch | package completeness defect did not change the governing TODO or architecture | resolved | immutable complete snapshot with per-file SHA-256; substantive redispatch completed |
| `AR2-01/C2-F03` | medium | release-blocker | integrate in current TODO | current-state bookkeeping remains in the same TODO | fixed-pending-revalidation | lifecycle fields reconciled to D-01..D-20 validation state |
| `C2-F01/C2-F02/C2-F04` | high/medium | release-blocker | integrate in current TODO | terminal evidence, legacy parity and read-only proof are approval-material parts of the validator contract | fixed-pending-revalidation | `D-18..D-20`; renewed full-set validation required |
| `AR3-01/C3-F04` | medium | release-blocker | integrate in current TODO | current-state bookkeeping remains in the same TODO | fixed-pending-revalidation | lifecycle fields reconciled to D-01..D-23 validation state |
| `C3-F01..C3-F03` | high/medium | release-blocker | integrate in current TODO | decision lifecycle coherence and portable read-only proof are approval-material parts of the validator contract | fixed-pending-revalidation | `D-21..D-23`; renewed full-set validation required |
| `R1-ARCH-01/C4-F01` | high | release-blocker | integrate in current TODO | multi-hop successor integrity is approval-material lifecycle semantics | fixed-pending-convergence | refined `D-21`, successor graph and `T-15` |
| `R1-ARCH-02` | high | release-blocker | integrate in current TODO | canonical semantic ownership is inside the validator adoption boundary | fixed-pending-convergence | `D-24`, expected paths and `DOD-06` |
| `R1-ARCH-03/C4-F02` | high | release-blocker | integrate in current TODO | structural versus temporal rejection guarantee changes the enforceable contract | fixed-pending-convergence | refined `D-22` and state grammar |
| `R1-ARCH-04/C4-F03` | high/medium | release-blocker | integrate in current TODO | portable filesystem/Git oracle split is part of current test trust | fixed-pending-convergence | refined `D-23` and `T-12` |
| `C4-F04` | high | release-blocker | integrate in current TODO | canonical attestation bytes are required for independent closeout verification | fixed-pending-convergence | `D-25`, attestation grammar and `T-22` |
| `R1-CRIT2-VAL02` | high | release-blocker | integrate in current TODO | legacy control retirement affects cutover claims | fixed-pending-convergence | `D-26`, legacy transition map and `T-23` |
| `R2-ARCH-01/R2-ARCH-02/R2-CRIT2-02` | high | release-blocker | integrate in current TODO | legal rejection transitions and accepted-history preservation are lifecycle semantics | fixed-pending-convergence | refined `D-22`, state grammar and `T-15` |
| `R2-CRIT2-01` | high | release-blocker | integrate in current TODO | successor identity must be unambiguous across multi-row records | fixed-pending-convergence | refined `D-21`, exact link label/owner grammar and `T-15` |
| `R2-ARCH-03/R2-CRIT1-02/R2-CRIT2-03` | high | release-blocker | integrate in current TODO | executable command identity and honest trust claims govern terminal evidence | fixed-pending-convergence | `D-27`, runner/verifier interface, registry and self-attestation boundary |
| `R2-CRIT1-01` | high | release-blocker | integrate in current TODO | roadmap gate evidence needs closed structural authority classes | fixed-pending-convergence | `D-28`, source graph and `T-16` |
| `R2-CRIT2-04` | medium | release-blocker | integrate in current TODO | write-producing compilation contradicts read-only materialization | fixed-pending-convergence | no-write compile oracle in `VAL-04`, attestation registry and `T-25` |
| `R2-CRIT1-03` | low | release-blocker | integrate in current TODO | incorrect decision-range bookkeeping obscured current state | resolved | corrected R-01 range to `D-21..D-26` |
| `R3-ARCH-01/R3-CRIT1-02/R3-CRIT2-01..03` | high/medium | release-blocker | integrate in current TODO | external implementation identity, execution substrate and dependency readiness bound terminal evidence | fixed-pending-convergence | `D-29`, `S-13`, context/provenance grammar and `T-24` |
| `R3-CRIT1-01` | high | release-blocker | integrate in current TODO | canonical roadmap guidance must not contradict the enforced lifecycle rule | fixed-pending-convergence | `D-30`, expected `system_roadmap.md` alignment and `T-26` |
| `R4-CRIT1-01/R4-CRIT2-01` | high | release-blocker | integrate in current TODO | registry identity and transient-path substitution are approval-material terminal trust semantics | fixed-pending-convergence | `D-31`, approved registry table and `T-27` |
| `R4-CRIT1-03` | medium | release-blocker | integrate in current TODO | module boundaries affect maintainability, independent testing and allowed diff | fixed-pending-convergence | `D-32`, bounded package/test seams |
| `R4-ARCH-01/R4-CRIT1-02` | low/medium | release-blocker | integrate in current TODO | inconsistent surface summaries could misroute implementation or evidence | resolved | Touched Surfaces and Files Expected synchronized; `T-28` |
| `R5-CRIT1-01` | high | release-blocker | integrate in current TODO | terminal security coverage must include every newly delivered and moved surface | fixed-pending-convergence | `D-33`, `delivery-secret-scan`, `VAL-05`, `T-29` |
| `R5-CRIT2-01` | high | release-blocker | integrate in current TODO | Python bytecode writes contradict exact read-only tree validation | fixed-pending-convergence | `D-34`, environment/argv binding and `T-30` |
| `R6-ARCH-01` | high | release-blocker | integrate in current TODO | mutable Python startup paths are direct controllable execution inputs | fixed-pending-convergence | `D-35`, isolated flags/overlay and `T-31` |
| `R6-CRIT1-01` | high | release-blocker | integrate in current TODO | canonical attestation requires a complete unambiguous Git message envelope | fixed-pending-convergence | `D-36`, exact envelope and `T-32` |
| `R6-CRIT2-01` | high | release-blocker | integrate in current TODO | legacy nested tool lookup must execute the identities recorded in provenance | fixed-pending-convergence | `D-37`, verified private PATH/launcher and `T-33` |
| `R7-ARCH-01/R7-CRIT1-01/R7-CRIT2-01` | high | release-blocker | integrate in current TODO | every child process and repository-config input must remain inside the attested execution boundary | fixed-pending-convergence | `D-38`, from-empty environment, global verified tool dir/config manifest and `T-34` |
| `R8-ARCH-01/R8-CRIT2-01` | high | release-blocker | integrate in current TODO | local Git include graphs would escape the bound config manifest | fixed-pending-convergence | `D-39`, include rejection and `T-35` |
| `R8-CRIT1-01` | high | release-blocker | integrate in current TODO | unbounded children/streams can hang or exhaust the attested runner | fixed-pending-convergence | `D-40`, registry Bounds and `T-36` |
| `R8-CRIT2-02` | high | release-blocker | integrate in current TODO | verifier results must be produced by attested code bytes | fixed-pending-convergence | `D-41`, materialized tree-consistency and `T-37` |
| `R9-ARCH-01/R9-CRIT2-02` | high | release-blocker | integrate in current TODO | execution context and cwd/source semantics must not contradict | fixed-pending-convergence | `D-42`, orthogonal fields/sole bridge and `T-38` |
| `R9-CRIT1-01` | medium | release-blocker | integrate in current TODO | terminal process/resource semantics require a declared capable substrate | fixed-pending-convergence | `D-43`, platform-preflight and `T-39` |
| `R9-CRIT2-01` | high | release-blocker | integrate in current TODO | current-state graph cannot prove unadmitted historical transitions | fixed-pending-convergence | refined `D-22`, `D-44` and `T-15/T-40` |
| `R10-CRIT1-01` | high | release-blocker | integrate in current TODO | final acceptance must execute verifier code from committed bytes | fixed-pending-convergence | `D-45`, post-commit HEAD materialization and `T-41` |
| `R10-CRIT2-01` | high | release-blocker | integrate in current TODO | mandatory provenance probes need the same bounded execution semantics | fixed-pending-convergence | `D-46`, bounded probe protocol and `T-42` |

## Security Risk Assessment

- **Risk level:** `low`
- **Why this risk level:** parser local read-only; riscos são path escape ou conteúdo sensível em diagnóstico.
- **Attack surface in scope:** filesystem paths and Markdown content inside Foundation root.
- **Attack simulation decision:** `not_needed`
- **Review evidence:** audit floor `SEC-NOT-TRIGGERED`; code/final review ainda verificará root confinement, ausência de shell interpolation e secret-value echo.
- **Residual security risk:** malformed Markdown may deny validation by design; diagnostics must remain bounded; tool provenance is direct but not a hermetic OS/shared-library attestation.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `low`
- **Why this level:** sem endpoint/query/runtime de produto, mas o runner local cria subprocessos e captura streams; `D-40` limita tempo, bytes, memória, descendants e cleanup por comando.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `n/a — no endpoint` | `before_local_implemented` | `EPS-E1` | `not_applicable` | `none` | `none` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `n/a — no frontend` | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `n/a — no backend mutation` | `before_local_implemented` | `BCI-INV` | `not_applicable` | `none` | `none` |
| `RLS` | `runtime-load-stress-validation` | `not_needed` | `low` | `n/a — local docs tooling` | `before_production_ready` | `RLS-E1` | `not_applicable` | `none` | `none` |

### Lane Detail Packets

#### `EPS`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** no endpoint, repository query or data-access path is changed.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

#### `FRC`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** no frontend, async UI or retriggerable user flow is changed.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

#### `BCI`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** validator is read-only and does not create backend mutation/idempotency surfaces.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

#### `RLS`
- **Policy schema version:** `pcv-1`
- **Trigger rationale:** no runtime/queue/worker/realtime/bulk production path or SLO claim changes.
- **Recorded at (UTC):** `2026-09-23T21:21:29Z`
- **Executor ID:** `primary-orchestrator`
- **Evidence object:** `n/a — trigger_result=not_needed and state=not_applicable`

## Verification Debt Assessment

- **Audit decision:** `required because complexity=medium`
- **Audit status:** `not_run`
- **Why this outcome:** guard logic/assertions can create hidden false-green debt.
- **Inline code TODO debt:** `pending implementation scan`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none planned`

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** validator trust depends on mutation coverage and negative assertions.
- **Trigger signals in scope:** `complexity=medium; touches_tests=yes; fail-closed enforcement`
- **Required evidence matrix:** each `DOD-02/03/05` scenario, expected failure and assertion quality.
- **Audit status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** enforcement determinístico deve ser desafiado após implementação.
- **Impact signals in scope:** `cross-stack governance; architecture protection harness; tests`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen decisions, diff, test/mutation outputs, adherence e audits.
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; reviewer cannot implement`
- **Review focus:** `adherence|regressions|validation evidence|security/performance residuals|elegance|structural soundness|verification debt`
- **Final review status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** R-11 satisfied the user-directed convergence criterion with no new approval-material decision; TODO remains active awaiting validation/freeze/formal gates/approval.
- **Post-commit/push status:** R-11 clean convergence bookkeeping is local pending validation/publication checks; no implementation claim.
- **Next path/status action:** publish R-11 bookkeeping and obtain `VALIDO D-01..D-46`; then freeze/publish the baseline and run formal gates before requesting `APROVADO`.

## Commands

### Planning / pre-approval

- `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`
- `python3 delphi-ai/tools/todo_authority_guard.py foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md --pre-approval`
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py --repo-root foundation_documentation foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md`

### Planned implementation validation

- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`
- `python3 -m unittest discover -s foundation_documentation/deterministic/tests -p 'test_*.py'`
- `PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 python3 -E -s -S -B -c "from pathlib import Path; import sys; [compile(Path(p).read_bytes(), p, 'exec') for p in sys.argv[1:]]" foundation_documentation/deterministic/validate_foundation_lifecycle.py foundation_documentation/deterministic/foundation_lifecycle/__init__.py foundation_documentation/deterministic/foundation_lifecycle/parser.py foundation_documentation/deterministic/foundation_lifecycle/attestation.py foundation_documentation/deterministic/foundation_lifecycle/runner.py foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py foundation_documentation/deterministic/tests/test_foundation_attestation.py foundation_documentation/deterministic/tests/test_foundation_runner.py`
- `git -C foundation_documentation diff --check`

## Files Expected

- `foundation_documentation/deterministic/validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/foundation_lifecycle/__init__.py`
- `foundation_documentation/deterministic/foundation_lifecycle/parser.py`
- `foundation_documentation/deterministic/foundation_lifecycle/attestation.py`
- `foundation_documentation/deterministic/foundation_lifecycle/runner.py`
- `foundation_documentation/deterministic/tests/test_validate_foundation_lifecycle.py`
- `foundation_documentation/deterministic/tests/test_foundation_attestation.py`
- `foundation_documentation/deterministic/tests/test_foundation_runner.py`
- `foundation_documentation/deterministic/README.md`
- `foundation_documentation/evolution_lifecycle.md`
- `foundation_documentation/system_roadmap.md`
- `foundation_documentation/README.md`
- `foundation_documentation/decisions/README.md`
- `foundation_documentation/decisions/ST-01-foundation-lifecycle-decisions.md`
- `foundation_documentation/todos/active/process/TODO-foundation-lifecycle-structural-validator.md` renamed to `foundation_documentation/todos/completed/process/TODO-foundation-lifecycle-structural-validator.md` at closeout.
