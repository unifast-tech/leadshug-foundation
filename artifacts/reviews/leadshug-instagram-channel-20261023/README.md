# Instagram Direct — pacote para aprovação

Contrato v1.3 pronto para decisão humana em2026-10-23. Este índice reúne a preparação e as revisões; a autoridade de escopo é o [TODO ST-IG-03](../../../todos/active/features/TODO-leadshug-instagram-channel.md). Nenhum código, banco, serviço ou configuração Meta foi alterado nesta preparação.

A primeira entrega conecta uma conta profissional com login do Instagram à BU, recebe DM textual iniciada pelo contato e permite resposta humana pela conta e rota corretas, usando Channel e os owners comuns de envio/aceitação. A BU pode reunir WhatsApp e várias contas Instagram com os mesmos grants. Nesta fatia, permanece um recurso empresarial WhatsApp por BU, compartilhado pelos adapters comprovados oficial/não oficial.

A implementação inclui identidade qualificada, ownership durável, contexto de rota, preservação dos dados e envios pendentes, testes PostgreSQL/concorrência/browser e regressão WhatsApp. Consultar e CSV por telefone permanecem WhatsApp-only. Mídia, histórico Instagram, merge, bots Instagram, campanhas e outros canais ficam para contratos próprios.

As revisões independentes encerraram sem achado material pendente:

- [Arquitetura r2 — go](evidence/architecture-r2-result.json).
- [Crítica r2 e sete lentes — go](evidence/critique-r2-result.json).
- [Coerência com código — go](evidence/assumption-code-guard-r4.json), apoiada na [leitura manual delimitada](evidence/assumption-code-manual-r4.json).
- [Escopo — go, zero seções materiais alteradas](evidence/review-scope-guard-r4.json).
- [Authority — preflight-go](evidence/authority-preflight-final-r4.json), sem autoridade de execução.

A baseline revisada é [f4891ba1](evidence/review-baseline-freeze-r4.json). Os pareceres anteriores e suas correções permanecem no diretório de evidências. Permissões reais, configuração Meta, rollout local, DM/resposta físicas e retomada são provas futuras sob plano runtime próprio. Não há resultado de teste de implementação Instagram nesta preparação.

Próxima ação: APROVADO explícito do TODO v1.3, seguido de registro de aprovação, ingestão das regras e authority normal go antes da implementação. Aprovação de código não concede a exceção de arquivos privados nem autoriza rollout, produção, App Review ou Git de produto.
