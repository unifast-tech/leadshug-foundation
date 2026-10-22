import argparse,datetime,difflib,hashlib,json,re
from pathlib import Path
R=Path('/mnt/c/unifast/leadshug/leadshug_now_docker')
B=R/'foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020'
E=B/'evidence';h=lambda x:hashlib.sha256(x).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--current-acceptance',required=True);p.add_argument('--freeze',required=True);p.add_argument('--log',required=True);p.add_argument('--receipt',required=True);p.add_argument('--source-proof',required=True);p.add_argument('--runtime-proof',required=True);p.add_argument('--red-evidence',action='append',required=True);p.add_argument('--root-how',required=True);p.add_argument('--static-tqa-json',required=True);p.add_argument('--static-tqa-raw',required=True);p.add_argument('--output',required=True);a=p.parse_args()
sections=[];inventory=[]
def add(title,s):sections.append('\n## '+title+'\n\n'+s.strip()+'\n')
def file(path,selection=None,note=None):
 raw=(R/path).read_bytes();s=raw.decode().replace('\r\n','\n') if selection is None else selection
 if selection is None and path.endswith('.json'):s=json.dumps(json.loads(s),ensure_ascii=False,separators=(',',':'))
 inventory.append({'path':path,'bytes':len(raw),'sha256':h(raw),'selection':note or 'full; newline normalization or JSON formatting only'})
 add(path+(' [selection declared]' if note else ''),'```text\n'+s.rstrip()+'\n```')
freeze=json.loads((R/a.freeze).read_text());prior=json.loads((E/'root-cp05-source-freeze-r35-common-failure-ownership-v1.1.json').read_text());old={x['path']:x for x in prior['records']}
assert all(x['path'].startswith(('api-app/src/','api-app/test/','api-app/prisma/','web-app/src/','web-app/e2e/')) for x in freeze['records'])
for x in freeze['records']:assert h((R/x['path']).read_bytes())==x['sha256'],x['path']
sealed=json.loads((E/'inherited-working-tree-v1.1.json').read_text());prefix={'root':'','api':'api-app/','web':'web-app/'}
for x in sealed['records']:
 if not x['active_mutation_admitted']:assert h((R/(prefix[x['repository']]+x['path'])).read_bytes())==x['sha256']
