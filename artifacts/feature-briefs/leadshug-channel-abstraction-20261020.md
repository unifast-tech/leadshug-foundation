# LeadsHug — Channel abstrato e implementações de transporte

**Data:** 2026-10-20. **Perfil:** Strategic / CTO-Tech-Lead; NestJS, React, PostgreSQL, Prisma e Docker. Gate0: Genesis rejeitado, projeto existente. Formato baseado em delphi-ai/templates/feature_brief_template.md.

## Artifact Role

- **Why this brief exists now:** orientação arquitetural transmitida pelo usuário altera o enquadramento dos templates e do primeiro envio. Definir Channel comum e avaliar os impactos antes de elaborar o contrato de refatoração.
- **What this brief is not:** implementação, novo contrato canônico de módulo, revisão pré-APROVADO concluída ou autorização de produto/runtime. O parecer deste enquadramento é consultivo; o TODO tático futuro terá escopo, decisões, DoD e gates próprios.

## Source Idea / Request

Em2026-10-20 o usuário trouxe o alinhamento do responsável: Channel é a abstração, WhatsApp oficial/não oficial são implementações concretas, o código de negócio solicita sendMessage sem conhecer a integração escolhida. Dependência de abstrações, DI e substituição comportamental são direção confirmada. O usuário esclareceu em seguida que as implementações concretas devem permanecer abertas para Instagram, Facebook/Messenger, Telegram e outros canais futuros. Oficial/não oficial são as primeiras implementações, não uma lista fechada. A abertura arquitetural é requisito atual; integrações adicionais terão seus contratos próprios.

## Problem / Desired Outcome

- **Problem:** já há interfaces MetaClient/EvolutionClient e DI, mas os serviços de atendimento/bot importam os dois contratos específicos e selecionam o provedor. A inversão existe no nível HTTP, sem contrato comum de transporte para o negócio.
- **Desired outcome:** consumidores comuns operam Channel; resolução autorizada seleciona uma implementação registrada, inicialmente oficial ou não oficial, com extensão para novos canais sem alterar os consumidores comuns. Identidade, grants, credencial, proveniência, aceitação de mensagens e regras atuais continuam explícitas.
- **Why now:** implementar autoria ou primeiro envio sobre dependências atuais consolidaria o acoplamento antes desta correção estrutural solicitada.

## Constraints / Non-Goals

- Canon atual: BU é número WhatsApp, conversa por BU/Contato; BuChannel é vínculo persistido. **Channel abstrato é contrato de execução**, distinto da entidade Prisma. Não transformar tabela em hierarquia de herança nem generalizar identidade de Telegram nesta frente.
- Usar abstract class Channel como contrato tipado; classes concretas implementam o comportamento comum. Interfaces com token também realizam DIP, mas a classe abstrata expressa literalmente a direção recebida e pode ser token runtime no NestJS.
- Como várias BUs e os dois transportes coexistem no processo, não vincular Channel globalmente a um único useClass por ambiente. Um resolver/fábrica abstrato retorna Channel para o vínculo server-side autorizado; registro e composição conhecem os concretos.
- Seleção só por channelId/BU/identidade confiáveis, com grants atuais. Nada de provider/credencial arbitrários do browser. Estado/segredos ficam no backend; nenhuma instância singleton pode guardar contexto mutável da última BU/credencial usada.
- Não repetir resolução/grant/cifra em cada adapter: reutilizar o owner atual de identidade/credenciais; contrato de contexto precisa preservar generation/epoch/identidade e definir explicitamente a captura da versão de credencial e os respectivos fences, sem expor segredo a consumers comuns. O resolver atual NÃO autoriza ator/grant e NÃO devolve versão ativa; esses contratos pertencem à nova composição sobre contexto autorizado, não são garantias já implementadas.
- Liskov: implementação concreta pode substituir o contrato base respeitando precondições/pós-condições/invariantes; não exige usar o pai em todo lugar que exige um filho. Métodos auxiliares privados são legítimos; o negócio não faz cast para chamar extensão concreta.
- Operação comum inicial: envio textual já existente. Tipos e resultados normalizados precisam definir aceito, recusa comprovada, bloqueio de política/capacidade e resultado incerto; não prometer sucesso externo, exactly-once ou retry automático. Compatibilidade dos erros públicos atuais deve entrar no contrato futuro, sem mudança implícita nesta minuta.
- Capacidades diferentes são contratos explícitos. Gestão de templates, envio de template e cadastro/QR não devem virar métodos obrigatórios não implementados nos outros canais. Consumidores de capacidade dependem da abstração dessa capacidade, obtida sem casts/conhecimento do concreto.
- Webhooks/HTTP/OAuth/QR permanecem específicos na fronteira de integração; payloads de entrada são normalizados antes do negócio. Falar com Meta dentro de seu adapter é o comportamento esperado da implementação concreta.
- Providers concretos encapsulam protocolo/IDs/credencial/erros de transporte. Domínio conserva autorização, persistência, aceitação/dedupe e políticas de atendimento, por contratos; esconder tudo num mega-adapter não satisfaz a direção.
- Sem novo canal, alteração de BU, desconexões, credenciais novas, chamadas Meta, mudança Delphi, worktrees/cópias, gitlinks/.gitmodules ou deploy. Não ler/listar/stat/hash/percorrer/montar api-app/.local-files nem ler .env/.env.testing.

