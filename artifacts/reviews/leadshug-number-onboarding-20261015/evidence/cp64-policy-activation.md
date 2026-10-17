# cp64 policy activation attempt

One authorized invocation of v7 `5e31094320fd2b45392a8436223517ac124d837062530190cab14adec8accb47` used operation GO `b0db632c7591722f18b620ee306974fb9e3dae7febff2a81ff27d6e9f243dd0c`. It exited 2 at `preflight_resources`, before the public-origin transaction or any API/Web/tag/gateway mutation. The first safe failure category is `docker_read_guard_failed` with native exit 1; Compose/API selection reached the known API ID, then Web selection was incomplete.

The stage receipt `9d7f04353d7d50c13bccc1bef75fe5dc872f28a944e6268084a48c836e23df26` records `originWriteOutcome=not_started`, API/Web mutation flags false, and no gateway reload. Terminal JSON reports `failed_rollback_incomplete_stop_for_root`; the incomplete label reflects that no Web postcondition was captured after the guard failure, not evidence that Web was changed. No retry or helper edit occurred.

Public policy activation is **not verified**. The accepted target policy is 12,865 bytes with SHA `d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d`; the only current readiness reference is the immediately preceding read-only preflight, which confirmed transport root/health/JS but not the activated policy.

This report preserves the safe terminal result and stage receipt. It does not claim successful publication or post-activation HTTP proof. Root should adjudicate the Compose read failure before authorizing any further invocation.
