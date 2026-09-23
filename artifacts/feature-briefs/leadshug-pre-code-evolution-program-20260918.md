# LeadsHug — programa de evolução pré-código

**Data:** 2026-09-18

**Estado:** evidência de descoberta; estados vivos pertencem aos registros canônicos vinculados; este brief não autoriza implementação

**Perfil:** Strategic / CTO-Tech-Lead

**Escopo:** Foundation, análise comparativa e modelagem conceitual de canais/atendimento

## Artifact Role

- **Why this brief exists now:** a iniciativa combina evolução de governança, estudo de dois sistemas de referência e possíveis decisões de domínio. Ela ainda é ampla demais para um único TODO tático seguro.
- **What this brief is not:** documentação canônica de módulo, constituição, roadmap, ADR, TODO tático ou autorização para alterar o código do LeadsHug ou dos projetos de referência.

## ST-01 canonical handoff

The completed ST-01 tactical contract and its delivery evidence live only in [the governing TODO](../../todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md). Its canonical targets are [evolution_lifecycle.md](../../evolution_lifecycle.md), [the backlog](../../backlog/README.md), [system_roadmap.md](../../system_roadmap.md), and [decisions](../../decisions/README.md). Candidate dispositions and next gates live only in the backlog. This brief remains discovery evidence and intentionally does not restate any live state.

## Source Idea / Request

- Evoluir `foundation_documentation` para tornar a evolução do produto mais previsível ao longo do tempo.
- Comparar o LeadsHug com `Central-Whatsapp`, projeto que serviu de inspiração e continuou evoluindo depois da transposição.
- Estudar o modelo de canais e formas de atendimento do `whatsflow_v2`, aproveitando conceitos úteis sem herdar sua desorganização ou dívida sistêmica.

## Problem / Desired Outcome

- **Problem:** a Foundation atual define autoridade, quatro fases de roadmap, módulos e execução por TODO, mas ainda não oferece uma visão suficientemente explícita de capacidades, maturidade, dependências, decisões pendentes e sequência provável de evolução. Ao mesmo tempo, os dois sistemas de referência contêm capacidades e lições úteis que ainda não foram traduzidas para problemas e contratos próprios do LeadsHug.
- **Desired outcome:** obter um sistema documental previsível e uma fila de decisões fundamentada em evidências, na qual cada evolução candidata tenha origem, valor, aderência ao domínio, dependências, riscos, estado e próximo passo visíveis antes de virar implementação.
- **Why now:** o usuário quer concluir essa preparação antes de iniciar novas features internas; isso reduz retrabalho e evita transportar conceitos ou código legado sem uma decisão arquitetural do LeadsHug.

## Constraints / Non-Goals

- **Constraints:**
  - Os projetos `Central-Whatsapp` e `whatsflow_v2` são referências somente leitura; nenhum código, schema, segredo, configuração ou infraestrutura será copiado, sincronizado ou alterado.
  - Toda observação útil deve ser reformulada como problema, capacidade ou hipótese pertencente ao LeadsHug.
  - A arquitetura vigente continua sendo NestJS/React/PostgreSQL/Prisma, com providers tratados como adapters.
  - A Mantenedora, a BU/número, o isolamento multi-tenant, a conversa única por BU e contato e as regras de auditoria permanecem restrições de projeto.
  - Segredos ou credenciais encontrados nos legados não são evidência publicável e não devem aparecer em artefatos.
  - Trabalho de documentação não autoriza mudança de código do produto.
- **Non-goals:**
  - Executar agora qualquer feature identificada nos projetos de referência.
  - Buscar paridade integral com qualquer legado.
  - Fazer diff ou port mecânico de arquivos entre stacks distintas.
  - Declarar o modelo de atendimento do `whatsflow_v2` como arquitetura-alvo antes da resolução das ambiguidades de domínio.
  - Misturar o encerramento dos três TODOs ativos atuais com este programa.

## Canonical Touchpoints

- **Constitution impact:** possible — pode ser necessário formalizar o ciclo ideia → descoberta → decisão → roadmap/backlog → TODO aprovado → evidência, além da fronteira de referências legadas.
- **Roadmap impact:** yes — as fases atuais precisam ganhar resultados verificáveis, dependências, maturidade e horizonte sem virar autorização automática de implementação.
- **Primary module candidates:** `foundation_documentation/modules/integrations-and-channels.md`, `foundation_documentation/modules/inbox-and-conversations.md`
- **Secondary module candidates:** `foundation_documentation/modules/identity-and-tenancy.md`, `foundation_documentation/modules/audit-and-history.md`

## Evidence / References

- Foundation atual: `README.md`, `project_constitution.md`, `domain_entities.md`, `system_roadmap.md`, `modules/`, `contracts/` e `todos/`.
- Verdade arquitetural: `artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md`.
- Fronteira de inspiração: `policies/central_whatsapp_independent_legacy_policy.md`.
- Estado funcional atual: `artifacts/analysis/leadshug-executive-system-dossier-20260915.md` e `artifacts/analysis/leadshug-system-analysis-20260915.md`.
- Referência Central oficial: `C:\Unifast\LeadsHug\Inspirações LeadsHug\Central-Whatsapp\api-oficial`.
- Referência Central não oficial: `C:\Unifast\LeadsHug\Inspirações LeadsHug\Central-Whatsapp\hub-whatsapp`.
- Referência de canais/atendimento: `C:\Unifast\LeadsHug\Inspirações LeadsHug\whatsflow_v2`.

