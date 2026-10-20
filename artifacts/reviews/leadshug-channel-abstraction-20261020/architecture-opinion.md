# ST-CON-06 — parecer tático de arquitetura e resolução

Data cliente:2026-10-20. Reviewer independente `/root/stcon06_architecture`, fresh/no-context, gpt-6.1-sol/max; routing `evidence/routing-architecture.json` go. Baseline revisada Foundation `b092c5a29c07d10384543b80d5fdb19fd54bfdea`, produto root80e3940/API db5a867/Web74b9d4b. Parecer terminal; nenhum arquivo editado, teste/runtime/account call executado ou path privado acessado pelo reviewer. Não é aprovação humana nem aderência de implementação.

**Resultado original: no-go pendente das correções AR01..04.** Direção Channel favorável; correções dentro do recorte. O owner integrou as disposições abaixo no contrato v1.1, a ser publicado e conferido por crítica independente. `findings_integrated` registra resolução documental, não inventa parecer inicial sem achados.

| ID / severidade | Achado / evidência pública exata | Resolução integrada no contrato |
| --- | --- | --- |
| AR-01 high | D03 dizia rotação sem invalidar recibo, mas number-registration.service.ts:346 incrementa generation a cada REAUTORIZAR; message-acceptance.service.ts:208 exige generation capturada | D03 distingue version-only com identidade/generation/epoch intactos de REAUTORIZAR real; sem rebind, contexto alterado após ACK usa projeção honesta; testes separados incluindo reautorização real concorrente |
| AR-02 high | falha local pós-ACK não se limita a retirada; Conversations:221/234 e acceptance:179 têm falhas de aceitação/finalização/diagnóstico | D03/05 outcome ACCEPTED_LOCAL_INCOMPLETE para qualquer falha local após ACK válido; localMessageState RECORDED somente com evidência positiva, UNCONFIRMED no resto (rollback não exclui eco);409 contexto ou503 conclusão local; null-ID só AMBIGUOUS_SEND_RECORDED após commit confirmado. Sem intent/schema/worker/replay; testes antes acceptance/commit incerto/depois commit/diagnóstico falho |
| AR-03 medium | Incoming:79/94 fixa incoming.channelId, ignora estadoDaJanela e não faz finalização humana; contrato universal podia mudar tudo implicitamente | D06/07 preservam binding do ingresso e fila/owner/autoria/unread do bot. Regra comum requiresWindow aplicada também ao bot: correção expressa do bypass, temporal atual preservado. Testar outra origem durante Typebot retido, janela expirada/contexto alterado |
| AR-04 medium | Conversations:164 ordena só createdAt, timeline canônica usa createdAt/id | D07 createdAt DESC,id DESC em seleção e disponibilidade; teste empate entre transportes |

Obrigações de implementação já no recorte, agora explícitas:

- Controller público: remover message.update(authorUserId:null) e atribuição incondicional pós-envio (public/conversations.controller.ts:161); autoria/assignment intent trusted antes do owner, MessageAcceptance continua dono do enrichment. Testar público vs claim humano e overlap BFF/público.
- Web api.ts:35/109 hoje perde outcome. D10 o conserva com metadados safe, mensagem honesta/draft, sem reenvio automático.
- D08 prova recipientRef opaco via BFF seeded/bot/internal, enquanto POST público mantém telefone numérico; nenhum novo enum/rede/flag de produto.
- EPS observa reutilização de metadados da BU na lista, sem novo fan-out por conversa. HTTP fora de tx, um POST, GET só metadados.

Lentes do reviewer: correctness favorável após correções; performance condicionalmente neutra; elegance favorável; structural soundness favorável com owners separados; operational fit favorável com runner seguro, namespace descartável, all/freshness e INOUT assistida. Nenhuma medição/readiness real foi feita.

Limite de verificação externa: a referência oficial Meta retornou429 ao reviewer; ele não certificou whitelist de erros. O owner obteve a referência pública primária para10/100/190 nesta preparação, registrada em source-assumptions.json. D04 mantém whitelist estreita e UNKNOWN default; testes raw e recheck da documentação antes da implementação não são dispensados.

Sequência de resolução: parecer terminal → integração v1.1 pelo owner → novo freeze documental → crítica fresh com contrato completo e este ledger → guardas. Produto permanece não implementado e sem APROVADO específico.
