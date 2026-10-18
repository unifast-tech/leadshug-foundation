'use strict';

// CP68 preparation only. Run inside the already-pinned owned API container
// only after a separate root GO. This file never writes application data.
const APP_ID = '874966345550148';
const EXPECTED_BU_ID = 'a1492634-8685-46d8-a7cb-685a99f5c930';
const EXPECTED_CHANNEL_ID = 'eeb74451-edaf-4a44-a6cb-059dd184e152';
const EXPECTED_ATTEMPT_ID = 'e3165ba6e498307fd31c0213f544bdf1';
const EXPECTED_GENERATION = 1;
const EXPECTED_EPOCH = 0;
const EXPECTED_STATUS = 'CONECTANDO';
const EXPECTED_CONNECTION_STATE = 'SUBSCRIBED';
const EXPECTED_ATTEMPT_STATE = 'PENDING_RECEIPT';
const EXPECTED_ATTEMPT_STAGE = 'SUBSCRIBED';
const EXPECTED_ATTEMPT_VERSION = 7;
const EXPECTED_CREDENTIAL_VERSION = 1;
const EXPECTED_IDENTITY_ID = '33980208-a547-4ab8-bab1-42a82bcd2197';
const EXPECTED_CALLBACK = 'https://estimation-editions-knee-inclusion.trycloudflare.com/webhooks/meta';
const GRAPH_HOST = 'graph.facebook.com';
const GRAPH_VERSION = 'v26.0';
const GRAPH_PATH_PREFIX = `/${GRAPH_VERSION}/`;
const MAX_RESPONSE_BYTES = 128 * 1024;
const REQUEST_TIMEOUT_MS = 10_000;

function parseSubscriptionResponse(body) {
  if (!body || typeof body !== 'object' || Array.isArray(body) || !Array.isArray(body.data)) {
    return {
      validShape: false,
      dataCount: null,
      currentAppPresent: null,
      pagingUnknown: true,
      overrideReturned: null,
      matchesExpectedComputed: null,
    };
  }

  const rows = body.data;
  const recognized = rows.map((row) => {
    if (!row || typeof row !== 'object' || Array.isArray(row)) return null;
    const app = row.whatsapp_business_api_data;
    if (!app || typeof app !== 'object' || Array.isArray(app) || typeof app.id !== 'string') return null;
    return { row, app };
  });

  const matching = recognized.filter((entry) => entry && entry.app.id === APP_ID);
  const matchingCallbacks = matching.map(({ row, app }) => {
    for (const obj of [row, app]) {
      if (obj && typeof obj === 'object' && Object.prototype.hasOwnProperty.call(obj, 'override_callback_uri')) {
        return typeof obj.override_callback_uri === 'string' ? obj.override_callback_uri : null;
      }
    }
    return null;
  });
  const pagingUnknown = Boolean(body.paging && typeof body.paging === 'object'
    && (body.paging.next || (body.paging.cursors && body.paging.cursors.after)));
  const allRowsRecognized = recognized.every(Boolean);
  const currentAppPresent = matching.length > 0 ? true : (allRowsRecognized && !pagingUnknown ? false : null);
  const distinctCallbackValues = [...new Set(matchingCallbacks)];
  const callbackUnambiguous = matching.length > 0
    && matchingCallbacks.every((value) => typeof value === 'string')
    && distinctCallbackValues.length === 1;

  return {
    validShape: true,
    dataCount: rows.length,
    currentAppPresent,
    pagingUnknown,
    overrideReturned: callbackUnambiguous ? true : null,
    matchesExpectedComputed: callbackUnambiguous
      ? distinctCallbackValues[0] === EXPECTED_CALLBACK
      : null,
  };
}

function safeGraphError(body) {
  const error = body && typeof body === 'object' && body.error && typeof body.error === 'object' ? body.error : null;
  return {
    graphErrorCode: error && Number.isSafeInteger(error.code) && error.code >= 0 ? error.code : null,
    graphErrorSubcode: error && Number.isSafeInteger(error.error_subcode) && error.error_subcode >= 0 ? error.error_subcode : null,
    graphIsTransient: error && typeof error.is_transient === 'boolean' ? error.is_transient : null,
  };
}

function safeHttpErrorFields(result) {
  return {
    outcome: result.outcome,
    httpStatus: result.httpStatus ?? null,
    graphErrorCode: result.graphErrorCode ?? null,
    graphErrorSubcode: result.graphErrorSubcode ?? null,
    graphIsTransient: result.graphIsTransient ?? null,
  };
}

