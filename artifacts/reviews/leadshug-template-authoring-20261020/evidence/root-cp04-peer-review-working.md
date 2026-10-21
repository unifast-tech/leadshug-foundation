# CP04 peer review — working ledger

Derived root-only working ledger; not an independent audit, final review or validation pass. Executor is the sole product writer and owns cp04* receipts. Sources are actively changing, so earlier observations are not assertions about final code. Every item below is already inside approved v1.1; no new functional scope is introduced.

CP04 first behavioral RED: direct domain call on real PG allowed an unknown list view instead of rejecting with Nest status400. Canonical api exit1, unit281 passed; disposable cleanup completed. Root directly verified retained log SHA256 `5cc996f8d7b68622565fef052cdb2bb10f78196268e59e92eefe8d652d83e92c` at `artifacts/tmp/stcon05-cp04-red-view-20261021T141500Z.log`. This is not a new BFF wire-contract proof. The main submit/recovery/observation block remains unvalidated at this ledger point.

| Item | Existing contract / concrete observation | Latest disposition; final verification still required |
| --- | --- | --- |
| R1 schema/SQL identity | Composite referenced draft index initially after FK; long manual PG names; missing Prisma reservation relation | Executor reports correcting order/relation and names; compare complete schema/SQL and actual migration proof. |
| R2 catalogue persistence | Remote observation initially lacked name/language and availability; empty/error page must be distinguished | Fields added/in progress; verify full projector and cached page error semantics, language35 parser agreement. |
| R3 idempotency | Draft+actor+key allowed reuse in another draft of same BU | BU+actor+key and draft-in-requestHash reported corrected; prove race/reuse/replay before provider. |
| R4 quota | Fixed bucket labelled sliding; actor admission rolled back on reservation conflict | Executor reports durable moving-window events, separate actor admission, advisory lock plus DB clock after lock. Verify actual60s/1h boundary, shared accounts, negative auth and free replays. |
| R5 final dispatch guard | CP03 lacked a local fence after a held grant | CP04 adds guarded create; prove actor/session/grant/context/credential/claim/lease changes yield0POST, no fourth provider method. |
| R6 commit certainty | Initial reservation readback discarded; release blanket error; accepted readback too weak | Executor repairing four boundaries; real rollback/real commit-then-error with exact captured readback≤3queries, fixed known-ACK error and no compensation/repost still required. |
| R7 administrative reads | Initial getOperation filtered actor=current user and blocked admin of same authorized draft | Keep owner/admin policy for resource access, original actor identity for replay-key scope; verify final behavior. |
| R8 locked/new key | Initial path returned revision conflict only | Require safe RECOVERY_REQUIRED and same authorized operation; draft GET reload without browser key. |
| R9 late result | Initial record-outcome allowed only SENDING | Monotonic same-op/same-claim late ACK after expiry/recovery, no overwrite of newer observation or another operation. |
| R10 provenance | Initial phaseACCEPTED automatically meant providerAcceptanceCONFIRMED | Explicit ACKNOWLEDGED versus CORRELATED_BY_DEFINITION added; verify no claim of creation/authorship/examples from correlation. |
| R11 receipts/teardown | Append-only receipt trigger rejects deleteMany | Executor reports explicit disposable05 TRUNCATE teardown; prove UPDATE/DELETE protection and preserve normal production invariants. New migrations have5s/60s transactional bounds. |
| R12 DI | Optional injected-boundary fallback was shaped for old fixtures | Require explicit production DI binding; fixtures adapt, no silent fake-store or missing-provider fallback. |
| R13 observation fence | Catalogue and individual must have same owner/projector/fence | Full bidirectional held-response+expiry/newPAUSED, oldsuccess/error/release loses all writes; clock DI, current context and300s eligibility still required. |
| R14 bounded history | Latest10receipt events alone do not supply recent draft operations | Detail current+last10ops and bounded receipt projection; list current summary only. Observe actual SQL, no fetch-all then truncate. |
| R15 mutation assertions | Early RED used temporary method cast/call and combined URL counts | Replace with typed service calls and hard-fail fake for unexpected URL/method; exact grant/GET/POST counts plus independent PG rows. |
| R16 proven refusal | Intermediate release conditioned on !dispatched would retain name after provenNoCreation POST refusal | Executor reports already corrected to unconditional CAS release for proven REJECTED, strengthened PG receipt sequence/reservation test. Not yet executed. |

Mechanical intermediate source issues (undefined locals, duplicated authorization, Nest429 import and PG void advisory return) were reported by root and executor reports correcting them before the next runner. They are not behavioural RED or passing-build evidence.

After a stable checkpoint: re-read actual sources, migration and tests, verify retained final logs/source hashes/30sealed/3HEADs, and record a terminal disposition. Only then advance to the Web checkpoint. Complete canonical all, full independent gates and assisted real template proof remain later requirements.

## Later pre-runner snapshot — observation/BFF

R17 (CR-V11-01 concrete race): initial ownsLease uses a nonlocking SELECT, then upserts and ignores release update count. A different owner can win between read and write. Require real lease lock/CAS before writes plus current context pinned/atomically verified to commit, full rollback on lost fence, and a real PG pause AFTER ownership check/before upsert in addition to held HTTP tests. Acquire debounce also needs lastStartedAt in atomic WHERE; calculating it from an old read allows an intervening release to evade debounce. One private write projector should serve both endpoints. Catalogue page availability must age at300s. Admin refresh must access vendor operation by authorized draft policy. Uncertain observation commit requires bounded readback, not compensation marking provider unavailable.

R18 (BFF draft snapshot, not final): submit referenced res without injected response, refresh POST defaulted201, submit replay defaulted201. Check actual HTTP200/201/202 contract. Strict runtime string checks needed for query.after/fingerprint; String(array) must not pass validation then crash. Refresh/reconcile body should reject unknown keys. Do not pass fictional expectedGeneration1 if service derives current metadata. Mechanical failures are not behavioural RED.

Executor subsequently reports R9 separated dispatch versus recovery lease owners; old GET checks recovery owner/live lease/phase/version, known original ACK can improve the same operation without clearing another owner's lease. Held-ACK/GET fixture authored, not yet run. R16 proven-refusal PG assertion strengthened, also not yet run. Independent recheck and terminal logs remain pending.

## Latest pre-runner residuals

R19: observation apply/page catches still rethrow a generic persistence error when the bounded readback returns false. The enclosing provider catch then attempts markUnavailable, conflating local uncertainty with an external failure. Require a local-incomplete result for both failed and negative readbacks, with no compensating write or repeated HTTP. Readback must also positively establish the release state. Acquisition uncertainty must dispatch no provider request.

R20: known-ACK local-incomplete response still omits the authorized operationId and approved fixed recovery text. Locked/new-key and prior-revision paths still restrict operation lookup to the current actor, despite owner/admin authorization to the vendor's draft. Preserve original actor identity for idempotency, while exposing the same scoped operation for authorized recovery. Sent to executor before canonical API validation; not yet verified.
