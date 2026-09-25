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

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** publicar a baseline revisada após `REVALIDO D-01..D-06 APÓS IC-01..IC-06` e repetir os gates pré-aprovação afetados.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** decisões revisadas foram revalidadas; freeze e gates renovados ainda estão em andamento.
- **Exit condition:** decisões revisadas revalidadas, novo freeze publicado, gates pré-aprovação concluídos e `APROVADO` explícito registrado.

## Scope

- [ ] `S-01` Publicar no catálogo um manifesto reproduzível com identidade, base, head, tree, pathspec permitido, papel e comandos exatos de verificação para cada snapshot.
- [ ] `S-02` Inventariar capacidades relevantes do Central oficial surgidas ou alteradas após a baseline de importação.
- [ ] `S-03` Inventariar capacidades relevantes do hub não oficial surgidas ou alteradas após a baseline de importação.
- [ ] `S-04` Examinar separadamente o overlay local do hub incorporado ao antigo LeadsHug, sem atribuí-lo ao Central independente.
- [ ] `S-05` Comparar cada capacidade candidata com o LeadsHug API/Web atual e seus contratos canônicos.
- [ ] `S-06` Classificar cada item por `origins[]`, época, transversalidade derivada, presença observada no LeadsHug, força da evidência, valor, risco, dependências e disposição recomendada.
- [ ] `S-07` Registrar lições negativas e exclusões explícitas para evitar que antipadrões legados sejam tratados como oportunidades.
- [ ] `S-08` Manter um ledger completo da população analisada, validar por amostragem bidirecional determinística/estratificada e publicar um único artefato de análise.

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

## Diff Expectation Contract (Required Before Delivery)

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| Foundation | `foundation_documentation` | `main@6344bf64d8bb7330d8c992aaff93833fc65ca6ed` | `working_tree` |
| LeadsHug API | `api-app` | `5db3fbe2043428749895fc3ff6441e9457467dd0` | `read_only_snapshot` |
| LeadsHug Web | `web-app` | `6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9` | `read_only_snapshot` |
| Central oficial | `.../Central-Whatsapp/api-oficial` | `337f3e4839cef8ca400de87b3de088a79d512944` | `read_only_snapshot` |
| Central hub | `.../Central-Whatsapp/hub-whatsapp` | `51bc16e544c7625a71c3012d8adef656c6392c37` | `read_only_snapshot` |
| LeadsHug legado | `.../Backup LeadsHug/LeadsHug` | `994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2` | `read_only_historical_snapshot` |

### Snapshot Manifest Contract

O catálogo deve reproduzir esta matriz com paths absolutos redigidos para identidade lógica, sem depender do branch ou working tree corrente.

| Identity | Base SHA | Head SHA | Head tree | Allowed pathspec / role |
| --- | --- | --- | --- | --- |
| `leadshug-api` | `n/a` | `5db3fbe2043428749895fc3ff6441e9457467dd0` | `4386ac3c732702c9d869f8a9482ccd99750e6ef8` | snapshot completo; alvo de comparação |
| `leadshug-web` | `n/a` | `6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9` | `8b83239b57e31ec34bfbf911d35af035866e3ff0` | snapshot completo; alvo de comparação |
| `central-official` | `6517f197c97d0b5bcad886d26eb0d28a813b47ca` | `337f3e4839cef8ca400de87b3de088a79d512944` | `1ee054a4630b0448b4432429e8b68b30f6e87ed5` | snapshot Git por SHA; origem oficial |
| `central-hub` | `94ce80aa96d2c2ee004abc4d7ddf2c99a331def2` | `51bc16e544c7625a71c3012d8adef656c6392c37` | `e8823e402d1110d3fec0f6d2923490536f97254a` | snapshot Git por SHA com `secrets/**` excluído; origem hub |
| `legacy-hub-overlay` | `beb655cd3109fc3a537fca38c2b49f8c64853e7b` | `994e1e8ccb2ae00899c13e3e7bb103dfa7bf46c2` | `ff142200b038ae642f24c467b8f084cbc78e6229` | somente `hub-whatsapp/**`, exceto `secrets/**`; origem overlay legado |

