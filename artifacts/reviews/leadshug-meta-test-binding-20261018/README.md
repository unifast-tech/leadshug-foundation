# Revisão do vínculo técnico local do Test Number

Pacote derivado do [TODO complementar](../../../todos/active/features/TODO-leadshug-meta-api-test-number-binding.md), autoridade de execução exclusiva deste complemento. Parent: ST-CON-01, Pending/VAL05 aberto. Direção humana aceita: modo técnico local para um recurso já provisionado; não é aprovação de implementação. Nenhum código ou runtime alterado neste pacote de planejamento.

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
