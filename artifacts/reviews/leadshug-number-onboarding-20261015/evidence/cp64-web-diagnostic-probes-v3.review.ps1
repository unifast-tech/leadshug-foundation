# Read-only probes for a separately root-authorized Web-only diagnostic.
# Never activates services, reads the private env file, or writes response bodies.
[CmdletBinding()]
param([string]$HostName='',[switch]$DummyOnly)
$ErrorActionPreference='Stop'
if(-not $DummyOnly -and $HostName -cne 'addressing-mar-perform-hormone.trycloudflare.com'){throw 'unexpected_public_host'}
Add-Type -AssemblyName System.Net.Http
function Get-Meta([byte[]]$Body,[string]$ContentType,[string]$ContentEncoding,[string]$CacheControl,[bool]$HasSetCookie,[int]$Status){
  $utf8=$true; $html=''
  try{$html=[Text.UTF8Encoding]::new($false,$true).GetString($Body)}catch{$utf8=$false}
  $sha=[Security.Cryptography.SHA256]::Create(); try{$digest=[BitConverter]::ToString($sha.ComputeHash($Body)).Replace('-','').ToLowerInvariant()}finally{$sha.Dispose()}
  [ordered]@{
    status=$Status; bytes=$Body.Length; sha256=$digest
    utf8Valid=$utf8; contentType=$ContentType; contentEncoding=$ContentEncoding; cacheControl=$CacheControl; setCookiePresent=$HasSetCookie
    emailDecodeScript=($html -match 'email-decode\.min\.js'); emailProtectionPath=($html -match '/cdn-cgi/l/email-protection'); dataCfemail=($html -match 'data-cfemail')
    scriptTagCount=([regex]::Matches($html,'(?i)<script\b')).Count; formTagCount=([regex]::Matches($html,'(?i)<form\b')).Count
  }
}
function Get-DirectWebMetadata {
  $apiId='f86d76c633f4f06a98a67dc4b6432700ac8e1e6f81b555697b5feabf6a1f08ab'
  $js="const h=require('http'),c=require('crypto');const q=[['directWeb','http://web/privacidade.html'],['directGateway','http://gateway/privacidade.html']];Promise.all(q.map(([name,url])=>new Promise(resolve=>{const req=h.get(url,{timeout:5000},res=>{const chunks=[];let size=0;res.on('data',b=>{size+=b.length;if(size>250000){res.destroy();resolve({name,errorCategory:'body_size_limit'});return}chunks.push(b)});res.on('end',()=>{const body=Buffer.concat(chunks);let html='',utf8Valid=true;try{html=new TextDecoder('utf-8',{fatal:true}).decode(body)}catch(e){utf8Valid=false;html=body.toString('utf8')}resolve({name,status:res.statusCode,redirected:res.statusCode>=300&&res.statusCode<400,bytes:body.length,utf8Valid,sha256:c.createHash('sha256').update(body).digest('hex'),contentType:res.headers['content-type']||'',contentEncoding:res.headers['content-encoding']||'',cacheControl:res.headers['cache-control']||'',age:res.headers.age||'',cfCacheStatus:res.headers['cf-cache-status']||'',vary:res.headers.vary||'',setCookiePresent:Object.prototype.hasOwnProperty.call(res.headers,'set-cookie'),emailDecodeScript:html.includes('email-decode.min.js'),emailProtectionPath:html.includes('/cdn-cgi/l/email-protection'),dataCfemail:html.includes('data-cfemail'),scriptTagCount:(html.match(/<script\b/gi)||[]).length,formTagCount:(html.match(/<form\b/gi)||[]).length})})});req.on('error',e=>resolve({name,errorCategory:e.code||'request_error'}));req.on('timeout',()=>req.destroy(new Error('timeout')))}))).then(x=>process.stdout.write(JSON.stringify(x)))"
  $encoded=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($js))
  $prior=$ErrorActionPreference
  try{$ErrorActionPreference='Continue';$raw=& docker.exe exec $apiId node -e "eval(Buffer.from('$encoded','base64').toString())" 2>$null;$exit=[int]$LASTEXITCODE}finally{$ErrorActionPreference=$prior}
  if($exit -ne 0){throw 'direct_web_probe_failed'}
  try{return ($raw|ConvertFrom-Json)}catch{throw 'direct_web_metadata_invalid'}
}
function Get-ResponseHeaderFacts([Net.Http.HttpResponseMessage]$Response){
  $ct='';$ce='';$cc='';$age='';$cfCache='';$vary=''
  if($Response.Content.Headers.Contains('Content-Type')){$ct=$Response.Content.Headers.GetValues('Content-Type') -join ','}
  if($Response.Content.Headers.Contains('Content-Encoding')){$ce=$Response.Content.Headers.GetValues('Content-Encoding') -join ','}
  if($Response.Headers.Contains('Cache-Control')){$cc=$Response.Headers.GetValues('Cache-Control') -join ','}
  if($Response.Headers.Contains('Age')){$age=$Response.Headers.GetValues('Age') -join ','}
  if($Response.Headers.Contains('CF-Cache-Status')){$cfCache=$Response.Headers.GetValues('CF-Cache-Status') -join ','}
  if($Response.Headers.Contains('Vary')){$vary=$Response.Headers.GetValues('Vary') -join ','}
  [ordered]@{contentType=$ct;contentEncoding=$ce;cacheControl=$cc;age=$age;cfCacheStatus=$cfCache;vary=$vary;setCookiePresent=$Response.Headers.Contains('Set-Cookie')}
}
function Get-PublicPolicy([string]$Uri){
  $handler=[Net.Http.HttpClientHandler]::new(); $handler.AllowAutoRedirect=$false; $handler.UseCookies=$false
  $client=[Net.Http.HttpClient]::new($handler); $client.Timeout=[TimeSpan]::FromSeconds(10); $client.MaxResponseContentBufferSize=250000; $request=[Net.Http.HttpRequestMessage]::new([Net.Http.HttpMethod]::Get,$Uri)
  $null=$request.Headers.AcceptEncoding.ParseAdd('identity')
  try{
    $response=$client.SendAsync($request).GetAwaiter().GetResult()
    try{
      [byte[]]$body=$response.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
      $headerFacts=Get-ResponseHeaderFacts $response
      [ordered]@{transport='windows_system_net_http';normalTls=$true;redirected=($response.StatusCode -ge 300 -and $response.StatusCode -lt 400);host=$HostName;path='/privacidade.html';meta=(Get-Meta $body $headerFacts.contentType $headerFacts.contentEncoding $headerFacts.cacheControl $headerFacts.setCookiePresent ([int]$response.StatusCode)); age=$headerFacts.age; cfCacheStatus=$headerFacts.cfCacheStatus; vary=$headerFacts.vary}
    }finally{$response.Dispose()}
  }finally{$request.Dispose();$client.Dispose();$handler.Dispose()}
}
if($DummyOnly){
  $dummy=[Net.Http.HttpResponseMessage]::new([Net.HttpStatusCode]::OK)
  try{
    $null=$dummy.Headers.TryAddWithoutValidation('Cache-Control','public, max-age=0')
    $null=$dummy.Headers.TryAddWithoutValidation('Vary','Accept-Encoding')
    $null=$dummy.Headers.TryAddWithoutValidation('Set-Cookie','dummy=1')
    $dummy.Content=[Net.Http.StringContent]::new('synthetic')
    $null=$dummy.Content.Headers.TryAddWithoutValidation('Content-Type','text/html; charset=utf-8')
    $facts=Get-ResponseHeaderFacts $dummy
    if($facts.cacheControl -cne 'public, max-age=0' -or $facts.vary -cne 'Accept-Encoding' -or -not $facts.setCookiePresent){throw 'dummy_header_contract_failed'}
    [ordered]@{dummyOnly=$true;cacheControl=$facts.cacheControl;vary=$facts.vary;setCookiePresent=$facts.setCookiePresent}|ConvertTo-Json -Compress
  }finally{$dummy.Dispose()}
  exit 0
}
[ordered]@{direct=Get-DirectWebMetadata;windowsPublic=Get-PublicPolicy ('https://'+$HostName+'/privacidade.html')} | ConvertTo-Json -Depth 7 -Compress
