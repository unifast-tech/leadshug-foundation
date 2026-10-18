'use strict';

// CP80 preparation only. Read-only scoped snapshot; execute only after a separate root GO.
// No Nest bootstrap, provider calls, credential resolver, or business writes.
const PIN = Object.freeze({
  anchorBusinessUnitId: 'a1492634-8685-46d8-a7cb-685a99f5c930',
  targetBusinessUnitName: 'Teste Meta',
});
const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const ATTEMPT_ID_RE = /^[0-9a-f]{32}$/i;
const CHANNEL_STATUS = new Set(['CONECTANDO', 'CONECTADO', 'DESCONECTADO', 'DESLOGADO']);
const ATTEMPT_STATES = new Set(['PENDING_AUTH', 'PENDING_NUMBER', 'REGISTERING', 'PENDING_RECEIPT', 'CONNECTED', 'ERROR', 'CANCELLED']);
const ATTEMPT_STAGES = new Set(['RESERVED', 'AUTHORIZING', 'AUTHORIZED', 'PENDING_NUMBER', 'REGISTERING', 'SUBSCRIBED', 'RECEIPT_VERIFIED', 'CONNECTED', 'ERROR', 'CANCELLED', 'VERIFYING', 'AWAITING_RECEIPT']);
const CONNECTION_STATES = new Set(['PENDING', 'SUBSCRIBED', 'CONNECTED', 'DISCONNECTED', 'OPEN', 'CLOSED', 'ERROR', 'ACTIVE', 'INACTIVE', 'UNKNOWN']);
const CLEANUP_STATES = new Set(['UNMANAGED', 'ACTIVE', 'PENDING', 'CLEANUP_PENDING', 'CLEANING', 'CLEANED', 'FAILED']);
const MESSAGE_DIRECTIONS = new Set(['IN', 'OUT']);
const MESSAGE_STATUSES = new Set(['RECEBIDA', 'ENVIADA', 'ENTREGUE', 'LIDA', 'FALHOU']);
const CUT_OFF_EVENT_TYPE = 'meta.webhook';

function isUuid(value) { return typeof value === 'string' && UUID_RE.test(value); }
function isAttemptId(value) { return typeof value === 'string' && ATTEMPT_ID_RE.test(value); }
function isSafeInteger(value, min = 0) { return Number.isSafeInteger(value) && value >= min; }
function safeDate(value) { return value instanceof Date && Number.isFinite(value.getTime()); }
function safeNullableDate(value) { return value === null || safeDate(value); }
function enumOrUnknown(value, choices) { return typeof value === 'string' && choices.has(value) ? value : 'UNKNOWN'; }
function safeFailure(stage) {
  const allowed = new Set(['anchor_guard', 'target_business_unit_guard', 'channel_cardinality_guard', 'channel_shape_guard', 'current_attempt_guard', 'identity_guard', 'credential_count_guard', 'aggregate_shape_guard', 'database_snapshot']);
  return { checkpoint: 'cp80-sandbox-binding-baseline-readonly', status: 'inconclusive', failureStage: allowed.has(stage) ? stage : 'database_snapshot' };
}