function selfTest() {
  const recognized = parseSubscriptionResponse({
    data: [{ whatsapp_business_api_data: { id: APP_ID, name: 'synthetic' }, override_callback_uri: 'https://wrong.synthetic.invalid/webhooks/meta' }],
  });
  const otherAppExpectedCallback = parseSubscriptionResponse({
    data: [{ whatsapp_business_api_data: { id: 'other-synthetic-app' }, override_callback_uri: EXPECTED_CALLBACK }],
  });
  const noRecognizedRows = parseSubscriptionResponse({ data: [{ unrelated: true }] });
  const absentOverride = parseSubscriptionResponse({ data: [{ whatsapp_business_api_data: { id: APP_ID } }] });
  const pagedNoMatch = parseSubscriptionResponse({ data: [{ whatsapp_business_api_data: { id: 'other-synthetic-app' } }], paging: { next: 'synthetic' } });
  const completeNoMatch = parseSubscriptionResponse({ data: [{ whatsapp_business_api_data: { id: 'other-synthetic-app' } }] });
  const emptyData = parseSubscriptionResponse({ data: [] });
  const conflictingCandidates = parseSubscriptionResponse({ data: [
    { whatsapp_business_api_data: { id: APP_ID }, override_callback_uri: EXPECTED_CALLBACK },
    { whatsapp_business_api_data: { id: APP_ID }, override_callback_uri: 'https://other.synthetic.invalid/webhooks/meta' },
  ] });
  const malformed = parseSubscriptionResponse({ data: 'not-an-array' });
  const safeError = safeGraphError({ error: { code: 190, error_subcode: 123, is_transient: false, message: 'synthetic secret text', type: 'synthetic', fbtrace_id: 'synthetic' } });
  const invalidError = safeGraphError({ error: { code: '190', error_subcode: -1, is_transient: 'false', message: 'discard' } });
  const propagatedError = safeHttpErrorFields({ outcome: 'http_non_200', httpStatus: 403, graphErrorCode: 10, graphErrorSubcode: 200, graphIsTransient: false, message: 'discard' });
  if (recognized.currentAppPresent !== true || recognized.overrideReturned !== true || recognized.matchesExpectedComputed !== false) throw new Error('synthetic_current_app_contract_failed');
  if (otherAppExpectedCallback.currentAppPresent !== false || otherAppExpectedCallback.overrideReturned !== null || otherAppExpectedCallback.matchesExpectedComputed !== null) throw new Error('synthetic_other_app_isolation_failed');
  if (noRecognizedRows.currentAppPresent !== null || noRecognizedRows.overrideReturned !== null) throw new Error('synthetic_unknown_contract_failed');
  if (absentOverride.currentAppPresent !== true || absentOverride.overrideReturned !== null || absentOverride.matchesExpectedComputed !== null) throw new Error('synthetic_absent_override_failed');
  if (pagedNoMatch.pagingUnknown !== true || pagedNoMatch.currentAppPresent !== null) throw new Error('synthetic_paging_contract_failed');
  if (completeNoMatch.currentAppPresent !== false || emptyData.currentAppPresent !== false) throw new Error('synthetic_complete_absence_failed');
  if (conflictingCandidates.currentAppPresent !== true || conflictingCandidates.overrideReturned !== null || conflictingCandidates.matchesExpectedComputed !== null) throw new Error('synthetic_conflicting_candidates_failed');
  if (malformed.validShape !== false || malformed.currentAppPresent !== null) throw new Error('synthetic_malformed_contract_failed');
  if (safeError.graphErrorCode !== 190 || safeError.graphErrorSubcode !== 123 || safeError.graphIsTransient !== false) throw new Error('synthetic_error_allowlist_failed');
  if (invalidError.graphErrorCode !== null || invalidError.graphErrorSubcode !== null || invalidError.graphIsTransient !== null) throw new Error('synthetic_invalid_error_failed');
  if (propagatedError.graphErrorCode !== 10 || propagatedError.graphErrorSubcode !== 200 || propagatedError.graphIsTransient !== false || Object.keys(propagatedError).includes('message')) throw new Error('synthetic_error_propagation_failed');
  if (invocationMode([]) !== 'invalid' || invocationMode(['--execute']) !== 'execute' || invocationMode(['--self-test']) !== 'self-test') throw new Error('synthetic_invocation_contract_failed');
  process.stdout.write(JSON.stringify({ syntheticCasesPassed: 13, networkCalled: false, resolverCalled: false, bodyTextOrTraceEmitted: false }) + '\n');
}

function invocationMode(args) {
  if (args.length !== 1) return 'invalid';
  if (args[0] === '--execute') return 'execute';
  if (args[0] === '--self-test') return 'self-test';
  return 'invalid';
}

