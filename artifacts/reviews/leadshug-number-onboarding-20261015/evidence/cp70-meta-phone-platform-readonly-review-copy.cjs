'use strict';

// CP70 preparation only: one guarded read-only Graph phone-resource GET.
// No provider write, retries, redirects, paging, raw response output or storage.
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
const GRAPH_HOST = 'graph.facebook.com';
const GRAPH_VERSION = 'v26.0';
const GRAPH_PATH_PREFIX = `/${GRAPH_VERSION}/`;
const MAX_RESPONSE_BYTES = 128 * 1024;
const REQUEST_TIMEOUT_MS = 10_000;
const REQUESTED_FIELDS = new Set(['platform_type', 'status', 'code_verification_status', 'is_on_biz_app']);
const PLATFORM_ENUMS = new Set(['CLOUD_API', 'ON_PREMISE', 'NOT_APPLICABLE']);
const STATUS_ENUMS = new Set(['CONNECTED', 'DISCONNECTED', 'PENDING', 'MIGRATED', 'DELETED']);
const VERIFICATION_ENUMS = new Set(['VERIFIED', 'NOT_VERIFIED', 'EXPIRED']);

function valueType(value) {
  if (value === null) return 'null';
  if (Array.isArray(value)) return 'array';
  if (typeof value === 'object') return 'object';
  if (typeof value === 'string') return 'string';
  if (typeof value === 'boolean') return 'boolean';
  if (typeof value === 'number') return 'number';
  return 'unknown';
}

function parsePhoneMetadataResponse(body) {
  if (!body || typeof body !== 'object' || Array.isArray(body)) {
    return { validResponseShape: false, fields: null, unknownFieldCount: null };
  }
  const enumField = (key, allowed) => {
    if (!Object.prototype.hasOwnProperty.call(body, key)) return { present: false, type: 'missing', value: null };
    const raw = body[key];
    const type = valueType(raw);
    return { present: true, type, value: type === 'string' ? (allowed.has(raw) ? raw : 'UNKNOWN') : null };
  };
  const boolField = (key) => {
    if (!Object.prototype.hasOwnProperty.call(body, key)) return { present: false, type: 'missing', value: null };
    const raw = body[key];
    return { present: true, type: valueType(raw), value: typeof raw === 'boolean' ? raw : null };
  };
  return {
    validResponseShape: true,
    unknownFieldCount: Object.keys(body).filter((key) => !REQUESTED_FIELDS.has(key)).length,
    fields: {
      platform_type: enumField('platform_type', PLATFORM_ENUMS),
      status: enumField('status', STATUS_ENUMS),
      code_verification_status: enumField('code_verification_status', VERIFICATION_ENUMS),
      is_on_biz_app: boolField('is_on_biz_app'),
    },
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

function invocationMode(args) {
  if (args.length !== 1) return 'invalid';
  if (args[0] === '--execute') return 'execute';
  if (args[0] === '--self-test') return 'self-test';
  return 'invalid';
}

function safeOutput(fields) {
  const allow = {
    outcome: fields.outcome,
    httpStatus: fields.httpStatus ?? null,
    responseTooLarge: fields.responseTooLarge ?? false,
    validResponseShape: fields.validResponseShape ?? null,
    unknownFieldCount: fields.unknownFieldCount ?? null,
    fields: fields.fields ?? null,
    graphErrorCode: fields.graphErrorCode ?? null,
    graphErrorSubcode: fields.graphErrorSubcode ?? null,
    graphIsTransient: fields.graphIsTransient ?? null,
    contextStable: fields.contextStable ?? null,
  };
  process.stdout.write(JSON.stringify(allow) + '\n');
}

function parseResponseBody(bytes) {
  try { return { parsed: true, value: JSON.parse(bytes.toString('utf8')) }; }
  catch { return { parsed: false, value: null }; }
}

function readGraphOnce(phoneNumberId, token) {
  const https = require('node:https');
  return new Promise((resolve) => {
    let finished = false;
    let size = 0;
    const chunks = [];
    let request;
    const hardTimeout = setTimeout(() => {
      if (request) request.destroy();
      finish({ outcome: 'timeout' });
    }, REQUEST_TIMEOUT_MS);
    const finish = (result) => {
      if (finished) return;
      finished = true;
      clearTimeout(hardTimeout);
      resolve(result);
    };
    const path = `${GRAPH_PATH_PREFIX}${encodeURIComponent(phoneNumberId)}?fields=platform_type,status,code_verification_status,is_on_biz_app`;
    request = https.request({
      protocol: 'https:', hostname: GRAPH_HOST, servername: GRAPH_HOST, port: 443,
      method: 'GET', path,
      headers: { Authorization: `Bearer ${token}`, Connection: 'close' },
      rejectUnauthorized: true, timeout: REQUEST_TIMEOUT_MS, maxHeaderSize: 16 * 1024,
    }, (response) => {
      const status = response.statusCode || null;
      if (status && status >= 300 && status < 400) {
        response.destroy();
        return finish({ outcome: 'redirect_refused', httpStatus: status });
      }
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
        const parsedBody = parseResponseBody(Buffer.concat(chunks, size));
        if (status !== 200) return finish({ outcome: 'http_non_200', httpStatus: status, ...(parsedBody.parsed ? safeGraphError(parsedBody.value) : {}) });
        if (!parsedBody.parsed) return finish({ outcome: 'invalid_response', httpStatus: 200 });
        finish({ outcome: 'http_200', httpStatus: 200, parsed: parsePhoneMetadataResponse(parsedBody.value) });
      });
      response.on('error', () => finish({ outcome: 'transport_error', httpStatus: status }));
    });
    request.on('timeout', () => { request.destroy(); finish({ outcome: 'timeout' }); });
    request.on('error', () => finish({ outcome: 'transport_error' }));
    request.end();
  });
}

