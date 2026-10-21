# ST-CON-05 — proposta de admissão de dois arquivos de histórico

Proposta derivada, ainda não autoriza editar os dois arquivos abaixo. A implementação e a validação dos caminhos já aprovados continuam. Não muda a jornada de criar/submeter/consultar modelos nem inclui envio a contatos.

## Motivo comprovado

O runner canônico `api` de CP04 executou282 testes unitários com sucesso e encontrou no E2E a ausência das7 novas rotas na cobertura obrigatória de ações. Evidência: `artifacts/tmp/stcon05-cp04-api-final-20261021T143733Z.log`, SHA256 `e34d102aa386dc262782825d0f1dc6b2fa1f311f3886f4b071f6f7a004fe17f5`. O resultado global é falho e não representa entrega. A regra existente de `src/domain/historico/cobertura.ts`, executada por `test/cobertura-do-catalogo.e2e-spec.ts`, exige decisão de registro ou isenção para cada rota de escrita.

O TODO aprovado tem lista estrita e declara `User validation: required on deviation`. Estes2 arquivos não aparecem nela. A validação pedida admite somente estes companions da mesma funcionalidade, mantendo todos os demais limites de v1.1.

## Alteração concreta proposta

| Arquivo adicional | Mudança delimitada |
| --- | --- |
| `api-app/src/domain/historico/catalogo.ts` | Acrescentar4 ações de modelos, usando categorias CRIAR/EDITAR, entidade INTEGRACAO e escopo BU já existentes. Frases fixas, sem corpo/exemplos/tokens. |
| `api-app/src/domain/historico/cobertura.ts` | Classificar exatamente as7 rotas novas:4 mutações com registro real e3 consultas com isenção justificada. Não alterar entradas existentes nem o teste guardião. |

As4 ações e pontos de registro são:

- `modelo.rascunho.criado`: criação nova do rascunho; mesma transação, sem duplicação em replay.
- `modelo.rascunho.atualizado`: nova revisão efetivamente salva; mesma transação do CAS, com ator que realizou a edição.
- `modelo.submissao.solicitada`: reserva nova da operação; registra a solicitação, sem afirmar aceitação/aprovação da Meta. Replay não cria outra atividade.
- `modelo.operacao.recuperada`: transição de negócio efetivamente realizada pelo POST reconcile; mesma transação protegida da operação. Consulta sem alteração ou replay não inventa atividade.

Mapeamento proposto para a cobertura:

```text
POST  /api/bff/business-units/:buId/message-templates                 -> modelo.rascunho.criado
PATCH /api/bff/message-templates/:id                                 -> modelo.rascunho.atualizado
POST  /api/bff/message-templates/:id/submit                          -> modelo.submissao.solicitada
POST  /api/bff/message-templates/:id/operations/:operationId/reconcile -> modelo.operacao.recuperada
POST  /api/bff/business-units/:buId/message-templates/preview         -> isento: prévia validada, sem gravação ou chamada ao provedor
POST  /api/bff/message-templates/:id/refresh                         -> isento: consulta explícita do estado externo e atualização da observação local, sem alterar o ativo na Meta
POST  /api/bff/business-units/:buId/channels/:channelId/message-template-catalog -> isento: consulta explícita de uma página e atualização da observação local, sem alterar o ativo na Meta
```

Usar o `RegistroDeAtividade` existente, já composto no BffModule. Serviços e testes de modelos já admitidos recebem as chamadas e as provas; não criar outro owner de histórico, campos espelhados, flags de bypass ou eventos de consulta artificialmente rotulados como mutação. Preservar ator/Mantenedora/BU e apenas identificadores locais seguros. Logs não recebem definição, exemplos, nome de contato, payload Graph ou credenciais. O contrato de certeza de commit e o limite de POST permanecem aplicáveis também se a gravação de atividade falhar.

## Validação antes da conclusão

Testes PG dentro de `test/message-template*` conferem atividades novas, autoria da edição administrativa, escopo, ausência em replay/rollback e ausência de conteúdo sensível. A suíte canônica completa deve passar com o guardião de catálogo original intacto. Revisões finais de aderência, segurança, qualidade e performance recebem esse delta. Nenhuma mudança de schema, dependência, rota, papel, envio, canal textual ou infraestrutura é adicionada por esta admissão.

## Disposição atual

Validado pelo usuário em2026-10-21: **“Validar os dois arquivos de apoio”**. A proposta publicada em `da41a3fc` foi admitida no TODO; baseline pública dos2 arquivos capturada antes de sua primeira mutação. Execução pelo mesmo único executor, após o terminal da suíte em andamento. A admissão é complementar ao APROVADO v1.1, não uma autorização de produto/Git/deploy adicional.
