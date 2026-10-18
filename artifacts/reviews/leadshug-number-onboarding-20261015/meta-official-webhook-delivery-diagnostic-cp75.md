# Diagnóstico para suporte Meta — mensagem real sem callback

Rascunho para consulta pelo administrador. Nenhum chamado foi enviado pelo agente.

O app LeadsHug (App ID público `874966345550148`, Graph `v26.0`) recebe o teste padrão do campo `messages` com HTTP 200, mas ainda não foi observada a entrega de mensagens reais ao callback do número oficial reservado para testes. Solicitamos verificar os registros de entrega e a elegibilidade de eventos para o app/número.

## Ambiente e vínculo

- Ambiente local de testes, callback HTTPS temporário: `https://estimation-editions-knee-inclusion.trycloudflare.com/webhooks/meta`.
- Administrador confirmou app publicado, `messages` inscrito, empresa verificada e permissões `whatsapp_business_management` e `whatsapp_business_messaging` com acesso padrão.
- Leituras Graph pontuais retornaram HTTP 200: callback de aplicação do número coincide com o endereço atual; app está inscrito na WABA; proprietário retornado da WABA coincide com o portfólio gestor do app.
- Camadas de override de WABA/número não foram retornadas; permanecem desconhecidas.
- Administrador alterou e salvou as cinco categorias de Conversation routing de Whatsflow para unifast.br2. O parceiro não foi removido. Ainda não há leitura independente do roteamento efetivo da conversa.
- A aba Messaging accounts mostra duas contas vinculadas. Administrador encontrou o número de teste nas duas; isso não identifica qual integração recebe eventos.

## Observações em UTC — 18/10/2026

1. Janela da mensagem real: início `03:11:56.914652Z`; captura de ingress em `03:18:33.655Z`. Operador relatou ausência na inbox. Leitura completa de 61 registros do gateway: zero chamadas à rota Meta. A conversa utilizou o contato já empregado nos testes anteriores; não temos prova com uma conversa inédita após a mudança de roteamento.
2. Checagem de disponibilidade posterior: `/health` HTTP 200 com conteúdo esperado. É uma observação pontual; o túnel temporário não tem disponibilidade contínua comprovada.
3. Controle separado: início `03:21:03.249333Z`; captura em `03:23:42.340Z`. Administrador enviou o evento padrão `messages` no painel e relatou sucesso/HTTP 200. Gateway registrou um POST à rota Meta com HTTP 200 nessa janela. Correlação temporal agregada; não guardamos payload nem identificadores por requisição.
4. Após as duas janelas: canal ainda aguarda primeiro recebimento, sem mensagem de entrada/saída ou conversa registrada no escopo do teste. Evento sintético não foi usado como comprovação de entrega real.

## Pontos solicitados à Meta

- Há tentativas de entrega de webhooks para mensagens reais desse número nessas janelas? Se há, qual destino/status; se não há, qual condição impede a emissão?
- Qual conta/aplicativo responde à conversa existente após a mudança das categorias de roteamento? Existe alguma associação efetiva anterior ainda aplicável a essa conversa?
- As duas Messaging accounts vinculadas afetam esse vínculo de número/app? Qual associação está ativa para a entrega dos eventos?
- Há restrição específica de acesso/revisão para este teste com número pertencente ao mesmo portfólio gestor do app? A verificação da empresa e a publicação foram confirmadas, mas não presumimos aprovação de acesso avançado.

Não atribuímos a causa ao parceiro, ao acesso padrão, à interface ou ao backend. Nenhuma remoção, migração, novo registro, reautorização ou expansão de permissões deve ser executada com base apenas neste relatório.

Se o suporte precisar de WABA ID, Phone Number ID ou identificação do número, o administrador deve preenchê-los diretamente no canal privado oficial da Meta. Não incluir tokens, App Secret, QR, códigos de autorização, credenciais ou conversas pessoais.

[Evidências locais e hashes](evidence/root-cp75-official-delivery-diagnosis.json). Os arquivos locais não foram compartilhados com terceiros. Próximo passo: consultar o diagnóstico disponível no painel/atendimento Meta; nenhuma nova mensagem física foi solicitada.
