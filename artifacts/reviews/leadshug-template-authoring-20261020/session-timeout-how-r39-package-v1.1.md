# Source-aware HOW opinion — one opaque session revalidation test timeout

Derived no-context diagnostic opinion, not product implementation/final assurance. Current approved ST-CON-05 v1.1 feature is still Pending. Only principal checkout/single writer. No tools, network, private files, mutation, test execution or root-cause certainty without evidence. This is a one-test diagnostic scope; do not redesign auth/operation/leases or weaken security gates. Earlier original test-after/unknown debt is separate.

Actual r38 all:801pass/1browser wrong-counter assertion. API284unit/398PG all passed, including this session test ~1.27sec. Browserall74/75 and mainworkflow/all5markers passed; all targeted A-to-B behavioral assertions passed, final fixturecounter wrong. r39 source changed ONLY final2browser counter lines; product/API/test entirely unchanged. Actual r39 APIunit284pass;PG397pass/1 test timed out60000ms; Web/browser not reached. Whole file44/45; aggregatefailure is timeout only, no stage/scenario trace. Exact logs/receipt/source checks linked below, not reproduced by you. No actual new provider/runtime/DB activation.

We need the simplest faithful next diagnostic HOW. Evaluate source for a concrete trigger if possible; separate proven bugs from hypotheses and do not label opaque failure flaky/environment/product on assumption. Important: test uses actual sessions/BFF/Prisma/PostgreSQL with external HTTP fetch stub held at provider; custom observation clock advances11s, global Date.now only temporarily advances past token expiry, passwordChangedAt is claims.iat+1, relogin after each scenario. Six held scenarios plus later ADMIN→ATENDENTE expected403 and exact before/after DB snapshots/no writes. No direct session fabrication/privilege bypass or timeout increase.

Proposed initial diagnostic direction only: inside THIS test, make every provider-entry wait race the corresponding real HTTP result with a bounded10s diagnostic deadline and fixed scenario labels. If HTTP finishes before provider entry, fail with kind/mode/invalidation+HTTPstatus only; no cookie/token/email/IDs/providerbody. Add fixed-phase breadcrumbs only if needed to locate preparation or cleanup hangs. Preserve actual provider gate/release order, all401/403/snapshot oracles, all scenarios, mocked external boundary only, current production code and overall60s timeout. Release held gates and await pending requests in finally; do not mask failures or auto-retry. Root will review exact diff before one canonical api diagnostic run; no new full all until failure attributed or bounded by evidence. A passing diagnostic run would not retroactively identify root cause of the opaque r39 timeout. Recommend alternatives A/B/C when material and whether a non-code source explanation already suffices.

Assess whether instrumentation itself alters authorization timing/invalidates the proof, and propose a smaller safer diagnostic if needed. Explicitly identify which invariant a proposed actual fix would preserve. No stronger claim from missing error context or old browser proofs. Return strict dispatch-bound review JSON with a substantive overall_assessment, concrete source lines, recommended next step and uncertainty; no fabricated reproduction. Status/evidence clarity is the goal, not cosmetic zero findings.

## api-app/test/message-template-management.e2e-spec.ts (declared lines1..104)

```text
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from 'vitest';
import { createHash, randomUUID } from 'node:crypto';
import request from 'supertest';
import type { Prisma } from '@prisma/client';
import { TEMPLATE_MANAGEMENT_RESOLVER, type TemplateManagementResolver } from '../src/domain/message-templates/template-management.ports';
import { TemplateDraftService } from '../src/domain/message-templates/template-draft.service';
import { TemplateSubmissionService } from '../src/domain/message-templates/template-submission.service';
import { TEMPLATE_TRANSACTION_BOUNDARY, type TemplateTransactionBoundary } from '../src/domain/message-templates/template-transaction-boundary';
import { TEMPLATE_OBSERVATION_CLOCK, TemplateObservationService, type TemplateObservationClock } from '../src/domain/message-templates/template-observation.service';
import { sealChannelCredential } from '../src/domain/channels/channel-credential-crypto';
import { templateDefinitionSemanticFingerprint } from '../src/domain/message-templates/template-definition';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { criarCanalVerificado, criarMantenedora, criarUsuario, limparBanco, login, META_APP_SECRET, subirApp } from './helpers';

function response(status: number, payload: unknown): Response {
  return new Response(JSON.stringify(payload), { status, headers: { 'content-type': 'application/json' } });
}

function deferred<T>() {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((done) => { resolve = done; });
  return { promise, resolve };
}

async function withReadbackFailure<T>(service: TemplateSubmissionService,
  model: 'messageTemplateOperation' | 'messageTemplateSubmissionReceipt', action: 'findFirst', run: () => Promise<T>): Promise<T> {
  const target = service as unknown as { prisma: PrismaService };
  const original = target.prisma;
  let pending = true;
  target.prisma = new Proxy(original, { get(prisma, property) {
    const delegate = Reflect.get(prisma, property, prisma);
    if (property !== model || !delegate || typeof delegate !== 'object') return delegate;
    return new Proxy(delegate as object, { get(modelDelegate, method) {
      const value = Reflect.get(modelDelegate, method, modelDelegate);
      if (method === action && pending) {
        pending = false;
        return () => Promise.reject(new Error('injected PostgreSQL readback unavailable'));
      }
      return value;
    } });
  } });
  try { return await run(); }
  finally { target.prisma = original; }
}

describe('scoped template-management provider (PostgreSQL)', () => {
  let app: Awaited<ReturnType<typeof subirApp>>['app'];
  let prisma: PrismaService;
  let buId: string;
  let buId2: string;
  let channel1: string;
  let channel2: string;
  let ownerId: string;
  let ownerEmail: string;

  beforeAll(async () => {
    const originalDatabaseUrl = process.env.DATABASE_URL;
    if (!originalDatabaseUrl) throw new Error('A configuração descartável de PostgreSQL não está disponível.');
    const boundedDatabaseUrl = new URL(originalDatabaseUrl);
    boundedDatabaseUrl.searchParams.set('connection_limit', '5');
    process.env.DATABASE_URL = boundedDatabaseUrl.toString();
    try { ({ app, prisma } = await subirApp(undefined, true)); }
    finally { process.env.DATABASE_URL = originalDatabaseUrl; }
  });
  beforeEach(async () => {
    await limparBanco(prisma);
    ownerEmail = `template-provider-${Date.now()}@example.test`;
    const tenant = await criarMantenedora(app, 'Template provider tenant', ownerEmail);
    buId = tenant.businessUnit.id;
    ownerId = tenant.owner.id;
    const first = await criarCanalVerificado(prisma, buId, 'OFICIAL', `template-phone-a-${Date.now()}`);
    const firstBu = await prisma.businessUnit.findUniqueOrThrow({ where: { id: buId }, select: { setorId: true } });
    const secondBu = await prisma.businessUnit.create({ data: {
      mantenedoraId: tenant.mantenedora.id, setorId: firstBu.setorId, name: `Template second number ${Date.now()}`,
    } });
    buId2 = secondBu.id;
    await prisma.userBuRole.create({ data: { userId: ownerId, buId: buId2, role: 'OWNER', grantedViaTipo: 'DIRETO' } });
    const second = await criarCanalVerificado(prisma, buId2, 'OFICIAL', `template-phone-b-${Date.now()}`);
    channel1 = first.channel.id;
    channel2 = second.channel.id;
    await prisma.buChannel.update({ where: { id: channel1 }, data: { wabaId: 'waba-a', status: 'DESCONECTADO', receiptVerifiedAt: null } });
    await prisma.buChannel.update({ where: { id: channel2 }, data: { wabaId: 'waba-b', status: 'DESCONECTADO', receiptVerifiedAt: null } });
    const keyId = process.env.CHANNEL_CREDENTIAL_KEY_ID!;
    const key = Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY!, 'base64');
    const otherAccountCredential = sealChannelCredential('fixture-account-b-token', keyId, key, {
      purpose: 'active', provider: 'OFICIAL', buId: buId2, channelId: channel2,
      generation: second.channel.generation, version: 1,
    });
    await prisma.channelCredential.update({ where: { channelId: channel2 }, data: {
      keyId, nonce: new Uint8Array(otherAccountCredential.nonce),
      ciphertext: new Uint8Array(otherAccountCredential.ciphertext), tag: new Uint8Array(otherAccountCredential.tag),
    } });
  });
  afterAll(async () => { if (prisma) await limparBanco(prisma); await app?.close(); });

  it('resolves capability without network or decryption and uses one scoped grant across pages and create', async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(response(200, { data: {
        app_id: 'fixture-app', is_valid: true, scopes: ['whatsapp_business_management'],
        granular_scopes: [{ scope: 'whatsapp_business_management', target_ids: ['waba-a'] }],
      } }))
      .mockResolvedValueOnce(response(200, { data: [
        { id: 'remote-1', name: 'welcome_user', language: 'pt_BR', status: 'APPROVED', category: 'UTILITY', parameter_format: 'NAMED', components: [{ type: 'BODY', text: 'Olá {{first_name}}.' }] },
      ], paging: { next: 'https://graph.facebook.com/v26.0/opaque', cursors: { after: 'cursor-one' } } }))
```

## api-app/test/message-template-management.e2e-spec.ts (declared lines2283..2398)

```text
  it('revalidates BFF session and current observation role before success and unavailable commits', async () => {
    const drafts = app.get(TemplateDraftService);
    const submissions = app.get(TemplateSubmissionService);
    const observations = app.get(TemplateObservationService);
    const resolver = app.get(TEMPLATE_MANAGEMENT_RESOLVER) as TemplateManagementResolver;
    const context = await resolver.resolve({ buId, channelId: channel1, expectedGeneration: 1 });
    const hash = (value: string) => createHash('sha256').update(value).digest('hex');
    const identity = { mantenedoraId: context.context.mantenedoraId, buId: context.context.buId,
      channelId: context.context.channelId, accountReference: context.context.accountReference,
      generation: context.context.generation, pairingEpoch: context.context.pairingEpoch,
      providerResourceIdentityId: context.context.providerResourceIdentityId,
      activeCredentialVersion: context.context.activeCredentialVersion };
    const contextKey = hash(JSON.stringify(Object.fromEntries(Object.entries(identity).sort(([a], [b]) => a.localeCompare(b)))));
    const cursorHash = hash(JSON.stringify('first-page'));
    const definition = { name: 'session_revalidation', language: 'pt_BR' as const, category: 'UTILITY' as const,
      body: 'Olá {{first_name}}.', examples: { first_name: 'Ana' } };
    const draft = await drafts.createDraft(ownerId, { buId, channelId: channel1, expectedGeneration: 1,
      clientRequestId: 'observation-session-revalidation', definition });
    const approved = { id: 'session-revalidation-remote', name: definition.name, language: definition.language,
      status: 'APPROVED', category: definition.category, parameter_format: 'NAMED',
      components: [{ type: 'BODY', text: definition.body }] };
    type Held = { kind: 'individual' | 'catalog'; mode: 'success' | 'error'; started: ReturnType<typeof deferred<void>>; gate: ReturnType<typeof deferred<Response>> };
    let held: Held | null = null;
    const fetchMock = vi.fn(async (input: RequestInfo | URL, init: RequestInit = {}) => {
      const url = String(input); const method = init.method ?? 'GET';
      if (url.includes('/debug_token')) return response(200, { data: { app_id: 'fixture-app', is_valid: true,
        scopes: ['whatsapp_business_management'], granular_scopes: [{ scope: 'whatsapp_business_management', target_ids: ['waba-a'] }] } });
      if (url.endsWith('/message_templates') && method === 'POST') return response(200, { id: approved.id });
      if (url.includes('/message_templates?') && method === 'GET') {
        if (new URL(url).searchParams.has('name')) return response(200, { data: [] });
        if (held?.kind === 'catalog') { const active = held; active.started.resolve(undefined); return active.gate.promise; }
        return response(200, { data: [approved] });
      }
      if (url.includes(`/${approved.id}?`) && method === 'GET') {
        if (held?.kind === 'individual') { const active = held; active.started.resolve(undefined); return active.gate.promise; }
        return response(200, approved);
      }
      throw new Error(`unexpected template request ${method} ${url}`);
    });
    vi.stubGlobal('fetch', fetchMock);
    const clock = app.get<TemplateObservationClock>(TEMPLATE_OBSERVATION_CLOCK);
    let now = new Date();
    const clockSpy = vi.spyOn(clock, 'now').mockImplementation(() => new Date(now));
    const inFlight: Array<Promise<unknown>> = [];
    const post = (cookie: string, path: string) => request(app.getHttpServer()).post(path)
      .set('Cookie', cookie).set('x-requested-with', 'teste').send({});
    const snapshot = async () => Promise.all([
      prisma.messageTemplateRemoteObservation.findUniqueOrThrow({ where: { contextKey_remoteTemplateId: { contextKey, remoteTemplateId: approved.id } },
        select: { status: true, available: true, safeCode: true, observedEligible: true, observedAt: true, observedFence: true, components: true } }),
      prisma.messageTemplateCatalogPage.findUniqueOrThrow({ where: { contextKey_cursorHash: { contextKey, cursorHash } },
        select: { remoteTemplateIds: true, nextCursor: true, available: true, safeCode: true, observedAt: true, observedFence: true } }),
    ]);
    try {
      const submitted = await submissions.submitDraft(ownerId, { draftId: draft.id, expectedRevision: 1,
        expectedGeneration: 1, expectedDefinitionFingerprint: draft.definitionFingerprint,
        idempotencyKey: 'ab3e8a56-2493-4a84-a64d-1744ddaf56f4' });
      expect(submitted.phase).toBe('ACCEPTED');
      await observations.refreshCatalog(ownerId, buId, channel1, null);
      now = new Date(now.getTime() + 11_000);
      await observations.refreshDraft(ownerId, draft.id);
      const before = await snapshot();
      let cookie = await login(app, ownerEmail);

      for (const scenario of [
        { kind: 'individual', mode: 'success', invalidation: 'password' }, { kind: 'individual', mode: 'error', invalidation: 'password' },
        { kind: 'catalog', mode: 'success', invalidation: 'password' }, { kind: 'catalog', mode: 'error', invalidation: 'password' },
        { kind: 'individual', mode: 'success', invalidation: 'expiry' },
        { kind: 'catalog', mode: 'success', invalidation: 'expiry' },
      ] as const) {
        now = new Date(now.getTime() + 11_000);
        const active: Held = { ...scenario, started: deferred<void>(), gate: deferred<Response>() };
        held = active;
        const path = scenario.kind === 'individual' ? `/api/bff/message-templates/${draft.id}/refresh`
          : `/api/bff/business-units/${buId}/channels/${channel1}/message-template-catalog`;
        const pending = post(cookie, path).then((result) => result);
        inFlight.push(pending);
        await active.started.promise;
        const token = cookie.slice(cookie.indexOf('=') + 1);
        const claims = JSON.parse(Buffer.from(token.split('.')[0], 'base64url').toString()) as { iat: number; exp: number };
        if (scenario.invalidation === 'password') {
          await prisma.appUser.update({ where: { id: ownerId }, data: { passwordChangedAt: new Date(claims.iat + 1) } });
        }
        const body = scenario.kind === 'individual'
          ? scenario.mode === 'success' ? approved : { ...approved, error: { code: 1, message: 'controlled contradiction' } }
          : scenario.mode === 'success' ? { data: [approved] } : { data: [approved], error: { code: 1, message: 'controlled contradiction' } };
        const originalDateNow = Date.now;
        if (scenario.invalidation === 'expiry') Date.now = () => claims.exp + 1;
        active.gate.resolve(response(200, body));
        try { expect((await pending).status).toBe(401); }
        finally { Date.now = originalDateNow; }
        expect(await snapshot()).toEqual(before);
        held = null;
        cookie = await login(app, ownerEmail);
      }

      const tenant = await prisma.businessUnit.findUniqueOrThrow({ where: { id: buId }, select: { mantenedoraId: true } });
      const adminEmail = `template-observation-admin-${Date.now()}@example.test`;
      const adminId = await criarUsuario(prisma, tenant.mantenedoraId, buId, adminEmail, 'ADMIN');
      const adminCookie = await login(app, adminEmail);
      now = new Date(now.getTime() + 11_000);
      const active: Held = { kind: 'individual', mode: 'success', started: deferred<void>(), gate: deferred<Response>() };
      held = active;
      const pending = post(adminCookie, `/api/bff/message-templates/${draft.id}/refresh`).then((result) => result);
      inFlight.push(pending);
      await active.started.promise;
      await prisma.userBuRole.update({ where: { userId_buId: { userId: adminId, buId } }, data: { role: 'ATENDENTE' } });
      active.gate.resolve(response(200, approved));
      expect((await pending).status).toBe(403);
      expect(await snapshot()).toEqual(before);
    } finally {
      held?.gate.resolve(response(200, { data: [approved] }));
      await Promise.allSettled(inFlight);
      clockSpy.mockRestore(); vi.unstubAllGlobals();
    }
  }, 60_000);
});
```

