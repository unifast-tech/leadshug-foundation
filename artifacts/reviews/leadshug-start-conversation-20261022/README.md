# ST-CON-04 v1.1 — início manual de conversa: implementação em andamento

[Contrato ativo](../../../todos/active/features/TODO-leadshug-start-conversation-by-contact.md). Estado atual: InProgress / Pending / implementation, após APROVADO explícito do usuário. A entrega completa ainda depende dos testes e gates registrados no contrato. As seções de planejamento preservam o histórico anterior à aprovação.

O vendedor informará telefone com DDI, abrirá ou reutilizará a conversa, escolherá o canal, conferirá texto/modelo e confirmará o primeiro envio. O canal oficial utilizará um modelo elegível realmente aprovado quando necessário. Haverá recuperação local após falha, sem reenvio automático nem troca automática de canal. O mesmo Channel abstrato e os owners existentes de envio, aceitação de Message e catálogo serão preservados.

## Revisões e verificações de planejamento

- Arquitetura r1: recomenda uma operação discriminada de envio; quatro findings integrados em [resolução](architecture-r1-resolution.md).
- Crítica r1: duas clarificações integradas em [resolução](critique-r1-resolution.md): prazo de acknowledgment e automação após abertura manual.
- [Crítica r2](evidence/critique-r2.merge.json): sem novos findings materiais; elegância, estrutura e operação aceitáveis para planejamento. Performance mista e ainda não medida.
- [Coerência com código](assumption-code-observations-v1.1.md): oito premissas rechecadas após as revisões; [guard GO](evidence/assumption-code-coherence-v1.1.json).
- [Escopo](evidence/review-scope-drift-v1.2.json):23 seções, zero mudanças materiais contra o freeze publicado a107a6ab. v1.1 conserva falha inicial de casing do adaptador Git, resolvida sem alterar guard/produto.
- [Authority preapproval](evidence/authority-preapproval-v1.1.json): preflight-go; execution_authority_granted=false.

Freeze inicial b7dfb212 antecede os primeiros guards/review; ef1ff014 publica integrações arquiteturais; a107a6ab publica as duas clarificações antes da crítica r2. Histórico19/20 é preservado e não equivale a revisão atual.

## Limites preservados

No encerramento do planejamento, as68 fontes públicas herdadas e o owner de aceitação suplementar mantinham seus bytes, sem alteração de produto. Essa afirmação é histórica: a execução autorizada abaixo já contém alterações de produto, e E02 registra o desvio de descoberta. Foundation main continua sendo a única publicação Git autorizada. [Recibo primário da Meta](evidence/meta-primary-reference-receipt-v1.1.json) prova apenas o contrato externo documentado. O enum de aprovação do modelo próprio e a saúde atual do runtime continuam desconhecidos.

Após aprovação: implementação test-first, testes de contrato/PG e navegador real, assurance e migração local autorizada; depois prova assistida pelos canais próprios. No encerramento do planejamento, nenhum teste de implementação04 havia sido executado; os checkpoints de execução abaixo registram as rodadas posteriores. As limitações SEC-R6-04, OPS-R4-01 e TQA-ST05-03 seguem com seus owners; não são corrigidas por este plano. Produto/Railway/promoção continuam fora do escopo atual.

## Execução autorizada — 2026-10-22

O usuário respondeu APROVADO para v1.1; [admissão](evidence/approval-execution-admission-v1.1.json) e [authority normal GO](evidence/authority-execution-admission-v1.2.json) registram execução autorizada, com perfil Operational/Coder e um executor de produto. O estado atual é InProgress/Pending/implementation. Seções anteriores de “aguarda aprovação” descrevem o encerramento do planejamento; não são o estado atual. As69 fontes herdadas foram conferidas antes da primeira edição. [Desvio procedural E02](evidence/execution-discovery-deviation-e02-v1.1.json) registra busca ampla inicial do executor, resultado de travessia desconhecido e contenção; não se afirma conformidade integral de privacidade desta execução. Primeira rodada RED por ausência dos novos módulos está [registrada](evidence/executor-red-e03-v1.1.json); nenhuma entrega04 GREEN ou prova real é reivindicada.