Evidência de fonte usa somente `repo@sha:path:symbol-or-commit`; código/payload não é copiado. Inspeção usa objetos Git congelados (`git show`, `git grep <sha>`, `git diff <base>..<head> -- <allowlisted-pathspec>`), nunca confiança implícita no working tree.

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
| Central oficial | `.../Central-Whatsapp/api-oficial/**` | `any` | referência somente leitura |
| Central hub | `.../Central-Whatsapp/hub-whatsapp/**` | `any` | referência somente leitura |
| LeadsHug legado | `.../Backup LeadsHug/LeadsHug/**` | `any` | referência histórica somente leitura |
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

Cada capacidade usa uma linha normalizada com: `capability_id`, `title`, `origins[]`, `epoch`, `cross_origin`, `central_evidence[]`, `leadshug_evidence[]`, `implementation_state`, `evidence_strength`, `user_value`, `risks[]`, `dependencies[]`, `disposition_recommendation`, `canonical_rejection_ref` e `notes`. Evidência aponta para `repo@sha:path:symbol-or-commit`, sem copiar código ou payload.

Cada linha também contém a matriz de aplicabilidade exigida pela policy: `tenancy`, `BU`, `conversation`, `provider_adapter`, `audit` e `channel_policy`, cada uma como `applies|not_applicable|unknown` com evidência ou justificativa. `cross_origin` é derivado de `origins[]`; não é origem autônoma.

## Definition of Done

- [ ] `DOD-01` O manifesto registra bases, heads, trees, pathspecs, papéis e comandos verificáveis para todos os snapshots.
- [ ] `DOD-02` Cada capacidade tem evidência do Central e evidência/estado correspondente no LeadsHug, ou incerteza explícita.
- [ ] `DOD-03` Cada capacidade informa `origins[]`, `epoch`, `cross_origin`, `implementation_state`, `evidence_strength`, valor, riscos, dependências e disposição recomendada sem misturar presença e desejabilidade.
- [ ] `DOD-04` Itens posteriores à baseline estão separados dos itens que já existiam na baseline mas não foram reimplementados.
- [ ] `DOD-05` Lições negativas e exclusões estão explícitas; uma rejeição como não desejada exige `canonical_rejection_ref`, caso contrário permanece recomendação.
- [ ] `DOD-06` O ledger mapeia toda a população admitida para capacidade, duplicata ou exclusão justificada; a auditoria estratificada não encontra item relevante sem mapeamento.
- [ ] `DOD-10` Cada capacidade avalia `tenancy`, `BU`, `conversation`, `provider_adapter`, `audit` e `channel_policy` como `applies|not_applicable|unknown`, com evidência/justificativa.
- [ ] `DOD-07` O catálogo não contém segredos, dados pessoais, payloads sensíveis nem trechos de código copiados.
- [ ] `DOD-08` Nenhuma recomendação é apresentada como prioridade aprovada ou autorização de implementação.
- [ ] `DOD-09` Gates documentais e revisão final passam; feature brief/backlog refletem apenas o estado factual concluído.

## Validation Steps

