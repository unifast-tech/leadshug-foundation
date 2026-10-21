# ST-CON-05 v1.1 — template authoring planning package

State: prepared-pre-freeze. Governing contract: ../../../todos/active/features/TODO-leadshug-official-template-authoring.md. Previous20261019 reviews remain history. This cycle rebases seller create/save/preview/submit/status onto delivered06 with a narrow TemplateManagementResolver/MessageTemplateProvider port, dedicated Meta integration, immutable scoped context and preserved textual Channel/OutboundService. No product/runtime/provider operation authorized yet.

Review focus: DIP/capability segregation, scope/management versus send authority, durable one-dispatch receipts and conservative ambiguity recovery, name/account isolation, status truth, UI fences, mandatory inherited working-tree seal, full CI-equivalent and actual assisted submission. Source baseline/evidence are public-only. Planned approval scope includes additive templates migration and source-bound local activation after disposable proof; no secret read/product push/deploy.

## Proposta para revisão

Jornada: Cadastros → Modelos → selecionar BU/canal → Novo modelo → preencher texto, variáveis e exemplos → visualizar prévia → salvar → confirmar envio à Meta → consultar andamento. Vendedor cria e submete sem aprovador administrativo. Rascunhos locais respeitam autor e grants; modelo submetido pertence ao catálogo compartilhado da conta.

Primeira versão: português do Brasil, corpo textual, variáveis nomeadas, cabeçalho/rodapé opcionais estáticos, categorias Marketing/Utility explicadas, status claros e ação explícita Atualizar. Não há envio ao destinatário nesta história; o catálogo aprovado será consumido por Nova conversa ST-CON-04.

Salvamento versionado e operação durável protegem duas abas/duplo clique/crash. Resultado de criação incerto fica explícito; recuperação só consulta a mesma conta/nome/definição e nunca repete a mutação automaticamente. Aprovação é observada na Meta, não inventada localmente.

Arquitetura: TemplateManagementResolver/MessageTemplateProvider são ports estreitos, separados de Channel.sendMessage. Um adapter Meta dedicado encapsula protocolo/segredo; domínio e tela não conhecem HTTP. O resolver reutiliza o único owner de credencial e não reduz o gate de envio de mensagens. Fake de capacidade, harness de dependência, PG concorrente e Playwright real fazem parte da validação prevista.

A implementação futura inclui schema/migration aditivos, deploy/status descartável, ativação local preservando dados e uma submissão/consulta real assistida em recurso de teste. Código/env/Meta/containers permanecem intocados no planejamento. O baseline público herdado de06 é selado por hash; somente caminhos explicitamente ativos da história05 poderão mudar após aprovação.