function selfTest() {
  const valid = parsePhoneMetadataResponse({ platform_type: 'CLOUD_API', status: 'CONNECTED', code_verification_status: 'VERIFIED', is_on_biz_app: true });
  const allowedOtherEnums = parsePhoneMetadataResponse({ platform_type: 'ON_PREMISE', status: 'MIGRATED', code_verification_status: 'EXPIRED', is_on_biz_app: false });
  const absent = parsePhoneMetadataResponse({});
  const unknown = parsePhoneMetadataResponse({ platform_type: 'synthetic_platform_canary', status: 'synthetic_status_canary', code_verification_status: 'synthetic_verification_canary', is_on_biz_app: 'synthetic_boolean_canary' });
  const malformed = parsePhoneMetadataResponse({ platform_type: {}, status: [], code_verification_status: null, is_on_biz_app: 1 });
  const unknownKeys = parsePhoneMetadataResponse({ platform_type: 'CLOUD_API', synthetic_unknown_field_canary: 'synthetic_unknown_value_canary' });
  const badTop = parsePhoneMetadataResponse('synthetic');
  const nonJson = parseResponseBody(Buffer.from('{synthetic'));
  const numericError = safeGraphError({ error: { code: 100, error_subcode: 33, is_transient: false, message: 'synthetic private text', type: 'x', fbtrace_id: 'synthetic' } });
  const invalidError = safeGraphError({ error: { code: '100', error_subcode: -1, is_transient: 'false', message: 'discard' } });
  const serializedUnknown = JSON.stringify(unknownKeys);
  const serializedUnknownEnum = JSON.stringify(unknown);
  if (valid.fields.platform_type.value !== 'CLOUD_API' || valid.fields.status.value !== 'CONNECTED' || valid.fields.code_verification_status.value !== 'VERIFIED' || valid.fields.is_on_biz_app.value !== true) throw new Error('synthetic_allowed_enum_boolean_failed');
  if (allowedOtherEnums.fields.platform_type.value !== 'ON_PREMISE' || allowedOtherEnums.fields.status.value !== 'MIGRATED' || allowedOtherEnums.fields.code_verification_status.value !== 'EXPIRED' || allowedOtherEnums.fields.is_on_biz_app.value !== false) throw new Error('synthetic_secondary_allowlist_failed');
  if (Object.values(absent.fields).some((field) => field.present !== false || field.value !== null)) throw new Error('synthetic_absent_fields_unknown_failed');
  if (unknown.fields.platform_type.value !== 'UNKNOWN' || unknown.fields.status.value !== 'UNKNOWN' || unknown.fields.code_verification_status.value !== 'UNKNOWN' || unknown.fields.is_on_biz_app.value !== null) throw new Error('synthetic_unknown_enums_null_boolean_failed');
  if (malformed.fields.platform_type.value !== null || malformed.fields.status.value !== null || malformed.fields.code_verification_status.value !== null || malformed.fields.is_on_biz_app.value !== null) throw new Error('synthetic_malformed_fields_unknown_failed');
  if (unknownKeys.unknownFieldCount !== 1 || serializedUnknown.includes('synthetic_unknown_field_canary') || serializedUnknown.includes('synthetic_unknown_value_canary')) throw new Error('synthetic_unknown_field_redaction_failed');
  if (serializedUnknownEnum.includes('synthetic_platform_canary') || serializedUnknownEnum.includes('synthetic_status_canary') || serializedUnknownEnum.includes('synthetic_boolean_canary')) throw new Error('synthetic_unknown_enum_redaction_failed');
  if (badTop.validResponseShape !== false || badTop.fields !== null || nonJson.parsed !== false) throw new Error('synthetic_bad_response_failed');
  if (numericError.graphErrorCode !== 100 || numericError.graphErrorSubcode !== 33 || numericError.graphIsTransient !== false) throw new Error('synthetic_graph_error_allowlist_failed');
  if (invalidError.graphErrorCode !== null || invalidError.graphErrorSubcode !== null || invalidError.graphIsTransient !== null) throw new Error('synthetic_invalid_graph_error_failed');
  if (invocationMode([]) !== 'invalid' || invocationMode(['--execute']) !== 'execute' || invocationMode(['--self-test']) !== 'self-test') throw new Error('synthetic_invocation_mode_failed');
  process.stdout.write(JSON.stringify({ allowedFiniteEnumsAndBooleans: true, missingAndMalformedValuesUnknown: true, unknownEnumsNormalizedAndRawValuesRedacted: true, unknownFieldsCountedAndRedacted: true, invalidResponseAndNumericErrorsBounded: true, invocationModeGuard: true, networkCalled: false, resolverCalled: false, dbCalled: false }) + '\n');
}

