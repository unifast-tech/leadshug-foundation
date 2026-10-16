# CP26 Web regression handoff

CP26 Web work is complete and at STOP pending the canonical integrated run. API CP26 had already reached terminal STOP before this one-file Web change. No product source, helper, fixture, dependency, runtime, or other E2E file was changed.

Added one real-browser regression in `web-app/e2e/number-onboarding.spec.ts`: an owner reserves a new official channel, the exact-scoped expiry fixture expires the attempt, and the first UI is observed in its visible `A tentativa expirou` state before a second BrowserContext signs in as the same seeded owner. That separate session uses the normal UI and BFF to reserve `REAUTORIZAR` for the exact same BU/channel/generation, replacing the channel's `currentAttemptId` with a new `PENDING_AUTH/RESERVED` attempt.

The first session then clicks its stale recovery action. The test requires the authoritative refresh guard's exact safe mismatch error, the expired state to remain visible, no reservation button, and zero first-page reservation POSTs. BFF readback verifies the competitor attempt remains `PENDING_AUTH/RESERVED`, the one official channel retains the original ID and generation with the competitor as current attempt, and the BU count remains unchanged.

The test uses the existing dedicated expiry fixture endpoint and current 12-second bounded polling/visibility waits. It does not create fixture APIs or manipulate database state outside the authorized expiry control. The two existing positive recovery cases and baseline tests were left untouched.

Validation was intentionally not run in this Web lane. Static end-to-end review confirmed the existing button labels, real BFF route and `Idempotency-Key` requirement, `REAUTORIZAR` DTO fields (`buId`, `channelId`, `expectedGeneration`), owner grant on the newly created BU, and the current product guard's `currentAttemptId` predicate. DevOps owns the single canonical integrated `all` run after all workers STOP.

Final changed-source SHA-256: `web-app/e2e/number-onboarding.spec.ts` `47fdb27c0b592dfe8df31b8ad1be219d96720abdc00660bc15f6b2c03096f31b`.
