# LeadsHug — dossiê executivo do sistema

**Data de referência:** 2026-09-15

**Público:** liderança, produto, operação e engenharia
**Estado da evidência:** arquitetura-alvo e implementação local verificadas. Este documento não afirma saúde de produção, disponibilidade de provedores, volume de clientes ou sucesso de deploy sem prova operacional específica.

## 1. Resumo executivo

O LeadsHug é a central de relacionamento da Unifast. Seu objetivo é concentrar o atendimento por WhatsApp, o histórico de conversas, a operação de equipes e a evolução futura de CRM e automações em um núcleo multi-tenant.

O produto em desenvolvimento está concentrado em dois componentes: `LeadsHug/apps/api` (backend NestJS) e `LeadsHug/apps/web` (aplicação React). A arquitetura unifica mensagens de canais diferentes em uma única conversa por **Business Unit (BU) + contato**; para o operador, o canal é o meio de transporte, não um sistema separado.

### Situação para decisão de liderança

| Tema | Situação verificável | Leitura executiva |
| --- | --- | --- |
| Núcleo de atendimento | Implementado e coberto por testes locais | Há base para identidade, multi-tenancy, números/BUs, canais, inbox, resposta, histórico e API pública. |
| Canal oficial WhatsApp | Implementado como piso arquitetural | O código integra Meta Cloud API, mas este dossiê não comprova que um número oficial esteja saudável em produção. |
| Canal não oficial | Adaptador Evolution/Baileys presente e condicionado por configuração | É capacidade opcional, com maior risco operacional e sem autorização para misturá-lo automaticamente ao fluxo oficial. |
| Typebot | Gestão, gatilhos e ponte de runtime implementados e testados localmente | Falta corrigir uma lacuna alta de isolamento multi-tenant em gatilhos globais, provar uma troca real por número oficial e decidir contrato completo de falha, retry, idempotência e auditoria. |
| CRM e campanhas | Fundamentos de histórico/atividade existem; CRM completo e campanhas não são capacidade concluída do núcleo | São fases posteriores, não promessas já entregues. |
| Legados | Retidos apenas como referência | Não são dependência de runtime, rollback, fonte de leitura/escrita ou destino de novas funcionalidades. |

### Decisões prioritárias sugeridas

1. Definir a prioridade imediata entre concluir o Typebot em canal oficial real, evoluir a identidade visual aprovada e iniciar CRM.
2. Para Typebot, aprovar o contrato de correlação, entrega, falha, retry, idempotência e auditoria antes de ampliar automações.
3. Definir os critérios de pronto para ambiente/cliente: número oficial, domínio/cookies, segredos, migrações, monitoramento e responsável operacional.
4. Definir a ordem de negócio para CRM, templates, campanhas e disparos; esses itens exigem contratos próprios e não devem entrar por inferência.

## 2. O que o produto resolve

O LeadsHug procura evitar que uma equipe atenda o mesmo cliente em múltiplas ferramentas, perca histórico entre números ou exponha conversas entre clientes. Seus princípios são:

- uma conversa pertence à combinação **BU + contato**, independentemente de ter vindo do canal oficial ou não oficial;
- uma BU é o número de WhatsApp e é a menor unidade de permissão, histórico e atendimento;
- cada Mantenedora é uma organização cliente; ela contém Setores e BUs;
- usuários têm papéis e grants nas BUs que podem operar;
- regras de canais e integrações externas são aplicadas no backend, preservando a autoridade do LeadsHug sobre dados, permissões e auditoria.

O mandato e o vocabulário canônicos estão em [project_mandate.md](../../project_mandate.md) e [domain_entities.md](../../domain_entities.md).

## 3. Mapa de responsabilidades e repositórios

