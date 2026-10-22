# ST-CON-05 — observation owner HOW opinion

Derived preparation; not implementation authority or a delivery gate pass. 2026-10-22T00:48:19.696222+00:00

The approved feature is textual template authoring/submission/status/catalogue, with no recipient sends. Current r30 all789 passed its authored scenarios, then fresh review found three compositional consumer defects. New real-BFF tests are frozen and one canonical browser RED is separately authorized; its terminal has not occurred. Do not infer those new scenarios reproduced or passed. This opinion is read-only design support for the correction AFTER actual RED/root adjudication. No tools or edits. The source supplied below is the unchanged r30 product.

Choose the simplest faithful correction within the existing Modelos observation owner. Preserve same-account reauth/current-vs-historical identity, meaningful completed intent authority, 202 no-op, passive-read watermark, same-resource monotonic persisted fences, page/cursor membership, current/common availability failures, draft-specific association proof, truthful observedAt, dirty text and one-POST semantics. No extra provider/BFF call, second cache, generic store/platform, API/DTO/schema/backend eligibility change or ACK policy rewrite. Common backend eligible=true is an authoritative fact separate from draft association; do not recompute global eligibility from status or OR arbitrary booleans.

Material seams: (1) projectSavedObservation narrows eligible to draft definition/ACK association while getCatalog/projectRow exposes common eligible; equal-fence AND merges them. (2) atualizarStatus catch erases TEMPLATE_CONTEXT_STALE while keeping historical high numeric fence, blocking a lower-fence current success. (3) successful individual and catalogue adoptions overwrite catalogue items/pages without comparing higher fences already admitted via a passive GET; meaningful UI intent cannot replace persisted-fence ordering. Root found the sibling explicit-catalogue direction in the same source, in addition to review's individual direction. New tests cover both.

Viable HOW candidates to compare, refine or reject with concrete source reasoning:
A. Keep existing local states and pure selector, but make common-versus-draft projection ownership explicit and funnel EVERY observation adoption through the existing same-resource selector against the current cache. Preserve historical class on failure. One possible subtraction is to stop writing draft-specific individual payloads into common catalogue pages, using existing final projection to combine them; then preserve higher cached common items when a page result arrives. This is a hypothesis, not a required implementation. Explain how membership, same-fence genuine common false gates, field-level draft restrictions, and both async directions remain safe.
B. A small component-local typed observation reducer owns page/individual adoption atomically, reusing the selector/authority and no additional state store or HTTP. Explain whether this is necessary and proportionate or more change than the demonstrated defects require. No generic framework.
C. Retain eventual correction through derived GET or accept stale common eligibility. This is not viable for current known-PAUSED→old-APPROVED regression; do not select it simply to avoid code.

The new pure unit currently tests selectTemplateObservation in both orders using equal common APPROVED/eligible=true and draft eligible=false/matchesDefinition=false/eligibleForUse=false, and negative common eligible/available gates. Challenge whether that assertion imposes common projection semantics on a generic selector that also serves draft state. If necessary, recommend targeting the existing common merge/consumer instead; do not distort production design merely to satisfy a test helper call. Such a test correction must preserve the actual behavior expectations and be explicit, not a pass-the-test weakening. New browser same-fence test uses actual external supported definition change and normal BFF catalogue/draft bodies.

Return concrete recommended internal ownership/data flow, tradeoffs, exact touched functions, performance/elegance/structural positions, and failure cases that the minimal HOW must prove. Do not recommend public DTO additions or new credential modes. Existing fresh reviews and actual test design are evidence, not implementation approval. Any materially broader direction must be identified as requiring separate contract review.


## web-app/src/telas/Modelos.tsx

