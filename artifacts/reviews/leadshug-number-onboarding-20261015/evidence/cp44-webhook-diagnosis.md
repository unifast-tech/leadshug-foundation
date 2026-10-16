# cp44 webhook verification diagnosis

Captured 2026-10-16T22:32:17Z.

The controller contract is `GET /webhooks/meta`: it returns the challenge only when mode is `subscribe` and the supplied verification token equals the runtime token; otherwise it returns 403. The canonical dotenv field and the process value in the guarded API container were present and equal, checked in memory only.

Local gateway synthetic checks: valid challenge returned 200 and matched; invalid and absent token each returned 403.

The public hostname did not resolve from WSL (`EAI_NONAME`) or Windows (`ENOTFOUND`), so the public valid, invalid, and absent-token requests were not reached. This is a transport/DNS limitation, not evidence of token rejection.

The gateway access format omits request target, query, headers, and body. No raw response, URL/query, secret value/hash, application logs, or tunnel logs were persisted/read. No source, private configuration, runtime, tunnel, provider, or database mutation occurred.
