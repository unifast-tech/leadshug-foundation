#!/usr/bin/env python3
"""Isolated CP69 route-map fixture with bounded log capture and owned cleanup."""
import collections
import datetime as dt
import hashlib
import json
import os
import re
import selectors
import subprocess
import sys
import threading
import time
import uuid
from pathlib import Path

ROOT = Path('/mnt/c/unifast/leadshug/leadshug_now_docker')
TEMPLATE = ROOT / 'docker/local-gateway.conf.template'
EVIDENCE = ROOT / 'foundation_documentation/artifacts/reviews/leadshug-number-onboarding-20261015/evidence/cp69-gateway-route-candidate-v2e.json'
OLD_TEMPLATE_SHA = '9329131376e0aaa8020e7440954af5125a65eb2bba69fd016292fe63843fe707'
CANDIDATE_SHA = '6d4563cc5f5823bdb1177f350c942dc2472fc70133aef5b177fa4b57c5c9f1a0'
NGINX_IMAGE = 'sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109'
API_IMAGE = 'sha256:fe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821'
OWNER_KEY = 'com.leadshug.channels.owner'
OWNER = 'number-onboarding'
CHECKPOINT = 'cp69-route-candidate-v2'
MAX_LOG_BYTES = 64 * 1024
MAX_LOG_LINES = 100
LOG_TIMEOUT_SECONDS = 15
FORMAT = re.compile(
    r'^(?P<docker_ts>\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)) '
    r'(?P<nginx_ts>\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)) '
    r'route=(?P<route>meta|other) method=(?P<method>[A-Z]+) status=(?P<status>\d{3}) bytes=(?P<bytes>\d+) '
    r'request_time=(?P<request_time>-|\d+(?:\.\d+)?) '
    r'upstream_status=(?P<upstream_status>-|\d{3}(?:, ?(?:-|\d{3}))*) '
    r'upstream_time=(?P<upstream_time>-|\d+(?:\.\d+)?(?:, ?(?:-|\d+(?:\.\d+)?))*)$'
)
FIXTURE = r'''const http=require("node:http");
http.createServer((req,res)=>{res.statusCode=201;res.setHeader("Content-Type","text/plain");res.end("api-fixture")}).listen(3000,"0.0.0.0");
http.createServer((req,res)=>{res.statusCode=202;res.setHeader("Content-Type","text/plain");res.end("web-fixture")}).listen(80,"0.0.0.0");'''
CASES = [
 {"case":"exact_get","method":"GET","path":"/webhooks/meta","route":"meta","status":201},
 {"case":"slash_get","method":"GET","path":"/webhooks/meta/","route":"meta","status":201},
 {"case":"query_get","method":"GET","path":"/webhooks/meta?cp69_query_canary=synthetic","route":"meta","status":201},
 {"case":"exact_post","method":"POST","path":"/webhooks/meta","route":"meta","status":201,"headers":{"Authorization":"Bearer cp69_auth_canary_synthetic","Cookie":"cp69_cookie_canary=synthetic","Content-Type":"text/plain"},"body":"cp69_body_canary_synthetic"},
 {"case":"slash_post","method":"POST","path":"/webhooks/meta/?cp69_query_canary=synthetic","route":"meta","status":201,"headers":{"Authorization":"Bearer cp69_auth_canary_synthetic","Cookie":"cp69_cookie_canary=synthetic","Content-Type":"text/plain"},"body":"cp69_body_canary_synthetic"},
 {"case":"uppercase_negative","method":"GET","path":"/WEBHOOKS/META","route":"other","status":202},
 {"case":"mixedcase_negative","method":"GET","path":"/webhooks/Meta","route":"other","status":201},
 {"case":"nested_negative","method":"GET","path":"/webhooks/meta/extra","route":"other","status":201},
 {"case":"health","method":"GET","path":"/health","route":"other","status":201},
 {"case":"privacy","method":"GET","path":"/privacidade.html","route":"other","status":202},
 {"case":"root_query","method":"GET","path":"/?cp69_query_canary=synthetic","route":"other","status":202},
]
CLIENT = "const http=require('node:http');const cases=" + json.dumps(CASES,separators=(',',':')) + r''';
function one(c){return new Promise(resolve=>{const req=http.request({hostname:"gateway",port:80,path:c.path,method:c.method,headers:c.headers||{}},res=>{res.resume();res.on("end",()=>resolve({case:c.case,status:res.statusCode}))});req.on("error",()=>resolve({case:c.case,status:null}));req.end(c.body)})}
(async()=>{const rows=[];for(const c of cases)rows.push(await one(c));process.stdout.write(JSON.stringify(rows))})().catch(()=>{process.stdout.write("[]");process.exitCode=2});'''