```text
import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { api, BusinessUnit, ErroDaApi, Eu, TemplateCatalogPage, TemplateDefinition, TemplateDraft, TemplateOperation, TemplatePreview, TemplateSummary, templateApi, ignorarSessaoMorta } from '../api';

const EMPTY: TemplateDefinition = { name: '', language: 'pt_BR', category: 'MARKETING', body: '', examples: {} };
const statusPt: Record<string, string> = {
  PENDING: 'Aguardando análise', APPROVED: 'Aprovado', REJECTED: 'Recusado', PAUSED: 'Pausado',
  DISABLED: 'Desativado', ARCHIVED: 'Arquivado', DELETED: 'Excluído', IN_APPEAL: 'Em contestação',
  PENDING_DELETION: 'Exclusão pendente', LIMIT_EXCEEDED: 'Limite excedido', UNKNOWN: 'Desconhecido',
};
const phasePt: Record<string, string> = {
  PREPARED: 'Preparada', SENDING: 'Envio em andamento', ACCEPTED: 'Cadastro registrado',
  REJECTED: 'Recusada com confirmação', AMBIGUOUS: 'Resultado inconclusivo',
};

function variables(body: string): string[] {
  return [...new Set(Array.from(body.matchAll(/\{\{([a-z][a-z_]{0,31})\}\}/g), (match) => match[1]))];
}

function definitionEqual(a: TemplateDefinition | null, b: TemplateDefinition): boolean {
  if (!a) return false;
  const canonical = (value: TemplateDefinition) => JSON.stringify({ ...value, examples: Object.fromEntries(Object.entries(value.examples).sort(([x], [y]) => x.localeCompare(y))) });
  return canonical(a) === canonical(b);
}

function operationFromDraft(draft: TemplateDraft | null): TemplateOperation | null {
  return draft?.currentOperation ?? draft?.recentOperations?.[0] ?? null;
}

function observationTime(value: string): string | null {
  const timestamp = Date.parse(value);
  return Number.isFinite(timestamp) ? new Date(timestamp).toLocaleString() : null;
}

export interface ObservationIntent {
  contextEpoch: number;
  id: number;
}

export interface ObservationSnapshot {
  contextEpoch: number;
  completedIntent: number;
}

/** Keeps HTTP request order separate from authority to replace an observation. */
export class TemplateObservationAuthority {
  private sequence = 0;
  private contextEpoch = 0;
  private completedIntent = 0;

  reset(): void {
    this.contextEpoch += 1;
    this.completedIntent = 0;
  }

  beginIntent(): ObservationIntent {
    return { contextEpoch: this.contextEpoch, id: ++this.sequence };
  }

  capturePassiveRead(): ObservationSnapshot {
    return { contextEpoch: this.contextEpoch, completedIntent: this.completedIntent };
  }

  canApplyIntent(intent: ObservationIntent): boolean {
    return intent.contextEpoch === this.contextEpoch && intent.id >= this.completedIntent;
  }

  canApplyPassiveRead(snapshot: ObservationSnapshot): boolean {
    return snapshot.contextEpoch === this.contextEpoch && snapshot.completedIntent === this.completedIntent;
  }

  completeMeaningfulIntent(intent: ObservationIntent): boolean {
    if (!this.canApplyIntent(intent)) return false;
    this.completedIntent = intent.id;
    return true;
  }
}

function fenceOrder(candidate: TemplateSummary, current: TemplateSummary): number {
  const candidateFence = /^\d+$/.test(candidate.observedFence) ? BigInt(candidate.observedFence) : null;
  const currentFence = /^\d+$/.test(current.observedFence) ? BigInt(current.observedFence) : null;
  if (candidateFence === null) return -1;
  if (currentFence === null) return 1;
  return candidateFence > currentFence ? 1 : candidateFence < currentFence ? -1 : 0;
}

function sameSemanticDefinition(left: TemplateSummary, right: TemplateSummary): boolean {
  return left.remoteTemplateId === right.remoteTemplateId
    && typeof left.semanticFingerprint === 'string' && left.semanticFingerprint.length > 0
    && left.semanticFingerprint === right.semanticFingerprint;
}

function carryMissingObservationRestrictions(winner: TemplateSummary, other: TemplateSummary): TemplateSummary {
  const merged: TemplateSummary = { ...winner };
  for (const key of ['matchesDefinition', 'eligibleForUse'] as const) {
    if (merged[key] !== undefined || other[key] === undefined) continue;
    if (other[key] === false || (other[key] === true && sameSemanticDefinition(winner, other))) merged[key] = other[key];
  }
  return merged;
}

function mergeEqualFenceRestrictions(current: TemplateSummary, candidate: TemplateSummary): TemplateSummary {
  const merged = carryMissingObservationRestrictions(current, candidate);
  const sameDefinition = sameSemanticDefinition(current, candidate);
  for (const key of ['matchesDefinition', 'eligibleForUse'] as const) {
    if (current[key] === false || candidate[key] === false) merged[key] = false;
    else if (sameDefinition && (current[key] === true || candidate[key] === true)) merged[key] = true;
    else delete merged[key];
  }
  return merged;
}

export function selectTemplateObservation(candidate: TemplateSummary, current: TemplateSummary | null): TemplateSummary | null {
  if (!current) return /^\d+$/.test(candidate.observedFence) ? candidate : null;
  if (candidate.remoteTemplateId !== current.remoteTemplateId) return /^\d+$/.test(candidate.observedFence) ? candidate : null;
  if (!/^\d+$/.test(candidate.observedFence)) return current;
  const candidateIsHistorical = candidate.safeCode === 'TEMPLATE_CONTEXT_STALE';
  const currentIsHistorical = current.safeCode === 'TEMPLATE_CONTEXT_STALE';
  if (candidateIsHistorical !== currentIsHistorical) return candidateIsHistorical ? current : candidate;
  const order = fenceOrder(candidate, current);
  let selected: TemplateSummary;
  if (order < 0) {
    selected = carryMissingObservationRestrictions(current, candidate);
  } else if (order === 0) {
    const restricted = mergeEqualFenceRestrictions(current, candidate);
    selected = { ...restricted, available: current.available && candidate.available,
      eligible: current.eligible && candidate.eligible, safeCode: current.safeCode ?? candidate.safeCode };
  } else {
    selected = carryMissingObservationRestrictions(candidate, current);
  }
  const keys = Object.keys(selected) as Array<keyof TemplateSummary>;
  return keys.length === Object.keys(current).length && keys.every((key) => selected[key] === current[key]) ? current : selected;
}

export function mergeTemplateObservations(
  pages: Record<string, TemplateCatalogPage>,
  individual: (TemplateSummary & { eligibleForUse?: boolean }) | null,
): TemplateSummary[] {
  const byId = new Map<string, TemplateSummary>();
  for (const result of Object.values(pages)) {
    for (const item of result.items) {
      const current = byId.get(item.remoteTemplateId);
      const selected = selectTemplateObservation(item, current ?? null);
      if (selected) byId.set(item.remoteTemplateId, selected);
    }
  }
  if (individual) {
    const current = byId.get(individual.remoteTemplateId);
    const selected = selectTemplateObservation(individual, current ?? null);
    if (selected) byId.set(individual.remoteTemplateId, selected);
  }
  return [...byId.values()];
}

export function templateObservationEligible(item: TemplateSummary, now: number, catalogAvailable: boolean, draftScoped = false): boolean {
  const observedAt = Date.parse(item.observedAt);
  return /^\d+$/.test(item.observedFence) && catalogAvailable && item.available && item.eligible
    && (!draftScoped || (item.matchesDefinition === true && item.eligibleForUse === true))
    && item.supported && item.status === 'APPROVED'
    && Number.isFinite(observedAt) && now >= observedAt && now - observedAt <= 300_000;
}

export function catalogHasBlockingFailure(pages: Record<string, TemplateCatalogPage>): boolean {
  return Object.values(pages).some((result) => !result.available && result.safeCode !== 'TEMPLATE_CATALOG_NOT_OBSERVED');
}

function isCorrelated(operation: TemplateOperation | null): boolean {
  if (!operation) return false;
  if (Object.prototype.hasOwnProperty.call(operation, 'acceptanceProvenance')) {
    return operation.acceptanceProvenance === 'CORRELATED_BY_DEFINITION';
  }
  return Boolean(operation.receipts?.some((receipt) => receipt.acceptanceProvenance === 'CORRELATED_BY_DEFINITION'));
}

export function operationLabel(operation: TemplateOperation): string {
  if (operation.safeCode === 'PROVIDER_ACK_CONFLICT') return 'Confirmação divergente';
  return operation.phase === 'ACCEPTED' && isCorrelated(operation)
    ? 'Correspondência localizada' : phasePt[operation.phase] ?? operation.phase;
}

export function operationNotice(operation: TemplateOperation): string {
  if (operation.safeCode === 'PROVIDER_ACK_CONFLICT') {
    return 'A Meta confirmou o envio, mas o identificador retornado diverge da correspondência localizada. A associação anterior foi preservada; confirme o status antes de usar.';
  }
  if (operation.phase === 'ACCEPTED' && isCorrelated(operation)) {
    return 'O modelo correspondente foi localizado na conta. A autoria deste cadastro não foi confirmada.';
  }
  return operation.phase === 'ACCEPTED' ? 'A Meta confirmou o cadastro; ele aguarda análise.'
    : `Operação atual: ${phasePt[operation.phase] ?? operation.phase}`;
}

export default function Modelos({ eu }: { eu: Eu }) {
  const [units, setUnits] = useState<BusinessUnit[]>([]);
  const [buId, setBuId] = useState('');
  const [channelId, setChannelId] = useState('');
  const [capability, setCapability] = useState<{ available: boolean; expectedGeneration: number; explanation: string | null } | null>(null);
  const [view, setView] = useState<'mine' | 'bu'>('mine');
  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(20);
  const [draftPage, setDraftPage] = useState<{ items: TemplateDraft[]; total: number; hasMore: boolean }>({ items: [], total: 0, hasMore: false });
  const [draft, setDraft] = useState<TemplateDraft | null>(null);
  const [savedDefinition, setSavedDefinition] = useState<TemplateDefinition | null>(null);
  const [form, setForm] = useState<TemplateDefinition>(EMPTY);
  const [preview, setPreview] = useState<TemplatePreview | null>(null);
  const [previewText, setPreviewText] = useState('');
  const [catalogPages, setCatalogPages] = useState<Record<string, TemplateCatalogPage>>({});
  const [catalogCursor, setCatalogCursor] = useState<string | null>(null);
  const [catalogFailure, setCatalogFailure] = useState(false);
  const [individualStatus, setIndividualStatus] = useState<(TemplateSummary & { eligibleForUse?: boolean }) | null>(null);
  const [recoveryReference, setRecoveryReference] = useState<{ operationId: string; phase?: string; outcome?: string; acceptance?: string; receipt?: string } | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [catalogBusy, setCatalogBusy] = useState(false);
  const [observedClock, setObservedClock] = useState(() => Date.now());
  const contextEpoch = useRef(0);
  // Fences editor ownership independently from the BU/channel context and text edits.
  // A response for draft A must never mutate a newly selected draft B in the same channel.
  const editorEpoch = useRef(0);
  const editEpoch = useRef(0);
  const pendingCreates = useRef(new Map<string, { key: string; definition: TemplateDefinition; buId: string; channelId: string; generation: number }>());
  const submitIntent = useRef<{ key: string; draftId: string; revision: number; fingerprint: string } | null>(null);
  const catalogBusyRequest = useRef(0);
  const listRequest = useRef(0);
  const openRequest = useRef(0);
  const previewRequest = useRef(0);
  const statusRequest = useRef(0);
  const observationAuthority = useRef(new TemplateObservationAuthority()).current;
  const catalogRefreshFlights = useRef(new Map<string, Promise<void>>());
  const operationRequest = useRef(0);
  const recoveryRequest = useRef(0);

  const activeBu = units.find((unit) => unit.id === buId);
  const officialChannels = activeBu?.channels.filter((channel) => channel.type === 'OFICIAL') ?? [];
  const channel = officialChannels.find((item) => item.id === channelId);
  const canManageBu = activeBu?.papel === 'OWNER' || activeBu?.papel === 'ADMIN';
  const dirty = draft ? !definitionEqual(savedDefinition, form) : Boolean(form.name || form.body || form.header || form.footer);
  const currentOperation = operationFromDraft(draft);
  const pendingCreate = buId && channelId ? pendingCreates.current.get(`${buId}:${channelId}`) : undefined;
  const variableNames = useMemo(() => variables(form.body), [form.body]);
  const hasExamples = variableNames.every((name) => typeof form.examples[name] === 'string' && form.examples[name].trim().length > 0);
  const definitionReady = form.name.trim().length > 0 && form.body.trim().length > 0 && hasExamples;
  const isLocked = draft?.state === 'LOCKED';
  const canSubmit = Boolean(draft && !dirty && !isLocked && preview?.persistence === 'PERSISTED'
    && preview.requestFingerprint && capability?.available && !recoveryReference
    && !['PREPARED', 'SENDING', 'AMBIGUOUS'].includes(currentOperation?.phase ?? ''));
  const catalogItems = useMemo(() => mergeTemplateObservations(catalogPages, individualStatus), [catalogPages, individualStatus]);

  function applyIndividualObservation(candidate: TemplateSummary) {
    setIndividualStatus((current) => selectTemplateObservation(candidate, current));
  }

  function restoreSavedObservation(candidate: TemplateSummary | null | undefined,
    lease: ObservationIntent | ObservationSnapshot, expectedRemoteTemplateId?: string | null) {
    if (!candidate || (expectedRemoteTemplateId && candidate.remoteTemplateId !== expectedRemoteTemplateId)) return;
    const admitted = 'id' in lease ? observationAuthority.canApplyIntent(lease) : observationAuthority.canApplyPassiveRead(lease);
    if (!admitted) return;
    applyIndividualObservation(candidate);
  }
  const catalogUnavailable = catalogFailure || catalogHasBlockingFailure(catalogPages);
  const isEligibleNow = (item: TemplateSummary, pageAvailable = item.available, draftScoped = false) => !catalogUnavailable && pageAvailable
    && templateObservationEligible(item, observedClock, true, draftScoped);
  const editorObservation = currentOperation?.remoteTemplateId
    ? catalogItems.find((item) => item.remoteTemplateId === currentOperation.remoteTemplateId) ?? null
    : null;

  useEffect(() => {
    const timer = window.setInterval(() => setObservedClock(Date.now()), 1_000);
    return () => window.clearInterval(timer);
  }, []);

  const loadDraftList = useCallback(async (id = buId, selectedView = view, selectedPage = page, selectedLimit = limit, epoch = contextEpoch.current) => {
    if (!id) { setDraftPage({ items: [], total: 0, hasMore: false }); return; }
    const requestId = ++listRequest.current;
    try {
      const result = await templateApi.listDrafts(id, selectedView, selectedPage, selectedLimit);
      if (requestId === listRequest.current && epoch === contextEpoch.current && id === buId
        && selectedView === view && selectedPage === page && selectedLimit === limit) setDraftPage(result);
    } catch (cause) {
      ignorarSessaoMorta(cause);
      if (requestId === listRequest.current && epoch === contextEpoch.current) setError('Não foi possível carregar os rascunhos desta Business Unit.');
    }
  }, [buId, limit, page, view]);

  const loadCatalogPage = useCallback(async (after: string | null, refresh: boolean, epoch = contextEpoch.current,
    inheritedIntent?: ObservationIntent) => {
    if (!buId || !channelId) return;
    const flightKey = refresh ? `${epoch}:${buId}:${channelId}:${after ?? ''}` : null;
    const existingFlight = flightKey ? catalogRefreshFlights.current.get(flightKey) : undefined;
    if (existingFlight) return existingFlight;
    const intent = refresh ? observationAuthority.beginIntent() : inheritedIntent;
    const passiveRead = intent ? null : observationAuthority.capturePassiveRead();
    const busyRequest = refresh ? ++catalogBusyRequest.current : null;
    if (refresh) setCatalogBusy(true);
    const canApply = () => epoch === contextEpoch.current && (intent
      ? observationAuthority.canApplyIntent(intent) : observationAuthority.canApplyPassiveRead(passiveRead!));
    const flight = (async () => {
      try {
        const result = refresh
          ? await templateApi.refreshCatalog(buId, channelId, after)
          : await templateApi.catalog(buId, channelId, after);
        if (epoch !== contextEpoch.current) return;
        if ('phase' in result) {
          if (refresh && intent && observationAuthority.canApplyIntent(intent)) {
            setNotice('Outra atualização do catálogo está em andamento. O estado observado anteriormente foi mantido.');
          }
          return;
        }
        if (refresh) {
          if (!intent || !observationAuthority.completeMeaningfulIntent(intent)) return;
        } else if (!canApply()) return;
        const key = after ?? '';
        setCatalogPages((current) => refresh && after === null
          ? { [key]: result }
          : { ...current, [key]: result });
        if (refresh && after === null && result.available) setCatalogFailure(false);
        setCatalogCursor(result.nextCursor);
        if (refresh) setNotice(result.available ? 'Catálogo atualizado.' : 'Catálogo indisponível; os dados observados permanecem identificados como indisponíveis.');
      } catch (cause) {
        ignorarSessaoMorta(cause);
        const admittedFailure = epoch === contextEpoch.current && (refresh
          ? Boolean(intent && observationAuthority.completeMeaningfulIntent(intent)) : canApply());
        if (admittedFailure) {
          setCatalogFailure(true);
          setError('Não foi possível consultar o catálogo desta conta.');
        }
      } finally {
        if (refresh && catalogBusyRequest.current === busyRequest) setCatalogBusy(false);
      }
    })();
    if (!flightKey) return flight;
    catalogRefreshFlights.current.set(flightKey, flight);
    try { await flight; }
    finally { if (catalogRefreshFlights.current.get(flightKey) === flight) catalogRefreshFlights.current.delete(flightKey); }
  }, [buId, channelId, observationAuthority]);

  useEffect(() => {
    let active = true;
    void api.get<{ businessUnits: BusinessUnit[] }>('/business-units').then((result) => {
      if (!active) return;
      const scoped = result.businessUnits.filter((unit) => unit.channels.some((item) => item.type === 'OFICIAL'));
      setUnits(result.businessUnits);
      const first = scoped[0];
      if (first) {
        setBuId(first.id);
        setChannelId(first.channels.find((item) => item.type === 'OFICIAL')?.id ?? '');
      }
    }).catch((cause: unknown) => { ignorarSessaoMorta(cause); if (active) setError('Não foi possível carregar suas Business Units.'); });
    return () => { active = false; };
  }, []);

  useEffect(() => {
    if (!buId || !channelId) { setCapability(null); return; }
    const epoch = contextEpoch.current;
    setCapability(null);
    void templateApi.capabilities(buId, channelId).then((result) => {
      if (epoch === contextEpoch.current) setCapability(result);
    }).catch((cause: unknown) => {
      ignorarSessaoMorta(cause);
      if (epoch === contextEpoch.current) setCapability({ available: false, expectedGeneration: channel?.generation ?? 0, explanation: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    });
    void loadDraftList(buId, view, page, limit, epoch);
    setCatalogPages({}); setCatalogCursor(null); setIndividualStatus(null); setCatalogFailure(false);
    void loadCatalogPage(null, false, epoch);
  }, [buId, channelId]);

  useEffect(() => { void loadDraftList(); }, [buId, view, page, limit, loadDraftList]);

  useEffect(() => {
    if (!buId || !channelId || !capability?.available || !definitionReady) return;
    const epoch = contextEpoch.current;
    const editing = editEpoch.current;
    const requestId = ++previewRequest.current;
    const selectedDraftId = draft?.id;
    const selectedRevision = draft?.revision;
    const editor = editorEpoch.current;
    const definition = structuredClone(form);
    setPreview(null); setPreviewText('');
    const timer = window.setTimeout(() => {
      void templateApi.preview(buId, {
        channelId, expectedGeneration: capability.expectedGeneration,
        ...(selectedDraftId ? { draftId: selectedDraftId, expectedRevision: selectedRevision } : {}),
        definition,
      }).then((result) => {
        if (requestId !== previewRequest.current || epoch !== contextEpoch.current || editor !== editorEpoch.current || editing !== editEpoch.current) return;
        setPreview(result); setPreviewText(result.renderedText); setError(null);
      }).catch((cause: unknown) => {
        if (requestId !== previewRequest.current || epoch !== contextEpoch.current || editing !== editEpoch.current) return;
        if (cause instanceof ErroDaApi && cause.status < 500) setError('Revise nome, texto e exemplos antes de pré-visualizar.');
        else setError('Não foi possível gerar a prévia neste momento.');
      });
    }, 300);
    return () => window.clearTimeout(timer);
  }, [buId, channelId, capability?.available, capability?.expectedGeneration, draft?.id, draft?.revision, definitionReady, form]);

  function trocarBu(nextBuId: string) {
    if (dirty && !window.confirm('Descartar as alterações que ainda não foram salvas ao trocar de Business Unit?')) return;
    contextEpoch.current += 1; editorEpoch.current += 1; editEpoch.current += 1;
    listRequest.current += 1; openRequest.current += 1; previewRequest.current += 1; statusRequest.current += 1; operationRequest.current += 1; recoveryRequest.current += 1;
    observationAuthority.reset();
    submitIntent.current = null;
    setRecoveryReference(null);
    setBusy(false);
    catalogBusyRequest.current += 1; setCatalogBusy(false);
    setBuId(nextBuId);
    const next = units.find((unit) => unit.id === nextBuId);
    setChannelId(next?.channels.find((item) => item.type === 'OFICIAL')?.id ?? '');
    setDraft(null); setSavedDefinition(null); setForm(EMPTY); setPreview(null); setPreviewText(''); setNotice(null); setError(null);
    setView('mine');
    setPage(1); setCatalogPages({}); setCatalogCursor(null); setCatalogFailure(false);
  }

  function trocarCanal(nextChannelId: string) {
    if (dirty && !window.confirm('Descartar as alterações que ainda não foram salvas ao trocar de canal?')) return;
    contextEpoch.current += 1; editorEpoch.current += 1; editEpoch.current += 1;
    openRequest.current += 1; previewRequest.current += 1; statusRequest.current += 1; operationRequest.current += 1; recoveryRequest.current += 1;
    observationAuthority.reset();
    submitIntent.current = null;
    setRecoveryReference(null);
    setBusy(false);
    catalogBusyRequest.current += 1; setCatalogBusy(false);
    setChannelId(nextChannelId); setDraft(null); setSavedDefinition(null); setForm(EMPTY); setPreview(null); setPreviewText('');
    setCatalogPages({}); setCatalogCursor(null); setIndividualStatus(null); setCatalogFailure(false); setNotice(null); setError(null);
  }

  function editar<K extends keyof TemplateDefinition>(key: K, value: TemplateDefinition[K]) {
    editEpoch.current += 1; setPreview(null); setPreviewText(''); setNotice(null); setError(null);
    setForm((current) => ({ ...current, [key]: value }));
  }

  async function abrirRascunho(id: string) {
    if (dirty && !window.confirm('Descartar as alterações que ainda não foram salvas?')) return;
    const epoch = contextEpoch.current;
    const editor = ++editorEpoch.current;
    const requestId = ++openRequest.current;
    const observationRead = observationAuthority.capturePassiveRead();
    submitIntent.current = null;
    recoveryRequest.current += 1; operationRequest.current += 1; statusRequest.current += 1;
    previewRequest.current += 1;
    setRecoveryReference(null); setIndividualStatus(null); setPreview(null); setPreviewText('');
    setBusy(true);
    editEpoch.current += 1; previewRequest.current += 1;
    try {
      const opened = await templateApi.getDraft(id);
      if (requestId !== openRequest.current || epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
      if (opened.buId !== buId) return;
      if (opened.channelId !== channelId) {
        contextEpoch.current += 1;
        observationAuthority.reset();
        setCatalogPages({}); setCatalogCursor(null); setIndividualStatus(null); setCatalogFailure(false);
      }
      const openedObservationRead = opened.channelId === channelId ? observationRead : observationAuthority.capturePassiveRead();
      restoreSavedObservation(opened.savedObservation ?? opened.currentOperation?.savedObservation, openedObservationRead,
        opened.currentOperation?.remoteTemplateId ?? null);
      setDraft(opened); setSavedDefinition(opened.definition); setForm(opened.definition);
      setChannelId(opened.channelId); setPreview(null); setPreviewText(''); setNotice('Rascunho aberto.'); setError(null);
      editEpoch.current += 1;
    } catch (cause) { ignorarSessaoMorta(cause); if (requestId === openRequest.current && epoch === contextEpoch.current && editor === editorEpoch.current) setError('Não foi possível abrir este rascunho.'); }
    finally { if (requestId === openRequest.current && epoch === contextEpoch.current && editor === editorEpoch.current) setBusy(false); }
  }

  function createVariationFromDefinition(definition: TemplateDefinition) {
    if (dirty && !window.confirm('Descartar as alterações que ainda não foram salvas e copiar este modelo?')) return;
    const stem = definition.name.slice(0, 124).replace(/_+$/g, '');
    const variation = { ...definition, name: `${stem}_v2` };
    contextEpoch.current += 1; editorEpoch.current += 1; editEpoch.current += 1;
    observationAuthority.reset();
    openRequest.current += 1; previewRequest.current += 1;
    submitIntent.current = null;
    setRecoveryReference(null); setIndividualStatus(null);
    setDraft(null); setSavedDefinition(null); setForm(variation); setPreview(null); setPreviewText('');
    setBusy(false);
    setNotice('Variação em novo rascunho. O modelo já enviado não será alterado.'); setError(null);
  }

  function createVariation() {
    if (draft) createVariationFromDefinition(draft.definition);
  }

  function novoRascunho() {
    if (dirty && !window.confirm('Descartar as alterações que ainda não foram salvas?')) return;
    editorEpoch.current += 1; editEpoch.current += 1; openRequest.current += 1; previewRequest.current += 1;
    submitIntent.current = null; setRecoveryReference(null); setIndividualStatus(null);
    setDraft(null); setSavedDefinition(null); setForm(EMPTY); setPreview(null); setPreviewText('');
    setBusy(false);
    setNotice(null); setError(null);
  }

  async function salvar() {
    if (!buId || !channelId || !capability?.available || !definitionReady || isLocked) return;
    const epoch = contextEpoch.current;
    const editor = editorEpoch.current;
    const editing = editEpoch.current;
    const definition = structuredClone(form);
    setBusy(true); setError(null); setNotice(null);
    try {
      if (draft) {
        const updated = await templateApi.saveDraft(draft.id, draft.revision, definition);
        if (epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
        setDraft(updated); setSavedDefinition(updated.definition);
        if (editing === editEpoch.current) setForm(updated.definition);
        setNotice(`Rascunho salvo na revisão ${updated.revision}.`);
        await loadDraftList(buId, view, page, limit, epoch);
      } else {
        const contextKey = `${buId}:${channelId}`;
        const pending = pendingCreates.current.get(contextKey);
        if (pending && (pending.buId !== buId || pending.channelId !== channelId || pending.generation !== capability.expectedGeneration
          || JSON.stringify(pending.definition) !== JSON.stringify(definition))) {
          setError('Há uma criação ainda não confirmada. Retome exatamente o conteúdo anterior antes de editar ou criar outro rascunho.');
          return;
        }
        const request = pending ?? { key: crypto.randomUUID(), definition, buId, channelId, generation: capability.expectedGeneration };
        pendingCreates.current.set(contextKey, request);
        const created = await templateApi.createDraft(buId, {
          clientRequestId: request.key, channelId, expectedGeneration: capability.expectedGeneration, ...request.definition,
        });
        pendingCreates.current.delete(contextKey);
        if (epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
        setDraft(created); setSavedDefinition(created.definition);
        if (editing === editEpoch.current) setForm(created.definition);
        setNotice(`Rascunho salvo na revisão ${created.revision}.`);
        await loadDraftList(buId, view, page, limit, epoch);
      }
    } catch (cause) {
      ignorarSessaoMorta(cause);
      if (epoch === contextEpoch.current && editor === editorEpoch.current && editing === editEpoch.current) setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível confirmar o salvamento. O texto continua nesta tela.');
    } finally { if (epoch === contextEpoch.current && editor === editorEpoch.current) setBusy(false); }
  }

  async function retomarCriacaoPendente() {
    if (!pendingCreate || pendingCreate.buId !== buId || pendingCreate.channelId !== channelId) return;
    const epoch = contextEpoch.current; const editor = editorEpoch.current;
    setBusy(true); setError(null); setNotice(null);
    try {
      const created = await templateApi.createDraft(pendingCreate.buId, {
        clientRequestId: pendingCreate.key, channelId: pendingCreate.channelId,
        expectedGeneration: pendingCreate.generation, ...pendingCreate.definition,
      });
      if (epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
      pendingCreates.current.delete(`${pendingCreate.buId}:${pendingCreate.channelId}`);
      setDraft(created); setSavedDefinition(created.definition);
      setNotice(`Rascunho salvo na revisão ${created.revision}. O texto editado continua nesta tela.`);
      await loadDraftList(buId, view, page, limit, epoch);
    } catch (cause) {
      ignorarSessaoMorta(cause);
      if (epoch === contextEpoch.current && editor === editorEpoch.current) {
        setError(cause instanceof ErroDaApi ? cause.message : 'Não foi possível confirmar a criação. O mesmo pedido continua disponível para retomada.');
      }
    } finally { if (epoch === contextEpoch.current && editor === editorEpoch.current) setBusy(false); }
  }

  async function carregarPrevia() {
    if (!buId || !channelId || !capability?.available || !definitionReady) return;
    const epoch = contextEpoch.current; const editor = editorEpoch.current; const editing = editEpoch.current; const requestId = ++previewRequest.current;
    try {
      const result = await templateApi.preview(buId, { channelId, expectedGeneration: capability.expectedGeneration,
        ...(draft ? { draftId: draft.id, expectedRevision: draft.revision } : {}), definition: structuredClone(form) });
      if (requestId !== previewRequest.current || epoch !== contextEpoch.current || editor !== editorEpoch.current || editing !== editEpoch.current) return;
      setPreview(result); setPreviewText(result.renderedText); setError(null);
    } catch (cause) { ignorarSessaoMorta(cause); if (requestId === previewRequest.current && epoch === contextEpoch.current && editor === editorEpoch.current && editing === editEpoch.current) setError('Não foi possível gerar a prévia. Revise o conteúdo e tente novamente.'); }
  }

  async function enviar() {
    if (!draft || !canSubmit || !preview?.requestFingerprint || !capability) return;
    const intent = submitIntent.current;
    const key = intent && intent.draftId === draft.id && intent.revision === draft.revision && intent.fingerprint === preview.requestFingerprint
      ? intent.key : crypto.randomUUID();
    submitIntent.current = { key, draftId: draft.id, revision: draft.revision, fingerprint: preview.requestFingerprint };
    const epoch = contextEpoch.current;
    const editor = editorEpoch.current;
    const editing = editEpoch.current;
    const targetDraftId = draft.id;
    const submitObservationRead = observationAuthority.capturePassiveRead();
    setBusy(true); setError(null); setNotice(null);
    try {
      const operation = await templateApi.submit(draft.id, key, { expectedRevision: draft.revision,
        expectedGeneration: capability.expectedGeneration, expectedDefinitionFingerprint: preview.requestFingerprint });
      if (epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
      setRecoveryReference(null);
      setDraft((current) => current ? { ...current, state: ['ACCEPTED', 'SENDING', 'PREPARED', 'AMBIGUOUS'].includes(operation.phase) ? 'LOCKED' : current.state,
        currentOperation: operation, recentOperations: [operation, ...(current.recentOperations ?? []).filter((item) => item.id !== operation.id)].slice(0, 11) } : current);
      restoreSavedObservation(operation.savedObservation, submitObservationRead, operation.remoteTemplateId);
      setNotice(operationNotice(operation));
      await loadDraftList(buId, view, page, limit, epoch);
    } catch (cause) {
      ignorarSessaoMorta(cause);
      if (cause instanceof ErroDaApi && cause.operationId) {
        if (epoch === contextEpoch.current && editor === editorEpoch.current) setRecoveryReference({ operationId: cause.operationId, phase: cause.phase, outcome: cause.outcome,
          acceptance: cause.providerAcceptance, receipt: cause.receiptPersistence });
        try {
          if (epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
          await templateApi.operation(targetDraftId, cause.operationId);
          if (epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
          const draftRead = observationAuthority.capturePassiveRead();
          const authoritative = await templateApi.getDraft(targetDraftId);
          if (epoch === contextEpoch.current && editor === editorEpoch.current) {
            setDraft((current) => current ? { ...authoritative,
              definition: editEpoch.current === editing ? authoritative.definition : current.definition } : current);
            const latestOperation = operationFromDraft(authoritative);
            if (authoritative.revision === draft.revision && latestOperation?.id === cause.operationId) {
              restoreSavedObservation(authoritative.savedObservation ?? latestOperation.savedObservation, draftRead,
                latestOperation.remoteTemplateId);
              setRecoveryReference(null);
            }
            if (editEpoch.current === editing) {
              setSavedDefinition(authoritative.definition);
              setForm(authoritative.definition);
              if (latestOperation?.id === cause.operationId && latestOperation.phase === 'REJECTED') {
                setPreview(null); setPreviewText(''); setRecoveryReference(null);
              }
            }
          }
        } catch { /* keep the server's safe operation metadata below */ }
      }
      if (epoch === contextEpoch.current && editor === editorEpoch.current) setError(cause instanceof ErroDaApi ? `${cause.message}${cause.operationId ? ' A operação foi preservada e não será reenviada automaticamente.' : ''}` : 'Não foi possível confirmar o cadastro. Consulte a operação antes de tentar novamente.');
    } finally { if (epoch === contextEpoch.current && editor === editorEpoch.current) setBusy(false); }
  }

  async function recuperar() {
    const operation = operationFromDraft(draft);
    if (!draft || (!operation && !recoveryReference)) return;
    const epoch = contextEpoch.current;
    const editor = editorEpoch.current;
    const editing = editEpoch.current;
    const targetDraftId = draft.id;
    const sequence = ++recoveryRequest.current;
    setBusy(true); setError(null);
    try {
      const operationId = operation?.id ?? recoveryReference!.operationId;
      if (operation?.recoveryAction === 'RECONCILE') await templateApi.reconcile(draft.id, operationId);
      else await templateApi.operation(draft.id, operationId);
      if (epoch !== contextEpoch.current || editor !== editorEpoch.current || sequence !== recoveryRequest.current) return;
      const draftRead = observationAuthority.capturePassiveRead();
      const authoritative = await templateApi.getDraft(targetDraftId);
      if (epoch !== contextEpoch.current || editor !== editorEpoch.current || sequence !== recoveryRequest.current) return;
      setDraft((current) => current ? { ...authoritative,
        definition: editEpoch.current === editing ? authoritative.definition : current.definition } : current);
      if (editEpoch.current === editing) {
        setSavedDefinition(authoritative.definition);
        setForm(authoritative.definition);
      }
      const latestOperation = operationFromDraft(authoritative);
      if (authoritative.revision === draft.revision && latestOperation?.id === operationId) {
        restoreSavedObservation(authoritative.savedObservation ?? latestOperation.savedObservation, draftRead,
          latestOperation.remoteTemplateId);
        setRecoveryReference(null);
        if (editEpoch.current === editing && latestOperation.phase === 'REJECTED') { setPreview(null); setPreviewText(''); }
        setNotice(operationNotice(latestOperation));
      }
    } catch (cause) { ignorarSessaoMorta(cause); if (epoch === contextEpoch.current && editor === editorEpoch.current && sequence === recoveryRequest.current) setError('Não foi possível atualizar esta operação. O identificador continua disponível para consulta.'); }
    finally { if (epoch === contextEpoch.current && editor === editorEpoch.current && sequence === recoveryRequest.current) setBusy(false); }
  }

  async function consultarOperacao(operationId: string) {
    if (!draft) return;
    const epoch = contextEpoch.current; const editor = editorEpoch.current; const targetDraftId = draft.id; const sequence = ++operationRequest.current;
    const observationRead = observationAuthority.capturePassiveRead();
    try {
      const result = await templateApi.operation(targetDraftId, operationId);
      if (epoch !== contextEpoch.current || editor !== editorEpoch.current || sequence !== operationRequest.current) return;
      setDraft((current) => current ? { ...current,
        currentOperation: result.revision === current.revision ? result : current.currentOperation,
        recentOperations: [result, ...(current.recentOperations ?? []).filter((item) => item.id !== result.id)].slice(0, 11) } : current);
      const selectedOperation = operationFromDraft(draft);
      if (result.revision === draft.revision && result.id === selectedOperation?.id && result.remoteTemplateId
        && selectedOperation.remoteTemplateId === result.remoteTemplateId) {
        restoreSavedObservation(result.savedObservation, observationRead, result.remoteTemplateId);
      }
      setNotice(`Operação consultada: ${operationLabel(result)}.`);
    } catch (cause) { ignorarSessaoMorta(cause); if (epoch === contextEpoch.current && editor === editorEpoch.current && sequence === operationRequest.current) setError('Esta operação não está disponível para consulta.'); }
  }

  async function atualizarStatus() {
    if (!draft || !currentOperation?.remoteTemplateId) return;
    const targetRemoteTemplateId = currentOperation.remoteTemplateId;
    const epoch = contextEpoch.current; const editor = editorEpoch.current; const targetDraftId = draft.id; const sequence = ++statusRequest.current;
    const intent = observationAuthority.beginIntent();
    setBusy(true); setError(null);
    try {
      const status = await templateApi.refreshDraft(draft.id);
      if (epoch !== contextEpoch.current || editor !== editorEpoch.current) return;
      if ('phase' in status) {
        if (observationAuthority.canApplyIntent(intent)) setNotice('A atualização do status já está em andamento. O estado anterior foi mantido.');
        return;
      }
      if (!observationAuthority.completeMeaningfulIntent(intent)) return;
      setIndividualStatus((current) => selectTemplateObservation(status, current));
      setCatalogPages((current) => Object.fromEntries(Object.entries(current).map(([key, result]) => [key, {
        ...result,
        items: result.items.map((item) => item.remoteTemplateId === status.remoteTemplateId ? status : item),
      }])));
      setNotice(`Status consultado: ${statusPt[status.status] ?? 'Desconhecido'}.`);
      await loadCatalogPage(null, false, epoch, intent);
    } catch (cause) {
      ignorarSessaoMorta(cause);
      if (epoch === contextEpoch.current && editor === editorEpoch.current
        && observationAuthority.completeMeaningfulIntent(intent)) {
        const unavailable = (item: TemplateSummary) => ({ ...item, available: false, eligible: false,
          eligibleForUse: false, safeCode: 'TEMPLATE_REFRESH_UNAVAILABLE' });
        setIndividualStatus((current) => current?.remoteTemplateId === targetRemoteTemplateId
          ? selectTemplateObservation(unavailable(current), current) : current);
        setCatalogPages((current) => Object.fromEntries(Object.entries(current).map(([key, result]) => [key, {
          ...result, items: result.items.map((item) => item.remoteTemplateId === targetRemoteTemplateId ? unavailable(item) : item),
        }])));
        setError('Não foi possível atualizar o status remoto. O estado anterior continua identificado como indisponível.');
      }
    }
    finally { if (epoch === contextEpoch.current && editor === editorEpoch.current && sequence === statusRequest.current) setBusy(false); }
  }

  async function refreshCatalog(after: string | null = null) {
    await loadCatalogPage(after, true);
  }

  const latestReceipt = currentOperation?.receipts?.[0]
    ?? draft?.recentOperations?.find((operation) => operation.id === currentOperation?.id)?.receipts?.[0];

  return <div className="grade">
    <h1 style={{ margin: 0 }}>Modelos de mensagem</h1>
    <p className="suave">Crie e envie um modelo para análise da Meta. Um cadastro aceito ainda pode estar aguardando aprovação.</p>
    {error && <p className="erro" role="alert">{error}</p>}
    {notice && <p className="suave" role="status">{notice}</p>}

    <section className="cartao grade" aria-label="Contexto do canal">
      <label>Business Unit
        <select value={buId} onChange={(event) => trocarBu(event.target.value)}>
          {units.filter((unit) => unit.channels.some((item) => item.type === 'OFICIAL')).map((unit) => <option key={unit.id} value={unit.id}>{unit.name}</option>)}
        </select>
      </label>
      <label>Canal oficial
        <select value={channelId} onChange={(event) => trocarCanal(event.target.value)}>
          {officialChannels.map((item) => <option key={item.id} value={item.id}>{activeBu?.name} · {item.status}</option>)}
        </select>
      </label>
      {capability?.available ? <p role="status">Gerenciamento de modelos disponível · geração {capability.expectedGeneration}</p>
        : capability ? <p role="status">Gerenciamento indisponível neste canal. A prévia não usará a Meta.</p>
          : <p role="status">Carregando capacidade do canal…</p>}
    </section>

    <section className="cartao grade" aria-label="Rascunhos de modelo">
      <div className="linha">
        <h2>Rascunhos</h2>
        {canManageBu && <label>Exibição
          <select value={view} onChange={(event) => { setView(event.target.value as 'mine' | 'bu'); setPage(1); }}>
            <option value="mine">Meus rascunhos</option><option value="bu">Rascunhos da BU</option>
          </select>
        </label>}
        <label>Por página
          <select value={limit} onChange={(event) => { setLimit(Number(event.target.value)); setPage(1); }}>
            <option value={20}>20</option><option value={50}>50</option>
          </select>
        </label>
        <button type="button" onClick={novoRascunho}>Novo rascunho</button>
      </div>
      {pendingCreate && JSON.stringify(pendingCreate.definition) !== JSON.stringify(form) && !draft && <p>
        <span>Uma criação anterior pode ter sido confirmada no servidor.</span>{' '}
        <button type="button" onClick={() => void retomarCriacaoPendente()} disabled={busy}>
          Retomar criação anterior sem perder este texto
        </button>
      </p>}
      <p className="suave">{draftPage.total} rascunhos · página {page} · {view === 'mine' ? 'seus rascunhos' : 'compartilhados na BU'}</p>
      <div className="grade">
        {draftPage.items.map((item) => <div className="linha" key={item.id}>
          <button type="button" onClick={() => void abrirRascunho(item.id)}>Abrir {item.definition.name}</button>
          <button type="button" onClick={() => createVariationFromDefinition(item.definition)}>Copiar como novo rascunho</button>
          <span>{item.state === 'LOCKED' ? 'Revisão congelada' : 'Rascunho editável'} · revisão {item.revision}</span>
          {item.currentOperation && <span>Operação: {operationLabel(item.currentOperation)}</span>}
        </div>)}
        {!draftPage.items.length && <p className="suave">Ainda não há rascunhos nesta lista.</p>}
      </div>
      <div className="linha">
        <button type="button" disabled={page <= 1} onClick={() => setPage((current) => Math.max(1, current - 1))}>Página anterior</button>
        <button type="button" disabled={!draftPage.hasMore} onClick={() => setPage((current) => current + 1)}>Próxima página</button>
      </div>
    </section>

    <section className="cartao grade" aria-label="Editor de modelo">
      <h2>{draft ? `Editar ${draft.definition.name} · revisão ${draft.revision}` : 'Novo rascunho de modelo'}</h2>
      <label>Nome do modelo
        <input value={form.name} maxLength={128} onChange={(event) => editar('name', event.target.value)} disabled={isLocked} />
      </label>
      <label>Idioma
        <select value={form.language} onChange={(event) => editar('language', event.target.value as 'pt_BR')} disabled={isLocked}>
          <option value="pt_BR">Português (Brasil)</option>
        </select>
      </label>
      <label>Categoria
        <select value={form.category} onChange={(event) => editar('category', event.target.value as TemplateDefinition['category'])} disabled={isLocked}>
          <option value="MARKETING">Marketing · abertura comercial</option>
          <option value="UTILITY">Utilidade · atualização transacional</option>
        </select>
      </label>
      <label>Cabeçalho estático (opcional)
        <input value={form.header ?? ''} maxLength={60} onChange={(event) => editar('header', event.target.value || undefined)} disabled={isLocked} />
      </label>
      <label>Texto do corpo
        <textarea value={form.body} maxLength={1024} rows={5} onChange={(event) => {
          const nextBody = event.target.value;
          const nextNames = variables(nextBody);
          const examples = Object.fromEntries(nextNames.map((name) => [name, form.examples[name] ?? '']));
          editEpoch.current += 1; setPreview(null); setPreviewText(''); setNotice(null); setError(null);
          setForm((current) => ({ ...current, body: nextBody, examples }));
        }} disabled={isLocked} />
      </label>
      <div className="grade" aria-label="Exemplos das variáveis">
        {variableNames.map((name) => <label key={name}>Exemplo para {name}
          <input value={form.examples[name] ?? ''} maxLength={128} onChange={(event) => editar('examples', { ...form.examples, [name]: event.target.value })} disabled={isLocked} />
        </label>)}
      </div>
      <label>Rodapé estático (opcional)
        <input value={form.footer ?? ''} maxLength={60} onChange={(event) => editar('footer', event.target.value || undefined)} disabled={isLocked} />
      </label>
      {dirty && <p role="status">Há alterações não salvas</p>}
      {preview && <div className="grade" aria-label="Prévia do modelo">
        <strong>Prévia renderizada</strong>
        <p style={{ whiteSpace: 'pre-wrap' }}>{previewText}</p>
        <p role="status">{preview.persistence === 'PERSISTED' ? 'Prévia vinculada à revisão salva' : 'Prévia de conteúdo não salvo'}</p>
      </div>}
      <div className="linha">
        <button type="button" onClick={() => void carregarPrevia()} disabled={!definitionReady || !capability?.available}>Pré-visualizar</button>
        <button type="button" onClick={() => void salvar()} disabled={!definitionReady || !capability?.available || busy || isLocked || !dirty}>
          {draft ? 'Salvar alterações' : 'Salvar rascunho'}
        </button>
        {draft?.state === 'DRAFT' && <button type="button" onClick={() => void enviar()} disabled={!canSubmit || busy}>Enviar à Meta para aprovação</button>}
        {isLocked && <button type="button" onClick={createVariation}>Criar variação</button>}
      </div>
      {currentOperation && <section className="grade" aria-label="Operação de submissão">
        <h3>Operação: {operationLabel(currentOperation)}</h3>
        <p>{operationNotice(currentOperation)}</p>
        {latestReceipt && <p>Última atualização registrada: {new Date(latestReceipt.createdAt).toLocaleString()}</p>}
        {currentOperation.remoteTemplateId && <button type="button" onClick={() => void atualizarStatus()} disabled={busy}>Atualizar status do modelo</button>}
        {['PREPARED', 'SENDING', 'AMBIGUOUS'].includes(currentOperation.phase) && <button type="button" onClick={() => void recuperar()} disabled={busy}>Recuperar estado da operação</button>}
        {(draft?.recentOperations ?? []).filter((item) => item.id !== currentOperation.id).slice(0, 10).map((item) => <p key={item.id}>
          Revisão {item.revision} · {phasePt[item.phase] ?? item.phase} · <button type="button" onClick={() => void consultarOperacao(item.id)}>Consultar operação</button>
        </p>)}
      </section>}
      {recoveryReference && !currentOperation && <section className="grade" aria-label="Operação preservada">
        <p>Há uma operação registrada que não pôde ser carregada agora.</p>
        <p>Identificador: {recoveryReference.operationId}</p>
        <button type="button" onClick={() => void recuperar()} disabled={busy}>Consultar operação registrada</button>
      </section>}
      {editorObservation && <p role="status">Status do modelo: {statusPt[editorObservation.status] ?? 'Desconhecido'} · {isEligibleNow(editorObservation, editorObservation.available, true) ? 'elegível para uso futuro' : 'Não elegível para uso'}{observationTime(editorObservation.observedAt) && <> · Observado em <time aria-label={`Observado em ${observationTime(editorObservation.observedAt)}`} dateTime={editorObservation.observedAt}>{observationTime(editorObservation.observedAt)}</time></>}</p>}
    </section>

    <section className="cartao grade" aria-label="Modelos da conta">
      <div className="linha"><h2>Modelos da conta</h2><button type="button" onClick={() => void refreshCatalog(null)} disabled={!capability?.available} aria-busy={catalogBusy}>Atualizar modelos da conta</button></div>
      {catalogUnavailable && <p role="status">Catálogo indisponível ou desatualizado; nenhum item foi marcado como elegível.</p>}
      {Object.entries(catalogPages).length === 0 && <p className="suave">O catálogo ainda não foi consultado.</p>}
      <div className="grade">
        {catalogItems.map((item, index) => <article className="linha" key={`${item.remoteTemplateId}:${index}`}>
          <strong>{item.name ?? 'Modelo sem nome observado'}</strong>
          <span>{item.language ?? 'Idioma desconhecido'} · {item.category}</span>
          <span>{statusPt[item.status] ?? 'Desconhecido'}</span>
          <span>{isEligibleNow(item, catalogPages[Object.keys(catalogPages).find((key) => catalogPages[key].items.includes(item)) ?? '']?.available) ? 'Elegível para uso futuro' : 'Não elegível para uso'}</span>
          {observationTime(item.observedAt) && <span>Observado em <time aria-label={`Observado em ${observationTime(item.observedAt)}`} dateTime={item.observedAt}>{observationTime(item.observedAt)}</time></span>}
          {!item.supported && <span>Formato sem suporte para prévia segura</span>}
        </article>)}
      </div>
      {catalogCursor && <button type="button" onClick={() => void refreshCatalog(catalogCursor)} disabled={catalogBusy}>Carregar próxima página</button>}
      {catalogItems.length === 0 && Object.values(catalogPages).some((item) => item.available) && <p className="suave">Nenhum modelo encontrado nesta página.</p>}
    </section>
  </div>;
}
```