## api-app/test/helpers.ts (declared lines329..339)

```text
export async function login(app: INestApplication, email: string, senha = 'senha-de-teste-1'): Promise<string> {
  const res = await request(app.getHttpServer())
    .post('/api/bff/auth/login')
    .set('x-requested-with', 'teste')
    .send({ email, senha })
    .expect(200);
  const setCookie = res.headers['set-cookie'] as unknown as string[];
  return setCookie[0].split(';')[0];
}
```

## api-app/src/infra/session/session.service.ts

```text
import { Injectable } from '@nestjs/common';
import { createHmac, timingSafeEqual } from 'node:crypto';

export const SESSION_COOKIE = 'lh_session';

export type SameSite = 'Lax' | 'Strict' | 'None';

/**
 * Lê `COOKIE_SAMESITE` sem exigir que ninguém acerte a caixa.
 *
 * O valor é o do atributo do cookie (`None`, com N maiúsculo), mas aceitar só a
 * forma exata seria uma armadilha: quem escrevesse `none` receberia `Lax` em
 * silêncio, e o sintoma seria exatamente o login mudo que a variável existe para
 * resolver. Vazio e desconhecido caem em `Lax` — nunca no mais permissivo.
 */
export function normalizarSameSite(valor: string | undefined): SameSite {
  switch (valor?.trim().toLowerCase()) {
    case 'none':
      return 'None';
    case 'strict':
      return 'Strict';
    default:
      return 'Lax';
  }
}

/** Um valor escrito e não reconhecido é engano de quem configurou, não default. */
export function valorDeSameSiteEhSuspeito(valor: string | undefined): boolean {
  const v = valor?.trim();
  if (!v) return false;
  return !['none', 'lax', 'strict'].includes(v.toLowerCase());
}

/** 1 dia — limita a janela de risco de um computador esquecido logado (ADR-0007). */
const DURACAO_MS = 24 * 60 * 60 * 1000;

export interface SessionClaims {
  /** id do app_user. O papel NÃO vem aqui: ele é lido do banco a cada request. */
  uid: string;
  iat: number;
  exp: number;
}

/**
 * Cookie de sessão assinado (ADR-0007 §1).
 *
 * O corpo carrega apenas `uid`, `iat` e `exp`. Papel, capacidade e escopo ficam
 * de fora de propósito: se viajassem no cookie, promoção e rebaixamento só
 * valeriam no próximo login.
 */
@Injectable()
export class SessionService {
  private readonly segredo = process.env.SESSION_SECRET ?? '';

  get configurado(): boolean {
    return this.segredo.length > 0;
  }

  assinar(uid: string, agora = Date.now()): string {
    const claims: SessionClaims = { uid, iat: agora, exp: agora + DURACAO_MS };
    const corpo = Buffer.from(JSON.stringify(claims)).toString('base64url');
    return `${corpo}.${this.hmac(corpo)}`;
  }

  verificar(token: string | undefined, agora = Date.now()): SessionClaims | null {
    if (!token || !token.includes('.')) return null;
    const [corpo, assinatura] = token.split('.');
    if (!corpo || !assinatura) return null;
    if (!this.assinaturaConfere(corpo, assinatura)) return null;

    try {
      const claims = JSON.parse(Buffer.from(corpo, 'base64url').toString()) as SessionClaims;
      if (!claims.uid || typeof claims.exp !== 'number') return null;
      if (agora > claims.exp) return null;
      return claims;
    } catch {
      return null;
    }
  }

  /**
   * `Secure` só fora de desenvolvimento: em http local o navegador descartaria
   * o cookie.
   *
   * `Domain` vem de COOKIE_DOMAIN e é o que faz o cookie emitido pela API valer
   * no subdomínio do front (ADR-0015). SameSite continua `Lax` porque
   * subdomínios do mesmo domínio são o **mesmo site** — sem essa variável, o
   * cookie fica preso ao host que o emitiu e o login "funciona e não entra".
   */
  cookie(token: string): string {
    const maxAge = Math.floor(DURACAO_MS / 1000);
    return `${SESSION_COOKIE}=${token}; HttpOnly;${this.atributos()} Max-Age=${maxAge}`;
  }

  cookieVazio(): string {
    return `${SESSION_COOKIE}=;${this.atributos()} HttpOnly; Max-Age=0`;
  }

  /**
   * `SameSite` é `Lax` por padrão, e é assim que produção tem de ficar.
   *
   * `COOKIE_SAMESITE=None` existe para UM caso: stage nos domínios gerados pela
   * Railway. `*.up.railway.app` é sufixo público, então dois serviços ali são
   * **sites diferentes** — o navegador recusa `Domain` compartilhado e o `Lax`
   * bloqueia o envio. O sintoma é mudo: o login responde 200, o Set-Cookie
   * chega, e a requisição seguinte vai sem cookie.
   *
   * O preço de `None`: a proteção de CSRF passa a depender **só** do cabeçalho
   * `X-Requested-With` exigido no que muda estado. Aceitável num ambiente de QA,
   * inaceitável em produção — ver ADR-0015, Emenda 1.
   */
  private atributos(): string {
    const sameSite = normalizarSameSite(process.env.COOKIE_SAMESITE);
    // `SameSite=None` sem `Secure` é recusado por todo navegador atual, então o
    // Secure deixa de depender do NODE_ENV quando ele está ligado.
    const secure = sameSite === 'None' || process.env.NODE_ENV === 'production' ? ' Secure;' : '';
    const dominio = process.env.COOKIE_DOMAIN ? ` Domain=${process.env.COOKIE_DOMAIN};` : '';
    return `${secure}${dominio} SameSite=${sameSite}; Path=/;`;
  }

  extrairDoCabecalho(cookieHeader: string | undefined): string | undefined {
    if (!cookieHeader) return undefined;
    for (const parte of cookieHeader.split(';')) {
      const [nome, ...resto] = parte.trim().split('=');
      if (nome === SESSION_COOKIE) return resto.join('=');
    }
    return undefined;
  }

  private hmac(corpo: string): string {
    return createHmac('sha256', this.segredo).update(corpo).digest('base64url');
  }

  private assinaturaConfere(corpo: string, assinatura: string): boolean {
    const esperada = Buffer.from(this.hmac(corpo));
    const recebida = Buffer.from(assinatura);
    if (esperada.length !== recebida.length) return false;
    return timingSafeEqual(esperada, recebida);
  }
}
```

## api-app/src/surfaces/bff/session.middleware.ts

```text
import { ConflictException, ForbiddenException, Injectable, NestMiddleware, UnauthorizedException } from '@nestjs/common';
import type { NextFunction, Request, Response } from 'express';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { SessionService } from '../../infra/session/session.service';

export interface UsuarioDaSessao {
  id: string;
  mantenedoraId: string;
  nome: string;
  email: string;
  precisaTrocarSenha: boolean;
}

declare global {
  // eslint-disable-next-line @typescript-eslint/no-namespace
  namespace Express {
    interface Request {
      usuario?: UsuarioDaSessao;
    }
  }
}

/** Rotas liberadas dentro do BFF: são o que existe ANTES de haver sessão. */
const PUBLICAS = new Set([
  '/api/bff/auth/login',
  // Convite e recuperação (ADR-0025 §6): quem pede recuperação não tem sessão
  // por definição, e quem aceita convite ainda não tem conta utilizável. Não
  // viram superfície nova — a plateia é a mesma do login: a tela.
  '/api/bff/auth/recuperar',
]);

/** As rotas de token carregam o valor no caminho, então casam por prefixo. */
const PUBLICAS_POR_PREFIXO = ['/api/bff/auth/token/'];

/** Enquanto a troca inicial não acontece, só estas respondem (ADR-0007 §4). */
const LIBERADAS_EM_TROCA_OBRIGATORIA = new Set(['/api/bff/me', '/api/bff/me/password', '/api/bff/auth/logout']);

/**
 * Enquanto o wizard não termina, só estas respondem (ADR-0016 §4).
 *
 * A ORDEM É `senha → wizard → produto` (ADR-0016, Emenda 1 §3), e é a razão de
 * o wizard NÃO estar na lista acima: a troca de senha é trava de SEGURANÇA — a
 * credencial do bootstrap passou por fora do produto — e o wizard é onboarding
 * de PRODUTO. Segurança primeiro. Sem essa ordem, o OWNER recém-criado fica
 * preso entre os dois portões sem rota para nenhum.
 */
const LIBERADAS_EM_ONBOARDING = new Set([
  '/api/bff/me',
  '/api/bff/me/password',
  '/api/bff/auth/logout',
  '/api/bff/onboarding',
]);

/**
 * Guard da superfície BFF (ADR-0006): montado no PREFIXO, então rota nova nasce
 * exigindo sessão sem ninguém lembrar de anotá-la.
 *
 * O cookie prova que ele é autêntico — não que o acesso continua válido AGORA.
 * Por isso o usuário é relido do banco a cada request (ADR-0007 §1).
 */
@Injectable()
export class SessionMiddleware implements NestMiddleware {
  constructor(
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
  ) {}

  async use(req: Request, _res: Response, next: NextFunction): Promise<void> {
    const caminho = req.path;
    const mudaEstado = !['GET', 'HEAD', 'OPTIONS'].includes(req.method);

    // Rota pública do BFF (só o login). Ela muda estado e não tem sessão para
    // proteger, mas ainda assim exige o cabeçalho: login por CSRF existe, e o
    // custo de barrar é zero.
    if (PUBLICAS.has(caminho) || PUBLICAS_POR_PREFIXO.some((p) => caminho.startsWith(p))) {
      this.exigirCabecalhoAntiCsrf(req, mudaEstado);
      return next();
    }

    const token = this.sessions.extrairDoCabecalho(req.headers.cookie);
    const claims = this.sessions.verificar(token);
    if (!claims) {
      throw new UnauthorizedException({ error: 'Não autenticado.', code: 'NAO_AUTENTICADO' });
    }

    const user = await this.prisma.appUser.findUnique({ where: { id: claims.uid } });
    // Excluído, inativado ou com senha trocada depois da emissão: a sessão cai
    // na requisição seguinte, não no vencimento do cookie.
    if (!user || user.status !== 'ATIVO') {
      throw new UnauthorizedException({ error: 'Não autenticado.', code: 'NAO_AUTENTICADO' });
    }
    if (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat) {
      throw new UnauthorizedException({ error: 'Sessão expirada.', code: 'NAO_AUTENTICADO' });
    }

    if (user.mustChangePassword && !LIBERADAS_EM_TROCA_OBRIGATORIA.has(caminho)) {
      throw new ForbiddenException({
        error: 'Troque sua senha inicial antes de usar o sistema.',
        code: 'TROCA_DE_SENHA_OBRIGATORIA',
      });
    }

    // O segundo portão, e SÓ depois que o primeiro foi vencido. Painel sem
    // módulo escolhido não tem o que mostrar — a tela em branco do /inbox já
    // custou uma sessão de QA.
    if (!LIBERADAS_EM_ONBOARDING.has(caminho)) {
      const cfg = await this.prisma.mantenedoraSettings.findUnique({
        where: { mantenedoraId: user.mantenedoraId },
        select: { onboardingConcluido: true },
      });
      if (!cfg?.onboardingConcluido) {
        throw new ConflictException({
          error: 'A conta ainda está sendo configurada.',
          code: 'ONBOARDING_PENDENTE',
        });
      }
    }

    // CSRF depois da sessão, de propósito: sem cookie válido não há nada que um
    // site de terceiro possa cavalgar, e responder 403 antes do 401 só
    // confundiria quem depura. SameSite=Lax cobre o caso comum; o cabeçalho
    // cobre o que muda estado (ADR-0007 §1).
    this.exigirCabecalhoAntiCsrf(req, mudaEstado);

    req.usuario = {
      id: user.id,
      mantenedoraId: user.mantenedoraId,
      nome: user.name,
      email: user.email,
      precisaTrocarSenha: user.mustChangePassword,
    };
    next();
  }

  private exigirCabecalhoAntiCsrf(req: Request, mudaEstado: boolean): void {
    if (mudaEstado && !req.headers['x-requested-with']) {
      throw new ForbiddenException({ error: 'Requisição sem X-Requested-With.', code: 'CSRF_SUSPEITO' });
    }
  }
}
```

