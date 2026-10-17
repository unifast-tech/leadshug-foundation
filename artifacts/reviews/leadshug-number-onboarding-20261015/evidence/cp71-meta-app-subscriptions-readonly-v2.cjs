'use strict';

// CP71 preparation: one read-only Meta app-subscriptions GET. No token exchange,
// retries, redirects, pagination, raw body/header/error output or persistence.
const APP_ID = '874966345550148';
const GRAPH_VERSION = 'v26.0';
const GRAPH_HOST = 'graph.facebook.com';
const EXPECTED_CALLBACK = 'https://addressing-mar-perform-hormone.trycloudflare.com/webhooks/meta';
const MAX_RESPONSE_BYTES = 128 * 1024;
const REQUEST_TIMEOUT_MS = 10_000;
const TARGET_OBJECT = 'whatsapp_business_account';
const TARGET_FIELD = 'messages';

function typeOf(value) {
  if (value === null) return 'null';
  if (Array.isArray(value)) return 'array';
  return typeof value;
}

function unknownDescriptor() {
  return { active: null, callbackUrlPresent: null, callbackMatchesExpected: null,
    messagesPresent: null, messagesVersionMatchesConfigured: null,
    fieldEntryCount: null, unknownFieldEntryCount: null };
}

function parseSubscriptionsResponse(body) {
  const invalid = { validResponseShape: false, dataState: 'unknown', pagingPresent: null,
    rowCount: null, recognizedRowCount: null, unrecognizedRowCount: null,
    subscription: unknownDescriptor() };
  if (!body || typeof body !== 'object' || Array.isArray(body)) return invalid;
  if (!Object.prototype.hasOwnProperty.call(body, 'data')) {
    return { ...invalid, validResponseShape: true, dataState: 'missing', pagingPresent: Object.hasOwn(body, 'paging') };
  }
  if (!Array.isArray(body.data)) {
    return { ...invalid, validResponseShape: true, dataState: 'malformed', pagingPresent: Object.hasOwn(body, 'paging') };
  }

  const pagingPresent = Object.hasOwn(body, 'paging');
  const recognized = [];
  let malformedRowCount = 0;
  let unrecognizedRowCount = 0;
  for (const row of body.data) {
    if (!row || typeof row !== 'object' || Array.isArray(row) || typeof row.object !== 'string') {
      malformedRowCount += 1;
    } else if (row.object === TARGET_OBJECT) {
      recognized.push(row);
    } else {
      unrecognizedRowCount += 1;
    }
  }

  const result = { validResponseShape: true, dataState: 'array', pagingPresent,
    rowCount: body.data.length, recognizedRowCount: recognized.length,
    unrecognizedRowCount, malformedRowCount, subscription: unknownDescriptor() };
  if (pagingPresent || malformedRowCount > 0 || recognized.length > 1) return result;
  if (recognized.length === 0) {
    result.subscription.active = false;
    result.subscription.messagesPresent = false;
    result.subscription.messagesVersionMatchesConfigured = false;
    result.subscription.fieldEntryCount = 0;
    result.subscription.unknownFieldEntryCount = 0;
    return result;
  }

  const row = recognized[0];
  const sub = result.subscription;
  sub.active = typeof row.active === 'boolean' ? row.active : null;
  if (Object.hasOwn(row, 'callback_url') && typeof row.callback_url === 'string' && row.callback_url.length > 0) {
    sub.callbackUrlPresent = true;
    sub.callbackMatchesExpected = row.callback_url === EXPECTED_CALLBACK;
  } else if (Object.hasOwn(row, 'callback_url')) {
    sub.callbackUrlPresent = typeOf(row.callback_url) === 'string' ? false : null;
    sub.callbackMatchesExpected = null;
  } else {
    sub.callbackUrlPresent = false;
  }

  if (!Object.hasOwn(row, 'fields')) return result;
  if (!Array.isArray(row.fields)) return result;
  sub.fieldEntryCount = row.fields.length;
  let malformedField = false;
  let unknownFieldEntryCount = 0;
  const messagesEntries = [];
  for (const field of row.fields) {
    let name;
    let version;
    if (typeof field === 'string') {
      name = field;
      version = undefined;
    } else if (field && typeof field === 'object' && !Array.isArray(field) && typeof field.name === 'string') {
      name = field.name;
      version = field.version;
      unknownFieldEntryCount += Object.keys(field).filter((key) => key !== 'name' && key !== 'version').length;
    } else {
      malformedField = true;
      continue;
    }
    if (name === TARGET_FIELD) messagesEntries.push(version);
    else unknownFieldEntryCount += 1;
  }
  sub.unknownFieldEntryCount = unknownFieldEntryCount;
  if (malformedField) return result;
  sub.messagesPresent = messagesEntries.length > 0;
  if (messagesEntries.length === 0) sub.messagesVersionMatchesConfigured = false;
  else if (messagesEntries.length === 1 && typeof messagesEntries[0] === 'string') {
    sub.messagesVersionMatchesConfigured = messagesEntries[0] === GRAPH_VERSION;
  }
  return result;
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
    dataState: fields.dataState ?? null,
    pagingPresent: fields.pagingPresent ?? null,
    rowCount: fields.rowCount ?? null,
    recognizedRowCount: fields.recognizedRowCount ?? null,
    unrecognizedRowCount: fields.unrecognizedRowCount ?? null,
    malformedRowCount: fields.malformedRowCount ?? null,
    subscription: fields.subscription ?? null,
    graphErrorCode: fields.graphErrorCode ?? null,
    graphErrorSubcode: fields.graphErrorSubcode ?? null,
    graphIsTransient: fields.graphIsTransient ?? null,
  };
  process.stdout.write(JSON.stringify(allow) + '\n');
}

