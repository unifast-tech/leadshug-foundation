# LeadsHug — registro de prontidão das dependências

Registro baseado em `delphi-ai/templates/dependency_readiness_template.md`; memória de readiness, não contrato ou aprovação. `unknown` é ausência de verificação; `healthy` exige prova recente. Referência: [brief de canais](feature-briefs/leadshug-channel-readiness-and-history-20261015.md).

## Snapshot

- **Last updated:** 2026-10-15, America/Sao_Paulo.
- **Current session/profile:** Operational / Coder com handoffs Assurance e DevOps explícitos; execução aprovada de canais NestJS/React/PostgreSQL/Prisma/Docker.
- **Why this register matters now:** usuário disponibilizará oficial e não oficial; confirmou local primeiro e Railway depois. Fechar wiring e evidência antes de executar testes externos.

## Dependency Register

| Dependency | Type | Why It Matters | Status | Last Verified | Verification Method | Known Failure Mode | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Evolution de teste | provider | QR, sessão e conexão. | unknown | 2026-10-15 | Versão2.3.7 por digest aprovada; instância própria ainda não iniciada/provada. | Contrato source não prova payload/identidade de instância real. | Criar runtime próprio, verificar versão e identidade sem adotar legado; importação fora deste recorte. |
| Conta/número oficial Meta | provider | Identidade, credencial, callback e IN/OUT. | unknown | 2026-10-15 | Operador criou app/configuração Embedded Signup, informou identificadores públicos e Graphv26.0; sandbox disponível, mas SDK/HTTPS/WABA/número/IN/OUT sem prova. | Configuração criada não comprova verificações aprovadas ou operação do canal. | Preparar backend privado e HTTPS; validar SDK/recebimento por dimensão sem publicar credencial nem identificadores em exemplos. |
| Números/interlocutores de teste | device | Troca real e recuperação. | unknown | n/a | Usuário confirmou que pode disponibilizar ambos; acesso não testado. | Disponibilidade potencial não prova pairing/permissão. | Confirmar interlocutor e vínculos descartáveis antes de mutações. |
| Callback do backend local | host/ingress | Provider precisa alcançar webhooks autenticados. | unknown | 2026-10-15 | App Meta criado, mas HTTPS/gateway/túnel ainda não iniciados; preparo autorizado. | URL incorreta, inacessível ou origem não verificável. | Preparar gateway e conferir build antes de Quick Tunnel temporário autorizado; sem DNS/túnel persistente. |
| Docker Windows | service | Engine local para runtime/testes. | healthy | 2026-10-15 | docker.exe version e inventário read-only responderam; Engine27.1.1. | Socket Linux indisponível; esta prova não certifica containers/app. | Usar cliente Windows no preparo local, com paths e wrappers confirmados. |
| Stack local LeadsHug | service | API/Web/PG e wiring dos providers. | degraded | 2026-10-15 | Overlay/runner source-owned implementados no cp7; operador/Evolution/gateway ainda não iniciados. Validação descartável passou21migrações/lint/build e parou em129/130unit. | Build/config não demonstram login, callback ou conexão real. | Corrigir teste/config Graph pela API, concluir browser e provar runtime antes do aparelho. |
| Documentação oficial Meta de onboarding | documentation | Cadastro/registro/assinatura e limites atuais. | degraded | 2026-10-15 | Developers direto limitado; coleção oficial Meta em Postman acessível para Embedded Signup, register e subscribed_apps. | Elegibilidade/app efetivo e histórico/coexistência ainda não verificados. | Usar fonte primária Postman para cadastro; histórico continua fora do recorte. |

## Operational Notes

Não há provedor classificado como healthy nesta sessão. Nenhuma credencial foi solicitada em texto, instância real foi criada, sessão foi removida ou mensagem externa foi enviada. PostgreSQL16/Node22 usados no histórico anterior são evidência daquela execução; não demonstram saúde atual dos providers.

## Inspeção local de2026-10-15

Checagem de `.env` e `api-app/.env` registrou apenas presença/ausência, sem imprimir valores: variáveis de sessão/token interno/token WhatsApp não vazias; variáveis de autenticação dos webhooks e configuração Evolution ausentes/não preenchidas. Isso não prova validade dos tokens existentes. O Compose usa `environment` explícito e não repassa esses campos ausentes; adicionar apenas ao arquivo privado não basta.

