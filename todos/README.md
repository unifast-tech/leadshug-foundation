# LeadsHug TODOs

Tactical TODOs are live execution contracts. Candidate ideas belong in [the backlog](../backlog/README.md), never in `todos/active/backlog/`.

Every development slice requires a TODO created from the governed engineering TODO template. A file in `todos/active/` can be `Draft`, `Review`, `Approved`, or `In-Progress`, but placement alone never authorizes implementation. Execution requires explicit `APROVADO` and an authority guard result of `go`.

Use `todos/active/features/` for capabilities and `todos/active/bugs-performance/<severity>/` for bugs and performance. Closed TODOs belong in `todos/completed/` and require Definition of Done, specific validations, evidence, and their governed closeout disposition. State schemas and transitions are defined by [the evolution lifecycle](../evolution_lifecycle.md).
