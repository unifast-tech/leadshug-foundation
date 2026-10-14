# Pacote de revisão de arquitetura e contrato da timeline da inbox

Data: 2026-10-14. Pacote derivado para revisão pré-implementação; sem entrega de aplicação reivindicada.

## Autoridade e escopo

O usuário selecionou atendimento e autorizou “Pode seguir para revisão e aprovação”. A aprovação final de implementação ainda será solicitada para o contrato revisado. O skill local wf-docker-todo-approval-gates-method exige revisão independente, freeze publicado e guardas. Foundation main autoriza commits/push documentais pelo git_write_authority_guard. Não autorizar deploy, mudanças no produto ou Git worktrees.

TODO: `foundation_documentation/todos/active/features/TODO-leadshug-inbox-message-timeline-pagination.md`.
Brief: `foundation_documentation/artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md`.

Leia o TODO completo, somente as seções/código abaixo quando necessários e a constituição/módulos indicados. Não leia secrets, .env local, payloads reais ou corpus histórico sem relação.

## Baselines e diagnóstico

API: 5db3fbe2043428749895fc3ff6441e9457467dd0; Web: 6c99c27dafdce8ed9b461d17aaaaa491b8ae16e9. Thread faz createdAt asc/take 200 e zera não lidas. React substitui thread em abrir/agir/evento. Cursor/paginação propostos ainda não existem. Não há teste da aplicação executado nesta preparação.

## Fontes bounded

- foundation_documentation/project_constitution.md; modules/inbox-and-conversations.md; modules/identity-and-tenancy.md; modules/audit-and-history.md.
- api-app/src/domain/inbox/conversations.service.ts (thread); src/surfaces/bff/conversations.controller.ts (thread/resolver); prisma/schema.prisma (Message/Conversation).
- web-app/src/telas/Inbox.tsx; src/api.ts (Thread); src/tempoReal.ts; playwright.config.ts.
- api-app/test/helpers.ts; test/setup-env.ts; test/atendimento.e2e-spec.ts; web-app/e2e/telas.spec.ts (bootstrap e fixtures).

## Decisão arquitetural em exame

Comparar o contrato proposto de cursor anterior + reconciliação da página recente com uma paginação bidirecional bounded para recuperar mensagens novas. Verificar gaps durante bursts, não lidas, timestamps empatados, uso de índice, crescimento de memória/requests, scope/cursor, scroll, respostas atrasadas e prova real de envio/browser.

Preservar o WHAT: inbox com histórico completo e recente, paginação incremental, refresh/envio sem perda e isolamento. API pública, Consultar, transferência, mídia, status, Typebot e deploy ficam fora deste recorte. Correções de suporte de teste só para provas fiéis do fluxo, sem shortcuts de produção.

Retornar achados concretos com severidade, locus, cenário e correção mínima; separar bloqueios de preferências. Incluir parecer de arquitetura e crítica de corretude/performance/elegância/riscos; não modificar nenhum arquivo. Alegações de aprovação, suite green ou waivers exigem evidência e não podem ser presumidas.