async function main() {
  let prisma;
  let resolved;
  try {
    if (process.env.META_APP_ID !== APP_ID || process.env.GRAPH_VERSION?.trim() !== GRAPH_VERSION) {
      return safeOutput({ outcome: 'runtime_meta_public_config_mismatch' });
    }
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
        receiptVerifiedAt: true, connectedAt: true, operationLeaseUntil: true,
        credential: { select: { generation: true, version: true } },
        currentAttempt: { select: { state: true, stage: true, version: true, generation: true, pairingEpoch: true, leaseUntil: true } },
      },
    });
    const guardOk = (ch) => Boolean(ch
      && ch.id === EXPECTED_CHANNEL_ID && ch.buId === EXPECTED_BU_ID && ch.type === 'OFICIAL'
      && ch.generation === EXPECTED_GENERATION && ch.pairingEpoch === EXPECTED_EPOCH
      && ch.verifiedEpoch === EXPECTED_EPOCH && ch.ownNumberVerified === true
      && ch.status === EXPECTED_STATUS && ch.providerConnectionState === EXPECTED_CONNECTION_STATE
      && ch.currentAttemptId === EXPECTED_ATTEMPT_ID
      && ch.currentAttempt && ch.currentAttempt.state === EXPECTED_ATTEMPT_STATE
      && ch.currentAttempt.stage === EXPECTED_ATTEMPT_STAGE
      && ch.currentAttempt.version === EXPECTED_ATTEMPT_VERSION
      && ch.currentAttempt.generation === EXPECTED_GENERATION
      && ch.currentAttempt.pairingEpoch === null
      && !ch.operationLeaseUntil && !ch.currentAttempt.leaseUntil
      && ch.credential && ch.credential.generation === EXPECTED_GENERATION
      && ch.credential.version === EXPECTED_CREDENTIAL_VERSION);
    const readIdentity = async () => prisma.providerResourceIdentity.findMany({
      where: { buId: EXPECTED_BU_ID, provider: 'OFICIAL', currentChannelId: EXPECTED_CHANNEL_ID, retiredAt: null },
      select: { id: true, externalResourceId: true, managedLifecycle: true },
      take: 2,
    });
    const before = await readGuard();
    if (!guardOk(before)) return safeOutput({ outcome: 'precondition_mismatch' });
    const identitiesBefore = await readIdentity();
    if (identitiesBefore.length !== 1 || identitiesBefore[0].id !== EXPECTED_IDENTITY_ID || !identitiesBefore[0].managedLifecycle ||
        typeof identitiesBefore[0].externalResourceId !== 'string' || !identitiesBefore[0].externalResourceId) {
      return safeOutput({ outcome: 'precondition_mismatch' });
    }
    const identityResourceId = identitiesBefore[0].externalResourceId;

    try { resolved = await resolver.resolve(EXPECTED_CHANNEL_ID, 'verify'); }
    catch { return safeOutput({ outcome: 'credential_resolution_failed' }); }
    if (!resolved || resolved.channelId !== EXPECTED_CHANNEL_ID || resolved.buId !== EXPECTED_BU_ID
        || resolved.provider !== 'OFICIAL' || resolved.generation !== EXPECTED_GENERATION
        || resolved.pairingEpoch !== EXPECTED_EPOCH || typeof resolved.accessToken !== 'string' || !resolved.accessToken
        || resolved.providerResourceIdentityId !== EXPECTED_IDENTITY_ID
        || resolved.phoneNumberId !== identityResourceId || resolved.externalResourceId !== identityResourceId
        || !/^\d{5,32}$/.test(resolved.phoneNumberId)) {
      return safeOutput({ outcome: 'credential_context_mismatch' });
    }

    let result;
    try { result = await readGraphOnce(resolved.phoneNumberId, resolved.accessToken); }
    catch { result = { outcome: 'transport_error' }; }
    resolved.accessToken = undefined;

    const after = await readGuard();
    const identitiesAfter = await readIdentity();
    const contextStable = guardOk(after) && identitiesAfter.length === 1
      && identitiesAfter[0].id === EXPECTED_IDENTITY_ID && identitiesAfter[0].managedLifecycle
      && identitiesAfter[0].externalResourceId === identityResourceId
      && identitiesAfter[0].externalResourceId === resolved.phoneNumberId
      && before.status === after.status && before.generation === after.generation
      && before.currentAttempt.version === after.currentAttempt.version
      && before.credential.version === after.credential.version
      && before.pairingEpoch === after.pairingEpoch && before.verifiedEpoch === after.verifiedEpoch;
    if (!contextStable) return safeOutput({ outcome: 'postcheck_drift', httpStatus: result.httpStatus ?? null, contextStable: false, responseTooLarge: result.responseTooLarge });
    if (result.outcome !== 'http_200' || !result.parsed) return safeOutput({ outcome: result.outcome, httpStatus: result.httpStatus ?? null, ...(result.graphErrorCode !== undefined ? { graphErrorCode: result.graphErrorCode } : {}), ...(result.graphErrorSubcode !== undefined ? { graphErrorSubcode: result.graphErrorSubcode } : {}), ...(result.graphIsTransient !== undefined ? { graphIsTransient: result.graphIsTransient } : {}), responseTooLarge: result.responseTooLarge, contextStable: true });
    return safeOutput({ outcome: result.outcome, httpStatus: result.httpStatus, ...result.parsed, contextStable: true });
  } catch {
    safeOutput({ outcome: 'inconclusive' });
  } finally {
    if (resolved) resolved.accessToken = undefined;
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

module.exports = { parsePhoneMetadataResponse, safeGraphError, invocationMode };
