[CmdletBinding()]
param(
    [switch]$ApplyApiOrigin,
    [switch]$RunByteCasFixtures,
    [string]$AcceptedProofPath
)
$ErrorActionPreference='Stop'
$repo='C:\unifast\leadshug\leadshug_now_docker'
$evidenceDir=Join-Path $repo 'foundation_documentation\artifacts\reviews\leadshug-number-onboarding-20261015\evidence'
$stageReceiptPath=Join-Path $evidenceDir 'cp73-api-origin-stage.json'
$envPath=Join-Path $repo '.env.testing'
$newApiImage='sha256:fe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821'
$apiTag='leadshug_channels_local-api'
$apiId='005529386c8a7ab499cd779942ce541bb90cd3a770b8436b41509d2655e54857'
$webImage='sha256:cfd5e58b91a67d2fae4f37759274a34209cd2501082650a49545a60a12642361'
$webId='9aa55b6681a8480dbfd7cbf2a51ab8571035603b288b52e6798d93741af01093'
$gatewayImage='sha256:76090a34b858323b6ab169711adc08253b5bee7123a973dc581ed46b643bc109'
$gatewayId='0c48d94e9fe5b4ad75efd304db2752dfa4cab3befc59b9f736574d6cd551eea3'
$expectedGatewayConfigSha='6d4563cc5f5823bdb1177f350c942dc2472fc70133aef5b177fa4b57c5c9f1a0'
$expectedJsSha='d14343604557296f2ed62c1df47d9c80d81c323abafd89ccbb64a6a0746ff4bd'
$expectedHost='estimation-editions-knee-inclusion.trycloudflare.com'
$knownOldOrigin='https://addressing-mar-perform-hormone.trycloudflare.com'
$composePrefix=@('compose','--project-name','leadshug_channels_local','--env-file',(Join-Path $repo '.env.testing'),'-f',(Join-Path $repo 'docker-compose.yml'),'-f',(Join-Path $repo 'docker-compose.channels.yml'),'--profile','channels-local')
$baselineContainers=[ordered]@{
 api=$apiId
 gateway=$gatewayId
 web=$webId
 evolution='cf749491f7149dc46ec4db597b2d9c12faf918dd4f05b5512ba75adaf8e29ea4'
 evolutionRedis='3b2e8d153d794a768ea87cb4f9cda7ba15dde242e2b8027bd372a475a9c26fbb'
 evolutionPostgres='150de898c3d9aa189ca0719eed7a65b95d95d8b948244e66b059a55f4554135a'
 postgres='4fcd87b431339e3b65a40beafa27db86cdc978ca79f71b911199f7090c837495'
}
$preservedImages=[ordered]@{
 gateway=$gatewayImage
 evolution='sha256:385a3c4bedf42c66b46b43d06aae8712620144a84aa3b2c831b30c68435ab27c'
 evolutionRedis='sha256:f84b0c4678011602b9b98c227a4dcd5468bf8b088b02fdd4165cb7758bad8058'
 evolutionPostgres='sha256:80f4c7a5e91618546dce5b4fe60cf03b14c0f9efa7e40157278d122772ced8d2'
 postgres='sha256:80f4c7a5e91618546dce5b4fe60cf03b14c0f9efa7e40157278d122772ced8d2'
}
$expectedVolumes=@('leadshug_channels_local_evolution_instances','leadshug_channels_local_evolution_pg_data','leadshug_channels_local_evolution_redis_data','leadshug_channels_local_leadshug_arquivos','leadshug_channels_local_leadshug_pg_data')
$script:stage='preflight';$script:lastDockerExitCode=$null;$script:lastHttpStatus=$null;$script:lastHttpPath=$null
$script:operationApiId=$null;$script:originWriteOutcome='not_started';$script:originChanged=$false;$script:originTransactionIncomplete=$false
$script:preservationVerified=$false;$script:receiptWriteFailure=$false;$script:events=@();$script:gatewayReloadAttempted=$false;$script:apiMutationStarted=$false
function Write-Stage([string]$Status,[string]$Failure,[switch]$NoThrow){
 $row=[ordered]@{capturedAtUtc=[DateTime]::UtcNow.ToString('o');stage=$script:stage;status=$Status;failureCategory=$Failure;nativeExitCode=$script:lastDockerExitCode;httpStatus=$script:lastHttpStatus;apiSelectedId=$script:operationApiId;apiImage=$newApiImage;originWriteOutcome=$script:originWriteOutcome;preservationVerified=$script:preservationVerified;gatewayReloadAttempted=$script:gatewayReloadAttempted;privateValuesOrBodiesPersisted=$false}
 $script:events+=,$row
 try{[IO.File]::WriteAllText($stageReceiptPath,([ordered]@{checkpoint='cp73-api-origin-stage';events=@($script:events)}|ConvertTo-Json -Depth 5),[Text.UTF8Encoding]::new($false))}
 catch{$script:receiptWriteFailure=$true;if(-not $NoThrow){throw 'stage_receipt_write_failed'}}
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
        Invoke-DockerMutation (@($composePrefix) + @('up','-d','--pull','never','--no-build','--no-deps','--force-recreate',$Service))
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

function Get-NoSessionResponse([string]$Uri,[int]$MaxBytes=400000){
 Add-Type -AssemblyName System.Net.Http
 $handler=[Net.Http.HttpClientHandler]::new();$handler.AllowAutoRedirect=$false;$handler.UseCookies=$false
 $client=[Net.Http.HttpClient]::new($handler);$client.Timeout=[TimeSpan]::FromSeconds(12);$client.MaxResponseContentBufferSize=$MaxBytes
 try{
  $script:lastHttpPath=([Uri]$Uri).AbsolutePath
  $r=$client.GetAsync($Uri).GetAwaiter().GetResult()
  try{$script:lastHttpStatus=[int]$r.StatusCode;$b=$r.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult();if($b.Length -gt $MaxBytes){throw 'http_response_over_limit'}
   return [ordered]@{status=[int]$r.StatusCode;body=$b;contentType=[string]$r.Content.Headers.ContentType;noSetCookie=(-not($r.Headers.Contains('Set-Cookie') -or $r.Content.Headers.Contains('Set-Cookie')));redirected=($r.StatusCode -ge 300 -and $r.StatusCode -lt 400)}
  }finally{$r.Dispose()}
 }finally{$client.Dispose();$handler.Dispose()}
}
function Assert-WebPreserved {
 $f=Assert-SelectedService 'web' $webId $webImage
 if($f.id -cne $webId){throw 'web_id_changed'}
}
function Assert-CurrentApi([string]$ExpectedId){
 $selected=Get-ComposeServiceId 'api'
 if($selected -cne $ExpectedId){throw 'api_compose_selected_id_mismatch'}
 $f=Assert-OwnedService $selected $newApiImage 'api' 'running'
 if((Get-ImageId $apiTag) -cne $newApiImage){throw 'api_image_tag_mismatch'}
 return $f
}
function Get-DirectApiHealth([string]$Id){
 $js="const h=require('http');const q=h.get('http://127.0.0.1:3000/health',{timeout:4000},r=>{r.resume();process.stdout.write(String(r.statusCode))});q.on('error',()=>process.stdout.write('0'));q.on('timeout',()=>{q.destroy();process.stdout.write('0')})"
 $encoded=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($js))
 $eval="eval(Buffer.from('$encoded','base64').toString())"
 $raw=Invoke-DockerText @('exec',$Id,'node','-e',$eval)
 if($raw -notmatch '^\d{1,3}$'){throw 'direct_api_health_status_invalid'}
 return [int]$raw
}
function Invoke-OneGuardedGatewayReload($Baseline,$Current,[int]$PublicStatus,[int]$DirectStatus){
 if($script:gatewayReloadAttempted){throw 'gateway_reload_already_attempted'}
 if($PublicStatus -ne 502 -or $DirectStatus -ne 200){throw 'gateway_reload_causal_status_guard_failed'}
 if($Current.networkId -cne $Baseline.networkId -or $Current.api.networkId -cne $Baseline.networkId -or $Current.web.networkId -cne $Baseline.networkId -or $Current.gateway.networkId -cne $Baseline.networkId){throw 'gateway_reload_network_guard_failed'}
 if($Current.api.id -ceq $Baseline.api.id -or $Current.api.ip -ceq $Baseline.api.ip -or $Current.api.image -cne $newApiImage -or $Current.api.owner -cne 'number-onboarding' -or $Current.api.project -cne 'leadshug_channels_local' -or $Current.api.service -cne 'api'){throw 'gateway_reload_api_identity_or_ip_guard_failed'}
 if($Current.gateway.id -cne $Baseline.gateway.id -or $Current.gateway.image -cne $gatewayImage -or $Current.gateway.owner -cne 'number-onboarding' -or $Current.gateway.project -cne 'leadshug_channels_local' -or $Current.gateway.service -cne 'gateway' -or $Current.runtimeConfigSha256 -cne $expectedGatewayConfigSha -or $Current.templateSha256 -cne $expectedGatewayConfigSha){throw 'gateway_reload_identity_or_static_config_guard_failed'}
 Assert-PreservedResources 'api';Assert-WebPreserved
 Invoke-DockerMutation @('exec',$gatewayId,'nginx','-t')
 if($script:lastDockerExitCode -ne 0){throw 'gateway_nginx_test_failed'}
 $fresh=Get-TopologySnapshot $script:operationApiId $webId $gatewayId
 if($fresh.gateway.id -cne $Baseline.gateway.id -or $fresh.gateway.image -cne $gatewayImage -or $fresh.runtimeConfigSha256 -cne $expectedGatewayConfigSha -or $fresh.networkId -cne $Baseline.networkId -or $fresh.api.ip -cne $Current.api.ip){throw 'gateway_reload_precondition_drift'}
 $script:gatewayReloadAttempted=$true
 Invoke-DockerMutation @('exec',$gatewayId,'nginx','-s','reload')
 if($script:lastDockerExitCode -ne 0){throw 'gateway_graceful_reload_failed'}
 $after=Get-TopologySnapshot $script:operationApiId $webId $gatewayId
 if($after.gateway.id -cne $Baseline.gateway.id -or $after.gateway.image -cne $gatewayImage -or $after.runtimeConfigSha256 -cne $expectedGatewayConfigSha -or $after.networkId -cne $Baseline.networkId){throw 'gateway_reload_postcondition_drift'}
 return $after
}
function Get-PublicApiHealth([string]$Origin){
 $r=Get-NoSessionResponse ($Origin+'/health') 32768
 [ordered]@{status=$r.status;redirected=$r.redirected;noSetCookie=$r.noSetCookie;contentTypeHtml=($r.contentType -match '^text/html');path='/health'}
}
function Test-ApiRuntimeModules([string]$Id){
 $expected=[ordered]@{
  'dist/domain/channels/channels.service.js'='aa2d4e51ee906b3cc7dd79d4835cd331b00eaa772655506630e6f944d13bda73'
  'dist/domain/channels/receipt-attempt-convergence.js'='93495861c2b300b66c5d5292803e3fbb71819c662896ae81ef457e8a4abbd1c4'
  'dist/surfaces/webhooks/evolution.controller.js'='09b1ba14d22f90d345cce9f1e87cfcee8de4560a755c6f59528e22b7955d47ac'
  'dist/integrations/meta/meta.client.js'='a756c9693c574f6fb4987d878af8d4fbeaf9f07c86a5c5e6acadeca4f7a771cb'
 }
 foreach($entry in $expected.GetEnumerator()){
  $r=Invoke-DockerText @('exec',$Id,'sha256sum',$entry.Key)
  if($r -notmatch '^([0-9a-f]{64})\s+(.+)$' -or $Matches[1] -cne $entry.Value -or $Matches[2] -cne $entry.Key){throw 'compiled_api_module_hash_mismatch'}
 }
 return $true
}
function Assert-ProductionOrigin([string]$Id,[string]$Origin){
 $escaped=$Origin.Replace("'","\\'")
 $check="if(process.env.NODE_ENV==='production'&&process.env.WEB_ORIGIN==='$escaped'){process.stdout.write('true')}else{process.stdout.write('false')}"
 if((Invoke-DockerText @('exec',$Id,'node','-e',$check)) -cne 'true'){throw 'api_public_origin_or_production_boolean_false'}
}
function Test-ApiByteCasFixtures {
 $text='KEEP_OPAQUE_A=***SECRET-SENTINEL***'+"`r`n"+'  export CHANNELS_LOCAL_ORIGIN = https://old.example'+"`r`n"+'KEEP_OPAQUE_B=***OTHER***'+"`r`n"
 $input=[Text.Encoding]::UTF8.GetBytes($text);$edit=New-OriginEdit $input $expectedHost
 if($edit.oldOrigin -cne 'https://old.example' -or -not (Test-ByteArrayEqual $input $edit.original)){throw 'fixture_target_edit_failed'}
 $s=[IO.MemoryStream]::new();$s.Write($input,0,$input.Length);$s.Position=0
 $ok=Invoke-ByteCAS $s $input $edit.replacement
 if($ok.outcome -cne 'written_and_verified'){throw 'fixture_success_cas_failed'}
 $s.SetLength(0);$s.Write($input,0,$input.Length);$s.Position=0
 $interrupted=Invoke-ByteCAS $s $input $edit.replacement 'write_after_prefix'
 if($interrupted.outcome -cne 'write_interrupted_restored'){throw 'fixture_interrupted_cas_restore_failed'}
 $s.SetLength(0);$s.Write($input,0,$input.Length);$s.Position=0
 $flush=Invoke-ByteCAS $s $input $edit.replacement 'flush_before_commit'
 if($flush.outcome -cne 'write_interrupted_restored'){throw 'fixture_flush_cas_restore_failed'}
 $s.Dispose()
 [ordered]@{result='byte_cas_fixtures_passed';successVerified=$true;interruptedWriteRestored=$true;interruptedFlushRestored=$true;opaqueSentinelsNotEmitted=$true;realFileOrDockerAccess=0}
}

