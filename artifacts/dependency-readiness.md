# LeadsHug — registro de prontidão das dependências

Registro baseado em `delphi-ai/templates/dependency_readiness_template.md`; memória de readiness, não contrato ou aprovação. `unknown` é ausência de verificação; `healthy` exige prova recente. Referência: [brief de canais](feature-briefs/leadshug-channel-readiness-and-history-20261015.md).

## Snapshot

- **Last updated:** 2026-10-16, America/Sao_Paulo; provas cp22 e confirmação humana do painel Meta.
- **Current session/profile:** Operational / Coder com handoffs Assurance e DevOps explícitos; execução aprovada de canais NestJS/React/PostgreSQL/Prisma/Docker.
- **Why this register matters now:** usuário disponibilizará oficial e não oficial; confirmou local primeiro e Railway depois. Fechar wiring e evidência antes de executar testes externos.

## Dependency Register

| Dependency | Type | Why It Matters | Status | Last Verified | Verification Method | Known Failure Mode | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Evolution de teste | provider | QR, sessão e conexão. | degraded | 2026-10-16 | Runtime próprio fixado2.3.7 em execução; probe sem QR provou header correto/errado200/403, presença antes de DELETE e ausência posterior. | Probe não comprova pareamento/ownPhone de aparelho nem IN/OUT. | Validar aparelho pelo cadastro normal depois da fonte integrada, sem adotar legado; histórico fora deste recorte. |
| Conta/número oficial Meta | provider | Identidade, credencial, callback e IN/OUT. | degraded | 2026-10-16 | Quatro campos privados reconhecidos por booleanos; usuário confirmou allowlists no host cp22 e webhook verificado/salvo pela Meta. | App/config/callback não provam OAuth, WABA/número, inscrição messages ou IN/OUT; app continua sem publicar. | Aguardar confirmação de messages; concluir wizard normal do produto e depois validar cadastro externo. Nenhum segredo em chat. |
| Números/interlocutores de teste | device | Troca real e recuperação. | unknown | n/a | Usuário confirmou que pode disponibilizar ambos; acesso não testado. | Disponibilidade potencial não prova pairing/permissão. | Confirmar interlocutor e vínculos descartáveis antes de mutações. |
| Callback do backend local | host/ingress | Provider precisa alcançar webhooks autenticados. | healthy | 2026-10-16, cp22 | HTTPS health/login/sessão segura passaram; processo Windows destacou cloudflared e root confirmou vida após STOP; Meta confirmou verificação do callback. | Quick Tunnel é efêmero; prova anterior não garante disponibilidade futura. | Usar somente https://mistress-spencer-mozilla-sciences.trycloudflare.com; callback /webhooks/meta. Revalidar antes do teste; host seafood anterior está retirado. |
| Docker Windows | service | Engine local para runtime/testes. | healthy | 2026-10-15 | docker.exe version e inventário read-only responderam; Engine27.1.1. | Socket Linux indisponível; esta prova não certifica containers/app. | Usar cliente Windows no preparo local, com paths e wrappers confirmados. |
| Stack local LeadsHug | service | API/Web/PG e wiring dos providers. | degraded | 2026-10-16, cp24/cp25 | Operador atualizado/22migrações; all498testes passou com230referências públicas pré/pós iguais e bundle conferido. Cp25 validou precedência do inicializador e HTTPS/sessão/CORS exatos. | BFF owner ainda retorna ONBOARDING_PENDENTE; revisão delta e prova externa pendentes. | Concluir reviews afetados e final; usuário confirma messages e wizard normal, sem bypass/seed; depois testar canais reais. |
| Documentação oficial Meta de onboarding | documentation | Cadastro/registro/assinatura e limites atuais. | degraded | 2026-10-15 | Developers direto limitado; coleção oficial Meta em Postman acessível para Embedded Signup, register e subscribed_apps. | Elegibilidade/app efetivo e histórico/coexistência ainda não verificados. | Usar fonte primária Postman para cadastro; histórico continua fora do recorte. |

## Operational Notes

Não há canal externo classificado como conectado/validado. Nenhuma credencial foi solicitada em texto, aparelho pareado ou mensagem externa enviada. A instância de probe foi criada e removida no runtime próprio sem QR. O alcance HTTPS e a verificação Meta são evidência de transporte/configuração, não de cadastro ou entrega de mensagens.

Evidência atual: [handoff HTTPS cp22](reviews/leadshug-number-onboarding-20261015/evidence/cp22-https-handoff.md), [painel Meta](reviews/leadshug-number-onboarding-20261015/evidence/cp22-meta-panel-setup.json) e [validação API cp22](reviews/leadshug-number-onboarding-20261015/evidence/cp22-rerun3-result.json). Os registros abaixo preservam o histórico dos checkpoints; as ausências ali descritas não representam o snapshot atual.

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


Checkpoint8 API no runner source-owned concluiu137unitários/277E2E e21migrações com Node22.23.3/OpenSSL3.0.22/Prisma debian-openssl-3.0.x. Root conferiu153hashes públicos antes/depois idênticos; log bruto cp8 preservado no review de onboarding. API parou. DevOps cp9 acrescentou4binds públicos faltantes e corrigiu prefixos de colisão/Graph fixture, config-only passou sem criar recursos, depois parou. Web cp10 é único writer, passou build/27unitários e iniciou preparação do Playwright pelo runner. Browser ainda sem resultado terminal; nenhum provider passa a healthy por essas observações. Dados .local-files e env privados não pertencem à coleta de source freshness. Operador ainda não inicializado; não há URL HTTPS ou teste real Meta/aparelho.


Checkpoint16:44/44 Playwright passaram contra BFF/sessão/PostgreSQL reais e bundle recém-compilado/servido com hash conferido antes dos workers. Root comparou os14paths Web e50paths alterados API com a fonte atual, sem diferenças. Replay perdido e FRC100triggers passaram; QR e refresh de mensagem preservaram ID/autoria com provider/SDK doubles. Essa prova não altera unknown dos providers. DevOps cp17 assume único writer para operador real, logs/headers, all final e HTTPS; API/Web param. A nova regressão PG novaBU cp15 ainda aguarda all. `.env.testing` e recursos do operador devem ser criados exclusivamente pela inicialização, sem adoção de ambientes existentes.
