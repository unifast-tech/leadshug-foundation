# TODO — Foundation lifecycle structural validator

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`

## Context

O lifecycle da Foundation exige um validator permanente quando backlog, decisões e roadmap ultrapassarem dez registros vivos combinados ou quando houver recorrência comprovada de drift. O ST-01 consolidou 18 registros vivos — três candidatos, onze decisões e quatro linhas de roadmap — e acionou o primeiro limiar.

## Framing Source & Story Slice

- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `n/a`
- **Why this is the right current slice:** materializar o follow-up obrigatório de D-09 sem ampliar nem implementar o validator dentro do ST-01.
- **Direct-to-TODO rationale:** o gatilho e o owner já estão definidos no [lifecycle](../../../evolution_lifecycle.md); este documento apenas abre o contrato separado exigido pelo limiar.

## Contract Boundary

- Este TODO está em `Review` e não possui autoridade de execução.
- Qualquer implementação exige refinamento completo, decisões validadas, `APROVADO` explícito e authority guard `go`.
- O validator deverá proteger schemas, IDs, owner singular, handoffs, eficácia de decisões e links sem se tornar uma segunda fonte de verdade.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Tactical TODO lifecycle state:** `Review`
- **Qualifiers:** `none`
- **Next exact step:** refinar o contrato e as opções de adoção do validator, então submetê-las à validação humana antes de qualquer execução.

## Active Work State

- **Work state:** `review`
- **Why this state now:** o limiar determinístico foi atingido, mas escopo, integração e comandos do validator ainda precisam de decisão própria.
- **Exit condition:** contrato completo e aprovado ou cancelado pela autoridade humana com racional explícito.

## Trigger Evidence

- **Trigger:** mais de dez registros vivos combinados em backlog, decisões e roadmap.
- **Observed count:** `18` em 2026-09-23 (`3` candidatos + `11` decisões Accepted + `4` linhas de roadmap).
- **Source:** [ST-01 D-09](../../completed/process/TODO-leadshug-foundation-evolution-lifecycle.md) e [Deterministic-adoption trigger](../../../evolution_lifecycle.md#deterministic-adoption-trigger).
- **Execution authority:** `none`; abertura do TODO não equivale a `APROVADO`.

## Scope

- [ ] Definir o contrato do validator permanente e sua superfície de execução.
- [ ] Tornar reproduzíveis as proteções estruturais hoje mantidas nos exact checks do ST-01.
- [ ] Definir adoção, ownership, evidência e integração com os gates da Foundation.

## Out of Scope

- [ ] Implementar o validator antes de aprovação própria.
- [ ] Alterar código, runtime, CI/CD ou contratos de produto do LeadsHug.
- [ ] Reabrir ou reescrever decisões D-01..D-11 do ST-01.

## Definition of Done

- [ ] Contrato, decisões, diff expectation, validações e gates do validator estão completos e aprovados.
- [ ] Implementação futura prova detecção fail-closed dos invariantes canônicos sem duplicar estado vivo.

## Validation Steps

- [ ] Executar os guards e checks definidos após o refinamento e aprovação deste TODO.

## Approval

- **Approved by:** `pending`
- **Approval scope:** `pending`
- **Execution authority:** `not_granted`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** o gatilho foi acionado e o contrato separado aguarda refinamento e aprovação próprios.
- **Post-commit/push status:** `n/a — no implementation claim`
- **Next path/status action:** manter em `todos/active/process/` no estado `Review`; refinar e apresentar o contrato à autoridade humana antes de qualquer implementação.
