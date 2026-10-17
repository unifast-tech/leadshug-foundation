#!/usr/bin/env python3
"""One-shot, guarded CP69 gateway config activation. Never reads env or logs."""
import argparse
import datetime as dt
import hashlib
import http.client
import io
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import tarfile
import time
import tempfile
import uuid
from pathlib import Path

ROOT = Path("/mnt/c/unifast/leadshug/leadshug_now_docker")
SOURCE = ROOT / "docker" / "local-gateway.conf.template"
EVIDENCE = ROOT / "foundation_documentation" / "artifacts" / "reviews" / "leadshug-number-onboarding-20261015" / "evidence"
STAGE = EVIDENCE / "cp69-gateway-activation-stage-v2.json"
OLD_SHA = "9329131376e0aaa8020e7440954af5125a65eb2bba69fd016292fe63843fe707"
NEW_SHA = "6d4563cc5f5823bdb1177f350c942dc2472fc70133aef5b177fa4b57c5c9f1a0"
NGINX_IMAGE = "sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109"
EXPECTED_NETWORK = "d48c8a9ac92f00d8e2f1c1c6a1744ab14463aeba4abeab491f82719336925c20"
EXPECTED_HOST = "addressing-mar-perform-hormone.trycloudflare.com"
ACTIVE = "/etc/nginx/conf.d/default.conf"
TEMPLATE = "/etc/nginx/templates/default.conf.template"
EXPECTED_CONTAINERS = {
    "api": ("005529386c8a7ab499cd779942ce541bb90cd3a770b8436b41509d2655e54857", "sha256:fe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821", "healthy"),
    "gateway": ("0c48d94e9fe5b4ad75efd304db2752dfa4cab3befc59b9f736574d6cd551eea3", NGINX_IMAGE, ""),
    "web": ("9aa55b6681a8480dbfd7cbf2a51ab8571035603b288b52e6798d93741af01093", "sha256:cfd5e58b91a67d2fae4f37759274a34209cd2501082650a49545a60a12642361", ""),
    "evolution": ("cf749491f7149dc46ec4db597b2d9c12faf918dd4f05b5512ba75adaf8e29ea4", "sha256:385a3c4bedf42c66b46b43d06aae8712620144a84aa3b2c831b30c68435ab27c", ""),
    "evolution-redis": ("3b2e8d153d794a768ea87cb4f9cda7ba15dde242e2b8027bd372a475a9c26fbb", "sha256:f84b0c4678011602b9b98c227a4dcd5468bf8b088b02fdd4165cb7758bad8058", "healthy"),
    "evolution-postgres": ("150de898c3d9aa189ca0719eed7a65b95d95d8b948244e66b059a55f4554135a", "sha256:80f4c7a5e91618546dce5b4fe60cf03b14c0f9efa7e40157278d122772ced8d2", "healthy"),
    "postgres": ("4fcd87b431339e3b65a40beafa27db86cdc978ca79f71b911199f7090c837495", "sha256:80f4c7a5e91618546dce5b4fe60cf03b14c0f9efa7e40157278d122772ced8d2", "healthy"),
}
EXPECTED_VOLUMES = (
    "leadshug_channels_local_evolution_instances",
    "leadshug_channels_local_evolution_pg_data",
    "leadshug_channels_local_evolution_redis_data",
    "leadshug_channels_local_leadshug_arquivos",
    "leadshug_channels_local_leadshug_pg_data",
)
EXPECTED_POLICY_SHA = "d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d"
EXPECTED_POLICY_BYTES = 12865
EXPECTED_JS_SHA = "d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd"
EXPECTED_OWNER = "number-onboarding"
EXPECTED_PROJECT = "leadshug_channels_local"
LABEL_FORMAT = '{{.Id}}|{{.Image}}|{{.State.Status}}|{{with index .State `Health`}}{{.Status}}{{end}}|{{index .Config.Labels "com.leadshug.channels.owner"}}|{{index .Config.Labels "com.docker.compose.project"}}|{{index .Config.Labels "com.docker.compose.service"}}|{{range .NetworkSettings.Networks}}{{.NetworkID}}{{end}}'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def run(args, *, data=None, timeout=30, cap=2_000_000):
    """Capture subprocess output in memory, bound it, and never echo diagnostics."""
    try:
        p = subprocess.run(args, input=data, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=timeout, check=False)
        if len(p.stdout) > cap:
            return p.returncode, None, "output_limit"
        return p.returncode, p.stdout, None
    except subprocess.TimeoutExpired:
        return None, None, "timeout"
    except Exception:
        return None, None, "invocation_failed"

