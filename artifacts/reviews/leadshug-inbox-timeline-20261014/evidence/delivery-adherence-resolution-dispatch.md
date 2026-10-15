# PACED Subagent Dispatch: architecture_adherence

## Dispatch Identity
- **Artifact kind:** `subagent_review_dispatch`
- **Authoritative:** `false`
- **Edit policy:** `derived_dispatch_packet`
- **Review kind:** `architecture_adherence`
- **Bounded package:** `foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-adherence-resolution-self-contained-package.md`
- **Reviewer count:** `1`
- **No-context required:** `true`

## Required Axes
- `adherence`
- `structural_soundness`
- `operational_fit`
- `performance`
- `elegance`

## Focus Points
- Compare the delivered bounded package against the frozen Architecture Change Governance contract and Decision Baseline.
- Identify any implementation path, temporary exception, or missing protection harness that diverges from the approved target steady-state.
- Do not redesign the approved architecture unless the delivered evidence exposes a material defect or an approval-breaking divergence.
- For each material finding, add category and formalizable-hint when you can judge them honestly.
- When assessing design, seek the simplest faithful Clean Code/SOLID design for the approved intent. Do not invent future-facing work or erase explicit TODO intent. Planning review may challenge proposed intent; delivery review must preserve approved intent or return for renewed approval.

## Required Result Fields
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings[].finding_id (optional)`
- `findings[].category (optional)`
- `findings[].formalizable_hint (optional)`
- `findings[].candidate_rule_level (optional)`
- `findings[]`

## Required Result Binding
The reviewer result's `dispatch_path` must equal this exact dispatch JSON path:
`/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-adherence-resolution-dispatch.json`
Do not substitute the bounded package path, governing TODO path, or reviewer output path.

## Goal
Fresh delivery-adherence-resolution-native: adjudicate ARCH-DEL-04 error ownership fix and current revision4, preserve prior resolved architecture; complete applicable adherence workload and four axes. Separate prior TQA remains live and is not replaced.

## Related TODO
`foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md`

Reviewers must cross-check findings against the governing TODO's explicit decisions, approved exceptions, compatibility mandates, and non-goals before classifying something as blocking drift.

## Historical Finding Carry-Forward
Previously adjudicated findings are historical context, not automatic reopening triggers.
- Resolved findings are historical context only. Do not reopen them unless the current bounded package materially changes the same locus/behavior or fresh evidence shows regression.
- Challenged findings stay closed unless the current bounded package materially changes the same locus/behavior or the prior rationale is objectively insufficient.
- Deferred findings must cite the recorded follow-up/waiver path first. Re-raise them only when the current bounded package changes the same locus or closure now depends on that deferred risk.
- Unresolved findings remain valid to re-raise until they are fixed, challenged, or formally deferred with authority.

### Recorded Dispositions
- `promotion_routing / ARCH-TL-01..03` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in current TODO; status=fixed
  - Summary: Contrato de leitura/recuperação pertence à mesma story
  - Reference: architecture-review.json e Proposed API Contract, a verificar na crítica
- `promotion_routing / ARCH-TL-04..06` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in current TODO; status=fixed
  - Summary: Estado/consulta/provas necessários ao mesmo contrato
  - Reference: architecture-review.json e testes planejados, a verificar na crítica
- `promotion_routing / ARCH-DEL-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in current TODO; status=fixed
  - Summary: Budget3 por rodada deve abranger coalescing; evento não renova automaticamente consultas
  - Reference: delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada.
- `promotion_routing / ARCH-DEL-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in current TODO; status=fixed
  - Summary: Thread inicialmente vazia e notificação entre rodadas devem conservar restart pendente até fetch recente
  - Reference: delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada.
- `promotion_routing / ARCH-DEL-03` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix in current TODO; status=fixed
  - Summary: Notificação durante abertura pertence à geração selecionada e deve recuperar sem esperar outroevento/poll
  - Reference: delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada.
- `promotion_routing / TQA-TL-01` -> `unresolved`
  - Disposition: classification=release-blocker; routing=fix with ARCH-DEL-01; status=open
  - Summary: Mesmo defeito de budget/single-flight; harness deve contar requests e passagens em voo, não só comparar IDs
  - Reference: delivery-tqa-round-1.json; duplicata sem novo escopo
- `promotion_routing / TQA-TL-02` -> `unresolved`
  - Disposition: classification=release-blocker; routing=fix in current TODO; status=open
  - Summary: Prova de geração exige draft/erro/scroll/metadados do destino em trocas conversa/BU com sucesso/falha/backfill antigos
  - Reference: delivery-tqa-round-1.json; novos asserts reais dentro de VAL-05
- `promotion_routing / TQA-EVID-03` -> `unresolved`
  - Disposition: classification=release-blocker; routing=retain exact CI leaf outputs now; status=open
  - Summary: Lacuna de evidência do claim CI atual; repetir somente generate/lint/build/unit API com logs imutáveis antes do browser final
  - Reference: delivery-tqa-round-1.json; VAL-02, sem repetir API224 unchanged
- `promotion_routing / ARCH-DEL-01-ERR` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix with ARCH-DEL-01; status=fixed
  - Summary: Variante objetiva: saldo era debitado após await; falha+dirty não debitava e permitia mais de3tentativas. Consumir no despacho e provar3aborts+eventos sem4aautomática; erro histórico com dirty deve conservar restart recente, não consumir a notificação ao retomar cursor antigo
  - Reference: delivery-adherence-delta.json confirmou resolução na fonte revision3; Web34/FRC3, incluindo negativos/restauração e notificações/retomada.
- `promotion_routing / ARCH-DEL-04` -> `unresolved`
  - Disposition: classification=release-blocker; routing=fix in current TODO; status=open
  - Summary: Retry bem-sucedido deve encerrar alerta do próprio recovery sem apagar erro posterior não relacionado; assert ausência no fim dos casos existentes
  - Reference: delivery-adherence-delta.json; correção faithful HOW, sem nova aprovação de produto
- `critique / ARCH-TL-03` -> `resolved`
  - Disposition: resolution=Integrated; usefulness=useful; formalizable=yes
  - Summary: Piso pendente T conservado entre passagens/dirty/retry e promoção somente após cobertura sem evento pendente; crítica delta critique-resolution.json confirmou a resolução do plano, agora testada no browser.
  - Reference: critique:findings_integrated

## Result Contract
Return exactly one JSON object and no Markdown fence or prose.
Do not emit `null`; omit optional fields that do not apply.
No top-level fields other than the following are allowed:
- `schema_version`: `subagent-review-result-v1`
- `artifact_kind`: `subagent_review_result`
- `dispatch_path`: the exact binding shown above
- `review_kind`: `architecture_adherence`
- `reviewer_label`
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings`

Every `*_position` value must be one of: `strong_positive`, `acceptable`, `mixed`, `regresses`, `unknown`, `not_evaluated`.
Each finding may contain only these fields:
- required: `severity`, `title`, `rationale`, `suggested_action`
- optional: `finding_id`, `category`, `formalizable_hint`, `candidate_rule_level`, `candidate_rule_id`, `affected_paths`
- `severity` values: `low`, `medium`, `high`
- `category` values: `architecture`, `adherence`, `tests`, `performance`, `security`, `elegance`, `structural_soundness`, `operational_fit`, `residual_risk`, `other`
- `formalizable_hint` values: `yes`, `partial`, `no`, `unknown`
- `candidate_rule_level` values: `paced`, `project`, `none`, `unknown`

