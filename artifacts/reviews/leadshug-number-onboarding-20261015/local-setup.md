# Preparação do teste local de números

Status em2026-10-15: implementação em curso. O usuário criou o app Meta, confirmou WhatsApp e criou a configuração Embedded Signup; versão Graph `v26.0` informada pelo painel, e origem HTTPS de teste ainda não confirmada. A execução dessa autorização no LeadsHug está pendente. Este roteiro não comprova cadastro de número, conectividade ou recebimento. Os comandos definitivos do runtime serão vinculados ao README depois da validação do runner.

Atualização do operador: já possui portfólio empresarial Meta, é administrador dele e acessa o painel de desenvolvedor. Criou o app usando o caso de uso WhatsApp; o produto aparece no painel. App ID e Configuration ID públicos foram informados pelo operador; seus valores não são reproduzidos em exemplos de configuração. O operador informou `v26.0` nos exemplos de Configuração da API; nenhum segredo foi solicitado em chat. Essas declarações não comprovam elegibilidade aprovada como Tech Provider ou operação WABA/número.

O operador acionou “Obter conta de sandbox”; o painel orientou executar Cadastro incorporado e selecionar Sandbox Business/Sandbox WhatsApp Account. Ainda não executou essa autorização no LeadsHug. A tela Configuração mostrou webhook, token permanente, telefones e conta de teste, sem configuração Embedded Signup identificada. O painel informa32números de produção e1de teste; isso não comprova posse, saúde ou autorização de alteração de nenhum deles. Também informa que o app não publicado só recebe webhooks de teste do painel. Manter a preparação em sandbox; não publicar o app nem substituir callbacks de números existentes por inferência.

O operador localizou “Adicionar casos de uso / Adicionar produtos”, sem opção de login nessa lista. Ao abrir “Torne-se um Provedor de Tecnologia”, encontrou a pergunta sobre prestar serviços a clientes/outras empresas; o próprio painel informa que a identificação é irreversível. Root explicou que “Sim” corresponde ao modelo de conexão de empresas clientes já aprovado para o LeadsHug, no aplicativo dedicado a ele. Depois dessa orientação, o operador relatou a tela com “Login do Facebook para Empresas”, requisitos de teste, Verificação da empresa e do acesso e Análise do app. Isso confirma o acesso à seção empresarial; não comprova aprovação das verificações ou da análise. Nenhuma publicação ou submissão de análise foi executada nesta sessão.

Em “Login do Facebook para Empresas” surgiram Configurações, Início rápido e Configurações e modelos. O operador selecionou o modelo de Cadastro incorporado do WhatsApp com token de60dias e informou o Configuration ID após salvar. A confirmação exibiu variação Cadastro incorporado do WhatsApp, token de usuário do sistema, ativo Contas do WhatsApp e permissões `whatsapp_business_management`/`whatsapp_business_messaging` em acesso padrão. O modelo separado de mensuração é somente leitura e não foi adotado. A versão do Embedded Signup realmente executada ainda depende da configuração/SDK; a existência do modelo não é prova de compatibilidade ou autorização concluída.

Dados públicos da instalação obtidos: App ID, Configuration ID e `GRAPH_VERSION=v26.0`, conforme o painel do operador. Próximo checkpoint humano depende do runtime: configurar origem/domínios e callback após o gateway HTTPS validado. App Secret será preenchido somente no backend privado, sem trânsito no chat. Não criar configuração parcial: preencher o conjunto Meta no ambiente privado somente quando todos os campos necessários estiverem disponíveis.

## O que pode ser preparado agora na conta Meta

