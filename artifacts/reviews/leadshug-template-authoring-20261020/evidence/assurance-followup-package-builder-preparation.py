import argparse,datetime,difflib,hashlib,json,re
from pathlib import Path
R=Path('/mnt/c/unifast/leadshug/leadshug_now_docker')
B=R/'foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020'
E=B/'evidence';h=lambda x:hashlib.sha256(x).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--freeze',required=True);p.add_argument('--log',required=True);p.add_argument('--receipt',required=True);p.add_argument('--source-proof',required=True);p.add_argument('--runtime-proof',required=True);p.add_argument('--red-evidence',action='append',required=True);p.add_argument('--output',required=True);a=p.parse_args()
sections=[];inventory=[]
def add(title,s):sections.append('\n## '+title+'\n\n'+s.strip()+'\n')
def file(path,selection=None,note=None):
 raw=(R/path).read_bytes();s=raw.decode().replace('\r\n','\n') if selection is None else selection
 if selection is None and path.endswith('.json'):s=json.dumps(json.loads(s),ensure_ascii=False,separators=(',',':'))
 inventory.append({'path':path,'bytes':len(raw),'sha256':h(raw),'selection':note or 'full; newline normalization or JSON formatting only'})
 add(path+(' [selection declared]' if note else ''),'```text\n'+s.rstrip()+'\n```')
freeze=json.loads((R/a.freeze).read_text());prior=json.loads((E/'root-cp05-source-freeze-r13-browser-oracle-corrections-v1.1.json').read_text());old={x['path']:x for x in prior['records']}
assert all(x['path'].startswith(('api-app/src/','api-app/test/','api-app/prisma/','web-app/src/','web-app/e2e/')) for x in freeze['records'])
for x in freeze['records']:assert h((R/x['path']).read_bytes())==x['sha256'],x['path']
sealed=json.loads((E/'inherited-working-tree-v1.1.json').read_text());prefix={'root':'','api':'api-app/','web':'web-app/'}
for x in sealed['records']:
 if not x['active_mutation_admitted']:assert h((R/(prefix[x['repository']]+x['path'])).read_bytes())==x['sha256']
changed=[x for x in freeze['records'] if x['path'] not in old or x['sha256']!=old[x['path']]['sha256']]
assert changed,'Follow-up must have actual material delta'
allowed={'web-app/src/telas/Modelos.tsx','web-app/e2e/message-templates.spec.ts','api-app/src/domain/message-templates/template-observation.service.ts','api-app/src/domain/message-templates/template-draft.service.ts','api-app/src/domain/message-templates/template-submission.service.ts','api-app/test/message-template-management.e2e-spec.ts','api-app/test/message-template-bff.e2e-spec.ts'}
assert all(x['path'] in allowed for x in changed),'Unexpected delta requires root admission, not silent packet growth'
add('Scope, authority and audit workload','''Derived delta-follow-up for approved ST-CON-05 v1.1. Current full source/test delta and actual validation are supplied below. This is candidate assurance before preserved local TEST migrations, source-bound API/Web activation and one assisted actual Meta template submission/status. Final fresh review after those actual proofs is still required; delivery remains Pending. No recipient send/ST-CON-04, no production/Railway, no new credential mode, no product commit/push, no private dotenv/local-files access, no worktree/copy.

The prior r13 all770 and four independent reviews assessed the full implementation. This follow-up is intentionally bounded to their four root-confirmed corrections: stale automatic recovery observation crossing editor/context; successful refresh leader discarded after blocked202 triggers; current observation lost after same-account reauthorization; missing observation time in status/catalogue. All other source hashes remain explicitly compared below. Late ACK HOW, immutable associations and original one-POST semantics stay unchanged. The separate ACK-conflict consumer test is pure function evidence plus real-PG producer tests, not a browser conflict race. Historical test-after/unknown provenance is not retroactively relabeled. Compiler/fixture failures are not behavioral RED.

Perform the FULL applicable lane workload under the complete embedded rubrics, including current delta, nearby integration seams and prior resolution checks. For TQA, overall_assessment must explicitly contain audit framing; test-first/after/unknown and exact RED limits; bypass/fallback/DI/real-boundary checks; CI/command/topology/source-served/platform matrix; assertion efficacy/efficiency; failure/uncertainty; a D01-D09, CR-01/02, AR-V11-01/02/03 and CR-V11-01 adherence table with evidence; and each of the five mandatory test-method answers. Do not substitute five answers for the full rubric. Issue cards need severity, concrete path/line, impact, A/B/C options and recommendation. Other lanes assess their complete applicable criteria. Do not reopen accepted debt or unaffected loci without concrete new evidence. No gate waiver, no live reviewer reduction and no tools/edit permission are implied.

Provider calls in automated evidence are external deterministic network fixtures with real session/CSRF/BFF/Prisma/PostgreSQL. Actual Meta proof remains a later explicit gate. No capacity/SLO/external exactly-once/approval guarantee is claimed. Operator confirmed the exposed connector credential revoked or disabled; this establishes reported containment, not prior-use audit or retraction of rendered text. No new confirmation or secret retest is needed. Sequential recovery read budget remains the canonical private-local-cohort-only debt, separately approved before untrusted/public admission or Railway.''')
for path in ['delphi-ai/skills/test-quality-audit/SKILL.md','delphi-ai/workflows/docker/independent-test-quality-audit-method.md','delphi-ai/workflows/docker/performance-concurrency-validation-method.md','delphi-ai/skills/security-adversarial-review/SKILL.md','delphi-ai/skills/audit-protocol-triple-review/SKILL.md','foundation_documentation/todos/active/features/TODO-leadshug-official-template-authoring.md','foundation_documentation/project_constitution.md'] :file(path)
packet=(B/'candidate-assurance-r13-baseline-b-package-v1.1.md').read_bytes();assert h(packet)=='45399bab6500d70e0132671cc397c19a475b9c13e8357dfbd45c4bebddcd1c64';text=packet.decode()
for x in changed:
 path=x['path'];file(path);marker='\n## '+path+'\n';assert marker in text,path
 start=text.index(marker);end=text.find('\n## ',start+len(marker));sec=text[start:end if end!=-1 else None];before=sec.split('```text\n',1)[1].rsplit('```',1)[0];now=(R/path).read_text().replace('\r\n','\n')
 add('Exact r13-to-current delta '+path,'Previous frozen package SHA256 '+h(packet)+'; normalized embedded prior section SHA256 '+h(before.encode())+'. Full current file is above.\n```diff\n'+''.join(difflib.unified_diff(before.splitlines(True),now.splitlines(True),fromfile='r13/'+path,tofile='current/'+path,n=6))+'```')
