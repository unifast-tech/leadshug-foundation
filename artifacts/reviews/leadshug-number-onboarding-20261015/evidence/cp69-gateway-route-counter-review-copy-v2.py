#!/usr/bin/env python3
"""Bounded route/method/status aggregate reader for the owned redacted gateway log."""
import argparse
import collections
import datetime as dt
import hashlib
import json
import os
import re
import selectors
import subprocess
import sys
from pathlib import Path
import time

GATEWAY_ID = "0c48d94e9fe5b4ad75efd304db2752dfa4cab3befc59b9f736574d6cd551eea3"
GATEWAY_IMAGE = "sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109"
ROUTE_TEMPLATE_SHA = "6d4563cc5f5823bdb1177f350c942dc2472fc70133aef5b177fa4b57c5c9f1a0"
SOURCE_PATH = Path("/mnt/c/unifast/leadshug/leadshug_now_docker/docker/local-gateway.conf.template")
OWNER = "number-onboarding"
PROJECT = "leadshug_channels_local"
SERVICE = "gateway"
MAX_BYTES = 1024 * 1024
TAIL = 1001
INSPECT_FORMAT = '{{.Id}}|{{.Image}}|{{.State.Status}}|{{index .Config.Labels "com.leadshug.channels.owner"}}|{{index .Config.Labels "com.docker.compose.project"}}|{{index .Config.Labels "com.docker.compose.service"}}'
LINE = re.compile(r"^(?P<docker_ts>\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)) (?P<nginx_ts>\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)) route=(?P<route>meta|other) method=(?P<method>[A-Z]+) status=(?P<status>\d{3}) bytes=(?P<bytes>\d+) request_time=(?P<request_time>-|\d+(?:\.\d+)?) upstream_status=(?P<upstream_status>-|\d{3}(?:, ?(?:-|\d{3}))*) upstream_time=(?P<upstream_time>-|\d+(?:\.\d+)?(?:, ?(?:-|\d+(?:\.\d+)?))*)$")

def run(args, timeout=8, cap=2048):
    try:
        p = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=timeout, check=False)
        return p.returncode, p.stdout if len(p.stdout) <= cap else None, ("output_limit" if len(p.stdout) > cap else None)
    except subprocess.TimeoutExpired:
        return None, None, "timeout"
    except Exception:
        return None, None, "invocation_failed"

def capture_logs(since):
    cmd = ["docker.exe", "logs", "--since", since, "--tail", str(TAIL), "--timestamps", GATEWAY_ID]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    except Exception:
        return b"", None, False, False, "log_command_failed"
    selector = selectors.DefaultSelector()
    selector.register(proc.stdout, selectors.EVENT_READ)
    chunks, total, overflow, timed_out = [], 0, False, False
    deadline = time.monotonic() + 20
    try:
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                timed_out = True
                proc.terminate()
                break
            ready = selector.select(min(0.2, remaining))
            if not ready:
                if proc.poll() is not None:
                    break
                continue
            block = os.read(proc.stdout.fileno(), 32768)
            if not block:
                break
            total += len(block)
            if total > MAX_BYTES:
                overflow = True
                proc.terminate()
                break
            chunks.append(block)
    finally:
        selector.close()
    try:
        proc.wait(timeout=2)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        timed_out = True
    return b"".join(chunks), proc.returncode, overflow, timed_out, None

def aggregate_rows(rows):
    routes, methods, statuses, joint = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    for row in rows:
        route, method, status = row["route"], row["method"], row["status"]
        routes[route] += 1
        methods[method] += 1
        statuses[status] += 1
        joint[(route, method, status)] += 1
    return routes, methods, statuses, joint

def coverage_is_complete(log_rc, overflow, timeout, capture_error, decode_ok, line_count, unparsed, source_match):
    return log_rc == 0 and not overflow and not timeout and capture_error is None and decode_ok and line_count < TAIL and unparsed == 0 and source_match