1. Acessar [Meus aplicativos](https://developers.facebook.com/apps/) na conta administradora do portfólio já existente. Concluir o cadastro de desenvolvedor se o painel o exigir e selecionar o portfólio correto no fluxo oferecido pela Meta.
2. Criar/configurar o aplicativo para WhatsApp Cloud API e a modalidade de Embedded Signup/Tech Provider disponível para essa conta. Conferir no painel elegibilidade, papéis de teste e requisitos de revisão. Ter um app criado não comprova que a modalidade foi liberada.
3. Configurar Facebook Login for Business e a configuração de Embedded Signup. Anotar **App ID**, **Configuration ID** e a **Graph version** admitida pelo app. Os nomes exatos das telas dependem do painel atual.
4. Conferir as permissões de gestão e mensagens do WhatsApp necessárias ao fluxo, incluindo `whatsapp_business_management` e `whatsapp_business_messaging`, conforme o app e seus recursos de teste. Não conceder escopos adicionais por conveniência.
5. Separar uma WABA/número de teste administrável e um interlocutor. Usar um número sem integração concorrente que precisaria ter seu callback substituído. Migração/coexistência e tomada de callback não pertencem a esta entrega.

Referências primárias: [Embedded Signup da Meta](https://www.postman.com/meta/whatsapp-business-platform/collection/du6gzjv/embedded-signup), [registro do número](https://www.postman.com/meta/whatsapp-business-platform/request/mk4p87j/register-phone-number) e [assinatura da WABA](https://www.postman.com/meta/whatsapp-business-platform/request/0yubu4i/subscribe-app-to-whatsapp-business-account). O fluxo genérico da coleção também contém billing de BSP, que não é adotado aqui. Durante a inspeção automatizada, developers.facebook.com respondeu429; a configuração efetivamente disponível deverá ser conferida na conta do operador.

## Campos da instalação

Preencher somente no ambiente privado local quando o runtime estiver pronto. Não enviar valores secretos no chat, commit, screenshots, traces ou logs. Os exemplos versionados permanecerão sem credenciais reais.

| Campo | Origem / uso |
| --- | --- |
| `META_APP_ID` | Identificador público do aplicativo. |
| `META_SIGNUP_CONFIG_ID` | Identificador público da configuração de Embedded Signup. |
| `GRAPH_VERSION` | Versão explicitamente admitida pelo app; frontend e backend devem usar a mesma. |
| `META_APP_SECRET` | Segredo do app, somente no backend. |
| `WEBHOOK_VERIFY_TOKEN` | Segredo local escolhido para a verificação do callback Meta. |
| `PUBLIC_ORIGIN` | Origem HTTPS real do gateway de teste; será registrada quando existir, sem hostname presumido. |
| `CHANNEL_CREDENTIAL_KEY_ID` | Identificador da chave de cifra da instalação. |
| `CHANNEL_CREDENTIAL_KEY` | Chave privada de32bytes em base64 canônico, usada para cifrar credenciais por canal. |

O token global `WHATSAPP_TOKEN` não será usado como credencial de cliente nem como fallback. O acesso do número será obtido na autorização e guardado cifrado no vínculo correspondente. Configuração Meta inteiramente ausente permite abrir a administração com o cadastro oficial indisponível; configuração parcial é erro que precisa ser corrigido.

## HTTPS e callback

O gateway local planejado usa porta8083 configurável (8082 já está ocupada por outro projeto) e entrega UI, API, WebSocket e webhooks pela mesma origem. Sua disponibilidade será checada antes do startup. A exposição externa ocorrerá depois de conferir o build servido e a autenticação local. Nenhum DNS ou túnel persistente foi criado.

Uma opção para teste é um Quick Tunnel temporário: ele fornece uma URL HTTPS gerada e termina quando o processo é encerrado. Não exige domínio/conta Cloudflare e muda de hostname a cada execução. Não tem garantia de disponibilidade; não representa publicação em produção. [Documentação oficial](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

Com a URL real disponível:

- Cadastrar exatamente essa origem nos campos de domínio/origem/URLs exigidos pela configuração Meta escolhida.
- Configurar o callback como `https://<origem-real>/webhooks/meta` e usar o mesmo segredo de verificação privado da instalação.
- Conferir o produto de webhook e os eventos necessários; a assinatura da WABA é uma etapa separada do fluxo implementado.
- Se o hostname temporário mudar, atualizar a configuração antes de repetir o teste. Não aplicar uma barreira de login interativo do túnel aos callbacks, pois Meta/Evolution precisam chamá-los sem navegador.

## Prova dos dois canais

Depois da implementação e validação local, cadastrar o oficial pela autorização Meta e o não oficial pelo QR na tela Números. O pareamento do aparelho será feito pelo operador. Aguardar confirmação do próprio número antes de enviar a mensagem de teste; eventos anteriores podem ser rejeitados sem replay garantido.

Para cada canal, conferir uma IN na BU correta e uma resposta OUT recebida pelo interlocutor. Não concluir a prova apenas por QR lido, lista de números, assinatura de WABA ou resposta do provider. App/HTTPS/aparelho indisponíveis mantêm esse critério pendente, sem substituir a operação real por um dublê.
