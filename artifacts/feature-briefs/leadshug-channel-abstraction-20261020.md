# LeadsHug — Channel abstrato e implementações de transporte

**Data:** 2026-10-20. **Perfil:** Strategic / CTO-Tech-Lead; NestJS, React, PostgreSQL, Prisma e Docker. Gate0: Genesis rejeitado, projeto existente. Formato baseado em delphi-ai/templates/feature_brief_template.md.

## Artifact Role

- **Why this brief exists now:** orientação arquitetural transmitida pelo usuário altera o enquadramento dos templates e do primeiro envio. Definir Channel comum e avaliar os impactos antes de elaborar o contrato de refatoração.
- **What this brief is not:** implementação, novo contrato canônico de módulo, revisão pré-APROVADO concluída ou autorização de produto/runtime. O parecer deste enquadramento é consultivo; o TODO tático futuro terá escopo, decisões, DoD e gates próprios.

## Source Idea / Request

Em2026-10-20 o usuário trouxe o alinhamento do responsável: Channel é a abstração, WhatsApp oficial/não oficial são implementações concretas, o código de negócio solicita sendMessage sem conhecer a integração escolhida. Dependência de abstrações, DI e substituição comportamental são direção confirmada. Telegram é exemplo de extensão futura, sem solicitação de implementar outro provedor agora.

## Problem / Desired Outcome

- **Problem:** já há interfaces MetaClient/EvolutionClient e DI, mas os serviços de atendimento/bot importam os dois contratos específicos e selecionam o provedor. A inversão existe no nível HTTP, sem contrato comum de transporte para o negócio.
- **Desired outcome:** consumidores comuns operam Channel; resolução autorizada seleciona implementação oficial ou não oficial. Identidade, grants, credencial, proveniência, aceitação de mensagens e regras atuais continuam explícitas.
- **Why now:** implementar autoria ou primeiro envio sobre dependências atuais consolidaria o acoplamento antes desta correção estrutural solicitada.

## Constraints / Non-Goals

- Canon atual: BU é número WhatsApp, conversa por BU/Contato; BuChannel é vínculo persistido. **Channel abstrato é contrato de execução**, distinto da entidade Prisma. Não transformar tabela em hierarquia de herança nem generalizar identidade de Telegram nesta frente.
- Usar abstract class Channel como contrato tipado; classes concretas implementam o comportamento comum. Interfaces com token também realizam DIP, mas a classe abstrata expressa literalmente a direção recebida e pode ser token runtime no NestJS.
- Como várias BUs e os dois transportes coexistem no processo, não vincular Channel globalmente a um único useClass por ambiente. Um resolver/fábrica abstrato retorna Channel para o vínculo server-side autorizado; registro e composição conhecem os concretos.
- Seleção só por channelId/BU/identidade confiáveis, com grants atuais. Nada de provider/credencial arbitrários do browser. Estado/segredos ficam no backend; nenhuma instância singleton pode guardar contexto mutável da última BU/credencial usada.
- Não repetir resolução/grant/cifra em cada adapter: reutilizar o owner atual de identidade/credenciais; contrato de contexto precisa preservar generation/epoch/versão/identidade e fences, sem expor segredo a consumers comuns.
- Liskov: implementação concreta pode substituir o contrato base respeitando precondições/pós-condições/invariantes; não exige usar o pai em todo lugar que exige um filho. Métodos auxiliares privados são legítimos; o negócio não faz cast para chamar extensão concreta.
- Operação comum inicial: envio textual já existente. Tipos e resultados normalizados precisam definir aceito, recusa comprovada, bloqueio de política/capacidade e resultado incerto; não prometer sucesso externo, exactly-once ou retry automático. Compatibilidade dos erros públicos atuais deve entrar no contrato futuro, sem mudança implícita nesta minuta.
- Capacidades diferentes são contratos explícitos. Gestão de templates, envio de template e cadastro/QR não devem virar métodos obrigatórios não implementados nos outros canais. Consumidores de capacidade dependem da abstração dessa capacidade, obtida sem casts/conhecimento do concreto.
- Webhooks/HTTP/OAuth/QR permanecem específicos na fronteira de integração; payloads de entrada são normalizados antes do negócio. Falar com Meta dentro de seu adapter é o comportamento esperado da implementação concreta.
- Providers concretos encapsulam protocolo/IDs/credencial/erros de transporte. Domínio conserva autorização, persistência, aceitação/dedupe e políticas de atendimento, por contratos; esconder tudo num mega-adapter não satisfaz a direção.
- Sem novo canal, alteração de BU, desconexões, credenciais novas, chamadas Meta, mudança Delphi, worktrees/cópias, gitlinks/.gitmodules ou deploy. Não ler/listar/stat/hash/percorrer/montar api-app/.local-files nem ler .env/.env.testing.

## Canonical Touchpoints

