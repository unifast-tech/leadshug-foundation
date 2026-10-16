# cp38 read-only preflight

Captured at 2026-10-16 20:19:56 UTC while source/runtime updates remain gated on fresh review. The current HTTPS root and `/health` both returned HTTP 200 from WSL; Windows fallback was not needed. The served JavaScript returned HTTP 200 and SHA-256 `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd`, matching the previously accepted bundle.

All seven `leadshug_channels_local` containers are running with the same IDs and images as cp37. All five expected local volumes are present with unchanged project and logical-volume identities. The API remains on its prior validated image; this is a preservation observation, not evidence that the newly tested source fixes are served. Runtime config was checked only in memory for booleans: production mode and exact current HTTPS origin match, four Meta fields are present, and sensitive value/hash data was not persisted.

No login, database, provider, source, configuration, build, recreate, or restart actions were performed. This preflight does not accept or validate the new runtime; it records readiness for a later, separately authorized API-only update.
