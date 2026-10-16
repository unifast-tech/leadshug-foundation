# cp26 API test-only handoff

Status: the authorized TQA-CP25-01 regression proof is added. No API test, build, runtime action, production change, or other source-path edit was performed in this activation. The coordinated all-499 canonical validation is intentionally pending the Web regression addition and DevOps run.

In `api-app/test/number-onboarding-flow.e2e-spec.ts`, the `RealtimeService.publicarNaBu` spy is now installed immediately before the old-instance stale `messages.upsert`. The test asserts zero realtime calls immediately after that request, then keeps the existing current-instance `PENDING_IDENTITY`/zero-call negative and the current-X same-key accepted path with exactly one realtime publication. The spy is restored from the existing `finally`, alongside release of both held operations and restoration of the Evolution fake method. No mock clear can erase the stale-event observation.

Static review confirms the test retains the old-verification 409, cleanup-stage transition, Y-owner quarantine, new-epoch old-WUID open invariants, no-content/Message/conversation/unread/Typebot/realtime effects before current X verification, and positive same-key retry after current X verification.

The targeted no-index whitespace check was run against the approved test file. It emitted no diagnostics and returned status 1 because the file is untracked relative to `/dev/null`; this is expected for the diff operation, not a test result. No canonical API run has been executed for cp26.

Before SHA-256: `40128cbe31499fa490430632367967d3b4a8851a7f53321ebf160dc69c533ff5`.
After SHA-256: `c1b8b03351179721a641d7139d46d7e93b45ae335ac5788cf5436fc35b69e280`.
