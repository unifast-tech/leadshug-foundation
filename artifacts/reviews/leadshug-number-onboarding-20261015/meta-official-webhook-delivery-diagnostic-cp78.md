# Diagnóstico para suporte Meta — eventos reais ausentes em dois recursos

Rascunho atualizado para envio pelo administrador. O agente não abriu nem enviou chamado. Substitui o rascunho cp75 para uma nova consulta; evidências históricas permanecem preservadas.

App LeadsHug, App ID público `874966345550148`, Graph `v26.0`. O app recebe o teste padrão de webhook do painel com HTTP 200. Não foram observadas chamadas à rota Meta nas janelas de respostas físicas a dois recursos: número próprio reservado para testes e Test Number fornecido pela Meta na Configuração da API.

## Configuração conferida

- Administrador confirmou app publicado, campo `messages` inscrito, empresa verificada e permissões `whatsapp_business_management` e `whatsapp_business_messaging` com acesso padrão.
- Callback HTTPS temporário atual: `https://estimation-editions-knee-inclusion.trycloudflare.com/webhooks/meta`.
- Número próprio: GETs guardadas retornaram app inscrito na WABA, callback de aplicação coincidente e proprietário da WABA igual ao portfólio gestor do app. Camadas adicionais não retornadas continuam desconhecidas.
- Número próprio: administrador alterou as cinco categorias de Conversation routing de Whatsflow para unifast.br2 e confirmou salvo. Não houve remoção do parceiro; a aba Messaging accounts mostrou o número em duas contas vinculadas. Isso não comprova o roteamento da conversa existente.
- Test Number: administrador informou que consegue enviar o teste da Configuração da API ao seu WhatsApp e confirmou resposta com dois tiques na conversa correspondente.
- Test Number: administrador executou GET `<WABA_TESTE>/subscribed_apps` no Explorador Graph e confirmou LeadsHug listado. Executou também GET `<PHONE_ID_TESTE>?fields=webhook_configuration` e confirmou o callback esperado, sem outro endereço observado. São confirmações humanas; não coletamos o JSON/IDs/tokens nem presumimos que campos não exibidos representam ausência de override.

## Janelas observadas — UTC de 18/10/2026

| Teste | Início da janela | Captura do gateway | Resultado observado |
| --- | --- | --- | --- |
| Mensagem real ao número próprio, conversa existente | 03:11:56.914652Z | 03:18:33.655Z | 61/61 registros completos, zero rota Meta; operador não viu a entrada. |
| Evento padrão `messages` enviado pelo painel Meta | 03:21:03.249333Z | 03:23:42.340Z | 5/5 registros completos, um POST à rota Meta com HTTP 200; painel informou sucesso. |
| Resposta física ao Test Number Meta | 03:53:32.196176Z | 03:55:50.977Z | 8/8 registros completos, apenas GETs de outras rotas; zero rota Meta; operador informou dois tiques. |

O gateway conta somente rota/método/status, sem payload ou identificador por requisição. As observações são correlações temporais agregadas; não identificam uma mensagem específica. Houve health HTTP 200 com conteúdo esperado em checagens pontuais antes/depois dos testes. Não foi comprovada disponibilidade contínua do túnel: ele é temporário e teve instabilidade histórica. A ausência no gateway não estabelece se a Meta deixou de emitir, tentou entregar ou encontrou falha de rede antes desse ponto.

## Integração e limites do teste

O número próprio está cadastrado no LeadsHug e aguardava primeiro recebimento no último snapshot do banco em cp75. Não houve uma nova consulta ao banco neste diagnóstico. O Test Number não teve vínculo concluído: a tentativa pelo Embedded Signup chegou a registro novo e a Meta informou número já registrado (`2655122`). Nenhuma migração, desconexão ou novo registro foi realizado pelo agente.

O teste direto do Test Number observa ingresso no webhook; não comprova persistência na inbox. O backend verifica a assinatura e pode reconhecer com HTTP 200 um evento de identidade ainda não vinculada sem criar conversa. Essa distinção não explica a ausência observada de chamadas à rota no gateway.

## Solicitações objetivas ao suporte

1. A Meta gerou notificações para as mensagens reais nessas janelas, especialmente a resposta ao Test Number? Quais tentativas de entrega existem?
2. Para cada tentativa, qual callback efetivamente resolvido, status HTTP ou erro de DNS/TLS/conexão e horário UTC? Se houver referência de entrega, fornecê-la pelo canal privado de suporte.
3. Se não houve emissão, qual requisito de configuração, elegibilidade/permissão, recurso de teste ou roteamento impediu o evento? A inscrição e o callback foram conferidos, sem assumir aprovação de acesso avançado.
4. Há override ou associação de conversa/conta que altere o destino em relação ao callback observado?

Não atribuímos a causa à Meta, ao Whatsflow, ao acesso padrão ou ao código. O transporte HTTPS também permanece em investigação. Não solicitamos migração, remoção de parceiro, troca de callback, expansão de permissões ou repetição de mensagens sem uma evidência/correção concreta.

Se o suporte precisar dos IDs da WABA, Phone Number ID ou número de teste, o administrador deve preenchê-los somente no canal privado oficial. Não incluir token, App Secret, senha, QR, códigos de autorização ou conversas pessoais.

Referências locais: [controle e número próprio](evidence/root-cp75-official-delivery-diagnosis.json), [resposta ao Test Number](evidence/root-cp77-direct-reply-readback.json), [confirmações da conta de teste](evidence/root-cp78-test-resource-readback.json). Nenhum arquivo foi enviado a terceiros pelo agente.
