# cp61 official inbound diagnosis

The owned API container/image and the fixed public `/health` endpoint passed. A single scoped snapshot of the exact official BU/channel/current attempt shows `SUBSCRIBED`, attempt `PENDING_RECEIPT` at stage `SUBSCRIBED` v7, identity verified, active credential and current managed mapping present, but no receipt or connected timestamp and no active lease.

No message rows exist for the exact current provider identity in the admitted post-baseline window. The bounded direction/status group is empty. A separate aggregate found zero `meta.webhook` events for this BU, official channel type, and time window. `WebhookEvent` has no provider identity/resource column, so that aggregate cannot be attributed to this exact resource. No payload was read.

The sender’s reported two checks are human evidence; this readback does not infer delivery from them. The possible upstream Meta app-publication restriction remains an unverified hypothesis. No route-specific gateway request count was collected or claimed. Terminal STOP; no polling or provider action.
