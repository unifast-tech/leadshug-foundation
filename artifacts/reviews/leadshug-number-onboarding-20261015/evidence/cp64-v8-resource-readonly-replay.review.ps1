$ErrorActionPreference='Stop'
$repo='C:\unifast\leadshug\leadshug_now_docker'
$sourcePath=Join-Path $repo 'foundation_documentation\artifacts\tmp\number-onboarding-execution\T\cp64-activate-origin-api-web-v8.ps1'
$sourceHash=(Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash.ToLowerInvariant()
$expectedSourceHash='01e198a7818b51fe447f46923f38b95d159e05aaeda4f3cdf27ae438f80b05b1'
$allowedFunctions=@('Invoke-DockerText','Get-ImageId','Get-ContainerFacts','Assert-OwnedService','Assert-PreservedResources')
$allowedVariables=@('newApiImage','oldWebImage','candidateWebImage','apiTag','webTag','webCandidateTag','webRollbackTag','baselineContainers','preservedImages','expectedVolumes')
$started=[DateTime]::UtcNow.ToString('o')
$stage='parse_v8_ast'
try {
    if($sourceHash -cne $expectedSourceHash){throw 'v8_source_hash_mismatch'}
    $tokens=$null;$parseErrors=$null
    $ast=[System.Management.Automation.Language.Parser]::ParseFile($sourcePath,[ref]$tokens,[ref]$parseErrors)
    if($parseErrors.Count -ne 0){throw 'v8_ast_parse_failed'}
    $functions=@($ast.FindAll({param($n) $n -is [System.Management.Automation.Language.FunctionDefinitionAst] -and $allowedFunctions -contains $n.Name},$true))
    if($functions.Count -ne $allowedFunctions.Count){throw 'v8_safe_function_set_incomplete'}
    $assignments=@()
    foreach($name in $allowedVariables){
        $found=@($ast.EndBlock.Statements | Where-Object { $_ -is [System.Management.Automation.Language.AssignmentStatementAst] -and $_.Left -is [System.Management.Automation.Language.VariableExpressionAst] -and $_.Left.VariablePath.UserPath -ceq $name })
        if($found.Count -ne 1){throw 'v8_safe_constant_missing_or_ambiguous'}
        $assignments+=,$found[0]
    }
    $code=@()
    foreach($statement in $assignments){$code+= $statement.Extent.Text}
    foreach($fn in $functions){$code+= $fn.Extent.Text}
    $stage='load_allowlisted_ast'
    Invoke-Expression ($code -join "`n")
    $script:lastDockerExitCode=$null;$script:lastFailureCategory=$null;$script:preservationVerified=$false
    $stage='assert_api'
    $api=Assert-OwnedService $baselineContainers.api $newApiImage 'api' 'running' 'healthy'
    $stage='assert_web'
    $web=Assert-OwnedService $baselineContainers.web $oldWebImage 'web' 'running'
    $stage='assert_preserved_resources'
    Assert-PreservedResources 'none'
    $gateway=Get-ContainerFacts $baselineContainers.gateway
    $stage='assert_tags'
    $apiTagId=Get-ImageId $apiTag;$webTagId=Get-ImageId $webTag;$candidateTagId=Get-ImageId $webCandidateTag
    $rollback=Invoke-DockerText @('image','ls','--quiet','--no-trunc','--filter',('reference='+$webRollbackTag))
    if($apiTagId -cne $newApiImage -or $webTagId -cne $oldWebImage -or $candidateTagId -cne $candidateWebImage -or -not [String]::IsNullOrWhiteSpace($rollback)){throw 'v8_image_tag_guard_failed'}
    $result=[ordered]@{result='v8_readonly_replay_passed';sourceV8Sha256=$sourceHash;functionsAstExtracted=$allowedFunctions;constantsAstExtracted=$allowedVariables;api=$api;web=$web;preservedResources=@{gateway=$gateway;allPreservedAndExpectedVolumesVerified=$script:preservationVerified};images=@{apiTag=$apiTagId;webTag=$webTagId;candidateTag=$candidateTagId;rollbackTagPresent=$false};volumeCount=$expectedVolumes.Count;privateRead=$false;ConfigEnvRead=$false;mutations=0}
    $result|ConvertTo-Json -Depth 7 -Compress
} catch {
    [ordered]@{result='v8_readonly_replay_failed';sourceV8Sha256=$sourceHash;stage=$stage;errorCategory=$_.Exception.Message;privateRead=$false;ConfigEnvRead=$false;mutations=0}|ConvertTo-Json -Compress
    exit 1
}
