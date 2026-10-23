# Module: Identity and Tenancy
**Version:** 1.0

Owns authentication, accounts, Mantenedoras, Setores, Business Units, roles and BU grants.

## Invariants

- Every request resolves one tenant/account context.
- Permissions are materialized at the BU boundary.
- Roles are `OWNER`, `ADMIN` and `ATENDENTE`.

## API Endpoint Definitions

The canonical BFF contracts live under `api-app` and must be documented here before new endpoints
are introduced.

## BU operacional multicanal — arquitetura alvo

Conforme [DEC-bu-operational-multichannel](../decisions/leadshug-multichannel-identity-decisions.md), confirmada pelo usuário em2026-10-23, a BU identifica a operação de atendimento, não o número WhatsApp. Contas/perfis e números pertencem às conexões dos canais. A mesma BU reúne WhatsApp e Instagram com os mesmos vendedores e grants; não criar outra identidade organizacional para representar um transporte.

Tenancy continua sendo o owner de Mantenedora, Setor, BU e grants. Canais possui os vínculos de integração; Inbox possui contatos e conversas. Nenhuma conexão concede grant por si só. O produto atual não foi migrado: os endpoints e o cadastro ST-CON-01 abaixo continuam sendo os contratos WhatsApp entregues. Contrato de identidade multicanal, mudanças de schema e adoção Instagram precisam de TODO/revisão/aprovação próprios; o parecer de arquitetura não é aprovação de execução.


## Autorização do cadastro de números ST-CON-01

APROVADO em2026-10-15; implementação exercitada localmente em2026-10-16 ([all499/22migrações e fonte/freshness](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp27-receipt.json)); architecture/security, Performance/cutover e TQA independentes aceitos no escopo local. Final review local aceito; source commits/bridge byteexact registrados, prova externa local dos dois canais concluída CP106-108; encerramento local concluído CP108 no TODO no [TODO](../todos/completed/features/TODO-leadshug-channel-connection-readiness.md). Jornada e endpoints pertencem ao [owner de canais](integrations-and-channels.md#cadastro-de-números-st-con-01).

- Endpoints /api/bff/number-registrations e pairing/verificação de canal passam pelo middleware de sessão e anti-CSRF existente; pairing é POST, GET antigo não tem efeito externo.
- Conectar/reautorizar BU existente exige ADMIN na BU da Mantenedora verificada; criar BU exige ADMIN na Mantenedora e reutiliza transação/expansão de grants de TenancyService. ATENDENTE não ganha gestão por UI.
- Validar permissão antes de revelar estado ou erro de payload: sem sessão401, recurso fora do contexto404, papel insuficiente403. Revalidar grant/sessão após HTTP antes de ativar candidata ou promover observação.
- Tentativa oficial liga usuário/Mantenedora/BU/hash de sessão/nonce com expiração10min e consumo CAS; code/nonce consumidos ou ambíguos exigem tentativa nova. SDK IDs são candidatos, nunca autoridade.
- Nova BU, reserva/tentativa e grants/audit são atômicos. Mesmo Idempotency-Key e payload devolvem a mesma tentativa; payload diferente409; reautorização usa slot existente e expectedGeneration.
- ProviderResourceIdentity conserva owner de BU após remoção de canal e não é transferível entre BUs neste recorte. Webhooks têm autenticação própria e só passam conteúdo após identidade corrente comprovada.

## Ownership multicanal aprovado — ST-IG-03

Arquitetura aprovada em2026-10-23 no [contrato v1.3](../todos/active/features/TODO-leadshug-instagram-channel.md), implementação em curso. Tenancy continua dona da BU e grants; Inbox possui contato/conversa/rota; Canais possui conexão, credencial e identidades empresarial/provedor.

O recurso empresarial qualificado conserva owner de BU após desconexão e atravessa adapters comprovados. Não vincular o mesmo número por oficial na BU A e Evolution na BU B. Claim e associação são atômicos; conflito falha fechado sem revelar outro tenant. Uma BU admite um recurso WhatsApp durável e múltiplas contas Instagram nesta fatia; múltiplos números WhatsApp exigem contrato próprio. Trocar a credencial não troca recurso ou owner. Nenhuma conexão cria permissões além dos grants existentes.

Os endpoints legados de BU mantêm sua projeção de canais apenas nos dois bindings WhatsApp compatíveis do recurso único; o catálogo Instagram é paginado e pertence a Canais. Não usar disponibilidade para esconder ambiguidade nem hidratar todos os perfis na lista de BUs.
