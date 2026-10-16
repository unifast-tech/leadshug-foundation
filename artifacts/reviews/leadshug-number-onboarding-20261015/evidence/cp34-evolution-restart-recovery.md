# cp34 Evolution restart recovery

With explicit human approval, the owned Evolution container was stopped and restarted in place. The exact container ID, Compose project/service, pinned Evolution image, and mounted instances volume were verified before the interruption. The same container ID returned to `running` after 5.59 seconds. The other six owned containers and all five project volumes kept the same identities and states. HTTPS gateway root and API health remained 200 during the stop.

The authenticated business-unit read while Evolution was stopped still showed persisted `CONECTADO`/`CONNECTED` and a verified receipt. That was last-known application state, not live provider health. After restart, the read-only database snapshot at `2026-10-16T18:40:18.033Z` retained one unofficial channel, matching pairing and verified epochs, one exact current identity mapping, the verified receipt, and the prior one-IN/one-OUT exchange in the same conversation.

The channel then reported `CONECTANDO`/`CONNECTING` with `connected=false`, despite the retained `CONNECTED` attempt and verified receipt. Three bounded authenticated reads through `2026-10-16T18:41:06.982257Z` remained in that state. The Evolution container is running, but live channel recovery is not confirmed. No provider verification call, QR operation, re-pairing, new message, or app mutation was performed.