function parseBody(bytes) {
  try { return { parsed: true, value: JSON.parse(bytes.toString('utf8')) }; }
  catch { return { parsed: false, value: null }; }
}

function readSubscriptionsOnce(appToken) {
  const https = require('node:https');
  return new Promise((resolve) => {
    let finished = false;
    let size = 0;
    const chunks = [];
    let request;
    const finish = (result) => {
      if (finished) return;
      finished = true;
      clearTimeout(hardTimeout);
      resolve(result);
    };
    const hardTimeout = setTimeout(() => {
      if (request) request.destroy();
      finish({ outcome: 'timeout' });
    }, REQUEST_TIMEOUT_MS);
    request = https.request({
      protocol: 'https:', hostname: GRAPH_HOST, servername: GRAPH_HOST, port: 443,
      method: 'GET', path: `/${GRAPH_VERSION}/${APP_ID}/subscriptions`,
      headers: { Authorization: `Bearer ${appToken}`, Connection: 'close' },
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
        const parsed = parseBody(Buffer.concat(chunks, size));
        if (status !== 200) return finish({ outcome: 'http_non_200', httpStatus: status, ...(parsed.parsed ? safeGraphError(parsed.value) : {}) });
        if (!parsed.parsed) return finish({ outcome: 'invalid_response', httpStatus: 200 });
        finish({ outcome: 'http_200', httpStatus: 200, ...parseSubscriptionsResponse(parsed.value) });
      });
      response.on('error', () => finish({ outcome: 'transport_error', httpStatus: status }));
    });
    request.on('timeout', () => { request.destroy(); finish({ outcome: 'timeout' }); });
    request.on('error', () => finish({ outcome: 'transport_error' }));
    request.end();
  });
}

