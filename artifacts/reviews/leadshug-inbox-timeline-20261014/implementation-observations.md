# Observações preliminares da implementação

Inspeção de suporte do orquestrador em 2026-10-14, antes de suites completas e revisão independente. Nenhuma conclusão de entrega reivindicada. Todos os pontos pertencem ao contrato já aprovado e foram enviados ao único executor.

| ID | Locus | Cenário / defeito observado | Correção solicitada | Situação |
| --- | --- | --- | --- | --- |
| IMPL-01 | Inbox.tsx/responder | `texto === textoEnviado` compara valores da mesma closure e limpa texto digitado durante await. | Ref/versão de input e prova browser de edição enquanto envio pendente. | Executor confirmou correção; prova pendente. |
| IMPL-02 | Inbox.tsx/abrir e trocarBu | finally antigo descartado por geração deixa flags de envio/backfill presas no destino. | Reset das flags no novo contexto e prova de navegação com request atrasado. | Executor confirmou correção; prova pendente. |
| IMPL-03 | Inbox.tsx/reconciliar | Thread vazia inicia múltiplas consultas fora do objeto de single-flight. | Usar o mesmo contexto de recuperação para vazio. | Executor confirmou correção; prova pendente. |
| IMPL-04 | Inbox.tsx/executarRecuperacao catch | Erro tardio de conversa anterior escreve erro/pendência no destino. | Verificar geração e ID em respostas e erros. | Executor confirmou correção; prova pendente. |
| IMPL-05 | tempoReal.ts/onopen | Só reconexão posterior dispara atualização, mas contrato inclui primeira conexão estabelecida. | Callback em todo onopen. | Executor confirmou correção; prova pendente. |
| IMPL-06 | Inbox.tsx/carregarLista | Resposta de aba antiga da mesma BU pode sobrescrever aba nova. | Capturar filtro/contexto e rejeitar resultado antigo. | Executor confirmou correção; prova pendente. |
| IMPL-07 | test/browser-server.cjs | Provider falso usa fake.enviadas, objeto define enviados; envio lançaria erro. | Uniformizar propriedade e validar persistência/autoria real no browser. | Enviado ao executor; prova pendente. |

Essas observações não substituem architecture_adherence, test_quality_audit ou final_review independentes. A resolução final depende dos arquivos consolidados, testes e revisores.
