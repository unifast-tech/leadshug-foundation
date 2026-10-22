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
freeze=json.loads((R/a.freeze).read_text());prior=json.loads((E/'root-cp05-source-freeze-r30-scoped-eligibility-v1.1.json').read_text());old={x['path']:x for x in prior['records']}
assert all(x['path'].startswith(('api-app/src/','api-app/test/','api-app/prisma/','web-app/src/','web-app/e2e/')) for x in freeze['records'])
for x in freeze['records']:assert h((R/x['path']).read_bytes())==x['sha256'],x['path']
sealed=json.loads((E/'inherited-working-tree-v1.1.json').read_text());prefix={'root':'','api':'api-app/','web':'web-app/'}
for x in sealed['records']:
 if not x['active_mutation_admitted']:assert h((R/(prefix[x['repository']]+x['path'])).read_bytes())==x['sha256']
changed=[x for x in freeze['records'] if x['path'] not in old or x['sha256']!=old[x['path']]['sha256']]
assert changed,'Follow-up must have actual material delta'
allowed={'web-app/src/telas/Modelos.tsx','web-app/src/telas/Modelos.spec.ts','web-app/e2e/message-templates.spec.ts'}
assert all(x['path'] in allowed for x in changed),'Unexpected delta requires root admission, not silent packet growth'
add('Scope, authority and audit workload','Affected delta-follow-up after accepted r30 all789 and four fresh reviews. All unchanged source hashes are compared against the r30 freeze. Candidate assurance only: preserved local TEST preflight/migrations, source-bound API/Web activation, actual assisted Meta submission/status and fresh final review remain separate mandatory gates; delivery Pending. No recipient send/ST-CON-04, public admission/Railway, new credentials, product Git writes, private dotenv/local-files reads, worktrees or copies.\n\nThree bounded consumer corrections must address the prior findings: (1) common observation eligibility versus draft definition/ACK proof at equal fences; (2) historical classification retained through failure after same-account reauthorization and lower-fence current success; (3) monotonic currently known resource observations when a passive higher-fence read precedes an older admitted explicit result, for BOTH individual and catalogue producer directions. Meaningful completed intent and persisted-fence authority are separate. The local two-slice reducer is admitted only for atomic selection and retained editor observation when a first-page response omits its resource; page membership remains exact. Later r33 recovery regression and r34 causal RED concern a draft-only use veto introduced into common failure facts. Current source must separate those scopes without suppressing real common unavailability or weakening editor proof; inspect the full transition tests and actual recovered response fields. The r34 capture is explicitly partial with recovered process exit, never first-byte canonical stdout; the mandatory current all remains complete. Current code, complete exact r30-to-current diffs, actual RED terminal limits and current GREEN markers are supplied; do not infer new behaviors from historical green outcomes. Old ACK/provider/backend contracts remain byte-unchanged unless the explicit inventory says otherwise. No frontend backend-eligibility recomputation, generic safeCode veto, arbitrary OR or extra HTTP/cache is authorized. Scope/shape of the pure test helper may change only for documented ownership semantics while preserving common/editor behavior and all negative gates; scrutinize this as a possible pass-the-test risk.\n\nPerform the FULL applicable lane workload under complete embedded rubrics. TQA must explicitly cover big cross-stack framing, original test-after/unknown versus actual later bugfix RED limits, bypass/auth/fallback/DI/real-boundary checks, owning commands/CI/topology/source-served/platform, semantic assertion efficacy and efficiency, failure/uncertainty, every D01-D09/CR-01/02/AR-V11-01/02/03/CR-V11-01 mapping and all five mandatory answers. Other lanes assess their full applicable criteria. Findings require concrete path/line, severity, impact, A/B/C choices and recommendation. No live review reduction or gate waiver. Do not reopen unchanged accepted design/debt without concrete new evidence.\n\nBrowser uses real BFF/session/CSRF/Prisma/PostgreSQL with deterministic external provider network fixtures. API cases use explicit typed-port or fetch doubles for provider effects with real PostgreSQL and applicable HTTP boundary. Both TEMPLATE-FRC markers are emitted by the browser main journey (100 actual BFF lease requests and separate5x20 UI attempts); inherited inbox FRC-COMPOSER cannot substitute. No actual Meta compatibility, approval, capacity/SLO or external exactly-once guarantee. Empty200 browser and browser ACK-conflict-race coverage remain explicit limits unless actual current evidence proves otherwise. Operator confirmed credential revoked/disabled; no repeat confirmation or secret retest, no historical-nonuse/text-retraction claim. Existing SEC-R6-04 recovery-read-budget debt remains private-local-cohort-only before separately approved untrusted/public/Railway admission. Prior round resolutions and reviews follow; root dispositions are advisory until assessed against current code/evidence.')
for path in ['delphi-ai/skills/test-quality-audit/SKILL.md','delphi-ai/workflows/docker/independent-test-quality-audit-method.md','delphi-ai/workflows/docker/performance-concurrency-validation-method.md','delphi-ai/skills/endpoint-performance-scrutiny/SKILL.md','delphi-ai/skills/frontend-race-condition-validation/SKILL.md','delphi-ai/skills/backend-concurrency-idempotency-validation/SKILL.md','delphi-ai/skills/runtime-load-stress-validation/SKILL.md','delphi-ai/skills/security-adversarial-review/SKILL.md','delphi-ai/skills/audit-protocol-triple-review/SKILL.md','foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md','foundation_documentation/project_constitution.md'] :file(path)
packet=(B/'candidate-assurance-r30-followup-package-v1.1.md').read_bytes();assert h(packet)=='89fd5689d7c7ada356f7860c2a3f063e3d8037a47ba1b22c2c39f10ce50bfa68';text=packet.decode()
for x in changed:
 path=x['path'];marker='\n## '+path+'\n';assert marker in text,path
 start=text.index(marker);end=text.find('\n## ',start+len(marker));sec=text[start:end if end!=-1 else None];before=sec.split('```text\n',1)[1].rsplit('```',1)[0];now=(R/path).read_text().replace('\r\n','\n')
 if path=='api-app/test/message-template-management.e2e-spec.ts':
  sentinel="  it('keeps a post-dispatch timeout ambiguous and same-key replay performs no second POST'"
  assert now.count(sentinel)==1 and before.count(sentinel)==1
  tail=now[now.index(sentinel):];prior_tail=before[before.index(sentinel):]
  assert tail.rstrip()==prior_tail.rstrip(),'Omitted integration-test suffix must be unchanged since reviewed r30'
  selected=now[:now.index(sentinel)]
  file(path,selected,'Full imports, PostgreSQL setup and every complete test before the post-dispatch-timeout case; includes the complete new current-generation case and adjacent projector/context tests. Remaining suffix unchanged from reviewed r30, normalized SHA256 '+h(tail.rstrip().encode())+'. Complete exact diff follows; full-file hash recorded.')
 else:file(path)
 add('Exact r30-to-current delta '+path,'Previous frozen package SHA256 '+h(packet)+'; normalized embedded prior section SHA256 '+h(before.encode())+'. Full current product source or explicitly declared whole-test selection is above.\n```diff\n'+''.join(difflib.unified_diff(before.splitlines(True),now.splitlines(True),fromfile='r30/'+path,tofile='current/'+path,n=6))+'```')
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
   file(path,selection,'Unchanged r30 producer: full imports/type declarations and whole methods '+', '.join(included)+'. Omitted unchanged methods: '+', '.join(omitted)+'. These are declared excerpts, not an executable module. Full-file SHA256 matches the reviewed r30 freeze; late-ACK design and existing assurance are carried separately. Full changed product source is never excerpted.')
  else:file(path)
