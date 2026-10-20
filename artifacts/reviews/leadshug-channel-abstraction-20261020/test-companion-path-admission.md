# ST-CON-06 — bounded test companion path admission

Derived proposal explicitly validated by the user2026-10-20: “Validar os dois arquivos de apoio”. Normal authority guard returned go after exact ExpectedPaths admission. Product scope, frozen D01..10 and acceptance requirements remain unchanged. No permission to weaken tests or access private paths.

The approved strict Diff Expectation Contract lists `src/api.ts` and `e2e/number-onboarding-freshness.ts`, but omits their existing companion unit test and nested freshness helper. Its literal rule is **User validation: required on deviation**.

Requested exact additional Web paths, both M:
- `src/api.spec.ts`: retain the added direct assertion that ErroDaApi carries the approved safe uncertainty fields (D10); no product behavior change. This test was already added by the executor before the path omission was noticed. It has not been accepted as a delivered deviation.
- `e2e/timeline-freshness.ts`: constrain staged/unstaged/untracked Git inventory to existing positive public pathspecs before discovery; preserve actual API/DB/build/served-bundle verification and all outputs. This nested helper runs before number-onboarding freshness. Its correction is prepared below but NOT applied. Browser/all must wait for admission.

No alternative shim, duplicate freshness implementation, bypass or excluded validation is proposed. Continue API and other authorized work independently. These are companion-path corrections within SCOPE05/D10, not new channels, templates, lifecycle or schema.

## Existing direct unit-test diff for explicit validation

```diff
diff --git a/src/api.spec.ts b/src/api.spec.ts
index 6b29974..0f5ca57 100644
--- a/src/api.spec.ts
+++ b/src/api.spec.ts
@@ -108,6 +108,18 @@ describe('falha do servidor (o 500 do Nest)', () => {
     responde(JSON.stringify({ error: 'E-mail ou senha inválidos.', code: 'CREDENCIAL_INVALIDA' }), { status: 401 });
     await expect(api.post('/auth/login', {})).rejects.toThrow(/E-mail ou senha inválidos/);
   });
+
+  it('retém outcome e metadados seguros de incerteza', async () => {
+    responde(JSON.stringify({
+      error: 'O envio não foi confirmado.', code: 'OUTBOUND_LOCAL_INCOMPLETE',
+      outcome: 'ACCEPTED_LOCAL_INCOMPLETE', evidence: 'ACK_WITHOUT_ID',
+      localMessageState: 'UNCONFIRMED', diagnosticPersistence: 'UNCONFIRMED',
+    }), { status: 503 });
+    await expect(api.post('/conversations/c1/messages', { texto: 'draft' })).rejects.toMatchObject({
+      codigo: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'ACCEPTED_LOCAL_INCOMPLETE',
+      evidence: 'ACK_WITHOUT_ID', localMessageState: 'UNCONFIRMED', diagnosticPersistence: 'UNCONFIRMED',
+    });
+  });
 });
 
 describe('requisição com cabeçalho de correlação', () => {
```

## Proposed nested freshness diff (not applied)

```diff
--- a/e2e/timeline-freshness.ts
+++ b/e2e/timeline-freshness.ts
@@ -7,13 +7,13 @@
 
 const hash = (value: Buffer | string) => createHash('sha256').update(value).digest('hex');
 
-async function changedSourceFiles(directory: string, scope: RegExp): Promise<Array<{ path: string; status: string; sha256: string | null }>> {
+async function changedSourceFiles(directory: string, scope: RegExp, publicPaths: readonly string[]): Promise<Array<{ path: string; status: string; sha256: string | null }>> {
   const gitArgs = ['-c', `safe.directory=${directory}`, '-C', directory];
   const parse = (output: string, layer: string) => output.trim().split('\n').filter(Boolean)
     .map((line) => { const [status, ...paths] = line.split('\t'); return { status: `${layer}:${status}`, path: paths.at(-1)! }; });
-  const staged = parse(execFileSync('git', [...gitArgs, 'diff', '--cached', '--name-status', 'HEAD'], { encoding: 'utf8' }), 'staged');
-  const unstaged = parse(execFileSync('git', [...gitArgs, 'diff', '--name-status'], { encoding: 'utf8' }), 'unstaged');
-  const untracked = execFileSync('git', [...gitArgs, 'ls-files', '--others', '--exclude-standard'], { encoding: 'utf8' }).trim().split('\n').filter(Boolean)
+  const staged = parse(execFileSync('git', [...gitArgs, 'diff', '--cached', '--name-status', 'HEAD', '--', ...publicPaths], { encoding: 'utf8' }), 'staged');
+  const unstaged = parse(execFileSync('git', [...gitArgs, 'diff', '--name-status', '--', ...publicPaths], { encoding: 'utf8' }), 'unstaged');
+  const untracked = execFileSync('git', [...gitArgs, 'ls-files', '--others', '--exclude-standard', '--', ...publicPaths], { encoding: 'utf8' }).trim().split('\n').filter(Boolean)
     .map((path) => ({ status: '??', path }));
   const inventory = new Map<string, string>();
   for (const item of [...staged, ...unstaged, ...untracked]) if (scope.test(item.path)) {
@@ -79,8 +79,8 @@
     'Dockerfile', '.dockerignore', '.gitignore', 'eslint.config.js', 'playwright.config.ts',
     'railway.json', 'tsconfig.json', 'vite.config.ts', 'docker', 'nginx',
   ];
-  const apiSourceManifest = await changedSourceFiles(api, /^(src\/|prisma\/|test\/|package(?:-lock)?\.json$|Dockerfile$|\.dockerignore$|\.env\.example$|nest-cli\.json$|tsconfig(?:\.[^/]+)?\.json$)/);
-  const webSourceManifest = await changedSourceFiles(web, /^(src\/|e2e\/|playwright\.config\.ts$|vite\.config\.ts$|Dockerfile$|\.dockerignore$|package(?:-lock)?\.json$|tsconfig(?:\.[^/]+)?\.json$)/);
+  const apiSourceManifest = await changedSourceFiles(api, /^(src\/|prisma\/|test\/|package(?:-lock)?\.json$|Dockerfile$|\.dockerignore$|\.env\.example$|nest-cli\.json$|tsconfig(?:\.[^/]+)?\.json$)/, apiPublicPaths);
+  const webSourceManifest = await changedSourceFiles(web, /^(src\/|e2e\/|playwright\.config\.ts$|vite\.config\.ts$|Dockerfile$|\.dockerignore$|package(?:-lock)?\.json$|tsconfig(?:\.[^/]+)?\.json$)/, webPublicPaths);
   const requireFromApi = createRequire(join(api, 'package.json'));
   const { PrismaClient } = requireFromApi('@prisma/client') as { PrismaClient: new (options: { datasources: { db: { url: string } } }) => any };
   const prisma = new PrismaClient({ datasources: { db: { url: databaseUrl } } });
```