## Explicit Extension Contract — human clarification2026-10-20

- Channel é uma abstração de comunicação extensível. WhatsApp oficial e não oficial são os concretos iniciais; Instagram, Facebook/Messenger, Telegram e outros são destinos futuros previstos, sem limite de dois provedores na arquitetura.
- Novo canal acrescenta implementação/adapter, registro explícito na composição e testes do contrato. Atendimento, API e Typebot continuam consumindo os mesmos ports, sem novos if/switch por provider. O registro é configurado por DI; não é descoberta dinâmica de código/plugins não confiáveis.
- O contrato comum usa referências de canal/destinatário e resultados de domínio. Não exigir WABA, phoneNumberId, nome de instância, QR, número E.164 ou janela específica do WhatsApp como campos/precondições universais. Tradução de endereçamento, credenciais, protocolo e requisitos próprios pertence à implementação/capacidade apropriada.
- Capacidades como gestão de templates são extensões tipadas, não métodos obrigatórios de Instagram/Telegram. A resolução informa capacidade suportada/indisponível de forma explícita e mantém autorização server-side; não usar casts para concretos.
- A prova de extensão planejada para o contrato ST-CON-06 inclui uma implementação fake adicional, independente de formatos WhatsApp, passando pelo mesmo resolvedor e pelos consumers comuns. Isso prova o ponto de extensão interno, não uma integração real com outra rede.
- O modelo persistido atual ainda representa BU/número WhatsApp. Cada integração futura tratará sua identidade externa, vínculos, autenticação e recebimento normalizado em TODO próprio; adicionar um adapter sozinho não será apresentado como entrega completa de uma nova rede. A abertura do port evita replicar essa limitação de persistência no contrato comum.

## Canonical Touchpoints

- **Constitution impact:** ST-CON-06 preserva o domínio WhatsApp existente e estabelece port extensível; ativar outras redes no futuro exige contrato e consolidação explícitos de identidade/BU/contato, porque a BU atual é número WhatsApp. A abstração comum não deve impor essa identidade ao protocolo de todos os canais.
- **Roadmap impact:** coerência do núcleo unificado atual, sem mudar horizonte ou gate derivado.
- **Primary module candidates:** modules/integrations-and-channels.md.
- **Secondary module candidates:** modules/inbox-and-conversations.md; identidade/grants e bot existentes são regressões obrigatórias.
- **Program:** BLG-leadshug-channel-readiness-and-history. ST-CON-05 e ST-CON-04 voltam a reconvergência antes de qualquer aprovação válida sobre a nova arquitetura.

## Evidence / References

Leitura pública delimitada em2026-10-20; root confirmou os HEADs por rev-parse sem varrer repositório API. Produto inalterado: root80e3940126f22a941f90dba4f5e801b6c0eb2f58, API db5a86758a165fac8a1ab587599c37b17890530c, Web74b9d4b714044829796f875d00553f077c1c329d; confirmar heads no handoff. Foundation iniciale0cf064e. Sem testes/runtime nesta análise.

