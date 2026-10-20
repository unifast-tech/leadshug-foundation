# Channel abstrato — parecer de enquadramento e disposição

Data2026-10-20. Perfil Strategic / CTO-Tech-Lead, escopos NestJS/React/PostgreSQL/Prisma/Docker. Governante desta preparação: [brief pré-TODO](../feature-briefs/leadshug-channel-abstraction-20261020.md), baseado no template canônico, publicado Foundationbddf9d92aea4eebd5d4e767afb2feba8432aa83a antes do parecer. Esta evidência é consultiva de enquadramento; não satisfaz gates de um TODO de implementação ainda não refinado nem concede APROVADO.

Reviewer: /root/channel_abstraction_framing, fresh fork_turns none, gpt-6.1-sol/max; routing formal-review/formal-reviewer/architecture_opinion go antes do dispatch. Autorização de review: main_instructions.md exige opinião interna independente quando a direção arquitetural permanece materialmente ambígua. Sem edits/testes/runtime/contas/private paths pelo reviewer; root também não executou produto/testes/runtime/contas/credenciais. Heads API db5a86758a165fac8a1ab587599c37b17890530c, Web74b9d4b714044829796f875d00553f077c1c329d e root80e3940126f22a941f90dba4f5e801b6c0eb2f58 confirmados pelo root via rev-parse; reviewer não os verificou independentemente.

## Findings first

| ID / severity | Evidence | Opinion / owner disposition |
| --- | --- | --- |
| ABS-01 high | meta.client.ts:186, evolution.client.ts:96, conversations.service.ts:310 — string/null e falhas colapsadas | Integrated: Channel precisa distinguir accepted+ID, blocked antes de dispatch, rejected comprovado e unknown. Timeout/malformed/ID ausente não provam recusa. Compatibilidade de código/status público por projeção explícita; mudança de persistência/outcome é decisão funcional no TODO, não simples rename. |
| ABS-02 high | channel-credential-resolver.ts:24 — procura só channelId, readiness/cifra, sem actor/grant; token retorna ao caller, versão não | Integrated: resolução usa referência da conversa autorizada ou ingresso verificado e confere owner BU/canal. Segredo privado; contexto imutável de identidade/generation/epoch, rotação/versionamento explicitamente distintos da retirada de identidade. |
| ABS-03 high | conversations.service.ts:155/172 — comentário proíbe troca, fallback usa canais[0] | Integrated: ausência do canal selecionado falha explicitamente; requisitos de canal/política de janela no domínio, sem dispatch por enum de provider. Congelar correção intencional no TODO futuro. |
| ABS-04 medium | interfaces MetaClient/EvolutionClient com tokens; consumers conhecem ambos/IDs e branches | Integrated: DIP parcial já existe; falta abstração comum no negócio, não DI do zero. |
| ABS-05 medium | bff.module.ts:95, public.module.ts:22, webhooks.module.ts:22; Typebot incoming.service.ts:94 | Integrated: todos senders comuns e composição convergem, preferir módulo exportado único sem misturar autenticação das superfícies. |

Paths de código da tabela são relativos a api-app/src/ com pastas integrations/meta, integrations/evolution, domain/inbox, domain/channels e surfaces/bff/public/webhooks citadas no brief. Nenhuma falha hipotética foi apresentada como exploit testado ou corrigido.

## Recommended minimum architecture

Domain-owned abstract Channel para envio de texto comum e resultados normalizados; ChannelResolver abstrato scoped; concretos oficial/não oficial usando clients HTTP; uma composição escolhe implementação pelo vínculo persistido confiável. Instância pequena por operação com contexto imutável basta; clients HTTP compartilhados sem estado por BU. Sem binding global único por ambiente, singleton mutável de token, propagação de request-scope, reflexão/plugin scanner, vault ou lock externo global.

BuChannel é vínculo persistido; Channel é port runtime. Sem herança Prisma nem novo modelo de identidade. Política/auth/janela/seleção permanecem domínio; payload/erro técnico pertence ao adapter; MessageAcceptanceService continua único owner de persistência chaveada, reconciliação sender/echo e fences de identidade/generation/epoch. Não transferir tudo a um mega-adapter.

AMB-ABS-01: direção por outcomes comuns/compatibilidade pública; aceitação não prova entrega. Definir corrida entre snapshot/rede/retirada de identidade, sem promessa de rollback externo ou retry automático. Assinatura/DTO/regras exatas ainda pertencem ao TODO futuro.

AMB-ABS-02: capacidades tipadas pequenas para gerir/enviar templates, resolvidas por contrato scoped que retorna capacidade ou unsupported/unavailable. Sem casts/concrete instanceof/check de provider, no-op ou NotImplemented na base; disponibilidade não concede autorização.

AMB-ABS-03: ST-CON-06 faz cutover de TODO envio comum atual; preserva onboarding/OAuth/QR e regressões. Lifecycle especializado pode ganhar ports pequenos depois, quando seu enquadramento justificar. Não declarar todos fluxos de cadastro abstratos após apenas refatorar senders. Telegram futuro.

## Positions and future evidence

Correctness favorável após decisões de outcome/scope/policy explícitas. Performance favorável por dispatch local e pequenas instâncias; sem novos probes/retries/locks obrigatórios, nenhuma medição executada. Elegância favorável com port pequeno/capacidades estreitas. Estrutura favorável com contratos de domínio e aceitação única. Operação favorável para múltiplos tenants/canais simultâneos sem substituir o owner de onboarding/credencial.

Futuro contrato precisa testes compartilhados de adapter, substituição por fake Channel, envios concorrentes de BUs distintas, contexto de identidade antigo, DTO/códigos públicos intencionais e sender-first/echo-first PG. Root acrescentou prerequisite operacional confirmado por inspeção scripts/test-channels-local.sh:25: substituir traversal amplo por inventário público positivo antes de qualquer teste. Runner não executado.

## Disposition

Direção incorporada ao brief e à sequência do candidato. ST-CON-05/04 voltaram a reconvergência, mantendo funcionalidade solicitada e histórico dos reviews antigos; nenhum gate de implementação revalidado ou autorização inventada. Próxima etapa do programa: contrato tático ST-CON-06 refinado, reviews/gates/APROVADO próprios; depois rebase05 e04. Módulos canônicos permanecem autoridade atual, não alterados como se o alvo já estivesse entregue.

Primary conceptual sources: [NestJS custom providers](https://docs.nestjs.com/fundamentals/custom-providers), [Liskov/Wing1994](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf). As propriedades do contrato base devem continuar válidas nas implementações; não se exige substituir o filho pelo pai em todo contexto específico. O contrato comum não promete enviar incondicionalmente quando a política/capacidade bloqueia.
