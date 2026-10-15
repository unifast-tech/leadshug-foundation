# LeadsHug — registro de prontidão das dependências

Registro baseado em `delphi-ai/templates/dependency_readiness_template.md`; memória de readiness, não contrato ou aprovação. `unknown` é ausência de verificação; `healthy` exige prova recente. Referência: [brief de canais](feature-briefs/leadshug-channel-readiness-and-history-20261015.md).

## Snapshot

- **Last updated:** 2026-10-15, America/Sao_Paulo.
- **Current session/profile:** Strategic / CTO-Tech-Lead; planejamento de canais NestJS/React/PostgreSQL/Prisma/Docker.
- **Why this register matters now:** usuário disponibilizará oficial e não oficial; confirmou local primeiro e Railway depois. Fechar wiring e evidência antes de executar testes externos.

## Dependency Register

| Dependency | Type | Why It Matters | Status | Last Verified | Verification Method | Known Failure Mode | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Evolution de teste | provider | QR, sessão, conexão e histórico. | unknown | n/a | Confirmar versão/runtime/configuração e depois consultar instância de teste. | Versão não fixada nas superfícies lidas; adapter pode divergir. | Não adivinhar versão nem usar serviço legado. |
| Conta/número oficial Meta | provider | Identidade, credencial, callback e IN/OUT. | unknown | n/a | Confirmar WABA/número/modalidade e permissões no target. | Listar números não prova operação do canal. | Registrar readiness por dimensão; não publicar credencial. |
| Números/interlocutores de teste | device | Troca real e recuperação. | unknown | n/a | Usuário confirmou que pode disponibilizar ambos; acesso não testado. | Disponibilidade potencial não prova pairing/permissão. | Confirmar interlocutor e vínculos descartáveis antes de mutações. |
| Callback do backend local | host/ingress | Provider precisa alcançar webhooks autenticados. | unknown | n/a | Ambiente local confirmado pelo usuário; endereço/mecanismo ainda não definido. | URL incorreta, inacessível ou origem não verificável. | Definir exposição local no contrato; não abrir túnel ou alterar DNS agora. |
| Docker Windows | service | Engine local para runtime/testes. | healthy | 2026-10-15 | docker.exe version e inventário read-only responderam; Engine27.1.1. | Socket Linux indisponível; esta prova não certifica containers/app. | Usar cliente Windows no preparo local, com paths e wrappers confirmados. |
| Stack local LeadsHug | service | API/Web/PG e wiring dos providers. | degraded | 2026-10-15 | Leitura do Compose/inventário: containers LeadsHug parados; sem serviço Evolution ou repasse de envs dos providers/webhooks. | Variáveis privadas presentes no host não chegam automaticamente ao container. | Completar contrato de runtime local antes de subir/alterar serviços. |
| Documentação oficial Meta de onboarding | documentation | Modalidade e capacidades atuais do oficial. | rate-limited | 2026-10-15 | Acesso web às páginas oficiais retornouHTTP429. | Não foi possível confirmar semântica atual de histórico/coexistência. | Retry antes de congelar decisão dependente; não substituir por blog de terceiro. |

## Operational Notes

Não há provedor classificado como healthy nesta sessão. Nenhuma credencial foi solicitada em texto, instância real foi criada, sessão foi removida ou mensagem externa foi enviada. PostgreSQL16/Node22 usados no histórico anterior são evidência daquela execução; não demonstram saúde atual dos providers.

## Inspeção local de2026-10-15

Checagem de `.env` e `api-app/.env` registrou apenas presença/ausência, sem imprimir valores: variáveis de sessão/token interno/token WhatsApp não vazias; variáveis de autenticação dos webhooks e configuração Evolution ausentes/não preenchidas. Isso não prova validade dos tokens existentes. O Compose usa `environment` explícito e não repassa esses campos ausentes; adicionar apenas ao arquivo privado não basta.

O inventário observou uma Evolution associada ao Hub legado. Esse recurso não foi consultado internamente, iniciado, parado ou adotado como dependência do LeadsHug. Sua imagem não seleciona versão para a nova instância própria. Nenhum provider continua classificado healthy; somente a disponibilidade do Engine foi comprovada.
