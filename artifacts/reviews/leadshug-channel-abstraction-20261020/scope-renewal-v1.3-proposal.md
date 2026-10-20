# ST-CON-06 v1.3 — proposed bounded scope renewal

Status: planning proposal; **not approved and no schema/CI execution authorized**. The existing v1.2 authorization, including both explicitly admitted Web companions, remains the authority for already-approved work. New paths below require renewed human approval after affected planning review. Product push, deployment/promotion and gitlink edits remain excluded.

## Confirmed reason

PERF-01 is reproduced in real PostgreSQL by canonical API run15524: 194 unit pass, 309 E2E pass, 2 new E2E fail. Two conversations with 100 OUT rows each (one old IN, one no IN) produce 200 rows removed by direction filter across two index loops, 16 shared-hit/0 shared-read blocks. Existing `(conversation_id,created_at)` cannot directly seek the latest IN. A real list whose selected origin is non-window NAO_OFICIAL also queried latest-IN once because another BU binding requires a window. Full raw log `artifacts/tmp/stcon06-perf01-current-red-api-final.log`, SHA256 `8b2fc6510dafe4be8a10de73d150695a82a667bcb4255067e3b64da9b87ae248`.

The selection-only optimization and PERF-02 per-conversation readback remain inside v1.2 admitted source/tests. Five overlap waves now prove twenty per-owned-conversation counts of exactly one each; this is distinct conversations, not a guarantee of external exactly-once for repeated requests.

TQA-01 / CIADM-01: the current remote workflow has unit/build jobs but omits the PG/browser suite family changed by this story. Full `ci-equivalent-test-surface-admission` requires corresponding pipeline configuration and fail-closed drift protection in this same change. The fresh governance opinion sustains that part, while challenging the implication that a successful remote run or waiver is prerequisite to the approved local milestone. Configuration, local executable topology/parity, actual remote execution and later promotion remain separate evidence. No remote execution is claimed.

## Proposed exact additional paths

| Repository | Exact path | Change |
|---|---|---|
| api | `prisma/schema.prisma` | M: one `@@index` declaration only |
| api | `prisma/migrations/20261020170000_message_inbound_window_index/migration.sql` | A / ??: one CREATE INDEX |
| root | `.github/workflows/ci.yml` | M: add isolated channels validation job, retain existing jobs |
| root | `scripts/check-channels-ci-parity.py` | A / ??: bounded pipeline/lifecycle drift guard with meaningful synthetic-negative checks |

Already admitted `scripts/test-channels-local.sh` may gain the bounded Linux host transport below in addition to its authorized public-inventory repair. No additional Docker Compose, package/lockfile, API/Web production file paths are admitted by this renewal. Existing public-source inventory and private-config boundaries remain mandatory. Removal of blanket forbidden `api:prisma/**` is replaced by these two exact ExpectedPaths; all other Prisma changes remain unclassified and fail closed.

## One database index, no data-model expansion

Proposed schema addition inside `model Message`:

```prisma
@@index([conversationId, direction, createdAt, id], map: "messages_conversation_direction_created_id_idx")
```

Proposed complete new migration:

```sql
CREATE INDEX "messages_conversation_direction_created_id_idx"
ON "messages"("conversation_id", "direction", "created_at", "id");
```

The first two equality keys permit a backward index scan for `ORDER BY created_at DESC,id DESC LIMIT 1`, including no-IN results, without walking an OUT-only suffix. Both keys and the tie-breaker are existing fields. Preserve existing indexes/unique keys, all MessageAcceptance code, data, enums, authorization, identity/generation fences and response semantics. The latest-IN timestamp is still read from the entire preserved history without a transport filter; expired timestamps must remain observable. No 24h predicate shortcut, retention, backfill, reset, durable intent or new table/column.

A full Prisma-managed B-tree is preferred over an unmodeled partial index: it adds storage and write maintenance for every direction but keeps Prisma schema/migration ownership explicit. PostgreSQL planner choice and buffer work must be measured, not inferred from the index name. Migration can briefly block writes; apply only to the existing authorized local test database after the same migration passed on disposable PostgreSQL16. No production/Railway migration. Record migration status and retain original rows/channels/credentials. A failed local migration stops activation rather than resetting or dropping the database.

## Shared CI/local executable owner

Keep `bash scripts/test-channels-local.sh all` as the single broad command and the existing embedded `RUNNER_SCRIPT` as the single ordered leaf/lifecycle owner. The change is confined to host path/CLI transport selection, not separate duplicated CI suites:

- Default remains Windows Docker CLI + wslpath on this workstation. Explicit `CHANNELS_DOCKER_TRANSPORT=linux` selects Linux Docker CLI and absolute POSIX bind paths in the GitHub Ubuntu job. Reject unknown values. Reuse existing Compose files, positive public path list, fictitious config masks, container-image runtime, service names and collision refusal. Existing `_WINDOWS` variable names may remain compatibility names for Compose inputs; their values are transport-appropriate paths.
- Both transports use disposable `leadshug_channels_validation`, Node22.23.3-bookworm-slim, PostgreSQL16 and the same `RUNNER_SCRIPT`: prerequisites/OpenSSL, positive-binds/dotenv-mask/hash assertions before npm, npm ci for both apps, Prisma generate, API migrate/status/lint/build/unit/E2E, Web build/unit, migrations/status and Chromium install/browser. Keep fresh API/provider/production Web preview ports3100/3101/4173, no server reuse, served-versus-built artifact proof and full suites. Browser remains mutation against disposable fixtures on an approved non-main lane.
- Cleanup stays in the same wrapper with strict namespace collision refusal before creation. Preserve EXIT cleanup after success/failure; do not delete pre-existing resources or unrelated human services. Ensure shell signal/failed lifecycle cleanup and cleanup failures are observable. No tunnel to fixtures.
- The new guard parses YAML safely with duplicate-key/alias rejection (distribution `python3-yaml`, installed in the existing isolated runner prerequisites alongside python3; no repository dependency change), checks the exact channels job/step/command/env and non-main PR condition, absence of bypass/continue-on-error, and the common ordered `RUNNER_SCRIPT` lifecycle. It fails before product suites on missing or divergent membership/lifecycle. Synthetic copies with E2E/browser removed, reorder, weakened job gating and swallowed errors must fail; the real contract must pass. If an implementation needs any extra path/dependency, return for admission rather than silently expanding this proposal.
- The workflow adds one PR-only, non-main-head `channels-validation` job with read-only repository permissions, timeout60minutes, checkout, existing private-submodule token pattern scoped to API/Web checkout, and `CHANNELS_DOCKER_TRANSPORT=linux` + `bash scripts/test-channels-local.sh all`. Preserve existing Compose/API/Web jobs and no publish/deploy step. No new secret type or real service credential. Runtime uses fixtures only. No `continue-on-error`, reduced test filtering, automatic source push or gitlink reconciliation.

Representative exact new job shape (normal workflow indentation):

```yaml
channels-validation:
  name: Channels PostgreSQL and browser
  if: github.event_name == 'pull_request' && github.head_ref != 'main'
  runs-on: ubuntu-latest
  timeout-minutes: 60
  steps:
    - uses: actions/checkout@v4
    - name: Checkout private channel validation sources
      env:
        SUBMODULES_REPO_TOKEN: ${{ secrets.SUBMODULES_REPO_TOKEN }}
      run: |
        test -n "$SUBMODULES_REPO_TOKEN" || exit 1
        git config --global url."https://x-access-token:${SUBMODULES_REPO_TOKEN}@github.com/".insteadOf "https://github.com/"
        git submodule sync -- api-app web-app
        git submodule update --init --depth=1 api-app web-app
    - name: Validate channel suite and lifecycle
      env:
        CHANNELS_DOCKER_TRANSPORT: linux
      run: bash scripts/test-channels-local.sh all
```

No local product push or remote job trigger is authorized. Remote execution stays `not_run`, owned by the later CI/promotion operator after authorized source publication. A configured workflow is not remote success. Isolated fixture mutation in this PR job does not target main/production services. Fork PRs without the existing private token must fail explicitly, never pretend to test absent submodules.

## Required proof before local delivery

1. Capture index-less RED above and the bounded no-window source correction; preserve raw provenance. Re-run all after the new index/CI contract is implemented and admitted. Invalidation is mandatory because tests, schema and runner ownership changed; prior582-pass run80903 remains historical.
2. New migration deploy/status on fresh disposable PG16; confirm managed index keys and latest-IN behavior with older/expired IN, equal-time tie, OUT-heavy and no-IN, mixed selected origins and at most500-reference page. Query equality includes direction in the index condition; measure loops/rows removed/buffer work and increasing suffix depth. Avoid fragile timing-only assertions or asserting one optimizer node name as a performance guarantee.
3. Demonstrate no-window selected conversations do not call latest-IN; require window only for the actually selected binding, retaining existing unavailable/ambiguous and metadata-only behavior. Maintain BU isolation and no credential decryption/network on GET.
4. Run the drift guard with real and meaningful mutated pipeline/lifecycle inputs; prove same full suite family/order/fixtures/freshness/cleanup for Windows local and Linux CI transport. Execute an isolated local Linux-transport rehearsal where available against the exact reviewed checkout and same disposable namespace, serialized with Windows runs. Compare the Docker server identity internally if both CLIs are used to prevent crossing unrelated engines. If Linux bind topology cannot actually execute, report that blocker and do not certify it from YAML/config-only checks. Do not use host npm or an unapproved alternate runner to bypass the contract.
5. Full canonical `all` on final principal checkout, PCV artifacts refreshed with per-conversation readback and actual new plan; complete fresh Performance/TQA/Cutover after remediation. TQA must explicitly complete its full reporting rubric; prior short report is not a full pass.
6. Only then rebuild exact changed local images, migrate the one local test DB, activate API/Web preserving other services/channels/credentials, restore gateway HTTPS and collect fresh real IN/OUT official and unofficial. Current containers and tunnel are not modified by this proposal.
7. Final review/guards/consolidation/closeout remain required. Seller-direct template submission in05 and contact-first04 remain handoffs, not execution authority.

## Contract edits to govern the renewal

Update the governing TODO to v1.3, planning/review state pending renewed approval. Add SCOPE-06 for this one query index plus shared CI admission. DOD-06/VAL-01/VAL-05 explicitly require this parity/index evidence. D06 in both resolved/frozen sections preserves existing indexes/acceptance and adds only this narrow D07 query-index exception. D07 adds selected-window-only work and history-distribution plan proof without temporal semantics changes. D10 adds host-transport parity and drift guard. Update strict ExpectedPaths with the four exact additions; remove blanket Prisma forbid while keeping all other Prisma paths fail-closed. Change out-of-scope/schema wording solely for this named index. Update required CI matrix, risks (index storage/write lock, CI duration/private checkout/platform), execution order and review ledger. Previous v1.2 APROVADO/companion validation and review history remain intact; new implementation authority is pending human approval.

The renewed approval would authorize this exact subordinate remediation and subsequent original local validation/activation; it would not authorize real new providers, templates, source push, Railway/production, private config reads or changing/deleting registered channels.