```text
Usuários/gestão
      │
      ▼
LeadsHug (produto)
├── apps/web                 Interface operacional React
├── apps/api                 Núcleo NestJS, regras, APIs, webhooks e dados
├── leadshug-foundation      Autoridade de produto, governança, ADRs e TODOs
└── leadshug-engineering     Método de engenharia, guardas e workflows

Referências delimitadas, fora do runtime do núcleo:
├── Central-Whatsapp         Repositórios legados independentes
├── api-oficial / hub-whatsapp embutidos  Snapshots legados congelados
└── whatsflow_v2             Referência de lições de engenharia
```

| Camada | Responsabilidade | Não faz |
| --- | --- | --- |
| `leadshug-foundation` | Escopo de produto, decisões, contratos, critérios de aceite e TODOs aprovados | Não substitui código, testes ou operação. |
| `leadshug-engineering` | Regras, workflows, verificação e ciclo Codex–Claude | Não decide escopo de produto. |
| `apps/api` | Domínio, autorização, persistência, integrações, webhooks e APIs | Não entrega segredos ao navegador. |
| `apps/web` | Interface operacional e consumo do BFF | Não contém regra de negócio ou credencial de provedor. |
| Adaptadores externos | Meta, Evolution, Typebot, e-mail | Não têm autoridade sobre tenancy, conversa, usuário ou auditoria. |

As referências de compatibilidade `delphi-ai/` e `foundation_documentation/` existentes dentro do checkout do produto apontam, respectivamente, para Engineering e Foundation. São caminhos de compatibilidade, não autoridades atuais.

## 4. Arquitetura do núcleo

```text
                   ┌─────────────────────────────────────────────────┐
                   │                  React Web                      │
                   │  login · painel · BUs · inbox · histórico       │
                   │  usuários · setores · integração · Typebot      │
                   └────────────────────┬────────────────────────────┘
                                        │ cookie de sessão / BFF
                                        ▼
┌───────────────┐             ┌───────────────────────────────────────┐
│ Meta Cloud API│─webhook────►│ NestJS API                             │
└───────────────┘             │ ├─ BFF /api/bff                       │
┌───────────────┐             │ ├─ API pública /api/v1                │
│ Evolution API │─webhook────►│ ├─ API interna /api/internal           │
└───────────────┘             │ └─ Webhooks /webhooks                 │
                              │                                       │
┌───────────────┐             │ Domínio: acesso, tenancy, inbox,       │
│ Typebot Cloud │◄───────────►│ canais, histórico, integrações         │
└───────────────┘             └───────────────┬───────────────────────┘
                                                │ Prisma
                                                ▼
                                     ┌──────────────────────┐
                                     │ PostgreSQL 16         │
                                     │ dados e migrations    │
                                     └──────────────────────┘
```

### Superfícies de entrada

O backend possui quatro superfícies deliberadamente separadas, cada uma com autenticação própria:

| Superfície | Consumidor | Controle de acesso | Uso principal |
| --- | --- | --- | --- |
| BFF `/api/bff` | Web LeadsHug | Cookie de sessão e grants | Operação humana: inbox, usuários, BUs, setores, histórico, integrações e onboarding. |
| API pública `/api/v1` | Parceiros/sistemas externos | API key limitada a BUs | Consultar contas/conversas/mensagens e enviar, assumir ou liberar atendimentos. |
| API interna `/api/internal` | Serviço de bootstrap | `x-internal-token` | Criar Mantenedora, BU e OWNER em transação. |
| Webhooks `/webhooks` | Meta e Evolution | Assinatura Meta ou segredo Evolution | Receber e normalizar eventos de provedores. |

Há ainda `/health`, WebSocket `/ws` e rotinas periódicas. Eles não substituem as quatro superfícies de negócio.

## 5. Camadas funcionais atuais

