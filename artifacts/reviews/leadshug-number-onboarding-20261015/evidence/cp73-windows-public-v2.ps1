$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Net.Http
$hostName='estimation-editions-knee-inclusion.trycloudflare.com'
$handler=[Net.Http.HttpClientHandler]::new()
$handler.AllowAutoRedirect=$false
$handler.UseCookies=$false
$client=[Net.Http.HttpClient]::new($handler)
$client.Timeout=[TimeSpan]::FromSeconds(12)
$client.MaxResponseContentBufferSize=400000
$results=@()
try {
 foreach($path in @('/','/health','/privacidade.html','/assets/index-txvhtd65.js')) {
  $x=[ordered]@{path=$path;status=$null;bytes=$null;redirected=$null;noSetCookie=$null;sha256=$null;errorCategory=$null}
  $response=$null
  try {
   $response=$client.GetAsync('https://'+$hostName+$path).GetAwaiter().GetResult()
   $bytes=$response.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
   $x.status=[int]$response.StatusCode
   $x.bytes=$bytes.Length
   $x.redirected=($x.status -ge 300 -and $x.status -lt 400)
   $x.noSetCookie=(-not($response.Headers.Contains('Set-Cookie') -or $response.Content.Headers.Contains('Set-Cookie')))
   $sha=[Security.Cryptography.SHA256]::Create()
   try {$x.sha256=([BitConverter]::ToString($sha.ComputeHash($bytes))).Replace('-','').ToLowerInvariant()} finally {$sha.Dispose()}
  } catch {$x.errorCategory=$_.Exception.GetType().FullName}
  finally {if($null -ne $response){$response.Dispose()}}
  $results+=,$x
 }
 [ordered]@{checkpoint='cp73-windows-public-v2';host=$hostName;normalTls=$true;noSession=$true;results=$results}|ConvertTo-Json -Depth 5 -Compress
} finally {$client.Dispose();$handler.Dispose()}
