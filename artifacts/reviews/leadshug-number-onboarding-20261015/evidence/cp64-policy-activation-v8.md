# cp64 v8 policy activation result

The frozen v8 helper was invoked once under the hash-bound root GO. It exited **2** with `failed_then_rollback_verified`. At `web_recreate`, the public policy endpoint returned HTTP 200 but its response bytes did not match the accepted policy artifact (`privacy_response_bytes_mismatch`). Public policy activation is therefore **not established**.

The helper reports API rollback to the same image and old origin verified, Web rollback verified, preserved resources verified, and origin bytes/security metadata restored. No gateway reload or recreation, provider/DB/volume action, or incomplete origin transaction was reported. No second attempt was made.

- Helper SHA-256: `01e198a7818b51fe447f46923f38b95d159e05aaeda4f3cdf27ae438f80b05b1`
- GO proof SHA-256: `a3804997d6711d8422d8049afc167de39bccb824b197450f5581d70d66422328`
- Stage receipt: `cp64-activation-stage-v8.json` (SHA-256 `1bfc417fa45a70383206a0b60110cc0a79452db6c766a45698fb8555f78638ce`)
- Safe terminal record: `cp64-policy-activation-v8.json`

Stopped after the guarded failure and verified rollback. Root should independently inspect the public result; this execution does not establish policy publication.
