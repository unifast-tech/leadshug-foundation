[CmdletBinding()]
param(
    [switch]$ApplyAll,
    [switch]$RunPredicateTests,
    [string]$AcceptedProofPath = 'C:\unifast\leadshug\leadshug_now_docker\foundation_documentation\artifacts\reviews\leadshug-number-onboarding-20261015\evidence\cp64-transport-proof.json'
)

$ErrorActionPreference = 'Stop'
$repo = 'C:\unifast\leadshug\leadshug_now_docker'
$evidenceDir = Join-Path $repo 'foundation_documentation\artifacts\reviews\leadshug-number-onboarding-20261015\evidence'
$stageReceiptPath = Join-Path $evidenceDir 'cp64-activation-stage-v9.json'
$envPath = Join-Path $repo '.env.testing'
$policyPath = Join-Path $repo 'web-app\public\privacidade.html'
$newApiImage = 'sha256:fe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821'
$oldWebImage = 'sha256:6f4b2500e02d1523f99b423a08b6a166e319d5f3246ad516ef8f4a56d30001ed'
$candidateWebImage = 'sha256:cfd5e58b91a67d2fae4f37759274a34209cd2501082650a49545a60a12642361'
$apiTag = 'leadshug_channels_local-api'
$webTag = 'leadshug_channels_local-web'
$webCandidateTag = 'leadshug-channels-web-candidate:cp64-notransform-0cdafce3f985'
$webRollbackTag = 'leadshug_channels_local-web-rollback:cp64-prenotransform'
$expectedPolicySha = 'd0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d'
$expectedJsSha = 'd14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd'
$expectedPolicyBytes = 12865
$composePrefix = @(
    'compose','--project-name','leadshug_channels_local',
    '--env-file',(Join-Path $repo '.env.testing'),
    '-f',(Join-Path $repo 'docker-compose.yml'),
    '-f',(Join-Path $repo 'docker-compose.channels.yml'),
    '--profile','channels-local'
)
$baselineContainers = [ordered]@{
    api = 'f86d76c633f4f06a98a67dc4b6432700ac8e1e6f81b555697b5feabf6a1f08ab'
    gateway = '0c48d94e9fe5b4ad75efd304db2752dfa4cab3befc59b9f736574d6cd551eea3'
    web = 'fe783b00b3160e45483cf0bd1d4e17d688f2001c03d47fff40ab605707bc49a3'
    evolution = 'cf749491f7149dc46ec4db597b2d9c12faf918dd4f05b5512ba75adaf8e29ea4'
    evolutionRedis = '3b2e8d153d794a768ea87cb4f9cda7ba15dde242e2b8027bd372a475a9c26fbb'
    evolutionPostgres = '150de898c3d9aa189ca0719eed7a65b95d95d8b948244e66b059a55f4554135a'
    postgres = '4fcd87b431339e3b65a40beafa27db86cdc978ca79f71b911199f7090c837495'
}
$preservedImages = [ordered]@{
    gateway = 'sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109'
    evolution = 'sha256:385a3c4bedf42c66b46b43d06aae8712620144a84aa3b2c831b30c68435ab27c'
    evolutionRedis = 'sha256:f84b0c4678011602b9b98c227a4dcd5468bf8b088b02fdd4165cb7758bad8058'
    evolutionPostgres = 'sha256:80f4c7a5e91618546dce5b4fe60cf03b14c0f9efa7e40157278d122772ced8d2'
    postgres = 'sha256:80f4c7a5e91618546dce5b4fe60cf03b14c0f9efa7e40157278d122772ced8d2'
}
$expectedVolumes = @(
    'leadshug_channels_local_evolution_instances',
    'leadshug_channels_local_evolution_pg_data',
    'leadshug_channels_local_evolution_redis_data',
    'leadshug_channels_local_leadshug_arquivos',
    'leadshug_channels_local_leadshug_pg_data'
)
$script:stage = 'preflight'
$script:lastDockerExitCode = $null
$script:lastHttpStatus = $null
$script:lastHttpPath = $null
$script:baselineTopology = $null
$script:gatewayReloadAttempted = $false
$script:gatewayRecovery = $null
$script:lastFailureCategory = $null
$script:apiContainerId = $null
$script:webContainerId = $null
$script:operationApiId = $null
$script:operationWebId = $null
$script:originWriteOutcome = 'not_started'
$script:rollbackWebOutcome = 'not_started'
$script:rollbackApiOutcome = 'not_started'
$script:stageEvents = @()
$script:apiMutationStarted = $false
$script:webMutationStarted = $false
$script:webTagChanged = $false
$script:originChanged = $false
$script:originTransactionIncomplete = $false
$script:preservationVerified = $false
$script:receiptWriteFailure = $false
$script:failedStage = $null
$script:originalExitCode = $null
$script:originalHttpStatus = $null
$script:failureSnapshot = $null

function Write-SafeStageReceipt([string]$Status,[string]$FailureCategory,[switch]$NoThrow) {
    $script:stageEvents += [ordered]@{
        capturedAtUtc=[DateTime]::UtcNow.ToString('o')
        stage=$script:stage
        status=$Status
        failureCategory=$FailureCategory
        failedStage=$script:failedStage
        nativeExitCode=$script:lastDockerExitCode
        originalNativeExitCode=$script:originalExitCode
        httpStatus=$script:lastHttpStatus
        originalHttpStatus=$script:originalHttpStatus
        originWriteOutcome=$script:originWriteOutcome
        rollbackWebOutcome=$script:rollbackWebOutcome
        rollbackApiOutcome=$script:rollbackApiOutcome
        apiContainerId=$script:apiContainerId
        apiImage=$newApiImage
        operationApiContainerId=$script:operationApiId
        webContainerId=$script:webContainerId
        webImage=$candidateWebImage
        operationWebContainerId=$script:operationWebId
        preRollbackSnapshot=$script:failureSnapshot
        baselineGatewayTopology=$script:baselineTopology
        gatewayRecovery=$script:gatewayRecovery
        volumeSetGuardSucceeded=$script:preservationVerified
        receiptWriteFailure=$script:receiptWriteFailure
        privateValueOrBodyPersisted=$false
    }
    $safe=[ordered]@{checkpoint='cp64-activation-stage-v3';events=@($script:stageEvents)}
    $json=$safe | ConvertTo-Json -Depth 6
    try { [IO.File]::WriteAllText($stageReceiptPath,$json,[Text.UTF8Encoding]::new($false)) }
    catch {
        $script:receiptWriteFailure=$true
        $script:stageEvents[-1].receiptWriteFailure=$true
        if (-not $NoThrow) { throw 'stage_receipt_write_failed' }
    }
}

