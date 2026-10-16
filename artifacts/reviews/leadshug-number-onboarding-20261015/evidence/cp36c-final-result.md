# cp36c final validation result

Canonical command: `bash scripts/test-channels-local.sh all` (full stdout/stderr preserved as `cp36c-api-recovery-final-all.log`); runner exit 1.

API lint and build passed. API unit tests: 141 passed. PostgreSQL E2E: 288 passed. Web build and unit tests: 28 passed. Browser: 46 passed, 1 failed.

The sole browser failure was the unrelated People invite flow at `web-app/e2e/telas.spec.ts:348`: after clicking “Convidar”, the test timed out waiting for the “Ana” cell (not found). The page also recorded the public browser console message `Failed to load resource: the server responded with a status of 400 (Bad Request)`. No response body or catalog code was captured; this evidence does not assign the 400 to a particular API error. No rerun or source edit was performed.

Actual pre-worker and browser authority attestations are preserved separately. They record Node v22.23.3; disposable `leadshug_timeline_channels_ci`; 22 completed migrations; API, fixture and preview health 200; and served JavaScript hash equal to the generated `dist` hash. The freshness manifest enumerates the exact eight approved API paths, including the new untracked convergence helper, and matches `cp36c-source-after.sha256`.

The failure context file was not copied or retained. The preserved log contains only the sanitized assertion and synthetic fixture output. No operator runtime payloads, private dotenv contents, or `api-app/.local-files` files were read or included. Validation used only the source-owned `leadshug_channels_validation` project; no operator database was reset or modified.
