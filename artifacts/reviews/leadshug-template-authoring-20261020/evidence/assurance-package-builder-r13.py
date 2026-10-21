import argparse, datetime, difflib, hashlib, json, re
from pathlib import Path

ROOT = Path('/mnt/c/unifast/leadshug/leadshug_now_docker')
B = ROOT/'foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020'
E = B/'evidence'
sha = lambda raw: hashlib.sha256(raw).hexdigest()
ap = argparse.ArgumentParser()
ap.add_argument('--freeze', required=True)
ap.add_argument('--log')
ap.add_argument('--source-proof')
ap.add_argument('--runtime-proof')
ap.add_argument('--receipt')
ap.add_argument('--output')
ap.add_argument('--size-only', action='store_true')
ap.add_argument('--rubric-set', choices=['baseline', 'security', 'adherence'], default='baseline')
a = ap.parse_args()
sections=[]; inventory=[]; selected_sources={}
def add(title, text):
    sections.append('\n## '+title+'\n\n'+text.strip()+'\n')
def source(path, text=None, omitted=None):
    p=ROOT/path; raw=p.read_bytes()
    if text is None:
        text=raw.decode('utf-8')
        if path.endswith('.json'):
            text=json.dumps(json.loads(text),ensure_ascii=False,separators=(',',':'))
            omitted='Formatting-only compact JSON; all keys/values retained; original raw bytes and digest recorded'
    text=text.replace('\r\n','\n')
    selected_sources[path]=text
    inventory.append({'path':path,'sha256':sha(raw),'bytes':len(raw),'selection':'full' if omitted is None else omitted})
    add(path+(' [selected; omission declared]' if omitted else ''), '```text\n'+text.rstrip()+'\n```')
freeze=json.loads((ROOT/a.freeze).read_text())
records=freeze['records']
assert len(records) >= 38 and len({r['path'] for r in records}) == len(records)
assert all(r['path'].startswith(('api-app/src/', 'api-app/test/', 'api-app/prisma/', 'web-app/src/', 'web-app/e2e/')) for r in records)
for r in records: assert sha((ROOT/r['path']).read_bytes())==r['sha256'],r['path']
inherited=json.loads((E/'inherited-working-tree-v1.1.json').read_text())
repo={'root':'','api':'api-app/','web':'web-app/'}
for r in inherited['records']:
    if not r['active_mutation_admitted']: assert sha((ROOT/(repo[r['repository']]+r['path'])).read_bytes())==r['sha256'],r['path']
