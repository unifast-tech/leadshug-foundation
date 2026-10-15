# ST-ATT-01 complete bounded delta audit, generation3
Fresh internal no-context review of fixes and refreshed evidence. Review all applicable adherence/test-quality axes; the full generation1 audits are embedded and remain context, not a waiver. Contract and scopes unchanged. Initial package SHA0b106804c789463057279df728e33635711244d4ca76dbf868b6427619cd5cd4. Original reviews both completed/merged before this new package; no live review was shortened or replaced. Product code remains one writer in primary checkout. API source invariant permits reuse of API224/EPS/BCI/RLS; new raw API CI leaf results remove prior retention debt. No deployment or remote CI claim.

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-adherence-round-1.json
```
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-adherence-dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "delivery-adherence-native",
  "findings": [
    {
      "finding_id": "ARCH-DEL-01",
      "severity": "medium",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "[P2] Dirty events automatically renew the three-page recovery budget",
      "rationale": "web-app/src/telas/Inbox.tsx:99 allocates three queries for every executarRecuperacao invocation. When an event arrives during traversal, :159 resets the cursor, and :177 immediately queues another invocation with a fresh budget. A round that has consumed its three queries can therefore issue another three page requests without Continue or polling. Repeated arrivals can sustain this cycle and repeatedly discard traversal progress. This diverges from the frozen requirement that a new event must not renew the round's budget. The strong browser case exercises this dirty path but asserts neither request count nor maximum concurrent recovery requests, so its green result does not establish the advertised budget protection.",
      "suggested_action": "Fix within this TODO. A, recommended: share the remaining budget across traversal and coalesced passes, retaining pending T and required restart state when the budget reaches zero. B: defer the dirty pass to the existing Continue/poll entry points after the current budget is exhausted. C: retain immediate budget renewal, which fails the approved contract. Add deterministic request-count and single-flight assertions, including events arriving after the third request; refresh the FRC evidence.",
      "affected_paths": [
        "web-app/src/telas/Inbox.tsx",
        "web-app/e2e/timeline.spec.ts",
        "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-frc.json"
      ]
    },
    {
      "finding_id": "ARCH-DEL-02",
      "severity": "medium",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "[P2] Empty-thread recovery loses notifications received between rounds",
      "rationale": "For a recovery created with vazio=true, web-app/src/telas/Inbox.tsx:204 deliberately leaves an existing cursor unchanged when a notification arrives while recovery is paused. The subsequent invocation snapshots the already-incremented event counter at :97 and clears dirty at :98. Because the cursor is non-null, :103 skips the recent-page read and continues older pages. On exhaustion, :128 can clear recovery without ever fetching the triggering new head. For example, open an empty thread, receive more than 150 messages, pause after three pages, then receive another message or complete a send. The continuation can declare coverage complete while omitting that message and retaining old metadata. The existing empty-thread test uses 131 messages, which fits one round and cannot expose this transition.",
      "suggested_action": "A, recommended: retain a restart-needed marker until a recent-page pass has incorporated notifications received between rounds, and require that work to finish before clearing pending coverage. B: share the same dirty-event accounting between empty and non-empty recovery branches while preserving their approved behavior. C: leave the notification discarded, which violates recovery continuity. Add a real-backend browser regression with an initially empty thread, more than three pages, and a notification or send between rounds; compare complete IDs and current metadata before accepting completion.",
      "affected_paths": [
        "web-app/src/telas/Inbox.tsx",
        "web-app/e2e/timeline.spec.ts"
      ]
    },
    {
      "finding_id": "ARCH-DEL-03",
      "severity": "medium",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "[P2] Opening a thread drops message and connection notifications",
      "rationale": "web-app/src/telas/Inbox.tsx:258 clears threadAtual while the initial request is pending. Message and connection callbacks invoke reconciliar, but :187 returns immediately when that thread is absent and records no pending work. If the initial GET has read its page, its real response is delayed, and an incoming message or reconnection occurs before delivery, that notification is discarded. Opening then installs the older response at :269 and only reloads the conversation list at :271. The selected thread remains stale until another trigger, ordinarily the 60-second poll. This leaves an uncovered opening transition in the approved message/connection recovery contract. The delayed-opening test checks loading presentation without an overlapping notification.",
      "suggested_action": "A, recommended: record recovery notifications against the opening conversation/generation and reconcile read-neutrally once its initial page is installed. B: coalesce an invalidated opening read into a subsequent read-neutral refresh with the same context and budget protections. C: rely solely on a later poll, leaving the required notification unhandled. Extend the delayed real-response browser test with an incoming message and a connection callback during opening; require recovery without another event or clock advancement and verify unread preservation.",
      "affected_paths": [
        "web-app/src/telas/Inbox.tsx",
        "web-app/e2e/timeline.spec.ts"
      ]
    }
  ],
  "overall_assessment": "Return for corrections in the current approved TODO. The delivered API follows the frozen architecture, and the principal non-empty recovery case preserves original T across H>T and dirty traversal. Three additional recovery transitions diverge from the approved protections. These are current implementation findings; they do not reopen the resolved planning findings merely because those findings were previously reported.\n\nDecision mapping: authorization precedes pagination validation and cursor resolution; cursor anchors remain scoped to the authorized conversation; limits/defaults, versioned cursors, strict createdAt/id ordering and N+1 reads are implemented. Human opening performs one atomic unread reset before the page SELECT; background and cursor reads remain neutral. Backfill merges by ID and does not apply historical metadata. Conversation/BU generation checks protect delayed responses and draft effects. The historical cursor and recovery cursor are separate in normal recovery. Public API, Consultar, incoming processing and other excluded stories retain their delivered boundaries. No temporary compatibility exception or production fetch-all fallback is shown. Recovery budget and notification accounting are Exceptions until ARCH-DEL-01..03 are resolved.\n\nArchitecture, code quality and elegance: the controller remains thin, persistence stays in the existing Prisma-backed domain service, and no unnecessary provider exports, scopes, cache framework or production test flags were introduced. The active-thread owner and merge helpers fit the approved design. The duplicated empty/non-empty recovery paths and locally reset scheduling state nevertheless create inconsistent transitions. A focused repair to this owner is appropriate; the evidence does not require changing the approved architecture.\n\nTest alignment, efficacy, efficiency and sufficiency: the supplied logs report API 115 unit tests by attestation and 224 PostgreSQL tests, Web 20 unit tests, 31 browser tests, and three repetitions of the strong recovery case. Full ID comparisons, persisted authorship, unread readback, scope negatives and relative scroll-anchor assertions substantiate the covered behaviors. Status hints are paired with business assertions; the migration COUNT aggregate is not ambient fixture selection. The weak 0..10 concurrency assertion is supplementary: the deterministic SELECT barrier and its failing negative control provide the discriminating ACK protection. Repeating the strong overlap case adds useful evidence efficiently. However, neither three-query enforcement nor the two notification transitions above has an adequate protection harness. Recovery-specific failure/retry coverage is also less direct than the demonstrated backfill retry coverage.\n\nWorkaround and retrofit assessment: implementation is honestly described as test-after. The BCI mutation fails with expected10/received0, restoration is byte-exact in the supplied evidence, and the canonical case subsequently passes. No earlier TDD execution is inferred for pagination or frontend recovery. The 251-ID and late-tie oracles meaningfully target the approved behavior, but successful final-state equality alone cannot establish scheduling bounds. No committed skip/focus marker or required-boundary mock fallback appears in the supplied changed tests; skips in the targeted BCI log result from test selection. Fixtures own their proof subjects. The pre-existing mocked Typebot browser scenario remains outside this story's integration claim.\n\nWiring, security and runtime provenance: the test bootstrap imports the real AppModule and replaces the Meta/Evolution output tokens, preserving real session, grant, domain, PostgreSQL and WebSocket behavior for the timeline. Fixture routes are isolated in test support, with explicit disposable-database checks. Distinct authorized-conversation, same-tenant BU, cross-tenant and unauthenticated negatives support the scoped authorization contract. No new tenant escape is demonstrated. Socket cleanup and late callbacks have unit coverage; browser cases cover conversation/BU switches, draft edits and backfill/close overlap. Node22, pre-worker attestations, matching recorded source manifests and served-JS/dist fingerprints support the local runtime claim. API generate/lint/build/unit stdout was not retained, so those leaf results have executor-attestation support rather than independently inspectable raw output. This review assessed embedded evidence without executing tools or independently recalculating hashes.\n\nPerformance and PCV: EPS supplies representative recent, deep and tied plans, including the deep scan residual. Rejecting the measured composite-index candidate is consistent with the conditional index decision; the contract does not mandate an index despite worse measured results. BCI supplies the required invariant and deterministic 10-operation, three-batch overlap profile. RLS supplies one stage, fixed correctness thresholds and measured latency, without a production capacity or SLO claim. Those evidence floors are supported on their face. FRC exercises 10 real pushes across three repetitions, but its adherence conclusion remains open because the stated budget protection is contradicted by source and the notification transitions are uncovered.\n\nOperational fit and governance: the React owning script npm run test:tela builds and runs source-owned Playwright against the real validation backend. Mapping run_web_navigation_smoke to that script faithfully satisfies the project contract; no Flutter execution or waiver is needed or demonstrated. CI-equivalent claims are appropriately limited to the declared API/Web leaf jobs, with PostgreSQL/browser checks identified as additional local validation. Loopback/test identities and the unchanged HTML detector justify the supplied scanner triage. The TODO correctly remains Pending/review with delivery gates open; the package does not establish completion, remote CI, deployment or production readiness.",
  "recommended_path": "Keep the approved architecture and resolve ARCH-DEL-01..03 in this TODO before accepting delivery adherence or promoting FRC to passed. Preserve pending T, distinct cursor ownership, read neutrality and generation checks while correcting budget and notification accounting. Add deterministic regressions for query budget/single-flight, an empty recovery spanning multiple rounds with a between-round notification, and a notification during initial opening. Validate complete IDs, metadata, pending-state transitions and unread readback. Rebuild and rerun affected Web unit/browser suites and the FRC repetitions against the declared Node22/real-backend/disposable-PostgreSQL topology, then bind refreshed evidence to the changed source. Retain unchanged API evidence where source identity remains established. Record the findings and dispositions in the current TODO, obtain a bounded adherence delta review, and complete the separate TQA, security, verification-debt, final-review and closeout gates before claiming completion. Renewed architecture approval is unnecessary for repairs that implement the existing frozen contract.",
  "performance_position": "mixed",
  "elegance_position": "mixed",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed"
}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/delivery-tqa-round-1.json
```
{"schema_version":"subagent-review-result-v1","artifact_kind":"subagent_review_result","dispatch_path":"/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-tqa-dispatch.json","review_kind":"test_quality_audit","reviewer_label":"delivery-tqa-native","overall_assessment":"Test effectiveness is mixed. The package strongly aligns most tests to the approved contract: real Nest/session/grant/PostgreSQL paths, owned fixtures, distinct scope negatives, complete ordered-ID readbacks, real browser/WebSocket flows, fresh served-bundle provenance, and external doubles limited to Meta/Evolution ports. The original-T scenario genuinely combines H>T, partial traversal, late tied UUID insertion, dirty events, and DB/UI ID comparison; the ACK barrier plus failing post-SELECT mutation is strong and honestly test-after rather than retroactive TDD. Status hints are paired with meaningful body/readback assertions, and no authoritative-run skip, focus marker, fake BFF payload, ambient proof subject, or production test hook is evidenced. Test efficiency is acceptable: full project-owned API and browser commands are used, with targeted repeated FRC evidence rather than redundant broad reruns. Performance evidence is mixed: EPS measures representative recent/deep/tied paths and documents the no-index decision, but the deep predicate still filters 10,001 rows locally and establishes no production capacity claim. Operational provenance is otherwise sound (Node 22, disposable PG, source manifests, fresh API/browser builds, served JS equals dist), although API generate/lint/build/unit raw stdout was not retained. The audit cannot pass yet because two explicit recovery/context invariants are asserted only indirectly or not at all.","recommended_path":"Return for focused test repair, not a design rewrite: make recovery page-call budget and single-flight behavior directly observable, then add destination-context assertions for stale draft/error/scroll effects. Rerun the full browser suite and repeated FRC case on the corrected test source. Preserve per-command API CI-equivalent raw logs or machine-readable results on the next authoritative run. Keep the documented EPS deep-scan residual explicit; it does not itself justify an unmeasured index change.","performance_position":"mixed","elegance_position":"acceptable","structural_soundness_position":"mixed","operational_fit_position":"acceptable","findings":[{"finding_id":"TQA-TL-01","severity":"medium","title":"Recovery tests do not directly prove the three-page round budget or single-flight invariant","rationale":"At web-app/e2e/timeline.spec.ts:108, :133, and :168, the pending banner and eventual full-ID equality only infer bounded recovery. With the 382-message setup, an implementation making more than three page requests can still remain pending before it reaches a timestamp below T, and parallel recoveries can deduplicate to the same final IDs. The tests do not count page GETs per round or prove that ten dirty events cannot start a second walk while the delayed walk is in flight. This leaves the approved maximum of three page queries per round and one in-flight pass unprotected.","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"timeline-recovery-observable-round-limits","affected_paths":["web-app/e2e/timeline.spec.ts"],"suggested_action":"Observe actual BFF page requests around a held real response: assert no more than three recovery page GETs before the pending state, and assert no second traversal starts while the held request remains in flight. Then release it, verify Continue/poll starts the next bounded round, and retain the existing full ordered-ID and unread readbacks."},{"finding_id":"TQA-TL-02","severity":"medium","title":"Context-switch race coverage omits target draft, stale-error, and stale-scroll assertions","rationale":"At web-app/e2e/timeline.spec.ts:333, the delayed-send test switches conversation and BU but releases the old response before placing any draft in the destination; it asserts selection, source persistence, and absence of the old bubble only. The delayed-backfill scroll test at :227 remains in the same context, while the same-context draft test at :260 does not exercise generation invalidation. A stale completion, failure, or delayed backfill callback that clears a destination draft, writes its error, or adjusts its scroll after a context switch could therefore pass despite the explicit contract requiring those effects to be ignored.","category":"tests","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"timeline-context-generation-observable-effects","affected_paths":["web-app/e2e/timeline.spec.ts"],"suggested_action":"Extend real-response race tests to switch context, type a destination draft, capture destination scroll/state, then release both prior success and failure/backfill responses. Assert the destination draft, error state, messages, metadata, and scroll remain unchanged for both conversation and BU changes."},{"finding_id":"TQA-EVID-03","severity":"low","title":"API CI-equivalent non-E2E command output is attested but not retained","rationale":"execution-evidence.md and executor-final-summary.json attest successful prisma generate, lint, build, and 115 API unit tests, but explicitly state that their raw stdout was not preserved. The retained E2E and browser logs are strong complementary evidence, but they do not independently demonstrate unit-test discovery or lint/build output for the frozen source.","category":"operational_fit","formalizable_hint":"yes","candidate_rule_level":"project","candidate_rule_id":"ci-equivalent-command-output-retention","affected_paths":["foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md","foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/executor-final-summary.json"],"suggested_action":"On the next authoritative run, retain immutable per-command stdout or machine-readable test reports with command, exit status, source manifest, and run identifier; keep the executor attestation as an index rather than the sole record."}]}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/executor-revision3-summary.json
```
{
  "task": "ST-ATT-01 inbox timeline pagination executor evidence",
  "capturedAtUtc": "2026-10-15T04:25:38.812920Z",
  "status": "revision 3 source frozen for independent review; no commit/push",
  "runtimeAndDatabase": {
    "node": "22.23.3",
    "postgres": "PostgreSQL 16.14",
    "database": "leadshug_timeline_20261014",
    "migrations": 17,
    "endpoint": "postgresql://timeline-postgres:5432/leadshug_timeline_20261014 (credentials redacted)",
    "disposable": true
  },
  "source": {
    "api": {
      "branch": "feature/inbox-timeline-pagination",
      "head": "5db3fbe2043428749895fc3ff6441e9457467dd0",
      "diffSha256": "d3d84c015c24348b1dbc885a90d66ff8f88eadf35a75b0a256a38c3f1230708b",
      "manifestSha256": "4722038d60e7b73ac3dc04d2adbbd7af9f2a71fda6d2f9f59c87214ca3d70125",
      "files": [
        {
          "path": "src/domain/inbox/conversations.service.ts",
          "sha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.spec.ts",
          "sha256": "a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.ts",
          "sha256": "d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af"
        },
        {
          "path": "src/surfaces/bff/conversations.controller.ts",
          "sha256": "0b5c46a78aafd8085b609ad711bcdb7626263094f434240f37b8700f20291565"
        },
        {
          "path": "test/atendimento.e2e-spec.ts",
          "sha256": "1bb4acb19fc522b397424b319ab04563e3608605dcfe307970eecdd0d464b5b8"
        },
        {
          "path": "test/browser-server.cjs",
          "sha256": "031e9d1e282603c098c4bb594fb13a08ab2bc2f301c9a3ebb5a6362cae6fe42b"
        },
        {
          "path": "test/timeline-fixtures.cjs",
          "sha256": "bc15f1758ec574dec1f1c66330e0cc9804705e103fb5abab7f9015e5e8563f9f"
        }
      ]
    },
    "web": {
      "branch": "feature/inbox-timeline-pagination",
      "head": "6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9",
      "diffSha256": "1101205003f78d9514a79ff38e846107bd224a50f73345d5fb166b8ec166b2c4",
      "manifestSha256": "3092a7c02dac4119e3a931ce6cf7b0ec750e8a1d4f1416b7f7973ef307a3353e",
      "files": [
        {
          "path": "e2e/timeline-freshness.ts",
          "sha256": "ad41153df34c53f6674325b72887e701259ba7a8e752afd38ff4cdd8728c4cd0"
        },
        {
          "path": "e2e/timeline.spec.ts",
          "sha256": "867c4de5d3a244923a185b935bd1bb149f342275949e285eb745f789c571cb82"
        },
        {
          "path": "playwright.config.ts",
          "sha256": "d69c084d15cfef29ad23851036cb90309c60aa7a7b16c6810e3ae9b0adbbdd98"
        },
        {
          "path": "src/api.ts",
          "sha256": "87ba36bd21518725ba0e42221030d77b723144ef8d0581fddb2d9102233e7db2"
        },
        {
          "path": "src/telas/Inbox.tsx",
          "sha256": "821ce011ce5738e40caeafa2c3fad20b9583053ce2373bb194abbeee567bc783"
        },
        {
          "path": "src/tempoReal.spec.ts",
          "sha256": "378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5"
        },
        {
          "path": "src/tempoReal.ts",
          "sha256": "118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf"
        },
        {
          "path": "src/timeline.test.ts",
          "sha256": "16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4"
        },
        {
          "path": "src/timeline.ts",
          "sha256": "0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311"
        }
      ]
    },
    "manifestRecheckAfterRuns": "all API and Web manifest entries match both immutable revision 3 final attestations and current source; zero mismatches",
    "gitDiffCheck": "passes with cr-at-eol whitespace configuration; project files use CRLF"
  },
  "buildFreshness": {
    "fullRunId": "web-authority-revision3-final-full-20261015",
    "capturedAtUtc": "2026-10-15T04:22:58.946Z",
    "frcRunId": "web-authority-revision3-final-frc3-20261015",
    "frcCapturedAtUtc": "2026-10-15T04:24:16.848Z",
    "apiHealth": 200,
    "fixtureHealth": 200,
    "preview": 200,
    "servedBundle": "/assets/index-DKhXhPnI.js",
    "servedBundleSha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e",
    "distBundleSha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e",
    "sameServedAssetForFrc": true,
    "fullAttestation": "attestation-browser-web-authority-revision3-final-full-20261015.json",
    "frcAttestation": "attestation-browser-web-authority-revision3-final-frc3-20261015.json",
    "attestationSha256": {
      "attestation-browser-web-authority-revision3-final-full-20261015.json": "94ceadbb83ef431eea7411cd28650d34626f196b5f344240c39ef294da20cc28",
      "attestation-browser-web-authority-revision3-final-frc3-20261015.json": "20e72c9376a276b6083d14688c4820b2f2169955ff28da152cd3cf82d4cd6716"
    }
  },
  "apiAuthority": {
    "command": "npm run prisma:generate && npm run lint && npm run build && npm test (API E2E remains the unchanged authoritative 224/224 run)",
    "exitCode": 0,
    "unitTests": {
      "files": 17,
      "passed": 115,
      "failed": 0,
      "stdoutPersisted": true,
      "log": "api-ci-light-revision2-20261015.log"
    },
    "e2e": {
      "files": 20,
      "passed": 224,
      "failed": 0,
      "durationSeconds": 111.92,
      "log": "api-e2e-authority.log",
      "sourceUnchanged": true
    },
    "runtimeLog": "api-runtime-authority.txt",
    "note": "Raw stdout retained for all four commands against unchanged API source; API E2E not repeated.",
    "revision2LightCommands": [
      {
        "command": "npm run prisma:generate",
        "exitCode": 0
      },
      {
        "command": "npm run lint",
        "exitCode": 0
      },
      {
        "command": "npm run build",
        "exitCode": 0
      },
      {
        "command": "npm test",
        "exitCode": 0,
        "files": 17,
        "passed": 115,
        "failed": 0
      }
    ],
    "revision2Log": "api-ci-light-revision2-20261015.log",
    "revision2LogSha256": "07f3536876fff3e4bf1e6e8caa39ed0215422b44daa6c52b138384b4797ef270"
  },
  "webAuthority": {
    "unit": {
      "command": "npm test",
      "exitCode": 0,
      "files": 3,
      "passed": 20,
      "failed": 0,
      "log": "web-authority-revision3-final-full-20261015.log"
    },
    "browser": {
      "command": "npm run test:tela",
      "exitCode": 0,
      "passed": 34,
      "failed": 0,
      "durationSeconds": 55.8,
      "log": "web-authority-revision3-final-full-20261015.log"
    },
    "frc": {
      "command": "npx playwright test e2e/timeline.spec.ts --grep=\"preserva o piso T\" --repeat-each=3",
      "exitCode": 0,
      "passed": 3,
      "failed": 0,
      "realWebhookTriggersPerRepeat": 10,
      "log": "web-authority-revision3-final-frc3-20261015.log"
    },
    "pollTargeted": {
      "command": "npx playwright test e2e/timeline.spec.ts --grep=\"poll retoma uma rodada pendente\"",
      "exitCode": 0,
      "passed": 1,
      "log": "web-poll-targeted.log"
    },
    "logoutTargeted": {
      "repeatEach": 5,
      "passed": 5,
      "exitCode": 0,
      "log": "web-logout-lifecycle-5x.log"
    },
    "revision2Targeted": {
      "archRecoveryRegressions": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"(abertura|thread vazia|piso T)\"",
        "exitCode": 0,
        "passed": 3,
        "log": "web-arch-targeted-second.log"
      },
      "contextRaces": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"troca de conversa e BU\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-context-revision2-target-20261015b.log"
      },
      "contextCoverage": "Both conversation and BU switches cover delayed old-send success, aborted old-send network failure, and delayed real backfill. Destination draft, error absence, IDs/messages, metadata, selection and scroll remain asserted."
    },
    "revision3Targeted": {
      "failedRecoveryBudget": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"falhas de recuperação consomem\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-revision3-failed-budget-target-20261015b.log"
      },
      "historicalCursorRestart": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"erro no cursor histórico\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-revision3-cursor-failure-target-20261015.log"
      },
      "contextRaces": {
        "command": "npx playwright test e2e/timeline.spec.ts --grep=\"troca de conversa e BU\"",
        "exitCode": 0,
        "passed": 1,
        "log": "web-context-revision2-target-20261015b.log"
      }
    }
  },
  "bci": {
    "fullApiE2eIncludesThreeRealPostgresBatches": true,
    "invariant": "10 unread increments after atomic ack while Message page SELECT waits on a lock; unread stays 10 before/after page; later real inbound makes 11",
    "negativeControl": "temporarily moved ack after findMany; targeted test failed expected 10 vs actual 0; restored exact saved bytes; canonical focused test passed",
    "negativeControlLog": "bci-mutation-control.log",
    "canonicalLog": "bci-canonical-after-mutation.log",
    "restoredServiceSha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
  },
  "eps": {
    "conversationRows": 20382,
    "largestEqualTimestampGroup": 1000,
    "recent": {
      "executionMs": 1.094,
      "sharedBuffersHit": 37
    },
    "deepCursorOffset": 10000,
    "deep": {
      "executionMs": 3.442,
      "sharedBuffersHit": 357,
      "rowsRemovedByFilter": 10001
    },
    "largeTieCursorOffset": 500,
    "largeTie": {
      "executionMs": 0.85,
      "sharedBuffersHit": 37,
      "rowsRemovedByFilter": 501
    },
    "candidateIndexTrial": {
      "index": "(conversation_id, created_at DESC, id DESC)",
      "executionMs": 3.942,
      "sharedBuffersHit": 9832,
      "rowsRemovedByFilter": 10001,
      "decision": "no index or migration; trial index removed; existing index retains deep scan residual"
    },
    "sql": "explain-timeline-exact.sql",
    "log": "explain-timeline-exact.log",
    "candidateSql": "explain-index-trial.sql",
    "candidateLog": "explain-index-trial.log"
  },
  "rlsReadSample": {
    "requests": 30,
    "concurrency": 5,
    "batches": 6,
    "status200": 30,
    "errors": 0,
    "messagesPerResponse": 50,
    "p50Ms": 23.36,
    "p95Ms": 64.26,
    "maxMs": 68.5,
    "foreignConversationWithMalformedLimitStatus": 404,
    "unreadBefore": 7,
    "unreadAfter": 7,
    "messagesBefore": 251,
    "messagesAfter": 251,
    "script": "rls-read-sample.mjs",
    "log": "rls-read-sample.log",
    "scopeNote": "foreign request used ?limite=invalid; raw JSON label says malformedCursor but malformed field is limite",
    "productionSloClaim": false
  },
  "historicalDiagnostics": {
    "invalidEarlierApiRun": "220/222 overlapped Browser cleanup/seed; not authoritative; later clean run 224/224 is authority",
    "earlierBrowserRun": "29/30 with initial WebSocket logout handshake issue; targeted logout 5/5 and final 31/31 pass after stable Inbox socket lifecycle",
    "incompleteFrcRepeat": "all-case repeat stopped at 20/30; not evidence; final strong FRC passed 3/3"
  },
  "cleanupAndResources": {
    "generatedWebTestResultsRemoved": true,
    "databaseContainer": "leadshug-timeline-postgres-20261014 remains running for reviewers",
    "dependencyVolumes": [
      "leadshug-timeline-api-node-modules-20261014",
      "leadshug-timeline-web-node-modules-20261014"
    ],
    "noOtherTimelineRunnerContainers": true,
    "sourceChangesFrozen": true,
    "disposableProbeRowsKeptForReview": true
  },
  "logSha256": {
    "api-ci-light-revision2-20261015.log": "07f3536876fff3e4bf1e6e8caa39ed0215422b44daa6c52b138384b4797ef270",
    "web-authority-revision2-full-20261015.log": "498b7e02295ddd70df9c64512a81d03d4bd535a5e53ad10fb2a8c107db1855de",
    "web-authority-revision2-frc3-20261015.log": "628acebdcfa9646cdca559ea5e69245479afb863e63b4dcf9ed273057e926dd7",
    "web-context-revision2-target-20261015a.log": "0974f0bd565563fd041f6faa070d42f0d664951732efff6a87b1a538bd05715d",
    "web-context-revision2-target-20261015b.log": "db388b4b9fdaa3cf0f740787f4ed16c7d7ebfd3563897e8b4021b383faf5e075",
    "web-arch-targeted-second.log": "d2e80466e2fab64303fc30b02aca1d1afdda483e8595907da7eeedb59bfd9dd2",
    "api-e2e-authority.log": "b508ca43e5157fea8fbf6951b2bd2b7c2b860ebde3e4c2dca1971094436317db",
    "web-poll-targeted.log": "14a49953f93214f078e30f4f449423a01fb2994188e8b60878b0b0580c8978df",
    "web-logout-lifecycle-5x.log": "4d21a8d1f11eba483a316fd5d15c4a1fc2c35ffca728433b9e00d7edb21a4047",
    "bci-mutation-control.log": "0c2b211c2078240a09519eeff76f2a32a358135090e32df1bb871c619d4e327d",
    "bci-canonical-after-mutation.log": "90fe5dd92cf6098fc7375258ba7452a29c4d74255d10fafd2efcc4c8b4866b4c",
    "explain-timeline-exact.sql": "30b7477601cd109ffd3af7d38e9df1e5fbf8a6af56bf90cf52a42f4779ee0cb8",
    "explain-timeline-exact.log": "6e346b5b0609de7f347481fb2b4eccc93e4ddf8b41219bb1348fbf169af9b9b6",
    "explain-index-trial.sql": "8ac4343ac0633b5b1535e171ec7466e58c5c6488d1de8abc516b15f6e6b914a3",
    "explain-index-trial.log": "43251847c09a71819a11aa135c8710b72a3eb4af2188f07bd3c071bfa980171c",
    "rls-read-sample.mjs": "d59fa9f53ffeb97aec02b32ccf91584868f1e2b1ebcd644278f00881ae3a3321",
    "rls-read-sample.log": "5b68b1b5f450153c7fa6c36c277aa19d5846860f63ef8124a1eaeb32dd3941fc",
    "web-authority-revision3-final-full-20261015.log": "db751c5b21cef3d774c7d2d0fa44cc373f879ae4c8c35abac65d085d63367e9c",
    "web-authority-revision3-final-frc3-20261015.log": "bf502bd2d032c2b2a37a50ccf6f2cb08e99dd86f756b20fc8355ede706148a1d",
    "web-revision3-failed-budget-target-20261015b.log": "5d02c39e207a6b10d06f56f6824e7db51e3a749359a6310f302a4e13c1e0a291",
    "web-revision3-cursor-failure-target-20261015.log": "c3ef437d10ab5c25d047ca67c7c5daa13bc33019c57ec02f402e62a84cb23f14",
    "web-revision3-budget-negative-control-20261015.log": "9ef570cf6e0e8829f2d24b705fd5a7184cb784f4317b81e7e56ec10f503b4646",
    "web-revision3-cursor-negative-control-20261015.log": "bcbadd84ee4327a619fd1b8d01c5530cf5de7bc6d5657d34b3b02c1a7dcf753e",
    "web-revision3-budget-negative-control-20261015.restore": "b6ddf0218fde28fb3013a6743a7bde0205c80e528ed3cef53f066dcca915e4b1",
    "web-revision3-cursor-negative-control-20261015.restore": "5f5606b3af229f362c6470fa1b3bd9c67d0ea5b2528d40508f156f5cebafc480"
  },
  "revision2Findings": {
    "ARCH-DEL-01": "One shared three-page budget spans the recovery traversal and dirty coalesced passes; the real late event during page three cannot renew it. The browser oracle checks exactly three recovery GETs, single-flight, and explicit Continue completion.",
    "ARCH-DEL-02": "An initially empty timeline with >150 persisted messages receives a real event between paused rounds; the restart marker survives until recent-head fetch and full ordered ID/unread readback pass.",
    "ARCH-DEL-03": "A real incoming event arrives while the opening GET response is held after fetch; installation performs read-neutral recovery without another event or clock advance, preserving unread.",
    "TQA-TL-02": "Context-race tests exercise success, network failure, and delayed backfill for both conversation and BU changes, after entering a destination draft and capturing destination metadata, IDs and scroll.",
    "testDevelopment": "Test-after implementation; no retroactive TDD claim.",
    "targetedRunClassification": "Initial context diagnostics exposed fixture-label and text-representation issues in the test harness. Those were corrected; the final targeted context run and the subsequent full 32-test browser run passed. These diagnostics did not establish a product regression."
  },
  "revision3Findings": {
    "ARCH-DEL-01": "Budget is debited immediately before dispatching each page GET, including attempts that fail. Real-network browser regression aborts three real recovery responses with an incoming event during each; verifies exactly 3 requests, single-flight 1, visible error/pending, no fourth request before Continue, then complete IDs and unread after Continue.",
    "ARCH-DEL-01NegativeControl": {
      "mutation": "Moved query debits from before await to after await, reproducing reviewed variant.",
      "result": "Targeted regression failed as expected: expected 3 recovery requests, received 5.",
      "exitCode": 1,
      "restore": "Inbox.tsx restored in finally; byte-exact restoration verified.",
      "restoreProof": "count=4; restoredBytesExact=True; sourceSha256=1af04dee7cad573fc4920cdac7ecb77ddd352200a7ff30dba450508a7f191521",
      "log": "web-revision3-budget-negative-control-20261015.log"
    },
    "ARCH-CURSOR-01": "On a failed historical cursor request, a concurrent dirty/event invalidation resets cursor to null so the next remaining-budget pass fetches recent head; failures without dirty events preserve cursor for retry.",
    "ARCH-CURSOR-01NegativeControl": {
      "mutation": "Temporarily removed dirty-error cursor reset.",
      "result": "Targeted regression failed as expected: expected 2 recent requests, received 1 with no later trigger.",
      "exitCode": 1,
      "restore": "Inbox.tsx restored in finally; byte-exact restoration verified.",
      "restoreProof": "restoredBytesExact=True; sourceSha256=821ce011ce5738e40caeafa2c3fad20b9583053ce2373bb194abbeee567bc783",
      "log": "web-revision3-cursor-negative-control-20261015.log"
    },
    "historicalCursorTarget": "Real tied-timestamp PostgreSQL history; hold real cursor-page response, emit real webhook while in flight, abort response, assert recent-head restart within remaining budget, Continue, then compare all ordered IDs and unread=2.",
    "testDevelopment": "Test-after implementation; no retroactive TDD claim.",
    "canonicalInboxSourceSha256": "821ce011ce5738e40caeafa2c3fad20b9583053ce2373bb194abbeee567bc783"
  }
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md
```
# Evidência de execução ST-ATT-01

Estado: geração1 revisada e geração2 histórica; geração3 corrige as variantes de falha de rede antes do delta independente. Provas Web abaixo são históricas até a renovação, gates de entrega abertos. Fonte de produto no checkout principal, branches locais `feature/inbox-timeline-pagination`, um único executor `/root/timeline_executor_resume`. Foundation permanece `main`.

## API

`artifacts/tmp/inbox-timeline-execution/api-e2e-authority.log`: execução serializada Linux Node22 sobre PostgreSQL16 descartável `leadshug-timeline-postgres-20261014`, DB `leadshug_timeline_20261014`, 17 migrations. Comandos próprios: `npm run prisma:generate`, `npm run lint`, `npm run build`, `npm test` (17 arquivos, 115 testes) e `npm run test:e2e` (20 arquivos, 224 testes, 111.92s). Todos exit0, conforme attestation do executor em evidence/executor-final-summary.json. O stdout detalhado de generate/lint/build/unit foi observado no executor e não foi preservado separadamente; o log E2E completo foi retido. Essa limitação é explícita para os auditores. Instalação `npm ci` pertence ao provisionamento do volume de dependências Linux; não foi substituída por módulos Windows.

A suite inclui paginação de 251 IDs, limite/cursor/read-state, isolamentos de conversa/BU/Mantenedora e precedência de autorização, regressões dos consumidores e concorrência. O teste forte de reconhecimento bloqueia o SELECT real no PostgreSQL e observa dez incrementos após ACK em três lotes; o contador permanece10 depois da resposta e uma entrada real posterior eleva a11.

Controle de regressão test-after: `bci-mutation-control.log` mostra falha quando o reconhecimento é temporariamente movido para depois da leitura (expected10/received0). `bci-source-restored.sha256` registra restauração exata da fonte; `bci-canonical-after-mutation.log` registra cenário canônico1/1 passando após restauração. Não houve commit da mutação e não se alega TDD anterior à implementação.

## Navegador

Suite própria `npm run test:tela`, Chromium Playwright1.62.1/Noble com Node22.23.3, backend Nest real e mesmo DB descartável. Somente portas Meta/Evolution são substituídas por adapters determinísticos; sessão, guards, grants, domínio, persistência e WebSocket são reais. Atrasos usam respostas BFF reais; erros de rede são aborts explícitos; acesso perdido remove grant de fixture. Nenhum endpoint de teste existe no entrypoint de produção.

A prova final usa `evidence/web-authority-final31.log`: **31/31**,48.6s,exit0, incluindo11 cenários próprios da timeline e20 regressões de telas. O build foi reconstruído pelos webServers do runner antes dos workers. `evidence/attestation-browser-full-final31-20261015.json`, capturada em **2026-10-15T03:39:29.661Z**, registra branch@HEAD, diff e hashes de todos os fontes novos/alterados, manifests API/dist e JS servido==dist SHA256 `549f99b15659969a0fed38a61c029c214b895093e98539a02861873b1b5139c8`. Todos os16 fontes registrados (API7/Web9) foram conferidos byte a byte após a suite, sem divergência. Validação em `http://127.0.0.1:4173` dentro do runner descartável, API3100 e fixtures3101; nenhuma URL operacional foi usada.

O teste de poll avança o relógio do navegador em60s, retoma recuperação maior que3 páginas sem clicar Continue e compara IDs completos/read-state. O socket permanece estável durante mudanças de filtro/BU, protege callbacks após cleanup e notificações onopen; logout targeted5/5 e suite completa passaram. Unidade Web20/20 em3 arquivos; `web-precheck-socket-fix.log` contém build/unit e a suite browser reconstrói o consumidor final. FRC final: evidence/web-frc-strong-final-3x.log,3/3 em22.7s; attestation imutável frc-strong-final-20261015 capturada antes dos workers, fonte e bundle idênticos ao full31,10 gatilhos reais por repetição mais o gatilho inicial,11 frames exigidos em cada uma. pcv-frc.json liga políticas por ação e provas.

## Medições e revisão

`evidence/explain-timeline-exact.sql/.log`:20382 mensagens e1000 no maior empate. Planos equivalentes à produção, com âncoras constantes resolvidas antes da medição: recente1.094ms, profundo3.442ms (10001 removidas pelo filtro), empate0.850ms. Candidato composto medido no DB descartável: profundo3.942ms e9832buffers contra357 existente; removido, nenhuma migration justificada. A primeira captura com subqueries OFFSET dentro do EXPLAIN foi diagnóstico de seleção de âncora e não é evidência autoritativa. O custo ainda cresce com a profundidade do predicado OR; as medições locais não estabelecem capacidade de produção.

`evidence/rls-read-sample.log/.mjs`: uma etapa,5 leituras concorrentes×6 lotes,30/30 respostas200 com50 mensagens, p50=23.36ms,p95=64.26ms,max=68.5ms, zero erros; unread7 e251 mensagens preservados. Query inválida em conversa estrangeira devolveu404. O campo raw com nome MalformedCursor representa `limite=invalid`, como documentado em pcv-rls.json; cursores reais são cobertos no E2E API. Limiar de correção/limite/read-neutral fixado no runner; latência é observada, sem SLO de produção.

PCV: EPS/BCI/RLS têm artefatos JSON canônicos com SHA; FRC final também consolidado. Todos permanecem running aguardando julgamento independente. Architecture adherence, TQA e final review são obrigatórios; pareceres de planejamento não satisfazem esses gates. TQA usará `gpt-5.6-terra/max` no runner interno nativo verificado, sem waiver.

## Execuções invalidadas

API/browser simultâneos no mesmo DB, tentativas Node24, execuções interrompidas e diagnósticos parciais não contam para entrega. Logs são retidos para causalidade; nenhuma saída parcial, retry ou correção de fixture é rotulada como suite completa green. Não há claim de CI remoto, deploy, promoção de código ou capacidade de produção.

## Limitações de metadados e mapeamento de runners

O resumo bruto do executor identifica incorretamente a primeira execução220/222 como sobreposta ao browser; aquela falhou por duas expectativas de fixture e foi corrigida. A execução223/223 foi a sobreposta e é inválida. A autoridade final é224/224 serializada. Esta correção de indexação preserva o resumo bruto, os resultados e os logs; nenhuma execução é reclassificada green.

O guard compartilhado todo_completion_guard possui detecção de runner Playwright com literais de Flutter. Neste projeto React, a capacidade `run_web_navigation_smoke` é satisfeita pelo owner `web-app/package.json`, script **npm run test:tela**, conforme constituição e test-surface-admission.md. O nome genérico nos registros representa esse mapeamento explícito; nenhum script/caminho Flutter foi invocado ou adicionado. A evidência continua sendo31 testes source-owned Playwright, backend real, DB exclusivo, build/served fingerprint e mutações em feature branch. Revisores devem julgar a equivalência e não presumir um comando inexistente.

## Revisão de entrega round1 e correções

Architecture adherence interno gpt-6.1-sol/max retornou3 achados P2: renovação indevida do budget por dirty, perda de evento entre rodadas de recuperação inicialmente vazia e descarte de notificação durante abertura. Ver delivery-adherence-round-1.json/merge. Classificados release-blocker no mesmo TODO, sem mudança de arquitetura/aprovação necessária. API/EPS/BCI/RLS permanecem suportados; evidência Web31/FRC3 descreve a geração anterior e será renovada para a correção. TQA ainda está executando contra aquele pacote completo e imutável; nenhuma revisão foi interrompida, substituída ou reduzida. Não há claim de entrega.

TQA interno gpt-5.6-terra/max também foi coletado/validado: delivery-tqa-round-1.json. O parecer integral cobre alinhamento, eficácia/eficiência, retrofit/test-after, DI, runner/frescor, asserts/readback, EPS/BCI/RLS e limites. Requer proteção direta do budget/single-flight e efeitos sobre o destino (draft/erro/scroll) após troca de conversa/BU; recomenda reter stdout CI API na próxima coleta. Todos os pontos serão resolvidos na geração2, mantendo o contrato original.

## Revisão2 e variante de falha de rede

Revisão2 passou API generate/lint/build/unit115 com stdout retido em api-ci-light-revision2-20261015.log; Webunit20/browser32 e FRC3 com novas attestations pré-workers e16hashes conferidos. A coleta de stdout resolve a lacuna TQA-EVID-03; erros anteriores do harness de contexto foram rótulo de BU e representação de texto, corrigidos sem mascarar asserts.

Antes de despachar o delta, inspeção identificou variante ARCH-DEL-01-ERR: o saldo compartilhado era debitado somente após await bem-sucedido. Falhas de rede durante dirty podiam gerar novas tentativas sem consumir saldo. A revisão3 debita no despacho e acrescenta barreira com três aborts+eventos, impedindo uma quarta chamada antes de Continue/poll. Revisão2 fica histórica até a prova revisada. Nenhuma revisão delta foi despachada contra essa fonte intermediária. API/EPS/BCI/RLS seguem com fontes idênticas, sem rerun desnecessário.

A mesma inspeção isolou uma segunda transição no caminho de erro: página histórica abortada com evento pendente podia retomar o cursor antigo e limpar dirty sem buscar a cabeça nova. A correção preserva restart recente quando a falha coincide com invalidação, mantendo piso T e saldo; falha sem evento mantém o cursor. O executor acrescenta regressão real específica antes do ciclo final. As primeiras coletas revision3 também são históricas após essa mudança, identificadas por runId distinto; a mutação negativa do débito pós-await falhou com3 esperadas/5 recebidas e a fonte foi restaurada byte a byte. Nenhuma revisão delta foi iniciada sobre essas fontes intermediárias.

## Scans da fonte congelada revision3

Scan rule-spirit executado somente sobre os16 fontes autorizados: API30 observações/15 loci e Web42/21, sem allowlist/supressão. Targets loopback e identidades .test pertencem às fixtures; regex HTML src/api.ts é preexistente, sem endpoint operacional. Triage atual está em scan-triage-api.json e scan-triage-web.json, raw completo em evidence/rule-spirit-final-*.json/.log.

O helper test-quality final retorna exit2/medium em ambos os repos por hints heurísticos: API1 status e Web13 status mais1 COUNT de migrations. Nenhum hard bypass, skip/focus, auth shortcut, no-exception-only, DI override ou mock/fallback foi detectado. Os status são etapas de setup/HTTP acompanhadas por conteúdo, persistência, IDs completos, metadados, unread e/ou efeito no destino; rows[0]?.count é resultado agregado de COUNT, não seleção de sujeito ambiente. Esta é classificação de suporte para a TQA independente; os logs raw exit2 permanecem íntegros.

## Prova atual congelada revision3-final

Autoridade Web atual: evidence/web-authority-revision3-final-full-20261015.log, exit0,20/20 unitários e34/34 Playwright em55.8s. FRC forte: evidence/web-authority-revision3-final-frc3-20261015.log,3/3 em22.5s,12frames reais/unread por repetição com10gatilhos repetidos mais abertura da recuperação e evento na terceira consulta. Atualizações automáticas daquela rodada limitadas a3requests, máximo1emvoo; Continue/poll autorizam novas rodadas. A recuperação de erro inclui tentativas abortadas no saldo e conserva restart recente após falha histórica+dirty.

Attestations capturadas ANTES dos workers em2026-10-15T04:22:58.946Z e04:24:16.848Z. Backend/preview/fixtures200,17migrations no DB descartável; bundle servido==dist SHA256 2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Root comparou os16 fontes atuais byte a byte às duas attestations; API7 também permanece idêntico à geração original que produziu224E2E. A API CI rev2 tem stdout completo dos quatro leafs e115unit; nenhuma repetição de224/SQL/RLS foi necessária.

Os dois controles negativos são diagnósticos separados: débito pós-await falha3esperadas/5requests; remoção da guarda restart no catch falha2esperadas/1recent. As duas fontes foram restauradas exatamente, cada .restore contém SHA. A prova atual inclui os dois testes canônicos no full34; não se reivindica TDD anterior. O primeiro target de falha de orçamento exigia por engano todo o histórico numa fixture sem empate; foi corrigido para o grupoT completo empatado, sem alterar o contrato de cobertura. Logs diagnósticos e runIds anteriores continuam distintos, sem serem apresentados como autoridade final.

FRC atual em pcv-frc.json substitui a observação antiga; pcv-frc-generation1.json preserva o payload histórico. Demais lanes PCV mantêm fontes e medições, ainda running até julgamento independente. Resumo completo: evidence/executor-revision3-summary.json. Não há runner ativo; saídas web/test-results removidas após os processos terminarem. Código congelado para delta; nenhuma publicação de produto autorizada ou realizada.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/test-surface-admission.md
```
# Admissão dos testes e significado da prova local

ST-ATT-01, 2026-10-14. Artefato derivado; não reivindica suites green antes dos relatórios de execução.

| Superfície | Owner / leaf command | Delta | Relação com CI / prova |
| --- | --- | --- | --- |
| API unit | api-app/package.json, `npm test` | parser/cursor e asserts scoped | CI API já usa este script; novos specs são descobertos por config própria sem wrapper divergente. |
| API real PostgreSQL | api-app/package.json, `npm run test:e2e` | contrato/paginação/neutralidade/overlap | Prova adicional obrigatória do TODO, script completo. Não há claim de inclusão no pipeline existente. |
| Web unit/build | web-app/package.json, `npm test` e `npm run build` | merge/piso/socket e consumidor tipado | CI Web já usa esses leaf commands; specs atuais pertencem à descoberta do runner. |
| Browser readonly/mutation | web-app/package.json, `npm run test:tela` | histórico/races/fixture/bootstrap/path correto | Suite completa adicional obrigatória. API Nest real, mesmo PG dedicado, provider fake somente nas portas externas. Não há claim de estágio remoto. |
| Runtime/bootstrap | playwright.config.ts, API test/browser-server.cjs e test/timeline-fixtures.cjs | rebuild/API path e recusa de DB não descartável | Test-only, fora de src/entrypoint de produção; fontes no checkout principal. Bundles construídos e prova de identidade do runtime exigidos. |

API e Web têm manifests donos auditados pelo node_capability_surface_audit, exit0, em artifacts/tmp/inbox-timeline-execution/api-capability-audit.json e web-capability-audit.json. Nenhum comando de aplicação foi executado por esse audit estático.

A CI-Equivalent deste recorte é limitada aos jobs API/Web tocados: install/lint/build/unit de API e install/build/unit de Web conforme .github/workflows/ci.yml. PostgreSQL e Playwright são validações locais adicionais, mais fortes e requeridas pelo TODO. Não declarar stage-full, pipeline remoto green ou promoção; não alterar .github, compose/env ou root gitlinks. API e Web estão em feature/inbox-timeline-pagination, não main, para provas de mutação.

Descoberta de testes usa os scripts/configs dos manifests. Fixtures e cleanup são executados no banco exclusivo leadshug_timeline_*, nunca herdados de ambiente operacional. Uma suite targeted permanece diagnóstico, e um teste adicionado depois de o processo carregar o arquivo exige resultado novo sobre a fonte consolidada. Os artefatos de execução devem registrar test-after/falhas observadas honestamente, evitando alegação retroativa de TDD.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/implementation-observations.md
```
# Observações preliminares da implementação

Inspeção de suporte do orquestrador em 2026-10-14/15, durante implementação e validação; revisão independente permanece um gate separado. Nenhuma conclusão de entrega reivindicada. Todos os pontos pertencem ao contrato já aprovado e foram enviados ao único executor.

| ID | Locus | Cenário / defeito observado | Correção solicitada | Situação |
| --- | --- | --- | --- | --- |
| IMPL-01 | Inbox.tsx/responder | `texto === textoEnviado` compara valores da mesma closure e limpa texto digitado durante await. | Ref/versão de input e prova browser de edição enquanto envio pendente. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-02 | Inbox.tsx/abrir e trocarBu | finally antigo descartado por geração deixa flags de envio/backfill presas no destino. | Reset das flags no novo contexto e prova de navegação com request atrasado. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-03 | Inbox.tsx/reconciliar | Thread vazia inicia múltiplas consultas fora do objeto de single-flight. | Usar o mesmo contexto de recuperação para vazio. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-04 | Inbox.tsx/executarRecuperacao catch | Erro tardio de conversa anterior escreve erro/pendência no destino. | Verificar geração e ID em respostas e erros. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-05 | tempoReal.ts/onopen | Só reconexão posterior dispara atualização, mas contrato inclui primeira conexão estabelecida. | Callback em todo onopen. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-06 | Inbox.tsx/carregarLista | Resposta de aba antiga da mesma BU pode sobrescrever aba nova. | Capturar filtro/contexto e rejeitar resultado antigo. | Correção e cenário específico confirmados no full31 final, com fonte/build atestados e hashes conferidos. |
| IMPL-07 | test/browser-server.cjs | Provider falso usa fake.enviadas, objeto define enviados; envio lançaria erro. | Uniformizar propriedade e validar persistência/autoria real no browser. | Correção presente; browser persistiu envio e autoria no PostgreSQL, sem chamar transporte externo. |
| IMPL-08 | Runner de validação compartilhando DB | Na retomada Playwright começou enquanto API E2E ainda executava; seed/deleteMany poderiam interferir. Agregado API223/223 e browser interrompido são diagnósticos inválidos. | Interromper browser, invalidar artefatos contaminados e executar API completa, depois Playwright, EXPLAIN e RLS serializados. | API completa serializada final: 20 arquivos / 224 testes, exit0, api-e2e-authority.log. Browser e medições são executados depois, sem concorrência de suites no DB. |

| IMPL-09 | Inbox.tsx/backfill/scroll | Capturar a posição antes de await ignora rolagem/chegadas enquanto a resposta real aguarda. | Capturar a âncora imediatamente antes de prepend; comparar deslocamento relativo do mesmo ID. | Confirmado no full31 final: mesmo ID/offset relativo com delta<2px, incluindo chegada durante await. |
| IMPL-10 | Runner browser | Imagem Playwright Noble fornece Node24; contrato exige Node22. | Derivar runner descartável com binário Node22 e manter browser/deps da versão instalada; sem Dockerfile do produto alterado. | Runner verifica v22.23.3 antes de executar; Node24 anterior é diagnóstico inválido. |
| IMPL-11 | test/atendimento.e2e-spec.ts | Assert 0..10 após chegadas concorrentes não distingue select-depois-reset. | Barreira PostgreSQL real: bloquear SELECT de messages depois do ack e executar 10 incrementos, três lotes. | API224 passa; controle negativo moveu ack depois do SELECT e falhou expected10/received0; restauração byte-exata e cenário canônico 1/1 passou. Não é alegação retroativa de TDD. |
| IMPL-12 | Freshness do browser | Attestation com nome fixo era sobrescrita por uma execução posterior. | Nome imutável por run_id, prova capturada no globalSetup antes dos workers e fonte/build/served SHA vinculados. | Full31 final e FRC3 têm attestations imutáveis pré-workers;16 hashes de fontes e bundle iguais conferidos após execução. |
| IMPL-13 | Inbox.tsx/effect realtime | Fullbrowser posterior: 29/30; logout encontrou handshake de socket ainda em curso. Efeito misturava carga/filtro/BU e recriação de socket. | Diagnosticar lifecycle e estabilizar socket com callbacks atuais; manter consumidores/cleanup, sem filtro que esconda erro de console. | Corrigido separando socket dos efeitos de carga/filtro/BU e protegendo callbacks após cleanup. Logout5/5, unidade lifecycle e full31 passaram. App/global exploratórios foram descartados, sem diff fora do recorte. |

| IMPL-14 | Inbox.tsx/poll60/reconciliar | Poll acionava reconciliar e zerava cursor de recuperação pendente; backlog maior que3 páginas repetiria a cabeça indefinidamente sem Continue. | Poll deve retomar cursor/piso pendentes; eventos/ações/conexão continuam marcando dirty. Provar avanço de60s no browser sem clique Continue. | Corrigido: poll retoma recuperação pendente, eventos mantêm dirty. Cenário específico avança60s sem Continue/evento adicional e compara382 IDs; targeted1/1 e full31 passaram. |

Essas observações não substituem architecture_adherence, test_quality_audit ou final_review independentes. A resolução final depende dos arquivos consolidados, testes e revisores.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/scan-triage-api.json
```
{
  "schema_version": "leadshug-rule-spirit-triage-v1",
  "status": "final revision3 frozen-source supporting triage; independent delta judgment pending",
  "repository": "api-app",
  "raw_observations": 30,
  "deduplicated_locations": 15,
  "allowlist": "none",
  "raw_scan_sha256": "8964a4ec932917b79fd5be679e04fa777db130d1f15d579dcb9d7b414b33057d",
  "findings": [
    {
      "location": "test/browser-server.cjs:22",
      "evidence": "  process.env.WEB_ORIGIN = 'http://127.0.0.1:4173';",
      "scanner_keys": [
        "0979048a3d65a061",
        "ebc11589454fe381"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/browser-server.cjs:40",
      "evidence": "  app.enableCors({ origin: ['http://127.0.0.1:4173'], credentials: true });",
      "scanner_keys": [
        "4fbbb42b5cb59875",
        "0917bac08ff24b2c"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/timeline-fixtures.cjs:64",
      "evidence": "  const response = await fetch(`http://127.0.0.1:${apiPort}/webhooks/meta`, {",
      "scanner_keys": [
        "fdfea179a243ad7f",
        "37bfde4a277e7c3d"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/timeline-fixtures.cjs:75",
      "evidence": "      const query = new URL(req.url, 'http://localhost').searchParams;",
      "scanner_keys": [
        "18168c16c1dedf03",
        "56b00be64ca0e1ee"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/timeline-fixtures.cjs:113",
      "evidence": "server.listen(fixturePort, '127.0.0.1', () => console.log(`timeline fixtures listening on 127.0.0.1:${fixturePort}`));",
      "scanner_keys": [
        "846e6036025e845c",
        "7f3ff2bf85a898ae"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:73",
      "evidence": "    A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test');",
      "scanner_keys": [
        "222e4dc3ac247da7",
        "62cfef2ea2d4aa2b"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:74",
      "evidence": "    B = await criarMantenedora(app, 'Beta', 'dono@beta.test');",
      "scanner_keys": [
        "ec8ad555564a5583",
        "443d317681c98942"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:78",
      "evidence": "    cookieOwner = await login(app, 'dono@alfa.test');",
      "scanner_keys": [
        "58b70f0495d8269d",
        "97671a27f5ffbb15"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:102",
      "evidence": "      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'atendente@alfa.test', 'ATENDENTE');",
      "scanner_keys": [
        "1f221a9d5648bf5e",
        "7d6f9d558588c7ab"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:103",
      "evidence": "      const cookie = await login(app, 'atendente@alfa.test');",
      "scanner_keys": [
        "fdb84b2351f2613d",
        "06c90369c5fa2c4c"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:110",
      "evidence": "      const cookieBeta = await login(app, 'dono@beta.test');",
      "scanner_keys": [
        "2b23b50e8f4a1f3d",
        "8dbcd394cef3e576"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:177",
      "evidence": "      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro@alfa.test', 'ATENDENTE');",
      "scanner_keys": [
        "7c7334b879b47440",
        "1b2227ad2236611a"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:178",
      "evidence": "      const cookieOutro = await login(app, 'outro@alfa.test');",
      "scanner_keys": [
        "7d35f697f2bcba03",
        "4febe17e8bc29011"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:203",
      "evidence": "      await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro2@alfa.test', 'ATENDENTE');",
      "scanner_keys": [
        "da6f914e2b0bf405",
        "73a91c5681c0199a"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "test/atendimento.e2e-spec.ts:204",
      "evidence": "      const cookieOutro = await login(app, 'outro2@alfa.test');",
      "scanner_keys": [
        "8a6ad3385f150106",
        "f435ef941f2b1e00"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    }
  ]
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/scan-triage-web.json
```
{
  "schema_version": "leadshug-rule-spirit-triage-v1",
  "status": "final revision3 frozen-source supporting triage; independent delta judgment pending",
  "repository": "web-app",
  "raw_observations": 42,
  "deduplicated_locations": 21,
  "allowlist": "none",
  "raw_scan_sha256": "bc0fe262ac4aa795a6689ead3178c73e4481b1df0c17411d485e84885a72b75b",
  "findings": [
    {
      "location": "src/tempoReal.spec.ts:12",
      "evidence": "    expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws'); ",
      "scanner_keys": [
        "2a8f09410b6f9592",
        "edf231b3eac47db3"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "src/tempoReal.spec.ts:32",
      "evidence": "    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() }); ",
      "scanner_keys": [
        "11de67ec67e28377",
        "3ae03706d1c501fb"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "src/tempoReal.spec.ts:58",
      "evidence": "    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout }); ",
      "scanner_keys": [
        "ecd8c6244fc918e1",
        "ac44ff645d061b9b"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "src/api.ts:75",
      "evidence": "    const pareceEstatico = res.status === 405 || /^\\s*<(!doctype|html)/i.test(bruto); ",
      "scanner_keys": [
        "3c3ff59eaca3694e",
        "3ebdb512aa908de7"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Unchanged baseline HTML detector regex; not a domain or runtime target. This story only adds Thread.paginacao."
    },
    {
      "location": "playwright.config.ts:5",
      "evidence": "const API = `http://127.0.0.1:${PORTA_DA_API}`; ",
      "scanner_keys": [
        "d0ac253aa5ff151c",
        "d8e95984315f8f6b"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:26",
      "evidence": "    baseURL: 'http://127.0.0.1:4173', ",
      "scanner_keys": [
        "2a29ea59c22e2638",
        "61883216dd8dc12f"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:32",
      "evidence": "      url: 'http://127.0.0.1:3101/health', ",
      "scanner_keys": [
        "59d1ac46cac22135",
        "405b3e41f6cda288"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:80",
      "evidence": "        WEB_ORIGIN: 'http://127.0.0.1:4173', ",
      "scanner_keys": [
        "a1e456347a8821fd",
        "8a5b48f8f8c6bee4"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:85",
      "evidence": "      // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`, ",
      "scanner_keys": [
        "4b7be4c40850487c",
        "8994854a4b272f6f"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:88",
      "evidence": "      // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em ",
      "scanner_keys": [
        "5e12863dffbccf69",
        "a06bafeb722161e4"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:91",
      "evidence": "      // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o ",
      "scanner_keys": [
        "2698063e108a0609",
        "1a0d611415fc6996"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:93",
      "evidence": "      command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort', ",
      "scanner_keys": [
        "ac41a31312e558bd",
        "164bf04d7b0bbb19"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "playwright.config.ts:97",
      "evidence": "      url: 'http://127.0.0.1:4173', ",
      "scanner_keys": [
        "70831863fa683675",
        "3c89510b83ba01a9"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline.spec.ts:3",
      "evidence": "const FIXTURES = 'http://127.0.0.1:3101';",
      "scanner_keys": [
        "2c1ee4d9b92a0c18",
        "bc9bc14a55d2591e"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline.spec.ts:5",
      "evidence": "const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`;",
      "scanner_keys": [
        "9e49f12c9c12faf6",
        "c72e0b5f5b133197"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:45",
      "evidence": "  const apiEndpoint = `http://127.0.0.1:${apiPort}`;",
      "scanner_keys": [
        "e4d3b43c6a981645",
        "1c70b5070fab5314"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:48",
      "evidence": "    fetch('http://127.0.0.1:3101/health'),",
      "scanner_keys": [
        "02ced4490c6f1ae3",
        "a129a7b950a8f0ec"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:49",
      "evidence": "    fetch('http://127.0.0.1:4173/'),",
      "scanner_keys": [
        "65dcca001d2e41a7",
        "e5308c3cb7d2f03f"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:57",
      "evidence": "  const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173'));",
      "scanner_keys": [
        "69c95e087f673536",
        "75ba7c8469649337"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:60",
      "evidence": "  const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`);",
      "scanner_keys": [
        "350a9bebcb085e01",
        "0ceda0f2bb2a2a57"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    },
    {
      "location": "e2e/timeline-freshness.ts:93",
      "evidence": "    endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname }",
      "scanner_keys": [
        "0b3266de3272c907",
        "ea4c693cfacd5dc5"
      ],
      "proposed_classification": "by-design/no-action",
      "rationale": "Owned test-only loopback target or reserved .test identity; no operational target or secret; no suppression."
    }
  ]
}

```

## foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md
```
# TODO LeadsHug histórico completo e paginado na inbox

## Quick Start

Contrato criado a partir de delphi-ai/templates/todo_template.md, revisado, congelado e aprovado pelo usuário em 2026-10-14. Execução autorizada pelo authority guard normal; validação e reviews de entrega estão em andamento.

## Title

Histórico completo e paginado na inbox do LeadsHug.

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Tactical state:** `In-Progress`
- **Prepared on:** 2026-10-14
- **Scope selection source:** atendimento selecionado pelo usuário; revisão e preparação de aprovação autorizadas por “Pode seguir para revisão e aprovação”, em 2026-10-14
- **Implementation approval:** APROVADO explícito do usuário em 2026-10-14; ver Approval e authority guard normal go

## Context

A thread da inbox busca as primeiras 200 mensagens em ordem crescente, sem metadados de continuação. Uma conversa longa oculta mensagens recentes. A tela Consultar já pagina, mas atende outro contrato e não marca leitura. Esta entrega torna todo o histórico acessível na inbox, preservando BU, sessão, janela de resposta e autoria.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md`
- **Primary story ID:** `ST-ATT-01`
- **Why this is the right current slice:** CAP-010 estende um fluxo existente, com aceitação verificável e sem depender das decisões ainda abertas de transferência, mídia e estados
- **Direct-to-TODO rationale:** n/a; há feature brief para o pacote

## Contract Boundary

Este contrato aprovado define somente ST-ATT-01. Mudanças materiais de contrato, autorização, escopo ou obrigação de validação precisam da governança de escopo e aprovação; refinamentos locais fiéis ao contrato são tratados nesta execução. O planejamento das demais stories não concede execução neste TODO.

## Implementation Intent

- **Current delivery:** leitura paginada da thread BFF e navegação incremental na inbox
- **Planned next steps:** transferência/ownership, estados e mídia, em TODOs próprios
- **Anticipatory implementation authorized now:** none
- **Rationale:** reutilizar Conversation/Message e as fronteiras existentes; acrescentar abstrações apenas quando necessárias ao contrato de paginação e mesclagem

## Delivery Status Canon (Required)

- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** obter deltas independentes de aderência/TQA sobre a fonte congelada, resolver pareceres e concluir final review/guardas/consolidação para closeout local.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** review
- **Why this state now:** código corrigido e suite Web/FRC finais green com fonte idêntica; deltas independentes e final review ainda abertos.
- **Exit condition:** pareceres independentes resolvidos, guardas e consolidação canônica completos para closeout local.

## Scope

- [x] Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API.
- [x] Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor.
- [x] Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores.
- [x] Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID.
- [x] Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada.
- [x] Preservar histórico, cursor histórico, metadados atuais e draft correto durante envio, claim, close, backfill, poll e eventos/reconexão de socket.
- [x] Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens.
- [x] Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo.
- [x] Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado.

## Proposed API Contract

### GET /api/bff/conversations/:id/messages

- Sessão e grant ATENDENTE ou superior na BU; resolver/autorizar a conversa antes de validar ou consultar cursores. Sem sessão: 401. Recurso fora do escopo: 404, inclusive com query/cursor malformado.
- Query: `limite` inteiro decimal 1..100, padrão 50; `antes` cursor opaco opcional, máximo 256 caracteres; `marcarLida` booleano textual `true|false` opcional.
- Sem `antes`, `marcarLida` ausente equivale a true para conservar abertura humana. Cliente usa explicitamente false para refresh, pós-ação, poll, reconexão e recuperação. Com `antes`, leitura é sempre false; `marcarLida=true` explícito com `antes` é inválido. Valores inválidos, query repetida/array e cursor inexistente/alheio à conversa autorizada: 400 `PAGINACAO_INVALIDA`; query desconhecida é ignorada e não altera comportamento.
- A marcação de abertura é uma única atualização atômica de `unreadCount=0`, depois da autorização e antes de buscar a página. Essa escrita é a fronteira de reconhecimento: incrementos de entrada serializados depois dela permanecem não lidos. Não fazer select-depois-reset nem adicionar estado de leitura por mensagem. Se abertura/marcação falhar, não executar uma escrita posterior compensatória que apague entradas novas.
- Resposta conserva `conversa`, `janela` e `messages` e acrescenta `paginacao: { limite, temAnteriores, cursorAnterior }`.
- Sem cursor, buscar as últimas N mensagens. Responder páginas em ordem crescente pelo par `(createdAt,id)`; ordenação de ID segue a comparação do banco.
- Cursor versionado identifica a mensagem-âncora; resolver seus dados somente na conversa autorizada. Paginação anterior usa comparação estrita do par, busca no máximo N+1 registros e nunca escreve não lidas.
- `cursorAnterior` representa o registro mais antigo da página quando há continuação; caso contrário null. Vazio: messages vazio, temAnteriores false, cursor null.
- API pública e Consultar mantêm seus contratos e efeitos atuais. Dublês no backend de testes substituem somente portas externas; não há flag de teste no código de produção.

### Recuperação e estado da inbox

- Manter somente a coleção da conversa ativa por ID; liberar contexto/páginas quando BU/conversa mudar. O cursor histórico pertence ao backfill e não é substituído pelo cursor da página recente de um refresh.
- Na atualização, capturar uma fronteira fixa T igual ao timestamp da mensagem mais recente conhecida antes da passagem. Buscar página recente sem marcar leitura e caminhar para trás até alcançar timestamp estritamente menor que T, ou esgotar mensagens. Incluir integralmente o grupo empatado em T; encontrar um ID conhecido não encerra a recuperação.
- Se a coleção ainda é vazia, atualização funciona como página inicial sem efeito de leitura. Separar o piso de cobertura confirmado do maior timestamp mesclado. A recuperação captura um piso pendente T e toda passagem coalescida/retomada/retry conserva esse piso original, mesmo quando a cabeça já avançou para H maior que T.
- Evento durante a recuperação marca uma nova passagem necessária desde a página recente, ainda com o piso pendente T; terminar a caminhada atual não confirma cobertura. Só promover o piso confirmado quando uma passagem atravessar todo T sem evento/trabalho concorrente pendente. Se houver dirty/pending, conservar T e a indicação de atualização, com o mesmo orçamento de três queries por rodada. Não promover pelo máximo da coleção nem por um poll enquanto houver recuperação pendente.
- A recuperação cobre inserções novas, incluindo ID menor em T atrás de um cursor já percorrido. Importação/backdating de histórico fora do grupo de cobertura permanece fora deste recorte. Mensagens mais recentes mescladas não eliminam essa prova de continuidade.
- Recuperação tem cursor/progresso próprios e uma única passagem em voo por contexto. Cada rodada executa no máximo três queries de página, separadas e bounded; uma rodada incompleta mantém indicação visível de atualização/lacuna e cursor para `Continuar atualização`/retry. Novo evento não reinicia seu orçamento; polling pode retomar a rodada pendente. Não afirmar continuidade até cruzar toda a fronteira.
- Disparadores: evento de mensagem coalescido, socket restabelecido sem depender de outro evento, pós-ação e poll da thread selecionada a cada 60 segundos. Registrar callback de conexão no helper existente; preservar seus consumidores.
- Backfill altera somente coleção e cursor histórico. Metadados conversa/janela só são aplicados pela leitura atual com versão/frescor adequado; uma página anterior atrasada não desfaz close, troca de status ou atualização de janela.
- Todo efeito assíncrono captura BU/conversa/geração. Resposta, erro, scroll e limpeza do texto enviado são ignorados se contexto mudou; limpeza de draft também verifica que o usuário não digitou outro texto enquanto o envio estava pendente.
- Histórico anterior preserva posição do usuário. Mensagens novas não forçam deslocamento quando ele lê trecho antigo. Estados de loading, vazio, fim, recuperação pendente, falha/retry e acesso perdido são visíveis e operáveis por teclado.

## Delivery Status Semantics

- `Pending`: no meaningful delivery milestone has been reached yet.
- `Local-Implemented`: work is implemented in a local branch and validated locally.
- `Lane-Promoted`: work has been merged through the declared lane threshold (usually `dev`).
- `Production-Ready`: final required lane threshold is complete and confidence gates are satisfied.
- `Provisional`: delivery is intentionally partial/incomplete but useful for unblocking dependent work.
- `Blocked`: work cannot currently proceed; `Blocker Notes` become mandatory.

## Active Work State Semantics

- `implementation`: the TODO is still gaining or changing implementation/test evidence.
- `review`: local implementation is materially complete, but the TODO remains in `active/` because package-wide review, Copilot-mimic, CI-equivalent, final validation, or explicit promotion-readiness scrutiny is still open.
- `blocked`: execution is paused on an explicit blocker; `Blocker Notes` are mandatory.
- `n/a once moved out of active`: use after the TODO moves to `promotion_lane/` or `completed/`.

## Provisional Notes (Required if `Qualifiers` includes `Provisional`)

n/a; nenhuma entrega parcial é reivindicada.

## Blocker Notes (Required if `Qualifiers` includes `Blocked`)

n/a; nenhuma decisão material bloqueando execução no início.

## Execution Lane Tracking (Required)

- **Local implementation branches:** api-app:feature/inbox-timeline-pagination; web-app:feature/inbox-timeline-pagination no checkout principal. Foundation:main
- **Promotion lane path:** branches locais -> validação local -> evidência/closeout na Foundation; deploy e promoção remota de código fora do recorte
- **Lane-promoted threshold for this TODO:** n/a; entrega local validada
- **Production-ready threshold for this TODO:** não reivindicado; publicação requer contrato separado
- **Execution topology:** primary-checkout-single-writer
- **Git isolation authorization:** not-requested; sem worktrees/cópias auxiliares
- **Subagent / delegation authorization:** revisão independente requerida pelo skill local wf-docker-todo-approval-gates-method e seu workflow; executor de código será o routine-executor predeclarado somente após APROVADO deste contrato
- **Documentation git-write authority:** git_write_authority_guard retornou go para git-commit e git-push de Foundation main; autorização autônoma documental conforme workflow local

## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Out of Scope

- Transferência, exclusividade de resposta, SLA, distribuição de agentes, novas equipes e papéis.
- Estados de entrega/leitura/falha e deduplicação de recebimento por externalId.
- Mídia, templates, campanhas, CRM e automações Typebot.
- Mudanças nos contratos da API pública ou da tela Consultar.
- Redesenho da lista de conversas ou paginação da lista; a story cobre mensagens de uma conversa.
- Expansão de infraestrutura, uso de dados reais, integração com runtime legado ou publicação.

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| api | api-app | 5db3fbe2043428749895fc3ff6441e9457467dd0 | working_tree |
| web | web-app | 6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9 | working_tree |
| foundation | foundation_documentation | 40828a20f2d6c3a1443e7ee132f42483840d6abb | working_tree |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/domain/inbox/conversations.service.ts | A,M,?? | Consulta bounded e cursor validado. |
| api | src/domain/inbox/*pagination*.ts | A,M,?? | Consulta bounded e cursor validado. |
| api | src/domain/inbox/*pagination*.spec.ts | A,M,?? | Consulta bounded e cursor validado. |
| api | src/surfaces/bff/conversations.controller.ts | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/atendimento.e2e-spec.ts | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/*timeline*.e2e-spec.ts | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/browser-server.cjs | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | test/timeline-fixtures.cjs | A,M,?? | Contrato, escopo, fixtures e bootstrap de teste, sem mudanças no entrypoint de produção. |
| api | prisma/schema.prisma | A,M,?? | Somente índice de paginação, se necessário e justificado por plano de consulta. |
| api | prisma/migrations/*timeline*/migration.sql | A,M,?? | Somente índice de paginação, se necessário e justificado por plano de consulta. |
| web | src/api.ts | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/telas/Inbox.tsx | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/*timeline* | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/estilo.css | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/tempoReal.ts | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | src/tempoReal.spec.ts | A,M,?? | Types, coleção/cursores, navegação, posição e callback de conexão/reconexão. |
| web | e2e/telas.spec.ts | A,M,?? | Fluxo real e correção do path da API. |
| web | e2e/*timeline*.spec.ts | A,M,?? | Fluxo real e correção do path da API. |
| web | playwright.config.ts | A,M,?? | Fluxo real e correção do path da API. |
| web | e2e/timeline-freshness.ts | A,M,?? | globalSetup canônico valida build/runtime servido antes dos testes, suporte de prova já autorizado. |
| foundation | todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md | A,M,D,R,?? | Contrato, framing e evidência específicos. |
| foundation | artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md | A,M,?? | Contrato, framing e evidência específicos. |
| foundation | artifacts/reviews/leadshug-inbox-timeline-20261014/** | A,M,?? | Contrato, framing e evidência específicos. |
| foundation | backlog/README.md | A,M,?? | Contrato, framing e evidência específicos. |
| foundation | modules/inbox-and-conversations.md | A,M,?? | Contrato, framing e evidência específicos. |

| foundation | todos/completed/features/TODO-leadshug-inbox-message-timeline-pagination.md | A,M,R,?? | Relocação do mesmo TODO no closeout aprovado, após provas e guardas. |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| api | src/integrations/** | any | Providers, API pública e recebimento fora do recorte. |
| api | src/surfaces/public/** | any | Providers, API pública e recebimento fora do recorte. |
| api | src/domain/inbox/incoming.service.ts | any | Providers, API pública e recebimento fora do recorte. |
| web | src/telas/Typebot.tsx | any | Funcionalidades independentes. |
| web | src/telas/IdentidadeVisual.tsx | any | Funcionalidades independentes. |
| foundation | project_mandate.md | any | Preservar história e autoridades não alteradas por este recorte. |
| foundation | project_constitution.md | any | Preservar história e autoridades não alteradas por este recorte. |
| foundation | system_roadmap.md | any | Preservar história e autoridades não alteradas por este recorte. |
| foundation | local_packages.yaml | any | Preservar história e autoridades não alteradas por este recorte. |
| api | .env* | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | .gitmodules | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | docker-compose.yml | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | .git/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | .github/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .env* | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .gitmodules | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | docker-compose.yml | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .git/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| web | .github/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .env* | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .gitmodules | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | docker-compose.yml | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .git/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| foundation | .github/** | any | Sem configuração secreta, gitlinks ou expansão do runtime/CI neste TODO. |
| api | node_modules/** | any | Saídas locais de validação não são entrega versionada. |
| api | dist/** | any | Saídas locais de validação não são entrega versionada. |
| api | artifacts/tmp/** | any | Saídas locais de validação não são entrega versionada. |
| web | node_modules/** | any | Saídas locais de validação não são entrega versionada. |
| web | dist/** | any | Saídas locais de validação não são entrega versionada. |
| web | artifacts/tmp/** | any | Saídas locais de validação não são entrega versionada. |
| foundation | node_modules/** | any | Saídas locais de validação não são entrega versionada. |
| foundation | dist/** | any | Saídas locais de validação não são entrega versionada. |
| foundation | artifacts/tmp/** | any | Saídas locais de validação não são entrega versionada. |

### Diff Deviation Analysis

Análise preliminar: o guard identificou incompatibilidade de representação (heading com sufixo, vários globs numa célula e labels workspace/all não declarados), sem desvio de produto. Corrigida a representação para título exato, um glob por linha e regras por repositório; os mesmos paths e baselines aprovados foram preservados. O tipo `??` explicita o estado ainda não staged dos arquivos novos já autorizados como A; não autoriza novos caminhos. A relocação do próprio TODO active → completed é o closeout já autorizado, sem alterar outros registros históricos. Guard final e diff real serão registrados antes da entrega.

Concretização de suporte de prova em 2026-10-15: `web-app/e2e/timeline-freshness.ts` implementa globalSetup de frescor já exigido pelo contrato aprovado (build fresco, backend real e evidência runtime), pois capturar do host falha quando preview é isolado no container e uma captura posterior à suite não satisfaz a regra temporal. A alternativa de arquivo temporário obrigatório faria clones dependerem de arquivo ausente; o helper versionado é a escolha local reproduzível. Acrescentado somente este path ao contrato. Não há nova story, comportamento de produto, provider, ambiente operacional ou obrigação de validação; é o HOW do suporte de teste já autorizado em Approval, VAL-04/05 e no pedido de continuidade. Sem exceção de modelo/topologia e sem nova aprovação de produto necessária.


## Bounded But Elastic Guardrails

Ajustes locais de cursor, queries, mesclagem e CSS podem permanecer neste objetivo. Alterar a API pública, papéis, unread semantics além do contrato proposto, providers, retries ou topology exige recorte/decisão próprios.

## Definition of Done

- [x] DOD-01: contrato aprovado e consolidado no módulo responsável.
- [x] DOD-02: histórico maior que 200 é alcançável sem lacunas/repetições, inicial recente, empates estáticos e inserções empatadas durante recuperação.
- [x] DOD-03: autorização/cursor não permitem outra conversa, BU ou Mantenedora; recurso inacessível é 404 antes de query inválida.
- [x] DOD-04: backfill, envio/refresh/close, troca rápida, reconexão sem evento posterior e recuperação mantêm histórico, posição, cursores, metadados e draft corretos.
- [x] DOD-05: limite/cursor/marcarLida, vazio/fim, falha/retry e recuperação pendente têm contrato/UI verificados; entradas posteriores à fronteira de abertura continuam não lidas.
- [x] DOD-06: suites API/Web/Playwright passam no backend real e banco isolado; plano SQL recente/profundo/empates registra custo e decisão de índice; migrate deploy validado se houver migração.
- [ ] DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão.

## Validation Steps

- [x] VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional.
- [x] VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e.
- [x] VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos.
- [x] VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL.
- [x] VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada.
- [x] VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado.
- [ ] VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout.
- [x] VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha.

## Completion Evidence Matrix (Required Before Delivery Claim)

Um registro por critério de Scope, Definition of Done e Validation Steps; texto integral preserva rastreabilidade. Status não são promovidos por resultado intermediário ou execução contaminada.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | Documentar o contrato da thread BFF no módulo inbox-and-conversations antes da alteração da API. | doc | Foundation4cabc467 + modules/inbox-and-conversations.md | Foundation main | passed | Contrato consolidado antes do executor alterar API; não é só nota tática. |
| SCOPE-02 | Scope | Validar paginação por cursor e limites na entrada; autorizar a conversa antes de resolver cursor. | PostgreSQL integration | test/atendimento.e2e-spec.ts:317,365,371; api-e2e-authority.log | Node22 / PG16 descartável | passed | Cursor alheio em recurso autorizado400; recurso sem grant404 antes da query; sem sessão401; unread readback preservado. |
| SCOPE-03 | Scope | Retornar a página recente, ordenar deterministicamente e fornecer continuação para mensagens anteriores. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282; api-e2e-authority.log | Node22 / PG16 descartável | passed | 251 IDs, limite37 e grupo empatado; comparação de IDs na ordem real do banco, página recente e continuação bounded. |
| SCOPE-04 | Scope | Atualizar tipos/adapter web e inbox para carregar anteriores, manter posição e mesclar atualizações por ID. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | 251IDs, prepend preserva âncora inclusive chegada durante await, merge porID e cursor histórico separado. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| SCOPE-05 | Scope | Impedir que respostas atrasadas de outra conversa/BU substituam a conversa selecionada. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Seis subcenários de contexto: conversa/BU × envio antigo com sucesso/falha/backfill. Destino mantém seleção, draft, erro, IDs, metadados e scroll. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| SCOPE-06 | Scope | Preservar histórico, cursor histórico, metadados atuais e draft correto durante envio, claim, close, backfill, poll e eventos/reconexão de socket. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Close vence backfill; autoria/draft/ref; reconnect sem evento; poll60 retoma progresso; T fixo, budget3 inclusive erros e restart obrigatório. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| SCOPE-07 | Scope | Atualizar testes de contrato, PostgreSQL e Playwright com fixtures determinísticas maiores que 200 mensagens. | PostgreSQL + source-owned Playwright | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Fixtures próprias251+, empates acima de página, grupoT/H>T/lateID, burst e readback DB completo; testes source-owned, sem payload BFF fabricado. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| SCOPE-08 | Scope | Corrigir o caminho ../api para ../api-app no harness; acrescentar bootstrap de teste do backend real com adapters externos determinísticos e fixtures de banco, estritamente para validar este fluxo. | source + integration | playwright.config.ts + test/browser-server.cjs + test/timeline-fixtures.cjs; execution-evidence.md | backend Nest real / DB exclusivo | passed | Path ../api-app; somente Meta/Evolution fake, sem flags ou rotas de teste no entrypoint de produção; autoria persistida observada. |
| SCOPE-09 | Scope | Se o plano de consulta exigir índice composto novo, acrescentar apenas a migração desse índice e validar deploy em banco de teste isolado. | SQL EXPLAIN + API e2e | evidence/explain-timeline-exact.sql/.log; evidence/explain-index-trial.sql/.log; pcv-eps.json; atendimento.e2e-spec.ts | PG16 /20382 mensagens/1000 empatadas | passed | Recent1.094ms/deep3.442ms/tie0.850ms; trial composto deep3.942ms e9832buffers contra357 existente. Sem migration nova: condição de índice não demonstrou ganho. Risco de varredura profunda explícito; avaliação independente pendente. |
| DOD-01 | Definition of Done | DOD-01: contrato aprovado e consolidado no módulo responsável. | doc | TODO + modules/inbox-and-conversations.md | foundation | passed | APROVADO explícito e contrato consolidado em modules/inbox-and-conversations.md. |
| DOD-02 | Definition of Done | DOD-02: histórico maior que 200 é alcançável sem lacunas/repetições, inicial recente, empates estáticos e inserções empatadas durante recuperação. | PostgreSQL + source-owned Playwright | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | 251IDs ordenados e grupoT completo com H>T/lateID/dirty; full IDs DB/UI depois de cobertura; FRC10gatilhos×3rep,12frames/unread. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| DOD-03 | Definition of Done | DOD-03: autorização/cursor não permitem outra conversa, BU ou Mantenedora; recurso inacessível é 404 antes de query inválida. | PostgreSQL integration | test/atendimento.e2e-spec.ts:317,365; api-e2e-authority.log | Node22 / PG16 descartável | passed | Negativos distintos: outra conversa autorizada, outra BU da mesma Mantenedora sem grant e outra Mantenedora. |
| DOD-04 | Definition of Done | DOD-04: backfill, envio/refresh/close, troca rápida, reconexão sem evento posterior e recuperação mantêm histórico, posição, cursores, metadados e draft corretos. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Backfill/envio/close/contextos/reconnect/poll/draft/scroll, mais falha histórica+evento com restart recente sem novo trigger. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| DOD-05 | Definition of Done | DOD-05: limite/cursor/marcarLida, vazio/fim, falha/retry e recuperação pendente têm contrato/UI verificados; entradas posteriores à fronteira de abertura continuam não lidas. | PostgreSQL + Browser / Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Parser/escopo/neutralidade API224; loading/vazio/fim/retry/acesso e pendência browser; abertura+evento não se perde, empty>3pages+evento entre rodadas. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| DOD-06 | Definition of Done | DOD-06: suites API/Web/Playwright passam no backend real e banco isolado; plano SQL recente/profundo/empates registra custo e decisão de índice; migrate deploy validado se houver migração. | scripts + SQL + Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | API115unit/224E2E; Web20unit/34browser; FRC3; SQL20382rows/1000ties. Sem migration: índice candidato não justificou custo. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| DOD-07 | Definition of Done | DOD-07: revisão, guardas de execução/closeout e matriz de evidência específicos completos antes de conclusão. | review | VAL-07 | foundation | planned | Gates não executados. |
| VAL-01 | Validation Steps | VAL-01: provisionar PostgreSQL 16 descartável com DB exclusivo e porta registrada; aplicar migrations e confirmar DATABASE_URL antes de qualquer helper deleteMany. Não usar banco operacional. | runtime + migration | api-e2e-authority.log + attestation-browser-full-final-20261015.json; execution-evidence.md | postgres:16-alpine / leadshug_timeline_20261014 | passed | 17 migrations; porta5432 somente rede Docker, sem host publish; DATABASE_URL explícita e guard de DB descartável antes do cleanup. |
| VAL-02 | Validation Steps | VAL-02: no runner Linux Node 22 da API: npm ci; npm run prisma:generate; npm run lint; npm run build; npm test; npm run test:e2e. | scripts completos | api-e2e-authority.log; execution-evidence.md | Linux Node22 / principal checkout | passed | npm ci no volume Linux; generate/lint/build/unit115/E2E224 exit0. Sem execução simultânea de browser no DB. |
| VAL-03 | Validation Steps | VAL-03: fixture base com 251 mensagens, empates maiores que uma página e duas conversas na BU autorizada; outra BU da mesma Mantenedora sem grant; outra Mantenedora/BU. Caminhar páginas, comparar todos os IDs e verificar 400 para cursor alheio em conversa autorizada, 404 antes de validar query em recurso inacessível e ausência de efeitos indevidos. | PostgreSQL integration | test/atendimento.e2e-spec.ts:282,317,365,371; api-e2e-authority.log | PG16 dedicado | passed | 251 IDs e empates; negativos scoped e consulta inválida sem efeitos de leitura. |
| VAL-04 | Validation Steps | VAL-04: no runner da Web: npm ci; npm run build; npm test; npm run test:tela; backend real fresco e mesmo DB dedicado via LEADSHUG_E2E_DATABASE_URL. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | npmci em volumesLinux; npmrunbuild/test/test:tela; Node22.23.3 e Nest/PG16 reais no mesmo DB descartável exclusivo. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| VAL-05 | Validation Steps | VAL-05: browser abre recente/carrega anteriores, envia com autoria persistida, recebe evento real do backend, executa close em paralelo com backfill e troca conversa/BU durante envio e request atrasado. Atrasar resposta real, sem fabricar payload BFF. Provar reconexão sem evento posterior, burst acima de 100, grupo empatado e ID menor inserido depois; mais de três páginas mantém estado de recuperação e retoma sem lacuna. Combinar H>T, passagem já atrás de parte do grupo T, inserção de ID menor atrás do cursor, evento durante a caminhada e passagem coalescida com o mesmo piso T; comparar IDs completos após cobertura confirmada. | Browser / Playwright navigation/mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | Autoria persistida, eventos/reconnect reais, close/contextos e todos os estados de recuperação. Counts3/max1, erros cobrados no despacho, restart histórico, seis efeitos de destino. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |
| VAL-06 | Validation Steps | VAL-06: sempre capturar EXPLAIN representativo da query recente, profunda e com grande grupo empatado, registrando SQL, linhas examinadas/ordenadas e decisão de índice. Se criado índice, executar migrate deploy no DB dedicado. | SQL EXPLAIN + API e2e | evidence/explain-timeline-exact.sql/.log; evidence/explain-index-trial.sql/.log; pcv-eps.json; atendimento.e2e-spec.ts | PG16 /20382 mensagens/1000 empatadas | passed | Recent1.094ms/deep3.442ms/tie0.850ms; trial composto deep3.942ms e9832buffers contra357 existente. Sem migration nova: condição de índice não demonstrou ganho. Risco de varredura profunda explícito; avaliação independente pendente. |
| VAL-07 | Validation Steps | VAL-07: cumprir revisões/guardas exigidos, incluindo aderência arquitetural, qualidade de testes, segurança, performance, dívida de verificação e review final, antes do closeout. | test/runtime/review | Validation Steps e relatório específico na execução | local isolado / foundation | planned | Prova futura; não executada nesta revisão. |
| VAL-08 | Validation Steps | VAL-08: PostgreSQL/browser verificam não lidas: abertura atômica, IN posterior à marcação, backfill/refresh/reconexão read-neutral e entrada concorrente à abertura. Testar também nenhuma escrita quando autorização/query falha. | PostgreSQL + Browser / Playwright mutation | web-app/e2e/timeline.spec.ts; npm run test:tela (project run_web_navigation_smoke equivalent); evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; pcv-frc.json | feature/inbox-timeline-pagination;http://127.0.0.1:4173;realNest/PG16 | passed | ACK atômico10incrementos×3lotes e INposterior11; background neutro; abertura+INpreserva1; recuperação forte12; erros auth/query sem escrita. Playwright mutation em branch non-main; build fresco/served==dist SHA2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e. Revisão independente ainda em andamento. |

## External Dependency Readiness (Required When External Systems Matter)

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Docker local | Runner e PostgreSQL isolado | healthy | 2026-10-14 | Daemon 27.1.1 respondeu | Containers operacionais não são alvos de testes. |
| Node.js 22 | Build/suites | healthy | 2026-10-14 | node.exe v22.22.2 disponível; node Linux ausente | Execução planejada em runner Linux Node 22 compatível com Dockerfiles; não misturar npm Windows com processos Linux. |
| Auditor interno TQA | Modelo prescrito gpt-5.6-terra | healthy | 2026-10-14 | codex exec ephemeral/read-only com effort max: exit0 MODEL_AVAILABLE; artifacts/tmp/inbox-timeline-execution/native-model-probe-events.jsonl | Usar runner nativo interno; nenhuma exceção de modelo é necessária. |
| Meta/Evolution externos | Interfaces de transporte preservadas | unknown | 2026-10-14 | Nenhum probe externo | Bootstrap de teste usa backend real e substitui somente portas externas; não enviar mensagens reais. |

Execução local planejada: runner Linux temporário Node 22, conforme imagens Node 22 dos Dockerfiles; PostgreSQL 16 descartável exclusivo deste TODO, com DB/porta registrados antes de E2E e DATABASE_URL explícita. Sem editar .env/Compose do produto. API e browser compartilham o mesmo DB de teste. A implementação pode acrescentar suporte de teste nos paths previstos; prontidão efetiva será provada antes da suite.

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Current profile:** Operational / Coder para execução delegada e consolidação local; Assurance / Tester-Quality para os gates independentes, mantendo owners serializados.
- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs, react, vite, postgresql, prisma, docker.
- **Handoff:** executor único implementa/testa API/Web; orchestrator mantém TODO/evidência; reviewers read-only nas fases derivadas.
- **Execution topology:** primary-checkout-single-writer; Foundation main, API/Web feature/inbox-timeline-pagination, sem worktrees.
- **Rule ingestion on 2026-10-14:** TODO, constituição/módulos e fontes da tabela Rules Acknowledgement recarregados após APROVADO; também boundary/orchestration e regras de schemas/migrations serão carregadas se houver índice.

## Complexity

- **Level:** medium
- **Checkpoint policy:** contrato e API, UI integrada, prova browser e closeout; cada checkpoint tem evidência afetada, sem alegar suite ampla antes de sua execução
- **Why this level:** alteração de API persistente consumida por UI com cursores, autorização e races de realtime

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** foundation_documentation/modules/inbox-and-conversations.md
- **Secondary module docs:** identity-and-tenancy.md e audit-and-history.md, para preservar invariantes
- **Consolidation target:** somente contrato local da thread e regras de cursor/paginação no módulo inbox-and-conversations
- **Source capability:** CAP-010 no catálogo ST-02, referência de evidência e não ID de capacidade canônica nova

## Decision Pending (Resolve Before Freeze)

Nenhuma decisão de produto permanece pendente: o usuário aprovou o contrato congelado com “APROVADO” em 2026-10-14. A implementação segue o recorte ST-ATT-01. A decisão condicional de índice depende dos planos SQL previstos; não amplia o contrato.

## Decisions (Resolved Before Freeze)

Decisões consolidadas após ARCH-TL-01..06 e aprovadas pelo usuário em 2026-10-14:

- Primeiro recorte BFF de mensagens na inbox; API pública, Consultar e demais stories ficam fora.
- Cursor anterior scoped, ordem createdAt/id, padrão 50 e teto 100. Não acrescentar cursor depois: ele não elimina a necessidade de sobreposição em timestamps empatados.
- Marcação atômica antes da consulta somente na abertura humana; refresh/backfill/recuperação são explicitamente read-neutral.
- Recuperação cruza integralmente o piso pendente de timestamp, preservado entre passagens coalescidas/retomadas/retry até cobertura sem trabalho concorrente; três queries por rodada, progresso/retry e reconexão/poll.
- Coleção por conversa, cursor de histórico separado do progresso de recuperação e versionamento local de metadados/efeitos; não criar framework ou cache de todas as conversas.
- Backend real, PostgreSQL descartável e providers fake somente nas portas externas; query plan obrigatório mesmo sem índice novo.
- Foundation main; código em branches locais com single writer; sem worktrees, deploy ou mensagens externas reais.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Decision | Source | Status | Handling / consolidation |
| --- | --- | --- | --- |
| Conversa única BU/contato | modules/inbox-and-conversations.md | preserved | Cursor consulta somente conversa autorizada. |
| Grants materializados na BU | modules/identity-and-tenancy.md | preserved | Negativos de tenant/BU no banco real. |
| Histórico e leitura scoped | modules/audit-and-history.md | preserved | Consulta de auditoria não ganha efeito de atendimento. |
| Janela/capability de envio | modules/inbox-and-conversations.md | preserved | Envio e API pública têm suites de regressão. |
| Paginação da thread | contrato proposto deste TODO | extend-local-contract | Contrato aprovado consolidado em modules/inbox-and-conversations.md antes da implementação. |

## Decision Baseline (Frozen Before Implementation)

Proposta técnica congelada para crítica em 2026-10-14 após integração ARCH-TL-01..06: superfície BFF, parâmetros/limites, reconhecimento atômico, recuperação bounded, estado por conversa, paths, DoD e provas reais deste TODO. A referência de versão publicada está em Gate: Review Baseline Freeze. O congelamento original não concedia implementação; a autorização posterior está registrada em Approval, pelo “APROVADO” explícito de 2026-10-14.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)

- **Applicability:** required
- **Why this applies:** estabelece acesso paginado scoped e mesclagem consistente para uma thread operacional antes truncada
- **Deviation / debt being retired:** teto silencioso de 200 mensagens e substituição da coleção após refresh
- **Target steady-state after closeout:** acesso determinístico bounded e atualização sem perda de histórico/contexto
- **Temporary exceptions allowed:** none
- **Cutover / removal condition:** BFF e inbox adotam o contrato aprovado juntos, com regressões passando; nenhum fallback para carregar todas as mensagens

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Cursor dentro da conversa autorizada | constituição + contrato BFF | API | Cursor não amplia grants. |
| Ordem createdAt/id e query bounded | contrato proposto | API | Empates e inserções não duplicam páginas. |
| Estado por conversa e geração de request | regra React | Web | Resposta antiga não troca conversa/BU. |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| Aumentar teto fixo ou fetch-all | Consulta sem paginação | Repete truncamento ou leitura ilimitada. | No exceptions |
| Cursor sem escopo ou só timestamp | Negativos/empates falham | Pode vazar dados ou perder mensagens. | No exceptions |
| Refresh substitui histórico ou aceita contexto antigo | Browser perde mensagens | Quebra atendimento em atualização/troca. | No exceptions |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| PostgreSQL contract tests | BFF/cursor | npm run test:e2e | Teto/empate/escopo/limites | implement-in-this-todo | VAL-03, DOD-02/03/05 |
| Browser mutation/navigation | Inbox | npm run test:tela | Envio/refresh/troca/contexto | implement-in-this-todo | VAL-05, DOD-04/06 |
| Query plan | índice de Message | EXPLAIN representativo | Scan/sort sem acesso scoped adequado | implement-in-this-todo | VAL-06, registrar decisão do índice |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)

- **Architecture decision review:** required
- **Decision review status:** findings_integrated
- **Decision review evidence:** artifacts/reviews/leadshug-inbox-timeline-20261014/architecture-review.json; resolução ARCH-TL-01..06 neste TODO e critique-resolution.json verificam a integração no plano.
- **Architecture adherence review:** required
- **Adherence review status:** running
- **Adherence review evidence:** round1 interno stateless gpt-6.1-sol/max coletado com turn.completed, JSON canônico validado/merge: delivery-adherence-round-1.json. ARCH-DEL-01..03 são3 blockersP2 atuais; correção e delta pendentes. Pacote revisado SHA0b106804c789463057279df728e33635711244d4ca76dbf868b6427619cd5cd4.
- **Dedicated multi-lane audit:** not_needed pelo piso atual; não substitui crítica, segurança/performance, TQA e final review requeridos.

## Gate: Review Baseline Freeze

- **Gate decision:** required
- **Gate status:** no_material_findings
- **Baseline branch:** main
- **Baseline commit:** 649372fbe81f6cccc0f8902b52fe32e2ecfc061a
- **Baseline push reference:** origin/main
- **Evidence / reference:** git.exe push origin main completado; baseline 649372fb com integração ARCH-TL-01..06 e resolução da crítica publicado em 2026-10-14; git_write_authority_guard go para commit/push
- **Waiver authority / reference (required if waived):** none

## Gate: Review Scope Drift

- **Gate decision:** required
- **Gate status:** no_material_findings
- **Evidence / reference:** executar após convergência da revisão contra o baseline publicado
- **Waiver authority / reference (required if waived):** none

## Questions To Close

Aprovação do contrato resolvida: APROVADO em2026-10-14, após crítica convergida; ARCH-TL-03 foi integrado e confirmado no delta, com contraprova de execução agora registrada. Questões de transferência, mídia e status continuam nas stories posteriores; não serão resolvidas por esta implementação.

## Pattern References (Optional; Enforced When Cited)

n/a; nenhum ID de pattern é reivindicado.

## Assumptions Preview (Required Before Plan Review)

| ID | Assumption | Evidence | Risk | Validation / Impact | Handling |
| --- | --- | --- | --- | --- | --- |
| A-01 | Thread pega primeiras 200 mensagens | api-app/src/domain/inbox/conversations.service.ts:88 | Oculta recente | Fixture 251; query/contrato | Keep as Assumption |
| A-02 | Refresh substitui coleção da thread | web-app/src/telas/Inbox.tsx:59 | Perda de páginas | Browser envio/refresh/troca | Keep as Assumption |
| A-03 | API pública lista mensagens em query própria | api-app/src/surfaces/public/conversations.controller.ts:103 | Regressão contrato | Suites atuais sem mudança de shape | Keep as Assumption |
| A-04 | Helpers E2E apagam dados do banco apontado | api-app/test/helpers.ts:112 | Perda de dados | PostgreSQL dedicado descartável | Keep as Assumption |
| A-05 | Harness precisa corrigir caminho e provider determinístico para provar envio | web-app/playwright.config.ts:32; api-app/test/helpers.ts:68 | Suite inválida ou envio externo | Backend real com portas externas fake em suporte de teste | Keep as Assumption |

## Execution Plan (Required Before `APROVADO`)

### Ordered Steps

1. Resolver DP-01..03, preparar revisão/freeze/aprovação conforme workflows; documentar contrato no módulo.
2. Reproduzir truncamento e testar cursor/limites/empates/escopo no PostgreSQL dedicado.
3. Implementar consulta bounded e contrato BFF; avaliar índice real e migrar somente se necessário.
4. Implementar coleção por conversa, páginas anteriores, posição, atualização e proteção contra respostas antigas.
5. Corrigir apenas o path do harness, construir API/Web frescos e executar fixtures/fluxos browser.
6. Validar regressões do núcleo, consolidar contrato/evidência e cumprir closeout.

### Flow Evidence Planning Matrix

| Flow | Fixture | Required evidence | Negative / race |
| --- | --- | --- | --- |
| Abrir/carregar anteriores | 251 mensagens | browser recente, scroll, alcançar primeira e última | empates, página vazia, cursor inválido |
| Enviar/atualizar | Histórico anterior carregado e canal fake | backend persiste e UI mantém coleção | resposta/evento repetido não duplica ID |
| Reconectar sem evento posterior | Burst acima de 100 e socket cortado | backend persiste; callback/poll recupera IDs completos | nenhuma mensagem extra para disparar a recuperação |
| Timestamps empatados | Cabeça H>T, grupo T maior que página, ID menor inserido atrás do cursor | Passagem coalescida conserva T e recupera todos os IDs | dirty durante caminhada e mais de três páginas não promovem piso prematuramente |
| Não lidas | IN antes/depois da abertura atômica | readback no PostgreSQL; background preserva contador | autorização/query inválida não escreve |
| Mesmo contexto em paralelo | Backfill atrasado e close/envio/refresh | cursor histórico e metadados/draft atuais preservados | resposta real atrasada não restaura estado |
| Trocar conversa/BU | Duas conversas e dois tenants | browser seleciona destino e conserva contexto | resposta antiga atrasada não substitui destino; sem grant falha |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Authority status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| API / CI api | BFF e parser alterados | npm ci; npm run prisma:generate; npm run lint; npm run build; npm test | Local-Implemented | passed | api-e2e-authority.log; execution-evidence.md | passed | Linux Node22,115 unitários; equivalente somente ao job API tocado. |
| API / PostgreSQL local adicional | Persistência/escopo/concorrência | npm run test:e2e | Local-Implemented | passed | api-e2e-authority.log; atendimento.e2e-spec.ts | passed | 224 testes/20 arquivos; DB exclusivo,17 migrations; não é claim de CI remoto. |
| Web / CI web | Consumidor/estado/realtime | npm ci; npm run build; npm test | Local-Implemented | passed | evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; execution-evidence.md | passed | LinuxNode22;Webunit20/browser34; source/build/served antes dos workers; prova local sem CI remoto. |
| Web / browser local adicional | Navegação/rolagem/races reais | npm run test:tela | Local-Implemented | passed | evidence/web-authority-revision3-final-full-20261015.log; evidence/attestation-browser-web-authority-revision3-final-full-20261015.json; execution-evidence.md | passed | LinuxNode22;Webunit20/browser34; source/build/served antes dos workers; prova local sem CI remoto. |

Compatibilidade de representação: completion guard lê status na coluna5, authority guard na coluna7. Os mesmos resultados são espelhados como Status/Authority status; notas permanecem na coluna8. Nenhuma validação ou comando é substituído.

### Frontend / Consumer Matrix

| Producer | Consumer | Impact / proof |
| --- | --- | --- |
| Thread BFF | web-app/src/api.ts e Inbox.tsx | Tipo paginacao e estado de páginas; teste contrato/browser |
| Evento WebSocket | Inbox.tsx | Refresh scoped preserva coleção; prova runtime |
| ConversationsService | BFF e operações existentes | Não alterar envio/claim/close/janela; suites de regressão |
| Consulta/public API | Consumidores existentes | Contrato independente preservado; suites atuais |

### Runtime / Rollout Notes

Backend de validação e Playwright usam o mesmo banco dedicado. Falta de runner ou banco impede prova de aplicação; não substituí-la por mocks de navegação. Publicação e envio real externo não integram este recorte.

## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)

- **Status:** findings_integrated; crítica inicial e resolução delta concluídas sem achados materiais pendentes.
- **Review output:** parecer de arquitetura no arquivo architecture-review.json.

### Issue Cards

| Finding ID | Severity | Scenario | Resolution | Status |
| --- | --- | --- | --- | --- |
| ARCH-TL-01 | high | Background zera não lidas; select/reset perde entrada concorrente | marcarLida=false e abertura atômica antes da query; VAL-08 | Integrated |
| ARCH-TL-02 | high | Socket retorna sem evento e thread não recupera | Callback de reconexão + poll da thread, paths de tempoReal explicitados | Integrated |
| ARCH-TL-03 | high | ID menor empatado pode entrar atrás do cursor após cabeça avançar | Cruzar grupo inteiro e conservar piso pendente T em todas as passagens coalescidas; promover só sem trabalho concorrente; teste H>T/ID atrás do cursor | Integrated; verified by critique delta |
| ARCH-TL-04 | medium | Mesmo contexto mistura cursores/metadados/draft | Estado mínimo com owners separados, geração e coalescing; races reais | Integrated |
| ARCH-TL-05 | medium | Índice existente aceito sem plano representativo | EXPLAIN obrigatório recente/profundo/empates mesmo sem migração | Integrated |
| ARCH-TL-06 | medium | Cursor errado não testado porque recurso já é 404 | Fixtures negativas distintas + browser backend real | Integrated |

### Residual Risks

Custo do grupo empatado é medido e cada rodada limitada; inserções concurrentes exigem nova passagem e UI de recuperação. Runners e suites serão provados na implementação. Nenhuma suite green ou aprovação material é presumida.

### Resultado da revisão pré-aprovação

- Revisão de arquitetura: seis achados integrados; crítica e delta encerrados sem achados materiais pendentes.
- Assumption code coherence: go; cinco premissas com fontes reais verificadas.
- Review scope drift: go; 23 seções comparadas, zero mudanças materiais após baseline 649372fb.
- Validação estrutural do TODO: PASS; lifecycle Foundation: exit 0.
- Authority preflight: preflight-go; execution_authority_granted=false.
- Evidências: artifacts/reviews/leadshug-inbox-timeline-20261014/README.md.
- Implementação e testes de aplicação continuam pendentes de autorização; nenhum gate de entrega é reivindicado.

## Additional Architectural Opinions (Required When Path Remains Materially Unclear)

Parecer independente concluído em 2026-10-14, modelo gpt-6.1-sol/max, sem contexto herdado. Recomenda cursor anterior com fronteira inteira de timestamp e recuperação bounded com piso pendente conservado; alternativa bidirecional aumenta contrato sem resolver inserções empatadas. Resultado validado pelo subagent_review_merge; arquivo: artifacts/reviews/leadshug-inbox-timeline-20261014/architecture-review.json.

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

| Trigger | Value | Evidence / Rationale |
| --- | --- | --- |
| complexity | medium | API e UI paginadas |
| blast_radius | cross-stack | BFF + React |
| behavioral_change_or_bugfix | yes | Primeiro carregamento passa a recente |
| changes_public_contract | yes | Contrato BFF consumido pela web |
| touches_auth_or_tenant | yes | Validação de cursor e grants |
| touches_runtime_or_infra | yes | Realtime e harness local |
| touches_tests | yes | API e browser |
| critical_user_journey | yes | Atendimento |
| release_or_promotion_critical | no | Sem release/deploy neste recorte |
| high_severity_plan_review_issue | yes | ARCH-TL-01..03 reportados e integrados na proposta |
| explicit_three_lane_request | no | Revisão solicitada, sem pedido de três lanes |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

- **Critique decision:** required
- **Why this decision:** piso de audit_escalation_guard; API/escopo/realtime e UI com races.
- **Package mode:** bounded-file-set
- **Critique isolation mode:** fresh internal no-context reviewer; resolução delta pelo mesmo crítico independente, sem contexto de implementação.
- **Critique status:** findings_integrated
- **Gate status:** findings_integrated
- **Evidence / reference:** artifacts/reviews/leadshug-inbox-timeline-20261014/critique-round-1.json e critique-resolution.json; primeiro parecer reabriu ARCH-TL-03; delta verificou resolução e retornou findings vazio. Baseline revisada 649372fb.
- **Waiver authority / reference:** none

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-TL-03 | Integrated | useful | yes | project | n/a | Piso pendente T conservado entre passagens/dirty/retry e promoção somente após cobertura sem evento pendente; crítica delta critique-resolution.json confirmou a resolução do plano, agora testada no browser. |

## Gate: Assumption Code Coherence

- **Gate decision:** required
- **Why this decision:** A-01..05 exigem evidência de código real antes de aprovação.
- **Trigger stage:** after critique convergence and before APROVADO
- **Guard scope:** A-01,A-02,A-03,A-04,A-05
- **Gate status:** no_material_findings
- **Findings summary:** revisão independente confirmou A-01/A-02/A-04/A-05 e, no delta, A-03 na query própria do controller público.
- **Evidence / reference:** artifacts/reviews/leadshug-inbox-timeline-20261014/critique-resolution.json; execução do guard registrada no mesmo diretório.
- **Waiver authority / reference:** none

## Approval

- **Approved by:** usuário, APROVADO explícito nesta conversa em 2026-10-14, após revisão e preflight-go.
- **Approval scope:** implementar e validar ST-ATT-01 conforme contrato revisado: BFF paginado/read-neutral, inbox/realtime/recovery/estado e suporte de teste, eventual índice justificado por SQL e documentação/evidência/closeout. Executor routine-executor predeclarado autorizado pelo contrato aprovado.
- **Execution not authorized by approval:** transferência, mídia, estados, CRM/campanhas/Typebot, mudanças da API pública/Consultar, worktrees/cópias auxiliares e deploy/promoção remota de código.
- **Renewed approval required when:** objetivo, contrato, autorização, escopo, riscos ou validação mudarem materialmente; detalhes locais necessários ao mesmo contrato permanecem no TODO.

## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)

Ingestão vinculante após APROVADO realizada em 2026-10-14; fontes da tabela recarregadas para execução, preservando contrato e guards.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| foundation_documentation/project_constitution.md | Produto | BU/conversa e teste real | inferir autorização da UI | Negativos scoped |
| delphi-ai/workflows/docker/todo-contract-refinement-method.md | Planejamento | matrizes/decisões | escopo implícito | Resolver Draft |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | Aprovação | freeze/revisão/evidência | declarar aprovação antes da revisão | Gates pendentes |
| delphi-ai/rules/stacks/nestjs/nestjs-architecture-always-on.md | API | input runtime e serviço de domínio | regra de negócio na UI | Validar cursor/limites |
| delphi-ai/rules/stacks/react/react-architecture-always-on.md | Inbox | owner de estado e races | resposta de conversa antiga | Browser real |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | BFF | contrato/guard | expandir API pública | Contrato local |
| delphi-ai/workflows/react/change-ui-boundary-method.md | UI | estados/acessibilidade | build como única prova | Fluxos browser |

## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Subagent / delegation authorization:** executor autorizado por APROVADO de 2026-10-14; revisão independente já requerida pelo workflow local invocado
- **Git isolation authorization:** not-authorized
- **Guard outcome:** go
- **Guard evidence:** agent_role_routing_guard avaliado em 2026-10-14 para este único tuple; go de routing não é autorização de implementação

Review lane separado: formal-reviewer, architecture_opinion/critique, gpt-6.1-sol, max, declared. Guard de critique retornou go; guard específico será executado antes do dispatch de arquitetura.

## Decision Adherence Validation (Mandatory Before Delivery)

Inspeção de suporte e primeiro parecer independente registrados; aderência Web depende do delta sobre as correções. API/EPS/BCI/RLS mantêm fonte idêntica e evidência do round1.

| Decision | Status | Evidence |
| --- | --- | --- |
| Autorização antes de paginação/cursor; erros scoped | Adherent na inspeção | controller thread/resolver e atendimento.e2e:317/365; API224 passa. |
| Últimas N, N+1, ordem DB e cursor de conversa | Adherent na inspeção | ConversationsService.timeline e atendimento.e2e:282; parser unitário. |
| ACK atômico anterior à query; background neutro | Adherent na inspeção | timeline/updateMany antes findMany; teste PostgreSQL com SELECT bloqueado e mutação negativa. |
| Coleção ativa por ID; piso T conservado e orçamento3 | A confirmar no runtime final/review | Inbox.tsx + timeline.spec.ts forte H>T/lateID/dirty; prova inicial passou. |
| Contexto/metadados/draft/scroll e socket/poll | A confirmar no runtime final/review | IMPL-01..06/09/13 e cenários browser específicos. |
| Índice condicionado ao EXPLAIN | Adherent na inspeção e round1 | pcv-eps.json e evidence/explain-timeline-exact.sql/.log:20382rows/1000ties; candidato composto piorou buffers e foi removido, sem migração; custo profundo residual explícito. |
| API pública/Consultar e outras stories fora | Adherent na inspeção | Sem diff nesses consumidores; regressões API224. |

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)

| Canonical owner / decision | Implementation | Status |
| --- | --- | --- |
| inbox-and-conversations / thread BFF paginada | controller + timeline-pagination + ConversationsService.timeline | Contrato consolidado em4cabc467 antes do código; implementação API validada. |
| inbox-and-conversations / recuperação e contexto | Inbox + timeline + tempoReal | Contrato preservado; consolidação Verified depende de browser final e review. |
| identity-and-tenancy / BU e grant | Resolver/AccessService existentes | Sem mudança canônica; negativos reais de escopo passaram. |
| audit-and-history / autoria e ações | responder/claim/close existentes | Sem alteração contratual; persistência e regressões cobertas. |

Round1 confirmou os owners e o contrato API; delta independente julgará a resolução dos achados Web e as novas provas.

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface | Focus | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| Orquestrador / inspeção bounded | API auth/read-state e UI races; runner/frescor | running | implementation-observations.md; execution-evidence.md | IMPL-01..14 | Correções no mesmo TODO; browser final, SQL e reviews ainda pendentes. |
| CI API local | Leaf scripts do job tocado | passed | evidence/api-ci-light-revision2-20261015.log; evidence/api-e2e-authority.log; test-surface-admission.md | 0 falhas na execução final | generate/lint/build/unit115 e PostgreSQL224 adicionais, serializados. |
| Revisão independente | Aderência, segurança, desempenho e provável P1/P2 | pending | delivery-package.md preparado | Ainda não executada | Não declarar clean antes do parecer e tratamento de achados. |

## Rule-Spirit Anti-Pattern Hunt

| Rule Surface | Lens | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| NestJS / parser e limites | Validação runtime, grant antes cursor, ACK e queries bounded | running | código + API224; test-quality-static-api.log | Inspeção sem bypass; avaliação independente pendente | Fonte/guards/session/persistência reais, sem alterar público/Consultar. |
| React / Inbox e socket | Owner/generation, piso T, cursor, lifecycle e poll | running | implementation-observations.md e cenários browser | IMPL-01..06/09/13/14 | Correções fiéis ao contrato; aguardar prova final. |
| Scan heurístico API/Web | Domínios/targets e bypass disfarçado | running | scan-triage-api.json e scan-triage-web.json | API30 observações/15 loci; Web42/21 na captura final só de fontes | Proposta by-design para fixtures localhost/.test e regex estática preexistente; sem allowlist. Rerun na fonte final e revisão independentes pendentes. |

## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-TL-01..03 | high | release-blocker | fix in current TODO | Contrato de leitura/recuperação pertence à mesma story | fixed | architecture-review.json e Proposed API Contract, a verificar na crítica |
| ARCH-TL-04..06 | medium | release-blocker | fix in current TODO | Estado/consulta/provas necessários ao mesmo contrato | fixed | architecture-review.json e testes planejados, a verificar na crítica |
| ARCH-DEL-01 | medium | release-blocker | fix in current TODO | Budget3 por rodada deve abranger coalescing; evento não renova automaticamente consultas | open | delivery-adherence-round-1.json; executor retoma com request-count/single-flight regressions |
| ARCH-DEL-02 | medium | release-blocker | fix in current TODO | Thread inicialmente vazia e notificação entre rodadas devem conservar restart pendente até fetch recente | open | delivery-adherence-round-1.json; cenário>150 com evento entre rodadas e IDs/metadata |
| ARCH-DEL-03 | medium | release-blocker | fix in current TODO | Notificação durante abertura pertence à geração selecionada e deve recuperar sem esperar outroevento/poll | open | delivery-adherence-round-1.json; resposta real atrasada+IN/reconnect e unread |
| TQA-TL-01 | medium | release-blocker | fix with ARCH-DEL-01 | Mesmo defeito de budget/single-flight; harness deve contar requests e passagens em voo, não só comparar IDs | open | delivery-tqa-round-1.json; duplicata sem novo escopo |
| TQA-TL-02 | medium | release-blocker | fix in current TODO | Prova de geração exige draft/erro/scroll/metadados do destino em trocas conversa/BU com sucesso/falha/backfill antigos | open | delivery-tqa-round-1.json; novos asserts reais dentro de VAL-05 |
| TQA-EVID-03 | low | release-blocker | retain exact CI leaf outputs now | Lacuna de evidência do claim CI atual; repetir somente generate/lint/build/unit API com logs imutáveis antes do browser final | open | delivery-tqa-round-1.json; VAL-02, sem repetir API224 unchanged |
| ARCH-DEL-01-ERR | medium | release-blocker | fix with ARCH-DEL-01 | Variante objetiva: saldo era debitado após await; falha+dirty não debitava e permitia mais de3tentativas. Consumir no despacho e provar3aborts+eventos sem4aautomática; erro histórico com dirty deve conservar restart recente, não consumir a notificação ao retomar cursor antigo | open | Inspeção de suporte na revisão2, mesmo contrato/owner; prova negativa em revisão3 |

## TODO Closeout Disposition

- **Disposition:** keep-active
- **Disposition reason:** contrato aprovado em implementação, provas de entrega ainda necessárias.
- **Post-commit/push status:** planejamento/aprovação e contrato canônico publicados até4cabc467; código em feature local e evidência de entrega ainda não commitados.
- **Next path/status action:** implementar, validar e revisar; mover para completed somente com evidência/guardas de closeout.

## Security Risk Assessment (Mandatory Before Delivery)

- **Gate decision:** required
- **Why this decision:** cursor, grants e mudança de contexto.
- Autorizar primeiro; resolver cursor na conversa; limitar sua forma/tamanho e queries. Testar cursor de outra conversa autorizada, outra BU sem grant no mesmo tenant e outro tenant, separadamente.
- Banco descartável dedicado; bootstrap com sessão/guards/domínio/persistência reais e dublês só nas portas externas. Não mascarar BFF nem expor suporte de teste em produção.
- API224 comprovou precedência401/404, cursor scoped400 e ausência de escrita em query inválida; testes negativos distintos e readback PostgreSQL. Parser rejeita array/repetição e limite/tamanho inválidos. Bootstrap/fixtures estão em test/, recusam DB não descartável, sem rotas de suporte em produção. Revisão independente de segurança segue pendente, sem alegação de pentest ou provider externo validado.

## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)

- **Gate decision:** required
- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** medium
- **Why this level:** paginação e cursores alteram queries; abertura e entrada concorrem na contagem de não lidas; contexto/realtime/ações assíncronas atualizam o histórico visível. Nenhuma promessa de SLO/capacidade foi aprovada.
- **Current delivery stage at review time:** Pending
- Registro de classificação na execução do contrato aprovado; não expande funcionalidade nem reduz obrigações de validação.

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `medium` | `EPS-QUERY-SHAPE-CHANGED` | `before_local_implemented` | `EPS-E2` | `running` | Custo depende da distribuição real de mensagens. | `none` |
| `FRC` | `frontend-race-condition-validation` | `required` | `medium` | `FRC-STALE-RESPONSE` | `before_local_implemented` | `FRC-E2` | `running` | Estados assíncronos requerem provas determinísticas de overlap. | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `required` | `medium` | `BCI-LOST-UPDATE-RISK` | `before_local_implemented` | `BCI-E2` | `running` | Reconhecimento e incrementos devem linearizar no PostgreSQL. | `none` |
| `RLS` | `runtime-load-stress-validation` | `recommended` | `medium` | `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED` | `before_production_ready` | `RLS-E1` | `running` | Amostra local não estabelece capacidade de produção. | `none` |

### Lane Details

#### EPS

- **Trigger rationale:** consulta recente e keyset mudam ordenação, limite e predicado; classificar acesso, auditar caminhos e registrar EXPLAIN recente/profundo/empates mesmo sem migração.
- **Recorded at (UTC):** `2026-10-15T03:36:56Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; execução observada e artefato consolidado, aguardando avaliação independente antes de passed.
- **Evidence object:**
  - `evidence_type`: `explain`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `explain-exact-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-eps.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `f20722cdaae0a7cddea80dbcb2df929035d742f47b49ab7f64a17444a9a79c83`
  - `sample_profile_id`: `EPS-SP-STRONG`
  - `acceptance_rule_id`: `EPS-A2`
  - `result_summary`: `Measured recent/deep/tied pages on20382 rows,1000 ties; existing index retained after candidate trial. Independent judgment pending.`
  - `reviewer_id`: `delivery-adherence-native`

#### FRC

- **Trigger rationale:** backfill, recuperação, fechamento, envio e troca de contexto podem sobrepor respostas; uma recuperação em voo e contexto/geração/versionamento de draft protegem o estado.
- **Recorded at (UTC):** `2026-10-15T04:25:48Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; provas finais revision3 executadas em fonte idêntica, aguardando julgamento independente antes de passed.
- **Evidence object:**
  - `evidence_type`: `source-owned-playwright-real-backend-races`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-chromium-disposable`
  - `run_id`: `web-authority-revision3-final-frc3-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-frc.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `9e0a448cc4d1cb625c350355e7f4f08c7b138db4116a29471e92300f9a1798b7`
  - `sample_profile_id`: `FRC-SP-M`
  - `acceptance_rule_id`: `FRC-A1`
  - `result_summary`: `Full34/34 and FRC3/3 passed on identical current source/build; shared3-attempt budget incl failures, retained T/restart, opening and empty notifications, context success/error/backfill covered. Independent delta judgment pending.`
  - `reviewer_id`: `delivery-adherence-delta-native`

#### BCI

- **Trigger rationale:** o UPDATE de reconhecimento precede a query, concorrendo com incrementos de entrada; incrementos posteriores devem permanecer não lidos e leituras de background nunca escrever.
- **Recorded at (UTC):** `2026-10-15T03:36:56Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; execução observada e artefato consolidado, aguardando avaliação independente antes de passed.
- **Evidence object:**
  - `evidence_type`: `postgresql-overlap-probe`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `bci-ack-barrier-canonical-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-bci.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `93eeac265b3c77b17e6fee0cbd20223a56cbe44fe17489052b9b4feeffa37995`
  - `sample_profile_id`: `BCI-SP-M`
  - `acceptance_rule_id`: `BCI-A1`
  - `result_summary`: `Three deterministic real PostgreSQL barrier batches retain10 increments after ACK; regression mutation fails10vs0 and exact source restoration passes. Independent judgment pending.`
  - `reviewer_id`: `delivery-adherence-native`

#### RLS

- **Trigger rationale:** consultas sensíveis a índice e recuperação realtime têm pressão de runtime; amostra de leitura neutra medirá erros, limites e latência sem promessa de SLO.
- **Recorded at (UTC):** `2026-10-15T03:39:44Z`
- **Executor ID:** `/root/timeline_executor_resume`
- **State transition:** pending -> running; amostra executada, revisão independente pendente antes de passed.
- **Evidence object:**
  - `evidence_type`: `one-stage-authenticated-read-load`
  - `environment_id`: `principal-checkout-linux-node22-postgresql16-disposable`
  - `run_id`: `rls-read-stage1-20261015`
  - `artifact_uri`: `foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-rls.json`
  - `artifact_schema_version`: `pcv-1`
  - `artifact_sha256`: `b9b05d0bd9127e4347e04685a91379924153c7c3a4f9b7445e8fa5ed9f548b3c`
  - `sample_profile_id`: `RLS-SP-L`
  - `acceptance_rule_id`: `RLS-A1`
  - `result_summary`: `30/30 reads,5 concurrent×6; p50 23.36ms,p95 64.26ms,max68.5ms; page50,unread7 unchanged,251 messages unchanged,foreign malformed request404. Review pending, no production SLO claim.`
  - `reviewer_id`: `delivery-adherence-native`

## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)

Pendentes contrato, runner, provas PostgreSQL/browser e revisões. Não reivindicar implementação ou fechamento com evidência histórica de outro TODO.

## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)

- **Audit decision:** required
- **Why this decision:** API/escopo/consulta e UI interativa com races
- **Audit status:** running
- **Critique status:** running
- **Evidence / reference:** revisão de entrega após testes completos; pacote de planejamento não substitui TQA. O roteamento technical_review exige gpt-5.6-terra. Na retomada, o catálogo nativo do Codex confirmou esse modelo, embora não seja selecionável via ferramenta collaboration. Será usado o runner interno subagent_review_run.py com o modelo prescrito e effort max; guard específico go em artifacts/tmp/inbox-timeline-execution/routing-tqa-native.json e probe nativo ephemeral/read-only exit0 MODEL_AVAILABLE (native-model-probe-events.jsonl). Exceção/substituição não é necessária e não foi presumida.
- **Waiver authority / reference:** none

Runner interno codex ephemeral/read-only/no-context gpt-5.6-terra/max terminou com turn.completed, JSON canônico validado/merge. Evidência: delivery-tqa-round-1.json/merge. TQA-TL-01 duplica a proteção de budget/single-flight ARCH-DEL-01; TQA-TL-02 requer asserts no destino para draft/erro/scroll após troca de contexto; TQA-EVID-03 registra falta de stdout API CI. Todos serão integrados no mesmo TODO antes de review delta; sem waiver.

## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)

- **Final review decision:** required
- **Why this decision:** API/escopo/consulta e UI interativa com races
- **Final review status:** not_run
- **Critique status:** not_run
- **Evidence / reference:** pacote ainda prepared-pre-freeze; executar revisão no gate correspondente
- **Waiver authority / reference:** none

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** not_needed
- **Cutover audit status:** no_material_findings
- **Why this decision:** recorte de paginação no BFF/inbox atuais; não há substituição de runtime legado, dual-read/dual-write ou exceção de compatibilidade temporária.
- **Evidence / reference:** Out of Scope e pareceres de arquitetura/crítica mantêm o produto atual como alvo único; nenhuma auditoria de cutover reivindicada.

## Delivery Confidence Gate (Required for `✅ Production-Ready`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Module Consolidation Gate (Required Before `Completed`)

Pendente no gate de execução/revisão correspondente; nenhuma evidência ou promoção reivindicada neste Draft.

## Commands (Run Locally)

Comandos exatos e resultados efetivos: artifacts/reviews/leadshug-inbox-timeline-20261014/execution-evidence.md. API generate/lint/build/unit115/E2E224 passou em Node22/PG16 descartável; EPS/BCI/RLS executados com artefatos; Web revision3 e revisões de entrega ainda abertas. Nunca apontar helpers para bancos operacionais.

## Files Expected (Compatibility Note)

O contrato de paths e baselines está no Diff Expectation Contract.

## COMENTÁRIO:

n/a; nenhum comentário pendente do usuário neste arquivo.


```

## foundation_documentation/project_constitution.md
```
# LeadsHug — Project Constitution
**Version:** 1.0

## Purpose and stack

Esta constituição governa o LeadsHug, uma central multi-tenant de relacionamento por WhatsApp. O stack ativo
é NestJS, React, PostgreSQL, Prisma, Docker e Railway.

## Authority hierarchy

1. Documentos canônicos vigentes deste foundation. Uma decisão `Accepted` só se torna efetiva depois que todos os seus alvos canônicos nomeados forem consolidados; sua direção passa a valer por meio desses alvos atualizados, nunca por sobreposição do registro de decisão. Antes disso, o registro preserva racional e proveniência, mas não compete com a verdade corrente.
2. TODO tático ativo e aprovado.
3. Código e testes do repositório LeadsHug.
4. Regras e workflows reutilizáveis do `leadshug-engineering`.

Quando houver conflito, a regra mais específica do produto prevalece sobre a regra genérica de engenharia.

## System invariants

- API, DTO and response projection changes require matching contract-test expectation updates in the same TODO.
- Prisma schema changes require an applicable versioned migration; changes to either the schema or migration files require `prisma migrate deploy` and CI database validation.
- Environment, port and topology changes require local validation with the same configuration as CI.
- Web-flow changes require Playwright against a freshly built bundle and the real validation backend using the same `DATABASE_URL` and resolved API port/endpoint as the CI-equivalent job, without exposing secrets.

- Toda implementação possui um TODO ativo, escopo, Definition of Done e evidência de validação.
- A Mantenedora contém Setores; a Business Unit é o número de WhatsApp.
- Grants e leituras são sempre filtrados pela BU e pela conta correta; vazamento entre tenants é falha crítica.
- Canal oficial e não oficial são transportes da BU; a conversa é unificada pelo par BU/Contato.
- BFF, API pública, API interna e webhooks são superfícies distintas, com autenticação própria.
- Domínio e regras de negócio pertencem ao backend NestJS; React consome contratos explícitos.
- Persistência usa PostgreSQL via Prisma; acesso ao banco não deve contornar a fronteira de domínio.
- Serviços executam em Docker e são promovidos pela topologia Railway declarada no projeto.
- Histórico de atendimento é persistente, consultável conforme permissão e auditável.
- Templates, disparos, CRM e campanhas só entram em execução mediante TODO e contrato próprios.

## TODO governance

`backlog/` registra candidatos não aprovados e é separado de `todos/active/`. `todos/active/` contém contratos
táticos vivos, mas sua localização nunca concede execução: somente `APROVADO` explícito e o authority guard em
`go` a concedem. Um TODO concluído deve conter evidência específica, validação e referência de branch/commit.

O lifecycle canônico em [evolution_lifecycle.md](evolution_lifecycle.md) define schemas, transições, papéis
neutros de fornecedor e owner singular por campo. Backlog possui disposição/próximo gate; roadmap possui tema,
horizonte, resultado, dependências e exit gate; módulos possuem verdade local estável; TODOs possuem
aprovação/execução/evidência; decisões possuem racional/histórico; briefs e artifacts são evidência, não
autoridade concorrente.

## Profiles and handoffs

- Genesis define a primeira arquitetura documental.
- Strategic/CTO-Tech-Lead governa constituição, lifecycle e roadmap.
- Operational/Coder implementa backend, frontend e testes por TODO.
- Operational/DevOps governa Docker, Railway, CI e runtime.
- Assurance valida qualidade, aderência e segurança.

## Lifecycle roles

- A autoridade humana de decisão valida escopo, produto e aprovação material.
- O strategic steward governa constituição, lifecycle e roadmap.
- O module owner governa ownership, invariantes e contratos locais.
- O TODO owner/executor executa somente o contrato aprovado e mantém suas evidências.
- O assurance reviewer valida qualidade, aderência e segurança sem adquirir autoridade de produto.

Ferramentas, agentes e fornecedores concretos são adapters desses papéis, não autoridade de produto.

## Explicit non-goals

Não ativar capacidades de stack não declaradas no topology do LeadsHug sem decisão documental específica.

```

## foundation_documentation/modules/inbox-and-conversations.md
```
# Module: Inbox and Conversations
**Version:** 1.0

Owns contacts, conversations, messages, inbox, assignment and service responses across official and unofficial
WhatsApp transports.

## Invariants

- A conversation is unique by BU and contact, not by transport.
- Incoming webhook processing is idempotent.
- Outbound responses enforce the platform window and channel capability.

## API Endpoint Definitions

BFF routes use `/api/bff`; public integrations use `/api/v1`; webhook contracts use `/webhooks`.

## Contrato aprovado da timeline da inbox

Aprovado pelo usuário em 2026-10-14 no [TODO ST-ATT-01](../todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md). Este módulo é o owner do contrato; implementação e verificação são registradas no TODO. Estado de verificação inicial: Documented; nenhuma implementação/evidência de execução reivindicada neste momento.

### Thread paginada BFF v1 — GET /api/bff/conversations/:id/messages

- Sessão e grant ATENDENTE ou superior na BU; resolver/autorizar a conversa antes de validar ou consultar cursores. Sem sessão: 401. Recurso fora do escopo: 404, inclusive com query/cursor malformado.
- Query: `limite` inteiro decimal 1..100, padrão 50; `antes` cursor opaco opcional, máximo 256 caracteres; `marcarLida` booleano textual `true|false` opcional.
- Sem `antes`, `marcarLida` ausente equivale a true para conservar abertura humana. Cliente usa explicitamente false para refresh, pós-ação, poll, reconexão e recuperação. Com `antes`, leitura é sempre false; `marcarLida=true` explícito com `antes` é inválido. Valores inválidos, query repetida/array e cursor inexistente/alheio à conversa autorizada: 400 `PAGINACAO_INVALIDA`; query desconhecida é ignorada e não altera comportamento.
- A marcação de abertura é uma única atualização atômica de `unreadCount=0`, depois da autorização e antes de buscar a página. Essa escrita é a fronteira de reconhecimento: incrementos de entrada serializados depois dela permanecem não lidos. Não fazer select-depois-reset nem adicionar estado de leitura por mensagem. Se abertura/marcação falhar, não executar uma escrita posterior compensatória que apague entradas novas.
- Resposta conserva `conversa`, `janela` e `messages` e acrescenta `paginacao: { limite, temAnteriores, cursorAnterior }`.
- Sem cursor, buscar as últimas N mensagens. Responder páginas em ordem crescente pelo par `(createdAt,id)`; ordenação de ID segue a comparação do banco.
- Cursor versionado identifica a mensagem-âncora; resolver seus dados somente na conversa autorizada. Paginação anterior usa comparação estrita do par, busca no máximo N+1 registros e nunca escreve não lidas.
- `cursorAnterior` representa o registro mais antigo da página quando há continuação; caso contrário null. Vazio: messages vazio, temAnteriores false, cursor null.
- API pública e Consultar mantêm seus contratos e efeitos atuais. Dublês no backend de testes substituem somente portas externas; não há flag de teste no código de produção.

### Recuperação e estado da inbox

- Manter somente a coleção da conversa ativa por ID; liberar contexto/páginas quando BU/conversa mudar. O cursor histórico pertence ao backfill e não é substituído pelo cursor da página recente de um refresh.
- Na atualização, capturar uma fronteira fixa T igual ao timestamp da mensagem mais recente conhecida antes da passagem. Buscar página recente sem marcar leitura e caminhar para trás até alcançar timestamp estritamente menor que T, ou esgotar mensagens. Incluir integralmente o grupo empatado em T; encontrar um ID conhecido não encerra a recuperação.
- Se a coleção ainda é vazia, atualização funciona como página inicial sem efeito de leitura. Separar o piso de cobertura confirmado do maior timestamp mesclado. A recuperação captura um piso pendente T e toda passagem coalescida/retomada/retry conserva esse piso original, mesmo quando a cabeça já avançou para H maior que T.
- Evento durante a recuperação marca uma nova passagem necessária desde a página recente, ainda com o piso pendente T; terminar a caminhada atual não confirma cobertura. Só promover o piso confirmado quando uma passagem atravessar todo T sem evento/trabalho concorrente pendente. Se houver dirty/pending, conservar T e a indicação de atualização, com o mesmo orçamento de três queries por rodada. Não promover pelo máximo da coleção nem por um poll enquanto houver recuperação pendente.
- A recuperação cobre inserções novas, incluindo ID menor em T atrás de um cursor já percorrido. Importação/backdating de histórico fora do grupo de cobertura permanece fora deste recorte. Mensagens mais recentes mescladas não eliminam essa prova de continuidade.
- Recuperação tem cursor/progresso próprios e uma única passagem em voo por contexto. Cada rodada executa no máximo três queries de página, separadas e bounded; uma rodada incompleta mantém indicação visível de atualização/lacuna e cursor para `Continuar atualização`/retry. Novo evento não reinicia seu orçamento; polling pode retomar a rodada pendente. Não afirmar continuidade até cruzar toda a fronteira.
- Disparadores: evento de mensagem coalescido, socket restabelecido sem depender de outro evento, pós-ação e poll da thread selecionada a cada 60 segundos. Registrar callback de conexão no helper existente; preservar seus consumidores.
- Backfill altera somente coleção e cursor histórico. Metadados conversa/janela só são aplicados pela leitura atual com versão/frescor adequado; uma página anterior atrasada não desfaz close, troca de status ou atualização de janela.
- Todo efeito assíncrono captura BU/conversa/geração. Resposta, erro, scroll e limpeza do texto enviado são ignorados se contexto mudou; limpeza de draft também verifica que o usuário não digitou outro texto enquanto o envio estava pendente.
- Histórico anterior preserva posição do usuário. Mensagens novas não forçam deslocamento quando ele lê trecho antigo. Estados de loading, vazio, fim, recuperação pendente, falha/retry e acesso perdido são visíveis e operáveis por teclado.

```

## Exact generation1 -> generation3 delta web-app/src/telas/Inbox.tsx
```diff
--- generation1/web-app/src/telas/Inbox.tsx
+++ generation3/web-app/src/telas/Inbox.tsx
@@ -18,7 +18,14 @@
   dirty: boolean;
   eventos: number;
   emVoo: boolean;
+  paginasRestantes: number;
   vazio?: boolean;
+}
+
+interface InvalidacaoDeAbertura {
+  id: string;
+  geracao: number;
+  eventos: number;
 }
 
 export default function Inbox({ eu }: { eu: Eu }) {
@@ -40,6 +47,7 @@
   const abaAtual = useRef('QUEUED');
   const threadAtual = useRef<Thread | null>(null);
   const recuperacao = useRef<Recuperacao | null>(null);
+  const invalidacaoAbertura = useRef<InvalidacaoDeAbertura | null>(null);
   const executarRecuperacaoRef = useRef<() => Promise<void>>(async () => {});
   const versaoMetadados = useRef(0);
   const bolhas = useRef<HTMLDivElement>(null);
@@ -92,25 +100,25 @@
 
   const executarRecuperacao = useCallback(async () => {
     const r = recuperacao.current;
-    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
+    if (!r || r.emVoo || r.paginasRestantes <= 0 || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
     r.emVoo = true;
     const eventosNoInicio = r.eventos;
     r.dirty = false;
-    let paginas = 3;
     let cruzou = false;
     try {
       if (r.vazio) {
-        if (r.cursor === null && paginas > 0) {
+        if (r.cursor === null && r.paginasRestantes > 0) {
           const versao = versaoMetadados.current;
+          r.paginasRestantes -= 1;
           const inicial = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
           if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
           aplicarPaginaRecente(r.id, r.geracao, versao, inicial);
           r.cursor = inicial.paginacao.cursorAnterior;
-          paginas -= 1;
           if (!inicial.paginacao.temAnteriores) r.cursor = null;
         }
-        while (r.cursor && paginas > 0) {
+        while (r.cursor && r.paginasRestantes > 0 && !r.dirty) {
           const cursor = r.cursor;
+          r.paginasRestantes -= 1;
           const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
           if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
           const atual = threadAtual.current;
@@ -120,7 +128,6 @@
             paginacao: pagina.paginacao,
           });
           r.cursor = pagina.paginacao.cursorAnterior;
-          paginas -= 1;
         }
         if (r.eventos !== eventosNoInicio || r.dirty) {
           r.cursor = null;
@@ -133,17 +140,18 @@
         }
         return;
       }
-      if (r.cursor === null) {
+      if (r.cursor === null && r.paginasRestantes > 0) {
         const versao = versaoMetadados.current;
+        r.paginasRestantes -= 1;
         const recente = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
         if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
         aplicarPaginaRecente(r.id, r.geracao, versao, recente);
         r.cursor = recente.paginacao.cursorAnterior;
-        paginas -= 1;
         cruzou = cruzouPiso(recente.messages, r.piso) || !recente.paginacao.temAnteriores;
       }
-      while (!cruzou && r.cursor && paginas > 0) {
+      while (!cruzou && r.cursor && r.paginasRestantes > 0 && !r.dirty) {
         const cursor = r.cursor;
+        r.paginasRestantes -= 1;
         const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
         if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
         const atual = threadAtual.current;
@@ -152,7 +160,6 @@
           messages: mesclarMensagens(atual.messages, pagina.messages),
         });
         r.cursor = pagina.paginacao.cursorAnterior;
-        paginas -= 1;
         cruzou = cruzouPiso(pagina.messages, r.piso) || !pagina.paginacao.temAnteriores;
       }
 
@@ -168,12 +175,13 @@
       }
     } catch (e) {
       if (r.geracao === geracao.current && r.id === conversaAtual.current) {
+        if (r.dirty || r.eventos !== eventosNoInicio) r.cursor = null;
         setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível atualizar o histórico. Tente novamente.');
         setRecuperacaoPendente(true);
       }
     } finally {
       r.emVoo = false;
-      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.geracao === geracao.current) {
+      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.paginasRestantes > 0 && r.geracao === geracao.current) {
         queueMicrotask(() => void executarRecuperacaoRef.current());
       }
     }
@@ -184,28 +192,40 @@
   const reconciliar = useCallback(() => {
     const thread = threadAtual.current;
     const id = conversaAtual.current;
-    if (!thread || !id) return;
+    if (!id) return;
+    if (!thread) {
+      const abertura = invalidacaoAbertura.current;
+      if (abertura?.id === id && abertura.geracao === geracao.current) abertura.eventos += 1;
+      return;
+    }
     let r = recuperacao.current;
     if (!r || r.id !== id || r.geracao !== geracao.current) {
       const mensagens = thread.messages;
       if (mensagens.length === 0) {
-        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, vazio: true };
+        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3, vazio: true };
         recuperacao.current = r;
         void executarRecuperacao();
         return;
       }
       const piso = mensagens.reduce((max, m) => Date.parse(m.createdAt) > Date.parse(max) ? m.createdAt : max, mensagens[0].createdAt);
-      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false };
+      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3 };
       recuperacao.current = r;
       setRecuperacaoPendente(true);
     } else {
       r.dirty = true;
       r.eventos += 1;
-      if (!r.emVoo && !r.vazio) r.cursor = null;
+      if (!r.emVoo) r.cursor = null;
       setRecuperacaoPendente(true);
     }
+    if (r.paginasRestantes > 0) void executarRecuperacao();
+  }, [aplicarPaginaRecente, executarRecuperacao]);
+
+  const iniciarRodadaAutorizada = useCallback(() => {
+    const r = recuperacao.current;
+    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
+    r.paginasRestantes = 3;
     void executarRecuperacao();
-  }, [aplicarPaginaRecente, executarRecuperacao]);
+  }, [executarRecuperacao]);
 
   useEffect(() => {
     carregarListaRef.current = carregarLista;
@@ -216,11 +236,11 @@
     void carregarLista().catch(ignorarSessaoMorta);
     const t = setInterval(() => {
       void carregarLista().catch(ignorarSessaoMorta);
-      if (recuperacao.current) void executarRecuperacaoRef.current();
+      if (recuperacao.current) iniciarRodadaAutorizada();
       else reconciliar();
     }, 60_000);
     return () => clearInterval(t);
-  }, [buId, aba, carregarLista, reconciliar]);
+  }, [buId, aba, carregarLista, reconciliar, iniciarRodadaAutorizada]);
 
   useEffect(() => {
     // Espera a lista inicial de BUs e mantém o socket apesar de filtros, BUs ou
@@ -239,6 +259,7 @@
     buAtual.current = novoBu;
     conversaAtual.current = null;
     recuperacao.current = null;
+    invalidacaoAbertura.current = null;
     guardarThread(null);
     setAbrindo(false);
     guardarTexto('');
@@ -254,6 +275,7 @@
     const gen = ++geracao.current;
     conversaAtual.current = id;
     recuperacao.current = null;
+    invalidacaoAbertura.current = { id, geracao: gen, eventos: 0 };
     versaoMetadados.current += 1;
     guardarThread(null);
     setAbrindo(true);
@@ -268,9 +290,13 @@
       response.messages = mesclarMensagens(response.messages);
       guardarThread(response);
       setAbrindo(false);
+      const invalidacao = invalidacaoAbertura.current;
+      invalidacaoAbertura.current = null;
       void carregarLista().catch(ignorarSessaoMorta);
+      if (invalidacao?.id === id && invalidacao.geracao === gen && invalidacao.eventos > 0) reconciliar();
     } catch (e) {
       if (gen === geracao.current) {
+        invalidacaoAbertura.current = null;
         guardarThread(null);
         setAbrindo(false);
         setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível carregar a conversa.');
@@ -382,7 +408,7 @@
                   </button>
                 : <span className="suave">Início do histórico</span>}
               {recuperacaoPendente && <span className="suave" role="status">Atualização pendente. O histórico pode ter uma lacuna.</span>}
-              {recuperacaoPendente && <button onClick={() => void executarRecuperacao()}>Continuar atualização</button>}
+              {recuperacaoPendente && <button onClick={() => iniciarRodadaAutorizada()}>Continuar atualização</button>}
             </div>
             <div className="bolhas" ref={bolhas} aria-live="polite">
               {aberta.messages.map((m: Mensagem) => <div key={m.id} data-message-id={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>

```

## Exact generation1 -> generation3 delta web-app/e2e/timeline.spec.ts
```diff
--- generation1/web-app/e2e/timeline.spec.ts
+++ generation3/web-app/e2e/timeline.spec.ts
@@ -42,10 +42,10 @@
   const webhook = await response.json() as { status: number; body: string };
   expect(webhook.status).toBe(200);
   expect(webhook.body).toBe('EVENT_RECEIVED');
+  return webhook;
 }
 
 test.describe('timeline da inbox com backend e PostgreSQL reais', () => {
-  test.describe.configure({ timeout: 120_000 });
   let pageErrors: string[];
   test.beforeEach(async ({ page }) => {
     pageErrors = [];
@@ -55,6 +55,13 @@
 
   test('expõe o estado de abertura enquanto a primeira página aguarda o backend', async ({ page, request }) => {
     const fixture = await seed(request, 3);
+    let mensagensRecebidas = 0;
+    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
+      try {
+        const frame = JSON.parse(String(payload)) as { tipo?: string; conversaId?: string };
+        if (frame.tipo === 'mensagem' && frame.conversaId === fixture.conversationId) mensagensRecebidas += 1;
+      } catch { /* frames de conexão não são mensagens */ }
+    }));
     await login(page, fixture.email, fixture.password, fixture.businessUnitId);
     let liberar!: () => void;
     let iniciou!: () => void;
@@ -70,8 +77,14 @@
     await page.getByRole('button', { name: 'Cliente Timeline' }).click();
     await solicitacao;
     await expect(page.getByRole('status').filter({ hasText: 'Abrindo conversa…' })).toBeVisible();
+    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-opening-invalidation', text: 'mensagem chega durante abertura atrasada' });
+    await expect.poll(() => mensagensRecebidas).toBe(1);
     liberar();
-    await expect(page.locator('.bolha')).toHaveCount(3);
+    await expect(page.locator('.bolha')).toHaveCount(4);
+    const expected = await audit(request, fixture.conversationId);
+    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
+    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
+    expect(expected.unreadCount).toBe(1);
   });
 
   test('abre a página recente, carrega todas as páginas anteriores e preserva posição', async ({ page, request }) => {
@@ -165,6 +178,37 @@
     expect(expected.unreadCount).toBe(1);
   });
 
+  test('retoma thread vazia após evento entre rodadas e inclui toda a cabeça sem reler', async ({ page, request }) => {
+    const fixture = await abrirTimeline(page, request, 0);
+    let paginasRecuperacao = 0;
+    const rotaRecuperacao = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.get('marcarLida') === 'false';
+    await page.route(rotaRecuperacao, async (route) => {
+      paginasRecuperacao += 1;
+      await route.continue();
+    });
+    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 160, createdAt: Date.now() + 10_000 } });
+    expect(burst.status()).toBe(201);
+    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-empty-first-head', text: 'primeira cabeça da thread vazia' });
+    const pending = page.getByText('Atualização pendente. O histórico pode ter uma lacuna.');
+    await expect(pending).toBeVisible({ timeout: 25_000 });
+    await expect(page.locator('.bolha')).toHaveCount(150);
+    expect(paginasRecuperacao).toBe(3);
+
+    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-empty-between-rounds', text: 'evento enquanto a thread vazia está pausada' });
+    await expect.poll(async () => (await audit(request, fixture.conversationId)).unreadCount).toBe(2);
+    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
+    for (let i = 0; i < 5 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
+      await page.getByRole('button', { name: 'Continuar atualização' }).click();
+      await page.waitForTimeout(100);
+    }
+    await expect(pending).toHaveCount(0, { timeout: 25_000 });
+    const expected = await audit(request, fixture.conversationId);
+    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
+    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
+    expect(ids).toHaveLength(162);
+    expect(expected.unreadCount).toBe(2);
+  });
+
   test('preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido', async ({ page, request }) => {
     const fixture = await seed(request, 251, true);
     let mensagensRecebidas = 0;
@@ -178,40 +222,68 @@
     await page.getByRole('button', { name: 'Cliente Timeline' }).click();
     await expect(page.locator('.bolha')).toHaveCount(50);
     let pagesBeforeCursor = 0;
+    let requestsRecovery = 0;
+    let requestsAtivo = 0;
+    let maxRequestsAtivo = 0;
+    let captureRequests = true;
     let liberar!: () => void;
     let aguardeSegundaPagina!: () => void;
+    let aguardeTerceiraPagina!: () => void;
     const continua = new Promise<void>((resolve) => { liberar = resolve; });
     const segundaPagina = new Promise<void>((resolve) => { aguardeSegundaPagina = resolve; });
+    const terceiraPagina = new Promise<void>((resolve) => { aguardeTerceiraPagina = resolve; });
     let lateId = '';
     const piso = new Date('2026-10-14T12:00:00.000Z').toISOString();
-    const rotaPaginaAnterior = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
-    await page.route(rotaPaginaAnterior, async (route) => {
-      pagesBeforeCursor += 1;
-      if (pagesBeforeCursor !== 2) return route.continue();
-      const response = await route.fetch();
-      const cursor = new URL(route.request().url()).searchParams.get('antes')!;
-      const cursorPayload = JSON.parse(Buffer.from(cursor.slice(3), 'base64url').toString('utf8')) as { m: string };
-      const min = BigInt(`0x${cursorPayload.m.replaceAll('-', '')}`);
-      const max = BigInt(`0x${fixture.expectedIds.at(-1)!.replaceAll('-', '')}`);
-      lateId = ((min + max) / 2n).toString(16).padStart(32, '0').replace(/(.{8})(.{4})(.{4})(.{4})(.{12})/, '$1-$2-$3-$4-$5');
-      expect(lateId > cursorPayload.m).toBe(true);
-      expect(lateId < fixture.expectedIds.at(-1)!).toBe(true);
-      expect(fixture.expectedIds).not.toContain(lateId);
-      await request.post(`${FIXTURES}/late-tie`, { data: { conversationId: fixture.conversationId, id: lateId, createdAt: piso } });
-      // Dez mensagens reais chegam enquanto a passagem está aberta. O navegador
-      // recebe cada push e deve coalescer a recuperação sem perder o piso T.
-      for (let i = 1; i <= 10; i += 1) {
-        await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-dirty-${i}`, text: `evento coalescido ${i}` });
+    const rotaTimeline = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
+    await page.route(rotaTimeline, async (route) => {
+      if (!captureRequests) return route.continue();
+      requestsRecovery += 1;
+      requestsAtivo += 1;
+      maxRequestsAtivo = Math.max(maxRequestsAtivo, requestsAtivo);
+      const pageNumber = requestsRecovery;
+      if (new URL(route.request().url()).searchParams.has('antes')) pagesBeforeCursor += 1;
+      try {
+        const response = await route.fetch();
+        if (pageNumber === 2) {
+          const cursor = new URL(route.request().url()).searchParams.get('antes')!;
+          const cursorPayload = JSON.parse(Buffer.from(cursor.slice(3), 'base64url').toString('utf8')) as { m: string };
+          const min = BigInt(`0x${cursorPayload.m.replaceAll('-', '')}`);
+          const max = BigInt(`0x${fixture.expectedIds.at(-1)!.replaceAll('-', '')}`);
+          lateId = ((min + max) / 2n).toString(16).padStart(32, '0').replace(/(.{8})(.{4})(.{4})(.{4})(.{12})/, '$1-$2-$3-$4-$5');
+          expect(lateId > cursorPayload.m).toBe(true);
+          expect(lateId < fixture.expectedIds.at(-1)!).toBe(true);
+          expect(fixture.expectedIds).not.toContain(lateId);
+          const lateTie = await request.post(`${FIXTURES}/late-tie`, { data: { conversationId: fixture.conversationId, id: lateId, createdAt: piso } });
+          expect(lateTie.status()).toBe(201);
+          for (let i = 1; i <= 10; i += 1) {
+            await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-dirty-${i}`, text: `evento coalescido ${i}` });
+          }
+          await expect.poll(() => mensagensRecebidas).toBe(11);
+          aguardeSegundaPagina();
+          await continua;
+        } else if (pageNumber === 3) {
+          expect(new URL(route.request().url()).searchParams.has('antes')).toBe(false);
+          aguardeTerceiraPagina();
+          const webhook = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-dirty-after-third-page-start', text: 'evento depois de iniciar a terceira consulta' });
+          expect(webhook.status).toBe(200);
+          await expect.poll(() => mensagensRecebidas).toBe(12);
+        }
+        await route.fulfill({ response });
+      } finally {
+        requestsAtivo -= 1;
       }
-      await expect.poll(() => mensagensRecebidas).toBe(11); // H + dez eventos durante a passagem
-      aguardeSegundaPagina();
-      await continua;
-      await route.fulfill({ response });
     });
     await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-head-H', text: 'nova cabeça H maior que T' });
     await segundaPagina;
     await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
     liberar();
+    await terceiraPagina;
+    await expect.poll(() => requestsRecovery).toBe(3);
+    await expect.poll(() => requestsAtivo).toBe(0);
+    expect(maxRequestsAtivo).toBe(1);
+    await page.waitForTimeout(250);
+    expect(requestsRecovery).toBe(3);
+    captureRequests = false;
     for (let i = 0; i < 12 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i++) {
       await page.getByRole('button', { name: 'Continuar atualização' }).click();
       await page.waitForTimeout(100);
@@ -221,7 +293,142 @@
     const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
     expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
     expect(ids).toContain(lateId);
-    expect(expected.unreadCount).toBe(11);
+    expect(expected.unreadCount).toBe(12);
+  });
+
+  test('falhas de recuperação consomem o orçamento e exigem continuação explícita', async ({ page, request }) => {
+    const fixture = await abrirTimeline(page, request, 251, true);
+    const attemptsStarted: Array<() => void> = [];
+    const attemptSignals = Array.from({ length: 3 }, () => new Promise<void>((resolve) => attemptsStarted.push(resolve)));
+    const releases: Array<() => void> = [];
+    const gates = Array.from({ length: 3 }, () => new Promise<void>((resolve) => releases.push(resolve)));
+    let attempts = 0;
+    let inFlight = 0;
+    let maxInFlight = 0;
+    let recoveryRequests = 0;
+    let failFirstThree = true;
+    const path = `/api/bff/conversations/${fixture.conversationId}/messages`;
+    await page.route((url) => url.pathname === path, async (route) => {
+      const url = new URL(route.request().url());
+      if (!url.searchParams.has('marcarLida') || url.searchParams.get('marcarLida') !== 'false') return route.continue();
+      recoveryRequests += 1;
+      inFlight += 1;
+      maxInFlight = Math.max(maxInFlight, inFlight);
+      const currentAttempt = recoveryRequests;
+      try {
+        const response = await route.fetch();
+        if (failFirstThree && currentAttempt <= 3) {
+          attempts += 1;
+          attemptsStarted[currentAttempt - 1]();
+          await gates[currentAttempt - 1];
+          await route.abort('failed');
+        } else {
+          await route.fulfill({ response });
+        }
+      } finally {
+        inFlight -= 1;
+      }
+    });
+
+    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-fail-budget-start', text: 'inicia atualização com resposta que falha' });
+    for (let i = 0; i < 3; i += 1) {
+      await attemptSignals[i];
+      const event = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-fail-budget-dirty-${i}`, text: `evento durante falha ${i + 1}` });
+      expect(event.status).toBe(200);
+      releases[i]();
+    }
+
+    await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
+    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
+    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
+    expect(attempts).toBe(3);
+    expect(recoveryRequests).toBe(3);
+    expect(maxInFlight).toBe(1);
+    await page.waitForTimeout(300);
+    expect(recoveryRequests).toBe(3);
+
+    failFirstThree = false;
+    for (let i = 0; i < 8 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
+      await page.getByRole('button', { name: 'Continuar atualização' }).click();
+      await page.waitForTimeout(100);
+    }
+    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
+    const expected = await audit(request, fixture.conversationId);
+    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
+    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
+    expect(expected.unreadCount).toBe(4);
+    expect(maxInFlight).toBe(1);
+  });
+
+  test('erro no cursor histórico reinicia pela cabeça após evento novo', async ({ page, request }) => {
+    let mensagensRecebidas = 0;
+    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
+      try {
+        if ((JSON.parse(String(payload)) as { tipo?: string }).tipo === 'mensagem') mensagensRecebidas += 1;
+      } catch { /* frames de conexão não representam mensagens */ }
+    }));
+    const fixture = await abrirTimeline(page, request, 251, true);
+    let liberarFalha!: () => void;
+    let iniciarPagina!: () => void;
+    const barreira = new Promise<void>((resolve) => { liberarFalha = resolve; });
+    const paginaIniciada = new Promise<void>((resolve) => { iniciarPagina = resolve; });
+    let requestsRecentes = 0;
+    let requestsHistoricos = 0;
+    let inFlight = 0;
+    let maxInFlight = 0;
+    const path = `/api/bff/conversations/${fixture.conversationId}/messages`;
+    await page.route((url) => url.pathname === path, async (route) => {
+      const url = new URL(route.request().url());
+      if (url.searchParams.get('marcarLida') !== 'false') return route.continue();
+      const historica = url.searchParams.has('antes');
+      if (historica) requestsHistoricos += 1;
+      else requestsRecentes += 1;
+      inFlight += 1;
+      maxInFlight = Math.max(maxInFlight, inFlight);
+      try {
+        const response = await route.fetch();
+        if (historica && requestsHistoricos === 1) {
+          iniciarPagina();
+          await barreira;
+          await route.abort('failed');
+        } else {
+          await route.fulfill({ response });
+        }
+      } finally {
+        inFlight -= 1;
+      }
+    });
+
+    try {
+      await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-cursor-failure-head', text: 'cabeça antes da falha histórica' });
+      await expect.poll(() => mensagensRecebidas).toBe(1);
+      await paginaIniciada;
+      const secondEvent = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-cursor-failure-during-page', text: 'nova cabeça durante falha histórica' });
+      expect(secondEvent.status).toBe(200);
+      await expect.poll(() => mensagensRecebidas).toBe(2);
+      liberarFalha();
+
+      await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
+      await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
+      await expect.poll(() => requestsRecentes).toBe(2);
+      await expect.poll(() => inFlight).toBe(0);
+      expect(requestsHistoricos).toBe(1);
+      expect(maxInFlight).toBe(1);
+
+      for (let i = 0; i < 8 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
+        await page.getByRole('button', { name: 'Continuar atualização' }).click();
+        await page.waitForTimeout(100);
+      }
+      await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
+      const expected = await audit(request, fixture.conversationId);
+      const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
+      expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
+      expect(expected.unreadCount).toBe(2);
+      expect(maxInFlight).toBe(1);
+    } finally {
+      liberarFalha();
+      await page.unrouteAll({ behavior: 'wait' });
+    }
   });
 
   test('preserva a âncora quando uma mensagem chega durante o backfill atrasado', async ({ page, request }) => {
@@ -331,56 +538,146 @@
   });
 
   test('troca de conversa e BU protege resposta atrasada de envio', async ({ page, request }) => {
+    test.setTimeout(30_000);
     const fixture = await abrirTimeline(page, request, 251);
-    let liberarEnvio!: () => void;
-    let envioRecebido!: () => void;
-    const continuaEnvio = new Promise<void>((resolve) => { liberarEnvio = resolve; });
-    const chegouEnvio = new Promise<void>((resolve) => { envioRecebido = resolve; });
-    await page.route(`**/api/bff/conversations/${fixture.otherConversationId}/messages`, async (route) => {
-      if (route.request().method() !== 'POST') return route.continue();
-      const response = await route.fetch();
-      envioRecebido();
-      await continuaEnvio;
-      await route.fulfill({ response });
-    });
-    // A chamada persistida chega atrasada ao cliente, depois de o usuário trocar de conversa.
-    const outra = fixture.otherConversationId;
-    await page.getByRole('button', { name: 'Cliente Secundário' }).click();
-    const draft = page.getByPlaceholder('Escreva uma resposta');
-    await draft.fill('envio durante troca');
-    await page.getByRole('button', { name: 'Enviar' }).click();
-    await chegouEnvio;
+    const secundaria = fixture.otherConversationId;
+    const outraBu = fixture.otherBuConversationId;
+    const populateSecondary = await request.post(`${FIXTURES}/burst`, { data: { conversationId: secundaria, count: 80, createdAt: Date.now() - 10_000 } });
+    const populateOtherBu = await request.post(`${FIXTURES}/burst`, { data: { conversationId: outraBu, count: 80, createdAt: Date.now() - 10_000 } });
+    expect(populateSecondary.status()).toBe(201);
+    expect(populateOtherBu.status()).toBe(201);
+
+    const holdRequest = async (conversationId: string, method: 'POST' | 'GET', fail = false) => {
+      let release!: () => void;
+      let started!: () => void;
+      let settled!: () => void;
+      const gate = new Promise<void>((resolve) => { release = resolve; });
+      const received = new Promise<void>((resolve) => { started = resolve; });
+      const finished = new Promise<void>((resolve) => { settled = resolve; });
+      const predicate = (url: URL) => url.pathname === `/api/bff/conversations/${conversationId}/messages` && (method === 'POST' ? url.search === '' : url.searchParams.has('antes'));
+      await page.route(predicate, async (route) => {
+        if (route.request().method() !== method) return route.continue();
+        if (method === 'GET' && !new URL(route.request().url()).searchParams.has('antes')) return route.continue();
+        try {
+          const response = fail ? undefined : await route.fetch();
+          started();
+          await gate;
+          if (fail) await route.abort('failed');
+          else await route.fulfill({ response });
+        } finally {
+          settled();
+        }
+      });
+      return { predicate, started: received, release, finished, remove: () => page.unroute(predicate) };
+    };
+
+    const destinationSnapshot = async (draftText: string) => {
+      const draft = page.getByPlaceholder('Escreva uma resposta');
+      await expect(draft).toBeVisible();
+      await draft.fill(draftText);
+      const timeline = page.locator('.bolhas');
+      const scrollTop = await timeline.evaluate((el) => {
+        el.scrollTop = Math.min(120, el.scrollHeight - el.clientHeight);
+        return el.scrollTop;
+      });
+      return {
+        draftText,
+        active: await page.locator('.item.ativo').innerText(),
+        metadata: await page.locator('.inbox > .cartao.grade .linha').first().innerText(),
+        ids: await timeline.evaluate((el) => [...el.querySelectorAll<HTMLElement>('.bolha')].map((item) => item.dataset.messageId)),
+        scrollTop,
+      };
+    };
+    const expectDestinationUnchanged = async (snapshot: Awaited<ReturnType<typeof destinationSnapshot>>) => {
+      expect((await page.locator('.item.ativo').innerText()).replace(/\s+/g, ' ').trim()).toBe(snapshot.active.replace(/\s+/g, ' ').trim());
+      expect((await page.locator('.inbox > .cartao.grade .linha').first().innerText()).replace(/\s+/g, ' ').trim()).toBe(snapshot.metadata.replace(/\s+/g, ' ').trim());
+      await expect(page.getByPlaceholder('Escreva uma resposta')).toHaveValue(snapshot.draftText);
+      await expect(page.getByRole('alert')).toHaveCount(0);
+      const timeline = page.locator('.bolhas');
+      expect(await timeline.evaluate((el) => [...el.querySelectorAll<HTMLElement>('.bolha')].map((item) => item.dataset.messageId))).toEqual(snapshot.ids);
+      expect(await timeline.evaluate((el) => el.scrollTop)).toBe(snapshot.scrollTop);
+    };
+    const openConversation = async (name: string, tab: 'Na fila' | 'Em atendimento' = 'Na fila', count = 50) => {
+      await page.getByRole('button', { name: tab }).click();
+      await page.getByRole('button', { name }).click();
+      await expect(page.locator('.bolha')).toHaveCount(count);
+    };
+    const openOtherBu = async () => {
+      await page.getByLabel('Business Unit').selectOption(fixture.otherBusinessUnitId);
+      await page.getByRole('button', { name: 'Na fila' }).click();
+      await page.getByRole('button', { name: 'Cliente Outra BU' }).click();
+      await expect(page.locator('.bolha')).toHaveCount(50);
+    };
+    const sendAndSwitch = async (context: 'conversation' | 'bu', fail: boolean, text: string, draftText: string) => {
+      const hold = await holdRequest(secundaria, 'POST', fail);
+      const input = page.getByPlaceholder('Escreva uma resposta');
+      await input.fill(text);
+      await page.getByRole('button', { name: 'Enviar' }).click();
+      try {
+        await hold.started;
+        if (context === 'conversation') await openConversation('Cliente Timeline', 'Na fila', 50);
+        else await openOtherBu();
+        const snapshot = await destinationSnapshot(draftText);
+        hold.release();
+        await hold.finished;
+        await page.waitForTimeout(100);
+        await expectDestinationUnchanged(snapshot);
+        return snapshot;
+      } finally {
+        hold.release();
+        await hold.remove();
+      }
+    };
+
+    await openConversation('Cliente Secundário');
+    await sendAndSwitch('conversation', false, 'envio antigo sucesso conversa', 'rascunho destino conversa');
+    const afterSuccess = await audit(request, secundaria);
+    expect(afterSuccess.messages.some((m: { content: string; direction: string }) => m.content === 'envio antigo sucesso conversa' && m.direction === 'OUT')).toBe(true);
+
+    await openConversation('Cliente Secundário', 'Em atendimento');
+    await sendAndSwitch('conversation', true, 'envio antigo falho conversa', 'rascunho apos falha conversa');
+    const afterFailure = await audit(request, secundaria);
+    expect(afterFailure.messages.some((m: { content: string }) => m.content === 'envio antigo falho conversa')).toBe(false);
+
+    const holdBackfillConversation = await holdRequest(fixture.conversationId, 'GET');
     await page.getByRole('button', { name: 'Cliente Timeline' }).click();
-    liberarEnvio();
-    await expect(page.locator('.item.ativo')).toContainText('Cliente Timeline');
-    await expect(page.locator('.bolha').filter({ hasText: 'envio durante troca' })).toHaveCount(0);
-    const enviado = await audit(request, outra);
-    expect(enviado.messages.some((m: { content: string; direction: string }) => m.content === 'envio durante troca' && m.direction === 'OUT')).toBe(true);
-
-    let liberarEnvioBu!: () => void;
-    let envioBuRecebido!: () => void;
-    const continuaBu = new Promise<void>((resolve) => { liberarEnvioBu = resolve; });
-    const chegouBu = new Promise<void>((resolve) => { envioBuRecebido = resolve; });
-    const buRequest = `**/api/bff/conversations/${fixture.otherConversationId}/messages`;
-    await page.route(buRequest, async (route) => {
-      if (route.request().method() !== 'POST') return route.continue();
-      const response = await route.fetch();
-      envioBuRecebido();
-      await continuaBu;
-      await route.fulfill({ response });
-    });
-    await page.getByRole('button', { name: 'Em atendimento' }).click();
-    await page.getByRole('button', { name: 'Cliente Secundário' }).click();
-    await page.getByPlaceholder('Escreva uma resposta').fill('envio durante troca de BU');
-    await page.getByRole('button', { name: 'Enviar' }).click();
-    await chegouBu;
-    await page.getByLabel('Business Unit').selectOption({ label: 'Número alternativo' });
-    await page.getByRole('button', { name: 'Na fila' }).click();
-    await page.getByRole('button', { name: 'Cliente Outra BU' }).click();
-    liberarEnvioBu();
-    await expect(page.locator('.item.ativo')).toContainText('Cliente Outra BU');
-    await expect(page.locator('.bolha').filter({ hasText: 'envio durante troca de BU' })).toHaveCount(0);
-    const crossBuSent = await audit(request, fixture.otherConversationId);
-    expect(crossBuSent.messages.some((m: { content: string }) => m.content === 'envio durante troca de BU')).toBe(true);
+    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
+    try {
+      await holdBackfillConversation.started;
+      await openConversation('Cliente Secundário', 'Em atendimento');
+      const backfillDestination = await destinationSnapshot('rascunho apos backfill conversa');
+      holdBackfillConversation.release();
+      await holdBackfillConversation.finished;
+      await expectDestinationUnchanged(backfillDestination);
+    } finally {
+      holdBackfillConversation.release();
+      await holdBackfillConversation.remove();
+    }
+
+    await sendAndSwitch('bu', false, 'envio antigo sucesso BU', 'rascunho destino BU');
+    const buSuccess = await audit(request, secundaria);
+    expect(buSuccess.messages.some((m: { content: string; direction: string }) => m.content === 'envio antigo sucesso BU' && m.direction === 'OUT')).toBe(true);
+
+    await page.getByLabel('Business Unit').selectOption(fixture.businessUnitId);
+    await openConversation('Cliente Secundário', 'Em atendimento');
+    await sendAndSwitch('bu', true, 'envio antigo falho BU', 'rascunho apos falha BU');
+    const buFailure = await audit(request, secundaria);
+    expect(buFailure.messages.some((m: { content: string }) => m.content === 'envio antigo falho BU')).toBe(false);
+
+    await page.getByLabel('Business Unit').selectOption(fixture.businessUnitId);
+    await openConversation('Cliente Timeline', 'Na fila', 50);
+    const holdBackfillBu = await holdRequest(fixture.conversationId, 'GET');
+    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
+    try {
+      await holdBackfillBu.started;
+      await openOtherBu();
+      const otherBuSnapshot = await destinationSnapshot('rascunho apos backfill BU');
+      holdBackfillBu.release();
+      await holdBackfillBu.finished;
+      await expectDestinationUnchanged(otherBuSnapshot);
+    } finally {
+      holdBackfillBu.release();
+      await holdBackfillBu.remove();
+    }
   });
 });

```

## web-app/src/telas/Inbox.tsx
```
import { FormEvent, useCallback, useEffect, useRef, useState } from 'react';
import { BusinessUnit, Conversa, ErroDaApi, Eu, Mensagem, Thread, api, ignorarSessaoMorta } from '../api';
import { ouvirTempoReal } from '../tempoReal';
import { cruzouPiso, mesclarMensagens } from '../timeline';

const ABAS = [
  { id: 'QUEUED', rotulo: 'Na fila' },
  { id: 'IN_SERVICE', rotulo: 'Em atendimento' },
  { id: 'CLOSED', rotulo: 'Finalizadas' },
  { id: 'GRUPO', rotulo: 'Grupos' },
];

interface Recuperacao {
  id: string;
  geracao: number;
  piso: string;
  cursor: string | null;
  dirty: boolean;
  eventos: number;
  emVoo: boolean;
  paginasRestantes: number;
  vazio?: boolean;
}

interface InvalidacaoDeAbertura {
  id: string;
  geracao: number;
  eventos: number;
}

export default function Inbox({ eu }: { eu: Eu }) {
  const [bus, setBus] = useState<BusinessUnit[]>([]);
  const [buId, setBuId] = useState<string>('');
  const [aba, setAba] = useState('QUEUED');
  const [conversas, setConversas] = useState<Conversa[]>([]);
  const [aberta, setAberta] = useState<Thread | null>(null);
  const [abrindo, setAbrindo] = useState(false);
  const [texto, setTexto] = useState('');
  const [erro, setErro] = useState<string | null>(null);
  const [carregandoAnteriores, setCarregandoAnteriores] = useState(false);
  const [recuperacaoPendente, setRecuperacaoPendente] = useState(false);
  const [enviando, setEnviando] = useState(false);
  const textoRef = useRef('');
  const geracao = useRef(0);
  const buAtual = useRef('');
  const conversaAtual = useRef<string | null>(null);
  const abaAtual = useRef('QUEUED');
  const threadAtual = useRef<Thread | null>(null);
  const recuperacao = useRef<Recuperacao | null>(null);
  const invalidacaoAbertura = useRef<InvalidacaoDeAbertura | null>(null);
  const executarRecuperacaoRef = useRef<() => Promise<void>>(async () => {});
  const versaoMetadados = useRef(0);
  const bolhas = useRef<HTMLDivElement>(null);
  const carregarListaRef = useRef<(id?: string, filtro?: string) => Promise<void>>(async () => {});
  const reconciliarRef = useRef<() => void>(() => {});

  const guardarThread = (thread: Thread | null) => {
    threadAtual.current = thread;
    setAberta(thread);
  };

  const guardarTexto = (valor: string) => {
    textoRef.current = valor;
    setTexto(valor);
  };

  useEffect(() => {
    api.get<{ businessUnits: BusinessUnit[] }>('/business-units').then((r) => {
      const lista = r.businessUnits ?? [];
      setBus(lista);
      const inicial = lista[0]?.id ?? '';
      buAtual.current = inicial;
      setBuId(inicial);
    }).catch(ignorarSessaoMorta);
  }, []);

  const carregarLista = useCallback(async (id = buAtual.current, filtro = aba) => {
    if (!id) return;
    try {
      const r = await api.get<{ conversations: Conversa[] }>(`/business-units/${id}/conversations?aba=${filtro}`);
      if (buAtual.current === id && abaAtual.current === filtro) setConversas(r.conversations);
    } catch (e) {
      if (buAtual.current === id && abaAtual.current === filtro) throw e;
    }
  }, [aba]);

  const aplicarPaginaRecente = useCallback((id: string, geracaoDaChamada: number, versao: number, response: Thread) => {
    if (conversaAtual.current !== id || geracao.current !== geracaoDaChamada) return;
    const anterior = threadAtual.current;
    const novo: Thread = {
      ...response,
      messages: mesclarMensagens(anterior?.messages ?? [], response.messages),
      // O cursor de reconciliação recente não substitui o cursor do histórico.
      paginacao: anterior && anterior.messages.length > 0 ? anterior.paginacao : response.paginacao,
      conversa: versaoMetadados.current === versao ? response.conversa : anterior?.conversa ?? response.conversa,
      janela: versaoMetadados.current === versao ? response.janela : anterior?.janela ?? response.janela,
    };
    guardarThread(novo);
  }, []);

  const executarRecuperacao = useCallback(async () => {
    const r = recuperacao.current;
    if (!r || r.emVoo || r.paginasRestantes <= 0 || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
    r.emVoo = true;
    const eventosNoInicio = r.eventos;
    r.dirty = false;
    let cruzou = false;
    try {
      if (r.vazio) {
        if (r.cursor === null && r.paginasRestantes > 0) {
          const versao = versaoMetadados.current;
          r.paginasRestantes -= 1;
          const inicial = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          aplicarPaginaRecente(r.id, r.geracao, versao, inicial);
          r.cursor = inicial.paginacao.cursorAnterior;
          if (!inicial.paginacao.temAnteriores) r.cursor = null;
        }
        while (r.cursor && r.paginasRestantes > 0 && !r.dirty) {
          const cursor = r.cursor;
          r.paginasRestantes -= 1;
          const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
          const atual = threadAtual.current;
          if (atual) guardarThread({
            ...atual,
            messages: mesclarMensagens(atual.messages, pagina.messages),
            paginacao: pagina.paginacao,
          });
          r.cursor = pagina.paginacao.cursorAnterior;
        }
        if (r.eventos !== eventosNoInicio || r.dirty) {
          r.cursor = null;
          setRecuperacaoPendente(true);
        } else if (!r.cursor) {
          recuperacao.current = null;
          setRecuperacaoPendente(false);
        } else {
          setRecuperacaoPendente(true);
        }
        return;
      }
      if (r.cursor === null && r.paginasRestantes > 0) {
        const versao = versaoMetadados.current;
        r.paginasRestantes -= 1;
        const recente = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        aplicarPaginaRecente(r.id, r.geracao, versao, recente);
        r.cursor = recente.paginacao.cursorAnterior;
        cruzou = cruzouPiso(recente.messages, r.piso) || !recente.paginacao.temAnteriores;
      }
      while (!cruzou && r.cursor && r.paginasRestantes > 0 && !r.dirty) {
        const cursor = r.cursor;
        r.paginasRestantes -= 1;
        const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
        const atual = threadAtual.current;
        if (atual) guardarThread({
          ...atual,
          messages: mesclarMensagens(atual.messages, pagina.messages),
        });
        r.cursor = pagina.paginacao.cursorAnterior;
        cruzou = cruzouPiso(pagina.messages, r.piso) || !pagina.paginacao.temAnteriores;
      }

      if (r.eventos !== eventosNoInicio || r.dirty) {
        // Um evento concorrente exige nova passagem recente e preserva o piso.
        r.cursor = null;
        setRecuperacaoPendente(true);
      } else if (cruzou) {
        recuperacao.current = null;
        setRecuperacaoPendente(false);
      } else {
        setRecuperacaoPendente(true);
      }
    } catch (e) {
      if (r.geracao === geracao.current && r.id === conversaAtual.current) {
        if (r.dirty || r.eventos !== eventosNoInicio) r.cursor = null;
        setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível atualizar o histórico. Tente novamente.');
        setRecuperacaoPendente(true);
      }
    } finally {
      r.emVoo = false;
      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.paginasRestantes > 0 && r.geracao === geracao.current) {
        queueMicrotask(() => void executarRecuperacaoRef.current());
      }
    }
  }, [aplicarPaginaRecente]);

  useEffect(() => { executarRecuperacaoRef.current = executarRecuperacao; }, [executarRecuperacao]);

  const reconciliar = useCallback(() => {
    const thread = threadAtual.current;
    const id = conversaAtual.current;
    if (!id) return;
    if (!thread) {
      const abertura = invalidacaoAbertura.current;
      if (abertura?.id === id && abertura.geracao === geracao.current) abertura.eventos += 1;
      return;
    }
    let r = recuperacao.current;
    if (!r || r.id !== id || r.geracao !== geracao.current) {
      const mensagens = thread.messages;
      if (mensagens.length === 0) {
        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3, vazio: true };
        recuperacao.current = r;
        void executarRecuperacao();
        return;
      }
      const piso = mensagens.reduce((max, m) => Date.parse(m.createdAt) > Date.parse(max) ? m.createdAt : max, mensagens[0].createdAt);
      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3 };
      recuperacao.current = r;
      setRecuperacaoPendente(true);
    } else {
      r.dirty = true;
      r.eventos += 1;
      if (!r.emVoo) r.cursor = null;
      setRecuperacaoPendente(true);
    }
    if (r.paginasRestantes > 0) void executarRecuperacao();
  }, [aplicarPaginaRecente, executarRecuperacao]);

  const iniciarRodadaAutorizada = useCallback(() => {
    const r = recuperacao.current;
    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
    r.paginasRestantes = 3;
    void executarRecuperacao();
  }, [executarRecuperacao]);

  useEffect(() => {
    carregarListaRef.current = carregarLista;
    reconciliarRef.current = reconciliar;
  }, [carregarLista, reconciliar]);

  useEffect(() => {
    void carregarLista().catch(ignorarSessaoMorta);
    const t = setInterval(() => {
      void carregarLista().catch(ignorarSessaoMorta);
      if (recuperacao.current) iniciarRodadaAutorizada();
      else reconciliar();
    }, 60_000);
    return () => clearInterval(t);
  }, [buId, aba, carregarLista, reconciliar, iniciarRodadaAutorizada]);

  useEffect(() => {
    // Espera a lista inicial de BUs e mantém o socket apesar de filtros, BUs ou
    // callbacks locais mudarem. Isso evita reconectar durante o mesmo login.
    if (bus.length === 0) return;
    const parar = ouvirTempoReal((evento) => {
      if (evento.buId !== buAtual.current) return;
      void carregarListaRef.current().catch(ignorarSessaoMorta);
      if (evento.conversaId === conversaAtual.current) reconciliarRef.current();
    }, () => reconciliarRef.current());
    return parar;
  }, [eu.id, bus.length]);

  function trocarBu(novoBu: string) {
    geracao.current += 1;
    buAtual.current = novoBu;
    conversaAtual.current = null;
    recuperacao.current = null;
    invalidacaoAbertura.current = null;
    guardarThread(null);
    setAbrindo(false);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    setErro(null);
    setRecuperacaoPendente(false);
    setConversas([]);
    setBuId(novoBu);
  }

  async function abrir(id: string) {
    const gen = ++geracao.current;
    conversaAtual.current = id;
    recuperacao.current = null;
    invalidacaoAbertura.current = { id, geracao: gen, eventos: 0 };
    versaoMetadados.current += 1;
    guardarThread(null);
    setAbrindo(true);
    guardarTexto('');
    setEnviando(false);
    setCarregandoAnteriores(false);
    setErro(null);
    setRecuperacaoPendente(false);
    try {
      const response = await api.get<Thread>(`/conversations/${id}/messages`);
      if (gen !== geracao.current || conversaAtual.current !== id) return;
      response.messages = mesclarMensagens(response.messages);
      guardarThread(response);
      setAbrindo(false);
      const invalidacao = invalidacaoAbertura.current;
      invalidacaoAbertura.current = null;
      void carregarLista().catch(ignorarSessaoMorta);
      if (invalidacao?.id === id && invalidacao.geracao === gen && invalidacao.eventos > 0) reconciliar();
    } catch (e) {
      if (gen === geracao.current) {
        invalidacaoAbertura.current = null;
        guardarThread(null);
        setAbrindo(false);
        setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível carregar a conversa.');
      }
    }
  }

  async function carregarAnteriores() {
    const atual = threadAtual.current;
    const id = conversaAtual.current;
    const cursor = atual?.paginacao.cursorAnterior;
    if (!atual || !id || !cursor || carregandoAnteriores) return;
    const gen = geracao.current;
    setCarregandoAnteriores(true);
    setErro(null);
    try {
      const pagina = await api.get<Thread>(`/conversations/${id}/messages?antes=${encodeURIComponent(cursor)}`);
      if (gen !== geracao.current || id !== conversaAtual.current || !threadAtual.current) return;
      // Inclua alterações legítimas que chegaram enquanto a página estava no ar.
      const alturaAntes = bolhas.current?.scrollHeight ?? 0;
      const topoAntes = bolhas.current?.scrollTop ?? 0;
      const corrente = threadAtual.current;
      guardarThread({ ...corrente, messages: mesclarMensagens(corrente.messages, pagina.messages), paginacao: pagina.paginacao });
      requestAnimationFrame(() => {
        if (gen === geracao.current && bolhas.current) bolhas.current.scrollTop = topoAntes + (bolhas.current.scrollHeight - alturaAntes);
      });
    } catch (e) {
      if (gen === geracao.current) setErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Falha ao carregar mensagens anteriores.');
    } finally {
      if (gen === geracao.current) setCarregandoAnteriores(false);
    }
  }

  async function agir(acao: () => Promise<unknown>) {
    const id = conversaAtual.current;
    const gen = geracao.current;
    if (!id) return;
    versaoMetadados.current += 1;
    setErro(null);
    try {
      await acao();
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) setErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
    }
  }

  async function responder(e: FormEvent) {
    e.preventDefault();
    const id = conversaAtual.current;
    const gen = geracao.current;
    const textoEnviado = textoRef.current;
    if (!id || !textoEnviado.trim() || enviando) return;
    setEnviando(true);
    setErro(null);
    try {
      await api.post(`/conversations/${id}/messages`, { texto: textoEnviado });
      if (gen !== geracao.current || id !== conversaAtual.current) return;
      if (textoRef.current === textoEnviado) guardarTexto('');
      void carregarLista().catch(ignorarSessaoMorta);
      reconciliar();
    } catch (e) {
      if (gen === geracao.current) setErro(e instanceof ErroDaApi ? e.message : 'Falha ao enviar mensagem.');
    } finally {
      if (gen === geracao.current) setEnviando(false);
    }
  }

  const janelaFechada = aberta?.janela.exigida && !aberta.janela.aberta;

  return (
    <div className="grade">
      <div className="linha">
        <select aria-label="Business Unit" value={buId} onChange={(e) => trocarBu(e.target.value)} style={{ maxWidth: 280 }}>
          {bus.map((b) => <option key={b.id} value={b.id}>{b.name}</option>)}
        </select>
        {erro && <span className="erro" role="alert">{erro}</span>}
      </div>

      <div className="abas">
        {ABAS.map((a) => <button key={a.id} className={aba === a.id ? 'ativa' : ''} onClick={() => { abaAtual.current = a.id; setAba(a.id); }}>{a.rotulo}</button>)}
      </div>

      <div className="inbox">
        <div className="cartao lista" style={{ padding: 0 }}>
          {conversas.map((c) => <button key={c.id} className={`item ${aberta?.conversa.id === c.id ? 'ativo' : ''}`} onClick={() => void abrir(c.id)}>
            <div className="linha"><strong>{c.displayName ?? c.contact}</strong>{c.unreadCount > 0 && <span className="suave">({c.unreadCount})</span>}</div>
            <div className="suave">{c.attendantName ?? 'sem atendente'}</div>
          </button>)}
          {conversas.length === 0 && <p className="suave" style={{ padding: 12 }}>Nada aqui.</p>}
        </div>

        <div className="cartao grade">
          {!aberta && (abrindo
            ? <p className="suave" role="status" aria-live="polite">Abrindo conversa…</p>
            : <p className="suave">Escolha uma conversa.</p>)}
          {aberta && <>
            <div className="linha">
              <strong>{aberta.conversa.nome ?? aberta.conversa.contato}</strong>
              <span className="suave">{aberta.conversa.status}</span>
              <span className="suave" style={{ marginLeft: 'auto' }}>{aberta.janela.canal}</span>
            </div>
            <div className="linha">
              {aberta.paginacao.temAnteriores
                ? <button onClick={() => void carregarAnteriores()} disabled={carregandoAnteriores} aria-label="Carregar mensagens anteriores">
                    {carregandoAnteriores ? 'Carregando…' : 'Carregar anteriores'}
                  </button>
                : <span className="suave">Início do histórico</span>}
              {recuperacaoPendente && <span className="suave" role="status">Atualização pendente. O histórico pode ter uma lacuna.</span>}
              {recuperacaoPendente && <button onClick={() => iniciarRodadaAutorizada()}>Continuar atualização</button>}
            </div>
            <div className="bolhas" ref={bolhas} aria-live="polite">
              {aberta.messages.map((m: Mensagem) => <div key={m.id} data-message-id={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>
                <div>{m.content}</div>
                <div className="suave">{new Date(m.createdAt).toLocaleString('pt-BR')}{m.authorName ? ` · ${m.authorName}` : ''}</div>
              </div>)}
              {aberta.messages.length === 0 && <p className="suave">Nenhuma mensagem nesta conversa.</p>}
            </div>

            {janelaFechada && <div className="aviso">Fora da janela de 24h da Meta: só dá para responder texto livre até 24h após a última mensagem da pessoa. A alternativa é disparar um modelo aprovado — isso ainda vive na Central de Modelos.</div>}
            <form className="linha" onSubmit={responder}>
              <input value={texto} onChange={(e) => guardarTexto(e.target.value)} placeholder={janelaFechada ? 'Janela fechada' : 'Escreva uma resposta'} disabled={Boolean(janelaFechada)} maxLength={4096} />
              <button className="primario" disabled={Boolean(janelaFechada) || enviando || !texto.trim()}>{enviando ? 'Enviando…' : 'Enviar'}</button>
            </form>
            {aberta.conversa.status !== 'CLOSED' && <div className="linha">
              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/claim`))}>Atender</button>
              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/close`))}>Finalizar</button>
            </div>}
          </>}
        </div>
      </div>
    </div>
  );
}

```

## web-app/src/tempoReal.ts
```
import { API_BASE as BASE } from './config';

/**
 * Conexão de tempo real com o BFF.
 *
 * A autenticação é o COOKIE, mandado no handshake — nada de token na URL, que
 * vaza em log de proxy (ADR-0007). Isso funciona porque o front é subdomínio do
 * mesmo domínio da API (ADR-0015).
 *
 * O servidor só entrega evento de BU em que a pessoa tem grant, então aqui não
 * há filtro a fazer: o que chegar, chegou porque podia.
 */

export interface EventoDeMensagem {
  tipo: 'mensagem';
  buId: string;
  conversaId: string;
  contato: string;
  direcao: 'IN' | 'OUT';
  naoLidas: number;
}

/**
 * Monta o endereço do socket por texto, e não mexendo em `url.protocol`.
 *
 * Trocar o esquema de um `URL` já construído é onde isso quebra em silêncio: se
 * a troca não pega, sobra `https://…` e o `new WebSocket` lança — dentro de um
 * efeito, o que derruba a tela inteira.
 */
export function enderecoDoSocket(base: string, origem: string): string {
  const raiz = (base || origem).replace(/\/+$/, '');
  return `${raiz.replace(/^http/, 'ws')}/ws`;
}

export function ouvirTempoReal(
  aoReceber: (evento: EventoDeMensagem) => void,
  aoReconectar?: () => void,
): () => void {
  const url = enderecoDoSocket(BASE, window.location.origin);

  let ws: WebSocket | null = null;
  let reconectar: number | undefined;
  let vivo = true;

  const conectar = () => {
    if (!vivo) return;
    // Tempo real é conforto, não requisito: se ele falhar, a tela continua de
    // pé com o poll. Um throw aqui derrubaria a aplicação inteira, porque isto
    // roda dentro de um efeito.
    try {
      ws = new WebSocket(url);
    } catch (e) {
      console.warn('tempo real indisponível:', e);
      return;
    }
    ws.onopen = () => {
      if (!vivo) {
        ws?.close();
        return;
      }
      aoReconectar?.();
    };
    ws.onmessage = (e) => {
      if (!vivo) return;
      const evento = JSON.parse(e.data as string);
      if (evento?.tipo === 'mensagem') aoReceber(evento as EventoDeMensagem);
    };
    // Reconecta sozinho: deploy, queda de rede e suspensão do notebook fecham o
    // socket, e a tela não pode ficar muda esperando um F5.
    ws.onclose = () => {
      if (vivo) reconectar = window.setTimeout(conectar, 3000);
    };
  };
  conectar();

  return () => {
    vivo = false;
    window.clearTimeout(reconectar);
    reconectar = undefined;
    ws?.close();
  };
}

```

## web-app/src/tempoReal.spec.ts
```
import { afterEach, describe, expect, it, vi } from 'vitest';
import { enderecoDoSocket, ouvirTempoReal } from './tempoReal';

afterEach(() => vi.unstubAllGlobals());

describe('enderecoDoSocket', () => {
  it('https vira wss', () => {
    expect(enderecoDoSocket('https://api.leadshug.com.br', 'x')).toBe('wss://api.leadshug.com.br/ws');
  });

  it('http vira ws', () => {
    expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws');
  });

  it('base vazia cai na origem da página', () => {
    expect(enderecoDoSocket('', 'https://app.leadshug.com.br')).toBe('wss://app.leadshug.com.br/ws');
  });

  it('barra sobrando não vira //ws', () => {
    expect(enderecoDoSocket('https://api.leadshug.com.br/', 'x')).toBe('wss://api.leadshug.com.br/ws');
  });

  it('notifica a recuperação ao estabelecer e restabelecer a conexão', () => {
    const sockets: Array<{ onopen?: () => void; onclose?: () => void; close: () => void }> = [];
    class SocketFake {
      onopen?: () => void;
      onclose?: () => void;
      constructor() { sockets.push(this); }
      close() {}
    }
    const timers: Array<() => void> = [];
    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() });
    vi.stubGlobal('WebSocket', SocketFake as unknown as typeof WebSocket);
    const reconnect = vi.fn();
    const stop = ouvirTempoReal(vi.fn(), reconnect);

    sockets[0].onopen?.();
    expect(reconnect).toHaveBeenCalledTimes(1);
    sockets[0].onclose?.();
    timers.shift()?.();
    sockets[1].onopen?.();
    expect(reconnect).toHaveBeenCalledTimes(2);
    stop();
  });

  it('descarta callbacks tardios e reconexão quando desmonta ainda conectando', () => {
    const sockets: Array<{ onopen?: () => void; onclose?: () => void; onmessage?: (event: { data: string }) => void; close: () => void }> = [];
    class SocketFake {
      onopen?: () => void;
      onclose?: () => void;
      onmessage?: (event: { data: string }) => void;
      close = vi.fn();
      constructor() { sockets.push(this); }
    }
    const timers: Array<() => void> = [];
    const clearTimeout = vi.fn();
    const setTimeout = vi.fn((fn: () => void) => { timers.push(fn); return timers.length; });
    vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout });
    vi.stubGlobal('WebSocket', SocketFake as unknown as typeof WebSocket);
    const receive = vi.fn();
    const reconnect = vi.fn();
    const stop = ouvirTempoReal(receive, reconnect);
    const lateOpen = sockets[0].onopen;
    const lateMessage = sockets[0].onmessage;
    sockets[0].onclose?.();
    const lateClose = sockets[0].onclose;

    stop();
    timers[0]?.();
    lateOpen?.();
    lateMessage?.({ data: JSON.stringify({ tipo: 'mensagem', buId: 'bu', conversaId: 'conv', contato: 'x', direcao: 'IN', naoLidas: 1 }) });
    lateClose?.();

    expect(sockets).toHaveLength(1);
    expect(receive).not.toHaveBeenCalled();
    expect(reconnect).not.toHaveBeenCalled();
    expect(setTimeout).toHaveBeenCalledTimes(1);
    expect(clearTimeout).toHaveBeenCalledWith(1);
    expect(sockets[0].close).toHaveBeenCalledTimes(2);
  });

});

```

## web-app/src/timeline.ts
```
import type { Mensagem } from './api';

export function mesclarMensagens(...grupos: Mensagem[][]): Mensagem[] {
  const porId = new Map<string, Mensagem>();
  for (const grupo of grupos) for (const mensagem of grupo) porId.set(mensagem.id, mensagem);
  return [...porId.values()].sort((a, b) => {
    const tempo = Date.parse(a.createdAt) - Date.parse(b.createdAt);
    return tempo || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
  });
}

export function cruzouPiso(mensagens: Mensagem[], piso: string): boolean {
  return mensagens.some((mensagem) => Date.parse(mensagem.createdAt) < Date.parse(piso));
}

```

## web-app/src/timeline.test.ts
```
import { describe, expect, it } from 'vitest';
import { cruzouPiso, mesclarMensagens } from './timeline';
import type { Mensagem } from './api';

const msg = (id: string, createdAt: string): Mensagem => ({
  id, createdAt, direction: 'IN', content: id, channelOrigin: 'OFICIAL', authorName: null,
});

describe('timeline da inbox', () => {
  it('mescla por ID e ordena estavelmente por timestamp e ID', () => {
    const empatada = '2026-01-01T00:00:00.000Z';
    expect(mesclarMensagens([msg('b', empatada), msg('a', empatada)], [msg('b', empatada), msg('c', '2026-01-02T00:00:00.000Z')]).map((m) => m.id))
      .toEqual(['a', 'b', 'c']);
  });

  it('só cruza a cobertura quando alcança timestamp estritamente anterior ao piso', () => {
    expect(cruzouPiso([msg('x', '2026-01-01T00:00:00.000Z')], '2026-01-01T00:00:00.000Z')).toBe(false);
    expect(cruzouPiso([msg('x', '2025-12-31T23:59:59.999Z')], '2026-01-01T00:00:00.000Z')).toBe(true);
  });
});

```

## web-app/e2e/timeline.spec.ts
```
import { expect, test, type Page, type APIRequestContext } from '@playwright/test';

const FIXTURES = 'http://127.0.0.1:3101';
const TOKEN_INTERNO = 'token-de-e2e';
const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`;

async function seed(request: APIRequestContext, count = 251, tied = false) {
  const response = await request.post(`${FIXTURES}/seed`, { data: { count, tied } });
  expect(response.status()).toBe(201);
  return response.json() as Promise<{
    email: string; password: string; userId: string; businessUnitId: string; conversationId: string;
    otherConversationId: string; otherBusinessUnitId: string; otherBuConversationId: string;
    phoneNumberId: string; expectedIds: string[];
  }>;
}

async function login(page: Page, email: string, password: string, businessUnitId: string) {
  await page.context().clearCookies();
  await page.goto('/login');
  await page.getByLabel('E-mail').fill(email);
  await page.getByLabel('Senha').fill(password);
  await page.getByRole('button', { name: 'Entrar' }).click();
  await expect(page).toHaveURL(/\/inbox$/);
  await page.getByLabel('Business Unit').selectOption(businessUnitId);
}

async function abrirTimeline(page: Page, request: APIRequestContext, count = 251, tied = false) {
  const fixture = await seed(request, count, tied);
  await login(page, fixture.email, fixture.password, fixture.businessUnitId);
  await page.getByRole('button', { name: 'Cliente Timeline' }).click();
  await expect(page.locator('.bolha')).toHaveCount(Math.min(50, count));
  return fixture;
}

async function audit(request: APIRequestContext, conversationId: string) {
  return request.get(`${FIXTURES}/audit?conversationId=${encodeURIComponent(conversationId)}`).then((r) => r.json());
}

async function triggerIncoming(request: APIRequestContext, data: Record<string, unknown>) {
  const response = await request.post(`${FIXTURES}/incoming`, { data });
  expect(response.status()).toBe(200);
  const webhook = await response.json() as { status: number; body: string };
  expect(webhook.status).toBe(200);
  expect(webhook.body).toBe('EVENT_RECEIVED');
  return webhook;
}

test.describe('timeline da inbox com backend e PostgreSQL reais', () => {
  let pageErrors: string[];
  test.beforeEach(async ({ page }) => {
    pageErrors = [];
    page.on('pageerror', (e) => pageErrors.push(e.message));
  });
  test.afterEach(async () => expect(pageErrors).toEqual([]));

  test('expõe o estado de abertura enquanto a primeira página aguarda o backend', async ({ page, request }) => {
    const fixture = await seed(request, 3);
    let mensagensRecebidas = 0;
    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
      try {
        const frame = JSON.parse(String(payload)) as { tipo?: string; conversaId?: string };
        if (frame.tipo === 'mensagem' && frame.conversaId === fixture.conversationId) mensagensRecebidas += 1;
      } catch { /* frames de conexão não são mensagens */ }
    }));
    await login(page, fixture.email, fixture.password, fixture.businessUnitId);
    let liberar!: () => void;
    let iniciou!: () => void;
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const solicitacao = new Promise<void>((resolve) => { iniciou = resolve; });
    const rotaAbertura = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route(rotaAbertura, async (route) => {
      const response = await route.fetch();
      iniciou();
      await continua;
      await route.fulfill({ response });
    });
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    await solicitacao;
    await expect(page.getByRole('status').filter({ hasText: 'Abrindo conversa…' })).toBeVisible();
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-opening-invalidation', text: 'mensagem chega durante abertura atrasada' });
    await expect.poll(() => mensagensRecebidas).toBe(1);
    liberar();
    await expect(page.locator('.bolha')).toHaveCount(4);
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(expected.unreadCount).toBe(1);
  });

  test('abre a página recente, carrega todas as páginas anteriores e preserva posição', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251, true);
    const timeline = page.locator('.bolhas');
    await timeline.evaluate((el) => { el.scrollTop = 90; });
    const anchor = await timeline.evaluate((el) => {
      const box = el.getBoundingClientRect();
      const child = [...el.querySelectorAll<HTMLElement>('.bolha')].find((item) => item.getBoundingClientRect().bottom > box.top);
      return child ? { id: child.dataset.messageId, offset: child.getBoundingClientRect().top - box.top } : null;
    });
    expect(anchor).not.toBeNull();
    let paginas = 0;
    while (await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).count()) {
      await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
      await expect(page.locator('.bolha')).toHaveCount(Math.min(251, 50 * (paginas + 2)));
      if (paginas === 0 && anchor) {
        await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));
        const depois = await timeline.locator(`[data-message-id="${anchor.id}"]`).evaluate((el) => {
          const pai = el.parentElement!;
          return el.getBoundingClientRect().top - pai.getBoundingClientRect().top;
        });
        expect(Math.abs(depois - anchor.offset)).toBeLessThan(2);
      }
      paginas += 1;
      expect(paginas).toBeLessThan(8);
    }
    await expect(page.getByText('Início do histórico')).toBeVisible();
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(fixture.expectedIds);
    expect(await audit(request, fixture.conversationId).then((r) => r.messages.length)).toBe(251);
  });

  test('reconecta sem evento posterior e recupera 130 mensagens em mais de uma rodada', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251, true);
    const timeline = page.locator('.bolhas');
    const cdp = await page.context().newCDPSession(page);
    await cdp.send('Network.enable');
    await cdp.send('Network.emulateNetworkConditions', { offline: true, latency: 0, downloadThroughput: 0, uploadThroughput: 0 });
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 130, createdAt: Date.now() + 10_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-reconnect-event', text: 'evento para disparar a reconexão' });
    await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: 0, downloadThroughput: -1, uploadThroughput: -1 });

    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible({ timeout: 25_000 });
    // A passagem excedeu o orçamento de três páginas; cada continuação mantém o piso T.
    for (let i = 0; i < 10 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i++) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(150);
    }
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await timeline.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toHaveLength(382);
    expect(expected.unreadCount).toBe(1);
  });

  test('o poll retoma uma rodada pendente sem evento novo nem clique de continuação', async ({ page, request }) => {
    await page.clock.install();
    const fixture = await abrirTimeline(page, request, 251, true);
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 130, createdAt: Date.now() + 10_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-poll-head', text: 'evento que inicia a recuperação via poll' });
    const pending = page.getByText('Atualização pendente. O histórico pode ter uma lacuna.');
    await expect(pending).toBeVisible({ timeout: 25_000 });
    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();

    for (let i = 0; i < 5 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
      await page.clock.fastForward(60_000);
      await expect.poll(async () => await page.locator('.bolha').count()).toBeGreaterThan(50 + i * 100);
    }
    await expect(pending).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toHaveLength(382);
    expect(expected.unreadCount).toBe(1);
  });

  test('recupera o histórico completo após uma thread vazia receber mais de uma página', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 0);
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 130, createdAt: Date.now() - 10_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-first-after-empty', text: 'primeira mensagem depois da abertura vazia' });
    await expect(page.locator('.bolha')).toHaveCount(131, { timeout: 25_000 });
    await expect(page.getByText('Início do histórico')).toBeVisible();
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(expected.unreadCount).toBe(1);
  });

  test('retoma thread vazia após evento entre rodadas e inclui toda a cabeça sem reler', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 0);
    let paginasRecuperacao = 0;
    const rotaRecuperacao = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.get('marcarLida') === 'false';
    await page.route(rotaRecuperacao, async (route) => {
      paginasRecuperacao += 1;
      await route.continue();
    });
    const burst = await request.post(`${FIXTURES}/burst`, { data: { conversationId: fixture.conversationId, count: 160, createdAt: Date.now() + 10_000 } });
    expect(burst.status()).toBe(201);
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-empty-first-head', text: 'primeira cabeça da thread vazia' });
    const pending = page.getByText('Atualização pendente. O histórico pode ter uma lacuna.');
    await expect(pending).toBeVisible({ timeout: 25_000 });
    await expect(page.locator('.bolha')).toHaveCount(150);
    expect(paginasRecuperacao).toBe(3);

    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-empty-between-rounds', text: 'evento enquanto a thread vazia está pausada' });
    await expect.poll(async () => (await audit(request, fixture.conversationId)).unreadCount).toBe(2);
    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
    for (let i = 0; i < 5 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(100);
    }
    await expect(pending).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toHaveLength(162);
    expect(expected.unreadCount).toBe(2);
  });

  test('preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido', async ({ page, request }) => {
    const fixture = await seed(request, 251, true);
    let mensagensRecebidas = 0;
    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
      try {
        const frame = JSON.parse(String(payload)) as { tipo?: string; conversaId?: string };
        if (frame.tipo === 'mensagem' && frame.conversaId === fixture.conversationId) mensagensRecebidas += 1;
      } catch { /* os frames de conexão não representam mensagens */ }
    }));
    await login(page, fixture.email, fixture.password, fixture.businessUnitId);
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    await expect(page.locator('.bolha')).toHaveCount(50);
    let pagesBeforeCursor = 0;
    let requestsRecovery = 0;
    let requestsAtivo = 0;
    let maxRequestsAtivo = 0;
    let captureRequests = true;
    let liberar!: () => void;
    let aguardeSegundaPagina!: () => void;
    let aguardeTerceiraPagina!: () => void;
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const segundaPagina = new Promise<void>((resolve) => { aguardeSegundaPagina = resolve; });
    const terceiraPagina = new Promise<void>((resolve) => { aguardeTerceiraPagina = resolve; });
    let lateId = '';
    const piso = new Date('2026-10-14T12:00:00.000Z').toISOString();
    const rotaTimeline = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route(rotaTimeline, async (route) => {
      if (!captureRequests) return route.continue();
      requestsRecovery += 1;
      requestsAtivo += 1;
      maxRequestsAtivo = Math.max(maxRequestsAtivo, requestsAtivo);
      const pageNumber = requestsRecovery;
      if (new URL(route.request().url()).searchParams.has('antes')) pagesBeforeCursor += 1;
      try {
        const response = await route.fetch();
        if (pageNumber === 2) {
          const cursor = new URL(route.request().url()).searchParams.get('antes')!;
          const cursorPayload = JSON.parse(Buffer.from(cursor.slice(3), 'base64url').toString('utf8')) as { m: string };
          const min = BigInt(`0x${cursorPayload.m.replaceAll('-', '')}`);
          const max = BigInt(`0x${fixture.expectedIds.at(-1)!.replaceAll('-', '')}`);
          lateId = ((min + max) / 2n).toString(16).padStart(32, '0').replace(/(.{8})(.{4})(.{4})(.{4})(.{12})/, '$1-$2-$3-$4-$5');
          expect(lateId > cursorPayload.m).toBe(true);
          expect(lateId < fixture.expectedIds.at(-1)!).toBe(true);
          expect(fixture.expectedIds).not.toContain(lateId);
          const lateTie = await request.post(`${FIXTURES}/late-tie`, { data: { conversationId: fixture.conversationId, id: lateId, createdAt: piso } });
          expect(lateTie.status()).toBe(201);
          for (let i = 1; i <= 10; i += 1) {
            await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-dirty-${i}`, text: `evento coalescido ${i}` });
          }
          await expect.poll(() => mensagensRecebidas).toBe(11);
          aguardeSegundaPagina();
          await continua;
        } else if (pageNumber === 3) {
          expect(new URL(route.request().url()).searchParams.has('antes')).toBe(false);
          aguardeTerceiraPagina();
          const webhook = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-dirty-after-third-page-start', text: 'evento depois de iniciar a terceira consulta' });
          expect(webhook.status).toBe(200);
          await expect.poll(() => mensagensRecebidas).toBe(12);
        }
        await route.fulfill({ response });
      } finally {
        requestsAtivo -= 1;
      }
    });
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-head-H', text: 'nova cabeça H maior que T' });
    await segundaPagina;
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
    liberar();
    await terceiraPagina;
    await expect.poll(() => requestsRecovery).toBe(3);
    await expect.poll(() => requestsAtivo).toBe(0);
    expect(maxRequestsAtivo).toBe(1);
    await page.waitForTimeout(250);
    expect(requestsRecovery).toBe(3);
    captureRequests = false;
    for (let i = 0; i < 12 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i++) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(100);
    }
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(ids).toContain(lateId);
    expect(expected.unreadCount).toBe(12);
  });

  test('falhas de recuperação consomem o orçamento e exigem continuação explícita', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251, true);
    const attemptsStarted: Array<() => void> = [];
    const attemptSignals = Array.from({ length: 3 }, () => new Promise<void>((resolve) => attemptsStarted.push(resolve)));
    const releases: Array<() => void> = [];
    const gates = Array.from({ length: 3 }, () => new Promise<void>((resolve) => releases.push(resolve)));
    let attempts = 0;
    let inFlight = 0;
    let maxInFlight = 0;
    let recoveryRequests = 0;
    let failFirstThree = true;
    const path = `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route((url) => url.pathname === path, async (route) => {
      const url = new URL(route.request().url());
      if (!url.searchParams.has('marcarLida') || url.searchParams.get('marcarLida') !== 'false') return route.continue();
      recoveryRequests += 1;
      inFlight += 1;
      maxInFlight = Math.max(maxInFlight, inFlight);
      const currentAttempt = recoveryRequests;
      try {
        const response = await route.fetch();
        if (failFirstThree && currentAttempt <= 3) {
          attempts += 1;
          attemptsStarted[currentAttempt - 1]();
          await gates[currentAttempt - 1];
          await route.abort('failed');
        } else {
          await route.fulfill({ response });
        }
      } finally {
        inFlight -= 1;
      }
    });

    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-fail-budget-start', text: 'inicia atualização com resposta que falha' });
    for (let i = 0; i < 3; i += 1) {
      await attemptSignals[i];
      const event = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: `timeline-fail-budget-dirty-${i}`, text: `evento durante falha ${i + 1}` });
      expect(event.status).toBe(200);
      releases[i]();
    }

    await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
    expect(attempts).toBe(3);
    expect(recoveryRequests).toBe(3);
    expect(maxInFlight).toBe(1);
    await page.waitForTimeout(300);
    expect(recoveryRequests).toBe(3);

    failFirstThree = false;
    for (let i = 0; i < 8 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
      await page.getByRole('button', { name: 'Continuar atualização' }).click();
      await page.waitForTimeout(100);
    }
    await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
    const expected = await audit(request, fixture.conversationId);
    const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
    expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
    expect(expected.unreadCount).toBe(4);
    expect(maxInFlight).toBe(1);
  });

  test('erro no cursor histórico reinicia pela cabeça após evento novo', async ({ page, request }) => {
    let mensagensRecebidas = 0;
    page.on('websocket', (socket) => socket.on('framereceived', ({ payload }) => {
      try {
        if ((JSON.parse(String(payload)) as { tipo?: string }).tipo === 'mensagem') mensagensRecebidas += 1;
      } catch { /* frames de conexão não representam mensagens */ }
    }));
    const fixture = await abrirTimeline(page, request, 251, true);
    let liberarFalha!: () => void;
    let iniciarPagina!: () => void;
    const barreira = new Promise<void>((resolve) => { liberarFalha = resolve; });
    const paginaIniciada = new Promise<void>((resolve) => { iniciarPagina = resolve; });
    let requestsRecentes = 0;
    let requestsHistoricos = 0;
    let inFlight = 0;
    let maxInFlight = 0;
    const path = `/api/bff/conversations/${fixture.conversationId}/messages`;
    await page.route((url) => url.pathname === path, async (route) => {
      const url = new URL(route.request().url());
      if (url.searchParams.get('marcarLida') !== 'false') return route.continue();
      const historica = url.searchParams.has('antes');
      if (historica) requestsHistoricos += 1;
      else requestsRecentes += 1;
      inFlight += 1;
      maxInFlight = Math.max(maxInFlight, inFlight);
      try {
        const response = await route.fetch();
        if (historica && requestsHistoricos === 1) {
          iniciarPagina();
          await barreira;
          await route.abort('failed');
        } else {
          await route.fulfill({ response });
        }
      } finally {
        inFlight -= 1;
      }
    });

    try {
      await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-cursor-failure-head', text: 'cabeça antes da falha histórica' });
      await expect.poll(() => mensagensRecebidas).toBe(1);
      await paginaIniciada;
      const secondEvent = await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-cursor-failure-during-page', text: 'nova cabeça durante falha histórica' });
      expect(secondEvent.status).toBe(200);
      await expect.poll(() => mensagensRecebidas).toBe(2);
      liberarFalha();

      await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
      await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
      await expect.poll(() => requestsRecentes).toBe(2);
      await expect.poll(() => inFlight).toBe(0);
      expect(requestsHistoricos).toBe(1);
      expect(maxInFlight).toBe(1);

      for (let i = 0; i < 8 && await page.getByRole('button', { name: 'Continuar atualização' }).count(); i += 1) {
        await page.getByRole('button', { name: 'Continuar atualização' }).click();
        await page.waitForTimeout(100);
      }
      await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toHaveCount(0, { timeout: 25_000 });
      const expected = await audit(request, fixture.conversationId);
      const ids = await page.locator('.bolha').evaluateAll((els) => els.map((el) => el.getAttribute('data-message-id')));
      expect(ids).toEqual(expected.messages.map((m: { id: string }) => m.id));
      expect(expected.unreadCount).toBe(2);
      expect(maxInFlight).toBe(1);
    } finally {
      liberarFalha();
      await page.unrouteAll({ behavior: 'wait' });
    }
  });

  test('preserva a âncora quando uma mensagem chega durante o backfill atrasado', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251);
    const timeline = page.locator('.bolhas');
    let iniciar!: () => void;
    let liberar!: () => void;
    const chegou = new Promise<void>((resolve) => { iniciar = resolve; });
    const continua = new Promise<void>((resolve) => { liberar = resolve; });
    const rota = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
    await page.route(rota, async (route) => {
      const response = await route.fetch();
      iniciar();
      await continua;
      await route.fulfill({ response });
    });
    await timeline.evaluate((el) => { el.scrollTop = 80; });
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await chegou;
    await timeline.evaluate((el) => { el.scrollTop = 130; });
    await triggerIncoming(request, { phoneNumberId: fixture.phoneNumberId, id: 'timeline-arrival-during-backfill', text: 'mensagem recebida durante backfill' });
    await expect(page.locator('.bolha')).toHaveCount(51, { timeout: 25_000 });
    const anchor = await timeline.evaluate((el) => {
      const bounds = el.getBoundingClientRect();
      const visible = [...el.querySelectorAll<HTMLElement>('.bolha')].find((item) => item.getBoundingClientRect().bottom > bounds.top);
      return visible ? { id: visible.dataset.messageId, offset: visible.getBoundingClientRect().top - bounds.top } : null;
    });
    expect(anchor).not.toBeNull();
    liberar();
    await expect(page.locator('.bolha')).toHaveCount(101);
    await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));
    const offset = await timeline.locator(`[data-message-id="${anchor!.id}"]`).evaluate((el) => el.getBoundingClientRect().top - el.parentElement!.getBoundingClientRect().top);
    expect(Math.abs(offset - anchor!.offset)).toBeLessThan(2);
  });

  test('mescla envio real com autoria e mantém o novo draft digitado durante o envio', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 4);
    let liberado!: () => void;
    let capturado!: () => void;
    const pronta = new Promise<void>((resolve) => { capturado = resolve; });
    const trava = new Promise<void>((resolve) => { liberado = resolve; });
    await page.route(`**/api/bff/conversations/${fixture.conversationId}/messages`, async (route) => {
      if (route.request().method() !== 'POST') return route.continue();
      const response = await route.fetch();
      capturado();
      await trava;
      await route.fulfill({ response });
    });
    const input = page.getByPlaceholder('Escreva uma resposta');
    await input.fill('resposta persistida');
    await page.getByRole('button', { name: 'Enviar' }).click();
    await pronta;
    await input.fill('rascunho novo');
    liberado();
    await expect(page.locator('.bolha').filter({ hasText: 'resposta persistida' })).toHaveCount(1);
    await expect(input).toHaveValue('rascunho novo');
    const gravado = await audit(request, fixture.conversationId);
    expect(gravado.messages.some((m: { content: string; direction: string; authorName: string }) =>
      m.content === 'resposta persistida' && m.direction === 'OUT' && m.authorName === 'Atendente Timeline')).toBe(true);
  });

  test('mostra thread vazia/fim, falha recuperável e acesso perdido', async ({ page, request }) => {
    const vazia = await abrirTimeline(page, request, 0);
    await expect(page.getByText('Nenhuma mensagem nesta conversa.')).toBeVisible();
    await expect(page.getByText('Início do histórico')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Carregar mensagens anteriores' })).toHaveCount(0);

    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    const cheia = await audit(request, vazia.conversationId);
    expect(cheia.messages).toHaveLength(0);

    const fixture = await abrirTimeline(page, request, 51);
    const caminho = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
    await page.route(caminho, (route) => route.abort('failed'));
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await expect(page.getByText('Falha ao carregar mensagens anteriores.')).toBeVisible();
    await page.unroute(caminho);
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await expect(page.locator('.bolha')).toHaveCount(51);
    await expect(page.getByText('Início do histórico')).toBeVisible();

    const perdida = await abrirTimeline(page, request, 51);
    await request.post(`${FIXTURES}/revoke`, { data: { userId: perdida.userId, businessUnitId: perdida.businessUnitId } });
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await expect(page.getByText('Acesso à conversa perdido.')).toBeVisible();
  });

  test('close vence resposta de backfill atrasada', async ({ page, request }) => {
    const fixture = await abrirTimeline(page, request, 251);
    let liberarBackfill!: () => void;
    let backfillRecebido!: () => void;
    const continua = new Promise<void>((resolve) => { liberarBackfill = resolve; });
    const chegou = new Promise<void>((resolve) => { backfillRecebido = resolve; });
    const rotaBackfill = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages` && url.searchParams.has('antes');
    await page.route(rotaBackfill, async (route) => {
      const response = await route.fetch();
      backfillRecebido();
      await continua;
      await route.fulfill({ response });
    });
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    await chegou;
    await page.getByRole('button', { name: 'Finalizar' }).click();
    await expect.poll(async () => (await audit(request, fixture.conversationId)).status).toBe('CLOSED');
    liberarBackfill();
    await expect(page.getByText('CLOSED', { exact: true })).toBeVisible();
  });

  test('troca de conversa e BU protege resposta atrasada de envio', async ({ page, request }) => {
    test.setTimeout(30_000);
    const fixture = await abrirTimeline(page, request, 251);
    const secundaria = fixture.otherConversationId;
    const outraBu = fixture.otherBuConversationId;
    const populateSecondary = await request.post(`${FIXTURES}/burst`, { data: { conversationId: secundaria, count: 80, createdAt: Date.now() - 10_000 } });
    const populateOtherBu = await request.post(`${FIXTURES}/burst`, { data: { conversationId: outraBu, count: 80, createdAt: Date.now() - 10_000 } });
    expect(populateSecondary.status()).toBe(201);
    expect(populateOtherBu.status()).toBe(201);

    const holdRequest = async (conversationId: string, method: 'POST' | 'GET', fail = false) => {
      let release!: () => void;
      let started!: () => void;
      let settled!: () => void;
      const gate = new Promise<void>((resolve) => { release = resolve; });
      const received = new Promise<void>((resolve) => { started = resolve; });
      const finished = new Promise<void>((resolve) => { settled = resolve; });
      const predicate = (url: URL) => url.pathname === `/api/bff/conversations/${conversationId}/messages` && (method === 'POST' ? url.search === '' : url.searchParams.has('antes'));
      await page.route(predicate, async (route) => {
        if (route.request().method() !== method) return route.continue();
        if (method === 'GET' && !new URL(route.request().url()).searchParams.has('antes')) return route.continue();
        try {
          const response = fail ? undefined : await route.fetch();
          started();
          await gate;
          if (fail) await route.abort('failed');
          else await route.fulfill({ response });
        } finally {
          settled();
        }
      });
      return { predicate, started: received, release, finished, remove: () => page.unroute(predicate) };
    };

    const destinationSnapshot = async (draftText: string) => {
      const draft = page.getByPlaceholder('Escreva uma resposta');
      await expect(draft).toBeVisible();
      await draft.fill(draftText);
      const timeline = page.locator('.bolhas');
      const scrollTop = await timeline.evaluate((el) => {
        el.scrollTop = Math.min(120, el.scrollHeight - el.clientHeight);
        return el.scrollTop;
      });
      return {
        draftText,
        active: await page.locator('.item.ativo').innerText(),
        metadata: await page.locator('.inbox > .cartao.grade .linha').first().innerText(),
        ids: await timeline.evaluate((el) => [...el.querySelectorAll<HTMLElement>('.bolha')].map((item) => item.dataset.messageId)),
        scrollTop,
      };
    };
    const expectDestinationUnchanged = async (snapshot: Awaited<ReturnType<typeof destinationSnapshot>>) => {
      expect((await page.locator('.item.ativo').innerText()).replace(/\s+/g, ' ').trim()).toBe(snapshot.active.replace(/\s+/g, ' ').trim());
      expect((await page.locator('.inbox > .cartao.grade .linha').first().innerText()).replace(/\s+/g, ' ').trim()).toBe(snapshot.metadata.replace(/\s+/g, ' ').trim());
      await expect(page.getByPlaceholder('Escreva uma resposta')).toHaveValue(snapshot.draftText);
      await expect(page.getByRole('alert')).toHaveCount(0);
      const timeline = page.locator('.bolhas');
      expect(await timeline.evaluate((el) => [...el.querySelectorAll<HTMLElement>('.bolha')].map((item) => item.dataset.messageId))).toEqual(snapshot.ids);
      expect(await timeline.evaluate((el) => el.scrollTop)).toBe(snapshot.scrollTop);
    };
    const openConversation = async (name: string, tab: 'Na fila' | 'Em atendimento' = 'Na fila', count = 50) => {
      await page.getByRole('button', { name: tab }).click();
      await page.getByRole('button', { name }).click();
      await expect(page.locator('.bolha')).toHaveCount(count);
    };
    const openOtherBu = async () => {
      await page.getByLabel('Business Unit').selectOption(fixture.otherBusinessUnitId);
      await page.getByRole('button', { name: 'Na fila' }).click();
      await page.getByRole('button', { name: 'Cliente Outra BU' }).click();
      await expect(page.locator('.bolha')).toHaveCount(50);
    };
    const sendAndSwitch = async (context: 'conversation' | 'bu', fail: boolean, text: string, draftText: string) => {
      const hold = await holdRequest(secundaria, 'POST', fail);
      const input = page.getByPlaceholder('Escreva uma resposta');
      await input.fill(text);
      await page.getByRole('button', { name: 'Enviar' }).click();
      try {
        await hold.started;
        if (context === 'conversation') await openConversation('Cliente Timeline', 'Na fila', 50);
        else await openOtherBu();
        const snapshot = await destinationSnapshot(draftText);
        hold.release();
        await hold.finished;
        await page.waitForTimeout(100);
        await expectDestinationUnchanged(snapshot);
        return snapshot;
      } finally {
        hold.release();
        await hold.remove();
      }
    };

    await openConversation('Cliente Secundário');
    await sendAndSwitch('conversation', false, 'envio antigo sucesso conversa', 'rascunho destino conversa');
    const afterSuccess = await audit(request, secundaria);
    expect(afterSuccess.messages.some((m: { content: string; direction: string }) => m.content === 'envio antigo sucesso conversa' && m.direction === 'OUT')).toBe(true);

    await openConversation('Cliente Secundário', 'Em atendimento');
    await sendAndSwitch('conversation', true, 'envio antigo falho conversa', 'rascunho apos falha conversa');
    const afterFailure = await audit(request, secundaria);
    expect(afterFailure.messages.some((m: { content: string }) => m.content === 'envio antigo falho conversa')).toBe(false);

    const holdBackfillConversation = await holdRequest(fixture.conversationId, 'GET');
    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    try {
      await holdBackfillConversation.started;
      await openConversation('Cliente Secundário', 'Em atendimento');
      const backfillDestination = await destinationSnapshot('rascunho apos backfill conversa');
      holdBackfillConversation.release();
      await holdBackfillConversation.finished;
      await expectDestinationUnchanged(backfillDestination);
    } finally {
      holdBackfillConversation.release();
      await holdBackfillConversation.remove();
    }

    await sendAndSwitch('bu', false, 'envio antigo sucesso BU', 'rascunho destino BU');
    const buSuccess = await audit(request, secundaria);
    expect(buSuccess.messages.some((m: { content: string; direction: string }) => m.content === 'envio antigo sucesso BU' && m.direction === 'OUT')).toBe(true);

    await page.getByLabel('Business Unit').selectOption(fixture.businessUnitId);
    await openConversation('Cliente Secundário', 'Em atendimento');
    await sendAndSwitch('bu', true, 'envio antigo falho BU', 'rascunho apos falha BU');
    const buFailure = await audit(request, secundaria);
    expect(buFailure.messages.some((m: { content: string }) => m.content === 'envio antigo falho BU')).toBe(false);

    await page.getByLabel('Business Unit').selectOption(fixture.businessUnitId);
    await openConversation('Cliente Timeline', 'Na fila', 50);
    const holdBackfillBu = await holdRequest(fixture.conversationId, 'GET');
    await page.getByRole('button', { name: 'Carregar mensagens anteriores' }).click();
    try {
      await holdBackfillBu.started;
      await openOtherBu();
      const otherBuSnapshot = await destinationSnapshot('rascunho apos backfill BU');
      holdBackfillBu.release();
      await holdBackfillBu.finished;
      await expectDestinationUnchanged(otherBuSnapshot);
    } finally {
      holdBackfillBu.release();
      await holdBackfillBu.remove();
    }
  });
});

```

## web-app/e2e/timeline-freshness.ts
```
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
import { mkdir, readdir, readFile, writeFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';

const hash = (value: Buffer | string) => createHash('sha256').update(value).digest('hex');

async function manifest(directory: string): Promise<Array<{ path: string; sha256: string }>> {
  const entries: Array<{ path: string; sha256: string }> = [];
  async function visit(current: string): Promise<void> {
    for (const entry of await readdir(current, { withFileTypes: true })) {
      const absolute = join(current, entry.name);
      if (entry.isDirectory()) await visit(absolute);
      else entries.push({ path: absolute.slice(directory.length + 1), sha256: hash(await readFile(absolute)) });
    }
  }
  await visit(directory);
  return entries.sort((a, b) => a.path.localeCompare(b.path));
}

function changedSourceFiles(directory: string): Array<{ path: string; sha256: string }> {
  const gitArgs = ['-c', `safe.directory=${directory}`, '-C', directory];
  const changed = execFileSync('git', [...gitArgs, 'diff', '--name-only', '--diff-filter=ACDMRTUXB'], { encoding: 'utf8' }).trim().split('\n').filter(Boolean);
  const untracked = execFileSync('git', [...gitArgs, 'ls-files', '--others', '--exclude-standard'], { encoding: 'utf8' }).trim().split('\n').filter(Boolean);
  const files = [...new Set([...changed, ...untracked])].filter((path) => /^(src\/|test\/|e2e\/|[^/]*config\.[^/]+$)/.test(path));
  return files.sort().map((path) => ({ path, sha256: hash(readFileSync(resolve(directory, path))) }));
}

export default async function timelineFreshness(): Promise<void> {
  const web = process.cwd();
  const root = resolve(web, '..');
  const api = join(root, 'api-app');
  const runtime = process.version;
  if (!/^v22\./.test(runtime)) throw new Error(`Attestation timeline exige Node 22; recebeu ${runtime}`);

  const databaseUrl = process.env.LEADSHUG_E2E_DATABASE_URL;
  if (!databaseUrl) throw new Error('LEADSHUG_E2E_DATABASE_URL ausente durante attestation.');
  const db = new URL(databaseUrl);
  const database = decodeURIComponent(db.pathname.slice(1));
  if (!database.startsWith('leadshug_timeline_')) throw new Error(`Banco fora da família descartável: ${database}`);

  const apiPort = process.env.LEADSHUG_API_PORT ?? '3100';
  const apiEndpoint = `http://127.0.0.1:${apiPort}`;
  const [apiHealth, fixtureHealth, htmlResponse] = await Promise.all([
    fetch(`${apiEndpoint}/health`),
    fetch('http://127.0.0.1:3101/health'),
    fetch('http://127.0.0.1:4173/'),
  ]);
  for (const [label, response] of [['API', apiHealth], ['fixtures', fixtureHealth], ['preview', htmlResponse]] as const) {
    if (!response.ok) throw new Error(`${label} indisponível na attestation: HTTP ${response.status}`);
  }
  const html = await htmlResponse.text();
  const asset = html.match(/src="([^"]+\.js)"/);
  if (!asset) throw new Error('HTML servido não referencia o bundle JavaScript esperado.');
  const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173'));
  if (!jsResponse.ok) throw new Error(`Bundle servido retornou HTTP ${jsResponse.status}`);
  const servedJs = Buffer.from(await jsResponse.arrayBuffer());
  const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`);
  const distJs = await readFile(servedPath);
  if (hash(servedJs) !== hash(distJs)) throw new Error('Bundle servido não corresponde ao artefato em web-app/dist.');

  const gitArgs = (directory: string, ...args: string[]) => ['-c', `safe.directory=${directory}`, '-C', directory, ...args];
  const git = (directory: string, ...args: string[]) => execFileSync('git', gitArgs(directory, ...args), { encoding: 'utf8' }).trim();
  const diffHash = (directory: string) => hash(execFileSync('git', gitArgs(directory, 'diff', '--no-ext-diff', '--binary')));
  const requireFromApi = createRequire(join(api, 'package.json'));
  const { PrismaClient } = requireFromApi('@prisma/client') as { PrismaClient: new (options: { datasources: { db: { url: string } } }) => any };
  const prisma = new PrismaClient({ datasources: { db: { url: databaseUrl } } });
  let completedMigrations: number;
  try {
    const rows = await prisma.$queryRawUnsafe('SELECT COUNT(*)::int AS count FROM "_prisma_migrations" WHERE finished_at IS NOT NULL AND rolled_back_at IS NULL') as Array<{ count: number }>;
    completedMigrations = Number(rows[0]?.count ?? 0);
  } finally {
    await prisma.$disconnect();
  }

  const artifactDirectory = resolve(root, 'foundation_documentation/artifacts/tmp/inbox-timeline-execution');
  await mkdir(artifactDirectory, { recursive: true });
  await writeFile(join(artifactDirectory, 'served-index-authority.html'), html);
  await writeFile(join(artifactDirectory, 'served-app-authority.js'), servedJs);
  const runId = process.env.LEADSHUG_ATTESTATION_RUN_ID ?? new Date().toISOString().replace(/[:.]/g, '-');
  if (!/^[A-Za-z0-9_-]+$/.test(runId)) throw new Error('LEADSHUG_ATTESTATION_RUN_ID contém caracteres inválidos.');
  const attestation = {
    capturedAtUtc: new Date().toISOString(),
    runId,
    branch: {
      api: { name: git(api, 'branch', '--show-current'), head: git(api, 'rev-parse', 'HEAD'), diffSha256: diffHash(api), sourceManifest: changedSourceFiles(api) },
      web: { name: git(web, 'branch', '--show-current'), head: git(web, 'rev-parse', 'HEAD'), diffSha256: diffHash(web), sourceManifest: changedSourceFiles(web) },
    },
    runtime,
    database: { name: database, endpoint: `${db.protocol}//${db.hostname}:${db.port || '5432'}/${database}`, completedMigrations },
    endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname },
    servedBundleSha256: hash(servedJs),
    distBundleSha256: hash(distJs),
    apiBuildManifest: await manifest(join(api, 'dist')),
    webDistManifest: await manifest(join(web, 'dist')),
  };
  const serialized = `${JSON.stringify(attestation, null, 2)}\n`;
  await writeFile(join(artifactDirectory, `attestation-browser-${runId}.json`), serialized);
  await writeFile(join(artifactDirectory, 'attestation-browser-authority.json'), serialized);
}

```

## web-app/playwright.config.ts
```
import { defineConfig } from '@playwright/test';

/** Porta própria: a 3000 desta máquina é de outro projeto. */
const PORTA_DA_API = process.env.LEADSHUG_API_PORT ?? '3100';
const API = `http://127.0.0.1:${PORTA_DA_API}`;
const DATABASE_URL = process.env.LEADSHUG_E2E_DATABASE_URL;
if (!DATABASE_URL) throw new Error('LEADSHUG_E2E_DATABASE_URL precisa apontar para o banco descartável dedicado.');

/**
 * Teste de navegador contra a tela **buildada**, não contra o dev server.
 *
 * O que ele existe para pegar é justamente o que o teste de API não pega: erro
 * de renderização, tela branca, rota que não leva a lugar nenhum. Foi assim que
 * "Cannot read properties of undefined" apareceu — depois de o QA topar com ela.
 *
 * Sobe dois processos: a API (com o Postgres local do docker compose) e o
 * `vite preview` servindo o `dist`. Mesma origem, como em desenvolvimento.
 */
export default defineConfig({
  globalSetup: './e2e/timeline-freshness.ts',
  testDir: './e2e',
  timeout: 30_000,
  fullyParallel: false,
  workers: 1,
  use: {
    baseURL: 'http://127.0.0.1:4173',
    trace: 'retain-on-failure',
  },
  webServer: [
    {
      command: 'node ../api-app/test/timeline-fixtures.cjs',
      url: 'http://127.0.0.1:3101/health',
      reuseExistingServer: false,
      timeout: 30_000,
      stdout: 'pipe',
      stderr: 'pipe',
      env: {
        DATABASE_URL,
        LEADSHUG_E2E_DATABASE_URL: DATABASE_URL,
        LEADSHUG_API_PORT: PORTA_DA_API,
        LEADSHUG_FIXTURE_PORT: '3101',
      },
    },
    {
      // `build &&` NÃO é zelo: `npm run start` da api é `node dist/main.js`, e
      // sem construir antes o teste de tela valida uma API VELHA — que é o
      // oposto do que ele existe para fazer. Foi assim que uma mudança de schema
      // passou por aqui reportando 500 de um dist de duas fases atrás.
      command: 'npm --prefix ../api-app run build && node ../api-app/test/browser-server.cjs',
      url: `${API}/health`,
      // Não reaproveitar: esta máquina roda outros serviços, e "já tem algo na
      // porta" foi o que fez a primeira corrida testar o projeto vizinho.
      reuseExistingServer: false,
      // 60s cobriam só o `start`; o comando passou a incluir o build, e num
      // runner frio isso não cabia.
      timeout: 180_000,
      // O log do servidor SOBE para a saída do teste.
      //
      // Sem isto, uma falha de boot aparece só como "Timed out waiting from
      // config.webServer" — sem uma linha do que a API disse. Foi exatamente
      // assim que este erro chegou do CI: um timeout, e nenhuma pista.
      stdout: 'pipe',
      stderr: 'pipe',
      env: {
        // O `.env` da API pode apontar para outro Postgres local (por exemplo,
        // o serviço legado na 5433). O harness deve ser determinístico e falar
        // com o Postgres deste compose, publicado na 55433.
        DATABASE_URL,
        LEADSHUG_E2E_DATABASE_URL: DATABASE_URL,
        SESSION_SECRET: 'segredo-de-e2e',
        INTERNAL_SERVICE_TOKEN: 'token-de-e2e',
        // O canal oficial é o PISO do produto: sem ele o processo não sobe
        // (ADR-0016, Emenda 2 §1).
        WHATSAPP_TOKEN: 'token-de-e2e',
        // Volume de arquivo (ADR-0024). Sem ele o produto recusa upload — e o
        // teste de tela precisa exercitar o caminho que EXISTE em stage.
        LH_ARQUIVOS_DIR: '/tmp/leadshug-arquivos-e2e',
        // O link do convite é montado com isto (ADR-0025): sem ele, o e-mail sai
        // com caminho relativo, que não abre em lugar nenhum.
        WEB_ORIGIN: 'http://127.0.0.1:4173',
        PORT: PORTA_DA_API,
      },
    },
    {
      // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`,
      // e quem resolve esse nome é o sistema. Nesta máquina ele dá só IPv4; no
      // runner do GitHub o `/etc/hosts` põe `::1` primeiro, o servidor sobe em
      // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em
      // porta fechada. O log mostrava o preview NO AR e o teste estourando 60s.
      //
      // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o
      // CORS da API. Só a ponta que ESCUTA ficava a cargo do resolvedor.
      command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort',
      stdout: 'pipe',
      stderr: 'pipe',
      env: { LEADSHUG_API: API },
      url: 'http://127.0.0.1:4173',
      reuseExistingServer: false,
      timeout: 60_000,
    },
  ],
});

```

## web-app/package.json
```
{
  "name": "@leadshug/web",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview",
    "test": "vitest run",
    "test:tela": "npm run build && playwright test",
    "test:tela:ui": "playwright test --ui"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.28.0"
  },
  "devDependencies": {
    "@playwright/test": "^1.62.1",
    "@types/react": "^18.3.12",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.3.4",
    "typescript": "^5.6.0",
    "vite": "^5.4.11",
    "vitest": "^2.1.0"
  }
}

```

## api-app/src/domain/inbox/timeline-pagination.ts
```
import { BadRequestException } from '@nestjs/common';

export const LIMITE_TIMELINE_PADRAO = 50;
export const LIMITE_TIMELINE_MAXIMO = 100;
const PREFIXO_CURSOR = 'v1.';

export interface ConsultaTimeline {
  limite: number;
  antes: string | null;
  marcarLida: boolean;
}

function invalida(): never {
  throw new BadRequestException({ error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA' });
}

function unico(q: Record<string, unknown>, chave: string): string | undefined {
  const valor = q[chave];
  if (valor === undefined) return undefined;
  if (typeof valor !== 'string') return invalida();
  return valor;
}

export function validarConsultaTimeline(q: Record<string, unknown>): ConsultaTimeline {
  const rawLimite = unico(q, 'limite');
  let limite = LIMITE_TIMELINE_PADRAO;
  if (rawLimite !== undefined) {
    if (!/^(0|[1-9][0-9]*)$/.test(rawLimite)) return invalida();
    limite = Number(rawLimite);
    if (!Number.isSafeInteger(limite) || limite < 1 || limite > LIMITE_TIMELINE_MAXIMO) return invalida();
  }

  const antes = unico(q, 'antes');
  if (antes !== undefined && (antes.length === 0 || antes.length > 256)) return invalida();
  const rawMarcarLida = unico(q, 'marcarLida');
  if (rawMarcarLida !== undefined && rawMarcarLida !== 'true' && rawMarcarLida !== 'false') return invalida();
  if (antes !== undefined && rawMarcarLida === 'true') return invalida();

  return { limite, antes: antes ?? null, marcarLida: antes === undefined && rawMarcarLida !== 'false' };
}

export function criarCursorTimeline(conversaId: string, mensagemId: string): string {
  return PREFIXO_CURSOR + Buffer.from(JSON.stringify({ c: conversaId, m: mensagemId })).toString('base64url');
}

export function lerCursorTimeline(cursor: string): { conversaId: string; mensagemId: string } {
  if (!cursor.startsWith(PREFIXO_CURSOR) || cursor.length > 256) return invalida();
  try {
    const encoded = cursor.slice(PREFIXO_CURSOR.length);
    const json = Buffer.from(encoded, 'base64url').toString('utf8');
    const valor: unknown = JSON.parse(json);
    if (
      !valor || typeof valor !== 'object' ||
      typeof (valor as { c?: unknown }).c !== 'string' ||
      typeof (valor as { m?: unknown }).m !== 'string' ||
      Buffer.from(json).toString('base64url') !== encoded
    ) return invalida();
    return { conversaId: (valor as { c: string }).c, mensagemId: (valor as { m: string }).m };
  } catch {
    return invalida();
  }
}

```

## api-app/test/browser-server.cjs
```
const { Test } = require('@nestjs/testing');
const { AppModule } = require('../dist/app.module.js');
const { META_CLIENT } = require('../dist/integrations/meta/meta.client.js');
const { EVOLUTION_CLIENT } = require('../dist/integrations/evolution/evolution.client.js');
const { configurarBodyParsers } = require('../dist/infra/http/body-parsers.js');
const { RealtimeService } = require('../dist/realtime/realtime.service.js');
const { PrismaService } = require('../dist/infra/prisma/prisma.service.js');

async function main() {
  const db = process.env.DATABASE_URL;
  const fixtureDb = process.env.LEADSHUG_E2E_DATABASE_URL;
  if (!db || db !== fixtureDb) throw new Error('O servidor de browser requer DATABASE_URL igual ao banco dedicado de E2E.');
  const dbName = new URL(db).pathname.slice(1).split('?')[0];
  if (!dbName.startsWith('leadshug_timeline_')) throw new Error('O servidor de browser aceita apenas banco leadshug_timeline_* descartável.');
  process.env.SESSION_SECRET = 'segredo-de-e2e';
  process.env.INTERNAL_SERVICE_TOKEN = 'token-de-e2e';
  process.env.META_APP_SECRET = 'segredo-do-app-meta';
  process.env.EVOLUTION_WEBHOOK_SECRET = 'segredo-do-caminho-evolution';
  process.env.WEBHOOK_VERIFY_TOKEN = 'verify-token-de-teste';
  process.env.WHATSAPP_TOKEN = 'token-de-e2e';
  process.env.LH_ARQUIVOS_DIR = '/tmp/leadshug-arquivos-e2e';
  process.env.WEB_ORIGIN = 'http://127.0.0.1:4173';

  const fake = {
    configurado: () => true,
    async enviarTexto(_canal, _contato, texto) { fake.enviados.push(texto); return `e2e-${fake.enviados.length}`; },
    async numerosDaWaba(id) { return [{ id: `phone-${id}`, telefone: '5584999990000', nomeVerificado: 'E2E' }]; },
    async criarInstancia() { return { qrcode: 'data:image/png;base64,QR' }; },
    async qrDaInstancia() { return 'data:image/png;base64,QR'; },
    async estadoDaInstancia() { return 'open'; },
    async apagarInstancia() {},
    enviados: [],
  };
  const moduleRef = await Test.createTestingModule({ imports: [AppModule] })
    .overrideProvider(META_CLIENT).useValue(fake)
    .overrideProvider(EVOLUTION_CLIENT).useValue(fake)
    .compile();
  const app = moduleRef.createNestApplication({ bodyParser: false });
  configurarBodyParsers(app);
  app.enableCors({ origin: ['http://127.0.0.1:4173'], credentials: true });
  await app.init();
  app.get(RealtimeService).ligar(app.getHttpServer());
  await app.listen(Number(process.env.PORT ?? '3100'), '0.0.0.0');
  const close = async () => { await app.get(PrismaService).$disconnect(); await app.close(); };
  process.on('SIGTERM', () => void close().finally(() => process.exit(0)));
  process.on('SIGINT', () => void close().finally(() => process.exit(0)));
  console.log(`timeline test API listening on ${process.env.PORT ?? '3100'}; database ${dbName}`);
}

main().catch((error) => { console.error(error); process.exit(1); });

```

## api-app/test/timeline-fixtures.cjs
```
const http = require('node:http');
const { createHmac } = require('node:crypto');
const bcrypt = require('bcryptjs');
const { PrismaClient } = require('@prisma/client');

const databaseUrl = process.env.DATABASE_URL;
const dedicatedUrl = process.env.LEADSHUG_E2E_DATABASE_URL;
const fixturePort = Number(process.env.LEADSHUG_FIXTURE_PORT ?? '3101');
const apiPort = Number(process.env.LEADSHUG_API_PORT ?? '3100');
if (!databaseUrl || databaseUrl !== dedicatedUrl) throw new Error('Fixtures exigem DATABASE_URL igual ao banco descartável de E2E.');
if (!new URL(databaseUrl).pathname.slice(1).split('?')[0].startsWith('leadshug_timeline_')) throw new Error('Fixtures aceitam apenas banco leadshug_timeline_* descartável.');

const prisma = new PrismaClient({ datasources: { db: { url: databaseUrl } } });
const json = (res, status, body) => { res.writeHead(status, { 'content-type': 'application/json' }); res.end(JSON.stringify(body)); };
const bodyOf = (req) => new Promise((resolve, reject) => {
  let raw = '';
  req.on('data', (chunk) => { raw += chunk; if (raw.length > 100_000) reject(new Error('body too large')); });
  req.on('end', () => { try { resolve(JSON.parse(raw || '{}')); } catch (e) { reject(e); } });
  req.on('error', reject);
});

async function seed(data) {
  const suffix = `${Date.now()}-${Math.random().toString(16).slice(2)}`;
  const mantenedora = await prisma.mantenedora.create({ data: { name: `Timeline ${suffix}` } });
  const setor = await prisma.setor.create({ data: { mantenedoraId: mantenedora.id, name: 'Geral' } });
  const businessUnit = await prisma.businessUnit.create({ data: { mantenedoraId: mantenedora.id, setorId: setor.id, name: 'Número timeline', phone: `5584${String(Date.now()).slice(-8)}` } });
  await prisma.mantenedoraSettings.create({ data: { mantenedoraId: mantenedora.id, onboardingConcluido: true, modulos: { canalNaoOficial: false } } });
  const email = `timeline-${suffix}@teste.local`;
  const user = await prisma.appUser.create({ data: {
    mantenedoraId: mantenedora.id, name: 'Atendente Timeline', email,
    passwordHash: await bcrypt.hash('senha-de-teste-1', 10),
  } });
  await prisma.userBuRole.create({ data: { userId: user.id, buId: businessUnit.id, role: 'OWNER', grantedViaTipo: 'DIRETO' } });
  const phoneNumberId = `timeline-phone-${suffix}`;
  await prisma.buChannel.create({ data: { buId: businessUnit.id, type: 'OFICIAL', phoneNumberId, requiresWindow: false, status: 'CONECTADO' } });
  const conversation = await prisma.conversation.create({ data: { buId: businessUnit.id, contact: '5584911112222', displayName: 'Cliente Timeline', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 0 } });
  const otherConversation = await prisma.conversation.create({ data: { buId: businessUnit.id, contact: '5584933334444', displayName: 'Cliente Secundário', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 0 } });
  const otherBu = await prisma.businessUnit.create({ data: { mantenedoraId: mantenedora.id, setorId: setor.id, name: 'Número alternativo', phone: `5585${String(Date.now()).slice(-8)}` } });
  await prisma.userBuRole.create({ data: { userId: user.id, buId: otherBu.id, role: 'OWNER', grantedViaTipo: 'DIRETO' } });
  const otherBuPhoneNumberId = `timeline-phone-other-${suffix}`;
  await prisma.buChannel.create({ data: { buId: otherBu.id, type: 'OFICIAL', phoneNumberId: otherBuPhoneNumberId, requiresWindow: false, status: 'CONECTADO' } });
  const otherBuConversation = await prisma.conversation.create({ data: { buId: otherBu.id, contact: '5585555555555', displayName: 'Cliente Outra BU', contactType: 'PESSOA', status: 'QUEUED' } });
  const count = Math.max(0, Math.min(Number(data.count ?? 251), 10_000));
  const tiedAt = new Date('2026-10-14T12:00:00.000Z');
  const messages = Array.from({ length: count }, (_, i) => ({
    conversationId: conversation.id, buId: businessUnit.id, direction: 'IN', messageType: 'TEXTO',
    content: `histórico ${i + 1}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
    createdAt: data.tied === true ? tiedAt : new Date(tiedAt.getTime() + i * 1000),
  }));
  if (messages.length) await prisma.message.createMany({ data: messages });
  const expectedIds = await prisma.message.findMany({ where: { conversationId: conversation.id }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true } });
  return { email, password: 'senha-de-teste-1', userId: user.id, mantenedoraId: mantenedora.id, businessUnitId: businessUnit.id, conversationId: conversation.id, otherConversationId: otherConversation.id, otherBusinessUnitId: otherBu.id, otherBuConversationId: otherBuConversation.id, otherBuPhoneNumberId, phoneNumberId, count, expectedIds: expectedIds.map((m) => m.id) };
}

async function incoming(data) {
  const id = String(data.id ?? `timeline-event-${Date.now()}`);
  const payload = { entry: [{ changes: [{ field: 'messages', value: {
    metadata: { phone_number_id: data.phoneNumberId },
    contacts: [{ profile: { name: 'Cliente Timeline' } }],
    messages: [{ id, from: '5584911112222', type: 'text', text: { body: String(data.text ?? id) } }],
  } }] }] };
  const raw = JSON.stringify(payload);
  const signature = 'sha256=' + createHmac('sha256', 'segredo-do-app-meta').update(raw).digest('hex');
  const response = await fetch(`http://127.0.0.1:${apiPort}/webhooks/meta`, {
    method: 'POST', headers: { 'content-type': 'application/json', 'x-hub-signature-256': signature }, body: raw,
  });
  return { status: response.status, body: await response.text() };
}

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === 'GET' && req.url === '/health') return json(res, 200, { status: 'ok' });
    const data = await bodyOf(req);
    if (req.method === 'GET' && req.url.startsWith('/audit?')) {
      const query = new URL(req.url, 'http://localhost').searchParams;
      const conversationId = query.get('conversationId');
      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
      const messages = await prisma.message.findMany({ where: { conversationId }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true, content: true, direction: true, authorName: true, createdAt: true } });
      return json(res, 200, { status: conversation.status, unreadCount: conversation.unreadCount, messages });
    }
    if (req.method === 'POST' && req.url === '/seed') return json(res, 201, await seed(data));
    if (req.method === 'POST' && req.url === '/incoming') return json(res, 200, await incoming(data));
    if (req.method === 'POST' && req.url === '/late-tie') {
      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: data.conversationId } });
      const message = await prisma.message.create({ data: {
        id: String(data.id), conversationId: conversation.id, buId: conversation.buId,
        direction: 'IN', messageType: 'TEXTO', content: 'inserção empatada tardia',
        channelOrigin: 'OFICIAL', status: 'RECEBIDA', createdAt: new Date(data.createdAt),
      } });
      return json(res, 201, { id: message.id });
    }
    if (req.method === 'POST' && req.url === '/revoke') {
      await prisma.userBuRole.deleteMany({ where: { userId: data.userId, buId: data.businessUnitId } });
      return json(res, 200, { revoked: true });
    }
    if (req.method === 'POST' && req.url === '/burst') {
      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: data.conversationId } });
      const count = Math.max(1, Math.min(Number(data.count ?? 120), 500));
      const base = new Date(data.createdAt ?? Date.now());
      await prisma.message.createMany({ data: Array.from({ length: count }, (_, i) => ({
        conversationId: conversation.id, buId: conversation.buId, direction: 'IN', messageType: 'TEXTO',
        content: `burst ${i + 1}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
        createdAt: new Date(base.getTime() + i),
      })) });
      return json(res, 201, { count });
    }
    return json(res, 404, { error: 'not found' });
  } catch (error) {
    console.error(error);
    return json(res, 500, { error: error instanceof Error ? error.message : String(error) });
  }
});
server.listen(fixturePort, '127.0.0.1', () => console.log(`timeline fixtures listening on 127.0.0.1:${fixturePort}`));
process.on('SIGTERM', () => server.close(() => prisma.$disconnect().finally(() => process.exit(0))));
process.on('SIGINT', () => server.close(() => prisma.$disconnect().finally(() => process.exit(0))));

```

## api-app/package.json
```
{
  "name": "@leadshug/api",
  "version": "0.1.0",
  "private": true,
  "description": "Núcleo unificado do LeadsHug — NestJS, quatro superfícies de entrada",
  "scripts": {
    "build": "nest build",
    "start": "node dist/main.js",
    "start:dev": "nest start --watch",
    "lint": "eslint \"{src,test}/**/*.ts\"",
    "test": "vitest run --config vitest.config.ts",
    "test:cov": "vitest run --coverage --config vitest.config.cov.ts",
    "test:e2e": "vitest run --config vitest.config.e2e.ts --no-file-parallelism --maxWorkers=1",
    "prisma:generate": "prisma generate",
    "prisma:migrate": "prisma migrate deploy",
    "prisma:dev": "prisma migrate dev"
  },
  "dependencies": {
    "@nestjs/common": "^11.0.0",
    "@nestjs/core": "^11.0.0",
    "@nestjs/platform-express": "^11.0.0",
    "@nestjs/schedule": "^6.1.3",
    "@prisma/client": "^6.0.0",
    "bcryptjs": "^2.4.3",
    "express": "^5.2.1",
    "prisma": "^6.0.0",
    "reflect-metadata": "^0.2.2",
    "rxjs": "^7.8.1",
    "ws": "^8.21.3"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@nestjs/cli": "^11.0.0",
    "@nestjs/schematics": "^11.0.0",
    "@nestjs/testing": "^11.0.0",
    "@types/bcryptjs": "^2.4.6",
    "@types/express": "^5.0.0",
    "@types/multer": "^2.2.0",
    "@types/node": "^22.0.0",
    "@types/supertest": "^6.0.2",
    "@types/ws": "^8.18.1",
    "@vitest/coverage-v8": "^2.1.0",
    "eslint": "^10.8.1",
    "supertest": "^7.0.0",
    "typescript": "^5.6.0",
    "typescript-eslint": "^8.67.0",
    "unplugin-swc": "^1.5.1",
    "vitest": "^2.1.0"
  },
  "engines": {
    "node": ">=22"
  }
}

```

## delphi-ai/skills/test-quality-audit/SKILL.md
```
---
name: test-quality-audit
description: "Audit stack-aware test quality and test-first alignment so bypasses, weak assertions, false parity, and retrofit risk are blocked."
---

# Test Quality Audit

## Purpose

Detect bypasses, weak assertions, false environment parity, and retrofit risk across project-declared stacks. Judge evidence against the behavior and boundary claimed, without imposing an unrelated framework, runner, database, transport, browser, or device.

## Scope Controls

- This skill never bypasses TODO governance. If project artifacts change, follow TODO and `APROVADO` gates first.
- Treat tests as executable specifications. Prefer fail-first evidence for verifiable bugfixes, regressions, and behavior-defining changes.
- Classify audit complexity as `small|medium|big`; medium/big audits include Architecture, Code Quality, Tests, Performance, and Security framing.
- Resolve active capabilities, owning manifests, project-owned commands, and affected boundaries before applying stack-specific checks.
- Pair with `bug-fix-evidence-loop`, `test-creation-standard`, `verification-debt-audit`, or `frontend-race-condition-validation` when their scopes apply.

## Preferred Deterministic Helpers

- Run `bash delphi-ai/tools/test_quality_audit.sh`, optionally with `--scan-git-modified` or repeatable `--path <test-path>`.
- For Node/TypeScript capability ownership, run `python3 delphi-ai/tools/node_capability_surface_audit.py --repo <project-root> --expect <capability> [--manifest <relative/package.json>] [--require-script <script>]` before judging runner or script coverage.
- Exit code `2` from the static audit means medium/high signals were found. Review them; do not weaken the scope to clear the signal.

## Generic Guardrails

- `GF-01` Preflight, harness, and environment failures are blocked evidence, not product failures by default.
- `GF-02` Shared-lane validation uses canonical product surfaces; test-only product endpoints are forbidden.
- `GF-03` Parse and contract failures in reference assertions hard-fail.
- `GF-04` Required promotion gates cannot pass with flaky or retry-only outcomes.
- `GF-05` Artifact fallback paths that mask ownership or permission faults are forbidden.
- `GF-06` A narrow test or mocked boundary cannot substantiate a broader compatibility or end-to-end claim.

## Audit Workflow

1. **Frame the audit**
   - Record active capabilities, compatibility intent, changed behaviors, affected boundaries, topology, and relevant baseline decisions.
   - For large or architectural changes, require unit/provider/component plus integration/module/adapter evidence for each affected critical path.
2. **Check fail-first alignment**
   - Identify `test-first`, `test-after`, `not-applicable`, or `unknown` and the concrete assertion that demonstrates the pre-change failure.
   - Classify final-state-only tests that would not expose the bug as `retrofit-risk` unless a coherent non-applicability rationale exists.
3. **Scan for bypass flags**
   - Block committed skips, focused-test markers such as `test.only`/`describe.only`, CI golden-update bypasses, and shared-lane test-only routes.
4. **Match evidence to the claim**
   - Require real infrastructure only when compatibility or the contract crosses that boundary.
   - Verify both reachability and identity/authentication paths when those are part of the claim.
   - Do not accept unit-only evidence for a changed wiring, serialization, persistence, transport, or runtime boundary.
5. **Check fallback logic**
   - Block silent fallback from required real calls to mocks, from an owned fixture to ambient live data, or from canonical artifact paths to fallback directories.
6. **Verify dependency-injection parity**
   - Test replacements must preserve the relevant production token, scope/lifecycle, and failure semantics unless an explicit documented exception is itself asserted.
7. **Validate failure behavior**
   - Require loud failures for error payloads, empty required responses, parse errors, contract mismatches, and rejected dependencies.
   - Block no-exception-only and transport-status-only assertions when business semantics matter.
8. **Validate assertion quality**
   - Assert externally meaningful outcomes and explicit negative states.
   - Cover retriggerable asynchronous races when applicable.
   - Use deterministic owned proof subjects; do not rely on first-row, first-page, or first-candidate ambient data.
9. **Confirm environment and command parity**
   - Verify the exact project-owned runner/package-manager scripts and the topology prerequisites for the active capability.
   - Treat live hosted services, hardcoded production targets, or undeclared local substitutions as findings unless the approved baseline explicitly requires them.
10. **Audit build and runtime integrity when applicable**
    - Confirm authored tests are not stored in compiled output.
    - Match bundle/artifact metadata to the source revision and prove that manual/browser/device targets serve that build.
11. **Audit the claimed platform matrix**
    - Require evidence only for platforms in the claim, but mark any missing required platform `blocked`, never `passed`.
12. **Write issue cards for material findings**
    - Include issue ID, severity, `file:line` evidence, why-now, options A/B/C including do-nothing when reasonable, and recommendation.
13. **Record failure modes and uncertainty**
    - State likely edge cases, assumptions, unknowns, and confidence.
14. **Validate decision adherence**
    - Map each active baseline decision to `Adherent` or `Exception` with evidence. An unresolved exception is not delivery-ready.

## Conditional Stack Checks

- **NestJS:** test provider/use-case behavior, testing-module wiring, provider tokens/scopes/exports, and externally visible contracts at the chosen transport. Use the owning manifest's runner; do not assume Jest, Vitest, HTTP, Express, Fastify, Prisma, or PostgreSQL.
- **Laravel:** use the project-owned safe runner. Require a local MongoDB replica set and prohibit Atlas only when MongoDB is the declared test datastore.
- **Flutter:** require unit, widget, integration, web, or mobile lanes only where the change and platform claim demand them; use project-owned domain/scheme overrides.
- **Browser/Web:** keep test sources outside compiled bundles, use the project-owned browser runner, and require runtime freshness before accepting observations.

## Common Bypass Patterns (Block)

- Catching exceptions and continuing without failing.
- Tests that codify current buggy behavior instead of intended behavior.
- Mock or live-service fallbacks that hide required-boundary failures.
- Dependency-injection scope/token changes without explicit validation.
- Environment flags that disable required integration behavior in CI.
- Overly broad stubs that always succeed.
- Assertions that pass on empty data or ignore required state transitions.
- Ambient live-data selection for release-gating proof subjects.
- End-to-end or architectural safety claimed from unit-only evidence.
- Flaky required gates accepted as pass.
- Behavior-defining changes with no fail-first target and no rationale.

## Required Evidence

- Capability and owning-command inventory.
- Coverage/evidence matrix with deliberate exclusions.
- Proof of the real declared boundary where compatibility requires it.
- Fail-first target or explicit non-applicability rationale.
- Dependency-injection parity evidence or documented/asserted exception.
- Required platform status as `passed|blocked|failed|flaky`.
- Decision-adherence table when baseline decisions are in scope.

## Done Criteria

- No bypass remains in changed tests.
- No unresolved retrofit risk remains for behavior-defining work.
- Evidence layers substantiate, and do not overstate, the compatibility or architecture claim.
- Required real-boundary tests fail loudly on mismatch.
- Exact commands and topology match the declared project surface.
- Material findings have actionable issue cards.
- Required platform and decision evidence is complete or explicitly dispositioned.

```

## delphi-ai/skills/verification-debt-audit/SKILL.md
```
---
name: verification-debt-audit
description: "Audit verification debt across TODO evidence, tactical-note drift, waivers, and inline code TODO hygiene before closure."
---

# Verification Debt Audit

## Purpose
Detect closure-time debt that makes future maintenance slower or less trustworthy even when the immediate feature appears to work.

## Scope Controls
- This skill audits closure quality; it does not bypass TODO governance for code/doc changes.
- If the audit finds debt that requires project changes, follow the active TODO lane and approval rules before fixing it.
- Pair with `test-quality-audit` when the main debt signal is weak or retrofitted tests.
- Typical triggers:
  - `medium|big` TODOs
  - shared contract or cross-module changes
  - TODOs with waivers or provisional notes
  - code changes that introduce or leave inline `TODO|FIXME|HACK|TBD`

## Preferred Deterministic Helper
- Default audit path for TODO evidence + inline debt scanning:
  - `bash delphi-ai/tools/verification_debt_audit.sh --todo <todo-path>`
- Include changed/untracked files from the current branch in the inline debt scan:
  - `bash delphi-ai/tools/verification_debt_audit.sh --todo <todo-path> --scan-git-modified`
- Add explicit scan targets when the touched scope is narrower than the whole branch:
  - `bash delphi-ai/tools/verification_debt_audit.sh --todo <todo-path> --path <touched-path> [--path <touched-path> ...]`
- Exit code `2` means the audit completed and found `medium|high` debt signals. Treat that as evidence to review, not as automatic permission to rewrite scope.

## Debt Categories
- **Evidence debt**: claims in the TODO lack concrete proof.
- **Validation debt**: promised validation steps were skipped, weakened, or left ambiguous.
- **Waiver debt**: too many waivers, or waivers without a clear reason and expiration.
- **Promotion debt**: durable knowledge still trapped in tactical TODO notes instead of module docs.
- **Inline code TODO debt**: source contains `TODO|FIXME|HACK|TBD|XXX` without owner/next action/canonical link.
- **Closure drift**: TODO looks complete, but blockers/provisional status/evidence still indicate unresolved work.

## Audit Workflow
1. **Frame the audit**
   - Capture the active/completing TODO and its delivery stage.
   - Note whether the change touched shared contracts, cross-module surfaces, or critical user journeys.
2. **Check TODO evidence completeness**
   - Verify `Definition of Done`, `Validation Steps`, adherence tables, security risk assessment, and promotion evidence are complete enough to justify closure.
   - Flag any statement that claims success without artifact, command output, test evidence, or doc traceability.
3. **Check waiver quality**
   - Identify every waiver, `N/A`, explicit skip, or deferred verification item.
   - Flag waivers that lack:
     - why the waiver is safe now
     - what risk remains
     - when or how the waiver should be revisited
4. **Check promotion discipline**
   - Compare the TODO against touched module docs.
   - Flag durable conclusions still trapped in the TODO or comments instead of canonical docs.
5. **Scan code TODO hygiene**
   - Search touched files for inline debt markers:
     - `TODO`
     - `FIXME`
     - `HACK`
     - `TBD`
     - `XXX`
   - Classify each hit:
     - `acceptable`: local marker with clear next action and owner/context
     - `cleanup-required`: vague or stale marker that should be resolved now
     - `canonical-link-missing`: marker represents roadmap/contract knowledge but has no link to canonical docs/TODO
6. **Classify audit outcome**
   - `none`: no meaningful verification debt remains
   - `low`: minor debt, explicitly accepted with low maintenance risk
   - `medium`: debt is present and should be scheduled/tracked explicitly
   - `high`: closure should be blocked until debt is reduced
7. **Issue cards for material debt**
   - For each material finding record:
     - `Issue ID`
     - severity
     - evidence (`file:line`, TODO section, command/log)
     - why it matters
     - fix options `A/B/C`
     - recommended option

## Recommended Search Heuristics
- TODO/waiver scan:
  - `rg -n "waiver|not run|not needed|n/a|TODO|FIXME|HACK|TBD|blocked|provisional" foundation_documentation/todos/active foundation_documentation/todos/completed`
- Inline code debt:
  - `rg -n "\\b(TODO|FIXME|HACK|TBD|XXX)\\b" <touched-paths...>`

## Required Outputs
- Audit outcome: `none|low|medium|high`
- Short rationale for the outcome
- Inline code TODO debt classification: `none|accepted|cleanup-required`
- Evidence or artifact path for the audit
- Accepted residual debt, if any

## Done Criteria
- Closure is not declared clean while material evidence/promotion/waiver debt remains hidden.
- Inline code TODO debt is either cleaned up or explicitly classified and justified.
- Durable knowledge is promoted into canonical docs instead of staying trapped in tactical artifacts.
- Any remaining verification debt is explicit enough to survive future sessions without rediscovery.

```

## delphi-ai/schemas/subagent_review_result.schema.json
```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://paced.internal/schemas/subagent_review_result.schema.json",
  "title": "PACED Subagent Review Result",
  "type": "object",
  "required": [
    "schema_version",
    "artifact_kind",
    "dispatch_path",
    "review_kind",
    "reviewer_label",
    "overall_assessment",
    "recommended_path",
    "performance_position",
    "elegance_position",
    "structural_soundness_position",
    "operational_fit_position",
    "findings"
  ],
  "properties": {
    "schema_version": {
      "const": "subagent-review-result-v1"
    },
    "artifact_kind": {
      "const": "subagent_review_result"
    },
    "dispatch_path": {
      "type": "string",
      "minLength": 1
    },
    "review_kind": {
      "enum": [
        "architecture_opinion",
        "architecture_adherence",
        "critique",
        "test_quality_audit",
        "final_review",
        "cutover_integrity_audit"
      ]
    },
    "reviewer_label": {
      "type": "string",
      "minLength": 1
    },
    "overall_assessment": {
      "type": "string",
      "minLength": 1
    },
    "recommended_path": {
      "type": "string",
      "minLength": 1
    },
    "performance_position": {
      "$ref": "#/$defs/position"
    },
    "elegance_position": {
      "$ref": "#/$defs/position"
    },
    "structural_soundness_position": {
      "$ref": "#/$defs/position"
    },
    "operational_fit_position": {
      "$ref": "#/$defs/position"
    },
    "findings": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/finding"
      }
    }
  },
  "additionalProperties": false,
  "$defs": {
    "position": {
      "enum": [
        "strong_positive",
        "acceptable",
        "mixed",
        "regresses",
        "unknown",
        "not_evaluated"
      ]
    },
    "finding": {
      "type": "object",
      "required": [
        "severity",
        "title",
        "rationale",
        "suggested_action"
      ],
      "properties": {
        "finding_id": {
          "type": "string",
          "minLength": 1
        },
        "severity": {
          "enum": [
            "low",
            "medium",
            "high"
          ]
        },
        "title": {
          "type": "string",
          "minLength": 1
        },
        "rationale": {
          "type": "string",
          "minLength": 1
        },
        "category": {
          "enum": [
            "architecture",
            "adherence",
            "tests",
            "performance",
            "security",
            "elegance",
            "structural_soundness",
            "operational_fit",
            "residual_risk",
            "other"
          ]
        },
        "formalizable_hint": {
          "enum": [
            "yes",
            "partial",
            "no",
            "unknown"
          ]
        },
        "candidate_rule_level": {
          "enum": [
            "paced",
            "project",
            "none",
            "unknown"
          ]
        },
        "candidate_rule_id": {
          "type": "string"
        },
        "affected_paths": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "suggested_action": {
          "type": "string",
          "minLength": 1
        }
      },
      "additionalProperties": false
    }
  }
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/api-ci-light-revision2-20261015.log
```
v22.23.3
COMMAND npm run prisma:generate

> @leadshug/api@0.1.0 prisma:generate
> prisma generate

Environment variables loaded from .env
Prisma schema loaded from prisma/schema.prisma

✔ Generated Prisma Client (v6.19.3) to ./node_modules/@prisma/client in 227ms

Start by importing your Prisma Client (See: https://pris.ly/d/importing-client)

Tip: Need your database queries to be 1000x faster? Accelerate offers you that and more: https://pris.ly/tip-2-accelerate

npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice
COMMAND npm run lint

> @leadshug/api@0.1.0 lint
> eslint "{src,test}/**/*.ts"

COMMAND npm run build

> @leadshug/api@0.1.0 build
> nest build

COMMAND npm test

> @leadshug/api@0.1.0 test
> vitest run --config vitest.config.ts

[33mThe CJS build of Vite's Node API is deprecated. See https://vite.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.[39m

 RUN  v2.1.9 /workspace/api-app

 ✓ src/main.spec.ts (6 tests) 7ms
 ✓ src/domain/access/role.spec.ts (9 tests) 7ms
 ✓ src/infra/config/modulos.spec.ts (10 tests) 9ms
 ✓ src/domain/access/scope.spec.ts (22 tests) 19ms
 ✓ src/domain/inbox/timeline-pagination.spec.ts (11 tests) 13ms
 ✓ src/domain/integration/rate-limit.service.spec.ts (3 tests) 7ms
[33m[Nest] 196  - [39m10/15/2026, 4:09:50 AM [33m   WARN[39m [38;5;3m[Email] [39m[33mRESEND_API_KEY ausente — "x" não foi enviado para a@b.test.[39m
[31m[Nest] 196  - [39m10/15/2026, 4:09:50 AM [31m  ERROR[39m [38;5;3m[Email] [39m[31mResend recusou (403): {"message":"domain is not verified"}[39m
[31m[Nest] 196  - [39m10/15/2026, 4:09:50 AM [31m  ERROR[39m [38;5;3m[Email] [39m[31mFalha de rede ao enviar para a@b.test: Error: getaddrinfo ENOTFOUND[39m
 ✓ src/integrations/meta/meta.client.spec.ts (4 tests) 11ms
 ✓ src/integrations/email/email.client.spec.ts (6 tests) 14ms
 ✓ src/infra/session/session.service.spec.ts (17 tests) 10ms
 ✓ src/integrations/typebot/typebot.client.spec.ts (5 tests) 11ms
 ✓ src/domain/inbox/historico.service.spec.ts (6 tests) 4ms
 ✓ src/domain/integration/api-key.service.spec.ts (2 tests) 5ms
 ✓ src/domain/inbox/incoming.typebot.integration.spec.ts (2 tests) 8ms
 ✓ src/surfaces/bff/integracao.typebot.spec.ts (2 tests) 5ms
 ✓ src/domain/inbox/incoming.typebot.spec.ts (2 tests) 3ms
 ✓ src/domain/channels/channels.service.spec.ts (3 tests) 4ms
 ✓ src/domain/identity/password.service.spec.ts (5 tests) 432ms

 Test Files  17 passed (17)
      Tests  115 passed (115)
   Start at  04:09:48
   Duration  2.81s (transform 12.72s, setup 0ms, collect 24.53s, tests 568ms, environment 5ms, prepare 2.96s)


EXIT_CODE=0 RUN_ID=api-ci-light-revision2-20261015

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/api-e2e-authority.log
```

> @leadshug/api@0.1.0 test:e2e
> vitest run --config vitest.config.e2e.ts --no-file-parallelism --maxWorkers=1

[33mThe CJS build of Vite's Node API is deprecated. See https://vite.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.[39m

 RUN  v2.1.9 /workspace/api-app

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":1,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":53,"dezIncrementosMs":26,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":2,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":48,"dezIncrementosMs":21,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":3,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":51,"dezIncrementosMs":24,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

 ✓ test/atendimento.e2e-spec.ts (19 tests) 7720ms
   ✓ atendimento > POST conversations/:id/messages — o trio (ADR-0012 §2) > autorizado: responde, envia pelo canal e assume a conversa 424ms
   ✓ atendimento > POST conversations/:id/messages — o trio (ADR-0012 §2) > ATENDENTE no escopo responde — estar na BU BASTA (ADR-0018 §3) 493ms
   ✓ atendimento > POST conversations/:id/messages — o trio (ADR-0012 §2) > CROSS-TENANT: o dono de Beta recebe 404 na conversa da BU de Alfa 380ms
   ✓ atendimento > janela de 24h — atributo do CANAL (ADR-0009 §3) > no canal NÃO oficial não existe janela: responde mesmo com a conversa velha 308ms
   ✓ atendimento > fila > assumir trava para outro agente (409), e finalizar libera 516ms
   ✓ atendimento > fila > responder NÃO rouba conversa de quem já está atendendo 463ms
   ✓ atendimento > fila > abrir a thread zera as não lidas — abrir É atender 307ms
   ✓ atendimento > fila > a lista filtra por aba e só enxerga a BU pedida 323ms
   ✓ atendimento > a inbox pagina — teto silencioso é o que vira "sumiram conversas" > devolve total e temMais, e a segunda página traz o resto 328ms
   ✓ atendimento > timeline paginada do atendimento > caminha por 251 mensagens na ordem do banco e mantém a página limitada 480ms
   ✓ atendimento > timeline paginada do atendimento > valida parâmetros depois da autorização e rejeita cursor de outra conversa autorizada 381ms
   ✓ atendimento > timeline paginada do atendimento > exige sessão antes de validar query e não altera unread 310ms
   ✓ atendimento > timeline paginada do atendimento > rejeita cursor/limite repetidos e mantém refresh e backfill sem efeito de leitura 364ms
   ✓ atendimento > timeline paginada do atendimento > serializa dez chegadas concorrentes com a fronteira de abertura em três lotes 546ms
   ✓ atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes 509ms
   ✓ atendimento > timeline paginada do atendimento > permite leituras de cursor concorrentes com close sem reescrever status 485ms
 ✓ test/setores.e2e-spec.ts (26 tests) 10430ms
   ✓ setores (ADR-0017) > o Geral nasce com a Mantenedora > a primeira BU já vem num setor — nenhum número fica sem 356ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > autorizado: OWNER cria, renomeia e inativa 345ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > papel insuficiente: ATENDENTE recebe 403 ao criar 462ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > cross-tenant: setor da Mantenedora B responde 404 para o OWNER de A 368ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > o nome é único DENTRO da Mantenedora — duas contas podem ter "Comercial" 407ms
   ✓ setores (ADR-0017) > CRUD — o trio (ADR-0012 §2) > setor COM número não é excluído — só inativado 305ms
   ✓ setores (ADR-0017) > concessão por setor é EXPANSÃO (ADR-0017 §2) > materializa uma linha POR NÚMERO do setor, com proveniência SETOR 433ms
   ✓ setores (ADR-0017) > concessão por setor é EXPANSÃO (ADR-0017 §2) > BU criada DEPOIS, no setor concedido, já nasce com o grant (regra 3) 411ms
   ✓ setores (ADR-0017) > concessão por setor é EXPANSÃO (ADR-0017 §2) > revogar o setor NÃO remove grant direto nem o da Mantenedora 400ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > autorizado: lista quem recebeu o setor, com papel e desde quando 375ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > papel insuficiente: ATENDENTE recebe 403 436ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > cross-tenant: setor da Mantenedora B responde 404 362ms
   ✓ setores (ADR-0017) > ver quem tem o setor — a leitura que faltava > a lista de pessoas diz DE QUAL ORIGEM veio cada acesso 401ms
   ✓ setores (ADR-0017) > renomear e inativar o número > papel insuficiente: ATENDENTE recebe 403 478ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > quem tinha pelo setor antigo perde; quem tem o novo ganha 513ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > o grant DIRETO sobrevive à mudança de setor 574ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > recusa quando mover deixaria o número sem OWNER 495ms
   ✓ setores (ADR-0017) > mover número entre setores — a escrita mais delicada do modelo > cross-setor: o atendente do Comercial recebe 404 na conversa do Suporte 566ms
   ✓ setores (ADR-0017) > conceder um setor VAZIO é lembrado — o número criado depois já nasce com o acesso 381ms
   ✓ setores (ADR-0017) > revogar apaga a CONCESSÃO — o próximo número não ressuscita o acesso 393ms
   ✓ setores (ADR-0017) > setor INATIVO não interrompe atendimento — só some do cadastro 329ms
[31m[Nest] 965  - [39m10/15/2026, 3:20:45 AM [31m  ERROR[39m [38;5;3m[Recuperacao] [39m[31mToken de recuperação emitido para dono@alfa.test, mas o e-mail NÃO saiu.[39m
[31m[Nest] 965  - [39m10/15/2026, 3:20:47 AM [31m  ERROR[39m [38;5;3m[Recuperacao] [39m[31mToken de recuperação emitido para dono@alfa.test, mas o e-mail NÃO saiu.[39m
 ✓ test/convites.e2e-spec.ts (18 tests) 4799ms
   ✓ convite e recuperação de senha (ADR-0025) > convite substitui a senha provisória > criar pessoa NÃO aceita mais senha, e envia o convite 341ms
   ✓ convite e recuperação de senha (ADR-0025) > convite substitui a senha provisória > usar o link define a senha e já entra logado 377ms
   ✓ convite e recuperação de senha (ADR-0025) > o token é de uso único > o mesmo link não funciona duas vezes 380ms
   ✓ convite e recuperação de senha (ADR-0025) > o token é de uso único > pedir recuperação DUAS vezes deixa só o último link vivo 370ms
   ✓ convite e recuperação de senha (ADR-0025) > o token é de uso único > definir a senha mata TODOS os pendentes — inclusive o convite antigo 369ms
 ✓ test/webhooks.e2e-spec.ts (15 tests) 3457ms
   ✓ webhooks de entrada > o dado recebido respeita o escopo > CROSS-TENANT: o dono de Beta não enxerga a conversa que entrou na BU de Alfa 303ms
 ✓ test/identidade.e2e-spec.ts (17 tests) 3660ms
   ✓ identidade > login > bloqueia o e-mail na quinta tentativa errada 513ms
   ✓ identidade > troca obrigatória de senha > trava tudo menos /me e a troca, e destrava depois de trocar 461ms
 ✓ test/api-publica.e2e-spec.ts (13 tests) 5082ms
   ✓ API pública v1 > autenticação pela chave > a chave sai em claro UMA vez, e o prefixo é lh_ 374ms
   ✓ API pública v1 > autenticação pela chave > sem chave: 401 NAO_AUTENTICADO 310ms
   ✓ API pública v1 > autenticação pela chave > cookie de sessão NÃO substitui a chave 374ms
   ✓ API pública v1 > autenticação pela chave > chave revogada responde igual a inexistente 384ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > escopo nulo devolve só as BUs DESTA Mantenedora 310ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > CROSS-TENANT: pedir a BU de Beta com a chave de Alfa dá 403 SEM_ACESSO_A_CONTA 364ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > escopo restrito não alcança outra BU da MESMA Mantenedora 421ms
   ✓ API pública v1 > escopo — a Mantenedora sai da CHAVE, nunca do request > criar chave com escopo apontando para BU de outra Mantenedora é recusado 414ms
   ✓ API pública v1 > contrato > conversations traz janela_aberta e datas em ISO-8601 UTC 349ms
   ✓ API pública v1 > contrato > messages aceita since para sincronização incremental 342ms
   ✓ API pública v1 > contrato > POST messages envia e marca a conversa como atendida por EXTERNO 326ms
   ✓ API pública v1 > contrato > fora da janela, POST messages recusa com JANELA_FECHADA 306ms
   ✓ API pública v1 > limite de taxa (ADR-0010 §7) — fecha o buraco de ritmo do S3 > estoura em 429 LIMITE_DE_TAXA com Retry-After 636ms
 ✓ test/usuarios.e2e-spec.ts (13 tests) 4676ms
   ✓ gestão de usuários > criar — o trio (ADR-0012 §2) > autorizado: cria com papel e escopo, e SEM credencial — quem entra define a senha 359ms
   ✓ gestão de usuários > criar — o trio (ADR-0012 §2) > papel insuficiente: MEMBRO não gerencia pessoas 512ms
   ✓ gestão de usuários > invariantes do modelo > ninguém concede papel maior que o próprio (ADR-0008 §4) 464ms
   ✓ gestão de usuários > invariantes do modelo > ADMIN não mexe em quem é OWNER — papel ≥ o do alvo (ADR-0008 §4) 481ms
   ✓ gestão de usuários > reenvio de acesso > reenviar o acesso derruba a sessão e emite um LINK, não uma senha 396ms
   ✓ gestão de usuários > a lista pagina e filtra > busca por nome ou e-mail 309ms
 ✓ test/historico.e2e-spec.ts (11 tests) 4003ms
   ✓ histórico (Consultar) > o par número → número > a resposta traz os DOIS números do par, não só o contato 423ms
   ✓ histórico (Consultar) > o par número → número > filtra pelo número do contato 336ms
   ✓ histórico (Consultar) > paginação — 20 é o corpo da página, não o tamanho do que existe > devolve as ÚLTIMAS 20 e avisa que há mais 371ms
   ✓ histórico (Consultar) > paginação — 20 é o corpo da página, não o tamanho do que existe > a segunda página traz o resto e fecha 332ms
   ✓ histórico (Consultar) > consultar não é atender > ler o histórico NÃO zera as não lidas 301ms
   ✓ histórico (Consultar) > CSV > usa os mesmos filtros e sai uma linha por mensagem 300ms
   ✓ histórico (Consultar) > permissão — o trio (ADR-0012 §2) > autorizado: ATENDENTE no escopo consulta — o grant é a permissão (ADR-0018) 441ms
   ✓ histórico (Consultar) > permissão — o trio (ADR-0012 §2) > CROSS-TENANT: o dono de Beta recebe 404 no histórico da BU de Alfa 363ms
   ✓ histórico (Consultar) > permissão — o trio (ADR-0012 §2) > CROSS-TENANT: o CSV também é barrado, e não vaza no corpo 352ms
 ✓ test/historico-atividades.e2e-spec.ts (13 tests) 4533ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o CHECK torna o vazamento IRREPRESENTÁVEL (ADR-0020 §1.1) > escopo BU sem bu_id falha NO BANCO, não no serviço 394ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o CHECK torna o vazamento IRREPRESENTÁVEL (ADR-0020 §1.1) > escopo CONTA COM bu_id falha pelo mesmo CHECK 303ms
   ✓ histórico de atividades (ADR-0020 e 0022) > a escrita acontece dentro da transação > criar setor grava EXATAMENTE uma linha, com a frase pronta 314ms
   ✓ histórico de atividades (ADR-0020 e 0022) > a escrita acontece dentro da transação > falhar a transação NÃO deixa linha 319ms
   ✓ histórico de atividades (ADR-0020 e 0022) > a escrita acontece dentro da transação > mover número grava MOVER com de/para preenchidos 325ms
   ✓ histórico de atividades (ADR-0020 e 0022) > leitura — o trio (ADR-0012 §2) > papel insuficiente: ATENDENTE recebe 403 — gravar é do produto, ler é de quem administra 452ms
   ✓ histórico de atividades (ADR-0020 e 0022) > leitura — o trio (ADR-0012 §2) > cross-tenant: o ADMIN de A não vê NENHUMA linha de B 364ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o que NÃO entra > trocar a própria senha não gera linha 420ms
   ✓ histórico de atividades (ADR-0020 e 0022) > o que NÃO entra > listar e filtrar não geram linha — leitura não registra 304ms
 ✓ test/onboarding.e2e-spec.ts (13 tests) 4652ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > antes de concluir, o resto do BFF responde 409 ONBOARDING_PENDENTE 427ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > o /me, a troca de senha e o próprio wizard continuam respondendo 352ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > a troca de senha vem ANTES do wizard — nunca preso entre os dois portões 640ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o portão: senha → wizard → produto > ninguém pode ser convidado antes do wizard — o caso deixa de existir 301ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > o wizard oferece SÓ o que a instalação tem > o canal oficial NÃO aparece — ele é o piso, não uma escolha 306ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > só o OWNER conclui, e o produto passa a responder 320ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > recusa papel de convite OWNER — seria transferência disfarçada de cadastro 302ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > recusa módulo fora do teto — pedido inválido é ERRO, não preferência ignorada 329ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > recusa módulo que não existe nesta instalação 335ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > concluir > grava a conclusão no histórico 335ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > adicionar e remover módulo depois — mesmo serviço, outra porta > ADMIN edita, e a mudança aparece no /me 346ms
   ✓ wizard de onboarding e módulos da conta (ADR-0016) > adicionar e remover módulo depois — mesmo serviço, outra porta > RECUSA desligar canal que ainda tem número conectado 358ms
 ✓ test/canais.e2e-spec.ts (10 tests) 3738ms
   ✓ canais da BU > POST channels — o trio (ADR-0012 §2) > autorizado: OWNER conecta o canal oficial, e o phone_number_id é capturado na mesma ida 372ms
   ✓ canais da BU > POST channels — o trio (ADR-0012 §2) > papel insuficiente: MEMBRO recebe 403 — a BU é dele, o poder é que não alcança 472ms
   ✓ canais da BU > canal não oficial > cria a instância e devolve o QR, com a janela DESLIGADA 301ms
   ✓ canais da BU > regras do vínculo > a BU aceita um canal de cada tipo, e recusa o segundo do mesmo tipo 311ms
   ✓ canais da BU > regras do vínculo > remover exige ADMIN e libera o tipo para ser conectado de novo 491ms
   ✓ canais da BU > regras do vínculo > listar canais é leitura: VIEWER enxerga 494ms
 ✓ test/cross-tenant.e2e-spec.ts (9 tests) 3039ms
   ✓ escopo entre Mantenedoras > GET /api/bff/business-units/:buId > autorizado: o dono enxerga a BU da própria Mantenedora 342ms
   ✓ escopo entre Mantenedoras > GET /api/bff/business-units > CROSS-TENANT: usuário sem grant nenhum recebe lista VAZIA, nunca "todas" 366ms
   ✓ escopo entre Mantenedoras > o grant do fundador nasce como expansão (ADR-0008 §4, importado já corrigido) > quem tem grant DIRETO não é alcançado pela expansão — e cai para VIEWER na Mantenedora 469ms
 ✓ test/realtime.e2e-spec.ts (7 tests) 5664ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > quem tem grant na BU recebe a mensagem que chegou 317ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > CROSS-TENANT: o dono de Beta NÃO recebe evento da BU de Alfa 1863ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > usuário da MESMA Mantenedora sem grant naquela BU também não recebe 1983ms
   ✓ push em tempo real — com escopo (fecha o risco S8) > o socket some da lista quando o cliente desconecta 589ms
 ✓ test/modulos.e2e-spec.ts (8 tests) 2892ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > o /me devolve o produto já interseccionado > teto ligado + contratado = ligado, e a marca vem junto 452ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > o /me devolve o produto já interseccionado > a Mantenedora NÃO amplia o teto: contratado sem teto continua desligado 345ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > o /me devolve o produto já interseccionado > sem nada contratado, o produto nasce sem módulo e com tema padrão 315ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a migração PRESERVA o módulo de quem já usa o canal — repetível, e é o que sobe em stage 353ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > autorizado: com teto e contrato, conecta o canal não oficial 357ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > módulo fora do teto da instalação: 404 MODULO_DESLIGADO, nunca 403 383ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > teto ligado mas a Mantenedora não contratou: 404 igual 355ms
   ✓ módulos: env é o teto, a Mantenedora escolhe dentro dele (ADR-0016) > a rota recusa o que o front não deveria nem ter oferecido > o canal OFICIAL nunca é barrado por módulo — ele é o PISO do produto 329ms
 ✓ test/arquivos.e2e-spec.ts (8 tests) 2772ms
   ✓ arquivos (ADR-0024) > SEM volume, recusa explicitamente — e o resto do produto funciona 426ms
   ✓ arquivos (ADR-0024) > com volume > guarda com nome de uuid — o nome do cliente NÃO chega ao disco 309ms
   ✓ arquivos (ADR-0024) > com volume > recusa .png que não é PNG por dentro — o tipo vem dos BYTES 333ms
   ✓ arquivos (ADR-0024) > com volume > devolve o arquivo para quem é da mesma Mantenedora 310ms
   ✓ arquivos (ADR-0024) > com volume > cross-tenant: arquivo de A responde 404 para B 507ms
   ✓ arquivos (ADR-0024) > com volume > id que não é uuid não vira caminho 346ms
[31m[Nest] 1517  - [39m10/15/2026, 3:21:59 AM [31m  ERROR[39m [38;5;3m[Rotina] [39m[31m{"nome":"rotina-quebrada","linhas":0,"lotes":0,"pulouPorLock":false,"erro":"estourei de propósito","duracaoMs":2}[39m
 ✓ test/rotinas.e2e-spec.ts (5 tests) 762ms
 ✓ test/surfaces.e2e-spec.ts (9 tests) 198ms
 ✓ test/cobertura-do-catalogo.e2e-spec.ts (4 tests) 294ms
 ✓ test/painel.e2e-spec.ts (4 tests) 1680ms
   ✓ painel > conta o atendimento e avisa do número sem canal 384ms
   ✓ painel > cross-tenant: NENHUM número da Mantenedora B entra na conta de A 311ms
   ✓ painel > o ATENDENTE vê os números, e NÃO vê o extrato de atividades 500ms
   ✓ painel > o ADMIN vê o extrato 318ms
[31m[Nest] 1688  - [39m10/15/2026, 3:22:08 AM [31m  ERROR[39m [38;5;3m[Banco] [39m[31mBANCO ATRÁS DA IMAGEM: "public.tokens_de_acesso" não existe (P2021). Rode `npx prisma migrate deploy` de dentro do serviço.[39m
 ✓ test/banco-atrasado.e2e-spec.ts (2 tests) 500ms
   ✓ banco atrás da imagem > tabela ausente vira 503 DIZENDO a causa, não 500 opaco 312ms

 Test Files  20 passed (20)
      Tests  224 passed (224)
   Start at  03:20:12
   Duration  111.92s (transform 6.83s, setup 184ms, collect 33.04s, tests 74.55s, environment 4ms, prepare 1.29s)


```

## Attestation bounded view foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-web-authority-revision3-final-frc3-20261015.json
```json
{
  "capturedAtUtc": "2026-10-15T04:24:16.848Z",
  "runId": "web-authority-revision3-final-frc3-20261015",
  "branch": {
    "api": {
      "name": "feature/inbox-timeline-pagination",
      "head": "5db3fbe2043428749895fc3ff6441e9457467dd0",
      "diffSha256": "d3d84c015c24348b1dbc885a90d66ff8f88eadf35a75b0a256a38c3f1230708b",
      "sourceManifest": [
        {
          "path": "src/domain/inbox/conversations.service.ts",
          "sha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.spec.ts",
          "sha256": "a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.ts",
          "sha256": "d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af"
        },
        {
          "path": "src/surfaces/bff/conversations.controller.ts",
          "sha256": "0b5c46a78aafd8085b609ad711bcdb7626263094f434240f37b8700f20291565"
        },
        {
          "path": "test/atendimento.e2e-spec.ts",
          "sha256": "1bb4acb19fc522b397424b319ab04563e3608605dcfe307970eecdd0d464b5b8"
        },
        {
          "path": "test/browser-server.cjs",
          "sha256": "031e9d1e282603c098c4bb594fb13a08ab2bc2f301c9a3ebb5a6362cae6fe42b"
        },
        {
          "path": "test/timeline-fixtures.cjs",
          "sha256": "bc15f1758ec574dec1f1c66330e0cc9804705e103fb5abab7f9015e5e8563f9f"
        }
      ]
    },
    "web": {
      "name": "feature/inbox-timeline-pagination",
      "head": "6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9",
      "diffSha256": "1101205003f78d9514a79ff38e846107bd224a50f73345d5fb166b8ec166b2c4",
      "sourceManifest": [
        {
          "path": "e2e/timeline-freshness.ts",
          "sha256": "ad41153df34c53f6674325b72887e701259ba7a8e752afd38ff4cdd8728c4cd0"
        },
        {
          "path": "e2e/timeline.spec.ts",
          "sha256": "867c4de5d3a244923a185b935bd1bb149f342275949e285eb745f789c571cb82"
        },
        {
          "path": "playwright.config.ts",
          "sha256": "d69c084d15cfef29ad23851036cb90309c60aa7a7b16c6810e3ae9b0adbbdd98"
        },
        {
          "path": "src/api.ts",
          "sha256": "87ba36bd21518725ba0e42221030d77b723144ef8d0581fddb2d9102233e7db2"
        },
        {
          "path": "src/telas/Inbox.tsx",
          "sha256": "821ce011ce5738e40caeafa2c3fad20b9583053ce2373bb194abbeee567bc783"
        },
        {
          "path": "src/tempoReal.spec.ts",
          "sha256": "378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5"
        },
        {
          "path": "src/tempoReal.ts",
          "sha256": "118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf"
        },
        {
          "path": "src/timeline.test.ts",
          "sha256": "16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4"
        },
        {
          "path": "src/timeline.ts",
          "sha256": "0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311"
        }
      ]
    }
  },
  "runtime": "v22.23.3",
  "database": {
    "name": "leadshug_timeline_20261014",
    "endpoint": "postgresql://timeline-postgres:5432/leadshug_timeline_20261014",
    "completedMigrations": 17
  },
  "endpoints": {
    "apiHealth": 200,
    "fixtureHealth": 200,
    "preview": 200,
    "servedBundle": "/assets/index-DKhXhPnI.js"
  },
  "servedBundleSha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e",
  "distBundleSha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e",
  "webDistManifest": [
    {
      "path": "assets/index-DKhXhPnI.js",
      "sha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e"
    },
    {
      "path": "assets/index-wuzy3kMN.css",
      "sha256": "38f979314555cda8b834189ed5c64826bbc309e294091c9f5c54ee5f8bd2aadd"
    },
    {
      "path": "config.js",
      "sha256": "1ad17fefa4173ed847cabd79e7fdc1b262fa19ea4ff33c3ef435e141275fb532"
    },
    {
      "path": "index.html",
      "sha256": "58854bed34a90d8f66296df9c3a6bad05b80a9b534f923774c8e0e439d805711"
    }
  ],
  "apiBuildManifestSummary": {
    "entries": 149,
    "canonicalListSha256": "d5a8885d8f3a2d30357b37986578498d5ded41c685de337da7c1954962c73955"
  },
  "rawAttestationFileSha256": "20e72c9376a276b6083d14688c4820b2f2169955ff28da152cd3cf82d4cd6716"
}
```

## Attestation bounded view foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-web-authority-revision3-final-full-20261015.json
```json
{
  "capturedAtUtc": "2026-10-15T04:22:58.946Z",
  "runId": "web-authority-revision3-final-full-20261015",
  "branch": {
    "api": {
      "name": "feature/inbox-timeline-pagination",
      "head": "5db3fbe2043428749895fc3ff6441e9457467dd0",
      "diffSha256": "d3d84c015c24348b1dbc885a90d66ff8f88eadf35a75b0a256a38c3f1230708b",
      "sourceManifest": [
        {
          "path": "src/domain/inbox/conversations.service.ts",
          "sha256": "93e69b0a1811533d0d718fe3fd3b105b1376d2a481ab2b22d8f1bfcf5dbe452e"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.spec.ts",
          "sha256": "a4c128981c7d3a0e93ba51de17392a34320e89f78098e5ed383532011ff6bb4d"
        },
        {
          "path": "src/domain/inbox/timeline-pagination.ts",
          "sha256": "d2cb9e533c8741f34babb1cef0a771878ae488474a3162e844a2f1d4d3acd6af"
        },
        {
          "path": "src/surfaces/bff/conversations.controller.ts",
          "sha256": "0b5c46a78aafd8085b609ad711bcdb7626263094f434240f37b8700f20291565"
        },
        {
          "path": "test/atendimento.e2e-spec.ts",
          "sha256": "1bb4acb19fc522b397424b319ab04563e3608605dcfe307970eecdd0d464b5b8"
        },
        {
          "path": "test/browser-server.cjs",
          "sha256": "031e9d1e282603c098c4bb594fb13a08ab2bc2f301c9a3ebb5a6362cae6fe42b"
        },
        {
          "path": "test/timeline-fixtures.cjs",
          "sha256": "bc15f1758ec574dec1f1c66330e0cc9804705e103fb5abab7f9015e5e8563f9f"
        }
      ]
    },
    "web": {
      "name": "feature/inbox-timeline-pagination",
      "head": "6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9",
      "diffSha256": "1101205003f78d9514a79ff38e846107bd224a50f73345d5fb166b8ec166b2c4",
      "sourceManifest": [
        {
          "path": "e2e/timeline-freshness.ts",
          "sha256": "ad41153df34c53f6674325b72887e701259ba7a8e752afd38ff4cdd8728c4cd0"
        },
        {
          "path": "e2e/timeline.spec.ts",
          "sha256": "867c4de5d3a244923a185b935bd1bb149f342275949e285eb745f789c571cb82"
        },
        {
          "path": "playwright.config.ts",
          "sha256": "d69c084d15cfef29ad23851036cb90309c60aa7a7b16c6810e3ae9b0adbbdd98"
        },
        {
          "path": "src/api.ts",
          "sha256": "87ba36bd21518725ba0e42221030d77b723144ef8d0581fddb2d9102233e7db2"
        },
        {
          "path": "src/telas/Inbox.tsx",
          "sha256": "821ce011ce5738e40caeafa2c3fad20b9583053ce2373bb194abbeee567bc783"
        },
        {
          "path": "src/tempoReal.spec.ts",
          "sha256": "378a97ce29c6382f6a7ae9018121ed99ef2733a2b1c8f01c3889074611fa7dd5"
        },
        {
          "path": "src/tempoReal.ts",
          "sha256": "118ceedc40649eb8b7ddfa44eee7824224994bf383dc9b51e496f80236da0fcf"
        },
        {
          "path": "src/timeline.test.ts",
          "sha256": "16d1f1a12d20935e399e4b23e4d93de7047f9015dfd5a65ee6093d0645c38fd4"
        },
        {
          "path": "src/timeline.ts",
          "sha256": "0bfd7d287f93c8c6393718f3f05cd9c248ce50311758bf9995e6ba80b5cd9311"
        }
      ]
    }
  },
  "runtime": "v22.23.3",
  "database": {
    "name": "leadshug_timeline_20261014",
    "endpoint": "postgresql://timeline-postgres:5432/leadshug_timeline_20261014",
    "completedMigrations": 17
  },
  "endpoints": {
    "apiHealth": 200,
    "fixtureHealth": 200,
    "preview": 200,
    "servedBundle": "/assets/index-DKhXhPnI.js"
  },
  "servedBundleSha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e",
  "distBundleSha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e",
  "webDistManifest": [
    {
      "path": "assets/index-DKhXhPnI.js",
      "sha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e"
    },
    {
      "path": "assets/index-wuzy3kMN.css",
      "sha256": "38f979314555cda8b834189ed5c64826bbc309e294091c9f5c54ee5f8bd2aadd"
    },
    {
      "path": "config.js",
      "sha256": "1ad17fefa4173ed847cabd79e7fdc1b262fa19ea4ff33c3ef435e141275fb532"
    },
    {
      "path": "index.html",
      "sha256": "58854bed34a90d8f66296df9c3a6bad05b80a9b534f923774c8e0e439d805711"
    }
  ],
  "apiBuildManifestSummary": {
    "entries": 149,
    "canonicalListSha256": "d5a8885d8f3a2d30357b37986578498d5ded41c685de337da7c1954962c73955"
  },
  "rawAttestationFileSha256": "94ceadbb83ef431eea7411cd28650d34626f196b5f344240c39ef294da20cc28"
}
```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-canonical-after-mutation.log
```
[33mThe CJS build of Vite's Node API is deprecated. See https://vite.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.[39m

 RUN  v2.1.9 /workspace/api-app

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":1,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":83,"dezIncrementosMs":42,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":2,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":55,"dezIncrementosMs":24,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

stdout | test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
{"prova":"BCI_ACK_COM_SELECT_BLOQUEADO","lote":3,"bloqueioDetectado":true,"sondagens":2,"ackAteSelectBloqueadoMs":53,"dezIncrementosMs":26,"unreadEnquantoSelectBloqueado":10,"unreadDepoisDaResposta":10}

 ✓ test/atendimento.e2e-spec.ts (19 tests | 18 skipped) 826ms
   ✓ atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes 637ms

 Test Files  1 passed (1)
      Tests  1 passed | 18 skipped (19)
   Start at  03:23:25
   Duration  8.66s (transform 6.07s, setup 45ms, collect 7.55s, tests 826ms, environment 0ms, prepare 75ms)

npm notice
npm notice New major version of npm available! 10.9.9 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-mutation-control.log
```

 RUN  v2.1.9 /workspace/api-app

 ❯ test/atendimento.e2e-spec.ts (19 tests | 1 failed | 18 skipped) 701ms
   × atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes 502ms
     → expected +0 to be 10 // Object.is equality

 Test Files  1 failed (1)
      Tests  1 failed | 18 skipped (19)
   Start at  03:22:45
   Duration  8.45s (transform 5.90s, setup 45ms, collect 7.43s, tests 701ms, environment 0ms, prepare 87ms)

[33mThe CJS build of Vite's Node API is deprecated. See https://vite.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.[39m
⎯⎯⎯⎯⎯⎯⎯ Failed Tests 1 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  test/atendimento.e2e-spec.ts > atendimento > timeline paginada do atendimento > preserva dez incrementos feitos após o ack e enquanto a página fica bloqueada, em três lotes
AssertionError: expected +0 to be 10 // Object.is equality

- Expected
+ Received

- 10
+ 0

 ❯ test/atendimento.e2e-spec.ts:464:30
    462|           expect(resposta.status).toBe(200);
    463|           const persistido = (await prisma.conversation.findUniqueOrTh…
    464|           expect(persistido).toBe(10);
       |                              ^
    465|           console.info(JSON.stringify({
    466|             prova: 'BCI_ACK_COM_SELECT_BLOQUEADO', lote: lote + 1,

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/1]⎯

npm notice
npm notice New major version of npm available! 10.9.9 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rule-spirit-final-api-app.log
```
Rule-Spirit Anti-Pattern Scan
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/api-app
Stacks: all
Findings: 30
Max active severity: warning

| Stack | Severity | Search Lens | Location | Evidence |
| --- | --- | --- | --- | --- |
| shared | review | hard-coded local/domain target in source/config | `test/browser-server.cjs:22` |   process.env.WEB_ORIGIN = 'http://127.0.0.1:4173'; |
| shared | review | hard-coded local/domain target in source/config | `test/browser-server.cjs:40` |   app.enableCors({ origin: ['http://127.0.0.1:4173'], credentials: true }); |
| shared | review | hard-coded local/domain target in source/config | `test/timeline-fixtures.cjs:64` |   const response = await fetch(`http://127.0.0.1:${apiPort}/webhooks/meta`, { |
| shared | review | hard-coded local/domain target in source/config | `test/timeline-fixtures.cjs:75` |       const query = new URL(req.url, 'http://localhost').searchParams; |
| shared | review | hard-coded local/domain target in source/config | `test/timeline-fixtures.cjs:113` | server.listen(fixturePort, '127.0.0.1', () => console.log(`timeline fixtures listening on 127.0.0.1:${fixturePort}`)); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:73` |     A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:74` |     B = await criarMantenedora(app, 'Beta', 'dono@beta.test'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:78` |     cookieOwner = await login(app, 'dono@alfa.test'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:102` |       await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'atendente@alfa.test', 'ATENDENTE'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:103` |       const cookie = await login(app, 'atendente@alfa.test'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:110` |       const cookieBeta = await login(app, 'dono@beta.test'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:177` |       await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro@alfa.test', 'ATENDENTE'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:178` |       const cookieOutro = await login(app, 'outro@alfa.test'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:203` |       await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro2@alfa.test', 'ATENDENTE'); |
| shared | review | hard-coded local/domain target in source/config | `test/atendimento.e2e-spec.ts:204` |       const cookieOutro = await login(app, 'outro2@alfa.test'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/browser-server.cjs:22` |   process.env.WEB_ORIGIN = 'http://127.0.0.1:4173'; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/browser-server.cjs:40` |   app.enableCors({ origin: ['http://127.0.0.1:4173'], credentials: true }); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/timeline-fixtures.cjs:64` |   const response = await fetch(`http://127.0.0.1:${apiPort}/webhooks/meta`, { |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/timeline-fixtures.cjs:75` |       const query = new URL(req.url, 'http://localhost').searchParams; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/timeline-fixtures.cjs:113` | server.listen(fixturePort, '127.0.0.1', () => console.log(`timeline fixtures listening on 127.0.0.1:${fixturePort}`)); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:73` |     A = await criarMantenedora(app, 'Alfa', 'dono@alfa.test'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:74` |     B = await criarMantenedora(app, 'Beta', 'dono@beta.test'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:78` |     cookieOwner = await login(app, 'dono@alfa.test'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:102` |       await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'atendente@alfa.test', 'ATENDENTE'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:103` |       const cookie = await login(app, 'atendente@alfa.test'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:110` |       const cookieBeta = await login(app, 'dono@beta.test'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:177` |       await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro@alfa.test', 'ATENDENTE'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:178` |       const cookieOutro = await login(app, 'outro@alfa.test'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:203` |       await criarUsuario(prisma, A.mantenedora.id, A.businessUnit.id, 'outro2@alfa.test', 'ATENDENTE'); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `test/atendimento.e2e-spec.ts:204` |       const cookieOutro = await login(app, 'outro2@alfa.test'); |

Note: this scanner supports the Rule-Spirit Anti-Pattern Hunt gate; it does not replace rule-specific review or P1/P2 judgment.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rule-spirit-final-web-app.log
```
Rule-Spirit Anti-Pattern Scan
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/web-app
Stacks: all
Findings: 42
Max active severity: warning

| Stack | Severity | Search Lens | Location | Evidence |
| --- | --- | --- | --- | --- |
| shared | review | hard-coded local/domain target in source/config | `src/tempoReal.spec.ts:12` |     expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws');  |
| shared | review | hard-coded local/domain target in source/config | `src/tempoReal.spec.ts:32` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() });  |
| shared | review | hard-coded local/domain target in source/config | `src/tempoReal.spec.ts:58` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout });  |
| shared | review | hard-coded local/domain target in source/config | `src/api.ts:75` |     const pareceEstatico = res.status === 405 \|\| /^\s*<(!doctype\|html)/i.test(bruto);  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:5` | const API = `http://127.0.0.1:${PORTA_DA_API}`;  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:26` |     baseURL: 'http://127.0.0.1:4173',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:32` |       url: 'http://127.0.0.1:3101/health',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:80` |         WEB_ORIGIN: 'http://127.0.0.1:4173',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:85` |       // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`,  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:88` |       // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:91` |       // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:93` |       command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort',  |
| shared | review | hard-coded local/domain target in source/config | `playwright.config.ts:97` |       url: 'http://127.0.0.1:4173',  |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline.spec.ts:3` | const FIXTURES = 'http://127.0.0.1:3101'; |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline.spec.ts:5` | const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`; |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:45` |   const apiEndpoint = `http://127.0.0.1:${apiPort}`; |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:48` |     fetch('http://127.0.0.1:3101/health'), |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:49` |     fetch('http://127.0.0.1:4173/'), |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:57` |   const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173')); |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:60` |   const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`); |
| shared | review | hard-coded local/domain target in source/config | `e2e/timeline-freshness.ts:93` |     endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname } |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/tempoReal.spec.ts:12` |     expect(enderecoDoSocket('http://localhost:3000', 'x')).toBe('ws://localhost:3000/ws');  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/tempoReal.spec.ts:32` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout: (fn: () => void) => { timers.push(fn); return timers.length; }, clearTimeout: vi.fn() });  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/tempoReal.spec.ts:58` |     vi.stubGlobal('window', { location: { origin: 'http://localhost' }, setTimeout, clearTimeout });  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `src/api.ts:75` |     const pareceEstatico = res.status === 405 \|\| /^\s*<(!doctype\|html)/i.test(bruto);  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:5` | const API = `http://127.0.0.1:${PORTA_DA_API}`;  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:26` |     baseURL: 'http://127.0.0.1:4173',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:32` |       url: 'http://127.0.0.1:3101/health',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:80` |         WEB_ORIGIN: 'http://127.0.0.1:4173',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:85` |       // `--host 127.0.0.1` NÃO é detalhe: o padrão do `vite preview` é `localhost`,  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:88` |       // `[::1]:4173` e o Playwright — que pergunta por `127.0.0.1` — bate em  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:91` |       // Todo o resto do harness já fala 127.0.0.1: a baseURL, o WEB_ORIGIN, o  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:93` |       command: 'npm run preview -- --host 127.0.0.1 --port 4173 --strictPort',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `playwright.config.ts:97` |       url: 'http://127.0.0.1:4173',  |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:45` |   const apiEndpoint = `http://127.0.0.1:${apiPort}`; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:48` |     fetch('http://127.0.0.1:3101/health'), |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:49` |     fetch('http://127.0.0.1:4173/'), |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:57` |   const jsResponse = await fetch(new URL(asset[1], 'http://127.0.0.1:4173')); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:60` |   const servedPath = resolve(web, 'dist', `.${new URL(asset[1], 'http://127.0.0.1').pathname}`); |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline-freshness.ts:93` |     endpoints: { apiHealth: apiHealth.status, fixtureHealth: fixtureHealth.status, preview: htmlResponse.status, servedBundle: new URL(asset[1], 'http://127.0.0.1:4173').pathname } |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline.spec.ts:3` | const FIXTURES = 'http://127.0.0.1:3101'; |
| docker | warning | hard-coded runtime/domain target in Docker or compose surface | `e2e/timeline.spec.ts:5` | const API = `http://127.0.0.1:${process.env.LEADSHUG_API_PORT ?? '3100'}`; |

Note: this scanner supports the Rule-Spirit Anti-Pattern Hunt gate; it does not replace rule-specific review or P1/P2 judgment.

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/test-quality-final-api-app.log
```
Test Quality Audit
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/api-app
Outcome heuristic: medium

Scan paths:
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/src/domain/inbox/timeline-pagination.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/atendimento.e2e-spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/browser-server.cjs
  - /mnt/c/unifast/leadshug/leadshug_now_docker/api-app/test/timeline-fixtures.cjs

Hard bypass markers:
  - none

Test-only support route usage:
  - none

Auth shortcut hints:
  - none

Status-only assertion hints:
  - 462:          expect(resposta.status).toBe(200);

No-exception-only assertion hints:
  - none

Ambient subject fallback hints:
  - none

DI override hints:
  - none

Mock / fallback hints:
  - none

Counts: hard_bypass=0 test_support=0 auth_shortcut=0 status_only=1 no_exception_only=0 ambient_subject_fallback=0 di_override=0 mock_hint=0

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/test-quality-final-web-app.log
```
Test Quality Audit
Repository: /mnt/c/unifast/leadshug/leadshug_now_docker/web-app
Outcome heuristic: medium

Scan paths:
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline-freshness.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/e2e/timeline.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/playwright.config.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/tempoReal.spec.ts
  - /mnt/c/unifast/leadshug/leadshug_now_docker/web-app/src/timeline.test.ts

Hard bypass markers:
  - none

Test-only support route usage:
  - none

Auth shortcut hints:
  - none

Status-only assertion hints:
  - 9:  expect(response.status()).toBe(201);
  - 41:  expect(response.status()).toBe(200);
  - 43:  expect(webhook.status).toBe(200);
  - 128:    expect(burst.status()).toBe(201);
  - 150:    expect(burst.status()).toBe(201);
  - 171:    expect(burst.status()).toBe(201);
  - 190:    expect(burst.status()).toBe(201);
  - 257:          expect(lateTie.status()).toBe(201);
  - 268:          expect(webhook.status).toBe(200);
  - 337:      expect(event.status).toBe(200);
  - 407:      expect(secondEvent.status).toBe(200);
  - 547:    expect(populateSecondary.status()).toBe(201);
  - 548:    expect(populateOtherBu.status()).toBe(201);

No-exception-only assertion hints:
  - none

Ambient subject fallback hints:
  - 73:    completedMigrations = Number(rows[0]?.count ?? 0);

DI override hints:
  - none

Mock / fallback hints:
  - none

Counts: hard_bypass=0 test_support=0 auth_shortcut=0 status_only=13 no_exception_only=0 ambient_subject_fallback=1 di_override=0 mock_hint=0

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision3-final-frc3-20261015.log
```
v22.23.3

> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-DKhXhPnI.js   224.03 kB │ gzip: 69.70 kB
✓ built in 1.35s
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice

> @leadshug/api@0.1.0 build
> nest build

[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 3 tests using 1 worker

  ✓  1 e2e/timeline.spec.ts:212:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (2.1s)
  ✓  2 e2e/timeline.spec.ts:212:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.8s)
  ✓  3 e2e/timeline.spec.ts:212:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.8s)

  3 passed (22.5s)

EXIT_CODE=0 RUN_ID=web-authority-revision3-final-frc3-20261015

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision3-final-full-20261015.log
```
v22.23.3
COMMAND npm test

> @leadshug/web@0.1.0 test
> vitest run


 RUN  v2.1.9 /workspace/web-app

 ✓ src/timeline.test.ts (2 tests) 4ms
 ✓ src/tempoReal.spec.ts (6 tests) 8ms
 ✓ src/api.spec.ts (12 tests) 45ms

 Test Files  3 passed (3)
      Tests  20 passed (20)
   Start at  04:22:40
   Duration  739ms (transform 467ms, setup 0ms, collect 553ms, tests 57ms, environment 1ms, prepare 324ms)

npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice
COMMAND npm run test:tela

> @leadshug/web@0.1.0 test:tela
> npm run build && playwright test


> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-DKhXhPnI.js   224.03 kB │ gzip: 69.70 kB
✓ built in 1.46s
[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 34 tests using 1 worker

  ✓   1 e2e/telas.spec.ts:78:3 › as telas, no navegador › sem sessão, qualquer URL leva ao login (250ms)
  ✓   2 e2e/telas.spec.ts:84:3 › as telas, no navegador › entrar leva de volta para a página que se queria abrir (892ms)
  ✓   3 e2e/telas.spec.ts:96:3 › as telas, no navegador › conta nova cai no wizard, e a Revisão diz qual é o próximo passo (925ms)
  ✓   4 e2e/telas.spec.ts:138:3 › as telas, no navegador › toda tela do menu abre sem quebrar (1.6s)
  ✓   5 e2e/telas.spec.ts:167:3 › as telas, no navegador › a paleta é a do desenho, e o tema segue a marca da conta (989ms)
  ✓   6 e2e/telas.spec.ts:191:3 › as telas, no navegador › os grupos do menu retraem, e a escolha sobrevive à navegação (984ms)
  ✓   7 e2e/telas.spec.ts:209:3 › as telas, no navegador › o tema é escolha de quem olha, e persiste (939ms)
  ✓   8 e2e/telas.spec.ts:227:3 › as telas, no navegador › Meu perfil abre pelo rodapé e salva o próprio nome (962ms)
  ✓   9 e2e/telas.spec.ts:246:3 › as telas, no navegador › a foto de perfil sobe, e a recusa do servidor aparece na tela (1.1s)
  ✓  10 e2e/telas.spec.ts:276:3 › as telas, no navegador › a barra lateral tem os três grupos do desenho (901ms)
  ✓  11 e2e/telas.spec.ts:290:3 › as telas, no navegador › Setores abre com o Geral, e o Histórico já mostra o que aconteceu (922ms)
  ✓  12 e2e/telas.spec.ts:302:3 › as telas, no navegador › a inbox abre, com o número no seletor e sem conversa nenhuma (805ms)
  ✓  13 e2e/telas.spec.ts:319:3 › as telas, no navegador › Pessoas abre, lista quem já existe e oferece os papéis que existem (868ms)
  ✓  14 e2e/telas.spec.ts:338:3 › as telas, no navegador › adicionar uma pessoa e conceder um setor a ela (1.0s)
  ✓  15 e2e/telas.spec.ts:357:3 › as telas, no navegador › convidar mostra o LINK quando o e-mail não sai, e ele leva a definir a senha (1.2s)
  ✓  16 e2e/telas.spec.ts:380:3 › as telas, no navegador › esqueci minha senha responde igual, exista a conta ou não (248ms)
  ✓  17 e2e/telas.spec.ts:391:3 › as telas, no navegador › a tela de números mostra a BU e os dois canais desconectados (890ms)
  ✓  18 e2e/telas.spec.ts:401:3 › as telas, no navegador › sair volta para o login (837ms)
  ✓  19 e2e/telas.spec.ts:411:3 › as telas, no navegador › identidade visual carrega e salva os campos pós-onboarding (1.0s)
  ✓  20 e2e/telas.spec.ts:430:3 › as telas, no navegador › Typebot permite buscar, abrir o editor e configurar um gatilho (1.5s)
  ✓  21 e2e/timeline.spec.ts:56:3 › timeline da inbox com backend e PostgreSQL reais › expõe o estado de abertura enquanto a primeira página aguarda o backend (865ms)
  ✓  22 e2e/timeline.spec.ts:90:3 › timeline da inbox com backend e PostgreSQL reais › abre a página recente, carrega todas as páginas anteriores e preserva posição (1.2s)
  ✓  23 e2e/timeline.spec.ts:121:3 › timeline da inbox com backend e PostgreSQL reais › reconecta sem evento posterior e recupera 130 mensagens em mais de uma rodada (1.3s)
  ✓  24 e2e/timeline.spec.ts:146:3 › timeline da inbox com backend e PostgreSQL reais › o poll retoma uma rodada pendente sem evento novo nem clique de continuação (1.2s)
  ✓  25 e2e/timeline.spec.ts:168:3 › timeline da inbox com backend e PostgreSQL reais › recupera o histórico completo após uma thread vazia receber mais de uma página (873ms)
  ✓  26 e2e/timeline.spec.ts:181:3 › timeline da inbox com backend e PostgreSQL reais › retoma thread vazia após evento entre rodadas e inclui toda a cabeça sem reler (1.2s)
  ✓  27 e2e/timeline.spec.ts:212:3 › timeline da inbox com backend e PostgreSQL reais › preserva o piso T após evento coalescido e encontra ID menor inserido atrás do cursor percorrido (1.6s)
  ✓  28 e2e/timeline.spec.ts:299:3 › timeline da inbox com backend e PostgreSQL reais › falhas de recuperação consomem o orçamento e exigem continuação explícita (1.5s)
  ✓  29 e2e/timeline.spec.ts:363:3 › timeline da inbox com backend e PostgreSQL reais › erro no cursor histórico reinicia pela cabeça após evento novo (1.3s)
  ✓  30 e2e/timeline.spec.ts:434:3 › timeline da inbox com backend e PostgreSQL reais › preserva a âncora quando uma mensagem chega durante o backfill atrasado (916ms)
  ✓  31 e2e/timeline.spec.ts:467:3 › timeline da inbox com backend e PostgreSQL reais › mescla envio real com autoria e mantém o novo draft digitado durante o envio (779ms)
  ✓  32 e2e/timeline.spec.ts:493:3 › timeline da inbox com backend e PostgreSQL reais › mostra thread vazia/fim, falha recuperável e acesso perdido (2.0s)
  ✓  33 e2e/timeline.spec.ts:519:3 › timeline da inbox com backend e PostgreSQL reais › close vence resposta de backfill atrasada (954ms)
  ✓  34 e2e/timeline.spec.ts:540:3 › timeline da inbox com backend e PostgreSQL reais › troca de conversa e BU protege resposta atrasada de envio (3.5s)

  34 passed (55.8s)

EXIT_CODE=0 RUN_ID=web-authority-revision3-final-full-20261015

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-revision3-budget-negative-control-20261015.log
```
v22.23.3

> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-CAD021o2.js   223.96 kB │ gzip: 69.69 kB
✓ built in 1.32s
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice
[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 1 test using 1 worker

  ✘  1 e2e/timeline.spec.ts:299:3 › timeline da inbox com backend e PostgreSQL reais › falhas de recuperação consomem o orçamento e exigem continuação explícita (1.6s)


  1) e2e/timeline.spec.ts:299:3 › timeline da inbox com backend e PostgreSQL reais › falhas de recuperação consomem o orçamento e exigem continuação explícita 

    Error: expect(received).toBe(expected) // Object.is equality

    Expected: 3
    Received: 5

      343 |     await expect(page.getByRole('button', { name: 'Continuar atualização' })).toBeVisible();
      344 |     expect(attempts).toBe(3);
    > 345 |     expect(recoveryRequests).toBe(3);
          |                              ^
      346 |     expect(maxInFlight).toBe(1);
      347 |     await page.waitForTimeout(300);
      348 |     expect(recoveryRequests).toBe(3);
        at /workspace/web-app/e2e/timeline.spec.ts:345:30

    Error Context: test-results/timeline-timeline-da-inbox-c0aef-xigem-continuação-explícita/error-context.md

    attachment #2: trace (application/zip) ─────────────────────────────────────────────────────────
    test-results/timeline-timeline-da-inbox-c0aef-xigem-continuação-explícita/trace.zip
    Usage:

        npx playwright show-trace test-results/timeline-timeline-da-inbox-c0aef-xigem-continuação-explícita/trace.zip

    ────────────────────────────────────────────────────────────────────────────────────────────────

  1 failed
    e2e/timeline.spec.ts:299:3 › timeline da inbox com backend e PostgreSQL reais › falhas de recuperação consomem o orçamento e exigem continuação explícita 

EXIT_CODE=1 RUN_ID=web-revision3-budget-negative-control-20261015 MUTATION=decrement-after-await

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-revision3-budget-negative-control-20261015.restore
```
count=4; restoredBytesExact=True; sourceSha256=1af04dee7cad573fc4920cdac7ecb77ddd352200a7ff30dba450508a7f191521

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-revision3-cursor-negative-control-20261015.log
```
v22.23.3

> @leadshug/web@0.1.0 build
> tsc -b && vite build

vite v5.4.21 building for production...
transforming...
✓ 55 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                   0.69 kB │ gzip:  0.44 kB
dist/assets/index-wuzy3kMN.css    8.32 kB │ gzip:  2.39 kB
dist/assets/index-3k5pQ0yc.js   223.99 kB │ gzip: 69.69 kB
✓ built in 1.42s
npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.0
npm notice To update run: npm install -g npm@12.2.0
npm notice
[WebServer] timeline fixtures listening on 127.0.0.1:3101
[WebServer] 
[WebServer] > @leadshug/api@0.1.0 build
[WebServer] > nest build
[WebServer] 
[WebServer] timeline test API listening on 3100; database leadshug_timeline_20261014
[WebServer] 
[WebServer] > @leadshug/web@0.1.0 preview
[WebServer] > vite preview --host 127.0.0.1 --port 4173 --strictPort
[WebServer] 
[WebServer]   ➜  Local:   http://127.0.0.1:4173/

Running 1 test using 1 worker

  ✘  1 e2e/timeline.spec.ts:363:3 › timeline da inbox com backend e PostgreSQL reais › erro no cursor histórico reinicia pela cabeça após evento novo (6.3s)


  1) e2e/timeline.spec.ts:363:3 › timeline da inbox com backend e PostgreSQL reais › erro no cursor histórico reinicia pela cabeça após evento novo 

    Error: expect(received).toBe(expected) // Object.is equality

    Expected: 2
    Received: 1

    Call Log:
    - Timeout 5000ms exceeded while waiting on the predicate

      411 |       await expect(page.getByRole('alert')).toHaveText('Não foi possível atualizar o histórico. Tente novamente.');
      412 |       await expect(page.getByText('Atualização pendente. O histórico pode ter uma lacuna.')).toBeVisible();
    > 413 |       await expect.poll(() => requestsRecentes).toBe(2);
          |                                                 ^
      414 |       await expect.poll(() => inFlight).toBe(0);
      415 |       expect(requestsHistoricos).toBe(1);
      416 |       expect(maxInFlight).toBe(1);
        at /workspace/web-app/e2e/timeline.spec.ts:413:49

    Error Context: test-results/timeline-timeline-da-inbox-74e82-ela-cabeça-após-evento-novo/error-context.md

    attachment #2: trace (application/zip) ─────────────────────────────────────────────────────────
    test-results/timeline-timeline-da-inbox-74e82-ela-cabeça-após-evento-novo/trace.zip
    Usage:

        npx playwright show-trace test-results/timeline-timeline-da-inbox-74e82-ela-cabeça-após-evento-novo/trace.zip

    ────────────────────────────────────────────────────────────────────────────────────────────────

  1 failed
    e2e/timeline.spec.ts:363:3 › timeline da inbox com backend e PostgreSQL reais › erro no cursor histórico reinicia pela cabeça após evento novo 

EXIT_CODE=1 RUN_ID=web-revision3-cursor-negative-control-20261015 MUTATION=removed-dirty-cursor-restart

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-revision3-cursor-negative-control-20261015.restore
```
restoredBytesExact=True; sourceSha256=821ce011ce5738e40caeafa2c3fad20b9583053ce2373bb194abbeee567bc783

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-eps.json
```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "EPS",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "explain-exact-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-native",
  "recorded_at_utc": "2026-10-15T03:36:56Z",
  "evidence_type": "explain",
  "sample_profile_id": "EPS-SP-STRONG",
  "acceptance_rule_id": "EPS-A2",
  "result_summary": "Measured recent/deep/tied pages on20382 rows,1000 ties; existing index retained after candidate trial. Independent judgment pending.",
  "artifact_payload": {
    "access_pattern_classification": {
      "authorization": "exact conversation/grant lookup before query validation",
      "anchor": "scoped message id lookup",
      "page": "conversation_id + strict lexicographic before + DESC(created_at,id) + LIMIT51",
      "response": "ascending order,50 messages max"
    },
    "touched_path_audit_summary": "BFF resolver/parser/service and active-conversation UI consumer; no public API/Consultar changes.",
    "strong_query_evidence_type": "explain",
    "fixture": {
      "conversation_rows": 20382,
      "maximum_timestamp_tie": 1000,
      "deep_anchor_offset_for_selection_only": 10000
    },
    "measurements": [
      {
        "scenario": "recent",
        "execution_ms": 1.094,
        "rows_returned": 51,
        "index_rows": 1001,
        "shared_hit_buffers": 37,
        "sort": "incremental/top-N"
      },
      {
        "scenario": "deep",
        "execution_ms": 3.442,
        "rows_returned": 51,
        "index_rows_surviving": 1000,
        "rows_removed_by_filter": 10001,
        "shared_hit_buffers": 357,
        "sort": "incremental/top-N"
      },
      {
        "scenario": "tie",
        "execution_ms": 0.85,
        "rows_returned": 51,
        "index_rows_surviving": 500,
        "rows_removed_by_filter": 501,
        "shared_hit_buffers": 37,
        "sort": "incremental/top-N"
      }
    ],
    "candidate_index": {
      "columns": [
        "conversation_id",
        "created_at DESC",
        "id DESC"
      ],
      "deep_execution_ms": 3.942,
      "deep_shared_hit_buffers": 9832,
      "rows_removed_by_filter": 10001,
      "decision": "not retained; same OR predicate still filters depth, heap access larger than existing index; no measured need for production migration"
    },
    "residual_risk": "Deep OR keyset still filters newer rows; timings are local warm data, not a production capacity or SLO claim.",
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-timeline-exact.sql",
        "sha256": "30b7477601cd109ffd3af7d38e9df1e5fbf8a6af56bf90cf52a42f4779ee0cb8"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-timeline-exact.log",
        "sha256": "6e346b5b0609de7f347481fb2b4eccc93e4ddf8b41219bb1348fbf169af9b9b6"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-index-trial.sql",
        "sha256": "8ac4343ac0633b5b1535e171ec7466e58c5c6488d1de8abc516b15f6e6b914a3"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/explain-index-trial.log",
        "sha256": "43251847c09a71819a11aa135c8710b72a3eb4af2188f07bd3c071bfa980171c"
      }
    ]
  },
  "artifact_sha256": "f20722cdaae0a7cddea80dbcb2df929035d742f47b49ab7f64a17444a9a79c83"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-frc.json
```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "FRC",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "web-authority-revision3-final-frc3-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-chromium-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-delta-native",
  "recorded_at_utc": "2026-10-15T04:25:48Z",
  "evidence_type": "source-owned-playwright-real-backend-races",
  "sample_profile_id": "FRC-SP-M",
  "acceptance_rule_id": "FRC-A1",
  "result_summary": "Full34/34 and FRC3/3 passed on identical current source/build; shared3-attempt budget incl failures, retained T/restart, opening and empty notifications, context success/error/backfill covered. Independent delta judgment pending.",
  "artifact_payload": {
    "concurrency_policy": "serialize",
    "policy_by_action": [
      {
        "action": "recovery",
        "policy": "serialize",
        "guard": "single-flight per generation,coalesce dirty,next pass retains pendingT,max3pagequeries per round"
      },
      {
        "action": "context switch",
        "policy": "cancel previous",
        "guard": "logical cancellation by BU/conversation/generation on responses/errors/draft/scroll"
      },
      {
        "action": "backfill/send",
        "policy": "drop duplicate",
        "guard": "in-flight flags and current-generation draft ref"
      },
      {
        "action": "metadata",
        "policy": "last-write-wins",
        "guard": "version-controlled current response; historical pages never overwrite metadata"
      }
    ],
    "burst_profile_observed": {
      "triggers_per_repetition": 10,
      "repetitions": 3,
      "cases_passed": 3,
      "pushes_asserted_per_repetition": 12,
      "pushes_note": "one initial head,10 real incoming webhooks during blocked traversal,one new event after third query;12 frames/unread; only3 automatic requests and max1 in flight before explicit Continue",
      "full_suite": {
        "cases_passed": 34,
        "duration_seconds": 55.8
      }
    },
    "runner_or_manual_path": "web-app/e2e/timeline.spec.ts; npm run test:tela; npx playwright test e2e/timeline.spec.ts --grep=\"preserva o piso T\" --repeat-each=3",
    "race_matrix": [
      {
        "surface": "history",
        "case": "251 IDs; prepend same visible anchor offset delta<2px, including arrival while delayed actual response"
      },
      {
        "surface": "recovery",
        "case": "H>T,late lower UUID inT behind walked cursor,dirty restart retains originalT; first authorized round exactly3requests/max1inflight, third-request event cannot mintbudget; full DB/UI ID equality and unread12 after Continue"
      },
      {
        "surface": "reconnect",
        "case": "real network disconnect and burst130 while offline; recover without subsequent message event"
      },
      {
        "surface": "poll",
        "case": "60s clock advancement resumes pending>3page recovery without more events or Continue click,full382 IDs"
      },
      {
        "surface": "send/draft/context",
        "case": "actual delayed POST, persisted author and typednewdraft preservation; full sixsubcase destination protection described below"
      },
      {
        "surface": "metadata",
        "case": "close wins over delayed historical response; no stale status restoration"
      },
      {
        "surface": "states",
        "case": "loading,empty,end,error/retry and grant-loss404; no fabricated BFF payloads"
      },
      {
        "surface": "budget/error",
        "case": "3 aborted actual GETs with real events consume3 attempts, no4th beforeContinue; negative control post-await debit fails3vs5; canonical restoration and full suite green"
      },
      {
        "surface": "historical error/restart",
        "case": "actual older page aborted while real new head arrives; recent-query restart required without another event, full tied-group IDs/unread after authorized continuations; negative control removedguard fails2vs1 recent reads"
      },
      {
        "surface": "opening",
        "case": "real initial GET snapshot held, real inbound frame during opening, read-neutral recovery without later trigger; unread preserved"
      },
      {
        "surface": "empty paused recovery",
        "case": "initiallyempty>3pages plus between-round inbound, retains recent restart through full IDs/currentmetadata"
      },
      {
        "surface": "context destination",
        "case": "BOTH BU and conversation, old send success/network failure and backfill; destination selection/draft/error/IDs/metadata/scroll compared after release"
      }
    ],
    "runtime_freshness": {
      "captured_before_workers": "2026-10-15T04:24:16.848Z",
      "served_equals_dist_sha256": "2da409a40ead5ef488b6ef33a9d6adc01e5befd9686d083bb1e53c7c0c42589e",
      "full_attestation_captured_at": "2026-10-15T04:22:58.946Z",
      "source_manifest_matches_full_suite": true,
      "root_verified_all16_current_source_hashes": true
    },
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision3-final-full-20261015.log",
        "sha256": "db751c5b21cef3d774c7d2d0fa44cc373f879ae4c8c35abac65d085d63367e9c"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/web-authority-revision3-final-frc3-20261015.log",
        "sha256": "bf502bd2d032c2b2a37a50ccf6f2cb08e99dd86f756b20fc8355ede706148a1d"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-web-authority-revision3-final-full-20261015.json",
        "sha256": "94ceadbb83ef431eea7411cd28650d34626f196b5f344240c39ef294da20cc28"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/attestation-browser-web-authority-revision3-final-frc3-20261015.json",
        "sha256": "20e72c9376a276b6083d14688c4820b2f2169955ff28da152cd3cf82d4cd6716"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/executor-revision3-summary.json",
        "sha256": "9a9f40e727f497e5721ed9dc9af222dd91373f4266c1d84008ed4b9e1fb9a0e8"
      }
    ],
    "residual_risk": "Bounded active-conversation memory grows as user loads history; no cache of other conversations. Backdated imports earlier thanT group and production traffic/provider transport are outside this approved slice."
  },
  "artifact_sha256": "9e0a448cc4d1cb625c350355e7f4f08c7b138db4116a29471e92300f9a1798b7"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-bci.json
```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "BCI",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "bci-ack-barrier-canonical-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-native",
  "recorded_at_utc": "2026-10-15T03:36:56Z",
  "evidence_type": "postgresql-overlap-probe",
  "sample_profile_id": "BCI-SP-M",
  "acceptance_rule_id": "BCI-A1",
  "result_summary": "Three deterministic real PostgreSQL barrier batches retain10 increments after ACK; regression mutation fails10vs0 and exact source restoration passes. Independent judgment pending.",
  "artifact_payload": {
    "invariant_id": "ST-ATT-01-ACK-BEFORE-PAGE-PRESERVES-LATER-INCREMENTS",
    "concurrency_policy": "serialize",
    "probe_profile_observed": {
      "overlapping_operations_per_batch": 10,
      "batches": 3,
      "barrier": "ACCESS EXCLUSIVE on messages; pg_stat_activity proves page SELECT blocked, Conversation updates remain unblocked",
      "records": [
        {
          "prova": "BCI_ACK_COM_SELECT_BLOQUEADO",
          "lote": 1,
          "bloqueioDetectado": true,
          "sondagens": 2,
          "ackAteSelectBloqueadoMs": 83,
          "dezIncrementosMs": 42,
          "unreadEnquantoSelectBloqueado": 10,
          "unreadDepoisDaResposta": 10
        },
        {
          "prova": "BCI_ACK_COM_SELECT_BLOQUEADO",
          "lote": 2,
          "bloqueioDetectado": true,
          "sondagens": 2,
          "ackAteSelectBloqueadoMs": 55,
          "dezIncrementosMs": 24,
          "unreadEnquantoSelectBloqueado": 10,
          "unreadDepoisDaResposta": 10
        },
        {
          "prova": "BCI_ACK_COM_SELECT_BLOQUEADO",
          "lote": 3,
          "bloqueioDetectado": true,
          "sondagens": 2,
          "ackAteSelectBloqueadoMs": 53,
          "dezIncrementosMs": 26,
          "unreadEnquantoSelectBloqueado": 10,
          "unreadDepoisDaResposta": 10
        }
      ]
    },
    "mutation_control": {
      "change": "Move ACK after SELECT (old regression)",
      "observed": "Expected10, received0; failed regression assertion",
      "restoration": "Exact original bytes restored in finally; SHA log retained; canonical targeted1/1 passes; broad API224 passed before byte-identical mutation/restoration",
      "test_first_classification": "test-after with negative control, not retroactive TDD"
    },
    "coverage": "FullAPI224 also covers real incoming overlap, post-boundary IN=>11, auth/query errors without writes, background neutral and close/read overlap.",
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/api-e2e-authority.log",
        "sha256": "b508ca43e5157fea8fbf6951b2bd2b7c2b860ebde3e4c2dca1971094436317db"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-mutation-control.log",
        "sha256": "0c2b211c2078240a09519eeff76f2a32a358135090e32df1bb871c619d4e327d"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-canonical-after-mutation.log",
        "sha256": "90fe5dd92cf6098fc7375258ba7452a29c4d74255d10fafd2efcc4c8b4866b4c"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/bci-source-restored.sha256",
        "sha256": "c9f7e6985e02086dfc2a79cdf10dc4204ec5b61db7bb3b8913a9abee25bc0625"
      }
    ]
  },
  "artifact_sha256": "93eeac265b3c77b17e6fee0cbd20223a56cbe44fe17489052b9b4feeffa37995"
}

```

## foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/pcv-rls.json
```
{
  "policy_schema_version": "pcv-1",
  "schema_version": "pcv-1",
  "lane_id": "RLS",
  "todo_id": "TODO-leadshug-inbox-message-timeline-pagination",
  "run_id": "rls-read-stage1-20261015",
  "environment_id": "principal-checkout-linux-node22-postgresql16-disposable",
  "executor_id": "/root/timeline_executor_resume",
  "reviewer_id": "delivery-adherence-native",
  "recorded_at_utc": "2026-10-15T03:39:44Z",
  "evidence_type": "one-stage-authenticated-read-load",
  "sample_profile_id": "RLS-SP-L",
  "acceptance_rule_id": "RLS-A1",
  "result_summary": "30/30 reads,5 concurrent×6; p50 23.36ms,p95 64.26ms,max68.5ms; page50,unread7 unchanged,251 messages unchanged,foreign malformed request404. Review pending, no production SLO claim.",
  "artifact_payload": {
    "stage_profile_observed": {
      "mode": "load",
      "stages": 1,
      "concurrency": 5,
      "batches": 6,
      "requests": 30,
      "dataset_messages": 251,
      "transport": "real authenticated BFF HTTP on disposable test Nest runtime"
    },
    "thresholds": {
      "errors": {
        "expected": 0,
        "actual": 0,
        "passed": true
      },
      "response_rows": {
        "expected": 50,
        "actual": 50,
        "passed": true
      },
      "has_previous": {
        "expected": true,
        "actual": true,
        "passed": true
      },
      "read_neutral": {
        "expected_unread": 7,
        "before": 7,
        "after": 7,
        "passed": true
      },
      "history_unchanged": {
        "before": 251,
        "after": 251,
        "passed": true
      },
      "authorization_first": {
        "expected": 404,
        "actual": 404,
        "passed": true
      },
      "latency": "measured only; no production SLO threshold authorized"
    },
    "metrics_summary": {
      "runId": "rls-read-stage1-20261015",
      "sample": {
        "requests": 30,
        "concurrency": 5,
        "batches": 6,
        "statusCounts": {
          "200": 30,
          "errors": 0
        },
        "p50Ms": 23.36,
        "p95Ms": 64.26,
        "maxMs": 68.5,
        "messagesPerResponse": 50,
        "hasPrevious": true
      },
      "scope": {
        "accessibleConversation": "200 x30",
        "foreignConversationWithMalformedCursor": 404,
        "unreadBefore": 7,
        "unreadAfter": 7,
        "messagesBefore": 251,
        "messagesAfter": 251
      },
      "conclusion": "small disposable one-stage read-neutral sample; no production SLO inferred"
    },
    "scope_probe_parameter": "Actual runner sends limite=invalid; raw output key foreignConversationWithMalformedCursor is an imprecise label for malformed query, not a cursor probe. Dedicated API E2E covers actual malformed/foreign cursors.",
    "threshold_origin": "Fixed stage loops and hard-failing assertions in raw runner before execution; no post-hoc latency acceptance invented.",
    "raw_artifacts": [
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rls-read-sample.log",
        "sha256": "5b68b1b5f450153c7fa6c36c277aa19d5846860f63ef8124a1eaeb32dd3941fc"
      },
      {
        "path": "foundation_documentation/artifacts/reviews/leadshug-inbox-timeline-20261014/evidence/rls-read-sample.mjs",
        "sha256": "d59fa9f53ffeb97aec02b32ccf91584868f1e2b1ebcd644278f00881ae3a3321"
      }
    ],
    "residual_risk": "Small warm disposable one-stage sample; no stress, spike, soak, throughput or production capacity certification."
  },
  "artifact_sha256": "b9b05d0bd9127e4347e04685a91379924153c7c3a4f9b7445e8fa5ed9f548b3c"
}

```

## Full applicable audit and resolution questions
Adherence: verify frozen API contract/authorization/read-neutral ACK, strict bounded SQL/scoped cursors, source identities, and focus ARCH-DEL-01..03 with current scheduling transitions. Check three total attempts per EXPLICIT round incl failed queries and dirty passes; negative control must fail the old post-await debit; restart recent after an older-page failure with dirty/new head, single-flight, paused events retaining restart/T, empty>3pages+between-round event, opening notifications/generation and reconnection behavior. Test-quality: evaluate all applicable test-quality-audit axes, product/test alignment, workaround/retrofit risk, assertion efficacy/efficiency/sufficiency, honest test-after, real boundaries/DI/auth/PG/WebSocket, owned fixture and source-owned test discovery, no skip/focus/fallback/fake BFF payload, positive/negative/readback, exact commands/topology/runtime/build/served-source freshness before workers. Examine request counts/max in-flight around held real third response; destination draft/error/scroll/messages/metadata for BOTH conversation and BU switches with old success/network failure/backfill completion. RawCI retention is now required to resolve TQA-EVID-03; unchanged API source means no gratuitous API224 repeat. Assess EPS/deep scan residual/no-index decision, BCI10×3 negative control+restoration, RLS one measured bounded stage, and refreshed FRC10×3. Derive conclusions for ALL applicable rubric axes, not a short answer. State exactly which original findings are resolved or remain open, and report new real regressions without redesign outside scope. Preserve transparent React owner npm run test:tela mapping; no Flutter command executed. Return canonical JSON only. Findings first, severity/file:line/counterexample/why-now/options/recommendation. Put detailed audit conclusions and decision mapping in overall_assessment/recommended_path strings. Do not infer waiver or approval from previous positive sub-findings.