// Pure projection/guard used by the DB path and offline synthetic controls.
function projectScope(input, now = new Date()) {
  if (!input || !input.anchor || input.anchor.id !== PIN.anchorBusinessUnitId ||
      !isUuid(input.anchor.id) || !isUuid(input.anchor.mantenedoraId)) return safeFailure('anchor_guard');
  if (!Array.isArray(input.targetBusinessUnitIds) || input.targetBusinessUnitIds.length !== 1 ||
      !isUuid(input.targetBusinessUnitIds[0])) return safeFailure('target_business_unit_guard');
  const buId = input.targetBusinessUnitIds[0];
  if (!Array.isArray(input.channels) || input.channels.length !== 1) return safeFailure('channel_cardinality_guard');
  const channel = input.channels[0];
  if (!channel || !isUuid(channel.id) || channel.buId !== buId || channel.type !== 'OFICIAL' ||
      !isSafeInteger(channel.generation, 1) || !isSafeInteger(channel.pairingEpoch) ||
      !(channel.verifiedEpoch === null || isSafeInteger(channel.verifiedEpoch)) ||
      typeof channel.ownNumberVerified !== 'boolean' || typeof channel.status !== 'string' ||
      typeof channel.providerConnectionState !== 'string' ||
      !(channel.currentAttemptId === null || isAttemptId(channel.currentAttemptId)) ||
      !safeNullableDate(channel.receiptVerifiedAt) || !safeNullableDate(channel.connectedAt) ||
      !safeNullableDate(channel.operationLeaseUntil)) return safeFailure('channel_shape_guard');
  if (!channel.currentAttemptId || !Array.isArray(input.attempts) || input.attempts.length !== 1) return safeFailure('current_attempt_guard');
  const attempt = input.attempts[0];
  if (!attempt || attempt.id !== channel.currentAttemptId || !isAttemptId(attempt.id) ||
      attempt.buId !== buId || attempt.channelId !== channel.id || attempt.type !== 'OFICIAL' ||
      attempt.generation !== channel.generation || !ATTEMPT_STATES.has(attempt.state) ||
      !isSafeInteger(attempt.version, 1) || !(attempt.pairingEpoch === null || isSafeInteger(attempt.pairingEpoch)) ||
      typeof attempt.stage !== 'string' || !safeNullableDate(attempt.leaseUntil)) return safeFailure('current_attempt_guard');
  if (!Array.isArray(input.identities) || input.identities.length !== 1) return safeFailure('identity_guard');
  const identity = input.identities[0];
  if (!identity || !isUuid(identity.id) || identity.buId !== buId || identity.provider !== 'OFICIAL' ||
      identity.currentChannelId !== channel.id || identity.retiredAt !== null ||
      typeof identity.managedLifecycle !== 'boolean' || typeof identity.cleanupState !== 'string' ||
      !safeNullableDate(identity.cleanupLeaseUntil)) return safeFailure('identity_guard');
  if (!isSafeInteger(input.credentialCount)) return safeFailure('credential_count_guard');
  if (!safeDate(now)) return safeFailure('aggregate_shape_guard');
  return {
    checkpoint: 'cp80-sandbox-binding-baseline-readonly', status: 'snapshot',
    targetBusinessUnitId: buId,
    channel: {
      id: channel.id, buId: channel.buId, type: channel.type,
      status: enumOrUnknown(channel.status, CHANNEL_STATUS),
      generation: channel.generation, currentAttemptId: channel.currentAttemptId,
      pairingEpoch: channel.pairingEpoch, verifiedEpoch: channel.verifiedEpoch,
      ownNumberVerified: channel.ownNumberVerified,
      providerConnectionState: enumOrUnknown(channel.providerConnectionState, CONNECTION_STATES),
      receiptPresent: channel.receiptVerifiedAt !== null,
      connectedAtPresent: channel.connectedAt !== null,
      channelLeaseActive: channel.operationLeaseUntil !== null && channel.operationLeaseUntil > now,
    },
    currentAttempt: {
      id: attempt.id, state: attempt.state,
      stage: enumOrUnknown(attempt.stage, ATTEMPT_STAGES), version: attempt.version,
      generation: attempt.generation, pairingEpoch: attempt.pairingEpoch,
      leaseActive: attempt.leaseUntil !== null && attempt.leaseUntil > now,
    },
    identity: {
      id: identity.id, currentMappingVerified: true,
      managedLifecycle: identity.managedLifecycle,
      cleanupState: enumOrUnknown(identity.cleanupState, CLEANUP_STATES),
      cleanupLeaseActive: identity.cleanupLeaseUntil !== null && identity.cleanupLeaseUntil > now,
    },
    credential: { currentGenerationCount: input.credentialCount, activeForCurrentGeneration: input.credentialCount === 1 },
  };
}