## api-app/src/surfaces/bff/message-templates.controller.ts

```text
import { BadRequestException, Body, Controller, Get, Headers, HttpCode, HttpStatus, Param, Patch, Post, Query, Req, Res, UnauthorizedException } from '@nestjs/common';
import type { Prisma } from '@prisma/client';
import type { Request, Response } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { TemplateDraftService } from '../../domain/message-templates/template-draft.service';
import { TemplateSubmissionService } from '../../domain/message-templates/template-submission.service';
import { TemplateObservationService } from '../../domain/message-templates/template-observation.service';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { SessionService } from '../../infra/session/session.service';

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const DEFINITION_KEYS = ['name', 'language', 'category', 'body', 'header', 'footer', 'examples'];

@Controller('api/bff')
export class MessageTemplatesController {
  constructor(
    private readonly access: AccessService,
    private readonly drafts: TemplateDraftService,
    private readonly submissions: TemplateSubmissionService,
    private readonly observations: TemplateObservationService,
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
  ) {}

  @Get('business-units/:buId/channels/:channelId/message-template-capabilities')
  async capabilities(@Param('buId') buId: string, @Param('channelId') channelId: string, @Req() req: Request) {
    requireUuid(buId); requireUuid(channelId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    return this.drafts.capabilities(req.usuario!.id, buId, channelId);
  }

  @Get('business-units/:buId/message-templates')
  async list(@Param('buId') buId: string, @Query() query: Record<string, string>, @Req() req: Request) {
    requireUuid(buId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    if (Object.keys(query).some((key) => !['view', 'page', 'limit'].includes(key))) throw badRequest();
    const page = query.page === undefined ? undefined : Number(query.page);
    const limit = query.limit === undefined ? undefined : Number(query.limit);
    if ((page !== undefined && (!Number.isSafeInteger(page) || page < 1))
      || (limit !== undefined && (!Number.isSafeInteger(limit) || limit < 1 || limit > 50))) throw badRequest();
    if (query.view !== undefined && query.view !== 'mine' && query.view !== 'bu') throw badRequest();
    return this.drafts.listDrafts(req.usuario!.id, buId, { view: query.view as 'mine' | 'bu' | undefined, page, limit });
  }

  @Post('business-units/:buId/message-templates/preview')
  @HttpCode(HttpStatus.OK)
  async preview(@Param('buId') buId: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    requireUuid(buId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    strictKeys(body, ['channelId', 'expectedGeneration', 'draftId', 'expectedRevision', 'definition']);
    if (typeof body.channelId !== 'string' || typeof body.expectedGeneration !== 'number'
      || !Number.isSafeInteger(body.expectedGeneration) || body.expectedGeneration < 1 || !('definition' in body)) throw badRequest();
    requireUuid(body.channelId);
    return this.drafts.preview(req.usuario!.id, {
      buId, channelId: body.channelId, expectedGeneration: body.expectedGeneration,
      ...(body.draftId === undefined ? {} : { draftId: stringField(body.draftId) }),
      ...(body.expectedRevision === undefined ? {} : { expectedRevision: numberField(body.expectedRevision) }),
      definition: body.definition,
    });
  }

  @Post('business-units/:buId/message-templates')
  async create(@Param('buId') buId: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(buId);
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    strictKeys(body, ['clientRequestId', 'channelId', 'expectedGeneration', ...DEFINITION_KEYS]);
    if (!UUID.test(stringField(body.clientRequestId)) || typeof body.channelId !== 'string'
      || typeof body.expectedGeneration !== 'number' || !Number.isSafeInteger(body.expectedGeneration) || body.expectedGeneration < 1) throw badRequest();
    requireUuid(body.channelId);
    const result = await this.drafts.createDraft(req.usuario!.id, {
      buId, clientRequestId: body.clientRequestId as string, channelId: body.channelId,
      expectedGeneration: body.expectedGeneration as number, definition: definitionFrom(body),
    });
    if ('replayed' in result && result.replayed) res.status(HttpStatus.OK);
    return result;
  }

  @Get('message-templates/:id')
  get(@Param('id') id: string, @Req() req: Request) { requireUuid(id); return this.drafts.getDraftById(req.usuario!.id, id); }

  @Patch('message-templates/:id')
  async save(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    requireUuid(id);
    strictKeys(body, ['expectedRevision', 'definition']);
    if (!('definition' in body)) throw badRequest();
    return this.drafts.saveDraftById(req.usuario!.id, id, numberField(body.expectedRevision), body.definition);
  }

  @Post('message-templates/:id/submit')
  @HttpCode(HttpStatus.CREATED)
  async submit(@Param('id') id: string, @Headers('idempotency-key') key: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(id);
    strictKeys(body, ['expectedRevision', 'expectedGeneration', 'expectedDefinitionFingerprint']);
    if (!UUID.test(key ?? '') || typeof body.expectedDefinitionFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(body.expectedDefinitionFingerprint)) throw badRequest();
    const result = await this.submissions.submitDraft(req.usuario!.id, {
      draftId: id, expectedRevision: numberField(body.expectedRevision),
      expectedGeneration: numberField(body.expectedGeneration),
      expectedDefinitionFingerprint: body.expectedDefinitionFingerprint as string, idempotencyKey: key,
    }, this.authRevalidation(req));
    if (result.phase === 'PREPARED' || result.phase === 'SENDING' || ('recoveryInProgress' in result && result.recoveryInProgress === true)) res.status(HttpStatus.ACCEPTED);
    else if ('replayed' in result && result.replayed === true) res.status(HttpStatus.OK);
    return result;
  }

  @Get('message-templates/:id/operations/:operationId')
  operation(@Param('id') id: string, @Param('operationId') operationId: string, @Req() req: Request) {
    requireUuid(id); requireUuid(operationId);
    return this.submissions.getOperation(req.usuario!.id, id, operationId);
  }

  @Post('message-templates/:id/operations/:operationId/reconcile')
  @HttpCode(HttpStatus.OK)
  async reconcile(@Param('id') id: string, @Param('operationId') operationId: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(id); requireUuid(operationId);
    strictKeys(body ?? {}, []);
    const result = await this.submissions.reconcile(req.usuario!.id, id, operationId, this.authRevalidation(req));
    if ('recoveryInProgress' in result && result.recoveryInProgress === true) res.status(HttpStatus.ACCEPTED);
    return result;
  }

  @Post('message-templates/:id/refresh')
  @HttpCode(HttpStatus.OK)
  async refreshDraft(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(id);
    strictKeys(body ?? {}, []);
    const result = await this.observations.refreshDraft(req.usuario!.id, id, this.authRevalidation(req));
    if ('phase' in result && result.phase === 'REFRESH_IN_PROGRESS') res.status(HttpStatus.ACCEPTED);
    return result;
  }

  @Get('business-units/:buId/channels/:channelId/message-template-catalog')
  async getCatalog(@Param('buId') buId: string, @Param('channelId') channelId: string, @Query() query: Record<string, string>, @Req() req: Request) {
    requireUuid(buId); requireUuid(channelId);
    if (Object.keys(query).some((key) => key !== 'after') || (query.after !== undefined && (typeof query.after !== 'string' || query.after.length < 1 || query.after.length > 512))) throw badRequest();
    return this.observations.getCatalog(req.usuario!.id, buId, channelId, query.after ?? null);
  }

  @Post('business-units/:buId/channels/:channelId/message-template-catalog')
  @HttpCode(HttpStatus.OK)
  async refreshCatalog(@Param('buId') buId: string, @Param('channelId') channelId: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) res: Response) {
    requireUuid(buId); requireUuid(channelId);
    strictKeys(body ?? {}, ['after']);
    const after = body?.after === undefined ? null : stringField(body.after);
    if (after !== null && (after.length < 1 || after.length > 512)) throw badRequest();
    const result = await this.observations.refreshCatalog(req.usuario!.id, buId, channelId, after, this.authRevalidation(req));
    if ('phase' in result && result.phase === 'REFRESH_IN_PROGRESS') res.status(HttpStatus.ACCEPTED);
    return result;
  }

  private authRevalidation(req: Request): (tx?: Prisma.TransactionClient) => Promise<void> {
    const claimsAtRequest = this.sessions.verificar(this.sessions.extrairDoCabecalho(req.headers.cookie));
    if (!claimsAtRequest || claimsAtRequest.uid !== req.usuario!.id) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    return async (tx) => {
      const claims = this.sessions.verificar(this.sessions.extrairDoCabecalho(req.headers.cookie));
      let user: { id: string; status: string; passwordChangedAt: Date | null } | null = null;
      if (claims && claims.uid === claimsAtRequest.uid) {
        if (tx) {
          const rows = await tx.$queryRaw<Array<{ id: string; status: string; passwordChangedAt: Date | null }>>`
            SELECT id, status::text AS status, password_changed_at AS "passwordChangedAt"
            FROM app_users WHERE id = ${claims.uid} FOR UPDATE`;
          user = rows[0] ?? null;
        } else {
          user = await this.prisma.appUser.findUnique({ where: { id: claims.uid }, select: { id: true, status: true, passwordChangedAt: true } });
        }
      }
      if (!claims || claims.uid !== claimsAtRequest.uid || claims.iat !== claimsAtRequest.iat || claims.exp !== claimsAtRequest.exp
        || !user || user.status !== 'ATIVO' || (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat)) {
        throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
      }
    };
  }
}

function strictKeys(value: unknown, allowed: readonly string[]): asserts value is Record<string, unknown> {
  if (!value || typeof value !== 'object' || Array.isArray(value)
    || Object.keys(value).some((key) => !allowed.includes(key))) throw badRequest();
}
function requireUuid(value: unknown): asserts value is string { if (typeof value !== 'string' || !UUID.test(value)) throw badRequest(); }
function stringField(value: unknown): string { if (typeof value !== 'string') throw badRequest(); return value; }
function numberField(value: unknown): number { if (typeof value !== 'number' || !Number.isSafeInteger(value) || value < 1) throw badRequest(); return value; }
function definitionFrom(body: Record<string, unknown>): Record<string, unknown> {
  const definition: Record<string, unknown> = {};
  for (const key of DEFINITION_KEYS) if (key in body) definition[key] = body[key];
  return definition;
}
function badRequest(): BadRequestException { return new BadRequestException({ code: 'TEMPLATE_PAYLOAD_INVALID' }); }
```

## api-app/src/domain/message-templates/template-observation.service.ts

