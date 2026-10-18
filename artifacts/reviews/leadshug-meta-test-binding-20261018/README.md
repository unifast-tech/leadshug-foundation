# Revisão do vínculo técnico local do Test Number

Pacote derivado do [TODO complementar](../../../todos/active/features/TODO-leadshug-meta-api-test-number-binding.md), autoridade de execução exclusiva deste complemento. Parent: ST-CON-01, Pending/VAL05 aberto. O usuário respondeu APROVADO ao plano publicado em 7f478ee3 em 2026-10-18. A execução é obrigatoriamente em etapas: qualificação somente leitura, depois implementação somente se o grant for qualificado e sob GO próprio. A preparação atual não altera código do produto nem runtime. Os registros CP81 abaixo preservam a história do planejamento anterior à aprovação.

## Entradas delimitadas

- TODO complementar, criado a partir do template canônico.
- [Proposta e opções](../../analysis/leadshug-meta-api-test-number-binding-proposal-20261018.md).
- [Inventário de código com fingerprints](../leadshug-number-onboarding-20261015/evidence/cp80-source-binding-inventory.json).
- [Confirmação da direção](../leadshug-number-onboarding-20261015/evidence/cp81-human-local-test-binding-scope-direction.json).
- Constituição e módulos integrations-and-channels, identity-and-tenancy, inbox-and-conversations e audit-and-history, somente invariantes/contratos do onboarding e consumers citados no TODO.
- Fontes públicas exatas listadas no inventário; complementar apenas com session.middleware.ts, configuração de bootstrap e schema quando necessário para verificar os anchors específicos do TODO. Sem scans globais de API, diretórios privados ou blobs de .local-files.

## Diagnóstico e limites da evidência

O Test Number da Configuração da API entregou uma mensagem no WhatsApp do operador. Isso foi confirmado pelo humano; ainda não existe vínculo desse recurso na inbox. O recurso Sandbox distinto foi cadastrado normalmente e conferido readonly; não estava disponível no WhatsApp do remetente. O envio por SMS não executou o teste da API WhatsApp.

CP77 observou zero rota Meta no gateway na janela da resposta ao Test Number da Configuração da API. O controle sintético do painel alcançou a rota em outra janela. Inscrição/callback da conta de teste foram conferidos pelo humano. Não há causa fechada, prova de disponibilidade contínua do túnel ou garantia de que o novo vínculo resolverá entrega. Não repetir envio nem consultar provider/DB durante o review de fonte.

## Perguntas para os pareceres

Arquitetura: a entrada técnica converge no domínio de cadastro e nos consumidores existentes, sem seed/SQL, token global, OAuth simulado ou fluxo paralelo de ativação? O discriminante de método impede NOVO/register no backend e sobrevive à recuperação? O desenho é proporcional a um único recurso de teste local?

Segurança/crítica: configuração privada fixa alvo, sem conceder autorização administrativa ao caller? O grant é provado pela Meta antes de qualquer promoção? A regra existente de alvos WABA granulares não será enfraquecida para acomodar uma credencial incompatível. Secretos permanecem no backend; sessão/nonce/CSRF/fences/lease/ownership e credencial ativa precisam permanecer protegidos até o commit. Exigir provas específicas do comportamento, não apenas suite verde.

Ambos os pareceres devem avaliar explicitamente correção, performance, qualidade, testes, segurança, elegância, estrutura e encaixe operacional. Classificar riscos materiais versus sugestões opcionais. Identificar pressupostos sem evidência; não afirmar que o token concreto do painel atende o validator. Se a primeira qualificação real não comprovar elegibilidade, o plano deve parar sem ativar vínculo ou afrouxar Embedded Signup.

## Governança

Estado inicial: prepared-pre-freeze. Root registra commit/push e hashes antes de abrir qualquer parecer formal. Arquitetura primeiro; achados materiais integrados e novo freeze quando necessário; crítica fresca e independente depois. Sem herança de contexto nos reviewers. Produto/runtime permanecem sem writer até APROVADO e authority guard normal. Um único writer futuro no checkout principal, sem worktree, push de código, Railway, migração externa ou novo teste físico sob autoridade de planejamento.