add('Candidate scope and review instructions', '''Derived bounded-file-set, ST-CON-05 v1.1, approved 2026-10-21. Review only current sources and actual validation below. This is independent CANDIDATE assurance before local activation, not final delivery review. Final fresh review after actual runtime/provider proof remains required. Current delivery Pending; no preserved DB template migrations, new API/Web activation or actual template submission/status yet. Those steps are approved but gated by this candidate assurance and bounded metadata preflight. Do not report those honestly pending later steps as concealed completed evidence. Identify concrete risks in their plan. No required gate or consumer waived. All mutations stay sole-executor/principal checkout; no product commits/push/deploy, no worktree/copy. Original 30 inherited seals exact; every source in the supplied current freeze independently matches retained actual validation attestations below.

Claim: authenticated seller ATENDENTE+ can create/edit/save/preview and directly submit official textual templates to Meta; inspect statuses/catalog, recover uncertain results without POST replay; bounded persistent account/fence/lease and tenant/grant policies. Recipient send/new conversation ST-CON-04, media, handover, technical token mode, production and Railway excluded. Channel.sendMessage remains narrow text abstraction; template management uses a separate narrow capability.

Assessment calibration: performance, elegance, structural soundness and operational fit explicit. Every material finding needs concrete file/line, impact, options A/B/C including do-nothing if reasonable, recommendation and verification. Distinguish blocking from nonblocking risk; do not expand scope for style. Full applicable TQA workload in embedded rubric required, not just five questions. TQA must report every applicable framing, fail-first/retrofit classification, bypass scan, real-boundary/fallback/DI parity, CI/command/topology, source-served/platform matrix, assertion efficacy/efficiency, failure uncertainty and D01–D09/CR/AR decision-adherence assessment, plus the five explicit method answers. Use overall_assessment as a structured Markdown string inside the result JSON if the schema has no separate fields. Missing full workload is incomplete audit evidence even if findings are empty. Security uses controlled disposable negatives and primary-source refresh, no production attack. Cutover audit not_needed by additive approved scope; flag evidence of accidental shim if present. No arbitrary reviewer deadline or package reduction to obtain pass.

Fail-first honesty: primary feature tests were authored during implementation; not all have retained behavioral RED before product. Classify test-after/unknown rather than claim test-first. Compiler/lint/harness failures are not behavioral RED. Retained browser 53/54 failure 2da614756b0cf51586ee5bc0265e45b9dc5ae577de3c3facdeb36f0f890c2f3d specifically required REJECTED revision1 remoteTemplateId:null before the four-null projection repair; existing assertions stayed intact for revision1 and2. Earlier 41-pass browser abort was host disk/overlay/Bus error, not proven product error. Strong existing BCI fixture remains same 5x20 body; human admitted only explicit loopback listen + positive startup assertions to avoid Supertest7.2.2 implicit-listen/autoclose concurrency, no global wrapper.

Limits: browser tests use real session/BFF/PostgreSQL/Prisma and replace only provider network with deterministic external fake; actual provider proof remains later. The previous r6 candidate lacked actual account-change browser proof and had a weak FRC provider-effect oracle. Required corrections and current regressions are included below; judge their actual executed reachability and terminal evidence, not test titles or authored assertions. r7 retained 53/55: actual refresh-failure eligibility RED and an unrelated private-waba DTO fixture-oracle failure; FRC was not reached. Never infer new FRC proof from r6 or from inherited number-onboarding FRC. External exactly-once, approval, capacity/SLO, delivery continuity and future networks are not claimed.

Process deviations: earlier wrong sibling source mapping corrected by canonical exact hashes; reported broad API Git status once (no protected-file inspection proved); stale attestations rejected; earlier log basename collision lost old bytes and is recorded, no final evidence inferred from lost log; root mistaken CRLF flag corrected; earlier recursion hypothesis corrected to malformed Graph fixture. Most recent inherited CLI Bitrix24 startup diagnostic exposed a connector credential; known artifacts redacted and operator notified to revoke/reissue. No token included here and no connector tool call executed. Future CLI ignores user config; native executor now used. Operator explicitly confirmed revocation or disablement in both pending questions; the separate confirmation receipt below records the statement without testing or retaining the credential. Security must assess the containment and residual limits explicitly, not infer historical absence of use or retraction of prior rendered output. No source/runtime credential rotated by agent.''')
rubrics={
    'baseline':['delphi-ai/skills/test-quality-audit/SKILL.md','delphi-ai/workflows/docker/independent-test-quality-audit-method.md','delphi-ai/workflows/docker/performance-concurrency-validation-method.md'],
    'security':['delphi-ai/skills/security-adversarial-review/SKILL.md'],
    'adherence':[],
}
add('Lane workload and faithful bounding', 'Rubric set: '+a.rubric_set+'. Same frozen sources, prior findings/dispositions and actual validation retained for every lane. Baseline reviewers receive the FULL test-quality skill, independent TQA method and performance/concurrency method. Security receives its FULL security skill. Adherence receives the complete frozen behavior contracts and decision matrix. The orchestrator has read and executes the full triple-audit skill; only its complete gate calibration and lane-blocking criteria are embedded below, omitting CLI/session orchestration mechanics that reviewers do not execute. This changes packet duplication, not the required audit workload or gate. No reviewer receives a reduced five-question substitute for a required TQA.')
for path in rubrics[a.rubric_set]: source(path)
p='delphi-ai/skills/audit-protocol-triple-review/SKILL.md'; t=(ROOT/p).read_text()
source(p,t[t.index('## Gate Calibration'):t.index('## Procedure')], 'Complete Gate Calibration and Lane-Specific Blocking Criteria; orchestrator-only session/CLI procedures omitted, root loaded and owns them. Full-file digest retained.')
todo='foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md'
text=(ROOT/todo).read_text()
omit={'Decisions (Resolved Before Freeze)','Completion Evidence Matrix (Required Before Delivery Claim)','Plan Review Gate (Review of the Execution Plan; required for `medium|big`; abbreviated for low-risk `small`)','Additional Architectural Opinions (Required When Path Remains Materially Unclear)','Architecture Review Resolution Ledger — 2026-10-19','Critique Resolution Ledger — 2026-10-19','Historical Pre-approval Planning Gate Receipt — 2026-10-19 (reframing2026-10-20)','Reframing — Channel abstraction request, 2026-10-20','Execution Admission — 2026-10-21',
      'Execution Plan (Required Before `APROVADO`)','Assumptions Preview (Required Before Plan Review)',
      'Rules Acknowledgement / Ingestion (Required After `APROVADO` and Before Execution)',
      'Planning External References — consulted 2026-10-19','Handoff recebido de ST-CON-06 v1.3',
      'Rebase v1.1 — current review authority','Architecture v1.1 Finding Resolution','Critique v1.1 Finding Resolution',
      'Title','Artifact Identity','Context','Framing Source & Story Slice','Implementation Intent',
      'Delivery Status Canon (Required)','Active Work State (Required While TODO Remains In `active/`)',
      'Profile Scope & Handoffs (Required Before `APROVADO`)','Complexity',
      'Canonical Module Anchors (Required Before APROVADO)','Decision Pending (Resolve Before Freeze)',
      'Module Decision Baseline Snapshot (Required Before APROVADO)','Questions To Close',
      'Pattern References (Optional; Enforced When Cited)','Commands (Run Locally)',
      'Files Expected (Compatibility Note)','COMENTÁRIO:','Module coherence — one-to-one',
      'Current Pre-approval Planning Receipt — ST-CON-05 v1.1'}
