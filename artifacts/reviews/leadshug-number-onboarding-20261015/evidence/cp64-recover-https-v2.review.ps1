[CmdletBinding()]
param(
    [switch]$LaunchNewSupervisor,
    [long]$ExpectedOldStartTicks = 639277908932385742,
    [switch]$ValidateOnly
)

$ErrorActionPreference = 'Stop'
$oldPid = 21180
$oldParentPid = 22836
$oldExe = 'C:\unifast\leadshug\leadshug_now_docker\foundation_documentation\artifacts\tmp\number-onboarding-execution\cloudflared-cp46\cloudflared-windows-amd64.exe'
$oldConfig = 'C:\unifast\leadshug\leadshug_now_docker\foundation_documentation\artifacts\tmp\number-onboarding-execution\cloudflared-cp46\empty-config.yml'
$newDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$newSupervisor = Join-Path $newDir 'cp64-supervisor.exe'
$newCloudflared = Join-Path $newDir 'cloudflared-windows-amd64.exe'
$newConfig = Join-Path $newDir 'empty-config.yml'
$newState = Join-Path $newDir 'runtime-state.json'
$expectedOldExeHash = '86aee4017b26625cee8484c113558f48effa4cd47f7aa05fcf425604e5d2b23c'
$expectedSupervisorHash = 'bdf68028ea2da0699b1e04d191453b5d7090861b17f518d236ce6b084d45c69b'
$expectedCloudflaredHash = '86aee4017b26625cee8484c113558f48effa4cd47f7aa05fcf425604e5d2b23c'
$expectedOldArgs = 'tunnel --config "' + $oldConfig + '" --no-autoupdate --url http://127.0.0.1:8083'

function Get-Sha256([string]$Path) {
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Assert-OldPinnedChild([long]$ExpectedTicks) {
    if ($ExpectedTicks -ne 639277908932385742) { throw 'old_child_native_start_ticks_mismatch' }
    $proc = Get-Process -Id $oldPid -ErrorAction Stop
    $nativeTicks = $proc.StartTime.ToUniversalTime().Ticks
    if ($nativeTicks -ne $ExpectedTicks) { throw 'old_child_native_start_ticks_mismatch' }
    $cim = Get-CimInstance Win32_Process -Filter "ProcessId=$oldPid" -Property ProcessId,ExecutablePath,CommandLine,ParentProcessId -ErrorAction Stop
    if ($cim.ExecutablePath -cne $oldExe) { throw 'old_child_executable_path_mismatch' }
    if ($cim.ParentProcessId -ne $oldParentPid) { throw 'old_child_parent_pid_mismatch' }
    if ($cim.CommandLine -cne ('"' + $oldExe + '" ' + $expectedOldArgs)) { throw 'old_child_command_line_mismatch' }
    if ((Get-Sha256 $cim.ExecutablePath) -ne $expectedOldExeHash) { throw 'old_child_executable_hash_mismatch' }
    $oldConfigItem = Get-Item -LiteralPath $oldConfig -ErrorAction Stop
    if ($oldConfigItem.Length -ne 0) { throw 'old_child_config_not_empty' }
    return [ordered]@{
        pid = $oldPid
        nativeStartTimeUtcTicks = $nativeTicks
        executablePath = $cim.ExecutablePath
        executableSha256 = $expectedOldExeHash
        parentPid = [int]$cim.ParentProcessId
        target = 'http://127.0.0.1:8083'
        argumentsMatch = $true
        configLength = 0
    }
}

function Get-ExactOwnedPathMatches([string]$Path) {
    # WQL string literal escaping: escape backslashes first, then apostrophes.
    $slash = [string][char]92
    $escapedPath = $Path.Replace($slash, $slash + $slash).Replace("'", $slash + "'")
    $query = "SELECT ProcessId, ExecutablePath, CreationDate FROM Win32_Process WHERE ExecutablePath = '$escapedPath'"
    @(Get-CimInstance -Query $query -ErrorAction Stop)
}

if ($LaunchNewSupervisor -and $ValidateOnly) { throw 'choose_validate_only_or_launch' }
if (-not $LaunchNewSupervisor -and -not $ValidateOnly) { $ValidateOnly = $true }

foreach ($entry in @(
    @{ Path = $newSupervisor; Hash = $expectedSupervisorHash; Name = 'supervisor' },
    @{ Path = $newCloudflared; Hash = $expectedCloudflaredHash; Name = 'cloudflared' }
)) {
    if (-not (Test-Path -LiteralPath $entry.Path -PathType Leaf)) { throw ('missing_cp64_' + $entry.Name) }
    if ((Get-Sha256 $entry.Path) -ne $entry.Hash) { throw ('cp64_' + $entry.Name + '_hash_mismatch') }
}
if (-not (Test-Path -LiteralPath $newConfig -PathType Leaf) -or (Get-Item -LiteralPath $newConfig).Length -ne 0) {
    throw 'cp64_config_not_empty_or_missing'
}
if (Test-Path -LiteralPath $newState) { throw 'cp64_state_already_exists_refuse_duplicate_launch' }

$oldPin = Assert-OldPinnedChild -ExpectedTicks $ExpectedOldStartTicks
if (-not (Test-NetConnection -ComputerName 127.0.0.1 -Port 8083 -InformationLevel Quiet)) {
    throw 'local_origin_listener_8083_unavailable'
}

if ($ValidateOnly) {
    [ordered]@{
        result = 'validate_only_passed_no_process_mutation'
        oldPinnedChild = $oldPin
        newSupervisorSha256 = $expectedSupervisorHash
        newCloudflaredSha256 = $expectedCloudflaredHash
        newConfigLength = 0
        newStateAbsent = $true
        localListener8083 = $true
        oldSupervisorAbsentStatus = 'known_from_prior_readonly_snapshot; not inferred from PID reuse'
    } | ConvertTo-Json -Depth 5
    exit 0
}

# Query only the two exact cp64 executable paths, server-side, and request only
# process ID, executable path, and creation date. No machine-wide argv projection.
$matchingNew = @(
    (Get-ExactOwnedPathMatches -Path $newSupervisor)
    (Get-ExactOwnedPathMatches -Path $newCloudflared)
)
if ($matchingNew.Count -gt 0) { throw 'cp64_owned_process_path_already_present_refuse_adoption_or_duplicate' }

# This branch creates a new, independently owned supervisor only. It never stops
# or signals the old child. Later retirement requires separately adjudicated
# proof of the new host over normal TLS from both Windows and WSL.
$startup = ([wmiclass]'Win32_ProcessStartup').CreateInstance()
$startup.ShowWindow = 0
$quotedSupervisor = '"' + $newSupervisor + '"'
$creation = ([wmiclass]'Win32_Process').Create($quotedSupervisor, $null, $startup)
if ($creation.ReturnValue -ne 0 -or -not $creation.ProcessId) { throw ('wmi_create_failed_code_' + $creation.ReturnValue) }
[ordered]@{
    result = 'new_owned_supervisor_created_old_child_not_touched'
    supervisorPid = [int]$creation.ProcessId
    supervisorExecutablePath = $newSupervisor
    supervisorSha256 = $expectedSupervisorHash
    expectedChildExecutablePath = $newCloudflared
    expectedChildSha256 = $expectedCloudflaredHash
    expectedTarget = 'http://127.0.0.1:8083'
    expectedTransport = 'http2'
    oldChildRetired = $false
    nextGate = 'wait for fresh state, exact child identity, and verified normal-TLS root/health/JS from Windows and WSL; do not edit origin before that proof'
} | ConvertTo-Json -Depth 5
