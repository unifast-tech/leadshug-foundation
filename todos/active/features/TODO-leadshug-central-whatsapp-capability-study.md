# TODO — Estudo comparativo de capacidades do Central-Whatsapp

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Program:** `leadshug-pre-code-evolution-program`
- **Backlog item:** `BLG-central-whatsapp-capability-study`

## Context

O LeadsHug foi reconstruído a partir de referências históricas do Central-Whatsapp, mas os repositórios seguiram evoluções independentes. Antes de implementar novas funcionalidades, o projeto precisa saber quais capacidades surgiram ou amadureceram no Central, quais já existem no LeadsHug e quais ideias merecem avaliação posterior dentro da arquitetura atual.

Este trabalho é um estudo de capacidades e comportamentos. O Central-Whatsapp permanece uma referência legada independente e somente leitura; não é upstream do LeadsHug e não autoriza cópia de código, sincronização de árvores ou adoção automática de decisões antigas.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md`
- **Primary story ID:** `ST-02`
- **Why this is the right current slice:** ST-01 está concluído e o catálogo comparativo é a próxima etapa pré-código. Ele produz evidência para decisões futuras sem misturar priorização (`ST-04`) nem o estudo específico do Whatsflow (`ST-03`).
- **Direct-to-TODO rationale:** `n/a`

## Contract Boundary

- Este TODO define o catálogo comparativo e a evidência necessária para considerá-lo confiável.
- A entrega descreve capacidades em linguagem própria do LeadsHug; ela não importa código, esquema, infraestrutura ou terminologia interna sem reinterpretação.
- Descobertas permanecem neste TODO enquanto forem linhas do mesmo catálogo. Uma segunda entrega independente ou mudança de arquitetura exige novo TODO e nova aprovação.

## Implementation Intent

- **Current delivery:** produzir um único catálogo de gaps de capacidade entre snapshots congelados do Central-Whatsapp e do LeadsHug, preservando todas as origens e derivando transversalidade sem apagar proveniência.
- **Planned next steps:** `ST-03` estuda separadamente canais no Whatsflow; `ST-04` prioriza oportunidades depois dos dois estudos.
- **Anticipatory implementation authorized now:** `none`
- **Rationale:** primeiro separar fatos, lacunas e lições; decisões de produto e implementação continuam fora deste trabalho.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `none`
- **Next exact step:** concluir assurance, revisão final independente e guards de closeout sobre o catálogo já produzido.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** catálogo e ledger foram produzidos dentro do escopo aprovado; validações e revisões de delivery estão em curso.
- **Exit condition:** catálogo, ledger, auditorias e evidências de delivery concluídos; TODO publicado e movido para `completed/features/`.

## Scope

- [x] `S-01` Publicar no catálogo um manifesto reproduzível com identidade, base, head, tree, pathspec permitido, papel e comandos exatos de verificação para cada snapshot.
- [x] `S-02` Inventariar capacidades relevantes do Central oficial surgidas ou alteradas após a baseline de importação.
- [x] `S-03` Inventariar capacidades relevantes do hub não oficial surgidas ou alteradas após a baseline de importação.
- [x] `S-04` Examinar separadamente o overlay local do hub incorporado ao antigo LeadsHug, sem atribuí-lo ao Central independente.
- [x] `S-05` Comparar cada capacidade candidata com o LeadsHug API/Web atual e seus contratos canônicos.
- [x] `S-06` Classificar cada item por `origins[]`, época, transversalidade derivada, presença observada no LeadsHug, força da evidência, valor, risco, dependências e disposição recomendada.
- [x] `S-07` Registrar lições negativas e exclusões explícitas para evitar que antipadrões legados sejam tratados como oportunidades.
- [x] `S-08` Manter um ledger completo da população analisada, validar por amostragem bidirecional determinística/estratificada e publicar um único artefato de análise.

## Out of Scope

- `OOS-01` Alterar código, testes, schema, migrations, configuração, runtime, deploy ou dados do LeadsHug.
- `OOS-02` Copiar ou portar código, dependências, variáveis, segredos, infraestrutura ou dados do Central-Whatsapp.
- `OOS-03` Criar sincronização, subtree, submodule ou dependência de runtime entre os projetos.
- `OOS-04` Inspecionar, listar ou reproduzir conteúdo de `hub-whatsapp/secrets/**` ou qualquer credencial.
- `OOS-05` Definir prioridade final, roadmap de implementação ou aprovar automaticamente capacidades (`ST-04`).
- `OOS-06` Modelar em profundidade canais com múltiplas formas de atendimento (`ST-03`).
- `OOS-07` Alterar módulos, contratos ou decisões canônicas antes de um TODO futuro específico.
- `OOS-08` Avaliar produção ou executar chamadas reais a provedores externos.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `foundation_documentation:main`
- **Promotion lane path:** `main (documentação somente)`
- **Lane-promoted threshold for this TODO:** `commit/push em foundation_documentation:main`
- **Production-ready threshold for this TODO:** `artefato publicado e TODO fechado em completed/features/`
- **Topology:** checkout principal, single-writer, sem worktrees.

## Promotion Evidence (Required Before Lane-Promoted / Production-Ready)

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Catálogo ST-02 e closeout | `main@pending` | `n/a` | `n/a` | `direct documentation publication` | pending |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `.` | `main@6344bf64d8bb7330d8c992aaff93833fc65ca6ed` | `working_tree` |
| LeadsHug API | `../api-app` | `5db3fbe2043428749895fc3ff6441e9457467dd0` | `working_tree` |
| LeadsHug Web | `../web-app` | `6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9` | `working_tree` |

Central oficial, Central hub e LeadsHug legado são fontes externas somente leitura, governadas pelo `Snapshot Manifest Contract`; não são superfícies de diff/escrita deste TODO.

### Snapshot Manifest Contract

O catálogo deve reproduzir esta matriz com paths absolutos redigidos para identidade lógica, sem depender do branch ou working tree corrente.

| Identity | Base SHA | Head SHA | Head tree | Exact allowed pathspecs / role |
| --- | --- | --- | --- | --- |
| `leadshug-api` | `n/a` | `5db3fbe2043428749895fc3ff6441e9457467dd0` | `4386ac3c732702c9d869f8a9482ccd99750e6ef8` | `src/** prisma/** test/** package.json README.md`; alvo de comparação |
| `leadshug-web` | `n/a` | `6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9` | `8b83239b57e31ec34bfbf911d35af035866e3ff0` | `src/** e2e/** public/** package.json README.md`; alvo de comparação |
| `central-official` | `6517f197c97d0b5bcad886d26eb0d28a813b47ca` | `337f3e4839cef8ca400de87b3de088a79d512944` | `1ee054a4630b0448b4432429e8b68b30f6e87ed5` | `src/** public/** migrations/** docs/** clientes/** package.json schema.sql wrangler.jsonc README.md CONTEXTO-CONTINUIDADE.txt`; origem oficial |
| `central-hub` | `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2` | `51bc16e544c7625a71c3012d8adef656c6392c37` | `e8823e402d1110d3fec0f6d2923490536f97254a` | `backend/** frontend/** docs/** docker-compose.yml README.md Caddyfile .env.backend.example .env.evolution.example .env.example`; origem hub; `secrets/**` não é allowlisted |
| `legacy-hub-overlay` | `beb655cd3109fc3a537fca38c2b49f8c64853e7b` | `994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2` | `ff142200b038ae642f24c467b8f084cbc78e6229` | `hub-whatsapp/backend/** hub-whatsapp/frontend/** hub-whatsapp/docs/** hub-whatsapp/docker-compose.yml hub-whatsapp/README.md hub-whatsapp/Caddyfile hub-whatsapp/.env.backend.example hub-whatsapp/.env.evolution.example hub-whatsapp/.env.example`; origem overlay; `hub-whatsapp/secrets/**` não é allowlisted |

Evidência de fonte usa somente `repo@sha:path:symbol-or-commit`; código/payload não é copiado. Inspeção usa objetos Git congelados e expande somente os pathspecs literais da matriz; nenhum placeholder ou path fora da allowlist é aceito.

### Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| Foundation | `todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md` | `A/M/D` | contrato, evidência e movimento atômico no closeout |
| Foundation | `todos/completed/features/TODO-leadshug-central-whatsapp-capability-study.md` | `A` | destino do closeout |
| Foundation | `artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md` | `A/M` | entrega documental única do ST-02 |
| Foundation | `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` | `M` | atualização factual do estado/evidência de ST-02 no closeout |
| Foundation | `backlog/README.md` | `M` | transição factual do item no closeout |

### Not Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| LeadsHug API | `api-app/**` | `any` | estudo sem código |
| LeadsHug Web | `web-app/**` | `any` | estudo sem código |
| Foundation | `modules/**` | `any` | nenhuma decisão de produto será promovida neste estudo |
| Foundation | `contracts/**` | `any` | contratos de runtime permanecem inalterados |
| Foundation | `project_constitution.md` | `any` | arquitetura permanece inalterada |
| Foundation | `system_roadmap.md` | `any` | priorização pertence ao ST-04 |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)

Qualquer caminho não classificado deve ser analisado antes da entrega. Expansão material requer validação humana e novo `APROVADO`.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** novas linhas de capacidade, evidência adicional, correção de classificação e melhorias locais no catálogo único.
- **Must update or split the TODO:** nova entrega independente, alteração canônica, priorização, implementação ou catálogo acima de 40 capacidades substantivas que deixe de ser revisável como uma unidade.

## Catalog Row Contract

O catálogo é Markdown, mas usa o schema fechado abaixo. Tooling/schema executável novo está fora de escopo porque não acrescentaria evidência ao estudo.

| Field | Type / cardinality | Allowed values / rule |
| --- | --- | --- |
| `capability_id` | required unique string | `CAP-###` |
| `title` | required non-empty string | linguagem própria do LeadsHug |
| `origins[]` | required set, min 1 | `official|hub|legacy_overlay` |
| `origin_epochs{}` | required map, one key per origin | each value `preexisting_gap|post_baseline_evolution` |
| `cross_origin` | required derived boolean | `true` iff `origins[]` has more than one value |
| `central_evidence[]` | required non-empty set | `repo@sha:path:symbol-or-commit` |
| `leadshug_evidence[]` | required set | evidence refs or the complete `not_found_protocol` record |
| `implementation_state` | required enum | `observed_present|partial|not_found_after_protocol|uncertain` |
| `evidence_strength` | required enum | `direct|corroborated|indirect|insufficient`; `uncertain` requires `insufficient` |
| `user_value` | required non-empty string | no priority claim |
| `risks[]` | required set | may be empty only with explicit `none_observed` |
| `dependencies[]` | required set | may be empty only with explicit `none_observed` |
| `disposition_recommendation` | required enum | `discard|study|candidate_st04` |
| `canonical_rejection_ref` | nullable evidence ref | required only when `discard` claims an existing canonical rejection; otherwise recommendation only |
| `policy_applicability{}` | required six-key map | see applicability contract below |
| `notes` | optional string | no copied source/payload |

Cada linha também contém a matriz de aplicabilidade exigida pela policy: `tenancy`, `BU`, `conversation`, `provider_adapter`, `audit` e `channel_policy`, cada uma como `applies|not_applicable|unknown` com evidência ou justificativa. `cross_origin` é derivado de `origins[]`; não é origem autônoma.

`not_found_after_protocol` exige: definir o fingerprint comportamental e sinônimos; executar buscas por SHA em todos os pathspecs allowlisted do API e Web; verificar contratos/módulos canônicos relacionados; registrar consultas/pathspecs sem persistir payload; e obter uma segunda checagem dirigida na superfície esperada. Superfície inacessível, busca incompleta ou conflito vira `uncertain`, nunca ausência.

## Source Ledger Contract

O ledger muitos-para-muitos usa este schema Markdown fechado:

| Field | Type / cardinality | Allowed values / rule |
| --- | --- | --- |
| `source_unit_id` | required unique string | `SU-` + primeiros 16 hex de SHA-256 do UTF-8 exato `origin|sha|path|locator|source_unit_type`; `/` é o separador de path |
| `origin` | required enum | `official|hub|legacy_overlay` |
| `sha` | required full commit SHA | deve pertencer ao intervalo/snapshot da origem |
| `path` | required string | path relativo admitido pela allowlist literal da origem; `@outside-allowlist` é permitido apenas em `commit_surface` com `excluded_reason=outside_st02`, quando a comparação hash-only prova que o commit não tocou path admitido e o path real permanece sem inspeção |
| `locator` | required string | símbolo estável ou ordinal `surface-NNN` no snapshot congelado |
| `source_unit_type` | required enum | `code_symbol|ui_flow|migration_contract|documentation_behavior|test_evidence|commit_surface` |
| `capability_ids[]` | required set | zero ou mais `CAP-###` existentes |
| `supports[]` | required set | zero ou mais `CAP-###` existentes |
| `duplicate_of[]` | required set | zero ou mais `SU-*` existentes; sem autorreferência ou ciclo |
| `excluded_reason` | nullable enum + rationale | `non_behavioral_chore|generated_or_vendor|duplicate_change|outside_st02|sensitive_unreadable|superseded_fix` |

Integridade: ao menos um entre `capability_ids[]`, `supports[]`, `duplicate_of[]` ou `excluded_reason` deve estar preenchido. `excluded_reason` é mutuamente exclusivo com `capability_ids[]` e `supports[]`; `duplicate_of[]` pode coexistir somente com `excluded_reason=duplicate_change`. Todo ID referenciado deve resolver no mesmo ledger/catálogo. `mapping-kind` é derivado (`capability`, `support`, `duplicate`, `excluded`) da presença desses campos; uma unidade entra em cada estrato derivado aplicável. A entrada textual exata usada no hash é preservada na linha, tornando seleção e reexecução determinísticas.

## Definition of Done

- [x] `DOD-01` O manifesto registra bases, heads, trees, pathspecs, papéis e comandos verificáveis para todos os snapshots.
- [x] `DOD-02` Cada capacidade tem evidência do Central e evidência/estado correspondente no LeadsHug, ou incerteza explícita.
- [x] `DOD-03` Cada capacidade informa `origins[]`, `epoch`, `cross_origin`, `implementation_state`, `evidence_strength`, valor, riscos, dependências e disposição recomendada sem misturar presença e desejabilidade.
- [x] `DOD-04` Itens posteriores à baseline estão separados dos itens que já existiam na baseline mas não foram reimplementados.
- [x] `DOD-05` Lições negativas e exclusões estão explícitas; uma rejeição como não desejada exige `canonical_rejection_ref`, caso contrário permanece recomendação.
- [x] `DOD-06` O ledger mapeia toda a população admitida para capacidade, duplicata ou exclusão justificada; a auditoria estratificada não encontra item relevante sem mapeamento.
- [x] `DOD-10` Cada capacidade avalia `tenancy`, `BU`, `conversation`, `provider_adapter`, `audit` e `channel_policy` como `applies|not_applicable|unknown`, com evidência/justificativa.
- [x] `DOD-07` O catálogo não contém segredos, dados pessoais, payloads sensíveis nem trechos de código copiados.
- [x] `DOD-08` Nenhuma recomendação é apresentada como prioridade aprovada ou autorização de implementação.
- [ ] `DOD-09` Gates documentais e revisão final passam; feature brief/backlog refletem apenas o estado factual concluído.

## Validation Steps

- [x] `VAL-01` Revalidar bases, heads e trees do manifesto com comandos Git por SHA e confirmar alcance dos commits de importação.
- [x] `VAL-02` Comparar os intervalos completos `6517f197..337f3e4` (129 não-merge) e `94ce80aa..51bc16e` (66 não-merge) somente nos pathspecs permitidos.
- [x] `VAL-03` Comparar o único commit do overlay que toca `hub-whatsapp/**` entre `beb655cd..994e1e8`, excluindo `secrets/**`.
- [x] `VAL-04` Verificar o ledger completo e auditar deterministicamente 100% de `not_found_after_protocol`, `uncertain`, rejeições canônicas, itens cross-origin e alegações sensíveis; amostrar de forma estratificada os estados positivos restantes.
- [ ] `VAL-05` Usar comandos allowlisted sem patch/body ou metadados pessoais por padrão; não persistir outputs brutos; executar scanner de segredo no diff final e revisão explícita de PII sem alegar garantia absoluta.
- [ ] `VAL-06` Executar validador estrutural, `git diff --check` e guards de diff, autoridade, conclusão e closeout aplicáveis.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01` | Scope | Manifesto reproduzível | doc+command | catálogo §§3–3.1; revalidação Git por SHA/tree em 2026-09-25 | read-only snapshots | passed | cinco identidades com papel/pathspec/comando |
| `S-02` | Scope | Inventário oficial | doc+ledger | catálogo §§4 e 7; 129 commits oficiais | central-official frozen SHA | passed | 126 tocam allowlist; 3 sentinelas fail-closed |
| `S-03` | Scope | Inventário hub | doc+ledger | catálogo §§4 e 7; 66 commits do hub | central-hub frozen SHA | passed | 64 tocam allowlist; 2 sentinelas fail-closed |
| `S-04` | Scope | Overlay separado | doc+ledger | catálogo §§3, 7 e 8.2; `SU-4b78629f9cae4e5e` | legacy frozen SHA | passed | único commit allowlisted, excluído como infraestrutura |
| `S-05` | Scope | Comparação com LeadsHug atual | doc+review | catálogo §§4.2 e 6; API/Web nos SHAs congelados | LeadsHug API/Web | passed | presença, parcialidade ou protocolo de ausência por CAP |
| `S-06` | Scope | Classificação normalizada | doc+integrity check | catálogo §§4.1–5 | n/a | passed | 27/27 linhas atendem o schema e a policy |
| `S-07` | Scope | Lições negativas/exclusões | doc+review | catálogo §9 e exclusões do ledger | n/a | passed | antipadrões não viraram oportunidades |
| `S-08` | Scope | Ledger e auditoria bidirecional | doc+command+review | catálogo §§7–8; verificador local: 204 IDs únicos, 0 issues | local/read-only | passed | amostra catálogo 23/27; ledger 83/204 |
| `DOD-01` | Definition of Done | Manifesto completo | doc+command | catálogo §§3–3.1; heads/trees revalidados | read-only snapshots | passed | identidades e comandos reproduzíveis |
| `DOD-02` | Definition of Done | Evidência Central e LeadsHug por capacidade | doc+integrity check | catálogo §4.2 e §6 | frozen snapshots | passed | 27/27 capacidades resolvem evidência/estado |
| `DOD-03` | Definition of Done | Campos semânticos separados | doc+review | catálogo §§4.1–4.2 | n/a | passed | presença não foi confundida com desejabilidade |
| `DOD-04` | Definition of Done | Época separada | doc+review | `origin_epochs{}` em catálogo §4.1 | n/a | passed | `preexisting_gap` e `post_baseline_evolution` explícitos |
| `DOD-05` | Definition of Done | Rejeições e lições qualificadas | doc+review | catálogo §§4.1 e 9 | n/a | passed | descarte canônico somente quando há referência; demais são recomendações |
| `DOD-06` | Definition of Done | População totalmente mapeada | command+review | catálogo §§7–8; 204/204 IDs válidos, 0 unmapped | local/read-only | passed | 177 mapeamentos capability/support e 27 exclusões |
| `DOD-07` | Definition of Done | Conteúdo sensível ausente | scan+manual review | exact sensitive-content check + revisão PII/payload no diff | Foundation diff | passed | scan silencioso sem match; revisão explícita sem PII/payload/código copiado |
| `DOD-08` | Definition of Done | Sem prioridade/implementação implícita | doc+review | catálogo §§1, 4.1 e 10 | n/a | passed | agrupamento do ST-04 é explicitamente não priorizado |
| `DOD-09` | Definition of Done | Gates e espelhos factuais | guard+review | delivery gates, feature brief e backlog | Foundation | in-progress | depende de revisão final e closeout |
| `DOD-10` | Definition of Done | Seis limites da policy | doc+integrity review | catálogo §5 | n/a | passed | 27/27 capacidades têm seis chaves |
| `VAL-01` | Validation Steps | SHAs/trees/alcance | command | `git[.exe] rev-parse` e `rev-list` em 2026-09-25 | frozen snapshots | passed | hashes iguais ao manifesto |
| `VAL-02` | Validation Steps | Intervalos Central completos | command+ledger | 129 oficial + 66 hub; catálogo §7 | frozen snapshots | passed | totais incluem as cinco sentinelas fora da allowlist |
| `VAL-03` | Validation Steps | Overlay allowlisted | command+ledger | `rev-list ... -- hub-whatsapp/<allowlist>` = 1 | legacy snapshot | passed | `secrets/**` não enumerado nem lido |
| `VAL-04` | Validation Steps | Integridade e amostragem | command+review | catálogo §8; hash da lista `acb1de38...e63` | local/read-only | passed | 100% dos estados/alegações de risco revisados |
| `VAL-05` | Validation Steps | Leitura/publicação segura | scan+manual review | exact sensitive-content check; revisão explícita PII/payload | Foundation diff | passed | `PASS` em 2026-09-25; repetir após integração final |
| `VAL-06` | Validation Steps | Validador e guards | command | lifecycle validator e `diff --check` exit 0; guards pendentes | Foundation | in-progress | completion/closeout somente após review final |

## External Dependency Readiness (Required When External Systems Matter)

- Nenhum sistema externo de runtime é necessário.
- Repositórios de referência são somente leitura; hashes congelados mantêm a reprodutibilidade se os branches avançarem.
- As duas `main` foram revalidadas em 2026-09-25: o oficial avançou 56 commits desde o snapshot anterior `9368421`; o hub permaneceu em `51bc16e`.

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality` para crítica/revisão documental obrigatória
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| Strategic / CTO-Tech-Lead | Assurance / Tester-Quality | desafiar cobertura, rastreabilidade e conclusões | TODO e catálogo | completed; fresh no-context test-quality audit `no_material_findings`, 2026-09-25 |

## Complexity

- **Level (`small|medium|big`):** `medium`
- **Checkpoint policy:** um checkpoint consolidado antes de `APROVADO` e revisão final após o catálogo.
- **Why this level:** vários repositórios e três origens de evidência, porém uma entrega documental, sem runtime nem implementação.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:**
  - `foundation_documentation/modules/inbox-and-conversations.md`
  - `foundation_documentation/modules/audit-and-history.md`
- **Planned decision promotion targets:** `none in ST-02; findings remain analysis inputs for ST-04`
- **Module decision consolidation targets:** `none; future implementation TODOs must promote accepted decisions`

## Decision Pending (Resolve Before Freeze)

- Nenhuma decisão material pendente. Integração operacional validada por `VALIDO INTEGRAÇÃO RC-01..RC-04 SEM NOVAS DECISÕES` em 2026-09-25.

## Decisions (Resolved Before Freeze)

- [x] `D-01` Usar o manifesto por repositório com base/head/tree/pathspec e comparar o intervalo oficial completo até `337f3e4839cef8ca400de87b3de088a79d512944`; categorizar gaps preexistentes e evolução posterior.
- [x] `D-02` Preservar `official`, `hub` e `legacy_overlay` em `origins[]`; `cross_origin` é derivado e nunca substitui a proveniência.
- [x] `D-03` Comparar capacidades/comportamentos, não arquivos, com evidência `repo@sha:path:symbol-or-commit` e avaliação dos seis limites da policy por capacidade.
- [x] `D-04` Separar `implementation_state` (`observed_present|partial|not_found_after_protocol|uncertain`) de `evidence_strength` e `disposition_recommendation`; rejeição do produto exige `canonical_rejection_ref`. Presença observada não afirma saúde produtiva.
- [x] `D-05` Manter um ledger completo da população e um catálogo único até 40 capacidades; acima disso, pausar para propor divisão. Auditar 100% dos estados/alegações de maior risco e amostrar deterministicamente os positivos.
- [x] `D-06` Tratar disposições (`descartar`, `estudar`, `candidata ao ST-04`) apenas como recomendação fundamentada; prioridade e canonização pertencem ao `ST-04` ou a TODO futuro aprovado.
- **Human revalidation:** usuário, `REVALIDO D-01..D-06 APÓS IC-01..IC-06`, conversa de 2026-09-25.
- **Operational integration validation:** usuário, `VALIDO INTEGRAÇÃO RC-01..RC-04 SEM NOVAS DECISÕES`, conversa de 2026-09-25.

### Decision Validation Review (Prepared Pre-Freeze)

| Decision | Technical validation | Evidence | Outcome |
| --- | --- | --- | --- |
| `D-01` | Os commits-base são exatos; manifesto e intervalo oficial foram corrigidos até o head atual congelado. | Trees importados `76e80538...` e `f926eca3...`; head oficial `337f3e4`, tree `1ee054a4...`. | revalidated-by-user |
| `D-02` | O overlay incorporado é uma origem histórica distinta e transversalidade não apaga origem. | Entre `beb655cd` e `994e1e8`, apenas `994e1e8` toca `hub-whatsapp/`; `cross_origin` passa a ser derivado. | revalidated-by-user |
| `D-03` | Comparação por capacidade continua correta, agora com schema/proveniência e policy applicability explícitos. | 129 commits não-merge no oficial e 66 no hub; policy exige seis limites por inspiração. | revalidated-by-user |
| `D-04` | Presença técnica, força da evidência e desejabilidade foram separadas. | Crítica `IC-03`; evidência estática não comprova saúde operacional e rejeição exige autoridade canônica. | revalidated-by-user |
| `D-05` | Ledger completo + auditoria estratificada substituem amostragem aberta. | Crítica `IC-02`; limite 40 permanece stop condition, nunca truncamento. | revalidated-by-user |
| `D-06` | Recomendações continuam sem autoridade de roadmap. | O backlog é dono da disposição e `ST-04` da síntese/priorização. | revalidated-by-user |

**Material-decision sweep:** `IC-01..IC-06` foram absorvidos nos mesmos seis IDs; nenhum `D-07` é necessário. A versão revisada foi revalidada pelo usuário e congelada em `707b336b`.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `modules/integrations-and-channels.md#Invariants` | provider como adapter; segredo fora de logs/docs/fixtures/client; falha determinística | Preserve | três invariantes explícitos do módulo |
| `modules/inbox-and-conversations.md#Invariants` | conversa única BU/contato; webhook idempotente; janela/capacidade do canal | Preserve | três invariantes explícitos do módulo |
| `modules/audit-and-history.md#Invariants` | histórico append-oriented; tenant/BU scope; leitura independente de escrita | Preserve | três invariantes explícitos do módulo |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-06` revisadas e revalidadas exatamente como registradas em `Decisions`.
- **Historical invalidated baseline:** `cff19546`; preservado como proveniência da primeira crítica.
- **Historical invalidated reviewed baseline:** `1dac5eaf`; preservado como baseline da segunda crítica.
- **Current freeze scope:** decisões preservadas, integração validada de `RC-01..RC-04`, manifesto/schema corrigidos, Scope/Out of Scope, Definition of Done, Validation Steps, Test Strategy e Diff Expectation Contract.
- **Renewal trigger:** qualquer mudança material nesses campos requer nova validação e novo `APROVADO`.

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `not_needed`
- **Why this applies:** o estudo registra evidência e recomendações; não muda arquitetura nem contratos.
- **Deviation / debt being retired:** `n/a`
- **Target steady-state after closeout:** Central permanece referência independente; LeadsHug permanece dono de suas decisões.
- **Temporary exceptions allowed:** `none`
- **Cutover / removal condition:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** crítica formal e guards precisam de um contrato reproduzível publicado antes de emitir evidência.
- **Trigger stage:** `before the first planning-side review or guard run`.
- **Status:** `passed`; integração validada, commitada e publicada antes da crítica final de planejamento.
- **Gate status:** `no_material_findings`
- **Freeze target:** decisões, manifesto/schema, escopo, DoD, validação, estratégia de auditoria e diff contract.
- **Baseline branch:** `main`
- **Baseline commit:** `707b336b`
- **Baseline push reference:** `origin/main`
- **Evidence / reference:** `git_write_authority_guard.py` retornou `go`; `git.exe push origin main` publicou `0ff8a5c3..707b336b` em 2026-09-25.
- **Findings summary:** decisões e integração `IC/RC` congeladas; nenhum blocker de publicação.
- **Historical invalidation evidence:** baseline `cff19546`, crítica `IC-01..IC-06`, verdict `findings`.
- **Current invalidation evidence:** baseline `1dac5eaf`, crítica renovada `RC-01..RC-04`, verdict `findings`.
- **Waiver authority / reference (required if waived):** `n/a`.
- **Pre-freeze packet-prep rule:** `pre-freeze evidence remained provisional until the recorded commit/push completed`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** confirmar que integrações pós-crítica não alteraram materialmente o contrato validado.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`.
- **Baseline source:** `Review Baseline Freeze -> 707b336b`.
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`.
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`.
- **No-go handling rule:** `return to review/revalidation; no automatic rollback`.
- **Gate status:** `no_material_findings`
- **Findings summary:** `0 de 22 seções materiais alteradas em relação a main@707b336b`.
- **Evidence / reference:** `foundation_documentation/artifacts/tmp/leadshug-central-whatsapp-capability-study-scope-drift.json`; guard retornou `Overall outcome: go` em 2026-09-25.
- **Waiver authority / reference (required if waived):** `n/a`.

## Questions To Close

- [x] Revalidar conjuntamente `D-01..D-06` revisadas após `IC-01..IC-06`.
- [x] Validar a integração de `RC-01..RC-04` sem novas decisões de produto.
- [x] Após os gates de planejamento, registrar `APROVADO` para executar o catálogo.

## Assumptions Preview (Required Before Plan Review)

- Hashes congelados são a unidade de reprodutibilidade; branches podem avançar sem mudar o escopo.
- Histórico, docs e código demonstram presença de capacidade, não automaticamente sua qualidade ou adequação.
- Ausência só será afirmada após busca no API, Web e documentação atual; caso contrário, será `Incerto`.
- `secrets/**`, valores de ambiente, dados reais e payloads sensíveis são excluídos mesmo quando aparecem no histórico.
- A terminologia Mantenedora → Setor → BU e conversa independente de transporte prevalece sobre nomes legados.

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | O estado observável do LeadsHug pode ser confrontado nas superfícies congeladas de API e Web sem executar produção. | `api-app/src/main.ts`; `web-app/src/App.tsx`; hashes/tree no Snapshot Manifest | estados ficam `uncertain` e o estudo não pode afirmar presença/ausência | High | Keep as Assumption |
| `A-02` | Integrações oficiais e não oficiais permanecem separadas por superfícies explícitas no LeadsHug atual. | `api-app/src/surfaces/webhooks/meta.controller.ts`; `api-app/src/surfaces/webhooks/evolution.controller.ts` | qualquer conclusão por origem deve ser reclassificada e o inventário reaberto | High | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces

- Escrita: TODO, catálogo, atualização factual do feature brief e backlog no closeout.
- Leitura: Foundation; LeadsHug API/Web; Central oficial/hub; snapshot legado incorporado.

### Ordered Steps

1. Revalidar hashes, proveniência e limpeza das árvores de referência.
2. Gerar inventários por histórico e superfícies funcionais nas três origens.
3. Normalizar capacidades, deduplicar e separar evolução pós-baseline de lacunas preexistentes.
4. Verificar cada candidato no LeadsHug e confrontar módulos/contratos canônicos.
5. Preencher valor, risco, dependências, disposição e exclusões sem definir prioridade.
6. Executar amostragem bidirecional, revisão de privacidade/segredos e crítica de conclusões.
7. Corrigir achados, preencher evidência, atualizar estados factuais e fechar o TODO.

### Test Strategy

- Validação documental e histórica somente leitura.
- População do ledger: todos os 195 commits não-merge pós-baseline do Central (129 oficial, 66 hub), o único commit do overlay que toca `hub-whatsapp/**` e as superfícies funcionais atuais identificadas nos snapshots allowlisted; população total de commits: 196.
- Cada commit é decomposto em unidades-fonte atômicas por superfície/comportamento. Cada unidade registra `source_unit_id`, origem, SHA, path/symbol, tipo, `capability_ids[]` (zero ou muitos), `supports[]` (zero ou muitos), `duplicate_of[]` (zero ou muitos) e `excluded_reason` anulável. Uma unidade só pode ter todos os arrays vazios quando `excluded_reason` estiver preenchido.
- Auditoria de 100% dos itens `not_found_after_protocol`, `uncertain`, com rejeição canônica, cross-origin ou alegação sensível.
- Auditoria catálogo → fontes: nos estados positivos restantes, seleção por estratos `origin × origin_epoch × implementation_state`; ordenar por `capability_id` e revisar todos quando o estrato tiver até cinco itens; acima disso, mínimo de cinco mais IDs cujo SHA-256 textual tenha primeiro byte divisível por quatro.
- Auditoria fontes → catálogo: estratificar separadamente por `origin × source-unit-type × mapping-kind` (`capability|support|duplicate|excluded`) e aplicar a mesma regra determinística; revisar 100% das unidades sem destino válido e das exclusões sensíveis.
- Qualquer unidade relevante sem mapeamento, referência que não resolve ou exclusão injustificada reprova a validação e reabre o inventário.
- O limite de 40 capacidades aciona proposta de divisão; nunca interrompe ou trunca o ledger.

### Flow Evidence Planning Matrix

| Flow / Criterion | User-visible or runtime impact now? | Planned Evidence | Runtime Lane | Waiver Rationale |
| --- | --- | --- | --- | --- |
| Catálogo ST-02 | no | rastreabilidade entre snapshots, catálogo e estado LeadsHug | n/a | análise sem mudança de runtime/UI |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundation lifecycle | TODO, análise, backlog e feature brief | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | approval/delivery | passed | exit 0 em 2026-09-25 | validação documental; não é alegação de CI de produto |
| Markdown/git hygiene | documentação | `git -C foundation_documentation diff --check` | delivery | passed | exit 0 em 2026-09-25 | inclui caminhos esperados; nenhum teste de produto se aplica |

### Runtime / Rollout Notes

- `n/a`: nenhuma mudança executável ou rollout.

## Plan Review Gate

- **Status:** `passed; all planning findings integrated, pre-approval guards passed and execution approved`.
- **Review baseline:** `foundation_documentation:main@cff19546` com evidência de freeze em `d2837312`.
- **Review scope:** cobertura, falsos positivos/negativos, separação histórica, segurança e suficiência da amostragem.
- **Outcome:** revisão primária encontrou dois riscos operacionais; crítica independente encontrou quatro altos e dois médios. Todos foram integrados, alterando materialmente o contrato.

### Issue Cards

| ID | Severity | Finding | Resolution | Status |
| --- | --- | --- | --- | --- |
| `PR-01` | medium | O checkout Windows aparece totalmente modificado quando lido pelo Git do WSL devido a LF/CRLF, criando risco de diff falso ou pull inseguro. | Usar `git.exe` para estado/diff dos dois Central e manter hashes como autoridade reproduzível. | Integrated |
| `PR-02` | medium | Enumeração ampla do hub poderia atravessar `secrets/**`, mesmo sem intenção de publicar valores. | Excluir o path da enumeração/leitura e validar o artefato final por ausência de segredo/PII. | Integrated |
| `IC-01` | high | Intervalo oficial terminava no snapshot antigo e working tree podia contaminar evidência. | Manifesto base/head/tree/pathspec e intervalo corrigido até `337f3e4`; evidência por objeto Git congelado. | Integrated |
| `IC-02` | high | Amostragem aberta não sustentava cobertura. | Ledger completo da população, auditoria determinística/estratificada e 100% dos estados de maior risco. | Integrated |
| `IC-03` | high | Origem, transversalidade, presença e desejabilidade estavam misturadas. | `Catalog Row Contract` separa `origins[]`, época, estado, força, recomendação e rejeição canônica. | Integrated |
| `IC-04` | high | Faltavam os seis limites da policy e invariantes completos dos módulos. | Matriz por capacidade e baseline modular corrigida para todos os invariantes. | Integrated |
| `IC-05` | medium | Proteção de segredo/PII não era fail-closed nos intermediários. | Comandos allowlisted, sem patch/body/metadados pessoais, sem output bruto persistido e revisão final de segredo/PII. | Integrated |
| `IC-06` | medium | Estado do TODO contradizia validação/freeze/crítica. | Máquina de estado consolidada como `review`, baseline anterior invalidada e revalidação explicitamente pendente. | Integrated |
| `RC-01` | high | Pathspec do overlay não excluía o segredo relativo e comandos tinham placeholders. | Allowlist literal por repositório/origem; `secrets/**` não está admitido; scanner final entra na validação. | Integrated |
| `RC-02` | high | Ledger um-para-um e amostragem por capacidade não provavam cobertura fonte→catálogo. | Unidade-fonte atômica muitos-para-muitos e auditorias determinísticas independentes nos dois sentidos. | Integrated |
| `RC-03` | high | Schema não fechava tipos/domínios, epoch cross-origin e protocolo de ausência. | Schema Markdown fechado, `origin_epochs{}` e protocolo completo; tooling novo rejeitado como complexidade sem valor probatório. | Integrated/Challenged |
| `RC-04` | medium | Espelhos de estado continuavam contraditórios. | Estado consolidado para integração pendente; baseline `1dac5eaf` invalidada explicitamente. | Integrated |
| `FC-01` | high | Ledger muitos-para-muitos não tinha tipos, identidade e integridade referencial fechados. | `Source Ledger Contract` define schema, hash/ID estável, domínios, cardinalidades e regras referenciais. | Integrated |
| `FC-02` | medium | Scanner imprimia a linha que poderia conter segredo. | Scanner usa `rg -q` e mensagens redigidas; nenhum match é ecoado. | Integrated |
| `FC-03` | medium | Espelhos ainda diziam que freeze/crítica estavam pendentes após publicação. | Next step, Active Work State, Plan Review, Critique e coherence gate foram reconciliados. | Integrated |

### Failure Modes & Edge Cases

- Commits distintos podem representar a mesma capacidade: deduplicar sem perder evidência de evolução.
- Uma capacidade pode atravessar oficial e hub: registrar como transversal e manter evidência de cada origem.
- Ausência não comprovada permanece `Incerto`, nunca `Ausente` por inferência.
- Se o catálogo ultrapassar 40 capacidades substantivas, pausar e propor divisão antes de produzir entregas independentes.
- Branches podem avançar depois do freeze; somente os hashes registrados pertencem ao estudo aprovado.

### Residual Unknowns / Risks

- A relevância de uma superfície pode exigir julgamento; mitigar com amostragem bidirecional e exclusões justificadas.
- Alguns commits de correção revelam lições operacionais, não capacidades; classificá-los como evidência de risco/antipadrão quando aplicável.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`
- **Latest TEACH evidence / artifact:** `foundation_documentation/artifacts/tmp/leadshug-central-whatsapp-capability-study-audit-escalation-v3.json`; fingerprint `75992daf3f8f`; `Overall outcome: go`.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | múltiplos repositórios, uma entrega documental |
| `blast_radius` | `cross-module` | integrações/canais, inbox/conversas e auditoria |
| `behavioral_change_or_bugfix` | `no` | análise sem alteração de comportamento |
| `changes_public_contract` | `no` | nenhum contrato será alterado |
| `touches_auth_or_tenant` | `no` | restrições são lidas, não modificadas |
| `touches_runtime_or_infra` | `no` | nenhum runtime ou infraestrutura será tocado |
| `touches_tests` | `no` | nenhuma suíte de produto será alterada |
| `critical_user_journey` | `no` | estudo pré-código |
| `release_or_promotion_critical` | `no` | não participa de release do produto |
| `high_severity_plan_review_issue` | `yes` | `IC-01..IC-04` foram altos e estão integrados; o audit floor será recalculado após novo freeze |
| `explicit_three_lane_request` | `no` | nenhuma solicitação de auditoria em três lanes |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** baseline obrigatória e depth expandido por complexidade média com blast radius cross-module (`CRITIQUE-BASELINE-ALWAYS`, `CRITIQUE-EXPANDED-RISK-SIGNALS`).
- **Impact signals in scope:** `cross-module blast radius`.
- **Package mode:** `bounded-file-set`.
- **Package minimum contents:** TODO congelado, feature brief, policy de legado e três módulos âncora.
- **Critique isolation mode:** `fresh internal no-context reviewer`.
- **Internal reviewer mandate:** `required; fresh stateless no-context internal reviewer, not the implementing agent`.
- **Canonical multi-lane audit protocol:** `n/a`.
- **Audit session / round evidence:** `n/a`.
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`.
- **Critique status:** `findings_integrated`
- **Findings summary:** `IC-01..IC-06`, `RC-01..RC-04` e `FC-01..FC-03` possuem resolução explícita; riscos residuais aceitos são julgamento na decomposição, limite de evidência estática e natureza heurística do scanner.
- **Evidence / reference:** revisores internos stateless `/root/st02_independent_critique` (`cff19546`), `/root/st02_revised_critique` (`1dac5eaf`) e `/root/st02_final_planning_critique` (`707b336b`), verdicts `findings`, 2026-09-25.
- **Waiver authority / reference:** `n/a`.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `IC-01` | Integrated | useful | no | none | n/a | manifesto e intervalo corrigidos |
| `IC-02` | Integrated | useful | no | none | n/a | ledger e auditoria determinística |
| `IC-03` | Integrated | useful | no | none | n/a | schema normalizado |
| `IC-04` | Integrated | useful | no | none | n/a | policy e invariantes completos |
| `IC-05` | Integrated | useful | no | none | n/a | procedimento fail-closed de leitura/publicação |
| `IC-06` | Integrated | useful | no | none | n/a | estado/freeze reconciliados |
| `RC-01` | Integrated | useful | no | none | n/a | allowlists literais e scanner final |
| `RC-02` | Integrated | useful | no | none | n/a | ledger muitos-para-muitos e duas auditorias |
| `RC-03` | Integrated | useful | partial | none | n/a | schema Markdown fechado; tooling executável desnecessário foi desafiado |
| `RC-04` | Integrated | useful | no | none | n/a | máquina de estado novamente reconciliada |
| `FC-01` | Integrated | useful | no | none | n/a | schema fechado do source ledger |
| `FC-02` | Integrated | useful | no | none | n/a | scanner silencioso/redigido |
| `FC-03` | Integrated | useful | no | none | n/a | espelhos de estado reconciliados |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** o estudo depende de snapshots de código para distinguir presença, parcialidade e ausência após protocolo.
- **Trigger stage:** `after critique convergence and before APROVADO`.
- **Guard scope:** `snapshot manifest, implementation-state protocol and cited source paths`.
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`.
- **Gate status:** `no_material_findings`
- **Findings summary:** `A-01/A-02 paths and frozen repository heads verified locally; no wrong-code assumption found`.
- **Evidence / reference:** `test -f` on four cited code files; API/Web and Central head checks on 2026-09-25.
- **Waiver authority / reference:** `n/a`.

## Approval

- **Decision validation:** `REVALIDO D-01..D-06 APÓS IC-01..IC-06` e `VALIDO INTEGRAÇÃO RC-01..RC-04 SEM NOVAS DECISÕES`, usuário, 2026-09-25.
- **Execution approval:** `APROVADO`, usuário, 2026-09-25.
- **Approved by:** usuário, com a frase exata `APROVADO`, em 2026-09-25.
- **Approval scope:** executar exclusivamente o catálogo documental ST-02, seu ledger, validações, revisões e closeout previstos neste TODO; sem alteração de código, runtime, contratos ou decisões canônicas do LeadsHug.
- **Required phrase after plan gates:** `APROVADO`

## Rules Acknowledgement / Ingestion

Recarregado após `APROVADO` em 2026-09-25; execução permanece documental, single-writer e sem worktrees.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | governa a execução do ST-02 por TODO | autoridade, sequência de gates e evidência | iniciar execução antes de aprovação | manter o TODO em `review` até `APROVADO` e guards verdes |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | governa o preflight atual | freeze, drift, assumptions, regras e routing | solicitar aprovação com gate pendente | exigir `preflight-go` antes do pedido de `APROVADO` |
| `delphi-ai/workflows/docker/audit-escalation-method.md` | define o piso de auditoria proporcional | decisões de crítica/final review/test quality/verification debt | inventar ou omitir lanes requeridas | preservar fingerprint `75992daf3f8f` e executar gates de delivery derivados |
| `delphi-ai/workflows/docker/independent-critique-method.md` | a crítica independente era obrigatória antes da aprovação | isolamento do revisor, baseline congelada e tratamento explícito | auto-revisão ou achado silenciosamente descartado | conservar `IC`, `RC` e `FC` com resolução e evidência |
| `delphi-ai/workflows/docker/todo-execution-boundary-method.md` | governa a execução agora autorizada | limite aprovado e regras recarregadas | ampliar objetivo ou tocar código | executar somente catálogo/ledger/evidência documental após authority guard verde |
| `delphi-ai/workflows/docker/todo-delivery-gates-method.md` | governa a prova e revisão pós-execução | evidência 1:1, auditorias e guards | alegação agregada ou fechamento antecipado | completar matrizes, assurance e guards antes de delivery |
| `delphi-ai/workflows/docker/todo-closeout-promotion-method.md` | governa publicação e fechamento | mesmo TODO, estado e disposition explícitos | deixar entrega concluída em `active/` | publicar em `main`, mover para `completed/features/` e validar closeout |
| `foundation_documentation/policies/central_whatsapp_independent_legacy_policy.md` | Central é referência independente, não componente do LeadsHug | proveniência por origem, separação oficial/não oficial e soberania do LeadsHug | copiar código/segredos ou criar vínculo de runtime | limitar a execução a leitura de snapshots e publicação documental |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `not authorized; execution remains with the primary agent`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** one writer in canonical checkout; reviewers read-only
- **Guard outcome:** `go`
- **Routing evidence:** `agent_role_routing_guard.py` confirmou lane executor, modelo/esforço e topologia em 2026-09-25.
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation (Mandatory Before Delivery)

| Decision | Delivery evidence | Outcome |
| --- | --- | --- |
| `D-01` | catálogo §§3–4 separa baseline/head e `preexisting_gap|post_baseline_evolution`; heads/trees revalidados | Adherent |
| `D-02` | `origins[]`, `origin_epochs{}` e `cross_origin` são campos separados em 27/27 capacidades; overlay tem ledger próprio | Adherent |
| `D-03` | catálogo descreve capacidades, usa refs `repo@sha:path:locator` e matriz de seis limites; nenhum código foi copiado | Adherent |
| `D-04` | `implementation_state`, `evidence_strength` e `disposition_recommendation` permanecem independentes | Adherent |
| `D-05` | catálogo tem 27 capacidades, abaixo do stop condition; ledger completo 204/204 e auditoria estratificada publicada | Adherent |
| `D-06` | conclusão do ST-04 declara ausência de ordem aprovada e exige TODO futuro para implementação | Adherent |

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Module decision ref | Preservation evidence | Outcome |
| --- | --- | --- |
| `modules/integrations-and-channels.md#Invariants` | matriz §5 trata adapter, segredo e falha como limites; nenhum módulo/contrato foi alterado | Preserved |
| `modules/inbox-and-conversations.md#Invariants` | comparação registra conversa/BU/capacidade sem substituir conversa canônica por modelo legado | Preserved |
| `modules/audit-and-history.md#Invariants` | riscos e evidências mantêm tenant/BU/audit explícitos; catálogo não promove histórico legado como contrato | Preserved |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| ST-02 documentary delivery candidate | falsos verdes no ledger, drift de escopo, alegações prescritivas, privacidade e rastreabilidade | passed | integridade local 27 CAP/204 SU/0 issues; lifecycle e diff hygiene exit 0; review independente ainda governa o closeout | nenhum P1/P2 conhecido antes da revisão final | não há pipeline/Copilot nem mudança executável; qualquer achado material da revisão reabre este preflight |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| soberania do LeadsHug | cópia mecânica, acoplamento ou decisão legada promovida | passed | catálogo §§1–2, 5, 9–10 e diff review | none | apenas capacidade/evidência foi transportada em linguagem própria |
| completude do ledger | unidade omitida, referência quebrada, exclusão com mapping | passed | verificador local: 204 IDs únicos, hash/ref/exclusividade e destino; 0 issues | none | cinco sentinelas permanecem hash-only e fail-closed |
| scanner heurístico Delphi | `TODO`/`panic` em superfície Go | passed after triage | `rule_spirit_anti_pattern_scan.sh --stack all` em 2026-09-25; 1 warning | false positive no nome do workflow `todo-driven-execution-method.md` dentro do TODO documental | não existe código Go no diff; finding sem P1/P2 e sem ação |
| strict diff | path fora do contrato | passed | `todo_diff_expectation_guard.py` retornou `Overall outcome: go` em 2026-09-25 | primeira execução expôs paths de repositório relativos ao root errado | contrato corrigido para `.`, `../api-app`, `../web-app`; 4 paths classificados, 0 forbidden/unclassified |

## Promotion Finding Routing Ledger

| Finding ID | Finding Source | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PR-01..PR-02` | planning review | medium | release-blocker | corrigir Git Windows/WSL e exclusão de segredo | mesmo TODO; segurança/reprodutibilidade do estudo | resolved | manifesto e procedimento allowlisted |
| `IC-01..IC-06` | independent critique | high/medium | release-blocker | fechar snapshots, cobertura, semântica, policy, privacidade e estado | mesmo TODO; contrato pré-aprovação | resolved | integração + revalidação humana D-01..D-06 |
| `RC-01..RC-04` | renewed critique | high/medium | release-blocker | fechar allowlists, ledger muitos-para-muitos, schema e estado | mesmo TODO; contrato pré-aprovação | resolved | `VALIDO INTEGRAÇÃO RC-01..RC-04 SEM NOVAS DECISÕES` |
| `FC-01..FC-03` | final planning critique | high/medium | release-blocker | fechar schema do ledger, scanner silencioso e espelhos | mesmo TODO; contrato pré-aprovação | resolved | baseline `707b336b`; `APROVADO` subsequente |
| `RS-01` | rule-spirit heuristic | warning | false-positive/no-action | nenhuma | texto documental contém o nome canônico `todo-driven-execution-method.md`; não há Go | resolved | triagem humana de 2026-09-25 |

## Security Risk Assessment (Mandatory Before Delivery)

- **Audit decision:** `not_needed` pelo audit floor (`SEC-NOT-TRIGGERED`); risco documental continua controlado localmente.
- **Risk:** baixo; exclusão de segredos/PII e leitura somente foram mantidas.
- **Evidence:** `hub-whatsapp/secrets/**` não foi enumerado nem lido; nenhum output bruto foi persistido; revisão explícita do TODO/catálogo não encontrou PII, payload ou trecho copiado; exact sensitive-content check retornou `PASS` em 2026-09-25. O scanner é apoio heurístico, não garantia absoluta.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Audit decision:** `not_needed` pelo audit floor (`PCV-NOT-TRIGGERED`).
- **Risk:** `n/a` para runtime; análise executada de forma somente leitura, limitada aos snapshots/pathspecs congelados e sem concorrência de escrita.

## Verification Debt Assessment (Required Before `Completed`)

- **Audit decision:** `required` antes de `Completed` (`VDA-MEDIUM-BIG-OR-RELEASE`).
- Pendente. Lacunas de amostragem e classificações `Incerto` serão dívida explícita, nunca ocultada.

## Independent Test Quality Audit Gate

- **Audit decision:** `recommended`
- **Audit status:** `no_material_findings`
- **Evidence / reference:** reviewer stateless `/root/st02_test_quality_audit`, pacote `artifacts/tmp/st02-test-quality-dispatch.json`, 2026-09-25; reproduziu 204 IDs/hashes, 27 vínculos e a seleção estratificada 83/204.
- **Applicability:** focar a qualidade da estratégia de amostragem; não há testes de produto.
- **Product/test delta alignment:** produto e testes não mudaram; alinhado.
- **Workaround/assertion position:** nenhum skip, fallback silencioso, exclusão ampla ou false-green material; integridade e amostragem são eficazes/proporcionais.
- **Fail-first/TDD, real backend, DI, platform e CI parity:** `not_applicable` ao estudo documental sem comportamento executável.
- **Material findings:** `none`; optional improvements: `none required`.

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Final review status:** `not_run`
- **Evidence / reference:** `FINAL-BASELINE-ALWAYS` e `FINAL-EXPANDED-RISK-SIGNALS`; revisão expanded programada para antes de `Completed`.
- **Required focus:** rastreabilidade, linguagem não prescritiva, cobertura, privacidade e ausência de implementação.

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `not_needed`
- **Cutover audit status:** `no_material_findings`
- **Evidence / reference:** não há cutover, rollout, migração de dados ou mudança executável no escopo.
- **Applicability:** `not_needed`; não há cutover.

## Delivery Confidence Gate

- **Status:** `pending`
- **Required outcome:** critérios/evidências passam sem recomendação apresentada como decisão aprovada.

## Module Consolidation Gate

- **Status:** `not applicable for product decisions`; somente feature brief/backlog recebem atualização factual de conclusão.

## Commands (Run Locally)

- `git rev-parse '<sha>^{tree}'` e `git cat-file -e '<sha>^{commit}'` nos snapshots congelados.
- Oficial: `git.exe -C 'C:/Unifast/LeadsHug/Inspirações LeadsHug/Central-Whatsapp/api-oficial' log --no-merges --format='%H' 6517f197c97d0b5bcad886d26eb0d28a813b47ca..337f3e4839cef8ca400de87b3de088a79d512944 -- src public migrations docs clientes package.json schema.sql wrangler.jsonc README.md CONTEXTO-CONTINUIDADE.txt`.
- Hub: `git.exe -C 'C:/Unifast/LeadsHug/Inspirações LeadsHug/Central-Whatsapp/hub-whatsapp' log --no-merges --format='%H' 94ce80aa96d2c2ee004abc4d7ddf2c99a331def2..51bc16e544c7625a71c3012d8adef656c6392c37 -- backend frontend docs docker-compose.yml README.md Caddyfile .env.backend.example .env.evolution.example .env.example`.
- Overlay: `git -C '/mnt/c/Unifast/LeadsHug/Backup LeadsHug/LeadsHug' log --no-merges --format='%H' beb655cd3109fc3a537fca38c2b49f8c64853e7b..994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2 -- hub-whatsapp/backend hub-whatsapp/frontend hub-whatsapp/docs hub-whatsapp/docker-compose.yml hub-whatsapp/README.md hub-whatsapp/Caddyfile hub-whatsapp/.env.backend.example hub-whatsapp/.env.evolution.example hub-whatsapp/.env.example`.
- Cada busca dirigida registra padrão literal, SHA e uma das allowlists acima na linha do ledger; não existe busca global ou fallback para o working tree.
- Nos dois Central em `/mnt/c`, usar `git.exe` para status/objetos a fim de evitar falso diff LF/CRLF; a evidência continua ancorada em SHA/tree.
- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`.
- `git -C foundation_documentation diff --check`.

### Exact Sensitive-Content Check

Antes da entrega, executar um scan fail-closed somente sobre os arquivos Foundation esperados que realmente existirem no diff. O regex é apoio heurístico; resultado limpo não substitui revisão explícita de PII/payload.

```bash
set -euo pipefail
mapfile -t relative_paths < <({
  git -C foundation_documentation diff --name-only 6344bf64d8bb7330d8c992aaff93833fc65ca6ed -- \
    todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md \
    todos/completed/features/TODO-leadshug-central-whatsapp-capability-study.md \
    artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md \
    artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md backlog/README.md
  git -C foundation_documentation ls-files --others --exclude-standard -- \
    todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md \
    todos/completed/features/TODO-leadshug-central-whatsapp-capability-study.md \
    artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md \
    artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md backlog/README.md
} | sort -u)
test "${#relative_paths[@]}" -gt 0
scan_paths=()
for relative_path in "${relative_paths[@]}"; do
  test -f "foundation_documentation/$relative_path" && scan_paths+=("foundation_documentation/$relative_path")
done
test "${#scan_paths[@]}" -gt 0
secret_pattern="(?i)(?:api[_-]?key|client[_-]?secret|password)\s*[:=]\s*(?:\"[^\"]+\"|'[^']+'|[^\s#]+)|authorization\s*:\s*bearer\s+[^\s#]+|BEGIN [A-Z ]*PRIVATE KEY"
set +e
rg -q --pcre2 "$secret_pattern" "${scan_paths[@]}"
rc=$?
set -e
if [ "$rc" -eq 1 ]; then
  echo 'OK: no secret-like values in ST-02 delivery paths'
elif [ "$rc" -eq 0 ]; then
  echo 'BLOCKED: secret-like value detected; output redacted'
  exit 1
else
  echo 'BLOCKED: sensitive-content scanner failed without exposing matches'
  exit "$rc"
fi
```

## Files Expected

- `foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`
- `foundation_documentation/artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md` após aprovação.
- Feature brief/backlog e movimento para `completed/features/` apenas no closeout.

## COMENTÁRIO:

- Contrato deliberadamente reduzido a uma entrega documental e seis decisões materiais reunidas em uma única rodada.