for name in ['root-cp05-all-r30-acceptance-v1.1.json', 'root-candidate-r30-disposition-v1.1.json', 'root-r30-new-ordering-evidence-plan-v1.1.json', 'root-r24-audit-floor-v1.1.json', 'root-candidate-r6-adherence-how-disposition-v1.1.json', 'root-candidate-r6-performance-security-disposition-v1.1.json', 'credential-containment-operator-confirmation-v1.1.json']:file(str((E/name).relative_to(R)))
for path in [a.root_how,a.static_tqa_json,a.static_tqa_raw]:file(path)
for name in ['root-template-frc-marker-attribution-clarification-v1.1.json','observation-owner-how-r31.raw-attempt1.txt','root-r33-observation-owner-how-admission-v1.1.json','root-r34-recovery-evidence-plan-v1.1.json','root-r34-capture-recovery-admission-v1.1.json']:file(str((E/name).relative_to(R)))
for path in ['candidate-audit-r6/round-03/results/performance.result.json','candidate-audit-r6/round-03/results/test-quality.result.json','evidence/candidate-r30-security.raw-attempt1.txt','evidence/candidate-r30-adherence.raw-attempt1.txt','candidate-audit-r6/round-01/resolution.md','candidate-audit-r6/round-02/resolution.md','candidate-audit-r6/round-03/resolution.md']:
 file(str((B/path).relative_to(R)))
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
add('Current actual source/runtime attribution',json.dumps({'source_proof':a.source_proof,'source_proof_sha256':h((R/a.source_proof).read_bytes()),'source_capture':sr['capturedAtUtc'],'runtime_proof':a.runtime_proof,'runtime_proof_sha256':h((R/a.runtime_proof).read_bytes()),'runtime_capture':ar['capturedAtUtc'],'heads':sr['branches'],'runtime':ar['runtime'],'database':ar['database'],'endpoints':ar['endpoints'],'servedBundleSha256':ar['servedBundleSha256'],'distBundleSha256':ar['distBundleSha256'],'source_matches':len(freeze['records']),'changed_paths':[x['path'] for x in changed],'unchanged_since_r30':[x['path'] for x in freeze['records'] if x not in changed]},ensure_ascii=False,separators=(',',':')))
file(a.freeze);add('Inclusion/omission inventory',json.dumps(inventory,ensure_ascii=False,separators=(',',':')))
out='# ST-CON-05 v1.1 — affected candidate follow-up\n\nGenerated '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'; derived, non-authoritative.\n'+''.join(sections);raw=out.encode();assert len(raw)<1_000_000
with (R/a.output).open('x') as f:f.write(out)
print(json.dumps({'bytes':len(raw),'sha256':h(raw),'changed_paths':[x['path'] for x in changed]}))