parts=re.split(r'(?m)(?=^## )',text);kept=[]; omitted=[]
for part in parts:
    heading=part.splitlines()[0][3:] if part.startswith('## ') else ''
    if heading in omit: omitted.append(heading)
    else: kept.append(part)
selected_todo='\n'.join(kept)
sealed_reason='Baseline herdada ST-CON-06 SOMENTE; nova mutação proibida, hash exato obrigatório no inherited-working-tree-v1.1.json'
assert sealed_reason in selected_todo
selected_todo=selected_todo.replace(sealed_reason, 'SEALED-ST06')
selected_todo='SEALED-ST06 = '+sealed_reason+'. This legend replaces only repeated table reason text; every repository/path/change type remains explicit.\n\n'+selected_todo
source(todo,selected_todo, 'omit metadata/indexes/empty planning placeholders, historical resolved ledgers, duplicated execution HOW/intake and handoff history: '+', '.join(omitted)+'. Delivery remains Pending v1.1, no promotion or activation; explicit current profile/authority/limits above replace duplicated metadata. Full Scope/DOD/VAL/frozen decisions/contracts/consumer matrix/approval/gates kept. Approved activation HOW is separately included in full; root finding dispositions and full-file SHA preserve provenance.')
source('foundation_documentation/project_constitution.md')
for path in ['foundation_documentation/modules/identity-and-tenancy.md','foundation_documentation/modules/audit-and-history.md']:
    source(path)
