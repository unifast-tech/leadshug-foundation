# LeadsHug Backlog

**Version:** 1.0

The backlog is the canonical home for candidate work that is not approved for execution. It owns each candidate's disposition and next gate. A candidate is not a tactical TODO; neither this record nor a `Selected-for-Planning` state authorizes implementation.

## Record schema

Each new record carries an immutable ID, title, state, source/evidence, value/risk, dependencies, disposition owner, and next gate. Lifecycle definitions and transitions live in [`../evolution_lifecycle.md`](../evolution_lifecycle.md).

## Candidates

| Immutable ID | Title | State | Source / evidence | Value / risk | Dependencies | Disposition owner | Next gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BLG-leadshug-evolution-synthesis | LeadsHug evolution synthesis (ST-04) | Selected-for-Planning | [pre-code evolution brief](../artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md) | synthesize evidence only after both independent studies; early synthesis risks false priority | ST-01, ST-02 and ST-03 completed | strategic steward | frame/refine ST-04 separately; no implementation or prioritization is authorized |
| BLG-leadshug-attendance-evolution | Atendimento com transferência histórico completo anexos e estados | Selected-for-Planning | [brief de atendimento](../artifacts/feature-briefs/leadshug-attendance-evolution-20261014.md) | ampliar o atendimento existente; preservar isolamento, ownership e ordenação dos eventos | contratos por recorte, validação local isolada e decisões de transferência/mídia/status | strategic steward | ST-ATT-01 Local-Implemented e revisado no [TODO de histórico](../todos/completed/features/TODO-leadshug-inbox-message-timeline-pagination.md); ST-ATT-02/03/04 aguardam contratos e aprovação próprios; prioridade seguinte passou a conexões/testes em BLG-leadshug-channel-readiness-and-history por concordância do usuário em2026-10-15 |
| BLG-leadshug-channel-readiness-and-history | Cadastro e conexão dos números oficiais e não oficiais; histórico posterior | Selected-for-Planning | [brief de canais](../artifacts/feature-briefs/leadshug-channel-readiness-and-history-20261015.md) | reproduzir jornada de cadastro Meta/QR e facilitar testes; preservar isolamento, estado honesto e integridade histórica nos recortes posteriores | local primeiro confirmado; versão/wiring Evolution próprios, modalidade/WABA, acesso e callback local; dois canais oferecidos pelo usuário; Railway depois | strategic steward | ST-CON-01 APROVADO em2026-10-15; cadastro/INOUT e retomada locais pelos dois canais comprovados CP33/49/52/106-108. Encerramento local concluído CP108; próximo gate de produto: contrato ST-CON-04 Nova conversa por contato; contrato governante: [ST-CON-01](../todos/completed/features/TODO-leadshug-channel-connection-readiness.md); em seguida ST-CON-04 Nova conversa informando contato, solicitado pelo usuário; importação ST-CON-02/03 vem depois |

| BLG-leadshug-runtime-dependency-security | Atualização delimitada das dependências de runtime e uploads | Proposed | [audit da imagem](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/cp21-api-production-npm-audit.json) e [diagnóstico de alcance](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/cp21-dependency-exposure-diagnostic.json) | Multer2.2 mantém DoS autenticado; demais avisos exigem condições não identificadas nesta topologia. Não equivale a8explorações remotas comprovadas. | validar compatibilidade Nest/Multer, Prisma/tooling e qs/source-map; nenhum upgrade neste recorte | security/technical steward | enquadrar manutenção com versões/lockfile e prova próprios antes de acesso autenticado não confiável; teste temporário ST-CON-01 limitado ao OWNER privado e dados sintéticos |

The IDs above are references for future planning; their live disposition and next gate remain only in this table.

## Fulfilled candidate handoffs

| Immutable ID | Fulfilled by | Evidence | Downstream use |
| --- | --- | --- | --- |
| BLG-central-whatsapp-capability-study | [completed ST-02 TODO](../todos/completed/features/TODO-leadshug-central-whatsapp-capability-study.md) | [27-capability catalog and 204-unit ledger](../artifacts/analysis/leadshug-central-whatsapp-capability-gap-catalog-20260925.md) | input to ST-04 after ST-03; no capability is prioritized or authorized by this handoff |
| BLG-whatsflow-channel-attendance-study | [completed ST-03 TODO](../todos/completed/features/TODO-leadshug-whatsflow-channel-attendance-study.md) | [conceptual channel and attendance model](../artifacts/analysis/leadshug-whatsflow-channel-attendance-conceptual-model-20260925.md) | input to ST-04; recommendations remain unprioritized and do not authorize product changes |
