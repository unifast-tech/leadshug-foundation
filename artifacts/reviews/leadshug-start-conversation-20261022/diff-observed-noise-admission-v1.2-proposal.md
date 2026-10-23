# Exact observed-noise admission v1.2 — proposal only

Functional ST-CON-04 v1.1 remains unchanged. The actual corrected fullguard is no-go: 764 changes, 759 expected, five observations requiring admission. Both real channel tests and the final product review remain valid; no new product defect was found.

| Entry code | Proposed admission | Required condition |
| --- | --- | --- |
| DECLARED_API_SUBMODULE | Exact M observation only | Root index link unchanged; approved API HEAD and259source seal unchanged |
| DECLARED_WEB_SUBMODULE | Exact M observation only | Root index link unchanged; approved Web HEAD and259source seal unchanged |
| DECLARED_FOUNDATION_SUBMODULE | Exact M observation only | Already-authorized main documentation commits; root index link unchanged |
| CARRIED_PUBLIC_HISTORICAL_DIFF | Exact M, retain untouched | Contract baseline/HEAD/worktree normalized bytes equal |
| STRAY_PUBLIC_BROWSER_OUTPUT_JSON | Exact ??, retain untouched |109byte hash frozen; origin unknown beyond browser-output location; not delivery proof or product input |

The exact patch is [restricted local patch](/tmp/stcon04-diff-admission-v1.2.patch); its SHA and parser-only checks are in evidence/diff-observed-noise-admission-v1.2-proposal.json. The mandatory companion conditions preserve the no-gitlink-mutation invariant; non-M types remain rejected. No source/runtime/private pattern/baseline/tool change, deletion/restore/cleanup or product Git action is proposed.

The execution proposal is evidence/diff-observed-noise-admission-v1.2-runtime-plan.json: only after explicit human validation, apply the exact documentation patch, check companions, run the full unchanged canonical guard once with restricted output, recheck companions and finish only on actual GO. No additional full invocation is currently authorized. Independent bounded governance review8583 completed0/merge0. Its three constraints were incorporated: ALL companions before/after, exclusive verified0600 capture before execution, and complete cached allowed-status unions/negative controls. Ready plan: evidence/diff-observed-noise-admission-v1.2-ready-plan.json (SHA bd4897b3cbc33b8e442f5891f6fe8e29173d0aa1aa74b75d273696172ce848ee). The exact patch is unchanged; it remains unapplied and the new fullguard remains unauthorized.