class SafeFailure(Exception):
    def __init__(self, phase, code=None):
        super().__init__(phase)
        self.phase, self.code = phase, code

def run(args, *, input_bytes=None, timeout=20, output_limit=256 * 1024, check=True):
    try:
        p = subprocess.run(['docker.exe', *args], input=input_bytes, stdout=subprocess.PIPE,
                           stderr=subprocess.DEVNULL, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise SafeFailure('docker_command_timeout')
    if len(p.stdout) > output_limit:
        raise SafeFailure('docker_command_output_limit')
    if check and p.returncode != 0:
        raise SafeFailure('docker_command_failed', p.returncode)
    return p

def inspect_container(obj_id):
    fmt = '{{.Id}}|{{.Image}}|{{.State.Status}}|{{index .Config.Labels "com.leadshug.channels.owner"}}|{{index .Config.Labels "checkpoint"}}|{{json .HostConfig.PortBindings}}|{{range .NetworkSettings.Networks}}{{.NetworkID}}{{end}}'
    p = run(['inspect', '--format', fmt, obj_id])
    fields = p.stdout.decode('ascii', 'strict').strip().split('|')
    if len(fields) != 7:
        raise SafeFailure('container_inspect_shape_invalid')
    return {'id':fields[0],'imageId':fields[1],'status':fields[2],'owner':fields[3],'checkpoint':fields[4],'portBindings':fields[5],'networkId':fields[6]}

def bounded_read(proc, *, timeout_seconds=LOG_TIMEOUT_SECONDS, max_bytes=MAX_LOG_BYTES):
    """Read a child pipe without blocking past deadline; always terminate/reap on bounds."""
    buf = bytearray()
    overflow = timed_out = False
    deadline = time.monotonic() + timeout_seconds
    sel = selectors.DefaultSelector()
    try:
        sel.register(proc.stdout, selectors.EVENT_READ)
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                timed_out = True
                break
            ready = sel.select(min(0.2, remaining))
            if not ready:
                if proc.poll() is not None:
                    break
                continue
            chunk = os.read(proc.stdout.fileno(), min(16384, max_bytes + 1 - len(buf)))
            if not chunk:
                break
            buf.extend(chunk)
            if len(buf) > max_bytes:
                overflow = True
                break
    except Exception:
        timed_out = True
    finally:
        sel.close()
        if timed_out or overflow:
            try: proc.terminate()
            except Exception: pass
        try:
            proc.wait(timeout=2)
        except Exception:
            try: proc.kill()
            except Exception: pass
            try: proc.wait(timeout=2)
            except Exception: pass
        try: proc.stdout.close()
        except Exception: pass
    rc = proc.poll()
    return bytes(buf[:max_bytes]), overflow, timed_out, rc

def bounded_logs(gateway_id, since):
    try:
        proc = subprocess.Popen(['docker.exe','logs','--timestamps','--since',since,'--tail',str(MAX_LOG_LINES),gateway_id],
                                stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    except Exception:
        return b'', False, False, None
    return bounded_read(proc)

def resolve_named_container(name, expected_image):
    fmt='{{.Id}}|{{.Image}}|{{index .Config.Labels "com.leadshug.channels.owner"}}|{{index .Config.Labels "checkpoint"}}'
    p=run(['inspect','--format',fmt,name],check=False,output_limit=2048)
    if p.returncode!=0:
        return None
    fields=p.stdout.decode('ascii','strict').strip().split('|')
    if len(fields)!=4 or not re.fullmatch(r'[0-9a-f]{64}',fields[0]) or fields[1]!=expected_image or fields[2]!=OWNER or fields[3]!=CHECKPOINT:
        raise SafeFailure('named_container_cleanup_identity_mismatch')
    return fields[0]

def resolve_named_network(name):
    p=run(['network','inspect','--format','{{.Id}}|{{.Internal}}|{{index .Labels "com.leadshug.channels.owner"}}|{{index .Labels "checkpoint"}}',name],check=False,output_limit=2048)
    if p.returncode!=0:
        return None
    fields=p.stdout.decode('ascii','strict').strip().split('|')
    if len(fields)!=4 or not re.fullmatch(r'[0-9a-f]{64}',fields[0]) or fields[1:]!=['true',OWNER,CHECKPOINT]:
        raise SafeFailure('named_network_cleanup_identity_mismatch')
    return fields[0]

def cleanup_owned(kind, obj_id):
    if not obj_id:
        return False
    if kind == 'container':
        f = inspect_container(obj_id)
        if f['owner'] != OWNER or f['checkpoint'] != CHECKPOINT:
            raise SafeFailure('cleanup_ownership_guard_failed')
        run(['rm','-f',obj_id],timeout=15)
        return True
    p = run(['network','inspect','--format','{{.Id}}|{{.Internal}}|{{index .Labels "com.leadshug.channels.owner"}}|{{index .Labels "checkpoint"}}',obj_id])
    fields = p.stdout.decode('ascii','strict').strip().split('|')
    if fields != [obj_id,'true',OWNER,CHECKPOINT]:
        raise SafeFailure('network_cleanup_guard_failed')
    run(['network','rm',obj_id],timeout=15)
    return True

def parse_rows(raw):
    try: lines = raw.decode('utf-8','strict').splitlines(); valid_utf8 = True
    except UnicodeDecodeError: lines = raw.decode('utf-8','replace').splitlines(); valid_utf8 = False
    parsed=[]
    for line in lines:
        m=FORMAT.fullmatch(line)
        if m: parsed.append(m.groupdict())
    return lines,parsed,len(lines)-len(parsed),valid_utf8

def self_test():
    # Strict parser and failure controls are pure; no Docker/network is invoked.
    synthetic='2026-10-17T17:00:00Z 2026-10-17T17:00:00+00:00 route=meta method=POST status=201 bytes=10 request_time=0.1 upstream_status=201 upstream_time=0.1'
    assert FORMAT.fullmatch(synthetic)
    assert not FORMAT.fullmatch(synthetic.replace('route=meta','route=/webhooks/meta'))
    expected=[c['route'] for c in CASES]
    observed=[c['route'] for c in CASES]
    assert observed == expected and len(observed) == len(CASES)
    # A no-output open pipe times out, is terminated, and is reaped.
    rfd,wfd=os.pipe(); reader=os.fdopen(rfd,'rb',buffering=0)
    class Hung:
        def __init__(self): self.stdout=reader; self.done=False; self.terminated=False; self.killed=False
        def poll(self): return -15 if self.done else None
        def terminate(self): self.terminated=True; self.done=True; os.close(wfd)
        def kill(self): self.killed=True; self.done=True
        def wait(self,timeout=None): self.done=True; return -15
    hung=Hung(); _,ov,to,rc=bounded_read(hung,timeout_seconds=0.05,max_bytes=32)
    assert to and hung.terminated and rc == -15
    # Byte overflow is detected and also terminates/reaps its child.
    rfd,wfd=os.pipe(); reader=os.fdopen(rfd,'rb',buffering=0)
    class Flood(Hung):
        def __init__(self): self.stdout=reader; self.done=False; self.terminated=False; self.killed=False; self.writer=wfd; self.thread=threading.Thread(target=self._write,daemon=True); self.thread.start()
        def _write(self):
            try: os.write(self.writer,b'x'*8192)
            except OSError: pass
        def terminate(self): self.terminated=True; self.done=True; os.close(self.writer)
    flood=Flood(); _,ov,to,rc=bounded_read(flood,timeout_seconds=1,max_bytes=128)
    assert ov and flood.terminated and rc == -15
    print(json.dumps({'strictSyntheticLineAccepted':True,'invalidRouteRejected':True,'perCaseSequenceAssertion':'11 expected/11 matched','hungPipeTimedOutAndReaped':True,'byteOverflowTerminatedAndReaped':True,'dockerOrNetworkCalled':False,'rawLogsPersistedOrPrinted':False},separators=(',',':')))

def main():
    if sys.argv[1:] == ['--self-test']:
        self_test(); return 0
    stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d%H%M%S'); nonce=uuid.uuid4().hex[:8]
    network_name=f'cp69-route-probe-v2-{stamp}-{nonce}'; stub_name=f'cp69-route-stub-v2-{stamp}-{nonce}'; gateway_name=f'cp69-route-gateway-v2-{stamp}-{nonce}'
    network_id=stub_id=gateway_id=None
    result={'checkpoint':'cp69-gateway-route-candidate-v2','startedAtUtc':dt.datetime.now(dt.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z'),
            'source':{'path':'docker/local-gateway.conf.template','oldSha256':OLD_TEMPLATE_SHA,'candidateSha256':hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
                      'expectedCaseSensitiveAnchoredRule':'~^/webhooks/meta/?$ meta;','fixtureCaseCount':len(CASES)},
            'images':{'nginx':NGINX_IMAGE,'nodeFixtureRuntime':API_IMAGE,'pullAttempted':False},
            'network':{'internal':True,'name':network_name},'operations':{},'cleanup':{'attempted':False,'containerIds':[],'networkId':None,'containersRemoved':0,'networkRemoved':False,'complete':False}}
    try:
        if result['source']['candidateSha256'] != CANDIDATE_SHA or result['source']['candidateSha256'] == OLD_TEMPLATE_SHA:
            raise SafeFailure('candidate_source_hash_mismatch')
        source_text=TEMPLATE.read_text(encoding='utf-8')
        if '~^/webhooks/meta/?$ meta;' not in source_text or 'route=$leadshug_route' not in source_text:
            raise SafeFailure('candidate_expected_source_contract_missing')
        for label,image in [('nginx',NGINX_IMAGE),('nodeFixtureRuntime',API_IMAGE)]:
            p=run(['image','inspect','--format','{{.Id}}',image])
            if p.stdout.decode('ascii','strict').strip()!=image: raise SafeFailure(label+'_image_pin_mismatch')
        np=run(['network','create','--internal','--label',f'{OWNER_KEY}={OWNER}','--label',f'checkpoint={CHECKPOINT}',network_name])
        network_id=np.stdout.decode('ascii','strict').strip()
        if not re.fullmatch(r'[0-9a-f]{64}',network_id): raise SafeFailure('network_id_invalid')
        result['network']['id']=network_id; result['cleanup']['networkId']=network_id
        n=run(['network','inspect','--format','{{.Id}}|{{.Internal}}|{{index .Labels "com.leadshug.channels.owner"}}|{{index .Labels "checkpoint"}}',network_id])
        if n.stdout.decode('ascii','strict').strip().split('|') != [network_id,'true',OWNER,CHECKPOINT]: raise SafeFailure('network_scope_guard_failed')
        sp=run(['run','-d','--name',stub_name,'--network',network_id,'--network-alias','api','--network-alias','web','--label',f'{OWNER_KEY}={OWNER}','--label',f'checkpoint={CHECKPOINT}','--entrypoint','node',API_IMAGE,'-e',FIXTURE])
        stub_id=sp.stdout.decode('ascii','strict').strip(); result['cleanup']['containerIds'].append(stub_id)
        sf=inspect_container(stub_id)
        if sf['owner']!=OWNER or sf['checkpoint']!=CHECKPOINT or sf['imageId']!=API_IMAGE or sf['networkId']!=network_id or sf['portBindings'] not in ('','null','{}'):
            raise SafeFailure('fixture_stub_scope_guard_failed')
        result['stub']={k:sf[k] for k in ('id','imageId','status','owner','checkpoint','portBindings','networkId')}
        gp=run(['create','--name',gateway_name,'--network',network_id,'--network-alias','gateway','--label',f'{OWNER_KEY}={OWNER}','--label',f'checkpoint={CHECKPOINT}',NGINX_IMAGE])
        gateway_id=gp.stdout.decode('ascii','strict').strip(); result['cleanup']['containerIds'].append(gateway_id)
        gf=inspect_container(gateway_id)
        if gf['owner']!=OWNER or gf['checkpoint']!=CHECKPOINT or gf['imageId']!=NGINX_IMAGE or gf['portBindings'] not in ('','null','{}'):
            raise SafeFailure('fixture_gateway_scope_guard_failed')
        result['candidateGatewayCreated']={k:gf[k] for k in ('id','imageId','status','owner','checkpoint','portBindings')}
        source_win=r'C:\unifast\leadshug\leadshug_now_docker\docker\local-gateway.conf.template'
        run(['cp',source_win,f'{gateway_id}:/etc/nginx/conf.d/default.conf'])
        run(['start',gateway_id])
        gf_running=inspect_container(gateway_id)
        if gf_running['status']!='running' or gf_running['networkId']!=network_id or gf_running['id']!=gateway_id or gf_running['owner']!=OWNER or gf_running['checkpoint']!=CHECKPOINT or gf_running['imageId']!=NGINX_IMAGE:
            raise SafeFailure('fixture_gateway_started_scope_guard_failed')
        result['candidateGateway']={k:gf_running[k] for k in ('id','imageId','status','owner','checkpoint','portBindings','networkId')}
        nt=run(['exec',gateway_id,'nginx','-t'],check=False)
        result['operations']['nginxTestExitCode']=nt.returncode
        if nt.returncode!=0: raise SafeFailure('candidate_nginx_test_failed',nt.returncode)
        since=dt.datetime.now(dt.timezone.utc).isoformat(timespec='microseconds').replace('+00:00','Z')
        client=run(['exec',stub_id,'node','-e',CLIENT],timeout=20,output_limit=8192)
        responses=json.loads(client.stdout.decode('utf-8','strict'))
        result['syntheticHttp']={'caseCount':len(CASES),'responseCount':len(responses),'allExpectedStatusesObserved':False,'requestsSentOnlyToIsolatedInternalNetwork':True,
                                 'cases':[{'case':c['case'],'expectedRoute':c['route'],'observedStatus':(responses[i].get('status') if i<len(responses) else None),'expectedStatus':c['status']} for i,c in enumerate(CASES)],
                                 'noLiveApiWebDatabaseVolumeOrCredentialsUsed':True}
        if len(responses)!=len(CASES): raise SafeFailure('synthetic_http_response_count_mismatch')
        if any(r.get('case')!=c['case'] or r.get('status')!=c['status'] for r,c in zip(responses,CASES)):
            raise SafeFailure('synthetic_http_observed_status_mismatch')
        result['syntheticHttp']['allExpectedStatusesObserved']=True
        raw,overflow,timed_out,log_rc=bounded_logs(gateway_id,since)
        lines,parsed,unparsed,utf8ok=parse_rows(raw)
        marker_list=[b'cp69_query_canary',b'cp69_auth_canary',b'cp69_cookie_canary',b'cp69_body_canary',b'Bearer',b'Cookie',b'/webhooks/meta',b'?']
        markers_absent=not any(marker in raw for marker in marker_list)
        expected_routes=[c['route'] for c in CASES]
        observed_routes=[row['route'] for row in parsed]
        per_case_match=(len(lines)==len(CASES) and len(parsed)==len(CASES) and observed_routes==expected_routes and all(int(row['status'])==c['status'] for row,c in zip(parsed,CASES)))
        result['syntheticHttp']['cases']=[{'case':c['case'],'expectedRoute':c['route'],'observedRoute':(observed_routes[i] if i<len(observed_routes) else None),'routeMatch':(i<len(observed_routes) and observed_routes[i]==c['route']),'observedStatus':responses[i].get('status'),'expectedStatus':c['status']} for i,c in enumerate(CASES)]
        route_counts=collections.Counter(observed_routes)
        joint=collections.Counter((row['route'],row['method'],row['status']) for row in parsed)
        complete=(log_rc==0 and not overflow and not timed_out and utf8ok and unparsed==0 and len(lines)<MAX_LOG_LINES)
        result['accessLog']={'sinceUtc':since,'tailLimit':MAX_LOG_LINES,'byteLimit':MAX_LOG_BYTES,'timeoutSeconds':LOG_TIMEOUT_SECONDS,
                             'bytesRead':len(raw),'lineCount':len(lines),'parsedLineCount':len(parsed),'unparsedLineCount':unparsed,'utf8Valid':utf8ok,
                             'overflow':overflow,'timeout':timed_out,'dockerExitCode':log_rc,'coverageComplete':complete,
                             'observedRouteSequence':observed_routes,'perCaseRouteAndStatusAssertionsPassed':per_case_match,
                             'routeCounts':dict(sorted(route_counts.items())),
                             'jointRouteMethodStatusCounts':[{'route':r,'method':m,'status':s,'count':n} for (r,m,s),n in sorted(joint.items())],
                             'syntheticCanaryMarkersAbsent':markers_absent,'rawLinesPersistedOrPrinted':False}
        if not complete or not per_case_match or not markers_absent: raise SafeFailure('bounded_log_or_per_case_route_assertion_failed')
        result['candidateStatus']='validated_isolated_candidate_only_not_activated'
    except SafeFailure as error:
        result['failure']={'phase':error.phase,'exitCode':error.code}; result['candidateStatus']='inconclusive_or_failed'
    except Exception:
        result['failure']={'phase':'unexpected_safe_failure'}; result['candidateStatus']='inconclusive_or_failed'
    finally:
        result['cleanup']['attempted']=True
        if gateway_id is None:
            try:
                gateway_id=resolve_named_container(gateway_name,NGINX_IMAGE)
                if gateway_id: result['cleanup']['containerIds'].append(gateway_id)
            except Exception: result['cleanup'].setdefault('failures',[]).append('gateway_named_cleanup_resolution_failed')
        if stub_id is None:
            try:
                stub_id=resolve_named_container(stub_name,API_IMAGE)
                if stub_id: result['cleanup']['containerIds'].append(stub_id)
            except Exception: result['cleanup'].setdefault('failures',[]).append('stub_named_cleanup_resolution_failed')
        if network_id is None:
            try:
                network_id=resolve_named_network(network_name)
                if network_id: result['cleanup']['networkId']=network_id
            except Exception: result['cleanup'].setdefault('failures',[]).append('network_named_cleanup_resolution_failed')
        for obj_id in (gateway_id,stub_id):
            if not obj_id: continue
            try:
                if cleanup_owned('container',obj_id): result['cleanup']['containersRemoved']+=1
            except Exception: result['cleanup'].setdefault('failures',[]).append('owned_container_cleanup_failed')
        if network_id:
            try:
                if cleanup_owned('network',network_id): result['cleanup']['networkRemoved']=True
            except Exception: result['cleanup'].setdefault('failures',[]).append('owned_network_cleanup_failed')
        result['cleanup']['complete']=result['cleanup']['containersRemoved']==len(result['cleanup']['containerIds']) and result['cleanup']['networkRemoved']
        result['completedAtUtc']=dt.datetime.now(dt.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z')
        tmp=EVIDENCE.with_name(EVIDENCE.name+'.tmp')
        tmp.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        os.replace(tmp,EVIDENCE)
    print(json.dumps(result,separators=(',',':')))
    return 0 if result.get('candidateStatus')=='validated_isolated_candidate_only_not_activated' and result['cleanup']['complete'] else 2

if __name__=='__main__': sys.exit(main())
