# PACED Subagent Dispatch: architecture_adherence

## Dispatch Identity
- **Artifact kind:** `subagent_review_dispatch`
- **Authoritative:** `false`
- **Edit policy:** `derived_dispatch_packet`
- **Review kind:** `architecture_adherence`
- **Bounded package:** `foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/api-checkpoint-packet-v1.md`
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
`/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/api-checkpoint-dispatch-v1.json`
Do not substitute the bounded package path, governing TODO path, or reviewer output path.

## Goal
Bounded API implementation security and adherence before consumer integration; no final TODO delivery claim

## Related TODO
`foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md`

Reviewers must cross-check findings against the governing TODO's explicit decisions, approved exceptions, compatibility mandates, and non-goals before classifying something as blocking drift.

## Historical Finding Carry-Forward
Previously adjudicated findings are historical context, not automatic reopening triggers.
- Resolved findings are historical context only. Do not reopen them unless the current bounded package materially changes the same locus/behavior or fresh evidence shows regression.
- Challenged findings stay closed unless the current bounded package materially changes the same locus/behavior or the prior rationale is objectively insufficient.
- Deferred findings must cite the recorded follow-up/waiver path first. Re-raise them only when the current bounded package changes the same locus or closure now depends on that deferred risk.
- Unresolved findings remain valid to re-raise until they are fixed, challenged, or formally deferred with authority.

### Recorded Dispositions
- `promotion_routing / NUM-ARCH-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Typebot tocado exige isolamento tenant já canônico
  - Reference: D-08; contratos de entrada; REG-SEC-01; VAL-08
- `promotion_routing / NUM-ARCH-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Recebimento do cadastro não pode duplicar efeitos
  - Reference: D-08; unique/transação; REG-SEC-02; VAL-08
- `promotion_routing / NUM-ARCH-03` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Pareamento exige comprovar número antes do conteúdo
  - Reference: D-06; rejeição pré-identidade; REG-SEC-03; VAL-08
- `promotion_routing / NUM-ARCH-04` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Evento atrasado não pode trocar owner BU
  - Reference: D-07; tombstone sem transferência; REG-SEC-04; VAL-08
- `promotion_routing / NUM-ARCH-05` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Pairing mutante exige POST/anti-CSRF
  - Reference: D-06; contrato BFF; REG-SEC-05; VAL-08
- `promotion_routing / NUM-ARCH-06` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Reautorizar canal existente sem substituir ativa prematuramente
  - Reference: D-03/04; candidata+CAS; REG-SEC-06/07; VAL-08
- `promotion_routing / NUM-CRIT-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Repareamento já prometido precisa invalidar prova anterior
  - Reference: D-06; instância por epoch e trust reset; REG-SEC-10
- `promotion_routing / NUM-CRIT-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=fix-current-contract; status=fixed-in-plan
  - Summary: Dois writers da mesma Message precisam compartilhar aceitação
  - Reference: D-08; message-acceptance e diff; REG-SEC-11
- `promotion_routing / NUM-OBS-01` -> `resolved`
  - Disposition: classification=by-design/no-action; routing=enforce-existing-requirement; status=covered-in-plan
  - Summary: Requisito secret-free já vinculante, sem defeito de gateway implementado alegado; harness concretizado
  - Reference: REG-SEC-12; runtime/logs; DOD-03
- `promotion_routing / NUM-OBS-02` -> `resolved`
  - Disposition: classification=by-design/no-action; routing=enforce-existing-requirement; status=covered-in-plan
  - Summary: Raw scoped já vinculante; batch por owner agora explícito, sem plataforma nova
  - Reference: REG-SEC-13; contrato raw; audit owner
- `promotion_routing / NUM-OBS-03` -> `resolved`
  - Disposition: classification=by-design/no-action; routing=enforce-existing-requirement; status=covered-in-plan
  - Summary: Harness de tenant/credencial já requerido; observar identificador não secreto e DB real
  - Reference: REG-SEC-01/11; VAL-02/08
- `promotion_routing / NUM-DELTA-OBS-01` -> `resolved`
  - Disposition: classification=by-design/no-action; routing=enforce-existing-requirement; status=covered-in-plan
  - Summary: Fence até commit já exigido; barrier do webhook em voo concretiza BCI
  - Reference: Delta v3; REG-SEC-10, nota de execução
- `promotion_routing / NUM-DELTA-OBS-02` -> `resolved`
  - Disposition: classification=by-design/no-action; routing=enforce-existing-requirement; status=covered-in-plan
  - Summary: Segredo em logs já proibido, inclusive hub.verify_token
  - Reference: Delta v3; REG-SEC-12, nota de execução
- `promotion_routing / NUM-DELTA-OBS-03` -> `resolved`
  - Disposition: classification=by-design/no-action; routing=enforce-existing-requirement; status=covered-in-plan
  - Summary: Refresh já prometido projeta autoria/conteúdo do mesmo ID
  - Reference: Delta v3; REG-SEC-11, nota browser; Inbox excluído preservado
- `critique / NUM-CRIT-01` -> `resolved`
  - Disposition: resolution=Integrated; usefulness=useful; formalizable=partial
  - Summary: Contrato de epoch/instância, D-06, REG-SEC-10; delta v3 confirma resolução contratual, produto ainda não verificado.
  - Reference: critique:findings_integrated
- `critique / NUM-CRIT-02` -> `resolved`
  - Disposition: resolution=Integrated; usefulness=useful; formalizable=partial
  - Summary: Aceitação keyed de todos os writers OUT, D-08, diff helper, REG-SEC-11.
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