| Domínio | O que existe no núcleo | Maturidade |
| --- | --- | --- |
| Identidade e acesso | Login por cookie, convite, definição/troca de senha, recuperação limitada, bloqueio de tentativas, usuários e três papéis (`OWNER`, `ADMIN`, `ATENDENTE`) | Implementado localmente |
| Tenancy | Mantenedora, Setor, BU, grants diretos e expansões de setor/Mantenedora, filtros por escopo | Implementado localmente |
| Onboarding e configuração | Bootstrap interno, cadastro de BUs, módulos da instalação, marca, perfil, arquivos de logo/avatar e telas administrativas | Implementado localmente; evolução de cores por tema aguarda aprovação específica |
| Canais | Cadastro/consulta/conexão de canais por BU, Meta oficial e Evolution não oficial, QR para não oficial | Implementado em código; saúde de provedor/produção não comprovada aqui |
| Atendimento | Fila, inbox, leitura, não lidas, assumir, responder, encerrar e reabrir conversa | Implementado localmente |
| Histórico e auditoria | Histórico consultável, exportação, catálogo de atividades e logs de ações | Implementado localmente; sem equivaler a um CRM completo |
| Tempo real | WebSocket autenticado por cookie, com publicação filtrada por BU | Implementado localmente |
| API para parceiros | Chaves por Mantenedora/BU, consultas, envio e claim/release | Implementado localmente; limite atual é em memória |
| Typebot | Catálogo, links de editor/criação, gatilhos, sessões, resposta pelo canal Meta e tratamento de indisponibilidade | Em validação externa; contrato completo de entrega/auditoria pendente |
| CRM, templates, disparos e campanhas | Referenciados no roadmap e/ou em legados | Planejados; não tratá-los como capacidade concluída do novo núcleo |

### Interface Web existente

O frontend possui telas para login, perfil, painel, wizard/onboarding, números, setores, usuários, inbox, histórico, integrações, Typebot e identidade visual. A existência de uma tela demonstra a superfície do produto; não é, por si só, prova de operação em ambiente produtivo.

## 6. Modelo de dados e isolamento

```text
Mantenedora (organização cliente)
 ├── Setor (agrupamento operacional)
 │    └── Business Unit / BU (número WhatsApp)
 │         ├── Canais: OFICIAL e/ou NAO_OFICIAL
 │         ├── Grants de usuários e papéis
 │         ├── Conversas (BU + contato é único)
 │         │    └── Mensagens
 │         └── Gatilhos e sessões Typebot, quando aplicável
 ├── Usuários, configurações, API keys e arquivos
 └── Atividades/auditoria e configuração de webhook de saída
```

| Regra de domínio | Consequência operacional |
| --- | --- |
| A BU é o número | Uma mesma Mantenedora pode operar vários números sem misturar filas, permissões ou histórico. |
| Grant é materializado na BU | Um usuário só lê ou atua nas BUs a que possui acesso; Setor facilita concessão, mas não substitui o escopo da BU. |
| Conversa é única por BU + contato | Trocar o transporte não cria outro histórico de atendimento para o mesmo par. |
| Mensagem mantém origem de canal | A operação vê uma timeline unificada, mas o sistema preserva pelo qual canal entrou/saiu. |
| Logs de atividade têm catálogo | Ações relevantes podem ser consultadas e auditadas em vez de depender só de logs técnicos. |

O banco é PostgreSQL via Prisma, com migrations versionadas. Toda alteração de esquema deve incluir migration e validação de banco conforme a Constituição do projeto.

## 7. Canais, integrações e regras operacionais

### 7.1 WhatsApp oficial — Meta Cloud API

É o piso do produto: o backend exige token de envio para iniciar. O canal é associado a uma BU por `phoneNumberId`/`wabaId` e recebe webhook assinado com `X-Hub-Signature-256` sobre o corpo bruto. Sem `META_APP_SECRET`, o produto recusa o webhook.

Regra importante: texto livre no canal oficial depende da janela de 24 horas desde a última mensagem de entrada. A tela/API recebe o estado da janela; se ela estiver fechada, o núcleo não troca silenciosamente para outro canal nem simula suporte a templates que não pertencem ao escopo atual.

**Estado:** integração e regras presentes no núcleo. Uma operação real requer número oficial, cadastro de webhook, segredos, ambiente e prova manual próprios.

### 7.2 WhatsApp não oficial — Evolution/Baileys

