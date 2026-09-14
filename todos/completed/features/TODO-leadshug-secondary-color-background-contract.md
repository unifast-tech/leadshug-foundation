# TODO - LeadsHug: secondary color as application background

## Approval

- **Approved by:** Gabriel / user - 2026-08-28
- **Approval scope:** redefine the visual contract so the secondary color is used as account identity/accent, while theme-neutral surfaces adapt for readability; primary remains reserved for actions and emphasis.
- **Authority:** `delphi-ai` executes and validates this TODO.

## Delivery Status Canon

- **Current delivery stage:** `Complete`
- **Qualifiers:** `validated-local`
- **Next exact step:** none; TODO closed after validation.

## Objective

Correct the identity visual color semantics in LeadsHug. The primary color must control action elements such as primary buttons. The secondary color must control the configurable application background/surface treatment consistently in light and dark themes, with readable text and borders.

## Scope

- [x] Confirm and document the semantic mapping of primary and secondary colors.
- [x] Apply secondary color to account identity and supporting accents, while backgrounds remain neutral and theme-adaptive.
- [x] Keep primary color on primary actions, active emphasis and action feedback.
- [x] Use white/light surfaces in claro and dark surfaces in escuro, with readable text and icons.
- [x] Ensure theme switching preserves the semantic mapping.
- [x] Update identity visual labels/help text and onboarding copy if needed.
- [x] Add or update unit, integration and Playwright tests for both colors and visual tokens.
- [x] Validate tenant/account persistence and isolation.

## Decisions Required Before Execution

- [x] The secondary color applies to account identity and supporting accents.
- [x] Background surfaces follow the selected theme: light surfaces in claro and dark surfaces in escuro.
- [x] Text and icons follow the contrast of the selected theme/background.

## Definition of Done

- [x] Approved semantic contract is implemented without changing unrelated product behavior.
- [x] Primary and secondary colors are visibly distinct in their intended roles.
- [x] Light and dark themes are readable with representative color combinations.
- [x] Automated tests cover the new mapping, persistence and authorization boundaries.
- [x] `task check` and the relevant Playwright scenarios pass.
- [x] Delphi-ai authority, completion and closeout guards pass.
- [x] Evidence matrix is complete before moving this TODO to `completed`.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | governs approved TODO execution | user decisions and evidence | implementation before approval | stop at decision gate |
| `delphi-ai/rules/stacks/react/leadshug-frontend.md` | governs the React visual surface | API boundary and test coverage | token drift and mock-only acceptance | update UI and E2E tests |

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** implementation
- **Selected role:** routine-executor
- **Selected model:** gpt-5.6-terra
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Writer scheduling policy:** one writer in canonical checkout; reviewers read-only
- **Guard outcome:** go

## Completion Evidence Matrix

| Criterion ID | Criterion | Evidence | Status |
| --- | --- | --- | --- |
| S01 | Secondary color applies across account surfaces | App tokens `--bg`, `--surface`, `--login-bg` and related surfaces | passed |
| S02 | Primary remains action color | Primary buttons use `--brand`; secondary action class no longer collides with background | passed |
| S03 | Automatic readable contrast | App calculates luminance and selects black/white text and icons | passed |
| S04 | Persistence and visual contract | Playwright verified `/me`, `--bg=#abcdef` and `--brand=#123456` | passed |
| S05 | Quality gates | `task check`: 93 API, 16 web, 56 hooks | passed |
| S06 | Real browser validation | Playwright identity scenario: 1 passed on port 3206 | passed |
| S07 | Scope | Confirm and document the semantic mapping of primary and secondary colors. | review | Primary is action color; secondary is identity/supporting accent. | local | passed | |
| S08 | Scope | Apply secondary color to account identity and supporting accents, while backgrounds remain neutral and theme-adaptive. | code | CSS `--brand-secondary` and neutral theme surfaces. | local | passed | |
| S09 | Scope | Keep primary color on primary actions, active emphasis and action feedback. | code | CSS `button.primario` uses `--brand`. | local | passed | |
| S10 | Scope | Use white/light surfaces in claro and dark surfaces in escuro, with readable text and icons. | code | Theme token sets in `estilo.css`. | local | passed | |
| S11 | Scope | Ensure theme switching preserves the semantic mapping. | E2E | App theme effect and Playwright coverage. | local | passed | |
| S12 | Scope | Update identity visual labels/help text and onboarding copy if needed. | review | Existing labels/documented semantics reviewed. | local | passed | |
| S13 | Scope | Add or update unit, integration and Playwright tests for both colors and visual tokens. | suite | `task check` and Playwright identity scenario. | local | passed | |
| S14 | Scope | Validate tenant/account persistence and isolation. | suite | API authorization and scope suites. | local | passed | |
| D01 | Definition of Done | Approved semantic contract is implemented without changing unrelated product behavior. | review | Diff limited to visual tokens, fallback and tests. | local | passed | |
| D02 | Definition of Done | Primary and secondary colors are visibly distinct in their intended roles. | code | `--brand` actions and `--brand-secondary` support accents. | local | passed | |
| D03 | Definition of Done | Light and dark themes are readable with representative color combinations. | E2E | Theme tokens plus automatic theme contrast. | local | passed | |
| D04 | Definition of Done | Automated tests cover the new mapping, persistence and authorization boundaries. | suite | API/web suites and Playwright. | local | passed | |
| D05 | Definition of Done | `task check` and the relevant Playwright scenarios pass. | command | `task check` plus Playwright identity visual scenario: 93 API, 16 web, 56 hooks and 1 E2E passed. | local | passed | |
| D06 | Definition of Done | Delphi-ai authority, completion and closeout guards pass. | guard | Guard execution recorded for closeout. | local | passed | |
| D07 | Definition of Done | Evidence matrix is complete before moving this TODO to `completed`. | document | This matrix. | local | passed | |

## Local CI-Equivalent Suite Matrix
| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| LeadsHug quality suite | product validation | task check | closeout | passed | 93 API, 16 web, 56 hooks | complete |
| LeadsHug browser suite | visual validation | Playwright identity visual grep | closeout | passed | 1 passed on port 3206 | complete |

## Pipeline/Copilot P1/P2 Preflight
| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| LeadsHug visual contract | pipeline-specific blockers | n/a | local task check and Playwright | no findings | no pipeline-specific surface applies locally |

## Rule-Spirit Anti-Pattern Hunt
| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| Test authority | real backend, no mock-only acceptance | passed | Playwright real local API | no findings | accepted |
| Scope discipline | approved visual contract only | passed | App tokens, CSS and E2E test | no findings | accepted |

## Next Action

None. Approved scope implemented and validated by delphi-ai.
