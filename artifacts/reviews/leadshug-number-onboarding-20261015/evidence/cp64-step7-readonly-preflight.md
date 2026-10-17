# cp64 step 7 read-only preflight

Observed at 2026-10-17T13:43:38.349843+00:00. This is a pre-activation snapshot; no origin or runtime mutation occurred.

The accepted transport currently answers with normal TLS at `addressing-mar-perform-hormone.trycloudflare.com`: `/` and `/health` return 200, and the served JS hash remains `d1434360…6ff4bd`.

The owned project still has the same seven running containers and five expected volumes, cross-referenced to root's preservation receipt (`root-cp64-phase1-preservation.json`, SHA-256 `db55921245c61e25385c3549c2805262426bcab869690f26b74bf373575aa80e`). API, Web and gateway are on owned network ID `d48c8a9a…36925c20` with IPs `172.27.0.5`, `172.27.0.4`, and `172.27.0.2`. The gateway's active managed config SHA-256 is `9329131376e0aaa8020e7440954af5125a65eb2bba69fd016292fe63843fe707`, identical to the public template SHA.

One direct metadata-only probe from the exact API container saw API `/health` 200, direct gateway `/health` 200, and direct gateway policy path 200. The old Web policy path currently returns 200 with 694 bytes, which does not equal the accepted 12,865-byte policy. This is expected before candidate activation and does not establish an activation defect. No response content was persisted.

The v6 helper is parser-clean and its pure causal predicate passed two positive cases plus nine negative cases (same IP, network/gateway/config/owner/backend-image drift, wrong policy hash, non-502, and unsupported route). The tests made no Docker or network calls. v6 remains unexecuted beyond its plan-only mode; no gateway reload, private-origin access, or API/Web mutation took place.

The JSON records the selected metadata, boundaries and hashes. This evidence is not operation authority; fresh independent review and root GO are still required.
