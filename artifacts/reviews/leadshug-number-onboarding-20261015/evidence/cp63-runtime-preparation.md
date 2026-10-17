# cp63 runtime preparation

The owned project currently has all seven containers running and all five expected project volumes. API remains image `sha256:fe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821`; current Web is `sha256:d11a882849dc806e0d4728ca90a8fc8655aebc77421acefac63054b4fbb89365`. Evolution, both PostgreSQL services, Redis, gateway, and their existing images/volumes were left unchanged.

The current public host passed normal-TLS root/health checks and served the existing JS bundle at the expected hash. A tunnel identity drift was observed: pinned child PID 21180 remains at its exact prior start time/hash and target, but pinned supervisor PID 22836 is absent. No process discovery or tunnel action was attempted. The public host currently works; root should adjudicate the owner/child continuity drift before activation.

The Web Dockerfile builds with `node:22-alpine` and serves from `nginx:alpine`. Both base images are locally present with the recorded IDs/digests. BuildKit cache is available in aggregate (30.93 GB); exact Web-layer reuse is unverified. The draft HTML hash is `43556cf3b502b569d8ac79a116da3cb7f3910ff7a444f52035ae1fcbdfe259f8`; the intended `web-app/public/privacidade.html` source is not present yet.

The JSON records the candidate build, old-image preservation, Web-only Compose recreation, rollback, and no-session public probe commands. The plan preserves API, Evolution, gateway, databases, cache, tunnel, and volumes. Material risks are the missing tunnel supervisor, mutable Docker base tags, unknown exact cache reuse, and the gateway’s static `proxy_pass http://web:80` resolution, which may become stale if Web IP changes. If public probes fail after a future Web recreation, stop; do not reload the gateway or touch other services without separate adjudication.

No candidate was built or tagged, and no container/runtime/config/source change occurred. STOP pending independent critique acceptance and root activation.