```text
import { ConflictException, ForbiddenException, Inject, Injectable, NotFoundException, ServiceUnavailableException, UnauthorizedException } from '@nestjs/common';
import { Prisma, type MessageTemplateDraft } from '@prisma/client';
import { createHash, randomUUID } from 'node:crypto';
import { AccessService } from '../access/access.service';
import { atLeast, type Role } from '../access/role';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { TEMPLATE_MANAGEMENT_RESOLVER, type TemplateDefinition, type TemplateManagementContext, type TemplateManagementResolver, type TemplateReference, type TemplateSummary } from './template-management.ports';
import { templateDefinitionSemanticFingerprint } from './template-definition';
import { TEMPLATE_TRANSACTION_BOUNDARY, type TemplateTransactionBoundary } from './template-transaction-boundary';

export const TEMPLATE_OBSERVATION_CLOCK = Symbol('TEMPLATE_OBSERVATION_CLOCK');
export interface TemplateObservationClock { now(): Date }
const LEASE_MS = 60_000;
const DEBOUNCE_MS = 10_000;
const FRESH_MS = 300_000;

class ObservationCommitUnconfirmedError extends Error {}
type ObservationAuthRevalidation = (tx: Prisma.TransactionClient) => Promise<void>;

interface ProjectedSavedObservation {
  remoteTemplateId: string;
  status: string;
  name: string | null;
  language: string | null;
  category: string;
  parameterFormat: string;
  components: Prisma.JsonValue;
  supported: boolean;
  semanticFingerprint: string | null;
  available: boolean;
  safeCode: string | undefined;
  observedAt: Date;
  observedFence: string;
  eligible: boolean;
}

export interface TemplateObservationBinding {
  readonly mantenedoraId: string;
  readonly buId: string;
  readonly channelId: string;
  readonly providerResourceIdentityId: string;
  readonly accountReference: string;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
}

@Injectable()
export class TemplateObservationService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly access: AccessService,
    @Inject(TEMPLATE_MANAGEMENT_RESOLVER) private readonly resolver: TemplateManagementResolver,
    @Inject(TEMPLATE_TRANSACTION_BOUNDARY) private readonly transactions: TemplateTransactionBoundary,
    @Inject(TEMPLATE_OBSERVATION_CLOCK) private readonly clock: TemplateObservationClock,
  ) {}

  async refreshDraft(actorId: string, draftId: string, revalidateAuth?: ObservationAuthRevalidation) {
    const { draft } = await this.authorizeDraft(actorId, draftId);
    const reference = await this.currentReference(actorId, draft.buId, draft.channelId);
    const resolved = await this.resolver.resolve(reference);
    this.assertBinding(draft, resolved.context);
    const operation = await this.prisma.messageTemplateOperation.findFirst({
      where: { draftId, buId: draft.buId, mantenedoraId: draft.mantenedoraId },
      orderBy: [{ revision: 'desc' }], select: { remoteTemplateId: true, acknowledgedRemoteTemplateId: true, phase: true },
    });
    if (!operation?.remoteTemplateId || !['ACCEPTED', 'AMBIGUOUS'].includes(operation.phase)) {
      throw new ConflictException({ code: 'TEMPLATE_REMOTE_ID_UNAVAILABLE' });
    }
    const lease = await this.acquire(resolved.context);
    if (!lease.acquired) return { phase: 'REFRESH_IN_PROGRESS', retryAfter: 10 };
    try {
      const summary = await resolved.provider.getTemplate({ context: resolved.context, remoteTemplateId: operation.remoteTemplateId });
      const applied = await this.applyObservation(actorId, resolved.context, lease, summary, draftId, revalidateAuth);
      if (!applied) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      const projected = await this.projectObservation(resolved.context, summary.remoteTemplateId, draft.definition);
      if (operation.acknowledgedRemoteTemplateId && operation.acknowledgedRemoteTemplateId !== operation.remoteTemplateId) {
        return { ...projected, eligible: false, eligibleForUse: false, safeCode: 'PROVIDER_ACK_CONFLICT' };
      }
      return projected;
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      if (error instanceof ConflictException && error.getResponse() && (error.getResponse() as { code?: string }).code === 'TEMPLATE_REFRESH_SUPERSEDED') throw error;
      if (error instanceof ObservationCommitUnconfirmedError) throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      if (!await this.markUnavailableSafely(actorId, resolved.context, lease, operation.remoteTemplateId, null, 'TEMPLATE_REFRESH_UNAVAILABLE', undefined, revalidateAuth, draftId)) {
        throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      }
      throw new ConflictException({ code: 'TEMPLATE_REFRESH_UNAVAILABLE' });
    }
  }

  async refreshCatalog(actorId: string, buId: string, channelId: string, after: string | null, revalidateAuth?: ObservationAuthRevalidation) {
    await this.authorizeBu(actorId, buId);
    const currentReference = await this.currentReference(actorId, buId, channelId);
    const resolved = await this.resolver.resolve(currentReference);
    const lease = await this.acquire(resolved.context);
    if (!lease.acquired) return { phase: 'REFRESH_IN_PROGRESS', retryAfter: 10 };
    const cursorHash = this.hash(after ?? 'first-page');
    try {
      const page = await resolved.provider.listTemplates({ context: resolved.context, after, limit: 50 });
      const applied = await this.applyCatalogPage(actorId, resolved.context, lease, cursorHash, after, page.templates, page.nextCursor, revalidateAuth);
      if (!applied) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      return this.getCatalog(actorId, buId, channelId, after);
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      if (error instanceof ConflictException && error.getResponse() && (error.getResponse() as { code?: string }).code === 'TEMPLATE_REFRESH_SUPERSEDED') throw error;
      if (error instanceof ObservationCommitUnconfirmedError) throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      if (!await this.markUnavailableSafely(actorId, resolved.context, lease, null, cursorHash, 'TEMPLATE_CATALOG_UNAVAILABLE', after, revalidateAuth)) {
        throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
      }
      throw new ConflictException({ code: 'TEMPLATE_CATALOG_UNAVAILABLE' });
    }
  }

  async getCatalog(actorId: string, buId: string, channelId: string, after: string | null) {
    await this.authorizeBu(actorId, buId);
    const currentReference = await this.currentReference(actorId, buId, channelId);
    const resolved = await this.resolver.resolve(currentReference);
    const cursorHash = this.hash(after ?? 'first-page');
    const page = await this.prisma.messageTemplateCatalogPage.findUnique({ where: { contextKey_cursorHash: { contextKey: this.contextKey(resolved.context), cursorHash } } });
    if (!page) return { items: [], nextCursor: null, available: false, safeCode: 'TEMPLATE_CATALOG_NOT_OBSERVED', observedAt: null };
    const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
    if (ids.length > 50) return { items: [], nextCursor: null, available: false,
      safeCode: 'TEMPLATE_CATALOG_INVALID', observedAt: page.observedAt };
    const rows = ids.length ? await this.prisma.$queryRaw<Array<{
      remoteTemplateId: string; status: string; name: string | null; language: string | null; category: string;
      parameterFormat: string; components: Prisma.JsonValue; supported: boolean; semanticFingerprint: string | null;
      available: boolean; safeCode: string | null; observedEligible: boolean; observedAt: Date; observedFence: bigint;
    }>>(Prisma.sql`
      WITH requested AS (
        SELECT remote_template_id, ordinality
        FROM unnest(ARRAY[${Prisma.join(ids)}]::varchar(128)[]) WITH ORDINALITY AS request(remote_template_id, ordinality)
      )
      SELECT observation.remote_template_id AS "remoteTemplateId", observation.status, observation.name, observation.language, observation.category,
        observation.parameter_format AS "parameterFormat", observation.components, observation.supported,
        observation.semantic_fingerprint AS "semanticFingerprint", observation.available, observation.safe_code AS "safeCode",
        observation.observed_eligible AS "observedEligible", observation.observed_at AS "observedAt", observation.observed_fence AS "observedFence"
      FROM requested
      CROSS JOIN LATERAL (
        SELECT remote_template_id, status, name, language, category, parameter_format, components, supported,
          semantic_fingerprint, available, safe_code, observed_eligible, observed_at, observed_fence
        FROM message_template_remote_observations
        WHERE context_key = ${page.contextKey}::char(64)
          AND remote_template_id = requested.remote_template_id
        LIMIT 1
      ) observation
      ORDER BY requested.ordinality`) : [];
    const byId = new Map(rows.map((row) => [row.remoteTemplateId, row]));
    const fresh = this.clock.now().getTime() - page.observedAt.getTime() <= FRESH_MS;
    return { items: ids.flatMap((id) => { const row = byId.get(id); return row ? [this.projectRow(row)] : []; }),
      nextCursor: page.nextCursor, available: page.available && fresh, safeCode: page.safeCode ?? (!fresh ? 'TEMPLATE_CATALOG_STALE' : undefined), observedAt: page.observedAt };
  }

  async projectSavedObservation(binding: TemplateObservationBinding, remoteTemplateId: string,
    definitionValue: unknown, acknowledgedRemoteTemplateId?: string | null): Promise<(ProjectedSavedObservation & { matchesDefinition: boolean; eligibleForUse: boolean }) | null> {
    const historicalContextKey = this.hash({ mantenedoraId: binding.mantenedoraId, buId: binding.buId,
      channelId: binding.channelId, accountReference: binding.accountReference,
      generation: binding.generation, pairingEpoch: binding.pairingEpoch,
      providerResourceIdentityId: binding.providerResourceIdentityId,
      activeCredentialVersion: binding.activeCredentialVersion });
    let currentContext: TemplateManagementContext | null = null;
    try {
      const channel = await this.prisma.buChannel.findFirst({ where: { id: binding.channelId, buId: binding.buId }, select: { generation: true } });
      if (channel) {
        const resolved = await this.resolver.resolve({ buId: binding.buId, channelId: binding.channelId, expectedGeneration: channel.generation });
        const sameResourceAssociation = resolved.context.mantenedoraId === binding.mantenedoraId
          && resolved.context.buId === binding.buId && resolved.context.channelId === binding.channelId
          && resolved.context.providerResourceIdentityId === binding.providerResourceIdentityId
          && resolved.context.accountReference === binding.accountReference;
        if (sameResourceAssociation) currentContext = resolved.context;
      }
    } catch { /* historical detail remains readable, but a stale binding cannot be eligible */ }

    const currentContextKey = currentContext ? this.contextKey(currentContext) : null;
    const currentRow = currentContextKey ? await this.prisma.messageTemplateRemoteObservation.findUnique({
      where: { contextKey_remoteTemplateId: { contextKey: currentContextKey, remoteTemplateId } },
    }) : null;
    const row = currentRow ?? (currentContextKey === historicalContextKey ? null
      : await this.prisma.messageTemplateRemoteObservation.findUnique({
        where: { contextKey_remoteTemplateId: { contextKey: historicalContextKey, remoteTemplateId } },
      }));
    if (!row) return null;
    const currentObservation = currentRow !== null;

    let matchesDefinition = false;
    try { matchesDefinition = row.semanticFingerprint !== null
      && row.semanticFingerprint === this.definitionFingerprint(definitionValue as TemplateDefinition); }
    catch { /* unsupported historical definitions cannot be considered a match */ }
    const projected = this.projectRow(row);
    const available = currentObservation && projected.available;
    const ackMatchesAssociation = !acknowledgedRemoteTemplateId || acknowledgedRemoteTemplateId === remoteTemplateId;
    const eligible = available && matchesDefinition && ackMatchesAssociation && row.supported && row.status === 'APPROVED';
    return { ...projected, available, eligible,
      ...(!currentObservation ? { safeCode: 'TEMPLATE_CONTEXT_STALE' }
        : !ackMatchesAssociation ? { safeCode: 'PROVIDER_ACK_CONFLICT' } : {}),
      matchesDefinition, eligibleForUse: eligible };
  }

  private async acquire(context: TemplateManagementContext): Promise<{ acquired: boolean; ownerId: string; fence: bigint; contextKey: string }> {
    const contextKey = this.contextKey(context);
    const ownerId = randomUUID();
    try { return await this.transactions.run('observation', async (tx) => {
      const now = this.clock.now();
      await tx.messageTemplateObservationLease.createMany({ data: [{
        contextKey, mantenedoraId: context.mantenedoraId, buId: context.buId,
        channelId: context.channelId, accountReference: context.accountReference,
        channelGeneration: context.generation, pairingEpoch: context.pairingEpoch,
        providerResourceIdentityId: context.providerResourceIdentityId,
        activeCredentialVersion: context.activeCredentialVersion ?? 0, fence: 0n,
      }], skipDuplicates: true });
      const current = await tx.messageTemplateObservationLease.findUniqueOrThrow({ where: { contextKey } });
      const debounceDone = !current.lastStartedAt || current.lastStartedAt.getTime() <= now.getTime() - DEBOUNCE_MS;
      const updated = debounceDone ? await tx.messageTemplateObservationLease.updateMany({
        where: { contextKey, lastStartedAt: current.lastStartedAt, OR: [{ leaseUntil: null }, { leaseUntil: { lte: now } }] },
        data: { ownerId, fence: { increment: 1n }, leaseUntil: new Date(now.getTime() + LEASE_MS), lastStartedAt: now },
      }) : { count: 0 };
      const latest = await tx.messageTemplateObservationLease.findUniqueOrThrow({ where: { contextKey } });
      return { acquired: updated.count === 1, ownerId, fence: latest.fence, contextKey };
    }); } catch (error) {
      if (error instanceof ConflictException) throw error;
      throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
    }
  }

  private async applyObservation(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, summary: TemplateSummary, draftId: string, revalidateAuth?: ObservationAuthRevalidation): Promise<boolean> {
    const observedAt = this.clock.now();
    try {
      return await this.transactions.run('observation', async (tx) => {
        await revalidateAuth?.(tx);
        await this.assertTxObservationAccess(tx, actorId, context, draftId);
        if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
        await this.writeObservation(tx, lease, observedAt, summary);
        await this.releaseLease(tx, lease);
        return true;
      });
    } catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      try { if (await this.observationCommitted(lease, observedAt, summary)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async applyCatalogPage(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, cursorHash: string, after: string | null, summaries: readonly TemplateSummary[], nextCursor: string | null, revalidateAuth?: ObservationAuthRevalidation): Promise<boolean> {
    const observedAt = this.clock.now();
    try { return await this.transactions.run('observation', async (tx) => {
      await revalidateAuth?.(tx);
      await this.assertTxObservationAccess(tx, actorId, context);
      if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
      const remoteTemplateIds = summaries.map((summary) => summary.remoteTemplateId);
      for (const summary of summaries) await this.writeObservation(tx, lease, observedAt, summary);
      await tx.messageTemplateCatalogPage.upsert({
        where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
        create: { contextKey: lease.contextKey, cursorHash, requestedCursor: after, remoteTemplateIds: remoteTemplateIds as Prisma.InputJsonValue,
          nextCursor, available: true, safeCode: null, observedAt, observedFence: lease.fence },
        update: { requestedCursor: after, remoteTemplateIds: remoteTemplateIds as Prisma.InputJsonValue, nextCursor,
          available: true, safeCode: null, observedAt, observedFence: lease.fence },
      });
      await this.releaseLease(tx, lease);
      return true;
    }); } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      try { if (await this.catalogPageCommitted(lease, cursorHash, observedAt, summaries, nextCursor)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async writeObservation(tx: Prisma.TransactionClient, lease: { fence: bigint; contextKey: string }, observedAt: Date, summary: TemplateSummary): Promise<void> {
    const observedEligible = summary.supported && summary.status === 'APPROVED';
    await tx.messageTemplateRemoteObservation.upsert({
      where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId } },
      create: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId, status: summary.status,
        name: summary.name, language: summary.language, category: summary.category, parameterFormat: summary.parameterFormat,
        components: summary.components as unknown as Prisma.InputJsonValue, semanticFingerprint: summary.semanticFingerprint,
        supported: summary.supported, available: true, safeCode: null, observedEligible, observedAt, observedFence: lease.fence },
      update: { status: summary.status, name: summary.name, language: summary.language, category: summary.category,
        parameterFormat: summary.parameterFormat, components: summary.components as unknown as Prisma.InputJsonValue,
        semanticFingerprint: summary.semanticFingerprint, supported: summary.supported, available: true,
        safeCode: null, observedEligible, observedAt, observedFence: lease.fence },
    });
  }

  private async observationCommitted(lease: { fence: bigint; contextKey: string }, observedAt: Date, summary: TemplateSummary): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    const row = await this.prisma.messageTemplateRemoteObservation.findUnique({
      where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: summary.remoteTemplateId } },
      select: { observedAt: true, observedFence: true, semanticFingerprint: true, available: true,
        status: true, name: true, language: true, category: true, parameterFormat: true, components: true, supported: true },
    });
    return Boolean(row && row.observedFence === lease.fence && row.observedAt.getTime() === observedAt.getTime()
      && row.semanticFingerprint === summary.semanticFingerprint && row.available
      && this.sameSummary(row, summary));
  }

  private async catalogPageCommitted(lease: { fence: bigint; contextKey: string }, cursorHash: string, observedAt: Date, summaries: readonly TemplateSummary[], nextCursor: string | null): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    const page = await this.prisma.messageTemplateCatalogPage.findUnique({
      where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
      select: { observedAt: true, observedFence: true, available: true, nextCursor: true, remoteTemplateIds: true },
    });
    if (!page || page.observedFence !== lease.fence || page.observedAt.getTime() !== observedAt.getTime()
      || !page.available || page.nextCursor !== nextCursor) return false;
    const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds : [];
    if (ids.length !== summaries.length || !summaries.every((summary, i) => ids[i] === summary.remoteTemplateId)) return false;
    if (!ids.length) return true;
    const rows = await this.prisma.messageTemplateRemoteObservation.findMany({
      where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids as string[] }, observedFence: lease.fence, observedAt, available: true },
      select: { remoteTemplateId: true, status: true, name: true, language: true, category: true,
        parameterFormat: true, components: true, supported: true, semanticFingerprint: true },
    });
    const byId = new Map(rows.map((row) => [row.remoteTemplateId, row]));
    return rows.length === ids.length && summaries.every((summary) => {
      const row = byId.get(summary.remoteTemplateId);
      return Boolean(row && row.semanticFingerprint === summary.semanticFingerprint && this.sameSummary(row, summary));
    });
  }

  private async markUnavailable(actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, remoteId: string | null, cursorHash: string | null, safeCode: string, requestedCursor: string | null = null, revalidateAuth?: ObservationAuthRevalidation, draftId?: string): Promise<boolean> {
    const observedAt = this.clock.now();
    try { return await this.transactions.run('observation', async (tx) => {
      await revalidateAuth?.(tx);
      await this.assertTxObservationAccess(tx, actorId, context, draftId);
      if (!await this.ownsLease(tx, actorId, context, lease, observedAt)) return false;
      if (remoteId) await tx.messageTemplateRemoteObservation.updateMany({
        where: { contextKey: lease.contextKey, remoteTemplateId: remoteId },
        data: { available: false, observedEligible: false, safeCode, observedFence: lease.fence },
      });
      if (cursorHash) {
        const page = await tx.messageTemplateCatalogPage.findUnique({ where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } }, select: { remoteTemplateIds: true } });
        const ids = Array.isArray(page?.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
        if (ids.length) await tx.messageTemplateRemoteObservation.updateMany({
          where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids } },
          data: { available: false, observedEligible: false, safeCode, observedFence: lease.fence },
        });
        await tx.messageTemplateCatalogPage.upsert({
          where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
          create: { contextKey: lease.contextKey, cursorHash, requestedCursor,
            remoteTemplateIds: [] as unknown as Prisma.InputJsonValue, nextCursor: null,
            available: false, safeCode, observedAt, observedFence: lease.fence },
          update: { available: false, safeCode, observedFence: lease.fence },
        });
      }
      await this.releaseLease(tx, lease);
      return true;
    }); } catch (error) {
      if (this.isAuthOrAccessFailure(error)) { await this.releaseLeaseAfterAuthorizationFailure(lease); throw error; }
      try { if (await this.unavailableCommitted(lease, remoteId, cursorHash, safeCode)) return true; }
      catch { throw new ObservationCommitUnconfirmedError(); }
      throw new ObservationCommitUnconfirmedError();
    }
  }

  private async markUnavailableSafely(actorId: string, context: TemplateManagementContext,
    lease: { ownerId: string; fence: bigint; contextKey: string }, remoteId: string | null,
    cursorHash: string | null, safeCode: string, requestedCursor: string | null = null,
    revalidateAuth?: ObservationAuthRevalidation, draftId?: string): Promise<boolean> {
    try { return await this.markUnavailable(actorId, context, lease, remoteId, cursorHash, safeCode, requestedCursor, revalidateAuth, draftId); }
    catch (error) {
      if (this.isAuthOrAccessFailure(error)) throw error;
      if (error instanceof ObservationCommitUnconfirmedError) {
        throw new ServiceUnavailableException({ code: 'TEMPLATE_OBSERVATION_LOCAL_INCOMPLETE' });
      }
      throw error;
    }
  }

  private async releaseLeaseAfterAuthorizationFailure(lease: { ownerId: string; fence: bigint; contextKey: string }): Promise<void> {
    try { await this.transactions.run('observation', (tx) => this.releaseLease(tx, lease)); }
    catch { /* authorization response remains authoritative; the bounded lease expires if cleanup cannot be confirmed */ }
  }

  private async unavailableCommitted(lease: { fence: bigint; contextKey: string }, remoteId: string | null, cursorHash: string | null, safeCode: string): Promise<boolean> {
    const currentLease = await this.prisma.messageTemplateObservationLease.findUnique({ where: { contextKey: lease.contextKey }, select: { fence: true, ownerId: true, leaseUntil: true } });
    if (currentLease?.fence !== lease.fence || currentLease.ownerId !== null || currentLease.leaseUntil !== null) return false;
    if (remoteId) {
      const row = await this.prisma.messageTemplateRemoteObservation.findUnique({
        where: { contextKey_remoteTemplateId: { contextKey: lease.contextKey, remoteTemplateId: remoteId } },
        select: { available: true, safeCode: true, observedFence: true },
      });
      return Boolean(row && !row.available && row.safeCode === safeCode && row.observedFence === lease.fence);
    }
    if (cursorHash) {
      const page = await this.prisma.messageTemplateCatalogPage.findUnique({
        where: { contextKey_cursorHash: { contextKey: lease.contextKey, cursorHash } },
        select: { available: true, safeCode: true, observedFence: true, remoteTemplateIds: true },
      });
      if (!page || page.available || page.safeCode !== safeCode || page.observedFence !== lease.fence) return false;
      const ids = Array.isArray(page.remoteTemplateIds) ? page.remoteTemplateIds.filter((id): id is string => typeof id === 'string') : [];
      if (!ids.length) return true;
      const rows = await this.prisma.messageTemplateRemoteObservation.findMany({
        where: { contextKey: lease.contextKey, remoteTemplateId: { in: ids }, available: false, safeCode, observedFence: lease.fence },
        select: { remoteTemplateId: true },
      });
      return rows.length === ids.length;
    }
    return false;
  }

  private sameSummary(row: { status: string; name: string | null; language: string | null; category: string;
    parameterFormat: string; components: Prisma.JsonValue; supported: boolean }, summary: TemplateSummary): boolean {
    return row.status === summary.status && row.name === summary.name && row.language === summary.language
      && row.category === summary.category && row.parameterFormat === summary.parameterFormat
      && row.supported === summary.supported
      && JSON.stringify(row.components) === JSON.stringify(summary.components);
  }

  private async ownsLease(tx: Prisma.TransactionClient, actorId: string, context: TemplateManagementContext, lease: { ownerId: string; fence: bigint; contextKey: string }, now: Date): Promise<boolean> {
    const lock = await tx.$queryRaw<Array<{ contextKey: string }>>`SELECT context_key AS "contextKey" FROM message_template_observation_leases WHERE context_key = ${lease.contextKey} FOR UPDATE`;
    if (lock.length !== 1) return false;
    const current = await tx.messageTemplateObservationLease.findFirst({ where: {
      contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: now },
      mantenedoraId: context.mantenedoraId, buId: context.buId, channelId: context.channelId, accountReference: context.accountReference,
      channelGeneration: context.generation, pairingEpoch: context.pairingEpoch,
      providerResourceIdentityId: context.providerResourceIdentityId, activeCredentialVersion: context.activeCredentialVersion ?? 0,
    }, select: { contextKey: true } });
    if (!current) return false;
    // Pin all mutable inputs while resolver rechecks the same transaction snapshot.
    await tx.$queryRaw`SELECT id FROM app_users WHERE id = ${actorId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${context.buId} AND mantenedora_id = ${context.mantenedoraId} FOR UPDATE`;
    await tx.$queryRaw`SELECT user_id FROM user_bu_roles WHERE user_id = ${actorId} AND bu_id = ${context.buId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${context.channelId} AND bu_id = ${context.buId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.providerResourceIdentityId} AND current_channel_id = ${context.channelId} FOR UPDATE`;
    await tx.$queryRaw`SELECT channel_id FROM channel_credentials WHERE channel_id = ${context.channelId} FOR UPDATE`;
    const checkedAt = this.clock.now();
    const stillOwned = await tx.messageTemplateObservationLease.findFirst({ where: {
      contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: checkedAt },
    }, select: { contextKey: true } });
    if (!stillOwned) return false;
    const [actor, bu, grant] = await Promise.all([
      tx.appUser.findFirst({ where: { id: actorId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.businessUnit.findFirst({ where: { id: context.buId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.userBuRole.findUnique({ where: { userId_buId: { userId: actorId, buId: context.buId } }, select: { userId: true } }),
    ]);
    if (!actor || !bu || !grant) return false;
    try {
      const actual = await this.resolver.resolve({ buId: context.buId, channelId: context.channelId, expectedGeneration: context.generation }, { transaction: tx });
      return this.sameContext(context, actual.context);
    } catch { return false; }
  }

  private async releaseLease(tx: Prisma.TransactionClient, lease: { ownerId: string; fence: bigint; contextKey: string }): Promise<void> {
    const checkedAt = this.clock.now();
    const released = await tx.messageTemplateObservationLease.updateMany({ where: { contextKey: lease.contextKey, ownerId: lease.ownerId, fence: lease.fence, leaseUntil: { gt: checkedAt } }, data: { ownerId: null, leaseUntil: null } });
    if (released.count !== 1) throw new ConflictException({ code: 'TEMPLATE_REFRESH_SUPERSEDED' });
  }

  private async projectObservation(context: TemplateManagementContext, remoteId: string, definitionValue: Prisma.JsonValue) {
    const row = await this.prisma.messageTemplateRemoteObservation.findUnique({ where: { contextKey_remoteTemplateId: { contextKey: this.contextKey(context), remoteTemplateId: remoteId } } });
    if (!row) throw new ConflictException({ code: 'TEMPLATE_REFRESH_UNAVAILABLE' });
    const definition = definitionValue as unknown as TemplateDefinition;
    const current = row.semanticFingerprint !== null && row.semanticFingerprint === this.definitionFingerprint(definition);
    return { ...this.projectRow(row), matchesDefinition: current,
      eligibleForUse: current && row.available && row.supported && row.status === 'APPROVED'
        && this.clock.now().getTime() - row.observedAt.getTime() <= FRESH_MS };
  }

  private projectRow(row: { remoteTemplateId: string; status: string; name: string | null; language: string | null; category: string; parameterFormat: string; components: Prisma.JsonValue; supported: boolean; semanticFingerprint: string | null; available: boolean; safeCode: string | null; observedEligible: boolean; observedAt: Date; observedFence: bigint }): ProjectedSavedObservation {
    const current = this.clock.now().getTime() - row.observedAt.getTime() <= FRESH_MS;
    return { remoteTemplateId: row.remoteTemplateId, status: row.status, name: row.name, language: row.language,
      category: row.category, parameterFormat: row.parameterFormat, components: row.components,
      supported: row.supported, semanticFingerprint: row.semanticFingerprint,
      available: row.available && current, safeCode: row.safeCode ?? undefined,
      observedAt: row.observedAt, observedFence: row.observedFence.toString(),
      eligible: row.available && current && row.observedEligible && row.supported && row.status === 'APPROVED' };
  }

  private async authorizeDraft(actorId: string, draftId: string) {
    const actor = await this.prisma.appUser.findUnique({ where: { id: actorId }, select: { mantenedoraId: true, status: true } });
    if (!actor || actor.status !== 'ATIVO') throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
    const grants = await this.access.grantsDoUsuario(actorId);
    const draft = await this.prisma.messageTemplateDraft.findFirst({ where: { id: draftId, mantenedoraId: actor.mantenedoraId, buId: { in: grants.map((grant) => grant.buId) } } });
    const grant = draft && grants.find((row) => row.buId === draft.buId);
    if (!draft || !grant || (draft.creatorUserId !== actorId && !atLeast(grant.role, 'ADMIN'))) throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
    return { draft, role: grant.role as Role };
  }

  private async assertTxObservationAccess(tx: Prisma.TransactionClient, actorId: string,
    context: TemplateManagementContext, draftId?: string): Promise<void> {
    const [actor, bu, grants] = await Promise.all([
      tx.appUser.findFirst({ where: { id: actorId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.businessUnit.findFirst({ where: { id: context.buId, mantenedoraId: context.mantenedoraId, status: 'ATIVO' }, select: { id: true } }),
      tx.$queryRaw<Array<{ role: Role }>>`SELECT role::text AS role FROM user_bu_roles
        WHERE user_id = ${actorId} AND bu_id = ${context.buId} FOR SHARE`,
    ]);
    if (!actor) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    if (!bu) throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    const role = grants[0]?.role;
    if (!role) throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
    if (draftId) {
      const draft = await tx.messageTemplateDraft.findFirst({ where: {
        id: draftId, buId: context.buId, mantenedoraId: context.mantenedoraId,
        channelId: context.channelId, providerResourceIdentityId: context.providerResourceIdentityId,
        accountReference: context.accountReference,
      }, select: { creatorUserId: true } });
      if (!draft) throw new NotFoundException({ code: 'TEMPLATE_DRAFT_NOT_FOUND' });
      if (draft.creatorUserId !== actorId && !atLeast(role, 'ADMIN')) {
        throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
      }
    } else if (!atLeast(role, 'ATENDENTE')) {
      throw new ForbiddenException({ code: 'TEMPLATE_AUTHORIZATION_CHANGED' });
    }
  }

  private isAuthOrAccessFailure(error: unknown): boolean {
    return error instanceof UnauthorizedException || error instanceof ForbiddenException || error instanceof NotFoundException;
  }

  private async authorizeBu(actorId: string, buId: string): Promise<void> {
    const scoped = await this.access.resolverBu(actorId, buId);
    const actor = await this.prisma.appUser.findUnique({ where: { id: actorId }, select: { mantenedoraId: true, status: true } });
    const bu = await this.prisma.businessUnit.findUnique({ where: { id: buId }, select: { mantenedoraId: true, status: true } });
    if (!scoped || !actor || actor.status !== 'ATIVO' || !bu || bu.status !== 'ATIVO' || actor.mantenedoraId !== bu.mantenedoraId) {
      throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    }
  }

  private assertBinding(draft: MessageTemplateDraft, context: TemplateManagementContext): void {
    if (draft.mantenedoraId !== context.mantenedoraId || draft.channelId !== context.channelId || draft.providerResourceIdentityId !== context.providerResourceIdentityId) throw new ConflictException({ code: 'TEMPLATE_CHANNEL_CONTEXT_STALE' });
    if (draft.accountReference !== context.accountReference) throw new ConflictException({ code: 'CONTA_ALTERADA' });
  }

  private sameContext(a: TemplateManagementContext, b: TemplateManagementContext): boolean {
    return a.mantenedoraId === b.mantenedoraId && a.buId === b.buId && a.channelId === b.channelId && a.accountReference === b.accountReference
      && a.providerResourceIdentityId === b.providerResourceIdentityId && a.generation === b.generation
      && a.pairingEpoch === b.pairingEpoch && a.activeCredentialVersion === b.activeCredentialVersion;
  }

  private async currentReference(actorId: string, buId: string, channelId: string): Promise<TemplateReference> {
    await this.authorizeBu(actorId, buId);
    const channel = await this.prisma.buChannel.findFirst({ where: { id: channelId, buId }, select: { generation: true } });
    if (!channel) throw new NotFoundException({ code: 'TEMPLATE_CHANNEL_NOT_FOUND' });
    return { buId, channelId, expectedGeneration: channel.generation };
  }
  private contextKey(context: TemplateManagementContext): string { return this.hash({ mantenedoraId: context.mantenedoraId, buId: context.buId, channelId: context.channelId, accountReference: context.accountReference, generation: context.generation, pairingEpoch: context.pairingEpoch, providerResourceIdentityId: context.providerResourceIdentityId, activeCredentialVersion: context.activeCredentialVersion }); }
  private hash(value: unknown): string { return createHash('sha256').update(this.canonicalJson(value)).digest('hex'); }
  private canonicalJson(value: unknown): string {
    if (Array.isArray(value)) return `[${value.map((item) => this.canonicalJson(item)).join(',')}]`;
    if (value && typeof value === 'object') {
      const row = value as Record<string, unknown>;
      return `{${Object.keys(row).filter((key) => key !== 'example').sort().map((key) => `${JSON.stringify(key)}:${this.canonicalJson(row[key])}`).join(',')}}`;
    }
    return JSON.stringify(value) ?? 'null';
  }
  private definitionFingerprint(definition: TemplateDefinition): string {
    return templateDefinitionSemanticFingerprint(definition);
  }
}
```

## api-app/src/domain/message-templates/template-transaction-boundary.ts

```text
import { Injectable } from '@nestjs/common';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';

export type TemplateTransactionPhase = 'actor-admission' | 'reserve' | 'claim' | 'record-outcome' | 'release' | 'reconcile-claim' | 'reconcile-release' | 'observation';
export const TEMPLATE_TRANSACTION_BOUNDARY = Symbol('TEMPLATE_TRANSACTION_BOUNDARY');

/** A fault-injectable boundary that always delegates to a real Prisma transaction. */
export interface TemplateTransactionBoundary {
  run<T>(phase: TemplateTransactionPhase, work: (tx: Prisma.TransactionClient) => Promise<T>): Promise<T>;
}

@Injectable()
export class PrismaTemplateTransactionBoundary implements TemplateTransactionBoundary {
  constructor(private readonly prisma: PrismaService) {}

  run<T>(_phase: TemplateTransactionPhase, work: (tx: Prisma.TransactionClient) => Promise<T>): Promise<T> {
    return this.prisma.$transaction(work);
  }
}
```

## api-app/src/integrations/message-templates/template-management.resolver.ts

```text
import { ConflictException, Injectable } from '@nestjs/common';
import { createHash } from 'node:crypto';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver } from '../../domain/channels/channel-credential-resolver';
import type {
  MessageTemplateProvider,
  ResolvedTemplateManagement,
  TemplateAccountReference,
  TemplateManagementContext,
  TemplateManagementResolver,
  TemplateReference,
} from '../../domain/message-templates/template-management.ports';
import { BoundMetaMessageTemplateProvider, MetaTemplateClient, TemplateManagementProviderError } from '../meta/message-template.client';

interface TemplateProviderFactory {
  create(context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider;
}

class OfficialTemplateProviderFactory implements TemplateProviderFactory {
  create(context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider {
    return new BoundMetaMessageTemplateProvider(context, credential, wabaId, new MetaTemplateClient());
  }
}

/** Explicit allowlist: unsupported origins have no placeholder/no-op provider. */
class TemplateProviderFactoryRegistry {
  private readonly factories = new Map([['OFICIAL', new OfficialTemplateProviderFactory()]]);

  create(origin: string, context: TemplateManagementContext, credential: () => Promise<string>, wabaId: string): MessageTemplateProvider {
    const factory = this.factories.get(origin);
    if (!factory) throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    return factory.create(context, credential, wabaId);
  }
}

@Injectable()
export class ScopedTemplateManagementResolver implements TemplateManagementResolver {
  private readonly factories = new TemplateProviderFactoryRegistry();

  constructor(private readonly prisma: PrismaService, private readonly credentials: ChannelCredentialResolver) {}

  async resolve(reference: TemplateReference, options?: { readonly transaction?: Prisma.TransactionClient }): Promise<ResolvedTemplateManagement> {
    const database = options?.transaction ?? this.prisma;
    const channel = await database.buChannel.findFirst({
      where: { id: reference.channelId, buId: reference.buId },
      include: { providerIdentities: true, bu: { select: { mantenedoraId: true } } },
    });
    if (!channel || channel.generation !== reference.expectedGeneration || channel.type !== 'OFICIAL'
      || !channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const identity = channel.providerIdentities.find((row) => row.currentChannelId === channel.id);
    if (!identity || !identity.managedLifecycle || identity.provider !== 'OFICIAL' || identity.buId !== channel.buId
      || !channel.phoneNumberId || identity.externalResourceId !== channel.phoneNumberId || !channel.wabaId) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const credentialMetadata = await this.credentials.inspectActiveCredential(channel.id, channel.generation, { provider: 'OFICIAL', buId: channel.buId }, options?.transaction);
    if (!credentialMetadata.ready || credentialMetadata.version === null) {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const context: TemplateManagementContext = Object.freeze({
      mantenedoraId: channel.bu.mantenedoraId,
      buId: channel.buId,
      channelId: channel.id,
      providerResourceIdentityId: identity.id,
      generation: channel.generation,
      pairingEpoch: channel.pairingEpoch,
      activeCredentialVersion: credentialMetadata.version,
      accountReference: this.accountReference(channel.wabaId),
    });
    const credential = async (): Promise<string> => {
      const current = await this.credentials.resolve(channel.id, 'template-management');
      if (current.provider !== 'OFICIAL' || current.buId !== context.buId || current.channelId !== context.channelId
        || current.providerResourceIdentityId !== context.providerResourceIdentityId || current.generation !== context.generation
        || current.pairingEpoch !== context.pairingEpoch || current.activeCredentialVersion !== context.activeCredentialVersion
        || current.wabaId !== channel.wabaId || current.phoneNumberId !== channel.phoneNumberId
        || this.accountReference(current.wabaId ?? '') !== context.accountReference || !current.accessToken) {
        throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
      }
      return current.accessToken;
    };
    const provider = this.factories.create(channel.type, context, credential, channel.wabaId);
    return Object.freeze({ context, provider });
  }

  private accountReference(wabaId: string): TemplateAccountReference {
    return createHash('sha256').update(`meta-waba\0${wabaId}`).digest('hex') as TemplateAccountReference;
  }
}
```

## api-app/src/integrations/meta/message-template.client.ts

```text
import { createHash } from 'node:crypto';
import type {
  MessageTemplateProvider,
  TemplateComponentSummary,
  TemplateCreateOutcome,
  TemplateDefinition,
  TemplateDispatchGuard,
  TemplateManagementContext,
  TemplatePage,
  TemplateSummary,
} from '../../domain/message-templates/template-management.ports';

const PROVEN_REFUSAL_CODES = new Set([10, 100, 190, 2388040, 2388047, 2388072, 2388073, 2388293, 2388299]);
const PROVIDER_FIELDS = 'id,name,language,status,category,parameter_format,components';
const OPERATION_BUDGET_MS = 45_000;
const MAX_PROVIDER_RESPONSE_BYTES = 1024 * 1024;

export class TemplateManagementProviderError extends Error {
  constructor(readonly code: 'TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE' | 'TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE') {
    super(code === 'TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE'
      ? 'A autorização atual não permite gerenciar modelos.'
      : 'A resposta do provedor de modelos está indisponível.');
    this.name = 'TemplateManagementProviderError';
  }
}

type GraphError = { readonly type: string; readonly message: string; readonly code: number; readonly is_transient?: boolean };
type Grant = { readonly appId: string; readonly valid: boolean; readonly expiresAt?: number; readonly scopes: readonly string[]; readonly targets: readonly string[] };

class RequestNotDispatchedError extends Error {}

/** Private, operation-scoped Graph client. One instance belongs to one resolved context. */
export class MetaTemplateClient {
  private readonly appId = process.env.META_APP_ID?.trim() ?? '';
  private readonly appSecret = process.env.META_APP_SECRET ?? '';
  private readonly graphVersion = process.env.GRAPH_VERSION?.trim() ?? '';
  private startedAt: number | null = null;
  private grantPromise: Promise<Grant> | null = null;
  private boundToken: string | null = null;
  private boundWaba: string | null = null;

  async createTemplate(input: { accessToken: string; wabaId: string; definition: TemplateDefinition; dispatchGuard?: TemplateDispatchGuard }): Promise<TemplateCreateOutcome> {
    const { accessToken, wabaId, definition } = input;
    try { await this.grant(accessToken, wabaId); } catch {
      return { kind: 'REJECTED', dispatched: false, code: 'PRE_DISPATCH_UNAVAILABLE' };
    }
    const components: Record<string, unknown>[] = [];
    if (definition.header !== undefined) components.push({ type: 'HEADER', format: 'TEXT', text: definition.header });
    const namedExamples = Object.keys(definition.examples).sort().map((paramName) => ({
      param_name: paramName,
      example: definition.examples[paramName],
    }));
    components.push({
      type: 'BODY', text: definition.body,
      ...(namedExamples.length ? { example: { body_text_named_params: namedExamples } } : {}),
    });
    if (definition.footer !== undefined) components.push({ type: 'FOOTER', text: definition.footer });

    let response: Response;
    let payload: unknown;
    try {
      try { await input.dispatchGuard?.beforeDispatch(); } catch { throw new RequestNotDispatchedError(); }
      response = await this.request(`/${encodeURIComponent(wabaId)}/message_templates`, accessToken, 'POST', {
        name: definition.name, language: definition.language, category: definition.category,
        parameter_format: 'NAMED', components,
      });
      payload = await this.readJson(response);
    } catch (error) {
      if (error instanceof RequestNotDispatchedError) return { kind: 'REJECTED', dispatched: false, code: 'PRE_DISPATCH_UNAVAILABLE' };
      return { kind: 'AMBIGUOUS', dispatched: true, code: 'PROVIDER_RESULT_UNCERTAIN' };
    }
    if (!isRecord(payload)) return { kind: 'AMBIGUOUS', dispatched: true, code: 'PROVIDER_RESULT_UNCERTAIN' };
    const hasGraphError = payload.error !== undefined;
    const validId = typeof payload.id === 'string' && payload.id.trim().length > 0 && payload.id.length <= 128;
    const hasAnyId = Object.hasOwn(payload, 'id');
    const contradicted = Object.hasOwn(payload, 'success') || Object.hasOwn(payload, 'data') || Object.hasOwn(payload, 'messages');
    if (response.ok && validId && !hasGraphError && !contradicted) {
      return { kind: 'ACCEPTED', dispatched: true, remoteTemplateId: payload.id as string };
    }
    const graphError = parseGraphError(payload.error);
    if ([400, 401, 403].includes(response.status) && graphError && PROVEN_REFUSAL_CODES.has(graphError.code)
      && graphError.is_transient !== true && !hasAnyId && !contradicted) {
      return { kind: 'REJECTED', dispatched: true, provenNoCreation: true, code: 'PROVIDER_REFUSED' };
    }
    return { kind: 'AMBIGUOUS', dispatched: true, code: 'PROVIDER_RESULT_UNCERTAIN' };
  }

  async listTemplates(input: {
    readonly context: TemplateManagementContext;
    readonly accessToken: string;
    readonly wabaId: string;
    readonly name?: string;
    readonly after: string | null;
    readonly limit: number;
  }): Promise<TemplatePage> {
    if (!Number.isSafeInteger(input.limit) || input.limit < 1 || input.limit > 50
      || (input.name !== undefined && (input.name.length < 1 || input.name.length > 128))
      || (input.after !== null && (input.after.length < 1 || input.after.length > 512))) {
      throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    }
    await this.grant(input.accessToken, input.wabaId);
    const templates: TemplateSummary[] = [];
    const query = new URLSearchParams({ fields: PROVIDER_FIELDS, limit: String(input.limit) });
    if (input.after) query.set('after', input.after);
    if (input.name) query.set('name', input.name);
    const result = await this.readObject(await this.request(`/${encodeURIComponent(input.wabaId)}/message_templates?${query}`, input.accessToken));
    if (!Array.isArray(result.data) || result.data.length > input.limit) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    for (const row of result.data) {
      const summary = parseTemplateSummary(row);
      if (input.name !== undefined && summary.name !== input.name) {
        throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
      }
      templates.push(summary);
    }
    return { templates, nextCursor: parseNextCursor(result.paging) };
  }

  async getTemplate(input: {
    readonly context: TemplateManagementContext;
    readonly accessToken: string;
    readonly wabaId: string;
    readonly remoteTemplateId: string;
  }): Promise<TemplateSummary> {
    if (!input.remoteTemplateId || input.remoteTemplateId.length > 128) {
      throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    }
    await this.grant(input.accessToken, input.wabaId);
    const query = new URLSearchParams({ fields: PROVIDER_FIELDS });
    const result = await this.request(`/${encodeURIComponent(input.remoteTemplateId)}?${query}`, input.accessToken);
    const summary = parseTemplateSummary(await this.readObject(result));
    if (summary.remoteTemplateId !== input.remoteTemplateId) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    return summary;
  }

  private async grant(token: string, wabaId: string): Promise<Grant> {
    if (!token || !wabaId || wabaId.length > 128 || !this.appId || !this.appSecret || !/^v\d+\.0$/.test(this.graphVersion)) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    if (this.boundToken !== null && (this.boundToken !== token || this.boundWaba !== wabaId)) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    this.boundToken = token;
    this.boundWaba = wabaId;
    this.grantPromise ??= this.loadGrant(token, wabaId);
    return this.grantPromise;
  }

  private async loadGrant(token: string, wabaId: string): Promise<Grant> {
    let payload: Record<string, unknown>;
    try {
      const query = new URLSearchParams({ input_token: token });
      const result = await this.request(`/debug_token?${query}`, `${this.appId}|${this.appSecret}`);
      const wrapper = await this.readObject(result);
      if (wrapper.error !== undefined || !isRecord(wrapper.data)) throw new Error('invalid');
      payload = wrapper.data;
    } catch {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    const appId = typeof payload.app_id === 'string' ? payload.app_id : '';
    const valid = payload.is_valid === true;
    if ((Object.hasOwn(payload, 'expires_at') && typeof payload.expires_at !== 'number')
      || (Object.hasOwn(payload, 'data_access_expires_at') && typeof payload.data_access_expires_at !== 'number')) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    const scopes = Array.isArray(payload.scopes) && payload.scopes.every((item) => typeof item === 'string')
      ? payload.scopes as string[] : [];
    const granular = Array.isArray(payload.granular_scopes) ? payload.granular_scopes : [];
    const targets = granular.flatMap((entry) => isRecord(entry) && entry.scope === 'whatsapp_business_management'
      && Array.isArray(entry.target_ids) && entry.target_ids.every((item) => typeof item === 'string')
      ? entry.target_ids as string[] : []);
    const expiresAt = typeof payload.expires_at === 'number' ? payload.expires_at : undefined;
    const dataExpiresAt = typeof payload.data_access_expires_at === 'number' ? payload.data_access_expires_at : undefined;
    const now = Math.floor(Date.now() / 1000);
    const expiryValid = (expiresAt === undefined || expiresAt === 0 || expiresAt > now)
      && (dataExpiresAt === undefined || dataExpiresAt === 0 || dataExpiresAt > now);
    if (appId !== this.appId || !valid || !scopes.includes('whatsapp_business_management')
      || !targets.includes(wabaId) || !expiryValid) {
      throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
    }
    return { appId, valid, expiresAt: expiresAt ?? dataExpiresAt, scopes, targets };
  }

  private async request(path: string, accessToken?: string, method: 'GET' | 'POST' = 'GET', body?: unknown): Promise<Response> {
    const startedAt = this.startedAt ?? (this.startedAt = Date.now());
    const remainingMs = OPERATION_BUDGET_MS - (Date.now() - startedAt);
    if (remainingMs <= 0 || !/^v\d+\.0$/.test(this.graphVersion)) {
      throw new RequestNotDispatchedError();
    }
    const headers: Record<string, string> = { accept: 'application/json' };
    if (accessToken) headers.authorization = `Bearer ${accessToken}`;
    if (body !== undefined) headers['content-type'] = 'application/json';
    try {
      return await fetch(`https://graph.facebook.com/${this.graphVersion}${path}`, {
        method, headers, body: body === undefined ? undefined : JSON.stringify(body),
        signal: AbortSignal.timeout(Math.max(1, Math.min(10_000, remainingMs))), redirect: 'error',
      });
    } catch {
      throw new Error('unavailable');
    }
  }

  private async readJson(response: Response): Promise<unknown> {
    const reader = response.body?.getReader();
    if (!reader) return null;
    const chunks: Uint8Array[] = [];
    let byteLength = 0;
    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        byteLength += value.byteLength;
        if (byteLength > MAX_PROVIDER_RESPONSE_BYTES) {
          await reader.cancel();
          return null;
        }
        chunks.push(value);
      }
      return JSON.parse(new TextDecoder().decode(Buffer.concat(chunks, byteLength))) as unknown;
    } catch {
      try { await reader.cancel(); } catch { /* body already aborted */ }
      return null;
    }
  }

  private async readObject(response: Response): Promise<Record<string, unknown>> {
    if (!response.ok) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    const payload = await this.readJson(response);
    if (!isRecord(payload) || Object.hasOwn(payload, 'error')) {
      throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
    }
    return payload;
  }
}

