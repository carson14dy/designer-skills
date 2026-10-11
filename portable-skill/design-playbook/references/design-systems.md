# design-systems

Systematise: tokens, components, and the rules that keep them coherent.

Build, document, and maintain scalable design systems — from tokens and components to accessibility and theming.

Each row is one skill. The description is what the skill produces, when to use it, and the boundary against its nearest neighbour; the trigger column is the clause to match against the situation in front of you. Read the source file before applying the skill: it holds the rules, numbers, tables, and the "do not" lines that the description only points at.

| Skill | Reach for it | Description | Source |
| --- | --- | --- | --- |
| `accessibility-audit` | Use when you have a design or build to assess now | Audit an existing interface against WCAG, producing findings with severity ratings and remediation steps. Use when you have a design or build to assess now. Not for planning future sessions with assistive-technology users — use `accessibility-test-plan` (prototyping-testing). | `source/design-systems/accessibility-audit.md` |
| `component-spec` | Use when defining a library component | Specify one component — props, states, variants, accessibility, and usage rules. Use when defining a library component. For the reusable doc scaffold use `documentation-template`; for a problem-solution pattern use `pattern-library`. | `source/design-systems/component-spec.md` |
| `design-system-governance` | Use when multiple teams contribute | Define how the system evolves — contribution model, versioning, deprecation, and change management. Use when multiple teams contribute. For driving uptake use `design-system-adoption` (designer-toolkit); for design file history use `version-control-strategy` (design-ops). | `source/design-systems/design-system-governance.md` |
| `design-token` | Use when establishing the token layer | Define and organise tokens for colour, spacing, type, and elevation with naming and usage rules. Use when establishing the token layer. For auditing existing usage use `design-token-audit` (designer-toolkit); for multi-brand mapping use `theming-system`. | `source/design-systems/design-token.md` |
| `documentation-template` | Use when standardising how the system is documented | Generate a reusable documentation scaffold for components, patterns, or guidelines. Use when standardising how the system is documented. For the content of one component's spec, use `component-spec`. | `source/design-systems/documentation-template.md` |
| `icon-system` | Use when standardising iconography | Specify an icon system — grid, sizing, stroke weight, naming, categories, and implementation. Use when standardising iconography. For broader illustration, use `illustration-style` (ui-design). | `source/design-systems/icon-system.md` |
| `localization-design` | Use when shipping beyond one locale | Design for multiple languages, writing directions, and cultural contexts — text expansion, RTL mirroring, and locale formats. Use when shipping beyond one locale. For the words themselves, use `ux-writing` (designer-toolkit). | `source/design-systems/localization-design.md` |
| `motion-system` | Use when standardising motion across a system | Define motion tokens — durations, easing vocabulary, and reduced-motion handling — for consistency product-wide. Use when standardising motion across a system. For crafting one specific animation, use `animation-principles` (interaction-design). | `source/design-systems/motion-system.md` |
| `naming-convention` | Use when names are inconsistent or being set | Establish naming rules for components, tokens, and layers with patterns and worked examples. Use when names are inconsistent or being set. For what the tokens actually contain, use `design-token`. | `source/design-systems/naming-convention.md` |
| `pattern-library` | Use when documenting a recurring solution rather than a component | Structure a pattern entry — problem context, solution, usage examples, and related patterns. Use when documenting a recurring solution rather than a component. For a single component's API, use `component-spec`. | `source/design-systems/pattern-library.md` |
| `theming-system` | Use when one system must serve multiple themes | Design theming architecture — brand variants, dark mode, and high-contrast — mapped through token layers. Use when one system must serve multiple themes. For a single palette use `color-system` (ui-design); for dark mode craft use `dark-mode-design` (ui-design). | `source/design-systems/theming-system.md` |

## Workflows in design-systems

Full steps in `workflows.md`.

- `/design-systems:audit-system`: Run a comprehensive audit of an existing design system for consistency, completeness, and accessibility.
- `/design-systems:create-component`: Scaffold a full component specification end to end — props, states, variants, accessibility, and documentation.
- `/design-systems:tokenize`: Extract tokens from an existing design or stylesheet and organise them — naming, structure, and theme mapping.