- [ ] `VAL-01` Revalidar bases, heads e trees do manifesto com comandos Git por SHA e confirmar alcance dos commits de importação.
- [ ] `VAL-02` Comparar os intervalos completos `6517f197..337f3e4` (129 não-merge) e `94ce80aa..51bc16e` (66 não-merge) somente nos pathspecs permitidos.
- [ ] `VAL-03` Comparar o único commit do overlay que toca `hub-whatsapp/**` entre `beb655cd..994e1e8`, excluindo `secrets/**`.
- [ ] `VAL-04` Verificar o ledger completo e auditar deterministicamente 100% de `not_found_after_protocol`, `uncertain`, rejeições canônicas, itens cross-origin e alegações sensíveis; amostrar de forma estratificada os estados positivos restantes.
- [ ] `VAL-05` Usar comandos allowlisted sem patch/body ou metadados pessoais por padrão; não persistir outputs brutos; executar scanner de segredo no diff final e revisão explícita de PII sem alegar garantia absoluta.
- [ ] `VAL-06` Executar validador estrutural, `git diff --check` e guards de diff, autoridade, conclusão e closeout aplicáveis.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01..S-08` | Scope | Entrega integral do estudo | doc+review | catálogo + rastreabilidade | n/a | planned | detalhar por critério antes do closeout |
| `DOD-01..DOD-10` | Definition of Done | Critérios do catálogo | doc+review+guard | catálogo, ledger, auditoria, guards e revisões | n/a | planned | detalhar por critério antes do closeout |
| `VAL-01..VAL-06` | Validation Steps | Validações reproduzíveis | command+manual review | comandos e relatório | local/read-only | planned | registrar resultados exatos |

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
| Strategic / CTO-Tech-Lead | Assurance / Tester-Quality | desafiar cobertura, rastreabilidade e conclusões | TODO e catálogo | planned |

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

- Nenhuma decisão material pendente após `REVALIDO D-01..D-06 APÓS IC-01..IC-06` em 2026-09-25.

## Decisions (Resolved Before Freeze)

- [x] `D-01` Usar o manifesto por repositório com base/head/tree/pathspec e comparar o intervalo oficial completo até `337f3e4839cef8ca400de87b3de088a79d512944`; categorizar gaps preexistentes e evolução posterior.
- [x] `D-02` Preservar `official`, `hub` e `legacy_overlay` em `origins[]`; `cross_origin` é derivado e nunca substitui a proveniência.
- [x] `D-03` Comparar capacidades/comportamentos, não arquivos, com evidência `repo@sha:path:symbol-or-commit` e avaliação dos seis limites da policy por capacidade.
- [x] `D-04` Separar `implementation_state` (`observed_present|partial|not_found_after_protocol|uncertain`) de `evidence_strength` e `disposition_recommendation`; rejeição do produto exige `canonical_rejection_ref`. Presença observada não afirma saúde produtiva.
- [x] `D-05` Manter um ledger completo da população e um catálogo único até 40 capacidades; acima disso, pausar para propor divisão. Auditar 100% dos estados/alegações de maior risco e amostrar deterministicamente os positivos.
- [x] `D-06` Tratar disposições (`descartar`, `estudar`, `candidata ao ST-04`) apenas como recomendação fundamentada; prioridade e canonização pertencem ao `ST-04` ou a TODO futuro aprovado.
- **Human revalidation:** usuário, `REVALIDO D-01..D-06 APÓS IC-01..IC-06`, conversa de 2026-09-25.

### Decision Validation Review (Prepared Pre-Freeze)

| Decision | Technical validation | Evidence | Outcome |
| --- | --- | --- | --- |
| `D-01` | Os commits-base são exatos; manifesto e intervalo oficial foram corrigidos até o head atual congelado. | Trees importados `76e80538...` e `f926eca3...`; head oficial `337f3e4`, tree `1ee054a4...`. | critique-integrated; pending-human-revalidation |
| `D-02` | O overlay incorporado é uma origem histórica distinta e transversalidade não apaga origem. | Entre `beb655cd` e `994e1e8`, apenas `994e1e8` toca `hub-whatsapp/`; `cross_origin` passa a ser derivado. | critique-integrated; pending-human-revalidation |
| `D-03` | Comparação por capacidade continua correta, agora com schema/proveniência e policy applicability explícitos. | 129 commits não-merge no oficial e 66 no hub; policy exige seis limites por inspiração. | critique-integrated; pending-human-revalidation |
| `D-04` | Presença técnica, força da evidência e desejabilidade foram separadas. | Crítica `IC-03`; evidência estática não comprova saúde operacional e rejeição exige autoridade canônica. | critique-integrated; pending-human-revalidation |
| `D-05` | Ledger completo + auditoria estratificada substituem amostragem aberta. | Crítica `IC-02`; limite 40 permanece stop condition, nunca truncamento. | critique-integrated; pending-human-revalidation |
| `D-06` | Recomendações continuam sem autoridade de roadmap. | O backlog é dono da disposição e `ST-04` da síntese/priorização. | critique-integrated; pending-human-revalidation |

**Material-decision sweep:** `IC-01..IC-06` foram absorvidos nos mesmos seis IDs; nenhum `D-07` é necessário. A versão revisada requer revalidação antes de novo freeze.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `modules/integrations-and-channels.md#Invariants` | provider como adapter; segredo fora de logs/docs/fixtures/client; falha determinística | Preserve | três invariantes explícitos do módulo |
| `modules/inbox-and-conversations.md#Invariants` | conversa única BU/contato; webhook idempotente; janela/capacidade do canal | Preserve | três invariantes explícitos do módulo |
| `modules/audit-and-history.md#Invariants` | histórico append-oriented; tenant/BU scope; leitura independente de escrita | Preserve | três invariantes explícitos do módulo |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-06` revisadas e revalidadas exatamente como registradas em `Decisions`.
- **Historical invalidated baseline:** `cff19546`; preservado como proveniência da primeira crítica.
- **Current freeze scope:** decisões, manifesto/schema, Scope/Out of Scope, Definition of Done, Validation Steps, Test Strategy e Diff Expectation Contract.
- **Renewal trigger:** qualquer mudança material nesses campos requer nova validação e novo `APROVADO`.

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `not_needed`
- **Why this applies:** o estudo registra evidência e recomendações; não muda arquitetura nem contratos.
- **Deviation / debt being retired:** `n/a`
- **Target steady-state after closeout:** Central permanece referência independente; LeadsHug permanece dono de suas decisões.
- **Temporary exceptions allowed:** `none`
- **Cutover / removal condition:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`.
- **Status:** `passed`; contrato revisado revalidado, commitado e publicado antes dos novos reviews/guards formais.
- **Gate status:** `no_material_findings`.
- **Freeze target:** decisões, manifesto/schema, escopo, DoD, validação, estratégia de auditoria e diff contract.
- **Baseline branch:** `foundation_documentation:main`.
- **Baseline commit:** `1dac5eaf`.
- **Baseline push reference:** `origin/main`.
- **Evidence / reference:** `git_write_authority_guard.py` retornou `go`; `git.exe push origin main` publicou `d2837312..1dac5eaf` em 2026-09-25.
- **Historical invalidation evidence:** baseline `cff19546`, crítica `IC-01..IC-06`, verdict `findings`.
- **Waiver authority / reference (required if waived):** `n/a`.