| Finding | Exact source | Consequence |
| --- | --- | --- |
| Interfaces de provedor existem e têm implementações HTTP | api-app/src/integrations/meta/meta.client.ts:20/42; integrations/evolution/evolution.client.ts:14/28 | DIP parcial já presente; não afirmar dependência de classes concretas nesses serviços |
| Atendimento injeta ambos os providers e faz if OFICIAL | api-app/src/domain/inbox/conversations.service.ts:28/29/297-317 | alta camada conhece seleção e parâmetros técnicos; migrar consumidor comum para Channel |
| Resposta de Typebot faz escolha duplicada | api-app/src/domain/inbox/incoming.service.ts:44/45/82-96 | toda saída comum, inclusive bot, deve convergir; trocar só Inbox deixa desvio |
| Mesma orquestração atende BFF/API pública; bot em Webhooks | api-app/src/surfaces/bff/bff.module.ts:98; public/public.module.ts:25; webhooks/webhooks.module.ts:22 | composição/injeção e harness devem convergir nas três superfícies |
| Resolver expõe campos específicos e segredo ao caller atual | api-app/src/domain/channels/channel-credential-resolver.ts:5-16/24-67 | novo boundary deve usar internamente o mecanismo sem vazar token ao negócio ou perder trust/readiness |
| Ingress já normaliza MensagemRecebida e aceita pela mesma identidade | api-app/src/domain/inbox/incoming.service.ts:12-32/52-69 | preservar normalização, proveniência/dedupe e fronteiras, não criar segunda aceitação |
| Cadastro específico depende de clients abstratos próprios | api-app/src/domain/channels/number-registration.service.ts:7/37; channels.service.ts:34/35 | não forçar OAuth e QR no contrato mínimo de enviar; avaliar capacidades/lifecycle separadamente |