changed=[x for x in freeze['records'] if x['path'] not in old or x['sha256']!=old[x['path']]['sha256']]
assert changed,'Follow-up must have actual material delta'
allowed={'web-app/src/telas/Modelos.tsx','web-app/src/telas/Modelos.spec.ts','web-app/e2e/message-templates.spec.ts','api-app/test/message-template-management.e2e-spec.ts'}
assert all(x['path'] in allowed for x in changed),'Unexpected delta requires root admission, not silent packet growth'
add('Scope, authority and audit workload','Affected current-selected-owner follow-up after actual accepted r35 all797 and fresh round04 candidate TQA/performance/security/adherence. Exact r35-to-current source/diff inventories below; only the three admitted Web files and the sole test-local API session diagnostic case may differ. SEC-R35-01 and ADH-R35-01 require current editor ownership when an account-owned page completes after Novo or A-to-B selection. Root source/handler review and actual r36 pure causal RED precede correction. The existing two-slice reducer now owns nullable selected identity metadata; guarded current draft/operation commits set it even without a saved snapshot, clear/context/editor events erase it, and page adoption retains only the current selected same-ID highest observation in the existing individual slice before exact returned page membership/cursor. No request-time selected field in product actions/callers, extra ref/cache/framework/HTTP or backend/DTO/ACK/eligibility semantic change is authorized. Assess full changed code, all12 actual draft state commits, three causal targets, page-only selection and both new real-BFF browser sequences. Named pure action fixtures deliberately retain a stale A hint as structurally extra test input, while product action does not declare/read it; do not mistake that for shipped compatibility.\n\nOPS-R4-01 is explicitly accepted nonblocking conservative local availability debt under fresh source-aware contract opinion: delayed code-only failure may withdraw availability from newer passive success but preserves status/time/fence/resource/content and canonical CAS; explicit refresh recovers. It neither permits stale APPROVED promotion nor waives mandatory server/consumer fences. Carry the canonical backlog owner/follow-up without reopening unchanged failure semantics or expanding into new error metadata/automatic HTTP. SEC-R6-04 read-budget private-cohort restriction and TQA-ST05-03 original test-after/unknown process debt remain. Reported credential containment is accepted; no repeated confirmation/retest, no historical nonuse/text-retraction claim.\n\nPerform the FULL applicable lane workload under complete embedded rubrics. In overall_assessment include substantive structured sections, not merely a terse zero-finding verdict. TQA explicitly answers all five mandatory questions, provides exact owning commands/topology, capability/coverage/platform matrix with exclusions, fail-first limits, bypass/auth/fallback/DI token-scope-lifecycle/CI/source-served checks, EACH D01-D09/CR-01/02/AR-V11-01/02/03/CR-V11-01 decision evidence table, and uncertainty/gate readiness. Other lanes assess full applicable performance/elegance/structure/operational/security/adherence criteria. Material finding cards need concrete path:line, severity, impact, A/B/C choices/recommendation using allowed schema fields. Zero unresolved blocking findings is the close condition; no cosmetic loop, no arbitrary reduced workload or waiver. Prior unchanged accepted design/debt remains closed absent concrete new evidence.\n\nCurrent all/receipt/freeze/source-runtime/served proof and all5 template markers are required actual evidence below, not planned counts. r36 is pure Web RED only (build passed42/3 of45): current-B301 first semantic failure reached, later page-only branch not reached; clear-owner and restored-A separate assertions reached. Browser new selection cases were not run before source change; do not label them browser RED or retrofit original feature test-first. Earlier RED capture/oracle limits are carried by prior resolutions. Browser uses real session/CSRF/BFF/Prisma/disposable PostgreSQL with explicit deterministic external provider fixtures. Both template FRC markers come from actual browser main workflow, separate100 BFF and100 UI attempts. No fixture proves actual Meta compatibility/approval, preserved activation, external exactly-once, production capacity/SLO or hosted CI. Empty200 browser and browser ACK-conflict-race limits stay explicit unless actual evidence proves otherwise.\n\nCandidate assurance only. Bounded preserved local TEST metadata preflight/two additive migrations, source-bound API/Web activation, owned HTTPS/normal access, one assisted actual Meta draft-submit-once-status, canonical module consolidation and fresh final review remain mandatory. Delivery Pending. No recipient send/ST-CON-04, public admission/Railway, new credentials, product Git, private dotenv/local-files, worktrees/copies or live review reduction.')
for path in ['delphi-ai/skills/test-quality-audit/SKILL.md','delphi-ai/workflows/docker/independent-test-quality-audit-method.md','delphi-ai/workflows/docker/performance-concurrency-validation-method.md','delphi-ai/skills/endpoint-performance-scrutiny/SKILL.md','delphi-ai/skills/frontend-race-condition-validation/SKILL.md','delphi-ai/skills/backend-concurrency-idempotency-validation/SKILL.md','delphi-ai/skills/runtime-load-stress-validation/SKILL.md','delphi-ai/skills/security-adversarial-review/SKILL.md','delphi-ai/skills/audit-protocol-triple-review/SKILL.md','foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md','foundation_documentation/project_constitution.md'] :file(path)
packet=(B/'candidate-assurance-r35-followup-package-v1.1.md').read_bytes();assert h(packet)=='7243afcaa92fb818c6c320cd1d07dbfae1b6a5eccf4f6c1a5c9d2e2138b13ccb';text=packet.decode()
for x in changed:
 path=x['path'];now=(R/path).read_text().replace('\r\n','\n')
 if path=='api-app/test/message-template-management.e2e-spec.ts':
  admission=json.loads((E/'root-r40-api-session-diagnostics-admission-v1.1.json').read_text())
  anchor="  it('revalidates BFF session and current observation role before success and unavailable commits'"
  assert now.count(anchor)==1 and now.endswith('  }, 60_000);\n});\n')
  begin=now.index(anchor);before=now[:begin]+admission['original_test_source']+'});\n'
  assert h(before.encode())==old[path]['sha256']==admission['original_file_sha256'],'Reconstructed whole reviewed r35 API test must match original immutable hash'
  first=re.search(r'^  it\(',now,re.M).start();omitted=now[first:begin]
  assert omitted==before[first:begin]
  selection=now[:first]+'\n'+now[begin:]
  file(path,selection,'Complete imports/helpers/beforeAll/beforeEach/afterAll and the WHOLE sole changed final session-revalidation test, including every diagnostic and six401/admin403/snapshot/cleanup oracle. Unchanged intervening44tests omitted; raw unchanged-prefix SHA256 '+h(omitted.encode())+'. Whole baseline reconstructed via immutable original test and verified against r35 full-fileSHA. Full exact whole-file r35-to-current diff follows. No changed test body or changed production source is excerpted.')
 else:
  marker='\n## '+path+'\n';assert marker in text,path
  start=text.index(marker);end=text.find('\n## ',start+len(marker));sec=text[start:end if end!=-1 else None];before=sec.split('```text\n',1)[1].rsplit('```',1)[0]
  file(path)
 add('Exact r35-to-current delta '+path,'Previous frozen package SHA256 '+h(packet)+'; baseline current API test reconstruction or embedded prior source SHA256 '+h(before.encode())+'. Full current changed product source/changed test body is above.\n```diff\n'+''.join(difflib.unified_diff(before.splitlines(True),now.splitlines(True),fromfile='r35/'+path,tofile='current/'+path,n=6))+'```')