function Invoke-DockerText([string[]]$Arguments) {
    $priorPreference=$ErrorActionPreference; $invokeFailed=$false
    try {
        $ErrorActionPreference='Continue'
        $text = & docker.exe @Arguments 2>$null
        $script:lastDockerExitCode=[int]$LASTEXITCODE
    } catch { $script:lastFailureCategory='docker_read_native_invocation_exception'; $invokeFailed=$true }
    finally { $ErrorActionPreference=$priorPreference }
    if ($invokeFailed) { throw 'docker_read_native_invocation_failed' }
    if ($script:lastDockerExitCode -ne 0) { $script:lastFailureCategory='docker_read_nonzero'; throw 'docker_read_guard_failed' }
    return (($text | Out-String).Trim())
}
function Invoke-DockerMutation([string[]]$Arguments) {
    $priorPreference=$ErrorActionPreference; $invokeFailed=$false
    try {
        $ErrorActionPreference='Continue'
        $null = & docker.exe @Arguments *> $null
        $script:lastDockerExitCode=[int]$LASTEXITCODE
    } catch { $script:lastFailureCategory='docker_mutation_native_invocation_exception'; $invokeFailed=$true }
    finally { $ErrorActionPreference=$priorPreference }
    if ($invokeFailed) { throw 'docker_mutation_native_invocation_failed' }
    if ($script:lastDockerExitCode -ne 0) { $script:lastFailureCategory='docker_mutation_nonzero'; throw 'docker_mutation_failed' }
}
function Assert-DockerExecutableAvailable {
    $cmd=Get-Command -Name 'docker.exe' -CommandType Application -ErrorAction SilentlyContinue
    if ($null -eq $cmd) { throw 'docker_native_executable_missing' }
}
function Get-ImageId([string]$Ref) {
    Invoke-DockerText @('image','inspect','--format','{{.Id}}',$Ref)
}
function Get-ContainerFacts([string]$Id) {
    $raw = Invoke-DockerText @('inspect','--format','{{.Id}}|{{.Image}}|{{.State.Status}}|{{with index .State `Health`}}{{.Status}}{{end}}',$Id)
    $p = $raw.Split('|')
    if ($p.Count -ne 4) { throw 'container_inspect_shape_mismatch' }
    $labelsRaw=Invoke-DockerText @('inspect','--format','{{json .Config.Labels}}',$Id)
    $labels=$labelsRaw | ConvertFrom-Json
    [ordered]@{ id=$p[0]; image=$p[1]; state=$p[2]; health=$p[3]; owner=[string]$labels.'com.leadshug.channels.owner'; project=[string]$labels.'com.docker.compose.project'; service=[string]$labels.'com.docker.compose.service' }
}
function Assert-OwnedService([string]$Id,[string]$Image,[string]$Service,[string]$RequiredState='running',[string]$RequiredHealth='') {
    $f=Get-ContainerFacts $Id
    if ($f.id -cne $Id -or $f.image -cne $Image -or $f.state -cne $RequiredState -or $f.owner -cne 'number-onboarding' -or $f.project -cne 'leadshug_channels_local' -or $f.service -cne $Service) { throw ('owned_service_identity_mismatch_'+$Service) }
    if ($RequiredHealth -and $f.health -cne $RequiredHealth) { throw ('owned_service_health_mismatch_'+$Service) }
    return $f
}
function Assert-PreservedResources([string]$Except) {
    $script:preservationVerified=$false
    foreach ($name in @('gateway','evolution','evolutionRedis','evolutionPostgres','postgres')) {
        $id = $baselineContainers[$name]
        $f = Get-ContainerFacts $id
        $serviceName=@{gateway='gateway';evolution='evolution';evolutionRedis='evolution-redis';evolutionPostgres='evolution-postgres';postgres='postgres'}[$name]
        if ($f.id -cne $id -or $f.image -cne $preservedImages[$name] -or $f.state -cne 'running' -or $f.owner -cne 'number-onboarding' -or $f.project -cne 'leadshug_channels_local' -or $f.service -cne $serviceName) { throw ('preserved_container_changed_' + $name) }
    }
    foreach ($volume in $expectedVolumes) {
        if ((Invoke-DockerText @('volume','inspect','--format','{{.Name}}',$volume)) -cne $volume) { throw 'owned_volume_missing_or_changed' }
    }
    $script:preservationVerified=$true
}
function Get-ComposeServiceId([string]$Service) {
    $id = Invoke-DockerText (@($composePrefix) + @('ps','-q',$Service))
    if ($id -notmatch '^[0-9a-f]{64}$') { throw ('compose_service_id_invalid_' + $Service) }
    return $id
}
function Assert-SelectedService([string]$Service,[string]$ExpectedId,[string]$ExpectedImage,[string]$Health='') {
    $selected=Get-ComposeServiceId $Service
    if ($selected -cne $ExpectedId) { throw ('compose_selected_id_mismatch_'+$Service) }
    return Assert-OwnedService $selected $ExpectedImage $Service 'running' $Health
}
function Invoke-ComposeUp([string]$Service,[string]$PublicOrigin) {
    $hadNode=Test-Path Env:CHANNELS_NODE_ENV; $savedNode=$env:CHANNELS_NODE_ENV
    $hadOrigin=Test-Path Env:CHANNELS_LOCAL_ORIGIN; $savedOrigin=$env:CHANNELS_LOCAL_ORIGIN
    try {
        $env:CHANNELS_NODE_ENV='production'; $env:CHANNELS_LOCAL_ORIGIN=$PublicOrigin
        Invoke-DockerMutation (@($composePrefix) + @('up','-d','--no-build','--no-deps','--force-recreate',$Service))
    } finally {
        if ($hadNode) { $env:CHANNELS_NODE_ENV=$savedNode } else { Remove-Item Env:CHANNELS_NODE_ENV -ErrorAction SilentlyContinue }
        if ($hadOrigin) { $env:CHANNELS_LOCAL_ORIGIN=$savedOrigin } else { Remove-Item Env:CHANNELS_LOCAL_ORIGIN -ErrorAction SilentlyContinue }
    }
}
function Find-ByteSequence([byte[]]$Haystack,[byte[]]$Needle,[int]$Start=0) {
    if ($Needle.Length -eq 0 -or $Start -lt 0 -or $Start -gt $Haystack.Length-$Needle.Length) { return -1 }
    for ($i=$Start; $i -le $Haystack.Length-$Needle.Length; $i++) {
        $match=$true
        for ($j=0; $j -lt $Needle.Length; $j++) { if ($Haystack[$i+$j] -ne $Needle[$j]) { $match=$false; break } }
        if ($match) { return $i }
    }
    return -1
}
function New-OriginEdit([byte[]]$InputBytes,[string]$HostName) {
    # Inspect only bytes needed to identify the one authorized key. Recognized
    # forms: optional first-line UTF-8 BOM, leading horizontal space, optional
    # export + horizontal space, key, optional horizontal space, equals.
    # Any other occurrence of this key is ambiguous and fails closed.
    $keyBytes=[Text.Encoding]::ASCII.GetBytes('CHANNELS_LOCAL_ORIGIN')
    $exportBytes=[Text.Encoding]::ASCII.GetBytes('export')
    $originPrefix=[Text.Encoding]::ASCII.GetBytes('https://')
    $occurrences=@(); $assignments=@(); $lineStart=0
    for ($i=0; $i -le $InputBytes.Length; $i++) {
        if ($i -eq $InputBytes.Length -or $InputBytes[$i] -eq 10 -or $InputBytes[$i] -eq 13) {
            $lineEnd=$i; $length=$lineEnd-$lineStart
            [byte[]]$lineBytes=New-Object byte[] $length
            if ($length -gt 0) { [Array]::Copy($InputBytes,$lineStart,$lineBytes,0,$length) }
            $bomLength=0
            if ($lineStart -eq 0 -and $length -ge 3 -and $lineBytes[0] -eq 239 -and $lineBytes[1] -eq 187 -and $lineBytes[2] -eq 191) { $bomLength=3 }
            $searchStart=$bomLength
            if ((Find-ByteSequence $lineBytes $keyBytes $searchStart) -ge 0) {
                $occurrences += 1
                $cursor=$bomLength
                while ($cursor -lt $length -and ($lineBytes[$cursor] -eq 32 -or $lineBytes[$cursor] -eq 9)) { $cursor++ }
                $exportPos=Find-ByteSequence $lineBytes $exportBytes $cursor
                if ($exportPos -eq $cursor) {
                    $afterExport=$cursor+$exportBytes.Length
                    if ($afterExport -ge $length -or ($lineBytes[$afterExport] -ne 32 -and $lineBytes[$afterExport] -ne 9)) { throw 'origin_key_unsupported_or_ambiguous_syntax' }
                    $cursor=$afterExport
                    while ($cursor -lt $length -and ($lineBytes[$cursor] -eq 32 -or $lineBytes[$cursor] -eq 9)) { $cursor++ }
                }
                if ($cursor+$keyBytes.Length -gt $length) { throw 'origin_key_unsupported_or_ambiguous_syntax' }
                for ($j=0; $j -lt $keyBytes.Length; $j++) { if ($lineBytes[$cursor+$j] -ne $keyBytes[$j]) { throw 'origin_key_unsupported_or_ambiguous_syntax' } }
                $cursor += $keyBytes.Length
                while ($cursor -lt $length -and ($lineBytes[$cursor] -eq 32 -or $lineBytes[$cursor] -eq 9)) { $cursor++ }
                if ($cursor -ge $length -or $lineBytes[$cursor] -ne 61) { throw 'origin_key_unsupported_or_ambiguous_syntax' }
                $cursor++
                while ($cursor -lt $length -and ($lineBytes[$cursor] -eq 32 -or $lineBytes[$cursor] -eq 9)) { $cursor++ }
                $valueStartInLine=$cursor
                $valueLength=$length-$valueStartInLine
                [byte[]]$valueBytes=New-Object byte[] $valueLength
                if ($valueLength -gt 0) { [Array]::Copy($lineBytes,$valueStartInLine,$valueBytes,0,$valueLength) }
                foreach ($b in $valueBytes) { if ($b -gt 127) { throw 'origin_previous_value_non_ascii_unsupported' } }
                $valueText=[Text.Encoding]::ASCII.GetString($valueBytes)
                if ($valueText -notmatch '^https://[A-Za-z0-9.-]+(?::[0-9]{1,5})?$') { throw 'origin_previous_value_unsupported_for_guarded_rollback' }
                $assignments += [ordered]@{valueStart=$lineStart+$valueStartInLine;lineEnd=$lineEnd;valueText=$valueText}
            }
            if ($i -lt $InputBytes.Length -and $InputBytes[$i] -eq 13 -and $i+1 -lt $InputBytes.Length -and $InputBytes[$i+1] -eq 10) { $i++ }
            $lineStart=$i+1
        }
    }
    if ($occurrences.Count -ne 1 -or $assignments.Count -ne 1) { throw 'origin_key_not_logically_unique' }
    $a=$assignments[0]
    $oldOrigin=$a.valueText
    $newValueBytes=[Text.Encoding]::UTF8.GetBytes('https://'+$HostName)
    $out=New-Object IO.MemoryStream
    $out.Write($InputBytes,0,$a.valueStart); $out.Write($newValueBytes,0,$newValueBytes.Length)
    $out.Write($InputBytes,$a.lineEnd,$InputBytes.Length-$a.lineEnd)
    [ordered]@{ original=$InputBytes; replacement=$out.ToArray(); oldOrigin=$oldOrigin; newOrigin=('https://'+$HostName) }
}

