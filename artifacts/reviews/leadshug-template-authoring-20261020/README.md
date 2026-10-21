# ST-CON-05 v1.1 — template authoring planning package

State: approved-v1.1-implementation-in-progress. Governing contract: ../../../todos/active/features/TODO-leadshug-official-template-authoring.md. Previous20261019 reviews remain history. This cycle rebases seller create/save/preview/submit/status onto delivered06 with a narrow TemplateManagementResolver/MessageTemplateProvider port, dedicated Meta integration, immutable scoped context and preserved textual Channel/OutboundService. Approval2026-10-21 authorizes the reviewed implementation; activation and assisted provider proof follow the disposable validation and assurance gates.

Review focus: DIP/capability segregation, scope/management versus send authority, durable one-dispatch receipts and conservative ambiguity recovery, name/account isolation, status truth, UI fences, mandatory inherited working-tree seal, full CI-equivalent and actual assisted submission. Source baseline/evidence are public-only. Planned approval scope includes additive templates migration and source-bound local activation after disposable proof; no secret read/product push/deploy.

## Proposta para revisão

Jornada: Cadastros → Modelos → selecionar BU/canal → Novo modelo → preencher texto, variáveis e exemplos → visualizar prévia → salvar → confirmar envio à Meta → consultar andamento. Vendedor cria e submete sem aprovador administrativo. Rascunhos locais respeitam autor e grants; modelo submetido pertence ao catálogo compartilhado da conta.

Primeira versão: português do Brasil, corpo textual, variáveis nomeadas, cabeçalho/rodapé opcionais estáticos, categorias Marketing/Utility explicadas, status claros e ação explícita Atualizar. Não há envio ao destinatário nesta história; o catálogo aprovado será consumido por Nova conversa ST-CON-04.

Salvamento versionado e operação durável protegem duas abas/duplo clique/crash. Resultado de criação incerto fica explícito; recuperação só consulta a mesma conta/nome/definição e nunca repete a mutação automaticamente. Aprovação é observada na Meta, não inventada localmente.

Arquitetura: TemplateManagementResolver/MessageTemplateProvider são ports estreitos, separados de Channel.sendMessage. Um adapter Meta dedicado encapsula protocolo/segredo; domínio e tela não conhecem HTTP. O resolver reutiliza o único owner de credencial e não reduz o gate de envio de mensagens. Fake de capacidade, harness de dependência, PG concorrente e Playwright real fazem parte da validação prevista.

A implementação futura inclui schema/migration aditivos, deploy/status descartável, ativação local preservando dados e uma submissão/consulta real assistida em recurso de teste. Código/env/Meta/containers permanecem intocados no planejamento. O baseline público herdado de06 é selado por hash; somente caminhos explicitamente ativos da história05 poderão mudar após aprovação.

## Histórico da revisão anterior à aprovação

Parecer arquitetural e duas críticas completas independentes concluídos; quatro achados incorporados, última crítica sem novos achados. O contrato protege confirmação incerta no banco, nome/quota por conta compartilhada, base pública herdada e ordem de atualização do catálogo/status. As conferências de código/escopo, estrutura, perfil, ciclo de vida e preparação de autoridade passaram. Resultado da autoridade: **preflight-go**, sem autorização de executar.

O [TODO v1.1](../../../todos/active/features/TODO-leadshug-official-template-authoring.md) é a proposta concreta. [Convergência das revisões](planning-convergence-v1.1.md) e [pré-aprovação](evidence/authority-preapproval-v1.1.json) registram o resultado. Freeze revisado:961dba71015f61a1f1c1badecb9efe090a77b306. Nenhum código, teste de produto, banco, ambiente ou conta externa foi alterado nesta etapa.

## Execução autorizada — 2026-10-21

O usuário respondeu APROVADO para v1.1. Aprovação e fontes binding estão no TODO; authority pós-aprovação GO com execução autorizada. A admissão inicial confirmou os3HEADs e todos41hashes herdados antes de qualquer código/teste. Executor único CP01 iniciou domínio/ports/parser/harness; demais checkpoints seguem serialmente na mesma aprovação. [Admissão inicial](evidence/initial-execution-admission-v1.1.json), [autoridade](evidence/authority-approved-v1.1.json) e [routing](evidence/routing-executor-approved-v1.1.json). Este estado não declara implementação concluída ou testes de05 passados.

## Checkpoints de implementação

CP01 base de domínio/parser/prévia/ports/harness implementada e conferida. Runner api com230testes unitários e338E2E PostgreSQL verdes foi reportado pelo executor; stdout não persistido, sem prova durável de all ainda. [Recibo e limites CP01](evidence/cp01-executor-report-v1.1.json). CP02 green3 passou com234unit/343PG; root conferiu os cinco hashes dos logs do [recibo](evidence/cp02-terminal-receipt.json). A revisão encontrou FK Restrict que bloquearia a desconexão existente após criar um rascunho; correção e regressão PG estão em andamento antes de aceitar o checkpoint. Tela/integração Meta e teste assistido ainda pendentes.

CP02 final aceito:234unit/344PG; correção test-first permite desconectar e recriar o mesmo número sem apagar histórico nem transferir autorização. [Recibo final](evidence/cp02-channel-detach-receipt.json), [disposição do root](evidence/root-cp02-disposition-v1.1.json). CP03 integração scoped e contratos HTTP de modelos iniciados sob a mesma aprovação; D09/entrega permanecem parciais.

CP03 aceito como fundamento parcial:281unit/351PG no api canônico,6logs/17sources e30sealed/3HEADs conferidos pelo root. [Recibo](evidence/cp03-terminal-receipt.json), [disposição](evidence/root-cp03-disposition-v1.1.json). CP04 backend durável/BFF/provas PG autorizado sob a aprovação existente; guard pós-grant e enum view fail-closed incluídos. Tela/all/assurance/prova real ainda pendentes.

CP04 segue em correção e validação, sem aceite final: final4 teve282unit verdes e375/376PG, com falha no caminho de consulta do catálogo. A execução seguinte mostra50 consultas pontuais indexadas na mesma query, em vez de varrer950 linhas adicionais, mas ainda possui uma asserção EPS falhando; aguarda terminal e disposição factual. O [registro de revisão em curso](evidence/root-cp04-peer-review-working.md) distingue falhas de produto, fixtures, infraestrutura e provas ainda não executadas, incluindo leitura concorrente scoped e erro de observação antigo. O usuário validou [dois companions de histórico](history-companion-path-admission-v1.1-proposal.md), com [admissão e baseline](evidence/history-companion-path-admission-v1.1.json); o guardião original de cobertura foi preservado. Handoff CP05 da interface está preparado no TODO, condicionado ao terminal API e mantendo gaps explícitos para o all. Nenhuma migração/ativação no banco preservado nem submissão real foi executada nesta etapa.
