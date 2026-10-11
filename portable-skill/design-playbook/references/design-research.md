# design-research

Understand: users, context, and the problem as it actually is.

User research skills for designers: personas, empathy maps, journey maps, interview scripts, usability testing, card sorting, behavioural analytics, and reconciling data with research.

Each row is one skill. The description is what the skill produces, when to use it, and the boundary against its nearest neighbour; the trigger column is the clause to match against the situation in front of you. Read the source file before applying the skill: it holds the rules, numbers, tables, and the "do not" lines that the description only points at.

| Skill | Reach for it | Description | Source |
| --- | --- | --- | --- |
| `affinity-diagram` | Use when synthesising across multiple sessions or sources | Cluster many qualitative data points into themes and insight statements. Use when synthesising across multiple sessions or sources. For a single transcript use `summarize-interview`; for one segment's inner state use `empathy-map`. | `source/design-research/affinity-diagram.md` |
| `behavioural-analytics` | Use when handed product data you did not design and asked why people drop off | Read funnels, retention curves, and event data as a designer — separating a design problem from a tracking artefact. Use when handed product data you did not design and asked why people drop off. For choosing what to measure, use `metrics-definition` (ux-strategy); for running a controlled test, use `a-b-test-design` (prototyping-testing). | `source/design-research/behavioural-analytics.md` + `source/design-research/behavioural-analytics.evals.md` |
| `card-sort-analysis` | Use after running a sort study | Analyse open or closed card sort results into a proposed grouping and label set. Use after running a sort study. For turning that evidence into a full structure, use `information-architecture` (ux-strategy). | `source/design-research/card-sort-analysis.md` |
| `diary-study-plan` | Use when behaviour unfolds over days or weeks | Design a diary study — prompts, cadence, duration, participant criteria, and analysis frame. Use when behaviour unfolds over days or weeks. For a single-session study, use `usability-test-plan`. | `source/design-research/diary-study-plan.md` |
| `empathy-map` | Use when sharing user understanding quickly | Build a Says, Thinks, Does, Feels map for one user or segment. Use when sharing user understanding quickly. For a composite archetype with goals and behaviours use `user-persona`; for cross-session themes use `affinity-diagram`. | `source/design-research/empathy-map.md` |
| `interview-script` | Use before running interviews | Write a structured interview guide — warm-up, core exploration, and wrap-up. Use before running interviews. For analysing what comes back, use `summarize-interview`. | `source/design-research/interview-script.md` |
| `jobs-to-be-done` | Use when reframing decisions around motivation rather than features | Map functional, emotional, and social jobs with outcome expectations. Use when reframing decisions around motivation rather than features. For who the user is, use `user-persona`. | `source/design-research/jobs-to-be-done.md` |
| `journey-map` | Use when improving an existing experience | Map one persona's end-to-end experience with stages, touchpoints, emotions, and pain points. Use when improving an existing experience. For the multi-channel ecosystem use `experience-map` (ux-strategy); for screen-level paths use `user-flow-diagram` (prototyping-testing). | `source/design-research/journey-map.md` |
| `qual-quant-triangulation` | Use when behavioural data and research findings point different ways | Reconcile what the numbers say with what users say, and design the study that settles it rather than restates it. Use when behavioural data and research findings point different ways. For reading the data on its own, use `behavioural-analytics`; for synthesising interviews on their own, use `affinity-diagram`. | `source/design-research/qual-quant-triangulation.md` + `source/design-research/qual-quant-triangulation.evals.md` |
| `research-repository` | Use when the same research keeps getting redone | Build a repository that makes findings findable, reusable, and cumulative across teams. Use when the same research keeps getting redone. For synthesising one study, use `affinity-diagram`. | `source/design-research/research-repository.md` |
| `summarize-interview` | Use immediately after a session | Turn one interview transcript into themes, supporting quotes, and action items. Use immediately after a session. For synthesising many sessions at once, use `affinity-diagram`. | `source/design-research/summarize-interview.md` |
| `survey-design` | Use when you need quantitative breadth | Design unbiased survey instruments — question wording, scales, and sampling — to measure attitudes at scale. Use when you need quantitative breadth. For behavioural experiments, use `a-b-test-design` (prototyping-testing). | `source/design-research/survey-design.md` |
| `usability-test-plan` | Use when planning the study as a whole | Design a usability study — research questions, methodology, participant criteria, metrics, and facilitation guide. Use when planning the study as a whole. For writing the task scenarios inside it, use `test-scenario` (prototyping-testing). | `source/design-research/usability-test-plan.md` |
| `user-persona` | Use when decisions need a consistent user reference | Build research-grounded personas with goals, frustrations, and behavioural patterns. Use when decisions need a consistent user reference. For one session's emotional snapshot use `empathy-map`; for motivation framing use `jobs-to-be-done`. | `source/design-research/user-persona.md` |

## Workflows in design-research

Full steps in `workflows.md`.

- `/design-research:discover`: Run a full user research cycle — persona creation, empathy mapping, and journey mapping for a product or feature.
- `/design-research:interview`: Prepare an interview script or summarize an interview transcript into structured insights.
- `/design-research:synthesize`: Synthesize research data into affinity diagrams, themes, and actionable insights.
- `/design-research:test-plan`: Run the full usability study workflow — research questions, participant criteria, tasks, metrics, and facilitation guide.
