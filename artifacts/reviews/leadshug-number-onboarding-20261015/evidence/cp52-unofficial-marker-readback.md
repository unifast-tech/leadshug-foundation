# cp52 unofficial marker readback

The user clarified the outbound text as “Teste resposta” and that the new-contact conversation is the intended subject. This explains why cp51’s different suggested marker had no match; cp51 remains unchanged.

The public Prisma schema defines `Message.content` as a string, and the Evolution mapper passes message text into that field. Using server-side exact equality on the user-supplied marker, restricted to the known BU, current managed provider identity, and messages after the 2026-10-17 04:13:01.849 UTC restart time, found one outbound match. That uniquely identified new conversation `efcd1776-3282-4cb0-a073-942a636719ae`, distinct from the old cp33 conversation.

A second read was restricted to that exact new conversation, BU, identity, and post-restart window. It found one inbound (`RECEBIDA`) and one outbound (`ENVIADA`) message in the same conversation. Only opaque message/conversation IDs, direction/status/timestamps, channel origin, author-presence expectation, and external-ID presence were selected. Content was not selected or returned.

The accepted API image and compiled module hashes, connected channel, attempt v2, generation/epochs 1, receipt, current identity mapping, and no-lease guards remain valid; the same Evolution container is running. Human visibility and delivery remain separately confirmed by the user and are not inferred from counts. Terminal STOP; root owns canon/Git.