## Gate: Review Scope Drift

- **Status:** `pending execution`
- **Rule:** implementação, promoção canônica ou entrega independente exige novo contrato/aprovação.

## Questions To Close

- [x] Revalidar conjuntamente `D-01..D-06` revisadas após `IC-01..IC-06`.
- [ ] Após os gates de planejamento, registrar `APROVADO` para executar o catálogo.

## Assumptions Preview (Required Before Plan Review)

- Hashes congelados são a unidade de reprodutibilidade; branches podem avançar sem mudar o escopo.
- Histórico, docs e código demonstram presença de capacidade, não automaticamente sua qualidade ou adequação.
- Ausência só será afirmada após busca no API, Web e documentação atual; caso contrário, será `Incerto`.
- `secrets/**`, valores de ambiente, dados reais e payloads sensíveis são excluídos mesmo quando aparecem no histórico.
- A terminologia Mantenedora → Setor → BU e conversa independente de transporte prevalece sobre nomes legados.

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
- População do ledger: todos os 195 commits não-merge pós-baseline admitidos (129 oficial, 66 hub), o único commit do overlay que toca `hub-whatsapp/**` e as superfícies funcionais atuais identificadas nos snapshots allowlisted.
- Cada unidade da população recebe exatamente um destino: `capability_id`, `duplicate_of`, `supporting_evidence_for` ou `excluded` com justificativa.
- Auditoria de 100% dos itens `not_found_after_protocol`, `uncertain`, com rejeição canônica, cross-origin ou alegação sensível.
- Nos estados positivos restantes, seleção determinística por estratos `origin × epoch × implementation_state`: ordenar por `capability_id` e revisar todos quando o estrato tiver até cinco itens; acima disso, mínimo de cinco mais os IDs cujo SHA-256 textual tenha primeiro byte divisível por quatro.
- Amostra fonte → catálogo e catálogo → fontes deve falhar se encontrar unidade relevante sem destino ou evidência que não resolve no snapshot.
- O limite de 40 capacidades aciona proposta de divisão; nunca interrompe ou trunca o ledger.