O caminho não oficial é opcional por instalação (`LH_CHANNEL_UNOFFICIAL`) e depende de `EVOLUTION_API_URL` e `EVOLUTION_API_KEY`. Cada BU pode ter sua instância Evolution e expor QR de pareamento. O webhook recebe um segredo no caminho, comparado em tempo constante, porque a Evolution não assina o payload como a Meta.

**Estado:** adaptador, controller e tela de canal existem. É uma capacidade com risco operacional e de plataforma maior; não deve ser acionada como fallback automático do oficial, nem misturada ao Typebot oficial sem decisão/validação próprias.

### 7.3 Typebot Cloud

O Typebot continua responsável por edição e execução de seus fluxos; o LeadsHug continua responsável por Mantenedora, usuários, BUs, contatos, conversas, canais, permissões e auditoria.

No núcleo existem catálogo de bots, criação/edição em nova aba, gatilhos de `NOVA_CONVERSA` ou `PALAVRA_CHAVE`, sessões por bot/BU/contato e envio de respostas pelo adaptador Meta. Credenciais Typebot ficam somente na API. Indisponibilidade de catálogo é devolvida à Web como estado recuperável, em vez de expor token ou gerar erro genérico.

**Estado:** implementação automatizada localmente validada, mas não pronta para ampliação multi-tenant. Permanecem três pendências: (a) corrigir a lacuna de isolamento descrita na seção 8.4, (b) provar uma mensagem real Typebot → número oficial → resposta, e (c) aprovar e implementar a semântica de correlação, entrega, falha, retry, idempotência e auditoria persistente.

### 7.4 E-mail transacional

O e-mail é usado para convite e acesso, via chave de provedor configurada no servidor (documentação indica Resend). Se o envio não estiver configurado, o fluxo devolve o link para o administrador compartilhar; ausência de e-mail não torna o navegador portador de segredo.

**Estado:** cliente e testes existem. Entregabilidade de domínio/remetente exige configuração operacional do ambiente.

### 7.5 Webhook de saída

Cada Mantenedora pode configurar URL e segredo próprios para receber eventos. O envio é best-effort, com timeout curto e uma tentativa adicional; falhar não deve derrubar o evento original.

**Implicação:** há uma integração de saída simples, não uma fila durável com garantia de entrega. Caso o negócio exija entrega garantida, reprocessamento, DLQ ou observabilidade por evento, isso precisa de TODO e contrato específicos.

## 8. Fluxos de mensageria

### 8.1 Entrada pelo canal oficial

```text
Contato no WhatsApp
        │
        ▼
Meta Cloud API
        │ POST /webhooks/meta (assinatura HMAC no corpo bruto)
        ▼
MetaWebhookController
        ├── valida origem; sem segredo/assinatura, recusa
        ├── grava evento cru de webhook
        └── normaliza para MensagemRecebida
                    │
                    ▼
IncomingService
        ├── encontra/cria conversa por BU + contato
        ├── persiste Message com origem OFICIAL
        ├── reabre conversa fechada quando aplicável
        ├── publica evento WebSocket apenas a grants da BU
        └── se texto e gatilho Typebot válido: inicia/continua bot
                    │
                    ▼
PostgreSQL (conversa, mensagem, evento, sessão) ──► Web React / Inbox
```

O payload bruto do webhook fica em `webhook_events` e há rotina de expurgo de 90 dias. Esse registro ajuda investigação, mas não substitui um contrato de auditoria de entrega ponta a ponta.

### 8.2 Entrada pelo canal não oficial

```text
WhatsApp / Baileys → Evolution API
        │ POST /webhooks/evolution/{segredo}
        ▼
EvolutionWebhookController
        ├── valida segredo no caminho
        ├── grava evento cru
        └── normaliza → IncomingService
                         │
                         └── mesma conversa, persistência e publicação por BU
```

O destino abaixo do adaptador é o mesmo. Isso preserva a unidade da conversa e evita manter duas inboxes para um mesmo número/contato.