for path in ['api-app/src/domain/message-templates/template-observation.service.ts','web-app/src/api.ts','api-app/src/surfaces/bff/message-templates.controller.ts','api-app/src/domain/message-templates/template-management.ports.ts','api-app/src/integrations/message-templates/template-management.module.ts','api-app/src/integrations/message-templates/template-management.resolver.ts']:
 file(path)
for path in ['api-app/src/domain/message-templates/template-draft.service.ts','api-app/src/domain/message-templates/template-submission.service.ts']:
 if path not in {x['path'] for x in changed}:
  if path.endswith('template-submission.service.ts'):
   now=(R/path).read_text().replace('\r\n','\n')
   assert h((R/path).read_bytes())==old[path]['sha256'],'Producer-method selection is allowed only for byte-unchanged reviewed source'
   starts=list(re.finditer(r'^  (?:(?:private|public|protected) )?(?:async )?([A-Za-z]\w*)\(',now,re.M))
   wanted={'constructor','submitDraft','getOperation','reconcile','authorizeDraft','assertTxOwnerAdmin','projectOperation','assertBinding','assertSameContext'}
   found={m.group(1) for m in starts};assert wanted<=found
   pieces=[now[:starts[0].start()]];omitted=[];included=[]
   for i,m in enumerate(starts):
    stop=starts[i+1].start() if i+1<len(starts) else len(now)
    if m.group(1) in wanted:pieces.append(now[m.start():stop]);included.append(m.group(1))
    else:omitted.append(m.group(1))
   selection='\n'.join(pieces)
   file(path,selection,'Unchanged r35 producer: full imports/type declarations and whole methods '+', '.join(included)+'. Omitted unchanged methods: '+', '.join(omitted)+'. These are declared excerpts, not an executable module. Full-file SHA256 matches the reviewed r35 freeze; late-ACK design and existing assurance are carried separately. Full changed product source is never excerpted.')
  else:file(path)
for name in ['root-cp05-all-r35-acceptance-v1.1.json', 'root-candidate-r35-preliminary-disposition-v1.1.json', 'root-r36-current-selection-evidence-plan-v1.1.json', 'root-r24-audit-floor-v1.1.json', 'root-candidate-r6-adherence-how-disposition-v1.1.json', 'root-candidate-r6-performance-security-disposition-v1.1.json', 'credential-containment-operator-confirmation-v1.1.json']:file(str((E/name).relative_to(R)))
for path in [a.root_how,a.static_tqa_json,a.static_tqa_raw]:file(path)
for name in ['root-template-frc-marker-attribution-clarification-v1.1.json','observation-owner-how-r31.raw-attempt1.txt','root-r33-observation-owner-how-admission-v1.1.json','root-r34-recovery-evidence-plan-v1.1.json','root-r34-capture-recovery-admission-v1.1.json']:file(str((E/name).relative_to(R)))
for path in ['candidate-audit-r6/round-04/results/performance.result.json','candidate-audit-r6/round-04/results/test-quality.result.json','evidence/candidate-r35-security.raw-attempt1.txt','evidence/candidate-r35-adherence.raw-attempt1.txt','candidate-audit-r6/round-01/resolution.md','candidate-audit-r6/round-02/resolution.md','candidate-audit-r6/round-03/resolution.md','candidate-audit-r6/round-04/resolution.md','evidence/candidate-r35-test-quality-complete.raw-attempt1.txt','evidence/root-failed-observation-authority-r35-disposition-v1.1.json','evidence/failed-observation-authority-how-r35.raw-attempt1.txt','evidence/root-r36-provenance-and-executor-reset-v1.1.json']:
 file(str((B/path).relative_to(R)))
for path in ['api-app/src/infra/session/session.service.ts','api-app/src/surfaces/bff/session.middleware.ts']:
 file(path)
login_source=(R/'api-app/test/helpers.ts').read_text().replace('\r\n','\n');login_start=login_source.index('export async function login(');login_end=login_source.index('\n}',login_start)+2
file('api-app/test/helpers.ts',login_source[login_start:login_end],'Whole unchanged actual login helper only; fixture setup and imports are in changed-test selection. Full-fileSHA recorded, all other helper bodies omitted unchanged since r35.')
for name in ['root-cp05-api-r40-diagnostic-acceptance-v1.1.json','root-r40-diagnostic-how-disposition-v1.1.json','session-timeout-how-r39.raw-attempt1.txt','root-r40-diagnostic-static-review-v1.1.json']:
 file(str((E/name).relative_to(R)))
