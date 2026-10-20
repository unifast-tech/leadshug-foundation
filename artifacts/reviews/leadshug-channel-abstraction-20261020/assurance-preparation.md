# ST-CON-06 — delivery audit framing

Derived preparation only. This document does not close a gate. The final frozen `all`, independent review dispositions, PCV evidence and post-publication operator proof must be attached separately.

## Scope and topology

Big architectural delivery on NestJS11, Prisma6/PostgreSQL16, React18/Vite5 and Docker. The approved scope is a common text Channel port, operation-scoped concrete adapters and one outbound orchestrator for existing BFF/public/Typebot senders. No new network, schema, template, first-send intent, durable outbox, external retry, lifecycle rewrite or production deployment is authorized. Current physical channel origins remain storage provenance; the opaque-recipient fake does not establish a new persisted network.

Canonical validation is `bash scripts/test-channels-local.sh all`, on the principal checkout through Windows Docker, disposable namespace `leadshug_channels_validation`, Node22.23.3/PG16, API3100/provider-double3101/Web4173. Both manifests and exact scripts are inventoried in `evidence/capability-manifest-inventory.json`. Runtime provider boundaries use controlled doubles; HTTP-client tests assert raw fetch envelopes. PostgreSQL/DI/BFF/public endpoints and browser-served production bundles are real. External WhatsApp delivery requires operator proof after local activation and cannot be inferred from these doubles.

## Mandatory audit workload

The independent Test Quality lane must apply the complete `test-quality-audit` skill and `independent-test-quality-audit-method`, with Architecture/Code Quality/Tests/Performance/Security framing. Answer all five audit questions and assess fail-first alignment, bypasses/fallbacks, DI token/scope parity, exact commands and CI/platform parity, mutation outcomes/negative states, fixture ownership, async overlap, source/bundle freshness, decision adherence and residual verification debt. Issue cards are required for material findings. A short five-answer response alone is insufficient. No product test endpoint, silent live/mock fallback, weakened assertion, flaky-required-gate acceptance or provider-only success may substantiate a broader claim.

Performance must inspect actual metadata batching and bounded indexed latest-IN projection, rather than treating a test count as query evidence. Cutover Integrity must verify that all current senders consume the canonical abstract port and sole keyed MessageAcceptance writer, without an old-dispatch wrapper, parallel completion writer or query-time compatibility stitching. Approved legacy HTTP error codes are response compatibility, not proof of definitive rejection. Source assertions and exact negative probes must establish the distinction.

## Fail-first and remediation history

The positive-inventory runner repair preceded every product test. Recorded initial RED is narrowly the dependency guard:175unit passed/one failed because legacy direct provider dispatch remained. This is not blanket pre-implementation RED for every new behavior. Most added classifier, PostgreSQL barrier and browser cases were expanded during implementation. Review-remediation regressions were test-after; do not relabel them test-first. The independent auditor must judge whether the final assertions would expose the targeted failure and explicitly disposition any retrofit risk, preserving this historical limitation.

Round1 architecture/security findings and their complete adjudication are in `implementation-round-1-resolution.md` and `evidence/{adherence,security}.raw.json`. R01/R03 are classifier defects, R02 is an ineffective browser scenario and R04 is missing adversarial evidence. Round2 is now recorded separately in `implementation-round-2-resolution.md`: original R01/R03 counterexamples corrected, new R05 false-success contradiction and remaining R02/R04 protection gaps open. R05 has actual canonical API49493 RED before the correction. Do not project that RED onto earlier test-after work. No waiver/debt or architecture expansion is granted. Earlier failed runs remain historical failures; passing all33610 is an earlier candidate invalidated for delivery by the round2 findings.

## Bounded static scan triage

Canonical `test_quality_audit.sh` was executed with16 explicit public test/support paths from the source inventory before the final R02 assertion and round2 remediation; it must be refreshed for final TQA. No generic root walk or Git status discovery was used. Full historical output: `evidence/test-quality-static-scan.txt`. Exit2 reports heuristic medium signals and is not suppressed or represented as a clean scan.

| Signal | Count | Preliminary owner assessment; independent challenge still required |
|---|---:|---|
| Hard skip/focus bypass | 0 | No matching committed skip/only marker in selected paths |
| Test-support route marker | 0 | Fixture audit is hosted only by disposable provider fixture server3101 and limited to seeded conversations; verify source, absence of this marker alone is not sufficient |
| Authentication shortcut | 0 | BFF tests use real signup/login/session middleware; API-key tests use issued scoped keys |
| Status assertion hint | 11 | Context also asserts IDs, tenant/provenance, counts, outcomes, drafts or fixed content; reviewer must confirm each surrounding assertion rather than demand removal of useful HTTP checks |
| Ambient subject fallback hint | 1 | `timeline-freshness.ts` reads `rows[0]?.count` from a single aggregate migration count; it does not select an ambient business subject |
| Other detected DI/mock/fallback/no-exception hints | 0 | Pattern scan is incomplete by design; manual review of Nest provider overrides, HTTP doubles, fixture routes and browser interception remains mandatory |

## Required proof boundaries

| Boundary | Required evidence | Explicit limit |
|---|---|---|
| Channel substitution | Independent opaque-recipient fake through registry, real resolver/BFF/PG; no concrete provider calls | No new real network/schema/ingress claim |
| Credentials/tenant ownership | Valid foreign session denial, CSRF denial, foreign scoped API-key mutation denial; two tenants concurrently using distinct sealed token/resource pairs and tenant-local persistence | Disposable credentials only; no attack on external systems |
| Before/after dispatch fences | Generation/epoch/version changes before single POST; actual reauthorization race separately from post-dispatch version-only reseal | Local-check-to-network race remains; no atomic external fence |
| Raw HTTP outcomes | Stable Meta refusal allowlist; malformed/contradictory/timeout/redirect uncertainty; supported ACK-without-ID contrasted with arbitrary2xx object | Accepted ID is provider acknowledgement, not handset delivery |
| Local completion/echo/claim | Sole acceptance keyed writer, sender/echo convergence, concurrent claims, incomplete local persistence/finalization after ACK and bounded readback | No crash recovery or unknown-ID deduplication guarantee |
| Human/public selection/bot policy | Deterministic latest origin, sole/zero/multi binding; pinned accepted bot ingress and window expiry | Current latest-IN stored-time algorithm/no transport filter preserved for ST-CON-04 |
| Inbox mutation/lifecycle | Real BFF/PG served bundle, accepted/unknown, unavailable/ambiguous composer; A→B→A late response with a newly edited draft;5waves×20 pending-send retriggers | Required final browser/all must bind exact source/bundle; serial accepted sends alone are not race proof |
| Query/load | Representative deep histories, actual query-log/explain;5×20 overlapping outbound operations, distinct-conversation scope stated | No SLO/capacity, same-key exactly-once or cross-tenant claim from this one batch |
| External resources | New post-activation operator IN/OUT on both existing official and QR bindings | CP108 and previous green tests are historical and cannot close this new runtime proof |

Required platforms: API unit/HTTP/real-PG, Web unit/build, Chromium served-bundle, then assisted official/unofficial WhatsApp. Mobile/native, Laravel/Flutter and Railway deployment are not claimed. Architectural baseline and exact D01..10 remain those of the approved TODO. The producer/consumer matrix in the audit package must distinguish implemented consumers from evidence still pending; no new waiver is inferred.
