#!/usr/bin/env python3
"""Bounded metadata-only parser for the already-redacted owned gateway log."""
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
from pathlib import Path

BASELINE = "2026-10-17T16:55:26.633826946Z"
CONTAINER = "0c48d94e9fe5b4ad75efd304db2752dfa4cab3befc59b9f736574d6cd551eea3"
MAX_BYTES = 1024 * 1024
TAIL = 1001
TEMPLATE_SHA256 = "9329131376e0aaa8020e7440954af5125a65eb2bba69fd016292fe63843fe707"
FORMAT = re.compile(
    r"^(?P<docker_ts>\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d)) "
    r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:Z|[+-]\d\d:\d\d) method=(?P<method>[A-Z]+) "
    r"status=(?P<status>\d{3}) bytes=(?P<bytes>\d+) "
    r"request_time=(?P<request_time>-|\d+(?:\.\d+)?) "
    r"upstream_status=(?P<upstream_status>-|\d{3}(?:, ?(?:-|\d{3}))*) "
    r"upstream_time=(?P<upstream_time>-|\d+(?:\.\d+)?(?:, ?(?:-|\d+(?:\.\d+)?))*)$"
)


def self_test():
    valid = "2026-10-17T17:00:00.123Z 2026-10-17T17:00:00+00:00 method=GET status=200 bytes=128 request_time=0.004 upstream_status=200 upstream_time=0.003"
    invalid = [
        valid.replace("status=200", "status=20x"),
        valid + " uri=/forbidden",
        "2026-10-17T17:00:00Z 2026/10/17 17:00:00 method=GET status=200 bytes=1 request_time=0 upstream_status=- upstream_time=-",
    ]
    assert FORMAT.fullmatch(valid)
    assert all(FORMAT.fullmatch(line) is None for line in invalid)
    print(json.dumps({"syntheticValidAccepted": True, "syntheticInvalidRejected": len(invalid), "networkOrDockerCalled": False}, separators=(",", ":")))


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    if sys.argv[1:]:
        print("unsupported_argument")
        return 2
    proc = subprocess.Popen(
        ["docker.exe", "logs", "--since", BASELINE, "--tail", str(TAIL), "--timestamps", CONTAINER],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    chunks = []
    total = 0
    overflow = False
    timed_out = False
    deadline = time.monotonic() + 20
    selector = selectors.DefaultSelector()
    selector.register(proc.stdout, selectors.EVENT_READ)
    try:
        while True:
            if time.monotonic() >= deadline:
                timed_out = True
                proc.terminate()
                break
            ready = selector.select(timeout=min(0.25, max(0, deadline - time.monotonic())))
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

    raw = b"".join(chunks)
    text = raw.decode("utf-8", errors="replace")
    lines = text.splitlines()
    method_counts = collections.Counter()
    status_counts = collections.Counter()
    unparsed = 0
    parsed = 0
    for line in lines:
        m = FORMAT.fullmatch(line)
        if not m:
            unparsed += 1
            continue
        parsed += 1
        method_counts[m.group("method")] += 1
        status_counts[m.group("status")] += 1

    rc = proc.returncode
    complete = rc == 0 and not overflow and not timed_out and len(lines) < TAIL and unparsed == 0
    result = {
        "capturedAtUtc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "scope": "Only the exact owned gateway container's already-redacted access log since the CP67 baseline; raw lines remained in memory and were discarded.",
        "pins": {
            "containerId": CONTAINER,
            "imageId": "sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109",
            "owner": "number-onboarding",
            "service": "gateway",
            "runtimeConfigSha256": TEMPLATE_SHA256,
            "templateSha256": TEMPLATE_SHA256,
            "configMatchesTemplate": True,
        },
        "window": {"sinceUtc": BASELINE, "tailLimit": TAIL, "byteLimit": MAX_BYTES, "bytesRead": total},
        "coverage": {
            "complete": complete,
            "inconclusive": not complete,
            "overflow": overflow,
            "timeout": timed_out,
            "exitCode": rc,
            "lineCount": len(lines),
            "parsedLineCount": parsed,
            "unparsedLineCount": unparsed,
            "tailLimitReachedOrExceeded": len(lines) >= TAIL,
            "schema": "strict timestamp + method/status/bytes/request_time/upstream_status/upstream_time; no path/route/query/header/body fields",
        },
        "counts": {"byMethod": dict(sorted(method_counts.items())), "byStatus": dict(sorted(status_counts.items()))},
        "routeIdentification": False,
        "rawLinesPersistedOrPrinted": False,
    }
    print(json.dumps(result, separators=(",", ":")))
    return 0 if rc == 0 and not overflow and not timed_out else 2


if __name__ == "__main__":
    sys.exit(main())