function safeCount(value) { return Number.isSafeInteger(value) && value >= 0 ? value : null; }
function projectAggregates(messages, conversationCount, webhook) {
  if (!Array.isArray(messages) || !isSafeInteger(conversationCount) || !webhook ||
      !isSafeInteger(webhook.count) || !(webhook.minReceivedAt === null || safeDate(webhook.minReceivedAt)) ||
      !(webhook.maxReceivedAt === null || safeDate(webhook.maxReceivedAt))) return null;
  const counts = { inbound: 0, outbound: 0, messageStatusBuckets: [] };
  for (const row of messages) {
    if (!row || !MESSAGE_DIRECTIONS.has(row.direction) || !MESSAGE_STATUSES.has(row.status) || !isSafeInteger(row.count)) return null;
    if (row.direction === 'IN') counts.inbound += row.count;
    if (row.direction === 'OUT') counts.outbound += row.count;
    counts.messageStatusBuckets.push({ direction: row.direction, status: row.status, count: row.count });
  }
  counts.messageStatusBuckets.sort((a, b) => `${a.direction}:${a.status}`.localeCompare(`${b.direction}:${b.status}`));
  return {
    messages: { ...counts, conversationCount },
    webhookAggregate: {
      count: webhook.count,
      minReceivedAtUtc: webhook.minReceivedAt ? webhook.minReceivedAt.toISOString() : null,
      maxReceivedAtUtc: webhook.maxReceivedAt ? webhook.maxReceivedAt.toISOString() : null,
      payloadSelectedOrFiltered: false,
      identityAttributionAvailable: false,
    },
  };
}