Revisões da entrega, auditoria de testes, segurança adversarial, performance/concorrência e final independente são posteriores à implementação/validação, sem reutilizar o review antigo do parent como evidência da nova autorização.

Planning freeze e83d5bdc: commit/push confirmado; recibo baseline-freeze-e83d5bdc.json confere os28blobs. Este registro factual não altera o contrato congelado. Reviewers devem usar o TODO/proposta desse commit e os fingerprints de fonte, mais este recibo. Nenhum parecer está concluído ainda.

Arquitetura v1 terminal: revise, direção estrutural endossada. ARCH-QUAL-01 Integrated com allowlist completa, freshness do módulo compilado, método público único (até3GET), resultados estritamente observáveis e hard-stop. ARCH-DOC-02 e ARCH-TEST-03 integrados. Raw preservado SHA9fa28a273d3fa0be1978954a4e313e71d397ba1fed938e216f58db7052260a5f; root-architecture-v1-resolution.json registra adjudicação. Novo freeze precederá crítica fresca, que verificará as correções. Sem execução autorizada.

Crítica v1 terminal: approve, zero bloqueadores materiais, três resoluções de arquitetura confirmadas; raw b39207f874cb7b3d58522756c5f5fd572af3bd1deb2d5c5bf89191379eb4543e preservado. CRIT-MIG-01 low integra caso de replay após migração nos critérios já existentes. Comparação módulos D01..06 e coerência estática registradas. Estrutural v1 PASS; scope-drift v1 GO/23seções/zeroalterações. Preflight v1 NO-GO por grafia de enum do harness; code-coherence v1 GOmas3rows por pipe na linhaA02. Ambos preservados/qualificados, duas correções de formato preparadas e final freeze/guardas pendentes. Não há dispensa ou aprovação de implementação.

cp81 planejamento pronto para aprovação humana: arquitetura/crítica convergiram, crítica approve/zero bloqueadores materiais. Baseline f35d1a0d publicada; code-coherencev3 GO4premissas, scope-driftv3 GO23seções/zerodesvio, estruturalv3 PASS e authorityv3 preflight-go/semexecauthority. Guardas v1/v2 negativos/parciais preservados e qualificados; correções apenas de formato/referência. Pacote artifacts/reviews/leadshug-meta-test-binding-20261018/root-planning-ready-for-approval.json. Próximo: APROVADO explícito do complemento antes de qualificação secreta/implementação; se grant não passar, parar antes de produto. Sem novas operações vivas/código; parent Pending/VAL05 aberto, mapping não garante entrega.

## CP82 — Aprovação e preparação da qualificação

- [Aprovação humana](approval-cp82.json) do escopo publicado; nenhum novo comportamento ou relaxamento.
- [Authority guard normal](authority-execution-cp82-v2.json): go, com aprovação e 10 fontes de regras/workflows ingeridas; não é o preflight de planejamento.
- [Estrutural v3](structural-execution-cp82-v3.json): PASS. A v1 negativa registra apenas enum de metadata corrigido; v2/v3 positivas a substituem.
- [Fontes públicas](source-attestation-cp82.json): 21 arquivos continuam idênticos ao plano revisado.
- [Roteamento do executor](routing-qualification-cp82.json) e [revisor independente](routing-helper-review-cp82.json): go, sem worktrees.
- Helper v4 e invocação aprovados por revisão independente, zero bloqueadores. Passaram 13 checagens do adaptador compilado com fetch fictício e 15 do executor; o revisor repetiu estas 15. Operador confirmou os três campos locais salvos; a leitura restrita ocorreu somente sob o GO real posterior.
- Produto ainda sem alterações; parent Pending/VAL05 aberto e sem dispensa.

## Resultado real CP82

Uma única execução consumiu o [GO](qualification-live-go-cp82.json). O [resultado exato](qualification-live-result-cp82.json) foi rejected_or_inconclusive, com adaptador atual e sem comprovar autorização/recurso ou telefone canônico utilizável. O erro combinado seguro não distingue a causa. Não houve retry nem escrita de provider, DB ou produto. [Adjudicação root](root-qualification-outcome-cp82.json): parar antes de produto e retornar ao desenho; TODO Pending+Blocked. Isso não conclui o cadastro ou a prova de mensagens e não dispensa VAL05.