## Checkpoint E05 — API GREEN parcial

A primeira camada passou no runner canônico:303 testes unitários e398 testes E2E PostgreSQL, além de lint/build/migrations. [Recibo e limites](evidence/executor-phase1-green-e05-v1.1.json). Abertura ainda tem prova mock-based e a política de janela ainda precisa de integração. A execução04 continua em andamento pelo mesmo executor; não há entrega completa, prova de navegador ou envio real nesta etapa. E02 e a cronologia causal E04 continuam válidos para assurance independente.

## Checkpoints E06–E13 — execução parcial e limites

Abertura/reuso com PostgreSQL e a persistência de data qualificada passaram em cenários específicos. A rodada mais recente teve308 testes unitários aprovados, mas a API completa continua RED: há ajustes de fixtures e um ECONNRESET no novo stress20×5. A revisão também exige correções do protocolo inicial real (conta explícita, fence, DTO e certeza do ACK), que o cliente simulado não prova. [Último recibo](evidence/transport-unit-and-bci-e13-v1.1.json). [Proposta de duas fixtures protegidas](window-fixture-companion-admission-v1.1.md) aguarda validação do usuário. A saga/admissão, interface, assurance e prova assistida permanecem pendentes. Nenhuma entrega04 completa é reivindicada.

## Checkpoint E14 — concorrência de abertura e protocolo

A rodada seguinte passou em311 testes unitários e399 testes PostgreSQL; restam seis falhas nas duas fixtures protegidas, aguardando validação. O stress de abertura passou com100 solicitações:5 criações,95 reusos, uma conversa por contato e nenhum envio ao provedor. Os três testes diretos de protocolo passaram, sem reivindicar RED causal anterior para eles. [Recibo E14](evidence/transport-and-open-e14-v1.1.json). Admissão e tentativa duráveis seguem em implementação; não há entrega04 completa.

## Checkpoint E23 — validação humana das fixtures e modelo aprovado

O usuário validou os dois ajustes exatos de fixtures e informou que o modelo criado já está aprovado. [Recibo E23](evidence/fixture-validation-and-asset-e23-v1.1.json) e [authority GO](evidence/authority-fixture-companion-e23-v1.1.json). Aplicação do patch e provas automatizadas ainda serão registradas; a aprovação do modelo foi informada pelo usuário e será conferida na conta/recurso selecionado antes da prova assistida. Menções anteriores a “aguarda validação” ou “enum desconhecido” descrevem checkpoints anteriores, sem autorização ou sucesso retroativos. Backend completo, interface e provas finais seguem em andamento.

## Checkpoint E33 — API completa passa; entrega em andamento

O patch exato das duas fixtures foi aplicado e passou nas rodadas seguintes. A rodada E33 passou em336 testes unitários e416 testes de integração PostgreSQL, além de lint/build e migrações descartáveis; os256 arquivos públicos permaneceram idênticos durante a execução. [Recibo E33](evidence/api-bff-result-e33-v1.1.json). Os fluxos BFF de primeiro texto, modelos NAMED/POSITIONAL e recuperação após aceitação conhecida passaram. O teste protegido de sessão passou sem alteração; a causa do401 observado em E32 permanece desconhecida.

O estado continua InProgress/Pending/implementation. Ainda faltam a matriz completa de falhas/concorrência, provas de isolamento e orçamento, SQL/schema, a interface e o navegador real, assurance e a prova assistida pelos canais próprios. Os checkpoints anteriores são históricos; E33 não conclui ST-CON-04 nem autoriza promoção de produto. Os desvios E02/E04/E18 e a incompatibilidade do diff guard com a fronteira privada continuam registrados.

## Checkpoint E34 — confirmação perdida, rollback e concorrência

