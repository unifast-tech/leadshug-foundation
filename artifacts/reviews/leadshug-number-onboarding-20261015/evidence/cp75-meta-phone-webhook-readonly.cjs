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
const EXPECTED_CALLBACK = 'https://estimation-editions-knee-inclusion.trycloudflare.com/webhooks/meta';
const GRAPH_HOST = 'graph.facebook.com';
const GRAPH_VERSION = 'v26.0';
const GRAPH_PATH_PREFIX = `/${GRAPH_VERSION}/`;
const MAX_RESPONSE_BYTES = 128 * 1024;
const REQUEST_TIMEOUT_MS = 10_000;
const CONFIG_KEYS = new Set(['application', 'whatsapp_business_account', 'phone_number']);
const CALLBACK_KEYS = new Set(['callback_uri', 'override_callback_uri']);

function valueType(value) {
  if (value === null) return 'null';
  if (Array.isArray(value)) return 'array';
  if (typeof value === 'object') return 'object';
  if (typeof value === 'string') return 'string';
  if (typeof value === 'boolean') return 'boolean';
  if (typeof value === 'number') return 'number';
  return 'unknown';
}

function valueState(value) {
  const type = valueType(value);
  if (type === 'null') return 'empty';
  if (type === 'string') return value.length === 0 ? 'empty' : 'configured';
  if (type === 'object') return Object.keys(value).length === 0 ? 'empty' : 'configured';
  if (type === 'array') return value.length === 0 ? 'empty' : 'configured';
  return 'unknown';
}

function parseWebhookConfigurationResponse(body) {
  if (!body || typeof body !== 'object' || Array.isArray(body)) {
    return { validResponseShape: false, fieldReturned: null, configurationType: 'unknown', unknownKeyCount: null, fields: null };
  }
  if (!Object.prototype.hasOwnProperty.call(body, 'webhook_configuration')) {
    return { validResponseShape: true, fieldReturned: false, configurationType: 'missing', unknownKeyCount: 0, fields: null };
  }
  const config = body.webhook_configuration;
  if (!config || typeof config !== 'object' || Array.isArray(config)) {
    return { validResponseShape: true, fieldReturned: true, configurationType: valueType(config), unknownKeyCount: null, fields: null };
  }

  const fields = {};
  let unknownKeyCount = 0;
  const describeLayer = (value) => {
    const type = valueType(value);
    const descriptor = { present: true, type, state: valueState(value), callbackPresent: null, matchesExpectedCallback: null };
    if (type === 'string') {
      if (value.length > 0) {
        descriptor.callbackPresent = true;
        descriptor.matchesExpectedCallback = value === EXPECTED_CALLBACK;
      }
      return descriptor;
    }
    if (type !== 'object') return descriptor;

    const callbacks = [];
    for (const [key, nestedValue] of Object.entries(value)) {
      if (CALLBACK_KEYS.has(key)) callbacks.push(typeof nestedValue === 'string' ? nestedValue : null);
      else unknownKeyCount += 1;
    }
    if (callbacks.length > 0) {
      descriptor.callbackPresent = true;
      const distinct = [...new Set(callbacks)];
      const unambiguous = callbacks.every((candidate) => typeof candidate === 'string' && candidate.length > 0) && distinct.length === 1;
      descriptor.matchesExpectedCallback = unambiguous ? distinct[0] === EXPECTED_CALLBACK : null;
    }
    return descriptor;
  };

  for (const [key, value] of Object.entries(config)) {
    if (CONFIG_KEYS.has(key)) fields[key] = describeLayer(value);
    else unknownKeyCount += 1;
  }
  for (const key of CONFIG_KEYS) {
    if (!Object.prototype.hasOwnProperty.call(config, key)) {
      fields[key] = { present: false, type: 'missing', state: 'unknown', callbackPresent: null, matchesExpectedCallback: null };
    }
  }
  return {
    validResponseShape: true,
    fieldReturned: true,
    configurationType: 'object',
    unknownKeyCount,
    fields,
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
    fieldReturned: fields.fieldReturned ?? null,
    configurationType: fields.configurationType ?? null,
    unknownKeyCount: fields.unknownKeyCount ?? null,
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
    const path = `${GRAPH_PATH_PREFIX}${encodeURIComponent(phoneNumberId)}?fields=webhook_configuration`;
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
        finish({ outcome: 'http_200', httpStatus: 200, parsed: parseWebhookConfigurationResponse(parsedBody.value) });
      });
      response.on('error', () => finish({ outcome: 'transport_error', httpStatus: status }));
    });
    request.on('timeout', () => { request.destroy(); finish({ outcome: 'timeout' }); });
    request.on('error', () => finish({ outcome: 'transport_error' }));
    request.end();
  });
}

