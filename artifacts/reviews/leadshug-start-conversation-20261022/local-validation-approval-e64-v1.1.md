# ST-CON-04 — ativação local e validação assistida

Proposta concreta para autorização; nenhuma ação abaixo foi executada. A revisão atual apontou três correções de claim/locks/consulta. Este E64 é histórico; fontes, provas, imagens e revisão precisam ser renovadas antes de solicitar autorização.

O candidato E64 implementa abertura/reuso de conversa por contato, escolha explícita do canal, prévia e primeiro envio textual ou por modelo oficial aprovado, com recuperação de resultado incerto sem reenvio automático. A rodada canônica terminou com 368 testes unitários da API, 444 com PostgreSQL, 54 da Web e 89 de navegador aprovados. Fontes, imagens e código servido foram conferidos. Essa prova usa provedor simulado; o teste real ainda é necessário.

## Operação proposta

1. Confirmar a identidade do projeto Docker local `leadshug_channels_local` por metadados selecionados, preservando os serviços e volumes existentes.
2. Validar o histórico técnico de migrations e aplicar somente `20261022140000_initial_message_orchestration`, `20261022150000_initial_message_admissions` e `20261022160000_initial_message_inbox_order`, se pendentes. Cada SQL conserva espera máxima de bloqueio de 5 segundos e limite de comando de 60 segundos. Parar diante de drift, bloqueio ou falha; preservar o banco.
3. Atualizar somente API e Web para as imagens já construídas `leadshug-stcon04-api:e64` e `leadshug-stcon04-web:e64`. Recarregar graciosamente o gateway existente após validar sua configuração e conferir saúde e versão servida. Haverá breve indisponibilidade local. Banco, Evolution, canais, credenciais, conversas e volumes serão preservados.
4. Usar `.env.testing` apenas como entrada opaca do Compose e das conexões técnicas necessárias, sem abrir, copiar, editar ou exibir seus valores. O entrypoint existente pode ajustar a propriedade do volume nomeado de arquivos; nenhum acesso do agente ao conteúdo de arquivos está incluído.
5. Se necessário, iniciar um túnel HTTPS próprio para o gateway validado. Informar a nova URL para o operador ajustar os campos Meta já conhecidos. Não adotar nem encerrar túneis de origem desconhecida.
6. Com o operador autenticado normalmente, testar na interface um primeiro texto no canal não oficial e um primeiro envio com o modelo realmente aprovado da conta oficial, cada um seguido de resposta do destinatário de teste. O operador escolhe o contato e confirma cada envio; registrar somente resultado/estado, sem conteúdo ou dados pessoais.

As imagens e os hashes completos estão no [plano técnico](evidence/local-activation-proof-plan-proposal-v1.1.json) e na [conferência das imagens](evidence/image-build-root-collection-e64-v1.1.json). Antes de qualquer envio, a fonte, a imagem, o container e a versão HTTP precisam corresponder. Um resultado desconhecido exige consulta/reconciliação, nunca repetição automática ou retorno automático à API anterior, que não possui o novo interlock.

## Inspeção final proposta

Executar uma vez o guard canônico `todo_diff_expectation_guard.py` para os quatro repositórios declarados no TODO. O helper não permite limitar sua enumeração a caminhos públicos; o Git pode enumerar/stat e ler/hash internamente arquivos privados ao comparar diferenças. A exceção cobre somente essa execução de leitura. Saída bruta ficará em arquivos locais restritos; a evidência pública conterá apenas resultado, contagens, códigos e hashes, sem nomes privados ou conteúdo. Não há autorização de edição, exclusão ou staging de arquivos privados. Falha será registrada e avaliada, sem filtragem silenciosa.

O detalhe está na [exceção pontual de inspeção](evidence/final-diff-guard-boundary-proposal-v1.1.json).

## Motivo da autorização específica

O [TODO aprovado](../../../todos/active/features/TODO-leadshug-start-conversation-by-contact.md) estabelece em VAL-08: “local source-bound API/Web activation and owned stable/temporary HTTPS only under later approved runtime plan”. Em Out of Scope, também proíbe “Ler/listar/stat/hash/traversar/montar” os caminhos privados. A autorização atual de implementação e dos ajustes de testes não elimina essas duas fronteiras; esta proposta define a operação e as exceções estritamente necessárias.

A entrega permanece Pending até a revisão, a ativação, a prova assistida, a consolidação dos módulos e os guards/review finais.
