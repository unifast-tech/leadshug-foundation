# Vínculo local do Test Number da Configuração da API

Estado: **direção aceita pelo usuário em CP81; contrato complementar revisado, finalizando pré-aprovação; implementação não autorizada**. Owner: integrações/canais. Complemento candidato do [ST-CON-01](../../todos/active/features/TODO-leadshug-channel-connection-readiness.md); não é outro contrato de execução nem substitui o TODO. Perfil: Operational/DevOps, análise sem mudanças de produto; eventual implementação exige handoff para Operational/Coder e revisão de segurança.

## Problema confirmado

O operador confirmou que a mensagem enviada pela Configuração da API chegou dentro do aplicativo WhatsApp. Esse recurso permite uma conversa real no aparelho. O número retornado pelo Embedded Signup Sandbox e vinculado à BU Teste Meta é outro recurso: no aparelho do operador apareceu indisponível no WhatsApp, e ele enviou SMS. A troca física Sandbox não foi executada via WhatsApp; não constitui falha de entrega da API.

O vínculo Sandbox confirmado em CP80 não cadastra automaticamente o Test Number da Configuração da API. Também não se deve registrar esse Test Number novamente por SMS: a tentativa anterior foi rejeitada como número já cadastrado.

Há ainda um problema independente: a resposta WhatsApp ao Test Number da Configuração da API, observada em CP77, não produziu rota Meta no gateway durante a janela medida. Cadastrar o recurso permite resolver sua BU quando um evento chegar; **não garante que a Meta entregue o webhook**. O teste padrão do painel é sintético e não fecha essa prova.

## Inventário do caminho atual

| Evidência de código | Comportamento existente |
| --- | --- |
| `api-app/src/surfaces/bff/number-registrations.controller.ts:21-65` | Criação, authorize com nonce/code, options, confirm e advance; nenhum recebimento de token manual. |
| `api-app/src/domain/channels/number-registration.service.ts:179-225` | Sessão/tentativa correntes, troca real de code e cifra da candidata antes de listar recursos. |
| `api-app/src/domain/channels/number-registration.service.ts:228-365` | Confirmação exige candidata autorizada, verifica recurso/telefone/owner e promove credencial por transação/CAS. JA_REGISTRADO só dispensa register. |
| `api-app/src/integrations/meta/meta.client.ts:67-104` | Token validado por app, validade, ambos os escopos e alvos WABA granulares; não basta colar IDs. |
| `api-app/src/surfaces/bff/channels.controller.ts:42-53` | Antigo cadastro direto desativado: USE_NUMBER_REGISTRATIONS. |
| `api-app/src/surfaces/webhooks/meta.controller.ts:76-94` | Mensagens dependem de identidade/canal corrente já vinculados; webhook não cria cadastro. |
| `api-app/test/number-onboarding-flow.e2e-spec.ts:39-78,286-319,555-584` | Jornada OAuth/JA_REGISTRADO, rejeição de recurso pertencente a outra BU e divergência do telefone canônico. |

Conclusão do inventário: não existe entrada suportada para uma credencial da Configuração da API sem uma candidata oriunda do OAuth. A ausência desse caminho não prova que a Meta nunca disponibilize o recurso em uma autorização; nenhuma nova tentativa foi executada para presumir isso.

