# ST-CON-05 — admissão pontual da fixture BCI existente

Proposta concreta para validação humana. Nenhuma alteração deste arquivo foi aplicada.

O `all`173629Z-r4 terminou com282unitários e379/380 testes PostgreSQL aprovados. A única falha é `read ECONNRESET` no teste BCI anterior, que faz20 solicitações concorrentes contra um servidor sem listener estável. A fixture nova de templates, corrigida com listener explícito, passou sua prova com5contas. Isso demonstra o ajuste nessa fixture; a causa exclusiva do evento anterior não é afirmada sem trace.

Solicita-se admitir somente `api-app/test/number-onboarding-bci.e2e-spec.ts` para a inicialização abaixo. O arquivo está fora dos caminhos ativos aprovados; ele **não** pertence aos41records do manifesto herdado e não reduz os30selos. Seu status Git pontual está limpo e seu SHA256 atual é `d21fef15e4bc3efbce43d86367f76031c22885cecbbfd8c39f6c0aded61b6974`. O TODO exige `User validation: required on deviation` na seção Diff Expectation Contract (linha91).

Mudança: abrir o servidor Nest uma única vez em127.0.0.1 e porta efêmera antes das requisições; comprovar listener/endereço. O `afterAll` existente fecha o mesmo app. Nenhum retry, skip, limiar, contador, perfil5×20, grant, provider ou código de produção muda. A alternativa de sobrescrever `app.listen` no helper foi rejeitada por alterar sua semântica padrão.

```diff
--- before/api-app/test/number-onboarding-bci.e2e-spec.ts
+++ proposed/api-app/test/number-onboarding-bci.e2e-spec.ts
@@ -13 +13 @@
-  beforeAll(async () => { tetoComCanalNaoOficial(); ({ app, prisma } = await subirApp()); await limparBanco(prisma); tenant = await criarMantenedora(app, 'BCI registration', 'bci-owner@example.test'); cookie = await login(app, 'bci-owner@example.test'); metaFake.confirmCalls = 0; const base = await prisma.businessUnit.findUniqueOrThrow({ where: { id: tenant.businessUnit.id }, select: { phone: true } }); metaFake.wabaRecursos = [{ wabaId: '123456789', phoneNumberId: '111111111', telefone: base.phone! }, ...Array.from({ length: 5 }, (_, i) => ({ wabaId: '123456789', phoneNumberId: String(700000001 + i), telefone: `5586${String(10000000 + i)}` }))]; });
+  beforeAll(async () => { tetoComCanalNaoOficial(); ({ app, prisma } = await subirApp()); await app.listen(0, '127.0.0.1'); expect(app.getHttpServer().listening).toBe(true); expect(app.getHttpServer().address()).toMatchObject({ address: '127.0.0.1', family: 'IPv4' }); await limparBanco(prisma); tenant = await criarMantenedora(app, 'BCI registration', 'bci-owner@example.test'); cookie = await login(app, 'bci-owner@example.test'); metaFake.confirmCalls = 0; const base = await prisma.businessUnit.findUniqueOrThrow({ where: { id: tenant.businessUnit.id }, select: { phone: true } }); metaFake.wabaRecursos = [{ wabaId: '123456789', phoneNumberId: '111111111', telefone: base.phone! }, ...Array.from({ length: 5 }, (_, i) => ({ wabaId: '123456789', phoneNumberId: String(700000001 + i), telefone: `5586${String(10000000 + i)}` }))]; });

```

Após validação: conferir baseline exata novamente, admitir este único caminho, aplicar o diff e executar o `all` completo com novas fontes/artefatos. Revisões independentes, banco/runtime preservados e prova Meta seguem os mesmos gates já aprovados. A validação dos2companions de histórico continua vigente.

Referência de mecanismo: [Supertest7.2.2, fonte primária](https://raw.githubusercontent.com/forwardemail/supertest/v7.2.2/lib/test.js), `serverAddress` auto-listen e `end` auto-close. Recibo estruturado: `evidence/baseline-bci-fixture-lifecycle-admission-v1.1-proposal.json`.