add('Additional affected test diagnostics and evidence limits','Only fourth admitted changed file is the final API session test. All production API sources and other44 cases are byte-unchanged since reviewed r35; whole current changed test+harness and exact diff are included. Opaque r39 API60s timeout had no phase trace and is NOT attributed or called flaky. Diagnostic-only r40 realAPI/PG passed682, with7 actual provider entries, six401/admin403,8unchanged observation snapshots and genuine cleanup. Tagged native10s provider-entry-vs-realHTTP guard fails earlier on earlyresponse/rejection/deadline; it neither fabricates entry nor cancels requests or advances clocks. Date.now remains expired through actual response settlement; all security oracles and overall60s remain. Current full all still controls candidate acceptance. Do not infer original cause from a passing subsequent run or waive test gates. Assess actual current TQA/security/PCV/adherence readiness with these limits; source-aware HOW was diagnostic-only, not a substitute candidate/final review.')
file('foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/local-activation-plan-v1.1.md')
for path in a.red_evidence:
 o=json.loads((R/path).read_text());file(path)
 for k in ['log','log_path']:
  if k in o:
   rp=R/o[k];assert rp.is_file()
   expected=o.get('log_sha256');assert expected and h(rp.read_bytes())==expected
 if 'capture_provenance' in o:
  cp=R/o['capture_provenance'];assert h(cp.read_bytes())==o['capture_provenance_sha256']
  file(o['capture_provenance'])
raw=(R/a.log).read_bytes();s=raw.decode();assert (R/a.receipt).read_text().strip()=='0'
accepted=json.loads((R/a.current_acceptance).read_text());assert accepted['log']==a.log and accepted['log_sha256']==h(raw) and accepted['receipt']==a.receipt and accepted['exit']==0
assert accepted['freeze']==a.freeze and accepted['freeze_sha256']==h((R/a.freeze).read_bytes())
file(a.current_acceptance)
sr=json.loads((R/a.source_proof).read_text());ar=json.loads((R/a.runtime_proof).read_text());actual={prefix[rp]+r['path']:r['sha256'] for rp,key in [('api','apiChangedSources'),('web','webChangedSources')] for r in sr[key]}
assert all(actual.get(x['path'])==x['sha256'] for x in freeze['records']);assert ar['servedBundleSha256']==ar['distBundleSha256']
assert sr['branches']['api']['head']=='db5a86758a165fac8a1ab587599c37b17890530c'
assert sr['branches']['web']['head']=='74b9d4b714044829796f875d00553f077c1c329d'
markers=[]
for label in ['MESSAGE-TEMPLATE-PCV','MESSAGE-TEMPLATE-EPS','TEMPLATE-RLS-EVIDENCE','TEMPLATE-FRC-EVIDENCE','TEMPLATE-FRC-UI-EVIDENCE']:
 lines=[line for line in s.splitlines() if '['+label+']' in line];assert lines,label
 for line in lines:markers.append('['+label+']'+json.dumps(json.loads(line.split('['+label+']',1)[1]),ensure_ascii=False,separators=(',',':')))
add('Current actual canonical all and complete structured markers',json.dumps({'log':a.log,'bytes':len(raw),'sha256':h(raw),'receipt':a.receipt,'receipt_sha256':h((R/a.receipt).read_bytes()),'exit':0})+'\n'+'\n'.join(markers)+'\nTerminal:\n'+s[-4000:])
add('Current actual source/runtime attribution',json.dumps({'source_proof':a.source_proof,'source_proof_sha256':h((R/a.source_proof).read_bytes()),'source_capture':sr['capturedAtUtc'],'runtime_proof':a.runtime_proof,'runtime_proof_sha256':h((R/a.runtime_proof).read_bytes()),'runtime_capture':ar['capturedAtUtc'],'heads':sr['branches'],'runtime':ar['runtime'],'database':ar['database'],'endpoints':ar['endpoints'],'servedBundleSha256':ar['servedBundleSha256'],'distBundleSha256':ar['distBundleSha256'],'source_matches':len(freeze['records']),'changed_paths':[x['path'] for x in changed],'unchanged_since_r35':[x['path'] for x in freeze['records'] if x not in changed]},ensure_ascii=False,separators=(',',':')))
file(a.freeze);add('Inclusion/omission inventory',json.dumps(inventory,ensure_ascii=False,separators=(',',':')))
out='# ST-CON-05 v1.1 — affected candidate follow-up\n\nGenerated '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'; derived, non-authoritative.\n'+''.join(sections);raw=out.encode();assert len(raw)<1_000_000
with (R/a.output).open('x') as f:f.write(out)
print(json.dumps({'bytes':len(raw),'sha256':h(raw),'changed_paths':[x['path'] for x in changed]}))
