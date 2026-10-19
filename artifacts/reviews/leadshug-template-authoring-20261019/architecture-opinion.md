# ST-CON-05 — independent architecture opinion

Reviewer /root/stcon05_architecture; fresh fork_turns none; gpt-6.1-sol/max; formal-review routing go before dispatch. Terminal read-only planning opinion against Foundation f42a2e72b3a42305f38c939c3e70eabad59d507d. No implementation, tests, runtime/account calls or private paths. Recommendation: retain direction, integrate five medium approval blockers; no high architecture defect established. Opinion does not authorize implementation.

| Finding | Evidence / original problem | Required disposition |
| --- | --- | --- |
| AR-01 | D04/07 generation alone misses active credential replacement; schema credential.version:237, canonical integrations:67. Cached approval indefinite. | Capture/fence account/channel/generation/managedIdentity/activeCredentialVersion; historical receipt cannot certify current context. Define finite freshness; show observedAt/stale, future firstsend independently validates. |
| AR-02 | D02 says same parser but separate API/Web repositories and missing preview route. | BFF POST preview, session/CSRF, zero DB/provider; normalized definition/plain text/fingerprint bound context/revision; React escape, debounce and monotonic fencing. No cross-repo import/duplicated authority. |
| AR-03 | D05 exhaustive unfiltered2x50 blocks larger provider accounts. | Server-derived name filter, exact name/language, complete bounded filtered pagination. Verify provider wire semantics; no unbounded scan/filter-as-authorization. |
| AR-04 | Request hash includes samples/context while remote exact definition undefined. | Immutable requestFingerprint versus exact supported remoteSemanticFingerprint; review samples/metadata excluded only from latter. No trim to force match; CORRELATED_BY_DEFINITION says compatible asset located, no authorship/POST-success claim. |
| AR-05 | D01/DOD01/CI mention LEITOR absent from schema:284/helpers:186. | Existing OWNER/ADMIN/ATENDENTE only; test no BU grant/foreign BU/tenant/other seller draft and authorized same-BU ADMIN. |

Known runner prerequisite: scripts/test-channels-local.sh:25 traverses API with find. Positive public inventory must be established before every test, including RED, not only the later suite step.

D01 seller submit/private drafts versus shared external assets is sound. D02 textual NAMED pt_BR is coherent subset. D03 backend ownership/revisions/CAS is sound. D04 explicit management purpose preserves send readiness. D05/06 durable reservation, single POST invocation per operation and GET-only reconciliation honestly model uncertainty. D07 one catalog owner is correct after freshness repair. D08 monotonic UI recovery is sound; firstsend remains ST-CON-04.

Performance favorable after targeted lookup; retain limits/no fan-out and measure SQL. Elegance favorable with domain preview and one owner, no generic operation platform. Structural soundness favorable after explicit credential fencing and request/observation/correlation separation. Operational fit appropriate for manual refresh/assisted creation; approval can remain pending/rejected.

Harness must prove distinct keys/actors on same revision at most one POST, PREPARED expiry/SENDING crash/late success, GET-only reconcile and divergent definitions, management without receipt while send remains blocked, same-generation credential replacement, stale preview/refresh, APPROVED→PAUSED and safe unknowns. Raw MetaHttpClient wire tests required: browser server overrides META_CLIENT and alone does not establish Graph query/body/error contract.

Primary evidence: [Meta fundamentals](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview/), [official Meta Postman name lookup](https://www.postman.com/meta/whatsapp-business-platform/request/7whkjje/get-template-by-name-default-fields), [Meta SDK parameters](https://github.com/facebook/facebook-python-business-sdk/blob/main/facebook_business/adobjects/whatsappbusinessaccount.py#L913). Owner resolution ledger in governing TODO integrates AR01..05/runner before fresh critique. No historical webhook cause inferred.