/** Adapter facade only; all network policy and translation stay in MetaTemplateClient. */
export class BoundMetaMessageTemplateProvider implements MessageTemplateProvider {
  constructor(
    private readonly context: TemplateManagementContext,
    private readonly accessToken: () => Promise<string>,
    private readonly wabaId: string,
    private readonly client: MetaTemplateClient,
  ) {}

  async createTemplate(input: { context: TemplateManagementContext; definition: TemplateDefinition; dispatchGuard?: TemplateDispatchGuard }): Promise<TemplateCreateOutcome> {
    this.assertContext(input.context);
    let accessToken: string;
    try { accessToken = await this.accessToken(); }
    catch { return { kind: 'REJECTED', dispatched: false, code: 'PRE_DISPATCH_UNAVAILABLE' }; }
    return this.client.createTemplate({ accessToken, wabaId: this.wabaId, definition: input.definition, dispatchGuard: input.dispatchGuard });
  }

  async listTemplates(input: { context: TemplateManagementContext; name?: string; after: string | null; limit: number }): Promise<TemplatePage> {
    this.assertContext(input.context);
    const accessToken = await this.accessToken();
    return this.client.listTemplates({ ...input, context: this.context, accessToken, wabaId: this.wabaId });
  }

  async getTemplate(input: { context: TemplateManagementContext; remoteTemplateId: string }): Promise<TemplateSummary> {
    this.assertContext(input.context);
    const accessToken = await this.accessToken();
    return this.client.getTemplate({ ...input, context: this.context, accessToken, wabaId: this.wabaId });
  }