function selfTest() {
  const layerKeys = [...CONFIG_KEYS];
  const alternate = 'https://synthetic.invalid/callback-canary';
  for (const key of layerKeys) {
    const equal = parseWebhookConfigurationResponse({ webhook_configuration: { [key]: EXPECTED_CALLBACK } });
    const different = parseWebhookConfigurationResponse({ webhook_configuration: { [key]: alternate } });
    const empty = parseWebhookConfigurationResponse({ webhook_configuration: { [key]: '' } });
    const malformed = parseWebhookConfigurationResponse({ webhook_configuration: { [key]: false } });
    if (equal.fields[key].callbackPresent !== true || equal.fields[key].matchesExpectedCallback !== true) throw new Error('synthetic_direct_equal_failed');
    if (different.fields[key].callbackPresent !== true || different.fields[key].matchesExpectedCallback !== false) throw new Error('synthetic_direct_different_failed');
    if (empty.fields[key].state !== 'empty' || empty.fields[key].matchesExpectedCallback !== null) throw new Error('synthetic_direct_empty_unknown_failed');
    if (malformed.fields[key].type !== 'boolean' || malformed.fields[key].matchesExpectedCallback !== null) throw new Error('synthetic_direct_malformed_unknown_failed');
  }
  const nestedMatching = parseWebhookConfigurationResponse({ webhook_configuration: {
    application: { override_callback_uri: EXPECTED_CALLBACK },
    whatsapp_business_account: { callback_uri: EXPECTED_CALLBACK },
    phone_number: { override_callback_uri: EXPECTED_CALLBACK },
  } });
  const conflictingNested = parseWebhookConfigurationResponse({ webhook_configuration: {
    application: { callback_uri: EXPECTED_CALLBACK, override_callback_uri: alternate },
  } });
  const mixedLayers = parseWebhookConfigurationResponse({ webhook_configuration: {
    application: EXPECTED_CALLBACK,
    whatsapp_business_account: alternate,
    phone_number: EXPECTED_CALLBACK,
  } });
  const absentField = parseWebhookConfigurationResponse({ id: 'synthetic' });
  const malformedConfig = parseWebhookConfigurationResponse({ webhook_configuration: 'synthetic' });
  const unknownKeys = parseWebhookConfigurationResponse({ webhook_configuration: { synthetic_unknown_key_canary: 'synthetic_unknown_value_canary', application: {} } });
  const badTop = parseWebhookConfigurationResponse('synthetic');
  const nonJson = parseResponseBody(Buffer.from('{synthetic'));
  const numericError = safeGraphError({ error: { code: 100, error_subcode: 33, is_transient: false, message: 'synthetic private text', type: 'x', fbtrace_id: 'synthetic' } });
  const invalidError = safeGraphError({ error: { code: '100', error_subcode: -1, is_transient: 'false', message: 'discard' } });
  const serializedUnknown = JSON.stringify(unknownKeys);
  if (layerKeys.some((key) => nestedMatching.fields[key].matchesExpectedCallback !== true)) throw new Error('synthetic_nested_layer_matches_failed');
  if (conflictingNested.fields.application.callbackPresent !== true || conflictingNested.fields.application.matchesExpectedCallback !== null) throw new Error('synthetic_conflicting_nested_unknown_failed');
  if (mixedLayers.fields.application.matchesExpectedCallback !== true || mixedLayers.fields.whatsapp_business_account.matchesExpectedCallback !== false || mixedLayers.fields.phone_number.matchesExpectedCallback !== true) throw new Error('synthetic_per_layer_mixed_comparison_failed');
  if (absentField.fieldReturned !== false || absentField.fields !== null) throw new Error('synthetic_missing_field_unknown_failed');
  if (malformedConfig.fieldReturned !== true || malformedConfig.configurationType !== 'string' || malformedConfig.fields !== null) throw new Error('synthetic_malformed_config_unknown_failed');
  if (unknownKeys.unknownKeyCount !== 1 || serializedUnknown.includes('synthetic_unknown_key_canary') || serializedUnknown.includes('synthetic_unknown_value_canary')) throw new Error('synthetic_unknown_key_redaction_failed');
  if (serializedUnknown.includes(EXPECTED_CALLBACK) || serializedUnknown.includes(alternate)) throw new Error('synthetic_url_redaction_failed');
  if (badTop.validResponseShape !== false || badTop.fieldReturned !== null || nonJson.parsed !== false) throw new Error('synthetic_bad_response_failed');
  if (numericError.graphErrorCode !== 100 || numericError.graphErrorSubcode !== 33 || numericError.graphIsTransient !== false) throw new Error('synthetic_graph_error_allowlist_failed');
  if (invalidError.graphErrorCode !== null || invalidError.graphErrorSubcode !== null || invalidError.graphIsTransient !== null) throw new Error('synthetic_invalid_graph_error_failed');
  if (invocationMode([]) !== 'invalid' || invocationMode(['--execute']) !== 'execute' || invocationMode(['--self-test']) !== 'self-test') throw new Error('synthetic_invocation_mode_failed');
  process.stdout.write(JSON.stringify({ allThreeLayersDirectEqualDifferentEmptyMalformed: true, allThreeLayersNestedMatches: true, conflictingNestedValuesUnknown: true, mixedLayerMatchesRemainDistinct: true, absentOrMalformedUnknown: true, unknownKeysCountedAndRedacted: true, URLsAndCanaryValuesAbsentFromSerializedOutput: true, malformedResponseAndNumericErrorAllowlist: true, invocationModeGuard: true, networkCalled: false, resolverCalled: false, dbCalled: false }) + '\n');
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

module.exports = { parseWebhookConfigurationResponse, safeGraphError, invocationMode };