function selfTest() {
  const anchor = { id: PIN.anchorBusinessUnitId, mantenedoraId: 'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' };
  const buId = 'bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb';
  const channel = { id: 'cccccccc-cccc-4ccc-8ccc-cccccccccccc', buId, type: 'OFICIAL', status: 'CONECTANDO', generation: 1, currentAttemptId: 'dddddddddddddddddddddddddddddddd', pairingEpoch: 1, verifiedEpoch: 0, ownNumberVerified: false, providerConnectionState: 'SUBSCRIBED', receiptVerifiedAt: null, connectedAt: null, operationLeaseUntil: null };
  const attempt = { id: channel.currentAttemptId, buId, channelId: channel.id, type: 'OFICIAL', state: 'PENDING_RECEIPT', stage: 'SUBSCRIBED', version: 2, generation: 1, pairingEpoch: 1, leaseUntil: null };
  const identity = { id: 'eeeeeeee-eeee-4eee-8eee-eeeeeeeeeeee', buId, provider: 'OFICIAL', currentChannelId: channel.id, retiredAt: null, managedLifecycle: true, cleanupState: 'ACTIVE', cleanupLeaseUntil: null };
  const base = { anchor, targetBusinessUnitIds: [buId], channels: [channel], attempts: [attempt], identities: [identity], credentialCount: 1 };
  const valid = projectScope(base, new Date('2026-10-18T00:00:00Z'));
  const multipleBus = projectScope({ ...base, targetBusinessUnitIds: [buId, 'ffffffff-ffff-4fff-8fff-ffffffffffff'] });
  const multipleChannels = projectScope({ ...base, channels: [channel, { ...channel, id: 'ffffffff-ffff-4fff-8fff-ffffffffffff' }] });
  const driftedAttempt = projectScope({ ...base, attempts: [{ ...attempt, buId: 'ffffffff-ffff-4fff-8fff-ffffffffffff' }] });
  const unmappedIdentity = projectScope({ ...base, identities: [{ ...identity, currentChannelId: null }] });
  const malformedCredentialCount = projectScope({ ...base, credentialCount: -1 });
  const noCredential = projectScope({ ...base, credentialCount: 0 });
  const arbitraryStrings = projectScope({ ...base, channel: undefined, channels: [{ ...channel, status: 'SYNTHETIC_PRIVATE_STATE_CANARY', providerConnectionState: 'SYNTHETIC_PRIVATE_CONNECTION_CANARY' }], attempts: [{ ...attempt, stage: 'SYNTHETIC_PRIVATE_STAGE_CANARY' }], identities: [{ ...identity, cleanupState: 'SYNTHETIC_PRIVATE_CLEANUP_CANARY' }] });
  const projectedCounts = projectAggregates([{ direction: 'IN', status: 'RECEBIDA', count: 2 }, { direction: 'OUT', status: 'ENVIADA', count: 1 }], 1, { count: 3, minReceivedAt: new Date('2026-10-18T00:00:00Z'), maxReceivedAt: new Date('2026-10-18T00:01:00Z') });
  const serialized = JSON.stringify([valid, multipleBus, multipleChannels, driftedAttempt, unmappedIdentity, malformedCredentialCount, noCredential, arbitraryStrings, projectedCounts]);
  if (valid.status !== 'snapshot' || valid.currentAttempt.id !== attempt.id) throw new Error('synthetic_valid_projection_failed');
  if (multipleBus.failureStage !== 'target_business_unit_guard' || multipleChannels.failureStage !== 'channel_cardinality_guard') throw new Error('synthetic_ambiguity_guard_failed');
  if (driftedAttempt.failureStage !== 'current_attempt_guard' || unmappedIdentity.failureStage !== 'identity_guard') throw new Error('synthetic_mapping_guard_failed');
  if (malformedCredentialCount.failureStage !== 'credential_count_guard' || noCredential.credential.activeForCurrentGeneration !== false) throw new Error('synthetic_credential_count_guard_failed');
  if (arbitraryStrings.channel.status !== 'UNKNOWN' || arbitraryStrings.channel.providerConnectionState !== 'UNKNOWN' || arbitraryStrings.currentAttempt.stage !== 'UNKNOWN' || arbitraryStrings.identity.cleanupState !== 'UNKNOWN') throw new Error('synthetic_string_allowlist_failed');
  if (serialized.includes('SYNTHETIC_PRIVATE') || serialized.includes(anchor.mantenedoraId)) throw new Error('synthetic_redaction_failed');
  if (!projectedCounts || projectedCounts.messages.inbound !== 2 || projectedCounts.messages.outbound !== 1 || projectedCounts.webhookAggregate.identityAttributionAvailable !== false) throw new Error('synthetic_aggregate_projection_failed');
  if (projectAggregates([{ direction: 'IN', status: 'SYNTHETIC_PRIVATE_STATUS', count: 1 }], 0, { count: 0, minReceivedAt: null, maxReceivedAt: null }) !== null) throw new Error('synthetic_invalid_aggregate_rejected_failed');
  process.stdout.write(JSON.stringify({ syntheticCasesPassed: 8, databaseCalled: false, providerCalled: false, resolverImported: false, privateFieldsEmitted: false }) + '\n');
}

function invocationMode(args) {
  if (args.length === 1 && args[0] === '--execute') return 'execute';
  if (args.length === 1 && args[0] === '--self-test') return 'self-test';
  return 'invalid';
}