  private assertContext(context: TemplateManagementContext): void {
    if (!sameContext(this.context, context)) throw new TemplateManagementProviderError('TEMPLATE_MANAGEMENT_AUTHORIZATION_UNAVAILABLE');
  }
}

function parseGraphError(value: unknown): GraphError | null {
  if (!isRecord(value) || typeof value.type !== 'string' || value.type.trim().length === 0
    || typeof value.message !== 'string' || value.message.trim().length === 0
    || typeof value.code !== 'number' || !Number.isSafeInteger(value.code) || value.code < 0
    || (value.is_transient !== undefined && typeof value.is_transient !== 'boolean')) return null;
  return { type: value.type, message: value.message, code: value.code, ...(typeof value.is_transient === 'boolean' ? { is_transient: value.is_transient } : {}) };
}

function parseTemplateSummary(value: unknown): TemplateSummary {
  if (!isRecord(value) || typeof value.id !== 'string' || value.id.trim().length === 0 || value.id.length > 128) {
    throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  }
  const statusValues = new Set(['PENDING', 'APPROVED', 'REJECTED', 'PAUSED', 'DISABLED', 'ARCHIVED', 'DELETED', 'IN_APPEAL', 'PENDING_DELETION', 'LIMIT_EXCEEDED']);
  const categoryValues = new Set(['MARKETING', 'UTILITY', 'AUTHENTICATION']);
  if (Array.isArray(value.components) && value.components.length > 16) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  const components: TemplateComponentSummary[] = Array.isArray(value.components) ? value.components.map(parseComponent) : [{ type: 'UNKNOWN', providerType: 'UNKNOWN', semanticFingerprint: createHash('sha256').update('missing-components').digest('hex') }];
  const summary: Omit<TemplateSummary, 'supported' | 'semanticFingerprint'> = {
    remoteTemplateId: value.id,
    status: typeof value.status === 'string' && statusValues.has(value.status) ? value.status as TemplateSummary['status'] : 'UNKNOWN',
    name: typeof value.name === 'string' && characterCount(value.name) > 0 && characterCount(value.name) <= 128 ? value.name : null,
    language: typeof value.language === 'string' && characterCount(value.language) > 0 && characterCount(value.language) <= 35 ? value.language : null,
    category: typeof value.category === 'string' && categoryValues.has(value.category) ? value.category as TemplateSummary['category'] : 'UNKNOWN',
    parameterFormat: value.parameter_format === 'NAMED' || value.parameter_format === 'POSITIONAL' ? value.parameter_format : 'UNKNOWN',
    components,
  };
  const bodies = components.filter((component) => component.type === 'BODY');
  const headers = components.filter((component) => component.type === 'HEADER');
  const footers = components.filter((component) => component.type === 'FOOTER');
  const noUnknown = components.every((component) => component.type !== 'UNKNOWN');
  const headerSupported = headers.every((component) => component.type === 'HEADER' && component.format === 'TEXT');
  const namedParameters = components.every((component) => component.type === 'UNKNOWN'
    || !('parameters' in component) || component.parameters.every((parameter) => !/^[1-9][0-9]{0,1}$/.test(parameter)));
  const supportable = summary.name !== null && summary.language !== null
    && (summary.category === 'UTILITY' || summary.category === 'MARKETING')
    && summary.parameterFormat === 'NAMED' && bodies.length === 1 && headers.length <= 1
    && footers.length <= 1 && noUnknown && headerSupported && namedParameters
    && bodies[0]?.type === 'BODY' && bodies[0].text.trim().length > 0;
  const semanticFingerprint = supportable ? createHash('sha256').update(canonicalSemanticJson({
      name: summary.name, language: summary.language, category: summary.category,
      parameterFormat: summary.parameterFormat, components: value.components,
    })).digest('hex') : null;
  return { ...summary, supported: supportable, semanticFingerprint };
}

