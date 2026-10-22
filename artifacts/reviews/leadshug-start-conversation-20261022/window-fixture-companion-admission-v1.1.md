# ST-CON-04 — proposta de admissão de duas fixtures de teste

Estado: proposta pronta, não aplicada; aguarda validação do usuário.

O contrato aprovado exige a data qualificada de uma mensagem Meta assinada, ligada ao recurso atual. O runner canônico83187 mostrou16 falhas em5 suítes; duas das suítes têm arquivos explicitamente protegidos como `NO new mutation`. Alterar um helper global ou aceitar `createdAt` esconderia o problema de proveniência.

A proposta admite somente:

- `api-app/test/number-onboarding-typebot.e2e-spec.ts`: incluir a data no payload antes da assinatura da fixture e envelhecer também `officialInboundAt` no cenário de expiração. Preservar contadores e asserções.
- `api-app/test/number-onboarding-pcv.e2e-spec.ts`: vincular as mensagens sintéticas à identidade atual e à data qualificada; alinhar o EXPLAIN do mesmo cenário com a consulta de janela e o novo índice. Preservar quantidade de consultas, zero chamadas externas, paginação, asserção de direção e adicionar a de origem oficial. O teste separado do índice anterior e do histórico OUT continua intacto.

[Diff exato proposto](window-fixture-companion-admission-v1.1.patch), gerado em memória contra os dois arquivos públicos sem editá-los. [Hashes e limites](evidence/window-fixture-companion-proposal-v1.1.json).

A exigência de validação vem do [TODO aprovado](../../../todos/active/features/TODO-leadshug-start-conversation-by-contact.md), seção Diff Expectation Contract: **User validation: required on deviation**, somada às linhas exatas de ambos os arquivos como **Inherited baseline ONLY, NO new mutation; byte-exact seal required**. Esta validação admite somente esses ajustes de teste; o escopo funcional permanece o aprovado.