p='foundation_documentation/modules/integrations-and-channels.md';t=(ROOT/p).read_text();source(p,t.split('## Cadastro de números ST-CON-01')[0]+ '\n## Channel abstrato e envio comum — ST-CON-06'+t.split('## Channel abstrato e envio comum — ST-CON-06',1)[1], 'Registration/operational/privacy history omitted; current Channel/narrow-capability contracts and invariants full; exact current registration credential context is in approved TODO and frozen code.')
source('foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/local-activation-plan-v1.1.md')
for r in records:
    path=r['path']
    if path=='api-app/test/number-onboarding-pcv.e2e-spec.ts': continue
    if path=='web-app/src/App.tsx':
        t=(ROOT/path).read_text();lines=t.splitlines(True)
        source(path,''.join(lines[:61])+ '\n[Unchanged theme/localStorage/brand-color effect omitted]\n'+ ''.join(lines[98:]), 'Only existing theme/localStorage/brand-color effect lines62-98 omitted; imports, complete identity/session/root state, route guards, Modelos route, shell/navigation and all remaining code kept. Complete two-line shared delta below.')
        continue
    if path=='api-app/test/helpers.ts':
        t=(ROOT/path).read_text();source(path,t.split('export const metaFake:',1)[0]+'\n[Unchanged pre-existing transport fakes omitted]\n'+t[t.index('export const TOKEN_INTERNO'):], 'Existing Meta/Evolution number/send fake bodies omitted; imports, constants, real AppModule/Prisma/session setup, cleanup and all tenant/channel/user fixtures kept. Exact complete shared delta below.')
        continue
    if path=='web-app/src/api.ts':
        t=(ROOT/path).read_text();source(path,t[:t.index('export interface Setor')], 'Only unrelated trailing sector/history/inbox DTO declarations omitted; complete HTTP/error layer, identity/BU and all template DTO/wrappers kept. Exact shared delta below.')
        continue
    if path=='api-app/src/integrations/meta/message-template.client.spec.ts':
        t=(ROOT/path).read_text()
        baseline_path=B/'candidate-assurance-r6-package-v1.1.md'
        baseline_raw=baseline_path.read_bytes()
        assert sha(baseline_raw)=='03c417596546a7d141c25febeaff6826a9de21e62dbaa7aff8ef32652bf84808'
        packet=baseline_raw.decode(); start=packet.index('\n## '+path+'\n'); end=packet.index('\n## ',start+5)
        old=packet[start:end].split('```text\n',1)[1].rsplit('```',1)[0]
        delta=''.join(difflib.unified_diff(old.splitlines(True),t.splitlines(True),fromfile='r6-reviewed/'+path,tofile='current/'+path,n=8))
        first=t.index("  it('")
        relevant=t.index("  it('requires getTemplate")
        after=t.index("  it('uses only Graph cursors.after")
        selected=t[:first]+'\n[Unchanged earlier raw-wire tests omitted; complete delta follows]\n'+t[relevant:after]+'\n[Unchanged later cursor/byte-cap tests omitted]\n});\n'
        source(path,selected+'\nComplete delta against frozen r6 package, including all additions/removals:\n'+delta, 'Full harness and complete getTemplate identity/Unicode, new 200+error list/get cases and adjacent contradictory debug-token cases; complete exact r6-to-current diff kept. Other unchanged grant/wire/category/cursor/stream-cap cases omitted as historical unchanged, retained in actual canonical unit execution. Frozen r6 package SHA256 '+sha(baseline_raw)+'; previous source SHA256 '+sha(old.encode())+'. This is an explicit delta-follow-up selection, not a claim that omitted test bodies are included.')
        continue
    if path=='api-app/test/number-onboarding-bci.e2e-spec.ts':
        import subprocess
        t=(ROOT/path).read_text();old=subprocess.check_output(['git.exe','-C','api-app','show','db5a86758a165fac8a1ab587599c37b17890530c:test/number-onboarding-bci.e2e-spec.ts']).decode().replace('\r\n','\n')
        source(path,''.join(difflib.unified_diff(old.splitlines(True),t.splitlines(True),fromfile='admitted-baseline',tofile='current',n=5)), 'Complete exact baseline delta only: approved listener startup fix. Unchanged inherited 5x20 body omitted; actual canonical all retains its results. Full-file digest and exact startup-only delta prevent unreported weakening.')
        continue
    if path=='api-app/prisma/schema.prisma':
        t=(ROOT/path).read_text(); wanted={'Mantenedora','Setor','SetorGrant','BusinessUnit','ChannelType','ChannelStatus','BuChannel','ChannelCredential','ProviderResourceIdentity','OrigemDoGrant','Role','AppUser','UserBuRole','ActivityLog','EscopoDaAtividade','CategoriaDeAtividade','EntidadeDaAtividade'}
        blocks=re.findall(r'(?ms)^(?:model|enum)\s+(\w+)\s*\{.*?^\}',t)
        selected=[]; template_start=None
        for match in re.finditer(r'(?ms)^(?:model|enum)\s+(\w+)\s*\{.*?^\}',t):
            if match[1].startswith('MessageTemplate'):
                if template_start is None: template_start=match.start()
            elif match[1] in wanted: selected.append(match[0])
        assert template_start is not None
        tail_start=t.rfind('\n}',0,template_start)+2
        source(path,'\n\n'.join(selected)+'\n'+t[tail_start:],'complete contiguous new-template tail including comments + existing tenant/identity/credential/user/audit entities; unrelated unchanged conversation/typebot/upload/public settings models omitted with full-file digest')
    else: source(path)
shared=json.loads((E/'inherited-shared-sources-v1.1.json').read_text())['records']
def elide_repeated_added_runs(delta, selected_source):
    lines=delta.splitlines(True); result=[]; i=0
    while i<len(lines):
        if lines[i].startswith('+') and not lines[i].startswith('+++'):
            end=i
            while end<len(lines) and lines[end].startswith('+') and not lines[end].startswith('+++'): end+=1
            added=''.join(line[1:] for line in lines[i:end])
            if end-i>40 and added.strip() in selected_source:
                result.append('[Repeated added block elided from this DELTA ONLY: '+str(end-i)+' lines; normalized-added-block SHA256 '+sha(added.encode())+'. Complete current block is included in the selected source section above; hunk coordinates remain unchanged.]\n')
            else: result.extend(lines[i:end])
            i=end
        else: result.append(lines[i]);i+=1
    return ''.join(result)
