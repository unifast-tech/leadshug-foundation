# LeadsHug Foundation Documentation

Este repositório é a autoridade documental do LeadsHug: mandato, entidades, constituição, módulos, roadmap,
políticas, contratos e TODOs táticos.

## Autoridade

- `project_mandate.md`: propósito e princípios permanentes.
- `domain_entities.md`: vocabulário e entidades do domínio.
- `project_constitution.md`: regras sistêmicas e limites de arquitetura.
- `system_roadmap.md`: fases estratégicas.
- `modules/`: contratos locais por contexto.
- `todos/active/`: execução aprovada e rastreável.

O conteúdo deste repositório é específico do LeadsHug. As regras, workflows e guardas de engenharia ficam no repositório irmão `../leadshug-engineering`.

## Engenharia

O produto usa NestJS 11, React 18/Vite 5, PostgreSQL 16 com Prisma 6, Docker e Railway. A integração WhatsApp suporta canal oficial da Meta e o caminho não oficial Evolution/Baileys. O sistema é multi-tenant e o número de WhatsApp é a Business Unit operacional. A fonte de manutenção desta afirmação é [`technology_baseline.md`](technology_baseline.md), que separa arquitetura-alvo de estado de runtime.

Todo desenvolvimento deve possuir um TODO ativo aprovado antes da implementação.

## Divisão de autoridade

`leadshug-engineering` é a autoridade de prática de engenharia: fornece regras, workflows e guardas reutilizáveis. Este repositório é a autoridade de produto e governança: mantém TODOs aprovados, contratos, decisões, critérios de aceite e o histórico de execução. O usuário aprova o escopo, Codex executa, e Claude Code revisa tecnicamente em modo somente leitura. Nenhum fluxo deve contornar essas autoridades para implementar trabalho registrado aqui.

## Navegação de estado atual

- [`technology_baseline.md`](technology_baseline.md): stack e fontes verificáveis da arquitetura-alvo.
- [`artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md`](artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md): fronteiras entre o núcleo ativo e os legados.
- [`policies/central_whatsapp_independent_legacy_policy.md`](policies/central_whatsapp_independent_legacy_policy.md): uso permitido de Central-Whatsapp como referência independente.

## Decisões e continuidade de execução

Decisões de produto, escopo, contrato, arquitetura e trade-offs devem ser tomadas pelo usuário antes
da aprovação do TODO. Depois de aprovado, o agente executa o TODO continuamente até finalizá-lo. A
execução só pausa quando surgir uma decisão nova, material e necessária que não esteja coberta pelo
TODO; nesse caso, o agente apresenta opções e impactos e aguarda a escolha do usuário.

`leadshug-engineering` é usado em todo o ciclo para fornecer o método, as regras, os workflows e os guardrails. A execução segue o TODO aprovado e as validações registradas nele.

Todo TODO que introduzir ou alterar uma ação, campo, rota, contrato, estado ou fluxo visível deve
exigir testes proporcionais no próprio escopo: unitários para regras e contratos, integração/E2E para
persistência e autorização, e Playwright quando houver comportamento web interativo. Um TODO não pode
ser encerrado apenas com build ou testes genéricos quando a nova superfície não foi exercitada.