if($RunByteCasFixtures){ Test-ApiByteCasFixtures | ConvertTo-Json -Depth 4 -Compress; exit 0 }
if(-not $ApplyApiOrigin){[ordered]@{result='plan_only_no_private_read_or_runtime_mutation';operation='api_origin_only';apiId=$apiId;apiImage=$newApiImage;webId=$webId;webImage=$webImage;gatewayId=$gatewayId;gatewayImage=$gatewayImage;hostname=$expectedHost;composeTail=@('up','-d','--pull','never','--no-build','--no-deps','--force-recreate','api');privateReadOccurred=$false;runtimeMutationOccurred=$false}|ConvertTo-Json -Depth 4 -Compress;exit 0}
if([string]::IsNullOrWhiteSpace($AcceptedProofPath) -or -not (Test-Path -LiteralPath $AcceptedProofPath -PathType Leaf)){throw 'accepted_root_go_proof_required'}
$proof=Get-Content -LiteralPath $AcceptedProofPath -Raw | ConvertFrom-Json
$self=(Get-FileHash -LiteralPath $MyInvocation.MyCommand.Path -Algorithm SHA256).Hash.ToLowerInvariant()
if($proof.decision -cne 'GO' -or $proof.operationAuthority -cne 'GO' -or $proof.rootOutcome -cne 'GO' -or $proof.operation -cne 'api_origin_only' -or $proof.helperSha256 -cne $self -or $proof.rootAccepted -ne $true){throw 'accepted_root_go_proof_mismatch'}
if($proof.hostname -cne $expectedHost -or $proof.apiId -cne $apiId -or $proof.apiImage -cne $newApiImage -or $proof.webId -cne $webId -or $proof.webImage -cne $webImage -or $proof.gatewayId -cne $gatewayId -or $proof.gatewayImage -cne $gatewayImage -or $proof.gatewayConfigSha256 -cne $expectedGatewayConfigSha){throw 'accepted_runtime_pin_mismatch'}
Assert-DockerExecutableAvailable
if(Test-Path -LiteralPath $stageReceiptPath){throw 'stage_receipt_already_exists_refuse_overwrite'}
$origin='https://'+$expectedHost
$privateBytes=$null;$replacement=$null;$oldOrigin=$null;$initialAcl=$null
try{
 $script:stage='preflight';Write-Stage 'started' 'none'
 Assert-PreservedResources 'api';Assert-WebPreserved
 $null=Assert-SelectedService 'api' $apiId $newApiImage 'healthy'
 $baselineTopology=Get-TopologySnapshot $apiId $webId $gatewayId
 if($baselineTopology.runtimeConfigSha256 -cne $expectedGatewayConfigSha -or (Get-ImageId $apiTag) -cne $newApiImage){throw 'api_or_gateway_pin_mismatch'}
 $script:stage='origin_preflight';Write-Stage 'started' 'none'
 $currentPublic=Get-PublicApiHealth $origin
 if($currentPublic.status -ne 200 -or $currentPublic.redirected -or -not $currentPublic.noSetCookie){throw 'new_public_health_precondition_failed_before_private_read'}
 Assert-ProductionOrigin $apiId $knownOldOrigin
 [byte[]]$privateBytes=[IO.File]::ReadAllBytes($envPath)
 $initialAcl=(Get-Acl -LiteralPath $envPath).Sddl
 $edit=New-OriginEdit $privateBytes $expectedHost
 if($edit.newOrigin -cne $origin -or $edit.oldOrigin -cne $knownOldOrigin){throw 'origin_expected_previous_hostname_mismatch'}
 $original=$edit.original;$replacement=$edit.replacement;$oldOrigin=$edit.oldOrigin
 $script:stage='origin_write';Write-Stage 'started' 'none'
 $null=Set-OriginBytesCAS $original $replacement
 if((Get-Acl -LiteralPath $envPath).Sddl -cne $initialAcl){throw 'origin_acl_postcondition_failed'}
 Write-Stage 'success' 'none'
 $script:stage='api_recreate';Write-Stage 'started' 'none'
 $null=Assert-SelectedService 'api' $apiId $newApiImage 'healthy'
 if((Get-ImageId $apiTag) -cne $newApiImage){throw 'api_tag_changed_before_recreate'}
 $script:apiMutationStarted=$true
 Invoke-ComposeUp 'api' $origin
 $newApiId=Get-ComposeServiceId 'api'
 if($newApiId -ceq $apiId){throw 'api_force_recreate_did_not_change_container_id'}
 $script:operationApiId=$newApiId
 $null=Assert-OwnedService $newApiId $newApiImage 'api' 'running'
 $null=Wait-ApiHealthy $origin $newApiId
 Assert-ProductionOrigin $newApiId $origin
 $null=Test-ApiRuntimeModules $newApiId
 if((Get-ImageId $apiTag) -cne $newApiImage){throw 'api_tag_postcondition_mismatch'}
 Assert-PreservedResources 'api';Assert-WebPreserved
 $postTopology=Get-TopologySnapshot $newApiId $webId $gatewayId
 if($postTopology.gateway.id -cne $baselineTopology.gateway.id -or $postTopology.gateway.image -cne $baselineTopology.gateway.image -or $postTopology.runtimeConfigSha256 -cne $expectedGatewayConfigSha -or $postTopology.networkId -cne $baselineTopology.networkId){throw 'gateway_or_network_drift_after_api_recreate'}
 $script:stage='public_health';Write-Stage 'started' 'none'
 $public=Get-PublicApiHealth $origin
 if($public.status -eq 502){
  $directStatus=Get-DirectApiHealth $newApiId
  $script:events+=,[ordered]@{capturedAtUtc=[DateTime]::UtcNow.ToString('o');stage='gateway_502_diagnostic';status='captured';failureCategory='public_502_direct_status_recorded';nativeExitCode=$script:lastDockerExitCode;httpStatus=$public.status;directApiHealthStatus=$directStatus;apiIpChanged=($postTopology.api.ip -cne $baselineTopology.api.ip);gatewayConfigMatchesPinnedTemplate=($postTopology.runtimeConfigSha256 -ceq $expectedGatewayConfigSha);privateValuesOrBodiesPersisted=$false}
  Write-Stage 'diagnostic_captured_before_gateway_gate' 'public_502_direct_status_recorded'
  $postTopology=Invoke-OneGuardedGatewayReload $baselineTopology $postTopology $public.status $directStatus
  $public=Get-PublicApiHealth $origin
 }
 if($public.status -ne 200 -or $public.redirected -or -not $public.noSetCookie){throw 'public_api_health_failed'}
 $script:stage='complete';Write-Stage 'success' 'none'
 [ordered]@{result='api_origin_only_success';hostname=$expectedHost;apiId=$newApiId;apiImage=$newApiImage;productionOriginVerified=$true;compiledModulesMatch=$true;publicHealth=$public;webId=$webId;webImage=$webImage;gatewayId=$gatewayId;gatewayConfigSha256=$expectedGatewayConfigSha;preservedSixOtherContainersAndFiveVolumes=$true;privateOldOriginPersisted=$false;gatewayReloadAttempted=$script:gatewayReloadAttempted}|ConvertTo-Json -Depth 5 -Compress
}catch{
 $failure='guard_or_api_origin_operation_failed';if($_.Exception.Message -match '^[a-z][a-z0-9_]+$'){$failure=$_.Exception.Message}
 $failedStage=$script:stage
 $script:stage='failure_before_rollback';Write-Stage 'failed' $failure -NoThrow
 $originRollback='not_needed';$apiRollback='not_needed';$rollbackOk=$true
 if($script:originTransactionIncomplete){$originRollback='incomplete_write_recovery_unverified';$rollbackOk=$false}
 elseif($script:originChanged){
  try{
   if(-not(Test-OriginIs $replacement)){throw 'origin_rollback_refused_concurrent_bytes'}
   $cur=Get-ComposeServiceId 'api';$f=Get-ContainerFacts $cur
   if($script:apiMutationStarted -and $null -ne $script:operationApiId){if($cur -cne $script:operationApiId -or $f.image -cne $newApiImage -or $f.owner -cne 'number-onboarding' -or $f.project -cne 'leadshug_channels_local' -or $f.service -cne 'api'){throw 'api_rollback_refused_unknown_current_id'}}
   elseif($cur -cne $apiId -or $f.image -cne $newApiImage -or $f.owner -cne 'number-onboarding' -or $f.project -cne 'leadshug_channels_local' -or $f.service -cne 'api'){throw 'api_rollback_refused_unknown_current_id'}
   $null=Set-OriginBytesCAS $replacement $original
   if((Get-Acl -LiteralPath $envPath).Sddl -cne $initialAcl){throw 'origin_rollback_acl_mismatch'}
   $originRollback='verified_original_bytes_and_security_metadata'
   if($script:apiMutationStarted){
    Assert-PreservedResources 'api';Assert-WebPreserved
    if((Get-ImageId $apiTag) -cne $newApiImage){throw 'api_rollback_refused_tag_drift'}
    if((Get-ComposeServiceId 'api') -cne $script:operationApiId){throw 'api_rollback_refused_selected_id_changed'}
    Invoke-ComposeUp 'api' $oldOrigin
    $restored=Get-ComposeServiceId 'api';$rf=Assert-OwnedService $restored $newApiImage 'api' 'running'
    if($restored -ceq $script:operationApiId){throw 'api_rollback_container_not_replaced'}
    $null=Wait-ApiHealthy $oldOrigin $restored;Assert-ProductionOrigin $restored $oldOrigin
    $script:operationApiId=$restored;$apiRollback='verified_same_image_health_old_origin'
   }else{$apiRollback='not_needed_api_never_recreated'}
  }catch{$originRollback='refused_or_unverified';$rollbackOk=$false}
 }
 $rollbackPublicStatus=$null
 $oldPublicOriginKnownUnavailable=$true
 if($script:gatewayReloadAttempted -and $apiRollback -eq 'verified_same_image_health_old_origin'){$rollbackOk=$false}
 try{Assert-PreservedResources 'api';Assert-WebPreserved}catch{$rollbackOk=$false}
 $script:stage='terminal';Write-Stage $(if($rollbackOk){'rollback_verified_or_no_mutation'}else{'rollback_incomplete_stop'}) $failure -NoThrow
 [ordered]@{result=$(if($rollbackOk){'failure_rollback_verified_or_no_mutation'}else{'failure_rollback_incomplete_stop'});failureCategory=$failure;failedStage=$failedStage;originRollback=$originRollback;apiRollback=$apiRollback;rollbackPublicHealthStatus=$rollbackPublicStatus;oldPublicOriginKnownUnavailable=$oldPublicOriginKnownUnavailable;fullPublicRollbackHealthVerified=$false;preservedResourcesVerified=$script:preservationVerified;originTransactionIncomplete=$script:originTransactionIncomplete;receiptWriteFailure=$script:receiptWriteFailure;gatewayReloadAttempted=$script:gatewayReloadAttempted;privateOldOriginExposed=$false;privateOldOriginPersisted=$false}|ConvertTo-Json -Depth 5 -Compress
 exit 2
}
