# ST-CON-06 — crítica independente e resolução

Data cliente2026-10-20. Fresh no-context reviewer `/root/stcon06_critique`, gpt-6.1-sol/max, formal-review/formal-reviewer/critique routing go em evidence/routing-critique.json. Pacote completo679 linhas + fontes públicas/canon/arquitetura/risco/producer-consumer/evidências planejadas. Baseline origin/main81d56f5e60a6ec99a996dfb3ba51987c4f009849 publicada antes do dispatch. Sem edição/testes/runtime/account calls/paths privados pelo reviewer; acesso público à documentação Meta falhou.

**Primeiro parecer terminal: no-go até CR01.** AR01..04 substancialmente integrados; extensão, scoped resolver, todos senders, autoria/claim, fake opaco e limites de durabilidade considerados coerentes. Nenhum resultado de implementação certificado.

| ID / severidade | Achado / fonte | Resolução pelo owner antes da reconvergência |
| --- | --- | --- |
| CR-01 medium/blocking | D03 exige409 quando contexto muda sem ID; D05 podia mapear a falha do fence de recordAmbiguousOutbound a503. Fonte message-acceptance.service.ts:179 | Integrated: D05 e baseline dão precedência explícita à mudança detectada identity/generation/epoch:409 CHANNEL_CONTEXT_CHANGED/outcome UNKNOWN, sem novo contexto. Outras falhas/commit incerto do diagnóstico503 UNKNOWN; ACK válido mantém ACCEPTED_LOCAL_INCOMPLETE. Metadado de persistência exige evidência positiva. Plano step2 exige barreiras antes do diagnóstico/durante fence/falha ordinária, um POST/no replay |
| CR-02 low/nonblocking | Final Review Gate apontava método de test-quality | Integrated: Canonical method corrigido para wf-docker-independent-final-review-method; TQA mantém método próprio |

Lentes do reviewer: performance condicionalmente aceitável (metadata da BU reutilizada, um POST, GET sem probe; medição EPS/BCI/FRC futura); elegance favorável; structural soundness favorável apósCR01; security/operational fit favoráveis com autenticações separadas, provenance trusted, segredo privado, runner fixfirst/all/PG/browserfresco/INOUT assistida.

Residuais aceitos no planejamento: corrida leitura local→rede, crash gaps/commit incerto e ausência de intent durável, dedupe null-ID, identidade/ingress de novas redes futuros. A janela temporal atual usa latest IN da conversa sem filtro de transporte; preservar explicitamente e reconvergir trusted timestamps em04. Nenhum resultado de medição, readiness ou produto é alegado.

Reconvergência após publicação do contrato v1.2: pending; mesmo reviewer receberá pacote completo atualizado e deltaCR01/02, sem substituir ou interromper revisão viva.