## Findings From Initial Reconnaissance

### Foundation

- O roadmap possui quatro fases amplas, mas não explicita resultados de saída, dependências, estado, horizonte ou vínculo com capacidades.
- Os documentos de módulo registram ownership e poucas invariantes, mas ainda não expõem mapa de capacidades, contratos locais, maturidade, lacunas, decisões e integrações dependentes.
- `contracts/` contém apenas a regra de documentação futura; não há catálogo navegável de contratos atuais.
- A constituição menciona backlog para ideias não aprovadas, porém não há hoje uma superfície de backlog presente na árvore verificada.
- Não existe ainda um índice explícito de decisões/ADRs nem uma cadeia navegável entre descoberta, decisão, roadmap, TODO e evidência.

Esses achados apontam para uma evolução de arquitetura da informação, não apenas para escrever mais documentos.

### Central-Whatsapp

Na janela observada desde 2026-08-17, os dois repositórios somam 188 commits não-merge. A comparação deve, portanto, ser por capacidade e comportamento, não por arquivo. Os principais grupos candidatos ao estudo são:

- API pública de conversas, auditoria e templates;
- ownership, transferência, consulta e exportação de atendimentos;
- anexos, normalização de áudio e estados de entrega/leitura/falha;
- importação, status e mídia de templates Meta;
- relatórios, filtros, custos de disparo e exportação;
- funis e cards de CRM originados da conversa;
- Agente IA e escolha entre equipe e automação;
- Embedded Signup e autoconexão do número oficial;
- grupos, comunidades, agrupamentos reutilizáveis e agendamentos no transporte não oficial;
- permissões específicas para números e integrações.

O inventário deverá classificar cada item como `já existe`, `parcial`, `ausente`, `não desejado` ou `incerto`, sempre com valor, risco, dependências e evidência.

### whatsflow_v2 — canais e atendimento

A evidência inicial mostra camadas distintas:

1. **Conexão/provedor:** `whatsapp_instances` para uazapi e `channel_integrations` para Meta, resolvidos por adapters comuns de envio.
2. **Entrada operacional:** conversas entram em uma inbox/fila unificada, independentemente do transporte.
3. **Especialização:** `departments` representa o tipo de demanda; uma instância de WhatsApp pode apontar para um departamento.
4. **Cobertura humana:** `agent_departments` permite que um atendente cubra vários departamentos.
5. **Distribuição:** cada departamento seleciona `round_robin`, `least_busy` ou `manual`, considerando presença e `max_conversations`.
6. **Ciclo do atendimento:** uma conversa pode ser assumida, atribuída, transferida entre atendentes/setores, finalizada e acompanhada por SLA.

Isso não comprova literalmente uma relação “um canal possui várias formas de atendimento”. No modelo encontrado, a instância aponta para no máximo um departamento, enquanto a multiplicidade aparece nos atendentes, nas estratégias de distribuição e nos caminhos manual, automático, transferência e automação. Essa diferença precisa ser resolvida antes de desenhar o domínio do LeadsHug.

Também há alertas que devem virar lições negativas: duplicação entre tabelas de provedores, cutovers incompletos, referências por nomes externos, migrações corretivas tardias, histórico de controles de acesso frágeis e funcionalidades documentadas como parciais.

### Colisão de vocabulário

No LeadsHug, **Setor** é hoje o agrupamento operacional de números dentro de uma Mantenedora e **BU** é o número/unidade mínima de permissão, histórico e atendimento. No `whatsflow_v2`, **department/setor** agrupa atendentes especializados e participa do roteamento de conversas. Importar o mesmo nome sem decisão criaria uma colisão semântica.

Uma hipótese de trabalho, ainda não canônica, é separar:

`conexão/adaptador de transporte → BU/número → fila ou unidade de atendimento → política de roteamento → sessão/atribuição`

O estudo deve validar se “fila”, “equipe”, “mesa de atendimento” ou outro termo representa melhor essa unidade sem redefinir silenciosamente o Setor atual.

## Ambiguities To Resolve Before TODO

