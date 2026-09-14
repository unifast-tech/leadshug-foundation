# LeadsHug Web Boundary Policy
**Version:** 1.0

LeadsHug is a web-first operational system. There is no app-promotion or anonymous public discovery contract in
the current product boundary.

- The React web client is an authenticated operational surface.
- Login, session handling and authorization are backend-owned contracts.
- Unauthenticated requests must receive deterministic authentication errors or the documented login response.
- The web client must not implement privileged actions locally or bypass BFF permissions.
- Any future mobile/app surface requires a new TODO, module contract and explicit constitutional decision.