function parseComponent(value: unknown): TemplateComponentSummary {
  if (!isRecord(value) || typeof value.type !== 'string') return unknownComponent(value, 'UNKNOWN');
  const supportedKeys = value.type === 'HEADER'
    ? new Set(['type', 'format', 'text', 'example'])
    : value.type === 'BODY' || value.type === 'FOOTER'
      ? new Set(['type', 'text', 'example'])
      : new Set(['type', 'example']);
  if (Object.keys(value).some((key) => !supportedKeys.has(key))) return unknownComponent(value, 'OTHER');
  if (value.type === 'HEADER') {
    if (value.format === 'TEXT' && typeof value.text === 'string' && characterCount(value.text) <= 60) {
      const parameters = parseRemoteParameters(value.text);
      if (parameters) return { type: 'HEADER', format: 'TEXT', text: value.text, parameters };
      return unknownComponent(value, 'OTHER');
    }
    if (value.text !== undefined) return unknownComponent(value, 'OTHER');
    const format = value.format === 'IMAGE' || value.format === 'VIDEO' || value.format === 'DOCUMENT' ? value.format : 'UNKNOWN';
    if (format === 'UNKNOWN') return unknownComponent(value, 'OTHER');
    return { type: 'HEADER', format, text: null };
  }
  if ((value.type === 'BODY' || value.type === 'FOOTER') && typeof value.text === 'string'
    && characterCount(value.text) <= (value.type === 'BODY' ? 1024 : 60)) {
    const parameters = parseRemoteParameters(value.text);
    if (parameters && (value.type !== 'FOOTER' || parameters.length === 0)) return { type: value.type, text: value.text, parameters };
  }
  return unknownComponent(value, 'OTHER');
}