for path in ['api-app/src/surfaces/bff/message-templates.controller.ts','api-app/src/domain/message-templates/template-management.ports.ts','api-app/src/integrations/message-templates/template-management.module.ts','api-app/src/integrations/message-templates/template-management.resolver.ts']:
 file(path)
for name in ['root-cp05-all-r13-acceptance-v1.1.json','root-candidate-r13-disposition-v1.1.json','root-candidate-r6-adherence-how-disposition-v1.1.json','root-candidate-r6-performance-security-disposition-v1.1.json','credential-containment-operator-confirmation-v1.1.json'] :file(str((E/name).relative_to(R)))
for path in ['candidate-audit-r6/round-02/results/performance.result.json','candidate-audit-r6/round-02/results/test-quality.result.json','evidence/candidate-r13-security.raw-attempt1.txt','evidence/candidate-r13-adherence.raw-attempt1.txt','candidate-audit-r6/round-01/resolution.md','candidate-audit-r6/round-02/resolution.md']:
 file(str((B/path).relative_to(R)))
file('foundation_documentation/artifacts/reviews/leadshug-template-authoring-20261020/local-activation-plan-v1.1.md')
for path in a.red_evidence:
 o=json.loads((R/path).read_text());file(path)
 for k in ['log','log_path']:
  if k in o:
   rp=R/o[k];assert rp.is_file()
   expected=o.get('log_sha256');assert expected and h(rp.read_bytes())==expected
raw=(R/a.log).read_bytes();s=raw.decode();assert (R/a.receipt).read_text().strip()=='0'
sr=json.loads((R/a.source_proof).read_text());ar=json.loads((R/a.runtime_proof).read_text());actual={prefix[rp]+r['path']:r['sha256'] for rp,key in [('api','apiChangedSources'),('web','webChangedSources')] for r in sr[key]}
assert all(actual.get(x['path'])==x['sha256'] for x in freeze['records']);assert ar['servedBundleSha256']==ar['distBundleSha256']
assert sr['branches']['api']['head']=='db5a86758a165fac8a1ab587599c37b17890530c'
assert sr['branches']['web']['head']=='74b9d4b714044829796f875d00553f077c1c329d'
markers=[]
for label in ['MESSAGE-TEMPLATE-PCV','MESSAGE-TEMPLATE-EPS','TEMPLATE-RLS-EVIDENCE','TEMPLATE-FRC-EVIDENCE']:
 lines=[line for line in s.splitlines() if '['+label+']' in line];assert lines,label
 for line in lines:markers.append('['+label+']'+json.dumps(json.loads(line.split('['+label+']',1)[1]),ensure_ascii=False,separators=(',',':')))
add('Current actual canonical all and complete structured markers',json.dumps({'log':a.log,'bytes':len(raw),'sha256':h(raw),'receipt':a.receipt,'receipt_sha256':h((R/a.receipt).read_bytes()),'exit':0})+'\n'+'\n'.join(markers)+'\nTerminal:\n'+s[-4000:])
add('Current actual source/runtime attribution',json.dumps({'source_proof':a.source_proof,'source_proof_sha256':h((R/a.source_proof).read_bytes()),'source_capture':sr['capturedAtUtc'],'runtime_proof':a.runtime_proof,'runtime_proof_sha256':h((R/a.runtime_proof).read_bytes()),'runtime_capture':ar['capturedAtUtc'],'heads':sr['branches'],'runtime':ar['runtime'],'database':ar['database'],'endpoints':ar['endpoints'],'servedBundleSha256':ar['servedBundleSha256'],'distBundleSha256':ar['distBundleSha256'],'source_matches':len(freeze['records']),'changed_paths':[x['path'] for x in changed],'unchanged_since_r13':[x['path'] for x in freeze['records'] if x not in changed]},ensure_ascii=False,separators=(',',':')))
file(a.freeze);add('Inclusion/omission inventory',json.dumps(inventory,ensure_ascii=False,separators=(',',':')))
out='# ST-CON-05 v1.1 — affected candidate follow-up\n\nGenerated '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'; derived, non-authoritative.\n'+''.join(sections);raw=out.encode();assert len(raw)<1_000_000
with (R/a.output).open('x') as f:f.write(out)
print(json.dumps({'bytes':len(raw),'sha256':h(raw),'changed_paths':[x['path'] for x in changed]}))