def docker(args, *, data=None, timeout=30, cap=2_000_000):
    return run(["docker.exe", *args], data=data, timeout=timeout, cap=cap)

def require_rc(args, data=None, timeout=30, cap=2_000_000, category="docker_guard_failed"):
    rc, out, err = docker(args, data=data, timeout=timeout, cap=cap)
    if rc != 0 or err is not None or out is None:
        raise RuntimeError(category)
    return out

def parse_one_line(data, category):
    try:
        text = data.decode("ascii", "strict").strip()
    except Exception:
        raise RuntimeError(category)
    if "\n" in text or "\r" in text:
        raise RuntimeError(category)
    return text

def container_facts(service, expected):
    cid, image, health = expected
    raw = require_rc(["inspect", "--format", LABEL_FORMAT, cid], category="container_inspect_failed")
    fields = parse_one_line(raw, "container_inspect_shape_invalid").split("|")
    if len(fields) != 8:
        raise RuntimeError("container_inspect_shape_invalid")
    found_id, found_image, state, found_health, owner, project, found_service, network = fields
    if (found_id, found_image, state, owner, project, found_service, network) != (cid, image, "running", EXPECTED_OWNER, EXPECTED_PROJECT, service, EXPECTED_NETWORK):
        raise RuntimeError("owned_container_pin_mismatch")
    if health and found_health != health:
        raise RuntimeError("owned_container_health_mismatch")
    return {"id": cid, "image": image, "state": state, "health": found_health or None, "owner": owner, "service": service, "networkId": network}

def parse_inventory_ids(text):
    values = [x.strip() for x in text.splitlines() if x.strip()]
    if any(not re.fullmatch(r"[0-9a-f]{64}", value) for value in values):
        raise RuntimeError("owned_container_inventory_id_shape_invalid")
    return sorted(values)

def inventory_matches(actual_ids, expected_ids):
    return sorted(actual_ids) == sorted(expected_ids)

def verify_inventory():
    expected_ids = sorted(v[0] for v in EXPECTED_CONTAINERS.values())
    raw = require_rc(["ps", "-aq", "--no-trunc", "--filter", "label=com.leadshug.channels.owner=number-onboarding", "--filter", "label=com.docker.compose.project=leadshug_channels_local"], category="owned_container_inventory_failed")
    actual_ids = parse_inventory_ids(raw.decode("ascii", "strict"))
    if not inventory_matches(actual_ids, expected_ids):
        raise RuntimeError("owned_container_inventory_drift")
    facts = {name: container_facts(name, pin) for name, pin in EXPECTED_CONTAINERS.items()}
    rawv = require_rc(["volume", "ls", "-q", "--filter", "label=com.leadshug.channels.owner=number-onboarding", "--filter", "label=com.docker.compose.project=leadshug_channels_local"], category="owned_volume_inventory_failed")
    actual_volumes = sorted(x.strip() for x in rawv.decode("ascii", "strict").splitlines() if x.strip())
    if actual_volumes != sorted(EXPECTED_VOLUMES):
        raise RuntimeError("owned_volume_inventory_drift")
    volume_facts = []
    vf = '{{.Name}}|{{index .Labels "com.leadshug.channels.owner"}}|{{index .Labels "com.docker.compose.project"}}'
    for name in EXPECTED_VOLUMES:
        raw = require_rc(["volume", "inspect", "--format", vf, name], category="volume_inspect_failed")
        values = parse_one_line(raw, "volume_inspect_shape_invalid").split("|")
        if values != [name, EXPECTED_OWNER, EXPECTED_PROJECT]:
            raise RuntimeError("owned_volume_pin_mismatch")
        volume_facts.append({"name": name, "owner": values[1], "project": values[2]})
    return facts, volume_facts