function Test-ByteArrayEqual([byte[]]$Left,[byte[]]$Right) {
    if ($Left.Length -ne $Right.Length) { return $false }
    for ($i=0; $i -lt $Left.Length; $i++) { if ($Left[$i] -ne $Right[$i]) { return $false } }
    return $true
}
function Read-StreamBytes([IO.Stream]$Stream) {
    $Stream.Position=0; [byte[]]$b=New-Object byte[] ([int]$Stream.Length); $offset=0
    while ($offset -lt $b.Length) { $n=$Stream.Read($b,$offset,$b.Length-$offset); if ($n -le 0) { throw 'origin_stream_read_failed' }; $offset += $n }
    return ,$b
}
function Flush-ByteStream([IO.Stream]$Stream) {
    if ($Stream -is [IO.FileStream]) { $Stream.Flush($true) } else { $Stream.Flush() }
}
function Invoke-ByteCAS([IO.Stream]$Stream,[byte[]]$Expected,[byte[]]$Replacement,[string]$DummyFault='none') {
    [byte[]]$current=Read-StreamBytes $Stream
    if (-not (Test-ByteArrayEqual $current $Expected)) { return [ordered]@{outcome='compare_failed_unchanged';bytesMatchExpected=$true} }
    try {
        $Stream.Position=0
        if ($DummyFault -eq 'write_after_prefix') {
            $partial=[Math]::Max(1,[Math]::Min($Replacement.Length,7)); $Stream.Write($Replacement,0,$partial); throw 'dummy_interrupted_write'
        }
        $Stream.Write($Replacement,0,$Replacement.Length); $Stream.SetLength($Replacement.Length)
        if ($DummyFault -eq 'flush_before_commit') { throw 'dummy_interrupted_flush' }
        Flush-ByteStream $Stream
        [byte[]]$verify=Read-StreamBytes $Stream
        if (-not (Test-ByteArrayEqual $verify $Replacement)) { throw 'origin_success_verification_failed' }
        return [ordered]@{outcome='written_and_verified';bytesMatchReplacement=$true}
    } catch {
        try {
            $Stream.Position=0; $Stream.Write($Expected,0,$Expected.Length); $Stream.SetLength($Expected.Length); Flush-ByteStream $Stream
            [byte[]]$restored=Read-StreamBytes $Stream
            if (Test-ByteArrayEqual $restored $Expected) { return [ordered]@{outcome='write_interrupted_restored';bytesMatchOriginal=$true} }
            return [ordered]@{outcome='restore_verification_failed';bytesMatchOriginal=$false}
        } catch { return [ordered]@{outcome='restore_incomplete';bytesMatchOriginal=$false} }
    }
}
function Set-OriginBytesCAS([byte[]]$Expected,[byte[]]$Replacement) {
    $aclBefore=(Get-Acl -LiteralPath $envPath).Sddl
    $fs=$null
    try {
        $fs=[IO.File]::Open($envPath,[IO.FileMode]::Open,[IO.FileAccess]::ReadWrite,[IO.FileShare]::None)
        $outcome=Invoke-ByteCAS $fs $Expected $Replacement
        $script:originWriteOutcome=$outcome.outcome
        if ($outcome.outcome -eq 'written_and_verified') { $script:originChanged=$true }
        if ($outcome.outcome -in @('restore_incomplete','restore_verification_failed')) { $script:originTransactionIncomplete=$true }
        $aclDuring=(Get-Acl -LiteralPath $envPath).Sddl
        if ($aclDuring -cne $aclBefore) {
            $script:originWriteOutcome='security_metadata_changed_during_transaction_'+$outcome.outcome
            throw 'origin_security_metadata_transaction_failed'
        }
        if ($outcome.outcome -ne 'written_and_verified') { throw ('origin_transaction_'+$outcome.outcome) }
    } finally { if ($null -ne $fs) { $fs.Dispose() } }
    $aclAfter=(Get-Acl -LiteralPath $envPath).Sddl
    if ($aclAfter -cne $aclBefore) { $script:originWriteOutcome='written_but_security_metadata_changed'; throw 'origin_security_metadata_postcondition_failed' }
    $script:originWriteOutcome='written_bytes_and_security_metadata_verified'
    return $true
}
function Test-OriginIs([byte[]]$Expected) {
    [byte[]]$cur=[IO.File]::ReadAllBytes($envPath)
    return (Test-ByteArrayEqual $cur $Expected)
}
function Wait-ApiHealthy([string]$ExpectedOrigin,[string]$ExpectedId) {
    $until=(Get-Date).AddSeconds(90)
    while ((Get-Date) -lt $until) {
        $id=Get-ComposeServiceId 'api'
        if ($id -cne $ExpectedId) { throw 'api_selected_id_changed_during_health_wait' }
        $f=Assert-OwnedService $id $newApiImage 'api' 'running'
        if ($f.health -ceq 'healthy') {
            $check="if(process.env.NODE_ENV==='production'&&process.env.WEB_ORIGIN==='$ExpectedOrigin'){process.stdout.write('true')}else{process.stdout.write('false')}"
            $v=Invoke-DockerText @('exec',$id,'node','-e',$check)
            if ($v -cne 'true') { throw 'api_public_origin_or_production_boolean_false' }
            return $id
        }
        Start-Sleep -Seconds 3
    }
    throw 'api_health_timeout'
}
function Get-NoSessionResponse([string]$Uri) {
    Add-Type -AssemblyName System.Net.Http
    $handler=New-Object Net.Http.HttpClientHandler
    $handler.AllowAutoRedirect=$false; $handler.UseCookies=$false
    $client=[Net.Http.HttpClient]::new($handler)
    try {
        $script:lastHttpPath=([Uri]$Uri).AbsolutePath
        $response=$client.GetAsync($Uri).GetAwaiter().GetResult()
        $script:lastHttpStatus=[int]$response.StatusCode
        [byte[]]$body=$response.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
        $headers=@{}
        foreach ($h in $response.Headers) { $headers[$h.Key]=$h.Value -join ',' }
        foreach ($h in $response.Content.Headers) { $headers[$h.Key]=$h.Value -join ',' }
        return [ordered]@{ status=[int]$response.StatusCode; body=$body; headers=$headers; redirected=($response.StatusCode -ge 300 -and $response.StatusCode -lt 400) }
    } finally { $client.Dispose(); $handler.Dispose() }
}
function Get-ContainerNetworkFacts([string]$Id) {
    $raw=Invoke-DockerText @('inspect','--format','{{.Id}}|{{.Image}}|{{json .Config.Labels}}|{{range .NetworkSettings.Networks}}{{.NetworkID}}|{{.IPAddress}}{{end}}',$Id)
    $parts=$raw.Split('|')
    if($parts.Count -ne 5){throw 'container_network_inspect_shape_mismatch'}
    $labels=$parts[2] | ConvertFrom-Json
    [ordered]@{id=$parts[0];image=$parts[1];owner=[string]$labels.'com.leadshug.channels.owner';project=[string]$labels.'com.docker.compose.project';service=[string]$labels.'com.docker.compose.service';networkId=$parts[3];ip=$parts[4]}
}
function Get-OwnedNetworkFacts {
    $raw=Invoke-DockerText @('network','inspect','--format','{{.Id}}|{{json .Labels}}','leadshug_channels_local_default')
    $parts=$raw.Split('|')
    if($parts.Count -ne 2){throw 'owned_network_inspect_shape_mismatch'}
    $labels=$parts[1] | ConvertFrom-Json
    [ordered]@{id=$parts[0];owner=[string]$labels.'com.leadshug.channels.owner';project=[string]$labels.'com.docker.compose.project';network=[string]$labels.'com.docker.compose.network'}
}
function Get-GatewayConfigSha([string]$GatewayId) {
    $raw=Invoke-DockerText @('exec',$GatewayId,'sha256sum','/etc/nginx/conf.d/default.conf')
    if($raw -notmatch '^([0-9a-f]{64})\s+/etc/nginx/conf\.d/default\.conf$'){throw 'gateway_runtime_config_hash_shape_mismatch'}
    return $Matches[1]
}
function Get-TopologySnapshot([string]$ApiId,[string]$WebId,[string]$GatewayId) {
    $network=Get-OwnedNetworkFacts
    if($network.owner -cne 'number-onboarding' -or $network.project -cne 'leadshug_channels_local' -or $network.network -cne 'default'){throw 'owned_network_identity_mismatch'}
    $api=Get-ContainerNetworkFacts $ApiId; $web=Get-ContainerNetworkFacts $WebId; $gateway=Get-ContainerNetworkFacts $GatewayId
    foreach($f in @($api,$web,$gateway)){
        if($f.owner -cne 'number-onboarding' -or $f.project -cne 'leadshug_channels_local' -or $f.networkId -cne $network.id){throw 'owned_backend_network_membership_mismatch'}
    }
    if($api.service -cne 'api' -or $web.service -cne 'web' -or $gateway.service -cne 'gateway'){throw 'owned_backend_service_identity_mismatch'}
    $runtimeConfigSha=Get-GatewayConfigSha $GatewayId
    $templateSha=(Get-FileHash -LiteralPath (Join-Path $repo 'docker\local-gateway.conf.template') -Algorithm SHA256).Hash.ToLowerInvariant()
    if($runtimeConfigSha -cne $templateSha){throw 'gateway_runtime_config_not_exact_public_template'}
    [ordered]@{networkId=$network.id;api=$api;web=$web;gateway=$gateway;runtimeConfigSha256=$runtimeConfigSha;templateSha256=$templateSha;configMatchesTemplate=$true}
}
function Get-DirectBackendSnapshot([string]$ApiId) {
    # The script is constant-only: fixed owned service DNS/IP endpoints, metadata output only.
    $js="const h=require('http'),c=require('crypto');const q=[['apiHealth','http://127.0.0.1:3000/health'],['webPolicy','http://web/privacidade.html'],['webRoot','http://web/'],['webJs','http://web/assets/index-txvhtd65.js'],['gatewayHealth','http://gateway/health'],['gatewayPolicy','http://gateway/privacidade.html'],['gatewayJs','http://gateway/assets/index-txvhtd65.js']];Promise.all(q.map(([n,u])=>new Promise(r=>{const x=h.get(u,{timeout:5000},z=>{const a=[];let size=0;z.on('data',b=>{size+=b.length;if(size>2000000){z.destroy();return}a.push(b)});z.on('end',()=>{const d=Buffer.concat(a);const o={name:n,status:z.statusCode,bytes:d.length};if(n==='webPolicy'){o.policyLengthMatch=d.length===12865;o.policyShaMatch=c.createHash('sha256').update(d).digest('hex')==='d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d'}if(n==='webJs'||n==='gatewayJs'){o.jsShaMatch=c.createHash('sha256').update(d).digest('hex')==='d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd'}r(o)})});x.on('error',e=>r({name:n,errorCategory:e.code||'request_error'}));x.on('timeout',()=>x.destroy(new Error('timeout')))}))).then(a=>process.stdout.write(JSON.stringify(a)))"
    $encoded=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($js))
    $eval="eval(Buffer.from('$encoded','base64').toString())"
    $raw=Invoke-DockerText @('exec',$ApiId,'node','-e',$eval)
    try { return ($raw | ConvertFrom-Json) } catch { throw 'direct_backend_metadata_json_invalid' }
}
function Test-GatewayStaleCause($Baseline,$Current,$Direct,[string]$FailedPath,[int]$FailedStatus,[int]$GatewayStatus) {
    if($FailedStatus -ne 502 -or $GatewayStatus -ne 502){return $false}
    if($null -eq $Baseline -or $null -eq $Current -or $null -eq $Direct){return $false}
    if($Current.networkId -cne $Baseline.networkId -or $Current.networkId -cne $Current.api.networkId -or $Current.networkId -cne $Current.web.networkId -or $Current.networkId -cne $Current.gateway.networkId){return $false}
    if($Current.api.owner -cne 'number-onboarding' -or $Current.web.owner -cne 'number-onboarding' -or $Current.gateway.owner -cne 'number-onboarding'){return $false}
    if($Current.api.project -cne 'leadshug_channels_local' -or $Current.web.project -cne 'leadshug_channels_local' -or $Current.gateway.project -cne 'leadshug_channels_local'){return $false}
    if($Current.gateway.id -cne $Baseline.gateway.id -or $Current.gateway.image -cne $Baseline.gateway.image -or $Current.gateway.service -cne 'gateway' -or $Current.gateway.ip -cne $Baseline.gateway.ip){return $false}
    if($Current.api.id -ceq $Baseline.api.id -or $Current.api.image -cne $newApiImage -or $Current.api.service -cne 'api' -or $Current.web.id -ceq $Baseline.web.id -or $Current.web.image -cne $candidateWebImage -or $Current.web.service -cne 'web'){return $false}
    if(-not $Current.configMatchesTemplate -or $Current.runtimeConfigSha256 -cne $Baseline.runtimeConfigSha256 -or $Current.runtimeConfigSha256 -cne $Current.templateSha256){return $false}
    $list=@($Direct)
    if($FailedPath -ceq '/health'){
        $d=@($list | Where-Object {$_.name -ceq 'apiHealth'}) | Select-Object -First 1
        return ($null -ne $d -and $d.status -eq 200 -and $Current.api.ip -cne $Baseline.api.ip)
    }
    if($FailedPath -ceq '/privacidade.html'){
        $d=@($list | Where-Object {$_.name -ceq 'webPolicy'}) | Select-Object -First 1
        return ($null -ne $d -and $d.status -eq 200 -and $d.policyLengthMatch -eq $true -and $d.policyShaMatch -eq $true -and $Current.web.ip -cne $Baseline.web.ip)
    }
    if($FailedPath -ceq '/assets/index-txvhtd65.js'){
        $d=@($list | Where-Object {$_.name -ceq 'webJs'}) | Select-Object -First 1
        return ($null -ne $d -and $d.status -eq 200 -and $d.jsShaMatch -eq $true -and $Current.web.ip -cne $Baseline.web.ip)
    }
    return $false
}
function Get-GatewayFailureSnapshot([string]$ApiId,[string]$WebId,[string]$GatewayId) {
    $current=Get-TopologySnapshot $ApiId $WebId $GatewayId
    $direct=Get-DirectBackendSnapshot $ApiId
    $gateHealth=@($direct | Where-Object {$_.name -ceq 'gatewayHealth'}) | Select-Object -First 1
    $gatePolicy=@($direct | Where-Object {$_.name -ceq 'gatewayPolicy'}) | Select-Object -First 1
    $gateJs=@($direct | Where-Object {$_.name -ceq 'gatewayJs'}) | Select-Object -First 1
    [ordered]@{topology=$current;direct=$direct;gatewayHealthStatus=$(if($null -ne $gateHealth){$gateHealth.status}else{$null});gatewayPolicyStatus=$(if($null -ne $gatePolicy){$gatePolicy.status}else{$null});gatewayJsStatus=$(if($null -ne $gateJs){$gateJs.status}else{$null})}
}
function Invoke-OneGuardedGatewayReload($Snapshot,[string]$GatewayId) {
    if($script:gatewayReloadAttempted){throw 'gateway_reload_already_attempted'}
    $before=$Snapshot.topology
    $current=Get-TopologySnapshot $script:operationApiId $script:operationWebId $GatewayId
    if($current.gateway.id -cne $before.gateway.id -or $current.gateway.image -cne $before.gateway.image -or $current.gateway.owner -cne 'number-onboarding' -or $current.gateway.service -cne 'gateway' -or $current.runtimeConfigSha256 -cne $before.runtimeConfigSha256 -or $current.networkId -cne $before.networkId){throw 'gateway_identity_or_config_drift_before_reload'}
    try { Invoke-DockerMutation @('exec',$GatewayId,'nginx','-t') } catch { $script:gatewayRecovery.nginxTestExitCode=$script:lastDockerExitCode; throw }
    $script:gatewayRecovery.nginxTestExitCode=$script:lastDockerExitCode
    if($script:lastDockerExitCode -ne 0){throw 'gateway_nginx_test_failed'}
    $current=Get-TopologySnapshot $script:operationApiId $script:operationWebId $GatewayId
    if($current.gateway.id -cne $before.gateway.id -or $current.gateway.image -cne $before.gateway.image -or $current.runtimeConfigSha256 -cne $before.runtimeConfigSha256 -or $current.networkId -cne $before.networkId){throw 'gateway_identity_or_config_drift_before_reload'}
    $script:gatewayReloadAttempted=$true
    try { Invoke-DockerMutation @('exec',$GatewayId,'nginx','-s','reload') } catch { $script:gatewayRecovery.nginxReloadExitCode=$script:lastDockerExitCode; throw }
    $script:gatewayRecovery.nginxReloadExitCode=$script:lastDockerExitCode
    $after=Get-TopologySnapshot $script:operationApiId $script:operationWebId $GatewayId
    if($after.gateway.id -cne $before.gateway.id -or $after.gateway.image -cne $before.gateway.image -or $after.runtimeConfigSha256 -cne $before.runtimeConfigSha256 -or $after.networkId -cne $before.networkId){throw 'gateway_identity_or_config_drift_after_reload'}
    return $after
}