A [coleção oficial Meta Cloud API](https://www.postman.com/meta/whatsapp-business-platform/documentation/wlk6lh4/whatsapp-cloud-api?entity=folder-fce1b64c-b7e2-41d6-b1eb-196c74e5c1ac) documenta tokens de usuário e de usuário do sistema e o token obtido pelo painel. Isso dá fundamento a um modo técnico, mas não comprova o grant nem a compatibilidade do token concreto com as regras atuais do LeadsHug. Nenhuma credencial foi lida nesta análise.

## Opções

| Opção | Esforço e impacto | Risco e manutenção | Disposição |
| --- | --- | --- | --- |
| A. Manter somente Embedded Signup | Nenhuma alteração de produto; investigar a exposição da conta de teste nesse fluxo | Não resolve um caminho de vínculo que possa ser reproduzido agora; suporte Meta continua útil para o ingresso histórico | Válida se não ampliarmos o cadastro |
| B. Entrada técnica local para recurso já provisionado, convergindo no domínio atual | Mudança de autorização, configuração local, pequeno passo no wizard e testes; provável metadado persistido do método | Exige revisão de segurança e validação real do grant; preserva um único mecanismo de confirmação/ownership/credencial/envio | Recomendada para viabilizar o teste local solicitado |
| C. Inserção manual de mapping/credencial no banco ou token global de envio | Baixo esforço aparente, alto acoplamento e dívida | Ignora invariantes e não exercita o cadastro; compromete a validade do teste | Rejeitada |

## Contrato candidato da opção B

1. Entrada de **configuração técnica da instalação local**, desabilitada por padrão e ausente das capacidades quando não configurada. Não reabre a rota antiga nem altera o fluxo normal Embedded Signup.
2. Credencial do recurso de teste mantida em configuração privada do backend, junto com o alvo explícito da BU/WABA/telefone. Serve somente para autorizar a candidata desse alvo; os envios continuam resolvendo a credencial cifrada do canal. Não vira fallback global. O segredo não entra no formulário, bundle, URL, logs, histórico, artifacts ou chat.
3. Usar uma BU de teste própria, criada pelo fluxo normal, por exemplo **Teste API Meta**. Não substituir automaticamente o número Sandbox já pertencente à BU Teste Meta, nem o número próprio de Local Test Ofc. Nenhuma transferência de identidade entre BUs ou mudança de telefone canônico é permitida.
4. No wizard, ADMIN da BU reserva uma tentativa oficial e escolhe explicitamente a configuração local disponível. Novo endpoint proposto `POST /api/bff/number-registrations/:id/authorize-local-test`, body apenas nonce; exige mesma sessão/ator, tentativa corrente, prazo, configuração habilitada e alvo exato. A configuração técnica não concede grant ao usuário da aplicação.
5. Distinguir duravelmente o método de autorização da tentativa. Não simular code, callback OAuth ou estágio CODE_CONSUMED. O método local só admite JA_REGISTRADO, inclusive na validação do backend; nunca recebe PIN nem chama register, migração, unregister ou coexistência.
6. Antes da cifra candidata, validar app de origem, validade reportada por is_valid e escopos na Meta. O adaptador atual não atesta separadamente classe do token ou prazo explícito de expiração; não prometer esses dados. Reutilizar as validações atuais de autorização e pertinência WABA/número; ausência de alvos granulares ou qualquer incompatibilidade deve bloquear com código seguro. **Não afrouxar o fluxo Embedded Signup para aceitar esse token.** Se o grant real não satisfizer o contrato, registrar a lacuna e retornar ao desenho/revisão antes de prosseguir.
7. Prosseguir por options e confirmação explícita do recurso. Owner durável, telefone canônico, currentAttempt/generation/epoch, lease, grant administrativo e versão da credencial permanecem verificados até o commit. Nenhum HTTP de provider ocorre dentro da transação. Candidata não substitui a credencial ativa antes da confirmação.
8. Cifrar com AAD da candidata e promover pelo mecanismo compartilhado para credencial por BU/canal. Cancelamento/expiração limpam candidata; reautorização preserva ativa válida e requer intenção nova. Token expirado mostra pendência/erro seguro; não há renovação automática presumida.
9. Mapping durável precede assinatura de eventos. Advance conserva orçamento e semântica atuais; inscrição já presente é reconciliada, resultado ambíguo não dispara retry cego. Não tomar override/callback de outro sistema nem alterar roteamento Meta por essa ação.
10. Cadastro termina inicialmente em recebimento pendente. Somente IN WhatsApp autenticada prova recebimento; resposta enviada pela inbox e confirmada no outro aparelho prova OUT observado. SMS, cadastro, dois tiques no remetente, token válido, inscrição e POST sintético não substituem essa prova.

Não haverá novo coletor de mensagens desconhecidas, identificação por texto/contato, importação de histórico, API pública de desenvolvimento ou seed no banco do operador.

## Superfícies esperadas e verificação

Possíveis alterações, sujeitas à revisão: serviço/controller de number registrations, Meta adapter para expor validação compartilhada sem duplicá-la, metadado do método no schema/migração, capacidades e passo técnico do wizard, configuração privada de teste e env.example sem segredo, runbook e testes existentes. Channel credential resolver, webhook e aceite de mensagens continuam compartilhados. Sem implementação neste documento.

Verificar com o runner canônico API/PostgreSQL: permissão/sessão/nonce, default desabilitado, alvo divergente, app estrangeiro, token expirado/revogado, escopo ou WABA ausentes, phone não pertencente, owner/telefone conflitantes, dupla confirmação, lease/attempt obsoletos, cancelamento e preservação da ativa. Provar zero register mesmo em payload forjado NOVO. Testes devem comprovar origem local sem simular OAuth. UI: disponibilidade e ocultação do segredo, confirmação explícita e tratamento de erro seguro. Regressão Embedded Signup/QR e consumers por BU obrigatória.

Prova real após implementação aprovada: confirmar configuração privada e grant sem exportar segredo; validar vínculo exato; testar primeiro chegada no gateway e depois processamento scoped/inbox, com janela e contagens separadas. Se não houver POST real, não alterar mapping para tentar corrigir transporte. Retomada/reautorização e preservação de conversa seguem VAL05; um sucesso parcial não encerra o parent.

## Limites e decisão humana necessária

O contrato aprovado SCOPE-02 escolheu Embedded Signup. A opção B é um **novo método de autorização**, com risco material próprio; a menção antiga a um caminho técnico possível não é implementação existente nem autorização automática. O [método de execução](../../../delphi-ai/workflows/docker/todo-execution-boundary-method.md) exige: “new independently testable behavior, a new primary objective, or a new approval/risk conversation requires TODO update/split and renewed approval”.

Usuário confirmou “Sim, incluir o modo técnico local”. Próximo passo: refinar o [TODO complementar](../../todos/active/features/TODO-leadshug-meta-api-test-number-binding.md), congelar baseline publicada, executar reviews de arquitetura/segurança/crítica e guardas, e só então solicitar aprovação de implementação conforme o [método de aprovação](../../../delphi-ai/workflows/docker/todo-approval-gates-method.md). Este documento está **prepared-pre-freeze**: não há review/guard de implementação declarado como aprovado.

Sem nova leitura de credenciais, Graph, banco, logs ou runtime; sem novo envio físico solicitado. Parent Pending; VAL05 aberto e sem waiver. O problema histórico de ausência de POST real permanece em diagnóstico separado.

CP81 arquitetura v1: direção estrutural aceita, parecer revise por uma lacuna material no contrato da qualificação. O TODO complementar agora explicita os quatro campos base Meta, token e alvo em memória, stdin privado, módulo compilado com freshness, método verificarNumeroVinculado (até3GET/10s cada, sem retry) e resultado booleano fixo. Nenhum token/URL/provider response é exportado. Sucesso prova app/is_valid/scopes/alvos/telefone no instante observado; classe e expiração explícita continuam desconhecidas. Numeração de decisões e teste pós-promoção/desativação alinhados. Nova baseline/critique pendentes; sem implementação autorizada.

Estado posterior CP81: crítica independente v1 approve com zero bloqueadores materiais confirmou a correção da arquitetura. LowCRIT-MIG-01 nomeia replay após migração em critérios já previstos. Guardas finais e publicação do pacote de aprovação em fechamento; nenhum grant real qualificado, nenhum código alterado e nenhum teste WhatsApp novo realizado.
