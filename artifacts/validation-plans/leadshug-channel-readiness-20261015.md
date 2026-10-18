# Plano de validação — conexões e histórico dos canais

**Data:** 2026-10-15
**Estado:** contrato aprovado; harness local aceito em cp27/all499 e revisões independentes. Prova com números reais ainda pendente; disposição atual por cenário no TODO.
**Contrato governante:** [ST-CON-01 aprovado](../../todos/active/features/TODO-leadshug-channel-connection-readiness.md).
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

## Próximo recorte confirmado — Nova conversa pelo contato (ST-CON-04)

O usuário confirmou que também quer iniciar conversas informando o contato. Estes sinais são candidatos do contrato seguinte, após o cadastro de números; não entram por antecipação no ST-CON-01.

| ID | Jornada | Sinal de aceitação candidato |
| --- | --- | --- |
| CONV-01 | Selecionar BU e informar telefone | Validar país/telefone e normalizar identidade sem criar variante do mesmo contato por formatação. |
| CONV-02 | Abrir conversa já existente | Reutilizar conversa BU/contato e histórico, sem duplicar thread ou apagar responsável/estado. |
| CONV-03 | Contato novo | Criar a conversa scoped e mostrar o destino antes do primeiro envio; não criar entidade CRM implicitamente. |
| CONV-04 | Duplo clique e mensagem chegando por webhook ao mesmo tempo | Um único par BU/contato e resultado consistente; nenhum envio duplicado por replay da UI. |
| CONV-05 | Primeiro envio não oficial | Canal conectado e credencial corretos; erro/aceite e recebimento real observáveis. |
| CONV-06 | Oficial dentro da janela | Texto livre somente quando janela e permissão de envio permitem. |
| CONV-07 | Oficial fora da janela | Usar template já aprovado pela Meta, com idioma/parâmetros validados; texto livre não é enviado. Gestão/submissão de templates e campanhas não são presumidas. |
| CONV-08 | Sem canal, sem grant, outro tenant ou contato inválido | Erro explícito; não criar thread ou chamar provider sem autorização. |
| CONV-09 | Trocar BU/destino com criação/envio pendente | Resposta antiga não abre conversa ou limpa texto do destino novo. |
| CONV-10 | Nova conversa por contato vs histórico importado | São ações distintas; abrir contato não importa conversas do aparelho. |

## Cadastro: regressões da revisão de arquitetura (VAL-08)

Casos de regressão exercitados localmente e aceitos nas revisões cp21/cp25/cp27, conforme tabela REG-SEC do TODO e raw completo cp27. Não equivalem a prova externa. Fixtures de dois tenants e recursos distintos; PostgreSQL real e barreiras para disputas. Provider stub só na porta externa; prova de aparelho separada.

| Caso | Cenário / expectativa obrigatória |
| --- | --- |
| REG-SEC-01 | Dois tenants com triggers globais concorrentes: IN A só escolhe bot/credencial A; nenhuma sessão/texto/saída B. Sessão estrangeira falha antes do HTTP externo. |
| REG-SEC-02 | Replay sequencial e dez duplicatas concorrentes x3 por Meta/Evolution: uma Message, um unread e uma ação downstream; controle negativo com mesmo externalMessageId em dois recursos aceita ambos. Sem ID rejeita; echo OUT não vira IN; echo e sender reconciliam a mesma linha conforme REG-SEC-11. |
| REG-SEC-03 | Mensagem Evolution antes da confirmação do número retorna503 e não persiste conteúdo/raw, Message, unread, realtime ou bot; ownPhone divergente409 mantém quarentena. Número correto permite retry idempotente; sem promessa de replay. LID sem telefone comprovado rejeita. |
| REG-SEC-04 | Evento Meta criado sob recurso de A; remover vínculo preserva owner; tentar vincular mesmo recurso a B retorna409; evento tardio não afeta B/receipt/bot. Reativar somente mesma BU. |
| REG-SEC-05 | GET QR não chama provider; POST pair sem anti-CSRF rejeita antes da chamada; ADMIN com header válido usa lease/generation e budget. |
| REG-SEC-06 | Canal migrado sem credencial reautoriza no slot ocupado, sem WHATSAPP_TOKEN; troca ambígua/consumida exige tentativa e nonce novos; reserva sem efeito expirada pode ser retomada sem nova BU. |
| REG-SEC-07 | Candidata para outro número/cancelada/expirada ou geração anterior nunca substitui ativa válida; duas candidatas concorrentes só currentAttemptId pode promover por CAS; owner/readiness confirmados antes da ativação. |
| REG-SEC-08 | Envelope Evolution com apikey/token/URL secreta fictícios e QR/code/PIN: segredo ausente em raw DB, audit, erro, DTO, log, trace e artefatos. Pré-identidade persiste apenas metadados seguros. |
| REG-SEC-09 | Code/PIN transitórios saem do formulário apenas via BFF HTTPS; não há browser storage/URL/retorno/trace; cifra candidata e ativa rejeitam tamper, purpose/BU/attempt/version incorretos e keyId ausente. |