### 8.3 Resposta humana

```text
Operador na Web
        │ BFF autenticado por cookie
        ▼
ConversationsController → AccessService / escopo BU
        │
        ├── verifica canal e janela de 24h quando aplicável
        ├── MetaClient ou EvolutionClient envia texto
        ├── persiste mensagem de saída e autoria
        ├── atualiza status/atribuição da conversa
        └── registra atividade
```

Uma resposta humana pode autoatribuir a conversa quando ela não tem dono; não toma uma conversa já atribuída a outro atendente. A API pública aplica lógica equivalente, mas marca o atendente como externo.

### 8.4 Resposta automatizada Typebot — lacuna atual de isolamento

```text
Mensagem oficial de texto recebida
        │
        ▼
IncomingService identifica gatilho ativo por BU
        │
        ▼
Typebot Cloud (iniciar ou continuar sessão)
        │ mensagens textuais de resposta
        ▼
MetaClient envia para o contato
        │
        ▼
IncomingService registra a saída na mesma conversa
```

O fluxo local está coberto por testes, mas a passagem real por canal oficial ainda é uma pendência explícita. Também não há decisão aprovada para tornar retry/idempotência/auditoria de entrega uma garantia persistente.

**Risco alto identificado em revisão:** a consulta de runtime dos gatilhos aceita `{ buId: null }` sem também restringir a Mantenedora do bot à Mantenedora da BU que recebeu a mensagem. Assim, um gatilho global criado por uma Mantenedora pode ser avaliado para uma BU de outra Mantenedora. A escrita administrativa pelo BFF restringe o cadastro à Mantenedora correta, mas essa proteção não está repetida na leitura do runtime. Até que o código seja corrigido e coberto por regressão cross-tenant, Typebot não deve ser habilitado para automações globais multi-tenant.

## 9. Segurança e controles relevantes

| Controle | Como está estruturado |
| --- | --- |
| Isolamento de tenant | BFF, API pública e fluxos principais aplicam escopo de BUs; uma BU de outra Mantenedora não deve ser revelada como existente. **Exceção crítica identificada:** a leitura de gatilhos globais Typebot no runtime ainda não filtra Mantenedora (seção 8.4). |
| Papéis | `OWNER`, `ADMIN` e `ATENDENTE`; privilégios são avaliados no domínio/backend. |
| Sessão | Cookie assinado; WebSocket autentica no handshake e não recebe token na URL. |
| Tempo real | Eventos são enviados apenas para sockets cujo escopo contém a BU. O escopo é capturado na conexão; novo grant requer reconexão. |
| Webhook Meta | Assinatura HMAC do corpo bruto; ausência de segredo é negação. |
| Webhook Evolution | Segredo no caminho e comparação em tempo constante; a URL deve ser tratada como credencial. |
| Segredos | Tokens Meta, Evolution, Typebot, e-mail, sessão e serviço interno ficam em variáveis protegidas; não são entregues ao frontend. |
| Navegador | CORS por origem explícita com credenciais; `*` não é permitido para esse modelo de sessão. |
| Banco | Migration pendente é detectada no boot e pode resultar em resposta explícita de banco desatualizado. |
| Arquivos | Logo/avatar usam volume configurado; sem volume, upload é recusado em vez de gravar localmente sem garantia. |

## 10. Operação, entrega e qualidade

### Stack e topologia declarada

| Componente | Tecnologia declarada |
| --- | --- |
| Backend | NestJS 11, TypeScript, Node.js 22+ |
| Frontend | React 18, Vite 5, TypeScript, Nginx em container |
| Persistência | PostgreSQL 16 + Prisma 6 |
| Contêineres | Docker; compose local e perfil de deploy |
| Destino de entrega | Railway, com definições separadas de API e Web |
| Testes | Vitest para API/Web, E2E da API e Playwright para fluxos Web |

O frontend recebe a URL de API em `/config.js`, gerado no início do container. Isso permite usar a mesma imagem em ambientes diferentes sem recompilar para trocar a URL da API.