function Assert-PublicWeb([string]$Origin) {
    [byte[]]$source=[IO.File]::ReadAllBytes($policyPath)
    if ($source.Length -ne $expectedPolicyBytes -or (Get-FileHash -LiteralPath $policyPath -Algorithm SHA256).Hash.ToLowerInvariant() -cne $expectedPolicySha) { throw 'approved_policy_source_mismatch' }
    $page=Get-NoSessionResponse ($Origin + '/privacidade.html')
    if ($page.status -ne 200 -or $page.redirected -or $page.headers.ContainsKey('Set-Cookie') -or $page.headers['Content-Type'] -notmatch '^text/html(?:\s*;|$)') { throw 'privacy_http_status_content_type_or_cookie_check_failed' }
    if ($page.body.Length -ne $expectedPolicyBytes -or ( [Convert]::ToBase64String($page.body) -cne [Convert]::ToBase64String($source))) { throw 'privacy_response_bytes_mismatch' }
    $html=[Text.UTF8Encoding]::new($false,$true).GetString($page.body)
    if ($html -notmatch '(?is)<meta\s+charset=["'']utf-8["'']' -or $html -notmatch '(?is)<meta\s+name=["'']referrer["'']\s+content=["'']no-referrer["'']' -or $html -notmatch '(?is)<meta\s+name=["'']robots["'']\s+content=["''][^"'']*noindex' -or $html -notmatch '(?is)<meta\s+http-equiv=["'']Content-Security-Policy["'']\s+content=') { throw 'privacy_policy_meta_check_failed' }
    if ($html -match '(?is)<(?:script|img|iframe|video|audio|source|link)\b') { throw 'privacy_automatic_resource_element_found' }
    foreach ($path in @('/','/health')) { $r=Get-NoSessionResponse ($Origin+$path); if ($r.status -ne 200 -or $r.redirected -or $r.headers.ContainsKey('Set-Cookie')) { throw 'public_root_or_health_check_failed' } }
    $js=Get-NoSessionResponse ($Origin+'/assets/index-txvhtd65.js')
    if ($js.status -ne 200 -or $js.redirected -or $js.headers.ContainsKey('Set-Cookie') -or (Get-FileHash -InputStream ([IO.MemoryStream]::new($js.body)) -Algorithm SHA256).Hash.ToLowerInvariant() -cne $expectedJsSha) { throw 'public_js_check_failed' }
    return [ordered]@{ policyStatus=200; contentTypeHtml=$true; strictUtf8AndCharsetMeta=$true; policyBytes=$page.body.Length; policySha256=$expectedPolicySha; noSetCookie=$true; noRedirect=$true; cspMetaPresent=$true; referrerMetaPresent=$true; noindexMetaPresent=$true; noDeclaredAutomaticResourceElements=$true; rootStatus=200; healthStatus=200; jsSha256=$expectedJsSha; authOrCookieSent=$false }
}

