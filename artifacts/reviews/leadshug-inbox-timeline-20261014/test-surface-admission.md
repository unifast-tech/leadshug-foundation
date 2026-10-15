# Admissão dos testes e significado da prova local

ST-ATT-01, 2026-10-14. Artefato derivado; não reivindica suites green antes dos relatórios de execução.

| Superfície | Owner / leaf command | Delta | Relação com CI / prova |
| --- | --- | --- | --- |
| API unit | api-app/package.json, `npm test` | parser/cursor e asserts scoped | CI API já usa este script; novos specs são descobertos por config própria sem wrapper divergente. |
| API real PostgreSQL | api-app/package.json, `npm run test:e2e` | contrato/paginação/neutralidade/overlap | Prova adicional obrigatória do TODO, script completo. Não há claim de inclusão no pipeline existente. |
| Web unit/build | web-app/package.json, `npm test` e `npm run build` | merge/piso/socket e consumidor tipado | CI Web já usa esses leaf commands; specs atuais pertencem à descoberta do runner. |
| Browser readonly/mutation | web-app/package.json, `npm run test:tela` | histórico/races/fixture/bootstrap/path correto | Suite completa adicional obrigatória. API Nest real, mesmo PG dedicado, provider fake somente nas portas externas. Não há claim de estágio remoto. |
| Runtime/bootstrap | playwright.config.ts, API test/browser-server.cjs e test/timeline-fixtures.cjs | rebuild/API path e recusa de DB não descartável | Test-only, fora de src/entrypoint de produção; fontes no checkout principal. Bundles construídos e prova de identidade do runtime exigidos. |

API e Web têm manifests donos auditados pelo node_capability_surface_audit, exit0, em artifacts/tmp/inbox-timeline-execution/api-capability-audit.json e web-capability-audit.json. Nenhum comando de aplicação foi executado por esse audit estático.

A CI-Equivalent deste recorte é limitada aos jobs API/Web tocados: install/lint/build/unit de API e install/build/unit de Web conforme .github/workflows/ci.yml. PostgreSQL e Playwright são validações locais adicionais, mais fortes e requeridas pelo TODO. Não declarar stage-full, pipeline remoto green ou promoção; não alterar .github, compose/env ou root gitlinks. API e Web estão em feature/inbox-timeline-pagination, não main, para provas de mutação.

Descoberta de testes usa os scripts/configs dos manifests. Fixtures e cleanup são executados no banco exclusivo leadshug_timeline_*, nunca herdados de ambiente operacional. Uma suite targeted permanece diagnóstico, e um teste adicionado depois de o processo carregar o arquivo exige resultado novo sobre a fonte consolidada. Os artefatos de execução devem registrar test-after/falhas observadas honestamente, evitando alegação retroativa de TDD.
