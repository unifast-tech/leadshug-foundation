# CP64 v9 policy activation receipt

The single authorized v9 helper invocation exited 0 and returned `success_exact_policy_and_regression_probes_passed`. It reports API container `005529386c8a7ab499cd779942ce541bb90cd3a770b8436b41509d2655e54857` on unchanged image `fe5fb7…`, Web container `9aa55b6681a8480dbfd7cbf2a51ab8571035603b288b52e6798d93741af01093` on candidate `sha256:cfd5e58b91a67d2fae4f37759274a34209cd2501082650a49545a60a12642361`, exact public policy response 200/12,865 bytes/SHA `d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d`, root and health 200, known JS SHA `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd`, and preserved containers/volumes. The new rollback tag `leadshug_channels_local-web-rollback:cp64-prenotransform` was preserved. There was no retry.

Separate Windows and WSL normal-TLS probes to `addressing-mar-perform-hormone.trycloudflare.com` both returned policy 200, 12,865 bytes, exact source SHA, UTF-8 `text/html`, `Cache-Control: no-store, no-transform`, no redirect or Set-Cookie, zero Cloudflare email markers, zero script tags and zero forms. Both also returned root and health 200 and the expected JS SHA `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd`. Full safe per-path facts are in the JSON.

A bounded read-only API Node check emitted only `production=true|webOriginMatches=true` for the expected public origin. The helper’s success path confirms all seven owned service containers and five volumes remained guarded; no gateway 502 recovery stage was entered. The stage receipt ended at `complete/success`; no receipt write failure was recorded.

The opaque origin update emitted no prior or other environment values. No provider, Meta, database, volume, or source/Git action was performed by this executor. Root’s independent HTTPS verification was still pending when this receipt was written.

Terminal stdout SHA-256 `44cce878127b586b1936c37f775edfbf5b52d435ae8d05978f1cc1dfa33db294`, exit-code receipt SHA-256 `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`, and stage receipt SHA-256 `8f6b60098e88ebc0ce48fad904f5fb2eafcb455d902dd91b0d9d5dd495e6a614`.