def self_test():
    valid = "2026-10-17T17:34:02.558891Z 2026-10-17T17:34:02+00:00 route=meta method=POST status=500 bytes=12 request_time=0.004 upstream_status=500 upstream_time=0.003"
    bad = [valid.replace("route=meta", "route=/webhooks/meta"), valid + " uri=/forbidden", valid.replace("status=500", "status=50x")]
    assert LINE.fullmatch(valid) is not None
    assert all(LINE.fullmatch(line) is None for line in bad)
    left=[("meta","POST","500"),("other","GET","200")]
    right=[("meta","GET","200"),("other","POST","500")]
    lrows=[{"route":r,"method":m,"status":st} for r,m,st in left]
    rrows=[{"route":r,"method":m,"status":st} for r,m,st in right]
    lj=aggregate_rows(lrows)[3]; rj=aggregate_rows(rrows)[3]
    assert lj != rj and lj[("meta","POST","500")] == 1 and rj[("meta","POST","500")] == 0
    assert coverage_is_complete(0,False,False,None,True,1,0,True)
    assert not coverage_is_complete(0,True,False,None,True,1,0,True)
    assert not coverage_is_complete(0,False,True,None,True,1,0,True)
    assert not coverage_is_complete(1,False,False,None,True,1,0,True)
    assert not coverage_is_complete(0,False,False,None,False,1,0,True)
    assert not coverage_is_complete(0,False,False,None,True,TAIL,0,True)
    assert not coverage_is_complete(0,False,False,None,True,1,1,True)
    assert not coverage_is_complete(0,False,False,None,True,1,0,False)
    print(json.dumps({"syntheticValidAccepted": True, "syntheticInvalidRejected": len(bad), "oppositeMarginalsProduceDistinctJointBuckets": True, "overflowTimeoutNonzeroUtf8TailParseAndSourceFailureControls": True, "dockerOrNetworkCalled": False, "rawLogsPersistedOrPrinted": False}, separators=(",", ":")))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since-utc", help="Explicit RFC3339 UTC timestamp ending in Z")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test(); return 0
    if not a.since_utc:
        print(json.dumps({"status": "since_utc_required", "rawLogsPersistedOrPrinted": False}, separators=(",", ":"))); return 2
    try:
        since_dt = dt.datetime.fromisoformat(a.since_utc.replace("Z", "+00:00"))
        if not a.since_utc.endswith("Z") or since_dt.tzinfo is None or since_dt.utcoffset() != dt.timedelta(0):
            raise ValueError()
        since = a.since_utc
    except Exception:
        print(json.dumps({"status": "invalid_utc_since_argument", "rawLogsPersistedOrPrinted": False}, separators=(",", ":")))
        return 2
    rc, out, err = run(["docker.exe", "inspect", "--format", INSPECT_FORMAT, GATEWAY_ID])
    if rc != 0 or out is None or err:
        result = {"status": "gateway_pin_unavailable", "coverageComplete": False, "rawLogsPersistedOrPrinted": False}
        print(json.dumps(result, separators=(",", ":"))); return 2
    try:
        fields = out.decode("ascii", "strict").strip().split("|")
        if fields != [GATEWAY_ID, GATEWAY_IMAGE, "running", OWNER, PROJECT, SERVICE]:
            raise ValueError()
    except Exception:
        result = {"status": "gateway_pin_mismatch", "coverageComplete": False, "rawLogsPersistedOrPrinted": False}
        print(json.dumps(result, separators=(",", ":"))); return 2
    config_rc, config_out, config_err = run(["docker.exe", "exec", GATEWAY_ID, "sha256sum", "/etc/nginx/conf.d/default.conf"], timeout=8, cap=1024)
    try:
        config_sha = config_out.decode("ascii", "strict").strip().split()[0] if config_rc == 0 and config_out is not None and not config_err else None
    except Exception:
        config_sha = None
    if config_sha != ROUTE_TEMPLATE_SHA:
        result = {"status": "active_route_config_pin_mismatch", "coverageComplete": False, "runtimeConfigSha256": config_sha, "rawLogsPersistedOrPrinted": False}
        print(json.dumps(result, separators=(",", ":"))); return 2
    raw, log_rc, overflow, timeout, capture_error = capture_logs(since)
    try:
        lines = raw.decode("utf-8", "strict").splitlines()
        decode_ok = True
    except UnicodeDecodeError:
        lines = raw.decode("utf-8", "replace").splitlines()
        decode_ok = False
    parsed_rows = []
    parsed = 0
    unparsed = 0
    for line in lines:
        m = LINE.fullmatch(line)
        if not m:
            unparsed += 1
            continue
        parsed += 1
        parsed_rows.append(m.groupdict())
    try:
        source_sha = hashlib.sha256(SOURCE_PATH.read_bytes()).hexdigest()
    except Exception:
        source_sha = None
    source_match = source_sha == ROUTE_TEMPLATE_SHA
    routes, methods, statuses, joint = aggregate_rows(parsed_rows)
    complete = coverage_is_complete(log_rc,overflow,timeout,capture_error,decode_ok,len(lines),unparsed,source_match)
    result = {
        "status": "complete" if complete else "inconclusive",
        "capturedAtUtc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "pins": {"gatewayId": GATEWAY_ID, "imageId": GATEWAY_IMAGE, "owner": OWNER, "project": PROJECT, "service": SERVICE, "sourceSha256": source_sha, "routeTemplateSha256": ROUTE_TEMPLATE_SHA, "activeConfigSha256": config_sha, "sourceMatchesRouteTemplatePin": source_match},
        "window": {"sinceUtc": since, "tailLimit": TAIL, "byteLimit": MAX_BYTES, "bytesRead": len(raw)},
        "coverage": {"complete": complete, "overflow": overflow, "timeout": timeout, "dockerExitCode": log_rc, "lineCount": len(lines), "parsedLineCount": parsed, "unparsedLineCount": unparsed, "tailLimitReachedOrExceeded": len(lines) >= TAIL, "strictUtf8": decode_ok},
        "counts": {"byRoute": dict(sorted(routes.items())), "byMethod": dict(sorted(methods.items())), "byStatus": dict(sorted(statuses.items())), "byRouteMethodStatus": [{"route":r,"method":m,"status":st,"count":n} for (r,m,st),n in sorted(joint.items())]},
        "routeAttribution": "aggregate route enum only; no request-level attribution or payload fields",
        "rawLogsPersistedOrPrinted": False,
    }
    print(json.dumps(result, separators=(",", ":")))
    return 0 if complete else 2

if __name__ == "__main__":
    sys.exit(main())