def docker_file_bytes(cid, path, expected_sha):
    rc, archive, err = docker(["cp", f"{cid}:{path}", "-"], timeout=20, cap=2_000_000)
    if rc != 0 or err or archive is None:
        raise RuntimeError("gateway_public_config_read_failed")
    try:
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:*") as tf:
            members = [m for m in tf.getmembers() if m.isfile()]
            if len(members) != 1 or members[0].name.rsplit("/", 1)[-1] != path.rsplit("/", 1)[-1]:
                raise RuntimeError("gateway_public_config_archive_shape_invalid")
            member = members[0]
            stream = tf.extractfile(member)
            content = stream.read(200_001)
            if len(content) > 200_000 or sha(content) != expected_sha:
                raise RuntimeError("gateway_public_config_sha_mismatch")
            return content, {"mode": member.mode & 0o7777, "uid": member.uid, "gid": member.gid}
    except RuntimeError:
        raise
    except Exception:
        raise RuntimeError("gateway_public_config_archive_invalid")

def remote_sha(cid, path):
    raw = require_rc(["exec", cid, "sha256sum", path], timeout=10, cap=1024, category="gateway_config_hash_read_failed")
    first = parse_one_line(raw, "gateway_config_hash_shape_invalid").split()[0]
    if not re.fullmatch(r"[0-9a-f]{64}", first):
        raise RuntimeError("gateway_config_hash_shape_invalid")
    return first

def remote_stat(cid, path):
    raw = require_rc(["exec", cid, "stat", "-c", "%a|%u|%g", path], timeout=10, cap=1024, category="gateway_config_metadata_read_failed")
    parts = parse_one_line(raw, "gateway_config_metadata_shape_invalid").split("|")
    if len(parts) != 3 or any(not re.fullmatch(r"[0-9]+", x) for x in parts):
        raise RuntimeError("gateway_config_metadata_shape_invalid")
    return {"mode": int(parts[0], 8), "uid": int(parts[1]), "gid": int(parts[2])}

def create_temp(cid, path, content, metadata):
    if remote_exists(cid, path):
        raise RuntimeError("owned_temp_path_collision")
    args = ["exec", "-i", cid, "sh", "-c", 'umask 077; cat > "$1"', "cp69-gateway", path]
    rc, out, err = docker(args, data=content, timeout=15, cap=1024)
    if rc != 0 or err or out is None:
        raise RuntimeError("gateway_temp_write_failed")
    mode = format(metadata["mode"], "o")
    rc, out, err = docker(["exec", cid, "chmod", mode, path], timeout=10, cap=1024)
    if rc != 0 or err:
        raise RuntimeError("gateway_temp_mode_failed")
    rc, out, err = docker(["exec", cid, "chown", f"{metadata['uid']}:{metadata['gid']}", path], timeout=10, cap=1024)
    if rc != 0 or err:
        raise RuntimeError("gateway_temp_owner_failed")

def remote_exists(cid, path):
    rc, out, err = docker(["exec", cid, "sh", "-c", 'test ! -e "$1"', "cp69-gateway", path], timeout=10, cap=256)
    if err:
        raise RuntimeError("gateway_temp_existence_check_failed")
    return rc != 0