for r in shared:
    path=repo[r['repository']]+r['path'];now=(ROOT/path).read_text().replace('\r\n','\n');old=r['content_utf8'].replace('\r\n','\n')
    diff=''.join(difflib.unified_diff(old.splitlines(True),now.splitlines(True),fromfile='inherited/'+path,tofile='candidate/'+path,n=0))
    if path in selected_sources:
        diff=elide_repeated_added_runs(diff,selected_sources[path])
    add('Shared-source delta '+path, 'Inherited SHA256 '+r['sha256']+'; comparison normalizes CRLF in memory only. Long pure-added schema/template DTO blocks already present in full selected source may be referenced rather than duplicated; all removals and other changes remain explicit.\n```diff\n'+(diff or '(byte/normalized-content identical; inherited unchanged)\n')+'```')
for path in ['api-app/src/domain/channels/transport/channel.ts','api-app/src/integrations/channels/channel-transport.module.ts','api-app/src/domain/access/access.service.ts','api-app/src/domain/access/role.ts','api-app/src/domain/access/require-role.ts','api-app/src/surfaces/bff/session.middleware.ts','api-app/src/infra/session/session.service.ts','api-app/src/main.ts','api-app/src/domain/historico/registro.service.ts','api-app/package.json','web-app/package.json','web-app/playwright.config.ts','scripts/test-channels-local.sh','.github/workflows/ci.yml']:
    source(path)
for path in ['positive-node-manifest-readiness-v1.1.json','security-source-refresh-v1.1.json','executor-startup-secret-redaction-v1.1.json','root-browser-r7-counterexample-terminal-v1.1.json','root-candidate-r6-tqa-disposition-v1.1.json','root-candidate-r6-performance-security-disposition-v1.1.json','root-candidate-r6-adherence-how-disposition-v1.1.json','credential-containment-operator-confirmation-v1.1.json']:
    source(str((E/path).relative_to(ROOT)))
