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

O conteúdo deste repositório é específico do LeadsHug. O método reutilizável permanece em `../delphi-ai`.

## Engenharia

O produto usa NestJS, React, PostgreSQL com Prisma, Docker e Railway. A integração WhatsApp suporta canal
oficial da Meta e canal não oficial via Evolution/Baileys. O sistema é multi-tenant e o número de WhatsApp é
a Business Unit operacional.

Todo desenvolvimento deve possuir um TODO ativo aprovado antes da implementação.

## Divisão de autoridade

O `delphi-ai` é a autoridade de engenharia e inteligência do processo: interpreta TODOs, roteia
agentes, aplica regras, executa desenvolvimento e valida os gates. Este repositório é a autoridade
de tarefas e evidências: mantém TODOs aprovados, contratos, decisões, critérios de aceite e o
histórico de execução. Nenhum fluxo deve contornar o Delphi para implementar trabalho registrado
aqui.
## Decisões e continuidade de execução

Decisões de produto, escopo, contrato, arquitetura e trade-offs devem ser tomadas pelo usuário antes
da aprovação do TODO. Depois de aprovado, o agente executa o TODO continuamente até finalizá-lo. A
execução só pausa quando surgir uma decisão nova, material e necessária que não esteja coberta pelo
TODO; nesse caso, o agente apresenta opções e impactos e aguarda a escolha do usuário.

O Delphi é usado em todo o ciclo: interpreta o TODO, seleciona perfil e método, orienta a implementação
pelas regras e workflows, aplica guardrails e executa as validações.

Todo TODO que introduzir ou alterar uma ação, campo, rota, contrato, estado ou fluxo visível deve
exigir testes proporcionais no próprio escopo: unitários para regras e contratos, integração/E2E para
persistência e autorização, e Playwright quando houver comportamento web interativo. Um TODO não pode
ser encerrado apenas com build ou testes genéricos quando a nova superfície não foi exercitada.
