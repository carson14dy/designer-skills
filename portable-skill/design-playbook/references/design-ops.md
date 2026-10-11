# design-ops

Ship: handoff, QA, review, sprints, debt, impact.

Streamline design operations with critique frameworks, handoff specs, sprint planning, review processes, and team workflows.

Each row is one skill. The description is what the skill produces, when to use it, and the boundary against its nearest neighbour; the trigger column is the clause to match against the situation in front of you. Read the source file before applying the skill: it holds the rules, numbers, tables, and the "do not" lines that the description only points at.

| Skill | Reach for it | Description | Source |
| --- | --- | --- | --- |
| `design-critique` | Use when running a session with people in the room | Facilitate a structured team critique — framing, feedback rules, and actionable outcomes. Use when running a session with people in the room. For a solo expert review, use `heuristic-evaluation` (prototyping-testing). | `source/design-ops/design-critique.md` |
| `design-debt-audit` | Use when drift has built up over time | Inventory and prioritise accumulated design inconsistencies across a product. Use when drift has built up over time. For token coverage specifically use `design-token-audit` (designer-toolkit); for WCAG gaps use `accessibility-audit` (design-systems). | `source/design-ops/design-debt-audit.md` |
| `design-impact-reporting` | Use when reporting results upward | Communicate design's contribution to business and user outcomes in stakeholder language. Use when reporting results upward. For choosing the metrics in the first place, use `metrics-definition` (ux-strategy). | `source/design-ops/design-impact-reporting.md` |
| `design-qa-checklist` | Use at implementation review | Build a QA checklist for verifying that a build matches the design. Use at implementation review. For the spec engineers build from, use `handoff-spec`. | `source/design-ops/design-qa-checklist.md` |
| `design-review-process` | Use when work ships without consistent review | Establish review gates — criteria, checkpoints, and approval flow. Use when work ships without consistent review. For running one individual session, use `design-critique`. | `source/design-ops/design-review-process.md` |
| `design-sprint-plan` | Use when compressing discovery into days | Plan and facilitate a design sprint from challenge framing through prototype testing. Use when compressing discovery into days. For ongoing team cadence, use `team-workflow`. | `source/design-ops/design-sprint-plan.md` |
| `handoff-spec` | Use when engineering picks up the work | Write the implementation handoff — measurements, behaviours, assets, states, and edge cases. Use when engineering picks up the work. For verifying the result afterwards use `design-qa-checklist`; for reusable library components use `component-spec` (design-systems). | `source/design-ops/handoff-spec.md` |
| `team-workflow` | Use when the day-to-day cadence needs structure | Design the team's operating rhythm — task management, collaboration rituals, and tooling. Use when the day-to-day cadence needs structure. For a time-boxed sprint, use `design-sprint-plan`. | `source/design-ops/team-workflow.md` |
| `version-control-strategy` | Use when file history is chaotic | Define version control for design files, components, and libraries — branching, naming, and release. Use when file history is chaotic. For design system contribution rules, use `design-system-governance` (design-systems). | `source/design-ops/version-control-strategy.md` |

## Workflows in design-ops

Full steps in `workflows.md`.

- `/design-ops:handoff`: Run the full handoff workflow — specs, measurements, assets, states, and a QA checklist — and output a developer-ready package.
- `/design-ops:plan-sprint`: Run a design sprint end to end — challenge framing, schedule, exercises, and prototype test plan.
- `/design-ops:setup-workflow`: Set up a team's operating rhythm end to end — rituals, task flow, tooling, review gates, and version control.
