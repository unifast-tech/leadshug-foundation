# cp36d pre-mapper RED

Canonical command: `bash scripts/test-channels-local.sh api`. Full stdout/stderr is preserved in `cp36d-api-recovery-red-full.log`; runner exited 1. Source hashes at that execution are in `cp36d-red-before-fix.sha256`.

The real BFF/Nest/PostgreSQL verify request received the existing typed `MetaIndisponivelError` through the test provider port. Before the production mapper, the observed response summary was `{status: 500, catalogCode: null}`, against the regression's expected `{status: 503, catalogCode: "META_INDISPONIVEL"}`. The API run had 141 unit tests pass and 287 of 288 PostgreSQL E2E tests pass; the one failure was this expected pre-fix assertion. This proves the BFF boundary's generic 500 for the typed provider error. It does not claim an external Meta request or a captured provider error body.

After this RED run, the BFF regression was strengthened to produce the typed error through `MetaFake.verificarNumeroVinculado`'s bounded loop using exactly two scoped page responses and to assert WABA/token/cursor arguments. That strengthened seam was not separately executed as pre-fix RED; it is covered in the single final all run. The existing Meta adapter unit tests separately assert the exact `META_INDISPONIVEL` code for over-budget, repeated, and oversized cursors.