function selfTest() {
  const valid = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: true, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] }] });
  const disabled = parseSubscriptionsResponse({ data: [] });
  const explicitDisabled = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: false, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] }] });
  const missingActive = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] }] });
  const malformedActiveString = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: 'false', callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] }] });
  const malformedActiveNumber = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: 0, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] }] });
  const wrongCallback = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: true, callback_url: 'https://synthetic.invalid/callback-canary', fields: [{ name: 'messages', version: GRAPH_VERSION }] }] });
  const missingMessages = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: true, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'message_status', version: GRAPH_VERSION }] }] });
  const malformed = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: true, callback_url: 17, fields: [null] }] });
  const missingArray = parseSubscriptionsResponse({ paging: {} });
  const duplicate = parseSubscriptionsResponse({ data: [
    { object: TARGET_OBJECT, active: true, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] },
    { object: TARGET_OBJECT, active: true, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] },
  ] });
  const paged = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: true, callback_url: EXPECTED_CALLBACK, fields: [{ name: 'messages', version: GRAPH_VERSION }] }], paging: { next: 'https://synthetic.invalid/canary' } });
  const unknown = parseSubscriptionsResponse({ data: [{ object: TARGET_OBJECT, active: true, callback_url: 'https://synthetic.invalid/URL_CANARY', fields: [{ name: 'messages', version: GRAPH_VERSION, synthetic_field_name_canary: 'secret-canary' }] }] });
  const serialized = JSON.stringify({ wrongCallback, paged, unknown, safeError: safeGraphError({ error: { code: 100, error_subcode: 33, is_transient: false, message: 'error-string-canary', fbtrace_id: 'trace-canary' } }) });
  if (valid.subscription.active !== true || valid.subscription.callbackMatchesExpected !== true || valid.subscription.messagesPresent !== true || valid.subscription.messagesVersionMatchesConfigured !== true) throw new Error('synthetic_valid_subscription_failed');
  if (disabled.subscription.active !== false || disabled.subscription.messagesPresent !== false) throw new Error('synthetic_disabled_subscription_failed');
  if (explicitDisabled.subscription.active !== false) throw new Error('synthetic_explicit_disabled_flag_failed');
  if (missingActive.subscription.active !== null || malformedActiveString.subscription.active !== null || malformedActiveNumber.subscription.active !== null) throw new Error('synthetic_missing_or_malformed_active_unknown_failed');
  if (wrongCallback.subscription.active !== true || wrongCallback.subscription.callbackMatchesExpected !== false) throw new Error('synthetic_wrong_callback_failed');
  if (missingMessages.subscription.messagesPresent !== false || missingMessages.subscription.messagesVersionMatchesConfigured !== false) throw new Error('synthetic_missing_messages_failed');
  if (malformed.subscription.active !== true || malformed.subscription.callbackMatchesExpected !== null || malformed.subscription.messagesPresent !== null) throw new Error('synthetic_malformed_fields_unknown_failed');
  if (missingArray.dataState !== 'missing' || missingArray.subscription.active !== null) throw new Error('synthetic_missing_array_unknown_failed');
  if (duplicate.recognizedRowCount !== 2 || duplicate.subscription.active !== null) throw new Error('synthetic_duplicate_unknown_failed');
  if (paged.pagingPresent !== true || paged.subscription.active !== null || paged.subscription.messagesPresent !== null) throw new Error('synthetic_paging_unknown_failed');
  if (serialized.includes('synthetic.invalid') || serialized.includes('URL_CANARY') || serialized.includes('synthetic_field_name_canary') || serialized.includes('secret-canary') || serialized.includes('error-string-canary') || serialized.includes('trace-canary')) throw new Error('synthetic_output_redaction_failed');
  if (safeGraphError({ error: { code: '100', error_subcode: -1, is_transient: 'false' } }).graphErrorCode !== null) throw new Error('synthetic_error_allowlist_failed');
  if (invocationMode([]) !== 'invalid' || invocationMode(['--execute']) !== 'execute' || invocationMode(['--self-test']) !== 'self-test') throw new Error('synthetic_invocation_guard_failed');
  process.stdout.write(JSON.stringify({ validSubscriptionRecognized: true, disabledAndMalformedRemainDistinct: true, wrongCallbackAndMissingMessagesRecognized: true, duplicatesAndPagingRemainUnknown: true, syntheticURLsFieldNamesAndErrorStringsRedacted: true, numericGraphErrorAllowlist: true, invocationGuard: true, networkCalled: false, appSecretRead: false }) + '\n');
}

async function main() {
  const mode = invocationMode(process.argv.slice(2));
  if (mode === 'self-test') { selfTest(); return 0; }
  if (mode !== 'execute') {
    safeOutput({ outcome: 'invalid_invocation' });
    return 2;
  }
  if (process.env.META_APP_ID !== APP_ID || process.env.GRAPH_VERSION?.trim() !== GRAPH_VERSION) {
    safeOutput({ outcome: 'runtime_public_config_mismatch' });
    return 2;
  }
  const appSecret = process.env.META_APP_SECRET;
  if (typeof appSecret !== 'string' || appSecret.length === 0) {
    safeOutput({ outcome: 'app_secret_unavailable' });
    return 2;
  }
  const appToken = `${APP_ID}|${appSecret}`;
  try {
    const result = await readSubscriptionsOnce(appToken);
    safeOutput(result);
    return result.outcome === 'http_200' ? 0 : 1;
  } catch {
    safeOutput({ outcome: 'request_failed' });
    return 1;
  }
}

main().then((code) => { process.exitCode = code; }).catch(() => {
  safeOutput({ outcome: 'execution_failed' });
  process.exitCode = 1;
});

module.exports = { parseSubscriptionsResponse, safeGraphError, invocationMode };
