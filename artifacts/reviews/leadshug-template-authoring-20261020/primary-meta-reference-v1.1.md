# ST-CON-05 v1.1 — current primary Meta reference receipt

Read-only public documentation research in2026-10-20. Browser fetch returned429/inaccessible for some pages; HTTP Accept:text/markdown returned200 from the same official URLs. No account API, credentials or provider mutation. Facts below are paraphrased; local limits/authorization are explicit product decisions.

## Template fundamentals

[Template fundamentals](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview/). Templates pertencem à Messaging account. Criação aceita category/language/parameter_format/components; nomes têm até512caracteres. NAMED e POSITIONAL têm exemplos por variável; POSITIONAL é default quando o formato não é informado. Uso exige APPROVED; criação não garante essa aprovação. A proposta local escolhe pt_BR/NAMED e limites mais restritos.

## Template components

[Template components](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/components/). BODY admite até1024caracteres; HEADER TEXT e FOOTER até60. Variáveis exigem exemplos. A proposta cria somente BODY com variáveis e HEADER/FOOTER estáticos, sem botões/mídia; são restrições do produto.

## Template review

[Template review](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-review/). A Meta analisa o conteúdo, podendo aprovar ou recusar. Amostras ajudam a avaliar variáveis. Parâmetros no início/fim, sintaxe inválida e excesso proporcional de variáveis podem levar à recusa. A proposta não promete prazo nem aprovação e não implementa editar ativo remoto/apelar.

## Template API

[Template API](https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-account/message-template-api/). POST account/message_templates cria e retorna ID/status/categoria; GET account/message_templates pagina e pode solicitar fields de nome/idioma/components/status/parameter_format; GET templateID consulta estado. Resposta de criação e estado de análise são dimensões separadas.

## Error codes

[Error codes](https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes/). O catálogo orienta mapear códigos estruturados, não textos/subcodes isolados. Lista códigos10/190 de autorização,100 de parâmetro e2388040/2388047/2388072/2388073/2388293/2388299 de formato/variáveis. A proposta exige envelope inequívoco e fase para REJECTED; resultado pós-dispatch inconclusivo permanece AMBIGUOUS.

## Lookup-by-name cross-check

Official [Meta Postman](https://www.postman.com/meta/whatsapp-business-platform/request/7whkjje/get-template-by-name-default-fields) shows the server name filter. The [Meta SDK](https://github.com/facebook/facebook-python-business-sdk/blob/main/facebook_business/adobjects/whatsappbusinessaccount.py) supports that parameter, category, parameter_format and template CRUD. Filter results are still checked for exact name/language; if the bounded response is inconclusive, no external create/correlation is permitted.

## Product-only restrictions

Name length128, first lowercase letter, variable count20/name32, examples128,16KiB input, Portuguese-only creation, manual status refresh, freshness300s,60local submissions/hour and no media/buttons are choices of this slice, not claims of universal Meta limits. Current actual account management access and response shapes will be proved only after approval via raw contracts plus the separate assisted operator submission.
