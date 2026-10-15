# PACED Subagent Review Merge: test_quality_audit

## Merge Identity
- **Artifact kind:** `subagent_review_merge`
- **Authoritative:** `false`
- **Edit policy:** `derived_merge_packet`
- **Dispatch path:** `/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/tmp/inbox-timeline-execution/delivery-tqa-resolution-dispatch.json`
- **Review count:** `1`
- **Highest finding severity:** `medium`

## Axis Summary
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `acceptable`

## Recommended Paths
- `Repair only the reconnect test sequencing; no product redesign or renewed approval is warranted. Rerun the targeted opening and empty scenarios, the full project-owned Web unit/browser suite, and the required FRC repetitions against a fresh manifest and served-bundle attestation. Preserve the unchanged API, EPS, BCI, and RLS evidence while source identity remains established. Then request a bounded TQA resolution review; do not mark the delivery review gates complete until this remaining evidence gap is closed.`

## Merged Findings
### F-1BACEEF7 [medium] [P2] Held-opening reconnect coverage does not isolate the reconnect callback as the recovery trigger
- **Reviewers:** delivery-tqa-resolution-native-no-context
- **Category:** `tests`
- **Formalizable hint:** `yes`
- **Candidate rule level:** `project`
- **Candidate rule id:** `timeline-opening-reconnect-must-trigger-recovery`
- **Suggested action:** A (recommended): before selecting the conversation, require the first authenticated socket frame so its onopen has run while no conversation is opening. Then hold the actual initial GET, persist the silent DB growth, close that established native socket, require the second authenticated frame, and only then release the response; retain the no-event/no-poll, read-neutral no-antes, full-ID, and unread assertions. Add a focused negative control that suppresses only the reconnect callback and must fail. B: use equivalent real-socket instrumentation that records the callback phase without replacing transport behavior. C: retain the current sequencing, which leaves reconnect-specific routing regressions able to pass.
- **Rationale:** The revision5 scenario starts the held opening before it proves that the initial socket's authenticated connection/onopen has completed; it waits only for sockets.length===1 after opening is already pending. Therefore the first onopen can occur while threadAtual is null and increment invalidacaoAbertura. Concrete counterexample: a regression suppresses the callback only on a subsequent reconnect, while the first connection opens during the held request. The test still observes a second authenticated server frame, then recovery after release caused by the first opening callback, so its read-neutral request and ID assertions pass. This proves that a reconnect coexisted with recovery, but not that the reconnect-onopen caused recovery in the required opening-generation state. This is the remaining unresolved ARCH-DEL-03 evidence gap; it does not reopen the resolved implementation finding.

## Reviewer Summaries
### delivery-tqa-resolution-native-no-context
- **Assessment:** Return for one focused browser-evidence repair. ARCH-DEL-02-EVID is resolved: the backlog predates both inbound events, the first authorized resume is required to be read-neutral and cursorless, current metadata is checked, and the retained-old-cursor mutation fails with exact restoration. ARCH-DEL-04 remains adequately protected by recovery-error disappearance assertions and the distinct newer-send-error preservation case. TQA-TL-01, TQA-TL-02, and TQA-EVID-03 remain resolved through direct budget/single-flight checks, six destination-context cases, and retained API command output.

Test effectiveness is otherwise strong but mixed because the new opening-reconnect scenario has the causal gap above. Test efficiency is acceptable: it uses project-owned commands, real Nest/session/grant/PostgreSQL/WebSocket paths, owned fixtures, held real BFF responses, and targeted repetition without a fabricated BFF payload, skip/focus marker, or production test hook. Test-after status is stated honestly; the retained mutation controls materially discriminate the empty-cursor, budget, cursor-restart, and ACK protections.

Performance evidence is mixed but candid: EPS documents the deep 10,001-row residual and rejects a worse measured index candidate, while BCI and RLS substantiate bounded local concurrency/read-neutral claims without asserting production capacity. The React owner, recovery-error ownership, DI topology, fresh served-bundle provenance, and source-invariant API reuse are structurally and operationally appropriate on the embedded evidence.
- **Recommended path:** `Repair only the reconnect test sequencing; no product redesign or renewed approval is warranted. Rerun the targeted opening and empty scenarios, the full project-owned Web unit/browser suite, and the required FRC repetitions against a fresh manifest and served-bundle attestation. Preserve the unchanged API, EPS, BCI, and RLS evidence while source identity remains established. Then request a bounded TQA resolution review; do not mark the delivery review gates complete until this remaining evidence gap is closed.`
- **Performance:** `mixed`
- **Elegance:** `acceptable`
- **Structural soundness:** `acceptable`
- **Operational fit:** `acceptable`
- **Findings:**
  - [medium] ARCH-DEL-03-EVID [P2] Held-opening reconnect coverage does not isolate the reconnect callback as the recovery trigger: The revision5 scenario starts the held opening before it proves that the initial socket's authenticated connection/onopen has completed; it waits only for sockets.length===1 after opening is already pending. Therefore the first onopen can occur while threadAtual is null and increment invalidacaoAbertura. Concrete counterexample: a regression suppresses the callback only on a subsequent reconnect, while the first connection opens during the held request. The test still observes a second authenticated server frame, then recovery after release caused by the first opening callback, so its read-neutral request and ID assertions pass. This proves that a reconnect coexisted with recovery, but not that the reconnect-onopen caused recovery in the required opening-generation state. This is the remaining unresolved ARCH-DEL-03 evidence gap; it does not reopen the resolved implementation finding.

## Exact Next Step
Record reviewer resolutions in the governing TODO using the machine-checkable resolution table or equivalent gate ledger, then extract the derived resolution packet and decide whether another bounded review pass is still required.

