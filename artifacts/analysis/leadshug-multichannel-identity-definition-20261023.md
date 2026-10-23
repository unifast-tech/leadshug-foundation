# LeadsHug — Definição de identidade e atendimento multicanal

**Version:** 1.0. **Data:** 2026-10-23. **Perfil:** Strategic / CTO-Tech-Lead. Documento de proposta técnica ST-IG-01, sem autoridade de execução. [Brief de origem](../feature-briefs/leadshug-instagram-channel-20261023.md).

## Direção humana confirmada e limites

O usuário confirmou: **a mesma BU deve reunir WhatsApp e Instagram, com os mesmos vendedores e permissões**. A BU representa a operação de atendimento; número e perfil pertencem às conexões. Há conta profissional Instagram de teste disponível e acesso humano para autorizá-la. A configuração do app Meta e as permissões efetivas ainda não foram verificadas.

Esta proposta detalha identidade, cardinalidade e encaminhamento para essa direção. A decisão de BU operacional foi consolidada como arquitetura alvo no [registro de decisões](../../decisions/leadshug-multichannel-identity-decisions.md); contato, ownership empresarial e rota permanecem propostas técnicas nesse registro. O produto atual continua WhatsApp e não foi migrado; a implementação exige TODO, revisão e aprovação próprios.

## Modelo proposto

| Conceito | Definição e responsabilidade | Exemplo fictício |
| --- | --- | --- |
| Mantenedora | Organização e limite de tenant. | Organização Exemplo |
| Setor | Agrupa BUs para organização e expansão de grants conforme regra existente. | Comercial |
| BU | Operação de atendimento e limite mínimo de permissão e dados, independente de telefone ou plataforma. Pode existir antes de conectar qualquer conta. | Equipe de vendas |
| Conexão de canal | Vínculo configurado de uma BU com uma implementação e um recurso externo autorizado. Tem ID local, estado, geração e referência privada de credencial próprios. | WhatsApp oficial do número A; WhatsApp via Evolution do número A; Instagram da conta B |
| Identidade do recurso de atendimento | Identidade empresarial estável da conta/número atendido, separada da tentativa OAuth, sessão QR, versão de token e namespace de recurso do provedor. Dois adapters podem representar o mesmo número WhatsApp, após comprovação. | Número A; conta profissional B |
| Identidade de recurso do provedor | Identidade técnica e durável usada para ingresso, deduplicação e proveniência em um adapter. Preserva seu namespace e referências históricas; pode apontar para a identidade empresarial comum comprovada. | phoneNumberId Meta; identidade da instância Evolution |
| Contato | Registro local de um interlocutor dentro de uma BU, com ID interno estável. Telefone ou username não são sua chave primária. | Contato C |
| Identidade externa do contato | Referência endereçável e qualificada por plataforma/escopo, associada ao contato local somente a partir de evidência confiável. | Telefone WhatsApp; referência de remetente recebida pela conta Instagram B |
| Conversa | Agregado único BU/contato local, com estado, responsável, mensagens e não lidas. O transporte não cria outra conversa quando a identidade é comprovadamente a mesma. | Conversa da equipe de vendas com C |
| Rota de comunicação | Associação autorizada entre conversa, recurso empresarial, identidade externa destinatária e conexões capazes de atendê-la. É um conceito de endereçamento; a tabela/estrutura física será decidida no contrato de implementação. | Responder pela conta B ao remetente Instagram conhecido |

**Channel permanece a abstração de execução**. A conexão é o vínculo persistido; Channel é o comportamento de envio resolvido por DI. Não usar herança de tabelas para representar a classe abstrata.

## Cardinalidade e propriedade

