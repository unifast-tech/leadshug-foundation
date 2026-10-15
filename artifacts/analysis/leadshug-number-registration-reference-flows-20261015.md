# Cadastro de números — fluxos de referência para o LeadsHug

**Data:** 2026-10-15. **Natureza:** leitura estática sanitizada; proposta de experiência, sem implementação autorizada.

## Correção do objetivo

O usuário esclareceu: “Eu estava falando sobre os processos de cadastros dos números que são API ofc e não oficial nos sitemas para reprodurzimos”. O objetivo imediato é reproduzir a jornada de cadastro/conexão. Diagnóstico é apoio à conclusão dessa jornada; importação de histórico não é pré-requisito dela. Local primeiro e Railway depois continuam confirmados.

## Oficial — Central-Whatsapp

Snapshot `337f3e4839cef8ca400de87b3de088a79d512944`, somente leitura.

1. Administrador abre a gestão de contas/números.
2. Quando a instalação tem configuração Meta para onboarding, aparece **Conectar pela Meta**.
3. O navegador abre Embedded Signup. A própria janela Meta conduz escolha/criação de conta e número e autorização.
4. A tela recebe código de autorização e IDs de WABA/número; encaminha ao backend.
5. Backend troca código por token, identifica o número e cria/completa o vínculo.
6. Backend tenta assinar o app na WABA e configurar o recebimento para a instalação. O resultado de recebimento é devolvido separadamente; a UI avisa quando o cadastro aconteceu mas o recebimento falhou.
7. A lista mostra o número cadastrado. Existe também caminho manual administrativo com nome e WABA ID; o botão automático fica oculto sem configuração Meta.

Evidências: `public/index.html:1335-1349` (telas e modo manual), `3154-3239` (janela/code/IDs/feedback); `src/index.js:2732-2818` (troca e cadastro), `6297-6365` (recebimento). São comportamentos do snapshot, não especificação atual da Meta ou comprovação de saúde externa.

## Não oficial — Hub/Central-Whatsapp

Snapshot `51bc16e544c7625a71c3012d8adef656c6392c37`, somente leitura.

1. Operador com permissão de gerenciar números informa **apelido do número**, por exemplo Atendimento.
2. Clica em **Adicionar número**. Backend cria a instância na Evolution e registra o vínculo em estado connecting.
3. Backend tenta configurar webhook; a tela recebe e apresenta QR. Nome técnico e credencial do servidor são responsabilidade da aplicação.
4. Operador abre WhatsApp no celular, acessa **Aparelhos conectados** e lê o QR.
5. Evento de conexão atualiza número/estado; a atualização chega à interface e remove o QR usado.
6. Se necessário, há ações explícitas de mostrar/renovar QR, desconectar, renomear e excluir.
7. **Importar conversas** é ação separada, após conexão; não confundir cadastro concluído com histórico importado.

Evidências: `frontend/src/pages/Numeros.tsx:40-81,178-186,217-270`; `backend/src/modules/instances/routes.ts:40-72,88-121`; `backend/src/evolution-client/instances.ts:14-40`; `backend/src/modules/webhooks/routes.ts:80-99`.

## WhatsFlow — experiência alternativa

Snapshot `3a36436c83ebefc6839380eb8fac1a6f13f4700a`, somente leitura.

O caminho Uazapi possui criação por nome da conexão e abre o modal de QR; também admite código de pareamento. Confirmação acompanha realtime e consulta periódica enquanto aguarda. Há ainda formulário genérico de provedores com label, token e URL/IDs conforme adapter; essa é uma experiência de configuração técnica, não precisa ser exigida do operador comum do LeadsHug.

Evidências: `src/components/mensageria/UazapiInstancesTab.tsx:104-138,220-242`; `UazapiQRCodeModal.tsx:74-109,145-181`; `NewConnectionModal.tsx:118-180`. A leitura não estabelece que todos esses caminhos estejam ativos ou saudáveis em produção.

## Jornada proposta para o LeadsHug

| Escolha | Operador informa/faz | Aplicação resolve | Conclusão visível |
| --- | --- | --- | --- |
| Oficial | Apelido/BU e autorização/escolha do número na janela Meta. | Contexto de sessão/BU, troca segura, identidade do número, vínculo e recebimento. | Número identificado; autorização/cadastro e recebimento com resultados explícitos. |
| Não oficial | Apelido/BU; lê QR pelo celular. | Criação da instância própria, webhook, telefone confirmado e acompanhamento do pareamento. | Número identificado e conectado; QR usado encerrado. |

Usar a linguagem e o fluxo como referência. Não copiar fontes, schema, configuração, credenciais ou infraestrutura. Não reproduzir seleção silenciosa do primeiro número, exposição de token ao cliente, falha escondida de webhook ou alteração de callback de outro sistema sem confirmação explícita. Cadastro oficial automatizado e configuração de credenciais por conta exigem desenho/revisão próprios antes de implementação.

Contrato candidato: [TODO de cadastro e conexão](../../todos/active/features/TODO-leadshug-channel-connection-readiness.md). A disponibilidade de números oficiais/não oficiais para teste está confirmada; configuração do app Meta e versão da Evolution permanecem decisões técnicas abertas, sem novo pedido de prioridade ao usuário.
