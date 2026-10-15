# LeadsHug — registro de prontidão das dependências

Registro baseado em `delphi-ai/templates/dependency_readiness_template.md`; memória de readiness, não contrato ou aprovação. `unknown` é ausência de verificação; `healthy` exige prova recente. Referência: [brief de canais](feature-briefs/leadshug-channel-readiness-and-history-20261015.md).

## Snapshot

- **Last updated:** 2026-10-15, America/Sao_Paulo.
- **Current session/profile:** Strategic / CTO-Tech-Lead; planejamento de canais NestJS/React/PostgreSQL/Prisma/Docker.
- **Why this register matters now:** usuário disponibilizará oficial e não oficial; definir ambiente e evidência antes de executar testes externos.

## Dependency Register

| Dependency | Type | Why It Matters | Status | Last Verified | Verification Method | Known Failure Mode | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Evolution de teste | provider | QR, sessão, conexão e histórico. | unknown | n/a | Confirmar versão/runtime/configuração e depois consultar instância de teste. | Versão não fixada nas superfícies lidas; adapter pode divergir. | Não adivinhar versão nem usar serviço legado. |
| Conta/número oficial Meta | provider | Identidade, credencial, callback e IN/OUT. | unknown | n/a | Confirmar WABA/número/modalidade e permissões no target. | Listar números não prova operação do canal. | Registrar readiness por dimensão; não publicar credencial. |
| Números/interlocutores de teste | device | Troca real e recuperação. | unknown | n/a | Usuário confirmou que pode disponibilizar ambos; acesso não testado. | Disponibilidade potencial não prova pairing/permissão. | Confirmar interlocutor e vínculos descartáveis antes de mutações. |
| Target/callbacks de teste | host/ingress | Provider precisa alcançar webhooks autenticados. | unknown | n/a | Aguardando definição local ou Railway de testes. | URL incorreta, inacessível ou origem não verificável. | Não abrir túnel, mudar DNS ou infraestrutura por suposição. |
| Documentação oficial Meta de onboarding | documentation | Modalidade e capacidades atuais do oficial. | rate-limited | 2026-10-15 | Acesso web às páginas oficiais retornouHTTP429. | Não foi possível confirmar semântica atual de histórico/coexistência. | Retry antes de congelar decisão dependente; não substituir por blog de terceiro. |

## Operational Notes

Não há provedor classificado como healthy nesta sessão. Nenhuma credencial foi solicitada em texto, instância real foi criada, sessão foi removida ou mensagem externa foi enviada. PostgreSQL16/Node22 usados no histórico anterior são evidência daquela execução; não demonstram saúde atual dos providers.
