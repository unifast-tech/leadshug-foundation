# cp64 PowerShell compatibility probe

In fresh Windows PowerShell `-NoProfile` processes, the dummy function with the prepared helper's `[string[]]$Args` parameter received **zero** values for both exact array-expression call patterns. None of the five dummy arguments survived. The same five-value array was received correctly when the dummy parameter was named `$Arguments`; explicit `-Args` binding against a parameter named `$Args` also received zero. This exposes a concrete compatibility problem in the prepared activation helper's `Invoke-DockerText` argument binding; it needs a reviewed correction before any use. The probe called only a dummy function and never invoked `docker.exe`.

A fresh process could not construct `System.Net.Http.HttpClientHandler`/`HttpClient` without loading `System.Net.Http` (`PSArgumentException`). In a separate fresh process, explicit `Add-Type -AssemblyName System.Net.Http` made both types construct successfully. No HTTP request was sent.

No helper script was run or edited, no project/runtime process was inspected, no private file was read, and no network, Docker, source, or Git operation occurred. The JSON companion contains the exact results and limits.
