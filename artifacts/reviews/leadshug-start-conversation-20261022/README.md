# ST-CON-04 v1.1 — início manual de conversa: plano pronto para aprovação

[Contrato ativo](../../../todos/active/features/TODO-leadshug-start-conversation-by-contact.md). Estado: NotStarted / Pending / review. A implementação depende de APROVADO explícito deste novo contrato; a autorização das etapas05/06 não se transfere.

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

As68 fontes públicas herdadas e o owner de aceitação suplementar mantêm seus bytes; não houve alteração de produto nem consulta/alteração de ambiente privado, dados de negócio, runtime, conta/provedor ou credencial. Foundation main é a única publicação. [Recibo primário da Meta](evidence/meta-primary-reference-receipt-v1.1.json) prova apenas o contrato externo documentado. O enum de aprovação do modelo próprio e a saúde atual do runtime continuam desconhecidos.

Após aprovação: implementação test-first, testes de contrato/PG e navegador real, assurance e migração local autorizada; depois prova assistida pelos canais próprios. Nenhum teste de implementação04 foi executado. As limitações SEC-R6-04, OPS-R4-01 e TQA-ST05-03 seguem com seus owners; não são corrigidas por este plano. Produto/Railway/promoção continuam fora do escopo atual.

## Execução autorizada — 2026-10-22

O usuário respondeu APROVADO para v1.1; [admissão](evidence/approval-execution-admission-v1.1.json) e [authority normal GO](evidence/authority-execution-admission-v1.2.json) registram execução autorizada, com perfil Operational/Coder e um executor de produto. O estado atual é InProgress/Pending/implementation. Seções anteriores de “aguarda aprovação” descrevem o encerramento do planejamento; não são o estado atual. As69 fontes herdadas foram conferidas antes da primeira edição. [Desvio procedural E02](evidence/execution-discovery-deviation-e02-v1.1.json) registra busca ampla inicial do executor, resultado de travessia desconhecido e contenção; não se afirma conformidade integral de privacidade desta execução. Primeira rodada RED por ausência dos novos módulos está [registrada](evidence/executor-red-e03-v1.1.json); nenhuma entrega04 GREEN ou prova real é reivindicada.