Limitação explícita: vencedor publica realtime/aciona bot após commit; crash nessa janela pode deixar efeito ausente. Não é claim exactly-once externo nem autorização para replay automático de automação. Esse risco constará do runbook de validação.

## Resoluções da crítica independente — casos discriminantes adicionais

| Caso | Cenário / expectativa obrigatória |
| --- | --- |
| REG-SEC-10 | Começar com canal Evolution comprovado X, executar RENEW com barrier no HTTP: proof invalidada antes da chamada. Nova instância tem nome channelId+epoch; retries reutilizam essa instância. Mensagem da nova rodada antes da prova, open/wuid=X antigo e conclusão de verify antigo não restauram aceitação nem persistem conteúdo/raw/unread/realtime/bot. Identidade nova Y fica em quarentena; consulta nova da instância atual com X permite replay aceito uma vez. Não satisfazer com fixture inicialmente não verificada. |
| REG-SEC-11 | Stub Evolution entrega webhook autenticado fromMe DENTRO de enviarTexto e só depois retorna o mesmo externalId. BFF e público retornam o mesmo Message.id e só uma OUT física scoped ao recurso, com conteúdo/autoria humana correta, zero IN/unread/bot. Repetir sender-first e ecos concorrentes; recurso distinto com mesmo ID é independente. Typebot usa o mesmo owner para gravar OUT/autoria, com sequência equivalente quando esse provider emite echo. Checar identificador não secreto da credencial/recurso na porta externa e triggers/sessões reais no PostgreSQL; mocks sem predicado não bastam. |
| REG-SEC-12 | Callback Evolution válido usa `/webhooks/evolution` e segredo fictício em `x-leadshug-webhook-secret`; a rota antiga com segredo na URL rejeita. Atravessar gateway real em sucesso, falha de autenticação, falha upstream e erro de parser anterior à seleção de location, com marcadores fictícios também em path/query e verificação Meta. Access/error/application/provider logs e artefatos não contêm esses valores; preservar diagnósticos úteis de status/upstream. Provar envio do header pela Evolution fixada antes de QR real. Requisito, não claim de execução. |
| REG-SEC-13 | Meta batch assinado contém recursos de duas BUs e recurso desconhecido/retirado. Cada raw record só tem fragmentos do owner verificado; partes não verificadas só metadados. Nenhum conteúdo cru global ou de outro tenant; assinatura original validada antes da partição. |

Não há garantia de sequenciamento para mensagens distintas simultâneas no Typebot; o contrato de replay diz respeito à mesma mensagem externa. Nenhum worker/fila/retry de envio é autorizado por estes testes.

## Notas de execução aceitas na revisão delta v3

Concretização de requisitos congelados, sem novo produto/arquitetura ou dispensa:

- REG-SEC-10/BCI: pausar webhook antigo DEPOIS do lookup preliminar e antes de raw/conteúdo; RENEW aposenta mapping e invalida prova. Liberar webhook e comprovar que o guard final sincronizado com aceitação impede conteúdo/receipt/unread/realtime/bot. Repetir remove/recreate. Não rotular sender antigo como recurso novo.
- REG-SEC-12: atravessar gateway também com hub.verify_token Meta fictício, aceito e rejeitado; segredo ausente em access/error/application logs e artefatos, preservando challenge/autenticação.
- REG-SEC-11/browser: mostrar OUT echo-first antes da resposta do sender, fazer refresh/pós-ação existente e conferir uma linha com mesmo Message.id/createdAt e autoria/conteúdo confiáveis, sem cursor/unread alterados. Se o cliente atual não satisfizer a projeção, registrar falha e admitir diff/escopo pelo processo normal antes de tocar Inbox.tsx excluído; a nota não autoriza tal edição.

Todos os casos continuam planned, com fonte/DB/backend reais na execução autorizada. Nenhuma prova executada nesta revisão documental.


cp69 corrente (2026-10-17): operador confirmou destinatário correto e dois tiques. Diagnóstico local agora ATIVO: fonte/managedconfig6d4563cc..., commitrootlocal80e3940, única ativação sob GOc2e18a59 consumido, nginx-t/um reload passaram e same7containers/5volumes preservados. V1nãoativada: seis achados RV01..06 Integrated e resolvidos na v2; revisão independente411e15b5..., 11casos isolados/per-case/joint/logprivacy/cleanup e mocks de falha aceitos. Histórico de fixtures falhas preservado/qualificado; sem suiteAPI/Web nova. Stdoutterminal truncado pela ferramenta não foi retido; recibo de ativação é reconstrução explícita de stage228c2d...+exit0+readbacks, sem retry nem stdout fabricado. Root TLS público independente200 confirma policy12865/d0 e JSd143 semcookie/redirect. Adoção do log em runtime comprovou apenas GETmeta403 próprio semquery; não é rejeição de POSTMeta ou receipt. Baseline readonly20f67e...capturado18:05:12.685Z mantém CONECTANDO/SUBSCRIBED/PENDING_RECEIPTv7 com identidade/credencial atuais, semreceipt/connectedAt/INOUT/conversas/eventBU. Teste físico oficial03 solicitado; janela route desde18:05:51.932693Z em evidence/cp69-official-physical-test03-window.json. Próximo: aguardar relato, contagens conjuntas meta/POST/status e SELECT agregado corrente; não reenviar automaticamente, trocarcadastro/credencial ou escrever no provider. Aceite root-cp69-gateway-runtime-accepted.json. Parent Pending/VAL05 aberto e semwaiver; R02/coorte OWNER privada e hostnameefêmero preservados. Sem pushsource ou gitlinkwrite.


cp71 corrente (2026-10-17): físico03 não apareceu; countercp70 completo97linhas/zero rotaMeta e SELECT semdelta, semreceipt/INOUT. Operador confirmou número conectado a outro sistema (nome/recebimento nele ainda pendentes) e teste padrão no painel MetaHTTP200. Janela separada do controle: countercp71completo5linhas,1metaPOST200 e4otherGET304; correlação temporal somente, semrequestid/identidadedeprovedor. SELECT continuaPENDING_RECEIPTv7/INOUT0/semreceipt; controle sintético não fechaVAL05. Três GETs readonly pontuais comGOsdistintos consumidos: phonewebhook200/contextstable applicationcallback coincide comaddressing-mar-perform-hormone, overridesWABA/phone não retornados=>unknown; phonemetadata200/contextstable CLOUD_API/CONNECTED/code_verification_statusEXPIRED/is_on_biz_appfalse (EXPIREDnãoestabelececausa nemautorizaSMS/registro); appsubscriptions200,1rowWhatsApp explicitactive=true/callbackmatch, semlista útilfields=>messages/versionunknown naAPI, mantendo confirmaçãohumana prévia de inscrição. Root corrigiu parserv1string/perlayer e inferencev1active antesexecução; versões/provas preservadas, semrawURLs/Graphbody/headers/erros/tokens/segredos/Config.Env/arquivosprivados/logsAPI expostos. Cipherkey/token só emmemóriaAPI para2GETphone e appsecret só emmemória para1GETapp-header, cadaumapósGO novo/pinos/limites. Nenhuma alteração de provider/credenciais/vínculos/runtime/fonte-produto, nenhum retry/callbacktakeover/migração ou permissões novas. Adjudicação root-cp71-official-delivery-diagnosis.json. Próximo: nome do outro sistema/provedor e entrega do03 nele, antes de correção concreta; não refazer cadastros nem testes físicos antecipadamente. ParentPending/VAL05aberto/semwaiver, coorte OWNERprivada/R02 e hostnameefêmero preservados.