- Mantenedora tem Setores; Setor tem BUs; cada conexão pertence a exatamente uma BU. Uma BU admite várias conexões, inclusive mais de uma conta da mesma plataforma: o tipo de adapter não identifica um vínculo.
- Dentro do LeadsHug, cada recurso empresarial qualificado tem owner durável único, independente do adapter. A mesma conta Instagram não pertence simultaneamente a duas BUs; o mesmo número WhatsApp não pertence à BU A pelo oficial e à BU B pelo Evolution. Essa regra não declara exclusividade em outros aplicativos externos à plataforma.
- O claim do recurso e sua associação às identidades de provedor precisam ser atômicos e comprovados. Conflito falha sem redirecionar nem revelar outro tenant. Desconectar não libera nem transfere a propriedade automaticamente. A conexão ativa é única por recurso/adapter nesse owner.
- WhatsApp oficial e Evolution do mesmo número podem coexistir na mesma BU como conexões diferentes, com credenciais e proveniências próprias. A identidade empresarial comum exige número comprovado, não similaridade de rótulos ou IDs de provedor.
- A identidade empresarial comum não substitui `ProviderResourceIdentity`: preservar IDs técnicos, ownership e chaves históricas de cada adapter. Compartilhar número, contato ou conversa não une espaços de IDs de mensagem nem permite deduplicar entre provedores por coincidência textual. A deduplicação segue na identidade de provedor comprovada; renovar credencial não cria outra identidade de dedup.
- Credencial pertence à conexão/geração. Reautorizar o mesmo recurso preserva sua identidade e o histórico; trocar o recurso não reutiliza o ID de identidade para representar outra conta.
- Contato, identidades, conversa e rota pertencem à mesma BU. Não haverá cadastro global de pessoas nem busca cruzada de contatos entre BUs neste recorte.

## Identificação do contato e da conversa

1. Autenticar o webhook e resolver sua conexão/recurso com ownership vigente antes de processar contato ou texto. Um payload ou parâmetro do browser não escolhe tenant/BU.
2. O adapter normaliza a identidade externa, preservando seu namespace. O domínio recebe referências tipadas/opacas, não um campo que significa ora telefone, ora username.
3. No WhatsApp, a identidade de pessoa usa plataforma WhatsApp e telefone normalizado no escopo da BU; oficial/não oficial não são plataformas de pessoa distintas. Identidade de grupo usa namespace próprio e não colide com pessoa. Não inventar país na entrada manual.
4. No Instagram, qualificar a referência do remetente pelo contexto autorizado do app/API e pela identidade estável da conta profissional atendida. Username/nome são metadados de exibição; não são endereço de envio nem prova de identidade. IDs numéricos são strings opacas, sem E.164 ou conversão para número JavaScript.
5. Se a identidade qualificada já existe na BU, reutilizar seu contato/conversa. Caso contrário, criar contato e conversa locais em transação com proteção de unicidade/concorrência.
6. Mesmo nome ou telefone declarado no perfil não une Instagram com WhatsApp. Na primeira entrega, cada identidade nova gera seu próprio contato; os dois transportes WhatsApp comprovados reutilizam o mesmo contato. Associação manual/verificada entre plataformas fica para contrato próprio; não construir merge nesta fatia.
7. Uma futura associação de duas identidades ao mesmo contato exigirá conciliar duas conversas potencialmente existentes, permissões e histórico. A possibilidade arquitetural não entrega essa operação nem autoriza sobrescrever uma conversa atual.

Com isso, uma lista unificada de Atendimento mostra conversas WhatsApp e Instagram da mesma BU, com origem legível, sem afirmar que contatos semelhantes são a mesma pessoa.

## Resposta pelo vínculo correto

- Toda mensagem conserva conexão, recurso empresarial, identidade destinatária, origem, ID externo e contexto de geração. Autoria humana continua separada do transporte e do echo.
- Ao abrir o compositor para responder, o backend resolve a rota da interação selecionada. A requisição de envio captura a referência e a versão esperada; não escolhe apenas pelo enum da plataforma nem pelo primeiro canal pronto da BU.
- Se houver mais de uma rota válida e não houver interação selecionada, exigir escolha explícita. Entrada concorrente por outra rota não muda silenciosamente conta ou destinatário do rascunho. Contexto obsoleto é recusado/atualizado antes do envio.
- Revalidar grant, vínculo, recurso, credencial e política no limite final de dispatch. Capturar a decisão para reconciliação local; nenhuma recuperação de envio incerto repete HTTP automaticamente.
- Responder à DM usa Instagram; não tentar WhatsApp se a conexão Instagram estiver indisponível. A identidade Instagram não fornece telefone. Escolher outro canal exige identidade conhecida e ação explícita, fora do percurso inicial.
- Oficial/não oficial do mesmo número seguem compartilhando a conversa, mas mantêm seleção e política próprias. Não criar fallback automático entre eles; respeitar a seleção capturada e a autorização do contexto atual.

## Dependências e capacidades

```text
Atendimento / envio comum
        → ChannelResolver (escopo + rota + política)
        → Channel.sendMessage
        → implementação registrada
            WhatsApp oficial | Evolution | Instagram
```