A API ampliada passou em339 testes unitários e428 de integração, com257 arquivos públicos idênticos antes/depois da execução. [Recibo E34](evidence/api-bff-result-e34-v1.1.json). Os novos casos distinguem commit confirmado no banco com confirmação perdida e rollback real, exercitam conflito P2002 com eco concorrente, preservação de atendimento assumido/encerrado, isolamento de empresa, perda de sessão/permissão durante preflight, limites de tentativas e recuperação por outro ator autorizado. O plano de consulta usa o índice aditivo de ordenação da inbox. Há limites explícitos de prova e de cronologia dos testes no recibo. A interface completa, navegador real, negativas restantes, schema e gates finais continuam em andamento; não há entrega04 nem teste de provedor real concluído neste checkpoint.

## Checkpoint E35 — lacuna de interface confirmada no navegador

O navegador passou em75 testes existentes. O teste novo abriu a conversa pelo BFF real, confirmou estado vazio sem envio e falhou somente ao exigir o formulário de primeira mensagem, ainda ausente. Os258 arquivos públicos permaneceram idênticos durante a rodada. [Recibo E35](evidence/browser-result-e35-v1.1.json). A interface completa segue em implementação após esse RED causal; a asserção posterior de ausência do composer comum não chegou a executar. Não há conclusão04 ou nova prova de provedor real neste checkpoint.

## Checkpoint E36 — interface compila e testes unitários passam

A interface compilou em TypeScript/Vite e passou em49 testes unitários de7 arquivos; os259 arquivos públicos permaneceram idênticos durante a execução. [Recibo E36](evidence/web-result-e36-v1.1.json). Esse modo não executa Playwright, API/PostgreSQL ou o protocolo simulado. A matriz de navegador e as provas restantes seguem em preparação para a rodada completa; não há conclusão04 neste checkpoint.

## Checkpoint E37 — retomada compila; navegador completo ainda pendente

O novo estado de retomada compilou e a suíte Web passou em51 testes unitários; os259 arquivos públicos ficaram idênticos durante a rodada. [Recibo E37](evidence/web-result-e37-v1.1.json). Esse resultado não executa a persistência/replay no navegador, API/PostgreSQL ou as novas negativas de protocolo. Essas provas seguem para o candidato completo. A [proposta de exceção de inspeção do diff guard](evidence/final-diff-guard-boundary-proposal-v1.1.json) permanece apenas proposta, sem autorização de inspeção privada ou GO do guard.

## Checkpoint E38 — rodada completa parou na integração

A API passou em353 testes unitários e429 de integração; quatro casos de integração falharam e impediram a execução Web/navegador nessa rodada. Os259 arquivos públicos ficaram idênticos durante a execução. [Recibo E38](evidence/all-result-e38-v1.1.json) registra causas, limites e as provas individuais que passaram (incluindo5ondas×20 submits sem duplicação). O executor corrige as falhas específicas antes de novo candidato; não há entrega04 ou API/all GREEN deste checkpoint.

## Checkpoint E39 — consultas e schema passam; uma expectativa restante

A rodada passou em353 testes unitários e432 de integração. Restou uma expectativa de código de erro no primeiro caso de modelo pausado; os casos negativos seguintes da mesma sequência não executaram. A instrumentação SQL real, as verificações restritas de schema e o teste de confirmação de risco passaram. [Recibo E39](evidence/all-result-e39-v1.1.json). Os259 arquivos públicos permaneceram idênticos durante a execução; Web/navegador ainda não foram alcançados. O estado continua InProgress/Pending/implementation.

## Checkpoint E40 — isolamento dos usuários de teste

A rodada passou em353 testes unitários e432 de integração. A sequência de negativas atingiu o limite real de10 tentativas/minuto do mesmo ator antes de alcançar a recusa de modelo pretendida. [Recibo E40](evidence/all-result-e40-v1.1.json). Os cenários serão isolados por usuários autorizados distintos; os limites do produto permanecem iguais. Web/navegador e a falha de armazenamento seguem sem execução nessa rodada. [Índice preliminar por critério](evidence/candidate-criterion-index-e40-v1.1.json) e [plano futuro de ativação local](evidence/local-activation-proof-plan-proposal-v1.1.json) não declaram conclusão ou autorização de runtime/inspeção privada.
