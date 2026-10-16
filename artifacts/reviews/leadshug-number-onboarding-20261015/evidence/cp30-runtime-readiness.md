# cp30 runtime readiness

The approved origin correction is active at `https://operating-brussels-internship-interviews.trycloudflare.com`. Only `CHANNELS_LOCAL_ORIGIN` changed in the private testing environment file. The saved production mode, blank `PUBLIC_ORIGIN`, four Meta values, owner and other protected values, all remaining file bytes, and file ACL were preserved. The API was recreated without a build; it is healthy and uses the same validated image ID. Other owned containers and all five project volumes remained unchanged.

HTTPS root and health endpoints returned 200 from WSL and Windows. One normal owner login returned 200; `/me` returned 200. The ephemeral session cookie was Secure, HttpOnly, SameSite=Lax, and host-only. Exact-origin CORS preflight returned 204 with credentials allowed.

Readiness remains gated by the live tenant state. `/me` reports onboarding pending; the onboarding endpoint returns 200 with `complete=false` and one offered module. Registration capabilities and business units both return 409 `ONBOARDING_PENDENTE`. Therefore business-unit count and modalities were not observable, and neither official nor unofficial registration availability is established. The installation-level unofficial ceiling is enabled, while the tenant's offered unofficial module is disabled. No module, billing, business-unit, provider, OAuth, QR, or number action was performed.

The user previously confirmed that Meta messages are subscribed and the initial wizard was completed, but the current application reports the wizard incomplete. The next supported step is to reconcile the existing OWNER “Configuração inicial” wizard in the application UI, then re-check readiness through the product flow. Do not bypass the gate or begin number registration before it clears.

Source heads at handoff: root `4bccdc4aa470d1166bc14a681d0008f242db2562`, API `f134bd11449a553e6f57e66cdc8fc71032151060`, and Web `d33c82c26760c671d98cab6f3e7bfe5676122c69`. No product source was changed or built in cp30. Credentials, secret values or hashes, raw responses/logs, and the session cookie were not persisted.