### Evidência de qualidade disponível

O checkpoint completo persistido no [TODO Typebot](../../todos/active/features/TODO-leadshug-typebot-automation-integration.md) registra 103 testes unitários de API, 16 de Web, 217 E2E de API, 20 de navegador e 320 de cobertura. Durante este levantamento, `task check` passou novamente com 104 testes unitários de API, 16 de Web, lint, typecheck da API/Web e amostras dos guardrails; esse comando e resultado estão registrados no TODO deste dossiê. As duas evidências são locais e não substituem CI remoto ou validação de produção.

As regras de entrega exigem que mudanças de contrato, schema, topologia ou fluxo Web incluam testes e validações proporcionais. O projeto possui gates locais de contrato, migration, E2E e Playwright, mas a proteção de `main` no GitHub depende de condição de plano ainda não habilitada.

## 11. O que ainda não se deve afirmar

Para evitar desalinhamento com liderança e clientes, não é correto concluir a partir do código local que:

- algum ambiente Railway está saudável ou atende tráfego de produção;
- um número oficial Meta está configurado, recebeu webhook ou respondeu mensagens reais;
- o canal não oficial está pareado, estável ou autorizado para uma operação específica;
- Typebot concluiu uma conversa real por WhatsApp oficial;
- e-mail está sendo entregue por domínio verificado;
- CRM, campanhas, modelos ou disparos já são capacidades completas do novo núcleo;
- legados foram desligados, migrados, sincronizados ou podem servir como rollback.

Essas afirmações exigem provas operacionais ou decisões aprovadas separadamente.

## 12. Legados e fronteiras

| Sistema | Papel atual | Uso permitido |
| --- | --- | --- |
| `LeadsHug/api-oficial` e `LeadsHug/hub-whatsapp` | Snapshots legados embutidos | Entender comportamento, vocabulário, payloads e cenários de regressão; não editar/deployar como parte de novo trabalho. |
| `Central-Whatsapp/api-oficial` e `Central-Whatsapp/hub-whatsapp` | Repositórios legados independentes | Inspirar requisitos e lições operacionais sob a política de legado; não copiar código, dados, configuração ou topologia. |
| `whatsflow_v2` | Referência de falhas e práticas | Extrair lições sobre filas duráveis, idempotência, catch-up, DLQ, observabilidade e testes de tenancy. |

Nenhum deles é dependência de runtime do núcleo. Qualquer retirada, sincronização, migração ou mudança de ownership/deploy exige decisão operacional explícita.

## 13. Riscos, lacunas e próximos passos recomendados

| Prioridade | Tema | Risco/lacuna | Próximo passo de decisão |
| --- | --- | --- | --- |
| P0 | Isolamento Typebot multi-tenant | Gatilho global sem filtro de Mantenedora no runtime pode executar bot de outra Mantenedora | Criar e aprovar TODO de correção, com teste cross-tenant; não habilitar automações globais antes disso. |
| P0 | Prova de canal oficial + Typebot | A automação está verde localmente, mas não há prova de mensagem real completa | Após corrigir o isolamento, disponibilizar número oficial e realizar validação manual registrada. |
| P0 | Semântica Typebot de entrega | Não há contrato aprovado para correlação, retry, falha, idempotência e auditoria persistente | Aprovar o comportamento esperado antes de ampliar automações. |
| P0 | Prontidão de ambiente | Código não é prova de domínio, cookies, segredos, migrations e observabilidade em runtime | Definir checklist e responsável de stage/produção. |
| P1 | Canal não oficial | Maior complexidade de pareamento, sessão e política de plataforma | Decidir quando/onde habilitar e validar isoladamente; não assumir fallback do oficial. |
| P1 | Evolução visual | TODO de cores por modo está definido, mas aguarda aprovação | Decidir se é prioridade de produto imediata. |
| P1 | Fechamento de governança CI | Geração de gates está implementada localmente, mas seu TODO está em ativo aguardando closeout formal | Encerrar em tarefa de processo própria, sem misturar com produto. |
| P2 | CRM | Há histórico e atividades, não CRM/funil completo | Definir primeiro recorte de lead, funil e ficha relacional. |
| P2 | Campanhas/templates/disparos | Ainda não pertencem ao núcleo concluído | Definir requisitos, política de canais e contrato de entrega antes de implementar. |
| P2 | Observabilidade de integrações | Webhook de saída é best-effort e não há evidência de DLQ/fila durável no núcleo | Decidir necessidade de garantias de entrega e orçamento operacional. |