async function main() {
  const mode = invocationMode(process.argv.slice(2));
  if (mode === 'self-test') { selfTest(); return 0; }
  if (mode !== 'execute') {
    process.stdout.write(JSON.stringify({ checkpoint: 'cp80-sandbox-binding-baseline-readonly', status: 'not_executed', requiredFlag: '--execute' }) + '\n');
    return 2;
  }
  let prisma;
  try {
    const { PrismaClient } = require('@prisma/client');
    prisma = new PrismaClient();
    let result;
    try {
      result = await prisma.$transaction(async (tx) => {
        await tx.$executeRawUnsafe('SET TRANSACTION READ ONLY');
        const anchor = await tx.businessUnit.findUnique({ where: { id: PIN.anchorBusinessUnitId }, select: { id: true, mantenedoraId: true } });
        if (!anchor || anchor.id !== PIN.anchorBusinessUnitId || !isUuid(anchor.mantenedoraId)) return safeFailure('anchor_guard');
        const targets = await tx.businessUnit.findMany({ where: { name: PIN.targetBusinessUnitName, mantenedoraId: anchor.mantenedoraId }, select: { id: true }, take: 2 });
        const targetIds = Array.isArray(targets) ? targets.map((x) => x && x.id) : null;
        if (!targetIds || targetIds.length !== 1 || !isUuid(targetIds[0])) return safeFailure('target_business_unit_guard');
        const buId = targetIds[0];
        const channels = await tx.buChannel.findMany({
          where: { buId, type: 'OFICIAL' }, take: 2,
          select: { id: true, buId: true, type: true, status: true, generation: true, currentAttemptId: true, pairingEpoch: true, verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true, receiptVerifiedAt: true, connectedAt: true, operationLeaseUntil: true },
        });
        if (!Array.isArray(channels) || channels.length !== 1) return safeFailure('channel_cardinality_guard');
        const channel = channels[0];
        const attempts = channel && isAttemptId(channel.currentAttemptId) ? await tx.channelRegistrationAttempt.findMany({
          where: { id: channel.currentAttemptId, buId, channelId: channel.id, type: 'OFICIAL', generation: channel.generation }, take: 2,
          select: { id: true, buId: true, channelId: true, type: true, state: true, stage: true, version: true, generation: true, pairingEpoch: true, leaseUntil: true },
        }) : [];
        const identities = channel && isUuid(channel.id) ? await tx.providerResourceIdentity.findMany({
          where: { buId, provider: 'OFICIAL', currentChannelId: channel.id, retiredAt: null }, take: 2,
          select: { id: true, buId: true, provider: true, currentChannelId: true, retiredAt: true, managedLifecycle: true, cleanupState: true, cleanupLeaseUntil: true },
        }) : [];
        const credentialCount = channel && isSafeInteger(channel.generation, 1) ? await tx.channelCredential.count({
          where: { channelId: channel.id, buId, provider: 'OFICIAL', generation: channel.generation },
        }) : -1;
        const projected = projectScope({ anchor, targetBusinessUnitIds: targetIds, channels, attempts, identities, credentialCount });
        if (projected.status !== 'snapshot') return projected;
        const identityId = identities[0].id;
        const grouped = await tx.message.groupBy({
          by: ['direction', 'status'],
          where: { buId, providerResourceIdentityId: identityId, channelOrigin: 'OFICIAL' },
          _count: { _all: true },
        });
        const groupedSafe = Array.isArray(grouped) ? grouped.map((row) => ({ direction: row.direction, status: row.status, count: row._count && row._count._all })) : null;
        const conversationCount = await tx.conversation.count({ where: { buId, messages: { some: { providerResourceIdentityId: identityId, channelOrigin: 'OFICIAL' } } } });
        const webhook = await tx.webhookEvent.aggregate({
          where: { buId, channel: 'OFICIAL', eventType: CUT_OFF_EVENT_TYPE },
          _count: { _all: true }, _min: { receivedAt: true }, _max: { receivedAt: true },
        });
        const aggregate = projectAggregates(groupedSafe, conversationCount, { count: webhook && webhook._count && webhook._count._all, minReceivedAt: webhook && webhook._min && webhook._min.receivedAt, maxReceivedAt: webhook && webhook._max && webhook._max.receivedAt });
        if (!aggregate) return safeFailure('aggregate_shape_guard');
        return { ...projected, ...aggregate, boundary: { readOnlyTransaction: true, providerOrGraphHttp: false, credentialOrEnvironmentDump: false, messageRowsOrContentSelected: false, webhookPayloadSelectedOrFiltered: false } };
      }, { isolationLevel: 'RepeatableRead', timeout: 10000, maxWait: 5000 });
    } catch {
      result = safeFailure('database_snapshot');
    }
    process.stdout.write(JSON.stringify(result) + '\n');
    return result && result.status === 'snapshot' ? 0 : 1;
  } finally {
    if (prisma) await prisma.$disconnect().catch(() => {});
  }
}

if (require.main === module) {
  main().then((code) => { process.exitCode = code; }).catch(() => {
    process.stdout.write(JSON.stringify(safeFailure('database_snapshot')) + '\n');
    process.exitCode = 1;
  });
}

module.exports = { projectScope, projectAggregates, invocationMode };
