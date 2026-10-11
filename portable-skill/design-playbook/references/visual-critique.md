# visual-critique

Validate by eye: the seven screen critiques.

Visual critique skills for designers. Analyse a screen across seven dimensions — hierarchy, brand consistency, composition, typography, colour, affordance, and information density — then compile a prioritised fix list.

Each row is one skill. The description is what the skill produces, when to use it, and the boundary against its nearest neighbour; the trigger column is the clause to match against the situation in front of you. Read the source file before applying the skill: it holds the rules, numbers, tables, and the "do not" lines that the description only points at.

| Skill | Reach for it | Description | Source |
| --- | --- | --- | --- |
| `critique-affordance` | Use when reviewing an existing screen | Critique a rendered screen's affordances — what looks clickable, state visibility, CTA clarity, and action discoverability. Use when reviewing an existing screen. For sizing and positioning targets in new work, use `fitts-law` (interaction-design). | `source/visual-critique/critique-affordance.md` |
| `critique-brand-consistency` | Use when those brand files exist and you are checking compliance | Critique a rendered screen against mood.md, voice.md, and tokens.md. Use when those brand files exist and you are checking compliance. For defining the visual language itself, use `illustration-style` (ui-design). | `source/visual-critique/critique-brand-consistency.md` |
| `critique-color` | Use when reviewing one screen | Critique a rendered screen's colour — contrast ratios, palette coherence, and semantic meaning. Use when reviewing one screen. For a product-wide WCAG audit use `accessibility-audit` (design-systems); for building the palette use `color-system` (ui-design). | `source/visual-critique/critique-color.md` |
| `critique-composition` | Use when a layout feels off but hierarchy is fine | Critique a rendered screen's composition — balance, whitespace, rhythm, and gestalt grouping. Use when a layout feels off but hierarchy is fine. For emphasis and eye flow specifically, use `critique-visual-hierarchy`. | `source/visual-critique/critique-composition.md` |
| `critique-information-density` | Use when a screen feels overwhelming | Critique a rendered screen's density — cognitive load, content prioritisation, scanning patterns, and progressive disclosure. Use when a screen feels overwhelming. For the underlying choice-count principle, use `hicks-law` (interaction-design). | `source/visual-critique/critique-information-density.md` |
| `critique-typography` | Use when reviewing type on a screen | Critique a rendered screen's typography — scale usage, readability, consistency, and token compliance. Use when reviewing type on a screen. For defining the scale itself, use `typography-scale` (ui-design). | `source/visual-critique/critique-typography.md` |
| `critique-visual-hierarchy` | Use when attention lands in the wrong place | Critique a rendered screen's hierarchy — entry point, eye flow, weight distribution, and emphasis. Use when attention lands in the wrong place. For establishing hierarchy in new work, use `visual-hierarchy` (ui-design). | `source/visual-critique/critique-visual-hierarchy.md` |

## Workflows in visual-critique

Full steps in `workflows.md`.

- `/visual-critique:critique-screen`: Run all seven visual critiques on a screen and output a prioritised fix list.
- `/visual-critique:critique-ux`: Run a focused UX critique on a screen — affordances, information density, and hierarchy — and output a prioritised fix list.
