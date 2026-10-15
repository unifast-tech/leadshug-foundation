# Plano de validação — conexões e histórico dos canais

**Data:** 2026-10-15
**Estado:** planejamento; nenhum cenário abaixo foi executado nesta frente.
**Contrato candidato:** [ST-CON-01 draft](../../todos/active/features/TODO-leadshug-channel-connection-readiness.md).
**Enquadramento:** [conexões e histórico](../feature-briefs/leadshug-channel-readiness-and-history-20261015.md).

## Sequência de ambientes

Usuário confirmou em2026-10-15: **local primeiro**, Railway de testes depois. O primeiro ciclo valida o backend local com providers/números de teste reais. Railway não é dependência de conclusão deste ciclo e exigirá readiness/evidência próprias antes de qualquer promoção.

Inspeção de leitura: Docker Engine acessível via cliente Windows; socket Linux indisponível nesta sessão. Containers do Compose LeadsHug existentes estavam parados. O Compose não declara Evolution nem repassa as variáveis de webhook/instância à API. A existência de uma Evolution no legado não fornece runtime autorizado para este teste. Nada foi iniciado ou alterado.

## Preparação do ambiente

1. Preparar ambiente local próprio do LeadsHug: fixar versão/build da Evolution, persistência/sessão e dono de execução; completar Compose/wiring e configuração privada em contrato antes da implementação. Não derivar o target do ambiente legado.
2. Identificar BU, canal, número oficial selecionado e instância de teste, com permissão do operador. Não publicar telefones completos, QR, payloads pessoais ou credenciais nos artefatos.
3. Configurar credenciais no mecanismo privado do ambiente; registrar apenas presença/ausência, permissões e resultados redigidos. Credencial presente não significa válida.
4. Definir endereço de callback alcançável pelos providers para o backend local e autenticação de origem; selecionar o mecanismo de exposição no contrato, sem presumir domínio ou abrir túnel agora. Webhook forjado deve ser recusado; endpoint responder200 a probe artificial não prova que o provider consegue alcançá-lo.
5. Confirmar interlocutor/segundo aparelho de teste. Identificar quais vínculos são descartáveis antes de interrupção/repareamento; não remover instância em uso.
6. Registrar branch@SHA API/Web, bundle servido e target redigido; fonte/build devem ser atuais antes do Playwright. Sessão, grants, PostgreSQL e WebSocket continuam reais no harness.

Dependências desconhecidas permanecem no [registro](../dependency-readiness.md). Uma oferta de número ainda não é prova de acesso ao provider.

## Matriz de prova de cadastro e conexão — ST-CON-01

| ID | Cenário | Resultado necessário | Evidência planejada |
| --- | --- | --- | --- |
| CAD-01 | Iniciar cadastro oficial, autorizar/cancelar na Meta e receber callback | Vínculo correlacionado com sessão/BU, código trocado somente no backend e credenciais scoped; sem sucesso em cancelamento/erro. | Contratos de OAuth/adapter, browser e autorização real separada. |
| CAD-02 | Iniciar cadastro não oficial por apelido e ler QR | Instância própria e vínculo corretos, número confirmado e conclusão visível; QR usado removido. | Browser/backend real e aparelho de teste. |
| CON-01 | WABA sem número, com um e com múltiplos | Erro explícito quando vazia; vínculo ao número escolhido; nunca escolher silenciosamente o primeiro quando há ambiguidade. | Contrato adapter/BFF e Playwright com readback da BU. |
| CON-02 | Credencial inválida, expirada ou sem permissão | Mostrar falha de verificação sem expor segredo ou converter ausência de prova em CONECTADO. | Negativas por canal + amostra real permitida. |
| CON-03 | Evolution cria instância e QR é lido | Transição compatível com estado real do provider e telefone confirmado; tela não fica exibindo QR como se ainda estivesse pendente após conclusão. | Browser + estado observado + mensagem real. |
| CON-04 | QR expirado/novo e repareamento | Renovação visível; resultado antigo não altera vínculo novo. | Browser/harness de concorrência e aparelho de teste. |
| CON-05 | Provider indisponível/timeout/payload inválido | Verificação falha de forma limitada e permite retry; momento da última observação continua explícito. | Adapter e E2E com contador de chamadas/tempo. |
| CON-06 | Vários cliques/poll/usuários | Orçamento e concorrência definidos; listar não gera consultas externas por BU em cada poll. | Readback e contagem/in-flight de consultas. |
| CON-07 | Evento mais novo enquanto consulta velha está pendente | Resposta velha não regrede estado; ordenação e origem da observação são testadas conforme regra congelada. | Barrier determinístico + controle negativo. |
| CON-08 | Remover/recriar canal durante consulta | Consulta antiga não escreve no vínculo novo e não o reativa. | Teste de geração/identidade com PostgreSQL real. |
| CON-09 | Atendente sem poder administrativo e usuário de outro tenant | Negação scoped; nenhuma consulta externa ou escrita não autorizada. | E2E + contador de adapter e readback. |
| CON-10 | Mensagem IN de interlocutor real | Callback autenticado, BU/contato corretos, uma mensagem visível e persistida; carimbo de build/provider/canal. | Observação provider → webhook → banco → inbox. |
| CON-11 | Resposta OUT pela inbox | Identificador externo e recebimento no interlocutor; estado de janela oficial respeitado. | Inbox → provider → aparelho e readback; aceite HTTP isolado não basta. |
| CON-12 | Interrupção e retomada permitidas | Estado honesto durante interrupção e recuperação comprovada por nova IN/OUT. | Checklist por canal; diferenciar reconexão de socket do navegador. |