### Flow Evidence Planning Matrix

| Flow / Criterion | User-visible or runtime impact now? | Planned Evidence | Runtime Lane | Waiver Rationale |
| --- | --- | --- | --- | --- |
| Catálogo ST-02 | no | rastreabilidade entre snapshots, catálogo e estado LeadsHug | n/a | análise sem mudança de runtime/UI |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundation lifecycle | TODO, análise, backlog e feature brief | `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation` | approval/delivery | planned | exact command | testes de produto não se aplicam |
| Markdown/git hygiene | documentação | `git -C foundation_documentation diff --check` | delivery | planned | exact command | inclui caminhos esperados |

### Runtime / Rollout Notes

- `n/a`: nenhuma mudança executável ou rollout.

## Plan Review Gate

- **Status:** `critique findings integrated; reconvergence pending human revalidation and new freeze`.
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
- **Latest TEACH evidence / artifact:** `foundation_documentation/artifacts/tmp/leadshug-central-whatsapp-capability-study-audit-escalation.json`; fingerprint `ef66891d75b2`; `Overall outcome: go`.

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

- **Critique decision:** `required`.
- **Why this decision:** baseline obrigatória e depth expandido por complexidade média com blast radius cross-module (`CRITIQUE-BASELINE-ALWAYS`, `CRITIQUE-EXPANDED-RISK-SIGNALS`).
- **Impact signals in scope:** `cross-module blast radius`.
- **Package mode:** `bounded-file-set`.
- **Package minimum contents:** TODO congelado, feature brief, policy de legado e três módulos âncora.
- **Critique isolation mode:** `fresh internal no-context reviewer`.
- **Internal reviewer mandate:** `required; fresh stateless no-context internal reviewer, not the implementing agent`.
- **Canonical multi-lane audit protocol:** `n/a`.
- **Audit session / round evidence:** `n/a`.
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`.
- **Critique status:** `not_run`; primeira crítica integrada, nova crítica aguardando baseline revisada.
- **Findings summary:** `IC-01..IC-04 high`, `IC-05..IC-06 medium`; todos integrados no contrato revisado.
- **Evidence / reference:** revisor interno stateless `/root/st02_independent_critique`, baseline `cff19546`, verdict `findings`, 2026-09-25.
- **Waiver authority / reference:** `n/a`.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `IC-01` | Integrated | useful | no | none | n/a | manifesto e intervalo corrigidos |
| `IC-02` | Integrated | useful | no | none | n/a | ledger e auditoria determinística |
| `IC-03` | Integrated | useful | no | none | n/a | schema normalizado |
| `IC-04` | Integrated | useful | no | none | n/a | policy e invariantes completos |
| `IC-05` | Integrated | useful | no | none | n/a | procedimento fail-closed de leitura/publicação |
| `IC-06` | Integrated | useful | no | none | n/a | estado/freeze reconciliados |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`.
- **Why this decision:** o estudo depende de snapshots de código para distinguir presença, parcialidade e ausência após protocolo.
- **Trigger stage:** `after critique convergence and before APROVADO`.
- **Guard scope:** `snapshot manifest, implementation-state protocol and cited source paths`.
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`.
- **Gate status:** `not_run`; aguarda novo freeze e nova crítica.
- **Findings summary:** `none yet on revised baseline`.
- **Evidence / reference:** `pending revised review baseline`.
- **Waiver authority / reference:** `n/a`.

## Approval

- **Decision validation:** `REVALIDO D-01..D-06 APÓS IC-01..IC-06`, usuário, 2026-09-25.
- **Execution approval:** `pending`
- **Required phrase after plan gates:** `APROVADO`

## Rules Acknowledgement / Ingestion

- Pendente até `APROVADO`. Na execução, preservar política de legado independente, modelo tenant/BU/conversa e limite estrito de escrita documental.

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** contract-refinement
- **Selected role:** strategic-cto
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Writer scheduling policy:** one writer in canonical checkout; reviewers read-only
- **Guard outcome:** pending decisions and approval gates

## Decision Adherence Validation (Mandatory Before Delivery)

- Pendente; verificar `D-01..D-06` linha a linha no catálogo e no diff final.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

- Pendente; preservar os três módulos âncora sem promover recomendações como decisões.

## Security Risk Assessment (Mandatory Before Delivery)

- **Audit decision:** `not_needed` pelo audit floor (`SEC-NOT-TRIGGERED`); risco documental continua controlado localmente.
- **Risk:** baixo se exclusão de segredos/PII e leitura somente forem mantidas.
- **Required evidence:** nenhuma leitura de `hub-whatsapp/secrets/**`; nenhum output bruto persistido; diff sem valor sensível, PII, payload ou trecho copiado; scanner de segredo como apoio, não garantia absoluta.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Audit decision:** `not_needed` pelo audit floor (`PCV-NOT-TRIGGERED`).
- **Risk:** `n/a` para runtime; análise local deve permanecer somente leitura e bounded.

## Verification Debt Assessment (Required Before `Completed`)

- **Audit decision:** `required` antes de `Completed` (`VDA-MEDIUM-BIG-OR-RELEASE`).
- Pendente. Lacunas de amostragem e classificações `Incerto` serão dívida explícita, nunca ocultada.

## Independent Test Quality Audit Gate

- **Audit decision:** `recommended`, focused, antes de `Completed` (`TQA-MEDIUM-OR-BIG-DEFAULT`).
- **Applicability:** focar a qualidade da estratégia de amostragem; não há testes de produto.

## Independent No-Context Final Review Gate

- **Audit decision:** `required`, expanded, antes de `Completed` (`FINAL-BASELINE-ALWAYS`, `FINAL-EXPANDED-RISK-SIGNALS`).
- **Status:** `pending delivery`
- **Required focus:** rastreabilidade, linguagem não prescritiva, cobertura, privacidade e ausência de implementação.

## Independent Cutover Integrity Audit Gate

- **Applicability:** `not_needed`; não há cutover.

## Delivery Confidence Gate

- **Status:** `pending`
- **Required outcome:** critérios/evidências passam sem recomendação apresentada como decisão aprovada.

## Module Consolidation Gate

- **Status:** `not applicable for product decisions`; somente feature brief/backlog recebem atualização factual de conclusão.

## Commands (Run Locally)

- `git rev-parse '<sha>^{tree}'` e `git cat-file -e '<sha>^{commit}'` nos snapshots congelados.
- `git log --no-merges --format='%H' <base>..<head> -- <allowlisted-pathspec>` sem body, autor ou e-mail.
- `git diff --name-only <base>..<head> -- <allowlisted-pathspec> ':(exclude)secrets/**'`; patches não são persistidos.
- `git grep -n <pattern> <sha> -- <allowlisted-pathspec> ':(exclude)secrets/**'` somente para hipóteses específicas; conclusões que exigiriam superfície sensível ficam `uncertain`.
- Nos dois Central em `/mnt/c`, usar `git.exe` para status/objetos a fim de evitar falso diff LF/CRLF; a evidência continua ancorada em SHA/tree.
- `python3 foundation_documentation/deterministic/validate_foundation_lifecycle.py --root foundation_documentation`.
- `git -C foundation_documentation diff --check`.

## Files Expected

- `foundation_documentation/todos/active/features/TODO-leadshug-central-whatsapp-capability-study.md`
- `foundation_documentation/artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md` após aprovação.
- Feature brief/backlog e movimento para `completed/features/` apenas no closeout.

## COMENTÁRIO:

- Contrato deliberadamente reduzido a uma entrega documental e seis decisões materiais reunidas em uma única rodada.