function safeOutput(fields) {
  const allowed = {
    outcome: fields.outcome,
    httpStatus: fields.httpStatus ?? null,
    dataCount: fields.dataCount ?? null,
    currentAppPresent: fields.currentAppPresent ?? null,
    pagingUnknown: fields.pagingUnknown ?? true,
    overrideReturned: fields.overrideReturned ?? null,
    matchesExpectedComputed: fields.matchesExpectedComputed ?? null,
    graphErrorCode: fields.graphErrorCode ?? null,
    graphErrorSubcode: fields.graphErrorSubcode ?? null,
    graphIsTransient: fields.graphIsTransient ?? null,
    responseTooLarge: fields.responseTooLarge ?? false,
    contextStable: fields.contextStable ?? null,
  };
  process.stdout.write(JSON.stringify(allowed) + '\n');
}

function readGraphOnce(url, token) {
  const https = require('node:https');
  return new Promise((resolve) => {
    let finished = false;
    let size = 0;
    const chunks = [];
    const hardTimeout = setTimeout(() => {
      request.destroy();
      finish({ outcome: 'timeout' });
    }, REQUEST_TIMEOUT_MS);
    const finish = (result) => {
      if (finished) return;
      finished = true;
      clearTimeout(hardTimeout);
      resolve(result);
    };
    const request = https.request(url, {
      method: 'GET',
      headers: { Authorization: `Bearer ${token}` },
      rejectUnauthorized: true,
      timeout: REQUEST_TIMEOUT_MS,
      maxHeaderSize: 16 * 1024,
    }, (response) => {
      const status = response.statusCode || null;
      response.on('data', (chunk) => {
        size += chunk.length;
        if (size > MAX_RESPONSE_BYTES) {
          response.destroy();
          request.destroy();
          finish({ outcome: 'response_too_large', httpStatus: status, responseTooLarge: true });
          return;
        }
        chunks.push(chunk);
      });
      response.on('end', () => {
        if (status !== 200) {
          let safeError = { graphErrorCode: null, graphErrorSubcode: null, graphIsTransient: null };
          try {
            const body = JSON.parse(Buffer.concat(chunks, size).toString('utf8'));
            safeError = safeGraphError(body);
          } catch {
            // Error body is intentionally discarded; only the allowlisted
            // numeric/boolean fields may leave this process.
          }
          return finish({ outcome: 'http_non_200', httpStatus: status, ...safeError });
        }
        try {
          const body = JSON.parse(Buffer.concat(chunks, size).toString('utf8'));
          finish({ outcome: 'http_200', httpStatus: 200, parsed: parseSubscriptionResponse(body) });
        } catch {
          finish({ outcome: 'invalid_response', httpStatus: 200 });
        }
      });
      response.on('error', () => finish({ outcome: 'transport_error', httpStatus: status }));
    });
    request.on('timeout', () => {
      request.destroy();
      finish({ outcome: 'timeout' });
    });
    request.on('error', () => finish({ outcome: 'transport_error' }));
    request.end();
  });
}