O teste CON-03 é específico do não oficial; no oficial usar o onboarding admitido, sem inventar QR de dispositivo. CON-12 não exige derrubar produção ou revogar credencial real: procedimento será limitado ao target de teste e às ações admitidas no contrato.

## Provas futuras de histórico — ST-CON-02/03

Estes cenários orientam contratos futuros; não ampliam o ST-CON-01.

| ID | Cenário | Resultado necessário |
| --- | --- | --- |
| HIS-01 | Carga inicial oferecida pelo provider | Quantidade, período e limitações visíveis; não anunciar todo o aparelho quando só há subconjunto disponível. |
| HIS-02 | Mesmo lote reapresentado e evento simultâneo | Identidade scoped e idempotência atômica; não duplicar a mensagem já persistida por envio/webhook. |
| HIS-03 | Datas antigas/empatadas e mensagens OUT | Preservar timestamp externo e direção; ordenação determinística e proveniência separadas da data de ingestão. |
| HIS-04 | Importação durante atendimento e bot ativo | Não incrementar não lidas, reabrir conversa, responder bot ou estender janela oficial por ingestão de mensagem antiga. |
| HIS-05 | Interrupção no meio e retry | Checkpoint persistente e retomada bounded; falha/progresso explícitos; não reiniciar tudo silenciosamente. |
| HIS-06 | Evento novo durante backfill e mensagens antigas inseridas | Cobertura e política de invalidação da timeline explicitamente definidas. ST-ATT-01 excluiu backdating fora da fronteira; importação exigirá novo contrato nessa fronteira. |
| HIS-07 | Dados de outra BU/canal/tenant ou payload sem ID | Recusar vazamento; regra de identidade/fallback decidida antes de persistir. |
| HIS-08 | Oficial sem capacidade/eligibilidade comprovada | Mostrar indisponível ou pendente; não prometer histórico e não importar usando mecanismo do não oficial. |

## Registro de resultados por canal

O resultado deve distinguir: configuração/identidade, conexão observada com horário, IN comprovada, OUT comprovada, recuperação comprovada, histórico disponível/importado e limitações. Falha em uma dimensão não deve ser escondida por sucesso em outra.

Para cada execução, registrar cenário, target redigido, canal, versão do provider, branch/build, precondição, resultado, IDs técnicos redigidos, horário e evidência. Nunca usar resultado do harness com provider substituído como prova real.

## Critério de encerramento

O TODO governante define o limiar final. Para a proposta ST-CON-01, exigir matriz local aceita e troca real por cada canal disponibilizado. Se não houver acesso, registrar pendência explícita; não substituir por falso sucesso, dispensa implícita ou alegação de produção pronta.