if($RunPredicateTests){
    $base=[ordered]@{networkId='n1';api=[ordered]@{id='a1';image=$newApiImage;owner='number-onboarding';project='leadshug_channels_local';service='api';networkId='n1';ip='172.0.0.2'};web=[ordered]@{id='w1';image=$oldWebImage;owner='number-onboarding';project='leadshug_channels_local';service='web';networkId='n1';ip='172.0.0.3'};gateway=[ordered]@{id='g1';image='gi';owner='number-onboarding';project='leadshug_channels_local';service='gateway';networkId='n1';ip='172.0.0.4'};runtimeConfigSha256='cfg';templateSha256='cfg';configMatchesTemplate=$true}
    $cur=ConvertFrom-Json -InputObject (ConvertTo-Json -InputObject $base -Depth 5)
    $cur.api.id='a2';$cur.api.ip='172.0.0.8';$cur.web.id='w2';$cur.web.image=$candidateWebImage;$cur.web.ip='172.0.0.9'
    $direct=@([ordered]@{name='apiHealth';status=200},[ordered]@{name='webPolicy';status=200;policyLengthMatch=$true;policyShaMatch=$true},[ordered]@{name='webJs';status=200;jsShaMatch=$true})
    $positiveApi=Test-GatewayStaleCause $base $cur $direct '/health' 502 502
    $positiveWeb=Test-GatewayStaleCause $base $cur $direct '/privacidade.html' 502 502
    $sameIp=ConvertFrom-Json -InputObject (ConvertTo-Json -InputObject $cur -Depth 5);$sameIp.api.ip=$base.api.ip
    $wrongNetwork=ConvertFrom-Json -InputObject (ConvertTo-Json -InputObject $cur -Depth 5);$wrongNetwork.networkId='n2'
    $wrongGateway=ConvertFrom-Json -InputObject (ConvertTo-Json -InputObject $cur -Depth 5);$wrongGateway.gateway.id='g2'
    $wrongConfig=ConvertFrom-Json -InputObject (ConvertTo-Json -InputObject $cur -Depth 5);$wrongConfig.runtimeConfigSha256='other'
    $wrongOwner=ConvertFrom-Json -InputObject (ConvertTo-Json -InputObject $cur -Depth 5);$wrongOwner.gateway.owner='other'
    $wrongImage=ConvertFrom-Json -InputObject (ConvertTo-Json -InputObject $cur -Depth 5);$wrongImage.web.image='other'
    $wrongDirect=@([ordered]@{name='webPolicy';status=200;policyLengthMatch=$true;policyShaMatch=$false})
    $negative=[ordered]@{
        sameRouteIp=( -not (Test-GatewayStaleCause $base $sameIp $direct '/health' 502 502) )
        networkDrift=( -not (Test-GatewayStaleCause $base $wrongNetwork $direct '/health' 502 502) )
        gatewayIdDrift=( -not (Test-GatewayStaleCause $base $wrongGateway $direct '/health' 502 502) )
        configDrift=( -not (Test-GatewayStaleCause $base $wrongConfig $direct '/health' 502 502) )
        gatewayOwnerDrift=( -not (Test-GatewayStaleCause $base $wrongOwner $direct '/health' 502 502) )
        backendImageDrift=( -not (Test-GatewayStaleCause $base $wrongImage $direct '/health' 502 502) )
        wrongPolicy=( -not (Test-GatewayStaleCause $base $cur $wrongDirect '/privacidade.html' 502 502) )
        non502=( -not (Test-GatewayStaleCause $base $cur $direct '/health' 200 502) )
        unsupportedRoute=( -not (Test-GatewayStaleCause $base $cur $direct '/unknown' 502 502) )
    }
    $ok=$positiveApi -and $positiveWeb -and @($negative.Values | Where-Object {$_ -ne $true}).Count -eq 0
    [ordered]@{result=$(if($ok){'predicate_tests_passed'}else{'predicate_tests_failed'});positiveApiRoute=$positiveApi;positivePolicyRoute=$positiveWeb;negativeCases=$negative;negativeCaseCount=$negative.Count;dockerInvocations=0;networkRequests=0;privateReads=0}|ConvertTo-Json -Depth 4
    if(-not $ok){exit 1};exit 0
}