Fontes primárias consultadas: [NestJS custom providers](https://docs.nestjs.com/fundamentals/custom-providers), que distingue interfaces apagadas e classe abstrata como token runtime; [Liskov/Wing1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf), substituição preserva propriedades do supertipo. Nenhuma equivalência entre regras dos provedores é inferida desses princípios.

## Candidate Architecture / Review Questions

Atendimento/bot → ChannelResolver abstrato, scoped → Channel abstrato → implementação registrada (inicialmente WhatsAppOfficialChannel ou WhatsAppUnofficialChannel) → adapter/clients do provedor. Esta é direção de enquadramento, não assinatura final de DTO nem classe implementada. Registro/composição seleciona concretos; consumidores comuns não importam MetaClient/EvolutionClient nem escolhem envio por enum de provider. Origem pode existir como metadado de auditoria/apresentação sem comandar dispatch no negócio.

| ID | Ambiguity | Why It Matters | Current Evidence | Handling |
| --- | --- | --- | --- | --- |
| AMB-ABS-01 | menor contrato comum de envio e resultado, política/readiness e compatibilidade de erro | não apagar regras oficiais nem classificar timeout como recusa definitiva | dois senders atuais, acceptance e resolver já separados | parecer concluído; congelar assinatura/testes/compatibilidade e races no TODO ST-CON-06 antes de aprovação |
| AMB-ABS-02 | descoberta tipada de capacidades para templates/lifecycle | evitar interface enorme, casts ou métodos no-op em implementações | ST-CON-05 planejado com domínio de modelos e provider adapter, ainda sem código | parecer concluído, ports tipados recomendados; ST-CON-05 reconverge para consumir capacidade abstrata |
| AMB-ABS-03 | alcance do primeiro recorte versus gestão de conexões | refatoração de todos os protocolos de onboarding pode engolir o objetivo de transporte comum | cadastro Meta/QR já testado, fronteiras explícitas | priorizar envio comum e avaliar lifecycle como capacidade separada; nenhum rewrite de cadastro implícito |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-CON-06 | Negócio usa Channel abstrato para o transporte existente | integrations-and-channels | inbox-and-conversations | contrato comum extensível/resolução autorizada/registro de implementações, inicialmente oficial e não oficial; prova com fake independente de WhatsApp; todos os senders comuns sem branch/import de provider; políticas, contratos públicos, credencial e aceitação preservados por critérios explícitos | teste de contrato compartilhado dos adapters + PostgreSQL/Playwright real e regressão BFF/API pública/bot; troca por fake Channel prova consumo abstrato; prova operacional dos recursos próprios no contrato futuro | create-next após enquadramento | assinatura/resultado/capacidades e fronteira de lifecycle precisam frozen TODO/reviews/APROVADO | não é novo provedor nem mudança de domínio BU |
| ST-CON-05 | Vendedor cria/submete/consulta modelos | integrations-and-channels | inbox-and-conversations | mesmo produto confirmado, domínio consome contrato abstrato de capacidade de template e credencial scoped, sem nova dependência de negócio em MetaClient | editor/submit/recovery/status com capacidade fake e adapter real em testes HTTP | reconverge existing | depende do contrato/cutover ST-CON-06 | vendedor envia para Meta sem aprovação ADMIN preservado |
| ST-CON-04 | Nova conversa usa Channel e catálogo comum | inbox-and-conversations | integrations-and-channels | consumo abstrato de envio/capacidades, contato/intent/idempotência/primeiro envio preservados | browser/PG com ambos canais e template elegível | reconverge existing | ST-CON-06 e05 | aprovação antiga de cadastro não autoriza este envio |

## Review / Disposition

Enquadramento pré-TODO revisado por parecer independente, com direção recomendada e cinco disposições integradas abaixo. Baseline consultivo publicadobddf9d92aea4eebd5d4e767afb2feba8432aa83a antes do parecer. [Relatório e resolução](../analysis/leadshug-channel-abstraction-framing-opinion-20261020.md). Parecer não substitui architecture_opinion/critique do futuro TODO refinado nem constitui aprovação de implementação. Próximo passo do programa: preparar ST-CON-06 específico com as decisões materiais abaixo e seus gates. Não solicitar APROVADO usando guardas de2026-10-19 do ST-CON-05, agora históricos. Nenhuma mudança de módulo canônico ou implementação é declarada por este brief.

| Finding / severity | Disposition | Consequence for the future tactical contract |
| --- | --- | --- |
| ABS-01 high — resultados atuais colapsam recusa/incerteza | Integrated | definir accepted com ID não vazio, blocked antes do dispatch, rejected comprovado e unknown após dispatch inconclusivo. Erros/códigos/status atuais exigem projeção pública explícita; timeout hoje não usa o mesmo tratamento do ID ausente. Mudança de comportamento/persistência deve entrar no contrato, não ser chamada só de refactor. |
| ABS-02 high — resolver atual não faz autorização por ator/BU nem retorna versão | Integrated | contexto server-side de conversa autorizada OU ingresso verificado; conferir owner BU/canal, nunca confiar em body. Identidade/generation/epoch preservadas; política de rotação de credencial distinta de retirada da identidade. Capturar versão não é fence automaticamente. Sem contexto mutável compartilhado. |
| ABS-03 high — fallback atual conflita com política de não trocar canal | Integrated | falhar explicitamente se o canal selecionado está ausente; seleção/janela pertencem a política de domínio por requisitos do canal, sem switch de provider. Formalizar correção intencional e contrato UI/API no TODO. |
| ABS-04 medium — DIP parcial | Integrated | diagnosticar precisamente interfaces por provider já existentes; falta abstração comum no negócio, não DI do zero. |
| ABS-05 medium — todos os senders/composição | Integrated | convergir Atendimento BFF/API pública e respostas Typebot, com módulo de composição exportado único; autenticações das superfícies preservadas. |

Direção das ambiguidades: AMB-ABS-01 usa resultados e política comuns, preservando o owner único MessageAcceptanceService; assinatura/error projection/races precisam freeze tático. AMB-ABS-02 usa ports abstratos pequenos para gerir e enviar templates, retornando capacidade tipada ou unsupported/unavailable antes do efeito; disponibilidade não concede autoridade. AMB-ABS-03 limita ST-CON-06 ao cutover completo do envio comum; cadastro/OAuth/QR preservados/regredidos em testes e lifecycle especializado será enquadrado separadamente quando necessário. Não declarar abstração concluída de todo onboarding nesta primeira entrega.

Estrutura recomendada: Channel e ChannelResolver abstratos de domínio; instâncias pequenas ligadas à operação, contexto privado imutável; clients HTTP existentes compartilhados sem estado por BU; resolução/composição conhece implementações. Orquestração comum de saída conserva política e tratamento de resultado e chama MessageAcceptanceService para aceitação/dedupe. Não criar novo owner de Message, vault, plugin scanner, escopo de request global ou locks externos globais.

Validação futura significativa: shared contract tests dos dois adapters; fake Channel para os consumers; envios concorrentes de BUs distintas; identidade antiga e rotação de credencial; ausência do canal selecionado; DTOs/códigos públicos explícitos; PG sender-first/echo-first. Inspeção do runner atual scripts/test-channels-local.sh:25 confirmou find amplo sobre API. Sua correção para inventário público positivo é pré-requisito ANTES de qualquer teste do futuro ST-CON-06; o runner não foi executado aqui. ST-CON-05 não pode permanecer como único dono futuro desse pré-requisito depois da mudança de ordem.

## Retire This Brief When

ST-CON-06 possuir contrato revisado/aprovado e seus resultados forem consolidados nos módulos; consumidores05/04 reconvergirem explicitamente. Enquanto isso este documento informa a preparação, não autoriza execução.
