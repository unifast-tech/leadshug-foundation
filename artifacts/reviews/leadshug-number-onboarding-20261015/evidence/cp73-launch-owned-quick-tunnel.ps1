[CmdletBinding()]
param(
    [switch]$LaunchNewSupervisor,
    [string]$AcceptedProofPath
)

$ErrorActionPreference = 'Stop'
$sourceDir = 'C:\unifast\leadshug\leadshug_now_docker\foundation_documentation\artifacts\tmp\number-onboarding-execution\T\cloudflared-cp64'
$runtimeDir = 'C:\unifast\leadshug\leadshug_now_docker\foundation_documentation\artifacts\tmp\number-onboarding-execution\T\cloudflared-cp73-runtime'
$sourceSupervisor = Join-Path $sourceDir 'cp64-supervisor.exe'
$sourceCloudflared = Join-Path $sourceDir 'cloudflared-windows-amd64.exe'
$sourceEmptyConfig = Join-Path $sourceDir 'empty-config.yml'
$supervisorPath = Join-Path $runtimeDir 'cp64-supervisor.exe'
$cloudflaredPath = Join-Path $runtimeDir 'cloudflared-windows-amd64.exe'
$emptyConfigPath = Join-Path $runtimeDir 'empty-config.yml'
$statePath = Join-Path $runtimeDir 'runtime-state.json'
$launchReceiptPath = Join-Path $runtimeDir 'launch-receipt.json'
$supervisorSha = 'bdf68028ea2da0699b1e04d191453b5d7090861b17f518d236ce6b084d45c69b'
$cloudflaredSha = '86aee4017b26625cee8484c113558f48effa4cd47f7aa05fcf425604e5d2b23c'
$target = 'http://127.0.0.1:8083'

function Get-Sha256([string]$Path) {
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Get-ExactPathMatches([string]$Path) {
    $slash = [string][char]92
    $escaped = $Path.Replace($slash, $slash + $slash).Replace("'", $slash + "'")
    $query = "SELECT ProcessId, ExecutablePath, CreationDate FROM Win32_Process WHERE ExecutablePath = '$escaped'"
    @(Get-CimInstance -Query $query -ErrorAction Stop)
}

if (-not $LaunchNewSupervisor) {
    $sourcesMatch = (Test-Path -LiteralPath $sourceSupervisor -PathType Leaf) -and
        (Test-Path -LiteralPath $sourceCloudflared -PathType Leaf) -and
        (Test-Path -LiteralPath $sourceEmptyConfig -PathType Leaf) -and
        ((Get-Sha256 $sourceSupervisor) -ceq $supervisorSha) -and
        ((Get-Sha256 $sourceCloudflared) -ceq $cloudflaredSha) -and
        ((Get-Item -LiteralPath $sourceEmptyConfig).Length -eq 0)
    $runtimePathAbsent = -not (Test-Path -LiteralPath $runtimeDir)
    [ordered]@{
        result = 'preparation_check_only_no_process_mutation'
        acceptedSourcesMatch = $sourcesMatch
        freshRuntimePathAbsent = $runtimePathAbsent
        target = $target
        processLaunchAttempted = $false
        boundary = [ordered]@{ processMutation = $false; configOrEnvMutation = $false; processArgvEnumeration = $false }
    } | ConvertTo-Json -Depth 4 -Compress
    exit 0
}

if ([string]::IsNullOrWhiteSpace($AcceptedProofPath) -or -not (Test-Path -LiteralPath $AcceptedProofPath -PathType Leaf)) { throw 'accepted_go_proof_required' }
$proof = Get-Content -LiteralPath $AcceptedProofPath -Raw | ConvertFrom-Json
$selfSha = Get-Sha256 $MyInvocation.MyCommand.Path
if ($proof.decision -cne 'GO' -or $proof.operation -cne 'launch_new_quick_tunnel' -or
    $proof.helperSha256 -cne $selfSha -or $proof.supervisorSha256 -cne $supervisorSha -or
    $proof.cloudflaredSha256 -cne $cloudflaredSha -or $proof.target -cne $target) {
    throw 'accepted_go_proof_mismatch'
}
if (Test-Path -LiteralPath $runtimeDir) { throw 'fresh_runtime_path_exists_refuse_adoption' }
if ((Get-Sha256 $sourceSupervisor) -cne $supervisorSha -or
    (Get-Sha256 $sourceCloudflared) -cne $cloudflaredSha -or
    (Get-Item -LiteralPath $sourceEmptyConfig).Length -ne 0) { throw 'accepted_source_binary_or_config_mismatch' }
if ((Get-ExactPathMatches -Path $sourceSupervisor).Count -gt 0 -or
    (Get-ExactPathMatches -Path $sourceCloudflared).Count -gt 0) { throw 'prior_owned_tunnel_process_present_refuse_duplicate' }
if ((Get-ExactPathMatches -Path $supervisorPath).Count -gt 0 -or
    (Get-ExactPathMatches -Path $cloudflaredPath).Count -gt 0) { throw 'exact_new_owned_process_path_already_present_refuse_adoption' }

New-Item -ItemType Directory -Path $runtimeDir | Out-Null
Copy-Item -LiteralPath $sourceSupervisor -Destination $supervisorPath
Copy-Item -LiteralPath $sourceCloudflared -Destination $cloudflaredPath
$empty = [System.IO.File]::Open($emptyConfigPath, [System.IO.FileMode]::CreateNew, [System.IO.FileAccess]::Write, [System.IO.FileShare]::Read)
$empty.Flush($true)
$empty.Dispose()
if ((Get-Sha256 $supervisorPath) -cne $supervisorSha -or
    (Get-Sha256 $cloudflaredPath) -cne $cloudflaredSha -or
    (Get-Item -LiteralPath $emptyConfigPath).Length -ne 0 -or
    (Test-Path -LiteralPath $statePath) -or
    (Get-ExactPathMatches -Path $supervisorPath).Count -gt 0 -or
    (Get-ExactPathMatches -Path $cloudflaredPath).Count -gt 0) { throw 'new_owned_runtime_prelaunch_guard_failed' }

$startup = ([wmiclass]'Win32_ProcessStartup').CreateInstance()
$startup.ShowWindow = 0
$creation = ([wmiclass]'Win32_Process').Create(('"' + $supervisorPath + '"'), $null, $startup)
if ($creation.ReturnValue -ne 0 -or -not $creation.ProcessId) { throw 'owned_supervisor_creation_failed' }
$receipt = [ordered]@{
    checkpoint = 'cp73-owned-quick-tunnel-launch'
    capturedAtUtc = [DateTime]::UtcNow.ToString('o')
    result = 'new_owned_supervisor_created'
    supervisorPid = [int]$creation.ProcessId
    supervisorSha256 = $supervisorSha
    cloudflaredSha256 = $cloudflaredSha
    target = $target
    newRuntimeDirectory = $runtimeDir
    oldProcessesStoppedOrAdopted = $false
    nextGate = 'read fresh runtime state and exact new process identity, then verify new hostname over normal TLS before any origin edit'
}
$receipt | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $launchReceiptPath -Encoding UTF8
$receipt | ConvertTo-Json -Depth 4 -Compress
