# CP64 v9 read-only preflight, current process-bound host

This fresh snapshot is bound to v9 helper `c783032964e9ec9e8c83ac450df592c7859a3b71eec5eeb3f9ef8eb0d154a95b`. It is read-only; `rootAccepted=false` and operation authority remains pending.

All seven owned containers matched their exact IDs, images, running state, owner/project/service labels; API is healthy on the accepted API image. All seven share network `d48c8a9ac92f00d8e2f1c1c6a1744ab14463aeba4abeab491f82719336925c20` (`leadshug_channels_local_default`), and all five expected volumes are present. The running gateway config SHA `9329131376e0aaa8020e7440954af5125a65eb2bba69fd016292fe63843fe707` matches the public template. The API service tag resolves to the accepted API image; the Web service tag resolves to the currently active provisional image `6f4b2500…`; the v9 candidate tag resolves to `cfd5e58b…`. The new rollback tag is absent; the existing cp63 rollback tag still resolves to old image `d11a8828…`.

The exact native owner and child PIDs remain alive with matching native 100ns start ticks, executable paths/hashes, parent relation and full expected command lines. The current state file records `addressing-mar-perform-hormone.trycloudflare.com`, target `http://127.0.0.1:8083`, HTTP/2, one registration event, two error events, zero stream callback faults and zero state-write failures. Windows and WSL no-session normal-TLS requests to that exact process-bound hostname returned root, health and JS status 200 with no redirect or Set-Cookie; JS SHA matched `d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd`.

An earlier probe used the reported `comments-heart-gale-muscles.trycloudflare.com` hostname; it did not match the process state and failed DNS. This supplement corrects only that hostname binding. No tunnel or runtime change was made.

The first candidate probe's helper did not persist its generated container ID/name or `docker rm` exit code. A scoped current readback by its exact checkpoint label and name prefix found zero matching containers. This proves current absence only, not the historical removal result. The successful second probe's exact temporary container ID and cleanup result remain in the candidate artifact.

No private environment, `Config.Env`, provider, database, source, or runtime state was changed. All artifacts are readiness evidence only; no v9 activation is authorized by this report.
