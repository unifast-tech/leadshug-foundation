#!/usr/bin/env node
'use strict';

// One guarded, read-only Prisma metadata/count snapshot for the known official
// test channel. Invoke explicitly with --execute only after separately checking
// the exact API container/image/owner pins. No Nest bootstrap or provider calls.
const { PrismaClient } = require('@prisma/client');

const PIN = Object.freeze({
  buId: "fe046ba1-289e-4d00-85f1-56a885c33b4b",
  channelId: "182dab05-a864-4935-b2b5-2c091da4d06f",
  identityId: "40aa8180-9371-45df-8759-3d36602db001",
  attemptId: "fcba4a8ed1a9c87e740fea3e07e7e8d1",
  generation: 2,
  epoch: 0,
  cutoffUtc: "2026-10-18T04:21:09.340235Z",
});

function safeDate(value) {
  return value instanceof Date && Number.isFinite(value.getTime())
    ? value.toISOString()
    : null;
}

function safeFailure(stage) {
  return { checkpoint: 'cp80-sandbox-inout-aggregate-readonly', status: 'inconclusive', failureStage: stage };
}

async function main() {
  if (process.argv.length !== 3 || process.argv[2] !== '--execute') {
    process.stdout.write(JSON.stringify({ checkpoint: 'cp80-sandbox-inout-aggregate-readonly', status: 'not_executed', requiredFlag: '--execute' }) + '\n');
    return 2;
  }

  const prisma = new PrismaClient();
  let result;
  try {
    result = await prisma.$transaction(async (tx) => {
      await tx.$executeRawUnsafe('SET TRANSACTION READ ONLY');

      const bu = await tx.businessUnit.findUnique({ where: { id: PIN.buId }, select: { id: true } });
      if (!bu || bu.id !== PIN.buId) return safeFailure('business_unit_guard');

      const channel = await tx.buChannel.findUnique({
        where: { id: PIN.channelId },
        select: {
          id: true, buId: true, type: true, status: true, generation: true,
          currentAttemptId: true, pairingEpoch: true, verifiedEpoch: true,
          ownNumberVerified: true, providerConnectionState: true,
          receiptVerifiedAt: true, connectedAt: true, operationLeaseUntil: true,
        },
      });
      if (!channel || channel.id !== PIN.channelId || channel.buId !== PIN.buId ||
          channel.type !== 'OFICIAL' || channel.generation !== PIN.generation ||
          channel.pairingEpoch !== PIN.epoch) return safeFailure('channel_guard');

      const attempts = await tx.channelRegistrationAttempt.findMany({
        where: { id: PIN.attemptId, buId: PIN.buId, channelId: PIN.channelId, type: 'OFICIAL', generation: PIN.generation },
        select: { id: true, state: true, stage: true, version: true, generation: true, pairingEpoch: true, leaseUntil: true },
        take: 2,
      });
      if (attempts.length !== 1 || attempts[0].id !== channel.currentAttemptId || attempts[0].id !== PIN.attemptId) {
        return safeFailure('current_attempt_guard');
      }

      const identity = await tx.providerResourceIdentity.findUnique({
        where: { id: PIN.identityId },
        select: { id: true, buId: true, provider: true, currentChannelId: true, retiredAt: true, managedLifecycle: true, cleanupState: true, cleanupLeaseUntil: true },
      });
      const identityMappingCount = await tx.providerResourceIdentity.count({
        where: { buId: PIN.buId, provider: 'OFICIAL', currentChannelId: PIN.channelId, retiredAt: null },
      });
      if (!identity || identity.id !== PIN.identityId || identity.buId !== PIN.buId ||
          identity.provider !== 'OFICIAL' || identity.currentChannelId !== PIN.channelId ||
          identity.retiredAt !== null || identityMappingCount !== 1) return safeFailure('identity_guard');

      const activeCredentialCount = await tx.channelCredential.count({
        where: { channelId: PIN.channelId, buId: PIN.buId, provider: 'OFICIAL', generation: PIN.generation },
      });
      const cutoff = new Date(PIN.cutoffUtc);
      // The pinned baseline has a non-zero sub-millisecond fraction; round
      // parsed .633 milliseconds up to .634 to avoid pre-baseline rows.
      cutoff.setTime(cutoff.getTime() + 1);
      const since = { gte: cutoff };
      const groupedMessages = await tx.message.groupBy({
        by: ['direction', 'status'],
        where: { buId: PIN.buId, providerResourceIdentityId: PIN.identityId, channelOrigin: 'OFICIAL', createdAt: since },
        _count: { _all: true },
      });
      const conversationCount = await tx.conversation.count({
        where: { buId: PIN.buId, messages: { some: { providerResourceIdentityId: PIN.identityId, channelOrigin: 'OFICIAL', createdAt: since } } },
      });
      const webhookAggregate = await tx.webhookEvent.aggregate({
        where: { buId: PIN.buId, channel: 'OFICIAL', eventType: 'meta.webhook', receivedAt: since },
        _count: { _all: true }, _min: { receivedAt: true }, _max: { receivedAt: true },
      });

      const counts = { inbound: 0, outbound: 0, messageStatusBuckets: [] };
      for (const row of groupedMessages) {
        const count = row._count._all;
        if (row.direction === 'IN') counts.inbound += count;
        if (row.direction === 'OUT') counts.outbound += count;
        counts.messageStatusBuckets.push({ direction: row.direction, status: row.status, count });
      }
      counts.messageStatusBuckets.sort((a, b) => `${a.direction}:${a.status}`.localeCompare(`${b.direction}:${b.status}`));

      return {
        checkpoint: 'cp80-sandbox-inout-aggregate-readonly',
        status: 'snapshot',
        scope: { buId: PIN.buId, channelId: PIN.channelId, identityId: PIN.identityId, attemptId: PIN.attemptId, generation: PIN.generation, epoch: PIN.epoch },
        channel: {
          type: channel.type, status: channel.status, generation: channel.generation,
          pairingEpoch: channel.pairingEpoch, verifiedEpoch: channel.verifiedEpoch,
          ownNumberVerified: channel.ownNumberVerified,
          providerConnectionState: channel.providerConnectionState,
          currentAttemptMatchesPinned: channel.currentAttemptId === PIN.attemptId,
          receiptPresent: channel.receiptVerifiedAt !== null,
          connectedAtPresent: channel.connectedAt !== null,
          channelLeaseActive: channel.operationLeaseUntil !== null && channel.operationLeaseUntil > new Date(),
        },
        currentAttempt: { state: attempts[0].state, stage: attempts[0].stage, version: attempts[0].version, generation: attempts[0].generation, pairingEpoch: attempts[0].pairingEpoch, leaseActive: attempts[0].leaseUntil !== null && attempts[0].leaseUntil > new Date() },
        identity: {
          identityVerified: channel.ownNumberVerified === true && channel.verifiedEpoch === channel.pairingEpoch,
          currentMappingCount: identityMappingCount,
          managedLifecycle: identity.managedLifecycle,
          cleanupState: identity.cleanupState,
          cleanupLeaseActive: identity.cleanupLeaseUntil !== null && identity.cleanupLeaseUntil > new Date(),
        },
        credential: { activeForPinnedGeneration: activeCredentialCount === 1 },
        messages: { ...counts, conversationCount },
        webhookAggregate: {
          cutoffUtc: cutoff.toISOString(), count: webhookAggregate._count._all,
          minReceivedAtUtc: safeDate(webhookAggregate._min.receivedAt),
          maxReceivedAtUtc: safeDate(webhookAggregate._max.receivedAt),
          payloadSelectedOrFiltered: false,
          identityAttributionAvailable: false,
        },
        boundary: { readOnlyTransaction: true, providerOrGraphHttp: false, authOrSession: false, credentialOrEnvironmentDump: false, messageRowsOrContentSelected: false, webhookPayloadSelectedOrFiltered: false },
      };
    }, { isolationLevel: 'RepeatableRead', timeout: 10000, maxWait: 5000 });
  } catch {
    result = safeFailure('database_snapshot');
  } finally {
    await prisma.$disconnect().catch(() => {});
  }

  process.stdout.write(JSON.stringify(result) + '\n');
  return result.status === 'snapshot' ? 0 : 1;
}

main().then((code) => { process.exitCode = code; }).catch(() => {
  process.stdout.write(JSON.stringify(safeFailure('execution')) + '\n');
  process.exitCode = 1;
});