def install_bytes(cid, content, expected_sha, expected_active_sha, metadata, transaction):
    temp = "/etc/nginx/conf.d/.cp69-default-conf-" + uuid.uuid4().hex + ".tmp"
    try:
        create_temp(cid, temp, content, metadata)
        if remote_sha(cid, temp) != expected_sha or remote_stat(cid, temp) != metadata:
            raise RuntimeError("gateway_temp_verification_failed")
        if remote_sha(cid, ACTIVE) != expected_active_sha or remote_stat(cid, ACTIVE) != metadata:
            raise RuntimeError("active_config_changed_before_atomic_rename")
        transaction["renameAttempted"] = True
        rc, out, err = docker(["exec", cid, "mv", "-f", "--", temp, ACTIVE], timeout=10, cap=1024)
        if rc != 0 or err:
            raise RuntimeError("gateway_atomic_rename_failed")
    except Exception:
        cleanup_temp(cid, temp)
        raise
    return temp

def cleanup_temp(cid, path):
    # Exact unique temp path only; never glob or discover arbitrary files.
    docker(["exec", cid, "rm", "-f", "--", path], timeout=10, cap=256)

def run_nginx(cid, args):
    rc, _, err = docker(["exec", cid, *args], timeout=20, cap=1024)
    return {"exitCode": rc, "stderrSuppressed": True, "invocationError": err}

def http_probe(host, port, path, tls=False):
    conn = None
    try:
        if tls:
            conn = http.client.HTTPSConnection(host, port, timeout=8, context=ssl.create_default_context())
        else:
            conn = http.client.HTTPConnection(host, port, timeout=5)
        conn.request("GET", path, headers={"Connection": "close"})
        response = conn.getresponse()
        body = response.read(300_001)
        if len(body) > 300_000:
            return {"status": response.status, "redirected": 300 <= response.status < 400, "noSetCookie": not bool(response.getheader("Set-Cookie")), "bodyWithinLimit": False}
        headers = {k.lower(): v for k, v in response.getheaders()}
        return {"status": response.status, "redirected": 300 <= response.status < 400, "noSetCookie": "set-cookie" not in headers, "bodyWithinLimit": True, "bytes": len(body), "sha256": sha(body), "contentTypeHtml": headers.get("content-type", "").lower().startswith("text/html") if path == "/privacidade.html" else None}
    except Exception:
        return {"status": None, "transportError": True}
    finally:
        if conn:
            try: conn.close()
            except Exception: pass

def probe_set(host, port, tls):
    paths = ("/", "/health", "/privacidade.html", "/assets/index-txvhtd65.js")
    found = {p: http_probe(host, port, p, tls) for p in paths}
    ok = all(v.get("status") == 200 and v.get("redirected") is False and v.get("noSetCookie") is True and v.get("bodyWithinLimit") is True for v in found.values())
    policy = found["/privacidade.html"]
    js = found["/assets/index-txvhtd65.js"]
    ok = ok and policy.get("bytes") == EXPECTED_POLICY_BYTES and policy.get("sha256") == EXPECTED_POLICY_SHA and policy.get("contentTypeHtml") is True and js.get("sha256") == EXPECTED_JS_SHA
    return {"passed": bool(ok), "tls": tls, "noSessionOrCookieSent": True, "paths": found}

def authority_check(path):
    try:
        proof = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        raise RuntimeError("root_operation_proof_unreadable")
    own_sha = sha(Path(__file__).read_bytes())
    if proof.get("checkpoint") != "cp69-gateway-route-activation-go" or proof.get("operationAuthority") != "GO" or proof.get("rootOutcome") != "GO" or proof.get("rootAccepted") is not True:
        raise RuntimeError("root_operation_GO_missing")
    if proof.get("helperSha256") != own_sha or proof.get("candidateSha256") != NEW_SHA or proof.get("oldActiveConfigSha256") != OLD_SHA:
        raise RuntimeError("root_operation_proof_not_bound_to_helper_and_bytes")
    if proof.get("hostname") != EXPECTED_HOST:
        raise RuntimeError("root_operation_host_pin_mismatch")
    if proof.get("containerIds") != {k: v[0] for k, v in EXPECTED_CONTAINERS.items()} or proof.get("networkId") != EXPECTED_NETWORK or proof.get("volumeNames") != list(EXPECTED_VOLUMES):
        raise RuntimeError("root_operation_resource_pins_mismatch")
    return proof, own_sha


