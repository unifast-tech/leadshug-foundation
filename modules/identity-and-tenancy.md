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


## Autorização do cadastro de números ST-CON-01

APROVADO em2026-10-15; implementação exercitada localmente em2026-10-16 ([all499/22migrações e fonte/freshness](../artifacts/reviews/leadshug-number-onboarding-20261015/evidence/root-cp27-receipt.json)); architecture/security, Performance/cutover e TQA independentes aceitos no escopo local. Final review local aceito; source commits/bridge byteexact registrados, closeout geral e prova externa permanecem pendentes no TODO no [TODO](../todos/active/features/TODO-leadshug-channel-connection-readiness.md). Jornada e endpoints pertencem ao [owner de canais](integrations-and-channels.md#cadastro-de-números-st-con-01).

- Endpoints /api/bff/number-registrations e pairing/verificação de canal passam pelo middleware de sessão e anti-CSRF existente; pairing é POST, GET antigo não tem efeito externo.
- Conectar/reautorizar BU existente exige ADMIN na BU da Mantenedora verificada; criar BU exige ADMIN na Mantenedora e reutiliza transação/expansão de grants de TenancyService. ATENDENTE não ganha gestão por UI.
- Validar permissão antes de revelar estado ou erro de payload: sem sessão401, recurso fora do contexto404, papel insuficiente403. Revalidar grant/sessão após HTTP antes de ativar candidata ou promover observação.
- Tentativa oficial liga usuário/Mantenedora/BU/hash de sessão/nonce com expiração10min e consumo CAS; code/nonce consumidos ou ambíguos exigem tentativa nova. SDK IDs são candidatos, nunca autoridade.
- Nova BU, reserva/tentativa e grants/audit são atômicos. Mesmo Idempotency-Key e payload devolvem a mesma tentativa; payload diferente409; reautorização usa slot existente e expectedGeneration.
- ProviderResourceIdentity conserva owner de BU após remoção de canal e não é transferível entre BUs neste recorte. Webhooks têm autenticação própria e só passam conteúdo após identidade corrente comprovada.
