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
import time

GATEWAY_ID = "0c48d94e9fe5b4ad75efd304db2752dfa4cab3befc59b9f736574d6cd551eea3"
GATEWAY_IMAGE = "sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109"
ROUTE_TEMPLATE_SHA = "8c5524a215717370c01a45f333854f24a2a413e84e3bd93184d80ab1a4efc00c"
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

def self_test():
    valid = "2026-10-17T17:34:02.558891Z 2026-10-17T17:34:02+00:00 route=meta method=POST status=200 bytes=12 request_time=0.004 upstream_status=200 upstream_time=0.003"
    bad = [valid.replace("route=meta", "route=/webhooks/meta"), valid + " uri=/forbidden", valid.replace("status=200", "status=20x")]
    assert LINE.fullmatch(valid) is not None
    assert all(LINE.fullmatch(line) is None for line in bad)
    print(json.dumps({"syntheticValidAccepted": True, "syntheticInvalidRejected": len(bad), "dockerOrNetworkCalled": False, "rawLogsPersistedOrPrinted": False}, separators=(",", ":")))

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
    routes, methods, statuses = collections.Counter(), collections.Counter(), collections.Counter()
    parsed = 0
    unparsed = 0
    for line in lines:
        m = LINE.fullmatch(line)
        if not m:
            unparsed += 1
            continue
        parsed += 1
        routes[m.group("route")] += 1
        methods[m.group("method")] += 1
        statuses[m.group("status")] += 1
    complete = log_rc == 0 and not overflow and not timeout and capture_error is None and decode_ok and len(lines) < TAIL and unparsed == 0
    result = {
        "status": "complete" if complete else "inconclusive",
        "capturedAtUtc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "pins": {"gatewayId": GATEWAY_ID, "imageId": GATEWAY_IMAGE, "owner": OWNER, "project": PROJECT, "service": SERVICE, "routeTemplateSha256": ROUTE_TEMPLATE_SHA, "activeConfigSha256": config_sha},
        "window": {"sinceUtc": since, "tailLimit": TAIL, "byteLimit": MAX_BYTES, "bytesRead": len(raw)},
        "coverage": {"complete": complete, "overflow": overflow, "timeout": timeout, "dockerExitCode": log_rc, "lineCount": len(lines), "parsedLineCount": parsed, "unparsedLineCount": unparsed, "tailLimitReachedOrExceeded": len(lines) >= TAIL, "strictUtf8": decode_ok},
        "counts": {"byRoute": dict(sorted(routes.items())), "byMethod": dict(sorted(methods.items())), "byStatus": dict(sorted(statuses.items()))},
        "routeAttribution": "aggregate route enum only; no request-level attribution or payload fields",
        "rawLogsPersistedOrPrinted": False,
    }
    print(json.dumps(result, separators=(",", ":")))
    return 0 if complete else 2

if __name__ == "__main__":
    sys.exit(main())