async function main() {
  let prisma;
  try {
    // These are the only process environment values inspected by this helper.
    if (process.env.META_APP_ID !== APP_ID || process.env.GRAPH_VERSION?.trim() !== GRAPH_VERSION) {
      return safeOutput({ outcome: 'runtime_meta_public_config_mismatch' });
    }
    // Delayed imports keep --self-test entirely offline and credential-free.
    const { PrismaClient } = require('@prisma/client');
    const path = require('node:path');
    const { ChannelCredentialResolver } = require(path.join(process.cwd(), 'dist/domain/channels/channel-credential-resolver.js'));
    prisma = new PrismaClient();
    const resolver = new ChannelCredentialResolver(prisma);

    const readGuard = async () => prisma.buChannel.findUnique({
      where: { id: EXPECTED_CHANNEL_ID },
      select: {
        id: true, buId: true, type: true, status: true, generation: true,
        currentAttemptId: true, pairingEpoch: true, verifiedEpoch: true,
        ownNumberVerified: true, providerConnectionState: true,
        receiptVerifiedAt: true, operationLeaseUntil: true,
        credential: { select: { generation: true, version: true } },
        currentAttempt: { select: { state: true, stage: true, version: true, generation: true, leaseUntil: true } },
      },
    });
    const guardOk = (ch) => Boolean(ch
      && ch.buId === EXPECTED_BU_ID && ch.type === 'OFICIAL'
      && ch.generation === EXPECTED_GENERATION && ch.pairingEpoch === EXPECTED_EPOCH
      && ch.verifiedEpoch === EXPECTED_EPOCH && ch.ownNumberVerified === true
      && ch.status === EXPECTED_STATUS && ch.providerConnectionState === EXPECTED_CONNECTION_STATE
      && ch.currentAttemptId === EXPECTED_ATTEMPT_ID
      && ch.currentAttempt && ch.currentAttempt.state === EXPECTED_ATTEMPT_STATE
      && ch.currentAttempt.stage === EXPECTED_ATTEMPT_STAGE
      && ch.currentAttempt.version === EXPECTED_ATTEMPT_VERSION
      && ch.currentAttempt.generation === EXPECTED_GENERATION
      && !ch.operationLeaseUntil && !ch.currentAttempt.leaseUntil
      && ch.credential && ch.credential.generation === EXPECTED_GENERATION
      && ch.credential.version === EXPECTED_CREDENTIAL_VERSION);

    const before = await readGuard();
    if (!guardOk(before)) return safeOutput({ outcome: 'precondition_mismatch' });
    const identities = await prisma.providerResourceIdentity.findMany({
      where: { buId: EXPECTED_BU_ID, provider: 'OFICIAL', currentChannelId: EXPECTED_CHANNEL_ID, retiredAt: null },
      select: { id: true, externalResourceId: true, managedLifecycle: true },
    });
    if (identities.length !== 1 || identities[0].id !== EXPECTED_IDENTITY_ID || !identities[0].managedLifecycle
      || typeof identities[0].externalResourceId !== 'string' || !identities[0].externalResourceId) {
      return safeOutput({ outcome: 'precondition_mismatch' });
    }
    const identityResourceId = identities[0].externalResourceId;

    let resolved;
    try {
      resolved = await resolver.resolve(EXPECTED_CHANNEL_ID, 'verify');
    } catch {
      return safeOutput({ outcome: 'credential_resolution_failed' });
    }
    if (!resolved || resolved.channelId !== EXPECTED_CHANNEL_ID || resolved.buId !== EXPECTED_BU_ID
      || resolved.provider !== 'OFICIAL' || resolved.generation !== EXPECTED_GENERATION
      || resolved.pairingEpoch !== EXPECTED_EPOCH || typeof resolved.accessToken !== 'string'
      || !resolved.accessToken || typeof resolved.wabaId !== 'string' || !resolved.wabaId
      || resolved.providerResourceIdentityId !== EXPECTED_IDENTITY_ID
      || resolved.phoneNumberId !== identityResourceId) {
      return safeOutput({ outcome: 'precondition_mismatch' });
    }

    const url = `https://${GRAPH_HOST}${GRAPH_PATH_PREFIX}${encodeURIComponent(resolved.wabaId)}/subscribed_apps`;
    const result = await readGraphOnce(url, resolved.accessToken);
    resolved.accessToken = undefined;

    const after = await readGuard();
    const afterIdentities = await prisma.providerResourceIdentity.findMany({
      where: { buId: EXPECTED_BU_ID, provider: 'OFICIAL', currentChannelId: EXPECTED_CHANNEL_ID, retiredAt: null },
      select: { id: true, externalResourceId: true, managedLifecycle: true },
    });
    const contextStable = guardOk(after) && afterIdentities.length === 1
      && afterIdentities[0].id === EXPECTED_IDENTITY_ID && afterIdentities[0].managedLifecycle
      && afterIdentities[0].externalResourceId === identityResourceId
      && afterIdentities[0].externalResourceId === resolved.phoneNumberId
      && before.status === after.status && before.generation === after.generation
      && before.currentAttempt.version === after.currentAttempt.version
      && before.pairingEpoch === after.pairingEpoch && before.verifiedEpoch === after.verifiedEpoch;
    if (!contextStable) return safeOutput({ outcome: 'postcheck_drift', httpStatus: result.httpStatus, contextStable: false, responseTooLarge: result.responseTooLarge });
    if (!result.parsed) return safeOutput({ ...safeHttpErrorFields(result), contextStable: true, responseTooLarge: result.responseTooLarge });
    return safeOutput({ outcome: result.outcome, httpStatus: result.httpStatus, ...result.parsed, contextStable: true });
  } catch {
    safeOutput({ outcome: 'inconclusive' });
  } finally {
    if (prisma) await prisma.$disconnect().catch(() => {});
  }
}

const invokedFromStdin = process.argv[1] === '-';
if (require.main === module || invokedFromStdin) {
  const mode = invocationMode(process.argv.slice(2));
  if (mode === 'self-test') selfTest();
  else if (mode === 'execute') main();
  else safeOutput({ outcome: 'invalid_invocation' });
}

module.exports = { parseSubscriptionResponse };
