'use strict';

// CP75 preparation only: read WABA owner_business_info once after a separate root GO.
// Run inside the pinned owned API container; this file never writes application data.
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
const EXPECTED_OWNER_BUSINESS_ID = '1435146480239867';
const GRAPH_HOST = 'graph.facebook.com';
const GRAPH_VERSION = 'v26.0';
const GRAPH_PATH_PREFIX = `/${GRAPH_VERSION}/`;
const MAX_RESPONSE_BYTES = 128 * 1024;
const REQUEST_TIMEOUT_MS = 10_000;

function parseOwnerBusinessInfoResponse(body) {
  const validResponseShape = Boolean(body && typeof body === 'object' && !Array.isArray(body));
  if (!validResponseShape) {
    return { validResponseShape: false, ownerBusinessInfoPresent: null, ownerBusinessInfoType: 'unknown', ownerBusinessInfoShape: 'invalid_top_level', ownerBusinessMatchesExpected: null };
  }
  const present = Object.prototype.hasOwnProperty.call(body, 'owner_business_info');
  if (!present) {
    return { validResponseShape: true, ownerBusinessInfoPresent: false, ownerBusinessInfoType: 'missing', ownerBusinessInfoShape: 'missing', ownerBusinessMatchesExpected: null };
  }
  const field = body.owner_business_info;
  const type = field === null ? 'null' : Array.isArray(field) ? 'array' : typeof field;
  if (field === null) {
    return { validResponseShape: true, ownerBusinessInfoPresent: true, ownerBusinessInfoType: type, ownerBusinessInfoShape: 'null', ownerBusinessMatchesExpected: null };
  }
  if (!field || typeof field !== 'object' || Array.isArray(field)) {
    return { validResponseShape: true, ownerBusinessInfoPresent: true, ownerBusinessInfoType: type, ownerBusinessInfoShape: 'non_object', ownerBusinessMatchesExpected: null };
  }
  if (!Object.prototype.hasOwnProperty.call(field, 'id')) {
    return { validResponseShape: true, ownerBusinessInfoPresent: true, ownerBusinessInfoType: type, ownerBusinessInfoShape: 'object_missing_id', ownerBusinessMatchesExpected: null };
  }
  if (typeof field.id !== 'string' || field.id.length === 0) {
    return { validResponseShape: true, ownerBusinessInfoPresent: true, ownerBusinessInfoType: type, ownerBusinessInfoShape: 'object_invalid_id', ownerBusinessMatchesExpected: null };
  }
  return {
    validResponseShape: true,
    ownerBusinessInfoPresent: true,
    ownerBusinessInfoType: type,
    ownerBusinessInfoShape: 'object_with_string_id',
    ownerBusinessMatchesExpected: field.id === EXPECTED_OWNER_BUSINESS_ID,
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
  const equal = parseOwnerBusinessInfoResponse({ owner_business_info: { id: EXPECTED_OWNER_BUSINESS_ID } });
  const different = parseOwnerBusinessInfoResponse({ owner_business_info: { id: 'synthetic-different-owner' } });
  const missing = parseOwnerBusinessInfoResponse({ other_field: 'synthetic-owner-canary' });
  const nullField = parseOwnerBusinessInfoResponse({ owner_business_info: null });
  const malformedTop = parseOwnerBusinessInfoResponse([]);
  const malformedArray = parseOwnerBusinessInfoResponse({ owner_business_info: [] });
  const malformedString = parseOwnerBusinessInfoResponse({ owner_business_info: 'synthetic-owner-canary' });
  const missingId = parseOwnerBusinessInfoResponse({ owner_business_info: { other: 'synthetic-owner-canary' } });
  const invalidId = parseOwnerBusinessInfoResponse({ owner_business_info: { id: 42 } });
  const emptyId = parseOwnerBusinessInfoResponse({ owner_business_info: { id: '' } });
  const unknownShape = parseOwnerBusinessInfoResponse({ owner_business_info: true });
  const safeError = safeGraphError({ error: { code: 100, error_subcode: 123, is_transient: false, message: 'synthetic secret text', type: 'synthetic', fbtrace_id: 'synthetic' } });
  const invalidError = safeGraphError({ error: { code: '100', error_subcode: -1, is_transient: 'false', message: 'discard' } });
  const serialized = JSON.stringify([equal, different, missing, nullField, malformedTop, malformedArray, malformedString, missingId, invalidId, emptyId, unknownShape, safeError, invalidError]);
  if (equal.ownerBusinessMatchesExpected !== true || equal.ownerBusinessInfoShape !== 'object_with_string_id') throw new Error('synthetic_owner_equal_failed');
  if (different.ownerBusinessMatchesExpected !== false) throw new Error('synthetic_owner_different_failed');
  if (missing.ownerBusinessInfoPresent !== false || missing.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_missing_failed');
  if (nullField.ownerBusinessInfoType !== 'null' || nullField.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_null_failed');
  if (malformedTop.validResponseShape !== false || malformedTop.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_top_shape_failed');
  if (malformedArray.ownerBusinessInfoType !== 'array' || malformedArray.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_array_failed');
  if (malformedString.ownerBusinessInfoType !== 'string' || malformedString.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_string_failed');
  if (missingId.ownerBusinessInfoShape !== 'object_missing_id' || missingId.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_id_missing_failed');
  if (invalidId.ownerBusinessInfoShape !== 'object_invalid_id' || invalidId.ownerBusinessMatchesExpected !== null || emptyId.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_id_invalid_failed');
  if (unknownShape.ownerBusinessInfoShape !== 'non_object' || unknownShape.ownerBusinessMatchesExpected !== null) throw new Error('synthetic_owner_unknown_shape_failed');
  if (safeError.graphErrorCode !== 100 || safeError.graphErrorSubcode !== 123 || safeError.graphIsTransient !== false) throw new Error('synthetic_error_allowlist_failed');
  if (invalidError.graphErrorCode !== null || invalidError.graphErrorSubcode !== null || invalidError.graphIsTransient !== null) throw new Error('synthetic_invalid_error_failed');
  if (serialized.includes(EXPECTED_OWNER_BUSINESS_ID) || serialized.includes('synthetic-owner-canary') || serialized.includes('synthetic secret text')) throw new Error('synthetic_output_redaction_failed');
  if (invocationMode([]) !== 'invalid' || invocationMode(['--execute']) !== 'execute' || invocationMode(['--self-test']) !== 'self-test') throw new Error('synthetic_invocation_contract_failed');
  process.stdout.write(JSON.stringify({ syntheticCasesPassed: 12, networkCalled: false, resolverCalled: false, identifiersOrRawGraphTextEmitted: false }) + '\n');
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
    validResponseShape: fields.validResponseShape ?? null,
    ownerBusinessInfoPresent: fields.ownerBusinessInfoPresent ?? null,
    ownerBusinessInfoType: fields.ownerBusinessInfoType ?? 'unknown',
    ownerBusinessInfoShape: fields.ownerBusinessInfoShape ?? 'unknown',
    ownerBusinessMatchesExpected: fields.ownerBusinessMatchesExpected ?? null,
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
          finish({ outcome: 'http_200', httpStatus: 200, parsed: parseOwnerBusinessInfoResponse(body) });
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

    const url = `https://${GRAPH_HOST}${GRAPH_PATH_PREFIX}${encodeURIComponent(resolved.wabaId)}?fields=owner_business_info`;
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

module.exports = { parseOwnerBusinessInfoResponse };
