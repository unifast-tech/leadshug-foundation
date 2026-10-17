# cp49 API activation

The accepted cp36i API candidate is active in the owned `leadshug_channels_local` project as container `c138a8456bc834d53c2ab4c3bc3c0307024dbc5a9cbb9a11c337218adcde7324` (image `sha256:fe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821`). API source is `7e948c3045da736f7db1f8e97825cf6384777e4f`; Web source is `34408c47b4f2f935291d5fc9934f5118b5516bd4`; manifest is `af21e98e41ec1ba86f4dac877ba2bd69b3ff0857fba930ca1c3973428723b581`.

The unique public origin setting was updated in place with a guarded byte-preserving change; the old value was held only in memory and is omitted. File mode 0777 remained intact. The API is healthy in production mode with the verified public origin. Local and public root/health return 200, and the served asset hash matches the known Web bundle. All four compiled API module hashes match the accepted candidate. Normal OWNER login, onboarding, unofficial capability, and business-unit readiness succeeded.

One pre-restart ADMIN verify returned `PENDING_RECEIPT`; this operation result was reconciled against scoped canonical state, which showed the same completed attempt/version, matching pairing and verified epochs, receipt, fresh `connectedAt`, connected provider state, current mapped owner identity, and no active lease. The other six containers, five volumes, and source/config state were preserved.

This is a conditional private unofficial checkpoint only. Official onboarding and overall delivery remain blocked by FINAL-CP36I-01. See [cp49 unofficial recovery](cp49-unofficial-recovery.md).