- **Constitution impact:** preservar invariantes, sem ampliar produto além de WhatsApp; consolidação futura deve distinguir transporte persistido e contrato comum.
- **Roadmap impact:** coerência do núcleo unificado atual, sem mudar horizonte ou gate derivado.
- **Primary module candidates:** modules/integrations-and-channels.md.
- **Secondary module candidates:** modules/inbox-and-conversations.md; identidade/grants e bot existentes são regressões obrigatórias.
- **Program:** BLG-leadshug-channel-readiness-and-history. ST-CON-05 e ST-CON-04 voltam a reconvergência antes de qualquer aprovação válida sobre a nova arquitetura.

## Evidence / References

Leitura pública delimitada em2026-10-20. Produto inalterado: root80e3940126f22a941f90dba4f5e801b6c0eb2f58, API db5a86758a165fac8a1ab587599c37b17890530c, Web74b9d4b714044829796f875d00553f077c1c329d; confirmar heads no handoff. Foundation iniciale0cf064e. Sem testes/runtime nesta análise.

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

Atendimento/bot → ChannelResolver abstrato, scoped → Channel abstrato → WhatsAppOfficialChannel ou WhatsAppUnofficialChannel → clients HTTP atuais. Esta é direção de enquadramento, não assinatura final de DTO nem classe implementada. Registro/composição seleciona concretos; consumidores comuns não importam MetaClient/EvolutionClient nem escolhem envio por enum de provider. Origem pode existir como metadado de auditoria/apresentação sem comandar dispatch no negócio.

| ID | Ambiguity | Why It Matters | Current Evidence | Handling |
| --- | --- | --- | --- | --- |
| AMB-ABS-01 | menor contrato comum de envio e resultado, política/readiness e compatibilidade de erro | não apagar regras oficiais nem classificar timeout como recusa definitiva | dois senders atuais, acceptance e resolver já separados | parecer arquitetural de enquadramento; congelar assinatura/testes no TODO ST-CON-06 antes de aprovação |
| AMB-ABS-02 | descoberta tipada de capacidades para templates/lifecycle | evitar interface enorme, casts ou métodos no-op em implementações | ST-CON-05 planejado com domínio de modelos e provider adapter, ainda sem código | parecer de direção agora; ST-CON-05 reconverge para consumir capacidade abstrata |
| AMB-ABS-03 | alcance do primeiro recorte versus gestão de conexões | refatoração de todos os protocolos de onboarding pode engolir o objetivo de transporte comum | cadastro Meta/QR já testado, fronteiras explícitas | priorizar envio comum e avaliar lifecycle como capacidade separada; nenhum rewrite de cadastro implícito |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-CON-06 | Negócio usa Channel abstrato para o transporte existente | integrations-and-channels | inbox-and-conversations | contrato comum/resolução autorizada/concretos oficial e não oficial; todos os senders comuns sem branch/import de provider; políticas, contratos públicos, credencial e aceitação preservados por critérios explícitos | teste de contrato compartilhado dos adapters + PostgreSQL/Playwright real e regressão BFF/API pública/bot; troca por fake Channel prova consumo abstrato; prova operacional dos recursos próprios no contrato futuro | create-next após enquadramento | assinatura/resultado/capacidades e fronteira de lifecycle precisam frozen TODO/reviews/APROVADO | não é novo provedor nem mudança de domínio BU |
| ST-CON-05 | Vendedor cria/submete/consulta modelos | integrations-and-channels | inbox-and-conversations | mesmo produto confirmado, domínio consome contrato abstrato de capacidade de template e credencial scoped, sem nova dependência de negócio em MetaClient | editor/submit/recovery/status com capacidade fake e adapter real em testes HTTP | reconverge existing | depende do contrato/cutover ST-CON-06 | vendedor envia para Meta sem aprovação ADMIN preservado |
| ST-CON-04 | Nova conversa usa Channel e catálogo comum | inbox-and-conversations | integrations-and-channels | consumo abstrato de envio/capacidades, contato/intent/idempotência/primeiro envio preservados | browser/PG com ambos canais e template elegível | reconverge existing | ST-CON-06 e05 | aprovação antiga de cadastro não autoriza este envio |

## Review / Disposition

Preparação pré-TODO. Próximo passo: publicar enquadramento e obter parecer arquitetural independente sobre as ambiguidades acima, integrar direção e preparar ST-CON-06 específico. Não solicitar APROVADO usando os guardas de2026-10-19 do ST-CON-05, que passam a ser históricos. Nenhuma mudança de módulo canônico ou implementação é declarada por este brief.

## Retire This Brief When

ST-CON-06 possuir contrato revisado/aprovado e seus resultados forem consolidados nos módulos; consumidores05/04 reconvergirem explicitamente. Enquanto isso este documento informa a preparação, não autoriza execução.
