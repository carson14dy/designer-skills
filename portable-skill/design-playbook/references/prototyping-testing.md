# prototyping-testing

Explore and validate: concepts, prototypes, tests, experiments.

Plan and execute design validation through prototyping strategies, usability testing, heuristic evaluation, and A/B experiments.

Each row is one skill. The description is what the skill produces, when to use it, and the boundary against its nearest neighbour; the trigger column is the clause to match against the situation in front of you. Read the source file before applying the skill: it holds the rules, numbers, tables, and the "do not" lines that the description only points at.

| Skill | Reach for it | Description | Source |
| --- | --- | --- | --- |
| `a-b-test-design` | Use when a change can be measured quantitatively at scale | Design an A/B experiment — hypothesis, variants, primary metric, and sample size. Use when a change can be measured quantitatively at scale. For observing behaviour qualitatively, use `test-scenario`. | `source/prototyping-testing/a-b-test-design.md` |
| `accessibility-test-plan` | Use when scheduling testing with real AT users | Plan accessibility testing — assistive technologies, participant criteria, WCAG coverage, and session protocol. Use when scheduling testing with real AT users. Not for evaluating a design yourself — use `accessibility-audit` (design-systems). | `source/prototyping-testing/accessibility-test-plan.md` |
| `click-test-plan` | Use when testing whether people can locate something | Design first-click and click tests for findability and navigation. Use when testing whether people can locate something. For full task-based observation, use `test-scenario`. | `source/prototyping-testing/click-test-plan.md` |
| `concept-selection` | Use when several directions are alive and one has to win | Choose between competing concepts against criteria fixed in advance, and record what each rejected concept was testing. Use when several directions are alive and one has to win. For picking which problem to work on, use `opportunity-framework` (ux-strategy); for deciding by production traffic, use `a-b-test-design`. | `source/prototyping-testing/concept-selection.md` |
| `heuristic-evaluation` | Use when you need findings without recruiting participants | Run an expert review against Nielsen's heuristics and domain criteria, with severity ratings. Use when you need findings without recruiting participants. For a facilitated team feedback session, use `design-critique` (design-ops). | `source/prototyping-testing/heuristic-evaluation.md` |
| `parallel-concepts` | Use when one direction is on the table and the team is about to refine it by default | Build several genuinely different solutions to the same problem at once, spread across what the user does rather than how it looks. Use when one direction is on the table and the team is about to refine it by default. For choosing between the concepts afterwards, use `concept-selection`. | `source/prototyping-testing/parallel-concepts.md` |
| `prototype-strategy` | Use before building a prototype | Choose prototype fidelity and method to match the design question and the decision at stake. Use before building a prototype. For what to test once it exists, use `test-scenario`. | `source/prototyping-testing/prototype-strategy.md` |
| `test-scenario` | Use when you have a study and need the tasks | Write realistic usability task scenarios with success criteria and facilitation notes. Use when you have a study and need the tasks. For the surrounding study design, use `usability-test-plan` (design-research). | `source/prototyping-testing/test-scenario.md` |
| `user-flow-diagram` | Use when specifying how a feature is traversed | Diagram screen-level paths, decision points, and branch logic. Use when specifying how a feature is traversed. For the emotional end-to-end arc, use `journey-map` (design-research). | `source/prototyping-testing/user-flow-diagram.md` |
| `wireframe-spec` | Use when defining structure before visual design | Specify wireframe layout — content priority, component placement, and annotation. Use when defining structure before visual design. For grid mechanics, use `layout-grid` (ui-design). | `source/prototyping-testing/wireframe-spec.md` |

## Workflows in prototyping-testing

Full steps in `workflows.md`.

- `/prototyping-testing:evaluate`: Run a heuristic evaluation end to end — expert review against heuristics with severity ratings and recommended fixes.
- `/prototyping-testing:experiment`: Design an A/B experiment end to end — hypothesis, variants, primary metric, and sample size.
- `/prototyping-testing:explore-options`: Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record.
- `/prototyping-testing:prototype-plan`: Create a prototyping and testing plan for a design initiative.
- `/prototyping-testing:test-plan`: Choose a testing method and build the plan around it — method selection, task scenarios, click tests, and accessibility coverage.