| ID | Ambiguity | Why It Matters | Current Evidence | Handling (`resolve now\|carry as TODO assumption\|block`) |
| --- | --- | --- | --- | --- |
| `AMB-01` | O que exatamente significa “um canal pode ter várias formas de atendimento”: várias equipes, regras de distribuição, modalidades humana/IA, filas, turnos ou combinações dessas opções? | Muda cardinalidades, vocabulário e ownership dos módulos. | O `whatsflow_v2` separa conexão, departamento, atendente, distribuição e transferência, mas não implementa tudo como uma única relação canal → formas. | `resolve now` antes do TODO de arquitetura de atendimento |
| `AMB-02` | O Setor atual do LeadsHug deve continuar agrupando BUs ou também representar especialização de atendimento? | Reusar o termo pode quebrar o modelo de autorização e a unidade mínima de histórico. | `domain_entities.md` e os módulos atuais dão ao Setor e à BU significados distintos do legado. | `block` para qualquer mudança de domínio; não bloqueia os estudos |
| `AMB-03` | Qual horizonte a Foundation deve representar: sequência estratégica sem datas, quarters, releases ou marcos por capacidade? | Determina o formato do roadmap e o nível de compromisso comunicado. | O roadmap atual possui fases sem horizonte ou estado. | `resolve now` na story de Foundation |
| `AMB-04` | Qual será a superfície canônica de ideias ainda não aprovadas: backlog, opportunity catalog ou capability gaps? | Sem isso, descobertas tendem a virar TODO ativo cedo demais. | A constituição menciona backlog, mas a árvore atual não possui essa superfície. | `resolve now` na story de Foundation |
| `AMB-05` | A política de referência independente deve ser generalizada para incluir explicitamente `whatsflow_v2`? | Evita que uma análise futura seja interpretada como permissão de copiar ou acoplar. | A política atual nomeia apenas Central-Whatsapp. | `carry as TODO assumption` no trabalho de Foundation |
| `AMB-06` | Qual data ou baseline funcional representa o momento da transposição do Central para o LeadsHug? | Necessária para distinguir evolução posterior de capacidade já transportada. | A inspeção inicial usou 2026-08-17 apenas como janela operacional, não como baseline comprovado. | `resolve now` no estudo comparativo |

## Story Decomposition

Cada linha abaixo deve virar, no máximo, um TODO tático próprio. Nenhum TODO deve cobrir o programa inteiro.

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Canonical handoff (live status elsewhere) | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ST-01` | Definir a arquitetura da informação e o modelo de previsibilidade da Foundation. | Foundation/governança | todos os módulos | Taxonomia, estados, horizontes, dependências, registro de decisões e rastreabilidade são propostos e validados sem alterar código do produto. | Auditoria cruzada da navegação e simulação de uma ideia atravessando todo o lifecycle. | [Governing ST-01 TODO](../../todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md) | Resolver `AMB-03` e `AMB-04`. | Primeira entrega recomendada, pois define onde os estudos seguintes serão registrados. |
| `ST-02` | Produzir um catálogo de diferenças de capacidade entre LeadsHug e Central-Whatsapp. | integrations-and-channels | inbox-and-conversations, audit-and-history, futuro CRM | Cada capacidade relevante tem evidência, estado no LeadsHug, valor, risco, dependência e disposição; nenhum código é portado. | Amostragem bidirecional entre catálogo, código/documentação dos três produtos e arquitetura vigente. | [`BLG-central-whatsapp-capability-study`](../../backlog/README.md) | Determinar baseline de comparação (`AMB-06`). | Dividir em oficial, não oficial e capacidades transversais se o inventário ultrapassar um TODO manejável. |
| `ST-03` | Modelar conceitualmente canais, filas/equipes e formas de atendimento a partir das lições do whatsflow_v2. | inbox-and-conversations | integrations-and-channels, identity-and-tenancy, audit-and-history | Diagrama conceitual, cardinalidades, vocabulário, invariantes, estados, roteamento, autorização e anti-padrões são documentados; nenhuma decisão é silenciosamente canonizada. | Cenários de entrada, atribuição, capacidade, transferência, SLA, múltiplas BUs e isolamento entre Mantenedoras. | [`BLG-whatsflow-channel-attendance-study`](../../backlog/README.md) | Resolver `AMB-01` e, antes de canonizar, `AMB-02`. | Deve separar inspiração útil de dívida observada. |
| `ST-04` | Sintetizar os estudos em mapa de capacidades, decisões e sequência de evolução do LeadsHug. | system roadmap | módulos e contracts | O roadmap passa a apontar para capacidades e decisões priorizadas, com dependências e critérios de saída; candidatos não aprovados permanecem fora de `todos/active/`. | Revisão de rastreabilidade: cada prioridade volta à evidência e avança para um TODO apenas quando aprovada. | [`BLG-leadshug-evolution-synthesis`](../../backlog/README.md) | Depende de `ST-01`, `ST-02` e `ST-03`. | É a convergência do programa, não uma implementação de produto. |

## Historical Recommended Sequence

The sequence below is retained as discovery provenance, not as live disposition or execution authority. Consult [the canonical backlog](../../backlog/README.md) for current candidate state and next gates.

1. Executar `ST-01` para criar a estrutura documental que receberá os resultados sem transformar descoberta em autoridade prematura.
2. Executar `ST-02` e `ST-03` como estudos independentes e comparáveis.
3. Validar com o usuário o vocabulário e as escolhas de produto encontradas.
4. Executar `ST-04` para atualizar superfícies canônicas e propor a ordem dos futuros TODOs de implementação.
5. Somente depois aprovar TODOs de produto, um recorte executável por vez.

## Retire This Brief When

- As quatro stories tiverem disposição explícita, os estudos tiverem sido absorvidos pelas superfícies canônicas e nenhuma ambiguidade viva depender mais deste artefato.
