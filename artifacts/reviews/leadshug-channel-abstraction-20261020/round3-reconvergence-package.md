# ST-CON-06 — round3 bounded remediation reconvergence

Derived, self-contained, fresh internal no-context architecture/security review; no tools/edits. Review current remediation delta against the COMPLETE frozen D01..10 rubric and scope. Code-gate only: finalall65587 is running; dedicated Performance/TQA/Cutover, PCV, local activation/assistedINOUT and finalreview remain pending and prevent delivery. These declared not-yet-complete gates are not claimed as passed by this package.

## Authority / frozen boundary

User explicitly APROVADO v1.2; two testcompanion paths were subsequently explicitly admitted. Main checkout/singleproductwriter; no private dotenv or protected data discovery/read/stat/hash/mount/stage. Source heads and exact dirty source hashes in manifest below. No schema/network/intent/template/outbox/retry/lifecycle rewrite/codepush/deployment. Small future capability ports remain successor work. Registry fake is internal substitution, not a new network schema. MessageAcceptance and the shipping adapter/Inbox guards were restored byte-exact after disposable fault injection.

## Full mandate and prior rounds

Assess D01..10 correctness/adherence, architecture/extensibility, authz/tenant/credential trust, postdispatch uncertainty, sender/echo/assignment invariants, DI and all producer/consumer contracts. Explicit performance/elegance/structural/operational positions. Detect concrete brittle workaround, parallel writer/dispatch/fallback/rebinding, unsupported assertions or changedconsumer omission; do not redesign unrelated approved scope. This is a four-product-file delta over the round2 snapshot. Full prior rawfindings/adjudications and unchanged critical contexts are embedded. Do not reopen resolved historical findings without a current changedlocus/newregression; do not ignore new concrete defects in changedloci.

## What changed and actual evidence

R05: Meta positive ACK and ACK-without-ID now require absent/boolean success indicator without explicitfalse. Malformed/contradictory indicators stay TRANSPORT_UNCONFIRMED; preserve valid normal ACK and stableGraph refusals. Actual canonical API49493 RED preceded production fix: expectedUNKNOWN for200success:false+ID, actualACCEPTED; no complete rawlog fromstart was retained, so this is executor-reported toolresult, not fabricated rawstdout. API54152 afterfix PASSED194unit/309realPG. New PG case uses production MetaHttpClient/factory, fetchdouble and realBFF/PG: bothfalse-success envelopes yieldUNKNOWN, exactlyonePOST/invocation and zeroOUT.

R04: self-guarding FencedDispatch testfake removed. Mutating testfactories delegate to REAL Meta/Evolution factories and wrap their actual predispatch callbacks with PG mutation. Meta testsgen/epoch/version; Evolutiongen/epoch (no per-channel officialcredentialversion exists forEvolution). Real callbacks/predicate/outbound response/zero client calls/zeroOUT are asserted. Separate shippingguard mutants were executed through canonicalapi: Meta16223 andEvolution59583 eachunit194pass/E2E308pass1expectedfail (409expected,201actual). Root independently observed exactoneguardremoval source whileeachrun active; closedlogs independentlyhashed; bothmodules restored exactreviewed hashes. Evidence below. No human runtime/provider was touched.

R02: uniqueactiveB/A headers and properstatus-tabnavigation retained. New same-textdraft is insertedafterreturningA. Testawaits heldPOST response bodyfinished (null asserted), then two browseranimationframes before draft/noalert assertions; no arbitrarysleep or producttestendpoint/field. Browserdiagnostic2225 PASSED50/50 before the extra nullresultassertion. Intentional removal of respondergen/idguard then canonicalbrowser97398 FAILED49pass1targetfail: newdraftempty. This browserfailure is executor-reported toolresult/excerpt, no independentmutantsource snapshot/fullrawlog retained; root independently confirmed restoredInboxhash. Last extra nullassertion is testonly and awaiting finalall65587. Be explicit about evidenceprovenance; no broadfailfirst history is invented.

All65587 is currently running on restoredfrozen source with fullstdout/stderr capture. Earlierall33610 passed194unit/308PG/29Web/50browser, but is earliercandidate and cannot substitute finalvalidation. No source edit allowedduring currentall. InitialdependencyguardRED175pass1fail is narrow; earlierclassifiers/matrices were testafter. Preserved limits: localcheck/network race, observationalavailability, knownACKnotdelivery, no crash recovery/durableintent/null-ID dedupe/externalexactlyonce, latestINstoredtime/no transportfilter. HistoricalCP108 is not currentphysicalproof.


## Exact frozen source manifest

```json
{
  "captured_at_utc": "2026-10-20T15:57:31.006071+00:00",
  "status": "candidate source frozen, captured near start of finalall65587; no testpass claimed",
  "heads": {
    "root": "80e3940126f22a941f90dba4f5e801b6c0eb2f58",
    "api": "db5a86758a165fac8a1ab587599c37b17890530c",
    "web": "74b9d4b714044829796f875d00553f077c1c329d",
    "foundation": "f810cae988bb47c44870d2324036dca72812a33d"
  },
  "scope": "Exact44 reviewed public source/context paths, not a whole API tree/private-data inventory. Sourcefile hashes, not dirty HEADs, identify candidate. Root runner included; full build/freshness inventory remains runner/executor evidence.",
  "records": [
    {
      "path": "api-app/package.json",
      "bytes": 1670,
      "sha256": "df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d",
      "round2_sha256": "df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d"
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.ts",
      "bytes": 5053,
      "sha256": "89cf17ac02af444092651470aee13e2d4a3bcee8d459508be818322b33b00c10",
      "round2_sha256": "89cf17ac02af444092651470aee13e2d4a3bcee8d459508be818322b33b00c10"
    },
    {
      "path": "api-app/src/domain/channels/transport/channel-dependencies.spec.ts",
      "bytes": 2383,
      "sha256": "f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3",
      "round2_sha256": "f59d838baf635c0ce0d1ebe725c88fbb0b19fac42e9b382452e31fd38e0511a3"
    },
    {
      "path": "api-app/src/domain/channels/transport/channel.ts",
      "bytes": 2678,
      "sha256": "432796b8685d07dcc53c3a699a7b9d1469ac4fb110aea080766ec207bec8621f",
      "round2_sha256": "432796b8685d07dcc53c3a699a7b9d1469ac4fb110aea080766ec207bec8621f"
    },
    {
      "path": "api-app/src/domain/inbox/conversations.service.ts",
      "bytes": 8137,
      "sha256": "c7d84f983ed61c6022424d4648e07282e7eb53c40fa9aba249618d77b3c223de",
      "round2_sha256": "c7d84f983ed61c6022424d4648e07282e7eb53c40fa9aba249618d77b3c223de"
    },
    {
      "path": "api-app/src/domain/inbox/incoming.service.ts",
      "bytes": 6076,
      "sha256": "b0ec43187b1f48720aa899e40f979dd0ae447321581d675b84ef9c71dbd0ff42",
      "round2_sha256": "b0ec43187b1f48720aa899e40f979dd0ae447321581d675b84ef9c71dbd0ff42"
    },
    {
      "path": "api-app/src/domain/inbox/incoming.typebot.integration.spec.ts",
      "bytes": 4647,
      "sha256": "0cac10e5ed05da5a6e89b39c8b32a40810b4678af77b4d3b8d20b4d1afc4704c",
      "round2_sha256": "0cac10e5ed05da5a6e89b39c8b32a40810b4678af77b4d3b8d20b4d1afc4704c"
    },
    {
      "path": "api-app/src/domain/inbox/message-acceptance.service.ts",
      "bytes": 15730,
      "sha256": "b053744ee44b7e91fd45b5c146f759f55c70b8e517b8fbb1cab39806407335e1",
      "round2_sha256": "b053744ee44b7e91fd45b5c146f759f55c70b8e517b8fbb1cab39806407335e1"
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.spec.ts",
      "bytes": 8314,
      "sha256": "ae1f9208d660c684dca9b1ac5727001d8e57c4c9504be9be1d20ecba32e01805",
      "round2_sha256": "ae1f9208d660c684dca9b1ac5727001d8e57c4c9504be9be1d20ecba32e01805"
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.ts",
      "bytes": 13056,
      "sha256": "63bcf773e2b4c5a5ddd688a1bb13745a0a206d995fafc665925df3fecaf394aa",
      "round2_sha256": "63bcf773e2b4c5a5ddd688a1bb13745a0a206d995fafc665925df3fecaf394aa"
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-factory.ts",
      "bytes": 440,
      "sha256": "e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc",
      "round2_sha256": "e0ebdd78e387f7ee3af902f038d22449e212c1301ffa642bbceb5a5f05d2abfc"
    },
    {
      "path": "api-app/src/integrations/channels/channel-adapter-registry.ts",
      "bytes": 975,
      "sha256": "655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b",
      "round2_sha256": "655b735e239e89fbaede36689d1c22245d3804d66646f7736db991cb5099b02b"
    },
    {
      "path": "api-app/src/integrations/channels/channel-transport.module.ts",
      "bytes": 1663,
      "sha256": "32203d3b8393a34a9effab4266683c389651d7ec197e8f9d704a77a6a37f40dc",
      "round2_sha256": "32203d3b8393a34a9effab4266683c389651d7ec197e8f9d704a77a6a37f40dc"
    },
    {
      "path": "api-app/src/integrations/channels/evolution-channel.ts",
      "bytes": 1561,
      "sha256": "60faf1ea40fe17ad62495b0f42a2cf958defcb41e3ad72d3d2213751539b460c",
      "round2_sha256": "60faf1ea40fe17ad62495b0f42a2cf958defcb41e3ad72d3d2213751539b460c"
    },
    {
      "path": "api-app/src/integrations/channels/meta-channel.ts",
      "bytes": 1613,
      "sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138",
      "round2_sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138"
    },
    {
      "path": "api-app/src/integrations/channels/prisma-channel-resolver.ts",
      "bytes": 18831,
      "sha256": "5d01cca30f25ea4354651303633aa5a02f3adbe0b7cc37c44c53d821fe7c062f",
      "round2_sha256": "5d01cca30f25ea4354651303633aa5a02f3adbe0b7cc37c44c53d821fe7c062f"
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.spec.ts",
      "bytes": 6530,
      "sha256": "119d962fdcd9c895b75845dca74d8506147e11480d74b82e8c37f29f97c04081",
      "round2_sha256": "119d962fdcd9c895b75845dca74d8506147e11480d74b82e8c37f29f97c04081"
    },
    {
      "path": "api-app/src/integrations/evolution/evolution.client.ts",
      "bytes": 7214,
      "sha256": "b0824e8fd4f801a239521855aaa02da5e0943a8c86c4ac8778e2f1f352821698",
      "round2_sha256": "b0824e8fd4f801a239521855aaa02da5e0943a8c86c4ac8778e2f1f352821698"
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.spec.ts",
      "bytes": 38572,
      "sha256": "d7e76f5c392afab1638363d3c851f8ce8c5223ff27c64801a79fdc8ec00d5e7a",
      "round2_sha256": "adc65f436e5164af64a8c98de0d392e033c2380cd4d2b9bea462faedfc0d210a"
    },
    {
      "path": "api-app/src/integrations/meta/meta.client.ts",
      "bytes": 17388,
      "sha256": "9f954f6c1c2bd10030f5eed0cb42e493d6e480106bcfc3f44977cb97a716d34f",
      "round2_sha256": "c5277e59ed12f3da70a5f3143499ce2884a3a23691acff5c58db87a513a37bb7"
    },
    {
      "path": "api-app/src/surfaces/bff/bff.module.ts",
      "bytes": 4917,
      "sha256": "327f34eba67746882abc601a3817d94270cff3018d6972a8095dae530a2d6e29",
      "round2_sha256": "327f34eba67746882abc601a3817d94270cff3018d6972a8095dae530a2d6e29"
    },
    {
      "path": "api-app/src/surfaces/bff/conversations.controller.ts",
      "bytes": 5626,
      "sha256": "53d3cffaa258ba1ad45c21eae4ab8712e2011255b7ca14965f73221edd0cc002",
      "round2_sha256": "53d3cffaa258ba1ad45c21eae4ab8712e2011255b7ca14965f73221edd0cc002"
    },
    {
      "path": "api-app/src/surfaces/public/conversations.controller.ts",
      "bytes": 9783,
      "sha256": "b55440061dd4574646e4fa1a3c265cdb8653bab4abf3aa0e86b4057bc7e365ff",
      "round2_sha256": "b55440061dd4574646e4fa1a3c265cdb8653bab4abf3aa0e86b4057bc7e365ff"
    },
    {
      "path": "api-app/src/surfaces/public/public.module.ts",
      "bytes": 1208,
      "sha256": "00a96d54fde7061f61f4ddf2b9cef836a02ad77ca29b62ea422695b9d8f90ef8",
      "round2_sha256": "00a96d54fde7061f61f4ddf2b9cef836a02ad77ca29b62ea422695b9d8f90ef8"
    },
    {
      "path": "api-app/src/surfaces/webhooks/webhooks.module.ts",
      "bytes": 1111,
      "sha256": "abc8fd7960fcca1ce43d21d44a90f8d4708d47e07bde9a48c0009e02dc0503a6",
      "round2_sha256": "abc8fd7960fcca1ce43d21d44a90f8d4708d47e07bde9a48c0009e02dc0503a6"
    },
    {
      "path": "api-app/test/api-publica.e2e-spec.ts",
      "bytes": 14387,
      "sha256": "4ce7360eb02621f89d25d41924bfafb86b76e8bbec8216dfb509f86000308837",
      "round2_sha256": "4ce7360eb02621f89d25d41924bfafb86b76e8bbec8216dfb509f86000308837"
    },
    {
      "path": "api-app/test/browser-server.cjs",
      "bytes": 11647,
      "sha256": "40e56e2d6672800acd4a00f87b942fc88b8361c770d06ee6d7c8a883a15d3390",
      "round2_sha256": "40e56e2d6672800acd4a00f87b942fc88b8361c770d06ee6d7c8a883a15d3390"
    },
    {
      "path": "api-app/test/channel-transport.e2e-spec.ts",
      "bytes": 34003,
      "sha256": "124d397bd3a5769271466e64b0e19b1235e08d1ea9a4df9f124fc629096822fe",
      "round2_sha256": "ce8bf7e6a6145bf5ca417becbd2c706728342bd8e7f71d1dfdc609bbfefb71df"
    },
    {
      "path": "api-app/test/helpers.ts",
      "bytes": 18367,
      "sha256": "747dcd1a6db374c1ccb0f2a248b08d49c2ec62a46beb345cc03eea3c058d36f2",
      "round2_sha256": "747dcd1a6db374c1ccb0f2a248b08d49c2ec62a46beb345cc03eea3c058d36f2"
    },
    {
      "path": "api-app/test/number-onboarding-pcv.e2e-spec.ts",
      "bytes": 16149,
      "sha256": "c62a11fc6302cd3bb807ff0b55b9dbcc7e46847cef638b81c382b455a8a29f20",
      "round2_sha256": "c62a11fc6302cd3bb807ff0b55b9dbcc7e46847cef638b81c382b455a8a29f20"
    },
    {
      "path": "api-app/test/number-onboarding-typebot.e2e-spec.ts",
      "bytes": 17679,
      "sha256": "22e1121d8a1f03b5e566fb8e314c3966e5d9355453b31b978afcd30de038fbd2",
      "round2_sha256": "22e1121d8a1f03b5e566fb8e314c3966e5d9355453b31b978afcd30de038fbd2"
    },
    {
      "path": "api-app/test/timeline-fixtures.cjs",
      "bytes": 24711,
      "sha256": "889707ec7857e8a17a850e56eb60d24e6953e59028f40880edff3756340fd23a",
      "round2_sha256": "889707ec7857e8a17a850e56eb60d24e6953e59028f40880edff3756340fd23a"
    },
    {
      "path": "web-app/e2e/channel-transport.spec.ts",
      "bytes": 9772,
      "sha256": "956058444775e1383324012236029f5a803d4730c9fac9c881e870c3a3825293",
      "round2_sha256": "24f1770fedeeb0fa9e58bc7a639f986cbead0890a6215dd8801a9c16e4a360ad"
    },
    {
      "path": "web-app/e2e/number-onboarding-freshness.ts",
      "bytes": 5059,
      "sha256": "880b49f8fa428568692b92a883dd00c5ce76214b1f2db5b35cafb9b0553ed9ad",
      "round2_sha256": "880b49f8fa428568692b92a883dd00c5ce76214b1f2db5b35cafb9b0553ed9ad"
    },
    {
      "path": "web-app/e2e/timeline-freshness.ts",
      "bytes": 8499,
      "sha256": "3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53",
      "round2_sha256": "3a06fb36e3a9bcf20a12cd8201da2daa3b567775f15e2be5f068e97e840d7f53"
    },
    {
      "path": "web-app/package.json",
      "bytes": 701,
      "sha256": "fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de",
      "round2_sha256": "fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de"
    },
    {
      "path": "web-app/src/api.spec.ts",
      "bytes": 6256,
      "sha256": "e305671fc6d9775ef3c0365ed12470fb14ea3dd71ff3aca49f153262017147d6",
      "round2_sha256": "e305671fc6d9775ef3c0365ed12470fb14ea3dd71ff3aca49f153262017147d6"
    },
    {
      "path": "web-app/src/api.ts",
      "bytes": 10385,
      "sha256": "dd59a37799453d3e68fc64a6477e1578956d15d1a4920af90e22ff2b83057505",
      "round2_sha256": "dd59a37799453d3e68fc64a6477e1578956d15d1a4920af90e22ff2b83057505"
    },
    {
      "path": "web-app/src/telas/Inbox.tsx",
      "bytes": 21225,
      "sha256": "d70bde9ede67759d479f644598356e46aac2916a12b2ed1770c17a169118586c",
      "round2_sha256": "d70bde9ede67759d479f644598356e46aac2916a12b2ed1770c17a169118586c"
    },
    {
      "path": "scripts/test-channels-local.sh",
      "bytes": 9873,
      "sha256": "b03176ef1a332c431ed55028c691052958ebc08ff7711db08d05316c1f8a34a6",
      "round2_sha256": "b03176ef1a332c431ed55028c691052958ebc08ff7711db08d05316c1f8a34a6"
    },
    {
      "path": "foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md",
      "bytes": 92833,
      "sha256": "b33eff13ac6f4fe7f07c853ff366f1abf869fdef84626543215d6ca22a485f76",
      "round2_sha256": "6ccfb59cff3a427532c4b249c55e85250dec60d8975974985ac5725b68667224"
    },
    {
      "path": "foundation_documentation/modules/inbox-and-conversations.md",
      "bytes": 12425,
      "sha256": "b9d2d151cceb2758e381c6787b8c4baf4e26630d88c62057ecfbc24e0dd26a72",
      "round2_sha256": "b9d2d151cceb2758e381c6787b8c4baf4e26630d88c62057ecfbc24e0dd26a72"
    },
    {
      "path": "foundation_documentation/modules/integrations-and-channels.md",
      "bytes": 31617,
      "sha256": "031fab31685d00d635794aa10d0b1b8ee0a830e54b32622958b6bdc3e079853d",
      "round2_sha256": "031fab31685d00d635794aa10d0b1b8ee0a830e54b32622958b6bdc3e079853d"
    },
    {
      "path": "foundation_documentation/project_constitution.md",
      "bytes": 4641,
      "sha256": "abfafa5576d051da58583e2be57499320c8ad155c4ae741f259c730bcca98390",
      "round2_sha256": "abfafa5576d051da58583e2be57499320c8ad155c4ae741f259c730bcca98390"
    }
  ],
  "changed_paths_since_round2": [
    "api-app/src/integrations/meta/meta.client.spec.ts",
    "api-app/src/integrations/meta/meta.client.ts",
    "api-app/test/channel-transport.e2e-spec.ts",
    "web-app/e2e/channel-transport.spec.ts",
    "foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md"
  ]
}
```

## Prior disposition / evidence implementation-round-1-resolution.md

# ST-CON-06 — implementation review round 1 adjudication

Derived from terminal canonical CLI reviews gpt-6.1-sol/xhigh; both raw JSONs strictly validated and merged. Frozen packet architecture hash18295b2f… /security64b54684…; no live reviewer cancelled, replaced or repackaged. These are independent architecture and separate security gates, not the dedicated Performance/TQA/Cutover session or final review. Final all ended with API/Web green and browser48/50; it does not satisfy the delivery gate.

| Deduplicated ID | Original findings | Severity | Classification | Decision / exact current-slice action | State |
|---|---|---|---|---|---|
| ST06-R01 | ADH-01, SEC-01 | high | release-blocker | Integrated D04: inspect complete single-send Meta acknowledgement envelope; non-first ID, malformed entries/IDs or other success contradiction remain UNKNOWN/TRANSPORT_UNCONFIRMED, one POST, no ambiguous diagnostic. Preserve documented stable refusal allowlist. | open, executor remediation |
| ST06-R02 | ADH-02 | medium | release-blocker | Integrated D10: keep return-navigation target reachable in correct status tab, verify unique active B/A thread and preserve a newly entered draft after stale completion. Correct test mechanics, not product assignment semantics. | open, executor remediation |
| ST06-R03 | SEC-02 | medium | release-blocker | Integrated D04/05: successful HTTP empty object lacks Evolution acknowledgement structure and must be TRANSPORT_UNCONFIRMED/no diagnostic; preserve key:{} as approved ACK-without-ID. Add exact raw evidence and local-effect assertions. | open, executor remediation |
| ST06-R04 | SEC-03 | medium | release-blocker | Integrated D02/03/security simulation evidence: cite existing candidate-bound denied mutations or add admitted local tests for no grant/CSRF, foreign API-key account, after-binding pre-dispatch version/generation/epoch changes, and overlapping distinct tenant token/resource pairing. Zero provider effects on blocked paths; preserve post-dispatch version-only success. | open, source/evidence reconciliation then necessary probes |

None changes Scope/DoD/frozen decisions or warrants new architecture/product approval. They are approved-contract compliance, not a mandate to expand Channel, schema, lifecycle, templates, networks or intent. Security observations remain source-only counterexamples/evidence gaps until local regression probes reproduce and verify them; no tenant breakout or credential disclosure was demonstrated.

Separate implementation-check finding caught during browser remediation: do not add Message.status to production timeline DTO just to observe a test diagnostic. D10 preserves message DTO, availability/outcomes are the authorized additions. Executor instructed to restore that extra selection/type/UI and use a seeded-conversation-only fixture audit readback on private validation port3101. This is not a production test endpoint. Unknown ACK may legitimately show a FALHOU diagnostic after normal refresh; zero visible bubbles is not the required invariant.

Follow-up review uses delta plus this prior adjudication after terminal remediation and actual validation; no narrowing of required rubric. No accepted-debt or waiver is recorded. Preserve unchanged MessageAcceptance and all canonical fences.


## Prior disposition / evidence implementation-round-2-resolution.md

# ST-CON-06 — implementation review round2 adjudication

Terminal canonical fresh CLI reviews, gpt-6.1-sol/xhigh, source snapshot `evidence/reconvergence-source.json`; both results strictly merged. Packages1641ec21…/a73b3eb0…; one turn.completed and zero tool items each. No running review was replaced or repackaged. This is code/security reconvergence, not dedicated audit or final review. Canonical all33610 is still running on these bytes; no source edit is permitted during it. Even a green result will not close the findings below.

Original round1 counterexamples for non-first/malformed Meta IDs and Evolution2xx{} are corrected according to both reviewers. B/A target reachability, unique active-thread checks and same-text replacement draft are now present. Negative session/CSRF/public-key probes and distinct-tenant concurrent token/resource proof are also present. These are substantive partial resolutions; the remaining defects cannot be closed by citing those successes.

| Stable finding | Exact review binding | Classification | Current action / scope | State |
|---|---|---|---|---|
| ST06-R01 | round1 ADH-01/SEC-01 | release-blocker, resolved original counterexample | Full single-send envelope prevents non-first/malformed-ID refusal; raw cases and API194/308 pass reported. New success-flag case is tracked separately below | resolved in reviewed snapshot; final validation still required |
| ST06-R03 | round1 SEC-02 | release-blocker, resolved original counterexample | Evolution2xx{} remains TRANSPORT_UNCONFIRMED; supported key:{} remains ACK_WITHOUT_ID | resolved in reviewed snapshot; final validation still required |
| ST06-R05 | adherence-round2 ADH-R2-01 | release-blocker, medium | Meta200 success:false plus validID currently ACCEPTED; same flag with messages:[{}] produces ACK_WITHOUT_ID. Validate contradictory/malformed success indicators before positive acknowledgement; exact raw regressions onePOST, no local acceptance/diagnostic for unconfirmed outcome | open; executor after current runner terminal |
| ST06-R02 | adherence-round2 ADH-R2-02; security-round2 ADH-R2-02 | release-blocker, medium | Response headers event alone can precede api.ts body/Inbox continuation. Deterministic full consumption/handler completion and fault-injection proof that removal of generation fence fails the same-text-draft scenario; no arbitrary sleep or production test fields/routes | open; navigation fix retained, protection proof incomplete |
| ST06-R04 | adherence-round2 ADH-R2-03; security-round2 ADH-R2-01 | release-blocker, medium | Current pre-dispatch fake itself invokes stillCurrent, so it cannot detect shipping adapter bypass. Delegate to real Meta/Evolution factories and wrap their actual callback to change disposable binding after resolution; assert BLOCKED, zero provider calls and zeroOUT; removing the shipping callback must fail the probe | open; other SEC03 proof retained |

Review IDs overlap between the two raw JSONs. The reviewer artifact prefix above is part of their identity; security-round2 ADH-R2-01 is the adapter protection gap, not the Meta success-flag issue.

All remaining findings are within D03/D04/D10 and the admitted test paths. No schema, port capability, lifecycle, new network, first-send/template, durable intent or user-contract expansion is warranted. No waiver or accepted debt is granted. Fault injection is disposable-validation evidence only; restore exact approved source before final all/review/runtime. Record actual RED honestly; prior classifier/harness changes remain test-after historically.

Next: let all33610 reach terminal without edits, capture its actual result, then sole writer completes these three bounded corrections/protection probes. Freeze revised bytes and collect candidate-bound canonical validation plus fresh focused review carrying forward both rounds' complete adjudications. Dedicated Performance/TQA/Cutover and operator proof remain separate pending gates.


## Prior disposition / evidence evidence/adherence.raw.json

{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/adherence.dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "fresh-internal-architecture-reviewer",
  "overall_assessment": "Changes required. The operation-bound adapters, shared outbound orchestration, scoped resolution and single acceptance owner substantially follow the frozen architecture. A D04 response-classification defect and an unreliable D10 browser scenario remain. Pending final-all, PCV and post-cutover operator evidence are not treated as completed gates.",
  "recommended_path": "Correct the classifier and browser scenario within the approved D04/D10 boundaries, then review the updated candidate and obtain the required validation evidence. No architectural redesign is indicated.",
  "performance_position": "acceptable",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "ADH-01",
      "severity": "high",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Meta refusal classification ignores contradictory IDs after the first message",
      "rationale": "api-app/src/integrations/meta/meta.client.ts:219-234 extracts an ID only from messages[0] and uses its absence to establish REJECTED. HTTP 400 with a valid non-transient Graph error code 100 and messages:[{}, {id:'external-ack'}] therefore becomes REJECTED despite containing a contradictory external ID. A malformed first ID, such as messages:[{id:42}], can also reach REJECTED. Frozen D04 requires malformed or contradictory responses to remain UNKNOWN; a definitive refusal here could encourage an unsafe repeat send.",
      "suggested_action": "Validate the complete relevant response shape before classification and detect contradictory acceptance markers throughout the messages array. Return UNKNOWN/TRANSPORT_UNCONFIRMED for malformed or contradictory payloads. Add direct HTTP-client regression cases for a non-first external ID and a malformed message ID, retaining the one-request invariant.",
      "affected_paths": [
        "api-app/src/integrations/meta/meta.client.ts",
        "api-app/src/integrations/meta/meta.client.spec.ts"
      ]
    },
    {
      "finding_id": "ADH-02",
      "severity": "medium",
      "category": "tests",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "The delayed-response browser scenario loses its return-navigation target",
      "rationale": "web-app/e2e/channel-transport.spec.ts:59-81 first completes an accepted human send, then attempts A→B→A using the Cliente Timeline sidebar button. OutboundService.finalizeOutbound at api-app/src/domain/inbox/outbound.service.ts:233-238 moves A to IN_SERVICE, while Inbox starts on QUEUED and refreshes that filtered list after success. Once refreshed, A is absent from the sidebar, so the return click cannot reliably execute. The line 79 getByText assertion also does not establish that B finished opening: it can match the sidebar alone or become ambiguous with the thread heading. This leaves the required D10 stale-response scenario unreliable.",
      "suggested_action": "Arrange navigation so both conversations remain reachable through the appropriate status tabs. Wait for a unique active-thread selector to confirm B and then A have opened before releasing the held response. Assert that the stale completion preserves a newly entered draft and does not introduce an error, then rerun the complete browser/all gate.",
      "affected_paths": [
        "web-app/e2e/channel-transport.spec.ts",
        "web-app/src/telas/Inbox.tsx"
      ]
    }
  ]
}

## Prior disposition / evidence evidence/security.raw.json

{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/security.dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "fresh-no-context-security-reviewer",
  "overall_assessment": "risk=high; attack_simulation=required. Reviewed BFF authorization and session/CSRF composition, public API-key scoping, verified Typebot ingress, Prisma ownership boundaries, identity/generation/epoch/credential fences, operation-local credentials, sender/echo attribution, provider response consumption, destinations, redirects, timeouts, retries and Inbox error rendering. The common outbound design follows the frozen architectural direction; no tenant breakout or credential disclosure was demonstrated. Two source-only provider-response classification defects and a required attack-evidence gap remain. This reviewer performed no execution; neither finding is independently reproduced. The earlier API pass is owner-reported historical evidence, while final frozen all/browser/freshness and assisted IN/OUT remain pending. Threat hypotheses use the owner-supplied OWASP API1 source https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/ and API10 source https://api-security.owasp.org/editions/2023/en/0xaa-unsafe-consumption-of-apis/; they were not independently retrieved.",
  "recommended_path": "Resolve the response-classification findings within ST-CON-06, preserving the approved architecture, stable refusals, compatibility contracts and existing valid acknowledgement fixtures. Supply the exact local adversarial probes identified below, using provider doubles and disposable PostgreSQL without external attacks. Freeze the corrected candidate and obtain canonical all results bound to those bytes before closing the security gate; retain the separately pending assisted IN/OUT requirement. No new schema, durable intent, lifecycle rewrite or provider integration is warranted. Accepted residual limits remain the D03 local-check-to-network race, D05 crash/unknown-ID recovery limits and D07 observational availability; their recorded ST-CON-04 follow-up is not reopened.",
  "performance_position": "acceptable",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "SEC-01",
      "severity": "medium",
      "title": "Meta can classify a contradictory response as a definite refusal",
      "category": "security",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "rationale": "Source-only counterexample, not reproduced: meta.client.ts:219-234 examines only messages[0] when checking for an accepted ID. HTTP 400 with a valid allowlisted Graph error and messages:[{}, {id:'accepted-id'}] therefore returns REJECTED, despite an explicit contradictory ID elsewhere in the response. No validation rejects the multi-entry envelope first. Frozen D04 requires malformed or contradictory responses to remain UNKNOWN. The existing contradictory-ID test covers only the first entry. All outbound consumers can consequently receive a false definitive refusal, encouraging a manual resend after an uncertain external effect; no tenant escalation is asserted.",
      "suggested_action": "Validate the complete single-send response envelope before classifying ACCEPTED or REJECTED. Malformed message entries or contradictory acceptance evidence anywhere in the envelope must produce UNKNOWN/TRANSPORT_UNCONFIRMED. Add a local fetch-double test for an allowlisted refusal with an ID after the first entry, asserting one POST and UNKNOWN, while preserving ordinary allowlisted refusal behavior.",
      "affected_paths": [
        "api-app/src/integrations/meta/meta.client.ts:219",
        "api-app/src/integrations/meta/meta.client.ts:233",
        "api-app/src/integrations/meta/meta.client.spec.ts:81"
      ]
    },
    {
      "finding_id": "SEC-02",
      "severity": "medium",
      "title": "Evolution treats an acknowledgement-free object as proof of an acknowledgement",
      "category": "security",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "rationale": "Source-only counterexample, not reproduced: evolution.client.ts:116-129 accepts any successful HTTP JSON object without a truthy error as ACK_WITHOUT_ID when key is absent. A malformed 2xx body of {} therefore reaches outbound.service.ts:128-145, persists a diagnostic and reports that the channel accepted the send without confirming its ID. HTTP success plus an arbitrary object does not establish the valid acknowledgement required by D04/D05. This does not falsely return send success, but it creates unsupported provider-trust metadata and a persistent diagnostic rather than retaining transport uncertainty.",
      "suggested_action": "Require the supported acknowledgement envelope before returning ACK_WITHOUT_ID; an absent acknowledgement structure must remain UNKNOWN/TRANSPORT_UNCONFIRMED. Preserve the approved key:{} acknowledgement case. Add local tests contrasting 2xx {} with key:{}, asserting one POST in each case and no ambiguous-outbound diagnostic for the malformed response.",
      "affected_paths": [
        "api-app/src/integrations/evolution/evolution.client.ts:116",
        "api-app/src/integrations/evolution/evolution.client.ts:126",
        "api-app/src/domain/inbox/outbound.service.ts:128",
        "api-app/src/integrations/evolution/evolution.client.spec.ts:70"
      ]
    },
    {
      "finding_id": "SEC-03",
      "severity": "medium",
      "title": "Required pre-dispatch and cross-tenant attack probes are not evidenced",
      "category": "tests",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "rationale": "This is a bounded evidence gap, not a reproduced vulnerability. The supplied tests demonstrate forged internal ingress rejection, post-dispatch identity/generation changes and permitted post-dispatch credential-version rotation. They do not demonstrate rejection when version or epoch changes after binding but before the adapter's pre-dispatch check. The overlapping-send test uses one BU and the common fixture token, so it cannot expose cross-tenant credential reuse. The supplied public cross-tenant test exercises GET, and no denied BFF send/CSRF-negative mutation probe is shown. These are explicit D02/D03 and Security Risk Assessment attack-simulation obligations; the previous API pass and pending final all do not establish these particular observations.",
      "suggested_action": "Supply existing probe source and candidate-bound results, or add probes within admitted test paths: deny a BFF send without conversation grant and without the required CSRF header; deny a scoped API-key POST to a foreign account with zero provider calls; hold execution after binding, change credential version, generation or pairing epoch separately, then assert CHANNEL_CONTEXT_CHANGED/BLOCKED with zero POSTs and zero OUT writes; overlap sends from two tenants with distinct resources and scoped tokens and assert each exact token/resource pairing and tenant-local persistence. Preserve the separate successful post-dispatch version-only rotation test.",
      "affected_paths": [
        "api-app/test/channel-transport.e2e-spec.ts:121",
        "api-app/test/channel-transport.e2e-spec.ts:175",
        "api-app/test/channel-transport.e2e-spec.ts:236",
        "api-app/test/channel-transport.e2e-spec.ts:280",
        "api-app/test/api-publica.e2e-spec.ts:100",
        "api-app/src/integrations/channels/prisma-channel-resolver.ts:281"
      ]
    }
  ]
}

## Prior disposition / evidence evidence/adherence-round2.raw.json

{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/adherence-round2.dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "fresh-no-context-architecture-reviewer-round2",
  "overall_assessment": "Changes required within the approved architecture. The operation-bound adapters, common outbound owner, scoped credentials, single MessageAcceptance writer, deterministic selection and preserved consumer contracts remain consistent with D01..10. The original Meta and Evolution counterexamples are corrected. A remaining contradictory-response case and weaknesses in the new D03/D10 protection evidence require remediation. No material performance or elegance regression is apparent from source. This review performed no execution; final all, PCV, dedicated audits, final review and post-activation operator proof remain pending.",
  "recommended_path": "Correct the remaining Meta contradiction handling and strengthen the pre-dispatch and stale-response regression probes within existing approved paths. Preserve the current architecture and recorded compatibility limits. Obtain candidate-bound canonical validation and complete the separately required delivery gates before closeout.",
  "performance_position": "acceptable",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "ADH-R2-01",
      "severity": "medium",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Meta still accepts an envelope containing an explicit contradictory success flag",
      "rationale": "In meta.client.ts:225, HTTP 200 with {success:false,messages:[{id:'external-ack'}]} returns ACCEPTED because the positive branch checks only error absence and the message ID. Likewise, {success:false,messages:[{}]} reaches ACK_WITHOUT_ID at lines238-241. The success field is examined only when considering rejection. These contradictory envelopes therefore permit authoritative Message persistence or an acknowledgement diagnostic despite D04 requiring a valid acknowledgement and uncertainty for contradictory responses. This is a new counterexample at the changed classifier locus, distinct from the resolved non-first and malformed-ID cases.",
      "suggested_action": "Validate explicit success indicators before either positive acknowledgement branch. Contradictory or malformed indicators should produce UNKNOWN/TRANSPORT_UNCONFIRMED. Add raw HTTP regressions for both contradictory envelopes, preserving valid responses without a success field, stable refusals, one POST and the absence of local acceptance or diagnostic writes for unconfirmed transport.",
      "affected_paths": [
        "api-app/src/integrations/meta/meta.client.ts",
        "api-app/src/integrations/meta/meta.client.spec.ts"
      ]
    },
    {
      "finding_id": "ADH-R2-02",
      "severity": "medium",
      "category": "tests",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "The stale-response assertions can finish before the Inbox consumes the response",
      "rationale": "The corrected browser scenario establishes reachable, uniquely opened B and A threads and enters a fresh same-text draft. However, channel-transport.spec.ts:91-96 waits only for Playwright's response event before asserting a value and alert count that already hold before release. That event does not establish completion of api.ts response-body consumption or the Inbox responder continuation. Both assertions can therefore pass before a defective stale continuation clears the draft or changes the error state, leaving the required D10 protection susceptible to a false green.",
      "suggested_action": "Synchronize with complete response consumption and browser-side handling before evaluating the retained draft and error state. Demonstrate that the scenario fails when the stale-completion generation fence is removed, then run the exact final browser/all candidate.",
      "affected_paths": [
        "web-app/e2e/channel-transport.spec.ts",
        "web-app/src/api.ts",
        "web-app/src/telas/Inbox.tsx"
      ]
    },
    {
      "finding_id": "ADH-R2-03",
      "severity": "medium",
      "category": "tests",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "The new pre-dispatch probe substitutes the adapter that must enforce the fence",
      "rationale": "channel-transport.e2e-spec.ts:115-151 exercises the real resolver predicate, but replaces the shipping adapter with FencedDispatchChannel. That test-only channel itself invokes stillCurrent and blocks its synthetic effect. The probe remains green if BoundMetaChannel or BoundEvolutionChannel stops invoking its pre-dispatch callback. It establishes the resolver predicate's behavior without protecting the required D03 connection between that predicate and the actual provider dispatch. The shipping source currently contains the guard; this is a protection-harness gap, not a demonstrated vulnerability.",
      "suggested_action": "Exercise the shipping bound adapters in negative pre-dispatch probes. A test factory can delegate to the real factory while wrapping its callback to mutate the disposable binding after resolution. Assert CHANNEL_CONTEXT_CHANGED, zero provider calls and zero OUT writes, and ensure removing the shipping callback invocation makes the probe fail.",
      "affected_paths": [
        "api-app/test/channel-transport.e2e-spec.ts",
        "api-app/src/integrations/channels/meta-channel.ts",
        "api-app/src/integrations/channels/evolution-channel.ts"
      ]
    }
  ]
}

## Prior disposition / evidence evidence/security-round2.raw.json

{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/security-round2.dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "fresh-no-context-security-reconvergence-reviewer",
  "overall_assessment": "Changes required in two protection scenarios. The supplied implementation follows the approved domain port, operation-scoped adapters, common orchestration and sole MessageAcceptance owner. The original Meta and Evolution classifier counterexamples are corrected without architectural expansion. Reviewed surfaces include BFF session/CSRF/BU authorization, public API-key ownership, verified bot ingress, credential and identity fences, concurrent credential isolation, provider response trust, redirects, retries, error rendering and acceptance provenance. Security risk remains high; attack simulation is required. The owner-supplied OWASP API1 and API10 references informed authorization and provider-consumption hypotheses; they were not independently retrieved. No execution, exploit reproduction, tenant breakout or credential disclosure is established by this review. API results are writer-reported, and final all/browser, PCV, dedicated audits and post-activation operator IN/OUT remain pending. Performance is acceptable at source level: metadata remains batched and dispatch adds no external probes or retries; measured performance is not certified.",
  "recommended_path": "Repair the pre-dispatch tests to exercise the production adapters and synchronize the delayed-response browser assertions with application processing. These are changes within the approved protection harness, requiring no redesign or new product capability. Obtain candidate-bound validation and reconverge review before closing the findings. Preserve the pending delivery gates and the approved local-check-to-network, crash recovery, null-ID deduplication and observational availability limits; fixtures cannot establish external readiness.",
  "performance_position": "acceptable",
  "elegance_position": "acceptable",
  "structural_soundness_position": "acceptable",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "ADH-R2-01",
      "severity": "medium",
      "category": "tests",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Pre-dispatch probes substitute the adapter that must enforce the fence",
      "rationale": "channel-transport.e2e-spec.ts:30-50 implements the pre-dispatch check inside FencedDispatchChannel, and lines 115-151 replace the production registry with that implementation. The probes exercise the real resolver callback and PostgreSQL changes, but would remain green if BoundMetaChannel stopped invoking beforeDispatch. Zero provider-client calls are also inherent in this substitute. Source inspection shows the production check exists today; this is a protection gap in the newly added D03/R04 scenario, not a demonstrated vulnerability.",
      "suggested_action": "Place the mutation immediately before delegation to a Channel created by the production MetaChannelFactory, retaining the real resolver callback and injected provider double. Assert BLOCKED/CHANNEL_CONTEXT_CHANGED, zero provider invocations and zero OUT writes for each mutation. Protect the Evolution adapter's invocation of the same fence as well. The scenarios should fail if the production adapter omits its check.",
      "affected_paths": [
        "api-app/test/channel-transport.e2e-spec.ts:30",
        "api-app/test/channel-transport.e2e-spec.ts:115",
        "api-app/src/integrations/channels/meta-channel.ts:14",
        "api-app/src/integrations/channels/evolution-channel.ts:14"
      ]
    },
    {
      "finding_id": "ADH-R2-02",
      "severity": "medium",
      "category": "tests",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "Draft preservation can be asserted before the stale completion is processed",
      "rationale": "web-app/e2e/channel-transport.spec.ts:90-96 enters the replacement draft before releasing the response, then waits only for the response event and status. That event does not establish completion of api.ts body consumption or Inbox's continuation. Both assertions already hold before release, so they can pass before an unfenced continuation clears the same-text draft. The navigation correction is sound, but the changed scenario still lacks reliable evidence that the draft survives application processing.",
      "suggested_action": "Synchronize with completion of the original response body and its browser-side application processing before checking the retained draft and absent alert. Use a deterministic completion signal without adding production DTO fields or arbitrary sleeps, and verify that removing the generation guard makes this scenario fail.",
      "affected_paths": [
        "web-app/e2e/channel-transport.spec.ts:90",
        "web-app/src/api.ts:71",
        "web-app/src/telas/Inbox.tsx:396"
      ]
    }
  ]
}

## Prior disposition / evidence evidence/meta-mutant-source-observation.json

{
  "captured_at_utc": "2026-10-20T15:51:00.509808+00:00",
  "scope": "one exact public module, read-only; no generic Git/source discovery",
  "executor_reported_run": 16223,
  "module": "api-app/src/integrations/channels/meta-channel.ts",
  "original_reviewed_raw_sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138",
  "current_raw_sha256": "ff13fad8fd3de8a5188a5bed4473ce562dcc1e6f70f7ca6eea49033bb83d19a7",
  "different_from_reviewed": true,
  "observed_diff_normalized_text": "--- reviewed-restored-target\n+++ observed-current-module\n@@ -11,7 +11,7 @@\n   ) {}\n \n   async sendMessage(message: TextMessage): Promise<ChannelSendResult> {\n-    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };\n+    // Mutation probe: intentionally skip the binding fence.\n     if (!this.credential.phoneNumberId || !this.credential.accessToken) {\n       return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };\n     }\n",
  "limitation": "Source observation only, not terminal result or proof of restoration. Read exact reporter result/log separately."
}


## Prior disposition / evidence evidence/meta-mutant-failure-restoration.json

{
  "captured_at_utc": "2026-10-20T15:52:38.393052+00:00",
  "run_id": 16223,
  "command": "bash scripts/test-channels-local.sh api",
  "terminal_exit_reported_by_executor": 1,
  "raw_log_path": "foundation_documentation/artifacts/tmp/stcon06-meta-shipping-mutant.log",
  "raw_log_sha256": "b6b02e76ade7471f4a26dd2670d768bd7952d59a30ad7456e9a8f56aba226ab0",
  "raw_log_bytes": 48600,
  "selected_log_lines": [
    " Test Files  21 passed (21)",
    "      Tests  194 passed (194)",
    "     \u2192 expected 409 \"Conflict\", got 201 \"Created\"",
    " FAIL  test/channel-transport.e2e-spec.ts > common Channel outbound (PostgreSQL) > blocks real binding changes inside Meta/Evolution adapter pre-dispatch callbacks",
    "Error: expected 409 \"Conflict\", got 201 \"Created\"",
    " Test Files  1 failed | 26 passed (27)",
    "      Tests  1 failed | 308 passed (309)"
  ],
  "mutant_source_observation": "evidence/meta-mutant-source-observation.json",
  "restored_module": "api-app/src/integrations/channels/meta-channel.ts",
  "restored_sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138",
  "reviewed_sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138",
  "restoration_exact": true,
  "scope": "One shipping guard omitted only in disposable validation; no human runtime activation. Root independently hashes closed log/source; process exit is writer-reported."
}


## Prior disposition / evidence evidence/evolution-mutant-source-observation.json

{
  "captured_at_utc": "2026-10-20T15:52:38.393052+00:00",
  "module": "api-app/src/integrations/channels/evolution-channel.ts",
  "original_reviewed_sha256": "60faf1ea40fe17ad62495b0f42a2cf958defcb41e3ad72d3d2213751539b460c",
  "current_sha256": "be111003d398e2f24cd8294c803068f97eda29a7b418ad04cce424a765f995ab",
  "different_from_reviewed": true,
  "observed_diff_normalized_text": "--- reviewed-restored-target\n+++ observed-current-module\n@@ -11,7 +11,7 @@\n   ) {}\n \n   async sendMessage(message: TextMessage): Promise<ChannelSendResult> {\n-    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };\n+    // Mutation probe: intentionally skip the binding fence.\n     if (!this.credential.evolutionInstanceName) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };\n     try {\n       return await this.client.enviarTexto(this.credential.evolutionInstanceName, message.recipientRef, message.text);\n",
  "scope": "One exact public module read-only; no terminal/restoration claim",
  "executor_reported_run": 59583
}


## Prior disposition / evidence evidence/evolution-mutant-failure-restoration.json

{
  "captured_at_utc": "2026-10-20T15:57:31.006071+00:00",
  "run_id": 59583,
  "terminal_exit_reported_by_executor": 1,
  "raw_log_path": "foundation_documentation/artifacts/tmp/stcon06-evolution-shipping-mutant.log",
  "raw_log_sha256": "bf7b65e18fa3e851a31a796adf3864b74e7a16080f2823492af80dbd6c3310a2",
  "raw_log_bytes": 49707,
  "selected_log_lines": [
    " Test Files  21 passed (21)",
    "      Tests  194 passed (194)",
    "     \u2192 expected 409 \"Conflict\", got 201 \"Created\"",
    " FAIL  test/channel-transport.e2e-spec.ts > common Channel outbound (PostgreSQL) > blocks real binding changes inside Meta/Evolution adapter pre-dispatch callbacks",
    "Error: expected 409 \"Conflict\", got 201 \"Created\"",
    " Test Files  1 failed | 26 passed (27)",
    "      Tests  1 failed | 308 passed (309)"
  ],
  "mutation_observation": "evidence/evolution-mutant-source-observation.json",
  "restoration_exact": true,
  "restored_modules": [
    {
      "path": "api-app/src/integrations/channels/meta-channel.ts",
      "restored_sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138",
      "reviewed_sha256": "997e739cf7d7231918dc97fc347bfeb32a1cd74d084ead8c64b01157022f8138"
    },
    {
      "path": "api-app/src/integrations/channels/evolution-channel.ts",
      "restored_sha256": "60faf1ea40fe17ad62495b0f42a2cf958defcb41e3ad72d3d2213751539b460c",
      "reviewed_sha256": "60faf1ea40fe17ad62495b0f42a2cf958defcb41e3ad72d3d2213751539b460c"
    },
    {
      "path": "web-app/src/telas/Inbox.tsx",
      "restored_sha256": "d70bde9ede67759d479f644598356e46aac2916a12b2ed1770c17a169118586c",
      "reviewed_sha256": "d70bde9ede67759d479f644598356e46aac2916a12b2ed1770c17a169118586c"
    }
  ],
  "limitation": "Root independently hashed closed log and exact restored public modules; command exit supplied by executor. Browser mutant result is separately executor-reported; no independent Inbox mutant-source snapshot."
}


## Prior disposition / evidence assurance-preparation.md

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


## Prior disposition / evidence decision-adherence-candidate.md

# ST-CON-06 — candidate decision trace

Derived integration map, not a delivered/adherent verdict. Source evidence refers to the principal-checkout candidate; final all, independent audit resolutions, local activation and assisted IN/OUT are separate requirements. Frozen D01..10 remain unchanged. No exception or waiver is declared here.

| Decision | Concrete source / regression locus | Current assessment / limit |
|---|---|---|
| D-01 | `domain/channels/transport/channel.ts` Channel/TextMessage; `integrations/channels/channel-adapter-registry.ts`; independent fake in `test/channel-transport.e2e-spec.ts:90` | Source matches an opaque text port and operation factory registration; no real future network is claimed |
| D-02 | `prisma-channel-resolver.ts:40` conversation/verified-ingress entry points; credential owner resolver; BFF/public existing auth middleware/controllers; `channel-transport.e2e-spec.ts:154`, `:176`, `:383` | Required denied mutations and distinct-tenant in-flight token/resource probes now present; exact candidate-bound finalall still required |
| D-03 | `prisma-channel-resolver.ts:181` frozen binding and pre-dispatch closure; `:281` local identity/version check; `channel-transport.e2e-spec.ts:115`, `:293`, `:322` | Pre-dispatch version/generation/epoch and real REAUTORIZAR versus version-only tests are distinct; local-check-to-network race remains explicit |
| D-04 | `meta.client.ts:189` and `evolution.client.ts:95`; direct HTTP tests in corresponding client specs | Round1 R01/R03 corrections validate complete supported envelopes; fresh independent follow-up must confirm classification, no retry and onePOST |
| D-05 | `outbound.service.ts:69` accepted completion, `:110` unknown projection, `:191` bounded readback, `:263` fixed incomplete error; `outbound.service.spec.ts` | Existing unit tests distinguish positive commit, uncertain commit and context retirement. Legacy400 code is not evidence of refusal; external ACCEPTED is not delivered |
| D-06 | `outbound.service.ts:148` pre-dispatch trusted source intent and `:221` conditional finalization; unchanged `message-acceptance.service.ts`; public controller no post-send writes; PG claim/echo regressions | One keyed acceptance writer and current-owner conditional completion; no new schema or intent. Crash and null-ID deduplication limits persist |
| D-07 | `prisma-channel-resolver.ts:240` deterministic latest origin; metadata batch `:103`, LATERAL window projection `:318`; `channel-transport.e2e-spec.ts:351`, `:370`; Typebot barrier suite | Metadata availability is observational only; no implicit provider fallback. Existing stored-time latest-IN window without transport filter remains for ST-CON-04 |
| D-08 | Registry/factory + opaque fake through real resolver/BFF/PG, `channel-transport.e2e-spec.ts:90` | Sender port remains open; current physical origin enum and existing public numeric-phone input are intentionally preserved. Future identity/ingress requires separate contract |
| D-09 | Single `channel-transport.module.ts` imported by BFF/Public/Webhooks; dependency guard `channel-dependencies.spec.ts` includes synthetic forbidden imports/branches | Initial dependency RED recorded; final guard green must be candidate-bound. No parallel legacy dispatch is authorized |
| D-10 | Web `api.ts`/`api.spec.ts` safe outcome fields; Inbox availability/error/draft fence; `e2e/channel-transport.spec.ts`; safe runner and both positive-path freshness helpers | Same-text newly edited draft scenario corrected after root check. Current browser/finalall and post-local-activation operator proof remain necessary; old50/50 diagnostic is insufficient |

API source paths above are relative to `api-app/src` unless explicitly prefixed `test/`. Web paths are relative to `web-app`. Exact file hashes are supplied by the frozen review/validation manifest, not inferred from unchanged HEADs.

## Module decision consistency

The approved module snapshot in the TODO is the comparison authority. The candidate preserves: one active number per BU/current channel slot; current registration and reauthorization lifecycle; scoped encrypted credentials; provider-resource identity and keyed message acceptance; per-surface session/API-key/bot authority; existing public numeric-phone contract; timeline ordering/DTOs; human claim semantics; bot queue/owner/unread semantics. D01/D06/D07/D09 establish the approved abstract transport, common orchestration and explicit bot window enforcement. Modules will record these delivered owners and limits only after actual gates. No constitution/schema or unapproved provider capability is introduced.


## Prior disposition / evidence evidence/ci-command-parity-observation.json

{
  "status": "read-only source observation, not a CI execution",
  "paths": [
    {
      "path": ".github/workflows/ci.yml",
      "sha256": "4448e7dbb47a85c432f4975bf55a1e786402f7e8c5ba3fe70d054eb182de1607"
    },
    {
      "path": "api-app/package.json",
      "sha256": "df8551d3e506e7c68516cbd482362c4282671b7ec7eebbf121386390ac080a9d"
    },
    {
      "path": "web-app/package.json",
      "sha256": "fc9083821e246d50c080f409b3590902b033041231d1688c04c4140f097818de"
    },
    {
      "path": "api-app/vitest.config.e2e.ts",
      "sha256": "ff76a3b94de4649d18f0f824a24bb45428afcbb751a872a6841a2e388f45f8ff"
    },
    {
      "path": "web-app/playwright.config.ts",
      "sha256": "53e9a54e97c9b785135d94846d99eb77c6f05789a58f27128544f9b2c903a63d"
    }
  ],
  "existing_root_workflow": "compose config + API lint/build/unit +Webbuild/unit, Node22; no rootPG E2E or Playwright job is asserted",
  "canonical_local_contract": "bash scripts/test-channels-local.sh all is a project-owned required local gate; runs realPG migration/status+APIlint/build/unit/E2E+Webbuild/unit+freshbuiltChromium. It is a broader local validation suite, not proof of a remote run.",
  "boundaries": "No rootCI edit, sourcecommit/push/gitlink/deploy. Do not infer submodule remoteCI configuration from the root workflow.",
  "dependency_parity": "Both production locks/manifests and real NestDI/Prisma/PostgreSQL/current public contracts used locally; external providers doubled, physical delivery operator-only.",
  "review_requirement": "IndependentTQA must judge command/topology parity and any concrete confidence gap without substituting remoteCI claim."
}


## Implemented Frontend / Consumer Matrix

| Producer | Required consumer | Implementation / evidence in snapshot | Pending requirement |
|---|---|---|---|
| Channel/ChannelResolver | Common Outbound, BFF/Public/Typebot | Domain port, operation-bound registry/factories/resolver and common Outbound; new PG independent opaque fake, barriers and dependency guard source included; prior API305 green before final narrow updates | Final frozen all |
| BFF GET thread availability | Inbox composer | Additive janela.disponivel/motivo in controller/api.ts/Inbox, fixed reason wording and disabled composer; real-BFF new browser cases provided | Final browser green/served freshness |
| BFF POST result/outcome | ErroDaApi/Inbox | Safe fields propagated, honest fixed backend errors; draft retained/no retry; new raw/unit/PG tests plus browser mutation/held response cases | Final frozen all |
| Public GET list/thread projection | Existing partner API clients | Additive envio_disponivel/motivo_indisponibilidade, null when available; server contract assertions and batching/query evidence tests | Final all; external-only API consumer as already approved, no new frontend promised |
| Public POST messages | Existing partner API client and inbox projection | Existing phone input/success contract preserved, PUBLIC attribution enters before dispatch, controller postwrites removed, real API-key PG claim overlap | Final all; no public API UI added |
| Incoming Typebot text | Existing bot session output | Accepted ingress pinned, shared window/readiness/outbound/acceptance; preserved bot queue/owner, held window/identity/other-origin tests included | Final all; no new bot UI |

Every row has an implemented current consumer. No backend-only waiver is invented. Pending evidence is explicit and prevents final delivery independently of this code-adherence review.


This historical matrix lists actual consumers; currentcomponent status194/309API and50browser is stated above. Finalall and physicalproof remain required. No new waiver.

## Unchanged critical context api-app/src/integrations/evolution/evolution.client.spec.ts

```text
0001 |import { afterEach, describe, expect, it, vi } from 'vitest';
0002 |import { EvolutionHttpClient, EvolutionIndisponivelError } from './evolution.client';
0003 |
0004 |describe('EvolutionHttpClient instance creation response', () => {
0005 |  const before = {
0006 |    url: process.env.EVOLUTION_API_URL,
0007 |    key: process.env.EVOLUTION_API_KEY,
0008 |    webhook: process.env.EVOLUTION_WEBHOOK_URL, secret: process.env.EVOLUTION_WEBHOOK_SECRET,
0009 |  };
0010 |  afterEach(() => {
0011 |    vi.unstubAllGlobals();
0012 |    if (before.url === undefined) delete process.env.EVOLUTION_API_URL; else process.env.EVOLUTION_API_URL = before.url;
0013 |    if (before.key === undefined) delete process.env.EVOLUTION_API_KEY; else process.env.EVOLUTION_API_KEY = before.key;
0014 |    if (before.webhook === undefined) delete process.env.EVOLUTION_WEBHOOK_URL; else process.env.EVOLUTION_WEBHOOK_URL = before.webhook;
0015 |    if (before.secret === undefined) delete process.env.EVOLUTION_WEBHOOK_SECRET; else process.env.EVOLUTION_WEBHOOK_SECRET = before.secret;
0016 |  });
0017 |
0018 |  it('returns only QR material when create confirms the exact instance name', async () => {
0019 |    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
0020 |    process.env.EVOLUTION_API_KEY = 'fixture-key';
0021 |    process.env.EVOLUTION_WEBHOOK_URL = 'https://api.invalid/webhooks/evolution';
0022 |    process.env.EVOLUTION_WEBHOOK_SECRET = 'fixture-secret';
0023 |    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => ({
0024 |      instance: { instanceName: 'lh-channel-1' }, hash: 'must-not-escape', qrcode: { base64: 'fixture-qr' },
0025 |    }) });
0026 |    vi.stubGlobal('fetch', fetchFake);
0027 |    const result = await new EvolutionHttpClient().criarInstancia('lh-channel-1');
0028 |    expect(result).toEqual({ qrcode: 'fixture-qr' });
0029 |    expect(JSON.stringify(result)).not.toContain('must-not-escape');
0030 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0031 |    const requestBody = JSON.parse(fetchFake.mock.calls[0][1].body as string);
0032 |    expect(requestBody.webhook).toMatchObject({ url: 'https://api.invalid/webhooks/evolution', headers: { 'x-leadshug-webhook-secret': 'fixture-secret' } });
0033 |  });
0034 |
0035 |  it.each([
0036 |    {},
0037 |    { instance: { instanceName: 'another-instance' }, qrcode: { base64: 'must-not-escape' } },
0038 |  ])('rejects a successful HTTP response without exact created identity confirmation', async (payload) => {
0039 |    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
0040 |    process.env.EVOLUTION_API_KEY = 'fixture-key';
0041 |    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => payload });
0042 |    vi.stubGlobal('fetch', fetchFake);
0043 |    await expect(new EvolutionHttpClient().criarInstancia('lh-requested-instance')).rejects.toBeInstanceOf(EvolutionIndisponivelError);
0044 |  });
0045 |
0046 |  it('requires an explicit SUCCESS response for exact-instance cleanup', async () => {
0047 |    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
0048 |    process.env.EVOLUTION_API_KEY = 'fixture-key';
0049 |    const fetchFake = vi.fn()
0050 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ status: 'SUCCESS', error: false }) })
0051 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ status: 'SUCCESS', error: true }) });
0052 |    vi.stubGlobal('fetch', fetchFake);
0053 |    const client = new EvolutionHttpClient();
0054 |    await expect(client.apagarInstancia('lh-exact-name')).resolves.toBeUndefined();
0055 |    await expect(client.apagarInstancia('lh-exact-name')).rejects.toBeInstanceOf(EvolutionIndisponivelError);
0056 |    expect(String(fetchFake.mock.calls[0][0])).toContain('/instance/delete/lh-exact-name');
0057 |  });
0058 |
0059 |  it('rejects redirects without following them or exposing the configured key', async () => {
0060 |    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
0061 |    process.env.EVOLUTION_API_KEY = 'fixture-secret-key';
0062 |    const fetchFake = vi.fn().mockRejectedValue(new TypeError('redirect fixture with secret URL'));
0063 |    vi.stubGlobal('fetch', fetchFake);
0064 |    const error = await new EvolutionHttpClient().criarInstancia('lh-safe-name').catch((caught: unknown) => caught as Error);
0065 |    expect(error).toBeInstanceOf(EvolutionIndisponivelError);
0066 |    expect(error.message).not.toMatch(/fixture-secret-key|secret URL/);
0067 |    expect(fetchFake.mock.calls[0][1].redirect).toBe('error');
0068 |  });
0069 |
0070 |  it('returns ACCEPTED only with an external ID and treats HTTP and post-dispatch failures as UNKNOWN once', async () => {
0071 |    process.env.EVOLUTION_API_URL = 'https://evolution.invalid';
0072 |    process.env.EVOLUTION_API_KEY = 'fixture-key';
0073 |    const fetchFake = vi.fn()
0074 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ key: { id: 'evo-id-1' } }) })
0075 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ key: {} }) })
0076 |      .mockResolvedValueOnce({ ok: false, status: 503, json: async () => ({ message: 'ambiguous provider body' }) })
0077 |      .mockRejectedValueOnce(new TypeError('timeout after dispatch'))
0078 |      .mockResolvedValueOnce({ ok: true, json: async () => { throw new SyntaxError('malformed'); } })
0079 |      .mockResolvedValueOnce({ ok: false, status: 503, json: async () => ({ key: { id: 'contradictory-id' } }) })
0080 |      .mockResolvedValueOnce({ ok: true, json: async () => ({}) });
0081 |    vi.stubGlobal('fetch', fetchFake);
0082 |    const client = new EvolutionHttpClient();
0083 |    await expect(client.enviarTexto('fixture-instance', 'user:opaque', 'hello'))
0084 |      .resolves.toMatchObject({ outcome: 'ACCEPTED', externalMessageId: 'evo-id-1' });
0085 |    await expect(client.enviarTexto('fixture-instance', 'user:opaque', 'hello'))
0086 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID' });
0087 |    await expect(client.enviarTexto('fixture-instance', 'user:opaque', 'hello'))
0088 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0089 |    await expect(client.enviarTexto('fixture-instance', 'user:opaque', 'hello'))
0090 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0091 |    await expect(client.enviarTexto('fixture-instance', 'user:opaque', 'hello'))
0092 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0093 |    await expect(client.enviarTexto('fixture-instance', 'user:opaque', 'hello'))
0094 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0095 |    await expect(client.enviarTexto('fixture-instance', 'user:opaque', 'hello'))
0096 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0097 |    expect(fetchFake).toHaveBeenCalledTimes(7);
0098 |    expect(fetchFake.mock.calls.every(([, options]) => options.signal instanceof AbortSignal)).toBe(true);
0099 |  });
0100 |});
```

## Unchanged critical context api-app/src/integrations/evolution/evolution.client.ts

```text
0001 |import { Injectable } from '@nestjs/common';
0002 |import type { ChannelSendResult } from '../../domain/channels/transport/channel';
0003 |
0004 |export const EVOLUTION_CLIENT = Symbol('EVOLUTION_CLIENT');
0005 |
0006 |export interface InstanciaCriada {
0007 |  qrcode: string | null;
0008 |}
0009 |export interface InstanciaObservada { name: string; ownerJid: string | null; connectionStatus: string | null; }
0010 |
0011 |/**
0012 | * Porta do canal não oficial. Adaptador de SAÍDA — a Evolution API é serviço
0013 | * interno do projeto, **sem domínio público** (ADR-0002).
0014 | */
0015 |export interface EvolutionClient {
0016 |  configurado(): boolean;
0017 |  criarInstancia(nome: string): Promise<InstanciaCriada>;
0018 |  qrDaInstancia(nome: string): Promise<string | null>;
0019 |  estadoDaInstancia(nome: string): Promise<string>;
0020 |  consultarInstancia(nome: string): Promise<InstanciaObservada | null>;
0021 |  apagarInstancia(nome: string): Promise<void>;
0022 |  /** Não existe janela aqui — o limite é o risco de ban, não a plataforma. */
0023 |  enviarTexto(instancia: string, para: string, texto: string): Promise<ChannelSendResult>;
0024 |}
0025 |
0026 |export class EvolutionIndisponivelError extends Error {}
0027 |
0028 |@Injectable()
0029 |export class EvolutionHttpClient implements EvolutionClient {
0030 |  private readonly base = process.env.EVOLUTION_API_URL ?? '';
0031 |  private readonly chave = process.env.EVOLUTION_API_KEY ?? '';
0032 |  private readonly webhook = process.env.EVOLUTION_WEBHOOK_URL ?? '';
0033 |  private readonly webhookSecret = process.env.EVOLUTION_WEBHOOK_SECRET ?? '';
0034 |
0035 |  configurado(): boolean {
0036 |    return this.base.length > 0 && this.chave.length > 0;
0037 |  }
0038 |
0039 |  async criarInstancia(nome: string): Promise<InstanciaCriada> {
0040 |    const corpo: Record<string, unknown> = {
0041 |      instanceName: nome,
0042 |      qrcode: true,
0043 |      integration: 'WHATSAPP-BAILEYS',
0044 |    };
0045 |    if (this.webhook && this.webhookSecret) {
0046 |      corpo.webhook = {
0047 |        enabled: true,
0048 |        url: this.webhook,
0049 |        headers: { 'x-leadshug-webhook-secret': this.webhookSecret },
0050 |        byEvents: false,
0051 |        base64: false,
0052 |        events: ['MESSAGES_UPSERT', 'CONNECTION_UPDATE'],
0053 |      };
0054 |    }
0055 |    const data = await this.chamar('POST', '/instance/create', corpo);
0056 |    const payload = data as { instance?: { instanceName?: unknown }; qrcode?: { base64?: string } | string; base64?: string };
0057 |    if (!payload.instance || payload.instance.instanceName !== nome) {
0058 |      throw new EvolutionIndisponivelError('A Evolution não confirmou a identidade da instância solicitada.');
0059 |    }
0060 |    return {
0061 |      qrcode:
0062 |        (typeof payload.qrcode === 'string' ? payload.qrcode : payload.qrcode?.base64) ??
0063 |        payload.base64 ??
0064 |        null,
0065 |    };
0066 |  }
0067 |
0068 |  async qrDaInstancia(nome: string): Promise<string | null> {
0069 |    const data = await this.chamar('GET', `/instance/connect/${nome}`);
0070 |    const payload = data as { qrcode?: { base64?: string } | string; base64?: string };
0071 |    return (typeof payload.qrcode === 'string' ? payload.qrcode : payload.qrcode?.base64) ?? payload.base64 ?? null;
0072 |  }
0073 |
0074 |  async estadoDaInstancia(nome: string): Promise<string> {
0075 |    const data = await this.chamar('GET', `/instance/connectionState/${nome}`);
0076 |    return (data as { instance?: { state?: string } }).instance?.state ?? 'desconhecido';
0077 |  }
0078 |
0079 |  async consultarInstancia(nome: string): Promise<InstanciaObservada | null> {
0080 |    const query = new URLSearchParams({ instanceName: nome });
0081 |    const data = await this.chamar('GET', `/instance/fetchInstances?${query.toString()}`);
0082 |    const instances = Array.isArray(data) ? data : [];
0083 |    const found = instances.find((item) => item && typeof item === 'object' && (item as { name?: unknown }).name === nome) as Record<string, unknown> | undefined;
0084 |    if (!found) return null;
0085 |    return {
0086 |      name: typeof found.name === 'string' ? found.name : nome,
0087 |      ownerJid: typeof found.ownerJid === 'string' ? found.ownerJid : null,
0088 |      connectionStatus: typeof found.connectionStatus === 'string' ? found.connectionStatus : null,
0089 |    };
0090 |  }
0091 |
0092 |  async apagarInstancia(nome: string): Promise<void> {
0093 |    const result = await this.chamar('DELETE', `/instance/delete/${encodeURIComponent(nome)}`) as { status?: unknown; error?: unknown };
0094 |    if (result.status !== 'SUCCESS' || result.error !== false) throw new EvolutionIndisponivelError('A Evolution não confirmou a remoção da instância.');
0095 |  }
0096 |
0097 |  async enviarTexto(instancia: string, para: string, texto: string): Promise<ChannelSendResult> {
0098 |    if (!instancia || !this.configurado()) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
0099 |    let response: Response;
0100 |    try {
0101 |      response = await fetch(`${this.base}/message/sendText/${encodeURIComponent(instancia)}`, {
0102 |        method: 'POST',
0103 |        headers: { apikey: this.chave, 'content-type': 'application/json' },
0104 |        body: JSON.stringify({ number: para, text: texto }),
0105 |        signal: AbortSignal.timeout(10_000), redirect: 'error',
0106 |      });
0107 |    } catch {
0108 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0109 |    }
0110 |    let data: unknown;
0111 |    try {
0112 |      data = await response.json();
0113 |    } catch {
0114 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0115 |    }
0116 |    if (!response.ok) return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0117 |    if (!isRecord(data)) return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0118 |    if (data.error) return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0119 |    if (data.key !== undefined && data.key !== null && !isRecord(data.key)) {
0120 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0121 |    }
0122 |    const key = isRecord(data.key) ? data.key : null;
0123 |    if (!key) return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0124 |    if (key && Object.hasOwn(key, 'id') && typeof key.id !== 'string') {
0125 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0126 |    }
0127 |    const id = typeof key?.id === 'string' && key.id.trim() ? key.id : null;
0128 |    return id
0129 |      ? { outcome: 'ACCEPTED', externalMessageId: id }
0130 |      : { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'EVOLUTION_RECUSOU' };
0131 |  }
0132 |
0133 |  private async chamar(metodo: string, caminho: string, corpo?: unknown): Promise<unknown> {
0134 |    let res: Response;
0135 |    try {
0136 |      res = await fetch(`${this.base}${caminho}`, {
0137 |        method: metodo,
0138 |        headers: { apikey: this.chave, 'content-type': 'application/json' },
0139 |        body: corpo ? JSON.stringify(corpo) : undefined,
0140 |        signal: AbortSignal.timeout(10_000), redirect: 'error',
0141 |      });
0142 |    } catch {
0143 |      throw new EvolutionIndisponivelError('A Evolution API está temporariamente indisponível.');
0144 |    }
0145 |    const data = await res.json().catch(() => ({}));
0146 |    if (!res.ok) {
0147 |      void data;
0148 |      throw new EvolutionIndisponivelError('A Evolution API recusou a operação.');
0149 |    }
0150 |    return data;
0151 |  }
0152 |}
0153 |
0154 |function isRecord(value: unknown): value is Record<string, unknown> {
0155 |  return typeof value === 'object' && value !== null && !Array.isArray(value);
0156 |}
```

## Changed source api-app/src/integrations/meta/meta.client.spec.ts

```text
0001 |import { afterEach, describe, expect, it, vi } from 'vitest';
0002 |import { MetaHttpClient, MetaIndisponivelError } from './meta.client';
0003 |
0004 |describe('MetaHttpClient scoped credentials', () => {
0005 |  const vars = ['META_APP_ID', 'META_APP_SECRET', 'META_SIGNUP_CONFIG_ID', 'GRAPH_VERSION', 'WHATSAPP_TOKEN'];
0006 |  const before = new Map(vars.map((key) => [key, process.env[key]]));
0007 |  afterEach(() => {
0008 |    vi.unstubAllGlobals();
0009 |    for (const key of vars) {
0010 |      const value = before.get(key);
0011 |      if (value === undefined) delete process.env[key]; else process.env[key] = value;
0012 |    }
0013 |  });
0014 |
0015 |  it('exposes only public installation capability and is unavailable when unset', () => {
0016 |    delete process.env.META_APP_ID;
0017 |    delete process.env.META_APP_SECRET;
0018 |    delete process.env.META_SIGNUP_CONFIG_ID;
0019 |    process.env.WHATSAPP_TOKEN = 'fake-legacy-token';
0020 |    delete process.env.GRAPH_VERSION;
0021 |    expect(new MetaHttpClient().capabilities()).toMatchObject({ available: false, reason: 'NOT_CONFIGURED', appId: null, configId: null, graphVersion: null });
0022 |  });
0023 |
0024 |  it('rejects partial installation setup without returning its secret', () => {
0025 |    process.env.META_APP_ID = 'fake-app-id';
0026 |    process.env.META_APP_SECRET = '';
0027 |    process.env.META_SIGNUP_CONFIG_ID = '';
0028 |    process.env.GRAPH_VERSION = '';
0029 |    expect(new MetaHttpClient().capabilities()).toMatchObject({ available: false, reason: 'PARTIAL_CONFIGURATION', appId: 'fake-app-id' });
0030 |  });
0031 |
0032 |  it.each([undefined, '', 'v26', '26.0', 'v26.1', 'vabc.0'])('fails closed for missing, blank, or malformed Graph version (%s)', (version) => {
0033 |    process.env.META_APP_ID = 'fake-app-id';
0034 |    process.env.META_APP_SECRET = 'fake-secret';
0035 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0036 |    if (version === undefined) delete process.env.GRAPH_VERSION; else process.env.GRAPH_VERSION = version;
0037 |    expect(new MetaHttpClient().capabilities()).toMatchObject({ available: false, reason: 'PARTIAL_CONFIGURATION', graphVersion: null });
0038 |  });
0039 |
0040 |  it('does not call Graph for a malformed configured version', async () => {
0041 |    process.env.META_APP_ID = 'fake-app-id';
0042 |    process.env.META_APP_SECRET = 'fake-secret';
0043 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0044 |    process.env.GRAPH_VERSION = 'https://graph.invalid';
0045 |    const fetchFake = vi.fn();
0046 |    vi.stubGlobal('fetch', fetchFake);
0047 |    await expect(new MetaHttpClient().registrarNumero('phone-id', '123456', 'scoped-token')).rejects.toBeInstanceOf(MetaIndisponivelError);
0048 |    expect(fetchFake).not.toHaveBeenCalled();
0049 |    expect(new MetaHttpClient().capabilities().graphVersion).toBeNull();
0050 |    process.env.GRAPH_VERSION = '';
0051 |    await expect(new MetaHttpClient().enviarTexto('phone-id', '5584999990000', 'fixture body', 'scoped-channel-token'))
0052 |      .resolves.toMatchObject({ outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' });
0053 |    expect(fetchFake).not.toHaveBeenCalled();
0054 |  });
0055 |
0056 |  it('exchanges code in a POST body and never places it in the URL', async () => {
0057 |    process.env.META_APP_ID = 'fake-id';
0058 |    process.env.META_APP_SECRET = 'fake-secret';
0059 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0060 |    process.env.GRAPH_VERSION = 'v26.0';
0061 |    expect(new MetaHttpClient().capabilities()).toMatchObject({ available: true, reason: 'AVAILABLE', graphVersion: 'v26.0' });
0062 |    const fetchFake = vi.fn()
0063 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ access_token: 'candidate-token' }) })
0064 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [{ scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] }] } }) });
0065 |    vi.stubGlobal('fetch', fetchFake);
0066 |    const result = await new MetaHttpClient().exchangeCode('sensitive-code');
0067 |    expect(result.accessToken).toBe('candidate-token');
0068 |    expect(fetchFake.mock.calls[0][0]).not.toContain('sensitive-code');
0069 |    expect(String(fetchFake.mock.calls[0][1].body)).toContain('code=sensitive-code');
0070 |  });
0071 |
0072 |  it('does not use legacy token and emits a safe error for provider details', async () => {
0073 |    process.env.WHATSAPP_TOKEN = 'legacy-token-must-not-be-used';
0074 |    const fetchFake = vi.fn().mockResolvedValue({ ok: false, status: 400, json: async () => ({ error: { message: 'secret provider detail' } }) });
0075 |    vi.stubGlobal('fetch', fetchFake);
0076 |    await expect(new MetaHttpClient().enviarTexto('phone-id', '558400000000', 'hello'))
0077 |      .resolves.toMatchObject({ outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' });
0078 |    expect(fetchFake).not.toHaveBeenCalled();
0079 |  });
0080 |
0081 |  it('classifies only allowlisted synchronous Graph refusals as REJECTED', async () => {
0082 |    process.env.GRAPH_VERSION = 'v26.0';
0083 |    const fetchFake = vi.fn()
0084 |      .mockResolvedValueOnce({ ok: false, status: 400, json: async () => ({ error: { message: 'bad request', code: 100, is_transient: false } }) })
0085 |      .mockResolvedValueOnce({ ok: false, status: 400, json: async () => ({ error: { message: 'unknown refusal', code: 999, is_transient: false } }) })
0086 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ messages: [{ id: 'wamid-1' }] }) })
0087 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ messages: [{}] }) })
0088 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => { throw new SyntaxError('malformed'); } })
0089 |      .mockResolvedValueOnce({ ok: false, status: 503, json: async () => ({ messages: [{ id: 'contradictory-id' }] }) })
0090 |      .mockResolvedValueOnce({ ok: false, status: 400, json: async () => ({
0091 |        error: { message: 'refusal with contradictory accepted ID', code: 100, is_transient: false }, messages: [{ id: 'contradictory-refusal-id' }],
0092 |      }) })
0093 |      .mockResolvedValueOnce({ ok: false, status: 400, json: async () => ({
0094 |        error: { message: 'refusal with contradictory success', code: 100, is_transient: false }, success: true,
0095 |      }) })
0096 |      .mockResolvedValueOnce({ ok: false, status: 400, json: async () => ({
0097 |        error: { message: 'malformed transient flag', code: 100, is_transient: 'false' },
0098 |      }) })
0099 |      .mockResolvedValueOnce({ ok: false, status: 400, json: async () => ({
0100 |        error: { message: 'later acknowledgement ID', code: 100, is_transient: false }, messages: [{}, { id: 'later-id' }],
0101 |      }) })
0102 |      .mockResolvedValueOnce({ ok: false, status: 400, json: async () => ({
0103 |        error: { message: 'malformed message ID', code: 100, is_transient: false }, messages: [{ id: 42 }],
0104 |      }) })
0105 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ messages: [{}, { id: 'second-id' }] }) })
0106 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ messages: [{ id: 42 }] }) })
0107 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ success: false, messages: [{ id: 'ack-with-false-success' }] }) })
0108 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ success: false, messages: [{}] }) })
0109 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ success: 'false', messages: [{ id: 'malformed-success' }] }) });
0110 |    vi.stubGlobal('fetch', fetchFake);
0111 |    const client = new MetaHttpClient();
0112 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0113 |      .resolves.toMatchObject({ outcome: 'REJECTED', code: 'META_RECUSOU' });
0114 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0115 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0116 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0117 |      .resolves.toMatchObject({ outcome: 'ACCEPTED', externalMessageId: 'wamid-1' });
0118 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0119 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID' });
0120 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0121 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0122 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0123 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0124 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0125 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0126 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0127 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0128 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0129 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0130 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0131 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0132 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0133 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0134 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0135 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0136 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0137 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0138 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0139 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0140 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0141 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0142 |    await expect(client.enviarTexto('phone-id', '558400000000', 'hello', 'scoped'))
0143 |      .resolves.toMatchObject({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' });
0144 |    expect(fetchFake).toHaveBeenCalledTimes(16);
0145 |  });
0146 |
0147 |  it('requires both scoped permissions on the same WABA before listing phone numbers', async () => {
0148 |    process.env.META_APP_ID = 'fake-id';
0149 |    process.env.META_APP_SECRET = 'fake-secret';
0150 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0151 |    process.env.GRAPH_VERSION = 'v26.0';
0152 |    const tokenInfo = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0153 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0154 |      { scope: 'whatsapp_business_messaging', target_ids: ['654321'] },
0155 |    ] } };
0156 |    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => tokenInfo });
0157 |    vi.stubGlobal('fetch', fetchFake);
0158 |    const client = new MetaHttpClient();
0159 |    await expect(client.recursos('candidate', '123456')).rejects.toBeInstanceOf(MetaIndisponivelError);
0160 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0161 |  });
0162 |
0163 |  it('verifies the selected phone on the provider-returned page cursor and rejects a foreign phone', async () => {
0164 |    process.env.META_APP_ID = 'fake-id';
0165 |    process.env.META_APP_SECRET = 'fake-secret';
0166 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0167 |    process.env.GRAPH_VERSION = 'v26.0';
0168 |    const fetchFake = vi.fn()
0169 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0170 |        { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0171 |        { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0172 |      ] } }) })
0173 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] }) });
0174 |    vi.stubGlobal('fetch', fetchFake);
0175 |    const client = new MetaHttpClient();
0176 |    const number = await client.confirmarNumero('123456', '987654321', 'candidate', 'provider-cursor-page-2');
0177 |    expect(number).toMatchObject({ id: '987654321', telefone: '5584999990000' });
0178 |    const edgeUrl = String(fetchFake.mock.calls[1][0]);
0179 |    expect(edgeUrl).toContain('/v26.0/123456/phone_numbers');
0180 |    expect(new URL(edgeUrl).searchParams.get('after')).toBe('provider-cursor-page-2');
0181 |    expect(String(fetchFake.mock.calls[0][1].headers.authorization)).toBe('Bearer fake-id|fake-secret');
0182 |
0183 |    const foreign = vi.fn()
0184 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0185 |        { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0186 |        { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0187 |      ] } }) })
0188 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321' }] }) });
0189 |    vi.stubGlobal('fetch', foreign);
0190 |    await expect(client.confirmarNumero('123456', '111111111', 'candidate', 'provider-cursor-page-2')).resolves.toBeNull();
0191 |  });
0192 |
0193 |  it('verifies a persisted phone on the second scoped page without following provider URLs', async () => {
0194 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0195 |    const grant = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0196 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0197 |    ] } };
0198 |    const fetchFake = vi.fn()
0199 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0200 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '111111111' }], paging: { next: 'https://foreign.invalid/secret', cursors: { after: 'cursor-page-2' } } }) })
0201 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] }) });
0202 |    vi.stubGlobal('fetch', fetchFake);
0203 |    const number = await new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0204 |    expect(number).toMatchObject({ id: '987654321', telefone: '5584999990000' });
0205 |    expect(fetchFake).toHaveBeenCalledTimes(3);
0206 |    expect(fetchFake.mock.calls[0][1].headers.authorization).toBe('Bearer fake-id|fake-secret');
0207 |    for (const [url, options] of fetchFake.mock.calls) {
0208 |      expect(String(url)).toMatch(/^https:\/\/graph\.facebook\.com\/v26\.0\//);
0209 |      expect(options.redirect).toBe('error');
0210 |    }
0211 |    expect(fetchFake.mock.calls[1][1].headers.authorization).toBe('Bearer scoped-candidate');
0212 |    expect(new URL(String(fetchFake.mock.calls[2][0])).searchParams.get('after')).toBe('cursor-page-2');
0213 |  });
0214 |
0215 |  it('returns absence only after an exhausted page and rejects a WABA outside the grant', async () => {
0216 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0217 |    const grant = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0218 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0219 |    ] } };
0220 |    const exhausted = vi.fn()
0221 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0222 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '111111111' }] }) });
0223 |    vi.stubGlobal('fetch', exhausted);
0224 |    await expect(new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate')).resolves.toBeNull();
0225 |    expect(exhausted).toHaveBeenCalledTimes(2);
0226 |
0227 |    const foreign = vi.fn().mockResolvedValue({ ok: true, json: async () => grant });
0228 |    vi.stubGlobal('fetch', foreign);
0229 |    await expect(new MetaHttpClient().verificarNumeroVinculado('654321', '987654321', 'scoped-candidate')).resolves.toBeNull();
0230 |    expect(foreign).toHaveBeenCalledTimes(1);
0231 |
0232 |    const invalidGrant = vi.fn().mockResolvedValue({ ok: true, json: async () => ({ data: {
0233 |      app_id: 'different-app', is_valid: true, scopes: ['whatsapp_business_management'],
0234 |      granular_scopes: [{ scope: 'whatsapp_business_management', target_ids: ['123456'] }],
0235 |    } }) });
0236 |    vi.stubGlobal('fetch', invalidGrant);
0237 |    const invalidGrantOperation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0238 |    await expect(invalidGrantOperation).rejects.toBeInstanceOf(MetaIndisponivelError);
0239 |    await expect(invalidGrantOperation).rejects.toMatchObject({ code: 'META_INDISPONIVEL' });
0240 |    expect(invalidGrant).toHaveBeenCalledTimes(1);
0241 |  });
0242 |
0243 |  it('rejects a revoked but otherwise valid scoped grant before listing phone numbers', async () => {
0244 |    process.env.META_APP_ID = 'fake-id';
0245 |    process.env.META_APP_SECRET = 'fake-secret';
0246 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0247 |    process.env.GRAPH_VERSION = 'v26.0';
0248 |    const revokedGrant = { data: {
0249 |      app_id: 'fake-id',
0250 |      is_valid: false,
0251 |      scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'],
0252 |      granular_scopes: [
0253 |        { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0254 |        { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0255 |      ],
0256 |    } };
0257 |    const validPhonePage = { data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] };
0258 |    const fetchFake = vi.fn()
0259 |      .mockResolvedValueOnce({ ok: true, json: async () => revokedGrant })
0260 |      .mockResolvedValueOnce({ ok: true, json: async () => validPhonePage });
0261 |    vi.stubGlobal('fetch', fetchFake);
0262 |
0263 |    const operation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0264 |    const rejection = await operation.catch((error: unknown) => error);
0265 |
0266 |    expect(rejection).toBeInstanceOf(MetaIndisponivelError);
0267 |    expect(rejection).toMatchObject({ code: 'META_INDISPONIVEL' });
0268 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0269 |    const debugUrl = new URL(String(fetchFake.mock.calls[0][0]));
0270 |    expect(debugUrl.origin).toBe('https://graph.facebook.com');
0271 |    expect(debugUrl.pathname).toBe('/v26.0/debug_token');
0272 |    expect(debugUrl.searchParams.get('input_token')).toBe('scoped-candidate');
0273 |    expect(fetchFake.mock.calls[0][1].headers.authorization).toBe('Bearer fake-id|fake-secret');
0274 |    expect(fetchFake.mock.calls.some(([url]) => String(url).includes('/phone_numbers'))).toBe(false);
0275 |  });
0276 |
0277 |  it('rejects an otherwise valid scoped grant issued to a different app before listing phone numbers', async () => {
0278 |    process.env.META_APP_ID = 'fake-id';
0279 |    process.env.META_APP_SECRET = 'fake-secret';
0280 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0281 |    process.env.GRAPH_VERSION = 'v26.0';
0282 |    const wrongAppGrant = { data: {
0283 |      app_id: 'different-app',
0284 |      is_valid: true,
0285 |      scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'],
0286 |      granular_scopes: [
0287 |        { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0288 |        { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0289 |      ],
0290 |    } };
0291 |    const validPhonePage = { data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] };
0292 |    const fetchFake = vi.fn()
0293 |      .mockResolvedValueOnce({ ok: true, json: async () => wrongAppGrant })
0294 |      .mockResolvedValueOnce({ ok: true, json: async () => validPhonePage });
0295 |    vi.stubGlobal('fetch', fetchFake);
0296 |
0297 |    const operation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0298 |    const rejection = await operation.catch((error: unknown) => error);
0299 |
0300 |    expect(rejection).toBeInstanceOf(MetaIndisponivelError);
0301 |    expect(rejection).toMatchObject({ code: 'META_INDISPONIVEL' });
0302 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0303 |    const debugUrl = new URL(String(fetchFake.mock.calls[0][0]));
0304 |    expect(debugUrl.origin).toBe('https://graph.facebook.com');
0305 |    expect(debugUrl.pathname).toBe('/v26.0/debug_token');
0306 |    expect(debugUrl.searchParams.get('input_token')).toBe('scoped-candidate');
0307 |    expect(fetchFake.mock.calls[0][1].headers.authorization).toBe('Bearer fake-id|fake-secret');
0308 |    expect(fetchFake.mock.calls.some(([url]) => String(url).includes('/phone_numbers'))).toBe(false);
0309 |  });
0310 |
0311 |  it.each([
0312 |    ['malformed JSON', { ok: true, json: async () => { throw new SyntaxError('provider-json-secret'); } }],
0313 |    ['missing data', { ok: true, json: async () => ({ paging: {} }) }],
0314 |    ['non-array data', { ok: true, json: async () => ({ data: { id: '987654321' } }) }],
0315 |    ['row without an id', { ok: true, json: async () => ({ data: [{ display_phone_number: '+55 84 99999-0000' }] }) }],
0316 |    ['null row', { ok: true, json: async () => ({ data: [null] }) }],
0317 |    ['non-object row', { ok: true, json: async () => ({ data: ['987654321'] }) }],
0318 |    ['non-object paging', { ok: true, json: async () => ({ data: [], paging: 'next-page' }) }],
0319 |    ['non-string next link', { ok: true, json: async () => ({ data: [], paging: { next: 42 } }) }],
0320 |    ['missing cursor for next page', { ok: true, json: async () => ({ data: [], paging: { next: 'https://graph.facebook.com/next' } }) }],
0321 |  ])('fails closed for invalid successful phone page: %s', async (_label, pageResponse) => {
0322 |    process.env.META_APP_ID = 'fake-id';
0323 |    process.env.META_APP_SECRET = 'fake-secret';
0324 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0325 |    process.env.GRAPH_VERSION = 'v26.0';
0326 |    const grant = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0327 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0328 |      { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0329 |    ] } };
0330 |    const fetchFake = vi.fn()
0331 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0332 |      .mockResolvedValueOnce(pageResponse);
0333 |    vi.stubGlobal('fetch', fetchFake);
0334 |    const operation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0335 |    await expect(operation).rejects.toBeInstanceOf(MetaIndisponivelError);
0336 |    await expect(operation).rejects.toMatchObject({ code: 'META_INDISPONIVEL' });
0337 |    expect(fetchFake).toHaveBeenCalledTimes(2);
0338 |    expect(String(fetchFake.mock.calls[1][0])).toMatch(/^https:\/\/graph\.facebook\.com\/v26\.0\/123456\/phone_numbers/);
0339 |  });
0340 |
0341 |  it.each([null, [], 'invalid-root', 17])('rejects a successful non-object JSON root before consuming page budget (%s)', async (root) => {
0342 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0343 |    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => root });
0344 |    vi.stubGlobal('fetch', fetchFake);
0345 |    const operation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0346 |    await expect(operation).rejects.toBeInstanceOf(MetaIndisponivelError);
0347 |    await expect(operation).rejects.toMatchObject({ code: 'META_INDISPONIVEL' });
0348 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0349 |  });
0350 |
0351 |  it.each([
0352 |    ['data object missing', {}],
0353 |    ['data null', { data: null }],
0354 |    ['data array', { data: [] }],
0355 |    ['data primitive', { data: 'invalid-data' }],
0356 |    ['app_id non-string', { data: { app_id: 17, is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0357 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0358 |    ] } }],
0359 |    ['is_valid non-boolean', { data: { app_id: 'fake-id', is_valid: 'true', scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0360 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0361 |    ] } }],
0362 |    ['scopes object', { data: { app_id: 'fake-id', is_valid: true, scopes: { invalid: true }, granular_scopes: [
0363 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0364 |    ] } }],
0365 |    ['scopes null', { data: { app_id: 'fake-id', is_valid: true, scopes: null, granular_scopes: [
0366 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0367 |    ] } }],
0368 |    ['scopes with non-string entry', { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 17], granular_scopes: [
0369 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0370 |    ] } }],
0371 |    ['granular_scopes null', { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: null } }],
0372 |    ['granular_scopes object', { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: {} } }],
0373 |    ['null granular entry', { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [null] } }],
0374 |    ['granular entry missing scope', { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [{ target_ids: ['123456'] }] } }],
0375 |    ['target_ids object', { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0376 |      { scope: 'whatsapp_business_management', target_ids: { invalid: true } }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0377 |    ] } }],
0378 |    ['target_ids with non-string entry', { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0379 |      { scope: 'whatsapp_business_management', target_ids: ['123456', 987654] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0380 |    ] } }],
0381 |  ])('fails closed for malformed debug-grant shape: %s', async (_label, grant) => {
0382 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0383 |    const validPhonePage = { data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] };
0384 |    const fetchFake = vi.fn()
0385 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0386 |      .mockResolvedValueOnce({ ok: true, json: async () => validPhonePage });
0387 |    vi.stubGlobal('fetch', fetchFake);
0388 |    const operation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0389 |    const error = await operation.catch((caught: unknown) => caught);
0390 |    expect(error).toBeInstanceOf(MetaIndisponivelError);
0391 |    expect(error).toMatchObject({ code: 'META_INDISPONIVEL' });
0392 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0393 |    expect(String(fetchFake.mock.calls[0][0])).toMatch(/^https:\/\/graph\.facebook\.com\/v26\.0\/debug_token\?/);
0394 |    expect(String(fetchFake.mock.calls[0][1].headers.authorization)).toBe('Bearer fake-id|fake-secret');
0395 |  });
0396 |
0397 |  it('accepts omitted scopes when required granular scopes authorize the selected WABA', async () => {
0398 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0399 |    const grant = { data: { app_id: 'fake-id', is_valid: true, granular_scopes: [
0400 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0401 |      { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0402 |    ] } };
0403 |    const fetchFake = vi.fn()
0404 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0405 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] }) });
0406 |    vi.stubGlobal('fetch', fetchFake);
0407 |    await expect(new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate'))
0408 |      .resolves.toMatchObject({ id: '987654321', telefone: '5584999990000' });
0409 |    expect(fetchFake).toHaveBeenCalledTimes(2);
0410 |    expect(String(fetchFake.mock.calls[0][0])).toMatch(/^https:\/\/graph\.facebook\.com\/v26\.0\/debug_token\?/);
0411 |    expect(String(fetchFake.mock.calls[0][1].headers.authorization)).toBe('Bearer fake-id|fake-secret');
0412 |    expect(String(fetchFake.mock.calls[1][0])).toMatch(/^https:\/\/graph\.facebook\.com\/v26\.0\/123456\/phone_numbers/);
0413 |  });
0414 |
0415 |  it('accepts an irrelevant granular scope without target_ids alongside required scopes', async () => {
0416 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0417 |    const grant = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0418 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0419 |      { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0420 |      { scope: 'business_management' },
0421 |    ] } };
0422 |    const fetchFake = vi.fn()
0423 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0424 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] }) });
0425 |    vi.stubGlobal('fetch', fetchFake);
0426 |    await expect(new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate'))
0427 |      .resolves.toMatchObject({ id: '987654321', telefone: '5584999990000' });
0428 |    expect(fetchFake).toHaveBeenCalledTimes(2);
0429 |    expect(String(fetchFake.mock.calls[0][0])).toMatch(/^https:\/\/graph\.facebook\.com\/v26\.0\/debug_token\?/);
0430 |    expect(String(fetchFake.mock.calls[0][1].headers.authorization)).toBe('Bearer fake-id|fake-secret');
0431 |    expect(String(fetchFake.mock.calls[1][0])).toMatch(/^https:\/\/graph\.facebook\.com\/v26\.0\/123456\/phone_numbers/);
0432 |  });
0433 |
0434 |  it('keeps a valid 101-WABA authorization target usable while limiting the options page to 100', async () => {
0435 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0436 |    const targets = Array.from({ length: 101 }, (_, index) => String(123450 + index));
0437 |    const grant = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0438 |      { scope: 'whatsapp_business_management', target_ids: targets },
0439 |      { scope: 'whatsapp_business_messaging', target_ids: targets },
0440 |    ] } };
0441 |    const selectedWaba = targets[100];
0442 |    const fetchFake = vi.fn()
0443 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0444 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0445 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321', display_phone_number: '+55 84 99999-0000' }] }) });
0446 |    vi.stubGlobal('fetch', fetchFake);
0447 |    const client = new MetaHttpClient();
0448 |    const options = await client.recursos('scoped-candidate');
0449 |    expect(options.wabas).toHaveLength(100);
0450 |    expect(options.wabas.some(({ id }) => id === selectedWaba)).toBe(false);
0451 |    await expect(client.verificarNumeroVinculado(selectedWaba, '987654321', 'scoped-candidate'))
0452 |      .resolves.toMatchObject({ id: '987654321', telefone: '5584999990000' });
0453 |    expect(fetchFake).toHaveBeenCalledTimes(3);
0454 |    expect(new URL(String(fetchFake.mock.calls[2][0])).pathname).toBe(`/v26.0/${selectedWaba}/phone_numbers`);
0455 |  });
0456 |
0457 |  it('fails closed at the page budget and for repeated or oversized cursors', async () => {
0458 |    process.env.META_APP_ID = 'fake-id'; process.env.META_APP_SECRET = 'fake-secret'; process.env.META_SIGNUP_CONFIG_ID = 'fake-config'; process.env.GRAPH_VERSION = 'v26.0';
0459 |    const grant = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0460 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0461 |    ] } };
0462 |    const page = (after: string) => ({ ok: true, json: async () => ({ data: [], paging: { next: 'https://graph.facebook.com/next', cursors: { after } } }) });
0463 |    const beyondBudget = vi.fn().mockResolvedValueOnce({ ok: true, json: async () => grant }).mockResolvedValueOnce(page('cursor-one')).mockResolvedValueOnce(page('cursor-two'));
0464 |    vi.stubGlobal('fetch', beyondBudget);
0465 |    const beyondBudgetOperation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0466 |    await expect(beyondBudgetOperation).rejects.toBeInstanceOf(MetaIndisponivelError);
0467 |    await expect(beyondBudgetOperation).rejects.toMatchObject({ code: 'META_INDISPONIVEL' });
0468 |    expect(beyondBudget).toHaveBeenCalledTimes(3);
0469 |
0470 |    const cyclic = vi.fn().mockResolvedValueOnce({ ok: true, json: async () => grant }).mockResolvedValueOnce(page('cursor-one')).mockResolvedValueOnce(page('cursor-one'));
0471 |    vi.stubGlobal('fetch', cyclic);
0472 |    const cyclicOperation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0473 |    await expect(cyclicOperation).rejects.toBeInstanceOf(MetaIndisponivelError);
0474 |    await expect(cyclicOperation).rejects.toMatchObject({ code: 'META_INDISPONIVEL' });
0475 |    expect(cyclic).toHaveBeenCalledTimes(3);
0476 |
0477 |    const oversized = vi.fn().mockResolvedValueOnce({ ok: true, json: async () => grant }).mockResolvedValueOnce(page('x'.repeat(513)));
0478 |    vi.stubGlobal('fetch', oversized);
0479 |    const oversizedOperation = new MetaHttpClient().verificarNumeroVinculado('123456', '987654321', 'scoped-candidate');
0480 |    await expect(oversizedOperation).rejects.toBeInstanceOf(MetaIndisponivelError);
0481 |    await expect(oversizedOperation).rejects.toMatchObject({ code: 'META_INDISPONIVEL' });
0482 |    expect(oversized).toHaveBeenCalledTimes(2);
0483 |  });
0484 |
0485 |  it('exposes a bounded page cursor only when the provider signals a next page', async () => {
0486 |    process.env.META_APP_ID = 'fake-id';
0487 |    process.env.META_APP_SECRET = 'fake-secret';
0488 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0489 |    process.env.GRAPH_VERSION = 'v26.0';
0490 |    const grant = { data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0491 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] }, { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0492 |    ] } };
0493 |    const fetchFake = vi.fn()
0494 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0495 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [{ id: '987654321' }], paging: { cursors: { after: 'cursor-last-page' } } }) });
0496 |    vi.stubGlobal('fetch', fetchFake);
0497 |    await expect(new MetaHttpClient().recursos('candidate', '123456')).resolves.toMatchObject({ next: null });
0498 |    fetchFake.mockReset()
0499 |      .mockResolvedValueOnce({ ok: true, json: async () => grant })
0500 |      .mockResolvedValueOnce({ ok: true, json: async () => ({ data: [], paging: { next: 'https://provider.invalid/page?secret=hidden', cursors: { after: 'safe-cursor' } } }) });
0501 |    await expect(new MetaHttpClient().recursos('candidate', '123456')).resolves.toMatchObject({ next: 'safe-cursor' });
0502 |  });
0503 |
0504 |  it('rejects redirects and never follows provider locations with registration credentials', async () => {
0505 |    process.env.GRAPH_VERSION = 'v26.0';
0506 |    const fetchFake = vi.fn().mockResolvedValue({ ok: false, status: 307, json: async () => ({ location: 'https://foreign.invalid' }) });
0507 |    vi.stubGlobal('fetch', fetchFake);
0508 |    await expect(new MetaHttpClient().registrarNumero('phone-id', '123456', 'candidate-token')).rejects.toBeInstanceOf(MetaIndisponivelError);
0509 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0510 |    expect(fetchFake.mock.calls[0][1].redirect).toBe('error');
0511 |  });
0512 |
0513 |  it('does not query a WABA outside the currently validated app grant', async () => {
0514 |    process.env.META_APP_ID = 'fake-id';
0515 |    process.env.META_APP_SECRET = 'fake-secret';
0516 |    process.env.META_SIGNUP_CONFIG_ID = 'fake-config';
0517 |    process.env.GRAPH_VERSION = 'v26.0';
0518 |    const fetchFake = vi.fn().mockResolvedValue({ ok: true, json: async () => ({ data: { app_id: 'fake-id', is_valid: true, scopes: ['whatsapp_business_management', 'whatsapp_business_messaging'], granular_scopes: [
0519 |      { scope: 'whatsapp_business_management', target_ids: ['123456'] },
0520 |      { scope: 'whatsapp_business_messaging', target_ids: ['123456'] },
0521 |    ] } }) });
0522 |    vi.stubGlobal('fetch', fetchFake);
0523 |    await expect(new MetaHttpClient().confirmarNumero('654321', '987654321', 'candidate')).resolves.toBeNull();
0524 |    expect(fetchFake).toHaveBeenCalledTimes(1);
0525 |  });
0526 |
0527 |  it.each([
0528 |    ['register', 'registrarNumero'],
0529 |    ['subscription', 'inscreverWaba'],
0530 |  ] as const)('requires an explicit provider success acknowledgement for %s', async (_label, method) => {
0531 |    process.env.GRAPH_VERSION = 'v26.0';
0532 |    const client = new MetaHttpClient();
0533 |    for (const response of [
0534 |      { success: false },
0535 |      { success: 'false' },
0536 |      { success: 'TRUE' },
0537 |      {},
0538 |    ]) {
0539 |      vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: async () => response }));
0540 |      await expect(method === 'registrarNumero'
0541 |        ? client.registrarNumero('phone-id', '123456', 'scoped-token')
0542 |        : client.inscreverWaba('waba-id', 'scoped-token')).rejects.toBeInstanceOf(MetaIndisponivelError);
0543 |    }
0544 |    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: async () => ({ success: true }) }));
0545 |    await expect(method === 'registrarNumero'
0546 |      ? client.registrarNumero('phone-id', '123456', 'scoped-token')
0547 |      : client.inscreverWaba('waba-id', 'scoped-token')).resolves.toBeUndefined();
0548 |    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: async () => ({ success: 'true' }) }));
0549 |    await expect(method === 'registrarNumero'
0550 |      ? client.registrarNumero('phone-id', '123456', 'scoped-token')
0551 |      : client.inscreverWaba('waba-id', 'scoped-token')).resolves.toBeUndefined();
0552 |  });
0553 |});
```

## Changed source api-app/src/integrations/meta/meta.client.ts

```text
0001 |import { Injectable } from '@nestjs/common';
0002 |import type { ChannelSendResult } from '../../domain/channels/transport/channel';
0003 |
0004 |export const META_CLIENT = Symbol('META_CLIENT');
0005 |
0006 |export interface MetaNumber {
0007 |  id: string;
0008 |  telefone: string | null;
0009 |  nomeVerificado: string | null;
0010 |}
0011 |
0012 |export interface MetaCapabilities {
0013 |  appId: string | null;
0014 |  configId: string | null;
0015 |  graphVersion: string | null;
0016 |  available: boolean;
0017 |  reason: 'AVAILABLE' | 'NOT_CONFIGURED' | 'PARTIAL_CONFIGURATION';
0018 |}
0019 |
0020 |/** Every customer operation is explicitly scoped to a decrypted channel token. */
0021 |export interface MetaClient {
0022 |  configurado(): boolean;
0023 |  canSendText(): boolean;
0024 |  capabilities(): MetaCapabilities;
0025 |  exchangeCode(code: string): Promise<{ accessToken: string }>;
0026 |  recursos(accessToken: string, wabaId?: string, after?: string): Promise<{ wabas: Array<{ id: string; name: string | null }>; numbers: MetaNumber[]; next: string | null }>;
0027 |  numerosDaWaba(wabaId: string, accessToken?: string, after?: string): Promise<{ data: MetaNumber[]; next: string | null }>;
0028 |  confirmarNumero(wabaId: string, phoneNumberId: string, accessToken: string, after?: string): Promise<MetaNumber | null>;
0029 |  verificarNumeroVinculado(wabaId: string, phoneNumberId: string, accessToken: string): Promise<MetaNumber | null>;
0030 |  registrarNumero(phoneNumberId: string, pin: string, accessToken: string): Promise<void>;
0031 |  inscreverWaba(wabaId: string, accessToken: string): Promise<void>;
0032 |  enviarTexto(phoneNumberId: string, para: string, texto: string, accessToken?: string): Promise<ChannelSendResult>;
0033 |}
0034 |
0035 |export class MetaIndisponivelError extends Error {
0036 |  readonly code = 'META_INDISPONIVEL';
0037 |  constructor(readonly detalhe = 'A Meta recusou a operação.') { super(detalhe); }
0038 |}
0039 |
0040 |type MetaGranularScope = { scope: string; targetIds?: string[] };
0041 |type MetaDebugGrant = { appId: string; valid: boolean; scopes: string[]; granularScopes: MetaGranularScope[] };
0042 |
0043 |@Injectable()
0044 |export class MetaHttpClient implements MetaClient {
0045 |  private readonly appId = process.env.META_APP_ID ?? '';
0046 |  private readonly appSecret = process.env.META_APP_SECRET ?? '';
0047 |  private readonly configId = process.env.META_SIGNUP_CONFIG_ID ?? '';
0048 |  private readonly graphVersion = process.env.GRAPH_VERSION?.trim() ?? '';
0049 |
0050 |  private graphVersionValida(): boolean { return /^v\d+\.0$/.test(this.graphVersion); }
0051 |
0052 |  capabilities(): MetaCapabilities {
0053 |    const configured = [this.appId, this.appSecret, this.configId, this.graphVersion].filter(Boolean).length;
0054 |    const graphValid = this.graphVersionValida();
0055 |    const available = configured === 4 && graphValid;
0056 |    return {
0057 |      appId: this.appId || null,
0058 |      configId: this.configId || null,
0059 |      graphVersion: graphValid ? this.graphVersion : null,
0060 |      available,
0061 |      reason: available ? 'AVAILABLE' : configured === 0 ? 'NOT_CONFIGURED' : 'PARTIAL_CONFIGURATION',
0062 |    };
0063 |  }
0064 |
0065 |  /** Compatibility probe for callers being retired; never supplies a credential. */
0066 |  configurado(): boolean { return this.capabilities().available; }
0067 |  canSendText(): boolean { return this.graphVersionValida(); }
0068 |
0069 |  async exchangeCode(code: string): Promise<{ accessToken: string }> {
0070 |    if (!this.capabilities().available) throw new MetaIndisponivelError('Autorização Meta indisponível.');
0071 |    const body = new URLSearchParams({
0072 |      client_id: this.appId,
0073 |      client_secret: this.appSecret,
0074 |      code,
0075 |    });
0076 |    const result = await this.request('/oauth/access_token', undefined, 'POST', body);
0077 |    const accessToken = typeof result.access_token === 'string' ? result.access_token : '';
0078 |    if (!accessToken) throw new MetaIndisponivelError('A Meta não concluiu a autorização.');
0079 |    await this.validateAccessToken(accessToken);
0080 |    return { accessToken };
0081 |  }
0082 |
0083 |  async recursos(accessToken: string, wabaId?: string, after?: string) {
0084 |    if (!accessToken) throw new MetaIndisponivelError('Credencial scoped do canal necessária.');
0085 |    const grant = this.assertCurrentGrant(await this.debugToken(accessToken));
0086 |    const wabas = wabaTargets(grant.granularScopes);
0087 |    if (!wabaId) return { wabas: wabas.slice(0, 100).map((id) => ({ id, name: null })), numbers: [], next: null };
0088 |    if (!wabas.includes(wabaId)) throw new MetaIndisponivelError('WABA não pertence à autorização atual.');
0089 |    const page = await this.numerosDaWaba(wabaId, accessToken, after);
0090 |    return { wabas: [{ id: wabaId, name: null }], numbers: page.data.slice(0, 100), next: page.next };
0091 |  }
0092 |
0093 |  private async validateAccessToken(accessToken: string) {
0094 |    this.assertCurrentGrant(await this.debugToken(accessToken));
0095 |  }
0096 |
0097 |  private assertCurrentGrant(value: unknown): MetaDebugGrant {
0098 |    const grant = parseMetaDebugGrant(value);
0099 |    const scopes = new Set([...grant.scopes, ...grant.granularScopes.map(({ scope }) => scope)]);
0100 |    if (grant.appId !== this.appId || !grant.valid || !scopes.has('whatsapp_business_management') || !scopes.has('whatsapp_business_messaging') || wabaTargets(grant.granularScopes).length === 0) {
0101 |      throw new MetaIndisponivelError('A autorização não concede identidade e escopos Meta necessários.');
0102 |    }
0103 |    return grant;
0104 |  }
0105 |
0106 |  private async debugToken(inputToken: string) {
0107 |    const query = new URLSearchParams({ input_token: inputToken });
0108 |    const response = await this.request(`/debug_token?${query.toString()}`, `${this.appId}|${this.appSecret}`);
0109 |    return response.data;
0110 |  }
0111 |
0112 |  async numerosDaWaba(wabaId: string, accessToken: string, after?: string) {
0113 |    if (!accessToken) throw new MetaIndisponivelError('Credencial scoped do canal necessária.');
0114 |    const url = new URL(`/${encodeURIComponent(wabaId)}/phone_numbers`, `https://graph.facebook.com/${this.graphVersion}`);
0115 |    url.searchParams.set('fields', 'id,display_phone_number,verified_name');
0116 |    url.searchParams.set('limit', '100');
0117 |    if (after) url.searchParams.set('after', after);
0118 |    const result = await this.request(url.pathname + url.search, accessToken);
0119 |    if (!Array.isArray(result.data)) throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0120 |    const rows = result.data.map((row) => {
0121 |      if (!isRecord(row) || typeof row.id !== 'string' || row.id.length === 0) {
0122 |        throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0123 |      }
0124 |      const digits = typeof row.display_phone_number === 'string' ? row.display_phone_number.replace(/\D/g, '') : '';
0125 |      return { id: row.id, telefone: digits || null, nomeVerificado: typeof row.verified_name === 'string' ? row.verified_name : null };
0126 |    });
0127 |    const data = rows;
0128 |    const paging = result.paging;
0129 |    if (paging !== undefined && paging !== null && !isRecord(paging)) {
0130 |      throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0131 |    }
0132 |    const providerNext = isRecord(paging) ? paging.next : undefined;
0133 |    if (providerNext !== undefined && providerNext !== null && typeof providerNext !== 'string') {
0134 |      throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0135 |    }
0136 |    const hasNext = typeof providerNext === 'string';
0137 |    const cursors = isRecord(paging) ? paging.cursors : undefined;
0138 |    if (cursors !== undefined && cursors !== null && !isRecord(cursors)) {
0139 |      throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0140 |    }
0141 |    const next = isRecord(cursors) ? cursors.after : undefined;
0142 |    if (hasNext && (typeof next !== 'string' || next.length === 0 || next.length > 512)) {
0143 |      throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
0144 |    }
0145 |    return { data, next: hasNext ? next as string : null };
0146 |  }
0147 |
0148 |  async confirmarNumero(wabaId: string, phoneNumberId: string, accessToken: string, after?: string) {
0149 |    const grant = this.assertCurrentGrant(await this.debugToken(accessToken));
0150 |    const targets = wabaTargets(grant.granularScopes);
0151 |    if (!targets.includes(wabaId)) return null;
0152 |    const page = await this.numerosDaWaba(wabaId, accessToken, after);
0153 |    return page.data.find((item) => item.id === phoneNumberId) ?? null;
0154 |  }
0155 |
0156 |  /** Revalidates a persisted phone identity across a small, fixed number of pages. */
0157 |  async verificarNumeroVinculado(wabaId: string, phoneNumberId: string, accessToken: string) {
0158 |    if (!accessToken) throw new MetaIndisponivelError('Credencial scoped do canal necessária.');
0159 |    const grant = this.assertCurrentGrant(await this.debugToken(accessToken));
0160 |    if (!wabaTargets(grant.granularScopes).includes(wabaId)) return null;
0161 |
0162 |    const cursors = new Set<string>();
0163 |    let after: string | undefined;
0164 |    for (let pageIndex = 0; pageIndex < 2; pageIndex += 1) {
0165 |      const page = await this.numerosDaWaba(wabaId, accessToken, after);
0166 |      const number = page.data.find((item) => item.id === phoneNumberId);
0167 |      if (number) return number;
0168 |      if (!page.next) return null;
0169 |      if (page.next.length > 512 || cursors.has(page.next)) {
0170 |        throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
0171 |      }
0172 |      if (pageIndex === 1) throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
0173 |      cursors.add(page.next);
0174 |      after = page.next;
0175 |    }
0176 |    throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
0177 |  }
0178 |
0179 |  async registrarNumero(phoneNumberId: string, pin: string, accessToken: string) {
0180 |    const result = await this.request(`/${encodeURIComponent(phoneNumberId)}/register`, accessToken, 'POST', { messaging_product: 'whatsapp', pin });
0181 |    if (result.success !== true && result.success !== 'true') throw new MetaIndisponivelError('A Meta não confirmou o registro do número.');
0182 |  }
0183 |
0184 |  async inscreverWaba(wabaId: string, accessToken: string) {
0185 |    const result = await this.request(`/${encodeURIComponent(wabaId)}/subscribed_apps`, accessToken, 'POST', {});
0186 |    if (result.success !== true && result.success !== 'true') throw new MetaIndisponivelError('A Meta não confirmou a inscrição do webhook.');
0187 |  }
0188 |
0189 |  async enviarTexto(phoneNumberId: string, para: string, texto: string, accessToken?: string): Promise<ChannelSendResult> {
0190 |    if (!accessToken) return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
0191 |    if (!phoneNumberId || !this.graphVersionValida()) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
0192 |    let response: Response;
0193 |    try {
0194 |      response = await fetch(`https://graph.facebook.com/${this.graphVersion}/${encodeURIComponent(phoneNumberId)}/messages`, {
0195 |        method: 'POST',
0196 |        headers: { accept: 'application/json', authorization: `Bearer ${accessToken}`, 'content-type': 'application/json' },
0197 |        body: JSON.stringify({ messaging_product: 'whatsapp', to: para, type: 'text', text: { body: texto } }),
0198 |        signal: AbortSignal.timeout(10_000), redirect: 'error',
0199 |      });
0200 |    } catch {
0201 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
0202 |    }
0203 |
0204 |    let payload: unknown;
0205 |    try {
0206 |      payload = await response.json();
0207 |    } catch {
0208 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
0209 |    }
0210 |    if (!isRecord(payload)) {
0211 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
0212 |    }
0213 |    if (payload.messages !== undefined && !Array.isArray(payload.messages)) {
0214 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
0215 |    }
0216 |    if (payload.error !== undefined && payload.error !== null && !isRecord(payload.error)) {
0217 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
0218 |    }
0219 |    const messages = Array.isArray(payload.messages) ? payload.messages : [];
0220 |    const first = messages[0];
0221 |    const validMessageEnvelope = messages.every((message) => isRecord(message)
0222 |      && (message.id === undefined || (typeof message.id === 'string' && message.id.trim().length > 0)));
0223 |    const id = messages.length === 1 && isRecord(first) && typeof first.id === 'string' && first.id.trim() ? first.id : null;
0224 |    const error = isRecord(payload.error) ? payload.error : null;
0225 |    const successIndicatorValid = payload.success === undefined || typeof payload.success === 'boolean';
0226 |    const contradictedFailure = payload.success === false;
0227 |    if (response.ok && successIndicatorValid && !contradictedFailure && !error && id) {
0228 |      return { outcome: 'ACCEPTED', externalMessageId: id };
0229 |    }
0230 |
0231 |    const refusalStatus = response.status === 400 || response.status === 401 || response.status === 403;
0232 |    const validGraphError = error !== null
0233 |      && typeof error.message === 'string' && error.message.length > 0
0234 |      && typeof error.code === 'number';
0235 |    const transientFieldValid = error && (error.is_transient === undefined || typeof error.is_transient === 'boolean');
0236 |    const contradictorySuccess = payload.success === true;
0237 |    const stableRefusal = validGraphError && transientFieldValid && error.is_transient !== true
0238 |      && [10, 100, 190].includes(error.code as number);
0239 |    if (refusalStatus && stableRefusal && successIndicatorValid && !contradictorySuccess
0240 |      && (payload.messages === undefined || messages.length === 0)) {
0241 |      return { outcome: 'REJECTED', code: 'META_RECUSOU' };
0242 |    }
0243 |    const validAckWithoutId = Array.isArray(payload.messages) && messages.length === 1
0244 |      && validMessageEnvelope && isRecord(first) && first.id === undefined;
0245 |    if (response.ok && successIndicatorValid && !contradictedFailure && !error && validAckWithoutId) {
0246 |      return { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'META_RECUSOU' };
0247 |    }
0248 |    return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
0249 |  }
0250 |
0251 |  private async request(path: string, accessToken?: string, method: 'GET' | 'POST' = 'GET', body?: unknown) {
0252 |    if (!this.graphVersionValida()) throw new MetaIndisponivelError('Versão Graph não configurada.');
0253 |    const headers: Record<string, string> = { accept: 'application/json' };
0254 |    if (accessToken) headers.authorization = `Bearer ${accessToken}`;
0255 |    if (body instanceof URLSearchParams) headers['content-type'] = 'application/x-www-form-urlencoded';
0256 |    else if (body !== undefined) headers['content-type'] = 'application/json';
0257 |    let response: Response;
0258 |    try {
0259 |      response = await fetch(`https://graph.facebook.com/${this.graphVersion}${path}`, {
0260 |        method, headers, body: body instanceof URLSearchParams ? body.toString() : body === undefined ? undefined : JSON.stringify(body),
0261 |        signal: AbortSignal.timeout(10_000), redirect: 'error',
0262 |      });
0263 |    } catch {
0264 |      throw new MetaIndisponivelError('A Meta está temporariamente indisponível.');
0265 |    }
0266 |    if (!response.ok) throw new MetaIndisponivelError('A Meta recusou a operação.');
0267 |    let payload: unknown;
0268 |    try {
0269 |      payload = await response.json();
0270 |    } catch {
0271 |      throw new MetaIndisponivelError('A resposta da Meta está temporariamente indisponível.');
0272 |    }
0273 |    if (!isRecord(payload)) throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0274 |    return payload;
0275 |  }
0276 |}
0277 |
0278 |function isRecord(value: unknown): value is Record<string, unknown> {
0279 |  return typeof value === 'object' && value !== null && !Array.isArray(value);
0280 |}
0281 |
0282 |function parseMetaDebugGrant(value: unknown): MetaDebugGrant {
0283 |  if (!isRecord(value) || typeof value.app_id !== 'string' || typeof value.is_valid !== 'boolean') {
0284 |    throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0285 |  }
0286 |  const scopes = value.scopes === undefined ? [] : parseStringArray(value.scopes);
0287 |  const rawGranularScopes = value.granular_scopes === undefined ? [] : value.granular_scopes;
0288 |  if (!Array.isArray(rawGranularScopes)) throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0289 |  const granularScopes = rawGranularScopes.map((entry): MetaGranularScope => {
0290 |    if (!isRecord(entry) || typeof entry.scope !== 'string' || entry.scope.length === 0) {
0291 |      throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0292 |    }
0293 |    const targetIds = entry.target_ids === undefined ? undefined : parseStringArray(entry.target_ids);
0294 |    return { scope: entry.scope, ...(targetIds === undefined ? {} : { targetIds }) };
0295 |  });
0296 |  return { appId: value.app_id, valid: value.is_valid, scopes, granularScopes };
0297 |}
0298 |
0299 |function parseStringArray(value: unknown): string[] {
0300 |  if (!Array.isArray(value) || value.some((item) => typeof item !== 'string')) {
0301 |    throw new MetaIndisponivelError('A resposta da Meta está estruturalmente inválida.');
0302 |  }
0303 |  return value;
0304 |}
0305 |
0306 |function wabaTargets(granular: MetaGranularScope[]): string[] {
0307 |  const byScope = new Map<string, Set<string>>();
0308 |  for (const item of granular) {
0309 |    if (!['whatsapp_business_management', 'whatsapp_business_messaging'].includes(item.scope)) continue;
0310 |    const targets = byScope.get(item.scope) ?? new Set<string>();
0311 |    for (const id of item.targetIds ?? []) if (/^\d{5,}$/.test(id)) targets.add(id);
0312 |    byScope.set(item.scope!, targets);
0313 |  }
0314 |  const management = byScope.get('whatsapp_business_management') ?? new Set<string>();
0315 |  const messaging = byScope.get('whatsapp_business_messaging') ?? new Set<string>();
0316 |  return [...management].filter((id) => messaging.has(id));
0317 |}
```

## Changed source api-app/test/channel-transport.e2e-spec.ts

```text
0001 |import { INestApplication } from '@nestjs/common';
0002 |import request from 'supertest';
0003 |import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from 'vitest';
0004 |import { PrismaService } from '../src/infra/prisma/prisma.service';
0005 |import { sealChannelCredential } from '../src/domain/channels/channel-credential-crypto';
0006 |import { OutboundService } from '../src/domain/inbox/outbound.service';
0007 |import { Channel, type ChannelSendResult, type TextMessage } from '../src/domain/channels/transport/channel';
0008 |import { ChannelAdapterFactory } from '../src/integrations/channels/channel-adapter-factory';
0009 |import { ChannelAdapterRegistry } from '../src/integrations/channels/channel-adapter-registry';
0010 |import type { ResolvedChannelCredential } from '../src/domain/channels/channel-credential-resolver';
0011 |import { MetaChannelFactory } from '../src/integrations/channels/meta-channel';
0012 |import { EvolutionChannelFactory } from '../src/integrations/channels/evolution-channel';
0013 |import { MetaHttpClient } from '../src/integrations/meta/meta.client';
0014 |import {
0015 |  contratarCanalNaoOficial, criarCanalVerificado, criarMantenedora, evolutionFake, limparBanco, login, metaFake, subirApp,
0016 |} from './helpers';
0017 |
0018 |class OpaqueRecipientChannel extends Channel {
0019 |  constructor(private readonly sent: TextMessage[]) { super(); }
0020 |  async sendMessage(message: TextMessage): Promise<ChannelSendResult> {
0021 |    this.sent.push(message);
0022 |    return { outcome: 'ACCEPTED', externalMessageId: `opaque-fake-${this.sent.length}` };
0023 |  }
0024 |}
0025 |
0026 |class OpaqueRecipientFactory extends ChannelAdapterFactory {
0027 |  readonly origin = 'OFICIAL' as const;
0028 |  constructor(private readonly sent: TextMessage[]) { super(); }
0029 |  locallyConfigured() { return true; }
0030 |  create() { return new OpaqueRecipientChannel(this.sent); }
0031 |}
0032 |
0033 |class MutatingMetaFactory extends ChannelAdapterFactory {
0034 |  readonly origin = 'OFICIAL' as const;
0035 |  private readonly delegate = new MetaChannelFactory(metaFake);
0036 |  constructor(private readonly mutateBeforeFence: () => Promise<void>) { super(); }
0037 |  locallyConfigured() { return this.delegate.locallyConfigured(); }
0038 |  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>) {
0039 |    return this.delegate.create(credential, async () => {
0040 |      await this.mutateBeforeFence();
0041 |      return beforeDispatch();
0042 |    });
0043 |  }
0044 |}
0045 |
0046 |class MutatingEvolutionFactory extends ChannelAdapterFactory {
0047 |  readonly origin = 'NAO_OFICIAL' as const;
0048 |  private readonly delegate = new EvolutionChannelFactory(evolutionFake);
0049 |  constructor(private readonly mutateBeforeFence: () => Promise<void>) { super(); }
0050 |  locallyConfigured() { return this.delegate.locallyConfigured(); }
0051 |  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>) {
0052 |    return this.delegate.create(credential, async () => {
0053 |      await this.mutateBeforeFence();
0054 |      return beforeDispatch();
0055 |    });
0056 |  }
0057 |}
0058 |
0059 |describe('common Channel outbound (PostgreSQL)', () => {
0060 |  let app: INestApplication;
0061 |  let prisma: PrismaService;
0062 |  let buId: string;
0063 |  let conversationId: string;
0064 |  let identityId: string;
0065 |  let cookie: string;
0066 |
0067 |  beforeAll(async () => { ({ app, prisma } = await subirApp()); });
0068 |  beforeEach(async () => {
0069 |    await limparBanco(prisma);
0070 |    const tenant = await criarMantenedora(app, 'Channel outbound fixture', 'channel-outbound@example.test');
0071 |    buId = tenant.businessUnit.id;
0072 |    const binding = await criarCanalVerificado(prisma, buId, 'OFICIAL', '987654321', { requiresWindow: false });
0073 |    identityId = binding.identity.id;
0074 |    const conversation = await prisma.conversation.create({ data: {
0075 |      buId, contact: 'user:opaque', contactType: 'PESSOA', displayName: 'Opaque recipient', status: 'QUEUED',
0076 |    } });
0077 |    conversationId = conversation.id;
0078 |    cookie = await login(app, 'channel-outbound@example.test');
0079 |  });
0080 |  afterAll(async () => { if (prisma) await limparBanco(prisma); await app?.close(); });
0081 |
0082 |  it('sends a trusted opaque recipient through one bound adapter and finalizes without stealing a later owner', async () => {
0083 |    const gate = await prisma.conversation.update({ where: { id: conversationId }, data: {
0084 |      status: 'IN_SERVICE', attendantName: 'Claim before send', attendantOrigin: 'INTERNO',
0085 |    } });
0086 |    const response = await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0087 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'opaque recipient test' }).expect(201);
0088 |    expect(response.body).toMatchObject({ canal: 'OFICIAL' });
0089 |    expect(metaFake.enviados).toEqual([{ para: 'user:opaque', texto: 'opaque recipient test' }]);
0090 |    const message = await prisma.message.findFirstOrThrow({ where: { conversationId, direction: 'OUT' } });
0091 |    expect(message).toMatchObject({ externalId: expect.any(String), content: 'opaque recipient test', authorUserId: expect.any(String) });
0092 |    const finalized = await prisma.conversation.findUniqueOrThrow({ where: { id: gate.id } });
0093 |    expect(finalized).toMatchObject({ attendantName: 'Claim before send', attendantOrigin: 'INTERNO' });
0094 |  });
0095 |
0096 |  it('runs an opaque user recipient through an independent Channel fake and never calls provider clients', async () => {
0097 |    const sent: TextMessage[] = [];
0098 |    const registry = new ChannelAdapterRegistry([new OpaqueRecipientFactory(sent)]);
0099 |    const isolated = await subirApp(registry);
0100 |    try {
0101 |      await limparBanco(isolated.prisma);
0102 |      const tenant = await criarMantenedora(isolated.app, 'Opaque fake contract', 'opaque-fake@example.test');
0103 |      const localBuId = tenant.businessUnit.id;
0104 |      await criarCanalVerificado(isolated.prisma, localBuId, 'OFICIAL', 'opaque-fake-resource', { requiresWindow: false });
0105 |      const localConversation = await isolated.prisma.conversation.create({ data: {
0106 |        buId: localBuId, contact: 'user:opaque', contactType: 'PESSOA', displayName: 'Opaque fake recipient', status: 'QUEUED',
0107 |      } });
0108 |      const localCookie = await login(isolated.app, 'opaque-fake@example.test');
0109 |      await request(isolated.app.getHttpServer()).post(`/api/bff/conversations/${localConversation.id}/messages`)
0110 |        .set('Cookie', localCookie).set('x-requested-with', 'teste').send({ texto: 'wire-independent fake' }).expect(201);
0111 |      expect(sent).toEqual([{ kind: 'text', recipientRef: 'user:opaque', text: 'wire-independent fake' }]);
0112 |      expect(metaFake.enviados).toHaveLength(0);
0113 |      expect(evolutionFake.enviados).toHaveLength(0);
0114 |      expect(await isolated.prisma.message.count({ where: { conversationId: localConversation.id, direction: 'OUT' } })).toBe(1);
0115 |    } finally {
0116 |      await limparBanco(isolated.prisma);
0117 |      await isolated.app.close();
0118 |    }
0119 |  });
0120 |
0121 |  it('blocks real binding changes inside Meta/Evolution adapter pre-dispatch callbacks', async () => {
0122 |    const cases = [
0123 |      { provider: 'OFICIAL' as const, changed: 'generation' as const },
0124 |      { provider: 'OFICIAL' as const, changed: 'pairingEpoch' as const },
0125 |      { provider: 'OFICIAL' as const, changed: 'credentialVersion' as const },
0126 |      { provider: 'NAO_OFICIAL' as const, changed: 'generation' as const },
0127 |      { provider: 'NAO_OFICIAL' as const, changed: 'pairingEpoch' as const },
0128 |    ];
0129 |    for (const { provider, changed } of cases) {
0130 |      let mutate!: () => Promise<void>;
0131 |      const previousModuleSwitch = process.env.LH_CHANNEL_UNOFFICIAL;
0132 |      if (provider === 'NAO_OFICIAL') process.env.LH_CHANNEL_UNOFFICIAL = 'true';
0133 |      const registry = new ChannelAdapterRegistry([provider === 'OFICIAL'
0134 |        ? new MutatingMetaFactory(() => mutate())
0135 |        : new MutatingEvolutionFactory(() => mutate())]);
0136 |      const isolated = await subirApp(registry);
0137 |      try {
0138 |        await limparBanco(isolated.prisma);
0139 |        const tenant = await criarMantenedora(isolated.app, `Pre-dispatch ${changed}`, `pre-dispatch-${changed}@example.test`);
0140 |        if (provider === 'NAO_OFICIAL') {
0141 |          await contratarCanalNaoOficial(isolated.prisma, tenant.mantenedora.id);
0142 |        }
0143 |        const localBinding = await criarCanalVerificado(isolated.prisma, tenant.businessUnit.id, provider,
0144 |          `pre-dispatch-${provider}-${changed}`, { requiresWindow: false });
0145 |        const localConversation = await isolated.prisma.conversation.create({ data: {
0146 |          buId: tenant.businessUnit.id, contact: `user:opaque-${provider}-${changed}`, contactType: 'PESSOA', status: 'QUEUED',
0147 |        } });
0148 |        const localCookie = await login(isolated.app, `pre-dispatch-${changed}@example.test`);
0149 |        let changedOnce = false;
0150 |        mutate = async () => {
0151 |          if (changedOnce) return;
0152 |          changedOnce = true;
0153 |          if (changed === 'generation') {
0154 |            await isolated.prisma.buChannel.update({ where: { id: localBinding.channel.id }, data: { generation: { increment: 1 } } });
0155 |          } else if (changed === 'pairingEpoch') {
0156 |            await isolated.prisma.buChannel.update({ where: { id: localBinding.channel.id }, data: { pairingEpoch: { increment: 1 } } });
0157 |          } else {
0158 |            await isolated.prisma.channelCredential.update({ where: { channelId: localBinding.channel.id }, data: { version: { increment: 1 } } });
0159 |          }
0160 |        };
0161 |        const metaCallsBefore = metaFake.providerCalls;
0162 |        const evolutionCallsBefore = evolutionFake.providerCalls;
0163 |        await request(isolated.app.getHttpServer()).post(`/api/bff/conversations/${localConversation.id}/messages`)
0164 |          .set('Cookie', localCookie).set('x-requested-with', 'teste').send({ texto: `blocked ${changed}` })
0165 |          .expect(409).expect(({ body }) => expect(body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' }));
0166 |        expect(await isolated.prisma.message.count({ where: { conversationId: localConversation.id, direction: 'OUT' } })).toBe(0);
0167 |        expect(metaFake.providerCalls).toBe(metaCallsBefore);
0168 |        expect(evolutionFake.providerCalls).toBe(evolutionCallsBefore);
0169 |      } finally {
0170 |        await limparBanco(isolated.prisma);
0171 |        await isolated.app.close();
0172 |        if (previousModuleSwitch === undefined) delete process.env.LH_CHANNEL_UNOFFICIAL;
0173 |        else process.env.LH_CHANNEL_UNOFFICIAL = previousModuleSwitch;
0174 |      }
0175 |    }
0176 |  });
0177 |
0178 |  it('persists nothing for contradictory successful Meta envelopes', async () => {
0179 |    process.env.GRAPH_VERSION = 'v26.0';
0180 |    const fetchFake = vi.fn()
0181 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ success: false, messages: [{ id: 'contradictory' }] }) })
0182 |      .mockResolvedValueOnce({ ok: true, status: 200, json: async () => ({ success: false, messages: [{}] }) });
0183 |    vi.stubGlobal('fetch', fetchFake);
0184 |    const isolated = await subirApp(new ChannelAdapterRegistry([new MetaChannelFactory(new MetaHttpClient())]));
0185 |    try {
0186 |      await limparBanco(isolated.prisma);
0187 |      const tenant = await criarMantenedora(isolated.app, 'Contradictory Meta ACK', 'contradictory-meta@example.test');
0188 |      await criarCanalVerificado(isolated.prisma, tenant.businessUnit.id, 'OFICIAL', 'contradictory-meta-resource', { requiresWindow: false });
0189 |      const conversation = await isolated.prisma.conversation.create({ data: {
0190 |        buId: tenant.businessUnit.id, contact: 'user:opaque', contactType: 'PESSOA', status: 'QUEUED',
0191 |      } });
0192 |      const session = await login(isolated.app, 'contradictory-meta@example.test');
0193 |      for (let requestIndex = 1; requestIndex <= 2; requestIndex += 1) {
0194 |        await request(isolated.app.getHttpServer()).post(`/api/bff/conversations/${conversation.id}/messages`)
0195 |          .set('Cookie', session).set('x-requested-with', 'teste').send({ texto: `contradictory result ${requestIndex}` })
0196 |          .expect(400).expect(({ body }) => expect(body).toMatchObject({
0197 |            outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED',
0198 |          }));
0199 |        expect((await request(isolated.app.getHttpServer()).get(`/api/bff/conversations/${conversation.id}/messages`)
0200 |          .set('Cookie', session)).body.messages.filter((message: { direction: string }) => message.direction === 'OUT')).toHaveLength(0);
0201 |        expect(fetchFake).toHaveBeenCalledTimes(requestIndex);
0202 |        expect(await isolated.prisma.message.count({ where: { conversationId: conversation.id, direction: 'OUT' } })).toBe(0);
0203 |      }
0204 |    } finally {
0205 |      vi.unstubAllGlobals();
0206 |      await limparBanco(isolated.prisma);
0207 |      await isolated.app.close();
0208 |    }
0209 |  });
0210 |
0211 |  it('requires BFF session and CSRF and rejects a foreign-account public send before dispatch', async () => {
0212 |    const sentBefore = metaFake.enviados.length;
0213 |    const outgoingBefore = await prisma.message.count({ where: { conversationId, direction: 'OUT' } });
0214 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0215 |      .send({ texto: 'without session' }).expect(401);
0216 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0217 |      .set('Cookie', cookie).send({ texto: 'without CSRF header' }).expect(403);
0218 |
0219 |    const foreign = await criarMantenedora(app, 'Foreign public destination', 'foreign-public-destination@example.test');
0220 |    const foreignCookie = await login(app, 'foreign-public-destination@example.test');
0221 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0222 |      .set('Cookie', foreignCookie).set('x-requested-with', 'teste').send({ texto: 'valid session without BU grant' }).expect(404);
0223 |    const key = await request(app.getHttpServer()).post('/api/bff/integracao/api-keys').set('Cookie', cookie)
0224 |      .set('x-requested-with', 'teste').send({ nome: 'Scoped channel key', buIds: [buId] }).expect(201);
0225 |    await request(app.getHttpServer()).post('/api/v1/messages').set('Authorization', `Bearer ${key.body.chave}`)
0226 |      .send({ account_id: foreign.businessUnit.id, telefone: 'user:opaque', texto: 'foreign API key send' })
0227 |      .expect(403).expect(({ body }) => expect(body.code).toBe('SEM_ACESSO_A_CONTA'));
0228 |    expect(metaFake.enviados).toHaveLength(sentBefore);
0229 |    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(outgoingBefore);
0230 |    expect(evolutionFake.enviados).toHaveLength(0);
0231 |  });
0232 |
0233 |  it('holds two tenants in flight with distinct scoped resources and credentials', async () => {
0234 |    const tenantB = await criarMantenedora(app, 'Parallel tenant B', 'parallel-tenant-b@example.test');
0235 |    const channelA = await prisma.buChannel.findFirstOrThrow({ where: { buId, type: 'OFICIAL' } });
0236 |    const bindingA = {
0237 |      channel: channelA,
0238 |      identity: await prisma.providerResourceIdentity.findFirstOrThrow({ where: { currentChannelId: channelA.id } }),
0239 |    };
0240 |    const bindingB = await criarCanalVerificado(prisma, tenantB.businessUnit.id, 'OFICIAL', 'parallel-resource-b', { requiresWindow: false });
0241 |    const credentialA = await prisma.channelCredential.findUniqueOrThrow({ where: { channelId: bindingA.channel.id } });
0242 |    const credentialB = await prisma.channelCredential.findUniqueOrThrow({ where: { channelId: bindingB.channel.id } });
0243 |    const key = Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY!, 'base64');
0244 |    const tokenA = 'tenant-a-distinct-scoped-token';
0245 |    const tokenB = 'tenant-b-distinct-scoped-token';
0246 |    for (const [binding, credential, token] of [[bindingA, credentialA, tokenA], [bindingB, credentialB, tokenB]] as const) {
0247 |      const envelope = sealChannelCredential(token, credential.keyId, key, {
0248 |        purpose: 'active', provider: 'OFICIAL', buId: binding.channel.buId,
0249 |        channelId: binding.channel.id, generation: binding.channel.generation, version: credential.version,
0250 |      });
0251 |      await prisma.channelCredential.update({ where: { channelId: binding.channel.id }, data: {
0252 |        nonce: new Uint8Array(envelope.nonce), ciphertext: new Uint8Array(envelope.ciphertext), tag: new Uint8Array(envelope.tag),
0253 |      } });
0254 |      metaFake.credentialByPhone.set(binding.channel.phoneNumberId!, token);
0255 |    }
0256 |    const conversationA = await prisma.conversation.create({ data: {
0257 |      buId, contact: 'user:tenant-a', contactType: 'PESSOA', status: 'QUEUED',
0258 |    } });
0259 |    const conversationB = await prisma.conversation.create({ data: {
0260 |      buId: tenantB.businessUnit.id, contact: 'user:tenant-b', contactType: 'PESSOA', status: 'QUEUED',
0261 |    } });
0262 |    const cookieB = await login(app, 'parallel-tenant-b@example.test');
0263 |    let arrived = 0;
0264 |    let markBothEntered!: () => void;
0265 |    let releaseBoth!: () => void;
0266 |    const bothEntered = new Promise<void>((resolve) => { markBothEntered = resolve; });
0267 |    const held = new Promise<void>((resolve) => { releaseBoth = resolve; });
0268 |    metaFake.sendHook = async () => { arrived += 1; if (arrived === 2) markBothEntered(); await held; };
0269 |    const pendingA = request(app.getHttpServer()).post(`/api/bff/conversations/${conversationA.id}/messages`)
0270 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'tenant A parallel' }).then((response) => response);
0271 |    const pendingB = request(app.getHttpServer()).post(`/api/bff/conversations/${conversationB.id}/messages`)
0272 |      .set('Cookie', cookieB).set('x-requested-with', 'teste').send({ texto: 'tenant B parallel' }).then((response) => response);
0273 |    await bothEntered;
0274 |    expect(metaFake.credentialCalls.map(({ phoneNumberId, accessToken }) => ({ phoneNumberId, accessToken })).sort((a, b) => a.phoneNumberId.localeCompare(b.phoneNumberId)))
0275 |      .toEqual([
0276 |        { phoneNumberId: channelA.phoneNumberId!, accessToken: tokenA },
0277 |        { phoneNumberId: 'parallel-resource-b', accessToken: tokenB },
0278 |      ]);
0279 |    releaseBoth();
0280 |    const [responseA, responseB] = await Promise.all([pendingA, pendingB]);
0281 |    expect(responseA.status).toBe(201);
0282 |    expect(responseB.status).toBe(201);
0283 |    const [messageA, messageB] = await Promise.all([
0284 |      prisma.message.findFirstOrThrow({ where: { conversationId: conversationA.id, direction: 'OUT' } }),
0285 |      prisma.message.findFirstOrThrow({ where: { conversationId: conversationB.id, direction: 'OUT' } }),
0286 |    ]);
0287 |    expect(messageA).toMatchObject({ buId, providerResourceIdentityId: bindingA.identity.id, channelOrigin: 'OFICIAL', content: 'tenant A parallel' });
0288 |    expect(messageB).toMatchObject({ buId: tenantB.businessUnit.id, providerResourceIdentityId: bindingB.identity.id, channelOrigin: 'OFICIAL', content: 'tenant B parallel' });
0289 |    expect(metaFake.enviados).toEqual(expect.arrayContaining([
0290 |      { para: 'user:tenant-a', texto: 'tenant A parallel' },
0291 |      { para: 'user:tenant-b', texto: 'tenant B parallel' },
0292 |    ]));
0293 |  });
0294 |
0295 |  it('reports ambiguous bindings and blocks before the provider call', async () => {
0296 |    await criarCanalVerificado(prisma, buId, 'NAO_OFICIAL', `outbound-evolution-${Date.now()}`, { requiresWindow: false });
0297 |    const thread = await request(app.getHttpServer()).get(`/api/bff/conversations/${conversationId}/messages`)
0298 |      .set('Cookie', cookie).expect(200);
0299 |    expect(thread.body.janela).toMatchObject({ disponivel: false, motivo: 'CANAL_AMBIGUO', canal: null });
0300 |    const before = metaFake.enviados.length;
0301 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0302 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'must not send' })
0303 |      .expect(409).expect(({ body }) => expect(body).toMatchObject({ code: 'CANAL_AMBIGUO', outcome: 'BLOCKED' }));
0304 |    expect(metaFake.enviados).toHaveLength(before);
0305 |  });
0306 |
0307 |  it('preserves a BFF claim acquired after the provider accepted an in-flight send', async () => {
0308 |    let markEntered!: () => void;
0309 |    let releaseSend!: () => void;
0310 |    const entered = new Promise<void>((resolve) => { markEntered = resolve; });
0311 |    const held = new Promise<void>((resolve) => { releaseSend = resolve; });
0312 |    metaFake.sendHook = async () => { markEntered(); await held; };
0313 |    const pending = request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0314 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'claim during BFF send' }).then((response) => response);
0315 |    await entered;
0316 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/claim`)
0317 |      .set('Cookie', cookie).set('x-requested-with', 'teste').expect(201);
0318 |    releaseSend();
0319 |    const response = await pending;
0320 |    expect(response.status).toBe(201);
0321 |    const claimed = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
0322 |    expect(claimed).toMatchObject({ status: 'IN_SERVICE', attendantOrigin: 'INTERNO', attendantUserId: expect.any(String) });
0323 |  });
0324 |
0325 |  it('gives a detected identity change precedence after dispatch and creates no new Message', async () => {
0326 |    metaFake.sendHook = async () => {
0327 |      await prisma.providerResourceIdentity.update({ where: { id: identityId }, data: { currentChannelId: null, retiredAt: new Date() } });
0328 |    };
0329 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0330 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'dispatch raced retirement' })
0331 |      .expect(409).expect(({ body }) => expect(body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState: 'UNCONFIRMED' }));
0332 |    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(0);
0333 |    expect(metaFake.enviados).toHaveLength(1);
0334 |  });
0335 |
0336 |  it('does not record the null-ID diagnostic when a PostgreSQL identity fence changes during dispatch', async () => {
0337 |    metaFake.sendIdNull = true;
0338 |    metaFake.sendHook = async () => {
0339 |      await prisma.providerResourceIdentity.update({ where: { id: identityId }, data: { currentChannelId: null, retiredAt: new Date() } });
0340 |    };
0341 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0342 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'unknown response raced retirement' })
0343 |      .expect(409).expect(({ body }) => expect(body).toMatchObject({
0344 |        code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', diagnosticPersistence: 'UNCONFIRMED',
0345 |      }));
0346 |    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(0);
0347 |    expect(metaFake.enviados).toHaveLength(1);
0348 |  });
0349 |
0350 |  it('fences a held send after a real same-resource REAUTORIZAR generation change', async () => {
0351 |    let markEntered!: () => void;
0352 |    let releaseSend!: () => void;
0353 |    const entered = new Promise<void>((resolve) => { markEntered = resolve; });
0354 |    const held = new Promise<void>((resolve) => { releaseSend = resolve; });
0355 |    metaFake.sendHook = async () => { markEntered(); await held; };
0356 |    const pending = request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0357 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'held across reauthorization' }).then((response) => response);
0358 |    await entered;
0359 |
0360 |    const created = await request(app.getHttpServer()).post('/api/bff/number-registrations')
0361 |      .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', '0f0f0f0f-0f0f-4f0f-8f0f-0f0f0f0f0f0f')
0362 |      .send({ buId, tipo: 'OFICIAL', operation: 'REAUTORIZAR', channelId: (await prisma.buChannel.findFirstOrThrow({ where: { buId, type: 'OFICIAL' } })).id, expectedGeneration: 1 })
0363 |      .expect(201);
0364 |    await request(app.getHttpServer()).post(`/api/bff/number-registrations/${created.body.attempt.id}/authorize`)
0365 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ nonce: created.body.nonce, code: 'fixture-held-send-reauthorize' }).expect(200);
0366 |    await request(app.getHttpServer()).post(`/api/bff/number-registrations/${created.body.attempt.id}/confirm`)
0367 |      .set('Cookie', cookie).set('x-requested-with', 'teste')
0368 |      .send({ wabaId: '123456789', phoneNumberId: '987654321', modoRegistro: 'JA_REGISTRADO', after: 'fixture-page-1' }).expect(200);
0369 |    releaseSend();
0370 |
0371 |    const response = await pending;
0372 |    expect(response.status).toBe(409);
0373 |    expect(response.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState: 'UNCONFIRMED' });
0374 |    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT' } })).toBe(0);
0375 |    expect(await prisma.buChannel.findFirstOrThrow({ where: { id: (await prisma.buChannel.findFirstOrThrow({ where: { buId, type: 'OFICIAL' } })).id } }))
0376 |      .toMatchObject({ generation: 2 });
0377 |  });
0378 |
0379 |  it('accepts a held acknowledged send when only the active credential version rotates', async () => {
0380 |    let markEntered!: () => void;
0381 |    let releaseSend!: () => void;
0382 |    const entered = new Promise<void>((resolve) => { markEntered = resolve; });
0383 |    const held = new Promise<void>((resolve) => { releaseSend = resolve; });
0384 |    metaFake.sendHook = async () => { markEntered(); await held; };
0385 |    const pending = request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0386 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'held across credential rotation' }).then((response) => response);
0387 |    await entered;
0388 |
0389 |    const channel = await prisma.buChannel.findFirstOrThrow({ where: { buId, type: 'OFICIAL' } });
0390 |    const prior = await prisma.channelCredential.findUniqueOrThrow({ where: { channelId: channel.id } });
0391 |    const key = Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY!, 'base64');
0392 |    const nextVersion = prior.version + 1;
0393 |    const envelope = sealChannelCredential('fixture-scoped-token', prior.keyId, key, {
0394 |      purpose: 'active', provider: 'OFICIAL', buId, channelId: channel.id, generation: channel.generation, version: nextVersion,
0395 |    });
0396 |    await prisma.channelCredential.update({ where: { channelId: channel.id }, data: {
0397 |      version: nextVersion, nonce: new Uint8Array(envelope.nonce), ciphertext: new Uint8Array(envelope.ciphertext), tag: new Uint8Array(envelope.tag),
0398 |    } });
0399 |    releaseSend();
0400 |
0401 |    const response = await pending;
0402 |    expect(response.status).toBe(201);
0403 |    expect(await prisma.message.count({ where: { conversationId, direction: 'OUT', externalId: 'wamid-enviado-1' } })).toBe(1);
0404 |    expect(await prisma.buChannel.findUniqueOrThrow({ where: { id: channel.id } })).toMatchObject({ generation: channel.generation, pairingEpoch: channel.pairingEpoch });
0405 |    expect(await prisma.providerResourceIdentity.findUniqueOrThrow({ where: { id: identityId } })).toMatchObject({ currentChannelId: channel.id, buId });
0406 |  });
0407 |
0408 |  it('keeps verified bot ingress pinned when a different channel origin becomes the latest message', async () => {
0409 |    const evolution = await criarCanalVerificado(prisma, buId, 'NAO_OFICIAL', `outbound-evolution-${Date.now()}`, { requiresWindow: false });
0410 |    await prisma.message.create({ data: {
0411 |      id: 'latest-other-origin', conversationId, buId, direction: 'IN', messageType: 'TEXTO', content: 'other origin arrived later',
0412 |      channelOrigin: 'NAO_OFICIAL', providerResourceIdentityId: evolution.identity.id, externalId: 'fixture-other-origin', status: 'RECEBIDA',
0413 |    } });
0414 |    const channel = await prisma.buChannel.findFirstOrThrow({ where: { buId, type: 'OFICIAL' } });
0415 |    const outbound = app.get(OutboundService);
0416 |    await outbound.send({
0417 |      conversationId, buId, text: 'pinned bot reply', attribution: { kind: 'BOT', name: 'Typebot' },
0418 |      ingress: {
0419 |        channelId: channel.id, providerResourceIdentityId: identityId, channelOrigin: 'OFICIAL',
0420 |        generation: channel.generation, pairingEpoch: channel.pairingEpoch,
0421 |      },
0422 |    });
0423 |    expect(metaFake.enviados).toEqual([{ para: 'user:opaque', texto: 'pinned bot reply' }]);
0424 |    expect(evolutionFake.enviados).toHaveLength(0);
0425 |  });
0426 |
0427 |  it('breaks equal-timestamp origin ties deterministically by descending message id', async () => {
0428 |    await criarCanalVerificado(prisma, buId, 'NAO_OFICIAL', `outbound-tie-evolution-${Date.now()}`, { requiresWindow: false });
0429 |    const sameTime = new Date('2026-10-20T12:00:00.000Z');
0430 |    await prisma.message.createMany({ data: [
0431 |      { id: 'channel-tie-a', conversationId, buId, direction: 'IN', messageType: 'TEXTO', content: 'official tie', channelOrigin: 'OFICIAL', status: 'RECEBIDA', createdAt: sameTime },
0432 |      { id: 'channel-tie-z', conversationId, buId, direction: 'IN', messageType: 'TEXTO', content: 'evolution tie', channelOrigin: 'NAO_OFICIAL', status: 'RECEBIDA', createdAt: sameTime },
0433 |    ] });
0434 |    await request(app.getHttpServer()).post(`/api/bff/conversations/${conversationId}/messages`)
0435 |      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ texto: 'tie winner' }).expect(201);
0436 |    expect(evolutionFake.enviados).toEqual([{ para: 'user:opaque', texto: 'tie winner' }]);
0437 |    expect(metaFake.enviados).toHaveLength(0);
0438 |  });
0439 |
0440 |  it('rejects cross-BU and mismatched verified-ingress bindings before dispatch', async () => {
0441 |    const setor = await prisma.setor.findFirstOrThrow({ where: { mantenedoraId: (await prisma.businessUnit.findUniqueOrThrow({ where: { id: buId } })).mantenedoraId } });
0442 |    const foreign = await prisma.businessUnit.create({
0443 |      data: { mantenedoraId: setor.mantenedoraId, setorId: setor.id, name: 'Foreign channel BU' },
0444 |    });
0445 |    const foreignChannel = await criarCanalVerificado(prisma, foreign.id, 'OFICIAL', 'foreign-resource-transport', { requiresWindow: false });
0446 |    const outbound = app.get(OutboundService);
0447 |    await expect(outbound.send({
0448 |      conversationId, buId, text: 'wrong BU', attribution: { kind: 'BOT', name: 'Typebot' },
0449 |      ingress: {
0450 |        channelId: foreignChannel.channel.id, providerResourceIdentityId: foreignChannel.identity.id, channelOrigin: 'OFICIAL',
0451 |        generation: foreignChannel.channel.generation, pairingEpoch: foreignChannel.channel.pairingEpoch,
0452 |      },
0453 |    })).rejects.toMatchObject({ status: 409, response: { code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' } });
0454 |    await expect(outbound.send({
0455 |      conversationId, buId, text: 'wrong identity', attribution: { kind: 'BOT', name: 'Typebot' },
0456 |      ingress: {
0457 |        channelId: (await prisma.buChannel.findFirstOrThrow({ where: { buId, type: 'OFICIAL' } })).id,
0458 |        providerResourceIdentityId: foreignChannel.identity.id, channelOrigin: 'OFICIAL', generation: 1, pairingEpoch: 0,
0459 |      },
0460 |    })).rejects.toMatchObject({ status: 409, response: { code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' } });
0461 |    expect(metaFake.enviados).toHaveLength(0);
0462 |  });
0463 |
0464 |  it('preserves a human BFF claim that overlaps a public API accepted send', async () => {
0465 |    const phone = '5584999912345';
0466 |    const conversation = await prisma.conversation.create({ data: { buId, contact: phone, contactType: 'PESSOA', status: 'QUEUED' } });
0467 |    await prisma.message.create({ data: {
0468 |      conversationId: conversation.id, buId, direction: 'IN', messageType: 'TEXTO', content: 'public inbound', channelOrigin: 'OFICIAL',
0469 |      status: 'RECEBIDA',
0470 |    } });
0471 |    const key = await request(app.getHttpServer()).post('/api/bff/integracao/api-keys').set('Cookie', cookie)
0472 |      .set('x-requested-with', 'teste').send({ nome: 'Channel overlap key', buIds: [buId] }).expect(201);
0473 |    metaFake.sendHook = async () => {
0474 |      await request(app.getHttpServer()).post(`/api/bff/conversations/${conversation.id}/claim`)
0475 |        .set('Cookie', cookie).set('x-requested-with', 'teste').expect(201);
0476 |    };
0477 |    await request(app.getHttpServer()).post('/api/v1/messages').set('Authorization', `Bearer ${key.body.chave}`)
0478 |      .send({ account_id: buId, telefone: phone, texto: 'public outbound during claim' }).expect(201);
0479 |    const claimed = await prisma.conversation.findUniqueOrThrow({ where: { id: conversation.id } });
0480 |    expect(claimed).toMatchObject({ status: 'IN_SERVICE', attendantUserId: expect.any(String), attendantOrigin: 'INTERNO' });
0481 |    expect(claimed.attendantName).toBeTruthy();
0482 |  });
0483 |
0484 |  it('completes five real-PostgreSQL rounds of twenty overlapping sends with one accepted Message each', async () => {
0485 |    const operationsPerRound = 20;
0486 |    const operationCounts: number[] = [];
0487 |    const acceptedCounts: number[] = [];
0488 |    const recordedCounts: number[] = [];
0489 |    for (let round = 0; round < 5; round += 1) {
0490 |      const conversations = await Promise.all(Array.from({ length: operationsPerRound }, (_, index) => prisma.conversation.create({ data: {
0491 |        buId, contact: `user:opaque-${round}-${index}`, contactType: 'PESSOA', status: 'QUEUED',
0492 |      } })));
0493 |      let arrivals = 0;
0494 |      let markBarrier!: () => void;
0495 |      let release!: () => void;
0496 |      const barrier = new Promise<void>((resolve) => { markBarrier = resolve; });
0497 |      const gate = new Promise<void>((resolve) => { release = resolve; });
0498 |      metaFake.sendHook = async () => {
0499 |        arrivals += 1;
0500 |        if (arrivals === operationsPerRound) markBarrier();
0501 |        await gate;
0502 |      };
0503 |      const pending = conversations.map((conversation, index) => request(app.getHttpServer())
0504 |        .post(`/api/bff/conversations/${conversation.id}/messages`).set('Cookie', cookie).set('x-requested-with', 'teste')
0505 |        .send({ texto: `round ${round} outbound ${index}` }).then((response) => response));
0506 |      await barrier;
0507 |      release();
0508 |      const responses = await Promise.all(pending);
0509 |      metaFake.sendHook = null;
0510 |      const accepted = responses.filter((response) => response.status === 201).length;
0511 |      const recorded = await prisma.message.count({ where: { conversationId: { in: conversations.map(({ id }) => id) }, direction: 'OUT' } });
0512 |      operationCounts.push(responses.length);
0513 |      acceptedCounts.push(accepted);
0514 |      recordedCounts.push(recorded);
0515 |      expect(accepted).toBe(operationsPerRound);
0516 |      expect(recorded).toBe(operationsPerRound);
0517 |    }
0518 |    console.log(`[CHANNEL-OUTBOUND-OVERLAP]${JSON.stringify({ repetitions: 5, operationsPerRepetition: operationsPerRound, operationCounts, acceptedCounts, recordedCounts, limits: 'Disposable PostgreSQL and provider fake; concurrent integrity observation, not capacity/SLO evidence.' })}`);
0519 |  });
0520 |});
```

## Unchanged critical context api-app/test/timeline-fixtures.cjs

```text
0001 |const http = require('node:http');
0002 |const { createHmac } = require('node:crypto');
0003 |const bcrypt = require('bcryptjs');
0004 |const { PrismaClient } = require('@prisma/client');
0005 |const { sealChannelCredential } = require('../dist/domain/channels/channel-credential-crypto.js');
0006 |
0007 |const databaseUrl = process.env.DATABASE_URL;
0008 |const dedicatedUrl = process.env.LEADSHUG_E2E_DATABASE_URL;
0009 |const fixturePort = Number(process.env.LEADSHUG_FIXTURE_PORT ?? '3101');
0010 |const apiPort = Number(process.env.LEADSHUG_API_PORT ?? '3100');
0011 |const providerInventory = new Map();
0012 |const fixtureConversationIds = new Set();
0013 |// Stateful provider-only controls for the real-BFF number-onboarding browser lane.
0014 |// No browser-visible API response is synthesized here; browser requests still
0015 |// traverse Nest, session/CSRF, policy, and PostgreSQL.
0016 |const onboarding = {
0017 |  resources: [], calls: [], effects: [], failures: {}, holds: {}, holdsAfter: {}, ambiguousAfter: {}, releases: {},
0018 |  meta: { codeTokens: {}, grants: {}, pages: {}, sendMode: 'accepted' },
0019 |  evolution: { inventory: {}, outcomes: {} },
0020 |};
0021 |const barriers = new Map();
0022 |function barrier(name) {
0023 |  if (!barriers.has(name)) {
0024 |    let release;
0025 |    const promise = new Promise((resolve) => { release = resolve; });
0026 |    barriers.set(name, { promise, release });
0027 |  }
0028 |  return barriers.get(name);
0029 |}
0030 |async function providerCall(operation, args = {}) {
0031 |  const call = { operation, at: Date.now(), ...args };
0032 |  onboarding.calls.push(call);
0033 |  const failure = onboarding.failures[operation];
0034 |  if (failure) { if (failure.remaining > 0) failure.remaining--; if (!failure.remaining) delete onboarding.failures[operation]; throw new Error(failure.message || 'controlled provider failure'); }
0035 |  if (onboarding.holds[operation]) await barrier(`${operation}:${onboarding.holds[operation]}`).promise;
0036 |  return call;
0037 |}
0038 |async function providerEffect(operation, args = {}) {
0039 |  const effect = { operation, at: Date.now(), ...args };
0040 |  onboarding.effects.push(effect);
0041 |  if (onboarding.holdsAfter[operation]) await barrier(`${operation}:${onboarding.holdsAfter[operation]}`).promise;
0042 |  const ambiguous = onboarding.ambiguousAfter[operation];
0043 |  if (ambiguous && ambiguous.remaining > 0) {
0044 |    ambiguous.remaining--;
0045 |    if (ambiguous.remaining === 0) delete onboarding.ambiguousAfter[operation];
0046 |    throw new Error('controlled response lost after provider effect');
0047 |  }
0048 |  return effect;
0049 |}
0050 |if (!databaseUrl || databaseUrl !== dedicatedUrl) throw new Error('Fixtures exigem DATABASE_URL igual ao banco descartável de E2E.');
0051 |if (!new URL(databaseUrl).pathname.slice(1).split('?')[0].startsWith('leadshug_timeline_')) throw new Error('Fixtures aceitam apenas banco leadshug_timeline_* descartável.');
0052 |
0053 |const prisma = new PrismaClient({ datasources: { db: { url: databaseUrl } } });
0054 |const json = (res, status, body) => { res.writeHead(status, { 'content-type': 'application/json' }); res.end(JSON.stringify(body)); };
0055 |const bodyOf = (req) => new Promise((resolve, reject) => {
0056 |  let raw = '';
0057 |  req.on('data', (chunk) => { raw += chunk; if (raw.length > 100_000) reject(new Error('body too large')); });
0058 |  req.on('end', () => { try { resolve(JSON.parse(raw || '{}')); } catch (e) { reject(e); } });
0059 |  req.on('error', reject);
0060 |});
0061 |
0062 |async function seed(data) {
0063 |  onboarding.meta.sendMode = 'accepted';
0064 |  const suffix = `${Date.now()}-${Math.random().toString(16).slice(2)}`;
0065 |  const mantenedora = await prisma.mantenedora.create({ data: { name: `Timeline ${suffix}` } });
0066 |  const setor = await prisma.setor.create({ data: { mantenedoraId: mantenedora.id, name: 'Geral' } });
0067 |  const businessUnit = await prisma.businessUnit.create({ data: { mantenedoraId: mantenedora.id, setorId: setor.id, name: 'Número timeline', phone: `5584${String(Date.now()).slice(-8)}` } });
0068 |  await prisma.mantenedoraSettings.create({ data: { mantenedoraId: mantenedora.id, onboardingConcluido: true, modulos: { canalNaoOficial: false } } });
0069 |  const email = `timeline-${suffix}@teste.local`;
0070 |  const user = await prisma.appUser.create({ data: {
0071 |    mantenedoraId: mantenedora.id, name: 'Atendente Timeline', email,
0072 |    passwordHash: await bcrypt.hash('senha-de-teste-1', 10),
0073 |  } });
0074 |  await prisma.userBuRole.create({ data: { userId: user.id, buId: businessUnit.id, role: 'OWNER', grantedViaTipo: 'DIRETO' } });
0075 |  const phoneNumberId = `timeline-phone-${suffix}`;
0076 |  const timelinePhone = businessUnit.phone;
0077 |  const wabaId = `timeline-waba-${suffix}`;
0078 |  const channel = await prisma.buChannel.create({ data: { buId: businessUnit.id, type: 'OFICIAL', phoneNumberId, wabaId, requiresWindow: false, status: 'CONECTADO', generation: 1, pairingEpoch: 1, ownNumberVerified: true, verifiedEpoch: 1, providerConnectionState: 'SUBSCRIBED', receiptVerifiedAt: new Date() } });
0079 |  const identity = await prisma.providerResourceIdentity.create({ data: { provider: 'OFICIAL', externalResourceId: phoneNumberId, buId: businessUnit.id, currentChannelId: channel.id, managedLifecycle: true, cleanupState: 'ACTIVE' } });
0080 |  const keyId = process.env.CHANNEL_CREDENTIAL_KEY_ID; const key = Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY, 'base64');
0081 |  const envelope = sealChannelCredential(`timeline-scoped-token:${phoneNumberId}`, keyId, key, { purpose: 'active', provider: 'OFICIAL', buId: businessUnit.id, channelId: channel.id, generation: channel.generation, version: 1 });
0082 |  await prisma.channelCredential.create({ data: { channelId: channel.id, provider: 'OFICIAL', buId: businessUnit.id, generation: channel.generation, version: 1, keyId, nonce: new Uint8Array(envelope.nonce), ciphertext: new Uint8Array(envelope.ciphertext), tag: new Uint8Array(envelope.tag) } });
0083 |  let evolutionInstanceName = null;
0084 |  if (data.includeEvolution === true) {
0085 |    evolutionInstanceName = `timeline-evolution-${suffix}`;
0086 |    const evolution = await prisma.buChannel.create({ data: { buId: businessUnit.id, type: 'NAO_OFICIAL', evolutionInstanceName, requiresWindow: false, status: 'CONECTADO', generation: 1, pairingEpoch: 1, ownNumberVerified: true, verifiedEpoch: 1, providerConnectionState: 'CONNECTED', receiptVerifiedAt: new Date() } });
0087 |    await prisma.providerResourceIdentity.create({ data: { provider: 'NAO_OFICIAL', externalResourceId: evolutionInstanceName, buId: businessUnit.id, currentChannelId: evolution.id, managedLifecycle: true, cleanupState: 'ACTIVE' } });
0088 |    onboarding.evolution.inventory[evolutionInstanceName] = { name: evolutionInstanceName, ownerJid: '5584911112222@s.whatsapp.net', connectionStatus: 'open' };
0089 |  }
0090 |  providerInventory.set(phoneNumberId, { id: phoneNumberId, wabaId, telefone: timelinePhone });
0091 |  const conversation = await prisma.conversation.create({ data: { buId: businessUnit.id, contact: '5584911112222', displayName: 'Cliente Timeline', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 0 } });
0092 |  const otherConversation = await prisma.conversation.create({ data: { buId: businessUnit.id, contact: '5584933334444', displayName: 'Cliente Secundário', contactType: 'PESSOA', status: 'QUEUED', unreadCount: 0 } });
0093 |  const otherBu = await prisma.businessUnit.create({ data: { mantenedoraId: mantenedora.id, setorId: setor.id, name: 'Número alternativo', phone: `5585${String(Date.now()).slice(-8)}` } });
0094 |  await prisma.userBuRole.create({ data: { userId: user.id, buId: otherBu.id, role: 'OWNER', grantedViaTipo: 'DIRETO' } });
0095 |  const otherBuPhoneNumberId = `timeline-phone-other-${suffix}`;
0096 |  const otherBuPhone = otherBu.phone;
0097 |  const otherChannel = await prisma.buChannel.create({ data: { buId: otherBu.id, type: 'OFICIAL', phoneNumberId: otherBuPhoneNumberId, wabaId: `${wabaId}-other`, requiresWindow: false, status: 'CONECTADO', generation: 1, pairingEpoch: 1, ownNumberVerified: true, verifiedEpoch: 1, providerConnectionState: 'SUBSCRIBED', receiptVerifiedAt: new Date() } });
0098 |  await prisma.providerResourceIdentity.create({ data: { provider: 'OFICIAL', externalResourceId: otherBuPhoneNumberId, buId: otherBu.id, currentChannelId: otherChannel.id, managedLifecycle: true, cleanupState: 'ACTIVE' } });
0099 |  providerInventory.set(otherBuPhoneNumberId, { id: otherBuPhoneNumberId, wabaId: `${wabaId}-other`, telefone: otherBuPhone });
0100 |  const otherEnvelope = sealChannelCredential(`timeline-scoped-token:${otherBuPhoneNumberId}`, keyId, key, { purpose: 'active', provider: 'OFICIAL', buId: otherBu.id, channelId: otherChannel.id, generation: otherChannel.generation, version: 1 });
0101 |  await prisma.channelCredential.create({ data: { channelId: otherChannel.id, provider: 'OFICIAL', buId: otherBu.id, generation: otherChannel.generation, version: 1, keyId, nonce: new Uint8Array(otherEnvelope.nonce), ciphertext: new Uint8Array(otherEnvelope.ciphertext), tag: new Uint8Array(otherEnvelope.tag) } });
0102 |  const otherBuConversation = await prisma.conversation.create({ data: { buId: otherBu.id, contact: '5585555555555', displayName: 'Cliente Outra BU', contactType: 'PESSOA', status: 'QUEUED' } });
0103 |  fixtureConversationIds.add(conversation.id);
0104 |  fixtureConversationIds.add(otherConversation.id);
0105 |  fixtureConversationIds.add(otherBuConversation.id);
0106 |  const count = Math.max(0, Math.min(Number(data.count ?? 251), 10_000));
0107 |  const tiedAt = new Date('2026-10-14T12:00:00.000Z');
0108 |  const messages = Array.from({ length: count }, (_, i) => ({
0109 |    conversationId: conversation.id, buId: businessUnit.id, direction: 'IN', messageType: 'TEXTO',
0110 |    content: `histórico ${i + 1}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
0111 |    createdAt: data.tied === true ? tiedAt : new Date(tiedAt.getTime() + i * 1000),
0112 |  }));
0113 |  if (messages.length) await prisma.message.createMany({ data: messages });
0114 |  const expectedIds = await prisma.message.findMany({ where: { conversationId: conversation.id }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true } });
0115 |  return { email, password: 'senha-de-teste-1', userId: user.id, mantenedoraId: mantenedora.id, businessUnitId: businessUnit.id, conversationId: conversation.id, otherConversationId: otherConversation.id, otherBusinessUnitId: otherBu.id, otherBuConversationId: otherBuConversation.id, otherBuPhoneNumberId, phoneNumberId, wabaId, evolutionInstanceName, count, expectedIds: expectedIds.map((m) => m.id) };
0116 |}
0117 |
0118 |async function seedNumberOnboarding() {
0119 |  const suffix = `number-${Date.now()}-${Math.random().toString(16).slice(2, 8)}`;
0120 |  const createTenant = async (label) => {
0121 |    const mantenedora = await prisma.mantenedora.create({ data: { name: `${label} ${suffix}` } });
0122 |    const setor = await prisma.setor.create({ data: { mantenedoraId: mantenedora.id, name: 'Geral' } });
0123 |    const bu = await prisma.businessUnit.create({ data: { mantenedoraId: mantenedora.id, setorId: setor.id, name: `${label} BU`, phone: `5511${String(Date.now()).slice(-8)}` } });
0124 |    await prisma.mantenedoraSettings.create({ data: { mantenedoraId: mantenedora.id, onboardingConcluido: true, modulos: { canalNaoOficial: true } } });
0125 |    return { mantenedora, setor, bu };
0126 |  };
0127 |  const a = await createTenant('Onboarding A'); const b = await createTenant('Onboarding B');
0128 |  const createUser = async (tenant, role, label) => {
0129 |    const email = `${label}-${suffix}@teste.local`;
0130 |    const user = await prisma.appUser.create({ data: { mantenedoraId: tenant.mantenedora.id, name: label, email, passwordHash: await bcrypt.hash('senha-onboarding-2026', 10) } });
0131 |    await prisma.userBuRole.create({ data: {
0132 |      userId: user.id, buId: tenant.bu.id, role,
0133 |      grantedViaTipo: role === 'OWNER' ? 'MANTENEDORA' : 'DIRETO',
0134 |      ...(role === 'OWNER' ? { grantedViaId: tenant.mantenedora.id } : {}),
0135 |    } });
0136 |    return { id: user.id, email, password: 'senha-onboarding-2026', role };
0137 |  };
0138 |  return {
0139 |    tenantA: { mantenedoraId: a.mantenedora.id, buId: a.bu.id, owner: await createUser(a, 'OWNER', 'owner'), admin: await createUser(a, 'ADMIN', 'admin'), operator: await createUser(a, 'ATENDENTE', 'operator') },
0140 |    tenantB: { mantenedoraId: b.mantenedora.id, buId: b.bu.id, owner: await createUser(b, 'OWNER', 'other-owner'), admin: await createUser(b, 'ADMIN', 'other-admin') },
0141 |  };
0142 |}
0143 |
0144 |async function incoming(data) {
0145 |  const id = String(data.id ?? `timeline-event-${Date.now()}`);
0146 |  const payload = { entry: [{ changes: [{ field: 'messages', value: {
0147 |    metadata: { phone_number_id: data.phoneNumberId },
0148 |    contacts: [{ profile: { name: 'Cliente Timeline' } }],
0149 |    messages: [{ id, from: '5584911112222', type: 'text', text: { body: String(data.text ?? id) } }],
0150 |  } }] }] };
0151 |  const raw = JSON.stringify(payload);
0152 |  const signature = 'sha256=' + createHmac('sha256', 'segredo-do-app-meta').update(raw).digest('hex');
0153 |  const response = await fetch(`http://127.0.0.1:${apiPort}/webhooks/meta`, {
0154 |    method: 'POST', headers: { 'content-type': 'application/json', 'x-hub-signature-256': signature }, body: raw,
0155 |  });
0156 |  return { status: response.status, body: await response.text() };
0157 |}
0158 |
0159 |const server = http.createServer(async (req, res) => {
0160 |  try {
0161 |    if (req.method === 'GET' && req.url.startsWith('/provider/resources')) {
0162 |      if (req.headers['x-fixture-provider-token'] !== 'timeline-provider-port-only') return json(res, 403, { error: 'forbidden' });
0163 |      return json(res, 200, onboarding.resources.length ? onboarding.resources : Array.from(providerInventory.values()));
0164 |    }
0165 |    if (req.method === 'GET' && req.url === '/provider/state') {
0166 |      if (req.headers['x-fixture-provider-token'] !== 'timeline-provider-port-only') return json(res, 403, { error: 'forbidden' });
0167 |      const inventory = Object.fromEntries(Object.entries(onboarding.evolution.inventory).map(([name, item]) => [name, { name, ownerJid: item.ownerJid, connectionStatus: item.connectionStatus }]));
0168 |      return json(res, 200, { resources: onboarding.resources, calls: onboarding.calls, effects: onboarding.effects, evolution: { inventory, outcomes: onboarding.evolution.outcomes }, meta: { grantResourceIds: Object.fromEntries(Object.entries(onboarding.meta.grants ?? {}).map(([code, grant]) => [code, grant.resources ?? []])), pages: onboarding.meta.pages, sendMode: onboarding.meta.sendMode }, failures: onboarding.failures, holds: onboarding.holds, holdsAfter: onboarding.holdsAfter, ambiguousAfter: onboarding.ambiguousAfter });
0169 |    }
0170 |    if (req.method === 'GET' && req.url === '/health') return json(res, 200, { status: 'ok' });
0171 |    const data = await bodyOf(req);
0172 |    if (req.url.startsWith('/provider/') && req.headers['x-fixture-provider-token'] !== 'timeline-provider-port-only') return json(res, 403, { error: 'forbidden' });
0173 |    if (req.method === 'POST' && req.url === '/provider/config') {
0174 |      if (data.reset === true) { onboarding.calls = []; onboarding.effects = []; onboarding.failures = {}; onboarding.holds = {}; onboarding.holdsAfter = {}; onboarding.ambiguousAfter = {}; onboarding.resources = []; onboarding.meta = { codeTokens: {}, grants: {}, pages: {}, sendMode: 'accepted' }; onboarding.evolution = { inventory: {}, outcomes: {} }; providerInventory.clear(); barriers.clear(); }
0175 |      if (Array.isArray(data.resources)) onboarding.resources = data.resources.map((r) => ({ ...r }));
0176 |      if (data.meta && typeof data.meta === 'object') Object.assign(onboarding.meta, data.meta);
0177 |      if (data.evolution && typeof data.evolution === 'object') Object.assign(onboarding.evolution, data.evolution);
0178 |      if (data.failures && typeof data.failures === 'object') onboarding.failures = Object.fromEntries(Object.entries(data.failures).map(([k, v]) => [k, { remaining: Math.max(1, Number(v.remaining ?? 1)), message: String(v.message ?? 'controlled provider failure') }]));
0179 |      if (data.holds && typeof data.holds === 'object') onboarding.holds = { ...data.holds };
0180 |      if (data.holdsAfter && typeof data.holdsAfter === 'object') onboarding.holdsAfter = { ...data.holdsAfter };
0181 |      if (data.ambiguousAfter && typeof data.ambiguousAfter === 'object') onboarding.ambiguousAfter = Object.fromEntries(Object.entries(data.ambiguousAfter).map(([k, v]) => [k, { remaining: Math.max(1, Number(v.remaining ?? 1)) }]));
0182 |      return json(res, 200, { configured: true });
0183 |    }
0184 |    if (req.method === 'POST' && req.url === '/provider/release') {
0185 |      const b = barriers.get(`${data.operation}:${data.key}`); if (b) b.release();
0186 |      return json(res, 200, { released: Boolean(b) });
0187 |    }
0188 |    if (req.method === 'POST' && req.url === '/provider/call') {
0189 |      const call = await providerCall(String(data.operation), data.args ?? {});
0190 |      return json(res, 200, { accepted: true, call });
0191 |    }
0192 |    if (req.method === 'POST' && req.url === '/provider/effect') return json(res, 200, { effect: await providerEffect(String(data.operation), data.args ?? {}) });
0193 |    if (req.method === 'POST' && req.url === '/provider/evolution/observe') {
0194 |      await providerCall('evolution.observe', { name: data.name });
0195 |      const name = String(data.name); const observed = onboarding.evolution.inventory[name];
0196 |      return json(res, 200, observed ? { ...observed } : null);
0197 |    }
0198 |    if (req.method === 'POST' && req.url === '/provider/evolution/create') {
0199 |      const call = await providerCall('evolution.create', { name: data.name, attemptId: data.attemptId, channelId: data.channelId, generation: data.generation, pairingEpoch: data.pairingEpoch });
0200 |      const created = onboarding.evolution.createOutcome ?? {};
0201 |      const instance = { name: String(data.name), ownerJid: data.ownerJid ?? created.ownerJid ?? null, connectionStatus: data.connectionStatus ?? created.connectionStatus ?? 'connecting', qrcode: data.qrcode ?? created.qrcode ?? 'data:image/png;base64,FAKE-QR' };
0202 |      onboarding.evolution.inventory[instance.name] = instance;
0203 |      await providerEffect('evolution.create', { name: instance.name, attemptId: data.attemptId, channelId: data.channelId, generation: data.generation, pairingEpoch: data.pairingEpoch });
0204 |      return json(res, 201, { created: true, instance, call });
0205 |    }
0206 |    if (req.method === 'POST' && req.url === '/provider/evolution/delete') {
0207 |      await providerCall('evolution.delete', { name: data.name });
0208 |      const existed = Boolean(onboarding.evolution.inventory[String(data.name)]);
0209 |      delete onboarding.evolution.inventory[String(data.name)];
0210 |      await providerEffect('evolution.delete', { name: data.name });
0211 |      return json(res, 200, { deleted: existed });
0212 |    }
0213 |    if (req.method === 'POST' && req.url === '/provider/evolution/receipt') {
0214 |      const name = String(data.name); const observed = onboarding.evolution.inventory[name];
0215 |      if (!observed) return json(res, 404, { error: 'unknown fixture instance' });
0216 |      Object.assign(observed, { ownerJid: data.ownerJid ?? observed.ownerJid, connectionStatus: data.connectionStatus ?? observed.connectionStatus });
0217 |      await providerEffect('evolution.receipt', { name });
0218 |      return json(res, 200, { updated: true });
0219 |    }
0220 |    if (req.method === 'POST' && req.url === '/provider/attempt/expire') {
0221 |      const attemptId = typeof data.attemptId === 'string' ? data.attemptId : '';
0222 |      const buId = typeof data.buId === 'string' ? data.buId : '';
0223 |      if (!/^[0-9a-f]{32}$/i.test(attemptId) || !/^[0-9a-f-]{36}$/i.test(buId)) return json(res, 400, { error: 'invalid attempt scope' });
0224 |      const changed = await prisma.channelRegistrationAttempt.updateMany({
0225 |        where: { id: attemptId, buId, operation: 'NOVO', state: 'PENDING_AUTH', channelId: { not: null } },
0226 |        data: { expiresAt: new Date(Date.now() - 1_000) },
0227 |      });
0228 |      if (changed.count !== 1) return json(res, 404, { error: 'eligible fixture attempt not found' });
0229 |      return json(res, 200, { expired: true, attemptId, buId });
0230 |    }
0231 |    if (req.method === 'POST' && req.url === '/seed-number-onboarding') {
0232 |      const result = await seedNumberOnboarding(data);
0233 |      return json(res, 201, result);
0234 |    }
0235 |    if (req.method === 'GET' && req.url.startsWith('/audit?')) {
0236 |      const query = new URL(req.url, 'http://localhost').searchParams;
0237 |      const conversationId = query.get('conversationId');
0238 |      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: conversationId } });
0239 |      const messages = await prisma.message.findMany({ where: { conversationId }, orderBy: [{ createdAt: 'asc' }, { id: 'asc' }], select: { id: true, content: true, direction: true, authorName: true, createdAt: true } });
0240 |      return json(res, 200, { status: conversation.status, unreadCount: conversation.unreadCount, messages });
0241 |    }
0242 |    if (req.method === 'GET' && req.url.startsWith('/audit-outbound?')) {
0243 |      const query = new URL(req.url, 'http://localhost').searchParams;
0244 |      const conversationId = query.get('conversationId');
0245 |      const content = query.get('content');
0246 |      if (!conversationId || !fixtureConversationIds.has(conversationId) || !content) return json(res, 400, { error: 'invalid fixture audit scope' });
0247 |      const messages = await prisma.message.findMany({ where: { conversationId, content, direction: 'OUT' }, select: { status: true, externalId: true } });
0248 |      return json(res, 200, {
0249 |        total: messages.length,
0250 |        accepted: messages.filter((message) => message.status === 'ENVIADA').length,
0251 |        failed: messages.filter((message) => message.status === 'FALHOU').length,
0252 |        failedWithoutExternalId: messages.filter((message) => message.status === 'FALHOU' && !message.externalId).length,
0253 |      });
0254 |    }
0255 |    if (req.method === 'POST' && req.url === '/seed') return json(res, 201, await seed(data));
0256 |    if (req.method === 'POST' && req.url === '/send-mode') {
0257 |      if (!['accepted', 'unknown'].includes(data.mode)) return json(res, 400, { error: 'invalid mode' });
0258 |      onboarding.meta.sendMode = data.mode;
0259 |      return json(res, 200, { mode: onboarding.meta.sendMode });
0260 |    }
0261 |    if (req.method === 'POST' && req.url === '/select-evolution') {
0262 |      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: data.conversationId } });
0263 |      const channel = await prisma.buChannel.findFirstOrThrow({ where: { buId: conversation.buId, type: 'NAO_OFICIAL' } });
0264 |      const identity = await prisma.providerResourceIdentity.findFirstOrThrow({ where: { currentChannelId: channel.id } });
0265 |      const message = await prisma.message.create({ data: {
0266 |        conversationId: conversation.id, buId: conversation.buId, direction: 'IN', messageType: 'TEXTO',
0267 |        content: 'ingress fixture selects Evolution', channelOrigin: 'NAO_OFICIAL', status: 'RECEBIDA',
0268 |        externalId: `fixture-ingress-${Date.now()}-${Math.random().toString(16).slice(2)}`,
0269 |        providerResourceIdentityId: identity.id, createdAt: new Date(Date.now() + 60_000),
0270 |      } });
0271 |      return json(res, 201, { id: message.id });
0272 |    }
0273 |    if (req.method === 'POST' && req.url === '/incoming') return json(res, 200, await incoming(data));
0274 |    if (req.method === 'POST' && req.url === '/late-tie') {
0275 |      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: data.conversationId } });
0276 |      const message = await prisma.message.create({ data: {
0277 |        id: String(data.id), conversationId: conversation.id, buId: conversation.buId,
0278 |        direction: 'IN', messageType: 'TEXTO', content: 'inserção empatada tardia',
0279 |        channelOrigin: 'OFICIAL', status: 'RECEBIDA', createdAt: new Date(data.createdAt),
0280 |      } });
0281 |      return json(res, 201, { id: message.id });
0282 |    }
0283 |    if (req.method === 'POST' && req.url === '/revoke') {
0284 |      await prisma.userBuRole.deleteMany({ where: { userId: data.userId, buId: data.businessUnitId } });
0285 |      return json(res, 200, { revoked: true });
0286 |    }
0287 |    if (req.method === 'POST' && req.url === '/burst') {
0288 |      const conversation = await prisma.conversation.findUniqueOrThrow({ where: { id: data.conversationId } });
0289 |      const count = Math.max(1, Math.min(Number(data.count ?? 120), 500));
0290 |      const base = new Date(data.createdAt ?? Date.now());
0291 |      await prisma.message.createMany({ data: Array.from({ length: count }, (_, i) => ({
0292 |        conversationId: conversation.id, buId: conversation.buId, direction: 'IN', messageType: 'TEXTO',
0293 |        content: `burst ${i + 1}`, channelOrigin: 'OFICIAL', status: 'RECEBIDA',
0294 |        createdAt: new Date(base.getTime() + i),
0295 |      })) });
0296 |      return json(res, 201, { count });
0297 |    }
0298 |    return json(res, 404, { error: 'not found' });
0299 |  } catch (error) {
0300 |    console.error(error);
0301 |    return json(res, 500, { error: error instanceof Error ? error.message : String(error) });
0302 |  }
0303 |});
0304 |server.listen(fixturePort, '127.0.0.1', () => console.log(`timeline fixtures listening on 127.0.0.1:${fixturePort}`));
0305 |process.on('SIGTERM', () => server.close(() => prisma.$disconnect().finally(() => process.exit(0))));
0306 |process.on('SIGINT', () => server.close(() => prisma.$disconnect().finally(() => process.exit(0))));
```

## Changed source web-app/e2e/channel-transport.spec.ts

```text
0001 |import { expect, test, type APIRequestContext, type Page } from '@playwright/test';
0002 |
0003 |const FIXTURES = 'http://127.0.0.1:3101';
0004 |
0005 |async function seed(request: APIRequestContext, includeEvolution = false, count = 3) {
0006 |  const response = await request.post(`${FIXTURES}/seed`, { data: { count, includeEvolution } });
0007 |  expect(response.status()).toBe(201);
0008 |  return response.json() as Promise<{
0009 |    email: string; password: string; businessUnitId: string; conversationId: string;
0010 |    otherConversationId: string; otherBusinessUnitId: string;
0011 |  }>;
0012 |}
0013 |
0014 |async function loginAndOpen(page: Page, fixture: Awaited<ReturnType<typeof seed>>, messages = 3) {
0015 |  await page.context().clearCookies();
0016 |  await page.goto('/login');
0017 |  await page.getByLabel('E-mail').fill(fixture.email);
0018 |  await page.getByLabel('Senha').fill(fixture.password);
0019 |  await page.getByRole('button', { name: 'Entrar' }).click();
0020 |  await expect(page).toHaveURL(/\/inbox$/);
0021 |  await page.getByLabel('Business Unit').selectOption(fixture.businessUnitId);
0022 |  await page.getByRole('button', { name: 'Cliente Timeline' }).click();
0023 |  await expect(page.locator('.bolha')).toHaveCount(messages);
0024 |}
0025 |
0026 |test.describe('Channel outbound pela Inbox com BFF e PostgreSQL reais', () => {
0027 |  test('envia por Meta, mantém rascunho em ACK sem ID e bloqueia conversa ambígua', async ({ page, request }) => {
0028 |    const fixture = await seed(request);
0029 |    await loginAndOpen(page, fixture);
0030 |    const composer = page.getByPlaceholder('Escreva uma resposta');
0031 |    await composer.fill('resposta oficial de teste');
0032 |    await page.getByRole('button', { name: 'Enviar' }).click();
0033 |    await expect(page.locator('.bolha').filter({ hasText: 'resposta oficial de teste' })).toBeVisible();
0034 |    await expect(composer).toHaveValue('');
0035 |
0036 |    await request.post(`${FIXTURES}/send-mode`, { data: { mode: 'unknown' } });
0037 |    await composer.fill('rascunho não reenviado');
0038 |    await page.getByRole('button', { name: 'Enviar' }).click();
0039 |    await expect(page.getByRole('alert')).toContainText('aceitou o envio sem confirmar o ID externo');
0040 |    await expect(composer).toHaveValue('rascunho não reenviado');
0041 |
0042 |    const ambiguous = await seed(request, true, 0);
0043 |    await page.context().clearCookies();
0044 |    await page.goto('/login');
0045 |    await page.getByLabel('E-mail').fill(ambiguous.email);
0046 |    await page.getByLabel('Senha').fill(ambiguous.password);
0047 |    await page.getByRole('button', { name: 'Entrar' }).click();
0048 |    await page.getByLabel('Business Unit').selectOption(ambiguous.businessUnitId);
0049 |    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
0050 |    await expect(page.getByText('Esta conversa ainda não tem um canal definido. Aguarde uma mensagem recebida para responder.')).toBeVisible();
0051 |    await expect(page.getByRole('button', { name: 'Enviar' })).toBeDisabled();
0052 |  });
0053 |
0054 |  test('seleciona Evolution pela última origem e descarta resposta atrasada após troca A→B→A', async ({ page, request }) => {
0055 |    const fixture = await seed(request, true);
0056 |    await request.post(`${FIXTURES}/select-evolution`, { data: { conversationId: fixture.conversationId } });
0057 |    await loginAndOpen(page, fixture, 4);
0058 |    const composer = page.getByPlaceholder('Escreva uma resposta');
0059 |    await composer.fill('resposta não oficial de teste');
0060 |    await page.getByRole('button', { name: 'Enviar' }).click();
0061 |    await expect(page.locator('.bolha').filter({ hasText: 'resposta não oficial de teste' })).toBeVisible();
0062 |    await expect(composer).toHaveValue('');
0063 |
0064 |    let liberar!: () => void;
0065 |    let iniciou!: () => void;
0066 |    const continua = new Promise<void>((resolve) => { liberar = resolve; });
0067 |    const solicitacao = new Promise<void>((resolve) => { iniciou = resolve; });
0068 |    const holdReply = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
0069 |    const holdResponse = async (route: import('@playwright/test').Route) => {
0070 |      if (route.request().method() !== 'POST') return route.continue();
0071 |      const response = await route.fetch();
0072 |      iniciou();
0073 |      await continua;
0074 |      await route.fulfill({ response });
0075 |    };
0076 |    await page.route(holdReply, holdResponse);
0077 |    await composer.fill('resposta cuja resposta chega tarde');
0078 |    await page.getByRole('button', { name: 'Enviar' }).click();
0079 |    await solicitacao;
0080 |    await page.getByRole('button', { name: 'Cliente Secundário' }).click();
0081 |    const activeThreadTitle = page.locator('.cartao.grade > .linha > strong');
0082 |    await expect(activeThreadTitle).toHaveCount(1);
0083 |    await expect(activeThreadTitle).toHaveText('Cliente Secundário');
0084 |    await expect(page.locator('.cartao.lista .item.ativo')).toHaveCount(1);
0085 |    await page.getByRole('button', { name: 'Em atendimento' }).click();
0086 |    await page.getByRole('button', { name: 'Cliente Timeline' }).click();
0087 |    await expect(activeThreadTitle).toHaveCount(1);
0088 |    await expect(activeThreadTitle).toHaveText('Cliente Timeline');
0089 |    await expect(page.locator('.cartao.lista .item.ativo')).toHaveCount(1);
0090 |    await composer.fill('resposta cuja resposta chega tarde');
0091 |    const respostaAntiga = page.waitForResponse((response) => response.request().method() === 'POST'
0092 |      && new URL(response.url()).pathname === `/api/bff/conversations/${fixture.conversationId}/messages`);
0093 |    liberar();
0094 |    const responseAntiga = await respostaAntiga;
0095 |    expect(responseAntiga.status()).toBe(201);
0096 |    expect(await responseAntiga.finished()).toBeNull();
0097 |    await page.evaluate(() => new Promise<void>((resolve) => {
0098 |      requestAnimationFrame(() => requestAnimationFrame(() => resolve()));
0099 |    }));
0100 |    await expect(composer).toHaveValue('resposta cuja resposta chega tarde');
0101 |    await expect(page.getByRole('alert')).toHaveCount(0);
0102 |    await page.unroute(holdReply, holdResponse);
0103 |  });
0104 |
0105 |  test('bloqueia vinte novos submits durante cada envio real em cinco ondas', async ({ page, request }) => {
0106 |    const fixture = await seed(request);
0107 |    await loginAndOpen(page, fixture);
0108 |    const composer = page.getByPlaceholder('Escreva uma resposta');
0109 |    const waveEvidence: Array<{ requests: number; retriggers: number; outcome: 'accepted' | 'unknown'; draftPreserved: boolean; messageCount: number }> = [];
0110 |    const form = page.locator('form').filter({ has: composer });
0111 |    for (let round = 0; round < 5; round += 1) {
0112 |      const outcome = round % 2 === 1 ? 'unknown' : 'accepted';
0113 |      const text = `composer wave ${round} ${outcome}`;
0114 |      await request.post(`${FIXTURES}/send-mode`, { data: { mode: outcome } });
0115 |      let requestCount = 0;
0116 |      let actualStatus = 0;
0117 |      let markEntered!: () => void;
0118 |      let release!: () => void;
0119 |      const entered = new Promise<void>((resolve) => { markEntered = resolve; });
0120 |      const held = new Promise<void>((resolve) => { release = resolve; });
0121 |      const matcher = (url: URL) => url.pathname === `/api/bff/conversations/${fixture.conversationId}/messages`;
0122 |      const holdRealResponse = async (route: import('@playwright/test').Route) => {
0123 |        if (route.request().method() !== 'POST') return route.continue();
0124 |        requestCount += 1;
0125 |        const response = await route.fetch();
0126 |        if (requestCount === 1) actualStatus = response.status();
0127 |        if (requestCount === 1) markEntered();
0128 |        await held;
0129 |        await route.fulfill({ response });
0130 |      };
0131 |      await page.route(matcher, holdRealResponse);
0132 |      await composer.fill(text);
0133 |      await page.getByRole('button', { name: 'Enviar' }).click();
0134 |      await entered;
0135 |      try {
0136 |        for (let index = 0; index < 20; index += 1) {
0137 |          await form.evaluate((element) => element.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true })));
0138 |        }
0139 |        expect(requestCount).toBe(1);
0140 |        expect(await page.getByRole('button', { name: 'Enviando…' }).isDisabled()).toBe(true);
0141 |      } finally {
0142 |        release();
0143 |      }
0144 |      if (outcome === 'unknown') {
0145 |        await expect(page.getByRole('alert')).toContainText('aceitou o envio sem confirmar o ID externo');
0146 |        await expect(composer).toHaveValue(text);
0147 |        expect(actualStatus).toBe(409);
0148 |      } else {
0149 |        await expect(page.locator('.bolha').filter({ hasText: text })).toBeVisible();
0150 |        await expect(composer).toHaveValue('');
0151 |        expect(actualStatus).toBe(201);
0152 |      }
0153 |      const auditResponse = await request.get(`${FIXTURES}/audit-outbound?conversationId=${encodeURIComponent(fixture.conversationId)}&content=${encodeURIComponent(text)}`);
0154 |      expect(auditResponse.status()).toBe(200);
0155 |      const audit = await auditResponse.json() as { total: number; accepted: number; failed: number; failedWithoutExternalId: number };
0156 |      expect(audit).toEqual(outcome === 'unknown'
0157 |        ? { total: 1, accepted: 0, failed: 1, failedWithoutExternalId: 1 }
0158 |        : { total: 1, accepted: 1, failed: 0, failedWithoutExternalId: 0 });
0159 |      waveEvidence.push({ requests: requestCount, retriggers: 20, outcome, draftPreserved: outcome === 'unknown', messageCount: audit.total });
0160 |      await page.unroute(matcher, holdRealResponse);
0161 |    }
0162 |    expect(waveEvidence).toHaveLength(5);
0163 |    expect(waveEvidence.every((wave) => wave.requests === 1 && wave.retriggers === 20)).toBe(true);
0164 |    expect(waveEvidence.filter((wave) => wave.outcome === 'accepted').every((wave) => wave.messageCount === 1 && !wave.draftPreserved)).toBe(true);
0165 |    expect(waveEvidence.filter((wave) => wave.outcome === 'unknown').every((wave) => wave.messageCount === 1 && wave.draftPreserved)).toBe(true);
0166 |    console.log(`[FRC-COMPOSER-EVIDENCE]${JSON.stringify({ waves: waveEvidence, limits: 'Five real BFF/PostgreSQL submits held after the actual response; twenty user-form submit events per in-flight send; one request per wave; no capacity/SLO claim.' })}`);
0167 |  });
0168 |});
```

## Unchanged critical context api-app/src/domain/channels/transport/channel.ts

```text
0001 |export type ChannelOrigin = 'OFICIAL' | 'NAO_OFICIAL';
0002 |
0003 |export type ChannelAvailabilityReason =
0004 |  | 'CANAL_AUSENTE'
0005 |  | 'CANAL_AMBIGUO'
0006 |  | 'CANAL_SELECIONADO_INDISPONIVEL'
0007 |  | 'CHANNEL_IDENTITY_NOT_VERIFIED'
0008 |  | 'CHANNEL_NOT_READY'
0009 |  | 'PENDING_CREDENTIAL'
0010 |  | 'JANELA_FECHADA';
0011 |
0012 |export type ChannelSendResult =
0013 |  | { outcome: 'ACCEPTED'; externalMessageId: string }
0014 |  | { outcome: 'BLOCKED'; reason: ChannelAvailabilityReason | 'CHANNEL_CONTEXT_CHANGED' }
0015 |  | { outcome: 'REJECTED'; code: string }
0016 |  | { outcome: 'UNKNOWN'; evidence: 'ACK_WITHOUT_ID' | 'TRANSPORT_UNCONFIRMED'; legacyCode: string };
0017 |
0018 |export interface TextMessage {
0019 |  kind: 'text';
0020 |  recipientRef: string;
0021 |  text: string;
0022 |}
0023 |
0024 |export abstract class Channel {
0025 |  abstract sendMessage(message: TextMessage): Promise<ChannelSendResult>;
0026 |}
0027 |
0028 |/** Safe storage provenance captured for one send; never includes provider credentials or protocol addresses. */
0029 |export interface ChannelOperationContext {
0030 |  readonly channelId: string;
0031 |  readonly buId: string;
0032 |  readonly channelOrigin: ChannelOrigin;
0033 |  readonly providerResourceIdentityId: string;
0034 |  readonly generation: number;
0035 |  readonly pairingEpoch: number;
0036 |  readonly activeCredentialVersion: number | null;
0037 |  readonly requiresWindow: boolean;
0038 |}
0039 |
0040 |export interface ResolvedChannelOperation {
0041 |  readonly channel: Channel;
0042 |  readonly context: ChannelOperationContext;
0043 |}
0044 |
0045 |export interface ChannelAvailability {
0046 |  available: boolean;
0047 |  reason: ChannelAvailabilityReason | null;
0048 |  channelOrigin: ChannelOrigin | null;
0049 |  requiresWindow: boolean;
0050 |  windowOpen: boolean;
0051 |  expiresAt: Date | null;
0052 |}
0053 |
0054 |export interface ConversationChannelReference {
0055 |  conversationId: string;
0056 |  buId: string;
0057 |}
0058 |
0059 |export interface ConversationAvailabilityReference extends ConversationChannelReference {
0060 |  latestMessageOrigin: ChannelOrigin | null;
0061 |}
0062 |
0063 |export interface VerifiedIngressChannelReference extends ConversationChannelReference {
0064 |  channelId: string;
0065 |  providerResourceIdentityId: string;
0066 |  channelOrigin: ChannelOrigin;
0067 |  generation: number;
0068 |  pairingEpoch: number;
0069 |}
0070 |
0071 |export abstract class ChannelResolver {
0072 |  abstract resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation>;
0073 |  abstract resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation>;
0074 |  abstract inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability>;
0075 |  abstract inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>>;
0076 |  abstract contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'>;
0077 |}
```

## Unchanged critical context api-app/src/domain/channels/transport/channel-dependencies.spec.ts

```text
0001 |import { readdirSync, readFileSync } from 'node:fs';
0002 |import { dirname, resolve } from 'node:path';
0003 |import { fileURLToPath } from 'node:url';
0004 |import { describe, expect, it } from 'vitest';
0005 |
0006 |const inboxDirectory = resolve(dirname(fileURLToPath(import.meta.url)), '../../inbox');
0007 |const consumerPaths = [
0008 |  resolve(inboxDirectory, 'conversations.service.ts'),
0009 |  resolve(inboxDirectory, 'incoming.service.ts'),
0010 |  ...readdirSync(inboxDirectory)
0011 |    .filter((name) => /^outbound.*\.ts$/.test(name))
0012 |    .map((name) => resolve(inboxDirectory, name)),
0013 |];
0014 |
0015 |function providerDispatchViolations(source: string): string[] {
0016 |  const rules: Array<[string, RegExp]> = [
0017 |    ['provider client or adapter import', /from\s+['"][^'"]*integrations\/(?:meta|evolution|channels)\/[^'"]+['"]/],
0018 |    ['credential resolver import', /from\s+['"][^'"]*channel-credential-resolver['"]/],
0019 |    ['provider injection token', /\b(?:META_CLIENT|EVOLUTION_CLIENT)\b/],
0020 |    ['provider text dispatch', /\.enviarTexto\s*\(/],
0021 |    ['provider-specific branch', /\.(?:provider|channelOrigin|type)\s*(?:===|!==|==|!=)\s*['"](?:OFICIAL|NAO_OFICIAL)['"]|switch\s*\(\s*[^)]*\.(?:provider|channelOrigin|type)\s*\)/],
0022 |  ];
0023 |  return rules.filter(([, expression]) => expression.test(source)).map(([name]) => name);
0024 |}
0025 |
0026 |describe('common outbound dependency boundary', () => {
0027 |  it('keeps provider clients and dispatch inside channel adapters', () => {
0028 |    const violations = consumerPaths.flatMap((path) => {
0029 |      const source = readFileSync(path, 'utf8');
0030 |      return providerDispatchViolations(source).map((rule) => `${path}: ${rule}`);
0031 |    });
0032 |    expect(violations).toEqual([]);
0033 |  });
0034 |
0035 |  it.each([
0036 |    "import { MetaClient } from '../../integrations/meta/meta.client';",
0037 |    "import { MetaChannelFactory } from '../../integrations/channels/meta-channel';",
0038 |    "import { ChannelCredentialResolver } from '../channels/channel-credential-resolver';",
0039 |    "if (context.channelOrigin === 'OFICIAL') return sendMeta();",
0040 |    "switch (binding.type) { case 'NAO_OFICIAL': return sendEvolution(); }",
0041 |    "const send = context.channelOrigin === 'OFICIAL' ? sendMeta() : sendEvolution();",
0042 |    "switch (context.provider) { case 'OFICIAL': return sendMeta(); }",
0043 |  ])('detects synthetic provider coupling outside the adapter allowlist: %s', (source) => {
0044 |    expect(providerDispatchViolations(source).length).toBeGreaterThan(0);
0045 |  });
0046 |});
```

## Unchanged critical context api-app/src/domain/channels/channel-credential-resolver.ts

```text
0001 |import { ConflictException, Injectable } from '@nestjs/common';
0002 |import { PrismaService } from '../../infra/prisma/prisma.service';
0003 |import { loadChannelCredentialKey, openChannelCredential } from './channel-credential-crypto';
0004 |
0005 |export interface ResolvedChannelCredential {
0006 |  channelId: string;
0007 |  buId: string;
0008 |  provider: 'OFICIAL' | 'NAO_OFICIAL';
0009 |  generation: number;
0010 |  pairingEpoch: number;
0011 |  providerResourceIdentityId: string;
0012 |  externalResourceId: string;
0013 |  activeCredentialVersion: number | null;
0014 |  accessToken?: string;
0015 |  phoneNumberId?: string;
0016 |  wabaId?: string;
0017 |  evolutionInstanceName?: string;
0018 |}
0019 |
0020 |/** Resolves only a currently verified, owned channel and decrypts its own credential. */
0021 |@Injectable()
0022 |export class ChannelCredentialResolver {
0023 |  constructor(private readonly prisma: PrismaService) {}
0024 |
0025 |  /** Metadata-only check for GET availability; it never decrypts the credential. */
0026 |  async inspectActiveCredential(channelId: string, generation: number): Promise<{ version: number | null; ready: boolean }> {
0027 |    return (await this.inspectActiveCredentials([{ channelId, generation }])).get(channelId) ?? { version: null, ready: false };
0028 |  }
0029 |
0030 |  /** One metadata-only credential read for a public conversation page. */
0031 |  async inspectActiveCredentials(bindings: readonly { channelId: string; generation: number }[]): Promise<Map<string, { version: number | null; ready: boolean }>> {
0032 |    const ids = [...new Set(bindings.map((binding) => binding.channelId))];
0033 |    if (!ids.length) return new Map();
0034 |    const credentials = await this.prisma.channelCredential.findMany({
0035 |      where: { channelId: { in: ids } }, select: { channelId: true, version: true, generation: true, keyId: true },
0036 |    });
0037 |    let currentKeyId: string | null = null;
0038 |    try {
0039 |      currentKeyId = loadChannelCredentialKey(process.env).keyId;
0040 |    } catch { /* absent key makes every official channel unavailable */ }
0041 |    const byId = new Map(credentials.map((credential) => [credential.channelId, credential]));
0042 |    return new Map(bindings.map(({ channelId, generation }) => {
0043 |      const credential = byId.get(channelId);
0044 |      return [channelId, {
0045 |        version: credential?.version ?? null,
0046 |        ready: Boolean(credential && credential.generation === generation && currentKeyId && credential.keyId === currentKeyId),
0047 |      }];
0048 |    }));
0049 |  }
0050 |
0051 |  async resolve(channelId: string, purpose: 'send' | 'registration' | 'verify' = 'send'): Promise<ResolvedChannelCredential> {
0052 |    const channel = await this.prisma.buChannel.findUnique({
0053 |      where: { id: channelId }, include: { credential: true, providerIdentities: true },
0054 |    });
0055 |    if (!channel || (purpose !== 'verify' && (!channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch))) {
0056 |      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
0057 |    }
0058 |    if (purpose === 'send' && (channel.status !== 'CONECTADO' || !channel.receiptVerifiedAt
0059 |      || (channel.type === 'OFICIAL' && channel.providerConnectionState !== 'SUBSCRIBED')
0060 |      || (channel.type === 'NAO_OFICIAL' && channel.providerConnectionState !== 'CONNECTED'))) {
0061 |      throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
0062 |    }
0063 |    const identity = channel.providerIdentities.find((row) => row.currentChannelId === channel.id);
0064 |    if (!identity || !identity.managedLifecycle || identity.provider !== channel.type || identity.buId !== channel.buId) {
0065 |      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
0066 |    }
0067 |    const result: ResolvedChannelCredential = {
0068 |      channelId: channel.id, buId: channel.buId, provider: channel.type, generation: channel.generation,
0069 |      pairingEpoch: channel.pairingEpoch, providerResourceIdentityId: identity.id,
0070 |      externalResourceId: identity.externalResourceId,
0071 |      activeCredentialVersion: channel.type === 'OFICIAL' ? channel.credential?.version ?? null : null,
0072 |      ...(channel.phoneNumberId ? { phoneNumberId: channel.phoneNumberId } : {}),
0073 |      ...(channel.wabaId ? { wabaId: channel.wabaId } : {}),
0074 |      ...(channel.evolutionInstanceName ? { evolutionInstanceName: channel.evolutionInstanceName } : {}),
0075 |    };
0076 |    if (channel.type === 'OFICIAL') {
0077 |      if (!channel.credential || channel.credential.generation !== channel.generation) {
0078 |        throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
0079 |      }
0080 |      const { keyId, key } = loadChannelCredentialKey(process.env);
0081 |      if (channel.credential.keyId !== keyId) throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
0082 |      const plaintext = openChannelCredential({
0083 |        ...channel.credential, nonce: Buffer.from(channel.credential.nonce),
0084 |        ciphertext: Buffer.from(channel.credential.ciphertext), tag: Buffer.from(channel.credential.tag),
0085 |      }, new Map([[keyId, key]]), {
0086 |        purpose: 'active', provider: channel.type, buId: channel.buId, channelId: channel.id,
0087 |        generation: channel.generation, version: channel.credential.version,
0088 |      });
0089 |      result.accessToken = plaintext.toString('utf8');
0090 |    }
0091 |    return result;
0092 |  }
0093 |}
```

## Unchanged critical context api-app/src/domain/inbox/outbound.service.ts

```text
0001 |import { BadRequestException, ConflictException, HttpException, Injectable, ServiceUnavailableException } from '@nestjs/common';
0002 |import { Prisma } from '@prisma/client';
0003 |import { PrismaService } from '../../infra/prisma/prisma.service';
0004 |import { ChannelResolver, type ChannelOperationContext, type VerifiedIngressChannelReference } from '../channels/transport/channel';
0005 |import type { ChannelSendResult, ResolvedChannelOperation } from '../channels/transport/channel';
0006 |import { MessageAcceptanceService, type MessageAcceptanceInput } from './message-acceptance.service';
0007 |import { RealtimeService } from '../../realtime/realtime.service';
0008 |
0009 |const FIXED_UNKNOWN = 'Resultado do envio não confirmado; confira a conversa antes de tentar novamente.';
0010 |const FIXED_LOCAL_INCOMPLETE = 'O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente.';
0011 |const FIXED_REJECTED = 'O canal recusou o envio.';
0012 |const ACK_TIMEOUT_MS = 24 * 60 * 60 * 1000;
0013 |type OutboundConversation = Prisma.ConversationGetPayload<object>;
0014 |
0015 |export type OutboundAttribution =
0016 |  | { kind: 'BFF'; userId: string; name: string }
0017 |  | { kind: 'PUBLIC'; name: string }
0018 |  | { kind: 'BOT'; name: string };
0019 |
0020 |export interface SendOutboundInput {
0021 |  conversationId: string;
0022 |  buId: string;
0023 |  text: string;
0024 |  attribution: OutboundAttribution;
0025 |  ingress?: Omit<VerifiedIngressChannelReference, 'conversationId' | 'buId'>;
0026 |}
0027 |
0028 |@Injectable()
0029 |export class OutboundService {
0030 |  constructor(
0031 |    private readonly prisma: PrismaService,
0032 |    private readonly resolver: ChannelResolver,
0033 |    private readonly acceptance: MessageAcceptanceService,
0034 |    private readonly realtime: RealtimeService,
0035 |  ) {}
0036 |
0037 |  async send(input: SendOutboundInput) {
0038 |    const conversation = await this.prisma.conversation.findFirst({
0039 |      where: { id: input.conversationId, buId: input.buId },
0040 |    });
0041 |    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
0042 |
0043 |    let operation: ResolvedChannelOperation;
0044 |    try {
0045 |      operation = input.ingress
0046 |        ? await this.resolver.resolveForIngress({
0047 |            conversationId: conversation.id, buId: conversation.buId, ...input.ingress,
0048 |          })
0049 |        : await this.resolver.resolveForConversation({ conversationId: conversation.id, buId: conversation.buId });
0050 |    } catch (error) {
0051 |      if (error instanceof HttpException) throw this.asBlocked(error);
0052 |      throw error;
0053 |    }
0054 |
0055 |    if (operation.context.requiresWindow && !await this.windowOpen(conversation.id)) {
0056 |      throw new ConflictException({ code: 'JANELA_FECHADA', outcome: 'BLOCKED', error: 'Fora da janela de 24h da última mensagem recebida.' });
0057 |    }
0058 |
0059 |    let result: ChannelSendResult;
0060 |    try {
0061 |      result = await operation.channel.sendMessage({ kind: 'text', recipientRef: conversation.contact, text: input.text });
0062 |    } catch {
0063 |      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
0064 |    }
0065 |    if (result.outcome === 'BLOCKED') throw this.blocked(result.reason);
0066 |    if (result.outcome === 'REJECTED') {
0067 |      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
0068 |    }
0069 |    if (result.outcome === 'UNKNOWN') return this.finishUnknown(input, conversation, operation.context, result);
0070 |
0071 |    const contextState = await this.contextState(operation.context);
0072 |    if (contextState !== 'CURRENT') {
0073 |      const message = await this.readBack(conversation, operation.context, result.externalMessageId);
0074 |      throw this.acceptedIncomplete(contextState, message ? 'RECORDED' : 'UNCONFIRMED');
0075 |    }
0076 |
0077 |    const acceptanceInput = this.acceptanceInput(input, conversation, operation.context, result.externalMessageId);
0078 |    let accepted: Awaited<ReturnType<MessageAcceptanceService['accept']>>;
0079 |    try {
0080 |      accepted = await this.acceptance.accept(acceptanceInput);
0081 |    } catch {
0082 |      const [after, message] = await Promise.all([
0083 |        this.contextState(operation.context),
0084 |        this.readBack(conversation, operation.context, result.externalMessageId),
0085 |      ]);
0086 |      throw this.acceptedIncomplete(after, message ? 'RECORDED' : 'UNCONFIRMED');
0087 |    }
0088 |
0089 |    let localFailure = false;
0090 |    if (accepted.creationWinner) {
0091 |      try {
0092 |        this.realtime.publicarNaBu(conversation.buId, {
0093 |          tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
0094 |          direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
0095 |        });
0096 |      } catch { localFailure = true; }
0097 |    }
0098 |    try {
0099 |      await this.finalizeOutbound({
0100 |        conversationId: conversation.id, buId: conversation.buId, contact: conversation.contact,
0101 |        contactType: conversation.contactType, attribution: input.attribution,
0102 |      });
0103 |    } catch { localFailure = true; }
0104 |    if (localFailure) {
0105 |      throw this.acceptedIncomplete(await this.contextState(operation.context), 'RECORDED');
0106 |    }
0107 |    return accepted.message;
0108 |  }
0109 |
0110 |  private async finishUnknown(
0111 |    input: SendOutboundInput,
0112 |    conversation: OutboundConversation,
0113 |    context: ChannelOperationContext,
0114 |    result: Extract<ChannelSendResult, { outcome: 'UNKNOWN' }>,
0115 |  ): Promise<never> {
0116 |    if (result.evidence === 'TRANSPORT_UNCONFIRMED') {
0117 |      const state = await this.contextState(context);
0118 |      if (state === 'CHANGED') {
0119 |        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
0120 |      }
0121 |      throw new BadRequestException({ code: result.legacyCode, outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
0122 |    }
0123 |
0124 |    if (await this.contextState(context) === 'CHANGED') {
0125 |      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
0126 |    }
0127 |
0128 |    try {
0129 |      await this.acceptance.recordAmbiguousOutbound(this.acceptanceInput(input, conversation, context));
0130 |    } catch {
0131 |      const state = await this.contextState(context);
0132 |      if (state === 'CHANGED') {
0133 |        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
0134 |      }
0135 |      throw new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
0136 |    }
0137 |
0138 |    const state = await this.contextState(context);
0139 |    if (state === 'CHANGED') {
0140 |      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'RECORDED', error: FIXED_UNKNOWN });
0141 |    }
0142 |    throw new ConflictException({
0143 |      code: 'EXTERNAL_MESSAGE_ID_MISSING', outcome: 'AMBIGUOUS_SEND_RECORDED', evidence: 'ACK_WITHOUT_ID',
0144 |      diagnosticPersistence: 'RECORDED', error: 'O canal aceitou o envio sem confirmar o ID externo. Verifique a conversa antes de tentar novamente.',
0145 |    });
0146 |  }
0147 |
0148 |  private acceptanceInput(
0149 |    input: SendOutboundInput,
0150 |    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
0151 |    context: ChannelOperationContext,
0152 |    externalMessageId: string,
0153 |  ): MessageAcceptanceInput;
0154 |  private acceptanceInput(
0155 |    input: SendOutboundInput,
0156 |    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
0157 |    context: ChannelOperationContext,
0158 |  ): Omit<MessageAcceptanceInput, 'externalMessageId'>;
0159 |  private acceptanceInput(
0160 |    input: SendOutboundInput,
0161 |    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
0162 |    context: ChannelOperationContext,
0163 |    externalMessageId?: string,
0164 |  ): MessageAcceptanceInput | Omit<MessageAcceptanceInput, 'externalMessageId'> {
0165 |    const attribution = input.attribution;
0166 |    return {
0167 |      ...(externalMessageId ? { externalMessageId } : {}),
0168 |      providerResourceIdentityId: context.providerResourceIdentityId,
0169 |      channelId: context.channelId,
0170 |      generation: context.generation,
0171 |      pairingEpoch: context.pairingEpoch,
0172 |      buId: context.buId,
0173 |      channelOrigin: context.channelOrigin,
0174 |      contact: conversation.contact,
0175 |      contactType: conversation.contactType,
0176 |      conversationId: conversation.id,
0177 |      direction: 'OUT',
0178 |      messageType: 'TEXTO',
0179 |      content: input.text,
0180 |      authorUserId: attribution.kind === 'BFF' ? attribution.userId || null : null,
0181 |      authorName: attribution.name,
0182 |      senderResult: true,
0183 |    };
0184 |  }
0185 |
0186 |  private async contextState(context: ChannelOperationContext) {
0187 |    try { return await this.resolver.contextAfterDispatch(context); }
0188 |    catch { return 'UNKNOWN' as const; }
0189 |  }
0190 |
0191 |  private async readBack(
0192 |    conversation: { id: string; buId: string; contact: string },
0193 |    context: ChannelOperationContext,
0194 |    externalMessageId: string,
0195 |  ) {
0196 |    try {
0197 |      return await this.findConfirmedOutbound({
0198 |        providerResourceIdentityId: context.providerResourceIdentityId,
0199 |        externalMessageId, conversationId: conversation.id, buId: conversation.buId,
0200 |        contact: conversation.contact, channelOrigin: context.channelOrigin,
0201 |      });
0202 |    } catch { return null; }
0203 |  }
0204 |
0205 |  private async findConfirmedOutbound(input: {
0206 |    providerResourceIdentityId: string; externalMessageId: string; conversationId: string;
0207 |    buId: string; contact: string; channelOrigin: 'OFICIAL' | 'NAO_OFICIAL';
0208 |  }) {
0209 |    const message = await this.prisma.message.findUnique({
0210 |      where: { providerResourceIdentityId_externalId: {
0211 |        providerResourceIdentityId: input.providerResourceIdentityId,
0212 |        externalId: input.externalMessageId,
0213 |      } }, include: { conversation: true },
0214 |    });
0215 |    if (!message || message.direction !== 'OUT' || message.buId !== input.buId
0216 |      || message.channelOrigin !== input.channelOrigin || message.conversation.contact !== input.contact
0217 |      || message.conversationId !== input.conversationId) return null;
0218 |    return message;
0219 |  }
0220 |
0221 |  private async finalizeOutbound(input: {
0222 |    conversationId: string; buId: string; contact: string; contactType: 'PESSOA' | 'GRUPO'; attribution: OutboundAttribution;
0223 |  }) {
0224 |    return this.prisma.$transaction(async (tx) => {
0225 |      await tx.$queryRaw`SELECT id FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId} FOR UPDATE`;
0226 |      const current = await tx.conversation.findFirst({
0227 |        where: { id: input.conversationId, buId: input.buId, contact: input.contact },
0228 |      });
0229 |      if (!current || current.contactType !== input.contactType) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
0230 |      if (input.attribution.kind === 'BOT') return current;
0231 |
0232 |      const hasOwner = current.attendantUserId !== null || current.attendantName !== null || current.attendantOrigin !== null;
0233 |      return tx.conversation.update({ where: { id: current.id }, data: {
0234 |        lastMessageAt: new Date(),
0235 |        status: input.contactType === 'GRUPO' ? undefined : 'IN_SERVICE',
0236 |        ...(hasOwner || input.contactType === 'GRUPO' ? {} : input.attribution.kind === 'BFF'
0237 |          ? { attendantUserId: input.attribution.userId || null, attendantName: input.attribution.name, attendantOrigin: 'INTERNO' }
0238 |          : { attendantUserId: null, attendantName: input.attribution.name, attendantOrigin: 'EXTERNO' }),
0239 |      } });
0240 |    });
0241 |  }
0242 |
0243 |  private async windowOpen(conversationId: string): Promise<boolean> {
0244 |    const lastInbound = await this.prisma.message.findFirst({
0245 |      where: { conversationId, direction: 'IN' },
0246 |      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
0247 |      select: { createdAt: true },
0248 |    });
0249 |    return Boolean(lastInbound && lastInbound.createdAt.getTime() + ACK_TIMEOUT_MS > Date.now());
0250 |  }
0251 |
0252 |  private asBlocked(error: HttpException): HttpException {
0253 |    const response = error.getResponse();
0254 |    const detail = typeof response === 'object' && response !== null ? response as Record<string, unknown> : { error: response };
0255 |    return new HttpException({ ...detail, outcome: 'BLOCKED' }, error.getStatus());
0256 |  }
0257 |
0258 |  private blocked(reason: Extract<ChannelSendResult, { outcome: 'BLOCKED' }>['reason']): HttpException {
0259 |    if (reason === 'CANAL_AUSENTE') return new BadRequestException({ code: reason, outcome: 'BLOCKED', error: 'Esta BU não tem canal conectado.' });
0260 |    return new ConflictException({ code: reason, outcome: 'BLOCKED', error: 'O canal selecionado não está disponível para envio.' });
0261 |  }
0262 |
0263 |  private acceptedIncomplete(contextState: 'CURRENT' | 'CHANGED' | 'UNKNOWN', localMessageState: 'RECORDED' | 'UNCONFIRMED'): HttpException {
0264 |    if (contextState === 'CHANGED') {
0265 |      return new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
0266 |    }
0267 |    return new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
0268 |  }
0269 |}
```

## Unchanged critical context api-app/src/domain/inbox/outbound.service.spec.ts

```text
0001 |import { describe, expect, it, vi } from 'vitest';
0002 |import type { ChannelOperationContext, ChannelSendResult } from '../channels/transport/channel';
0003 |import { OutboundService } from './outbound.service';
0004 |
0005 |const context: ChannelOperationContext = Object.freeze({
0006 |  channelId: 'channel-1', buId: 'bu-1', channelOrigin: 'OFICIAL', providerResourceIdentityId: 'identity-1',
0007 |  generation: 1, pairingEpoch: 2, activeCredentialVersion: 3, requiresWindow: false,
0008 |});
0009 |const conversation = { id: 'conversation-1', buId: 'bu-1', contact: 'user:opaque', contactType: 'PESSOA' as const };
0010 |
0011 |function setup(result: ChannelSendResult) {
0012 |  const channel = { sendMessage: vi.fn().mockResolvedValue(result) };
0013 |  const resolver = {
0014 |    resolveForConversation: vi.fn().mockResolvedValue({ channel, context }),
0015 |    contextAfterDispatch: vi.fn().mockResolvedValue('CURRENT'),
0016 |  };
0017 |  const acceptance = {
0018 |    recordAmbiguousOutbound: vi.fn().mockResolvedValue({ id: 'diagnostic-1' }),
0019 |    accept: vi.fn().mockResolvedValue({
0020 |      message: { id: 'message-1', channelOrigin: 'OFICIAL' }, creationWinner: false,
0021 |    }),
0022 |  };
0023 |  const prisma = {
0024 |    conversation: { findFirst: vi.fn().mockResolvedValue(conversation) },
0025 |    message: { findUnique: vi.fn().mockResolvedValue(null) },
0026 |    $transaction: vi.fn(),
0027 |  };
0028 |  const realtime = { publicarNaBu: vi.fn() };
0029 |  const service = new OutboundService(prisma as never, resolver as never, acceptance as never, realtime as never);
0030 |  return { service, resolver, acceptance, prisma, channel };
0031 |}
0032 |
0033 |function input() {
0034 |  return { conversationId: conversation.id, buId: conversation.buId, text: 'hello', attribution: { kind: 'BFF' as const, userId: 'user-1', name: 'Agent' } };
0035 |}
0036 |
0037 |describe('OutboundService error projection', () => {
0038 |  it('records one diagnostic only for a valid ACK without external ID', async () => {
0039 |    const { service, acceptance, channel } = setup({ outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'META_RECUSOU' });
0040 |    await expect(service.send(input())).rejects.toMatchObject({
0041 |      status: 409, response: { code: 'EXTERNAL_MESSAGE_ID_MISSING', outcome: 'AMBIGUOUS_SEND_RECORDED', diagnosticPersistence: 'RECORDED' },
0042 |    });
0043 |    expect(channel.sendMessage).toHaveBeenCalledTimes(1);
0044 |    expect(acceptance.recordAmbiguousOutbound).toHaveBeenCalledTimes(1);
0045 |    expect(acceptance.accept).not.toHaveBeenCalled();
0046 |  });
0047 |
0048 |  it('keeps malformed or failed transport unknown without writing a diagnostic', async () => {
0049 |    const { service, acceptance, channel } = setup({ outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' });
0050 |    await expect(service.send(input())).rejects.toMatchObject({
0051 |      status: 400, response: { code: 'META_RECUSOU', outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED' },
0052 |    });
0053 |    expect(channel.sendMessage).toHaveBeenCalledTimes(1);
0054 |    expect(acceptance.recordAmbiguousOutbound).not.toHaveBeenCalled();
0055 |    expect(acceptance.accept).not.toHaveBeenCalled();
0056 |  });
0057 |
0058 |  it('gives a detected post-dispatch identity change precedence before null-ID diagnostics', async () => {
0059 |    const { service, resolver, acceptance } = setup({ outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'META_RECUSOU' });
0060 |    resolver.contextAfterDispatch.mockResolvedValue('CHANGED');
0061 |    await expect(service.send(input())).rejects.toMatchObject({
0062 |      status: 409, response: { code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', diagnosticPersistence: 'UNCONFIRMED' },
0063 |    });
0064 |    expect(acceptance.recordAmbiguousOutbound).not.toHaveBeenCalled();
0065 |  });
0066 |
0067 |  it('returns UNKNOWN/503 when the diagnostic commit is uncertain and context remains current', async () => {
0068 |    const { service, acceptance, resolver } = setup({ outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'SEND_RESULT_UNAVAILABLE' });
0069 |    acceptance.recordAmbiguousOutbound.mockRejectedValue(new Error('fixture commit uncertain'));
0070 |    await expect(service.send(input())).rejects.toMatchObject({
0071 |      status: 503, response: { code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED' },
0072 |    });
0073 |    expect(resolver.contextAfterDispatch).toHaveBeenCalledTimes(2);
0074 |    expect(acceptance.accept).not.toHaveBeenCalled();
0075 |  });
0076 |
0077 |  it('gives a detected context retirement during diagnostic persistence precedence with no external-id write', async () => {
0078 |    const { service, resolver, acceptance } = setup({ outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'SEND_RESULT_UNAVAILABLE' });
0079 |    acceptance.recordAmbiguousOutbound.mockImplementation(async () => {
0080 |      resolver.contextAfterDispatch.mockResolvedValue('CHANGED');
0081 |      throw new Error('identity fence rejected diagnostic transaction');
0082 |    });
0083 |    await expect(service.send(input())).rejects.toMatchObject({
0084 |      status: 409, response: { code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED' },
0085 |    });
0086 |    expect(acceptance.recordAmbiguousOutbound).toHaveBeenCalledTimes(1);
0087 |    expect(acceptance.accept).not.toHaveBeenCalled();
0088 |  });
0089 |
0090 |  it('reports a confirmed diagnostic write as RECORDED if the identity retires immediately afterward', async () => {
0091 |    const { service, resolver, acceptance } = setup({ outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'SEND_RESULT_UNAVAILABLE' });
0092 |    resolver.contextAfterDispatch.mockResolvedValueOnce('CURRENT').mockResolvedValueOnce('CHANGED');
0093 |    await expect(service.send(input())).rejects.toMatchObject({
0094 |      status: 409, response: { code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'RECORDED' },
0095 |    });
0096 |    expect(acceptance.recordAmbiguousOutbound).toHaveBeenCalledTimes(1);
0097 |  });
0098 |
0099 |  it('does not start Message acceptance when the identity changed after an acknowledged send', async () => {
0100 |    const { service, resolver, acceptance, prisma } = setup({ outcome: 'ACCEPTED', externalMessageId: 'external-1' });
0101 |    resolver.contextAfterDispatch.mockResolvedValue('CHANGED');
0102 |    prisma.message.findUnique.mockResolvedValue(null);
0103 |    await expect(service.send(input())).rejects.toMatchObject({
0104 |      status: 409, response: { code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState: 'UNCONFIRMED' },
0105 |    });
0106 |    expect(acceptance.accept).not.toHaveBeenCalled();
0107 |  });
0108 |
0109 |  it('reports uncertainty before local Message acceptance as UNCONFIRMED', async () => {
0110 |    const { service, resolver, acceptance, prisma } = setup({ outcome: 'ACCEPTED', externalMessageId: 'external-1' });
0111 |    acceptance.accept.mockRejectedValue(new Error('fixture transaction did not confirm'));
0112 |    resolver.contextAfterDispatch.mockResolvedValue('CURRENT');
0113 |    prisma.message.findUnique.mockResolvedValue(null);
0114 |    await expect(service.send(input())).rejects.toMatchObject({
0115 |      status: 503, response: { code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState: 'UNCONFIRMED' },
0116 |    });
0117 |  });
0118 |
0119 |  it('reports a confirmed Message commit as RECORDED after a later local finalization failure', async () => {
0120 |    const { service, acceptance, prisma } = setup({ outcome: 'ACCEPTED', externalMessageId: 'external-1' });
0121 |    prisma.$transaction.mockRejectedValue(new Error('fixture conversation finalization failure'));
0122 |    await expect(service.send(input())).rejects.toMatchObject({
0123 |      status: 503, response: { code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState: 'RECORDED' },
0124 |    });
0125 |    expect(acceptance.accept).toHaveBeenCalledTimes(1);
0126 |  });
0127 |
0128 |  it('keeps a known committed Message RECORDED and returns context-changed after a local finalization failure', async () => {
0129 |    const { service, resolver, acceptance, prisma } = setup({ outcome: 'ACCEPTED', externalMessageId: 'external-1' });
0130 |    prisma.$transaction.mockRejectedValue(new Error('fixture finalization failure'));
0131 |    resolver.contextAfterDispatch.mockResolvedValueOnce('CURRENT').mockResolvedValueOnce('CHANGED');
0132 |    await expect(service.send(input())).rejects.toMatchObject({
0133 |      status: 409, response: { code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState: 'RECORDED' },
0134 |    });
0135 |    expect(acceptance.accept).toHaveBeenCalledTimes(1);
0136 |  });
0137 |});
```

## Unchanged critical context api-app/src/domain/inbox/message-acceptance.service.ts

```text
0001 |import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
0002 |import { Prisma } from '@prisma/client';
0003 |import { PrismaService } from '../../infra/prisma/prisma.service';
0004 |import { redactProviderData } from '../channels/safe-redaction';
0005 |
0006 |export interface VerifiedResourceContext {
0007 |  providerResourceIdentityId: string;
0008 |  buId: string;
0009 |  channelId: string;
0010 |  generation: number;
0011 |  pairingEpoch: number;
0012 |  channelOrigin: 'OFICIAL' | 'NAO_OFICIAL';
0013 |}
0014 |
0015 |export interface MessageAcceptanceInput extends VerifiedResourceContext {
0016 |  externalMessageId: string;
0017 |  contact: string;
0018 |  contactType: 'PESSOA' | 'GRUPO';
0019 |  displayName?: string | null;
0020 |  conversationId?: string;
0021 |  direction: 'IN' | 'OUT';
0022 |  messageType: 'TEXTO' | 'IMAGEM' | 'AUDIO' | 'VIDEO' | 'DOCUMENTO' | 'OUTRO';
0023 |  status?: 'RECEBIDA' | 'ENVIADA' | 'ENTREGUE' | 'LIDA' | 'FALHOU';
0024 |  content?: string | null;
0025 |  authorUserId?: string | null;
0026 |  authorName?: string | null;
0027 |  /** True only for an authenticated sender result; echo payloads cannot assert authorship. */
0028 |  senderResult?: boolean;
0029 |}
0030 |
0031 |export interface MessageAcceptanceResult {
0032 |  conversation: Prisma.ConversationGetPayload<object>;
0033 |  message: Prisma.MessageGetPayload<object>;
0034 |  creationWinner: boolean;
0035 |  reconciled: boolean;
0036 |  conversationCreated: boolean;
0037 |  reopened: boolean;
0038 |}
0039 |
0040 |/** Sole transactional owner of keyed Message creation and sender/echo reconciliation. */
0041 |@Injectable()
0042 |export class MessageAcceptanceService {
0043 |  constructor(private readonly prisma: PrismaService) {}
0044 |
0045 |  /** Persist only an allowlist-redacted, identity-scoped diagnostic while the resource fence is held. */
0046 |  async persistVerifiedDiagnostic(
0047 |    context: VerifiedResourceContext,
0048 |    eventType: string,
0049 |    safeMetadata: Record<string, unknown>,
0050 |  ): Promise<void> {
0051 |    if (!/^[A-Za-z0-9_.:-]{1,100}$/.test(eventType)) throw new BadRequestException({ code: 'INVALID_EVENT_TYPE' });
0052 |    await this.prisma.$transaction(async (tx) => {
0053 |      await this.lockAndValidateCurrentIdentity(tx, context);
0054 |      await tx.webhookEvent.create({
0055 |        data: {
0056 |          buId: context.buId, channel: context.channelOrigin, eventType,
0057 |          payload: redactProviderData(safeMetadata) as Prisma.InputJsonValue,
0058 |        },
0059 |      });
0060 |    });
0061 |  }
0062 |
0063 |  /** Persist safe identity/state metadata while fenced, even before own-number proof. */
0064 |  async persistCurrentResourceMetadata(
0065 |    context: VerifiedResourceContext,
0066 |    eventType: string,
0067 |    safeMetadata: Record<string, unknown>,
0068 |  ): Promise<void> {
0069 |    if (!/^[A-Za-z0-9_.:-]{1,100}$/.test(eventType)) throw new BadRequestException({ code: 'INVALID_EVENT_TYPE' });
0070 |    await this.prisma.$transaction(async (tx) => {
0071 |      const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null }>>`
0072 |        SELECT id, bu_id, current_channel_id FROM provider_resource_identities
0073 |        WHERE id = ${context.providerResourceIdentityId} FOR SHARE
0074 |      `;
0075 |      if (!rows[0] || rows[0].bu_id !== context.buId || rows[0].current_channel_id !== context.channelId) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
0076 |      const channel = await tx.buChannel.findFirst({ where: { id: context.channelId, buId: context.buId, type: context.channelOrigin, generation: context.generation, pairingEpoch: context.pairingEpoch }, select: { id: true } });
0077 |      if (!channel) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
0078 |      await tx.webhookEvent.create({ data: { buId: context.buId, channel: context.channelOrigin, eventType, payload: redactProviderData(safeMetadata) as Prisma.InputJsonValue } });
0079 |    });
0080 |  }
0081 |
0082 |  async accept(input: MessageAcceptanceInput): Promise<MessageAcceptanceResult> {
0083 |    if (!input.externalMessageId?.trim()) {
0084 |      throw new BadRequestException({ code: 'EXTERNAL_MESSAGE_ID_REQUIRED' });
0085 |    }
0086 |    if (!input.providerResourceIdentityId || !input.channelId || !input.buId) {
0087 |      throw new BadRequestException({ code: 'VERIFIED_RESOURCE_REQUIRED' });
0088 |    }
0089 |
0090 |    try {
0091 |      return await this.prisma.$transaction(async (tx) => {
0092 |        await this.lockAndValidateCurrentIdentity(tx, input);
0093 |        const key = { providerResourceIdentityId: input.providerResourceIdentityId, externalId: input.externalMessageId };
0094 |        const prior = await tx.message.findUnique({
0095 |          where: { providerResourceIdentityId_externalId: key }, include: { conversation: true },
0096 |        });
0097 |        if (prior) return this.reconcile(tx, prior, input);
0098 |
0099 |        let conversation: Prisma.ConversationGetPayload<object>;
0100 |        let conversationCreated = false;
0101 |        let reopened = false;
0102 |        if (input.direction === 'IN') {
0103 |          const acceptedConversation = await this.acceptIncomingConversation(tx, input);
0104 |          conversation = acceptedConversation.conversation;
0105 |          conversationCreated = acceptedConversation.created;
0106 |          reopened = acceptedConversation.reopened;
0107 |        } else {
0108 |          conversation = await this.loadOutboundConversation(tx, input);
0109 |        }
0110 |        const message = await tx.message.create({
0111 |          data: {
0112 |            conversationId: conversation.id,
0113 |            buId: input.buId,
0114 |            direction: input.direction,
0115 |            messageType: input.messageType,
0116 |            content: input.content ?? null,
0117 |            channelOrigin: input.channelOrigin,
0118 |            status: input.status ?? (input.direction === 'IN' ? 'RECEBIDA' : 'ENVIADA'),
0119 |            externalId: input.externalMessageId,
0120 |            providerResourceIdentityId: input.providerResourceIdentityId,
0121 |            authorUserId: input.senderResult ? input.authorUserId ?? null : null,
0122 |            authorName: input.senderResult ? input.authorName ?? null : null,
0123 |          },
0124 |        });
0125 |        if (input.direction === 'IN') {
0126 |          const now = new Date();
0127 |          await tx.buChannel.updateMany({
0128 |            where: { id: input.channelId, buId: input.buId, generation: input.generation, pairingEpoch: input.pairingEpoch },
0129 |            data: { receiptVerifiedAt: now },
0130 |          });
0131 |          const currentChannel = await tx.buChannel.findUnique({ where: { id: input.channelId }, select: { currentAttemptId: true, providerConnectionState: true, type: true } });
0132 |          const providerReady = currentChannel?.providerConnectionState === 'SUBSCRIBED'
0133 |            || (input.channelOrigin === 'NAO_OFICIAL' && currentChannel?.providerConnectionState === 'CONNECTED');
0134 |          if (providerReady) {
0135 |            await tx.buChannel.updateMany({ where: { id: input.channelId, generation: input.generation, pairingEpoch: input.pairingEpoch }, data: { status: 'CONECTADO', connectedAt: now } });
0136 |          }
0137 |          if (currentChannel?.type === 'NAO_OFICIAL' && currentChannel.currentAttemptId && currentChannel.providerConnectionState === 'CONNECTED') {
0138 |            await tx.buChannel.updateMany({ where: { id: input.channelId, generation: input.generation, pairingEpoch: input.pairingEpoch }, data: { status: 'CONECTADO', connectedAt: now } });
0139 |            await tx.channelRegistrationAttempt.updateMany({ where: { id: currentChannel.currentAttemptId, generation: input.generation, pairingEpoch: input.pairingEpoch, state: { in: ['PENDING_NUMBER', 'PENDING_RECEIPT'] } }, data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', version: { increment: 1 } } });
0140 |          }
0141 |          if (input.channelOrigin === 'OFICIAL' && currentChannel?.currentAttemptId && providerReady) {
0142 |            await tx.channelRegistrationAttempt.updateMany({
0143 |              where: { id: currentChannel.currentAttemptId, state: 'PENDING_RECEIPT', stage: 'SUBSCRIBED' },
0144 |              data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', version: { increment: 1 } },
0145 |            });
0146 |          }
0147 |        }
0148 |        return { conversation, message, creationWinner: true, reconciled: false, conversationCreated, reopened };
0149 |      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
0150 |    } catch (error) {
0151 |      // A concurrent insert may win after our initial lookup. Its transaction
0152 |      // rolled back this attempt's conversation/unread effects atomically.
0153 |      if (!isUniqueViolation(error)) throw error;
0154 |      const prior = await this.prisma.message.findUnique({
0155 |        where: {
0156 |          providerResourceIdentityId_externalId: {
0157 |            providerResourceIdentityId: input.providerResourceIdentityId,
0158 |            externalId: input.externalMessageId,
0159 |          },
0160 |        }, include: { conversation: true },
0161 |      });
0162 |      if (!prior) throw error;
0163 |      return this.prisma.$transaction(async (tx) => {
0164 |        await this.lockAndValidateCurrentIdentity(tx, input);
0165 |        const current = await tx.message.findUniqueOrThrow({
0166 |          where: {
0167 |            providerResourceIdentityId_externalId: {
0168 |              providerResourceIdentityId: input.providerResourceIdentityId,
0169 |              externalId: input.externalMessageId,
0170 |            },
0171 |          }, include: { conversation: true },
0172 |        });
0173 |        return this.reconcile(tx, current, input);
0174 |      });
0175 |    }
0176 |  }
0177 |
0178 |  /** Persist an explicitly ambiguous result after a provider accepted a send but returned no key. */
0179 |  async recordAmbiguousOutbound(input: Omit<MessageAcceptanceInput, 'externalMessageId' | 'status'>): Promise<Prisma.MessageGetPayload<object>> {
0180 |    if (input.direction !== 'OUT' || !input.senderResult) throw new BadRequestException({ code: 'OUTBOUND_RESULT_REQUIRED' });
0181 |    return this.prisma.$transaction(async (tx) => {
0182 |      await this.lockAndValidateCurrentIdentity(tx, input);
0183 |      const conversation = await tx.conversation.findFirst({ where: { id: input.conversationId, buId: input.buId, contact: input.contact } });
0184 |      if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
0185 |      await tx.conversation.update({ where: { id: conversation.id }, data: { lastMessageAt: new Date() } });
0186 |      return tx.message.create({ data: {
0187 |        conversationId: conversation.id, buId: input.buId, direction: 'OUT', messageType: input.messageType,
0188 |        content: input.content ?? null, channelOrigin: input.channelOrigin, status: 'FALHOU', externalId: null,
0189 |        providerResourceIdentityId: input.providerResourceIdentityId, authorUserId: input.authorUserId ?? null,
0190 |        authorName: input.authorName ?? null,
0191 |      } });
0192 |    });
0193 |  }
0194 |
0195 |  private async lockAndValidateCurrentIdentity(tx: Prisma.TransactionClient, input: VerifiedResourceContext): Promise<void> {
0196 |    // Retirement/renewal must update this same identity row before changing the
0197 |    // channel epoch. The lock is held through message commit as the ingress fence.
0198 |    const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null }>>`
0199 |      SELECT id, bu_id, current_channel_id
0200 |      FROM provider_resource_identities
0201 |      WHERE id = ${input.providerResourceIdentityId}
0202 |      FOR SHARE
0203 |    `;
0204 |    const identity = rows[0];
0205 |    if (!identity || identity.bu_id !== input.buId || identity.current_channel_id !== input.channelId) {
0206 |      throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
0207 |    }
0208 |    const channel = await tx.buChannel.findFirst({
0209 |      where: {
0210 |        id: input.channelId, buId: input.buId, generation: input.generation,
0211 |        pairingEpoch: input.pairingEpoch, ownNumberVerified: true, verifiedEpoch: input.pairingEpoch,
0212 |      }, select: { id: true, type: true, currentAttemptId: true },
0213 |    });
0214 |    if (!channel || channel.type !== input.channelOrigin) {
0215 |      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
0216 |    }
0217 |  }
0218 |
0219 |  private async acceptIncomingConversation(tx: Prisma.TransactionClient, input: MessageAcceptanceInput) {
0220 |    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${JSON.stringify([input.buId, input.contact])}, 0))::text AS locked`;
0221 |    const existing = await tx.conversation.findUnique({
0222 |      where: { buId_contact: { buId: input.buId, contact: input.contact } },
0223 |    });
0224 |    if (input.conversationId && existing?.id !== input.conversationId) {
0225 |      throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
0226 |    }
0227 |    const reopens = existing?.status === 'CLOSED' && input.contactType === 'PESSOA';
0228 |    const conversation = await tx.conversation.upsert({
0229 |      where: { buId_contact: { buId: input.buId, contact: input.contact } },
0230 |      create: {
0231 |        buId: input.buId, contact: input.contact, contactType: input.contactType,
0232 |        displayName: input.displayName ?? null,
0233 |        status: 'QUEUED', unreadCount: 1, lastMessageAt: new Date(),
0234 |      },
0235 |      update: {
0236 |        displayName: input.displayName ?? undefined,
0237 |        lastMessageAt: new Date(), unreadCount: { increment: 1 },
0238 |        status: reopens ? 'QUEUED' : undefined,
0239 |        attendantUserId: reopens ? null : undefined,
0240 |        attendantName: reopens ? null : undefined,
0241 |        attendantOrigin: reopens ? null : undefined,
0242 |      },
0243 |    });
0244 |    return { conversation, created: !existing, reopened: Boolean(reopens) };
0245 |  }
0246 |
0247 |  private async loadOutboundConversation(tx: Prisma.TransactionClient, input: MessageAcceptanceInput) {
0248 |    if (!input.conversationId && input.senderResult) throw new BadRequestException({ code: 'CONVERSATION_REQUIRED' });
0249 |    if (input.conversationId) {
0250 |      const conversation = await tx.conversation.findFirst({
0251 |        where: { id: input.conversationId, buId: input.buId, contact: input.contact },
0252 |      });
0253 |      if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
0254 |      return tx.conversation.update({ where: { id: conversation.id }, data: { lastMessageAt: new Date() } });
0255 |    }
0256 |    // An authenticated provider echo can arrive before our send result and can
0257 |    // be the first observed message for this contact. Create an OUT-only
0258 |    // conversation with zero unread; an authenticated sender result above must
0259 |    // always name an already-authorized conversation.
0260 |    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${JSON.stringify([input.buId, input.contact])}, 0))::text AS locked`;
0261 |    return tx.conversation.upsert({
0262 |      where: { buId_contact: { buId: input.buId, contact: input.contact } },
0263 |      create: {
0264 |        buId: input.buId, contact: input.contact, contactType: input.contactType,
0265 |        status: 'QUEUED', unreadCount: 0, lastMessageAt: new Date(),
0266 |      },
0267 |      update: { lastMessageAt: new Date() },
0268 |    });
0269 |  }
0270 |
0271 |  private async reconcile(
0272 |    tx: Prisma.TransactionClient,
0273 |    prior: Prisma.MessageGetPayload<{ include: { conversation: true } }>,
0274 |    input: MessageAcceptanceInput,
0275 |  ): Promise<MessageAcceptanceResult> {
0276 |    const conversation = prior.conversation;
0277 |    if (prior.buId !== input.buId || conversation.buId !== input.buId || conversation.contact !== input.contact
0278 |      || (input.conversationId && conversation.id !== input.conversationId)
0279 |      || prior.direction !== input.direction || prior.channelOrigin !== input.channelOrigin) {
0280 |      throw new ConflictException({ code: 'MESSAGE_IDENTITY_CONFLICT' });
0281 |    }
0282 |    let message = prior;
0283 |    const trustedSenderEnrichment = input.senderResult && !prior.authorUserId && !prior.authorName;
0284 |    if (trustedSenderEnrichment) {
0285 |      message = await tx.message.update({
0286 |        where: { id: prior.id },
0287 |        data: {
0288 |          authorUserId: input.authorUserId ?? null,
0289 |          authorName: input.authorName ?? null,
0290 |          content: input.content ?? prior.content,
0291 |        },
0292 |        include: { conversation: true },
0293 |      });
0294 |    }
0295 |    return { conversation, message, creationWinner: false, reconciled: true, conversationCreated: false, reopened: false };
0296 |  }
0297 |}
0298 |
0299 |function isUniqueViolation(error: unknown): boolean {
0300 |  return error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002';
0301 |}
```

## Unchanged critical context api-app/src/integrations/channels/prisma-channel-resolver.ts

```text
0001 |import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
0002 |import { Prisma } from '@prisma/client';
0003 |import { PrismaService } from '../../infra/prisma/prisma.service';
0004 |import { ChannelCredentialResolver, type ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
0005 |import {
0006 |  ChannelResolver,
0007 |  type ChannelAvailability,
0008 |  type ConversationAvailabilityReference,
0009 |  type ChannelOperationContext,
0010 |  type ChannelOrigin,
0011 |  type ConversationChannelReference,
0012 |  type ResolvedChannelOperation,
0013 |  type VerifiedIngressChannelReference,
0014 |} from '../../domain/channels/transport/channel';
0015 |import { ChannelAdapterRegistry } from './channel-adapter-registry';
0016 |
0017 |type Candidate = {
0018 |  id: string;
0019 |  buId: string;
0020 |  type: ChannelOrigin;
0021 |  status: string;
0022 |  generation: number;
0023 |  pairingEpoch: number;
0024 |  verifiedEpoch: number | null;
0025 |  ownNumberVerified: boolean;
0026 |  providerConnectionState: string;
0027 |  receiptVerifiedAt: Date | null;
0028 |  requiresWindow: boolean;
0029 |  providerIdentities: Array<{ id: string; buId: string; provider: ChannelOrigin; currentChannelId: string | null; managedLifecycle: boolean }>;
0030 |};
0031 |
0032 |@Injectable()
0033 |export class PrismaChannelResolver extends ChannelResolver {
0034 |  constructor(
0035 |    private readonly prisma: PrismaService,
0036 |    private readonly credentials: ChannelCredentialResolver,
0037 |    private readonly adapters: ChannelAdapterRegistry,
0038 |  ) { super(); }
0039 |
0040 |  async resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation> {
0041 |    const { candidate } = await this.selectForConversation(reference);
0042 |    return this.bind(candidate);
0043 |  }
0044 |
0045 |  async resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation> {
0046 |    const conversation = await this.prisma.conversation.findFirst({
0047 |      where: { id: reference.conversationId, buId: reference.buId },
0048 |      select: { id: true, buId: true, contact: true },
0049 |    });
0050 |    if (!conversation) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
0051 |    const candidate = await this.findCandidate(reference.channelId, reference.buId);
0052 |    const identity = candidate?.providerIdentities.find((item) => item.id === reference.providerResourceIdentityId);
0053 |    if (!candidate || candidate.type !== reference.channelOrigin || candidate.generation !== reference.generation
0054 |      || candidate.pairingEpoch !== reference.pairingEpoch || !identity || identity.buId !== reference.buId
0055 |      || identity.provider !== reference.channelOrigin || identity.currentChannelId !== reference.channelId
0056 |      || !identity.managedLifecycle) {
0057 |      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
0058 |    }
0059 |    return this.bind(candidate);
0060 |  }
0061 |
0062 |  async inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability> {
0063 |    try {
0064 |      const conversation = await this.prisma.conversation.findFirst({
0065 |        where: { id: reference.conversationId, buId: reference.buId }, select: { id: true },
0066 |      });
0067 |      if (!conversation) return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
0068 |      const { candidate, selectionReason, selectedOrigin } = await this.selectCandidate(reference);
0069 |      if (!candidate) {
0070 |        return this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL');
0071 |      }
0072 |      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
0073 |      let reason: ChannelAvailability['reason'] = null;
0074 |      if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
0075 |        || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
0076 |        reason = 'CHANNEL_IDENTITY_NOT_VERIFIED';
0077 |      } else if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
0078 |        || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
0079 |        || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
0080 |        || !this.adapters.locallyConfigured(candidate.type)) {
0081 |        reason = 'CHANNEL_NOT_READY';
0082 |      } else if (candidate.type === 'OFICIAL') {
0083 |        const credential = await this.credentials.inspectActiveCredential(candidate.id, candidate.generation);
0084 |        if (!credential.ready) reason = 'PENDING_CREDENTIAL';
0085 |      }
0086 |
0087 |      const window = candidate.requiresWindow ? await this.window(reference.conversationId) : { open: true, expiresAt: null };
0088 |      if (!reason && candidate.requiresWindow && !window.open) reason = 'JANELA_FECHADA';
0089 |      return {
0090 |        available: reason === null,
0091 |        reason,
0092 |        channelOrigin: candidate.type,
0093 |        requiresWindow: candidate.requiresWindow,
0094 |        windowOpen: window.open,
0095 |        expiresAt: window.expiresAt,
0096 |      };
0097 |    } catch {
0098 |      return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
0099 |    }
0100 |  }
0101 |
0102 |  /** Batch-only GET view: BU bindings and credential metadata are read once for the page. */
0103 |  async inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>> {
0104 |    if (!references.length) return new Map();
0105 |    const buId = references[0].buId;
0106 |    if (references.some((reference) => reference.buId !== buId)) {
0107 |      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
0108 |    }
0109 |    try {
0110 |      const ids = references.map(({ conversationId }) => conversationId);
0111 |      const channels = await this.channels(buId);
0112 |      const credentialState = await this.credentials.inspectActiveCredentials(channels
0113 |        .filter((candidate) => candidate.type === 'OFICIAL')
0114 |        .map(({ id, generation }) => ({ channelId: id, generation })));
0115 |      const candidatesWithWindows = channels.filter((candidate) => candidate.requiresWindow);
0116 |      const windows = candidatesWithWindows.length
0117 |        ? await this.latestInboundByConversation(ids)
0118 |        : new Map<string, Date>();
0119 |      const byId = new Map(references.map((reference) => [reference.conversationId, reference]));
0120 |      const result = new Map<string, ChannelAvailability>();
0121 |      for (const id of ids) {
0122 |        const reference = byId.get(id)!;
0123 |        let selectedOrigin = reference.latestMessageOrigin;
0124 |        let candidate: Candidate | null;
0125 |        let selectionReason: ChannelAvailability['reason'] | null = null;
0126 |        if (selectedOrigin) {
0127 |          candidate = channels.find((item) => item.type === selectedOrigin) ?? null;
0128 |          if (!candidate) selectionReason = 'CANAL_SELECIONADO_INDISPONIVEL';
0129 |        } else if (channels.length === 0) {
0130 |          candidate = null; selectionReason = 'CANAL_AUSENTE';
0131 |        } else if (channels.length > 1) {
0132 |          candidate = null; selectionReason = 'CANAL_AMBIGUO';
0133 |        } else {
0134 |          candidate = channels[0]; selectedOrigin = candidate.type;
0135 |        }
0136 |        if (!candidate) {
0137 |          result.set(id, this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL'));
0138 |          continue;
0139 |        }
0140 |        const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
0141 |        let reason: ChannelAvailability['reason'] = null;
0142 |        if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
0143 |          || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
0144 |          reason = 'CHANNEL_IDENTITY_NOT_VERIFIED';
0145 |        } else if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
0146 |          || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
0147 |          || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
0148 |          || !this.adapters.locallyConfigured(candidate.type)) {
0149 |          reason = 'CHANNEL_NOT_READY';
0150 |        } else if (candidate.type === 'OFICIAL' && !credentialState.get(candidate.id)?.ready) {
0151 |          reason = 'PENDING_CREDENTIAL';
0152 |        }
0153 |        let windowOpen = true;
0154 |        let expiresAt: Date | null = null;
0155 |        if (candidate.requiresWindow) {
0156 |          const lastInbound = windows.get(id);
0157 |          windowOpen = Boolean(lastInbound && lastInbound.getTime() + 24 * 60 * 60 * 1000 > Date.now());
0158 |          expiresAt = lastInbound ? new Date(lastInbound.getTime() + 24 * 60 * 60 * 1000) : null;
0159 |          if (!reason && !windowOpen) reason = 'JANELA_FECHADA';
0160 |        }
0161 |        result.set(id, {
0162 |          available: reason === null, reason, channelOrigin: candidate.type,
0163 |          requiresWindow: candidate.requiresWindow, windowOpen, expiresAt,
0164 |        });
0165 |      }
0166 |      return result;
0167 |    } catch {
0168 |      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
0169 |    }
0170 |  }
0171 |
0172 |  async contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
0173 |    try {
0174 |      const status = await this.contextStatus(context, false);
0175 |      return status;
0176 |    } catch {
0177 |      return 'UNKNOWN';
0178 |    }
0179 |  }
0180 |
0181 |  private async bind(candidate: Candidate): Promise<ResolvedChannelOperation> {
0182 |    const availability = await this.inspectCandidate(candidate);
0183 |    if (availability) this.throwUnavailable(availability);
0184 |    const credential = await this.credentials.resolve(candidate.id);
0185 |    const context: ChannelOperationContext = Object.freeze({
0186 |      channelId: candidate.id,
0187 |      buId: candidate.buId,
0188 |      channelOrigin: candidate.type,
0189 |      providerResourceIdentityId: credential.providerResourceIdentityId,
0190 |      generation: credential.generation,
0191 |      pairingEpoch: credential.pairingEpoch,
0192 |      activeCredentialVersion: credential.activeCredentialVersion,
0193 |      requiresWindow: candidate.requiresWindow,
0194 |    });
0195 |    if (!this.sameCredentialContext(candidate, credential)) {
0196 |      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
0197 |    }
0198 |    const factory = this.adapters.get(candidate.type);
0199 |    if (!factory) throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
0200 |    const channel = factory.create(credential, async () => {
0201 |      try { return (await this.contextStatus(context, true)) === 'CURRENT'; }
0202 |      catch { return false; }
0203 |    });
0204 |    return { channel, context };
0205 |  }
0206 |
0207 |  private async inspectCandidate(candidate: Candidate): Promise<ChannelAvailability['reason']> {
0208 |    const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
0209 |    if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
0210 |      || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId) {
0211 |      return 'CHANNEL_IDENTITY_NOT_VERIFIED';
0212 |    }
0213 |    if (candidate.status !== 'CONECTADO' || !candidate.receiptVerifiedAt
0214 |      || (candidate.type === 'OFICIAL' && candidate.providerConnectionState !== 'SUBSCRIBED')
0215 |      || (candidate.type === 'NAO_OFICIAL' && candidate.providerConnectionState !== 'CONNECTED')
0216 |      || !this.adapters.locallyConfigured(candidate.type)) return 'CHANNEL_NOT_READY';
0217 |    if (candidate.type === 'OFICIAL' && !(await this.credentials.inspectActiveCredential(candidate.id, candidate.generation)).ready) {
0218 |      return 'PENDING_CREDENTIAL';
0219 |    }
0220 |    return null;
0221 |  }
0222 |
0223 |  private async selectForConversation(reference: ConversationChannelReference) {
0224 |    const conversation = await this.prisma.conversation.findFirst({
0225 |      where: { id: reference.conversationId, buId: reference.buId },
0226 |      select: { id: true, buId: true, contact: true },
0227 |    });
0228 |    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
0229 |    const { candidate, selectionReason } = await this.selectCandidate(reference);
0230 |    if (!candidate) this.throwUnavailable(selectionReason ?? 'CANAL_AUSENTE');
0231 |    const reason = await this.inspectCandidate(candidate);
0232 |    if (reason) this.throwUnavailable(reason);
0233 |    if (candidate.requiresWindow) {
0234 |      const window = await this.window(conversation.id);
0235 |      if (!window.open) this.throwUnavailable('JANELA_FECHADA');
0236 |    }
0237 |    return { conversation, candidate };
0238 |  }
0239 |
0240 |  private async selectCandidate(reference: ConversationChannelReference): Promise<{
0241 |    candidate: Candidate | null; selectedOrigin: ChannelOrigin | null; selectionReason: ChannelAvailability['reason'] | null;
0242 |  }> {
0243 |    const latest = await this.prisma.message.findFirst({
0244 |      where: { conversationId: reference.conversationId },
0245 |      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
0246 |      select: { channelOrigin: true },
0247 |    });
0248 |    const channels = await this.channels(reference.buId);
0249 |    if (latest) {
0250 |      const selectedOrigin = latest.channelOrigin as ChannelOrigin;
0251 |      const candidate = channels.find((channel) => channel.type === selectedOrigin) ?? null;
0252 |      return { candidate, selectedOrigin, selectionReason: candidate ? null : 'CANAL_SELECIONADO_INDISPONIVEL' };
0253 |    }
0254 |    if (channels.length === 0) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AUSENTE' };
0255 |    if (channels.length > 1) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AMBIGUO' };
0256 |    return { candidate: channels[0], selectedOrigin: channels[0].type, selectionReason: null };
0257 |  }
0258 |
0259 |  private async channels(buId: string): Promise<Candidate[]> {
0260 |    return this.prisma.buChannel.findMany({
0261 |      where: { buId },
0262 |      select: {
0263 |        id: true, buId: true, type: true, status: true, generation: true, pairingEpoch: true,
0264 |        verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
0265 |        receiptVerifiedAt: true, requiresWindow: true,
0266 |        providerIdentities: { select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } },
0267 |      },
0268 |    }) as unknown as Promise<Candidate[]>;
0269 |  }
0270 |
0271 |  private async findCandidate(channelId: string, buId: string): Promise<Candidate | null> {
0272 |    const rows = await this.prisma.buChannel.findMany({ where: { id: channelId, buId }, select: {
0273 |      id: true, buId: true, type: true, status: true, generation: true, pairingEpoch: true,
0274 |      verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
0275 |      receiptVerifiedAt: true, requiresWindow: true,
0276 |      providerIdentities: { select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } },
0277 |    } });
0278 |    return (rows[0] as unknown as Candidate | undefined) ?? null;
0279 |  }
0280 |
0281 |  private async contextStatus(context: ChannelOperationContext, beforeDispatch: boolean): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
0282 |    const where: Prisma.BuChannelWhereInput = {
0283 |      id: context.channelId, buId: context.buId, type: context.channelOrigin,
0284 |      generation: context.generation, pairingEpoch: context.pairingEpoch,
0285 |      ownNumberVerified: true, verifiedEpoch: context.pairingEpoch,
0286 |      ...(beforeDispatch ? {
0287 |        status: 'CONECTADO', receiptVerifiedAt: { not: null },
0288 |        providerConnectionState: context.channelOrigin === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
0289 |      } : {}),
0290 |    };
0291 |    const channel = await this.prisma.buChannel.findFirst({
0292 |      where,
0293 |      select: { id: true, credential: { select: { version: true, generation: true } },
0294 |        providerIdentities: { where: { id: context.providerResourceIdentityId }, select: { id: true, buId: true, provider: true, currentChannelId: true, managedLifecycle: true } } },
0295 |    });
0296 |    const identity = channel?.providerIdentities[0];
0297 |    if (!channel || !identity || identity.buId !== context.buId || identity.provider !== context.channelOrigin
0298 |      || identity.currentChannelId !== context.channelId || !identity.managedLifecycle) {
0299 |      return 'CHANGED';
0300 |    }
0301 |    if (context.channelOrigin === 'OFICIAL') {
0302 |      const credential = channel.credential;
0303 |      if (!credential || credential.generation !== context.generation) return 'CHANGED';
0304 |      if (beforeDispatch && credential.version !== context.activeCredentialVersion) return 'CHANGED';
0305 |    }
0306 |    return 'CURRENT';
0307 |  }
0308 |
0309 |  private async window(conversationId: string): Promise<{ open: boolean; expiresAt: Date | null }> {
0310 |    const lastInbound = await this.prisma.message.findFirst({
0311 |      where: { conversationId, direction: 'IN' }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], select: { createdAt: true },
0312 |    });
0313 |    if (!lastInbound) return { open: false, expiresAt: null };
0314 |    const expiresAt = new Date(lastInbound.createdAt.getTime() + 24 * 60 * 60 * 1000);
0315 |    return { open: expiresAt.getTime() > Date.now(), expiresAt };
0316 |  }
0317 |
0318 |  private async latestInboundByConversation(conversationIds: string[]): Promise<Map<string, Date>> {
0319 |    if (!conversationIds.length) return new Map();
0320 |    const rows = await this.prisma.$queryRaw<Array<{ conversation_id: string; created_at: Date }>>`
0321 |      SELECT requested.conversation_id, latest.created_at
0322 |      FROM unnest(ARRAY[${Prisma.join(conversationIds)}]::text[]) AS requested(conversation_id)
0323 |      CROSS JOIN LATERAL (
0324 |        SELECT message.created_at
0325 |        FROM messages AS message
0326 |        WHERE message.conversation_id = requested.conversation_id AND message.direction = 'IN'
0327 |        ORDER BY message.created_at DESC, message.id DESC
0328 |        LIMIT 1
0329 |      ) AS latest
0330 |    `;
0331 |    return new Map(rows.map((row) => [row.conversation_id, row.created_at]));
0332 |  }
0333 |
0334 |  private sameCredentialContext(candidate: Candidate, credential: ResolvedChannelCredential): boolean {
0335 |    const identity = candidate.providerIdentities.find((item) => item.id === credential.providerResourceIdentityId);
0336 |    return credential.channelId === candidate.id && credential.buId === candidate.buId
0337 |      && credential.provider === candidate.type && credential.generation === candidate.generation
0338 |      && credential.pairingEpoch === candidate.pairingEpoch && identity?.currentChannelId === candidate.id
0339 |      && identity?.buId === candidate.buId && identity.provider === candidate.type;
0340 |  }
0341 |
0342 |  private unavailable(channelOrigin: ChannelOrigin | null, reason: ChannelAvailability['reason']): ChannelAvailability {
0343 |    return { available: false, reason, channelOrigin, requiresWindow: false, windowOpen: false, expiresAt: null };
0344 |  }
0345 |
0346 |  private throwUnavailable(reason: ChannelAvailability['reason']): never {
0347 |    if (reason === 'CANAL_AUSENTE') throw new BadRequestException({ code: reason, error: 'Esta BU não tem canal conectado.' });
0348 |    if (reason === 'CANAL_AMBIGUO') throw new ConflictException({ code: reason, error: 'Selecione uma origem de conversa antes de responder.' });
0349 |    throw new ConflictException({ code: reason, error: reason === 'JANELA_FECHADA'
0350 |      ? 'Fora da janela de 24h da última mensagem recebida.'
0351 |      : 'O canal selecionado não está disponível para envio.' });
0352 |  }
0353 |}
```

## Unchanged critical context api-app/src/integrations/channels/meta-channel.ts

```text
0001 |import type { Channel, ChannelSendResult, TextMessage } from '../../domain/channels/transport/channel';
0002 |import type { MetaClient } from '../meta/meta.client';
0003 |import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
0004 |import { ChannelAdapterFactory } from './channel-adapter-factory';
0005 |
0006 |class BoundMetaChannel implements Channel {
0007 |  constructor(
0008 |    private readonly credential: ResolvedChannelCredential,
0009 |    private readonly client: MetaClient,
0010 |    private readonly beforeDispatch: () => Promise<boolean>,
0011 |  ) {}
0012 |
0013 |  async sendMessage(message: TextMessage): Promise<ChannelSendResult> {
0014 |    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
0015 |    if (!this.credential.phoneNumberId || !this.credential.accessToken) {
0016 |      return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
0017 |    }
0018 |    try {
0019 |      return await this.client.enviarTexto(
0020 |        this.credential.phoneNumberId,
0021 |        message.recipientRef,
0022 |        message.text,
0023 |        this.credential.accessToken,
0024 |      );
0025 |    } catch {
0026 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
0027 |    }
0028 |  }
0029 |}
0030 |
0031 |export class MetaChannelFactory extends ChannelAdapterFactory {
0032 |  readonly origin = 'OFICIAL' as const;
0033 |  constructor(private readonly client: MetaClient) { super(); }
0034 |  locallyConfigured(): boolean { return this.client.canSendText(); }
0035 |  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
0036 |    return new BoundMetaChannel(credential, this.client, beforeDispatch);
0037 |  }
0038 |}
```

## Unchanged critical context api-app/src/integrations/channels/evolution-channel.ts

```text
0001 |import type { Channel, ChannelSendResult, TextMessage } from '../../domain/channels/transport/channel';
0002 |import type { EvolutionClient } from '../evolution/evolution.client';
0003 |import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
0004 |import { ChannelAdapterFactory } from './channel-adapter-factory';
0005 |
0006 |class BoundEvolutionChannel implements Channel {
0007 |  constructor(
0008 |    private readonly credential: ResolvedChannelCredential,
0009 |    private readonly client: EvolutionClient,
0010 |    private readonly beforeDispatch: () => Promise<boolean>,
0011 |  ) {}
0012 |
0013 |  async sendMessage(message: TextMessage): Promise<ChannelSendResult> {
0014 |    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
0015 |    if (!this.credential.evolutionInstanceName) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
0016 |    try {
0017 |      return await this.client.enviarTexto(this.credential.evolutionInstanceName, message.recipientRef, message.text);
0018 |    } catch {
0019 |      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
0020 |    }
0021 |  }
0022 |}
0023 |
0024 |export class EvolutionChannelFactory extends ChannelAdapterFactory {
0025 |  readonly origin = 'NAO_OFICIAL' as const;
0026 |  constructor(private readonly client: EvolutionClient) { super(); }
0027 |  locallyConfigured(): boolean { return this.client.configurado(); }
0028 |  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
0029 |    return new BoundEvolutionChannel(credential, this.client, beforeDispatch);
0030 |  }
0031 |}
```

## Unchanged critical context api-app/src/integrations/channels/channel-adapter-registry.ts

```text
0001 |import { Injectable } from '@nestjs/common';
0002 |import type { ChannelOrigin } from '../../domain/channels/transport/channel';
0003 |import { ChannelAdapterFactory } from './channel-adapter-factory';
0004 |
0005 |/** Explicit provider registration; common consumers never select a provider. */
0006 |@Injectable()
0007 |export class ChannelAdapterRegistry {
0008 |  private readonly factories: ReadonlyMap<ChannelOrigin, ChannelAdapterFactory>;
0009 |
0010 |  constructor(factories: ChannelAdapterFactory[]) {
0011 |    const entries = factories.map((factory) => [factory.origin, factory] as const);
0012 |    if (new Set(entries.map(([origin]) => origin)).size !== entries.length) {
0013 |      throw new Error('Duplicate channel adapter registration.');
0014 |    }
0015 |    this.factories = new Map(entries);
0016 |  }
0017 |
0018 |  get(origin: ChannelOrigin): ChannelAdapterFactory | undefined {
0019 |    return this.factories.get(origin);
0020 |  }
0021 |
0022 |  locallyConfigured(origin: ChannelOrigin): boolean {
0023 |    return this.factories.get(origin)?.locallyConfigured() ?? false;
0024 |  }
0025 |}
```

## Unchanged critical context api-app/src/integrations/channels/channel-transport.module.ts

```text
0001 |import { Module } from '@nestjs/common';
0002 |import { ChannelResolver } from '../../domain/channels/transport/channel';
0003 |import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
0004 |import { MessageAcceptanceService } from '../../domain/inbox/message-acceptance.service';
0005 |import { OutboundService } from '../../domain/inbox/outbound.service';
0006 |import { EVOLUTION_CLIENT, EvolutionHttpClient } from '../evolution/evolution.client';
0007 |import { META_CLIENT, MetaHttpClient } from '../meta/meta.client';
0008 |import { ChannelAdapterRegistry } from './channel-adapter-registry';
0009 |import { EvolutionChannelFactory } from './evolution-channel';
0010 |import { MetaChannelFactory } from './meta-channel';
0011 |import { PrismaChannelResolver } from './prisma-channel-resolver';
0012 |
0013 |@Module({
0014 |  providers: [
0015 |    MessageAcceptanceService,
0016 |    ChannelCredentialResolver,
0017 |    MetaHttpClient,
0018 |    EvolutionHttpClient,
0019 |    { provide: META_CLIENT, useExisting: MetaHttpClient },
0020 |    { provide: EVOLUTION_CLIENT, useExisting: EvolutionHttpClient },
0021 |    {
0022 |      provide: ChannelAdapterRegistry,
0023 |      useFactory: (meta: MetaHttpClient, evolution: EvolutionHttpClient) => new ChannelAdapterRegistry([
0024 |        new MetaChannelFactory(meta),
0025 |        new EvolutionChannelFactory(evolution),
0026 |      ]),
0027 |      inject: [META_CLIENT, EVOLUTION_CLIENT],
0028 |    },
0029 |    PrismaChannelResolver,
0030 |    { provide: ChannelResolver, useExisting: PrismaChannelResolver },
0031 |    OutboundService,
0032 |  ],
0033 |  exports: [
0034 |    MessageAcceptanceService,
0035 |    ChannelCredentialResolver,
0036 |    META_CLIENT,
0037 |    EVOLUTION_CLIENT,
0038 |    ChannelResolver,
0039 |    OutboundService,
0040 |  ],
0041 |})
0042 |export class ChannelTransportModule {}
```

## Unchanged critical context api-app/src/domain/inbox/incoming.service.ts

```text
0001 |import { Inject, Injectable } from '@nestjs/common';
0002 |import { PrismaService } from '../../infra/prisma/prisma.service';
0003 |import { RealtimeService } from '../../realtime/realtime.service';
0004 |import { TYPEBOT_CLIENT, TypebotClient } from '../../integrations/typebot/typebot.client';
0005 |import { MessageAcceptanceService } from './message-acceptance.service';
0006 |import { OutboundService } from './outbound.service';
0007 |import type { ChannelOrigin } from '../channels/transport/channel';
0008 |
0009 |export type CanalDeOrigem = ChannelOrigin;
0010 |
0011 |export interface MensagemRecebida {
0012 |  buId: string;
0013 |  canal: CanalDeOrigem;
0014 |  /** Telefone E.164 só dígitos, ou o identificador do grupo. */
0015 |  contato: string;
0016 |  ehGrupo: boolean;
0017 |  /** Nome do contato, quando o canal informa e ele é confiável (ver webhooks). */
0018 |  nomeExibicao?: string | null;
0019 |  direcao: 'IN' | 'OUT';
0020 |  tipo: 'TEXTO' | 'IMAGEM' | 'AUDIO' | 'VIDEO' | 'DOCUMENTO' | 'OUTRO';
0021 |  conteudo?: string | null;
0022 |  externalId?: string | null;
0023 |  /** Quem respondeu, quando a mensagem saiu por fora do produto. */
0024 |  autorNome?: string | null;
0025 |  providerResourceIdentityId: string;
0026 |  channelId: string;
0027 |  generation: number;
0028 |  pairingEpoch: number;
0029 |}
0030 |
0031 |/**
0032 | * O ponto onde os dois canais viram a MESMA coisa (ADR-0009 §1): uma conversa
0033 | * pendurada na BU, com as mensagens marcadas pelo canal por onde entraram.
0034 | *
0035 | * Os adaptadores de webhook traduzem o formato de cada plataforma para
0036 | * `MensagemRecebida`; daqui para baixo não existe Meta nem Evolution.
0037 | */
0038 |@Injectable()
0039 |export class IncomingService {
0040 |  constructor(
0041 |    private readonly prisma: PrismaService,
0042 |    private readonly realtime: RealtimeService,
0043 |    @Inject(TYPEBOT_CLIENT) private readonly typebot: TypebotClient,
0044 |    private readonly acceptance: MessageAcceptanceService,
0045 |    private readonly outbound: OutboundService,
0046 |  ) {}
0047 |
0048 |  async registrar(m: MensagemRecebida) {
0049 |    const accepted = await this.acceptance.accept({
0050 |      providerResourceIdentityId: m.providerResourceIdentityId, channelId: m.channelId, generation: m.generation,
0051 |      pairingEpoch: m.pairingEpoch, buId: m.buId, channelOrigin: m.canal, externalMessageId: m.externalId ?? '',
0052 |      contact: m.contato, contactType: m.ehGrupo ? 'GRUPO' : 'PESSOA', displayName: m.nomeExibicao,
0053 |      direction: m.direcao, messageType: m.tipo, content: m.conteudo, authorName: m.autorNome,
0054 |    });
0055 |    const { conversation: conversa, message: mensagem, creationWinner } = accepted;
0056 |    if (creationWinner) {
0057 |      this.realtime.publicarNaBu(m.buId, { tipo: 'mensagem', conversaId: conversa.id, contato: conversa.contact, direcao: m.direcao, canal: m.canal, naoLidas: conversa.unreadCount });
0058 |      if (m.direcao === 'IN' && m.tipo === 'TEXTO' && m.conteudo?.trim()) {
0059 |        await this.executarTypebot(m, m.conteudo.trim(), conversa.id, accepted.conversationCreated).catch(() => undefined);
0060 |      }
0061 |    }
0062 |    return { conversa, mensagem, reabriu: accepted.reopened, creationWinner, reconciled: accepted.reconciled };
0063 |  }
0064 |
0065 |  private async executarTypebot(incoming: MensagemRecebida, texto: string, conversationId: string, conversationCreated: boolean): Promise<void> {
0066 |    const { buId, contato } = incoming;
0067 |    const bu = await this.prisma.businessUnit.findUnique({ where: { id: buId }, select: { mantenedoraId: true } });
0068 |    if (!bu) return;
0069 |    const gatilhos = await this.prisma.typebotTrigger.findMany({
0070 |      where: { active: true, bot: { status: 'ATIVO', mantenedoraId: bu.mantenedoraId }, OR: [{ buId: null }, { buId }] },
0071 |      include: { bot: true }, orderBy: { createdAt: 'asc' },
0072 |    });
0073 |    const normalized = texto.toLocaleLowerCase('pt-BR');
0074 |    const gatilho = gatilhos.find((g) => gatilhoCombina(g.kind, g.value, normalized, conversationCreated));
0075 |    if (!gatilho || !this.typebot.configurado()) return;
0076 |    const botId = gatilho.bot.publishedTypebotId;
0077 |    if (!botId) return;
0078 |    const atual = await this.prisma.typebotSession.findUnique({ where: { botId_buId_contato: { botId: gatilho.botId, buId, contato } } });
0079 |    if (atual && (atual.mantenedoraId !== bu.mantenedoraId || atual.buId !== buId || atual.botId !== gatilho.botId || gatilho.bot.mantenedoraId !== bu.mantenedoraId)) return;
0080 |    const resposta = atual?.ativo ? await this.typebot.continuar(atual.sessionId, texto) : await this.typebot.iniciar(botId, contato, texto);
0081 |    const sessionId = 'sessionId' in resposta && typeof resposta.sessionId === 'string' ? resposta.sessionId : null;
0082 |    if (!atual && sessionId) await this.prisma.typebotSession.create({ data: { botId: gatilho.botId, mantenedoraId: gatilho.bot.mantenedoraId, buId, contato, sessionId } });
0083 |    for (const mensagem of resposta.messages) {
0084 |      const saida = textoDaRespostaTypebot(mensagem);
0085 |      if (!saida) continue;
0086 |      await this.outbound.send({
0087 |        conversationId,
0088 |        buId,
0089 |        text: saida,
0090 |        attribution: { kind: 'BOT', name: 'Typebot' },
0091 |        ingress: {
0092 |          channelId: incoming.channelId,
0093 |          providerResourceIdentityId: incoming.providerResourceIdentityId,
0094 |          channelOrigin: incoming.canal,
0095 |          generation: incoming.generation,
0096 |          pairingEpoch: incoming.pairingEpoch,
0097 |        },
0098 |      });
0099 |    }
0100 |  }
0101 |
0102 |}
0103 |
0104 |function textoDaRespostaTypebot(mensagem: unknown): string | null {
0105 |  if (!mensagem || typeof mensagem !== 'object') return null;
0106 |  const m = mensagem as { type?: string; content?: { richText?: unknown; text?: string } };
0107 |  if (m.type !== 'text') return null;
0108 |  if (typeof m.content?.text === 'string') return m.content.text.trim() || null;
0109 |  const juntar = (v: unknown): string => Array.isArray(v) ? v.map(juntar).join('') : v && typeof v === 'object' ? juntar((v as { children?: unknown }).children) : typeof v === 'string' ? v : '';
0110 |  const texto = juntar(m.content?.richText).trim();
0111 |  return texto || null;
0112 |}
0113 |
0114 |export function gatilhoCombina(tipo: 'PALAVRA_CHAVE' | 'NOVA_CONVERSA', valor: string, textoNormalizado: string, novaConversa: boolean): boolean {
0115 |  return tipo === 'NOVA_CONVERSA' ? novaConversa : textoNormalizado.toLocaleLowerCase('pt-BR').includes(valor.toLocaleLowerCase('pt-BR'));
0116 |}
```

## Unchanged critical context api-app/src/domain/inbox/conversations.service.ts

```text
0001 |import {
0002 |  BadRequestException,
0003 |  ConflictException,
0004 |  Injectable,
0005 |  NotFoundException,
0006 |} from '@nestjs/common';
0007 |import { PrismaService } from '../../infra/prisma/prisma.service';
0008 |import { criarCursorTimeline, lerCursorTimeline } from './timeline-pagination';
0009 |import { OutboundService } from './outbound.service';
0010 |import { ChannelResolver, type ChannelOrigin } from '../channels/transport/channel';
0011 |import type { OutboundAttribution } from './outbound.service';
0012 |
0013 |export const JANELA_MS = 24 * 60 * 60 * 1000;
0014 |
0015 |export interface Atendente {
0016 |  userId: string;
0017 |  nome: string;
0018 |}
0019 |
0020 |@Injectable()
0021 |export class ConversationsService {
0022 |  constructor(
0023 |    private readonly prisma: PrismaService,
0024 |    private readonly outbound: OutboundService,
0025 |    private readonly channelResolver: ChannelResolver,
0026 |  ) {}
0027 |
0028 |  /** Carrega a conversa **dentro do escopo**. Fora dele, ninguém sabe que ela existe. */
0029 |  async carregarNoEscopo(conversaId: string, buIdsDoEscopo: string[]) {
0030 |    const conversa = await this.prisma.conversation.findFirst({
0031 |      where: { id: conversaId, buId: { in: buIdsDoEscopo } },
0032 |    });
0033 |    if (!conversa) throw new NotFoundException({ error: 'Não encontrado.', code: 'NAO_ENCONTRADO' });
0034 |    return conversa;
0035 |  }
0036 |
0037 |  /**
0038 |   * A inbox pagina.
0039 |   *
0040 |   * Antes o `take` era 200 fixo, e o que passasse disso era **inalcançável em
0041 |   * silêncio** — nada na resposta dizia que cortou. Teto silencioso é o que vira
0042 |   * "sumiram conversas" seis meses depois; `temMais` é o mínimo para que quem
0043 |   * consome saiba que existe mais.
0044 |   */
0045 |  async listar(
0046 |    buId: string,
0047 |    filtro: { status?: string; grupos?: boolean; minhas?: string; pagina?: number; limite?: number },
0048 |  ) {
0049 |    const limite = Math.min(Math.max(filtro.limite ?? 50, 1), 200);
0050 |    const pagina = Math.max(filtro.pagina ?? 1, 1);
0051 |
0052 |    const where: Record<string, unknown> = { buId };
0053 |    if (filtro.grupos) where.contactType = 'GRUPO';
0054 |    else {
0055 |      where.contactType = 'PESSOA';
0056 |      if (filtro.status) where.status = filtro.status;
0057 |    }
0058 |    if (filtro.minhas) where.attendantUserId = filtro.minhas;
0059 |
0060 |    const [total, conversas] = await Promise.all([
0061 |      this.prisma.conversation.count({ where }),
0062 |      this.prisma.conversation.findMany({
0063 |      where,
0064 |      orderBy: { lastMessageAt: 'desc' },
0065 |      skip: (pagina - 1) * limite,
0066 |      take: limite,
0067 |      select: {
0068 |        id: true,
0069 |        contact: true,
0070 |        contactType: true,
0071 |        displayName: true,
0072 |        status: true,
0073 |        attendantName: true,
0074 |        attendantOrigin: true,
0075 |        unreadCount: true,
0076 |        lastMessageAt: true,
0077 |        // O setor é PROJEÇÃO, não modelo (ADR-0017 §3): vem por junção do
0078 |        // número. Duplicá-lo na conversa criaria a pergunta "e quando o número
0079 |        // muda de setor, o histórico muda junto?" — pergunta que não precisa
0080 |        // existir.
0081 |        bu: { select: { setor: { select: { id: true, name: true } } } },
0082 |      },
0083 |      }),
0084 |    ]);
0085 |
0086 |    return { total, pagina, temMais: pagina * limite < total, conversas };
0087 |  }
0088 |
0089 |  /** Página bounded da timeline; o reconhecimento é uma atualização atômica anterior à leitura. */
0090 |  async timeline(conversaId: string, limite: number, cursor: string | null, marcarLida: boolean) {
0091 |    let ancora: { id: string; createdAt: Date } | null = null;
0092 |    if (cursor) {
0093 |      const decodificado = lerCursorTimeline(cursor);
0094 |      if (decodificado.conversaId !== conversaId) {
0095 |        throw new BadRequestException({
0096 |          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
0097 |        });
0098 |      }
0099 |      ancora = await this.prisma.message.findFirst({
0100 |        where: { id: decodificado.mensagemId, conversationId: conversaId },
0101 |        select: { id: true, createdAt: true },
0102 |      });
0103 |      if (!ancora) {
0104 |        throw new BadRequestException({
0105 |          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
0106 |        });
0107 |      }
0108 |    }
0109 |
0110 |    if (marcarLida) {
0111 |      await this.prisma.conversation.updateMany({
0112 |        where: { id: conversaId }, data: { unreadCount: 0 },
0113 |      });
0114 |    }
0115 |
0116 |    const where = ancora
0117 |      ? {
0118 |          conversationId: conversaId,
0119 |          OR: [
0120 |            { createdAt: { lt: ancora.createdAt } },
0121 |            { createdAt: ancora.createdAt, id: { lt: ancora.id } },
0122 |          ],
0123 |        }
0124 |      : { conversationId: conversaId };
0125 |    const encontradas = await this.prisma.message.findMany({
0126 |      where,
0127 |      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
0128 |      take: limite + 1,
0129 |      select: {
0130 |        id: true, direction: true, messageType: true, content: true,
0131 |        channelOrigin: true, authorName: true, createdAt: true,
0132 |      },
0133 |    });
0134 |    const temAnteriores = encontradas.length > limite;
0135 |    const messages = encontradas.slice(0, limite).reverse();
0136 |    return {
0137 |      messages,
0138 |      paginacao: {
0139 |        limite,
0140 |        temAnteriores,
0141 |        cursorAnterior: temAnteriores && messages.length
0142 |          ? criarCursorTimeline(conversaId, messages[0].id)
0143 |          : null,
0144 |      },
0145 |    };
0146 |  }
0147 |
0148 |  /**
0149 |   * Estado da janela de 24h — **atributo do canal, não do produto** (ADR-0009 §3).
0150 |   *
0151 |   * Numa BU com os dois canais, o canal considerado é o da ÚLTIMA mensagem: a
0152 |   * janela fechada no oficial não libera responder pelo não oficial sozinha.
0153 |   * Trocar de número no meio da conversa é decisão de quem atende, nunca do
0154 |   * sistema.
0155 |   */
0156 |  async estadoDaJanela(conversaId: string, buId: string) {
0157 |    const estado = await this.channelResolver.inspectForConversation({ conversationId: conversaId, buId });
0158 |    return {
0159 |      canal: estado.channelOrigin ? { type: estado.channelOrigin } : null,
0160 |      exigeJanela: estado.requiresWindow,
0161 |      aberta: estado.windowOpen,
0162 |      expiraEm: estado.expiresAt,
0163 |      disponivel: estado.available,
0164 |      motivoIndisponibilidade: estado.reason,
0165 |    };
0166 |  }
0167 |
0168 |  async estadosDasJanelas(references: readonly { conversationId: string; buId: string; latestMessageOrigin: ChannelOrigin | null }[]) {
0169 |    return this.channelResolver.inspectManyForConversations(references);
0170 |  }
0171 |
0172 |  async responder(conversaId: string, buId: string, texto: string, attribution: OutboundAttribution) {
0173 |    return this.outbound.send({ conversationId: conversaId, buId, text: texto, attribution });
0174 |  }
0175 |
0176 |  /** Assumir sem responder. 409 se outro — interno ou externo — já está nela. */
0177 |  async assumir(conversaId: string, atendente: Atendente) {
0178 |    const conversa = await this.prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
0179 |    if (conversa.contactType === 'GRUPO') {
0180 |      throw new BadRequestException({ error: 'Grupos não usam fila de atendimento.', code: 'GRUPO_SEM_FILA' });
0181 |    }
0182 |    if (
0183 |      conversa.status === 'IN_SERVICE' &&
0184 |      conversa.attendantUserId &&
0185 |      conversa.attendantUserId !== atendente.userId
0186 |    ) {
0187 |      throw new ConflictException({
0188 |        error: `Já está sendo atendida por ${conversa.attendantName ?? 'outro agente'}.`,
0189 |        code: 'JA_ATENDIDA',
0190 |      });
0191 |    }
0192 |    if (conversa.status === 'IN_SERVICE' && conversa.attendantOrigin === 'EXTERNO' && !conversa.attendantUserId) {
0193 |      throw new ConflictException({
0194 |        error: `Já está sendo atendida por ${conversa.attendantName ?? 'um sistema externo'}.`,
0195 |        code: 'JA_ATENDIDA',
0196 |      });
0197 |    }
0198 |
0199 |    return this.prisma.conversation.update({
0200 |      where: { id: conversa.id },
0201 |      data: {
0202 |        status: 'IN_SERVICE',
0203 |        attendantUserId: atendente.userId,
0204 |        attendantName: atendente.nome,
0205 |        attendantOrigin: 'INTERNO',
0206 |      },
0207 |    });
0208 |  }
0209 |
0210 |  /** Finalizar. Mensagem nova do contato reabre para QUEUED (ver incoming). */
0211 |  async finalizar(conversaId: string) {
0212 |    const conversa = await this.prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
0213 |    if (conversa.contactType === 'GRUPO') {
0214 |      throw new BadRequestException({ error: 'Grupos não usam fila de atendimento.', code: 'GRUPO_SEM_FILA' });
0215 |    }
0216 |    return this.prisma.conversation.update({
0217 |      where: { id: conversa.id },
0218 |      data: { status: 'CLOSED', attendantUserId: null, attendantName: null, attendantOrigin: null },
0219 |    });
0220 |  }
0221 |}
```

## Unchanged critical context api-app/src/surfaces/bff/conversations.controller.ts

```text
0001 |import { BadRequestException, Body, Controller, Get, HttpCode, Param, Post, Query, Req } from '@nestjs/common';
0002 |import type { Request } from 'express';
0003 |import { AccessService } from '../../domain/access/access.service';
0004 |import { exigirPapelNaBu } from '../../domain/access/require-role';
0005 |import { ConversationsService } from '../../domain/inbox/conversations.service';
0006 |import { RegistroDeAtividade } from '../../domain/historico/registro.service';
0007 |import { ator } from './setores.controller';
0008 |import { validarConsultaTimeline } from '../../domain/inbox/timeline-pagination';
0009 |
0010 |const ABAS = ['QUEUED', 'IN_SERVICE', 'CLOSED'] as const;
0011 |
0012 |/** A inbox por BU (ADR-0009): uma tela para os dois canais. */
0013 |@Controller('api/bff')
0014 |export class ConversationsController {
0015 |  constructor(
0016 |    private readonly access: AccessService,
0017 |    private readonly conversas: ConversationsService,
0018 |    private readonly registro: RegistroDeAtividade,
0019 |  ) {}
0020 |
0021 |  @Get('business-units/:buId/conversations')
0022 |  async listar(
0023 |    @Param('buId') buId: string,
0024 |    @Query() q: Record<string, string>,
0025 |    @Req() req: Request,
0026 |  ) {
0027 |    // Estar no escopo BASTA: com o eixo de capacidades dissolvido (ADR-0018 §3),
0028 |    // quem tem grant na BU atende as conversas dela. Era isso que a capacidade
0029 |    // ATENDIMENTO dizia, e agora quem diz é o papel.
0030 |    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
0031 |
0032 |    const aba = q.aba?.toUpperCase();
0033 |    const r = await this.conversas.listar(buId, {
0034 |      grupos: aba === 'GRUPO',
0035 |      status: ABAS.includes(aba as (typeof ABAS)[number]) ? aba : undefined,
0036 |      minhas: q.minhas === 'true' ? req.usuario!.id : undefined,
0037 |      pagina: q.pagina ? Number(q.pagina) : undefined,
0038 |      limite: q.limite ? Number(q.limite) : undefined,
0039 |    });
0040 |    // O setor sobe achatado, como a tela o consome (`conversa.setor`).
0041 |    return {
0042 |      total: r.total,
0043 |      pagina: r.pagina,
0044 |      temMais: r.temMais,
0045 |      conversations: r.conversas.map(({ bu, ...c }) => ({ ...c, setor: bu.setor.name })),
0046 |    };
0047 |  }
0048 |
0049 |  @Get('conversations/:id/messages')
0050 |  async thread(@Param('id') id: string, @Query() q: Record<string, unknown>, @Req() req: Request) {
0051 |    const { conversa } = await this.resolver(id, req);
0052 |    // Validar somente depois do resolver: recurso fora do escopo permanece 404,
0053 |    // mesmo quando os parâmetros enviados são inválidos.
0054 |    const consulta = validarConsultaTimeline(q);
0055 |    const timeline = await this.conversas.timeline(
0056 |      conversa.id, consulta.limite, consulta.antes, consulta.marcarLida,
0057 |    );
0058 |
0059 |    const janela = await this.conversas.estadoDaJanela(conversa.id, conversa.buId);
0060 |    return {
0061 |      conversa: {
0062 |        id: conversa.id,
0063 |        contato: conversa.contact,
0064 |        nome: conversa.displayName,
0065 |        status: conversa.status,
0066 |        atendente: conversa.attendantName,
0067 |      },
0068 |      // O front precisa saber que "responder" pode estar indisponível, e por quê.
0069 |      janela: {
0070 |        exigida: janela.exigeJanela,
0071 |        aberta: janela.aberta,
0072 |        expiraEm: janela.expiraEm,
0073 |        canal: janela.canal?.type ?? null,
0074 |        disponivel: janela.disponivel,
0075 |        motivo: janela.motivoIndisponibilidade,
0076 |      },
0077 |      messages: timeline.messages,
0078 |      paginacao: timeline.paginacao,
0079 |    };
0080 |  }
0081 |
0082 |  @Post('conversations/:id/messages')
0083 |  @HttpCode(201)
0084 |  async responder(@Param('id') id: string, @Body() body: { texto?: string }, @Req() req: Request) {
0085 |    const { conversa } = await this.resolver(id, req);
0086 |
0087 |    const texto = String(body?.texto ?? '').trim();
0088 |    if (!texto) throw new BadRequestException({ error: 'Escreva uma mensagem.', code: 'TEXTO_VAZIO' });
0089 |    if (texto.length > 4096) {
0090 |      throw new BadRequestException({ error: 'Mensagem muito longa (máx. 4096).', code: 'TEXTO_LONGO' });
0091 |    }
0092 |
0093 |    const m = await this.conversas.responder(conversa.id, conversa.buId, texto, {
0094 |      kind: 'BFF',
0095 |      userId: req.usuario!.id,
0096 |      name: req.usuario!.nome,
0097 |    });
0098 |    return { id: m.id, canal: m.channelOrigin, em: m.createdAt };
0099 |  }
0100 |
0101 |  @Post('conversations/:id/claim')
0102 |  async assumir(@Param('id') id: string, @Req() req: Request) {
0103 |    const { conversa } = await this.resolver(id, req);
0104 |
0105 |    const c = await this.conversas.assumir(conversa.id, { userId: req.usuario!.id, nome: req.usuario!.nome });
0106 |    await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.assumido', ator(req), {
0107 |      buId: conversa.buId,
0108 |      entidadeId: conversa.id,
0109 |      frase: { contato: conversa.contact },
0110 |    });
0111 |    return { id: c.id, status: c.status, atendente: c.attendantName };
0112 |  }
0113 |
0114 |  @Post('conversations/:id/close')
0115 |  async finalizar(@Param('id') id: string, @Req() req: Request) {
0116 |    const { conversa } = await this.resolver(id, req);
0117 |
0118 |    const c = await this.conversas.finalizar(conversa.id);
0119 |    await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.encerrado', ator(req), {
0120 |      buId: conversa.buId,
0121 |      entidadeId: conversa.id,
0122 |      frase: { contato: conversa.contact },
0123 |    });
0124 |    return { id: c.id, status: c.status };
0125 |  }
0126 |
0127 |  /** Escopo primeiro: fora dele, 404 — inclusive para BU de outra Mantenedora. */
0128 |  private async resolver(conversaId: string, req: Request) {
0129 |    const escopo = await this.access.escopo(req.usuario!.id);
0130 |    const conversa = await this.conversas.carregarNoEscopo(conversaId, escopo);
0131 |    const bu = await exigirPapelNaBu(this.access, req.usuario!.id, conversa.buId, 'ATENDENTE');
0132 |    return { conversa, papel: bu.papel };
0133 |  }
0134 |}
```

## Unchanged critical context api-app/src/surfaces/public/conversations.controller.ts

```text
0001 |import {
0002 |  BadRequestException,
0003 |  Body,
0004 |  Controller,
0005 |  ForbiddenException,
0006 |  Get,
0007 |  HttpCode,
0008 |  HttpException,
0009 |  Param,
0010 |  Post,
0011 |  Query,
0012 |  Req,
0013 |  Res,
0014 |} from '@nestjs/common';
0015 |import type { Request, Response } from 'express';
0016 |import { ApiKeyService } from '../../domain/integration/api-key.service';
0017 |import { RateLimitService } from '../../domain/integration/rate-limit.service';
0018 |import { ConversationsService } from '../../domain/inbox/conversations.service';
0019 |import { PrismaService } from '../../infra/prisma/prisma.service';
0020 |
0021 |const TETO = 500;
0022 |
0023 |/**
0024 | * Superfície pública v1 (ADR-0010) — o contrato do parceiro.
0025 | *
0026 | * `account_id` continua se chamando assim e passa a valer o **UUID da BU**: o
0027 | * parceiro já integrou esse nome com esse significado nos dois sistemas antigos,
0028 | * e trocá-lo daria trabalho a ele sem entregar clareza.
0029 | */
0030 |@Controller('api/v1')
0031 |export class PublicConversationsController {
0032 |  constructor(
0033 |    private readonly chaves: ApiKeyService,
0034 |    private readonly conversas: ConversationsService,
0035 |    private readonly limite: RateLimitService,
0036 |    private readonly prisma: PrismaService,
0037 |  ) {}
0038 |
0039 |  @Get('accounts')
0040 |  async accounts(@Req() req: Request) {
0041 |    const ids = await this.chaves.busDaChave(req.chave!);
0042 |    const bus = await this.prisma.businessUnit.findMany({
0043 |      where: { id: { in: ids } },
0044 |      select: { id: true, name: true, phone: true, channels: { select: { type: true, status: true } } },
0045 |      orderBy: { name: 'asc' },
0046 |    });
0047 |
0048 |    return {
0049 |      accounts: bus.map((b) => ({
0050 |        id: b.id,
0051 |        name: b.name,
0052 |        numero: b.phone,
0053 |        canais: b.channels.map((c) => ({ tipo: c.type, conectado: c.status === 'CONECTADO' })),
0054 |      })),
0055 |    };
0056 |  }
0057 |
0058 |  @Get('conversations')
0059 |  async conversations(@Query() q: Record<string, string>, @Req() req: Request) {
0060 |    const buId = await this.resolverConta(req, q.account_id);
0061 |    const periodo = periodoDe(q.de, q.ate);
0062 |    const limite = Math.min(Number(q.limit) || 200, TETO);
0063 |
0064 |    const where: Record<string, unknown> = { buId, contactType: 'PESSOA' };
0065 |    if (periodo) where.lastMessageAt = { gte: periodo.de, lte: periodo.ate };
0066 |    if (q.q?.trim()) {
0067 |      where.OR = [
0068 |        { displayName: { contains: q.q.trim(), mode: 'insensitive' } },
0069 |        { contact: { contains: q.q.trim() } },
0070 |      ];
0071 |    }
0072 |
0073 |    const linhas = await this.prisma.conversation.findMany({
0074 |      where,
0075 |      orderBy: { lastMessageAt: 'desc' },
0076 |      take: limite + 1,
0077 |      include: { messages: { orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], take: 1 } },
0078 |    });
0079 |
0080 |    const pagina = linhas.slice(0, limite);
0081 |    const estados = await this.conversas.estadosDasJanelas(pagina.map((c) => ({
0082 |      conversationId: c.id, buId, latestMessageOrigin: c.messages[0]?.channelOrigin ?? null,
0083 |    })));
0084 |    const conversas = pagina.map((c) => {
0085 |        const janela = estados.get(c.id);
0086 |        return {
0087 |          telefone: c.contact,
0088 |          nome_whatsapp: c.displayName,
0089 |          status: c.status,
0090 |          atendendo: c.attendantName,
0091 |          ultima_mensagem: c.messages[0]?.content ?? null,
0092 |          ultima_direcao: c.messages[0] ? (c.messages[0].direction === 'OUT' ? 'enviada' : 'recebida') : null,
0093 |          ultima_em: c.lastMessageAt?.toISOString() ?? null,
0094 |          nao_lidas: c.unreadCount,
0095 |          // Campo generalizado: quem integrou só o Hub recebe `true` e não muda
0096 |          // nada; quem integrou a Central continua lendo o que já lia.
0097 |          janela_aberta: janela?.windowOpen ?? false,
0098 |          janela_expira_em: janela?.expiresAt?.toISOString() ?? null,
0099 |          envio_disponivel: janela?.available ?? false,
0100 |          motivo_indisponibilidade: janela ? janela.reason : 'CANAL_SELECIONADO_INDISPONIVEL',
0101 |        };
0102 |      });
0103 |
0104 |    return { conta: { id: buId }, conversations: conversas, truncado: linhas.length > limite };
0105 |  }
0106 |
0107 |  @Get('conversations/:telefone/messages')
0108 |  async messages(
0109 |    @Param('telefone') telefone: string,
0110 |    @Query() q: Record<string, string>,
0111 |    @Req() req: Request,
0112 |  ) {
0113 |    const buId = await this.resolverConta(req, q.account_id);
0114 |    const conversa = await this.conversaDoTelefone(buId, telefone);
0115 |    const limite = Math.min(Number(q.limit) || 100, TETO);
0116 |
0117 |    const mensagens = await this.prisma.message.findMany({
0118 |      where: {
0119 |        conversationId: conversa.id,
0120 |        // `since` permite sync incremental: o parceiro guarda a data da última
0121 |        // mensagem copiada e pede só o que veio depois.
0122 |        ...(q.since ? { createdAt: { gt: new Date(q.since) } } : {}),
0123 |      },
0124 |      orderBy: { createdAt: 'asc' },
0125 |      take: limite,
0126 |    });
0127 |
0128 |    const janela = await this.conversas.estadoDaJanela(conversa.id, buId);
0129 |    return {
0130 |      telefone: conversa.contact,
0131 |      janela_aberta: janela.aberta,
0132 |      envio_disponivel: janela.disponivel,
0133 |      motivo_indisponibilidade: janela.motivoIndisponibilidade,
0134 |      messages: mensagens.map((m) => ({
0135 |        id: m.id,
0136 |        direcao: m.direction === 'OUT' ? 'enviada' : 'recebida',
0137 |        tipo: m.messageType,
0138 |        texto: m.content,
0139 |        canal: m.channelOrigin,
0140 |        respondido_por: m.authorName,
0141 |        // Data SEMPRE em ISO-8601 UTC: API externa não pode entregar formato variável.
0142 |        em: m.createdAt.toISOString(),
0143 |      })),
0144 |    };
0145 |  }
0146 |
0147 |  @Post('messages')
0148 |  @HttpCode(201)
0149 |  async enviar(@Body() body: Record<string, string>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
0150 |    const buId = await this.resolverConta(req, body?.account_id);
0151 |    const telefone = String(body?.telefone ?? '').replace(/\D/g, '');
0152 |    const texto = String(body?.texto ?? '').trim();
0153 |    if (!telefone) throw new BadRequestException({ error: 'Informe o telefone.', code: 'TELEFONE_INVALIDO' });
0154 |    if (!texto) throw new BadRequestException({ error: 'Informe o texto.', code: 'TEXTO_VAZIO' });
0155 |    if (texto.length > 4096) throw new BadRequestException({ error: 'Texto muito longo.', code: 'TEXTO_LONGO' });
0156 |
0157 |    const espera = this.limite.consumir(req.chave!.id, buId);
0158 |    if (espera > 0) {
0159 |      res.setHeader('Retry-After', String(espera));
0160 |      throw new HttpException({ error: 'Ritmo acima do permitido.', code: 'LIMITE_DE_TAXA' }, 429);
0161 |    }
0162 |
0163 |    const conversa = await this.conversaOuNova(buId, telefone);
0164 |    const atendente = String(body?.atendente ?? '').trim() || req.chave!.nome;
0165 |    const m = await this.conversas.responder(conversa.id, buId, texto, { kind: 'PUBLIC', name: atendente });
0166 |
0167 |    return { ok: true, message_id: m.id, canal: m.channelOrigin };
0168 |  }
0169 |
0170 |  @Post('conversations/:telefone/claim')
0171 |  async claim(@Param('telefone') telefone: string, @Body() body: Record<string, string>, @Req() req: Request) {
0172 |    const buId = await this.resolverConta(req, body?.account_id);
0173 |    const conversa = await this.conversaDoTelefone(buId, telefone);
0174 |    const atendente = String(body?.atendente ?? '').trim() || req.chave!.nome;
0175 |
0176 |    if (conversa.status === 'IN_SERVICE' && conversa.attendantName && conversa.attendantName !== atendente) {
0177 |      throw new HttpException(
0178 |        { error: `Já está sendo atendida por ${conversa.attendantName}.`, code: 'JA_ATENDIDA' },
0179 |        409,
0180 |      );
0181 |    }
0182 |    await this.prisma.conversation.update({
0183 |      where: { id: conversa.id },
0184 |      data: { status: 'IN_SERVICE', attendantName: atendente, attendantOrigin: 'EXTERNO', attendantUserId: null },
0185 |    });
0186 |    return { ok: true };
0187 |  }
0188 |
0189 |  @Post('conversations/:telefone/release')
0190 |  async release(@Param('telefone') telefone: string, @Body() body: Record<string, string>, @Req() req: Request) {
0191 |    const buId = await this.resolverConta(req, body?.account_id);
0192 |    const conversa = await this.conversaDoTelefone(buId, telefone);
0193 |    await this.prisma.conversation.update({
0194 |      where: { id: conversa.id },
0195 |      data: { status: 'QUEUED', attendantName: null, attendantOrigin: null, attendantUserId: null },
0196 |    });
0197 |    return { ok: true };
0198 |  }
0199 |
0200 |  /** A conta pedida precisa estar no escopo DA CHAVE — e o escopo nulo nunca sai da Mantenedora. */
0201 |  private async resolverConta(req: Request, accountId?: string): Promise<string> {
0202 |    if (!accountId) {
0203 |      throw new BadRequestException({ error: 'Informe o account_id.', code: 'CONTA_NAO_INFORMADA' });
0204 |    }
0205 |    const permitidas = await this.chaves.busDaChave(req.chave!);
0206 |    if (!permitidas.includes(accountId)) {
0207 |      throw new ForbiddenException({
0208 |        error: 'Esta chave não tem acesso a essa conta.',
0209 |        code: 'SEM_ACESSO_A_CONTA',
0210 |      });
0211 |    }
0212 |    return accountId;
0213 |  }
0214 |
0215 |  private async conversaDoTelefone(buId: string, telefone: string) {
0216 |    const conversa = await this.prisma.conversation.findUnique({
0217 |      where: { buId_contact: { buId, contact: telefone.replace(/\D/g, '') } },
0218 |    });
0219 |    if (!conversa) {
0220 |      throw new BadRequestException({ error: 'Conversa não encontrada.', code: 'CONVERSA_NAO_ENCONTRADA' });
0221 |    }
0222 |    return conversa;
0223 |  }
0224 |
0225 |  private async conversaOuNova(buId: string, telefone: string) {
0226 |    return this.prisma.conversation.upsert({
0227 |      where: { buId_contact: { buId, contact: telefone } },
0228 |      create: { buId, contact: telefone, contactType: 'PESSOA', status: 'IN_SERVICE' },
0229 |      update: {},
0230 |    });
0231 |  }
0232 |}
0233 |
0234 |function periodoDe(de?: string, ate?: string): { de: Date; ate: Date } | null {
0235 |  if (!de || !ate) return null;
0236 |  if (!/^\d{4}-\d{2}-\d{2}$/.test(de) || !/^\d{4}-\d{2}-\d{2}$/.test(ate)) {
0237 |    throw new BadRequestException({ error: 'Use de e ate no formato AAAA-MM-DD.', code: 'PERIODO_INVALIDO' });
0238 |  }
0239 |  return { de: new Date(`${de}T00:00:00.000Z`), ate: new Date(`${ate}T23:59:59.999Z`) };
0240 |}
```

## Unchanged critical context api-app/test/helpers.ts

```text
0001 |import { INestApplication } from '@nestjs/common';
0002 |import { Test } from '@nestjs/testing';
0003 |import type { NestExpressApplication } from '@nestjs/platform-express';
0004 |import request from 'supertest';
0005 |import { AppModule } from '../src/app.module';
0006 |import { ChannelAdapterRegistry } from '../src/integrations/channels/channel-adapter-registry';
0007 |import { configurarBodyParsers } from '../src/infra/http/body-parsers';
0008 |import { PrismaService } from '../src/infra/prisma/prisma.service';
0009 |import { EVOLUTION_CLIENT, EvolutionClient } from '../src/integrations/evolution/evolution.client';
0010 |import { META_CLIENT, MetaClient, MetaIndisponivelError } from '../src/integrations/meta/meta.client';
0011 |import { TYPEBOT_CLIENT, TypebotClient } from '../src/integrations/typebot/typebot.client';
0012 |import { sealChannelCredential } from '../src/domain/channels/channel-credential-crypto';
0013 |
0014 |/** Dublês das portas de saída: o teste prova permissão, não a Meta. */
0015 |export const metaFake: MetaClient & { wabaRecusada: string | null; wabaRecursos: { wabaId: string; phoneNumberId: string; telefone: string }[]; enviados: { para: string; texto: string }[]; credentialByPhone: Map<string, string>; credentialCalls: { phoneNumberId: string; accessToken: string }[]; registrosNumero: number; subscriptionHook: (() => Promise<void>) | null; confirmHook: (() => Promise<void>) | null; registrosHook: (() => Promise<void>) | null; sendHook: ((id: string, para: string, texto: string) => Promise<void>) | null; confirmCalls: number; exchangeCalls: number; exchangeFails: number; providerCalls: number; sendIdNull: boolean } = {
0016 |  wabaRecusada: null,
0017 |  wabaRecursos: [
0018 |    { wabaId: '123456789', phoneNumberId: '111111111', telefone: '5584998880000' },
0019 |    { wabaId: '123456789', phoneNumberId: '987654321', telefone: '5584999990000' },
0020 |    { wabaId: '555555555', phoneNumberId: '222222222', telefone: '5584997770000' },
0021 |  ],
0022 |  enviados: [],
0023 |  credentialByPhone: new Map(),
0024 |  credentialCalls: [],
0025 |  registrosNumero: 0,
0026 |  subscriptionHook: null,
0027 |  confirmHook: null,
0028 |  registrosHook: null,
0029 |  sendHook: null,
0030 |  confirmCalls: 0,
0031 |  exchangeCalls: 0,
0032 |  exchangeFails: 0,
0033 |  providerCalls: 0,
0034 |  sendIdNull: false,
0035 |  capabilities: () => ({ appId: 'fixture-app', configId: 'fixture-config', graphVersion: 'v26.0', available: true, reason: 'AVAILABLE' }),
0036 |  async exchangeCode() {
0037 |    metaFake.providerCalls += 1; metaFake.exchangeCalls += 1;
0038 |    if (metaFake.exchangeFails > 0) { metaFake.exchangeFails -= 1; throw new Error('fixture exchange response lost'); }
0039 |    return { accessToken: 'fixture-scoped-token' };
0040 |  },
0041 |  async recursos(accessToken, wabaId, after) {
0042 |    metaFake.providerCalls += 1;
0043 |    if (accessToken !== 'fixture-scoped-token') throw new Error('scoped credential required');
0044 |    if (wabaId && metaFake.wabaRecusada === wabaId) throw new Error('WABA recusada');
0045 |    const targets = metaFake.wabaRecursos.filter((r) => !wabaId || r.wabaId === wabaId);
0046 |    const page = after ? targets.slice(1) : targets.slice(0, 1);
0047 |    return { wabas: wabaId ? [{ id: wabaId, name: 'Fixture' }] : [...new Map(targets.map((r) => [r.wabaId, { id: r.wabaId, name: 'Fixture' }])).values()], numbers: page.map((r) => ({ id: r.phoneNumberId, telefone: r.telefone, nomeVerificado: 'Fixture' })), next: !after && targets.length > 1 ? 'fixture-page-1' : null };
0048 |  },
0049 |  async enviarTexto(phoneNumberId: string, para: string, texto: string, accessToken?: string) {
0050 |    metaFake.providerCalls += 1;
0051 |    metaFake.credentialCalls.push({ phoneNumberId, accessToken: accessToken ?? '' });
0052 |    const expected = metaFake.credentialByPhone.get(phoneNumberId) ?? 'fixture-scoped-token';
0053 |    if (accessToken !== expected) throw new Error('scoped credential required');
0054 |    metaFake.enviados.push({ para, texto });
0055 |    const id = `wamid-enviado-${metaFake.enviados.length}`;
0056 |    await metaFake.sendHook?.(id, para, texto);
0057 |    return metaFake.sendIdNull
0058 |      ? { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'META_RECUSOU' }
0059 |      : { outcome: 'ACCEPTED', externalMessageId: id };
0060 |  },
0061 |  configurado: () => true,
0062 |  canSendText: () => true,
0063 |  async numerosDaWaba(wabaId: string, accessToken?: string, after?: string) {
0064 |    metaFake.providerCalls += 1;
0065 |    if (metaFake.wabaRecusada === wabaId || accessToken !== 'fixture-scoped-token') throw new Error('WABA recusada');
0066 |    const targets = metaFake.wabaRecursos.filter((r) => r.wabaId === wabaId); const page = after ? targets.slice(1) : targets.slice(0, 1);
0067 |    return { data: page.map((r) => ({ id: r.phoneNumberId, telefone: r.telefone, nomeVerificado: `WABA ${wabaId}` })), next: !after && targets.length > 1 ? 'fixture-page-1' : null };
0068 |  },
0069 |  async confirmarNumero(wabaId, phoneNumberId, accessToken, after) {
0070 |    metaFake.providerCalls += 1;
0071 |    metaFake.confirmCalls += 1;
0072 |    await metaFake.confirmHook?.();
0073 |    const page = await metaFake.numerosDaWaba(wabaId, accessToken, after);
0074 |    return page.data.find((item) => item.id === phoneNumberId) ?? null;
0075 |  },
0076 |  async verificarNumeroVinculado(wabaId, phoneNumberId, accessToken) {
0077 |    metaFake.confirmCalls += 1;
0078 |    await metaFake.confirmHook?.();
0079 |    const seen = new Set<string>(); let after: string | undefined;
0080 |    for (let index = 0; index < 2; index += 1) {
0081 |      const page = await metaFake.numerosDaWaba(wabaId, accessToken, after);
0082 |      const number = page.data.find((item) => item.id === phoneNumberId);
0083 |      if (number) return number;
0084 |      if (!page.next) return null;
0085 |      if (page.next.length > 512 || seen.has(page.next) || index === 1) throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
0086 |      seen.add(page.next); after = page.next;
0087 |    }
0088 |    throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
0089 |  },
0090 |  async registrarNumero(_phoneNumberId, pin, accessToken) { metaFake.providerCalls += 1; if (accessToken !== 'fixture-scoped-token' || !/^\d{6}$/.test(pin)) throw new Error('scoped registration credential required'); metaFake.registrosNumero += 1; await metaFake.registrosHook?.(); },
0091 |  async inscreverWaba(_wabaId, accessToken) { metaFake.providerCalls += 1; if (accessToken !== 'fixture-scoped-token') throw new Error('scoped subscription credential required'); await metaFake.subscriptionHook?.(); },
0092 |};
0093 |
0094 |export const evolutionFake: EvolutionClient & { enviados: { para: string; texto: string }[]; inventory: Map<string, { name: string; ownerJid: string | null; connectionStatus: string | null }>; createCalls: number; providerCalls: number; sendIdNull: boolean; sendHook: ((id: string, para: string, texto: string) => Promise<void>) | null; createHook: ((name: string) => Promise<void>) | null; ownerPhone: string | null; createdState: string; deleteFails: boolean } = {
0095 |  enviados: [], inventory: new Map(), createCalls: 0, providerCalls: 0,
0096 |  sendHook: null,
0097 |  createHook: null,
0098 |  configurado: () => true,
0099 |  async enviarTexto(_instancia: string, para: string, texto: string) {
0100 |    evolutionFake.providerCalls += 1;
0101 |    evolutionFake.enviados.push({ para, texto });
0102 |    const id = `evo-enviado-${evolutionFake.enviados.length}`;
0103 |    await evolutionFake.sendHook?.(id, para, texto);
0104 |    return evolutionFake.sendIdNull
0105 |      ? { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'EVOLUTION_RECUSOU' }
0106 |      : { outcome: 'ACCEPTED', externalMessageId: id };
0107 |  },
0108 |  async criarInstancia(nome) {
0109 |    evolutionFake.providerCalls += 1;
0110 |    evolutionFake.createCalls += 1;
0111 |    evolutionFake.inventory.set(nome, { name: nome, ownerJid: evolutionFake.ownerPhone ? `${evolutionFake.ownerPhone}@s.whatsapp.net` : null, connectionStatus: evolutionFake.createdState });
0112 |    await evolutionFake.createHook?.(nome);
0113 |    return { qrcode: 'data:image/png;base64,QR' };
0114 |  },
0115 |  async qrDaInstancia() {
0116 |    evolutionFake.providerCalls += 1;
0117 |    return 'data:image/png;base64,QR';
0118 |  },
0119 |  async estadoDaInstancia() {
0120 |    evolutionFake.providerCalls += 1;
0121 |    return 'open';
0122 |  },
0123 |  async consultarInstancia(nome) { evolutionFake.providerCalls += 1; return evolutionFake.inventory.get(nome) ?? null; },
0124 |  async apagarInstancia(nome) { evolutionFake.providerCalls += 1; if (evolutionFake.deleteFails) throw new Error('fixture cleanup timeout'); evolutionFake.inventory.delete(nome); },
0125 |};
0126 |
0127 |/**
0128 | * Liga o canal não oficial nos DOIS níveis: o teto da instalação (env, lido no
0129 | * boot do serviço) e o contrato da Mantenedora (banco) — ADR-0016.
0130 | *
0131 | * Precisa vir ANTES de `subirApp`, porque o teto é lido uma vez na construção.
0132 | * É o mesmo que acontece em produção: mudar módulo de instalação é deploy.
0133 | */
0134 |export function tetoComCanalNaoOficial(): void {
0135 |  process.env.LH_CHANNEL_UNOFFICIAL = 'true';
0136 |}
0137 |
0138 |export async function contratarCanalNaoOficial(prisma: PrismaService, mantenedoraId: string): Promise<void> {
0139 |  await prisma.mantenedoraSettings.upsert({
0140 |    where: { mantenedoraId },
0141 |    create: { mantenedoraId, modulos: { canalNaoOficial: true } },
0142 |    update: { modulos: { canalNaoOficial: true } },
0143 |  });
0144 |}
0145 |
0146 |export const TOKEN_INTERNO = 'token-interno-de-teste';
0147 |export const META_APP_SECRET = 'segredo-do-app-meta';
0148 |export const EVOLUTION_WEBHOOK_SECRET = 'fixture-evolution-secret-header';
0149 |export const typebotFake: TypebotClient & { enabled: boolean; starts: number; continues: number; startedBots: Array<{ botId: string; contact: string; text: string }>; beforeReply: (() => Promise<void>) | null } = {
0150 |  enabled: false, starts: 0, continues: 0, startedBots: [], beforeReply: null,
0151 |  configurado() { return typebotFake.enabled; }, async listarBots() { return []; }, editorUrl(id) { return `https://typebot.invalid/${id}`; }, workspaceUrl() { return 'https://typebot.invalid'; },
0152 |  async iniciar(botId, contact, text) { typebotFake.starts += 1; typebotFake.startedBots.push({ botId, contact, text }); await typebotFake.beforeReply?.(); return { sessionId: `fixture-typebot-${typebotFake.starts}`, messages: [{ type: 'text', content: { text: 'resposta do bot' } }] }; },
0153 |  async continuar() { typebotFake.continues += 1; return { messages: [] }; },
0154 |};
0155 |
0156 |export async function subirApp(registryOverride?: ChannelAdapterRegistry, captureQueries = false): Promise<{ app: INestApplication; prisma: PrismaService }> {
0157 |  process.env.SESSION_SECRET ||= 'segredo-de-teste';
0158 |  process.env.INTERNAL_SERVICE_TOKEN = TOKEN_INTERNO;
0159 |  process.env.META_APP_ID = 'fixture-app';
0160 |  process.env.META_APP_SECRET = META_APP_SECRET;
0161 |  process.env.META_SIGNUP_CONFIG_ID = 'fixture-config';
0162 |  process.env.GRAPH_VERSION = 'v26.0';
0163 |  process.env.EVOLUTION_WEBHOOK_SECRET = EVOLUTION_WEBHOOK_SECRET;
0164 |  process.env.EVOLUTION_WEBHOOK_URL = 'https://api.example.test/webhooks/evolution';
0165 |  process.env.WEBHOOK_VERIFY_TOKEN = 'verify-token-de-teste';
0166 |  process.env.CHANNEL_CREDENTIAL_KEY_ID = 'fixture-key-v1';
0167 |  process.env.CHANNEL_CREDENTIAL_KEY = Buffer.alloc(32, 17).toString('base64');
0168 |
0169 |  const testingModule = Test.createTestingModule({ imports: [AppModule] })
0170 |    .overrideProvider(META_CLIENT)
0171 |    .useValue(metaFake)
0172 |    .overrideProvider(EVOLUTION_CLIENT)
0173 |    .useValue(evolutionFake)
0174 |    .overrideProvider(TYPEBOT_CLIENT)
0175 |    .useValue(typebotFake);
0176 |  if (captureQueries) {
0177 |    testingModule.overrideProvider(PrismaService).useValue(new PrismaService({ log: [{ emit: 'event', level: 'query' }] }));
0178 |  }
0179 |  if (registryOverride) testingModule.overrideProvider(ChannelAdapterRegistry).useValue(registryOverride);
0180 |  const moduleRef = await testingModule.compile();
0181 |  // A MESMA fiação de produção: sem isto o corpo bruto não existe e o teste de
0182 |  // assinatura passaria a provar outra coisa.
0183 |  const app = moduleRef.createNestApplication({ bodyParser: false });
0184 |  configurarBodyParsers(app as unknown as NestExpressApplication);
0185 |  await app.init();
0186 |  return { app, prisma: app.get(PrismaService) };
0187 |}
0188 |
0189 |/** Limpa na ordem das dependências — o banco de teste é real (ADR-0012 §4). */
0190 |/** Cria um usuário com papel escolhido numa BU — para o caso "papel insuficiente". */
0191 |export async function criarUsuario(
0192 |  prisma: PrismaService,
0193 |  mantenedoraId: string,
0194 |  buId: string,
0195 |  email: string,
0196 |  role: 'OWNER' | 'ADMIN' | 'ATENDENTE',
0197 |  senha = 'senha-de-teste-1',
0198 |): Promise<string> {
0199 |  const bcrypt = await import('bcryptjs');
0200 |  const user = await prisma.appUser.create({
0201 |    data: {
0202 |      mantenedoraId,
0203 |      name: email,
0204 |      email,
0205 |      passwordHash: await bcrypt.default.hash(senha, 10),
0206 |    },
0207 |  });
0208 |  await prisma.userBuRole.create({ data: { userId: user.id, buId, role, grantedViaTipo: 'DIRETO' } });
0209 |  return user.id;
0210 |}
0211 |
0212 |export async function limparBanco(prisma: PrismaService): Promise<void> {
0213 |  evolutionFake.inventory.clear();
0214 |  evolutionFake.createCalls = 0; evolutionFake.providerCalls = 0; evolutionFake.createHook = null;
0215 |  metaFake.enviados.length = 0; metaFake.sendIdNull = false; metaFake.sendHook = null; evolutionFake.enviados.length = 0; evolutionFake.sendIdNull = false; evolutionFake.sendHook = null; metaFake.confirmCalls = 0; metaFake.exchangeCalls = 0; metaFake.exchangeFails = 0; metaFake.providerCalls = 0;
0216 |  metaFake.credentialByPhone.clear(); metaFake.credentialCalls.length = 0;
0217 |  metaFake.registrosNumero = 0;
0218 |  metaFake.wabaRecusada = null;
0219 |  metaFake.confirmHook = null; metaFake.registrosHook = null; metaFake.confirmCalls = 0; metaFake.subscriptionHook = null;
0220 |  typebotFake.enabled = false; typebotFake.starts = 0; typebotFake.continues = 0; typebotFake.startedBots.length = 0; typebotFake.beforeReply = null;
0221 |  evolutionFake.ownerPhone = '5584999990000'; evolutionFake.createdState = 'open'; evolutionFake.deleteFails = false;
0222 |  await prisma.webhookEvent.deleteMany();
0223 |  await prisma.message.deleteMany();
0224 |  await prisma.providerResourceIdentity.deleteMany();
0225 |  await prisma.channelRegistrationAttempt.deleteMany();
0226 |  await prisma.channelCredential.deleteMany();
0227 |  await prisma.conversation.deleteMany();
0228 |  await prisma.activityLog.deleteMany();
0229 |  await prisma.tokenDeAcesso.deleteMany();
0230 |  await prisma.arquivo.deleteMany();
0231 |  await prisma.setorGrant.deleteMany();
0232 |  await prisma.userBuRole.deleteMany();
0233 |  await prisma.appUser.deleteMany();
0234 |  await prisma.buChannel.deleteMany();
0235 |  await prisma.businessUnit.deleteMany();
0236 |  await prisma.setor.deleteMany();
0237 |  await prisma.mantenedora.deleteMany();
0238 |  await prisma.loginAttempt.deleteMany();
0239 |}
0240 |
0241 |/** Test channel fixture with the same durable ownership and credential invariants as production. */
0242 |export async function criarCanalVerificado(
0243 |  prisma: PrismaService,
0244 |  buId: string,
0245 |  type: 'OFICIAL' | 'NAO_OFICIAL',
0246 |  externalResourceId: string,
0247 |  options: { status?: 'CONECTADO' | 'CONECTANDO' | 'DESCONECTADO'; requiresWindow?: boolean } = {},
0248 |) {
0249 |  const channel = await prisma.buChannel.create({ data: {
0250 |    buId, type, status: options.status ?? 'CONECTADO', requiresWindow: options.requiresWindow ?? type === 'OFICIAL',
0251 |    ...(type === 'OFICIAL' ? { phoneNumberId: externalResourceId } : { evolutionInstanceName: externalResourceId }),
0252 |    ownNumberVerified: true, verifiedEpoch: 0, providerConnectionState: type === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
0253 |    receiptVerifiedAt: new Date(),
0254 |  } });
0255 |  const priorIdentity = await prisma.providerResourceIdentity.findUnique({
0256 |    where: { provider_externalResourceId: { provider: type, externalResourceId } },
0257 |  });
0258 |  if (priorIdentity && (priorIdentity.buId !== buId || priorIdentity.currentChannelId)) {
0259 |    throw new Error('Fixture resource identity is owned or active elsewhere.');
0260 |  }
0261 |  const identity = priorIdentity
0262 |    ? await prisma.providerResourceIdentity.update({ where: { id: priorIdentity.id }, data: { currentChannelId: channel.id, retiredAt: null, managedLifecycle: true, cleanupState: 'ACTIVE' } })
0263 |    : await prisma.providerResourceIdentity.create({ data: {
0264 |      provider: type, externalResourceId, buId, currentChannelId: channel.id, managedLifecycle: true, cleanupState: 'ACTIVE',
0265 |    } });
0266 |  if (type === 'OFICIAL') {
0267 |    const keyId = process.env.CHANNEL_CREDENTIAL_KEY_ID!;
0268 |    const key = Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY!, 'base64');
0269 |    const envelope = sealChannelCredential('fixture-scoped-token', keyId, key, {
0270 |      purpose: 'active', provider: type, buId, channelId: channel.id, generation: channel.generation, version: 1,
0271 |    });
0272 |    await prisma.channelCredential.create({ data: {
0273 |      channelId: channel.id, provider: type, buId, generation: channel.generation, version: 1,
0274 |      keyId, nonce: new Uint8Array(envelope.nonce), ciphertext: new Uint8Array(envelope.ciphertext), tag: new Uint8Array(envelope.tag),
0275 |    } });
0276 |  }
0277 |  return { channel, identity };
0278 |}
0279 |
0280 |/** Cria uma Mantenedora pela superfície interna — o caminho real de bootstrap. */
0281 |/**
0282 | * Cria a Mantenedora **com o onboarding já concluído**.
0283 | *
0284 | * O bootstrap a cria PENDENTE (ADR-0016 §4), e é assim em produção. Os testes
0285 | * que exercitam o produto vêm depois do wizard; quem exercita o portão é
0286 | * `onboarding.e2e-spec.ts`, que usa `criarMantenedoraPendente`.
0287 | */
0288 |export async function criarMantenedora(
0289 |  app: INestApplication,
0290 |  nome: string,
0291 |  email: string,
0292 |  senha = 'senha-de-teste-1',
0293 |) {
0294 |  const r = await criarMantenedoraPendente(app, nome, email, senha);
0295 |  const prisma = app.get(PrismaService);
0296 |  await prisma.mantenedoraSettings.update({
0297 |    where: { mantenedoraId: r.mantenedora.id },
0298 |    data: { onboardingConcluido: true },
0299 |  });
0300 |  return r;
0301 |}
0302 |
0303 |export async function criarMantenedoraPendente(
0304 |  app: INestApplication,
0305 |  nome: string,
0306 |  email: string,
0307 |  senha = 'senha-de-teste-1',
0308 |) {
0309 |  const res = await request(app.getHttpServer())
0310 |    .post('/api/internal/mantenedoras')
0311 |    .set('x-internal-token', TOKEN_INTERNO)
0312 |    .set('x-requested-with', 'teste')
0313 |    .send({ nome, bu: { nome: `Número da ${nome}`, telefone: '5584999990000' }, owner: { nome: 'Dono', email, senha } })
0314 |    .expect(201);
0315 |  return res.body as {
0316 |    mantenedora: { id: string; nome: string };
0317 |    businessUnit: { id: string; nome: string };
0318 |    owner: { id: string; email: string };
0319 |  };
0320 |}
0321 |
0322 |/** Faz login e devolve o cookie de sessão para reusar nas próximas chamadas. */
0323 |export async function login(app: INestApplication, email: string, senha = 'senha-de-teste-1'): Promise<string> {
0324 |  const res = await request(app.getHttpServer())
0325 |    .post('/api/bff/auth/login')
0326 |    .set('x-requested-with', 'teste')
0327 |    .send({ email, senha })
0328 |    .expect(200);
0329 |  const setCookie = res.headers['set-cookie'] as unknown as string[];
0330 |  return setCookie[0].split(';')[0];
0331 |}
```

## Unchanged critical context web-app/src/api.ts

```text
0001 |/**
0002 | * Cliente do BFF.
0003 | *
0004 | * O front é serviço próprio, num SUBDOMÍNIO do mesmo domínio da API (ADR-0015).
0005 | * Isso é origem diferente e **mesmo site** — então:
0006 | *  - `credentials: 'include'` manda o cookie `HttpOnly` para a API;
0007 | *  - o cookie continua `SameSite=Lax`, porque subdomínio é o mesmo site;
0008 | *  - `X-Requested-With` é exigido pelo servidor no que muda estado (CSRF).
0009 | *
0010 | * A base da API vem de `/config.js`, escrito pelo container no START — não do
0011 | * build (ver `config.ts`). Vazio = mesma origem.
0012 | */
0013 |import { API_BASE as BASE } from './config';
0014 |/** Evento disparado quando qualquer chamada volta 401. */
0015 |export const SESSAO_MORTA = 'leadshug:sessao-morta';
0016 |
0017 |/**
0018 | * A conta ainda não terminou o wizard (409 ONBOARDING_PENDENTE), ou um módulo
0019 | * foi desligado com a aba aberta (404 MODULO_DESLIGADO).
0020 | *
0021 | * Nos dois casos o estado da tela está VELHO, não errado: o app rebusca o /me e
0022 | * se remonta, em vez de mostrar erro. É o mesmo padrão do SESSAO_MORTA.
0023 | */
0024 |export const PRODUTO_MUDOU = 'leadshug:produto-mudou';
0025 |
0026 |/**
0027 | * `typeof window` porque este módulo também é exercitado fora do navegador —
0028 | * é o teste de unidade que prova isso. Estourar aqui trocaria o erro REAL da
0029 | * chamada por um "window is not defined", que aponta para o lugar errado.
0030 | */
0031 |function avisar(evento: string): void {
0032 |  if (typeof window !== 'undefined') window.dispatchEvent(new CustomEvent(evento));
0033 |}
0034 |
0035 |export class ErroDaApi extends Error {
0036 |  constructor(
0037 |    readonly status: number,
0038 |    readonly codigo: string | undefined,
0039 |    mensagem: string,
0040 |    readonly outcome?: string,
0041 |    readonly evidence?: string,
0042 |    readonly localMessageState?: string,
0043 |    readonly diagnosticPersistence?: string,
0044 |  ) {
0045 |    super(mensagem);
0046 |  }
0047 |}
0048 |
0049 |async function chamar<T>(caminho: string, init: RequestInit = {}): Promise<T> {
0050 |  const mudaEstado = Boolean(init.method && init.method !== 'GET');
0051 |  const res = await fetch(`${BASE}/api/bff${caminho}`, {
0052 |    ...init,
0053 |    credentials: 'include',
0054 |    headers: {
0055 |      'content-type': 'application/json',
0056 |      ...(mudaEstado ? { 'x-requested-with': 'leadshug-web' } : {}),
0057 |      ...(init.headers ?? {}),
0058 |    },
0059 |  });
0060 |
0061 |  if (res.status === 204) return undefined as T;
0062 |
0063 |  // Resposta que NÃO é JSON é falha de configuração, não corpo vazio.
0064 |  //
0065 |  // O caso real: sem `LEADSHUG_API_URL`, a base fica vazia e o front chama a
0066 |  // PRÓPRIA origem — onde o nginx serve o index.html para qualquer caminho. A
0067 |  // resposta vem 200, com HTML. Engolir isso como `{}` fazia a tela quebrar três
0068 |  // passos depois, num campo que não tem relação nenhuma com a causa
0069 |  // ("Cannot read properties of undefined"), e mandava quem depura para o lugar
0070 |  // errado. Falhar aqui, dizendo o que provavelmente está errado, é o mínimo.
0071 |  const bruto = await res.text();
0072 |  let corpo: Record<string, unknown>;
0073 |  try {
0074 |    corpo = bruto ? JSON.parse(bruto) : {};
0075 |  } catch {
0076 |    // 405 num POST é assinatura de SERVIDOR DE ARQUIVOS: nginx responde assim
0077 |    // quando recebe POST para um arquivo estático. Dizer isso poupa a rodada de
0078 |    // "confira se é mesmo a API" — o que responde não é uma API.
0079 |    const pareceEstatico = res.status === 405 || /^\s*<(!doctype|html)/i.test(bruto);
0080 |
0081 |    throw new ErroDaApi(
0082 |      res.status,
0083 |      'RESPOSTA_NAO_E_JSON',
0084 |      !BASE
0085 |        ? 'A base da API está VAZIA: o front está chamando a própria origem. ' +
0086 |          'Configure LEADSHUG_API_URL no serviço web.'
0087 |        : pareceEstatico
0088 |          ? `${BASE} respondeu ${res.status} como um servidor de ARQUIVOS, não como a API ` +
0089 |            `(em ${caminho}). Esse endereço aponta para o serviço errado — confira ` +
0090 |            'LEADSHUG_API_URL e o domínio do serviço `api`.'
0091 |          : `A API respondeu ${res.status} com algo que não é JSON em ${caminho}. ` +
0092 |            `Confira se ${BASE} é mesmo a API.`,
0093 |    );
0094 |  }
0095 |
0096 |  if (res.status === 401) {
0097 |    // A sessão morreu (expirou, a conta foi inativada, a senha foi resetada).
0098 |    // Quem descobre isso é qualquer chamada, então o aviso é central: a tela
0099 |    // que estava aberta não tem como saber o que fazer sozinha.
0100 |    avisar(SESSAO_MORTA);
0101 |  }
0102 |  // Estado VELHO, não erro: a conta não terminou o wizard, ou um módulo foi
0103 |  // desligado com esta aba aberta. O app rebusca o /me e se remonta.
0104 |  if (corpo.code === 'ONBOARDING_PENDENTE' || corpo.code === 'MODULO_DESLIGADO') {
0105 |    avisar(PRODUTO_MUDOU);
0106 |  }
0107 |  if (!res.ok) {
0108 |    // `error` é o campo das recusas do produto. Um 500 do Nest NÃO tem esse
0109 |    // campo — ele traz `message` —, e ignorá-lo transformava toda falha de
0110 |    // servidor em "Falha inesperada.", que não diz nem o status. O status entra
0111 |    // sempre: é o primeiro dado que quem depura precisa.
0112 |    const dito = corpo.error ?? corpo.message;
0113 |    throw new ErroDaApi(
0114 |      res.status,
0115 |      typeof corpo.code === 'string' ? corpo.code : undefined,
0116 |      dito ? `${dito} (HTTP ${res.status})` : `A API respondeu ${res.status} sem explicar o motivo.`,
0117 |      typeof corpo.outcome === 'string' ? corpo.outcome : undefined,
0118 |      typeof corpo.evidence === 'string' ? corpo.evidence : undefined,
0119 |      typeof corpo.localMessageState === 'string' ? corpo.localMessageState : undefined,
0120 |      typeof corpo.diagnosticPersistence === 'string' ? corpo.diagnosticPersistence : undefined,
0121 |    );
0122 |  }
0123 |  return corpo as T;
0124 |}
0125 |
0126 |/**
0127 | * Trata a falha de uma chamada disparada e esquecida (carregamento de tela).
0128 | *
0129 | * 401 aqui é normal e não é problema da tela: a sessão morreu — no logout, por
0130 | * expiração, ou porque a conta foi inativada — e quem redireciona é o App. Sem
0131 | * este filtro, cada chamada em voo no momento do logout vira uma **rejeição não
0132 | * tratada**, que o navegador registra como exceção da página. Foi assim que o
0133 | * teste de navegador pegou o primeiro defeito real.
0134 | */
0135 |export function ignorarSessaoMorta(e: unknown): void {
0136 |  if (e instanceof ErroDaApi && e.status === 401) return;
0137 |  // Tratados centralmente pelo App, que rebusca o /me e remonta. Deixá-los
0138 |  // chegar ao console faria a tela reclamar de algo que já está sendo resolvido.
0139 |  if (e instanceof ErroDaApi && (e.codigo === 'ONBOARDING_PENDENTE' || e.codigo === 'MODULO_DESLIGADO')) return;
0140 |  console.error(e);
0141 |}
0142 |
0143 |export const api = {
0144 |  get: <T>(c: string) => chamar<T>(c),
0145 |  post: <T>(c: string, corpo?: unknown) =>
0146 |    chamar<T>(c, { method: 'POST', body: corpo ? JSON.stringify(corpo) : undefined }),
0147 |  postWithHeaders: <T>(c: string, corpo: unknown, headers: Record<string, string>) =>
0148 |    chamar<T>(c, { method: 'POST', body: JSON.stringify(corpo), headers }),
0149 |  patch: <T>(c: string, corpo?: unknown) =>
0150 |    chamar<T>(c, { method: 'PATCH', body: corpo ? JSON.stringify(corpo) : undefined }),
0151 |  put: <T>(c: string, corpo?: unknown) =>
0152 |    chamar<T>(c, { method: 'PUT', body: corpo ? JSON.stringify(corpo) : undefined }),
0153 |  del: <T>(c: string) => chamar<T>(c, { method: 'DELETE' }),
0154 |
0155 |  /**
0156 |   * Envia um arquivo (ADR-0024). Sem `content-type`: o navegador precisa montar
0157 |   * o `boundary` do multipart sozinho, e declará-lo à mão quebra o parse no
0158 |   * servidor de um jeito que não diz o que houve.
0159 |   */
0160 |  async enviarArquivo(arquivo: File): Promise<{ id: string; tipo: string }> {
0161 |    const corpo = new FormData();
0162 |    corpo.append('arquivo', arquivo);
0163 |    const res = await fetch(`${BASE}/api/bff/arquivos`, {
0164 |      method: 'POST',
0165 |      credentials: 'include',
0166 |      headers: { 'x-requested-with': 'leadshug-web' },
0167 |      body: corpo,
0168 |    });
0169 |    const bruto = await res.text();
0170 |    let json: Record<string, string> = {};
0171 |    try {
0172 |      json = bruto ? JSON.parse(bruto) : {};
0173 |    } catch {
0174 |      throw new ErroDaApi(res.status, 'RESPOSTA_NAO_E_JSON', 'A API respondeu algo que não é JSON.');
0175 |    }
0176 |    if (!res.ok) throw new ErroDaApi(res.status, json.code, json.error ?? 'Falha ao enviar o arquivo.');
0177 |    return json as unknown as { id: string; tipo: string };
0178 |  },
0179 |};
0180 |
0181 |/** O endereço de leitura de um arquivo guardado — passa pela sessão. */
0182 |export function urlDoArquivo(id: string | null | undefined): string | null {
0183 |  return id ? `${BASE}/api/bff/arquivos/${id}` : null;
0184 |}
0185 |
0186 |export interface Produto {
0187 |  /** JÁ interseccionado no servidor (env ∩ Mantenedora) — aqui não se faz conta. */
0188 |  modulos: { canalNaoOficial: boolean };
0189 |  marca: { nome: string | null; cor: string | null; corClaro: string | null; corEscuro: string | null; corSecundaria: string | null; tema: string; logo: string | null };
0190 |  /** O wizard ainda não terminou: o app monta o wizard, não o produto. */
0191 |  onboardingPendente: boolean;
0192 |}
0193 |
0194 |export interface Eu {
0195 |  id: string;
0196 |  nome: string;
0197 |  email: string;
0198 |  precisaTrocarSenha: boolean;
0199 |  papel: string | null;
0200 |  mantenedora: { id: string; name: string } | null;
0201 |  escopo: string[];
0202 |  produto: Produto;
0203 |  telefone: string | null;
0204 |  avatar: string | null;
0205 |}
0206 |
0207 |export interface BusinessUnit {
0208 |  id: string;
0209 |  name: string;
0210 |  phone: string | null;
0211 |  papel?: string | null;
0212 |  setor?: { id: string; name: string } | null;
0213 |  channels: {
0214 |    id: string;
0215 |    type: string;
0216 |    status: string;
0217 |    generation?: number;
0218 |    currentAttemptId?: string | null;
0219 |    ownNumberVerified?: boolean;
0220 |    providerConnectionState?: string | null;
0221 |    receiptVerifiedAt?: string | null;
0222 |    requiresWindow?: boolean;
0223 |    connectedAt?: string | null;
0224 |  }[];
0225 |}
0226 |
0227 |export interface Setor {
0228 |  id: string;
0229 |  nome: string;
0230 |  status: 'ATIVO' | 'INATIVO';
0231 |  numeros: number;
0232 |}
0233 |
0234 |export interface Atividade {
0235 |  id: string;
0236 |  categoria: string;
0237 |  entidade: string;
0238 |  ator: string | null;
0239 |  texto: string;
0240 |  de: string | null;
0241 |  para: string | null;
0242 |  em: string;
0243 |}
0244 |
0245 |export interface Conversa {
0246 |  id: string;
0247 |  contact: string;
0248 |  displayName: string | null;
0249 |  status: string;
0250 |  attendantName: string | null;
0251 |  unreadCount: number;
0252 |  lastMessageAt: string | null;
0253 |}
0254 |
0255 |export interface Mensagem {
0256 |  id: string;
0257 |  direction: 'IN' | 'OUT';
0258 |  content: string | null;
0259 |  channelOrigin: string;
0260 |  authorName: string | null;
0261 |  createdAt: string;
0262 |}
0263 |
0264 |export interface Thread {
0265 |  conversa: { id: string; contato: string; nome: string | null; status: string; atendente: string | null };
0266 |  janela: { exigida: boolean; aberta: boolean; expiraEm: string | null; canal: string | null; disponivel: boolean; motivo: string | null };
0267 |  messages: Mensagem[];
0268 |  paginacao: { limite: number; temAnteriores: boolean; cursorAnterior: string | null };
0269 |}
```

## Unchanged critical context web-app/src/telas/Inbox.tsx

```text
0001 |import { FormEvent, useCallback, useEffect, useRef, useState } from 'react';
0002 |import { BusinessUnit, Conversa, ErroDaApi, Eu, Mensagem, Thread, api, ignorarSessaoMorta } from '../api';
0003 |import { ouvirTempoReal } from '../tempoReal';
0004 |import { cruzouPiso, mesclarMensagens } from '../timeline';
0005 |
0006 |const ABAS = [
0007 |  { id: 'QUEUED', rotulo: 'Na fila' },
0008 |  { id: 'IN_SERVICE', rotulo: 'Em atendimento' },
0009 |  { id: 'CLOSED', rotulo: 'Finalizadas' },
0010 |  { id: 'GRUPO', rotulo: 'Grupos' },
0011 |];
0012 |
0013 |function explicarMotivoEnvio(motivo: string | null): string {
0014 |  switch (motivo) {
0015 |    case 'CANAL_AUSENTE': return 'Não há um canal conectado para responder.';
0016 |    case 'CANAL_AMBIGUO': return 'Esta conversa ainda não tem um canal definido. Aguarde uma mensagem recebida para responder.';
0017 |    case 'CANAL_SELECIONADO_INDISPONIVEL': return 'O canal desta conversa não está disponível.';
0018 |    case 'CHANNEL_IDENTITY_NOT_VERIFIED': return 'A identidade do canal ainda precisa ser verificada.';
0019 |    case 'CHANNEL_NOT_READY': return 'O canal ainda não está pronto para enviar.';
0020 |    case 'PENDING_CREDENTIAL': return 'A credencial do canal precisa ser atualizada.';
0021 |    case 'JANELA_FECHADA': return 'A janela de 24 horas foi encerrada.';
0022 |    default: return 'O envio está temporariamente indisponível.';
0023 |  }
0024 |}
0025 |
0026 |interface Recuperacao {
0027 |  id: string;
0028 |  geracao: number;
0029 |  piso: string;
0030 |  cursor: string | null;
0031 |  dirty: boolean;
0032 |  eventos: number;
0033 |  emVoo: boolean;
0034 |  paginasRestantes: number;
0035 |  vazio?: boolean;
0036 |}
0037 |
0038 |interface InvalidacaoDeAbertura {
0039 |  id: string;
0040 |  geracao: number;
0041 |  eventos: number;
0042 |}
0043 |
0044 |interface ErroDeRecuperacao {
0045 |  geracao: number;
0046 |  versao: number;
0047 |}
0048 |
0049 |export default function Inbox({ eu }: { eu: Eu }) {
0050 |  const [bus, setBus] = useState<BusinessUnit[]>([]);
0051 |  const [buId, setBuId] = useState<string>('');
0052 |  const [aba, setAba] = useState('QUEUED');
0053 |  const [conversas, setConversas] = useState<Conversa[]>([]);
0054 |  const [aberta, setAberta] = useState<Thread | null>(null);
0055 |  const [abrindo, setAbrindo] = useState(false);
0056 |  const [texto, setTexto] = useState('');
0057 |  const [erro, setErro] = useState<string | null>(null);
0058 |  const [carregandoAnteriores, setCarregandoAnteriores] = useState(false);
0059 |  const [recuperacaoPendente, setRecuperacaoPendente] = useState(false);
0060 |  const [enviando, setEnviando] = useState(false);
0061 |  const textoRef = useRef('');
0062 |  const versaoErro = useRef(0);
0063 |  const erroRecuperacao = useRef<ErroDeRecuperacao | null>(null);
0064 |  const geracao = useRef(0);
0065 |  const buAtual = useRef('');
0066 |  const conversaAtual = useRef<string | null>(null);
0067 |  const abaAtual = useRef('QUEUED');
0068 |  const threadAtual = useRef<Thread | null>(null);
0069 |  const recuperacao = useRef<Recuperacao | null>(null);
0070 |  const invalidacaoAbertura = useRef<InvalidacaoDeAbertura | null>(null);
0071 |  const executarRecuperacaoRef = useRef<() => Promise<void>>(async () => {});
0072 |  const versaoMetadados = useRef(0);
0073 |  const bolhas = useRef<HTMLDivElement>(null);
0074 |  const carregarListaRef = useRef<(id?: string, filtro?: string) => Promise<void>>(async () => {});
0075 |  const reconciliarRef = useRef<() => void>(() => {});
0076 |
0077 |  const guardarThread = (thread: Thread | null) => {
0078 |    threadAtual.current = thread;
0079 |    setAberta(thread);
0080 |  };
0081 |
0082 |  const guardarTexto = (valor: string) => {
0083 |    textoRef.current = valor;
0084 |    setTexto(valor);
0085 |  };
0086 |
0087 |  const definirErro = useCallback((mensagem: string | null, geracaoDaRecuperacao?: number) => {
0088 |    versaoErro.current += 1;
0089 |    erroRecuperacao.current = mensagem !== null && geracaoDaRecuperacao !== undefined
0090 |      ? { geracao: geracaoDaRecuperacao, versao: versaoErro.current }
0091 |      : null;
0092 |    setErro(mensagem);
0093 |  }, []);
0094 |
0095 |  const limparErroRecuperacao = useCallback((geracaoDaRecuperacao: number) => {
0096 |    const erroAtual = erroRecuperacao.current;
0097 |    if (erroAtual?.geracao !== geracaoDaRecuperacao || erroAtual.versao !== versaoErro.current) return;
0098 |    erroRecuperacao.current = null;
0099 |    versaoErro.current += 1;
0100 |    setErro(null);
0101 |  }, []);
0102 |
0103 |  useEffect(() => {
0104 |    api.get<{ businessUnits: BusinessUnit[] }>('/business-units').then((r) => {
0105 |      const lista = r.businessUnits ?? [];
0106 |      setBus(lista);
0107 |      const inicial = lista[0]?.id ?? '';
0108 |      buAtual.current = inicial;
0109 |      setBuId(inicial);
0110 |    }).catch(ignorarSessaoMorta);
0111 |  }, []);
0112 |
0113 |  const carregarLista = useCallback(async (id = buAtual.current, filtro = aba) => {
0114 |    if (!id) return;
0115 |    try {
0116 |      const r = await api.get<{ conversations: Conversa[] }>(`/business-units/${id}/conversations?aba=${filtro}`);
0117 |      if (buAtual.current === id && abaAtual.current === filtro) setConversas(r.conversations);
0118 |    } catch (e) {
0119 |      if (buAtual.current === id && abaAtual.current === filtro) throw e;
0120 |    }
0121 |  }, [aba]);
0122 |
0123 |  const aplicarPaginaRecente = useCallback((id: string, geracaoDaChamada: number, versao: number, response: Thread) => {
0124 |    if (conversaAtual.current !== id || geracao.current !== geracaoDaChamada) return;
0125 |    const anterior = threadAtual.current;
0126 |    const novo: Thread = {
0127 |      ...response,
0128 |      messages: mesclarMensagens(anterior?.messages ?? [], response.messages),
0129 |      // O cursor de reconciliação recente não substitui o cursor do histórico.
0130 |      paginacao: anterior && anterior.messages.length > 0 ? anterior.paginacao : response.paginacao,
0131 |      conversa: versaoMetadados.current === versao ? response.conversa : anterior?.conversa ?? response.conversa,
0132 |      janela: versaoMetadados.current === versao ? response.janela : anterior?.janela ?? response.janela,
0133 |    };
0134 |    guardarThread(novo);
0135 |  }, []);
0136 |
0137 |  const executarRecuperacao = useCallback(async () => {
0138 |    const r = recuperacao.current;
0139 |    if (!r || r.emVoo || r.paginasRestantes <= 0 || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
0140 |    r.emVoo = true;
0141 |    const eventosNoInicio = r.eventos;
0142 |    r.dirty = false;
0143 |    let cruzou = false;
0144 |    try {
0145 |      if (r.vazio) {
0146 |        if (r.cursor === null && r.paginasRestantes > 0) {
0147 |          const versao = versaoMetadados.current;
0148 |          r.paginasRestantes -= 1;
0149 |          const inicial = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
0150 |          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
0151 |          aplicarPaginaRecente(r.id, r.geracao, versao, inicial);
0152 |          r.cursor = inicial.paginacao.cursorAnterior;
0153 |          if (!inicial.paginacao.temAnteriores) r.cursor = null;
0154 |        }
0155 |        while (r.cursor && r.paginasRestantes > 0 && !r.dirty) {
0156 |          const cursor = r.cursor;
0157 |          r.paginasRestantes -= 1;
0158 |          const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
0159 |          if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
0160 |          const atual = threadAtual.current;
0161 |          if (atual) guardarThread({
0162 |            ...atual,
0163 |            messages: mesclarMensagens(atual.messages, pagina.messages),
0164 |            paginacao: pagina.paginacao,
0165 |          });
0166 |          r.cursor = pagina.paginacao.cursorAnterior;
0167 |        }
0168 |        if (r.eventos !== eventosNoInicio || r.dirty) {
0169 |          r.cursor = null;
0170 |          setRecuperacaoPendente(true);
0171 |        } else if (!r.cursor) {
0172 |          recuperacao.current = null;
0173 |          setRecuperacaoPendente(false);
0174 |          limparErroRecuperacao(r.geracao);
0175 |        } else {
0176 |          setRecuperacaoPendente(true);
0177 |        }
0178 |        return;
0179 |      }
0180 |      if (r.cursor === null && r.paginasRestantes > 0) {
0181 |        const versao = versaoMetadados.current;
0182 |        r.paginasRestantes -= 1;
0183 |        const recente = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false`);
0184 |        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
0185 |        aplicarPaginaRecente(r.id, r.geracao, versao, recente);
0186 |        r.cursor = recente.paginacao.cursorAnterior;
0187 |        cruzou = cruzouPiso(recente.messages, r.piso) || !recente.paginacao.temAnteriores;
0188 |      }
0189 |      while (!cruzou && r.cursor && r.paginasRestantes > 0 && !r.dirty) {
0190 |        const cursor = r.cursor;
0191 |        r.paginasRestantes -= 1;
0192 |        const pagina = await api.get<Thread>(`/conversations/${r.id}/messages?limite=50&marcarLida=false&antes=${encodeURIComponent(cursor)}`);
0193 |        if (r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
0194 |        const atual = threadAtual.current;
0195 |        if (atual) guardarThread({
0196 |          ...atual,
0197 |          messages: mesclarMensagens(atual.messages, pagina.messages),
0198 |        });
0199 |        r.cursor = pagina.paginacao.cursorAnterior;
0200 |        cruzou = cruzouPiso(pagina.messages, r.piso) || !pagina.paginacao.temAnteriores;
0201 |      }
0202 |
0203 |      if (r.eventos !== eventosNoInicio || r.dirty) {
0204 |        // Um evento concorrente exige nova passagem recente e preserva o piso.
0205 |        r.cursor = null;
0206 |        setRecuperacaoPendente(true);
0207 |      } else if (cruzou) {
0208 |        recuperacao.current = null;
0209 |        setRecuperacaoPendente(false);
0210 |        limparErroRecuperacao(r.geracao);
0211 |      } else {
0212 |        setRecuperacaoPendente(true);
0213 |      }
0214 |    } catch (e) {
0215 |      if (r.geracao === geracao.current && r.id === conversaAtual.current) {
0216 |        if (r.dirty || r.eventos !== eventosNoInicio) r.cursor = null;
0217 |        definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível atualizar o histórico. Tente novamente.', r.geracao);
0218 |        setRecuperacaoPendente(true);
0219 |      }
0220 |    } finally {
0221 |      r.emVoo = false;
0222 |      if (recuperacao.current === r && (r.dirty || r.eventos !== eventosNoInicio) && r.paginasRestantes > 0 && r.geracao === geracao.current) {
0223 |        queueMicrotask(() => void executarRecuperacaoRef.current());
0224 |      }
0225 |    }
0226 |  }, [aplicarPaginaRecente, definirErro, limparErroRecuperacao]);
0227 |
0228 |  useEffect(() => { executarRecuperacaoRef.current = executarRecuperacao; }, [executarRecuperacao]);
0229 |
0230 |  const reconciliar = useCallback(() => {
0231 |    const thread = threadAtual.current;
0232 |    const id = conversaAtual.current;
0233 |    if (!id) return;
0234 |    if (!thread) {
0235 |      const abertura = invalidacaoAbertura.current;
0236 |      if (abertura?.id === id && abertura.geracao === geracao.current) abertura.eventos += 1;
0237 |      return;
0238 |    }
0239 |    let r = recuperacao.current;
0240 |    if (!r || r.id !== id || r.geracao !== geracao.current) {
0241 |      const mensagens = thread.messages;
0242 |      if (mensagens.length === 0) {
0243 |        r = { id, geracao: geracao.current, piso: '', cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3, vazio: true };
0244 |        recuperacao.current = r;
0245 |        void executarRecuperacao();
0246 |        return;
0247 |      }
0248 |      const piso = mensagens.reduce((max, m) => Date.parse(m.createdAt) > Date.parse(max) ? m.createdAt : max, mensagens[0].createdAt);
0249 |      r = { id, geracao: geracao.current, piso, cursor: null, dirty: true, eventos: 0, emVoo: false, paginasRestantes: 3 };
0250 |      recuperacao.current = r;
0251 |      setRecuperacaoPendente(true);
0252 |    } else {
0253 |      r.dirty = true;
0254 |      r.eventos += 1;
0255 |      if (!r.emVoo) r.cursor = null;
0256 |      setRecuperacaoPendente(true);
0257 |    }
0258 |    if (r.paginasRestantes > 0) void executarRecuperacao();
0259 |  }, [aplicarPaginaRecente, executarRecuperacao]);
0260 |
0261 |  const iniciarRodadaAutorizada = useCallback(() => {
0262 |    const r = recuperacao.current;
0263 |    if (!r || r.emVoo || r.geracao !== geracao.current || r.id !== conversaAtual.current) return;
0264 |    r.paginasRestantes = 3;
0265 |    void executarRecuperacao();
0266 |  }, [executarRecuperacao]);
0267 |
0268 |  useEffect(() => {
0269 |    carregarListaRef.current = carregarLista;
0270 |    reconciliarRef.current = reconciliar;
0271 |  }, [carregarLista, reconciliar]);
0272 |
0273 |  useEffect(() => {
0274 |    void carregarLista().catch(ignorarSessaoMorta);
0275 |    const t = setInterval(() => {
0276 |      void carregarLista().catch(ignorarSessaoMorta);
0277 |      if (recuperacao.current) iniciarRodadaAutorizada();
0278 |      else reconciliar();
0279 |    }, 60_000);
0280 |    return () => clearInterval(t);
0281 |  }, [buId, aba, carregarLista, reconciliar, iniciarRodadaAutorizada]);
0282 |
0283 |  useEffect(() => {
0284 |    // Espera a lista inicial de BUs e mantém o socket apesar de filtros, BUs ou
0285 |    // callbacks locais mudarem. Isso evita reconectar durante o mesmo login.
0286 |    if (bus.length === 0) return;
0287 |    const parar = ouvirTempoReal((evento) => {
0288 |      if (evento.buId !== buAtual.current) return;
0289 |      void carregarListaRef.current().catch(ignorarSessaoMorta);
0290 |      if (evento.conversaId === conversaAtual.current) reconciliarRef.current();
0291 |    }, () => reconciliarRef.current());
0292 |    return parar;
0293 |  }, [eu.id, bus.length]);
0294 |
0295 |  function trocarBu(novoBu: string) {
0296 |    geracao.current += 1;
0297 |    buAtual.current = novoBu;
0298 |    conversaAtual.current = null;
0299 |    recuperacao.current = null;
0300 |    invalidacaoAbertura.current = null;
0301 |    guardarThread(null);
0302 |    setAbrindo(false);
0303 |    guardarTexto('');
0304 |    setEnviando(false);
0305 |    setCarregandoAnteriores(false);
0306 |    definirErro(null);
0307 |    setRecuperacaoPendente(false);
0308 |    setConversas([]);
0309 |    setBuId(novoBu);
0310 |  }
0311 |
0312 |  async function abrir(id: string) {
0313 |    const gen = ++geracao.current;
0314 |    conversaAtual.current = id;
0315 |    recuperacao.current = null;
0316 |    invalidacaoAbertura.current = { id, geracao: gen, eventos: 0 };
0317 |    versaoMetadados.current += 1;
0318 |    guardarThread(null);
0319 |    setAbrindo(true);
0320 |    guardarTexto('');
0321 |    setEnviando(false);
0322 |    setCarregandoAnteriores(false);
0323 |    definirErro(null);
0324 |    setRecuperacaoPendente(false);
0325 |    try {
0326 |      const response = await api.get<Thread>(`/conversations/${id}/messages`);
0327 |      if (gen !== geracao.current || conversaAtual.current !== id) return;
0328 |      response.messages = mesclarMensagens(response.messages);
0329 |      guardarThread(response);
0330 |      setAbrindo(false);
0331 |      const invalidacao = invalidacaoAbertura.current;
0332 |      invalidacaoAbertura.current = null;
0333 |      void carregarLista().catch(ignorarSessaoMorta);
0334 |      if (invalidacao?.id === id && invalidacao.geracao === gen && invalidacao.eventos > 0) reconciliar();
0335 |    } catch (e) {
0336 |      if (gen === geracao.current) {
0337 |        invalidacaoAbertura.current = null;
0338 |        guardarThread(null);
0339 |        setAbrindo(false);
0340 |        definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Não foi possível carregar a conversa.');
0341 |      }
0342 |    }
0343 |  }
0344 |
0345 |  async function carregarAnteriores() {
0346 |    const atual = threadAtual.current;
0347 |    const id = conversaAtual.current;
0348 |    const cursor = atual?.paginacao.cursorAnterior;
0349 |    if (!atual || !id || !cursor || carregandoAnteriores) return;
0350 |    const gen = geracao.current;
0351 |    setCarregandoAnteriores(true);
0352 |    definirErro(null);
0353 |    try {
0354 |      const pagina = await api.get<Thread>(`/conversations/${id}/messages?antes=${encodeURIComponent(cursor)}`);
0355 |      if (gen !== geracao.current || id !== conversaAtual.current || !threadAtual.current) return;
0356 |      // Inclua alterações legítimas que chegaram enquanto a página estava no ar.
0357 |      const alturaAntes = bolhas.current?.scrollHeight ?? 0;
0358 |      const topoAntes = bolhas.current?.scrollTop ?? 0;
0359 |      const corrente = threadAtual.current;
0360 |      guardarThread({ ...corrente, messages: mesclarMensagens(corrente.messages, pagina.messages), paginacao: pagina.paginacao });
0361 |      requestAnimationFrame(() => {
0362 |        if (gen === geracao.current && bolhas.current) bolhas.current.scrollTop = topoAntes + (bolhas.current.scrollHeight - alturaAntes);
0363 |      });
0364 |    } catch (e) {
0365 |      if (gen === geracao.current) definirErro(e instanceof ErroDaApi && e.status === 404 ? 'Acesso à conversa perdido.' : 'Falha ao carregar mensagens anteriores.');
0366 |    } finally {
0367 |      if (gen === geracao.current) setCarregandoAnteriores(false);
0368 |    }
0369 |  }
0370 |
0371 |  async function agir(acao: () => Promise<unknown>) {
0372 |    const id = conversaAtual.current;
0373 |    const gen = geracao.current;
0374 |    if (!id) return;
0375 |    versaoMetadados.current += 1;
0376 |    definirErro(null);
0377 |    try {
0378 |      await acao();
0379 |      if (gen !== geracao.current || id !== conversaAtual.current) return;
0380 |      void carregarLista().catch(ignorarSessaoMorta);
0381 |      reconciliar();
0382 |    } catch (e) {
0383 |      if (gen === geracao.current) definirErro(e instanceof ErroDaApi ? e.message : 'Falhou.');
0384 |    }
0385 |  }
0386 |
0387 |  async function responder(e: FormEvent) {
0388 |    e.preventDefault();
0389 |    const id = conversaAtual.current;
0390 |    const gen = geracao.current;
0391 |    const textoEnviado = textoRef.current;
0392 |    if (!id || !textoEnviado.trim() || enviando) return;
0393 |    setEnviando(true);
0394 |    definirErro(null);
0395 |    try {
0396 |      await api.post(`/conversations/${id}/messages`, { texto: textoEnviado });
0397 |      if (gen !== geracao.current || id !== conversaAtual.current) return;
0398 |      if (textoRef.current === textoEnviado) guardarTexto('');
0399 |      void carregarLista().catch(ignorarSessaoMorta);
0400 |      reconciliar();
0401 |    } catch (e) {
0402 |      if (gen === geracao.current) definirErro(e instanceof ErroDaApi ? e.message : 'Falha ao enviar mensagem.');
0403 |    } finally {
0404 |      if (gen === geracao.current) setEnviando(false);
0405 |    }
0406 |  }
0407 |
0408 |  const envioIndisponivel = aberta ? !aberta.janela.disponivel : false;
0409 |  const janelaFechada = aberta?.janela.exigida && !aberta.janela.aberta;
0410 |
0411 |  return (
0412 |    <div className="grade">
0413 |      <div className="linha">
0414 |        <select aria-label="Business Unit" value={buId} onChange={(e) => trocarBu(e.target.value)} style={{ maxWidth: 280 }}>
0415 |          {bus.map((b) => <option key={b.id} value={b.id}>{b.name}</option>)}
0416 |        </select>
0417 |        {erro && <span className="erro" role="alert">{erro}</span>}
0418 |      </div>
0419 |
0420 |      <div className="abas">
0421 |        {ABAS.map((a) => <button key={a.id} className={aba === a.id ? 'ativa' : ''} onClick={() => { abaAtual.current = a.id; setAba(a.id); }}>{a.rotulo}</button>)}
0422 |      </div>
0423 |
0424 |      <div className="inbox">
0425 |        <div className="cartao lista" style={{ padding: 0 }}>
0426 |          {conversas.map((c) => <button key={c.id} className={`item ${aberta?.conversa.id === c.id ? 'ativo' : ''}`} onClick={() => void abrir(c.id)}>
0427 |            <div className="linha"><strong>{c.displayName ?? c.contact}</strong>{c.unreadCount > 0 && <span className="suave">({c.unreadCount})</span>}</div>
0428 |            <div className="suave">{c.attendantName ?? 'sem atendente'}</div>
0429 |          </button>)}
0430 |          {conversas.length === 0 && <p className="suave" style={{ padding: 12 }}>Nada aqui.</p>}
0431 |        </div>
0432 |
0433 |        <div className="cartao grade">
0434 |          {!aberta && (abrindo
0435 |            ? <p className="suave" role="status" aria-live="polite">Abrindo conversa…</p>
0436 |            : <p className="suave">Escolha uma conversa.</p>)}
0437 |          {aberta && <>
0438 |            <div className="linha">
0439 |              <strong>{aberta.conversa.nome ?? aberta.conversa.contato}</strong>
0440 |              <span className="suave">{aberta.conversa.status}</span>
0441 |              <span className="suave" style={{ marginLeft: 'auto' }}>{aberta.janela.canal}</span>
0442 |            </div>
0443 |            <div className="linha">
0444 |              {aberta.paginacao.temAnteriores
0445 |                ? <button onClick={() => void carregarAnteriores()} disabled={carregandoAnteriores} aria-label="Carregar mensagens anteriores">
0446 |                    {carregandoAnteriores ? 'Carregando…' : 'Carregar anteriores'}
0447 |                  </button>
0448 |                : <span className="suave">Início do histórico</span>}
0449 |              {recuperacaoPendente && <span className="suave" role="status">Atualização pendente. O histórico pode ter uma lacuna.</span>}
0450 |              {recuperacaoPendente && <button onClick={() => iniciarRodadaAutorizada()}>Continuar atualização</button>}
0451 |            </div>
0452 |            <div className="bolhas" ref={bolhas} aria-live="polite">
0453 |              {aberta.messages.map((m: Mensagem) => <div key={m.id} data-message-id={m.id} className={`bolha ${m.direction === 'OUT' ? 'saiu' : ''}`}>
0454 |                <div>{m.content}</div>
0455 |                <div className="suave">{new Date(m.createdAt).toLocaleString('pt-BR')}{m.authorName ? ` · ${m.authorName}` : ''}</div>
0456 |              </div>)}
0457 |              {aberta.messages.length === 0 && <p className="suave">Nenhuma mensagem nesta conversa.</p>}
0458 |            </div>
0459 |
0460 |            {envioIndisponivel && <div className="aviso" role="status">{janelaFechada
0461 |              ? 'Fora da janela de 24h do canal selecionado. Texto livre está indisponível.'
0462 |              : explicarMotivoEnvio(aberta.janela.motivo)}</div>}
0463 |            <form className="linha" onSubmit={responder}>
0464 |              <input value={texto} onChange={(e) => guardarTexto(e.target.value)} placeholder={envioIndisponivel ? 'Envio indisponível' : 'Escreva uma resposta'} disabled={envioIndisponivel} maxLength={4096} />
0465 |              <button className="primario" disabled={envioIndisponivel || enviando || !texto.trim()}>{enviando ? 'Enviando…' : 'Enviar'}</button>
0466 |            </form>
0467 |            {aberta.conversa.status !== 'CLOSED' && <div className="linha">
0468 |              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/claim`))}>Atender</button>
0469 |              <button onClick={() => void agir(() => api.post(`/conversations/${aberta.conversa.id}/close`))}>Finalizar</button>
0470 |            </div>}
0471 |          </>}
0472 |        </div>
0473 |      </div>
0474 |    </div>
0475 |  );
0476 |}
```

## Unchanged critical context scripts/test-channels-local.sh

```text
0001 |#!/usr/bin/env bash
0002 |set -euo pipefail
0003 |
0004 |ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
0005 |TARGET="${1:-all}"
0006 |case "$TARGET" in
0007 |  api|web|browser|all) ;;
0008 |  *) printf 'Usage: %s [api|web|browser|all]\n' "$0" >&2; exit 2 ;;
0009 |esac
0010 |
0011 |command -v docker.exe >/dev/null || { echo 'Windows Docker CLI (docker.exe) is required.' >&2; exit 1; }
0012 |command -v wslpath >/dev/null || { echo 'wslpath is required to bind the principal checkout.' >&2; exit 1; }
0013 |CHANNELS_SOURCE_WINDOWS="$(wslpath -w "$ROOT_DIR")"
0014 |CHANNELS_EXPECTED_API_PACKAGE_SHA256="$(sha256sum "$ROOT_DIR/api-app/package.json" | cut -d ' ' -f 1)"
0015 |CHANNELS_EXPECTED_WEB_PACKAGE_SHA256="$(sha256sum "$ROOT_DIR/web-app/package.json" | cut -d ' ' -f 1)"
0016 |
0017 |# Keep host inputs as a positive inventory. Do not discover dotenv files with
0018 |# find/glob over either application tree: those trees can contain private
0019 |# configuration and local-only data. The exact public bind paths are listed
0020 |# below; only api-app/.env.example is mounted, while .env and .env.testing are
0021 |# supplied inside the validation container by the Compose config masks below.
0022 |
0023 |cd "$ROOT_DIR"
0024 |temp_env="$(mktemp)"
0025 |chmod 600 "$temp_env"
0026 |cat > "$temp_env" <<EOF
0027 |CHANNELS_SOURCE_WINDOWS=$CHANNELS_SOURCE_WINDOWS
0028 |SESSION_SECRET=channels-validation-session-only
0029 |INTERNAL_SERVICE_TOKEN=channels-validation-internal-only
0030 |POSTGRES_PASSWORD=channels-validation-postgres-only
0031 |EVOLUTION_POSTGRES_PASSWORD=channels-validation-evolution-postgres-only
0032 |EVOLUTION_AUTHENTICATION_API_KEY=channels-validation-evolution-api-key-only
0033 |EVOLUTION_WEBHOOK_SECRET=validation-evolution-header-secret
0034 |CHANNELS_EXPECTED_API_PACKAGE_SHA256=$CHANNELS_EXPECTED_API_PACKAGE_SHA256
0035 |CHANNELS_EXPECTED_WEB_PACKAGE_SHA256=$CHANNELS_EXPECTED_WEB_PACKAGE_SHA256
0036 |EOF
0037 |add_bind_path() {
0038 |  local key="$1" path="$2"
0039 |  local relative_path="${path#"$ROOT_DIR"/}"
0040 |  case "$relative_path" in
0041 |    .env|.env.testing|api-app/.env|api-app/.env.testing|api-app/.local-files|api-app/.local-files/*|web-app/.env|web-app/.env.*)
0042 |      printf 'Refusing excluded private configuration/data path: %s\n' "$relative_path" >&2
0043 |      exit 1
0044 |      ;;
0045 |  esac
0046 |  case "$relative_path" in
0047 |    api-app/.git|api-app/src|api-app/test|api-app/prisma|api-app/package.json|api-app/package-lock.json|api-app/.env.example|api-app/.dockerignore|api-app/.gitignore|api-app/docker/entrypoint.sh|api-app/Dockerfile|api-app/eslint.config.mjs|api-app/nest-cli.json|api-app/railway.json|api-app/tsconfig.json|api-app/tsconfig.build.json|api-app/vitest.config.ts|api-app/vitest.config.e2e.ts|api-app/vitest.config.cov.ts|web-app/.git|web-app/src|web-app/e2e|web-app/public|web-app/package.json|web-app/package-lock.json|web-app/index.html|web-app/playwright.config.ts|web-app/tsconfig.json|web-app/vite.config.ts|web-app/railway.json|web-app/.gitignore|web-app/.dockerignore|web-app/Dockerfile|web-app/docker/40-config-js.sh|web-app/nginx/default.conf.template) ;;
0048 |    *) printf 'Refusing path outside the public bind inventory: %s\n' "$relative_path" >&2; exit 1 ;;
0049 |  esac
0050 |  [[ -e "$path" ]] || { printf 'Expected principal source path is missing: %s\n' "${path#"$ROOT_DIR"/}" >&2; exit 1; }
0051 |  printf '%s=%s\n' "$key" "$(wslpath -w "$path")" >> "$temp_env"
0052 |}
0053 |add_bind_path CHANNELS_API_GIT_WINDOWS "$ROOT_DIR/api-app/.git"
0054 |add_bind_path CHANNELS_API_SRC_WINDOWS "$ROOT_DIR/api-app/src"
0055 |add_bind_path CHANNELS_API_TEST_WINDOWS "$ROOT_DIR/api-app/test"
0056 |add_bind_path CHANNELS_API_PRISMA_WINDOWS "$ROOT_DIR/api-app/prisma"
0057 |add_bind_path CHANNELS_API_PACKAGE_JSON_WINDOWS "$ROOT_DIR/api-app/package.json"
0058 |add_bind_path CHANNELS_API_PACKAGE_LOCK_WINDOWS "$ROOT_DIR/api-app/package-lock.json"
0059 |add_bind_path CHANNELS_API_ENV_EXAMPLE_WINDOWS "$ROOT_DIR/api-app/.env.example"
0060 |add_bind_path CHANNELS_API_DOCKERIGNORE_WINDOWS "$ROOT_DIR/api-app/.dockerignore"
0061 |add_bind_path CHANNELS_API_GITIGNORE_WINDOWS "$ROOT_DIR/api-app/.gitignore"
0062 |add_bind_path CHANNELS_API_ENTRYPOINT_WINDOWS "$ROOT_DIR/api-app/docker/entrypoint.sh"
0063 |add_bind_path CHANNELS_API_DOCKERFILE_WINDOWS "$ROOT_DIR/api-app/Dockerfile"
0064 |add_bind_path CHANNELS_API_ESLINT_WINDOWS "$ROOT_DIR/api-app/eslint.config.mjs"
0065 |add_bind_path CHANNELS_API_NEST_WINDOWS "$ROOT_DIR/api-app/nest-cli.json"
0066 |add_bind_path CHANNELS_API_RAILWAY_WINDOWS "$ROOT_DIR/api-app/railway.json"
0067 |add_bind_path CHANNELS_API_TSCONFIG_WINDOWS "$ROOT_DIR/api-app/tsconfig.json"
0068 |add_bind_path CHANNELS_API_TSCONFIG_BUILD_WINDOWS "$ROOT_DIR/api-app/tsconfig.build.json"
0069 |add_bind_path CHANNELS_API_VITEST_WINDOWS "$ROOT_DIR/api-app/vitest.config.ts"
0070 |add_bind_path CHANNELS_API_VITEST_E2E_WINDOWS "$ROOT_DIR/api-app/vitest.config.e2e.ts"
0071 |add_bind_path CHANNELS_API_VITEST_COV_WINDOWS "$ROOT_DIR/api-app/vitest.config.cov.ts"
0072 |add_bind_path CHANNELS_WEB_GIT_WINDOWS "$ROOT_DIR/web-app/.git"
0073 |add_bind_path CHANNELS_WEB_SRC_WINDOWS "$ROOT_DIR/web-app/src"
0074 |add_bind_path CHANNELS_WEB_E2E_WINDOWS "$ROOT_DIR/web-app/e2e"
0075 |add_bind_path CHANNELS_WEB_PUBLIC_WINDOWS "$ROOT_DIR/web-app/public"
0076 |add_bind_path CHANNELS_WEB_PACKAGE_JSON_WINDOWS "$ROOT_DIR/web-app/package.json"
0077 |add_bind_path CHANNELS_WEB_PACKAGE_LOCK_WINDOWS "$ROOT_DIR/web-app/package-lock.json"
0078 |add_bind_path CHANNELS_WEB_INDEX_WINDOWS "$ROOT_DIR/web-app/index.html"
0079 |add_bind_path CHANNELS_WEB_PLAYWRIGHT_WINDOWS "$ROOT_DIR/web-app/playwright.config.ts"
0080 |add_bind_path CHANNELS_WEB_TSCONFIG_WINDOWS "$ROOT_DIR/web-app/tsconfig.json"
0081 |add_bind_path CHANNELS_WEB_VITE_WINDOWS "$ROOT_DIR/web-app/vite.config.ts"
0082 |add_bind_path CHANNELS_WEB_RAILWAY_WINDOWS "$ROOT_DIR/web-app/railway.json"
0083 |add_bind_path CHANNELS_WEB_GITIGNORE_WINDOWS "$ROOT_DIR/web-app/.gitignore"
0084 |add_bind_path CHANNELS_WEB_DOCKERIGNORE_WINDOWS "$ROOT_DIR/web-app/.dockerignore"
0085 |add_bind_path CHANNELS_WEB_DOCKERFILE_WINDOWS "$ROOT_DIR/web-app/Dockerfile"
0086 |add_bind_path CHANNELS_WEB_CONFIG_JS_WINDOWS "$ROOT_DIR/web-app/docker/40-config-js.sh"
0087 |add_bind_path CHANNELS_WEB_NGINX_TEMPLATE_WINDOWS "$ROOT_DIR/web-app/nginx/default.conf.template"
0088 |trap 'rm -f "$temp_env"' EXIT
0089 |COMPOSE=(docker.exe compose --project-name leadshug_channels_validation \
0090 |  --env-file "$(wslpath -w "$ROOT_DIR/.env.example")" --env-file "$(wslpath -w "$temp_env")" \
0091 |  -f "$(wslpath -w "$ROOT_DIR/docker-compose.yml")" -f "$(wslpath -w "$ROOT_DIR/docker-compose.channels.yml")" --profile validation)
0092 |
0093 |resource_conflicts=()
0094 |while IFS= read -r resource_name; do
0095 |  if [[ "$resource_name" == leadshug_channels_validation_* || "$resource_name" == leadshug_channels_validation-* ]]; then
0096 |    resource_conflicts+=("container:$resource_name")
0097 |  fi
0098 |done < <(docker.exe ps -a --format '{{.Names}}')
0099 |while IFS= read -r resource_name; do
0100 |  [[ "$resource_name" == leadshug_channels_validation_* ]] && resource_conflicts+=("volume:$resource_name")
0101 |done < <(docker.exe volume ls --format '{{.Name}}')
0102 |while IFS= read -r resource_name; do
0103 |  [[ "$resource_name" == leadshug_channels_validation_* ]] && resource_conflicts+=("network:$resource_name")
0104 |done < <(docker.exe network ls --format '{{.Name}}')
0105 |if ((${#resource_conflicts[@]})); then
0106 |  echo 'Refusing any pre-existing validation namespace resource, regardless of labels.' >&2
0107 |  printf '%s\n' "${resource_conflicts[@]}" >&2
0108 |  exit 1
0109 |fi
0110 |
0111 |"${COMPOSE[@]}" config --quiet
0112 |if [[ "${CHANNELS_CONFIG_ONLY:-0}" == 1 ]]; then
0113 |  echo 'Validation Compose config is valid; no resources were created.'
0114 |  exit 0
0115 |fi
0116 |started=0
0117 |cleanup() {
0118 |  if [[ "$started" == 1 ]]; then
0119 |    "${COMPOSE[@]}" down --volumes --remove-orphans >/dev/null 2>&1 || true
0120 |  fi
0121 |}
0122 |trap 'cleanup; rm -f "$temp_env"' EXIT
0123 |started=1
0124 |
0125 |RUNNER_SCRIPT='set -eu
0126 |target="$1"
0127 |printf "Runner Node: "
0128 |node --version
0129 |apt-get update -qq
0130 |DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssl libssl3 ca-certificates bash git >/dev/null
0131 |rm -rf /var/lib/apt/lists/*
0132 |printf "OpenSSL: "
0133 |openssl version
0134 |ldconfig -p | grep -q "libssl.so.3"
0135 |test -f /workspace/api-app/.env
0136 |cmp -s /workspace/api-app/.env /workspace/api-app/.env.example || { echo "API dotenv mask mismatch." >&2; exit 1; }
0137 |for private_path in /workspace/.env /workspace/.env.testing; do
0138 |  test -f "$private_path"
0139 |  cmp -s "$private_path" /workspace/.env.example || { echo "Root dotenv mask mismatch." >&2; exit 1; }
0140 |done
0141 |bound_sha="$(sha256sum /workspace/api-app/package.json | cut -d " " -f 1)"
0142 |test "$bound_sha" = "$CHANNELS_EXPECTED_API_PACKAGE_SHA256" || { echo "Source bind checksum mismatch before npm." >&2; exit 1; }
0143 |bound_web_sha="$(sha256sum /workspace/web-app/package.json | cut -d " " -f 1)"
0144 |test "$bound_web_sha" = "$CHANNELS_EXPECTED_WEB_PACKAGE_SHA256" || { echo "Web source bind checksum mismatch before npm." >&2; exit 1; }
0145 |test "$(git -c safe.directory=/workspace -C /workspace rev-parse --show-toplevel)" = /workspace
0146 |echo "Principal API/Web source binds and API/root dotenv masks verified before npm."
0147 |cd /workspace/api-app
0148 |npm ci
0149 |prisma_info="$(npx prisma -v)"
0150 |printf "%s\n" "$prisma_info"
0151 |printf "%s\n" "$prisma_info" | grep -q "debian-openssl-3.0.x" || { echo "Prisma did not detect the supported OpenSSL 3 engine." >&2; exit 1; }
0152 |npm run prisma:generate
0153 |cd /workspace/web-app
0154 |npm ci
0155 |case "$target" in
0156 |  api|all)
0157 |    cd /workspace/api-app
0158 |    npm run prisma:migrate
0159 |    npx prisma migrate status
0160 |    npm run lint
0161 |    npm run build
0162 |    npm test
0163 |    npm run test:e2e
0164 |    ;;
0165 |esac
0166 |case "$target" in
0167 |  web|all)
0168 |    cd /workspace/web-app
0169 |    npm run build
0170 |    npm test
0171 |    ;;
0172 |esac
0173 |case "$target" in
0174 |  browser|all)
0175 |    cd /workspace/api-app
0176 |    if [ "$target" = browser ]; then
0177 |      echo "Building API before starting browser fixture services."
0178 |      npm run build
0179 |    fi
0180 |    npm run prisma:migrate
0181 |    npx prisma migrate status
0182 |    cd /workspace/web-app
0183 |    npx playwright install --with-deps chromium
0184 |    npm run test:tela -- --trace off
0185 |    ;;
0186 |esac'
0187 |
0188 |"${COMPOSE[@]}" run --rm -e CHANNELS_EXPECTED_API_PACKAGE_SHA256="$CHANNELS_EXPECTED_API_PACKAGE_SHA256" validation-runner sh -ec "$RUNNER_SCRIPT" channels-validation-runner "$TARGET"
```

## Unchanged critical context foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md

```text
0001 |# Tactical TODO — ST-CON-06
0002 |
0003 |## Title
0004 |LeadsHug — ST-CON-06: Channel abstrato extensível e cutover do envio comum
0005 |
0006 |## Artifact Identity
0007 |- **Artifact type:** tactical_execution_contract
0008 |- **Status:** NotStarted
0009 |- **Version:** 1.2
0010 |- **Created:** 2026-10-20
0011 |- **Template provenance:** copied delphi-ai/templates/todo_template.md before population.
0012 |
0013 |## Context
0014 |Usuário confirmou Channel abstrato/concretos e extensibilidade para Instagram, Facebook/Messenger, Telegram e outros; em2026-10-20 autorizou avançar ao contrato. Este TODO entrega o cutover do envio textual comum atual, não novos provedores reais. MetaClient/EvolutionClient já são interfaces injetadas, mas Conversa/Typebot conhecem ambos e seus parâmetros. O parecer de enquadramento identificou outcomes falsamente tratados como recusa, escopo/versionamento insuficientemente expresso e fallback de canal divergente da política. Decisões abaixo concretizam esses pontos antes da revisão tática. O parecer anterior não satisfaz os gates deste contrato e concordância com conceito não é APROVADO específico.
0015 |
0016 |## Framing Source & Story Slice
0017 |- **Feature brief:** foundation_documentation/artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md
0018 |- **Primary story ID:** ST-CON-06
0019 |- **Why this is the right current slice:** um owner de transporte comum para todos os senders existentes, antes de modelos ST-CON-05 e primeiro envio ST-CON-04.
0020 |- **Direct-to-TODO rationale (required when `Feature brief = direct-to-todo`):** n/a; brief e parecer prévios publicados.
0021 |
0022 |## Contract Boundary
0023 |- This TODO defines **WHAT** must be delivered and what counts as done.
0024 |- `Assumptions Preview` and `Execution Plan` below define **HOW** Delphi currently intends to deliver this contract.
0025 |- This TODO is **bounded but elastic**: Delphi may absorb local discoveries only while they remain inside the same primary objective and the same main approval/review/promotion conversation. Secondary modules may still be touched when they are subordinate to that same slice.
0026 |- If any assumption or plan step changes `Scope`, `Out of Scope`, `Definition of Done`, required validation semantics, public contract, or frozen decisions, update the TODO contract first and request renewed approval before execution continues.
0027 |- If the intended path explicitly authorizes a compatibility shim, fallback bridge, dual-read/dual-write period, or another non-canonical temporary construct, record that authorization in the TODO with exact scope, rationale, and removal/closeout condition. Reviewers must be able to distinguish an approved temporary exception from accidental workaround drift.
0028 |
0029 |## Implementation Intent
0030 |- **Current delivery:** contrato abstrato de envio textual, resolução scoped, implementações atuais e orquestração compartilhada, com política/outcomes/consumers/testes coerentes.
0031 |- **Planned next steps:** reconvergir ST-CON-05 para capacidades de modelos e ST-CON-04 para primeiro envio/intent; redes adicionais em histórias próprias.
0032 |- **Anticipatory implementation authorized now:** somente o ponto de extensão e fake de teste exigidos no D01/08; nenhuma implementação/capacidade real futura.
0033 |- **Rationale:** dependências apontam ao domínio abstrato; protocolo e segredo ficam nos adapters, aceitação/política no domínio.
0034 |
0035 |## Delivery Status Canon (Required)
0036 |- **Current delivery stage:** Pending
0037 |- **Qualifiers:** none
0038 |- **Next exact step:** executor único resolve R05 e proteção R02/R04 após all33610 terminal0; RED49493 confirmou classifier antes da correção; validar falha por remoção dos guards, congelar nova versão e reconvergir all/reviews antes de publicação local/INOUT.
0039 |
0040 |## Active Work State (Required While TODO Remains In `active/`)
0041 |- **Work state:** implementation
0042 |- **Why this state now:** APROVADO específico recebido e binding recarregado; seguir Ordered Steps com executor único e autoridade normal go antes de código.
0043 |- **Exit condition:** implementação aderente com all/assurance/pcv e prova real pós-publicação local; nenhum bloqueador de review aberto antes de entrega.
0044 |
0045 |## Scope
0046 |- [ ] SCOPE-01 — Channel/ChannelResolver abstratos de domínio, registro explícito e instâncias por operação, concretos oficial/não oficial e extensão verificada com fake não WhatsApp.
0047 |- [ ] SCOPE-02 — Migrar envios de Conversa BFF/API pública e respostas Typebot para a mesma orquestração, mantendo autenticações próprias, política e MessageAcceptanceService único.
0048 |- [ ] SCOPE-03 — Contexto autorizado e owner BU/canal, segredos privados, credencial/identidade correntes e fences explícitos; nenhuma troca silenciosa do canal selecionado.
0049 |- [ ] SCOPE-04 — Outcomes tipados verdadeiros, projeção pública explícita de erro/disponibilidade e UI honesta; sem retry externo automático ou garantia de exactly-once.
0050 |- [ ] SCOPE-05 — Runner de inventário positivo antes de testes, harness durável de imports/contrato/PG/Playwright, regressões completas e prova real assistida nos dois vínculos próprios; consolidação/revisões de entrega.
0051 |
0052 |## Provisional Notes (Required if `Qualifiers` includes `Provisional`)
0053 |n/a; sem entrega de produto reivindicada.
0054 |
0055 |## Blocker Notes (Required if `Qualifiers` includes `Blocked`)
0056 |Planejamento não bloqueado; readiness de runtime/túnel/aparelhos revalidada depois da aprovação. Ausência de template aprovado não bloqueia esta história textual em janela válida.
0057 |
0058 |## Execution Lane Tracking (Required)
0059 |- **Local implementation branches:** root/api/web:feature/number-onboarding, confirmar antes de executor; Foundation:main.
0060 |- **Promotion lane path:** local feature → dev → stage → main; nenhum push/deploy de produto nesta autorização local proposta.
0061 |- **Lane-promoted threshold for this TODO:** dev, fora do escopo atual.
0062 |- **Production-ready threshold for this TODO:** main e gates próprios, sem claim atual.
0063 |
0064 |## Promotion Evidence (Required Before `🟣 Lane-Promoted` / `✅ Production-Ready`)
0065 |n/a; só Foundation main é autoridade documental autônoma nesta preparação.
0066 |
0067 |## Out of Scope
0068 |- [ ] Instagram/Messenger/Telegram reais, alteração de identidade/BU/contato/schema ou enums de persistência para novas redes; fake não prova integração real.
0069 |- [ ] Criação/envio de templates, Nova conversa manual/novo intent, importação, campanhas, anexos ou novos fluxos Typebot; ST-CON-05/04 permanecem separados.
0070 |- [ ] Reescrever OAuth/QR/cadastro/lifecycle, rotacionar credenciais, desconectar vínculos ou criar sondagem externa por envio.
0071 |- [ ] Worker/outbox/fila, durable intent/exactly-once externo, retry automático de POST, heurística para unir eco sem ID.
0072 |- [ ] Delphi, worktrees/cópias, gitlinks/.gitmodules, deploy/push de produto, leitura de .env/.env.testing e qualquer read/list/stat/hash/traversal/mount/stage api-app/.local-files.
0073 |
0074 |## Diff Expectation Contract
0075 |Required before delivery. Heading normalized for canonical parser; contract obligation unchanged.
0076 |- **Contract status:** required
0077 |- **Policy:** strict; forbidden/unclassified blocks delivery
0078 |- **User validation:** required on deviation
0079 |- **Comparison mode:** working_tree
0080 |
0081 |### Repository Baselines
0082 || Repository | Path | Baseline ref | Comparison mode |
0083 || --- | --- | --- | --- |
0084 || root | . | 80e3940126f22a941f90dba4f5e801b6c0eb2f58 | working_tree |
0085 || api | api-app | db5a86758a165fac8a1ab587599c37b17890530c | working_tree |
0086 || web | web-app | 74b9d4b714044829796f875d00553f077c1c329d | working_tree |
0087 || foundation | foundation_documentation | 82fa66b33b81b31024dc8cebef9e72e9253964a7 | working_tree |
0088 |
0089 |### Expected Changed Paths
0090 || Repository | Path glob | Change types | Reason |
0091 || --- | --- | --- | --- |
0092 || api | src/domain/channels/transport/** | any | ports/resolver/orquestração/registro e harness |
0093 || api | src/integrations/channels/** | any | concretos e projeções privadas |
0094 || api | src/domain/channels/channel-credential-resolver.ts | M | contexto/versionamento privado, send protegido |
0095 || api | src/domain/inbox/outbound*.ts | any | política/orquestração sem ciclo DI com Conversations |
0096 || api | src/domain/inbox/conversations.service.ts | M | seleção/política e consumo abstrato |
0097 || api | src/domain/inbox/incoming.service.ts | M | Typebot usa saída comum |
0098 || api | src/integrations/meta/meta.client.ts | M | texto com resultado tipado; cadastro preservado |
0099 || api | src/integrations/meta/*.spec.ts | any | wire/erro real do adapter |
0100 || api | src/integrations/evolution/evolution.client.ts | M | texto com resultado tipado |
0101 || api | src/integrations/evolution/*.spec.ts | any | wire/classificação conservadora |
0102 || api | src/surfaces/bff/conversations.controller.ts | M | contexto autorizado e DTO disponibilidade |
0103 || api | src/surfaces/public/conversations.controller.ts | M | contexto API key e projeção compatível |
0104 || api | src/surfaces/bff/bff.module.ts | M | DI da composição única |
0105 || api | src/surfaces/public/public.module.ts | M | DI preservando auth |
0106 || api | src/surfaces/webhooks/webhooks.module.ts | M | DI Typebot/ingress |
0107 || api | test/channel-transport* | A, ?? | PG/contrato/corridas |
0108 || api | test/helpers.ts | M | fakes/DI de contrato |
0109 || api | test/timeline-fixtures.cjs | M | provider controlado de browser |
0110 || api | test/browser-server.cjs | M | bootstrap real |
0111 || api | test/*.e2e-spec.ts | M | suites consumidoras da interface alterada, sem afrouxar assertivas |
0112 || api | src/domain/inbox/*.spec.ts | M | consumo abstrato e regressões |
0113 || web | src/api.ts | M | DTO aditivo disponibilidade |
0114 || web | src/api.spec.ts | M | companion de metadados seguros D10; admissão humana2026-10-20 |
0115 || web | src/telas/Inbox.tsx | M | composer indisponível/motivo e erro |
0116 || web | src/telas/Inbox*.test.tsx | any | render/estado |
0117 || web | e2e/channel-transport* | A, ?? | mutation BFF real |
0118 || web | e2e/number-onboarding-freshness.ts | M | manifesto se afetado |
0119 || web | e2e/timeline-freshness.ts | M | companion chamado antes do manifesto; pathspec positivo antes de discovery; admissão humana2026-10-20 |
0120 || root | scripts/test-channels-local.sh | M | inventário positivo seguro antes de testes |
0121 || foundation | todos/active/features/TODO-leadshug-channel-abstraction.md | A, M | governança/evidências |
0122 || foundation | todos/completed/features/TODO-leadshug-channel-abstraction.md | A | closeout após gates |
0123 || foundation | todos/active/features/TODO-leadshug-official-template-authoring.md | M | handoff sem execução |
0124 || foundation | todos/active/features/TODO-leadshug-start-conversation-by-contact.md | M | handoff sem execução |
0125 || foundation | artifacts/reviews/leadshug-channel-abstraction-20261020/** | any | reviews/evidências |
0126 || foundation | artifacts/feature-briefs/leadshug-channel-abstraction-20261020.md | M | link do contrato |
0127 || foundation | artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md | M | sequência |
0128 || foundation | backlog/README.md | M | próximo gate |
0129 || foundation | artifacts/dependency-readiness.md | M | readiness observada |
0130 || foundation | modules/integrations-and-channels.md | M | ports/outcomes/cutover após entrega |
0131 || foundation | modules/inbox-and-conversations.md | M | política/consumers após entrega |
0132 |
0133 |### Not Expected Changed Paths
0134 || Repository | Path glob | Change types | Reason |
0135 || --- | --- | --- | --- |
0136 || api | .local-files/** | any | privado, nem percorrer |
0137 || api | .env* | any | segredo/config intocados |
0138 || api | prisma/** | any | sem mudança de persistência/migration |
0139 || root | .env* | any | privado |
0140 || root | .gitmodules | any | pipeline-owned |
0141 || root | api-app | any | gitlink pipeline-owned |
0142 || root | web-app | any | gitlink pipeline-owned |
0143 || root | delphi-ai | any | sem self-improvement |
0144 || web | dist/** | any | gerado, não fonte |
0145 |
0146 |### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)
0147 |Guard público preliminar executado com fonte canônica inalterada e invocações Git limitadas ANTES da descoberta por pathspecs positivos (API/Web/root); não é guard final de entrega ou prova dos paths excluídos. Primeiro título com sufixo não foi reconhecido pelo parser; normalizado sem alterar obrigação. A segunda execução encontrou 88 mudanças públicas,85 esperadas e3 diferenças mecânicas de tipo, zero path proibido ou novo path fora do escopo.
0148 |
0149 || Finding | Classification | Resolution / authority |
0150 || --- | --- | --- |
0151 || api:test/channel-transport.e2e-spec.ts aparece ?? e já era adição A aprovada | noise; by-design/no-action in product | Comparação working_tree inclui arquivo ainda não staged; adicionar ?? ao mesmo glob já aprovado representa a mesma adição, não amplia paths nem produto; não stagear fonte por conveniência do guard |
0152 || web:e2e/channel-transport.spec.ts aparece ?? e já era adição A aprovada | noise; by-design/no-action in product | Mesmo ajuste mecânico A,?? no mesmo glob aprovado, sem mudar cobertura ou permissão funcional |
0153 || Foundation TODO aparece A contra baseline82fa66b e constava só M | noise; by-design/no-action in product | O contrato foi criado depois da baseline, portanto A,M expressa a criação/modificação documental já autorizada; nenhum novo artefato/escopo |
0154 |
0155 |Evidência histórica: evidence/public-diff-working-tree-type-no-go.json. Ajuste de representação Git não muda Scope/DoD/decisões/risco/paths e não exige nova aprovação material; as duas admissões de paths reais permanecem validadas separadamente pelo usuário. Descoberta de path real não aprovado continua bloqueada e exige validação humana. Rerun preliminar e final ainda necessários.
0156 |
0157 |## Bounded But Elastic Guardrails
0158 |- **May stay inside this TODO:** DI, DTO/fixture/componente subordinados ao mesmo envio comum e preservação de seus invariantes.
0159 |- **Must update or split the TODO:** schema/novo provedor/capacidade real, template/intent novo, mudança de política fora das decisões e novos endpoints.
0160 |
0161 |## Definition of Done
0162 |- [ ] DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real.
0163 |- [ ] DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes.
0164 |- [ ] DOD-03 — Seleção humana/pública segue última origem determinística ou único vínculo; bot fica no ingresso verificado; policy/janela comuns, ausência/ambiguidade sem fallback e disponibilidade/UI honestas preservam rascunho.
0165 |- [ ] DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout.
0166 |- [ ] DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; finalização pública/humana não rouba claim e bot conserva fila/owner; falhas locais pós-ACK e unknown estão explícitas.
0167 |- [ ] DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot.
0168 |- [ ] DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede.
0169 |- [ ] DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção.
0170 |
0171 |## Validation Steps
0172 |- [ ] VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo, sem subset como aceite, com API/PG reais e bundle servido fresco.
0173 |- [ ] VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco.
0174 |- [ ] VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa.
0175 |- [ ] VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto.
0176 |- [ ] VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff.
0177 |
0178 |## Completion Evidence Matrix (Required Before Delivery Claim)
0179 || Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
0180 || --- | --- | --- | --- | --- | --- | --- | --- |
0181 || DOD-01 | Definition of Done | DOD-01 — Channel e ChannelResolver são abstrações de domínio, com concretos atuais registrados e todos os senders comuns sem imports/dispatch por provider; fake de destinatário opaco prova extensão sem novo canal real. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0182 || DOD-02 | Definition of Done | DOD-02 — Resolução usa contexto server-side autorizado ou ingresso verificado, confere BU/canal/identidade e readiness, mantém segredo privado/contexto imutável e não vaza entre envios concorrentes. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0183 || DOD-03 | Definition of Done | DOD-03 — Seleção humana/pública segue última origem determinística ou único vínculo; bot fica no ingresso verificado; policy/janela comuns, ausência/ambiguidade sem fallback e disponibilidade/UI honestas preservam rascunho. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0184 || DOD-04 | Definition of Done | DOD-04 — Outcomes ACCEPTED/BLOCKED/REJECTED/UNKNOWN e projeções de erro obedecem D04/05; sem ID confirmado não há sucesso, sem retry de POST ou rejeição falsa por timeout. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0185 || DOD-05 | Definition of Done | DOD-05 — MessageAcceptanceService continua owner único e sender/echo conservam ID/autor/unread; finalização pública/humana não rouba claim e bot conserva fila/owner; falhas locais pós-ACK e unknown estão explícitas. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0186 || DOD-06 | Definition of Done | DOD-06 — Runner público corrigido antes de qualquer teste; harness de dependências/contrato, PG e CI-equivalent all/Playwright reais passam com fonte/bundle frescos e regressões de cadastro/API/bot. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0187 || DOD-07 | Definition of Done | DOD-07 — Operador confirma nova IN e resposta OUT em cada vínculo próprio oficial/não oficial após publicação local autorizada; prova observada não promete disponibilidade contínua nem nova rede. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0188 || DOD-08 | Definition of Done | DOD-08 — Decisões consolidadas, arquitetura/critique e assurance/cutover/security/pcv/TQA/final/debt/diff/authority/completion/closeout satisfeitos; consumidores05/04 recebem handoff, sem claim de produção. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0189 || VAL-01 | Validation Steps | VAL-01 — Executar bash scripts/test-channels-local.sh all após boundary positivo, sem subset como aceite, com API/PG reais e bundle servido fresco. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0190 || VAL-02 | Validation Steps | VAL-02 — Exercitar contratos raw HTTP e compartilhados, fake Channel não WhatsApp, autorização BFF/API key/bot e barreiras PG de BUs/credencial/identidade/claim/eco. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0191 || VAL-03 | Validation Steps | VAL-03 — Executar web-app/e2e/channel-transport.spec.ts pelo runner real: envio por ambos, indisponibilidade/ambiguidade, unknown e rascunho, resposta atrasada em troca de BU/conversa. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0192 || VAL-04 | Validation Steps | VAL-04 — Revalidada readiness local, operador faz IN/OUT reais nos dois vínculos reservados, sem tokens em artifacts e sem fixture como substituto. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0193 || VAL-05 | Validation Steps | VAL-05 — Rodar revisões/pcv/cutover/diff público/authority/completion/closeout e consolidar módulos antes de encerrar;05/04 apenas rebase/handoff. | test/runtime/review | test/channel-transport.e2e-spec.ts; e2e/channel-transport.spec.ts; all + gates VAL05; prova real para DOD07/VAL04 | namespace descartável; recursos próprios só assistidos | planned | Nenhum produto/teste/runtime nesta preparação. |
0194 |
0195 |## External Dependency Readiness (Required When External Systems Matter)
0196 || Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
0197 || --- | --- | --- | --- | --- | --- |
0198 || runner Docker próprio | regressões completas | unknown | fonte2026-10-20 | find amplo confirmado, não executado | corrigir antes de RED; Node22/PG16/namespace validation |
0199 || vínculos de teste oficial/QR | prova real de resposta | unknown | CP108 histórico2026-10-19 | prova passada não é saúde atual | revalidar runtime/túnel/operador depois de aprovação |
0200 || semântica de erros de provider | evitar falsa recusa | partial | fontes locais2026-10-20 | adapter atual colapsa falhas | classifier conservador D04, sem inferir de string |
0201 || redes futuras | extensibilidade | unknown | nenhuma integração | só fake independente | contratos próprios de identidade/capacidades, sem alegar funcionamento |
0202 |
0203 |## Profile Scope & Handoffs (Required Before `APROVADO`)
0204 |- **Primary execution profile:** operational-coder
0205 |- **Active technical scope:** nestjs,react,vite,postgresql,prisma,docker
0206 |- **Expected supporting profiles:** strategic-cto,operational-devops,assurance-tester-quality,assurance-security-adversarial
0207 |- **Scope-check command:** python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
0208 |- **Gate 0:** Genesis rejeitado; contexto canônico existente. Genesis rejeitado pelo canon existente; ativo operational-coder com handoffs DevOps/assurance planejados.
0209 |
0210 |### Handoff Log (Update when execution crosses profile boundaries)
0211 || From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
0212 || --- | --- | --- | --- | --- |
0213 || strategic-cto | operational-coder | APROVADO explícito recebido2026-10-20 | API/Web/runner/harness | active; binding reload + authority-execution.json |
0214 || operational-coder | operational-devops | readiness/publicação local | imagem própria e recursos de teste | planned |
0215 || operational-coder | assurance-tester-quality | aderência/cutover/TQA/final | pacote público bounded | planned |
0216 || operational-coder | assurance-security-adversarial | isolamento/segredos/DI | resolução e surfaces | planned |
0217 |
0218 |## Complexity
0219 |- **Level (`small|medium|big`):** big
0220 |- **Checkpoint policy:** section-by-section
0221 |- **Why this level:** cutover cross-stack de todos senders, auth/identidade e contratos de resultado externo, com mudanças funcionais expressas e regressão real.
0222 |
0223 |## Canonical Module Anchors (Required Before APROVADO)
0224 |- **Primary module doc:** foundation_documentation/modules/integrations-and-channels.md
0225 |- **Secondary module docs (if any):** foundation_documentation/modules/inbox-and-conversations.md
0226 |- **Planned decision promotion targets (module sections):** Integrations: Channel/resolução/DI/outcomes/extensão; Inbox: seleção/disponibilidade/saída comum e limites.
0227 |- **Module decision consolidation targets (required):** mesmos targets com provenance D01..10, retirar descrição de dispatch direto; invariantes de BU/aceitação/segredo preservados.
0228 |
0229 |## Decision Pending (Resolve Before Freeze)
0230 |Nenhuma decisão de produto aberta. Assinaturas e semântica material congeladas abaixo para challenge tático; readiness externa continua desconhecida.
0231 |
0232 |## Decisions (Resolved Before Freeze)
0233 |- [x] D-01 — Channel é abstract class no domínio, sendMessage recebe {kind:text,recipientRef:string,text:string} e retorna ChannelSendResult discriminado. recipientRef é opaco ao port; sem E164/WABA/phoneNumberId/instância/QR como contrato universal. Limites4096 atuais permanecem nos consumers atuais, não são requisito universal da abstração. ChannelResolver abstrato retorna implementação registrada; seleção por registro explícito, sem if/provider nos senders. Concretos atuais usam clients HTTP; nenhum new no domínio, global useClass único, ModuleRef/service locator ou singleton mutável de BU/token.
0234 |- [x] D-02 — Resolução recebe referência de conversa/BU/canal carregada server-side após autorização de sessão ou API key OU referência do ingresso já verificado para Typebot; não aceita declaração de provider/owner/credencial do body. Validar owner BU/Mantenedora do vínculo e identidade corrente, ownNumberVerified/verifiedEpoch/readiness/receipt e envelope atuais usando o owner de credenciais existente. Expor somente binding/proveniência safe para aceitação; tokens/IDs de protocolo ficam privados ao concreto. Resolver atual não autoriza ator e não retorna versão: adequação explícita, sem fingir garantia já existente. Auth por sessão/API key/bot mantém fontes diferentes, nunca exigir usuário humano no bot ou tomar disponibilidade como grant.
0235 |- [x] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST não há rollback externo: somente mudança de credentialVersion com identidade/generation/epoch TODOS inalterados permite aceitar o recibo capturado. REAUTORIZAR real incrementa generation, mesmo no mesmo recurso; não substituir a generation antiga. Mudança de identidade/generation/epoch depois do efeito não rebind/migra conteúdo:409 CHANNEL_CONTEXT_CHANGED; ACK conhecido conserva outcome ACCEPTED_LOCAL_INCOMPLETE e localMessageState RECORDED ou UNCONFIRMED conforme D05; sem ID, UNKNOWN. MessageAcceptance conserva seu fence. Testar REAUTORIZAR real concorrente e version-only separadamente. Janela entre leitura/CAS local e rede existe, sem fence atômico externo ou nova operação durável.
0236 |- [x] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
0237 |- [x] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID tenta recordAmbiguousOutbound uma vez por execução: somente commit confirmado permite409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, diagnóstico FALHOU/null-ID, nunca Message ENVIADA. Precedência: mudança detectada de identidade/generation/epoch após dispatch sem ID, inclusive antes ou durante o fence de recordAmbiguousOutbound, devolve409 CHANNEL_CONTEXT_CHANGED/outcome UNKNOWN; não rebind nem grava diagnóstico sob contexto novo. Somente OUTRAS falhas/commit incerto do diagnóstico devolvem503 OUTBOUND_LOCAL_INCOMPLETE/outcome UNKNOWN/evidence ACK_WITHOUT_ID/diagnosticPersistence UNCONFIRMED, sem afirmar diagnóstico gravado; no409 só declarar diagnóstico gravado com evidência positiva do commit capturado, senão UNCONFIRMED. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa. ACK externo válido seguido de QUALQUER falha local de aceitação/reconciliação/finalização conserva outcome ACCEPTED_LOCAL_INCOMPLETE;409 CHANNEL_CONTEXT_CHANGED se fence alterado, senão503 OUTBOUND_LOCAL_INCOMPLETE. Texto fixo O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente. localMessageState RECORDED somente com commit de Message confirmado ou readback positivo pelo owner/chave/proveniência capturados; nos demais casos UNCONFIRMED, inclusive rollback local confirmado pois eco pode ter gravado em paralelo. No máximo um readback local bounded, sem rebind ou nova chamada externa. Falha após Message commit mantém RECORDED mesmo se atribuição/status falhar; nenhum erro local vira recusa externa. Propagação transient do recibo não cria intent/outbox/schema/segundo owner. UI preserva draft e nunca reenvia automaticamente; Typebot interrompe a rodada, sem replay de saídas. Sem durabilidade/recuperação prometida nem união heurística de Message nula ao eco; dedupe sem ID continua limite para ST-CON-04.
0238 |- [x] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), política extraída sem ciclo DI com ConversationsService, executa policy/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/autoria/publicação. Input trusted distingue BFF humano, API EXTERNO com snapshot e bot; autoria/intenção de atribuição entram ANTES do dispatch. Remover message.update e conversation.update de conclusão no controller público; não limpar autoria comprovada no sender/echo. Para respostas humanas/públicas, atribuição após ACCEPTED é condicional sobre owner corrente, nunca snapshot semDono: claim concorrente é preservado, inclusive público vs claim humano e overlap BFF/público. Status humano/público move IN_SERVICE (grupo preservado); resposta aceita após close concorrente pode reabrir sem roubar novo owner. Bot conserva autoria/unread/status de fila/owner humano e não executa essa finalização humana. Toda falha local pós-ACK segue D05 mesmo após Message commit. MessageAcceptance e índices preservados, nenhum schema novo;04 reconverge primeiro envio depois.
0239 |- [x] D-07 — Seleção para resposta BFF/API pública usa última mensagem por createdAt DESC,id DESC (ordenação DB, mesma timeline); se seu vínculo falta, nunca substitui por primeiro/outro conectado. Sem última origem: único vínculo pode ser usado; zero CANAL_AUSENTE400, múltiplos CANAL_AMBIGUO409. Origem sem vínculo CANAL_SELECIONADO_INDISPONIVEL409. Bot usa exclusivamente channelId/identidade do ingresso aceito/verificado, mesmo se outra entrada mais recente vier por outro transporte; sem fallback/rebind. Policy comum avalia readiness e requiresWindow do binding selecionado para TODOS, inclusive bot: corrigir explicitamente bypass atual do Typebot. Reavaliar janela antes de cada texto do bot; expiração bloqueia zeroPOST e interrompe rodada, sem replay. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. disponivel observa localmente seleção/policy/trust/conexão/credencial cadastrada, não prova provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem token/rede/mutação; reutilizar metadados da BU na lista, sem novo fan-out por conversa, medir EPS. GET thread não falha por canal ausente: janela mantém exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null se seleção impossível. Lista pública mantém campos e acrescenta envio_disponivel/motivo_indisponibilidade. API pública mantém criação prévia da conversa, inclusive vazia em erro; mudar isso é contrato04.
0240 |- [x] D-08 — Extensão aberta por factories/registro DI tipado, inicialmente dois providers. Fake com recipientRef user:opaque não telefônico passa pelo mesmo resolver/owner/BFF com conversa seeded e bot/internal fixtures, sem alterar branches/interfaces dos senders. Regressão pública conserva telefone numérico/normalização atual; não exigir handle Telegram no POST /api/v1/messages. Enum físico OFICIAL/NAO_OFICIAL permanece no adapter de binding; fixture pode mapear slot existente ao fake, sem flag de produto nem alegar rede nova persistida. Registrar adapter estende o port; identidade/BU/contato/credenciais/ingress de redes futuras exigem contratos próprios. Capacidades terão ports pequenos em05/04 e lifecycle futuro, sem no-op/NotImplemented/casts/concrete instanceof nos consumers; não implementar runtime antecipado.
0241 |- [x] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
0242 |- [x] D-10 — UI Inbox e ErroDaApi em api.ts preservam outcome e metadados safe de incerteza do backend, exibem texto fixo honesto, bloqueiam composer por disponibilidade/motivo e mantêm draft em qualquer erro/UNKNOWN/ACCEPTED_LOCAL_INCOMPLETE; sem sucesso ou retry automático. Respostas atrasadas em troca BU/conversa conservam fencing monotônico atual. HTTP sucesso/DTOs de mensagem preservados; disponibilidade/outcome aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts positivos/descartáveis. all completo em leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais INOUT assistida dos dois vínculos. Consolidar owners/limites e rebase05/04 só após gates.
0243 |
0244 |## Module Decision Baseline Snapshot (Required Before APROVADO)
0245 || Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
0246 || --- | --- | --- | --- |
0247 || constitution#system-invariants | BU/número, domínio backend, superfícies separadas | Preserve | D01/02/08/09 |
0248 || integrations#invariants | providers adapters, erros determinísticos, segredo privado | Preserve | D01/03/04/05 |
0249 || integrations#send-ST-CON-01 | consumer usa credencial scoped/current/receipt | Preserve | novo binding privado, send readiness intacta |
0250 || inbox#aceitação-ST-CON-01 | MessageAcceptance único, identity/gen/epoch, sender/echo | Preserve | D03/06, sem schema |
0251 || inbox#seleção/atribuição | sem troca automática/sem roubar claim | Preserve | corrigir desvio de fallback e snapshot de owner |
0252 || integrations/inbox#projeção-erros | código técnico específico distingue plataformas | Preserve | mapper explícito, outcome aditivo, sem false refusal de UNKNOWN |
0253 || ST-CON-05/04 pending | modelos/primeiro envio em contratos próprios | Preserve | só handoff/reconvergência, sem execução |
0254 |
0255 |## Decision Baseline (Frozen Before Implementation)
0256 |- [ ] D-01 — Channel é abstract class no domínio, sendMessage recebe {kind:text,recipientRef:string,text:string} e retorna ChannelSendResult discriminado. recipientRef é opaco ao port; sem E164/WABA/phoneNumberId/instância/QR como contrato universal. Limites4096 atuais permanecem nos consumers atuais, não são requisito universal da abstração. ChannelResolver abstrato retorna implementação registrada; seleção por registro explícito, sem if/provider nos senders. Concretos atuais usam clients HTTP; nenhum new no domínio, global useClass único, ModuleRef/service locator ou singleton mutável de BU/token.
0257 |- [ ] D-02 — Resolução recebe referência de conversa/BU/canal carregada server-side após autorização de sessão ou API key OU referência do ingresso já verificado para Typebot; não aceita declaração de provider/owner/credencial do body. Validar owner BU/Mantenedora do vínculo e identidade corrente, ownNumberVerified/verifiedEpoch/readiness/receipt e envelope atuais usando o owner de credenciais existente. Expor somente binding/proveniência safe para aceitação; tokens/IDs de protocolo ficam privados ao concreto. Resolver atual não autoriza ator e não retorna versão: adequação explícita, sem fingir garantia já existente. Auth por sessão/API key/bot mantém fontes diferentes, nunca exigir usuário humano no bot ou tomar disponibilidade como grant.
0258 |- [ ] D-03 — Binding de operação captura channelId/BU/identidade/generation/epoch e activeCredentialVersion oficial, imutáveis e privados no dispatch. Revalidar owner/identidade/readiness/versão imediatamente antes do único POST por leitura/CAS local curta, sem HTTP em tx. Contexto alterado antes do dispatch bloqueia409 CHANNEL_CONTEXT_CHANGED sem rede. Depois do POST não há rollback externo: somente mudança de credentialVersion com identidade/generation/epoch TODOS inalterados permite aceitar o recibo capturado. REAUTORIZAR real incrementa generation, mesmo no mesmo recurso; não substituir a generation antiga. Mudança de identidade/generation/epoch depois do efeito não rebind/migra conteúdo:409 CHANNEL_CONTEXT_CHANGED; ACK conhecido conserva outcome ACCEPTED_LOCAL_INCOMPLETE e localMessageState RECORDED ou UNCONFIRMED conforme D05; sem ID, UNKNOWN. MessageAcceptance conserva seu fence. Testar REAUTORIZAR real concorrente e version-only separadamente. Janela entre leitura/CAS local e rede existe, sem fence atômico externo ou nova operação durável.
0259 |- [ ] D-04 — ChannelSendResult: ACCEPTED exige ID externo string não vazia de resposta válida, não significa entregue ao aparelho; BLOCKED é falha local de política/trust/config antes de HTTP; REJECTED exige recusa síncrona comprovada; UNKNOWN é padrão após POST inconclusivo, com evidence ACK_WITHOUT_ID ou TRANSPORT_UNCONFIRMED. Meta REJECTED apenas HTTP400/401/403 + error Graph válido/sem sucesso ou ID contraditório + is_transient não true + code10/100/190; outros códigos/non2xx/429/5xx/timeout/redirect/malformed permanecem UNKNOWN. Evolution pós-dispatch falha é UNKNOWN nesta versão; não inventar classifier por texto/status sem evidência de recusa. Raw clients têm resultado tipado para texto; métodos de cadastro conservam contratos/erros. Uma invocação externa, timeout10s, sem retries/sondagens/grant HTTP extras por envio.
0260 |- [ ] D-05 — Projeção pública de REJECTED conserva400 META_RECUSOU ou EVOLUTION_RECUSOU por mapper de composição, sem branch no negócio; texto fixo O canal recusou o envio e outcome REJECTED aditivo. UNKNOWN ACK_WITHOUT_ID tenta recordAmbiguousOutbound uma vez por execução: somente commit confirmado permite409 EXTERNAL_MESSAGE_ID_MISSING/outcome AMBIGUOUS_SEND_RECORDED, diagnóstico FALHOU/null-ID, nunca Message ENVIADA. Precedência: mudança detectada de identidade/generation/epoch após dispatch sem ID, inclusive antes ou durante o fence de recordAmbiguousOutbound, devolve409 CHANNEL_CONTEXT_CHANGED/outcome UNKNOWN; não rebind nem grava diagnóstico sob contexto novo. Somente OUTRAS falhas/commit incerto do diagnóstico devolvem503 OUTBOUND_LOCAL_INCOMPLETE/outcome UNKNOWN/evidence ACK_WITHOUT_ID/diagnosticPersistence UNCONFIRMED, sem afirmar diagnóstico gravado; no409 só declarar diagnóstico gravado com evidência positiva do commit capturado, senão UNCONFIRMED. UNKNOWN TRANSPORT_UNCONFIRMED conserva ausência de Message autoritativa dos throws atuais e400/código legado projetado, mas texto fixo Resultado do envio não confirmado; confira a conversa antes de tentar novamente e outcome UNKNOWN aditivo. Código legado não prova recusa. ACK externo válido seguido de QUALQUER falha local de aceitação/reconciliação/finalização conserva outcome ACCEPTED_LOCAL_INCOMPLETE;409 CHANNEL_CONTEXT_CHANGED se fence alterado, senão503 OUTBOUND_LOCAL_INCOMPLETE. Texto fixo O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente. localMessageState RECORDED somente com commit de Message confirmado ou readback positivo pelo owner/chave/proveniência capturados; nos demais casos UNCONFIRMED, inclusive rollback local confirmado pois eco pode ter gravado em paralelo. No máximo um readback local bounded, sem rebind ou nova chamada externa. Falha após Message commit mantém RECORDED mesmo se atribuição/status falhar; nenhum erro local vira recusa externa. Propagação transient do recibo não cria intent/outbox/schema/segundo owner. UI preserva draft e nunca reenvia automaticamente; Typebot interrompe a rodada, sem replay de saídas. Sem durabilidade/recuperação prometida nem união heurística de Message nula ao eco; dedupe sem ID continua limite para ST-CON-04.
0261 |- [ ] D-06 — Orquestração outbound comum no domínio inbox (outbound*.ts), política extraída sem ciclo DI com ConversationsService, executa policy/Channel/result mapping e delega toda Message com ID ao MessageAcceptanceService atual; nenhum segundo owner de insert/unique/autoria/publicação. Input trusted distingue BFF humano, API EXTERNO com snapshot e bot; autoria/intenção de atribuição entram ANTES do dispatch. Remover message.update e conversation.update de conclusão no controller público; não limpar autoria comprovada no sender/echo. Para respostas humanas/públicas, atribuição após ACCEPTED é condicional sobre owner corrente, nunca snapshot semDono: claim concorrente é preservado, inclusive público vs claim humano e overlap BFF/público. Status humano/público move IN_SERVICE (grupo preservado); resposta aceita após close concorrente pode reabrir sem roubar novo owner. Bot conserva autoria/unread/status de fila/owner humano e não executa essa finalização humana. Toda falha local pós-ACK segue D05 mesmo após Message commit. MessageAcceptance e índices preservados, nenhum schema novo;04 reconverge primeiro envio depois.
0262 |- [ ] D-07 — Seleção para resposta BFF/API pública usa última mensagem por createdAt DESC,id DESC (ordenação DB, mesma timeline); se seu vínculo falta, nunca substitui por primeiro/outro conectado. Sem última origem: único vínculo pode ser usado; zero CANAL_AUSENTE400, múltiplos CANAL_AMBIGUO409. Origem sem vínculo CANAL_SELECIONADO_INDISPONIVEL409. Bot usa exclusivamente channelId/identidade do ingresso aceito/verificado, mesmo se outra entrada mais recente vier por outro transporte; sem fallback/rebind. Policy comum avalia readiness e requiresWindow do binding selecionado para TODOS, inclusive bot: corrigir explicitamente bypass atual do Typebot. Reavaliar janela antes de cada texto do bot; expiração bloqueia zeroPOST e interrompe rodada, sem replay. Cálculo temporal atual preservado; trusted timestamp novo pertence a04. disponivel observa localmente seleção/policy/trust/conexão/credencial cadastrada, não prova provider ativo/decrypt/grant externo; POST revalida. GET usa só metadados, sem token/rede/mutação; reutilizar metadados da BU na lista, sem novo fan-out por conversa, medir EPS. GET thread não falha por canal ausente: janela mantém exigida/aberta/expiraEm/canal e acrescenta disponivel:boolean/motivo:enum|null; aberta=false/canal=null se seleção impossível. Lista pública mantém campos e acrescenta envio_disponivel/motivo_indisponibilidade. API pública mantém criação prévia da conversa, inclusive vazia em erro; mudar isso é contrato04.
0263 |- [ ] D-08 — Extensão aberta por factories/registro DI tipado, inicialmente dois providers. Fake com recipientRef user:opaque não telefônico passa pelo mesmo resolver/owner/BFF com conversa seeded e bot/internal fixtures, sem alterar branches/interfaces dos senders. Regressão pública conserva telefone numérico/normalização atual; não exigir handle Telegram no POST /api/v1/messages. Enum físico OFICIAL/NAO_OFICIAL permanece no adapter de binding; fixture pode mapear slot existente ao fake, sem flag de produto nem alegar rede nova persistida. Registrar adapter estende o port; identidade/BU/contato/credenciais/ingress de redes futuras exigem contratos próprios. Capacidades terão ports pequenos em05/04 e lifecycle futuro, sem no-op/NotImplemented/casts/concrete instanceof nos consumers; não implementar runtime antecipado.
0264 |- [ ] D-09 — Um módulo de composição de transporte exporta resolver/orquestração para BFF/Public/Webhooks, mantendo middlewares e autenticações separados. Clients específicos podem ser usados por cadastro e adapters de protocolo, não por consumidores comuns de envio. Harness durável de dependências bloqueia imports/dispatch provider em Conversations/Incoming e no owner outbound comum, com allowlist exata de adapters/registro/mapper; testar o harness com violação sintética. Sem compat wrapper de envio antigo ou dispatch paralelo após cutover; fixture/mocks/DI de todas superfícies adaptados, não apenas testes novos.
0265 |- [ ] D-10 — UI Inbox e ErroDaApi em api.ts preservam outcome e metadados safe de incerteza do backend, exibem texto fixo honesto, bloqueiam composer por disponibilidade/motivo e mantêm draft em qualquer erro/UNKNOWN/ACCEPTED_LOCAL_INCOMPLETE; sem sucesso ou retry automático. Respostas atrasadas em troca BU/conversa conservam fencing monotônico atual. HTTP sucesso/DTOs de mensagem preservados; disponibilidade/outcome aditivos. Antes de qualquer RED/teste corrigir scripts/test-channels-local.sh para inventário positivo sem percorrer API root/.local-files ou ler dotenv privado; mounts positivos/descartáveis. all completo em leadshug_channels_validation/Node22/PG16, API3100/provider3101/Web4173, mais INOUT assistida dos dois vínculos. Consolidar owners/limites e rebase05/04 só após gates.
0266 |
0267 |## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)
0268 |- **Applicability (`required|not_needed`):** required
0269 |- **Why this applies:** estabelece port comum e retira dispatch específico duplicado dos negócios.
0270 |- **Deviation / debt being retired:** Consumers dependem de dois providers/IDs e mapeiam toda falha como recusa; seleção/atribuição violam intenção canônica.
0271 |- **Target steady-state after closeout:** Channel/Resolver de domínio, registro/adapters privados, uma saída comum e aceitação única.
0272 |- **Temporary exceptions allowed:** none
0273 |- **Cutover / removal condition:** nenhum sender comum usa provider client/dispatch antigo; cadastro/protocolo específicos permanecem legítimos e não são compat shim.
0274 |
0275 |### Patterns To Enforce (Required when applicability = `required`)
0276 || Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
0277 || --- | --- | --- | --- |
0278 || consumidor depende do Channel | D01/08/09 | outbound | extensibilidade verificável |
0279 || contexto privado por operação | D02/03 | resolver/concretos | sem vazamento ou cross-BU |
0280 || aceitação única | ST-CON-01/D06 | todos senders | dedupe/autoria/epoch |
0281 |
0282 |### Prohibited Anti-Patterns (Required when applicability = `required`)
0283 || Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
0284 || --- | --- | --- | --- |
0285 || adicionar interface e manter branch no sender | dependency harness/AST | falso DIP | none |
0286 || singleton que troca token/BU | barriers concorrentes | cross-tenant | none |
0287 || timeout como recusa ou retry POST | raw HTTP count | efeito externo incerto | none |
0288 || mega-interface com no-op/cast específico | shared contract/fake | quebra substituição/segregação | none |
0289 |
0290 |### Architecture Protection Harness (Required when applicability = `required`)
0291 || Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
0292 || --- | --- | --- | --- | --- | --- |
0293 || dependency guard/test | api src/domain/channels/transport/channel-dependencies.spec.ts | all + violation fixture | imports/dispatch diretos fora allowlist | implement-in-this-todo | DOD01/06/08 |
0294 || shared contract/PG | api test/channel-transport.e2e-spec.ts | all | substituição/scopes/identity/unknown/echo/claim | implement-in-this-todo | DOD02..06/VAL02 |
0295 || browser real BFF | web e2e/channel-transport.spec.ts | all | disponibilidade/envio/erro/rascunho/freshness | implement-in-this-todo | DOD03/04/06/VAL03 |
0296 |
0297 |## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)
0298 |- **Architecture decision review:** required
0299 |- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
0300 |- **Decision review kind:** architecture_opinion
0301 |- **Decision review package:** bounded-file-set
0302 |- **Decision review status:** findings_integrated
0303 |- **Decision review evidence / resolution:** artifacts/reviews/leadshug-channel-abstraction-20261020/architecture-opinion.md; parecer tático terminal no-go inicial, AR01..04 e obrigações integrados pelo owner antes da crítica; sem claim de implementação.
0304 |- **Architecture adherence review:** required
0305 |- **Adherence review lifecycle:** after implementation and before Completed
0306 |- **Adherence review kind:** architecture_adherence
0307 |- **Adherence review package:** bounded-file-set
0308 |- **Adherence review status:** not_run
0309 |- **Adherence review evidence / resolution:** planned after implementation
0310 |- **No-go handling:** reconvergir contrato, sem waiver automático.
0311 |
0312 |## Gate: Review Baseline Freeze
0313 |- **Gate decision:** required
0314 |- **Why this decision:** publicar autoridade do contrato antes de review/guard.
0315 |- **Trigger stage:** before the first planning-side review or guard run
0316 |- **Baseline branch:** main
0317 |- **Baseline commit:** a35f676c696e21ec8b4e8ed5cbe6eafbe8da482c
0318 |- **Baseline push reference:** origin/main
0319 |- **Gate status:** no_material_findings
0320 |- **Findings summary:** contrato publicado antes dos reviews/guardas; somente freeze metadata factual acrescentada depois.
0321 |- **Evidence / reference:** origin/maina35f676c696e21ec8b4e8ed5cbe6eafbe8da482c push terminal0 em2026-10-20; CR01/02 integrados antes de reconvergência do reviewer.
0322 |- **Waiver authority / reference (required if waived):** n/a
0323 |
0324 |## Gate: Review Scope Drift
0325 |- **Gate decision:** required
0326 |- **Why this decision:** aprovação usa o pacote efetivamente revisado.
0327 |- **Trigger stage:** after the planning-side review/guard cycle converges and before APROVADO
0328 |- **Baseline source:** Review Baseline Freeze -> Baseline commit
0329 |- **Material sections compared:** Context|Scope|Out of Scope|Definition of Done|Validation Steps|Decisions|Decision Baseline|Assumptions Preview|Execution Plan|Security Risk Assessment|Performance & Concurrency Risk Assessment
0330 |- **Guard command:** python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
0331 |- **No-go handling rule:** reconvergir review/freeze, sem código.
0332 |- **Gate status:** no_material_findings
0333 |- **Findings summary:** guard go;23 seções materiais comparadas,0 alterações frente a baselinea35f676c publicada/revisada.
0334 |- **Evidence / reference:** foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/review-scope-drift.json
0335 |- **Waiver authority / reference (required if waived):** n/a
0336 |
0337 |## Questions To Close
0338 |Nenhuma decisão funcional de produto aberta; D01..10 cobrem limites para challenge independente. Readiness real não é aprovação de escopo.
0339 |
0340 |## Pattern References (Optional; Enforced When Cited)
0341 |n/a; decisões/canon citados diretamente, sem ID de catálogo presumido.
0342 |
0343 |## Assumptions Preview (Required Before Plan Review)
0344 || Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
0345 || --- | --- | --- | --- | --- | --- |
0346 || A-01 | dois senders comuns escolhem diretamente Meta/Evolution. | api-app/src/domain/inbox/conversations.service.ts; api-app/src/domain/inbox/incoming.service.ts | ampliar inventário/reconvergir | High | Keep as Assumption |
0347 || A-02 | credential resolver não verifica actor grant e não retorna active version. | api-app/src/domain/channels/channel-credential-resolver.ts | reutilizar mecanismo real, sem duplicação | High | Keep as Assumption |
0348 || A-03 | aceitação é owner único keyed e faz fence de identidade. | api-app/src/domain/inbox/message-acceptance.service.ts | corrigir boundary antes de cutover | High | Keep as Assumption |
0349 || A-04 | BFF/API pública respondem pelo ConversationsService; compose DI repetida. | api-app/src/surfaces/bff/conversations.controller.ts; api-app/src/surfaces/public/conversations.controller.ts; api-app/src/surfaces/bff/bff.module.ts | adaptar todos consumers legítimos | High | Keep as Assumption |
0350 || A-05 | browser usa backend real/build e runner faz find amplo. | web-app/playwright.config.ts; scripts/test-channels-local.sh | readiness antes de teste | High | Keep as Assumption |
0351 |
0352 |## Execution Plan (Required Before `APROVADO`)
0353 |### Touched Surfaces
0354 |Somente Diff Expectation Contract; nenhuma superfície privada/produto modificada durante preparação.
0355 |
0356 |### Ordered Steps
0357 |1. APROVADO específico, reload binding e authority/routing go, executor único no checkout principal. Corrigir runner para inventário positivo ANTES de qualquer teste, inclusive RED; não executar find antigo.
0358 |2. Test-first: harness dependências com negativa sintética, contrato Channel/fake opaco, raw HTTP/resultados/scopes/seleção. PG barriers/readbacks próprios; contexto muda antes do diagnóstico null-ID e durante seu fence vs falha ordinária/commit incerto:409/503/outcome/metadados, um POST e nenhum replay.
0359 |3. Ports/concretos/registro/binding privado com credencial owner existente; revalidar contexto e classificar outcomes, sem duplicar aceitação.
0360 |4. Orquestração/cutover BFF/Public/Typebot, política/projeção/DTO e UI indisponível/unknown; retirar dispatch antigo e adaptar fakes/DI de suites existentes.
0361 |5. CI-equivalent all completo em recursos descartáveis, Playwright real/fonte-servido e pcv. Não testar ambiente humano por conveniência.
0362 |6. DevOps revalida runtime/túnel e publica API/Web locais do código aprovado, conservando banco/canais; operador valida INOUT dos dois vínculos próprios. Nenhuma rotação/repareamento automático.
0363 |7. Adherence/cutover/security/TQA/final/debt/diff/authority/completion/closeout, módulos e handoff05/04; nenhum push/deploy de produto automático.
0364 |
0365 |### Test Strategy
0366 |- **Strategy:** test-first
0367 |- **Why:** cutover de side effects externos/auth e substituição real.
0368 |- **Fail-first target(s) (when required):** dependency guard, fake opaco, raw unknown, owner/contexto e política seleção/claim.
0369 |
0370 |### Pre-APROVADO RED Evidence Capture (Optional for bugfix/regression)
0371 |- **Decision (`required|recommended|not_needed|waived`):** not_needed
0372 |- **Why now:** direção nova com diagnóstico por fonte suficiente; sem execução para congelar hipótese.
0373 |- **Target symptom:** n/a
0374 |- **Allowed surfaces:** none
0375 |- **Forbidden surfaces reaffirmed:** production code|runtime/config/deploy|canonical project docs outside TODO authoring
0376 |- **Planned command / target:** n/a
0377 |- **Status (`not_run|running|red_reproduced|red_not_reproduced|blocked|waived`):** not_run
0378 |- **Findings summary:** nenhuma execução de produto/testes atual.
0379 |
0380 |### Flow Evidence Planning Matrix (Required Before `APROVADO`)
0381 || Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
0382 || --- | --- | --- | --- | --- | --- | --- | --- |
0383 || DOD01/02 substituição/scope | refactor/auth/context | web-only | API PG + browser mutation | yes | yes | channel-transport.e2e/spec e shared contracts | n/a |
0384 || DOD03/04 disponibilidade/outcome | DTO/composer/persistência | web-only | Playwright mutation | yes | yes | e2e/channel-transport.spec.ts com BFF real | n/a |
0385 || DOD05/06 + VAL01/02/03 | aceitação/claim/echo/cutover | web-only | PG barriers + browser mutation | yes | yes | suites completas e served freshness | n/a |
0386 || DOD07/VAL04 | recursos verdadeiros | web-only | operador local | yes | yes | receipt redigido de INOUT dos dois vínculos | fake não substitui |
0387 || DOD08/VAL05 | consolidação/qualidade | web-only | audits + provas anteriores | yes | yes | pacote/guards por critério | n/a |
0388 |
0389 |### Local CI-Equivalent Suite Matrix (Required Before `APROVADO` and Before Delivery Claim)
0390 |Colunas Status duplicadas projetam o mesmo fato para leitores determinísticos de índices distintos; evidence inclui ressalvas.
0391 |
0392 || Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status (completion projection) | Evidence Artifact / Command | Status (authority projection) | Notes | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions |
0393 || --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0394 || api / all PG/units/contracts | cutover/DI/auth/HTTP | bash scripts/test-channels-local.sh all | Local-Implemented | planned | npm ci/lint/build/unit/E2E completos + migration deploy/status de baseline | planned | subset só diagnóstico | Channel contract/opaque fake/unknown/scope/current identity/echo/claim | Node22/PG16 próprios; dois tenants/BUs; api-key e actor humano/bot; lease barriers/provider controlado |
0395 || web / all build/unit/browser | DTO/composer/erro | bash scripts/test-channels-local.sh all | Local-Implemented | planned | spec channel-transport e regressões completas, BFF não mockado | planned | mesmo all | positivo ambos, canal ausente/ambíguo, draft unknown e contexto atrasado | Web4173/API3100/provider3101, mesma DB/resolução da CI, bundle fresco |
0396 || root / runner topology | positive inventory | bash scripts/test-channels-local.sh all | Local-Implemented | planned | manifests/masks fictícios; nenhuma leitura dotenv/.local-files | planned | sem namespace humano | safe mount/config e origem da principal | leadshug_channels_validation inexistente antes do run, dados descartáveis |
0397 |
0398 |### Runtime / Rollout Notes
0399 |Sem migration nova/schema/enum. Migrations existentes deploy/status em PG descartável fazem parte de all. Namespace validation exclusivo, bundles/builds da principal. Runtime humano somente publicação local planejada e prova assistida depois de readiness; banco/canais preservados, sem reset ou rotação. Nenhum transporte real futuro ou status externo de entrega presumido.
0400 |
0401 |## Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)
0402 |### Review Sections
0403 |- [x] Architecture
0404 |- [x] Code Quality
0405 |- [x] Tests
0406 |- [x] Performance
0407 |- [x] Security
0408 |- [x] Elegance
0409 |- [x] Structural Soundness
0410 |
0411 |Revisão de planejamento concluída: architecture_opinion findings_integrated e crítica fresh terminal go. Checkboxes representam análise do plano, não execução/testes/medição do produto. PLAN01/02 opçãoA adotada; AR01..04/CR01..02 resolvidos nos relatórios.
0412 |
0413 |### Issue Cards
0414 |- **Issue ID:** PLAN-01
0415 |  - **Severity:** high
0416 |  - **Evidence:** conversations.service.ts:300; incoming.service.ts:94; resolver:24 não autoriza ator.
0417 |  - **Why it matters now:** falsa abstração ou singleton de token mantém acoplamento/vaza escopo.
0418 |  - **Option A (Recommended):** ports de domínio, contexto por operação, registro explícito e auth trusted-scoped.
0419 |    - **Effort:** medium; **Risk:** medium; **Blast radius:** cross-module; **Maintenance burden:** low; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
0420 |  - **Option B (Alternative):** wrapper com switch no próprio consumer e config global.
0421 |    - **Effort:** low; **Risk:** high; **Blast radius:** cross-module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
0422 |  - **Option C (Do Nothing):** manter providers atuais; **Effort:** low; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** regresses.
0423 |  - **Recommendation:** A; direção humana expressa e menor mecanismo fiel ao escopo.
0424 |- **Issue ID:** PLAN-02
0425 |  - **Severity:** high
0426 |  - **Evidence:** clients atuais string/null e generic errors, fallback canais[0].
0427 |  - **Why it matters now:** contrato de substituição precisa outcomes e política verdadeiros, não apenas nomes iguais.
0428 |  - **Option A (Recommended):** D03..07 com UNKNOWN conservador, projeção compatível e seleção explícita.
0429 |    - **Effort:** medium; **Risk:** medium; **Blast radius:** cross-stack; **Maintenance burden:** medium; **Performance impact:** neutral; **Elegance impact:** improves; **Structural soundness impact:** improves.
0430 |  - **Option B (Alternative):** ocultar falhas como recusa e trocar canal para enviar.
0431 |    - **Effort:** low; **Risk:** high; **Blast radius:** cross-stack; **Maintenance burden:** high; **Performance impact:** regresses; **Elegance impact:** regresses; **Structural soundness impact:** regresses.
0432 |  - **Option C (Do Nothing):** adiar o cutover; **Effort:** low; **Risk:** medium; **Blast radius:** module; **Maintenance burden:** high; **Performance impact:** neutral; **Elegance impact:** neutral; **Structural soundness impact:** neutral.
0433 |  - **Recommendation:** A; sem plataforma de operação durável antecipada.
0434 |
0435 |### Failure Modes & Edge Cases
0436 |- [ ] BUs concorrentes, actor sem grant, bot de tenant alheio, owner de canal divergente e stale epoch/version.
0437 |- [ ] selected channel removido, dois vínculos sem última origem, leitura segura sem envio habilitado e draft preservado.
0438 |- [ ] POST efeito seguido de timeout/5xx/malformed, ID ausente e receipt tardio após rotação/retirada.
0439 |- [ ] eco antes/depois do sender; público vs claim humano/overlap BFF; Typebot retido enquanto outra origem chega, janela expira ou contexto muda; empate de createdAt entre transportes.
0440 |- [ ] falha antes de acceptance, commit incerto, Message commit seguido de erro na finalização e diagnóstico null-ID sem commit: projeções D03/05, sem replay.
0441 |- [ ] UI troca A→B→A durante erro/envio; nenhum retry ou limpeza de draft de outra conversa.
0442 |
0443 |### Residual Unknowns / Risks
0444 |- [ ] Cutover sem intent durável conserva limite de crash antes da aceitação/publicação e diagnósticos null-ID sem dedupe; ST-CON-04 deve reconvergir esse limite, não inferir exactly-once.
0445 |- [ ] Port extensível não significa persistência/contato/ingress de rede nova pronto; fake só prova substituição interna.
0446 |- [ ] Readiness real e medições só depois de aprovação; coorte privada continua, sem produção/usuário não confiável liberado.
0447 |- [ ] Arquitetura integrada e crítica fresh reconvergida go no pacote v1.2; guardas finais de planejamento abaixo, toda prova de produto permanece planned.
0448 |
0449 |## Additional Architectural Opinions (Required When Path Remains Materially Unclear)
0450 |- **Needed:** no
0451 |- **Why ambiguity remains:** diagnóstico teve parecer independente de enquadramento; agora gate architecture_opinion desafia D01..10, sem tratá-lo como duplicado satisfeito.
0452 |- **Opinion count:** 1 framing advisory,1 tactical terminal com achados integrados
0453 |- **Package mode:** bounded-file-set
0454 |- **Internal reviewer mandate:** required na gate tática
0455 |- **Required lenses:** correctness,performance,elegance,structural-soundness,operational-fit
0456 |
0457 |## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)
0458 |- **Canonical method:** wf-docker-audit-escalation-method
0459 |- **Guard command:** python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
0460 |- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/audit-floor.json; go/fa884bf1d2e7
0461 |
0462 || Trigger | Value | Notes |
0463 || --- | --- | --- |
0464 || complexity | big | cutover completo do envio comum |
0465 || blast_radius | cross-stack | API/Web/runner |
0466 || behavioral_change_or_bugfix | yes | política/erros/claim explícitos |
0467 || changes_public_contract | yes | campos aditivos/erro honesto |
0468 || touches_auth_or_tenant | yes | resolver e contexto |
0469 || touches_runtime_or_infra | yes | runner/publicação local |
0470 || touches_tests | yes | harness/suites |
0471 || critical_user_journey | yes | respostas reais |
0472 || release_or_promotion_critical | no | só local |
0473 || high_severity_plan_review_issue | yes | PLAN01/02 |
0474 || explicit_three_lane_request | no | floor derivado |
0475 |
0476 |## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)
0477 |- **Critique decision:** required
0478 |- **Why this decision:** big/cross-stack/auth/side effect e cutover arquitetural.
0479 |- **Impact signals in scope:** public contract/schema/api|auth|runtime
0480 |- **Package mode:** bounded-file-set
0481 |- **Package minimum contents:** TODO publicado, fontes públicas exatas, parecer/disposição e matrizes/risco.
0482 |- **Critique isolation mode:** fresh internal no-context reviewer
0483 |- **Internal reviewer mandate:** required, não executor; aguardar terminal sem prazo rígido.
0484 |- **Critique lenses:** correctness,performance,elegance,structural-soundness,risk
0485 |- **Critique status:** no_material_findings
0486 |- **Findings summary:** CR01/02 integrados; reconvergência terminal go no contrato completo v1.2/baselinea35f676c, nenhum achado material aberto. Parecer no-go original preservado no ledger.
0487 |- **Resolution ledger:** artifacts/reviews/leadshug-channel-abstraction-20261020/critique.md
0488 |- **Evidence / reference:** artifacts/reviews/leadshug-channel-abstraction-20261020/critique.md; fresh /root/stcon06_critique gpt-6.1-sol/max, inicial81d56f5e + reconvergência terminala35f676c.
0489 |- **Waiver authority / reference (required if waived):** n/a
0490 |
0491 |## Gate: Assumption Code Coherence
0492 |- **Gate decision:** required
0493 |- **Why this decision:** premissas concretas de senders/resolver/aceitação/runtime.
0494 |- **Trigger stage:** after critique convergence and before APROVADO
0495 |- **Guard scope:** A01..05
0496 |- **Guard command:** python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-channel-abstraction.md
0497 |- **Gate status:** no_material_findings
0498 |- **Findings summary:** revisão semântica A01..05 ancorada em fonte pública e conferida por arquitetura/crítica; adequações são trabalho explícito, sem fingir garantias atuais.
0499 |- **Evidence / reference:** foundation_documentation/artifacts/reviews/leadshug-channel-abstraction-20261020/source-assumptions.json; architecture-opinion.md; critique.md; evidence/assumption-coherence.json, guard go/5 premissas.
0500 |- **Waiver authority / reference (required if waived):** n/a
0501 |
0502 |## Approval
0503 |- **Approved by:** usuário — autoridade humana deste contrato
0504 |- **Approval reference:** resposta literal APROVADO nesta conversa em2026-10-20, após apresentação do contrato v1.2 publicado em Foundation781ea16e51e0db2a654e6956ea633a03dd509dfd (freeze materiala35f676c).
0505 |- **Approval scope:** ST-CON-06/SCOPE01..05/D01..10, depois da convergência do pacote concreto; concordância com conceito não substitui APROVADO.
0506 |- **Execution not authorized by approval:** todo Out of Scope, redes futuras,05/04, push/deploy de produto ou mudanças privadas.
0507 |- **Renewed approval required when:** decisões/DoD/paths/risco/contrato mudarem materialmente.
0508 |- **Pre-approval readiness evidence:** artifacts/reviews/leadshug-channel-abstraction-20261020/README.md; authority-preapproval.json = preflight-go, execution_authority_granted=false; estrutura PASS. APROVADO específico recebido; authority normal pós-ingestão registrado em evidence/authority-execution.json.
0509 |
0510 |## Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)
0511 |Binding reload realizado após APROVADO em2026-10-20 pelo orquestrador: fontes da tabela relidas; constituição/política/módulos recarregados e verify_context PACED-Ready. Executor relerá as regras técnicas pertinentes antes dos edits. Ingestão não é evidência de implementação/testes. Nenhum GOAL persistente foi criado.
0512 |
0513 || Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
0514 || --- | --- | --- | --- | --- |
0515 || delphi-ai/main_instructions.md | autoridade e roteamento | executor único | código no planejamento | handoff após aprovação |
0516 || delphi-ai/workflows/docker/todo-approval-gates-method.md | aprovação | freeze/reviews/APROVADO | concordância genérica como execução | authority pré/post |
0517 || delphi-ai/workflows/docker/effort-selection-method.md | routing | agent_role_routing_guard.py | fingir modelo primário | guard antes da lane |
0518 || delphi-ai/workflows/nestjs/change-application-boundary-method.md | BFF/domínio | adapters finos | regra no controller | contratos E2E |
0519 || delphi-ai/workflows/react/change-ui-boundary-method.md | formulário/estado | freshness/draft | resposta atrasada | Playwright mutation |
0520 || delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | schema | migration versionada | reset operacional | deploy/status descartável |
0521 || delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | intenção/locks | unique/CAS | HTTP em tx | barriers reais |
0522 || foundation_documentation/project_constitution.md | multi-tenant | BU/Contato | credencial global | testes scoped |
0523 || foundation_documentation/policies/scope_subscope_governance.md | rotas existentes | BFF sessão | endpoint fora do owner | contrato explícito |
0524 || delphi-ai/workflows/docker/performance-concurrency-validation-method.md | pcv-1 | quatro lanes | prose sem artefato | JSON/hash antes entrega |
0525 |
0526 |## Agent Routing Preflight (Required Before Execution When Effort/Model Routing Applies)
0527 |- **Client surface:** codex
0528 |- **Current governed action:** implementation
0529 |- **Selected role:** routine-executor
0530 |- **Selected model:** gpt-6-luna
0531 |- **Selected effort:** medium
0532 |- **Proof mode:** declared
0533 |- **Exception reason:** n/a
0534 |- **Subagent / delegation authorization:** AGENTS/main instructions/workflows exigem reviews internos e executor; código só após APROVADO.
0535 |- **Execution topology:** primary-checkout-single-writer
0536 |- **Worktree / auxiliary-checkout authorization:** not-authorized
0537 |- **Worktree authorization evidence:** n/a
0538 |- **Writer scheduling policy:** single-writer-serialized
0539 |- **Guard outcome:** go
0540 |- **Waiver / exception reference:** n/a
0541 |
0542 |Reviewers architecture_opinion e critique: gpt-6.1-sol/max, fresh fork_turns none, routing go distinto antes de dispatch. Primário não se declara outro modelo. Nenhum GOAL persistente criado sem pedido humano.
0543 |
0544 |## Decision Adherence Validation (Mandatory Before Delivery)
0545 |Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.
0546 |
0547 |## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)
0548 |Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.
0549 |
0550 |## Pipeline/Copilot P1/P2 Preflight
0551 |Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.
0552 |
0553 |## Rule-Spirit Anti-Pattern Hunt
0554 |Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.
0555 |
0556 |## Promotion Finding Routing Ledger (Required When Promotion/Review Finds Any Finding)
0557 |
0558 |Terminal architecture/security findings classified by review-finding-classification. All current-slice findings remain blockers until fixed and evidenced; no waiver/debt accepted. Exact text and deduplication: artifacts/reviews/leadshug-channel-abstraction-20261020/implementation-round-1-resolution.md.
0559 |
0560 || Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
0561 || --- | --- | --- | --- | --- | --- | --- |
0562 || ST06-R01 (ADH-01=SEC-01) | high | release-blocker | same-todo | Original non-first/malformed-ID counterexample corrected; new flag case tracked R05 | resolved in round2 snapshot; finalvalidation pending | implementation-round-1-resolution.md; existing D04 approval |
0563 || ST06-R02 (ADH-02) | medium | release-blocker | same-todo | Navigation corrected; await body/handler completion and prove same-text draft fence catches removal | open; round2 remediation | implementation-round-1-resolution.md; existing D10 approval |
0564 || ST06-R03 (SEC-02) | medium | release-blocker | same-todo | D04/05 Evolution empty object is not ACK; key:{} preserved | resolved in round2 snapshot; finalvalidation pending | implementation-round-1-resolution.md; existing D04/05 approval |
0565 || ST06-R04 (SEC-03) | medium | release-blocker | same-todo | Denied mutations/twoTENANT proof added; preDispatch must exercise real Meta/Evo adapters and detect omitted callback | open; round2 remediation | implementation-round-1-resolution.md; existing scope/validation approval |
0566 || ST06-R05 (adherence-round2 ADH-R2-01) | medium | release-blocker | same-todo | D04 explicit false/malformed success flag contradicts positive ACK; UNKNOWN/no authoritative write | open; executor after runner terminal | implementation-round-2-resolution.md; D04 existing approval |
0567 |
0568 |
0569 |## TODO Closeout Disposition
0570 |- **Disposition:** keep-active
0571 |- **Disposition reason:** contrato aprovado, implementação e validação em execução; não encerrar antes de todos gates.
0572 |- **Post-commit/push status:** baseline materiala35f676c publicada/revisada; pacote documental finalizado com guardas pré-aprovação; produto Pending.
0573 |- **Next path/status action:** executar ST-CON-06 aprovado, manter active até evidências e gates de entrega.
0574 |
0575 |## Security Risk Assessment (Mandatory Before Delivery)
0576 |- **Risk level:** high
0577 |- **Why this risk level:** canal/credencial de múltiplos tenants e side effect externo.
0578 |- **Attack surface in scope:** sessão/key/bot, BU/channel/contexto, singleton/mapping forjado, rawerro/token, adapter recipient/URL e DI.
0579 |- **Attack simulation decision:** required
0580 |- **Review evidence:** planned após implementação, com actor sem grant/BU alheia/ingress falso/version stale e concorrência.
0581 |- **Residual security risk:** coorte privada atual preservada; nenhum usuário não confiável ou produção autorizado.
0582 |
0583 |## Performance & Concurrency Risk Assessment (Mandatory Before Delivery)
0584 |- **Policy schema version:** pcv-1
0585 |- **Global sensitivity level:** high
0586 |- **Why this level:** cutover de envio/identidade/aceitação/DI com concorrência real.
0587 |- **Current delivery stage at review time:** Pending
0588 |
0589 || Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
0590 || --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0591 || EPS | endpoint-performance-scrutiny | required | medium | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | pending | none | none |
0592 || FRC | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-E3 | pending | none | none |
0593 || BCI | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-E3 | pending | external ambiguity explicit | none |
0594 || RLS | runtime-load-stress-validation | recommended | medium | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E1 | pending | none | none |
0595 |
0596 |### Lane Detail Packet Template
0597 |#### EPS
0598 |- **Trigger rationale:** medir seleção/resolução scoped e projections de disponibilidade; EXPLAIN ANALYZE e cardinalidade representativa. Nenhuma chamada externa nova em GET e um POST por dispatch.
0599 |- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
0600 |- **Executor ID:** planned-executor-st-con-06
0601 |- **Evidence object:** pending; JSON pcv-1 com sha256 antes da entrega, não existe execução ainda.
0602 |#### FRC
0603 |- **Trigger rationale:** envio/erro e troca BU/conversa; draft, requests e readback BFF real.
0604 |- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
0605 |- **Executor ID:** planned-executor-st-con-06
0606 |- **Evidence object:** pending; JSON pcv-1 com sha256.
0607 |#### BCI
0608 |- **Trigger rationale:** barreiras PG/contador HTTP de BUs/credencial/identidade/claim/eco; provar D02..07 e ausência de retry. Crash recovery durável novo não é contratado.
0609 |- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
0610 |- **Executor ID:** planned-executor-st-con-06
0611 |- **Evidence object:** pending; JSON pcv-1 com sha256.
0612 |#### RLS
0613 |- **Trigger rationale:** ensaio bounded de concorrência no envio fake/PG, sem claim SLO/produção.
0614 |- **Recorded at (UTC):** pending; planning only, record real UTC with execution evidence
0615 |- **Executor ID:** planned-executor-st-con-06
0616 |- **Evidence object:** pending; resolver recomendação com evidência ou waiver válido até o deadline, sem deixar pendente na entrega.
0617 |
0618 |## Verification Debt Assessment (Required Before `Completed`; mandatory audit for `medium|big` or when debt signals exist)
0619 |- **Audit outcome:** high
0620 |- **Why this outcome:** não implementado; toda evidência de produto pendente, sem claim de entrega.
0621 |- **Inline code TODO debt:** none
0622 |- **Evidence / audit artifact:** planned após implementação
0623 |- **Accepted residual debt:** none; dependência externa não é waiver.
0624 |
0625 |## Independent Test Quality Audit Gate (Deterministic Floor From Audit Escalation)
0626 |- **Audit decision:** required
0627 |- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
0628 |- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
0629 |- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
0630 |- **Required evidence matrix (when architectural):** unit|integration|web real-backend
0631 |- **Package mode:** bounded-file-set
0632 |- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
0633 |- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
0634 |- **Canonical method:** wf-docker-independent-test-quality-audit-method
0635 |- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
0636 |- **Audit session / round evidence (when protocol used):** planned após implementação
0637 |- **Audit status:** not_run
0638 |- **Findings summary:** none; nenhuma auditoria de entrega executada
0639 |- **Evidence / reference:** planned após implementação
0640 |- **Waiver authority / reference (required if waived):** n/a
0641 |
0642 |## Independent No-Context Final Review Gate (Deterministic Floor From Audit Escalation)
0643 |- **Final review decision:** required
0644 |- **Why this decision:** big, contrato/API/schema/auth e fluxo crítico.
0645 |- **Trigger signals in scope:** architectural change|shared contract/api/schema|critical-user-journey
0646 |- **Impact signals in scope:** cross-module blast radius|public contract/schema/api|auth/payment
0647 |- **Required evidence matrix (when architectural):** unit|integration|web real-backend
0648 |- **Package mode:** bounded-file-set
0649 |- **Package minimum contents:** baseline aprovado, diff público limitado, evidência por critério, aderência e riscos.
0650 |- **Internal reviewer mandate:** required, fresh internal no-context reviewer, não executor; aguardar terminal.
0651 |- **Canonical method:** wf-docker-independent-final-review-method
0652 |- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
0653 |- **Audit session / round evidence (when protocol used):** planned após implementação
0654 |- **Final review status:** not_run
0655 |- **Findings summary:** none; nenhuma auditoria de entrega executada
0656 |- **Evidence / reference:** planned após implementação
0657 |- **Waiver authority / reference (required if waived):** n/a
0658 |
0659 |## Independent Cutover Integrity Audit Gate
0660 |- **Cutover audit decision:** required
0661 |- **Why this decision:** migra todos senders comuns para owner/port canônicos e elimina dispatch antigo, mantendo protocolos legítimos separados.
0662 |- **Cutover signals in scope:** intentional canonical boundary change|shared dispatch replacement
0663 |- **Package mode:** bounded-file-set
0664 |- **Canonical multi-lane audit protocol (when used):** audit-protocol-triple-review
0665 |- **Cutover audit status:** not_run
0666 |- **Findings summary:** planned after implementation
0667 |- **Evidence / reference:** harness D09 e módulos/sources consolidados, sem shim temporário
0668 |- **Waiver authority / reference (required if waived):** n/a
0669 |
0670 |## Delivery Confidence Gate (Required for `✅ Production-Ready`)
0671 |Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.
0672 |
0673 |## Module Consolidation Gate (Required Before `Completed`)
0674 |Planejado para o gate de entrega após APROVADO; nenhum resultado de implementação reivindicado.
0675 |
0676 |## Commands (Run Locally)
0677 |Guardas de planejamento após freeze. Produto somente após APROVADO: bash scripts/test-channels-local.sh all, depois do boundary positivo. Nenhum teste/runtime/account call nesta preparação.
0678 |
0679 |## Files Expected (Compatibility Note)
0680 |Diff Expectation Contract governa os paths, sem autorização de mudanças além dele.
0681 |
0682 |## COMENTÁRIO:
0683 |Nenhuma pergunta de produto material pendente.
0684 |
0685 |
0686 |## Producer / Consumer Contract Matrix
0687 |
0688 || Producer | Consumers | Auth / fields | Planned effect / constraint |
0689 || --- | --- | --- | --- |
0690 || Channel.sendMessage internal | OutboundService | opaque recipientRef/text; operation-bound implementation, no raw token | normalized result D04; one external POST, no retry, no DB message write by adapter |
0691 || ChannelResolver internal | OutboundService/policy | trusted reference derived from authorized session/API-key conversation or verified bot ingress; owner DB rechecked | Channel plus safe storage-provenance binding; no caller provider selection/secret |
0692 || GET /api/bff/conversations/:id/messages | Inbox | existing session/BU lookup, timeline fields unchanged; janela adds disponivel/motivo | observational availability, no external calls/secret decrypt; unavailable composer with fixed reason |
0693 || POST /api/bff/conversations/:id/messages | Inbox | existing session/CSRF/ATENDENTE+ and {texto}; success201 existing {id,canal,em} | shared outbound; D05 errors additive outcome, honest text; preserve draft and no auto resend |
0694 || GET /api/v1/conversations | public API clients | existing partner key scope; existing fields, adds envio_disponivel/motivo_indisponibilidade | existing window values remain, unavailable selection returns false/null rather than failing whole list |
0695 || GET /api/v1/conversations/:telefone/messages | public API client | existing partner key/BU and phone conversation lookup; timeline/window fields unchanged | disponibilidade aditiva como listagem, sem provider GET/segredo |
0696 || POST /api/v1/messages | public API client | existing API key/account_id, telefone/texto/atendente and rate limit | request shape/success unchanged; same shared outbound, source authorization and EXTERNO authorship; D05 error mapping |
0697 || IncomingService Typebot text response | existing bot sessions | accepted ingress exact channel/identity/tenant, no fabricated human user | same shared outbound/window/result/acceptance; preserve queue/status/human owner, stop on unknown/block/refusal, no replay |
0698 |
0699 |**Fixed availability reasons:** CANAL_AUSENTE, CANAL_AMBIGUO, CANAL_SELECIONADO_INDISPONIVEL, CHANNEL_IDENTITY_NOT_VERIFIED, CHANNEL_NOT_READY, PENDING_CREDENTIAL, JANELA_FECHADA; null when observed available. Availability never grants authority or guarantees external delivery. Existing input limit4096/request phone normalization stays at current product boundaries; the Channel port has no universal WhatsApp address requirement. No new public route or channel choice field is introduced in06.
0700 |
0701 |## Planning references / provenance
0702 |
0703 |Direction and extension requirements are explicit user statements2026-10-20. Initial framing opinion is artifacts/analysis/leadshug-channel-abstraction-framing-opinion-20261020.md (advisory only). Primary conceptual sources: NestJS custom providers https://docs.nestjs.com/fundamentals/custom-providers and Liskov/Wing1994 https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf, previously consulted. Provider error source consulted by owner (bounded public reference; reviewer independently hit429): https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes/. Local code proves current behavior, not future platform integration or live readiness.
0704 |
0705 |## Execution Checkpoints
0706 |
0707 || Checkpoint | State | Evidence / limit |
0708 || --- | --- | --- |
0709 || CP01 — runner antes de testes | passed precondition | artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/runner-checkpoint.json; allowlist antes de stat, sem varredura ampla; bash-n/diffcheck/mock config-only. Nenhum teste de produto ou Docker real executado neste checkpoint. |
0710 || CP02 — Channel/outbound/consumers + Web/tests | implementation, not delivered | Executor único; artifacts/tmp/stcon06-executor-* e evidence/executor-validation.json reservados. Initial RED dependencyguard175pass/1fail. all33610 terminal0:194unit/308PG/29Web/50browser, snapshot anterior agora insuficiente pelas findings round2. |
0711 || CP03 — independent adherence/security rounds1/2 | terminal,3 blockers open | Original R01/R03 counterexamples corrected. R05 success:false contradiction; R02 browser handler completion; R04 shippingadapter callback protection. Full implementation-round-1/2-resolution.md; no waiver/debt or physicalproof. |
0712 || CP04 — actual R05 regression RED | reproduced before fix | Canonical API49493 terminal1: Meta200 success:false+ID expectedUNKNOWN/TRANSPORT_UNCONFIRMED, actualACCEPTED;20otherunitfiles green. Executor will preserve exact log/provenance and correct source after terminal. Not blanket RED for other cases. |
0713 |
0714 |## Supplemental Expected-Path Validation — 2026-10-20
0715 |
0716 |User explicitly replied **“Validar os dois arquivos de apoio”** to the exact bounded proposal [test-companion-path-admission.md](../../../artifacts/reviews/leadshug-channel-abstraction-20261020/test-companion-path-admission.md). This validates only Web `src/api.spec.ts` and `e2e/timeline-freshness.ts` as M companions for D10/SCOPE05. Scope, DoD, public behavior, frozen D01..10, private-data prohibition and required checks are unchanged. The direct client test was already added before the path omission was noticed; its admission is explicit here. The nested helper correction was not applied or run before this validation. Executor remains sole product writer; browser/all may proceed only after both freshness inventories use positive pathspecs before discovery.
0717 |
0718 |## Implementation Assurance — Round 1
0719 |
0720 |Architecture adherence and separate security reviews completed through canonical subagent_review_run.py, gpt-6.1-sol/xhigh, closed embedded source packages; strict merge passed. Architecture: changes required; security: source-only classification defects and evidence gaps, no demonstrated tenant breakout or credential disclosure. Artifacts: evidence/adherence.raw.json, adherence.merge.json; security.raw.json, security.merge.json. Reviews did not certify final all or physical proof. No live review was cancelled or repackaged. All findings integrated as approved-contract remediation, with delivery still Pending.
0721 |
0722 || Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
0723 || --- | --- | --- | --- | --- | --- | --- |
0724 || ADH-01 | Integrated | useful | yes | project | n/a | ST06-R01; D04 complete-envelope classification, remediation open |
0725 || SEC-01 | Integrated | useful | yes | project | n/a | duplicate ADH-01 consolidated ST06-R01; same open blocker, not ignored |
0726 || ADH-02 | Integrated | useful | partial | project | n/a | ST06-R02; independently confirms browser navigation defect, remediation open |
0727 || SEC-02 | Integrated | useful | yes | project | n/a | ST06-R03; supported ACK structure vs malformed empty object, remediation open |
0728 || SEC-03 | Integrated | useful | yes | project | n/a | ST06-R04; reconcile source/proofs and add only missing local negative/isolation cases |
0729 |
0730 |
0731 |## Implementation Assurance — Round 2
0732 |
0733 |Both canonical CLI reviews terminal0, strict merge passed: evidence/adherence-round2.raw.json and security-round2.raw.json. Full adjudication and exact overlapping ID bindings: implementation-round-2-resolution.md. Original R01/R03 counterexamples resolved at source; R02/R04 protection gaps remain and R05 is a new classifier case. No architecture expansion, waiver/debt or delivery claim. Runner33610 must terminate before further product edits.
0734 |
0735 || Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
0736 || --- | --- | --- | --- | --- | --- | --- |
0737 || adherence-round2:ADH-R2-01 | Integrated | useful | yes | project | n/a | ST06-R05 Meta success:false contradiction; approved D04 remediation open |
0738 || adherence-round2:ADH-R2-02 | Integrated | useful | partial | project | n/a | ST06-R02 headers-only wait can falsely pass before stale completion |
0739 || adherence-round2:ADH-R2-03 | Integrated | useful | yes | project | n/a | ST06-R04 testfake owns guard, must exercise shipping adapter callback |
0740 || security-round2:ADH-R2-01 | Integrated | useful | yes | project | n/a | duplicate ST06-R04, same shipping-adapter harness gap |
0741 || security-round2:ADH-R2-02 | Integrated | useful | partial | project | n/a | duplicate ST06-R02, same browser completion gap |
```