if (-not $ApplyAll) {
    [ordered]@{ result='plan_only_no_private_read_or_mutation'; apiImage=$newApiImage; oldWebImage=$oldWebImage; candidateWebImage=$candidateWebImage; apiComposeTail=@('up','-d','--no-build','--no-deps','--force-recreate','api'); webComposeTail=@('up','-d','--no-build','--no-deps','--force-recreate','web') } | ConvertTo-Json -Depth 4
    exit 0
}

$proof=Get-Content -LiteralPath $AcceptedProofPath -Raw | ConvertFrom-Json
if ($proof.operationAuthority -cne 'GO' -or $proof.rootOutcome -cne 'GO' -or $proof.rootAccepted -ne $true) { throw 'cp64_root_operation_GO_missing' }
if ($proof.windows.normalTls -ne $true -or $proof.wsl.normalTls -ne $true -or $proof.windows.redirected -ne $false -or $proof.wsl.redirected -ne $false) { throw 'new_transport_proof_incomplete' }
if ($proof.windows.rootStatus -ne 200 -or $proof.windows.healthStatus -ne 200 -or $proof.windows.jsSha256 -cne $expectedJsSha -or $proof.wsl.rootStatus -ne 200 -or $proof.wsl.healthStatus -ne 200 -or $proof.wsl.jsSha256 -cne $expectedJsSha) { throw 'new_transport_public_asset_proof_mismatch' }
Assert-DockerExecutableAvailable
$hostName=[string]$proof.hostname
if ($hostName -notmatch '^[a-z0-9-]+\.trycloudflare\.com$') { throw 'new_hostname_invalid' }
$origin='https://'+$hostName