O inventário observou uma Evolution associada ao Hub legado. Esse recurso não foi consultado internamente, iniciado, parado ou adotado como dependência do LeadsHug. Sua imagem não seleciona versão para a nova instância própria. Nenhum provider continua classificado healthy; somente a disponibilidade do Engine foi comprovada.

## Versão proposta do provider local

Registry consultado em leitura confirmou `evoapicloud/evolution-api:v2.3.7@sha256:1bd8afc4a6cf48822e6cf02469aeae7bd35a12a6b616eacd1291926307f4d339`. A proposta cria instância/DB/cache próprios no overlay local; não presume compatibilidade ou saúde antes de startup/prova. Origem HTTPS única será declarada pelo operador para SDK/callback; não há domínio escolhido ou túnel aberto nesta sessão.


## Execução aprovada e readiness confirmada pelo usuário

Em2026-10-15 o usuário aprovou ST-CON-01. Informou depois que ainda não possui app Meta Embedded Signup configurado nem HTTPS de teste, e concordou em prepará-los. Essa confirmação é sobre disponibilidade, não um health check. App/autorizações requerem a conta Meta do operador; o ambiente e guia local serão preparados nesta execução. Nenhuma credencial deve ser enviada no chat.

Checkpoint1 usou Node22.23.3/Prisma6.19.3/PG16 descartável separados dos serviços existentes; schema/migration,119unidades e3E2E de aceitação passaram na fonte final desse checkpoint. Isso não prova conexões Meta/Evolution nem substitui a suíte final após o cutover. Detalhes no artefato checkpoint1-execution-evidence.md da revisão de onboarding.

Checkpoint2 API passou build/lint,130unitários e234E2E PostgreSQL,20migrações, fonte registrada em checkpoint2-api-source-hashes.sha256. A revisão independente subsequente encontrou18 achados aceitos para remediação; essa fonte ainda não é considerada integration-ready. Checkpoint4 Web passou build e25unitários; browser/backend real e provider continuam sem prova. Resultados de suites não alteram o estado unknown dos canais externos.

Preflight DevOps read-only encontrou8082,3000 e55433 ocupadas por outro projeto e confirmou ausência dos novos runners/overlay. Gateway próprio terá default configurável8083, sujeito a checagem de disponibilidade imediatamente antes do startup. Preservar recursos existentes e os PG descartáveis dos checkpoints; nenhum serviço legado foi adotado/alterado. `.env.testing` estava ausente por checagem somente de existência; é destino ignorado permitido para futura configuração de teste, recusando substituição se passar a existir.

Checkpoint5a API terminou parado, com build/lint,130unitários/19arquivos,265E2E/25arquivos,21migrações e48hashes de arquivos presentes iguais antes/depois, mais uma exclusão admitida. Prova funcional, não aceite final de ambiente: o runner provisório montou o checkout inteiro e deixou `.env` da API visível a process.loadEnvFile/Prisma; fake env explícito não exclui variáveis privadas não sobrescritas. Também não tinha CLI OpenSSL/libssl detectável e emitiu warnings. Runner DevOps source-owned deve corrigir ambos e regenerar Prisma antes da matriz final. Projetos planejados separados: operador `leadshug_channels_local`/DB homônima e validação descartável `leadshug_channels_validation`/DB `leadshug_timeline_channels_ci`; fixtures nunca seguem ao gateway público. Ainda não criados. Web assume remediação/source/build/unit; browser real-backend/PCV vem depois pelo runner próprio.

Checkpoint6 Web passou build/27unitários e preparou cinco cenários browser; não executou Playwright. DevOps cp7 implementou os oito paths runtime previstos; os relatórios cp7-api-first.json e cp7-api-retry.json registram Node22/OpenSSL3/Prisma3-target, binds read-only da principal, máscara pública da dotenv e21migrações. EBUSY do mount dist foi corrigido por volume-pai; lint/build passaram,129/130unit falhou na expectativa de Graph default. Validação descartável foi criada e removida pelo runner; operador permanece não inicializado. API cp8 assume configuração Graph explícita e harness pendente pelo mesmo runner; Web/DevOps parados. Sem stdout bruto completo cp7 anexado, essas observações do executor não são matriz final nem proof de provider.
