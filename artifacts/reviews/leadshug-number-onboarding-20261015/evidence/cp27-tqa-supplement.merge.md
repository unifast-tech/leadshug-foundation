# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/cp27-tqa-supplement.dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `none`

## Axis Summary
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Recommended Paths
- `Record the recommended local dispositions separately: TQA-CP25-01 resolved because the stale old-name ingress is now observed by a preinstalled realtime spy and remains zero through the pending negative before the verified current-key positive; TQA-CP25-02 resolved because a real second OWNER session supersedes the retained-slot attempt and the stale first page demonstrably fails safe without a reservation or state mutation. No further source edit, fixture expansion, rerun, or whole-feature audit is indicated by this supplemental review. Preserve the existing accepted performance/cutover/architecture positions on the unchanged manifest. Overall TODO status remains Pending: VAL-05 is mandatory and unwaived, is not accepted debt, and remains outside this strict local correction gate; the local fake-provider/browser evidence must not be promoted into a provider/device/platform completion claim.`

## Merged Findings
- `none`

## Reviewer Summaries
### native-gpt-5.6-terra-max-cp27-tqa-supplement
- **Assessment:** Strict local supplemental disposition: recommend TQA-CP25-01 and TQA-CP25-02 as resolved/Integrated for this correction gate, with no new material local finding. This is not count-only acceptance. Hashes recomputed from root-cp27-receipt.json matched all listed cp27 artifacts and both current test sources. Semantic manifest comparison found exactly 230 entries/228 unique paths, exactly two cp25→cp27 source-hash differences (api-app/test/number-onboarding-flow.e2e-spec.ts and web-app/e2e/number-onboarding.spec.ts), and no cp27 pre→post source difference; production paths remain unchanged. TQA-CP25-01 is now a discriminating REG-SEC-10 negative proof: api-app/test/number-onboarding-flow.e2e-spec.ts:712 installs the real DI-resolved RealtimeService spy before the stale old-instance webhook at :714, immediately asserts zero calls at :715, retains the current-name PENDING_IDENTITY negative at :736-742, then proves exactly one verified-current same-key publication at :751-758. The Nest app is constructed from AppModule with only external-provider tokens overridden, while RealtimeService is not overridden (test/helpers.ts:149-162); the actual stale ingress guard is evolution.controller.ts:31-37. Existing message/conversation/Typebot and current-identity assertions remain, cleanup restores the spy and held gates at :760-765, and there is no clear/reset that could erase the stale observation. TQA-CP25-02 is likewise effective rather than a projection-only repair: web-app/e2e/number-onboarding.spec.ts:178-243 uses a separately authenticated BrowserContext for the same MANTENEDORA-granted OWNER, drives actual UI/BFF REAUTORIZAR with exact BU/channel/generation assertions (:195-217), then proves the first browser receives the exact fail-safe mismatch alert, retains expiry, exposes no reservation control, sends zero first-page reservation POSTs, and leaves the competitor attempt/currentAttemptId, one official channel, and BU count intact (:222-240). This directly exercises CadastroNumero.tsx:521-555, especially its currentAttemptId/channel/generation guard at :539-544; the seeded OWNER grant is materially appropriate while direct ADMIN is only direct-BU-granted (timeline-fixtures.cjs:116-128). The correction contains no BFF mock, SQL shortcut, new fixture route, or product change; its only external seam is the pre-existing SDK/provider fixture, while browser requests traverse the built web app, session/CSRF BFF, Nest API, and disposable PostgreSQL. The expiry fixture is narrowly guarded and changes only an exact NOVO/PENDING_AUTH attempt plus BU (timeline-fixtures.cjs:208-217). Static scans of both changed tests and Playwright configuration found no focused/skipped/fixme/TODO bypass, test-only fallback, or new inline debt. These are correctly test-after proofs of already-correct behavior; no RED was fabricated. Retain TQA-CP21-02 as accepted mixed/test-after process debt, and carry the accepted D-01..D-10, REG-SEC-01..13, performance, cutover, and architecture judgments rather than reopening unchanged production. The cp27 local CI-equivalent evidence is sufficient for this gate: the recorded all run exercised the named API file and both first browser recovery cases; globalSetup freshness attestation predates browser workers and records disposable PostgreSQL, 22 migrations, API/fixture/preview health, and equal served/dist bundle hashes. It remains bounded local evidence, not real Meta OAuth, device QR, real per-channel IN/OUT, or recovery proof.
- **Recommended path:** `Record the recommended local dispositions separately: TQA-CP25-01 resolved because the stale old-name ingress is now observed by a preinstalled realtime spy and remains zero through the pending negative before the verified current-key positive; TQA-CP25-02 resolved because a real second OWNER session supersedes the retained-slot attempt and the stale first page demonstrably fails safe without a reservation or state mutation. No further source edit, fixture expansion, rerun, or whole-feature audit is indicated by this supplemental review. Preserve the existing accepted performance/cutover/architecture positions on the unchanged manifest. Overall TODO status remains Pending: VAL-05 is mandatory and unwaived, is not accepted debt, and remains outside this strict local correction gate; the local fake-provider/browser evidence must not be promoted into a provider/device/platform completion claim.`
- **Performance:** `acceptable`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `mixed`

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

