# ST-CON-04 — concrete module consolidation proposal

This proposal is a reviewable patch, not canonical module authority or delivery proof. It replaces the r6 narrative proposal as the concrete candidate for later review/application; all historical artifacts stay immutable.

```json
{
  "kind": "Concrete two-module documentation patch proposal; not applied",
  "recorded_at_utc": "2026-10-23T05:27:03.083992+00:00",
  "patch": "module-consolidation-r7-v1.1.patch",
  "patch_sha256": "70b6d9fc91f037556b936be2b143601aa10339d3313d67b2fe692acada5ace9f",
  "paths": [
    {
      "path": "foundation_documentation/modules/inbox-and-conversations.md",
      "baseline_sha256": "24b3f1edd8f10bf991d61135be2364b49679c43e5894ce024c2d5169921756a2",
      "proposed_lf_text_sha256": "a6711b55b173f2f8b3f6bf83ed4fbb55e6a7e2ffa0132dfd80f594d838d75d44"
    },
    {
      "path": "foundation_documentation/modules/integrations-and-channels.md",
      "baseline_sha256": "6b1865ab4f27458e1e1e225535e2f4a713e987e18344ca86d3f9411fa6c6f168",
      "proposed_lf_text_sha256": "3dfd99329d974e5a1aac22f04745017764d4c94b2566e0c63383151b1ef7459f"
    }
  ],
  "application_conditions": [
    "Actual corrected fullGREEN, independent findings resolved and decision/module consistency review.",
    "Apply only at the authorized delivery/consolidation stage; retain truthful runtime/operator/fullguard/final gates until actually satisfied.",
    "Preserve historical ST05/ST06 text and clearly identify the two approved supersedes. No constitution/roadmap/product/private changes.",
    "Closeout must update the active TODO link only when the TODO is actually moved; no broken future-completion links now."
  ],
  "current_state": "Drafted during E73 ALL; this proposal establishes no test result or application. Selected later actual receipts govern readiness."
}
```

The patch supplies the complete nine-route BFF contract, states and field definitions; manual open/no-send semantics; durable intent, admission and local recovery; exact Channel union and protocol ownership; trusted managed-resource IN provenance and `requiresWindow`; clock/lock/CAS bounds; same-account catalog subset and explicit historical supersession mapping. No canonical module has been changed.