- Registro/composição conhece implementações; consumidores comuns não importam cliente Instagram/Meta/Evolution, não fazem cast para o concreto e não montam URLs de provedor.
- O payload comum de texto usa referência de destinatário resolvida. Cada implementação declara os tipos de mensagem suportados e respeita o mesmo contrato de aceito, bloqueado, recusado e incerto.
- A política de elegibilidade é resolvida por conexão/capacidade. O atual booleano de janela e a política oficial WhatsApp não provam suporte à janela Instagram. Não criar condicionais de plataforma espalhadas no domínio.
- Cadastro/OAuth, renovação de credencial, templates WhatsApp e importação histórica são capacidades separadas do envio. Nenhum adapter deve implementar métodos fictícios para operações não suportadas.
- Não habilitar bots automaticamente ao ligar Instagram. Contrato de automações e sessões precisa incluir identidade qualificada, rota e capacidade/política; na primeira prova o atendimento é humano.

## Alternativas avaliadas

| Opção | Benefício | Custo, risco e decisão |
| --- | --- | --- |
| A — BU representa a operação, com conexões e identidades separadas | mesma equipe/grants atende canais diferentes; suporta crescimento sem número fictício | exige evolução explícita de identidade, seleção, cadastro e consumidores. Direção escolhida pelo usuário; desenho técnico recomendado. |
| B — uma BU obrigatória por número/perfil | preserva separação simples dos destinos | fragmenta grants e operação; não atende à escolha humana de reunir canais. Não recomendada. |
| C — preservar BU=WhatsApp e guardar Instagram como telefone sintético | evita enfrentar parte do contrato atual | cria colisões, validação falsa e dependência escondida; não aceitável. |

O custo de A é cross-module, com migrações e regressão dos consumidores. Não ampliar junto CRM, merge de pessoas, campanhas ou uma plataforma genérica de plugins. Contato/identidade/rota são responsabilidades necessárias, não autorização para camadas sem uso.

## Coerência com o código atual

| Evidência pública delimitada | Consequência para o futuro contrato |
| --- | --- |
| `api-app/prisma/schema.prisma`: BusinessUnit.phone; ChannelType; unique BuChannel(buId,type) | telefone deixa de definir BU; conexões precisam de identidade própria e cardinalidade explícita. Migrações não podem apenas acrescentar INSTAGRAM ao enum. |
| mesmo schema: Conversation.contact E.164/grupo e unique(buId,contact) | substituir significado ambíguo por identidade local/externa qualificada, preservando conversas existentes e unicidade. |
| `api-app/src/domain/channels/transport/channel.ts`: Channel/ChannelResolver/ChannelOrigin/recipientRef | preservar o envio abstrato e evoluir contexto/seleção/capacidades sem segredo ou protocolo no negócio. |
| `api-app/src/integrations/channels/prisma-channel-resolver.ts`: selectCandidate por latest.channelOrigin e channels.find(type) | tipo sozinho passa a ser insuficiente; rota e vínculo exatos devem comandar a resolução. |
| `api-app/src/domain/inbox/incoming.service.ts`: MensagemRecebida.contato e TypebotSession por bot/BU/contato | normalização de ingresso e consumidores de identidade precisam de contrato; não ativar automação Instagram por acidente. |
| `api-app/src/domain/inbox/outbound.service.ts` e `initial-message.service.ts`: conversation.contact como recipientRef, snapshots/contextos duráveis e janela oficial | manter único sender/admissões; separar identidade e endereço de envio, preservar recuperação e aplicar política da capacidade correta. |
| `web-app/src/telas/Numeros.tsx`: BU=número, rótulos binários; `componentes/NovaConversa.tsx`: abertura por telefone; `api.ts`: DTOs de telefone/contato | rever cadastro/apresentação das conexões e referências de contato no futuro TODO; preservar o percurso WhatsApp atual, sem habilitar prospecção Instagram por username. |
| `foundation_documentation/domain_entities.md`, constituição, política de escopo e módulos | alvo de consolidação documental antes de o contrato de código ser aprovado; não declarar implementação por atualização de texto. |

## Validação que o contrato deve exigir