$original=$null; $replacement=$null; $oldOrigin=$null; $initialAcl=$null; $rollbackTagCreated=$false
try {
    $script:stage='preflight_resources'; Write-SafeStageReceipt 'started' 'none'
    Assert-PreservedResources 'none'
    $selectedApi=Get-ComposeServiceId 'api'; $selectedWeb=Get-ComposeServiceId 'web'
    if ($selectedApi -cne $baselineContainers.api -or $selectedWeb -cne $baselineContainers.web) { throw 'compose_selection_changed_from_accepted_baseline' }
    $apiBefore=Assert-SelectedService 'api' $baselineContainers.api $newApiImage 'healthy'
    $webBefore=Assert-SelectedService 'web' $baselineContainers.web $oldWebImage
    $script:apiContainerId=$apiBefore.id; $script:webContainerId=$webBefore.id
    $script:baselineTopology=Get-TopologySnapshot $apiBefore.id $webBefore.id $baselineContainers.gateway
    if ((Get-ImageId $apiTag) -cne $newApiImage -or (Get-ImageId $webTag) -cne $oldWebImage -or (Get-ImageId $webCandidateTag) -cne $candidateWebImage -or (Get-ImageId $candidateWebImage) -cne $candidateWebImage) { throw 'image_tag_or_candidate_guard_mismatch' }
    $existingRollback=Invoke-DockerText @('image','ls','--quiet','--no-trunc','--filter',('reference='+$webRollbackTag))
    if (-not [String]::IsNullOrWhiteSpace($existingRollback)) { throw 'rollback_tag_already_exists_refuse_overwrite' }

    $script:stage='origin_preflight'; Write-SafeStageReceipt 'started' 'none'
    [byte[]]$privateBytes=[IO.File]::ReadAllBytes($envPath)
    $initialAcl=(Get-Acl -LiteralPath $envPath).Sddl
    $edit=New-OriginEdit $privateBytes $hostName; $original=$edit.original; $replacement=$edit.replacement; $oldOrigin=$edit.oldOrigin
    $script:stage='origin_write'; Write-SafeStageReceipt 'started' 'none'
    $null=Set-OriginBytesCAS $original $replacement
    if ((Get-Acl -LiteralPath $envPath).Sddl -cne $initialAcl) { throw 'origin_initial_security_metadata_not_preserved' }
    Write-SafeStageReceipt 'success' 'none'

    $script:stage='api_recreate'; Write-SafeStageReceipt 'started' 'none'
    $null=Assert-SelectedService 'api' $baselineContainers.api $newApiImage 'healthy'
    if ((Get-ImageId $apiTag) -cne $newApiImage) { throw 'api_tag_changed_before_recreate' }
    $script:apiMutationStarted=$true
    Invoke-ComposeUp 'api' $origin
    $newApiId=Get-ComposeServiceId 'api'
    if ($newApiId -ceq $baselineContainers.api) { throw 'api_force_recreate_did_not_change_container_id' }
    $script:operationApiId=$newApiId; $script:apiContainerId=$newApiId
    $null=Assert-OwnedService $newApiId $newApiImage 'api' 'running'
    $newApiId=Wait-ApiHealthy $origin $newApiId
    Assert-PreservedResources 'api'
    Write-SafeStageReceipt 'success' 'none'

    $script:stage='web_rollback_tag'; Write-SafeStageReceipt 'started' 'none'
    $null=Assert-SelectedService 'web' $baselineContainers.web $oldWebImage
    $existingRollback=Invoke-DockerText @('image','ls','--quiet','--no-trunc','--filter',('reference='+$webRollbackTag))
    if (-not [String]::IsNullOrWhiteSpace($existingRollback)) { throw 'rollback_tag_appeared_refuse_overwrite' }
    Invoke-DockerMutation @('tag',$oldWebImage,$webRollbackTag)
    if ((Get-ImageId $webRollbackTag) -cne $oldWebImage) { throw 'rollback_tag_image_mismatch' }
    $rollbackTagCreated=$true
    Write-SafeStageReceipt 'success' 'none'

    $script:stage='web_service_tag'; Write-SafeStageReceipt 'started' 'none'
    $null=Assert-SelectedService 'web' $baselineContainers.web $oldWebImage
    if ((Get-ImageId $webTag) -cne $oldWebImage -or (Get-ImageId $webRollbackTag) -cne $oldWebImage) { throw 'web_tag_changed_before_activation' }
    Invoke-DockerMutation @('tag',$candidateWebImage,$webTag)
    $script:webTagChanged=$true
    if ((Get-ImageId $webTag) -cne $candidateWebImage) { throw 'web_service_tag_candidate_mismatch' }
    Write-SafeStageReceipt 'success' 'none'

    $script:stage='web_recreate'; Write-SafeStageReceipt 'started' 'none'
    $null=Assert-SelectedService 'web' $baselineContainers.web $oldWebImage
    if ((Get-ImageId $webTag) -cne $candidateWebImage) { throw 'web_service_tag_candidate_mismatch_before_recreate' }
    $script:webMutationStarted=$true
    Invoke-ComposeUp 'web' $origin
    $webId=Get-ComposeServiceId 'web'; $webFacts=Get-ContainerFacts $webId
    if ($webId -ceq $baselineContainers.web) { throw 'web_force_recreate_did_not_change_container_id' }
    $script:operationWebId=$webId; $script:webContainerId=$webId
    $null=Assert-OwnedService $webId $candidateWebImage 'web' 'running'
    Assert-PreservedResources 'api+web'
    $apiAfterWeb=Get-ContainerFacts $newApiId
    if ($apiAfterWeb.id -cne $newApiId -or $apiAfterWeb.image -cne $newApiImage -or $apiAfterWeb.state -cne 'running' -or $apiAfterWeb.health -cne 'healthy' -or $apiAfterWeb.owner -cne 'number-onboarding' -or $apiAfterWeb.project -cne 'leadshug_channels_local' -or $apiAfterWeb.service -cne 'api') { throw 'api_changed_during_web_activation' }
    $public=Assert-PublicWeb $origin
    $script:stage='complete'; Write-SafeStageReceipt 'success' 'none'
    [ordered]@{ result='success_exact_policy_and_regression_probes_passed'; origin=$origin; apiContainerId=$newApiId; apiImage=$newApiImage; webContainerId=$webId; webImage=$candidateWebImage; public=$public; preservedContainersAndVolumes=$true; rollbackTag=$webRollbackTag; rollbackTagPreserved=$true } | ConvertTo-Json -Depth 6
} catch {
    $failure='unexpected_guard_or_operation_failure'
    if ($_.Exception.Message -match '^[a-z][a-z0-9_]+$') { $failure=$_.Exception.Message }
    $script:lastFailureCategory=$failure
    $script:failedStage=$script:stage
    $script:originalExitCode=$script:lastDockerExitCode
    $script:originalHttpStatus=$script:lastHttpStatus
    $snapshot=[ordered]@{apiSelectedId=$null;apiImage=$null;webSelectedId=$null;webImage=$null;capture='partial_or_unavailable';gatewayCause='not_applicable'}
    try {
        $sid=Get-ComposeServiceId 'api'; $sf=Get-ContainerFacts $sid
        $snapshot.apiSelectedId=$sid; $snapshot.apiImage=$sf.image
        $sid=Get-ComposeServiceId 'web'; $sf=Get-ContainerFacts $sid
        $snapshot.webSelectedId=$sid; $snapshot.webImage=$sf.image
        $snapshot.capture='complete'
    } catch { $snapshot.capture='partial_or_unavailable' }
    if($script:originalHttpStatus -eq 502 -and $null -ne $script:baselineTopology -and $script:apiMutationStarted -and $script:webMutationStarted -and $null -ne $script:operationApiId -and $null -ne $script:operationWebId){
        $script:gatewayRecovery=[ordered]@{causalRecoveryEntered=$false;failedPath=$script:lastHttpPath;originalHttpStatus=$script:originalHttpStatus;originalNativeExitCode=$script:originalExitCode;diagnosticCapture='not_started';causalPredicateMatched=$false;nginxTestExitCode=$null;nginxReloadExitCode=$null;postReloadPublicCheck='not_run';failureCategory=$null}
        try {
            $snapshot.gatewayDiagnostic=Get-GatewayFailureSnapshot $script:operationApiId $script:operationWebId $baselineContainers.gateway
            $script:gatewayRecovery.diagnosticCapture='complete'
            $script:failureSnapshot=$snapshot
            $script:stage='gateway_502_diagnostic'
            Write-SafeStageReceipt 'diagnostic_captured_before_reload_gate' $failure
            $gatewayFailedRouteStatus=$null
            if($script:lastHttpPath -ceq '/health'){$gatewayFailedRouteStatus=$snapshot.gatewayDiagnostic.gatewayHealthStatus}
            elseif($script:lastHttpPath -ceq '/privacidade.html'){$gatewayFailedRouteStatus=$snapshot.gatewayDiagnostic.gatewayPolicyStatus}
            elseif($script:lastHttpPath -ceq '/assets/index-txvhtd65.js'){$gatewayFailedRouteStatus=$snapshot.gatewayDiagnostic.gatewayJsStatus}
            $script:gatewayRecovery.causalPredicateMatched=Test-GatewayStaleCause $script:baselineTopology $snapshot.gatewayDiagnostic.topology $snapshot.gatewayDiagnostic.direct $script:lastHttpPath $script:originalHttpStatus $gatewayFailedRouteStatus
            if($script:gatewayRecovery.causalPredicateMatched){
                $script:gatewayRecovery.causalRecoveryEntered=$true
                $null=Invoke-OneGuardedGatewayReload $snapshot.gatewayDiagnostic $baselineContainers.gateway
                $script:lastHttpStatus=$script:originalHttpStatus
                try { $publicAfterReload=Assert-PublicWeb $origin; $script:gatewayRecovery.postReloadPublicCheck='passed'; $script:lastHttpStatus=$script:originalHttpStatus
                    $script:stage='complete_after_one_gateway_reload'; Write-SafeStageReceipt 'success_after_guarded_gateway_reload' $failure
                    Assert-PreservedResources 'api+web'
                    $null=Assert-OwnedService $script:operationApiId $newApiImage 'api' 'running' 'healthy'
                    $null=Assert-OwnedService $script:operationWebId $candidateWebImage 'web' 'running'
                    [ordered]@{result='success_after_one_guarded_gateway_reload';origin=$origin;apiContainerId=$script:operationApiId;apiImage=$newApiImage;webContainerId=$script:operationWebId;webImage=$candidateWebImage;public=$publicAfterReload;originalFailureCategory=$failure;originalNativeExitCode=$script:originalExitCode;originalHttpStatus=$script:originalHttpStatus;failedPath=$script:gatewayRecovery.failedPath;gatewayRecovery=$script:gatewayRecovery;preservedContainersAndVolumes=$true;rollbackTag=$webRollbackTag;rollbackTagPreserved=$true}|ConvertTo-Json -Depth 8
                    exit 0
                } catch { $script:gatewayRecovery.postReloadPublicCheck='failed'; $script:lastHttpStatus=$script:originalHttpStatus; $script:gatewayRecovery.failureCategory='public_probe_failed_after_single_reload' }
            }
        } catch { $script:gatewayRecovery.failureCategory='gateway_diagnostic_or_guard_failed' }
        if($script:receiptWriteFailure){$snapshot.gatewayCause='diagnostic_receipt_failed_no_reload'}
        else{$snapshot.gatewayCause=$(if($script:gatewayReloadAttempted){'reload_attempted_but_public_probe_failed'}elseif($script:gatewayRecovery.causalPredicateMatched){'causal_conditions_matched_reload_guard_not_completed'}elseif($script:gatewayRecovery.diagnosticCapture -eq 'complete'){'causal_conditions_not_proven'}else{'diagnostic_capture_incomplete'})}
        $snapshot.gatewayRecovery=$script:gatewayRecovery
    }
    $script:failureSnapshot=$snapshot
    $script:stage='failure_before_rollback'
    Write-SafeStageReceipt 'failed' $failure -NoThrow
    # This copy intentionally refuses any rollback whose currently selected
    # service/tag is not the pinned baseline or this invocation's captured ID.
    $webRollback='not_needed'; $apiRollback='not_needed'; $originRollback='not_needed'
    if ($script:originTransactionIncomplete) { $originRollback='incomplete_write_recovery_unverified' }
    elseif ($script:originWriteOutcome -eq 'write_interrupted_restored') { $originRollback='verified_original_after_interrupted_write' }
    try {
        if ($script:webTagChanged) {
            $selected=Get-ComposeServiceId 'web'; $facts=Get-ContainerFacts $selected
            $expectedWebContainer=$script:operationWebId
            if ($null -eq $expectedWebContainer) {
                if ($selected -cne $baselineContainers.web -or $facts.image -cne $oldWebImage) { throw 'web_rollback_refused_unknown_current_id' }
            } elseif ($selected -cne $expectedWebContainer -or $facts.image -cne $candidateWebImage) { throw 'web_rollback_refused_unknown_current_id' }
            if ($facts.owner -cne 'number-onboarding' -or $facts.project -cne 'leadshug_channels_local' -or $facts.service -cne 'web' -or (Get-ImageId $webTag) -cne $candidateWebImage -or (Get-ImageId $webRollbackTag) -cne $oldWebImage) { throw 'web_rollback_refused_ownership_or_tag_drift' }
            Invoke-DockerMutation @('tag',$webRollbackTag,$webTag)
            if ((Get-ImageId $webTag) -cne $oldWebImage) { throw 'web_rollback_tag_postcondition_failed' }
            if ($script:webMutationStarted -and $null -ne $script:operationWebId) {
                if ((Get-ComposeServiceId 'web') -cne $script:operationWebId) { throw 'web_rollback_refused_selected_id_changed' }
                Invoke-ComposeUp 'web' $origin
                $restoredWeb=Get-ComposeServiceId 'web'; $wf=Assert-OwnedService $restoredWeb $oldWebImage 'web' 'running'
                if ($restoredWeb -ceq $script:operationWebId) { throw 'web_rollback_container_id_not_replaced' }
                $script:webContainerId=$restoredWeb
            } else { $wf=Assert-SelectedService 'web' $baselineContainers.web $oldWebImage }
            $webRollback='verified'
        }
    } catch { $webRollback='refused_or_unverified' }

    try {
        if ($script:originChanged) {
            if (-not (Test-OriginIs $replacement)) { throw 'origin_rollback_refused_concurrent_bytes' }
            $currentApi=Get-ComposeServiceId 'api'
            $af=Get-ContainerFacts $currentApi
            if ($script:apiMutationStarted -and $null -ne $script:operationApiId) {
                if ($currentApi -cne $script:operationApiId -or $af.image -cne $newApiImage -or $af.owner -cne 'number-onboarding' -or $af.project -cne 'leadshug_channels_local' -or $af.service -cne 'api' -or (Get-ImageId $apiTag) -cne $newApiImage) { throw 'api_rollback_refused_unknown_current_id_or_tag' }
            } elseif ($currentApi -cne $baselineContainers.api -or $af.image -cne $newApiImage -or $af.owner -cne 'number-onboarding' -or $af.project -cne 'leadshug_channels_local' -or $af.service -cne 'api') { throw 'api_rollback_refused_unknown_current_id' }
            $null=Set-OriginBytesCAS $replacement $original
            if ((Get-Acl -LiteralPath $envPath).Sddl -cne $initialAcl) { throw 'origin_rollback_security_metadata_mismatch' }
            if ($script:apiMutationStarted -and $null -ne $script:operationApiId) {
                if ((Get-ComposeServiceId 'api') -cne $script:operationApiId) { throw 'api_rollback_refused_selected_id_changed' }
                Invoke-ComposeUp 'api' $oldOrigin
                $restoredApi=Get-ComposeServiceId 'api'; $rf=Assert-OwnedService $restoredApi $newApiImage 'api' 'running'
                if ($restoredApi -ceq $script:operationApiId) { throw 'api_rollback_container_id_not_replaced' }
                $null=Wait-ApiHealthy $oldOrigin $restoredApi
                $script:apiContainerId=$restoredApi
            } else {
                $null=Assert-SelectedService 'api' $baselineContainers.api $newApiImage 'healthy'
                $check="if(process.env.NODE_ENV==='production'&&process.env.WEB_ORIGIN==='$oldOrigin'){process.stdout.write('true')}else{process.stdout.write('false')}"
                if ((Invoke-DockerText @('exec',$currentApi,'node','-e',$check)) -cne 'true') { throw 'api_old_public_inputs_boolean_failed' }
            }
            $originRollback='verified_bytes_security_and_old_origin'
            $apiRollback='verified_same_image_health_and_old_origin'
        }
    } catch { if ($originRollback -eq 'not_needed') { $originRollback='refused_or_unverified' }; if ($apiRollback -eq 'not_needed' -and $script:apiMutationStarted) { $apiRollback='refused_or_unverified' } }
    $preservedAfterRollback=$false
    try { Assert-PreservedResources 'rollback'; $preservedAfterRollback=$true } catch { $script:lastFailureCategory='preserved_resource_postcondition_failed'; $script:preservationVerified=$false }
    $apiPostcondition=$false; $webPostcondition=$false
    try {
        $currentApi=Get-ComposeServiceId 'api'; $af=Assert-OwnedService $currentApi $newApiImage 'api' 'running' 'healthy'
        if ((Get-ImageId $apiTag) -cne $newApiImage) { throw 'rollback_api_tag_mismatch' }
        if ($null -ne $oldOrigin) {
            $check="if(process.env.NODE_ENV==='production'&&process.env.WEB_ORIGIN==='$oldOrigin'){process.stdout.write('true')}else{process.stdout.write('false')}"
            if ((Invoke-DockerText @('exec',$currentApi,'node','-e',$check)) -cne 'true') { throw 'rollback_api_old_origin_boolean_false' }
        }
        $apiPostcondition=$true
    } catch { $apiPostcondition=$false }
    try {
        $currentWeb=Get-ComposeServiceId 'web'; $wf=Assert-OwnedService $currentWeb $oldWebImage 'web' 'running'
        if ((Get-ImageId $webTag) -cne $oldWebImage) { throw 'rollback_web_tag_mismatch' }
        $webPostcondition=$true
    } catch { $webPostcondition=$false }
    $script:rollbackWebOutcome=$webRollback; $script:rollbackApiOutcome=$apiRollback
    $script:stage='rollback_postconditions'
    $originOutcomeOk=($originRollback -in @('not_needed','verified_original_after_interrupted_write','verified_bytes_security_and_old_origin'))
    $rollbackOk=($webRollback -in @('not_needed','verified') -and $originOutcomeOk -and -not $script:originTransactionIncomplete -and $apiRollback -in @('not_needed','verified_same_image_health_and_old_origin') -and $apiPostcondition -and $webPostcondition -and $preservedAfterRollback)
    Write-SafeStageReceipt $(if($rollbackOk){'rollback_verified'}else{'rollback_incomplete_stop'}) $failure -NoThrow
    [ordered]@{ result=$(if($rollbackOk){'failed_then_rollback_verified'}else{'failed_rollback_incomplete_stop_for_root'}); originalFailureCategory=$failure; originalNativeExitCode=$script:originalExitCode; failureHttpStatus=$script:originalHttpStatus; failedStage=$script:failedStage; preRollbackSnapshot=$snapshot; gatewayRecovery=$script:gatewayRecovery; rollbackWeb=$webRollback; rollbackApi=$apiRollback; rollbackOrigin=$originRollback; apiPostconditionVerified=$apiPostcondition; webPostconditionVerified=$webPostcondition; preservedResourcesVerified=$preservedAfterRollback; originTransactionIncomplete=$script:originTransactionIncomplete; receiptWriteFailure=$script:receiptWriteFailure; gatewayReloadAttempted=$script:gatewayReloadAttempted; noGatewayReload=(-not $script:gatewayReloadAttempted); noGatewayRecreate=$true; privateOldOriginExposed=$false; noProviderDatabaseOrVolumeActions=$true } | ConvertTo-Json -Depth 5
    exit 2
}
