# Vínculo local do Test Number da Configuração da API Meta

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`
- **Parent contract:** `ST-CON-01` in [TODO-leadshug-channel-connection-readiness.md](TODO-leadshug-channel-connection-readiness.md)
- **Child story:** `ST-CON-01-TESTAUTH`
- **Proposal:** [leadshug-meta-api-test-number-binding-proposal-20261018.md](../../../artifacts/analysis/leadshug-meta-api-test-number-binding-proposal-20261018.md)
- **Status of this document:** approved staged execution; qualification rejected/inconclusive, product edits stopped.

## Context

The operator confirmed that the WhatsApp message sent by Meta's API Setup Test Number arrived in the WhatsApp application. That Test Number is distinct from the Sandbox number already linked to BU `Teste Meta`; the Sandbox number was not available in WhatsApp and its physical WhatsApp test was not performed. No conclusion about the Sandbox delivery path follows from the SMS attempt.

The ordinary supported official-number workflow is Embedded Signup OAuth. It creates a registration attempt, exchanges a nonce-bound OAuth code, lists resources under that candidate grant, confirms a selected WABA and phone, applies ownership and BU-phone checks, then stores an encrypted credential per channel. Its `JA_REGISTRADO` mode skips the provider `/register` mutation; it does not skip OAuth or accept an arbitrary credential. The current implementation has no supported way to bind the already-provisioned API Setup Test Number using a privately configured local credential.

This child proposes a default-off local technical authorization method for that already-provisioned resource. It must converge on the existing registration, ownership, encrypted credential, webhook identity, and receipt paths. It does not replace or alter the approved Embedded Signup contract. The parent remains Pending and VAL05 remains open; this child cannot close or waive either parent obligation.

## Framing Source & Story Slice
- **Feature brief:** `direct-to-TODO`
- **Primary story ID:** `ST-CON-01-TESTAUTH`
- **Why this is the right current slice:** provide one auditable way to bind a locally configured Meta API Setup Test Number to its own BU without registering it again, while preserving the approved per-BU credential and identity model.
- **Direct-to-TODO rationale:** this is a bounded authorization-method complement to the already approved ST-CON-01 implementation. It needs its own approval and validation contract, but no separate product brief is needed before the technical feasibility and grant qualification are decided.

## Contract Boundary

The user explicitly replied APROVADO on 2026-10-18 to the published staged plan at Foundation 7f478ee38d31827786c6eafc0b1168f9fc5d2d83. This authorizes the exact bounded qualification-first implementation contract. The earlier direction-only approval is superseded; separate root qualification and code-execution GOs remain mandatory. A grant that fails existing authorization requirements blocks this plan; it does not authorize weakening the Embedded Signup validators.

## Implementation Intent
- **Current delivery:** one default-off local authorization method binding a pre-provisioned Meta API Setup Test Number through the existing channel workflow; approved staged contract; qualification returned rejected_or_inconclusive; no product implementation started.
- **Planned next steps:** return to design after the one bounded qualification failed to establish eligibility. No product code GO or retry issued; any new authorization approach needs scoped review before execution.
- **Anticipatory implementation authorized now:** none.
- **Rationale:** isolate the new trust entry point while reusing the existing confirmation, identity, credential promotion, subscription, webhook, and send paths.

## Delivery Status Canon (Required)
- **Current delivery stage:** `Pending`
- **Qualifiers:** `Blocked`
- **Next exact step:** return to the authorization design with qualification-live-result-cp82.json: the current credential/resource was not qualified. Preserve validators, no product edits or retry. Define a compatible authorization path before a new execution decision.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** `blocked`
- **Why this state now:** the reviewed helper ran once under the approved staged contract, but returned rejected_or_inconclusive. The prerequisite for product implementation was not met.
- **Exit condition:** a reviewed authorization design and eligible grant establish the unchanged prerequisite under an explicit execution decision; material contract changes require renewed approval. No automatic requalification or relaxed validator.

## Scope
- [ ] Add a server-only, explicitly enabled local test-number authorization method to the existing number-registration workflow.
- [ ] Bind only the configured BU/WABA/phone resource, with canonical E.164 verified from Meta. Browser never supplies a token or overrides the configured target; existing confirm resource-ID fields may echo the authorized displayed choice only and must equal the server-pinned target.
- [ ] Create/use a dedicated BU through the normal tenant/admin flow, such as `Teste API Meta`; do not reuse or transfer the separate Sandbox resource in `Teste Meta` or the own-number resource in `Local Test Ofc`.
- [ ] Persist the authorization method on the registration attempt so the new path never fabricates an OAuth code, callback, or `CODE_CONSUMED` event.
- [ ] Reuse nonce/session/actor checks, `currentAttemptId`, attempt version, generation, lease, BU phone claim, durable global provider-resource ownership, candidate encryption, active credential promotion, audit, subscription, webhook receipt, and safe DTO behavior.
- [ ] Permit this local authorization method to confirm only `JA_REGISTRADO`, enforced in backend validation even when a client forges `NOVO`; never request a PIN or call provider number registration, migration, coexistence, unregister, or destructive cleanup.
- [ ] Validate the configured credential against the current Meta app, provider-reported current validity, required WhatsApp scopes and exact WABA/phone target before storing the candidate. If Meta does not return the required grant evidence, fail closed without a weaker fallback.
- [ ] Keep the bootstrap credential in private server configuration only. Never put it in UI payloads, bundles, browser/CLI/artifact URLs, logs, audit, fixtures, support artifacts, or responses. The existing internal provider-bound debug_token request is narrowly preserved under the qualification contract, without exposing its URL. Use the existing encrypted per-channel credential after promotion; do not use the bootstrap credential as a global outbound fallback.
- [ ] Add focused backend and browser-flow evidence for the new local method and regression coverage proving Embedded Signup behavior is unchanged.
- [ ] Document setup using placeholders only, default-off behavior, and safe cleanup/rotation of the private local bootstrap credential.

## Delivery Status Semantics
- `Pending`: no implementation milestone has been reached.
- `Local-Implemented`: only after the scoped changes are implemented and required local validation passes.
- `Lane-Promoted`: only after the declared lane threshold is met.
- `Production-Ready`: not an intended claim for this local-only method; require a new explicit scope decision if production support is proposed.
- `Blocked` is set because the qualification prerequisite was not established; `Provisional` is not set.

## Provisional Notes
- Not applicable: this plan does not claim partial implementation.

## Blocker Notes
- **Blocker:** the one real qualification returned rejected_or_inconclusive; required app/grant/target acceptance and usable canonical phone were not established.
- **Why blocked now:** the approved staged contract forbids product edits after rejected/inconclusive qualification. No code GO was issued.
- **What unblocks it:** return to design and establish an eligible authorization path without weakening shared validators; review any material change before a new execution decision.
- **Owner / source:** root design owner; current Meta credential/resource evidence remains limited to the safe adapter result.
- **Last confirmed truth:** user APROVADO recorded; compiled artifact fresh; helper v4 independently approved; 13 adapter plus 15 launcher synthetic checks passed; one consumed GO, zero retries/provider writes/DB/product changes. No specific provider-cause, token-class, expiry or delivery conclusion.

## Execution Lane Tracking (Required)
- **Local implementation branches:** `feature/number-onboarding` in the principal checkout; local commits only after explicit implementation approval.
- **Promotion lane path:** `none authorized; local-only validation`
- **Lane-promoted threshold for this TODO:** `n/a`
- **Production-ready threshold for this TODO:** `n/a; local-only method`

## Promotion Evidence (Required Before Lane Promotion / Production Ready)
| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Local Meta test-number authorization | `feature/number-onboarding`; future local commit only | n/a | n/a | n/a | staged implementation approved; qualification rejected/inconclusive; product edits stopped; no promotion or source push |

## Out of Scope
- [ ] Changing, weakening, or bypassing the normal Embedded Signup OAuth flow or its grant validators.
- [ ] Registering the API Setup Test Number again, sending SMS, entering a PIN, migrating it, enabling coexistence, unregistering it, or changing Meta account/app settings.
- [ ] Reusing the Sandbox BU or the own-number BU, transferring provider identity across BUs, or changing a BU's canonical phone to make a candidate fit.
- [ ] SQL seeds, direct DB writes, manual mapping/credential insertion, global-token send fallback, fake OAuth, fake webhook receipts, or synthetic physical-message acceptance.
- [ ] Reading or staging `api-app/.local-files`, credentials, private env contents, live provider data, runtime logs, or customer messages as part of planning.
- [ ] Creating an unauthenticated/public development endpoint or accepting a token/resource IDs from a client.
- [ ] Production activation or official onboarding completion. Parent VAL05 and any official proof remain governed by the parent TODO.

## Diff Expectation Contract (Required Before Delivery)
- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| root | `.` | `80e3940126f22a941f90dba4f5e801b6c0eb2f58` | `working_tree` |
| api-app | `api-app` | `db5a86758a165fac8a1ab587599c37b17890530c` | `working_tree` |
| web-app | `web-app` | `74b9d4b714044829796f875d00553f077c1c329d` | `working_tree` |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api-app | `src/domain/channels/number-registration.service.ts` | `M` | Add a distinct local authorization transition converging on candidate promotion. |
| api-app | `src/domain/channels/local-meta-test-config.ts` | A | Optional narrow private configuration/policy helper shared by capabilities and candidate operations; no generic framework. |
| api-app | `src/domain/channels/local-meta-test-config.spec.ts` | A | Focused tests of default-off, partial configuration and exact-target policy if that helper is introduced. |
| api-app | `.env.example` | `M` | Document blank server-side local-mode settings when the API example is the canonical template. |
| api-app | `src/surfaces/bff/number-registrations.controller.ts` | `M` | Add an admin/session-protected route to the existing registration resource. |
| api-app | `src/integrations/meta/meta.client.ts` | `M` | Reuse `MetaHttpClient` grant and exact-resource validation. |
| api-app | `src/integrations/meta/meta.client.spec.ts` | `M` | Cover grant qualification and provider response shapes. |
| api-app | `prisma/schema.prisma` | `M` | Persist explicit official-authorization provenance. |
| api-app | `prisma/migrations/20261018*_local_test_auth_method/migration.sql` | `A` | One scoped migration backfills only existing OFICIAL attempts and preserves NAO_OFICIAL null provenance. |
| api-app | `test/number-onboarding-flow.e2e-spec.ts` | `M` | Prove new and unchanged registration paths, nonofficial regression and owner races. |
| api-app | `test/timeline-fixtures.cjs` | `M` | Add only safe fake local-mode configuration to the existing browser fixture when required. |
| api-app | `test/browser-server.cjs` | `M` | Pass safe fake local-mode settings to the disposable browser-validation API process when required. |
| web-app | `src/componentes/CadastroNumero.tsx` | `M` | Expose local method only when server capability is enabled. |
| web-app | `src/cadastroNumero.ts` | `M` | Extend the existing registration DTO for explicit method selection. |
| web-app | `src/cadastroNumero.lifecycle.ts` | `M` | Preserve method selection through the existing wizard lifecycle. |
| web-app | `src/cadastroNumero.spec.ts` | `M` | Cover capability and unchanged lifecycle behavior. |
| web-app | `e2e/number-onboarding.spec.ts` | `M` | Exercise local onboarding in the real browser flow. |
| web-app | `e2e/number-onboarding-freshness.ts` | `M` | Keep browser request/state freshness assertions bound to the selected method. |
| web-app | `playwright.config.ts` | `M` | Wire only existing disposable browser fixtures if needed. |
| root | `.env.example` | `M` | Document private bootstrap settings with blank/example values only. |
| root | `docker-compose.channels.yml` | `M` | Pass local private settings to API only if required. |
| root | `scripts/test-channels-local.sh` | `M` | Pass safe fake configuration to the canonical disposable browser test when required. |


### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api-app | `.local-files/**` | A,M,D,R | Private operational data is forbidden from scope and Git. |
| api-app | `.env` | A,M,D,R | Private API environment file must never be changed or committed. |
| api-app | `prisma/seed.ts` | A,M,D,R | No seed path is part of this feature. Other unlisted Prisma paths remain unclassified and fail the strict diff guard. |
| api-app | `src/integrations/evolution/**` | A,M,D,R | Evolution behavior is outside this slice. |
| api-app | `src/surfaces/webhooks/meta.controller.ts` | A,M,D,R | Webhook identity and message behavior remain unchanged. |
| root | `.env` | A,M,D,R | Private root environment file must never be changed or committed. |
| root | `.env.testing` | A,M,D,R | Private test/runtime environment file is excluded from versioned diffs and agent rewrites; named human-filled bootstrap settings are allowed only after later approval and explicit setup instructions. |
| web-app | `.env*` | A,M,D,R | Browser/client env must not carry the bootstrap credential. |
| root | `Dockerfile` | A,M,D,R | No image or deployment changes. |
| root | `docker-compose.yml` | A,M,D,R | Base topology is unchanged; only the named local channels overlay may be considered. |
| root | `foundation_documentation/todos/active/features/TODO-leadshug-channel-connection-readiness.md` | A,M,D,R | The parent contract and VAL05 remain under root ownership. |
| root | `foundation_documentation/modules/**` | A,M,D,R | Canonical module consolidation is root-owned and separately reviewed. |
| root | `foundation_documentation/artifacts/analysis/leadshug-meta-api-test-number-binding-proposal-20261018.md` | A,M,D,R | Existing proposal is supporting context and root-owned. |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
| Diff item | Classification (`scope deviation|necessary need|noise`) | Evidence / agent defense | Decision (`revert|clean noise|retain with renewed approval`) | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| none at planning time | n/a | No implementation diff exists. | n/a | n/a |

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** local authorization provenance, provider validation needed for this one credential source, backend capability, the existing wizard step, migration/backfill, and narrowly targeted tests/docs required to preserve the existing registration invariants.
- **Must update or split the TODO:** any production use, other Meta resources/apps, customer-entered credentials, provider registration/migration, changing outbound resolver semantics, changing other channel types, accepting unverified grants, changing parent VAL05, or modifying general ownership/webhook/message behavior.

## Definition of Done
- [ ] DOD-01: Local mode is disabled by default and capability appears only when private server settings pass local shape checks and the caller is allowed to administer the configured BU. Capabilities never calls Meta; real grant/resource validation occurs in authorization and confirmation.
- [ ] DOD-02: An authorized BU admin creates a normal official-channel attempt in the dedicated test BU and chooses the authorization method before nonce reservation; method is included in the idempotency payload and cannot change during the attempt.
- [ ] DOD-03: A separately approved, read-only qualification before product edits proves that the existing adapter accepted Meta is_valid=true, the configured app, both required WhatsApp scopes, intersecting granular WABA targets and exact selected-phone membership. It does not separately establish token type, an expiry timestamp or future lifetime; those remain unknown. Any missing, expired, wrong-app, wrong-scope, wrong-target, malformed, or ambiguous response stops before product edits.
- [ ] DOD-04: Persist nullable official authorization provenance only for `OFICIAL` attempts: `EMBEDDED_SIGNUP|LOCAL_TEST`; existing official rows are backfilled as `EMBEDDED_SIGNUP`, nonofficial rows remain null. Local flow never fabricates OAuth code/callback or `CODE_CONSUMED`.
- [ ] DOD-05: Local authorization and confirmation are read-only provider operations and backend-restricted to `JA_REGISTRADO`; forged `NOVO`/PIN never calls `/register`. After explicit admin confirmation and successful mapping, the existing normal `advance` may perform only the existing current-app WABA subscription step; no callback override or other provider write is added.
- [ ] DOD-06: Options, confirmation, promotion and advance honor the immutable attempt source and fixed configured BU/WABA/phone. Any disabled/changed local configuration during a candidate operation invalidates that candidate before promotion; active credentials are never replaced by a stale candidate.
- [ ] DOD-07: Confirmation reuses exact BU phone, global provider-resource ownership, tenant/admin, current attempt/version/generation/epoch/lease, and active-credential version guards. Existing active credential remains valid until successful promotion; identity never transfers across BUs.
- [ ] DOD-08: Candidate and active credentials use existing authenticated encryption/AAD and per-channel storage. Bootstrap token is never returned, logged, audited, placed in fixtures/artifacts, or used by send/verify/subscribe as global fallback. Secrets never enter browser, callback, CLI argument or artifact URLs. The existing Meta debug_token provider-bound HTTPS request necessarily carries input_token; reuse that adapter call without exposing/recording its URL, headers or errors. This does not authorize any other secret-bearing URL.
- [ ] DOD-09: After promotion, existing subscription, signed webhook identity resolution, receipt gate, `ChannelCredentialResolver`, inbox and outbound path use the same current BU/channel identity and credential contract.
- [ ] DOD-10: React/Vite UI presents local option only when server capability is enabled, never collects/displays secrets, and preserves Embedded Signup and nonofficial flows.
- [ ] DOD-11: Focused PostgreSQL-backed integration/race tests, Meta adapter tests, and Playwright browser navigation prove the new path and rejection cases; canonical API, Web and browser runners pass.
- [ ] DOD-12: Implementation evidence is consolidated; child remains local-only. Parent VAL05 remains independently open with no waiver.

## Validation Steps
- [ ] V-01: Run schema/migration validation and PostgreSQL tests for official-method provenance/backfill, nonofficial null provenance, ownership uniqueness, locking and promotion rollback.
- [ ] V-02: Test `MetaHttpClient` with valid app/grant and wrong app, expired token, missing scopes, missing granular WABA target, wrong WABA/phone, malformed response and timeout/ambiguous provider result.
- [ ] V-03: Test BFF admin/session/nonce/expiry/replay, method selection before attempt reservation, idempotency binding, disabled/default mode, exact configured BU/resource, candidate staging, cancellation, stale attempt, lease contention and active credential preservation.
- [ ] V-04: Assert forged `NOVO`/PIN is rejected before any `/register`; assert no token, OAuth code, PIN, app secret or credential envelope appears in DTO, audit, logs, artifacts or browser requests. Public installation app/config IDs already exposed by capabilities keep their existing classification.
- [ ] V-05: Test same-resource replay and concurrent BU claims; only one owner wins, foreign identity and canonical phone mismatch do not mutate candidate or active credential.
- [ ] V-06: Test local candidate fence: disable or change configured BU/WABA/phone/token source between authorization and options/confirm/promotion; candidate is rejected and cannot be promoted. Revalidate source and fixed target at every candidate use. Also promote successfully, then disable/remove bootstrap settings: normal advance/identity/receipt/resolver operations use the same persisted envelope and owned identity; no deletion, retargeting or bootstrap fallback.
- [ ] V-07: Run project-owned browser navigation in final Web app: enabled method appears only for scoped admin/target, disabled mode is absent, errors are safe, Embedded Signup stays functional, and no secret appears in requests.
- [ ] V-08: After implementation approval and a distinct grant-qualification GO, run the read-only grant qualification. If it passes, a separate code-execution GO is still required. Following implementation, prove signed inbound WhatsApp mapping to exact BU/channel and separately observe outbound reply. SMS, synthetic dashboard HTTP 200, sender ticks, and aggregate counts alone are not delivery proof.
- [ ] V-09: Run `bash scripts/test-channels-local.sh api`, `bash scripts/test-channels-local.sh web`, and `bash scripts/test-channels-local.sh browser` from the approved local branch and preserve actual result artifacts.
- [ ] V-10: Run scope, diff, architecture, security, audit-escalation, assumption coherence, decision adherence, performance/concurrency, and test-quality gates after baseline freeze. Do not claim any result before it is run.

## Completion Evidence Matrix (Required Before Delivery Claim)
| Criterion | Required evidence | Status |
| --- | --- | --- |
| DOD-01, DOD-10 local capability/UI visibility | Browser navigation spec against final local app plus capability integration evidence | pending; no implementation |
| DOD-02, DOD-04 attempt/session/provenance | PostgreSQL-backed BFF integration spec; migration proves OFICIAL backfill and NAO_OFICIAL remains null | pending; no implementation |
| DOD-03 grant qualification | Meta adapter tests plus one bounded authorized real grant qualification after approval; safe metadata only | blocked: one real qualification rejected_or_inconclusive; no product edits permitted |
| DOD-05 registration/subscription boundary | Integration assertions: zero `/register`; only explicit normal `advance` may subscribe the mapped WABA through the current app | pending |
| DOD-06 candidate fencing | PostgreSQL tests: disable/rotate local source while candidate is in flight; active credential preserved | pending |
| DOD-09 after-promotion disable | PostgreSQL scenario: disable/remove bootstrap after promotion, normal advance/receipt/resolver still use unchanged persisted credential and identity | pending |
| DOD-07 ownership/phone/races | PostgreSQL concurrency tests on same-resource claims and BU canonical phone guards | pending |
| DOD-08 encryption/privacy | crypto/AAD unit tests, response/audit/log redaction assertions, security review | pending |
| DOD-09 subscription/webhook/resolver/inbox | focused signed-webhook and outbound integration flow with exact current identity; no synthetic receipt accepted | pending |
| DOD-10 React/Vite UI behavior | Existing wizard component/lifecycle specs and focused Playwright navigation prove capability gating, secret-free requests, and unchanged Embedded Signup behavior | pending; no implementation |
| DOD-11 canonical test suites | Actual API, Web, and browser runner outputs from the approved local branch | pending; no implementation |
| DOD-12 child closeout and parent separation | Reviewed local-only implementation evidence; parent VAL05 remains open without waiver | pending; no implementation |

## External Dependency Readiness (Required When External Systems Matter)
| Dependency | Required capability | Current evidence | Readiness |
| --- | --- | --- | --- |
| Meta Graph API | Credential for the same app, is_valid=true reported by Meta, both WhatsApp scopes, intersecting granular WABA targets, and exact-phone read. Token type and explicit expiry metadata are not inspected by the current adapter. | API Setup Test Number message was observed in WhatsApp; no credential/grant was read or tested. Existing `MetaHttpClient` rejects grants that do not meet current app/scope/target rules. | unknown; after implementation approval, do bounded read-only qualification under distinct GO before product edits; fail closed on mismatch |
| Meta webhook delivery | Signed message for exact mapped phone must arrive at configured callback. | Direct message arrival in handset is not webhook evidence; official ingress remains separate. | separate real proof required |
| Local private config | Bootstrap token and exact BU/WABA/phone settings available only to local API process; opt-in defaults false and is independent of `NODE_ENV`. | No private configuration inspected. | pending; setup requires separate authorization and must not appear in artifacts |
| PostgreSQL | Migration and race behavior for official method provenance and identity/credential promotion. | Existing registration model has attempt/lease/credential/identity fences; no schema change made. | pending local integration proof |

## Profile Scope & Handoffs (Required Before APROVADO)
- **Primary execution profile:** operational-coder
- **Current profile:** operational-devops, bounded qualification preparation; Genesis rejected because canonical project and reviewed contract already exist
- **Active technical scope:** nestjs, react, vite, prisma, postgresql, docker
- **Expected supporting profiles:** `assurance-tester-quality, assurance-security-adversarial, strategic-cto`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log (Update when execution crosses profile boundaries)
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| operational-devops | operational-coder | Implement only after qualification and approval, then return to DevOps for activation. | Named source/schema/UI/test paths | planned; no product writer active |
| planning owner | strategic-cto | Review a new authorization method adjacent to the approved channel architecture. | bounded TODO, module decision baseline, architecture review package | planned; not dispatched |
| operational-coder | assurance-security-adversarial | Assess secret bootstrap, tenant isolation, trust/ownership and grant validation. | API, schema, config, UI, tests | planned after approval; not dispatched |
| operational-coder | assurance-tester-quality | Verify exact behavior, rejection evidence, fixtures and real-backend/browser coverage. | API/PostgreSQL and Web navigation tests | planned after implementation; not dispatched |

## Complexity
- **Level (`small|medium|big`):** `medium`
- **Checkpoint policy:** one full checkpoint before approval; serialized qualification, schema/authentication, UI/validation and delivery-review checkpoints after approval.
- **Why this level:** bounded extension of existing channel registration; the auth, tenant, schema, UI and provider edges still require full planning, architecture, security, TQA and concurrency scrutiny.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md` (current provider implementation is `api-app/src/integrations/meta/meta.client.ts`, class `MetaHttpClient`).
- **Secondary module docs:**
  - `foundation_documentation/modules/identity-and-tenancy.md`
  - `foundation_documentation/modules/audit-and-history.md`
  - `foundation_documentation/modules/inbox-and-conversations.md`
- **Planned decision promotion targets:** `Cadastro de números ST-CON-01` and `Reautorização e ativação da credencial (NUM-ARCH-06)` in integrations-and-channels.
- **Module decision consolidation targets:** add a clearly local-only authorization-method subsection and links to the child TODO; preserve the existing OAuth, ownership, credential, and receipt rules.

## Decision Pending (Resolve Before Freeze)
No unresolved architecture choice remains in the proposed design. The concrete grant remains unqualified and is a staged prerequisite: after implementation approval, a bounded read-only grant qualification must pass before any product edit. Failure returns the work to design without weakening current validators.

## Decisions (Resolved Before Freeze)
- D-01: The supplied Meta API Setup access credential must pass the existing same-app, is_valid, required scopes, intersecting granular WABA targets and exact-phone checks. No independent token-class or explicit-expiry/lifetime proof is claimed. Failed/inconclusive qualification is a hard stop before product edits, never a reason to weaken Embedded Signup.
- D-02: Server-only settings are META_LOCAL_TEST_ENABLED=false, META_LOCAL_TEST_BU_ID, META_LOCAL_TEST_WABA_ID, META_LOCAL_TEST_PHONE_NUMBER_ID and META_LOCAL_TEST_ACCESS_TOKEN. The opt-in is separate from NODE_ENV. Create a dedicated BU through the normal admin flow before configuring its fixed ID; the canonical phone comes from Meta and must match the BU. Bootstrap is not a send fallback.
- D-03: Preserve existing OAuth semantics and add nullable officialAuthorizationMethod values EMBEDDED_SIGNUP|LOCAL_TEST only for OFICIAL. Backfill existing official rows to EMBEDDED_SIGNUP; NAO_OFICIAL remains null. Choose method before attempt/nonce reservation, include it in the idempotency request hash, and keep it immutable.
- D-04: Local method is JA_REGISTRADO-only, enforced server-side. No PIN, register, migration, coexistence, unregister or callback override. Confirm reuses shared ownership/canonical-phone/candidate/active-credential promotion; normal advance may perform the existing current-app subscription after mapping.
- D-05: Reuse current actor/tenant/admin/session, nonce, attempt/version/generation/epoch/lease and active-credential fences through commit. Fixed local source and target are rechecked through candidate operations; disabled/rotated source invalidates unpromoted candidates. After promotion, bootstrap disable/rotation does not delete or retarget the active channel; normal consumers use its stored credential.
- D-06: Scope remains a single explicitly configured local test resource; no source push, Railway, production activation, new global credential service or parallel channel/message lifecycle. Binding is not webhook delivery proof. Child and parent real-message evidence remain separate; parent VAL05 cannot be waived by this child.

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `integrations-and-channels#Cadastro de números ST-CON-01` | OAuth is the current authorization entry; shared ownership/candidate/credential/receipt invariants apply. | Supersede (Intentional): extend authorization entry with default-off local method; preserve all shared invariants | `foundation_documentation/modules/integrations-and-channels.md:13-54` |
| `integrations-and-channels#NUM-ARCH-06` | Candidate credential is separate from active; promotion uses current attempt/ownership/generation fences. | Preserve | `foundation_documentation/modules/integrations-and-channels.md:55-59` |
| `identity-and-tenancy#Autorização do cadastro de números ST-CON-01` | Existing BU admin and tenant isolation remain required. | Preserve | `foundation_documentation/modules/identity-and-tenancy.md:18` |
| `audit-and-history#Cadastro e diagnóstico de canais ST-CON-01` | Registration stages are auditable without secrets or raw provider payloads. | Preserve; record method as safe enum only | `foundation_documentation/modules/audit-and-history.md:13` |
| `inbox-and-conversations#Aceitação de mensagens ST-CON-01` | Inbound acceptance uses a verified current identity; exact message receipt is not inferred from unrelated activity. | Preserve | `foundation_documentation/modules/inbox-and-conversations.md:55` |

## Decision Baseline (Frozen Before Implementation)

D-01..D-06 above form the single decision set, proposed for renewed published freeze after ARCH-QUAL-01 integration. No parallel numbering or implementation approval is implied. Decision adherence must cover every row, including app/grant qualification and private configuration.

## Architecture Change Governance
- **Applicability:** `required`
- **Why this applies:** a new credential trust source and authorization transition affect authentication, tenant isolation, persistence, and a critical channel connection flow.
- **Deviation / debt being retired:** none; this extends the approved Embedded Signup flow without replacing it.
- **Target steady-state after closeout:** both authorization methods produce the same verified, owned, encrypted per-channel credential state; only the method provenance differs.
- **Temporary exceptions allowed:** one explicitly enabled local-only bootstrap source for the single configured API Setup Test Number; no production use, no other number/app, and no generic credential endpoint.
- **Cutover / removal condition:** no cutover from OAuth. Local exception remains only while explicitly enabled for local test use; disable by removing the opt-in and private bootstrap values.

### Patterns To Enforce
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Tenant-owned resource identity | `ST-CON-01` | OFICIAL resources | A provider ID cannot move between BUs or bypass the durable owner. |
| Candidate then atomic active promotion | `NUM-ARCH-06` | channel credentials | Failed setup cannot replace a valid active credential. |
| Secret-free DTO and audit | `integrations-and-channels` invariants | BFF/config/audit | Local configuration is a server trust source, never browser data. |
| Receipt-gated connection | `ST-CON-01` | channel readiness | Binding and successful provider authorization alone do not mean connected. |

### Prohibited Anti-Patterns
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| OAuth-shaped fake local flow | `CODE_CONSUMED`, synthetic code/callback, OAuth nonce exchange called for local method | Misstates provenance and can hide replay/security gaps. | none |
| Global token send fallback | Resolver or outbound adapter reads local bootstrap token | Breaks per-channel BU isolation and credential rotation. | none |
| Manual DB mapping/credential seed | SQL seed or direct insert outside domain path | Bypasses ownership locks, audit, encryption and current-attempt fencing. | none |
| Browser-supplied secret/resource | token or arbitrary WABA/phone fields in request | Makes local bootstrap a credential exposure and confused-deputy surface. | none |
| Weakening common grant validator | special-case accepts missing scopes/target grant | Makes normal OAuth less secure and masks unsupported provider state. | none |

### Architecture Protection Harness
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| integration test | registration API | focused PostgreSQL e2e in `api-app/test/number-onboarding-flow.e2e-spec.ts` | Local method skips admin/session/nonce/attempt/ownership fences | implement-in-this-todo | DOD-02/06 evidence |
| test | provider boundary | focused `meta.client` specs | Local method accepts wrong app, scope, WABA or phone | implement-in-this-todo | DOD-03 evidence |
| migration test | Prisma schema | migration deploy/status plus old-attempt backfill assertion | Existing attempts acquire wrong/missing method provenance | implement-in-this-todo | DOD-04 evidence |
| browser navigation | registration wizard | project-owned Web runner and new focused spec | Secret exposure, hidden/visible capability errors, OAuth regression | implement-in-this-todo | DOD-09 evidence |
| static review/guard | repository diff | scope, secret, architecture, audit escalation guards | unscoped files, `.local-files`, global fallback, unrelated runtime edits | already-enforced | freeze package records actual guard outputs |

## Architecture Review Gates
- **Architecture decision review:** `required`
- **Decision review lifecycle:** after diagnosis and before implementation approval.
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** fresh internal architecture_opinion raw planning-architecture-v1.raw.json, verdict revise; ARCH-QUAL-01 integrated as bounded qualification contract, ARCH-DOC-02 numbering aligned and ARCH-TEST-03 post-promotion-disable scenario named. Separate fresh critique will verify these corrections; no implementation pass claimed.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** after implementation and before Completed.
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** pending implementation; no review claimed.
- **No-go handling:** unresolved architecture divergence returns to diagnosis/decision; no APROVADO or completion claim.

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Why this decision:** exact reviewed contract plus schema/Markdown/source-citation corrections published before final guards.
- **Trigger stage:** before final post-review guards and approval request
- **Baseline branch:** main
- **Baseline commit:** f35d1a0d4815629342cc0ac8df3c2e14a97e8a97
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** final7ownedblobs byte-exact and pushed. Architecture e83d5bdc + approve critique 92429fed remain valid; root-final-format-equivalence proves all23materialsections match after only row-aware format and existing-source-citation transforms. No waiver or execution approval.
- **Evidence / reference:** artifacts/reviews/leadshug-meta-test-binding-20261018/baseline-freeze-f35d1a0d.json; root-final-format-equivalence.json
- **Waiver authority / reference:** n/a

## Gate: Review Scope Drift
- **Gate decision:** `required`
- **Why this decision:** this addition must remain within the local API Setup resource and cannot silently change parent ST-CON-01.
- **Trigger stage:** after planning reviews converge and before implementation approval.
- **Baseline source:** `Gate: Review Baseline Freeze -> Baseline commit`.
- **Material sections compared:** `Context|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Decisions|Decision Baseline|Architecture Change Governance|Execution Plan|Flow Evidence Planning Matrix|Security Risk Assessment|Performance & Concurrency Risk Assessment`.
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-meta-api-test-number-binding.md`
- **No-go handling rule:** return to review, revalidate any material evolution with the user, refresh the baseline, and rerun affected lanes.
- **Gate status:** `no_material_findings`
- **Findings summary:** final guard v3 go against pushed f35d1a0d; all23materialsections compared, zero changed. No waiver.
- **Evidence / reference:** artifacts/reviews/leadshug-meta-test-binding-20261018/scope-drift-v3.json
- **Waiver authority / reference:** `n/a`

## Questions To Close
- [x] Local technical method direction accepted by the human in CP81, without implementation approval.
- [x] Server-only configuration, explicit method provenance, fixed target and default-off behavior selected in D-01..06; no competing product decision remains.
- [ ] Execution prerequisite after later approval: qualify the concrete token using current app/scope/target rules. Unknown eligibility is neither waived nor claimed; failed qualification stops before product edits.
- [ ] Delivery prerequisite: prove real webhook arrival and inbox/reply separately. Parent VAL05 remains open.

## Pattern References (Optional; Enforced When Cited)
No PACED pattern ID is asserted in this draft. The module decisions above are project-local invariants, not catalog IDs.

| Pattern/Anti-Pattern ID | Type | Why Referenced | Level |
| --- | --- | --- | --- |
| none | n/a | No catalog entry has been verified for this behavior. | n/a |

## Assumptions Preview (Required Before Plan Review)
| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | The configured Meta API Setup token may satisfy current same-app, provider-reported validity, scope and granular target checks for this API Setup resource. | No credential was inspected; `MetaHttpClient.assertCurrentGrant`, `recursos` and `confirmarNumero` define the checks but do not prove this token (`api-app/src/integrations/meta/meta.client.ts:80-107,155-173`). | Run only the separately approved bounded pre-code grant qualification specified below; success proves the checks actually performed, not token type/explicit lifetime. If any check fails, stop before product edits and return to design. | Low | Keep as Assumption |
| A-02 | Nullable `officialAuthorizationMethod` can be persisted only for `OFICIAL` attempts with EMBEDDED_SIGNUP or LOCAL_TEST; existing official attempts backfill to `EMBEDDED_SIGNUP`, while `NAO_OFICIAL` remains null. | `ChannelRegistrationAttempt` is shared by official and nonofficial flows and stores state/stage/version/candidate envelope (`api-app/prisma/schema.prisma:191-225`; shared creation for both types: `api-app/src/domain/channels/number-registration.service.ts:122-128`). | Migration and PostgreSQL regression must prove the official backfill, nonofficial-null invariant, and immutable method binding before nonce reservation. | Medium | Keep as Assumption |
| A-03 | A local explicit opt-in can be passed to the API process separately from `NODE_ENV`. | `docker-compose.channels.yml` and `api-app/src/infra/config/modulos.ts` provide process configuration seams; no private configuration was inspected. | If deployment cannot enforce this as local-only, do not implement or enable the mode. | Medium | Keep as Assumption |
| A-04 | Existing resource confirmation can be reused without a credential fallback. | `NumberRegistrationService.confirm` and `MetaHttpClient.confirmarNumero` validate selected WABA/phone (`api-app/src/domain/channels/number-registration.service.ts:228-241`; `api-app/src/integrations/meta/meta.client.ts:145-174`). | Add a narrow adapter only if necessary; keep current behavior for OAuth. | High | Keep as Assumption |

## Execution Plan (Required Before APROVADO)
### Touched Surfaces
- `api-app/src/surfaces/bff/number-registrations.controller.ts` and `api-app/src/domain/channels/number-registration.service.ts`.
- `api-app/src/integrations/meta/meta.client.ts` (`MetaHttpClient`) and `api-app/src/integrations/meta/meta.client.spec.ts`.
- `api-app/prisma/schema.prisma`, one migration, `api-app/test/number-onboarding-flow.e2e-spec.ts`, and only the existing browser fixtures `api-app/test/timeline-fixtures.cjs` / `api-app/test/browser-server.cjs` if needed.
- `web-app/src/componentes/CadastroNumero.tsx`, `web-app/src/cadastroNumero.ts`, `web-app/src/cadastroNumero.lifecycle.ts`, `web-app/src/cadastroNumero.spec.ts`, `web-app/e2e/number-onboarding.spec.ts`, `web-app/e2e/number-onboarding-freshness.ts`, and `web-app/playwright.config.ts` only if fixture wiring is needed.
- Root `.env.example`, `docker-compose.channels.yml`, and `scripts/test-channels-local.sh` only for blank docs or safe disposable test wiring; private env files remain excluded.
- Foundation module documentation is root-owned and outside this code diff; parent TODO remains unchanged.

### Ordered Steps
1. After explicit implementation approval, prepare and review a bounded read-only grant qualification helper under `foundation_documentation/artifacts/tmp/number-onboarding-execution/`; product-source edits remain prohibited until it passes.
2. After a distinct root GO, execute only the bounded qualification contract below. Read the explicitly allowlisted base app configuration and one local token/target in memory, call the named public exact-target method, and emit its fixed booleans/enums. No Nest bootstrap, DB, mutation, raw provider details or secret output. Failure/inconclusive result stops before product edits.
3. Select authorization method before attempt creation/idempotency and nonce reservation; include it in the idempotency request hash (the client key remains the existing UUID). Persist nullable official-only `officialAuthorizationMethod`; backfill existing OFICIAL rows to `EMBEDDED_SIGNUP`, keep NAO_OFICIAL null, and enforce the invariant in schema/migration validation. The method is immutable for the attempt and cannot switch after candidate lease or during confirmation.
4. Add an ADMIN/session/nonce/current-attempt guarded local authorization route that reads only server configuration, validates exact app/grant/target, and stages an encrypted candidate with `LOCAL_TEST` provenance. Never exchange OAuth code or write `CODE_CONSUMED`.
5. Make `options`, `confirm`, and promotion recheck immutable method and exact BU/WABA/phone. If local mode is disabled or its token/target changes while a candidate is staged, reject it before promotion and require a new attempt; never promote a stale candidate. `advance` acts only on the current mapped resource and promoted per-channel credential, using the existing current-app subscription step.
6. Enforce `JA_REGISTRADO` in the domain layer and controller boundary; prove zero `/register` calls. Add capability and a small wizard choice for only the configured resource; no secrets or arbitrary provider IDs enter the browser.
7. Add focused provider, migration, nonofficial regression, race, privacy and browser tests; preserve existing Embedded Signup assertions. Run canonical API/Web/browser suites.
8. Complete architecture, security, TQA, concurrency and scope reviews; consolidate stable module decisions through root ownership. Close only this child after evidence passes; parent VAL05 stays independent.

### Test Strategy
- **Strategy:** `test-first`
- **Why:** authorization provenance, server-only configuration and ownership races need explicit fail-closed assertions.
- **Fail-first targets:** disabled mode; wrong/expired/incomplete grant; forged NOVO; method-switch/replay; stale attempt; foreign resource; BU phone mismatch; concurrent claim; secret redaction; nonofficial attempts remaining null and unchanged.

### Pre-APROVADO RED Evidence Capture
- **Decision (`required|recommended|not_needed|waived`):** `not_needed`
- **Why now:** this is a new feature, not a reproduced defect; no pre-approval red reproduction is required.
- **Target symptom:** `n/a`.
- **Allowed surfaces:** `n/a`.
- **Forbidden surfaces reaffirmed:** product code, runtime/config/deploy mutation, private credentials, provider calls, DB and docs beyond this child TODO.
- **Planned command / target:** `n/a`.
- **Status (`not_run|running|red_reproduced|red_not_reproduced|blocked|waived`):** `not_run`.
- **Findings summary:** not applicable; no pre-approval tests or support writes are authorized.

### Flow Evidence Planning Matrix
| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Local method capability and wizard selection | visible UI and authorization mutation | web-only | Playwright mutation | yes | yes | focused browser journey in `web-app/e2e/number-onboarding.spec.ts` against local API/PostgreSQL | n/a; React/Vite Web is the product surface |
| Local credential authorization and candidate display | DTO/domain/state consumed by UI | web-only | Playwright mutation | yes | yes | BFF integration plus browser flow using project Playwright runner | n/a |
| Confirmation and receipt-gated readiness | persisted state and webhook/inbox flow | web-only | Playwright mutation | yes | yes | signed-webhook integration and browser readback | n/a |
| Existing Embedded Signup | regression of same public flow | web-only | Playwright mutation | yes | yes | existing browser flow on final local app | n/a |

### Local CI-Equivalent Suite Matrix
| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| api-app + PostgreSQL | authorization, migration, races, owner isolation | local method acceptance/rejection, official provenance migration, unchanged OAuth and NAO_OFICIAL | disposable project DB; migration applied | `bash scripts/test-channels-local.sh api` | Local-Implemented | planned | pending | Real project-owned runner and PostgreSQL. |
| Web unit/component | wizard state and lifecycle | capability disabled/enabled and unchanged OAuth control | deterministic fixtures; no token in browser | `bash scripts/test-channels-local.sh web` | Local-Implemented | planned | pending | Project-defined Web suite. |
| Web browser | final browser navigation and API mutation | complete local registration and unchanged Embedded Signup | local API/PostgreSQL validation services; no secret in browser | `bash scripts/test-channels-local.sh browser` | Local-Implemented | planned | pending | `web-app/e2e/number-onboarding.spec.ts` and `web-app/playwright.config.ts`. |

### Runtime / Rollout Notes
- Private settings are `META_LOCAL_TEST_ENABLED=false`, `META_LOCAL_TEST_BU_ID`, `META_LOCAL_TEST_WABA_ID`, `META_LOCAL_TEST_PHONE_NUMBER_ID`, and `META_LOCAL_TEST_ACCESS_TOKEN`. Document blank placeholders in root `.env.example`; pass through `docker-compose.channels.yml` only if required. The opt-in is independent of `NODE_ENV`, defaults false, and is permitted only in explicitly configured local setup.
- Pre-code qualification is read-only, requires later implementation approval plus a distinct root GO, and follows the complete allowlist/method/budget/output contract below. Failed/inconclusive qualification stops before product source changes. Private .env.testing is operator-owned: the human may fill the new named values after approval; no tracked diff, bulk rewrite, mount, copy, hash or dump of that file is authorized.
- Apply one additive migration through the project migration process; no SQL seeds or direct identity/credential writes.
- Local authorization and confirmation make no provider writes. After explicit admin confirmation and successful mapping, the existing normal `advance` action may subscribe the exact WABA to the current app as the established channel flow does; no callback override or other provider write is added.
- Disable new local authorization by setting the opt-in false and removing private bootstrap settings; do not silently delete active per-channel credentials. No production rollout, product source push, Railway action, Meta publication, re-registration, DNS/tunnel change, or lane promotion is authorized.

### Bounded Qualification Contract — ARCH-QUAL-01

Applies only after later explicit implementation approval, helper review/offline checks and a distinct consumed-once root live GO. It is a provider-read prerequisite before any product-source edit, not a general runtime diagnostic authorization.

- Inputs: existing API-process META_APP_ID, META_APP_SECRET, META_SIGNUP_CONFIG_ID and GRAPH_VERSION, plus only META_LOCAL_TEST_ACCESS_TOKEN, META_LOCAL_TEST_WABA_ID and META_LOCAL_TEST_PHONE_NUMBER_ID from the operator-owned private configuration. The four base values may already be inherited by the API process; do not inspect Config.Env. Validate expected app/version from the accepted installation. The target BU is enforced later by the normal application flow; qualification performs no BU lookup or ownership claim.
- Delivery: read only the named local keys from .env.testing into memory after the operator fills them. Send any needed private inputs via subprocess stdin, never command arguments, shell interpolation, a URL, a persisted temporary payload or environment/config dump. Do not serialize/print/hash the file, token, app secret, WABA, phone ID or canonical phone. No other private configuration keys are admitted by inference.
- Artifact: import only the already-built dist/integrations/meta/meta.client.js and instantiate MetaHttpClient, without AppModule/Nest bootstrap, DI overrides or private method access. Attest its file hash and container/image/source ownership against the accepted source inventory before credential use; historical image/compiled pins are context, not a new live observation. If no matching artifact is available, stop. An isolated no-private-input compile may be separately planned/reviewed if needed; do not modify source or quietly use stale code.
- Method and budget: exactly one call to public verificarNumeroVinculado(expectedWabaId, expectedPhoneNumberId, token). It performs one debug grant read and at most two phone pages for that fixed WABA: at most three provider GETs, each existing timeout10s, no retries, no redirects, no exchangeCode/register/subscribe/send. Fixed HTTPS graph.facebook.com and configured v26.0 only. Maximum page size100; absent/beyond-limit/malformed/inconclusive target stops. Outer helper deadline40s; abort safely if exceeded.
- Success means only the inherited app/is_valid/scopes/intersecting granular WABA guards passed, the selected phone was found, and its canonical-phone shape is usable. No token-class, expiry timestamp, remaining lifetime, app subscription, BU ownership, inbox or real delivery assertion follows. Revalidate grant/resource through normal candidate confirmation after implementation; an earlier qualification never grants permanent trust.
- Result allowlist: schema/checkpoint, outcome qualified|rejected_or_inconclusive|preflight_failed, adapterFresh boolean, currentGrantAndTargetAccepted boolean, canonicalPhoneUsable boolean, tokenClassEvidence=unknown, explicitExpiryEvidence=unknown, deliveryEvidence=not_tested, providerWrites=0, optional fixed safe error enum. A true grant/target boolean is inferred only from successful return through the named adapter; no raw debug response is exported. Unknown failure details remain a safe combined outcome rather than invented attribution.
- Privacy/operation checks: helper source frozen and inspected with fake inputs before real use; fixed schema validated on success and failure. No raw errors, HTTP URLs/headers/bodies, arbitrary stdout/stderr, provider-ID logs, other-WABA scans, DB access or mutation. The existing provider-bound debug request internally carries input_token as required by the adapter; its URL is neither printed nor retained. Root records one safe receipt and stops before any product edit unless qualified. No weakening of any common validator or token fallback is authorized.

## Plan Review Gate
Full planning review completed through independent architecture v1 and fresh critique v1 on the corrected pushed baseline. Critique verdict approve, zero material blockers; all seven lenses explicitly assessed. Product, tests, grant and delivery remain unproved.

### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards
- **Issue ID:** `PLAN-01`
  - **Severity:** `high`
  - **Evidence:** `api-app/src/domain/channels/number-registration.service.ts:179-204,228-365`; `api-app/src/domain/channels/channel-credential-resolver.ts:21-59`.
  - **Why it matters now:** a new credential source could bypass existing OAuth, grant, ownership, or per-channel send boundaries if modeled as a shortcut.
  - **Option A (Recommended):** add explicit authorization-method provenance and a separate guarded entry point that stages the same encrypted candidate and converges on existing confirmation/promotion.
    - **Effort:** high; **Risk:** medium; **Blast radius:** cross-module; **Maintenance burden:** medium; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** accept a token/resource on current `authorize` body and infer its origin.
    - **Effort:** medium; **Risk:** high; **Blast radius:** cross-module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** keep OAuth-only behavior.
    - **Effort:** low; **Risk:** low; **Blast radius:** local; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** Option A, only after grant qualification and implementation approval; otherwise Option C.
- **Issue ID:** `PLAN-02`
  - **Severity:** `high`
  - **Evidence:** Meta API Setup grant semantics have not been verified for the exact resource.
  - **Why it matters now:** a missing granular WABA grant cannot be repaired safely by relaxing shared validators.
  - **Option A (Recommended):** qualify the credential and exact target with current Meta validators; fail closed if unsupported.
    - **Effort:** medium; **Risk:** low; **Blast radius:** local; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
  - **Option B (Alternative):** bypass granular grant checks for local mode.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
  - **Option C (Do Nothing):** defer if Meta grant cannot satisfy current contract.
    - **Effort:** low; **Risk:** low; **Blast radius:** local; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
  - **Recommendation:** Option A with Option C as mandatory stop condition; reject Option B.

### Failure Modes & Edge Cases
- Expired/revoked token, wrong app, missing scope, missing granular target, wrong WABA/phone, malformed provider response, provider timeout with ambiguous result.
- Admin session changes, nonce replay, attempt expiration, stale currentAttempt/generation/epoch, concurrent confirmation, active credential rotation during candidate staging.
- Same resource claimed by another BU, canonical BU phone mismatch, un-managed legacy identity, deleted/detached identity, duplicate local config.
- Forged `NOVO` or PIN, local mode disabled, partial configuration, production/global deployment accidentally enabled, disabled configuration after candidate creation.
- Error/audit/DTO/log/screenshots accidentally contain access token, secret, phone resource identifiers, or provider raw payload.
- Webhook arrives before promotion, after disable, for an unmapped or stale identity; receipt cannot be inferred from dashboard HTTP 200 or handset display.

### Residual Unknowns / Risks
- Whether the concrete API Setup credential exposes the exact scopes and granular resource grant required by existing validators is unknown.
- Whether the configured resource is valid for app subscription and both inbound/outbound operations must be qualified after approval.
- A local bootstrap token is an additional secret-at-rest and must have a documented rotation/removal path; no production availability is intended.

## Additional Architectural Opinions
- **Needed:** `no`
- **Why ambiguity remains:** the candidate architecture is to reuse the existing number-registration workflow with explicit method provenance. The unresolved grant compatibility is a provider qualification blocker, not a competing architecture requiring an opinion package.
- **Opinion count:** `0`
- **Package mode:** `bounded-summary`
- **Internal reviewer mandate:** `not_needed` for additional opinions; required architecture and security review gates remain above.
- **Required lenses:** `correctness|security|operational-fit`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | n/a | n/a | no opinion dispatched |

## Audit Trigger Matrix
- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-meta-api-test-number-binding.md`
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-meta-test-binding-20261018/audit-floor-v1.json; actual outcome go after published freeze, fingerprint de083b11b58d. All derived gates remain pending until performed at their lifecycle stage.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | Bounded cross-stack authorization extension with high security impact. |
| `blast_radius` | `cross-stack` | BFF, provider adapter, persistence, browser flow. |
| `behavioral_change_or_bugfix` | `yes` | Adds a new authorization method. |
| `changes_public_contract` | `yes` | New BFF route and registration provenance. |
| `touches_auth_or_tenant` | `yes` | Credential trust and BU ownership. |
| `touches_runtime_or_infra` | `yes` | Local private configuration and service process behavior. |
| `touches_tests` | `yes` | New and regression tests. |
| `critical_user_journey` | `yes` | Official channel onboarding. |
| `release_or_promotion_critical` | `no` | Local-only scope; no production release or promotion is authorized. Auth/security review remains required. |
| `high_severity_plan_review_issue` | `yes` | PLAN-01 and PLAN-02 are high until resolved. |
| `explicit_three_lane_request` | `yes` | The planning review package requires the canonical triple-review protocol for this cross-module auth/schema change. |

## Independent No-Context Critique Gate
- **Critique decision:** `required`
- **Why this decision:** medium-sized auth/schema extension with high tenant and credential impact; full architecture, security, test-quality, and concurrency review remains required.
- **Impact signals in scope:** `cross-module blast radius|public contract/schema/api|auth/payment|critical-user-journey`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen baseline, scope, assumptions, execution plan, issue cards, residual risks and any waivers.
- **Critique isolation mode:** fresh internal no-context reviewer.
- **Internal reviewer mandate:** required after a frozen package; executor cannot be reviewer.
- **Canonical multi-lane audit protocol:** `audit-protocol-triple-review`
- **Audit session / round evidence:** pending freeze and dispatch.
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `findings_integrated`
- **Findings summary:** fresh critique approve; zero material blockers; ARCH-QUAL-01, ARCH-DOC-02 and ARCH-TEST-03 confirmed resolved. CRIT-MIG-01 optional test timing clarification integrated under V-01/V-03.
- **Resolution ledger:** no findings yet.
- **Evidence / reference:** artifacts/reviews/leadshug-meta-test-binding-20261018/planning-critique-v1.raw.json; root-critique-v1-resolution.json; raw SHA b39207f874cb7b3d58522756c5f5fd572af3bd1deb2d5c5bf89191379eb4543e.
- **Waiver authority / reference:** `n/a`

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CRIT-MIG-01 | Integrated | useful | partial | project | none | Name existing V-01/V-03 historical same-method replay case after provenance migration; no new behavior/framework. |

## Gate: Assumption Code Coherence
- **Gate decision:** `required`
- **Why this decision:** the exact grant and persistence shape can affect implementation safety.
- **Trigger stage:** after critique convergence and before implementation approval.
- **Guard scope:** `A-01,A-02,A-03,A-04`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-meta-api-test-number-binding.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** A-01..04 statically checked against current named source and both independent reviews; actual token remains unknown and mandatory pre-code qualification is unwaived.
- **Evidence / reference:** artifacts/reviews/leadshug-meta-test-binding-20261018/root-assumption-coherence-v1.json; code-coherence-v3.json go validates all4live assumptions. v1/v2 qualified historical results retained; actual grant remains unknown.
- **Waiver authority / reference:** `n/a`

## Approval
- **Approved by:** user, explicit APROVADO on 2026-10-18.
- **Approval scope:** exact reviewed local-only staged contract published at 7f478ee38d31827786c6eafc0b1168f9fc5d2d83 (scope baseline f35d1a0d4815629342cc0ac8df3c2e14a97e8a97): bounded read-only qualification first; product implementation only if qualified and under a separate root code GO; named local validation and later activation gates preserved.
- **Approval reference:** current user statement “APROVADO”, after root presented the reviewed staged plan; earlier direction-only statement retained in CP81 history.
- **Implementation approval:** `APROVADO; staged`
- **Execution not authorized by approval:** product edits before qualification/code GO; provider writes during qualification; register/migrate/unregister; arbitrary credential or DB inspection; source push, Railway, worktrees, production activation or physical sends without their distinct gates.
- **Renewed approval required when:** auth method, target cohort, secret handling, grant/ownership validation, schema, validation semantics or deployment boundary materially change.

## Rules Acknowledgement / Ingestion

The listed sources were actually reloaded after APROVADO on 2026-10-18 for qualification preparation. Future product/runtime surface handoffs must reload their relevant methods again before edits.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | Tactical and delegation boundaries | One writer and review gates | Worktrees or unsolicited scope | Separate root/reviewer/executor |
| delphi-ai/workflows/docker/effort-selection-method.md and delphi-ai/tools/agent_role_routing_guard.py | Executor and independent reviewer routing | Declared model/effort and positive guard | Root implementation or topology inference | Qualification executor gpt-6-luna/medium; formal critique gpt-6.1-sol/max; both routing receipts go |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | New authorization method | Frozen review and explicit approval | Direction mistaken for implementation approval | No source before gates |
| delphi-ai/workflows/docker/todo-execution-boundary-method.md | Scope and execution authority | Normal authority GO and source fences | Hidden scope expansion | Stop on material change |
| delphi-ai/workflows/docker/environment-readiness-method.md | Existing local runtime | Owned runtime and private env preservation | Reset or broad stack restart | Distinct live GO |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | BFF and domain entry | Shared domain invariants | Public dev bypass | API/PG contract evidence |
| delphi-ai/workflows/react/change-ui-boundary-method.md | Wizard consumer | Lifecycle and explicit capability | Secret in browser or stale submit | Real-backend browser |
| delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | Nullable official provenance | Versioned additive migration | Rewriting applied migrations | Migrate deploy/PG test |
| delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | Identity/promotion races | Locks and short transactions | HTTP inside transaction | Barrier tests |
| foundation_documentation/policies/scope_subscope_governance.md | Route ownership | BFF session/tenant/BU | Confused deputy | Module consistency |

Status: ingested 2026-10-18 by root. Also reloaded profile-selection-method.md, effort-selection-method.md, operational_devops.md, project_constitution.md and integrations-and-channels.md. verify_context.sh passed read-only (PACED-Ready). Preserve one product/runtime writer; no private file access before operator confirmation, no provider execution before separate GO.

## Agent Routing Preflight
- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Subagent / delegation authorization:** required by delphi-ai/main_instructions.md and todo-approval-gates-method; scoped executor after implementation approval only
- **Execution topology:** primary-checkout-single-writer
- **Worktree / auxiliary-checkout authorization:** not-authorized
- **Worktree authorization evidence:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

Execution tuple reconfirmed after APROVADO: artifacts/reviews/leadshug-meta-test-binding-20261018/routing-qualification-cp82.json returned go; normal authority guard is required before helper execution. Qualification and product execution remain distinct stages. Fresh architecture and critique reviewers use separate formal-review/gpt-6.1-sol/max routing receipts.

## Decision Adherence Validation
- **Status:** `not_run`
- **When required:** before delivery, against every frozen decision D-01 through D-06 after freeze.
- **Evidence:** no implementation exists.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)
- **Status:** `not_run`
- **When required:** before delivery, one-to-one against the module baseline snapshot.
- **Exception handling:** any conflict returns to decision review; parent ST-CON-01 is not silently superseded.


Planning one-to-one comparison D-01..06 completed in artifacts/reviews/leadshug-meta-test-binding-20261018/module-consistency-planning-v1.json. Explicitly extend only authorization entry/provenance after later approval; shared contracts preserved. Delivery comparison and module consolidation remain not_run.

## Pipeline/Copilot P1/P2 Preflight
- **Status:** `not_run`
- **Required before delivery:** inspect actual pipeline and review findings for this bounded diff; do not claim P1/P2 clearance in planning.
- **Evidence:** pending implementation branch.

## Rule-Spirit Anti-Pattern Hunt
- **Status:** `not_run`
- **Focus:** fake OAuth, global token fallback, direct DB seeding, public dev endpoints, weakened grant validation, client-supplied credential, missing owner/phone fences, or secret leakage.
- **Evidence:** pending implementation.

## Promotion Finding Routing Ledger

No promotion or delivery findings exist; delivery review is not_run. Planning findings are recorded in the dedicated resolution ledger.

## TODO Closeout Disposition
- **Disposition:** `keep-active`
- **Disposition reason:** staged implementation approved; qualification did not establish eligibility, so product implementation is blocked and design must be revisited.
- **Post-commit/push status:** `pending`
- **Next path/status action:** keep active/Pending+Blocked; return to authorization design with the safe qualification receipt. No source edits, retry or new provider diagnostics authorized by this result.

## Security Risk Assessment
- **Risk level:** `high`
- **Security review decision:** required
- **Why this risk level:** adds a new credential source and persisted trust transition in a multi-tenant messaging channel.
- **Attack surface in scope:** authenticated BFF, local configuration, Meta grant validation, database ownership/credential storage, browser response and webhook mapping.
- **Attack simulation decision:** `required`
- **Review evidence:** pending fresh security-adversarial review after implementation approval; no security pass claimed.
- **Residual security risk:** provider grant semantics and local config protection remain unknown.

## Performance & Concurrency Risk Assessment
- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** write races, leases, provider calls and credential promotion are in scope.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | medium | EPS-EXACT-LOOKUP-SURFACE-CHANGED | before_local_implemented | EPS-E1 | pending | provider budget unproven | U-QUERY-PATH-UNKNOWN |
| FRC | frontend-race-condition-validation | required | medium | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-POLICY | pending | lifecycle validation pending | U-ASYNC-SURFACE-UNKNOWN |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-DUPLICATE-SUBMIT-OR-REPLAY | before_local_implemented | BCI-INV | pending | overlapping confirmation/promotion unproven | U-WRITE-OVERLAP-UNKNOWN |
| RLS | runtime-load-stress-validation | not_needed | low | none | before_production_ready | RLS-E1 | not_applicable | no SLO, queue, bulk or cache change | none |

### Lane Detail Packet Template
#### EPS
- **Trigger rationale:** bounded exact resource/grant lookup and candidate staging; record latency/budget evidence if the query path changes.
- **Recorded at (UTC):** pending implementation review.
- **Executor ID:** pending.
- **Evidence object:** none; state is pending.
#### FRC
- **Trigger rationale:** wizard capability and submit/refresh flows can race or replay.
- **Recorded at (UTC):** pending implementation review.
- **Executor ID:** pending.
- **Evidence object:** none; state is pending.
#### BCI
- **Trigger rationale:** provider grant checks, currentAttempt, ownership claim, and promotion are concurrent and externally side-effecting.
- **Recorded at (UTC):** pending implementation review.
- **Executor ID:** pending.
- **Evidence object:** none; state is pending.
#### RLS
- **Trigger rationale:** no high-volume queue, bulk, realtime, or SLO change is proposed.
- **Recorded at (UTC):** n/a.
- **Executor ID:** n/a.
- **Evidence object:** not applicable.

## Verification Debt Assessment
- **Audit decision:** required
- **Audit outcome:** `pending`
- **Why this outcome:** no implementation exists to audit.
- **Inline code TODO debt:** `none known`
- **Evidence / audit artifact:** not run.
- **Accepted residual debt:** grant compatibility is a mandatory staged execution prerequisite before product edits, not waived or accepted debt.

## Independent Test Quality Audit Gate
- **Audit decision:** `required`
- **Why this decision:** new behavior, schema, auth, race cases, and critical channel journey.
- **Trigger signals in scope:** `changed test logic|behavior-defining change|architectural change|shared contract/api/schema|critical-user-journey|non-trivial validation risk`
- **Required evidence matrix:** `unit|integration|web real-backend`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen baseline, scope, implementation/test diff, behavior evidence, residual risks.
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** fresh internal no-context reviewer.
- **Internal reviewer mandate:** required after implementation and before delivery.
- **Gate-satisfying evidence expectation:** fresh internal no-context audit; wait for terminal reviewer result.
- **Audit focus:** product/test delta, fail-first alignment, bypass detection, assertion efficacy, real backend/browser coverage, race and redaction checks.
- **Required applicable evidence:** framing, fail-first, bypass scan, PostgreSQL integration, browser flow, issue cards, uncertainty and decision adherence.
- **Audit status:** `not_run`
- **Findings summary:** no audit run.
- **Resolution ledger:** no findings yet.
- **Evidence / reference:** pending implementation.
- **Waiver authority / reference:** `n/a`

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| none | n/a | n/a | n/a | none | n/a | no findings exist |

## Independent No-Context Final Review Gate
- **Final review decision:** `required`
- **Why this decision:** cross-stack auth/persistence and critical user journey.
- **Impact signals in scope:** `cross-module blast radius|public contract/schema/api|auth/payment|critical-user-journey`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen baseline, approved scope, bounded diff, adherence, validation index, TQA evidence, residual risks and verification debt.
- **Review isolation mode:** fresh internal no-context reviewer.
- **Internal reviewer mandate:** required; not yet dispatched.
- **Canonical multi-lane audit protocol:** `audit-protocol-triple-review`
- **Audit session / round evidence:** pending delivery review dispatch.
- **Review focus:** adherence, regressions, evidence, test audit, security, performance, elegance and structural soundness.
- **Final review status:** `not_run`
- **Findings summary:** no final review run.
- **Resolution ledger:** no findings yet.
- **Evidence / reference:** pending implementation and reviews.
- **Waiver authority / reference:** `n/a`

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| none | n/a | n/a | n/a | none | n/a | no findings exist |

## Independent Cutover Integrity Audit Gate
- **Cutover audit decision:** `recommended`
- **Why this decision:** there is no legacy cutover, but the local exception must not become a hidden fallback bridge.
- **Cutover signals in scope:** `compatibility exception`
- **Package mode:** `bounded-file-set`
- **Canonical multi-lane audit protocol:** `audit-protocol-triple-review`
- **Audit session / round evidence:** pending cutover review dispatch.
- **Audit focus:** explicit opt-in boundary, disable/removal behavior, and absence of hidden global credential use.
- **Cutover audit status:** `not_run`
- **Findings summary:** no audit run.
- **Resolution ledger:** no findings yet.
- **Evidence / reference:** pending implementation review.
- **Waiver authority / reference:** `n/a`

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| none | n/a | n/a | n/a | none | n/a | no findings exist |

## Delivery Confidence Gate
- [ ] Lane promotion evidence complete: pending; no delivery claim.
- [ ] Runtime impact classified: `medium`
- [ ] Every `pcv-1` lane with production-ready deadline is gate-satisfying: `no`
- [ ] Any waived lane carried forward has owner/expiry/mitigation/follow-up: `no waivers`
- [ ] Operational checks run: pending implementation; migration and local smoke will be required.
- [ ] Lane artifacts recorded and hashed: pending.
- [ ] Confidence stated: `low`; grant compatibility and implementation are unproven.
- [ ] Release readiness outcome: `not_ready`

## Module Consolidation Gate
- [ ] Stable concept and final decision added to the integrations-and-channels module.
- [ ] Module decision ledger links to this child TODO.
- [ ] Existing OAuth/tenant/credential decisions preserved or explicitly superseded.
- [ ] No superseded tactical note remains without a canonical link.
- [ ] Parent/child paths and status cross-links reconciled by root.

## Commands (Run Locally)
- No implementation commands are authorized in this planning handoff.
- After explicit implementation approval, use the canonical local runner: `bash scripts/test-channels-local.sh api` and `bash scripts/test-channels-local.sh web`.
- Use scoped profile and audit guards only after the review baseline freeze; record actual output, never mark planned checks passed.

## Files Expected (Compatibility Note)
Use the Diff Expectation Contract as the authoritative inventory. The expected source/schema/UI/test/config paths above are candidates for a later approved implementation; no implementation files are changed by this planning handoff.

## Approval Boundary
Explicit staged implementation APROVADO has been recorded for the exact published plan. Keep Pending until implementation evidence passes. First prepare/review the helper and obtain normal authority GO; then one bounded read-only qualification under its consumed-once live GO. Product-source edits are forbidden until qualified and a separate root code GO is issued. Other excluded surfaces remain excluded.

## Planning Finding Resolutions — CP81

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-QUAL-01 | Integrated | useful | partial | project | none | Complete helper input/delivery/freshness/method/budget/result contract; validity is Meta is_valid through current adapter, token class/explicit lifetime unknown. Reuses current validator; failed qualification stops. Fresh critique still required. |
| ARCH-DOC-02 | Integrated | useful | no | none | none | One D-01..06 set, all decisions included in later adherence. |
| ARCH-TEST-03 | Integrated | useful | partial | project | none | V-06 and evidence matrix name post-promotion disable with unchanged active envelope/identity and normal stored-credential operations. |

CRIT-MIG-01 Integrated (optional): within existing V-01/V-03, use a pre-change official attempt/requestHash, apply provenance migration, and replay equivalent Embedded Signup input. Assert same attempt and expected same-session nonce semantics; a LOCAL_TEST method change on that key must still fail. NAO_OFICIAL remains null. This is a concrete migration/idempotency regression oracle, not authorization for a compatibility framework or unrelated hash rewrite. Fresh critique considered it non-blocking under the existing frozen behavior.

## Planning Readiness Summary — CP81

- Architecture raw v1 revise retained unchanged; ARCH-QUAL-01 Integrated and explicitly confirmed resolved by fresh critique. Two optional architecture notes integrated.
- Fresh critique v1 approve, zero material blockers; optional CRIT-MIG-01 concretizes V-01/V-03 without a new behavior or compatibility framework.
- Final baseline f35d1a0d pushed; exact reviewed scope equivalence across all23materialsections is recorded. Format-only enum/table/source-citation corrections did not require a new reviewer round and are not a waiver.
- Code coherence v3 go checks A-01..04; scope drift v3 go checks23sections/zerochanged; structural v3 PASS; authority preflight v3 preflight-go with execution_authority_granted=false. Earlier negative/partial guard evidence is preserved and superseded explicitly, never overwritten.
- Evidence: artifacts/reviews/leadshug-meta-test-binding-20261018/root-planning-ready-for-approval.json.
- No implementation approval, credential qualification, product build/test, runtime/provider/DB action, physical send, source push or Railway deployment occurred in CP81. Parent Pending/VAL05 open and unwaived.
- On later APROVADO, scope is the exact local-only staged plan above; failed/inconclusive real grant qualification stops before product edits. Rules/workflows named in Rules Acknowledgement must be reloaded; the preflight never substitutes for normal authority GO.

## Execution Checkpoint CP82 — Approval and Qualification Preparation

- User APROVADO recorded on 2026-10-18 for published plan 7f478ee3; no material behavior, decision or validation relaxation.
- Operational/DevOps qualification preparation; scopes nestjs, react, vite, prisma, postgresql, docker. Coder handoff remains conditional on qualified grant.
- Helper preparation only under ignored artifacts/tmp/number-onboarding-execution/. No product edits, private input reads, provider calls, DB or runtime changes performed at this checkpoint. Structural validation v2 PASS supersedes v1: metadata work-state enum corrected from execution to implementation; no scope change.
- Operator confirmed the three requested META_LOCAL_TEST_ACCESS_TOKEN, META_LOCAL_TEST_WABA_ID and META_LOCAL_TEST_PHONE_NUMBER_ID fields saved locally. No values collected in chat; no private read before the distinct live GO. Incidental IDE selection is not an input.
- Parent Pending and VAL05 open/unwaived.

## CP82 — Qualification Outcome / Stop Before Product

- Human confirmed the three named local fields saved; values stayed local. Frozen v4 helper and invocation reviewed independently: approve, zero blockers. Root verified all seven public hashes.
- Offline evidence: 13 checks exercise the actual pinned compiled adapter with fake fetch; 15 launcher checks passed and were independently rerun. All preparation findings integrated, including CP82-TIME-01 absolute remote deadline.
- Distinct root GO issued and atomically consumed once. Real result: rejected_or_inconclusive, adapterFresh=true, currentGrantAndTargetAccepted=false, canonicalPhoneUsable=false; fixed combined error GRANT_OR_TARGET_REJECTED_OR_INCONCLUSIVE.
- This does not identify a provider cause, prove the telephone invalid, or establish token class/explicit expiry. Delivery not tested. The result is a hard stop under D-01 and ARCH-QUAL-01.
- No retry, provider write, database access, Nest bootstrap, product source change, source build/push, tunnel change or Railway action. No product code GO issued. Parent Pending/VAL05 remains open and unwaived.
- Evidence: artifacts/reviews/leadshug-meta-test-binding-20261018/helper-review-v4.raw.json; qualification-preparation-cp82.json; qualification-live-go-cp82.json; qualification-live-result-cp82.json; root-qualification-outcome-cp82.json.
