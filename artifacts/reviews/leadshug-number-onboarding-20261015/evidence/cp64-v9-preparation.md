# CP64 v9 activation helper preparation

This is a copy of the accepted v8 activation helper with literal identity, tag, and stage-file repins only. It is prepared for independent review; it has no execution authority and was not run.

The baseline API pin is current API container `f86d76…` on the same accepted API image. The baseline Web pin is current provisional container `fe783b…` on existing image `6f4b2500…`. The new candidate is `cfd5e58b…` at tag `leadshug-channels-web-candidate:cp64-notransform-0cdafce3f985`; the new rollback tag `leadshug_channels_local-web-rollback:cp64-prenotransform` is reserved to preserve the currently active `6f4b2500…` image. The existing `cp63-preprivacy` rollback tag remains untouched. A distinct stage receipt path prevents overwriting v8 evidence.

The v8 source hash is `01e198a7818b51fe447f46923f38b95d159e05aaeda4f3cdf27ae438f80b05b1` and the v9 helper hash is `c783032964e9ec9e8c83ac450df592c7859a3b71eec5eeb3f9ef8eb0d154a95b`. The JSON artifact carries the complete line diff proving only the listed pin values changed. No origin/private file access or runtime mutation occurred during this preparation. Candidate build and direct-probe evidence is `8070af367588d6e9d1381fd8b6467324883f3bc560b52881f58440e57341ac50`.

Await fresh root review and a separate operation GO before any v9 execution.
