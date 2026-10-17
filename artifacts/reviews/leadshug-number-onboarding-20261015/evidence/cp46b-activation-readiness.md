# cp46b activation readiness (read-only)

Captured the owned `leadshug_channels_local` runtime for possible later API-only activation. The exact seven container IDs/images and five local volume identities still match cp38; all seven containers were running. The API remains image tag `leadshug_channels_local-api`, digest `sha256:c2e8d62bde2c85305deb9d72569f773072e77292465e09ed7283051b40ed4f4f`.

The selected API's Compose labels identify the two project files, working directory, project `leadshug_channels_local`, service `api`, and owner `number-onboarding`. No `Config.Env` dump was used. A read-only Node script on that exact API container read only the allowlisted public fields: `NODE_ENV=production`, `WEB_ORIGIN` still matches the previous accepted tunnel origin and not cp46's hostname, `PUBLIC_ORIGIN` is blank, and `EVOLUTION_WEBHOOK_URL` matches the expected internal `http://api:3000/webhooks/evolution` address, not either public tunnel origin. Thus Evolution callback routing is internal and should not be conflated with the public web-origin mismatch.

`docker/local-gateway.conf.template` routes API/webhook paths to the static Compose service name `api:3000`; web paths go to `web:80`. Only if a future API-only recreate changes the API IP and the owned gateway then shows a stale-upstream 502 is a graceful reload of that same owned gateway a candidate. No reload or other action was performed.

This checkpoint is metadata only. It does not activate the new hostname for the API, alter any origin/token, restart services, or establish Meta/WhatsApp recovery. The tunnel and all runtime objects were left unchanged.