def recovery_plan(current_sha, old_sha, candidate_sha, forward_reload_attempted):
    if current_sha is None:
        return {"decision":"unreadable_refuse_mutation","restore":False,"rollbackReload":False,"terminal":"active_state_unknown"}
    if current_sha == old_sha:
        return {"decision":"already_old_no_restore","restore":False,"rollbackReload":False,"terminal":"old_config_preserved"}
    if current_sha == candidate_sha:
        return {"decision":"restore_exact_candidate","restore":True,"rollbackReload":bool(forward_reload_attempted),"terminal":"restore_required"}
    return {"decision":"unknown_bytes_refuse_mutation","restore":False,"rollbackReload":False,"terminal":"unknown_active_bytes"}

def reserve_stage(path=STAGE):
    """Acquire a unique receipt with O_EXCL; never replace a preexisting receipt."""
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    try:
        fd = os.open(str(path), flags, 0o600)
    except FileExistsError:
        return False
    try:
        os.write(fd, b"{}\n")
        os.fsync(fd)
    finally:
        os.close(fd)
    return True

def guarded_recovery(read_sha, read_metadata, install_old, nginx_test, graceful_reload, old_sha, candidate_sha, old_meta, forward_reload_attempted):
    """Reconcile uncertain active-file writes; only exact candidate bytes are restorable."""
    try:
        current = read_sha()
    except Exception:
        return {"decision":"unreadable_refuse_mutation","rollbackAttempted":False,"rollbackVerified":False,"rollbackReloadCount":0}
    plan = recovery_plan(current, old_sha, candidate_sha, forward_reload_attempted)
    result = {"decision":plan["decision"],"rollbackAttempted":False,"rollbackVerified":False,"rollbackReloadCount":0}
    if plan["decision"] in ("unreadable_refuse_mutation", "unknown_bytes_refuse_mutation"):
        return result
    if plan["decision"] == "already_old_no_restore":
        try:
            result["rollbackVerified"] = read_metadata() == old_meta
        except Exception:
            result["rollbackVerified"] = False
        return result
    result["rollbackAttempted"] = True
    try:
        install_old()
    except Exception:
        # The restore rename can also commit before its response is lost.
        try:
            if read_sha() != old_sha:
                return result
        except Exception:
            return result
    try:
        if read_sha() != old_sha or read_metadata() != old_meta:
            return result
        if nginx_test() != 0:
            return result
        if forward_reload_attempted:
            result["rollbackReloadCount"] = 1
            if graceful_reload() != 0:
                return result
        result["rollbackVerified"] = True
        return result
    except Exception:
        return result

def write_stage(stage, status, failure=None, details=None, no_throw=False):
    global stage_events, stage_write_failure
    stage_events.append({"atUtc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"), "stage": stage, "status": status, "failureCategory": failure, "details": details or {}})
    if not stage_owned:
        return
    obj = {"checkpoint": "cp69-gateway-activation-stage-v2", "events": stage_events, "rawConfigOrLogsPersisted": False}
    tmp = STAGE.with_name(STAGE.name + "." + stage_nonce + "." + uuid.uuid4().hex + ".tmp")
    try:
        with tmp.open("x", encoding="utf-8") as stream:
            stream.write(json.dumps(obj, separators=(",", ":")))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, STAGE)
    except Exception:
        stage_write_failure = True
        if not no_throw:
            raise RuntimeError("stage_receipt_write_failed")

stage_events = []
stage_write_failure = False
stage_owned = False
stage_nonce = uuid.uuid4().hex

