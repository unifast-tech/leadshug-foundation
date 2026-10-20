# ST-CON-06 — pacote pré-aprovação

Data cliente2026-10-20. [Contrato tático v1.2](../../../todos/active/features/TODO-leadshug-channel-abstraction.md). Estado: **revisado e pronto para APROVADO específico**; sem implementação/testes/runtime de produto nesta preparação. Authority `preflight-go` declara `execution_authority_granted=false`.

## Escopo revisado

Channel/ChannelResolver abstratos de domínio, composição scoped e concretos WhatsApp atuais; cutover completo BFF/API pública/Typebot para um owner outbound, com MessageAcceptanceService preservado. Fake com destinatário opaco verifica o ponto de extensão; Instagram/Messenger/Telegram reais e seus vínculos/identidades terão contratos próprios. Capabilities pequenas de templates seguem em05 e primeiro envio04, depois de06.

Seleção humana/pública determinística, bot vinculado ao ingresso verificado, mesma policy/window com correção expressa do bypass atual. Autoria e atribuição não são reescritas pelo controller público após envio. Resultado externo é distinto de conclusão local; incerteza preserva draft/aviso e não produz retry automático. Credencial e contexto privados por operação, sem singleton de BU/token.

## Evidência de revisão

| Gate | Resultado / evidência |
| --- | --- |
| Freeze inicial de arquitetura | origin/main b092c5a29c07d10384543b80d5fdb19fd54bfdea, push terminal0 antes do parecer |
| Arquitetura tática fresh | [parecer + resolução AR01..04](architecture-opinion.md), original no-go, findings_integrated; todas obrigações conferidas pela crítica |
| Freeze da crítica | origin/main81d56f5e60a6ec99a996dfb3ba51987c4f009849 publicado após integração arquitetural |
| Crítica fresh | [parecer e reconvergência](critique.md), original no-go CR01, depois go terminal no contrato completo v1.2; CR01/02 resolvidos |
| Freeze material final | origin/main a35f676c696e21ec8b4e8ed5cbe6eafbe8da482c, push terminal0 antes da reconvergência |
| Audit floor | [audit-floor.json](evidence/audit-floor.json) go, fingerprint fa884bf1d2e7 |
| Assumptions A01..05 | [inspeção pública delimitada](source-assumptions.json) + [guard](evidence/assumption-coherence.json) go/5 premissas; nenhum guarantee futuro chamado existente |
| Drift | [review-scope-drift.json](evidence/review-scope-drift.json) go,23 seções comparadas/0 alteradas |
| Authority pré-aprovação | [authority-preapproval.json](evidence/authority-preapproval.json) preflight-go, nenhuma execução autorizada |
| Estrutura | [structure-final.json](evidence/structure-final.json) PASS |
| Routing | architecture/critique/reconvergência/planned-executor em evidence/routing-*.json, todos go; executor planejado não despachado |

Artefatos go são guardas de planejamento, não evidência de implementação ou testes de produto. CI-equivalent all, HTTP raw/shared contract, PG/Playwright, PCV, adherence/security/TQA/final/cutover/consolidação e INOUT assistida dos dois recursos continuam **planned**. Runner deve ter inventário público positivo ANTES de qualquer teste. Nunca acessar/percorrer/montar api-app/.local-files ou ler dotenv privado.

## Limites e sequência

Sem novo provedor/schema/enum/capability runtime, lifecycle refeito, outbox/intent durável, retry de POST, worktree, gitlink ou push/deploy de produto. Permanece janela leitura local→rede, crash/commit incerto e dedupe sem ID. O algoritmo temporal latest-IN da conversa sem filtro de transporte permanece explícito para o handoff04; não é consertado silenciosamente neste recorte.

Material de arquitetura/erro foi corrigido antes da crítica/reconvergência; nenhum parecer no-go foi reclassificado retroativamente como sem achados. Depois de APROVADO: reload binding, authority normal go, executor único na principal, fix runner e execução da sequência.05/04 exigem reconvergência e suas aprovações próprias; vendedor cria/submete modelo à Meta preservado.
