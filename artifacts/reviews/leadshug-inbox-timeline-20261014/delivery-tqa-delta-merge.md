# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-tqa-delta-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `acceptable`

## Recommended Paths
- `Keep the approved architecture and repair only the two missing browser regressions. Make the paused-empty scenario use chronologically older backlog data, assert that the first post-event resume is a fresh head request rather than an old-cursor request, and add a failing old-cursor mutation control. Add a held-opening real reconnect scenario with no later message trigger. Rerun the affected tests, the full project-owned npm run test:tela suite, and the repeated FRC evidence against the resulting source manifest; retain existing unchanged API evidence. Then request a bounded delta review.`

## Merged Findings
### F-62C9D827 [medium] [P2] Opening-race coverage omits reconnect while the initial response is held
- **Reviewers:** delivery-tqa-delta-native-no-context
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `timeline-opening-reconnect-must-trigger-recovery`
- **Suggested action:** A (recommended): hold the actual opening GET after its backend fetch, force a real socket reconnect while it remains pending, and require a read-neutral recovery without a later message event or clock advance; assert current IDs and unread after release. B: add an equivalent browser-level controllable real-socket integration case. C: rely on the helper unit test plus the post-opening reconnect test, which does not protect this opening-generation transition.
- **Rationale:** web-app/e2e/timeline.spec.ts:56 proves a real inbound message during a held opening response, but not an onopen/reconnect callback in that same threadAtual-null state. src/tempoReal.spec.ts:25 uses a fake socket to prove callback emission, while the browser reconnect case at web-app/e2e/timeline.spec.ts:121 begins after opening has completed. A regression that suppresses or misroutes the reconnect callback only while invalidacaoAbertura is active would pass all supplied assertions, despite the approved requirement that reconnection recover without a further event or poll.

### F-248119D3 [medium] [P2] Empty-thread recovery test does not prove restart from the new head
- **Reviewers:** delivery-tqa-delta-native-no-context
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `timeline-empty-paused-recovery-must-restart-at-head`
- **Suggested action:** A (recommended): seed the burst in the past so each real inbound event is newer, instrument the resumed request and require a read-neutral recent-page request without antes before any older traversal, then retain complete ID/unread and visible current-metadata assertions. Add a mutation that retains the old empty-thread cursor and require this regression to fail. B: provide explicit inbound timestamps later than the burst with the same request-level assertion. C: retain final-state equality alone, which leaves the reviewed stale-cursor behavior unprotected.
- **Rationale:** web-app/e2e/timeline.spec.ts:181 seeds the 160-message burst at Date.now()+10_000, then sends both inbound webhooks through a fixture that supplies no message timestamp (api-app/test/timeline-fixtures.cjs:57). The final run completes far inside that ten-second offset, so receipt-time inbound messages are older than the entire burst. A broken paused-empty branch that retains its old cursor can load the remaining ten burst rows plus the two older inbound rows after Continue, still reach 162 IDs and unread=2, and never issue the required fresh-head read. The test counts only the initial three requests and never asserts that the first request after the between-round event has no antes cursor. It therefore does not discriminate the ARCH-DEL-02 regression or prove current metadata refresh in that path.

## Reviewer Summaries
### delivery-tqa-delta-native-no-context
- **Assessment:** Return for focused test-evidence repair. TQA-TL-01 is resolved: final-source browser tests directly count three requests, maximum one in flight, third-request dirty behavior, failure-budget consumption, explicit continuation, and complete ID/unread readback; the post-await-debit negative control fails 3 versus 5. The dirty historical-cursor restart has an equally discriminating negative control. TQA-TL-02 is resolved through the six real destination cases covering conversation/BU times delayed send success, network failure, and backfill with draft, error, IDs, metadata, selection, and scroll assertions. TQA-EVID-03 is resolved by retained raw API generate/lint/build/unit output; unchanged API identity makes the retained API224 evidence proportionate.

Test effectiveness remains mixed because two prior transition obligations are not directly discriminated: the empty-thread between-round test orders its burst after the inbound events, and opening coverage does not combine an actual reconnect with the held opening response. Test efficiency is otherwise acceptable: source-owned full commands, targeted mutation controls, and three repetitions of the high-risk FRC case are proportionate. The package uses real Nest/session/grant/PostgreSQL/WebSocket boundaries, owned fixtures, fresh served-bundle attestation, and no skip/focus, fake BFF payload, ambient proof subject, or broad fallback.

Performance is mixed but honestly bounded: EPS records the deep 10,001-row residual and a worse composite-index trial without claiming a production SLO; BCI's real PostgreSQL barrier and 10-by-3 mutation control are strong; RLS is correctly described as a limited local sample. The React owner remains a simple faithful implementation rather than a new cache/framework. Operational fit is otherwise sound: Node 22, disposable PostgreSQL, real browser runner, retained leaf logs, and no remote-CI/deployment claim. ARCH-DEL-01, ARCH-DEL-01-ERR, TQA-TL-01, TQA-TL-02, and TQA-EVID-03 are closed by this package; ARCH-DEL-02 and ARCH-DEL-03 remain open as test-evidence gaps.
- **Recommended path:** `Keep the approved architecture and repair only the two missing browser regressions. Make the paused-empty scenario use chronologically older backlog data, assert that the first post-event resume is a fresh head request rather than an old-cursor request, and add a failing old-cursor mutation control. Add a held-opening real reconnect scenario with no later message trigger. Rerun the affected tests, the full project-owned npm run test:tela suite, and the repeated FRC evidence against the resulting source manifest; retain existing unchanged API evidence. Then request a bounded delta review.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `mixed`
- **Operational fit:** `acceptable`
- **Findings:**
  - [medium] ARCH-DEL-02 [P2] Empty-thread recovery test does not prove restart from the new head: web-app/e2e/timeline.spec.ts:181 seeds the 160-message burst at Date.now()+10_000, then sends both inbound webhooks through a fixture that supplies no message timestamp (api-app/test/timeline-fixtures.cjs:57). The final run completes far inside that ten-second offset, so receipt-time inbound messages are older than the entire burst. A broken paused-empty branch that retains its old cursor can load the remaining ten burst rows plus the two older inbound rows after Continue, still reach 162 IDs and unread=2, and never issue the required fresh-head read. The test counts only the initial three requests and never asserts that the first request after the between-round event has no antes cursor. It therefore does not discriminate the ARCH-DEL-02 regression or prove current metadata refresh in that path.
  - [medium] ARCH-DEL-03 [P2] Opening-race coverage omits reconnect while the initial response is held: web-app/e2e/timeline.spec.ts:56 proves a real inbound message during a held opening response, but not an onopen/reconnect callback in that same threadAtual-null state. src/tempoReal.spec.ts:25 uses a fake socket to prove callback emission, while the browser reconnect case at web-app/e2e/timeline.spec.ts:121 begins after opening has completed. A regression that suppresses or misroutes the reconnect callback only while invalidacaoAbertura is active would pass all supplied assertions, despite the approved requirement that reconnection recover without a further event or poll.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