- WhatsApp oficial/não oficial do mesmo recurso/peer preservam a conversa e os IDs históricos. Importação dos dados atuais não inventa origem ou identidade quando faltar evidência; ambiguidades precisam de disposição explícita.
- Cutover abrange intenções/admissões persistidas e seus snapshots, além de mensagens e conversas: definir compatibilidade ou disposição explícita do contexto antigo e preservar conclusão local de envios já aceitos, sem repetir HTTP. Não deduzir rota histórica de `BU.phone` ou do primeiro vínculo disponível. Conflitos empresariais legados entre BUs precisam de inventário seguro e resolução humana; não mover dados silenciosamente.
- Mesmo valor textual de ID em WhatsApp, Instagram e duas contas Instagram não une interlocutores indevidamente. Username alterado não cria nem redireciona contato.
- Entrada duplicada/concorrente produz uma aceitação, sem segunda conversa, unread ou publicação por perdedor. Deduplicação segue por recurso de provedor/mensagem; conta igual com credencial renovada mantém identidade.
- Dois canais ou contas na mesma BU não trocam destinatários; duas BUs/tenants não compartilham histórico, grants, tokens ou rotas. Troca de BU e respostas atrasadas na UI falham fechadas.
- Falha/revogação/rotação de credencial, remoção do vínculo e reautorização respeitam geração e propriedade durável; não há fallback de canal nem retry externo ambíguo.
- Prova real: DM Instagram → Atendimento → resposta recebida; depois retomada. Repetir prova de envio/entrada dos dois WhatsApps. Contratos comuns precisam de teste de substituição do Channel, além dos testes específicos de adapter.
- Cardinalidade ampliada exige índices/unicidade e resolução em lote por vínculo/rota, sem HTTP por conversa na listagem. Catálogos/opções de conexões terão limite e paginação explícitos; não truncar silenciosamente os dez primeiros vínculos nem introduzir varredura ilimitada.

## Próximos passos e incertezas

1. Parecer independente concluído; achados incorporados abaixo. A escolha humana de BU conjunta já foi confirmada; parecer não concede aprovação humana das demais decisões nem de código.
2. A decisão de BU operacional e sua consolidação pertencem ao [registro de decisões](../../decisions/leadshug-multichannel-identity-decisions.md). Identidade de contato, ownership empresarial e rota estão propostas para validação no contrato. Elaborar o TODO com fronteira e sequência revisáveis, sem iniciar migração, runtime ou mudanças Meta.
3. Verificar Instagram Login, elegibilidade do app/conta, permissões, callback e regras específicas com documentação primária e painel. O fluxo de WhatsApp existente não prova esses requisitos.

Riscos restantes: migração de contatos legados sem proveniência completa; extensão de autorização/cadastro/API pública/Typebot; semântica de janela e IDs do fluxo Meta escolhido. Confiança alta na separação BU/conexão/identidade; desenho físico, endpoints e limites operacionais ainda precisam do TODO. Nenhuma promessa de suporte a usuários externos, App Review ou produção nesta definição.

## Parecer independente

Parecer terminal de `/root/instagram_identity_opinion`, em2026-10-23, sem histórico da conversa, leitura estática delimitada e sem mutações. Roteamento conferido com `agent_role_routing_guard.py`: codex, formal-review, architecture_opinion, gpt-6.1-sol, xhigh, declared; resultado go. Não equivale ao Plan Review Gate, ao parecer de um futuro TODO ou à autorização de implementação.

| Finding | Severidade e evidência | Disposição pela análise principal |
| --- | --- | --- |
| IG-REV-01 | Alta: exclusividade empresarial transversal não estava explícita; schema atual unique(provider,externalResourceId) não a prova | Integrated: owner durável por recurso empresarial atravessa adapters; claim atômico, falha fechada e conflito legado explícitos em cardinalidade/validação. |
| IG-REV-02 | Média: identidade empresarial e identidade de provedor podiam ser confundidas; schema/ChannelResolver usam phoneNumberId ou instância por adapter | Integrated: conceitos separados; IDs, ownership e dedup históricos conservados, sem dedup cruzado por coincidência textual. |
| IG-REV-03 | Média: cutover precisa incluir intenções/admissões e snapshots, não só mensagens | Integrated como requisito do futuro TODO: compatibilidade/disposição dos contextos e recuperação local dos aceitos, sem derivar rota histórica ou reenviar. |
| IG-REV-04 | Baixa: cardinalidade ampliada pode introduzir fan-out e truncamento; opções atuais limitam dez vínculos | Integrated como requisito do futuro TODO: batch, índices, paginação/limites explícitos e nenhum HTTP por conversa da lista. |

Posições do parecer: performance viável com índices e unicidade, sem medições nesta etapa; simplicidade/elegância favoráveis, sem tabela de rota ou framework genérico obrigatórios; estrutura sólida após as duas clarificações de identidade/ownership; operação humana DM/resposta bem delimitada. As duas lacunas que impediam consolidar a proposta foram resolvidas documentalmente acima. Nenhum achado foi renomeado como prova de implementação ou dispensado.
