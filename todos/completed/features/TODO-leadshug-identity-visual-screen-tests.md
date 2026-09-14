# TODO - LeadsHug identity visual screen tests

## Approval
- **Approved by:** Gabriel / user - 2026-08-28
- **Approval scope:** tests for the post-onboarding identity visual screen and fields.
- Authority: delphi-ai executes and validates this TODO.

## Delivery Status Canon
- **Current delivery stage:** Complete
- Qualifiers: validated-local
- Next exact step: none; TODO closed after validation.

## Objective
Create tests for loading, editing, validation, persistence, authorization and visual update.

## Scope
- [x] Test OWNER and ADMIN access.
- [x] Test ATENDENTE restriction.
- [x] Test current logo, primary color, secondary color and theme loading.
- [x] Test logo upload and removal.
- [x] Test persistence of both colors and theme.
- [x] Test invalid format, file and contrast errors.
- [x] Test visual update after save and new login.
- [x] Test tenant isolation.

## Definition of Done
- [x] Unit/integration tests cover relevant states and contracts.
- [x] Playwright covers navigation and mutation with a real local backend.
- [x] task check passes.
- [x] Specific evidence matrix is filled.
- [x] Delphi guards pass before closeout.

## Rules Acknowledgement / Ingestion
| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | governs TODO execution | approved scope and evidence | closing without tests | run completion guards |
| `delphi-ai/rules/stacks/react/leadshug-frontend.md` | browser surface is tested | API boundary and user flow | mocked-only acceptance | Playwright required |

## Agent Routing Preflight
- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-5.6-terra
- **Selected effort:** medium
- **Proof mode:** declared
- Execution topology: primary-checkout-single-writer
- Writer scheduling policy: one writer in canonical checkout; reviewers read-only
- **Guard outcome:** go

## Local CI-Equivalent Suite Matrix
| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| API unit tests | backend contracts | task check | closeout | passed | 93 passed | complete |
| Web unit tests | screen behavior | task check | closeout | passed | 16 passed | complete |
| Hooks | repository guardrails | task check | closeout | passed | 56 passed | complete |
| Playwright E2E | real browser flow | Playwright identity grep | closeout | passed | 1 passed | backend port 3201 |

## Pipeline/Copilot P1/P2 Preflight
| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| Identity visual screen tests | P1/P2 preflight | n/a | task check and Playwright | no findings | no pipeline-specific P1/P2 surface applies locally |

## Rule-Spirit Anti-Pattern Hunt
| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| Mock-only acceptance | real backend required | passed | Playwright real local API | none | accepted |
| Unauthorized scope expansion | approved scope only | passed | identity screen, test and safeguard changes | none | accepted |
| Missing required tests | proportional coverage | passed | API, web, hooks and E2E | none | accepted |

## Completion Evidence Matrix
| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Scope | Test OWNER and ADMIN access. | automated | route/menu authorization and role guards | local | passed | |
| S02 | Scope | Test ATENDENTE restriction. | automated | route/menu authorization and role guards | local | passed | |
| S03 | Scope | Test current logo, primary color, secondary color and theme loading. | integration | identity screen GET onboarding | local | passed | |
| S04 | Scope | Test logo upload and removal. | integration | upload component and API validation | local | passed | |
| S05 | Scope | Test persistence of both colors and theme. | E2E | Playwright real API identity scenario | local | passed | |
| S06 | Scope | Test invalid format, file and contrast errors. | integration | API validation coverage | local | passed | |
| S07 | Scope | Test visual update after save and new login. | E2E | Playwright real API identity scenario | local | passed | |
| S08 | Scope | Test tenant isolation. | integration | authorization and scope suites | local | passed | |
| D01 | Definition of Done | Unit/integration tests cover relevant states and contracts. | suite | 93 API and 16 web tests passed | local | passed | |
| D02 | Definition of Done | Playwright covers navigation and mutation with a real local backend. | E2E | 1 Playwright test passed on port 3201 | local | passed | |
| D03 | Definition of Done | task check passes. | command | task check: 93 API, 16 web, 56 hooks | local | passed | |
| D04 | Definition of Done | Specific evidence matrix is filled. | document | this matrix | local | passed | |
| D05 | Definition of Done | Delphi guards pass before closeout. | guard | authority, completion and closeout guards | local | passed | |

## Next Action
None. Approved scope implemented and validated by delphi-ai.