cp72 (2026-10-17): operador não sabe o nome do outro sistema nem se o teste chegou nele; ambos permanecem desconhecidos, sem atribuir causalidade à integração existente. Uma GET com projeção explícita dos campos da assinatura do app, sob GO distinto consumido e API/image/owner/health conferidos, retornou HTTP 200, uma assinatura WhatsApp ativa e callback correto. A propriedade fields continuou ausente; presença/versão de messages seguem desconhecidas pela API, preservando a confirmação humana anterior de inscrição. Helper v4 e cópia de evidência byte-exact, selftest offline root passou; stdout sanitizado persistido diretamente e hashes conferidos em root-cp72-official-delivery-diagnosis.json. Sem fallback, novas chamadas, writes no provedor, alterações de fonte/runtime/cadastro ou teste físico. Próximo: consultar níveis das permissões whatsapp_business_messaging/management e estado da verificação da empresa no painel Meta; isso é investigação, não causa confirmada nem pedido de expansão de acesso. Não repetir a pergunta sobre o outro sistema nem novos testes físicos sem ajuste concreto. Parent Pending; VAL05 aberto e sem waiver.


cp73 — recuperação local e roteamento (2026-10-18): operador confirmou permissões padrão e empresa verificada; identificou Whatsflow nas atribuições e nas cinco categorias de Conversation routing. Remoção indisponível foi abandonada. O usuário autorizou mudar todas as categorias para unifast.br2, portfólio gestor do app, e confirmou “Alterado e salvo”. Isso é configuração declarada, ainda sem prova causal ou mensagem real. O hostname anterior deixou de resolver e seus processos estavam ausentes. Um novo túnel próprio foi lançado, sem adoção/kill, para estimation-editions-knee-inclusion.trycloudflare.com. Falhas anteriores 530/Windows indeterminado foram preservadas; o diagnóstico posterior observou health200 e uma conexão HA. Uma execução API-only alterou somente CHANNELS_LOCAL_ORIGIN por CAS/ACL e recriou a API com a mesma imagem fe5; novo ID9eccbea4825108cec2b8a6fcd48c43c17845e216415fe95e3972265c6ad34cf1. Outros seis containers/cinco volumes e gateway/config6d foram preservados, sem rebuild/pull, mudança Web ou reload. Provas finais Windows/WSL: root/health/política/JS200 e hashes esperados, TLS normal e sem redirects/cookies; GET Meta sem query/token403 esperado. Não há promessa de disponibilidade contínua do túnel. Novo agregado readonly mantém identidade/credencial atuais, SUBSCRIBED/PENDING_RECEIPT v7, IN0/OUT0/conversas0/sem receipt. Root conferiu hashes e limites em evidence/root-cp73-local-recovery-adjudication.json. Próximo: operador atualizar domínios/OAuthSDK/callback/política no mesmo app Meta publicado e validar webhook mantendo messages; só depois abrir janela física04. Conta Railway disponível, mas sem projeto LeadsHug; nenhum deploy/push de produto/gitlink autorizado ou realizado. Coorte privada OWNER/R02 preservada. Parent Pending; VAL05 aberto sem waiver. A imagem API continua i, com fonte j diferente apenas em teste excluído; nenhuma nova matriz all537/browserj foi reivindicada.
