# ux-strategy

Frame: the problem, the direction, and what matters.

Shape product direction through competitive analysis, design principles, experience mapping, and strategic alignment.

Each row is one skill. The description is what the skill produces, when to use it, and the boundary against its nearest neighbour; the trigger column is the clause to match against the situation in front of you. Read the source file before applying the skill: it holds the rules, numbers, tables, and the "do not" lines that the description only points at.

| Skill | Reach for it | Description | Source |
| --- | --- | --- | --- |
| `business-design` | Use when defending design to commercial stakeholders | Read financials, map competitive landscapes, and argue design decisions in the language of value. Use when defending design to commercial stakeholders. For the live negotiation itself, use `design-negotiation` (designer-toolkit). | `source/ux-strategy/business-design.md` |
| `competitive-analysis` | Use when you need to know what others actually do | Compare UX patterns, features, strengths, and gaps across rival products. Use when you need to know what others actually do. For deliberately adopting their conventions, use `jakobs-law` (interaction-design). | `source/ux-strategy/competitive-analysis.md` |
| `content-strategy` | Use when content itself is the problem | Define what content a product needs, how it is structured, and who owns it. Use when content itself is the problem. For the words in the interface use `ux-writing` (designer-toolkit); for structural hierarchy use `information-architecture`. | `source/ux-strategy/content-strategy.md` |
| `design-brief` | Use at kickoff for one specific project | Write a project brief — problem space, constraints, audience, and success criteria. Use at kickoff for one specific project. For long-horizon aspiration use `north-star-vision`; for reusable decision rules use `design-principles`. | `source/ux-strategy/design-brief.md` |
| `design-principles` | Use when the same decisions keep getting relitigated | Define actionable principles that resolve trade-offs when the team disagrees. Use when the same decisions keep getting relitigated. For a single project's framing, use `design-brief`. | `source/ux-strategy/design-principles.md` |
| `experience-map` | Use when the experience spans more than one product | Map the full ecosystem of touchpoints, channels, and relationships across a service. Use when the experience spans more than one product. For one persona's linear journey use `journey-map` (design-research); for backstage operations use `service-blueprint`. | `source/ux-strategy/experience-map.md` |
| `information-architecture` | Use when organising what exists | Design content structure, hierarchy, labelling, and the navigation model. Use when organising what exists. For the UI that exposes it use `navigation-patterns` (interaction-design); for user-generated grouping evidence use `card-sort-analysis` (design-research). | `source/ux-strategy/information-architecture.md` |
| `metrics-definition` | Use when choosing what to measure | Define UX metrics and KPIs that connect design decisions to measurable outcomes. Use when choosing what to measure. For presenting the results afterwards, use `design-impact-reporting` (design-ops). | `source/ux-strategy/metrics-definition.md` |
| `north-star-vision` | Use when direction is contested or absent | Articulate a long-horizon product vision that aligns teams and anchors strategy. Use when direction is contested or absent. For near-term project scope, use `design-brief`. | `source/ux-strategy/north-star-vision.md` |
| `opportunity-framework` | Use when there are more ideas than capacity | Identify, score, and prioritise design opportunities against impact and effort. Use when there are more ideas than capacity. For framing the one you choose, use `design-brief`. | `source/ux-strategy/opportunity-framework.md` |
| `service-blueprint` | Use when staff and operations are part of the experience | Map service delivery across frontstage actions, backstage processes, and supporting systems. Use when staff and operations are part of the experience. For the customer-visible layer only, use `experience-map`. | `source/ux-strategy/service-blueprint.md` |
| `stakeholder-alignment` | Use when unclear ownership stalls decisions | Build alignment artifacts — responsibility matrices, decision rights, and communication plans. Use when unclear ownership stalls decisions. For persuading in the moment, use `design-negotiation` (designer-toolkit). | `source/ux-strategy/stakeholder-alignment.md` |

## Workflows in ux-strategy

Full steps in `workflows.md`.

- `/ux-strategy:benchmark`: Run a competitive benchmark across a set of products — pattern comparison, gap analysis, and opportunity callouts.
- `/ux-strategy:frame-problem`: Structure an ambiguous design challenge into a clear problem definition with constraints and criteria.
- `/ux-strategy:strategize`: Develop a complete UX strategy for a product or feature area.