source(str((E/'inherited-working-tree-v1.1.json').relative_to(ROOT)))
j=(E/'root-cp04-peer-review-working.md').read_text(); idx=j.find('## R47');assert idx>=0;add('Current peer-review residuals and resolutions (not independent gate)','Earlier self-review and superseded failed-attempt narratives omitted. Process deviations/fail-first limits remain explicit above; current r6 dispositions and retained RED/terminal records are included separately. Current R47 onward retained. Historical r5 self-review disposition omitted (full SHA256 '+sha((E/'root-cp05-static-tqa-r5-disposition-v1.1.json').read_bytes())+'): it is not independent gate evidence. Its material EPS budget change100→150 followed actual50indexed lookups/150buffers; no planner forcing or query weakening is authorized. Current deep-query source/tests and actual all EPS plans below remain the evidence to judge. Full ledger SHA256 '+sha((E/'root-cp04-peer-review-working.md').read_bytes())+'\n'+j[idx:])
old_browser=E/'root-restored-browser-terminal-v1.1.json'
add('Historical receipt not expanded','r6 earlier restored-browser terminal is historical only, superseded by current actual all. Raw receipt SHA256 '+sha(old_browser.read_bytes())+'; no current result inferred from it. Retained r7 behavioral RED and current actual terminal remain explicit.')
add('Frozen candidate source inventory',json.dumps(freeze,ensure_ascii=False,separators=(',',':')))
if a.log:
    raw=(ROOT/a.log).read_bytes();t=raw.decode();markers=[]
    for label in ['MESSAGE-TEMPLATE-PCV','MESSAGE-TEMPLATE-EPS','TEMPLATE-RLS-EVIDENCE','TEMPLATE-FRC-EVIDENCE']:
        found=[line for line in t.splitlines() if '['+label+']' in line]
        if not a.size_only: assert found,'missing actual marker '+label
        for line in found:
            prefix,body=line.split('['+label+']',1)
            payload=json.loads(body)
            if label=='MESSAGE-TEMPLATE-EPS':
                zero_defaults={'Shared Read Blocks':0,'Shared Dirtied Blocks':0,'Shared Written Blocks':0,'Local Hit Blocks':0,'Local Read Blocks':0,'Local Dirtied Blocks':0,'Local Written Blocks':0,'Temp Read Blocks':0,'Temp Written Blocks':0}
                def encode_plan(value):
                    if isinstance(value,list): return [encode_plan(x) for x in value]
                    if not isinstance(value,dict): return value
                    out={k:encode_plan(v) for k,v in value.items()}
                    zero_keys=[k for k,v in zero_defaults.items() if k in out and out[k]==v]
                    if zero_keys:
                        out['$zeroCounters']=sum(1<<list(zero_defaults).index(k) for k in zero_keys)
                        for k in zero_keys: del out[k]
                    return out
                encoded=encode_plan(payload)
                def decode_plan(value):
                    if isinstance(value,list): return [decode_plan(x) for x in value]
                    if not isinstance(value,dict): return value
                    out={k:decode_plan(v) for k,v in value.items() if k!='$zeroCounters'}
                    mask=value.get('$zeroCounters',0)
                    for i,k in enumerate(zero_defaults):
                        if mask & (1<<i):
                            assert k not in out
                            out[k]=0
                    return out
                assert decode_plan(encoded)==payload, 'lossless EPS encoding roundtrip'
                payload={'lossless_encoding':'$zeroCounters is an integer bitmask. For every set bit i, restore zero_counter_keys[i] with numeric0, then remove $zeroCounters. Unset/absent keys are not added. All nonzero values, plan nodes, indexes, rows, loops, timing and scenario metrics retained.','zero_counter_keys':list(zero_defaults),'data':encoded}
            markers.append('['+label+']'+json.dumps(payload,ensure_ascii=False,separators=(',',':')))
    add('Canonical all actual terminal and structured markers','log '+a.log+' bytes '+str(len(raw))+' sha256 '+sha(raw)+'\n'+ '\n'.join(markers)+'\nTerminal tail:\n'+t[-3200:])
    assert a.source_proof and a.runtime_proof and a.receipt
    sr=json.loads((ROOT/a.source_proof).read_text()); ar=json.loads((ROOT/a.runtime_proof).read_text());rc=(ROOT/a.receipt).read_text()
    if not a.size_only: assert rc.strip()=='0',('all terminal not0',rc)
    actual={repo[rp]+r['path']:r['sha256'] for rp,key in [('api','apiChangedSources'),('web','webChangedSources')] for r in sr[key]}
    matches=[{'path':r['path'],'actual_attested_sha256':actual.get(r['path']),'matches':actual.get(r['path'])==r['sha256']} for r in records]
    if not a.size_only:
        assert all(r['matches'] for r in matches)
        assert ar['servedBundleSha256']==ar['distBundleSha256']
        assert sr['branches']['api']['head']=='db5a86758a165fac8a1ab587599c37b17890530c'
        assert sr['branches']['web']['head']=='74b9d4b714044829796f875d00553f077c1c329d'
    add('Actual all freshness and validation authority',json.dumps({'source_proof':a.source_proof,'source_proof_sha256':sha((ROOT/a.source_proof).read_bytes()),'source_capture_utc':sr['capturedAtUtc'],'actual_branches':sr['branches'],'runtime_proof':a.runtime_proof,'runtime_proof_sha256':sha((ROOT/a.runtime_proof).read_bytes()),'runtime_capture_utc':ar['capturedAtUtc'],'runtime':ar['runtime'],'database':ar['database'],'endpoints':ar['endpoints'],'servedBundleSha256':ar['servedBundleSha256'],'distBundleSha256':ar['distBundleSha256'],'operationalDataBoundary':ar['operationalDataBoundary'],'matches':[{'path':m['path'],'matches_frozen_sha256':m['matches']} for m in matches],'terminal_receipt':a.receipt,'receipt_sha256':sha((ROOT/a.receipt).read_bytes()),'receipt':rc},ensure_ascii=False,separators=(',',':')))
elif not a.size_only: raise AssertionError('Actual full terminal/freshness required before dispatch package')
add('Source inclusion/omission inventory',json.dumps(inventory,ensure_ascii=False,separators=(',',':')))
out='# ST-CON-05 v1.1 — candidate assurance package\n\nGenerated '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'; derived/non-authoritative; package must be judged with its full embedded applicable rubrics.\n'+''.join(sections)
print(json.dumps({'bytes':len(out.encode()),'characters':len(out),'sections':len(sections),'sha256':sha(out.encode()),'size_only':a.size_only}))
if a.size_only: print(json.dumps(sorted([{'title':x.splitlines()[1], 'bytes':len(x.encode())} for x in sections],key=lambda x:x['bytes'],reverse=True)[:20]))
if not a.size_only:
    assert len(out.encode())<1_040_000,'reserve dispatch overhead below1MiB; combined dispatch+round prompt separately checked'
    assert a.output;dest=ROOT/a.output
    with dest.open('x') as file: file.write(out)