## 14. Sequência recomendada para os próximos passos

1. **Corrigir o isolamento Typebot:** implementar o filtro de Mantenedora no runtime e testes de regressão cross-tenant antes de habilitar gatilhos globais.
2. **Concluir a verdade operacional do canal oficial:** validar número, webhook, sessão/cookies, migrations e uma conversa real controlada.
3. **Fechar a automação com contrato:** decidir idempotência, retries, correlação e trilha de auditoria Typebot; depois validar o fluxo real.
4. **Estabelecer baseline de operação:** checklist de stage/produção, responsáveis, monitoramento, logs, backup/restore e critérios de corte.
5. **Priorizar experiência e operação humana:** decidir se o TODO de identidade visual é a próxima entrega e avaliar lacunas reais da inbox com usuários.
6. **Definir CRM como domínio próprio:** desenhar lead, funil e relação com conversa/histórico antes de introduzir tabelas ou telas.
7. **Planejar campanhas por contrato:** somente após decisão de canal, janela Meta, templates, listas, limites e rastreabilidade.

## 15. Índice de evidências

| Assunto | Fonte |
| --- | --- |
| Mandato e entidades | [project_mandate.md](../../project_mandate.md), [domain_entities.md](../../domain_entities.md) |
| Autoridade e invariantes | [project_constitution.md](../../project_constitution.md) |
| Stack e topologia | [technology_baseline.md](../../technology_baseline.md), [`apps/api/package.json`](../../../LeadsHug/apps/api/package.json), [`apps/web/package.json`](../../../LeadsHug/apps/web/package.json), [`docker-compose.yml`](../../../LeadsHug/docker-compose.yml) |
| Decisões arquiteturais | [`docs/adr`](../../../LeadsHug/docs/adr/README.md), especialmente ADRs 0002, 0003, 0006, 0008, 0009, 0010, 0013, 0015, 0016 e 0025 |
| Superfícies e contratos | [`docs/artifacts/api.yml`](../../../LeadsHug/docs/artifacts/api.yml), [`apps/api/src/app.module.ts`](../../../LeadsHug/apps/api/src/app.module.ts) |
| Dados e tenancy | [`apps/api/prisma/schema.prisma`](../../../LeadsHug/apps/api/prisma/schema.prisma) |
| Fluxo de entrada | [`incoming.service.ts`](../../../LeadsHug/apps/api/src/domain/inbox/incoming.service.ts), controllers Meta/Evolution |
| Fluxo de atendimento | [`conversations.service.ts`](../../../LeadsHug/apps/api/src/domain/inbox/conversations.service.ts), controller BFF de conversas |
| Typebot | [TODO ativo Typebot](../../todos/active/features/TODO-leadshug-typebot-automation-integration.md), client/integração da API |
| Legados | [architecture truth and legacy boundaries](leadshug-architecture-truth-and-legacy-boundaries-20260915.md), [Central-Whatsapp policy](../../policies/central_whatsapp_independent_legacy_policy.md) |

---

### Leitura final para liderança

O LeadsHug já tem um núcleo arquitetural coerente para centralizar relacionamento por WhatsApp com isolamento por cliente, número e usuário. O ponto decisivo não é iniciar mais frentes ao mesmo tempo: é converter a base local já construída em uma operação comprovada do canal oficial, fechar a semântica de automação e então escolher o próximo domínio de negócio com evidência e prioridade claras.