function parseRemoteParameters(text: string): string[] | null {
  const tokens: string[] = [];
  const pattern = /\{\{([^{}]+)\}\}/g;
  for (const match of text.matchAll(pattern)) {
    if (!/^(?:[a-z][a-z_]{0,31}|[1-9][0-9]{0,1})$/.test(match[1])) return null;
    tokens.push(match[1]);
  }
  if (/[{}]/.test(text.replace(pattern, ''))) return null;
  return tokens;
}

function characterCount(value: string): number {
  return Array.from(value).length;
}

function unknownComponent(value: unknown, providerType: 'OTHER' | 'UNKNOWN'): TemplateComponentSummary {
  return {
    type: 'UNKNOWN', providerType,
    semanticFingerprint: createHash('sha256').update(canonicalSemanticJson(value)).digest('hex'),
  };
}

function canonicalSemanticJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalSemanticJson).join(',')}]`;
  if (isRecord(value)) return `{${Object.keys(value).filter((key) => key !== 'example').sort()
    .map((key) => `${JSON.stringify(key)}:${canonicalSemanticJson(value[key])}`).join(',')}}`;
  return JSON.stringify(value) ?? 'null';
}

function parseNextCursor(value: unknown): string | null {
  if (value === undefined || value === null) return null;
  if (!isRecord(value)) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  if (value.next === undefined || value.next === null || value.next === '') return null;
  if (typeof value.next !== 'string') throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  if (!isRecord(value.cursors)) throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  const after = value.cursors.after;
  if (typeof after !== 'string' || after.trim().length === 0 || after.length > 512) {
    throw new TemplateManagementProviderError('TEMPLATE_PROVIDER_RESPONSE_UNAVAILABLE');
  }
  return after;
}

function sameContext(a: TemplateManagementContext, b: TemplateManagementContext): boolean {
  return a.mantenedoraId === b.mantenedoraId && a.buId === b.buId && a.channelId === b.channelId && a.providerResourceIdentityId === b.providerResourceIdentityId
    && a.generation === b.generation && a.pairingEpoch === b.pairingEpoch
    && a.activeCredentialVersion === b.activeCredentialVersion && a.accountReference === b.accountReference;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}
```

## api-app/vitest.config.e2e.ts

```text
import swc from 'unplugin-swc';
import { defineConfig } from 'vitest/config';

// E2E roda contra Postgres DE VERDADE (ADR-0012 §4): o que precisa ser provado
// é o filtro por BU dentro do SQL, e mock de repositório provaria só que o
// código chama o método.
export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['test/**/*.e2e-spec.ts'],
    testTimeout: 30_000,
    hookTimeout: 30_000,
    fileParallelism: false,
    maxWorkers: 1,
    minWorkers: 1,
    sequence: { concurrent: false, shuffle: false },
    setupFiles: ['./test/setup-env.ts'],
  },
  plugins: [swc.vite({ module: { type: 'es6' } })],
});
```

## foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-cp05-all-r38-counter-oracle-failure-v1.1.json

```text
{
  "schema": "stcon05.r38-root-all-terminal.v1",
  "recorded_at_utc": "2026-10-22T03:47:22.488076+00:00",
  "outcome": "STOP one browser measurement assertion; not GREEN or delivery acceptance",
  "executor_id": "/root/template_selection_executor_r37",
  "counts": {
    "api_unit": 284,
    "api_postgresql": 398,
    "web_unit": 45,
    "playwright_passed": 74,
    "playwright_failed": 1,
    "total_passed": 801,
    "total_failed": 1
  },
  "log": "foundation_documentation/artifacts/tmp/st-con-05-r38-all-WsVoGG/canonical-all.log",
  "log_bytes": 213816,
  "log_sha256": "2953620e2108ee74a1b0af7410ed80f97f6e413436310f83c2bfe81f24d723d5",
  "receipt": "foundation_documentation/artifacts/tmp/st-con-05-r38-all-WsVoGG/runner-exit.txt",
  "receipt_sha256": "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865",
  "exit": 1,
  "handoff": "foundation_documentation/artifacts/tmp/st-con-05-r38-all-WsVoGG/handoff.json",
  "handoff_sha256": "c2e5abe4a43fe22decbdfa48a03a8093c84355d9c35bb50e865aedc7fc7936d4",
  "freeze": "foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-cp05-source-freeze-r38-current-selected-owner-typed-v1.1.json",
  "freeze_sha256": "05b144997fff3b97eb15bb94cd08694591fe7389d2a396f29468c5d486bd1b38",
  "source38_matches": true,
  "protected30_exact": true,
  "heads": {
    "root": "80e3940126f22a941f90dba4f5e801b6c0eb2f58",
    "api": "db5a86758a165fac8a1ab587599c37b17890530c",
    "web": "74b9d4b714044829796f875d00553f077c1c329d"
  },
  "proofs": [
    {
      "path": "foundation_documentation/artifacts/tmp/st-con-05-r38-all-WsVoGG/proofs/pre-worker-freshness.json",
      "sha256": "8c51c61fdd5211f7e210a858effc0da68db697e4078be88fbc3ab36a6c4f5110"
    },
    {
      "path": "foundation_documentation/artifacts/tmp/st-con-05-r38-all-WsVoGG/proofs/attestation-browser-authority.json",
      "sha256": "78735f06b8ce05ef0f1cb9a8c293dccf50e1e433515cffdc026b46dced0d0a37"
    }
  ],
  "served_dist_sha256": "ba7560c12923e68148560d108f2b04571897b84e04e3e8a82339241101bc90fb",
  "template_marker_counts": {
    "MESSAGE-TEMPLATE-PCV": 1,
    "MESSAGE-TEMPLATE-EPS": 1,
    "TEMPLATE-RLS-EVIDENCE": 1,
    "TEMPLATE-FRC-EVIDENCE": 1,
    "TEMPLATE-FRC-UI-EVIDENCE": 1
  },
  "exact_failure": {
    "test": "retém a observação passiva mais nova do draft B quando refresh antigo de A omite B",
    "source": "web-app/e2e/message-templates.spec.ts:415",
    "expected": 2,
    "actual": 0,
    "measurement": "effects.filter(meta.template.create)",
    "reached": "Every preceding assertion in same case passed, including real BFF201 A/B accepted creation, exact empty page/cursor, B newer PAUSED fence, passive response, editor PAUSED/ineligible before and after old response, retained B article PAUSED/ineligible and A absent. Failure is final create counter only. No skipped/not-reached target UI assertion claimed."
  },
  "attribution": "Fixture timeline-fixtures.cjs records every template HTTP request in meta.templateCalls and providerCall before dispatch; normal accepted create appends resource but calls providerEffect only when holdsAfter/ambiguousAfter are configured. This normal scenario does not configure them. effects=[] is valid fixture behavior, so the new counter oracle queried the wrong collection. Existing templateCallCount reads the authoritative normal call record and can enforce exactly2 attempted POSTs, paired with already required201/ACCEPTED/resource identities. No fixture/product/contract change needed.",
  "limits": "Exact terminal full log/receipt/source-served proof verified; reported container error-context.md unavailable after normal cleanup, not recreated or claimed. Candidate all failed, though all5 structured markers/main workflow and existing tests passed. No preserved DB/runtime/Meta/activation/production proof.",
  "next": "Admit only last counter type/accessor change to existing templateCallCount, preserving expected2 and all other assertions; source product/tests immutable except these2browser lines. Fresh full all after root exact diff/freeze; candidate assurance still pending."
}
```

## foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-cp05-all-r39-session-timeout-v1.1.json

```text
{
  "schema": "stcon05.r39-root-all-terminal.v1",
  "at_utc": "2026-10-22T04:00:20.531019+00:00",
  "outcome": "STOP API security-test timeout; no blind retry",
  "counts": {
    "api_unit_passed": 284,
    "api_postgresql_passed": 397,
    "api_postgresql_failed": 1,
    "total_passed": 681,
    "total_failed": 1
  },
  "log": "foundation_documentation/artifacts/tmp/st-con-05-r39-all-3KOaki/canonical-all.log",
  "log_bytes": 148409,
  "log_sha256": "7e689084ccb9be2c0ac09c3bd7270fae0365467eecaf82aad7c711e62b9c782a",
  "receipt": "foundation_documentation/artifacts/tmp/st-con-05-r39-all-3KOaki/runner-exit.txt",
  "receipt_sha256": "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865",
  "exit": 1,
  "handoff": "foundation_documentation/artifacts/tmp/st-con-05-r39-all-3KOaki/handoff.json",
  "handoff_sha256": "f3edc387a72f24436dd4a6273afa061ba7e4121ab851c37db1f71ae31c7a346a",
  "freeze": "foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-cp05-source-freeze-r39-current-selection-counter-v1.1.json",
  "freeze_sha256": "01e047218deb79b32b4ad6a229a476a3f697dd4ef31d0ce91fb3d60fd042e72c",
  "source38_matches": true,
  "protected30_exact": true,
  "heads": {
    "root": "80e3940126f22a941f90dba4f5e801b6c0eb2f58",
    "api": "db5a86758a165fac8a1ab587599c37b17890530c",
    "web": "74b9d4b714044829796f875d00553f077c1c329d"
  },
  "failure": {
    "path": "api-app/test/message-template-management.e2e-spec.ts:2283",
    "test": "revalidates BFF session and current observation role before success and unavailable commits",
    "observed": "Vitest60s timeout only, no scenario/stage/assertion trace; same test passed r37/r38. API/product unchanged; r39 changed only browser counter, which was not executed.",
    "unknown": "Which preparation/provider gate/response phase waited, whether request settled before provider entry, and whether cause is test timing, early legitimate refusal, runtime or product. No flaky/environment/product root cause claim."
  },
  "web_unit": "not reached",
  "browser": "not reached; new counter still requires verification",
  "freshness": "Current globalSetup not reached; 03:30 host files/previous browser hash were correctly NOT copied or claimed current. r38 snapshots remain separate actual historical proof.",
  "next": "Read-only source-aware independent HOW opinion and minimal diagnostic-only test instrumentation plan, preserving all6 session scenarios/admin-role403/snapshot/no-write oracles and timeout60s. No product change, bypass, relaxed assertion, automatic retry or preserved action. Then root review/admission of a bounded canonical api diagnostic run before any new full all."
}
```

## Exact inclusion/omission inventory

[
  {
    "path": "api-app/test/message-template-management.e2e-spec.ts",
    "bytes": 173631,
    "sha256": "e3705cf23067994922aa4a47def30698f8e3099f62ac84b5fbc9ef1dd26914b7",
    "selection": "lines1..104"
  },
  {
    "path": "api-app/test/message-template-management.e2e-spec.ts",
    "bytes": 173631,
    "sha256": "e3705cf23067994922aa4a47def30698f8e3099f62ac84b5fbc9ef1dd26914b7",
    "selection": "lines2283..2398"
  },
  {
    "path": "api-app/test/helpers.ts",
    "bytes": 18758,
    "sha256": "117e4f85c81dda37ab30e7eb23704b31538c8c5161aa7562a844eaf11de6819c",
    "selection": "lines329..339"
  },
  {
    "path": "api-app/src/infra/session/session.service.ts",
    "bytes": 5483,
    "sha256": "884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200",
    "selection": "full"
  },
  {
    "path": "api-app/src/surfaces/bff/session.middleware.ts",
    "bytes": 5651,
    "sha256": "80d8be0072b817ec34b3eb7d29218835bd218a40670c1f917d0b1787b0b57211",
    "selection": "full"
  },
  {
    "path": "api-app/src/surfaces/bff/message-templates.controller.ts",
    "bytes": 11822,
    "sha256": "0e0449a80852a4513f626d0df7b1a5bb17b034eeceb50f53842fb91454ff4491",
    "selection": "full"
  },
  {
    "path": "api-app/src/domain/message-templates/template-observation.service.ts",
    "bytes": 39343,
    "sha256": "41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488",
    "selection": "full"
  },
  {
    "path": "api-app/src/domain/message-templates/template-transaction-boundary.ts",
    "bytes": 978,
    "sha256": "ea3e0550ad5c82b263391dbfb3dae6b9e8656d219f18aa0d7c55cd5668722123",
    "selection": "full"
  },
  {
    "path": "api-app/src/integrations/message-templates/template-management.resolver.ts",
    "bytes": 5094,
    "sha256": "2a2a57355ff9fa29774cd4dfef33d9d3fd876bdf5d8a8fe654f0c0435284b59a",
    "selection": "full"
  },
  {
    "path": "api-app/src/integrations/meta/message-template.client.ts",
    "bytes": 21888,
    "sha256": "8dff223f7a97632cf228800cdbbb12ce6f5b151efc5fa30411d03e5ec3280cb5",
    "selection": "full"
  },
  {
    "path": "api-app/vitest.config.e2e.ts",
    "bytes": 683,
    "sha256": "ff76a3b94de4649d18f0f824a24bb45428afcbb751a872a6841a2e388f45f8ff",
    "selection": "full"
  },
  {
    "path": "foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-cp05-all-r38-counter-oracle-failure-v1.1.json",
    "bytes": 4125,
    "sha256": "2a2d88b0036fa7be45e8933b9a6be091dc68ffab731fd1032930fc3a7dde56a2",
    "selection": "full"
  },
  {
    "path": "foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-cp05-all-r39-session-timeout-v1.1.json",
    "bytes": 2698,
    "sha256": "42ac20594eb6b828eae75b9cde019be0985bd4838074a156b979bf0823ef95b9",
    "selection": "full"
  }
]
