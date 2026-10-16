# cp33 unofficial message readback

The owner reports that the synthetic inbound message appeared in Atendimento and the synthetic outbound reply reached the other test device. The read-only database statement at `2026-10-16T18:37:51.745Z` found exactly one inbound and one outbound message for the current unofficial provider identity. Both belong to the same single conversation. The BU had one conversation total, up from the cp32 pre-test baseline of zero conversations, zero IN, and zero OUT.

The current channel is `CONECTADO`; provider state is `CONNECTED`. Own-number verification remains true with pairing and verified epochs both 1. The current attempt is `CONNECTED` at `RECEIPT_VERIFIED`, and exactly one active identity mapping matches the current channel. The receipt and connection timestamps are both `2026-10-16T18:34:04.872Z`. External IDs are present for both directions; outbound author metadata is present and inbound author metadata is absent. No message content, names, phone numbers, message IDs, resource IDs, or raw payloads were selected or retained.

The post-test HTTPS root and health checks returned 200. The served bundle and the Web container bundle still match the cp27-accepted SHA-256 `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd`. The unchanged source heads and validated API/Web image IDs are recorded in the JSON artifact.

This readback confirms the reported synthetic test path and receipt state only. It does not claim historical recovery, an official channel, or production readiness. No provider calls, verify actions, QR access, pairing, or message sends were performed by the agent.
