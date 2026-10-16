# cp36e API validation

The sole cp36e source change is in `api-app/src/integrations/meta/meta.client.spec.ts`. Four rejected operations now assert both `MetaIndisponivelError` instance identity and `META_INDISPONIVEL` code on the same captured promise; the pre-existing fetch-call budgets remain asserted.

Validation command: `bash scripts/test-channels-local.sh api` (captured by the invoking `set -o pipefail` shell with full stdout/stderr in `cp36e-api-validation.log`). Exit code: 0. The canonical API runner passed ESLint, Nest build, 141 unit tests (19 files), and 288 PostgreSQL E2E tests (26 files). It applied/verified 22 migrations in the disposable validation database.

`cp36e-source-before.sha256` and `cp36e-source-after.sha256` enumerate the same nine public source paths. Eight hashes are identical; only the admitted unit spec changed, from `d7ab2a4b5d6cd7f2c83f3b7939f5b86436baf82e69d085df5d35236e66caf8d9` to `1cbcd9a9bade8c90c0c468042c1396285b1e2f3eae4b5beb1718551d8ef65078`.

The cp36d Web/browser results and their pre-worker/bundle attestations remain bound to the unchanged cp36d runtime, fixtures and Web-test source hashes. They are retained as prior accepted evidence, not relabeled as cp36e validation. No new Web/browser run or pre-worker attestation was produced. No private payloads, `.local-files`, private dotenv or operator data were accessed.
