# Fresh no-context focused final provider fence HOW opinion

## Closed package
```json
{
  "kind": "closed-focused-final-provider-fence47-HOW-opinion",
  "reviewKind": "architecture_opinion",
  "governingTodo": {
    "path": "foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md",
    "bytes": 276303,
    "sha256": "d43e788f8ee4057d6a6deda7862c24b21d7c54f0eb227bebe71859855b1e9056"
  },
  "requiredSourceBodies": [
    {
      "path": "api-app/src/domain/channels/transport/channel.ts",
      "bytes": 13235,
      "sha256": "aa6485060287910d586d17b8cbffe2f194b1b3a29fb71c697f27e0b78c28ffbf"
    },
    {
      "path": "api-app/src/domain/inbox/channel-eligibility-policy.ts",
      "bytes": 9602,
      "sha256": "9812de537d5e5f0c84ae9b824b7343f8dfd9f63dfa0520f6da9a7063d2d13eee"
    },
    {
      "path": "api-app/src/integrations/channels/prisma-channel-resolver.ts",
      "bytes": 64107,
      "sha256": "607a14170052225551396210293625f26182385c7bc7fa1e6acfa318c405aa0f"
    },
    {
      "path": "api-app/src/domain/inbox/outbound.service.ts",
      "bytes": 49351,
      "sha256": "37bcfc6cdc9e3ba53f8ee97ec68c923d07aab8bb90492b60872ece10ae473c30"
    },
    {
      "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
      "bytes": 48540,
      "sha256": "559039c84b20ac986b6bc3b2b0590a50a6be9454634d7bbb2c05d706c5a387e4"
    },
    {
      "path": "api-app/src/domain/channels/channel-credential-resolver.ts",
      "bytes": 9525,
      "sha256": "34f25985091f0c0873b682bc3d27f7eb0cde95a56e5b74497afdc541f79f7630"
    },
    {
      "path": "api-app/src/domain/inbox/initial-message.service.ts",
      "bytes": 24534,
      "sha256": "aa33ca7ed6f74cabd878ebccec9529dd6a32b8311dad107babbc212d905ecc41"
    },
    {
      "path": "api-app/src/domain/inbox/conversations.service.ts",
      "bytes": 9520,
      "sha256": "1aa8ad944527529255b589af45f5e1d05aa0bc36d504f2315330ca9ed546cd5b"
    },
    {
      "path": "api-app/src/surfaces/bff/conversations.controller.ts",
      "bytes": 21521,
      "sha256": "799a1866c203557b9a115c327dfb466b40c71cb937218997c1a2fecec6ad34e2"
    },
    {
      "path": "api-app/src/infra/session/session.service.ts",
      "bytes": 5483,
      "sha256": "884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200"
    },
    {
      "path": "api-app/src/domain/access/access.service.ts",
      "bytes": 2390,
      "sha256": "2ef3761a138d7c8c386c5ddb4bf2a2000c960328789834bde5e12135a1ea66e7"
    },
    {
      "path": "api-app/src/domain/access/scope.ts",
      "bytes": 5701,
      "sha256": "412f68eb157328855c87cb86b6b89cc1c267eee7068dc59c0abbe085074db26d"
    },
    {
      "path": "api-app/src/integrations/channels/instagram-channel.ts",
      "bytes": 2375,
      "sha256": "ed53f4eb0119ec6187c115e5816412d0cd2ef00213d83f341efd8640bac5f526"
    },
    {
      "path": "api-app/src/integrations/channels/meta-channel.ts",
      "bytes": 3900,
      "sha256": "99a9ca01a57527a76de54cdbdf8b49f65b5dcceb1a71abce883d1845c6cd8f26"
    },
    {
      "path": "api-app/src/integrations/channels/evolution-channel.ts",
      "bytes": 2211,
      "sha256": "6a41ef2f3b0ee9e5c6b381d54faf48b0b2c672e52751f8be1480ad01cb178a34"
    },
    {
      "path": "api-app/src/integrations/instagram/instagram-messaging.client.ts",
      "bytes": 2815,
      "sha256": "a5efd1ced025fa3822126cd4deada4ca5c31505edefa3cc71d85a475a9de28a5"
    },
    {
      "path": "api-app/src/domain/channels/channels.service.ts",
      "bytes": 46758,
      "sha256": "3783c1b2a3afa982b4e9d719c71c172df1717bda7ba380ef143c9dd06045805f"
    },
    {
      "path": "api-app/src/domain/channels/instagram-authorization.service.ts",
      "bytes": 73878,
      "sha256": "2ecfcbfe83de72da41f3b89543df021d164168cccc13254b63c1069a84e6263a"
    },
    {
      "path": "api-app/test/instagram-cp3-authorization-fences.e2e-spec.ts",
      "bytes": 15205,
      "sha256": "ac62369b48608336ab89e1a865881927d3a1ab5c1821653e6006a24318a30411"
    },
    {
      "path": "api-app/test/helpers.ts",
      "bytes": 34495,
      "sha256": "79c9343d80b72b1d8c378d6946bf38997133d528117b11a4fc1827fa3e52586c"
    }
  ],
  "sourceCount": 20,
  "evidence": [
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-adherence46a-raw.json",
      "bytes": 7301,
      "sha256": "d6bd798c4dfd1c0afadc67c81fd13dcc0f88c7d385bdc14d20e47c71bc4bebc2"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-adherence46b-raw.json",
      "bytes": 9994,
      "sha256": "e0bc9ca5ee93a9f40370c06e1b1609641f6bb8531e97931c1b09f56e1f38cf08"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-adherence46-root-adjudication.json",
      "bytes": 3703,
      "sha256": "56bc6fe372e9bfda183e5cd45b13d56bc0d04f1370102036802080fa5e98b39a"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-api45-root-reconciliation.json",
      "bytes": 3310,
      "sha256": "4ed54d84ff162b52e18a57e9e92a31a9936e2d9e32d3f6d8b51f66ae08c169f0"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-api45-result.json",
      "bytes": 4197,
      "sha256": "293aaa58ccea7b0b9bc66bb96ee3e129fa8a8920cd1e1565b6082508a410f04e"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-auth36-terminal.json",
      "bytes": 1615,
      "sha256": "c27674ac93dc888fa817fa78f2e2263b1fd44fba9dc2756f25492e1ed43a0b83"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-repair44-terminal.json",
      "bytes": 2076,
      "sha256": "ec5f6e149b492558fbe6bc26d39c0ef91c5e1bb267630b1fd47ada1af92ca12a"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/primary-subscription-index-research40.json",
      "bytes": 2739,
      "sha256": "10c684467046785d87396a31d01ef80ef878d5f9bd2de7fc753a7d899602285d"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp4-connections-preparation21-root-qualified.json",
      "bytes": 2543,
      "sha256": "3e9e59a0f972fa7d02b33833515c8bc4d15b00dee5847fbb1f710916ce4a7969"
    },
    {
      "path": "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp4-browser-composer-preparation23-root-qualified.json",
      "bytes": 4783,
      "sha256": "9923d9fcd1045355665ec9793968c6431518f0d363e18a914e063f74dbff79c2"
    }
  ],
  "question": "Choose the simplest faithful HOW to fix IG-CP3-A46-01 under the EXISTING approved WHAT. Do not reopen Channel architecture or waive delivery. Current finalProviderFence awaits contextBeforeDispatch then policy.inspect then BFFactor callback; mutable provider/generation/credential facts can change during the later awaits while actor remains live. All API45 tests pass but do not cover this interleaving. Existing callback locks actor/grant/BU rows, not provider facts. Current bound adapters do extra context checks BEFORE common callback, not after it. Need a coherent last awaited local authorization observation covering the captured current tuple AND current actor, followed by synchronous signed-session/deadline/window/credential-margin checks and provider HTTP OUTSIDE any transaction. Preserve no-redispatch ACK/V1 facts and common sender/policy owners.\nAssess a short coherent transaction reusing current resolver validation and actor callback with appropriate NOWAIT row pins and canonical lock order, versus a genuinely simpler atomic final read/port if actually feasible. The current callback checks signed session after its raw query; a new transaction adds a later awaited COMMIT, so explicitly preserve a synchronous session-expiry check after that last await, not only captured operation deadline. Do not solve by repeatedly alternating context and actor reads, holding transaction over provider HTTP, broad locks, extending deadlines, provider-specific branches in generic sender, new plugin framework, or guessed external protocol. No product/schema/config/HTTProute change outside existing approved intent is authorized by this opinion.\nSpecify concrete internal signatures/data flow, minimal existing admitted source/test paths, lock order and transient contention outcome, and why actor/policy/provider facts cannot become mixed DURING remaining awaits. Be precise about the unavoidable instant after a valid final local observation: do not claim atomic external network effects with DB state. Identify the correct linearization/acceptance interpretation within current contract, not a hidden criterion waiver.\nPlan faithful native causal RED then GREEN controls using actual successful reauthorization (encrypted credential replacement, not metadata-only change), actual existing WhatsApp disconnect, real PostgreSQL and provider HTTP fake only. Existing auth helper holds contextBeforeDispatch AFTER its delegated read; this is a real current interleaving because more awaits follow, but after a coherent final observation the same test-inserted post-read pause could manufacture a false stale failure. Define native oracles that prove a mutation committed BEFORE final authorization prevents POST, and prove correct serialization if the coherent final observation pins rows so lifecycle mutation must wait. Preserve actual grant/session negative+live controls, current P2002/lock thresholds and no wrong-account POST. No fixture assertions weakened merely to accommodate design; explain necessary observation-hook adaptation honestly.\nAll review advice is HOW only; if any recommendation changes WHAT/validation scope, flag it instead of implementing. Complete CP4 and primary GET proof remain open independently. Return canonical architecture_opinion JSON, all five positions and concrete recommendation. No tools or source edits.",
  "authority": "Existing approvedSTIG03v1.3, no product edits fromopinion; exactprotectedOAuthmiddleware/access/session/concreteproviderclients preserved. Advice doesnotapprove newWHAT or runtime.",
  "frontendConsumerMatrix": "Actual normative T matrix enclosed. CP4connections/lifecycle/safeprojection/composer/realtime/HTTPSbrowser NOTimplemented/no waiver; full featuredelivery stillmandatory. This review only chooses HOW for currenthighA46 interleaving.",
  "currentTests": "RootAPI45 full424unit+586E2E GREEN for matching261/T690inputs35rows3links; doesnotprove uncovered A46 race. Current20fullbodies are actualAPI45source. NewnativecausalRED notyet authored/run.",
  "model": "gpt-6.1-sol",
  "effort": "xhigh",
  "execution": "Canonical runner/closedstdin/no tools; onlystrictCLI model_reasoning_effort=xhigh argvconfig in-memory; no runnerfile/config edit."
}
```

## Governing contract (all normative sections, currentconsumer matrix and actual46 finding resolution)
# TODO — LeadsHug Instagram Direct por Channel

## Title
ST-IG-03 — Conectar Instagram e atender DMs na mesma BU dos WhatsApps

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`
- **Artifact status:** In-Progress
- **Contract version:** 1.3 — APROVADO em2026-10-23; implementação governada, sem ativação real autorizada.
- **Template:** copiado de `delphi-ai/templates/todo_template.md` em2026-10-23; seções aplicáveis preenchidas abaixo.

## Context
O usuário priorizou Instagram antes de histórico, confirmou conta profissional para teste e acesso para autorizá-la, confirmou a configuração com login do Instagram no app Meta existente e escolheu reunir os canais na mesma BU. A BU operacional, contatos qualificados, ownership empresarial e rota foram ratificados pelo APROVADO v1.3 e consolidados como arquitetura alvo. A implementação e suas provas continuam em curso. ST-CON-01/04/05/06 são baseline local entregue, não código que este TODO possa substituir silenciosamente. Preservar dados e recuperar envios pendentes exige mais que acrescentar INSTAGRAM ao enum.

## Framing Source & Story Slice
- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/leadshug-instagram-channel-20261023.md`
- **Primary story ID:** ST-IG-03; dependências subordinadas ST-IG-01/02.
- **Why this is the right current slice:** uma entrega funcional coesa: autorizar uma conta, receber uma DM e responder texto pelo Atendimento usando Channel. Identidade e conexão são pré-requisitos dessa mesma prova; checkpoints não declaram entregas parciais suficientes.
- **Direct-to-TODO rationale:** n/a; há brief, decisão de BU e desenho revisado.
- **Design evidence:** `foundation_documentation/artifacts/analysis/leadshug-multichannel-identity-definition-20261023.md`.

## Contract Boundary
Este TODO define WHAT, exclusões e critérios de entrega. A baseline v1.3 abaixo foi revisada e aprovada explicitamente em2026-10-23. “Pode fazer” em2026-10-23 autorizou preparar o TODO/revisão, não código, banco, credenciais, runtime ou Meta. A execução está limitada à versão revisada e aprovada, com authority guard go registrado. Qualquer alteração material de escopo, decisões, validação, rota pública ou padrões de diff exige reconvergência e nova aprovação; descobertas locais que preservam o objetivo podem ser concretizadas dentro dele.

## Implementation Intent
- **Current delivery:** DM individual textual Instagram, iniciada pelo usuário externo; conexão explícita na BU; resposta humana pelo mesmo recurso; evolução necessária de identidade e roteamento com regressão WhatsApp.
- **Planned next steps:** mídia, importação histórica, CRM, merge de contatos, automação Instagram e outros canais; informacionais.
- **Anticipatory implementation authorized now:** none; nem código desta fatia antes de APROVADO.
- **Rationale:** identidade/ownership/rota são usados pelo percurso atual. Não criar framework de plugins, catálogo universal de capacidades ou operação futura sem uso.

## Delivery Status Canon (Required)
- **Current delivery stage:** Pending
- **Qualifiers:** none
- **Next exact step:** concretizar HOW de fence final coerente paraA46-01 em opinião técnica delimitada, depois REDcausal de reautorização/desconexão e elegibilidade inicial antes de reparar os3achados46. API45GREEN preservada como baseline; CP4 completo segue obrigatório.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** implementation
- **Why this state now:** API45 completaGREEN sobre261fontes/T/690inputs/35preservações/3gitlinks; lint/build/31mig/424unit/586E2E. Sourcefixes35..44 têm prova de execução, aguardam adherence46afetada. CP4 e gates restantes continuam obrigatórios.
- **Exit condition:** todos os checkpoints e critérios validados, revisões/guards completos e prova runtime posterior explicitamente aprovada; nenhum fechamento parcial implícito.

## Blocker Notes
- **Blocker:** none for remaining admitted code/disposable synthetic validation. Exact OAuth-session v2 source is applied; corrected infrastructure tests24 passed in API29 with native503 and callback confidentiality controls. Browser/gateway proof remains unvalidated. Privacy HTML and outbound UTF-8 proposals await explicit human validation; primary own-subscription observation remains unresolved, no gate waiver.
- **Last confirmed truth:** API45 completaGREEN:424unit39files/586E2E55files; auth6/ACK4/query4/CSV1/native lock3grupos/P2002count3/finalclock9/residual12 passaram. Lote1000 inicial5099.176ms/replay3344.715ms e asserts seguintes passaram. Root conferiu261fontes/T/690inputs/35preservações/3gitlinks/log226548bytes SHA07fd007b5795d91b324b1f2baf8e315004271c6957639c9cfb7c51eb2070aa8a. Evidência somente API; fonteadherence46/CP4/primário/runtime ainda pendentes.
- **Runtime boundary:** ativação real, leitura privada, Meta e prova física dependem do plano posterior; nenhuma autorização herdada é reutilizada.

## Scope
- [x] SCOPE-01 Consolidar, após aprovação, as propostas DEC-qualified-contact-conversation, DEC-business-resource-provider-identity e DEC-explicit-channel-routing nos owners canônicos, distinguindo arquitetura e entrega.
- [ ] SCOPE-02 Estabelecer contato local e identidade externa qualificada, recursos empresariais e rotas imutáveis; no máximo um recurso empresarial WhatsApp durável por BU (oficial+Evolution no mesmo número comprovado) e múltiplas contas Instagram; preservar IDs de BU/conversa/mensagem e identidades técnicas existentes.
- [ ] SCOPE-03 Migrar consumidores de telefone/tipo para identidade/rota; BFF multicanal, API pública, Typebot e Consultar (lista/drilldown/CSV) preservados no subconjunto WhatsApp, sem Instagram acidental.
- [ ] SCOPE-04 Conexão Instagram Login no app existente com configuração própria do produto, tentativas por ator/sessão/BU, autorização server-side, armazenamento cifrado, reautorização e desconexão locais explícitas.
- [ ] SCOPE-05 Ingresso Instagram autenticado, normalização textual, deduplicação transacional e estado honesto de recebimento; nenhum sucesso inferido de OAuth/challenge sintético.
- [ ] SCOPE-06 Implementação Instagram registrada no Channel; política textual por recurso; envio pelo único OutboundService e aceitação comuns, sem fallback e sem retry externo ambíguo.
- [ ] SCOPE-07 Cadastro de conexões e Atendimento React com origem/conta/contato legíveis, compositor vinculado à rota e proteção contra resposta atrasada/troca de BU.
- [ ] SCOPE-08 Testes comuns e específicos, PostgreSQL, navegador real-backend/freshness, concorrência, isolamento, cutover, provas físicas e fechamento local com todos os gates.

## Out of Scope
- [ ] Posts/reels, comentários, comentário→DM, prospecção por username, DM não solicitada, grupos Instagram, templates Instagram, mídia, campanhas e importação histórica.
- [ ] Merge de contatos/conversas entre plataformas, contatos globais, transferência de recurso entre BUs, CRM, novas automações Instagram ou ativação implícita de Typebot.
- [ ] Facebook/Messenger, Telegram, novo provedor WhatsApp, migração/desregistro de números, alterações de outros apps/partners/roteamento Meta e desvincular WhatsApp existente.
- [ ] Railway/produção, publicação/app review Meta, Git de produto/promoção, worktrees/checkouts/cópias auxiliares, branches worker/reconcile ou alterar gitlinks/.gitmodules.
- [ ] Ler/listar/hash de arquivos privados, `.env*` reais, bancos/conversas/logs/credenciais operacionais, argumentos/env de processos ou volumes. Testes usam somente inventário público e valores sintéticos. `.env.example` é configuração pública admitida. Runtime real e eventual exceção limitada do verificador de diff exigem plano posterior explícito; nenhuma autorização herdada de ST-CON-04 é reutilizada.

## Execution Lane Tracking (Required)
- **Local implementation branches:** principal checkout API/Web no estado existente; nenhum branch, worktree, commit/push de produto criado por este planejamento. Foundation:main, único checkout.
- **Promotion lane path:** n/a para entrega local; promoção futura separada, pelo mesmo TODO se admitida.
- **Lane-promoted threshold for this TODO:** n/a; Local-Implemented somente.
- **Production-ready threshold for this TODO:** fora desta aprovação.

## Diff Expectation Contract
- **Contract status:** required
- **Policy:** strict; unclassified or forbidden paths block delivery
- **User validation:** required on deviation
- **Comparison mode:** working_tree

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| root | . | 80e3940126f22a941f90dba4f5e801b6c0eb2f58 | working_tree |
| API | api-app | db5a86758a165fac8a1ab587599c37b17890530c | working_tree |
| Web | web-app | 74b9d4b714044829796f875d00553f077c1c329d | working_tree |
| Foundation | foundation_documentation | f191266a4ae06042c875ca1efb4454a6d0ec7d52 | working_tree |

Baselines Git não representam checkout limpo: `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/public-source-baseline.json` sela218arquivos API e54Web, inclusive entregas locais anteriores ainda não commitadas. Conteúdo pré-existente fora da fatia deve ser preservado por comparação de inventário/bytes; não reverter nem incluir como implementação Instagram. Contrato de diff e herança foram reconvergidos para review v1.1; não rodar varredura integral com arquivos privados neste planejamento.

### Expected Changed Paths
| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| root | scripts/test-channels-local.sh | M | safe runner/admissão de fontes e cenários Instagram |
| root | scripts/check-channels-ci-parity.py | A,M,?? | paridade explícita dos specs novos |
| root | .github/workflows/ci.yml | M | paridade de config/testes; sem promoção |
| root | docker-compose.channels.yml | M | somente validação/variáveis públicas sintéticas da capacidade nova |
| root | docker/local-gateway.conf.template | M | callback seguro, sem query/logs privados |
| root | .env.example | M | contrato público de configuração Instagram |
| root | api-app | M | projeção de submódulo, índice não pode ser alterado |
| root | web-app | M | projeção de submódulo, índice não pode ser alterado |
| root | foundation_documentation | M | projeção documental, índice preservado |
| API | prisma/schema.prisma | M | identidade, contato, rota e OAuth |
| API | prisma/migrations/*_instagram_*/migration.sql | A,?? | migração versionada delimitada, sem reset |
| API | src/domain/channels/** | A,M,?? | conexões, identidade empresarial, credenciais e contratos Channel |
| API | src/domain/inbox/** | A,M,?? | contato/rota, política, aceitação e recuperação |
| API | src/infra/http/body-parsers* | A,M,?? | raw bytes e limite específico do webhook, incluindo testes |
| API | src/infra/config/modulos* | A,M,?? | capacidade Instagram isolada e testes de configuração pública |
| API | src/domain/tenancy/tenancy.service.ts | M | BU operacional sem exigir telefone |
| API | src/domain/historico/catalogo.ts | M | eventos seguros, sem token/conteúdo DM |
| API | src/domain/historico/cobertura.ts | M | leituras justificadas |
| API | src/integrations/channels/** | A,M,?? | composição e resolver por vínculo/rota |
| API | src/integrations/instagram/** | A,?? | cliente/protocolo Instagram isolados |
| API | src/surfaces/bff/session.middleware.ts | M | Exact reviewed OAuth callback confidentiality v2 only; user admitted2026-10-24, original/candidate hashes in oauth-callback-session-user-admission-v2.json |
| API | src/surfaces/bff/me.controller.ts | M | Bound legacy BU connections projection to compatible WhatsApp max2; preserve grants and other controller behavior |
| API | src/surfaces/bff/bff.module.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/conversations.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/channels.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/number-registrations.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/bff/instagram-authorizations.controller.ts | A,M,?? | projeções/registro dos controllers governantes de conexão/inbox |
| API | src/surfaces/webhooks/** | A,M,?? | callback/OAuth/ingresso Instagram sem mudar semântica WhatsApp |
| API | src/surfaces/public/conversations.controller.ts | M | conservar API v1 WhatsApp pelo namespace correto |
| API | test/*instagram*.e2e-spec.ts | A,?? | OAuth/ingresso/isolation/routing/cutover reais |
| API | test/*multichannel*.e2e-spec.ts | A,?? | identidades, colisões e preservação |
| API | test/*onboarding*.e2e-spec.ts | M | fixtures/asserts com a nova identidade, sem perder cenários |
| API | test/initial-message.e2e-spec.ts | M | snapshots e recuperação de aceitos |
| API | test/channel-transport.e2e-spec.ts | M | substituição por Channel e rota |
| API | test/api-publica.e2e-spec.ts | M | API antiga não trata ID Instagram como telefone |
| API | test/atendimento.e2e-spec.ts | M | inbox/claim/readback |
| API | test/webhooks.e2e-spec.ts | M | autenticação, echo e dedup |
| API | test/historico.e2e-spec.ts | M | Canonical fixtures and qualified WhatsApp Consultar boundary assertions; preserve all existing scenarios/assertions |
| API | test/painel.e2e-spec.ts | M | Canonical fixture-only adaptation for mandatory contact identity; preserve all existing scenarios/assertions/counters |
| API | test/historico-atividades.e2e-spec.ts | M | Canonical fixture-only adaptation for mandatory contact identity; preserve all existing scenarios/assertions/counters |
| API | test/setores.e2e-spec.ts | M | Canonical fixture-only adaptation for mandatory contact identity; preserve all existing scenarios/assertions/counters |
| API | test/helpers.ts | M | seed determinístico por identidade |
| API | test/browser-server.cjs | M | backend real e fake de fronteira HTTP |
| API | test/timeline-fixtures.cjs | M | persistência/identidade sintéticas |
| API | .env.example | M | nomes de configuração sem segredos |
| Web | src/telas/Inbox.tsx | M | rota e identidade legíveis |
| Web | src/telas/Numeros.tsx | M | BU/conexões multicanal, preservando WhatsApp |
| Web | src/componentes/CadastroNumero.tsx | M | link de cadastro WhatsApp por conexão |
| Web | src/componentes/NovaConversa.tsx | M | texto/template WhatsApp e capacidades corretas |
| Web | src/componentes/*Instagram* | A,?? | conexão/callback/estado Instagram |
| Web | src/*instagram* | A,?? | estado puro e testes do fluxo |
| Web | src/api.ts | M | DTOs seguros e rota esperada |
| Web | src/api.spec.ts | M | contratos/erros seguros |
| Web | src/cadastroNumero* | M | lifecycle WhatsApp preservado |
| Web | src/componentes/NovaConversa.spec.ts | M | rascunho/fences/política |
| Web | e2e/instagram*.spec.ts | A,?? | jornada browser completa |
| Web | e2e/number-onboarding.spec.ts | M | não regredir cadastro |
| Web | e2e/channel-transport.spec.ts | M | substituição e rota |
| Web | e2e/start-conversation.spec.ts | M | primeiro envio existente |
| Web | e2e/message-templates.spec.ts | M | modelo WhatsApp não elegível Instagram |
| Web | e2e/*freshness.ts | M | inventário positivo e backend real |
| Foundation | todos/active/features/TODO-leadshug-instagram-channel.md | A,M,?? | contrato/evidências |
| Foundation | todos/completed/features/TODO-leadshug-instagram-channel.md | A,?? | apenas após conclusão |
| Foundation | artifacts/tmp/instagram-channel-planning/** | A,M,?? | preparação/reviews/guards públicos |
| Foundation | artifacts/reviews/leadshug-instagram-channel-20261023/** | A,M,?? | evidências delimitadas |
| Foundation | artifacts/feature-briefs/leadshug-instagram-channel-20261023.md | A,M,?? | enquadramento autorizado |
| Foundation | artifacts/analysis/leadshug-multichannel-identity-definition-20261023.md | A,M,?? | desenho autorizado |
| Foundation | decisions/leadshug-multichannel-identity-decisions.md | A,M,?? | proveniência/aceitação após aprovação |
| Foundation | decisions/README.md | M | índice singular |
| Foundation | domain_entities.md | M | identidade do contato aprovada |
| Foundation | project_constitution.md | M | consolidação estratégica já iniciada, sem claim de execução |
| Foundation | policies/scope_subscope_governance.md | M | BU operação/rotas governadas |
| Foundation | modules/identity-and-tenancy.md | M | contrato canônico do owner tocado |
| Foundation | modules/inbox-and-conversations.md | M | contrato canônico do owner tocado |
| Foundation | modules/integrations-and-channels.md | M | contrato canônico do owner tocado |
| Foundation | modules/audit-and-history.md | M | contrato canônico do owner tocado |
| Foundation | backlog/README.md | M | candidato/next gate |
| Foundation | system_roadmap.md | M | prioridade antes de histórico |
| Foundation | artifacts/dependency-readiness.md | M | readiness honesta |
| API | prisma/migrations/20261020170000_message_inbound_window_index/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261021130000_message_template_drafts/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261021150000_message_template_operations/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261022140000_initial_message_orchestration/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261022150000_initial_message_admissions/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | prisma/migrations/20261022160000_initial_message_inbox_order/migration.sql | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-definition.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-definition.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-draft.service.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-management.dependencies.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-management.ports.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-management.ports.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-observation.service.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-submission.service.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/domain/message-templates/template-transaction-boundary.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/message-templates/template-management.module.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/message-templates/template-management.resolver.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/initial-message.client.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/initial-message.client.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/message-template.client.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/message-template.client.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/surfaces/bff/message-templates.controller.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | test/conversation-start.e2e-spec.ts | A,M,?? | Canonical fixture/qualified lookup/context adaptations only; preserve all scenarios/assertions/counters and deliberate v1 cutover cases; baseline hash retained, final freeze lifted per IG-CRIT-R1-01 |
| API | test/dispatch-admission.e2e-spec.ts | A,M,?? | Canonical fixture/qualified lookup/context adaptations only; preserve all scenarios/assertions/counters and deliberate v1 cutover cases; baseline hash retained, final freeze lifted per IG-CRIT-R1-01 |
| API | test/message-template-bff.e2e-spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | test/message-template-drafts.e2e-spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | test/message-template-management.e2e-spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/evolution/evolution.client.spec.ts | M | Limited user-validated Evolution observation guard/unit tests; exact scope and original hashes in evidence/evolution-observation-companion-user-validation.json; no unrelated mutation |
| API | src/integrations/evolution/evolution.client.ts | M | Limited user-validated Evolution observation guard/unit tests; exact scope and original hashes in evidence/evolution-observation-companion-user-validation.json; no unrelated mutation |
| API | src/integrations/meta/meta.client.spec.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/integrations/meta/meta.client.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| API | src/surfaces/public/public.module.ts | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Web | src/telas/Modelos.spec.ts | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Web | src/telas/Modelos.tsx | ?? | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Web | src/App.tsx | M | Inherited public source ONLY; byte-exact baseline hash required, NO new Instagram mutation |
| Foundation | artifacts/reviews/leadshug-channel-abstraction-20261020/evidence/v13-public-product.diff | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| Foundation | artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-output-e53-v1.1.txt | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| Foundation | artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-output-e54-v1.1.txt | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| Foundation | artifacts/reviews/leadshug-start-conversation-20261022/evidence/test-quality-public-roots-output-e64-v1.1.txt | M | Existing carried difference ONLY; preserve exact current hash, do not edit/stage/normalize |
| root | [ ]foundation_documentation/artifacts/tmp/st-con-05-r27-browser-capture-20261021T2325Z/chunks/012.json | ?? | Prior ST-CON-04 retained109byte artifact only, exact SHA b9e84a70e27049eb661ac7c9496c0db2a8721f8c46909aa90f872e6c40ec7c80; no input/proof or new mutation; later authorized companion check required |

### Not Expected Changed Paths
| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| root | .gitmodules | any | pipeline-owned, sem alteração |
| root | .env | any | segredo privado |
| root | .env.testing | any | segredo privado |
| API | .env | any | segredo privado |
| API | .env.testing | any | segredo privado |
| API | .local-files/** | any | dados privados |
| Web | .env | any | segredo privado |
| Web | .env.testing | any | segredo privado |
| API | package-lock.json | any | nenhum pacote novo é necessário para HTTP/crypto |
| Web | package-lock.json | any | nenhum SDK novo no browser |
| Foundation | todos/completed/features/TODO-leadshug-start-conversation-by-contact.md | any | preservar prova anterior |

### Diff Deviation Analysis
Superfícies root/safe runner/CI/compose/gateway e diferenças públicas herdadas estão admitidas por caminhos exatos e inventário de preservação em evidence/inherited-public-preservation-v1.2.json. Só a zona de mutação desta fatia pode ganhar alterações; herança fora dela deve manter hashes/deleções e índice root. O resíduo root109bytes conserva a admissão exata anterior e exige companion autorizado posterior. Não executar guards integrais que enumerem/leiam/hash privados até o plano específico posterior; code approval não concede essa exceção. Nada será restaurado automaticamente para satisfazer guard.

Active v1.2 preserves35inherited rows plus two user-admitted Evolution paths. Complete original v1.1 policy and hashes remain unchanged historical evidence.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** nomes privados de classes, índices e testes dentro das responsabilidades congeladas; correções exigidas pelo mesmo percurso.
- **Must update or split the TODO:** mídia, merge, nova plataforma, publicação Meta, outro ambiente, permissões mais amplas, política externa diferente ou novos caminhos fora da admissão estrita.

## Definition of Done
- [ ] DOD-01 Contato local, identidades qualificadas e rota imutável têm unicidade/FKs que comprovam mesma BU, mesmo contato e recurso da conexão; nenhum recurso empresarial em duas BUs através de adapters. Uma BU admite um recurso WhatsApp durável, com seus dois adapters, e várias contas Instagram; outro número WhatsApp falha409sem alterar owner.
- [ ] DOD-02 Migração preserva IDs de conversa/mensagem/BU/ProviderResourceIdentity, autoria, timestamps, unread e conteúdo; proveniência desconhecida conserva sua incerteza. Snapshots/intenções antigos e conclusão local de aceitos têm cutover explícito, sem HTTP repetido.
- [ ] DOD-03 Conexão OAuth Instagram é ADMIN+, idempotente, ligada à sessão e ao recurso verificado; tokens cifrados, expirados/revogados não habilitam envio; reautorizar não muda recurso/owner silenciosamente.
- [ ] DOD-04 Webhook autentica raw body e app correto antes de conteúdo; nova entrada e replay concorrem sem duplicar contato/conversa/mensagem/unread; echo não vira entrada nem autoria humana inventada.
- [ ] DOD-05 DM textual aparece na lista/thread da BU; resposta usa rota exata pelo Channel/OutboundService, respeita política e conserva distinção entre aceitação e entrega.
- [ ] DOD-06 Cadastro/Atendimento apresentam BU, conta/origem e remetente sem tratar ID Instagram como telefone; ações/rascunhos e respostas assíncronas estão vinculados à BU/rota/geração.
- [ ] DOD-07 API v1, Typebot e Consultar/lista/drilldown/CSV WhatsApp mantêm contratos e isolamento; projeções legadas de conexões carregam no máximo os dois bindings WhatsApp compatíveis e não hidratam Instagram; Instagram não entra por telefone ou ativa bot por acidente; autoria/modelos/janela atuais preservados.
- [ ] DOD-08 Harness de dependência abstrata, batch/queries limitadas e invariantes PostgreSQL/concorrência passam; nenhum framework genérico ou fallback escondido.
- [ ] DOD-09 ALL canônico com fontes seladas, migrações descartáveis e Playwright mutation contra backend real passa, com admissão CI de todos os novos cenários e sem segredos operacionais.
- [ ] DOD-10 Em plano runtime posterior aprovado: DM real Instagram→LeadsHug→resposta no aparelho e retomada; nova troca nos dois WhatsApps. Teste Meta sintético não substitui essas provas.
- [ ] DOD-11 Revisões independentes, segurança, pcv-1, cutover, TQA, guards de escopo/completion/authority e owners canônicos concluídos, riscos herdados mantidos sob suas restrições.

## Validation Steps
- [ ] VAL-01 RED/GREEN causal para identidade/ownership/rota/nonce/replay/assinatura; falhar contra baseline real antes da implementação e não adaptar asserts para mascarar erro.
- [ ] VAL-02 PostgreSQL descartável: todas as migrations, seed legado com duas modalidades, grupos e proveniência incompleta; snapshots PREPARED/SENDING/aceitos; deploy/checksum e preservação antes/depois, com abortos seguros.
- [ ] VAL-03 OAuth falso no boundary HTTP, multi-BU/tenant/ator, CAS concorrente, code único e troca tardia; assinatura raw/segredo errado, contas com IDs iguais, credencial vencida/rotacionada, eco e replay.
- [ ] VAL-04 Playwright real-backend: conectar/salvar/recarregar, pending/erro/reautorizar, DM e resposta por conta, duas contas Instagram na mesma BU com mesmo peer textual, mudança de BU A→B→A e janela fechada; nenhuma chamada a destinatários reais no browser automatizado.
- [ ] VAL-05 `bash scripts/test-channels-local.sh all` com paridade CI e bundle/backend comprovadamente frescos; testes específicos são diagnóstico, nunca substituto do ALL.
- [ ] VAL-06 Segurança + EPS/FRC/BCI/RLS + audit-protocol-triple-review (Performance, TQA e Cutover), adherence e final review independentes sobre a fonte consolidada.
- [ ] VAL-07 Plano local separado aprovado, sem reset: estado/migrations, imagens/freshness, HTTPS e callback próprios Instagram, prova física Instagram+WhatsApps e retomada preservando outros serviços/volumes.
- [ ] VAL-08 Guards finais e evidência específica por Scope/DoD/Validation; sem nova varredura privada não autorizada, promoção ou produção.

## Completion Evidence Matrix (Required Before Delivery Claim)
Linhas por critério exato; evidência futura permanece planned, sem alegação de implementação. Em critérios de schema/migration, anexar deploy/status e preservação em PostgreSQL descartável. Em fluxos visíveis, anexar Playwright mutation com backend real e freshness; testes unitários não substituem navegação ou prova física. Atualizar caminhos/comandos exatos com receipts reais antes de aceitar cada linha.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCOPE-01 | Scope | SCOPE-01 Consolidar, após aprovação, as propostas DEC-qualified-contact-conversation, DEC-business-resource-provider-identity e DEC-explicit-channel-routing nos owners canônicos, distinguindo arquitetura e entrega. | doc | artifacts/reviews/leadshug-instagram-channel-20261023/evidence/canonical-consolidation-cp1.json | n/a | passed | Canonical target consolidation only; no product/runtime proof |
| SCOPE-02 | Scope | SCOPE-02 Estabelecer contato local e identidade externa qualificada, recursos empresariais e rotas imutáveis; no máximo um recurso empresarial WhatsApp durável por BU (oficial+Evolution no mesmo número comprovado) e múltiplas contas Instagram; preservar IDs de BU/conversa/mensagem e identidades técnicas existentes. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-03 | Scope | SCOPE-03 Migrar consumidores de telefone/tipo para identidade/rota; BFF multicanal, API pública, Typebot e Consultar (lista/drilldown/CSV) preservados no subconjunto WhatsApp, sem Instagram acidental. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-04 | Scope | SCOPE-04 Conexão Instagram Login no app existente com configuração própria do produto, tentativas por ator/sessão/BU, autorização server-side, armazenamento cifrado, reautorização e desconexão locais explícitas. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-05 | Scope | SCOPE-05 Ingresso Instagram autenticado, normalização textual, deduplicação transacional e estado honesto de recebimento; nenhum sucesso inferido de OAuth/challenge sintético. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-06 | Scope | SCOPE-06 Implementação Instagram registrada no Channel; política textual por recurso; envio pelo único OutboundService e aceitação comuns, sem fallback e sem retry externo ambíguo. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-07 | Scope | SCOPE-07 Cadastro de conexões e Atendimento React com origem/conta/contato legíveis, compositor vinculado à rota e proteção contra resposta atrasada/troca de BU. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| SCOPE-08 | Scope | SCOPE-08 Testes comuns e específicos, PostgreSQL, navegador real-backend/freshness, concorrência, isolamento, cutover, provas físicas e fechamento local com todos os gates. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-01 | Definition of Done | DOD-01 Contato local, identidades qualificadas e rota imutável têm unicidade/FKs que comprovam mesma BU, mesmo contato e recurso da conexão; nenhum recurso empresarial em duas BUs através de adapters. Uma BU admite um recurso WhatsApp durável, com seus dois adapters, e várias contas Instagram; outro número WhatsApp falha409sem alterar owner. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-02 | Definition of Done | DOD-02 Migração preserva IDs de conversa/mensagem/BU/ProviderResourceIdentity, autoria, timestamps, unread e conteúdo; proveniência desconhecida conserva sua incerteza. Snapshots/intenções antigos e conclusão local de aceitos têm cutover explícito, sem HTTP repetido. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-03 | Definition of Done | DOD-03 Conexão OAuth Instagram é ADMIN+, idempotente, ligada à sessão e ao recurso verificado; tokens cifrados, expirados/revogados não habilitam envio; reautorizar não muda recurso/owner silenciosamente. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-04 | Definition of Done | DOD-04 Webhook autentica raw body e app correto antes de conteúdo; nova entrada e replay concorrem sem duplicar contato/conversa/mensagem/unread; echo não vira entrada nem autoria humana inventada. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-05 | Definition of Done | DOD-05 DM textual aparece na lista/thread da BU; resposta usa rota exata pelo Channel/OutboundService, respeita política e conserva distinção entre aceitação e entrega. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-06 | Definition of Done | DOD-06 Cadastro/Atendimento apresentam BU, conta/origem e remetente sem tratar ID Instagram como telefone; ações/rascunhos e respostas assíncronas estão vinculados à BU/rota/geração. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-07 | Definition of Done | DOD-07 API v1, Typebot e Consultar/lista/drilldown/CSV WhatsApp mantêm contratos e isolamento; projeções legadas de conexões carregam no máximo os dois bindings WhatsApp compatíveis e não hidratam Instagram; Instagram não entra por telefone ou ativa bot por acidente; autoria/modelos/janela atuais preservados. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-08 | Definition of Done | DOD-08 Harness de dependência abstrata, batch/queries limitadas e invariantes PostgreSQL/concorrência passam; nenhum framework genérico ou fallback escondido. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-09 | Definition of Done | DOD-09 ALL canônico com fontes seladas, migrações descartáveis e Playwright mutation contra backend real passa, com admissão CI de todos os novos cenários e sem segredos operacionais. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-10 | Definition of Done | DOD-10 Em plano runtime posterior aprovado: DM real Instagram→LeadsHug→resposta no aparelho e retomada; nova troca nos dois WhatsApps. Teste Meta sintético não substitui essas provas. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| DOD-11 | Definition of Done | DOD-11 Revisões independentes, segurança, pcv-1, cutover, TQA, guards de escopo/completion/authority e owners canônicos concluídos, riscos herdados mantidos sob suas restrições. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-01 | Validation Steps | VAL-01 RED/GREEN causal para identidade/ownership/rota/nonce/replay/assinatura; falhar contra baseline real antes da implementação e não adaptar asserts para mascarar erro. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-02 | Validation Steps | VAL-02 PostgreSQL descartável: todas as migrations, seed legado com duas modalidades, grupos e proveniência incompleta; snapshots PREPARED/SENDING/aceitos; deploy/checksum e preservação antes/depois, com abortos seguros. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-03 | Validation Steps | VAL-03 OAuth falso no boundary HTTP, multi-BU/tenant/ator, CAS concorrente, code único e troca tardia; assinatura raw/segredo errado, contas com IDs iguais, credencial vencida/rotacionada, eco e replay. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-04 | Validation Steps | VAL-04 Playwright real-backend: conectar/salvar/recarregar, pending/erro/reautorizar, DM e resposta por conta, duas contas Instagram na mesma BU com mesmo peer textual, mudança de BU A→B→A e janela fechada; nenhuma chamada a destinatários reais no browser automatizado. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-05 | Validation Steps | VAL-05 `bash scripts/test-channels-local.sh all` com paridade CI e bundle/backend comprovadamente frescos; testes específicos são diagnóstico, nunca substituto do ALL. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-06 | Validation Steps | VAL-06 Segurança + EPS/FRC/BCI/RLS + audit-protocol-triple-review (Performance, TQA e Cutover), adherence e final review independentes sobre a fonte consolidada. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-07 | Validation Steps | VAL-07 Plano local separado aprovado, sem reset: estado/migrations, imagens/freshness, HTTPS e callback próprios Instagram, prova física Instagram+WhatsApps e retomada preservando outros serviços/volumes. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |
| VAL-08 | Validation Steps | VAL-08 Guards finais e evidência específica por Scope/DoD/Validation; sem nova varredura privada não autorizada, promoção ou produção. | test | CP-specific source-owned tests, migration/flow and safe receipts required before acceptance; pending | local | planned | Not yet proved; no aggregate suite pass or implementation location substitutes for this exact criterion |

## External Dependency Readiness (Required When External Systems Matter)
| Dependency | Why It Matters | Status (`unknown|healthy|degraded|failing|rate-limited|stale`) | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Conta profissional e acesso humano | autorização/prova real | healthy | 2026-10-24, declaração humana | conta adicionada, sem token de teste gerado | não é teste de API/token; geração aguarda plano apropriado |
| Opção Instagram no app existente | reutilização da instalação | healthy | 2026-10-23, declaração humana | usuário consultou o painel | não comprova configuração/Advanced Access |
| Documentação Meta detalhada | OAuth/assinatura/expiração/eligibilidade | healthy | 2026-10-23 | leitura direta pública200 de Business Login, get-started, Messaging e Webhooks; hashes no receipt primário | 429da ferramenta web foi observação anterior, não limite corrente; conta real continua unknown |
| Conta/app/API Instagram efetivos | campos, permissões e entrega | unknown | n/a | nenhuma API/segredo consultados | gates próprios, sem copiar WABA/SDK WhatsApp |
| Runtime/HTTPS local | prova assistida | stale | última prova ST-CON-04 | nenhum probe nesta tarefa | plano separado, não reutilizar túnel antigo por suposição |

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** operational-coder
- **Active technical scope:** nestjs, react, postgresql, prisma, docker
- **Expected supporting profiles:** strategic-cto, operational-devops, assurance-tester-quality, assurance-security-adversarial
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | contrato e código após aprovação | API/Web | CP1 accepted; CP2 sole writer next, authority/routing receipts recorded below |
| operational-coder | strategic-cto | consolidação de domínio/constituição | Foundation | SCOPE-01 consolidated; implementation evidence remains pending |
| operational-coder | operational-devops | rollout local com migrações/HTTPS | runtime aprovado depois | planned |
| operational-coder | assurance-tester-quality | testes e revisões | provas consolidadas | planned |

## Complexity
- **Level (`small|medium|big`):** big
- **Checkpoint policy:** section-by-section: CP1identidade/cutover; CP2OAuth/ingresso; CP3Channel/política; CP4UI/CI; CP5reviews; CP6runtime real/fechamento. Somente CP6 fecha a entrega funcional.
- **Why this level:** alteração cross-module de schema, grants, entrada autenticada, envio irreversível e UI concorrente, mantendo dados e consumidores existentes.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** `foundation_documentation/modules/integrations-and-channels.md`
- **Secondary module docs:** identity-and-tenancy.md, inbox-and-conversations.md, audit-and-history.md no mesmo diretório.
- **Planned decision promotion targets (module sections):** identidade empresarial/credencial/Instagram em Canais; contato/conversa/rota em Inbox; BU/grants em Tenancy; eventos seguros em Audit.
- **Module decision consolidation targets:** os mesmos owners; não promover essas propostas como entregues antes dos gates e provas.

## Decision Pending (Resolve Before Freeze)
- Q-IG-01 resolved-for-review: Instagram Login confirmado pelo operador; protocolo e relações de IDs verificados em fontes primárias200, com contrato explícito abaixo. Valores/concessões/entrega reais permanecem gates de runtime, não suposições de readiness atual.
- Q-IG-02 resolved-for-review: caminhos públicos exatos e ledger de herança/fingerprints preservados; nenhuma inspeção privada ou alteração de produto feita. Revisão/guards de preapproval ainda precisam aceitar a estrutura; conferência integral posterior requer plano próprio.

## Decisions (Resolved Before Freeze)
- D-01 BU operacional conforme escolha humana; Channel abstrato com conexões persistidas, sem telefone sintético.
- D-02 Contato local por BU e identidades qualificadas: WhatsApp pessoa E.164 compartilhado por oficial/não oficial comprovados; grupo namespace separado; Instagram por contexto de app/API+conta empresarial+peer opaco. Sem merge entre plataformas.
- D-03 Identidade empresarial única no LeadsHug atravessa adapters e mantém owner durável; ProviderResourceIdentity preserva IDs técnicos/chaves de mensagens. Conflito não transfere nem vaza.
- D-04 Rota imutável com contato/recurso/BU coerentes e operação v2 capturada com vínculo exato; múltiplas contas Instagram na BU, mas um único recurso empresarial WhatsApp durável com oficial+Evolution comprovados. Sem seleção pelo primeiro tipo, fallback automático ou redirecionamento por nova entrada concorrente.
- D-05 Instagram Login confirmado no app existente; clientId/secret do produto e segredo de webhook por finalidade, sem fallback. OAuth, user_id/IG_ID, assinatura, inscrição e token longo seguem o contrato primário abaixo; configuração real e entrega são verificadas só no plano runtime posterior.
- D-06 DM individual textual recebida primeiro; política própria, sem HUMAN_AGENT, prospecção, mídia/grupos ou templates. Bots Instagram desabilitados explicitamente.
- D-07 Único sender/aceitação e resultados ACCEPTED/BLOCKED/REJECTED/UNKNOWN; preservar idempotência/admissões, autoria, dedup e fences; erro/timeout não autoriza novo POST.
- D-08 Migração versionada preserva IDs/histórico e bytes lógicos de request/fingerprint/snapshots/deadlines v1; a matriz de estados abaixo governa recuperação local sem provider HTTP. Contexto v2 e novas identidades somente para novos writes; não rehash/rewrite v1 nem derivar rota histórica de BU.phone/canal disponível.
- D-09 Consultar/lista/drilldown/CSV conservam o contrato por telefone apenas para identidades WhatsApp qualificadas, com número empresarial do recurso único comprovado; Instagram fica no Atendimento e não nessa consulta. Projeções legadas de conexões de BU retornam no máximo os dois bindings WhatsApp compatíveis; Instagram usa catálogo paginado. API pública v1 conserva semântica WhatsApp: accounts/conversations/messages/claim/release não aceitam nem projetam Instagram como telefone; rotas BFF evoluem com React. Typebot/session/webhooks OUT existentes devem qualificar identidade e manter automação Instagram bloqueada.
- D-10 Test-first e ALL real-backend com fontes frescas; isolamento e capacidade também provados com duas contas Instagram sintéticas na mesma BU. Prova real exige plano posterior e não habilita produção/App Review.

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling (`Preserve|Supersede (Intentional)|Out of Scope`) | Evidence |
| --- | --- | --- | --- |
| identity-and-tenancy#bu-operacional-multicanal | BU operação/grants confirmados; produto ainda WhatsApp | Preserve | decisão DEC-bu-operational-multichannel |
| integrations-and-channels#cadastro-de-números-st-con-01 | recurso/credencial por vínculo e geração, ownership durável de provider | Preserve | contrato ST-CON-01 |
| integrations-and-channels#channel | Channel/Resolver e sender comum | Preserve | channel.ts e registro |
| inbox-and-conversations#iniciar-conversa-e-primeiro-envio--st-con-04 | abertura WhatsApp por telefone, preview/intenção/admissão e snapshots duráveis | Supersede (Intentional) | evoluir endereço/rota e manter o percurso funcional WhatsApp e recuperação |
| inbox-and-conversations#invariants | conversa por BU/contato | Preserve | contato passa a ter ID local/identidade qualificada |
| integrations-and-channels#templates | gestão e envio de templates WhatsApp | Preserve | nenhuma elegibilidade fictícia Instagram |

## Decision Baseline (Frozen Before Implementation)
D-01..D-10 e as cláusulas normativas v1.3 estão FROZEN e APROVADAS para implementação pela resposta humana de2026-10-23. Receipt approval-execution-cp1.json preserva hash do TODO apresentado e baseline f4891ba1. Atualizações de status/ingestão registram a aprovação, sem mudar WHAT; novos achados materiais exigem reconvergência/renovação antes de executar o desvio.

## Architecture Change Governance (Required When This TODO Establishes, Corrects, or Supersedes Architecture)
- **Applicability (`required|not_needed`):** required
- **Why this applies:** aposenta BU=número no comportamento e seleção por enum único; muda identidade/rotas canônicas.
- **Deviation / debt being retired:** telefone/username como identidade de domínio e primeiro canal do tipo como endereço de dispatch.
- **Target steady-state after closeout:** BU operacional, contato/peer/empresa/provider separados, conexão e rota explícitas e um Channel/Outbound/Acceptance.
- **Temporary exceptions allowed:** reader v1 somente para leitura/replay/conclusão local de fatos preexistentes, e colunas legadas read-only para preservar evidência; limites definidos na matriz por estado IG-ARCH-R1-02. Nenhuma escrita canônica v1 ou dispatch nesse reader.
- **Cutover / removal condition:** migrações descartáveis e auditoria provam novos writes exclusivamente v2/identidades/rotas; consumidores deixam de resolver destinatário por contact string ou BU.phone. Reader de fatos v1 fica restrito ao acervo imutável, sem reinserir o caminho antigo de envio.

### Patterns To Enforce
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| DIP/DI e capacidades explícitas, substituição pelo contrato Channel | D-01, D-06, D-07 | consumers/Channel/composição | nenhum cast concreto ou sender paralelo |
| Constraints, ownership durável e rota/contexto imutáveis | D-02, D-03, D-04, IG-ARCH-R1-01 | PostgreSQL/Inbox/Canais | mesma BU, contato e recurso comprovados antes de dispatch |
| Transações curtas, HTTP fora da transação e aceitação comum | D-07, D-08 | OAuth/ingresso/envio | concorrência e recuperação não repetem efeito externo |
| Segredo por finalidade e dados privados somente no adapter/crypto | D-05 | configuração/OAuth/webhook | nenhuma credencial ou destinatário controlado pelo browser |

### Prohibited Anti-Patterns
| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| Contato sem namespace, primeiro canal pronto, rota inferida ou lista truncada | testes de colisão/rota/cardinalidade e revisão | destinatário e recurso errados | none |
| Cast concreto, sender/inbox duplicado ou fallback de segredo | dependency harness e testes negativos | viola contrato comum e isolamento | none |
| Getter que muta provider, bot Instagram implícito ou HTTP de recuperação v1 | contadores HTTP/Typebot e cutover | efeitos não autorizados/duplicação | none |
| Asserts removidos, fonte stale ou dual-write canônico indefinido | ALL/freshness/TQA/cutover | prova fraca ou autoridade concorrente | somente reader v1 limitado, sem novos writes |

### Architecture Protection Harness
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing (`already-enforced|implement-in-this-todo|follow-up-approved|manual-only-with-rationale`) | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | domínio→integração | channel-dependencies.spec.ts e template-management.dependencies.spec.ts | import concreto/cast ou sender duplicado | implement-in-this-todo | DOD-08 / VAL-01,05 |
| test | PostgreSQL | instagram/multichannel e2e e migrations | colisão, ownership interadapter, replay, snapshots | implement-in-this-todo | DOD-01,02 / VAL-02,03 |
| test | UI/rotas | e2e/instagram*.spec.ts com backend real | troca de BU/conta, rascunho e publicação desatualizada | implement-in-this-todo | DOD-06 / VAL-04,05 |
| audit | fonte consolidada | adherence, TQA, Performance e Cutover independentes | atalhos, bridge oculto e prova fraca | implement-in-this-todo | DOD-11 / VAL-06 |

## Architecture Review Gates
- **Architecture decision review:** required
- **Decision review lifecycle:** after diagnosis is closed and before APROVADO
- **Decision review kind:** architecture_opinion
- **Decision review package:** bounded-file-set
- **Decision review status:** no_material_findings
- **Decision review evidence / resolution:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/architecture-r2-result.json; terminal go sobre r1 integrado e duas clarificações r2 revisadas/fechadas, sem autoridade de implementação.
- **Architecture adherence review:** required
- **Adherence review lifecycle:** after implementation and before Completed
- **Adherence review kind:** architecture_adherence
- **Adherence review package:** bounded-file-set
- **Adherence review status:** not_run
- **Adherence review evidence / resolution:** planned para entrega.
- **No-go handling:** findings materiais reconvergem contrato e baseline antes de aprovação/entrega.

## Gate: Review Baseline Freeze
- **Gate decision:** required
- **Trigger stage:** before the first planning-side review or guard run
- **Baseline branch:** main
- **Baseline commit:** f4891ba1bddec62737f5624cac8d4a32224006d7
- **Baseline push reference:** origin/main
- **Gate status:** no_material_findings
- **Findings summary:** baseline v1.3 publicada após integração dos três achados de crítica r1; re-review permitido, sem execução de produto.
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/review-baseline-freeze-r4.json
- **Pre-freeze packet-prep rule:** prepared-pre-freeze não equivale a passed; guards formais só depois do commit/push.

## Gate: Review Scope Drift
- **Gate decision:** required
- **Baseline source:** Review Baseline Freeze -> Baseline commit
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md`
- **Gate status:** no_material_findings
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/review-scope-guard-r4.json; actual go,23seções materiais comparadas e0alteradas contra baseline publicada f4891ba1.

## Questions To Close
- Q-IG-01/02 reconvergidos para review: verificar suficiência na nova rodada. Detalhe físico de classes sem efeito no contrato não vira pergunta de produto.
- O operador já confirmou profissional/acesso/BU conjunta/produto Instagram: manter fatos, sem pedir número/IDs/tokens no chat.

## Assumptions Preview
| Assumption ID | Assumption | Evidence | If False | Confidence (`High|Medium|Low`) | Handling (`Keep as Assumption|Promote to Decision|Block`) |
| --- | --- | --- | --- | --- | --- |
| A-01 | Channel/OutboundService e MessageAcceptanceService são os owners reutilizáveis de envio/aceitação; preservam contexto/admissões | api-app/src/domain/channels/transport/channel.ts; api-app/src/domain/inbox/outbound.service.ts; api-app/src/domain/inbox/message-acceptance.service.ts | reabrir diagnóstico/escopo, não criar outro sender | High | Keep as Assumption |
| A-02 | consumer atual seleciona tipo e contact string; mudança demanda mais que adapter | api-app/src/integrations/channels/prisma-channel-resolver.ts; api-app/prisma/schema.prisma; web-app/src/telas/Numeros.tsx | revisar plano, não declarar banco pronto para Instagram | High | Promote to Decision |
| A-03 | API v1 e Typebot usam endereço WhatsApp e devem ficar fora da ativação Instagram | api-app/src/surfaces/public/conversations.controller.ts; api-app/src/domain/inbox/incoming.service.ts | revisar consumers antes de code | High | Promote to Decision |
| A-04 | Protocolo Instagram deve usar namespace/cliente próprios; valores e concessões reais só serão verificados no plano runtime | api-app/src/surfaces/webhooks/meta.controller.ts é somente WhatsApp; primary-instagram-contract-r1.json e confirmação do título Instagram Login | impedir ativação/prova se recurso/testador não for elegível | High | Promote to Decision |

## Execution Plan (Required Before `APROVADO`)

### Touched Surfaces
Contrato de API proposto e modelo físico a seguir; lista estrita e herança pública explícitas acima. Runners públicos e fixtures são owners da validação descartável. API/Web e Foundation no checkout principal, sem ambiente runtime tocado agora.

### Ordered Steps
1. CP0confirmar a reconvergência Q-IG-01/02; diagnóstico+arquitetura e crítica no-context táticas; Plan Review completo; coherence/scope/authority pre-approval; pedir APROVADO.
2. CP1executor único, baseline público pós-aprovação, REDcausal de identidade/cutover e migrações descartáveis; garantir ownership/dedupe/recuperação sem provider HTTP.
3. CP2OAuth/registro Instagram e ingresso contra HTTP fake nos limites reais; assinatura/nonce/contexto e estados.
4. CP3Channel Instagram e resolução de política/rota; aceitação/admissões comuns, APIv1/Typebot WhatsApp isolados.
5. CP4UI e paridade CI/browser; fontes/bundle/backend selados antes do ALL e das reviews.
6. CP5adherence, segurança, pcv, TQA/cutover e final review; consolidar owners, rever diffs e preparar plano runtime concreto.
7. CP6somente depois de aprovar plano runtime: migração local preservativa, imagens e HTTPS comprovados, configuração Meta pelo operador, DM/reply/retomada e regressão WhatsApp; guards/fechamento local.

### Test Strategy
- **Strategy:** test-first
- **Why:** isolamento e envio irreversível não podem depender de testes espelhando a implementação.
- **Fail-first target(s):** colisões de peer por plataforma/conta; owner do mesmo telefone em adapters/BUs distintos; replay concorrente; nonce de outra sessão; assinatura errada; composer A→B→A; aceito remoto com persistência local interrompida.
- **Pre-APROVADO RED Evidence Capture:** not_needed; feature nova, nenhuma edição de teste antes de aprovação.

### Flow Evidence Planning Matrix
| Criterion / Flow | Why Flow-Impacting | Platform Parity (`android-only|web-only|shared-android-web|divergent-android-web|n/a`) | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Conectar/reautorizar/cancelar e persistir conta | OAuth/config/estado/admin | web-only | Playwright mutation | yes | yes | instagram*.spec.ts com fake no HTTP, PostgreSQL real e reload | n/a |
| DM/Inbox/resposta/rotas e troca de BU | identidade, DTO, unread, dispatch | web-only | Playwright mutation | yes | yes | duas contas e dois tenants sintéticos; backend real | n/a |
| Preservação WhatsApp/modelos/primeiro envio | refatoração de consumers/dados | web-only | Playwright mutation | yes | yes | onboarding/channel/start/template specs existentes preservados | n/a |
| DM real e retomada | provedor externo e aparelho | web-only | prova assistida e runtime aprovado | yes | yes | operador + receipts seguros/freshness, sem conteúdo privado | browser fake não substitui provider |

### Frontend / Consumer Matrix
| Producer / Contract | Consumers | Handling and regression boundary |
| --- | --- | --- |
| BU/conexão/identidades/rotas | BFF/React/cadastro/tenancy | DTOs explícitos e navegação por IDs locais; sem número obrigatório |
| Contact/Conversation/Message | Inbox/paginação/realtime/histórico/initial/admissions | mesmos IDs e owner de aceitação, contexto versionado e rota segura |
| Novos tipos/plataformas | API v1, Typebot/session, webhook OUT, templates | revisar todas as projeções; conservar subconjunto WhatsApp, bloquear Instagram não contratado |
| Credencial/geração/política | resolver/adapter/estado/compositor | não enviar segredo, nem tratar readiness local como concessão permanente |
| OAuth/webhook | gateway/session/CSRF/audit/HTTPclients | callback dedicado com segredo correto, sem query sensível nos logs |

### Local CI-Equivalent Suite Matrix
| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API + PostgreSQL | schema/auth/rotas/consumers | identidade/ownership, OAuth, dedup/echo, snapshots e WhatsApp legado | DB descartável; seed legado+novo; fake na fronteira HTTP; config sintética | `bash scripts/test-channels-local.sh all` | Local-Implemented | planned | ALLstdout/JSONduráveis | unitários não substituem constraints/transações |
| Web + Playwright | UI/projeções/rotas | conexão→reload→DM→resposta, multiaccount/tenant e races | build atual, backend real, mesmo DB/porta de CI, bundle provado | `bash scripts/test-channels-local.sh all` | Local-Implemented | planned | traces+report+fontes+fingerprints | sem stub de regra de domínio |
| Root CI/paridade | runners/compose/admissão | novos specs efetivamente executados com corpo/asserts | inventário público; nenhum .env real; admissões explícitas | `python3 scripts/check-channels-ci-parity.py --self-test` e ALL | Local-Implemented | planned | relatório de admissão/freshness | caminhos e ledger públicos explícitos |

### Runtime / Rollout Notes
Local primeiro, projeto runtime existente `leadshug_channels_local`; validação descartável `leadshug_channels_validation`, conforme runner. NÃO executar runtime nesta tarefa. Ativação, acesso opaco ao .env.testing, migração em DB real e callbacks/túneis dependem de plano próprio posterior. Plano deverá provar preservação de peers/volumes, snapshots/admissões pendentes, versões/checksums e abort-before-write em conflito. Lock timeout5s/statement60s nos comandos de migração; nenhum reset. Aprovação de código não publica app Meta nem autoriza produção.

## Plan Review Gate
**Status:** arquitetura r2go, findings r1/r2 integrados; crítica r2 terminal go após as três correções r1; sete lentes revisadas, sem achado material pendente. Evidência critique-r2-result.json; isso não prova implementação.

### Review Sections
- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards
| Issue ID / evidence / why now | Option A — recommended | Option B | Option C — do nothing | Recommendation |
| --- | --- | --- | --- | --- |
| IG-P01 high — schema.prisma:93/127/175/389; mesma BU terá peers não telefônicos | identidade local/qualificada, recurso empresarial+provider e rota. Effort high; risk medium; blast cross-module; manutenção medium; performance indexed; elegância/solidez improve | só adicionar enum/guardar IGSID em contact. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | manter WhatsApp-only. Effort none; risk low; blast local; manutenção neutral; performance/elegância/solidez neutral; não entrega objetivo | A, com cutover preservativo |
| IG-P02 high — prisma-channel-resolver.ts:selectCandidate; tipo não identifica conta | rota/vínculo capturados e revalidados. Effort medium; risk medium; blast cross-module; manutenção low; performance bounded; elegância/solidez improve | primeiro canal pronto/fallback. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | não habilitar Instagram. Effort none; risk low; blast local; manutenção/performance/elegância/solidez neutral | A, sem roteamento silencioso |
| IG-P03 high — meta.controller.ts só WhatsApp; Q-IG-01 agora documentado em fonte primária | protocolo/segredo/config Instagram próprios verificados; nonce/session/CAS. Effort medium; risk medium; blast module; manutenção medium; performance bounded; elegância/solidez improve | reutilizar token/WABA/segredo sem prova. Effort low; risk high; blast cross-module; manutenção high; performance unknown; elegância/solidez regress | esperar evidência antes de code. Effort low; risk low; blast local; manutenção neutral; performance/elegância/solidez neutral | A após evidência, C enquanto pendente |
| IG-P04 high — intents/admissions e receipts de ST-CON-04 persistidos | cutover versionado para dados+snapshots, reconstrução só comprovada, accepted local-only. Effort high; risk medium; blast cross-module; manutenção medium; performance bounded; elegância/solidez improve | recriar DB/IDs. Effort low; risk high; blast cross-module; manutenção low; performance neutral; elegância/solidez regress | não migrar. Effort none; risk low; blast local; manutenção/performance/elegância/solidez neutral; não entrega objetivo | A, sem reset/route guess |

### Failure Modes & Edge Cases
Mesmo ID em plataformas/contas; username mutável; propriedade conflitante entre adapters; OAuth popup cancelado/code consumido/sem sessão; token vencido/revogado; bad signature e payload oversized; eventos fora de ordem, duplicados e echo-first; timeout remoto; DB após ACK; rascunho antigo/A→B→A; janela fechada; múltiplas rotas; legacy sem proveniência; bot e APIv1 tratando IGSID como telefone; callbacks WhatsApp alterados indevidamente.

### Residual Unknowns / Risks
Q-IG-01/02 estão reconvergidos para review; arquitetura/crítica e guards ainda impedem pedir APROVADO. Não há medidas de desempenho ou prova de permissão real nesta etapa. SEC-R6-04, OPS-R4-01 e TQA-ST05-03 do baseline permanecem sob a coorte privada e restrições já registradas; este TODO não as resolve nem amplia público/ambiente.

## Additional Architectural Opinions
- **Needed:** yes
- **Why ambiguity remains:** modelo físico, cutover e protocolo operacional precisam de challenge no pacote completo; opinião estratégica prévia não revisou este TODO.
- **Opinion count:** 2 para este TODO; r1changes_required integrado e r2go terminal
- **Package mode:** bounded-file-set
- **Internal reviewer mandate:** required; fresh internal no-context reviewer, sem implementação; esperar estado terminal sem interromper/reempacotar por demora.
- **Required lenses:** correctness, performance, elegance, structural-soundness, operational-fit.

## Audit Trigger Matrix
- **Canonical method:** wf-docker-audit-escalation-method
- **Latest TEACH evidence / artifact:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/audit-floor-r2.json, actual go; todas as lanes abaixo preservam o piso required.

| Trigger | Value | Notes |
| --- | --- | --- |
| complexity | big | jornada cross-module |
| blast_radius | cross-stack | Nest/React/DB |
| behavioral_change_or_bugfix | yes | canal novo |
| changes_public_contract | yes | BFF/schema/consumers |
| touches_auth_or_tenant | yes | ownership/OAuth/grants |
| touches_runtime_or_infra | yes | novo callback/freshness |
| touches_tests | yes | causal/integração/browser |
| critical_user_journey | yes | atendimento/envio |
| release_or_promotion_critical | no | local/coorte privada |
| high_severity_plan_review_issue | yes | riscos acima |
| explicit_three_lane_request | yes | Performance+TQA+Cutover após implementação |

## Independent No-Context Critique Gate
- **Critique decision:** required
- **Why this decision:** big/cross-stack/schema/auth; confirmar piso após freeze.
- **Package mode:** bounded-file-set
- **Package minimum contents:** baseline publicada, escopo candidato completo, decisões, assumptions, plano/issue cards, fontes públicas exatas, dívida/limitações herdadas.
- **Critique isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; não implementing agent; wait status-based, external provider não satisfaz gate.
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review, posterior à implementação e adicional à crítica.
- **Critique status:** no_material_findings
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/critique-r2-result.json; terminal go, três achados r1 fechados no contrato v1.3 publicado.

## Rules Acknowledgement / Ingestion
Ingestão vinculante recarregada após APROVADO em2026-10-23: fontes abaixo e workflow de execução/orquestração; executor recarrega o subconjunto do checkpoint antes de editar. Não há waiver.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| delphi-ai/main_instructions.md | autoridade | escopo/execução separadas | code antes de aprovação | executor único |
| delphi-ai/workflows/docker/todo-approval-gates-method.md | gates | freeze/reviews/preflight | aprovação implícita | GO antes de code |
| delphi-ai/workflows/docker/effort-selection-method.md | routing | lanes e provas | modelo inventado | guard por lane |
| delphi-ai/workflows/nestjs/change-application-boundary-method.md | backend | contrato/domain/adapter | regra no controller | integração real |
| delphi-ai/workflows/react/change-ui-boundary-method.md | interface | estado/contexto/freshness | resposta atrasada | Playwright |
| delphi-ai/rules/stacks/prisma/prisma-schema-migration-always-on.md | schema | migrations versionadas | reset | deploy descartável |
| delphi-ai/rules/stacks/postgresql/postgresql-data-integrity-always-on.md | dados/concurrency | constraints/locks | HTTP em tx | barriers reais |
| foundation_documentation/project_constitution.md | multitenancy | BU/grants | scope por browser | isolamento |
| foundation_documentation/policies/scope_subscope_governance.md | superfícies | owner/route | superfície informal | contrato scoped |
| delphi-ai/workflows/docker/performance-concurrency-validation-method.md | pcv-1 | provas/thresholds | boolean pass | lanes antes da entrega |

## Agent Routing Preflight
- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-6-luna
- **Selected effort:** medium
- **Proof mode:** declared
- **Exception reason:** n/a
- **Routing evidence:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/routing-execution-cp1.json; actual go pós-aprovação, gpt-6-luna medium, um writer no checkout principal.
- **Execution topology:** primary-checkout-single-writer
- **Subagent / delegation authorization:** workflows de executor/review; um writer de produto serializado.
- **Git isolation authorization:** not-authorized
- **Worktree authorization:** not-authorized
- **Worktree authorization reference:** n/a
- **Writer scheduling policy:** single-writer-serialized
- **Guard outcome:** go
- **Waiver / exception reference:** n/a

## Decision Adherence Validation
D-01..D-10 terão evidência específica após execução; todas planned, nenhuma alegação Adherent de código ainda.

## Module Decision Consistency Validation (1-1 Mandatory Before Delivery)
Uma linha por decisão da baseline dos módulos antes da entrega; Preserved/Superseded(Approved) com prova. Regression ou Exception não resolvidas bloqueiam fechamento.

## Pipeline/Copilot P1/P2 Preflight
Planned sobre fonte/evidências finais; unresolved P1/P2 bloqueia entrega.

## Rule-Spirit Anti-Pattern Hunt
Planned: telefone sintético, segredo global, provider branch nos consumers, fallback de rota, mocks de regra de negócio, asserts enfraquecidos e replay HTTP disfarçado.

## Promotion Finding Routing Ledger
Historical planning observation retained: IG-REV-01..04, strategic source, high/medium/low, release-blocker; ownership/dedup/cutover/limits were integrated into the approved plan, with product verification still open. These observations are not a waiver or proof of product repair. The concrete CP1 findings below all remain in this approved delivery.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP1-R1-01 | high | release-blocker | fix in this TODO | immutable qualified peer is SCOPE-02/DOD-01 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-02 | high | release-blocker | fix in this TODO | current provider attachment equality is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; final persisted association defect repaired; actual official confirmation proved |
| IG-CP1-R1-03 | high | release-blocker | fix in this TODO | durable cross-adapter resource ownership is SCOPE-02/DOD-01 | closed by r5 | adherence-cp1-r5-result.json; exact current quarantine recovery after actual prior receipt |
| IG-CP1-R1-04 | high | release-blocker | fix in this TODO | qualified contact reuse is SCOPE-02,03 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-05 | medium | release-blocker | fix in this TODO | retained ownership/cardinality is SCOPE-02/DOD-01 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-06 | medium | release-blocker | fix in this TODO | safe canonical migration is DOD-02/VAL-02 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R1-07 | medium | release-blocker | fix in this TODO | preserved regression tests are SCOPE-08/DOD-09 | closed by r5 | cp1-frozen-full-api-green-r5.json; complete379unit/483e2e GREEN on matching37sources |
| IG-CP1-R1-08 | medium | release-blocker | fix in this TODO | required historical cohort is DOD-02/VAL-02 | closed by r2 | adherence-cp1-r2-result.json; source/proof repair reviewed; no delivery acceptance |
| IG-CP1-R2-01 | high | release-blocker | fix in this TODO | one coherent WA business scope is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; WA business scope BU agrees with CHECK/FK and actual positive route |
| IG-CP1-R2-02 | high | release-blocker | fix in this TODO | honest unverified renewal staging is SCOPE-02/DOD-01 | closed by r3 | adherence-cp1-r3-result.json; original reservation/proof defect repaired; distinct pending lifecycle findings remain below |
| IG-CP1-R3-01 | high | release-blocker | fix in this TODO | single-create/read-before-retry after pending renewal is SCOPE-02/08 | closed by r5 | adherence-cp1-r5-result.json; single create and read-before-retry retained |
| IG-CP1-R3-02 | high | release-blocker | fix in this TODO | managed cleanup ownership survives staged unlink under SCOPE-02/08 | closed by r5 | adherence-cp1-r5-result.json; current staged unlink and stale snapshot fence repaired |
| IG-CP1-R3-03 | medium | release-blocker | fix in this TODO | durable quarantine and later correct-proof recovery preserve existing channel contract | closed by r5 | adherence-cp1-r5-result.json; wrong-number quarantine and correct-proof recovery retained |
| IG-CP1-R3-04 | low | release-blocker | fix in this TODO | required ownership concurrency proof cannot assume winner scheduling; fix assertions in this TODO | closed by r5 | adherence-cp1-r5-result.json; actual-winner concurrency assertion retained |
| IG-CP1-ROOT-01 | high | release-blocker | fix in this TODO | pending current ingress remains retryable without content/trust before proof | closed by r5 | adherence-cp1-r5-result.json; metadata-only staged retry and accepted-key proof retained |
| IG-CP1-R4-01 | high | release-blocker | repeat affected proof in this TODO | four mutations violated the explicit r4 freeze; preserve evidence and validate current bytes anew | closed by r5 | adherence-cp1-r5-result.json; cp1-frozen-full-api-green-r5.json; new stable proof replaces invalidated acceptance |
| IG-CP1-R5-01 | medium | release-blocker | bounded companion in this TODO; protected path validation required | current staged cleanup guarantee depends on a truthful absence observation; inherited adapter weakness is not a new Instagram regression | closed by r8 complete review/current full API | cp1-r8-acceptance.json; adherence-cp1-r8-result.json; cp1-observation-r8-full-api-green.json |
| IG-EVOCOMP-01 | medium | release-blocker | fix admitted caller lifecycle in this TODO | conclusive cleanup must recover same reserved operation and permit one create, without widening protected paths | closed by r3/current full API; protected parser remains R5-01 | evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json |
| IG-EVOCOMP-02 | medium | release-blocker | strengthen proposed tests before source admission | independent malformed name/state and null projection branches need concrete proof plan | proposal resolved r2; implementation not admitted | evolution-observation-companion-critique-r2-result.json |
| IG-EVOCOMP-03 | low | release-blocker | correct proposal wording before validation | exact subject and absence contract must be clear to approving user; small same-artifact correction | proposal resolved r2; implementation not admitted | evolution-observation-companion-critique-r2-result.json |
| IG-EVOCOMP-R2-01 | medium | release-blocker | fence late failure mutation in same admitted caller/test paths | same-attempt recovery must retain later holder facts after lease takeover; inherited catch is not a new adapter regression | closed by r3/current full API | evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json |
| IG-CP1-ROOT-R7-01 | medium | release-blocker | revalidate authorization before provider-error fact mutation in same admitted paths | live DB lease does not replace post-call session/grant revalidation; same existing lifecycle contract, no new middleware scope | closed by r3/current full API | evolution-observation-companion-critique-r3-result.json; cp1-caller-r7-full-api-green.json |

| IG-CP2-ROOT-01 | medium | release-blocker | fix in this TODO | accurate persisted budget backoff under SCOPE-04/VAL-03 | closed original defect by CP2 r1; persisted actor/BU backoff assertions; no pre-fix causal RED inferred | adherence-cp2-r1-result.json; prior evidence retained |
| IG-CP2-ROOT-02 | high | release-blocker | fix in this TODO | current post-HTTP lease fence under SCOPE-04/VAL-03 | open; source16 clocks proved; residual finalmapping and mapped preHTTP attemptTTL | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-CP2-ROOT-03 | medium | release-blocker | fix in this TODO | actual credential acquisition/expiry under DOD-03/VAL-03 | closed original defect by CP2 r1; acquisition before delayed profile; no pre-fix causal RED inferred | adherence-cp2-r1-result.json; prior evidence retained |
| IG-CP2-ROOT-04 | high | release-blocker | fix in this TODO | Existing UUID key and durable replay/conflict contract also governs OAuth confirmation | closed original key/recovery defect; strict20 and actualnewversion/currentexpiry historical replay passed | adherence-cp2-r4-result.json; cp2-r3-source-validation-16-result.json; cp2-api-full-r4-result.json |
| IG-CP2-ROOT-05 | medium | release-blocker | verify and fix in this TODO | Successful connected-channel reauthorization must preserve resource/receipt and known subscription | closed original defect by CP2 r1; connected reauthorization preserves receipt/messages without another POST | adherence-cp2-r1-result.json; prior evidence retained |
| IG-CP2-ROOT-06 | high | release-blocker | fix in this TODO | Eligible authenticated current-resource ingress must provide independent receipt after ambiguous dispatch | closed original defect by CP2 r1; signed ingress during held POST and after uncertainty | adherence-cp2-r1-result.json; prior evidence retained |
| IG-SUBPROTO-01 | high | release-blocker | resolve primary protocol in this TODO | Own-subscription GET envelope, ID subject and completeness remain unproved; do not infer unsupported from omission | open; primary prerequisite | subscription-protocol-opinion-result.json |
| IG-SUBPROTO-02 | medium | release-blocker | preserve UNKNOWN fence in admitted code | An unexplained empty or mismatched-ID observation cannot permit a second POST after uncertainty | closed original defect by CP2 r1; UNKNOWN preserves mutation fence; concurrent lifecycle stays SUBREC-02 | adherence-cp2-r1-result.json; prior evidence retained |
| IG-SUBPROTO-03 | medium | release-blocker | retain typed identity purposes in this TODO | No speculative parent-app configuration or guessed ID comparison; same approved OAuth path | closed original defect by CP2 r1; distinct identity purposes; no speculative parent-app configuration | adherence-cp2-r1-result.json; prior evidence retained |
| IG-SUBREC-02 | high | release-blocker | fix in this TODO; related to IG-SUBPROTO-02 | Resource-lifecycle dispatch fence survives new attempt, reauthorization, lease expiry and crash | open; source16 settledcleanup/GETtuple proved; acquisition postCOMMIT cleanup residual | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json |
| IG-SUBREC-03 | medium | release-blocker | retain with IG-SUBPROTO-01 in this TODO | UNKNOWN is valid, but own-account observation remains mandatory and unaccepted | open; primary protocol | subscription-recovery-concretization-result.json |
| IG-SUBREC-04 | medium | by-design/no-action | proposed investigation remains unexecuted | Bounded empirical observations cannot establish universal completeness or authorize repeated mutation | documented; no execution authority inferred | subscription-recovery-concretization-result.json |

| IG-CP2-R1-01 | high | release-blocker | fix in this TODO | Confirmation can promote an expired candidate or overwrite cancellation | closed original TTL/cancel/CAS defect; final clocks remain ROOT02 | adherence-cp2-r3-result.json; qualified stable11..13 |
| IG-CP2-R1-02 | medium | release-blocker | fix in this TODO | Instagram authorization admission diverges from current BU scope and error ordering | closed original authorization order/activeBU/array defect | adherence-cp2-r3-result.json; qualified stable11..13 |
| IG-CP2-R1-03 | high | release-blocker | fix in this TODO | The Instagram HTTP boundary follows redirects beyond its validated endpoints | closed original redirect defect; native fetch boundary proof | adherence-cp2-r3-result.json; qualified stable11..13 |
| IG-CP2-R1-04 | medium | release-blocker | fix in this TODO | Failed OAuth callbacks retain sensitive query URLs without the required response protections | open; exact user-admitted v2 source applied12; infrastructure/fullAPI/gateway/browser proof NOTRUN | adherence-cp2-r3-result.json; oauth-callback-session-companion-ready-v2.json |
| IG-CP2-R1-05 | medium | release-blocker | fix in this TODO | Whole-batch preflight does not validate the supported message structure | closed original preflight defect and exactaccount fixture; currentfullAPI passed | adherence-cp2-r4-result.json; cp2-api-full-r4-result.json |
| IG-CP2-R1-06 | medium | release-blocker | fix in this TODO | The reported sixteen-obligation map exceeds the behavioral proof actually present | open; exact finalmapping/preHTTP TTL/postCOMMIT proof plus primary/precontroller; replay/config/secondNest now supported | adherence-cp2-r4-result.json; cp2-r4-root-adjudication.json; cp2-api-full-r4-result.json |
| IG-CP2-ROOT-07 | medium | release-blocker | fix in this TODO | Five Instagram write routes need safe catalog/audit classification | closed original audit/catalog defect; complete canonical coverage passed | adherence-cp2-r3-result.json; cp2-api-full-r3-result.json |

| IG-OAUTH-SESSCOMP-01 | medium | release-blocker | revise companion in same TODO | Unexpected precontroller callback failure also needs clean generic failure redirect | proposal resolved by terminal r2; source unadmitted, implementation proof pending | oauth-callback-session-companion-critique-result.json |

| IG-CP2-ROOT-08 | medium | release-blocker | reprove stable candidate in this TODO | Executor edited authorization source during GREEN05, invalidating current-source proof | closed original source-drift proof defect by stable16/fullAPI/currentcompleteR4; GREEN05 remains invalid | cp2-r4-root-adjudication.json; cp2-api-full-r4-result.json; adherence-cp2-r4-collection.json |

| IG-CP2-ROOT-09 | medium | release-blocker | validate actual current candidate in this TODO | Executor consulted non-authoritative backup instructions and misread empty exact-path Git diff; root corrected authority and positive hash evidence | closed original backup-input/emptydiff inference by currentprincipal/publicproof; filename-only metadata note retained | cp2-r4-root-adjudication.json; adherence-cp2-r4-collection.json; cp2-api-full-r4-result.json |

| IG-CP2-ROOT-15 | medium | release-blocker | fix test fixture in this TODO | Exact account selection is required under multiaccount CP2 proof | closed exactaccount fixture; selected16 andfull549 passed | cp2-api-full-r4-result.json; adherence-cp2-r4-result.json |

| IG-CP3-ROOT-01 | high | release-blocker | fix in this TODO | Exact selection and bounded WA discovery are SCOPE-03/06 and DOD-07/08 | closed original defect by API45/adherence46; newA46 remains open | cp3-api45-root-reconciliation.json; cp3-adherence46-root-adjudication.json |
| IG-CP3-ROOT-02 | high | release-blocker | fix in this TODO | Strict V2, historical accepted-fact tuple and no redispatch are approved scope | closed original defect by API45/adherence46; newA46 remains open | cp3-api45-root-reconciliation.json; cp3-adherence46-root-adjudication.json |
| IG-CP3-ROOT-03 | high | release-blocker | fix in this TODO | All declared connections/UI/projection/realtime/browser consumers remain required | open; CP4 integral and later gates required | cp3-adherence35-root-adjudication.json; CP4 qualified preparation receipts |
| IG-CP3-ROOT-04 | medium | release-blocker | fix in this TODO | Writer-path discipline and preservation remain authoritative | corrected qualified; no dynamic proof invalidation inferred | cp3-source03-boundary-correction04.json |
| IG-CP3-ROOT-05 | high | release-blocker | fix in this TODO | Actual verified WA ingress must establish its qualified reply route | closed original defect by API35 and complete complementary adherence35 | cp3-api35-root-reconciliation.json; cp3-adherence35-root-adjudication.json |
| IG-CP3-ROOT-06 | high | release-blocker | fix in this TODO | Canonical peer identity governs acceptance while preserving legacy presentation | closed original defect by API35 and complete complementary adherence35 | cp3-api35-root-reconciliation.json; cp3-adherence35-root-adjudication.json |
| IG-CP3-ROOT-07 | high | release-blocker | fix in this TODO | Provider identity, qualified peer and conversation lock order is shared | closed original defect by API45/adherence46; newA46 remains open | cp3-api45-root-reconciliation.json; cp3-adherence46-root-adjudication.json |
| IG-CP3-ROOT-08 | high | release-blocker | fix in this TODO | Accepted and uncertain facts retain captured qualified Instagram address | closed original defect by native API35 and complete complementary adherence35 | cp3-api35-root-reconciliation.json; cp3-adherence35-root-adjudication.json |
| IG-CP3-A-01 | high | release-blocker | fix in this TODO | Current human actor/session/grant fence is DOD-03 and VAL-03 | closed original defect by API45/adherence46; newA46 remains open | cp3-api45-root-reconciliation.json; cp3-adherence46-root-adjudication.json |
| IG-CP3-A-02 | medium | release-blocker | fix in this TODO | Dependency harness must catch concrete Instagram coupling and initial consumer | open; partial fix proved45, Official window/namespace policy guard residual46 | cp3-adherence46b-raw.json; cp3-adherence46-root-adjudication.json |
| IG-CP3-B35-05 | medium | release-blocker | fix in this TODO | Bound internal CSV hydration preserving full public output and filters | closed original defect by API45/adherence46; newA46 remains open | cp3-api45-root-reconciliation.json; cp3-adherence46-root-adjudication.json |
| IG-CP3-A46-01 | high | release-blocker | fix in this TODO | coherent provider/currentactor final observation is IG-ARCH-R1-01/DOD-03 | open; nativecausal proof then faithfulHOW repair | cp3-adherence46a-raw.json; cp3-adherence46-root-adjudication.json |
| IG-CP3-B46-01 | medium | release-blocker | fix in this TODO | options and dispatch must share recipient-qualified initial eligibility | open; preserve12cohort/WApositive and addIGnegative | cp3-adherence46b-raw.json; cp3-adherence46-root-adjudication.json |

## TODO Closeout Disposition
- **Disposition:** blocked
- **Disposition reason:** implementação aprovada em curso; CP1 aceito, findings CP2 e demais checkpoints/gates abertos, sem entrega parcial aceita.
- **Post-commit/push status:** pending
- **Next path/status action:** manter ativo em implementation; corrigir CP2 e continuar CP3..CP6 sob a aprovação e os limites existentes.

## Security Risk Assessment
- **Risk level:** high
- **Why this risk level:** OAuth/segredos/ownership multi-tenant, webhook público e envio irreversível.
- **Attack surface in scope:** session/state/CSRF, assinatura raw, SSRF/URLsdecontinuação, token storage, callbacks/logs e alcance cross-BU.
- **Attack simulation decision:** required
- **Review evidence:** planned, nenhum ataque executado em runtime.
- **Residual security risk:** dívidas herdadas mantidas na coorte OWNER privada; nenhum acesso público novo sem tratamento.

## Performance & Concurrency Risk Assessment
- **Policy schema version:** pcv-1
- **Global sensitivity level:** high
- **Why this level:** chaves de lookup/rota/listagem, OAuth e mensagens concorrentes, estado React.
- **Current delivery stage at review time:** Pending

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPS | endpoint-performance-scrutiny | required | high | EPS-QUERY-SHAPE-CHANGED | before_local_implemented | EPS-E2 | pending | none | U-QUERY-PATH-UNKNOWN |
| FRC | frontend-race-condition-validation | required | high | FRC-STALE-RESPONSE | before_local_implemented | FRC-E3 | pending | none | U-ASYNC-SURFACE-UNKNOWN |
| BCI | backend-concurrency-idempotency-validation | required | high | BCI-JOB-WEBHOOK-API-OVERLAP | before_local_implemented | BCI-E3 | pending | none | U-WRITE-OVERLAP-UNKNOWN |
| RLS | runtime-load-stress-validation | required | high | RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED | before_local_implemented | RLS-E2 | pending | none | U-RUNTIME-PRESSURE-UNKNOWN |

Thresholds/amostragem por lane estão congelados na integração IG-ARCH-R1-04 abaixo; nenhum budget de fornecedor é benchmark do produto.

## Verification Debt Assessment
- **Audit outcome:** high
- **Why this outcome:** feature não implementada, ainda faltam provas de todos os critérios.
- **Inline code TODO debt:** none introduced
- **Evidence / audit artifact:** planned antes de Completed.
- **Accepted residual debt:** somente restrições herdadas declaradas; nenhuma waiver nova.

## Independent Test Quality Audit Gate
- **Audit decision:** required
- **Why this decision:** schema/auth/sharedcontract/criticaljourney e testes novos.
- **Trigger signals in scope:** changed test logic, behavior-defining change, architectural change, shared contract/api/schema, compatibility, critical-user-journey.
- **Required evidence matrix (when architectural):** unit, integration PostgreSQL, web real-backend.
- **Package mode:** bounded-file-set
- **Canonical method:** wf-docker-independent-test-quality-audit-method
- **Audit isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; não implementing agent, sem deadline artificial/review externo.
- **Audit status:** not_run
- **Evidence / reference:** after implementation, full applicable audit, não questionário abreviado.

## Independent No-Context Final Review Gate
- **Final review decision:** required
- **Why this decision:** big/cross-module/schema/auth/runtime.
- **Impact signals in scope:** cross-module blast radius, public contract/schema/api, auth/payment, runtime/queue/realtime/ingress, intentional module supersede, high-severity issue card.
- **Package mode:** bounded-file-set
- **Review isolation mode:** fresh internal no-context reviewer
- **Internal reviewer mandate:** required; esperar estado terminal.
- **Canonical multi-lane audit protocol (when required):** audit-protocol-triple-review
- **Final review status:** not_run
- **Evidence / reference:** after all applicable implementation/proof/adherence/test-audit gates.

## Independent Cutover Integrity Audit Gate
- **Cutover audit decision:** required
- **Why this decision:** migração de contato/rotas e contextos persistidos.
- **Cutover signals in scope:** canonical cutover, compatibility exception.
- **Package mode:** bounded-file-set
- **Canonical multi-lane audit protocol (when used):** audit-protocol-triple-review
- **Cutover audit status:** not_run
- **Evidence / reference:** planned, receita legada versionada deve ser contrato explícito e não shadow canonical path.

## Delivery Confidence Gate
Production-Ready fora de escopo. Local exige todos os critérios, pcv-1 e provas reais do contrato; não declarar concluído com adapter/fake apenas.

## Module Consolidation Gate
Após aprovação, promover decisões aceitas nos owners; após evidência, atualizar estado entregue e cruzar links. Não reescrever entregas históricas ST-CON para parecer novas.

## Commands (Run Locally)
Somente análise pública e guards documentais antes da aprovação. Depois: runner canônico e deploy descartável; runtime local só após plano específico. Nenhum comando com token ou env real aparece neste TODO.

## Gate: Assumption Code Coherence
- **Gate decision:** required
- **Gate status:** no_material_findings
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md`
- **Evidence / reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/assumption-code-manual-r4.json; leitura delimitada confirmou A-01..04, sem achado material. Guard determinístico artifacts/reviews/leadshug-instagram-channel-20261023/evidence/assumption-code-guard-r4.json retornou actual go; elegibilidade real segue runtime.

## Approval
- **Approval status:** APROVADO
- **Approved by:** usuário desta conversa, em2026-10-23, resposta explícita `APROVADO` ao contrato Instagram v1.3.
- **Approval reference:** artifacts/reviews/leadshug-instagram-channel-20261023/evidence/approval-execution-cp1.json; hash do pacote apresentado e baseline revisada preservados nesse receipt.
- **Approval scope:** SCOPE-01..08, D-01..10, DOD/VAL e cláusulas normativas v1.3; implementação API/Web, documentação e validação descartável sintética exclusivamente nos caminhos admitidos. Não autoriza arquivos privados/dados reais, ativação local, Meta/envios externos, Git de produto, gitlinks, worktrees/cópias, produção ou App Review; plano runtime próprio continua obrigatório.
- **Renewed approval trigger:** mudança material de WHAT/decisões/validação/escopo ou qualquer caminho não admitido.


## Proposed Data and API Contract — candidate v1.0

Esta seção e as cláusulas normativas seguintes tornam o candidato v1.1 revisável; Q-IG-01 tem evidência primária e confirmação humana do caminho de login, sem prova de concessão real. Os limites abaixo são políticas propostas do LeadsHug, não quotas ou garantias da Meta.

### Modelo físico candidato

| Owner | Modelo / chave | Preservação e transição |
| --- | --- | --- |
| Inbox | Contact: UUID local e buId; ContactIdentity: buId,platform,namespace,scopeReference,externalPeerId únicos | criar um contato por identidade inédita; WhatsApp pessoa/grupo separados; Instagram scope inclui contexto app/API e identidade estável da conta. FKscoped impede ligação cross-BU; não usar username como unique. |
| Canais | BusinessChannelIdentity: plataforma+namespace+externalResourceId único no LeadsHug, owner buId imutável | WhatsApp usa número próprio comprovado comum aos adapters; Instagram recurso devolvido pela autorização verificada no namespace correto. Conflicts abort antes de promover credencial; ownership não liberado por desconexão. |
| Canais | ProviderResourceIdentity existente com associação opcional/comprovada a BusinessChannelIdentity | preservar ID/provider/externalResourceId/owner/tombstone e unique de Message; não reinterpretar instância Evolution como phoneNumberId ou colapsar dedup. Identidade desconhecida não ganha mapeamento por conveniência. |
| Canais | BuChannel existente, ID mantido, tipo/adapter e vínculo ao recurso empresarial; remover unique(buId,type) como seletor de conta | restrição da conexão ativa por recurso/adapter; OAuth/credencial por vínculo/geração. APIs antigas por tipo só podem operar quando houver exatamente um vínculo compatível; ambiguidade409, nunca primeiro. Número próprio fica no recurso, BU.phone deixa de governar validação/dispatch. |
| Inbox | Conversation.contactId local obrigatório após backfill; unique(buId,contactId), mesmos IDs de conversa | Conversation.contact antigo fica somente como evidência legada/read-only, nullable para Instagram; não é fonte canônica nem endereço de dispatch após cutover. Uma identidade WhatsApp legada válida mapeia exatamente à conversa existente; incerteza/conflito bloqueia adoção e recebe disposição explícita. |
| Inbox/Canais | ConversationRoute: conversationId,businessIdentityId,contactIdentityId com unicidade/FKs da mesma BU | uma rota pode ter adapters WhatsApp diferentes comprovados; resposta captura também channelId concreto e generation. Peers Instagram de duas contas não são unidos. Não há operação de merge nesta entrega. |
| Inbox | Message e admissões/intents conservam IDs/proveniência e recebem referência opcional/versionada de rota | reader v1 apenas para recuperar/exibir receipts antigos com associação comprovada; novos writes somente contrato v2. Nenhum HTTP para reconstruir rota, nenhum side effect de backfill. |
| Canais | InstagramAuthorizationAttempt: UUID, BU, ator/sessionHash, nonceHash, expiry, state, generation e token candidato cifrado | nova tentativa atômica/idempotente, state10min, CAS antes de code exchange; code nunca persiste. Token candidato não sobrescreve ativo até identidade/ownership verificados. |

Compatibilidade admitida é delimitada: receipt reader v1 conserva fatos antigos e pode concluir localmente aceitos já conhecidos; não dispara novo envio e não sustenta dual-write. Colunas legadas só para preservação de evidência e compatibilidade explicitamente testada; consultas/novas gravações usam o modelo canônico. Adoção local ocorre com API quiescente sob plano posterior; inventário seguro deve incluir intenções ativas, conflitos de owners e referências sem prova. Conflito ou versão desconhecida aborta antes de escrita destrutiva. Nada é resetado, transferido ou unido automaticamente.

### Auth, projeções e endpoints candidatos

Todos os endpoints BFF resolvem tenant pela sessão e BU pelos grants atuais; ADMIN+ administra conexões; ATENDENTE+ lê/atende. POST exige anti-CSRF. Idempotency-Key UUID e replay/conflito duráveis são exigidos nas criações/confirmações OAuth e nos primeiros envios já contratados; resposta ordinária preserva as admissões existentes, sem prometer idempotência durável por request key após término. Respostas:401sem sessão,403papel insuficiente em BU conhecida,404fora do escopo,400payload inválido após autorização,409contexto/geração/conflito,429budget com Retry-After,503resultado externo inconclusivo. Erros nunca carregam payload bruto/URL/token. Nenhuma operação recebe URL externa arbitrária, WABA, credencial ou peer Instagram declarado pelo browser.

| Endpoint | Entrada e autorização | Resultado/efeitos |
| --- | --- | --- |
| GET /api/bff/channel-capabilities | sessão e grants; sem I/O externo | plataformas, login disponível e motivos seguros; configuração Instagram ausente desabilita essa capacidade, sem fallback WhatsApp. Parcial/malformada não anuncia disponibilidade. |
| POST /api/bff/business-units/:buId/instagram-authorizations | ADMIN+, CSRF, key; operation CONNECT ou REAUTHORIZE, channelId+expectedGeneration quando reautorizar | reserva tentativa durável e URL de autorização somente para hosts/redirect da instalação; TTL10min, consentimento explícito. Mesmo key/body replay; key com outro body409. |
| GET /api/bff/instagram-authorizations/:id | ADMIN+, mesma BU/ator quando tentativa em andamento | etapa, conta redigida, erro seguro; não consulta provider, não expõe state/code/token. |
| GET /api/bff/instagram-authorizations/callback | callback OAuth no contexto de sessão, state/nonce/session/expiry exatos; validar antes de usar code | CAS único; troca/valida recurso por client configurado; persistir candidato e ownership antes de inscrições; code/erro em query nunca logado; redirect303 sem parâmetros sensíveis e headers no-store/no-referrer. Expirado/ambíguo exige tentativa nova. Não é webhook de mensagens. |
| POST /api/bff/instagram-authorizations/:id/confirm | ADMIN+, CSRF, key, expectedGeneration; apenas recurso candidato devolvido pelo servidor | operador confirma conta legível; claim empresarial e provider identity atômicos, promover token por CAS; inscrição só depois de mapping durável. Conexão fica aguardando receipt real. |
| POST /api/bff/instagram-authorizations/:id/advance | ADMIN+, CSRF; recuperação explícita | até3requests de10s, budget40s sob lease60s; read-before-retry; inscrição ambígua não vira repetição automática de mutação. |
| POST /api/bff/instagram-authorizations/:id/cancel | ADMIN+, CSRF | encerra tentativa; preserva recurso/sideeffects parciais e token ativo anterior; não deleta histórico/BU nem revoga outro sistema. |
| GET /api/bff/business-units/:buId/channel-connections | ATENDENTE+, cursor local opaco, limit1..50(default20) | conexões identificadas por UUID+conta legível; página com continuação explícita, nenhum fan-out externo. Alias WhatsApp existente só preserva seu contrato, não escolhe entre múltiplos. |
| POST /api/bff/business-units/:buId/channel-connections/:channelId/verify | ADMIN+, CSRF e generation | observação explícita limitada/lease; autenticação e identity não comprovam recebimento. Receipt real depende de ingresso aceito. |
| POST /api/bff/business-units/:buId/channel-connections/:channelId/disconnect | ADMIN+, CSRF, expectedGeneration | desliga uso local, cerca geração/credencial e mantém tombstone/histórico; limpeza remota só quando sua propriedade/alcance for comprovada, senão reporta pendência. Não transferir recurso. |
| GET /webhooks/instagram | challenge e verify-token da instalação; sem sessão | handshake isolado, sem leitura de negócio ou promover canal pronto. |
| POST /webhooks/instagram | assinatura do app/produto correto sobre raw bytes, antes de conteúdo/DB de domínio | resolve recurso/server owner; normaliza mensagens textuais, echo/proveniência; commit e dedup transacionais. Eventos válidos fora da capacidade não inventam texto/destinatário. |
| GET /api/bff/conversations/:id/reply-options | ATENDENTE+; sem provider HTTP | rotas/vínculos da conversa, capacidades e política locais com versão/fingerprint. Conteúdo é autorizado antes da consulta. |
| POST /api/bff/conversations/:id/messages (existente, ampliado) | ATENDENTE+, CSRF; text e routeId/channelId/expectedGeneration/contextFingerprint | captura rota e destinatário server-side, passa pelo único OutboundService/admissões; contexto obsoleto409, sem enviar. Ack remoto e persistência local seguem resultados existentes. |

O único endpoint BFF de resposta continua POST /api/bff/conversations/:id/messages, com texto e contexto de rota obrigatório no cliente atualizado. Instagram aceita1..1000caracteres, WhatsApp mantém4096e seu parser/envelope atual; não reduzir o limite do WhatsApp por causa da nova plataforma. A resposta ordinária preserva concorrência entre replies existentes e claims single-use, com exclusão entre primeiro envio e reply, sem novo subsistema de request-key. O cliente impede duplo clique da mesma ação e não repete automaticamente envio incerto. Não criar POST /reply concorrente nem duplicar sender. A projeção de leitura devolve IDs locais/display, separando telefone WhatsApp e username Instagram; atualizar React/fixtures/expectativas no mesmo contrato. API v1/account_id e telefone continuam WhatsApp-only: filtrar accounts/canais/conversations e resolver messages/claim/release/post por identidade WhatsApp. Conta sem WhatsApp não aparece como número nulo usável no contrato legado. Typebot e webhook OUT não recebem Instagram por acidente.

### Limites de produto e confiança

- Instagram textual inicialmente entre1e1000caracteres; WhatsApp mantém4096e o envelope/parser atual. Novas rotas OAuth de payload pequeno limitam16KiB; não aplicar esse limite ao reply WhatsApp. Webhook Instagram até8MiB com no máximo1000updates por POST, conforme limite de batch documentado. Parser/gateway aplicam8MiB somente nessa rota; demais limites permanecem. Excedentes413antes de efeitos, sem slice/drop silencioso. Batch com falha parcial usa o mesmo replay/dedup das entradas já confirmadas; não retornar200para trabalho perdido.
- OAuth/troca de code, inscrição e send: um dispatch por claim, timeout10s/request e no máximo3requests externos por etapa administrativa; HTTP fora da transação. Máximo10tentativas de autorização/ator/hora e30/BU/hora persistentes. verify/advance usam lease por vínculo e cooldown10s; listagens não chamam provider.
- Token nunca no bundle, URL de retorno, docs, logs, histórico, eventos ou erros. Variáveis públicas exemplificam INSTAGRAM_CLIENT_ID, INSTAGRAM_CLIENT_SECRET, INSTAGRAM_WEBHOOK_APP_SECRET, INSTAGRAM_WEBHOOK_VERIFY_TOKEN, INSTAGRAM_API_VERSION e redirect/origin permitidos; os propósitos e a origem dos segredos seguem o contrato primário abaixo, sem fallback automático a META_APP_SECRET.
- Credential expiry vem do expires_in verificado na troca obrigatória curta→longa, armazenado com instante de aquisição e margem de60spara bloquear uso perto da expiração. Reautorização explícita renova a concessão; nada é chamado permanente. Nenhum cron/refresh automático ou token manual global nesta entrega.
- Política candidata de resposta: somente após INtextual assinada daquela conta/peer, até24hdo timestamp qualificado, com fence/lease atuais; read/echo/out/localcreatedAt não abrem janela. Esse teto é política conservadora do LeadsHug: a documentação primária admite a janela padrão24he uma exceção de até7dias para certos anúncios, que esta fatia não oferece. Usar o timestamp da ação original; não o entry.time de entrega. Timestamp ausente/inválido/futuro além de5minnão abre janela; timestamp antigo não a reabre por atraso. Não há HUMAN_AGENT ou extensão de janela.
- Frontend apresenta nome/username se conhecido, plataforma e conta atendida, nunca ID opaco como telefone. Nova conversa por telefone e templates permanece WhatsApp-only; DM Instagram nasce pelo ingresso autorizado. Compositor captura rota antes de digitar; mudança de contexto não apaga nem envia rascunho em outro destino.
- Medição pcv congelada abaixo: seed10milconversas, doze contas Instagram e um recurso WhatsApp por BU. Opções e lista não inspecionam todos os vínculos nem fazem HTTP por conversa. Nenhum benchmark foi realizado nesta etapa.

### Fontes primárias e limites da leitura

Coleção oficial Meta consultada em2026-10-23: [Instagram Login](https://www.postman.com/meta/instagram/folder/6raa77c/instagram-api-with-instagram-login), [pré-requisitos de mensagens](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api?entity=request-23987686-3fe78620-2258-44b6-893f-42d76c7200d7) e [envio de texto](https://www.postman.com/meta/instagram/request/scob1z4/text-message). Confirmam conta profissional, escopos de perfil/mensagens, início pelo usuário e referência opaca do destinatário; o exemplo inclui message_id no aceite. Não provam que o app do operador tem concessão ativa, nem entregam todo o contrato de OAuth/assinatura/renovação. O erro429foi a primeira observação da ferramenta web; a leitura direta posterior200 e o receipt primário abaixo encerram esse limite documental, sem usar terceiros como autoridade técnica.


## Normative architecture r1 integration — candidate v1.1

O parecer tático r1 em `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/architecture-r1-result.json` retornou changes_required. As resoluções abaixo são parte do contrato candidato que entrará em nova baseline/review; não mudaram código e não transformam o r1 em aprovação.

### IG-ARCH-R1-01 — rota, destinatário e contexto v2

A rota é imutável: não trocar seu contato, peer, recurso ou escopo. A rota deve provar simultaneamente Conversation.buId=Contact.buId=ContactIdentity.buId=BusinessChannelIdentity.buId=BuChannel.buId=ProviderResourceIdentity.buId; ContactIdentity.contactId=Conversation.contactId; ProviderResourceIdentity.businessIdentityId=ConversationRoute.businessIdentityId e a mesma igualdade para BuChannel; ProviderResourceIdentity.currentChannelId=BuChannel.id e provider=adapter. O namespace/escopo Instagram da identidade destinatária deve corresponder à conta/app da rota. Implementar essas relações por FKs compostas/unicidade e validação transacional centralizada das associações, com imutabilidade defendida no banco, sem depender somente de checks no controller.

Contexto de novos envios tem schemaVersion=2 e a tupla obrigatória: buId,conversationId,contactId,contactIdentityId,routeId,channelId,businessIdentityId,providerResourceIdentityId,adapterOrigin,generation,pairingEpoch,activeCredentialVersion,providerAccountReference. References imutáveis determinam o peer no servidor; nenhuma cópia de token/URL ou peer do browser entra no contexto. O fingerprint inclui a versão, a rota/tupla e os mesmos dados semânticos do pedido; cada claim conserva sua tupla. Antes do POST validar tupla e grant atuais sob as cercas já existentes; depois de ACK, reconciliação local aceita somente a identidade comprovada da tupla original, sem pedir token atual para apagar um fato passado nem aceitar outra conta.

Introduzir porta pequena ChannelEligibilityPolicy, resolvida junto à operação, para `reply`, `initial` e `automation`: supportedKinds continua no Channel; política/credencial/cadastro não viram métodos fictícios. OutboundService deixa de depender diretamente de OfficialChannelWindowPolicy; a implementação WhatsApp reutiliza a política existente e Instagram aplica24h/recebimento textual qualificado. Initial Instagram=false e automation Instagram=false, antes de reserva ou chamada Typebot. Não criar catálogo universal de plugins. Opções e dispatch usam o mesmo owner de política e mesmo contexto confiável.

Testes negativos obrigatórios: rota de outro contato na MESMA BU; peer de outra conta Instagram na mesma BU; canal/provider de outro recurso; versão desconhecida; mudança de geração; entrada concorrente por outra rota enquanto rascunho/envio usa a anterior. Todos recusam sem HTTP ao destinatário errado.

### IG-ARCH-R1-02 — cutover e leitura v1 por estado

Preservar request/canonicalRequest/requestFingerprint/selectedContext/ownerNonce/originalConversation (inclusive updatedAt)/deadlines/actor/receipt e IDs; não rehash, converter v1 em v2 ou tocar updatedAt de conversas durante backfill. O reader de contexto v1 só reconhece o shape exato existente (inclusive ausência do novo version tag); desconhecido não é v1 por fallback. Mapeamento v1→identidade local é associação comprovada externa ao receipt, sem escrever rota fictícia nele. Replay de mesma key com payload original é resolvido antes de elegibilidade atual; mudança de payload permanece409.

| Versão/estado existente | Ação permitida no cutover e recuperação | Proibição |
| --- | --- | --- |
| v1 PREPARED inicial/ordinário | quiescer API e cercar CAS; preservar exclusão até expiração original; depois encerrar/liberar somente pelo mecanismo local existente que prova ausência de dispatch. Nova intenção exige novo preview/key/contexto v2 | não enviar pelo reader v1, antecipar deadline, reescrever snapshot ou transformar em aceite |
| v1 SENDING sem receipt | manter exclusão/deadline original; após prazo, usar reconciliação local existente para AMBIGUOUS(initial) ou UNCERTAIN(ordinário) | não reenviar HTTP nem liberar por migração/restart |
| v1 AMBIGUOUS/UNCERTAIN | manter registro e exclusão; liberar somente com ação humana explícita de risco e deadline original, conforme contrato ST-CON-04 | migração não faz acknowledge automático nem zera lease/deadline |
| v1 EXTERNAL_ACCEPTED / EXTERNAL_ACCEPTED_LOCAL_BLOCKED | completar Message/slot localmente pelo mesmo owner, receipt/ator/snapshot e associação comprovada; se associação/grant/CAS não passar, conservar bloqueio e fatos | não repetir provider POST, apagar ACK ou recalcular originalConversation.updatedAt para forçar CAS |
| v1 terminal ou ordinário SETTLED | conservar fatos e replay/leitura; owner comprovado protege leitura; novo envio é v2 com nova key quando o owner já a exige; reply ordinário recebe nova admissão/nonce | não editar desfecho nem reabrir exclusão como se nunca enviado |
| versão desconhecida ou associação sem prova | registrar diagnóstico seguro e bloquear adoção/fluxo afetado antes de qualquer dispatch; intervenção explícita sob plano runtime | não inferir rota de BU.phone, do primeiro canal ou de coincidência de externalId |

Fixtures PostgreSQL devem cobrir todos os estados, snapshots/keys/deadlines antes/depois e zero chamadas de provider em recuperação v1. Opções de versão e migração mantêm v1 só para leitura/conclusão local; não há novo writer canônico v1 nem dual-write. IDs de mensagens/recurso e autoria/timestamps permanecem. Conflitos de owner ou duas conversas legadas para a mesma identidade não podem ser resolvidos por merge automático.

### IG-ARCH-R1-03 — cardinalidade nesta entrega

Uma BU admite no máximo UMA BusinessChannelIdentity WhatsApp durável, mesmo desconectada, e pode ter oficial+Evolution sobre esse mesmo número comprovado. Constraint parcial por buId para platform=WHATSAPP na identidade empresarial retida; segundo número retorna409antes de promover credencial, preservando owners/grants/histórico. Não filtrar só conexões prontas para decidir unicidade/ambiguidade. Múltiplas contas Instagram são admitidas e identificadas pelo vínculo exato.

Múltiplos números empresariais WhatsApp na mesma BU são fora desta entrega e exigem contrato próprio de API v1/Typebot/rotas; não criar primary/default ou multi-number UI antecipadamente. account_id continua BU e numero/telefone vêm do único recurso/identidade WhatsApp qualificados, nunca de um IGSID ou de BU.phone como autoridade. Typebot consulta/cria sessão e chama seu cliente apenas após provar plataforma WhatsApp, antes de trigger/session; keys legadas são preservadas, não generalizadas para Instagram.

### IG-ARCH-R1-04 — consultas e pcv congelados

- Inbox consulta em batch somente IDs de rotas/conexões relevantes à página de até50conversas; nenhuma leitura de toda a lista de conexões da BU e nenhum HTTP por conversa.
- reply-options faz lookup exato da rota/identidade da conversa: uma conta Instagram oferece um vínculo compatível; WhatsApp oferece no máximo oficial+Evolution do recurso único. Mais vínculos do que a cardinalidade ou referência incompatível é conflito, não truncamento. Quando houver mais de uma rota conhecida na conversa, usar a interação selecionada; se ausente, seleção explícita e catálogo paginado20até50, cursor opaco de até512caracteres, sem coletar todas as páginas no backend.
- start-options de abertura manual/primeira mensagem continua apenas WhatsApp, no máximo seus dois adapters; Instagram pronto não torna abertura por telefone elegível. Não manter take10silencioso sobre todos os tipos; catalogar conexões por página e resolver apenas as selecionadas. Verificar ambiguidade antes de readiness.
- EPS: seed10milconversas/BU em duas BUs/tenants, doze contas Instagram por BU+um recurso WA com dois adapters; leituras por ID e listagem50, cinco rodadas de20clientes após warmup. p95<=1000ms lookup/options e<=2000ms lista50; no máximo8queries de domínio por página e zero HTTP externo; plano de índice para peer/owner/rota, sem N+1. Registrar CPU/memória/DB, versões/imagens, amostra, percentis e query counts.
- FRC: navegação/mutações A→B→A e respostas em ordem inversa, duplo clique, popup cancelado, recarga/storage indisponível, chegada por outra conta com rascunho aberto; destino/rascunho/estado nunca atravessam contexto, zero POST no destino errado.
- BCI: nos owners com key durável (OAuth e primeiro envio), cinco ondas20requisições com mesmo key/payload: um claim/um POST/uma aceitação e mismatches409. Mais20replays de ingresso sobre a mesma mensagem: uma persistência, sem duplicar unread. Resposta ordinária preserva concorrência ordinary→ordinary e exclusão initial↔ordinary existentes: cada claim só é usado uma vez; o cliente é single-flight por ação, sem retry automático após incerteza. Não se promete um único ordinary admission global nem replay por key após estado terminal; retries locais conhecidos não repetem HTTP. Também20claims de recurso concorrentes de BUs/adapters distintos, um owner apenas. Barriers reais, não mocks de transação.
- RLS: sobre a mesma amostra, burst20readers+20mensagens sintéticas concorrentes por5rodadas; erro inesperado zero, nenhum bloqueio/deadlock pendente, preservação dos invariantes e dos budgets de leitura. Batch de1000updates textuais documentado: aceitar todos com dedup em até15sno teste isolado; replay sem novos efeitos. Execução é descartável com fake HTTP; não é SLA de provedor nem teste de carga no número real.

## Primary Instagram protocol reconvergence — r1

Fonte primária direta retornou200 em2026-10-23 após o acesso via ferramenta web ter retornado429. O receipt `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/primary-instagram-contract-r1.json` guarda URLs e hashes públicos, sem payloads operacionais. Não usar blogs/SDKs de terceiros como autoridade. Usuário confirmou o título Instagram Login no app existente; dados secretos serão configurados só na fase própria.

- Instagram Login usa client_id e client_secret do produto Instagram. Autorizar em www.instagram.com/oauth/authorize com redirect configurado e state; trocar code uma vez via POST api.instagram.com/oauth/access_token. Verificar lista de permissions retornada, exigindo apenas instagram_business_basic e instagram_business_manage_messages. Exigir envelope único válido; resposta ambígua/inválida falha sem escolher primeiro.
- Troca inicial também captura o user_id de autorização no seu namespace; não presumir que seja o mesmo valor de outros campos. Trocar token curto por longo via graph.instagram.com/access_token e ler expires_in. Ler /me?fields=user_id,username com o token ativo candidato: user_id identifica IG_ID da conta profissional e o entry.id de webhook; id app-scoped é diferente e não o substitui. Persistir a associação de forma tipada/comprovada, sem converter IDs para Number.
- API Graph desta entrega configurada explicitamente em v26.0, conforme exemplos primários atuais; ausente/malformada desabilita Instagram, sem fallback à versão WhatsApp. Token longo não é permanente; reautorização explícita usa mesma regra e só promove recurso igual. Refresh automático não está incluído; expirado/revogado pede reautorização e bloqueia envio.
- Inscrever o campo messages na configuração do app e ativar /IG_ID/subscribed_apps em graph.instagram.com para essa conta depois do mapping local. Inscrição no app e na conta são verificações distintas. Ler somente estado de inscrição da conta própria; mutação ambígua exige read-before-retry, sem tocar subscriptions de outros apps.
- GETchallenge usa token de verificação próprio. POST exige X-Hub-Signature-256 e HMAC SHA256 nos bytes brutos com o segredo explicitamente configurado para o app que entrega o webhook. O guia de setup aponta o App Secret do app; não presumir que seja o client_secret OAuth do produto nem fazer try-all/fallback a segredos WhatsApp. Teste negativo cruza os dois propósitos e recusa segredo errado. Corpo/parser/gateway seguem limites/assinatura antes de trust de dados.
- Para IN, entry.id e recipient.id precisam identificar a mesma conta empresarial verificada; sender.id é o peer IGSID. Para OUTecho, orientação é inversa: sender.id é a conta, recipient.id é o peer; message.mid qualifica o ID de mensagem. is_echo/is_self/is_deleted/unsupported/read/reaction não abrem janela ou simulam entrada textual. Timestamp da mensagem é em ms, não entry.time nem receivedAt local; clamp/falha fechada conforme política.
- Responder texto por POST graph.instagram.com/v26.0/IG_ID/messages com recipient.id resolvido da rota. Exigir message_id válido e compatibilidade da referência destinatária na resposta; ACKsemID ou timeout permanecem incertos. Só uma IN elegível cria contexto de resposta. Teto conservador24h; nenhum caso de CTD7dias ou HUMAN_AGENT é habilitado.
- Setup/testes controlados devem respeitar o nível de acesso e os papéis exigidos pela Meta para os recursos do operador. Disponibilidade de produto/conta não é aprovação de Advanced Access. Usuários externos, publicação e App Review não são autorizados por este TODO; a prova real só é aceita após recurso/testador elegível, app/conta inscritos, callback200, assinatura real e receipt persistido.


## Planning Finding Resolution Ledger — architecture r1

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-ARCH-R1-01 | Integrated | useful | partial | project | n/a | tupla v2, invariantes de contato/conta/recurso e porta de política congelados no candidato; testes negativos exigidos, sem código ainda |
| IG-ARCH-R1-02 | Integrated | useful | partial | project | n/a | matriz por estado v1, snapshots/fingerprint/CAS e recuperação zeroHTTP; nada reescrito no produto |
| IG-ARCH-R1-03 | Integrated | useful | yes | project | n/a | limite de um recurso WA por BU e múltiplas contas Instagram, partial unique e preservação APIv1/Typebot; sujeito à aprovação do contrato |
| IG-ARCH-R1-04 | Integrated | useful | partial | project | n/a | batch/cardinalidade/paginação exatos e thresholds EPS/FRC/BCI/RLS; ainda sem medição |

Essa disposição resolve a proposta documental para a nova rodada; não muda o outcome histórico changes_required do r1 e não prova a implementação. Nenhum finding foi dispensado ou tratado como waiver.

## Planning Finding Resolution Ledger — architecture r2

| Finding ID | Resolution | Status | Evidence |
| --- | --- | --- | --- |
| IG-ARCH-R2-01 | Integrated | closed | chaves duráveis OAuth/initial, concorrência ordinary preservada e BCI delimitado; correção inspecionada pelo reviewer |
| IG-ARCH-R2-02 | Integrated | closed | limites Instagram separados de WhatsApp4096/parser; correção inspecionada pelo reviewer |

Parecer terminal r2go, estático e sem execução; receipt architecture-r2-result.json. Crítica r2go e guards de coerência/escopo concluídos posteriormente, com receipts próprios; nenhuma autorização de implementação.

## Normative critique r1 integration — candidate v1.3

As três correções abaixo integram o parecer changes_required de critique-r1-result.json; nenhum teste/código foi editado. Baseline v1.3 publicada em f4891ba1 e crítica r2go concluída posteriormente; ver receipt próprio.

- IG-CRIT-R1-01: seis arquivos exatos de regressão admitidos acima. conversation-start e dispatch-admission deixam de ter freeze final byte-exact, mas hashes originais continuam fatos de baseline. Só fixtures canônicas, lookup qualificado e contextos versionados podem ser adaptados; preservar todos os cenários, asserts, contadores e evidência causal. Casos v1 deliberados continuam como cutover, não writers novos. Os outros quatro arquivos recebem apenas fixtures, exceto historico que também testa a fronteira explícita abaixo. Não interceptar Prisma nem criar writer/trigger legado para satisfazer fixtures obsoletas. A política v1.1 de preservação governa essas exceções; as observações anteriores não são apagadas.
- IG-CRIT-R1-02: GET /api/bff/business-units e seu detalhe preservam a projeção legacy channels/canais apenas WhatsApp, no máximo os dois bindings compatíveis do recurso empresarial durável único. Resolver bindings atuais/proveniência antes de readiness; desconectado não é apagado para esconder ambiguidade. Histórico de bindings aposentados não vira catálogo implícito. Incompatibilidade/cardinalidade excedida é conflito explícito, sem take/slice silencioso. me.controller.ts é admitido somente para essa projeção limitada; grants/criação e outras responsabilidades ficam preservadas. A UI Instagram usa channel-connections paginado, sem hidratar toda a conta via business-units. Testes provam zero contas Instagram nessa projeção, inclusive com12contas, consultas limitadas e ausência de HTTP externo.
- IG-CRIT-R1-03: Consultar legado (lista, drilldown e CSV) é WhatsApp-only. historico.service.ts filtra por identidade WhatsApp qualificada, usa telefone do peer e número empresarial do recurso comprovado único, nunca Conversation.contact/BU.phone como autoridade. BU só Instagram não produz linha telefônica; BU mista exclui Instagram; IGSID numérico igual a E.164 não colide nem revela conversa. Preservar filtros, paginação, grants e histórico WhatsApp; os testes de historico cobrem esses três casos sem enfraquecer os anteriores. Instagram continua na caixa de Atendimento; Consultar multicanal exige contrato próprio futuro, sem Web/controller novos nesta fatia.
- Webhook de saída para parceiro: owner atualmente sem import/call nos fontes públicos verificados. Não implementar nem registrar novo caller Instagram; nenhum caminho novo para esse serviço dormente, nenhuma expansão de contrato parceiro. Typebot continua bloqueado antes de trigger/session/client para Instagram.

| Finding ID | Resolution | Status | Evidence |
| --- | --- | --- | --- |
| IG-CRIT-R1-01 | Integrated | closed by critique r2 | seis caminhos exatos e política de preservação v1.1 |
| IG-CRIT-R1-02 | Integrated | closed by critique r2 | produtor BU legacy limitado e Instagram paginado |
| IG-CRIT-R1-03 | Integrated | closed by critique r2 | Consultar WhatsApp qualificado, testes de isolamento/collision |

## Approval Readiness Evidence — v1.3

Arquitetura r2 e crítica r2 retornaram go. Crítica revisou as sete lentes e fechou os três findings r1. Coherence e scope-drift retornaram go; nenhuma das23seções materiais mudou após a baseline revisada. Authority preflight é estrutural, não execução. Full diff guard/runtime/API/Meta/provas físicas ainda não foram executados nesta preparação e permanecem para suas fases próprias. APROVADO do contrato não autoriza leitura privada, banco real, callbacks, envio externo, Git de produto, produção ou App Review.

Authority preflight final: `artifacts/reviews/leadshug-instagram-channel-20261023/evidence/authority-preflight-final-r4.json`, outcome preflight-go, execution_authority_granted=false. Naquele preflight, aprovação humana permanecia pendente; ela foi recebida posteriormente e registrada em approval-execution-cp1.json.

## Execution Checkpoints — approved v1.3

| Checkpoint | State | Owner / next proof |
| --- | --- | --- |
| CP1 Identity/route/state cutover | accepted r8 | cp1-r8-acceptance.json; source companion validated and proved, no Instagram runtime claim |
| CP2 OAuth/ingress | in progress; not accepted | source18 full398unit/555E2E GREEN +affectedR5 reconciled; ROOT02/SUBREC02 resolvedqualified; primary/precontroller remainopen |
| CP3 Channel/policy/consumers | test-first lane ready | two new admitted specs and externalHTTP fake only; shared sender/acceptance next |
| CP4 UI/CI/browser | pending | profile handoff for CI/runtime tooling |
| CP5 independent audits | pending | consolidated source and ALL evidence |
| CP6 local real rollout/proof | pending separate plan | approval later; no real runtime/private inputs now |


## CP3 affected adherence46 terminal — 2026-10-24

Ambas lanes retornaramturn.completed e strictmerge válido; root conferiu261fontes/T/34inputs/35preservações/3index. União35corpos atuais cobre19deltas desdeAPI35 e11mudados da revisão52original;41antigos preservados porhash. `cp3-adherence46-root-adjudication.json` integra3achados atuais: A46-01 finalProviderFence lê contexto antes de awaits posteriores de política/ator, permitindo provider tuple obsoleto; B46-01 initialOptions ofereceWAparacontatoIG emBUmista embora dispatchrecuse; A-02 ainda não detectaOfficialChannelWindowPolicy e namespaceOfficialEligibilityPolicy. São fixes dentro doWHATaprovado. Antes da fonte, obter HOW coerente e provaREDcausal sem teste artificial após última observação; shortTX/HTTPfora deTX, política abstrata, locks e knownACK permanecem. ROOT03/CP4integral e primaryGET/SUBREC03 seguemopen; propostasprivacidade/UTF8pendentes sem autoridade. Defeitos originais ROOT01/02/07/A01/CSV35-05 têm fonte/prova45+46; o novoA46permaneceopen independente. Sem aceiteCP3/feature.

### CP3 adherence46 finding resolution

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| IG-CP3-A46-01 | Integrated | useful | partial | project | n/a | Current provider andactor facts need coherent lastlocal observation; nativecausal proof and HOWreview before source; cp3-adherence46-root-adjudication.json |
| IG-CP3-B46-01 | Integrated | useful | yes | project | n/a | Initialoptions mustrejectIGrecipients; actualWApositive andIGnegative boundedtests required; cp3-adherence46b-raw.json |
| IG-CP3-A-02 | Integrated | useful | yes | project | n/a | Residual Official window/namespace policy dependencies require guardnegativefixtures; current consumers notclaimedconcrete; cp3-adherence46b-raw.json |
| IG-CP3-ROOT-03 | Integrated | useful | partial | project | n/a | CP4whole/latergatesremainopeninTODO, no waiver; both46reviews |
| IG-SUBPROTO-01 | Integrated | useful | partial | project | n/a | OwnGETprotocol unproved; retainUNKNOWN/no-repeat andSUBREC03, no copiedPage/guessedabsence; cp3-adherence46b-raw.json |

## Complete current source api-app/src/domain/channels/transport/channel.ts
```
import type { TemplateManagementContext, TemplateSummary } from '../../message-templates/template-management.ports';
import type { Prisma } from '@prisma/client';
import { createHash } from 'node:crypto';
import type { ChannelEligibilityPolicy } from '../../inbox/channel-eligibility-policy';

export type ChannelOrigin = 'OFICIAL' | 'NAO_OFICIAL' | 'INSTAGRAM';
export type LegacyChannelOrigin = Exclude<ChannelOrigin, 'INSTAGRAM'>;
export type ChannelAdapterOrigin = ChannelOrigin;

export type ChannelAvailabilityReason =
  | 'CANAL_AUSENTE'
  | 'CANAL_AMBIGUO'
  | 'CANAL_SELECIONADO_INDISPONIVEL'
  | 'CHANNEL_IDENTITY_NOT_VERIFIED'
  | 'CHANNEL_NOT_READY'
  | 'PENDING_CREDENTIAL'
  | 'JANELA_FECHADA'
  | 'UNSUPPORTED_KIND';

export type ChannelSendResult =
  | { outcome: 'ACCEPTED'; externalMessageId: string }
  | { outcome: 'BLOCKED'; reason: ChannelAvailabilityReason | 'CHANNEL_CONTEXT_CHANGED' }
  | { outcome: 'REJECTED'; code: string }
  | { outcome: 'UNKNOWN'; evidence: 'ACK_WITHOUT_ID' | 'TRANSPORT_UNCONFIRMED'; legacyCode: string };

export interface TextMessage {
  kind: 'text';
  recipientRef: string;
  text: string;
}

export interface ApprovedTemplateMessage {
  kind: 'approved-template';
  recipientRef: string;
  template: {
    readonly summary: TemplateSummary;
    readonly values: Readonly<Record<string, string>> | readonly string[];
    readonly managementContext: TemplateManagementContext;
    readonly renderedText: string;
    readonly semanticFingerprint: string;
  };
}

export type ChannelMessage = TextMessage | ApprovedTemplateMessage;
export type ChannelMessageKind = ChannelMessage['kind'];

export interface ChannelSendOptions {
  /** Initial dispatch carries its durable claim fence into the provider adapter. */
  readonly purpose?: 'initial';
  /** Generic dispatch fence; invoked at the final provider boundary for ordinary and initial sends. */
  readonly beforeDispatch?: () => Promise<boolean>;
}

export abstract class Channel {
  abstract readonly supportedKinds: readonly ChannelMessageKind[];
  abstract sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult>;
}

/** Safe storage provenance captured by pre-v2 WhatsApp sends. */
export interface LegacyChannelOperationContextV1 {
  readonly channelId: string;
  readonly buId: string;
  readonly channelOrigin: LegacyChannelOrigin;
  readonly providerResourceIdentityId: string;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
  readonly requiresWindow: boolean;
  readonly providerAccountReference: string | null;
}

/** The immutable local route and provider ownership captured by every new send. */
export interface ChannelOperationContextV2 {
  readonly schemaVersion: 2;
  readonly buId: string;
  readonly conversationId: string;
  readonly contactId: string;
  readonly contactIdentityId: string;
  readonly routeId: string;
  readonly channelId: string;
  readonly businessIdentityId: string;
  readonly providerResourceIdentityId: string;
  readonly adapterOrigin: ChannelAdapterOrigin;
  readonly generation: number;
  readonly pairingEpoch: number;
  readonly activeCredentialVersion: number | null;
  readonly providerAccountReference: string | null;
}

/** Every newly resolved and persisted operation is strictly route-bound V2. */
export type ChannelOperationContext = ChannelOperationContextV2;

const V1_CONTEXT_KEYS = [
  'channelId', 'buId', 'channelOrigin', 'providerResourceIdentityId', 'generation',
  'pairingEpoch', 'activeCredentialVersion', 'requiresWindow', 'providerAccountReference',
] as const;

const V2_CONTEXT_KEYS = [
  'schemaVersion', 'buId', 'conversationId', 'contactId', 'contactIdentityId', 'routeId',
  'channelId', 'businessIdentityId', 'providerResourceIdentityId', 'adapterOrigin',
  'generation', 'pairingEpoch', 'activeCredentialVersion', 'providerAccountReference',
] as const;

function record(value: unknown): Record<string, unknown> | null {
  return value !== null && typeof value === 'object' && !Array.isArray(value)
    ? value as Record<string, unknown>
    : null;
}

function exactKeys(row: Record<string, unknown>, keys: readonly string[]): boolean {
  const actual = Object.keys(row);
  return actual.length === keys.length && actual.every((key) => (keys as readonly string[]).includes(key));
}

/** Parse only the exact unversioned v1 shape; it can be used to read and finish known receipts, never to dispatch. */
export function parseLegacyChannelOperationContextV1(value: unknown): LegacyChannelOperationContextV1 | null {
  const row = record(value);
  if (!row || !exactKeys(row, V1_CONTEXT_KEYS)) return null;
  if (typeof row.channelId !== 'string' || !row.channelId
    || typeof row.buId !== 'string' || !row.buId
    || (row.channelOrigin !== 'OFICIAL' && row.channelOrigin !== 'NAO_OFICIAL')
    || typeof row.providerResourceIdentityId !== 'string' || !row.providerResourceIdentityId
    || typeof row.generation !== 'number' || !Number.isSafeInteger(row.generation) || row.generation < 1
    || typeof row.pairingEpoch !== 'number' || !Number.isSafeInteger(row.pairingEpoch) || row.pairingEpoch < 0
    || row.activeCredentialVersion !== null && (typeof row.activeCredentialVersion !== 'number'
      || !Number.isSafeInteger(row.activeCredentialVersion) || row.activeCredentialVersion < 1)
    || typeof row.requiresWindow !== 'boolean'
    || row.providerAccountReference !== null && (typeof row.providerAccountReference !== 'string' || !row.providerAccountReference)) return null;
  return row as unknown as LegacyChannelOperationContextV1;
}

/** Parse a new immutable v2 operation tuple. Unknown keys and versions fail closed. */
export function parseChannelOperationContextV2(value: unknown): ChannelOperationContextV2 | null {
  const row = record(value);
  if (!row || !exactKeys(row, V2_CONTEXT_KEYS) || row.schemaVersion !== 2) return null;
  const requiredIds = [
    'buId', 'conversationId', 'contactId', 'contactIdentityId', 'routeId', 'channelId',
    'businessIdentityId', 'providerResourceIdentityId',
  ] as const;
  if (requiredIds.some((key) => typeof row[key] !== 'string' || !(row[key] as string).trim())
    || (row.adapterOrigin !== 'OFICIAL' && row.adapterOrigin !== 'NAO_OFICIAL' && row.adapterOrigin !== 'INSTAGRAM')
    || typeof row.generation !== 'number' || !Number.isSafeInteger(row.generation) || row.generation < 1
    || typeof row.pairingEpoch !== 'number' || !Number.isSafeInteger(row.pairingEpoch) || row.pairingEpoch < 0
    || row.activeCredentialVersion !== null && (typeof row.activeCredentialVersion !== 'number'
      || !Number.isSafeInteger(row.activeCredentialVersion) || row.activeCredentialVersion < 1)
    || row.providerAccountReference !== null && (typeof row.providerAccountReference !== 'string' || !row.providerAccountReference)) return null;
  return row as unknown as ChannelOperationContextV2;
}

export function channelContextFingerprint(context: ChannelOperationContextV2): string {
  const values = V2_CONTEXT_KEYS.map((key) => context[key]);
  return createHash('sha256').update(JSON.stringify(values)).digest('hex');
}

export type StoredChannelOperationContext =
  | { readonly version: 1; readonly context: LegacyChannelOperationContextV1 }
  | { readonly version: 2; readonly context: ChannelOperationContextV2 };

/** Version-dispatching read path. An unknown explicit version is never reinterpreted as legacy v1. */
export function parseStoredChannelOperationContext(value: unknown): StoredChannelOperationContext | null {
  const row = record(value);
  if (!row) return null;
  if (row.schemaVersion === 2) {
    const context = parseChannelOperationContextV2(value);
    return context ? { version: 2, context } : null;
  }
  if (Object.prototype.hasOwnProperty.call(row, 'schemaVersion')) return null;
  const context = parseLegacyChannelOperationContextV1(value);
  return context ? { version: 1, context } : null;
}

/** Deprecated v1-only compatibility parser. New admission writers must call the v2 parser/serializer. */
export function parseChannelOperationContext(value: Prisma.JsonValue): LegacyChannelOperationContextV1 | null {
  return parseLegacyChannelOperationContextV1(value);
}

export interface ResolvedChannelOperation {
  readonly channel: Channel;
  readonly context: ChannelOperationContext;
  readonly eligibilityPolicy: ChannelEligibilityPolicy;
  /** Transient expiry fence; it is never persisted into V2 context. */
  readonly credentialExpiresAt: Date | null;
}

/** Historical V1 records have no dispatch capability and are only validated as local facts. */
export interface ResolvedLegacyOperation {
  readonly context: LegacyChannelOperationContextV1;
}

export interface ChannelAvailability {
  available: boolean;
  reason: ChannelAvailabilityReason | null;
  channelOrigin: ChannelOrigin | null;
  requiresWindow: boolean;
  windowOpen: boolean;
  expiresAt: Date | null;
}

export interface ChannelReplyOptions {
  readonly schemaVersion: 2;
  readonly options: readonly {
    readonly schemaVersion: 2;
    readonly routeId: string;
    readonly channelId: string;
    readonly channelOrigin: ChannelOrigin;
    readonly generation: number;
    readonly contextFingerprint: string;
    readonly accountLabel: string;
    readonly recipientLabel: string;
    readonly supportedKinds: readonly ['text'];
    readonly policy: 'INSTAGRAM_24H' | 'OFFICIAL_WINDOW' | 'EVOLUTION';
    readonly available: boolean;
    readonly reason: string;
    readonly requiresWindow: boolean;
    readonly windowOpen: boolean;
    readonly windowExpiresAt: Date | null;
  }[];
}

export interface InitialChannelOption {
  readonly id: string;
  readonly type: Exclude<ChannelOrigin, 'INSTAGRAM'>;
  readonly generation: number;
  readonly pairingEpoch?: number;
  readonly activeCredentialVersion?: number | null;
  readonly supportedKinds: readonly ChannelMessageKind[];
  readonly availability: Readonly<Record<ChannelMessageKind, string | null>>;
  readonly windowExpiresAt?: Date;
}

export interface ConversationChannelReference {
  conversationId: string;
  buId: string;
  readonly routeId?: string;
  readonly channelId?: string;
  readonly expectedGeneration?: number;
  readonly contextFingerprint?: string;
}

export interface InitialChannelReference extends ConversationChannelReference {
  readonly channelId: string;
  readonly kind: ChannelMessageKind;
}

export interface ConversationAvailabilityReference extends ConversationChannelReference {
  latestMessageOrigin: ChannelOrigin | null;
  readonly latestProviderResourceIdentityId?: string | null;
}

export interface VerifiedIngressChannelReference extends ConversationChannelReference {
  channelId: string;
  providerResourceIdentityId: string;
  channelOrigin: ChannelOrigin;
  generation: number;
  pairingEpoch: number;
}

export abstract class ChannelResolver {
  abstract resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation>;
  abstract resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation>;
  /** Explicit channel selection for first-message intent; never infers or falls back. */
  abstract resolveForInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation>;
  /** Metadata-only choices for an explicit WhatsApp initial-channel selection. */
  abstract initialOptions(conversationId: string, buId: string): Promise<readonly InitialChannelOption[]>;
  abstract inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability>;
  abstract inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>>;
  abstract replyOptions(conversationId: string, buId: string): Promise<ChannelReplyOptions>;
  abstract hasReadyChannelForNewConversation(buId: string): Promise<boolean>;
  /** Revalidates the immutable captured transport tuple using the caller's already locked local transaction. */
  abstract validateOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedContext: Prisma.JsonValue,
    expectedCredentialExpiresAt: Date | null,
    expectedRecipientRef?: string,
  ): Promise<boolean>;
  /** Validates a known accepted operation for local-only Message recovery; credential/readiness may rotate after provider ACK. */
  abstract validateAcceptedOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedContext: Prisma.JsonValue,
  ): Promise<boolean>;
  /** Exact V1 association proof for local known-receipt recovery only. */
  abstract validateLegacyAcceptedContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: LegacyChannelOperationContextV1,
    selectedContext: Prisma.JsonValue,
  ): Promise<boolean>;
  abstract contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'>;
  /** Fresh post-claim provider fence, including the current credential version and readiness tuple. */
  abstract contextBeforeDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'>;
}

```

## Complete current source api-app/src/domain/inbox/channel-eligibility-policy.ts
```
import { Prisma } from '@prisma/client';
import type { ChannelAdapterOrigin, ChannelMessageKind } from '../channels/transport/channel';
import type { PrismaService } from '../../infra/prisma/prisma.service';
import { OfficialChannelWindowPolicy, officialWindowState, type OfficialWindowReference, type OfficialWindowState } from './channel-window-policy';

export type ChannelOperationKind = 'REPLY' | 'INITIAL' | 'AUTOMATION';

export interface ChannelEligibilityInput {
  readonly operation: ChannelOperationKind;
  readonly humanActor: boolean;
  readonly kind: ChannelMessageKind;
  readonly inboundWindowOpen: boolean;
}

export interface ChannelEligibilityResult {
  readonly eligible: boolean;
  readonly reason: 'AVAILABLE' | 'UNSUPPORTED_KIND' | 'WINDOW_UNQUALIFIED' | 'WINDOW_CLOSED' | 'HUMAN_REPLY_REQUIRED';
}

export type ChannelWindowReference = OfficialWindowReference;

/** Domain contract for operation-specific eligibility and its current resource window. */
export abstract class ChannelEligibilityPolicy {
  abstract readonly origin: ChannelAdapterOrigin;
  abstract readonly requiresWindow: boolean;
  abstract inspect(reference: ChannelWindowReference, tx?: Prisma.TransactionClient): Promise<OfficialWindowState>;
  abstract inspectMany(references: readonly ChannelWindowReference[], tx?: Prisma.TransactionClient): Promise<Map<string, OfficialWindowState>>;
  abstract evaluate(input: ChannelEligibilityInput): ChannelEligibilityResult;

  protected available(input: ChannelEligibilityInput): ChannelEligibilityResult {
    if (input.kind !== 'text') return { eligible: false, reason: 'UNSUPPORTED_KIND' };
    if (!input.inboundWindowOpen) return { eligible: false, reason: 'WINDOW_CLOSED' };
    return { eligible: true, reason: 'AVAILABLE' };
  }
}

export class OfficialEligibilityPolicy extends ChannelEligibilityPolicy {
  readonly origin = 'OFICIAL' as const;
  readonly requiresWindow = true;
  constructor(private readonly windows: OfficialChannelWindowPolicy) { super(); }
  inspect(reference: ChannelWindowReference, tx?: Prisma.TransactionClient): Promise<OfficialWindowState> {
    return tx ? this.windows.inspectInTransaction(tx, reference) : this.windows.inspect(reference);
  }
  async inspectMany(references: readonly ChannelWindowReference[], tx?: Prisma.TransactionClient): Promise<Map<string, OfficialWindowState>> {
    const uniqueByPair = new Map(references.map((reference) => [this.key(reference), reference]));
    const uniqueReferences = [...uniqueByPair.values()];
    if (tx) {
      const rows = await Promise.all(uniqueReferences.map(async (reference) => [
        this.key(reference), await this.windows.inspectInTransaction(tx, reference),
      ] as const));
      return new Map(rows);
    }
    const firstByConversation = new Map<string, ChannelWindowReference>();
    const duplicates: ChannelWindowReference[] = [];
    for (const reference of uniqueReferences) {
      if (firstByConversation.has(reference.conversationId)) duplicates.push(reference);
      else firstByConversation.set(reference.conversationId, reference);
    }
    const firstReferences = [...firstByConversation.values()];
    const states = await this.windows.inspectMany(firstReferences);
    const output = new Map(firstReferences.map((reference) => [
      this.key(reference), states.get(reference.conversationId) ?? { open: false, expiresAt: null },
    ]));
    for (const reference of duplicates) output.set(this.key(reference), await this.windows.inspect(reference));
    return output;
  }
  evaluate(input: ChannelEligibilityInput): ChannelEligibilityResult {
    if (input.kind === 'approved-template') {
      return input.operation === 'INITIAL'
        ? { eligible: true, reason: 'AVAILABLE' }
        : { eligible: false, reason: 'UNSUPPORTED_KIND' };
    }
    return this.available(input);
  }
  private key(reference: ChannelWindowReference) { return JSON.stringify([reference.conversationId, reference.providerResourceIdentityId]); }
}

export class EvolutionEligibilityPolicy extends ChannelEligibilityPolicy {
  readonly origin = 'NAO_OFICIAL' as const;
  readonly requiresWindow = false;
  async inspect(): Promise<OfficialWindowState> { return { open: true, expiresAt: null }; }
  async inspectMany(references: readonly ChannelWindowReference[]): Promise<Map<string, OfficialWindowState>> {
    return new Map(references.map((reference) => [JSON.stringify([reference.conversationId, reference.providerResourceIdentityId]), { open: true, expiresAt: null }]));
  }
  evaluate(input: ChannelEligibilityInput) {
    return input.kind === 'text' ? { eligible: true, reason: 'AVAILABLE' as const } : { eligible: false, reason: 'UNSUPPORTED_KIND' as const };
  }
}

/** Instagram opens only from a qualified original inbound text for the exact pair. */
export class InstagramEligibilityPolicy extends ChannelEligibilityPolicy {
  readonly origin = 'INSTAGRAM' as const;
  readonly requiresWindow = true;
  constructor(private readonly prisma: PrismaService) { super(); }

  async inspect(reference: ChannelWindowReference, tx?: Prisma.TransactionClient): Promise<OfficialWindowState> {
    return (await this.inspectMany([reference], tx)).get(this.key(reference)) ?? { open: false, expiresAt: null };
  }

  async inspectMany(references: readonly ChannelWindowReference[], tx?: Prisma.TransactionClient): Promise<Map<string, OfficialWindowState>> {
    const output = new Map<string, OfficialWindowState>();
    if (!references.length) return output;
    const uniqueReferences = [...new Map(references.map((reference) => [this.key(reference), reference])).values()];
    if (uniqueReferences.length > 100) {
      return new Map(references.map((reference) => [this.key(reference), { open: false, expiresAt: null }]));
    }
    const conversationIds = uniqueReferences.map(({ conversationId }) => conversationId);
    const resourceIds = uniqueReferences.map(({ providerResourceIdentityId }) => providerResourceIdentityId);
    const client = tx ?? this.prisma;
    const rows = await client.$queryRaw<Array<{ conversation_id: string; provider_resource_identity_id: string; inbound_at: Date | null; now: Date }>>`
      SELECT requested.conversation_id, requested.provider_resource_identity_id, latest.official_inbound_at AS inbound_at,
        clock_timestamp() AS now
      FROM unnest(ARRAY[${Prisma.join(conversationIds)}]::text[], ARRAY[${Prisma.join(resourceIds)}]::text[])
        AS requested(conversation_id, provider_resource_identity_id)
      LEFT JOIN LATERAL (
        SELECT message.official_inbound_at
        FROM messages AS message
        WHERE message.conversation_id = requested.conversation_id
          AND message.provider_resource_identity_id = requested.provider_resource_identity_id
          AND message.direction = 'IN' AND message.channel_origin = 'INSTAGRAM'::"ChannelType"
          AND message.message_type = 'TEXTO'::"MessageType" AND message.content IS NOT NULL
          AND btrim(message.content) <> ''
          AND message.official_inbound_at IS NOT NULL AND message.official_inbound_at <= clock_timestamp()
        ORDER BY message.official_inbound_at DESC, message.id DESC
        LIMIT 1
      ) AS latest ON TRUE
    `;
    const byPair = new Map(rows.map((row) => [this.key({ conversationId: row.conversation_id, providerResourceIdentityId: row.provider_resource_identity_id }), officialWindowState(row.inbound_at, row.now)]));
    for (const reference of uniqueReferences) output.set(this.key(reference), byPair.get(this.key(reference)) ?? { open: false, expiresAt: null });
    return output;
  }

  evaluate(input: ChannelEligibilityInput): ChannelEligibilityResult {
    if (input.operation !== 'REPLY' || !input.humanActor) return { eligible: false, reason: 'HUMAN_REPLY_REQUIRED' };
    if (input.kind !== 'text') return { eligible: false, reason: 'UNSUPPORTED_KIND' };
    return this.available(input);
  }

  private key(reference: ChannelWindowReference) { return JSON.stringify([reference.conversationId, reference.providerResourceIdentityId]); }
}

/** Runtime composition map. Every origin must have one concrete policy. */
export class ChannelEligibilityPolicyRegistry {
  private readonly policies: ReadonlyMap<ChannelAdapterOrigin, ChannelEligibilityPolicy>;
  constructor(policies: readonly ChannelEligibilityPolicy[]) {
    const entries = policies.map((policy) => [policy.origin, policy] as const);
    if (entries.length !== 3 || new Set(entries.map(([origin]) => origin)).size !== entries.length) {
      throw new Error('Channel eligibility policy registration must cover each channel origin exactly once.');
    }
    this.policies = new Map(entries);
  }
  get(origin: ChannelAdapterOrigin): ChannelEligibilityPolicy {
    const policy = this.policies.get(origin);
    if (!policy) throw new Error(`Missing channel eligibility policy for ${origin}.`);
    return policy;
  }
  async inspectMany(references: readonly (ChannelWindowReference & { origin: ChannelAdapterOrigin })[]) {
    const grouped = new Map<ChannelAdapterOrigin, ChannelWindowReference[]>();
    for (const { origin, ...reference } of references) grouped.set(origin, [...(grouped.get(origin) ?? []), reference]);
    const output = new Map<string, OfficialWindowState>();
    for (const [origin, group] of grouped) {
      const states = await this.get(origin).inspectMany(group);
      for (const [key, state] of states) output.set(key, state);
    }
    return output;
  }
  key(reference: ChannelWindowReference) { return JSON.stringify([reference.conversationId, reference.providerResourceIdentityId]); }
}

```

## Complete current source api-app/src/integrations/channels/prisma-channel-resolver.ts
```
import { BadRequestException, ConflictException, Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelCredentialResolver, type ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import {
  ChannelResolver,
  channelContextFingerprint,
  type ChannelAvailability,
  type ChannelReplyOptions,
  type InitialChannelOption,
  type InitialChannelReference,
  type ConversationAvailabilityReference,
  type ChannelOperationContext,
  type LegacyChannelOperationContextV1,
  type ChannelOrigin,
  type ConversationChannelReference,
  type ResolvedChannelOperation,
  type VerifiedIngressChannelReference,
  parseChannelOperationContextV2,
  parseLegacyChannelOperationContextV1,
} from '../../domain/channels/transport/channel';
import { ChannelAdapterRegistry } from './channel-adapter-registry';
import type { OfficialWindowState } from '../../domain/inbox/channel-window-policy';
import { ChannelEligibilityPolicyRegistry } from '../../domain/inbox/channel-eligibility-policy';
import { metaAccountReference } from './account-reference';
import { normalizeWhatsAppPersonPeer } from '../../domain/inbox/contact-identity';
import { hasChannelProviderReadiness } from '../../domain/channels/channel-provider-readiness';
function canonicalV2(context: ChannelOperationContext): string {
  return JSON.stringify([context.schemaVersion, context.buId, context.conversationId, context.contactId, context.contactIdentityId,
    context.routeId, context.channelId, context.businessIdentityId, context.providerResourceIdentityId, context.adapterOrigin,
    context.generation, context.pairingEpoch, context.activeCredentialVersion, context.providerAccountReference]);
}

type Candidate = {
  id: string;
  buId: string;
  type: ChannelOrigin;
  status: string;
  phoneNumberId: string | null;
  evolutionInstanceName: string | null;
  generation: number;
  pairingEpoch: number;
  verifiedEpoch: number | null;
  ownNumberVerified: boolean;
  providerConnectionState: string;
  receiptVerifiedAt: Date | null;
  requiresWindow: boolean;
  businessIdentityId: string | null;
  businessIdentity: { id: string; buId: string; platform: string; namespace: string; scopeReference: string; externalResourceId: string } | null;
  wabaId: string | null;
  providerIdentities: Array<{ id: string; buId: string; provider: ChannelOrigin; currentChannelId: string | null; managedLifecycle: boolean; externalResourceId: string; businessIdentityId: string | null }>;
};

@Injectable()
export class PrismaChannelResolver extends ChannelResolver {
  constructor(
    private readonly prisma: PrismaService,
    private readonly credentials: ChannelCredentialResolver,
    private readonly adapters: ChannelAdapterRegistry,
    private readonly policies: ChannelEligibilityPolicyRegistry,
  ) { super(); }

  async resolveForConversation(reference: ConversationChannelReference): Promise<ResolvedChannelOperation> {
    const { candidate } = await this.selectForConversation(reference);
    const operation = await this.bind(candidate, reference.conversationId, reference.routeId);
    if (reference.expectedGeneration !== undefined && operation.context.generation !== reference.expectedGeneration) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    if (reference.contextFingerprint && channelContextFingerprint(operation.context) !== reference.contextFingerprint) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    return operation;
  }

  async resolveForInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true, contactId: true, contactType: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    if (!candidate) this.throwUnavailable('CANAL_SELECIONADO_INDISPONIVEL');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    const eligibilityPolicy = this.policies.get(candidate.type);
    const policy = eligibilityPolicy.evaluate({ operation: 'INITIAL', humanActor: true, inboundWindowOpen: true, kind: reference.kind });
    if (!policy.eligible) this.throwUnavailable('UNSUPPORTED_KIND');
    const routeId = await this.ensureExplicitWhatsAppInitialRoute(conversation, candidate);
    const operation = await this.bind(candidate, conversation.id, routeId);
    if (!operation.channel.supportedKinds.includes(reference.kind)) this.throwUnavailable('UNSUPPORTED_KIND');
    if (reference.kind === 'text' && operation.eligibilityPolicy.requiresWindow) {
      const window = await operation.eligibilityPolicy.inspect({ conversationId: conversation.id, providerResourceIdentityId: operation.context.providerResourceIdentityId });
      if (!window.open) this.throwUnavailable('JANELA_FECHADA');
    }
    return operation;
  }

  async initialOptions(conversationId: string, buId: string): Promise<readonly InitialChannelOption[]> {
    const conversation = await this.prisma.conversation.findFirst({ where: { id: conversationId, buId }, select: { id: true } });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const candidates = await this.whatsAppChannels(buId);
    if (candidates.length > 2) throw new BadRequestException({ code: 'INITIAL_CHANNEL_OPTIONS_LIMIT' });
    const preflight = this.classifyWhatsAppCandidates(candidates);
    const preflightEligible = (candidate: Candidate & { type: 'OFICIAL' | 'NAO_OFICIAL' }) => preflight.get(candidate.id) === null;
    const credentialState = await this.credentials.inspectActiveCredentials(candidates
      .filter((candidate) => candidate.type === 'OFICIAL' && preflightEligible(candidate))
      .map(({ id, generation, buId: candidateBuId }) => ({ channelId: id, generation, provider: 'OFICIAL' as const, buId: candidateBuId })));
    const windowRefs = candidates.flatMap((candidate) => {
      if (!preflightEligible(candidate)) return [];
      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      return identity && this.policies.get(candidate.type).requiresWindow
        ? [{ conversationId, providerResourceIdentityId: identity.id, origin: candidate.type }]
        : [];
    });
    const windows = windowRefs.length ? await this.policies.inspectMany(windowRefs) : new Map<string, OfficialWindowState>();
    return candidates.map((candidate) => {
      const policy = this.policies.get(candidate.type);
      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      const window = identity ? windows.get(this.policies.key({ conversationId, providerResourceIdentityId: identity.id }))
        ?? { open: !policy.requiresWindow, expiresAt: null } : { open: false, expiresAt: null };
      const metadata = candidate.type === 'OFICIAL' ? credentialState.get(candidate.id) : { version: null, ready: true, expiresAt: null };
      const readiness = preflight.get(candidate.id) ?? this.candidateReadiness(candidate, metadata);
      const supportedKinds = (['text', 'approved-template'] as const).filter((kind) =>
        policy.evaluate({ operation: 'INITIAL', humanActor: true, kind, inboundWindowOpen: true }).eligible);
      const textEligibility = policy.evaluate({ operation: 'INITIAL', humanActor: true, kind: 'text', inboundWindowOpen: window.open });
      const templateEligibility = policy.evaluate({ operation: 'INITIAL', humanActor: true, kind: 'approved-template', inboundWindowOpen: true });
      const availability = {
        text: readiness ?? (textEligibility.eligible ? null : policy.requiresWindow && !window.open
          ? (window.expiresAt ? 'JANELA_FECHADA' : 'WINDOW_UNQUALIFIED') : textEligibility.reason),
        'approved-template': readiness ?? (templateEligibility.eligible ? null : templateEligibility.reason),
      };
      return {
        id: candidate.id, type: candidate.type, generation: candidate.generation, pairingEpoch: candidate.pairingEpoch,
        activeCredentialVersion: metadata?.version ?? null, supportedKinds, availability,
        ...(window.expiresAt ? { windowExpiresAt: window.expiresAt } : {}),
      };
    });
  }

  async resolveForIngress(reference: VerifiedIngressChannelReference): Promise<ResolvedChannelOperation> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true, contact: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    const candidate = await this.findCandidate(reference.channelId, reference.buId);
    const identity = candidate?.providerIdentities.find((item) => item.id === reference.providerResourceIdentityId);
    if (!candidate || candidate.type !== reference.channelOrigin || candidate.generation !== reference.generation
      || candidate.pairingEpoch !== reference.pairingEpoch || !identity || identity.buId !== reference.buId
      || identity.provider !== reference.channelOrigin || identity.currentChannelId !== reference.channelId
      || !identity.managedLifecycle) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    return this.bind(candidate, conversation.id);
  }

  async hasReadyChannelForNewConversation(buId: string): Promise<boolean> {
    const candidates = await this.whatsAppChannels(buId);
    if (candidates.length > 2) return false;
    const preflight = this.classifyWhatsAppCandidates(candidates);
    for (const candidate of candidates) {
      if (preflight.get(candidate.id) !== null) continue;
      if (!await this.inspectCandidate(candidate)) return true;
    }
    return false;
  }

  async inspectForConversation(reference: ConversationChannelReference): Promise<ChannelAvailability> {
    try {
      const conversation = await this.prisma.conversation.findFirst({
        where: { id: reference.conversationId, buId: reference.buId }, select: { id: true },
      });
      if (!conversation) return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
      const { candidate, selectionReason, selectedOrigin } = await this.selectCandidate(reference);
      if (!candidate) {
        return this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL');
      }
      let reason: ChannelAvailability['reason'] = await this.inspectCandidate(candidate);

      const currentIdentity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      const window = !reason && currentIdentity
        ? await this.policies.get(candidate.type).inspect({ conversationId: reference.conversationId, providerResourceIdentityId: currentIdentity.id })
        : { open: false, expiresAt: null };
      if (!reason && this.policies.get(candidate.type).requiresWindow && !window.open) reason = 'JANELA_FECHADA';
      return {
        available: reason === null,
        reason,
        channelOrigin: candidate.type,
        requiresWindow: this.policies.get(candidate.type).requiresWindow,
        windowOpen: window.open,
        expiresAt: window.expiresAt,
      };
    } catch {
      return this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL');
    }
  }

  /** Batch-only GET view: BU bindings and credential metadata are read once for the page. */
  async inspectManyForConversations(references: readonly ConversationAvailabilityReference[]): Promise<Map<string, ChannelAvailability>> {
    if (!references.length) return new Map();
    if (references.length > 50) throw new BadRequestException({ code: 'CHANNEL_AVAILABILITY_PAGE_LIMIT' });
    const buId = references[0].buId;
    if (references.some((reference) => reference.buId !== buId)) {
      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
    }
    try {
      const ids = references.map(({ conversationId }) => conversationId);
      const routes = await this.prisma.conversationRoute.findMany({ where: { conversationId: { in: ids }, buId },
        select: { conversationId: true, businessIdentityId: true, platform: true, businessScopeReference: true } });
      const channels = await this.channelsForBusinessIdentities(buId, [...new Set(routes.map(({ businessIdentityId }) => businessIdentityId))]);
      const selectedById = new Map<string, {
        candidate: Candidate | null;
        selectedOrigin: ChannelOrigin | null;
        selectionReason: ChannelAvailability['reason'] | null;
        route: (typeof routes)[number] | null;
      }>();
      for (const reference of references) {
        let selectedOrigin = reference.latestMessageOrigin;
        const conversationRoutes = routes.filter((route) => route.conversationId === reference.conversationId);
        const routedCandidates = channels.filter((item) => conversationRoutes.some((route) =>
          route.businessIdentityId === item.businessIdentityId
          && (route.platform === 'INSTAGRAM' ? item.type === 'INSTAGRAM' : item.type !== 'INSTAGRAM')));
        let candidate: Candidate | null = null;
        let selectedRoute: typeof routes[number] | null = null;
        let selectionReason: ChannelAvailability['reason'] | null = null;
        if (selectedOrigin) {
          const matches = routedCandidates.filter((item) => item.type === selectedOrigin
            && (!reference.latestProviderResourceIdentityId || item.providerIdentities.some((identity) => identity.id === reference.latestProviderResourceIdentityId)));
          if (matches.length > 1) selectionReason = 'CANAL_AMBIGUO';
          else {
            candidate = matches[0] ?? null;
            selectedRoute = conversationRoutes.find((route) => route.businessIdentityId === candidate?.businessIdentityId
              && (route.platform === 'INSTAGRAM' ? candidate?.type === 'INSTAGRAM' : candidate?.type !== 'INSTAGRAM')) ?? null;
            if (!candidate) selectionReason = 'CANAL_SELECIONADO_INDISPONIVEL';
            else if (!selectedRoute) selectionReason = 'CANAL_SELECIONADO_INDISPONIVEL';
          }
        } else if (routedCandidates.length === 0) {
          candidate = null; selectionReason = 'CANAL_AUSENTE';
        } else {
          if (routedCandidates.length > 1) selectionReason = 'CANAL_AMBIGUO';
          else {
            candidate = routedCandidates[0] ?? null;
            selectedOrigin = candidate?.type ?? null;
            selectedRoute = conversationRoutes.find((route) => route.businessIdentityId === candidate?.businessIdentityId
              && (route.platform === 'INSTAGRAM' ? candidate?.type === 'INSTAGRAM' : candidate?.type !== 'INSTAGRAM')) ?? null;
            if (!candidate || !selectedRoute) selectionReason = 'CANAL_SELECIONADO_INDISPONIVEL';
          }
        }
        if (candidate && selectedRoute) selectionReason = this.candidateAssociationReason(candidate, selectedRoute) ?? selectionReason;
        selectedById.set(reference.conversationId, { candidate, selectedOrigin, selectionReason, route: selectedRoute });
      }
      const eligibleCandidates = [...new Map([...selectedById.values()]
        .filter(({ candidate, selectionReason }) => candidate && !selectionReason)
        .map(({ candidate }) => [candidate!.id, candidate!])).values()];
      const credentialState = await this.credentials.inspectActiveCredentials(eligibleCandidates
        .filter((candidate) => candidate.type === 'OFICIAL' || candidate.type === 'INSTAGRAM')
        .map(({ id, generation, type, buId: candidateBuId }) => ({ channelId: id, generation, provider: type, buId: candidateBuId })));
      const windowRefs = references.flatMap(({ conversationId }) => {
        const selected = selectedById.get(conversationId);
        const candidate = selected?.candidate;
        const identity = candidate?.providerIdentities.find((item) => item.currentChannelId === candidate.id);
        return candidate && !selected?.selectionReason && this.policies.get(candidate.type).requiresWindow && identity
          ? [{ conversationId, providerResourceIdentityId: identity.id, origin: candidate.type }]
          : [];
      });
      const windows = windowRefs.length ? await this.policies.inspectMany(windowRefs) : new Map<string, OfficialWindowState>();
      const result = new Map<string, ChannelAvailability>();
      for (const id of ids) {
        const { candidate, selectedOrigin, selectionReason } = selectedById.get(id)!;
        if (!candidate) {
          result.set(id, this.unavailable(selectedOrigin, selectionReason ?? 'CANAL_SELECIONADO_INDISPONIVEL'));
          continue;
        }
        let reason: ChannelAvailability['reason'] = null;
        reason = selectionReason ?? this.candidateReadiness(candidate, credentialState.get(candidate.id));
        let windowOpen = true;
        let expiresAt: Date | null = null;
        const identityForWindow = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      if (!reason && this.policies.get(candidate.type).requiresWindow) {
          const state = identityForWindow ? windows.get(this.policies.key({ conversationId: id, providerResourceIdentityId: identityForWindow.id })) : undefined;
          windowOpen = state?.open ?? false;
          expiresAt = state?.expiresAt ?? null;
          if (!reason && !windowOpen) reason = 'JANELA_FECHADA';
        }
        result.set(id, {
          available: reason === null, reason, channelOrigin: candidate.type,
          requiresWindow: this.policies.get(candidate.type).requiresWindow, windowOpen, expiresAt,
        });
      }
      return result;
    } catch {
      return new Map(references.map(({ conversationId }) => [conversationId, this.unavailable(null, 'CANAL_SELECIONADO_INDISPONIVEL')]));
    }
  }

  /** One server-owned, metadata-only reply-options projection for the selected conversation. */
  async replyOptions(conversationId: string, buId: string): Promise<ChannelReplyOptions> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: conversationId, buId }, select: { id: true, buId: true, displayName: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const routes = await this.prisma.conversationRoute.findMany({
        where: { conversationId, buId }, include: { contactIdentity: true, businessIdentity: true },
        orderBy: [{ createdAt: 'asc' }, { id: 'asc' }],
      });
    const channels = await this.channelsForBusinessIdentities(buId, [...new Set(routes.map(({ businessIdentityId }) => businessIdentityId))]);
    const candidatesByRoute = new Map<string, Candidate[]>();
    const reasonsByRoute = new Map<string, Map<string, ChannelAvailability['reason']>>();
    const identityByRoute = new Map<string, Candidate['providerIdentities'][number]>();
    for (const route of routes) {
      if (!route.contactIdentity || !route.businessIdentity) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      const routeCandidates = channels.filter((candidate) => candidate.businessIdentityId === route.businessIdentityId
        && (route.platform === 'INSTAGRAM' ? candidate.type === 'INSTAGRAM' : candidate.type !== 'INSTAGRAM'));
      const counts = new Map<string, number>();
      for (const candidate of routeCandidates) counts.set(candidate.type, (counts.get(candidate.type) ?? 0) + 1);
      candidatesByRoute.set(route.id, routeCandidates);
      const reasons = new Map<string, ChannelAvailability['reason']>();
      for (const candidate of routeCandidates) {
        const identities = candidate.providerIdentities.filter((item) => item.currentChannelId === candidate.id);
        if (identities.length !== 1) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
        identityByRoute.set(`${route.id}:${candidate.id}`, identities[0]);
        const association = this.candidateAssociationReason(candidate, route);
        reasons.set(candidate.id, (counts.get(candidate.type) ?? 0) > 1 ? 'CANAL_AMBIGUO' : association);
      }
      reasonsByRoute.set(route.id, reasons);
    }
    const eligibleCandidates = routes.flatMap((route) => (candidatesByRoute.get(route.id) ?? [])
      .filter((candidate) => !reasonsByRoute.get(route.id)?.get(candidate.id)));
    const channelIds = [...new Set(routes.flatMap((route) => (candidatesByRoute.get(route.id) ?? []).map(({ id }) => id)))];
    const credentials = await this.credentials.inspectActiveCredentials(eligibleCandidates
      .filter((candidate) => candidate.type === 'OFICIAL' || candidate.type === 'INSTAGRAM')
      .map(({ id, generation, type, buId: candidateBuId }) => ({ channelId: id, generation, provider: type, buId: candidateBuId })));
    const pairs = routes.flatMap((route) => (candidatesByRoute.get(route.id) ?? []).flatMap((candidate) => {
      if (reasonsByRoute.get(route.id)?.get(candidate.id)) return [];
      const identity = identityByRoute.get(`${route.id}:${candidate.id}`);
      return identity ? [{ conversationId, providerResourceIdentityId: identity.id, origin: candidate.type }] : [];
    }));
    const windows = await this.policies.inspectMany(pairs);
    const instagramChannelIds = channelIds.filter((id) => channels.some((candidate) => candidate.id === id && candidate.type === 'INSTAGRAM'));
    const usernameRows = instagramChannelIds.length ? await this.prisma.$queryRaw<Array<{ channel_id: string; username: string | null }>>`
      SELECT DISTINCT ON (channel_id) channel_id, username
      FROM instagram_authorization_attempts
      WHERE channel_id IN (${Prisma.join(instagramChannelIds)})
      ORDER BY channel_id, created_at DESC, id DESC
    ` : [];
    const usernames = new Map(usernameRows.map((row) => [row.channel_id, row.username]));
    const options: ChannelReplyOptions['options'][number][] = [];
    for (const route of routes) {
      const routeChannels = candidatesByRoute.get(route.id) ?? [];
      for (const candidate of routeChannels) {
        const identity = identityByRoute.get(`${route.id}:${candidate.id}`)!;
        const metadata = candidate.type === 'NAO_OFICIAL'
          ? { version: null, ready: true, expiresAt: null }
          : credentials.get(candidate.id) ?? { version: null, ready: false, expiresAt: null };
        const policy = this.policies.get(candidate.type);
        const window = windows.get(this.policies.key({ conversationId, providerResourceIdentityId: identity.id }))
          ?? { open: !policy.requiresWindow, expiresAt: null };
        const readiness = reasonsByRoute.get(route.id)?.get(candidate.id) ?? this.candidateReadiness(candidate, metadata);
        const ready = readiness === null;
        const available = ready && (!policy.requiresWindow || window.open);
        const context: ChannelOperationContext = {
          schemaVersion: 2, buId, conversationId, contactId: route.contactId,
          contactIdentityId: route.contactIdentityId, routeId: route.id, channelId: candidate.id,
          businessIdentityId: route.businessIdentityId, providerResourceIdentityId: identity.id,
          adapterOrigin: candidate.type, generation: candidate.generation, pairingEpoch: candidate.pairingEpoch,
          activeCredentialVersion: metadata.version,
          providerAccountReference: candidate.type === 'OFICIAL' && candidate.wabaId
            ? metaAccountReference(candidate.wabaId) : candidate.type === 'INSTAGRAM' ? identity.externalResourceId : null,
        };
        const instagram = candidate.type === 'INSTAGRAM';
        options.push({
          schemaVersion: 2, routeId: route.id, channelId: candidate.id, channelOrigin: candidate.type,
          generation: candidate.generation, contextFingerprint: channelContextFingerprint(context),
          accountLabel: instagram ? (usernames.get(candidate.id) ? `Instagram @${usernames.get(candidate.id)}` : 'Instagram')
            : candidate.type === 'OFICIAL' ? `WhatsApp ${candidate.wabaId ?? 'Oficial'}` : 'WhatsApp',
          recipientLabel: conversation.displayName || (instagram ? 'Contato do Instagram' : route.contactIdentity.externalPeerId),
          supportedKinds: ['text'], policy: instagram ? 'INSTAGRAM_24H' : candidate.type === 'OFICIAL' ? 'OFFICIAL_WINDOW' : 'EVOLUTION',
          available, reason: available ? 'AVAILABLE' : ready
            ? (!window.expiresAt ? 'WINDOW_UNQUALIFIED' : 'WINDOW_CLOSED') : readiness ?? 'CHANNEL_NOT_READY',
          requiresWindow: policy.requiresWindow, windowOpen: window.open, windowExpiresAt: window.expiresAt,
        });
      }
    }
    return { schemaVersion: 2, options };
  }

  async contextAfterDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
    try {
      const status = await this.contextStatus(context, false);
      return status;
    } catch {
      return 'UNKNOWN';
    }
  }

  async contextBeforeDispatch(context: ChannelOperationContext): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
    try {
      return await this.contextStatus(context, true);
    } catch {
      return 'UNKNOWN';
    }
  }

  async validateOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
    expectedCredentialExpiresAt: Date | null,
    expectedRecipientRef?: string,
  ): Promise<boolean> {
    const selected = parseChannelOperationContextV2(selectedValue);
    if (!selected || canonicalV2(selected) !== canonicalV2(expected)) return false;

    // Pin mutable readiness/bindings without waiting after identity acquisition.
    // ST-05 observation refresh takes channel/credential locks before identity;
    // NOWAIT keeps this established identity-first path finite and cycle-safe.
    const businessUnits = await tx.$queryRaw<Array<{ id: string }>>`
      SELECT id FROM business_units WHERE id = ${expected.buId} AND status = 'ATIVO' FOR SHARE NOWAIT`;
    if (!businessUnits[0]) return false;
    const channelPins = await tx.$queryRaw<Array<{ id: string }>>`
      SELECT id FROM bu_channels WHERE id = ${expected.channelId} AND bu_id = ${expected.buId} FOR SHARE NOWAIT`;
    if (!channelPins[0]) return false;
    if (expected.adapterOrigin !== 'NAO_OFICIAL') {
      const credentialPins = await tx.$queryRaw<Array<{ channel_id: string }>>`
        SELECT channel_id FROM channel_credentials WHERE channel_id = ${expected.channelId} FOR SHARE NOWAIT`;
      if (!credentialPins[0]) return false;
      const credentialState = await this.credentials.inspectActiveCredential(expected.channelId, expected.generation,
        { provider: expected.adapterOrigin, buId: expected.buId }, tx);
      if (!credentialState.ready || credentialState.version !== expected.activeCredentialVersion
        || (credentialState.expiresAt?.getTime() ?? null) !== (expectedCredentialExpiresAt?.getTime() ?? null)) return false;
    }

    const identity = await tx.providerResourceIdentity.findFirst({
      where: {
        id: expected.providerResourceIdentityId,
        buId: expected.buId,
        provider: expected.adapterOrigin,
        currentChannelId: expected.channelId,
        managedLifecycle: true,
      },
      select: { id: true, externalResourceId: true, businessIdentityId: true },
    });
    if (!identity || identity.businessIdentityId !== expected.businessIdentityId) return false;

    const channel = await tx.buChannel.findFirst({
      where: {
        id: expected.channelId,
        buId: expected.buId,
        type: expected.adapterOrigin,
        generation: expected.generation,
        pairingEpoch: expected.pairingEpoch,
        ownNumberVerified: true,
        verifiedEpoch: expected.pairingEpoch,
        status: 'CONECTADO',
        receiptVerifiedAt: { not: null },
        providerConnectionState: expected.adapterOrigin === 'NAO_OFICIAL' ? 'CONNECTED'
          : expected.adapterOrigin === 'INSTAGRAM' ? { in: ['SUBSCRIBED', 'SUBSCRIBED_PENDING_RECEIPT'] } : 'SUBSCRIBED',
      },
      select: {
        status: true,
        providerConnectionState: true,
        receiptVerifiedAt: true,
        wabaId: true,
        phoneNumberId: true,
        evolutionInstanceName: true,
        credential: { select: { generation: true, version: true, expiresAt: true } },
      },
    });
    const providerResource = expected.adapterOrigin === 'OFICIAL' ? channel?.phoneNumberId
      : expected.adapterOrigin === 'NAO_OFICIAL' ? channel?.evolutionInstanceName : identity?.externalResourceId;
    const route = await tx.conversationRoute.findFirst({ where: { id: expected.routeId, conversationId: expected.conversationId,
      buId: expected.buId, contactId: expected.contactId, contactIdentityId: expected.contactIdentityId,
      businessIdentityId: expected.businessIdentityId }, include: { contactIdentity: true, businessIdentity: true } });
    if (!channel || !hasChannelProviderReadiness({ provider: expected.adapterOrigin, status: channel.status,
      providerConnectionState: channel.providerConnectionState, receiptVerifiedAt: channel.receiptVerifiedAt })
      || !route || providerResource !== identity.externalResourceId
      || route.platform !== (expected.adapterOrigin === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP')
      || route.contactIdentity.id !== expected.contactIdentityId || route.contactIdentity.contactId !== expected.contactId
      || route.contactIdentity.buId !== expected.buId || route.contactIdentity.platform !== route.platform
      || route.contactIdentity.scopeReference !== route.contactScopeReference || !route.contactIdentity.externalPeerId
      || (expectedRecipientRef !== undefined && route.contactIdentity.externalPeerId !== expectedRecipientRef)
      || route.businessIdentity.id !== expected.businessIdentityId || route.businessIdentity.buId !== expected.buId
      || route.businessIdentity.platform !== route.platform || route.businessIdentity.scopeReference !== route.businessScopeReference
      || (route.platform === 'WHATSAPP' ? route.businessIdentity.namespace !== 'WHATSAPP_RESOURCE'
        || route.businessIdentity.scopeReference !== 'BU' : route.businessIdentity.namespace !== 'INSTAGRAM_LOGIN')
      || (channel.wabaId ? metaAccountReference(channel.wabaId) : expected.adapterOrigin === 'INSTAGRAM' ? identity.externalResourceId : null) !== expected.providerAccountReference) return false;
    if (expected.adapterOrigin !== 'NAO_OFICIAL' && (!channel.credential
      || channel.credential.generation !== expected.generation
      || channel.credential.version !== expected.activeCredentialVersion
      || (channel.credential.expiresAt?.getTime() ?? null) !== (expectedCredentialExpiresAt?.getTime() ?? null))) return false;
    if (expected.adapterOrigin === 'INSTAGRAM') {
      const clock = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
      if (!clock[0]?.now || !channel.credential?.expiresAt
        || channel.credential.expiresAt.getTime() <= clock[0].now.getTime() + 60_000) return false;
    }
    return true;
  }

  async validateAcceptedOperationContextInTransaction(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
  ): Promise<boolean> {
    const selected = parseChannelOperationContextV2(selectedValue);
    if (!selected || canonicalV2(selected) !== canonicalV2(expected)) return false;
    const [businessUnit, identity, channel] = await Promise.all([
      tx.businessUnit.findFirst({ where: { id: expected.buId, status: 'ATIVO' }, select: { id: true } }),
      tx.providerResourceIdentity.findFirst({ where: {
        id: expected.providerResourceIdentityId, buId: expected.buId, provider: expected.adapterOrigin,
        currentChannelId: expected.channelId, managedLifecycle: true,
      }, select: { id: true, externalResourceId: true, businessIdentityId: true } }),
      tx.buChannel.findFirst({ where: {
        id: expected.channelId, buId: expected.buId, type: expected.adapterOrigin,
        generation: expected.generation, pairingEpoch: expected.pairingEpoch,
        ownNumberVerified: true, verifiedEpoch: expected.pairingEpoch,
      }, select: { wabaId: true, phoneNumberId: true, evolutionInstanceName: true } }),
    ]);
    const route = await tx.conversationRoute.findFirst({ where: { id: expected.routeId, conversationId: expected.conversationId,
      buId: expected.buId, contactId: expected.contactId, contactIdentityId: expected.contactIdentityId,
      businessIdentityId: expected.businessIdentityId }, include: { contactIdentity: true, businessIdentity: true } });
    if (!businessUnit || !identity || !channel || !route || identity.businessIdentityId !== expected.businessIdentityId) return false;
    if (route.platform !== (expected.adapterOrigin === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP')
      || route.contactIdentity.id !== expected.contactIdentityId || route.contactIdentity.contactId !== expected.contactId
      || route.contactIdentity.buId !== expected.buId || route.contactIdentity.platform !== route.platform
      || route.contactIdentity.scopeReference !== route.contactScopeReference || !route.contactIdentity.externalPeerId
      || route.businessIdentity.id !== expected.businessIdentityId || route.businessIdentity.buId !== expected.buId
      || route.businessIdentity.platform !== route.platform || route.businessIdentity.scopeReference !== route.businessScopeReference
      || (route.platform === 'WHATSAPP' ? route.businessIdentity.namespace !== 'WHATSAPP_RESOURCE'
        || route.businessIdentity.scopeReference !== 'BU' : route.businessIdentity.namespace !== 'INSTAGRAM_LOGIN')) return false;
    const providerResource = expected.adapterOrigin === 'OFICIAL' ? channel.phoneNumberId
      : expected.adapterOrigin === 'NAO_OFICIAL' ? channel.evolutionInstanceName : identity.externalResourceId;
    return providerResource === identity.externalResourceId
      && (channel.wabaId ? metaAccountReference(channel.wabaId) : expected.adapterOrigin === 'INSTAGRAM' ? identity.externalResourceId : null) === expected.providerAccountReference;
  }

  async validateLegacyAcceptedContextInTransaction(tx: Prisma.TransactionClient,
    expected: LegacyChannelOperationContextV1, selectedValue: Prisma.JsonValue): Promise<boolean> {
    const selected = parseLegacyChannelOperationContextV1(selectedValue);
    if (!selected || ['channelId', 'buId', 'channelOrigin', 'providerResourceIdentityId', 'generation', 'pairingEpoch',
      'activeCredentialVersion', 'requiresWindow', 'providerAccountReference'].some((key) =>
      selected[key as keyof LegacyChannelOperationContextV1] !== expected[key as keyof LegacyChannelOperationContextV1])) return false;
    const [identity, channel] = await Promise.all([
      tx.providerResourceIdentity.findFirst({ where: { id: expected.providerResourceIdentityId, buId: expected.buId,
        provider: expected.channelOrigin, currentChannelId: expected.channelId, managedLifecycle: true },
        select: { id: true, externalResourceId: true } }),
      tx.buChannel.findFirst({ where: { id: expected.channelId, buId: expected.buId, type: expected.channelOrigin,
        generation: expected.generation, pairingEpoch: expected.pairingEpoch },
        select: { wabaId: true, phoneNumberId: true, evolutionInstanceName: true, requiresWindow: true } }),
    ]);
    if (!identity || !channel || channel.requiresWindow !== expected.requiresWindow) return false;
    const resourceId = expected.channelOrigin === 'OFICIAL' ? channel.phoneNumberId : channel.evolutionInstanceName;
    return identity.externalResourceId === resourceId
      && (channel.wabaId ? metaAccountReference(channel.wabaId) : null) === expected.providerAccountReference;
  }

  private async bind(candidate: Candidate, conversationId: string, selectedRouteId?: string): Promise<ResolvedChannelOperation> {
    const availability = await this.inspectCandidate(candidate);
    if (availability) this.throwUnavailable(availability);
    const credential = await this.credentials.resolve(candidate.id);
    const route = await this.prisma.conversationRoute.findFirst({ where: {
      conversationId, buId: candidate.buId, businessIdentityId: candidate.businessIdentityId ?? undefined,
      ...(selectedRouteId ? { id: selectedRouteId } : {}),
    }, include: { contactIdentity: true, businessIdentity: true } });
    if (!route || !route.contactIdentity || !route.businessIdentity || route.businessIdentityId !== candidate.businessIdentityId) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    const context: ChannelOperationContext = Object.freeze({
      schemaVersion: 2,
      channelId: candidate.id,
      buId: candidate.buId,
      conversationId,
      contactId: route.contactId,
      contactIdentityId: route.contactIdentityId,
      routeId: route.id,
      businessIdentityId: route.businessIdentityId,
      providerResourceIdentityId: credential.providerResourceIdentityId,
      adapterOrigin: candidate.type,
      generation: credential.generation,
      pairingEpoch: credential.pairingEpoch,
      activeCredentialVersion: credential.activeCredentialVersion,
      providerAccountReference: credential.wabaId ? metaAccountReference(credential.wabaId)
        : candidate.type === 'INSTAGRAM' ? credential.instagramAccountId ?? null : null,
    });
    if (!this.sameCredentialContext(candidate, credential)) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    const factory = this.adapters.get(candidate.type);
    if (!factory) throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
    const channel = factory.create(credential, async () => {
      try { return (await this.contextStatus(context, true)) === 'CURRENT'; }
      catch { return false; }
    });
    return { channel, context, eligibilityPolicy: this.policies.get(candidate.type), credentialExpiresAt: credential.expiresAt ?? null };
  }

  /** A route is established only after an explicit initial-channel selection and canonical peer proof. */
  private async ensureExplicitWhatsAppInitialRoute(
    conversation: { id: string; buId: string; contactId: string; contactType: string },
    candidate: Candidate,
  ): Promise<string> {
    const businessIdentityId = candidate.businessIdentityId;
    if (candidate.type === 'INSTAGRAM' || !businessIdentityId) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    const providerIdentity = candidate.providerIdentities.find((identity) => identity.currentChannelId === candidate.id
      && identity.buId === candidate.buId && identity.provider === candidate.type
      && identity.businessIdentityId === businessIdentityId && identity.managedLifecycle);
    if (!providerIdentity) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    return this.prisma.$transaction(async (tx) => {
      const locked = await tx.$queryRaw<Array<{ id: string; bu_id: string; contact_id: string; contact_type: string }>>`
        SELECT id, bu_id, contact_id, contact_type::text AS contact_type
        FROM conversations WHERE id = ${conversation.id} AND bu_id = ${conversation.buId} FOR UPDATE`;
      const row = locked[0];
      if (!row || row.contact_id !== conversation.contactId
        || row.contact_type !== conversation.contactType) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      const namespace = row.contact_type === 'PESSOA' ? 'PERSON' : row.contact_type === 'GRUPO' ? 'GROUP' : null;
      if (!namespace) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      const [contactIdentity, businessIdentity] = await Promise.all([
        tx.contactIdentity.findMany({ where: {
          contactId: row.contact_id, buId: row.bu_id, platform: 'WHATSAPP',
          namespace, scopeReference: 'BU',
        }, select: { id: true, contactId: true, buId: true, platform: true, namespace: true, scopeReference: true, externalPeerId: true } }),
        tx.businessChannelIdentity.findFirst({ where: {
          id: businessIdentityId, buId: row.bu_id, platform: 'WHATSAPP',
          namespace: 'WHATSAPP_RESOURCE', scopeReference: 'BU',
        }, select: { id: true, buId: true, platform: true, namespace: true, scopeReference: true } }),
      ]);
      if (contactIdentity.length !== 1 || !businessIdentity || businessIdentity.id !== providerIdentity.businessIdentityId) {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      }
      const selectedContactIdentity = contactIdentity[0];
      if (selectedContactIdentity.contactId !== row.contact_id || selectedContactIdentity.buId !== row.bu_id
        || selectedContactIdentity.platform !== 'WHATSAPP' || selectedContactIdentity.namespace !== namespace
        || selectedContactIdentity.scopeReference !== 'BU' || !selectedContactIdentity.externalPeerId) {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      }
      if (namespace === 'PERSON') {
        try {
          if (normalizeWhatsAppPersonPeer(selectedContactIdentity.externalPeerId) !== selectedContactIdentity.externalPeerId) {
            throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
          }
        } catch { throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' }); }
      }
      const existingForBusiness = await tx.conversationRoute.findFirst({ where: {
        conversationId: row.id, buId: row.bu_id, businessIdentityId: businessIdentity.id, platform: 'WHATSAPP',
      }, select: { id: true, contactIdentityId: true } });
      if (existingForBusiness && existingForBusiness.contactIdentityId !== selectedContactIdentity.id) {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      }
      const existing = await tx.conversationRoute.findFirst({ where: {
        conversationId: row.id, buId: row.bu_id, contactId: row.contact_id,
        contactIdentityId: selectedContactIdentity.id, businessIdentityId: businessIdentity.id,
        platform: 'WHATSAPP', contactScopeReference: selectedContactIdentity.scopeReference,
        businessScopeReference: businessIdentity.scopeReference,
      }, select: { id: true } });
      if (existing) return existing.id;
      await tx.conversationRoute.createMany({ data: [{
        buId: row.bu_id, conversationId: row.id, contactId: row.contact_id,
        contactIdentityId: selectedContactIdentity.id, platform: 'WHATSAPP',
        contactScopeReference: selectedContactIdentity.scopeReference,
        businessScopeReference: businessIdentity.scopeReference, businessIdentityId: businessIdentity.id,
      }], skipDuplicates: true });
      const route = await tx.conversationRoute.findFirst({ where: {
        conversationId: row.id, buId: row.bu_id, contactId: row.contact_id,
        contactIdentityId: selectedContactIdentity.id, businessIdentityId: businessIdentity.id,
        platform: 'WHATSAPP', contactScopeReference: selectedContactIdentity.scopeReference,
        businessScopeReference: businessIdentity.scopeReference,
      }, select: { id: true } });
      if (!route) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      return route.id;
    }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
  }

  private async inspectCandidate(candidate: Candidate): Promise<ChannelAvailability['reason']> {
    const metadata = candidate.type === 'OFICIAL' || candidate.type === 'INSTAGRAM'
      ? await this.credentials.inspectActiveCredential(candidate.id, candidate.generation, { provider: candidate.type, buId: candidate.buId })
      : undefined;
    return this.candidateReadiness(candidate, metadata);
  }

  private candidateReadiness(
    candidate: Candidate,
    metadata?: { readonly version: number | null; readonly ready: boolean; readonly expiresAt: Date | null },
  ): ChannelAvailability['reason'] {
    const identities = candidate.providerIdentities.filter((item) => item.currentChannelId === candidate.id);
    if (identities.length > 1) return 'CANAL_AMBIGUO';
    const identity = identities[0];
    const business = candidate.businessIdentity;
    if (!candidate.ownNumberVerified || candidate.verifiedEpoch !== candidate.pairingEpoch || !identity
      || !identity.managedLifecycle || identity.provider !== candidate.type || identity.buId !== candidate.buId
      || !candidate.businessIdentityId || identity.businessIdentityId !== candidate.businessIdentityId) {
      return 'CHANNEL_IDENTITY_NOT_VERIFIED';
    }
    const expectedPlatform = candidate.type === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP';
    const expectedNamespace = candidate.type === 'INSTAGRAM' ? 'INSTAGRAM_LOGIN' : 'WHATSAPP_RESOURCE';
    if (!business || business.id !== candidate.businessIdentityId || business.buId !== candidate.buId
      || business.platform !== expectedPlatform || business.namespace !== expectedNamespace
      || (candidate.type !== 'INSTAGRAM' && business.scopeReference !== 'BU') || !business.externalResourceId
      || (candidate.type === 'INSTAGRAM' && business.externalResourceId !== identity.externalResourceId)) return 'CANAL_AMBIGUO';
    if (!hasChannelProviderReadiness({ provider: candidate.type, status: candidate.status,
      providerConnectionState: candidate.providerConnectionState, receiptVerifiedAt: candidate.receiptVerifiedAt })
      || !this.adapters.locallyConfigured(candidate.type)) return 'CHANNEL_NOT_READY';
    if ((candidate.type === 'OFICIAL' && (!candidate.wabaId || !candidate.phoneNumberId
        || identity.externalResourceId !== candidate.phoneNumberId))
      || (candidate.type === 'NAO_OFICIAL' && (!candidate.evolutionInstanceName
        || identity.externalResourceId !== candidate.evolutionInstanceName))
      || (candidate.type === 'INSTAGRAM' && !identity.externalResourceId)) {
      return 'CHANNEL_IDENTITY_NOT_VERIFIED';
    }
    if ((candidate.type === 'OFICIAL' || candidate.type === 'INSTAGRAM') && !metadata?.ready) {
      return 'PENDING_CREDENTIAL';
    }
    return null;
  }

  private async selectForConversation(reference: ConversationChannelReference) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: reference.conversationId, buId: reference.buId },
      select: { id: true, buId: true, contact: true },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    const { candidate, selectionReason } = await this.selectCandidate(reference);
    if (!candidate) this.throwUnavailable(selectionReason ?? 'CANAL_AUSENTE');
    const reason = await this.inspectCandidate(candidate);
    if (reason) this.throwUnavailable(reason);
    if (this.policies.get(candidate.type).requiresWindow) {
      const identity = candidate.providerIdentities.find((item) => item.currentChannelId === candidate.id);
      const window = identity
        ? await this.policies.get(candidate.type).inspect({ conversationId: conversation.id, providerResourceIdentityId: identity.id })
        : { open: false, expiresAt: null };
      if (!window.open) this.throwUnavailable('JANELA_FECHADA');
    }
    return { conversation, candidate };
  }

  private async selectCandidate(reference: ConversationChannelReference): Promise<{
    candidate: Candidate | null; selectedOrigin: ChannelOrigin | null; selectionReason: ChannelAvailability['reason'] | null;
  }> {
    if (reference.routeId || reference.channelId) {
      if (!reference.routeId || !reference.channelId) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_SELECIONADO_INDISPONIVEL' };
      const route = await this.prisma.conversationRoute.findFirst({ where: {
        id: reference.routeId, conversationId: reference.conversationId, buId: reference.buId,
      }, select: { businessIdentityId: true, platform: true, businessScopeReference: true } });
      if (!route) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_SELECIONADO_INDISPONIVEL' };
      const candidate = await this.findCandidate(reference.channelId, reference.buId, route.businessIdentityId);
      if (!candidate || route.platform !== (candidate.type === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP')
        || (reference.expectedGeneration !== undefined && candidate.generation !== reference.expectedGeneration)) {
        return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_SELECIONADO_INDISPONIVEL' };
      }
      const association = this.candidateAssociationReason(candidate, route);
      if (association) return { candidate: null, selectedOrigin: candidate.type, selectionReason: association };
      return { candidate, selectedOrigin: candidate.type, selectionReason: null };
    }
    const latest = await this.prisma.message.findFirst({
      where: { conversationId: reference.conversationId },
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
      select: { channelOrigin: true, providerResourceIdentityId: true },
    });
    const routes = await this.prisma.conversationRoute.findMany({ where: { conversationId: reference.conversationId, buId: reference.buId },
      select: { businessIdentityId: true, platform: true, businessScopeReference: true } });
    const routeBusinessIds = new Set(routes.map((route) => route.businessIdentityId));
    const channels = await this.channelsForBusinessIdentities(reference.buId, [...routeBusinessIds]);
    if (latest) {
      const matches = channels.filter((channel) => channel.type === latest.channelOrigin && routeBusinessIds.has(channel.businessIdentityId ?? '')
        && channel.providerIdentities.some((identity) => identity.id === latest.providerResourceIdentityId));
      if (matches.length > 1) return { candidate: null, selectedOrigin: latest.channelOrigin as ChannelOrigin, selectionReason: 'CANAL_AMBIGUO' };
      const candidate = matches[0] ?? null;
      const route = routes.find((item) => item.businessIdentityId === candidate?.businessIdentityId
        && item.platform === (candidate?.type === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP'));
      if (candidate && route) {
        const association = this.candidateAssociationReason(candidate, route);
        if (association) return { candidate: null, selectedOrigin: candidate.type, selectionReason: association };
      }
      const selectedOrigin = candidate?.type ?? latest.channelOrigin as ChannelOrigin;
      return { candidate, selectedOrigin, selectionReason: candidate && route ? null : 'CANAL_SELECIONADO_INDISPONIVEL' };
    }
    const routed = channels.filter((channel) => routes.some((route) => route.businessIdentityId === channel.businessIdentityId
      && route.platform === (channel.type === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP')));
    if (routed.length === 0) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AUSENTE' };
    if (routed.length > 1) return { candidate: null, selectedOrigin: null, selectionReason: 'CANAL_AMBIGUO' };
    const candidate = routed[0];
    const route = routes.find((item) => item.businessIdentityId === candidate.businessIdentityId
      && item.platform === (candidate.type === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP'));
    const association = route ? this.candidateAssociationReason(candidate, route) : 'CANAL_SELECIONADO_INDISPONIVEL';
    return { candidate: association ? null : candidate, selectedOrigin: candidate.type, selectionReason: association };
  }

  private async channelsForBusinessIdentities(buId: string, businessIdentityIds: readonly string[]): Promise<Candidate[]> {
    if (!businessIdentityIds.length) return [];
    return this.prisma.buChannel.findMany({
      where: { buId, businessIdentityId: { in: [...new Set(businessIdentityIds)] } },
      select: {
        id: true, buId: true, type: true, businessIdentityId: true, wabaId: true, phoneNumberId: true, evolutionInstanceName: true, status: true, generation: true, pairingEpoch: true,
        businessIdentity: { select: { id: true, buId: true, platform: true, namespace: true, scopeReference: true, externalResourceId: true } },
        verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
        receiptVerifiedAt: true, requiresWindow: true,
        providerIdentities: { select: { id: true, buId: true, provider: true, externalResourceId: true, currentChannelId: true, businessIdentityId: true, managedLifecycle: true } },
      },
    }) as unknown as Promise<Candidate[]>;
  }

  private async whatsAppChannels(buId: string): Promise<Array<Candidate & { type: 'OFICIAL' | 'NAO_OFICIAL' }>> {
    return this.prisma.buChannel.findMany({ where: { buId, type: { in: ['OFICIAL', 'NAO_OFICIAL'] } }, take: 3, select: {
      id: true, buId: true, type: true, businessIdentityId: true, wabaId: true, phoneNumberId: true, evolutionInstanceName: true, status: true, generation: true, pairingEpoch: true,
      businessIdentity: { select: { id: true, buId: true, platform: true, namespace: true, scopeReference: true, externalResourceId: true } },
      verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
      receiptVerifiedAt: true, requiresWindow: true,
      providerIdentities: { select: { id: true, buId: true, provider: true, externalResourceId: true, currentChannelId: true, businessIdentityId: true, managedLifecycle: true } },
    } }) as unknown as Promise<Array<Candidate & { type: 'OFICIAL' | 'NAO_OFICIAL' }>>;
  }

  private classifyWhatsAppCandidates(
    candidates: readonly (Candidate & { type: 'OFICIAL' | 'NAO_OFICIAL' })[],
  ): Map<string, ChannelAvailability['reason']> {
    const typeCounts = new Map<string, number>();
    for (const candidate of candidates) typeCounts.set(candidate.type, (typeCounts.get(candidate.type) ?? 0) + 1);
    const owners = new Set(candidates.map(({ businessIdentityId }) => businessIdentityId).filter((id): id is string => Boolean(id)));
    return new Map(candidates.map((candidate) => {
      if (typeCounts.get(candidate.type)! > 1 || owners.size > 1) return [candidate.id, 'CANAL_AMBIGUO'] as const;
      if (!candidate.businessIdentityId) return [candidate.id, 'CHANNEL_IDENTITY_NOT_VERIFIED'] as const;
      const business = candidate.businessIdentity;
      const identities = candidate.providerIdentities.filter((item) => item.currentChannelId === candidate.id);
      const identity = identities[0];
      const resourceId = candidate.type === 'OFICIAL' ? candidate.phoneNumberId : candidate.evolutionInstanceName;
      if (!business || business.id !== candidate.businessIdentityId || business.buId !== candidate.buId
        || business.platform !== 'WHATSAPP' || business.namespace !== 'WHATSAPP_RESOURCE'
        || business.scopeReference !== 'BU' || !business.externalResourceId || identities.length !== 1
        || !identity || identity.buId !== candidate.buId || identity.provider !== candidate.type
        || identity.businessIdentityId !== candidate.businessIdentityId || !identity.managedLifecycle
        || !resourceId || identity.externalResourceId !== resourceId) {
        return [candidate.id, 'CANAL_AMBIGUO'] as const;
      }
      return [candidate.id, null] as const;
    }));
  }

  private async findCandidate(channelId: string, buId: string, businessIdentityId?: string): Promise<Candidate | null> {
    const rows = await this.prisma.buChannel.findMany({ where: { id: channelId, buId,
      ...(businessIdentityId ? { businessIdentityId } : {}) }, select: {
      id: true, buId: true, type: true, businessIdentityId: true, wabaId: true, phoneNumberId: true, evolutionInstanceName: true, status: true, generation: true, pairingEpoch: true,
      businessIdentity: { select: { id: true, buId: true, platform: true, namespace: true, scopeReference: true, externalResourceId: true } },
      verifiedEpoch: true, ownNumberVerified: true, providerConnectionState: true,
      receiptVerifiedAt: true, requiresWindow: true,
      providerIdentities: { select: { id: true, buId: true, provider: true, externalResourceId: true, currentChannelId: true, businessIdentityId: true, managedLifecycle: true } },
    } });
    return (rows[0] as unknown as Candidate | undefined) ?? null;
  }

  private candidateAssociationReason(
    candidate: Candidate,
    route: { businessIdentityId: string; platform: string; businessScopeReference: string },
  ): ChannelAvailability['reason'] | null {
    if (!candidate.businessIdentityId) return 'CHANNEL_IDENTITY_NOT_VERIFIED';
    const business = candidate.businessIdentity;
    const identities = candidate.providerIdentities.filter((item) => item.currentChannelId === candidate.id);
    if (!business || business.id !== candidate.businessIdentityId || business.id !== route.businessIdentityId
      || business.buId !== candidate.buId || business.platform !== route.platform
      || business.scopeReference !== route.businessScopeReference || !business.externalResourceId
      || identities.length !== 1) return 'CANAL_AMBIGUO';
    const identity = identities[0];
    const expectedPlatform = candidate.type === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP';
    const expectedNamespace = candidate.type === 'INSTAGRAM' ? 'INSTAGRAM_LOGIN' : 'WHATSAPP_RESOURCE';
    const resourceId = candidate.type === 'OFICIAL' ? candidate.phoneNumberId
      : candidate.type === 'NAO_OFICIAL' ? candidate.evolutionInstanceName : identity.externalResourceId;
    if (route.platform !== expectedPlatform || business.namespace !== expectedNamespace
      || (candidate.type !== 'INSTAGRAM' && business.scopeReference !== 'BU')
      || identity.buId !== candidate.buId || identity.provider !== candidate.type
      || identity.currentChannelId !== candidate.id || identity.businessIdentityId !== candidate.businessIdentityId
      || !identity.managedLifecycle || !resourceId || identity.externalResourceId !== resourceId) return 'CANAL_AMBIGUO';
    if (candidate.type === 'INSTAGRAM' && business.externalResourceId !== identity.externalResourceId) return 'CANAL_AMBIGUO';
    return null;
  }

  private async contextStatus(context: ChannelOperationContext, beforeDispatch: boolean): Promise<'CURRENT' | 'CHANGED' | 'UNKNOWN'> {
    const where: Prisma.BuChannelWhereInput = {
      id: context.channelId, buId: context.buId, type: context.adapterOrigin,
      generation: context.generation, pairingEpoch: context.pairingEpoch,
      ...(context.adapterOrigin !== 'INSTAGRAM' ? { ownNumberVerified: true, verifiedEpoch: context.pairingEpoch } : {}),
      ...(beforeDispatch ? {
        status: 'CONECTADO', receiptVerifiedAt: { not: null },
        providerConnectionState: context.adapterOrigin === 'NAO_OFICIAL' ? 'CONNECTED'
          : context.adapterOrigin === 'INSTAGRAM' ? { in: ['SUBSCRIBED', 'SUBSCRIBED_PENDING_RECEIPT'] } : 'SUBSCRIBED',
      } : {}),
    };
    const channel = await this.prisma.buChannel.findFirst({
      where,
      select: { id: true, businessIdentityId: true, wabaId: true, status: true, providerConnectionState: true,
        receiptVerifiedAt: true,
        ...(beforeDispatch ? { credential: { select: { version: true, generation: true, expiresAt: true } } } : {}),
        providerIdentities: { where: { id: context.providerResourceIdentityId }, select: { id: true, buId: true, provider: true, externalResourceId: true, currentChannelId: true, businessIdentityId: true, managedLifecycle: true } } },
    });
    const identity = channel?.providerIdentities[0];
    const route = await this.prisma.conversationRoute.findFirst({ where: { id: context.routeId, conversationId: context.conversationId,
      buId: context.buId, contactId: context.contactId, contactIdentityId: context.contactIdentityId,
      businessIdentityId: context.businessIdentityId }, include: { contactIdentity: true, businessIdentity: true } });
    if (!channel || (beforeDispatch && !hasChannelProviderReadiness({ provider: context.adapterOrigin, status: channel.status,
      providerConnectionState: channel.providerConnectionState, receiptVerifiedAt: channel.receiptVerifiedAt }))
      || !identity || !route || channel.businessIdentityId !== context.businessIdentityId
      || identity.buId !== context.buId || identity.provider !== context.adapterOrigin
      || identity.currentChannelId !== context.channelId || identity.businessIdentityId !== context.businessIdentityId || !identity.managedLifecycle
      || route.platform !== (context.adapterOrigin === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP')
      || route.contactIdentity.id !== context.contactIdentityId || route.contactIdentity.contactId !== context.contactId
      || route.contactIdentity.buId !== context.buId || route.contactIdentity.platform !== route.platform
      || route.contactIdentity.scopeReference !== route.contactScopeReference || !route.contactIdentity.externalPeerId
      || route.businessIdentity.id !== context.businessIdentityId || route.businessIdentity.buId !== context.buId
      || route.businessIdentity.platform !== route.platform || route.businessIdentity.scopeReference !== route.businessScopeReference) {
      return 'CHANGED';
    }
    const currentAccountReference = channel.wabaId ? metaAccountReference(channel.wabaId)
      : context.adapterOrigin === 'INSTAGRAM' ? identity.externalResourceId : null;
    if (currentAccountReference !== context.providerAccountReference) return 'CHANGED';
    if (beforeDispatch && context.adapterOrigin !== 'NAO_OFICIAL') {
      const credential = channel.credential;
      if (!credential || credential.generation !== context.generation || credential.version !== context.activeCredentialVersion) return 'CHANGED';
      if (context.adapterOrigin === 'INSTAGRAM') {
        const clock = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
        if (!credential.expiresAt || !clock[0]?.now || credential.expiresAt.getTime() <= clock[0].now.getTime() + 60_000) return 'CHANGED';
      }
    }
    return 'CURRENT';
  }

  private sameCredentialContext(candidate: Candidate, credential: ResolvedChannelCredential): boolean {
    if (!candidate.businessIdentityId || !credential.businessIdentityId) return false;
    const identity = candidate.providerIdentities.find((item) => item.id === credential.providerResourceIdentityId);
    return credential.channelId === candidate.id && credential.buId === candidate.buId
      && credential.provider === candidate.type && credential.generation === candidate.generation
      && (credential.wabaId ? metaAccountReference(credential.wabaId) : null) === (candidate.wabaId ? metaAccountReference(candidate.wabaId) : null)
      && credential.pairingEpoch === candidate.pairingEpoch && identity?.currentChannelId === candidate.id
      && identity?.buId === candidate.buId && identity.provider === candidate.type
      && identity.businessIdentityId === candidate.businessIdentityId
      && credential.businessIdentityId === candidate.businessIdentityId
      && identity.externalResourceId === credential.externalResourceId;
  }

  private unavailable(channelOrigin: ChannelOrigin | null, reason: ChannelAvailability['reason']): ChannelAvailability {
    return { available: false, reason, channelOrigin, requiresWindow: false, windowOpen: false, expiresAt: null };
  }

  private throwUnavailable(reason: ChannelAvailability['reason']): never {
    if (reason === 'CANAL_AUSENTE') throw new BadRequestException({ code: reason, error: 'Esta BU não tem canal conectado.' });
    if (reason === 'CANAL_AMBIGUO') throw new ConflictException({ code: reason, error: 'Selecione uma origem de conversa antes de responder.' });
    throw new ConflictException({ code: reason, error: reason === 'JANELA_FECHADA'
      ? 'Fora da janela de 24h da última mensagem recebida.'
      : 'O canal selecionado não está disponível para envio.' });
  }
}

```

## Complete current source api-app/src/domain/inbox/outbound.service.ts
```
import { BadRequestException, ConflictException, HttpException, Injectable, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type InitialMessageIntent } from '@prisma/client';
import { randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { ChannelResolver, parseStoredChannelOperationContext, type ChannelMessage, type ChannelOperationContext, type ChannelOrigin, type InitialChannelReference, type ResolvedChannelOperation, type VerifiedIngressChannelReference } from '../channels/transport/channel';
import type { ChannelSendResult } from '../channels/transport/channel';
import { MessageAcceptanceService, type MessageAcceptanceInput } from './message-acceptance.service';
import { resolveContactIdentityAddress, type ContactIdentityAddress } from './contact-identity';
import { DispatchAdmissionService, type DispatchClaimEligibility } from './dispatch-admission.service';
import { RealtimeService } from '../../realtime/realtime.service';
import type { ChannelEligibilityPolicy, ChannelOperationKind } from './channel-eligibility-policy';

const FIXED_UNKNOWN = 'Resultado do envio não confirmado; confira a conversa antes de tentar novamente.';
const FIXED_LOCAL_INCOMPLETE = 'O canal aceitou o envio, mas a conclusão local não foi confirmada; confira a conversa antes de tentar novamente.';
const FIXED_REJECTED = 'O canal recusou o envio.';
type OutboundConversation = Prisma.ConversationGetPayload<object>;

type InitialConversationSnapshot = Pick<OutboundConversation, 'updatedAt' | 'status' | 'attendantUserId' | 'attendantName' | 'attendantOrigin'>;
type InitialActorFence = (tx: Prisma.TransactionClient) => Promise<boolean>;

export type OutboundAttribution =
  | { kind: 'BFF'; userId: string; name: string }
  | { kind: 'PUBLIC'; name: string }
  | { kind: 'BOT'; name: string };

export interface SendOutboundInput {
  conversationId: string;
  buId: string;
  text: string;
  attribution: OutboundAttribution;
  ingress?: Omit<VerifiedIngressChannelReference, 'conversationId' | 'buId'>;
  routeSelection?: { routeId: string; channelId: string; expectedGeneration: number; contextFingerprint: string };
  /** Fresh server-owned BFF session and grant check; required for human dispatch. */
  validateActorInTransaction?: InitialActorFence;
}

@Injectable()
export class OutboundService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly resolver: ChannelResolver,
    private readonly acceptance: MessageAcceptanceService,
    private readonly realtime: RealtimeService,
    private readonly admissions: DispatchAdmissionService,
  ) {}

  async prepareInitial(reference: InitialChannelReference): Promise<ResolvedChannelOperation> {
    return this.resolver.resolveForInitial(reference);
  }

  async recipientForOperation(context: ChannelOperationContext): Promise<string> {
    const address = await this.contactAddressForOperation(context);
    return address.externalPeerId;
  }

  private async contactAddressForOperation(context: ChannelOperationContext): Promise<ContactIdentityAddress> {
    const address = await resolveContactIdentityAddress(this.prisma, context);
    if (!address) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    return address;
  }

  async initialOptions(conversationId: string, buId: string) {
    return this.resolver.initialOptions(conversationId, buId);
  }

  /** Local-only completion of a separately persisted known Meta/Evolution receipt. */
  async reconcileInitial(input: {
    readonly intent: InitialMessageIntent;
    readonly actorId: string;
    readonly actorName: string;
    readonly validateActorInTransaction: InitialActorFence;
  }) {
    const intent = input.intent;
    if (!intent.externalMessageId || !['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) return null;
    const storedContext = parseStoredChannelOperationContext(intent.selectedContext);
    const context = storedContext?.context ?? null;
    const acceptedOrigin = storedContext ? (storedContext.version === 1 ? storedContext.context.channelOrigin : storedContext.context.adapterOrigin) : null;
    const stored = this.initialRequestRecord(intent.request);
    const canonicalRequest = stored?.canonicalRequest;
    const renderedText = stored?.renderedText;
    const original = this.originalConversationSnapshot(stored?.originalConversation);
    const originalActorName = stored?.originalActorName;
    if (!storedContext || !context || acceptedOrigin === 'INSTAGRAM' || !original || typeof renderedText !== 'string' || !renderedText || typeof originalActorName !== 'string' || !originalActorName) {
      await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(intent.id, 'RECORDED');
    }
    const conversation = await this.prisma.conversation.findFirst({ where: { id: intent.conversationId, buId: intent.buId } });
    if (!conversation || !canonicalRequest || typeof canonicalRequest !== 'object' || Array.isArray(canonicalRequest)) {
      throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    }
    const contactAddress = storedContext.version === 2
      ? await this.recipientForOperation(storedContext.context)
      : conversation.contact;
    const acceptanceInput: MessageAcceptanceInput = {
      externalMessageId: intent.externalMessageId, providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId, generation: context.generation, pairingEpoch: context.pairingEpoch,
      buId: context.buId, channelOrigin: acceptedOrigin as 'OFICIAL' | 'NAO_OFICIAL', contact: contactAddress,
      contactType: conversation.contactType, conversationId: conversation.id, direction: 'OUT', messageType: 'TEXTO',
      content: renderedText, authorUserId: intent.actorId, authorName: originalActorName, senderResult: true,
    };
    const complete = (tx: Prisma.TransactionClient) => this.acceptance.acceptInTransaction(tx, acceptanceInput,
      async (transaction, priorExists) => {
        const validContext = storedContext.version === 1
          ? await this.resolver.validateLegacyAcceptedContextInTransaction(transaction, storedContext.context, intent.selectedContext)
          : await this.resolver.validateAcceptedOperationContextInTransaction(transaction, storedContext.context, intent.selectedContext);
        if (!validContext) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
        if (!await input.validateActorInTransaction(transaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        await this.finalizeInitialInTransaction(transaction, {
          conversationId: conversation.id, buId: conversation.buId, intent, ownerNonce: intent.ownerNonce,
          originalConversation: original, actorId: intent.actorId, actorName: originalActorName,
          conversation, externalMessageId: intent.externalMessageId!, priorExists,
        });
      });
    try {
      const accepted = await this.prisma.$transaction(complete, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (accepted.creationWinner) {
        try {
          this.realtime.publicarNaBu(conversation.buId, {
            tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
            direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
          });
        } catch { /* Durable local completion is authoritative; realtime is best effort. */ }
      }
      return accepted.message;
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        const prior = await this.findConfirmedOutbound({ providerResourceIdentityId: context.providerResourceIdentityId, externalMessageId: intent.externalMessageId, conversationId: conversation.id, buId: conversation.buId, contact: contactAddress, channelOrigin: acceptedOrigin as ChannelOrigin,
          ...(storedContext.version === 2 ? { routeContext: storedContext.context } : {}) });
        if (prior) {
          try {
            const retried = await this.prisma.$transaction(complete, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
            if (retried.creationWinner) {
              try {
                this.realtime.publicarNaBu(conversation.buId, {
                  tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
                  direcao: 'OUT', canal: retried.message.channelOrigin, naoLidas: retried.conversation.unreadCount,
                });
              } catch { /* Durable local completion is authoritative; realtime is best effort. */ }
            }
            return retried.message;
          } catch {
            await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
            throw this.initialLocalIncomplete(intent.id, 'RECORDED');
          }
        }
      } else {
        const message = await this.findConfirmedOutbound({ providerResourceIdentityId: context.providerResourceIdentityId, externalMessageId: intent.externalMessageId, conversationId: conversation.id, buId: conversation.buId, contact: contactAddress, channelOrigin: acceptedOrigin as ChannelOrigin,
          ...(storedContext.version === 2 ? { routeContext: storedContext.context } : {}) });
        const current = await this.admissions.getInitialForScopedAttempt({ id: intent.id, conversationId: intent.conversationId, buId: intent.buId }).catch(() => null);
        if (message && current?.state === 'SUCCEEDED' && current.externalMessageId === intent.externalMessageId) return message;
      }
      await this.admissions.markInitialLocalBlocked({ id: intent.id, ownerNonce: intent.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(intent.id, 'RECORDED');
    }
  }

  /** Dispatches one already-reserved initial intent through the common channel and Message owners. */
  async sendInitial(input: {
    readonly conversationId: string;
    readonly buId: string;
    readonly channelId: string;
    readonly kind: ChannelMessage['kind'];
    readonly intent: Pick<InitialMessageIntent, 'id' | 'selectedContext' | 'leaseExpiresAt'>;
    readonly ownerNonce: string;
    readonly operation: ResolvedChannelOperation;
    readonly payload: ChannelMessage;
    readonly request: Prisma.InputJsonValue;
    readonly originalConversation: InitialConversationSnapshot;
    readonly actorId: string;
    readonly actorName: string;
    readonly validateActorInTransaction: InitialActorFence;
  }) {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: input.conversationId, buId: input.buId },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    let operation: ResolvedChannelOperation;
    try {
      operation = await this.resolver.resolveForInitial({
        conversationId: conversation.id, buId: conversation.buId, channelId: input.channelId, kind: input.kind,
      });
    } catch (error) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
      throw error;
    }
    if (!sameContext(operation.context, input.operation.context)) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
    }
    let selectedPeer: string;
    try { selectedPeer = await this.recipientForOperation(operation.context); }
    catch (error) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
      throw error;
    }
    if (input.payload.recipientRef !== selectedPeer) {
      await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
    }

    let claimed = false;
    let dispatchAuthorized = false;
    type InitialClaimOutcome = 'NOT_ATTEMPTED' | 'CLAIMED' | 'NOT_CLAIMED' | 'UNKNOWN';
    const claimStatus: { value: InitialClaimOutcome } = { value: 'NOT_ATTEMPTED' };
    const claimOutcome = (): InitialClaimOutcome => claimStatus.value;
    const dispatchDeadlineAt = input.intent.leaseExpiresAt;
    let claimPromise: Promise<boolean> | null = null;
    const beforeDispatch = async () => {
      if (!claimPromise) {
        claimPromise = this.admissions.claimInitial({
          id: input.intent.id,
          ownerNonce: input.ownerNonce,
          validate: async (tx, selectedContext, request) => {
            if (canonicalJson(request) !== canonicalJson(input.request)) return { eligible: false, windowExpiresAt: null, credentialExpiresAt: null };
            const eligibility = await this.validateDispatchContext(tx, operation.context, selectedContext, conversation.id, operation.eligibilityPolicy, { operation: 'INITIAL', humanActor: true, kind: input.kind }, input.kind === 'text', selectedPeer, operation.credentialExpiresAt);
            if (!eligibility.eligible || !await input.validateActorInTransaction(tx)) {
              return { ...eligibility, eligible: false };
            }
            return eligibility;
          },
        }).then((value) => { claimStatus.value = value ? 'CLAIMED' : 'NOT_CLAIMED'; return value; }, () => { claimStatus.value = 'UNKNOWN'; return false; });
      }
      claimed = await claimPromise;
      if (!claimed) return false;
      dispatchAuthorized = await this.finalProviderFence(operation.context, operation.eligibilityPolicy, conversation.id,
        dispatchDeadlineAt, operation.credentialExpiresAt, input.kind === 'text', input.validateActorInTransaction);
      return dispatchAuthorized;
    };

    let result: ChannelSendResult;
    try {
      result = await operation.channel.sendMessage(input.payload, { purpose: 'initial', beforeDispatch });
    } catch {
      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
    }
    if (claimed && !dispatchAuthorized && result.outcome !== 'BLOCKED') {
      result = { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }

    if (result.outcome === 'BLOCKED') {
      if (claimOutcome() === 'NOT_ATTEMPTED' || claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'CLAIMED' && dispatchAuthorized) await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'CLAIMED') await this.admissions.rejectInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw this.blocked(result.reason);
    }
    if (result.outcome === 'REJECTED') {
      if (claimOutcome() === 'NOT_ATTEMPTED' || claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'CLAIMED') await this.admissions.rejectInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
    }
    if (result.outcome === 'UNKNOWN') {
      if (!claimed) {
        if (claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
        else if (claimOutcome() === 'UNKNOWN') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
        throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_UNCONFIRMED', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
      }
      let classified = false;
      try {
        classified = await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      } catch { /* a lost write acknowledgment needs a positive scoped readback */ }
      if (!classified) {
        const persisted = await this.admissions.getInitialForScopedAttempt({
          id: input.intent.id, conversationId: input.conversationId, buId: input.buId,
        }).catch(() => null);
        classified = persisted?.ownerNonce === input.ownerNonce && persisted.state === 'AMBIGUOUS'
          && persisted.slotReleasedAt === null;
      }
      if (!classified) {
        throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_UNCONFIRMED', outcome: 'UNKNOWN', attemptId: input.intent.id, error: FIXED_UNKNOWN });
      }
      throw new ConflictException({ code: 'INITIAL_SEND_AMBIGUOUS', outcome: 'AMBIGUOUS', state: 'AMBIGUOUS', attemptId: input.intent.id, error: FIXED_UNKNOWN });
    }
    if (!claimed) {
      if (claimOutcome() === 'NOT_CLAIMED') await this.admissions.rejectPreparedInitial({ id: input.intent.id, ownerNonce: input.ownerNonce });
      else if (claimOutcome() === 'UNKNOWN') await this.admissions.markInitialAmbiguous({ id: input.intent.id, ownerNonce: input.ownerNonce });
      throw new ServiceUnavailableException({ code: 'INITIAL_DISPATCH_FENCE_MISSING', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
    }

    let receipt: boolean;
    try {
      receipt = await this.admissions.recordInitialExternalAccepted({
        id: input.intent.id, ownerNonce: input.ownerNonce, externalMessageId: result.externalMessageId,
      });
    } catch {
      const exact = await this.admissions.getInitialForScopedAttempt({
        id: input.intent.id, conversationId: input.conversationId, buId: input.buId,
      }).catch(() => null);
      receipt = exact?.ownerNonce === input.ownerNonce && exact.externalMessageId === result.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(exact.state);
        if (!receipt) throw this.initialLocalIncomplete(input.intent.id, 'UNCONFIRMED', 'INITIAL_RECEIPT_UNCONFIRMED');
    }
    if (!receipt) {
      await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
      throw this.initialLocalIncomplete(input.intent.id, 'UNCONFIRMED', 'INITIAL_RECEIPT_UNCONFIRMED');
    }

    const acceptanceInput = this.initialAcceptanceInput(input, conversation, operation.context, selectedPeer, result.externalMessageId);
    const completeInitial = async (transaction: Prisma.TransactionClient, priorExists: boolean) => {
      const valid = await this.resolver.validateAcceptedOperationContextInTransaction(transaction, operation.context, input.intent.selectedContext);
      if (!valid) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      if (!await input.validateActorInTransaction(transaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
      await this.finalizeInitialInTransaction(transaction, {
        ...input, conversation, externalMessageId: result.externalMessageId, priorExists,
      });
    };
    let accepted: Awaited<ReturnType<MessageAcceptanceService['acceptInTransaction']>>;
    try {
      accepted = await this.prisma.$transaction(async (tx) => this.acceptance.acceptInTransaction(
        tx,
        acceptanceInput,
        completeInitial,
      ), { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        const prior = await this.findConfirmedOutbound({
          providerResourceIdentityId: operation.context.providerResourceIdentityId,
          externalMessageId: result.externalMessageId,
          conversationId: conversation.id, buId: conversation.buId,
          contact: selectedPeer, channelOrigin: operation.context.adapterOrigin,
          routeContext: operation.context,
        }).catch(() => null);
        if (prior) {
          try {
            accepted = await this.prisma.$transaction(async (tx) => this.acceptance.acceptInTransaction(
              tx,
              acceptanceInput,
              completeInitial,
            ), { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
          } catch {
            await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
            throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
          }
        } else {
          await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
          throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
        }
      } else {
        const message = await this.readBack(conversation, operation.context, selectedPeer, result.externalMessageId).catch(() => null);
        if (message) {
          const row = await this.admissions.getInitialForScopedAttempt({
            id: input.intent.id, conversationId: conversation.id, buId: conversation.buId,
          }).catch(() => null);
          if (row?.state === 'SUCCEEDED' && row.externalMessageId === result.externalMessageId) {
            return message;
          }
        }
        await this.admissions.markInitialLocalBlocked({ id: input.intent.id, ownerNonce: input.ownerNonce }).catch(() => false);
        throw this.initialLocalIncomplete(input.intent.id, 'RECORDED');
      }
    }

    if (accepted.creationWinner) {
      try {
        this.realtime.publicarNaBu(conversation.buId, {
          tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
          direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
        });
      } catch { /* Message commit is authoritative; realtime is best effort. */ }
    }
    return accepted.message;
  }

  async send(input: SendOutboundInput) {
    if (input.attribution.kind === 'BFF' && !input.validateActorInTransaction) {
      throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    }
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: input.conversationId, buId: input.buId },
    });
    if (!conversation) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });

    let operation: ResolvedChannelOperation;
    try {
      operation = input.ingress
        ? await this.resolver.resolveForIngress({
            conversationId: conversation.id, buId: conversation.buId, ...input.ingress,
          })
        : await this.resolver.resolveForConversation({ conversationId: conversation.id, buId: conversation.buId, ...input.routeSelection });
    } catch (error) {
      if (error instanceof HttpException) throw this.asBlocked(error);
      throw error;
    }

    const window = await operation.eligibilityPolicy.inspect({ conversationId: conversation.id, providerResourceIdentityId: operation.context.providerResourceIdentityId });
    const policy = operation.eligibilityPolicy.evaluate({ operation: 'REPLY',
      humanActor: input.attribution.kind === 'BFF', inboundWindowOpen: window.open,
      kind: operation.channel.supportedKinds.includes('text') ? 'text' : 'approved-template' });
    if (!policy.eligible) {
      if (policy.reason === 'HUMAN_REPLY_REQUIRED') throw new ConflictException({ code: 'INSTAGRAM_HUMAN_REPLY_ONLY', outcome: 'BLOCKED' });
      throw new ConflictException({ code: 'JANELA_FECHADA', outcome: 'BLOCKED', error: 'Fora da janela de 24h da última mensagem recebida.' });
    }
    const contactAddress = await this.contactAddressForOperation(operation.context);
    const recipientRef = contactAddress.externalPeerId;

    const attribution = input.attribution;
    const actorId = attribution.kind === 'BFF' ? attribution.userId
      : attribution.kind === 'PUBLIC' ? `public:${conversation.buId}`
        : `bot:${attribution.name}`;
    const reservation = await this.admissions.reserveOrdinary({
      conversationId: conversation.id,
      buId: conversation.buId,
      caller: attribution.kind,
      actorId,
      ownerNonce: randomUUID(),
      selectedContext: operation.context as unknown as Prisma.InputJsonValue,
    });
    let claimed = false;
    let dispatchAuthorized = false;
    const dispatchDeadlineAt = reservation.admission.expiresAt;
    let claimPromise: Promise<boolean> | null = null;
    const beforeDispatch = async () => {
      if (!claimPromise) {
        claimPromise = this.admissions.claimOrdinary({
          id: reservation.admission.id,
          ownerNonce: reservation.ownerNonce,
          validate: async (tx, selectedContext) => {
            const eligibility = await this.validateDispatchContext(
              tx, operation.context, selectedContext, conversation.id, operation.eligibilityPolicy,
              { operation: 'REPLY', humanActor: input.attribution.kind === 'BFF', kind: 'text' }, true, recipientRef, operation.credentialExpiresAt,
            );
            if (!eligibility.eligible || input.attribution.kind !== 'BFF') return eligibility;
            if (!input.validateActorInTransaction || !await input.validateActorInTransaction(tx)) {
              return { ...eligibility, eligible: false };
            }
            return eligibility;
          },
        });
      }
      claimed = await claimPromise;
      if (!claimed) return false;
      dispatchAuthorized = await this.finalProviderFence(operation.context, operation.eligibilityPolicy, conversation.id,
        dispatchDeadlineAt, operation.credentialExpiresAt, true,
        input.attribution.kind === 'BFF' ? input.validateActorInTransaction : undefined);
      return dispatchAuthorized;
    };

    let result: ChannelSendResult;
    try {
      result = await operation.channel.sendMessage(
        { kind: 'text', recipientRef, text: input.text },
        { beforeDispatch },
      );
    } catch {
      result = { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'SEND_RESULT_UNAVAILABLE' };
    }
    if (claimed && !dispatchAuthorized && result.outcome !== 'BLOCKED') {
      result = { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (result.outcome === 'BLOCKED') {
      try {
        if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
        else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      } catch { /* Preserve the established BLOCKED projection; uncertain bookkeeping retains its slot. */ }
      throw this.blocked(result.reason);
    }
    if (result.outcome === 'REJECTED') {
      try {
        if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
        else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      } catch { /* The provider refusal is definitive; uncertain bookkeeping cannot retry it. */ }
      throw new BadRequestException({ code: result.code, outcome: 'REJECTED', error: FIXED_REJECTED });
    }
    if (result.outcome === 'UNKNOWN') {
      try {
        if (claimed) await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'UNCERTAIN' });
        else await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce });
      } catch { /* Preserve the provider uncertainty and never infer a released slot. */ }
      return this.finishUnknown(input, conversation, operation.context, recipientRef, contactAddress, result);
    }
    if (!claimed) {
      // An adapter may not report acceptance unless the durable owner fence ran.
      try { await this.admissions.releasePrepared({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce }); }
      catch { /* Keep the fence failure projection; an unconfirmed reservation remains conservative. */ }
      throw new ServiceUnavailableException({ code: 'OUTBOUND_DISPATCH_FENCE_MISSING', outcome: 'UNKNOWN', error: FIXED_UNKNOWN });
    }

    const contextState = await this.contextState(operation.context);
    if (contextState !== 'CURRENT') {
      const message = await this.readBack(conversation, operation.context, recipientRef, result.externalMessageId);
      try { await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: message ? 'SETTLED' : 'UNCERTAIN' }); }
      catch { /* Keep the confirmed provider result projection below. */ }
      throw this.acceptedIncomplete(contextState, message ? 'RECORDED' : 'UNCONFIRMED');
    }

    const acceptanceInput = this.acceptanceInput(input, conversation, operation.context, recipientRef, contactAddress, result.externalMessageId);
    let accepted: Awaited<ReturnType<MessageAcceptanceService['accept']>>;
    try {
      accepted = await this.acceptance.accept(acceptanceInput);
    } catch {
      const [after, message] = await Promise.all([
        this.contextState(operation.context),
        this.readBack(conversation, operation.context, recipientRef, result.externalMessageId),
      ]);
      try { await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: message ? 'SETTLED' : 'UNCERTAIN' }); }
      catch { /* Preserve the confirmed remote ACK and local Message readback. */ }
      throw this.acceptedIncomplete(after, message ? 'RECORDED' : 'UNCONFIRMED');
    }

    let settled = false;
    try {
      settled = await this.admissions.settleOrdinary({ id: reservation.admission.id, ownerNonce: reservation.ownerNonce, state: 'SETTLED' });
    } catch {
      // The provider ACK and accepted Message are already durable; settlement uncertainty
      // must preserve that projection without retrying the provider operation.
    }
    if (!settled) throw this.acceptedIncomplete(await this.contextState(operation.context), 'RECORDED');

    let localFailure = false;
    if (accepted.creationWinner) {
      try {
        this.realtime.publicarNaBu(conversation.buId, {
          tipo: 'mensagem', conversaId: conversation.id, contato: conversation.contact,
          direcao: 'OUT', canal: accepted.message.channelOrigin, naoLidas: accepted.conversation.unreadCount,
        });
      } catch { localFailure = true; }
    }
    try {
      await this.finalizeOutbound({
        conversationId: conversation.id, buId: conversation.buId, contact: conversation.contact,
        contactType: conversation.contactType, attribution: input.attribution,
      });
    } catch { localFailure = true; }
    if (localFailure) {
      throw this.acceptedIncomplete(await this.contextState(operation.context), 'RECORDED');
    }
    return accepted.message;
  }

  private initialAcceptanceInput(
    input: { actorId: string; actorName: string; payload: ChannelMessage },
    conversation: OutboundConversation,
    context: ChannelOperationContext,
    recipientRef: string,
    externalMessageId: string,
  ): MessageAcceptanceInput {
    const content = input.payload.kind === 'text' ? input.payload.text : input.payload.template.renderedText;
    return {
      externalMessageId, providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId, generation: context.generation, pairingEpoch: context.pairingEpoch,
      buId: context.buId, channelOrigin: context.adapterOrigin, contact: recipientRef,
      contactType: conversation.contactType, conversationId: conversation.id, direction: 'OUT',
      messageType: 'TEXTO', content, authorUserId: input.actorId, authorName: input.actorName, senderResult: true,
    };
  }

  private async finalizeInitialInTransaction(
    tx: Prisma.TransactionClient,
    input: {
      conversationId: string; buId: string; intent: Pick<InitialMessageIntent, 'id'>; ownerNonce: string;
      originalConversation: InitialConversationSnapshot; actorId: string; actorName: string;
      conversation: OutboundConversation; externalMessageId: string; priorExists: boolean;
    },
  ): Promise<void> {
    const rows = await tx.$queryRaw<Array<{ id: string; updated_at: Date; status: string; attendant_user_id: string | null; attendant_name: string | null; attendant_origin: string | null }>>`
      SELECT id, updated_at, status::text AS status, attendant_user_id
        , attendant_name, attendant_origin
      FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId} FOR UPDATE
    `;
    await tx.$queryRaw`SELECT id FROM initial_message_intents WHERE id = ${input.intent.id} FOR UPDATE`;
    const intent = await tx.initialMessageIntent.findUnique({ where: { id: input.intent.id } });
    const current = rows[0];
    if (!current || !intent || intent.ownerNonce !== input.ownerNonce
      || intent.externalMessageId !== input.externalMessageId
      || !['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) {
      throw new ConflictException({ code: 'INITIAL_INTENT_CONTEXT_CHANGED' });
    }

    const original = input.originalConversation;
    const originalCas = current.updated_at.getTime() === original.updatedAt.getTime()
      && current.status === original.status && current.attendant_user_id === original.attendantUserId
      && current.attendant_name === original.attendantName && current.attendant_origin === original.attendantOrigin;
    const ownsSlot = intent.slotReleasedAt === null;
    const hasOwner = current.attendant_user_id !== null || current.attendant_name !== null || current.attendant_origin !== null;
    const canAssign = !input.priorExists && originalCas && ownsSlot && (!hasOwner || current.attendant_user_id === input.actorId);
    if (canAssign) {
      await tx.conversation.updateMany({
        where: {
          id: input.conversationId, buId: input.buId, updatedAt: original.updatedAt,
          status: original.status as InitialConversationSnapshot['status'], attendantUserId: original.attendantUserId,
          attendantName: original.attendantName, attendantOrigin: original.attendantOrigin,
        },
        data: { status: 'IN_SERVICE', attendantUserId: input.actorId, attendantName: input.actorName, attendantOrigin: 'INTERNO' },
      });
    }
    const completed = await tx.$queryRaw<Array<{ id: string }>>`
      UPDATE initial_message_intents
      SET state = 'SUCCEEDED'::"InitialMessageIntentState",
          slot_released_at = CASE WHEN slot_released_at IS NULL THEN clock_timestamp() ELSE slot_released_at END,
          updated_at = clock_timestamp()
      WHERE id = ${input.intent.id}
        AND owner_nonce = ${input.ownerNonce}
        AND external_message_id = ${input.externalMessageId}
        AND state IN ('EXTERNAL_ACCEPTED'::"InitialMessageIntentState", 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'::"InitialMessageIntentState")
        AND slot_released_at IS NOT DISTINCT FROM ${intent.slotReleasedAt}
      RETURNING id
    `;
    if (completed.length !== 1) throw new ConflictException({ code: 'INITIAL_INTENT_CONTEXT_CHANGED' });
  }

  private async finishUnknown(
    input: SendOutboundInput,
    conversation: OutboundConversation,
    context: ChannelOperationContext,
    recipientRef: string,
    contactAddress: ContactIdentityAddress,
    result: Extract<ChannelSendResult, { outcome: 'UNKNOWN' }>,
  ): Promise<never> {
    if (result.evidence === 'TRANSPORT_UNCONFIRMED') {
      const state = await this.contextState(context);
      if (state === 'CHANGED') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
      }
      throw new BadRequestException({ code: result.legacyCode, outcome: 'UNKNOWN', evidence: result.evidence, error: FIXED_UNKNOWN });
    }

    if (await this.contextState(context) === 'CHANGED') {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
    }

    try {
      await this.acceptance.recordAmbiguousOutbound(this.acceptanceInput(input, conversation, context, recipientRef, contactAddress));
    } catch {
      const state = await this.contextState(context);
      if (state === 'CHANGED') {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
      }
      throw new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'UNCONFIRMED', error: FIXED_UNKNOWN });
    }

    const state = await this.contextState(context);
    if (state === 'CHANGED') {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', diagnosticPersistence: 'RECORDED', error: FIXED_UNKNOWN });
    }
    throw new ConflictException({
      code: 'EXTERNAL_MESSAGE_ID_MISSING', outcome: 'AMBIGUOUS_SEND_RECORDED', evidence: 'ACK_WITHOUT_ID',
      diagnosticPersistence: 'RECORDED', error: 'O canal aceitou o envio sem confirmar o ID externo. Verifique a conversa antes de tentar novamente.',
    });
  }

  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
    recipientRef: string,
    contactAddress: ContactIdentityAddress,
    externalMessageId: string,
  ): MessageAcceptanceInput;
  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
    recipientRef: string,
    contactAddress: ContactIdentityAddress,
  ): Omit<MessageAcceptanceInput, 'externalMessageId'>;
  private acceptanceInput(
    input: SendOutboundInput,
    conversation: Pick<OutboundConversation, 'id' | 'buId' | 'contact' | 'contactType'>,
    context: ChannelOperationContext,
    recipientRef: string,
    contactAddress: ContactIdentityAddress,
    externalMessageId?: string,
  ): MessageAcceptanceInput | Omit<MessageAcceptanceInput, 'externalMessageId'> {
    const attribution = input.attribution;
    return {
      ...(externalMessageId ? { externalMessageId } : {}),
      providerResourceIdentityId: context.providerResourceIdentityId,
      channelId: context.channelId,
      generation: context.generation,
      pairingEpoch: context.pairingEpoch,
      buId: context.buId,
      channelOrigin: context.adapterOrigin,
      contact: recipientRef,
      contactAddress,
      contactType: conversation.contactType,
      conversationId: conversation.id,
      direction: 'OUT',
      messageType: 'TEXTO',
      content: input.text,
      authorUserId: attribution.kind === 'BFF' ? attribution.userId || null : null,
      authorName: attribution.name,
      senderResult: true,
    };
  }

  private async contextState(context: ChannelOperationContext) {
    try { return await this.resolver.contextAfterDispatch(context); }
    catch { return 'UNKNOWN' as const; }
  }

  /** Rechecks current DB-owned tuple/window after claim commit, then applies the captured deadlines immediately before provider I/O. */
  private async finalProviderFence(
    context: ChannelOperationContext,
    policy: ChannelEligibilityPolicy,
    conversationId: string,
    dispatchDeadlineAt: Date,
    credentialExpiresAt: Date | null,
    checkWindow: boolean,
    validateActorInTransaction?: InitialActorFence,
  ): Promise<boolean> {
    if (await this.resolver.contextBeforeDispatch(context) !== 'CURRENT') return false;
    const window = checkWindow
      ? await policy.inspect({ conversationId, providerResourceIdentityId: context.providerResourceIdentityId })
      : { open: true, expiresAt: null };
    // The trusted callback only uses $queryRaw; execute it as one autocommit read
    // so its post-query session check follows the last awaited database operation.
    if (validateActorInTransaction
      && !await validateActorInTransaction(this.prisma as unknown as Prisma.TransactionClient)) return false;
    const now = Date.now();
    return window.open && now < dispatchDeadlineAt.getTime()
      && (!window.expiresAt || now < window.expiresAt.getTime())
      && (!credentialExpiresAt || now + 60_000 < credentialExpiresAt.getTime());
  }

  private async validateDispatchContext(
    tx: Prisma.TransactionClient,
    expected: ChannelOperationContext,
    selectedValue: Prisma.JsonValue,
    conversationId: string,
    policy: ChannelEligibilityPolicy,
    eligibilityInput: { operation: ChannelOperationKind; humanActor: boolean; kind: ChannelMessage['kind'] },
    checkWindow = true,
    expectedRecipientRef?: string,
    expectedCredentialExpiresAt: Date | null = null,
  ): Promise<DispatchClaimEligibility> {
    const current = await this.resolver.validateOperationContextInTransaction(tx, expected, selectedValue, expectedCredentialExpiresAt, expectedRecipientRef);
    if (!current) return { eligible: false, windowExpiresAt: null, credentialExpiresAt: null };
    const window = checkWindow
      ? await policy.inspect({ conversationId, providerResourceIdentityId: expected.providerResourceIdentityId }, tx)
      : { open: true, expiresAt: null };
    const result = policy.evaluate({ ...eligibilityInput, inboundWindowOpen: window.open });
    return { eligible: result.eligible, windowExpiresAt: window.expiresAt,
      credentialExpiresAt: result.eligible ? expectedCredentialExpiresAt : null };
  }

  private initialRequestRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value) ? value as Record<string, Prisma.JsonValue> : null;
  }

  private originalConversationSnapshot(value: Prisma.JsonValue | undefined): InitialConversationSnapshot | null {
    if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
    const row = value as Record<string, Prisma.JsonValue>;
    const updatedAt = typeof row.updatedAt === 'string' ? new Date(row.updatedAt) : null;
    if (!updatedAt || !Number.isFinite(updatedAt.getTime()) || typeof row.status !== 'string'
      || row.attendantUserId !== null && typeof row.attendantUserId !== 'string'
      || row.attendantName !== null && typeof row.attendantName !== 'string'
      || row.attendantOrigin !== null && typeof row.attendantOrigin !== 'string') return null;
    return { updatedAt, status: row.status as InitialConversationSnapshot['status'],
      attendantUserId: row.attendantUserId as string | null, attendantName: row.attendantName as string | null,
      attendantOrigin: row.attendantOrigin as InitialConversationSnapshot['attendantOrigin'] };
  }

  private async readBack(
    conversation: { id: string; buId: string; contact: string },
    context: ChannelOperationContext,
    recipientRef: string,
    externalMessageId: string,
  ) {
    try {
      return await this.findConfirmedOutbound({
        providerResourceIdentityId: context.providerResourceIdentityId,
        externalMessageId, conversationId: conversation.id, buId: conversation.buId,
        contact: recipientRef, channelOrigin: context.adapterOrigin,
        routeContext: context,
      });
    } catch { return null; }
  }

  private async findConfirmedOutbound(input: {
    providerResourceIdentityId: string; externalMessageId: string; conversationId: string;
    buId: string; contact: string; channelOrigin: ChannelOrigin; routeContext?: ChannelOperationContext;
  }) {
    const message = await this.prisma.message.findUnique({
      where: { providerResourceIdentityId_externalId: {
        providerResourceIdentityId: input.providerResourceIdentityId,
        externalId: input.externalMessageId,
      } }, include: { conversation: true },
    });
    if (!message || message.direction !== 'OUT' || message.buId !== input.buId
      || message.channelOrigin !== input.channelOrigin
      || message.conversationId !== input.conversationId) return null;
    if (!input.routeContext) return message.conversation.contact === input.contact ? message : null;
    const context = input.routeContext;
    if (message.conversation.contactId !== context.contactId) return null;
    const route = await this.prisma.conversationRoute.findFirst({
      where: { id: context.routeId, conversationId: context.conversationId, buId: context.buId,
        contactId: context.contactId, contactIdentityId: context.contactIdentityId,
        businessIdentityId: context.businessIdentityId,
        platform: context.adapterOrigin === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP' },
      include: { contactIdentity: true, businessIdentity: true },
    });
    if (!route || route.contactIdentity.id !== context.contactIdentityId
      || route.contactIdentity.contactId !== context.contactId || route.contactIdentity.buId !== context.buId
      || route.contactIdentity.platform !== route.platform || route.contactIdentity.scopeReference !== route.contactScopeReference
      || route.contactIdentity.externalPeerId !== input.contact || route.businessIdentity.id !== context.businessIdentityId
      || route.businessIdentity.buId !== context.buId || route.businessIdentity.platform !== route.platform
      || route.businessIdentity.scopeReference !== route.businessScopeReference) return null;
    return message;
  }

  private async finalizeOutbound(input: {
    conversationId: string; buId: string; contact: string; contactType: 'PESSOA' | 'GRUPO'; attribution: OutboundAttribution;
  }) {
    return this.prisma.$transaction(async (tx) => {
      await tx.$queryRaw`SELECT id FROM conversations WHERE id = ${input.conversationId} AND bu_id = ${input.buId} FOR UPDATE`;
      const current = await tx.conversation.findFirst({
        where: { id: input.conversationId, buId: input.buId, contact: input.contact },
      });
      if (!current || current.contactType !== input.contactType) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
      if (input.attribution.kind === 'BOT') return current;

      const hasOwner = current.attendantUserId !== null || current.attendantName !== null || current.attendantOrigin !== null;
      return tx.conversation.update({ where: { id: current.id }, data: {
        lastMessageAt: new Date(),
        status: input.contactType === 'GRUPO' ? undefined : 'IN_SERVICE',
        ...(hasOwner || input.contactType === 'GRUPO' ? {} : input.attribution.kind === 'BFF'
          ? { attendantUserId: input.attribution.userId || null, attendantName: input.attribution.name, attendantOrigin: 'INTERNO' }
          : { attendantUserId: null, attendantName: input.attribution.name, attendantOrigin: 'EXTERNO' }),
      } });
    });
  }

  private asBlocked(error: HttpException): HttpException {
    const response = error.getResponse();
    const detail = typeof response === 'object' && response !== null ? response as Record<string, unknown> : { error: response };
    return new HttpException({ ...detail, outcome: 'BLOCKED' }, error.getStatus());
  }

  private blocked(reason: Extract<ChannelSendResult, { outcome: 'BLOCKED' }>['reason']): HttpException {
    if (reason === 'CANAL_AUSENTE') return new BadRequestException({ code: reason, outcome: 'BLOCKED', error: 'Esta BU não tem canal conectado.' });
    return new ConflictException({ code: reason, outcome: 'BLOCKED', error: 'O canal selecionado não está disponível para envio.' });
  }

  private acceptedIncomplete(contextState: 'CURRENT' | 'CHANGED' | 'UNKNOWN', localMessageState: 'RECORDED' | 'UNCONFIRMED'): HttpException {
    if (contextState === 'CHANGED') {
      return new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
    }
    return new ServiceUnavailableException({ code: 'OUTBOUND_LOCAL_INCOMPLETE', outcome: 'ACCEPTED_LOCAL_INCOMPLETE', localMessageState, error: FIXED_LOCAL_INCOMPLETE });
  }

  private initialLocalIncomplete(attemptId: string, receiptPersistence: 'RECORDED' | 'UNCONFIRMED', code = 'INITIAL_LOCAL_ACCEPTANCE_UNCONFIRMED') {
    return new ServiceUnavailableException({
      code, outcome: 'ACCEPTED_LOCAL_INCOMPLETE', attemptId, state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED',
      providerAcceptance: 'CONFIRMED', receiptPersistence,
      localMessageState: 'UNCONFIRMED', recoveryAction: 'RECONCILE', error: FIXED_LOCAL_INCOMPLETE,
    });
  }
}

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (value && typeof value === 'object') {
    const record = value as Record<string, unknown>;
    return `{${Object.keys(record).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(record[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}

function sameContext(a: ChannelOperationContext, b: ChannelOperationContext): boolean {
  return canonicalJson(a) === canonicalJson(b);
}

```

## Complete current source api-app/src/domain/inbox/dispatch-admission.service.ts
```
import { ConflictException, Injectable, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type DispatchAdmission, type InitialMessageIntent } from '@prisma/client';
import { randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { parseChannelOperationContextV2, parseStoredChannelOperationContext } from '../channels/transport/channel';
import { lockContactIdentityAddress, resolveContactIdentityAddress, whatsappPeerAddress, type ContactIdentityAddress } from './contact-identity';

const TOKEN_LEASE_MS = 90_000;

export interface DispatchClaimEligibility {
  readonly eligible: boolean;
  /** Trusted channel-window edge captured by the sole window-policy owner. */
  readonly windowExpiresAt: Date | null;
  /** Credential safety edge captured for the same immutable operation tuple. */
  readonly credentialExpiresAt: Date | null;
}

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (value && typeof value === 'object') {
    const record = value as Record<string, unknown>;
    const entries = Object.keys(record).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(record[key])}`);
    return `{${entries.join(',')}}`;
  }
  return JSON.stringify(value);
}

export function isInitialRiskAcknowledgmentEligible(
  state: InitialMessageIntent['state'], deadline: Date | null, databaseNow: Date,
): boolean {
  return (state === 'AMBIGUOUS' || state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED')
    && deadline !== null && databaseNow.getTime() >= deadline.getTime();
}

export interface ReserveOrdinaryAdmissionInput {
  conversationId: string;
  buId: string;
  caller: 'BFF' | 'PUBLIC' | 'BOT';
  actorId: string;
  ownerNonce: string;
  selectedContext: Prisma.InputJsonValue;
}

export interface ReserveInitialIntentInput {
  conversationId: string;
  buId: string;
  actorId: string;
  idempotencyKey: string;
  ownerNonce: string;
  selectedContext: Prisma.InputJsonValue;
  requestFingerprint: string;
  request: Prisma.InputJsonValue;
}

export interface InitialReplayLookup {
  conversationId: string;
  buId: string;
  actorId: string;
  idempotencyKey: string;
  requestFingerprint: string;
  selectedChannelId: string;
  expectedGeneration: number;
  ownerNonce: string;
}

@Injectable()
export class DispatchAdmissionService {
  constructor(private readonly prisma: PrismaService) {}

  /** Idempotency replay lookup happens before channel binding or provider preflight. */
  async findInitialReplay(input: InitialReplayLookup): Promise<{ intent: InitialMessageIntent; ownerNonce: string } | null> {
    const intent = await this.prisma.initialMessageIntent.findUnique({ where: {
      buId_actorId_idempotencyKey: { buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey },
    } });
    if (!intent) return null;
    if (intent.conversationId !== input.conversationId || intent.requestFingerprint !== input.requestFingerprint) {
      throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
    }
    const stored = parseStoredChannelOperationContext(intent.selectedContext);
    const context = stored?.context;
    const channelId = stored?.version === 1 ? context?.channelId : stored?.version === 2 ? context?.channelId : null;
    const generation = context?.generation ?? null;
    if (!context || channelId !== input.selectedChannelId || generation !== input.expectedGeneration) {
      throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
    }
    return { intent, ownerNonce: input.ownerNonce };
  }

  /** Create a finite owner token under the shared conversation row lock. */
  async reserveOrdinary(input: ReserveOrdinaryAdmissionInput): Promise<{ admission: DispatchAdmission; ownerNonce: string }> {
    const selected = parseChannelOperationContextV2(input.selectedContext);
    if (!selected || selected.conversationId !== input.conversationId || selected.buId !== input.buId) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    const admissionId = randomUUID();
    try {
      const admission = await this.prisma.$transaction(async (tx) => {
        const identities = await tx.$queryRaw<Array<{ id: string }>>`
          SELECT id FROM provider_resource_identities
          WHERE id = ${selected.providerResourceIdentityId} AND bu_id = ${input.buId}
            AND current_channel_id = ${selected.channelId} AND business_identity_id = ${selected.businessIdentityId}
            AND provider = ${selected.adapterOrigin}::"ChannelType" AND managed_lifecycle = TRUE
          FOR SHARE`;
        if (!identities[0]) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
        if (!await this.lockCapturedPeer(tx, selected, input.conversationId, input.buId)) {
          throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
        }
        const { now } = await this.lockConversation(tx, input.conversationId, input.buId);
        const route = await tx.conversationRoute.findFirst({ where: {
          id: selected.routeId, conversationId: input.conversationId, buId: input.buId,
          contactId: selected.contactId, contactIdentityId: selected.contactIdentityId,
          businessIdentityId: selected.businessIdentityId,
          platform: selected.adapterOrigin === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP',
        }, select: { id: true } });
        if (!route) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
        const initial = await tx.initialMessageIntent.findFirst({
          where: { conversationId: input.conversationId, slotReleasedAt: null },
          select: { id: true, state: true },
        });
        if (initial) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: initial.id, state: initial.state });
        return tx.dispatchAdmission.create({ data: {
          id: admissionId,
          conversationId: input.conversationId,
          buId: input.buId,
          caller: input.caller,
          actorId: input.actorId,
          ownerNonce: input.ownerNonce,
          selectedContext: input.selectedContext,
          state: 'PREPARED',
          expiresAt: new Date(now.getTime() + TOKEN_LEASE_MS),
        } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      return { admission, ownerNonce: input.ownerNonce };
    } catch (error) {
      const admission = await this.readAdmission(admissionId);
      if (admission && this.sameOrdinaryOwner(admission, input)) return { admission, ownerNonce: input.ownerNonce };
      throw error;
    }
  }

  /** Reserve the exclusive first-send slot and immutable request under that same row lock. */
  async reserveInitial(input: ReserveInitialIntentInput): Promise<{ intent: InitialMessageIntent; ownerNonce: string; created: boolean }> {
    const selectedV2 = parseChannelOperationContextV2(input.selectedContext);
    if (!selectedV2 || selectedV2.conversationId !== input.conversationId || selectedV2.buId !== input.buId) {
      throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
    }
    const intentId = randomUUID();
    try {
      return await this.prisma.$transaction(async (tx) => {
      const replay = await tx.initialMessageIntent.findUnique({
        where: { buId_actorId_idempotencyKey: {
          buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
        } },
      });
      if (replay) {
        if (replay.conversationId !== input.conversationId || replay.requestFingerprint !== input.requestFingerprint) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        if (canonicalJson(this.canonicalRequestFromStored(replay.request)) !== canonicalJson(this.canonicalRequestFromStored(input.request))) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        // Never adopt a nonce read from an idempotent replay. The caller keeps
        // the nonce it captured before this request; a stale/replayed owner
        // cannot pass a later CAS with the new nonce.
        return { intent: replay, ownerNonce: input.ownerNonce, created: false };
      }

      const selected = selectedV2;
      const identity = await tx.$queryRaw<Array<{ id: string }>>`
        SELECT id FROM provider_resource_identities
        WHERE id = ${selected.providerResourceIdentityId} AND bu_id = ${input.buId}
          AND current_channel_id = ${selected.channelId} AND business_identity_id = ${selected.businessIdentityId}
          AND provider = ${selected.adapterOrigin}::"ChannelType" AND managed_lifecycle = TRUE
        FOR SHARE
      `;
      if (!identity[0]) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      if (!await this.lockCapturedPeer(tx, selected, input.conversationId, input.buId)) {
        throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      }
      const { now } = await this.lockConversation(tx, input.conversationId, input.buId);
      const route = await tx.conversationRoute.findFirst({ where: {
        id: selected.routeId, conversationId: input.conversationId, buId: input.buId,
        contactId: selected.contactId, contactIdentityId: selected.contactIdentityId,
        businessIdentityId: selected.businessIdentityId,
        platform: selected.adapterOrigin === 'INSTAGRAM' ? 'INSTAGRAM' : 'WHATSAPP',
      }, select: { id: true } });
      if (!route) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });

      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'initial-actor:' + input.actorId}, 0))::text AS locked`;
      const accountNamespace = selected.providerAccountReference ?? selected.providerResourceIdentityId;
      if (!accountNamespace) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'initial-account:' + accountNamespace}, 0))::text AS locked`;
      const rateNow = await this.databaseNow(tx);
      const actorRate = await tx.$queryRaw<Array<{ count: number }>>`
        SELECT count(*)::int AS count FROM initial_message_intents
        WHERE actor_id = ${input.actorId} AND created_at >= ${new Date(rateNow.getTime() - 60_000)}
      `;
      const accountRate = await tx.$queryRaw<Array<{ count: number }>>`
        SELECT count(*)::int AS count FROM initial_message_intents
        WHERE COALESCE(selected_context->>'providerAccountReference', selected_context->>'providerResourceIdentityId') = ${accountNamespace}
          AND created_at >= ${new Date(rateNow.getTime() - 60 * 60_000)}
      `;
      if ((actorRate[0]?.count ?? 0) >= 10 || (accountRate[0]?.count ?? 0) >= 60) {
        throw new ConflictException({ code: 'INITIAL_RATE_LIMIT' });
      }

      // PREPARED means no provider claim occurred, so its immutable lease can
      // close it safely. SENDING/UNCERTAIN are never released by elapsed time.
      await tx.dispatchAdmission.updateMany({
        where: { conversationId: input.conversationId, releasedAt: null, state: 'PREPARED', expiresAt: { lte: now } },
        data: { state: 'SETTLED', releasedAt: now },
      });
      const ordinary = await tx.dispatchAdmission.findMany({
        where: { conversationId: input.conversationId, releasedAt: null },
        orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
        select: { id: true, state: true }, take: 11,
      });
      if (ordinary.length) throw new ConflictException({ code: 'ORDINARY_SEND_IN_PROGRESS', outcome: 'BLOCKED',
        ordinaryAdmissions: ordinary.slice(0, 10).map(({ id, state }) => ({ id, state })), admissionsTruncated: ordinary.length > 10 });

      const active = await tx.initialMessageIntent.findFirst({
        where: { conversationId: input.conversationId, slotReleasedAt: null },
        select: { id: true, state: true },
      });
      if (active) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: active.id, state: active.state });

      const intent = await tx.initialMessageIntent.create({ data: {
        id: intentId,
        conversationId: input.conversationId,
        buId: input.buId,
        actorId: input.actorId,
        idempotencyKey: input.idempotencyKey,
        ownerNonce: input.ownerNonce,
        requestFingerprint: input.requestFingerprint,
        request: input.request,
        selectedContext: input.selectedContext,
        state: 'PREPARED',
        leaseExpiresAt: new Date(now.getTime() + TOKEN_LEASE_MS),
      } });
      return { intent, ownerNonce: input.ownerNonce, created: true };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const intent = await this.readIntent(intentId);
      if (intent && this.sameInitialOwner(intent, input)) return { intent, ownerNonce: input.ownerNonce, created: true };
      const replay = await this.prisma.initialMessageIntent.findUnique({ where: { buId_actorId_idempotencyKey: {
        buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
      } } });
      if (replay) {
        if (replay.conversationId !== input.conversationId || replay.requestFingerprint !== input.requestFingerprint
          || canonicalJson(this.canonicalRequestFromStored(replay.request)) !== canonicalJson(this.canonicalRequestFromStored(input.request))
          || canonicalJson(replay.selectedContext) !== canonicalJson(input.selectedContext)) {
          throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
        }
        return { intent: replay, ownerNonce: input.ownerNonce, created: false };
      }
      throw error;
    }
  }

  /** Same-owner CAS after preflight; lock provider→peer→conversation before admission state. */
  async claimOrdinary(input: {
    id: string;
    ownerNonce: string;
    /** Must perform only bounded, transaction-local checks; all remote preflight is already complete. */
    validate: (tx: Prisma.TransactionClient, selectedContext: Prisma.JsonValue) => Promise<DispatchClaimEligibility>;
  }): Promise<boolean> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return false;
        const context = parseChannelOperationContextV2(hint.selectedContext);
        if (!context || context.conversationId !== hint.conversationId || context.buId !== hint.buId) return false;
        // Identity retirement/renewal takes the same lock first in acceptance.
        // Preserve the global identity -> conversation -> admission order.
        const identities = await tx.$queryRaw<Array<{ id: string; bu_id: string; current_channel_id: string | null }>>`
          SELECT id, bu_id, current_channel_id
          FROM provider_resource_identities
          WHERE id = ${context.providerResourceIdentityId}
            AND bu_id = ${hint.buId}
            AND current_channel_id = ${context.channelId}
          FOR SHARE
        `;
        if (!identities[0]) return false;
        if (!await this.lockCapturedPeer(tx, context, hint.conversationId, hint.buId)) return false;
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || current.state !== 'PREPARED'
          || current.releasedAt !== null || current.expiresAt.getTime() <= now.getTime()) return false;
        const eligibility = await input.validate(tx, current.selectedContext);
        if (!eligibility.eligible) return false;
        const claimNow = await this.databaseNow(tx);
        if (current.expiresAt.getTime() <= claimNow.getTime()) return false;
        const claimed = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE dispatch_admissions
          SET state = 'SENDING'::"DispatchAdmissionState",
              dispatch_deadline_at = expires_at,
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state = 'PREPARED'::"DispatchAdmissionState"
            AND released_at IS NULL
            AND expires_at > clock_timestamp()
            AND (${eligibility.windowExpiresAt}::timestamptz IS NULL OR ${eligibility.windowExpiresAt}::timestamptz > clock_timestamp())
            AND (${eligibility.credentialExpiresAt}::timestamptz IS NULL OR ${eligibility.credentialExpiresAt}::timestamptz > clock_timestamp() + INTERVAL '60 seconds')
          RETURNING id
        `;
        return claimed.length === 1;
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SENDING'
        && current.dispatchDeadlineAt?.getTime() === current.expiresAt.getTime()) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.releasedAt === null) return false;
      throw error;
    }
  }

  /** Initial claim shares the identity→peer→conversation→intent lock order and immutable 90s deadline. */
  async claimInitial(input: {
    id: string;
    ownerNonce: string;
    validate: (tx: Prisma.TransactionClient, selectedContext: Prisma.JsonValue, request: Prisma.JsonValue) => Promise<DispatchClaimEligibility>;
  }): Promise<boolean> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.initialMessageIntent.findUnique({ where: { id: input.id } });
        if (!hint) return false;
        const context = parseChannelOperationContextV2(hint.selectedContext);
        if (!context || context.conversationId !== hint.conversationId || context.buId !== hint.buId) return false;
        const identities = await tx.$queryRaw<Array<{ id: string }>>`
          SELECT id
          FROM provider_resource_identities
          WHERE id = ${context.providerResourceIdentityId}
            AND bu_id = ${hint.buId}
            AND current_channel_id = ${context.channelId}
          FOR SHARE
        `;
        if (!identities[0]) return false;
        if (!await this.lockCapturedPeer(tx, context, hint.conversationId, hint.buId)) return false;
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.initialMessageIntent.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || current.state !== 'PREPARED'
          || current.slotReleasedAt !== null || current.leaseExpiresAt.getTime() <= now.getTime()) return false;
        const eligibility = await input.validate(tx, current.selectedContext, current.request);
        if (!eligibility.eligible) return false;
        const eligibleAtClaim = await this.databaseNow(tx);
        if (current.leaseExpiresAt.getTime() <= eligibleAtClaim.getTime()) return false;
        const claimed = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE initial_message_intents
          SET state = 'SENDING'::"InitialMessageIntentState",
              dispatch_deadline_at = lease_expires_at,
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state = 'PREPARED'::"InitialMessageIntentState"
            AND slot_released_at IS NULL
            AND lease_expires_at > clock_timestamp()
            AND (${eligibility.windowExpiresAt}::timestamptz IS NULL OR ${eligibility.windowExpiresAt}::timestamptz > clock_timestamp())
            AND (${eligibility.credentialExpiresAt}::timestamptz IS NULL OR ${eligibility.credentialExpiresAt}::timestamptz > clock_timestamp() + INTERVAL '60 seconds')
          RETURNING id
        `;
        return claimed.length === 1;
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SENDING'
        && current.dispatchDeadlineAt?.getTime() === current.leaseExpiresAt.getTime()) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.slotReleasedAt === null) return false;
      throw error;
    }
  }

  async rejectInitial(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null
          || !['PREPARED', 'SENDING'].includes(current.state) || current.externalMessageId !== null) return { count: 0 };
        const now = await this.databaseNow(tx);
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: current.state, slotReleasedAt: null, externalMessageId: null },
          data: { state: 'REJECTED', slotReleasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null) return true;
      throw error;
    }
  }

  /** Releases only an owner positively known to be PREPARED; never guesses after a claim commit ACK loss. */
  async rejectPreparedInitial(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null || current.state !== 'PREPARED') return { count: 0 };
        const now = await this.databaseNow(tx);
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'PREPARED', slotReleasedAt: null, externalMessageId: null },
          data: { state: 'REJECTED', slotReleasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'REJECTED' && current.slotReleasedAt !== null) return true;
      throw error;
    }
  }

  async recordInitialExternalAccepted(input: { id: string; ownerNonce: string; externalMessageId: string }): Promise<boolean> {
    if (!input.externalMessageId.trim()) return false;
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce) return { count: 0 };
        if (current.externalMessageId === input.externalMessageId
          && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state)) {
          return { count: 1 };
        }
        if (current.externalMessageId !== null || !['SENDING', 'AMBIGUOUS'].includes(current.state)) return { count: 0 };
        // A late known provider receipt improves only this original intent. If
        // risk acknowledgment already released its slot, retain that release
        // and classify the local projection as blocked; never reacquire a slot.
        const nextState = current.slotReleasedAt === null ? 'EXTERNAL_ACCEPTED' : 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED';
        return tx.initialMessageIntent.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: current.state,
            externalMessageId: null, slotReleasedAt: current.slotReleasedAt,
          },
          data: { state: nextState, externalMessageId: input.externalMessageId },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.externalMessageId === input.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state);
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.externalMessageId === input.externalMessageId
        && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED'].includes(current.state)) return true;
      throw error;
    }
  }

  async markInitialAmbiguous(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null) return { count: 0 };
        if (current.state === 'AMBIGUOUS') return { count: 1 };
        if (current.state !== 'SENDING' || current.externalMessageId !== null) return { count: 0 };
        return tx.initialMessageIntent.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'SENDING', externalMessageId: null, slotReleasedAt: null },
          data: { state: 'AMBIGUOUS' },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'AMBIGUOUS' && current.slotReleasedAt === null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'AMBIGUOUS' && current.slotReleasedAt === null) return true;
      throw error;
    }
  }

  async acknowledgeInitialRisk(input: { id: string; ownerNonce: string; actorId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean>; audit?: (tx: Prisma.TransactionClient) => Promise<void> }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || current.slotReleasedAt !== null
          || !['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(current.state)
          || !current.dispatchDeadlineAt) return { count: 0 };
        if (input.validateActor && !await input.validateActor(tx)) return { count: 0 };
        const rows = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE initial_message_intents
          SET slot_released_at = clock_timestamp(),
              risk_acknowledged_at = clock_timestamp(),
              risk_acknowledged_by_actor_id = ${input.actorId},
              updated_at = clock_timestamp()
          WHERE id = ${input.id}
            AND owner_nonce = ${input.ownerNonce}
            AND state IN ('AMBIGUOUS'::"InitialMessageIntentState", 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'::"InitialMessageIntentState")
            AND external_message_id IS NOT DISTINCT FROM ${current.externalMessageId}
            AND slot_released_at IS NULL
            AND dispatch_deadline_at IS NOT NULL
            AND clock_timestamp() >= dispatch_deadline_at
          RETURNING id
        `;
        if (rows.length === 1 && input.audit) await input.audit(tx);
        return { count: rows.length };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.slotReleasedAt !== null
        && current.riskAcknowledgedAt !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.slotReleasedAt !== null
        && current.riskAcknowledgedAt !== null) return true;
      throw error;
    }
  }

  async listActiveAdmissions(input: { conversationId: string; buId: string; limit?: number }): Promise<{ items: DispatchAdmission[]; truncated: boolean }> {
    const limit = input.limit ?? 10;
    const rows = await this.prisma.dispatchAdmission.findMany({
      where: { conversationId: input.conversationId, buId: input.buId, releasedAt: null },
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], take: limit + 1,
    });
    return { items: rows.slice(0, limit), truncated: rows.length > limit };
  }

  async reconcileOrdinary(input: { id: string; conversationId: string; buId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean> }): Promise<DispatchAdmission | null> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return null;
        const context = parseStoredChannelOperationContext(hint.selectedContext);
        if (!context) return null;
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.context.providerResourceIdentityId} FOR SHARE`;
        if (!await this.lockCapturedPeer(tx, hint.selectedContext, input.conversationId, input.buId)) return null;
        await this.lockConversation(tx, input.conversationId, input.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.conversationId !== input.conversationId || current.buId !== input.buId) return null;
        if (input.validateActor && !await input.validateActor(tx)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        const now = await this.databaseNow(tx);
        if (current.state === 'PREPARED' && current.releasedAt === null && current.expiresAt <= now) {
          await tx.dispatchAdmission.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'PREPARED', releasedAt: null },
            data: { state: 'SETTLED', releasedAt: now },
          });
        } else if (current.state === 'SENDING' && current.releasedAt === null
          && current.dispatchDeadlineAt !== null && current.dispatchDeadlineAt <= now) {
          await tx.dispatchAdmission.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'SENDING', releasedAt: null, dispatchDeadlineAt: current.dispatchDeadlineAt },
            data: { state: 'UNCERTAIN' },
          });
        }
        return tx.dispatchAdmission.findUnique({ where: { id: current.id } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof ConflictException) throw error;
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      if (current && ((current.state === 'SETTLED' && current.releasedAt !== null)
        || ['SENDING', 'UNCERTAIN'].includes(current.state))) return current;
      throw new ServiceUnavailableException({ code: 'ADMISSION_RECONCILE_UNCONFIRMED' });
    }
  }

  async acknowledgeOrdinaryRisk(input: { id: string; conversationId: string; buId: string; actorId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean>; audit?: (tx: Prisma.TransactionClient) => Promise<void> }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return { count: 0 };
        const context = parseStoredChannelOperationContext(hint.selectedContext);
        if (!context) return { count: 0 };
        await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE id = ${context.context.providerResourceIdentityId} FOR SHARE`;
        if (!await this.lockCapturedPeer(tx, hint.selectedContext, input.conversationId, input.buId)) return { count: 0 };
        await this.lockConversation(tx, input.conversationId, input.buId);
        if (input.validateActor && !await input.validateActor(tx)) return { count: 0 };
        const rows = await tx.$queryRaw<Array<{ id: string }>>`
          UPDATE dispatch_admissions
          SET released_at = clock_timestamp(), risk_acknowledged_at = clock_timestamp(),
              risk_acknowledged_by_actor_id = ${input.actorId}, updated_at = clock_timestamp()
          WHERE id = ${input.id} AND conversation_id = ${input.conversationId} AND bu_id = ${input.buId}
            AND state = 'UNCERTAIN'::"DispatchAdmissionState" AND released_at IS NULL
            AND dispatch_deadline_at IS NOT NULL AND clock_timestamp() >= dispatch_deadline_at
          RETURNING id
        `;
        if (rows.length === 1 && input.audit) await input.audit(tx);
        return { count: rows.length };
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      return Boolean(current?.releasedAt && current.riskAcknowledgedAt);
    } catch {
      const current = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
      if (current?.releasedAt && current.riskAcknowledgedAt) return true;
      throw new ServiceUnavailableException({ code: 'ADMISSION_RELEASE_UNCONFIRMED' });
    }
  }

  async reconcileInitial(input: { id: string; conversationId: string; buId: string; validateActor?: (tx: Prisma.TransactionClient) => Promise<boolean> }): Promise<InitialMessageIntent | null> {
    try {
      return await this.prisma.$transaction(async (tx) => {
        const hint = await tx.initialMessageIntent.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
        if (!hint) return null;
        if (!parseStoredChannelOperationContext(hint.selectedContext)) {
          if (input.validateActor && !await input.validateActor(tx)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
          // Return only the scoped receipt. The caller's known-acceptance path
          // will report it as locally blocked without guessing a route or mutating it.
          return hint;
        }
        const current = await this.lockInitialOwner(tx, hint.id);
        if (!current) return null;
        if (input.validateActor && !await input.validateActor(tx)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
        const now = await this.databaseNow(tx);
        if (current.state === 'PREPARED' && current.slotReleasedAt === null && current.leaseExpiresAt <= now) {
          await tx.initialMessageIntent.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'PREPARED', slotReleasedAt: null },
            data: { state: 'REJECTED', slotReleasedAt: now },
          });
        } else if (current.state === 'SENDING' && current.slotReleasedAt === null
          && current.dispatchDeadlineAt !== null && current.dispatchDeadlineAt <= now) {
          await tx.initialMessageIntent.updateMany({
            where: { id: current.id, ownerNonce: current.ownerNonce, state: 'SENDING', slotReleasedAt: null, dispatchDeadlineAt: current.dispatchDeadlineAt },
            data: { state: 'AMBIGUOUS' },
          });
        }
        return tx.initialMessageIntent.findUnique({ where: { id: current.id } });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
    } catch (error) {
      if (error instanceof ConflictException) throw error;
      const current = await this.getInitialForScopedAttempt(input);
      if (current && ['PREPARED', 'SENDING', 'AMBIGUOUS', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED', 'SUCCEEDED', 'REJECTED'].includes(current.state)) return current;
      throw new ServiceUnavailableException({ code: 'INITIAL_RECONCILE_UNCONFIRMED' });
    }
  }

  async getInitialForActor(input: { id: string; conversationId: string; buId: string; actorId: string }): Promise<InitialMessageIntent | null> {
    return this.prisma.initialMessageIntent.findFirst({ where: {
      id: input.id, conversationId: input.conversationId, buId: input.buId, actorId: input.actorId,
    } });
  }

  async getInitialForScopedAttempt(input: { id: string; conversationId: string; buId: string }): Promise<InitialMessageIntent | null> {
    return this.prisma.initialMessageIntent.findFirst({ where: {
      id: input.id, conversationId: input.conversationId, buId: input.buId,
    } });
  }

  async initialRiskWindow(input: { id: string; conversationId: string; buId: string }): Promise<{ intent: InitialMessageIntent; eligibleAt: Date | null; eligible: boolean } | null> {
    const intent = await this.getInitialForScopedAttempt(input);
    if (!intent) return null;
    const rows = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    const now = rows[0]?.now;
    if (!(now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    const allowedState = intent.state === 'AMBIGUOUS' || intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED';
    return { intent, eligibleAt: allowedState ? intent.dispatchDeadlineAt : null,
      eligible: isInitialRiskAcknowledgmentEligible(intent.state, intent.dispatchDeadlineAt, now) };
  }

  async ordinaryRiskWindow(input: { id: string; conversationId: string; buId: string }): Promise<{ admission: DispatchAdmission; eligibleAt: Date | null; eligible: boolean } | null> {
    const admission = await this.prisma.dispatchAdmission.findFirst({ where: { id: input.id, conversationId: input.conversationId, buId: input.buId } });
    if (!admission) return null;
    const rows = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    const now = rows[0]?.now;
    if (!(now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    return { admission, eligibleAt: admission.dispatchDeadlineAt, eligible: Boolean(admission.dispatchDeadlineAt && now.getTime() >= admission.dispatchDeadlineAt.getTime()) };
  }

  async markInitialLocalBlocked(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const current = await this.lockInitialOwner(tx, input.id);
        if (!current || current.ownerNonce !== input.ownerNonce || !current.externalMessageId) return { count: 0 };
        if (current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') return { count: 1 };
        if (current.state !== 'EXTERNAL_ACCEPTED') return { count: 0 };
        return tx.initialMessageIntent.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: 'EXTERNAL_ACCEPTED',
            externalMessageId: current.externalMessageId, slotReleasedAt: current.slotReleasedAt,
          },
          data: { state: 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED' },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readIntent(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'
        && current.externalMessageId !== null;
    } catch (error) {
      const current = await this.readIntent(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'
        && current.externalMessageId !== null) return true;
      throw error;
    }
  }

  /** Settle only the original owner; a late completion cannot release a successor token. */
  async settleOrdinary(input: { id: string; ownerNonce: string; state: 'SETTLED' | 'UNCERTAIN' }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return { count: 0 };
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        const current = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!current || current.ownerNonce !== input.ownerNonce || !['SENDING', 'UNCERTAIN'].includes(current.state)) return { count: 0 };
        return tx.dispatchAdmission.updateMany({
          where: {
            id: input.id, ownerNonce: input.ownerNonce, state: { in: ['SENDING', 'UNCERTAIN'] }, releasedAt: current.releasedAt,
          },
          data: {
            state: input.state,
            ...(input.state === 'SETTLED' ? { releasedAt: current.releasedAt ?? now } : {}),
          },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readAdmission(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === input.state
        && (input.state === 'UNCERTAIN' ? current.releasedAt === null : current.releasedAt !== null);
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === input.state
        && (input.state === 'UNCERTAIN' ? current.releasedAt === null : current.releasedAt !== null)) return true;
      if (current?.ownerNonce === input.ownerNonce && ['SENDING', 'UNCERTAIN'].includes(current.state) && current.releasedAt === null) return false;
      throw error;
    }
  }

  /** A confirmed pre-dispatch abort releases only this still-PREPARED owner. */
  async releasePrepared(input: { id: string; ownerNonce: string }): Promise<boolean> {
    try {
      const result = await this.prisma.$transaction(async (tx) => {
        const hint = await tx.dispatchAdmission.findUnique({ where: { id: input.id } });
        if (!hint) return { count: 0 };
        const { now } = await this.lockConversation(tx, hint.conversationId, hint.buId);
        return tx.dispatchAdmission.updateMany({
          where: { id: input.id, ownerNonce: input.ownerNonce, state: 'PREPARED', releasedAt: null },
          data: { state: 'SETTLED', releasedAt: now },
        });
      }, { isolationLevel: Prisma.TransactionIsolationLevel.ReadCommitted });
      if (result.count === 1) return true;
      const current = await this.readAdmission(input.id);
      return current?.ownerNonce === input.ownerNonce && current.state === 'SETTLED' && current.releasedAt !== null;
    } catch (error) {
      const current = await this.readAdmission(input.id);
      if (current?.ownerNonce === input.ownerNonce && current.state === 'SETTLED' && current.releasedAt !== null) return true;
      if (current?.ownerNonce === input.ownerNonce && current.state === 'PREPARED' && current.releasedAt === null) return false;
      throw error;
    }
  }

  private async lockCapturedPeer(
    tx: Prisma.TransactionClient,
    selectedContext: unknown,
    conversationId: string,
    buId: string,
  ): Promise<boolean> {
    const stored = parseStoredChannelOperationContext(selectedContext);
    if (!stored) return false;
    let address: ContactIdentityAddress | null;
    if (stored.version === 2) {
      if (stored.context.conversationId !== conversationId || stored.context.buId !== buId) return false;
      address = await resolveContactIdentityAddress(tx, stored.context);
      if (!address) return false;
    } else {
      const conversation = await tx.conversation.findFirst({
        where: { id: conversationId, buId }, select: { contact: true, contactType: true },
      });
      if (!conversation) return false;
      address = whatsappPeerAddress({
        buId, externalPeerId: conversation.contact, contactType: conversation.contactType,
      });
    }
    await lockContactIdentityAddress(tx, address);
    return true;
  }

  private async lockConversation(tx: Prisma.TransactionClient, conversationId: string, buId: string) {
    const rows = await tx.$queryRaw<Array<{ id: string; bu_id: string; contact: string }>>`
      SELECT id, bu_id, contact
      FROM conversations
      WHERE id = ${conversationId} AND bu_id = ${buId}
      FOR UPDATE
    `;
    const row = rows[0];
    if (!row) throw new ConflictException({ code: 'CONVERSATION_IDENTITY_MISMATCH' });
    return { now: await this.databaseNow(tx), contact: row.contact };
  }

  /** Preserve identity→qualified peer→conversation→intent order for initial lifecycle mutations. */
  private async lockInitialOwner(tx: Prisma.TransactionClient, id: string): Promise<InitialMessageIntent | null> {
    const hint = await tx.initialMessageIntent.findUnique({ where: { id } });
    if (!hint) return null;
    const stored = parseStoredChannelOperationContext(hint.selectedContext);
    if (!stored) return null;
    await tx.$queryRaw<Array<{ id: string }>>`
      SELECT id FROM provider_resource_identities
      WHERE id = ${stored.context.providerResourceIdentityId}
      FOR SHARE
    `;
    if (!await this.lockCapturedPeer(tx, hint.selectedContext, hint.conversationId, hint.buId)) return null;
    await this.lockConversation(tx, hint.conversationId, hint.buId);
    return tx.initialMessageIntent.findUnique({ where: { id } });
  }

  private async databaseNow(tx: Prisma.TransactionClient): Promise<Date> {
    const rows = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    if (!rows[0] || !(rows[0].now instanceof Date)) throw new ServiceUnavailableException({ code: 'ADMISSION_CLOCK_UNAVAILABLE' });
    return rows[0].now;
  }

  private canonicalRequestFromStored(value: Prisma.JsonValue | Prisma.InputJsonValue): unknown {
    const record = value && typeof value === 'object' && !Array.isArray(value)
      ? value as Record<string, unknown>
      : null;
    return record && Object.hasOwn(record, 'canonicalRequest') ? record.canonicalRequest ?? null : value;
  }

  private async readAdmission(id: string): Promise<DispatchAdmission | null> {
    try { return await this.prisma.dispatchAdmission.findUnique({ where: { id } }); }
    catch { throw new ServiceUnavailableException({ code: 'ADMISSION_COMMIT_UNCONFIRMED' }); }
  }

  private async readIntent(id: string): Promise<InitialMessageIntent | null> {
    try { return await this.prisma.initialMessageIntent.findUnique({ where: { id } }); }
    catch { throw new ServiceUnavailableException({ code: 'INITIAL_INTENT_COMMIT_UNCONFIRMED' }); }
  }

  private sameOrdinaryOwner(row: DispatchAdmission, input: ReserveOrdinaryAdmissionInput): boolean {
    return Boolean(row.id) && row.ownerNonce === input.ownerNonce && row.conversationId === input.conversationId
      && row.buId === input.buId && row.caller === input.caller && row.actorId === input.actorId
      && canonicalJson(row.selectedContext) === canonicalJson(input.selectedContext);
  }

  private sameInitialOwner(row: InitialMessageIntent, input: ReserveInitialIntentInput): boolean {
    return row.ownerNonce === input.ownerNonce && row.conversationId === input.conversationId
      && row.buId === input.buId && row.actorId === input.actorId && row.idempotencyKey === input.idempotencyKey
      && row.requestFingerprint === input.requestFingerprint
      && canonicalJson(row.selectedContext) === canonicalJson(input.selectedContext)
      && canonicalJson(row.request) === canonicalJson(input.request);
  }
}

```

## Complete current source api-app/src/domain/channels/channel-credential-resolver.ts
```
import { ConflictException, Injectable } from '@nestjs/common';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { loadChannelCredentialKey, openChannelCredential } from './channel-credential-crypto';
import { hasChannelProviderReadiness } from './channel-provider-readiness';

export interface ResolvedChannelCredential {
  channelId: string;
  buId: string;
  provider: 'OFICIAL' | 'NAO_OFICIAL' | 'INSTAGRAM';
  generation: number;
  pairingEpoch: number;
  providerResourceIdentityId: string;
  businessIdentityId: string | null;
  externalResourceId: string;
  activeCredentialVersion: number | null;
  accessToken?: string;
  phoneNumberId?: string;
  wabaId?: string;
  evolutionInstanceName?: string;
  instagramAccountId?: string;
  expiresAt?: Date;
}

/** Resolves only a currently verified, owned channel and decrypts its own credential. */
@Injectable()
export class ChannelCredentialResolver {
  constructor(private readonly prisma: PrismaService) {}

  /** Metadata-only check for GET availability; it never decrypts the credential. */
  async inspectActiveCredential(
    channelId: string,
    generation: number,
    expected?: { readonly provider: 'OFICIAL' | 'NAO_OFICIAL' | 'INSTAGRAM'; readonly buId: string },
    transaction?: Prisma.TransactionClient,
  ): Promise<{ version: number | null; ready: boolean; expiresAt: Date | null }> {
    if (!transaction) return (await this.inspectActiveCredentials([{ channelId, generation, ...expected }])).get(channelId) ?? { version: null, ready: false, expiresAt: null };
    const [credential, clock] = await Promise.all([
      transaction.channelCredential.findUnique({
        where: { channelId }, select: { version: true, generation: true, keyId: true, provider: true, buId: true, expiresAt: true },
      }),
      transaction.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`,
    ]);
    const now = clock[0]?.now;
    let currentKeyId: string | null = null;
    try { currentKeyId = loadChannelCredentialKey(process.env).keyId; } catch { /* absent key makes the credential unavailable */ }
    const expiryReady = credential?.provider === 'INSTAGRAM'
      ? Boolean(now && credential.expiresAt && credential.expiresAt.getTime() > now.getTime() + 60_000)
      : !credential?.expiresAt || Boolean(now && credential.expiresAt.getTime() > now.getTime() + 60_000);
    const ready = Boolean(credential && currentKeyId && credential.keyId === currentKeyId
      && credential.generation === generation && (!expected?.provider || credential.provider === expected.provider)
      && (!expected?.buId || credential.buId === expected.buId)
      && expiryReady);
    return { version: credential?.version ?? null, ready, expiresAt: credential?.expiresAt ?? null };
  }

  /** One metadata-only credential read for a public conversation page. */
  async inspectActiveCredentials(bindings: readonly { channelId: string; generation: number; provider?: 'OFICIAL' | 'NAO_OFICIAL' | 'INSTAGRAM'; buId?: string }[]): Promise<Map<string, { version: number | null; ready: boolean; expiresAt: Date | null }>> {
    const ids = [...new Set(bindings.map((binding) => binding.channelId))];
    if (!ids.length) return new Map();
    const [credentials, clock] = await Promise.all([
      this.prisma.channelCredential.findMany({
        where: { channelId: { in: ids } }, select: { channelId: true, version: true, generation: true, keyId: true, provider: true, buId: true, expiresAt: true },
      }),
      this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`,
    ]);
    const now = clock[0]?.now;
    let currentKeyId: string | null = null;
    try {
      currentKeyId = loadChannelCredentialKey(process.env).keyId;
    } catch { /* absent key makes every official channel unavailable */ }
    const byId = new Map(credentials.map((credential) => [credential.channelId, credential]));
    return new Map(bindings.map(({ channelId, generation, provider, buId }) => {
      const credential = byId.get(channelId);
      const expiryReady = credential?.provider === 'INSTAGRAM'
        ? Boolean(now && credential.expiresAt && credential.expiresAt.getTime() > now.getTime() + 60_000)
        : !credential?.expiresAt || Boolean(now && credential.expiresAt.getTime() > now.getTime() + 60_000);
      return [channelId, {
        version: credential?.version ?? null,
        expiresAt: credential?.expiresAt ?? null,
        ready: Boolean(credential && credential.generation === generation && currentKeyId && credential.keyId === currentKeyId
          && (!provider || credential.provider === provider) && (!buId || credential.buId === buId)
          && expiryReady),
      }];
    }));
  }

  async resolve(channelId: string, purpose: 'send' | 'registration' | 'verify' | 'template-management' = 'send'): Promise<ResolvedChannelCredential> {
    const channel = await this.prisma.buChannel.findUnique({
      where: { id: channelId }, include: { credential: true, providerIdentities: true },
    });
    if (!channel || (channel.type !== 'INSTAGRAM' && purpose !== 'verify' && (!channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch))) {
      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
    }
    if (purpose === 'send' && !hasChannelProviderReadiness({ provider: channel.type, status: channel.status,
      providerConnectionState: channel.providerConnectionState, receiptVerifiedAt: channel.receiptVerifiedAt })) {
      throw new ConflictException({ code: 'CHANNEL_NOT_READY' });
    }
    if (purpose === 'template-management' && channel.type !== 'OFICIAL') {
      throw new ConflictException({ code: 'TEMPLATE_MANAGEMENT_UNAVAILABLE' });
    }
    const identity = channel.providerIdentities.find((row) => row.currentChannelId === channel.id);
    if (!identity || !identity.managedLifecycle || identity.provider !== channel.type || identity.buId !== channel.buId) {
      throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
    }
    const result: ResolvedChannelCredential = {
      channelId: channel.id, buId: channel.buId, provider: channel.type, generation: channel.generation,
      pairingEpoch: channel.pairingEpoch, providerResourceIdentityId: identity.id,
      businessIdentityId: identity.businessIdentityId,
      externalResourceId: identity.externalResourceId,
      activeCredentialVersion: channel.credential?.version ?? null,
      ...(channel.phoneNumberId ? { phoneNumberId: channel.phoneNumberId } : {}),
      ...(channel.wabaId ? { wabaId: channel.wabaId } : {}),
      ...(channel.evolutionInstanceName ? { evolutionInstanceName: channel.evolutionInstanceName } : {}),
    };
    if (channel.type === 'INSTAGRAM') {
      const clock = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
      if (!channel.credential || channel.credential.provider !== 'INSTAGRAM' || channel.credential.buId !== channel.buId
        || channel.credential.generation !== channel.generation || !channel.credential.expiresAt
        || !clock[0]?.now || channel.credential.expiresAt.getTime() <= clock[0].now.getTime() + 60_000) {
        throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      }
      const { keyId, key } = loadChannelCredentialKey(process.env);
      if (channel.credential.keyId !== keyId) throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      const plaintext = openChannelCredential({ ...channel.credential, nonce: Buffer.from(channel.credential.nonce),
        ciphertext: Buffer.from(channel.credential.ciphertext), tag: Buffer.from(channel.credential.tag) }, new Map([[keyId, key]]), {
        purpose: 'active', provider: 'INSTAGRAM', buId: channel.buId, channelId: channel.id,
        generation: channel.generation, version: channel.credential.version,
      });
      result.accessToken = plaintext.toString('utf8');
      result.instagramAccountId = identity.externalResourceId;
      result.expiresAt = channel.credential.expiresAt;
    } else if (channel.type === 'OFICIAL') {
      if (!channel.credential || channel.credential.generation !== channel.generation
        || channel.credential.provider !== channel.type || channel.credential.buId !== channel.buId) {
        throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      }
      if (channel.credential.expiresAt) {
        const clock = await this.prisma.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
        if (!clock[0]?.now || channel.credential.expiresAt.getTime() <= clock[0].now.getTime() + 60_000) {
          throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
        }
      }
      const { keyId, key } = loadChannelCredentialKey(process.env);
      if (channel.credential.keyId !== keyId) throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      const plaintext = openChannelCredential({
        ...channel.credential, nonce: Buffer.from(channel.credential.nonce),
        ciphertext: Buffer.from(channel.credential.ciphertext), tag: Buffer.from(channel.credential.tag),
      }, new Map([[keyId, key]]), {
        purpose: 'active', provider: channel.type, buId: channel.buId, channelId: channel.id,
        generation: channel.generation, version: channel.credential.version,
      });
      result.accessToken = plaintext.toString('utf8');
      if (channel.credential.expiresAt) result.expiresAt = channel.credential.expiresAt;
    }
    return result;
  }
}

```

## Complete current source api-app/src/domain/inbox/initial-message.service.ts
```
import { ConflictException, HttpException, Injectable, NotFoundException, ServiceUnavailableException } from '@nestjs/common';
import { Prisma, type InitialMessageIntent } from '@prisma/client';
import { createHash, randomUUID } from 'node:crypto';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { OutboundService } from './outbound.service';
import { DispatchAdmissionService } from './dispatch-admission.service';
import { TEMPLATE_MANAGEMENT_RESOLVER, type TemplateManagementResolver, type TemplateManagementContext, type TemplateSummary } from '../message-templates/template-management.ports';
import { TemplateObservationService } from '../message-templates/template-observation.service';
import { InitialTemplateRenderError, renderInitialTemplate } from './initial-message-template-renderer';
import type { ChannelMessage, ChannelOperationContext } from '../channels/transport/channel';
import { Inject } from '@nestjs/common';

type TextRequest = { channelId: string; expectedGeneration: number; kind: 'text'; text: string; previewFingerprint: string };
type TemplateRequest = { channelId: string; expectedGeneration: number; kind: 'approved-template'; remoteTemplateId: string; language: string; catalogAfter: string | null; expectedDefinitionFingerprint: string; values: Readonly<Record<string, string>> | readonly string[]; previewFingerprint: string };
type ObservedTemplateSummary = TemplateSummary & { readonly available: boolean };
export type InitialMessageRequest = TextRequest | TemplateRequest;
export type InitialMessagePreviewRequest = Omit<TextRequest, 'previewFingerprint'> | Omit<TemplateRequest, 'previewFingerprint'>;
type InitialRequest = InitialMessageRequest;
type PreviewRequest = InitialMessagePreviewRequest;
const canonical = (value: unknown): string => {
  if (Array.isArray(value)) return `[${value.map(canonical).join(',')}]`;
  if (value && typeof value === 'object') return `{${Object.keys(value as object).sort().map((key) => `${JSON.stringify(key)}:${canonical((value as Record<string, unknown>)[key])}`).join(',')}}`;
  return JSON.stringify(value) ?? 'null';
};
const fingerprint = (value: unknown) => createHash('sha256').update(canonical(value)).digest('hex');

@Injectable()
export class InitialMessageService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly outbound: OutboundService,
    private readonly admissions: DispatchAdmissionService,
    @Inject(TEMPLATE_MANAGEMENT_RESOLVER) private readonly templates: TemplateManagementResolver,
    private readonly observations: TemplateObservationService,
  ) {}

  async assertOrdinaryDispatchAllowed(conversationId: string, buId: string): Promise<void> {
    const conversation = await this.prisma.conversation.findFirst({
      where: { id: conversationId, buId }, select: { id: true },
    });
    if (!conversation) throw new NotFoundException({ code: 'CONVERSATION_NOT_FOUND' });
    const [existingMessage, active] = await Promise.all([
      this.prisma.message.findFirst({ where: { conversationId }, select: { id: true } }),
      this.prisma.initialMessageIntent.findFirst({ where: { conversationId, buId, slotReleasedAt: null }, select: { id: true, state: true } }),
    ]);
    if (active) throw new ConflictException({ code: 'INITIAL_SEND_IN_PROGRESS', outcome: 'BLOCKED', attemptId: active.id, state: active.state });
    if (!existingMessage) throw new ConflictException({ code: 'INITIAL_SEND_REQUIRED' });
  }

  async preview(input: { conversationId: string; buId: string; actorId: string; message: PreviewRequest }) {
    const conversation = await this.conversation(input.conversationId, input.buId);
    const operation = await this.outbound.prepareInitial({ conversationId: conversation.id, buId: conversation.buId, channelId: input.message.channelId, kind: input.message.kind });
    this.assertGeneration(operation.context, input.message.expectedGeneration);
    let text: string;
    let semantics: unknown;
    let managementContext: TemplateManagementContext | undefined;
    if (input.message.kind === 'text') {
      if (typeof input.message.text !== 'string' || !input.message.text.trim() || [...input.message.text].length > 4096) throw new ConflictException({ code: 'INITIAL_PREVIEW_INVALID' });
      text = input.message.text;
      semantics = { kind: 'text', text };
    } else {
      const templateRequest = input.message;
      const resolved = await this.templates.resolve({ buId: input.buId, channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration });
      managementContext = resolved.context;
      this.assertManagementContext(operation.context, resolved.context);
      const catalog = await this.observations.getCatalog(input.actorId, input.buId, input.message.channelId, input.message.catalogAfter);
      const observation = (catalog.items as ObservedTemplateSummary[]).find((item) => item.remoteTemplateId === templateRequest.remoteTemplateId && item.language === templateRequest.language);
      if (!catalog.available || !observation || !observation.available || observation.status !== 'APPROVED' || !managementContext.accountReference) throw new ConflictException({ code: 'INITIAL_TEMPLATE_UNAVAILABLE' });
      const summary = observation;
      const rendered = this.renderTemplate(summary, input.message.values);
      if (rendered.semanticFingerprint !== input.message.expectedDefinitionFingerprint) throw new ConflictException({ code: 'INITIAL_TEMPLATE_CHANGED' });
      text = rendered.text;
      semantics = { kind: 'approved-template', remoteTemplateId: summary.remoteTemplateId, language: input.message.language,
        values: input.message.values, semanticFingerprint: rendered.semanticFingerprint };
    }
    const recipientRef = await this.outbound.recipientForOperation(operation.context);
    const previewFingerprint = fingerprint({ version: 'initial-preview-v1', context: operation.context, recipient: recipientRef, semantics });
    return { text, previewFingerprint,
      channel: { channelId: operation.context.channelId, channelOrigin: operation.context.adapterOrigin,
        generation: operation.context.generation, requiresWindow: operation.eligibilityPolicy.requiresWindow },
      ...(managementContext ? { template: { available: true } } : {}) };
  }

  async submit(input: {
    conversationId: string; buId: string; actorId: string; actorName: string; idempotencyKey: string;
    message: InitialRequest; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>;
  }) {
    if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(input.idempotencyKey)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_INVALID' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const conversation = await this.conversation(input.conversationId, input.buId);
    // Keep the historical replay lookup fingerprint stable. The durable V2
    // request below records the route-derived peer after explicit resolution.
    const replayFingerprint = fingerprint({ ...input.message, recipient: conversation.contact });
    const ownerNonce = randomUUID();
    const replay = await this.admissions.findInitialReplay({
      conversationId: input.conversationId, buId: input.buId, actorId: input.actorId,
      idempotencyKey: input.idempotencyKey, requestFingerprint: replayFingerprint, ownerNonce,
      selectedChannelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration,
    });
    if (replay) {
      const stored = this.requestRecord(replay.intent.request);
      const storedCanonical = stored?.canonicalRequest;
      const replayMessage = storedCanonical && typeof storedCanonical === 'object' && !Array.isArray(storedCanonical)
        ? Object.fromEntries(Object.entries(storedCanonical as Record<string, unknown>).filter(([key]) => key !== 'recipient')) : null;
      if (canonical(replayMessage) !== canonical(input.message)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
      if (replay.intent.state === 'AMBIGUOUS' || replay.intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') {
        throw new ConflictException({ code: 'INITIAL_SEND_UNCERTAIN', attemptId: replay.intent.id, state: replay.intent.state });
      }
      return { replay: true, attempt: this.projectIntent(replay.intent), expiredPrepared: replay.intent.state === 'PREPARED' && replay.intent.leaseExpiresAt <= new Date() };
    }

    let preview: Awaited<ReturnType<InitialMessageService['preview']>>;
    let operation: Awaited<ReturnType<OutboundService['prepareInitial']>>;
    let payload: ChannelMessage;
    let finalSemantics: unknown;
    let recipientRef: string;
    try {
      preview = await this.preview({ conversationId: input.conversationId, buId: input.buId, actorId: input.actorId, message: input.message.kind === 'text'
        ? { channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration, kind: 'text', text: input.message.text }
        : { channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration, kind: 'approved-template', remoteTemplateId: input.message.remoteTemplateId, language: input.message.language, catalogAfter: input.message.catalogAfter, expectedDefinitionFingerprint: input.message.expectedDefinitionFingerprint, values: input.message.values } });
      if (preview.previewFingerprint !== input.message.previewFingerprint) throw new ConflictException({ code: 'PREVIEW_CONTEXT_CHANGED' });
      operation = await this.outbound.prepareInitial({ conversationId: input.conversationId, buId: input.buId, channelId: input.message.channelId, kind: input.message.kind });
      this.assertGeneration(operation.context, input.message.expectedGeneration);
      recipientRef = await this.outbound.recipientForOperation(operation.context);
      if (input.message.kind === 'text') {
        payload = { kind: 'text', recipientRef, text: input.message.text };
        finalSemantics = { kind: 'text', text: input.message.text };
      } else {
        const templateRequest = input.message;
        const management = await this.templates.resolve({ buId: input.buId, channelId: input.message.channelId, expectedGeneration: input.message.expectedGeneration });
        this.assertManagementContext(operation.context, management.context);
        const catalog = await this.observations.getCatalog(input.actorId, input.buId, input.message.channelId, input.message.catalogAfter);
        const observation = (catalog.items as ObservedTemplateSummary[]).find((item) => item.remoteTemplateId === templateRequest.remoteTemplateId && item.language === templateRequest.language);
        if (!catalog.available || !observation || !observation.available || observation.status !== 'APPROVED') throw new ConflictException({ code: 'INITIAL_TEMPLATE_UNAVAILABLE' });
        const summary = observation;
        const rendered = this.renderTemplate(summary, input.message.values);
        if (rendered.semanticFingerprint !== input.message.expectedDefinitionFingerprint) throw new ConflictException({ code: 'INITIAL_TEMPLATE_CHANGED' });
        finalSemantics = { kind: 'approved-template', remoteTemplateId: summary.remoteTemplateId, language: input.message.language,
          values: input.message.values, semanticFingerprint: rendered.semanticFingerprint };
        payload = { kind: 'approved-template', recipientRef, template: {
          summary, values: input.message.values, managementContext: management.context,
          renderedText: rendered.text, semanticFingerprint: rendered.semanticFingerprint,
        } };
      }
      const context = operation.context;
      if (fingerprint({ version: 'initial-preview-v1', context, recipient: recipientRef, semantics: finalSemantics }) !== input.message.previewFingerprint) {
        throw new ConflictException({ code: 'PREVIEW_CONTEXT_CHANGED' });
      }
    } catch (error) {
      if (error instanceof HttpException) {
        const response = error.getResponse();
        const body = response && typeof response === 'object' && !Array.isArray(response)
          ? response as Record<string, unknown> : {};
        const marked = {
          ...(typeof body.code === 'string' ? { code: body.code } : { code: 'INITIAL_PRE_ADMISSION_REJECTED' }),
          ...(typeof body.message === 'string' ? { message: body.message } : {}),
          ...(typeof body.error === 'string' ? { error: body.error } : {}),
          preAdmission: true,
        };
        throw new HttpException(marked, error.getStatus());
      }
      throw error;
    }
    const context = operation.context;
    const canonicalRequest = { ...input.message, recipient: recipientRef };
    const requestFingerprint = fingerprint({ ...input.message, recipient: conversation.contact });
    const originalConversation = { updatedAt: conversation.updatedAt.toISOString(), status: conversation.status,
      attendantUserId: conversation.attendantUserId, attendantName: conversation.attendantName, attendantOrigin: conversation.attendantOrigin };
    const storedRequest = { canonicalRequest, originalConversation, renderedText: preview.text, originalActorName: input.actorName } as unknown as Prisma.InputJsonValue;
    const reservation = await this.admissions.reserveInitial({
      conversationId: input.conversationId, buId: input.buId, actorId: input.actorId, idempotencyKey: input.idempotencyKey,
      ownerNonce, selectedContext: context as unknown as Prisma.InputJsonValue,
      requestFingerprint, request: storedRequest,
    });
    if (!reservation.created) {
      const stored = this.requestRecord(reservation.intent.request);
      const storedCanonical = stored?.canonicalRequest;
      const replayMessage = storedCanonical && typeof storedCanonical === 'object' && !Array.isArray(storedCanonical)
        ? Object.fromEntries(Object.entries(storedCanonical as Record<string, unknown>).filter(([key]) => key !== 'recipient')) : null;
      if (canonical(replayMessage) !== canonical(input.message)) throw new ConflictException({ code: 'IDEMPOTENCY_KEY_REUSED' });
      if (reservation.intent.state === 'AMBIGUOUS' || reservation.intent.state === 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED') {
        throw new ConflictException({ code: 'INITIAL_SEND_UNCERTAIN', attemptId: reservation.intent.id, state: reservation.intent.state });
      }
      return { replay: true, attempt: this.projectIntent(reservation.intent), expiredPrepared: reservation.intent.state === 'PREPARED' && reservation.intent.leaseExpiresAt <= new Date() };
    }
    const result = await this.outbound.sendInitial({
      conversationId: input.conversationId, buId: input.buId, channelId: input.message.channelId,
      kind: input.message.kind, intent: reservation.intent, ownerNonce, operation, payload,
      request: storedRequest,
      originalConversation: { updatedAt: conversation.updatedAt, status: conversation.status, attendantUserId: conversation.attendantUserId,
        attendantName: conversation.attendantName, attendantOrigin: conversation.attendantOrigin },
      actorId: input.actorId, actorName: input.actorName, validateActorInTransaction: input.validateActorInTransaction,
    });
    let finalIntent: InitialMessageIntent | null;
    try {
      finalIntent = await this.admissions.getInitialForScopedAttempt({ id: reservation.intent.id, conversationId: input.conversationId, buId: input.buId });
    } catch {
      finalIntent = null;
    }
    if (!finalIntent) throw new ServiceUnavailableException({ code: 'INITIAL_ATTEMPT_READBACK_UNCONFIRMED', attemptId: reservation.intent.id,
      providerAcceptance: 'CONFIRMED', receiptPersistence: 'RECORDED', localMessageState: 'RECORDED', recoveryAction: 'RECONCILE' });
    return { replay: false, expiredPrepared: false, attempt: this.projectIntent(finalIntent),
      message: { id: result.id, channelOrigin: result.channelOrigin, createdAt: result.createdAt } };
  }

  async options(input: { conversationId: string; buId: string }) {
    const conversation = await this.conversation(input.conversationId, input.buId);
    const [channels, active, admissions, recent] = await Promise.all([
      this.outbound.initialOptions(conversation.id, input.buId),
      this.prisma.initialMessageIntent.findFirst({ where: { conversationId: conversation.id, slotReleasedAt: null }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }] }),
      this.admissions.listActiveAdmissions({ conversationId: conversation.id, buId: input.buId, limit: 10 }),
      this.prisma.initialMessageIntent.findMany({ where: { conversationId: conversation.id, buId: input.buId }, orderBy: [{ createdAt: 'desc' }, { id: 'desc' }], take: 11 }),
    ]);
    return { conversationId: conversation.id,
      channels,
      activeAttempt: active ? this.projectIntent(active) : null,
      ordinaryAdmissions: admissions.items.map(({ id, state, expiresAt, dispatchDeadlineAt, createdAt }) => ({ id, state, expiresAt, dispatchDeadlineAt, createdAt })),
      admissionsTruncated: admissions.truncated,
      recentAttempts: recent.slice(0, 10).map((intent) => this.projectIntent(intent)),
      attemptsTruncated: recent.length > 10 };
  }

  async getAttempt(input: { id: string; conversationId: string; buId: string }) {
    const intent = await this.admissions.getInitialForScopedAttempt(input);
    if (!intent) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    return this.projectIntent(intent);
  }

  async reconcile(input: { id: string; conversationId: string; buId: string; actorId: string; actorName: string; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean> }) {
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const intent = await this.admissions.reconcileInitial({ ...input, validateActor: input.validateActorInTransaction });
    if (!intent) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    if (intent.externalMessageId && ['EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)) {
      const message = await this.outbound.reconcileInitial({ intent, actorId: input.actorId, actorName: input.actorName, validateActorInTransaction: input.validateActorInTransaction });
      const current = await this.admissions.getInitialForScopedAttempt(input);
      return { ...this.projectIntent(current ?? intent), ...(message ? { message: { id: message.id, channelOrigin: message.channelOrigin, createdAt: message.createdAt } } : {}) };
    }
    return this.projectIntent(intent);
  }

  async acknowledge(input: { id: string; conversationId: string; buId: string; actorId: string; confirmed: boolean; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>; auditInTransaction: (tx: Prisma.TransactionClient) => Promise<void> }) {
    if (input.confirmed !== true) throw new ConflictException({ code: 'DUPLICATION_RISK_CONFIRMATION_REQUIRED' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const window = await this.admissions.initialRiskWindow(input);
    if (!window) throw new NotFoundException({ code: 'ATTEMPT_NOT_FOUND' });
    if (window.eligibleAt && !window.eligible) throw new ConflictException({ code: 'ACK_TOO_EARLY', eligibleAt: window.eligibleAt });
    if (!await this.admissions.acknowledgeInitialRisk({ id: input.id, actorId: input.actorId, ownerNonce: window.intent.ownerNonce,
      validateActor: input.validateActorInTransaction, audit: input.auditInTransaction })) throw new ConflictException({ code: 'ACK_NOT_ELIGIBLE' });
    return this.getAttempt(input);
  }

  async reconcileOrdinary(input: { id: string; conversationId: string; buId: string; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean> }) {
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const result = await this.admissions.reconcileOrdinary({ ...input, validateActor: input.validateActorInTransaction });
    if (!result) throw new NotFoundException({ code: 'ADMISSION_NOT_FOUND' });
    const { id, state, expiresAt, dispatchDeadlineAt, createdAt, releasedAt, riskAcknowledgedAt } = result;
    return { id, state, expiresAt, dispatchDeadlineAt, createdAt, releasedAt, riskAcknowledgedAt };
  }

  async acknowledgeOrdinary(input: { id: string; conversationId: string; buId: string; actorId: string; confirmed: boolean; validateActorInTransaction: (tx: Prisma.TransactionClient) => Promise<boolean>; auditInTransaction: (tx: Prisma.TransactionClient) => Promise<void> }) {
    if (!input.confirmed) throw new ConflictException({ code: 'DUPLICATION_RISK_CONFIRMATION_REQUIRED' });
    if (!await this.prisma.$transaction(input.validateActorInTransaction)) throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
    const window = await this.admissions.ordinaryRiskWindow(input);
    if (!window) throw new NotFoundException({ code: 'ADMISSION_NOT_FOUND' });
    if (window.eligibleAt && !window.eligible) throw new ConflictException({ code: 'ACK_TOO_EARLY', eligibleAt: window.eligibleAt });
    if (!await this.admissions.acknowledgeOrdinaryRisk({ ...input, validateActor: input.validateActorInTransaction, audit: input.auditInTransaction })) throw new ConflictException({ code: 'ACK_NOT_ELIGIBLE' });
    const { admission } = window;
    return { id: admission.id, acknowledged: true };
  }

  private async conversation(id: string, buId: string) {
    const conversation = await this.prisma.conversation.findFirst({ where: { id, buId } });
    if (!conversation) throw new NotFoundException({ code: 'CONVERSATION_NOT_FOUND' });
    return conversation;
  }
  private projectIntent(intent: InitialMessageIntent) {
    return {
      id: intent.id, state: intent.state, createdAt: intent.createdAt, updatedAt: intent.updatedAt,
      leaseExpiresAt: intent.leaseExpiresAt, dispatchDeadlineAt: intent.dispatchDeadlineAt,
      eligibleAt: ['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state) && intent.slotReleasedAt === null
        ? intent.dispatchDeadlineAt : null,
      slotReleasedAt: intent.slotReleasedAt, externalAccepted: intent.externalMessageId !== null,
      providerAcceptance: intent.externalMessageId !== null ? 'CONFIRMED' : ['SENDING', 'AMBIGUOUS'].includes(intent.state) ? 'UNKNOWN' : 'NOT_ACCEPTED',
      receiptPersistence: intent.externalMessageId !== null ? 'RECORDED' : 'NOT_RECORDED',
      localMessageState: intent.state === 'SUCCEEDED' ? 'RECORDED' : 'UNCONFIRMED',
      recoveryAction: ['PREPARED', 'SENDING', 'EXTERNAL_ACCEPTED', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state)
        ? 'RECONCILE' : intent.state === 'AMBIGUOUS' ? 'ACK_AFTER_DEADLINE' : null,
      riskAcknowledgementAvailable: intent.slotReleasedAt === null && ['AMBIGUOUS', 'EXTERNAL_ACCEPTED_LOCAL_BLOCKED'].includes(intent.state),
    };
  }
  private requestRecord(value: Prisma.JsonValue): Record<string, Prisma.JsonValue> | null {
    return value && typeof value === 'object' && !Array.isArray(value) ? value as Record<string, Prisma.JsonValue> : null;
  }
  private renderTemplate(summary: TemplateSummary, values: Readonly<Record<string, string>> | readonly string[]) {
    try { return renderInitialTemplate(summary, values); }
    catch (error) {
      if (error instanceof InitialTemplateRenderError) throw new ConflictException({ code: error.code });
      throw error;
    }
  }
  private assertGeneration(context: ChannelOperationContext, expected: number) {
    if (context.generation !== expected) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
  }
  private assertManagementContext(operation: ChannelOperationContext, management: TemplateManagementContext) {
    if (operation.channelId !== management.channelId || operation.buId !== management.buId
      || operation.providerResourceIdentityId !== management.providerResourceIdentityId || operation.generation !== management.generation
      || operation.pairingEpoch !== management.pairingEpoch || operation.activeCredentialVersion !== management.activeCredentialVersion
      || operation.providerAccountReference !== management.accountReference) throw new ConflictException({ code: 'CHANNEL_CONTEXT_CHANGED' });
  }
}

```

## Complete current source api-app/src/domain/inbox/conversations.service.ts
```
import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { criarCursorTimeline, lerCursorTimeline } from './timeline-pagination';
import { OutboundService } from './outbound.service';
import { ChannelResolver, type ChannelOrigin } from '../channels/transport/channel';
import type { OutboundAttribution } from './outbound.service';

export const JANELA_MS = 24 * 60 * 60 * 1000;

export interface Atendente {
  userId: string;
  nome: string;
}

@Injectable()
export class ConversationsService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly outbound: OutboundService,
    private readonly channelResolver: ChannelResolver,
  ) {}

  /** Carrega a conversa **dentro do escopo**. Fora dele, ninguém sabe que ela existe. */
  async carregarNoEscopo(conversaId: string, buIdsDoEscopo: string[]) {
    const conversa = await this.prisma.conversation.findFirst({
      where: { id: conversaId, buId: { in: buIdsDoEscopo } },
    });
    if (!conversa) throw new NotFoundException({ error: 'Não encontrado.', code: 'NAO_ENCONTRADO' });
    return conversa;
  }

  /**
   * A inbox pagina.
   *
   * Antes o `take` era 200 fixo, e o que passasse disso era **inalcançável em
   * silêncio** — nada na resposta dizia que cortou. Teto silencioso é o que vira
   * "sumiram conversas" seis meses depois; `temMais` é o mínimo para que quem
   * consome saiba que existe mais.
   */
  async listar(
    buId: string,
    filtro: { status?: string; grupos?: boolean; minhas?: string; pagina?: number; limite?: number },
  ) {
    const limite = Math.min(Math.max(filtro.limite ?? 50, 1), 50);
    const pagina = Math.max(filtro.pagina ?? 1, 1);

    const where: Record<string, unknown> = { buId };
    if (filtro.grupos) where.contactType = 'GRUPO';
    else {
      where.contactType = 'PESSOA';
      if (filtro.status) where.status = filtro.status;
    }
    if (filtro.minhas) where.attendantUserId = filtro.minhas;

    const conditions = [Prisma.sql`bu_id = ${buId}`];
    if (filtro.grupos) conditions.push(Prisma.sql`contact_type = 'GRUPO'::"ContactType"`);
    else {
      conditions.push(Prisma.sql`contact_type = 'PESSOA'::"ContactType"`);
      if (filtro.status) conditions.push(Prisma.sql`status = ${filtro.status}::"ConversationStatus"`);
    }
    if (filtro.minhas) conditions.push(Prisma.sql`attendant_user_id = ${filtro.minhas}`);
    const [total, pageIds] = await Promise.all([
      this.prisma.conversation.count({ where }),
      this.prisma.$queryRaw<Array<{ id: string }>>`
        SELECT id FROM conversations
        WHERE ${Prisma.join(conditions, ' AND ')}
        ORDER BY COALESCE(last_message_at, created_at) DESC, id DESC
        OFFSET ${(pagina - 1) * limite} LIMIT ${limite}
      `,
    ]);
    const loaded = pageIds.length ? await this.prisma.conversation.findMany({
      where: { ...where, id: { in: pageIds.map(({ id }) => id) } },
      select: {
        id: true,
        contact: true,
        contactType: true,
        displayName: true,
        status: true,
        attendantName: true,
        attendantOrigin: true,
        unreadCount: true,
        lastMessageAt: true,
        // O setor é PROJEÇÃO, não modelo (ADR-0017 §3): vem por junção do
        // número. Duplicá-lo na conversa criaria a pergunta "e quando o número
        // muda de setor, o histórico muda junto?" — pergunta que não precisa
        // existir.
        bu: { select: { setor: { select: { id: true, name: true } } } },
      },
    }) : [];
    const loadedById = new Map(loaded.map((conversation) => [conversation.id, conversation]));
    const conversas = pageIds.map(({ id }) => loadedById.get(id)).filter((conversation) => conversation !== undefined);

    return { total, pagina, temMais: pagina * limite < total, conversas };
  }

  /** Página bounded da timeline; o reconhecimento é uma atualização atômica anterior à leitura. */
  async timeline(conversaId: string, limite: number, cursor: string | null, marcarLida: boolean) {
    let ancora: { id: string; createdAt: Date } | null = null;
    if (cursor) {
      const decodificado = lerCursorTimeline(cursor);
      if (decodificado.conversaId !== conversaId) {
        throw new BadRequestException({
          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
        });
      }
      ancora = await this.prisma.message.findFirst({
        where: { id: decodificado.mensagemId, conversationId: conversaId },
        select: { id: true, createdAt: true },
      });
      if (!ancora) {
        throw new BadRequestException({
          error: 'Parâmetros de paginação inválidos.', code: 'PAGINACAO_INVALIDA',
        });
      }
    }

    if (marcarLida) {
      await this.prisma.conversation.updateMany({
        where: { id: conversaId }, data: { unreadCount: 0 },
      });
    }

    const where = ancora
      ? {
          conversationId: conversaId,
          OR: [
            { createdAt: { lt: ancora.createdAt } },
            { createdAt: ancora.createdAt, id: { lt: ancora.id } },
          ],
        }
      : { conversationId: conversaId };
    const encontradas = await this.prisma.message.findMany({
      where,
      orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
      take: limite + 1,
      select: {
        id: true, direction: true, messageType: true, content: true,
        channelOrigin: true, authorName: true, createdAt: true,
      },
    });
    const temAnteriores = encontradas.length > limite;
    const messages = encontradas.slice(0, limite).reverse();
    return {
      messages,
      paginacao: {
        limite,
        temAnteriores,
        cursorAnterior: temAnteriores && messages.length
          ? criarCursorTimeline(conversaId, messages[0].id)
          : null,
      },
    };
  }

  /**
   * Estado da janela de 24h — **atributo do canal, não do produto** (ADR-0009 §3).
   *
   * Numa BU com os dois canais, o canal considerado é o da ÚLTIMA mensagem: a
   * janela fechada no oficial não libera responder pelo não oficial sozinha.
   * Trocar de número no meio da conversa é decisão de quem atende, nunca do
   * sistema.
   */
  async estadoDaJanela(conversaId: string, buId: string) {
    const estado = await this.channelResolver.inspectForConversation({ conversationId: conversaId, buId });
    return {
      canal: estado.channelOrigin ? { type: estado.channelOrigin } : null,
      exigeJanela: estado.requiresWindow,
      aberta: estado.windowOpen,
      expiraEm: estado.expiresAt,
      disponivel: estado.available,
      motivoIndisponibilidade: estado.reason,
    };
  }

  async estadosDasJanelas(references: readonly { conversationId: string; buId: string; latestMessageOrigin: ChannelOrigin | null; latestProviderResourceIdentityId?: string | null }[]) {
    return this.channelResolver.inspectManyForConversations(references);
  }

  async replyOptions(conversationId: string, buId: string) {
    return this.channelResolver.replyOptions(conversationId, buId);
  }

  async responder(conversaId: string, buId: string, texto: string, attribution: OutboundAttribution,
    routeSelection?: { routeId: string; channelId: string; expectedGeneration: number; contextFingerprint: string },
    validateActorInTransaction?: (tx: Prisma.TransactionClient) => Promise<boolean>) {
    return this.outbound.send({ conversationId: conversaId, buId, text: texto, attribution, routeSelection, validateActorInTransaction });
  }

  /** Assumir sem responder. 409 se outro — interno ou externo — já está nela. */
  async assumir(conversaId: string, atendente: Atendente) {
    const conversa = await this.prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
    if (conversa.contactType === 'GRUPO') {
      throw new BadRequestException({ error: 'Grupos não usam fila de atendimento.', code: 'GRUPO_SEM_FILA' });
    }
    if (
      conversa.status === 'IN_SERVICE' &&
      conversa.attendantUserId &&
      conversa.attendantUserId !== atendente.userId
    ) {
      throw new ConflictException({
        error: `Já está sendo atendida por ${conversa.attendantName ?? 'outro agente'}.`,
        code: 'JA_ATENDIDA',
      });
    }
    if (conversa.status === 'IN_SERVICE' && conversa.attendantOrigin === 'EXTERNO' && !conversa.attendantUserId) {
      throw new ConflictException({
        error: `Já está sendo atendida por ${conversa.attendantName ?? 'um sistema externo'}.`,
        code: 'JA_ATENDIDA',
      });
    }

    return this.prisma.conversation.update({
      where: { id: conversa.id },
      data: {
        status: 'IN_SERVICE',
        attendantUserId: atendente.userId,
        attendantName: atendente.nome,
        attendantOrigin: 'INTERNO',
      },
    });
  }

  /** Finalizar. Mensagem nova do contato reabre para QUEUED (ver incoming). */
  async finalizar(conversaId: string) {
    const conversa = await this.prisma.conversation.findUniqueOrThrow({ where: { id: conversaId } });
    if (conversa.contactType === 'GRUPO') {
      throw new BadRequestException({ error: 'Grupos não usam fila de atendimento.', code: 'GRUPO_SEM_FILA' });
    }
    return this.prisma.conversation.update({
      where: { id: conversa.id },
      data: { status: 'CLOSED', attendantUserId: null, attendantName: null, attendantOrigin: null },
    });
  }
}

```

## Complete current source api-app/src/surfaces/bff/conversations.controller.ts
```
import { BadRequestException, Body, ConflictException, Controller, Get, HttpCode, NotFoundException, Param, Post, Query, Req, Res } from '@nestjs/common';
import type { Request, Response } from 'express';
import { AccessService } from '../../domain/access/access.service';
import { exigirPapelNaBu } from '../../domain/access/require-role';
import { ConversationsService } from '../../domain/inbox/conversations.service';
import { RegistroDeAtividade } from '../../domain/historico/registro.service';
import { ator } from './setores.controller';
import { validarConsultaTimeline } from '../../domain/inbox/timeline-pagination';
import { ConversationStartService } from '../../domain/inbox/conversation-start.service';
import { InitialMessageService, type InitialMessagePreviewRequest, type InitialMessageRequest } from '../../domain/inbox/initial-message.service';
import { SessionService } from '../../infra/session/session.service';
import type { Prisma } from '@prisma/client';
import { PrismaService } from '../../infra/prisma/prisma.service';

const ABAS = ['QUEUED', 'IN_SERVICE', 'CLOSED'] as const;

/** A inbox por BU (ADR-0009): uma tela para os dois canais. */
@Controller('api/bff')
export class ConversationsController {
  constructor(
    private readonly access: AccessService,
    private readonly conversas: ConversationsService,
    private readonly registro: RegistroDeAtividade,
    private readonly conversationStart: ConversationStartService,
    private readonly initialMessages: InitialMessageService,
    private readonly sessions: SessionService,
    private readonly prisma: PrismaService,
  ) {}

  @Post('business-units/:buId/conversations/open')
  @HttpCode(200)
  async abrirPorContato(
    @Param('buId') buId: string,
    @Body() body: { telefone?: unknown },
    @Req() req: Request,
    @Res({ passthrough: true }) response: Response,
  ) {
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');
    await this.assertActorTenant(req, buId);
    if (!body || typeof body !== 'object' || Object.keys(body).some((key) => key !== 'telefone')
      || typeof body.telefone !== 'string') {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    const result = await this.conversationStart.start(buId, body.telefone);
    if (result.created) {
      await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.conversa.aberta', ator(req), {
        buId,
        entidadeId: result.conversation.id,
        frase: { contato: result.conversation.contact },
      });
    }
    response.status(result.created ? 201 : 200);
    return {
      conversaId: result.conversation.id,
      criada: result.created,
      contact: result.conversation.contact,
    };
  }

  @Get('conversations/:id/start-options')
  async startOptions(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    return this.initialMessages.options({ conversationId: conversa.id, buId: conversa.buId });
  }

  @Get('conversations/:id/reply-options')
  async replyOptions(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    return this.conversas.replyOptions(conversa.id, conversa.buId);
  }

  @Post('conversations/:id/initial-message-preview')
  @HttpCode(200)
  async initialPreview(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    const message = this.initialMessageRequest(body, false);
    return this.initialMessages.preview({ conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id, message });
  }

  @Post('conversations/:id/initial-messages')
  async initialSend(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request, @Res({ passthrough: true }) response: Response) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    const key = req.header('Idempotency-Key') ?? '';
    const message = this.initialMessageRequest(body, true);
    const result = await this.initialMessages.submit({
      conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id, actorName: req.usuario!.nome,
      idempotencyKey: key, message,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
    });
    const { expiredPrepared, ...safeResult } = result;
    const active = ['SENDING', 'EXTERNAL_ACCEPTED'].includes(result.attempt.state)
      || result.attempt.state === 'PREPARED' && !expiredPrepared;
    response.status(result.expiredPrepared ? 409 : active ? 202 : result.replay ? 200 : result.attempt.state === 'SUCCEEDED' ? 201 : 409);
    return expiredPrepared ? { ...safeResult, code: 'INITIAL_ATTEMPT_EXPIRED' } : safeResult;
  }

  @Get('conversations/:id/initial-messages/:attemptId')
  async initialAttempt(@Param('id') id: string, @Param('attemptId') attemptId: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertUuid(attemptId);
    return this.initialMessages.getAttempt({ id: attemptId, conversationId: conversa.id, buId: conversa.buId });
  }

  @Post('conversations/:id/initial-messages/:attemptId/reconcile')
  @HttpCode(200)
  async reconcileInitial(@Param('id') id: string, @Param('attemptId') attemptId: string, @Body() body: unknown, @Req() req: Request, @Res({ passthrough: true }) response: Response) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(attemptId);
    const result = await this.initialMessages.reconcile({ id: attemptId, conversationId: conversa.id, buId: conversa.buId,
      actorId: req.usuario!.id, actorName: req.usuario!.nome,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx) });
    if (['PREPARED', 'SENDING'].includes(result.state)) response.status(202);
    return result;
  }

  @Post('conversations/:id/initial-messages/:attemptId/acknowledge')
  @HttpCode(200)
  async acknowledgeInitial(@Param('id') id: string, @Param('attemptId') attemptId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(attemptId);
    return this.initialMessages.acknowledge({ id: attemptId, conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id,
      confirmed: req.header('X-Confirm-Duplication-Risk') === 'true', validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
      auditInTransaction: (tx) => this.registro.registrar(tx, req.usuario!.mantenedoraId, 'atendimento.initial.risk_acknowledged', ator(req), { buId: conversa.buId, entidadeId: attemptId }) });
  }

  @Post('conversations/:id/dispatch-admissions/:admissionId/reconcile')
  @HttpCode(200)
  async reconcileAdmission(@Param('id') id: string, @Param('admissionId') admissionId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(admissionId);
    return this.initialMessages.reconcileOrdinary({ id: admissionId, conversationId: conversa.id, buId: conversa.buId,
      validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx) });
  }

  @Post('conversations/:id/dispatch-admissions/:admissionId/acknowledge')
  @HttpCode(200)
  async acknowledgeAdmission(@Param('id') id: string, @Param('admissionId') admissionId: string, @Body() body: unknown, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    await this.assertActorTenant(req, conversa.buId);
    this.assertEmptyBody(body);
    this.assertUuid(admissionId);
    return this.initialMessages.acknowledgeOrdinary({ id: admissionId, conversationId: conversa.id, buId: conversa.buId, actorId: req.usuario!.id,
      confirmed: req.header('X-Confirm-Duplication-Risk') === 'true', validateActorInTransaction: (tx) => this.currentActorHasGrant(req, conversa.buId, tx),
      auditInTransaction: (tx) => this.registro.registrar(tx, req.usuario!.mantenedoraId, 'atendimento.dispatch.risk_acknowledged', ator(req), { buId: conversa.buId, entidadeId: admissionId }) });
  }

  private initialMessageRequest(body: Record<string, unknown>, includeFingerprint: true): InitialMessageRequest;
  private initialMessageRequest(body: Record<string, unknown>, includeFingerprint: false): InitialMessagePreviewRequest;
  private initialMessageRequest(body: Record<string, unknown>, includeFingerprint: boolean): InitialMessageRequest | InitialMessagePreviewRequest {
    if (!body || typeof body !== 'object' || Array.isArray(body)) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    const allowed = ['channelId', 'expectedGeneration', 'mensagem', ...(includeFingerprint ? ['previewFingerprint'] : [])];
    if (Object.keys(body).some((key) => !allowed.includes(key)) || typeof body.channelId !== 'string'
      || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(body.channelId)
      || !Number.isSafeInteger(body.expectedGeneration) || (body.expectedGeneration as number) < 1
      || includeFingerprint && (typeof body.previewFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(body.previewFingerprint))) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    const message = body.mensagem;
    if (!message || typeof message !== 'object' || Array.isArray(message)) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    const row = message as Record<string, unknown>;
    const base = { channelId: body.channelId, expectedGeneration: body.expectedGeneration as number };
    const preview = includeFingerprint ? { previewFingerprint: body.previewFingerprint as string } : {};
    if (row.tipo === 'TEXTO') {
      if (Object.keys(row).some((key) => !['tipo', 'texto'].includes(key)) || typeof row.texto !== 'string'
        || !row.texto.trim() || [...row.texto].length > 4096) throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
      return { ...base, kind: 'text' as const, text: row.texto, ...preview };
    }
    if (row.tipo !== 'TEMPLATE' || Object.keys(row).some((key) => !['tipo', 'templateId', 'language', 'catalogAfter', 'expectedDefinitionFingerprint', 'parameters'].includes(key))
      || typeof row.templateId !== 'string' || !row.templateId || row.templateId.length > 128
      || typeof row.language !== 'string' || !row.language || row.language.length > 16
      || row.catalogAfter !== undefined && (typeof row.catalogAfter !== 'string' || row.catalogAfter.length < 1 || row.catalogAfter.length > 512)
      || typeof row.expectedDefinitionFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(row.expectedDefinitionFingerprint)
      || !row.parameters || typeof row.parameters !== 'object'
      || Array.isArray(row.parameters) && (row.parameters.length > 20 || row.parameters.some((value) => typeof value !== 'string' || !value || [...value].length > 1024))
      || !Array.isArray(row.parameters) && (Object.keys(row.parameters as object).length > 20 || Object.values(row.parameters as Record<string, unknown>).some((value) => typeof value !== 'string' || !value || [...value].length > 1024))) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    return { ...base, kind: 'approved-template' as const, remoteTemplateId: row.templateId, language: row.language,
      catalogAfter: typeof row.catalogAfter === 'string' ? row.catalogAfter : null,
      expectedDefinitionFingerprint: row.expectedDefinitionFingerprint,
      values: row.parameters as Record<string, string> | string[], ...preview };
  }

  private assertEmptyBody(body: unknown): void {
    if (body !== undefined && (!body || typeof body !== 'object' || Array.isArray(body) || Object.keys(body).length !== 0)) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
  }

  private assertUuid(value: string): void {
    if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(value)) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
  }

  private async currentActorHasGrant(req: Request, buId: string, tx: Prisma.TransactionClient): Promise<boolean> {
    const cookie = this.sessions.extrairDoCabecalho(req.headers.cookie);
    const claimsAtRequest = this.sessions.verificar(cookie);
    if (!claimsAtRequest || claimsAtRequest.uid !== req.usuario!.id) return false;
    let rows: Array<{ id: string; user_status: string; password_changed_at: Date | null;
      user_mantenedora_id: string; bu_status: string; bu_mantenedora_id: string; role: string }>;
    try {
      rows = await tx.$queryRaw<Array<{ id: string; user_status: string; password_changed_at: Date | null;
        user_mantenedora_id: string; bu_status: string; bu_mantenedora_id: string; role: string }>>`
        SELECT u.id, u.status::text AS user_status, u.password_changed_at,
          u.mantenedora_id AS user_mantenedora_id, b.status::text AS bu_status,
          b.mantenedora_id AS bu_mantenedora_id, r.role::text AS role
        FROM app_users u
        JOIN user_bu_roles r ON r.user_id = u.id AND r.bu_id = ${buId}
        JOIN business_units b ON b.id = r.bu_id
        WHERE u.id = ${claimsAtRequest.uid}
        FOR SHARE OF u, r, b NOWAIT`;
    } catch (error) {
      const candidate = error as { code?: unknown; meta?: { code?: unknown; message?: unknown }; cause?: { code?: unknown } };
      const lockCode = candidate.meta?.code ?? candidate.cause?.code ?? candidate.code;
      if (lockCode === '55P03' || candidate.meta?.message === '55P03'
        || typeof candidate.meta?.message === 'string' && candidate.meta.message.includes('55P03')) {
        throw new ConflictException({ code: 'CURRENT_GRANT_REQUIRED' });
      }
      throw error;
    }
    const current = rows[0];
    const claimsNow = this.sessions.verificar(cookie);
    return Boolean(current && claimsNow && claimsNow.uid === claimsAtRequest.uid
      && claimsNow.iat === claimsAtRequest.iat && claimsNow.exp === claimsAtRequest.exp
      && claimsNow.exp > Date.now() && current.user_status === 'ATIVO'
      && current.bu_status === 'ATIVO' && current.user_mantenedora_id === current.bu_mantenedora_id
      && (!current.password_changed_at || current.password_changed_at.getTime() <= claimsNow.iat)
      && ['ATENDENTE', 'ADMIN', 'OWNER'].includes(current.role));
  }

  /** New initial-contact routes require the actor's home tenant to match the BU. */
  private async assertActorTenant(req: Request, buId: string): Promise<void> {
    const rows = await this.prisma.$queryRaw<Array<{ user_id: string; user_mantenedora_id: string; bu_mantenedora_id: string; user_status: string; bu_status: string }>>`
      SELECT u.id AS user_id, u.mantenedora_id AS user_mantenedora_id,
        b.mantenedora_id AS bu_mantenedora_id, u.status::text AS user_status,
        b.status::text AS bu_status
      FROM app_users u CROSS JOIN business_units b
      WHERE u.id = ${req.usuario!.id} AND b.id = ${buId}`;
    const row = rows[0];
    if (!row || row.user_status !== 'ATIVO' || row.bu_status !== 'ATIVO'
      || row.user_mantenedora_id !== row.bu_mantenedora_id) throw new NotFoundException();
  }

  @Get('business-units/:buId/conversations')
  async listar(
    @Param('buId') buId: string,
    @Query() q: Record<string, string>,
    @Req() req: Request,
  ) {
    // Estar no escopo BASTA: com o eixo de capacidades dissolvido (ADR-0018 §3),
    // quem tem grant na BU atende as conversas dela. Era isso que a capacidade
    // ATENDIMENTO dizia, e agora quem diz é o papel.
    await exigirPapelNaBu(this.access, req.usuario!.id, buId, 'ATENDENTE');

    const aba = q.aba?.toUpperCase();
    const r = await this.conversas.listar(buId, {
      grupos: aba === 'GRUPO',
      status: ABAS.includes(aba as (typeof ABAS)[number]) ? aba : undefined,
      minhas: q.minhas === 'true' ? req.usuario!.id : undefined,
      pagina: q.pagina ? Number(q.pagina) : undefined,
      limite: q.limite ? Number(q.limite) : undefined,
    });
    // O setor sobe achatado, como a tela o consome (`conversa.setor`).
    return {
      total: r.total,
      pagina: r.pagina,
      temMais: r.temMais,
      conversations: r.conversas.map(({ bu, ...c }) => ({ ...c, setor: bu.setor.name })),
    };
  }

  @Get('conversations/:id/messages')
  async thread(@Param('id') id: string, @Query() q: Record<string, unknown>, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);
    // Validar somente depois do resolver: recurso fora do escopo permanece 404,
    // mesmo quando os parâmetros enviados são inválidos.
    const consulta = validarConsultaTimeline(q);
    const timeline = await this.conversas.timeline(
      conversa.id, consulta.limite, consulta.antes, consulta.marcarLida,
    );

    const janela = await this.conversas.estadoDaJanela(conversa.id, conversa.buId);
    return {
      conversa: {
        id: conversa.id,
        contato: conversa.contact,
        nome: conversa.displayName,
        status: conversa.status,
        atendente: conversa.attendantName,
      },
      // O front precisa saber que "responder" pode estar indisponível, e por quê.
      janela: {
        exigida: janela.exigeJanela,
        aberta: janela.aberta,
        expiraEm: janela.expiraEm,
        canal: janela.canal?.type ?? null,
        disponivel: janela.disponivel,
        motivo: janela.motivoIndisponibilidade,
      },
      messages: timeline.messages,
      paginacao: timeline.paginacao,
    };
  }

  @Post('conversations/:id/messages')
  @HttpCode(201)
  async responder(@Param('id') id: string, @Body() body: Record<string, unknown>, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);

    const allowed = ['texto', 'schemaVersion', 'routeId', 'channelId', 'expectedGeneration', 'contextFingerprint'];
    if (!body || typeof body !== 'object' || body.schemaVersion !== 2 || Object.keys(body).length !== allowed.length
      || Object.keys(body).some((key) => !allowed.includes(key)) || typeof body.routeId !== 'string'
      || typeof body.channelId !== 'string' || !Number.isSafeInteger(body.expectedGeneration)
      || typeof body.contextFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(body.contextFingerprint)) {
      throw new BadRequestException({ code: 'REQUISICAO_INVALIDA' });
    }
    const routeSelection = { routeId: body.routeId, channelId: body.channelId,
      expectedGeneration: body.expectedGeneration as number, contextFingerprint: body.contextFingerprint };

    const texto = String(body?.texto ?? '').trim();
    if (!texto) throw new BadRequestException({ error: 'Escreva uma mensagem.', code: 'TEXTO_VAZIO' });
    const selectedOrigin = await this.prisma.buChannel.findFirst({ where: { id: routeSelection.channelId, buId: conversa.buId }, select: { type: true } });
    const maxLength = selectedOrigin?.type === 'INSTAGRAM' ? 1000 : 4096;
    if (Array.from(texto).length > maxLength) throw new BadRequestException({ error: 'Mensagem muito longa.', code: 'TEXTO_LONGO' });

    await this.initialMessages.assertOrdinaryDispatchAllowed(conversa.id, conversa.buId);

    const m = await this.conversas.responder(conversa.id, conversa.buId, texto, {
      kind: 'BFF',
      userId: req.usuario!.id,
      name: req.usuario!.nome,
    }, routeSelection, (tx) => this.currentActorHasGrant(req, conversa.buId, tx));
    return { id: m.id, canal: m.channelOrigin, em: m.createdAt };
  }

  @Post('conversations/:id/claim')
  async assumir(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);

    const c = await this.conversas.assumir(conversa.id, { userId: req.usuario!.id, nome: req.usuario!.nome });
    await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.assumido', ator(req), {
      buId: conversa.buId,
      entidadeId: conversa.id,
      frase: { contato: conversa.contact },
    });
    return { id: c.id, status: c.status, atendente: c.attendantName };
  }

  @Post('conversations/:id/close')
  async finalizar(@Param('id') id: string, @Req() req: Request) {
    const { conversa } = await this.resolver(id, req);

    const c = await this.conversas.finalizar(conversa.id);
    await this.registro.registrarSolto(req.usuario!.mantenedoraId, 'atendimento.encerrado', ator(req), {
      buId: conversa.buId,
      entidadeId: conversa.id,
      frase: { contato: conversa.contact },
    });
    return { id: c.id, status: c.status };
  }

  /** Escopo primeiro: fora dele, 404 — inclusive para BU de outra Mantenedora. */
  private async resolver(conversaId: string, req: Request) {
    const escopo = await this.access.escopo(req.usuario!.id);
    const conversa = await this.conversas.carregarNoEscopo(conversaId, escopo);
    const bu = await exigirPapelNaBu(this.access, req.usuario!.id, conversa.buId, 'ATENDENTE');
    return { conversa, papel: bu.papel };
  }
}

```

## Complete current source api-app/src/infra/session/session.service.ts
```
import { Injectable } from '@nestjs/common';
import { createHmac, timingSafeEqual } from 'node:crypto';

export const SESSION_COOKIE = 'lh_session';

export type SameSite = 'Lax' | 'Strict' | 'None';

/**
 * Lê `COOKIE_SAMESITE` sem exigir que ninguém acerte a caixa.
 *
 * O valor é o do atributo do cookie (`None`, com N maiúsculo), mas aceitar só a
 * forma exata seria uma armadilha: quem escrevesse `none` receberia `Lax` em
 * silêncio, e o sintoma seria exatamente o login mudo que a variável existe para
 * resolver. Vazio e desconhecido caem em `Lax` — nunca no mais permissivo.
 */
export function normalizarSameSite(valor: string | undefined): SameSite {
  switch (valor?.trim().toLowerCase()) {
    case 'none':
      return 'None';
    case 'strict':
      return 'Strict';
    default:
      return 'Lax';
  }
}

/** Um valor escrito e não reconhecido é engano de quem configurou, não default. */
export function valorDeSameSiteEhSuspeito(valor: string | undefined): boolean {
  const v = valor?.trim();
  if (!v) return false;
  return !['none', 'lax', 'strict'].includes(v.toLowerCase());
}

/** 1 dia — limita a janela de risco de um computador esquecido logado (ADR-0007). */
const DURACAO_MS = 24 * 60 * 60 * 1000;

export interface SessionClaims {
  /** id do app_user. O papel NÃO vem aqui: ele é lido do banco a cada request. */
  uid: string;
  iat: number;
  exp: number;
}

/**
 * Cookie de sessão assinado (ADR-0007 §1).
 *
 * O corpo carrega apenas `uid`, `iat` e `exp`. Papel, capacidade e escopo ficam
 * de fora de propósito: se viajassem no cookie, promoção e rebaixamento só
 * valeriam no próximo login.
 */
@Injectable()
export class SessionService {
  private readonly segredo = process.env.SESSION_SECRET ?? '';

  get configurado(): boolean {
    return this.segredo.length > 0;
  }

  assinar(uid: string, agora = Date.now()): string {
    const claims: SessionClaims = { uid, iat: agora, exp: agora + DURACAO_MS };
    const corpo = Buffer.from(JSON.stringify(claims)).toString('base64url');
    return `${corpo}.${this.hmac(corpo)}`;
  }

  verificar(token: string | undefined, agora = Date.now()): SessionClaims | null {
    if (!token || !token.includes('.')) return null;
    const [corpo, assinatura] = token.split('.');
    if (!corpo || !assinatura) return null;
    if (!this.assinaturaConfere(corpo, assinatura)) return null;

    try {
      const claims = JSON.parse(Buffer.from(corpo, 'base64url').toString()) as SessionClaims;
      if (!claims.uid || typeof claims.exp !== 'number') return null;
      if (agora > claims.exp) return null;
      return claims;
    } catch {
      return null;
    }
  }

  /**
   * `Secure` só fora de desenvolvimento: em http local o navegador descartaria
   * o cookie.
   *
   * `Domain` vem de COOKIE_DOMAIN e é o que faz o cookie emitido pela API valer
   * no subdomínio do front (ADR-0015). SameSite continua `Lax` porque
   * subdomínios do mesmo domínio são o **mesmo site** — sem essa variável, o
   * cookie fica preso ao host que o emitiu e o login "funciona e não entra".
   */
  cookie(token: string): string {
    const maxAge = Math.floor(DURACAO_MS / 1000);
    return `${SESSION_COOKIE}=${token}; HttpOnly;${this.atributos()} Max-Age=${maxAge}`;
  }

  cookieVazio(): string {
    return `${SESSION_COOKIE}=;${this.atributos()} HttpOnly; Max-Age=0`;
  }

  /**
   * `SameSite` é `Lax` por padrão, e é assim que produção tem de ficar.
   *
   * `COOKIE_SAMESITE=None` existe para UM caso: stage nos domínios gerados pela
   * Railway. `*.up.railway.app` é sufixo público, então dois serviços ali são
   * **sites diferentes** — o navegador recusa `Domain` compartilhado e o `Lax`
   * bloqueia o envio. O sintoma é mudo: o login responde 200, o Set-Cookie
   * chega, e a requisição seguinte vai sem cookie.
   *
   * O preço de `None`: a proteção de CSRF passa a depender **só** do cabeçalho
   * `X-Requested-With` exigido no que muda estado. Aceitável num ambiente de QA,
   * inaceitável em produção — ver ADR-0015, Emenda 1.
   */
  private atributos(): string {
    const sameSite = normalizarSameSite(process.env.COOKIE_SAMESITE);
    // `SameSite=None` sem `Secure` é recusado por todo navegador atual, então o
    // Secure deixa de depender do NODE_ENV quando ele está ligado.
    const secure = sameSite === 'None' || process.env.NODE_ENV === 'production' ? ' Secure;' : '';
    const dominio = process.env.COOKIE_DOMAIN ? ` Domain=${process.env.COOKIE_DOMAIN};` : '';
    return `${secure}${dominio} SameSite=${sameSite}; Path=/;`;
  }

  extrairDoCabecalho(cookieHeader: string | undefined): string | undefined {
    if (!cookieHeader) return undefined;
    for (const parte of cookieHeader.split(';')) {
      const [nome, ...resto] = parte.trim().split('=');
      if (nome === SESSION_COOKIE) return resto.join('=');
    }
    return undefined;
  }

  private hmac(corpo: string): string {
    return createHmac('sha256', this.segredo).update(corpo).digest('base64url');
  }

  private assinaturaConfere(corpo: string, assinatura: string): boolean {
    const esperada = Buffer.from(this.hmac(corpo));
    const recebida = Buffer.from(assinatura);
    if (esperada.length !== recebida.length) return false;
    return timingSafeEqual(esperada, recebida);
  }
}

```

## Complete current source api-app/src/domain/access/access.service.ts
```
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { Role } from './role';
import { Grant, buNoEscopo, escopoDoUsuario, papelNaBu, papelNaMantenedora } from './scope';

/**
 * A única porta por onde um `bu_id` vindo do request pode passar.
 *
 * Regra 0 do CLAUDE.md: toda leitura de dado de negócio filtra por BU dentro do
 * escopo do usuário, e a Mantenedora intersecciona esse conjunto — nunca o soma.
 */
@Injectable()
export class AccessService {
  constructor(private readonly prisma: PrismaService) {}

  async grantsDoUsuario(userId: string): Promise<Grant[]> {
    const linhas = await this.prisma.userBuRole.findMany({
      where: { userId, bu: { status: 'ATIVO' } },
      select: { buId: true, role: true, grantedViaTipo: true, grantedViaId: true },
    });
    return linhas.map((l) => ({
      buId: l.buId,
      role: l.role as Role,
      origemTipo: l.grantedViaTipo,
      origemId: l.grantedViaId,
    }));
  }

  async escopo(userId: string): Promise<string[]> {
    return escopoDoUsuario(await this.grantsDoUsuario(userId));
  }

  /**
   * Resolve uma BU pedida contra os grants. Devolve null quando não pode ser
   * vista — e quem chama responde **404**, não 403: confirmar a existência de
   * recurso alheio entrega informação a quem varre identificadores.
   */
  async resolverBu(userId: string, buId: string): Promise<{ id: string; name: string; papel: Role } | null> {
    const grants = await this.grantsDoUsuario(userId);
    if (!buNoEscopo(grants, buId)) return null;

    const bu = await this.prisma.businessUnit.findFirst({
      where: { id: buId, status: 'ATIVO' },
      select: { id: true, name: true },
    });
    if (!bu) return null;

    const papel = papelNaBu(grants, buId);
    if (!papel) return null;
    return { id: bu.id, name: bu.name, papel };
  }

  /** Papel na Mantenedora: calculado, nunca armazenado (ADR-0008 §4). */
  async papelNaMantenedoraDoUsuario(userId: string, mantenedoraId: string): Promise<Role | null> {
    const grants = await this.grantsDoUsuario(userId);
    const bus = await this.prisma.businessUnit.findMany({
      where: { mantenedoraId, status: 'ATIVO' },
      select: { id: true },
    });
    return papelNaMantenedora(grants, bus.map((b) => b.id));
  }
}

```

## Complete current source api-app/src/domain/access/scope.ts
```
import { Role, atLeast, menorPapel } from './role';

// Escopo e papel derivado. A regra 0 do CLAUDE.md vive aqui: o escopo é o
// conjunto de BUs concedidas, e a Mantenedora INTERSECCIONA esse conjunto,
// nunca o soma.

/** De onde o grant veio (ADR-0017 §2). */
export type OrigemDoGrant = 'DIRETO' | 'SETOR' | 'MANTENEDORA';

export interface Grant {
  buId: string;
  role: Role;
  origemTipo: OrigemDoGrant;
  /** null quando DIRETO; o id do setor ou da Mantenedora quando é expansão. */
  origemId: string | null;
}

/** As BUs que o usuário enxerga. Sem grant, conjunto vazio — nunca "todas". */
export function escopoDoUsuario(grants: readonly Grant[]): string[] {
  return [...new Set(grants.map((g) => g.buId))];
}

/**
 * A BU pedida está no escopo? É a única porta por onde um bu_id vindo do
 * request pode passar.
 */
export function buNoEscopo(grants: readonly Grant[], buId: string): boolean {
  return grants.some((g) => g.buId === buId);
}

/** O papel numa BU específica. Ausência de grant é negação, não fallback. */
export function papelNaBu(grants: readonly Grant[], buId: string): Role | null {
  return grants.find((g) => g.buId === buId)?.role ?? null;
}

/**
 * Papel na Mantenedora — CALCULADO, nunca armazenado (ADR-0008 §4):
 *
 *  - sem grant em nenhuma BU  -> null (não enxerga)
 *  - grant em ALGUMAS         -> ATENDENTE (enxerga, mas não administra)
 *  - grant em TODAS           -> o MENOR papel entre elas
 *
 * Mantenedora sem BU nenhuma devolve null: "administrada por ninguém", não
 * "por qualquer um".
 *
 * O piso do grant parcial era `VIEWER` e passou a ser `ATENDENTE` (ADR-0018 §2).
 * **Isso não afrouxa nada:** quem tinha VIEWER derivado não administrava, e quem
 * tem ATENDENTE derivado também não — `podeAdministrarMantenedora` continua
 * exigindo >= ADMIN em TODAS as BUs. A derivação nunca concedeu acesso a BU
 * alguma; ela só resume.
 */
export function papelNaMantenedora(
  grants: readonly Grant[],
  todasAsBusDaMantenedora: readonly string[],
): Role | null {
  if (todasAsBusDaMantenedora.length === 0) return null;

  const doEscopo = grants.filter((g) => todasAsBusDaMantenedora.includes(g.buId));
  if (doEscopo.length === 0) return null;
  if (doEscopo.length < todasAsBusDaMantenedora.length) return 'ATENDENTE';

  return menorPapel(doEscopo.map((g) => g.role));
}

/**
 * Administrar o agrupamento (conceder em lote, renomear, integrações) exige
 * papel >= ADMIN em TODAS as BUs.
 *
 * O conjunto vazio é negado ANTES da contagem, de propósito: "em todas" seria
 * verdadeiro por vacuidade numa Mantenedora sem BU, o que daria a qualquer um o
 * direito de administrá-la.
 */
export function podeAdministrarMantenedora(
  grants: readonly Grant[],
  todasAsBusDaMantenedora: readonly string[],
): boolean {
  const papel = papelNaMantenedora(grants, todasAsBusDaMantenedora);
  return papel !== null && atLeast(papel, 'ADMIN');
}

/**
 * Expansão: cria uma linha por BU, e GRANT DIRETO VENCE EXPANSÃO — a expansão só
 * cria onde não existe **nenhum** grant (ADR-0008 §4, regra 1).
 *
 * Vale para as duas origens, Mantenedora e Setor: a regra é a mesma, e é isso
 * que faz o Setor não ser um eixo novo de permissão, só mais uma proveniência
 * (ADR-0017 §2).
 *
 * É também este ponto que faz o grant do fundador nascer como expansão em vez de
 * direto: no gateway_unifast o fundador recebeu grant direto, a replicação não o
 * enxergou, e ele perdeu a administração da conta que criou.
 */
export function expandir(
  grantsAtuais: readonly Grant[],
  bus: readonly string[],
  role: Role,
  origemTipo: Exclude<OrigemDoGrant, 'DIRETO'>,
  origemId: string,
): Grant[] {
  const jaTemGrant = new Set(grantsAtuais.map((g) => g.buId));
  return bus.filter((buId) => !jaTemGrant.has(buId)).map((buId) => ({ buId, role, origemTipo, origemId }));
}

/**
 * Revogar em lote remove só o que AQUELA origem criou. O grant direto sobrevive,
 * e o que veio de outra origem também (ADR-0008 §4 regra 2, ADR-0017 §2).
 */
export function revogarExpansao(
  grants: readonly Grant[],
  origemTipo: Exclude<OrigemDoGrant, 'DIRETO'>,
  origemId: string,
): Grant[] {
  return grants.filter((g) => !(g.origemTipo === origemTipo && g.origemId === origemId));
}

/**
 * Mover um número de setor reescreve **só as expansões de setor daquele número**
 * (ADR-0017 §2, regra 5).
 *
 * Sai o que o setor antigo concedia; entra o que o novo concede, onde não houver
 * grant. O grant DIRETO sobrevive — e o vindo da Mantenedora também: os dois
 * continuam valendo e, por isso, **bloqueiam** a expansão do setor novo, que é a
 * regra 1 aplicada aqui.
 *
 * A diferença que isso preserva é entre "perdeu porque o time mudou" e "perdeu
 * porque alguém arrumou o cadastro".
 */
export function reescreverExpansaoAoMover(
  grantsDaBu: readonly { userId: string; origemTipo: OrigemDoGrant; origemId: string | null }[],
  setorAntigo: string,
  expansoesDoSetorNovo: readonly { userId: string; role: Role }[],
): { remover: string[]; adicionar: { userId: string; role: Role }[] } {
  const remover: string[] = [];
  // Quem continua com grant nesta BU depois da remoção — e por isso não recebe
  // expansão do setor novo.
  const permanecem = new Set<string>();

  for (const g of grantsDaBu) {
    if (g.origemTipo === 'SETOR' && g.origemId === setorAntigo) remover.push(g.userId);
    else permanecem.add(g.userId);
  }

  return { remover, adicionar: expansoesDoSetorNovo.filter((e) => !permanecem.has(e.userId)) };
}

```

## Complete current source api-app/src/integrations/channels/instagram-channel.ts
```
import type { Channel, ChannelMessage, ChannelMessageKind, ChannelSendOptions, ChannelSendResult } from '../../domain/channels/transport/channel';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { InstagramMessagingClient } from '../instagram/instagram-messaging.client';
import { ChannelAdapterFactory } from './channel-adapter-factory';
import { instagramConfig } from '../instagram/instagram-http.client';

class BoundInstagramChannel implements Channel {
  readonly supportedKinds: readonly ChannelMessageKind[] = Object.freeze(['text']);

  constructor(private readonly credential: ResolvedChannelCredential, private readonly client: InstagramMessagingClient,
    private readonly beforeDispatch: () => Promise<boolean>) {}

  async sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult> {
    if (message.kind !== 'text') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (options?.purpose === 'initial') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (!this.credential.instagramAccountId || !this.credential.accessToken) return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
    if (!await this.beforeDispatch().catch(() => false)) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    const finalDispatchFence = async () => {
      // Claim may await locks/DB work until the captured token approaches expiry.
      if (!await this.beforeDispatch().catch(() => false)) return false;
      if (!options?.beforeDispatch || !await options.beforeDispatch().catch(() => false)) return false;
      return Boolean(this.credential.expiresAt && Date.now() < this.credential.expiresAt.getTime());
    };
    return this.client.sendMessage(this.credential.instagramAccountId, message.recipientRef, message.text,
      this.credential.accessToken, finalDispatchFence);
  }
}

export class InstagramChannelFactory extends ChannelAdapterFactory {
  readonly origin = 'INSTAGRAM' as const;

  constructor(private readonly client: InstagramMessagingClient) { super(); }

  locallyConfigured(): boolean { return instagramConfig() !== null; }

  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundInstagramChannel(credential, this.client, beforeDispatch);
  }
}

```

## Complete current source api-app/src/integrations/channels/meta-channel.ts
```
import type { Channel, ChannelMessage, ChannelMessageKind, ChannelSendOptions, ChannelSendResult } from '../../domain/channels/transport/channel';
import type { MetaClient } from '../meta/meta.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';
import { MetaInitialMessageClient } from '../meta/initial-message.client';
import { metaAccountReference } from './account-reference';

class BoundMetaChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: MetaClient,
    private readonly initialClient: MetaInitialMessageClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  readonly supportedKinds: readonly ChannelMessageKind[] = Object.freeze(['text', 'approved-template']);

  async sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult> {
    // Approved templates always use the initial protocol path; text selects
    // that path explicitly so ordinary text retains its legacy wire format.
    if (options?.purpose === 'initial' || message.kind === 'approved-template') {
      const claimFence = options?.beforeDispatch;
      if (!claimFence) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
      if (!this.credential.phoneNumberId || !this.credential.wabaId || !this.credential.accessToken) {
        return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
      }
      if (!/^\d{8,15}$/.test(message.recipientRef)) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
      const template = message.kind === 'approved-template' ? message.template : null;
      const managementContext = template?.managementContext;
      return this.initialClient.sendInitialMessage({
        wabaId: this.credential.wabaId,
        phoneNumberId: this.credential.phoneNumberId,
        recipientE164: `+${message.recipientRef}`,
        accessToken: this.credential.accessToken,
        accountReference: metaAccountReference(this.credential.wabaId),
        payload: message,
        ...(managementContext ? { managementContext } : {}),
        beforeDispatch: async () => {
          const contextCurrent = await this.beforeDispatch().catch(() => false);
          if (!contextCurrent) return false;
          try { return await claimFence(); } catch { return false; }
        },
      });
    }
    if (message.kind !== 'text') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    if (!this.credential.phoneNumberId || !this.credential.accessToken) {
      return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
    }
    if (options?.beforeDispatch) {
      let dispatched: boolean;
      try { dispatched = await options.beforeDispatch(); } catch { dispatched = false; }
      if (!dispatched) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    try {
      return await this.client.enviarTexto(
        this.credential.phoneNumberId,
        message.recipientRef,
        message.text,
        this.credential.accessToken,
      );
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'META_RECUSOU' };
    }
  }
}

export class MetaChannelFactory extends ChannelAdapterFactory {
  readonly origin = 'OFICIAL' as const;
  constructor(private readonly client: MetaClient, private readonly initialClient: MetaInitialMessageClient) { super(); }
  locallyConfigured(): boolean { return this.client.canSendText(); }
  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundMetaChannel(credential, this.client, this.initialClient, beforeDispatch);
  }
}

```

## Complete current source api-app/src/integrations/channels/evolution-channel.ts
```
import type { Channel, ChannelMessage, ChannelMessageKind, ChannelSendOptions, ChannelSendResult } from '../../domain/channels/transport/channel';
import type { EvolutionClient } from '../evolution/evolution.client';
import type { ResolvedChannelCredential } from '../../domain/channels/channel-credential-resolver';
import { ChannelAdapterFactory } from './channel-adapter-factory';

class BoundEvolutionChannel implements Channel {
  constructor(
    private readonly credential: ResolvedChannelCredential,
    private readonly client: EvolutionClient,
    private readonly beforeDispatch: () => Promise<boolean>,
  ) {}

  readonly supportedKinds: readonly ChannelMessageKind[] = Object.freeze(['text']);

  async sendMessage(message: ChannelMessage, options?: ChannelSendOptions): Promise<ChannelSendResult> {
    if (message.kind !== 'text') return { outcome: 'BLOCKED', reason: 'UNSUPPORTED_KIND' };
    if (!await this.beforeDispatch()) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    if (options?.purpose === 'initial' && !options.beforeDispatch) {
      return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (options?.beforeDispatch) {
      let dispatched: boolean;
      try { dispatched = await options.beforeDispatch(); } catch { dispatched = false; }
      if (!dispatched) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (!this.credential.evolutionInstanceName) return { outcome: 'BLOCKED', reason: 'CHANNEL_NOT_READY' };
    try {
      return await this.client.enviarTexto(this.credential.evolutionInstanceName, message.recipientRef, message.text);
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'EVOLUTION_RECUSOU' };
    }
  }
}

export class EvolutionChannelFactory extends ChannelAdapterFactory {
  readonly origin = 'NAO_OFICIAL' as const;
  constructor(private readonly client: EvolutionClient) { super(); }
  locallyConfigured(): boolean { return this.client.configurado(); }
  create(credential: ResolvedChannelCredential, beforeDispatch: () => Promise<boolean>): Channel {
    return new BoundEvolutionChannel(credential, this.client, beforeDispatch);
  }
}

```

## Complete current source api-app/src/integrations/instagram/instagram-messaging.client.ts
```
import { Inject, Injectable, Optional } from '@nestjs/common';
import { INSTAGRAM_HTTP_FETCH, type InstagramFetch } from './instagram-http.client';

const GRAPH = 'https://graph.instagram.com/v26.0';

export type InstagramMessageResult =
  | { outcome: 'ACCEPTED'; externalMessageId: string }
  | { outcome: 'BLOCKED'; reason: 'CHANNEL_CONTEXT_CHANGED' | 'PENDING_CREDENTIAL' | 'CHANNEL_NOT_READY' }
  | { outcome: 'UNKNOWN'; evidence: 'ACK_WITHOUT_ID' | 'TRANSPORT_UNCONFIRMED'; legacyCode: string };

/** Fixed Instagram Login plaintext-reply wire boundary; no endpoint or payload can be caller-selected. */
@Injectable()
export class InstagramMessagingClient {
  constructor(@Optional() @Inject(INSTAGRAM_HTTP_FETCH) private readonly request: InstagramFetch = fetch) {}

  async sendMessage(accountId: string, peerId: string, text: string, accessToken: string,
    beforeDispatch?: () => Promise<boolean>): Promise<InstagramMessageResult> {
    if (!/^[A-Za-z0-9_.:-]{1,256}$/.test(accountId) || !/^[A-Za-z0-9_.:-]{1,256}$/.test(peerId)
      || !text.trim() || Array.from(text).length > 1000) {
      return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    }
    if (!accessToken) return { outcome: 'BLOCKED', reason: 'PENDING_CREDENTIAL' };
    if (beforeDispatch && !await beforeDispatch().catch(() => false)) return { outcome: 'BLOCKED', reason: 'CHANNEL_CONTEXT_CHANGED' };
    const url = `${GRAPH}/${encodeURIComponent(accountId)}/messages`;
    try {
      const response = await this.request(url, { method: 'POST', redirect: 'error', signal: AbortSignal.timeout(10_000),
        headers: { authorization: `Bearer ${accessToken}`, 'content-type': 'application/json' },
        body: JSON.stringify({ recipient: { id: peerId }, message: { text } }) });
      if (!response.ok) return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'INSTAGRAM_UNCONFIRMED' };
      const body: unknown = await response.json();
      if (!body || typeof body !== 'object' || Array.isArray(body)) return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'INSTAGRAM_ACK_INVALID' };
      const ack = body as Record<string, unknown>;
      if ('recipient_id' in ack && (typeof ack.recipient_id !== 'string' || ack.recipient_id !== peerId)) {
        return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'INSTAGRAM_ACK_RECIPIENT_MISMATCH' };
      }
      const id = ack.message_id;
      return typeof id === 'string' && id.length > 0 && id.length <= 256
        ? { outcome: 'ACCEPTED', externalMessageId: id }
        : { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'INSTAGRAM_ACK_WITHOUT_ID' };
    } catch {
      return { outcome: 'UNKNOWN', evidence: 'TRANSPORT_UNCONFIRMED', legacyCode: 'INSTAGRAM_UNCONFIRMED' };
    }
  }
}

```

## Complete current source api-app/src/domain/channels/channels.service.ts
```
import { createHash, randomUUID } from 'node:crypto';
import {
  ConflictException,
  Inject,
  Injectable,
  ServiceUnavailableException,
  Optional,
} from '@nestjs/common';
import { PrismaService } from '../../infra/prisma/prisma.service';
import {
  EVOLUTION_CLIENT,
  EvolutionClient,
} from '../../integrations/evolution/evolution.client';
import { META_CLIENT, MetaClient, MetaIndisponivelError, type MetaNumber } from '../../integrations/meta/meta.client';
import { ChannelCredentialResolver } from './channel-credential-resolver';
import { RegistroDeAtividade } from '../historico/registro.service';
import { convergeReceiptVerifiedAttempt } from './receipt-attempt-convergence';
import { claimWhatsAppBusinessResource, findCompatibleWhatsAppChannel, normalizeProvedWhatsAppBusinessPhone } from './business-resource-ownership';

export type TipoDeCanal = 'OFICIAL' | 'NAO_OFICIAL';
const OPERATION_LEASE_MS = 45_000;
const ATTEMPT_TTL_MS = 10 * 60_000;

interface PairActor { userId: string; mantenedoraId: string; sessionHash: string; nome?: string; email?: string; ip?: string; }

/**
 * Conectar um número a uma BU (ADR-0008 §2): o canal é vínculo da BU, no máximo
 * um de cada tipo. A janela de 24h é atributo do canal, não do produto
 * (ADR-0009 §3) — quem decide é o tipo, não quem cadastrou.
 */
@Injectable()
export class ChannelsService {
  constructor(
    private readonly prisma: PrismaService,
    @Inject(META_CLIENT) private readonly meta: MetaClient,
    @Inject(EVOLUTION_CLIENT) private readonly evolution: EvolutionClient,
    private readonly credentials: ChannelCredentialResolver,
    @Optional() private readonly registro?: RegistroDeAtividade,
  ) {}

  /** POST-only Evolution pairing. Trust is reset in the database before any provider call. */
  async parearNaoOficial(buId: string, intent: 'INITIAL' | 'RENEW', expectedGeneration: number | undefined, revalidate: (() => Promise<void>) | undefined, actor: PairActor) {
    if (!this.evolution.configurado() || (!process.env.EVOLUTION_WEBHOOK_URL?.trim() || !process.env.EVOLUTION_WEBHOOK_SECRET?.trim())) {
      throw new ServiceUnavailableException({ code: 'EVOLUTION_NOT_CONFIGURED' });
    }
    if (intent === 'INITIAL') {
      const pending = await this.prisma.providerResourceIdentity.findFirst({ where: { buId, provider: 'NAO_OFICIAL', managedLifecycle: true, cleanupState: 'CLEANUP_PENDING', currentChannelId: null } });
      if (pending) {
        const token = randomUUID(); const now = new Date();
        const lease = await this.prisma.providerResourceIdentity.updateMany({ where: { id: pending.id, cleanupState: 'CLEANUP_PENDING', OR: [{ cleanupLeaseUntil: null }, { cleanupLeaseUntil: { lte: now } }] }, data: { cleanupLeaseToken: token, cleanupLeaseUntil: new Date(now.getTime() + OPERATION_LEASE_MS) } });
        if (!lease.count) throw new ConflictException({ code: 'CLEANUP_RECOVERY_BUSY' });
        try {
          await revalidate?.();
          const observed = await this.evolution.consultarInstancia(pending.externalResourceId);
          await revalidate?.();
          if (observed?.name === pending.externalResourceId) {
            await revalidate?.();
            await this.evolution.apagarInstancia(pending.externalResourceId);
            await revalidate?.();
          }
          const done = await this.prisma.providerResourceIdentity.updateMany({ where: { id: pending.id, cleanupState: 'CLEANUP_PENDING', cleanupLeaseToken: token }, data: { cleanupState: 'CLEANED', cleanupLeaseToken: null, cleanupLeaseUntil: null } });
          if (!done.count) throw new ConflictException({ code: 'CLEANUP_RECOVERY_STALE' });
        } catch {
          await this.prisma.providerResourceIdentity.updateMany({ where: { id: pending.id, cleanupLeaseToken: token }, data: { cleanupLeaseToken: null, cleanupLeaseUntil: null } });
          throw new ConflictException({ code: 'CLEANUP_AMBIGUOUS' });
        }
        throw new ConflictException({ code: 'CLEANUP_COMPLETED_RETRY_PAIR' });
      }
    }
    const leaseToken = randomUUID();
    const reservation = await this.prisma.$transaction(async (tx) => {
      let channel = await findCompatibleWhatsAppChannel(tx, buId, 'NAO_OFICIAL');
      if (intent === 'RENEW' && !channel) throw new ConflictException({ code: 'CHANNEL_AUSENTE' });
      // Lock the retained identity first, as incoming acceptance does. BU and
      // channel locks follow so retirement cannot deadlock an in-flight message.
      let lockedIdentityId: string | null = null;
      if (channel?.evolutionInstanceName) {
        const identityRows = await tx.$queryRaw<Array<{ id: string; managed_lifecycle: boolean }>>`SELECT id, managed_lifecycle FROM provider_resource_identities WHERE provider = 'NAO_OFICIAL' AND external_resource_id = ${channel.evolutionInstanceName} AND bu_id = ${buId} FOR UPDATE`;
        lockedIdentityId = identityRows[0]?.id ?? null;
      }
      await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${buId} FOR UPDATE`;
      if (!channel) channel = await tx.buChannel.create({ data: { buId, type: 'NAO_OFICIAL', status: 'CONECTANDO' } });
      else await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${channel.id} FOR UPDATE`;
      channel = await tx.buChannel.findUniqueOrThrow({ where: { id: channel.id } });
      if (expectedGeneration !== undefined && channel.generation !== expectedGeneration) throw new ConflictException({ code: 'GENERATION_CONFLICT' });
      const now = new Date();
      const lease = await tx.buChannel.updateMany({
        where: { id: channel.id, generation: channel.generation, OR: [{ operationLeaseUntil: null }, { operationLeaseUntil: { lte: now } }] },
        data: { operationLeaseToken: leaseToken, operationLeaseUntil: new Date(now.getTime() + OPERATION_LEASE_MS) },
      });
      if (!lease.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
      const currentAttempt = channel.currentAttemptId ? await tx.channelRegistrationAttempt.findUnique({ where: { id: channel.currentAttemptId }, select: { channelId: true, buId: true, type: true, stage: true, state: true, safeErrorCode: true, generation: true, pairingEpoch: true } }) : null;
      const cleanupIdentity = channel.pendingCleanupIdentityId
        ? await tx.providerResourceIdentity.findUnique({ where: { id: channel.pendingCleanupIdentityId } })
        : null;
      const exactCleanedCleanup = Boolean(channel.pendingCleanupInstanceName && channel.pendingCleanupIdentityId && cleanupIdentity
        && cleanupIdentity.buId === buId && cleanupIdentity.provider === 'NAO_OFICIAL'
        && cleanupIdentity.externalResourceId === channel.pendingCleanupInstanceName
        && cleanupIdentity.managedLifecycle && cleanupIdentity.currentChannelId === null
        && cleanupIdentity.cleanupState === 'CLEANED' && cleanupIdentity.cleanupLeaseToken === null
        && cleanupIdentity.cleanupLeaseUntil === null);
      const attemptMatchesLease = Boolean(currentAttempt && currentAttempt.channelId === channel.id && currentAttempt.buId === buId
        && currentAttempt.type === 'NAO_OFICIAL' && currentAttempt.generation === channel.generation
        && currentAttempt.pairingEpoch === channel.pairingEpoch);
      const resumablePending = Boolean(attemptMatchesLease && currentAttempt?.state === 'PENDING_NUMBER'
        && ['PAIRING', 'RESERVED_NEVER_CREATED'].includes(currentAttempt.stage));
      const resumableCreateAmbiguity = Boolean(attemptMatchesLease && currentAttempt?.state === 'ERROR'
        && currentAttempt.stage === 'CREATE_AMBIGUOUS' && currentAttempt.safeErrorCode === 'CREATE_AMBIGUOUS');
      const resumableCleanupAmbiguity = Boolean(attemptMatchesLease && currentAttempt?.state === 'ERROR'
        && currentAttempt.stage === 'CLEANUP_AMBIGUOUS' && currentAttempt.safeErrorCode === 'CLEANUP_AMBIGUOUS'
        && exactCleanedCleanup);
      const canResume = Boolean(channel.evolutionInstanceName && channel.pairingEpoch > 0
        && !channel.ownNumberVerified && (resumablePending || resumableCreateAmbiguity || resumableCleanupAmbiguity));
      if (intent === 'INITIAL' && channel.evolutionInstanceName && !canResume) throw new ConflictException({ code: 'CHANNEL_SLOT_OCCUPIED' });
      if (intent === 'RENEW' && channel.pendingCleanupInstanceName) throw new ConflictException({ code: 'CLEANUP_RECOVERY_REQUIRED' });
      if (canResume) {
        const identity = lockedIdentityId ? await tx.providerResourceIdentity.findUnique({ where: { id: lockedIdentityId } }) : null;
        if (!identity) throw new ConflictException({ code: 'IDENTITY_NOT_MAPPED' });
    if (!identity.managedLifecycle) throw new ConflictException({ code: 'LEGACY_RESOURCE_UNMANAGED' });
        if (channel.currentAttemptId) {
          const stage = currentAttempt?.stage === 'RESERVED_NEVER_CREATED' ? 'RESERVED_NEVER_CREATED' : channel.pendingCleanupInstanceName ? 'CLEANUP_AMBIGUOUS' : 'PAIRING';
          await tx.channelRegistrationAttempt.updateMany({ where: { id: channel.currentAttemptId, generation: channel.generation, pairingEpoch: channel.pairingEpoch }, data: { stage, state: channel.pendingCleanupInstanceName ? 'ERROR' : 'PENDING_NUMBER', version: { increment: 1 } } });
        }
        const leased = await tx.buChannel.findUniqueOrThrow({ where: { id: channel.id } });
        if (channel.currentAttemptId) await this.audit(tx, actor, 'canal.pareado', buId, channel.currentAttemptId, 'PAIRING');
        return { channel: leased, identityId: identity.id, name: channel.evolutionInstanceName!, generation: channel.generation, epoch: channel.pairingEpoch, resume: true, cleanupName: channel.pendingCleanupInstanceName, cleanupIdentityId: channel.pendingCleanupIdentityId, leaseToken, attemptId: channel.currentAttemptId };
      }
      const oldIdentity = lockedIdentityId ? await tx.providerResourceIdentity.findUnique({ where: { id: lockedIdentityId } }) : null;
      const oldName = oldIdentity?.managedLifecycle ? oldIdentity.externalResourceId : null;
      if (oldName && oldName !== channel.evolutionInstanceName) throw new ConflictException({ code: 'IDENTITY_MAPPING_MISMATCH' });
      const epoch = channel.pairingEpoch + 1;
      const generation = intent === 'RENEW' ? channel.generation + 1 : channel.generation;
      const name = `lh-${channel.id.replace(/-/g, '')}-${epoch}`;
      await tx.providerResourceIdentity.updateMany({ where: { currentChannelId: channel.id }, data: { currentChannelId: null, retiredAt: new Date(), cleanupState: { set: oldIdentity?.managedLifecycle ? 'CLEANUP_PENDING' : 'UNMANAGED' } } });
      const attemptId = randomUUID();
      const attempt = await tx.channelRegistrationAttempt.create({ data: {
        id: attemptId, mantenedoraId: actor.mantenedoraId, buId, channelId: channel.id,
        type: 'NAO_OFICIAL', operation: intent === 'RENEW' ? 'REAUTORIZAR' : 'NOVO', userId: actor.userId,
        sessionHash: actor.sessionHash, idempotencyKey: `evolution:${channel.id}:${epoch}`,
        requestHash: createHash('sha256').update(`${intent}:${channel.id}:${epoch}`).digest('hex'),
        state: 'PENDING_NUMBER', stage: 'PAIRING', generation, pairingEpoch: epoch,
        expiresAt: new Date(Date.now() + ATTEMPT_TTL_MS),
      } });
      const updated = await tx.buChannel.update({
        where: { id: channel.id },
        data: { generation, pairingEpoch: epoch, evolutionInstanceName: name, currentAttemptId: attempt.id, ownNumberVerified: false, verifiedEpoch: null, providerConnectionState: 'PENDING', receiptVerifiedAt: null, connectedAt: null, status: 'CONECTANDO', pendingCleanupInstanceName: oldName, pendingCleanupIdentityId: oldName ? oldIdentity!.id : null },
      });
      const identity = await tx.providerResourceIdentity.create({ data: {
        provider: 'NAO_OFICIAL', externalResourceId: name, buId,
        currentChannelId: channel.businessIdentityId ? null : channel.id,
        unverifiedStaging: Boolean(channel.businessIdentityId), managedLifecycle: true, cleanupState: 'ACTIVE',
      } });
      await this.audit(tx, actor, 'canal.pareado', buId, attempt.id, 'PAIRING');
      return { channel: updated, identityId: identity.id, name, generation, epoch, resume: false, cleanupName: oldName, cleanupIdentityId: oldName ? oldIdentity!.id : null, leaseToken, attemptId: attempt.id };
    });
    const operationFence = async () => {
      await revalidate?.();
      const current = await this.prisma.buChannel.findFirst({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId, operationLeaseToken: leaseToken, operationLeaseUntil: { gt: new Date() } } });
      if (!current) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
    };
    try {
      return await this.completePairing(buId, reservation, operationFence);
    } finally {
      await this.prisma.buChannel.updateMany({
        where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, operationLeaseToken: leaseToken },
        data: { operationLeaseToken: null, operationLeaseUntil: null },
      });
    }
  }

  private async completePairing(
    buId: string,
    reservation: { channel: { id: string }; identityId: string; name: string; generation: number; epoch: number; resume: boolean; cleanupName: string | null; cleanupIdentityId: string | null; leaseToken: string; attemptId: string | null },
    revalidate?: () => Promise<void>,
  ) {
    if (reservation.cleanupName) {
      const cleanupName = reservation.cleanupName;
      const cleanupIdentityId = reservation.cleanupIdentityId;
      if (!cleanupIdentityId) throw new ConflictException({ code: 'CLEANUP_RECOVERY_STALE' });
      const recordAmbiguousCleanup = async () => {
        await this.prisma.$transaction(async (tx) => {
          const identityLock = await tx.$queryRaw<Array<{ id: string }>>`
            SELECT id FROM provider_resource_identities
            WHERE id = ${cleanupIdentityId} AND bu_id = ${buId}
              AND provider = 'NAO_OFICIAL'::"ChannelType" AND external_resource_id = ${cleanupName}
              AND managed_lifecycle = TRUE AND current_channel_id IS NULL
            FOR UPDATE`;
          if (!identityLock.length) throw new ConflictException({ code: 'CLEANUP_RECOVERY_STALE' });
          await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${buId} FOR UPDATE`;
          await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${reservation.channel.id} FOR UPDATE`;
          const channel = await tx.buChannel.findFirst({ where: {
            id: reservation.channel.id, buId, type: 'NAO_OFICIAL', generation: reservation.generation,
            pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId,
            operationLeaseToken: reservation.leaseToken, operationLeaseUntil: { gt: new Date() },
            pendingCleanupInstanceName: cleanupName, pendingCleanupIdentityId: cleanupIdentityId,
          }, select: { id: true } });
          if (!channel) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
          const cleanup = await tx.providerResourceIdentity.updateMany({ where: {
            id: cleanupIdentityId, buId, provider: 'NAO_OFICIAL', externalResourceId: cleanupName,
            managedLifecycle: true, currentChannelId: null, cleanupState: { in: ['CLEANUP_PENDING', 'CLEANED'] },
            cleanupLeaseToken: null, cleanupLeaseUntil: null,
          }, data: { cleanupState: 'CLEANUP_PENDING' } });
          if (!cleanup.count) throw new ConflictException({ code: 'CLEANUP_RECOVERY_STALE' });
          if (reservation.attemptId) {
            const attempt = await tx.channelRegistrationAttempt.updateMany({ where: {
              id: reservation.attemptId, channelId: reservation.channel.id, buId, type: 'NAO_OFICIAL',
              generation: reservation.generation, pairingEpoch: reservation.epoch,
              OR: [
                { stage: 'PAIRING', state: 'PENDING_NUMBER' },
                { stage: 'CLEANUP_AMBIGUOUS', state: 'ERROR', safeErrorCode: 'CLEANUP_AMBIGUOUS' },
              ],
            }, data: { state: 'ERROR', stage: 'CLEANUP_AMBIGUOUS', safeErrorCode: 'CLEANUP_AMBIGUOUS', version: { increment: 1 } } });
            if (!attempt.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
          }
        });
      };

      await revalidate?.();
      let prior: Awaited<ReturnType<EvolutionClient['consultarInstancia']>>;
      try {
        prior = await this.evolution.consultarInstancia(reservation.cleanupName);
      } catch {
        await revalidate?.();
        await recordAmbiguousCleanup();
        return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CLEANUP_AMBIGUOUS', qrcode: null };
      }
      await revalidate?.();
      if (prior?.name === reservation.cleanupName) {
        await revalidate?.();
        try {
          await this.evolution.apagarInstancia(reservation.cleanupName);
        } catch {
          await revalidate?.();
          await recordAmbiguousCleanup();
          return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CLEANUP_AMBIGUOUS', qrcode: null };
        }
        await revalidate?.();
      }
      await this.prisma.$transaction(async (tx) => {
        if (reservation.cleanupIdentityId) {
          const cleanup = await tx.providerResourceIdentity.updateMany({
            where: { id: reservation.cleanupIdentityId, buId, provider: 'NAO_OFICIAL', externalResourceId: reservation.cleanupName!, managedLifecycle: true, currentChannelId: null, cleanupState: { in: ['CLEANUP_PENDING', 'CLEANED'] } },
            data: { cleanupState: 'CLEANED', cleanupLeaseToken: null, cleanupLeaseUntil: null },
          });
          if (!cleanup.count) throw new ConflictException({ code: 'CLEANUP_RECOVERY_STALE' });
        }
        const cleared = await tx.buChannel.updateMany({
        where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId, operationLeaseToken: reservation.leaseToken, operationLeaseUntil: { gt: new Date() }, pendingCleanupInstanceName: reservation.cleanupName, pendingCleanupIdentityId: reservation.cleanupIdentityId },
          data: { pendingCleanupInstanceName: null, pendingCleanupIdentityId: null },
        });
        if (!cleared.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
        if (reservation.attemptId) {
          const moved = await tx.channelRegistrationAttempt.updateMany({
            where: {
              id: reservation.attemptId, channelId: reservation.channel.id, buId, type: 'NAO_OFICIAL',
              generation: reservation.generation, pairingEpoch: reservation.epoch,
              OR: [
                { stage: 'PAIRING', state: 'PENDING_NUMBER' },
                { stage: 'CLEANUP_AMBIGUOUS', state: 'ERROR', safeErrorCode: 'CLEANUP_AMBIGUOUS' },
              ],
            },
            data: { state: 'PENDING_NUMBER', stage: 'RESERVED_NEVER_CREATED', safeErrorCode: null, version: { increment: 1 } },
          });
          if (!moved.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
        }
      });
      return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CLEANUP_COMPLETED_RETRY_PAIR', qrcode: null };
    }
    let created: { qrcode: string | null };
    const attemptStage = reservation.attemptId ? (await this.prisma.channelRegistrationAttempt.findUnique({ where: { id: reservation.attemptId }, select: { stage: true } }))?.stage : undefined;
    const reservedOnly = reservation.resume && attemptStage === 'RESERVED_NEVER_CREATED';
    if (reservedOnly && reservation.attemptId) {
      const claimed = await this.prisma.channelRegistrationAttempt.updateMany({
        where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, stage: 'RESERVED_NEVER_CREATED' },
        data: { stage: 'PAIRING', state: 'PENDING_NUMBER', version: { increment: 1 } },
      });
      if (!claimed.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
    }
    if (reservation.resume && !reservedOnly) await revalidate?.();
    let observed = reservation.resume && !reservedOnly ? await this.evolution.consultarInstancia(reservation.name).catch(() => null) : null;
    if (reservation.resume && !reservedOnly) await revalidate?.();
    if (reservation.resume && !reservedOnly && !observed) {
      if (reservation.attemptId) await this.prisma.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'CREATE_AMBIGUOUS', safeErrorCode: 'CREATE_AMBIGUOUS', version: { increment: 1 } } });
      return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CREATE_AMBIGUOUS', qrcode: null };
    }
    if (!reservation.resume || reservedOnly) {
      try {
        await revalidate?.();
        created = await this.evolution.criarInstancia(reservation.name);
      } catch {
        await revalidate?.();
        observed = await this.evolution.consultarInstancia(reservation.name).catch(() => null);
        await revalidate?.();
        if (!observed) {
          if (reservation.attemptId) await this.prisma.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'CREATE_AMBIGUOUS', safeErrorCode: 'CREATE_AMBIGUOUS', version: { increment: 1 } } });
          return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: 'CREATE_AMBIGUOUS', qrcode: null };
        }
        created = { qrcode: null };
      }
      await revalidate?.();
    } else created = { qrcode: null };
    let qr = created.qrcode;
    if (!qr) { await revalidate?.(); qr = await this.evolution.qrDaInstancia(reservation.name).catch(() => null); await revalidate?.(); }
    if (!observed) { await revalidate?.(); observed = await this.evolution.consultarInstancia(reservation.name).catch(() => null); await revalidate?.(); }
    if (observed?.name !== reservation.name) observed = null;
    if (observed?.connectionStatus?.toLowerCase() === 'open' && observed.ownerJid) {
      const ownerPhone = parseEvolutionOwnerPhone(observed.ownerJid);
      const provedBusinessPhone = ownerPhone ? normalizeProvedWhatsAppBusinessPhone(ownerPhone) : null;
      let ownerMismatch = false;
      await revalidate?.();
      if (!provedBusinessPhone) {
        await this.prisma.$transaction(async (tx) => {
          const locked = await tx.$queryRaw<Array<{ id: string }>>`
            SELECT id FROM provider_resource_identities WHERE id = ${reservation.identityId} AND managed_lifecycle = TRUE
              AND (current_channel_id = ${reservation.channel.id}
                OR (current_channel_id IS NULL AND unverified_staging = TRUE AND provider = 'NAO_OFICIAL'::"ChannelType" AND external_resource_id = ${reservation.name}))
            FOR UPDATE`;
          if (!locked.length) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
          await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${buId} FOR UPDATE`;
          await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${reservation.channel.id} FOR UPDATE`;
          const channel = await tx.buChannel.findFirst({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId, operationLeaseToken: reservation.leaseToken, operationLeaseUntil: { gt: new Date() } } });
          if (!channel) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
          const changed = await tx.buChannel.updateMany({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId, operationLeaseToken: reservation.leaseToken, operationLeaseUntil: { gt: new Date() } }, data: { providerConnectionState: 'IDENTITY_QUARANTINED', ownNumberVerified: false, verifiedEpoch: null } });
          if (!changed.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
          if (reservation.attemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'IDENTITY_QUARANTINED', safeErrorCode: 'IDENTITY_QUARANTINED', version: { increment: 1 } } });
        });
        throw new ConflictException({ code: 'IDENTITY_QUARANTINED' });
      }
      await this.prisma.$transaction(async (tx) => {
        const locked = await tx.$queryRaw<Array<{ id: string }>>`
          SELECT id FROM provider_resource_identities WHERE id = ${reservation.identityId} AND managed_lifecycle = TRUE
            AND (current_channel_id = ${reservation.channel.id}
              OR (current_channel_id IS NULL AND unverified_staging = TRUE AND provider = 'NAO_OFICIAL'::"ChannelType" AND external_resource_id = ${reservation.name}))
          FOR UPDATE`;
        if (!locked.length) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
        await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${buId} FOR UPDATE`;
        await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${reservation.channel.id} FOR UPDATE`;
        const current = await tx.buChannel.findFirst({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId, operationLeaseToken: reservation.leaseToken, operationLeaseUntil: { gt: new Date() } } });
        if (!current) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
        const existingOwner = await tx.businessChannelIdentity.findFirst({ where: { buId, platform: 'WHATSAPP' } });
        if (existingOwner && existingOwner.externalResourceId !== provedBusinessPhone) {
          const quarantined = await tx.buChannel.updateMany({ where: { id: current.id, generation: reservation.generation, pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId, operationLeaseToken: reservation.leaseToken, operationLeaseUntil: { gt: new Date() } }, data: { ownNumberVerified: false, verifiedEpoch: null, providerConnectionState: 'IDENTITY_QUARANTINED' } });
          if (!quarantined.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
          if (reservation.attemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch }, data: { state: 'ERROR', stage: 'IDENTITY_QUARANTINED', safeErrorCode: 'IDENTITY_QUARANTINED', version: { increment: 1 } } });
          ownerMismatch = true;
          return;
        }
        await claimWhatsAppBusinessResource(tx, {
          buId, channelId: reservation.channel.id, providerResourceIdentityId: reservation.identityId,
          adapter: 'NAO_OFICIAL', provedPhone: provedBusinessPhone,
        });
        const updated = await tx.buChannel.updateMany({ where: { id: reservation.channel.id, generation: reservation.generation, pairingEpoch: reservation.epoch, currentAttemptId: reservation.attemptId, operationLeaseToken: reservation.leaseToken, operationLeaseUntil: { gt: new Date() } }, data: { ownNumberVerified: true, verifiedEpoch: reservation.epoch, providerConnectionState: 'CONNECTED', ...(current.receiptVerifiedAt ? { status: 'CONECTADO', connectedAt: new Date() } : {}) } });
        if (!updated.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
        if (reservation.attemptId) {
          const attempt = await tx.channelRegistrationAttempt.updateMany({ where: { id: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: { in: ['PENDING_NUMBER', 'PENDING_RECEIPT'] } }, data: { state: current.receiptVerifiedAt ? 'CONNECTED' : 'PENDING_RECEIPT', stage: current.receiptVerifiedAt ? 'RECEIPT_VERIFIED' : 'MAPPED_PENDING_RECEIPT', version: { increment: 1 } } });
          if (!attempt.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
        }
      });
      if (ownerMismatch) throw new ConflictException({ code: 'IDENTITY_QUARANTINED' });
    }
    return { channelId: reservation.channel.id, attemptId: reservation.attemptId, generation: reservation.generation, pairingEpoch: reservation.epoch, state: observed?.connectionStatus?.toLowerCase() === 'open' ? 'PENDING_RECEIPT' : 'PENDING_IDENTITY', qrcode: qr };
  }

  async verificar(buId: string, tipo: TipoDeCanal, revalidate?: () => Promise<void>, actor?: PairActor) {
    const leaseToken = randomUUID();
    const now = new Date();
    const reservation = await this.prisma.$transaction(async (tx) => {
      const snapshot = await findCompatibleWhatsAppChannel(tx, buId, tipo);
      if (!snapshot) throw new ConflictException({ code: 'CHANNEL_AUSENTE' });
      const ownerRows = await tx.$queryRaw<Array<{ id: string }>>`
        SELECT id FROM provider_resource_identities
        WHERE provider = CAST(${tipo} AS "ChannelType") AND bu_id = ${buId}
          AND (current_channel_id = ${snapshot.id}
            OR (CAST(${tipo} AS "ChannelType") = 'NAO_OFICIAL'::"ChannelType" AND current_channel_id IS NULL
              AND unverified_staging = TRUE AND external_resource_id = ${snapshot.evolutionInstanceName ?? ''}))
        FOR UPDATE`;
      if (!ownerRows.length) throw new ConflictException({ code: 'IDENTITY_NOT_MAPPED' });
      await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${buId} FOR UPDATE`;
      await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${snapshot.id} FOR UPDATE`;
      const channel = await tx.buChannel.findUniqueOrThrow({ where: { id: snapshot.id } });
      const identity = await tx.providerResourceIdentity.findUniqueOrThrow({ where: { id: ownerRows[0].id } });
      if (!identity.managedLifecycle) throw new ConflictException({ code: 'LEGACY_RESOURCE_UNMANAGED' });
      const lease = await tx.buChannel.updateMany({
        where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, currentAttemptId: channel.currentAttemptId, OR: [{ operationLeaseUntil: null }, { operationLeaseUntil: { lte: now } }] },
        data: { operationLeaseToken: leaseToken, operationLeaseUntil: new Date(now.getTime() + OPERATION_LEASE_MS) },
      });
      if (!lease.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
      return { channel, identity };
    });
    const { channel, identity } = reservation;
    try {
    let verifiedPhone: string | null = null;
    let connectionOpen = false;
    if (tipo === 'OFICIAL') {
      if (!channel.wabaId || !channel.phoneNumberId) throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
      const credential = await this.credentials.resolve(channel.id, 'verify');
      if (!credential.accessToken) throw new ConflictException({ code: 'PENDING_CREDENTIAL' });
      await revalidate?.();
      await this.assertOperationLease(channel, leaseToken);
      let number: MetaNumber | null;
      try {
        number = await this.meta.verificarNumeroVinculado(channel.wabaId, channel.phoneNumberId, credential.accessToken);
      } catch (error) {
        if (error instanceof MetaIndisponivelError) {
          throw new ServiceUnavailableException({ code: 'META_INDISPONIVEL', error: 'A verificação do número está temporariamente indisponível.' });
        }
        throw error;
      }
      await revalidate?.();
      await this.assertOperationLease(channel, leaseToken);
      if (!number) throw new ConflictException({ code: 'PROVIDER_RESOURCE_NOT_FOUND' });
      verifiedPhone = number.telefone;
      if (!verifiedPhone || !/^\+?[1-9]\d{7,14}$/.test(verifiedPhone)) throw new ConflictException({ code: 'PENDING_IDENTITY' });
    } else {
      if (!channel.evolutionInstanceName) throw new ConflictException({ code: 'CHANNEL_IDENTITY_NOT_VERIFIED' });
      await revalidate?.();
      await this.assertOperationLease(channel, leaseToken);
      const observed = await this.evolution.consultarInstancia(channel.evolutionInstanceName);
      await revalidate?.();
      await this.assertOperationLease(channel, leaseToken);
      if (!observed || observed.name !== identity.externalResourceId) throw new ConflictException({ code: 'PROVIDER_RESOURCE_NOT_FOUND' });
      const ownerPhone = observed.ownerJid ? parseEvolutionOwnerPhone(observed.ownerJid) : null;
      connectionOpen = observed.connectionStatus?.toLowerCase() === 'open';
      if (!ownerPhone || !connectionOpen) throw new ConflictException({ code: 'PENDING_IDENTITY' });
      verifiedPhone = ownerPhone;
    }
    await revalidate?.();
    await this.assertOperationLease(channel, leaseToken);
    let ownerMismatch = false;
    await this.prisma.$transaction(async (tx) => {
      const locked = await tx.$queryRaw<Array<{ id: string }>>`
        SELECT id FROM provider_resource_identities WHERE id = ${identity.id} AND managed_lifecycle = TRUE
          AND (current_channel_id = ${channel.id}
            OR (provider = 'NAO_OFICIAL'::"ChannelType" AND current_channel_id IS NULL AND unverified_staging = TRUE
              AND external_resource_id = ${channel.evolutionInstanceName ?? ''}))
        FOR UPDATE`;
      if (!locked.length) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
      await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${buId} FOR UPDATE`;
      await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${channel.id} FOR UPDATE`;
      const current = await tx.buChannel.findFirst({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, currentAttemptId: channel.currentAttemptId, operationLeaseToken: leaseToken, operationLeaseUntil: { gt: new Date() } } });
      if (!current) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
      if (!verifiedPhone) throw new ConflictException({ code: 'PENDING_IDENTITY' });
      const provedPhone = normalizeProvedWhatsAppBusinessPhone(verifiedPhone);
      const existingOwner = tipo === 'NAO_OFICIAL' ? await tx.businessChannelIdentity.findFirst({ where: { buId, platform: 'WHATSAPP' } }) : null;
      if (existingOwner && existingOwner.externalResourceId !== provedPhone) {
        const quarantined = await tx.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken, operationLeaseUntil: { gt: new Date() } }, data: { ownNumberVerified: false, verifiedEpoch: null, providerConnectionState: 'IDENTITY_QUARANTINED' } });
        if (!quarantined.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
        if (channel.currentAttemptId) await tx.channelRegistrationAttempt.updateMany({ where: { id: channel.currentAttemptId, generation: channel.generation, pairingEpoch: channel.pairingEpoch }, data: { state: 'ERROR', stage: 'IDENTITY_QUARANTINED', safeErrorCode: 'IDENTITY_QUARANTINED', version: { increment: 1 } } });
        ownerMismatch = true;
        return;
      }
      await claimWhatsAppBusinessResource(tx, {
        buId, channelId: channel.id, providerResourceIdentityId: identity.id, adapter: tipo, provedPhone,
      });
      const updated = await tx.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken, operationLeaseUntil: { gt: new Date() } }, data: { ownNumberVerified: true, verifiedEpoch: channel.pairingEpoch, providerConnectionState: tipo === 'NAO_OFICIAL' ? 'CONNECTED' : current.providerConnectionState === 'SUBSCRIBED' ? 'SUBSCRIBED' : 'VERIFIED' } });
      if (!updated.count) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
      if (channel.receiptVerifiedAt && (tipo === 'NAO_OFICIAL' || channel.providerConnectionState === 'SUBSCRIBED')) {
        const connected = await tx.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken, operationLeaseUntil: { gt: new Date() } }, data: { status: 'CONECTADO', connectedAt: new Date() } });
        if (!connected.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
        if (channel.currentAttemptId) {
          const attemptEpoch = tipo === 'OFICIAL' ? null : channel.pairingEpoch;
          const recoveredQuarantine = await tx.channelRegistrationAttempt.updateMany({
            where: {
              id: channel.currentAttemptId,
              channelId: channel.id,
              buId,
              type: tipo,
              generation: current.generation,
              pairingEpoch: attemptEpoch,
              state: 'ERROR',
              stage: 'IDENTITY_QUARANTINED',
              safeErrorCode: 'IDENTITY_QUARANTINED',
            },
            data: { state: 'CONNECTED', stage: 'RECEIPT_VERIFIED', safeErrorCode: null, version: { increment: 1 } },
          });
          const attemptConverged = recoveredQuarantine.count > 0
            || await convergeReceiptVerifiedAttempt(tx, channel.currentAttemptId, current.generation, attemptEpoch);
          if (!attemptConverged) throw new ConflictException({ code: 'ATTEMPT_STALE' });
        }
      } else if (tipo === 'NAO_OFICIAL' && channel.currentAttemptId) {
        const attemptFence = {
          id: channel.currentAttemptId,
          channelId: channel.id,
          buId,
          type: tipo,
          generation: current.generation,
          pairingEpoch: current.pairingEpoch,
        };
        const pendingAttempt = await tx.channelRegistrationAttempt.updateMany({
          where: { ...attemptFence, state: { in: ['PENDING_NUMBER', 'PENDING_RECEIPT'] } },
          data: { state: 'PENDING_RECEIPT', stage: 'MAPPED_PENDING_RECEIPT', safeErrorCode: null, version: { increment: 1 } },
        });
        if (!pendingAttempt.count) {
          const recoveredUncertainAttempt = await tx.channelRegistrationAttempt.updateMany({
            where: {
              ...attemptFence,
              state: 'ERROR',
              OR: [
                { stage: 'IDENTITY_QUARANTINED', safeErrorCode: 'IDENTITY_QUARANTINED' },
                { stage: 'CREATE_AMBIGUOUS', safeErrorCode: 'CREATE_AMBIGUOUS' },
              ],
            },
            data: { state: 'PENDING_RECEIPT', stage: 'MAPPED_PENDING_RECEIPT', safeErrorCode: null, version: { increment: 1 } },
          });
          if (!recoveredUncertainAttempt.count) throw new ConflictException({ code: 'ATTEMPT_STALE' });
        }
      }
      if (actor) await this.audit(tx, actor, 'canal.identidade.verificada', buId, channel.currentAttemptId ?? channel.id, 'IDENTITY_VERIFIED');
    });
    if (ownerMismatch) throw new ConflictException({ code: 'IDENTITY_QUARANTINED' });
    return { status: connectionOpen ? 'PENDING_RECEIPT' : 'IDENTITY_VERIFIED', ownNumberVerified: true, receiptVerified: Boolean(channel.receiptVerifiedAt) };
    } finally {
      await this.prisma.buChannel.updateMany({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: leaseToken }, data: { operationLeaseToken: null, operationLeaseUntil: null } });
    }
  }

  async desconectar(buId: string, tipo: TipoDeCanal, actor?: PairActor, revalidate?: () => Promise<void>) {
    const snapshot = await findCompatibleWhatsAppChannel(this.prisma, buId, tipo);
    if (!snapshot) return false;
    const token = randomUUID();
    const detached = await this.prisma.$transaction(async (tx) => {
      const snapshotResource = tipo === 'OFICIAL' ? snapshot.phoneNumberId : snapshot.evolutionInstanceName;
      let identity = snapshotResource ? await tx.providerResourceIdentity.findUnique({ where: { provider_externalResourceId: { provider: tipo, externalResourceId: snapshotResource } } }) : null;
      if (identity) {
        const locked = await tx.$queryRaw<Array<{ id: string }>>`SELECT id FROM provider_resource_identities WHERE id = ${identity.id} AND bu_id = ${buId} AND provider = CAST(${tipo} AS "ChannelType") AND (current_channel_id = ${snapshot.id} OR (current_channel_id IS NULL AND unverified_staging = TRUE AND external_resource_id = ${snapshotResource ?? ''})) FOR UPDATE`;
        if (!locked.length) identity = null;
      }
      await tx.$queryRaw`SELECT id FROM business_units WHERE id = ${buId} FOR UPDATE`;
      await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${snapshot.id} FOR UPDATE`;
      const current = await tx.buChannel.findUnique({ where: { id: snapshot.id } });
      if (!current) return null;
      const currentResource = tipo === 'OFICIAL' ? current.phoneNumberId : current.evolutionInstanceName;
      if (current.buId !== buId || current.type !== tipo
        || current.generation !== snapshot.generation
        || current.pairingEpoch !== snapshot.pairingEpoch
        || current.currentAttemptId !== snapshot.currentAttemptId
        || currentResource !== snapshotResource) {
        throw new ConflictException({ code: 'CHANNEL_SNAPSHOT_STALE' });
      }
      const now = new Date();
      if (current.operationLeaseUntil && current.operationLeaseUntil > now) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
      const claim = await tx.buChannel.updateMany({ where: { id: current.id, generation: current.generation, pairingEpoch: current.pairingEpoch, currentAttemptId: current.currentAttemptId, OR: [{ operationLeaseUntil: null }, { operationLeaseUntil: { lte: now } }] }, data: { operationLeaseToken: token, operationLeaseUntil: new Date(now.getTime() + OPERATION_LEASE_MS) } });
      if (!claim.count) throw new ConflictException({ code: 'CHANNEL_OPERATION_BUSY' });
      if (identity) {
        const update = await tx.providerResourceIdentity.updateMany({ where: { id: identity.id, buId, provider: tipo, OR: [{ currentChannelId: current.id }, { currentChannelId: null, unverifiedStaging: true, externalResourceId: snapshotResource ?? '' }] }, data: { currentChannelId: null, retiredAt: now, ...(identity.managedLifecycle ? { cleanupState: 'CLEANUP_PENDING', cleanupLeaseToken: token, cleanupLeaseUntil: new Date(now.getTime() + OPERATION_LEASE_MS) } : {}) } });
        if (!update.count) throw new ConflictException({ code: 'IDENTITY_NOT_CURRENT' });
      }
      await tx.channelRegistrationAttempt.updateMany({ where: { channelId: current.id, state: { notIn: ['CONNECTED', 'CANCELLED'] } }, data: { state: 'CANCELLED', stage: 'DETACHED', candidateKeyId: null, candidateNonce: null, candidateCiphertext: null, candidateTag: null, nonceHash: null, version: { increment: 1 } } });
      await tx.channelRegistrationAttempt.updateMany({ where: { channelId: current.id }, data: { channelId: null, candidateKeyId: null, candidateNonce: null, candidateCiphertext: null, candidateTag: null, nonceHash: null } });
      await tx.channelCredential.deleteMany({ where: { channelId: current.id } });
      if (actor) await this.audit(tx, actor, 'canal.removido', buId, current.id, 'DETACHED');
      await tx.buChannel.delete({ where: { id: current.id, operationLeaseToken: token } });
      return identity?.managedLifecycle ? identity.externalResourceId : null;
    });
    if (tipo === 'NAO_OFICIAL' && detached && this.evolution.configurado()) {
      const identity = await this.prisma.providerResourceIdentity.findUnique({ where: { provider_externalResourceId: { provider: tipo, externalResourceId: detached } } });
      try {
        await revalidate?.();
        const lease = await this.prisma.providerResourceIdentity.findFirst({ where: { id: identity?.id, cleanupState: 'CLEANUP_PENDING', cleanupLeaseToken: token, cleanupLeaseUntil: { gt: new Date() } } });
        if (!lease) throw new ConflictException({ code: 'CLEANUP_RECOVERY_STALE' });
        const observed = await this.evolution.consultarInstancia(detached);
        await revalidate?.();
        const currentLease = await this.prisma.providerResourceIdentity.findFirst({ where: { id: identity?.id, cleanupState: 'CLEANUP_PENDING', cleanupLeaseToken: token, cleanupLeaseUntil: { gt: new Date() } } });
        if (!currentLease) throw new ConflictException({ code: 'CLEANUP_RECOVERY_STALE' });
        if (observed?.name === detached) { await revalidate?.(); await this.evolution.apagarInstancia(detached); await revalidate?.(); }
        if (identity) await this.prisma.providerResourceIdentity.updateMany({ where: { id: identity.id, cleanupState: 'CLEANUP_PENDING', cleanupLeaseToken: token }, data: { cleanupState: 'CLEANED', cleanupLeaseToken: null, cleanupLeaseUntil: null } });
      } catch { /* durable CLEANUP_PENDING and lease block a new managed instance */ }
    }
    return true;
  }

  private async assertOperationLease(channel: { id: string; generation: number; pairingEpoch: number }, token: string) {
    const current = await this.prisma.buChannel.findFirst({ where: { id: channel.id, generation: channel.generation, pairingEpoch: channel.pairingEpoch, operationLeaseToken: token, operationLeaseUntil: { gt: new Date() } }, select: { id: true } });
    if (!current) throw new ConflictException({ code: 'CHANNEL_OPERATION_STALE' });
  }

  private async audit(tx: import('@prisma/client').Prisma.TransactionClient, actor: PairActor, key: import('../historico/catalogo').ChaveDoCatalogo, buId: string, entityId: string, stage: string) {
    if (!this.registro || !actor.nome) return;
    const bu = await tx.businessUnit.findUnique({ where: { id: buId }, select: { name: true, mantenedoraId: true } });
    if (!bu) return;
    await this.registro.registrar(tx, actor.mantenedoraId, key, { id: actor.userId, nome: actor.nome, email: actor.email, ip: actor.ip }, {
      buId, entidadeId: entityId, detalhe: { attemptId: entityId, stage }, frase: { canal: 'não oficial', nome: bu.name },
    });
  }

}
function parseEvolutionOwnerPhone(ownerJid: string): string | null {
  if (!ownerJid.endsWith('@s.whatsapp.net')) return null;
  const local = ownerJid.split('@')[0].split(':')[0];
  return /^\d{8,15}$/.test(local) ? local : null;
}

```

## Complete current source api-app/src/domain/channels/instagram-authorization.service.ts
```
import { createHash, createHmac, randomBytes, randomUUID, timingSafeEqual } from 'node:crypto';
import { BadRequestException, ConflictException, ForbiddenException, HttpException, HttpStatus, Injectable, NotFoundException, ServiceUnavailableException, UnauthorizedException } from '@nestjs/common';
import { AccessService } from '../access/access.service';
import { Prisma } from '@prisma/client';
import { exigirPapelNaBu } from '../access/require-role';
import { PrismaService } from '../../infra/prisma/prisma.service';
import { InstagramHttpClient, instagramConfig } from '../../integrations/instagram/instagram-http.client';
import { loadChannelCredentialKey, openChannelCredential, sealChannelCredential } from './channel-credential-crypto';
import { SessionService } from '../../infra/session/session.service';
import { RegistroDeAtividade } from '../historico/registro.service';

const TTL = 10 * 60_000;
const BUDGET_WINDOW_MS = 60 * 60_000;
const KEY = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const RECEIPT_CONFIRMED = Symbol('INSTAGRAM_RECEIPT_CONFIRMED');
type SubscriptionClockFacts = { deadlineAt: Date; attemptExpiresAt: Date; credentialExpiresAt: Date | null; bindingLeaseUntil: Date; attemptLeaseUntil: Date };

export interface InstagramActor { id: string; mantenedoraId: string; sessionToken: string; nome: string; email: string; ip?: string; }

@Injectable()
export class InstagramAuthorizationService {
  constructor(private readonly prisma: PrismaService, private readonly access: AccessService, private readonly http: InstagramHttpClient, private readonly sessions: SessionService, private readonly activity: RegistroDeAtividade) {}

  capabilities() {
    const configured = Boolean(instagramConfig());
    const cryptoReady = (() => { try { loadChannelCredentialKey(process.env); return true; } catch { return false; } })();
    return { instagram: { available: configured && cryptoReady, reason: !configured ? 'NOT_CONFIGURED' : cryptoReady ? 'AVAILABLE' : 'CREDENTIAL_ENCRYPTION_UNAVAILABLE', apiVersion: 'v26.0' } };
  }

  async create(actor: InstagramActor, buId: string, idempotencyKey: string, body: { operation: 'CONNECT' | 'REAUTHORIZE'; channelId?: string; expectedGeneration?: number }) {
    const config = instagramConfig();
    if (!config || !this.capabilities().instagram.available) throw new ServiceUnavailableException({ code: 'INSTAGRAM_UNAVAILABLE' });
    if (!KEY.test(idempotencyKey)) throw new BadRequestException({ code: 'IDEMPOTENCY_KEY_INVALID' });
    const sessionHash = hash(actor.sessionToken);
    const requestHash = hash(JSON.stringify({ buId, ...body }));
    let expectedCredentialVersion: number | null = null;
    const { attempt, replay } = await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, buId);
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'instagram-attempt-actor:' + actor.id}, 0))::text AS locked`;
      await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'instagram-attempt-bu:' + buId}, 0))::text AS locked`;
      const prior = await tx.instagramAuthorizationAttempt.findUnique({ where: { mantenedoraId_idempotencyKey: { mantenedoraId: actor.mantenedoraId, idempotencyKey } } });
      if (prior) {
        if (prior.userId !== actor.id || prior.sessionHash !== sessionHash) throw new ConflictException({ code: 'ATTEMPT_SESSION_MISMATCH' });
        if (prior.requestHash !== requestHash) throw new ConflictException({ code: 'IDEMPOTENCY_CONFLICT' });
        return { attempt: prior, replay: true };
      }
      const bu = await tx.businessUnit.findFirst({ where: { id: buId, mantenedoraId: actor.mantenedoraId }, select: { id: true } });
      if (!bu) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
      if (body.operation === 'REAUTHORIZE') {
        const channel = await tx.buChannel.findFirst({ where: { id: body.channelId, buId, type: 'INSTAGRAM' }, select: { id: true, generation: true, businessIdentity: { select: { externalResourceId: true } } } });
        if (!channel) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
        if (!channel.businessIdentity) throw new ConflictException({ code: 'BUSINESS_RESOURCE_OWNER_CONFLICT' });
        await this.lockMappedResource(tx, channel.businessIdentity.externalResourceId);
        await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${channel.id} FOR UPDATE`;
        if (channel.generation !== body.expectedGeneration) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
        const credential = await tx.channelCredential.findUnique({ where: { channelId: channel.id }, select: { provider: true, generation: true, version: true } });
        if (!credential || credential.provider !== 'INSTAGRAM' || credential.generation !== channel.generation) throw new ConflictException({ code: 'CREDENTIAL_UNAVAILABLE' });
        expectedCredentialVersion = credential.version;
      }
      const since = new Date(Date.now() - BUDGET_WINDOW_MS);
      const [actorCount, buCount] = await Promise.all([
        tx.instagramAuthorizationAttempt.count({ where: { userId: actor.id, createdAt: { gte: since } } }),
        tx.instagramAuthorizationAttempt.count({ where: { buId, createdAt: { gte: since } } }),
      ]);
      if (actorCount >= 10 || buCount >= 30) {
        const [actorOldest, buOldest] = await Promise.all([
          actorCount >= 10 ? tx.instagramAuthorizationAttempt.findFirst({ where: { userId: actor.id, createdAt: { gte: since } }, orderBy: { createdAt: 'asc' }, select: { createdAt: true } }) : null,
          buCount >= 30 ? tx.instagramAuthorizationAttempt.findFirst({ where: { buId, createdAt: { gte: since } }, orderBy: { createdAt: 'asc' }, select: { createdAt: true } }) : null,
        ]);
        const resetTimes = [actorOldest, buOldest].filter((row): row is { createdAt: Date } => row !== null)
          .map(({ createdAt }) => createdAt.getTime() + BUDGET_WINDOW_MS);
        const retryAfterSeconds = Math.max(1, Math.ceil((Math.max(...resetTimes) - Date.now()) / 1000));
        throw new HttpException({ code: 'AUTHORIZATION_BUDGET_EXHAUSTED', retryAfterSeconds }, HttpStatus.TOO_MANY_REQUESTS);
      }
      const id = randomUUID();
      const state = this.stateFor(id, sessionHash, config.clientSecret);
      await this.requireActorTx(tx, actor, buId);
      const created = await tx.instagramAuthorizationAttempt.create({ data: {
        id, mantenedoraId: actor.mantenedoraId, buId, userId: actor.id, sessionHash,
        idempotencyKey, requestHash, operation: body.operation, channelId: body.channelId ?? null,
        expectedGeneration: body.expectedGeneration ?? null, stateHash: hash(state), expiresAt: new Date(Date.now() + TTL),
        expectedCredentialVersion,
      } });
      await this.activity.registrar(tx, actor.mantenedoraId, 'instagram.autorizacao.iniciada', this.auditActor(actor), { buId, entidadeId: id });
      return { attempt: created, replay: false };
    });
    if (replay) return this.authorizationDto(attempt, config);
    return this.authorizationDto(attempt, config);
  }

  async authorizeBusinessUnit(actor: InstagramActor, buId: string) {
    await this.requireAdmin(actor, buId);
  }

  async authorizeAttempt(actor: InstagramActor, id: string) {
    await this.requireAttempt(actor, id);
  }

  async callback(actor: InstagramActor, state: string, code: string) {
    const parsed = /^([0-9a-f-]{36})\.([a-f0-9]{64})$/.exec(state);
    if (!parsed || !code || code.length > 4096) throw new BadRequestException({ code: 'OAUTH_STATE_INVALID' });
    const sessionHash = hash(actor.sessionToken);
    const attempt = await this.prisma.instagramAuthorizationAttempt.findFirst({ where: { id: parsed[1], mantenedoraId: actor.mantenedoraId } });
    if (!attempt) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    await this.requireAdmin(actor, attempt.buId);
    if (attempt.userId !== actor.id || attempt.sessionHash !== sessionHash || attempt.expiresAt <= new Date() || !safeEqual(attempt.stateHash, hash(state))) {
      throw new ForbiddenException({ code: 'OAUTH_STATE_INVALID' });
    }
    const config = instagramConfig();
    if (!config) throw new ServiceUnavailableException({ code: 'INSTAGRAM_UNAVAILABLE' });
    const expectedState = this.stateFor(parsed[1], sessionHash, config.clientSecret);
    if (!safeEqual(hash(state), hash(expectedState))) throw new ForbiddenException({ code: 'OAUTH_STATE_INVALID' });
    const lease = randomBytes(24).toString('hex');
    const callbackDeadlineAt = new Date(Date.now() + 40_000);
    const claimed = await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, attempt.buId);
      const result = await tx.$queryRaw<Array<{ id: string }>>`UPDATE instagram_authorization_attempts
        SET status = 'EXCHANGING', callback_lease_token = ${lease}, callback_lease_until = clock_timestamp() + interval '60 seconds',
          operation_deadline_at = ${callbackDeadlineAt}, updated_at = clock_timestamp()
        WHERE id = ${attempt.id} AND status = 'AUTHORIZATION_PENDING' AND expires_at > clock_timestamp()
          AND callback_lease_token IS NULL AND state_hash = ${hash(state)} AND user_id = ${actor.id}
          AND session_hash = ${sessionHash} AND ${callbackDeadlineAt} > clock_timestamp()
        RETURNING id`;
      return result.length;
    });
    this.assertSignedSession(actor);
    if (claimed !== 1) throw new ConflictException({ code: 'OAUTH_CALLBACK_ALREADY_USED' });
    let candidate: Awaited<ReturnType<InstagramHttpClient['exchangeCode']>>;
    try {
      candidate = await this.http.exchangeCode(code, config, () => this.revalidateCallbackOwner(actor, attempt.id, lease), callbackDeadlineAt);
    } catch {
      await this.actorTransaction(actor, async (tx) => {
        await this.requireActorTx(tx, actor, attempt.buId);
        const stillOwned = await tx.$queryRaw<Array<{ id: string; callback_lease_until: Date; operation_deadline_at: Date; expires_at: Date }>>`SELECT id, callback_lease_until, operation_deadline_at, expires_at FROM instagram_authorization_attempts
          WHERE id = ${attempt.id} AND status = 'EXCHANGING' AND callback_lease_token = ${lease}
            AND callback_lease_until > clock_timestamp() AND operation_deadline_at > clock_timestamp()
            AND expires_at > clock_timestamp() AND user_id = ${actor.id} AND session_hash = ${sessionHash}
          FOR UPDATE`;
        if (stillOwned.length !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
        await this.requireActorTx(tx, actor, attempt.buId);
        const failed = await tx.$queryRaw<Array<{ id: string }>>`UPDATE instagram_authorization_attempts SET status = 'FAILED_SAFE',
          callback_lease_token = NULL, callback_lease_until = NULL, operation_deadline_at = NULL, updated_at = clock_timestamp()
          WHERE id = ${attempt.id} AND status = 'EXCHANGING' AND callback_lease_token = ${lease}
            AND callback_lease_until > clock_timestamp() AND operation_deadline_at > clock_timestamp()
            AND expires_at > clock_timestamp() AND user_id = ${actor.id} AND session_hash = ${sessionHash}
          RETURNING id`;
        if (failed.length !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
        this.assertSignedSession(actor);
        const [clock] = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
        const finalNow = Math.max(clock.now.getTime(), Date.now());
        if (finalNow >= stillOwned[0].callback_lease_until.getTime() || finalNow >= stillOwned[0].operation_deadline_at.getTime()
          || finalNow >= stillOwned[0].expires_at.getTime()) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      });
      this.assertSignedSession(actor);
      throw new ServiceUnavailableException({ code: 'OAUTH_EXCHANGE_UNCERTAIN' });
    }
    const { keyId, key } = loadChannelCredentialKey(process.env);
    const encrypted = sealChannelCredential(candidate.accessToken, keyId, key, {
      purpose: 'candidate', provider: 'INSTAGRAM', buId: attempt.buId, channelId: attempt.channelId ?? attempt.id,
      generation: attempt.expectedGeneration ?? 1, attemptId: attempt.id,
    });
    const completed = await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, attempt.buId);
      const owned = await tx.$queryRaw<Array<{ id: string; callback_lease_until: Date; operation_deadline_at: Date; expires_at: Date }>>`SELECT id, callback_lease_until, operation_deadline_at, expires_at FROM instagram_authorization_attempts WHERE id = ${attempt.id} AND status = 'EXCHANGING' AND callback_lease_token = ${lease} AND callback_lease_until > clock_timestamp() AND operation_deadline_at > clock_timestamp() AND expires_at > clock_timestamp() AND user_id = ${actor.id} AND session_hash = ${sessionHash} AND ${candidate.expiresAt} > clock_timestamp() + interval '60 seconds' FOR UPDATE`;
      if (owned.length !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      await this.requireActorTx(tx, actor, attempt.buId);
      const candidateNonce = Uint8Array.from(encrypted.nonce);
      const candidateCiphertext = Uint8Array.from(encrypted.ciphertext);
      const candidateTag = Uint8Array.from(encrypted.tag);
      const written = await tx.$queryRaw<Array<{ id: string }>>`UPDATE instagram_authorization_attempts SET
        status = 'CANDIDATE_READY', callback_lease_token = NULL, callback_lease_until = NULL, operation_deadline_at = NULL,
        authorization_reference = ${candidate.authorizationReference}, professional_user_id = ${candidate.professionalUserId},
        username = ${candidate.username}, candidate_key_id = ${encrypted.keyId}, candidate_nonce = ${candidateNonce},
        candidate_ciphertext = ${candidateCiphertext}, candidate_tag = ${candidateTag}, acquired_at = ${candidate.acquiredAt},
        credential_expires_at = ${candidate.expiresAt}, updated_at = clock_timestamp()
        WHERE id = ${attempt.id} AND status = 'EXCHANGING' AND callback_lease_token = ${lease}
          AND callback_lease_until > clock_timestamp() AND operation_deadline_at > clock_timestamp()
          AND expires_at > clock_timestamp() AND user_id = ${actor.id} AND session_hash = ${sessionHash}
          AND ${candidate.expiresAt} > clock_timestamp() + interval '60 seconds'
        RETURNING id`;
      if (written.length === 1) await this.activity.registrar(tx, actor.mantenedoraId, 'instagram.autorizacao.recebida', this.auditActor(actor), { buId: attempt.buId, entidadeId: attempt.id });
      this.assertSignedSession(actor);
      const [clock] = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
      const finalNow = Math.max(clock.now.getTime(), Date.now());
      if (finalNow >= owned[0].callback_lease_until.getTime() || finalNow >= owned[0].operation_deadline_at.getTime()
        || finalNow >= owned[0].expires_at.getTime() || finalNow + 60_000 >= candidate.expiresAt.getTime()) {
        throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      }
      return written.length;
    });
    this.assertSignedSession(actor);
    if (completed !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
    return { attemptId: attempt.id, status: 'CANDIDATE_READY' as const };
  }

  async get(actor: InstagramActor, id: string) {
    const attempt = await this.prisma.instagramAuthorizationAttempt.findFirst({ where: { id, mantenedoraId: actor.mantenedoraId } });
    if (!attempt) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    await this.requireAdmin(actor, attempt.buId);
    if (attempt.userId !== actor.id || attempt.sessionHash !== hash(actor.sessionToken)) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    return { id: attempt.id, buId: attempt.buId, status: attempt.status, operation: attempt.operation,
      account: attempt.professionalUserId ? { username: attempt.username } : null,
      expiresAt: attempt.expiresAt.toISOString(), subscriptionState: attempt.subscriptionState };
  }

  async cancel(actor: InstagramActor, id: string) {
    const attempt = await this.requireAttempt(actor, id);
    await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, attempt.buId);
      await this.lockMappedResource(tx, attempt.professionalUserId);
      if (attempt.channelId) await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${attempt.channelId} FOR UPDATE`;
      const locked = await tx.$queryRaw<Array<{ id: string }>>`SELECT id FROM instagram_authorization_attempts WHERE id = ${id} AND user_id = ${actor.id} AND session_hash = ${hash(actor.sessionToken)} FOR UPDATE`;
      if (locked.length !== 1) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
      const current = await tx.instagramAuthorizationAttempt.findUnique({ where: { id } });
      if (!current || current.mantenedoraId !== actor.mantenedoraId) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
      if (!['CANDIDATE_READY', 'AUTHORIZATION_PENDING', 'FAILED_SAFE', 'EXCHANGING', 'MAPPED_PENDING_SUBSCRIPTION', 'MAPPED_PENDING_RECEIPT'].includes(current.status)) return;
      await this.requireActorTx(tx, actor, attempt.buId);
      const changed = await tx.instagramAuthorizationAttempt.updateMany({ where: {
        id, userId: actor.id, sessionHash: hash(actor.sessionToken), status: current.status,
        callbackLeaseToken: current.callbackLeaseToken, operationLeaseToken: current.operationLeaseToken,
      }, data: {
        status: 'CANCELLED', callbackLeaseToken: null, callbackLeaseUntil: null,
        candidateKeyId: null, candidateNonce: null, candidateCiphertext: null, candidateTag: null,
        operationLeaseToken: null, operationLeaseUntil: null, operationDeadlineAt: null,
        ...(current.subscriptionState === 'OBSERVING' ? { subscriptionState: 'UNCERTAIN' } : {}),
      } });
      if (changed.count !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      await this.activity.registrar(tx, actor.mantenedoraId, 'instagram.autorizacao.cancelada', this.auditActor(actor), { buId: attempt.buId, entidadeId: id });
      this.assertSignedSession(actor);
    });
    this.assertSignedSession(actor);
    return this.get(actor, id);
  }

  async confirm(actor: InstagramActor, id: string, idempotencyKey: string, expectedGeneration?: number) {
    const invocationDeadlineAt = new Date(Date.now() + 40_000);
    if (!KEY.test(idempotencyKey)) throw new BadRequestException({ code: 'IDEMPOTENCY_KEY_INVALID' });
    const requestHash = hash(JSON.stringify({ id, expectedGeneration: expectedGeneration ?? null }));
    let attempt = await this.requireAttempt(actor, id);
    const claim = await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, attempt.buId);
      await this.lockMappedResource(tx, attempt.professionalUserId);
      if (attempt.channelId) await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${attempt.channelId} FOR UPDATE`;
      const locked = await tx.$queryRaw<Array<{ id: string }>>`SELECT id FROM instagram_authorization_attempts WHERE id = ${id} AND mantenedora_id = ${actor.mantenedoraId} AND user_id = ${actor.id} AND session_hash = ${hash(actor.sessionToken)} FOR UPDATE`;
      if (locked.length !== 1) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
      const current = await tx.instagramAuthorizationAttempt.findUnique({ where: { id } });
      if (!current) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
      if (current.expiresAt <= new Date() && current.status === 'CANDIDATE_READY') {
        throw new ConflictException({ code: 'OAUTH_ATTEMPT_EXPIRED' });
      }
      await this.requireActorTx(tx, actor, attempt.buId);
      if (current.confirmationIdempotencyKey) {
        if (current.confirmationIdempotencyKey !== idempotencyKey || current.confirmationRequestHash !== requestHash) {
          throw new ConflictException({ code: 'IDEMPOTENCY_CONFLICT' });
        }
        if (current.confirmationState === 'COMPLETED' && current.confirmationResultStatus && current.confirmationResultSubscriptionState) {
          return { attempt: current, replay: true, busy: false };
        }
        if (current.confirmationState === 'IN_PROGRESS' && ((current.status === 'CANDIDATE_READY' && current.updatedAt.getTime() > Date.now() - 60_000)
          || (current.status === 'MAPPED_PENDING_SUBSCRIPTION' && current.subscriptionState === 'NOT_STARTED'
            && current.operationDeadlineAt && current.operationDeadlineAt > new Date())
          || (current.operationLeaseUntil && current.operationLeaseUntil > new Date()))) {
          return { attempt: current, replay: false, busy: true };
        }
        await tx.instagramAuthorizationAttempt.update({ where: { id }, data: { operationDeadlineAt: invocationDeadlineAt } });
      } else {
        if (current.status !== 'CANDIDATE_READY') throw new ConflictException({ code: 'CANDIDATE_NOT_READY' });
        if ((current.expectedGeneration ?? undefined) !== expectedGeneration) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
        await tx.instagramAuthorizationAttempt.update({ where: { id }, data: {
          confirmationIdempotencyKey: idempotencyKey, confirmationRequestHash: requestHash, confirmationState: 'IN_PROGRESS', operationDeadlineAt: invocationDeadlineAt,
        } });
        await this.activity.registrar(tx, actor.mantenedoraId, 'instagram.autorizacao.confirmada', this.auditActor(actor), { buId: attempt.buId, entidadeId: id });
      }
      return { attempt: current.confirmationIdempotencyKey ? current : { ...current, confirmationIdempotencyKey: idempotencyKey, confirmationRequestHash: requestHash, confirmationState: 'IN_PROGRESS' }, replay: false, busy: false };
    });
    attempt = claim.attempt;
    if (claim.busy) throw new ConflictException({ code: 'CONFIRMATION_IN_PROGRESS' });
    if (claim.replay) return { id, status: attempt.confirmationResultStatus, channelId: attempt.confirmationResultChannelId, subscriptionState: attempt.confirmationResultSubscriptionState };

    const config = instagramConfig();
    if (!config) throw new ServiceUnavailableException({ code: 'INSTAGRAM_UNAVAILABLE' });
    if ((attempt.expectedGeneration ?? undefined) !== expectedGeneration) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
    let token: string;
    let channel: { id: string; generation: number } | null;
    let version: number;
    if (attempt.status === 'MAPPED_PENDING_SUBSCRIPTION' || attempt.status === 'MAPPED_PENDING_RECEIPT') {
      if (!attempt.channelId || !attempt.professionalUserId) throw new ConflictException({ code: 'MAPPING_REQUIRED' });
      const credential = await this.prisma.channelCredential.findUnique({ where: { channelId: attempt.channelId } });
      if (!credential) throw new ConflictException({ code: 'CREDENTIAL_UNAVAILABLE' });
      const keys = loadChannelCredentialKey(process.env);
      token = openChannelCredential({ keyId: credential.keyId, nonce: Buffer.from(credential.nonce), ciphertext: Buffer.from(credential.ciphertext), tag: Buffer.from(credential.tag) }, new Map([[keys.keyId, keys.key]]), {
        purpose: 'active', provider: 'INSTAGRAM', buId: attempt.buId, channelId: attempt.channelId, generation: credential.generation, version: credential.version,
      }).toString('utf8');
      channel = await this.prisma.buChannel.findFirst({ where: { id: attempt.channelId, buId: attempt.buId, type: 'INSTAGRAM' } });
      version = credential.version;
    } else {
      if (attempt.status !== 'CANDIDATE_READY' || !attempt.professionalUserId || !attempt.candidateKeyId || !attempt.candidateNonce || !attempt.candidateCiphertext || !attempt.candidateTag || !attempt.credentialExpiresAt || !attempt.acquiredAt) {
        throw new ConflictException({ code: 'CANDIDATE_NOT_READY' });
      }
      if (attempt.credentialExpiresAt.getTime() <= Date.now() + 60_000) throw new ConflictException({ code: 'CREDENTIAL_EXPIRED' });
      const key = loadChannelCredentialKey(process.env);
      token = openChannelCredential({ keyId: attempt.candidateKeyId, nonce: Buffer.from(attempt.candidateNonce), ciphertext: Buffer.from(attempt.candidateCiphertext), tag: Buffer.from(attempt.candidateTag) }, new Map([[key.keyId, key.key]]), {
        purpose: 'candidate', provider: 'INSTAGRAM', buId: attempt.buId, channelId: attempt.channelId ?? attempt.id,
        generation: attempt.expectedGeneration ?? 1, attemptId: attempt.id,
      }).toString('utf8');
      const scope = `${config.clientId}:graph.instagram.com:${attempt.professionalUserId}`;
      const mapping = await this.actorTransaction(actor, async (tx) => {
        await this.requireActorTx(tx, actor, attempt.buId);
        await this.lockMappedResource(tx, attempt.professionalUserId);
        if (attempt.channelId) await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${attempt.channelId} FOR UPDATE`;
        const lockedAttempt = await tx.$queryRaw<Array<{ id: string }>>`SELECT id FROM instagram_authorization_attempts
          WHERE id = ${id} AND status = 'CANDIDATE_READY' AND confirmation_idempotency_key = ${idempotencyKey}
            AND confirmation_request_hash = ${requestHash} AND user_id = ${actor.id} AND session_hash = ${hash(actor.sessionToken)}
            AND expires_at > clock_timestamp() AND operation_deadline_at > clock_timestamp()
            AND credential_expires_at > clock_timestamp() + interval '60 seconds'
          FOR UPDATE`;
        if (lockedAttempt.length !== 1) {
          const live = await tx.instagramAuthorizationAttempt.findUnique({ where: { id }, select: {
            status: true, confirmationIdempotencyKey: true, confirmationRequestHash: true, userId: true, sessionHash: true,
            expiresAt: true, credentialExpiresAt: true, operationDeadlineAt: true,
          } });
          if (!live || live.status !== 'CANDIDATE_READY' || live.confirmationIdempotencyKey !== idempotencyKey
            || live.confirmationRequestHash !== requestHash || live.userId !== actor.id || live.sessionHash !== hash(actor.sessionToken)) {
            throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
          }
          const observedAt = new Date();
          if (live.expiresAt <= observedAt) throw new ConflictException({ code: 'OAUTH_ATTEMPT_EXPIRED' });
          if (!live.credentialExpiresAt || live.credentialExpiresAt.getTime() <= observedAt.getTime() + 60_000) throw new ConflictException({ code: 'CREDENTIAL_EXPIRED' });
          if (!live.operationDeadlineAt || live.operationDeadlineAt <= observedAt) throw new ConflictException({ code: 'OPERATION_DEADLINE_EXCEEDED' });
          throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
        }
        await this.requireActorTx(tx, actor, attempt.buId);
        const current = await tx.instagramAuthorizationAttempt.findFirst({ where: { id, status: 'CANDIDATE_READY', confirmationIdempotencyKey: idempotencyKey, confirmationRequestHash: requestHash, userId: actor.id, sessionHash: hash(actor.sessionToken) } });
        if (!current || current.expiresAt <= new Date() || !current.credentialExpiresAt || current.credentialExpiresAt.getTime() <= Date.now() + 60_000
          || current.professionalUserId !== attempt.professionalUserId) throw new ConflictException({ code: 'OAUTH_ATTEMPT_EXPIRED' });
      let channel;
      if (attempt.operation === 'REAUTHORIZE') {
        channel = await tx.buChannel.findFirst({ where: { id: attempt.channelId!, buId: attempt.buId, type: 'INSTAGRAM', generation: expectedGeneration } });
        if (!channel) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
        const identity = await tx.businessChannelIdentity.findUnique({ where: { platform_namespace_externalResourceId: { platform: 'INSTAGRAM', namespace: 'INSTAGRAM_LOGIN', externalResourceId: attempt.professionalUserId! } } });
        if (!identity || identity.buId !== attempt.buId || identity.scopeReference !== scope || channel.businessIdentityId !== identity.id) throw new ConflictException({ code: 'BUSINESS_RESOURCE_OWNER_CONFLICT' });
      } else {
        const existing = await tx.businessChannelIdentity.findUnique({ where: { platform_namespace_externalResourceId: { platform: 'INSTAGRAM', namespace: 'INSTAGRAM_LOGIN', externalResourceId: attempt.professionalUserId! } } });
        if (existing && (existing.buId !== attempt.buId || existing.scopeReference !== scope)) throw new ConflictException({ code: 'BUSINESS_RESOURCE_OWNER_CONFLICT' });
        const business = existing ?? await tx.businessChannelIdentity.create({ data: { buId: attempt.buId, platform: 'INSTAGRAM', namespace: 'INSTAGRAM_LOGIN', scopeReference: scope, externalResourceId: attempt.professionalUserId! } });
        channel = await tx.buChannel.findFirst({ where: { buId: attempt.buId, type: 'INSTAGRAM', businessIdentityId: business.id } });
        if (channel) throw new ConflictException({ code: 'CHANNEL_ALREADY_EXISTS' });
        channel = await tx.buChannel.create({ data: { buId: attempt.buId, type: 'INSTAGRAM', businessIdentityId: business.id, status: 'CONECTANDO', ownNumberVerified: true, verifiedEpoch: 0, providerConnectionState: 'MAPPED_PENDING_SUBSCRIPTION', requiresWindow: true } });
        const priorResource = await tx.providerResourceIdentity.findUnique({ where: { provider_externalResourceId: { provider: 'INSTAGRAM', externalResourceId: attempt.professionalUserId! } } });
        if (priorResource && (priorResource.buId !== attempt.buId || priorResource.businessIdentityId !== business.id || priorResource.currentChannelId)) throw new ConflictException({ code: 'PROVIDER_RESOURCE_OWNER_CONFLICT' });
        if (!priorResource) await tx.providerResourceIdentity.create({ data: { provider: 'INSTAGRAM', externalResourceId: attempt.professionalUserId!, buId: attempt.buId, currentChannelId: channel.id, businessIdentityId: business.id, managedLifecycle: true, cleanupState: 'ACTIVE' } });
        else await tx.providerResourceIdentity.update({ where: { id: priorResource.id }, data: { currentChannelId: channel.id, retiredAt: null, cleanupState: 'ACTIVE' } });
      }
      const old = await tx.channelCredential.findUnique({ where: { channelId: channel.id }, select: { version: true } });
      if (attempt.operation === 'REAUTHORIZE' && old?.version !== attempt.expectedCredentialVersion) {
        throw new ConflictException({ code: 'CHANNEL_CREDENTIAL_STALE' });
      }
      const binding = await tx.providerResourceIdentity.findUnique({ where: { provider_externalResourceId: { provider: 'INSTAGRAM', externalResourceId: attempt.professionalUserId! } }, select: {
        id: true, instagramOperationLeaseUntil: true, instagramLastSubscriptionAttemptAt: true,
      } });
      if (binding?.instagramOperationLeaseUntil && binding.instagramOperationLeaseUntil > new Date()) throw new ConflictException({ code: 'OPERATION_IN_PROGRESS' });
      const version = (old?.version ?? 0) + 1;
      const { keyId, key } = loadChannelCredentialKey(process.env);
      const encrypted = sealChannelCredential(token, keyId, key, { purpose: 'active', provider: 'INSTAGRAM', buId: attempt.buId, channelId: channel.id, generation: channel.generation, version });
      await this.requireActorTx(tx, actor, attempt.buId);
      await tx.channelCredential.upsert({ where: { channelId: channel.id }, create: { channelId: channel.id, provider: 'INSTAGRAM', buId: attempt.buId, generation: channel.generation, version, acquiredAt: attempt.acquiredAt, expiresAt: attempt.credentialExpiresAt, keyId: encrypted.keyId, nonce: Uint8Array.from(encrypted.nonce), ciphertext: Uint8Array.from(encrypted.ciphertext), tag: Uint8Array.from(encrypted.tag) }, update: { provider: 'INSTAGRAM', buId: attempt.buId, generation: channel.generation, version, acquiredAt: attempt.acquiredAt, expiresAt: attempt.credentialExpiresAt, keyId: encrypted.keyId, nonce: Uint8Array.from(encrypted.nonce), ciphertext: Uint8Array.from(encrypted.ciphertext), tag: Uint8Array.from(encrypted.tag) } });
      await this.requireActorTx(tx, actor, attempt.buId);
      const promoted = await tx.$queryRaw<Array<{ id: string }>>`UPDATE instagram_authorization_attempts SET
        status = 'MAPPED_PENDING_SUBSCRIPTION', subscription_started_at = clock_timestamp(), channel_id = ${channel.id},
        mapped_credential_version = ${version}, candidate_key_id = NULL, candidate_nonce = NULL,
        candidate_ciphertext = NULL, candidate_tag = NULL, updated_at = clock_timestamp()
        WHERE id = ${id} AND status = 'CANDIDATE_READY' AND confirmation_idempotency_key = ${idempotencyKey}
          AND confirmation_request_hash = ${requestHash} AND user_id = ${actor.id} AND session_hash = ${hash(actor.sessionToken)}
          AND expires_at > clock_timestamp() AND operation_deadline_at > clock_timestamp()
          AND credential_expires_at > clock_timestamp() + interval '60 seconds'
        RETURNING id`;
      if (promoted.length !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      await this.assertFreshMappingClock(tx, current);
      this.assertSignedSession(actor);
      return { channel, version };
      });
      this.assertSignedSession(actor);
      channel = mapping.channel;
      version = mapping.version;
    }
    if (!channel) throw new ConflictException({ code: 'CHANNEL_GENERATION_STALE' });
    await this.requireLiveActor(actor, attempt.buId);
    const subscriptionState = attempt.status === 'MAPPED_PENDING_RECEIPT' ? 'SUBSCRIBED'
      : await this.subscribeAfterMapping(actor, id, channel.id, attempt.buId, channel.generation, version, attempt.professionalUserId!, token, false, invocationDeadlineAt);
    this.assertSignedSession(actor);
    const result = { id, status: subscriptionState === 'SUBSCRIBED' ? 'MAPPED_PENDING_RECEIPT' : 'SUBSCRIPTION_UNCERTAIN', channelId: channel.id, subscriptionState };
    await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, attempt.buId);
      await this.lockAttemptResource(tx, id, channel.id);
      if (result.subscriptionState === 'SUBSCRIBED') {
        if (!await this.assertMappedSubscriptionResult(tx, actor, id, channel.id, attempt.buId, channel.generation, version, attempt.professionalUserId!)) {
          throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        }
      } else {
        if (!await this.assertMappedUncertainResult(tx, actor, id, channel.id, attempt.buId, channel.generation, version, attempt.professionalUserId!)) {
          throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        }
      }
      await this.requireActorTx(tx, actor, attempt.buId);
      const saved = await tx.instagramAuthorizationAttempt.updateMany({ where: {
        id, confirmationIdempotencyKey: idempotencyKey, confirmationRequestHash: requestHash,
        userId: actor.id, sessionHash: hash(actor.sessionToken),
        status: result.subscriptionState === 'SUBSCRIBED' ? 'MAPPED_PENDING_RECEIPT' : 'MAPPED_PENDING_SUBSCRIPTION',
        subscriptionState: result.subscriptionState, operationLeaseToken: null,
      }, data: {
        confirmationState: 'COMPLETED', confirmationResultStatus: result.status, confirmationResultChannelId: result.channelId,
        confirmationResultSubscriptionState: result.subscriptionState,
      } });
      if (saved.count !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      this.assertSignedSession(actor);
    });
    this.assertSignedSession(actor);
    return result;
  }

  async advance(actor: InstagramActor, id: string) {
    const invocationDeadlineAt = new Date(Date.now() + 40_000);
    const attempt = await this.requireAttempt(actor, id);
    if (attempt.status === 'MAPPED_PENDING_RECEIPT' || attempt.subscriptionState === 'SUBSCRIBED') {
      if (!attempt.channelId || !attempt.professionalUserId || attempt.mappedCredentialVersion === null) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
      const current = await this.actorTransaction(actor, async (tx) => {
        await this.requireActorTx(tx, actor, attempt.buId);
        await this.lockAttemptResource(tx, attempt.id, attempt.channelId!);
        const channel = await tx.buChannel.findFirst({ where: { id: attempt.channelId!, buId: attempt.buId, type: 'INSTAGRAM' }, select: { generation: true } });
        if (!channel) return false;
        return this.assertMappedSubscriptionResult(tx, actor, attempt.id, attempt.channelId!, attempt.buId, channel.generation,
          attempt.mappedCredentialVersion!, attempt.professionalUserId!);
      });
      this.assertSignedSession(actor);
      if (!current) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
      return { id, status: 'MAPPED_PENDING_RECEIPT', subscriptionState: 'SUBSCRIBED' };
    }
    if (!attempt.channelId || !attempt.professionalUserId) throw new ConflictException({ code: 'MAPPING_REQUIRED' });
    const credential = await this.prisma.channelCredential.findUnique({ where: { channelId: attempt.channelId } });
    if (!credential || credential.provider !== 'INSTAGRAM' || credential.buId !== attempt.buId) throw new ConflictException({ code: 'CREDENTIAL_UNAVAILABLE' });
    if (credential.expiresAt && credential.expiresAt.getTime() <= Date.now() + 60_000) throw new ConflictException({ code: 'CREDENTIAL_EXPIRED' });
    const keys = loadChannelCredentialKey(process.env);
    const token = openChannelCredential({ keyId: credential.keyId, nonce: Buffer.from(credential.nonce), ciphertext: Buffer.from(credential.ciphertext), tag: Buffer.from(credential.tag) }, new Map([[keys.keyId, keys.key]]), {
      purpose: 'active', provider: 'INSTAGRAM', buId: attempt.buId, channelId: attempt.channelId, generation: credential.generation, version: credential.version,
    }).toString('utf8');
    const state = await this.subscribeAfterMapping(actor, id, attempt.channelId, attempt.buId, credential.generation, credential.version, attempt.professionalUserId, token, true, invocationDeadlineAt);
    this.assertSignedSession(actor);
    return { id, status: state === 'SUBSCRIBED' ? 'MAPPED_PENDING_RECEIPT' : 'SUBSCRIPTION_UNCERTAIN', subscriptionState: state };
  }

  private async subscribeAfterMapping(actor: InstagramActor, attemptId: string, channelId: string, buId: string, generation: number, version: number, accountId: string, token: string, recordAdvance = false, invocationDeadlineAt?: Date) {
    const config = instagramConfig();
    if (!config) throw new ServiceUnavailableException({ code: 'INSTAGRAM_UNAVAILABLE' });
    const lease = randomBytes(24).toString('hex');
    const deadlineAt = invocationDeadlineAt ?? new Date(Date.now() + 40_000);
    let alreadySubscribed = false;
    let mustObserve = false;
    try {
      await this.actorTransaction(actor, async (tx) => {
        await this.requireActorTx(tx, actor, buId);
        await this.lockMappedResource(tx, accountId);
        await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${channelId} FOR UPDATE`;
        await tx.$queryRaw`SELECT id FROM instagram_authorization_attempts WHERE id = ${attemptId} FOR UPDATE`;
        const attempt = await tx.instagramAuthorizationAttempt.findFirst({ where: { id: attemptId, channelId, buId, userId: actor.id, sessionHash: hash(actor.sessionToken) } });
        const channel = await tx.buChannel.findFirst({ where: { id: channelId, buId, type: 'INSTAGRAM', generation }, select: { id: true, status: true, businessIdentityId: true, receiptVerifiedAt: true } });
        if (!attempt || !channel || !attempt.professionalUserId || attempt.professionalUserId !== accountId) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        const [credential, identity] = await Promise.all([
          tx.channelCredential.findFirst({ where: { channelId, buId, provider: 'INSTAGRAM', generation, version }, select: { expiresAt: true } }),
          tx.providerResourceIdentity.findFirst({ where: { provider: 'INSTAGRAM', externalResourceId: accountId, buId, currentChannelId: channelId, businessIdentityId: channel.businessIdentityId, retiredAt: null }, select: { id: true } }),
        ]);
        if (!credential || !identity || attempt.mappedCredentialVersion !== version) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        const binding = await tx.providerResourceIdentity.findUnique({ where: { provider_externalResourceId: { provider: 'INSTAGRAM', externalResourceId: accountId } }, select: {
          id: true, instagramOperationLeaseToken: true, instagramOperationLeaseUntil: true,
          instagramLastSubscriptionAttemptAt: true, instagramSubscriptionPostDispatchStartedAt: true,
        } });
        if (!binding) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        if (!channel.receiptVerifiedAt && credential.expiresAt && credential.expiresAt.getTime() <= Date.now() + 60_000) throw new ConflictException({ code: 'CREDENTIAL_EXPIRED' });
        if (attempt.subscriptionState === 'SUBSCRIBED') { alreadySubscribed = true; return; }
        if (attempt.status !== 'MAPPED_PENDING_SUBSCRIPTION') throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        const [priorSubscribed, priorMutation] = await Promise.all([
          tx.instagramAuthorizationAttempt.findFirst({ where: { id: { not: attemptId }, professionalUserId: accountId, subscriptionState: 'SUBSCRIBED' }, select: { id: true } }),
          tx.instagramAuthorizationAttempt.findFirst({ where: { id: { not: attemptId }, professionalUserId: accountId, subscriptionRequests: { gt: 0 } }, select: { id: true } }),
        ]);
        if (priorSubscribed) { alreadySubscribed = true; return; }
        mustObserve = attempt.subscriptionRequests > 0 || binding.instagramSubscriptionPostDispatchStartedAt !== null || Boolean(priorMutation);
        const claimedAt = new Date();
        if (deadlineAt.getTime() <= claimedAt.getTime()) throw new ConflictException({ code: 'OPERATION_DEADLINE_EXCEEDED' });
        if ((binding.instagramOperationLeaseUntil && binding.instagramOperationLeaseUntil > claimedAt)
          || (attempt.operationLeaseUntil && attempt.operationLeaseUntil > claimedAt)) throw new ConflictException({ code: 'OPERATION_IN_PROGRESS' });
        if (binding.instagramLastSubscriptionAttemptAt && claimedAt.getTime() - binding.instagramLastSubscriptionAttemptAt.getTime() < 10_000) throw new HttpException({ code: 'OPERATION_COOLDOWN' }, HttpStatus.TOO_MANY_REQUESTS);
        if (attempt.subscriptionRequests >= 3) throw new ConflictException({ code: 'SUBSCRIPTION_REQUEST_BUDGET_EXHAUSTED' });
        await this.requireActorTx(tx, actor, buId);
        // Commit first-POST intent before network I/O so a lost acknowledgement
        // or interrupted writer can never authorize a second POST.
        const bindingClaim = await tx.$queryRaw<Array<{ id: string }>>`UPDATE provider_resource_identities
          SET instagram_operation_lease_token = ${lease}, instagram_operation_lease_until = clock_timestamp() + interval '60 seconds',
              instagram_last_subscription_attempt_at = clock_timestamp(),
              instagram_subscription_post_dispatch_started_at = CASE WHEN ${!mustObserve}
                THEN COALESCE(instagram_subscription_post_dispatch_started_at, clock_timestamp()) ELSE instagram_subscription_post_dispatch_started_at END
          WHERE id = ${binding.id} AND provider = 'INSTAGRAM'
            AND (instagram_operation_lease_until IS NULL OR instagram_operation_lease_until <= clock_timestamp())
            AND (instagram_last_subscription_attempt_at IS NULL OR instagram_last_subscription_attempt_at <= clock_timestamp() - interval '10 seconds')
          RETURNING id`;
        if (bindingClaim.length !== 1) throw new ConflictException({ code: 'OPERATION_IN_PROGRESS' });
        const updated = await tx.$queryRaw<Array<{ id: string }>>`UPDATE instagram_authorization_attempts
          SET operation_lease_token = ${lease}, operation_lease_until = clock_timestamp() + interval '60 seconds',
            operation_deadline_at = ${deadlineAt}, last_subscription_attempt_at = clock_timestamp(),
            subscription_requests = subscription_requests + 1, subscription_state = 'OBSERVING', updated_at = clock_timestamp()
          WHERE id = ${attemptId} AND status = 'MAPPED_PENDING_SUBSCRIPTION' AND channel_id = ${channelId}
            AND operation_lease_token IS NOT DISTINCT FROM ${attempt.operationLeaseToken}
            AND operation_lease_until IS NOT DISTINCT FROM ${attempt.operationLeaseUntil}
            AND subscription_requests < 3
            AND (last_subscription_attempt_at IS NULL OR last_subscription_attempt_at <= clock_timestamp() - interval '10 seconds')
            AND expires_at > clock_timestamp() AND ${deadlineAt} > clock_timestamp()
          RETURNING id`;
        if (updated.length !== 1) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        if (recordAdvance) await this.activity.registrar(tx, actor.mantenedoraId, 'instagram.autorizacao.avancada', this.auditActor(actor), { buId, entidadeId: attemptId });
        await this.assertSubscriptionTuple(tx, actor, attemptId, channelId, buId, generation, version, lease);
        this.assertSignedSession(actor);
      });
      this.assertSignedSession(actor);
      if (alreadySubscribed) {
        await this.actorTransaction(actor, async (tx) => {
          await this.requireActorTx(tx, actor, buId);
          await this.lockAttemptResource(tx, attemptId, channelId);
          await this.requireActorTx(tx, actor, buId);
          const changed = await tx.instagramAuthorizationAttempt.updateMany({ where: { id: attemptId, channelId, buId, userId: actor.id, sessionHash: hash(actor.sessionToken), status: 'MAPPED_PENDING_SUBSCRIPTION' }, data: {
            status: 'MAPPED_PENDING_RECEIPT', subscriptionState: 'SUBSCRIBED', operationLeaseToken: null, operationLeaseUntil: null, operationDeadlineAt: null,
          } });
          if (changed.count !== 1) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
          this.assertSignedSession(actor);
        });
        this.assertSignedSession(actor);
        return 'SUBSCRIBED';
      }
      if (mustObserve) {
        const observation = await this.providerCall(actor, attemptId, channelId, buId, generation, version, lease,
          () => this.http.subscribedFields(accountId, token, config, deadlineAt,
            () => this.assertBeforeSubscriptionRequest(actor, attemptId, channelId, buId, generation, version, accountId, lease)), deadlineAt,
          accountId);
        if (observation === RECEIPT_CONFIRMED) return 'SUBSCRIBED';
        if (observation === null) {
          const receipt = await this.actorTransaction(actor, async (tx) => {
            await this.requireActorTx(tx, actor, buId);
            await this.lockAttemptResource(tx, attemptId, channelId);
            await this.requireActorTx(tx, actor, buId);
            if (await this.assertSubscriptionTuple(tx, actor, attemptId, channelId, buId, generation, version, lease)) return true;
            const facts = await this.readSubscriptionClockFacts(tx, actor.id, attemptId, channelId, buId, generation, version, accountId, lease);
            await this.requireActorTx(tx, actor, buId);
            const written = await this.writeSubscriptionUncertain(tx, actor, attemptId, channelId, buId, generation, version, accountId, lease);
            if (!written) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
            this.assertSignedSession(actor);
            await this.assertFreshSubscriptionClock(tx, facts);
            return false;
          });
          this.assertSignedSession(actor);
          return receipt ? 'SUBSCRIBED' : 'UNCERTAIN';
        }
      } else {
        const dispatched = await this.providerCall(actor, attemptId, channelId, buId, generation, version, lease,
          async () => { await this.http.subscribeMessages(accountId, token, config, deadlineAt,
            () => this.assertBeforeSubscriptionRequest(actor, attemptId, channelId, buId, generation, version, accountId, lease)); return true; }, deadlineAt,
          accountId);
        if (!dispatched) return 'UNCERTAIN';
        if (dispatched === RECEIPT_CONFIRMED) return 'SUBSCRIBED';
      }
      const receiptAlreadyCommitted = await this.requireSubscriptionOrReceipt(actor, attemptId, channelId, buId, generation, version, lease);
      const completed = await this.actorTransaction(actor, async (tx) => {
        await this.requireActorTx(tx, actor, buId);
        await this.lockAttemptResource(tx, attemptId, channelId);
        if (await this.assertSubscriptionTuple(tx, actor, attemptId, channelId, buId, generation, version, lease)) return true;
        if (receiptAlreadyCommitted) return true;
        const facts = await this.readSubscriptionClockFacts(tx, actor.id, attemptId, channelId, buId, generation, version, accountId, lease);
        await this.requireActorTx(tx, actor, buId);
        const attemptUpdate = await tx.$queryRaw<Array<{ id: string }>>`UPDATE instagram_authorization_attempts SET status = 'MAPPED_PENDING_RECEIPT',
          subscription_state = 'SUBSCRIBED', operation_lease_token = NULL, operation_lease_until = NULL, operation_deadline_at = NULL,
          updated_at = clock_timestamp()
          WHERE id = ${attemptId} AND channel_id = ${channelId} AND bu_id = ${buId} AND user_id = ${actor.id}
            AND session_hash = ${hash(actor.sessionToken)} AND status = 'MAPPED_PENDING_SUBSCRIPTION'
            AND operation_lease_token = ${lease} AND operation_lease_until > clock_timestamp()
            AND operation_deadline_at > clock_timestamp() AND expires_at > clock_timestamp()
            AND EXISTS (SELECT 1 FROM channel_credentials cc WHERE cc.channel_id = ${channelId} AND cc.bu_id = ${buId}
              AND cc.provider = 'INSTAGRAM' AND cc.generation = ${generation} AND cc.version = ${version}
              AND (cc.expires_at IS NULL OR cc.expires_at > clock_timestamp() + interval '60 seconds'))
            AND EXISTS (SELECT 1 FROM provider_resource_identities pri WHERE pri.provider = 'INSTAGRAM'
              AND pri.external_resource_id = ${accountId} AND pri.bu_id = ${buId} AND pri.current_channel_id = ${channelId}
              AND pri.business_identity_id = (SELECT bc.business_identity_id FROM bu_channels bc WHERE bc.id = ${channelId})
              AND pri.retired_at IS NULL AND pri.instagram_operation_lease_token = ${lease}
              AND pri.instagram_operation_lease_until > clock_timestamp())
          RETURNING id`;
        const channelUpdate = await tx.buChannel.updateMany({ where: { id: channelId, buId, generation, type: 'INSTAGRAM' }, data: { providerConnectionState: 'SUBSCRIBED_PENDING_RECEIPT', status: 'CONECTANDO' } });
        if (attemptUpdate.length !== 1 || channelUpdate.count !== 1) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        this.assertSignedSession(actor);
        await this.assertFreshSubscriptionClock(tx, facts);
        return true;
      });
      this.assertSignedSession(actor);
      return completed ? 'SUBSCRIBED' : 'UNCERTAIN';
    } finally {
      await this.releaseBindingOperation(accountId, lease);
    }
  }

  private async providerCall<T>(actor: InstagramActor, attemptId: string, channelId: string, buId: string, generation: number, version: number, lease: string, call: () => Promise<T>, deadlineAt: Date, accountId: string): Promise<T | null | typeof RECEIPT_CONFIRMED> {
    if (await this.requireSubscriptionOrReceipt(actor, attemptId, channelId, buId, generation, version, lease)) {
      this.assertSignedSession(actor);
      return RECEIPT_CONFIRMED;
    }
    this.assertSignedSession(actor);
    if (deadlineAt.getTime() <= Date.now()) throw new ConflictException({ code: 'OPERATION_DEADLINE_EXCEEDED' });
    let value: T;
    try {
      value = await call();
    } catch {
      const receipt = await this.actorTransaction(actor, async (tx) => {
        await this.requireActorTx(tx, actor, buId);
        await this.lockAttemptResource(tx, attemptId, channelId);
        if (await this.assertSubscriptionTuple(tx, actor, attemptId, channelId, buId, generation, version, lease)) return true;
        const facts = await this.readSubscriptionClockFacts(tx, actor.id, attemptId, channelId, buId, generation, version, accountId, lease);
        await this.requireActorTx(tx, actor, buId);
        const written = await this.writeSubscriptionUncertain(tx, actor, attemptId, channelId, buId, generation, version, accountId, lease);
        if (!written) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        this.assertSignedSession(actor);
        await this.assertFreshSubscriptionClock(tx, facts);
        return false;
      });
      this.assertSignedSession(actor);
      return receipt ? RECEIPT_CONFIRMED : null;
    }
    // Provider success does not authorize a stale actor or lease. Keep this
    // revalidation outside the provider-error catch so a revoked grant or
    // replaced operation cannot be misreported as an uncertain provider call.
    const receipt = await this.requireSubscriptionOrReceipt(actor, attemptId, channelId, buId, generation, version, lease);
    this.assertSignedSession(actor);
    if (receipt) {
      this.assertSignedSession(actor);
      return RECEIPT_CONFIRMED;
    }
    return value;
  }

  private async assertBeforeSubscriptionRequest(actor: InstagramActor, attemptId: string, channelId: string, buId: string, generation: number, version: number, accountId: string, lease: string) {
    const facts = await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, buId);
      await this.lockAttemptResource(tx, attemptId, channelId);
      await this.requireActorTx(tx, actor, buId);
      const current = await this.assertSubscriptionTuple(tx, actor, attemptId, channelId, buId, generation, version, lease);
      if (current) throw new ConflictException({ code: 'SUBSCRIPTION_ALREADY_RECEIVED' });
      const currentFacts = await this.readSubscriptionClockFacts(tx, actor.id, attemptId, channelId, buId, generation, version, accountId, lease);
      this.assertSignedSession(actor);
      return currentFacts;
    });
    await this.assertFreshSubscriptionClock(this.prisma, facts);
    this.assertSignedSession(actor);
  }

  private async releaseBindingOperation(accountId: string, lease: string) {
    await this.prisma.$executeRaw`UPDATE provider_resource_identities
      SET instagram_operation_lease_token = NULL, instagram_operation_lease_until = NULL
      WHERE provider = 'INSTAGRAM' AND external_resource_id = ${accountId}
        AND instagram_operation_lease_token = ${lease}`;
  }

  private async assertFreshMappingClock(tx: Prisma.TransactionClient, attempt: { expiresAt: Date; operationDeadlineAt: Date | null; credentialExpiresAt: Date | null }) {
    const [clock] = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    const now = Math.max(clock.now.getTime(), Date.now());
    if (!attempt.operationDeadlineAt || now >= attempt.expiresAt.getTime()
      || now >= attempt.operationDeadlineAt.getTime()
      || !attempt.credentialExpiresAt || now + 60_000 >= attempt.credentialExpiresAt.getTime()) {
      throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
    }
  }

  private async readSubscriptionClockFacts(tx: Prisma.TransactionClient, userId: string, attemptId: string, channelId: string, buId: string,
    generation: number, version: number, accountId: string, lease: string): Promise<SubscriptionClockFacts> {
    const rows = await tx.$queryRaw<Array<{ operation_deadline_at: Date; expires_at: Date; credential_expires_at: Date | null; binding_lease_until: Date; attempt_lease_until: Date }>>`SELECT
      a.operation_deadline_at, a.expires_at, cc.expires_at AS credential_expires_at,
      pri.instagram_operation_lease_until AS binding_lease_until, a.operation_lease_until AS attempt_lease_until
      FROM instagram_authorization_attempts a
      JOIN bu_channels c ON c.id = a.channel_id AND c.id = ${channelId} AND c.bu_id = ${buId} AND c.generation = ${generation} AND c.type = 'INSTAGRAM'
      JOIN channel_credentials cc ON cc.channel_id = c.id AND cc.bu_id = ${buId} AND cc.provider = 'INSTAGRAM' AND cc.generation = ${generation} AND cc.version = ${version}
      JOIN provider_resource_identities pri ON pri.provider = 'INSTAGRAM' AND pri.external_resource_id = ${accountId}
        AND pri.bu_id = ${buId} AND pri.current_channel_id = c.id AND pri.business_identity_id = c.business_identity_id AND pri.retired_at IS NULL
      WHERE a.id = ${attemptId} AND a.channel_id = c.id AND a.bu_id = ${buId} AND a.user_id = ${userId}
        AND a.status = 'MAPPED_PENDING_SUBSCRIPTION' AND a.mapped_credential_version = ${version}
        AND a.operation_lease_token = ${lease} AND pri.instagram_operation_lease_token = ${lease}
      FOR UPDATE OF a, cc, pri`;
    const facts = rows[0];
    if (!facts || !facts.operation_deadline_at || !facts.attempt_lease_until || !facts.binding_lease_until) {
      throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
    }
    return { deadlineAt: facts.operation_deadline_at, attemptExpiresAt: facts.expires_at,
      credentialExpiresAt: facts.credential_expires_at, bindingLeaseUntil: facts.binding_lease_until,
      attemptLeaseUntil: facts.attempt_lease_until };
  }

  private async writeSubscriptionUncertain(tx: Prisma.TransactionClient, actor: InstagramActor, attemptId: string,
    channelId: string, buId: string, generation: number, version: number, accountId: string, lease: string) {
    const rows = await tx.$queryRaw<Array<{ id: string }>>`UPDATE instagram_authorization_attempts SET subscription_state = 'UNCERTAIN',
      operation_lease_token = NULL, operation_lease_until = NULL, operation_deadline_at = NULL, updated_at = clock_timestamp()
      WHERE id = ${attemptId} AND channel_id = ${channelId} AND bu_id = ${buId} AND user_id = ${actor.id}
        AND session_hash = ${hash(actor.sessionToken)} AND status = 'MAPPED_PENDING_SUBSCRIPTION'
        AND operation_lease_token = ${lease} AND operation_lease_until > clock_timestamp()
        AND operation_deadline_at > clock_timestamp() AND expires_at > clock_timestamp()
        AND EXISTS (SELECT 1 FROM channel_credentials cc WHERE cc.channel_id = ${channelId} AND cc.bu_id = ${buId}
          AND cc.provider = 'INSTAGRAM' AND cc.generation = ${generation} AND cc.version = ${version}
          AND (cc.expires_at IS NULL OR cc.expires_at > clock_timestamp() + interval '60 seconds'))
        AND EXISTS (SELECT 1 FROM provider_resource_identities pri JOIN bu_channels c ON c.id = pri.current_channel_id
          WHERE pri.provider = 'INSTAGRAM' AND pri.external_resource_id = ${accountId} AND pri.bu_id = ${buId}
            AND pri.current_channel_id = ${channelId} AND pri.business_identity_id = c.business_identity_id
            AND pri.retired_at IS NULL AND pri.instagram_operation_lease_token = ${lease}
            AND pri.instagram_operation_lease_until > clock_timestamp() AND c.generation = ${generation} AND c.type = 'INSTAGRAM')
      RETURNING id`;
    return rows.length === 1;
  }

  private async assertFreshSubscriptionClock(tx: Prisma.TransactionClient | PrismaService, facts: SubscriptionClockFacts) {
    const [clock] = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
    this.assertSubscriptionClockAt(facts, Math.max(clock.now.getTime(), Date.now()));
  }

  private assertSubscriptionClockAt(facts: SubscriptionClockFacts, now: number) {
    if (now >= facts.deadlineAt.getTime() || now >= facts.attemptExpiresAt.getTime()
      || now >= facts.bindingLeaseUntil.getTime() || now >= facts.attemptLeaseUntil.getTime()
      || (facts.credentialExpiresAt && now + 60_000 >= facts.credentialExpiresAt.getTime())) {
      throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
    }
  }

  private async requireSubscriptionOrReceipt(actor: InstagramActor, attemptId: string, channelId: string, buId: string, generation: number, version: number, lease: string) {
    const { result, facts } = await this.actorTransaction(actor, async (tx) => {
      await this.requireActorTx(tx, actor, buId);
      await this.lockAttemptResource(tx, attemptId, channelId);
      await this.requireActorTx(tx, actor, buId);
      const current = await this.assertSubscriptionTuple(tx, actor, attemptId, channelId, buId, generation, version, lease);
      let currentFacts: SubscriptionClockFacts | null = null;
      if (!current) {
        const attempt = await tx.instagramAuthorizationAttempt.findUnique({ where: { id: attemptId }, select: { professionalUserId: true } });
        if (!attempt?.professionalUserId) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
        currentFacts = await this.readSubscriptionClockFacts(tx, actor.id, attemptId, channelId, buId, generation, version, attempt.professionalUserId, lease);
      }
      this.assertSignedSession(actor);
      return { result: current, facts: currentFacts };
    });
    if (facts) {
      await this.assertFreshSubscriptionClock(this.prisma, facts);
      this.assertSignedSession(actor);
    }
    return result;
  }

  private async assertSubscriptionTuple(tx: Prisma.TransactionClient, actor: InstagramActor, attemptId: string, channelId: string, buId: string, generation: number, version: number, lease: string): Promise<boolean> {
    const attempt = await tx.instagramAuthorizationAttempt.findFirst({ where: { id: attemptId, channelId, buId, userId: actor.id, sessionHash: hash(actor.sessionToken) } });
    const channel = await tx.buChannel.findFirst({ where: { id: channelId, buId, generation, type: 'INSTAGRAM' }, select: { id: true, status: true, providerConnectionState: true, receiptVerifiedAt: true, businessIdentityId: true } });
    const credential = await tx.channelCredential.findFirst({ where: { channelId, buId, provider: 'INSTAGRAM', generation, version }, select: { channelId: true, expiresAt: true } });
    const identity = attempt?.professionalUserId && channel ? await tx.providerResourceIdentity.findFirst({ where: {
      provider: 'INSTAGRAM', externalResourceId: attempt.professionalUserId, buId, currentChannelId: channelId,
      businessIdentityId: channel.businessIdentityId, retiredAt: null,
    }, select: { id: true, instagramOperationLeaseToken: true, instagramOperationLeaseUntil: true } }) : null;
    if (!attempt || !channel || !credential || !identity) throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
    if (attempt.status === 'MAPPED_PENDING_SUBSCRIPTION' && attempt.operationLeaseToken === lease
      && attempt.operationLeaseUntil && attempt.operationDeadlineAt && channel.status === 'CONECTANDO'
      && identity.instagramOperationLeaseToken === lease && identity.instagramOperationLeaseUntil) {
      const [clock] = await tx.$queryRaw<Array<{ now: Date }>>`SELECT clock_timestamp() AS now`;
      const observedAt = Math.max(clock.now.getTime(), Date.now());
      if (attempt.expiresAt.getTime() <= observedAt || attempt.operationLeaseUntil.getTime() <= observedAt
        || attempt.operationDeadlineAt.getTime() <= observedAt || identity.instagramOperationLeaseUntil.getTime() <= observedAt) {
        throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
      }
      if (credential.expiresAt && credential.expiresAt.getTime() <= observedAt + 60_000) throw new ConflictException({ code: 'CREDENTIAL_EXPIRED' });
      return false;
    }
    if (attempt.status === 'MAPPED_PENDING_RECEIPT' && attempt.subscriptionState === 'SUBSCRIBED'
      && !attempt.operationLeaseToken && channel.status === 'CONECTADO'
      && ['SUBSCRIBED_PENDING_RECEIPT', 'SUBSCRIBED'].includes(channel.providerConnectionState)
      && channel.receiptVerifiedAt !== null) return true;
    throw new ConflictException({ code: 'SUBSCRIPTION_CONTEXT_STALE' });
  }

  private async assertMappedSubscriptionResult(tx: Prisma.TransactionClient, actor: InstagramActor, attemptId: string, channelId: string, buId: string, generation: number, version: number, accountId: string) {
    const [attempt, channel, credential, identity] = await Promise.all([
      tx.instagramAuthorizationAttempt.findFirst({ where: { id: attemptId, channelId, buId, userId: actor.id, sessionHash: hash(actor.sessionToken), status: 'MAPPED_PENDING_RECEIPT', subscriptionState: 'SUBSCRIBED', operationLeaseToken: null }, select: { id: true, mappedCredentialVersion: true } }),
      tx.buChannel.findFirst({ where: { id: channelId, buId, generation, type: 'INSTAGRAM', providerConnectionState: { in: ['SUBSCRIBED_PENDING_RECEIPT', 'SUBSCRIBED'] } }, select: { id: true, businessIdentityId: true, receiptVerifiedAt: true } }),
      tx.channelCredential.findFirst({ where: { channelId, buId, provider: 'INSTAGRAM', generation, version }, select: { expiresAt: true } }),
      tx.providerResourceIdentity.findFirst({ where: { provider: 'INSTAGRAM', externalResourceId: accountId, buId, currentChannelId: channelId, retiredAt: null }, select: { id: true, businessIdentityId: true } }),
    ]);
    if (!attempt || attempt.mappedCredentialVersion !== version || !channel || !credential || !identity || identity.businessIdentityId !== channel.businessIdentityId) return false;
    return Boolean(channel.receiptVerifiedAt || !credential.expiresAt || credential.expiresAt.getTime() > Date.now() + 60_000);
  }

  private async assertMappedUncertainResult(tx: Prisma.TransactionClient, actor: InstagramActor, attemptId: string, channelId: string, buId: string, generation: number, version: number, accountId: string) {
    const [attempt, channel, credential, identity] = await Promise.all([
      tx.instagramAuthorizationAttempt.findFirst({ where: { id: attemptId, channelId, buId, userId: actor.id, sessionHash: hash(actor.sessionToken), status: 'MAPPED_PENDING_SUBSCRIPTION', professionalUserId: accountId, subscriptionState: 'UNCERTAIN', operationLeaseToken: null }, select: { id: true, mappedCredentialVersion: true } }),
      tx.buChannel.findFirst({ where: { id: channelId, buId, generation, type: 'INSTAGRAM' }, select: { id: true, businessIdentityId: true } }),
      tx.channelCredential.findFirst({ where: { channelId, buId, provider: 'INSTAGRAM', generation, version }, select: { channelId: true } }),
      tx.providerResourceIdentity.findFirst({ where: { provider: 'INSTAGRAM', externalResourceId: accountId, buId, currentChannelId: channelId, retiredAt: null }, select: { id: true, businessIdentityId: true } }),
    ]);
    return Boolean(attempt && attempt.mappedCredentialVersion === version && channel && credential && identity && identity.businessIdentityId === channel.businessIdentityId);
  }

  private async revalidateCallbackOwner(actor: InstagramActor, attemptId: string, lease: string) {
    const sessionHash = hash(actor.sessionToken);
    await this.actorTransaction(actor, async (tx) => {
      const attempt = await tx.instagramAuthorizationAttempt.findUnique({ where: { id: attemptId }, select: { buId: true } });
      if (!attempt) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      await this.requireActorTx(tx, actor, attempt.buId);
      const rows = await tx.$queryRaw<Array<{ id: string }>>`SELECT id FROM instagram_authorization_attempts WHERE id = ${attemptId} AND status = 'EXCHANGING' AND callback_lease_token = ${lease} AND callback_lease_until > clock_timestamp() AND operation_deadline_at > clock_timestamp() AND expires_at > clock_timestamp() AND user_id = ${actor.id} AND session_hash = ${sessionHash} FOR SHARE`;
      if (rows.length !== 1) throw new ConflictException({ code: 'OAUTH_ATTEMPT_STALE' });
      await this.requireActorTx(tx, actor, attempt.buId);
      this.assertSignedSession(actor);
    });
    this.assertSignedSession(actor);
  }

  private async requireAttempt(actor: InstagramActor, id: string) {
    const attempt = await this.prisma.instagramAuthorizationAttempt.findFirst({ where: { id, mantenedoraId: actor.mantenedoraId } });
    if (!attempt) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    await this.requireAdmin(actor, attempt.buId);
    if (attempt.userId !== actor.id || attempt.sessionHash !== hash(actor.sessionToken)) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    return attempt;
  }

  private async lockMappedResource(tx: Prisma.TransactionClient, accountId?: string | null) {
    if (!accountId) return;
    await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtextextended(${'instagram-resource:' + accountId}, 0))::text AS locked`;
    await tx.$queryRaw`SELECT id FROM provider_resource_identities WHERE provider = 'INSTAGRAM' AND external_resource_id = ${accountId} FOR UPDATE`;
  }
  private async lockAttemptResource(tx: Prisma.TransactionClient, attemptId: string, channelId: string) {
    const attempt = await tx.instagramAuthorizationAttempt.findUnique({ where: { id: attemptId }, select: { professionalUserId: true } });
    await this.lockMappedResource(tx, attempt?.professionalUserId);
    await tx.$queryRaw`SELECT id FROM bu_channels WHERE id = ${channelId} FOR UPDATE`;
    await tx.$queryRaw`SELECT id FROM instagram_authorization_attempts WHERE id = ${attemptId} FOR UPDATE`;
  }

  private async requireAdmin(actor: InstagramActor, buId: string) { return exigirPapelNaBu(this.access, actor.id, buId, 'ADMIN'); }
  private auditActor(actor: InstagramActor) { return { id: actor.id, nome: actor.nome, email: actor.email, ip: actor.ip }; }
  private async requireActorTx(tx: Prisma.TransactionClient, actor: InstagramActor, buId: string) {
    const claims = this.sessions.verificar(actor.sessionToken);
    if (!claims || claims.uid !== actor.id) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    const users = await tx.$queryRaw<Array<{ mantenedora_id: string; status: string; password_changed_at: Date | null }>>`SELECT mantenedora_id, status, password_changed_at FROM app_users WHERE id = ${actor.id} FOR SHARE`;
    const user = users[0];
    if (!user || user.status !== 'ATIVO' || user.mantenedora_id !== actor.mantenedoraId
      || (user.password_changed_at && user.password_changed_at.getTime() > claims.iat)) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    const bu = await tx.businessUnit.findFirst({ where: { id: buId, mantenedoraId: actor.mantenedoraId, status: 'ATIVO' }, select: { id: true } });
    if (!bu) throw new NotFoundException({ code: 'NAO_ENCONTRADO' });
    const grants = await tx.$queryRaw<Array<{ role: string }>>`SELECT role::text AS role FROM user_bu_roles WHERE user_id = ${actor.id} AND bu_id = ${buId} FOR SHARE`;
    if (!grants.some(({ role }) => role === 'OWNER' || role === 'ADMIN')) throw new ForbiddenException({ code: 'ADMIN_REQUIRED' });
    const currentClaims = this.sessions.verificar(actor.sessionToken);
    if (!currentClaims || currentClaims.uid !== actor.id) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
  }
  private assertSignedSession(actor: InstagramActor) {
    const claims = this.sessions.verificar(actor.sessionToken);
    if (!claims || claims.uid !== actor.id) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
  }
  private async actorTransaction<T>(actor: InstagramActor, work: (tx: Prisma.TransactionClient) => Promise<T>): Promise<T> {
    const result = await this.prisma.$transaction(async (tx) => {
      const value = await work(tx);
      this.assertSignedSession(actor);
      return value;
    });
    this.assertSignedSession(actor);
    return result;
  }
  private async requireLiveActor(actor: InstagramActor, buId: string) {
    const claims = this.sessions.verificar(actor.sessionToken);
    if (!claims || claims.uid !== actor.id) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    const user = await this.prisma.appUser.findUnique({ where: { id: actor.id }, select: { mantenedoraId: true, status: true, passwordChangedAt: true } });
    if (!user || user.status !== 'ATIVO' || user.mantenedoraId !== actor.mantenedoraId
      || (user.passwordChangedAt && user.passwordChangedAt.getTime() > claims.iat)) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
    await this.requireAdmin(actor, buId);
    const currentClaims = this.sessions.verificar(actor.sessionToken);
    if (!currentClaims || currentClaims.uid !== actor.id) throw new UnauthorizedException({ code: 'NAO_AUTENTICADO' });
  }
  private stateFor(id: string, sessionHash: string, secret: string) { return `${id}.${createHmac('sha256', secret).update(`instagram-oauth-state\0${id}\0${sessionHash}`).digest('hex')}`; }
  private authorizationDto(attempt: { id: string; sessionHash: string; status: string; expiresAt: Date }, config: NonNullable<ReturnType<typeof instagramConfig>>) {
    if (attempt.status !== 'AUTHORIZATION_PENDING' || attempt.expiresAt <= new Date()) throw new ConflictException({ code: 'ATTEMPT_NOT_PENDING' });
    const state = this.stateFor(attempt.id, attempt.sessionHash, config.clientSecret);
    return { id: attempt.id, status: attempt.status, expiresAt: attempt.expiresAt.toISOString(), authorizationUrl: this.http.authorizationUrl({ clientId: config.clientId, redirectUri: config.redirectUri, state }) };
  }
}

function hash(value: string) { return createHash('sha256').update(value).digest('hex'); }
function safeEqual(a: string, b: string) { const x = Buffer.from(a); const y = Buffer.from(b); return x.length === y.length && timingSafeEqual(x, y); }

```

## Complete current source api-app/test/instagram-cp3-authorization-fences.e2e-spec.ts
```
import type { INestApplication } from '@nestjs/common';
import request from 'supertest';
import { createHmac, randomUUID } from 'node:crypto';
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from 'vitest';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { SessionService } from '../src/infra/session/session.service';
import { ChannelResolver } from '../src/domain/channels/transport/channel';
import {
  contratarCanalNaoOficial, criarCanalVerificado, criarMantenedora, evolutionFake, instagramFake,
  INSTAGRAM_WEBHOOK_SECRET, limparBanco, login, subirApp,
} from './helpers';

describe('CP3 current BFF authorization at the provider boundary (PostgreSQL)', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let buId = '';
  let ownerId = '';
  let cookie = '';
  let conversationId = '';
  let channelId = '';
  let generation = 1;

  beforeAll(async () => {
    ({ app, prisma } = await subirApp());
    await app.listen(0, '127.0.0.1');
  });

  beforeEach(async () => {
    await limparBanco(prisma);
    const tenant = await criarMantenedora(app, 'CP3 authorization fence', 'cp3-authorization@example.test');
    buId = tenant.businessUnit.id;
    ownerId = tenant.owner.id;
    await contratarCanalNaoOficial(prisma, tenant.mantenedora.id);
    const channel = await criarCanalVerificado(prisma, buId, 'NAO_OFICIAL', 'cp3-authorization-evolution', { requiresWindow: false });
    channelId = channel.channel.id;
    generation = channel.channel.generation;
    cookie = await login(app, 'cp3-authorization@example.test');
    const conversation = await request(app.getHttpServer()).post(`/api/bff/business-units/${buId}/conversations/open`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').send({ telefone: '+55 (11) 98765-4321' }).expect(201);
    conversationId = conversation.body.conversaId;
  });

  afterAll(async () => { if (prisma) await limparBanco(prisma); await app?.close(); });

  const holdFinalBoundary = () => {
    const resolver = app.get(ChannelResolver);
    const delegate = resolver.contextBeforeDispatch.bind(resolver);
    let reached!: () => void;
    let release!: () => void;
    const atBoundary = new Promise<void>((resolve) => { reached = resolve; });
    const held = new Promise<void>((resolve) => { release = resolve; });
    resolver.contextBeforeDispatch = async (context) => {
      const result = await delegate(context);
      reached();
      await held;
      return result;
    };
    return { atBoundary, release, restore: () => { resolver.contextBeforeDispatch = delegate; } };
  };

  const waitForFinalBoundary = async (atBoundary: Promise<void>, pending: Promise<unknown>) => Promise.race([
    atBoundary,
    pending.then(() => { throw new Error('Request completed before reaching the held final provider boundary.'); }),
  ]);

  const shortLivedSession = () => {
    const exp = Date.now() + 30_000;
    return { cookie: `lh_session=${app.get(SessionService).assinar(ownerId, exp - 24 * 60 * 60_000)}`, exp };
  };

  const createInstagramReplyFixture = async () => {
    const accountId = `synthetic-cp3-auth-${randomUUID()}`;
    instagramFake.meEnvelope = { user_id: accountId, username: 'fixture_auth_boundary' };
    const started = await request(app.getHttpServer()).post(`/api/bff/business-units/${buId}/instagram-authorizations`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').set('idempotency-key', randomUUID())
      .send({ operation: 'CONNECT' }).expect(201);
    const state = new URL(started.body.authorizationUrl).searchParams.get('state');
    expect(state).toBeTruthy();
    await request(app.getHttpServer()).get('/api/bff/instagram-authorizations/callback').set('Cookie', cookie)
      .query({ state, code: `synthetic-code-${accountId}` }).expect(303);
    await request(app.getHttpServer()).post(`/api/bff/instagram-authorizations/${started.body.id}/confirm`)
      .set('Cookie', cookie).set('x-requested-with', 'teste').set('idempotency-key', randomUUID()).send({}).expect(200);
    const event = JSON.stringify({ object: 'instagram', entry: [{ id: accountId, messaging: [{
      sender: { id: 'synthetic-auth-boundary-peer' }, recipient: { id: accountId }, timestamp: Date.now(),
      message: { mid: `synthetic-auth-boundary-${randomUUID()}`, text: 'Need a hand' },
    }] }] });
    const signature = `sha256=${createHmac('sha256', INSTAGRAM_WEBHOOK_SECRET).update(event).digest('hex')}`;
    await request(app.getHttpServer()).post('/webhooks/instagram').set('content-type', 'application/json')
      .set('x-hub-signature-256', signature).send(event).expect(200);
    const route = await prisma.conversationRoute.findFirstOrThrow({
      where: { buId, contactIdentity: { externalPeerId: 'synthetic-auth-boundary-peer' } }, include: { conversation: true },
    });
    const options = await request(app.getHttpServer()).get(`/api/bff/conversations/${route.conversationId}/reply-options`)
      .set('Cookie', cookie).expect(200);
    expect(options.body.options).toHaveLength(1);
    const option = options.body.options[0];
    const postBody = { texto: 'boundary reply', schemaVersion: 2, routeId: option.routeId, channelId: option.channelId,
      expectedGeneration: option.generation, contextFingerprint: option.contextFingerprint };
    return { conversationId: route.conversationId as string, postBody };
  };

  it('blocks an ordinary reply when the real grant is revoked after claim at the held final boundary', async () => {
    const fixture = await createInstagramReplyFixture();
    const fence = holdFinalBoundary();
    let pending: Promise<{ status: number; body: Record<string, unknown> }> | undefined;
    try {
      const before = instagramFake.calls.filter((call) => call.method === 'POST' && /\/messages$/.test(call.url)).length;
      pending = request(app.getHttpServer()).post(`/api/bff/conversations/${fixture.conversationId}/messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').send(fixture.postBody).then((response) => response);
      await waitForFinalBoundary(fence.atBoundary, pending);
      const admission = await prisma.dispatchAdmission.findFirstOrThrow({ where: { conversationId: fixture.conversationId, releasedAt: null } });
      expect(admission.dispatchDeadlineAt?.getTime()).toBeGreaterThan(Date.now());
      expect(await prisma.userBuRole.findUnique({ where: { userId_buId: { userId: ownerId, buId } } })).not.toBeNull();
      await prisma.userBuRole.delete({ where: { userId_buId: { userId: ownerId, buId } } });
      fence.release();
      const response = await pending;
      expect(response.status).toBe(409);
      expect(response.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
      expect(instagramFake.calls.filter((call) => call.method === 'POST' && /\/messages$/.test(call.url))).toHaveLength(before);
    } finally { fence.release(); await pending?.catch(() => undefined); fence.restore(); }
  });

  it('blocks an ordinary reply when the real signed session expires before its dispatch deadline', async () => {
    const fixture = await createInstagramReplyFixture();
    const short = shortLivedSession();
    const fence = holdFinalBoundary();
    let pending: Promise<{ status: number; body: Record<string, unknown> }> | undefined;
    try {
      const before = instagramFake.calls.filter((call) => call.method === 'POST' && /\/messages$/.test(call.url)).length;
      pending = request(app.getHttpServer()).post(`/api/bff/conversations/${fixture.conversationId}/messages`)
        .set('Cookie', short.cookie).set('x-requested-with', 'teste').send(fixture.postBody).then((response) => response);
      await waitForFinalBoundary(fence.atBoundary, pending);
      const admission = await prisma.dispatchAdmission.findFirstOrThrow({ where: { conversationId: fixture.conversationId, releasedAt: null } });
      expect(admission.expiresAt.getTime()).toBeGreaterThan(short.exp);
      expect(admission.dispatchDeadlineAt?.getTime()).toBeGreaterThan(short.exp);
      expect(await prisma.userBuRole.findUnique({ where: { userId_buId: { userId: ownerId, buId } } })).not.toBeNull();
      vi.useFakeTimers({ toFake: ['Date'] });
      vi.setSystemTime(new Date(short.exp + 1));
      fence.release();
      const response = await pending;
      vi.useRealTimers();
      expect(response.status).toBe(409);
      expect(response.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
      expect(instagramFake.calls.filter((call) => call.method === 'POST' && /\/messages$/.test(call.url))).toHaveLength(before);
    } finally { vi.useRealTimers(); fence.release(); await pending?.catch(() => undefined); fence.restore(); }
  });

  it('blocks initial dispatch when a real signed session expires after claim at the held final boundary', async () => {
    const fence = holdFinalBoundary();
    let pending: Promise<{ status: number; body: Record<string, unknown> }> | undefined;
    try {
      const base = `/api/bff/conversations/${conversationId}`;
      const message = { tipo: 'TEXTO', texto: 'initial authorization fence' };
      const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
      const short = shortLivedSession();
      const before = evolutionFake.enviados.length;
      pending = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', short.cookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'de18ba23-4e3a-4f2c-9d11-8bfe99848780')
        .send({ channelId, expectedGeneration: generation, mensagem: message, previewFingerprint: preview.body.previewFingerprint })
        .then((response) => response);
      await waitForFinalBoundary(fence.atBoundary, pending);
      const intent = await prisma.initialMessageIntent.findFirstOrThrow({ where: { conversationId, slotReleasedAt: null } });
      expect(intent.leaseExpiresAt.getTime()).toBeGreaterThan(short.exp);
      expect(intent.dispatchDeadlineAt?.getTime()).toBeGreaterThan(short.exp);
      expect(await prisma.userBuRole.findUnique({ where: { userId_buId: { userId: ownerId, buId } } })).not.toBeNull();
      vi.useFakeTimers({ toFake: ['Date'] });
      vi.setSystemTime(new Date(short.exp + 1));
      fence.release();
      const response = await pending;
      vi.useRealTimers();
      expect(response.status).toBe(409);
      expect(response.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
      expect(evolutionFake.enviados).toHaveLength(before);
    } finally { vi.useRealTimers(); fence.release(); await pending?.catch(() => undefined); fence.restore(); }
  });

  it('blocks initial dispatch when the real grant is revoked after claim at the held final boundary', async () => {
    const fence = holdFinalBoundary();
    let pending: Promise<{ status: number; body: Record<string, unknown> }> | undefined;
    try {
      const base = `/api/bff/conversations/${conversationId}`;
      const message = { tipo: 'TEXTO', texto: 'initial grant fence' };
      const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
      const before = evolutionFake.enviados.length;
      pending = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'de18ba23-4e3a-4f2c-9d11-8bfe99848782')
        .send({ channelId, expectedGeneration: generation, mensagem: message, previewFingerprint: preview.body.previewFingerprint })
        .then((response) => response);
      await waitForFinalBoundary(fence.atBoundary, pending);
      const intent = await prisma.initialMessageIntent.findFirstOrThrow({ where: { conversationId, slotReleasedAt: null } });
      expect(intent.leaseExpiresAt.getTime()).toBeGreaterThan(Date.now());
      expect(intent.dispatchDeadlineAt?.getTime()).toBeGreaterThan(Date.now());
      expect(await prisma.userBuRole.findUnique({ where: { userId_buId: { userId: ownerId, buId } } })).not.toBeNull();
      await prisma.userBuRole.delete({ where: { userId_buId: { userId: ownerId, buId } } });
      fence.release();
      const response = await pending;
      expect(response.status).toBe(409);
      expect(response.body).toMatchObject({ code: 'CHANNEL_CONTEXT_CHANGED', outcome: 'BLOCKED' });
      expect(evolutionFake.enviados).toHaveLength(before);
    } finally { fence.release(); await pending?.catch(() => undefined); fence.restore(); }
  });

  it('keeps the matched live-grant control eligible through the same held boundary', async () => {
    const fixture = await createInstagramReplyFixture();
    const fence = holdFinalBoundary();
    let pending: Promise<{ status: number; body: Record<string, unknown> }> | undefined;
    try {
      const before = instagramFake.calls.filter((call) => call.method === 'POST' && /\/messages$/.test(call.url)).length;
      pending = request(app.getHttpServer()).post(`/api/bff/conversations/${fixture.conversationId}/messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').send(fixture.postBody).then((response) => response);
      await waitForFinalBoundary(fence.atBoundary, pending);
      fence.release();
      expect((await pending).status).toBe(201);
      expect(instagramFake.calls.filter((call) => call.method === 'POST' && /\/messages$/.test(call.url))).toHaveLength(before + 1);
    } finally { fence.release(); await pending?.catch(() => undefined); fence.restore(); }
  });

  it('keeps the matched live-session control eligible for an initial send through the held boundary', async () => {
    const fence = holdFinalBoundary();
    let pending: Promise<{ status: number; body: Record<string, unknown> }> | undefined;
    try {
      const base = `/api/bff/conversations/${conversationId}`;
      const message = { tipo: 'TEXTO', texto: 'matched initial live control' };
      const preview = await request(app.getHttpServer()).post(`${base}/initial-message-preview`)
        .set('Cookie', cookie).set('x-requested-with', 'teste')
        .send({ channelId, expectedGeneration: generation, mensagem: message }).expect(200);
      const before = evolutionFake.enviados.length;
      pending = request(app.getHttpServer()).post(`${base}/initial-messages`)
        .set('Cookie', cookie).set('x-requested-with', 'teste').set('Idempotency-Key', 'de18ba23-4e3a-4f2c-9d11-8bfe99848781')
        .send({ channelId, expectedGeneration: generation, mensagem: message, previewFingerprint: preview.body.previewFingerprint })
        .then((response) => response);
      await waitForFinalBoundary(fence.atBoundary, pending);
      fence.release();
      expect((await pending).status).toBe(201);
      expect(evolutionFake.enviados).toHaveLength(before + 1);
    } finally { fence.release(); await pending?.catch(() => undefined); fence.restore(); }
  });
});

```

## Complete current source api-app/test/helpers.ts
```
import { INestApplication } from '@nestjs/common';
import { Test } from '@nestjs/testing';
import type { NestExpressApplication } from '@nestjs/platform-express';
import request from 'supertest';
import { AppModule } from '../src/app.module';
import { ChannelAdapterRegistry } from '../src/integrations/channels/channel-adapter-registry';
import { configurarBodyParsers } from '../src/infra/http/body-parsers';
import { PrismaService } from '../src/infra/prisma/prisma.service';
import { EVOLUTION_CLIENT, EvolutionClient } from '../src/integrations/evolution/evolution.client';
import { META_CLIENT, MetaClient, MetaIndisponivelError } from '../src/integrations/meta/meta.client';
import { TYPEBOT_CLIENT, TypebotClient } from '../src/integrations/typebot/typebot.client';
import { sealChannelCredential } from '../src/domain/channels/channel-credential-crypto';
import type { Prisma } from '@prisma/client';
import { randomUUID } from 'node:crypto';
import { normalizeWhatsAppPersonPeer, resolveOrCreateContactIdentity, whatsappPeerAddress } from '../src/domain/inbox/contact-identity';
import { INSTAGRAM_HTTP_FETCH } from '../src/integrations/instagram/instagram-http.client';

/** Explicit synthetic WhatsApp conversation fixture with its canonical BU-local peer. */
export async function criarConversaFixture(
  prisma: PrismaService,
  data: Omit<Prisma.ConversationUncheckedCreateInput, 'contactId'>,
) {
  return prisma.$transaction(async (tx) => {
    const peer = await resolveOrCreateContactIdentity(tx, whatsappPeerAddress({
      buId: data.buId,
      externalPeerId: data.contact,
      contactType: data.contactType ?? 'PESSOA',
      displayName: data.displayName,
    }));
    return tx.conversation.create({ data: { ...data, contactId: peer.contactId } });
  });
}

/** Explicit route for manually seeded conversations; callers must name both endpoints. */
export async function criarRotaConversaFixture(
  prisma: PrismaService,
  input: { conversationId: string; channelId: string },
) {
  return prisma.$transaction(async (tx) => {
    const conversation = await tx.conversation.findUnique({ where: { id: input.conversationId }, include: { localContact: { include: { identities: true } } } });
    const channel = await tx.buChannel.findUnique({ where: { id: input.channelId }, include: { businessIdentity: true, providerIdentities: true } });
    if (!conversation || !channel || conversation.buId !== channel.buId || !channel.businessIdentityId || !channel.businessIdentity
      || channel.type === 'INSTAGRAM' || channel.businessIdentity.buId !== conversation.buId
      || channel.businessIdentity.platform !== 'WHATSAPP' || channel.businessIdentity.namespace !== 'WHATSAPP_RESOURCE'
      || channel.businessIdentity.scopeReference !== 'BU' || channel.status !== 'CONECTADO'
      || !channel.ownNumberVerified || channel.verifiedEpoch !== channel.pairingEpoch) {
      throw new Error('Explicit route fixture requires a current, verified same-BU channel and business identity.');
    }
    const peerAddress = whatsappPeerAddress({ buId: conversation.buId, externalPeerId: conversation.contact,
      contactType: conversation.contactType, displayName: conversation.displayName });
    if (peerAddress.externalPeerId !== (conversation.contactType === 'PESSOA' ? normalizeWhatsAppPersonPeer(conversation.contact) : conversation.contact.trim())) {
      throw new Error('Explicit route fixture requires a canonical WhatsApp peer.');
    }
    const identities = conversation.localContact.identities.filter((item) => item.buId === conversation.buId
      && item.contactId === conversation.contactId && item.platform === 'WHATSAPP'
      && item.namespace === peerAddress.namespace && item.scopeReference === 'BU'
      && item.externalPeerId === peerAddress.externalPeerId);
    if (identities.length !== 1) throw new Error('Explicit route fixture requires exactly one canonical WhatsApp peer identity.');
    const identity = identities[0];
    const expectedResourceId = channel.type === 'OFICIAL' ? channel.phoneNumberId : channel.evolutionInstanceName;
    const currentResources = channel.providerIdentities.filter((resource) => resource.currentChannelId === channel.id
      && resource.buId === conversation.buId && resource.businessIdentityId === channel.businessIdentityId
      && resource.provider === channel.type && resource.externalResourceId === expectedResourceId
      && resource.managedLifecycle && resource.retiredAt === null && resource.cleanupState === 'ACTIVE');
    if (!expectedResourceId || currentResources.length !== 1) {
      throw new Error('Explicit route fixture requires exactly one current matching provider resource.');
    }
    return tx.conversationRoute.create({ data: {
      buId: conversation.buId, conversationId: conversation.id, contactId: identity.contactId,
      contactIdentityId: identity.id, platform: 'WHATSAPP', contactScopeReference: identity.scopeReference,
      businessScopeReference: channel.businessIdentity.scopeReference, businessIdentityId: channel.businessIdentity.id,
    } });
  });
}

/** Fetches the native V2 route tuple for one explicitly selected channel. */
export async function obterSelecaoRespostaV2(app: INestApplication, conversationId: string, cookie: string, channelId: string) {
  const response = await request(app.getHttpServer()).get(`/api/bff/conversations/${conversationId}/reply-options`)
    .set('Cookie', cookie).expect(200);
  if (response.body.schemaVersion !== 2 || !Array.isArray(response.body.options)) throw new Error('Unexpected V2 reply-options response.');
  const matches = response.body.options.filter((option: Record<string, unknown>) => option.channelId === channelId);
  if (matches.length !== 1) throw new Error(`Expected one V2 reply option for selected channel ${channelId}; found ${matches.length}.`);
  const option = matches[0];
  if (option.schemaVersion !== 2 || typeof option.routeId !== 'string' || typeof option.channelId !== 'string'
    || typeof option.generation !== 'number' || !Number.isSafeInteger(option.generation)
    || typeof option.contextFingerprint !== 'string' || !/^[a-f0-9]{64}$/i.test(option.contextFingerprint)) {
    throw new Error('Selected reply option is missing its complete V2 route context.');
  }
  return { schemaVersion: 2, routeId: option.routeId, channelId: option.channelId,
    expectedGeneration: option.generation, contextFingerprint: option.contextFingerprint };
}

/** Explicit bulk fixture path for PostgreSQL query-bound tests with synthetic histories. */
export async function criarConversasFixtureEmLote(
  prisma: PrismaService,
  rows: readonly Omit<Prisma.ConversationUncheckedCreateInput, 'contactId'>[],
) {
  const prepared = rows.map((row) => {
    const id = row.id ?? randomUUID();
    const contactId = randomUUID();
    const address = whatsappPeerAddress({
      buId: row.buId,
      externalPeerId: row.contact,
      contactType: row.contactType ?? 'PESSOA',
      displayName: row.displayName,
    });
    return { row: { ...row, id }, contactId, identityId: randomUUID(), address };
  });
  const chunkSize = 750;
  for (let offset = 0; offset < prepared.length; offset += chunkSize) {
    const chunk = prepared.slice(offset, offset + chunkSize);
    await prisma.$transaction(async (tx) => {
      await tx.contact.createMany({ data: chunk.map(({ row, contactId }) => ({
        id: contactId, buId: row.buId, displayName: row.displayName ?? null,
      })) });
      await tx.contactIdentity.createMany({ data: chunk.map(({ row, contactId, identityId, address }) => ({
        id: identityId, buId: row.buId, contactId, platform: address.platform,
        namespace: address.namespace, scopeReference: address.scopeReference, externalPeerId: address.externalPeerId,
      })) });
      await tx.conversation.createMany({ data: chunk.map(({ row, contactId }) => ({ ...row, contactId })) });
    });
  }
  return prepared.map(({ row }) => row);
}

/** Dublês das portas de saída: o teste prova permissão, não a Meta. */
export const metaFake: MetaClient & { wabaRecusada: string | null; wabaRecursos: { wabaId: string; phoneNumberId: string; telefone: string }[]; enviados: { para: string; texto: string }[]; credentialByPhone: Map<string, string>; credentialCalls: { phoneNumberId: string; accessToken: string }[]; registrosNumero: number; subscriptionHook: (() => Promise<void>) | null; confirmHook: (() => Promise<void>) | null; registrosHook: (() => Promise<void>) | null; sendHook: ((id: string, para: string, texto: string) => Promise<void>) | null; confirmCalls: number; exchangeCalls: number; exchangeFails: number; providerCalls: number; sendIdNull: boolean } = {
  wabaRecusada: null,
  wabaRecursos: [
    { wabaId: '123456789', phoneNumberId: '111111111', telefone: '5584998880000' },
    { wabaId: '123456789', phoneNumberId: '987654321', telefone: '5584999990000' },
    { wabaId: '555555555', phoneNumberId: '222222222', telefone: '5584997770000' },
  ],
  enviados: [],
  credentialByPhone: new Map(),
  credentialCalls: [],
  registrosNumero: 0,
  subscriptionHook: null,
  confirmHook: null,
  registrosHook: null,
  sendHook: null,
  confirmCalls: 0,
  exchangeCalls: 0,
  exchangeFails: 0,
  providerCalls: 0,
  sendIdNull: false,
  capabilities: () => ({ appId: 'fixture-app', configId: 'fixture-config', graphVersion: 'v26.0', available: true, reason: 'AVAILABLE' }),
  async exchangeCode() {
    metaFake.providerCalls += 1; metaFake.exchangeCalls += 1;
    if (metaFake.exchangeFails > 0) { metaFake.exchangeFails -= 1; throw new Error('fixture exchange response lost'); }
    return { accessToken: 'fixture-scoped-token' };
  },
  async recursos(accessToken, wabaId, after) {
    metaFake.providerCalls += 1;
    if (accessToken !== 'fixture-scoped-token') throw new Error('scoped credential required');
    if (wabaId && metaFake.wabaRecusada === wabaId) throw new Error('WABA recusada');
    const targets = metaFake.wabaRecursos.filter((r) => !wabaId || r.wabaId === wabaId);
    const page = after ? targets.slice(1) : targets.slice(0, 1);
    return { wabas: wabaId ? [{ id: wabaId, name: 'Fixture' }] : [...new Map(targets.map((r) => [r.wabaId, { id: r.wabaId, name: 'Fixture' }])).values()], numbers: page.map((r) => ({ id: r.phoneNumberId, telefone: r.telefone, nomeVerificado: 'Fixture' })), next: !after && targets.length > 1 ? 'fixture-page-1' : null };
  },
  async enviarTexto(phoneNumberId: string, para: string, texto: string, accessToken?: string) {
    metaFake.providerCalls += 1;
    metaFake.credentialCalls.push({ phoneNumberId, accessToken: accessToken ?? '' });
    const expected = metaFake.credentialByPhone.get(phoneNumberId) ?? 'fixture-scoped-token';
    if (accessToken !== expected) throw new Error('scoped credential required');
    metaFake.enviados.push({ para, texto });
    const id = `wamid-enviado-${metaFake.enviados.length}`;
    await metaFake.sendHook?.(id, para, texto);
    return metaFake.sendIdNull
      ? { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'META_RECUSOU' }
      : { outcome: 'ACCEPTED', externalMessageId: id };
  },
  configurado: () => true,
  canSendText: () => true,
  async numerosDaWaba(wabaId: string, accessToken?: string, after?: string) {
    metaFake.providerCalls += 1;
    if (metaFake.wabaRecusada === wabaId || accessToken !== 'fixture-scoped-token') throw new Error('WABA recusada');
    const targets = metaFake.wabaRecursos.filter((r) => r.wabaId === wabaId); const page = after ? targets.slice(1) : targets.slice(0, 1);
    return { data: page.map((r) => ({ id: r.phoneNumberId, telefone: r.telefone, nomeVerificado: `WABA ${wabaId}` })), next: !after && targets.length > 1 ? 'fixture-page-1' : null };
  },
  async confirmarNumero(wabaId, phoneNumberId, accessToken, after) {
    metaFake.providerCalls += 1;
    metaFake.confirmCalls += 1;
    await metaFake.confirmHook?.();
    const page = await metaFake.numerosDaWaba(wabaId, accessToken, after);
    return page.data.find((item) => item.id === phoneNumberId) ?? null;
  },
  async verificarNumeroVinculado(wabaId, phoneNumberId, accessToken) {
    metaFake.confirmCalls += 1;
    await metaFake.confirmHook?.();
    const seen = new Set<string>(); let after: string | undefined;
    for (let index = 0; index < 2; index += 1) {
      const page = await metaFake.numerosDaWaba(wabaId, accessToken, after);
      const number = page.data.find((item) => item.id === phoneNumberId);
      if (number) return number;
      if (!page.next) return null;
      if (page.next.length > 512 || seen.has(page.next) || index === 1) throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
      seen.add(page.next); after = page.next;
    }
    throw new MetaIndisponivelError('A verificação do número está inconclusiva.');
  },
  async registrarNumero(_phoneNumberId, pin, accessToken) { metaFake.providerCalls += 1; if (accessToken !== 'fixture-scoped-token' || !/^\d{6}$/.test(pin)) throw new Error('scoped registration credential required'); metaFake.registrosNumero += 1; await metaFake.registrosHook?.(); },
  async inscreverWaba(_wabaId, accessToken) { metaFake.providerCalls += 1; if (accessToken !== 'fixture-scoped-token') throw new Error('scoped subscription credential required'); await metaFake.subscriptionHook?.(); },
};

export const evolutionFake: EvolutionClient & { enviados: { para: string; texto: string }[]; inventory: Map<string, { name: string; ownerJid: string | null; connectionStatus: string | null }>; createCalls: number; providerCalls: number; sendIdNull: boolean; sendHook: ((id: string, para: string, texto: string) => Promise<void>) | null; createHook: ((name: string) => Promise<void>) | null; ownerPhone: string | null; createdState: string; deleteFails: boolean } = {
  enviados: [], inventory: new Map(), createCalls: 0, providerCalls: 0,
  sendHook: null,
  createHook: null,
  configurado: () => true,
  async enviarTexto(_instancia: string, para: string, texto: string) {
    evolutionFake.providerCalls += 1;
    evolutionFake.enviados.push({ para, texto });
    const id = `evo-enviado-${evolutionFake.enviados.length}`;
    await evolutionFake.sendHook?.(id, para, texto);
    return evolutionFake.sendIdNull
      ? { outcome: 'UNKNOWN', evidence: 'ACK_WITHOUT_ID', legacyCode: 'EVOLUTION_RECUSOU' }
      : { outcome: 'ACCEPTED', externalMessageId: id };
  },
  async criarInstancia(nome) {
    evolutionFake.providerCalls += 1;
    evolutionFake.createCalls += 1;
    evolutionFake.inventory.set(nome, { name: nome, ownerJid: evolutionFake.ownerPhone ? `${evolutionFake.ownerPhone}@s.whatsapp.net` : null, connectionStatus: evolutionFake.createdState });
    await evolutionFake.createHook?.(nome);
    return { qrcode: 'data:image/png;base64,QR' };
  },
  async qrDaInstancia() {
    evolutionFake.providerCalls += 1;
    return 'data:image/png;base64,QR';
  },
  async estadoDaInstancia() {
    evolutionFake.providerCalls += 1;
    return 'open';
  },
  async consultarInstancia(nome) { evolutionFake.providerCalls += 1; return evolutionFake.inventory.get(nome) ?? null; },
  async apagarInstancia(nome) { evolutionFake.providerCalls += 1; if (evolutionFake.deleteFails) throw new Error('fixture cleanup timeout'); evolutionFake.inventory.delete(nome); },
};

/**
 * Liga o canal não oficial nos DOIS níveis: o teto da instalação (env, lido no
 * boot do serviço) e o contrato da Mantenedora (banco) — ADR-0016.
 *
 * Precisa vir ANTES de `subirApp`, porque o teto é lido uma vez na construção.
 * É o mesmo que acontece em produção: mudar módulo de instalação é deploy.
 */
export function tetoComCanalNaoOficial(): void {
  process.env.LH_CHANNEL_UNOFFICIAL = 'true';
}

export async function contratarCanalNaoOficial(prisma: PrismaService, mantenedoraId: string): Promise<void> {
  await prisma.mantenedoraSettings.upsert({
    where: { mantenedoraId },
    create: { mantenedoraId, modulos: { canalNaoOficial: true } },
    update: { modulos: { canalNaoOficial: true } },
  });
}

export const TOKEN_INTERNO = 'token-interno-de-teste';
export const META_APP_SECRET = 'segredo-do-app-meta';
export const INSTAGRAM_WEBHOOK_SECRET = 'fixture-instagram-webhook-app-secret';
export const instagramFake = {
  calls: [] as { url: string; method: string; redirect?: RequestRedirect; signal: AbortSignal | null }[],
  messages: [] as { accountId: string; recipientId: string; text: string }[],
  sendEnvelope: null as unknown,
  subscribed: false, failNext: false, redirectNext: false,
  shortEnvelope: null as unknown, longEnvelope: null as unknown, meEnvelope: null as unknown,
  subscribedEnvelope: null as unknown, subscribeEnvelope: null as unknown, failAfterSubscription: false,
  afterRequestHook: null as ((method: string, url: URL) => Promise<void>) | null, longTokenIssuedAt: null as number | null,
};
const instagramFetch: typeof fetch = async (input, init) => {
  const url = new URL(typeof input === 'string' || input instanceof URL ? input.toString() : input.url);
  const method = init?.method ?? 'GET';
  if (!['www.instagram.com', 'api.instagram.com', 'graph.instagram.com'].includes(url.hostname)) throw new Error('fixture rejected non-Instagram host');
  const signal = init?.signal ?? null;
  if (signal?.aborted) throw signal.reason ?? new Error('synthetic Instagram request aborted');
  instagramFake.calls.push({ url: `${url.origin}${url.pathname}`, method, redirect: init?.redirect, signal });
  if (instagramFake.failNext) { instagramFake.failNext = false; throw new Error('synthetic Instagram HTTP timeout'); }
  if (instagramFake.redirectNext) {
    instagramFake.redirectNext = false;
    return new Response(null, { status: 302, headers: { location: 'https://attacker.test/collect' } });
  }
  let body: Record<string, unknown>;
  if (url.hostname === 'api.instagram.com' && url.pathname === '/oauth/access_token' && method === 'POST') {
    body = (instagramFake.shortEnvelope ?? { data: [{ access_token: 'synthetic-short-token', user_id: 'synthetic-app-scoped-authref', permissions: 'instagram_business_basic,instagram_business_manage_messages' }] }) as Record<string, unknown>;
  } else if (url.hostname === 'graph.instagram.com' && url.pathname === '/access_token') {
    instagramFake.longTokenIssuedAt = Date.now();
    body = (instagramFake.longEnvelope ?? { access_token: 'synthetic-long-lived-token', expires_in: 7200 }) as Record<string, unknown>;
  } else if (url.hostname === 'graph.instagram.com' && url.pathname === '/v26.0/me') {
    body = (instagramFake.meEnvelope ?? { user_id: 'synthetic-professional-ig-id', username: 'fixture_professional' }) as Record<string, unknown>;
  } else if (url.hostname === 'graph.instagram.com' && url.pathname.endsWith('/subscribed_apps') && method === 'GET') {
    const accountId = decodeURIComponent(url.pathname.split('/').at(-2) ?? '');
    body = (instagramFake.subscribedEnvelope ?? { data: instagramFake.subscribed ? [{ id: accountId, subscribed_fields: ['messages'] }] : [] }) as Record<string, unknown>;
  } else if (url.hostname === 'graph.instagram.com' && url.pathname.endsWith('/subscribed_apps') && method === 'POST') {
    instagramFake.subscribed = true;
    if (instagramFake.failAfterSubscription) { instagramFake.failAfterSubscription = false; throw new Error('synthetic timeout after remote subscription'); }
    body = (instagramFake.subscribeEnvelope ?? { success: true }) as Record<string, unknown>;
  } else if (url.hostname === 'graph.instagram.com' && /^\/v26\.0\/[A-Za-z0-9_-]+\/messages$/.test(url.pathname) && method === 'POST') {
    if (url.origin !== 'https://graph.instagram.com' || url.search || init?.headers === undefined) throw new Error('fixture rejected Instagram message request metadata');
    let requestBody: unknown;
    try { requestBody = JSON.parse(String(init.body ?? '')); } catch { throw new Error('fixture rejected malformed Instagram message JSON'); }
    if (!requestBody || typeof requestBody !== 'object' || Array.isArray(requestBody)) throw new Error('fixture rejected Instagram message body');
    const envelope = requestBody as Record<string, unknown>;
    if (Object.keys(envelope).sort().join(',') !== 'message,recipient' || !envelope.recipient || typeof envelope.recipient !== 'object'
      || Array.isArray(envelope.recipient) || !envelope.message || typeof envelope.message !== 'object' || Array.isArray(envelope.message)) {
      throw new Error('fixture rejected unsupported Instagram message shape');
    }
    const recipient = envelope.recipient as Record<string, unknown>;
    const message = envelope.message as Record<string, unknown>;
    if (Object.keys(recipient).sort().join(',') !== 'id' || typeof recipient.id !== 'string'
      || Object.keys(message).sort().join(',') !== 'text' || typeof message.text !== 'string' || message.text.length === 0) {
      throw new Error('fixture rejected unsupported Instagram message fields');
    }
    const accountId = decodeURIComponent(url.pathname.split('/').at(-2)!);
    instagramFake.messages.push({ accountId, recipientId: recipient.id, text: message.text });
    body = (instagramFake.sendEnvelope ?? { recipient_id: recipient.id, message_id: `synthetic-ig-message-${instagramFake.messages.length}` }) as Record<string, unknown>;
  } else throw new Error(`fixture rejected unlisted Instagram endpoint ${method} ${url.origin}${url.pathname}`);
  const hook = instagramFake.afterRequestHook?.(method, url);
  if (hook && signal) {
    let onAbort: (() => void) | undefined;
    try {
      await Promise.race([hook, new Promise<never>((_, reject) => {
        onAbort = () => reject(signal.reason ?? new Error('synthetic Instagram request aborted'));
        signal.addEventListener('abort', onAbort, { once: true });
      })]);
    } finally {
      if (onAbort) signal.removeEventListener('abort', onAbort);
    }
  } else await hook;
  return new Response(JSON.stringify(body), { status: 200, headers: { 'content-type': 'application/json' } });
};
export const EVOLUTION_WEBHOOK_SECRET = 'fixture-evolution-secret-header';
export const typebotFake: TypebotClient & { enabled: boolean; starts: number; continues: number; startedBots: Array<{ botId: string; contact: string; text: string }>; beforeReply: (() => Promise<void>) | null } = {
  enabled: false, starts: 0, continues: 0, startedBots: [], beforeReply: null,
  configurado() { return typebotFake.enabled; }, async listarBots() { return []; }, editorUrl(id) { return `https://typebot.invalid/${id}`; }, workspaceUrl() { return 'https://typebot.invalid'; },
  async iniciar(botId, contact, text) { typebotFake.starts += 1; typebotFake.startedBots.push({ botId, contact, text }); await typebotFake.beforeReply?.(); return { sessionId: `fixture-typebot-${typebotFake.starts}`, messages: [{ type: 'text', content: { text: 'resposta do bot' } }] }; },
  async continuar() { typebotFake.continues += 1; return { messages: [] }; },
};

export async function subirApp(registryOverride?: ChannelAdapterRegistry, captureQueries = false): Promise<{ app: INestApplication; prisma: PrismaService }> {
  process.env.SESSION_SECRET ||= 'segredo-de-teste';
  process.env.INTERNAL_SERVICE_TOKEN = TOKEN_INTERNO;
  process.env.META_APP_ID = 'fixture-app';
  process.env.META_APP_SECRET = META_APP_SECRET;
  process.env.META_SIGNUP_CONFIG_ID = 'fixture-config';
  process.env.GRAPH_VERSION = 'v26.0';
  process.env.EVOLUTION_WEBHOOK_SECRET = EVOLUTION_WEBHOOK_SECRET;
  process.env.EVOLUTION_WEBHOOK_URL = 'https://api.example.test/webhooks/evolution';
  process.env.WEBHOOK_VERIFY_TOKEN = 'verify-token-de-teste';
  process.env.CHANNEL_CREDENTIAL_KEY_ID = 'fixture-key-v1';
  process.env.CHANNEL_CREDENTIAL_KEY = Buffer.alloc(32, 17).toString('base64');
  process.env.INSTAGRAM_CLIENT_ID = 'synthetic-instagram-client-id';
  process.env.INSTAGRAM_CLIENT_SECRET = 'synthetic-instagram-client-secret';
  process.env.INSTAGRAM_REDIRECT_URI = 'https://api.example.test/api/bff/instagram-authorizations/callback';
  process.env.INSTAGRAM_API_VERSION = 'v26.0';
  process.env.INSTAGRAM_WEBHOOK_APP_SECRET = INSTAGRAM_WEBHOOK_SECRET;
  process.env.INSTAGRAM_WEBHOOK_VERIFY_TOKEN = 'synthetic-instagram-verify-token';

  const testingModule = Test.createTestingModule({ imports: [AppModule] })
    .overrideProvider(META_CLIENT)
    .useValue(metaFake)
    .overrideProvider(EVOLUTION_CLIENT)
    .useValue(evolutionFake)
    .overrideProvider(TYPEBOT_CLIENT)
    .useValue(typebotFake)
    .overrideProvider(INSTAGRAM_HTTP_FETCH)
    .useValue(instagramFetch);
  if (captureQueries) {
    testingModule.overrideProvider(PrismaService).useValue(new PrismaService({ log: [{ emit: 'event', level: 'query' }] }));
  }
  if (registryOverride) testingModule.overrideProvider(ChannelAdapterRegistry).useValue(registryOverride);
  const moduleRef = await testingModule.compile();
  // A MESMA fiação de produção: sem isto o corpo bruto não existe e o teste de
  // assinatura passaria a provar outra coisa.
  const app = moduleRef.createNestApplication({ bodyParser: false });
  configurarBodyParsers(app as unknown as NestExpressApplication);
  await app.init();
  return { app, prisma: app.get(PrismaService) };
}

/** Limpa na ordem das dependências — o banco de teste é real (ADR-0012 §4). */
/** Cria um usuário com papel escolhido numa BU — para o caso "papel insuficiente". */
export async function criarUsuario(
  prisma: PrismaService,
  mantenedoraId: string,
  buId: string,
  email: string,
  role: 'OWNER' | 'ADMIN' | 'ATENDENTE',
  senha = 'senha-de-teste-1',
): Promise<string> {
  const bcrypt = await import('bcryptjs');
  const user = await prisma.appUser.create({
    data: {
      mantenedoraId,
      name: email,
      email,
      passwordHash: await bcrypt.default.hash(senha, 10),
    },
  });
  await prisma.userBuRole.create({ data: { userId: user.id, buId, role, grantedViaTipo: 'DIRETO' } });
  return user.id;
}

export async function limparBanco(prisma: PrismaService): Promise<void> {
  evolutionFake.inventory.clear();
  evolutionFake.createCalls = 0; evolutionFake.providerCalls = 0; evolutionFake.createHook = null;
  metaFake.enviados.length = 0; metaFake.sendIdNull = false; metaFake.sendHook = null; evolutionFake.enviados.length = 0; evolutionFake.sendIdNull = false; evolutionFake.sendHook = null; metaFake.confirmCalls = 0; metaFake.exchangeCalls = 0; metaFake.exchangeFails = 0; metaFake.providerCalls = 0;
  metaFake.credentialByPhone.clear(); metaFake.credentialCalls.length = 0;
  instagramFake.calls.length = 0; instagramFake.messages.length = 0; instagramFake.sendEnvelope = null;
  instagramFake.subscribed = false; instagramFake.failNext = false; instagramFake.redirectNext = false;
  instagramFake.shortEnvelope = null; instagramFake.longEnvelope = null; instagramFake.meEnvelope = null;
  instagramFake.subscribedEnvelope = null; instagramFake.subscribeEnvelope = null; instagramFake.failAfterSubscription = false;
  instagramFake.afterRequestHook = null; instagramFake.longTokenIssuedAt = null;
  metaFake.registrosNumero = 0;
  metaFake.wabaRecusada = null;
  metaFake.confirmHook = null; metaFake.registrosHook = null; metaFake.confirmCalls = 0; metaFake.subscriptionHook = null;
  typebotFake.enabled = false; typebotFake.starts = 0; typebotFake.continues = 0; typebotFake.startedBots.length = 0; typebotFake.beforeReply = null;
  evolutionFake.ownerPhone = '5584999990000'; evolutionFake.createdState = 'open'; evolutionFake.deleteFails = false;
  await prisma.$executeRawUnsafe(`TRUNCATE TABLE
    "message_template_remote_observations", "message_template_catalog_pages",
    "message_template_observation_leases",
    "message_template_submission_receipts", "message_template_quota_events",
    "message_template_name_reservations", "message_template_operations",
    "message_template_revisions", "message_template_drafts" CASCADE`);
  await prisma.webhookEvent.deleteMany();
  await prisma.instagramAuthorizationAttempt.deleteMany();
  await prisma.message.deleteMany();
  await prisma.$executeRaw`TRUNCATE TABLE "conversation_routes"`;
  await prisma.providerResourceIdentity.deleteMany();
  await prisma.channelRegistrationAttempt.deleteMany();
  await prisma.channelCredential.deleteMany();
  await prisma.conversation.deleteMany();
  await prisma.contactIdentity.deleteMany();
  await prisma.contact.deleteMany();
  await prisma.activityLog.deleteMany();
  await prisma.tokenDeAcesso.deleteMany();
  await prisma.arquivo.deleteMany();
  await prisma.setorGrant.deleteMany();
  await prisma.userBuRole.deleteMany();
  await prisma.appUser.deleteMany();
  await prisma.buChannel.deleteMany();
  // Ownership tombstones are immutable in product paths; this is an explicit
  // table reset confined to the disposable synthetic PostgreSQL fixture.
  await prisma.$executeRaw`TRUNCATE TABLE "business_channel_identities" CASCADE`;
  await prisma.businessUnit.deleteMany();
  await prisma.setor.deleteMany();
  await prisma.mantenedora.deleteMany();
  await prisma.loginAttempt.deleteMany();
}

/** Test channel fixture with the same durable ownership and credential invariants as production. */
export async function criarCanalVerificado(
  prisma: PrismaService,
  buId: string,
  type: 'OFICIAL' | 'NAO_OFICIAL',
  externalResourceId: string,
  options: { status?: 'CONECTADO' | 'CONECTANDO' | 'DESCONECTADO'; requiresWindow?: boolean; provedBusinessPhone?: string; provedWabaId?: string } = {},
) {
  const priorBusinessIdentity = await prisma.businessChannelIdentity.findFirst({ where: { buId, platform: 'WHATSAPP' } });
  if (priorBusinessIdentity && options.provedBusinessPhone && priorBusinessIdentity.externalResourceId !== options.provedBusinessPhone) {
    throw new Error('Synthetic provider proof does not match the retained WhatsApp business resource.');
  }
  const businessResourceId = options.provedBusinessPhone ?? priorBusinessIdentity?.externalResourceId ?? `55${buId.replace(/\D/g, '').slice(-13)}`;
  const businessIdentity = priorBusinessIdentity ?? await prisma.businessChannelIdentity.upsert({
    where: { platform_namespace_externalResourceId: { platform: 'WHATSAPP', namespace: 'WHATSAPP_RESOURCE', externalResourceId: businessResourceId } },
    create: { buId, platform: 'WHATSAPP', namespace: 'WHATSAPP_RESOURCE', scopeReference: 'BU', externalResourceId: businessResourceId },
    update: {},
  });
  if (businessIdentity.buId !== buId) throw new Error('Synthetic WhatsApp business resource is owned by another BU.');
  const channel = await prisma.buChannel.create({ data: {
    buId, businessIdentityId: businessIdentity.id, type, status: options.status ?? 'CONECTADO', requiresWindow: options.requiresWindow ?? type === 'OFICIAL',
    ...(type === 'OFICIAL' ? { phoneNumberId: externalResourceId } : { evolutionInstanceName: externalResourceId }),
    ...(type === 'OFICIAL' ? { wabaId: options.provedWabaId ?? null } : {}),
    ownNumberVerified: true, verifiedEpoch: 0, providerConnectionState: type === 'OFICIAL' ? 'SUBSCRIBED' : 'CONNECTED',
    receiptVerifiedAt: new Date(),
  } });
  const priorIdentity = await prisma.providerResourceIdentity.findUnique({
    where: { provider_externalResourceId: { provider: type, externalResourceId } },
  });
  if (priorIdentity && (priorIdentity.buId !== buId || priorIdentity.currentChannelId)) {
    throw new Error('Fixture resource identity is owned or active elsewhere.');
  }
  const identity = priorIdentity
    ? await prisma.providerResourceIdentity.update({ where: { id: priorIdentity.id }, data: { currentChannelId: channel.id, businessIdentityId: businessIdentity.id, retiredAt: null, managedLifecycle: true, cleanupState: 'ACTIVE' } })
    : await prisma.providerResourceIdentity.create({ data: {
      provider: type, externalResourceId, buId, currentChannelId: channel.id, businessIdentityId: businessIdentity.id, managedLifecycle: true, cleanupState: 'ACTIVE',
    } });
  if (type === 'OFICIAL') {
    const keyId = process.env.CHANNEL_CREDENTIAL_KEY_ID!;
    const key = Buffer.from(process.env.CHANNEL_CREDENTIAL_KEY!, 'base64');
    const envelope = sealChannelCredential('fixture-scoped-token', keyId, key, {
      purpose: 'active', provider: type, buId, channelId: channel.id, generation: channel.generation, version: 1,
    });
    await prisma.channelCredential.create({ data: {
      channelId: channel.id, provider: type, buId, generation: channel.generation, version: 1,
      keyId, nonce: new Uint8Array(envelope.nonce), ciphertext: new Uint8Array(envelope.ciphertext), tag: new Uint8Array(envelope.tag),
    } });
  }
  return { channel, identity };
}

/** Cria uma Mantenedora pela superfície interna — o caminho real de bootstrap. */
/**
 * Cria a Mantenedora **com o onboarding já concluído**.
 *
 * O bootstrap a cria PENDENTE (ADR-0016 §4), e é assim em produção. Os testes
 * que exercitam o produto vêm depois do wizard; quem exercita o portão é
 * `onboarding.e2e-spec.ts`, que usa `criarMantenedoraPendente`.
 */
export async function criarMantenedora(
  app: INestApplication,
  nome: string,
  email: string,
  senha = 'senha-de-teste-1',
) {
  const r = await criarMantenedoraPendente(app, nome, email, senha);
  const prisma = app.get(PrismaService);
  await prisma.mantenedoraSettings.update({
    where: { mantenedoraId: r.mantenedora.id },
    data: { onboardingConcluido: true },
  });
  return r;
}

export async function criarMantenedoraPendente(
  app: INestApplication,
  nome: string,
  email: string,
  senha = 'senha-de-teste-1',
) {
  const res = await request(app.getHttpServer())
    .post('/api/internal/mantenedoras')
    .set('x-internal-token', TOKEN_INTERNO)
    .set('x-requested-with', 'teste')
    .send({ nome, bu: { nome: `Número da ${nome}`, telefone: '5584999990000' }, owner: { nome: 'Dono', email, senha } })
    .expect(201);
  return res.body as {
    mantenedora: { id: string; nome: string };
    businessUnit: { id: string; nome: string };
    owner: { id: string; email: string };
  };
}

/** Faz login e devolve o cookie de sessão para reusar nas próximas chamadas. */
export async function login(app: INestApplication, email: string, senha = 'senha-de-teste-1'): Promise<string> {
  const res = await request(app.getHttpServer())
    .post('/api/bff/auth/login')
    .set('x-requested-with', 'teste')
    .send({ email, senha })
    .expect(200);
  const setCookie = res.headers['set-cookie'] as unknown as string[];
  return setCookie[0].split(';')[0];
}

```

## Complete evidence cp3-adherence46a-raw.json
```json
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-adherence46a-dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "cp3-adherence46a-fresh-no-context",
  "overall_assessment": "Changes required. Inspected all 26 enclosed current source bodies, five governing excerpts and 24 evidence bodies without tools or additional context. Obligation coverage: (1) the common sender uses abstract Channel and operation-policy contracts; actual adapter composition is carried forward from review35. (2) strict V2 parsing, exact route selection and captured ownership are present, but final provider validation has the interleaving below. (3) captured qualified addresses reach shared known-ACK and UNKNOWN acceptance without external retry. (4) applicable admission paths now use provider→qualified peer→conversation locking; conversation-only bookkeeping preserves the valid suffix. The native contention and preserved P2002 bodies support the reported repairs. (5) operation-specific windows and Instagram human-only textual replies are preserved; the current 1000-character contract remains normative. (6) exact V1 readers preserve historical facts and perform local-only recovery; current credential usability no longer gates ordinary known-ACK completion. The Instagram version-change case proves metadata mutation, not cryptographic rotation. (7) selected lookups and WhatsApp discovery are scoped and bounded; current CSV, dependency-harness and remaining consumer bodies require complementary lane B. (8) scheduler/preflight inspection is carried forward, while the packaged API45 reconciliation reports successful 1000-update and replay execution. (9) bounded query improvements and the small policy boundary are positive; complete frozen performance measurements remain outstanding, and final validation is structurally fragmented. (10) full CP4 and subsequent delivery gates remain mandatory. API45 reports 424 unit and 586 E2E passes; this reviewer neither executed them nor independently inspected the referenced log. The 41 unchanged prior body reviews are carried evidence, not fresh reads. Recorded read-boundary and code-before-test qualifications remain intact. This lane alone cannot accept CP3 or the feature.",
  "recommended_path": "Repair the final provider-fence interleaving within the existing shared owners and approved contract, add native pre-POST lifecycle-mutation controls, then freeze and validate the affected candidate. Reconcile both complementary review results and current evidence before closing individual CP3 findings. Complete all CP4 consumers and the remaining primary-protocol, browser, ALL, performance, assurance, cutover and separately approved physical-runtime gates. Preserve the recorded provenance limitations and pending human decisions.",
  "performance_position": "mixed",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "IG-CP3-A46-01",
      "severity": "high",
      "category": "adherence",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "Final provider validation can become stale during subsequent awaited checks",
      "rationale": "After the claim transaction releases its locks, OutboundService.finalProviderFence awaits contextBeforeDispatch, then policy.inspect, then the actor callback. The callback locks only user, grant and BU rows; its final checks cover the signed session and captured deadlines. A credential replacement or generation-changing disconnect committed after the provider-context observation can therefore escape this common fence while the actor remains authorized and the operation retains its previously decrypted credential. The Channel contract provides no guarantee of another provider-tuple observation after these awaits. The native authorization tests hold this same context-read boundary but mutate only grants/session; accepted-fact tests mutate credentials after POST. This is an uncovered source-supported interleaving, not a demonstrated production failure. It conflicts with IG-ARCH-R1-01's requirement to validate the captured current tuple before external dispatch.",
      "suggested_action": "Make the final local observation coherently validate the captured provider, generation, credential, readiness and actor facts at the last awaited boundary, followed by synchronous session/deadline checks. Preserve abstract policy ownership, short transactions and HTTP outside transactions. Add native held-boundary cases for actual reauthorization and disconnect with a live actor, requiring zero message POSTs and matched unchanged-context controls.",
      "affected_paths": [
        "api-app/src/domain/inbox/outbound.service.ts",
        "api-app/src/integrations/channels/prisma-channel-resolver.ts",
        "api-app/src/surfaces/bff/conversations.controller.ts",
        "api-app/test/instagram-cp3-authorization-fences.e2e-spec.ts"
      ]
    },
    {
      "finding_id": "IG-CP3-ROOT-03",
      "severity": "high",
      "category": "operational_fit",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "Recorded CP4 consumers and remaining delivery gates remain open",
      "rationale": "The recorded follow-up paths are cp4-connections-preparation21-root-qualified.json, cp4-safe-display-preparation22.json, cp4-browser-composer-preparation23-root-qualified.json and cp4-live-ingress-preparation19.json. The governing TODO explicitly retains their unimplemented connection catalogue/verify/disconnect/reactivation lifecycle, qualified account/peer display, strict V2 React composer and asynchronous context fences, shared Incoming/realtime publication, and HTTPS browser/freshness/CI proofs. Current list/thread projections still expose legacy contact presentation, and replyOptions still selects the latest authorization username without successful same-account mapping qualification. These are acknowledged CP4 obligations, not newly attributed CP3 regressions. Primary own-subscription observation remains unresolved under primary-subscription-index-research40.json; API45 does not close it or the remaining ALL, assurance, performance, cutover and physical-runtime gates. No waiver permits backend-only delivery.",
      "suggested_action": "Keep ROOT-03 open in this TODO and implement the complete recorded CP4 producer/consumer work with native PostgreSQL, WS and real-backend browser proofs. Retain the primary-observer and subsequent gates, respect the exact admitted OAuth middleware scope, and preserve the current character limit while the UTF-8 and protected privacy proposals await their required human decisions.",
      "affected_paths": [
        "api-app/src/domain/inbox/conversations.service.ts",
        "api-app/src/surfaces/bff/conversations.controller.ts",
        "api-app/src/integrations/channels/prisma-channel-resolver.ts",
        "foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md"
      ]
    }
  ]
}
```

## Complete evidence cp3-adherence46b-raw.json
```json
{
  "schema_version": "subagent-review-result-v1",
  "artifact_kind": "subagent_review_result",
  "dispatch_path": "/mnt/c/unifast/leadshug/leadshug_now_docker/foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/cp3-adherence46b-dispatch.json",
  "review_kind": "architecture_adherence",
  "reviewer_label": "cp3-adherence46b-no-context",
  "overall_assessment": "changes_required",
  "recommended_path": "Inspected all 18 enclosed source bodies, five governing excerpts and 24 evidence artifacts without tools or additional reads. This result covers affected lane B; the complementary lane and root freeze/coverage reconciliation remain necessary. The recorded 41 unchanged prior body reviews are carried forward, not claimed as fresh inspections. Obligation coverage: (1) the abstract Channel and operation-policy contracts remain appropriate, with generic business consumers and carried-forward DI composition; the protection-harness residual below remains. (2) exact selected-route lookup, strict V2 parsing and captured fingerprints have source support; native routing preserves distinct conversations for identical peers under two Instagram accounts. (3) post-ACK contextStatus no longer requires current credentials, while retained ownership/generation checks and the recorded four ACK cases support the original credential-coupling repair; complete sender/acceptance inspection belongs to the complementary lane. (4) inspected admission paths now acquire provider identity, qualified peer and conversation in order; conversation-only bookkeeping retains a valid suffix. API45 records all three native lock groups and preserved P2002 assertions/count three, without establishing a historical production deadlock. (5) qualified resource windows and Instagram human-reply-only policy remain intact, but initial-options recipient eligibility is inconsistent as detailed below. The approved 1000-character limit remains normative. (6) exact historical parsers and local-only admission recovery preserve the V1 boundary; the unknown-context repair returns a scoped read-only hint rather than inventing a route or redispatching. Complete historical recovery coverage requires the complementary lane. (7) selected and WhatsApp discovery reads are bounded; CSV now pages conversations and messages while preserving full output, qualification, filters, ordering and escaping. Public API and legacy BU consumers retain their recorded unchanged review coverage. (8) scheduler source coverage is carried forward; API45 records the complete 1000-update/replay case at 5099.176/3344.715 ms, including downstream assertions. (9) affected read shapes improve performance and the small contracts remain reasonably simple, but the frozen full EPS/RLS cohorts and broader assurance are not established by these API results. The documented read-boundary incident and code-before-test authorship remain qualifications; GREEN does not establish retroactive RED/test-first compliance. (10) complete CP4 and subsequent gates remain mandatory. Fix the two current CP3 gaps below within the approved owners, preserve all existing assertions and budgets, reconcile fresh frozen validation and complementary review, then complete CP4. Retain primary protocol, OAuth gateway/browser, ALL, security, TQA, cutover, final review and separately approved physical-runtime gates. Pending privacy and UTF-8 proposals confer no implementation authority.",
  "performance_position": "mixed",
  "elegance_position": "acceptable",
  "structural_soundness_position": "mixed",
  "operational_fit_position": "mixed",
  "findings": [
    {
      "finding_id": "IG-CP3-B46-01",
      "severity": "medium",
      "category": "adherence",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Initial options advertise eligible WhatsApp operations for an Instagram recipient",
      "rationale": "initialOptions verifies only that the conversation exists, then evaluates the BU's WhatsApp connections without qualifying the conversation's recipient identity. In a mixed BU, an Instagram-only contact therefore receives an available Evolution text option and potentially an available official template option. resolveForInitial subsequently rejects those same choices because ensureExplicitWhatsAppInitialRoute requires a WhatsApp contact identity. The new bounded-query test actually supplies a conversation created by signed Instagram ingress and expects two WhatsApp choices. This preserves query bounds while accepting inconsistent options and dispatch eligibility, contrary to the frozen requirement that both use the same trusted operation context. No wrong-recipient POST is demonstrated; dispatch currently fails closed.",
      "suggested_action": "Qualify the conversation's recipient platform before advertising initial-send eligibility, using bounded canonical identity reads. Keep Instagram contacts ineligible for initial WhatsApp operations. Use a genuine WhatsApp conversation for the positive bounded-options fixture and add a mixed-BU Instagram negative control, preserving the twelve-account cohort, connection budgets and zero-effect assertions.",
      "affected_paths": [
        "api-app/src/integrations/channels/prisma-channel-resolver.ts",
        "api-app/test/instagram-cp3-query-boundaries.e2e-spec.ts"
      ]
    },
    {
      "finding_id": "IG-CP3-A-02",
      "severity": "medium",
      "category": "tests",
      "formalizable_hint": "yes",
      "candidate_rule_level": "project",
      "title": "Concrete operation-policy dependencies can still pass the protection harness",
      "rationale": "The harness now covers Instagram imports, tokens, adapterOrigin branches and InitialMessageService, supporting those portions of A-02. However, a direct OfficialChannelWindowPolicy import/reference passes: its module is outside policyModule and its name matches none of the concrete-name checks. A valid namespace import followed by new policies.OfficialEligibilityPolicy(windows) also passes because policy import inspection handles only named imports and the identifier matcher omits Official classes. These are ordinary concrete policy dependencies forbidden by the approved abstract-policy boundary, including the specific OfficialChannelWindowPolicy dependency being retired. This is a remaining protection gap, not evidence that current consumers contain those dependencies.",
      "suggested_action": "Extend the existing bounded guard and negative fixtures to reject the concrete window-policy dependency and concrete eligibility-policy namespace access. Retain positive abstract dispatch, abstract policy and legitimate address-validation controls; no general dataflow framework is needed.",
      "affected_paths": [
        "api-app/src/domain/channels/transport/channel-dependencies.spec.ts"
      ]
    },
    {
      "finding_id": "IG-CP3-ROOT-03",
      "severity": "high",
      "category": "residual_risk",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "Recorded CP4 consumers remain mandatory delivery blockers",
      "rationale": "The recorded follow-up paths are cp4-connections-preparation21-root-qualified.json, cp4-safe-display-preparation22.json, cp4-browser-composer-preparation23-root-qualified.json and cp4-live-ingress-preparation19.json. They explicitly retain the paginated connection lifecycle, safe account/peer projections, strict V2 React composer, shared Incoming/realtime integration and HTTPS real-backend browser proof. Inspected list projections still expose legacy contact fields, and replyOptions still uses raw WABA display and an unqualified latest authorization username. These are acknowledged CP4 obligations with no waiver, not newly inferred CP3 regressions. API45 establishes neither their implementation nor browser/ALL acceptance.",
      "suggested_action": "Keep ROOT-03 open in this TODO and implement complete CP4, including lifecycle recovery, mapped-account display, draft/context fencing, native realtime, browser freshness and CI parity. Complete the remaining assurance and approved runtime gates before claiming functional delivery.",
      "affected_paths": [
        "api-app/src/domain/inbox/conversations.service.ts",
        "api-app/src/domain/inbox/incoming.service.ts",
        "api-app/src/integrations/channels/prisma-channel-resolver.ts",
        "foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md"
      ]
    },
    {
      "finding_id": "IG-SUBPROTO-01",
      "severity": "high",
      "category": "operational_fit",
      "formalizable_hint": "partial",
      "candidate_rule_level": "project",
      "title": "Primary own-subscription observation remains unresolved",
      "rationale": "The recorded follow-up is IG-SUBPROTO-01 together with IG-SUBREC-03. primary-subscription-index-research40.json explicitly leaves the Instagram Login GET envelope, returned ID namespace, visibility and completeness unproved. The synthetic subscribed_apps envelope in helpers.ts is a fixture assumption and cannot establish that protocol. Preserving UNKNOWN and preventing repeated mutation provides protection but does not fulfill the approved own-account observation obligation. No current API pass closes this release gate.",
      "suggested_action": "Retain both findings as open and establish the required primary protocol evidence before accepting or implementing conclusive subscription/absence interpretation. Preserve UNKNOWN and the no-repeat fence; do not substitute Facebook Page semantics, guessed ID equality or undocumented completeness assumptions.",
      "affected_paths": [
        "api-app/test/helpers.ts",
        "foundation_documentation/artifacts/reviews/leadshug-instagram-channel-20261023/evidence/primary-subscription-index-research40.json",
        "foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md"
      ]
    }
  ]
}
```

## Complete evidence cp3-adherence46-root-adjudication.json
```json
{
  "kind": "root-adjudicated-complementary-cp3-adherence46",
  "status": "changes_required",
  "all261SourcesTodo34Inputs35Preservations3GitlinksExact": true,
  "sourceBodies": {
    "a": 26,
    "b": 18,
    "union": 35,
    "priorUnchangedCarried": 41,
    "all19DeltaSourcesCovered": true
  },
  "bothCanonicalTurnCompleted": true,
  "bothStrictSchemaMergesPassed": true,
  "sourceFreeze": "d9c9139238f428f67f9bae5fa89e6fbe15f2e73c",
  "apiProof": "cp3-api45-root-reconciliation.json",
  "qualifications": [
    "Fresh current35body union+41unchanged carried from original52body review; no peer-lane actualread claim.",
    "Source46finalfence defect is supported interleaving, not executedproductionfailure. Need nativecausal RED beforeprodrepair.",
    "Readboundaryincident and code-before-test consumer39 preserved. Metadata-version ACKcase notcryptographicrotation.",
    "Root corrected14explicitopen/pending classes in derived dispatch beforelaunch; no canonicalhelpercodechange.",
    "Canonical runner retained; only documentedstrictCLI xhigh argvconfigurationaddedinmemory; noexecutable/config/source edits."
  ],
  "findings": [
    {
      "id": "IG-CP3-A46-01",
      "severity": "high",
      "resolution": "Integrated",
      "classification": "release-blocker",
      "route": "fix in this TODO",
      "state": "open; final provider tuple/actor observation must be coherent at last awaited local boundary",
      "next": "Focused HOW opinion, native actualreauthorize/disconnect causalcontrols, source repair within existing sharedowners."
    },
    {
      "id": "IG-CP3-B46-01",
      "severity": "medium",
      "resolution": "Integrated",
      "classification": "release-blocker",
      "route": "fix in this TODO",
      "state": "open; initialOptions wrongly offers WA for IGcontact whiledispatchdenies",
      "next": "Boundedcanonicalrecipient eligibility inoptions; genuineWApositivefixture+mixedBUIGnegative; retain12accountcohort."
    },
    {
      "id": "IG-CP3-A-02",
      "alias": "B46 guardfinding",
      "severity": "medium",
      "resolution": "Integrated",
      "classification": "release-blocker",
      "route": "fix in this TODO",
      "state": "partiallyfixed; concreteOfficialWindow andnamespaceOfficialEligibility imports evadeguard",
      "next": "Exactnegativefixtures+boundedASTguard withoutfutureframework; preservepositiveabstract/addresscontrols."
    },
    {
      "id": "IG-CP3-ROOT-03",
      "alias": "both46lanes",
      "severity": "high",
      "resolution": "Integrated",
      "classification": "release-blocker",
      "route": "fix in this TODO",
      "state": "open; completeCP4 andlatergatesmandatory"
    },
    {
      "id": "IG-SUBPROTO-01",
      "alias": "IG-SUBREC-03",
      "severity": "high",
      "resolution": "Integrated",
      "classification": "release-blocker",
      "route": "resolve primary protocol in this TODO",
      "state": "open; no conclusiveGETID/envelope/completeness/absenceguess"
    }
  ],
  "originalFindingClosures": [
    {
      "ids": [
        "IG-CP3-ROOT-01",
        "IG-CP3-ROOT-02",
        "IG-CP3-ROOT-07",
        "IG-CP3-A-01",
        "IG-CP3-B35-05"
      ],
      "basis": "Original boundedselection, credentialcoupling, peerlocks, currenthumanfencepresence andunboundedCSV sourceissues fixed and supported bycurrentAPI45 andaffected46source. NewA46-01 remains independentlyopen; A-02 partial. Nowholecheckpoint/delivery acceptance."
    }
  ],
  "next": "Concretize A46 coherent final-fence HOW without relaxing last-boundary/shortTX/HTTPoutsideTX and with faithful native linearization controls, then test-first remaining source corrections; fullCP4 remains in sequence."
}

```

## Complete evidence cp3-api45-root-reconciliation.json
```json
{
  "kind": "root-independent-api45-reconciliation",
  "date": "2026-10-24",
  "all261SourceHashesExact": true,
  "todo": {
    "path": "foundation_documentation/todos/active/features/TODO-leadshug-instagram-channel.md",
    "sha256": "804e17228c1b6735ae3e1e91c0c36ad18fe961c73bf6a8deaf99001ba156693b",
    "bytes": 272714
  },
  "all690BoundInputsExact": true,
  "all35PreservationRowsExact": true,
  "all3RootIndexGitlinksExact": true,
  "log": {
    "path": "cp3-api45-api.log",
    "bytes": 226548,
    "sha256": "07fd007b5795d91b324b1f2baf8e315004271c6957639c9cfb7c51eb2070aa8a",
    "completeStdoutStderr": true
  },
  "exitCode": 0,
  "proofs": {
    "oldNativeP2002": "PASS: dispatch-admission real P2002 race rollback/readback/retry case passed in 545ms with the frozen count-3/nine-oracle assertions. Native log shows passing case rather than a separate count scalar.",
    "newAuthorizationFences": "PASS: 6/6 tests in instagram-cp3-authorization-fences.e2e-spec.ts (5157ms).",
    "nativeSerializedLockScopes": "PASS: full CP3 native dispatch lock case passed (739ms); all same-account IG, independent-account, and formatted-WA assertions in that case completed, including the formerly blocking WA fixture.",
    "queryBoundaries": "PASS: 4/4 tests in instagram-cp3-query-boundaries.e2e-spec.ts; explicit route/read boundary and IG-only BU readiness queries completed.",
    "ackCases": "PASS: 4/4 CP3 Instagram ACK/local-fact cases (credential delete, metadata version change, shortened expiry, real generation conflict).",
    "csv": "PASS: new CP3 CSV boundary case 1/1 and existing historical CSV controls pass.",
    "cp2FinalClock": "PASS: strict CP2 final-clock file 9/9 tests (20113ms suite); no timing threshold modified.",
    "cp2ResidualClock": "PASS: CP2 residual file 12/12 tests, including natural session-expiry matched-live case.",
    "batch": "PASS: initial 1000 updates elapsedMs=5099.176; replay 1000 elapsedMs=3344.715; full batch test passed in 8471ms. The initial <=15000ms assertion and all following count/replay/malformed/oversize/echo/read checks were reached."
  },
  "counts": {
    "parityMutationsRejected": 26,
    "migrations": 31,
    "unitFiles": 39,
    "unitPassed": 424,
    "unitFailed": 0,
    "e2eFiles": 55,
    "e2ePassed": 586,
    "e2eFailed": 0,
    "p2002RecoveryCasePassed": 1,
    "nativeP2002ExpectedCount": 3,
    "authorizationFenceTestsPassed": 6,
    "nativeLockCasePassed": 1,
    "nativeLockGroupsPassed": 3,
    "cp3QueryBoundaryTestsPassed": 4,
    "cp3AckCasesPassed": 4,
    "cp3CsvBoundaryTestsPassed": 1,
    "cp2FinalClockTestsPassed": 9,
    "cp2ResidualClockTestsPassed": 12,
    "batchInitialUpdates": 1000,
    "batchInitialElapsedMs": 5099.176,
    "batchReplayUpdates": 1000,
    "batchReplayElapsedMs": 3344.715
  },
  "rootActualLogRead": "Exact complete-log hash plus native summary/case/phase lines independently inspected after terminal. No current or growing log was used as acceptance.",
  "scope": "Full API synthetic disposable evidence; no formaladherence/CP4/browser/ALL/physicalruntime acceptance",
  "next": "Fresh complementary affected-source review46 carrying all35 priorfindings, all19actualchanged/new sources and fullcurrentbodies, then completeCP4. Primary/human/assurance/runtime gates remain mandatory."
}

```

## Complete evidence cp3-api45-result.json
```json
{
  "kind": "cp3-api45-canonical-full-api-result",
  "date": "2026-10-24",
  "command": "bash scripts/test-channels-local.sh api",
  "invocations": 1,
  "exitCode": 0,
  "terminalOutcome": "PASS (full canonical API validation only)",
  "log": {
    "path": "cp3-api45-api.log",
    "bytes": 226548,
    "sha256": "07fd007b5795d91b324b1f2baf8e315004271c6957639c9cfb7c51eb2070aa8a",
    "completeStdoutStderr": true
  },
  "preflight": {
    "files": 261,
    "exact": true,
    "boundInputs": 690,
    "exactBoundInputs": true,
    "preservationRows": 35,
    "rootGitlinks": 3,
    "authority": "GO",
    "routing": "GO",
    "outputsAbsent": true
  },
  "postflight": {
    "files": 261,
    "exact": true,
    "boundInputs": 690,
    "exactBoundInputs": true,
    "preservationRows": 35,
    "rootGitlinks": 3
  },
  "stages": [
    {
      "name": "channels parity/self-guards",
      "status": "PASS",
      "parityMutationsRejected": 26
    },
    {
      "name": "Prisma client generation",
      "status": "PASS",
      "evidence": "Prisma Client v6.19.3 generated in 275ms"
    },
    {
      "name": "database migrations",
      "status": "PASS",
      "migrations": 31,
      "evidence": "all applied; schema up to date"
    },
    {
      "name": "lint",
      "status": "PASS"
    },
    {
      "name": "build",
      "status": "PASS"
    },
    {
      "name": "unit tests",
      "status": "PASS",
      "files": 39,
      "passed": 424,
      "failed": 0
    },
    {
      "name": "E2E tests",
      "status": "PASS",
      "files": 55,
      "passed": 586,
      "failed": 0
    }
  ],
  "requestedProofs": {
    "oldNativeP2002": "PASS: dispatch-admission real P2002 race rollback/readback/retry case passed in 545ms with the frozen count-3/nine-oracle assertions. Native log shows passing case rather than a separate count scalar.",
    "newAuthorizationFences": "PASS: 6/6 tests in instagram-cp3-authorization-fences.e2e-spec.ts (5157ms).",
    "nativeSerializedLockScopes": "PASS: full CP3 native dispatch lock case passed (739ms); all same-account IG, independent-account, and formatted-WA assertions in that case completed, including the formerly blocking WA fixture.",
    "queryBoundaries": "PASS: 4/4 tests in instagram-cp3-query-boundaries.e2e-spec.ts; explicit route/read boundary and IG-only BU readiness queries completed.",
    "ackCases": "PASS: 4/4 CP3 Instagram ACK/local-fact cases (credential delete, metadata version change, shortened expiry, real generation conflict).",
    "csv": "PASS: new CP3 CSV boundary case 1/1 and existing historical CSV controls pass.",
    "cp2FinalClock": "PASS: strict CP2 final-clock file 9/9 tests (20113ms suite); no timing threshold modified.",
    "cp2ResidualClock": "PASS: CP2 residual file 12/12 tests, including natural session-expiry matched-live case.",
    "batch": "PASS: initial 1000 updates elapsedMs=5099.176; replay 1000 elapsedMs=3344.715; full batch test passed in 8471ms. The initial <=15000ms assertion and all following count/replay/malformed/oversize/echo/read checks were reached."
  },
  "counts": {
    "parityMutationsRejected": 26,
    "migrations": 31,
    "unitFiles": 39,
    "unitPassed": 424,
    "unitFailed": 0,
    "e2eFiles": 55,
    "e2ePassed": 586,
    "e2eFailed": 0,
    "p2002RecoveryCasePassed": 1,
    "nativeP2002ExpectedCount": 3,
    "authorizationFenceTestsPassed": 6,
    "nativeLockCasePassed": 1,
    "nativeLockGroupsPassed": 3,
    "cp3QueryBoundaryTestsPassed": 4,
    "cp3AckCasesPassed": 4,
    "cp3CsvBoundaryTestsPassed": 1,
    "cp2FinalClockTestsPassed": 9,
    "cp2ResidualClockTestsPassed": 12,
    "batchInitialUpdates": 1000,
    "batchInitialElapsedMs": 5099.176,
    "batchReplayUpdates": 1000,
    "batchReplayElapsedMs": 3344.715
  },
  "failures": [],
  "notes": [
    "All full canonical API stages and test assertions completed successfully for this frozen candidate.",
    "This is local API validation evidence only; it does not assert ALL, browser, current formal review, provider protocol, real runtime, checkpoint, or feature-gate acceptance.",
    "No source/input change, autofix, retry, additional validation command, or Git write occurred."
  ]
}

```

## Complete evidence cp3-auth36-terminal.json
```json
{
  "kind": "root-reconciled-auth36-static-terminal",
  "changedExisting": [
    "api-app/src/domain/inbox/conversations.service.ts",
    "api-app/src/domain/inbox/outbound.service.spec.ts",
    "api-app/src/domain/inbox/outbound.service.ts",
    "api-app/src/surfaces/bff/conversations.controller.ts"
  ],
  "new": [
    "api-app/test/instagram-cp3-authorization-fences.e2e-spec.ts"
  ],
  "sourceCountMatched": 257,
  "preservationRowsMatched": 35,
  "rootIndexMatched": true,
  "hashes": {
    "api-app/src/domain/inbox/outbound.service.ts": "34e7b98462228f37ff2915cfbdf067fa2b2591a198d9ae7d8779976e35db5a26",
    "api-app/src/domain/inbox/outbound.service.spec.ts": "ad8e4f19b3aacf6df772526ab730d6de9e89dc420ad0ccc859f820cbf882e5b2",
    "api-app/src/domain/inbox/conversations.service.ts": "1aa8ad944527529255b589af45f5e1d05aa0bc36d504f2315330ca9ed546cd5b",
    "api-app/src/domain/inbox/initial-message.service.ts": "ed7dac94eb2125525d66553b059b63f1770651dc30638e262fd33e157c6f188a",
    "api-app/src/surfaces/bff/conversations.controller.ts": "799a1866c203557b9a115c327dfb466b40c71cb937218997c1a2fecec6ad34e2",
    "api-app/test/instagram-cp3-routing.e2e-spec.ts": "fb01016fbce4294ba68c1223c14fc05c184255ab388bf6688e92d702d29ee823",
    "api-app/test/instagram-cp3-authorization-fences.e2e-spec.ts": "ac62369b48608336ab89e1a865881927d3a1ab5c1821653e6006a24318a30411"
  },
  "tests": "NOTRUN; code-first authored then corrected native causal preconditions beforefirstexecution, no RED claim",
  "reviewQualification": "No formal/checkpointacceptance; next ROOT07source serialized beforecanonicalvalidation"
}

```

## Complete evidence cp3-repair44-terminal.json
```json
{
  "kind": "root-qualified-repair44-terminal",
  "sourceCount": 261,
  "changedPaths": [
    {
      "path": "api-app/src/domain/inbox/dispatch-admission.service.ts",
      "bytes": 48540,
      "sha256": "559039c84b20ac986b6bc3b2b0590a50a6be9454634d7bbb2c05d706c5a387e4"
    },
    {
      "path": "api-app/test/initial-message.e2e-spec.ts",
      "bytes": 122472,
      "sha256": "f35e939d81f537458b08e91ab9a98632bd4f614892f86fbf1632dda8ce95ed17"
    },
    {
      "path": "api-app/test/instagram-cp3-csv-boundaries.e2e-spec.ts",
      "bytes": 14963,
      "sha256": "311609e3e03a3ad3088e82035cc0a53fde3822abd346617d0566988aea548795"
    },
    {
      "path": "api-app/test/instagram-cp3-locks.e2e-spec.ts",
      "bytes": 14422,
      "sha256": "e571b7438a4ef88a5645ba14b32c457357c00e1e557d2dcb85b9ad44e9bbbfb4"
    },
    {
      "path": "api-app/test/instagram-cp3-query-boundaries.e2e-spec.ts",
      "bytes": 13341,
      "sha256": "b8e360136c9c501e2e1f54e6c22ba2adbea108dbd2c19ab6a23e0751509aeacc"
    }
  ],
  "allOther256SourcesExactToAPI43": true,
  "writerTerminal": true,
  "tests": "NOTRUN",
  "qualifications": [
    "Only five approvedpaths changed. Scope did notexpand.",
    "Root staticread rejected first unknown-context custom503 envelope before execution. Writer removedcustomexception and returns scopedhint read-only after actorcheck, delegating canonical knownACK503 to existing Outbound caller; no nativeassert changed.",
    "CSV retains409+exactcode, reads historical CSV content-type response.text JSON.",
    "12account cohort retains all actual OAuth+PG mappings; only synthetic completedattemptcreatedAt aged2..13hours, productionbudgets unchanged.",
    "BU readiness test retains lockwait/zeroPOSTwhilepinned; afterinactivecommit asserts409/REJECTED/zeroPOST/zeroMessage/nullReceipt, as required by finalactorfence.",
    "FormattedWA Contact createdseparately before ConversationcontactId, allnativewait/scopeoracles retained."
  ],
  "next": "One full canonicalAPI45 under newfrozen261/T/boundinputs/35/3; nofreshPASSuntil terminal."
}

```

## Complete evidence primary-subscription-index-research40.json
```json
{
  "kind": "public-primary-index-research40",
  "date": "2026-10-24",
  "method": "Read-only official Meta web pages via web tool then direct urllib HTTPS without cookies, credentials or Graph API calls. Web tool429/inaccessibility did not establish direct-fetch unavailability.",
  "retrievals": [
    {
      "url": "https://developers.facebook.com/llms.txt",
      "http": 200,
      "bytes": 6068,
      "sha256": "fc98bed87f818e2cf2f0bbec5c880fe97011a1bd33738e940ffcaf1dce70d3ab"
    },
    {
      "url": "https://developers.facebook.com/documentation/instagram-platform/llms.txt",
      "http": 200,
      "bytes": 18901,
      "sha256": "204f82d1869e4bd9237f5ca4c16a67ad0b60835ddea02f71220f9cd7fcada3ff"
    },
    {
      "url": "https://developers.facebook.com/documentation/instagram-platform/reference/me.md",
      "http": 200,
      "bytes": 942,
      "sha256": "5f14ed97cb888aceecbe022ca53effa06be0cb9dbe04e0e10859b79b3d7ad9be"
    },
    {
      "url": "https://developers.facebook.com/documentation/instagram-platform/webhooks/setup.md",
      "http": 200,
      "bytes": 18504,
      "sha256": "c3ae23a8c1a32d96879f78dab2eaf5fd793c1192b86dcd86463d1a9a912724ca"
    },
    {
      "url": "https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user.md",
      "http": 200,
      "bytes": 15447,
      "sha256": "6ad72e0c2f1efdc5f1dd35410703c20083effb0ac4fe0a5f43450feccb49cea0"
    },
    {
      "url": "https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks/debugging.md",
      "http": 200,
      "bytes": 2356,
      "sha256": "7461a4a10001f52124ba3f02d7dff12c96e380234119f2218602b7ac35a3498f"
    }
  ],
  "observations": [
    "The official root index exposes product-specific llms indexes and actual Markdown exports. Some responses vary content type/body; .md naming or200 alone is not accepted as evidence of actual desired content.",
    "Instagram setup explicitly distinguishes Unified Login/Facebook Login graph.facebook.com from Instagram Login graph.instagram.com and documents account-level subscription POST with success:true.",
    "The inspected Instagram Login sources still do not establish own-subscription GET response envelope, returned ID namespace, visibility/completeness or conclusive-empty absence.",
    "The inspected debugger guide concerns a linked Facebook Page and Messenger dashboard; it cannot establish Instagram Login GET semantics."
  ],
  "conclusion": "IG-SUBPROTO01/SUBREC03 remain open. No guessed IDs, Page flow, success/absence parser, new config or no-op acceptance. No conclusion of unsupported endpoint from omission.",
  "implementationChange": false,
  "runtimeOrProviderProof": false
}

```

## Complete evidence cp4-connections-preparation21-root-qualified.json
```json
{
  "kind": "root-qualified-cp4-connections-preparation21",
  "status": "Preparation only; no sourcewrite/review/test acceptance",
  "approvedRoutes": "T753-833 existing GET channel-connections and byUUID verify/disconnect, plus OAuth current CONNECT/REAUTHORIZE. No newWHAT.",
  "actualGaps": [
    "No channel-connections routes currently implemented. Legacy /channels GET reads all types/unbounded.",
    "REAUTHORIZE requires existing matching credential; correct localdisconnect removal/detach would otherwise prevent any sameaccount reactivation."
  ],
  "qualifiedHow": [
    "Use second controller class in already-admitted channels.controller.ts, register bff.module.ts; do not use advisor newcontroller path outside exact list. Tests must match admitted *instagram*.e2e-spec.ts, not unadmitted channel-connections spec name.",
    "Small domain/channels catalogue service: stable localopaque cursor<=512/limit1..50 default20, fixedBU query limit+1 continuation, safeusername/WAcanonicaldisplay/no rawIGIDs/credentials/provider fanout. LegacyWA projection validates compatible resource/cardinality, no silently sliced subset.",
    "IG verify/disconnect remain existing InstagramAuthorizationService lifecycle owner, reusing actor/session/resource lock/livegrant/lease/deadline/cooldown; no duplicate independently fenced IG lifecycle or blind advance→POST onverify.",
    "Verify is explicit bounded observation only. CurrentGET observer UNKNOWN neverproves absence/ownsubscription/receipt; do not change states toconnected fromprofile.",
    "Disconnect atomically disableslocalbinding/incrementsgeneration/invalidatescredentials and activeoperationleases; retains BCI/providerowner/routes/messages/attempts. No guessed GraphDELETE/remoteCLEANED: reportcleanup pending unless ownscope proved.",
    "Complete safe REAUTHORIZE of disconnected sameBU/samebusiness account under expectedGeneration and absentcredential CAS; reject foreignresource and changedlivecredential; remaponly sameownedtombstone withfreshversion/generation. This is existing reauthorization lifecycle HOW, not new operation enum/resource transfer. Existing completed snapshots/ACK recovery unaffected.",
    "Add nativePG auth/scoping/cursor/negativegeneration/livegrant/lease/cooldown/UNKNOWN/noeffects/disconnect→sameaccountreactivate/inflightfence/history tests; no fixture rewrite of ownerfacts."
  ],
  "otherCP4": "Preps18/19 safe display, strictV2 composer and shared Incoming realtime remain required. API currentcandidate awaitingcompleteproof."
}

```

## Complete evidence cp4-browser-composer-preparation23-root-qualified.json
```json
{
  "kind": "root-qualified-cp4-browser-composer-preparation23",
  "state": "Preparation, not implementation or executed proof. New unbound artifact only during API22 freeze.",
  "readset": [
    {
      "path": "web-app/src/api.ts",
      "sha256": "7c80a2e738655c5b54382e2805d5e8e808b80e25af283ca90402e932a3d3794c"
    },
    {
      "path": "web-app/src/telas/Inbox.tsx",
      "sha256": "66658161c7c74610288bf6c92583b616bacc1ada0fced27af01997ed22481737"
    },
    {
      "path": "web-app/src/componentes/NovaConversa.tsx",
      "sha256": "2702cae2c4d913d511e33ca8d305ecc03d7ee56f34623877058865d884aa1bdd"
    },
    {
      "path": "api-app/test/browser-server.cjs",
      "sha256": "02354237e3c0c5f8d918f65cbb833270e2ce02469cfe3e926e3a6790abc106dc"
    },
    {
      "path": "web-app/playwright.config.ts",
      "sha256": "53e9a54e97c9b785135d94846d99eb77c6f05789a58f27128544f9b2c903a63d"
    },
    {
      "path": "api-app/src/surfaces/bff/instagram-authorizations.controller.ts",
      "sha256": "618795b4cb3291c48652b63fce969a10977e32ab0adc2683e40cfbe392b3b62b"
    },
    {
      "path": "api-app/src/infra/session/session.service.ts",
      "sha256": "884618471c7cc58c037f04d20c790979409bbbcfc2fe61b34312b2625b28e200"
    }
  ],
  "composerHow": [
    "Add narrow pure frontend context/draft state in admitted src/*instagram*.ts with unit tests and typed safe API DTOs. Preserve existing timeline recovery, initial-message/template owners.",
    "Fetch reply-options once per current opened composer and authorize exact route/channel/generation/fingerprint before typing. Independent in-memory draft per BU/conversation/route/context; restore only when same tuple is freshly authorized.",
    "Monotonic intent token fences A→B→A and late option/send completions. Synchronous per-action in-flight ref blocks doubleclick. Exact V2 POST only; clear only captured draft version after acceptance. Conflict/uncertainty retains draft, no automatic retry.",
    "Use same safe platform/account/recipient projection for list/thread/options. No opaque Instagram ID as phone. IG initial/template/automation paths stay ineligible; WhatsApp initial/template journeys remain unchanged."
  ],
  "FrcFixtureQualification": "Same opaque peer in two Instagram accounts must be two contacts/conversations created by actual signed ingress. No fabricated cross-account merge to make UI test pass. Test actual account A→B→A and delayed completion; use same-business WhatsApp adapters for in-conversation adapter switch if needed.",
  "harnessBaselineCorrection": "Prep03 WEB_ORIGIN assumption is now stale: current InstagramAuthorizationsController builds final303 from WEB_ORIGIN. A proxy alone over default HTTP API would not prove HTTPS final return. Protected Playwright/global default WEB_ORIGIN must remain unchanged.",
  "harnessHow": [
    "In admitted browser-server.cjs, parent HTTP3100/4173 remains unchanged; own same-file internal child real Nest3102 uses exact child-only WEB_ORIGIN HTTPS4174 and Instagram redirect callback on HTTPS4174. No new global config/protected App.tsx edit.",
    "Owned loopback TLS frontdoor4174 proxies /api and native /ws upgrade to real child3102 and all assets/config to built preview4173. Preserve browser path/Host/Origin/cookie and response/Location; no auth/session/DB/WS/response stubs. Child API uses same guarded synthetic dedicated PG, session secret and external provider fixture3101.",
    "Only external provider authorization document/HTTP boundary is simulated. BFF creates real attempt/state; actual browser top-level callback crosses TLS and real session/PG, asserts safe303 and native page/attempt. Generic relative middleware denial resolves to HTTPS and must remain allowed, not rewritten for test.",
    "Same-file child flag prevents recursion. Parent owns health/readiness, child/frontdoor/cert lifetime and awaited cleanup. Child never migrates/resets shared DB. Bind only loopback; deny unlisted external fixture calls.",
    "Use per-spec HTTPS context/cert-error exception without changing global Playwright config; document that ephemeral cert trust itself is not production trust proof. To claim Secure-cookie behavior, use explicit child-only production/None cookie configuration and observe native cookie, not fake/injected session.",
    "Verify actual HTTPS served bundle/source/child compiled backend freshness and real API/PG effects. Existing global HTTP freshness is insufficient for new child by itself. Keep all WA ordinary/initial/template/onboarding/browser regressions."
  ],
  "next": "After API22 terminal reconciliation, issue exact serialized test-first/source handoffs under admitted paths, then execute canonical browser proof. No current activation/private/tunnel/provider authority."
}

```