def self_test():
    expected=["a"*64,"b"*64]
    assert parse_inventory_ids("\n".join(expected)+"\n") == expected
    assert inventory_matches(expected,expected)
    assert not inventory_matches(expected+["c"*64],expected)
    assert not inventory_matches(expected[:1],expected)
    try: parse_inventory_ids("a"*12+"\n")
    except RuntimeError: pass
    else: raise AssertionError("truncated_id_not_rejected")
    with tempfile.TemporaryDirectory() as directory:
        existing=Path(directory)/"stage.json"; existing.write_bytes(b"prior-receipt")
        assert reserve_stage(existing) is False and existing.read_bytes()==b"prior-receipt"
        fresh=Path(directory)/"fresh.json"
        assert reserve_stage(fresh) is True and fresh.read_bytes()==b"{}\n"
    # Remote candidate rename commits, then its command response times out.
    state={"sha":OLD_SHA,"metadata":{"mode":420,"uid":0,"gid":0},"restores":0,"tests":0,"reloads":0}
    def readsha(): return state["sha"]
    def readmeta(): return state["metadata"]
    def install_old(): state["restores"]+=1; state["sha"]=OLD_SHA
    def test_old(): state["tests"]+=1; return 0
    def reload_old(): state["reloads"]+=1; return 0
    state["sha"]=NEW_SHA
    simulated_forward_rename_response="timeout"
    decision=recovery_plan(state["sha"],OLD_SHA,NEW_SHA,False)
    assert simulated_forward_rename_response=="timeout" and decision["decision"]=="restore_exact_candidate"
    recovered=guarded_recovery(readsha,readmeta,install_old,test_old,reload_old,OLD_SHA,NEW_SHA,state["metadata"],False)
    assert state["sha"]==OLD_SHA and recovered["rollbackAttempted"] and recovered["rollbackVerified"] and state["restores"]==1 and state["reloads"]==0
    # A failure before the rename leaves the original bytes and must not reinstall or reload.
    state.update(sha=OLD_SHA,restores=0,tests=0,reloads=0)
    unchanged=guarded_recovery(readsha,readmeta,install_old,test_old,reload_old,OLD_SHA,NEW_SHA,state["metadata"],False)
    assert unchanged["decision"]=="already_old_no_restore" and unchanged["rollbackVerified"] and state["restores"]==0 and state["reloads"]==0
    # Unknown and unreadable byte states are fail-closed with no restore or reload.
    state["sha"]="f"*64
    unknown=guarded_recovery(readsha,readmeta,install_old,test_old,reload_old,OLD_SHA,NEW_SHA,state["metadata"],True)
    unreadable=guarded_recovery(lambda: (_ for _ in ()).throw(OSError()),readmeta,install_old,test_old,reload_old,OLD_SHA,NEW_SHA,state["metadata"],True)
    assert unknown["decision"]=="unknown_bytes_refuse_mutation" and unreadable["decision"]=="unreadable_refuse_mutation" and state["restores"]==0 and state["reloads"]==0
    # A failed path after one forward reload permits exactly one rollback reload.
    state.update(sha=NEW_SHA,restores=0,tests=0,reloads=0)
    once=guarded_recovery(readsha,readmeta,install_old,test_old,reload_old,OLD_SHA,NEW_SHA,state["metadata"],True)
    assert once["rollbackVerified"] and once["rollbackReloadCount"]==1 and state["reloads"]==1
    # A rollback rename response can be lost after commit; exact old bytes reconcile it.
    state.update(sha=NEW_SHA,restores=0,tests=0,reloads=0)
    def install_old_uncertain(): state["restores"]+=1; state["sha"]=OLD_SHA; raise TimeoutError()
    uncertain_restore=guarded_recovery(readsha,readmeta,install_old_uncertain,test_old,reload_old,OLD_SHA,NEW_SHA,state["metadata"],False)
    assert uncertain_restore["rollbackVerified"] and state["sha"]==OLD_SHA and state["restores"]==1
    print(json.dumps({"fullIdInventoryAndDriftControls":True,"stageExclusiveReservationPreservesPriorBytes":True,"renameAppliedThenTimeoutRestored":True,"preRenameFailureRecognizesOldWithoutMutation":True,"unknownAndUnreadableBytesRefuseRestore":True,"forwardReloadBoundaryAllowsAtMostOneRollbackReload":True,"rollbackRenameAppliedThenTimeoutReconciled":True,"dockerOrNetworkCalled":False,"privateRead":False},separators=(",",":")))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--accepted-proof", help="Root-issued, hash-bound activation GO JSON")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test(); return 0
    if not args.accepted_proof:
        print(json.dumps({"checkpoint":"cp69-gateway-route-activation-v2","status":"accepted_root_GO_required","liveMutationAttempted":False},separators=(",",":"))); return 2
    result = {"checkpoint": "cp69-gateway-route-activation-v2", "status": "not_started", "liveMutationAttempted": False, "gatewayReloadAttempted": False, "rawConfigOrLogsPersisted": False}
    old_bytes = None
    old_meta = None
    changed = False
    active_write_may_have_started = False
    candidate_transaction = {"renameAttempted": False}
    forward_reload_attempted = False
    category = None
    try:
        proof, helper_sha = authority_check(args.accepted_proof)
        if sha(SOURCE.read_bytes()) != NEW_SHA:
            raise RuntimeError("candidate_source_hash_mismatch")
        exe = shutil.which("docker.exe")
        if not exe:
            raise RuntimeError("docker_executable_unavailable")
        global stage_owned
        if not reserve_stage(STAGE):
            raise RuntimeError("activation_stage_receipt_exists_refuse_overwrite")
        stage_owned = True
        write_stage("preflight", "started")
        containers, volumes = verify_inventory()
        gateway_id = EXPECTED_CONTAINERS["gateway"][0]
        if proof.get("containerIds") != {k: v[0] for k, v in EXPECTED_CONTAINERS.items()}:
            raise RuntimeError("operation_container_pin_drift")
        old_bytes, old_meta = docker_file_bytes(gateway_id, ACTIVE, OLD_SHA)
        if remote_sha(gateway_id, TEMPLATE) != NEW_SHA:
            raise RuntimeError("mounted_candidate_template_sha_mismatch")
        if remote_sha(gateway_id, ACTIVE) != OLD_SHA or remote_stat(gateway_id, ACTIVE) != old_meta:
            raise RuntimeError("active_config_old_snapshot_or_metadata_mismatch")
        result["preflight"] = {"containers": containers, "volumeNames": [x["name"] for x in volumes], "networkId": EXPECTED_NETWORK, "oldActiveConfigSha256": OLD_SHA, "candidateTemplateSha256": NEW_SHA, "activeMetadata": old_meta}
        write_stage("preflight", "passed", details={"containerCount": 7, "volumeCount": 5, "oldConfigSha256": OLD_SHA, "candidateSha256": NEW_SHA})
        write_stage("candidate_atomic_write", "started")
        result["liveMutationAttempted"] = True
        active_write_may_have_started = True
        install_bytes(gateway_id, SOURCE.read_bytes(), NEW_SHA, OLD_SHA, old_meta, candidate_transaction)
        changed = True
        if remote_sha(gateway_id, ACTIVE) != NEW_SHA or remote_stat(gateway_id, ACTIVE) != old_meta:
            raise RuntimeError("candidate_active_bytes_or_metadata_mismatch")
        result["activeConfigSha256"] = NEW_SHA
        result["activeMetadataPreserved"] = True
        write_stage("candidate_atomic_write", "passed", details={"candidateSha256": NEW_SHA, "metadataPreserved": True})
        write_stage("nginx_test", "started")
        test = run_nginx(gateway_id, ["nginx", "-t"])
        result["nginxTest"] = test
        if test.get("exitCode") != 0:
            raise RuntimeError("candidate_nginx_test_failed")
        write_stage("nginx_test", "passed", details={"exitCode": 0})
        write_stage("forward_graceful_reload", "started")
        forward_reload_attempted = True
        result["gatewayReloadAttempted"] = True
        reload_result = run_nginx(gateway_id, ["nginx", "-s", "reload"])
        result["forwardReload"] = reload_result
        if reload_result.get("exitCode") != 0:
            raise RuntimeError("forward_graceful_reload_failed")
        write_stage("forward_graceful_reload", "passed", details={"exitCode": 0})
        local = probe_set("127.0.0.1", 8083, False)
        public = probe_set(EXPECTED_HOST, 443, True)
        result["postchecks"] = {"local": local, "public": public}
        if not local["passed"] or not public["passed"]:
            raise RuntimeError("gateway_public_postcheck_failed")
        facts_after, volumes_after = verify_inventory()
        if facts_after != containers or [v["name"] for v in volumes_after] != [v["name"] for v in volumes]:
            raise RuntimeError("resource_preservation_postcheck_failed")
        if remote_sha(gateway_id, ACTIVE) != NEW_SHA or remote_stat(gateway_id, ACTIVE) != old_meta:
            raise RuntimeError("active_config_changed_after_reload")
        result["postconditions"] = {"activeConfigSha256": NEW_SHA, "gatewayId": gateway_id, "gatewayImage": NGINX_IMAGE, "networkId": EXPECTED_NETWORK, "ownedContainersPreserved": True, "ownedVolumesPreserved": True}
        result["status"] = "success_candidate_route_config_active"
        write_stage("terminal", "success", details={"configSha256": NEW_SHA, "publicProbePassed": True, "localProbePassed": True})
    except Exception as exc:
        category = str(exc) if re.fullmatch(r"[a-z0-9_]+", str(exc)) else "guard_or_transport_failure"
        result["failureCategory"] = category
        result["candidateRenameAttempted"] = candidate_transaction["renameAttempted"]
        if active_write_may_have_started and old_bytes is not None and old_meta is not None:
            gateway_id = EXPECTED_CONTAINERS["gateway"][0]
            def read_current_sha(): return remote_sha(gateway_id, ACTIVE)
            def read_current_metadata(): return remote_stat(gateway_id, ACTIVE)
            def restore_old(): install_bytes(gateway_id, old_bytes, OLD_SHA, NEW_SHA, old_meta, {"renameAttempted":False})
            def test_old(): return run_nginx(gateway_id, ["nginx", "-t"]).get("exitCode")
            def reload_old(): return run_nginx(gateway_id, ["nginx", "-s", "reload"]).get("exitCode")
            recovery = guarded_recovery(read_current_sha, read_current_metadata, restore_old, test_old, reload_old, OLD_SHA, NEW_SHA, old_meta, forward_reload_attempted)
            result["recovery"] = recovery
            result["rollbackAttempted"] = recovery["rollbackAttempted"]
            result["rollbackVerified"] = recovery["rollbackVerified"]
            result["rollbackReloadCount"] = recovery["rollbackReloadCount"]
            result["recoveryRefused"] = recovery["decision"] in ("unreadable_refuse_mutation", "unknown_bytes_refuse_mutation")
            result["recoveryDecision"] = recovery["decision"]
            if recovery["rollbackAttempted"] and not recovery["rollbackVerified"]:
                result["rollbackFailureCategory"] = "guarded_restore_or_verification_failed"
            write_stage("guarded_restore", "verified" if recovery["rollbackVerified"] else "incomplete_or_refused", category,
                        {"decision":recovery["decision"],"rollbackReloadCount":recovery["rollbackReloadCount"]}, no_throw=True)
        result["status"] = "failed_or_guarded_rollback"
        result["stageReceiptOwned"] = stage_owned
        result["stageReceiptWriteFailure"] = stage_write_failure
        if stage_owned:
            write_stage("terminal", result["status"], category, {"rollbackVerified": result.get("rollbackVerified", False), "gatewayReloadAttempted": forward_reload_attempted}, no_throw=True)
    print(json.dumps(result, separators=(",", ":")))
    return 0 if result["status"] == "success_candidate_route_config_active" else 2

if __name__ == "__main__":
    sys.exit(main())
