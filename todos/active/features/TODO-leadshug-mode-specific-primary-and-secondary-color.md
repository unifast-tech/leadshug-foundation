# TODO - LeadsHug: mode-specific primary and secondary colors

## Approval

- **Approved by:** pending user approval
- **Approval scope:** allow the account to configure a primary color for light mode and another for dark mode, remove the configurable secondary-color field, use fixed dark-theme color `#121212`, and preserve the current light-theme color.
- **Authority:** `delphi-ai` executes and validates this TODO.

## Delivery Status Canon

- **Current delivery stage:** `Not-Started`
- **Qualifiers:** `awaiting-approval`
- **Next exact step:** explicit user approval, then implement the approved contract.

## Objective

Improve LeadsHug branding flexibility by allowing the primary action color to vary by theme, while replacing the current secondary color that does not match the desired visual identity.

## Proposed Contract

- Primary color for light mode: configurable by the user for buttons, tabs, links and indicators.
- Primary color for dark mode: configurable by the user for buttons, tabs, links and indicators.
- The active theme selects the corresponding primary color for buttons, links and active indicators.
- Secondary/background color: fixed per theme and not user-configurable; dark theme uses `#121212`, light theme keeps the current system color.
- Text and icons must preserve readable contrast in both themes.
- Existing accounts must not lose their current branding during migration.

## Decisions Required Before Execution

- [x] Dark-theme secondary/background color is fixed as `#121212`.
- [x] Light-theme secondary/background color keeps the current system color.
- [x] Existing accounts follow the fixed per-theme colors.
- [x] The configurable secondary-color field is removed.
- [x] Existing primary color populates both new mode-specific primary fields initially.

## Scope

- [ ] Extend persistence and API contracts for primary light/dark colors.
- [ ] Add both primary color controls to onboarding and identity visual settings.
- [ ] Apply the active primary color according to the selected theme.
- [ ] Remove the secondary-color control and migrate all accounts to fixed `#121212`.
- [ ] Implement readable contrast for both theme-specific primary colors and the secondary color.
- [ ] Preserve backward compatibility for existing accounts.
- [ ] Add unit, integration and Playwright tests for all new fields and theme transitions.
- [ ] Update migration and deployment documentation.

## Definition of Done

- [ ] Decisions are approved and recorded.
- [ ] Light and dark modes use their configured primary colors.
- [ ] Secondary color uses the approved replacement value.
- [ ] Existing accounts remain valid and retain branding according to the approved migration decision.
- [ ] Automated tests cover persistence, authorization, theme switching and contrast.
- [ ] `task check` and relevant Playwright scenarios pass.
- [ ] Delphi-ai authority, completion and closeout guards pass.
- [ ] Evidence matrix is complete before closeout.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | governs TODO execution | user decisions and evidence | implementation before approval | stop at decision gate |
| `delphi-ai/rules/stacks/react/leadshug-frontend.md` | governs React visual behavior | API boundary and test coverage | theme-specific token drift | update UI and E2E tests |

## Agent Routing Preflight

- **Client surface:** codex
- **Current governed action:** planning
- **Selected role:** primary-chat
- **Selected model:** gpt-5.6-terra
- **Selected effort:** medium
- **Proof mode:** declared
- **Execution topology:** primary-checkout-single-writer
- **Writer scheduling policy:** one writer in canonical checkout; reviewers read-only
- **Guard outcome:** go after decisions and approval

## Next Action

Confirm the secondary color, migration behavior for existing accounts, inheritance behavior for primary colors, and then approve execution.
