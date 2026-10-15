import { createRequire } from 'node:module';
import { performance } from 'node:perf_hooks';
const requireFromApi = createRequire('/workspace/api-app/package.json');
const requireFromWeb = createRequire('/workspace/web-app/package.json');
const { PrismaClient } = requireFromApi('@prisma/client');
const { request } = requireFromWeb('@playwright/test');
const base = 'http://127.0.0.1:3100';
const fixtureBase = 'http://127.0.0.1:3101';
const product = await request.newContext({ baseURL: base });
const fixtureApi = await request.newContext({ baseURL: fixtureBase });
const prisma = new PrismaClient({ datasources: { db: { url: process.env.LEADSHUG_E2E_DATABASE_URL } } });
try {
  const seededResponse = await fixtureApi.post('/seed', { data: { count: 251, tied: true } });
  if (seededResponse.status() !== 201) throw new Error(`seed falhou: ${seededResponse.status()}`);
  const seeded = await seededResponse.json();
  const foreignResponse = await fixtureApi.post('/seed', { data: { count: 2 } });
  if (foreignResponse.status() !== 201) throw new Error(`seed estrangeira falhou: ${foreignResponse.status()}`);
  const foreign = await foreignResponse.json();
  await prisma.conversation.update({ where: { id: seeded.conversationId }, data: { unreadCount: 7 } });
  const login = await product.post('/api/bff/auth/login', { data: { email: seeded.email, senha: seeded.password }, headers: { origin: 'http://127.0.0.1:4173', 'x-requested-with': 'XMLHttpRequest' } });
  if (login.status() !== 200) throw new Error(`login falhou: ${login.status()} ${(await login.text()).slice(0, 300)}`);
  const before = await (await fixtureApi.get(`/audit?conversationId=${seeded.conversationId}`)).json();
  const accessUrl = `/api/bff/conversations/${seeded.conversationId}/messages?limite=50&marcarLida=false`;
  const timings = [];
  const statuses = [];
  for (let batch = 0; batch < 6; batch += 1) {
    const results = await Promise.all(Array.from({ length: 5 }, async () => {
      const started = performance.now();
      const response = await product.get(accessUrl);
      const elapsedMs = performance.now() - started;
      const body = await response.json();
      return { status: response.status(), elapsedMs, count: body.messages?.length, hasPrevious: body.paginacao?.temAnteriores };
    }));
    for (const result of results) { statuses.push(result.status); timings.push(result.elapsedMs); if (result.status !== 200 || result.count !== 50 || result.hasPrevious !== true) throw new Error(`resposta inesperada: ${JSON.stringify(result)}`); }
  }
  const denied = await product.get(`/api/bff/conversations/${foreign.conversationId}/messages?limite=invalid`);
  const after = await (await fixtureApi.get(`/audit?conversationId=${seeded.conversationId}`)).json();
  if (denied.status() !== 404) throw new Error(`conversa sem grant devia ocultar-se como404; recebeu ${denied.status()}`);
  if (before.unreadCount !== 7 || after.unreadCount !== 7 || before.messages.length !== after.messages.length) throw new Error('leitura alterou estado ou histórico.');
  const sorted = timings.toSorted((a, b) => a - b);
  const percentile = (p) => Number(sorted[Math.ceil(p * sorted.length) - 1].toFixed(2));
  console.log(JSON.stringify({ runId: 'rls-read-stage1-20261015', sample: { requests: timings.length, concurrency: 5, batches: 6, statusCounts: { '200': statuses.filter((x) => x === 200).length, errors: statuses.filter((x) => x !== 200).length }, p50Ms: percentile(0.50), p95Ms: percentile(0.95), maxMs: Number(Math.max(...timings).toFixed(2)), messagesPerResponse: 50, hasPrevious: true }, scope: { accessibleConversation: '200 x30', foreignConversationWithMalformedCursor: denied.status(), unreadBefore: before.unreadCount, unreadAfter: after.unreadCount, messagesBefore: before.messages.length, messagesAfter: after.messages.length }, conclusion: 'small disposable one-stage read-neutral sample; no production SLO inferred' }, null, 2));
} finally {
  await prisma.$disconnect();
  await product.dispose();
  await fixtureApi.dispose();
}
