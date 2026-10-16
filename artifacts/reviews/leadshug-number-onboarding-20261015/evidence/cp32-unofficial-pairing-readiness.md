# cp32 unofficial pairing readiness

The authenticated owner account is onboarding-complete, the unofficial module is enabled, and both registration capabilities report `AVAILABLE`. The account has one business unit and one `NAO_OFICIAL` channel.

The read-only readiness sequence began at `2026-10-16T18:32:30.924785Z`, before the human test request. The database query ran during that sequence; a statement-level timestamp was not separately recorded. It confirms `ownNumberVerified=true`, `pairingEpoch=verifiedEpoch=1`, and a current attempt whose generation and pairing epoch match. The provider state is `CONNECTED`; the channel remains `CONECTANDO`, with receipt not yet verified and `connected=false`. There is exactly one active owned identity mapping, and its current provider identity matches the current channel mapping. No identity, phone, instance, or resource identifier was retained.

At that same pre-request baseline, this business unit had zero conversations, zero unofficial inbound messages, and zero unofficial outbound messages. Counts were read by business-unit scope and channel origin only; no content or external identifiers were selected or persisted.

The fresh runtime check was captured at `2026-10-16T18:32:43.248856Z`, after the human synthetic-test request had been sent; its timing is recorded as post-request. HTTPS root and health returned 200. The served bundle and the Web container asset matched the cp27-accepted SHA-256 `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd`. Source heads and validated API/Web image IDs are recorded in the JSON artifact.

No provider call, QR access, OAuth, pairing, registration, or application mutation was performed by the agent. The human can send one synthetic inbound message from the other test WhatsApp account, confirm it in the expected UI, and only then send one synthetic outbound reply.
