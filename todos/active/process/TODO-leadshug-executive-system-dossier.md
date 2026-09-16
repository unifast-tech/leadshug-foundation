# TODO — LeadsHug: dossiê executivo do sistema para alinhamento de próximos passos

## Approval

- **Approved by:** `pending explicit APROVADO`
- **Approval scope:** produzir um dossiê executivo, completo e verificável, do estado atual do LeadsHug para compartilhamento com a liderança. O dossiê descreve arquitetura, capacidades, canais, mensageria, dados, segurança, operação, legado, maturidade e próximos passos; não altera produto, infraestrutura, integrações ou decisões de arquitetura.
- **Renewed approval required when:** o trabalho exigir acesso a produção, dados de clientes, credenciais, uma alegação de saúde/deploy não comprovada localmente, uma mudança de arquitetura/escopo, ou a produção de material externo além do dossiê Markdown aprovado.

## Objective

Criar um documento claro para gestão, com uma camada executiva e um apêndice técnico, que responda de forma rastreável:

1. O que é o LeadsHug, para quem serve e qual problema resolve.
2. Como o núcleo atual está estruturado e quais repositórios têm qual responsabilidade.
3. Quais capacidades estão implementadas, em evolução, planejadas ou deliberadamente fora de escopo.
4. Como funcionam os canais WhatsApp oficial e não oficial, Typebot e e-mail, sem confundir adaptador com autoridade do sistema.
5. Como mensagens entram, são normalizadas, persistidas, auditadas, distribuídas e exibidas ao usuário.
6. Como tenancy, Mantenedora, Setor, Business Unit, permissões, contatos e conversas se relacionam.
7. Qual é a topologia tecnológica e de entrega, e o que ela prova — sem alegar saúde de produção sem evidência.
8. Quais riscos, dependências, validações manuais, decisões e próximos passos precisam de alinhamento da liderança.

## Proposed deliverable

Criar `artifacts/analysis/leadshug-executive-system-dossier-YYYYMMDD.md`, escrito em português e organizado para leitura de gestão:

1. **Resumo executivo:** proposta de valor, estágio atual, arquitetura-alvo e principais decisões necessárias.
2. **Mapa do sistema:** produto, API, Web, Foundation, Engineering e a fronteira dos legados.
3. **Mapa funcional:** identidade e acesso, tenancy/BU, contatos, conversas/inbox, CRM, atividades/auditoria, automações e administração.
4. **Canais e provedores:** Meta Cloud API, caminho Evolution/Baileys, Typebot Cloud e e-mail transacional; autoridade, estado, restrições e responsabilidade de cada um.
5. **Fluxos de mensageria:** diagramas legíveis de entrada e saída, incluindo webhook, adaptador, domínio, Prisma/PostgreSQL, API/BFF e Web; explicitar pontos de falha, correlação, idempotência e auditoria já resolvidos versus pendentes.
6. **Dados, segurança e isolamento:** Mantenedora → Setor → Business Unit, papéis, fronteiras de autorização e segredos de provedores.
7. **Arquitetura e operação:** NestJS, React/Vite, Prisma/PostgreSQL, Docker, Railway, testes e limites entre evidência local, stage e produção.
8. **Estado de entrega:** tabela por capacidade com evidência, maturidade (`implementado`, `em validação`, `pendente de decisão`, `planejado` ou `legado/referência`) e lacunas conhecidas.
9. **Legado e inspiração:** Central-Whatsapp e whatsflow_v2 como referências delimitadas, sem dependência, cópia ou migração implícita.
10. **Riscos e próximos passos recomendados:** itens priorizados, pré-condições e decisões humanas necessárias, distinguindo fatos observados de recomendações.
11. **Apêndice de evidências:** ADRs, contratos, manifests, topologia declarada, TODOs ativos, testes e artefatos consultados.

## Scope

- [ ] Inventariar o núcleo atual `LeadsHug/apps/api` e `LeadsHug/apps/web` por módulos, superfícies de entrada, fluxos e contratos efetivamente presentes.
- [ ] Reconciliar o inventário com ADRs, Foundation, TODOs ativos, manifests, migrations, definições Docker/Railway e evidência de testes.
- [ ] Documentar os canais e a mensageria com estado verificável, limitações e fluxos ponta a ponta.
- [ ] Produzir diagramas textuais ou Mermaid que sejam compreensíveis sem acesso ao código.
- [ ] Distinguir capacidade implementada de hipótese, pendência, validação externa e estado de runtime não comprovado.
- [ ] Incluir matriz executiva de maturidade, riscos, dependências e próximos passos para decisão da liderança.
- [ ] Fazer revisão técnica sênior somente leitura com Claude Code e integrar achados pertinentes.
- [ ] Não alterar código, configurações, dados, infraestrutura, integrações, credenciais, legados ou ADRs.

## Evidence and framing rules

| Tipo de afirmação | Fonte mínima | Tratamento no dossiê |
| --- | --- | --- |
| Arquitetura-alvo | ADR aceito, contrato Foundation ou código/manifests atuais | Declarar como alvo, não como saúde de runtime. |
| Capacidade implementada | Código e teste/contrato correspondente | Marcar como implementada localmente, com referência. |
| Canal/provedor funcionando externamente | Evidência manual explícita no TODO/artefato | Não inferir a partir de mocks, builds ou testes locais. |
| Item pendente | TODO ativo, matriz de evidências ou decisão ausente | Marcar como pendente e apontar a pré-condição. |
| Sistema legado | Matriz de fronteiras e política de legado | Tratar somente como referência delimitada. |

## Definition of Done

- [ ] O dossiê permite a uma pessoa não técnica entender o produto, a arquitetura e o estágio de entrega sem navegar o repositório.
- [ ] Cada camada do sistema, canal e fluxo de mensageria possui descrição e diagrama rastreáveis.
- [ ] A matriz de maturidade diferencia claramente implementado, validação pendente, pendente de decisão, planejado e legado/referência.
- [ ] Nenhuma afirmação de deploy, produção, segurança ou provedor ultrapassa sua evidência disponível.
- [ ] Riscos, dependências e decisões necessárias estão priorizados e acionáveis para a liderança.
- [ ] O documento contém índice de evidências e links locais válidos.
- [ ] Revisão final do Claude Code, checagens documentais e o guard Codex–Claude passam.

## Validation Steps

- [ ] Verificar links, caminhos e referências de evidência no dossiê.
- [ ] Rodar `git diff --check` e buscas de consistência entre maturidade declarada, TODOs ativos e fronteiras legadas.
- [ ] Realizar revisão Claude Code somente leitura sobre precisão factual, clareza executiva, omissões materiais e extrapolação de evidência.
- [ ] Rodar `python3 tools/codex_claude_delivery_guard.py <todo-path> --require-final-review` antes do fechamento.

## Codex–Claude Delivery Cycle

- **User approval evidence:** `<pending explicit APROVADO>`
- **Execution lead:** `Codex`
- **Senior technical reviewer:** `Claude Code`
- **Claude checkpoint status:** `not_run`
- **Claude final review status:** `not_run`
- **Claude final review evidence:** `<pending>`
- **Material findings disposition:** `<pending>`
- **Continuity rule:** `Após aprovação, continuar o inventário, a redação, as verificações e os reparos de revisão sem pausar; apresentar somente decisões materiais ou validações externas necessárias.`
- **Escalate to user only if:** `a fonte contradisser uma decisão aceita, a evidência exigir alegação de runtime/produção, houver dado sensível, ou uma decisão de produto/arquitetura mudar materialmente o dossiê.`