## web-app/src/api.ts

```text
/**
 * Cliente do BFF.
 *
 * O front é serviço próprio, num SUBDOMÍNIO do mesmo domínio da API (ADR-0015).
 * Isso é origem diferente e **mesmo site** — então:
 *  - `credentials: 'include'` manda o cookie `HttpOnly` para a API;
 *  - o cookie continua `SameSite=Lax`, porque subdomínio é o mesmo site;
 *  - `X-Requested-With` é exigido pelo servidor no que muda estado (CSRF).
 *
 * A base da API vem de `/config.js`, escrito pelo container no START — não do
 * build (ver `config.ts`). Vazio = mesma origem.
 */
import { API_BASE as BASE } from './config';
/** Evento disparado quando qualquer chamada volta 401. */
export const SESSAO_MORTA = 'leadshug:sessao-morta';

/**
 * A conta ainda não terminou o wizard (409 ONBOARDING_PENDENTE), ou um módulo
 * foi desligado com a aba aberta (404 MODULO_DESLIGADO).
 *
 * Nos dois casos o estado da tela está VELHO, não errado: o app rebusca o /me e
 * se remonta, em vez de mostrar erro. É o mesmo padrão do SESSAO_MORTA.
 */
export const PRODUTO_MUDOU = 'leadshug:produto-mudou';

/**
 * `typeof window` porque este módulo também é exercitado fora do navegador —
 * é o teste de unidade que prova isso. Estourar aqui trocaria o erro REAL da
 * chamada por um "window is not defined", que aponta para o lugar errado.
 */
function avisar(evento: string): void {
  if (typeof window !== 'undefined') window.dispatchEvent(new CustomEvent(evento));
}

export class ErroDaApi extends Error {
  constructor(
    readonly status: number,
    readonly codigo: string | undefined,
    mensagem: string,
    readonly outcome?: string,
    readonly evidence?: string,
    readonly localMessageState?: string,
    readonly diagnosticPersistence?: string,
    readonly operationId?: string,
    readonly phase?: string,
    readonly providerAcceptance?: string,
    readonly receiptPersistence?: string,
    readonly acceptanceProvenance?: string,
    readonly recoveryAction?: string,
  ) {
    super(mensagem);
  }
}

async function chamar<T>(caminho: string, init: RequestInit = {}): Promise<T> {
  const mudaEstado = Boolean(init.method && init.method !== 'GET');
  const res = await fetch(`${BASE}/api/bff${caminho}`, {
    ...init,
    credentials: 'include',
    headers: {
      'content-type': 'application/json',
      ...(mudaEstado ? { 'x-requested-with': 'leadshug-web' } : {}),
      ...(init.headers ?? {}),
    },
  });

  if (res.status === 204) return undefined as T;

  // Resposta que NÃO é JSON é falha de configuração, não corpo vazio.
  //
  // O caso real: sem `LEADSHUG_API_URL`, a base fica vazia e o front chama a
  // PRÓPRIA origem — onde o nginx serve o index.html para qualquer caminho. A
  // resposta vem 200, com HTML. Engolir isso como `{}` fazia a tela quebrar três
  // passos depois, num campo que não tem relação nenhuma com a causa
  // ("Cannot read properties of undefined"), e mandava quem depura para o lugar
  // errado. Falhar aqui, dizendo o que provavelmente está errado, é o mínimo.
  const bruto = await res.text();
  let corpo: Record<string, unknown>;
  try {
    corpo = bruto ? JSON.parse(bruto) : {};
  } catch {
    // 405 num POST é assinatura de SERVIDOR DE ARQUIVOS: nginx responde assim
    // quando recebe POST para um arquivo estático. Dizer isso poupa a rodada de
    // "confira se é mesmo a API" — o que responde não é uma API.
    const pareceEstatico = res.status === 405 || /^\s*<(!doctype|html)/i.test(bruto);

    throw new ErroDaApi(
      res.status,
      'RESPOSTA_NAO_E_JSON',
      !BASE
        ? 'A base da API está VAZIA: o front está chamando a própria origem. ' +
          'Configure LEADSHUG_API_URL no serviço web.'
        : pareceEstatico
          ? `${BASE} respondeu ${res.status} como um servidor de ARQUIVOS, não como a API ` +
            `(em ${caminho}). Esse endereço aponta para o serviço errado — confira ` +
            'LEADSHUG_API_URL e o domínio do serviço `api`.'
          : `A API respondeu ${res.status} com algo que não é JSON em ${caminho}. ` +
            `Confira se ${BASE} é mesmo a API.`,
    );
  }

  if (res.status === 401) {
    // A sessão morreu (expirou, a conta foi inativada, a senha foi resetada).
    // Quem descobre isso é qualquer chamada, então o aviso é central: a tela
    // que estava aberta não tem como saber o que fazer sozinha.
    avisar(SESSAO_MORTA);
  }
  // Estado VELHO, não erro: a conta não terminou o wizard, ou um módulo foi
  // desligado com esta aba aberta. O app rebusca o /me e se remonta.
  if (corpo.code === 'ONBOARDING_PENDENTE' || corpo.code === 'MODULO_DESLIGADO') {
    avisar(PRODUTO_MUDOU);
  }
  if (!res.ok) {
    // `error` é o campo das recusas do produto. Um 500 do Nest NÃO tem esse
    // campo — ele traz `message` —, e ignorá-lo transformava toda falha de
    // servidor em "Falha inesperada.", que não diz nem o status. O status entra
    // sempre: é o primeiro dado que quem depura precisa.
    const dito = corpo.error ?? corpo.message;
    throw new ErroDaApi(
      res.status,
      typeof corpo.code === 'string' ? corpo.code : undefined,
      dito ? `${dito} (HTTP ${res.status})` : `A API respondeu ${res.status} sem explicar o motivo.`,
      typeof corpo.outcome === 'string' ? corpo.outcome : undefined,
      typeof corpo.evidence === 'string' ? corpo.evidence : undefined,
      typeof corpo.localMessageState === 'string' ? corpo.localMessageState : undefined,
      typeof corpo.diagnosticPersistence === 'string' ? corpo.diagnosticPersistence : undefined,
      typeof corpo.operationId === 'string' ? corpo.operationId : undefined,
      typeof corpo.phase === 'string' ? corpo.phase : undefined,
      typeof corpo.providerAcceptance === 'string' ? corpo.providerAcceptance : undefined,
      typeof corpo.receiptPersistence === 'string' ? corpo.receiptPersistence : undefined,
      typeof corpo.acceptanceProvenance === 'string' ? corpo.acceptanceProvenance : undefined,
      typeof corpo.recoveryAction === 'string' ? corpo.recoveryAction : undefined,
    );
  }
  return corpo as T;
}

/**
 * Trata a falha de uma chamada disparada e esquecida (carregamento de tela).
 *
 * 401 aqui é normal e não é problema da tela: a sessão morreu — no logout, por
 * expiração, ou porque a conta foi inativada — e quem redireciona é o App. Sem
 * este filtro, cada chamada em voo no momento do logout vira uma **rejeição não
 * tratada**, que o navegador registra como exceção da página. Foi assim que o
 * teste de navegador pegou o primeiro defeito real.
 */
export function ignorarSessaoMorta(e: unknown): void {
  if (e instanceof ErroDaApi && e.status === 401) return;
  // Tratados centralmente pelo App, que rebusca o /me e remonta. Deixá-los
  // chegar ao console faria a tela reclamar de algo que já está sendo resolvido.
  if (e instanceof ErroDaApi && (e.codigo === 'ONBOARDING_PENDENTE' || e.codigo === 'MODULO_DESLIGADO')) return;
  console.error(e);
}

export const api = {
  get: <T>(c: string) => chamar<T>(c),
  post: <T>(c: string, corpo?: unknown) =>
    chamar<T>(c, { method: 'POST', body: corpo ? JSON.stringify(corpo) : undefined }),
  postWithHeaders: <T>(c: string, corpo: unknown, headers: Record<string, string>) =>
    chamar<T>(c, { method: 'POST', body: JSON.stringify(corpo), headers }),
  patch: <T>(c: string, corpo?: unknown) =>
    chamar<T>(c, { method: 'PATCH', body: corpo ? JSON.stringify(corpo) : undefined }),
  put: <T>(c: string, corpo?: unknown) =>
    chamar<T>(c, { method: 'PUT', body: corpo ? JSON.stringify(corpo) : undefined }),
  del: <T>(c: string) => chamar<T>(c, { method: 'DELETE' }),

  /**
   * Envia um arquivo (ADR-0024). Sem `content-type`: o navegador precisa montar
   * o `boundary` do multipart sozinho, e declará-lo à mão quebra o parse no
   * servidor de um jeito que não diz o que houve.
   */
  async enviarArquivo(arquivo: File): Promise<{ id: string; tipo: string }> {
    const corpo = new FormData();
    corpo.append('arquivo', arquivo);
    const res = await fetch(`${BASE}/api/bff/arquivos`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'x-requested-with': 'leadshug-web' },
      body: corpo,
    });
    const bruto = await res.text();
    let json: Record<string, string> = {};
    try {
      json = bruto ? JSON.parse(bruto) : {};
    } catch {
      throw new ErroDaApi(res.status, 'RESPOSTA_NAO_E_JSON', 'A API respondeu algo que não é JSON.');
    }
    if (!res.ok) throw new ErroDaApi(res.status, json.code, json.error ?? 'Falha ao enviar o arquivo.');
    return json as unknown as { id: string; tipo: string };
  },
};

/** O endereço de leitura de um arquivo guardado — passa pela sessão. */
export function urlDoArquivo(id: string | null | undefined): string | null {
  return id ? `${BASE}/api/bff/arquivos/${id}` : null;
}

export interface Produto {
  /** JÁ interseccionado no servidor (env ∩ Mantenedora) — aqui não se faz conta. */
  modulos: { canalNaoOficial: boolean };
  marca: { nome: string | null; cor: string | null; corClaro: string | null; corEscuro: string | null; corSecundaria: string | null; tema: string; logo: string | null };
  /** O wizard ainda não terminou: o app monta o wizard, não o produto. */
  onboardingPendente: boolean;
}

export interface Eu {
  id: string;
  nome: string;
  email: string;
  precisaTrocarSenha: boolean;
  papel: string | null;
  mantenedora: { id: string; name: string } | null;
  escopo: string[];
  produto: Produto;
  telefone: string | null;
  avatar: string | null;
}

export interface BusinessUnit {
  id: string;
  name: string;
  phone: string | null;
  papel?: string | null;
  setor?: { id: string; name: string } | null;
  channels: {
    id: string;
    type: string;
    status: string;
    generation?: number;
    currentAttemptId?: string | null;
    ownNumberVerified?: boolean;
    providerConnectionState?: string | null;
    receiptVerifiedAt?: string | null;
    requiresWindow?: boolean;
    connectedAt?: string | null;
  }[];
}

export interface TemplateDefinition {
  name: string;
  language: 'pt_BR';
  category: 'MARKETING' | 'UTILITY';
  body: string;
  header?: string;
  footer?: string;
  examples: Record<string, string>;
}

export interface TemplateReceipt {
  id: string;
  sequence: number;
  phase: string;
  safeCode: string | null;
  remoteTemplateId: string | null;
  acceptanceProvenance?: string | null;
  createdAt: string;
}

export interface TemplateOperation {
  id: string;
  phase: string;
  revision: number;
  providerAcceptance: 'CONFIRMED' | 'UNKNOWN';
  acceptanceProvenance?: 'ACKNOWLEDGED' | 'CORRELATED_BY_DEFINITION' | null;
  receiptPersistence: 'RECORDED' | 'UNCONFIRMED';
  safeCode?: string | null;
  remoteTemplateId: string | null;
  updatedAt: string;
  leaseExpiresAt: string | null;
  recoveryAction: 'WAIT' | 'RECONCILE' | null;
  savedObservation?: TemplateSummary | null;
  receipts?: TemplateReceipt[];
}

export interface TemplateDraft {
  id: string;
  mantenedoraId: string;
  buId: string;
  creatorUserId: string;
  channelId: string;
  revision: number;
  state: 'DRAFT' | 'LOCKED';
  definition: TemplateDefinition;
  definitionFingerprint?: string;
  savedObservation?: TemplateSummary | null;
  currentOperation?: TemplateOperation | null;
  recentOperations?: TemplateOperation[];
}

export interface TemplatePreview {
  definition: TemplateDefinition;
  renderedText: string;
  requestFingerprint: string;
  persistence: 'PERSISTED' | 'UNPERSISTED';
}

export interface TemplateSummary {
  remoteTemplateId: string;
  status: string;
  name: string | null;
  language: string | null;
  category: string;
  parameterFormat: string;
  components: unknown[];
  supported: boolean;
  semanticFingerprint: string | null;
  available: boolean;
  safeCode?: string;
  observedAt: string;
  observedFence: string;
  eligible: boolean;
  matchesDefinition?: boolean;
  eligibleForUse?: boolean;
}

export interface TemplateCatalogPage {
  items: TemplateSummary[];
  nextCursor: string | null;
  available: boolean;
  safeCode?: string;
  observedAt: string | null;
}
export interface TemplateRefreshInProgress { phase: 'REFRESH_IN_PROGRESS'; retryAfter: number }

export interface TemplateCapabilities {
  available: boolean;
  expectedGeneration: number;
  explanation: string | null;
}

export const templateApi = {
  capabilities: (buId: string, channelId: string) =>
    api.get<TemplateCapabilities>(`/business-units/${buId}/channels/${channelId}/message-template-capabilities`),
  listDrafts: (buId: string, view: 'mine' | 'bu' = 'mine', page = 1, limit = 20) =>
    api.get<{ items: TemplateDraft[]; page: number; limit: number; total: number; hasMore: boolean }>(
      `/business-units/${buId}/message-templates?view=${view}&page=${page}&limit=${limit}`),
  preview: (buId: string, input: { channelId: string; expectedGeneration: number; draftId?: string; expectedRevision?: number; definition: TemplateDefinition }) =>
    api.post<TemplatePreview>(`/business-units/${buId}/message-templates/preview`, input),
  createDraft: (buId: string, input: { clientRequestId: string; channelId: string; expectedGeneration: number } & TemplateDefinition) =>
    api.post<TemplateDraft & { replayed?: boolean }>(`/business-units/${buId}/message-templates`, input),
  getDraft: (draftId: string) => api.get<TemplateDraft>(`/message-templates/${draftId}`),
  saveDraft: (draftId: string, expectedRevision: number, definition: TemplateDefinition) =>
    api.patch<TemplateDraft>(`/message-templates/${draftId}`, { expectedRevision, definition }),
  submit: (draftId: string, idempotencyKey: string, input: { expectedRevision: number; expectedGeneration: number; expectedDefinitionFingerprint: string }) =>
    api.postWithHeaders<TemplateOperation & { replayed?: boolean; recoveryInProgress?: boolean }>(
      `/message-templates/${draftId}/submit`, input, { 'idempotency-key': idempotencyKey }),
  operation: (draftId: string, operationId: string) =>
    api.get<TemplateOperation>(`/message-templates/${draftId}/operations/${operationId}`),
  reconcile: (draftId: string, operationId: string) =>
    api.post<TemplateOperation & { recoveryInProgress?: boolean }>(`/message-templates/${draftId}/operations/${operationId}/reconcile`, {}),
  refreshDraft: (draftId: string) => api.post<(TemplateSummary & { matchesDefinition?: boolean; eligibleForUse?: boolean }) | TemplateRefreshInProgress>(`/message-templates/${draftId}/refresh`, {}),
  catalog: (buId: string, channelId: string, after: string | null = null) =>
    api.get<TemplateCatalogPage>(`/business-units/${buId}/channels/${channelId}/message-template-catalog${after ? `?after=${encodeURIComponent(after)}` : ''}`),
  refreshCatalog: (buId: string, channelId: string, after: string | null = null) =>
    api.post<TemplateCatalogPage | TemplateRefreshInProgress>(`/business-units/${buId}/channels/${channelId}/message-template-catalog`, after ? { after } : {}),
};

export interface Setor {
  id: string;
  nome: string;
  status: 'ATIVO' | 'INATIVO';
  numeros: number;
}

export interface Atividade {
  id: string;
  categoria: string;
  entidade: string;
  ator: string | null;
  texto: string;
  de: string | null;
  para: string | null;
  em: string;
}

export interface Conversa {
  id: string;
  contact: string;
  displayName: string | null;
  status: string;
  attendantName: string | null;
  unreadCount: number;
  lastMessageAt: string | null;
}

export interface Mensagem {
  id: string;
  direction: 'IN' | 'OUT';
  content: string | null;
  channelOrigin: string;
  authorName: string | null;
  createdAt: string;
}

export interface Thread {
  conversa: { id: string; contato: string; nome: string | null; status: string; atendente: string | null };
  janela: { exigida: boolean; aberta: boolean; expiraEm: string | null; canal: string | null; disponivel: boolean; motivo: string | null };
  messages: Mensagem[];
  paginacao: { limite: number; temAnteriores: boolean; cursorAnterior: string | null };
}
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


## foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-candidate-r30-disposition-v1.1.json

```text
{
  "schema": "stcon05.r30-root-candidate-disposition.v1",
  "recorded_at_utc": "2026-10-22T00:37:12.844930+00:00",
  "delivery": "Pending",
  "current_all": "r30 all789 remains an honest accepted historical candidate; it does not cover the newly identified orderings. No rerun or product mutation yet.",
  "adjudication": "Performance and TQA do not establish a severe runtime or test-quality blocker; security and adherence identify concrete changed-owner D07/D08 counterexamples. Lane thresholds are compatible. Root integrates three bounded corrections; no cosmetic third opinion and no debt waiver for these current behavior defects.",
  "findings": [
    {
      "ids": [
        "OPS-R3-01",
        "SEC-R30-01",
        "ADH-R30-02"
      ],
      "decision": "Integrated; blocking current candidate context/catalogue contract",
      "evidence": "Common projectRow eligible=true versus same-fence projectSavedObservation eligible=false due draft association; equal-fence AND contaminates common view. Root confirmed source, not executed yet.",
      "direction": "Preserve authoritative common eligibility separately from draft proof inside the existing component owner; retain genuine false common gates, strict editor proof and immutable ACK semantics. Add pure merge-order cases plus real BFF externally changed supported definition, no BFF mocking."
    },
    {
      "ids": [
        "SEC-R30-02"
      ],
      "decision": "Integrated; blocking current refresh/reload contract",
      "evidence": "atualizarStatus catch overwrites exact historical classification with generic refresh-unavailable while retaining old context-relative numeric fence. Root confirmed source; sequence unexecuted.",
      "direction": "Failure must not manufacture current-context authority from a historical observation. Test old high fence restored after normal same-account reauthorization, actual failed refresh, then actual lower-fence current success; retained time and immediate current DOM adoption."
    },
    {
      "ids": [
        "ADH-R30-01"
      ],
      "decision": "Integrated; blocking known newer PAUSED observation regression",
      "evidence": "Successful individual refresh blindly replaces catalogue entry rather than selecting against its current known higher fence. Passive GET does not advance completed intent, so source-supported feasible ordering can revert PAUSED to old APPROVED before derived GET. Root confirmed source; no executed reproduction yet.",
      "direction": "Select each same-resource page item against incoming status within current state; keep intent authority and persisted fence ordering independent. Real BFF held older individual response, newer cached PAUSED via passive GET, derived GET held during UI assertions; no added provider call or new store."
    }
  ],
  "test_admission": "One sole executor may add deterministic fail-first regressions only on web-app/src/telas/Modelos.spec.ts and web-app/e2e/message-templates.spec.ts after public source inspection. Product Modelos/API/fixtures remain byte-exact. Stop for root static review/freeze before any canonical browser RED run. Preserve every existing assertion/cooldown/cardinality and real BFF payload. No selected tests, runner changes, broad fixtures or product correction in this step.",
  "runtime": "DevOps preparation may finish as unexecuted public artifacts only. No preserved inspection/migration/build/recreate/tunnel/Meta action until new gates close.",
  "security": "Reported credential containment and existing private-cohort read-budget debt remain unchanged; no new secret confirmation/retest."
}
```


## foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r30-security.raw-attempt1.txt

```text
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r30-security.dispatch.json",
  "review_kind": "critique",
  "reviewer_label": "fresh-internal-no-context-security-r30",
  "overall_assessment": "Recommend holding affected candidate closure for two source-supported projection regressions: draft-specific ineligibility still contaminates common catalogue eligibility at an equal fence, and failure handling can erase historical-context classification and subsequently reject a valid current-context observation. Both concern changed observation-selection behavior and explicit D04/D07/D08 requirements. Their exact sequences are not demonstrated by the supplied executed cases; this reviewer performed no tools, tests or live attacks.\n\nSecurity framing: risk remains high because authenticated sellers can create external assets in a shared account. Attack simulation is required. The package supplies controlled BFF/PostgreSQL/provider-boundary evidence and the reported r30 canonical all result: 284 API unit, 398 PostgreSQL, 37 Web unit and 70 Playwright cases, including 69 browser cases and one pure consumer case. Source, seal, receipt and served-bundle bindings are supplied attestations; I did not independently recompute them.\n\nAttack surfaces assessed include session/CSRF boundaries, active actor and BU grants, draft ownership and administrative authority, operation identity, current versus historical account contexts, credential resolution, provider response consumption, observation ordering, parameterized persistence, escaped React rendering and resource consumption. Unchanged middleware, provider parsing and omitted submission methods retain their recorded prior assurance and hash comparisons. No fresh evidence warrants reopening the accepted late-ACK design, global technical account coordination, typed refusal classification or original one-POST policy.\n\nAuthorization and association: the changed saved-observation projector remains an internal consumer of authorized draft/operation reads. Current observation lookup requires matching tenant, BU, channel, resource identity and account association before permitting generation or credential renewal. Changed-account history remains unavailable. Observation commit paths retain captured-session and current actor/role/context checks under transaction locks. The bounded changes establish no new tenant breakout, arbitrary credential selection or recipient-send capability.\n\nObservation ownership: meaningful completed intents correctly separate observation authority from request issuance. A 202 does not advance authority; derived catalogue GETs inherit their originating intent; passive reads capture the completed watermark and cannot promote it. Context/editor checks precede automatic recovery hydration. Later sequential draft reads now supply coherent current operation metadata, with matching recent receipts used for presentation. These substantively address SEC-R13-01 and the recorded ordering defects. Accessible observedAt presentation also follows the approved evidence distinction. The two findings identify additional interactions within this changed owner.\n\nAdherence: D01–D03, D05–D06 and D09 show no new bounded drift. CR-01/02 and AR-V11-01/02/03 retain their recorded dispositions. D04/D07/D08 and CR-V11-01 have the projection exceptions below. In particular, common catalogue eligibility must retain its own authoritative gates while draft-definition and ACK-association restrictions remain scoped to the editor. Historical context classification must survive failure projection so numeric fences remain comparable only within their context class.\n\nEvidence limits remain explicit. Original feature provenance is test-after/unknown. The r16 failures establish their reached assertions only; r21 establishes five new semantic REDs while its derived-read case was incomplete; r27 metadata RED retains the complete worker segment but lacks initial setup stdout; r28 did not inspect the final catalogue response; r29 failed in its first merge order before later assertions. Reported r30 GREEN completes the current assertions without extending those earlier RED claims. Empty-200 browser-race coverage remains unproved. ACK-conflict presentation has PostgreSQL producer and pure consumer evidence, without a browser conflict-race claim. Both template FRC markers belong to the browser journey: 100 actual BFF requests and a separate 100 UI attempts coalesced into one BFF request. Fixtures establish no actual Meta acceptance or account readiness.\n\nPerformance is acceptable at this boundary: authority metadata is constant-size, loaded observation selection remains bounded by loaded items, and current-context projection adds bounded indexed local reads without provider I/O. Existing page-first hydration and bounded history remain supported by supplied plans. No production capacity, SLO or external exactly-once claim follows. Elegance is acceptable: the existing selector and authority owner are an appropriate small design; the findings call for narrow scope/classification corrections rather than another cache or generic framework. Structural soundness and operational fit remain mixed because the new interactions can misrepresent common eligibility or retain historical status after a successful current refresh.\n\nResidual risk: SEC-R6-04 remains deferred through foundation_documentation/backlog/README.md#BLG-leadshug-template-recovery-read-budget, owned by integrations-and-channels/security and restricted to the existing private local cohort. Sequential authorized reconciliation can still amplify provider reads; persistent operation/account budgets and separate approval remain prerequisites to untrusted/public admission or Railway. Operator-confirmed credential revocation/disablement is accepted reported containment. Historical use and removal of previously rendered text remain unestablished; no new confirmation or credential retest is requested.\n\nThreat-intelligence input is limited to the embedded historical attribution to OWASP API1, API4 and CSRF guidance. No fresh intelligence retrieval or dependency-advisory clearance was performed. Preserved TEST migrations, source-bound activation, actual assisted Meta submission/status, formal PCV disposition and fresh final review remain pending. This assessment grants no activation or delivery approval.",
  "recommended_path": "Return for the two narrow projection corrections and meaningful regression evidence within the existing approved paths. Preserve common eligibility gates, editor-specific restrictions, historical associations, one-POST behavior and accepted debt. After current validation and affected independent reassessment close, continue the already approved PCV, TEST preflight, activation, assisted Meta proof and final-review sequence; delivery remains Pending.",
  "performance_position": "acceptable",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "SEC-R30-01",
      "severity": "medium",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Equal-fence merging still applies draft-specific ineligibility to the common catalogue",
      "rationale": "In web-app/src/telas/Modelos.tsx, selectTemplateObservation's equal-fence branch ANDs current.eligible with candidate.eligible. TemplateObservationService.projectSavedObservation separately narrows eligible for draft-definition matching and ACK association. Consequently, a fresh supported APPROVED catalogue row with available=true and eligible=true becomes commonly ineligible when an authorized draft read supplies the same remote ID/fence with available=true but draft-specific eligible=false. This occurs for a changed remote definition or PROVIDER_ACK_CONFLICT. mergeTemplateObservations processes catalogue pages and then the individual projection, so the common catalogue also displays the restriction. Removing the unconditional eligibleForUse veto does not resolve this equal-fence path because item.eligible is already false. The current scope test covers an older PAUSED individual and a newer catalogue fence, not this pairing. This is fresh evidence in the changed selector/scope correction and contradicts the explicit common-versus-draft boundary; it does not challenge accepted ACK handling. Exploitability is source-supported but unexecuted here. Blast radius is incorrect eligibility presentation for an already authorized account asset.",
      "suggested_action": "A (recommended): preserve the authoritative common observation's eligibility when combining equal-fence common and draft projections, while retaining matchesDefinition/eligibleForUse and ACK restrictions for the editor. Preserve genuinely false common eligible/available gates; do not simply remove item.eligible or add a generic safeCode veto. B: make the existing projection explicitly scope-aware for the two views, using the same state owner and no additional API/cache. C: retain the extra catalogue restriction; this requires explicit disposition of the approved scope exception and should not silently close D07. Verify equal-fence common APPROVED/available/eligible data combined with draft-only rejection in both relevant orders: the catalogue remains eligible, the editor remains restricted, and false common gates still block. Use actual projector payload semantics; no browser ACK-conflict proof is inferred from the existing pure consumer case.",
      "affected_paths": [
        "web-app/src/telas/Modelos.tsx:124",
        "web-app/src/telas/Modelos.spec.ts",
        "api-app/src/domain/message-templates/template-observation.service.ts:192"
      ]
    },
    {
      "finding_id": "SEC-R30-02",
      "severity": "medium",
      "category": "structural_soundness",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Refresh failure erases historical classification and lets an old fence defeat current success",
      "rationale": "In web-app/src/telas/Modelos.tsx, atualizarStatus's catch creates unavailable(item) by unconditionally replacing safeCode with TEMPLATE_REFRESH_UNAVAILABLE. The new selector uses exact TEMPLATE_CONTEXT_STALE classification before comparing context-relative numeric fences. After same-account reauthorization, an original-context PAUSED observation at fence 100 can be restored as historical while the new context has no observation. A failed explicit refresh relabels that historical copy as a current-class unavailable observation, retaining fence 100. A later successful current-context APPROVED response at fence 2 then loses numeric selection against 100, leaving historical PAUSED/unavailable status visible despite successful refresh. An unwarmed catalogue need not provide another current copy to rescue selection. Existing tests cover direct historical-to-current selection and same-context failure separately, leaving this composition uncovered. The newly introduced classifier makes this a changed-locus interaction rather than reopening unchanged architecture. The sequence is source-supported and has not been reproduced by this reviewer; it creates a conservative availability/status regression, without evidence of unauthorized sending.",
      "suggested_action": "A (recommended): preserve historical-context classification when marking an already historical observation unavailable, so failure cannot manufacture current-context authority. Keep conservative failure restrictions for observations already belonging to the current context. B: represent context classification explicitly inside the existing observation owner if that can be done without expanding the public contract or adding another cache. C: require reload to recover the current observation; this leaves the approved explicit-refresh behavior unmet. Add a deterministic regression with an old historical fence greater than the restarted current fence: historical restore, current refresh failure, then current refresh success. Assert truthful retained time during failure and immediate adoption of current status/eligibility after success, with existing provider-call bounds and immutable operation binding preserved.",
      "affected_paths": [
        "web-app/src/telas/Modelos.tsx:115",
        "web-app/src/telas/Modelos.tsx:697",
        "web-app/src/telas/Modelos.spec.ts",
        "web-app/e2e/message-templates.spec.ts"
      ]
    }
  ]
}
```


## foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r30-adherence.raw-attempt1.txt

```text
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r30-adherence.dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "fresh-internal-no-context-adherence-r30",
  "overall_assessment": "Candidate adherence requires two bounded corrections in the changed observation consumer. The original four r13 findings have substantive corrections and current execution evidence, but observation selection still loses a newer cached fence in one admissible response ordering, and equal-fence merging still lets draft-specific eligibility restrict the common catalogue. These are source-supported counterexamples; this reviewer executed no tools or tests.\n\nDecision table — assessed at candidate scope:\n| Decision | Position | Evidence and limits |\n| D01 | Adherent | Seller submission and owner/admin access remain intact; the supplied browser journeys use normal authenticated product flows without an intermediate approval role. |\n| D02 | Adherent | Backend preview/definition authority and persisted fingerprints remain unchanged; the consumer retains preview debounce, escaped rendering and edit/context guards. |\n| D03 | Adherent | Draft revision/CAS and immutable submission snapshots remain owned by message-templates. Variations create new drafts rather than modifying remote assets. |\n| D04 | Adherent for this correction | projectSavedObservation resolves the current context only when tenant, BU, channel, resource identity and account association match. Generation/credential renewal does not rebind the operation. The new PostgreSQL case and normal browser reauthorization/refresh/reload pass in r30. Changed-account history remains unavailable or absent. |\n| D05 | Adherent on carried producer evidence | Durable operation/name/quota coordination, captured dispatch authority and bounded provider access remain unchanged. The follow-up introduces no extra provider call or parallel submission path. |\n| D06 | Adherent on carried producer evidence | The accepted immutable ACK fact and associated resource identity remain distinct. No current change weakens original one-POST behavior, certainty reporting or immutable associations. The ACK-conflict consumer case remains pure-function evidence, not a browser conflict race. |\n| D07 | Exception | Backend shared observation ownership remains consistent with the contract, and the current cross-producer 202, passive/derived-read, failure and timestamp scenarios pass. Findings ADH-R30-01/02 identify remaining consumer projection defects. |\n| D08 | Exception | Recovery now uses the later sequential draft metadata and preserves dirty text behind context/editor guards. However, ADH-R30-01 permits an older observation to replace a newer cached observation despite the same-context fence requirement. |\n| D09 | Adherent | Narrow template ports, scoped integration resolver, explicit factory registry and TemplateManagementModule reuse of ChannelTransportModule preserve the approved boundary. No textual Channel extension, fake unsupported provider, generic platform or compatibility bridge is introduced. |\n| CR-01 | Adherent | GETs remain observational; recovery remains explicit and associated with the same durable operation, without automatic POST replay. |\n| CR-02 | Adherent on unchanged evidence | Conservative typed refusal versus ambiguity behavior is unchanged; current consumer changes do not reinterpret correlation as acknowledgement. |\n| AR-V11-01 | Adherent on carried evidence | Real PostgreSQL transaction and commit-return fault evidence remains recorded; positive bounded readback, rather than inferred rollback or acceptance, governs certainty. |\n| AR-V11-02 | Adherent on carried evidence | Global technical account coordination remains separate from tenant-owned definitions, operations and observations. |\n| AR-V11-03 | Adherent by supplied attestations | Initial admission and current source/seal records report the required comparisons, including three unchanged product HEADs and thirty protected sources. This reviewer did not recompute hashes. |\n| CR-V11-01 | Backend adherent; consumer exception | Both producers retain one persistent context lease/fence/projector. ADH-R30-01 concerns loss of a higher observation fence already known by the consumer, rather than backend write authority. |\n\nCurrent evidence calibration: r30 is the supplied successful canonical all: 284 API unit, 398 PostgreSQL, 37 Web unit and 70 Playwright cases, totaling 789; Playwright includes 69 browser cases and one pure consumer case. The supplied attestations bind validation to 38 sources, matching served/dist bundle bytes and 25 disposable migrations. Both template FRC markers are browser-suite evidence: 100 actual BFF requests with 99 blocked 202 responses and one completed provider leader, plus a separate 100 UI attempts coalesced into one BFF refresh with PAUSED/ineligible DOM adoption. This proves the executed scenarios, not every admissible cache ordering.\n\nHistorical RED limits remain correctly bounded: r16 establishes its reached projection/context/timestamp failures; r21 establishes five semantic failures but not its timed-out derived-read oracle; r27 retains the complete worker segment for the two metadata failures while missing the setup stdout prefix; r28 did not inspect the final catalogue response; r29 failed in the first merge order before subsequent assertions. Current r30 completes the authored assertions without retroactively expanding those RED claims. Original feature provenance remains test-after/unknown. Empty-200 browser coverage remains a disclosed limitation.\n\nPerformance is acceptable for the approved slice: page-first SQL bounds child hydration, detail history and catalogue probes are bounded, current-context projection uses exact indexed lookups, and the new authority bookkeeping adds no network fan-out. Deep OFFSET/count work and the fixture measurements establish no production capacity or SLO. Elegance and structural soundness are mixed because the observation authority and selector are bypassed by destructive page replacement and by mixing common eligibility with draft association proof; the issue cards request correction inside the existing owner, not architectural expansion.\n\nNo new temporary exception or cutover shim is evident. TQA-ST05-03 and SEC-R6-04 remain under their recorded dispositions; the latter retains BLG-leadshug-template-recovery-read-budget and private-local-cohort containment before separately approved public admission or Railway. Operator-confirmed credential revocation/disablement is reported containment only. Preserved TEST migration, activated runtime provenance, actual Meta submission/status, module consolidation, formal PCV disposition and final review remain later mandatory gates. Delivery remains Pending.",
  "recommended_path": "Hold candidate adherence closure for the two narrow observation-consumer corrections. Preserve the approved backend, ACK design and existing assertions. Add deterministic regressions for higher cached fence preservation and equal-fence common-versus-draft eligibility, run the required validation for the corrected source, and obtain affected independent reassessment. Then continue through the remaining candidate/PCV gates, bounded TEST preflight and activation, assisted actual Meta proof and fresh final review.",
  "performance_position": "acceptable",
  "elegance_position": "mixed",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "ADH-R30-01",
      "severity": "high",
      "category": "adherence",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "An admitted refresh can overwrite a higher observation fence already cached in a catalogue page",
      "rationale": "Blocking D07/D08 consumer gap in web-app/src/telas/Modelos.tsx, atualizarStatus(): the successful branch selects the response only against individualStatus, then unconditionally replaces matching catalogue items with that response. It never compares the incoming fence with the current catalogue item. A feasible ordering is: an individual refresh produces APPROVED at fence 2 but its response is held; another authorized client persists PAUSED at fence 3; an already pending passive catalogue GET reads fence 3 and reaches this screen while the individual response remains held. Passive reads correctly do not advance completedIntent, so the old individual intent remains admissible. Releasing fence 2 selects it against an older individualStatus and replaces the cached fence-3 catalogue item. Both views can revert to eligible APPROVED until the subsequent derived GET completes. Holding that derived GET exposes the regression. The current meaningful-intent tests do not cover this ordering because the newer observation here arrives through a passive read, without a newer completed UI intent. This is source-supported, not a reviewer-executed reproduction.",
      "suggested_action": "A (recommended): apply the existing same-resource selector against the current catalogue entry before replacing it, and preserve the highest currently known observation across individual and catalogue state. Retain meaningful-intent admission as a separate condition; it does not replace persisted-fence ordering. B: centralize these writes in the already intended component-local observation reducer so every adoption reads the current cache atomically; no new API, provider call or generic store is needed. C: retain eventual correction by the derived GET; unsuitable because it permits a known PAUSED observation to regress during an outstanding read. Add a real-BFF regression with a held older individual response, a newer PAUSED observation admitted through a passive catalogue GET, and a held derived GET. Assert that editor/catalogue remain PAUSED and ineligible throughout release, with unchanged provider mutation counts.",
      "affected_paths": [
        "web-app/src/telas/Modelos.tsx:686",
        "web-app/e2e/message-templates.spec.ts"
      ]
    },
    {
      "finding_id": "ADH-R30-02",
      "severity": "medium",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Equal-fence merging still promotes a draft-specific eligibility restriction into the common catalogue",
      "rationale": "Blocking gap in the scoped-eligibility correction. TemplateObservationService.projectRow() returns common eligibility, whereas projectSavedObservation() replaces eligible with a value additionally constrained by matchesDefinition and ACK association. For the same current APPROVED, supported, available observation and fence, the catalogue can therefore return eligible=true while an authorized saved draft projection returns eligible=false, matchesDefinition=false and eligibleForUse=false. selectTemplateObservation(), at web-app/src/telas/Modelos.tsx:125–126, combines equal-fence eligible values with AND. mergeTemplateObservations consequently produces eligible=false for the common item, and templateObservationEligible(..., draftScoped=false) still rejects it through item.eligible. Removing the unconditional eligibleForUse veto fixes the strictly-newer catalogue case tested in r29/r30, but not this equal-fence case. A changed remote definition or draft ACK-association conflict can thus suppress common catalogue eligibility. This contradicts the package's explicit separation of common catalogue eligibility from draft-specific proof; no generic safeCode veto is involved.",
      "suggested_action": "A (recommended): preserve the common catalogue eligibility fact independently of draft-specific matchesDefinition/eligibleForUse restrictions within the existing selector/projection, while continuing to require both strict flags in the editor. Preserve real common eligible=false and available=false failures; do not repair this with a blanket OR or client-side eligibility recomputation. B: explicitly distinguish common observation facts from draft association proof in the existing internal projection, reviewing any public-contract change before implementation. C: retain false common ineligibility as an exception; not recommended and not currently approved. Add both merge-order tests using equal fences, available=true, common eligible=true and draft eligible=false/matchesDefinition=false/eligibleForUse=false. Require common eligibility true and editor eligibility false, retaining negative common-gate cases. Include a real-BFF saved-draft/catalogue case for an externally changed supported definition without changing immutable snapshots or ACK policy.",
      "affected_paths": [
        "web-app/src/telas/Modelos.tsx:126",
        "web-app/src/telas/Modelos.spec.ts",
        "api-app/src/domain/message-templates/template-observation.service.ts",
        "web-app/e2e/message-templates.spec.ts"
      ]
    }
  ]
}
```


## Approved bounded expectations

## Scope

- [ ] SCOPE-01 — Página autenticada Modelos de mensagem, com BU/canal oficial explícitos, listagem dos próprios rascunhos, editor textual com variáveis/exemplos e prévia.
- [ ] SCOPE-02 — Vendedor ATENDENTE+ cria/edita seus rascunhos e envia para análise da Meta, sem aprovação de ADMIN intermediária; ADMIN/OWNER da BU pode administrar rascunhos locais da mesma BU.
- [ ] SCOPE-03 — Capacidade abstrata estreita de gerenciamento de templates, separada de Channel.sendMessage; submissão oficial scoped, revisionada/idempotente, reserva de nome por conta/idioma e recuperação de resultado incerto sem repetir POST automaticamente; criptografia/segredos atuais preservados.
- [ ] SCOPE-04 — Atualização explícita de status/catálogo da Messaging account correta; aprovado/pendente/recusado/pausado/desativado/indisponível com evidência de consulta; somente APPROVED suportado pode ser indicado como apto para uso futuro.
- [ ] SCOPE-05 — Harness de dependências/capacidade e testes de domínio/contrato/concorrência PostgreSQL, Playwright contra BFF real e prova de criação/consulta em recurso oficial próprio, sem envio a destinatário; consolidação do contrato e revisões derivadas.


## Definition of Done

- [ ] DOD-01 — Vendedor ATENDENTE+ abre Modelos de mensagem, cria/salva/reabre seu rascunho por BU/canal, edita com revision CAS, preenche exemplos e vê prévia coerente; atores sem grant na BU e escopos alheios falham antes de efeitos.
- [ ] DOD-02 — Submissão no LeadsHug não exige ADMIN; usa a conta/credencial verificadas do canal, valida texto/variáveis/categoria/idioma e confirma snapshot/revisão; nenhuma mensagem ou conversa é criada.
- [ ] DOD-03 — Replays/duplo clique/crash não repetem POST por operação; conta/nome/idioma concorrentes são protegidos; resultado incerto permanece explícito e reconcile não faz POST externo nem vincula definição diferente.
- [ ] DOD-04 — Consulta/status e catálogo paginados refletem Meta com frescor/categoria efetiva, sem promover PENDING/UNKNOWN/recusado/pausado a pronto; erro seguro conserva estado anterior e não finge catálogo vazio.
- [ ] DOD-05 — Troca de BU/canal/revisão, saves concorrentes e status atrasado não sobrescrevem draft/estado atual; refresh da página recupera operação sem chave do browser e sem divulgar token/segredo.
- [ ] DOD-06 — Schema/migration deploy/status, harness durável, CI-equivalent completo e Playwright mutation passam com API/PG reais e bundle servido fresco; gate send de ST-CON-01 e contratos Channel/OutboundService de ST-CON-06 permanecem inalterados.
- [ ] DOD-07 — Operador valida criar/submeter um modelo textual de teste na conta correta e consultar seu resultado real; decisão Meta pode ser PENDING/REJECTED sem falsear APPROVED. Consumo físico aprovado no ST-CON-04 continua dependência separada.
- [ ] DOD-08 — Decisões e contrato promovidos ao módulo responsável, revisões derivadas/segurança/pcv/TQA/final e guardas de entrega satisfeitos; sem P1/P2 aberto e sem claim de produção.



## Source inclusion inventory

[{"path": "web-app/src/telas/Modelos.tsx", "sha256": "0a1796367f9f415e1de6b552b06dc56e322898ec84789043a6be868c63f4fd19"}, {"path": "web-app/src/api.ts", "sha256": "177d660cccb7d74e47ef1dd180d9e74f830bce97b631c896c4e82fa39ae44a84"}, {"path": "api-app/src/domain/message-templates/template-observation.service.ts", "sha256": "41c7c640fd31ca0759d0d88647e24c74787597dcf75fd8a3c773fe6e02965488"}, {"path": "foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/root-candidate-r30-disposition-v1.1.json", "sha256": "47746af5490258d3c2d0494b358610d36f58d3ac711fd76f5f9900519cb9046d"}, {"path": "foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r30-security.raw-attempt1.txt", "sha256": "5bb28e45a0209312efc1df77d98b8afd29f6112d69031aed3674b5619fc95592"}, {"path": "foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/evidence/candidate-r30-adherence.raw-attempt1.txt", "sha256": "958451379fca41fb87140efcdf22f6e214239296809b870795b1d5dcaa6b8a4e"}]